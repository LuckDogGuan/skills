# [Python Alpha 挑战赛] SKILL: Regular to Python Alpha ｜ 稳定转写Python Alpha经验分享

- **链接**: https://support.worldquantbrain.com[Commented] [Python Alpha 挑战赛] SKILL Regular to Python Alpha  稳定转写Python Alpha经验分享_41032955115927.md
- **作者**: AK76468
- **发布时间/热度**: 18天前, 得票: 86

## 帖子正文

# 把 Regular FastExpr 转成 Python Alpha：一个可复刻的 Codex Skill

这是一份公开版技术分享。目标不是展示某个 Alpha 的结果，而是把转换方法、源码、回测工具和案例沉淀流程放在一篇帖子里，别人可以按同一套规则复刻并继续迭代。

> **这个 skill 的特点：** 它不是一次性写出来的“转换提示词”，而是一套随着真实 Python Alpha 回测持续更新的转换工作流。每次回测失败、超时、指标偏离或平台拒绝提交，都会被归类到 casebook：是 operator 语义问题、NaN/窗口覆盖问题、computed intermediate 太重、store warm-up 差异、settings schema 差异，还是 Python Alpha 平台本身的限制。确认稳定复现后，再把经验沉淀回  `operator-semantics.md` 、 `verified-snippets.md`  和主  `SKILL.md` 。因此它的价值不只是“把表达式翻译成 Python”，而是把回测中踩过的坑变成下一次转换时自动遵守的规则。

**公开版说明：** 本文删除了原始工作区里的 平台私有标识、具体IS指标、个人案例标签和账号相关痕迹。那些内容不是 skill 运行依赖；读者可以用本文附带的 MCP 回测流程，在自己的表达式和平台账号上重新生成自己的 casebook。

[1. 为什么需要这个 skill](#why) 
 [2. Python Alpha 执行模型](#model) 
 [3. 转换工作流](#workflow) 
 [4. 公开版源码](#source) 
 [5. MCP Python 回测工具](#mcp)

[6. 如何继续沉淀案例](#casebook)

## 1. 为什么需要这个 skill

Regular FastExpr 和 Python Alpha 的目标都可以是同一个信号，但执行模型并不一样。直接把操作符名机械翻译成 NumPy，经常会遇到三类问题：

- **语义不等价：** FastExpr 操作符的 NaN、窗口、rank、group、state 行为不总是等于简单 NumPy reducer。
- **平台不可运行：** 在 Python Alpha 里每天重建长历史 computed intermediate，语义上好看，但平台执行成本可能过高。
- **回测设置不同：** Regular 返回的部分 settings 不一定能原样用于 Python submit。

这个 skill 的核心原则是：优先保留 FastExpr 语义，遇到平台执行模型冲突时，选择可运行且可解释的实现，并把 warm-up、近似点和风险写进 Notes。

## 2. Python Alpha 执行模型

**关键模型：** BRAIN 会按时间逐日调用 Python Alpha。每个声明的数据字段是形如  `[available_history, n_instruments]`  的只读数组；最新一天是  `data.field[-1]` 。函数只返回今天的一维  `np.float32`  信号。

问题
推荐处理

raw field 的时间序列操作
优先使用  `data.field[-d:]` ，但仍需确认 operator 语义，不默认等价于  `np.nanmean`  等。

computed intermediate 的时间序列操作
默认使用 typed  `store`  每天缓存一行，再对缓存做外层时间序列操作。

vector field 或  `vec_*` 

Python Alpha 平台不支持，停止转换，不假设有额外 vector 维度。

 `lookback` 
Python Alpha 接收  `lookback + 1`  行；如果代码需要含今天共 317 行，最小  `lookback = 316` 。

store warm-up
store 从第一次调用开始积累，可能晚于 FastExpr 的 pre-start 历史；必须在 Notes 中说明。

## 3. 转换工作流

1. 解析 assignments 和 final expression，保留变量依赖顺序。
2. 列出 data fields、group fields、vector fields、operators、named arguments 和最大历史窗口。
3. 先用 BRAIN MCP 查询官方 operator 定义；本地缓存只能做辅助，不作为最高权威。
4. 分类 operator：element-wise、cross-sectional、group、time-series、stateful、platform-internal。
5. 选择策略：raw time-series 可直接切窗口；time-series over computed intermediate 默认用  `store` ；长历史 no-store 只在明确需要严格重建时使用。
6. 输出完整  `@alpha`  core code，包含 helper、data 声明、typed store、 `np.float32`  返回和 Notes。
7. 如果用户明确要求回测，再用 MCP Python simulation 工具提交；否则只给转换代码。

## 4. 公开版源码

目录结构如下。可以直接按这个结构创建 skill：

```
skills/brain-regular-to-python-alpha/
├── SKILL.md
├── references/
│   ├── conversion-guide.md
│   ├── operator-semantics.md
│   ├── python-alpha-platform-gotchas.md
│   ├── verified-snippets.md
│   └── replication-casebook-template.md
├── scripts/
│   └── operator_lookup.py
└── evals/
    └── evals.json
```

SKILL.md

```
---
name: brain-regular-to-python-alpha
description: Convert a WorldQuant BRAIN Regular Alpha Fast Expression into a Python Alpha core implementation. Use this whenever the user provides a Regular Alpha or FASTEXPR expression and asks for a Python Alpha, Python version, conversion, rewrite, migration, or equivalent NumPy implementation. Query official BRAIN operator definitions first, preserve operator semantics, and return the @alpha-decorated core code without running simulations unless explicitly requested.
---

# Convert Regular Alpha FastExpr to Python Alpha

Convert one Regular Alpha Fast Expression into Python Alpha code that follows the BRAIN Python Alpha execution model.

## Required reading

Read `references/conversion-guide.md` before converting an expression.
Read `references/operator-semantics.md` before implementing time-series operators or deciding NaN/window semantics.
Read `references/python-alpha-platform-gotchas.md` when the expression contains nested time-series operators, computed intermediates, group operators, long lookbacks, or any conversion intended for actual platform simulation.
Read `references/verified-snippets.md` before writing `store` caches or group neutralization helpers.
Consult `references/replication-casebook-template.md` when a conversion fails, times out, differs materially from Fast Expression results, or you need to record evidence behind a compact rule.

For every operator used by the expression, use the official BRAIN API definitions as the authoritative source:

1. Authenticate with BRAIN MCP if needed.
2. Call the BRAIN MCP `get_operators` tool.
3. Extract definitions and descriptions for the operators used by the expression.

Use cached local operator lookup only as an auxiliary source for search hints, examples, or offline fallback:

```bash
python skills/brain-regular-to-python-alpha/scripts/operator_lookup.py operator_name
```

The local YAML or JSON knowledge files may be generated or stale. Never treat them as authoritative when they conflict with official BRAIN API or official Learn documentation. Forum posts and personal notes are supporting evidence only.

Do not invent exact semantics for platform-internal operators. Clearly label any approximation. The target is close FastExpr metric replication, so prefer platform-tested rules and snippets over visually simple NumPy translations when they conflict.

## Input

Expect a Regular Alpha Fast Expression. The user may also provide simulation settings or data-field metadata.

If settings are omitted, convert the code without simulating. Infer the minimum required Python `lookback` as the maximum raw historical window needed by the implementation and state it briefly after the code.

Python Alpha does not support BRAIN vector data fields. If the Regular expression depends on a vector field or a vector operator such as `vec_avg`, `vec_sum`, `vec_stddev`, `vec_min`, `vec_max`, `vec_count`, `vec_percentage`, `vec_choose`, or `vec_range`, do not emit a platform-ready Python Alpha and do not submit a Python simulation. Instead, report that the expression is blocked by Python Alpha vector-field support and suggest replacing the vector-field dependency with a scalar data field or keeping the expression as Regular/FastExpr.

## Workflow

1. Parse assignments and the final expression. Preserve statement order and variable dependencies.
2. List data fields, group fields, vector fields, operators, named arguments, and maximum historical windows.
   - If any vector field or `vec_*` operator is present, stop the conversion as unsupported for Python Alpha platform simulation.
3. Classify each operator:
   - Element-wise arithmetic or logical operation.
   - Cross-sectional operation on today's `[n_instruments]` vector.
   - Group operation on today's signal and today's group vector.
   - Time-series operation over `[time, n_instruments]`.
   - Stateful operation requiring `store`.
   - Platform-internal operation that cannot be replicated exactly from published semantics.
4. Query official BRAIN MCP operator definitions for operators used by the expression. Use local files only as auxiliary references. If official documentation does not expose NaN behavior, parameter semantics, ranking convention, or state behavior, label the Python implementation as an approximation.
5. Write a self-contained core Python Alpha:
   - Include `from brain.alphas import alpha`, `import numpy as np`, and `import numpy.typing as npt`.
   - Include helper functions used by the Alpha.
   - Declare all required fields in `@alpha(data=[...])`.
   - Declare typed store entries for cross-day state.
   - Return a one-dimensional `np.float32` array.
6. Choose an implementation strategy:
   - Direct raw-field time-series operations may use the `data.field[-d:]` window.
   - Time-series operations over computed intermediates should prefer typed `store` caches for platform viability.
   - Do not default to rebuilding long computed histories every day. It may be semantically neat but can time out on the platform.
   - If exact FastExpr first-day equivalence requires history initialization, label it as a hybrid attempt and disclose that it may be heavier than pure store warm-up.
   - For `ts_zscore` over a cached computed intermediate, default to the strict full-window helper in `verified-snippets.md`: require all `d` values to be finite for the instrument and return `NaN` when the rolling standard deviation is zero.
7. Review semantic edge cases against the checklist in the conversion guide and platform gotchas.

## Output format

Return:

1. One Python code block containing the complete core Alpha definition.
2. One short `Notes` section listing:
   - Minimum required `lookback`.
   - Whether the implementation is direct, store-warm-up, or hybrid.
   - Any warm-up period introduced by `store`.
   - Any approximations or unresolved operator semantics.
   - Any expected platform viability concerns, such as long computed history reconstruction.

Do not include BrainLabs setup, simulation calls, submission code, or backtest results unless the user asks for them.

## Quality rules

- Preserve semantics over brevity. Do not mechanically translate operator names.
- Treat vector fields and `vec_*` operators as unsupported in Python Alpha. Do not approximate them by assuming a `[time, instruments, vector_elements]` NumPy shape.
- Implement each non-trivial FastExpr operator as a clearly named helper function by default, such as `ts_zscore`, `ts_backfill`, or `group_neutralize`.
- Use `data.field[-1]` only for operations that consume today's cross section. Keep a historical matrix for time-series operations.
- Prefer the provided raw `data` window for direct time-series operations. Use `store` when an intermediate computed signal must persist across days or when an operator is inherently stateful.
- For nested time-series over computed intermediates, prefer a platform-viable `store` implementation by default and clearly state the warm-up tradeoff.
- For `ts_zscore(ts_backfill(a, m) - ts_backfill(b, m), d)`, prefer store-warm-up plus strict full-window z-score.
- Copy read-only data arrays before mutating them.
- Treat integer missing-value sentinels explicitly when integer fields participate in numerical calculations.
- Do not list `universe` in `@alpha(data=[...])`; use `data.universe`.
- Cast the final output with `.astype(np.float32)`.
- Do not simulate unless the user explicitly requests it.
```

references/conversion-guide.md

```
# FastExpr to Python Alpha Conversion Guide

## Execution model

BRAIN calls the decorated Python Alpha once per time step. Each declared `data.field` is a read-only array shaped `[available_history, n_instruments]`. The newest row is `data.field[-1]`. The function returns only today's signal as a one-dimensional `np.float32` array.

Use the raw history window where possible, but do not assume a simple NumPy reducer is metric-equivalent to the FastExpr operator. Treat direct reconstructions such as `np.nanmean(data.field[-d:], axis=0)` as approximations unless the exact operator/field pattern has been platform-tested. Use a typed `store` cache when a time-series operator wraps an intermediate value computed inside the Alpha, such as `ts_mean(group_rank(returns, sector), 20)`.

Python Alpha does not support BRAIN vector data types. Regular expressions that use vector fields or vector operators such as `vec_avg`, `vec_sum`, `vec_stddev`, `vec_min`, `vec_max`, `vec_count`, `vec_percentage`, `vec_choose`, or `vec_range` are not platform-ready Python Alpha conversion candidates.

## Core template

```python
from brain.alphas import alpha
import numpy as np
import numpy.typing as npt

@alpha(
    data=["returns"],
    store=[],
)
def converted_alpha(data, store) -> npt.NDArray[np.float32]:
    signal = -data.returns[-1].astype(np.float64)
    return signal.astype(np.float32)
```

## Operator implementation rules

Keep generated code auditable: define one clearly named helper for each non-trivial FastExpr operator. Inline ordinary arithmetic such as unary minus, addition, subtraction, multiplication, and division.

### Element-wise operations

Translate ordinary arithmetic with NumPy, but preserve documented NaN behavior. Operators such as `add(..., filter=true)` and `subtract(..., filter=true)` require replacing NaNs before applying arithmetic. Do not silently use Python arithmetic when the FastExpr operator has extra arguments.

### Time-series operations

Time-series operators consume trailing `d` rows along axis 0 and produce today's `[n_instruments]` vector. Preserve documented window parameters and named arguments.

Illustrative examples, not guaranteed parity templates:

```python
def ts_mean(x, d):
    return np.nanmean(x[-d:], axis=0)

def ts_delta(x, d):
    if x.shape[0] <= d:
        return np.full(x.shape[1], np.nan, dtype=np.float64)
    return x[-1] - x[-(d + 1)]
```

Do not replace all time-series operators with simple NumPy reducers. Operators such as `ts_rank`, `ts_quantile`, `ts_decay_linear`, `ts_regression`, `hump`, and `trade_when` need dedicated semantics.

### `ts_zscore` coverage semantics

For cached computed intermediates, use strict full-window coverage by default:

- The cached history must contain full `d` rows.
- All `d` values for an instrument must be finite.
- Use population standard deviation over the `d` values.
- Return `NaN` when rolling standard deviation is zero.

Loose `np.nanmean` / `np.nanstd` can materially over-expand coverage and change metrics.

### `ts_min_max_cps` semantics

The official formula is `ts_min(x, d) + ts_max(x, d) - f * x`, with default `f=2`. When input `x` is computed inside the Alpha, store today's computed value and run the min/max formula over cached history. Do not apply min and max across instruments.

For reversed `ts_min_max_diff`, use the identity `-ts_min_max_diff(x, d) = 0.5 * ts_min_max_cps(x, d)` when both operators use default parameters.

### Computed intermediate history

When a time-series operator wraps a computed cross-sectional signal, cache the daily intermediate:

```python
@alpha(
    data=["returns", "sector"],
    store=[{"name": "signal_history", "dims": "xi", "extend": np.float64(np.nan)}],
)
def converted_alpha(data, store) -> npt.NDArray[np.float32]:
    today = data.returns[-1]
    groups = data.sector[-1]
    intermediate = group_neutralize(today, groups)

    if store.signal_history is None:
        store.signal_history = intermediate[np.newaxis, :]
    else:
        store.signal_history = np.vstack(
            [store.signal_history, intermediate[np.newaxis, :]]
        )[-20:]

    return np.nanmean(store.signal_history, axis=0).astype(np.float32)
```

Use NumPy scalar constructors in typed store declarations, such as `np.float64(np.nan)`. Do not use bare `np.nan`, `0`, or `0.0` as `extend` values.

### Cross-sectional operations

Cross-sectional operators consume today's one-dimensional vector. Keep NaNs excluded from statistics and preserve them in output unless documented otherwise.

```python
def normalize(x, use_std=False, limit=0.0):
    out = x.astype(np.float64, copy=True)
    finite = np.isfinite(out)
    if not finite.any():
        return out
    out[finite] -= np.mean(out[finite])
    if use_std:
        std = np.std(out[finite])
        if std > 0:
            out[finite] /= std
    if limit > 0:
        out[finite] = np.clip(out[finite], -limit, limit)
    return out
```

Ranking conventions can affect exact equality. Query the operator definition and label the implementation as an approximation if tie handling or rate behavior is not published.

### Group operations

Use today's group vector, such as `data.sector[-1]`. Missing group identifiers must remain excluded rather than becoming a real group. All-NaN groups remain NaN.

```python
def group_neutralize(x, groups):
    out = np.full(x.shape, np.nan, dtype=np.float64)
    if np.issubdtype(groups.dtype, np.integer):
        valid_group = groups != np.iinfo(groups.dtype).min
    else:
        valid_group = np.isfinite(groups)
    for group in np.unique(groups[valid_group]):
        mask = valid_group & (groups == group) & np.isfinite(x)
        if mask.any():
            out[mask] = x[mask] - np.mean(x[mask])
    return out
```

Do not initialize group results with zeros.

### Backfill semantics

The documented signature is `ts_backfill(x, lookback=d, k=1)`. Respect both `lookback` and `k`: `k=1` selects nearest valid historical value, while larger values select kth nearest valid historical value. Search raw historical values inside the bounded prior window.

When `ts_backfill(x, backfill_days)` is nested inside an outer time-series operator with `outer_days`, retain `backfill_days + outer_days` rows of raw input. Because Python Alpha `lookback` counts extra rows beyond today, request at least `backfill_days + outer_days - 1`.

### Stateful operators

Operators such as `trade_when`, `hump`, and some turnover-targeting operators require previous outputs or platform-specific state. Use typed `store` entries where published semantics are sufficient. Otherwise describe approximation explicitly.

### Integer fields

Integer arrays cannot store NaN. Convert integer missing-value sentinels before calculations:

```python
def integer_field_to_float(x):
    missing = np.iinfo(x.dtype).min
    out = x.astype(np.float32)
    out[x == missing] = np.nan
    return out
```

## Review checklist

- No vector field or `vec_*` operator is present.
- Every FastExpr data field appears in `@alpha(data=[...])`, except `universe`.
- Every raw time-series operation uses enough history.
- Every time-series operation over computed intermediate has typed store cache.
- Any store warm-up introduced by conversion is disclosed.
- Named arguments such as `filter`, `dense`, `constant`, `k`, and `rettype` are preserved.
- Missing values remain missing unless the documented operator changes them.
- Cached computed `ts_zscore` uses strict full-window coverage unless a specific case proves otherwise.
- Group fields use today's row and do not treat missing groups as valid categories.
- Any approximation is disclosed in Notes.
- Final return value is one-dimensional and explicitly cast to `np.float32`.
```

references/operator-semantics.md

```
# Operator Semantics Rules

This file contains compact, action-oriented rules extracted from platform replication work. Prefer these rules over older exploratory notes in the casebook.

## Goal

The conversion goal is metric parity with the original FastExpr alpha, not just syntactically valid Python. When official operator documentation omits NaN handling, window coverage, or zero-variance behavior, use the closest platform-tested rule below and disclose remaining uncertainty.

## `ts_zscore`

For `ts_zscore` over cached computed intermediate, default to strict full-window coverage:

- The cache must contain full `d` rows.
- Every value in the `d`-day window must be finite for that instrument.
- Use population standard deviation over those `d` values.
- Return `NaN` when standard deviation is zero.

Do not default to `np.nanmean` / `np.nanstd` over any available observations. Loose NaN-skipping z-score can materially over-expand coverage.

## `ts_min_max_cps`

The official formulas are:

```text
ts_min_max_cps(x, d, f=2) = ts_min(x, d) + ts_max(x, d) - f * x
ts_min_max_diff(x, d, f=0.5) = x - f * (ts_min(x, d) + ts_max(x, d))
```

Therefore `-ts_min_max_diff(x, d)` is exactly `0.5 * ts_min_max_cps(x, d)` when both operators use default `f` values.

When `x` is a computed intermediate, cache one row per day and apply the formula to trailing `d` cached rows. Do not compute min and max from today's cross-section.

Default to strict full-window coverage for cached computed intermediates unless platform testing proves a looser NaN policy is closer:

- The cache must contain full `d` rows.
- Every value in the `d`-day window must be finite for that instrument.
- Use current cached value as `x` in the final `- f * x` term.
- For default `f=2`, a constant window returns `0.0`.

If strict coverage produces materially different long/short counts or turnover, record a controlled partial-window experiment in the casebook. Treat any partial-window threshold as field/operator-family evidence, not a universal CPS rule.

## `ts_backfill`

Implement bounded nearest-valid lookup, not unlimited forward fill:

- `ts_backfill(x, lookback=d, k=1)` searches only the last `d` rows including today.
- `k=1` selects nearest valid raw observation.
- When nested inside an outer `d2`-day time-series operator, request enough raw rows for both backfill and outer history.

For `ts_zscore(ts_backfill(a, m) - ts_backfill(b, m), d)`, use store-warm-up plus strict `ts_zscore` by default. No-store reconstruction is more direct but can fail on large universes.

## Raw Time-Series Reducers

Treat direct NumPy reducers such as `np.nanmean(data.field[-d:], axis=0)` as approximations unless platform-tested for the exact operator and field class.

## Store Strategy

Use typed `xi` stores for time-series operators over computed intermediates. Store warm-up can differ from FastExpr pre-start history, but is often the platform-viable route. Hybrid first-call reconstruction may be closer in theory, but can fail or trigger store resume inconsistency; use it only when the user explicitly prioritizes strict reconstruction and the case has manageable cost.
```

references/python-alpha-platform-gotchas.md

```
# Python Alpha Platform Gotchas

This file records platform-driven conversion rules discovered while replicating Fast Expression alphas in actual BRAIN Python simulations.

## Prefer viability over formal neatness

Fast Expression can evaluate nested operators inside the platform engine. Python Alpha code runs once per time step and pays the cost of every NumPy operation in user code.

A formally direct conversion can fail if it rebuilds a long computed history every day. For example:

```text
ts_zscore(ts_mean(pos, 252) / ts_mean(neg, 252), 66)
```

Strict reconstruction needs `252 + 66 - 1 = 317` raw rows and computes 66 daily ratios. In platform tests, versions that rebuilt this computed history every call can fail or time out, while a `store` version that appends one ratio per day can run successfully.

## Store warm-up tradeoff

For computed intermediate history, the platform-viable pattern is:

```text
today_intermediate = compute today's value from raw data
append today_intermediate to store.history
keep the last d rows
apply the outer time-series operator to store.history
```

This introduces warm-up. A `store` cache for 66 days has only one row on the first simulation call and becomes complete on the 66th call. Fast Expression may have access to pre-start history and produce a complete value earlier.

Always disclose this difference in Notes.

## Viability is not enough

A Python Alpha that runs can still be a poor conversion if operator edge cases expand or shrink coverage. After choosing a platform-viable store strategy, preserve closest platform-tested operator semantics. For `ts_zscore` over cached computed intermediates, default to strict full-window coverage and `NaN` for zero standard deviation, not loose `np.nanmean` / `np.nanstd` over partial windows.

## Hybrid initialization is not guaranteed viable

A hybrid implementation can attempt:

```text
first call: initialize store.history from raw lookback
later calls: append one new value
```

This is closer to Fast Expression first-day behavior but can still fail if initialization reconstructs a large computed history. Do not present hybrid as guaranteed.

## Group fields

Group fields such as `market`, `industry`, and `subindustry` can be used as data fields when available:

```python
@alpha(data=["signal_field", "industry"], store=[])
def alpha_fn(data, store):
    groups = data.industry[-1]
```

Use today's group vector for group operators. A robust group helper filters missing integer groups with dtype minimum sentinel and filters signal values with `np.isfinite`.

Do not assume settings neutralization and expression-level group neutralization are the same thing.

## Helper functions and platform errors

Simple helpers can work, but platform error messages may be generic. If helper-based version fails while inline version passes, reduce abstraction and avoid complex type annotations in helper signatures. Keep only helpers that are platform-tested or necessary for readability.

## Warnings

`np.nanmean` and `np.nanstd` can warn on all-NaN slices. The platform may report generic failure without exposing the warning. Prefer explicit count/sum implementations for platform-critical code when repeated all-NaN windows are likely.

## Lookback wording

Python Alpha receives `lookback + 1` rows. If an expression needs 317 rows including today, strict minimum setting is `lookback = 316`.

## Settings schema differences

Regular Alpha details may show fields that are not accepted by Python simulation submit schema. Do not blindly copy all settings from `get_alpha` into `submit_python_simulation`.

Observed Python submit rejections:

- `startDate` and `endDate` can appear in returned alpha settings but be extra/forbidden on Python submit.
- Regular-only `nanHandling` and `unitHandling` may not be accepted by Python submit settings.

Use `get_platform_setting_options` and Python submit validation response to trim settings before submission.
```

references/verified-snippets.md

```
# Verified Snippets

These snippets are templates that matched observed platform behavior during Python Alpha replication work. Keep them small and conservative.

## Group neutralize

```python
def group_neutralize(x, groups):
    out = np.full(x.shape, np.nan, dtype=np.float64)

    if np.issubdtype(groups.dtype, np.integer):
        valid_group = groups != np.iinfo(groups.dtype).min
    else:
        valid_group = np.isfinite(groups)

    for group in np.unique(groups[valid_group]):
        mask = valid_group & (groups == group) & np.isfinite(x)
        if mask.any():
            out[mask] = x[mask] - np.mean(x[mask])

    return out
```

Notes:

- Use `data.group_field[-1]` for today's grouping vector.
- Do not add `universe` masking by default unless the user asks or a case shows it is required.
- `np.isfinite(x)` avoids NaN and inf entering group means.

## Store cache for computed time-series intermediate

Use a typed `xi` store for a cached `[days, instruments]` matrix:

```python
@alpha(
    data=["field_a", "field_b", "market"],
    store=[
        {"name": "ratio_history", "dims": "xi", "extend": np.float64(np.nan)},
    ],
)
def converted_alpha(data, store):
    ...
```

Append one row per call:

```python
if store.ratio_history is None:
    store.ratio_history = ratio_today[np.newaxis, :]
else:
    store.ratio_history = np.vstack(
        [store.ratio_history, ratio_today[np.newaxis, :]]
    )[-66:]
```

Notes:

- This is platform-viable for long computed histories.
- It introduces warm-up until cache reaches required number of rows.
- Use `np.float64(np.nan)` as `extend` value, not bare `np.nan`.

## NaNHandling OFF mean

Use explicit count/sum when warnings from `np.nanmean` are risky:

```python
valid = ~np.isnan(window)
count = valid.sum(axis=0)
total = np.where(valid, window, 0.0).sum(axis=0)

mean = np.full(window.shape[1], np.nan, dtype=np.float64)
ok = count > 0
mean[ok] = total[ok] / count[ok]
```

## Vectorized bounded backfill

Prefer this over a Python loop across rows or instruments for `ts_backfill(x, lookback=d, k=1)`.

```python
def field_to_float(x):
    if np.issubdtype(x.dtype, np.integer):
        missing = np.iinfo(x.dtype).min
        out = x.astype(np.float64)
        out[x == missing] = np.nan
        return out
    return x.astype(np.float64)

def ts_backfill_nearest(x, lookback):
    window = field_to_float(x[-lookback:])
    valid = np.isfinite(window)
    has_valid = valid.any(axis=0)

    out = np.full(window.shape[1], np.nan, dtype=np.float64)
    if has_valid.any():
        rows_from_end = np.argmax(valid[::-1], axis=0)
        row_idx = window.shape[0] - 1 - rows_from_end
        cols = np.where(has_valid)[0]
        out[cols] = window[row_idx[cols], cols]

    return out
```

## Strict z-score from cached history

Use this as the default for FastExpr `ts_zscore` over cached computed intermediates.

```python
def ts_zscore_strict(history, days):
    hist = history[-days:]
    out = np.full(hist.shape[1], np.nan, dtype=np.float64)
    if hist.shape[0] < days:
        return out

    valid = ~np.isnan(hist)
    full = valid.sum(axis=0) == days
    if not full.any():
        return out

    mean = hist[:, full].mean(axis=0)
    centered = hist[:, full] - mean
    std = np.sqrt((centered ** 2).mean(axis=0))
    today = hist[-1, full]

    values = np.full(today.shape, np.nan, dtype=np.float64)
    normal = std > 0.0
    values[normal] = (today[normal] - mean[normal]) / std[normal]
    out[np.where(full)[0]] = values
    return out
```

## Strict min-max CPS from cached history

```python
def ts_min_max_cps_strict(history, days, f=2.0):
    hist = history[-days:]
    out = np.full(hist.shape[1], np.nan, dtype=np.float64)
    if hist.shape[0] < days:
        return out

    valid = np.isfinite(hist)
    full = valid.sum(axis=0) == days
    if not full.any():
        return out

    window = hist[:, full]
    today = window[-1]
    values = window.min(axis=0) + window.max(axis=0) - f * today
    out[np.where(full)[0]] = values
    return out
```

## Loose z-score warning

A loose implementation that computes mean/std over any non-NaN observations can over-expand coverage. Treat loose implementations as experiments, not defaults.
```

scripts/operator_lookup.py

```
#!/usr/bin/env python3
"""Look up cached BRAIN operator definitions for offline conversion work."""

from __future__ import annotations

import json
import sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: operator_lookup.py OPERATOR_NAME", file=sys.stderr)
        return 2

    operator_name = sys.argv[1]
    repo_root = Path(__file__).resolve().parents[3]
    knowledge_file = (
        repo_root / "operator-analysis" / "knowledge" / "operators" / f"{operator_name}.yaml"
    )
    if knowledge_file.exists():
        print(knowledge_file.read_text(encoding="utf-8"))
        return 0

    operator_file = repo_root / "operator-analysis" / "brain_operators.json"
    payload = json.loads(operator_file.read_text(encoding="utf-8"))

    for operator in payload.get("operators", []):
        if operator.get("name") == operator_name:
            print(json.dumps(operator, ensure_ascii=False, indent=2))
            return 0

    print(f"operator not found: {operator_name}", file=sys.stderr)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
```

evals/evals.json

```
{
  "skill_name": "brain-regular-to-python-alpha",
  "evals": [
    {
      "id": 1,
      "prompt": "Convert this Regular Alpha Fast Expression to Python Alpha core code without simulating: -ts_mean(returns, 20)",
      "expected_output": "A self-contained @alpha core definition using the raw returns history window and returning float32.",
      "files": []
    },
    {
      "id": 2,
      "prompt": "Convert this Regular Alpha Fast Expression to Python Alpha core code without simulating: ts_mean(group_neutralize(returns, sector), 20)",
      "expected_output": "A self-contained @alpha core definition using today's returns and sector values, a typed xi store cache for computed intermediate history, correct missing-group handling, and a float32 return.",
      "files": []
    },
    {
      "id": 3,
      "prompt": "Convert this Regular Alpha Fast Expression to Python Alpha core code without simulating: trade_when(volume > ts_mean(volume, 20), rank(-returns), -1)",
      "expected_output": "A self-contained @alpha core definition with typed state for prior output, a documented handling choice for the exit condition, and a float32 return.",
      "files": []
    },
    {
      "id": 4,
      "prompt": "Convert this Regular Alpha Fast Expression to Python Alpha core code without simulating: group_neutralize(ts_zscore(ts_mean(field_a, 252) / ts_mean(field_b, 252), 66), market)",
      "expected_output": "A platform-viable Python Alpha that uses a typed xi store for computed ratio history by default, applies strict full-window ts_zscore to cached ratio history unless explicitly justified otherwise, declares two scalar fields plus market, implements group neutralization using today's market group vector, returns float32, and notes store warm-up versus exact FastExpr first-window behavior.",
      "files": []
    },
    {
      "id": 5,
      "prompt": "Convert this Regular Alpha Fast Expression to Python Alpha core code without simulating: ts_zscore(ts_backfill(field_a, 252) - ts_backfill(field_b, 252), 66)",
      "expected_output": "A Python Alpha that uses bounded ts_backfill semantics, a typed xi store for spread history, strict full-window ts_zscore over cached spread history, lookback at least 316, float32 output, and notes that store warm-up is chosen because no-store reconstruction can fail on large universes.",
      "files": []
    },
    {
      "id": 6,
      "prompt": "Convert this Regular Alpha Fast Expression to Python Alpha core code without simulating: ts_min_max_cps(log(((ts_backfill(field_a, 252)) + 1) / ((ts_backfill(field_b, 252)) + 1)), 252)",
      "expected_output": "A Python Alpha that declares both scalar fields, implements bounded nearest-valid ts_backfill for each raw field, computes today's log ratio with invalid log inputs preserved as NaN, stores computed log-ratio history in a typed xi store, applies official ts_min + ts_max - 2*x formula over trailing 252 cached rows with strict full-window coverage, returns float32, and notes store warm-up plus lookback 251 for store version or 502 for strict no-store reconstruction.",
      "files": []
    }
  ]
}
```

## 5. MCP Python 回测工具

下面是最小工具链。先认证，再轻量验证状态，然后提交 Python simulation。不要把认证和重接口并发调用。

### 认证

```
authenticate({})
get_auth_status()
```

### 提交 Python Alpha

```
submit_python_simulation({
  "python_code": "from brain.alphas import alpha\nimport numpy as np\n...",
  "settings": {
    "instrumentType": "EQUITY",
    "region": "USA",
    "universe": "TOP3000",
    "delay": 1,
    "lookback": 252,
    "decay": 3,
    "neutralization": "INDUSTRY",
    "truncation": 0.08,
    "pasteurization": "ON",
    "visualization": false
  }
})
```

Python Alpha 不支持 MultiSim；GLB 暂时不支持Python Alpha

### 等待、刷新和查看任务

```
# 短任务：前台等待
wait_simulation_tasks({
  "task_ids": ["local-task-id"],
  "max_wait_seconds": 600
})

# 长任务或排障：刷新指定任务
refresh_simulation_tasks({
  "task_ids": ["local-task-id"],
  "force": true
})

# 查看一个任务
get_simulation_task({
  "task_id": "local-task-id",
  "include_children": true
})

# 列出最近任务
list_simulation_tasks({
  "include_children": true,
  "kind": "python_single",
  "limit": 30
})
```

**不要重复提交 submission_unknown：** Simulation 创建是  `POST /simulations` ，网络超时或平台 5xx 后，客户端无法确认平台是否已经创建任务。遇到  `submission_unknown` ，先人工核对平台状态，再决定是否清理本地任务；不要直接重复提交同一份代码。

### settings 裁剪规则

- 不要把  `get_alpha`  返回的 settings 全量复制到  `submit_python_simulation` 。
- `startDate` 、 `endDate`  这类返回详情字段可能被 Python submit 拒绝。
- Regular-only 的  `nanHandling` 、 `unitHandling`  可能不能用于 Python submit；如果行为重要，应在 Python code 中显式近似并回测验证。
- 用  `get_platform_setting_options`  和提交校验错误来收敛 settings。

## 6. 如何继续沉淀案例

原始私有 casebook 不适合公开粘贴，但它的方法可以公开。建议每次转换失败、超时或指标明显不同，就按下面模板记录。长期看，skill 的质量主要来自这些反例和对照实验。

references/replication-casebook-template.md

```
# Replication Casebook Template

This file records concrete FastExpr-to-Python replication cases. Keep private IDs, account information, and sensitive metrics out of public copies.

## How to Use This File

Do not read the whole casebook during ordinary conversion. Start with `operator-semantics.md` and `verified-snippets.md`. Use this casebook only to diagnose failed conversion, explain why a compact rule exists, or decide between competing implementations.

## Compact Lessons

- Record only generalized lessons here.
- Keep field/operator-family scope explicit.
- Do not promote one case into a universal rule without repeated evidence.

## Case: YYYY-MM-DD short title

### Fast Expression

```text
paste_expression_here
```

### Settings

```text
region = ...
universe = ...
delay = ...
decay = ...
neutralization = ...
truncation = ...
pasteurization = ...
lookback = ... for Python, if applicable
```

### Candidates

```text
FastExpr baseline: internal/private identifier omitted
Python candidate A: strategy = direct raw window / store warm-up / hybrid
Python candidate B: strategy = ...
```

### Observed behavior

- Did the Python simulation complete?
- Did it fail with validation error, generic simulation failure, timeout, or store resume inconsistency?
- Did coverage, long/short counts, turnover, Sharpe/Fitness, or PnL shape materially differ?
- Which helper or settings choice changed the result?

### Sanitized comparison

Use relative or bucketed descriptions for public notes:

```text
baseline turnover: target range
candidate A turnover: lower/similar/higher
candidate B turnover: closest
coverage: under-expanded / similar / over-expanded
headline metrics: worse / similar / better
```

### Implication

- What rule should be updated?
- Is the rule universal, field-family-specific, or just a local hypothesis?
- Should default conversion change, or should this remain an optional experiment?
```

### 从回测反哺 skill 的原则

- 先把失败归类：语法、settings schema、字段支持、执行成本、operator 语义、store 状态。
- 只把稳定复现的经验写进  `operator-semantics.md`  或  `verified-snippets.md` 。
- 单个案例的特殊阈值只放在 casebook，不要变成全局默认。
- 所有公开版本都移除私有 ID、任务 UUID、账号痕迹和完整收益指标。

## 结论

Regular to Python 的难点不是写出能运行的 NumPy，而是建立一套可审计的转换流程：官方 operator 定义优先、computed intermediate 默认 store、严格记录 warm-up 和近似点、用 MCP 回测验证，再把失败案例反哺到规则里。本文的公开版 skill 刻意不包含私有案例数据，但保留了完整复刻方法。

---

## 讨论与评论 (6)

### 评论 #1 (作者: LA79055, 时间: 17天前)

这份 skill 的重点不只是把操作符名改写成 NumPy，而是把 operator 语义、NaN 行为、store warm-up、settings schema 差异都放进 casebook。官方 Python Alpha 文档也明确了 `@alpha`、`data`、`store` 和 `float32` 返回的约束；把这些规则写进 SKILL.md，比一次性提示词更适合长期维护。

---

### 评论 #2 (作者: 顾问 RM49262 (Rank 30), 时间: 16天前)

=====================================评论区====================================

感谢大佬分享 这个贴子的skill真的是干货  方便大家一起做Python alpha

我这就去试试看

=============================================================================

---

### 评论 #3 (作者: SY90356, 时间: 16天前)

首先感谢分享经验，光看这内容真是用心了，对于Pa目前还没有进行深入研究，也仅仅是使用python对op进行了复现尝试，我看不少顾问已经提交了不少Pa了，大家一起努力！

------------------------------------------------------------------------------------------

回测是历史的答案，实盘是未来的考题。

------------------------------------------------------------------------------------------

---

### 评论 #4 (作者: RL71875, 时间: 16天前)

非常有启发！Alpha研究需要不断尝试和优化，感谢分享实战经验。

---

### 评论 #5 (作者: YT18046, 时间: 15天前)

感谢分享，通过这个skill，成功提交了第一个python alpha的回测


> [!NOTE] [图片 OCR 识别内容]
> 三 alpha_
> example py
> untitledl py
> Untitledtipynb
> &
> Code
> settings
> Simulationsettings (
> instrument
> tyDe=
> EOUITY"
> region='USA
> delay=l
> universe='T0P3000
> lookback=252
> 三121:
> 252  提供足够余虽
> Oecay=6
> neutralization=' FAST
> truncation=o
> pasteurization=
> ONI'
> language=
> PYTHON'
> Visualization-False
> alpha_id
> brain. simulate
> converted_alpha, settings)
> Drint (f"Alpha ID:
> {alpha_id}
> Simulation Id:
> 2560.0/? [06.13<00;00,
> 6.93it/5]


---

### 评论 #6 (作者: YQ84572, 时间: 15天前)

很好的分享，对于想要入门python alpha的顾问是非常好的入手方式，但是仍要提醒各位，转写不是python alpha的最终目的，找出python 和fast 的表达式的差异，做出独特的alpha 才是最终我们需要追求的。作为对新人入门来说，这个skill非常方便，感谢分享

---

