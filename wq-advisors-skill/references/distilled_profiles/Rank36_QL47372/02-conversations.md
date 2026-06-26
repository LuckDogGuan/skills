# 顾问 QL47372 (Rank 36) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 QL47372 (Rank 36) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: Getting started with India Alphas置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Getting started with India Alphas置顶的_36059391387415.md
- **时间**: 2个月前

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

**顾问 QL47372 (Rank 36) 的解答与建议**:
Thanks for sharing. I've been focusing on alpha development for the India region recently, and the biggest hurdle is still the robust universe Sharpe test.


---

### 技术对话片段 2 (原帖: [BRAIN TIPS] How can you improve Alpha coverage with ts_backfill and group_backfill?置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [BRAIN TIPS] How can you improve Alpha coverage with ts_backfill and group_backfill置顶的_40576075554327.md
- **时间**: 22天前

**提问/主帖背景 (AG20578)**:
**Why is handling Alpha coverage important?**

When your Alpha has missing values, it covers fewer instruments in the universe. This can lead to:

- More concentrated positions – higher risk
- Higher chance of overfitting to a small subset of instruments
- Potentially worse after-cost performance

Coverage is the fraction of instruments in the universe that have a defined value. Improving coverage helps Alpha assign weights to more instruments. This improves diversification and can make performance more reliable.

Two operators for you to consider:

- ts_backfill – fills gaps using the instrument's own past values
- group_backfill – fills gaps using peer instruments in the same group

**How do you check if an Alpha has coverage issue?**

You can assess coverage of data field before simulation. Open the  [Data]([链接已屏蔽])  tab on the Platform and check the data field Coverage in the table.


> [!NOTE] [图片 OCR 识别内容]
> 鬯"
> @Simulale
> QNphas
> 0learn
> @ Data
> Lal5
> Genius
> Competiors (0
> Reglon
> Delay
> Universe
> Data
> Datasets
> Oil Price Resilience Scores
> EUR
> TOP2SOO
> Fields
> Description
> Search
> Theme
> Coverage
> Dae coverage
> uphas
> 4「9
> dpccnntIOT
> 100
> Clear
> PTun
> Fld
> cThon
> TM
> Cotg
> Qua
> Hphs
> CoTr[
> NulbtLet
> U
> Nueel CL WILJUCIOIIeCUrIYIn TemonulCUTenC' UTIU
> UITI'
> IIb5 Joie
> SHIELDOIL COOIeYoCIO-TIIUJIR
> WuUII
> rocncelnuponollshock rce
> Puge sle
> oUto?
> d』
> TPe
> TU


Another sign is a low Long Count and Short Count in the Summary table.


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Average
> Single Data Set Alpha
> Simple Alphas
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.85
> 24.339
> 1.12
> 8.9796
> 8.019
> 7.379600
> Year
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 5.77
> 26.749
> 4.80
> 18.4796
> 1.359
> 13.820o
> 580
> 587
> 2013
> 4.35
> 25.07%6
> 2.85
> 10.7096
> 1.039
> 8.539o
> 599
> 597
> 2014
> 4.75
> 26.76%
> 3.49
> 14.48%6
> 2.58%
> 10.829o0o
> 599
> 595
> 2015
> 2.70
> 27.55%
> .60
> 9.6996
> 2.6796
> 7.04D0
> 627
> 631
> 2016
> 5.37
> 27.51%6
> 4.37
> 18.1996
> 1.71%
> 13.229o
> 777
> 778
> 2017
> 30
> 24.93%6
> 3.29%6
> 2.30%
> 2.649oo
> 662
> 657
> 2018
> 24.71%
> 0.21
> 2.3596
> 2.8996
> 90o
> 661
> 654
> 2019
> 2.71
> 24.16%6
> .66
> 9.05%
> 3.50%
> 7.499ooo
> 628
> 628
> 2020
> 26.13%
> 1.28
> 17.5696
> 5.139
> 13.44oo
> 652
> 658
> 2021
> 0,84
> 22.42%
> 0,44
> 6,039
> 3,8196
> 5.389o
> 668
> 667
> 2022
> 19.02%6
> 0,01
> 0.39%
> 4.11%
> 0.41
> 865
> 868
> 2023
> -0.16
> 18.33%
> -0.03
> 0.5096
> 3.369
> 0.559o
> 838
> 829
> Oos


Ideally, the average long count plus short count should be close to the size of the universe. If it is less than 50% of the universe, you may need to improve coverage.

To get more information, simulate your Alpha with Visualization turned on so you can access the daily Coverage plot.


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> Chart
> Coverage Of Universe
> 1,300
> 1.100
> 000
> 900
> SUU
> 700
> 2016
> 2018
> 2020
> 2022
> 2024


This helps you:

- Check maximum coverage
- Compare maximum coverage with average coverage
- Judge which operator is more likely to solve the issue.

**What does ts_backfill do?**

For each instrument, ts_backfill fills forward the most recent valid value – up to a specified number of days back.

**Syntax**

ts_backfill(x, lookback)

- x – field or Alpha expression
- lookback – maximum days to look back

**When to use it**

- Data is reported periodically (e.g., quarterly earnings)
- An instrument missed a few days but had a valid value recently

**Lookback parameter:**

- Fundamental (earnings, revenue) and other low-frequency data: 65 or 252 days
- News / sentiment and other high-frequency data: start with 5–21 days

**What does group_backfill do?**

group_backfill fills missing values by averaging peer instruments in the same group (subindustry, industry, or sector) over defined window.

**Syntax**

group_backfill(x, group, lookback, std=4.0)

- x – field or Alpha expression
- group – subindustry, industry, sector, or other group
- lookback – lookback for computing group statistics
- std – outlier threshold (optional, default std=4.0)

**When to use it**

- ts_backfill alone still leaves too many gaps
- Data is structurally sparse across many instruments at the same time

**How can you use ts_backfill and group_backfill?**

Start with ts_backfill on data fields with low coverage (based on information from Data tab). In most cases, it works better when applied to individual fields rather than to the final Alpha expression.

Use it carefully:

- Start with short lookback windows
- Test different lookbacks instead of using one setting everywhere
- Be careful when backfilling with old values: for some types of data, older values may still be a good approximation, while for others they are closer to noise.
- Remember that missing data can also be informative, so do not backfill blindly

After applying ts_backfill, check the daily Coverage plot and the average Long Count and Short Count. If coverage stays the same, the missing values are likely not caused only by short time gaps, so group_backfill can be more helpful.

When using group_backfill:

- It is usually better to apply it to the whole Alpha expression
- If data fields are normalized, it can sometimes be applied to individual fields as well (with smaller groups, such as subindustry)
- It often increases coverage significantly, especially with larger groups such as industry or sector

**Example — data field etz_revenue in USA TOP3000 universe**

- No backfill: ~1,000 instruments
- After ts_backfill(63): ~1,500 instruments
- After adding group_backfill:     ~3,000 instruments

**顾问 QL47372 (Rank 36) 的解答与建议**:
Thanks for sharing. The point that backfill lookback can affect Alpha performance, and that one lookback should not be applied everywhere, is very useful for parameter tuning and optimization.


---

### 技术对话片段 3 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【Community Leader - 因子构造】提升挖矿产率深度分析数据集经验分享.md
- **时间**: 5个月前

**提问/主帖背景 (TL53163)**:
相信不少同学已经注意到，平台后续将对回测数量进行限制。这一变动对还在“暴力跑一二阶”策略的同学来说，无疑是当头一棒。失去了大量回测的支撑，很多人将面临出货效率骤降甚至“断粮”的风险。

那么，在有限的挥镐次数下，如何提高回测命中率、挖出真正有价值的 Alpha？

最关键的一步，是 **先探明矿脉所在** 。换句话说，在使用某个数据集进行回测前，我们必须先 **分析数据集** ，避免在无效表达式上浪费宝贵的回测资源。

我之前分享过一篇帖子，正是基于这一思路，将搜索空间大大压缩，显著提升了回测效率 [../顾问 YH25030 (Rank 31)/[Commented] 理解模板与数据集 我将搜索空间缩小10万倍Alpha Template.md](../顾问 YH25030 (Rank 31)/[Commented] 理解模板与数据集 我将搜索空间缩小10万倍Alpha Template.md)


> [!NOTE] [图片 OCR 识别内容]
> 理解模板与数据集:
> 我将搜索空间缩小10万
> Unfollow
> 倍
> Alpha Template
> TL53163
> 3months ago
> 102
> 发现模板


### 

### 实战案例：ASI fnd17 数据集

以我曾做过的  `ASI fnd17`  为例：

 **1. 选数据集** ：通过华子哥插件查看数据集的整体 OS 表现，若低于平均水平（黄色），则暂时不考虑。 
> [!NOTE] [图片 OCR 识别内容]
> Search
> Categon
> Theme
> Coverage。
> L7IUIe
> |T
> Alphas
> US2c
> Wame  Cescmpwon
> Eundamenbl
> OO
> Dataset
> Felds
> Pyramid Theme
> Coverage
> Value Score
> Users
> Alphas
> Multiplier
> Fundamental PolntInTIme Data
> 045[525341
> 376
> 759
> 2852
> 51981
> marketf3140e
> Company Fundamental Datator Equit
> 0.48(35940)
> 295
> 5O
> 2254
> 41259
> Mant37.7190
> GIobal Fundamental Data
> 0.46(35356)
> market(42 86%6)
> 522
> 2016
> 34729
> DregEundamenalDal
> 046(24799)
> markel(25 98购)
> 370
> 2093
> 28805
> Ogrcpated Fundamental Dat
> 0.46(81161
> T06
> 89
> 819
> 10691


**2. 导出字段** ：将字段导出为 CSV 文件（使用  `df.to_csv()`  方法），方便后续交给 AI 分析。 
> [!NOTE] [图片 OCR 识别内容]
> 3,获取数据字段
> 在官网Data页面中显示的为自己目前有权限的数据集。在数据集Description面板下可以看到dataset_id
> df-Bet_datafields(s, dataset_id
> analyst39
> region= 'AMR
> universe= ' TOP6BO'
> delay-l, data_type= 'MATRIX'
> print(len(df) )
> [1]
> 225
> df.to_csVG 'data_field_CSV /ANR_anl39_data
> CSV
> [19]
> 00s


**3. AI 辅助分析** ：将字段文件和数据集描述一同喂给 AI，让它对字段进行分类。以 fnd17 为例，我得到了几个清晰的分类结果。 
> [!NOTE] [图片 OCR 识别内容]
> ## ASI fndl7
> 数据分类
> ########
> ######1+
> 苹础佶息类 (Basic Information)
> 货币代码
> hb_code
> [ 'financial_reporting_currency
> pricing
> Currency
> code 4
> reporting_currency_code_II'
> pricing
> Currency
> 汇率数据
> ['fnd17
> reptoprcexrate
> fndl7
> reptoprcexrate
> fndl7
> reptoprcexrate
> fndl7
> reptoprcexrate
> fndl7
> reptop
> basic
> Code
> ################  2.
> 盈利能力维度 (Profitability)
> 毛利率指标
> BrOs5_margin
> fndl7_agrosngn
> fndl7_aBrOSIBnZ
> fndl7_qBrosmgn
> fndl7
> OSIBn
> fndi7_Brosngnsyr
> 苔业利润牵
> operating_margin
> [ 'fndl7_tcpngmpoa
> fndl7_aznetmrgn
> fndI7_tcpngmpoq
> fndl7_ttmopmgn
> 净利润率
> net_profit_margin
> 'fndl7_tcpngmpna
> fndl7_tcpngmpnq
> fndl7_ngmpnmtt`
> fndl7_ngmpnmtp
> 税前利润牵
> pretax_margin
> [ 'fndi7_aptmgnpct
> fndl7_aptmgnpctz
> fndI7_tcpngmtpq
> fndI7_ngmtpmtt
> fndI7_rysngmtp
> EBIT /EBITDA相关
> ebit_ebitda
> [ 'fndl7_aebit'
> fndl7_aebitd'
> fndl7_aebitdz'
> fndl7_qebit"
> fndl7_qebitd
> fndl7_ttmebit
> fndl7_ttmebitd'
> profitability
> Bross_margin
> operating_margin
> Iet
> profit_margin
> pretax_margin
> ebit_ebitda
> ################  3
> 坞长性维度
> (Growth)
> 收入垧长
> Fevelue
> Browth
> [ fndl_arevchg
> fndl7_revchngin
> fndl7_revchngyr
> fndl7_revgrpct
> fndl7_Bhcspemtt
> 盈利坩长
> profit_Bronth
> [ 'fndi7_anichg
> fndl7_nichngin
> fndl7_nichngyr
> fndl7_ttmnicng
> EPSS长
> eps
> growth
> [ 'fndi7_ghcspea
> fndl7_epschngin
> fndl7_rygnhcspe ]
> Browth
> pevenue
> Brouth
> profit_Browth
> eps_Browth
> 估值雏度
> (Valuation)
> Code
> ttnr


**4. 生成有意义的模板** ：基于分类结果，让 AI 推荐具有经济学逻辑的模板，而不是盲目让 MCP 推荐。这一步比“暴力枚举”靠谱得多。 
> [!NOTE] [图片 OCR 识别内容]
> data_list = []
> #  1。跨维度价值组合
> #  盈利能力
> 估值维度
> data_list
> list(product(profitability,
> Valuation )
> 增长性 *财务健康度
> data Iist
> list (product(growth,
> financial_health )
> 现金流
> 市场表现
> data Iist
> Iist(product(cash_flow,
> market_performance)
> # 2。质量因子组合
> 盈利能力
> 运莒效率
> 财务健康度
> 股东回报
> #  增长质量
> 风险控制
> #  3。时间序列组台
> 同一措标的不同时间维度
> 年度
> Vs
> 季度 Vs TTM 数据对比
> # 4。相对价值组合
> 同行业不同公司的相同指标
> 公司自身历史数据的纵向比较
 

**5. 构建 Alpha** ：我尝试了前三种建议，即不同维度的字段两两相乘，模板如下：

 `zscore(field1) * zscore(field2)` 

> 注：zscore 可替换为 rank 等可以统一量纲的op，field 可用  `ts_backfill`  和  `winsorize`  预处理。跑完后续可进一步增强信号。

**6. 控制搜索空间** ：由于字段已分组且每组内字段数量有限，最终生成的表达式数量控制在 1~2 万条，跑完后得到了不少可提交的 Alpha，PC 普遍较低。

### 

### 总结：三步走，精准回测

1. **挑数据集** ：优先选择 OS 表现优异的数据集。
2. **让 AI 分析字段并分类** ：快速理解数据结构，识别潜在逻辑。
3. **基于分类构建有意义模板** ：避免无意义组合，提升命中率。

这套方法不仅能有效降低回测数量，避免资源浪费，还能帮助你在有限次数内，挖出真正有价值的 Alpha。

如果你也在为回测受限而头疼，不妨试试这套“AI 辅助 + 分类建模”的思路—— **少挥几次镐，但每次都落在金矿上。**

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬的无私分享，也感谢华子哥的插件，精准导航太强了。限5000回测的当下，缩小搜索空间太有必要了。

**==================================================================================
路漫漫其修远兮，吾将上下而求索。
==================================================================================**


---

### 技术对话片段 4 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader - 因子构造】提升挖矿产率深度分析数据集经验分享_36744363518999.md
- **时间**: 5个月前

**提问/主帖背景 (TL53163)**:
相信不少同学已经注意到，平台后续将对回测数量进行限制。这一变动对还在“暴力跑一二阶”策略的同学来说，无疑是当头一棒。失去了大量回测的支撑，很多人将面临出货效率骤降甚至“断粮”的风险。

那么，在有限的挥镐次数下，如何提高回测命中率、挖出真正有价值的 Alpha？

最关键的一步，是 **先探明矿脉所在** 。换句话说，在使用某个数据集进行回测前，我们必须先 **分析数据集** ，避免在无效表达式上浪费宝贵的回测资源。

我之前分享过一篇帖子，正是基于这一思路，将搜索空间大大压缩，显著提升了回测效率 [[L2] 理解模板与数据集 我将搜索空间缩小10万倍Alpha Template_34478018977687.md]([L2] 理解模板与数据集 我将搜索空间缩小10万倍Alpha Template_34478018977687.md)


> [!NOTE] [图片 OCR 识别内容]
> 理解模板与数据集:
> 我将搜索空间缩小10万
> Unfollow
> 倍
> Alpha Template
> TL53163
> 3months ago
> 102
> 发现模板


### 

### 实战案例：ASI fnd17 数据集

以我曾做过的  `ASI fnd17`  为例：

 **1. 选数据集** ：通过华子哥插件查看数据集的整体 OS 表现，若低于平均水平（黄色），则暂时不考虑。 
> [!NOTE] [图片 OCR 识别内容]
> Search
> Categon
> Theme
> Coverage。
> L7IUIe
> |T
> Alphas
> US2c
> Wame  Cescmpwon
> Eundamenbl
> OO
> Dataset
> Felds
> Pyramid Theme
> Coverage
> Value Score
> Users
> Alphas
> Multiplier
> Fundamental PolntInTIme Data
> 045[525341
> 376
> 759
> 2852
> 51981
> marketf3140e
> Company Fundamental Datator Equit
> 0.48(35940)
> 295
> 5O
> 2254
> 41259
> Mant37.7190
> GIobal Fundamental Data
> 0.46(35356)
> market(42 86%6)
> 522
> 2016
> 34729
> DregEundamenalDal
> 046(24799)
> markel(25 98购)
> 370
> 2093
> 28805
> Ogrcpated Fundamental Dat
> 0.46(81161
> T06
> 89
> 819
> 10691


**2. 导出字段** ：将字段导出为 CSV 文件（使用  `df.to_csv()`  方法），方便后续交给 AI 分析。 
> [!NOTE] [图片 OCR 识别内容]
> 3,获取数据字段
> 在官网Data页面中显示的为自己目前有权限的数据集。在数据集Description面板下可以看到dataset_id
> df-Bet_datafields(s, dataset_id
> analyst39
> region= 'AMR
> universe= ' TOP6BO'
> delay-l, data_type= 'MATRIX'
> print(len(df) )
> [1]
> 225
> df.to_csVG 'data_field_CSV /ANR_anl39_data
> CSV
> [19]
> 00s


**3. AI 辅助分析** ：将字段文件和数据集描述一同喂给 AI，让它对字段进行分类。以 fnd17 为例，我得到了几个清晰的分类结果。 
> [!NOTE] [图片 OCR 识别内容]
> ## ASI fndl7
> 数据分类
> ########
> ######1+
> 苹础佶息类 (Basic Information)
> 货币代码
> hb_code
> [ 'financial_reporting_currency
> pricing
> Currency
> code 4
> reporting_currency_code_II'
> pricing
> Currency
> 汇率数据
> ['fnd17
> reptoprcexrate
> fndl7
> reptoprcexrate
> fndl7
> reptoprcexrate
> fndl7
> reptoprcexrate
> fndl7
> reptop
> basic
> Code
> ################  2.
> 盈利能力维度 (Profitability)
> 毛利率指标
> BrOs5_margin
> fndl7_agrosngn
> fndl7_aBrOSIBnZ
> fndl7_qBrosmgn
> fndl7
> OSIBn
> fndi7_Brosngnsyr
> 苔业利润牵
> operating_margin
> [ 'fndl7_tcpngmpoa
> fndl7_aznetmrgn
> fndI7_tcpngmpoq
> fndl7_ttmopmgn
> 净利润率
> net_profit_margin
> 'fndl7_tcpngmpna
> fndl7_tcpngmpnq
> fndl7_ngmpnmtt`
> fndl7_ngmpnmtp
> 税前利润牵
> pretax_margin
> [ 'fndi7_aptmgnpct
> fndl7_aptmgnpctz
> fndI7_tcpngmtpq
> fndI7_ngmtpmtt
> fndI7_rysngmtp
> EBIT /EBITDA相关
> ebit_ebitda
> [ 'fndl7_aebit'
> fndl7_aebitd'
> fndl7_aebitdz'
> fndl7_qebit"
> fndl7_qebitd
> fndl7_ttmebit
> fndl7_ttmebitd'
> profitability
> Bross_margin
> operating_margin
> Iet
> profit_margin
> pretax_margin
> ebit_ebitda
> ################  3
> 坞长性维度
> (Growth)
> 收入垧长
> Fevelue
> Browth
> [ fndl_arevchg
> fndl7_revchngin
> fndl7_revchngyr
> fndl7_revgrpct
> fndl7_Bhcspemtt
> 盈利坩长
> profit_Bronth
> [ 'fndi7_anichg
> fndl7_nichngin
> fndl7_nichngyr
> fndl7_ttmnicng
> EPSS长
> eps
> growth
> [ 'fndi7_ghcspea
> fndl7_epschngin
> fndl7_rygnhcspe ]
> Browth
> pevenue
> Brouth
> profit_Browth
> eps_Browth
> 估值雏度
> (Valuation)
> Code
> ttnr


**4. 生成有意义的模板** ：基于分类结果，让 AI 推荐具有经济学逻辑的模板，而不是盲目让 MCP 推荐。这一步比“暴力枚举”靠谱得多。 
> [!NOTE] [图片 OCR 识别内容]
> data_list = []
> #  1。跨维度价值组合
> #  盈利能力
> 估值维度
> data_list
> list(product(profitability,
> Valuation )
> 增长性 *财务健康度
> data Iist
> list (product(growth,
> financial_health )
> 现金流
> 市场表现
> data Iist
> Iist(product(cash_flow,
> market_performance)
> # 2。质量因子组合
> 盈利能力
> 运莒效率
> 财务健康度
> 股东回报
> #  增长质量
> 风险控制
> #  3。时间序列组台
> 同一措标的不同时间维度
> 年度
> Vs
> 季度 Vs TTM 数据对比
> # 4。相对价值组合
> 同行业不同公司的相同指标
> 公司自身历史数据的纵向比较
 

**5. 构建 Alpha** ：我尝试了前三种建议，即不同维度的字段两两相乘，模板如下：

 `zscore(field1) * zscore(field2)` 

> 注：zscore 可替换为 rank 等可以统一量纲的op，field 可用  `ts_backfill`  和  `winsorize`  预处理。跑完后续可进一步增强信号。

**6. 控制搜索空间** ：由于字段已分组且每组内字段数量有限，最终生成的表达式数量控制在 1~2 万条，跑完后得到了不少可提交的 Alpha，PC 普遍较低。

### 

### 总结：三步走，精准回测

1. **挑数据集** ：优先选择 OS 表现优异的数据集。
2. **让 AI 分析字段并分类** ：快速理解数据结构，识别潜在逻辑。
3. **基于分类构建有意义模板** ：避免无意义组合，提升命中率。

这套方法不仅能有效降低回测数量，避免资源浪费，还能帮助你在有限次数内，挖出真正有价值的 Alpha。

如果你也在为回测受限而头疼，不妨试试这套“AI 辅助 + 分类建模”的思路—— **少挥几次镐，但每次都落在金矿上。**

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬的无私分享，也感谢华子哥的插件，精准导航太强了。限5000回测的当下，缩小搜索空间太有必要了。

**==================================================================================
路漫漫其修远兮，吾将上下而求索。
==================================================================================**


---

### 技术对话片段 5 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template.md
- **时间**: 4 months ago

**提问/主帖背景 (MY82844)**:
在EUR点塔Sentiment的时候，我们尝试把 [顾问 RM49262 (Rank 30)](/hc/en-us/profiles/32668684211991-顾问 RM49262 (Rank 30)) 的 [强大模版](../顾问 JR23144 (Rank 6)/[Commented] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template.md) 交给AI学习，最后AI推荐了一个新的条件动量模版，使用下来发现可以提炼一个通用模版，适用多种情形。

**因子模版：**

```
ts_mean(if_else(<condition>, returns, 0), <days>)
```

这边condition可以是某种事件，或者正负数/正负力的对比关系。当然，如果condition取1，days取252，我们就回到最简单的动量情形。

**因子逻辑：**

截取某种“有效“时间区间内的股票回报做度量，未来的表现会惯性持续一段时间。

在EUR的Sentiment的情形，我们尝试了下面的组合方式，得到一些低pc的结果：


> [!NOTE] [图片 OCR 识别内容]
> ts_mean (if_else
> Snt21_ZPO5
> mean
> snt2l
> 2neg_mean,
> peturns
> 0)
> Simulation Settings
> Instrument Type
> Region
> Unierse
> LangUaqe
> Decay
> Delay
> Tmuncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Equi
> EUR
> TOPZSOO
> Fast ExPression
> 0.01
> FES- FaC-Ors
> Verify
> Clone Alpha
> Chart
> Pnl
> OOOK
> OOOK
> Jul'13
> Jul1
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
> Jul17
> Jan '18
> Jul'18
> Jan '19
> Jul19
> Jan 20
> Jul'20
> Jan 21
> Jul 21
> Jan'22
> Jul'22
> Jan '23
> Jan _


**后续：**

1. 可以再配合一些group_op()的操作，进一步提升alpha的表现

2. ts_mean和ts_sum可以比较进行，表现有时候会有些差异（包括NaN的不同处理）

3. condition可以多种多样，比如analyst的up/down的力对比，call/put的力对比，有待进一步挖掘

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬分享的模板。最近EUR地区开了新宇宙TOPCS1600，试试这个模板好使不。祝大佬一马当先，马到成功。


---

### 技术对话片段 6 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md
- **时间**: 4个月前

**提问/主帖背景 (MY82844)**:
在EUR点塔Sentiment的时候，我们尝试把 [顾问 RM49262 (Rank 30)](/hc/en-us/profiles/32668684211991-顾问 RM49262 (Rank 30)) 的 [强大模版]([L2] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template_35294898626711.md) 交给AI学习，最后AI推荐了一个新的条件动量模版，使用下来发现可以提炼一个通用模版，适用多种情形。

**因子模版：**

```
ts_mean(if_else(<condition>, returns, 0), <days>)
```

这边condition可以是某种事件，或者正负数/正负力的对比关系。当然，如果condition取1，days取252，我们就回到最简单的动量情形。

**因子逻辑：**

截取某种“有效“时间区间内的股票回报做度量，未来的表现会惯性持续一段时间。

在EUR的Sentiment的情形，我们尝试了下面的组合方式，得到一些低pc的结果：


> [!NOTE] [图片 OCR 识别内容]
> ts_mean (if_else
> Snt21_ZPO5
> mean
> snt2l
> 2neg_mean,
> peturns
> 0)
> Simulation Settings
> Instrument Type
> Region
> Unierse
> LangUaqe
> Decay
> Delay
> Tmuncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Equi
> EUR
> TOPZSOO
> Fast ExPression
> 0.01
> FES- FaC-Ors
> Verify
> Clone Alpha
> Chart
> Pnl
> OOOK
> OOOK
> Jul'13
> Jul1
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
> Jul17
> Jan '18
> Jul'18
> Jan '19
> Jul19
> Jan 20
> Jul'20
> Jan 21
> Jul 21
> Jan'22
> Jul'22
> Jan '23
> Jan _


**后续：**

1. 可以再配合一些group_op()的操作，进一步提升alpha的表现

2. ts_mean和ts_sum可以比较进行，表现有时候会有些差异（包括NaN的不同处理）

3. condition可以多种多样，比如analyst的up/down的力对比，call/put的力对比，有待进一步挖掘

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬分享的模板。最近EUR地区开了新宇宙TOPCS1600，试试这个模板好使不。祝大佬一马当先，马到成功。


---

### 技术对话片段 7 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (SZ83096)**:
分享下我判断因子是否值得提交的一些经验，希望小伙伴们能有所收获。

一个因子值不值得提交，一个是看因子本身的指标，一个是对组合的增益情况。

对我个人而言，后者的重要性一般会大于因子本身的指标（这是在 **因子指标合格的情况下** 的）；

一般很难找到所有指标对performance都是正面明显的。所以你需要在各个指标之间权衡。

## 根据is performance 的正负面影响判断：

### 可提交的情况

1. fitness 是排首位的，一般fitness有明显增益，margin和sharpe的增益不明显，或者稍微一点负面影响，我会选择提交；
2. 95%的情况下，fitness 对最近3-5年 的performance 有明显的负面影响（比如-0.1），不提交;
3. sharpe 和fitness,margin有增益，但是returns稍微有些负面影响，提交；


> [!NOTE] [图片 OCR 识别内容]
> N
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 7.95
> 0,03
> 6.48 %
> -0.02
> 5.50
> 0.01
> 5.98 %
> -0.02
> 0.48 %
> 0,01
> 18.46 %oo -0.01
> 川
> IS Performance After Submission (Equity, EUR, Delay-1 alphas)
> :
> Combined performance data is shown for all Equity, EUR, Delay-1 alphas. Submitting this alpha will not effect the combined performance ofyour other alphas
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2013
> 9.23
> 0.03
> 7.71 %
> -0.03
> 6.33
> 0.00
> 5.87 %
> -0.05
> 0.19 %
> 0.00
> 15.23 %o。
> -0.07
> 2014
> 10.36
> -0.11
> 6.14 %
> 0.02
> 7.52
> -0.14
> 6.59 %
> -0.10
> 0.17 %
> 0.00
> 21.45 %o。
> -0.28
> 2015
> 7.49
> -0.06
> 6.54 %
> -0.01
> 4.93
> -0.09
> 5.42 %
> -0.10
> 0.26 %
> 0.00
> 16.59 %o。
> -0.24
> 2016
> 6.42
> 0.12
> 6.39 %
> 0.02
> 4.22
> 0.11
> 5.40 %
> 0.08
> 0.42 %
> -0.01
> 16.90 %o。
> 0.29
> 2017
> 7.27
> 0.00
> 6.37 %
> 0.02
> 3.98
> 0.00
> 3.75 %
> 0.00
> 0.14 %
> -0.01
> 11.78 %o。
> 0.05
> 2018
> 7.54
> 0.06
> 6.35 %
> 0.02
> 4.60
> 0.02
> 4.66 %
> -0.03
> 0.44 %
> -0.01
> 14.69 %o。
> -0.06
> 2019
> 8.82
> 0.10
> 6.35 %
> 0.02
> 5.69
> 0.07
> 5.20 %
> 0.00
> 0.21 %
> 0.00
> 16.39 %o。
> 0.07
> 2020
> 7.06
> 0.05
> 6.54 %
> 0.02
> 5.19
> 0.05
> 6.75 %
> 0.04
> 0.48 %
> 0.01
> 20.62 %oo
> 0.14
> 2021
> 9.60
> 0.02
> 6.18 %
> -0.02
> 7.56
> 0.00
> 7.76 %
> -0.03
> 0.15 %
> 0.00
> 25.1
> 9oo
> 0.01
> 2022
> 9.06
> 0.05
> 6.35 %
> -0.01
> 7.62
> 0.03
> 8.84 %
> -0.04
> 0.25 %
> 0.01
> 27.87 %oo
> -0.03
> 2023
> -0.93
> 0.14
> 5.07 %
> 0.00
> -0.27
> 0.07
> 1.08 %
> 0.20
> 0.29 %
> 0.00
> -4.26 %oo
> 0.78
> Pnl


### 什么情况下不会提交：

1、margin不符合地区的最低要求，不提交

3、fitness 最近几年明显负面影响，不提交( 超过1个年份<-0.1)

4、sharpe  最近几年明显负面影响 ，不提交( 超过1个年份 <-0.1)

3、多个指标对组合负面明显过大，即使自相关性低，也不提交

很难一一列举对performance 影响的所有情况，是否提交这个因子，根据组合影响，个人情况判断。

### 从因子本身的指标来看：

1、sharpe>=1 ,fitness>=0.6 的前提下

margin 必须达到各地区margin要求的最低标准，我一般要求比最低标准高万分之五（USA，eur）,glb和ASI 地区的margin有时候比较难找到超过15的，在没有选择的情况下，一般ASI 最低14，15；GLB 14，15（少部分情况下会只要求>10【点塔】）

2、pnl线的波动比较小，向上，sharpe线 **不往下走；**

3、ASI 地区 还会观察下jpn的表现，如果jpn明显表现不佳或者或者kor表现明显大于其他地区的表现，不会提交

以上是我个人的一些经验，可能考虑还欠缺一些其他的点， **如果小伙伴有其他好的 判断方法，期待你评论区的分享**

**如果想要保证combine 的稳定，我个人的经验是 绝对不要提交margin不合格、fitness 负面影响过大、最近3年sharpe 线明显下降，pnl趋于厂 的因子（个人经验）**

**最后，给大家看看我现在的combine 情况，希望国区顾问的combine 都能保持稳定增长。**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.38
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 3.17
> Reached Grandmaster
> 0.5
> Combined Power Pool Alpha Performance
> 2.63


**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬分享。在因子指标合格的情况下，更注重is performance的情况，特别是fitness，简单直接，学习了


---

### 技术对话片段 8 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md
- **时间**: 6个月前

**提问/主帖背景 (SZ83096)**:
分享下我判断因子是否值得提交的一些经验，希望小伙伴们能有所收获。

一个因子值不值得提交，一个是看因子本身的指标，一个是对组合的增益情况。

对我个人而言，后者的重要性一般会大于因子本身的指标（这是在 **因子指标合格的情况下** 的）；

一般很难找到所有指标对performance都是正面明显的。所以你需要在各个指标之间权衡。

## 根据is performance 的正负面影响判断：

### 可提交的情况

1. fitness 是排首位的，一般fitness有明显增益，margin和sharpe的增益不明显，或者稍微一点负面影响，我会选择提交；
2. 95%的情况下，fitness 对最近3-5年 的performance 有明显的负面影响（比如-0.1），不提交;
3. sharpe 和fitness,margin有增益，但是returns稍微有些负面影响，提交；


> [!NOTE] [图片 OCR 识别内容]
> N
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 7.95
> 0,03
> 6.48 %
> -0.02
> 5.50
> 0.01
> 5.98 %
> -0.02
> 0.48 %
> 0,01
> 18.46 %oo -0.01
> 川
> IS Performance After Submission (Equity, EUR, Delay-1 alphas)
> :
> Combined performance data is shown for all Equity, EUR, Delay-1 alphas. Submitting this alpha will not effect the combined performance ofyour other alphas
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2013
> 9.23
> 0.03
> 7.71 %
> -0.03
> 6.33
> 0.00
> 5.87 %
> -0.05
> 0.19 %
> 0.00
> 15.23 %o。
> -0.07
> 2014
> 10.36
> -0.11
> 6.14 %
> 0.02
> 7.52
> -0.14
> 6.59 %
> -0.10
> 0.17 %
> 0.00
> 21.45 %o。
> -0.28
> 2015
> 7.49
> -0.06
> 6.54 %
> -0.01
> 4.93
> -0.09
> 5.42 %
> -0.10
> 0.26 %
> 0.00
> 16.59 %o。
> -0.24
> 2016
> 6.42
> 0.12
> 6.39 %
> 0.02
> 4.22
> 0.11
> 5.40 %
> 0.08
> 0.42 %
> -0.01
> 16.90 %o。
> 0.29
> 2017
> 7.27
> 0.00
> 6.37 %
> 0.02
> 3.98
> 0.00
> 3.75 %
> 0.00
> 0.14 %
> -0.01
> 11.78 %o。
> 0.05
> 2018
> 7.54
> 0.06
> 6.35 %
> 0.02
> 4.60
> 0.02
> 4.66 %
> -0.03
> 0.44 %
> -0.01
> 14.69 %o。
> -0.06
> 2019
> 8.82
> 0.10
> 6.35 %
> 0.02
> 5.69
> 0.07
> 5.20 %
> 0.00
> 0.21 %
> 0.00
> 16.39 %o。
> 0.07
> 2020
> 7.06
> 0.05
> 6.54 %
> 0.02
> 5.19
> 0.05
> 6.75 %
> 0.04
> 0.48 %
> 0.01
> 20.62 %oo
> 0.14
> 2021
> 9.60
> 0.02
> 6.18 %
> -0.02
> 7.56
> 0.00
> 7.76 %
> -0.03
> 0.15 %
> 0.00
> 25.1
> 9oo
> 0.01
> 2022
> 9.06
> 0.05
> 6.35 %
> -0.01
> 7.62
> 0.03
> 8.84 %
> -0.04
> 0.25 %
> 0.01
> 27.87 %oo
> -0.03
> 2023
> -0.93
> 0.14
> 5.07 %
> 0.00
> -0.27
> 0.07
> 1.08 %
> 0.20
> 0.29 %
> 0.00
> -4.26 %oo
> 0.78
> Pnl


### 什么情况下不会提交：

1、margin不符合地区的最低要求，不提交

3、fitness 最近几年明显负面影响，不提交( 超过1个年份<-0.1)

4、sharpe  最近几年明显负面影响 ，不提交( 超过1个年份 <-0.1)

3、多个指标对组合负面明显过大，即使自相关性低，也不提交

很难一一列举对performance 影响的所有情况，是否提交这个因子，根据组合影响，个人情况判断。

### 从因子本身的指标来看：

1、sharpe>=1 ,fitness>=0.6 的前提下

margin 必须达到各地区margin要求的最低标准，我一般要求比最低标准高万分之五（USA，eur）,glb和ASI 地区的margin有时候比较难找到超过15的，在没有选择的情况下，一般ASI 最低14，15；GLB 14，15（少部分情况下会只要求>10【点塔】）

2、pnl线的波动比较小，向上，sharpe线 **不往下走；**

3、ASI 地区 还会观察下jpn的表现，如果jpn明显表现不佳或者或者kor表现明显大于其他地区的表现，不会提交

以上是我个人的一些经验，可能考虑还欠缺一些其他的点， **如果小伙伴有其他好的 判断方法，期待你评论区的分享**

**如果想要保证combine 的稳定，我个人的经验是 绝对不要提交margin不合格、fitness 负面影响过大、最近3年sharpe 线明显下降，pnl趋于厂 的因子（个人经验）**

**最后，给大家看看我现在的combine 情况，希望国区顾问的combine 都能保持稳定增长。**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.38
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 3.17
> Reached Grandmaster
> 0.5
> Combined Power Pool Alpha Performance
> 2.63


**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬分享。在因子指标合格的情况下，更注重is performance的情况，特别是fitness，简单直接，学习了


---

### 技术对话片段 9 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Eligibility Criteria篇】一文告诉你如何GOLD直通Grandmaster上篇置顶的论坛精选_39922788056343.md
- **时间**: 1个月前

**提问/主帖背景 (LX57490)**:
### 一、引言

大家好，我是来自兰州的一位大学生顾问，在AI发展迅速的现在，我没有学会我专业应该熟悉的算法，而是全权使用AI从0到1进行各种新事物的学习。从国际经济与贸易专业转到计算机科学与技术，赶上AI大爆发，从刚转过去就开始用AI，导致我虽然对代码一无所知，也能和AI对话制作出我想要的代码，当时还是半人工的方法，询问完，复制过来，我最开始的回测系统和AI模版以及自相关代码也是这样改出来的。而如今，AI已经可以自动化回测，自动写代码，真的只需要敲敲键盘，写下你的想法，就能实现你想要的结果，算是赶上了一波时代的红利，让我借此通过AI拿到了GrandMaster！

Gold直通GrandMaster的难度看似变高，实则变低了，为什么呢？听我细细说来：

1.  PPA虽然大削，但是大家使用的操作符数量都会上升，正常做RA被操作符影响的概率更低了，还能督促大家提高PPA质量到RA，从而保证combine！

2.  回测大削，大家不能无脑代码堆量低opPPA，此时奔着RA制作将是一个不错的选择，RA毕竟0.7以下就行，PPA还得保证0.5以下，或者用sharpe压过去，还是比较麻烦的。

3.  人数少，相较于M，GM的竞争力不高，虽然限制了75人，不过上赛季最终达标也就83/75人，只要能稳住combine，达到标准，基本上没什么太大问题！

**高筑墙！广积粮！缓称王！**

### **二、Eligibility Criteria**

#### **（一）Signals**  
> [!NOTE] [图片 OCR 识别内容]
> Signals
> 252
> Reached Grandmaster
> 020


我们这里使用 [LH44620](/hc/zh-cn/profiles/26717918976919-LH44620)  大佬开源的代码进行分析！

本季度共计317个alpha，其中Regular Alpha:252个，Super Alpha：65个 。

1.  主要制作USA，IND，EUR的SA，IND拉一下我的margin，USA,EUR正常稳固地区且好做。

2.  IND的model和analyst比较多，是因为听到IND手续费比较高，选择提升质量，拉高margin，降低turnover，稳固一点。

3.  EUR的model是当时为了吃2倍的加成，猛猛多高了点高质量，美美吃base。

4.  其余地区数据集，亮就跑。


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> IND
> ANALYST
> EARNINGS
> FUNDAMENTAL
> IMBALANCE
> INSIDERS
> INSTITUTIONS
> MACRO
> MODEL
> NEWS
> OPTION
> OTHER
> PV
> RISK
> SENTIMENT
> SHORTINTERES
> SOCIALMEDIA
  
> [!NOTE] [图片 OCR 识别内容]
> SA
> 26


#### **（二）Pyramids Completed**  
> [!NOTE] [图片 OCR 识别内容]
> Pyramids Completed
> 60
> Reached Grandmaster
> 10


一月下旬觉得有机会冲级GM，开始猛攻点塔，刚刚好凑够60塔，被迫五地区QAQ。IND RA开路，为我奠定了冲塔的基础，给足了做RA的信心，我以RA为基础，PPA为辅助进行冲级之路。

1.  IND USA EUR几乎百分之95的RA，几个PPA，绝大部分ATOM+RA。

2.  GLB 绝大部分PPA，因为三地区sharpe，我只能尽力接近，不能什么数据集都RA，且margin达标。赶上GLB TOPDIV3000 PPA 直接用COUNTRY起手，高质量快速PPA点完GLB。

3.  USA EUR GLB IND四地区GOLD点满也没有60塔，索性直接ASI RA，大地区总比小地区稳定，就是太难做了，下次我还是选小地区QWQ！

4. 基于（2026-4-22）目前版本对于我开的五地区进行难度排序：

ASI >>>> GLB > USA ≈ IND >  EUR


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GlB
> EUR
> ASI
> CHN
> KOR
> TN
> HKG
> JPN
> AR
> I0
> Analys:
> Broker
> Earnines
> Fundamentar
> Imbalanze
> Insizlers
> Instittions
> MIaro
> Madel
> NEWs
> 03tion
> C-hEI
> Frice VlUME
> Risk
> SEntiMERT
> Shai In-eres-
> Social Media


#### **（三）Combine**  
> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 1.98
> 0.02 more to Grandmaster
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.28
> Reached Grandmaster
> 0C


这里我们使用 [顾问 JG15244 (Rank 67)](/hc/zh-cn/profiles/26966744854807-顾问 JG15244 (Rank 67))  为国区无私开源的网址 [[链接已屏蔽])  进行分析！

#### **（一） Combined Alpha Performance**

1.  高质量RA，高质量PPA，高质量SA，死守各地区magin底线，其次越高越好。

2.  补救差地区提交高质量SA，拉高fitness，sharpe，magrin，returns，降低drawdown！

3.  margin建议：

- USA:  margin > 10 ( ILLIQUID_MINVOL1M > 15 )
- EUR:  margin > 10
- GLB:  margin > 15   (10+也可以)
- ASI:  margin > 15 (10 12 13也能忍受)
- IND:  margin > 15 (同时turnover低于15，我偏向于这个地区更降低一点，手续费偏高，需要更高margin，例如turnover 15  margin 15  我可能会把turnover降低到 12 10 9 8这样提交)
- 其余小地区均 > 15

#### **（二） Combined Power Pool Alpha Performance**

当我通过删改PPA tag，将0.14变成2.49后，我便没有轻易动，然后OS出来了，我删了os差的，然后combine明显变差，所以已知的os在未来两年依然是未知数，改变更好的IS反而会过拟合，影响表现。其次，达标以后，我交一个PPA，删一个ppa tag，以保我的combine还能维持住！


> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化趋势
> Combined Alpha
> POWer Pool
> 0
> Selected Alpha
> 0 Combined Osmosis
> Combined
> 3.00
> 2.00
> 1.00
> 0.00
> 1.00
> 2.00
> 202510
> 20251
> 202512
> 202601
> 202602


### 三、碎碎念

回顾三赛季历程，感叹时间飞速，在这期间我学到了很多知识，认识到了很多人，来自五湖四海，各行各业，各个年龄段，宛如线上旅游，了解各地工作就业情况，体验各个地区的人文交流，颇感良多，感谢各位一路陪伴，终于实现了Gold直通GrandMaster的奇迹！

#### **（一） IQC赛季（2025-Q2）**

从零开始的量化之路，我从一个回测界面Simulate都需要单词查询意思的人，通过翻译以及挨个按钮点击学习，了解到了WQ平台的运作原理，开始使用machine_lib.py代码为基础的回测流程，同一开始的无脑一二三阶，二三阶叠加，变成了有精准选择的使用一二阶。

1. 通过一阶代码，将ts_ops(ts_backfill(winsorize(单字段)))，选择改进零阶单字段，把单字段变成多字段组合形式，我提供给AI一个数据集里面的字段和描述，通过简单的四则运算给我一键制作零阶字段，省回测且有经济学意义的方法，例如新手教程的option8, call - put 双字段以后进行其他操作符叠加，得到alpha。

2. 通过给二阶代码加入相关性剪枝，进行对一阶alpha的剪枝，减去大部分重复alpha，并且关于bukcet进行更多的想象力，详细内容可以从课代表（ [XX42289](/hc/zh-cn/profiles/14187300941847-XX42289) ）的帖子进行学习，制作有经济学意义的特别bucket，这里面不只是bucket(rank)，不只是range ="0.1,1,0.1"，还可以更多的操作符，更多的字段，更多的参数范围，这使得我在IQC期间交了很多alpha。

#### **（二）初步了解赛季（2025-Q3）**

IQC顾问转正式顾问，跨度很大，IQC的长周期让人陷入在用户权限的温柔乡，在这里学习了很多知识，才进入顾问的状态。

1. 了解RA,ATOM,PPA,SA四大类的区别和提交区别，以及IS指标的作用，sc，ppac，pc三者的区别与联系。

2. 修改回测代码，将用户三并发改为8*10并发，解决4xx，5xx报错问题，使得代码更加稳健，除了亚马逊服务器崩了，一般不会再有问题了 : (

3. 读论坛所有经验贴，避雷贴，结合回测出来的alpha进行IS数据的初步了解，知道什么alpha可以提交，什么alpha肯定不能提交，学习什么会影响VF和combine稳定，地区这么多可不可以多开，新手应该交什么样的alpha，以至于我这个赛季就交了31个alpha，实际VF combine也还行，没什么大事，combine稳定提升，VF最低0.64，起码大于0.5。

#### **（三）稳扎稳打赛季（2025-Q4）**

终于学的差不多了，开始尝试冲级，此时的我combine从0.79变成了1.52上下徘徊，说明质量没什么问题，开始往上走，这个时候我不交PPA，对PPA还不是很明白，顶多是RA+PPA+ATOM这种情况，顺带提交PPA，这也是日后的一个伏笔。

1. PPA combine一直不咋好，0.14，删除了第一个不知道怎么提交的顾问PPA，更新一跃2.49，从此稳定2+，奠定了冲级的资格。

2. 此时我并不知道六维带来的影响很大，还是用着用户的方法，bucket使用的操作符很多，densify我也没删，操作符平均数量飙升，加上刚转顾问断了一天回测，六维太可怜了，赛季末使用华子哥插件expert排行985，遗憾被刷，依然GOLD。

3. 但是当时做出来的alpha，在日后的OS更新后，明显可以看出来，质量很好，不过操作符比较多，bucket的二阶是一个提升质量不可多得好方法！

#### **（四）奇迹出现赛季（2025-Q1）**

三赛季铺垫，终于厚积薄发！开头的我也是几天偶尔交一个，到了赛季更新后，各种新规则出来，我下定决心，直冲GM，二月初的时候我也不到7个塔，直接二月底到达35塔，四月冲级60塔，人不逼自己一把，不知道自己的上限有多高！

1.  PPA大削，趁机通过RA进行点塔，我采用5op，2fileds方式进行RA制作，保证我的六维维持在这附近，下篇我会详细讲六维这方面。

2.  返璞归真，AI+machine_lib，制作模版，遍历模版，保证4+1点塔，按照数据集进行分析，不同数据集制作不同模版，同数据集同预处理模版，二次切换不同一阶二阶，可得到无穷无尽的RA，只不过还需要看IS和近四年趋势，有些RA我并不会选择提交。

3.  华子哥RAW数据横空出世！得到了全部数据，我开始精准选择我有的数据集，通过筛选我的要求，进行选择中性化和字段，精准打击alpha！既然他们能做出来，那我也能做出来的思想，做出来一个又一个小数据集的ATOM+RA！

最后的最后，再次感谢各位朋友陪伴，使得我能够创造奇迹：

感谢WQ平台，感谢国区各位老师，感谢研究小组二群的各位，感谢IQC的朋友们（以下排名，不分先后）：

感谢weijie老师，kunqi老师，huangkai老师，顾问 KZ79256 (Rank 21) (华子哥)，XX42289 (课代表) ，worldquant brain赛博游戏王 (游戏王)，顾问 QX52484 (Rank 35) (司源老师)，顾问 FX25214 (Rank 22)，DA98440，JX39934，ZH41150，顾问 RM49262 (Rank 30)，PP26750， LD27384，顾问 JG15244 (Rank 67)，LS17092，WT73952，XJ80376，QW94165，ZY20347，JZ45765，ll46807，JW52291等研究小组二群的各位朋友们！！！！

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬干货满满的分享，太强了。这塔点的，赏心悦目。国区大佬有东西是真分享，感谢。


---

### 技术对话片段 10 (原帖: 【Template by Tiger】 关于news21中的fast_d1的一个思路)
- **原帖链接**: [Commented] 【Template by Tiger】 关于news21中的fast_d1的一个思路.md
- **时间**: 5个月前

**提问/主帖背景 (ZZ13271)**:
话不多说，直接上模版：

group_rank(winsorize(ts_backfill(news21_a/news21_b,252),std=4),gr)

表现还不错，出货也可以，pc在USA还能低于0.7也实属难得


> [!NOTE] [图片 OCR 识别内容]
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> IS Summary
> Period
> 05
> Theme: Fast D1 Theme x2
> A Single Data Set Alpha
> [ Power Pool Alpha
> 眙 Regular Alpha
> U FastD1 Alpha
> Pyramid theme: USAIDTIFUNDAMENTAL XT.1
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Re-Urns
> 13TOULN
> Nargin
> 1.99
> 4.339
> 1.52
> 7.339
> 4.939
> 33.849600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.79
> 4,5336
> 0.96
> 3.593
> 1.049
> 15.529620
> 737
> 1462
> 2014
> 3.31
> 3.88%
> 2.77
> 8.511
> 1.173
> 44.435230
> 845
> 155-
> 2015
> ,829
> 1.25
> 5.751
> 2.633
> 2%30
> 891
> 1553
> 2016
> 3.9536
> 2.-4
> 8.321
> 5995
> 44.656520
> 915
> 1502
> 2017
> 2.54
> 4.35%
> 1.80
> 6.2715
> 1.573
> 28.795220
> 995
> 139
> 2018
> 2.27
> 4.799
> 1.89
> 8.551
> 1.-23
> 45220
> 1533
> 883
> 激活 Winoows
> 2019
> 3,97%
> 014
> 36
> 3.8795
> 6.37520
> 1520
> 399
> 转到"设置"以激活 Windows


news21的fast_d1字段如下，全在这了：

event_end_date_is_estimated_fast_d1
event_end_date_type_fast_d1
event_end_time_fast_d1
event_fiscal_year_fast_d1
event_quarter_label_fast_d1
event_start_date_is_estimated_fast_d1
event_start_date_type_fast_d1
event_start_time_2_fast_d1
info10_event_type_code_simple_fast_d1
info10_expiration_date_simple_fast_d1
info10_expiration_time_simple_fast_d1
info10_last_update_date_simple_fast_d1
info10_last_update_time_simple_fast_d1
info10_negative_sentiment_score_simple_fast_d1
info10_negative_word_count_simple_fast_d1
info10_positive_sentiment_score_simple_fast_d1
info10_positive_word_count_simple_fast_d1
info10_start_date_simple_fast_d1
info10_start_time_simple_fast_d1
info10_tone_score_simple_fast_d1
info10_version_label_simple_fast_d1
last_event_timestamp_info10_simple_fast_d1
last_event_timestamp_streetevents2_fast_d1
nws21_abz4s2_eventtype_fast_d1
nws21_abz4s2_neg_freq_fast_d1
nws21_abz4s2_neg_sc_fast_d1
nws21_abz4s2_pos_freq_fast_d1
nws21_abz4s2_pos_sc_fast_d1
nws21_abz4s2_tone_sc_fast_d1
nws21_abz4s2_version_fast_d1
nws21_participants_fast_d1
nws21_qa_count_fast_d1
streetevents2_expiration_date_fast_d1
streetevents2_expiration_time_fast_d1
streetevents2_last_update_date_fast_d1
streetevents2_last_update_time_fast_d1
streetevents2_start_date_fast_d1
streetevents2_start_time_fast_d1

**顾问 QL47372 (Rank 36) 的解答与建议**:
模板、数字字段全都有，虎哥真是威武霸气！感谢分享

=============================================================================

路漫漫其修远兮，吾将上下而求索。

=============================================================================


---

### 技术对话片段 11 (原帖: 【Template by Tiger】 关于news21中的fast_d1的一个思路)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Template by Tiger】 关于news21中的fast_d1的一个思路_37256491735959.md
- **时间**: 5个月前

**提问/主帖背景 (ZZ13271)**:
话不多说，直接上模版：

group_rank(winsorize(ts_backfill(news21_a/news21_b,252),std=4),gr)

表现还不错，出货也可以，pc在USA还能低于0.7也实属难得


> [!NOTE] [图片 OCR 识别内容]
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> IS Summary
> Period
> 05
> Theme: Fast D1 Theme x2
> A Single Data Set Alpha
> [ Power Pool Alpha
> 眙 Regular Alpha
> U FastD1 Alpha
> Pyramid theme: USAIDTIFUNDAMENTAL XT.1
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Re-Urns
> 13TOULN
> Nargin
> 1.99
> 4.339
> 1.52
> 7.339
> 4.939
> 33.849600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.79
> 4,5336
> 0.96
> 3.593
> 1.049
> 15.529620
> 737
> 1462
> 2014
> 3.31
> 3.88%
> 2.77
> 8.511
> 1.173
> 44.435230
> 845
> 155-
> 2015
> ,829
> 1.25
> 5.751
> 2.633
> 2%30
> 891
> 1553
> 2016
> 3.9536
> 2.-4
> 8.321
> 5995
> 44.656520
> 915
> 1502
> 2017
> 2.54
> 4.35%
> 1.80
> 6.2715
> 1.573
> 28.795220
> 995
> 139
> 2018
> 2.27
> 4.799
> 1.89
> 8.551
> 1.-23
> 45220
> 1533
> 883
> 激活 Winoows
> 2019
> 3,97%
> 014
> 36
> 3.8795
> 6.37520
> 1520
> 399
> 转到"设置"以激活 Windows


news21的fast_d1字段如下，全在这了：

event_end_date_is_estimated_fast_d1
event_end_date_type_fast_d1
event_end_time_fast_d1
event_fiscal_year_fast_d1
event_quarter_label_fast_d1
event_start_date_is_estimated_fast_d1
event_start_date_type_fast_d1
event_start_time_2_fast_d1
info10_event_type_code_simple_fast_d1
info10_expiration_date_simple_fast_d1
info10_expiration_time_simple_fast_d1
info10_last_update_date_simple_fast_d1
info10_last_update_time_simple_fast_d1
info10_negative_sentiment_score_simple_fast_d1
info10_negative_word_count_simple_fast_d1
info10_positive_sentiment_score_simple_fast_d1
info10_positive_word_count_simple_fast_d1
info10_start_date_simple_fast_d1
info10_start_time_simple_fast_d1
info10_tone_score_simple_fast_d1
info10_version_label_simple_fast_d1
last_event_timestamp_info10_simple_fast_d1
last_event_timestamp_streetevents2_fast_d1
nws21_abz4s2_eventtype_fast_d1
nws21_abz4s2_neg_freq_fast_d1
nws21_abz4s2_neg_sc_fast_d1
nws21_abz4s2_pos_freq_fast_d1
nws21_abz4s2_pos_sc_fast_d1
nws21_abz4s2_tone_sc_fast_d1
nws21_abz4s2_version_fast_d1
nws21_participants_fast_d1
nws21_qa_count_fast_d1
streetevents2_expiration_date_fast_d1
streetevents2_expiration_time_fast_d1
streetevents2_last_update_date_fast_d1
streetevents2_last_update_time_fast_d1
streetevents2_start_date_fast_d1
streetevents2_start_time_fast_d1

**顾问 QL47372 (Rank 36) 的解答与建议**:
模板、数字字段全都有，虎哥真是威武霸气！感谢分享

=============================================================================

路漫漫其修远兮，吾将上下而求索。

=============================================================================


---

### 技术对话片段 12 (原帖: 【效率王】七十二变的大升级_跨区点塔？指定Category?完全不是问题！)
- **原帖链接**: [Commented] 【效率王】七十二变的大升级_跨区点塔指定Category完全不是问题.md
- **时间**: 5个月前

**提问/主帖背景 (CQ89422)**:
关于七十二变的初步介绍已在这里，不多赘述了👉 [【效率王】七十二变！AI助力一个Alpha变成更多个Alpha! – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template.md?input_string=%E3%80%90%E6%95%88%E7%8E%87%E7%8E%8B%E3%80%91%E4%B8%83%E5%8D%81%E4%BA%8C%E5%8F%98%E7%9A%84%E5%A4%A7%E5%8D%87%E7%BA%A7) 。 **快升级到1.8.7体验吧！**

最新功能如下展示，你可以将任意一个好的Alpha进行指定区域的变换，同时指定data category。缺啥点啥。再配上缘分一道桥的功能（ [【效率王】横向点塔神器！左脚踩右脚我直接起飞]([Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞.md) ），点塔还是问题吗？轻松拿捏！


> [!NOTE] [图片 OCR 识别内容]
> Alpha ID
> Datafield
> N (数值越大娈种数量越多,建议低于50)
> 目标地区 (可选
> 留空则使用种子Alpha的默认值)
> 使用种孑Nphal认值
> 目标Delay (可选
> 留空则使用种子Alpha的默认值)
> 使用种孑Nphal认值
> 目标股票池 (可选 -留空则使用种子Alpha的默认值)
> 使用种孑Alpha栽认值
> 目标数据类别 (可多选)
> 不筛选(默认)
> Top


[【Community Leader -因子构造 💎】Alpha模板库，来自社区的馈赠，为你的72变添砖加瓦](../顾问 MZ45384 (Rank 51)/[Commented] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template.md)

**快升级到1.8.7体验吧** 。最近吹哨发帖有点多了，祝大家春节愉快了。

**顾问 QL47372 (Rank 36) 的解答与建议**:
工具是个好工具，用什么大模型很重要，免费的大模型出货率实在有点感人……


---

### 技术对话片段 13 (原帖: 【效率王】七十二变的大升级_跨区点塔？指定Category?完全不是问题！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变的大升级_跨区点塔指定Category完全不是问题_36974265471511.md
- **时间**: 5个月前

**提问/主帖背景 (CQ89422)**:
关于七十二变的初步介绍已在这里，不多赘述了👉 [【效率王】七十二变！AI助力一个Alpha变成更多个Alpha! – WorldQuant BRAIN]([L2] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template_36671111976983.md?input_string=%E3%80%90%E6%95%88%E7%8E%87%E7%8E%8B%E3%80%91%E4%B8%83%E5%8D%81%E4%BA%8C%E5%8F%98%E7%9A%84%E5%A4%A7%E5%8D%87%E7%BA%A7) 。 **快升级到1.8.7体验吧！**

最新功能如下展示，你可以将任意一个好的Alpha进行指定区域的变换，同时指定data category。缺啥点啥。再配上缘分一道桥的功能（ [【效率王】横向点塔神器！左脚踩右脚我直接起飞]([Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md) ），点塔还是问题吗？轻松拿捏！


> [!NOTE] [图片 OCR 识别内容]
> Alpha ID
> Datafield
> N (数值越大娈种数量越多,建议低于50)
> 目标地区 (可选
> 留空则使用种子Alpha的默认值)
> 使用种孑Nphal认值
> 目标Delay (可选
> 留空则使用种子Alpha的默认值)
> 使用种孑Nphal认值
> 目标股票池 (可选 -留空则使用种子Alpha的默认值)
> 使用种孑Alpha栽认值
> 目标数据类别 (可多选)
> 不筛选(默认)
> Top


[【Community Leader -因子构造 💎】Alpha模板库，来自社区的馈赠，为你的72变添砖加瓦]([L2] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template_37117908343831.md)

**快升级到1.8.7体验吧** 。最近吹哨发帖有点多了，祝大家春节愉快了。

**顾问 QL47372 (Rank 36) 的解答与建议**:
工具是个好工具，用什么大模型很重要，免费的大模型出货率实在有点感人……


---

### 技术对话片段 14 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】你说你没有模板这里你多得用不完.md
- **时间**: 5个月前

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

**顾问 QL47372 (Rank 36) 的解答与建议**:
AI时代，工具是越来越多，看似简化了很多流程，效率提升了很多。但如果自身没有理解，很容易被AI给糊弄住，自己的思考至关重要。


---

### 技术对话片段 15 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **时间**: 5个月前

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

**顾问 QL47372 (Rank 36) 的解答与建议**:
AI时代，工具是越来越多，看似简化了很多流程，效率提升了很多。但如果自身没有理解，很容易被AI给糊弄住，自己的思考至关重要。


---

### 技术对话片段 16 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞.md
- **时间**: 5个月前

**提问/主帖背景 (CQ89422)**:
吹哨人我又来了。看到了MCP里的新工具


> [!NOTE] [图片 OCR 识别内容]
> 缘分一道桥 (Alpha 跨区连锁)
> 返回主页
> C 使用说明
> 1.获取一段时间内的Alpha列表
> 2.分析每个 Alpha里的数据字段并迸行强替换。查看是否在其他Region/Universe/Delay有同样字段
> 3.生成新的Alpha
> 4.本页面的回测方式为排队回测; 一个完成后才会发送另一个;因此中途退出页面会中断回测
> 5.过长的回测队列有时会因为账号超时登出而出现连续失败。因此不建议选择过长时间跨度
> 6.如想批量回测;请下载所有待回测的Alphaf 选择首页回测器迸行回测
> 7.如果你想;你可以输入个很大的时间范围;下载所有表达式。慢慢迸行批量回测。


这个能直接一键回测并且横向点塔。更新到1.7.0版本以上就有噢。

我已经想到这样美好的图景：

- 1.横向点塔 （跨区、跨Universe)
- 2.点亮的塔，放入72变纵向点塔
- 3.被72变点量的纵向塔，再用桥，横向点塔。
- 4.横向点了塔，再72变
- 5. 如此反复，无穷尽也

以后我的研究，只需要专注于做好1-2个手搓或者AI合作的高级货，就能不断繁衍了！

效果不错，单击一下就能直接排队回测，我已经又完成了今天的提交。


> [!NOTE] [图片 OCR 识别内容]
> 2025-11-30104:40:58-05;00
> 10 个可用娈体
> 表达式: Srowp
> IIOIJLalize (1
> subindustry}
> 夏普: 0.65|收益:4.1%
> 戛普:0.69
> 收益:
> 4%
> 夏普:1.121收益:6.0%
> 夏普:0.95
> 收益:4.9%
> 夏普:
> 收益:
> .8%
> 夏普:086
> 收益:4.5%
> 戛普:0.76
> 收益:4.1%
> 戛普:1.16 |收益:7.7%
> 夏普:1.11 |收益:7.5%
> 夏普
> 1.05
> 收益-7.2%


再次叠甲：如有侵权，请联系本人。再次感谢作者。

**顾问 QL47372 (Rank 36) 的解答与建议**:
搞出这个cnhkmcp_app的大佬真是天才，太佩服了，现在首页还有使用说明，简单明了。感谢大佬。


---

### 技术对话片段 17 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md
- **时间**: 5个月前

**提问/主帖背景 (CQ89422)**:
吹哨人我又来了。看到了MCP里的新工具


> [!NOTE] [图片 OCR 识别内容]
> 缘分一道桥 (Alpha 跨区连锁)
> 返回主页
> C 使用说明
> 1.获取一段时间内的Alpha列表
> 2.分析每个 Alpha里的数据字段并迸行强替换。查看是否在其他Region/Universe/Delay有同样字段
> 3.生成新的Alpha
> 4.本页面的回测方式为排队回测; 一个完成后才会发送另一个;因此中途退出页面会中断回测
> 5.过长的回测队列有时会因为账号超时登出而出现连续失败。因此不建议选择过长时间跨度
> 6.如想批量回测;请下载所有待回测的Alphaf 选择首页回测器迸行回测
> 7.如果你想;你可以输入个很大的时间范围;下载所有表达式。慢慢迸行批量回测。


这个能直接一键回测并且横向点塔。更新到1.7.0版本以上就有噢。

我已经想到这样美好的图景：

- 1.横向点塔 （跨区、跨Universe)
- 2.点亮的塔，放入72变纵向点塔
- 3.被72变点量的纵向塔，再用桥，横向点塔。
- 4.横向点了塔，再72变
- 5. 如此反复，无穷尽也

以后我的研究，只需要专注于做好1-2个手搓或者AI合作的高级货，就能不断繁衍了！

效果不错，单击一下就能直接排队回测，我已经又完成了今天的提交。


> [!NOTE] [图片 OCR 识别内容]
> 2025-11-30104:40:58-05;00
> 10 个可用娈体
> 表达式: Srowp
> IIOIJLalize (1
> subindustry}
> 夏普: 0.65|收益:4.1%
> 戛普:0.69
> 收益:
> 4%
> 夏普:1.121收益:6.0%
> 夏普:0.95
> 收益:4.9%
> 夏普:
> 收益:
> .8%
> 夏普:086
> 收益:4.5%
> 戛普:0.76
> 收益:4.1%
> 戛普:1.16 |收益:7.7%
> 夏普:1.11 |收益:7.5%
> 夏普
> 1.05
> 收益-7.2%


再次叠甲：如有侵权，请联系本人。再次感谢作者。

**顾问 QL47372 (Rank 36) 的解答与建议**:
搞出这个cnhkmcp_app的大佬真是天才，太佩服了，现在首页还有使用说明，简单明了。感谢大佬。


---

### 技术对话片段 18 (原帖: 【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的)
- **原帖链接**: [Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的.md
- **时间**: 5个月前

**提问/主帖背景 (XZ23611)**:
今天我们来聊聊顾问的名片指标也是GENIUS最重要的指标： **Combined Alpha Performance** 。无论你是刚入门的新人，还是已经提交了几百个 alpha 的“老手”，这个话题都值得你花点时间认真琢磨。因为理解它，不仅能帮你提升 alpha 的表现，还能让你少走很多弯路。

## **什么是 Combined Alpha Performance？**

先说说这个“Combined Alpha Performance”到底是什么。简单来说，它是一个用来衡量所有提交过的 alpha 和 super alpha 的整体表现的指标。它的计算方式很直接：把所有地区已经提交的 alpha 和 super alpha  **等权组合** ，然后看它们在 2023-2025 年（semi-OS）的表现，具体是 **费后表现。**

这就像是一个大锅饭——你提交的每一个 alpha 都是这锅饭里的一粒米，表现好的米会让这锅饭更香，而表现差的米则可能毁掉整锅饭的味道。所以， **Combined Alpha Performance**  不仅仅是一个数字，它实际上反映了你提交的 alpha 是否在整体上“靠谱”。

## **计算原理：从公式看本质**

Combined Alpha Performance 的计算公式其实很简单：
 **等权组合 + 手续费调整 + 2023-2025 年的费后表现** 。

换句话说，平台会把你提交的所有 alpha 和 super alpha 按等权组合起来，然后在 2023-2025 年的市场环境下模拟它们的表现，最后扣除手续费，得出一个费后的 Sharpe 值。

从这个公式里，我们可以提炼出三个提升表现的关键词：

```
分散、质量、手续费。
```

接下来，我们就从这三个关键词出发，聊聊如何一步步提升你的 Combined Alpha Performance。

## **关键词一：分散（Diversity)**

### **为什么分散很重要？**

分散的核心在于降低风险。就像投资一样，如果你把所有的钱都投在一个篮子里（比如一个地区、一个模板），一旦这个篮子表现不好，你的整体表现就会被拖累。而分散可以让你的 alpha 表现更加稳定，减少单一因素的影响。

### **如何做到分散？**

1. **地区分散** ：
   最容易做到的分散就是  **region 的分散** 。不同地区的市场环境、手续费、波动性都不一样，把 alpha 分散到多个地区，可以有效降低单一区域表现不佳的风险。
2. **降低同一地区的 SC（Self Correlation）** ：
   在同一个 region 下，尽量降低 alpha 之间的相关性（SC）。最直接的方法就是多用不同类型的模板和数据类别（category）。也就是多点塔（Pyramid）这里要注意一点：我们说的“点塔”是指  **主信号**  的多样性，而不是通过科技（技术优化）或者附带信号来实现的点塔。换句话说，真正的分散是从信号本身出发，而不是靠“修修补补”来实现。

### **总结**

分散是提升 Combined Alpha Performance 的第一步，也是最容易做到的一步。记住： **多地区、多模板、多数据类别** ，多中性化，尤其是风险中性化，让你的 alpha 表现更加稳健。

## **关键词二：质量**

### **质量比数量更重要**

不管是 Combined Alpha Performance 还是 VF(Value Factor），在不能兼顾的情况下， **质量永远比数量重要得多** 。一个质量差的 alpha 不仅不会给你的组合加分，反而会拖累整体表现。而且，质量差的 alpha 需要很多个高质量的 alpha 来弥补。

### **举个例子：一个负的 OS Sharpe 如何拖累组合表现？**

#### **假设场景**

我们有一个组合，资金规模为  **100 万美元** ，包含以下几个 alpha：

- **Alpha A** ：OS Sharpe = -1
- **Alpha B** ：OS Sharpe = +1
- **Alpha C** ：OS Sharpe = +1

这些 alpha 是等权分配资金的，也就是说每个 alpha 分配的资金为：
 **100 万 ÷ 3 = 33.33 万美元** 。

#### **计算组合表现**

1. **Alpha A 的影响** ：
   - Alpha A 的 OS Sharpe = -1，相当于这 33.33 万美元的资金在拖累组合表现。
2. **Alpha B 和 Alpha C 的贡献** ：
   - Alpha B 和 Alpha C 的 OS Sharpe = +1，它们的表现为组合提供了正收益。
3. **组合表现** ：
   - 由于等权组合的 Sharpe 是所有 alpha 的加权平均值，Alpha A 的负表现会显著拉低整体表现。
   - 结果是：即使有两个 OS Sharpe = +1 的 alpha，组合的 Sharpe 也只有  **0.33** ，远低于 +1。一个负的alpha 让原本+1的组合表现降低了-66%

#### **需要多少好的 alpha 来弥补？**

如果我们想让组合的 Sharpe ≥ +1，那么至少需要  **2 个 OS Sharpe = +1 的 alpha 来弥补 1 个 OS Sharpe = -1 的 alpha** 。
如果有 2 个 OS Sharpe = -1 的 alpha，则需要至少  **4 个 OS Sharpe = +1 的 alpha**  来弥补。

### **如何提升质量？**

1. **关注 alpha 的核心逻辑** ：
   一个 alpha 的质量，核心在于它的逻辑是否有意义。不要为了提交而提交，确保你的 alpha 有清晰的经济学或统计学依据。论坛内有很多其它顾问的内容，就不在此赘述
2. 巧用AI和MCP来帮助我们验证一个alpha是否有意义。在MCP样例中就有如何写出alpha description （验证是否合理）和 alpha performance improvement会让你受益匪浅

[使用MCP成功地将alpha优化成可提交状态的案例 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 使用MCP成功地将alpha优化成可提交状态的案例经验分享.md)

### **总结**

质量是 Combined Alpha Performance 的基石。在不能兼顾的情况下，不要盲目追求数量，专注于打磨高质量的 alpha。

## **关键词三：手续费**

### **手续费的影响**

我们在提交 alpha 时看到的 Sharpe，都是  **不计手续费**  的。但在 Combined Alpha Performance 和真实的市场交易中，手续费是必须考虑的。

如果一个 alpha 的 margin（利润空间）过低，那么在扣除手续费后，原本的正 Sharpe 可能会变成负的，或者大幅降低。

### **如何控制手续费？**

1. **关注 ASI** ：
   不同市场的手续费标准不同。通常来说：
   - **亚洲市场（ASI）** ：尽量保持在 15 以上，20以上为佳。
   - **其他地区** ：建议保持在 10 以上。
2. **优化交易频率** ：
   如果一个 alpha 的交易频率过高，手续费会显著增加。通过调整 decay 或者优化信号，可以有效降低交易频率，从而减少手续费。论坛内有其它帖子自行搜索
3. **避免低 margin 的 alpha** ：
   提交前，检查 alpha 的 margin。如果 margin 太低，即使 Sharpe 看起来不错，也可能在扣除手续费后变得毫无价值。

## **关于 Super Alpha（SA）：双刃剑的误区与正确使用**

### **误区：IS Sharpe 高的 SA 一定能提升表现**

很多人会觉得， **SA 的 IS Sharpe 高** ，所以它一定能在 OS 中表现得很好。但事实是， **IS 的表现和 OS 的表现没有直接关系** 。一个 IS Sharpe 高达 10 的 SA，在 OS 中可能会是负的表现。

### **风险：质量差的 RA 会让 SA 成为“双倍伤害”**

SA 是通过组合多个原始 alpha（RA）生成的。如果这些 RA 的质量本身就很差，那么 SA 的表现也不会好。正所谓  **“Garbage In, Garbage Out”** ，如果你用的是“垃圾”原材料，SA 只会把这些问题放大。

### **如何正确使用 SA？**

- **过滤掉 IQC 表现差的 RA** ：如果IQC的OS表现不好，组SA时候学会剔除 product_correlation > 0 的 RA，确保组合的分散性。
- **确保 RA 的质量** ：优先选择 OS 表现稳定且为正的 RA。
- **优化组合逻辑** ：降低相关性，分散风险，提升 SA 的稳定性。

## **结语：提升 Combined Alpha Performance 的核心思路**

总结一下，提升 Combined Alpha Performance 的核心在于三个关键词： **分散、质量、手续费** 。

- **分散** ：多地区、多模板、多数据类别，多风险中性化，降低风险。
- **质量** ：专注于高质量的 alpha，避免被低质量的 alpha 拖累。
- **手续费** ：优化交易频率，确保 ASI 达标，避免低 margin 的 alpha。

最后送给大家一句话： **“少即是多，精益求精。”**  希望这篇文章能对你有所启发，祝大家的 Combined Alpha Performance 节节高升！

**顾问 QL47372 (Rank 36) 的解答与建议**:
今天更新了Combined Alpha Performance，惨不忍睹。再来复习下基础知识，依然有收获，感谢大佬的分享。


---

### 技术对话片段 19 (原帖: 根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"]))
- **原帖链接**: [Commented] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的.md
- **时间**: 5个月前

**提问/主帖背景 (MH33574)**:
## 引言：为什么我们要关心 PC？

 **降低 PC 是提升收益和保证账号健康的最重要因素之一** 。

1. PC的高低直接影响个人短期（base payment)和长期收入 (quarterly payment),
2. PC的高低间接影响Value Factor，从而再次影响收入
3. 高PC alpha 无法入库，无法参与比赛，长期提交大量高pc alpha，可能会导致账户封禁

## 一、理解Product Correlation

### 什么是 Product Correlation（PC）？

PC 衡量一个 alpha 与平台中其他 顾问提交的alpha 的相关性，其计算公式和自相关类似，为最近四年PNL 每日变化（diff）的皮尔逊相关性系数。

### PC高低与收入的关系

顾问提交的alpha被平台接收后，会进行多次筛选以决定是否对平台有用，其中最重要的筛选就是PC。当PC大于0.7，则被认为是相同/及其相近的alpha，则该alpha不会被平台采用，因此也不会有机会获得任何weight。在顾问协议中披露的每日base payment 计算公式中也明确提到与base payment与PC的负相关性。通常来说，当pc< 0.5 会被认为是比较独特的因子，从而会获得更高的base payment，也更有机会被基金经理采纳而获得weight，进而获得更高的quarterly payment。

而更低的PC也意味着更低的SC，组合的correlation 越低，也会进一步提升组合的整体多样性表现，从而获得更好的value factor。从个人经验看，在点塔的时候偶尔提交了更高的pc alpha，相应的该月份的vf就会受到影响。不知道平台在计算vf的时候是否对高pc有额外的惩罚系数。

### 举例说明PC高低与收入的实证

Alpha 1： PC 0.49的SA，获得了58.97的 base payment


> [!NOTE] [图片 OCR 识别内容]
> anonymoUs
> Super
> ACTIVE
> 08/30/2025 EDT
> JPN
> TOP1600
> 0.31
> 0.49



> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 08/30/2025
> Super:
> 58.97
> Regular:
> 7.94
> Total:
> 66.91
> 40
> 20
> 28.
> 29.
> 30.
> 31 _
> 1.Sep
> 2.Sep
> Aug
> Aug
> Aug
> Aug


Alpha 2：SAC 期间的一个表现更好的alpha，PC 0.68，只获得了9.69 USD的收入。而7月14日一个0.73的pc 只获得了5.4USD的收入。对不起当时0.9+的VF


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/19/2025
> Super:
> 9.69
> Regular:
> 8.10
> 15
> Total:
> 17.79
> 10
> 14.Jul
> 15.Jul
> 16.Jul
> 17.JUl
> 18.Jul
> 19.Jul
> 20.Jul


# **二、如何检查PC并降低PC的实操**

**获取PC的代码：论坛有很多，部分同学反馈没有权限，已更新在评论区**

[[链接已屏蔽])

**几个注意事项：**

1. 不建议直接只用check submission的接口，会更慢，因为要检查其他的测试比如自相关，而自相关等检测都可以在本地完成，效率更高
2. 该接口也会限流，甚至影响提交alpha，建议做一些在本地的限流，这样不触发平台限流，从而获得整体的结果最优（代码如下，可以自己调整睡眠时间）
3. 极少数情况会pc通过但是提交失败，这是因为pc是用的缓存数据，在pc检查和提交之间如果别人交了类似的会在提交时候出现pc不过的情况，但这种情况极少极少。

```
s = login()start_time = datetime.now()pass_pc_ids = []last_request_time = datetime.now()max_sleep_time = 60 * 60 # 最大睡眠时间1小时current_sleep_time = 60 # 初始睡眠时间60秒定义重连时间间隔reconnect_interval = timedelta(hours=3.5)for id in batch_ids:# 检查是否需要重新登录current_time = datetime.now()if current_time - start_time >= reconnect_interval:s = login()start_time = current_time# 记录请求开始时间request_start_time = datetime.now()# 调用 get_prod_corrpc = get_prod_corr(s, id)# 记录请求结束时间request_end_time = datetime.now()request_duration = (request_end_time - request_start_time).total_seconds()# 检查相关性if pc > 0.7:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['PROD Correlation'])elif pc >0.5:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['ace_tag'])else:result = get_simulation_result_json(s,id)selection = result['selection']['code']tag_value = ['PC 0.5','Ready to Submit']name_value = result['name']if "own" in selection:color = 'GREEN'count = count+1else:color = 'None'combo = result['combo']['code']while len(selection)<100:selection = selection + selectionwhile len(combo)<100:combo = combo + combo set_alpha_properties(s,id,name_value,selection_desc=selection,combo_desc=combo,tags=tag_value,color=color)pass_pc_ids.append(id)print(id,pc)# 计算上次请求到本次请求的时间间隔time_since_last_request = (request_start_time - last_request_time).total_seconds()# 如果请求时间明显增加，调整睡眠时间if request_duration > current_sleep_time * 1.5:current_sleep_time = min(max_sleep_time, current_sleep_time * 2)else:current_sleep_time = 60 # 如果请求时间正常，恢复默认睡眠时间# 更新上次请求时间last_request_time = request_start_time# 等待当前睡眠时间time.sleep(current_sleep_time)print(len(pass_pc_ids))
```

## 三、如何降低 PC？

Global 论坛有一篇外区的帖子，有些内容是很有可取之处的

- [Reduce Production Correlations. – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] Reduce Production Correlations.md)

### 避免使用过于常见的 signal

- 如单纯的暴力一二三阶，没有任何自己的迭代

### 增加创新表达方式

- 多尝试非线性组合、二阶交叉项、相对排名等。使用sigmoid，sign power，ts linear window等做一些数学变换
- 尝试使用target tvr的几个operator来降低tvr的同时也会变化pnl从而降低pc （但有时会反而提高，因为别人也使用了该方法提交过）

### 尝试多种region，unvierse和netralization 方式

- 一些高pc的因子，在变换了中性化，unvierse和regioin后会有意想不到的收获，而这个可以代码工程化完成

### 多尝试新的数据集

- 当有新的数据集，新的unvnierse和新的region的时候是pc最低的时候，如TOPDIV3000，最近新上的数据集等

### 使用独特的分组方式

- 最常见的是group datafield （如other455），bucket分组

### 当然王牌还是有自己的模版和自制数据

### 如何快速总结已经提交alpha的PC：

在alphas菜单中点击submitted，选中select column 勾选product correlation，已经提交alpha的PC一目了然


> [!NOTE] [图片 OCR 识别内容]
> 鬯2
> Simulate
> Alphas
> Leamn
> Data
> Labs
> Genius
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> 《
> Refer a friend
> Select Columns
> Summany
> Properties
> Settings
> Perommance
> Alphas
> Nams
> SzazUs
> Resion
> Instrument TypE
> Sharpe
> Rezurns
> Competi-ion
> Catesory
> Universe
> Delay
> Pnl
> Turnoer
> Page size
> Typ=
> Color
> Decay
> Neutralization
> Drawdown
> Marsin
> Fllter
> LansuaEs
> TaE
> Truncation
> Unit Handlins
> Fitnsss
> Book Sizs
> Date Submit-ed (EST]
> Hidgzn
> NaN Handlins
> Pasteurization
> ~oun
> Shor Count
> Select Columns
> Turnover
> Tag
> Favorite
> Sharo 50
> Sharpe 125
> S-ar Date (EST
> Sharpe 250
> Sharpe 500
> 22
> See
> OSIIS Razio
> Pre Close Sharpe
> 4.974
> Pre-Close Razio
> Self-Correlation
> Prod-Correlation
> Reset
> Apply
> Lns


最后祝大家新的赛季VF和Genius双高！如果对你有用还请点赞评论！

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢大佬的分享，不仅解读了PC跟收入的关系，还给出了降低PC的实操方案，很受用。

现在还只能把PC艰难的控制在0.7以下，希望能早日把它再降一档。


---

### 技术对话片段 20 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月7日，我的量化日记第七季打卡第一天

IND区有主题，真是太卷了，好多看着很漂亮的因子，都是高PC


---

### 技术对话片段 21 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月8日，我的量化日记第七季打卡第二天

继续IND区。马上限回测数了，工作流优化中，加油！


---

### 技术对话片段 22 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月9日，我的量化日记第七季打卡第三天

IND区卷不动了，转战GLB，加油！


---

### 技术对话片段 23 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月10日，我的量化日记第七季打卡第四天

GLB的回测是真慢啊，一天跑不满1万


---

### 技术对话片段 24 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月11日，我的量化日记第七季打卡第五天

GLB这个回测真是一言难尽。今天竟然搞出个PC1.0的，哭笑不得


---

### 技术对话片段 25 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月11日，我的量化日记第七季打卡第六天

暴力回测的路不好走了，得泡论坛学习大佬们分享的AI经验


---

### 技术对话片段 26 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月13日，我的量化日记第七季打卡第七天

翻垃圾桶的一天，差点断粮


---

### 技术对话片段 27 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月14日，我的量化日记第七季打卡第八天

数据集吃不透真是要走很多弯路！


---

### 技术对话片段 28 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月15日，我的量化日记第七季打卡第九天

回测数是又降了吗？降到7500了？


---

### 技术对话片段 29 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月15日，我的量化日记第七季打卡第九天

试了试用AI优化因子，结果不太理想，还要好好研究


---

### 技术对话片段 30 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月20日 我的量化日记第九季 第一天久违的日记终于回来了。最近AI相关又开始井喷了，试了试Skill，AI好像比之前聪明了一点。


---

### 技术对话片段 31 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月21日 我的量化日记第九季 第二天平台更新了IS，想翻垃圾桶得再重新跑一遍了，炸裂……


---

### 技术对话片段 32 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月22日 我的量化日记第九季 第三天现在的PPA主题，给的GLB的几个数据集是真难搞……


---

### 技术对话片段 33 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月23日 我的量化日记第九季 第四天GLB这个回测速度，5000回测跑不完，火力全开也跑不完


---

### 技术对话片段 34 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月24日 我的量化日记第九季 第五天GLB的Returns好低啊，每天交1个吃低保


---

### 技术对话片段 35 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月25日 我的量化日记第九季 第六天是免费的大模型不给力，还是我使用的方法不对？AI总是编的头头是道，但结果并不好。


---

### 技术对话片段 36 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月26日 我的量化日记第九季 第七天GLB地区news20这个数据集真难跑，想趁着PPA主题点塔都费劲


---

### 技术对话片段 37 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月27日 我的量化日记第九季 第八天GLB地区的PPA主题实在跑不动了，不知道下次PPA会是哪个区


---

### 技术对话片段 38 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月28日 我的量化日记第九季 第九天AI比赛还没有参加，不知道从哪下手，希望晚上的会议能有所启发


---

### 技术对话片段 39 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月29日 我的量化日记第九季 第十天参加了AI比赛的培训会，有了点头绪，感恩老师的讲解


---

### 技术对话片段 40 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月30日 我的量化日记第九季 第十一天GLB地区的PPA主题活动马上结束，才点了3个塔，难受。不知道下一期的主题会是哪个地区。


---

### 技术对话片段 41 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月31日 我的量化日记第九季 第十二天新的PPA主题竟然又是GLB地区的，好消息是这次不限某几个数据集了？坏消息是universe限定为TOPDIV3000了。


---

### 技术对话片段 42 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年2月1日 我的量化日记第九季 第十三天workday账单出来了，马上要见钱了，蚊子腿再细也是肉，不容易


---

### 技术对话片段 43 (原帖: 【日常生活贴】我的量化日记第九季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第九季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年2月2日 我的量化日记第九季 第十四天这次的PPA主题限定GLB地区的universe为TOPDIV3000，好像比之前限定数据集稍微简单点，希望能多点几个塔


---

### 技术对话片段 44 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月20日 我的量化日记第九季 第一天

久违的日记终于回来了。最近AI相关又开始井喷了，试了试Skill，AI好像比之前聪明了一点。


---

### 技术对话片段 45 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月21日 我的量化日记第九季 第二天

平台更新了IS，想翻垃圾桶得再重新跑一遍了，炸裂……


---

### 技术对话片段 46 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月22日 我的量化日记第九季 第三天

现在的PPA主题，给的GLB的几个数据集是真难搞……


---

### 技术对话片段 47 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月23日 我的量化日记第九季 第四天

GLB这个回测速度，5000回测跑不完，火力全开也跑不完


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月24日 我的量化日记第九季 第五天

GLB的Returns好低啊，每天交1个吃低保


---

### 技术对话片段 49 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月25日 我的量化日记第九季 第六天

是免费的大模型不给力，还是我使用的方法不对？AI总是编的头头是道，但结果并不好。


---

### 技术对话片段 50 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月26日 我的量化日记第九季 第七天

GLB地区news20这个数据集真难跑，想趁着PPA主题点塔都费劲


---

### 技术对话片段 51 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月27日 我的量化日记第九季 第八天

GLB地区的PPA主题实在跑不动了，不知道下次PPA会是哪个区


---

### 技术对话片段 52 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月28日 我的量化日记第九季 第九天

AI比赛还没有参加，不知道从哪下手，希望晚上的会议能有所启发


---

### 技术对话片段 53 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月29日 我的量化日记第九季 第十天

参加了AI比赛的培训会，有了点头绪，感恩老师的讲解


---

### 技术对话片段 54 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月30日 我的量化日记第九季 第十一天

GLB地区的PPA主题活动马上结束，才点了3个塔，难受。不知道下一期的主题会是哪个地区。


---

### 技术对话片段 55 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年1月31日 我的量化日记第九季 第十二天

新的PPA主题竟然又是GLB地区的，好消息是这次不限某几个数据集了？坏消息是universe限定为TOPDIV3000了。


---

### 技术对话片段 56 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年2月1日 我的量化日记第九季 第十三天

workday账单出来了，马上要见钱了，蚊子腿再细也是肉，不容易


---

### 技术对话片段 57 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2026年2月2日 我的量化日记第九季 第十四天

这次的PPA主题限定GLB地区的universe为TOPDIV3000，好像比之前限定数据集稍微简单点，希望能多点几个塔


---

### 技术对话片段 58 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月122日，我的量化日记第八季打卡第1天

终于又有日记可写了，论坛是真热闹，学不过来，完全学不过来。


---

### 技术对话片段 59 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月23日，我的量化日记第八季打卡第2天

AI相关井喷式的爆发了，5000回测不会AI真可能被淘汰


---

### 技术对话片段 60 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月24日，我的量化日记第八季打卡第3天

今天开始EUR。5000回测不耐用啊。。。


---

### 技术对话片段 61 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月25日，我的量化日记第八季打卡第4天

参加了主题会，感谢老师的付出与分享


---

### 技术对话片段 62 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月26日，我的量化日记第八季打卡第5天

各种AI工具只是提高研究效率，不能无中生有。加油！


---

### 技术对话片段 63 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
2025年12月27日，我的量化日记第八季打卡第6天

让心流用MCP读取指定数据集的数据字段，它竟然只能读50个……


---

### 技术对话片段 64 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十一季 3月19日第一天

终于又开日记了，前两季都满的好快。。。最近渗透分频繁谷底，难受


---

### 技术对话片段 65 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十一季 3月20日第二天

最近在点JPN地区的塔，想着用FAST中性化，多少能出点PPA，出是出了，指标有点难看……


---

### 技术对话片段 66 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十一季 3月21日第三天

渗透分连续三次更新在0.3左右徘徊，得调整调整了，不然这日base没眼看


---

### 技术对话片段 67 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月3日 第一天久违的日记终于又来了。没出正月还是年，给大家拜个晚年，祝大家VF高高，收入多多。


---

### 技术对话片段 68 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月4日 第二天最近一直在跟着PPA主题走，EUR-D1-TOPCS1600点了几个塔，现在有个很闹心的问题，这个宇宙的提交太慢了，半小时起步


---

### 技术对话片段 69 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月5日 第三天继续死磕EUR主题，现在的base受渗透分的影响挺大的。还没摸索出稳定打分的思路，继续努力。


---

### 技术对话片段 70 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月6日 第四天最近在用TRAE进行一些优化工作，水平忽高忽低，有时候真会让人血压飙升


---

### 技术对话片段 71 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月7日 第五天参加了AI工具助您研究顺利的培训，cnhkmcp竟然又又又更新了，要进入一键生成可提交的Alpha的时代了？


---

### 技术对话片段 72 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月8日 第六天试用了下最新版的cnhkmcp中的Alpha自动流水线功能，随变调了个数据集，结果并不很理想，得再琢磨琢磨


---

### 技术对话片段 73 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。往期（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第六季+【日常生活贴】我的量化日记第七季+【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第十季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月9日 第七天这次Osmosis刷新总算是往上走了点，周一的刷一次管三天，太重要了。Combined Performance也快刷了吧，希望能有个好结果。


---

### 技术对话片段 74 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月3日 第一天

久违的日记终于又来了。没出正月还是年，给大家拜个晚年，祝大家VF高高，收入多多。


---

### 技术对话片段 75 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月4日 第二天

最近一直在跟着PPA主题走，EUR-D1-TOPCS1600点了几个塔，现在有个很闹心的问题，这个宇宙的提交太慢了，半小时起步


---

### 技术对话片段 76 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 QL47372 (Rank 36) 的解答与建议**:
我的量化日记第十季 2026年3月5日 第三天

继续死磕EUR主题，现在的base受渗透分的影响挺大的。还没摸索出稳定打分的思路，继续努力。


---

### 技术对话片段 77 (原帖: 利用Gemini从0到1手搓IND区alpha尝试经验分享)
- **原帖链接**: [Commented] 利用Gemini从0到1手搓IND区alpha尝试经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (JX84394)**:
## 以imbalance5数据集为例

该数据集有imb5_mktcap和imb5_score两个字段，先用Gemini解读下


> [!NOTE] [图片 OCR 识别内容]
> Gemini
> 解释 Fworldquant brain这两个字段imb5_mktcap和
> imb5_score,
> 他属于Oil Price Resilience Scores数据集
> Show thinking
> 从你在WorldQuant BRAIN平台上查看的0i1 Price Resilience Scores (油价韧性评
> 分)  数据集页面来看。这两个字段的具体含义如下:
> 1.
> imb5
> mktcap
> (Market Cap)
> 含义:  代表市值 (Market Capitalization)c
> 用途:  这是量化交易中最基础的数据之一。通常指公司当前的总股票价值
> (股价 x总股本)c
> 在构建Alpha因子时。这个字段非常重要。主要用于:
> 中性化 (Neutralization): 消除因子对市值的偏露 (例如。确保你的策
> 略不仅仅是买入大盘股。卖出小盘股)c
> 权重分配:  在组合构建中根据市值大小分配权重。
> 筛选:  过滤掉市值过小的流动性差的股票。
> Current tab
> Jsk Gemini
> Thinking
  
> [!NOTE] [图片 OCR 识别内容]
> 2.
> ib5_score
> (SHIELD OIL Composite Score)
> 含义:  这是该数据集的核心字段。即SHIELD油价韧性综合评分。
> 数值范围: 0到1。
> 解读:
> 该评分旨在衡量一家公司的股价在面对石油价格波动时的"韧性"或承受
> 能力。
> 接近 1(高分):  通常表示该公司的股价对油价的剧烈波动具有较强的抵
> 抗力。或者其业务模式受油价冲击的影响较小 (表现出高韧性)c
> 接近 0 (低分):  表示该公司对油价波动较为敏感。或者在油价不稳定时
> 容易受到负面影响 (表现出低韧性)。
> 数据来源:  描述中提到的 "SHIELD" 很可能是指提供该数据的第三方供应商或
> 特定算法模型的名称。
> 数据集背景信息 (供参考)
> 覆盖范围 (Region): IND (印度市场)。
> 股票池 (Universe): TOP5OO (市值前500的股票)。
> 延迟 (Delay): 1 (数据有1天的延迟。意味着你在T8只能看到T-1曰的数据,这
> 是回测中防止"未来函数"的关键)。
> 建议下-步:
> 如果你打算使用
> imb5_score
> 构建Alpha, 建议先测试它与特定行业
> (如能源。运输) 的相关性。或者直接将其作为风险控制因子。做多"高韧性"股票
> 并做空"低韧性"股票来对冲油价风险。


得出基本信息imb5_score可以作为主信号，先回测试试，初始设置我习惯设置decay=2，truncation=0.08，neutralization=SECTOR

回测结果如下：


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> Competitions (4)
> 三
> Simulation
> Simulation 2
> Simulation 3
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIA
> Settings
> IND/D1ITOP500
> Convert to Multi-Simulation
> Chart
> Pnl
> Streak: 45
> 1
> imbs_score
> 1OM
> 5,OOOK
> 2015
> 2017
> 2019
> 2021
> 2023
> Ct31
> day



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 8 PASS
> Sharpe Of 2.95 is above CUtOff of 1.58
> Fitness of 3.20 is above cutoff of 1.
> Turnoverof 13.409 is above cutoff of 1 %.
> Turnover of 13.409 is below cutoff of 40%.
> Sub-universe Sharpe Of 1.42 is above cUtOff Of 0.87.
> 2year
> Sharpe of 1.72 is above cutoff Of 1.58。
> Pyramid theme IND/DIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the following multipliers: IND Region Theme
> 
> 2;
> INDIDIIIMBALANCE Pyramid Theme
> 
> 1. The final theme multiplieris 2。
> 2 FAIL
> Weight is too strongly concentrated or too few instruments are assigned weight。
> Robust universe
> Sharpe of 0.83 is below CUtoff of 1


有两个FAIL项，继续向Gemini提问

```
该alpha回测后IS指标有两个fail项，请帮我解释下这两个FAIL是什么意思，并分析造成这两个FAIL可能得原因有哪些，并给出改进建议，只能使用页面中提供的操作符。
```

下面是Gemini给出的回答


> [!NOTE] [图片 OCR 识别内容]
> 1. FAIL: Weight is too strongly concentrated or too few
> instruments are assigned weight
> 含义:
> 权重过于集中,或者被分配权重的股票数量太少。
> 简单来说:  你的策略要么是把大部分资金押注在极少数几只股票上 (风险太大) ,
> 要么是整个股票池里只有很少的股票有分数 (覆盖率太低)c
> 可能原因:
> 数据覆盖率不足:
> imb5
> SCOre
> 是关于"油价韧性"的数据。可能只有能源相关或特
> 定行业的股票才有这个数据。其他股票可能是
> NaN
> (空值)。
> 如果只有几十只股票
> 有数值。就会导致此项失败。
> 数值差异极大:  如果原始分数
> imb5
> SCOre
> 的分布很不均匀 (例如某些股票是
> 0.9,大多数是0.01) ,系统分配权重时会过度向高分股票倾斜。
> 末进行标准化:  直接使用原始数据作为Alpha信号,会导致数值大的股票权重极
> 大。
> 改进建议 (操作符):
> 使用
> rank()
> 或
> Zscore()
> 强制将分数分布均匀化。
> 尝试:
> rank (imb5
> SCore)
> 解释:
> rank
> 会将所有有数据的股票按排名分配0到1之间的数值。这样可
> 以保证更多的股票被分配到合理的权重。而不是集中在数值最大的那几个。
> 使用
> ts_rank()
> 如果横截面数据太少,可以尝试时间序列排名,看该股票当前
> 介粼讨夫段时间相对仿署_



> [!NOTE] [图片 OCR 识别内容]
> 2. FAIL: Robust universe Sharpe of 0.83 is below cutoff of 1
> 含义:
> 稳健股票池
> (Robust Universe) 的夏普比率低于1。
> 简单来说:  平台不仅在 Top5o0 (主要股票池)  上测试你的策略,还在一个被称
> 为"稳健池" (通常是流动性稍差或更具代表性的子集)
> 上测试。你的策略在主测试
> 中表现很好(2.95),但在稳健池中表现很差(0.83),说明你的策略不稳定。可能
> 只在特定的某些大盘股上有效。或者只是捕捉了某种市场风格 (Beta) 而非真正的
> Alpha。
> 可能原因:
> 风格1行业偏露:
> imb5
> SCOFe
> 可能本质上是在做一个"做多能源股"的策略。如果
> 油价上涨。所有高分股票都涨。但这可能只是行业Beta, 而不是Alpha。 稳健性测
> 试通常会惩罚这种单纯的行业贝塔。
> 缺乏中性化:  没有剔除市场或行业的影响。
> 改进建议 (操作符):
> 行业中性化
> group_neutralize
> 尝试:
> group_neutralize
> imb5_score ,
> group )
> 或
> group_neutralize(rank
> imb5_score )
> group)
> 解释:
> 这会消除行业板块的影响。
> 比如。它会让你在能源板块内部买入"韧性
> 最高"的。卖出"韧性最低"的,而不是买入整个能源板块。这通常能大幅提高
> Robust Sharpe。
> 行业内摊名
> group_
> rank
> 尝试:
> GroUD
> rank
> imb5
> SCOre
> aroun )


思考：根据AI的建议对数据进行回填,为什么不使用ai建议的rank等数据标准化操作因为我认为原始数据已经是0-1范围了所以没必要进行rank或zscore，当然有兴趣的可以自己尝试下，经过回填几轮迭代效果如下，成功解决了weight问题：


> [!NOTE] [图片 OCR 识别内容]
> (C@
> 1C10
> (
> PASS
> Settings
> IND/D1/T0P500
> Convert to Multi-Simulation
> Sharpe of 2.96 is above CUtoff of 1.58
> Streak: 45
> Fitness of 3.28 is above cUtoff of 1.
> 1
> ts
> backfill
> imb5_
> SCOre
> 20
> Turnoverof 12.849 is above cUtoff of 19
> Turnover of 12.849 is below cUtoff of 40%.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 1.39 is above CUtOff Of 0.87.
> 2year Sharpe of 1.66 is above Cutoff Of 1.58.
> Pyramid theme INDIDIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the following multipliers: IND Region Theme - 2;
> INDIDIIIMBALANCE Pyramid Theme
> 
> 1. The final theme multiplieris 2.
> FAIL
> Robust universe
> Sharpe of 0.81 is below CUtoff of 1
> WARNING
> PENDING
> day


第二个问题根据AI建议先试试行业中性化：


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> Competitions (4)
> Simulation
> Simulation 2
> Simulation 3
> CODE
> RESULTS
> LEARN
> DATA
> TUTORI
> PASS
> Settings
> IND/D1/T0P500
> Convert to Multi-Simulation
> Sharpe Of 3.06 is above CUtOff of 1.58
> Streak: 45
> Fitness of 3.23is above cutoff of 1.
> 1
> Broup_
> neutralize
> ts_backfill
> imb5_
> SCore,20) ,
> industry)
> Turnoverof 13.839 is above cUtoff of 1%.
> Turnover of 13.839 is below cUtoff of 40%.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 1.41 is above cutoff Of 0.9.
> 2 year Sharpe Of 2.02 is above cUtOff Of 1.58.
> Pyramid theme INDIDIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the following multipliers: IND Region Theme - 2;
> INDIDIIIMBALANCE Pyramid Theme
> 1. The final theme multiplieris 2.
> FAIL
> Robust universe
> Sharpe of 0.98 is below CUtoff of 1
> WARNING
> PENDING
> day


效果还是挺好的，差一点就能提交了，最后进行参数微调就可以得到最终可以提交的alpha，最终结果如下：


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> IND
> TOPSOO
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Sector
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> On
> YEARS
> MONTHS
> MAX TRADE
> Off
> Save as Default
> Apply



> [!NOTE] [图片 OCR 识别内容]
> Simulation 1
> Simulation 2
> Simulation 3
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> IND/D1/T0P500
> Convert to Multi-Simulation
> IS Testing Status
> N
> Streak: 45
> 1 |
> Broup_
> neutralize
> rank(ts_backfill(imbs
> SCOre,
> 20)), industry
> 10 PASS
> Sharpe of 3.18 is above cUtOff of 1.58。
> Fitness of 2.94is above cUtoff of 1.
> Turnoverof 18.749 is above cUtoff of 19
> Turnover of 18.749 is below cutoff of 40%.
> Weight is well distributed over instruments。
> Sub-Universe
> Sharpe Of 1.45 is above CUtOff of 0.94。
> Robust universe Sharpe Of 1.03 is above CUtOff of 1.
> 2year
> Sharpe of 2.2is above cutoff of 1.58.
> Pyramid theme INDIDIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the
> following multipliers: IND Region Theme
> 
> 2;
> INDIDIIIMBALANCE Pyramid Theme
> 1. The final theme multiplieris 2.
> WARNING
> 291[C
> 十T
> 00C
> NOC
> H十
> I十
> day


最后总结：

1、本人菜鸟一枚；

2、AI时代希望与大家一起成为那个被AI需要的人，而不是被AI替代的人；

3、本人菜鸟一枚希望大家轻点，也希望以后有更多的想法可以一起分享，共同进步。

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢分享。IND区开活动了，学习下


---

### 技术对话片段 78 (原帖: 利用Gemini从0到1手搓IND区alpha尝试经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 利用Gemini从0到1手搓IND区alpha尝试经验分享_36444272754711.md
- **时间**: 6个月前

**提问/主帖背景 (JX84394)**:
## 以imbalance5数据集为例

该数据集有imb5_mktcap和imb5_score两个字段，先用Gemini解读下


> [!NOTE] [图片 OCR 识别内容]
> Gemini
> 解释 Fworldquant brain这两个字段imb5_mktcap和
> imb5_score,
> 他属于Oil Price Resilience Scores数据集
> Show thinking
> 从你在WorldQuant BRAIN平台上查看的0i1 Price Resilience Scores (油价韧性评
> 分)  数据集页面来看。这两个字段的具体含义如下:
> 1.
> imb5
> mktcap
> (Market Cap)
> 含义:  代表市值 (Market Capitalization)c
> 用途:  这是量化交易中最基础的数据之一。通常指公司当前的总股票价值
> (股价 x总股本)c
> 在构建Alpha因子时。这个字段非常重要。主要用于:
> 中性化 (Neutralization): 消除因子对市值的偏露 (例如。确保你的策
> 略不仅仅是买入大盘股。卖出小盘股)c
> 权重分配:  在组合构建中根据市值大小分配权重。
> 筛选:  过滤掉市值过小的流动性差的股票。
> Current tab
> Jsk Gemini
> Thinking
  
> [!NOTE] [图片 OCR 识别内容]
> 2.
> ib5_score
> (SHIELD OIL Composite Score)
> 含义:  这是该数据集的核心字段。即SHIELD油价韧性综合评分。
> 数值范围: 0到1。
> 解读:
> 该评分旨在衡量一家公司的股价在面对石油价格波动时的"韧性"或承受
> 能力。
> 接近 1(高分):  通常表示该公司的股价对油价的剧烈波动具有较强的抵
> 抗力。或者其业务模式受油价冲击的影响较小 (表现出高韧性)c
> 接近 0 (低分):  表示该公司对油价波动较为敏感。或者在油价不稳定时
> 容易受到负面影响 (表现出低韧性)。
> 数据来源:  描述中提到的 "SHIELD" 很可能是指提供该数据的第三方供应商或
> 特定算法模型的名称。
> 数据集背景信息 (供参考)
> 覆盖范围 (Region): IND (印度市场)。
> 股票池 (Universe): TOP5OO (市值前500的股票)。
> 延迟 (Delay): 1 (数据有1天的延迟。意味着你在T8只能看到T-1曰的数据,这
> 是回测中防止"未来函数"的关键)。
> 建议下-步:
> 如果你打算使用
> imb5_score
> 构建Alpha, 建议先测试它与特定行业
> (如能源。运输) 的相关性。或者直接将其作为风险控制因子。做多"高韧性"股票
> 并做空"低韧性"股票来对冲油价风险。


得出基本信息imb5_score可以作为主信号，先回测试试，初始设置我习惯设置decay=2，truncation=0.08，neutralization=SECTOR

回测结果如下：


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> Competitions (4)
> 三
> Simulation
> Simulation 2
> Simulation 3
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIA
> Settings
> IND/D1ITOP500
> Convert to Multi-Simulation
> Chart
> Pnl
> Streak: 45
> 1
> imbs_score
> 1OM
> 5,OOOK
> 2015
> 2017
> 2019
> 2021
> 2023
> Ct31
> day



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 8 PASS
> Sharpe Of 2.95 is above CUtOff of 1.58
> Fitness of 3.20 is above cutoff of 1.
> Turnoverof 13.409 is above cutoff of 1 %.
> Turnover of 13.409 is below cutoff of 40%.
> Sub-universe Sharpe Of 1.42 is above cUtOff Of 0.87.
> 2year
> Sharpe of 1.72 is above cutoff Of 1.58。
> Pyramid theme IND/DIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the following multipliers: IND Region Theme
> 
> 2;
> INDIDIIIMBALANCE Pyramid Theme
> 
> 1. The final theme multiplieris 2。
> 2 FAIL
> Weight is too strongly concentrated or too few instruments are assigned weight。
> Robust universe
> Sharpe of 0.83 is below CUtoff of 1


有两个FAIL项，继续向Gemini提问

```
该alpha回测后IS指标有两个fail项，请帮我解释下这两个FAIL是什么意思，并分析造成这两个FAIL可能得原因有哪些，并给出改进建议，只能使用页面中提供的操作符。
```

下面是Gemini给出的回答


> [!NOTE] [图片 OCR 识别内容]
> 1. FAIL: Weight is too strongly concentrated or too few
> instruments are assigned weight
> 含义:
> 权重过于集中,或者被分配权重的股票数量太少。
> 简单来说:  你的策略要么是把大部分资金押注在极少数几只股票上 (风险太大) ,
> 要么是整个股票池里只有很少的股票有分数 (覆盖率太低)c
> 可能原因:
> 数据覆盖率不足:
> imb5
> SCOre
> 是关于"油价韧性"的数据。可能只有能源相关或特
> 定行业的股票才有这个数据。其他股票可能是
> NaN
> (空值)。
> 如果只有几十只股票
> 有数值。就会导致此项失败。
> 数值差异极大:  如果原始分数
> imb5
> SCOre
> 的分布很不均匀 (例如某些股票是
> 0.9,大多数是0.01) ,系统分配权重时会过度向高分股票倾斜。
> 末进行标准化:  直接使用原始数据作为Alpha信号,会导致数值大的股票权重极
> 大。
> 改进建议 (操作符):
> 使用
> rank()
> 或
> Zscore()
> 强制将分数分布均匀化。
> 尝试:
> rank (imb5
> SCore)
> 解释:
> rank
> 会将所有有数据的股票按排名分配0到1之间的数值。这样可
> 以保证更多的股票被分配到合理的权重。而不是集中在数值最大的那几个。
> 使用
> ts_rank()
> 如果横截面数据太少,可以尝试时间序列排名,看该股票当前
> 介粼讨夫段时间相对仿署_



> [!NOTE] [图片 OCR 识别内容]
> 2. FAIL: Robust universe Sharpe of 0.83 is below cutoff of 1
> 含义:
> 稳健股票池
> (Robust Universe) 的夏普比率低于1。
> 简单来说:  平台不仅在 Top5o0 (主要股票池)  上测试你的策略,还在一个被称
> 为"稳健池" (通常是流动性稍差或更具代表性的子集)
> 上测试。你的策略在主测试
> 中表现很好(2.95),但在稳健池中表现很差(0.83),说明你的策略不稳定。可能
> 只在特定的某些大盘股上有效。或者只是捕捉了某种市场风格 (Beta) 而非真正的
> Alpha。
> 可能原因:
> 风格1行业偏露:
> imb5
> SCOFe
> 可能本质上是在做一个"做多能源股"的策略。如果
> 油价上涨。所有高分股票都涨。但这可能只是行业Beta, 而不是Alpha。 稳健性测
> 试通常会惩罚这种单纯的行业贝塔。
> 缺乏中性化:  没有剔除市场或行业的影响。
> 改进建议 (操作符):
> 行业中性化
> group_neutralize
> 尝试:
> group_neutralize
> imb5_score ,
> group )
> 或
> group_neutralize(rank
> imb5_score )
> group)
> 解释:
> 这会消除行业板块的影响。
> 比如。它会让你在能源板块内部买入"韧性
> 最高"的。卖出"韧性最低"的,而不是买入整个能源板块。这通常能大幅提高
> Robust Sharpe。
> 行业内摊名
> group_
> rank
> 尝试:
> GroUD
> rank
> imb5
> SCOre
> aroun )


思考：根据AI的建议对数据进行回填,为什么不使用ai建议的rank等数据标准化操作因为我认为原始数据已经是0-1范围了所以没必要进行rank或zscore，当然有兴趣的可以自己尝试下，经过回填几轮迭代效果如下，成功解决了weight问题：


> [!NOTE] [图片 OCR 识别内容]
> (C@
> 1C10
> (
> PASS
> Settings
> IND/D1/T0P500
> Convert to Multi-Simulation
> Sharpe of 2.96 is above CUtoff of 1.58
> Streak: 45
> Fitness of 3.28 is above cUtoff of 1.
> 1
> ts
> backfill
> imb5_
> SCOre
> 20
> Turnoverof 12.849 is above cUtoff of 19
> Turnover of 12.849 is below cUtoff of 40%.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 1.39 is above CUtOff Of 0.87.
> 2year Sharpe of 1.66 is above Cutoff Of 1.58.
> Pyramid theme INDIDIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the following multipliers: IND Region Theme - 2;
> INDIDIIIMBALANCE Pyramid Theme
> 
> 1. The final theme multiplieris 2.
> FAIL
> Robust universe
> Sharpe of 0.81 is below CUtoff of 1
> WARNING
> PENDING
> day


第二个问题根据AI建议先试试行业中性化：


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> Competitions (4)
> Simulation
> Simulation 2
> Simulation 3
> CODE
> RESULTS
> LEARN
> DATA
> TUTORI
> PASS
> Settings
> IND/D1/T0P500
> Convert to Multi-Simulation
> Sharpe Of 3.06 is above CUtOff of 1.58
> Streak: 45
> Fitness of 3.23is above cutoff of 1.
> 1
> Broup_
> neutralize
> ts_backfill
> imb5_
> SCore,20) ,
> industry)
> Turnoverof 13.839 is above cUtoff of 1%.
> Turnover of 13.839 is below cUtoff of 40%.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 1.41 is above cutoff Of 0.9.
> 2 year Sharpe Of 2.02 is above cUtOff Of 1.58.
> Pyramid theme INDIDIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the following multipliers: IND Region Theme - 2;
> INDIDIIIMBALANCE Pyramid Theme
> 1. The final theme multiplieris 2.
> FAIL
> Robust universe
> Sharpe of 0.98 is below CUtoff of 1
> WARNING
> PENDING
> day


效果还是挺好的，差一点就能提交了，最后进行参数微调就可以得到最终可以提交的alpha，最终结果如下：


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> IND
> TOPSOO
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Sector
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> On
> YEARS
> MONTHS
> MAX TRADE
> Off
> Save as Default
> Apply



> [!NOTE] [图片 OCR 识别内容]
> Simulation 1
> Simulation 2
> Simulation 3
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> IND/D1/T0P500
> Convert to Multi-Simulation
> IS Testing Status
> N
> Streak: 45
> 1 |
> Broup_
> neutralize
> rank(ts_backfill(imbs
> SCOre,
> 20)), industry
> 10 PASS
> Sharpe of 3.18 is above cUtOff of 1.58。
> Fitness of 2.94is above cUtoff of 1.
> Turnoverof 18.749 is above cUtoff of 19
> Turnover of 18.749 is below cutoff of 40%.
> Weight is well distributed over instruments。
> Sub-Universe
> Sharpe Of 1.45 is above CUtOff of 0.94。
> Robust universe Sharpe Of 1.03 is above CUtOff of 1.
> 2year
> Sharpe of 2.2is above cutoff of 1.58.
> Pyramid theme INDIDIIIMBALANCE matches with multiplier of 1. Effective pyramid
> count for Geniusis 1
> These themes match with the
> following multipliers: IND Region Theme
> 
> 2;
> INDIDIIIMBALANCE Pyramid Theme
> 1. The final theme multiplieris 2.
> WARNING
> 291[C
> 十T
> 00C
> NOC
> H十
> I十
> day


最后总结：

1、本人菜鸟一枚；

2、AI时代希望与大家一起成为那个被AI需要的人，而不是被AI替代的人；

3、本人菜鸟一枚希望大家轻点，也希望以后有更多的想法可以一起分享，共同进步。

**顾问 QL47372 (Rank 36) 的解答与建议**:
感谢分享。IND区开活动了，学习下


---
