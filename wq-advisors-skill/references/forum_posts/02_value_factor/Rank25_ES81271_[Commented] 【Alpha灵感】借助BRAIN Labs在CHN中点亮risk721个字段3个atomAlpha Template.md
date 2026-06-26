# 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk72（1个字段3个atom）Alpha Template

- **链接**: [Commented] 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk721个字段3个atomAlpha Template.md
- **作者**: LR93609
- **发布时间/热度**: 9个月前, 得票: 104

## 帖子正文

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

---

## 讨论与评论 (19)

### 评论 #1 (作者: WF37935, 时间: 9个月前)

请教一下，这三个alpha和lab的关系是什么?

第一个是看正态分布，所以判断是因子，可以简单处理。

第二个是因为第三点日均换手率极高，且存在波动性，所以用ts_std_dev来处理？

那第三个呢。

也没有见industry的使用，是中性化用的industry吗？

---

### 评论 #2 (作者: HX47598, 时间: 9个月前)

好奇Daily reproducible specific returns in % units和returns有什么不同，我理解本质是差不多的，分布也是差不多的（-10到10之间，某些产业比如科创板，新股会出现超过10的极值）

所以本质上以上alpha都是trend following策略？

感觉使用tradewhen加入开始和退出条件或许有用...

---

### 评论 #3 (作者: JX28185, 时间: 9个月前)

冷兄请教一下,可以重点解答一下借助BRAIN Labs给了你哪些灵感和思考，以上三个模版进行了多长时间,多大空间的探索.还是手到擒来,我想了解一下过程和细节.

---

### 评论 #4 (作者: SX13432, 时间: 9个月前)

非常有启发，感谢大佬分享！

示例中有个操作符还没有权限，加油~

---

### 评论 #5 (作者: HJ88260, 时间: 9个月前)

太顶了这波分享！给大佬递茶🍵～ 看完真的忍不住夸一句：这才是Brain平台正确打开方式啊！！

之前自己也搓过risk72，但真没像楼主这样拆得这么细——从字面解读到分布可视化，再到换手率、极值处理，甚至连不同industry的分布密度都考虑到了，属实硬核。感觉不像在逛论坛，像在偷学量化私募的内部培训哈哈😂

尤其赞同“数据基本功”这点！很多人一上来就疯狂堆算子，结果回测一堆废alpha，归根到底还是没吃透原始字段。risk72本身质素能打，接近正态、日频可复现，这种字段稍微调个参、加个波动率缩放，真的很容易出信号。楼主分享那几个实操作业（虽然有一个不推荐hhh），抄起来超级顺手，拯救了我这种没灵感又卡ddl的懒人……

另外跪求多来点这种Lab分析可视化！！平时自己看分布经常懵一圈，有图有真相直观看行业密集度和极值，调权都有方向了。已经拿小本本记下“波动率放大”这个思路了，今晚就滚去搓因子试试🙏

最后小声bb：risk72这么香，能不能求个后续——比如怎么和其他字段混搭？或者极端行情咋稳过？……（疯狂暗示.jpg）总之给楼主疯狂打call，多更这类干货！！👏

---

### 评论 #6 (作者: QD44113, 时间: 9个月前)

感谢分享

---

### 评论 #7 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

感谢分享。我最近也在用lab。只是看看数据字段缺失值多不多，然后挑缺失值少的拿来做回赐。

你的“接近正态分布的字段本身就可能是因子，简单处理便可以使用。” 这句话真是点醒我了。以后在用lab做分析的时候，可以有的放矢，事半功倍。

---

### 评论 #8 (作者: CS14313, 时间: 9个月前)

感谢分享，受益匪浅，目前CHN还没有尝试过，等我把ASI和USA挖掘的差不多了，也去试试CHN，好像CHN的系数还比较高呢。祝大家多赚钱。

---

### 评论 #9 (作者: SZ24058, 时间: 9个月前)

感谢分享，等下也去跑一下试试

---

### 评论 #10 (作者: 顾问 WX64154 (Rank 32), 时间: 9个月前)

这曲线有点不大平滑 我有点不大敢交1 这种

---

### 评论 #11 (作者: BW14163, 时间: 9个月前)

学到了，感谢大佬的分享，一个字段，3个提交的alpha，直接点亮一个塔

---

### 评论 #12 (作者: LR93609, 时间: 9个月前)

[WF37935](/hc/en-us/profiles/30529442824471-WF37935)

感谢回帖

当时我对Labs的使用也不太熟悉，大体路径是：

1. 我一般会先上三件套：裸跑、波动率、反转

2. 三件套表现不错，我就遍历一遍常用的模版

3.选择表现最好的，遍历neut和Decay，提交。

不知道是否能够帮助到你，再次感谢。

---

### 评论 #13 (作者: 顾问 ES81271 (Rank 25), 时间: 9个月前)

感谢分享，给出了很多思路。

---

### 评论 #14 (作者: MY27687, 时间: 9个月前)

================================MY27687=============================================

感谢大佬分享，之前跑了几天chn ，发现一个也没出，失去信心，再也没跑过chn，感谢大佬分享的经验！！！学到了，祝大佬base多多，value factor 高高，谢谢大佬分享！！！

====================================================================================

每天坚持提交一个好的alpha！！！加油

---

### 评论 #15 (作者: AM12075, 时间: 9个月前)

====================================================================================

感谢分享，但是fitness0.3+的因子提交上去对于整体vf会不会有影响呢？

====================================================================================

---

### 评论 #16 (作者: MY49971, 时间: 8个月前)

感谢大佬分享，这几个指标确实都比较一般，不知道对combine  和 vf 影响怎么样

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #17 (作者: 顾问 SJ65808 (Rank 20), 时间: 8个月前)

看了一下这几个alpha好像指标都挺一般，不知道楼主如何权衡，提交标准是咋样的

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #18 (作者: YL20304, 时间: 6个月前)

感谢大佬分享! 我试试看能否改进下！

---

### 评论 #19 (作者: JJ69164, 时间: 5个月前)

**不同时期不同industry分布过于密集------浅显理解集中不是要好一些吗？**

---

