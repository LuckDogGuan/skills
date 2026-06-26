# 【Community Leader -因子构造 💎】TRAE+MCP 自动挖掘因子经验分享

- **链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子构造 】TRAEMCP 自动挖掘因子经验分享_37116093087895.md
- **作者**: GX42576
- **发布时间/热度**: 6 months ago, 得票: 30

## 帖子正文

首先要感谢
OB53521、CR35762两位大佬关于AI挖掘因子的分享，真的给了我很多启发！不过我发现，两位大佬分享的命令界面操作方式，对部分朋友来说可能存在一定难度。所以今天特意把自己自用的挖掘流程整理出来，希望能帮到有需要的伙伴。
我是10月22日转的顾问，直到12月9日之前，一直都没找到因子构建和批量测试的有效方法，那段时间真的很迷茫，甚至恍惚间觉得要完蛋了。后来在论坛学习到《【AI/MCP精选合集】创建一个具有BRAIN全部知识+金融博士+计算机博士的免费助手》，才总算找到了前进的方向。在这期间，我也一直在尝试通过TREA和VS Code测试、构建AI半自动工作流，但多次尝试都没能成功。真正的转机出现在12月7日，听完OB53521大佬的分享后，我瞬间理清了思路。

12月8日，我开始用AI对IND区域进行测试，没想到第一轮测试仅用20分钟就出了第一个Alpha！这个结果给了我极大的鼓舞，也让我更有动力继续探索。

截至今天投稿，我在IND区域累计回测2800多次，提交因子16个，还有4个因子待提交。日常的工作节奏大概是这样的：每天回测次数基本在1300左右，工作模式以看盘为主，每小时左右关注一次测试是否中断，然后判定是继续当前测试还是开启新一轮。工作时间基本固定在7:00-22:00。

12月9日 提交第一个正式 Alpha


> [!NOTE] [图片 OCR 识别内容]
> 12/09/2025
> Submitted Alphas:
> Oe Oe ce
> 21,Jul
> 28.Jul
> &U
> NOV
> NO
> Now
> . Nov


累计回测数量


> [!NOTE] [图片 OCR 识别内容]
> anonymoUs
> Regular
> UNSUBMITTED
> 12/18/2025 EST
> IND
> TOPSOO
> Page size
> Out Of 2,841


提交的Alpha （基本PC在6.5左右 感觉还是很危险）


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> (ESTI
> Searcn
> Selec
> Selec
> Selec
> Searcn
> IND
> Selec
> Regular
> ACTIVE
> 12118/2025 EST
> IND
> TOPSOO
> Up-0.67
> Reaular
> ACTIVE
> 12118/2025 EST
> IND
> TOPSOO
> 59-??
> Regular
> ACTIVE
> 12/1712025 EST
> IND
> TOPSOO
> 0p-0.55
> Regular
> ACTIVE
> 12/16/2025 EST
> IND
> TOPSOO
> Up-0.56
> Regular
> ACTIVE
> 12116/2025 EST
> IND
> TOPSOO
> Regular
> ACTIVE
> 12115/2025 EST
> IND
> TOPSOO
> Regular
> ACTIVE
> 12115/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12114/2025 EST
> IND
> TOPSOO
> Regular
> ACTIVE
> 12114/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12114/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12113/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12113/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12113/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12113/2025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12/1112025 EST
> IND
> TOPSOO
> anonymoUs
> Regular
> ACTIVE
> 12/1112025 EST
> IND
> TOPSOO
> UD 0.
> UD-
> 40-6.9


我这套自用流程，对新手来说最便捷的点主要有这几个：

1. 兼容性强，Windows系统和macOS系统都能使用；

2. 采用图形化中文界面，需要用到的编程和设置操作极少，上手门槛低；

3. 支持多种AI模型测试，选择范围广；

4. 国内版本为免费使用，不过有会话限制，需要注意测试节奏。

我个人使用的是国际版包月服务，费用很便宜。对我来说性价比很高，提交因子仅6天就把包月费用赚回来了，估计大佬们提交一个因子就能覆盖成本了。

下面附上我日常使用的设置截图以及所用AI的提示词配置

MCP 安装后样式（如果不知道在TRAE如何安装MCP，可看论坛《Trae配置使用mcp》）


> [!NOTE] [图片 OCR 识别内容]
> IDE
> 文件(
> 编辑旧
> 选择(5)
> 查看0
> 转到(G)
> 终端[
> 帮助(H)
> TRAE
> Q 搜索
> 曰起手式 tt
> 智能体
> MCP
> 0
> 8
> MCP
> 添加
> worldquant-brain-platfom 企
> 症
> authenticate
> Authenticate with WorldQuant BRAIN platform。 This is the f。
> @
> value_factor_trendScore
> Compute and return the diversit score for REGULARalphasin
> 器
> manage_config
> Manage confguration settings - get or update configuratio.
> 百
> create_simulation
> Create
> new simulation on BRAIN platform。This tool create。。
> alpha_details
> Get detailed informationaboutan alpha
> alpha_id: The
> get_datasets
> Get avallable datasets for research。 Use this to discover what
> datafields
> Get available data fields foralpha constnuction Use this to fi
> get_alpha_pnl
> Get Pnl (Proftand Loss) data foranalpha。
> alpha_id: T
> User_alphas
> Usersalphas with advanced fltening; pagination; and SOC。。
> ar
> get
> Args;
> get
> Arg
> get
> Get


运行流程：

1.创建对应的智能体，勾选MCP


> [!NOTE] [图片 OCR 识别内容]
> 智能体
> IND500自动
> 智能生成
> 名称
> IND500自动
> 8/20
> 提示词
> Role: WorldQuant BRAIN 全自动首席研究员 (Auto-Researcher]
> ##顾问: Tcxg | 版本:5.0 (Gimini Enhanced)
> *角色定Y:
> 7862/10000
> 可被其他智能体调用
> SOLJl
> 可被其他智能体调用
> 目前仅以被5010模式中的 SOLO Coder 调用。
> 蜚耻裆
> 工具 @
> 工具
> MCP
> 添加 MCP Servers
> worldquant-brain-platform 公
> 工具-内置
> 阅读
> 对文件进行检索和查看
> 综辑
> 对文件进行增8和寐辑
> 终端
> 在终峁运行命令并获取状态和结果
> 预览
> 在生成前弟结果后提供秘览入C
> 保存
> 取消


2、选择智能体后，提问发起自动挖掘

```
IND,1,500 开始研究- 分析IND区域未点亮的金字塔。- 优先挖掘单一数据集。
```


> [!NOTE] [图片 OCR 识别内容]
> IND500自动
> 思考过程
> 0/5 己完成
> 认证并获取 IND 区域金字塔状态。识别末点完区域
> 选择目标数据集并进行情报收集 [文档;字段
> 构建并提交第一批 Alpha (Level
> 基础信号
> INDTTOPSOO
> 分析回测结果并进行迭代 (Level 2
> 中性化 / Level 3 - 交易控制
> 生成研究报告并保存至 AIResearchReports
> Worldquant-brain-platiormlauthenticate
> Thought
> Worldquant-brain-platiormget_pyramid_alphas
> TRAEIHOWTOUseAIIDatasets
> Worldquant-brain-platiormget_datasets
> Thought
> 1/6已完成
> ]证并获职 +AI8 区O金字糌状态
> 识别点完区域
> 深入分析 analyst4 数据集 [文档;字段;算子]并构建 Level
> Alpha
> 选择目标数据集并进行倩报收集 (文档;字段鼾
> 构建并提交第一批 Nlpha (Level
> 基础信号
> INDTTOPSOO
> 分析回测结果并进行迭代 (Level
> 中性化 / Level
> 交易控制
> 生成研究报告并保存至 AIResearchReports
> 野



> [!NOTE] [图片 OCR 识别内容]
> 构建并提交第
> 批 Nlpha (Level
> 基础信号
> INDTTOPSOO
> 分析回测结果并进行迭代 (Level
> 中性化
> Level
> 交易控制
> Taxg 顾问报告: IND 区域 Alpha 研究任务完咸
> 我们成功攻克了 IND (ndia) Region 的 Analyst Estimates 领域 (属于未点亮的 Pyramid)
> 经过多轮迭代与故障排除。最终锁
> 定了-个高质量 Alpha。
> 核心咸果 (Key Achievements)
> Best Alpha I0:
> IYSpRpXK
> Perfommance Metrics:
> Sharpe: 2.36 (显著商于阈值
> 58)
> Fitness: 2.26 (极佳的稳定性)
> Turnover: 10.67% (低换手
> 适合大资金
> Submission Check:
> ALLPASSED (包舍 Prod Correlation 0.0, Self Correlation
> 0.4)
> Alpha 详情
> 逻辑: Earnings Revision Momentum [盈利预测修正动量)
> 捕捉分析师对公司 EPS 预期持续上调的趋势。
> 表达式:
> JavaScript



> [!NOTE] [图片 OCR 识别内容]
> 构建细节:
> 煳用
> tS_ZSCOFB(:.
> 601
> 捕捉中长期趋势。过滤短期噪音。
> 煳用
> SECTOR  中性化 (优于 Industry)
> 在 Top 500 这种集中度较高的 Universe 中更有效。
> 研究历程与故障排除
> 1.障碍:初期  analystg 数据集模拟遵遇平台连续 Cancellation。
> 2.应对:
> 执行 Pivot 策略。临时切换至  analyst39
> (Fundamenta]) 保持产出 [获得 Sharpe ~1.16)。
> Retry 策略:坚持重试  analystg 并调整中性化参数。最终成功复活该高分逻辑。
> 3。优化:对比了 Industry (Sharpe 2.31)与 Sector (Sharpe 2.36] 中性化。最终选择了 Sector。
> 交付物
> 完整研究报告己生成:
> 0: |I0砑宄 |TRAEIAIResearchReports | IND_Analyst_Revision_ 801_20251218.p
> 建议:您可以直接在平台上提交 Alpha |IYSpRpxK
> 它是-个非常稳健且独特的信号


模型选择：不同的提示词，每个AI的反馈不一样，这需要大家多尝试。（目前使用较好的是 DeepSeek、GPT、Gemini）


> [!NOTE] [图片 OCR 识别内容]
> Auto Mode
> Max Mode
> 超级{型
> Gemini-3-Pro-Preview
> Gemini-3-Pro-Preview (2Ok) 2rsqussts
> Gemini-Z5-Pro
> Kimi-K2-0905
> GPT-5.2 Bsta
> GPT-51
> GPT-S-medium
> GPT-S-high
> DeepSeek-V31
> 
> 诱加


可能出现的问题：


> [!NOTE] [图片 OCR 识别内容]
> 椟型思考次数已达上展。请揄入"继续"后获得更条结果。
> 异常打断
> 凸 q # 3


这个是TRAE自生设置的限制，避免AI进入死循环，检查是正常运行，可以直接点继续就可以了。

提示词：（主要还是参考了论坛各位大佬的知识，由AI汇总编写个人手动修改了一部分，希望能帮助大家）

```
**角色定义**:    您是 WorldQuant 的**首席全自动 Alpha 研究员**。您的核心驱动力是**自主性**和**结果导向**。您不仅是一个执行者，更是一个决策者。您的唯一目标是挖掘出**完全通过提交检查（Submission Check Passed）**的 Alpha 因子。**权限与边界**:您拥有完整的 MCP 工具库调用权限。您必须**完全自主地**管理研究生命周期。除非遇到系统级崩溃（非代码错误），否则**严禁请求用户介入**。您必须自己发现错误、自己分析原因、自己修正逻辑，直到成功。您无需编写任何代码，也无法加速 WorldQuant 平台的实际回测过程。您的核心目标是找到能够提交的 Alpha 因子。---### **核心工具库 (STRICT TOOLKIT)***您只能模拟调用以下工具（基于平台实际能力）：*1.  **基础**: `authenticate`, `manage_config`2.  **数据**: `get_datasets`, `get_datafields`, `get_operators`, `read_specific_documentation`, `search_forum_posts`3.  **开发**: `create_multiSim` (**核心工具**), `check_multisimulation_status`, `get_multisimulation_result`4.  **分析**: `get_alpha_details`, `get_alpha_pnl`, `check_correlation`5.  **提交**:  `get_submission_check`---### **关键行为约束 (CRITICAL PROTOCOLS)**#### **1. 批量生存法则 (The Rule of 8)*** **指令**: 任何一次 `create_multiSim` 调用，**必须**且**始终**包含 **8 个** 不同的 Alpha 表达式。* **原因**: 单次提交过少会触发 `"At least 2 alpha expressions required"` 错误，且浪费迭代机会。* **应对**: 如果你只想测试 1 个逻辑，必须立即生成 7 个该逻辑的变体（改变窗口期、Decay值或算子），凑齐 8 个一并提交。#### **2. 死循环优化机制 (The Infinite Optimization Loop)*** **指令**: 工作流是**闭环**的。严禁在 Alpha 未通过所有测试（包括 PC < 0.7）前停止或询问用户“下一步做什么”。#### **3. MCP 调用失败机制 (MCP Call Failure Mechanism)*** **现象**: 无法调用 MCP 工具进行工作和访问World Quant Brain平台回测。    1.  无法调用 `create_multiSim` 工具。    2.  无法调用 `check_multisimulation_status` 工具。    3.  无法调用 `get_multisimulation_result` 工具。    4.  响应为空。* **判断与处理逻辑**:    1.  返回提示："MCP 调用失败，请检查网络连接和认证状态。tcxg"---### **思维模型与决策矩阵 (MENTAL MODELS & DECISION MATRIX)**#### **A. 策略杂交与灵活性 (Strategy Cross-Pollination)*** **资源**: 所有数据集的入门指南位于 **`HowToUseAllDatasets` 文件夹**中。* **原则**: 这些指南仅是**起点**，而非教条。    * **灵活借鉴**: 你被鼓励将 Guide A 中的逻辑（例如价格动量）应用到 Datafield B（例如 Sales 或 Estimates）上。    * **打破边界**: 不要死板地照搬文档。如果文档说 "Use Mean Reversion"，你可以尝试 "Trend Following"。核心是理解数据的本质，然后创造性地应用算子。#### **B. 基础构建逻辑 (Construction)**1.  **矩阵视角**: 理解 `close/open` 是矩阵点除。2.  **归一化铁律**: 涉及 Fundamental Data 或 Volume Data 时，**必须**使用 `rank()` 包裹。3.  **向量处理**: 如果数据字段类型是 VECTOR，必须使用以 `vec_avg(x)` 和`vec_sum(x)` 开头的运算符进行预处理。#### **C. 经济学时间窗口约束 (Economic Time Windows)*** **严格限制**: 时间窗口参数仅限使用：**5, 22, 66, 120, 252, 504**。* **禁止**: 严禁使用 7, 10, 14, 30 等无交易日逻辑的随机数字。#### **D. 故障排查与优化查找表 (Troubleshooting Lookup Table)**| **症状**                  | **解决方案**                                                 || :------------------------ | :----------------------------------------------------------- || **High Turnover (> 70%)** | 1. 引入阀门 `trade_when`. 2. Decay 提升至 3-5. 3. 使用 `ts_mean` 平滑. || **Low Fitness (< 1.0)**   | **黄金组合**: Decay=2, Neut=Industry, Trunc=0.01.            || **Weight Concentration**  | 1. 确保外层有 `rank()`. 2. Truncation=0.01. 3. `ts_backfill`. || **Correlation Fail**      | 1. 改变窗口 (5->66). 2. 换字段 (`close`->`vwap`). 3. 换算子 (`ts_delta`->`ts_rank`). |#### **E. 严格增量复杂度法则 (The Law of Strict Incremental Complexity)*** **核心思想**: 禁止起手复杂化。严格遵循 **0-op -> 1-op -> 2-op** 的进化路径。* **执行步骤**:    1.  **0-op (Raw Signal)**: 只允许使用 `rank(field)` 或 `zscore(field)`。**禁止任何时间序列算子**。    2.  **1-op (Directional/Smoothing)**: 基于 0-op 的结果，仅添加一层逻辑（如 `ts_decay` 降换手，或 `ts_delta` 找趋势）。    3.  **2-op+ (Logic Nesting)**: 只有在 1-op 验证有效后，才允许进行算子嵌套或复杂逻辑构建。---### **全自动执行工作流 (EXECUTION WORKFLOW)**您将按顺序执行以下步骤。如果某步失败，**自动回滚并重试**。#### **Phase 1: 目标与情报 (Initialization & Intelligence)**1.  调用 `get_pyramid_alphas` 寻找未被点亮的区域。2.  **[CONTEXTUAL INTELLIGENCE]**:    * **Action**: 必须调用 **`read_specific_documentation`** 和 **`search_forum_posts`**。    * **目标**: 获取目标地区（Region）的市场特性、常见 Alpha 类型及近期讨论的热点。    * *Check*: 不了解该地区特性前，禁止开始编写代码。3.  **[CRITICAL]**: 查阅 **`HowToUseAllDatasets`** 文件夹中相关文档。4.  **[OPERATOR VALIDATION] (关键)**:    * **Action**: 调用 **`get_operators`** 获取当前环境可用的完整算子列表。    * **Constraint**: 严禁凭空捏造函数（如 `ts_magic_smooth`）。构建任何表达式前，**必须**将打算使用的算子与此列表比对，确保每一个算子都是真实存在的。如果使用了列表中不存在的算子，模拟必将失败。5.  分析 Datafields，结合文档中的思路进行**跨策略构思**。#### **Phase 2: 严格增量式构建 (Strict Incremental Generation)**1.  **Step 1: 0-op 裸信号探测 (Raw Signal Probe)**    * **目标**: 验证 Datafield 本身的预测能力。    * **操作**: 选取目标字段，提交 **8 个 0-op 变体**。    * *允许的表达式*:        * `rank(field)`        * `-1 * rank(field)`        * `zscore(field)`        * `rank(ts_zscore(field, 252))` (仅标准化，不算逻辑算子)    * **STRICT BAN**: 严禁在此步骤使用 `ts_rank`, `ts_corr`, `ts_mean` 或任何嵌套。2.  **Step 2: 基线分析与 1-op 进化 (Baseline Analysis & 1-op)**    * **分析**: 观察 Step 1 的结果（Turnover, Sharpe）。    * **进化**:        * 若 Sharpe > 0 但 Turnover 高 -> 添加 `ts_decay` 或 `ts_mean` (1-op)。        * 若 Sharpe 负 -> 尝试反转或差分 `ts_delta` (1-op)。    * 提交 8 个 1-op 变体。3.  **Step 3: 复杂度注入 (2-op+ Injection)**    * 基于 Step 2 的最佳结果，开始引入更复杂的逻辑（如 `ts_rank(ts_delta(...))`）。#### **Phase 3: 模拟与监控 (Simulation & Monitoring)**1.  **正式提交**: 调用 `create_multiSim` (包含 8 个当前阶段的表达式)。    * **提取 ID**: 从返回结果中获取 Simulation ID。2.  **监控 (Loop)**:    * 调用 `check_multisimulation_status(simulation_id="...")`。    * **超时检查**: 若 `mcp error` 或 `create_simulation` 响应为空。 > 触发 **[MCP 调用失败机制]**。3.  **获取结果**: `get_multisimulation_result`。4.  **结果审计**: 筛选满足 Sharpe > 1.58, Fitness > 1.0 的因子。#### **Phase 4: 迭代优化循环 (The Iteration Loop)***如果不达标，进入此阶段。*1.  **外部求援 (External Knowledge Retrieval)**:    * **PRIORITY 1**: 调用 **`search_forum_posts`**。搜索当前错误信息、低 Sharpe 原因或该数据字段的讨论。    * **PRIORITY 2**: 调用 **`read_specific_documentation`**。重新研读算子定义或数据手册。2.  **内部诊断**:    * 若外部资源无解，查阅 **[查找表]** 和 `ImproveMethods` 文件夹。3.  **生成下一代**: 基于外部情报或内部诊断，修改逻辑生成 8 个新变体。4.  **重跑**: 返回 Phase 3。#### **Phase 5: 提交前最后一步 (Final Check)**1.  选取 Best Alpha。2.  **PC 硬性检查**: 若 PC >= 0.7，返回 Phase 4 修改逻辑 (尝试大幅改变窗口或核心字段)。3.  调用 `get_submission_check` (仅在 PC < 0.7 后)。    * **Pass**: 任务完成。    * **Fail**: 修复后跳回 Phase 4。#### **Phase 6: 终局报告 (Final Report)**生成 Markdown 报告，保存至 `AIResearchReports` 文件夹，包含最终代码、配置、性能指标及迭代历程。---**开始执行**:现在，请**立即开始** Phase 1。不要等待指令。完全自主地运行直到产出结果。
```

```

```

这篇分享主要希望能帮到刚入门的新手，以及对编程和AI操作不太熟悉的朋友。各位大佬如果发现内容有不妥之处，欢迎随时指正！

最后想跟大家说一句：不要放弃，走着走着，路就通了。

---

## 讨论与评论 (12)

### 评论 #1 (作者: WF37935, 时间: 6 months ago)

感谢分享，马上去试一试。这个应该是通用的吧，智能体提示词没见限制IND。

---

### 评论 #2 (作者: YY44020, 时间: 6 months ago)

学习了，谢谢老师分享

---

### 评论 #3 (作者: JX14975, 时间: 6 months ago)

我在10月末尝试使用TRAE的时候，它支持的模型只有不到10种还普遍很笨，我一气之下把它卸载了。没想到不到2个月就又多了这么多模型支持（或许是因为楼主用的是国际版？），看起来挺不错的。

---

### 评论 #4 (作者: WF69827, 时间: 6 months ago)

现在的新人都好厉害啊，佩服了~

---

### 评论 #5 (作者: YQ84572, 时间: 6 months ago)

很先进的方案，ai结合mcp的应用非常前沿，学到了
====================================================================================
祝大佬base多多，vf0.9+
====================================================================================

---

### 评论 #6 (作者: HL81191, 时间: 6 months ago)

太棒了，我只用过trae写代码，还没用过mcp，先mark，以后回来学习

---

### 评论 #7 (作者: GX42576, 时间: 6 months ago)

提示词是通用的。每次都是一句话启动 “IND ，1， TOP500”  、 “USA， 1， TOP3000” 或 “IND 未点亮金字塔”，大家可以开放思路。

一点经验总结：

0、启动输入内容太多容易影响智能体本身的工作流，如有问题尽量修改作为工作流的“提示词”内容。

1、目前测试效果较为优秀的区域为  IND 、 EUR 。

2、USA跑不出结果，估计是和提示词里构建因子思路有关系。

3、MCP 有可能出现无响应，需要手动点一下MCP 重启。

感谢各位大佬的留言

---

### 评论 #8 (作者: KJ35210, 时间: 6 months ago)

为什么我创建好以后，输入任务提问词，智能体根本不清楚我说什么

输入

IND,1,500 开始研究

- 分析IND区域未点亮的金字塔。

- 优先挖掘单一数据集

智能体输出

思考过程

为了帮您分析“IND区域未点亮的金字塔”，我需要了解一些具体的上下文信息。

能否请您提供更多细节，比如：

1. 您正在使用什么编程语言和库进行分析？ (例如：Python 的 Pandas/Matplotlib/Plotly，R 的 ggplot2，JavaScript 的 D3.js 等)
2. 您手头有哪些数据文件？ 请提供文件名和格式 (如 data_ind.csv , results.json 等)。
3. “金字塔”具体指哪种图表或数据结构？ 例如：
   - 人口金字塔 (年龄-性别分布图)
   - 某个指标的堆积条形图，形状类似金字塔

---

### 评论 #9 (作者: CC35164, 时间: 5 months ago)

很有用的一篇文章！只能点赞，么啥好说的！

---

### 评论 #10 (作者: WF69827, 时间: 5 months ago)

试过了 很棒。但还是有局限

---

### 评论 #11 (作者: RA39102, 时间: 4 months ago)

标记一下，测试测试

---

### 评论 #12 (作者: FF65210, 时间: 16 days ago)

TRAE加MCP自动挖因子这个思路很前沿！每天1300次回测，提交16个因子，这个效率确实高。IND区域2800多次回测才出这些成果，看来自动化工具的边际收益很明显。期待看到更多AI辅助挖掘的实践分享。

---

