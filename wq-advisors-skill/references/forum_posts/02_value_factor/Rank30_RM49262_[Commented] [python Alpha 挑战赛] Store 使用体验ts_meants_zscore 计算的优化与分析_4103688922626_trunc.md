# [python Alpha 挑战赛] Store 使用体验：ts_mean(ts_zscore(...)) 计算的优化与分析

- **链接**: https://support.worldquantbrain.com[Commented] [python Alpha 挑战赛] Store 使用体验ts_meants_zscore 计算的优化与分析_41036889226263.md
- **作者**: MY82844
- **发布时间/热度**: 17天前, 得票: 68

## 帖子正文

### 背景

这两天我们尝试将一个 Fast Expression 表达式 `ts_mean(ts_zscore(imb5_score, 252), 21)` 转换为 Python Alpha，遇到了超时问题，基于论坛中前期关于store算子的宝贵分享，调试了几天终于跑通了，把经验分享出来，希望对大家上手复杂的python alpha有所帮助。

### 一、什么时候需要 store？

看这个表达式：`ts_mean(ts_zscore(field, 252), 21)`

FE 中一行搞定，但到 Python 里就要想：`ts_zscore` 算出每只股票的一个 z-score（1D），但外层的 `ts_mean` 需要 **21 天的 z-score 历史**（2D）才能算均值。

这就是 store 的典型场景——**嵌套 TS 算子，内层输出 1D，外层需要 2D 历史窗口**。

更一般地：只要你的 Python Alpha 需要在**不同交易日之间保持状态**（EWMA、滚动窗口、缓存等），就要用 store。

### 二、两种实现对比

#### 方案 A：无 store，lookback=273

```python
@alpha(data=['imb5_score'], store=[])
def auto_alpha(data, store):
    T = data.imb5_score.shape[0]
    z_list = []
    for j in range(21):
        i = T - 21 + j
        sub = data.imb5_score[i - 251 : i + 1]
        m = np.nanmean(sub, axis=0)
        s = np.nanstd(sub, axis=0, ddof=0)
        ok = (s > 0) & ~np.isnan(m)
        z = np.full_like(data.imb5_score[i], np.nan)
        z[ok] = (data.imb5_score[i, ok] - m[ok]) / s[ok]
        z_list.append(z)
    signal = np.nanmean(z_list, axis=0)
    return signal.astype(np.float32)
```

**问题**：
- 每天算 21 次 z-score，计算量大
- lookback=273（252+21），数据量更大
- 实际提交时轮询超时（600s 不够），导致失败

#### 方案 B：store 环形缓冲区，lookback=252

```python
@alpha(
    data=['imb5_score'],
    store=[{"name": "z_buf", "dims": "xi", "extend": np.float32(np.nan)}],
)
def auto_alpha(data, store):
    # ts_zscore(imb5_score, 252) — 每天只算 1 次
    m = np.nanmean(data.imb5_score, axis=0)
    s = np.nanstd(data.imb5_score, axis=0, ddof=0)
    ok = (s > 0) & ~np.isnan(m)
    z = np.full_like(data.imb5_score[-1], np.nan)
    z[ok] = (data.imb5_score[-1, ok] - m[ok]) / s[ok]

# Store 环形缓冲区：FIFO shift + append
    if store.z_buf is None:
        store.z_buf = np.full((21, z.shape[0]), np.nan, dtype=np.float32)
    store.z_buf[:-1] = store.z_buf[1:]  # 丢弃最旧一行
    store.z_buf[-1] = z                 # 追加今天 z-score

# ts_mean(z_buf, 21)
    signal = np.nanmean(store.z_buf, axis=0)
    return signal.astype(np.float32)
```

**优势**：
- 每天只算 1 次 z-score，不是 21 次
- lookback=252（少了 21 天数据量）
- 提交成功，耗时 ~470s

### 三、Store 的核心规则（踩坑总结）

| 规则 | 说明 |
|------|------|
| `dims` 合法值 | SDK 源码 `_DIMENSIONS = ["i", "x"]`，组合为 `"i"` `"x"` `"xi"` `"ii"` |
| `"i"` = 股票轴 | universe 扩张时自动 padding |
| `"x"` = 自由轴 | 自己管理长度，不会自动扩展 |
| `"ii"` = 工具×工具矩阵 | 如相关矩阵，universe 扩张时自动扩展行列，需手动修复对角线（见下文） |
| `extend` 必须是 numpy 标量 | ✅ `np.float32(0)` `np.float64(np.nan)` ❌ `0` `0.0` `np.nan` |
| 首次调用 store 是 None | 必须手动建数组初始化 |
| 注意类型提升 | `np.nanmean` / `np.nanstd` 会将 float32 提升到 float64，返回前记得 `.astype(np.float32)` |
| 数据只读 | 不能修改 data.xxx，必须先 `.copy()` |
| 返回类型 | 必须 `astype(np.float32)` |

### 四、进阶 Store 技巧

#### 4.1 dims="ii"：工具×工具矩阵

```python
store=[{"name": "corr", "dims": "ii", "extend": np.float64(0)}]
```

用于相关矩阵等 `[n_instruments, n_instruments]` 场景。universe 扩张时行列自动扩展，但**新增工具的对角线需手动修复**（平台会填 0）：

```python
n = data.returns.shape[1]
if store.corr is None:
    store.corr = np.eye(n, dtype=np.float64)
    store.prev_n = n
else:
    if n > store.prev_n:
        store.corr[n-1, n-1] = 1.0  # 修复对角线
        store.prev_n = n
```

#### 4.2 无类型 store 的手动 padding

如果用了普通字符串声明 store，universe 增长时需要手动 pad：

```python
@alpha(data=["returns"], store=["my_cache"])
def alpha(data, store):
    n = data.returns.shape[1]
    if store.my_cache is None:
        store.my_cache = np.zeros(n, dtype=np.float32)
    elif store.my_cache.shape[-1] < n:
        # 手动 padding
        store.my_cache = np.pad(store.my_cache, (0, n - store.my_cache.shape[-1]),
                                mode='constant', constant_values=np.nan)
```

#### 4.3 Warm-start：预填缓冲区消除冷启动

直接使用方案 B 时，store 缓冲区初始全是 NaN，前 21 天 ts_mean 算出来是 NaN。顾问 JX79797 (Rank 9) 的帖子提出了 **warm-start** 方案：首次调用时用 lookback 数据回填缓冲区，消除冷启动期：

```python
def _warmup_z_buf(data, n_inst):
    """Pre-fill z_buf from lookback data so buffer isn't cold."""
    buf = np.full((21, n_inst), np.nan, dtype=np.float32)
    for k in range(21):
        sub = data.imb5_score[-252 - k : -k if k > 0 else None]
        m = np.nanmean(sub, axis=0)
        s = np.nanstd(sub, axis=0, ddof=0)
        ok = (s > 0) & ~np.isnan(m)
        z = np.full(n_inst, np.nan)
        z[ok] = (sub[-1, ok] - m[ok]) / s[ok]
        buf[21 - 1 - k] = z
    return buf

@alpha(
    data=['imb5_score'],
    store=[{"name": "z_buf", "dims": "xi", "extend": np.float32(np.nan)}],
)
def auto_alpha(data, store):
    m = np.nanmean(data.imb5_score, axis=0)
    s = np.nanstd(data.imb5_score, axis=0, ddof=0)
    ok = (s > 0) & ~np.isnan(m)
    z = np.full_like(data.imb5_score[-1], np.nan)
    z[ok] = (data.imb5_score[-1, ok] - m[ok]) / s[ok]

if store.z_buf is None:
        store.z_buf = _warmup_z_buf(data, z.shape[0])
    store.z_buf[:-1] = store.z_buf[1:]
    store.z_buf[-1] = z

signal = np.nanmean(store.z_buf, axis=0)
    return signal.astype(np.float32)
```

#### 4.4 vstack 截断模式（替代环形缓冲区）

HZ32281 的帖子用了另一种方式——每次 vstack 追加新行，然后只保留后 N 行：

```python
new_cache = np.vstack([store.rank_cache, today_rank[np.newaxis, :]])
store.rank_cache = new_cache[-RANK_DAYS:]
```

每次分配新内存，适合小窗口（N < 100）；大窗口建议用 FIFO shift。

#### 4.5 EWMA 状态持久化（dims="i"）

```python
store=[{"name": "ewma", "dims": "i", "extend": np.float32(0)}]
# 每日更新
if store.ewma is None:
    store.ewma = np.zeros(data.returns.shape[1], dtype=np.float32)
store.ewma = 0.9 * store.ewma + 0.1 * today_value
```

### 五、Lookback 选取建议

| lookback | 窗口大小 | 适用场景 | 模拟耗时 |
|----------|---------|---------|---------|
| 30 | 31天 | 快速迭代测试 | ~2-3 分钟 |
| 63 | 64天 | 季度数据 | ~3-5 分钟 |
| 120 | 121天 | 半年数据 | ~5-8 分钟 |
| 252 | 253天 | 年度数据 | ~10-15 分钟 |

顾问 JX79797 (Rank 9) 的转换器使用 **max_window × 2** 的经验公式自动推断 lookback。对于我们的例子，最大窗口是 252（ts_zscore 的窗口），所以 lookback=504。但实测 lookback=252 也够用，因为 store 环形缓冲区自己保存中间结果。

### 六、时序分析

#### 轮询耗时数据（来自实际提交）

我们的 alpha 提交轮询日志（lookback=252, 单字段, store 方案）：

```
Status: 201
Waiting 5.0s... × 96 次 = ~480 秒（约 8 分钟）
```

#### 超时经验

第一次用方案 A（lookback=273，每天 21 次 z-score），工具 600s 超时被 kill。改用方案 B（store，lookback=252，每天 1 次 z-score），~480s 成功。

建议：
- API 轮询设 5s 间隔
- 超时至少设 600s（10 分钟）
- 用后台任务提交，避免前端超时中断
- 复杂 alpha 预估 5-10 分钟

### 总结

Store 是 Python Alpha 实现跨周期状态持久化的核心工具。它的本质是将全量重算（O(n) 全历史）转为增量更新（O(1) 当日），在减少 lookback、降低计算量、避免超时方面非常有价值。

关键就是记住几点：
1. dims 用 i/x/xi/ii 组合
2. extend 必须 numpy scalar
3. 首次调用记得初始化
4. np.nanmean 会提升类型，返回前 astype(np.float32)
5. 大窗口用 FIFO shift，小窗口可以 vstack 截断
6. 考虑 warm-start 预填缓冲区避免冷启动

### 参考帖子

- [HZ32281] [Python Alpha 挑战赛] 基于 skill: brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化 —  [[L2] [Python Alpha 挑战赛] 基于skill brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化_40796757798807.md]([L2] [Python Alpha 挑战赛] 基于skill brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化_40796757798807.md) 
- [顾问 JX79797 (Rank 9)] [Python Alpha 挑战赛] AI Agent 自动将 Fast Expression 转为 Python Alpha 并回测经验分享 —  [[L2] [Python Alpha 挑战赛] AI Agent 自动将 Fast Expression 转为 Python Alpha 并回测经验分享_40740029001239.md]([L2] [Python Alpha 挑战赛] AI Agent 自动将 Fast Expression 转为 Python Alpha 并回测经验分享_40740029001239.md)

---

## 讨论与评论 (8)

### 评论 #1 (作者: 顾问 RM49262 (Rank 30), 时间: 17天前)

=====================================评论区====================================

感谢大佬分享 每次都干货满满啊

这就去试试看

=============================================================================

---

### 评论 #2 (作者: CZ39633, 时间: 17天前)

====================================================================================  感谢的大佬的关于python alpha的运算符构建思路分享！！！太强了                                        ================================自信人生两百年，会当水击三千里==========================

---

### 评论 #3 (作者: LA79055, 时间: 17天前)

这个 store 例子很有参考价值，`ts_mean(ts_zscore(imb5_score,252),21)` 正好说明 Python Alpha 逐日调用时，内层 1D z-score 要缓存成 21 天历史。官方文档里 store 可以跨 time step 保留状态，你用环形缓冲把 lookback 从 273 降到 252，也把计算从每天 21 次 z-score 降到 1 次，问题拆得很清楚。

---

### 评论 #4 (作者: YQ84572, 时间: 16天前)

很精彩的分享，社区已经越来越多人开始着手python alpha了，真是令人振奋。

====================================================================================

感谢大佬的分析，祝大佬vf高高，base多多
====================================================================================

---

### 评论 #5 (作者: RL71875, 时间: 16天前)

学习了！这个方向确实值得深入研究。建议结合多种数据源进行验证，确保策略的鲁棒性。

---

### 评论 #6 (作者: RL71875, 时间: 16天前)

好文章！因子设计确实需要理论与实践结合，期待更多分享。

---

### 评论 #7 (作者: WY18421, 时间: 16天前)

非常好的实战总结。方案 B 把 daily z-score 从 21 次降到 1 次，是嵌套 TS 算子转 Python Alpha 的核心技巧。

补充一个微小优化：FIFO shift（ `store.z_buf[:-1] = store.z_buf[1:]` ）每天做一次整数组复制。在 21×3000 的 float32 上影响不大，但如果 store 矩阵更大，可以用循环索引指针消除复制。需在 store 声明中增加  `"head"`  字段：

```
if store.z_buf is None:
    store.z_buf = np.full((21, n_inst), np.nan, dtype=np.float32)
    store.head = 0
store.z_buf[store.head] = z
store.head = (store.head + 1) % 21
idx = (np.arange(21) + store.head) % 21
signal = np.nanmean(store.z_buf[idx], axis=0)
```

代价是每次需计算 idx 重排和 fancy indexing，实际收益在小窗口下不显著。帖中 FIFO shift 在 21 天窗口已够用，此变体仅作备选。

---

### 评论 #8 (作者: JR57542, 时间: 15天前)

环形缓冲区的方案 B 写得很清楚，lookback 从 273 降到 252 的优化也很实用。

我这边在 Python Alpha 中也大量使用 store，补充两个实践经验：

**1. store 的 dims 计算要精确：** 环形缓冲区的 dims 就是窗口长度（这里是 21），但如果有多个 store 变量，每个都要单独声明。我之前踩过坑——忘记声明第二个 store 的 dims，导致默认为空，运行时 silent error（返回全 NaN），回测结果 Sharpe=0 但不报错。

**2. 超时问题的另一个解法：** 除了 store 优化外，还可以考虑把 ts_zscore 的 lookback 缩短。我在 imb5_score 类字段上测试过，252 天的 z-score 窗口其实可以缩短到 120 天而不显著损失信号——因为 imb 类字段的均值回归速度通常比基本面字段快。这样 total lookback 从 273 降到 141，计算量减少约一半。

---

