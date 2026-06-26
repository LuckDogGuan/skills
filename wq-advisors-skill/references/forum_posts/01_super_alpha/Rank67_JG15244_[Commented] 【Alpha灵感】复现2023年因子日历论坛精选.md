# 【Alpha灵感】复现2023年因子日历论坛精选

- **链接**: [Commented] 【Alpha灵感】复现2023年因子日历论坛精选.md
- **作者**: LR93609
- **发布时间/热度**: 1年前, 得票: 47

## 帖子正文

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

---

## 讨论与评论 (35)

### 评论 #1 (作者: JB71859, 时间: 1年前)

> 很强的新人，加油

---

### 评论 #2 (作者: FG26814, 时间: 1年前)

冷哥超棒的， 深邃睿智， 学习了。 复现定位过程也是学习的过程。

---

### 评论 #3 (作者: CL49716, 时间: 1年前)

手动点赞！

---

### 评论 #4 (作者: DX58146, 时间: 1年前)

对操作符用的真好，很好的分享

---

### 评论 #5 (作者: 顾问 JG15244 (Rank 67), 时间: 1年前)

大受震撼！！！！！！！！！！！！！！！！！！！！！

震撼之情，已经不知道怎么表达了，只能说一句，大佬牛逼！

期待大佬成功正式顾问，加入研究小组，带来更加精彩的分享！

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================

---

### 评论 #6 (作者: RL69491, 时间: 1年前)

向大佬学习，我也复现了一些，基本提交完就忘了，还需进行深入思考~

---

### 评论 #7 (作者: SY86571, 时间: 1年前)

分享就是好同志,火钳刘明

---

### 评论 #8 (作者: AR86302, 时间: 1年前)

很棒的分享，学习到了！

---

### 评论 #9 (作者: AK76468, 时间: 1年前)

************************************************************************************************

感谢大佬分享这些有意思的alpha灵感，IQC期间凭借有限的数据和运算符，竟能作出如此数量众多、丰富多彩的alpha，真的是令人羡慕的实力。希望大佬在IQC取得好成绩！！！

************************************************************************************************

---

### 评论 #10 (作者: BJ10003, 时间: 1年前)

**信号普遍性验证** ‌
贴主观察到"多数因子有信号"的结论与行业研究高度吻合。根据量化多因子研究，估值、动量、技术等十大类因子中，约70%的因子在特定市场条件下具有统计显著性（如估值因子BP_LR的累积收益率显著优于基准）

---

### 评论 #11 (作者: LG87838, 时间: 1年前)

太强了，总是发愁做不出模板，找不到因子，其实是我太懒了，不愿走出舒适区。

感谢大佬的启发！

-----------------------------------------------------------------------------------

走出舒适区，就是有想法啦，不管结果，动手去做！

-------------------------------------------------------------------------------------

---

### 评论 #12 (作者: MY21251, 时间: 1年前)

大佬牛逼，我也想过去复现，但是一开始没有头绪，就没有继续深入研究。看到大佬的帖子，深感不足，接下来要卷起来，多多努力！！！

发现个小问题，应该是

Amihud = ts_mean(abs(returns)/（volume*close）,n)

---

### 评论 #13 (作者: AL13375, 时间: 1年前)

太强了！！！

对新人王的以下几点：

**1. 经济学原理是通的，虽然多是国内投研的因子，USA依然能跑出信号。**

**2. 复现的过程是学习，关键在于对字段的深刻理解和操作符的灵活运用。**

**3. 学习的目的是拓展，重点是对因子构建逻辑的领会和灵感的孜孜追索**  **。**

我也深有体会！

经济学原理是相通的，同样的策略不管是用在哪个region都会有不错的效果，只是或多或少需要加一些微调就能得到很好的alpha。

对字段的深刻理解和对操作符的灵活运用，这两点是我非常欠缺的地方，目前也在手搓的过程中有所收获，等sac结束后我会花更多时间在这上面！

对因子构建逻辑的领会，这也是需要一些经济学基础的，不然就变成了穷举型seek alpha的不归之路，长久来看是很不友好的，应该不断的学习并且让自己生出更多的灵感才是王道！

wq之路漫漫，吾将上下而求索！！！

---

### 评论 #14 (作者: TS96358, 时间: 1年前)

冷哥是领袖，超级牛的

---

### 评论 #15 (作者: 顾问 KZ79256 (Rank 21), 时间: 1年前)

火钳刘明

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================

---

### 评论 #16 (作者: QQ68782, 时间: 1年前)

太强了!!!!!!!!

向大佬学习, 期待大佬后续的分享

---------------------------------------------------------------------------------------------------
知识就是力量 Knowledge is power.

---

### 评论 #17 (作者: BW14163, 时间: 1年前)

分享就是好同志,感谢大佬分享

---

### 评论 #18 (作者: 顾问 YX23928 (Rank 8), 时间: 1年前)

太强了，向大佬学习！！！！！

====================================================================================

---

### 评论 #19 (作者: 顾问 MG88592 (Rank 38), 时间: 1年前)

iqc大佬吗，期待你成为正式顾问解锁权限，给咱国区带来更多更好的分享！！！！！
================================================================
================================================================

---

### 评论 #20 (作者: JX28185, 时间: 1年前)

牛啊，来顶一下

---

### 评论 #21 (作者: FH33043, 时间: 1年前)

冷神直冲gm

---

### 评论 #22 (作者: YQ51506, 时间: 1年前)

为大佬的分享点赞，我也正有此意，加油

---

### 评论 #23 (作者: PW58059, 时间: 1年前)

看完冷神的帖子深有感悟，复现中对字段和操作符的深挖比单纯跑信号更有价值，而从模仿到领悟构建逻辑的过程，正是从新手到进阶的关键。很多人卡在 “找不到因子”，其实缺的就是这种沉下心拆解、转化、再创新的耐心。

能看透因子背后的逻辑，才能真正生出属于自己的 alpha 灵感。期待后续更多拆解，太值得反复琢磨了！

=======================================================================
那些凌晨三点还亮着的屏幕光，终会化作晋级榜单上闪耀...
=======================================================================

---

### 评论 #24 (作者: XX42289, 时间: 1年前)

GM俱乐部欢迎您！看到这样强大的新人，真的是非常震撼啊！

====================不混信号，不过拟合=======================

---

### 评论 #25 (作者: JS34795, 时间: 1年前)

2023年因子日历在哪里找的

---

### 评论 #26 (作者: YD74724, 时间: 1年前)

感谢您的分享！

---

### 评论 #27 (作者: AH18340, 时间: 1年前)

大佬牛啊

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #28 (作者: YW93864, 时间: 1年前)

确实不错！！

这些因子都是常规的因子，虽然可能经济逻辑都很简单易懂，但是可以丰富基础因子库，后续成为顾问后，这些因子都是做SuperAlpha的基石。期待更好的效果！

=======================================================================================================================================================

---

### 评论 #29 (作者: TQ88961, 时间: 1年前)

非常棒。请教 **调试结果（升阶并调试效果：中性化并增加进出场条件），这里中性化是指经过2阶处理吗？增加进出场条件是指3阶处理吗？**

---

### 评论 #30 (作者: XC66172, 时间: 1年前)

大佬太厉害了~~

感觉这样系统性的学习一番后，楼主的码力和对量化的理解都上了一个台阶。

预祝这个赛季取得一个好的成绩~~

=======================================

FIGHTING LABUBU

=======================================

---

### 评论 #31 (作者: 顾问 SJ65808 (Rank 20), 时间: 11个月前)

太强了!!!!!!!!

向大佬学习, 期待大佬后续的分享

---------------------------------------------------------------------------------------------------
知识就是力量 Knowledge is power.

---

### 评论 #32 (作者: LR93609, 时间: 9个月前)

[TQ88961](/hc/en-us/profiles/29438986292759-TQ88961)

**可以这么理解吧，毕竟平台进行的中性化也有风控相关的**

我认为，平滑pnl最有效也是最靠谱的方式，还是进出场条件的控制，

即便是再完美的因子表达式，也要看市场行情吧，总不能跳火坑吧！

当然了，平台不鼓励混信号，或者是增加操作符，

也不鼓励使用非线性， **我们这里只从技术层面进行分析。**

**自从转正以后，我自己也很少用if_else、trade_when等非线性操作符了，请大家慎重使用。**

---

### 评论 #33 (作者: EL94401, 时间: 6个月前)

从60天的点亮60塔的帖子，一路阅读大佬所有文章到这里。篇篇精品，还需反复阅读。开始只是看到60天点60塔，两个月从转正顾问到GM的飞跃。看到这里，知道厚积薄发的道理。自惭形愧，本来为学习量化，但忘记初衷，一路为了短暂晋级，堆积低质量因子的无效学习中，欲速则不达。向大佬学习，注重基础积累。

---

### 评论 #34 (作者: LK25891, 时间: 6个月前)

这内功是真深厚啊，底层都扒得一干二净，确实练好内功比什么都重要，不下苦功夫不行，吾辈楷模~

---

### 评论 #35 (作者: 顾问 SJ65808 (Rank 20), 时间: 5个月前)

这就是gold直升GM的实力吧，值得新人们借鉴学习

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

