# 顾问 JG15244 (Rank 67) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 JG15244 (Rank 67) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: alpha 模拟高效篇)
- **原帖链接**: [Commented] alpha 模拟高效篇.md
- **时间**: 1 year ago

**提问/主帖背景 (SH90982)**:
大家好，

这是我成为顾问以来第一次发帖，我承认确实有懒的因素，但我个人认为既然分享那就得展现出绝活嘛。

好了，话不多说在我初识worldquant中国区的小伙伴们我就意识到我们的工作其实需要的是一整套完整的服务器运行代码体系。so ~ 我开始构建了一套高效的alpha回测运行体系。
        
> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> DOO
> 20OO
> @ @
> <eo
> ppp p
> CC
> ^370''2 ^" 0  2
> 3&^D今
>  ^"识
> 9 ^  96
> 9 ^O"
> Displayed Period
> 1212872024
> 06/23/2025
> 98956
> Yesterday
> 06/23/2025
> 5663
> Current period
> 05/01/2025
> 06/30/2025
> 55393
> Previous period
> 03/01/2025
> 04/30/2025
> 3146
> Yearto date
> 01/01/2025
> 06/23/2025
> 98956
> Total
> 12/28/2024
> 06/23/2025
> 98956
> Jan
> Feb
> Feb
> Mar
> Mar
> Nal
> Mar
> Mar
> May
> May
> May
> May
> Jun
> 23.jun


可以从回测条看出来，我确实比较咸鱼。收到邮件通知才开始启动alpha回测，现在我每天都能保证4个alpha的提交。究其原因，是我构建了一整套完整高效的回测体系大家可以参考也可以提意见我们一起进步


> [!NOTE] [图片 OCR 识别内容]
> 充当持久性任贪队列
> 入口点:  表达式敛据库
> alpha_running_expressions
> 外西迸程在此处生咸并插入 alpha 表达式。
> 初始化并启动所盲系统组迕。
> 列:。
> erDr Tegion
> UIIVEFse
> 在连读遁环中运行一组立为步 多
> 军排器
> T1n
> 0atab35e
> 荩理 DB 连接。
> TasrScheduler
> 任务的集中尤态笤理。
> 初始化的关筵组件:
> TaSkEYECUCOT
> 执行任务迓辑。
> BrainhDIClien-
> 外部仿兵引孥的接口。
> 鼬发器:  足鄢运行。
> 睑段:_趑据趣取
> 服务:
> 03t-
> PToOUCeT
> SeTCe
> 1 词用以获取一批新表达式。
> 41313135e
> TSTCT
> eXpFeSS1Ons
> T 「TN
> JDUI
> 2 至关茔1的足。这会从效m厍中刨呆获]行。
> 3.对于每个表达式。在
> BACNTEST TaskScheduler
> 触发器:  查询具有
> Taskscheduler szatus-PENIDING
> 猴务:
> hachtest
> TNNSIIP[
> SeTce
> 怍:  将任务函4
> 捉交到
> Client  submi-
> CTTMTTnn
> TasLCracVTIr
> 管理侍定于类型酌并发池 (例如。 一次最多3个回溯测过
> 雹2阶段:_回测趑行_
> 组仵:
> T3SICerITnT
> 获取信号虽井在
> RIIIIIIIG TastScheduter
> 调用 以启动外部葆拟。
> Brainpclient
> 服务范围:
> NOIICOT
> LODO
> 「unnlno
> T3S
> 1a5KxeCUtOT!
> 街引婺: 管道
> 子进裎:  长时回运行的任务监控
> 定翔轮询 以获取任务的状态。
> BrainApzCient RUINING
> 模拟完咸后。它会将任务更新到 $并存储
> TasLSchanVTer
> COIPLETED
> WorldQuant Alpha 生或工怍 翟
> 髭发器
> 否诲具有 . TaskScheduler BACNTEST status-CONPLETED
> 噩3豳段: Alpha 验证
> :务:
> check_alpha
> SeTice
> 1讨于每个完成为回:1试。向提交一个新任务。
> CHECRHLPH
> TaskEXECUCO「
> 2 存裆原始任务以防止垂新处瑾。
> BACKTEST
> 触发器:  查询具有
> Taskscheduler CHECK ALPH
> STatUs=COIPLETED
> 雳 4阶段:_ 进-步加工_
> 暇务:
> Chn02
> alpha_
> COLOI
> SerVice
> submit_alpha_service
> 作:_裉揖枪查结果执行后续作
> [引如:
> 对 Alpha 迸行分茭
> 讦分或正式提交)。
> Trigger:
> 监视己达到显终达态匈任务
> 噩5阶段:_数据持久性 _
> 暇务:
> I05eTT
> data_
> 作:  将最终的 alpha 敬据 (表达式。结果等)  与入持久表。如或。
> pass_expressions
> Tail
> EpFeSSIons
> 孚格尔颉:_屯枢神经系统。
> TaskScheduler
> (大脑
> 为直任多的坯态提箧单一幸实来e
> 使用导步队列和索引迸行非阻塞
> 亏效昀太态管理
> Snglaton
> 负贡所有任务的执行。
> ~庾用待定于类型的队列和信号豆迸行精细井发控制。
> 关M架杓组件
> TaskExecutor
> (肌肉)
> 与外部服务的接0
> RrainuDTCTTen
> 垂新中的任务状态。
> 13545CheUILer
> 昃步窘理所有教挹库交互。
> Database
> (网关
> 实观用于任务摄驭的类似队列的表
> 3LCha
> 「UIITIO
> eXDTeSSlons
> 捉供用于最终结果存储的表格
> 异步和事件驱动:  完全垂于. asyncio
> Decoupled Serices
> 答道的每个阶段都是
> 个单独的服务
> 它对状态娈化箧出反应。而不是直接诩用。
> 总体架杓原则
> 弹饪和可扩展饪
> 使用效据库作为持久队列和寺淅钩关注点分离使组件可以独立扩展或重新启动
> 以状态为中心:  踅个工作流程由由  笤理的任务扶态转换辽动。
> T35LSCheTer
> ulpha
> 31652
> 3105
     如上图所示，这是我的回测体系框架全程异步队列+任务调度运行现在基本一天下来我其实没有跑满的，也就放了8个并发目前最高6644个。在这里给大家提供的一整套体系化思维希望各位同志给出建设性建议让大家一起进步。

**顾问 JG15244 (Rank 67) 的解答与建议**:
佬现在是不是还是iqc顾问呀，只有三个槽。如果是有条件顾问的话，8*10个槽，回测量一版要在2.5w/天，才算可以的。可以看看论坛里的关于wqb的分享，是一个大佬开源的python包。

最后祝佬，vf1.0！

==========================================

原来，让内心强大，我只需要看到自己，接纳我还不能做的，欣赏我已经做到的。 ---维吉尼亚·萨提亚-

==========================================


---

### 技术对话片段 2 (原帖: alpha 模拟高效篇)
- **原帖链接**: https://support.worldquantbrain.com[Commented] alpha 模拟高效篇_33036460396567.md
- **时间**: 1年前

**提问/主帖背景 (SH90982)**:
大家好，

这是我成为顾问以来第一次发帖，我承认确实有懒的因素，但我个人认为既然分享那就得展现出绝活嘛。

好了，话不多说在我初识worldquant中国区的小伙伴们我就意识到我们的工作其实需要的是一整套完整的服务器运行代码体系。so ~ 我开始构建了一套高效的alpha回测运行体系。
        
> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> DOO
> 20OO
> @ @
> <eo
> ppp p
> CC
> ^370''2 ^" 0  2
> 3&^D今
>  ^"识
> 9 ^  96
> 9 ^O"
> Displayed Period
> 1212872024
> 06/23/2025
> 98956
> Yesterday
> 06/23/2025
> 5663
> Current period
> 05/01/2025
> 06/30/2025
> 55393
> Previous period
> 03/01/2025
> 04/30/2025
> 3146
> Yearto date
> 01/01/2025
> 06/23/2025
> 98956
> Total
> 12/28/2024
> 06/23/2025
> 98956
> Jan
> Feb
> Feb
> Mar
> Mar
> Nal
> Mar
> Mar
> May
> May
> May
> May
> Jun
> 23.jun


可以从回测条看出来，我确实比较咸鱼。收到邮件通知才开始启动alpha回测，现在我每天都能保证4个alpha的提交。究其原因，是我构建了一整套完整高效的回测体系大家可以参考也可以提意见我们一起进步


> [!NOTE] [图片 OCR 识别内容]
> 充当持久性任贪队列
> 入口点:  表达式敛据库
> alpha_running_expressions
> 外西迸程在此处生咸并插入 alpha 表达式。
> 初始化并启动所盲系统组迕。
> 列:。
> erDr Tegion
> UIIVEFse
> 在连读遁环中运行一组立为步 多
> 军排器
> T1n
> 0atab35e
> 荩理 DB 连接。
> TasrScheduler
> 任务的集中尤态笤理。
> 初始化的关筵组件:
> TaSkEYECUCOT
> 执行任务迓辑。
> BrainhDIClien-
> 外部仿兵引孥的接口。
> 鼬发器:  足鄢运行。
> 睑段:_趑据趣取
> 服务:
> 03t-
> PToOUCeT
> SeTCe
> 1 词用以获取一批新表达式。
> 41313135e
> TSTCT
> eXpFeSS1Ons
> T 「TN
> JDUI
> 2 至关茔1的足。这会从效m厍中刨呆获]行。
> 3.对于每个表达式。在
> BACNTEST TaskScheduler
> 触发器:  查询具有
> Taskscheduler szatus-PENIDING
> 猴务:
> hachtest
> TNNSIIP[
> SeTce
> 怍:  将任务函4
> 捉交到
> Client  submi-
> CTTMTTnn
> TasLCracVTIr
> 管理侍定于类型酌并发池 (例如。 一次最多3个回溯测过
> 雹2阶段:_回测趑行_
> 组仵:
> T3SICerITnT
> 获取信号虽井在
> RIIIIIIIG TastScheduter
> 调用 以启动外部葆拟。
> Brainpclient
> 服务范围:
> NOIICOT
> LODO
> 「unnlno
> T3S
> 1a5KxeCUtOT!
> 街引婺: 管道
> 子进裎:  长时回运行的任务监控
> 定翔轮询 以获取任务的状态。
> BrainApzCient RUINING
> 模拟完咸后。它会将任务更新到 $并存储
> TasLSchanVTer
> COIPLETED
> WorldQuant Alpha 生或工怍 翟
> 髭发器
> 否诲具有 . TaskScheduler BACNTEST status-CONPLETED
> 噩3豳段: Alpha 验证
> :务:
> check_alpha
> SeTice
> 1讨于每个完成为回:1试。向提交一个新任务。
> CHECRHLPH
> TaskEXECUCO「
> 2 存裆原始任务以防止垂新处瑾。
> BACKTEST
> 触发器:  查询具有
> Taskscheduler CHECK ALPH
> STatUs=COIPLETED
> 雳 4阶段:_ 进-步加工_
> 暇务:
> Chn02
> alpha_
> COLOI
> SerVice
> submit_alpha_service
> 作:_裉揖枪查结果执行后续作
> [引如:
> 对 Alpha 迸行分茭
> 讦分或正式提交)。
> Trigger:
> 监视己达到显终达态匈任务
> 噩5阶段:_数据持久性 _
> 暇务:
> I05eTT
> data_
> 作:  将最终的 alpha 敬据 (表达式。结果等)  与入持久表。如或。
> pass_expressions
> Tail
> EpFeSSIons
> 孚格尔颉:_屯枢神经系统。
> TaskScheduler
> (大脑
> 为直任多的坯态提箧单一幸实来e
> 使用导步队列和索引迸行非阻塞
> 亏效昀太态管理
> Snglaton
> 负贡所有任务的执行。
> ~庾用待定于类型的队列和信号豆迸行精细井发控制。
> 关M架杓组件
> TaskExecutor
> (肌肉)
> 与外部服务的接0
> RrainuDTCTTen
> 垂新中的任务状态。
> 13545CheUILer
> 昃步窘理所有教挹库交互。
> Database
> (网关
> 实观用于任务摄驭的类似队列的表
> 3LCha
> 「UIITIO
> eXDTeSSlons
> 捉供用于最终结果存储的表格
> 异步和事件驱动:  完全垂于. asyncio
> Decoupled Serices
> 答道的每个阶段都是
> 个单独的服务
> 它对状态娈化箧出反应。而不是直接诩用。
> 总体架杓原则
> 弹饪和可扩展饪
> 使用效据库作为持久队列和寺淅钩关注点分离使组件可以独立扩展或重新启动
> 以状态为中心:  踅个工作流程由由  笤理的任务扶态转换辽动。
> T35LSCheTer
> ulpha
> 31652
> 3105
     如上图所示，这是我的回测体系框架全程异步队列+任务调度运行现在基本一天下来我其实没有跑满的，也就放了8个并发目前最高6644个。在这里给大家提供的一整套体系化思维希望各位同志给出建设性建议让大家一起进步。

**顾问 JG15244 (Rank 67) 的解答与建议**:
佬现在是不是还是iqc顾问呀，只有三个槽。如果是有条件顾问的话，8*10个槽，回测量一版要在2.5w/天，才算可以的。可以看看论坛里的关于wqb的分享，是一个大佬开源的python包。

最后祝佬，vf1.0！

==========================================

原来，让内心强大，我只需要看到自己，接纳我还不能做的，欣赏我已经做到的。 ---维吉尼亚·萨提亚-

==========================================


---

### 技术对话片段 3 (原帖: Are some of the Alphas submitted as powerpool alphas noise?)
- **原帖链接**: [Commented] Are some of the Alphas submitted as powerpool alphas noise.md
- **时间**: 1年前

**提问/主帖背景 (CM45657)**:
Are some of the Alphas submitted as powerpool alphas noise?
I have faced some alphas with wierd graphs ,where there is no history, are these alphas hamful?

**顾问 JG15244 (Rank 67) 的解答与建议**:
Don't submit these alphas. Even though they perform excellently in terms of return, fitness, or margin, if the PNL (Profit and Loss) curve is not normal, you should not submit them. It will seriously damage your value factory.


---

### 技术对话片段 4 (原帖: Are some of the Alphas submitted as powerpool alphas noise?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Are some of the Alphas submitted as powerpool alphas noise_32098070589335.md
- **时间**: 1年前

**提问/主帖背景 (CM45657)**:
Are some of the Alphas submitted as powerpool alphas noise?
I have faced some alphas with wierd graphs ,where there is no history, are these alphas hamful?

**顾问 JG15244 (Rank 67) 的解答与建议**:
Don't submit these alphas. Even though they perform excellently in terms of return, fitness, or margin, if the PNL (Profit and Loss) curve is not normal, you should not submit them. It will seriously damage your value factory.


---

### 技术对话片段 5 (原帖: First Alpha in EUR region)
- **原帖链接**: [Commented] First Alpha in EUR region.md
- **时间**: 1年前

**提问/主帖背景 (SD99406)**:
Hey Consultants

Happy to share my first alpha submission in EUR region, Neutralization: Statistical, Universe: Top 2500


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 3,00OK
> 20OOK
> OOOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> 2.38
> 21.579
> 1.03
> 4.049
> 1.9996
> 3.749600
> Vear
> Sharpe
> Turover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.60
> 22.13%
> 1.73
> 5.0395
> 0.4795
> 4.5090c3
> 985
> 1123
> 2014
> 2.12
> 21.2496
> 0.85
> 3.4195
> 0.7195
> 3.2
> No
> 1198
> 1422
> 2015
> 2.75
> 21.1896
> 1.29
> 4.64N5
> 599b
> 4.389003
> 1241
> 1486
> 2016
> 3.52
> 21.4196
> 5.9195
> 0.5095
> 5.529003
> 1252
> 1473
> 2017
> 2.06
> 21.23%
> 1.99
> 5.0395
> 4795
> 4.8090c3
> 1358
> 1597
> 2018
> 2.05
> 21.82%
> 3.31%
> 0.6995
> 0290c3
> 1342
> 1591
> 2019
> 2.77
> 21.5496
> 1.22
> 4.2095
> 66NJ
> 883003
> 1295
> 1539
> 2020
> 0.45
> 21.93%
> 0.10
> 1.0395
> 1.3395
> 949oo
> 1276
> 492
> 2021
> 2.28
> 21.8096
> 2.49
> 7.359
> 6890
> 29003
> 1345
> 522
> 2022
> 0.30
> 21.54%6
> 0.05
> 0.6195
> 9995
> 0.5790c3
> 1323
> 1587
> 2023
> 3.37
> 19.35%
> -1.51
> 3.8995
> 0.2495
> 020003
> 1287
> 1482


Share your thoughts on this submission

**顾问 JG15244 (Rank 67) 的解答与建议**:
Congratulations, I also tried some on EUR-TOP2500, but many alphas got the "Sub-universe Sharpe of 0.5 is below cutoff of 0.74." error, I don't know how to optimize it, can you help me?


---

### 技术对话片段 6 (原帖: First Alpha in EUR region)
- **原帖链接**: https://support.worldquantbrain.com[Commented] First Alpha in EUR region_30098892113559.md
- **时间**: 1年前

**提问/主帖背景 (SD99406)**:
Hey Consultants

Happy to share my first alpha submission in EUR region, Neutralization: Statistical, Universe: Top 2500


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 3,00OK
> 20OOK
> OOOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> 2.38
> 21.579
> 1.03
> 4.049
> 1.9996
> 3.749600
> Vear
> Sharpe
> Turover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.60
> 22.13%
> 1.73
> 5.0395
> 0.4795
> 4.5090c3
> 985
> 1123
> 2014
> 2.12
> 21.2496
> 0.85
> 3.4195
> 0.7195
> 3.2
> No
> 1198
> 1422
> 2015
> 2.75
> 21.1896
> 1.29
> 4.64N5
> 599b
> 4.389003
> 1241
> 1486
> 2016
> 3.52
> 21.4196
> 5.9195
> 0.5095
> 5.529003
> 1252
> 1473
> 2017
> 2.06
> 21.23%
> 1.99
> 5.0395
> 4795
> 4.8090c3
> 1358
> 1597
> 2018
> 2.05
> 21.82%
> 3.31%
> 0.6995
> 0290c3
> 1342
> 1591
> 2019
> 2.77
> 21.5496
> 1.22
> 4.2095
> 66NJ
> 883003
> 1295
> 1539
> 2020
> 0.45
> 21.93%
> 0.10
> 1.0395
> 1.3395
> 949oo
> 1276
> 492
> 2021
> 2.28
> 21.8096
> 2.49
> 7.359
> 6890
> 29003
> 1345
> 522
> 2022
> 0.30
> 21.54%6
> 0.05
> 0.6195
> 9995
> 0.5790c3
> 1323
> 1587
> 2023
> 3.37
> 19.35%
> -1.51
> 3.8995
> 0.2495
> 020003
> 1287
> 1482


Share your thoughts on this submission

**顾问 JG15244 (Rank 67) 的解答与建议**:
Congratulations, I also tried some on EUR-TOP2500, but many alphas got the "Sub-universe Sharpe of 0.5 is below cutoff of 0.74." error, I don't know how to optimize it, can you help me?


---

### 技术对话片段 7 (原帖: 目录结构)
- **原帖链接**: [Commented] Gemini CLI 结合 MCP 工具的探索经验分享.md
- **时间**: 10 months ago

**提问/主帖背景 (KZ55390)**:
最近在积极地尝试使用 MCP ，基本没有错过论坛内的相关帖子，大家都在使用各种各样的工具。最近接触了 Gemini CLI ，论坛内正好也没有类似的内容，于是便进行了一番初步探索，分享给大家。

简单了解一下 Gemini CLI，是直接运行在终端地命令行工具， **免费调用 Gemini 2.5 Pro 模型，支持百万 Token 上下文，60 次/分钟，1000 次/每天的免费调用额度** ，个人用户应该是非常充足了。上下文的容量也比较大（正如 weijie 老师所说，上下文容量很重要，针对顾问们与 mcp 进行多轮对话来拷打出 alpha 是很适配的）。因此在我看来值得尝试一下。

先分享一下个人简单总结的初步使用感受，来供大家参考是否继续阅读并尝试使用：

**优点：** 免费；上下文容量很大（正常对话非常足够，且能压缩上下文）；速度还算较快；Memory 功能可以自定义规范；脱离 IDE 独立行走；能够输出有价值的alpha idea（尝试了一下难产的 insiders 数据集，还真整了一个ppa出来）；道歉还挺诚恳的（虽然没啥用）。

**缺点：** 命令行操作也许不够直观便捷；偶尔不够稳定；模型的表现有时也似乎不太稳定，会犯一些低级错误，如vector数据处理、数据字段名错误，有时候会有幻觉，也有我刚开始用没调教好的原因。

另外：在使用过程中可以保存或者让 AI 记住你的“指导”，利用编写工作流或者其他类似的方式，可以提高使用的效率。AI 还是需要好好调教的，需要一步步引导才能得到预期内和效果比较好的结果，感觉我的方法和技巧还是比较稚嫩，希望各位大佬能够多指导和分享 AI 的使用技巧！

如果对您有启发和帮助，请告诉我或者给我一个赞吧！

MCP 的安装和配置相信应该都没有什么难度了，就不多赘述。

## Gemini CLI 启动

> 参照 Github:  [[链接已屏蔽])  中的  `Quickstart`

**Pre：**

- Node.js ≥ 20 版本（Gemini CLI 是ts开发的）
- Google 账户（用于身份验证）

建议使用 npm 全局安装（npx用于临时使用）：

```
npm install -g @google/gemini-cli
gemini

```

安装完成之后就可以在任意地方输入  `gemini`  来启动 Gemini CLI 了。

### 用户认证

> 这里可能会有点小坑，可能会出现一些不同的认证失败的情况..
> 本文会在后面附上一些认证失败的解决办法，这里不影响继续阅读

作为个人用户就直接用 <  *Login with Google >* Google 账号来验证。点击回车之后会跳转到登录 Google 账号的页面。认证成功后就会进入 Gemini CLI。


> [!NOTE] [图片 OCR 识别内容]
> SE[UI
> Tips
> for getting started:
> 1
> Ask questions;
> edit
> files
> OI
> TUn
> Commands
> 2
> Be specific
> For
> the
> best results
> 3
> Create
> GEMINI .md files
> to
> CUstomize
> yOUI
> interactions With Gemini。
> 4
> /help for
> more
> information
> Using
> 工
> MCP
> SerVer
> Cctrltt
> to view)
> Type Your message
> 01
> @path/to/file


## MCP 配置

Gemini CLI 支持两种配置文件：项目级配置文件 和 全局配置文件。

全局配置文件一般位于用户主目录下  `C:\\Users\\xxx\\.gemini\\settings.json`  。

如果只想在某项目目录中配置，那么打开你想使用 Gemini CLI 的项目文件夹（一般在你的 WQ 的常用工作区目录下即可），创建  `.gemini`  目录，再在此目录下创建文件  `settings.json`  作为 mcp 配置文件。

```
# 创建 .gemini 目录
mkdir .gemini
# 在 VS Code 中打开设置文件
code .gemini/settings.json

# 目录结构
Your WQ Workspace/
├── .gemini/
│   └── settings.json
├── ....
├── ....

```

接着复制 WQ mcp 的 json 配置到 Gemini CLI mcp 配置文件  `settings.json`  中即可。

配置文件中 Gemini CLI 的行为按照以下优先级加载：

- 全局设置：~/.gemini/setting.json
- 项目设置：（项目根目录）/.gemini/setting.json

主要配置项：

- mcpServers：定义提供自定义工具的 MCP 服务器。

## Gemini CLI + MCP 使用

当 mcp 配置完成后，就可以使用  `/mcp`  或  `/mcp nodesc`  查看来查看已有的 mcp 及其工具。

`/mcp desc`  可以显示已有 mcp 及其工具的具体介绍。

### Compress 功能

Gemini CLI 提供了一个 compress 功能（ `/compress` ），可以对上下文进行压缩。

假设对话过程中超出了最大的上下文窗口，那么就会开始丢弃最开始的会话内容，那么 AI 模型就不能获取到全部的内容，会影响最终生成的结果。

那这个时候利用 Compress 功能对上下文进行压缩，AI 就能够获取到全部的上下文。并且压缩后上下文变短，那么 AI 要处理的数据也变少了，消耗的 Token 也会随之减少。

### 保存会话记录

如果需要退出当前会话并保存，方便下次再次进入会话，可以用命令： `/chat save <tag>`  。其中 tag 就是你给这个会话的标签，是下次再找到并进入会话的凭证。

查看已经保存的所有会话： `/chat list`  。

> 不会自动保存会话历史记录，需要保存的话记得 save。

### Shell 命令

使用  `！`  开头即可使用常规的 shell 命令。

退出 shell 命令就再次输入  `！`  。

### Memory 功能

`/memory show`  可以展示已添加到会话上下文中的记忆文件。（默认为  [GEMINI.md]([链接已屏蔽]) ，可以在 `~/.gemini/` 或项目目录中）

可以自己将需要它遵循的规则写入文件，让它记住并遵守，如环境、编程规范、代码风格等，甚至工作流程之类的也可以。

附1（Gemini CLI 认证）：

1. 如果认证成功那真是太好了。
2. 如果 **选择账号并登录之后一直卡在这个认证页面，那么可能是网络的问题** 。
   解决方法比较简单。回到命令行按  `ESC`  ，两次  `Ctrl+c`  退出 Gemini CLI。打开代理软件，复制终端代理命令，粘贴到命令行（为 **当前命令行** 配置代理）。或者打开 TUN 模式。
   然后重启 Gemini CLI，重新认证即可。
3. 如果 **选择账号并登录之后显示授权成功，但是回到命令行发现报错了** 。
   命令行会提示需要设置 GOOGLE_CLOUD_PROJECT 这个环境变量。
   这种情况需要先进入 Google Cloud 的控制台，在左上角图标旁选择一个项目（如果没有创建过项目那就新建一个项目。
   进入项目后搜索  `Gemini for Google Cloud`  ，点击启用服务。等启用成功后，回到项目页面，复制项目的ID，这就是我们需要的参数。
   接着就是设置一下环境变量参数，操作就不多赘述。重新进入Gemini CLI ，重新认证即可。
4. 如果除了上述的其他情况，那么可以分享到评论区大家一起来解决~

> 使用 export 方式配置环境变量或终端代理只对当前终端生效，如果需要全局生效就需要写入系统的配置文件中哦~

附2（它给的一个ppa，虽然性能比较普通）：


> [!NOTE] [图片 OCR 识别内容]
> 5,033K
> 250OK
> Jn"4
> Jn'15
> Jan'17
> Jn'13
> J3n'19
> J31'20
> Jn21
> J31'22
> J123


附3（来自AI诚挚的歉意）：


> [!NOTE] [图片 OCR 识别内容]
> 我为在这个过程中给您带来的巨大困扰。浪费您宝贵的时间和耐心
> 致以最深刻。最诚挚的歉意。
> 我已经证明了我目前无法胜任您托付的这项任务。
> 我不会再提出任何新的方案了。非常抱歉,我没能帮到您。
> Using:
> 1
> MCP
> SerVer
> (ctrltt
> to
> View)
> accepting
> edits
> (shift
> 十
> tab
> t0
> toggle)


看到这了别忘了点个赞再走 ：）

**顾问 JG15244 (Rank 67) 的解答与建议**:
设置环境变量的命令

$env:GOOGLE_CLOUD_PROJECT="你的项目ID"

============================================

不论斟满的是什么，都要——干杯！ ---吉皮乌斯诗-

============================================


---

### 技术对话片段 8 (原帖: 目录结构)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md
- **时间**: 10个月前

**提问/主帖背景 (KZ55390)**:
最近在积极地尝试使用 MCP ，基本没有错过论坛内的相关帖子，大家都在使用各种各样的工具。最近接触了 Gemini CLI ，论坛内正好也没有类似的内容，于是便进行了一番初步探索，分享给大家。

简单了解一下 Gemini CLI，是直接运行在终端地命令行工具， **免费调用 Gemini 2.5 Pro 模型，支持百万 Token 上下文，60 次/分钟，1000 次/每天的免费调用额度** ，个人用户应该是非常充足了。上下文的容量也比较大（正如 weijie 老师所说，上下文容量很重要，针对顾问们与 mcp 进行多轮对话来拷打出 alpha 是很适配的）。因此在我看来值得尝试一下。

先分享一下个人简单总结的初步使用感受，来供大家参考是否继续阅读并尝试使用：

**优点：** 免费；上下文容量很大（正常对话非常足够，且能压缩上下文）；速度还算较快；Memory 功能可以自定义规范；脱离 IDE 独立行走；能够输出有价值的alpha idea（尝试了一下难产的 insiders 数据集，还真整了一个ppa出来）；道歉还挺诚恳的（虽然没啥用）。

**缺点：** 命令行操作也许不够直观便捷；偶尔不够稳定；模型的表现有时也似乎不太稳定，会犯一些低级错误，如vector数据处理、数据字段名错误，有时候会有幻觉，也有我刚开始用没调教好的原因。

另外：在使用过程中可以保存或者让 AI 记住你的“指导”，利用编写工作流或者其他类似的方式，可以提高使用的效率。AI 还是需要好好调教的，需要一步步引导才能得到预期内和效果比较好的结果，感觉我的方法和技巧还是比较稚嫩，希望各位大佬能够多指导和分享 AI 的使用技巧！

如果对您有启发和帮助，请告诉我或者给我一个赞吧！

MCP 的安装和配置相信应该都没有什么难度了，就不多赘述。

## Gemini CLI 启动

> 参照 Github:  [[链接已屏蔽])  中的  `Quickstart`

**Pre：**

- Node.js ≥ 20 版本（Gemini CLI 是ts开发的）
- Google 账户（用于身份验证）

建议使用 npm 全局安装（npx用于临时使用）：

```
npm install -g @google/gemini-cli
gemini

```

安装完成之后就可以在任意地方输入  `gemini`  来启动 Gemini CLI 了。

### 用户认证

> 这里可能会有点小坑，可能会出现一些不同的认证失败的情况..
> 本文会在后面附上一些认证失败的解决办法，这里不影响继续阅读

作为个人用户就直接用 <  *Login with Google >* Google 账号来验证。点击回车之后会跳转到登录 Google 账号的页面。认证成功后就会进入 Gemini CLI。


> [!NOTE] [图片 OCR 识别内容]
> SE[UI
> Tips
> for getting started:
> 1
> Ask questions;
> edit
> files
> OI
> TUn
> Commands
> 2
> Be specific
> For
> the
> best results
> 3
> Create
> GEMINI .md files
> to
> CUstomize
> yOUI
> interactions With Gemini。
> 4
> /help for
> more
> information
> Using
> 工
> MCP
> SerVer
> Cctrltt
> to view)
> Type Your message
> 01
> @path/to/file


## MCP 配置

Gemini CLI 支持两种配置文件：项目级配置文件 和 全局配置文件。

全局配置文件一般位于用户主目录下  `C:\\Users\\xxx\\.gemini\\settings.json`  。

如果只想在某项目目录中配置，那么打开你想使用 Gemini CLI 的项目文件夹（一般在你的 WQ 的常用工作区目录下即可），创建  `.gemini`  目录，再在此目录下创建文件  `settings.json`  作为 mcp 配置文件。

```
# 创建 .gemini 目录
mkdir .gemini
# 在 VS Code 中打开设置文件
code .gemini/settings.json

# 目录结构
Your WQ Workspace/
├── .gemini/
│   └── settings.json
├── ....
├── ....

```

接着复制 WQ mcp 的 json 配置到 Gemini CLI mcp 配置文件  `settings.json`  中即可。

配置文件中 Gemini CLI 的行为按照以下优先级加载：

- 全局设置：~/.gemini/setting.json
- 项目设置：（项目根目录）/.gemini/setting.json

主要配置项：

- mcpServers：定义提供自定义工具的 MCP 服务器。

## Gemini CLI + MCP 使用

当 mcp 配置完成后，就可以使用  `/mcp`  或  `/mcp nodesc`  查看来查看已有的 mcp 及其工具。

`/mcp desc`  可以显示已有 mcp 及其工具的具体介绍。

### Compress 功能

Gemini CLI 提供了一个 compress 功能（ `/compress` ），可以对上下文进行压缩。

假设对话过程中超出了最大的上下文窗口，那么就会开始丢弃最开始的会话内容，那么 AI 模型就不能获取到全部的内容，会影响最终生成的结果。

那这个时候利用 Compress 功能对上下文进行压缩，AI 就能够获取到全部的上下文。并且压缩后上下文变短，那么 AI 要处理的数据也变少了，消耗的 Token 也会随之减少。

### 保存会话记录

如果需要退出当前会话并保存，方便下次再次进入会话，可以用命令： `/chat save <tag>`  。其中 tag 就是你给这个会话的标签，是下次再找到并进入会话的凭证。

查看已经保存的所有会话： `/chat list`  。

> 不会自动保存会话历史记录，需要保存的话记得 save。

### Shell 命令

使用  `！`  开头即可使用常规的 shell 命令。

退出 shell 命令就再次输入  `！`  。

### Memory 功能

`/memory show`  可以展示已添加到会话上下文中的记忆文件。（默认为  [GEMINI.md]([链接已屏蔽]) ，可以在 `~/.gemini/` 或项目目录中）

可以自己将需要它遵循的规则写入文件，让它记住并遵守，如环境、编程规范、代码风格等，甚至工作流程之类的也可以。

附1（Gemini CLI 认证）：

1. 如果认证成功那真是太好了。
2. 如果 **选择账号并登录之后一直卡在这个认证页面，那么可能是网络的问题** 。
   解决方法比较简单。回到命令行按  `ESC`  ，两次  `Ctrl+c`  退出 Gemini CLI。打开代理软件，复制终端代理命令，粘贴到命令行（为 **当前命令行** 配置代理）。或者打开 TUN 模式。
   然后重启 Gemini CLI，重新认证即可。
3. 如果 **选择账号并登录之后显示授权成功，但是回到命令行发现报错了** 。
   命令行会提示需要设置 GOOGLE_CLOUD_PROJECT 这个环境变量。
   这种情况需要先进入 Google Cloud 的控制台，在左上角图标旁选择一个项目（如果没有创建过项目那就新建一个项目。
   进入项目后搜索  `Gemini for Google Cloud`  ，点击启用服务。等启用成功后，回到项目页面，复制项目的ID，这就是我们需要的参数。
   接着就是设置一下环境变量参数，操作就不多赘述。重新进入Gemini CLI ，重新认证即可。
4. 如果除了上述的其他情况，那么可以分享到评论区大家一起来解决~

> 使用 export 方式配置环境变量或终端代理只对当前终端生效，如果需要全局生效就需要写入系统的配置文件中哦~

附2（它给的一个ppa，虽然性能比较普通）：


> [!NOTE] [图片 OCR 识别内容]
> 5,033K
> 250OK
> Jn"4
> Jn'15
> Jan'17
> Jn'13
> J3n'19
> J31'20
> Jn21
> J31'22
> J123


附3（来自AI诚挚的歉意）：


> [!NOTE] [图片 OCR 识别内容]
> 我为在这个过程中给您带来的巨大困扰。浪费您宝贵的时间和耐心
> 致以最深刻。最诚挚的歉意。
> 我已经证明了我目前无法胜任您托付的这项任务。
> 我不会再提出任何新的方案了。非常抱歉,我没能帮到您。
> Using:
> 1
> MCP
> SerVer
> (ctrltt
> to
> View)
> accepting
> edits
> (shift
> 十
> tab
> t0
> toggle)


看到这了别忘了点个赞再走 ：）

**顾问 JG15244 (Rank 67) 的解答与建议**:
设置环境变量的命令

$env:GOOGLE_CLOUD_PROJECT="你的项目ID"

============================================

不论斟满的是什么，都要——干杯！ ---吉皮乌斯诗-

============================================


---

### 技术对话片段 9 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享.md
- **时间**: 5个月前

**提问/主帖背景 (PP26750)**:
最近cnhkmcp更新了个好东西Skills，有了它我们就可以将自己摸索出来的或者大佬分享的 **"方法论"全部告诉ai，再配合Gemini 3 pro这个最强大脑真的是当之无愧的好东西**

**不过现在Gemini cli默认无法使用skills，需要进行一些配置**

**关于cnhkmcp的更新这里就不再讲解了，更新完成后会多一个skills文件夹，你需要在你的项目文件夹下新建.gemini文件夹然后将cnhkmcp中的skills文件夹复制到.gemini文件夹中。**

**第一步需要在终端运行更新，让你的Gemini cli到最新的预览版**

```
npm install -g @google/gemini-cli@preview
```

更新完成后再输入

```
gemini --version
```


> [!NOTE] [图片 OCR 识别内容]
> PS 0: |量化 IAIKnowledgeBase> gemini
> C-Version
> 0.24.0-preview . 2


如图所示如果显示0.24.0-preview.2就表示成功了，我们再用gemini进入

在对话框中输入/settings进入设置模式


> [!NOTE] [图片 OCR 识别内容]
> Settings
> Bearch
> to
> filter
> Preview Features Ce.9.
> models)
> truex
> Enable preview features
> preview models)
> Vim Mode
> false
> Enable
> Vim keybindings
> Disable Auto Update
> false
> Disable
> automatic updates
> Apply
> To
> User
> Settings
> Workspace Settings
> System Settings
> (Use
> Enter to select,
> Tab to change focus
> Esc
> to close)
> Ce.9.


第一个 Preview Features (e.g., models)推荐打开，也就是右边显示为true*

然后再在上方的搜索框中输入skills，按回车将Agent Skills设置为true*如图所示


> [!NOTE] [图片 OCR 识别内容]
> Settings
> skill
> Agent Skills
> tPuex
> Enable Agent
> Skills Cexperimental)
> Apply
> To
> User Settings
> Workspace Settings
> System Settings
> (Use
> Enter
> to
> select
> Tab
> to change focus
> Esc
> to
> Close)


这时候我们退出再重新进入，在对话框中输入/skills列出所有的技能，如图所示就表示成功了，有一点需要注意你启动Gemini的目录中需要有~/.gemini/skills/ 
> [!NOTE] [图片 OCR 识别内容]
> /skills
> Available Agent
> Skills
> brain-Calculate-alpha-selfcorrQuick
> Calculates
> self-correlation
> and
> PPAC (Power Pool Alpha
> correlations
> checks
> PPAC
> brain-datafield-exploration-general
> Provides
> 6 proVen
> methods
> to
> eValuate
> new datasets
> 00
> t
> Use
> When
> the
> USer Wants
> to
> understand
> specific datafie
> brain-dataset-exploration-general
> Provides
> comprehensive Workflow for deep-diving
> into
> research
> Use
> When
> the
> user Wants
> to
> audit
> dataset"
> brain-explain-alphas
> Provides
> step-by-step Workflow for analyzing
> and explz
> operators
> Work together
> Includes
> steps
> for data
> field
> brain-how-to-pass-AlphaTest
> Provides
> detailed requirements
> thresholds
> and improver
> When the
> User asks
> about alpha submission
> failures
> how


**顾问 JG15244 (Rank 67) 的解答与建议**:
TT大佬，学习了！


---

### 技术对话片段 10 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享_37661413598231.md
- **时间**: 5个月前

**提问/主帖背景 (PP26750)**:
最近cnhkmcp更新了个好东西Skills，有了它我们就可以将自己摸索出来的或者大佬分享的 **"方法论"全部告诉ai，再配合Gemini 3 pro这个最强大脑真的是当之无愧的好东西**

**不过现在Gemini cli默认无法使用skills，需要进行一些配置**

**关于cnhkmcp的更新这里就不再讲解了，更新完成后会多一个skills文件夹，你需要在你的项目文件夹下新建.gemini文件夹然后将cnhkmcp中的skills文件夹复制到.gemini文件夹中。**

**第一步需要在终端运行更新，让你的Gemini cli到最新的预览版**

```
npm install -g @google/gemini-cli@preview
```

更新完成后再输入

```
gemini --version
```


> [!NOTE] [图片 OCR 识别内容]
> PS 0: |量化 IAIKnowledgeBase> gemini
> C-Version
> 0.24.0-preview . 2


如图所示如果显示0.24.0-preview.2就表示成功了，我们再用gemini进入

在对话框中输入/settings进入设置模式


> [!NOTE] [图片 OCR 识别内容]
> Settings
> Bearch
> to
> filter
> Preview Features Ce.9.
> models)
> truex
> Enable preview features
> preview models)
> Vim Mode
> false
> Enable
> Vim keybindings
> Disable Auto Update
> false
> Disable
> automatic updates
> Apply
> To
> User
> Settings
> Workspace Settings
> System Settings
> (Use
> Enter to select,
> Tab to change focus
> Esc
> to close)
> Ce.9.


第一个 Preview Features (e.g., models)推荐打开，也就是右边显示为true*

然后再在上方的搜索框中输入skills，按回车将Agent Skills设置为true*如图所示


> [!NOTE] [图片 OCR 识别内容]
> Settings
> skill
> Agent Skills
> tPuex
> Enable Agent
> Skills Cexperimental)
> Apply
> To
> User Settings
> Workspace Settings
> System Settings
> (Use
> Enter
> to
> select
> Tab
> to change focus
> Esc
> to
> Close)


这时候我们退出再重新进入，在对话框中输入/skills列出所有的技能，如图所示就表示成功了，有一点需要注意你启动Gemini的目录中需要有~/.gemini/skills/ 
> [!NOTE] [图片 OCR 识别内容]
> /skills
> Available Agent
> Skills
> brain-Calculate-alpha-selfcorrQuick
> Calculates
> self-correlation
> and
> PPAC (Power Pool Alpha
> correlations
> checks
> PPAC
> brain-datafield-exploration-general
> Provides
> 6 proVen
> methods
> to
> eValuate
> new datasets
> 00
> t
> Use
> When
> the
> USer Wants
> to
> understand
> specific datafie
> brain-dataset-exploration-general
> Provides
> comprehensive Workflow for deep-diving
> into
> research
> Use
> When
> the
> user Wants
> to
> audit
> dataset"
> brain-explain-alphas
> Provides
> step-by-step Workflow for analyzing
> and explz
> operators
> Work together
> Includes
> steps
> for data
> field
> brain-how-to-pass-AlphaTest
> Provides
> detailed requirements
> thresholds
> and improver
> When the
> User asks
> about alpha submission
> failures
> how


**顾问 JG15244 (Rank 67) 的解答与建议**:
TT大佬，学习了！


---

### 技术对话片段 11 (原帖: General Discussion-说任何你想说的话置顶的)
- **原帖链接**: [Commented] General Discussion-说任何你想说的话置顶的.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
说 **任何** 你想说的话

 **Criteria** 
 **Action** 
 **Points** 
 **Weightage** 

论坛活动
当前季度内对您在本季度发布的评论（评论长度不少于100字符）的点赞数

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

对您的Gunies评级中的社区活跃项有20%的权重影响

当前季度内对您在本季度发布的帖子（帖子长度不少于100字符）的点赞数

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

👆中文翻译，👇以英文为主

Forum Activity
Likes in the current quarter on a comment published in current quarter (min. length 100 chars)

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

20%

Likes in the current quarter on a post published in current quarter (min. length 100 chars)

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

**顾问 JG15244 (Rank 67) 的解答与建议**:
太好了有这么一个单独的论坛，可以畅所欲言，不然大量重复低质量的帖子和评论充斥着之前的论坛，有些时候找篇帖子，找个评论可费劲了。感谢weijie老师为中国区的付出！

=======================================================================
没有幸福像这种幸福：寂静的清晨，来自河流的光，周末就在眼前。 ---詹姆斯·索特-
=======================================================================


---

### 技术对话片段 12 (原帖: General Discussion-说任何你想说的话置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] General Discussion-说任何你想说的话置顶的_32984741297815.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
说 **任何** 你想说的话

 **Criteria** 
 **Action** 
 **Points** 
 **Weightage** 

论坛活动
当前季度内对您在本季度发布的评论（评论长度不少于100字符）的点赞数

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

对您的Gunies评级中的社区活跃项有20%的权重影响

当前季度内对您在本季度发布的帖子（帖子长度不少于100字符）的点赞数

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

👆中文翻译，👇以英文为主

Forum Activity
Likes in the current quarter on a comment published in current quarter (min. length 100 chars)

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

20%

Likes in the current quarter on a post published in current quarter (min. length 100 chars)

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

**顾问 JG15244 (Rank 67) 的解答与建议**:
太好了有这么一个单独的论坛，可以畅所欲言，不然大量重复低质量的帖子和评论充斥着之前的论坛，有些时候找篇帖子，找个评论可费劲了。感谢weijie老师为中国区的付出！

=======================================================================
没有幸福像这种幸福：寂静的清晨，来自河流的光，周末就在眼前。 ---詹姆斯·索特-
=======================================================================


---

### 技术对话片段 13 (原帖: Getting started with India Alphas置顶的)
- **原帖链接**: [Commented] Getting started with India Alphas置顶的.md
- **时间**: 7个月前

**提问/主帖背景 (NL41370)**:
### Introduction

India universe on BRAIN consists of the top 500 stocks by liquidity.

Normal Alpha tests are applied, including Sharpe, fitness, sub-universe Sharpe, IS ladder etc.

Maxtrade is not mandatory in IND, and maximum turnover cap is 40%.

IND need to pass an additional  **robust universe Sharpe test** : IND Alpha should have minimum Sharpe of 1, in liquid stocks selected by BRAIN.

### Tips for Success

**IND stocks are not included in ASI universes** , also  **many data appear in both ASI and IND** , so we encourage  **retrying your ASI Alphas in IND** . Alphas that do well in both universes, may be strong candidates.

Try  **diverse data categories** , while it can lead to better combined performance.

Though maxtrade is optional, we still encourage  **keeping the investability constrained PnL to have a reasonable performance** .

Though max turnover is 40%, however we still encourage to  **lower the turnover**  if possible. Having  **high margin** , with turnover lower than 20% is a good practice.

**顾问 JG15244 (Rank 67) 的解答与建议**:
There are only 500 stocks in the IND, so why is the simulation speed slower than that of the AMR which includes 600 stocks?


---

### 技术对话片段 14 (原帖: Getting started with India Alphas置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Getting started with India Alphas置顶的_36059391387415.md
- **时间**: 7个月前

**提问/主帖背景 (NL41370)**:
### Introduction

India universe on BRAIN consists of the top 500 stocks by liquidity.

Normal Alpha tests are applied, including Sharpe, fitness, sub-universe Sharpe, IS ladder etc.

Maxtrade is not mandatory in IND, and maximum turnover cap is 40%.

IND need to pass an additional  **robust universe Sharpe test** : IND Alpha should have minimum Sharpe of 1, in liquid stocks selected by BRAIN.

### Tips for Success

**IND stocks are not included in ASI universes** , also  **many data appear in both ASI and IND** , so we encourage  **retrying your ASI Alphas in IND** . Alphas that do well in both universes, may be strong candidates.

Try  **diverse data categories** , while it can lead to better combined performance.

Though maxtrade is optional, we still encourage  **keeping the investability constrained PnL to have a reasonable performance** .

Though max turnover is 40%, however we still encourage to  **lower the turnover**  if possible. Having  **high margin** , with turnover lower than 20% is a good practice.

**顾问 JG15244 (Rank 67) 的解答与建议**:
There are only 500 stocks in the IND, so why is the simulation speed slower than that of the AMR which includes 600 stocks?


---

### 技术对话片段 15 (原帖: Key Insights for India alphas)
- **原帖链接**: [Commented] Key Insights for India alphas.md
- **时间**: 7个月前

**提问/主帖背景 (LR13671)**:
The  **India (IND)**  universe on BRAIN offers a unique blend of liquidity, sectoral diversity, and behavioral inefficiencies — making it an excellent testing ground for innovative alphas. Here’s a quick guide to help you approach IND research effectively.

### 1. Universe Overview

- **Constituents:**  Top 500 stocks by liquidity.
- **Turnover Cap:**  40% (but lower is generally better).
- **Additional Requirement:**  IND Alphas must achieve a  **minimum Sharpe ≥ 1**  on the  *liquid subset*  defined by BRAIN.
- **MaxTrade:**  Optional — though enabling it can improve practical investability.
- ### 2. Testing & Metrics
  All standard alpha tests apply:
  - **IS/OS Sharpe**  and  **Fitness**  for robustness
  - **Sub-universe Sharpe ladder**  for consistency across stock tiers
  - **Universe Sharpe**  to ensure strength across liquidity filters
  A strong IND alpha shows balanced  **Sharpe across IS and OS** , stable turnover, and low sensitivity to individual stock movements.

**顾问 JG15244 (Rank 67) 的解答与建议**:
Thanks for sharing.

What do you think of the overall survival (OS) performance of IND alpha?


---

### 技术对话片段 16 (原帖: Key Insights for India alphas)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Key Insights for India alphas_36172722618903.md
- **时间**: 7个月前

**提问/主帖背景 (LR13671)**:
The  **India (IND)**  universe on BRAIN offers a unique blend of liquidity, sectoral diversity, and behavioral inefficiencies — making it an excellent testing ground for innovative alphas. Here’s a quick guide to help you approach IND research effectively.

### 1. Universe Overview

- **Constituents:**  Top 500 stocks by liquidity.
- **Turnover Cap:**  40% (but lower is generally better).
- **Additional Requirement:**  IND Alphas must achieve a  **minimum Sharpe ≥ 1**  on the  *liquid subset*  defined by BRAIN.
- **MaxTrade:**  Optional — though enabling it can improve practical investability.
- ### 2. Testing & Metrics
  All standard alpha tests apply:
  - **IS/OS Sharpe**  and  **Fitness**  for robustness
  - **Sub-universe Sharpe ladder**  for consistency across stock tiers
  - **Universe Sharpe**  to ensure strength across liquidity filters
  A strong IND alpha shows balanced  **Sharpe across IS and OS** , stable turnover, and low sensitivity to individual stock movements.

**顾问 JG15244 (Rank 67) 的解答与建议**:
Thanks for sharing.

What do you think of the overall survival (OS) performance of IND alpha?


---

### 技术对话片段 17 (原帖: MCP结合论文实践经验分享)
- **原帖链接**: [Commented] MCP结合论文实践经验分享.md
- **时间**: 7个月前

**提问/主帖背景 (YZ13693)**:
官方推荐的论文

Research Paper: Overvalued Equity and Financing Decisions

[[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md]([L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md)

根据MCP工具里面的APP, 提取论文的方程 和表达式
 
> [!NOTE] [图片 OCR 识别内容]
> DI
> (44T
> 4CBQ
> 4TXDB)/ATt-I
> Debt issuance measure
> change in assets minus change in book equity
> deferred taxes scaled by lagged assets
> Variables:
> English
> 中文
> ATt-I
> Total assets at previous period (COMPUSTAT item AT, dollars)
> DI
> Debt issuance (dimensionless ratio)
> 4AT
> Change in total assets (COMPUSTAT item AT, dollars)
> 4CBQ
> Change in book equity (COMPUSTAT item CEQ dollars)
> 4TYDB
> Change in deferred taxes (COMPUSTAT item TXDB, dollars)
> Context: Measurement of net debt issuance following Baker and Wurgler (2002)
> methodology
> 中文描述:债务发行衡量指标
> 总资产娈动减去账面权益和递延税款娈动,再除以前期总资产。用于衡量公司净债务融资活动
> and
 
 
> [!NOTE] [图片 OCR 识别内容]
> 9 =
> (MVE + AT
> (C卫Q + TXDB))|AT
> Tobins 9
> market Value of equity plus assets minus book Value of equity; all divided by assets
> Variables:
> English
> 甲文
> AT
> Total assets (COMPUSTAT item AT, dollars)
> 0卫0
> Book value of equity (COMPUSTAT item CEQ dollars)
> MV卫
> Market value of equity (dollars)
> TJDB
> Deferred taxes (COMPUSTAT item TXDB, dollars)
> Tobin's q (dimensionless ratio)
> Context: Control variable for growth opportunities and investment prospects in regression tests
> 中文描述:托宾0值
> 权益市场价值加总资产减去权益账面价值。再除以总资产
> 用于衡量公司投资机会和市场估值
 导出分析结果
根据论文提供的 数据字段 mdl23_bk_net_equity_financ 利用ai  对起进行分析，

分析结果如下：

## 原始表达式（已回测）

**Alpha ID**: `rK3edZVd`

**表达式**:

```

group_neutralize(ts_rank(ts_mean(mdl23_bk_net_equity_financ, 20), 60) + ts_rank(ts_mean(pv87_stock_tvrwgthold, 20), 60), densify(sector))

```

**回测结果**:

- IS Sharpe: 0.61 (FAIL - 低于1.58阈值)

- IS Fitness: 0.22 (FAIL - 低于1.0阈值)

- Turnover: 0.0651 (PASS)

- Sub-universe Sharpe: 0.19 (FAIL)

**逻辑**: 高股权融资 + 高换手率 = 更强的市场时机信号

**顾问 JG15244 (Rank 67) 的解答与建议**:
看最后的pnl图线，是一个非常好的alpha！

有几个疑问，我看文中提到的示例alpha表达式中，还存在pv类型的字段，这个字段是怎么来的呢？

贴主，是否分享一下提问的具体呀。


---

### 技术对话片段 18 (原帖: MCP结合论文实践经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] MCP结合论文实践经验分享_36221002981271.md
- **时间**: 7 months ago

**提问/主帖背景 (YZ13693)**:
官方推荐的论文

Research Paper: Overvalued Equity and Financing Decisions

[[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md]([L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md)

根据MCP工具里面的APP, 提取论文的方程 和表达式
 
> [!NOTE] [图片 OCR 识别内容]
> DI
> (44T
> 4CBQ
> 4TXDB)/ATt-I
> Debt issuance measure
> change in assets minus change in book equity
> deferred taxes scaled by lagged assets
> Variables:
> English
> 中文
> ATt-I
> Total assets at previous period (COMPUSTAT item AT, dollars)
> DI
> Debt issuance (dimensionless ratio)
> 4AT
> Change in total assets (COMPUSTAT item AT, dollars)
> 4CBQ
> Change in book equity (COMPUSTAT item CEQ dollars)
> 4TYDB
> Change in deferred taxes (COMPUSTAT item TXDB, dollars)
> Context: Measurement of net debt issuance following Baker and Wurgler (2002)
> methodology
> 中文描述:债务发行衡量指标
> 总资产娈动减去账面权益和递延税款娈动,再除以前期总资产。用于衡量公司净债务融资活动
> and
 
 
> [!NOTE] [图片 OCR 识别内容]
> 9 =
> (MVE + AT
> (C卫Q + TXDB))|AT
> Tobins 9
> market Value of equity plus assets minus book Value of equity; all divided by assets
> Variables:
> English
> 甲文
> AT
> Total assets (COMPUSTAT item AT, dollars)
> 0卫0
> Book value of equity (COMPUSTAT item CEQ dollars)
> MV卫
> Market value of equity (dollars)
> TJDB
> Deferred taxes (COMPUSTAT item TXDB, dollars)
> Tobin's q (dimensionless ratio)
> Context: Control variable for growth opportunities and investment prospects in regression tests
> 中文描述:托宾0值
> 权益市场价值加总资产减去权益账面价值。再除以总资产
> 用于衡量公司投资机会和市场估值
 导出分析结果
根据论文提供的 数据字段 mdl23_bk_net_equity_financ 利用ai  对起进行分析，

分析结果如下：

## 原始表达式（已回测）

**Alpha ID**: `rK3edZVd`

**表达式**:

```

group_neutralize(ts_rank(ts_mean(mdl23_bk_net_equity_financ, 20), 60) + ts_rank(ts_mean(pv87_stock_tvrwgthold, 20), 60), densify(sector))

```

**回测结果**:

- IS Sharpe: 0.61 (FAIL - 低于1.58阈值)

- IS Fitness: 0.22 (FAIL - 低于1.0阈值)

- Turnover: 0.0651 (PASS)

- Sub-universe Sharpe: 0.19 (FAIL)

**逻辑**: 高股权融资 + 高换手率 = 更强的市场时机信号

**顾问 JG15244 (Rank 67) 的解答与建议**:
看最后的pnl图线，是一个非常好的alpha！

有几个疑问，我看文中提到的示例alpha表达式中，还存在pv类型的字段，这个字段是怎么来的呢？

贴主，是否分享一下提问的具体呀。


---

### 技术对话片段 19 (原帖: Navigating Trade-offs in Alpha Development)
- **原帖链接**: [Commented] Navigating Trade-offs in Alpha Development.md
- **时间**: 1年前

**提问/主帖背景 (FO38556)**:
What frameworks or thought processes can someone use to balance alpha performance (like Sharpe or IC) with platform constraints such as turnover, capacity, and self-correlation?

**顾问 JG15244 (Rank 67) 的解答与建议**:
Among multiple indicators, I think fitness is the most important. It is a comprehensive reflection of multiple indicators. Next is margin. A high margin represents higher returns. However, margin depends on turnover, return, and drawdown. Different regions should have different numerical thresholds for margin, and you need to decide this on your own. In short, a single indicator cannot directly determine the quality of this alpha. Multiple indicators are needed for evaluation.


---

### 技术对话片段 20 (原帖: Navigating Trade-offs in Alpha Development)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Navigating Trade-offs in Alpha Development_32120930759063.md
- **时间**: 1年前

**提问/主帖背景 (FO38556)**:
What frameworks or thought processes can someone use to balance alpha performance (like Sharpe or IC) with platform constraints such as turnover, capacity, and self-correlation?

**顾问 JG15244 (Rank 67) 的解答与建议**:
Among multiple indicators, I think fitness is the most important. It is a comprehensive reflection of multiple indicators. Next is margin. A high margin represents higher returns. However, margin depends on turnover, return, and drawdown. Different regions should have different numerical thresholds for margin, and you need to decide this on your own. In short, a single indicator cannot directly determine the quality of this alpha. Multiple indicators are needed for evaluation.


---

### 技术对话片段 21 (原帖: One Alpha submitted in different region)
- **原帖链接**: [Commented] One Alpha submitted in different region.md
- **时间**: 1年前

**提问/主帖背景 (SD99406)**:
Hii,

I want to ask that, I have one alpha submitted in say  "USA" and then same alpha is submitted in say "GLB" is this a good practice and what effect it will make to my alpha pool in terms of performances

**顾问 JG15244 (Rank 67) 的解答与建议**:
I think this is a very good operation. If your alpha performs well in the "USA" region and also shows good performance in the "GLB" region, it indicates that this alpha is extremely stable and has a more pronounced investment effect. However, it is necessary to be cautious about preventing overfitting and maintaining a low level of correlation.


---

### 技术对话片段 22 (原帖: One Alpha submitted in different region)
- **原帖链接**: https://support.worldquantbrain.com[Commented] One Alpha submitted in different region_32144831395991.md
- **时间**: 1年前

**提问/主帖背景 (SD99406)**:
Hii,

I want to ask that, I have one alpha submitted in say  "USA" and then same alpha is submitted in say "GLB" is this a good practice and what effect it will make to my alpha pool in terms of performances

**顾问 JG15244 (Rank 67) 的解答与建议**:
I think this is a very good operation. If your alpha performs well in the "USA" region and also shows good performance in the "GLB" region, it indicates that this alpha is extremely stable and has a more pronounced investment effect. However, it is necessary to be cautious about preventing overfitting and maintaining a low level of correlation.


---

### 技术对话片段 23 (原帖: Suggestion: Option to Refine or Unsubmit an Alpha Before Its  Compensated/Paid)
- **原帖链接**: [Commented] Suggestion Option to Refine or Unsubmit an Alpha Before Its  CompensatedPaid.md
- **时间**: 7个月前

**提问/主帖背景 (ME83843)**:
Dear Brain Team,

I really appreciate the learning and innovation opportunities that the WorldQuant Brain platform provides. I wanted to share a small suggestion that could make the experience even better for consultants.

Sometimes, an alpha might be submitted accidentally or before it’s fully refined. It would be great if there were an option to  **“unsubmit” or edit an alpha before it’s compensated** , especially when a contributor realizes there’s room for improvement.

This feature could help participants like me refine our ideas into more meaningful and higher-quality submissions, rather than leaving less effective ones in the system. I believe it would also enhance the overall quality of alphas on the platform.

Thank you for continuously improving Brain and for giving us the chance to grow and contribute to such an inspiring community.

**顾问 JG15244 (Rank 67) 的解答与建议**:
Good idea. I often make incorrect submissions due to code errors or accidental slips of the hand.


---

### 技术对话片段 24 (原帖: Suggestion: Option to Refine or Unsubmit an Alpha Before Its  Compensated/Paid)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Suggestion Option to Refine or Unsubmit an Alpha Before Its  CompensatedPaid_36117965917463.md
- **时间**: 7个月前

**提问/主帖背景 (ME83843)**:
Dear Brain Team,

I really appreciate the learning and innovation opportunities that the WorldQuant Brain platform provides. I wanted to share a small suggestion that could make the experience even better for consultants.

Sometimes, an alpha might be submitted accidentally or before it’s fully refined. It would be great if there were an option to  **“unsubmit” or edit an alpha before it’s compensated** , especially when a contributor realizes there’s room for improvement.

This feature could help participants like me refine our ideas into more meaningful and higher-quality submissions, rather than leaving less effective ones in the system. I believe it would also enhance the overall quality of alphas on the platform.

Thank you for continuously improving Brain and for giving us the chance to grow and contribute to such an inspiring community.

**顾问 JG15244 (Rank 67) 的解答与建议**:
Good idea. I often make incorrect submissions due to code errors or accidental slips of the hand.


---

### 技术对话片段 25 (原帖: 依次添加到总列表中)
- **原帖链接**: [Commented] 【Alpha灵感】复现2023年因子日历论坛精选.md
- **时间**: 1年前

**提问/主帖背景 (LR93609)**:
**一、概况：**

**1. 2023年因子日历，日历部分共379页，删除、去重、合并并整理后约359个因子...**


> [!NOTE] [图片 OCR 识别内容]
> 2029
> 詈


**2. 我从3月初开始复现，预计7月初整理完成，历时近4个月...**

**
> [!NOTE] [图片 OCR 识别内容]
> 财务因子 (79个)
> 规模因子 (6个)
> 投资因子 (19个)
> 成长因子 (20个)
> 估值因子 (17个)
> 波动率因子 (25个)
> 杠杆因子 (10个)
> 流动性因子 (19个)
> 动量因子 (25个)
> 13
> 质量因子
> (4个)
> 11
> 技术因子 (39个)
> 12
> 无形资产 (9个)
> 13
> 股东因子 (6个)
> 14.
> 公司治理 (2个)
> 另类因子 (21个)
> 15
> 分析师因子 (20个)
> 高频因子 (38个)
> 成交量占比:  0x开盘黛合竟众成交量-(1-0) 收盏集合竞价成交量
> -致卖出/买入交易:
> 股权集中度:  前三大流通股东持股数/流通股股本
> 价量相关性趋势因子:
> 成交量比值:  每曰上午
> 下午开盘前30分钟成交量的比值
> TRt
> U
> Lolmowin
> 卫t
> 工i)
> 时间加权平均的股票相对价格位置:
> RP卫 .t
> {olfemon
**

**3. 对多信号因子创建Alpha-tree回测，约105个trees，1677+行函数表达式，仍在整理中...**

**
> [!NOTE] [图片 OCR 识别内容]
> 2023
> 1473
> def
> f1121_Amount ( ):
> Apr
> 1474
> n_values
> list (range(125,
> 1801,
> 125) )
> 1475
> expressions
> []
> Dec
> 1476
> 1477
> for
> in n_values
> Jan
> 1478
> product_expr
> "log(close
> Volume
> July
> 1479
> mean_expr
> f"ts
> mean ( {product_
> expr},
> {n})
> Mar
> 1488
> std_expr
> f"ts
> std_dev({product_expr},
> {n})
> 1481
> final_expr
> f"{mean_expr}
> {std_expr}
> NeV
> 1482
> expressions .append (mean_expr _
> 61101_List_
> 1483
> expressions .append (final_expr
> 1484
> eXP-
> u
> O
> C;^1
> 01114_Operating_Curr _
> (variable) expressions
> Iist
> 1485
> 01118_Cash_Income
> 1486
> return expressions
> Q1121_Amount
> 1487
> 01122_Movement
> 1488
> def
> f1122_Movement ():
> 01129_News
> 1489
> n_Values
> Iist (range (19
> 252,10) )
> Oct
> 1498
> 初始化三个空列表
> Sec
> 1491
> expr
> []
> 1492
> for
> in n_values
> 1493
> rank(returns )
> 4888
> 4881
> 2024
> 1494
> a_eXpr
> f"rank(returns )
> 4888
> 4801
> factors_lib_2023.py
> 1495
> # b
> sqrt (48e1
> 3999
> 12)
> factors lib
> 2024py
> 1496
> b_expr
> +
> {a_expr}
> sqrt ( 4881
> 3999
> 12)
> factors_lib
> 1497
> ts_mean(b,
> h)
> factors_lib_Vo.py
> 1498
> C_expr
> f"ts_mean ({bexpr},
> {n})
> 1499
> ts_std_dev(b,
> 几)
> filters_
> 1588
> d_expr
> std_dev ({bexpr},
> {n})
> functionpy
> 1581
> machine_
> 1502
> eXpr
> f"{bexpr}
> {d_expr}
> Aug
> May
> Days
> '
> Sep
> TS.Py
> lib py
> "ts _
> Jib py
**

**4. 结论：**

**1）除部分user操作符和字段受限的因子外，其他多数因子是有信号的，稍作调试便可能得到不错的效果。**

**2）多数高频因子可以降维使用，主要是借鉴其构建逻辑；**  **分析师或另类因子，可以选择datafield替代，借鉴其idea。**

**3）技术类因子，可以选择操作符替代，比如用ts_mean替代SMA，用ts_decay_linear近似替代EMA（效果一般），特殊情形中用ts_sum部分实现递归运算等...**

**二、举例（仅选择其中表现相对优异的几个予以示意）：**

**1. 1月19日 流动性因子—— Amihub 非流动性因子**

**（由于IQC无法获取当日成交额数据，此处用close*volume近似）**


> [!NOTE] [图片 OCR 识别内容]
> 星期四
> 96
> 1月
> Jan.
> 躺局忪
> Amihud 非流动性因子
> 勐牺厅
> IRial
> ILLIQit
> VOLDid
> 其中
> R;d为 t月内殷票
> 的巳宦收益率;
> VOLDiu 为 [月内股祟
> 的E度咸交额;
> 通常要汆月内正常交易的交易日夫数不少亍15天。
> 说明
> 预期市场流动性不足会对V前股票超额妆益产生积极影响 ,
> 带来非流动性滏价;
> 取值越高
> 流动性及险趱大。诋担及险带来的末来收益趱高 _
> !^考交s
> TTHU?
> rakg。 7002
> NNIII
> T
> LrCts-SCCUICT
> Serles etfz-ts。
> CIe
> Fnoncial Marlets
> Jug


**# 公式**

Amihud = ts_mean(abs(returns)/volume/close,n)

**# 表达式函数**

def f0119_Amihud():

expressions = []

windows = range(20, 500, 20)

for window in windows:

expr = f"-ts_mean((abs(returns) / (volume * close)), {window})"

expressions.append(expr)

return expressions

**# 调试结果（升阶并调试效果：中性化并增加进出场条件）**


> [!NOTE] [图片 OCR 识别内容]
> 10N
> OOOK
> OOOK
> OOOK
> OOOK
> Nay '18
> Sep '18
> Jan 19
> 5ep'19
> Sep '20
> Jan '21
> Nay '21
> SCP "21
> Jan "22
> May'22
> Jan '23
> Iay
> May
> SCN



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 0C
> Spectacular
> Asingle Data Set Alpha
> Aggregate Data
> Sharpe
> TIICn N?
> TTSc
> RPITT
> Drawow
> Margin
> 2.30
> 14.9396
> 3.00
> 25.3996
> 9.18%
> 34.029600
> Year
> Sharpe
> TUrnOVeT
> Ftness
> Retums
> Drawdoyn
> Marqin
> Count
> Short Count
> 2018
> 0.31
> 11.319
> 0.11
> 2.05呖
> 5.93%
> 3.529
> 1915
> 1129
> 2019
> 2.18
> 15.55%
> 2.4
> 98%
> 50035
> 25.715
> 1933
> 1103
> 2020
> 2.24
> 16.3395
> 3.07
> 30.839
> 089
> 37.58Cco
> 97
> 1085
> 2021
> 2.92
> 16.41%
> 4.37
> 36.72%
> 9.1835
> 44.74
> 2005
> 1080
> 2022
> 15,139
> 425
> 33,539
> 5.1035
> 4.34o
> 2035
> 1052
> 2023
> 7.51
> 10.639
> 9.42
> 83.50%
> 743
> 157.3r
> 2070
> 1037
> Correlation
> Self Correlation
> MaximuI
> Winimum
> Las Run:
> Check Submission
> Submit Alpha
> Long


**2. 6月10日VS 11月21日 流动性因子——成交额 VS 成交额波动系数**

**（由于IQC无法获取当日成交额数据，此处用close*volume近似）**


> [!NOTE] [图片 OCR 识别内容]
> 星期五
> @@
> 10月
> Oct
> 》尻乩性
> 成交额
> 最近K个月日度成交额的均值
> 即:
> mean (最近'个月日度戍交额序列)
> 说明
> 衡蟹股票交易流动性的虿斐捐硫
> 如冥股票流动性较差
> ,格扫对较低
> 投资者对
> 其预期收益就会较高
> 存在流动性溢价
> (袄号文颍 !
> Rrrra I
> TTUT Uel
> AATCHa [
> SUbIaRNaTS, 1999
> Je;it;
> T
> 50aritI3
> 10/5
> SOUTI
> 'IIITCTTS5
> 5T
> PNeCeO
> SUC
> PIUIN
> e:Ja|
> FIIATCIU'
> EONOITS 49,345.173,



> [!NOTE] [图片 OCR 识别内容]
> 星期二
> 十月初九
> 29
> 11月
> NoV
> 流动性
> 成交额波动系数
> '^国
> mean (最近{个月日度咸交鞭庐列)
> std (最近氐个月日度成交额序列)
> 说明
> 在衡量咸交颧高低水乎的同时还考虑了成交额的波动惜况,是u量交易流动性的
> 综合性指标。
> 5薄文咸 
> TCVCI
> LCI Ku
> Zhnd。 1020. teplcaiing
> 71+
> I
> FnanCia
> Slucles 32[51


**# 公式**

ts_mean( log(volume*close),500)

拓展：1/ ts_std_dev( log(volume*close), 500)

**# 表达式函数**

def f1121_Amount():

n_values = list(range(125, 1001, 125))

expressions = []

for n in n_values:

product_expr = "log(close * volume)"

mean_expr = f"ts_mean({product_expr}, {n})"

std_expr = f"ts_std_dev({product_expr}, {n})"

final_expr = f"{mean_expr} / {std_expr}"

expressions.append(mean_expr)

expressions.append(final_expr)

expressions.append(final_expr)

return expressions

**# 原始数据回测（有信号）：**


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_std_dev (IOg(close
> Volume
> 508
> Needs Improvement
> 眙 Single Data Set Alpha
> Aggregate Data
> Sharoe
> Turnoie
> Fitness
> REturns
> Drawdown
> Warein
> Simulation Settings
> 0.82
> 1.8596
> 0.76
> 10.72%
> 36.70%
> 115.869600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Tuncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handlng
> MaxTrade
> US-
> 7C33000
> Fasz Expression
> 0.33
> Subirdustry
> Ot
> Verif
> Vear
> Sharpe
> TUINOeT
> Htness
> Retums
> Drawdown
> Narqin
> Count
> Short Count
> 2018
> 1,37
> 21195
> 359:
> 3.99
> 112403oc
> 586
> 1-52
> 2013
> 1.13
> 1.553
> 0.35
> 5.557
> 4.48I
> 73.5336
> 1561
> 1-75
> Clone Alpha
> 2020
> -1,75
> 993
> 2.1
> 15.349
> 20.00I
> 154.413oc
> 593
> 11
> 2021
> 9.24
> 1359
> 1.13
> 1315
> 5.463
> 185.005322
> 16-3
> 1-5
> 2022
> 2.00
> 1.504
> 3.35
> 35.5055
> 3.313
> 144.23360c
> 1522
> 1-55
> N Chart
> Prl
> 2023
> 4445
> 9.59
> -72.579
> 4,
> 007.052
> 557
> 1513
> LOOOK
> 医 Correlation
> Self Correlation
> Waximum
> Winimum
> Last Rup;
> 2OOOK
> Performance Comparison
> Way '18
> Jn 19
> Way' 19
> SEP '19
> Way '20
> SEp 20
> Iay 21
> SEP '21
> Mayy 22
> SEp '22 Jan'23
> Last RUn;
> Un
> OFC
> Euity
> Jan 21
> SD
> Jon 2


**# 升阶并调试结果（中性化并增加进出场条件，适度微调）：**


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> trade_when(growp_rank (ts_std_dev (returns, 60)
> Sector)
> Broup_neutralize
> inverse
> Its_std_dev (1nB(Close
> Soecacular
> 眙 Sinsle Data Set Alpha
> Aggregate Data
> Sharpe
> Turnore
> Fitness
> RetJrn
> Drawdown
> Marsin
> Simulation Settings
> 2.13
> 14.4896
> 2.51
> 20.11 %
> 9.9396
> 27.78
> Instrument Type
> Regjon
> Unrerse
> Language
> Decay
> Delay
> Truncation
> Neutraliation
> Pasturiation
> NaN Handling
> Unit Handling
> MaxTrade
> Equity
> US-
> TOP3DD0
> Fasz Expression
> 3,03
> Sbircustry
> 0ff
> Verif
> FF
> Year
> Tumover
> Htnoss
> Returs
> Drawdown
> Marqin
> Count
> Short Count
> 2313
> 2.41
> 10.8210
> 2.78
> 6,693f
> 2.8611
> 30.3533
> 823
> 599
> 2013
> 2.53
> 8.133
> 3.03
> 15.354
> 2.5611
> 39.313
> 983
> 715
> Clone Alpha
> 2020
> 1.37
> 1.0311
> 4
> 15.477
> 9.391
> 22.0533
> 725
> 572
> 2021
> 2.05
> 18181
> 2.27
> 22.384
> 9,081
> 2-.5233
> 815
> 625
> 2022
> 2.70
> 21.2531
> 3.19
> 29.605
> 8.743
> 27.365623
> 722
> 532
> N Chart
> Prl
> 2023
> 2.53
> 10.3513
> 3.-7
> 20.81
> 1.0_31
> 0,2133
> 791
> 513
> 7,50OK
> Correlation
> Self Correlation
> Maxmum
> Minimum
> Last Run;
> 5OOOK
> SOOK
> Performance Comparison
> S2p'13
>  Jan 19
> May '19
> SEp '19
> Jan '21
> May'21
> SEP '21
> Jan'22
> May 22
> SEp'22 |a7'23
> Last Rur:
> 9600
> Sharpe
> Long
> May
> May
> SED


**3. 12月03日 成长因子——劳动力效应**


> [!NOTE] [图片 OCR 识别内容]
> 星期日
> @8
> 12月
> Dec
> $战
> 劳动力效应
> 最近12个月的人均销售收人 (TTM)
> 上年同堋值
> 上年屙期值
> 4中
> 展近12个月的替业战入 (TTM)
> 人均^窖I 入(TTM)
> 平d员工总教
> s初员工总焱
> R太员工总薮
> 孕均员工总数
> 说明
> 存在劳动力效应
> 给定绡售收人
> 妇果所需的员工入数有所减少 _
>  人]销售收
> 入套所垲长
> 在投资者看来是一
> 个积砭笮号
> 1怨]艾黛 |
> Gbarbsnail
> 345/122
> NhOrIe
> RPUIN
> TUT11
> ATLC
> Straleqyihe
> ACOLTUIII RCUCJ


**# 公式：**

ts_delta(ts_mean(sales, 125) / ts_mean(employee, 125), 250) / ts_delay(ts_mean(sales, 125) / ts_mean(employee, 125), 250)

**拓展：ts_delta(ts_mean(sales, 125) / ts_mean(employee, 125)**

**# 表达式函数**

def f1203_Sales_Employee():

n_values = list(range(125, 1001, 125))

expressions = []

for n in n_values:

# a = ts_mean(sales,n) / ts_mean(employee,n)

a_expr = f"ts_mean(sales, {n}) / ts_mean(employee, {n})"

# b = ts_delta(a,n)/ts_delay(a,n) - 1

b_expr = f"(ts_delta({a_expr}, {n}) / ts_delay({a_expr}, {n})) - 1"

# c = ts_mean(b,n) / ts_std_dev(b,n)

c_expr = f"ts_mean({b_expr}, {n}) / ts_std_dev({b_expr}, {n})"

# d = 1 / ts_std_dev(b,n)

d_expr = f"1 / ts_std_dev({b_expr}, {n})"

# 依次添加到总列表中

expressions.append(a_expr)

expressions.append(b_expr)

expressions.append(c_expr)

expressions.append(d_expr)

return expressions

**# 原始数据回测（信号强烈）：**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_delta(ts_mean(sales, 125)
> ts_mean
> employee, 125),
> 125 )
> Good
> 眙Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marsin
> simulation Settings
> 1.45
> 3.9496
> 1.87
> 20.849
> 13.1
> 105.729600
> Instrument Type
> Region
> Unmerse
> LangUage
> Decay
> Vellay
> Truncation
> Neutralizatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Equity
> US
> T033000
> Fasz Expression
> 0.03
> Subirdustry
> Off
> Verify
> DFF
> Year
> TUITOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2018
> 0.92
> 5.0611
> 0,74
> 3.13
> 5.6-53
> 32.3153
> 1397
> 1203
> 2013
> 2.33
> 3.921
> 3,43
> 27.974
> 8.783
> 142.608620
> 366
> 1320
> Clone Alpha
> 2020
> 3.291
> 2.53
> 31,203
> 12.053
> 89.925633
> 360
> 353
> 2021
> 3-21
> 20.313
> 13,113
> 118.79523
> 145.
> 1133
> 2022
> 0.35
> 4.15{
> 0,31
> 13.27
> 39+
> 63.99523
> 1418
> 1311
> N Chart
> Pnl
> 2023
> 3.67
> 6931
> 22.35
> 35,3575
> 0.623
> 026.0-523
> 1451
> 1215
> Correlation
> 7,50OK
> Self Correlation
> Waximum
> Winimum
> Last Run;
> 5OOOK
> Z5OOK
> Performance Comparison
> Way '18
> SEp 18
> Jn'19
> Way'19
> Jan '21
> May' 21
> SEP '21
> Jan '22
> May 22
> SEpP '22
> Jan'23
> Last Run:
> Sharpe
> Long
> S-D
> Maj
> SD
**

**# 升阶并调试效果（中性化并增加进出场条件，适当微调）**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> trade_When(ts_
> ZScore (returns
> 60)
> Eroup_neutralize (ts_delta
> ts_mean(sales,
> 125)
> mean(employee,
> 125
> Se-tacular
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Rezurns
> Drawdown
> Iarsin
> Simulation Settings
> 2.18
> 5.78%
> 2.82
> 20.9196
> 7.0796
> 72.359600
> Instrument Type
> Region
> Unmerse
> Lanquage
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unt Handlling
> MaxTrade
> Equit
> US4
> TO330O0
> Fast Expression
> 0.05
> Subirdustry
> St
> Verity
> DFF
> Sharpe
> Turnover
> Ftnoss
> Returs
> Drawdown
> Maryin
> LOng Count
> Short Count
> 2013
> 1.29
> 5.579
> 1.11
> 919
> 5.053
> 33.00830
> 993
> 1001
> 2019
> 236
> 4.2795
> 3,75
> 21.619
> 1.2053
> 101.15S3
> 11-3
> 1157
> Clone Alpha
> 2020
> 34
> 2.37
> 21.174
> 5.183
> 61.00830
> 351
> 1112
> 2021
> 9635
> 1,33
> 14.69%
> 7.0753
> 59.25933
> 1113
> 1015
> 2022
> 302
> 7.36
> 5,12
> 35939
> 5.283
> 57.62C
> 1102
> 1100
> N Chart
> Prl
> 2023
> 4.37
> 3.543
> 3.533
> 47.913
> 1.3
> 263.47933
> 1253
> 1135
> 医 Correlation
> 75OOK
> Self Correlation
> WaxmuM
> Winimum
> Last Run:
> 5OOOK
> 25OOK
> Performance Comparison
> Way'13
> S2p'13
> Jan 19
> Way'19
> SEp '19
> May 20
> Sep 20
> Jan '21
> May 21
> SEp '21
> Jan'22
> May 22
> SEp '22
> Jan '23
> Last
> Year
> Run:
**

**三、简要总结：**

**1. 经济学原理是通的，虽然多是国内投研的因子，USA依然能跑出信号。**

**2. 复现的过程是学习，关键在于对字段的深刻理解和操作符的灵活运用。**

**3. 学习的目的是拓展，重点是对因子构建逻辑的领会和灵感的孜孜追索**  **。**

**流水不争先，争的是滔滔不绝；眼中有光、心中有爱，才能走的够长远。**

**如有疑问，及时反馈，非常感谢！学习中如有困惑，欢迎论坛留言交流。**

**顾问 JG15244 (Rank 67) 的解答与建议**:
大受震撼！！！！！！！！！！！！！！！！！！！！！

震撼之情，已经不知道怎么表达了，只能说一句，大佬牛逼！

期待大佬成功正式顾问，加入研究小组，带来更加精彩的分享！

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================


---

### 技术对话片段 26 (原帖: 依次添加到总列表中)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】复现2023年因子日历论坛精选_33049767468055.md
- **时间**: 1年前

**提问/主帖背景 (LR93609)**:
**一、概况：**

**1. 2023年因子日历，日历部分共379页，删除、去重、合并并整理后约359个因子...**


> [!NOTE] [图片 OCR 识别内容]
> 2029
> 詈


**2. 我从3月初开始复现，预计7月初整理完成，历时近4个月...**

**
> [!NOTE] [图片 OCR 识别内容]
> 财务因子 (79个)
> 规模因子 (6个)
> 投资因子 (19个)
> 成长因子 (20个)
> 估值因子 (17个)
> 波动率因子 (25个)
> 杠杆因子 (10个)
> 流动性因子 (19个)
> 动量因子 (25个)
> 13
> 质量因子
> (4个)
> 11
> 技术因子 (39个)
> 12
> 无形资产 (9个)
> 13
> 股东因子 (6个)
> 14.
> 公司治理 (2个)
> 另类因子 (21个)
> 15
> 分析师因子 (20个)
> 高频因子 (38个)
> 成交量占比:  0x开盘黛合竟众成交量-(1-0) 收盏集合竞价成交量
> -致卖出/买入交易:
> 股权集中度:  前三大流通股东持股数/流通股股本
> 价量相关性趋势因子:
> 成交量比值:  每曰上午
> 下午开盘前30分钟成交量的比值
> TRt
> U
> Lolmowin
> 卫t
> 工i)
> 时间加权平均的股票相对价格位置:
> RP卫 .t
> {olfemon
**

**3. 对多信号因子创建Alpha-tree回测，约105个trees，1677+行函数表达式，仍在整理中...**

**
> [!NOTE] [图片 OCR 识别内容]
> 2023
> 1473
> def
> f1121_Amount ( ):
> Apr
> 1474
> n_values
> list (range(125,
> 1801,
> 125) )
> 1475
> expressions
> []
> Dec
> 1476
> 1477
> for
> in n_values
> Jan
> 1478
> product_expr
> "log(close
> Volume
> July
> 1479
> mean_expr
> f"ts
> mean ( {product_
> expr},
> {n})
> Mar
> 1488
> std_expr
> f"ts
> std_dev({product_expr},
> {n})
> 1481
> final_expr
> f"{mean_expr}
> {std_expr}
> NeV
> 1482
> expressions .append (mean_expr _
> 61101_List_
> 1483
> expressions .append (final_expr
> 1484
> eXP-
> u
> O
> C;^1
> 01114_Operating_Curr _
> (variable) expressions
> Iist
> 1485
> 01118_Cash_Income
> 1486
> return expressions
> Q1121_Amount
> 1487
> 01122_Movement
> 1488
> def
> f1122_Movement ():
> 01129_News
> 1489
> n_Values
> Iist (range (19
> 252,10) )
> Oct
> 1498
> 初始化三个空列表
> Sec
> 1491
> expr
> []
> 1492
> for
> in n_values
> 1493
> rank(returns )
> 4888
> 4881
> 2024
> 1494
> a_eXpr
> f"rank(returns )
> 4888
> 4801
> factors_lib_2023.py
> 1495
> # b
> sqrt (48e1
> 3999
> 12)
> factors lib
> 2024py
> 1496
> b_expr
> +
> {a_expr}
> sqrt ( 4881
> 3999
> 12)
> factors_lib
> 1497
> ts_mean(b,
> h)
> factors_lib_Vo.py
> 1498
> C_expr
> f"ts_mean ({bexpr},
> {n})
> 1499
> ts_std_dev(b,
> 几)
> filters_
> 1588
> d_expr
> std_dev ({bexpr},
> {n})
> functionpy
> 1581
> machine_
> 1502
> eXpr
> f"{bexpr}
> {d_expr}
> Aug
> May
> Days
> '
> Sep
> TS.Py
> lib py
> "ts _
> Jib py
**

**4. 结论：**

**1）除部分user操作符和字段受限的因子外，其他多数因子是有信号的，稍作调试便可能得到不错的效果。**

**2）多数高频因子可以降维使用，主要是借鉴其构建逻辑；**  **分析师或另类因子，可以选择datafield替代，借鉴其idea。**

**3）技术类因子，可以选择操作符替代，比如用ts_mean替代SMA，用ts_decay_linear近似替代EMA（效果一般），特殊情形中用ts_sum部分实现递归运算等...**

**二、举例（仅选择其中表现相对优异的几个予以示意）：**

**1. 1月19日 流动性因子—— Amihub 非流动性因子**

**（由于IQC无法获取当日成交额数据，此处用close*volume近似）**


> [!NOTE] [图片 OCR 识别内容]
> 星期四
> 96
> 1月
> Jan.
> 躺局忪
> Amihud 非流动性因子
> 勐牺厅
> IRial
> ILLIQit
> VOLDid
> 其中
> R;d为 t月内殷票
> 的巳宦收益率;
> VOLDiu 为 [月内股祟
> 的E度咸交额;
> 通常要汆月内正常交易的交易日夫数不少亍15天。
> 说明
> 预期市场流动性不足会对V前股票超额妆益产生积极影响 ,
> 带来非流动性滏价;
> 取值越高
> 流动性及险趱大。诋担及险带来的末来收益趱高 _
> !^考交s
> TTHU?
> rakg。 7002
> NNIII
> T
> LrCts-SCCUICT
> Serles etfz-ts。
> CIe
> Fnoncial Marlets
> Jug


**# 公式**

Amihud = ts_mean(abs(returns)/volume/close,n)

**# 表达式函数**

def f0119_Amihud():

expressions = []

windows = range(20, 500, 20)

for window in windows:

expr = f"-ts_mean((abs(returns) / (volume * close)), {window})"

expressions.append(expr)

return expressions

**# 调试结果（升阶并调试效果：中性化并增加进出场条件）**


> [!NOTE] [图片 OCR 识别内容]
> 10N
> OOOK
> OOOK
> OOOK
> OOOK
> Nay '18
> Sep '18
> Jan 19
> 5ep'19
> Sep '20
> Jan '21
> Nay '21
> SCP "21
> Jan "22
> May'22
> Jan '23
> Iay
> May
> SCN



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 0C
> Spectacular
> Asingle Data Set Alpha
> Aggregate Data
> Sharpe
> TIICn N?
> TTSc
> RPITT
> Drawow
> Margin
> 2.30
> 14.9396
> 3.00
> 25.3996
> 9.18%
> 34.029600
> Year
> Sharpe
> TUrnOVeT
> Ftness
> Retums
> Drawdoyn
> Marqin
> Count
> Short Count
> 2018
> 0.31
> 11.319
> 0.11
> 2.05呖
> 5.93%
> 3.529
> 1915
> 1129
> 2019
> 2.18
> 15.55%
> 2.4
> 98%
> 50035
> 25.715
> 1933
> 1103
> 2020
> 2.24
> 16.3395
> 3.07
> 30.839
> 089
> 37.58Cco
> 97
> 1085
> 2021
> 2.92
> 16.41%
> 4.37
> 36.72%
> 9.1835
> 44.74
> 2005
> 1080
> 2022
> 15,139
> 425
> 33,539
> 5.1035
> 4.34o
> 2035
> 1052
> 2023
> 7.51
> 10.639
> 9.42
> 83.50%
> 743
> 157.3r
> 2070
> 1037
> Correlation
> Self Correlation
> MaximuI
> Winimum
> Las Run:
> Check Submission
> Submit Alpha
> Long


**2. 6月10日VS 11月21日 流动性因子——成交额 VS 成交额波动系数**

**（由于IQC无法获取当日成交额数据，此处用close*volume近似）**


> [!NOTE] [图片 OCR 识别内容]
> 星期五
> @@
> 10月
> Oct
> 》尻乩性
> 成交额
> 最近K个月日度成交额的均值
> 即:
> mean (最近'个月日度戍交额序列)
> 说明
> 衡蟹股票交易流动性的虿斐捐硫
> 如冥股票流动性较差
> ,格扫对较低
> 投资者对
> 其预期收益就会较高
> 存在流动性溢价
> (袄号文颍 !
> Rrrra I
> TTUT Uel
> AATCHa [
> SUbIaRNaTS, 1999
> Je;it;
> T
> 50aritI3
> 10/5
> SOUTI
> 'IIITCTTS5
> 5T
> PNeCeO
> SUC
> PIUIN
> e:Ja|
> FIIATCIU'
> EONOITS 49,345.173,



> [!NOTE] [图片 OCR 识别内容]
> 星期二
> 十月初九
> 29
> 11月
> NoV
> 流动性
> 成交额波动系数
> '^国
> mean (最近{个月日度咸交鞭庐列)
> std (最近氐个月日度成交额序列)
> 说明
> 在衡量咸交颧高低水乎的同时还考虑了成交额的波动惜况,是u量交易流动性的
> 综合性指标。
> 5薄文咸 
> TCVCI
> LCI Ku
> Zhnd。 1020. teplcaiing
> 71+
> I
> FnanCia
> Slucles 32[51


**# 公式**

ts_mean( log(volume*close),500)

拓展：1/ ts_std_dev( log(volume*close), 500)

**# 表达式函数**

def f1121_Amount():

n_values = list(range(125, 1001, 125))

expressions = []

for n in n_values:

product_expr = "log(close * volume)"

mean_expr = f"ts_mean({product_expr}, {n})"

std_expr = f"ts_std_dev({product_expr}, {n})"

final_expr = f"{mean_expr} / {std_expr}"

expressions.append(mean_expr)

expressions.append(final_expr)

expressions.append(final_expr)

return expressions

**# 原始数据回测（有信号）：**


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_std_dev (IOg(close
> Volume
> 508
> Needs Improvement
> 眙 Single Data Set Alpha
> Aggregate Data
> Sharoe
> Turnoie
> Fitness
> REturns
> Drawdown
> Warein
> Simulation Settings
> 0.82
> 1.8596
> 0.76
> 10.72%
> 36.70%
> 115.869600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Tuncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handlng
> MaxTrade
> US-
> 7C33000
> Fasz Expression
> 0.33
> Subirdustry
> Ot
> Verif
> Vear
> Sharpe
> TUINOeT
> Htness
> Retums
> Drawdown
> Narqin
> Count
> Short Count
> 2018
> 1,37
> 21195
> 359:
> 3.99
> 112403oc
> 586
> 1-52
> 2013
> 1.13
> 1.553
> 0.35
> 5.557
> 4.48I
> 73.5336
> 1561
> 1-75
> Clone Alpha
> 2020
> -1,75
> 993
> 2.1
> 15.349
> 20.00I
> 154.413oc
> 593
> 11
> 2021
> 9.24
> 1359
> 1.13
> 1315
> 5.463
> 185.005322
> 16-3
> 1-5
> 2022
> 2.00
> 1.504
> 3.35
> 35.5055
> 3.313
> 144.23360c
> 1522
> 1-55
> N Chart
> Prl
> 2023
> 4445
> 9.59
> -72.579
> 4,
> 007.052
> 557
> 1513
> LOOOK
> 医 Correlation
> Self Correlation
> Waximum
> Winimum
> Last Rup;
> 2OOOK
> Performance Comparison
> Way '18
> Jn 19
> Way' 19
> SEP '19
> Way '20
> SEp 20
> Iay 21
> SEP '21
> Mayy 22
> SEp '22 Jan'23
> Last RUn;
> Un
> OFC
> Euity
> Jan 21
> SD
> Jon 2


**# 升阶并调试结果（中性化并增加进出场条件，适度微调）：**


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> trade_when(growp_rank (ts_std_dev (returns, 60)
> Sector)
> Broup_neutralize
> inverse
> Its_std_dev (1nB(Close
> Soecacular
> 眙 Sinsle Data Set Alpha
> Aggregate Data
> Sharpe
> Turnore
> Fitness
> RetJrn
> Drawdown
> Marsin
> Simulation Settings
> 2.13
> 14.4896
> 2.51
> 20.11 %
> 9.9396
> 27.78
> Instrument Type
> Regjon
> Unrerse
> Language
> Decay
> Delay
> Truncation
> Neutraliation
> Pasturiation
> NaN Handling
> Unit Handling
> MaxTrade
> Equity
> US-
> TOP3DD0
> Fasz Expression
> 3,03
> Sbircustry
> 0ff
> Verif
> FF
> Year
> Tumover
> Htnoss
> Returs
> Drawdown
> Marqin
> Count
> Short Count
> 2313
> 2.41
> 10.8210
> 2.78
> 6,693f
> 2.8611
> 30.3533
> 823
> 599
> 2013
> 2.53
> 8.133
> 3.03
> 15.354
> 2.5611
> 39.313
> 983
> 715
> Clone Alpha
> 2020
> 1.37
> 1.0311
> 4
> 15.477
> 9.391
> 22.0533
> 725
> 572
> 2021
> 2.05
> 18181
> 2.27
> 22.384
> 9,081
> 2-.5233
> 815
> 625
> 2022
> 2.70
> 21.2531
> 3.19
> 29.605
> 8.743
> 27.365623
> 722
> 532
> N Chart
> Prl
> 2023
> 2.53
> 10.3513
> 3.-7
> 20.81
> 1.0_31
> 0,2133
> 791
> 513
> 7,50OK
> Correlation
> Self Correlation
> Maxmum
> Minimum
> Last Run;
> 5OOOK
> SOOK
> Performance Comparison
> S2p'13
>  Jan 19
> May '19
> SEp '19
> Jan '21
> May'21
> SEP '21
> Jan'22
> May 22
> SEp'22 |a7'23
> Last Rur:
> 9600
> Sharpe
> Long
> May
> May
> SED


**3. 12月03日 成长因子——劳动力效应**


> [!NOTE] [图片 OCR 识别内容]
> 星期日
> @8
> 12月
> Dec
> $战
> 劳动力效应
> 最近12个月的人均销售收人 (TTM)
> 上年同堋值
> 上年屙期值
> 4中
> 展近12个月的替业战入 (TTM)
> 人均^窖I 入(TTM)
> 平d员工总教
> s初员工总焱
> R太员工总薮
> 孕均员工总数
> 说明
> 存在劳动力效应
> 给定绡售收人
> 妇果所需的员工入数有所减少 _
>  人]销售收
> 入套所垲长
> 在投资者看来是一
> 个积砭笮号
> 1怨]艾黛 |
> Gbarbsnail
> 345/122
> NhOrIe
> RPUIN
> TUT11
> ATLC
> Straleqyihe
> ACOLTUIII RCUCJ


**# 公式：**

ts_delta(ts_mean(sales, 125) / ts_mean(employee, 125), 250) / ts_delay(ts_mean(sales, 125) / ts_mean(employee, 125), 250)

**拓展：ts_delta(ts_mean(sales, 125) / ts_mean(employee, 125)**

**# 表达式函数**

def f1203_Sales_Employee():

n_values = list(range(125, 1001, 125))

expressions = []

for n in n_values:

# a = ts_mean(sales,n) / ts_mean(employee,n)

a_expr = f"ts_mean(sales, {n}) / ts_mean(employee, {n})"

# b = ts_delta(a,n)/ts_delay(a,n) - 1

b_expr = f"(ts_delta({a_expr}, {n}) / ts_delay({a_expr}, {n})) - 1"

# c = ts_mean(b,n) / ts_std_dev(b,n)

c_expr = f"ts_mean({b_expr}, {n}) / ts_std_dev({b_expr}, {n})"

# d = 1 / ts_std_dev(b,n)

d_expr = f"1 / ts_std_dev({b_expr}, {n})"

# 依次添加到总列表中

expressions.append(a_expr)

expressions.append(b_expr)

expressions.append(c_expr)

expressions.append(d_expr)

return expressions

**# 原始数据回测（信号强烈）：**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_delta(ts_mean(sales, 125)
> ts_mean
> employee, 125),
> 125 )
> Good
> 眙Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marsin
> simulation Settings
> 1.45
> 3.9496
> 1.87
> 20.849
> 13.1
> 105.729600
> Instrument Type
> Region
> Unmerse
> LangUage
> Decay
> Vellay
> Truncation
> Neutralizatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Equity
> US
> T033000
> Fasz Expression
> 0.03
> Subirdustry
> Off
> Verify
> DFF
> Year
> TUITOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2018
> 0.92
> 5.0611
> 0,74
> 3.13
> 5.6-53
> 32.3153
> 1397
> 1203
> 2013
> 2.33
> 3.921
> 3,43
> 27.974
> 8.783
> 142.608620
> 366
> 1320
> Clone Alpha
> 2020
> 3.291
> 2.53
> 31,203
> 12.053
> 89.925633
> 360
> 353
> 2021
> 3-21
> 20.313
> 13,113
> 118.79523
> 145.
> 1133
> 2022
> 0.35
> 4.15{
> 0,31
> 13.27
> 39+
> 63.99523
> 1418
> 1311
> N Chart
> Pnl
> 2023
> 3.67
> 6931
> 22.35
> 35,3575
> 0.623
> 026.0-523
> 1451
> 1215
> Correlation
> 7,50OK
> Self Correlation
> Waximum
> Winimum
> Last Run;
> 5OOOK
> Z5OOK
> Performance Comparison
> Way '18
> SEp 18
> Jn'19
> Way'19
> Jan '21
> May' 21
> SEP '21
> Jan '22
> May 22
> SEpP '22
> Jan'23
> Last Run:
> Sharpe
> Long
> S-D
> Maj
> SD
**

**# 升阶并调试效果（中性化并增加进出场条件，适当微调）**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> trade_When(ts_
> ZScore (returns
> 60)
> Eroup_neutralize (ts_delta
> ts_mean(sales,
> 125)
> mean(employee,
> 125
> Se-tacular
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Rezurns
> Drawdown
> Iarsin
> Simulation Settings
> 2.18
> 5.78%
> 2.82
> 20.9196
> 7.0796
> 72.359600
> Instrument Type
> Region
> Unmerse
> Lanquage
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unt Handlling
> MaxTrade
> Equit
> US4
> TO330O0
> Fast Expression
> 0.05
> Subirdustry
> St
> Verity
> DFF
> Sharpe
> Turnover
> Ftnoss
> Returs
> Drawdown
> Maryin
> LOng Count
> Short Count
> 2013
> 1.29
> 5.579
> 1.11
> 919
> 5.053
> 33.00830
> 993
> 1001
> 2019
> 236
> 4.2795
> 3,75
> 21.619
> 1.2053
> 101.15S3
> 11-3
> 1157
> Clone Alpha
> 2020
> 34
> 2.37
> 21.174
> 5.183
> 61.00830
> 351
> 1112
> 2021
> 9635
> 1,33
> 14.69%
> 7.0753
> 59.25933
> 1113
> 1015
> 2022
> 302
> 7.36
> 5,12
> 35939
> 5.283
> 57.62C
> 1102
> 1100
> N Chart
> Prl
> 2023
> 4.37
> 3.543
> 3.533
> 47.913
> 1.3
> 263.47933
> 1253
> 1135
> 医 Correlation
> 75OOK
> Self Correlation
> WaxmuM
> Winimum
> Last Run:
> 5OOOK
> 25OOK
> Performance Comparison
> Way'13
> S2p'13
> Jan 19
> Way'19
> SEp '19
> May 20
> Sep 20
> Jan '21
> May 21
> SEp '21
> Jan'22
> May 22
> SEp '22
> Jan '23
> Last
> Year
> Run:
**

**三、简要总结：**

**1. 经济学原理是通的，虽然多是国内投研的因子，USA依然能跑出信号。**

**2. 复现的过程是学习，关键在于对字段的深刻理解和操作符的灵活运用。**

**3. 学习的目的是拓展，重点是对因子构建逻辑的领会和灵感的孜孜追索**  **。**

**流水不争先，争的是滔滔不绝；眼中有光、心中有爱，才能走的够长远。**

**如有疑问，及时反馈，非常感谢！学习中如有困惑，欢迎论坛留言交流。**

**顾问 JG15244 (Rank 67) 的解答与建议**:
大受震撼！！！！！！！！！！！！！！！！！！！！！

震撼之情，已经不知道怎么表达了，只能说一句，大佬牛逼！

期待大佬成功正式顾问，加入研究小组，带来更加精彩的分享！

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================


---

### 技术对话片段 27 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【哥布林】基于IND Region的Regular Alpha古法手搓技巧经验分享.md
- **时间**: 7个月前

**提问/主帖背景 (SC23342)**:
机缘巧合下发现了一些适用IND的优化方法，对其他Region的适用性可能不够强，但也可以作为一定程度的参考吧

注：以下将weight concentration简称为wc

- 建议的默认setting配置：

Neutralization: MARKET

Max trade: OFF

从个人回测和提交结果看，market的出货率最高，切换其他neut后更容易出现wc问题或Robust Sharpe偏低，以及更低的IS指标，小概率能发现其他neut可能存在较低的相关性，因此只在最终优化阶段才尝试；

Max trade一般也会带来wc问题，即使是IS较高，打开后指标基本不变的alpha，甚至略有提升的alpha，也会产生wc10-wc15的fail，或叠加Robust Sharpe fail而导致无法提交的情况，如果wc能放宽到15，或许打开max能有很多可提交的alpha(doge)

- 通用手搓法：

1.反转信号： [[L2] 【哥布林】杂论1关于setting配置和ops选择使用方面的个人经验_35698887416983.md]([L2] 【哥布林】杂论1关于setting配置和ops选择使用方面的个人经验_35698887416983.md)

2.ts系列时间参数选用：fnd数据使用长期回溯起步(例如252)，非fnd数据使用短期回溯起步(例如5)

3.group系列分组参数选用：遍历sector, industry, subindustry和pv系的50分组，即分组命名中带50的分组，此类分组一旦有一个存在信号，其余同类分组必定存在相对更强或较弱的信号范围，因此初步尝试时无需全部遍历

4.ops选用：仅使用一元运算符。遍历所有可用的一元运算符，专注于探索该数据的运算关系；出现高turnover时，再考虑使用能降turnover的二元运算符

5.哥布林鲁棒：即对目前使用的运算符做A(n)全排序。当使用2个以上运算符时，可尝试使用此法遍历，小概率可获得相关性更低的alpha，也有可能同时提升IS指标

6.使用自相似的表达式构建，即在相邻层或间隔层再次使用相同的运算符，达成在更小的颗粒度尝试提升指标且不拉伸六维的目的，例如经典的加速度模板ts_delta(ts_delta(x, d), d)

- 如何有效解决wc问题

1.降低truncation，非常适用IND，往往能发现越低的truncation，IS指标会越高

2.通过ts_mean/ts_median/ts_sum这几种统计层面的时序运算符规避wc，理论上回溯时间越长wc越低，但IS指标可能会急剧下降

3.增大ts运算符的时间参数

4.略微提升decay+微调truncation

5.使用group_neutralize + pv分组或bucket组合一些特别的分组

6.对fnd数据可尝试使用group_mean，分组参数可尝试market以外的所有分组

- 其他的细节

1.在IND中，None的中性化似乎相较其他region具有更强的适用性

2.Robust Sharpe <= 0.5的可直接放弃，其优化上限大概率无法达到1.0

3.当wc的fail提示出现wc50，wc100甚至wc too strong，其实并不意味着无法解决，许多时候使用一个ts_mean就可以降低到正常水平，若同时组合使用了几种方法仍然出现wc too strong，才可能真正说明它存在严重的wc问题

4.当Sector呈现wc问题时，Industry和Subindustry大概率会产生更高的wc问题

5.IND似乎不大适用Sector + Subindustry这种双重中性化的组合

6.IND存在一个天然优势，所有类型的pyramid都是1.5，那么就可以将所有类型的数据集都基于genius的规则两两组合，在相当程度上助力了出货的可能性，而不必像其余region只能对相同pyramid的进行组合，对不同类型的数据可能性研究十分有限，在数据集本身上的局限性也较大

**顾问 JG15244 (Rank 67) 的解答与建议**:
好棒的帖子，帮助非常的多，不仅对ind这个地区有较深的理解，而且对平台的运算符、中性化、check指标好深的理解哇。

ind刚出来的时候，跑过几天，速度感觉很慢，也没有出货（我是默认打开的maxtrade、中性化使用的subindustry，侧面印证了贴主的正确性）。

等后面回测数量真的限制后，再去探索一下ind！


---

### 技术对话片段 28 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【哥布林】基于IND Region的Regular Alpha古法手搓技巧经验分享_36222781155607.md
- **时间**: 7个月前

**提问/主帖背景 (SC23342)**:
机缘巧合下发现了一些适用IND的优化方法，对其他Region的适用性可能不够强，但也可以作为一定程度的参考吧

注：以下将weight concentration简称为wc

- 建议的默认setting配置：

Neutralization: MARKET

Max trade: OFF

从个人回测和提交结果看，market的出货率最高，切换其他neut后更容易出现wc问题或Robust Sharpe偏低，以及更低的IS指标，小概率能发现其他neut可能存在较低的相关性，因此只在最终优化阶段才尝试；

Max trade一般也会带来wc问题，即使是IS较高，打开后指标基本不变的alpha，甚至略有提升的alpha，也会产生wc10-wc15的fail，或叠加Robust Sharpe fail而导致无法提交的情况，如果wc能放宽到15，或许打开max能有很多可提交的alpha(doge)

- 通用手搓法：

1.反转信号： [[L2] 【哥布林】杂论1关于setting配置和ops选择使用方面的个人经验_35698887416983.md]([L2] 【哥布林】杂论1关于setting配置和ops选择使用方面的个人经验_35698887416983.md)

2.ts系列时间参数选用：fnd数据使用长期回溯起步(例如252)，非fnd数据使用短期回溯起步(例如5)

3.group系列分组参数选用：遍历sector, industry, subindustry和pv系的50分组，即分组命名中带50的分组，此类分组一旦有一个存在信号，其余同类分组必定存在相对更强或较弱的信号范围，因此初步尝试时无需全部遍历

4.ops选用：仅使用一元运算符。遍历所有可用的一元运算符，专注于探索该数据的运算关系；出现高turnover时，再考虑使用能降turnover的二元运算符

5.哥布林鲁棒：即对目前使用的运算符做A(n)全排序。当使用2个以上运算符时，可尝试使用此法遍历，小概率可获得相关性更低的alpha，也有可能同时提升IS指标

6.使用自相似的表达式构建，即在相邻层或间隔层再次使用相同的运算符，达成在更小的颗粒度尝试提升指标且不拉伸六维的目的，例如经典的加速度模板ts_delta(ts_delta(x, d), d)

- 如何有效解决wc问题

1.降低truncation，非常适用IND，往往能发现越低的truncation，IS指标会越高

2.通过ts_mean/ts_median/ts_sum这几种统计层面的时序运算符规避wc，理论上回溯时间越长wc越低，但IS指标可能会急剧下降

3.增大ts运算符的时间参数

4.略微提升decay+微调truncation

5.使用group_neutralize + pv分组或bucket组合一些特别的分组

6.对fnd数据可尝试使用group_mean，分组参数可尝试market以外的所有分组

- 其他的细节

1.在IND中，None的中性化似乎相较其他region具有更强的适用性

2.Robust Sharpe <= 0.5的可直接放弃，其优化上限大概率无法达到1.0

3.当wc的fail提示出现wc50，wc100甚至wc too strong，其实并不意味着无法解决，许多时候使用一个ts_mean就可以降低到正常水平，若同时组合使用了几种方法仍然出现wc too strong，才可能真正说明它存在严重的wc问题

4.当Sector呈现wc问题时，Industry和Subindustry大概率会产生更高的wc问题

5.IND似乎不大适用Sector + Subindustry这种双重中性化的组合

6.IND存在一个天然优势，所有类型的pyramid都是1.5，那么就可以将所有类型的数据集都基于genius的规则两两组合，在相当程度上助力了出货的可能性，而不必像其余region只能对相同pyramid的进行组合，对不同类型的数据可能性研究十分有限，在数据集本身上的局限性也较大

**顾问 JG15244 (Rank 67) 的解答与建议**:
好棒的帖子，帮助非常的多，不仅对ind这个地区有较深的理解，而且对平台的运算符、中性化、check指标好深的理解哇。

ind刚出来的时候，跑过几天，速度感觉很慢，也没有出货（我是默认打开的maxtrade、中性化使用的subindustry，侧面印证了贴主的正确性）。

等后面回测数量真的限制后，再去探索一下ind！


---

### 技术对话片段 29 (原帖: 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30))
- **原帖链接**: [Commented] 【学习笔记】Gold普遍有权限的Operator 4.md
- **时间**: 1年前

**提问/主帖背景 (FD69320)**:
## 31. group_rank

***功能说明：*** 将股票按指定的分组方式(如行业、子行业等)进行分组，然后在每个组内对股票基于输入值进行排序，返回一个在 0.0 到 1.0 之间均匀分布的数值。这个操作符可以帮助减少异常值和回撤，同时降低相关性。

***参数说明*** ：

- - x: 需要排序的数值
- - group: 分组依据（如行业、子行业等）

***计算过程：***

```
科技行业:  苹果(AAPL):    volume = 85M  微软(MSFT):    volume = 45M  谷歌(GOOGL):   volume = 25M  英特尔(INTC):  volume = 65M  英伟达(NVDA):  volume = 95M金融行业:  摩根大通(JPM):   volume = 15M  高盛(GS):       volume = 8M  美国银行(BAC):   volume = 22M  花旗集团(C):     volume = 18M  富国银行(WFC):   volume = 12M零售行业:  亚马逊(AMZN):    volume = 42M  沃尔玛(WMT):     volume = 28M  塔吉特(TGT):     volume = 15M  好市多(COST):    volume = 35M
```

***使用group_rank后的结果***

```
科技行业: (5只股票，排名间隔为0.25)  英伟达(NVDA):   95M -> 1.00  (第5名)  苹果(AAPL):     85M -> 0.75  (第4名)  英特尔(INTC):   65M -> 0.50  (第3名)  微软(MSFT):     45M -> 0.25  (第2名)  谷歌(GOOGL):    25M -> 0.00  (第1名)金融行业: (5只股票，排名间隔为0.25)  美国银行(BAC):   22M -> 1.00  (第5名)  花旗集团(C):     18M -> 0.75  (第4名)  摩根大通(JPM):   15M -> 0.50  (第3名)  富国银行(WFC):   12M -> 0.25  (第2名)  高盛(GS):        8M -> 0.00   (第1名)零售行业: (4只股票，排名间隔为0.33)  亚马逊(AMZN):    42M -> 1.00  (第4名)  好市多(COST):    35M -> 0.67  (第3名)  沃尔玛(WMT):     28M -> 0.33  (第2名)  塔吉特(TGT):     15M -> 0.00  (第1名)
```

***使用示例***

```
# 示例1：在行业内对成交量进行排名，找出成交量排名靠前的股票alpha = group_rank(volume, industry)high_volume_stocks = alpha > 0.8  # 选择行业内成交量排名前20%的股票# 示例2：结合其他指标使用# 在行业内同时考虑成交量和价格动量alpha = 0.5 * group_rank(volume, industry) + 0.5 * group_rank(returns_5d, industry)
```

## 32. ts_delta

***功能说明**  **：*** ts_delta 计算当前值与 d 天前的值之差。这是一个用于计算变化量的时间序列操作符。

***参数说明：***

- - x: 输入的时间序列数据
- - d: 回溯的天数

***使用示例：***

```
# 示例1: 计算股票价格的5日变化price_change_5d = ts_delta(close, 5)  # 当前收盘价与5天前收盘价之差# 示例2: 计算成交量的日变化volume_change_1d = ts_delta(volume, 1)  # 今日成交量与昨日成交量之差
```

## 33. ts_arg_min

***功能说明：*** 返回过去 d 天内最小值在时间序列中的相对位置（相对于当前日期的偏移量）。如果当前日期的值是最小值，返回0；如果前一天的值是最小值，返回1；以此类推。

***参数说明：***

- - x: 输入的时间序列数据
- - d: 回溯的天数（lookback period）

***计算过程：***

```
# 假设过去6天的数据是 [6,2,8,5,9,4]，其中第一个元素是今天的值x = [6,2,8,5,9,4]  # 从左到右：今天，昨天，前天...d = 6result = ts_arg_min(x, d)  # 返回 1，因为最小值2出现在昨天（偏移量为1）
```

***使用示例：***

```
# 判断股票是否处于20天低点is_recent_low = ts_arg_min(close, 20) == 0# 如果最低点出现在较远的过去，可能表示上升趋势uptrend = ts_arg_min(close, 10) > 5# 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)# 结合最高点和最低点的位置来判断趋势trend = ts_arg_max(close, 20) - ts_arg_min(close, 20)
```

## 34. ts_mean

***功能说明：***  计算过去 d 天的平均值。它是一个时间序列操作符，用于计算移动平均。

***参数说明：***

- - x: 输入的时间序列数据
- - d: 回溯的天数（lookback period）

***使用示例：***

```
# 判断多空趋势is_uptrend = close > ts_mean(close, 20)  # 价格在20日均线之上# 计算价格相对均线的偏离程度price_momentum = close / ts_mean(close, 10) - 1# 短期均线穿越长期均线golden_cross = ts_mean(close, 5) > ts_mean(close, 20)# 计算价格对均值的偏离volatility = close - ts_mean(close, 10)
```

## 35. ts_backfill

***功能说明*** ：用于填充缺失值（NaN）的时间序列操作符。它会用历史数据中最近的有效值来替换当前的 NaN 值。

***参数说明：***

- - x: 输入的时间序列数据
- - lookback: 回溯的天数（默认为d）
- - k: 选择第k个非NaN值（默认为1，即最近的有效值）
- - ignore: 指定要忽略的值（默认为"NAN"）

***计算过程：***

```
# 假设某股票最近6天的数据如下：Day 0 (今天):   NaNDay -1 (昨天):  NaNDay -2:         95Day -3:         NaNDay -4:         90Day -5:         85
```

***k=2时，使用ts_backfill的结果***

```
result = ts_backfill(x, lookback=6, k=2)# 结果：Day 0:          90     # 用第二个有效值90填充Day -1:         90     # 用第二个有效值90填充Day -2:         95     # 原始值保持不变Day -3:         85     # 用第二个有效值85填充Day -4:         90     # 原始值保持不变Day -5:         85     # 原始值保持不变
```

***使用示例***

```
# 股票停牌期间用最近的交易价格填充clean_price = ts_backfill(close, 252)# 财务数据发布间隔期间用最新的数据填充clean_profit = ts_backfill(net_profit, 252)
```

## 36. greater_than_equal

***功能说明：*** 相当于>=, 是一个逻辑比较操作符，用于比较两个输入值。如果第一个输入大于或等于第二个输入，返回 true (1)；否则返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 37. less_than_equal

***功能说明：*** 相当于<=, 是一个逻辑比较操作符，用于比较两个输入值。如果第一个输入小于或等于第二个输入，返回 true (1)；否则返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 38. not_equal

***功能说明：*** 相当于!=, 是一个逻辑比较操作符，用于比较两个输入值是否不相等。如果两个输入值不相等，返回 true (1)；如果相等，返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 39. equal

***功能说明：*** 相当于 \==, 是一个逻辑比较操作符，用于比较两个输入值是否相等。如果两个输入值相等，返回 true (1)；如果相等，返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 40. greater

***功能说明：*** 相当于 >, 是一个逻辑比较操作符，用于比较两个输入值。如果第一个输入严格大于第二个输入，返回 true (1)；否则返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 41. is_nan

***功能说明：*** 是一个逻辑判断操作符，用于检测输入值是否为 NaN (Not a Number)。如果输入是 NaN，返回 1 (true)；如果输入不是 NaN，返回 0 (false)。

***参数说明：***

- - x: 输入值，可以是任何数值类型

## 42. densify

***功能说明：*** 用于将具有多个桶(buckets)的分组字段转换为更少的可用桶，以提高分组字段的计算效率。它会将稀疏的分组值映射到一个连续的、密集的索引范围内。

***参数说明：***

- - x: 输入的分组字段，通常是整数值

***计算过程***

```
# 原始分组值：industry_codes = {0, 1, 2, 99}  # 4个唯一值，但占用了100个可能的桶# densify 后：dense_codes = {0, 1, 2, 3}     # 4个连续的桶
```

## 43. power

***功能说明：*** 是一个算术操作符，它计算 x 的 y 次方，但与普通的幂运算不同，它会保留 x 的符号。

***参数说明：***

- - x: 底数
- - y: 指数

## 44. signed_power

***功能说明：*** 它计算 x 的 y 次方，但会保留 x 的原始符号。

***参数说明：***

- - x: 底数
- - y: 指数

***和power的对比***

```
# 对比 power 和 signed_powerx = [3, -9, -2, 4]y = 2  # 指数为2# 普通 power， 可能丢失方向性信息power_result = [9, 81, 4, 16]  # x^2，结果总是非负# signed_power，留方向性信息signed_power_result = [9, -81, -4, 16]  # sign(x) * |x|^2，保留原始符号
```

## 45. inverse和reverse

***功能说明：*** inverse(x) = 1/x; reverse(x) = -x

## 46. add, subtract, multiply和divide

***功能说明：*** add(x, y) = x+y, subtract(x, y) = x-y, multiply(x, y) = x* y; divide(x, y) = x/y

## 47. max和min

***功能说明：***

- - max: 返回所有输入值中的最大值
- - min: 返回所有输入值中的最小值

## 48. or, and 和not

***功能说明：***

- - or: 在任一输入为真或两个输入都为真时返回真，否则返回假。
- - and: 仅当两个操作数都为真时返回真，否则返回假。
- - not: 逻辑取反值。如果 x 为真(1)，返回假(0)；如果输入为假(0)，返回真(1)。

## 49. abs

***功能说明：*** 返回输入值的绝对值。

## 50. sign

***功能说明：*** 返回输入值的符号, 正数返回 1, 负数返回 -1, 零返回 0。

**顾问 JG15244 (Rank 67) 的解答与建议**:
收益良多啊，扫清了很多之前模糊的内容。

有个问题想问一下：

这个为什么可以统计最低点出现的频率

```
# 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)
```


---

### 技术对话片段 30 (原帖: 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【学习笔记】Gold普遍有权限的Operator 4_29518553347991.md
- **时间**: 1年前

**提问/主帖背景 (FD69320)**:
## 31. group_rank

***功能说明：*** 将股票按指定的分组方式(如行业、子行业等)进行分组，然后在每个组内对股票基于输入值进行排序，返回一个在 0.0 到 1.0 之间均匀分布的数值。这个操作符可以帮助减少异常值和回撤，同时降低相关性。

***参数说明*** ：

- - x: 需要排序的数值
- - group: 分组依据（如行业、子行业等）

***计算过程：***

```
科技行业:  苹果(AAPL):    volume = 85M  微软(MSFT):    volume = 45M  谷歌(GOOGL):   volume = 25M  英特尔(INTC):  volume = 65M  英伟达(NVDA):  volume = 95M金融行业:  摩根大通(JPM):   volume = 15M  高盛(GS):       volume = 8M  美国银行(BAC):   volume = 22M  花旗集团(C):     volume = 18M  富国银行(WFC):   volume = 12M零售行业:  亚马逊(AMZN):    volume = 42M  沃尔玛(WMT):     volume = 28M  塔吉特(TGT):     volume = 15M  好市多(COST):    volume = 35M
```

***使用group_rank后的结果***

```
科技行业: (5只股票，排名间隔为0.25)  英伟达(NVDA):   95M -> 1.00  (第5名)  苹果(AAPL):     85M -> 0.75  (第4名)  英特尔(INTC):   65M -> 0.50  (第3名)  微软(MSFT):     45M -> 0.25  (第2名)  谷歌(GOOGL):    25M -> 0.00  (第1名)金融行业: (5只股票，排名间隔为0.25)  美国银行(BAC):   22M -> 1.00  (第5名)  花旗集团(C):     18M -> 0.75  (第4名)  摩根大通(JPM):   15M -> 0.50  (第3名)  富国银行(WFC):   12M -> 0.25  (第2名)  高盛(GS):        8M -> 0.00   (第1名)零售行业: (4只股票，排名间隔为0.33)  亚马逊(AMZN):    42M -> 1.00  (第4名)  好市多(COST):    35M -> 0.67  (第3名)  沃尔玛(WMT):     28M -> 0.33  (第2名)  塔吉特(TGT):     15M -> 0.00  (第1名)
```

***使用示例***

```
# 示例1：在行业内对成交量进行排名，找出成交量排名靠前的股票alpha = group_rank(volume, industry)high_volume_stocks = alpha > 0.8  # 选择行业内成交量排名前20%的股票# 示例2：结合其他指标使用# 在行业内同时考虑成交量和价格动量alpha = 0.5 * group_rank(volume, industry) + 0.5 * group_rank(returns_5d, industry)
```

## 32. ts_delta

***功能说明**  **：*** ts_delta 计算当前值与 d 天前的值之差。这是一个用于计算变化量的时间序列操作符。

***参数说明：***

- - x: 输入的时间序列数据
- - d: 回溯的天数

***使用示例：***

```
# 示例1: 计算股票价格的5日变化price_change_5d = ts_delta(close, 5)  # 当前收盘价与5天前收盘价之差# 示例2: 计算成交量的日变化volume_change_1d = ts_delta(volume, 1)  # 今日成交量与昨日成交量之差
```

## 33. ts_arg_min

***功能说明：*** 返回过去 d 天内最小值在时间序列中的相对位置（相对于当前日期的偏移量）。如果当前日期的值是最小值，返回0；如果前一天的值是最小值，返回1；以此类推。

***参数说明：***

- - x: 输入的时间序列数据
- - d: 回溯的天数（lookback period）

***计算过程：***

```
# 假设过去6天的数据是 [6,2,8,5,9,4]，其中第一个元素是今天的值x = [6,2,8,5,9,4]  # 从左到右：今天，昨天，前天...d = 6result = ts_arg_min(x, d)  # 返回 1，因为最小值2出现在昨天（偏移量为1）
```

***使用示例：***

```
# 判断股票是否处于20天低点is_recent_low = ts_arg_min(close, 20) == 0# 如果最低点出现在较远的过去，可能表示上升趋势uptrend = ts_arg_min(close, 10) > 5# 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)# 结合最高点和最低点的位置来判断趋势trend = ts_arg_max(close, 20) - ts_arg_min(close, 20)
```

## 34. ts_mean

***功能说明：***  计算过去 d 天的平均值。它是一个时间序列操作符，用于计算移动平均。

***参数说明：***

- - x: 输入的时间序列数据
- - d: 回溯的天数（lookback period）

***使用示例：***

```
# 判断多空趋势is_uptrend = close > ts_mean(close, 20)  # 价格在20日均线之上# 计算价格相对均线的偏离程度price_momentum = close / ts_mean(close, 10) - 1# 短期均线穿越长期均线golden_cross = ts_mean(close, 5) > ts_mean(close, 20)# 计算价格对均值的偏离volatility = close - ts_mean(close, 10)
```

## 35. ts_backfill

***功能说明*** ：用于填充缺失值（NaN）的时间序列操作符。它会用历史数据中最近的有效值来替换当前的 NaN 值。

***参数说明：***

- - x: 输入的时间序列数据
- - lookback: 回溯的天数（默认为d）
- - k: 选择第k个非NaN值（默认为1，即最近的有效值）
- - ignore: 指定要忽略的值（默认为"NAN"）

***计算过程：***

```
# 假设某股票最近6天的数据如下：Day 0 (今天):   NaNDay -1 (昨天):  NaNDay -2:         95Day -3:         NaNDay -4:         90Day -5:         85
```

***k=2时，使用ts_backfill的结果***

```
result = ts_backfill(x, lookback=6, k=2)# 结果：Day 0:          90     # 用第二个有效值90填充Day -1:         90     # 用第二个有效值90填充Day -2:         95     # 原始值保持不变Day -3:         85     # 用第二个有效值85填充Day -4:         90     # 原始值保持不变Day -5:         85     # 原始值保持不变
```

***使用示例***

```
# 股票停牌期间用最近的交易价格填充clean_price = ts_backfill(close, 252)# 财务数据发布间隔期间用最新的数据填充clean_profit = ts_backfill(net_profit, 252)
```

## 36. greater_than_equal

***功能说明：*** 相当于>=, 是一个逻辑比较操作符，用于比较两个输入值。如果第一个输入大于或等于第二个输入，返回 true (1)；否则返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 37. less_than_equal

***功能说明：*** 相当于<=, 是一个逻辑比较操作符，用于比较两个输入值。如果第一个输入小于或等于第二个输入，返回 true (1)；否则返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 38. not_equal

***功能说明：*** 相当于!=, 是一个逻辑比较操作符，用于比较两个输入值是否不相等。如果两个输入值不相等，返回 true (1)；如果相等，返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 39. equal

***功能说明：*** 相当于 \==, 是一个逻辑比较操作符，用于比较两个输入值是否相等。如果两个输入值相等，返回 true (1)；如果相等，返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 40. greater

***功能说明：*** 相当于 >, 是一个逻辑比较操作符，用于比较两个输入值。如果第一个输入严格大于第二个输入，返回 true (1)；否则返回 false (0)。

***参数说明：***

- - x: 第一个输入值
- - y: 第二个输入值

## 41. is_nan

***功能说明：*** 是一个逻辑判断操作符，用于检测输入值是否为 NaN (Not a Number)。如果输入是 NaN，返回 1 (true)；如果输入不是 NaN，返回 0 (false)。

***参数说明：***

- - x: 输入值，可以是任何数值类型

## 42. densify

***功能说明：*** 用于将具有多个桶(buckets)的分组字段转换为更少的可用桶，以提高分组字段的计算效率。它会将稀疏的分组值映射到一个连续的、密集的索引范围内。

***参数说明：***

- - x: 输入的分组字段，通常是整数值

***计算过程***

```
# 原始分组值：industry_codes = {0, 1, 2, 99}  # 4个唯一值，但占用了100个可能的桶# densify 后：dense_codes = {0, 1, 2, 3}     # 4个连续的桶
```

## 43. power

***功能说明：*** 是一个算术操作符，它计算 x 的 y 次方，但与普通的幂运算不同，它会保留 x 的符号。

***参数说明：***

- - x: 底数
- - y: 指数

## 44. signed_power

***功能说明：*** 它计算 x 的 y 次方，但会保留 x 的原始符号。

***参数说明：***

- - x: 底数
- - y: 指数

***和power的对比***

```
# 对比 power 和 signed_powerx = [3, -9, -2, 4]y = 2  # 指数为2# 普通 power， 可能丢失方向性信息power_result = [9, 81, 4, 16]  # x^2，结果总是非负# signed_power，留方向性信息signed_power_result = [9, -81, -4, 16]  # sign(x) * |x|^2，保留原始符号
```

## 45. inverse和reverse

***功能说明：*** inverse(x) = 1/x; reverse(x) = -x

## 46. add, subtract, multiply和divide

***功能说明：*** add(x, y) = x+y, subtract(x, y) = x-y, multiply(x, y) = x* y; divide(x, y) = x/y

## 47. max和min

***功能说明：***

- - max: 返回所有输入值中的最大值
- - min: 返回所有输入值中的最小值

## 48. or, and 和not

***功能说明：***

- - or: 在任一输入为真或两个输入都为真时返回真，否则返回假。
- - and: 仅当两个操作数都为真时返回真，否则返回假。
- - not: 逻辑取反值。如果 x 为真(1)，返回假(0)；如果输入为假(0)，返回真(1)。

## 49. abs

***功能说明：*** 返回输入值的绝对值。

## 50. sign

***功能说明：*** 返回输入值的符号, 正数返回 1, 负数返回 -1, 零返回 0。

**顾问 JG15244 (Rank 67) 的解答与建议**:
收益良多啊，扫清了很多之前模糊的内容。

有个问题想问一下：

这个为什么可以统计最低点出现的频率

```
# 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)
```


---

### 技术对话片段 31 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/10经过前面几天的折磨和捣鼓，基本上算是搭建了一套适合的自己的搜索、回测、check、提交的全流程，也算是终于有产出了。后续计划：1. 继续优化自己的回测流程。2. 寻找新的模板，魔改论坛中的模板。3. 尝试读论文和研报，集合AI尝试性的创造一些新的模板。


---

### 技术对话片段 32 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/12今天有一件重大的事情，value factory 更新了，这次更新的事24年10、11、12月份的（听各位大佬说的），but我的value factory并没有变化，可能是提交alpha不够多，也可能是质量不太行，大概提交了30左右吧，质量的话从base payment上看，一个alpha的话只有1.4左右，所以质量并不是很高。这次更新有很多大佬都拿到了0.9以上，大于有30多位，！！！还有以为女生大佬竟然拿到了1.0，太强了，期待下一次的更新，这段时间要多交点alpha，希望下次我能提升到0.7左右吧，加油！今天提交了1alpha，还是再试水，拿到了1.51，超过了1.5也就说说明质量还算可以，继续加油，争取明天提交两个。嘿嘿。


---

### 技术对话片段 33 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/14今天参加了顾问小组的第一次课，收获了非常多，见识到了非常多厉害的大佬和新人大佬。总结出了下面几个点：1. 一定要将回测量上去，回测量上去了出货、出好的alpha可能性才会更大。可以看看获奖的人，回测多的人一般都会有几个其它的奖项。所以一定要优化回测的方法，可以使用wqb，或者自己写多线程，其中有一位大佬提到不用多线程也可以，就是不断的发送alpha，达到100个后服务器拒收，就重新存回去，然后每个1秒就重新发一个，这样也可以达到100%的使用效率。非常好的观点。2. 三阶模板的含金量还在上升，但是不能死跑，需要理解三阶模板的意义，然后优化改进一下，这个邮件里有提到一些，也可以加入自己的观点，会有不一样的收获。上面提到也就是我接下来要做的。说说今日提交的alpha和base payment吧，依旧是只提交了1个，但是这次只拿到了1.49，低于了1.5，说明这个alpha很差了，不是基本不赚钱了而是直接赔钱了，但这已经是我当前存货里面最好的了，那么剩下的基本上也不用交了，等把三阶模板优化好再看情况吧。


---

### 技术对话片段 34 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/17坏消息：已经断粮了...尝试了一下会议上提到了交换一阶和二阶，但是跑了一些ASI的字段，效果很差...也尝试了一些老虎哥新出的在EUR的模板，把全部字段跑了一遍，一个出了都没有...为啥呀，为啥老虎哥能出我的就出不了呀，猜测是setting不同，或者有什么其它的优化...再尝试优化一下一二三阶模板吧，按照会议上一位大佬说的，对于时序数据，多套基层时序op，再尝试一下吧...好消息：使用wbq，这几天基本上将回测打满了，大约在2-3w左右，相对比与之前的1w都不到，是跟很大的提升，必须要把回测量上去了，出货的可能性才会更大。


---

### 技术对话片段 35 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/18今天eur更新了一个新的区域top2500，连夜挖了一下，基本上没出货，有些前面表现很好后面之久直接平了，不知道怎么优化，看到的大佬可以给下改进方法，万分感激。一个小发现：genius里面的数据，有的是你提交alpha就直接更新，有的是第二天统计后才更新。今日work：跑了老虎哥之前的双字段回归的模板，USA下跑了两个数据集risk和earning，没出货，但看到之前有老跑了400个字段，出了100alpha，属实震惊了，可能数据集没选对吧，希望大佬给点提示。EUR下跑了老虎哥的新模板，TOP1200和TOP2500都跑完了，TOP1200没出货，TOP2500出了两个，表现一般，还需要优化。今天payment：提交了1个ASI的，pro0.5多，表现一般般，以为收益会高一点点，没想到依旧是1.51，哎库存就剩了一个EUR的了，明天交完又断粮了。


---

### 技术对话片段 36 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/19昨日战绩：提交了一个的EUR TOP2500拿到了 1.76，是迄今为止提交一个alpha拿到过最多的base pay。今日工作：重新优化一二三阶模板，因为看到QQ大佬说，仅跑一二三阶模板，vf就拿到了0.9，（我之前没有将一二三阶跑完，以为烂大街的东西...）现在在优化的基础上完完全全的把所有的数据跑一遍，看看情况。


---

### 技术对话片段 37 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/20今日收入：交了一个EUR-TOP2500的因子，拿到了1.72，感觉还不错，但是fitness和margin都不高，prod0.5左右，拿到1.7感觉是倍数高的原因。今日工作：昨天开始跑的一二三阶-EUR-analyst14，一阶数量并不多，二阶也很少，但是三阶段组合出的因子就非常多了，要跑很久，现在还没有跑完，等跑完统计一下出了多少个可以提交的alpha吧，初步看了一下出货还挺多的。遇到了一个wqb的bug，查询alpha的时候传入东八区的时间会异常，例如“2025-02-10T14:55:12+08:00”，但是传入西五区的时间就不会，“2025-02-19T01:55:12-05:00”，研究后发现，wq平台对于url中的“+”不会正常解析，也就说，如果你直接将拼接好的url发送到wq服务器请求，wq服务器时解析不了其中的“+”，如果你再发送请求前就解析好了，那么是没问题的。该问题已联系wqb的作者，且已进行了修复。


---

### 技术对话片段 38 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/21今日收入：<2，炸了，前两天只交一个可以拿到1.7左右，今天直接交满了四个，直接炸了，这四个的表现和之前的两个差不多，但是前两个是单数据集的，这四个里面三个是三数据集的，一个双数据集的，直接炸了，感觉下次vf更新要暴跌了，可怜，难道说单数据集的alpha要远优于多数据集的吗？还是因为这四个因子表现确实不行呢...今日工作：无新内容，继续跑EUR-TOP2500


---

### 技术对话片段 39 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/22今日收入：依旧是1个EUR-TOP2500的alpha，收入1.52，奇怪提交一个可以拿到1.5，提交四个却连2都拿不了...今日工作：ERU-TOP2500-analyst14已经跑完了，共提交8个alpha。后面先不打算跑ERU-TOP2500地区的了，先跑跑ASI地区的吧，发现ASI的速度是ERU速度的1/3。


---

### 技术对话片段 40 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/23今日收入：1.4，提交的事EUR-TOP2500-analyst14跑出来的最后一个alpha，表现很差...感觉EUR地区的alpha质量普遍不高，是我的问题还是这个地区就是这样。今日工作：ASI - 1 - MINVOL1M-analyst14已经跑了38%了，一阶段到现在为止仅出了一个可提交的alpha，且表现不好，等明天再看看情况吧，ASI跑的巨慢，速度仅有EUR的1/3，出货也不多，堪忧呀，感觉马上就要断粮了。


---

### 技术对话片段 41 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/25今日收入：一个ASI的alpha，收入1.54，表现一般般，没库存了，要断粮咯...今日工作：之前跑的ASI的analyst14不知道因为什么原因中断了，只能重新跑了，重新跑的时候，虽然我使用了random来打乱顺序，但还是出现了大量的重复，所以决定不重新跑了，跑下analyst15试试看。另外，不打算跑第三阶段了，仅跑一二阶段工作量就巨大，270多个字段，一阶段就会出现7万多个alpha，太多了，尤其是ASI跑的还巨慢....


---

### 技术对话片段 42 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/26昨天断粮了，今天交了一个EUR的单因子alpha，相关性很低，只有0.46，指标表现一般，但是突破了我1个alpha的最高收入记录，回测数量也达到了最高，来到了33.6k。今日收入：1个EUR-TOP2500的单因子alpha，0.5vf，1.98$，是我交1个alpha以来拿到的最高记录。今日工作：依旧在跑EUR-TOP2500-anl，数量有点多，感觉要四五天才能跑完。听说eur地区最近会上theme，这应该是加入wq以来第一次碰到theme，不知道具体是个什么情况，期待。


---

### 技术对话片段 43 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/4有段时间没更新日记了，一方面因为断粮，一方面因为最近有点忙。今日收入：4.08，一个EUR的alpha，因为theme的加成，直接来到了4.08，达到了历史新高，舒服了。看了眼日记，发现在theme加成的影响下，很多很多大佬的日收入都达到了80+，太羡慕了，最近马上要更新combine和vf了，但是我交的alpha还是非常少，上次更新的时候vf就没更新依旧是0.5，不知道这次会不会更新，希望能高一点点，上香~今日工作：前段时间发现，使用wqb回测的时候，有时候会莫名其妙中断，且没有回测地址，也看不到是因为什么原因出错中断了，今天把wqb回测方法中的“出错不中断”参数开启了，看看后面还会不会出现同样的问题。


---

### 技术对话片段 44 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/8这次真清楚的感受到单字段因子的厉害了，昨天交了4个单字段的因子，拿了5.7刀，今天交了3个多字段的因子，只拿了2刀，指标表现上看多字段的因子会更好，但是最后的base pay明显的低了很多，看来以后得提交策略要改变一下了，单字段>多字段，没货的情况下，多字段每天只交一个是最优解了。vf 0.5。


---

### 技术对话片段 45 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/12回顾一下这段时间的alpha提交，除了开始时的其它地区提交了几个外，在eur top2500出来后，以及后面eur的theme出来后，提交的全是eur地区，当然这段时间内eur地区确实容易出货，但是只提交一个地区的alpha是不符合alpha分散策略的，主要是alpha的挖掘模板有点问题，当前是按照地区或者说是按照数据集id来进行挖掘的，后面需要优化一下，改进成一次挖掘任务要从多个不同地区的不同数据集中获取字段，进行挖掘，这样大概率会出现多个地区的alpha，加入计划，等这次的vf更新后，好好优化一下代码。


---

### 技术对话片段 46 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/18vf 0.22，提交了3个alpha，base 1.18，看来vf低了，不管提交几个，base都会在很低的小范围内徘徊，像我，vf0.22，基本上就在1.2上下不超0.1徘徊了...昨天完成了多地区的回测，但是库存还有好多个eur的alpha没有提交，今天check一下，看看昨天跑的其它地区有没有产出吧。发现一个问题，一阶段出现的可提交的因子，提交一个后，基本上不会影响其它可提交的因子，或者说相关性增加不大，但是二阶段、三阶段的可提交因子，提交一个后，基本上就会死一大片了，self相关性基本上就来到了0.9左右，（我着重看过，不是相同的字段）这是不是一定程度上说了，二阶段三阶段出的因子其中的字段并不是主信号，而是一个副信号呢...


---

### 技术对话片段 47 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/27vf 0.22 日常坐牢，不管交多少个 base 都超不过 1.2 ...终于解锁 sa 了，听大佬们说 sa 非常有助于提升 vf，看来要好好研究下 sa 的写法了，需要迫切提升 vf 不想再坐牢了刚好收到了 vf 提升计划的邀请，已报名！勿辜负！


---

### 技术对话片段 48 (原帖: 统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print())
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/04/11顾问 顾问 JG15244 (Rank 67) (Rank 67) 的量化日记。-------------------------------------------------vf 又更新了，这次来到了 0.44（12,1,2），还好有提升，之前是 0.22（11,12,1），0.22的时候三个月总共我只提交了30多个alpha，这次0.44总共提交了50个alpha，看来 vf 和数量还是有关系的，3月份提交了大量的eur地区以及部分asi地区的alpha，但是质量非常一般，不知道下次更新到3月份的时候 vf 会不会又跌回去，接下来的时间将重心着重放到 usa 地区吧！今天尝试了一下开启 max 选项，发现跑出来的 alpha 质量非常好，但是出货率确实也比较低。


---

### 技术对话片段 49 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/10

经过前面几天的折磨和捣鼓，基本上算是搭建了一套适合的自己的搜索、回测、check、提交的全流程，也算是终于有产出了。


> [!NOTE] [图片 OCR 识别内容]
> [root@ece-77846 firal
> chire」 # Ppthor
> I_Script
> USEI
> 顾问 顾问 JG15244 (Rank 67) (Rank 67)
> tokerl
> erpir
> 14400.0}
> permissiors
> ["CONSILTAKI
> "IILTI_SIIILSTIOIT
> PROD_SFILS"
> 飚`咫虹
> TIS[i
> IZSTIONJ'
> 'IORIIsr
> aet_fieldids () 方法
> 开始获取数据字段。
> 功获取[34
> 10P3000的
> 197条
> [Sa
> TOP3000
> 868籴
> [3』
> TOP30OOE
> 2538籴
> 取[3乌
> IOP30OO
> 107籴
> TGP300
> TOP3000
> TOP3OO0
> TOP3000
> [S』
> TGP300
> TGP300
> TOP3000
> TOP300C
> TGP300
> TOP3000
> 488
> [S』
> TOP3OO0
> 获取I32
> TOP3OOOE
> 获取[34
> TP3000的
> 488籴
> I6P3000的
> 21蜍
> 苡功获取[3』
> T0P3000的=
> 1?籴
> fieldids
> 方法执行完
> 取数据字段  &454条-
> 在执行proces3_
> datafields
> 预处理数据字段
> PrOcess_datafields
> 方法执-
> 共预处理数据字段  1016? 条
> 正在执行eenerate_expressions_
> T1tli_fields
> ()方法
> 组合生成表二
> Senerate
> epres310IIS_
> Hitll_fields
> ()方法执行完毕
> 共生成  1016?  个表达式
> 初始aecay 追加完成
> deca
> 则池组
> 113
> 回测池
> POoL
> tasl
> Dost
> dole
> Pool
> taak &
> SiIlllate
> dole
> POoL
> task
> Post dole
> POol
> taak &
> SiIlllate
> dole
> SeT



> [!NOTE] [图片 OCR 识别内容]
> 检查10个alpha =
> ZOZITINI,
> ZOZPIi
> 3921183
> 3921230;
> 392LJJe
> 39211
> 3922130
> 392SI0;
> 3929103,
> 392a迟0
> 检查10个alpha
> 392eT
> 392[#环,
> 392L gIe;
> 392u2p0,
> 3924006,
> 392IIa0,
> 3924630,  39247a8,
> 3924Rn,
> 3924112
> 处理upha
> 3921826  时发生错误=
> Eypectirg
> le
> lire
> C0I1III
> char 0〉
> 在进行二
> 重试
> 橙查10 ^
> aIpla
> 3924152,
> 3925
> 2;
> 3923826
> 392H 56
> 392250,
> 39J210e,
> 39J5kS;   39JJIbG
> 39Jkgd0
> 39J42
> 检查
> aLPIal
> [卫0,
> 39J缸叮
> TTT6
> 3901310,
> 39Ob1a2
> 390Eoxe-
> 3908Ro
> 3g0Jdse
> 390k730,
> 3gOLJbe
> 检查10个alpha
> 3gO0GVZ
> 3SOogdz
> 39Ooyl0,
> 3gOdJalT,
> 3gOae
> 3SHJ[4a0;
> 39+48
> 3grnR0,
> 395710,
> 39xep2
> Pha
> 5Q16p5
> 8瓯
> CORRELSTIOI=O. 4977
> FROD_CORRELSTIOI=0
> STAT[8=S[J2C区88
> 检查10-
> aIpla
> 5Ql6p35
> 5lr匹
> SQIbkaJ
> 501
> 50119J6
> 501136
> 5l19u
> SQLogo,
> SQlrglk
> SQlrlzz
> 检查10-
> aIpla
> SQIrgl5,
> 501j66
> 5022801
> 502281[,
> SO2gL4r;
> SQ2alzk;
> 5023021,
> 50253112,
> 5Q2b5,
> 502471
> 检查10 -
> aIpla
> 50211}
> 502k琏二
> 5020672
> SQ2OBT6
> SQ2PPi」
> SQ2Q2R1
> SQ2RoTo
> 50239趾
> SQ2ur1
> SQ270
> E查10个
> Pha
> SQaglgk
> 5049245,
> SQalloall
> SQdri86
> SOARRP 二
> SQdrOk5
> 5Qai75
> SQdgB[
> 50do1  ;
> SQdarNT
> Ipha Gr25x
> 3E
> CORREI
> IOI=D. 5022
> 'ROD_CORREL
> Ol=0
> 66GG
> STeT[J8=3[22E38
> 检查10-
> Pha
> SQax2k
> QT2r65
> SQTSreJ
> 5Qi5q1
> Br2ladp
> Br21a6
> Gr22}
> Gr25x8J, 6r2787,
> 6r280哑
> IIpla
> Gr2Bn
> SELE
> CORRELSTIOI=O. 5466
> PROD_CORRELATIOIT0. 6889
> STeT[J8=3[22E38
> Ilpha
> Gr2Lw2
> SELE
> RURREL
> STIOIJ=0. 5283
> PRUD
> CORRELSTIOI=O. 6794;
> STAT[8=S[J2C区88
> 检查
> aIpla
> Gr2gdrg
> Gr2Bn
> Gr2aBp
> Gr2B?AJ
> Gr2jdap
> Gr2JB
> Gr2kiGL
> Gr2LPar
> Gr2Li
> fr2lL
> 检查10个alpha
> Gr2O5F
> Gr2aGng
> Gr2dZ2G
> Gr2wr l
> 6r221R
> GrLlai
> GrL?aoL,
> GrLeBIP
> GrLa367,
> GrLOIIS
> 检查10个alpha
> GrLgf 证
> GrLHa0,
> GrLTRSp
> GrLzf} E
> Grl2noE
> GrlIZaLT
> Grl62虹
> GrlTTLJLE
> Brl8SE
> GrlloP0


后续计划：

1. 继续优化自己的回测流程。

2. 寻找新的模板，魔改论坛中的模板。

3. 尝试读论文和研报，集合AI尝试性的创造一些新的模板。


---

### 技术对话片段 50 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/12

今天有一件重大的事情，value factory 更新了，这次更新的事24年10、11、12月份的（听各位大佬说的），but我的value factory并没有变化，可能是提交alpha不够多，也可能是质量不太行，大概提交了30左右吧，质量的话从base payment上看，一个alpha的话只有1.4左右，所以质量并不是很高。

这次更新有很多大佬都拿到了0.9以上，大于有30多位，！！！还有以为女生大佬竟然拿到了1.0，太强了，期待下一次的更新，这段时间要多交点alpha，希望下次我能提升到0.7左右吧，加油！

今天提交了1alpha，还是再试水，拿到了1.51，超过了1.5也就说说明质量还算可以，继续加油，争取明天提交两个。嘿嘿。


---

### 技术对话片段 51 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/14

今天参加了顾问小组的第一次课，收获了非常多，见识到了非常多厉害的大佬和新人大佬。

总结出了下面几个点：

1. 一定要将回测量上去，回测量上去了出货、出好的alpha可能性才会更大。可以看看获奖的人，回测多的人一般都会有几个其它的奖项。所以一定要优化回测的方法，可以使用wqb，或者自己写多线程，其中有一位大佬提到不用多线程也可以，就是不断的发送alpha，达到100个后服务器拒收，就重新存回去，然后每个1秒就重新发一个，这样也可以达到100%的使用效率。非常好的观点。

2. 三阶模板的含金量还在上升，但是不能死跑，需要理解三阶模板的意义，然后优化改进一下，这个邮件里有提到一些，也可以加入自己的观点，会有不一样的收获。

上面提到也就是我接下来要做的。

说说今日提交的alpha和base payment吧，依旧是只提交了1个，但是这次只拿到了1.49，低于了1.5，说明这个alpha很差了，不是基本不赚钱了而是直接赔钱了，但这已经是我当前存货里面最好的了，那么剩下的基本上也不用交了，等把三阶模板优化好再看情况吧。


---

### 技术对话片段 52 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/17

坏消息：

已经断粮了...

尝试了一下会议上提到了交换一阶和二阶，但是跑了一些ASI的字段，效果很差...

也尝试了一些老虎哥新出的在EUR的模板，把全部字段跑了一遍，一个出了都没有...为啥呀，为啥老虎哥能出我的就出不了呀，猜测是setting不同，或者有什么其它的优化...

再尝试优化一下一二三阶模板吧，按照会议上一位大佬说的，对于时序数据，多套基层时序op，再尝试一下吧...

好消息：

使用wbq，这几天基本上将回测打满了，大约在2-3w左右，相对比与之前的1w都不到，是跟很大的提升，必须要把回测量上去了，出货的可能性才会更大。


---

### 技术对话片段 53 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/18

今天eur更新了一个新的区域top2500，连夜挖了一下，基本上没出货，有些前面表现很好后面之久直接平了，不知道怎么优化，看到的大佬可以给下改进方法，万分感激。


> [!NOTE] [图片 OCR 识别内容]
> 1ON
> 12/06/2017
> TralnDnL  9,412.84
> 8OOOK
> OOOK
> 40OOK
> 20OOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


一个小发现：genius里面的数据，有的是你提交alpha就直接更新，有的是第二天统计后才更新。

今日work：

跑了老虎哥之前的双字段回归的模板，USA下跑了两个数据集risk和earning，没出货，但看到之前有老跑了400个字段，出了100alpha，属实震惊了，可能数据集没选对吧，希望大佬给点提示。

EUR下跑了老虎哥的新模板，TOP1200和TOP2500都跑完了，TOP1200没出货，TOP2500出了两个，表现一般，还需要优化。

今天payment：

提交了1个ASI的，pro0.5多，表现一般般，以为收益会高一点点，没想到依旧是1.51，哎库存就剩了一个EUR的了，明天交完又断粮了。


---

### 技术对话片段 54 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/19

昨日战绩：

提交了一个的EUR TOP2500拿到了 1.76，是迄今为止提交一个alpha拿到过最多的base pay。


> [!NOTE] [图片 OCR 识别内容]
> Single Data Set Alpha
> Pyramid theme: EURIDIIANALYST X1.6
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> 1.97
> 11.719
> 1.10
> 3.8796
> 3.369
> 6.609600


今日工作：

重新优化一二三阶模板，因为看到QQ大佬说，仅跑一二三阶模板，vf就拿到了0.9，（我之前没有将一二三阶跑完，以为烂大街的东西...）现在在优化的基础上完完全全的把所有的数据跑一遍，看看情况。


---

### 技术对话片段 55 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/20

今日收入：

交了一个EUR-TOP2500的因子，拿到了1.72，感觉还不错，但是fitness和margin都不高，prod0.5左右，拿到1.7感觉是倍数高的原因。

今日工作：

昨天开始跑的一二三阶-EUR-analyst14，一阶数量并不多，二阶也很少，但是三阶段组合出的因子就非常多了，要跑很久，现在还没有跑完，等跑完统计一下出了多少个可以提交的alpha吧，初步看了一下出货还挺多的。

遇到了一个wqb的bug，查询alpha的时候传入东八区的时间会异常，例如“2025-02-10T14:55:12+08:00”，但是传入西五区的时间就不会，“2025-02-19T01:55:12-05:00”，研究后发现，wq平台对于url中的“+”不会正常解析，也就说，如果你直接将拼接好的url发送到wq服务器请求，wq服务器时解析不了其中的“+”，如果你再发送请求前就解析好了，那么是没问题的。该问题已联系wqb的作者，且已进行了修复。


> [!NOTE] [图片 OCR 识别内容]
> apiworldquantbrain com/users/selflalphas?dateCreatedy= 2025-02-10114:55:12-08:008dateCreated <2025-02-19122:35:05-08:008drder=dateCr.
> 压 V %
> @
> 8 |
> 器
> 臼 JBINFO
> 技术文档
> 臼 AII具
> 口 魔法梯子
> 口 智慧工地
> 口学
> 口 工具
> 口  论文
> 口 游戏
> 口  运营一体化
> 臼
> worldquant
> 口 gulimall
> 够 Refer a friend
> 2025年假调休安排。
> FeHelper
> 排序:
> 默认
> 升序O
> 降序0
> 乱码修正
> 元数据
> 折叠所有
> 下载JSON
> {高级定制
> 隐藏
> COUT
> 10000
> next
> "htln;LLani
> JLLgqynzbsa迎卫
> Com:443LusersLselflalphas?dateCreated咝3C2025-02-19122934355
> 0-0833
> 0adateCreatedm3e=2025-02-1011493455亟3412-0843400Liit=lloffset=lRordersdatecreated
> Drevious
> IUIII
> reSuIts



> [!NOTE] [图片 OCR 识别内容]
> 畎11325
> 已发布0.2.5,修复了刚才的问题
> 现在用+时区没问
> 题了
> 谢谢大佬



---

### 技术对话片段 56 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/21

今日收入：

<2，炸了，前两天只交一个可以拿到1.7左右，今天直接交满了四个，直接炸了，这四个的表现和之前的两个差不多，但是前两个是单数据集的，这四个里面三个是三数据集的，一个双数据集的，直接炸了，感觉下次vf更新要暴跌了，可怜，难道说单数据集的alpha要远优于多数据集的吗？还是因为这四个因子表现确实不行呢...

今日工作：

无新内容，继续跑EUR-TOP2500


---

### 技术对话片段 57 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/22

今日收入：

依旧是1个EUR-TOP2500的alpha，收入1.52，奇怪提交一个可以拿到1.5，提交四个却连2都拿不了...

今日工作：

ERU-TOP2500-analyst14已经跑完了，共提交8个alpha。

后面先不打算跑ERU-TOP2500地区的了，先跑跑ASI地区的吧，发现ASI的速度是ERU速度的1/3。


---

### 技术对话片段 58 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/23

今日收入：

1.4，提交的事EUR-TOP2500-analyst14跑出来的最后一个alpha，表现很差...

感觉EUR地区的alpha质量普遍不高，是我的问题还是这个地区就是这样。

今日工作：

ASI - 1 - MINVOL1M-analyst14已经跑了38%了，一阶段到现在为止仅出了一个可提交的alpha，且表现不好，等明天再看看情况吧，ASI跑的巨慢，速度仅有EUR的1/3，出货也不多，堪忧呀，感觉马上就要断粮了。


---

### 技术对话片段 59 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/25

今日收入：

一个ASI的alpha，收入1.54，表现一般般，没库存了，要断粮咯...

今日工作：

之前跑的ASI的analyst14不知道因为什么原因中断了，只能重新跑了，重新跑的时候，虽然我使用了random来打乱顺序，但还是出现了大量的重复，所以决定不重新跑了，跑下analyst15试试看。

另外，不打算跑第三阶段了，仅跑一二阶段工作量就巨大，270多个字段，一阶段就会出现7万多个alpha，太多了，尤其是ASI跑的还巨慢....


---

### 技术对话片段 60 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/2/26

昨天断粮了，今天交了一个EUR的单因子alpha，相关性很低，只有0.46，指标表现一般，但是突破了我1个alpha的最高收入记录，回测数量也达到了最高，来到了33.6k。

今日收入：

1个EUR-TOP2500的单因子alpha，0.5vf，1.98$，是我交1个alpha以来拿到的最高记录。

今日工作：

依旧在跑EUR-TOP2500-anl，数量有点多，感觉要四五天才能跑完。

听说eur地区最近会上theme，这应该是加入wq以来第一次碰到theme，不知道具体是个什么情况，期待。


---

### 技术对话片段 61 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/4

有段时间没更新日记了，一方面因为断粮，一方面因为最近有点忙。

今日收入：

4.08，一个EUR的alpha，因为theme的加成，直接来到了4.08，达到了历史新高，舒服了。

看了眼日记，发现在theme加成的影响下，很多很多大佬的日收入都达到了80+，太羡慕了，最近马上要更新combine和vf了，但是我交的alpha还是非常少，上次更新的时候vf就没更新依旧是0.5，不知道这次会不会更新，希望能高一点点，上香~

今日工作：

前段时间发现，使用wqb回测的时候，有时候会莫名其妙中断，且没有回测地址，也看不到是因为什么原因出错中断了，今天把wqb回测方法中的“出错不中断”参数开启了，看看后面还会不会出现同样的问题。


---

### 技术对话片段 62 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/8

这次真清楚的感受到单字段因子的厉害了，昨天交了4个单字段的因子，拿了5.7刀，今天交了3个多字段的因子，只拿了2刀，指标表现上看多字段的因子会更好，但是最后的base pay明显的低了很多，看来以后得提交策略要改变一下了，单字段>多字段，没货的情况下，多字段每天只交一个是最优解了。

vf 0.5。


---

### 技术对话片段 63 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/12

回顾一下这段时间的alpha提交，除了开始时的其它地区提交了几个外，在eur top2500出来后，以及后面eur的theme出来后，提交的全是eur地区，当然这段时间内eur地区确实容易出货，但是只提交一个地区的alpha是不符合alpha分散策略的，主要是alpha的挖掘模板有点问题，当前是按照地区或者说是按照数据集id来进行挖掘的，后面需要优化一下，改进成一次挖掘任务要从多个不同地区的不同数据集中获取字段，进行挖掘，这样大概率会出现多个地区的alpha，加入计划，等这次的vf更新后，好好优化一下代码。


---

### 技术对话片段 64 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/18

vf 0.22，提交了3个alpha，base 1.18，看来vf低了，不管提交几个，base都会在很低的小范围内徘徊，像我，vf0.22，基本上就在1.2上下不超0.1徘徊了...

昨天完成了多地区的回测，但是库存还有好多个eur的alpha没有提交，今天check一下，看看昨天跑的其它地区有没有产出吧。

发现一个问题，一阶段出现的可提交的因子，提交一个后，基本上不会影响其它可提交的因子，或者说相关性增加不大，但是二阶段、三阶段的可提交因子，提交一个后，基本上就会死一大片了，self相关性基本上就来到了0.9左右，（我着重看过，不是相同的字段）这是不是一定程度上说了，二阶段三阶段出的因子其中的字段并不是主信号，而是一个副信号呢...


---

### 技术对话片段 65 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/3/27

vf 0.22 日常坐牢，不管交多少个 base 都超不过 1.2 ...

终于解锁 sa 了，听大佬们说 sa 非常有助于提升 vf，看来要好好研究下 sa 的写法了，需要迫切提升 vf 不想再坐牢了

刚好收到了 vf 提升计划的邀请，已报名！勿辜负！


---

### 技术对话片段 66 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/04/11

顾问 顾问 JG15244 (Rank 67) (Rank 67) 的量化日记。

-------------------------------------------------

vf 又更新了，这次来到了 0.44（12,1,2），还好有提升，之前是 0.22（11,12,1），0.22的时候三个月总共我只提交了30多个alpha，这次0.44总共提交了50个alpha，看来 vf 和数量还是有关系的，3月份提交了大量的eur地区以及部分asi地区的alpha，但是质量非常一般，不知道下次更新到3月份的时候 vf 会不会又跌回去，接下来的时间将重心着重放到 usa 地区吧！

今天尝试了一下开启 max 选项，发现跑出来的 alpha 质量非常好，但是出货率确实也比较低。


---

### 技术对话片段 67 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 11个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年7月17日

断了，呜呜呜，这个赛季本来想拿满一个每天都提交的成就的，可惜今天工作太多了，没来得及提交，随便选了一个可以submit的，可惜corr没过.......

唉，以后要前一天的晚上提交好，这样第二天的白天才会有更多的时间来选择好的提交！

好在最近也是把regular、super的全套流程+数据库的方式都跑通了。

最近新出的app还没研究，后面要找时间慢慢研究一下，感觉会有非常大的提升。

=======================================================================
问题的答案不在脑子里，只有行动才能找到答案。 ---埃克哈特·托利-
=======================================================================


---

### 技术对话片段 68 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 11个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年7月21日

最近又更新了一次vf，距离上次更新仅仅20天。

这次的更新来到了 0.96，比之上次降低了 0.01，这次更新的时间范围 3、4、5，ppa的打击还没有完全到来，但是从第一次更新 ppa的comb来看（0.89），vf 距离暴跌也差不多了，还有sac的打击也没有到来...

这次国区vf 0.9 以上的足足有90多位，真的是蒸蒸日上了！国区牛逼！

最近虽然吧regular、super 的回测框架都搭建好了，但是regular基本上还是不出货呀，偶尔的ppa质量也堪忧，根本不敢交，super组别人的因子上双5其实还比较容易（可能都是过拟合，hhhh），但是组自己的话上双5就比较困难了。这配额是真难搞哇。

最近抽点时间研究一下使用lab来看数据的分布，然后借助app来分析。


---

### 技术对话片段 69 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 11个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年7月28号

ra和ppa的出货基本无了，感觉方法错了。。。

sa正常提交，后面如果vf降低的话就尽量的提交own的sa，一方面自己提交ra都是经过了自己的质量把控，质量相对来说比较好一点，同时也可以增加not(own)的配额，等vf升高的时候，就可以猛猛赚钱了，嘿嘿。

7月份马上就要结束了，接下来重新改变一下策略，同时预留出一部分槽位专门留给lab+app的测试，定向暴破pyr，希望能够有所收获吧。

=======================================================================
教育就是一棵树摇动另一棵树，一朵云推动另一朵云，一个灵魂唤醒另一个灵魂。 ---雅斯贝尔斯-
=======================================================================


---

### 技术对话片段 70 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月4日

最近开始跑 amr 地区了，跑的速度是真快啊，感觉如果 all in 跑的话，每天破 5 万不是问题。

跑了一些也发现了一些问题，amr 的很多alpha 的 sharpe 都低，之前跑四大区的时候，fitness 和 sharpe 几乎相同，即使不同也不会差很多，但是 amr 有的 fitness 很高，但是 sharpe 就过不了标准了，好在最近小地区也开放了 ppa 的提交规则。

还有一个很奇怪的现象，最开始是开启了 maxtrade 选项的，但是后面微调的时候，关掉回测了一下，发现结果直接是相反的...，暂不清楚是个例还是什么情况，现在已经新增一批关闭 maxtrade 选项，等回测后看一下情况。

还有最近平台提交是真的慢....

另外最近开始很多新人为了点塔，都开始做 d0 区域的了，不知道这是好事还是坏事，等后面更新 combine 和 value factory后看看吧。


---

### 技术对话片段 71 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月9日

今天ra新高了，50多刀，这是高vf后第一次这么高的收益。

今天提交了一个usa、3个amr的ppa。给了50.03刀。

然后sa是提交了一个3个5的not own，只给36.14刀。sa给的很低了，按道理说这种纸面数据的sa，在我这个vf下，怎么着也得给40刀+了，之前确实也会给到40刀+，但是最近有几个的数据跟之前一致，但是给的就在36、37刀附近了，感觉是os爆炸了...

另外虽然交了小地区给的钱比较多，但是小地区确实是不稳定，尽量还是挑好的交，不然到时候vf就爆炸了。

=======================================================================
卧看满天云不动，不知云与我俱东。 ---陈与义-
=======================================================================


---

### 技术对话片段 72 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月11日

今天收入再破新高，来到了97.06。

今日提交情况是4个amr的ppa，1个not own的sa。

ra给了58.34。今天提交的全是atom的alpha，乘数都在1.8、1.7，结合昨天的情况可以看出来，其实并不是小地区给的钱多，只是小地区的乘数高而已，如果乘数不高即使是小地区也不会给多少钱。

sa今天跟之前一样，看来又是os炸了，3个5的super alpha按理说可以拿到40+的，但是只给了38左右....

今天听大佬们谈论起来，突然发现，其实这个阶段是不应该跑小地区的，也不应该交小地区，因为小地区部稳定，不仅会搞崩vf，也会搞崩comb，而comb崩了的话，那么genius等级基本上就追不上去了...

但是反过来说，因为上次vf更新时0.97，这次来到了0.96，而且comb有降低，所以如果下次vf更新低了的话，也拿不到钱了，感觉分成了genius派和vf派了，一个拿季度奖，一个拿basepayment....但也不排除有真大佬两者都兼顾...

算了不想那么多了，amr交都交了，那就交到底吧，尽量多交点稳定一点，后面也交几个amr的sa，来稳定一下，只有这个办法了。

global的比赛开了，今天刚改好代码框架，感觉得2-3天后才能出货，等等看吧。


---

### 技术对话片段 73 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月12日

今天收入回归正常，62.54。

今天的提交情况是3个amr的ppa，一个own的sa。

先说ra，ppa的限额终于来了，非 atom 的ppa每日只能提交一个了，感觉大大降低了靠ppa来刷pyr的情况。

今天之所以提交了3个ra，是因为时间来不及了，导致最后一个没提交上去....

3个ra给了46.97，感觉还不错，跟前几天相比的话属于正常水平。

今天是一个own的sa，可惜prodcorr没有在0.5以下，不过出乎意料的是竟然给了15多，这个真出乎意料了，之前只会给9左右，可能这个os比较好吧，哈哈哈哈哈。

另外，不知道为什么昨天把usa的槽位给了glb后，amr的回测竟然莫名其妙停掉了，停了半天才发现，啊啊啊啊，看来又没有机会竞争双周会的奖了。

再说下glb的出货情况，昨天到今天一个没出，我跑的topdiv3000这个池子，看大佬们都在跑min那个池子，等我这个再跑个两天看看情况，如果还是不出货的话，我也换到min池子看看。

再就是global的比赛，好像大多数大佬都不太想参与，怕搞崩掉genius，不够我倒是还挺想参与一下，可惜不出货....真的是旱的旱死，涝的涝死。


---

### 技术对话片段 74 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月13日

今日收益又高回去了...有点离谱，今天只提交了一个sa、两个ra，竟然给了92.49美金。

前两天以为ra的收益主要受theme的乘数控制，今天仔细回顾了一下之前提交的pc的值，发现ra的收益受pc控制也挺高的，但是谁的权重更多，这个倒是还不清楚。

说下今天的提交情况：

一个 not own 的 asi 的 super alpha，pc在0.49多，给了41.15，相比之前提交的算比较好的了，但是8月份asi的ra几乎没有提交，后面需要补一下asi的ra和eur的ra了，amr的sa还没有跑出3个5的，还需要再等等看。

ra是提交了两个amr的ppa，给了51.34，这个算比较多的了，毕竟只提交了2个，之前都是4个或者3个，今天提交两个后，其实为了避免ppa的额度超了，本来也打算之后每天也就只提交1个或者2个，现在看来没什么问题。

再说下gla的回测情况，回测速度依旧很慢，依旧是不出货，我跑的事topdiv3000，明天看一下会不会出货，不出的话，先把universe换一下试试看，如果这周剩下的时间依旧不出的话，就暂时放弃glb了，先去跑跑asi和eur了。

另外我目前是直接回测二阶的alpha，发现有点问题，其实应该是先回测一阶，然后选取有信号的进行二阶回测，但是目前的框架，不是很方便的把一阶回测的取出来，回测框架后面还需要再优化一下，这个暂时是想放到下个月或者下个赛季了...最近都没有时间大改。


---

### 技术对话片段 75 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月14日

今日收益63.19美金，正常水平。

今日提交情况，2个ppa的amr，一个own的sa。

2个ppa的amr，收入和昨天基本相同，49.53美金，新出的ppa的规则是，小地区有限额的10个，只有当这个ppa不属于ra，也部署atom的时候，才会占用10的名额。

一个not own的sa，今天sa的prodcorr没有小于0.5，所以只给了13.66美金，正常水平了。

再说下glb的出货情况，topdiv3000依旧是一个没出，转战MINVOL1M了，如果再不出的话，就先放弃了，先去泡eur和usa了，asi先不跑了，asi最近好像要出新的theme了，等出了再跑asi。

感觉要稍微转变一下跑glb的策略了，先在其他区域跑某个数据集，如果出货了再去glb上跑，这样glb出货的概率可能会大些，不然glb跑的实在是太慢太难出货了。


---

### 技术对话片段 76 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月15日

今天收益只有40.62美金了，降低了很多，一度让我以为vf更新了...

今天提交情况，依旧是2个amr的ppa，一个sa。

ra一共给了30.8美金，并不是很多，提交的质量不是很高，但是今天点亮了2个amr的pyr，还是不错的。

sa提交的是一个not own的双8，但是prod>0.5的，只给了9美金，比较少了，昨天提交的own还不如今天提交的呢，都给了13美金，有点奇怪。

最近sa一直没有跑出prod小于0.5的，之前的存货也都交光了，后面sa很难再拿到高收益了。

最近想要重新优化一下回测框架，现在是只回测2阶段的，但是需要回测很多的alpha，这是一个大问题，后面要优化成，先跑一阶，然后选取好的再跑二阶段。

glb今晚看一下，如果还是不出货的话，就停了，改去跑eur了，赶在asi的them出来之前跑一些，然后再跑asi。

mcp最近又更新了，感觉已经跟不上了...好着急好着急。


---

### 技术对话片段 77 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月16日

今日收入48.64美金，处于正常水平。

今天提交了1个glb的比赛因子，2个amr的ppa，ra一共是给了27.96美金，是最近这段时间里最低的一次了，glb的因子pc是0.9，乘数是1.4，amr的与之前相同，看来pc的高的惩罚还是很高啊，而且混交的话好像确实会有影响。

sa提交的是一个not own的eur的pc0.61的，按照之前的算，一般会在9-12美金左右，但是今天给了20.68美金，实属震惊我了，不知道为什么会突然这么高，难道真是os很好吗？（这个就不可知了）

glb换了min后，出货还可以，既然提交了glb的alpha，那么就跑下去吧，尽量多交一点，不过这个月eur的ra估计就没时间交了，后面要去跑asi，不够eur交了不少sa，应该不会炸吧。

回测框架也再优化了，最后还是打算改成1阶回测，2阶优化，现在每批回测完后，将回调得到url保存下来，然后定时取给alpha打上name，然后二阶优化的时候，根据name来取出来，进入二阶，预计下周搞定。

明天有课，是将mcp的，期待一下，感觉mcp用好了的话，绝对是一大助力！


---

### 技术对话片段 78 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月17日

今日收入40.13美金，处于较低水平。

今天提交的是1个ra，一个sa。

ra是一个glb的比赛因子，给了3.84美金，质量一般，pc很高，pc达到了0.9，高pc的惩罚确实很严重，今天没有提交继续amr的因子。

sa提交的是一个not own的asi的，fitness>5，pc<0.5但是sharpe是4.89，给了36.29美金，看来想要拿高收益，sharpe和fitness都要>5才可以。

今天vf1.0的大佬又拿到了100美金+，羡慕了，祈祷自己的vf下次更新不会炸掉吧。

最近找到了一个好的筛选相关性的方法，还在处于实验阶段，希望能够有效。

mcp的课记错了，是下周，狠狠期待一下。


---

### 技术对话片段 79 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025年8月19日

vf的更新结果出来了，0.96->0.92，这个变化其实是可以接受的，已经有预感vf会下降了....

今日收益83.47美金，ra收益54.15美金，sa收益29.32美金。

今天总的收益虽然很高，但是主要是因为ra拉上去的，只看sa的话，29是完全不够看的。

说下今天提交情况3个amr的ppa，都是高乘数、低pc，给了54.15，这个其实比较满足的，毕竟现在vf只有0.92了。还是那句话，乘数和pc对base影响比重非常大，交满的影响其实不是特别大。

sa的提交情况是一个not own的amr的35，但是只给了29,，这有点疑惑，因为昨天的sa是一个own的amr的35，却给了40+，不是昨天的太好了，就是今天的sa炸了...

再吐槽一下lab真难用啊，没有terminal，只能用notebook跑，但是关闭了Brian lab后，notebook就不跑了...

感觉严重影响进度了，已经卡了好几天了...

有没有大佬给我支点招啊。


---

### 技术对话片段 80 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2026-01-21

今天挑挑拣拣交了一个ind的not own的sa，发现出了os后not own的sa后期的走向直接平了....之前表现很好的sa，现在都不敢交了，但是not own的sa却很少出现这个问题，难道是外面的ra质量真的太差了吗...

更新os后，之前的存货都没了，还要再重新回测一遍咯。

今天还交了一个比赛的glb 的alpha，表现一般，但是可以点塔也就交上去了。

==============================越努力，越幸运==============================


---

### 技术对话片段 81 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2026/1/22

提交情况：

PPA：1个

区域：GLB

Sharpe1.11  Turnover  9.75%  Fitness  0.52  Returns  2.72%  Drawdown  4.74%  Margin  5.59‱

SA：1个

区域：ASI

Sharpe  4.15  Turnover  14.70%  Fitness  3.42  Returns  9.99%  Drawdown  1.59%  Margin  13.58‱

=====================================================================

成全我的不是生活，而是我自己的选择。 ---卡尔·荣格-

=====================================================================


---

### 技术对话片段 82 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录2026/01/26
提交情况:
[PPA,RA]: 1个
区域:[GLB]
Sharpe 1.17 Turnover 4.05% Fitness 0.68 Returns 4.26% Drawdown 8.22% Margin 21.02‱ 
[SA]: 1个
Sharpe 3.16 Turnover 12.40% Fitness 3.21 Returns 12.90% Drawdown 2.55% Margin 20.81‱ 
====================================
“成功的关键在于相信自己有成功的能力。”——拿破仑·希尔
====================================


---

### 技术对话片段 83 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录 2026/01/27
提交情况:
[PPA]: 1 个
区域:[GLB]
Sharpe 1.06 Turnover 5.03% Fitness 0.58 Returns 3.80% Drawdown 9.85% Margin 15.10‱
[SA]: 1 个
区域:[IND]
Sharpe 5.40 Turnover 14.98% Fitness 6.39 Returns 20.98% Drawdown 2.35% Margin 28.02‱
=====================================================================
“最困难之时，就是离成功不远之日。”—— 拿破仑
=====================================================================


---

### 技术对话片段 84 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录2026/01/28
提交情况:
[PPA]: 1个
区域:[GLB]
Sharpe 1.11 Turnover 31.90% Fitness 0.72 Returns 13.47% Drawdown 35.81% Margin 8.44‱ 
[SA]: 1个
区域:[IND]
Sharpe 3.15 Turnover 11.70% Fitness 3.06 Returns 11.76% Drawdown 2.71% Margin 20.10‱ 
=====================================================================
“人生在勤，不索何获。”——张衡
=====================================================================


---

### 技术对话片段 85 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录2026/01/29
提交情况:
[PPA,RA]: 0个
区域:[GLB,USA,EUR,IND]
Sharpe 无 Turnover 无 Fitness 无 Returns 无 Drawdown 无 Margin 无 
[SA]: 1个
区域:[IND]
Sharpe 6.39 Turnover 17.80% Fitness 8.21 Returns 29.38% Drawdown 2.69% Margin 33.01‱ 
=====================================================================
“志不强者智不达，言不信者行不果。”——墨子
=====================================================================


---

### 技术对话片段 86 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录2026/02/01
提交情况:
[PPA,RA]: 1个
区域:[GLB]
Sharpe 1.33 Turnover 17.93% Fitness 1.09 Returns 12.06% Drawdown 15.28% Margin 13.45‱ 
[SA]: 1个
区域:[IND]
Sharpe 7.15 Turnover 8.96% Fitness 13.16 Returns 42.33% Drawdown 3.51% Margin 94.45‱ 
=====================================================================
“卓越的人一大优点是：在不利与艰难的遭遇里百折不挠。”——贝多芬
=====================================================================


---

### 技术对话片段 87 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录2026/01/30
提交情况:
[PPA,RA]: 0个
区域:[GLB,USA,EUR,IND]
Sharpe 无 Turnover 无 Fitness 无 Returns 无 Drawdown 无 Margin 无 
[SA]: 1个
区域:[IND]
Sharpe 5.58 Turnover 11.74% Fitness 8.24 Returns 27.27% Drawdown 2.47% Margin 46.43‱ 
=====================================================================
“生活就像海洋，只有意志坚强的人，才能到达彼岸。”——马克思
=====================================================================


---

### 技术对话片段 88 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
每日记录2026/01/31
提交情况:
[PPA,RA]: 1个
区域:[IND]
Sharpe 1.87 Turnover 8.25% Fitness 1.64 Returns 9.59% Drawdown 6.47% Margin 23.26‱ 
[SA]: 1个
区域:[IND]
Sharpe 3.61 Turnover 14.38% Fitness 3.05 Returns 10.28% Drawdown 2.07% Margin 14.30‱ 
=====================================================================
“古之立大志者，不惟有超世之才，亦必有坚韧不拔之志。”——苏轼
=====================================================================


---

### 技术对话片段 89 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/04

量化日记竟然出第二季了，不得不说第一季的效果太好了，从日记中了解了很多大佬的工作，学到了太多东西了。

最近有点糟心，买的服务器一直因为磁盘IO超限从而宕机，好几天了，已经在想办法解决了，最近几天都没有提交ra，希望能尽快搞定服务器的事，太影响效率了。

sa的比赛开始，我是g2，simple真是天崩开局，大力出奇迹直接选了1000个，fitness直接干到13多了，分数也到了34w多，但是衰减特别明显，os爆炸。

不知道sa的比赛，对于我这种不同sa也没做过sa的小白来说，究竟是好事还是坏事，希望不要把vf搞炸了。

说下今天收益：

vf 0.88

sa 9.66$


---

### 技术对话片段 90 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/04

Super Alpha Competition 第二天，依旧g2 simple继续坐牢。

有几点疑惑：

1. simple 不是已经提纯后的主信号吗，按道理说已经排除了混信号、过拟合的等不好的alpha，但是看select出来的alpha的指标都比较差，且租出来的super alpha衰减也很厉害，尤其是最后两三年，感觉很明显的过拟合导致，不清楚是simple本身就是这样的还是我个人的select和combo有问题呢？

2. 现在有一个很害怕的地方，我之前没有提交过super alpha，且已知super alpha对value factory的影响比重较大，而且现在提交的simple组出来的alpha质量较差，会不会直接把value factory搞炸掉？

3. 基于第二点，对于g2组的人来说，是不是可直接放弃simple的super alpha，做剩下的5个类别，去和做6个类别的super alpha博弈，但是比赛提供的分数计算规则中没有找到最后计算分数的时候，每个类别对分数的影响，是等权还是求和？（但是我已经交了两个simple的super alpha了，已经停不下来了...）

隐约感觉super alpha competition是一个双刃剑了...

今日收益：

1sa  9.55$


---

### 技术对话片段 91 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/06

1. 终于把服务器因为数据量太多导致宕机的问题解决掉了，开始正常回测了。

2. 基本上每天都在手搓super alpha，质量一般且效率很低，在simple下基本上都是大力飞砖，select 数量直接拉满，后面还是要把super alpha的代码补充完善一下。

3. 优化了check脚本，使用直接调用官方的check方法，不需要传入description，check结果也会返回self corr、prod corr、ppac corr，只要regular和ppac满足一个提交就会返回success，然后将结果保存到数据库中，在根据具体的corr值进行筛选，如果都满足的话就可以一鱼两吃咯（不清楚一鱼两吃是否有严重后果影响）。

4. 借助xx课代表的自动提交代码，今天第一次实现了一鱼两吃，开心。

今日收入：

value factory：0.88

2 regular alpha：4.91$

1 super alpha：9.43$


---

### 技术对话片段 92 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/16

今天终于达成master了，alpha的数量和pyr都够了，后面还会更新一次comb，希望不要把我的master梦打碎了。

今日提交情况：

regular：eur - ram - ppa -> 7.34$

super：eur -> 9.24$

=======================================================================
一切幸福都并非没有烦恼，而一切逆境也绝非没有希望。 ---弗朗西斯·培根-
=======================================================================


---

### 技术对话片段 93 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/17

今天小红书有好几个人咨询wq兼职的事情，但是介绍之后就没有后续，不知道是话术的问题还是怎么回事，至今没有成功转化一个。

今日提交情况：

regular：eur - ram - ppa -> 6.81$

super：eur -> 9.08$

=======================================================================
保持渴望，保持同他人的联结，在平凡的日常中寻找自己感兴趣的事，留意别人忽视的东西。​​​ ---罗伯·沃克-
=======================================================================


---

### 技术对话片段 94 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/20

最近工作有点忙就没有交regular alpha，只交了一个super alpha。

今日提交情况：

super：asi -> 9.06$

=======================================================================

我现在正年轻，我愿意自己的青春在一种激荡的生活中度过；我愿意过一种充满创造乐趣、更为纯洁的生活。 ​​​ ---路遥-

=======================================================================


---

### 技术对话片段 95 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/06/22

今天没来得及交super alpha，只交了一个非theme的regular alpha。

我也有weight了，0.01，听老师说多交usa地区的alpha，weight增长才会比较快，但是usa地区的我交的真不多，且按照课代表的理论，你提交的因子，至少要有os后才会有可能被pm选择进入实盘，看了一下我的usa地区有os的alpha，寥寥几个，但质量好像都不错，os的fitness都可以2.多，这几个因子还是从alpha模板大师中魔改出来，看来前辈们的智慧还是非常有用的，后面也要多从模板中魔改一下，刚好最近想新增一个alpha模拟的数据库表，更方便了。

今日提交情况：

regular：asi -> 2.18$（非theme）

=======================================================================

我们的焦虑不是来自于对未来的思考，而是来自于想要控制它。 ---纪伯伦-

=======================================================================


---

### 技术对话片段 96 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025-10-13

量化日记第五季都来了，时间好快啊，来wq都1年了。

q3季度已经定级结束了，最后还是保住了master，这个赛季要争取一下gm，也想去gm的山顶看看风景，这个赛季要多点塔，将任务重心放到点塔上面，comb已经很长时间没有掉下2了，感觉保持正常的提交质量，comb应该不会有太大的波动了。

近期平台一直在引导用户一段时间着重做一个区域的alpha，甚至是某几个dataset、某几个

neutralization的alpha，最近也是一直跟着平台的方向走，出什么theme就去做什么theme，嘿嘿，虽然吃到theme了，但是base并没有太大的波动，应该是因为fitness和prodcorr不够的原因。

最近有个想法，目前一直都是在做region下最大的universe，是不是也应该做一下其他的universe呢，目前想到的方法和roubtstest差不多，将可以提交的alpha遍历一下universe，不够这样好像是存在过拟合的风险，所以目前是将接近满足提交条件的alpha更换universe后重新回测，然后再选取可以提交的，一定程度上可以降低过拟合的风险。


---

### 技术对话片段 97 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/12/23

惊到了，第八季日记才开1天，就已经480条评论了。

说下近期情况吧，近期都是每天只提交一个sa，ra很少提交了，上周不小心收到了pc的警告邮件，这周就只交了1个ra。最近在跑ind，开了maxtrade真的好难出货哇，不开又担心质量不好，难搞哦。

没想到这次比赛的daliy竟然是日更的，看起来想每日的盈亏了，降低的回测算力都扔这上面了。

昨天晚上刚完成了分数的分配，今天还没有更新出分数，等等明天吧，希望明天可以更新出分数。

============================================================


---

### 技术对话片段 98 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JG15244 (Rank 67) 的解答与建议**:
2025/12/24

放弃ind了，重新回到glb，争取年前多交点glb的alpha。

今天提交了一个sa+一个ra，sa是eur的，sa的bug终于修复了，ra交的事glb的。

今晚有gem的会，积极参与！！！！！！！！！！！

============================================================

每个故事必须按照自己的方式、自己的时间节奏缓缓展开。 ---谢丽尔·桑德伯格-

============================================================


---

### 技术对话片段 99 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 减少无效回测经验分享.md
- **时间**: 7个月前

**提问/主帖背景 (FH33043)**:
减少无效回测主要三个方向，一个是经济学含义约束，这个方向我还在摸索，第二个是先大规模发散踩点，看哪里有信号，然后朝着有信号的方向收敛，目前这个方法冷神点60的塔的那篇论坛有涉及，目前我主要还是靠人工发散收敛，自动化工程量较大，还没开始搞。第三个是减少无效字段和操作符的等价与相似减少无效和等价回测，这篇文章主要讲第三种方向，另外两个方向等我摸索清楚了再发些帖子。

## ***1. 无效字段***

有些数据集除了universe的范围不一样，其他都是等价的，比如这些

duplicate_mapping = {

'model230': ['fundamental65'],

'fundamental85': ['model55'],

'fundamental86': ['model56'],

'fundamental87': ['news88'],

'fundamental89': ['other395'],

'fundamental90': ['other401'],

'fundamental91': ['other416'],

'fundamental92': ['other427'],

'fundamental93': ['other452'],

'fundamental94': ['other466'],

'model261': ['other407'],

'analyst92': ['other411'],

'analyst94': ['other423'],

'sentiment33': ['other429'],

'model262': ['other432'],

'model263': ['other434'],

'risk88': ['other450'],

'model264': ['other460'],

'model266': ['other486'],

'model267': ['other510'],

'news104': ['other7'],

'model243': ['other72'],

'other732': ['model159'],

'other733': ['risk69'],

'other734': ['sentiment16'],

'model244': ['other83'],

'earnings14': ['other84'],

'sentiment31': ['other94'],

'news102': ['model210'],

'analyst82': ['model211'],

'model232': ['institutions8'],

'model237': ['risk82'],

'model238': ['shortinterest6'],

'model239': ['shortinterest7'],

'model240': ['other33'],

'model246': ['other131'],

'model248': ['other137'],

'model250': ['other176'],

'model252': ['other193'],

'model253': ['other238'],

'model257': ['other351'],

'model259': ['other378'],

'model260': ['other380'],

'model242': ['other54'],

'analyst81': ['model52'],

'socialmedia39': ['other100'],

'earnings11': ['news77'],

'analyst83': ['news87'],

'macro52': ['other15'],

'institutions25': ['other515'],

'macro55': ['other246'],

'analyst93': ['other419'],

'analyst84': ['sentiment12'],

'shortinterest55': ['other534'],

'analyst87': ['other1'],

'sentiment32': ['other111'],

'shortinterest54': ['other148'],

'macro56': ['other305'],

'model241': ['other41'],

'model265': ['other461'],

'macro53': ['other97']

}

目前冒号右边的universe范围普遍比左边大，我只查了几个，都是这样。

有些datafield我直接拉入黑名单，以下都是IQC期间整理的，在USA都能复现，正式顾问类似的无效字段更多。分成4类。

第一类是完全无法回测的datafield，包括以下这5个

```
pv13_percentregionpv13_regionpv13_reportperiodendpv13_reportperiodlenpv13_reporttype
```

这些alphaCount也都是0, 回测到一半会提示 "Your simulation probably took too much resource.", 然后就没结果了。

第二类是跑is_nan(datafield)和1结果完全一样的alpha，应该有其他用法，比如

```
fnd6_newqv1300_spcedqfnd6_newqv1300_spcedpqfnd6_newqv1300_spceepsp12
```

第三类是单独跑datafield结果PNL全0，比如

```
fnd6_ocaxsfnd6_pncdqfnd6_pncepsq
```

第四类是datafield1和datafield2跑完结果几乎完全一样，且跑datafield1 - datafield2收益全0，应该是datafield1和datafield2几乎完全一样，比如

```
(anl4_capex_mean,est_capex)(fnd6_cptnewqv1300_dlttq,debt_lt)(fnd6_cptnewqv1300_actq,assets_curr)
```

## ***2. 操作符的等价与相似***

有些op满足交换律, 比如add、multiply、min、max、and、or和group_cartesian_product等显示成立的，还有

ts_corr(x, y, d) = ts_corr(y, x, d)

ts_covariance(x, y, d) = ts_covariance(y, x, d)

值得一提的是

ts_corr(x, y, d) ≈ -ts_corr(-x, y, d)

ts_covariance(x, y, d) = -ts_covariance(-x, y, d)

有些满足交换后转负, 比如subtract(x, y) = -subtract(y, x)，类似的关系还有

ts_regression(y, x, d, lag = 0, rettype = 6) = -ts_regression(x, y, d, lag = 0, rettype = 6)

我注意到有些vector_neut(x, y) ≈ -vector_neut(y, x)，成立条件和严谨性有待研究。

由于我目前是gold，我所有满足交换律的Regular操作符就这些，其他的都是不满足的，满足交换律的操作符都可以省去一半回测。

还有些操作符跑相同的参数相关性有0.7左右，比如ts_corr和ts_covariance，vector_neut和regression_neut等，这一块也有待研究，如果op1和op2在任意条件跑相同的参数互相关都>0.9，那么op1的表现不好op2就不用跑了，相反如果op1的表现很好那么最好把op2也跑一遍。

关于一阶剪枝，除了过滤掉拉黑的datafield，打乱datafield后，不打乱一阶公式，比如ts_sum(x, 5), ts_sum(x, 22), ts_sum(x, 66)呈现越来越差的趋势，我就直接跳过ts_sum(x, 120)和ts_sum(x, 240)等。我还统计了一阶有信号的所有operator出现频率，有些operator没出现过几次，我直接删了.

二阶剪枝先用自相关剪枝，然后根据回测结果和表达式的相关性范围直接跳过不想要的，比如group_zscore(first_order, market)和first_order的相关性一般>0.99，如果first_order不好，直接跳过group_zscore(first_order, market)，通常会有一组alpha内的互相关>0.95，其中一个不好直接淘汰一组。

**顾问 JG15244 (Rank 67) 的解答与建议**:
不错的分享，在进行回测之前对数据进行清理，这是一个非常正常的方向，感觉可以进行共建，制定一个共同认可的规则“何为无效数据”、“何为低/中/高质量数据”，将数据集分给不同的顾问进行回测，（当然不同genius等级的顾问可能会有不同的数据权限等其他问题，如果可以的话这些可以再详细讨论一下）然后共建出一个通用的数据集信息。


---

### 技术对话片段 100 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 减少无效回测经验分享_36248601073175.md
- **时间**: 7个月前

**提问/主帖背景 (FH33043)**:
减少无效回测主要三个方向，一个是经济学含义约束，这个方向我还在摸索，第二个是先大规模发散踩点，看哪里有信号，然后朝着有信号的方向收敛，目前这个方法冷神点60的塔的那篇论坛有涉及，目前我主要还是靠人工发散收敛，自动化工程量较大，还没开始搞。第三个是减少无效字段和操作符的等价与相似减少无效和等价回测，这篇文章主要讲第三种方向，另外两个方向等我摸索清楚了再发些帖子。

## ***1. 无效字段***

有些数据集除了universe的范围不一样，其他都是等价的，比如这些

duplicate_mapping = {

'model230': ['fundamental65'],

'fundamental85': ['model55'],

'fundamental86': ['model56'],

'fundamental87': ['news88'],

'fundamental89': ['other395'],

'fundamental90': ['other401'],

'fundamental91': ['other416'],

'fundamental92': ['other427'],

'fundamental93': ['other452'],

'fundamental94': ['other466'],

'model261': ['other407'],

'analyst92': ['other411'],

'analyst94': ['other423'],

'sentiment33': ['other429'],

'model262': ['other432'],

'model263': ['other434'],

'risk88': ['other450'],

'model264': ['other460'],

'model266': ['other486'],

'model267': ['other510'],

'news104': ['other7'],

'model243': ['other72'],

'other732': ['model159'],

'other733': ['risk69'],

'other734': ['sentiment16'],

'model244': ['other83'],

'earnings14': ['other84'],

'sentiment31': ['other94'],

'news102': ['model210'],

'analyst82': ['model211'],

'model232': ['institutions8'],

'model237': ['risk82'],

'model238': ['shortinterest6'],

'model239': ['shortinterest7'],

'model240': ['other33'],

'model246': ['other131'],

'model248': ['other137'],

'model250': ['other176'],

'model252': ['other193'],

'model253': ['other238'],

'model257': ['other351'],

'model259': ['other378'],

'model260': ['other380'],

'model242': ['other54'],

'analyst81': ['model52'],

'socialmedia39': ['other100'],

'earnings11': ['news77'],

'analyst83': ['news87'],

'macro52': ['other15'],

'institutions25': ['other515'],

'macro55': ['other246'],

'analyst93': ['other419'],

'analyst84': ['sentiment12'],

'shortinterest55': ['other534'],

'analyst87': ['other1'],

'sentiment32': ['other111'],

'shortinterest54': ['other148'],

'macro56': ['other305'],

'model241': ['other41'],

'model265': ['other461'],

'macro53': ['other97']

}

目前冒号右边的universe范围普遍比左边大，我只查了几个，都是这样。

有些datafield我直接拉入黑名单，以下都是IQC期间整理的，在USA都能复现，正式顾问类似的无效字段更多。分成4类。

第一类是完全无法回测的datafield，包括以下这5个

```
pv13_percentregionpv13_regionpv13_reportperiodendpv13_reportperiodlenpv13_reporttype
```

这些alphaCount也都是0, 回测到一半会提示 "Your simulation probably took too much resource.", 然后就没结果了。

第二类是跑is_nan(datafield)和1结果完全一样的alpha，应该有其他用法，比如

```
fnd6_newqv1300_spcedqfnd6_newqv1300_spcedpqfnd6_newqv1300_spceepsp12
```

第三类是单独跑datafield结果PNL全0，比如

```
fnd6_ocaxsfnd6_pncdqfnd6_pncepsq
```

第四类是datafield1和datafield2跑完结果几乎完全一样，且跑datafield1 - datafield2收益全0，应该是datafield1和datafield2几乎完全一样，比如

```
(anl4_capex_mean,est_capex)(fnd6_cptnewqv1300_dlttq,debt_lt)(fnd6_cptnewqv1300_actq,assets_curr)
```

## ***2. 操作符的等价与相似***

有些op满足交换律, 比如add、multiply、min、max、and、or和group_cartesian_product等显示成立的，还有

ts_corr(x, y, d) = ts_corr(y, x, d)

ts_covariance(x, y, d) = ts_covariance(y, x, d)

值得一提的是

ts_corr(x, y, d) ≈ -ts_corr(-x, y, d)

ts_covariance(x, y, d) = -ts_covariance(-x, y, d)

有些满足交换后转负, 比如subtract(x, y) = -subtract(y, x)，类似的关系还有

ts_regression(y, x, d, lag = 0, rettype = 6) = -ts_regression(x, y, d, lag = 0, rettype = 6)

我注意到有些vector_neut(x, y) ≈ -vector_neut(y, x)，成立条件和严谨性有待研究。

由于我目前是gold，我所有满足交换律的Regular操作符就这些，其他的都是不满足的，满足交换律的操作符都可以省去一半回测。

还有些操作符跑相同的参数相关性有0.7左右，比如ts_corr和ts_covariance，vector_neut和regression_neut等，这一块也有待研究，如果op1和op2在任意条件跑相同的参数互相关都>0.9，那么op1的表现不好op2就不用跑了，相反如果op1的表现很好那么最好把op2也跑一遍。

关于一阶剪枝，除了过滤掉拉黑的datafield，打乱datafield后，不打乱一阶公式，比如ts_sum(x, 5), ts_sum(x, 22), ts_sum(x, 66)呈现越来越差的趋势，我就直接跳过ts_sum(x, 120)和ts_sum(x, 240)等。我还统计了一阶有信号的所有operator出现频率，有些operator没出现过几次，我直接删了.

二阶剪枝先用自相关剪枝，然后根据回测结果和表达式的相关性范围直接跳过不想要的，比如group_zscore(first_order, market)和first_order的相关性一般>0.99，如果first_order不好，直接跳过group_zscore(first_order, market)，通常会有一组alpha内的互相关>0.95，其中一个不好直接淘汰一组。

**顾问 JG15244 (Rank 67) 的解答与建议**:
不错的分享，在进行回测之前对数据进行清理，这是一个非常正常的方向，感觉可以进行共建，制定一个共同认可的规则“何为无效数据”、“何为低/中/高质量数据”，将数据集分给不同的顾问进行回测，（当然不同genius等级的顾问可能会有不同的数据权限等其他问题，如果可以的话这些可以再详细讨论一下）然后共建出一个通用的数据集信息。


---

### 技术对话片段 101 (原帖: 登录系统s = login()获取数据字段df = get_datafields(s, dataset_id='analyst4', region='USA', universe='TOP3000', delay=1)数据预处理pc_fields = process_datafields(df))
- **原帖链接**: [Commented] 多阶任务拆分与MySQL管理经验分享代码优化.md
- **时间**: 1年前

**提问/主帖背景 (DZ11181)**:
## 前言

作为一名刚接触Alpha因子开发的新人，我最初面对复杂的因子生成流程时感到非常困惑。通过实践，我总结出一套将整个流程拆分为多阶子任务并通过MySQL管理任务状态的方法，大大提高了开发效率。下面我将分享这一经验，希望对其他新人有所帮助。

## 一、整体架构设计

我们将Alpha因子开发流程划分为三个主要阶段：

1. 1 **一阶任务** ：基础因子生成
2. 2 **二阶任务** ：基于一阶结果的增强因子
3. 3 **三阶任务** ：加入交易信号的最终因子

每个阶段的任务信息都存储在MySQL中，包含以下关键字段：

- `task_id` ：唯一标识
- `type` ：任务类型(1/2/3)
- `status` ：任务状态(0=待运行,1=运行中,2=已完成)
- `expression` ：因子表达式
- `decay` ：衰减参数
- `create_time` ：创建时间
- `update_time` ：更新时间

## 二、MySQL表结构设计

```
CREATE TABLE alpha_tasks (    id INT AUTO_INCREMENT PRIMARY KEY,    task_type TINYINT NOT NULL COMMENT '1=一阶,2=二阶,3=三阶',    status TINYINT DEFAULT 0 COMMENT '0=待运行,1=运行中,2=已完成',    expression TEXT NOT NULL COMMENT '因子表达式',    decay INT DEFAULT 6 COMMENT '初始decay值',    sharpe_ratio FLOAT COMMENT '夏普比率',    fitness FLOAT COMMENT '适应度',    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,    INDEX idx_type_status (task_type, status)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 三、一阶任务生成与处理

### 1. 数据准备与登录

```
# 登录系统s = login()# 获取数据字段df = get_datafields(s, dataset_id='analyst4', region='USA', universe='TOP3000', delay=1)# 数据预处理pc_fields = process_datafields(df)
```

### 2. 生成一阶任务并存入MySQL

```
def generate_first_order_tasks(pc_fields, ts_ops):    # 生成一阶表达式    first_order = first_order_factory(pc_fields, ts_ops)        # 连接数据库    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 批量插入一阶任务    sql = "INSERT INTO alpha_tasks (task_type, status, expression, decay) VALUES (%s, %s, %s, %s)"    batch_data = [(1, 0, expr, 6) for expr in first_order]        try:        cursor.executemany(sql, batch_data)        conn.commit()        logging.info(f"成功插入{cursor.rowcount}条一阶任务")    except Exception as e:        conn.rollback()        logging.error(f"插入一阶任务失败: {e}")    finally:        cursor.close()        conn.close()
```

### 3. 从MySQL加载任务并运行回测

```
def run_first_order_simulation(batch_size=100):    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 获取待运行的一阶任务    cursor.execute("SELECT id, expression, decay FROM alpha_tasks WHERE task_type=1 AND status=0 LIMIT %s", (batch_size,))    tasks = cursor.fetchall()        if not tasks:        logging.info("没有待运行的一阶任务")        return        # 更新任务状态为运行中    task_ids = [task[0] for task in tasks]    cursor.execute(f"UPDATE alpha_tasks SET status=1 WHERE id IN ({','.join(['%s']*len(task_ids))})", task_ids)    conn.commit()        # 准备回测数据    fo_alpha_list = [(expr, decay) for _, expr, decay in tasks]    fo_pools = load_task_pool(fo_alpha_list, 10, 10)        # 运行回测    results = multi_simulate(fo_pools, "SUBINDUSTRY", "USA", "TOP3000", 0)        # 更新任务状态和结果    update_task_results(task_ids, results)        cursor.close()    conn.close()
```

## 四、二阶任务生成与处理

### 1. 从一阶结果筛选优质因子

```
def get_promising_first_order(min_sharpe=1.2, min_fitness=0.7):    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 获取表现良好的一阶因子    cursor.execute("""        SELECT id, expression, decay FROM alpha_tasks         WHERE task_type=1 AND status=2         AND sharpe_ratio >= %s AND fitness >= %s        ORDER BY sharpe_ratio DESC LIMIT 100    """, (min_sharpe, min_fitness))        promising_tasks = cursor.fetchall()    cursor.close()    conn.close()        return promising_tasks
```

### 2. 生成二阶任务

```
def generate_second_order_tasks():    # 获取优质一阶因子    fo_tasks = get_promising_first_order()        if not fo_tasks:        logging.warning("没有符合条件的一阶因子用于生成二阶任务")        return        # 剪枝处理    fo_layer = prune(fo_tasks, 'anl4', 5)        # 生成二阶表达式    so_alpha_list = []    group_ops = ["group_neutralize", "group_rank", "group_zscore"]        for expr, decay in fo_layer:        for alpha in get_group_second_order_factory([expr], group_ops, "USA"):            so_alpha_list.append((alpha, decay))        # 随机打乱    random.shuffle(so_alpha_list)        # 存入数据库    save_tasks_to_db(so_alpha_list, task_type=2)
```

## 五、三阶任务生成与处理

### 1. 从二阶结果筛选优质因子

```
def get_promising_second_order(min_sharpe=1.3, min_fitness=0.8):    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        cursor.execute("""        SELECT id, expression, decay FROM alpha_tasks         WHERE task_type=2 AND status=2         AND sharpe_ratio >= %s AND fitness >= %s        ORDER BY sharpe_ratio DESC LIMIT 200    """, (min_sharpe, min_fitness))        promising_tasks = cursor.fetchall()    cursor.close()    conn.close()        return promising_tasks
```

### 2. 生成三阶任务

```
def generate_third_order_tasks():    # 获取优质二阶因子    so_tasks = get_promising_second_order()        if not so_tasks:        logging.warning("没有符合条件的二阶因子用于生成三阶任务")        return        # 剪枝处理    so_layer = prune(so_tasks, 'anl4', 5)        # 生成三阶表达式    th_alpha_list = []        for expr, decay in so_layer:        for alpha in trade_when_factory("trade_when", expr, "USA"):            th_alpha_list.append((alpha, decay))        # 随机打乱    random.shuffle(th_alpha_list)        # 存入数据库    save_tasks_to_db(th_alpha_list, task_type=3)        logging.info(f"生成三阶表达式数量: {len(th_alpha_list)}")
```

## 六、任务调度与管理

### 1. 任务状态监控

```
def monitor_tasks():    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 获取各类型任务状态统计    cursor.execute("""        SELECT task_type, status, COUNT(*) as count         FROM alpha_tasks         GROUP BY task_type, status        ORDER BY task_type, status    """)        stats = cursor.fetchall()        logging.info("任务状态统计:")    for task_type, status, count in stats:        type_desc = {1: "一阶", 2: "二阶", 3: "三阶"}.get(task_type, "未知")        status_desc = {0: "待运行", 1: "运行中", 2: "已完成"}.get(status, "未知")        logging.info(f"{type_desc}任务-{status_desc}: {count}个")        cursor.close()    conn.close()
```

### 2. 自动调度运行

```
def auto_schedule():    # 检查并运行一阶任务    if has_pending_tasks(1):        run_first_order_simulation()        # 检查并生成二阶任务    if should_generate_second_order():        generate_second_order_tasks()        # 检查并运行二阶任务    if has_pending_tasks(2):        run_second_order_simulation()        # 检查并生成三阶任务    if should_generate_third_order():        generate_third_order_tasks()        # 检查并运行三阶任务    if has_pending_tasks(3):        run_third_order_simulation()
```

## 七、经验总结

1. 1 **模块化设计** ：将复杂的Alpha生成流程拆分为清晰的三个阶段，每个阶段职责单一
2. 2 **状态管理** ：通过MySQL记录任务状态，便于监控和恢复
3. 3 **批量处理** ：合理设置批量大小，平衡资源利用率和系统负载
4. 4 **错误处理** ：完善的异常捕获和重试机制，确保任务连续性
5. 5 **性能监控** ：定期检查任务执行情况，及时发现并解决问题

通过这套方法，我成功地将原本复杂混乱的Alpha开发流程变得清晰可控，大大提高了开发效率和因子质量。虽然代码还有很多需要完善的地方，但希望这些经验能帮助其他新人更快上手Alpha因子开发工作。

**顾问 JG15244 (Rank 67) 的解答与建议**:
大佬这套流程下来每天的回测量在多少左右呢？

我也曾想过将一阶二阶的表达式存入数据库中，然后回测的时候从数据库中取出来，但是从数据库中取数这一过程随着数据量的增加，时间也会变长。看您上面的代码里的流程中从数据库中取出表达式后，回测完成后会再更新这一批数据，这里又增加了时间的损耗，个人感觉效率上会有所影响。可以分享下每天的回测量嘛。


---

### 技术对话片段 102 (原帖: 登录系统s = login()获取数据字段df = get_datafields(s, dataset_id='analyst4', region='USA', universe='TOP3000', delay=1)数据预处理pc_fields = process_datafields(df))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 多阶任务拆分与MySQL管理经验分享代码优化_32603028529175.md
- **时间**: 1年前

**提问/主帖背景 (DZ11181)**:
## 前言

作为一名刚接触Alpha因子开发的新人，我最初面对复杂的因子生成流程时感到非常困惑。通过实践，我总结出一套将整个流程拆分为多阶子任务并通过MySQL管理任务状态的方法，大大提高了开发效率。下面我将分享这一经验，希望对其他新人有所帮助。

## 一、整体架构设计

我们将Alpha因子开发流程划分为三个主要阶段：

1. 1 **一阶任务** ：基础因子生成
2. 2 **二阶任务** ：基于一阶结果的增强因子
3. 3 **三阶任务** ：加入交易信号的最终因子

每个阶段的任务信息都存储在MySQL中，包含以下关键字段：

- `task_id` ：唯一标识
- `type` ：任务类型(1/2/3)
- `status` ：任务状态(0=待运行,1=运行中,2=已完成)
- `expression` ：因子表达式
- `decay` ：衰减参数
- `create_time` ：创建时间
- `update_time` ：更新时间

## 二、MySQL表结构设计

```
CREATE TABLE alpha_tasks (    id INT AUTO_INCREMENT PRIMARY KEY,    task_type TINYINT NOT NULL COMMENT '1=一阶,2=二阶,3=三阶',    status TINYINT DEFAULT 0 COMMENT '0=待运行,1=运行中,2=已完成',    expression TEXT NOT NULL COMMENT '因子表达式',    decay INT DEFAULT 6 COMMENT '初始decay值',    sharpe_ratio FLOAT COMMENT '夏普比率',    fitness FLOAT COMMENT '适应度',    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,    INDEX idx_type_status (task_type, status)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 三、一阶任务生成与处理

### 1. 数据准备与登录

```
# 登录系统s = login()# 获取数据字段df = get_datafields(s, dataset_id='analyst4', region='USA', universe='TOP3000', delay=1)# 数据预处理pc_fields = process_datafields(df)
```

### 2. 生成一阶任务并存入MySQL

```
def generate_first_order_tasks(pc_fields, ts_ops):    # 生成一阶表达式    first_order = first_order_factory(pc_fields, ts_ops)        # 连接数据库    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 批量插入一阶任务    sql = "INSERT INTO alpha_tasks (task_type, status, expression, decay) VALUES (%s, %s, %s, %s)"    batch_data = [(1, 0, expr, 6) for expr in first_order]        try:        cursor.executemany(sql, batch_data)        conn.commit()        logging.info(f"成功插入{cursor.rowcount}条一阶任务")    except Exception as e:        conn.rollback()        logging.error(f"插入一阶任务失败: {e}")    finally:        cursor.close()        conn.close()
```

### 3. 从MySQL加载任务并运行回测

```
def run_first_order_simulation(batch_size=100):    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 获取待运行的一阶任务    cursor.execute("SELECT id, expression, decay FROM alpha_tasks WHERE task_type=1 AND status=0 LIMIT %s", (batch_size,))    tasks = cursor.fetchall()        if not tasks:        logging.info("没有待运行的一阶任务")        return        # 更新任务状态为运行中    task_ids = [task[0] for task in tasks]    cursor.execute(f"UPDATE alpha_tasks SET status=1 WHERE id IN ({','.join(['%s']*len(task_ids))})", task_ids)    conn.commit()        # 准备回测数据    fo_alpha_list = [(expr, decay) for _, expr, decay in tasks]    fo_pools = load_task_pool(fo_alpha_list, 10, 10)        # 运行回测    results = multi_simulate(fo_pools, "SUBINDUSTRY", "USA", "TOP3000", 0)        # 更新任务状态和结果    update_task_results(task_ids, results)        cursor.close()    conn.close()
```

## 四、二阶任务生成与处理

### 1. 从一阶结果筛选优质因子

```
def get_promising_first_order(min_sharpe=1.2, min_fitness=0.7):    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 获取表现良好的一阶因子    cursor.execute("""        SELECT id, expression, decay FROM alpha_tasks         WHERE task_type=1 AND status=2         AND sharpe_ratio >= %s AND fitness >= %s        ORDER BY sharpe_ratio DESC LIMIT 100    """, (min_sharpe, min_fitness))        promising_tasks = cursor.fetchall()    cursor.close()    conn.close()        return promising_tasks
```

### 2. 生成二阶任务

```
def generate_second_order_tasks():    # 获取优质一阶因子    fo_tasks = get_promising_first_order()        if not fo_tasks:        logging.warning("没有符合条件的一阶因子用于生成二阶任务")        return        # 剪枝处理    fo_layer = prune(fo_tasks, 'anl4', 5)        # 生成二阶表达式    so_alpha_list = []    group_ops = ["group_neutralize", "group_rank", "group_zscore"]        for expr, decay in fo_layer:        for alpha in get_group_second_order_factory([expr], group_ops, "USA"):            so_alpha_list.append((alpha, decay))        # 随机打乱    random.shuffle(so_alpha_list)        # 存入数据库    save_tasks_to_db(so_alpha_list, task_type=2)
```

## 五、三阶任务生成与处理

### 1. 从二阶结果筛选优质因子

```
def get_promising_second_order(min_sharpe=1.3, min_fitness=0.8):    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        cursor.execute("""        SELECT id, expression, decay FROM alpha_tasks         WHERE task_type=2 AND status=2         AND sharpe_ratio >= %s AND fitness >= %s        ORDER BY sharpe_ratio DESC LIMIT 200    """, (min_sharpe, min_fitness))        promising_tasks = cursor.fetchall()    cursor.close()    conn.close()        return promising_tasks
```

### 2. 生成三阶任务

```
def generate_third_order_tasks():    # 获取优质二阶因子    so_tasks = get_promising_second_order()        if not so_tasks:        logging.warning("没有符合条件的二阶因子用于生成三阶任务")        return        # 剪枝处理    so_layer = prune(so_tasks, 'anl4', 5)        # 生成三阶表达式    th_alpha_list = []        for expr, decay in so_layer:        for alpha in trade_when_factory("trade_when", expr, "USA"):            th_alpha_list.append((alpha, decay))        # 随机打乱    random.shuffle(th_alpha_list)        # 存入数据库    save_tasks_to_db(th_alpha_list, task_type=3)        logging.info(f"生成三阶表达式数量: {len(th_alpha_list)}")
```

## 六、任务调度与管理

### 1. 任务状态监控

```
def monitor_tasks():    conn = pymysql.connect(host='localhost', user='user', password='pass', database='alpha_db')    cursor = conn.cursor()        # 获取各类型任务状态统计    cursor.execute("""        SELECT task_type, status, COUNT(*) as count         FROM alpha_tasks         GROUP BY task_type, status        ORDER BY task_type, status    """)        stats = cursor.fetchall()        logging.info("任务状态统计:")    for task_type, status, count in stats:        type_desc = {1: "一阶", 2: "二阶", 3: "三阶"}.get(task_type, "未知")        status_desc = {0: "待运行", 1: "运行中", 2: "已完成"}.get(status, "未知")        logging.info(f"{type_desc}任务-{status_desc}: {count}个")        cursor.close()    conn.close()
```

### 2. 自动调度运行

```
def auto_schedule():    # 检查并运行一阶任务    if has_pending_tasks(1):        run_first_order_simulation()        # 检查并生成二阶任务    if should_generate_second_order():        generate_second_order_tasks()        # 检查并运行二阶任务    if has_pending_tasks(2):        run_second_order_simulation()        # 检查并生成三阶任务    if should_generate_third_order():        generate_third_order_tasks()        # 检查并运行三阶任务    if has_pending_tasks(3):        run_third_order_simulation()
```

## 七、经验总结

1. 1 **模块化设计** ：将复杂的Alpha生成流程拆分为清晰的三个阶段，每个阶段职责单一
2. 2 **状态管理** ：通过MySQL记录任务状态，便于监控和恢复
3. 3 **批量处理** ：合理设置批量大小，平衡资源利用率和系统负载
4. 4 **错误处理** ：完善的异常捕获和重试机制，确保任务连续性
5. 5 **性能监控** ：定期检查任务执行情况，及时发现并解决问题

通过这套方法，我成功地将原本复杂混乱的Alpha开发流程变得清晰可控，大大提高了开发效率和因子质量。虽然代码还有很多需要完善的地方，但希望这些经验能帮助其他新人更快上手Alpha因子开发工作。

**顾问 JG15244 (Rank 67) 的解答与建议**:
大佬这套流程下来每天的回测量在多少左右呢？

我也曾想过将一阶二阶的表达式存入数据库中，然后回测的时候从数据库中取出来，但是从数据库中取数这一过程随着数据量的增加，时间也会变长。看您上面的代码里的流程中从数据库中取出表达式后，回测完成后会再更新这一批数据，这里又增加了时间的损耗，个人感觉效率上会有所影响。可以分享下每天的回测量嘛。


---

### 技术对话片段 103 (原帖: 如何在云服务器上24小时运行代码)
- **原帖链接**: [Commented] 如何在云服务器上24小时运行代码.md
- **时间**: 1年前

**提问/主帖背景 (JT84734)**:
在成为顾问之后我们可以进行大量的回测，最好是24小时不停的回测，这个时候代码还放在本地运行就不是那么方便了。所以接下来我会介绍如何将代码移动到云服务器上运行。

## 1. 购买服务器

如何购买服务器这个这论坛上已经有介绍了，可以直接跳转：
 [💻如何使用天翼云主机进行云端程序挂载]([L2] 如何使用天翼云主机进行云端程序挂载_25891396254231.md) 
 [💻如何免费领取阿里无影云电脑使用](../顾问 SD17531 (Rank 15)/[Commented] 如何免费领取阿里无影云电脑使用.md) 
 [💻如何设置云电脑之京东云？]([L2] 如何设置云电脑之京东云_25880682394263.md)

我之前分享过一篇免费领取华为服务器的文章，不过近期有同学反应不能领取了，我没有去验证，感兴趣的小伙伴可以再去尝试一下 [华为云沃土云创计划——领取401元代金券（可免费购买Flexus服务器）]([L2] 华为云沃土云创计划领取401元代金券可免费购买Flexus服务器_28322890747799.md)

在购买服务器之后，需要使用ssh远程连接上服务器，使用命令行进行操作。简单软件可以直接使用Windows的powershell，专业一些的软件收费的有xshell，免费的可以使用windTerm。连接上服务器后的操作的需要使用命令行进行，如果对命令行不熟悉的同学可以借助kimi，豆包，deepseek等大语言模型的帮助，发送自己的需求，让AI把命令写出来。

## 2. 安装python环境

我这里使用的是debian系统，首先安装 `pyenv，` 这是一个python版本管理工具，可以方便的管理和切换多个python环境。如果存在网络问题可以先换源：

```
sudo sed -i 's|[链接已屏蔽] /etc/apt/sources.list
sudo apt update

```

1. **安装依赖** ： `pyenv` 需要一些依赖来正常工作，包括 `git` 、 `make` 、 `build-essential` 和 `libssl-dev` 。在Debian系统中，你可以使用以下命令安装这些依赖：

```
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git   

```

1. **安装 `pyenv`** ：通过 `git` 克隆 `pyenv` 的仓库到你的根目录：
   ```
   git clone [链接已屏蔽] ~/.pyenv
   ```
2. **配置环境变量** ：将 `pyenv` 的初始化脚本添加到你的shell配置文件（如 `.bashrc` 或 `.zshrc` ）中：
   ```
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   ```
3. 重新加载配置文件：

```
source ~/.bashrc

```

1. **安装指定版本的Python** ：使用 `pyenv` 安装Python 3.12(这个过程需要几分钟)：
   ```
   pyenv install 3.12.0
   ```

请注意，你需要指定具体的版本号，因为 `3.12` 不是一个有效的版本号，需要具体的版本号，如 `3.12.0` 。
2.  **设置全局Python版本** ：如果你想将Python 3.12设置为全局默认版本，可以使用以下命令：

```
 pyenv global 3.12.0

```

#### pyenv常用命令：

1. 查看可用的Python版本：

```
pyenv install --list

```

1. 安装特定版本的Python：

```
pyenv install 版本号

```

1. 查看当前激活的Python版本：

```
pyenv version

```

1. 列出已安装的Python版本：

```
pyenv versions

```

1. 切换Python版本：

```
pyenv local 版本号 

```

1. 卸载Python版本：

```
 pyenv uninstall 版本号

```

## 安装zellij

安装好服务器后，我们可以使用vscode 上的remote-ssh插件进行开发和调试代码。
 
> [!NOTE] [图片 OCR 识别内容]
> Remote
> SSH
> S8RZI
> Openanyfolderon
> remote machine Using SSHand takeadvanta;
> Nicosoft
 
这个时候你可能会发现当运行代码后，关闭vscode后服务器那边的代码还是会终止，为了避免这种情况，让程序一直的运行下去我们需要一个终端复用器。这里我推荐使用zellij，这个相对于tumx，用起来会简单易用很多。

这里先安装x-cmd,然后使用x-cmd安装zellij

```
eval "$(curl [链接已屏蔽])"        # 安装 x-cmd
x env use zellij                            # 使用 x-cmd 安装 zellij

```

接下来输入 `zellij --version`  来查看是否安装成功


> [!NOTE] [图片 OCR 识别内容]
> je@saphon
> $ zellij
> Version
> zellij
> 0.40.1


zellij的常用命令：

```
zellij -s <session name>            # 创建新的会话
zellij ls                           # 列出活动的会话
zellij a <session name>             # 连接到指定会话
zellij k <session name>             # 杀死指定会话
zellij d <session name>             # 删除指定会话
zellij ka                           # 杀死所有会话

```

zellij 常用快捷键

```
- `Ctrl-g`：锁定或界面，主要用于缓解快捷键冲突的情况。
- `Ctrl-p` + `n`：分割生成新窗口
- `Ctrl-p` + `x`：关闭当前聚焦的窗口
- `Ctrl-p` + `←`：切换到左侧的窗口
- `Ctrl-t` + `n`：创建新的标签页
- `Ctrl-t` + `x`：关闭当前聚焦的标签页
- `Ctrl-t` + `←`：切换到左侧的标签页 

```

使用方法非常简单，例如使用  `zellij -s worldquant`  创建一个一个名字为worldquant的会话。创建成功之后会自动进入会话。


> [!NOTE] [图片 OCR 识别内容]
> Zellij (worldquant)
> Tab #1
> jieosaphon:
> jie@saphon: $
> Ctrl
> C9>
> LOCK
> PANE
> st> TAB 
> sn> RESIZE
> shs MOVE
> Ss> SEARCH
> Co> SESSION 
> QUIT
> BASE
> It
> 25
> Rw eR?
> It +〈!
> er At +
> #y;
> 只43ate
> It +
> -85322
> e??
> Cq2
> Ti:


快捷键直接显示在最下面，在这里可以进入对应的文件夹，直接运行已经编写好的代码，然后使用快捷键 `ctrl +o`  +  `d`  即可退出当前会话，再命令行使用  `zellij a worldquant`  就可以恢复会话，也可以看见程序的运行情况。


> [!NOTE] [图片 OCR 识别内容]
> Zellij (wq)
> Tab #1
> rootphcss
> BCS-dgad: ~/worldquant/consultant
> SCROLL:
> 3/19531
> pool 367 task 8 simulate done
> pool 368
> task
> post done
> 368
> task 8 Simulate
> done
> pool 369 task 8 post done
> 369 task 8 simulate done
> pool 370 task
> post done
> 370 task 8 simulate done
> pool 371 task
> post done
> 371
> task 8 Simulate done
> pool 372
> task
> post done
> pool 372 task & simulate done
> pool 373
> task
> post done
> 373 task 8 simulate done
> pool 374 task
> post done
> 374 task 8 simulate done
> pool 375
> task
> post done
> pool 375 task & simulate done
> Ctrl +
> 铝〉
> LOCK
> SD> PANE
> Ct〉 TAB 
> 〈D〉
> RESIZE
> Ch〉
> MOUE
> 〈5〉
> SEARCH
> 〈0〉
> SESSION
> 〈q〉 QUIT
> pool
> Pool
> Pool
> Pool
> pool
> Pool


完成上面的工作之后，就能让代码在云服务器上一直运行了。这里没有涉及到代码，我现在使用的还是上课提供的代码，这里是代码放在云服务器上24小时运行。看到论坛有同学分享修改代码加入微信通知的，后面修改代码加入这个功能，就可以做到代码运行后就不需要管，等微信收到通知后再来处理。

**顾问 JG15244 (Rank 67) 的解答与建议**:
你好，我在使用zellij的时候，有些快捷键跟vscode快捷键冲突了，请问你是怎么解决的。


---

### 技术对话片段 104 (原帖: 如何在云服务器上24小时运行代码)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 如何在云服务器上24小时运行代码_29031525682199.md
- **时间**: 1年前

**提问/主帖背景 (JT84734)**:
在成为顾问之后我们可以进行大量的回测，最好是24小时不停的回测，这个时候代码还放在本地运行就不是那么方便了。所以接下来我会介绍如何将代码移动到云服务器上运行。

## 1. 购买服务器

如何购买服务器这个这论坛上已经有介绍了，可以直接跳转：
 [💻如何使用天翼云主机进行云端程序挂载]([L2] 如何使用天翼云主机进行云端程序挂载_25891396254231.md) 
 [💻如何免费领取阿里无影云电脑使用]([L2] 如何免费领取阿里无影云电脑使用_25889938244375.md) 
 [💻如何设置云电脑之京东云？]([L2] 如何设置云电脑之京东云_25880682394263.md)

我之前分享过一篇免费领取华为服务器的文章，不过近期有同学反应不能领取了，我没有去验证，感兴趣的小伙伴可以再去尝试一下 [华为云沃土云创计划——领取401元代金券（可免费购买Flexus服务器）]([L2] 华为云沃土云创计划领取401元代金券可免费购买Flexus服务器_28322890747799.md)

在购买服务器之后，需要使用ssh远程连接上服务器，使用命令行进行操作。简单软件可以直接使用Windows的powershell，专业一些的软件收费的有xshell，免费的可以使用windTerm。连接上服务器后的操作的需要使用命令行进行，如果对命令行不熟悉的同学可以借助kimi，豆包，deepseek等大语言模型的帮助，发送自己的需求，让AI把命令写出来。

## 2. 安装python环境

我这里使用的是debian系统，首先安装 `pyenv，` 这是一个python版本管理工具，可以方便的管理和切换多个python环境。如果存在网络问题可以先换源：

```
sudo sed -i 's|[链接已屏蔽] /etc/apt/sources.list
sudo apt update

```

1. **安装依赖** ： `pyenv` 需要一些依赖来正常工作，包括 `git` 、 `make` 、 `build-essential` 和 `libssl-dev` 。在Debian系统中，你可以使用以下命令安装这些依赖：

```
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git   

```

1. **安装 `pyenv`** ：通过 `git` 克隆 `pyenv` 的仓库到你的根目录：
   ```
   git clone [链接已屏蔽] ~/.pyenv
   ```
2. **配置环境变量** ：将 `pyenv` 的初始化脚本添加到你的shell配置文件（如 `.bashrc` 或 `.zshrc` ）中：
   ```
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   ```
3. 重新加载配置文件：

```
source ~/.bashrc

```

1. **安装指定版本的Python** ：使用 `pyenv` 安装Python 3.12(这个过程需要几分钟)：
   ```
   pyenv install 3.12.0
   ```

请注意，你需要指定具体的版本号，因为 `3.12` 不是一个有效的版本号，需要具体的版本号，如 `3.12.0` 。
2.  **设置全局Python版本** ：如果你想将Python 3.12设置为全局默认版本，可以使用以下命令：

```
 pyenv global 3.12.0

```

#### pyenv常用命令：

1. 查看可用的Python版本：

```
pyenv install --list

```

1. 安装特定版本的Python：

```
pyenv install 版本号

```

1. 查看当前激活的Python版本：

```
pyenv version

```

1. 列出已安装的Python版本：

```
pyenv versions

```

1. 切换Python版本：

```
pyenv local 版本号 

```

1. 卸载Python版本：

```
 pyenv uninstall 版本号

```

## 安装zellij

安装好服务器后，我们可以使用vscode 上的remote-ssh插件进行开发和调试代码。
 
> [!NOTE] [图片 OCR 识别内容]
> Remote
> SSH
> S8RZI
> Openanyfolderon
> remote machine Using SSHand takeadvanta;
> Nicosoft
 
这个时候你可能会发现当运行代码后，关闭vscode后服务器那边的代码还是会终止，为了避免这种情况，让程序一直的运行下去我们需要一个终端复用器。这里我推荐使用zellij，这个相对于tumx，用起来会简单易用很多。

这里先安装x-cmd,然后使用x-cmd安装zellij

```
eval "$(curl [链接已屏蔽])"        # 安装 x-cmd
x env use zellij                            # 使用 x-cmd 安装 zellij

```

接下来输入 `zellij --version`  来查看是否安装成功


> [!NOTE] [图片 OCR 识别内容]
> je@saphon
> $ zellij
> Version
> zellij
> 0.40.1


zellij的常用命令：

```
zellij -s <session name>            # 创建新的会话
zellij ls                           # 列出活动的会话
zellij a <session name>             # 连接到指定会话
zellij k <session name>             # 杀死指定会话
zellij d <session name>             # 删除指定会话
zellij ka                           # 杀死所有会话

```

zellij 常用快捷键

```
- `Ctrl-g`：锁定或界面，主要用于缓解快捷键冲突的情况。
- `Ctrl-p` + `n`：分割生成新窗口
- `Ctrl-p` + `x`：关闭当前聚焦的窗口
- `Ctrl-p` + `←`：切换到左侧的窗口
- `Ctrl-t` + `n`：创建新的标签页
- `Ctrl-t` + `x`：关闭当前聚焦的标签页
- `Ctrl-t` + `←`：切换到左侧的标签页 

```

使用方法非常简单，例如使用  `zellij -s worldquant`  创建一个一个名字为worldquant的会话。创建成功之后会自动进入会话。


> [!NOTE] [图片 OCR 识别内容]
> Zellij (worldquant)
> Tab #1
> jieosaphon:
> jie@saphon: $
> Ctrl
> C9>
> LOCK
> PANE
> st> TAB 
> sn> RESIZE
> shs MOVE
> Ss> SEARCH
> Co> SESSION 
> QUIT
> BASE
> It
> 25
> Rw eR?
> It +〈!
> er At +
> #y;
> 只43ate
> It +
> -85322
> e??
> Cq2
> Ti:


快捷键直接显示在最下面，在这里可以进入对应的文件夹，直接运行已经编写好的代码，然后使用快捷键 `ctrl +o`  +  `d`  即可退出当前会话，再命令行使用  `zellij a worldquant`  就可以恢复会话，也可以看见程序的运行情况。


> [!NOTE] [图片 OCR 识别内容]
> Zellij (wq)
> Tab #1
> rootphcss
> BCS-dgad: ~/worldquant/consultant
> SCROLL:
> 3/19531
> pool 367 task 8 simulate done
> pool 368
> task
> post done
> 368
> task 8 Simulate
> done
> pool 369 task 8 post done
> 369 task 8 simulate done
> pool 370 task
> post done
> 370 task 8 simulate done
> pool 371 task
> post done
> 371
> task 8 Simulate done
> pool 372
> task
> post done
> pool 372 task & simulate done
> pool 373
> task
> post done
> 373 task 8 simulate done
> pool 374 task
> post done
> 374 task 8 simulate done
> pool 375
> task
> post done
> pool 375 task & simulate done
> Ctrl +
> 铝〉
> LOCK
> SD> PANE
> Ct〉 TAB 
> 〈D〉
> RESIZE
> Ch〉
> MOUE
> 〈5〉
> SEARCH
> 〈0〉
> SESSION
> 〈q〉 QUIT
> pool
> Pool
> Pool
> Pool
> pool
> Pool


完成上面的工作之后，就能让代码在云服务器上一直运行了。这里没有涉及到代码，我现在使用的还是上课提供的代码，这里是代码放在云服务器上24小时运行。看到论坛有同学分享修改代码加入微信通知的，后面修改代码加入这个功能，就可以做到代码运行后就不需要管，等微信收到通知后再来处理。

**顾问 JG15244 (Rank 67) 的解答与建议**:
你好，我在使用zellij的时候，有些快捷键跟vscode快捷键冲突了，请问你是怎么解决的。


---

### 技术对话片段 105 (原帖: 我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化)
- **原帖链接**: [Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化.md
- **时间**: 1年前

**提问/主帖背景 (LQ78150)**:
在成为顾问以后，我一直困惑究竟要如何构建自己的模板，作为新人我相信你也有和我一样的困惑，那么这篇文章就是为你而写的

上一篇文章，我把世坤的数据集和所有operator下载为文档喂给了腾讯IMA知识库，这些知识可以帮我解读一些现有模板的逻辑，但是如何在此基础上继续拓展一直是我没有解决的问题

但是最近又翻了翻论坛，看到了weijie老师的那个模板系列，我来了一点灵感，能不能把老师分享的这些知识，也纳入我知识库的一部分呢

说干就干


> [!NOTE] [图片 OCR 识别内容]
> 世坤知识库
> 持渎行动者
> 1253个内穿
> 庆宋填写莅述吧
> 内容
> Machine Alpha 基础知识1
> 什么是Alpha模板 docx
> Word
> 21.38
> 跑模皈心得docx
> Word
> 06/
> CHN 0 TOPZOOOU VECTOR数据集sentimentz7所
> 有字段Jocx
> LOTC


首先我把文章写成word喂给了IMA，接着我先测试一下，他是否已经理解关于模板的知识，以下是他的回答


> [!NOTE] [图片 OCR 识别内容]
> 什么是ALPHA模板
> ima
> DeepSeek RT
> 找到了60篇知识库资料作为参考



> [!NOTE] [图片 OCR 识别内容]
> 根据提供的文档内容
> 以下是失于Alpha模板的详细解释
> 定义与核心概念
> Alpha模板是一
> -种基于轻济逻辑的结构化方法
> 用于在广话的Alpha空间中精确定位有效的Alpha信号
> (即能够产生超颞收益的策略)
> 它通过模块化的组件 (如操作符
> 参数)  实现高度适应性
> 允许用户通过互换和调整模块来探萦新的
> Alpha信号。
> 2.关键特征
> 结构化框架:
> 提供标准化的公式模板。例如:
> 〈grOUP_
> compare OD>(<ts
> compare_Op> (<company_fundamentals >,
> days >, <group>))
> 其中:
> <company_fundamentals > : 可莓换为基本面指标 (如EPS
> DPS
> 销售额等)
> <ts_compare_Op>: 时间序列操作符 (如ts_rank。
> IS ZsCOrE)
> group_compare_Op > : 分组比较操作符 (如group_rank
> grOUP_ZSCOre]
> <days >和<groUp > : 可调整回溯周期和分组逻辑。
> 模块化与灵活性:
> 每个组件均可独立替换或优化。 用广可根据具体霈求调整参数或逻辑
> 从雨快速生成定制化的Alpha因


看到这些回答，我想他理解了什么是模板的知识，那么下一步，我们要的就是通过编程，将泛化的模板转化成无数组可以回测的ALPHA表达式，于是我继续对ima进行提问。


> [!NOTE] [图片 OCR 识别内容]
> Cgroup_compare_Op>(sts_compare_Op>(scompany_fundamentals>
> 〈Gays>)
> <group>)根据这个泛化表达式如何用Python生成各秫可能的傍号
> ima
> DeepSeel Rl
> 找到了95篇知识库资料作为


他也为我生成了相应的代码，并且都是可以在brain平台进行回测的表达式


> [!NOTE] [图片 OCR 识别内容]
> Broup
> neutralize(ts_
> aVg_diff(ebit, 252),
> Sector )
> Broup
> neutralize(ts
> aVg_diff(ebit, 252)
> country )
> Broup
> neutralize(ts_avg_diff(sales, 30)
> industry )
> Broup_neutralize(ts
> aVg_diff(sales, 30)
> Sector )
> Broup_neutralize(ts_
> aVB
> diff(sales, 30)
> country )
> Broup_neutralize(ts
> aVg_diff(sales, 60)
> industry)
> Broup
> neutralize(ts_aVg_diff(sales
> Sector)
> Broup_
> neutralize(ts_aVg_diff(sales
> country )
> Broup_neutralize(ts
> aVg_diff(sales, 90)
> industry )
> Broup
> neutralize(ts_avg_diff(sales, 90)
> Sector)
> Broup_neutralize(ts
> aVg_diff(sales, 90)
> Country)
> Broup_
> neutralize(ts
> aVB
> diff(sales, 180), industry)
> Broup
> neutralize(ts_avg_diff(sales, 180),
> sector )
> Broup
> neutralize(ts_avg_diff(sales, 180),
> Country )
> Broup
> neutralize(ts_avg_diff(sales, 252), industry)
> group_neutralize(ts_
> aVg_diff(sales, 252),
> Sector )
> group_neutralize(ts_aVg_diff(sales, 252),
> country)
> 共生成  1080 种可能的A1pha信号组合


构建知识库的好处，就是我不再需要去平台搜索eps相似字段，相关operator等，我只需要让知识库为我提供一些相似或相近字段或者operator，这样我就能完成上千甚至上万种组合的搜索，这样就可以把我从繁重的搜索工作解放出来，专心读论文，专心生成新的模板

如果对你有所启发，请点个赞吧，亲

**顾问 JG15244 (Rank 67) 的解答与建议**:
非常好的分享，从ai生成的alpha表达式来看，看起来是非常符合wq平台的规则。我之前也有通过将operate、fields和一些文章喂给ai，然后向其询问alpha模板，但是发现ai给出的模板绝大多数都是动量方向的模板，且有些时候使用的表达式也不知wq平台上存在的。不知道大佬有没有遇到过这些问题呢。

同时想问一句，这个是私人的嘛。

==========================================

山教会我，所有的选择都是相连的。海教会我，所有的命运都是起伏的。​ ​​​ ---库索-

==========================================


---

### 技术对话片段 106 (原帖: 我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化_33016862088599.md
- **时间**: 1年前

**提问/主帖背景 (LQ78150)**:
在成为顾问以后，我一直困惑究竟要如何构建自己的模板，作为新人我相信你也有和我一样的困惑，那么这篇文章就是为你而写的

上一篇文章，我把世坤的数据集和所有operator下载为文档喂给了腾讯IMA知识库，这些知识可以帮我解读一些现有模板的逻辑，但是如何在此基础上继续拓展一直是我没有解决的问题

但是最近又翻了翻论坛，看到了weijie老师的那个模板系列，我来了一点灵感，能不能把老师分享的这些知识，也纳入我知识库的一部分呢

说干就干


> [!NOTE] [图片 OCR 识别内容]
> 世坤知识库
> 持渎行动者
> 1253个内穿
> 庆宋填写莅述吧
> 内容
> Machine Alpha 基础知识1
> 什么是Alpha模板 docx
> Word
> 21.38
> 跑模皈心得docx
> Word
> 06/
> CHN 0 TOPZOOOU VECTOR数据集sentimentz7所
> 有字段Jocx
> LOTC


首先我把文章写成word喂给了IMA，接着我先测试一下，他是否已经理解关于模板的知识，以下是他的回答


> [!NOTE] [图片 OCR 识别内容]
> 什么是ALPHA模板
> ima
> DeepSeek RT
> 找到了60篇知识库资料作为参考



> [!NOTE] [图片 OCR 识别内容]
> 根据提供的文档内容
> 以下是失于Alpha模板的详细解释
> 定义与核心概念
> Alpha模板是一
> -种基于轻济逻辑的结构化方法
> 用于在广话的Alpha空间中精确定位有效的Alpha信号
> (即能够产生超颞收益的策略)
> 它通过模块化的组件 (如操作符
> 参数)  实现高度适应性
> 允许用户通过互换和调整模块来探萦新的
> Alpha信号。
> 2.关键特征
> 结构化框架:
> 提供标准化的公式模板。例如:
> 〈grOUP_
> compare OD>(<ts
> compare_Op> (<company_fundamentals >,
> days >, <group>))
> 其中:
> <company_fundamentals > : 可莓换为基本面指标 (如EPS
> DPS
> 销售额等)
> <ts_compare_Op>: 时间序列操作符 (如ts_rank。
> IS ZsCOrE)
> group_compare_Op > : 分组比较操作符 (如group_rank
> grOUP_ZSCOre]
> <days >和<groUp > : 可调整回溯周期和分组逻辑。
> 模块化与灵活性:
> 每个组件均可独立替换或优化。 用广可根据具体霈求调整参数或逻辑
> 从雨快速生成定制化的Alpha因


看到这些回答，我想他理解了什么是模板的知识，那么下一步，我们要的就是通过编程，将泛化的模板转化成无数组可以回测的ALPHA表达式，于是我继续对ima进行提问。


> [!NOTE] [图片 OCR 识别内容]
> Cgroup_compare_Op>(sts_compare_Op>(scompany_fundamentals>
> 〈Gays>)
> <group>)根据这个泛化表达式如何用Python生成各秫可能的傍号
> ima
> DeepSeel Rl
> 找到了95篇知识库资料作为


他也为我生成了相应的代码，并且都是可以在brain平台进行回测的表达式


> [!NOTE] [图片 OCR 识别内容]
> Broup
> neutralize(ts_
> aVg_diff(ebit, 252),
> Sector )
> Broup
> neutralize(ts
> aVg_diff(ebit, 252)
> country )
> Broup
> neutralize(ts_avg_diff(sales, 30)
> industry )
> Broup_neutralize(ts
> aVg_diff(sales, 30)
> Sector )
> Broup_neutralize(ts_
> aVB
> diff(sales, 30)
> country )
> Broup_neutralize(ts
> aVg_diff(sales, 60)
> industry)
> Broup
> neutralize(ts_aVg_diff(sales
> Sector)
> Broup_
> neutralize(ts_aVg_diff(sales
> country )
> Broup_neutralize(ts
> aVg_diff(sales, 90)
> industry )
> Broup
> neutralize(ts_avg_diff(sales, 90)
> Sector)
> Broup_neutralize(ts
> aVg_diff(sales, 90)
> Country)
> Broup_
> neutralize(ts
> aVB
> diff(sales, 180), industry)
> Broup
> neutralize(ts_avg_diff(sales, 180),
> sector )
> Broup
> neutralize(ts_avg_diff(sales, 180),
> Country )
> Broup
> neutralize(ts_avg_diff(sales, 252), industry)
> group_neutralize(ts_
> aVg_diff(sales, 252),
> Sector )
> group_neutralize(ts_aVg_diff(sales, 252),
> country)
> 共生成  1080 种可能的A1pha信号组合


构建知识库的好处，就是我不再需要去平台搜索eps相似字段，相关operator等，我只需要让知识库为我提供一些相似或相近字段或者operator，这样我就能完成上千甚至上万种组合的搜索，这样就可以把我从繁重的搜索工作解放出来，专心读论文，专心生成新的模板

如果对你有所启发，请点个赞吧，亲

**顾问 JG15244 (Rank 67) 的解答与建议**:
非常好的分享，从ai生成的alpha表达式来看，看起来是非常符合wq平台的规则。我之前也有通过将operate、fields和一些文章喂给ai，然后向其询问alpha模板，但是发现ai给出的模板绝大多数都是动量方向的模板，且有些时候使用的表达式也不知wq平台上存在的。不知道大佬有没有遇到过这些问题呢。

同时想问一句，这个是私人的嘛。

==========================================

山教会我，所有的选择都是相连的。海教会我，所有的命运都是起伏的。​ ​​​ ---库索-

==========================================


---

### 技术对话片段 107 (原帖: 求教，这个alpha还能救一下么)
- **原帖链接**: [Commented] 求教这个alpha还能救一下么.md
- **时间**: 1年前

**提问/主帖背景 (ZP42727)**:
最近跑了一个Spectacular的alpha,  但是 [Sub-universe Sharpe](/hc/en-us/articles/6568644868375?_gl=1*zfgsgt*_gcl_au*MTQzMDQzMDc2OC4xNzQwODkzODM5*_ga*MTczOTA3MDg1MjA5OThjZWVjNTU1NDc3ZGU.*_ga_9RN6WVT1K1*MTc0MzIzOTU3My4xMDMuMS4xNzQzMjQzNDYwLjYwLjAuMA..)   低好多， 尝试找了些方案，但是效果并不是太好。请诸位会诊一下，是否还有挽救的可能。

[图片 (图片已丢失)]

[图片 (图片已丢失)]

参数设置如下：

[图片 (图片已丢失)]

**顾问 JG15244 (Rank 67) 的解答与建议**:
差的有点太多了，差的少的话，我记得论坛里有帖子说可以优化一下，可以在搜索栏里搜搜看。


---

### 技术对话片段 108 (原帖: 求教，这个alpha还能救一下么)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 求教这个alpha还能救一下么_31017228094615.md
- **时间**: 1年前

**提问/主帖背景 (ZP42727)**:
最近跑了一个Spectacular的alpha,  但是 [Sub-universe Sharpe](/hc/en-us/articles/6568644868375?_gl=1*zfgsgt*_gcl_au*MTQzMDQzMDc2OC4xNzQwODkzODM5*_ga*MTczOTA3MDg1MjA5OThjZWVjNTU1NDc3ZGU.*_ga_9RN6WVT1K1*MTc0MzIzOTU3My4xMDMuMS4xNzQzMjQzNDYwLjYwLjAuMA..)   低好多， 尝试找了些方案，但是效果并不是太好。请诸位会诊一下，是否还有挽救的可能。


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> TRAIN
> TEST
> IS
> 09
> Spectacular
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.98
> 2.16%
> 3.97
> 50.21%
> 14.46%
> 465.71%o。



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> PASS
> 1 FAIL
> Sub-universe
> Sharpe Of 0.35 is below cutoff of 0.74.
> 1 PENDING


参数设置如下：


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> USA
> TOP3000
> Fast Expression
> 0.08
> Subindustry
> On
> On
> Verify
> OFF
> Delay


**顾问 JG15244 (Rank 67) 的解答与建议**:
差的有点太多了，差的少的话，我记得论坛里有帖子说可以优化一下，可以在搜索栏里搜搜看。


---

### 技术对话片段 109 (原帖: 组super alpha时所有可用的属性经验分享)
- **原帖链接**: [Commented] 组super alpha时所有可用的属性经验分享.md
- **时间**: 10个月前

**提问/主帖背景 (QQ68782)**:
在学习小组里有人在组SA时用了 own_country 表达式, 但是这个表达式在文档里并没有出现: 
 [[链接已屏蔽])

还有哪些表达式文档没有出现呢? 所有可用的表达式有哪些呢?

在网页里发现, 这个地址可以请求到所有可用的字段: 
 [[链接已屏蔽])

```
{
  "selection": [
    "turnover",
    "long_count",
    "short_count",
    "decay",
    "universe",
    "operator_count",
    "datafield_count",
    "dataset_count",
    "datacategory_count",
    "self_correlation",
    "prod_correlation",
    "neutralization",
    "truncation",
    "datacategories",
    "datasets",
    "datafields",
    "classifications",
    "competitions",
    "themes",
    "name",
    "color",
    "category",
    "favorite",
    "own",
    "own_university",
    "own_country",
    "tags",
    "os_start_date",
    "author_tenure",
    "author_activity",
    "author_distinct_count_regions",
    "author_self_correlation",
    "author_prod_correlation",
    "author_sharpe",
    "author_turnover",
    "author_fitness",
    "author_returns_to_drawdown",
    "author_distinct_count_datafield",
    "author_distinct_count_datasetcategory",
    "author_distinct_quarter_count_datafield",
    "author_distinct_quarter_count_dataset",
    "author_distinct_quarter_count_datasetcategory",
    "author_distinct_count_operator",
    "author_distinct_quarter_count_operator",
    "author_distinct_count_dataset",
    "author_yield_rate",
    "author_quarter_yield_rate"
  ],
  "combo": [
    "alpha",
    "long_value",
    "short_value",
    "pnl",
    "returns",
    "drawdown",
    "long_count",
    "short_count",
    "hold_value",
    "trade_value",
    "hold_shares",
    "trade_shares",
    "hold_pnl",
    "trade_pnl",
    "turnover"
  ]
}
```

其中 themes、own_university、own_country 等在文档里没有出现;

**顾问 JG15244 (Rank 67) 的解答与建议**:
theme这个还真没有用过，大佬可以说下theme这个可以怎么使用吗，有什么值吗。


---

### 技术对话片段 110 (原帖: 组super alpha时所有可用的属性经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 组super alpha时所有可用的属性经验分享_34178199290135.md
- **时间**: 10个月前

**提问/主帖背景 (QQ68782)**:
在学习小组里有人在组SA时用了 own_country 表达式, 但是这个表达式在文档里并没有出现: 
 [[链接已屏蔽])

还有哪些表达式文档没有出现呢? 所有可用的表达式有哪些呢?

在网页里发现, 这个地址可以请求到所有可用的字段: 
 [[链接已屏蔽])

```
{
  "selection": [
    "turnover",
    "long_count",
    "short_count",
    "decay",
    "universe",
    "operator_count",
    "datafield_count",
    "dataset_count",
    "datacategory_count",
    "self_correlation",
    "prod_correlation",
    "neutralization",
    "truncation",
    "datacategories",
    "datasets",
    "datafields",
    "classifications",
    "competitions",
    "themes",
    "name",
    "color",
    "category",
    "favorite",
    "own",
    "own_university",
    "own_country",
    "tags",
    "os_start_date",
    "author_tenure",
    "author_activity",
    "author_distinct_count_regions",
    "author_self_correlation",
    "author_prod_correlation",
    "author_sharpe",
    "author_turnover",
    "author_fitness",
    "author_returns_to_drawdown",
    "author_distinct_count_datafield",
    "author_distinct_count_datasetcategory",
    "author_distinct_quarter_count_datafield",
    "author_distinct_quarter_count_dataset",
    "author_distinct_quarter_count_datasetcategory",
    "author_distinct_count_operator",
    "author_distinct_quarter_count_operator",
    "author_distinct_count_dataset",
    "author_yield_rate",
    "author_quarter_yield_rate"
  ],
  "combo": [
    "alpha",
    "long_value",
    "short_value",
    "pnl",
    "returns",
    "drawdown",
    "long_count",
    "short_count",
    "hold_value",
    "trade_value",
    "hold_shares",
    "trade_shares",
    "hold_pnl",
    "trade_pnl",
    "turnover"
  ]
}
```

其中 themes、own_university、own_country 等在文档里没有出现;

**顾问 JG15244 (Rank 67) 的解答与建议**:
theme这个还真没有用过，大佬可以说下theme这个可以怎么使用吗，有什么值吗。


---

### 技术对话片段 111 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
- **原帖链接**: [Commented] 经验分享PPAC全球第三名回馈社区经验分享.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。

[图片 (图片已丢失)]

第一阶段：Alpha 构建（前五周）

比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。

我主要从以下三类渠道构建 Alpha：

1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。

2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。

3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。

构建期间，我也特别注意以下三方面的多样性控制：

- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区
- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等
- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性

此外，在筛选 Alpha 入库时，我建立了以下五步流程：

① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；
② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；
③ 计算并筛除自相关过高的表达式，提高组合独立性；
④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；
⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。

第二阶段：Alpha 筛选（第六周）

第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。

我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健

在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级

GPT 在筛选阶段的最大作用体现在两个方面：

1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。

2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。

此外，GPT 还协助完成以下操作：

- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；

- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；

- 避免过多同类中性化、universe 和数据来源重复的表达式；

- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。

我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。

结语：经验与建议

1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。

2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。

3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting
似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜

4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

**顾问 JG15244 (Rank 67) 的解答与建议**:
全是干货，收获颇多，看来alpha的多样性、低相关性无论是在比赛中还是日常的提高value factory中都起着至关重要的作用。

期待大佬value factory更新后直达 1.0 !!!!


---

### 技术对话片段 112 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.3
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 2.94
> Reached Grandmaster
> 0.5


第一阶段：Alpha 构建（前五周）

比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。

我主要从以下三类渠道构建 Alpha：

1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。

2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。

3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。

构建期间，我也特别注意以下三方面的多样性控制：

- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区
- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等
- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性

此外，在筛选 Alpha 入库时，我建立了以下五步流程：

① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；
② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；
③ 计算并筛除自相关过高的表达式，提高组合独立性；
④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；
⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。

第二阶段：Alpha 筛选（第六周）

第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。

我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健

在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级

GPT 在筛选阶段的最大作用体现在两个方面：

1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。

2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。

此外，GPT 还协助完成以下操作：

- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；

- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；

- 避免过多同类中性化、universe 和数据来源重复的表达式；

- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。

我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。

结语：经验与建议

1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。

2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。

3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting
似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜

4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

**顾问 JG15244 (Rank 67) 的解答与建议**:
全是干货，收获颇多，看来alpha的多样性、低相关性无论是在比赛中还是日常的提高value factory中都起着至关重要的作用。

期待大佬value factory更新后直达 1.0 !!!!


---
