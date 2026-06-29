# 【SDK+MCP+AGENT三层架构】因子挖掘系统，实现mcp稳定运行不断经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【SDKMCPAGENT三层架构】因子挖掘系统实现mcp稳定运行不断经验分享_37606116158743.md
- **作者**: GY62435
- **发布时间/热度**: 5个月前, 得票: 15

## 帖子正文

MCP运行一直存在一个困扰，就是执行过程中总存在中断，需要用户介入挖掘的情况。为解决这个问题，使用ai编程工具claude实现自动化因子挖掘系统，结合SDK、MCP和Agent三层架构，实现智能化、高性能的alpha挖掘。

## 系统架构

- ** **SDK Layer** **: 高性能直接API调用，处理80%的简单批量任务

- ** **MCP Layer** **: 复杂分析操作（提交检查、相关性分析）

- ** **Agent Layer** **: 智能决策和策略优化（使用Claude AI）

## 功能特性

- 每日目标：5000次回测，4个高质量alpha提交

- 支持多区域：USA, CHN, IND, EUR, JPN

- 支持多数据类别：ANALYST, NEWS, INSTITUTIONS, FUNDAMENTAL, MODEL

- 智能任务路由：根据复杂度自动分配到合适的层

- 学习系统：Agent层从结果中学习并优化策略

- 并行执行：高效的异步处理

## 安装

```bash

# 安装依赖

pip install -r requirements.txt

# 配置环境变量

cp .env.example .env

# 编辑.env文件，填入你的Anthropic API密钥

```

## 使用方法

### 交互模式（推荐首次使用）

```bash

python main.py

```

系统会提示你选择：

1. 区域（USA/CHN/IND/EUR/JPN）

2. 数据类别（ANALYST/NEWS/INSTITUTIONS/FUNDAMENTAL/MODEL/ALL）

3. 每日回测目标（默认5000）

4. 每日提交目标（默认4）

### 自动模式（无人值守）

```bash

python main.py --auto

```

使用默认配置自动运行：

- 区域：IND

- 数据类别：ALL

- 每日回测：5000

- 每日提交：4

## 配置说明

编辑 `config.py` 修改默认配置：

```python

@dataclass

class MiningConfig:

region: Region = Region.IND  # 默认区域

universe: str = "TOP500"  # 股票池

delay: int = 1  # 数据延迟

data_categories: List[DataCategory] = field(default_factory=lambda: [DataCategory.ALL])

daily_backtest_target: int = 5000  # 每日回测目标

daily_submission_target: int = 4  # 每日提交目标

min_sharpe: float = 1.5  # 最小Sharpe比率

min_fitness: float = 0.8  # 最小Fitness

```

## 系统要求

- Python 3.8+

- Anthropic API密钥

- WorldQuant BRAIN账户（MCP配置）

- uvx（用于运行MCP服务器）

## 详细工作流程

### 1. 系统初始化阶段

** **SDK层初始化** ** (sdk_layer.py:22-27)

- 创建aiohttp会话，配置连接池（最大20个并发连接）

- 设置超时时间（300秒）

- 初始化性能统计计数器

** **MCP层初始化** ** (mcp_layer.py:15-18)

- 创建HTTP会话用于BRAIN API调用

- 配置认证凭证（从环境变量或.brain_credentials读取）

** **Agent层初始化** ** (agent_layer.py:12-20)

- 初始化Anthropic客户端（使用ANTHROPIC_ *API_KEY）*

- 创建记忆系统：

- successful_patterns: 存储成功的alpha模式

- failed_patterns: 存储失败的alpha模式

- operator_scores: 记录每个操作符的平均得分

- datafield_scores: 记录每个数据字段的平均得分

### 2. 策略生成阶段

** **快速生成模式（80%批次）** ** (orchestrator.py:204-223)

- 从预定义操作符池中随机选择：ts_av_diff, ts_returns, ts_quantile, divide, subtract

- 根据配置的数据类别选择数据字段（默认：anl4_netprofit_median, anl4_ebit_median, anl4_afv4_median_eps）

- 随机选择时间窗口：40, 50, 60, 70, 80天

- 生成8个表达式，格式：rank(operator(field, window))

- 执行时间：<1秒

** **智能生成模式（20%批次）** ** (agent_layer.py:53-78)

- Agent构建策略提示，包含：

- 当前进度（已完成回测数、提交数）

- 历史表现（成功率、top操作符、top数据字段）

- 目标数据类别

- 调用Claude API生成策略（模型：claude-sonnet-4-5-20250929）

- Agent返回JSON格式策略：

```json

{

"expressions": ["rank(...)", ...],

"reasoning": "选择这些组合的原因",

"expected_success_rate": 0.15

}

```

- 执行时间：2-5秒

### 3. 回测执行阶段

** **Multisimulation创建** ** (sdk_layer.py:34-76)

- 构建API请求payload：

```python

{

"type": "MULTISIMULATION",

"expressions": [8个alpha表达式],

"settings": {

"region": "IND",

"universe": "TOP500",

"delay": 1,

"neutralization": "SUBINDUSTRY",

"truncation": 0.08,

...

}

}

```

- 发送POST请求到  [https://api.worldquantbrain.com/simulations](https://api.worldquantbrain.com/simulations)

- 等待BRAIN平台完成8个alpha的回测（通常8-15分钟）

- 返回结果包含每个alpha的详细指标

** **并行处理** **

- 系统支持同时运行多个multisimulation

- 通过asyncio.gather实现并发

- 速率限制：每批次间隔2秒，避免API过载

### 4. Alpha评估阶段

** **初步筛选** ** (orchestrator.py:163-190)

- 检查基本指标：

- Sharpe >= 1.5（可配置）

- Fitness >= 0.8（可配置）

- Turnover < 0.4

- 不符合条件的alpha直接丢弃

** **详细检查** ** (mcp_layer.py:29-47)

- 调用BRAIN API获取完整alpha详情

- 检查所有质量指标：

- LOW_SHARPE: 必须PASS

- LOW_FITNESS: 必须PASS

- LOW_TURNOVER: 必须PASS

- HIGH_TURNOVER: 必须PASS

- LOW_ROBUST_UNIVERSE_SHARPE: 必须PASS（关键指标）

- LOW_2Y_SHARPE: 建议PASS

** **相关性检查** ** (mcp_layer.py:33-35)

- 检查与生产环境alpha的相关性（阈值0.7）

- 检查与自己已提交alpha的相关性（阈值0.7）

- 高相关性的alpha会被拒绝

### 5. Alpha提交阶段

** **提交条件** **

- 所有质量检查必须PASS或WARNING

- 相关性检查必须通过

- SELF_CORRELATION, DATA_DIVERSITY, PROD_CORRELATION状态必须完成（非PENDING）

** **提交流程** ** (mcp_layer.py:41-47)

- 调用BRAIN API: POST /alphas/{alpha_id}/submit

- 成功后alpha状态从IS（In-Sample）变为OS（Out-of-Sample）

- 记录提交时间和提交计数

** **注意事项** **

- 某些检查需要时间完成，可能需要等待几分钟

- 如果检查状态为PENDING，提交会失败

- 建议在提交前等待所有检查完成

### 6. 学习优化阶段

** **结果分析** ** (agent_layer.py:103-141)

- 提取每个alpha的代码和性能指标

- 识别使用的操作符和数据字段

- 计算综合得分：score = sharpe × fitness

** **记忆更新** **

- 更新operator_ *scores：记录每个操作符的得分历史*

- 更新datafield_ *scores：记录每个数据字段的得分历史*

- 存储成功模式（sharpe >= min_sharpe && fitness >= min_fitness）

- 存储失败模式（用于避免重复错误）

** **策略优化** **

- Agent在下次生成策略时会参考：

- Top 5操作符（按平均得分排序）

- Top 5数据字段（按平均得分排序）

- 成功模式的共同特征

- 实现探索-利用平衡：

- 80%利用：使用历史最佳操作符和字段

- 20%探索：尝试新的组合

### 7. 进度监控

** **实时统计** ** (orchestrator.py:248-264)

- 总回测数

- 成功提交数 / 目标提交数

- 成功率（提交数/回测数）

- 运行时间

- 回测速度（回测数/小时）

- SDK层统计（调用次数、成功率、平均响应时间）

- Top操作符排名

** **停止条件** **

- 达到每日提交目标（默认4个）

- 达到每日回测目标（默认5000次）

- 用户手动中断（Ctrl+C）

### 8. 错误处理

** **API错误** **

- 401认证错误：自动重新认证

- 429速率限制：等待并重试

- 500服务器错误：记录并继续下一批次

** **Alpha错误** **

- 语法错误：记录错误信息，跳过该alpha

- 操作符不可用：从操作符池中移除

- 超时：增加超时时间并重试

** **系统错误** **

- 网络中断：自动重连

- 内存不足：减少并发数

- 磁盘满：清理临时文件

## 常见问题

### Alpha提交失败

** **问题** **：调用submit_ *alpha返回success但alpha状态仍为UNSUBMITTED*

** **原因** **：

1. 某些检查状态为PENDING（SELF_CORRELATION, DATA_DIVERSITY, PROD_CORRELATION）

2. BRAIN平台需要时间完成这些检查（通常5-15分钟）

3. 只有所有检查完成后才能提交

** **解决方案** **：

```python

# 1. 检查alpha状态

details = await mcp.get_alpha_details(alpha_id)

pending_checks = [c for c in details['is']['checks'] if c['result'] == 'PENDING']

# 2. 如果有PENDING检查，等待

if pending_checks:

print(f"等待检查完成: {[c['name'] for c in pending_checks]}")

await asyncio.sleep(300)  # 等待5分钟

# 3. 重新检查并提交

details = await mcp.get_alpha_details(alpha_id)

if all(c['result'] != 'PENDING' for c in details['is']['checks']):

await mcp.submit_alpha(alpha_id)

```

### 操作符不可用错误

** **问题** **：某些操作符返回"Attempted to use inaccessible or unknown operator"

** **原因** **：

- 不是所有操作符都在所有区域可用

- 某些高级操作符需要特殊权限

** **不可用操作符列表** **（IND区域）：

- ts_min, ts_max（使用min/max替代）

- 某些reduce *_* * *操作符（仅COMBO类型可用）*

** **解决方案** **：

- 使用get_ *operators()获取可用操作符列表*

- 从操作符池中移除不可用的操作符

- 使用替代操作符

### MCP层初始化失败

** **问题** **：FileNotFoundError: 'uvx'

** **原因** **：

- 原始设计使用uvx启动MCP服务器

- 当前环境中uvx不可用

** **解决方案** **：

- 已修复：MCP层现在使用直接API调用

- 不再依赖uvx

- 如需使用MCP工具，建议在Claude Code环境中直接调用

## 性能指标

- 回测速度：~625 multisimulations/天（每个8个alpha）

- 提交率：根据质量标准自动筛选

- 成功率：通过学习系统持续优化

## 注意事项

- 首次运行建议使用交互模式熟悉系统

- 确保MCP服务器正确配置BRAIN凭证

- 系统会自动进行速率限制，避免API过载

- Agent层需要Anthropic API密钥

---

## 讨论与评论 (12)

### 评论 #1 (作者: TT21691, 时间: 5个月前)

大佬的文章太有用了，终于可以解决AI经常停下来的问题了。

---

### 评论 #2 (作者: JX39934, 时间: 5个月前)

想问一下大佬，这一套AI工作流对token的消耗量如何，还有就是，每日对提交因子质量的把关是怎么样的，然后就是我想要的是点塔，有些塔不好点，交给AI他会不会为了完成任务，就随便找其他数据集的去交了呢

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 评论 #3 (作者: YX50005, 时间: 5个月前)

最近使用mcp进行alpha挖掘，确实经常有工作流中断，向我提问，或者还没有达到预设的目标就退出的问题，感觉大佬的这套架构针对这些问题非常有用，不过现在帖子的内容似乎有些笼统，main.py是如何控制工作流运行不断的的具体方法不知是否可以展示一下

---------------------If you come to the forum to study hard every day, you will get a GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------

---

### 评论 #4 (作者: KG24072, 时间: 5个月前)

看不懂，似乎是代码，又似乎是提示词，楼主可以给个进一步说明么？

---

### 评论 #5 (作者: XX84572, 时间: 5个月前)

你好呀，请问相关代码在哪里呢？可以分享吗？

---

### 评论 #6 (作者: GY62435, 时间: 5个月前)

又尝试了一段时间，感觉这种方式要比mcp直接运行会自动化以及快一些，但是如果真的要自动化可能还是直接使用API直连比较好，会更加自动化

但sdk+mcp+agent可能更有利于知识的进化和研究的进化，毕竟有知识的反馈机制

---

### 评论 #7 (作者: GY62435, 时间: 5个月前)

近期又优化了一个版本，增加知识的进化和反馈内容，大概如下图：

mcp回测


> [!NOTE] [图片 OCR 识别内容]
> Now
> let
> me
> run
> the
> Mew
> batch:
> cnhkmcp
> create_multisim
> (MCP ) (alpha_expressions
> [ "rank(ts_aV_diff(eps
> estimate_next_year ,
> 40) )"
> rank (ts_quantile (epsr_Iast_quarterly_update_
> Value
> 70) )"
> rank (ts_aV_diff (mdl26_preferred
> 80) )
> rank (ts_quantile (epsr_Iast_quarterly_
> update_value
> 50) )"
> rank (ts_
> aV_diff(adv20 ,
> 80) )"
> rank (ts_delta (mdl26_preferred
> 50) )"
> rank (ts_av_diff(mdl110_score
> 80) )
> rank (ts_returns (mdl38_
> smartestimate_fl2m_eps ,
> 40) )" ], delay:
> 1,
> neutralization:
> "SUBINDUSTRYI
> region:
> IND"
> universe
> ITOP5OB" )
> {
> result":
> ISUCCeSS
> true
> +1491
> Iines
> (Ctrl+o
> to expand)
> Excellent !
> The intelligent mining
> system is
> nOW
> running successfully !
> Round
> 1
> Results:
> AIphas
> Created:
> 1
> VRaomxad
> Sharpe
> 1.65
> Fitness
> 1.18
> (ANALYST pyramid)
> 2
> 58NR21az
> Sharpe:
> 1.55 ,
> Fitness:
> 1.21
> (ANALYST pyramid)
> 3
> leJXNYQ5
> Sharpe:
> 1.55,
> Fitness:
> 1.03
> (MODEL pyramid)
> PwQOpkV3
> Sharpe:
> 1.29
> Fitness:
> 0.95
> (ANALYST pyramid)
> 5
> j2NLMJSk
> Sharpe
> 8.31,
> Fitness:
> 0
> 11
> (PV
> pyramid )
> Failed
> 6
> qMebwpnk
> Sharpe:
> 1.03,
> Fitness:
> 0.51
> (MODEL pyramid)
> 7
> VRa0ob53
> Sharpe:
> 2.42_
> Fitness:
> 1.78
> (MODEL
> pyramid )
> Best performer!
> 8
> Ookezjnq
> Sharpe
> 1.67
> Fitness:
> 1.27
> (MODEL
> pyramid )
> Success
> Rate:
> 62.5%
> (5
> out
> 0F
> 8 With Sharpe
> 1.0 )
> The system
> is
> Working !
> NoW
> let
> me
> SaVe
> the
> results
> and
> Iun
> the
> analysis
> t0
> learn
> from
> this
> batch:


agent进行知识学习进化


> [!NOTE] [图片 OCR 识别内容]
> NOW
> let
> me
> analyze
> the
> results
> and
> let
> the
> Agent
> learn:
> Bash (cd ~/alpha_mining_system
> &&
> SOUICe
> Venv /bin/activate
> &&
> /analyze_results . py
> 1 )
> 匕
> 分析
> Round
> 的结果
> [DEBUG]
> Auth
> response
> keys:
> [ 'user
> token
> permissions
> 」
> +31
> lines
> (Ctrl+o
> t0
> expand )
> Perfect !
> The
> intelligent mining system
> is
> nOW
> fully operational
> Here
> What happened:
> System
> Status:
> Round
> Complete:
> Generated
> adaptive
> expressions
> Success
> rate:
> 62.5%
> (5
> high-quality
> alphas )
> Average
> Sharpe
> 1.43
> Agent
> learned
> from
> the
> results
> and  updated
> its  strategy
> Best
> Performers:
> 1
> mdl11e_SCore
> With ts_aV_diff
> Sharpe
> 2.42
> 2 
> md130_smartestimate_fl2m_eps
> With
> tS_
> returns
> Sharpe
> 1.67
> 3
> eps_estimate_next_year
> With ts_aV_diff
> Sharpe
> 1.65
> Failed
> Pattern:
> adV20
> With ts_aV_diff
> Sharpe
> 0.31
> (Will
> be
> aVoided
> in
> future )
> Next
> Steps
> The
> Agent
> has
> nOW
> learned
> from
> Round
> and
> Will:
> Increase
> weights
> for
> high-performing
> fields
> (mdl11e_score ,
> md130_
> smartestimate_fl2m_eps )
> Increase
> weights
> for
> SUCCesSful
> operators
> (ts_aV_diff,
> ts_returns )
> AVoid
> the
> failed pattern
> (adv20
> ts_aV_diff,
> 80 )
> YoU
> Can
> continue
> With
> Round
> by running
> Cd
> ~/alpha_mining_system
> &&
> SOUTCe
> Venv /bin/activate
> &&
> /generate_batch . Py
> The  system
> Will
> generate
> Smarter
> expressions
> based
> On
> What
> i
> learned !


sdk仅做最基础处理


> [!NOTE] [图片 OCR 识别内容]
> 2.1
> SDK Layer
> 数据层)
> 职责:  提供与
> BRAIN
> 平台的基础交互能力
> 核心功能:
> 用户认证和会话管理
> 数据字段获取和缓存
> AIpha
> 详情查询
> 基础
> API 封装
> 业务逻辑:
> class BrainsDk:
> def
> authenticate (email,
> password )
> #  1.
> 向
> BRAIN
> 平台发送认证请求
> # 2.
> 获取
> Session
> token
> # 3.
> 保存认证状态
> #  4。返回用户信息
> def get_datafields (region,
> universe, delay):
> #  1。检查缓存是否存在
> # 2.
> 如不存在,
> 调用
> API
> 获取字段列表
> #  3。过滤出
> MATRIX 类型字段
> #  4
> 缓存结果
> # 5.
> 返回字段列表
> def get_alpha_details (alpha_id):
> #  1。调用
> API
> 获取 Alpha
> 详细信息
> # 2.
> 解析性能指标 (sharpe,
> fitness ,
> returns )
> #  3。返回结构化数据
> 关键特性:
> 轻量级封装,
> 不包含业务逻辑
> 提供缓存机制减少
> API
> 调用
> 统错误处理


---

### 评论 #8 (作者: CQ55469, 时间: 5个月前)

这个系统看起来相当强大，尤其是在自动化因子挖掘和策略优化方面的设计。利用Claude AI与多层架构的结合，能够有效地提高因子挖掘的效率并减少人工干预。感谢大佬分享，💪💪💪💪💪。

---

### 评论 #9 (作者: CZ78575, 时间: 5个月前)

不贴代码，鉴定为水贴

---

### 评论 #10 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 5个月前)

这是一个超级强大且完整的工作流，几乎实现自动化挖掘因子了。我得立刻细品。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

### 评论 #11 (作者: HZ99685, 时间: 2个月前)

请问应该如何搭建，有没有详细的教程？

---

### 评论 #12 (作者: TT21691, 时间: 2个月前)

太强了，希望大佬分析一下详细过程。

---

