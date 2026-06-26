# [Python Alpha 挑战赛] 基于skill: brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化

- **链接**: https://support.worldquantbrain.com[L2] [Python Alpha 挑战赛] 基于skill brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化_40796757798807.md
- **作者**: HZ32281
- **发布时间/热度**: 28 days ago, 得票: 16

## 帖子正文

1,  **Idea** ：

用IDE尝试python alpha回测的时候，发现 skill: brain-simAlphasinBatch-and-track 当中的batch_simulator可以用来回测python alpha。然后为了看懂官方文档，让AI把文档改写为方法论。最后尝试把方法论与现有的fast expression版本全自动工作流结合，得到了python alpha版本全自动工作流。

核心思路 ：

- 💡 发现 ： brain-simAlphasinBatch-and-track 技能不仅能批量回测，还可以作为 Python Alpha 的独立回测器使用

- 🎯 整合 ：将官方 Python Alpha 文档与成熟的 FASTEXPR 工作流相结合

- 🔄 迭代 ：建立"构思 → 编写 → 回测 → 审计 → 优化"的闭环流程

2, **实现：**

核心工作流架构：


> [!NOTE] [图片 OCR 识别内容]
> Python Alpha 工作流
> Phase 1: 情报收集
> Phase 2:
> Phase 3: 单次回测
> Phase 4:
> Python Alpha 构建
> 单次回测
> 结果审计与优化
> 平台认证
> 核心语法
> JSON 配置
> Gatekeeper Checklist
> @alpha 装饰器
> gel_platform_setting_options
> 〈/
> datalstore 参数
> 数据集获取
> 策略模板
> 双视图展示
> 人类可读 (Python)
> Sharpe | Fitness
> 时序操作
> AI 执行 (JSON)
> Turnover 检查
> 横哉面操作
> get_datasets | get_datafields
> 条件交易
> 执行命令
> 快速反应
> 数据特性分析
> 信号处理
> 失败诊断
> 覆盖率
> pasteurize
> 性能优化
> 更新频率
> neutralize
> brainsimAlphasinBatch。
> 相关性验证
> 中性化逑摔
> scale
> and-track
> Aloha generation Workflow Jiagram based on user request。


核心代码示例：

```
from brain.alphas import alphaimport numpy as npimport numpy.typing as nptdef pasteurize(a, u):    """掩码到库外工具"""    a = a.copy()    a[~u.astype(bool)] = np.nan    return adef neutralize(a):    """市场中性化"""    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)    return a - np.mean(a0)def scale(a):    """L1范数归一化"""    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)    norm = np.linalg.norm(a0, ord=1)    return a / norm if norm > 0 else a@alpha(data=["returns"], store=[])def mean_reversion(data, store) -> npt.NDArray[np.float32]:    signal = -np.nanmean(data.returns, axis=0)    signal = pasteurize(signal, data.universe[-1])    signal = scale(neutralize(signal))    return signal.astype(np.float32)
```

回测命令 ：

```
Set-Location "你的任意CLI或者IDE的skills路径：skills\brain-simAlphasinBatch-and-track"python scripts/batch_simulator.py `  --config configs/config.json `  --alpha-json "path/to/alpha_list.json" `  --output-csv "path/to/simulation_status.csv" `  --batch-size 1 `  --concurrency 1
```

启动模板：

```
## 【Python Alpha 启动提示词】请帮我用 Python Alpha 工作流回测以下 Alpha：## 目标设置- Region: `目标区域`- Universe: `目标宇宙`- Dataset: `目标数据集`- Delay: `1`**如果你想顺利找到数据集，搜索之前请严格配置以上四个参数，不要选择性忽略任何一个。**## Alpha 构思[描述你的 Alpha 逻辑，例如： 使用 eur_director_value_1 和 eur_top_value_1 两个字段， 做横截面排名后相加，模拟 ts_target_tvr_hump 效果]## 可用工具函数（选填）[如无特殊需求，使用默认实现： - pasteurize: 掩码到库外工具 - neutralize: 市场中性化 - scale: L1归一化 - cross_sectional_rank: 横截面排名]请按以下步骤执行：1. 根据 Alpha 构思编写 Python Alpha 代码2. 创建 JSON 配置文件3. 运行 batch_simulator 回测4. 返回结果（Sharpe/Fitness/Turnover/状态）5. 如需优化，给出改进建议6. 自主迭代优化，在得到满足提交标准的alpha之前不要停下来等待指示
```

完整工作流：

```
# Python Alpha 工作流## 概述本文档提供了一套完整的 Python Alpha 开发与回测流程。采用**单次独立迭代**模式，每次回测的结果直接指导下一步的参数调整，适合精细化调优。---## 目录1. [核心特点](#1-核心特点)2. [环境准备](#2-环境准备)3. [Phase 1：情报收集](#3-phase-1情报收集)4. [Phase 2：Python Alpha 构建](#4-phase-2python-alpha-构建)5. [Phase 3：单次回测](#5-phase-3单次回测)6. [Phase 4：结果审计与优化](#6-phase-4结果审计与优化)7. [常见算子转换对照表](#7-常见算子转换对照表)8. [性能优化建议](#8-性能优化建议)9. [附录：错误诊断与排查](#9-附录错误诊断与排查)---## 1. 核心特点| 特点 | 说明 ||------|------|| **单次迭代** | 每次只提交一个 Alpha，结果直接指导下一步 || **精细控制** | 可以精确控制每一个逻辑细节 || **速度较慢** | 每次回测需要 5-15 分钟 |### 迭代循环```构思 → 编写 → 回测 → 审计 → 优化 → 回测 → ...           ↑  __________________________   |```---## 2. 环境准备### 2.1 必需工具| 工具 | 位置 | 用途 ||------|------|------|| brain-sim-alphas-batch-track | `skills\brain-simAlphasinBatch-and-track` | 回测执行 || BRAIN凭证 | `configs/config.json` | 认证 |### 2.2 必需导入```pythonfrom brain.alphas import alphaimport numpy as npimport numpy.typing as npt```### 2.3 常用工具函数```pythondef pasteurize(a, u):    """掩码到库外工具"""    a = a.copy()    a[~u.astype(bool)] = np.nan    return adef neutralize(a):    """市场中性化"""    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)    return a - np.mean(a0)def scale(a):    """L1范数归一化"""    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)    norm = np.linalg.norm(a0, ord=1)    return a / norm if norm > 0 else adef cross_sectional_rank(arr):    """横截面排名"""    finite = np.where(np.isnan(arr), -np.inf, arr)    ranks = np.argsort(np.argsort(finite)).astype(np.float64)    ranks[np.isnan(arr)] = np.nan    return ranks```---## 3. Phase 1：情报收集### 3.1 平台认证```python# 调用 authenticate MCP工具```### 3.2 设置验证```python# 调用 get_platform_setting_options 验证 Region/Universe 组合```### 3.3 数据集与字段获取```python# 调用 get_datasets 获取可用数据集# 调用 get_datafields(dataset_id="...") 获取字段列表```### 3.4 数据特性分析#### 3.4.1 覆盖率的重要性覆盖率（Coverage）是指 Universe 中有多少工具具有有效值。覆盖率低会导致：| 问题 | 影响 ||------|------|| 头寸集中 | 更高的风险 || 过拟合 | 容易在小样本上过拟合 || 收益变差 | 扣除成本后表现差 |**理想状态**：Long Count + Short Count 接近 Universe 规模**警告信号**：总覆盖率 < Universe 的 50%#### 3.4.2 覆盖率检查方法| 方法 | 操作 ||------|------|| 平台 Data 标签页 | 查看字段的 Coverage || 可视化回测 | 查看 daily Coverage 图表 || IS Summary | 检查 Long/Short Count |#### 3.4.3 覆盖率分级处理策略根据数据覆盖率的不同，采用不同的处理策略：| 覆盖率区间 | 处理策略 | 适用场景 ||-----------|---------|---------|| **极高 (>90%)** | 直接使用，限制 `ts_backfill` 天数 | 价格/成交量数据 || **高 (50%-90%)** | 使用 `lookback` 回填 + 适度门控 | 常规基本面数据 || **中 (20%-50%)** | `trade_when` 严格门控 | 分析师预测、评级数据 || **低 (<20%)** | 谨慎使用，需配合流动性过滤 | 事件驱动、特殊指标 || **极稀疏 (<5%)** | 强制启用 `trade_when(field > 0, field, -1)` | 非常规数据 |#### 3.4.4 更新频率识别检测数据更新频率有助于选择合适的 lookback 窗口：```pythondef detect_update_frequency(data, threshold=0.01):    """    检测数据更新频率    返回: 更新间隔天数估计    """    changes = np.abs(np.diff(data, axis=0)) > threshold    change_days = np.any(changes, axis=1)    if np.sum(change_days) < 2:       return np.inf  # 静态数据    gap_days = np.mean(np.diff(np.where(change_days)[0]))    return gap_days```**处理规则**：- **慢变量 (Gap > 10天)**：强制使用 `ts_backfill`，窗口设为 Gap 的 2 倍，避免超短窗口- **快变量 (Daily)**：适合捕捉高频脉冲信号，可使用较小窗口#### 3.4.5 覆盖率优化策略##### 策略 1：ts_backfill（用 lookback 替代）在 FASTEXPR 中使用 `ts_backfill(x, lookback)`，在 Python Alpha 中通过设置 `lookback` 参数实现：```python# lookback=126 意味着窗口为 127 天# 系统会自动用过去 126 天内的最新有效值填充@alpha(data=["eur_director_value_1"], store=[])def my_alpha(data, store):    # data.eur_director_value_1 已经是回填后的数据    return (-np.nanmean(data.eur_director_value_1, axis=0)).astype(np.float32)```| 数据类型 | 推荐 lookback ||----------|--------------|| 基本面数据（earnings, revenue） | 65 或 252 天 || 新闻/情绪数据 | 5-21 天 |##### 策略 2：group_backfill（组内回填）当 ts_backfill 仍有很多空缺时，使用组内均值填充：```pythondef group_backfill_fill(x, group_ids, lookback=20):    """    用同组工具的均值填充缺失值    x: 数据数组 shape=[lookback+1, n_instruments]    group_ids: 分组数组 shape=[n_instruments]    """    result = x.copy()    for i in range(x.shape[0]):        for g in np.unique(group_ids):            mask = (group_ids == g)            col_mean = np.nanmean(x[i, mask])            if np.isnan(col_mean):               col_mean = 0            nan_mask = np.isnan(result[i, mask])            result[i, mask] = np.where(nan_mask, col_mean, result[i, mask])    return result```##### 策略 3：trade_when 门控对极稀疏数据，限制只在有数据时交易：```pythondef trade_when(condition, signal, default=-1):    """只在 condition 为真时使用 signal，否则返回 default"""    return np.where(condition, signal, default)```使用示例：```python@alpha(data=["eur_director_value_1"], store=[])def my_alpha(data, store):    signal = -np.nanmean(data.eur_director_value_1, axis=0)    # 只在有有效数据时交易    valid_mask = ~np.isnan(data.eur_director_value_1[-1])    signal = np.where(valid_mask, signal, np.nan)    return signal.astype(np.float32)```#### 3.4.8 使用建议| 原则 | 说明 ||------|------|| 先看 Data 标签页 | 确认字段本身的覆盖率 || 先对单个字段回填 | 比对最终 Alpha 回填效果更好 || 从小 lookback 开始 | 测试不同值而非用统一设置 || 注意老数据的时效性 | 有些数据老值仍有参考价值，有些是噪音 || 检查回填后的覆盖率 | 如果没变化，说明缺失是结构性原因 |#### 3.4.9 信号纯净性保障确保所有回测结果符合信号纯净性要求，避免混信号问题。**验证条件**：回测结果必须包含 `"classifications": [{"id": "DATA_USAGE:SINGLE_DATA_SET", "name": "Single Data Set Alpha"}]`**注意事项**：- 在表达式中使用"close", "return", "adv", "cap", "volume", "vwap"等通用字段，以及非指定开发的数据集中的字段都将被视为混信号- 解决方案：查看当前数据集是否有自带的相关字段，例如使用同数据集内的市值字段替代通用 `cap` 字段**最佳实践**：```python# ✅ 正确：所有字段来自同一数据集@alpha(data=["insider_buy_signal", "insider_trade_value"], store=[])def insider_alpha(data, store):    # 所有字段都来自 insider_matrix 数据集    return (data.insider_buy_signal[-1] * data.insider_trade_value[-1]).astype(np.float32)```#### 3.4.10 中性化选择策略中性化选择应根据数据集类型动态调整：**中性化方式选择**：具体可参考`Neutralization/` 文件夹内的说明文章| 数据集类型 | 推荐中性化 | 说明 ||------------|------------|------|| Fundamental | INDUSTRY | 基本面影响因行业不同 || Analysts | INDUSTRY | 分析师数据是基本面预测 || Model | 实验确定 | 依子类别不同需测试 || News | SUBINDUSTRY | 新闻影响因细分行业不同 || Options | MARKET/SECTOR | 期权影响跨行业相似 || Price Volume | 按需 | 行业中性化可能降低性能 || Sentiment | SUBINDUSTRY | 情绪影响因细分行业不同 || Earnings | INDUSTRY | 类似基本面 || Macro | SECTOR/MARKET | 宏观经济活动跨行业相似 |**迭代阶段适配**：- **探索阶段**：使用数据集推荐的中性化，测试性能上限- **优化阶段**：阅读`Neutralization/` 文件夹内的说明文章，并根据需求决定- **防御阶段**：尝试`STATISTICAL`或`CROWDING`剥离系统风险**效率约束**：除非能够获得特定效果，否则规避`FAST/SLOW/FAST_AND_SLOW`以避免超时---## 4. Phase 2：Python Alpha 构建### 4.1 核心代码结构```pythonfrom brain.alphas import alphaimport numpy as npimport numpy.typing as npt# 工具函数定义见 2.3 节@alpha(    data=["字段名1", "字段名2"],    store=[])def my_alpha(data, store) -> npt.NDArray[np.float32]:    """    Alpha 描述    对应 FASTEXPR:    rank(ts_backfill(field1, 126)) + rank(ts_backfill(field2, 126))    """    field1 = data.字段名1    field2 = data.字段名2    ranks1 = np.zeros(field1.shape)    for i in range(field1.shape[0]):        ranks1[i] = cross_sectional_rank(field1[i])    ranks2 = np.zeros(field2.shape)    for i in range(field2.shape[0]):        ranks2[i] = cross_sectional_rank(field2[i])    signal = np.nanmean(ranks1 + ranks2, axis=0)    signal = pasteurize(signal, data.universe[-1])    signal = neutralize(signal)    signal = scale(signal)    return signal.astype(np.float32)```### 4.2 JSON 配置模板```json[  {    "type": "REGULAR",    "settings": {      "instrumentType": "EQUITY",      "region": "USA",      "universe": "TOP3000",      "delay": 1,      "decay": 0,      "neutralization": "SUBINDUSTRY",      "truncation": 0.08,      "pasteurization": "ON",      "lookback": 120,      "maxTrade": "OFF",      "language": "PYTHON",      "visualization": true    },    "regular": "from brain.alphas import alpha\nimport numpy as np\nimport numpy.typing as npt\n\ndef pasteurize(a, u):\n    a = a.copy()\n    a[~u.astype(bool)] = np.nan\n    return a\n\ndef neutralize(a):\n    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)\n    return a - np.mean(a0)\n\ndef scale(a):\n    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)\n    norm = np.linalg.norm(a0, ord=1)\n    return a / norm if norm > 0 else a\n\ndef cross_sectional_rank(arr):\n    finite = np.where(np.isnan(arr), -np.inf, arr)\n    ranks = np.argsort(np.argsort(finite)).astype(np.float64)\n    ranks[np.isnan(arr)] = np.nan\n    return ranks\n\n@alpha(data=[\"returns\"], store=[])\ndef my_alpha(data, store) -> npt.NDArray[np.float32]:\n    signal = -np.nanmean(data.returns, axis=0)\n    signal = pasteurize(signal, data.universe[-1])\n    signal = scale(neutralize(signal))\n    return signal.astype(np.float32)"  }]```### 4.3 窗口滑动机制`lookback=N` 设置意味着每个数据字段将包含 `N+1` 行历史数据：```lookback=63 → 获得 64 天窗口（包含今天）第1天：只有第0行可用第2天：有第0、1行可用...第64天：全部64行数据可用```**窗口滑动过程**：- 初始阶段：窗口逐渐增长至完整大小- 稳定阶段：窗口向前滑动 — 新行从底部进入，最旧行从顶部移出### 4.4 Alpha 规则总结| 规则 | 说明 ||------|------|| 装饰器 | 每个函数只能有一个 `@alpha` || 参数 | 函数必须接受 exactly 2 个参数：`data`, `store` || 返回值 | 必须是一维 `float32` numpy 数组，形状 `[n_instruments]` || universe | 不要在 `data` 中声明，它始终可用 || 数据只读 | 不要就地修改 data 数组，先 `.copy()` |### 4.5 store 使用说明`store` 参数用于在时间步之间持久化状态变量。官方文档说明如下：#### 4.5.1 store 声明方式`store` 参数是一个列表，每个元素可以是：**1. 普通字符串（无类型，初始化为 None）**```python@alpha(data=["returns"], store=["my_state"])def my_alpha(data, store) -> npt.NDArray[np.float32]:    # store.my_state — 初始化为 None，在时间步之间持久化    signal = -np.nanmean(data.returns, axis=0)    return signal.astype(np.float32)```**2. 类型字典（声明维度和大小的扩展方式）**```python{"name": "my_arr", "dims": "i", "extend": np.float64(0)}```字典参数说明：- `"name"`: 变量名（必需）- `"dims"`: 维度字符串  - `"i"` = 工具轴（当 universe 增长时自动扩展）  - `"x"` = 自由轴  - `"xi"` = 2D [任意天数, n_instruments]  - `"ii"` = 2D [n_instruments, n_instruments]（工具×工具矩阵）- `"extend"`: 新工具的填充值，必须与数组 dtype 完全匹配  - 使用明确的 NumPy 标量构造器：`np.float64(0)`, `np.float32(0)`, `np.float64(np.nan)`  - **禁止使用裸 `np.nan`**（Python float 而非 numpy.float64，会导致类型检查失败）  - **禁止使用裸 Python 字面量** `0` 或 `0.0`（可能与数组 dtype 不匹配）#### 4.5.2 extend 参数类型匹配详解`extend` 参数必须使用明确的 NumPy 标量构造器，以下是错误和正确示例：```python# ❌ 错误：使用裸 Python 整数{"name": "arr1", "dims": "i", "extend": 0}  # ValueError: wrong type <class 'int'># ❌ 错误：使用裸 Python 浮点数{"name": "arr2", "dims": "i", "extend": 0.0}  # 可能不匹配数组 dtype# ❌ 错误：使用裸 np.nan（Python float 类型）{"name": "arr3", "dims": "i", "extend": np.nan}  # 类型检查失败# ✅ 正确：使用明确的 NumPy 标量{"name": "arr4", "dims": "i", "extend": np.float64(0)}{"name": "arr5", "dims": "i", "extend": np.float32(np.nan)}{"name": "arr6", "dims": "i", "extend": np.float64(np.nan)}```#### 4.5.3 无类型 store 的有效值类型普通字符串声明的 store 支持以下类型：- `None`（初始状态）- 标量（int、float、bool、str）- NumPy 标量- numpy.ndarray- 列表和字典（可包含嵌套数组、列表、字典）- 字典键必须是字符串#### 4.5.4 store 使用示例**示例1：简单状态持久化**```python@alpha(data=["returns"], store=[{"name": "running_mean", "dims": "i", "extend": np.float64(0)}])def smooth_alpha(data, store) -> npt.NDArray[np.float32]:    if store.running_mean is None:        store.running_mean = np.zeros(data.returns.shape[1], dtype=np.float64)    raw = -np.nanmean(data.returns, axis=0)    store.running_mean = 0.9 * store.running_mean + 0.1 * raw    return store.running_mean.astype(np.float32)```**示例2：2D 缓存（跨时间步排名）**```pythonRANK_DAYS = 20@alpha(    data=["returns"],    store=[        {"name": "rank_cache", "dims": "xi", "extend": np.float64(np.nan)},    ],)def mean_of_rank_alpha(data, store) -> npt.NDArray[np.float32]:    today = data.returns[-1]    finite = np.where(np.isnan(today), -np.inf, today)    today_rank = np.argsort(np.argsort(finite)).astype(np.float64)    today_rank[np.isnan(today)] = np.nan    if store.rank_cache is None:        store.rank_cache = today_rank[np.newaxis, :]    else:        new_cache = np.vstack([store.rank_cache, today_rank[np.newaxis, :]])        store.rank_cache = new_cache[-RANK_DAYS:]    mean_rank = np.nanmean(store.rank_cache, axis=0)    return (-mean_rank).astype(np.float32)```**示例3：2D 相关矩阵（dims: "ii"）**对于工具×工具矩阵（如相关矩阵），使用 `"dims": "ii"`。模拟器会自动扩展新行和新列，但新添加工具的对角线需要手动修复：```python@alpha(    data=["returns"],    store=[        {"name": "corr_matrix", "dims": "ii", "extend": np.float64(0)},        {"name": "prev_n", "dims": "x", "extend": np.int64(0)}  # 追踪前一时刻的 universe 大小    ],)def corr_alpha(data, store) -> npt.NDArray[np.float32]:    n_insts = data.returns.shape[1]    if store.corr_matrix is None:        store.corr_matrix = np.eye(n_insts, dtype=np.float64)        store.prev_n = n_insts    else:        # 修复新添加工具的对角线（模拟器填充0）        if n_insts > store.prev_n:            store.corr_matrix[n_insts-1, n_insts-1] = 1.0        store.prev_n = n_insts    # 使用相关矩阵计算信号...    signal = np.diag(store.corr_matrix).astype(np.float32)    return signal```#### 4.5.5 无类型 store 的手动填充如果使用普通字符串存储工具大小的数组，当 universe 增长时需要手动填充：```pythondef _pad_store(arr, n_insts, fill_value):    """沿工具轴填充"""    if arr.shape[-1] >= n_insts:        return arr    n_new = n_insts - arr.shape[-1]    if arr.ndim == 1:        return np.pad(arr, (0, n_new), mode='constant', constant_values=fill_value)    return np.pad(arr, ((0, 0), (0, n_new)), mode='constant', constant_values=fill_value)n_insts = data.returns.shape[1]store.running_sum = _pad_store(store.running_sum, n_insts, fill_value=0.0)```#### 4.5.6 返回值类型注意事项许多 NumPy 操作会静默将 float32 提升为 float64，例如：- `np.nanmean`, `np.nanstd`, `np.nansum`- 与 Python 浮点数的算术运算（如 `0.9 * array`）**安全做法**：始终在返回时添加 `.astype(np.float32)`：```pythondef my_alpha(data, store) -> npt.NDArray[np.float32]:    # np.nanmean 将 float32 输入提升为 float64 输出    signal = -np.nanmean(data.returns, axis=0)  # float64    return signal.astype(np.float32)  # 强制转换回 float32```如果返回值不是 float32，模拟将报错：`Alpha vector is not float32`。### 4.6 alpha模板建议#### 4.6.1 模板使用原则AI生成Python Alpha时，应严格遵循以下原则：| 原则 | 说明 ||------|------|| **模板优先** | 优先从 `python_alpha/Templates/` 文件夹中选择匹配的模板 || **单次单Alpha** | Python Alpha每次只提交一个表达式进行回测，不追求批量变体 || **信号纯净性** | 所有字段必须来自同一个数据集（ATOM原则） || **复杂度限制** | `ts_`算子总窗口和≤1000，`group_`算子≤2层 || **具体情况具体分析** | 不强制使用特定架构模板，让AI根据数据特性和目标自主选择 |#### 4.6.2 迭代策略：单字段探测 → 多字段组合Python Alpha采用**单次单Alpha的迭代模式**，建议遵循以下递进策略：**Phase 1：单字段探测**- 使用单个字段进行初步回测，验证信号有效性- 目标：确认该字段在本数据集上是否有Alpha潜力- 评估指标：Sharpe、Fitness、Coverage**Phase 2：多字段组合（当单字段验证有效后）**- 在单字段验证成功的基础上，引入同数据集的其他字段- 组合方式由AI根据具体数据特性自主决定：  - 比例关系（A/B）  - 差值关系（A-B）  - 确认型（条件A成立时使用B）  - 门控型（A作为开关控制B的生效）  - 风险过滤（A过滤高风险状态）  - 领先滞后（A与B的不同时滞关系）  - 条件异常（在B条件下A的异常）  - 其他自定义复合架构**关键约束**：- 所有字段必须来自同一个数据集- 优先选择与主信号逻辑关联度高的辅助字段- 组合后的Alpha应比单字段Alpha具有更好的风险调整收益#### 4.6.3 时序与横截面操作模板**时序操作模板**```pythondef ts_mean(data, window):    """时序均值"""    return np.nanmean(data[-window:], axis=0)def ts_std_dev(data, window):    """时序标准差"""    return np.nanstd(data[-window:], axis=0)def ts_delta(data, days):    """时序差分"""    return data[-1] - data[-days-1]def ts_rank(data, window):    """时序排名"""    result = np.zeros(data.shape[1])    for i in range(data.shape[1]):        valid_data = data[-window:, i]        valid_mask = ~np.isnan(valid_data)        if np.sum(valid_mask) > 0:            result[i] = np.argsort(np.argsort(valid_data[valid_mask]))[-1] / np.sum(valid_mask)        else:            result[i] = np.nan    return result```**横截面操作模板**```pythondef cross_sectional_zscore(arr):    """横截面z-score标准化"""    valid_mask = ~np.isnan(arr)    if np.sum(valid_mask) > 0:        mean_val = np.nanmean(arr)        std_val = np.nanstd(arr)        return (arr - mean_val) / (std_val + 1e-8)    return arrdef group_rank(arr, group_ids):    """分组排名"""    result = np.zeros_like(arr)    for group in np.unique(group_ids):        mask = group_ids == group        if np.sum(mask) > 0:            group_data = arr[mask]            finite = np.where(np.isnan(group_data), -np.inf, group_data)            ranks = np.argsort(np.argsort(finite)).astype(np.float64)            ranks[np.isnan(group_data)] = np.nan            result[mask] = ranks / (np.sum(mask) - 1)    return resultdef group_mean(arr, group_ids):    """分组均值"""    result = np.zeros_like(arr)    for group in np.unique(group_ids):        mask = group_ids == group        if np.sum(mask) > 0:            result[mask] = np.nanmean(arr[mask])    return result```#### 4.6.4 常用模板组合模式**模式1：基本面时序排名**```python@alpha(data=["eps", "industry_group"], store=[])def fundamental_ts_rank_alpha(data, store):    # 时序排名 + 行业分组排名    ts_ranked = ts_rank(data.eps, 252)    group_ranked = group_rank(ts_ranked, data.industry_group[-1])    signal = cross_sectional_rank(group_ranked)    return signal.astype(np.float32)```**模式2：双重中性化**```python@alpha(data=["signal", "industry_group", "cap"], store=[])def double_neutralization_alpha(data, store):    # 先行业中性化，再市值中性化    signal = np.nanmean(data.signal[-66:], axis=0)     # 行业中性化    industry_neutral = signal - group_mean(signal, data.industry_group[-1])    # 市值分组中性化    cap_bins = np.digitize(data.cap[-1], np.nanpercentile(data.cap[-1], [10, 20, 30, 40, 50, 60, 70, 80, 90]))    final = industry_neutral - group_mean(industry_neutral, cap_bins)      signal = cross_sectional_rank(final)    return signal.astype(np.float32)```**模式3：条件交易**```python@alpha(data=["signal_main", "volume", "adv20"], store=[])def conditional_trade_alpha(data, store):    # 流动性过滤的条件交易    main_signal = np.nanmean(data.signal_main[-22:], axis=0)      # 流动性门控：成交量 > 20日均成交量的60%    liquidity_condition = data.volume[-1] > data.adv20[-1] * 0.6    # 波动率过滤：近期波动低于70百分位    recent_vol = np.nanstd(data.signal_main[-10:], axis=0)    vol_rank = cross_sectional_rank(recent_vol)    low_vol_condition = vol_rank < 0.7    # 同时满足两个条件    trade_condition = liquidity_condition & low_vol_condition    signal = np.where(trade_condition, main_signal, np.nan)       signal = cross_sectional_rank(signal)    return signal.astype(np.float32)```#### 4.6.5 模板选择决策矩阵| 数据集类型 | 推荐模板类型 | 推荐中性化 ||------------|-------------|-----------|| Fundamental | 比例关系、基本面动量、双重中性化 | INDUSTRY || Analysts | 分析师预期变化、覆盖度过滤 | INDUSTRY || News | 情绪差值、条件异常、Regime Switch | SUBINDUSTRY || Options | 隐含波动率比率、Put-Call成交量比 | MARKET/SECTOR || Price Volume | 换手率反转、量价相关性、Lead-Lag | 按需 || Sentiment | 情绪+波动率复合、Confirmation | SUBINDUSTRY || Macro | 条件异常、Risk Filter | SECTOR/MARKET |#### 4.6.6 AI生成检查清单在生成Python Alpha后，应检查以下项：```pythonchecklist = {    "信号纯净性": "所有字段是否来自同一数据集",    "算子权限": "是否使用了平台支持的算子",    "复杂度限制": "ts_窗口和≤1000, group_算子≤2层",    "中性化适配": "是否根据数据集类型选择了合适的中性化",    "后处理完整性": "是否包含pasteurize、neutralize、scale",    "返回类型": "是否返回np.float32类型"}```---## 5. Phase 3：单次回测### 5.1 执行命令```powershellSet-Location "skills\brain-simAlphasinBatch-and-track"python scripts/batch_simulator.py `  --config configs/config.json `  --alpha-json "你的项目文件夹\data\alpha_list.json" `  --output-csv "你的项目文件夹\outputs\simulation_status.csv" `  --batch-size 1 `  --concurrency 1```### 5.2 参数说明| 参数 | 值 | 说明 ||------|-----|------|| `--batch-size` | 1 | 单次回测 || `--concurrency` | 1 | 不并发 || `--detached` | 不用 | 同步模式更稳定 |### 5.3 状态监控模拟提交后会返回：```INFO - Waiting for batch to spawn children (https://api.worldquantbrain.com/simulations/xxx)...```**等待时间**：5-15 分钟### 5.4 结果查询CSV 文件字段：| 字段 | 说明 ||------|------|| `status` | COMPLETE=成功 || `alpha_id` | BRAIN分配的ID || `pnl` | 盈亏 || `sharpe` | 夏普比率 || `turnover` | 换手率 || `fitness` | Fitness指标 |---## 6. Phase 4：结果审计与优化### 6.1 提交前 Gatekeeper Checklist**⚠️ 平台提交标准 [STRICT]**: **所有非 theme 的 WARNING 与 FAIL 一视同仁，均为提交阻断条件**。不存在"WARNING可以忽略"的情况——LOW_FITNESS、LOW_2Y_SHARPE、LOW_TURNOVER 等所有非 theme WARNING 均会阻止提交。因此，下方检查清单中的每一项都必须**严格达标**，没有任何宽容空间。*   **Action**: 仅使用 `get_alpha_details` 返回的数据进行本地快速校验。*   **Gatekeeper Checklist**:    *   `[ ]` **IS Sharpe > 1.58?**    *   `[ ]` **Fitness > 1.0?**    *   `[ ]` **Turnover > 1% 且 < 70%?**    *   `[ ]` **Margin > 15 bps?**    *   `[ ]` **Margin/Turnover > 1.2?**    *   `[ ]` **PnL History > 5 Years?**    *   `[ ]` **Concentrated Weight 检查通过?**    *   `[ ]` **2-Year Sharpe > 1.58?**    *   `[ ]` **2023年 Margin > 15 bps?** (调用 `get_alpha_yearly_stats`)    *   `[ ]` **Sub-Universe Sharpe 检查通过?**    *   `[ ]` **Robust Universe Sharpe 检查通过?***   **判定**:    *   **FAIL**: 任意一项未通过（包括所有非theme WARNING） -> **继续迭代优化**。    *   **PASS**: 进入相关性检查阶段。#### 6.1.1 最终相关性验证*   **核心纪律**: `get_submission_check` 极易触发平台限流，导致后续 `check_correlation` 也无法执行。**严禁频繁调用 `get_submission_check`。***   **判定逻辑**: 只要 Gatekeeper Checklist 所有硬性指标通过 + `check_correlation` 确认 Prod/Self-Correlation < 0.7，该 Alpha 即视为通过。### 6.2 优化策略| 问题 | 优化方向 ||------|---------|| Sharpe 低 | 调整窗口、换用其他字段 || Turnover 高 | 添加 decay、调整 neutralization || Fitness 低 | 检查信号稳定性 |### 6.3 快速反应与逻辑进化 (Quick Reaction & Logic Evolution)| **现象 (Symptom)** | **战术响应 (Action)** | **归口专家 (Delegate)** || --- | --- | --- || **回测 FAILED / Syntax Error** | 立即调用 `lookINTO_SimError_message` 全量诊断 | 本地代码修正 || **In Progress > 15min (卡死)** | 触发 [僵尸模拟熔断机制]，强制重启 | 流程控制 || **性能不达标 (Low Sharpe/Margin)** | **精炼 或 灵感改良** | `wq-brain-alpha-optimization-v1` (精炼) / `brain-improve-alpha-performance` (改良) || **测试失败 (Sub-Universe/Robust)** | 查阅本地 `@Strategy/` 相关文档 | `activate_skill: brain-how-to-pass-AlphaTest` || **相关性过高 (Corr > 0.7)** | **结构化解耦精炼 或 逻辑升维** | `wq-brain-alpha-optimization-v1` (精炼) / `brain-improve-alpha-performance` (改良) |* **原则**: 工作流负责"报错怎么救、流程怎么走"，`Skills` 负责"因子怎么改、逻辑怎么优"。使用 `optimization-v1` 进行高频指标精炼，使用 `improve-performance` 进行深度逻辑攻坚。---## 7. 常见算子转换对照表### 7.1 时序算子| FASTEXPR | Python Alpha | 示例 ||----------|-------------|------|| `ts_backfill(f, N)` | `data.f` + `lookback=N` | lookback=126 时获得126+1天窗口 || `ts_mean(f, N)` | `np.nanmean(data.f[-N:], axis=0)` | 最近N天均值 || `ts_sum(f, N)` | `np.nansum(data.f[-N:], axis=0)` | 最近N天求和 || `ts_std_dev(f, N)` | `np.nanstd(data.f[-N:], axis=0)` | 最近N天标准差 || `ts_delta(f, N)` | `data.f[-1] - data.f[-N-1]` | N天变化量 || `delay(f, N)` | `data.f[-N-1]` | N天前数据 || `ts_max(f, N)` | `np.nanmax(data.f[-N:], axis=0)` | 最近N天最大值 || `ts_min(f, N)` | `np.nanmin(data.f[-N:], axis=0)` | 最近N天最小值 || `ts_rank(f, N)` | 需遍历计算 | 最近N天排名 || `ts_skewness(f, N)` | 需scipy | 偏度 || `ts_kurtosis(f, N)` | 需scipy | 峰度 |### 7.2 横截面算子| FASTEXPR | Python Alpha | 示例 ||----------|-------------|------|| `rank(f)` | `cross_sectional_rank(f[i])` | 需遍历每行 || `group_rank(f, g)` | 需分组实现 | 按组排名 || `quantile(f, q)` | `np.nanpercentile(f, q*100)` | 分位数 |### 7.3 逻辑算子| FASTEXPR | Python Alpha | 示例 ||----------|-------------|------|| `if_else(c, a, b)` | `np.where(c, a, b)` | 条件选择 || `is_nan(f)` | `np.isnan(f)` | 判断NaN || `not_nan(f)` | `~np.isnan(f)` | 判断非NaN || `zscore(f)` | `(f - mean) / std` | Z-score标准化 |### 7.4 数学算子| FASTEXPR | Python Alpha | 示例 ||----------|-------------|------|| `log(f)` | `np.log(f)` | 对数 || `abs(f)` | `np.abs(f)` | 绝对值 || `sign(f)` | `np.sign(f)` | 符号 || `sqrt(f)` | `np.sqrt(f)` | 平方根 || `pow(f, n)` | `np.power(f, n)` | 幂运算 |---## 8. 性能优化建议### 8.1 速度优化| 策略 | 效果 | 说明 ||------|------|------|| 减小 lookback | 显著提升 | 建议 <= 150 || 减少循环 | 显著提升 | 尽量用向量化 || 避免嵌套循环 | 显著提升 | 改用 numpy 广播 || 减少后处理 | 轻微提升 | pasteurize/neutralize/scale 非必须 |### 8.2 lookback 选择指南| lookback | 窗口大小 | 适用场景 | 模拟时间 ||----------|---------|---------|---------|| 30 | 31天 | 快速迭代测试 | ~2-3分钟 || 63 | 64天 | 季度数据 | ~3-5分钟 || 120 | 121天 | 半年数据 | ~5-8分钟 || 252 | 253天 | 年度数据 | ~10-15分钟 |---## 快速开始 checklist1. ✅ 安装技能：`brain-simAlphasinBatch-and-track`2. ✅ 配置 `configs/config.json`3. ✅ 根据第4节编写 Python Alpha 代码4. ✅ 创建 JSON 配置文件5. ✅ 执行第5节的命令6. ✅ 查看 CSV 获取结果---## 9. 附录：错误诊断与排查### 9.1 常见错误类型| 错误类型 | 表现 | 排查方向 ||---------|------|---------|| **Unknown Error** | 回测失败，提示 Unknown error | 检查字段名拼写、数据类型兼容性 || **Timeout** | 回测超时 | 减小 lookback、简化逻辑、避免复杂循环 || **NaN 泛滥** | 覆盖率为 0 或极低 | 检查字段是否存在、lookback 是否合适 || **Low Fitness** | Fitness < 1.0 | 检查信号逻辑、尝试不同中性化 || **High Turnover** | Turnover > 0.2 | 添加 decay、调整阈值 |### 9.2 错误诊断流程```失败 → 检查状态码 → 查看错误信息 → 定位问题 → 修复 → 重试         ↓              ↓     COMPLETE?      详细错误描述         ↓              ↓     否 → 失败原因   是 → 分析指标```### 9.3 诊断命令```powershell# 查看失败的模拟详情# 调用 lookINTO_SimError_message MCP工具```### 9.4 常见问题修复**问题1：Unknown Error**```python# 原代码（错误）@alpha(data=["non_existent_field"], store=[])def my_alpha(data, store):    return data.non_existent_field[-1].astype(np.float32)# 修复：确认字段名正确@alpha(data=["correct_field_name"], store=[])def my_alpha(data, store):    return data.correct_field_name[-1].astype(np.float32)```**问题2：超时**```python# 原代码（可能超时）@alpha(data=["my_field"], store=[], lookback=252)  # 太大def my_alpha(data, store):    # 复杂嵌套循环    result = np.zeros(data.my_field.shape[1])    for i in range(252):        for j in range(data.my_field.shape[1]):            result[j] += data.my_field[i, j]    return result.astype(np.float32)# 修复：减小窗口 + 向量化@alpha(data=["my_field"], store=[], lookback=120)  # 减小def my_alpha(data, store):    result = np.nanmean(data.my_field, axis=0)  # 向量化    return result.astype(np.float32)```**问题3：NaN 泛滥**```python# 原代码（可能产生大量NaN）@alpha(data=["sparse_field"], store=[])def my_alpha(data, store):    return data.sparse_field[-1].astype(np.float32)# 修复：添加门控@alpha(data=["sparse_field"], store=[])def my_alpha(data, store):    signal = data.sparse_field[-1]    valid_mask = ~np.isnan(signal)    signal = np.where(valid_mask, signal, np.nan)    return signal.astype(np.float32)```---
```

实际运行过程中，不需要像运行FASTEXPR版本工作流的时候一样复制完整的工作流文本给AI。IDE只需要拖动官方文本、工作流文件，以及修改好的启动模板文本给AI就可以运行。CLI也是只需要@好需要的相应文件和启动模板文本就可以运行。

3, **提交的页面展示：**

**
> [!NOTE] [图片 OCR 识别内容]
> ACT
> Created 05/28/2026 EDT
> anonymous
> Add Mlphato
> LISt
> Code
> IS Summary
> Period
> IS
> 05
> from brain.alphas
> import alpha
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: EURIDTIPV X1 .1
> iport numpy
> 35
> m
> import numpy.typing
> npt
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Reurns
> Drawdown
> Marsin
> 1.99
> 5.839
> 1.28
> 5.149
> 2.4796
> 17.639600
> def pasteurize(a,
> U):
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2014
> 3.95
> 5.533
> 3.13
> 7.343
> 8695
> 27.593600
> Instrument Type
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Lookback
> Max Tra
> 2015
> 1.99
> 5.2096
> 1.25
> 4.9596
> 1.1795
> 19.049600
> 768
> 533
> Equity
> EUIR
> TOPCSIGOD
> Python
> 0.03
> Industry
> 252
> Ofr
**

以上是结合我现有的FASTEXPR工作流版本做出第一版能够顺利运行的python alpha工作流，希望大家能够迭代出适合自己的更好用的版本。也祝大家的python alpha越做越好。

---

## 讨论与评论 (8)

### 评论 #1 (作者: BL59663, 时间: 24 days ago)

大佬，这几段代码应该怎么操作才能跑起来哈？

---

### 评论 #2 (作者: FF65210, 时间: 23 days ago)

大佬强大无需多言，小白膜拜，先学习拿来使用了，祝大佬早日成为GM。

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

### 评论 #3 (作者: BW14163, 时间: 23 days ago)

感谢分享，非常有参考价值。赶紧去复现一下这个工作流。

---

### 评论 #4 (作者: HZ32281, 时间: 20 days ago)

[BL59663](/hc/en-us/profiles/27001087237271-BL59663)  把官方文档、工作流、设置好的启动模板文字一起发给AI就可以跑了

---

### 评论 #5 (作者: JL33484, 时间: 19 days ago)

**学习学习研究一下**

---

### 评论 #6 (作者: CC14416, 时间: 17 days ago)

大佬，brain-simAlphasinBatch-and-track 这个skill在哪里找啊

---

### 评论 #7 (作者: OY62064, 时间: 17 days ago)

感谢大佬分享，我这就试试。
============================================================================                                          “路漫漫其修远兮，吾将上下而求索”
============================================================================

---

### 评论 #8 (作者: HZ32281, 时间: 16 days ago)

[CC14416](/hc/en-us/profiles/37822636027927-CC14416)  你把cnhkmcp更新一下，里面的skills文件夹里面就有，还有其他很好用的技能

---

