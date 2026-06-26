# 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **作者**: 顾问 ML47973 (Rank 100)
- **发布时间/热度**: 9个月前, 得票: 125

## 帖子正文


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

---

## 讨论与评论 (60)

### 评论 #1 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

帖子内容是我的一些个人浅见/拙见和在一些大佬(比如：游戏王)那儿学习到的知识，我自己可能没察觉哪里没说清楚或者有错误，拜托各位小伙伴一起检查一下啦！

诚邀各位大佬和uu们不吝赐教，若发现有误或是有更好的想法，有任何想法都欢迎在评论区拍砖或种草，大家一起学习一起进步！

---

### 评论 #2 (作者: AK76468, 时间: 9个月前)

============================================================

天呐，大佬的回测产出效率也太高，不到15w次回测竟然产出了266+个信号，真的是让人惊讶！
我看了你的点塔方法，感觉是给强信号增加噪音的方式，将塔字段引入该信号，我认为应该算是混信号。但又看了你十分高的combined，似乎又不一定是混信号，就这一点你怎么看呢？另外您是否会在提交前详细了解alpha表达式的经济学含义呢？
提前预祝大佬Gold直升GM！！！
============================================================

---

### 评论 #3 (作者: JL67084, 时间: 9个月前)

非常感谢大佬的分享，字字如珠，细节满分，期待part2

---

### 评论 #4 (作者: 顾问 RM49262 (Rank 30), 时间: 9个月前)

=====================================评论区=========================================

感谢大佬分享，通过add点塔这个小技巧倒是真的学到了

不过发现自己两个per的数据都是大佬的一倍，作为gold感觉冲expert是有点艰难了

===================================================================================

---

### 评论 #5 (作者: HS89714, 时间: 9个月前)

这个太棒了，及时雨啊，像我这种gold，操作符数量真是非常吃亏，目前还有hump（x,hump=0.01）还没找到合适的alpha可以提交，再就是逻辑操作符能不能给点思路？大佬

---

### 评论 #6 (作者: QZ28759, 时间: 9个月前)

这是一篇能大幅度提升国区点塔效率帖子，作者太强了，佩服的五体投地，我再读多几遍~~~

---

### 评论 #7 (作者: JW89289, 时间: 9个月前)

太干了，啥都抖落出来了，学到新东西了

**我学会了，赶紧删帖**

---

### 评论 #8 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

通过以上的操作，如果有一些上进思进取的consultant还是无法找出alpha，还有最后一条邪修之路，不一定有效还需多尝试，不建议且请谨慎使用.

       把你跑过的alpha，区分大区和Delay，找出phl趋势相同或者补齐(充好)的alpha，就两两组合吧，其中universe和decay等等不同的话，自己思考下怎么组合，组合出几个alpha还是一个你自己的想法实践，一般来说使用乘法、加法和减法，有时效果会非常好，sharpe和fitness会激增，且相似度会低；有时相似度会更高且sharpe和fitness下降的情况发生. 手动组一下就好了，不用写程序，毕竟有些邪修的感觉

       不建议且谨慎使用的原因是 和组superalpha有些冲突，superalpha的组合方式我以为是单纯的把每个要组合的alpha按照纯数字权重进行组合，不了解superalpha是怎么组的可以看看这个 What is a SuperAlpha?
 [https://platform.worldquantbrain.com/learn/documentation/superalpha/superalpha-overview](https://platform.worldquantbrain.com/learn/documentation/superalpha/superalpha-overview) 

        希望对你有帮助，自己通过组合两两alpha的操作类似于组superalpha的低低低低低低低配版，多多少少(猜测，影响不会很大)会对自己后期组superalpha有影响 .

---

### 评论 #9 (作者: SZ24058, 时间: 9个月前)

===================================================================

感谢大佬的分享，解决了我一直以来对于op计数方式的困惑，我也经常使用四则运算，搞了半天原来也是要算 在op数量里的QAQ。同时点塔的想法很有启发，点赞！👍

===================================================================

---

### 评论 #10 (作者: DS48533, 时间: 9个月前)

金字塔是本人的么，这也太强了。提到的案例，用了很多字段想加，长见识了，主要是结果竟然特别好

---

### 评论 #11 (作者: 顾问 WX64154 (Rank 32), 时间: 9个月前)

感谢大佬分享。给我深深上了一课，期待下节。

想知道大佬怎么把combine刷的那么高

---

### 评论 #12 (作者: 顾问 SC23342 (Rank 23), 时间: 9个月前)

我也有过很多类似的心路历程，以为四则运算不会计入运算符数量，点塔时要各方面兼顾，少用符号多用字段，而且还要用乘数接近的才行……在iqc阶段我就已经在用自造的函数和数学运算来创造更多新的字段和表达式，就像在广袤无垠的总宇宙中，自己划定了一个小宇宙，然后在这当中持续进行挖掘。虽然文中提到的部分思路我也曾经探索过，但在几次提交后就没有进一步的探索了，只是浅尝辄止。感谢这篇文章让我意识到了目前的思路还是有较大的局限性，应该在已有的基础上继续做更多的扩展和新的探索方向

---

### 评论 #13 (作者: SZ20589, 时间: 9个月前)

“使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .”

大佬太厉害了，说得太好了。看了帖子真佩服大佬有这么多奇思妙想，我正发觉我的operators数使用提高不了，看了大佬的帖子，我觉得我又行了，下个季度再发力。真心祝福大佬次次GM，多发总结贴给我这种小虾米带带福利。

===========================================

---

### 评论 #14 (作者: YP44571, 时间: 9个月前)

非常对胃口的帖子，正是我这个阶段需要了解学习的知识，谢谢大佬的分享！获益匪浅！

---

### 评论 #15 (作者: FF56620, 时间: 9个月前)

好强的佬，回测数量竟然那么少，也就是说基本不用代码回测吗，这样直升gm，太厉害了

--------------------------------------

“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）

--------------------------------------

---

### 评论 #16 (作者: YQ51506, 时间: 9个月前)

很好的文章，给你点赞，加油！！对我系统完善帮助很大

---

### 评论 #17 (作者: WC77208, 时间: 9个月前)

没有停留在表面，而是深入探讨了容易被忽略的细节。例如，对操作符 `+` ,  `-` ,  `*` ,  `/` ,  `^` 和对应函数 `add` ,  `multiply` 等是否重复计数的验证，以及​ **​通过变量替换减少重复操作符来优化 `Operators per Alpha` ​** ​ 的方法，非常实用。这种“踩坑”后的经验分享尤其宝贵。从“使用模板”转向“创造字段”，鼓励充分发挥想象力和数学基础，​ **​将创造Alpha的过程视为一种具有经济学意义的探索​** ​，而不仅仅是机械的套用，这是更高层次的思维提升。

---

### 评论 #18 (作者: SQ89646, 时间: 9个月前)

感谢提供的思路 原先真没注意到运算符

---

### 评论 #19 (作者: YZ88594, 时间: 9个月前)

感谢大佬的帖子。对于如何降低平均操作符，简直是雪中送炭。观察大佬所构造的alpha，又给我提供了新的思路。

---

### 评论 #20 (作者: BL72197, 时间: 9个月前)

大佬好强，看完这篇帖子，打开了很多新的思路，谢谢

---

### 评论 #21 (作者: ZW42877, 时间: 9个月前)

大佬很有想法，思路很清晰，根据WQ的规则深挖WQ平台的各种功能，将自己的想法化为现实，诸如检测op的重复计数，变量代换等，并且有着极其敏锐的数学思维，将数学应用在因子发掘之中，研读这一帖子解答了很多疑惑。向您学习对WQ平台研究的思路，对op，fields以及相关参数研究的思路。期待大佬新帖！

---

### 评论 #22 (作者: YQ84572, 时间: 9个月前)

很好的文章，对脱离模板真正意义的去制造分析alpha很有帮助！

---

### 评论 #23 (作者: LL49894, 时间: 9个月前)

感谢大佬的无私分享，现在我才真正意识到 6 维能力的重要性，之前以为各项硬性指标达标就万事大吉，没多想背后的深层逻辑，才发现指标合格才是起点，6维的提升才是重点呀，真心期待大佬后续能分享更多实操经验，帮我们少走弯路，再次感谢！

祝日进斗金，VF1，weight天天涨

---

### 评论 #24 (作者: JM40377, 时间: 9个月前)

受益良多

---

### 评论 #25 (作者: LL61351, 时间: 9个月前)

一口气看完，非常好的文章，将六个维度及如何提升讲得非常清楚。我是个新手，因为RA比较难挖，想问一下RA和PPA在点塔过程中，会有差异不？

---

### 评论 #26 (作者: AH18340, 时间: 9个月前)

感谢大佬的分享，看到你在回测不高的情况下，确能交出这么多高质量的alpha,并且塔都点满了。看了你的alpha模版之后我看到了简单但是实用的idea。预祝大佬早日成为gm,vf1。

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #27 (作者: CW63908, 时间: 9个月前)

佬，看了你这篇详细分享，真是受益匪浅呀。感谢

---

### 评论 #28 (作者: ZH39644, 时间: 9个月前)

大佬的视角果然不一样，向你学习了！ 简单才是美，从研究字段，和基本数学运算开始。

感谢分享！

---

### 评论 #29 (作者: YH37288, 时间: 9个月前)

学习了，感谢大佬，期待下一期

---

### 评论 #30 (作者: LZ21262, 时间: 9个月前)

受益匪浅

---

### 评论 #31 (作者: 顾问 FX25214 (Rank 22), 时间: 9个月前)

我非常想请教楼主一个问题。对于直接跨数据集两个字段相加，如何避免混信号或者过拟合呢？这种直接加噪音的方式难道不会在样本外非常的危险吗？因为我自己点塔是基本上可以一天一个塔，我感觉单数据集也可以在一个允许的时间范围内很好的点塔，所以我比较好奇这样做的意义是什么？是因为提前用相同或者相似的运算符跑了不同的字段发现他们能捕捉相似的市场信息然后进行简单的加和来加强吗？

---

### 评论 #32 (作者: MH27590, 时间: 9个月前)

很受启发，非常感谢

---

### 评论 #33 (作者: HX55085, 时间: 9个月前)

大佬太强了，看得酣畅淋漓！！！

---

### 评论 #34 (作者: 顾问 LY85808 (Rank 86), 时间: 9个月前)

很有帮助，感谢分享！

---

### 评论 #35 (作者: 顾问 HP65370 (Rank 93), 时间: 9个月前)

感谢大佬的分享，我认真地看完了，文章的风格独特且美观，我也收获了很多，对于alpha的研究豁然开朗，有了不一样的见解，并且，此前一直没有想过用a=表达式1；表达式2（a)；这样也可以降操作符，突然感觉自己损失了很多；再者，对于在表达式中再加一个字段有时可以改良alpha的性能，以及我们可以自创数据字段，这些为我后面的研究带来了启迪性的作用

---

### 评论 #36 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

您的帖子写得太详细了。到了赛季末了，我用华子哥的插件看了自己排名，说实话对六维其实是一知半解，不知到具体怎么分析。感觉您的分享就是手把手教我这种小白。

---

### 评论 #37 (作者: XQ96410, 时间: 9个月前)

厉害，学到了好多，谢谢。

---

### 评论 #38 (作者: YZ64617, 时间: 9个月前)

@ [顾问 ML47973 (Rank 100)](/hc/en-us/profiles/29991129347991-顾问 ML47973 (Rank 100))  那个Header Basic *****，****部分是由你的email:pwd 编码生成的，是可逆的！建议迅速修改密码，且截图重新打水印。

---

### 评论 #39 (作者: LR93609, 时间: 9个月前)

感谢分享，确实有不少地方可圈可点

1. 混信号发挥到了极致，但不太推荐，至少方法要对；先rank再加和会不会好一点？或者说先归一化

2. 创造字段一说是否合适？两元、三元、四元组合是不是创造字段的意思？

```
 field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .
```

3. 没看懂放这个公式的意义？


> [!NOTE] [图片 OCR 识别内容]
> 看到这里。你还在想向我找寻310h3模板吗?  其实我没有模板
> 时间多的话可以再瞧
> -瞧上面的内容。看看
> 能不能绐到你一点点启发呢 _
> Va > 1,JN,{.t。
> lm
> Sol)- Srr
> lm
> falr) < I0
> O
> 川U


请帮忙回复，再次感谢分享

-----------------------------------------------------------------------------------------------------------------------------

凡事发生，皆利于我；愿我所愿，尽是美好

-----------------------------------------------------------------------------------------------------------------------------

---

### 评论 #40 (作者: JM85274, 时间: 9个月前)

谢谢大佬的分享，之前一直没有注重软指标，不小心断了回测，现在通过华子的插件进行排名预测发现影响还是很大的，之后会注意保持每日回测。但是Community activity最近一直在调，不知道是不是因为会议参加比较少的原因。

---

### 评论 #41 (作者: PL95083, 时间: 9个月前)

感谢大佬分享，十分有用

---

### 评论 #42 (作者: SM90987, 时间: 9个月前)

学到东西了，谢谢大佬

---

### 评论 #43 (作者: 顾问 JR23144 (Rank 6), 时间: 9个月前)

太强了， gold 直升 GM ，点塔的范围也让我深有启发，chn 也可以点这么多的哇，下个赛季我再来碰chn 吧，感谢大佬分享

=========================================================================================VF1.0===================================================================================

---

### 评论 #44 (作者: XC39347, 时间: 9个月前)

非常全面的分析了如何提高alpha的质量 学习了！！！

---

### 评论 #45 (作者: LH44620, 时间: 9个月前)

内容好丰富，也包含了很多“潜规则”小知识哈哈哈哈。

----------------------------------------------------加油----------------------------------------------------

---

### 评论 #46 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[YZ64617](/hc/en-us/profiles/4527497709335-YZ64617)

> @ [顾问 ML47973 (Rank 100)](/hc/en-us/profiles/29991129347991-顾问 ML47973 (Rank 100))  那个Header Basic *****，****部分是由你的email:pwd 编码生成的，是可逆的！建议迅速修改密码，且截图重新打水印。

感谢大佬的提醒，现密码已更改。

---

### 评论 #47 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[LR93609](https://support.worldquantbrain.com/hc/en-us/profiles/30244554462231-LR93609)

> 1. 混信号发挥到了极致，但不太推荐，至少方法要对；先rank再加和会不会好一点？或者说先归一化

倘若不考虑六维，我想我不会这做(回答前部分)；我想我会这么做(后部分) .

> 2. 创造字段一说是否合适？两元、三元、四元组合是不是创造字段的意思？
> ```
> field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .
> ```

我理解二元、三元乃至四元都算是创造字段，创造字段一说也许不合理，它只是作为一种思想，帮助发散思维，能带来更多的想法 .

> 3. 没看懂放这个公式的意义？
> 
> [!NOTE] [图片 OCR 识别内容]
> 看到这里。你还在想向我找寻alpha模板吗?  其实我没有模板
> 时间多的话可以再瞧一瞧上面的内容。看看
> 能不能给到你一点点启发呢 .
> N-l
> Ha > 1 ,3N, 8.t
> Iim
> fa()- Cfa()
> Iim
> fa(?) <
> n〉+o
> n〉+o
> 2=1
> 2二1
> DFN
> 10-P


分隔符 . 它同样代表着一种思想 . 来源于 我有一段时间对黎曼zeta函数ζ(s)的值感兴趣，例如: ζ(2)=Π² / 6，ζ(3)没有结果且不知是有理数还是无理数 . 我想要求ζ(s)保留小数点后P位的精确值，我无法保证前N-1位的值加起来能有这个精度，后来想到了我只需要保证N位后面的数加起来能够小于10^(-P)便能达到目的，于是便产生了上面这个公式，在此作为分隔符 .

---

### 评论 #48 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[顾问 FX25214 (Rank 22)](/hc/en-us/profiles/32678330190999-顾问 FX25214 (Rank 22))

> 对于直接跨数据集两个字段相加，如何避免混信号或者过拟合呢？

先分别验证两个因子有相似逻辑和单独微弱信号，然后才用加和来“加强”信噪比 .

> 这种直接加噪音的方式难道不会在样本外非常的危险吗？

确实会比较危险，通过数据挖掘大量试错偶然发现“巧合”。这个巧合在样本外持续的概率会很低，缺乏稳健的经济学逻辑支撑 .

> 因为我自己点塔是基本上可以一天一个塔，我感觉单数据集也可以在一个允许的时间范围内很好的点塔，所以我比较好奇这样做的意义是什么？

意义: 点塔 . 还是需要先分别验证两个因子有相似逻辑和单独微弱信号，才可用于组合，才能成为一个稳健的alpha .

> 是因为提前用相同或者相似的运算符跑了不同的字段发现他们能捕捉相似的市场信息然后进行简单的加和来加强吗？

我有时并未这样做，不过还是建议像你说的这样，先分别验证因子之是否有类似的趋势信号，从而趋势合成来形成一个更强的信号 .

---

### 评论 #49 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[LL61351](/hc/en-us/profiles/32148227400983-LL61351)

> 一口气看完，非常好的文章，将六个维度及如何提升讲得非常清楚。我是个新手，因为RA比较难挖，想问一下RA和PPA在点塔过程中，会有差异不？

并无差异，ra和ppa都是能够点塔的，但是需要保证的是alpha中包含的字段最多只能够属于两个数据集才能够点塔，alpha中的字段若是属于两个数据集，便能够点这两个数据集的  **⅓ .**

---

### 评论 #50 (作者: CC21336, 时间: 9个月前)

非常用心，质量非常高的一篇帖子，受益匪浅。前两个赛季一直在关注vf，没有好好关关注genius，这篇帖子的帮助非常大。

---

### 评论 #51 (作者: BL72197, 时间: 9个月前)

作为新人受益匪浅，虽然这个赛季还不太会冲等级，但也给下一赛季提供了指导思想，感谢大佬分享！

---

### 评论 #52 (作者: ZJ47021, 时间: 9个月前)

不错，学到了！

---

### 评论 #53 (作者: AM12075, 时间: 9个月前)

=============================================================================

混信号的话，有时间直接+一个field效果并不明显甚至更差了，请问选择另外这个field有什么技巧吗，能够让整体组合表现更加好？

=============================================================================

---

### 评论 #54 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[顾问 WX64154 (Rank 32)](/hc/en-us/profiles/30063596966551-顾问 WX64154 (Rank 32))

> 感谢大佬分享。给我深深上了一课，期待下节。
> 想知道大佬怎么把combine刷的那么高

[图片 (图片已丢失)]

我理解你说的 combine 是指帖子中的 Combined Alpha Performance 指标，我了解到的 Combined Alpha Performance 是指 提交的所有 alpha 的表现 .

我在没成为正式顾问时期，提交的 alpha 虽然没有很好，也没有保持多样性 (只有USA D0和D1)，但是交的都是没有数据缺失的，也几乎没有断交，保持每天一个的样子 .

我第一次更新 combine 是在今年7月，combine 是 2.14不算很高，然后7月14 日成为正式顾问后，刚开始比较难交出 alpha ，过了几天之后我交出了一些比较差的 alpha，fitness 平均 0.6，但是数量上逐渐趋于4-5个；年份以及数据集的变化，alpha 的 prod 相对较低，同时我没有在某地区点不计倍数塔 .

我以为 八月也就是帖子上的 combine 会变差，因为七月体提交的 alpha 质量较差，结果 combine 2.39 . 那我理解  combine 增加的原因有  **自身成长 (alpha每日提交数量较前面有增量)** 、 **alpha组群多样性**  和  **prod相关性**  这几个原因，可以从这几个方面去考虑提交 alpha . [图片 (图片已丢失)]

---

### 评论 #55 (作者: DQ66419, 时间: 9个月前)

看了大佬的分享才知道这个operator计算是这样的，还以为是去重呢，之前都没注意过，学习了。我也是在六维上失败了，大家都太强了，六维排名根本跟不上。下个季度从头开始，感谢帮忙理清了一些思路。另外信号强化的内容也非常受益，只是需要尽量小心一点。

---

### 评论 #56 (作者: 顾问 SJ65808 (Rank 20), 时间: 9个月前)

很不错的分享，也算给新人一些启发，原始字段的一些数学变换可以看做一个新的字段，然后在套一二三阶代码来使用

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #57 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

> 混信号的话，有时间直接+一个field效果并不明显甚至更差了，请问选择另外这个field有什么技巧吗，能够让整体组合表现更加好？

我理解首先需要找一个合适的 alpha，并不需要 alpha 能达到可以提交的程度，需要保证的是 alpha 的phl 图像不严重“跳动”，phl相对较平缓且有上升趋势，那此 alpha 就有可以组合的潜力，选取的另外一个field字段 (遍历) 只要趋势同样有上升类似的phl，那两个组合就会有比较好的效果；

直接组合亦可，不过还是建议先分别验证两个因子有相似逻辑和单独微弱信号，这样比较保险，不然可能会比较容易炸OS，Combine 表现也可能会变差，最后最好是使用 rank 和 sign 检验一下该 alpha 会更加保险 .

---

### 评论 #58 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

[AK76468](/hc/en-us/profiles/28846915371031-AK76468)

> 我看了你的点塔方法，感觉是给强信号增加噪音的方式，将塔字段引入该信号，我认为应该算是混信号。但又看了你十分高的combined，似乎又不一定是混信号，就这一点你怎么看呢？

首先 combined 是看提交的所有 alpha 的综合表现，我使用此种方式并不算多， 所以 我混信号 跟 combined 关系并不大，使用此种方式混信号有可能会降低 combined，但是被 自身成长 和 alpha 多样性 拉回来了.

在点塔时，点塔字段有可能改善 强信号某些指标不通过 (比如: sub-sharpe) 的情况，从而达到可提交的状态 . 至少说这一点是好的，当然也可以不使用点塔字段，只要能达到目的，还能实现点塔，那我就觉我应该使用点塔字段更好一些 .

> 另外您是否会在提交前详细了解alpha表达式的经济学含义呢？

目前没有哦 .

---

### 评论 #59 (作者: JD23670, 时间: 9个月前)

学习了，感谢老大，非常受用

---

### 评论 #60 (作者: MY82844, 时间: 8个月前)

如果达到了GM的硬指标，但是软指标六维拉胯，理论上来说最差可能评为GOLD级别吗，还是说至少Master级别？

---

