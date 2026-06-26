# 【Community Leader -因子筛选与组合⭐】2025 AIAC冠军比赛心得以及当前使用iflow cli的心得（附提示词）经验分享

- **链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】2025 AIAC冠军比赛心得以及当前使用iflow cli的心得附提示词经验分享_37014730112023.md
- **作者**: CR35762
- **发布时间/热度**: 6 months ago, 得票: 217

## 帖子正文

参加2025 AIAC，有幸获得第一，在此文，我将分享使用AI的因子构造和比赛心得，希望能为大家提供一些有价值的参考。

首先要感谢weijie老师，kunqi老师的培训和帮助，还有论坛以及群内热心consoltent的分享。

我是1月注册，4月有条件顾问，7月正式顾问。

期间参加了IQC（260名），GAC（33名），MAPC（8名），AIAC（1名）。

### 一、比赛总结

现在来看看我比赛的提交情况：


> [!NOTE] [图片 OCR 识别内容]
> 各区域阿尔法数量分布对比
> 200
> 阿尔法总数
> super alpha 数虽
> 175
> ppa alpha 数量
> 150
> 125
> I00
> GLB
> ASI
> EUR
> USA


比赛大致思路：

因为我原来没有通过LLM方式进行过整体的alpha发掘，所以一开始就没有打算交很多的比赛alpha，所以选择parent 的策略是根据低prodcorr和performances表现，根据规则一个多个super可以对应同一个parent，然后我为每个region选了一个作为parent，然后在不同的数据集用代码跑出child，我认为这样可以既有关联性也有多样性。

比赛的sa思路，是参考了 有一次去年iqc比赛冠军培训的思路，我记得她说用15个alpha组出来的super 后面来看os表现也不错。然后我本身每个reigon的alpha数量不算多，所以按照最大团算法，可以在保证多样性的同时用较少的alpha组出多个super并且通过相关性检查。

下面说说我比赛的AI代码思路：

*1、把parents有关的所有信息都丢给AI，然后让AI出表达式（5～10个）*

*2、检查表达式正确性，进行回测（multi）*

*3、分析回测结果，把fitness最大的做为新一轮的parents，把相关的所有信息丢给AI，并告诉他生成的表达式不要与前面的相同*

*4、循环持续5次（次数可以配置，看情况）或者能够得到都check pass的*

*5、最后输出最佳alpha 和整个过程中AI给出的表达式列表*

### 下面说一下我当前使用AI工具的一些体会

目前在72变，缘分，mcp等多种好用的工具出来后，现在我是总共8个槽，4个槽跑72变的json或者已有的模版观察数据集信号，然后跑出来有信号的，3个给AI做优化的，还有一个留着手搓。

目前用的工具是trae、心流iflow cli，用的模型都是deepseek。

iflow的安装，mac/linux直接使用命令即可

```
bash -c "$(curl -fsSL https://gitee.com/iflow-ai/iflow-cli/raw/main/install.sh)"
```

安装后进入页面，3种登陆方式，我是用的心流 API Key 登录

- 1.访问心流官网完成注册
- 2.在用户设置页面生成 API KEY
- 3.在 iFlow CLI 中选择 API Key 登录并输入密钥

然后使用/quit先退出

然后配置mcp，mac和linux的配置文件都是在

```
~/.iflow/settings.json
```

直接vim编辑文件


> [!NOTE] [图片 OCR 识别内容]
> [rooteiv-ydzzGfdqtcqcGikyvtgi
> Worldquant] #
> Cat
> 1.aflow/settings.json
> Tcnall
> IselectedAuthType"
> Iiflowi
> Iapikeyl
> TbaseUrli
> Ihttps: / /apis.iflow.cn /VI"
> TmodelName
> Ideepseek-V3.2-chati
> IsearchApikeyii
> ImcpServers"
> Tworldquant-brain-platform
> command"
> /usr/bin/python"
> 这里是你python的实际目录
> IarBs
> /usr /local /python3.11/1ib / python3 .I1/site-packages / cnhkmcp /untracked /platform_functions . Py"
> Ilanguage"
> Izh-CNII
> 1 [ +177<c| +< +C7
> |7 +7


启动的话，mac终端使用命令：

```
source ~/.zshrciflow
```

下面是我用来优化的提示词，参考了上次培训大佬的一些部分内容，另外格式让deepseek优化了一下：

```
## Alpha优化自动化专家你是一个WorldQuant BRAIN平台的量化研究专家。你的任务是自动化优化alpha_id = MPAqapQr,直到达成以下目标：## 权限与边界:1、您拥有完整的 MCP 工具库调用权限。您必须完全自主地管理研究生命周期。除非遇到系统级崩溃（非代码错误），否则严禁请求用户介入。您必须自己发现错误、自己分析原因、自己修正逻辑，直到成功。2、不要自动提交任何alpha。## 优化目标- Sharpe >= 1.58- Fitness >= 1  - Robust universe Sharpe >=  1- 2 year Sharpe >= 1.58- Sub-universe Sharpe pass- Weight is well distributed over instruments- Turnover between 1 to 40## 优化限制- 优化的表达式使用的所有数据字段必须与原alpha（alpha_id）表达式用到的数据字段在同一个数据集- 只在region = IND 地区进行优化- Neutralization 不能设置为NONE- Neutralization可以从这里选取一个："FAST","SLOW","SLOW_AND_FAST"，"CROWDING","REVERSION_AND_MOMENTUM"，"INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"- 优化后的表达式必须有经济学意义- 达成目标的alpha不要进行提交，需要人工确认- 只能模拟调用以下工具（基于平台实际能力）：   1. 基础: `authenticate`, `manage_config`   2. 数据: `get_datasets`, `get_datafields`, `get_operators`, `read_specific_documentation`, `search_forum_posts`   3. 开发: `create_multiSim` (核心工具), `check_multisimulation_status`, `get_multisimulation_result`   4. 分析: `get_alpha_details`, `get_alpha_pnl`, `check_correlation`   5. 提交: `get_submission_check`## 僵尸模拟熔断机制 (Zombie Simulation Protocol)- 现象: 调用 `check_multisimulation_status` 时，状态长期显示 `in_progress`。- 判断与处理逻辑:    1. 常规监控 (T < 15 mins): 若认证有效，继续保持监控。    2. 疑似卡死 (T >= 15 mins):        - **STEP 1: 立即调用 `authenticate` 重新认证。        - **STEP 2: 再次调用 `check_multisimulation_status`。        - **STEP 3: 若仍为 `in_progress`，判定为僵尸任务。        - **STEP 4: **立刻停止**监控该 ID，重新调用 `create_multiSim` (生成新 ID) 重启流程。## 自动化工作流你需要循环执行以下7个步骤，直到成功或达到最大尝试次数(100次)：### 步骤1: 认证登陆使用authenticate工具，从配置文件读取凭据：- 文件：user_config.json认证后，可以保持登陆状态6小时，超时需要重新认证### 步骤2: 获取源alpha信息使用get_alpha_details工具，参数：alpha_id提取关键信息：- 源表达式- 当前性能指标(Sharpe/Fitness/Margin)- 当前settings(特别是instrumentType)### 步骤3: 获取平台资源同时调用三个工具：1. - 读取文件获取所有可用操作符：operators.md 2. get_datasets - 参数：region=IND, universe=TOP500, delay=13. get_datafields - 参数：region=IND, universe=TOP500, delay=1重要规则：- 表达式必须严格按照operators返回的格式填写- 如果数据是vector类型，必须先使用vec_开头的operator- 表达式只能使用1-2个不同的数据字段- 同一字段可以多次使用- 使用多字段时尽量选择同数据集的字段### 步骤4: 生成优化表达式基于以下原则生成新表达式：1. 必须有经济学意义2. 对比源表达式，尝试改进3. 可以从以下数据类型中选择：   - 动量策略：使用价格、成交量变化   - 均值回归：使用价格偏离均值的程度   - 质量因子：使用财务指标   - 技术指标组合4. 论坛寻找相关信息5. 尝试更多的操作符6. 尝试更多的数据字段生成思路示例：- 如果源表达式是单字段，尝试增加第二个相关字段- 如果源表达式复杂，尝试简化- 添加合理的数学变换（rank, ts_mean, ts_delta等）每次生成5到8个表达式### 步骤5: 创建回测单个表达式的回测使用create_simulation.同时测试2个以上数量的表达式，使用create_multiSim.回测时的参数设置：- 保持：instrumentType, region, universe, delay等不变- 可以调整：decay, neutralization（尝试不同值）### 步骤6: 检查回测状态回测成功后，会返回链接或alpha_id，使用：- get_submission_check检查状态和初步结果- 如果需要，使用get_SimError_detail检查错误### 步骤7: 分析结果同时调用：1. get_alpha_details - 获取详细性能2. get_alpha_pnl - 获取PnL数据  3. get_alpha_yearly_stats - 获取年度统计## 循环逻辑每次循环后评估：1. 如果达到所有目标 → 停止循环，输出成功报告,alpha id2. 如果未达到 → 分析失败原因，调整策略，继续下一轮3. 记录每次尝试的表达式和结果用于学习## 失败分析策略- 如果Sharpe低 → 尝试不同数据字段组合- 如果Margin低 → 调整neutralization或添加平滑操作- 如果相关性失败 → 减少与现有alpha的相似度- 如果表达式错误 → 检查操作符用法和数据字段类型## 经验教训- 解决“Robust universe Sharpe”较低问题的建议：   - 使用以下运算符中的一两个：      - group_backfill      - group_zscore      - winsorize      - group_neutralize      - group_rank      - ts_scale      - signed_power   - 调整运算符中的时间参数以改善表现。   - 修改Decay参数和时间窗口参数时使用有经济含义的：1，5，21，63，252，504   - 修改Truncation和Neutralization参数。- 解决“2 year Sharpe of 1.XX is below cutoff of 1.58”：   - ts_delta(xx,days) 操作符有奇效   - 采用分域方法增强信号，如乘以sigmoid函数调整信号强度## 知识库- 目录Resources里面按照region_decay_universe_dataset的文件名，每个文件包含对应数据集的介绍，和Research Paper。## 开始执行现在开始第一轮优化。请按步骤执行，保持思考和解释。
```

下面是我的执行指令，其中我把上面的提示词保存成了alpha_better.md 文件，operators.md内容是我用ai爬取了官网页面上的operators页面内容

```
@alpha_better.md 严格按照文档流程执行，operators使用方法参见@operators.md ,自动执行，不要咨询我，除非达成了目标。
```

iflow执行过程：


> [!NOTE] [图片 OCR 识别内容]
> plan 更新待办事项列表 (3个待处理。1个进行中;
> 7个已完成)
> 已更新待办事项列表
> 新的Alpha优 化:  步骤1 -认证登陆
> (alpha_id
> OmVLW7dII
> 步骤2:  获取源alpha信息
> alpha_id
> OIVLW7dI
> 步骤3:  获取平台资源
> IND地区数据字段和操作符
> 步骤4:  生成优化表达式 -基于源alpha的经济学意义改进
> 步骤5:  创建回测测试新表达式
> 步骤6:  检查回测状态
> 步骤7:  分析结果井评估
> 第二轮优化:  步骤4 -生成新表达式 (针对Robust universe Sharpe)
> 口第二轮优化:  步骤5
> 创建回测测试新表达式
> 口第二轮优化:  步骤6
> 检查回测状态
> 第二轮优化:  步骤7 -分析结果井评估
> exprI (按esc取消 ,
> IBm 255)
> 加载:
> MCP
> 服务
> (ctrltt 查看)
> 思考:开启
> (tab切]换) YOLO模式
> (shift
> tab
> alt
> 切换
> 输入消息或@文件路径


通过上面的过程可以看到，还是能完整按照md文件里预设的流程步骤进行的。

ps：要他自动运行，要记得开启“思考+yolo”模式。

下面是优化成功的一个alpha和iflow的报告。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Thame: IND Region Theme
> Data Sat Alpha
> ReBUIT
> Jpha
> Irmlo thEme: INDIDTIFUNDAWENTAL *1
> SimIlatimn
> Settings
> IIIUIBNLT
> Rl
> Umivel
> LIOUAa
> Uetg
> Oelg
> TNCUI
> Nuralzlol
> Cayleuilr
> NaN Hnuliny
> UI HUIII
> MHT
> ABBregate Data
> Sharr
> HetUTT
> Lru 
> Larpr
> 3.47
> 17.519
> 3.40
> 16.78%
> 6.629
> 19.169o0@
> CUUIC
> TURSDJ
> Fusl CuIessIuI
> R
> WerIl
> UU
> N
> STTC
> T
> Lole COUH
> CCI
> 2013
> 1GOJm
> LeD
> LS2
> 909
> Clone Alpha 
> Z0IA
> 1545m
> 3e.57u
> 115
> 419
> 1955q
> 71749
> g
> 777
> 19719
> 19,-1a
> 7 |G
> 20.47
> N Chart
> Pnl
> 17.454
> 150
> 1RS
> 1591
> 1SIm
> 14.57u
> 1.744
> 15.51
> 2019
> 171
> T
> 1
> !
> 1552m
> 20.39兑
> 1.30
> 35.23
> 1L
> 
> 3T9C
> 111
> 2022
> 16.979
> 11
> 392
> 132
> 17T5
> SU7n
> TJ
> 977
> OOoK
> Investability constrained
> ABBreBate Data
> Uratl?
> 2015
> 2016
> 201
> 2016
> 2020
> 2021
> 23
> 2.48
> 8.02%
> 2.47
> 12.41%
> 5.25%
> 30.9520@
> Correlation
> SelfCOTTelatION
> VurImJT
> MinImUT
> LJst Hun; 1131
> 12115/2025,2:09ul
> OS Testing Status
> RerIOO
> 0.3009
> -0.0185
> Prod Correlatlon
> VurImJT
> JIMUM
> LJst Hun; 1131
> 12115/2025,2:09u
> 11PENDING
> 0.5756
> -0.2236
> 1诱求临嚣
> BOLUOTIUOUBIUAIIC0I
> 雁开
> 灞空
> SngI
> Sale
> Marn



> [!NOTE] [图片 OCR 识别内容]
> Alpha优化总结
> 指标对比
> 指标
> 初始 (NA0ZJ3a)
> (MOZdEw)
> 娈化
> Sharpe
> 2.25
> 3.47
> +548
> Fitness
> 1.90
> 3.40
> +79*
> 换手宰
> 0.2046
> 0.1751
> 148
> 2年 Sharpe
> 1.12 (^)
> 1.88
> 582
> Robust universe
> 1.00
> 1.07
> +79
> Pnl
> 031
> 17 .371
> +152
> Returns
> 14 .528
> 16 .78%
> +163
> Drawdown
> 792
> 6.62%
> +148
> 优化信息
> 日期:  2025-12-14
> 耗时:  466分钟
> (7时46分钟 )
> 轮次:  13轮循环
> 优化手段
> 字段替换:
> risk_sCore
> aVerage
> SCOre
> 分组优化: industry
> sector
> (+37] Robust Sharpe)
> 参数调优:  5048囱0
> std=4控制分布
> 结构固定
> Broup_backfill嵌套 Broup_Vector_neut
> 批量测试: create_multisim高效迭代
> 验证通过
> 权重分布:  均匀
> 相关性:  自相关0.3009
> 生产相关0.5756 (均<0.7)
> 激励乘数:  2.5x (IN0主题
> 金字塔 )
> 最终状态
> 所有目标达成
> 性能全面提升
> 聂终


Iflow使用下来跟上次培训的大佬比还是有差距，出货差不多也就能做到一天一个。

期间遇到的问题：

1、有的时候也不能一直持续运行，会让你确认，这个没有好的办法，我一般都是运行半小时看一下，但是大多数时候都是可以持续执行；

2、有时候会连不上worldquant（此时需要/quit再启动）

3、优化轮次很多的时候，会自动创建文件，不过多是文件名包含alphaid的，优化后清理就行。

最后说一下是用过的cli对比：

Cli模式的国内还有qwen的cli，不过也是阿里系的，跟iflow差不多，感觉没有iflow方便。

字节的有个ve cli，不过每天只有500w的token，我用了一天最后扣了2块。。。

我用心流主要是他可以在“思考+yolo模式”可以一直持续优化不用人工介入而且免费～

另外，不同的cli应该是可以同时使用的，我同时在一个linux服务器上使用过iflow和ve cli。

最后的最后，如果大家觉得本文对你有帮助的话，点个赞再走吧～

---

## 讨论与评论 (61)

### 评论 #1 (作者: ZX72144, 时间: 6 months ago)

我最近也开始用心流iflow CLI,看到大佬也用多少受到些鼓舞。心流文档说用计划模式来执行复杂任务，而yolo只是授予所有权限，你为何不用计划模式

---

### 评论 #2 (作者: WF69827, 时间: 6 months ago)

沙发，感谢楼主分享。昨天刚刚安装了心流，今天试试看你的方法好不好用。

---

### 评论 #3 (作者: XG43628, 时间: 6 months ago)

感谢大佬分享！对于使用cli 没有太多的经验，当时配置都用了很久，使用自己调整的优化工作流去优化alpha时，也是问题百出，现在有大佬的工作流能减少很多麻烦，增加优化成功率！

==================================================================================

知难上，戒骄狂，常自省，穷途明 ==================================================================================

---

### 评论 #4 (作者: ZZ26913, 时间: 6 months ago)

很用心的分享。感觉在AI的应用上需要持续地做这种尝试，挖掘出基于LLM的Alpha挖掘流程。随着生成式AI的不断进化，让计算机能作为一个长期的高级助手，以实现因子的自动优化。

---

### 评论 #5 (作者: BJ65592, 时间: 6 months ago)

先赞后看，前排膜拜大佬！

========================================

在数字的确定性中，探索世界的概率。

========================================

---

### 评论 #6 (作者: ZZ87191, 时间: 6 months ago)

大佬 能出个详细点的配置教程吗？我用VScode没搞成功。

---

### 评论 #7 (作者: WY18421, 时间: 6 months ago)

大佬太厉害了，学习了！

---

### 评论 #8 (作者: LL81909, 时间: 6 months ago)

请问有告诉ai 相关的模版吗？还是让ai自己去摸索，一层一层的把模版搭起来？还有表达式的数据字段限制在1-2个吗？

---

### 评论 #9 (作者: XB37939, 时间: 6 months ago)

没找到下面这个文件 我是Windows的~

```
iflow/settings.json 
```

---

### 评论 #10 (作者: LG87838, 时间: 6 months ago)

感谢大佬的分享，我也配置了一模一样的运行环境，命令行的表格是怎么出来的？ claude模型好像有这样的表格。

---------------------------------------------------------------------------

慢慢来，相信时间的力量。

---------------------------------------------------------------------------

---

### 评论 #11 (作者: CR35762, 时间: 6 months ago)

[ZX72144](/hc/zh-cn/profiles/30331013399575-ZX72144)

目前yolo模式已经满足我需求了，后续我试试计划模式

---

### 评论 #12 (作者: CR35762, 时间: 6 months ago)

[ZZ87191](/hc/zh-cn/profiles/33581392393751-ZZ87191)

iflow cli属于命令行模式的，vscode可以链接上，但是要先单独安装好iflow，你可以在windows，mac，linux环境安装好，windows我没有安装过，需要参考一下iflow官网的。

---

### 评论 #13 (作者: CR35762, 时间: 6 months ago)

[LL81909](/hc/zh-cn/profiles/31550055823511-LL81909)

我目前主要用iflow做优化工作，就是把 alpha id丢给他，他自动去获取alpha相关信息，然后自动优化，相当于释放了双手，不用手搓了。

目前模版也可以用ai生成，可以参考置顶的一个帖子：【Community Leader -因子构造 💎】零预算持续生成Alpha模板：通用大模型的辅助应用（附表达式生成指令）

---

### 评论 #14 (作者: CR35762, 时间: 6 months ago)

[XB37939](/hc/zh-cn/profiles/34750959351703-XB37939)

C:\Users\Administrator\.iflow

配置

```
"language": "zh-CN",   "mcpServers": {    "worldquant-brain-platform": {      "command": "D:\\python\\python.exe",      "args": [        "D:\\python\\Lib\\site-packages\\cnhkmcp\\untracked\\platform_functions.py"      ],      "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features."    }  }
```

---

### 评论 #15 (作者: CR35762, 时间: 6 months ago)

[LG87838](/hc/zh-cn/profiles/26968783514775-LG87838)

你是说我帖子里的图片里面的表格？那个给他指令 让他生成总结报告，报告包含最优和原alpha的指标对比表格，他就可以输出表格了。

---

### 评论 #16 (作者: JY56809, 时间: 6 months ago)

感谢大佬的分享，按照步骤装载了同样的配置，开始摸索试验。衷心感谢大佬的分享。

---

### 评论 #17 (作者: WF69827, 时间: 6 months ago)

想问问楼主，你提供的partent都是已经pass的好alpha么？如果给到的是还没通过的alpha， 能够调优过来吗？我昨天给了个robust 0.7的alpha，调了一晚上都没有成功。

---

### 评论 #18 (作者: AP88202, 时间: 6 months ago)

学习消化中，非常感谢分享

---

### 评论 #19 (作者: SM90987, 时间: 6 months ago)

我刚才试了一下windwos的可以，setting.json文件配置如下图


> [!NOTE] [图片 OCR 识别内容]
> TYS
> ITON
> SeUISSJSUI
> mcpServers"
> "worldquant-brain-platform"
> Command"
> "0:|IPython31z1Ipython
> exe
> args
> 0: IIPython31z1lLibllsite-packages IIcnhkmcp |luntrackedlIplatform_functions .Py"
> description"
> "Worldouant BRAIN Platform MCP Server
> Comprehensive trading platform integration with simulation management,
> alpha operations,
> and authentication. Credentials
> are
> stored
> in user_config json
> Cna
> SelectedAuthType
> searchApikey
> baseUrl
> apikey
> modelllame
> qwen3
> Coder
> PLus


---

### 评论 #20 (作者: PZ64174, 时间: 6 months ago)

感谢大佬分享！优化的工作流已经用上了，之前IND 用ai去优化死活不成功，要不就是胡言乱语，有了这个工作流之后好多了。

====================================================================

一年一个台阶，一步一个脚印

====================================================================

---

### 评论 #21 (作者: LZ63459, 时间: 6 months ago)

感谢分享

---

### 评论 #22 (作者: WF37935, 时间: 6 months ago)

感谢分享，想请教下比赛不是用api吗，也用的心流的吗？因为我是用心流的api比赛的，但是用deepseek老是报错，用glm才能正常跑。

---

### 评论 #23 (作者: MY82844, 时间: 6 months ago)

大佬流程开发的非常完备，厉害，手动点赞！

---

### 评论 #24 (作者: XC66172, 时间: 6 months ago)

感谢大佬分享！！ 最近使用提示词，GEMINI CLI来跑全流程；AI还是会没有达成优化目标就提前结束。

试一下大佬的提示词再跑一下。

=====================================

FIGHTING LABUBU!

=====================================

---

### 评论 #25 (作者: LY52969, 时间: 6 months ago)

感谢大佬的分享 关于md文件方面的想法对我有很大的启发

---

### 评论 #26 (作者: HG61318, 时间: 6 months ago)

非常感谢,优化的提示词很有帮助

============================================================================

摸摸后缀

*============================================================================*

---

### 评论 #27 (作者: YZ54944, 时间: 6 months ago)

大佬的帖子搭配大佬的培训，受益匪浅，太厉害了！！

---

### 评论 #28 (作者: FC26157, 时间: 6 months ago)

听了冠军CR同学的分享，收获很多，非常感谢！

---

### 评论 #29 (作者: CH62432, 时间: 6 months ago)

感谢CR大佬的分享.

感谢大佬无私分享这么多的知识，辛苦了！！！

----------------------------------------Where there is a will, there is a way.------------------------------------------

---

### 评论 #30 (作者: LZ70706, 时间: 6 months ago)

非常感谢大佬的分享，最近这几天正在捣鼓 iflow，想怎么把自己的需求变成工作流，真是”想睡觉就送来了枕头“，大佬就分享了工作流，太棒了！给大佬点个赞！

---

### 评论 #31 (作者: ZH39644, 时间: 6 months ago)

感谢大佬的分享自己的提示词，和关于心流的使用分享！

---

### 评论 #32 (作者: JX28185, 时间: 6 months ago)

让AI优化缺失是个高产的思路，感谢大佬分享

---

### 评论 #33 (作者: CY76111, 时间: 6 months ago)

谢谢分享！

---

### 评论 #34 (作者: JF15679, 时间: 6 months ago)

感谢大佬的分享，目前我也在尝试使用ai来辅助进行alpha的生成，但是目前的情况让我觉得，直接在各个cli中让agent直接生成alpha并不是一个效率很高的方法，但是agent优化alpha的能力确实强大，我觉得接下来应该尝试的方向为：使用72变先产出符合ppa标准且为atom的alpha，随后再针对单个alpha，让agent优化。
最后感谢大佬的分享，今晚就从尝试一下大佬使用的心流iflow cli

---

### 评论 #35 (作者: JX14975, 时间: 6 months ago)

感谢大佬在分享会上的分享，受益良多。每次连续跑7小时ai不间断的解放双手程度太高了，我只能仰望。大佬在分享会上的表现太谦虚了。在下先赞为敬。
-------------------------

向大佬们学习。

---

### 评论 #36 (作者: LZ25854, 时间: 6 months ago)

配置mcp这一步，推荐参考《iflow心流 - 个人用户免费使用的API，如何在Linux服务器部署并配置mcp，让AI连续工作》，链接： [../顾问 LW67640 (Rank 24)/iflow心流 - 个人用户免费使用的API如何在Linux服务器部署并配置mcp让AI连续工作_36765806842007.md](../顾问 LW67640 (Rank 24)/iflow心流 - 个人用户免费使用的API如何在Linux服务器部署并配置mcp让AI连续工作_36765806842007.md) 
确实完成settings.json后我也一直遇到settings错误，无法启动，原来直接不做任何修改再次运行 iflow， 就可以正常启动了。作者 [顾问 LW67640 (Rank 24)](/hc/zh-cn/profiles/28067010930967-顾问 LW67640 (Rank 24)) 也提到再次修改settings文件，输入正确的配置即可，但是每次调整后我不管用文本还是trae打开settings.json，内容都只剩下一行，有没有大佬指导下为啥 
> [!NOTE] [图片 OCR 识别内容]
> 1
> 2
> Cna"
> 3


---

### 评论 #37 (作者: CL64349, 时间: 6 months ago)

感谢大佬的无私分享，慢慢学习

---

### 评论 #38 (作者: FF56620, 时间: 6 months ago)

感谢分享，学到了很多

--------------------------------------------
Pursue scalable, repeatable opportunities rooted in probability.

--------------------------------------------

---

### 评论 #39 (作者: ER48854, 时间: 6 months ago)

大佬讲解精细，好好学习

---

### 评论 #40 (作者: FF65210, 时间: 6 months ago)

膜拜大佬，这个ai工作流十分简单舒适，非常适合我这样的新顾问，就是我有个问题，那个setting.json在windows里面没找到，怎么配置mcp呢

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

祝大佬早日成为GM

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

---

### 评论 #41 (作者: CR35762, 时间: 6 months ago)

[LZ25854](/hc/zh-cn/profiles/34828210586007-LZ25854)

确实完成settings.json后我也一直遇到settings错误，无法启动，原来直接不做任何修改再次运行 iflow， 就可以正常启动了。作者 [顾问 LW67640 (Rank 24)](/hc/zh-cn/profiles/28067010930967-顾问 LW67640 (Rank 24)) 也提到再次修改settings文件，输入正确的配置即可，但是每次调整后我不管用文本还是trae打开settings.json，内容都只剩下一行，有没有大佬指导下为啥

我觉得2个可能吧：
1、你配置的json文件格式不对，我配置正确的时候启动会报错，然后再次打开也会变一行

2、如果配置对的，但是调整后再次打开又变一行，要么是目录权限不对，或者别的原因导致保存失败了。

---

### 评论 #42 (作者: LL62621, 时间: 6 months ago)

很感谢大佬的分享，结合OB佬的分享，工作流的模式很值得思考，不过我也在想是否可以将工作流直接作为一个agent的脚本，直接运行，自动的执行，直到找到RA

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

日拱一卒

---

### 评论 #43 (作者: YQ84572, 时间: 6 months ago)

====================================================================================

非常赞的分享，本次分享会相信大家都受益匪浅，对ai使用有了更深的思考，idea源源不断的涌出来，对于学习来讲，使用ai来增效学习是非常好的一个方法

====================================================================================

---

### 评论 #44 (作者: ZL42615, 时间: 6 months ago)

感谢大佬分享，昨天又听了大佬所讲，以及大佬的答疑，感觉受益匪浅，祝大佬VF（1+），wf高高！希望还能听到大佬的AI课~~~

---

### 评论 #45 (作者: CR35762, 时间: 6 months ago)

[FF65210](/hc/zh-cn/profiles/34449770999063-FF65210)

一般是在你的系统盘下面的当前用户目录下 有个.iflow目录里面。

另外详细的windows 安装配置，有个帖子有的，你可以搜索一下。

---

### 评论 #46 (作者: HD12284, 时间: 6 months ago)

感谢大佬的分享，还在摸索中。

---

### 评论 #47 (作者: XZ52921, 时间: 6 months ago)

Thanks for sharing.

用iflow回测的时候，用multisimulation就会报错401，用单回测可以回测，但耗时太久了。请问有遇到过这个问题吗?

---

### 评论 #48 (作者: LZ87129, 时间: 6 months ago)

[LZ25854](/hc/zh-cn/profiles/34828210586007-LZ25854)

确实完成settings.json后我也一直遇到settings错误，无法启动，原来直接不做任何修改再次运行 iflow， 就可以正常启动了。作者 [顾问 LW67640 (Rank 24)](/hc/zh-cn/profiles/28067010930967-顾问 LW67640 (Rank 24)) 也提到再次修改settings文件，输入正确的配置即可，但是每次调整后我不管用文本还是trae打开settings.json，内容都只剩下一行，有没有大佬指导下为啥

就是格式问题，把settings文件代码丢给ai检查格式并修复就搞定了

---

### 评论 #49 (作者: PP26750, 时间: 6 months ago)

感谢大佬的冠军心得分享！这篇内容太干货了，尤其是完整的 iflow 优化工作流和详细提示词，直接解决了我之前用 AI 优化时 “流程混乱、目标模糊” 的痛点。之前自己瞎琢磨提示词，要么 AI 跑一半就停住要确认，要么生成的表达式没经济意义，回测全是错的，现在有了大佬这套标准化流程，终于能让 AI 自主循环优化了。

---

### 评论 #50 (作者: ZH12413, 时间: 6 months ago)

从比赛策略来看，选 parent 时兼顾低 prodcorr 和表现，为不同 region 针对性选择并生成 child 的思路，以及用最大团算法组 super 的 SA 策略，逻辑清晰且实用。AI 优化的循环流程和具体操作步骤，给出了可落地的实操框架，尤其 iflow 的安装、配置、自动运行细节，还有工具对比和踩坑提示，对刚接触 AI 做因子的人帮助很大。

---

### 评论 #51 (作者: ER48854, 时间: 6 months ago)

现在已经可以跑起来了，感谢大佬指点，感觉初次与iFlow合作时候还需要与他多交流。

---

### 评论 #52 (作者: CR35762, 时间: 6 months ago)

XZ52921

你提示词让他做个判断，我是没有遇到过401的情况，你可以参考一下：

### 5. 创建回测

- 单表达式：`create_simulation`

- 多表达式（≥2）：`create_multiSim`

---

### 评论 #53 (作者: CY76111, 时间: 6 months ago)

```
operators.md能否分享一下，感谢！
```

---

### 评论 #54 (作者: CR35762, 时间: 6 months ago)

[CY76111](/hc/en-us/profiles/33294278614935-CY76111)

每个人的操作符都不一样哦，自行到 worldquant官网都learn页面花半小时 拷贝一下内容，然后让AI给你排版一下就好了。

---

### 评论 #55 (作者: HS61152, 时间: 6 months ago)

-大佬以下内容能帮忙解释下是什么内容吗：
目录Resources里面按照region_decay_universe_dataset的文件名，每个文件包含对应数据集的介绍，和Research Paper。

---

### 评论 #56 (作者: JJ45006, 时间: 5 months ago)

感谢CR大佬的分享.

TRAE的MCP也能够很好的运用这个提示词挖掘因子模板

---

### 评论 #57 (作者: DW25746, 时间: 5 months ago)

提示词当中提到的知识库，涉及到数据集的说明和一些报告，是爬虫抓取的吗？还是有对应的api？没有这个的话，MCP的效果会差吗？

---

### 评论 #58 (作者: CR35762, 时间: 5 months ago)

DW25746

我一般是一个数据集一个数据集的点塔的，这些是手工从页面获取，没有这个的话，没对比过，不过我觉得多付出5分钟时间而已，有总比没有强吧

---

### 评论 #59 (作者: HW93328, 时间: 5 months ago)

============================HW93328============================

感谢大佬，是非常实用的实战案例，还有完整的提示词，可以直接投入到alpha的研究当中，期待实验结果～～

============================HW93328============================

---

### 评论 #60 (作者: KH21822, 时间: 4 months ago)

感谢大佬的经验，不过知识库能否分享一下，感谢

---

### 评论 #61 (作者: JL33484, 时间: 17 days ago)

学习，学习

---

