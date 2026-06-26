# 顾问 WX64154 (Rank 32) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 WX64154 (Rank 32) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 26年Q1 Genius定级已更新Q2赛季加油_39728814444695.md
- **时间**: 2个月前

**提问/主帖背景 (KH94146)**:

> [!NOTE] [图片 OCR 识别内容]
> Ganius
> 3喜报
> 2026年01季度 Genius项目定级
> 困
> 区荣誉榜
> Grand Master 级别
> Master 级别
> Expert 级别
> GRAND
> MASTER
> MASTER
> EXPERT
> 49人
> 131人
> 326人
> 获得
> 获得
> 获得
> 季度奖金:
> 季度奖金:
> 季度奖金:
> 8000
> 2000
> 200
> 25000
> 8000
> 2000
> USD
> USD
> USD
> Gonius
> Genius 定级,荣耀共享


**顾问 WX64154 (Rank 32) 的解答与建议**:

> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2026-21,January 1st, 2026
> Mar-h 315t, 2026
> SJIJ
> EpErt
> Iaster
> GranTas-er
> Signals
> 276
> Reached Grandmaster
> Pyramids Completed
> 60
> Reached Grandmaster
> Combined Alpha Performance
> 2.04
> Reached Grandmaster
> Combined Selected Alpha Performance
> 0.99
> 0.01 more t0 Master
> Combined Power Pool Alpha Performance
> 2.03
> Reached Grandmaster
> Combined Osmosis Performance
> -1.06
> 1.56 more to Expert
 努力了一个季度 又一次成为了GM

================================================================================

=============================越努力，越幸运======================================

==============================================================================


---

### 技术对话片段 2 (原帖: 【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘)
- **原帖链接**: [Commented] 【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘.md
- **时间**: 6个月前

**提问/主帖背景 (PZ66162)**:
基于传统的遗传算法和表达式变异的 Alpha 挖掘在效率上存在瓶颈。

我们开发了一个基于 LLM Agent 的全自动 Alpha 挖掘工作流，代码仓库地址：
 [[链接已屏蔽])

我们的想法是从 WorldQuant 平台的讨论帖中挖掘可用的 Alpha，具体流程如下：

1. 模拟登录到论坛链接，爬取最近的 200 条帖子（工具会打开默认浏览器，这一步需要用户手动输入账户密码登录）；
2. 通过 WQ API 获取 Fast Expression 可用的操作符和字段；
3. 对操作符和字段进行规约，生成操作符类型和字段类型集合；
4. 对每一条帖子，判定是否是“有指导 Alpha 挖掘潜力的”；
5. 对于筛选出的帖子，调用 LLM 总结观点假设，从观点假设中生成 Alpha 模板（模板由操作符、字段、操作符类型、字段类型构成）；
6. 对于 Alpha 模板，依据其包含的操作符类型和字段类型，多重循环遍历可选参数，生成 Alpha；
7. 对每个 Alpha 调用 WQ API 回测，保存回测结果到本地。

我们生成了 2334887 个 Alpha，在 USA TOP3000 和 ASI MINVOL1M 上进行了回测，alpha 可用率占所有已回测合法的 alpha 的 0.5% 上下。

后续计划：

1. 添加基于 AST 的本地的 Fast Expression 合法检查，提前筛选掉不合法的 Alpha；
2. 添加迭代循环，构建 Self Improve 的 Alpha 挖掘流程。

我们欢迎大家 Fork 我们的工作，合理的 issue 和 pull request 是非常欢迎的。有任何的疑问和建议我们也可以一起在评论区讨论～

**顾问 WX64154 (Rank 32) 的解答与建议**:
非计算机专业，实在是不会用AI，不大知道能走多远

=================================================================================================================good good study==========================================

===============================day day up=============================================


---

### 技术对话片段 3 (原帖: 【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘_35951496406551.md
- **时间**: 6个月前

**提问/主帖背景 (PZ66162)**:
基于传统的遗传算法和表达式变异的 Alpha 挖掘在效率上存在瓶颈。

我们开发了一个基于 LLM Agent 的全自动 Alpha 挖掘工作流，代码仓库地址：
 [[链接已屏蔽])

我们的想法是从 WorldQuant 平台的讨论帖中挖掘可用的 Alpha，具体流程如下：

1. 模拟登录到论坛链接，爬取最近的 200 条帖子（工具会打开默认浏览器，这一步需要用户手动输入账户密码登录）；
2. 通过 WQ API 获取 Fast Expression 可用的操作符和字段；
3. 对操作符和字段进行规约，生成操作符类型和字段类型集合；
4. 对每一条帖子，判定是否是“有指导 Alpha 挖掘潜力的”；
5. 对于筛选出的帖子，调用 LLM 总结观点假设，从观点假设中生成 Alpha 模板（模板由操作符、字段、操作符类型、字段类型构成）；
6. 对于 Alpha 模板，依据其包含的操作符类型和字段类型，多重循环遍历可选参数，生成 Alpha；
7. 对每个 Alpha 调用 WQ API 回测，保存回测结果到本地。

我们生成了 2334887 个 Alpha，在 USA TOP3000 和 ASI MINVOL1M 上进行了回测，alpha 可用率占所有已回测合法的 alpha 的 0.5% 上下。

后续计划：

1. 添加基于 AST 的本地的 Fast Expression 合法检查，提前筛选掉不合法的 Alpha；
2. 添加迭代循环，构建 Self Improve 的 Alpha 挖掘流程。

我们欢迎大家 Fork 我们的工作，合理的 issue 和 pull request 是非常欢迎的。有任何的疑问和建议我们也可以一起在评论区讨论～

**顾问 WX64154 (Rank 32) 的解答与建议**:
非计算机专业，实在是不会用AI，不大知道能走多远

=================================================================================================================good good study==========================================

===============================day day up=============================================


---

### 技术对话片段 4 (原帖: 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享)
- **原帖链接**: [Commented] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享.md
- **时间**: 9个月前

**提问/主帖背景 (ML42552)**:
还记得weijie老师上课说过的一句话，一些sharp很高，turnover也很高的alpha是非常具有价值的，然后当时我就找到了下面这个alpha，并在labs上对其数据进行了分析。

本文讲的相对比较详细，建议新手务必认真读完，模板在本文的最下面，经过验证可以，在USA，GLB，EUR 三个大区都有不错的效果，至于你问我为什么没有ASI，因为我也没有这个数据集的权限。其他的数据集我相信也会有一定的效果，但是我还是十分建议你先在labs上对数据进行分析研究，而不是无脑的跑模板。

1.首先我们需要找到这样的alpha


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Created 05/01/2025 EDT
> anonymous
> Udd Mpha tO
> Lst
> Alphas
> Unsubmitted
> Openalpha details in newtab
> Aggregate Data
> 5harDE
> TUrnover
> Fitness
> Re-Urns
> Drawidowin
> Warsin
> Size
> OUL OT
> 1.92
> 34.089
> 0.70
> 4.539
> 2.429
> 2.669600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Select Columns
> Name
> Competition
> Type
> Date Created
> 2013
> 36,75{
> 0,50
> 3.9435
> 1.1795
> 2.143oc
> 500
> 496
> Search
> Selec
> Regular
> 05/01/2025
> 2014
> 2.43
> 35,153
> 0,95
> 5.1395
> 0335
> 923occ
> 553
> 553
> anonymous
> Regular
> 05/01/2025
> 2015
> 34,951
> 0.56
> 983
> 263
> 2.233oc
> 525
> 530
> 2016
> 0.23
> 35,38{
> 0,03
> 0.5335
> 9235
> 303occ
> 570
> 53'
> 2017
> 3.19
> 33.953
> 5.9095
> 0.9535
> 433o0c
> 708
> 725
> 2018
> 0.42
> 33,381
> 0,07
> .88驮
> 2.-23
> 0.533o
> 794
> 780
> 2019
> 3.11
> 33.035
> 1,40
> 5.733
> 1.193
> 1.073occ
> 829
> 78'
> 2020
> 2.99
> 31,153
> 1,51
> 8.2635
> 5095
> 5.303oc
> 331
> 301
> 2021
> 101
> 35,303
> 2.15
> 10.319
> 0.1795
> 5.7G3occ
> 876
> 875
> 2021
> 1.21
> 33.595
> 0,38
> 3.38%
> 1.173
> 2.013occ
> 1125
> 1070
> 2022
> 2.52
> 33.335
> 1.23
> 7.363
> 0.923
> 1.413oc
> 1230
> 1176
> 2023
> 31,323
> -2.45
> 10.6195
> 6245
> 733occ
> 1223
> 1220
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RezUrns
> Drawdown
> Marsin
> 2.24
> 34.089
> 0.82
> 4.609
> 2.029
> 2.709600
> Page


2. 然后将其用到的字段名复制下来，在Data上搜索


> [!NOTE] [图片 OCR 识别内容]
> 40QL
> 鬯
> Simulate
> C Alphas
> Learn
> Data
> 器
> Labs
> Genius
> 智
> Competitions (4)
> Community
> y Refer a friend
> Region
> Delay
> Universe
> USA
> T0P3000
> What data do you want to find?
> mcr27_
> company_jobsactivel
> Search
> Fields
> The number of active job postings by the company。
> mcrz7_company_jobsactive in Job records from job posting
> Show all matching fields
> Datasets
> mid theme multipliers
> No datasets found by quick search
> Analyst
> Showallmatching datasets
> TCe
> Value score: 4
> Value score: 6
> Value score: 5
> Value score:
> Datasets: 38
> Datasets: 9
> Datasets: 36
> Datasets:
> Fields: 11618
> Fields: 251
> Fields: 20081
> Fields: 3
> Regions: AMR, ASI, CHN,EUR, GLB,
> Regions: AMR, ASI,CHN EUR, GLB
> Regions: AMR, ASL, CHN, EUR, GLB,
> Regions: USA
> JPN,USA
> JPN,USA
> JPN,USA


3. 点击搜索后得到下面的结果


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Search result
> USA
> TOP3000
> Fields
> Datasets
> Search
> Theme
> Coverage
> Type
> Alphas
> Users
> mcrz7_company_jol
> 100
> Clear
> Dataset
> Field
> Description
> Vpe
> Pyramid
> Coverage
> Users
> Alphas
> Theme
> Multiplier
> Iobrecords trom job posting
> mcrz7_bucket_monthly_jobsa
> The number of active jobs postings bythe
> Vector
> 51 %
> ctive
> Company。
> mcrz7_bucket_daily_jobsactiv
> The number of active job postings by the
> Vector
> 50%
> 192
> 540
> Company
> mcrz7_daily_sdioc
> The number of company IDs with active jobs
> Vector
> 50%
> in the Same macro bUCket。
> mCrz7_monthly_sdioc
> The number of company IDs with active jobs
> Vector
> i the Same IaCro DUICKet
> mCr27_bUcket_daily_jobsactiv
> The number of active jobs postings bythe
> Vector
> 4996
> company,after neutralizationinthe
> respective macro bucket
> mCr27_bUcket_monthly_jobsa
> The number of active jobs postings bythe
> Vector
> 4996
> ctive_n
> company,after neutralizationinthe
> respective macro bucket
> mCrz7_daily_jr_sdioc
> The number of company IDs inthe same
> Vector
> 45%6
> macro bucket that have removed jobs since
> the last scraping:
> mCrz7_daily_jc_sdioc
> The number of company IDs inthe same
> Vector
> 4596
> macro bucket that have created jobs since the
> last scraping:
> mcrz7_bucket_daily_jobsremo
> The number ofjob postings removed by the
> Vector
> 459
> Ved
> company
> ICrz7 DUCez monthl ObSI
> The number ofiob postines remoyed by the
> Vector


一般第一个就是你要的那个字段，之后点进去再找到下面的Visualiaze Field


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Job records from job posting
> mcrz7_bucket_monthly_jobsactive
> USA
> TOP3000
> Simulate Field
> Visualize Field
> Field description
> Category: Macro
> Macroeconomic Activities
> Type: Vector
> The number of active jobs postings by the company.
> Region
> Delay
> Universe
> Pyramid Theme
> Theme
> Coverage
> Users
> Alphas
> Multiplier
> USA
> T0P3000
> 519
> Show all settings
> Data field visualizationincludes:
> Whatis the range ofvalues and theirfrequency?
> How Uothe Values Vany Dy SECtor?
> How does the distribution Vary overtime?
> How often do Values update?
> What % Ofvalues are NaNOrZero?
> And more。
> 黟^
> Visualize Field


4.开始分析数据

这里我们发现这个数据字段是大量的0值的，这种情况我们的ts_backfill是没有办法进行填充的，所以我们在这之前需要先 to_nan 一下  ，例 : ts_backfill(to_nan({data_filed}),60)


> [!NOTE] [图片 OCR 识别内容]
> What is the range of mcr27_
> bucket_monthly_jobsactive Values
> their frequency?
> L2N
> IM
> Linear Axes
> 08N
> Log X-Axis
> 
> 0.GN
> Y-Axis
> 0AM
> Log-Log Axes
> 0.2N
> SOK
> I0OK
> 15Ok
> 20Or
> 25OK
> TIP
> and
> Log


简单的处理之后turnover会有明显的下降，两个alpha之间唯一的区别就是有没有加to_nan，下面的图因为我改了一下decay，所以和刚找的alpha有一点点不太一样（是的，难以想象只是改了一下decay，turnover居然高了这么多）


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Date Created (EST)
> Region
> Delay
> Neutralization
> Sharpe
> Returns
> Turnover
> Margin
> Fitness
> Color
> Search
> Seec
> Regular
> 08/30/2025
> 08/31/
> USA
> Selec
> e.g>
> e.g>
> Pg
> e.g>
> e.g>
> Purple
> anOIYMOUS
> RegUlaT
> 08/31/2025 EDT 
> USA
> Subindustry
> +94
> 4.5596
> 34.09%6
> 2.67960c
> 0.71
> Purple
> anOIYMOUS
> RegUlaT
> 08/31/2025 EDT 
> USA
> Subindustry
> 1.61
> 4.73%6
> 75.78%
> 1.25960c
> 0.40
> Purple


一个简简单单的0值处理成nan，就把turnover降了一半，同时sharp和return都有一定的提升

5.发现异常值，对异常值进行处理


> [!NOTE] [图片 OCR 识别内容]
> (3.685.465,1.307732N)
> L2N
> IN
> Linear Axes
> 08N
> X-AxIs
> 
> 0.GN
> YAxis
> 04l
> Log-Log Axes
> 02N1
> In
> TV
> 0.001
> 1000
> IN
> Value
> Log
> Log



> [!NOTE] [图片 OCR 识别内容]
> What are the key statistical characteristics (min, max; mean, median, and quantiles) of the mcr27
> BOK
> M
> Mean
> Da
> median
> GOK
> 25th_quantile
> 75th_quantile
> `
> 4OK
> ZOK
> 9
> 2014
> 2015
> 2018
> 2020
> 2022
> Date


在这里我尝试了ts_quantile和winsorize，发现ts_quantile的效果要更好

至此，数据处理的环节就完成了

例：ts_quantile(ts_backfill(to_nan({datafield}),60), 5, driver=gaussian)

6.将处理好的数据放入一二三阶框架中直接运行，就能得到不错的效果，我尝试了一二（先时序处理再横截面处理）和二一（先横截面处理再时序处理），目前来看一二的效果比较好（时序处理：ts；横截面处理：group）

7.最后展示一下结果（USA)


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 12/30/2022
> Test Pnl: 4,952.33k
> DOOK
> 3.0OOk
> Z.0OOK
> DOOK



> [!NOTE] [图片 OCR 识别内容]
> Single Data Set Alpha
> Power Pool Alpha
> Pyramidtheme: USADIIMACRO X1.1
> Aggre
> Data
> SharDE
> Turnover
> Fitness
> Rezurns
> Drawdowin
> Marsin
> 2.00
> 12.209
> 1.27
> 5.01%
> 2.229
> 8.229600
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.30
> 12.493
> 0.53
> 2.479
> 539
> 3,959230
> 1493
> 1598
> 2014
> 2.17
> 11.925
> 1.27
> 4,309
> 269
> 7.229230
> 1472
> 1526
> 2015
> 212
> 12.153
> 1.31
> 4.7936
> 163
> 885230
> 1453
> 1576
> 2016
> 0,33
> 11.525
> 0.08
> 0.719
> 1,213
> 229330
> 444
> 1586
> 2017
> 2.23
> 11.991
> 1.37
> 4.719
> 629
> 869330
> 505
> 1597
> 2018
> 1,61
> 12.50
> 0.85
> 3,48%
> 28%
> 585330
> 553
> 1553
> 2019
> 3.35
> 12.13{
> 2.-3
> ,503
> 974
> 10,3753
> 430
> 1529
> 2020
> 3,67
> 12.435
> 3.69
> 12.519
> 1.799
> 20.299330
> 1573
> 1525
> 2021
> -1,50
> 13.531
> 0.96
> -5.549
> 0.56%
> 68po
> 534
> 1468
> 2021
> 1.51
> 12.73{
> 0.97
> 5.243
> 2.20%
> 8.2-So30
> 1705
> 2022
> 2.00
> 11.9535
> 1.33
> 5.923
> 1.103
> 895330
> 1431
> 1675
> 2023
> 3,88
> 13.251
> 3.34
> ,849
> 14,839330
> 404
> 1772
> egate
> Year
> 147


不算特别好，但只是简单处理了一下数据，就能得到一个还不是“死鱼”的Alpha，还算不错  （注：死鱼是weijie老师的一个梗，暗指turnover小于5的Alpha）

最后的最后，大家还能结合一下MCP找到一些有意思的处理方式，下面抛砖引玉

### 1. 时间序列特征明显

- 数据有明显的趋势变化（2018年末转折点）

- 存在周期性波动和异常尖峰

- 推荐operators：

- ts_delta - 捕捉趋势变化

- ts_rank - 处理时间序列排序

- ts_zscore - 标准化处理异常值

- ts_returns - 计算收益率变化

### 2. 异常值处理需求

- 数据中存在显著的异常尖峰

- 分布从集中变为高度偏斜

- 推荐operators：

- ts_quantile - 分位数处理，减少异常值影响

- ts_skewness - 检测偏度变化

- ts_std_dev - 标准差，识别异常波动

- ts_entropy - 信息熵，检测分布变化

### 3. 分布特征变化

- 从稳定分布变为高度偏斜

- 不同时期数据特征差异巨大

- 推荐operators：

- rank - 排序，处理分布偏斜

- zscore - 标准化

- quantile - 分位数变换

- normalize - 归一化处理

### 4. 多实体比较

- 不同实体表现差异显著

- 推荐operators：

- group_rank - 分组排序

- group_mean - 分组均值

- group_std_dev - 分组标准差

### 组合1：异常值稳健处理

ts_quantile(ts_zscore(mcr27, 22), 22, driver='gaussian')

### 组合2：趋势捕捉

ts_delta(ts_rank(mcr27, 66), 5)

### 组合3：分布标准化

rank(ts_std_dev(mcr27, 120))

### 组合4：分组比较

group_rank(ts_mean(mcr27, 22), densify(sector))

如果你觉得写得还不错，麻烦给个宝贵的赞，这将是对我最大的鼓励！！

**顾问 WX64154 (Rank 32) 的解答与建议**:
to_nan的操作符权限Gold好像没有


---

### 技术对话片段 5 (原帖: 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享_34584423754263.md
- **时间**: 9个月前

**提问/主帖背景 (ML42552)**:
还记得weijie老师上课说过的一句话，一些sharp很高，turnover也很高的alpha是非常具有价值的，然后当时我就找到了下面这个alpha，并在labs上对其数据进行了分析。

本文讲的相对比较详细，建议新手务必认真读完，模板在本文的最下面，经过验证可以，在USA，GLB，EUR 三个大区都有不错的效果，至于你问我为什么没有ASI，因为我也没有这个数据集的权限。其他的数据集我相信也会有一定的效果，但是我还是十分建议你先在labs上对数据进行分析研究，而不是无脑的跑模板。

1.首先我们需要找到这样的alpha


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Created 05/01/2025 EDT
> anonymous
> Udd Mpha tO
> Lst
> Alphas
> Unsubmitted
> Openalpha details in newtab
> Aggregate Data
> 5harDE
> TUrnover
> Fitness
> Re-Urns
> Drawidowin
> Warsin
> Size
> OUL OT
> 1.92
> 34.089
> 0.70
> 4.539
> 2.429
> 2.669600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Select Columns
> Name
> Competition
> Type
> Date Created
> 2013
> 36,75{
> 0,50
> 3.9435
> 1.1795
> 2.143oc
> 500
> 496
> Search
> Selec
> Regular
> 05/01/2025
> 2014
> 2.43
> 35,153
> 0,95
> 5.1395
> 0335
> 923occ
> 553
> 553
> anonymous
> Regular
> 05/01/2025
> 2015
> 34,951
> 0.56
> 983
> 263
> 2.233oc
> 525
> 530
> 2016
> 0.23
> 35,38{
> 0,03
> 0.5335
> 9235
> 303occ
> 570
> 53'
> 2017
> 3.19
> 33.953
> 5.9095
> 0.9535
> 433o0c
> 708
> 725
> 2018
> 0.42
> 33,381
> 0,07
> .88驮
> 2.-23
> 0.533o
> 794
> 780
> 2019
> 3.11
> 33.035
> 1,40
> 5.733
> 1.193
> 1.073occ
> 829
> 78'
> 2020
> 2.99
> 31,153
> 1,51
> 8.2635
> 5095
> 5.303oc
> 331
> 301
> 2021
> 101
> 35,303
> 2.15
> 10.319
> 0.1795
> 5.7G3occ
> 876
> 875
> 2021
> 1.21
> 33.595
> 0,38
> 3.38%
> 1.173
> 2.013occ
> 1125
> 1070
> 2022
> 2.52
> 33.335
> 1.23
> 7.363
> 0.923
> 1.413oc
> 1230
> 1176
> 2023
> 31,323
> -2.45
> 10.6195
> 6245
> 733occ
> 1223
> 1220
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RezUrns
> Drawdown
> Marsin
> 2.24
> 34.089
> 0.82
> 4.609
> 2.029
> 2.709600
> Page


2. 然后将其用到的字段名复制下来，在Data上搜索


> [!NOTE] [图片 OCR 识别内容]
> 40QL
> 鬯
> Simulate
> C Alphas
> Learn
> Data
> 器
> Labs
> Genius
> 智
> Competitions (4)
> Community
> y Refer a friend
> Region
> Delay
> Universe
> USA
> T0P3000
> What data do you want to find?
> mcr27_
> company_jobsactivel
> Search
> Fields
> The number of active job postings by the company。
> mcrz7_company_jobsactive in Job records from job posting
> Show all matching fields
> Datasets
> mid theme multipliers
> No datasets found by quick search
> Analyst
> Showallmatching datasets
> TCe
> Value score: 4
> Value score: 6
> Value score: 5
> Value score:
> Datasets: 38
> Datasets: 9
> Datasets: 36
> Datasets:
> Fields: 11618
> Fields: 251
> Fields: 20081
> Fields: 3
> Regions: AMR, ASI, CHN,EUR, GLB,
> Regions: AMR, ASI,CHN EUR, GLB
> Regions: AMR, ASL, CHN, EUR, GLB,
> Regions: USA
> JPN,USA
> JPN,USA
> JPN,USA


3. 点击搜索后得到下面的结果


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Search result
> USA
> TOP3000
> Fields
> Datasets
> Search
> Theme
> Coverage
> Type
> Alphas
> Users
> mcrz7_company_jol
> 100
> Clear
> Dataset
> Field
> Description
> Vpe
> Pyramid
> Coverage
> Users
> Alphas
> Theme
> Multiplier
> Iobrecords trom job posting
> mcrz7_bucket_monthly_jobsa
> The number of active jobs postings bythe
> Vector
> 51 %
> ctive
> Company。
> mcrz7_bucket_daily_jobsactiv
> The number of active job postings by the
> Vector
> 50%
> 192
> 540
> Company
> mcrz7_daily_sdioc
> The number of company IDs with active jobs
> Vector
> 50%
> in the Same macro bUCket。
> mCrz7_monthly_sdioc
> The number of company IDs with active jobs
> Vector
> i the Same IaCro DUICKet
> mCr27_bUcket_daily_jobsactiv
> The number of active jobs postings bythe
> Vector
> 4996
> company,after neutralizationinthe
> respective macro bucket
> mCr27_bUcket_monthly_jobsa
> The number of active jobs postings bythe
> Vector
> 4996
> ctive_n
> company,after neutralizationinthe
> respective macro bucket
> mCrz7_daily_jr_sdioc
> The number of company IDs inthe same
> Vector
> 45%6
> macro bucket that have removed jobs since
> the last scraping:
> mCrz7_daily_jc_sdioc
> The number of company IDs inthe same
> Vector
> 4596
> macro bucket that have created jobs since the
> last scraping:
> mcrz7_bucket_daily_jobsremo
> The number ofjob postings removed by the
> Vector
> 459
> Ved
> company
> ICrz7 DUCez monthl ObSI
> The number ofiob postines remoyed by the
> Vector


一般第一个就是你要的那个字段，之后点进去再找到下面的Visualiaze Field


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Job records from job posting
> mcrz7_bucket_monthly_jobsactive
> USA
> TOP3000
> Simulate Field
> Visualize Field
> Field description
> Category: Macro
> Macroeconomic Activities
> Type: Vector
> The number of active jobs postings by the company.
> Region
> Delay
> Universe
> Pyramid Theme
> Theme
> Coverage
> Users
> Alphas
> Multiplier
> USA
> T0P3000
> 519
> Show all settings
> Data field visualizationincludes:
> Whatis the range ofvalues and theirfrequency?
> How Uothe Values Vany Dy SECtor?
> How does the distribution Vary overtime?
> How often do Values update?
> What % Ofvalues are NaNOrZero?
> And more。
> 黟^
> Visualize Field


4.开始分析数据

这里我们发现这个数据字段是大量的0值的，这种情况我们的ts_backfill是没有办法进行填充的，所以我们在这之前需要先 to_nan 一下  ，例 : ts_backfill(to_nan({data_filed}),60)


> [!NOTE] [图片 OCR 识别内容]
> What is the range of mcr27_
> bucket_monthly_jobsactive Values
> their frequency?
> L2N
> IM
> Linear Axes
> 08N
> Log X-Axis
> 
> 0.GN
> Y-Axis
> 0AM
> Log-Log Axes
> 0.2N
> SOK
> I0OK
> 15Ok
> 20Or
> 25OK
> TIP
> and
> Log


简单的处理之后turnover会有明显的下降，两个alpha之间唯一的区别就是有没有加to_nan，下面的图因为我改了一下decay，所以和刚找的alpha有一点点不太一样（是的，难以想象只是改了一下decay，turnover居然高了这么多）


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Date Created (EST)
> Region
> Delay
> Neutralization
> Sharpe
> Returns
> Turnover
> Margin
> Fitness
> Color
> Search
> Seec
> Regular
> 08/30/2025
> 08/31/
> USA
> Selec
> e.g>
> e.g>
> Pg
> e.g>
> e.g>
> Purple
> anOIYMOUS
> RegUlaT
> 08/31/2025 EDT 
> USA
> Subindustry
> +94
> 4.5596
> 34.09%6
> 2.67960c
> 0.71
> Purple
> anOIYMOUS
> RegUlaT
> 08/31/2025 EDT 
> USA
> Subindustry
> 1.61
> 4.73%6
> 75.78%
> 1.25960c
> 0.40
> Purple


一个简简单单的0值处理成nan，就把turnover降了一半，同时sharp和return都有一定的提升

5.发现异常值，对异常值进行处理


> [!NOTE] [图片 OCR 识别内容]
> (3.685.465,1.307732N)
> L2N
> IN
> Linear Axes
> 08N
> X-AxIs
> 
> 0.GN
> YAxis
> 04l
> Log-Log Axes
> 02N1
> In
> TV
> 0.001
> 1000
> IN
> Value
> Log
> Log



> [!NOTE] [图片 OCR 识别内容]
> What are the key statistical characteristics (min, max; mean, median, and quantiles) of the mcr27
> BOK
> M
> Mean
> Da
> median
> GOK
> 25th_quantile
> 75th_quantile
> `
> 4OK
> ZOK
> 9
> 2014
> 2015
> 2018
> 2020
> 2022
> Date


在这里我尝试了ts_quantile和winsorize，发现ts_quantile的效果要更好

至此，数据处理的环节就完成了

例：ts_quantile(ts_backfill(to_nan({datafield}),60), 5, driver=gaussian)

6.将处理好的数据放入一二三阶框架中直接运行，就能得到不错的效果，我尝试了一二（先时序处理再横截面处理）和二一（先横截面处理再时序处理），目前来看一二的效果比较好（时序处理：ts；横截面处理：group）

7.最后展示一下结果（USA)


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 12/30/2022
> Test Pnl: 4,952.33k
> DOOK
> 3.0OOk
> Z.0OOK
> DOOK



> [!NOTE] [图片 OCR 识别内容]
> Single Data Set Alpha
> Power Pool Alpha
> Pyramidtheme: USADIIMACRO X1.1
> Aggre
> Data
> SharDE
> Turnover
> Fitness
> Rezurns
> Drawdowin
> Marsin
> 2.00
> 12.209
> 1.27
> 5.01%
> 2.229
> 8.229600
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.30
> 12.493
> 0.53
> 2.479
> 539
> 3,959230
> 1493
> 1598
> 2014
> 2.17
> 11.925
> 1.27
> 4,309
> 269
> 7.229230
> 1472
> 1526
> 2015
> 212
> 12.153
> 1.31
> 4.7936
> 163
> 885230
> 1453
> 1576
> 2016
> 0,33
> 11.525
> 0.08
> 0.719
> 1,213
> 229330
> 444
> 1586
> 2017
> 2.23
> 11.991
> 1.37
> 4.719
> 629
> 869330
> 505
> 1597
> 2018
> 1,61
> 12.50
> 0.85
> 3,48%
> 28%
> 585330
> 553
> 1553
> 2019
> 3.35
> 12.13{
> 2.-3
> ,503
> 974
> 10,3753
> 430
> 1529
> 2020
> 3,67
> 12.435
> 3.69
> 12.519
> 1.799
> 20.299330
> 1573
> 1525
> 2021
> -1,50
> 13.531
> 0.96
> -5.549
> 0.56%
> 68po
> 534
> 1468
> 2021
> 1.51
> 12.73{
> 0.97
> 5.243
> 2.20%
> 8.2-So30
> 1705
> 2022
> 2.00
> 11.9535
> 1.33
> 5.923
> 1.103
> 895330
> 1431
> 1675
> 2023
> 3,88
> 13.251
> 3.34
> ,849
> 14,839330
> 404
> 1772
> egate
> Year
> 147


不算特别好，但只是简单处理了一下数据，就能得到一个还不是“死鱼”的Alpha，还算不错  （注：死鱼是weijie老师的一个梗，暗指turnover小于5的Alpha）

最后的最后，大家还能结合一下MCP找到一些有意思的处理方式，下面抛砖引玉

### 1. 时间序列特征明显

- 数据有明显的趋势变化（2018年末转折点）

- 存在周期性波动和异常尖峰

- 推荐operators：

- ts_delta - 捕捉趋势变化

- ts_rank - 处理时间序列排序

- ts_zscore - 标准化处理异常值

- ts_returns - 计算收益率变化

### 2. 异常值处理需求

- 数据中存在显著的异常尖峰

- 分布从集中变为高度偏斜

- 推荐operators：

- ts_quantile - 分位数处理，减少异常值影响

- ts_skewness - 检测偏度变化

- ts_std_dev - 标准差，识别异常波动

- ts_entropy - 信息熵，检测分布变化

### 3. 分布特征变化

- 从稳定分布变为高度偏斜

- 不同时期数据特征差异巨大

- 推荐operators：

- rank - 排序，处理分布偏斜

- zscore - 标准化

- quantile - 分位数变换

- normalize - 归一化处理

### 4. 多实体比较

- 不同实体表现差异显著

- 推荐operators：

- group_rank - 分组排序

- group_mean - 分组均值

- group_std_dev - 分组标准差

### 组合1：异常值稳健处理

ts_quantile(ts_zscore(mcr27, 22), 22, driver='gaussian')

### 组合2：趋势捕捉

ts_delta(ts_rank(mcr27, 66), 5)

### 组合3：分布标准化

rank(ts_std_dev(mcr27, 120))

### 组合4：分组比较

group_rank(ts_mean(mcr27, 22), densify(sector))

如果你觉得写得还不错，麻烦给个宝贵的赞，这将是对我最大的鼓励！！

**顾问 WX64154 (Rank 32) 的解答与建议**:
to_nan的操作符权限Gold好像没有


---

### 技术对话片段 6 (原帖: 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk72（1个字段3个atom）Alpha Template)
- **原帖链接**: [Commented] 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk721个字段3个atomAlpha Template.md
- **时间**: 9个月前

**提问/主帖背景 (LR93609)**:
**根据本人当前权限：** CHN中的risk72仅有1个字段rsk72_atop2000_dsrt（Daily reproducible specific returns in % units）。

**一、根据对字面的理解：** 每日可复制特定收益率（以百分比为单位）。

1. 提交的alpha相对比较多，用户也多；

2. 内在质素是不错的，优于大多数字段；

3. 具有通过多种组合，生成有效alpha的潜质。

**
> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Specific return of extended factors
> rsk72_atopzooo_dsrt
> CHN
> TOPZOOOU
> Simulate Field
> 罟
> Visualize Field
> Field description
> Category: Risk _
> Risk Factors
> Type: Matrix
> Daily reproducible specific returns in % units
> Region
> Delay
> Unjverse
> Fyramid Theme
> Theme
> Coverage
> Users
> Alphas
> Multiplier
> CHN
> TOPZOOOU
> 1003
> 135
> 444
**

**二、对其数据结构分析：** 可视化来自于BRAIN labs和Simulation

**1. 接近于正态分布**

**
> [!NOTE] [图片 OCR 识别内容]
> Distribution of rsk72_atop2000_dsrt values
> 250000
> 200000
> 150000
> 
> 100000
> 50000
> 0.4
> 20.3
> 0,2
> 01
> 00
> 01
> 0,2
> Value
**

**2. 不同时期不同industry分布过于密集，而且极值较多**


> [!NOTE] [图片 OCR 识别内容]
> Country Tield 0f
> brain.
> data Trame(brain.get data Tield(industpy")
> universe=T02280OU
> 0at25
> (>
> 7021-81-01]
> 0 ^ I 古 =_
> ClOSe Tield dT
> brazn.get
> 03ta
> frame (brain.get_data_field("rsk72_at0p2880_dsrt),
> universe= T0P200gU"
> gates (>
> 2821-81-01")]]
> Visualizations.plot_group_statistics
> data Tield 0T
> Close Tield_dT,
> 9roup_Of
> Country field dT,
> Average O rsk 72_alopz000_dsrtIn Industry
> 008
> 006
> 0C
> 002
> 
> 000
> 一0.02
> 0.04
> -0,06
> 2021-01
> 2021-0+
> 2021-07
> 202110
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Uae
> Ndvertising
> Ch-mic-ls
> Fnvironm-ntl Conrol
> HolsEhold Producrs 5 {res
> M-ra
> Fbrcahon 5 Hardare
> Real Estate
> Nerospace 6 Uefense
> Coal
> Hooo
> HUSeMare5
> Mning
> Heal
> Agnculture
> Commercial Serices
> Fooo Sernce
> ISUTanCe
> NISCellanegus
> Manufacturing
> Smlconductors
> AITIIICS
> CompUters
> FOIest ProJucts G Papel
> DerC
> OIIIce & 3uslness Equpmen。
> Spbullding
> Jlterrauve Energy
> CosIeLIs & PersonulCare
> Gus
> IICSIILII
> Corrpunles
> Otfice Furnlshings
> SltwJl
> Apoarel
> Oisrioution G Wholesale
> Hand & Machne Tools
> Iron & Steel
> 01G Gas
> Storaye 5 Warehousing
> AUO Manufacturers
> DNerstfed Fnancal Sericss
> Iealthcare Procrs
> LeIsUre Time
> 015Gas Sennices
> Telecommmncatons
> AUITO PTts G Fauinmen;
> Elsctrc
> Healthcare Sences
> lodqing
> Pckaqing & Contaners
> Texiles
> Banks
> Clectncal Components 6 Lqupment
> Holding Companles Diversified
> Machinery Consructon & Minng
> MhammaceUlcals
> Toys, Games & hoboies
> Beverages
> Electronics
> Home Bullders
> Machinery Dwversified
> ppelines
> Transportation
> Biotechnology
> Enginesring 6 Consructon
> Homs Hurnishings
> Madia
> Privare Fquin
> Wter
> OIIIIIII
> get


3. 日均换手率极高，且存在波动性


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Turnover
> 903
> 80
> 703
> 6093
> 12/0212022
> OVeT
> 59,043
> 509
> 403
> 303
> 203
> 103
> an '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23


**三、应用举例**

**1. 直接缩放（建议精力旺盛的小伙伴多调试，当时为了卡时间，相对粗糙）**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 08/30/2025 EDT
> anonymoUs
> udd Alphato
> List
> Code
> IS Summary
> Period
> a=-rsk72_atopzoBg_dsrt;
> Ksinale Data Set Alpha
> K Power Pool Alpha
> Pyramidtheme: CHNIDIIRISK X14
> b=signed_power(a,0
> Aggregate Data
> Sharpe
> TUICnOEI
> itmess
> REIICns
> Cpatm
> Marein
> 1.09
> 66.299
> 0.37
> 7.529
> 36.579
> 2.279600
> simulation Settings
> Instrument Type
> Region
> UnNerse
> LangUage
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> Sharpe
> TUINOVeT
> Ftness
> Returns
> Drawdow
> Marqin
> Count
> Short Cownt
> Equi?
> CHN
> TOPZJOOU
> Fast Expression
> 0.03
> RAN
> 2013
> 452
> 54.15*
> 3.18
> 25.774
> 3295
> 539
> 507
> -33
> 2014
> 5.-9
> 57.53*
> 一5
> 31.034
> 2991
> 10.7692
> 502
> 2015
> 0.83
> 56.75*
> 0.38
> -12.5095
> 33.2993
> 7392
> 075
> 933
> 2016
> 0.45
> 59.35北
> 0.10
> 234
> 4593
> 9293
> 007
> 9933
> Clone Alpha
> 201
> 1
> 55.25*
> 3.054
> 1.339
> 949323
> 335
> 1023
> 2013
> 41
> 50.90;
> 0.08
> 2074
> 1093
> 539
> 930
> 1011
> N Chart
> Pnl
> 2019
> 57.84*
> 5304
> 4.8295
> 55933
> 335
> 1015
> 2020
> 0.29
> 72.974
> 0.04
> 1.751:
> 3591
> 439323
> 934
> 1011
> 2021
> 73.52*
> 0.31
> 11.224
> 3693
> 0592
> 932
> 1023
> 202
> 73.55沁
> 14
> 7.714
> 1.3191
> 109323
> 933
> 1011
> 2023
> 70.53*
> 5.541
> 0.5093
> 609333
> 345
> 1055
> OOOK
> 20OOK
> 医 Correlation
> Self Correlation
> LIam IF
> IinimFT
> T
> TII:
> Jan'14
> Jan '15
> Jan'16
> Jan'17
> Jan'13
> Jan '19
> Jan '20
> Jan 21
> J3n'22
> Jan '23
> 25);
> Lono
> VeriN


**2. 波动率放大（推荐）**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 08/30/2025 EDT
> 0830-submitable
> Add Alphato
> List
> Code
> IS Summary
> Period
> 05
> a=rsk72_
> atopzggg_dsnt;
> Asinale Data Set Alpha
> M
> Power Pool Alpha
> Pyramidtheme: CHNIDIIRISK X14
> b-ts_std_dev(a,
> 252);
> 5igned_power(b
> Aggregate Data
> Sharpe
> Turnove
> FrnEss
> ReTUTn
> Oraa
> Marein
> 1.09
> 5.689
> 1.25
> 16.469
> 42.54%
> 57.9
> 900
> Simulation Settings
> Instrument Type
> Region
> Unjverse
> LangUaqe
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> TUIOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Cownt
> Equiz
> CHN
> TOPZDOOU
> Fast ExPression
> 0.05
> Crowing Factors
> Verify
> 2013
> 042
> 5.70*
> 0.27
> 5.2395
> 00*
> 13.354
> 536
> 390
> 2014
> 4沁
> .1391
> 14.16*
> 70.045
> 75
> 11
> 2015
> 5.75*
> 36.7795
> 42.54光
> 123.004
> 1135
> 313
> 2016
> 5.75*
> 13.1193
> 82光
> 62.955
> 1133
> Clone Alpha
> 201
> 2.73
> 3沁
> 4.95
> 41.159
> 6.33沁
> 153.555
> 1258
> 743
> 2013
> 132
> 99光
> 1.71
> 20.9393
> 17.72北
> 10-.845
> 1233
> 713
> Chart
> Pnl
> 2019
> 09沁
> 2.35
> 二7.5491
> 13.63沁
> 134.535
> 1258
> 743
> 2020
> 93沁
> 20.0591
> 10.95*
> 67.135
> 1256
> 735
> 2021
> 60兆
> 21.3793
> 13.51兆
> 64.79*
> 1134
> 311
> 202
> 7.21沁
> 2.30
> 1.3291
> 12.55*
> 63.105
> 1154
> 340
> IOM
> 2023
> 63;
> 0.15
> 3.2195
> 09*
> 9.515
> 1151
> 33
> OOOK
> Correlation
> Self Correlation
> Iam IFT
> Ninimum
> Lt RIn:
> Jan'14
> Jan '15
> Jan'16
> Jan '17
> jan '18
> Jan '19
> Jan'20
> Jan 21
> J3n'22
> Jan '23
> Sharpe
> Lono


**3. 反转并缩放（倍数过小，不鼓励）**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 08/30/2025 EDT
> anonymoUs
> Add Alphato
> List
> Code
> IS Summary
> Period
> 05
> a=rsk72_atop2oOB_dsnt;
> Asinale Data Set Alpha
> Power Pool Alpha
> Pyramidtheme: CHNIDIIRISK X14
> breverse(ts_delta
> 53)
> sqrt(inst
> tvp
> 126 )
> signed_power (b,8
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> REIICns
> Cpat
> Marein
> 1.18
> 42.96%
> 0.46
> 6.41%
> 13.6096
> 2.9
> Simulation Settings
> Instrument Type
> Region
> Unjverse
> LangUaqe
> Decay
> Delay
> Truncation
> Neutralizatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> Sharpe
> TUIIOVeT
> Ftnoss
> Returns
> Drawdow
> Wargin
> Count
> Short Cownt
> Equiz
> CHN
> TOPZDOOU
> Fast Expression
> SIOW Facors
> Verify
> 2013
> 2.31
> 35.314
> 1.73
> 14.5093
> 3093
> 5Foo
> 495
> 501
> 2014
> 3.14
> 33.371
> 1.30
> 12.5493
> 1.-591
> 53530
> 59
> 535
> 2015
> 0.15
> 41.334
> 003
> 3893
> 13.1993
> GEoDD
> 390
> 1003
> 2016
> 1.23
> 45.334
> 4393
> 1-295
> 338o
> 002
> 1003
> Clone Alpha
> 201
> 0.44
> 42.371
> 0.03
> 7591
> 3.4893
> 0.325200
> 1013
> 935
> 2013
> 1.73
> 40.14*
> 0.75
> 7.2395
> 3.0595
> 535320
> 391
> 1007
> Chart
> Pnl
> 2019
> 1.75
> 4-.741
> 0.73
> 3091
> 1.3291
> 496oo
> 004
> 937
> 2020
> -0.62
> 45.301
> 0.13
> 3.8593
> 6.2191
> 535200
> 391
> 1010
> 2021
> 114
> 45.554
> 3693
> 5493
> 7356o
> 386
> 1013
> 202
> 47.231
> 0.93
> 52N
> 3.449
> 03530
> 1000
> 1004
> COOOK
> 2023
> 0.35
> 47.51
> 2.4991
> 0.5791
> 055oo
> 373
> 1025
> OOOK
> Correlation
> Self Correlation
> Iam IFT
> Ninimum
> Lt RIn:
> Jan '14
> Jan '15
> an'16
> Jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan 21
> J3n'22
> Jan '23
> 89600
> Lono


**四、总结概述**

1. 数据分析是因子挖掘的基本功， **数据本身研究的越透，越高效** ；

2. 因子优劣来自于字段本身的素质， **好字段能组成更多有效因子** ；

3.  **接近正态分布的字段本身就可能是因子** ，简单处理便可以使用。

**顾问 WX64154 (Rank 32) 的解答与建议**:
这曲线有点不大平滑 我有点不大敢交1 这种


---

### 技术对话片段 7 (原帖: 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk72（1个字段3个atom）Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk721个字段3个atomAlpha Template_34715794180247.md
- **时间**: 9个月前

**提问/主帖背景 (LR93609)**:
**根据本人当前权限：** CHN中的risk72仅有1个字段rsk72_atop2000_dsrt（Daily reproducible specific returns in % units）。

**一、根据对字面的理解：** 每日可复制特定收益率（以百分比为单位）。

1. 提交的alpha相对比较多，用户也多；

2. 内在质素是不错的，优于大多数字段；

3. 具有通过多种组合，生成有效alpha的潜质。

**
> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Specific return of extended factors
> rsk72_atopzooo_dsrt
> CHN
> TOPZOOOU
> Simulate Field
> 罟
> Visualize Field
> Field description
> Category: Risk _
> Risk Factors
> Type: Matrix
> Daily reproducible specific returns in % units
> Region
> Delay
> Unjverse
> Fyramid Theme
> Theme
> Coverage
> Users
> Alphas
> Multiplier
> CHN
> TOPZOOOU
> 1003
> 135
> 444
**

**二、对其数据结构分析：** 可视化来自于BRAIN labs和Simulation

**1. 接近于正态分布**

**
> [!NOTE] [图片 OCR 识别内容]
> Distribution of rsk72_atop2000_dsrt values
> 250000
> 200000
> 150000
> 
> 100000
> 50000
> 0.4
> 20.3
> 0,2
> 01
> 00
> 01
> 0,2
> Value
**

**2. 不同时期不同industry分布过于密集，而且极值较多**


> [!NOTE] [图片 OCR 识别内容]
> Country Tield 0f
> brain.
> data Trame(brain.get data Tield(industpy")
> universe=T02280OU
> 0at25
> (>
> 7021-81-01]
> 0 ^ I 古 =_
> ClOSe Tield dT
> brazn.get
> 03ta
> frame (brain.get_data_field("rsk72_at0p2880_dsrt),
> universe= T0P200gU"
> gates (>
> 2821-81-01")]]
> Visualizations.plot_group_statistics
> data Tield 0T
> Close Tield_dT,
> 9roup_Of
> Country field dT,
> Average O rsk 72_alopz000_dsrtIn Industry
> 008
> 006
> 0C
> 002
> 
> 000
> 一0.02
> 0.04
> -0,06
> 2021-01
> 2021-0+
> 2021-07
> 202110
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Uae
> Ndvertising
> Ch-mic-ls
> Fnvironm-ntl Conrol
> HolsEhold Producrs 5 {res
> M-ra
> Fbrcahon 5 Hardare
> Real Estate
> Nerospace 6 Uefense
> Coal
> Hooo
> HUSeMare5
> Mning
> Heal
> Agnculture
> Commercial Serices
> Fooo Sernce
> ISUTanCe
> NISCellanegus
> Manufacturing
> Smlconductors
> AITIIICS
> CompUters
> FOIest ProJucts G Papel
> DerC
> OIIIce & 3uslness Equpmen。
> Spbullding
> Jlterrauve Energy
> CosIeLIs & PersonulCare
> Gus
> IICSIILII
> Corrpunles
> Otfice Furnlshings
> SltwJl
> Apoarel
> Oisrioution G Wholesale
> Hand & Machne Tools
> Iron & Steel
> 01G Gas
> Storaye 5 Warehousing
> AUO Manufacturers
> DNerstfed Fnancal Sericss
> Iealthcare Procrs
> LeIsUre Time
> 015Gas Sennices
> Telecommmncatons
> AUITO PTts G Fauinmen;
> Elsctrc
> Healthcare Sences
> lodqing
> Pckaqing & Contaners
> Texiles
> Banks
> Clectncal Components 6 Lqupment
> Holding Companles Diversified
> Machinery Consructon & Minng
> MhammaceUlcals
> Toys, Games & hoboies
> Beverages
> Electronics
> Home Bullders
> Machinery Dwversified
> ppelines
> Transportation
> Biotechnology
> Enginesring 6 Consructon
> Homs Hurnishings
> Madia
> Privare Fquin
> Wter
> OIIIIIII
> get


3. 日均换手率极高，且存在波动性


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Turnover
> 903
> 80
> 703
> 6093
> 12/0212022
> OVeT
> 59,043
> 509
> 403
> 303
> 203
> 103
> an '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23


**三、应用举例**

**1. 直接缩放（建议精力旺盛的小伙伴多调试，当时为了卡时间，相对粗糙）**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 08/30/2025 EDT
> anonymoUs
> udd Alphato
> List
> Code
> IS Summary
> Period
> a=-rsk72_atopzoBg_dsrt;
> Ksinale Data Set Alpha
> K Power Pool Alpha
> Pyramidtheme: CHNIDIIRISK X14
> b=signed_power(a,0
> Aggregate Data
> Sharpe
> TUICnOEI
> itmess
> REIICns
> Cpatm
> Marein
> 1.09
> 66.299
> 0.37
> 7.529
> 36.579
> 2.279600
> simulation Settings
> Instrument Type
> Region
> UnNerse
> LangUage
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> Sharpe
> TUINOVeT
> Ftness
> Returns
> Drawdow
> Marqin
> Count
> Short Cownt
> Equi?
> CHN
> TOPZJOOU
> Fast Expression
> 0.03
> RAN
> 2013
> 452
> 54.15*
> 3.18
> 25.774
> 3295
> 539
> 507
> -33
> 2014
> 5.-9
> 57.53*
> 一5
> 31.034
> 2991
> 10.7692
> 502
> 2015
> 0.83
> 56.75*
> 0.38
> -12.5095
> 33.2993
> 7392
> 075
> 933
> 2016
> 0.45
> 59.35北
> 0.10
> 234
> 4593
> 9293
> 007
> 9933
> Clone Alpha
> 201
> 1
> 55.25*
> 3.054
> 1.339
> 949323
> 335
> 1023
> 2013
> 41
> 50.90;
> 0.08
> 2074
> 1093
> 539
> 930
> 1011
> N Chart
> Pnl
> 2019
> 57.84*
> 5304
> 4.8295
> 55933
> 335
> 1015
> 2020
> 0.29
> 72.974
> 0.04
> 1.751:
> 3591
> 439323
> 934
> 1011
> 2021
> 73.52*
> 0.31
> 11.224
> 3693
> 0592
> 932
> 1023
> 202
> 73.55沁
> 14
> 7.714
> 1.3191
> 109323
> 933
> 1011
> 2023
> 70.53*
> 5.541
> 0.5093
> 609333
> 345
> 1055
> OOOK
> 20OOK
> 医 Correlation
> Self Correlation
> LIam IF
> IinimFT
> T
> TII:
> Jan'14
> Jan '15
> Jan'16
> Jan'17
> Jan'13
> Jan '19
> Jan '20
> Jan 21
> J3n'22
> Jan '23
> 25);
> Lono
> VeriN


**2. 波动率放大（推荐）**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 08/30/2025 EDT
> 0830-submitable
> Add Alphato
> List
> Code
> IS Summary
> Period
> 05
> a=rsk72_
> atopzggg_dsnt;
> Asinale Data Set Alpha
> M
> Power Pool Alpha
> Pyramidtheme: CHNIDIIRISK X14
> b-ts_std_dev(a,
> 252);
> 5igned_power(b
> Aggregate Data
> Sharpe
> Turnove
> FrnEss
> ReTUTn
> Oraa
> Marein
> 1.09
> 5.689
> 1.25
> 16.469
> 42.54%
> 57.9
> 900
> Simulation Settings
> Instrument Type
> Region
> Unjverse
> LangUaqe
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> TUIOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Cownt
> Equiz
> CHN
> TOPZDOOU
> Fast ExPression
> 0.05
> Crowing Factors
> Verify
> 2013
> 042
> 5.70*
> 0.27
> 5.2395
> 00*
> 13.354
> 536
> 390
> 2014
> 4沁
> .1391
> 14.16*
> 70.045
> 75
> 11
> 2015
> 5.75*
> 36.7795
> 42.54光
> 123.004
> 1135
> 313
> 2016
> 5.75*
> 13.1193
> 82光
> 62.955
> 1133
> Clone Alpha
> 201
> 2.73
> 3沁
> 4.95
> 41.159
> 6.33沁
> 153.555
> 1258
> 743
> 2013
> 132
> 99光
> 1.71
> 20.9393
> 17.72北
> 10-.845
> 1233
> 713
> Chart
> Pnl
> 2019
> 09沁
> 2.35
> 二7.5491
> 13.63沁
> 134.535
> 1258
> 743
> 2020
> 93沁
> 20.0591
> 10.95*
> 67.135
> 1256
> 735
> 2021
> 60兆
> 21.3793
> 13.51兆
> 64.79*
> 1134
> 311
> 202
> 7.21沁
> 2.30
> 1.3291
> 12.55*
> 63.105
> 1154
> 340
> IOM
> 2023
> 63;
> 0.15
> 3.2195
> 09*
> 9.515
> 1151
> 33
> OOOK
> Correlation
> Self Correlation
> Iam IFT
> Ninimum
> Lt RIn:
> Jan'14
> Jan '15
> Jan'16
> Jan '17
> jan '18
> Jan '19
> Jan'20
> Jan 21
> J3n'22
> Jan '23
> Sharpe
> Lono


**3. 反转并缩放（倍数过小，不鼓励）**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 08/30/2025 EDT
> anonymoUs
> Add Alphato
> List
> Code
> IS Summary
> Period
> 05
> a=rsk72_atop2oOB_dsnt;
> Asinale Data Set Alpha
> Power Pool Alpha
> Pyramidtheme: CHNIDIIRISK X14
> breverse(ts_delta
> 53)
> sqrt(inst
> tvp
> 126 )
> signed_power (b,8
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> REIICns
> Cpat
> Marein
> 1.18
> 42.96%
> 0.46
> 6.41%
> 13.6096
> 2.9
> Simulation Settings
> Instrument Type
> Region
> Unjverse
> LangUaqe
> Decay
> Delay
> Truncation
> Neutralizatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> Sharpe
> TUIIOVeT
> Ftnoss
> Returns
> Drawdow
> Wargin
> Count
> Short Cownt
> Equiz
> CHN
> TOPZDOOU
> Fast Expression
> SIOW Facors
> Verify
> 2013
> 2.31
> 35.314
> 1.73
> 14.5093
> 3093
> 5Foo
> 495
> 501
> 2014
> 3.14
> 33.371
> 1.30
> 12.5493
> 1.-591
> 53530
> 59
> 535
> 2015
> 0.15
> 41.334
> 003
> 3893
> 13.1993
> GEoDD
> 390
> 1003
> 2016
> 1.23
> 45.334
> 4393
> 1-295
> 338o
> 002
> 1003
> Clone Alpha
> 201
> 0.44
> 42.371
> 0.03
> 7591
> 3.4893
> 0.325200
> 1013
> 935
> 2013
> 1.73
> 40.14*
> 0.75
> 7.2395
> 3.0595
> 535320
> 391
> 1007
> Chart
> Pnl
> 2019
> 1.75
> 4-.741
> 0.73
> 3091
> 1.3291
> 496oo
> 004
> 937
> 2020
> -0.62
> 45.301
> 0.13
> 3.8593
> 6.2191
> 535200
> 391
> 1010
> 2021
> 114
> 45.554
> 3693
> 5493
> 7356o
> 386
> 1013
> 202
> 47.231
> 0.93
> 52N
> 3.449
> 03530
> 1000
> 1004
> COOOK
> 2023
> 0.35
> 47.51
> 2.4991
> 0.5791
> 055oo
> 373
> 1025
> OOOK
> Correlation
> Self Correlation
> Iam IFT
> Ninimum
> Lt RIn:
> Jan '14
> Jan '15
> an'16
> Jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan 21
> J3n'22
> Jan '23
> 89600
> Lono


**四、总结概述**

1. 数据分析是因子挖掘的基本功， **数据本身研究的越透，越高效** ；

2. 因子优劣来自于字段本身的素质， **好字段能组成更多有效因子** ；

3.  **接近正态分布的字段本身就可能是因子** ，简单处理便可以使用。

**顾问 WX64154 (Rank 32) 的解答与建议**:
这曲线有点不大平滑 我有点不大敢交1 这种


---

### 技术对话片段 8 (原帖: 【⚡️VF0.77，单alpha60刀分享⚡️】活动主题+高fitness+低PC或是base payment的版本答案经验分享)
- **原帖链接**: [Commented] 【VF077单alpha60刀分享】活动主题高fitness低PC或是base payment的版本答案经验分享.md
- **时间**: 8个月前

**提问/主帖背景 (DS48533)**:
## 首先，展示下昨日战果：


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> u
> "Wllll
> rllllllillllllll_Illlilhllmlllllllmm
> Fe
> CC
> 》.》$
> eeQ
> 识''5'12 39"
> 9'<6'3'5
> ^ '识
> ~^ ^'?
> Period
> Regular
> Super
> Total
> Displayed Period
> 03/28/2025
> 09/30/2025
> 0S $895.14
> 05517.03
> 05$912.17
> Yesterday
> 09/30/2025
> US $60.00
> USS0.00
> US $60.00
> Current period
> 09/01/2025
> 10/31/2025
> US$189.54
> US51.89
> 0S$191.43
> Previous period
> 07/01/2025
> 08/31/2025
> US$118.79
> 05515.14
> 0S$133.93
> Yearto date
> 03/28/2025
> 09/30/2025
> 0S $895.14
> 05517.03
> 0S$912.17
> Total
> 03/28/2025
> 09/30/2025
> 05 $895.14
> 05517.03
> 05$912.17
> Nay
> May
> Way
> May
> Jun
> 5
> Nue
> RB
> Sep
> Sep
> Sep
> Sep


如图，本人VF只有0.77，但昨天 base payment 收益竟然达到了60刀，特发此贴，来介绍赚base的版本答案。所以只要比我VF高的人，都可以复现此贴，加油哇。

 
> [!NOTE] [图片 OCR 识别内容]
> User
> Welght
> Value
> Used
> Regular
> Regular
> Regular
> Super
> Super
> Super
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> CHANGCHUN
> UNIVERSITY OF
> 0548533 (Me)
> 0.00
> 0.77
> 380
> 255
> 0.24
> 0.51
> 0.54
> Nainlal
> SCIENCE AND
> Mean


## 那么究竟是怎样的alpha，拿到了这样的成绩呢：

## PNL
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> ZON
> 15N
> TON
> DOoK
> MN"N
> 2014
> 2015
> 2015
> 2011
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


## IS 年度表现：
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Theme: ASI Dataset Utilization Theme *2
> u Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIMODEL *1.2
> Aggregate Data
> Snarpe
> ULTONC I
> FItness
> RerUrns
> JITINOTITI
> Nargln
> 1.43
> 12.55%
> 2.78
> 47.31 %
> 22.01%
> 75.42%。
> Year
> Turnover
> Fitness
> Returns
> Urawdown
> Margin
> Long Count
> Short Count
> 2013
> OO0
> 0009
> 0OD
> 00%
> 00096
> 0053
> 2014
> 0.00
> 0.009
> 000
> 0.00%
> 0.0095
> 0.005,
> 2015
> 0.O0
> 00*
> 000
> 0.00%
> 0.0095
> 0.005
> 2016
> 0O0
> 009
> 00%
> 009
> 0053
> 2017
> 0.00
> 0.009
> 00O
> 0.00%
> 0.003
> 0.005
> 2018
> 1.51
> 11.58*
> 244
> 32.55%
> 11.303
> 55.7253
> 703
> 1293
> 2019
> 12.399
> 2.28
> 49.05%
> 22019
> 76.12535
> 907
> 943
> 2020
> 2.03
> 13.009
> 4.25
> 57.00%
> 12.503
> 87.715
> 1193
> 792
> 2021
> 1.61
> 10.349
> 3.12
> 47.06%
> 9.339
> 86.32533
> 1127
> 1307
> 2022
> 1.31
> 13.78*
> 257
> 53.09%
> 19.2196
> 7707535
> 1344
> 931
> 2023
> 1.00
> 20.259
> 0.82
> 13.51%
> 1.333
> 13.3350
> 120
> 1041
> Sharpe
 相关性：


> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> MNmUM
> MInIMUm
> LasT RUn. Thu, 10102'2025,12.14 AN
> 0.2898
> -0.2473
> I0M
> 1M
> I0Ok
> 鬓
> IOk
> 昱
> I00
> 03
> 03
> 03
> 09
> 03
> 09
> 0?
> 06
> 09
> 02'
> 02
> 0^ 
> 0
> 03
> 09
> 0,6
> 0,9
> 0.7..
> -0.1. ..
> 0,1
> 0.0。
> -1,0
> ~0,8
> ~0 .4。
> ~0.3.


如标题，我认为其中关键的地方在 **PC<0.3&&fitness>2.5&&UtilizationTheme** ，希望对各位对于base payment的理解，有所帮助。

## **祝各位也能拿满base！！**

**顾问 WX64154 (Rank 32) 的解答与建议**:
牛逼 我见到这种只有5年数据都是直接放弃的


---

### 技术对话片段 9 (原帖: 【⚡️VF0.77，单alpha60刀分享⚡️】活动主题+高fitness+低PC或是base payment的版本答案经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【VF077单alpha60刀分享】活动主题高fitness低PC或是base payment的版本答案经验分享_35332601368215.md
- **时间**: 8个月前

**提问/主帖背景 (DS48533)**:
## 首先，展示下昨日战果：


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> u
> "Wllll
> rllllllillllllll_Illlilhllmlllllllmm
> Fe
> CC
> 》.》$
> eeQ
> 识''5'12 39"
> 9'<6'3'5
> ^ '识
> ~^ ^'?
> Period
> Regular
> Super
> Total
> Displayed Period
> 03/28/2025
> 09/30/2025
> 0S $895.14
> 05517.03
> 05$912.17
> Yesterday
> 09/30/2025
> US $60.00
> USS0.00
> US $60.00
> Current period
> 09/01/2025
> 10/31/2025
> US$189.54
> US51.89
> 0S$191.43
> Previous period
> 07/01/2025
> 08/31/2025
> US$118.79
> 05515.14
> 0S$133.93
> Yearto date
> 03/28/2025
> 09/30/2025
> 0S $895.14
> 05517.03
> 0S$912.17
> Total
> 03/28/2025
> 09/30/2025
> 05 $895.14
> 05517.03
> 05$912.17
> Nay
> May
> Way
> May
> Jun
> 5
> Nue
> RB
> Sep
> Sep
> Sep
> Sep


如图，本人VF只有0.77，但昨天 base payment 收益竟然达到了60刀，特发此贴，来介绍赚base的版本答案。所以只要比我VF高的人，都可以复现此贴，加油哇。

 
> [!NOTE] [图片 OCR 识别内容]
> User
> Welght
> Value
> Used
> Regular
> Regular
> Regular
> Super
> Super
> Super
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> CHANGCHUN
> UNIVERSITY OF
> 0548533 (Me)
> 0.00
> 0.77
> 380
> 255
> 0.24
> 0.51
> 0.54
> Nainlal
> SCIENCE AND
> Mean


## 那么究竟是怎样的alpha，拿到了这样的成绩呢：

## PNL
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> ZON
> 15N
> TON
> DOoK
> MN"N
> 2014
> 2015
> 2015
> 2011
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


## IS 年度表现：
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Theme: ASI Dataset Utilization Theme *2
> u Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIMODEL *1.2
> Aggregate Data
> Snarpe
> ULTONC I
> FItness
> RerUrns
> JITINOTITI
> Nargln
> 1.43
> 12.55%
> 2.78
> 47.31 %
> 22.01%
> 75.42%。
> Year
> Turnover
> Fitness
> Returns
> Urawdown
> Margin
> Long Count
> Short Count
> 2013
> OO0
> 0009
> 0OD
> 00%
> 00096
> 0053
> 2014
> 0.00
> 0.009
> 000
> 0.00%
> 0.0095
> 0.005,
> 2015
> 0.O0
> 00*
> 000
> 0.00%
> 0.0095
> 0.005
> 2016
> 0O0
> 009
> 00%
> 009
> 0053
> 2017
> 0.00
> 0.009
> 00O
> 0.00%
> 0.003
> 0.005
> 2018
> 1.51
> 11.58*
> 244
> 32.55%
> 11.303
> 55.7253
> 703
> 1293
> 2019
> 12.399
> 2.28
> 49.05%
> 22019
> 76.12535
> 907
> 943
> 2020
> 2.03
> 13.009
> 4.25
> 57.00%
> 12.503
> 87.715
> 1193
> 792
> 2021
> 1.61
> 10.349
> 3.12
> 47.06%
> 9.339
> 86.32533
> 1127
> 1307
> 2022
> 1.31
> 13.78*
> 257
> 53.09%
> 19.2196
> 7707535
> 1344
> 931
> 2023
> 1.00
> 20.259
> 0.82
> 13.51%
> 1.333
> 13.3350
> 120
> 1041
> Sharpe
 相关性：


> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> MNmUM
> MInIMUm
> LasT RUn. Thu, 10102'2025,12.14 AN
> 0.2898
> -0.2473
> I0M
> 1M
> I0Ok
> 鬓
> IOk
> 昱
> I00
> 03
> 03
> 03
> 09
> 03
> 09
> 0?
> 06
> 09
> 02'
> 02
> 0^ 
> 0
> 03
> 09
> 0,6
> 0,9
> 0.7..
> -0.1. ..
> 0,1
> 0.0。
> -1,0
> ~0,8
> ~0 .4。
> ~0.3.


如标题，我认为其中关键的地方在 **PC<0.3&&fitness>2.5&&UtilizationTheme** ，希望对各位对于base payment的理解，有所帮助。

## **祝各位也能拿满base！！**

**顾问 WX64154 (Rank 32) 的解答与建议**:
牛逼 我见到这种只有5年数据都是直接放弃的


---

### 技术对话片段 10 (原帖: 【插件】Genius Rank分析代码优化)
- **原帖链接**: [Commented] 【插件】Genius Rank分析代码优化.md
- **时间**: 9个月前

**提问/主帖背景 (KZ79256)**:
插件地址： [[链接已屏蔽])

在插件中增加了对于genius rank的分析，这里非常感谢  [XX42289](/hc/en-us/profiles/14187300941847-XX42289)  提供的 [python分析代码]([L2] 【课代表】最新genius排名模拟代码_29383292162199.md)

使用说明

- 安装完插件后，打开genius页面（如果没有可以刷新一下，这可能和WQ的加载逻辑相关，后续会进行fix），可以看到会增加了两个按钮，其中`排名分析`是抓取排行榜的数据进行分析.`显示排名分析`是调用之前抓取的分析结果（自己的排名数据）. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> Gnius
> Displaying quarter:
> 2025-01 (Curren)
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析

- 无论点击以上哪一个按钮都会在该页面的按钮的下面显示一个自己的分析表格, 表格右上角是分析的时间.PS:排名分析按钮需要等待片刻（抓取时按钮上显示抓取的进度） 
> [!NOTE] [图片 OCR 识别内容]
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> Genius Rank Analysis
> 2025-01-25112:48:02.2082
> 我的排名信息
> 2025-01-2571243.022082
> 总人数:5691 人
> 可能的基准人数:936人
> (交够40个)
> 名个Level 满足的人数 _
> 最终的人数:
> For Expert: 721 /187
> For Master: 22194
> For Grandmaster: 0119
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171/187
> 总排名:15/94
> 总排名:0119
> Operator Count: 533名
> Operator Count: 21 名
> Operator Count:
> Operator AVE: 3名
> Operator AVE: 1 名
> Operator AVg:
> Field Count: 705 名
> Field Count: 23 多
> Field Count:
> Field AVB: 2名
> Field AVg:
> Field AVg:
> Community Activity: 81 名
> Community Activiny: 15 名
> Community Activity:
> Completed Referrals: 58 名
> Completed Referrals: 2 多
> Completed Referrals; 1 名
> Max Simulation Streak: 310名
> Max Simulation Streak: 18 名
> Max Simulation Streak:
> TotalRank; 1692 多
> Tota
> Rank: 81 名
> Tota
> Rank:
> Current level;: Gold
> Best leyel: Gold
> Current quarterend: March 31st. 2025
> COUO

- 此外，还可将鼠标移动到排行榜上的UserId处展示他人的分析数据 
> [!NOTE] [图片 OCR 识别内容]
> X42289 排名信息
> 总人数:5691 人
> Aggregate by:
> 可能的基准人数:936  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 721/187
> For Master: 22194
> For Grandmaster: 0/19
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171187
> 总排名:4194
> 总排名:0/19
> Operator Count: 199名
> Operator Count: 13名
> Operator Count: 1 名
> Operator
> 17名
> Operator
> 2名
> Operator
> 1名
> Rank
> User
> Field Count: 423名
> Field Count: 23名
> Field Count:
> 名
> Field
> 18名
> Field
> 名
> Field
> Community Activity: 20名
> Community Activity: 3名
> Community Activity:
> Completed Referrals: 12名
> Completed Referrals: 1 名
> Completed Referrals:
> 名
> 1,090
> 1279256
> Max Simulation Streak:
> Max Simulation Streak: 16
> Max Simulation Streak:
> 273名
> Total Rank: 962名
> Total Rank: 59名
> Total Rank: 7名
> XP21
> 042289
> Maser
> Maser
> 117
> 0.00
> AVB:
> AVE: 
> AVg:
> AVB: -
> AVg:
> AVB: -


**顾问 WX64154 (Rank 32) 的解答与建议**:
6维的具体排名机制是怎么排的，每个维度的权重是相同的吗


---

### 技术对话片段 11 (原帖: 【插件】Genius Rank分析代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md
- **时间**: 9 months ago

**提问/主帖背景 (KZ79256)**:
插件地址： [[链接已屏蔽])

在插件中增加了对于genius rank的分析，这里非常感谢  [XX42289](/hc/en-us/profiles/14187300941847-XX42289)  提供的 [python分析代码]([L2] 【课代表】最新genius排名模拟代码_29383292162199.md)

使用说明

- 安装完插件后，打开genius页面（如果没有可以刷新一下，这可能和WQ的加载逻辑相关，后续会进行fix），可以看到会增加了两个按钮，其中`排名分析`是抓取排行榜的数据进行分析.`显示排名分析`是调用之前抓取的分析结果（自己的排名数据）. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> Gnius
> Displaying quarter:
> 2025-01 (Curren)
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析

- 无论点击以上哪一个按钮都会在该页面的按钮的下面显示一个自己的分析表格, 表格右上角是分析的时间.PS:排名分析按钮需要等待片刻（抓取时按钮上显示抓取的进度） 
> [!NOTE] [图片 OCR 识别内容]
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> Genius Rank Analysis
> 2025-01-25112:48:02.2082
> 我的排名信息
> 2025-01-2571243.022082
> 总人数:5691 人
> 可能的基准人数:936人
> (交够40个)
> 名个Level 满足的人数 _
> 最终的人数:
> For Expert: 721 /187
> For Master: 22194
> For Grandmaster: 0119
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171/187
> 总排名:15/94
> 总排名:0119
> Operator Count: 533名
> Operator Count: 21 名
> Operator Count:
> Operator AVE: 3名
> Operator AVE: 1 名
> Operator AVg:
> Field Count: 705 名
> Field Count: 23 多
> Field Count:
> Field AVB: 2名
> Field AVg:
> Field AVg:
> Community Activity: 81 名
> Community Activiny: 15 名
> Community Activity:
> Completed Referrals: 58 名
> Completed Referrals: 2 多
> Completed Referrals; 1 名
> Max Simulation Streak: 310名
> Max Simulation Streak: 18 名
> Max Simulation Streak:
> TotalRank; 1692 多
> Tota
> Rank: 81 名
> Tota
> Rank:
> Current level;: Gold
> Best leyel: Gold
> Current quarterend: March 31st. 2025
> COUO

- 此外，还可将鼠标移动到排行榜上的UserId处展示他人的分析数据 
> [!NOTE] [图片 OCR 识别内容]
> X42289 排名信息
> 总人数:5691 人
> Aggregate by:
> 可能的基准人数:936  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 721/187
> For Master: 22194
> For Grandmaster: 0/19
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171187
> 总排名:4194
> 总排名:0/19
> Operator Count: 199名
> Operator Count: 13名
> Operator Count: 1 名
> Operator
> 17名
> Operator
> 2名
> Operator
> 1名
> Rank
> User
> Field Count: 423名
> Field Count: 23名
> Field Count:
> 名
> Field
> 18名
> Field
> 名
> Field
> Community Activity: 20名
> Community Activity: 3名
> Community Activity:
> Completed Referrals: 12名
> Completed Referrals: 1 名
> Completed Referrals:
> 名
> 1,090
> 1279256
> Max Simulation Streak:
> Max Simulation Streak: 16
> Max Simulation Streak:
> 273名
> Total Rank: 962名
> Total Rank: 59名
> Total Rank: 7名
> XP21
> 042289
> Maser
> Maser
> 117
> 0.00
> AVB:
> AVE: 
> AVg:
> AVB: -
> AVg:
> AVB: -


**顾问 WX64154 (Rank 32) 的解答与建议**:
6维的具体排名机制是怎么排的，每个维度的权重是相同的吗


---

### 技术对话片段 12 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】你说你没有模板这里你多得用不完.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
吹哨人又来了，这次继续带来一个好消息。当你点击下面那个小灯，你就找对了地方。


> [!NOTE] [图片 OCR 识别内容]
> Expression Editor
> Clear
> SaVe Current Template
> Overrite Existing
> 找灵感
> ctime_series_operator/> (sentiment_difference,
> 〈days/〉)


操作如图


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)步骤3:输入搜索关键词搜索数据集
> 关键词可以是pyramid之类都行
> 步骤4:点击生成
> Configuration
> Select Dataset
> 3. Results
> Generate Nlpha Templates
> Download MD
> LLM Settings
> Search dataset _
> Search
> 以下绐出5 组可直接在平台落地的" Alpha 模板"。
> Base URL
> 每个模板均保留"插槽"一一用<>标注
> ~方便后续批量替换。
> 网格搜索或遗传进化。
> 已选数据集: analyst15
> https llapimoonshot cnlvl
> 所有模板已预置:
> 数据清洗 (backfill
> Winsorize)
> 步骤5:下载后慢慢品味和
> Name
> Mocel Name
> 经济逻辑 (动量
> 预期差
> 估值。质量。情绪)
> 实施,并把模板放入赢
> kimi-k2-turbo-preview
> Performance
> 常见中性化(行业/市值)与衰减选项
> tUTnoVer
> 控制接口
> (ts_target_tVr_* )
> 进行配置和展开
> Weighted
> API Key
> analystl0
> Analyst
> 模板1:  分析师预期动量
> (Estimate Revision Momentum)
> Test
> Estimates
> 经济直觉:  过去1个月 EPS 上调幅度越大的股票。未来越可能继续跑赢。
> 步骤1
> 输入API
> analyst11
> ESG SCOres
> 3Iph3
> eXP_Window(
> Simulation Settings
> Estimations OT
> 9rOUP_ZsCOre(
> analyst14
> T5_backfil(
> Reglon
> Fundamentals
> winsorize(<anll15_9r_12_m_Im_chg >, std=4j
> EUR
> Earnings
> Unierse
> analystl5
> fore-asts
> 9rOUP>
> TOP12O0
> Analyst
> Delay
> analyst4
> Estimate Data
> 〈half_life >
> for Equity
> 插槽:
> Integrated
> gr_12_m_Im_chg>
> 可换 3m/Gm 或 SAL/CPS/EBG 等
> 步骤2:按需选择
> analyst44
> Broker
> 〈groUp>
> industry
> Sector
> subindustry
> Estimates
> 〈half_life >
> 5~30天可调。控制换手
> Block comments Tor multiple lines
> Key
> Jecay
> Kej
> <anl15


**这是2.0时代了，拥抱交不完的Alpha吧。**

**下面有一个无脑mcp简易版**

**[[MCP]找灵感功能上手详解](../顾问 LW67640 (Rank 24)/[Commented] [MCP]找灵感功能上手详解经验分享.md)**

**顾问 WX64154 (Rank 32) 的解答与建议**:
准备升级了

反复升级还有点累

========================================================================================================Pursue scalable, repeatable opportunities rooted in probability.================

====================================================================================


---

### 技术对话片段 13 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
吹哨人又来了，这次继续带来一个好消息。当你点击下面那个小灯，你就找对了地方。


> [!NOTE] [图片 OCR 识别内容]
> Expression Editor
> Clear
> SaVe Current Template
> Overrite Existing
> 找灵感
> ctime_series_operator/> (sentiment_difference,
> 〈days/〉)


操作如图


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)步骤3:输入搜索关键词搜索数据集
> 关键词可以是pyramid之类都行
> 步骤4:点击生成
> Configuration
> Select Dataset
> 3. Results
> Generate Nlpha Templates
> Download MD
> LLM Settings
> Search dataset _
> Search
> 以下绐出5 组可直接在平台落地的" Alpha 模板"。
> Base URL
> 每个模板均保留"插槽"一一用<>标注
> ~方便后续批量替换。
> 网格搜索或遗传进化。
> 已选数据集: analyst15
> https llapimoonshot cnlvl
> 所有模板已预置:
> 数据清洗 (backfill
> Winsorize)
> 步骤5:下载后慢慢品味和
> Name
> Mocel Name
> 经济逻辑 (动量
> 预期差
> 估值。质量。情绪)
> 实施,并把模板放入赢
> kimi-k2-turbo-preview
> Performance
> 常见中性化(行业/市值)与衰减选项
> tUTnoVer
> 控制接口
> (ts_target_tVr_* )
> 进行配置和展开
> Weighted
> API Key
> analystl0
> Analyst
> 模板1:  分析师预期动量
> (Estimate Revision Momentum)
> Test
> Estimates
> 经济直觉:  过去1个月 EPS 上调幅度越大的股票。未来越可能继续跑赢。
> 步骤1
> 输入API
> analyst11
> ESG SCOres
> 3Iph3
> eXP_Window(
> Simulation Settings
> Estimations OT
> 9rOUP_ZsCOre(
> analyst14
> T5_backfil(
> Reglon
> Fundamentals
> winsorize(<anll15_9r_12_m_Im_chg >, std=4j
> EUR
> Earnings
> Unierse
> analystl5
> fore-asts
> 9rOUP>
> TOP12O0
> Analyst
> Delay
> analyst4
> Estimate Data
> 〈half_life >
> for Equity
> 插槽:
> Integrated
> gr_12_m_Im_chg>
> 可换 3m/Gm 或 SAL/CPS/EBG 等
> 步骤2:按需选择
> analyst44
> Broker
> 〈groUp>
> industry
> Sector
> subindustry
> Estimates
> 〈half_life >
> 5~30天可调。控制换手
> Block comments Tor multiple lines
> Key
> Jecay
> Kej
> <anl15


**这是2.0时代了，拥抱交不完的Alpha吧。**

**下面有一个无脑mcp简易版**

**[[MCP]找灵感功能上手详解]([L2] [MCP]找灵感功能上手详解经验分享_37113649831831.md)**

**顾问 WX64154 (Rank 32) 的解答与建议**:
准备升级了

反复升级还有点累

========================================================================================================Pursue scalable, repeatable opportunities rooted in probability.================

====================================================================================


---

### 技术对话片段 14 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

12月份来了，开始我的混塔日常

又又通过group_backfill混了2塔

==================================================================================================================点塔中！！！=======================================

==================================================================================


---

### 技术对话片段 15 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

20251206

为了点塔 又交了一个只有5年的垃圾

=================================================================================

================================继续点塔！！！=====================================

==================================================================================


---

### 技术对话片段 16 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
===============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===================================

20251208

combine更新了

PPA的combine有点让人够不懂，三条线表现并不一致

===============================================================================================================HOPE HIGH COMBINE===================================

==================================================================================


---

### 技术对话片段 17 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

回测限10000了！！！

确实限制产出

太卷了

===================================================================================================================VF1.0=============================================

==================================================================================


---

### 技术对话片段 18 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

20251209

限速后的base似乎高了一点

3RA的base20刀只有1个主题

==============================================================================================================HOPE HIGH BASE=======================================

==================================================================================


---

### 技术对话片段 19 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记================================

20251210

又是SA < 0.3 base拿满的一天

====================================================================================================================天天拿满！！！====================================

==================================================================================


---

### 技术对话片段 20 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记================================

20251214

Sentiment的真难点！！！

====================================================================================================================努力点塔=========================================

=================================================================================


---

### 技术对话片段 21 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
==============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记====================================

20260120

昨天OS更新

今天的sa怎么组，都感觉怪怪的

还是交个三五吧

==================================================================================

================================第九季开始=========================================

==================================================================================


---

### 技术对话片段 22 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
====================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==============================

5000用完了

3 + 1个GLB

==================================================================================

=================================VF1.0============================================

=================================================================================


---

### 技术对话片段 23 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记================================

OS出来 GLB的OS表现不太满意

GLB的THEME 要注意质量了

==================================================================================

===================================VF1.0=========================================

=================================================================================


---

### 技术对话片段 24 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

OS 更新后组不出 PC < 0.3 的SA了

Base少了好多

==================================================================================

==============================VF1.0================================================

=================================================================================


---

### 技术对话片段 25 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================20251012==============================================

4+1个alpha

Q4的第10塔点亮，继续！！！

====================================================================================================================加油============================================


---

### 技术对话片段 26 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
量化日记 251015

到底是没能在12点前交上，提交太慢了~~

2 + 1 alpha

=============================================================================

========Genius is one percent inspiration and ninety-nine percent perspiration.================

==============================================================================


---

### 技术对话片段 27 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
================2025-10-18==顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记======================================

4+1个alpha base8+刀

vf 0.74

=========坚决不要混信号、坚决不要过拟合、确保多样性、确保稳健性、要有经济学意义=========


---

### 技术对话片段 28 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
===============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===================================

第一次三五的SA  也首次超过5刀 vf 0.73

=======================================================================

Achievements are reached by hard work, but ruined by idleness; Actions are accomplished through thorough consideration, but destroyed by casual decision.​​  =======================================================================


---

### 技术对话片段 29 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记========================================

vf 更新了 0.76 base较0.74基本没什么变化

================================加油！！！=================================


---

### 技术对话片段 30 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)========================================

VF 0.76 的三五SA  base在6+刀左右

==========================Talk is cheap,show me the alpha================================


---

### 技术对话片段 31 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
===================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===============================

20251221

第八季开始！！！

今天回测7200，提交3alpha

====================================================================================================================Hope high combine==================================

==================================================================================


---

### 技术对话片段 32 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

SA的PC有找到一个小于0.3的

又有60刀了

=====================================================================================================================Hope high VF=====================================

==================================================================================


---

### 技术对话片段 33 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

回测开始5000了

极度影响产量

只有2RA

====================================================================================================================加油！！！=======================================

==================================================================================


---

### 技术对话片段 34 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251222

今天又是SA 60刀打卡

==================================================================================

=================================加油！！！========================================

==================================================================================


---

### 技术对话片段 35 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251223

AI工具还是不好用，总要有一定的回测量才行，太影响产出了

===================================================================================================================HOPE HIGH COMBINE==============================

=================================================================================


---

### 技术对话片段 36 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251224

做出了个EUR的own三五！！！

===================================================================================================================加油！！！=========================================

==================================================================================


---

### 技术对话片段 37 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
===============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===========================-=========

没跑出好的 交了一个垃圾

====================================================================================

===================================Q4优化6维中=======================================

====================================================================================


---

### 技术对话片段 38 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251226

交了一个 RA一个SA

=====================================================================================================================优化6维中=======================================

==================================================================================


---

### 技术对话片段 39 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

今天27刀，没有三五

======================================================================================================================加油！！！=========================================

====================================================================================


---

### 技术对话片段 40 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260319

4RA 9+

SA 60

OS 0.7+

===================================================================================================================点塔中！==========================================

==================================================================================


---

### 技术对话片段 41 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260318

4RA 6+

SA 9+

total 16

OS 0.7+

===================================================================================================================点塔中！==========================================

==================================================================================


---

### 技术对话片段 42 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260320

4RA 7+

SA 59

OS 0.6+

===================================================================================================================点塔！==========================================

==================================================================================


---

### 技术对话片段 43 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260316（回忆）

4RA 7+

SA 58+

OS 0.7+

===================================================================================================================点塔！==========================================

==================================================================================


---

### 技术对话片段 44 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260321

52塔了

USA点塔中

===================================================================================================================点塔！==========================================

==================================================================================


---

### 技术对话片段 45 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

20260303

os 0.7+

ra 1个 48$

sa 59$

total 107$

=================================================================================

=================================HIGH VF AND OS==============================

===============================================================================


---

### 技术对话片段 46 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

20260301

ra  0个  没想到是GLB的Theme

SA 11$

=================================================================================

=================================HIGH VF AND OS==============================

===============================================================================


---

### 技术对话片段 47 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
===================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===============================

20260228

高os  三五 SA 57$

=================================================================================

=================================HIGH VF AND OS==============================

===============================================================================


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
2025年09月19日

今天一共提交了1个Super Alpha(s)，表现如下：

第1个：type=SUPER, region=EUR, sharp=6.13, turnover=9.26%, fitness=5.22, returns=11.89%, drawdown=1.95%, margin=26.19%%

以下是昨日SA表现与BASE：

date

vf

fitness

prod

base

0919

0.74

5.22

0.68

4.9


---

### 技术对话片段 49 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
20250921 5个alpha交满的第三天

===========================================

RA：GLB 1个，  ASI 2个， USA1个

SA: GLB

=======================不混信号、不过拟合、多样性、稳健性============================


---

### 技术对话片段 50 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
2025923

4个RA 没组出 super alpha

base  3.98  vf 0.74

=======================不混信号、不过拟合、多样性、稳健性============================


---

### 技术对话片段 51 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
我的量化流水账：2025年09月24日

4个RA， 依然组不出Super alpha

Base 4.24 vf 0.74

=======================================================================
那些凌晨三点还亮着的屏幕光，终会化作晋级榜单上闪耀...
=======================================================================


---

### 技术对话片段 52 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX64154 (Rank 32) 的解答与建议**:
9.25 我的量化日记第四季

4个RA ，0Super alpha

Base 5 vf 0.74

===================================================================================
===================Talk is cheap,show me the alpha=======================================


---

### 技术对话片段 53 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX44j9wB86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAjcBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzM0OTEzNzQ3Nzg4Njk1LS0lRTclQkIlOEYlRTklQUElOEMlRTUlODglODYlRTQlQkElQUItJUU1JTg2JUIyJUU1JTg4JUJBLWdlbml1cy0lRTclQkIlODYlRTglOEElODIlRTUlODYlQjMlRTUlQUUlOUElRTYlODglOTAtJUU4JUI0JUE1LSVFNCVCRCVBMCVFNyU5QSU4NCVFNSU4NSVBRCVFNyVCQiVCNCVFOCVCRiU5OCVFOCU4MyVCRCVFNiU4RiU5MCVFNSU4RCU4Ny0lRTclODIlQjklRTUlQTElOTQtYWxwaGElRTYlQTglQTElRTYlOUQlQkYGOwhUOg5zZWFyY2hfaWRJIik3MWJmMjVmNS1lYTY3LTRjOGEtYjIyNi0zN2E1Zjc2YWE1NmIGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDY0MTU0BjsIVDoScmVzdWx0c19jb3VudGkf--dc515f535bff21c3d15516c213be8bc24369be03
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:
一、Genius定级与何相干？总体来说，一共与两方面有关，一是硬性指标，二是软指标。其中硬性指标包括由1. 本季度 Signals (阿尔法)；2. 本季度 Pyramids (金字塔)；3. Combined Alpha Performance (提交的所有alpha表现)；4. Combined Selected Alpha Performance (被选中的alpha费后表现)5. Combined Power Pool Alpha Performance (power pool alpha表现)五部分组成；点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。我们以Expert (专家)为例，硬性指标必须同时满足1. 本季度alpha数量 Signals ≥ 20；2. 本季度金字塔数量 Pyramids ≥ 10，3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).软指标又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。其中软指标(六维数据)包括由本季度1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；2. Operators used (操作符的去重使用个数)；3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；4. Fields used (字段使用(去重)数量)5. Community activity (rank[社区活跃程度])6. Max simulation streak (最大连续回测天数)六部分组成；·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。二、冲刺 Genius !通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。1. 关于六维数据细节这部分我们娓娓道来，关于六维数据我们能做的是什么?i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .首先，讲讲我的一些蠢行为! ,等等上面还有一点重要的忘记说了，要保持区域、Delay以及数据集多样性！使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多8~10个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，直到我使用华子哥的插件才发现我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！下面的操作有几率降低你的Operators per Alpha，和想要查看自己的alpha数据也可以认真看一下在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)下面的是查询alpha信息的url接下来我们就来看看几个alpha，查看它们的数据情况1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果重复算 operatorCount 操作符了 .没有字段使用数量信息，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .重点：巧妙的节省重复操作符 ！！！从以上几个alpha操作符测试，让我们知道了i ) +、-、*、/ 和 ^ 都是算入操作符计数的；ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .2. 点塔！点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节：交一个怎样的alpha能提升你的六维数据之定性定量分析 .我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 .通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .3. 好而优的 alpha何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .一点：好，我理解在:1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；2) fitness ≥ 1  全方面稳定还是非常不错；3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；4) returns ≥ 10%  收益还是要好点能赚钱吧；5) drawdown 回撤越小越好吧，大了心理抗压不行；6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；7) 十年数据中做多做空不能太少吧，权重太高危险危险！8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .二点：优，我理解在:1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；使用不建议使用三、alpha模板 ！看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .下节预告:Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析2025年9月14日

**顾问 WX64154 (Rank 32) 的解答与建议**:
感谢大佬分享。给我深深上了一课，期待下节。想知道大佬怎么把combine刷的那么高


---

### 技术对话片段 54 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX44j9wB86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAjcBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzM0OTEzNzQ3Nzg4Njk1LS0lRTclQkIlOEYlRTklQUElOEMlRTUlODglODYlRTQlQkElQUItJUU1JTg2JUIyJUU1JTg4JUJBLWdlbml1cy0lRTclQkIlODYlRTglOEElODIlRTUlODYlQjMlRTUlQUUlOUElRTYlODglOTAtJUU4JUI0JUE1LSVFNCVCRCVBMCVFNyU5QSU4NCVFNSU4NSVBRCVFNyVCQiVCNCVFOCVCRiU5OCVFOCU4MyVCRCVFNiU4RiU5MCVFNSU4RCU4Ny0lRTclODIlQjklRTUlQTElOTQtYWxwaGElRTYlQTglQTElRTYlOUQlQkYGOwhUOg5zZWFyY2hfaWRJIik3MWJmMjVmNS1lYTY3LTRjOGEtYjIyNi0zN2E1Zjc2YWE1NmIGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDY0MTU0BjsIVDoScmVzdWx0c19jb3VudGkf--dc515f535bff21c3d15516c213be8bc24369be03
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 冲刺genius !
> 细节决定成败,你的六维还能提升 ! &模板
> 
> 
> 首先感谢游戏王 (2559763) ,
> 橘子姐
> (6383096) ,
> base payment 拉满的
> 大佬 (AH18340) 以及 上海 (MF59400)等等的帮助.也许你们自己都不知道 ,
> 但是潜移默化
> 的影响了我,
> 下面阐述的其中有-些内容是我在游戏王那里学习到的.


## **一、Genius定级与何相干？**

总体来说，一共与两方面有关，一是  **硬性指标** ，二是  **软指标** 。


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-03,July 1st, 2025
> September 3Oth; 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 266
> Reached Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 72
> Reached Grandmaster
> 10
> 30
> Combined Alpha Performance
> 2.39
> Reached Grandmaster
> 0.5


其中  **硬性指标** 包括由

1. 本季度 Signals (阿尔法)；

2. 本季度 Pyramids (金字塔)；

3. Combined Alpha Performance (提交的所有alpha表现)；

4. Combined Selected Alpha Performance (被选中的alpha费后表现)

5. Combined Power Pool Alpha Performance (power pool alpha表现)

五部分组成；

```
点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。
```

我们以Expert (专家)为例，硬性指标必须同时满足

1. 本季度alpha数量 Signals ≥ 20；

2. 本季度金字塔数量 Pyramids ≥ 10，

3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5

       这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).

[图片 (图片已丢失)]

**软指标** 又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。

**
> [!NOTE] [图片 OCR 识别内容]
> What happens 迂 more consultants qualify for a level than there are available
> If more consultants meet the base criteria for
> level than there are available Spots
> a tiebreaker criterion is used _
> This is based on a sum Of ranks across the following metrics
> 1.
> distinct Operators
> Alpha (Lower is better )
> 2.
> distinct Fields
> Alpha (Lower is better)
> 3. Total distinct Operators (Higher is better)
> 4
> Total distinct Fields (Higher is better)
> 5. Maximum Simulation Streak
> Best streak of
> consultant that ends i that quarter
> OI
> continues into the next quarter
> Streak does not reset to 0 every quarter。
> 6. Community leader
> Forum
> Number Of Likes on Posts Or comments that are
> published as Of the end Of quarter
> Ninimm length of post Or comment must be 100 characters。
> Referral
> Total number Of successful referrals i the quarter
> A referral is considered
> Slccessfil
> Khen the
> referring consultant h as become eligible to accrte the referral fee for someone
> have referred to BRAIN
> 讧 accordance with the guidelines Of the referral fee program
> Spots?
> Avg
> AVg
> they
**

**
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st, 2025
> September 3Oth, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.41
> 68
> 1.54
> Fields used
> Community activity
> Max simulation streak
> 260
> 33.2
> 88
**

其中  **软指标** (六维数据)包括由本季度

1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；

2. Operators used (操作符的去重使用个数)；

3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；

4. Fields used (字段使用(去重)数量)

5. Community activity (rank[社区活跃程度])

6. Max simulation streak (最大连续回测天数)

六部分组成；

```
·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。
```

[图片 (图片已丢失)]

## **二、冲刺 Genius !**

通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。

1. 关于六维数据  **细节**

这部分我们娓娓道来，关于六维数据我们能做的是什么?

i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；

ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；

iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；

iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；

v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .

首先，讲讲我的一些  **蠢行为! ,** 等等上面还有一点重要的忘记说了， **要保持区域、Delay以及数据集多样性！**

**
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st, 2025
> September 3Oth, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Fundamental
> Insiders
> Macro
> Mogel
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Social Media
> Earnin3s
**

使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多  **8~10**  个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Delayo
> NAN
> Delayl
> NAN
> Fundamental data
> Fundamental data
> Analyst data
> Analyst data
> Broker
> Broker
> News data
> News data
> Social media data
> Social media data
> Sentiment data
> Sentiment data
> Price VOluMe data
> Price Volume data
> Option data
> Option data
> Eamings
> Earnings
> Insiders
> Insiders
> Instiutional Ownership Data
> Instiutional Ownership Data
> Short interest data
> Short interest data
> Macro data
> Macro data
> Other
> Other
> Risk data
> Risk data
> Model data
> Model data
> USA
> ASI
> CHN
> EUR
> GL
> HKG
> KOR
> TVN
> AMR
> JPN
> USA
> ASI
> CHN
> EUR
> GLB
> HKG
> KOR
> TVN
> AMR
> JPN
> Click to drill down
> EUR
> ASI
> GLB
> USA
> CHN


保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.

[图片 (图片已丢失)]

接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/26/2025 EDT
> 顾问 ML47973 (Rank 100)
> Add Alphato
> LiSt
> Code
> IS Summary
> Period
> IS
> 05
> power(2,
> md177_astcomp
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> Simulation Settings
> 1.65
> 6.11%
> 2.64
> 31.939
> 16.609
> 104.449600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Subindustry
> On
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 1.69
> 5.46%
> 1.56
> 10.65%
> 4.76%
> 39.05920
> 1999
> 357
> 2019
> 4.949
> 1.71
> 18.5896
> 8.66%
> 75.279620
> 1988
> 375
> 2020
> -0.,04
> 029
> 0.01
> 0.5596
> 15.18%
> 82920
> 2010
> 375
> Clone Alpha 
> 2021
> 2.46
> 699
> 4.84
> 48.489
> 15.30%
> 122.899620
> 2142
> 380
> 2022
> 2.44
> 7.42%
> 6.08
> 77.70%
> 13.23%
> 209.41920
> 2136
> 390
> Chart
> Pnl
> 2023
> 3.61
> 6.13%
> 7.40
> 52.519
> 1.71%
> 171.19920
> 2114
> 397
> 匣
> Correlation
> 1ON
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,4;51
> PM
> 0.6840
> -0.0542
> OOOK
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,4;51
> Du
> 0.4204
> -0.1633
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 4;51
> 0
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul "22
> Jan '23
> Du
> 0.6874
> -0.6201
> Vear



> [!NOTE] [图片 OCR 识别内容]
> 这个 Q 当时让我 base payment 日 赚54.816 ,当时 iqc 结束 ,第一次0f更新0.86


直到我使用华子哥的插件才发现


> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 美东时间:2025/9/1200:38:06 北京时间: 2025/9/1212:38:06
> 在你可用的运算符中。共有67种运算符被使用。12种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统一为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x, Y, filter
> false); X + y
> 52
> COMBO,REGULARSELECTION
> base
> Arithmetic
> multiply(x ,y
> filterzfalse); X * y
> 76
> COMBO,REGULARSELECTION
> base
> Arithmetic
> sign(x)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> subtract(x, Y, filter-false) X -Y
> 157
> COMBO,REGULARSELECTION
> base
> Arithmetic
> pasteurize(x)
> COMBO,REGULAR
> genius
> Arithmetic
> log(x)
> COMBOREGULARSELECTION
> base
> Arithmetic
> maXfx;y
> COMBO,REGULARSELECTION
> base
> Arithmetic
> absfx)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> divide(x; y), XIy
> 158
> COMBO,REGULARSELECTION
> base


我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！

下面的操作有几率  **降低** 你的  ***Operators per Alpha*** ，和想要查看自己的alpha数据也可以认真看一下

在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)


> [!NOTE] [图片 OCR 识别内容]
> #  登录 (login)url
> CUrl
> --location
> --request
> POST
> https : / /api. worldquantbrain . com
> authentication
> header
> Authorization:
> Basic MZAZODUBMTAZOEBXcSSjbzeGQUYrQUYrQUYgMBFG
> ~-header
> Cookie:
> t=eyJeeXAiOiJKVIQiLCJhbGciOiJIUZIINiJg .eyJqdGkioi -



> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> login
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> POST
> https:Hapi.orldquantbrain comlauthentication
> Send
> Environments
> POST Simulation
> Params
> Authorization
> Headers (10)
> Body
> Scripts
> Settings
> Cookies
> PATCH alpha-adjust
> FIOws
> Auth Type
> GET data-fields
> Username
> 30-510
> COm
> Basic Auth
> GET alpha
> History
> GET Check
> Password
> The authorization header will be
> POST submit
> 0+
> automatically qenerated when yoU send the
> GET Self-COrr
> Body
> Cookies
> Headers (20)
> Test Results
> 201 Created
> 1.975
> 1.14 KB
> Save Response
> GET data-sets
> JSON
> Preview
> Visualize
> 三
> Q  @
> GET
> pyramid
> USET"
> id
> 顾问 ML47973 (Rank 100)
> Loken"
> EXDiTy
> 14400
> DeTmissions
> BEFORE
> ANID_
> AFTER
> PERFORMANCE_
> 10
> BRAIN_LA3S"
> 11
> BRAIN_LABS_JUPYTER
> L43
> 12
> CONSULTANTI
> 13
> "MULTI_SIMULATION "
> 14
> PROD_ALPHAS
> 15
> REFERRAL
> 16
> SUPER_ALPHA "
> 17
> IVISUALIZATION"
> 18
> WORKDAY"
> 19
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> 9@.


下面的是查询alpha信息的url


> [!NOTE] [图片 OCR 识别内容]
> #
> check_alpha_info 其中{alpha_id} 使用alpha_id替代即可
> Curl
> -location
> https : / /api .worldquantbrain . com/alphas / {alpha_id}
> -header
> Cookie:
> tseyJeexAioiJKVIQiLCJhbGciOiJIUZIINiJ9 .eyJqdGkioi


接下来我们就来看看几个alpha，查看它们的数据情况

1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/09/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> ib5
> SCOFe
> Single Data Set Alpha
> 俳
> Power Pool Alpha
> Pyramid theme: EURIDIIIMBALANCE X2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> Simulation Settings
> 3.37
> 22.089
> 2.26
> 9.9396
> 2.4596
> 9.009o0
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.02
> Statistical
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.19
> 23.9499
> 200
> 14.1990
> 1.08%
> 11.8590
> 1324
> 781
> 2014
> 4.55
> 23.2595
> 3.25
> 11.85%
> 0.78%
> 10.20950
> 1612
> 1005
> 2015
> 4.20
> 23.68%
> 3.26
> 13.02%
> 1.31%
> 11.00930
> 1101
> Clone Alpha
> 2016
> 4.52
> 22.9795
> 3.52
> 13.78%
> 1.65%
> 11.99930
> 627
> 1092
> 2017
> 4.22
> 22.0095
> 2.79
> 9.519
> 0.9190
> 8.72930
> 1749
> 1203
> Chart
> Pnl
> 2018
> 3.4
> 21.699
> 2.37
> 10.29%
> 20%
> 499
> 1714
> 1212
> 2019
> 3.26
> 21.4495
> 2.26
> 10.32%
> 1.23%
> 52930
> 1665
> 1162
> 2020
> 1.99
> 21.1495
> 1.12
> 6.6296
> 2.4596
> 2890
> 1616
> 1125
> 2021
> 2.52
> 20.1895
> 47
> 6.729
> 1.02%
> 58930
> 1703
> 1259
> 7,50OK
> 2022
> 1.37
> 20.139
> 0.67
> 4.839
> 2.29%
> 4.80930
> 652
> 1240
> 5,0OOK
> 2023
> -11.03
> 29.179
> 10.18
> -24.859
> 1.539
> -17.0293o
> 1505
> 1077
> 2,50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.99
> 8.649
> 1.44
> 6.5296
> 8.4096
> 15.089600
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 5;43
> PM
> 0.1456
> -0.0393
> 00
> IS Testing Status
> Period
> 05
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 5;43
> PM
> 0.6239
> -0.0916
> 6 PASS
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 5;43
> Sharpe Of 3.37 is above CUtOff of 1.58。
> PM
> Fitness Of 2.26 is above cutoff of 1
> 0.7043
> -0.3995
> Turnover of 22.089 is above cutoff of 1%
> Turnover of 22.08% is below cutoff of 70%


仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain.comlalphas BOPXEEZ
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 3.06
> 2.19 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> IaXTTaCE
> OFF
> operatorcount
> _
> 1Of1
> 个 b = X
> 17
> "language
> FASTEXPR'
> 18
> IVis0a1i2ation"
> false,
> 19
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE
> imb5_
> SCOIC!
> 24
> description
> Iaea:
> Take
> The
> negative
> Inverse
> O1 The
> inbalance
> SCOIE
> -0
> CIeaTe
> ConTLaLian Signal
> That
> elphasizes
> anC
> fLips
> The
> OIIgInal Ielatzonsh-p. InRatzonale
> for
> 0a-a
> USeC
> The
> inbalance
> SCOIE
> (imb5_
> SCOIE )
> Iikely
> IIea5ULe5
> OIOEI
> fIOW
> OI
> Iiquidity
> aSyIIeTTy;
> Its Inverse highlishts periods
> O1 balance,
> and
> The
> negative sign
> fuITher
> inverts
> The signal. InRationale
> fJI
> OperatoIs  used:
> The
> inVerBe
> (1/x)
> TTansfoIms high
> imbalance
> Into
> Ioy
> Values
> anC
> CHe
> negative sign
> (-〉 Iips
> The
> OUTpU
> PTLOIICIZe
> Conci-inns Where
> The OLiginal
> SCOIe
> Is negative (e.8
> sellIng pressuTe)
> bUT
> OWI
> appears
> positive signals
> 25
> ODeratozCount
> 25
> 27
> UateCzeated "
> 2025
> 09-09T01:43:59
> 04:00
> 28
> "dateSubmitted "
> 2025-09-09102:20:35-04:00
> "datelodified
> 2025-09-13109:42:37
> 04:00
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> alpha C


只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符

2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 08/14/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(2
> rsk72_atopzooO_dsrt
> rank
> mdl26
> FLtV
> rsSII
> 2000_30_
> Power Pool Alpha
> Pyramid theme: CHNIDIIRISK X1.4
> Simulation Settings
> Pyramid theme: CHNIDIIMODEL X1.6
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaNHar
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.59
> 48.989
> 0.96
> 17.739
> 14.389
> 7.249600
> Equity
> CHN
> TOPZOOOU
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,00
> 50.9796
> 2.14
> 25.8395
> 3.459
> 10.14930
> 376
> 311
> Clone Alpha
> 2014
> 3.19
> 50.37%6
> 2.39
> 28.3395
> 4.5996
> 11.259530
> 449
> 375
> 2015
> .99
> 43.99%
> 1.76
> 32.2995
> 14.38%
> 15.5935o
> 726
> 502
> 2016
> 2.15
> 46.26%
> 22.0595
> 5.0596
> 9.5390
> 675
> 556
> Chart
> Pnl
> 2017
> 0.46
> 46.93%
> 0.14
> 43895
> 8.6795
> 879530
> 595
> 501
> 2018
> 1.31
> 48.3796
> 0.64
> 11.6395
> 4.6796
> 83900
> 554
> 455
> 2019
> 2.07
> 50.56%
> 1.22
> 17.6995
> 4.11%
> 9850
> 524
> 420
> 2020
> 0.17
> 50.68%
> 0.03
> -1.9695
> 10.9096
> 0.77930
> 542
> 427
> 1ON
> 2021
> 51.20%
> 0.38
> 11.1295
> 9.73%
> 4.34900
> 543
> 425
> 2022
> 50.5696
> 1.12
> 20.1999
> 5.7390
> 7.979530
> 552
> 447
> 5,00OK
> 2023
> 10.25
> 50.3896
> 10.51
> 52.9395
> 2496
> 21.019500
> 562
> 484
> Risk neutralized
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> 1.17
> 48.989
> 0.39
> 5.4296
> 18.579
> 2.219600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.52
> 42.179
> 0.97
> 17.049
> 14.409
> 8.089600
> IS Testing Status
> Period
> IS
> 05
> [
> Correlation
> 8 PASS
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 6;01
> Turnover of 48.989 is above cutoff of 1%
> PM
> Turnover of 48.98% is below cutoff of 70%
> Weight is well distributed over instruments。
> Returns Of 17.73% is above cutoff of 8%.
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 6;01
> Sub-universe Sharpe of 1.55 is above Cutoff of 1.13.
> PM
> Robust universe Sharpe of 1.30 is above CUtoff of 0.64 (40% of Alphal
> 0.8918
> -0.2468
> Robust universe returns of 9.139 is above cutoff of 7.09% (40% of Alphal.
> These pyramid themes match with the following multipliers: CHN/DI/RISK-
> 1.4; CHNIDIIMODEL
> 1.6.The final
> pyramid theme multiplier is 1.4. Effective pyramid count for Genius is 2。
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 6;01
> PM
> 5WARNING
> 0.8234
> -0.6297
> Sharpe of 1.59is below CUtOff of 2.07.
> chng


我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi. worldquantbrain comlalphas/SdnGl4z
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 17.925
> 2.3 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三 Q6 &
> 15
> IaXTTaCE
> OFF
> operatorcount
> 酏*
> 1Of1
> 个 b = X
> 17
> "language
> IFASTEXPR"
> 18
> IVis0a1i2ation"
> false
> 19
> startDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> TegUIaT"
> 23
> COCE
> raIk (2
> ISk72_a20p2000_
> OSIT)
> raIk (3
> 10125_
> Chng_IICV_T_
> 工5511
> 2000_
> 30)
> 24
> "description"
> Iaea:
> Dual-Iank PIOCUCT
> Signal
> Combining
> SHOIT
> MnTerest
> anC
> RSS
> Iquidity
> Changes
> 1nRaTi3na12
> for 0a-a
> USeC:
> 1 -
> ISK72
> aTOp2OOO_OSIT:
> RUSSeII
> 2000
> SHOIT
> MnTerest
> percentile
> {几-
> Ic126_chng_
> IITV_T_ISSII
> 2000_
> 30:
> 30 -
> IelatIve Izquzdity
> Change
> SCOIC
> InlnRaionale
> fJI
> OpeIaTOIS
> USee
> 1-
> EXpOnenTiaI
> TransforIs
> CIeaTe
> COIVCX
> Ianking:
> 3a5e-2:
> SHOIT
> Interest
> aMplification
> 3a5e-3
> Htouidity
> change sensitivity
> 1 -
> MulTiplicaive
> Combinazion:
> High when
> boTh
> signals
> agTeE
> Near- ZeIn
> when
> eiTher
> neUTIaI
> {- Negative
> SIgn
> CargeTs:
> High
> SHOIT
> MnTerest
> CeTeriorating
> liquidity
> 1"5hoI
> 50UeeZe
> TIap
> ioentification
> OpezatozCount
> 25
> 27
> "datecreated "
> 2025
> 08-14T05:27:35-04:00
> 75
> rateSwhmitterl"
> 2025-08-15T01:04:25-04:Q0
> alpha C
> day


重复算 operatorCount 操作符了 .

没有  **字段使用数量信息** ，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .

[图片 (图片已丢失)]

**重点** ：巧妙的节省重复操作符 ！！！

从以上几个alpha操作符测试，让我们知道了

i ) +、-、*、/ 和 ^ 都是算入操作符计数的；

ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；

iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha

3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/12/2025 EDT
> anonymoUs
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> brk
> VeC
> Sum(brkl_start_stock_price);
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIBROKER X1.5
> alpha
> ts covariance
> bpk,
> 股票起始价格汇总
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> bpk
> 11同一序列的自相关讦算
> 1.05
> 13.439
> 0.86
> 9.059
> 10.689
> 13.479600
> 24
> 24周期(约1个月)滚动窗0
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0,80
> 14.3096
> 5.2995
> 5.0195
> 40930
> 1157
> 1571
> Instrument Tpe
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> 2014
> .85
> 12.39%
> .90
> 13.2495
> 3.239
> 21.369600
> 1424
> 1722
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> On
> OfT
> 2015
> +28
> 12.59%6
> 1.28
> 12.6295
> 7.6596
> 20.05930
> 1537
> 1751
> 2016
> 1.36
> 13.59%
> 1.57
> 18.2595
> 9.249
> 26.67930
> 1477
> 1690
> 2017
> 0.63
> 11.4796
> 0.32
> -3.20%
> 6.959
> -5.5893o
> 1746
> 1497
> Clone Alpha
> 2018
> 0.72
> 12.4696
> 0.52
> 5.469
> 8.5096
> 10.379530
> 1980
> 1765
> 2019
> 13.25%
> 1.71
> 13.5695
> 5.18%
> 20.47930
> 1757
> 1611
> 2020
> 0.47
> 15.54%
> 0.25
> 2.4495
> 7.5096
> 68930
> 1818
> 1731
> Chart
> Pnl
> 2021
> 14.52%
> 1.17
> 10.8195
> 4.0096
> 14.79930
> 2194
> 2300
> 2022
> 1.17
> 13.7096
> 0.94
> 8.759
> 6.35%
> 12.779530
> 1980
> 2197
> 2023
> 0.48
> 20.3796
> 0.17
> 26Ob
> 8296
> 2.5593o
> 1640
> 1992
> 7,50OK
> SOOOK
> Correlation
> 2,50OK
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,8;43
> Du
> 0.2112
> -0.0733
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
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 8;43
> PM
> 0.4247
> -0.0733
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 8;44
> PM
> 0.3960
> -0.3483


我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain comlalphaslobd5qOE
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 2.545
> 2.41 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> nanHandling"
> OFF
> operatorcount
> 劭
> ? Of1
> 个 b = X
> 16
> IaXTTaCE
> ON
> 17
> "language
> FASTEXPR
> 18
> IVis0ali2ation
> false,
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE"
> Ibrk
> VeC
> SUII ( bIkz_
> STAIT_
> sTOCk_priCe ) ; Irlnalpha
> C5_
> Covariance (IIin
> DIK,
> L 股票起始价格汇总 Irln
> bIk ,
> LL 同-序列的
> 自相关计算 {210
> 24
> J24周期〈约1个月)滚动窗OIrln) ; '
> 24
> "JesCZIptiOn"
> Iaea:
> COIpUTE
> the negatlve IoIIIng
> COVariance
> Of aggTegated
> starting stock prices with itself
> Iea5UIE
> 5e11-similarity
> anO
> invert
> The
> Ielationship
> InRationale
> fJI
> USeO:
> The aggIe
> starting
> STOCK priCe
> (VeC_
> SUII
> (brki_
> STaIT
> sTOCk_price)
> IeTIeCTS
> baseline
> Valuation
> levels
> 35
> boTh
> IpUTS
> COVariance
> CapTUIeS
> i5
> OIII
> Volatility
> and pattern
> consistency
> InRaTionale
> for OperatoIs
> USeC:
> The
> 24-period
> COVariance
> (TS
> COVariance)
> SeIies Iizh
> iself simplifies
> VaTZance
> measUring
> HOWI Uispersed
> The
> Values
> aIe
> aIOUnC
> Their
> IIean
> DVEI
> ShOIt
> term Window.
> The
> negative
> sign (-)
> TIVeITS
> 375,
> 50
> higher
> Variance (inszability)
> IeSUITs
> 11
> IOIeI
> 518na1 ,
> penalizing
> VoIatility
> 25
> OpezatozCount
> 25
> alpha C
> Jaza
> gazed
> Using


事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/01/2025 EDT
> jiao?
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> Vector
> neut
> VeC
> SUN(rSKGG
> offer),
> VeC
> SUm(rsk6o
> Offer)))
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> Simulation Settings
> 1.33
> 10.339
> 1.05
> 7.819
> 16.029
> 15.139600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Equity
> USA
> ILLIQUID_MINVOLIM
> Fast Expression
> 0.08
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.009
> 0.00
> 0.0096
> 00%
> 0093o
> 2014
> 1.30
> 7.1995
> 0.77
> 4.4296
> 1.6296
> 12.36950
> 936
> 1552
> 2015
> -0.29
> 7.5095
> -0.21
> 2.28%
> 8390
> 079330
> 716
> 1825
> Clone Alpha
> 2016
> 1.03
> 7.3295
> 5.4796
> 0996
> 14.93930
> 539
> 1878
> 2017
> 0.77
> 8.3595
> 3.36%
> 4.839
> 0593o
> 555
> 832
> Chart
> Pnl
> 2018
> 1.07
> 13.9099
> 5.29%
> 2.5795
> 7.62930
> 577
> 888
> 2019
> 0.95
> 13.0395
> 5.5596
> 4.98%
> 8.5390
> 512
> 1905
> 2020
> 1.25
> 11.1495
> 1.16
> 10.6596
> 5.11%
> 19.139500
> 464
> 1922
> 2021
> 0.91
> 10.1895
> 0.b
> 79%
> 12.53%
> 13.34930
> 2248
> 2022
> 5.02
> 14.389
> 7.52
> 32.31%
> 2.2796
> 44.9493o
> 1070
> 1821
> 40OOK
> 2023
> -1.55
> 10.6890
> -1.48
> -11.40%
> 2.35%
> -21.32930
> 752
> 1893
> 20OOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;55
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
> Du
> 0.3766
> -0.1774
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;55
> PM
> 0.3713
> -0.1928
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;55
> 00
> IS Testing Status
> Period
> OS
> PM
> 0.6809
> -0.5425


这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =

1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .

[图片 (图片已丢失)]

2. 点塔！

```
点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题
```

当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节： [交一个怎样的alpha能提升你的六维数据之定性定量分析 .]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！

关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：

i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)

[图片 (图片已丢失)]

比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 . 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(anl3g
> rOXLCXSpeq
> anl3g_xIcxspemtp)
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> RetUrns
> DrawOOwn
> Margin
> Simulation Settings
> 0.37
> 3.549
> 0.14
> 1.869
> 13.18%
> 10.539600
> Instrument Tpe
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.71
> 3.769
> 1.30
> -7.22%
> 11.439
> -38.389530
> 775
> 1332
> 2014
> 1.18
> 3.1795
> 0.75
> 5.0096
> 3.51%
> 31.53950
> 1058
> 1558
> 2015
> 0.37
> 3.4295
> 0.15
> 2.1796
> 7.36%
> -12.67900
> 1156
> 1557
> Clone Alpha
> 2016
> 1.83
> 3.8795
> 1.84
> 12.6796
> 3.21%
> 65.529530
> 1093
> 1627
> 2017
> 0.58
> 3.3295
> 0.32
> 2.6996
> 5.33%
> 16.2390
> 1172
> 1779
> Chart
> Pnl
> 2018
> 1.81
> 3.43995
> 1.42
> 7.42%
> 3.40%
> 43.25930
> 1135
> 1792
> 2019
> -U.61
> 3.3995
> 0.33
> 3.029
> 4.92%
> -17.9390
> 004
> 1825
> 2020
> 3.5395
> 0.10
> 5696
> 5.6796
> 8.84930
> 998
> 1752
> 2021
> 1.38
> 3.8595
> 5.5896
> 4.20%
> 28.97930
> 1855
> OOOK
> Mlwto
> 2022
> 0.32
> 3,6695
> 0.13
> 9996
> 859
> 10.8593o
> 1072
> 830
> 2023
> -3.70
> 3,0095
> 2.01
> -14.5890
> 0090
> 97.97930
> 970
> 1792
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Margin
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
> 0.27
> 2.2296
> 0.09
> 1.4096
> 14.639
> 12.579600
> Pnl
> Investability Constrained Pnl
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;36
> PM
> 0.2624
> -0.0448
> IS Testing Status
> Period
> OS
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;37
> PM
> 0.8554
> -0.6340
> 5PASS


通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 07/30/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank
> star
> Val
> industry_rank
> anl39
> rOXLCXSpeq
> anl39_xlcxspemtp
> Power Pool Alpha
> Pyramid theme: EURIDIIMODEL X1.4
> Simulation Settings
> Pyramid theme: EURIDIIANALYST X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.45
> 7.5596
> 1.91
> 7.629
> 4.2396
> 20.189600
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> On
> On
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.70
> 6.7096
> 1.04
> 46895
> 1.289
> 13.98900
> 778
> 1329
> Clone Alpha
> 2014
> 3.25
> 7.59%6
> 2.69
> 8.5495
> 1.149
> 22.5035o
> 1070
> 1525
> 2015
> 1.27
> 7.84%
> 0.72
> 2.0595
> 2.839
> 10.359500
> 1113
> 1611
> 2016
> 4,09
> 8.03%
> 2.34
> 12.0895
> .20%
> 35.07930
> 1025
> 695
> Chart
> Pnl
> 2017
> 2.61
> 7.3396
> 1.75
> 5.6295
> #1090
> 15.3390
> 1120
> 831
> 2018
> 3,05
> 7.7096
> 2.30
> 7.10%
> 2.0590
> 18.43900
> 1166
> 1750
> 2019
> 1.27
> 7.56%
> 62
> 3.0195
> 1.70%
> 7.95930
> 1183
> 1625
> 2020
> 2.34
> 8.01%
> 1.94
> 8.6095
> 1.72%
> 21.469530
> 1121
> 1621
> 5OOOK
> 2021
> 2.71
> 86%
> 2.35
> 9.4095
> 3.52%
> 27.40950
> 1122
> 1820
> 2022
> 2.45
> 7.81%6
> 2.27
> 10.75%
> 4.2390
> 27.51930
> 1163
> 1739
> 2,50OK
> 2023
> 3,80
> 7.5596
> 3.63
> 11.8095
> 0.489
> 31.269500
> 1093
> 1672
> Investability constrained
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.88
> 3.599
> 1.30
> 5.9796
> 3.9796
> 33.269600
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025,7.05
> PM
> 00
> IS Testing Status
> Period
> 05
> 0.5189
> -0.0937
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> 8 PASS
> PM
> 0.5189
> -0.1529
> Sharpe of 2.45 is above CUtOff of 1.58.
> Fitness Of 1.91 is above cutoffof1.
> Turnover of 7.5596 is above CUtoff of
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> PM
> Turnover of 7.55% is below cutoff of 70%.
> Weight is well distributed over instruments。
> 0.8288
> -0.4965
> Sub-universe Sharpe of 1.27 is above cutoff of 1.27.
> IS Iadder Sharpe Of 2.49 is above cutoff of 2.02 for Iadderyear 2: 1/20/2023.1/21/2021


ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> OS
> ts_target_
> tvr_decay (imbs_
> SCOre
> Iambda_min-o,
> Iambda
> maX=l, target
> tVr=0.1
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> Simulation Settings
> 2.86
> 7.7796
> 1.98
> 5.979
> 2.319
> 15.379600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.32
> 7.96%
> 2.54
> 7.3295
> 009
> 18.40950
> 1363
> 1355
> 2014
> 5.73
> 7.0796
> 5.12
> 9.999
> 0.739
> 28.259530
> 1569
> 1577
> 2015
> 4.83
> 7.5196
> 264
> 11.5495
> 1.289
> 30.7390
> 1645
> 653
> Clone Alpha 
> 2016
> 2.76
> 7.3796
> .82
> 5.42%
> .6890
> 14.71930
> 1574
> 593
> 2017
> 2.23
> 7.51%
> 3.00
> 5.2995
> 639
> 16.52930
> 1610
> 533
> Chart
> Pnl
> 2018
> 3.49
> 7.81%
> 2.54
> 6495
> .239
> 6.93930
> 1875
> 1871
> 2019
> 2.96
> 7.5596
> 2.04
> 5.9195
> 1.129
> 15.45930
> 645
> 1723
> 2020
> 8.30%6
> 22795
> 1.729
> 5.48930
> 1736
> 1813
> 2021
> .05
> 299
> 2.43%
> 2.31%
> 5.86930
> 2203
> 2291
> 40OOK
> 2022
> 7.97%6
> 0.22
> 1.5195
> .839
> 3.79950
> 2057
> 2121
> 2023
> 11.09%
> 5.57
> 8.2395
> 08%
> 14.85930
> 1783
> 1829
> ZOOOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;33
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
> PM
> 0.3352
> -0.0929
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> Du
> 0.5597
> -0.1764
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> IS Testing Status
> Period
> 0S
> Du
> 0.9227
> -0.5410
> Year


比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .


> [!NOTE] [图片 OCR 识别内容]
> 说到这里,
> 我想说一下关于提交 alpha 关于 Prod Correlation ,
> Power Pool
> Correlation 和 Self Correlation,
> 也许在绿灯亮起提交 alpha 显示出的错误或许不
> 那么明确. (个人看法,如有问题还望大佬们不忘吝啬,
> 可评论区说明我好做出调
> 整)但大致是这样的 .
> 举个例子:有一个国王喜欢吃各种各样式的苹果
> 大家都会送苹果给国王
> 吃,
> 当然会获得相应的报酬,吃之前需要将苹果放进池子进行清洗,
> 有两个大小
> 的池子。如果你送来的苹果好,自然是放在大池子里。和大池子里的苹果比较 ,
> 如果大池子没有类似的苹果,
> 或者如果有类似的苹果,
> 但是你的苹果比这个类似
> 的苹果有更少的瑕疵,那你的苹果将会被收取从而获得报酬;  如果你的苹果不满^
> 足大池子,
> 那就继续按照以上这种方式放小池子,
> 当然这种小池子只是大家人手
> 一个,
> 大池子也是谁想用可以随时搬自己家测试,
> 小池子的作用是什么,如果大
> 池子的苹果被国王吃完了,那就会考虑小池子了,当然人家毕竟是国王,没有那
> 么容易吃完大池子的稀奇苹果.



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 09/11/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> ts_target_
> tvr_decay (imbs_
> SCOre
> mCr63_membership,  Iambda
> min=0
> Iambda
> Iax=l
> targe
> Power Pool Alpha
> Pyramid theme: ASIIDIIIMBALANCE X1.1
> Simulation Settings
> Pyramid theme: ASIIDIIMACRO X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 7.739
> 1.19
> 5.249
> 5.899
> 13.56900
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> 0n
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.03
> 8.02%
> 1.34
> 5.4795
> 2.0596
> 13.63330
> 1377
> 1351
> Clone Alpha 
> 2014
> 2.21
> 7.0596
> 407
> 11.659
> .76%
> 33.089500
> 1573
> 1573
> 2015
> 3.41
> 7.4796
> 293
> 9.20%
> 1.129
> 24.61930
> 670
> 628
> 2016
> +94
> 7.45%6
> 0.47
> 3.16%
> 5.8990
> 48930
> 590
> 1577
> Chart
> Pnl
> 2017
> 2.28
> 7.50%
> 2.8895
> 1.6596
> 12.84930
> 620
> 1623
> 2018
> 2.55
> 7.74%
> .84
> 5.5395
> 1.2996
> 16.879500
> 899
> 1827
> 2019
> .83
> 7.5496
> 1.14
> 4.8795
> .9890
> 12.91930
> 1705
> 653
> 2020
> 0.02
> 8.3296
> 0.00
> 0.059
> 2.259
> 0.1593o
> 800
> 1729
> 2021
> 8.18%6
> 1.21
> 5.159
> .6390
> 12.5893o
> 2305
> 2190
> 2022
> 7.82%
> 0.07
> 0.8795
> 2.5696
> 2.239500
> 2113
> 2055
> ZOOOK
> 2023
> 3.80
> 10.50%
> 3.02
> 7.9295
> 0.1996
> 15.08930
> 864
> 1757
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;43
> PM
> 0.3474
> -0.0437
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.3645
> -0.0892
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.6217
> -0.4420
> PASS
> Vear


事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .

[图片 (图片已丢失)]

3. 好而优的 alpha

何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .

一点：好，我理解在:

1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；

2) fitness ≥ 1  全方面稳定还是非常不错；

3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；

4) returns ≥ 10%  收益还是要好点能赚钱吧；

5) drawdown 回撤越小越好吧，大了心理抗压不行；

6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；

7) 十年数据中做多做空不能太少吧，权重太高危险危险！

8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .

满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/08/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> 1
> OS Summary
> Period
> I5
> 05
> peVerse(r
> ib5
> SCOre
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDOIIMBALANCE
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> Simulation Settings
> 0172112023 CT
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Close
> Close Ratio
> Self-Correlation
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone Alpha
> 2013
> 3.9
> 23.8899
> 4.13
> 26.189
> 2.5995
> 21.929600
> 986
> 405
> 2014
> 3.52
> 22.6895
> 3.36
> 20.65%
> 2.9096
> 18.22930
> 1070
> 431
> 2015
> 3.32
> 22.8295
> 3.46
> 24.43%
> 3.03%
> 21.41950
> 1130
> 459
> Chart
> Pnl
> 2016
> 2.53
> 21.1195
> 2.65
> 21.4796
> 3.4796
> 20.349530
> 1138
> 455
> 2017
> 2.77
> 20.7795
> 2.47
> 16.5496
> 3.40%
> 15.92930
> 1125
> 470
> 2018
> 1.88
> 19.5696
> 1.67
> 15.3796
> 7.27%6
> 15.71930
> 1010
> 418
> 2019
> 2.77
> 19.1395
> 3.03
> 22.829
> 3.18%
> 23.8890
> 998
> 423
> 1ON
> 2020
> 0.71
> 19.4395
> 0.39
> 5.9596
> 5.659
> 2930
> 908
> 392
> 2021
> 1.73
> 19.20%
> 10.789
> 5.089
> 11.22930
> 972
> 416
> 5OOOK
> 2022
> 18.4390
> 1.42
> 14.789
> 4.5795
> 16.0493o
> 050
> 439
> 2023
> 10.22
> 31.6599
> -14.39
> 62.7790
> 3.5796
> 39.67930
> 945
> 393
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
> Pre
> Sharpe
> Pre


二点：优，我理解在:

1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；

2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；

3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；

使用


> [!NOTE] [图片 OCR 识别内容]
> 1
> 1.
> 事件距离基础信号:  距离越大。事件影响越小
> eVent
> signal
> VeC
> SUI
> nWs7g_event_detection_distance_358-
> 1
> 距离平方增骚:  放大极端距离信号的非线性影响
> brk
> VeC
> sum(brkl_start_stock_price);
> distance_squared
> event_signal
> 2;
> alpha
> ts covariance(
> brk,
> 股票起始价格汇总
> 1
> 词频倒数因子:  词数越少。信息浓度越高(1/词数)
> brk,
> 11  同一序列的自相关计算
> Word
> density
> 二 1
> VeC
> SUII
> nWS7g_word_count_391 )
> 24
> 24周期(约1个月)滚动窗口
> 10
> 1
> 复合事件驱动因子:  距离信号
> 非线性增骚
> 信息浓度
> 11
> alpha
> (event_signal
> distance_squared
> Word_density)



> [!NOTE] [图片 OCR 识别内容]
> 11 Core Logic:
> Reverse standardized composite factor
> reverse
> operation when large trader behavior diverges
> 1
> Synthetic
> Base
> Factor: Market
> pattern
> trader Value differential
> base factor
> mdl175 OGam
> power(Vec
> sum(pvz7_value_diff_large_trader), 2);
> /12. standardization: Convert to
> Z-score to eliminate scale effects
> Zscore_factor
> Zscore(base_factor) =
> 1
> Signal Reversal: Negative sign indicates
> Contrarian
> selection, seeking
> undervalued
> opportunities
> alpha
> ZSCOre
> factor;
> large



> [!NOTE] [图片 OCR 识别内容]
> Description
> 507
> 100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template_
> Idea: Identify the time index ofthe maximum imbalance score over a 2O-day Window, then invert the result:
> Rationale for data used: The imbalance score (imb5_score) likely measures order flow or liquidity asymmetry; its maximum pinpoints the
> most extreme positive imbalance event。
> Rationale for operators Used: The 20-dayarg max (ts_arg_max)returns the lookback period (0-19) where the series peaked_and the


不建议使用


> [!NOTE] [图片 OCR 识别内容]
> 1 |
> ts_covariance(vec
> SUm(brkl_start_stock_price) ,
> VeC
> sum(brkI_start_stock_price), 24)



> [!NOTE] [图片 OCR 识别内容]
> brk
> VeC
> sum(brkl_start_stock_price)
> alpha
> ts covariance
> brk,
> 股票起始价格汇总
> bk,
> 11同一序列的自相关计算
> 24
> 1124周期(约1个月)滚动窗口
> );
> alpha


[图片 (图片已丢失)]

**三、alpha模板 ！**

看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .


> [!NOTE] [图片 OCR 识别内容]
> N-1
> Ha
> 1,3N,8.七
> lim
> fa()-Cfa(a)
> 二
> Iim
> fa(a)
> n-〉+O
> n〉+O
> 2二1
> 2二1
> C=N
> 10-P


换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！

field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .

其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> 2,000
> UUJ
> OIlU
> 〈ee
> 3" A0。
> 02
> Displayed Period
> 02/14/2025
> 09/12/2025
> 149346
>  Mar
>  Mar
> Mar
> Mar
> Mar
> 30。
> 31。
> 24。


从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .

[图片 (图片已丢失)]

使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .

造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .

[图片 (图片已丢失)]

下节预告:  [Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

2025年9月14日

**顾问 WX64154 (Rank 32) 的解答与建议**:
感谢大佬分享。给我深深上了一课，期待下节。

想知道大佬怎么把combine刷的那么高


---

### 技术对话片段 55 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 冲刺genius !
> 细节决定成败,你的六维还能提升 ! &模板
> 
> 
> 首先感谢游戏王 (2559763) ,
> 橘子姐
> (6383096) ,
> base payment 拉满的
> 大佬 (AH18340) 以及 上海 (MF59400)等等的帮助.也许你们自己都不知道 ,
> 但是潜移默化
> 的影响了我,
> 下面阐述的其中有-些内容是我在游戏王那里学习到的.


## **一、Genius定级与何相干？**

总体来说，一共与两方面有关，一是  **硬性指标** ，二是  **软指标** 。


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-03,July 1st, 2025
> September 3Oth; 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 266
> Reached Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 72
> Reached Grandmaster
> 10
> 30
> Combined Alpha Performance
> 2.39
> Reached Grandmaster
> 0.5


其中  **硬性指标** 包括由

1. 本季度 Signals (阿尔法)；

2. 本季度 Pyramids (金字塔)；

3. Combined Alpha Performance (提交的所有alpha表现)；

4. Combined Selected Alpha Performance (被选中的alpha费后表现)

5. Combined Power Pool Alpha Performance (power pool alpha表现)

五部分组成；

```
点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。
```

我们以Expert (专家)为例，硬性指标必须同时满足

1. 本季度alpha数量 Signals ≥ 20；

2. 本季度金字塔数量 Pyramids ≥ 10，

3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5

       这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).

[图片 (图片已丢失)]

**软指标** 又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。

**
> [!NOTE] [图片 OCR 识别内容]
> What happens 迂 more consultants qualify for a level than there are available
> If more consultants meet the base criteria for
> level than there are available Spots
> a tiebreaker criterion is used _
> This is based on a sum Of ranks across the following metrics
> 1.
> distinct Operators
> Alpha (Lower is better )
> 2.
> distinct Fields
> Alpha (Lower is better)
> 3. Total distinct Operators (Higher is better)
> 4
> Total distinct Fields (Higher is better)
> 5. Maximum Simulation Streak
> Best streak of
> consultant that ends i that quarter
> OI
> continues into the next quarter
> Streak does not reset to 0 every quarter。
> 6. Community leader
> Forum
> Number Of Likes on Posts Or comments that are
> published as Of the end Of quarter
> Ninimm length of post Or comment must be 100 characters。
> Referral
> Total number Of successful referrals i the quarter
> A referral is considered
> Slccessfil
> Khen the
> referring consultant h as become eligible to accrte the referral fee for someone
> have referred to BRAIN
> 讧 accordance with the guidelines Of the referral fee program
> Spots?
> Avg
> AVg
> they
**

**
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st, 2025
> September 3Oth, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.41
> 68
> 1.54
> Fields used
> Community activity
> Max simulation streak
> 260
> 33.2
> 88
**

其中  **软指标** (六维数据)包括由本季度

1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；

2. Operators used (操作符的去重使用个数)；

3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；

4. Fields used (字段使用(去重)数量)

5. Community activity (rank[社区活跃程度])

6. Max simulation streak (最大连续回测天数)

六部分组成；

```
·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。
```

[图片 (图片已丢失)]

## **二、冲刺 Genius !**

通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。

1. 关于六维数据  **细节**

这部分我们娓娓道来，关于六维数据我们能做的是什么?

i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；

ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；

iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；

iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；

v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .

首先，讲讲我的一些  **蠢行为! ,** 等等上面还有一点重要的忘记说了， **要保持区域、Delay以及数据集多样性！**

**
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st, 2025
> September 3Oth, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Fundamental
> Insiders
> Macro
> Mogel
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Social Media
> Earnin3s
**

使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多  **8~10**  个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Delayo
> NAN
> Delayl
> NAN
> Fundamental data
> Fundamental data
> Analyst data
> Analyst data
> Broker
> Broker
> News data
> News data
> Social media data
> Social media data
> Sentiment data
> Sentiment data
> Price VOluMe data
> Price Volume data
> Option data
> Option data
> Eamings
> Earnings
> Insiders
> Insiders
> Instiutional Ownership Data
> Instiutional Ownership Data
> Short interest data
> Short interest data
> Macro data
> Macro data
> Other
> Other
> Risk data
> Risk data
> Model data
> Model data
> USA
> ASI
> CHN
> EUR
> GL
> HKG
> KOR
> TVN
> AMR
> JPN
> USA
> ASI
> CHN
> EUR
> GLB
> HKG
> KOR
> TVN
> AMR
> JPN
> Click to drill down
> EUR
> ASI
> GLB
> USA
> CHN


保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.

[图片 (图片已丢失)]

接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/26/2025 EDT
> 顾问 ML47973 (Rank 100)
> Add Alphato
> LiSt
> Code
> IS Summary
> Period
> IS
> 05
> power(2,
> md177_astcomp
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> Simulation Settings
> 1.65
> 6.11%
> 2.64
> 31.939
> 16.609
> 104.449600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Subindustry
> On
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 1.69
> 5.46%
> 1.56
> 10.65%
> 4.76%
> 39.05920
> 1999
> 357
> 2019
> 4.949
> 1.71
> 18.5896
> 8.66%
> 75.279620
> 1988
> 375
> 2020
> -0.,04
> 029
> 0.01
> 0.5596
> 15.18%
> 82920
> 2010
> 375
> Clone Alpha 
> 2021
> 2.46
> 699
> 4.84
> 48.489
> 15.30%
> 122.899620
> 2142
> 380
> 2022
> 2.44
> 7.42%
> 6.08
> 77.70%
> 13.23%
> 209.41920
> 2136
> 390
> Chart
> Pnl
> 2023
> 3.61
> 6.13%
> 7.40
> 52.519
> 1.71%
> 171.19920
> 2114
> 397
> 匣
> Correlation
> 1ON
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,4;51
> PM
> 0.6840
> -0.0542
> OOOK
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,4;51
> Du
> 0.4204
> -0.1633
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 4;51
> 0
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul "22
> Jan '23
> Du
> 0.6874
> -0.6201
> Vear



> [!NOTE] [图片 OCR 识别内容]
> 这个 Q 当时让我 base payment 日 赚54.816 ,当时 iqc 结束 ,第一次0f更新0.86


直到我使用华子哥的插件才发现


> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 美东时间:2025/9/1200:38:06 北京时间: 2025/9/1212:38:06
> 在你可用的运算符中。共有67种运算符被使用。12种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统一为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x, Y, filter
> false); X + y
> 52
> COMBO,REGULARSELECTION
> base
> Arithmetic
> multiply(x ,y
> filterzfalse); X * y
> 76
> COMBO,REGULARSELECTION
> base
> Arithmetic
> sign(x)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> subtract(x, Y, filter-false) X -Y
> 157
> COMBO,REGULARSELECTION
> base
> Arithmetic
> pasteurize(x)
> COMBO,REGULAR
> genius
> Arithmetic
> log(x)
> COMBOREGULARSELECTION
> base
> Arithmetic
> maXfx;y
> COMBO,REGULARSELECTION
> base
> Arithmetic
> absfx)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> divide(x; y), XIy
> 158
> COMBO,REGULARSELECTION
> base


我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！

下面的操作有几率  **降低** 你的  ***Operators per Alpha*** ，和想要查看自己的alpha数据也可以认真看一下

在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)


> [!NOTE] [图片 OCR 识别内容]
> #  登录 (login)url
> CUrl
> --location
> --request
> POST
> https : / /api. worldquantbrain . com
> authentication
> header
> Authorization:
> Basic MZAZODUBMTAZOEBXcSSjbzeGQUYrQUYrQUYgMBFG
> ~-header
> Cookie:
> t=eyJeeXAiOiJKVIQiLCJhbGciOiJIUZIINiJg .eyJqdGkioi -



> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> login
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> POST
> https:Hapi.orldquantbrain comlauthentication
> Send
> Environments
> POST Simulation
> Params
> Authorization
> Headers (10)
> Body
> Scripts
> Settings
> Cookies
> PATCH alpha-adjust
> FIOws
> Auth Type
> GET data-fields
> Username
> 30-510
> COm
> Basic Auth
> GET alpha
> History
> GET Check
> Password
> The authorization header will be
> POST submit
> 0+
> automatically qenerated when yoU send the
> GET Self-COrr
> Body
> Cookies
> Headers (20)
> Test Results
> 201 Created
> 1.975
> 1.14 KB
> Save Response
> GET data-sets
> JSON
> Preview
> Visualize
> 三
> Q  @
> GET
> pyramid
> USET"
> id
> 顾问 ML47973 (Rank 100)
> Loken"
> EXDiTy
> 14400
> DeTmissions
> BEFORE
> ANID_
> AFTER
> PERFORMANCE_
> 10
> BRAIN_LA3S"
> 11
> BRAIN_LABS_JUPYTER
> L43
> 12
> CONSULTANTI
> 13
> "MULTI_SIMULATION "
> 14
> PROD_ALPHAS
> 15
> REFERRAL
> 16
> SUPER_ALPHA "
> 17
> IVISUALIZATION"
> 18
> WORKDAY"
> 19
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> 9@.


下面的是查询alpha信息的url


> [!NOTE] [图片 OCR 识别内容]
> #
> check_alpha_info 其中{alpha_id} 使用alpha_id替代即可
> Curl
> -location
> https : / /api .worldquantbrain . com/alphas / {alpha_id}
> -header
> Cookie:
> tseyJeexAioiJKVIQiLCJhbGciOiJIUZIINiJ9 .eyJqdGkioi


接下来我们就来看看几个alpha，查看它们的数据情况

1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/09/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> ib5
> SCOFe
> Single Data Set Alpha
> 俳
> Power Pool Alpha
> Pyramid theme: EURIDIIIMBALANCE X2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> Simulation Settings
> 3.37
> 22.089
> 2.26
> 9.9396
> 2.4596
> 9.009o0
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.02
> Statistical
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.19
> 23.9499
> 200
> 14.1990
> 1.08%
> 11.8590
> 1324
> 781
> 2014
> 4.55
> 23.2595
> 3.25
> 11.85%
> 0.78%
> 10.20950
> 1612
> 1005
> 2015
> 4.20
> 23.68%
> 3.26
> 13.02%
> 1.31%
> 11.00930
> 1101
> Clone Alpha
> 2016
> 4.52
> 22.9795
> 3.52
> 13.78%
> 1.65%
> 11.99930
> 627
> 1092
> 2017
> 4.22
> 22.0095
> 2.79
> 9.519
> 0.9190
> 8.72930
> 1749
> 1203
> Chart
> Pnl
> 2018
> 3.4
> 21.699
> 2.37
> 10.29%
> 20%
> 499
> 1714
> 1212
> 2019
> 3.26
> 21.4495
> 2.26
> 10.32%
> 1.23%
> 52930
> 1665
> 1162
> 2020
> 1.99
> 21.1495
> 1.12
> 6.6296
> 2.4596
> 2890
> 1616
> 1125
> 2021
> 2.52
> 20.1895
> 47
> 6.729
> 1.02%
> 58930
> 1703
> 1259
> 7,50OK
> 2022
> 1.37
> 20.139
> 0.67
> 4.839
> 2.29%
> 4.80930
> 652
> 1240
> 5,0OOK
> 2023
> -11.03
> 29.179
> 10.18
> -24.859
> 1.539
> -17.0293o
> 1505
> 1077
> 2,50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.99
> 8.649
> 1.44
> 6.5296
> 8.4096
> 15.089600
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 5;43
> PM
> 0.1456
> -0.0393
> 00
> IS Testing Status
> Period
> 05
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 5;43
> PM
> 0.6239
> -0.0916
> 6 PASS
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 5;43
> Sharpe Of 3.37 is above CUtOff of 1.58。
> PM
> Fitness Of 2.26 is above cutoff of 1
> 0.7043
> -0.3995
> Turnover of 22.089 is above cutoff of 1%
> Turnover of 22.08% is below cutoff of 70%


仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain.comlalphas BOPXEEZ
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 3.06
> 2.19 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> IaXTTaCE
> OFF
> operatorcount
> _
> 1Of1
> 个 b = X
> 17
> "language
> FASTEXPR'
> 18
> IVis0a1i2ation"
> false,
> 19
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE
> imb5_
> SCOIC!
> 24
> description
> Iaea:
> Take
> The
> negative
> Inverse
> O1 The
> inbalance
> SCOIE
> -0
> CIeaTe
> ConTLaLian Signal
> That
> elphasizes
> anC
> fLips
> The
> OIIgInal Ielatzonsh-p. InRatzonale
> for
> 0a-a
> USeC
> The
> inbalance
> SCOIE
> (imb5_
> SCOIE )
> Iikely
> IIea5ULe5
> OIOEI
> fIOW
> OI
> Iiquidity
> aSyIIeTTy;
> Its Inverse highlishts periods
> O1 balance,
> and
> The
> negative sign
> fuITher
> inverts
> The signal. InRationale
> fJI
> OperatoIs  used:
> The
> inVerBe
> (1/x)
> TTansfoIms high
> imbalance
> Into
> Ioy
> Values
> anC
> CHe
> negative sign
> (-〉 Iips
> The
> OUTpU
> PTLOIICIZe
> Conci-inns Where
> The OLiginal
> SCOIe
> Is negative (e.8
> sellIng pressuTe)
> bUT
> OWI
> appears
> positive signals
> 25
> ODeratozCount
> 25
> 27
> UateCzeated "
> 2025
> 09-09T01:43:59
> 04:00
> 28
> "dateSubmitted "
> 2025-09-09102:20:35-04:00
> "datelodified
> 2025-09-13109:42:37
> 04:00
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> alpha C


只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符

2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 08/14/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(2
> rsk72_atopzooO_dsrt
> rank
> mdl26
> FLtV
> rsSII
> 2000_30_
> Power Pool Alpha
> Pyramid theme: CHNIDIIRISK X1.4
> Simulation Settings
> Pyramid theme: CHNIDIIMODEL X1.6
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaNHar
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.59
> 48.989
> 0.96
> 17.739
> 14.389
> 7.249600
> Equity
> CHN
> TOPZOOOU
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,00
> 50.9796
> 2.14
> 25.8395
> 3.459
> 10.14930
> 376
> 311
> Clone Alpha
> 2014
> 3.19
> 50.37%6
> 2.39
> 28.3395
> 4.5996
> 11.259530
> 449
> 375
> 2015
> .99
> 43.99%
> 1.76
> 32.2995
> 14.38%
> 15.5935o
> 726
> 502
> 2016
> 2.15
> 46.26%
> 22.0595
> 5.0596
> 9.5390
> 675
> 556
> Chart
> Pnl
> 2017
> 0.46
> 46.93%
> 0.14
> 43895
> 8.6795
> 879530
> 595
> 501
> 2018
> 1.31
> 48.3796
> 0.64
> 11.6395
> 4.6796
> 83900
> 554
> 455
> 2019
> 2.07
> 50.56%
> 1.22
> 17.6995
> 4.11%
> 9850
> 524
> 420
> 2020
> 0.17
> 50.68%
> 0.03
> -1.9695
> 10.9096
> 0.77930
> 542
> 427
> 1ON
> 2021
> 51.20%
> 0.38
> 11.1295
> 9.73%
> 4.34900
> 543
> 425
> 2022
> 50.5696
> 1.12
> 20.1999
> 5.7390
> 7.979530
> 552
> 447
> 5,00OK
> 2023
> 10.25
> 50.3896
> 10.51
> 52.9395
> 2496
> 21.019500
> 562
> 484
> Risk neutralized
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> 1.17
> 48.989
> 0.39
> 5.4296
> 18.579
> 2.219600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.52
> 42.179
> 0.97
> 17.049
> 14.409
> 8.089600
> IS Testing Status
> Period
> IS
> 05
> [
> Correlation
> 8 PASS
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 6;01
> Turnover of 48.989 is above cutoff of 1%
> PM
> Turnover of 48.98% is below cutoff of 70%
> Weight is well distributed over instruments。
> Returns Of 17.73% is above cutoff of 8%.
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 6;01
> Sub-universe Sharpe of 1.55 is above Cutoff of 1.13.
> PM
> Robust universe Sharpe of 1.30 is above CUtoff of 0.64 (40% of Alphal
> 0.8918
> -0.2468
> Robust universe returns of 9.139 is above cutoff of 7.09% (40% of Alphal.
> These pyramid themes match with the following multipliers: CHN/DI/RISK-
> 1.4; CHNIDIIMODEL
> 1.6.The final
> pyramid theme multiplier is 1.4. Effective pyramid count for Genius is 2。
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 6;01
> PM
> 5WARNING
> 0.8234
> -0.6297
> Sharpe of 1.59is below CUtOff of 2.07.
> chng


我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi. worldquantbrain comlalphas/SdnGl4z
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 17.925
> 2.3 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三 Q6 &
> 15
> IaXTTaCE
> OFF
> operatorcount
> 酏*
> 1Of1
> 个 b = X
> 17
> "language
> IFASTEXPR"
> 18
> IVis0a1i2ation"
> false
> 19
> startDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> TegUIaT"
> 23
> COCE
> raIk (2
> ISk72_a20p2000_
> OSIT)
> raIk (3
> 10125_
> Chng_IICV_T_
> 工5511
> 2000_
> 30)
> 24
> "description"
> Iaea:
> Dual-Iank PIOCUCT
> Signal
> Combining
> SHOIT
> MnTerest
> anC
> RSS
> Iquidity
> Changes
> 1nRaTi3na12
> for 0a-a
> USeC:
> 1 -
> ISK72
> aTOp2OOO_OSIT:
> RUSSeII
> 2000
> SHOIT
> MnTerest
> percentile
> {几-
> Ic126_chng_
> IITV_T_ISSII
> 2000_
> 30:
> 30 -
> IelatIve Izquzdity
> Change
> SCOIC
> InlnRaionale
> fJI
> OpeIaTOIS
> USee
> 1-
> EXpOnenTiaI
> TransforIs
> CIeaTe
> COIVCX
> Ianking:
> 3a5e-2:
> SHOIT
> Interest
> aMplification
> 3a5e-3
> Htouidity
> change sensitivity
> 1 -
> MulTiplicaive
> Combinazion:
> High when
> boTh
> signals
> agTeE
> Near- ZeIn
> when
> eiTher
> neUTIaI
> {- Negative
> SIgn
> CargeTs:
> High
> SHOIT
> MnTerest
> CeTeriorating
> liquidity
> 1"5hoI
> 50UeeZe
> TIap
> ioentification
> OpezatozCount
> 25
> 27
> "datecreated "
> 2025
> 08-14T05:27:35-04:00
> 75
> rateSwhmitterl"
> 2025-08-15T01:04:25-04:Q0
> alpha C
> day


重复算 operatorCount 操作符了 .

没有  **字段使用数量信息** ，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .

[图片 (图片已丢失)]

**重点** ：巧妙的节省重复操作符 ！！！

从以上几个alpha操作符测试，让我们知道了

i ) +、-、*、/ 和 ^ 都是算入操作符计数的；

ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；

iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha

3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/12/2025 EDT
> anonymoUs
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> brk
> VeC
> Sum(brkl_start_stock_price);
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIBROKER X1.5
> alpha
> ts covariance
> bpk,
> 股票起始价格汇总
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> bpk
> 11同一序列的自相关讦算
> 1.05
> 13.439
> 0.86
> 9.059
> 10.689
> 13.479600
> 24
> 24周期(约1个月)滚动窗0
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0,80
> 14.3096
> 5.2995
> 5.0195
> 40930
> 1157
> 1571
> Instrument Tpe
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> 2014
> .85
> 12.39%
> .90
> 13.2495
> 3.239
> 21.369600
> 1424
> 1722
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> On
> OfT
> 2015
> +28
> 12.59%6
> 1.28
> 12.6295
> 7.6596
> 20.05930
> 1537
> 1751
> 2016
> 1.36
> 13.59%
> 1.57
> 18.2595
> 9.249
> 26.67930
> 1477
> 1690
> 2017
> 0.63
> 11.4796
> 0.32
> -3.20%
> 6.959
> -5.5893o
> 1746
> 1497
> Clone Alpha
> 2018
> 0.72
> 12.4696
> 0.52
> 5.469
> 8.5096
> 10.379530
> 1980
> 1765
> 2019
> 13.25%
> 1.71
> 13.5695
> 5.18%
> 20.47930
> 1757
> 1611
> 2020
> 0.47
> 15.54%
> 0.25
> 2.4495
> 7.5096
> 68930
> 1818
> 1731
> Chart
> Pnl
> 2021
> 14.52%
> 1.17
> 10.8195
> 4.0096
> 14.79930
> 2194
> 2300
> 2022
> 1.17
> 13.7096
> 0.94
> 8.759
> 6.35%
> 12.779530
> 1980
> 2197
> 2023
> 0.48
> 20.3796
> 0.17
> 26Ob
> 8296
> 2.5593o
> 1640
> 1992
> 7,50OK
> SOOOK
> Correlation
> 2,50OK
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,8;43
> Du
> 0.2112
> -0.0733
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
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 8;43
> PM
> 0.4247
> -0.0733
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 8;44
> PM
> 0.3960
> -0.3483


我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain comlalphaslobd5qOE
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 2.545
> 2.41 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> nanHandling"
> OFF
> operatorcount
> 劭
> ? Of1
> 个 b = X
> 16
> IaXTTaCE
> ON
> 17
> "language
> FASTEXPR
> 18
> IVis0ali2ation
> false,
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE"
> Ibrk
> VeC
> SUII ( bIkz_
> STAIT_
> sTOCk_priCe ) ; Irlnalpha
> C5_
> Covariance (IIin
> DIK,
> L 股票起始价格汇总 Irln
> bIk ,
> LL 同-序列的
> 自相关计算 {210
> 24
> J24周期〈约1个月)滚动窗OIrln) ; '
> 24
> "JesCZIptiOn"
> Iaea:
> COIpUTE
> the negatlve IoIIIng
> COVariance
> Of aggTegated
> starting stock prices with itself
> Iea5UIE
> 5e11-similarity
> anO
> invert
> The
> Ielationship
> InRationale
> fJI
> USeO:
> The aggIe
> starting
> STOCK priCe
> (VeC_
> SUII
> (brki_
> STaIT
> sTOCk_price)
> IeTIeCTS
> baseline
> Valuation
> levels
> 35
> boTh
> IpUTS
> COVariance
> CapTUIeS
> i5
> OIII
> Volatility
> and pattern
> consistency
> InRaTionale
> for OperatoIs
> USeC:
> The
> 24-period
> COVariance
> (TS
> COVariance)
> SeIies Iizh
> iself simplifies
> VaTZance
> measUring
> HOWI Uispersed
> The
> Values
> aIe
> aIOUnC
> Their
> IIean
> DVEI
> ShOIt
> term Window.
> The
> negative
> sign (-)
> TIVeITS
> 375,
> 50
> higher
> Variance (inszability)
> IeSUITs
> 11
> IOIeI
> 518na1 ,
> penalizing
> VoIatility
> 25
> OpezatozCount
> 25
> alpha C
> Jaza
> gazed
> Using


事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/01/2025 EDT
> jiao?
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> Vector
> neut
> VeC
> SUN(rSKGG
> offer),
> VeC
> SUm(rsk6o
> Offer)))
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> Simulation Settings
> 1.33
> 10.339
> 1.05
> 7.819
> 16.029
> 15.139600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Equity
> USA
> ILLIQUID_MINVOLIM
> Fast Expression
> 0.08
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.009
> 0.00
> 0.0096
> 00%
> 0093o
> 2014
> 1.30
> 7.1995
> 0.77
> 4.4296
> 1.6296
> 12.36950
> 936
> 1552
> 2015
> -0.29
> 7.5095
> -0.21
> 2.28%
> 8390
> 079330
> 716
> 1825
> Clone Alpha
> 2016
> 1.03
> 7.3295
> 5.4796
> 0996
> 14.93930
> 539
> 1878
> 2017
> 0.77
> 8.3595
> 3.36%
> 4.839
> 0593o
> 555
> 832
> Chart
> Pnl
> 2018
> 1.07
> 13.9099
> 5.29%
> 2.5795
> 7.62930
> 577
> 888
> 2019
> 0.95
> 13.0395
> 5.5596
> 4.98%
> 8.5390
> 512
> 1905
> 2020
> 1.25
> 11.1495
> 1.16
> 10.6596
> 5.11%
> 19.139500
> 464
> 1922
> 2021
> 0.91
> 10.1895
> 0.b
> 79%
> 12.53%
> 13.34930
> 2248
> 2022
> 5.02
> 14.389
> 7.52
> 32.31%
> 2.2796
> 44.9493o
> 1070
> 1821
> 40OOK
> 2023
> -1.55
> 10.6890
> -1.48
> -11.40%
> 2.35%
> -21.32930
> 752
> 1893
> 20OOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;55
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
> Du
> 0.3766
> -0.1774
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;55
> PM
> 0.3713
> -0.1928
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;55
> 00
> IS Testing Status
> Period
> OS
> PM
> 0.6809
> -0.5425


这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =

1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .

[图片 (图片已丢失)]

2. 点塔！

```
点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题
```

当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节： [交一个怎样的alpha能提升你的六维数据之定性定量分析 .]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！

关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：

i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)

[图片 (图片已丢失)]

比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 . 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(anl3g
> rOXLCXSpeq
> anl3g_xIcxspemtp)
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> RetUrns
> DrawOOwn
> Margin
> Simulation Settings
> 0.37
> 3.549
> 0.14
> 1.869
> 13.18%
> 10.539600
> Instrument Tpe
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.71
> 3.769
> 1.30
> -7.22%
> 11.439
> -38.389530
> 775
> 1332
> 2014
> 1.18
> 3.1795
> 0.75
> 5.0096
> 3.51%
> 31.53950
> 1058
> 1558
> 2015
> 0.37
> 3.4295
> 0.15
> 2.1796
> 7.36%
> -12.67900
> 1156
> 1557
> Clone Alpha
> 2016
> 1.83
> 3.8795
> 1.84
> 12.6796
> 3.21%
> 65.529530
> 1093
> 1627
> 2017
> 0.58
> 3.3295
> 0.32
> 2.6996
> 5.33%
> 16.2390
> 1172
> 1779
> Chart
> Pnl
> 2018
> 1.81
> 3.43995
> 1.42
> 7.42%
> 3.40%
> 43.25930
> 1135
> 1792
> 2019
> -U.61
> 3.3995
> 0.33
> 3.029
> 4.92%
> -17.9390
> 004
> 1825
> 2020
> 3.5395
> 0.10
> 5696
> 5.6796
> 8.84930
> 998
> 1752
> 2021
> 1.38
> 3.8595
> 5.5896
> 4.20%
> 28.97930
> 1855
> OOOK
> Mlwto
> 2022
> 0.32
> 3,6695
> 0.13
> 9996
> 859
> 10.8593o
> 1072
> 830
> 2023
> -3.70
> 3,0095
> 2.01
> -14.5890
> 0090
> 97.97930
> 970
> 1792
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Margin
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
> 0.27
> 2.2296
> 0.09
> 1.4096
> 14.639
> 12.579600
> Pnl
> Investability Constrained Pnl
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;36
> PM
> 0.2624
> -0.0448
> IS Testing Status
> Period
> OS
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;37
> PM
> 0.8554
> -0.6340
> 5PASS


通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 07/30/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank
> star
> Val
> industry_rank
> anl39
> rOXLCXSpeq
> anl39_xlcxspemtp
> Power Pool Alpha
> Pyramid theme: EURIDIIMODEL X1.4
> Simulation Settings
> Pyramid theme: EURIDIIANALYST X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.45
> 7.5596
> 1.91
> 7.629
> 4.2396
> 20.189600
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> On
> On
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.70
> 6.7096
> 1.04
> 46895
> 1.289
> 13.98900
> 778
> 1329
> Clone Alpha
> 2014
> 3.25
> 7.59%6
> 2.69
> 8.5495
> 1.149
> 22.5035o
> 1070
> 1525
> 2015
> 1.27
> 7.84%
> 0.72
> 2.0595
> 2.839
> 10.359500
> 1113
> 1611
> 2016
> 4,09
> 8.03%
> 2.34
> 12.0895
> .20%
> 35.07930
> 1025
> 695
> Chart
> Pnl
> 2017
> 2.61
> 7.3396
> 1.75
> 5.6295
> #1090
> 15.3390
> 1120
> 831
> 2018
> 3,05
> 7.7096
> 2.30
> 7.10%
> 2.0590
> 18.43900
> 1166
> 1750
> 2019
> 1.27
> 7.56%
> 62
> 3.0195
> 1.70%
> 7.95930
> 1183
> 1625
> 2020
> 2.34
> 8.01%
> 1.94
> 8.6095
> 1.72%
> 21.469530
> 1121
> 1621
> 5OOOK
> 2021
> 2.71
> 86%
> 2.35
> 9.4095
> 3.52%
> 27.40950
> 1122
> 1820
> 2022
> 2.45
> 7.81%6
> 2.27
> 10.75%
> 4.2390
> 27.51930
> 1163
> 1739
> 2,50OK
> 2023
> 3,80
> 7.5596
> 3.63
> 11.8095
> 0.489
> 31.269500
> 1093
> 1672
> Investability constrained
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.88
> 3.599
> 1.30
> 5.9796
> 3.9796
> 33.269600
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025,7.05
> PM
> 00
> IS Testing Status
> Period
> 05
> 0.5189
> -0.0937
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> 8 PASS
> PM
> 0.5189
> -0.1529
> Sharpe of 2.45 is above CUtOff of 1.58.
> Fitness Of 1.91 is above cutoffof1.
> Turnover of 7.5596 is above CUtoff of
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> PM
> Turnover of 7.55% is below cutoff of 70%.
> Weight is well distributed over instruments。
> 0.8288
> -0.4965
> Sub-universe Sharpe of 1.27 is above cutoff of 1.27.
> IS Iadder Sharpe Of 2.49 is above cutoff of 2.02 for Iadderyear 2: 1/20/2023.1/21/2021


ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> OS
> ts_target_
> tvr_decay (imbs_
> SCOre
> Iambda_min-o,
> Iambda
> maX=l, target
> tVr=0.1
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> Simulation Settings
> 2.86
> 7.7796
> 1.98
> 5.979
> 2.319
> 15.379600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.32
> 7.96%
> 2.54
> 7.3295
> 009
> 18.40950
> 1363
> 1355
> 2014
> 5.73
> 7.0796
> 5.12
> 9.999
> 0.739
> 28.259530
> 1569
> 1577
> 2015
> 4.83
> 7.5196
> 264
> 11.5495
> 1.289
> 30.7390
> 1645
> 653
> Clone Alpha 
> 2016
> 2.76
> 7.3796
> .82
> 5.42%
> .6890
> 14.71930
> 1574
> 593
> 2017
> 2.23
> 7.51%
> 3.00
> 5.2995
> 639
> 16.52930
> 1610
> 533
> Chart
> Pnl
> 2018
> 3.49
> 7.81%
> 2.54
> 6495
> .239
> 6.93930
> 1875
> 1871
> 2019
> 2.96
> 7.5596
> 2.04
> 5.9195
> 1.129
> 15.45930
> 645
> 1723
> 2020
> 8.30%6
> 22795
> 1.729
> 5.48930
> 1736
> 1813
> 2021
> .05
> 299
> 2.43%
> 2.31%
> 5.86930
> 2203
> 2291
> 40OOK
> 2022
> 7.97%6
> 0.22
> 1.5195
> .839
> 3.79950
> 2057
> 2121
> 2023
> 11.09%
> 5.57
> 8.2395
> 08%
> 14.85930
> 1783
> 1829
> ZOOOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;33
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
> PM
> 0.3352
> -0.0929
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> Du
> 0.5597
> -0.1764
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> IS Testing Status
> Period
> 0S
> Du
> 0.9227
> -0.5410
> Year


比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .


> [!NOTE] [图片 OCR 识别内容]
> 说到这里,
> 我想说一下关于提交 alpha 关于 Prod Correlation ,
> Power Pool
> Correlation 和 Self Correlation,
> 也许在绿灯亮起提交 alpha 显示出的错误或许不
> 那么明确. (个人看法,如有问题还望大佬们不忘吝啬,
> 可评论区说明我好做出调
> 整)但大致是这样的 .
> 举个例子:有一个国王喜欢吃各种各样式的苹果
> 大家都会送苹果给国王
> 吃,
> 当然会获得相应的报酬,吃之前需要将苹果放进池子进行清洗,
> 有两个大小
> 的池子。如果你送来的苹果好,自然是放在大池子里。和大池子里的苹果比较 ,
> 如果大池子没有类似的苹果,
> 或者如果有类似的苹果,
> 但是你的苹果比这个类似
> 的苹果有更少的瑕疵,那你的苹果将会被收取从而获得报酬;  如果你的苹果不满^
> 足大池子,
> 那就继续按照以上这种方式放小池子,
> 当然这种小池子只是大家人手
> 一个,
> 大池子也是谁想用可以随时搬自己家测试,
> 小池子的作用是什么,如果大
> 池子的苹果被国王吃完了,那就会考虑小池子了,当然人家毕竟是国王,没有那
> 么容易吃完大池子的稀奇苹果.



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 09/11/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> ts_target_
> tvr_decay (imbs_
> SCOre
> mCr63_membership,  Iambda
> min=0
> Iambda
> Iax=l
> targe
> Power Pool Alpha
> Pyramid theme: ASIIDIIIMBALANCE X1.1
> Simulation Settings
> Pyramid theme: ASIIDIIMACRO X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 7.739
> 1.19
> 5.249
> 5.899
> 13.56900
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> 0n
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.03
> 8.02%
> 1.34
> 5.4795
> 2.0596
> 13.63330
> 1377
> 1351
> Clone Alpha 
> 2014
> 2.21
> 7.0596
> 407
> 11.659
> .76%
> 33.089500
> 1573
> 1573
> 2015
> 3.41
> 7.4796
> 293
> 9.20%
> 1.129
> 24.61930
> 670
> 628
> 2016
> +94
> 7.45%6
> 0.47
> 3.16%
> 5.8990
> 48930
> 590
> 1577
> Chart
> Pnl
> 2017
> 2.28
> 7.50%
> 2.8895
> 1.6596
> 12.84930
> 620
> 1623
> 2018
> 2.55
> 7.74%
> .84
> 5.5395
> 1.2996
> 16.879500
> 899
> 1827
> 2019
> .83
> 7.5496
> 1.14
> 4.8795
> .9890
> 12.91930
> 1705
> 653
> 2020
> 0.02
> 8.3296
> 0.00
> 0.059
> 2.259
> 0.1593o
> 800
> 1729
> 2021
> 8.18%6
> 1.21
> 5.159
> .6390
> 12.5893o
> 2305
> 2190
> 2022
> 7.82%
> 0.07
> 0.8795
> 2.5696
> 2.239500
> 2113
> 2055
> ZOOOK
> 2023
> 3.80
> 10.50%
> 3.02
> 7.9295
> 0.1996
> 15.08930
> 864
> 1757
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;43
> PM
> 0.3474
> -0.0437
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.3645
> -0.0892
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.6217
> -0.4420
> PASS
> Vear


事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .

[图片 (图片已丢失)]

3. 好而优的 alpha

何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .

一点：好，我理解在:

1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；

2) fitness ≥ 1  全方面稳定还是非常不错；

3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；

4) returns ≥ 10%  收益还是要好点能赚钱吧；

5) drawdown 回撤越小越好吧，大了心理抗压不行；

6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；

7) 十年数据中做多做空不能太少吧，权重太高危险危险！

8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .

满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/08/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> 1
> OS Summary
> Period
> I5
> 05
> peVerse(r
> ib5
> SCOre
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDOIIMBALANCE
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> Simulation Settings
> 0172112023 CT
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Close
> Close Ratio
> Self-Correlation
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone Alpha
> 2013
> 3.9
> 23.8899
> 4.13
> 26.189
> 2.5995
> 21.929600
> 986
> 405
> 2014
> 3.52
> 22.6895
> 3.36
> 20.65%
> 2.9096
> 18.22930
> 1070
> 431
> 2015
> 3.32
> 22.8295
> 3.46
> 24.43%
> 3.03%
> 21.41950
> 1130
> 459
> Chart
> Pnl
> 2016
> 2.53
> 21.1195
> 2.65
> 21.4796
> 3.4796
> 20.349530
> 1138
> 455
> 2017
> 2.77
> 20.7795
> 2.47
> 16.5496
> 3.40%
> 15.92930
> 1125
> 470
> 2018
> 1.88
> 19.5696
> 1.67
> 15.3796
> 7.27%6
> 15.71930
> 1010
> 418
> 2019
> 2.77
> 19.1395
> 3.03
> 22.829
> 3.18%
> 23.8890
> 998
> 423
> 1ON
> 2020
> 0.71
> 19.4395
> 0.39
> 5.9596
> 5.659
> 2930
> 908
> 392
> 2021
> 1.73
> 19.20%
> 10.789
> 5.089
> 11.22930
> 972
> 416
> 5OOOK
> 2022
> 18.4390
> 1.42
> 14.789
> 4.5795
> 16.0493o
> 050
> 439
> 2023
> 10.22
> 31.6599
> -14.39
> 62.7790
> 3.5796
> 39.67930
> 945
> 393
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
> Pre
> Sharpe
> Pre


二点：优，我理解在:

1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；

2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；

3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；

使用


> [!NOTE] [图片 OCR 识别内容]
> 1
> 1.
> 事件距离基础信号:  距离越大。事件影响越小
> eVent
> signal
> VeC
> SUI
> nWs7g_event_detection_distance_358-
> 1
> 距离平方增骚:  放大极端距离信号的非线性影响
> brk
> VeC
> sum(brkl_start_stock_price);
> distance_squared
> event_signal
> 2;
> alpha
> ts covariance(
> brk,
> 股票起始价格汇总
> 1
> 词频倒数因子:  词数越少。信息浓度越高(1/词数)
> brk,
> 11  同一序列的自相关计算
> Word
> density
> 二 1
> VeC
> SUII
> nWS7g_word_count_391 )
> 24
> 24周期(约1个月)滚动窗口
> 10
> 1
> 复合事件驱动因子:  距离信号
> 非线性增骚
> 信息浓度
> 11
> alpha
> (event_signal
> distance_squared
> Word_density)



> [!NOTE] [图片 OCR 识别内容]
> 11 Core Logic:
> Reverse standardized composite factor
> reverse
> operation when large trader behavior diverges
> 1
> Synthetic
> Base
> Factor: Market
> pattern
> trader Value differential
> base factor
> mdl175 OGam
> power(Vec
> sum(pvz7_value_diff_large_trader), 2);
> /12. standardization: Convert to
> Z-score to eliminate scale effects
> Zscore_factor
> Zscore(base_factor) =
> 1
> Signal Reversal: Negative sign indicates
> Contrarian
> selection, seeking
> undervalued
> opportunities
> alpha
> ZSCOre
> factor;
> large



> [!NOTE] [图片 OCR 识别内容]
> Description
> 507
> 100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template_
> Idea: Identify the time index ofthe maximum imbalance score over a 2O-day Window, then invert the result:
> Rationale for data used: The imbalance score (imb5_score) likely measures order flow or liquidity asymmetry; its maximum pinpoints the
> most extreme positive imbalance event。
> Rationale for operators Used: The 20-dayarg max (ts_arg_max)returns the lookback period (0-19) where the series peaked_and the


不建议使用


> [!NOTE] [图片 OCR 识别内容]
> 1 |
> ts_covariance(vec
> SUm(brkl_start_stock_price) ,
> VeC
> sum(brkI_start_stock_price), 24)



> [!NOTE] [图片 OCR 识别内容]
> brk
> VeC
> sum(brkl_start_stock_price)
> alpha
> ts covariance
> brk,
> 股票起始价格汇总
> bk,
> 11同一序列的自相关计算
> 24
> 1124周期(约1个月)滚动窗口
> );
> alpha


[图片 (图片已丢失)]

**三、alpha模板 ！**

看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .


> [!NOTE] [图片 OCR 识别内容]
> N-1
> Ha
> 1,3N,8.七
> lim
> fa()-Cfa(a)
> 二
> Iim
> fa(a)
> n-〉+O
> n〉+O
> 2二1
> 2二1
> C=N
> 10-P


换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！

field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .

其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> 2,000
> UUJ
> OIlU
> 〈ee
> 3" A0。
> 02
> Displayed Period
> 02/14/2025
> 09/12/2025
> 149346
>  Mar
>  Mar
> Mar
> Mar
> Mar
> 30。
> 31。
> 24。


从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .

[图片 (图片已丢失)]

使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .

造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .

[图片 (图片已丢失)]

下节预告:  [Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

2025年9月14日

**顾问 WX64154 (Rank 32) 的解答与建议**:
感谢大佬分享。给我深深上了一课，期待下节。

想知道大佬怎么把combine刷的那么高


---

### 技术对话片段 56 (原帖: 看到好多同期已经拿到顾问协议了，想问问有多少人没有，又是什么原因？)
- **原帖链接**: [Commented] 看到好多同期已经拿到顾问协议了想问问有多少人没有又是什么原因.md
- **时间**: 1年前

**提问/主帖背景 (FF30691)**:
我是参加的2025第一期量化，从基础课一直跟到了顾问课程，具体流程如下：

2025.1.10左右开始提交alpha

1.20日收到金牌邮件

1.22日填写问卷

2.12日初审通过

目前已提交32个alpha，但还没有等到顾问协议，大家的流程又是怎么样的，愿意分享的可以在评论区留言。有同期已经拿到顾问协议的老哥也希望分享一下经验。

**顾问 WX64154 (Rank 32) 的解答与建议**:
可我都交到67个了 还没收到顾问协议


---

### 技术对话片段 57 (原帖: 看到好多同期已经拿到顾问协议了，想问问有多少人没有，又是什么原因？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 看到好多同期已经拿到顾问协议了想问问有多少人没有又是什么原因_31041301082007.md
- **时间**: 1年前

**提问/主帖背景 (FF30691)**:
我是参加的2025第一期量化，从基础课一直跟到了顾问课程，具体流程如下：

2025.1.10左右开始提交alpha

1.20日收到金牌邮件

1.22日填写问卷

2.12日初审通过

目前已提交32个alpha，但还没有等到顾问协议，大家的流程又是怎么样的，愿意分享的可以在评论区留言。有同期已经拿到顾问协议的老哥也希望分享一下经验。

**顾问 WX64154 (Rank 32) 的解答与建议**:
可我都交到67个了 还没收到顾问协议


---

### 技术对话片段 58 (原帖: 高VF的经验和VF崩盘的反思（0.99>0.93>0.99>0.98>0.97>0.7）经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 高VF的经验和VF崩盘的反思09909309909809707经验分享_41021984423063.md
- **时间**: 16天前

**提问/主帖背景 (FF56620)**:
如图，从12月开始，到4月，几个月的VF分别为0.99，0.93，0.99，0.98，0.97，而在五月更新，一下子崩盘来到了0.7，总结一下自己一些高VF的经验和崩盘的反思


> [!NOTE] [图片 OCR 识别内容]
> Value Factor
> 1.04
> 1.00
> 0.90
> 0.80
> 0.70
> 0.65
> 202508
> 202509
> 202510
> 202511
> 202512
> 202601
> 202509
> 202510
> 202511
> 202512
> 202601
> 202602
> 202510
> 202511
> 202512
> 202601
> 202602
> 202603


前几个月，我个人 VF 的积累基本都来自 Regular Alpha。我几乎不交 PPA，除非某个塔实在点不上。另外，我提交的大部分 Alpha 都是单数据集（single dataset），即使是 PV 分组也很少使用，当然，七个豁免的分组字段除外。

再说一下 Alpha 的提交数量。我基本采用 1+1 的提交方式。对我来说，追求更高的 RA 带来的一个问题，就是出货量会比较少，自然也没法像一些大佬那样每天都能稳定交满。不过我想表达的重点是，量少也能高VF。

关于VF的崩盘，回头看，我认为，后面的崩盘更多是因为自己过于追求高 Base。之前听说了 553 这个概念后，我尝试了一段时间，也确实吃到了一些甜头。从去年 12 月左右开始，我大量提交 553。OS 更新之后，我又提交了很多“厂”字形的 553。这些操作后来证明给自己埋下了不小的隐患。

到了 5 月更新时，VF 和 Combine 都出现了明显下滑。VF 从之前的水平掉到了 0.7，Combine 也降到了 1.84。从这次季度奖的结果来看，整体其实非常不划算。仅仅因为两次 VF 的差距（0.99 和 0.7），季度奖就相差了大约 1800 美元。另外，调 553 本身也非常耗费时间。把这两部分成本加在一起，投入产出比其实很低。

这次经历也给了我一个比较深刻的教训：无论什么时候，都要把质量放在第一位。

简单分享一下，希望对大家有所帮助。

**顾问 WX64154 (Rank 32) 的解答与建议**:
同交553 目前vf坐牢中

0.99-0.99-0.98-0.88-0.6

还是交三五吧

============================553还是少交==============================================

====================================================================================


---
