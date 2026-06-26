# 【Alpha灵感】A股换手率类因子

- **链接**: [Commented] 【Alpha灵感】A股换手率类因子.md
- **作者**: KJ42842
- **发布时间/热度**: 2年前, 得票: 124

## 帖子正文

标题：华泰单因子测试之换手率类因子

作者：林晓明

概述：该篇论文作者构建了近N个月每日换手率均值，标准差，及衍生的换手率乖离率等12个基于换手率的因子，首先分析了这些因子行业间的差异以及与市值因子的相关性，然后使用回归法和分层回测等因子测试流程中的因子收益率,t值,IC值等系统地验证了换手率因子在A股市场中的有效性。

Alpha Idea:

直接将论文中构建的因子原封不动的用Fast Expression实现。


> [!NOTE] [图片 OCR 识别内容]
> 图表1:
> 华泰单因子测试一换手率因子及其描述
> 大类因子
> 具体因子
> 因子描述
> turn_Im
> 个股最近 N 个月内日均换手率
> turn_3m
> N=l,
> turn_Gm
> bias_turn_Im
> 个股最近 N 个月内日均换手率除以最近2年内日均换手率
> 再减去1
> bias_turn_3m
> N=l,
> 换手率因子
> bias_turn Gm
> (Turnover
> std_turn_Im
> 个股最近 N 个月内日换手率序列的标准差
> Factor)
> std_turn_3m
> N=l, 3,
> std_turn_Gm
> bias_std turn Im
> 个股最近 N 个月内日换手率序列的标准差除以最近2年内日换手率序列的标
> bias_std_turn_3m
> 准差,
> 再减去1
> bias_std_turn Gm
> N=1, 3,


由于论文中论证了换手率因子的行业差异，所以我们选用Industry中性化，可以看出该alpha表现出明显的信号。


> [!NOTE] [图片 OCR 识别内容]
> 5|?
> S2
> 11
> .
> AESULTs
> LC
> Sotts
> CHIIOTITOPJD00
> 04014 MVU Sonwlatoa
> Chart
> UNcUCT
> 4T1
> Kl L
> Tl
> oCI
> [o
> 1o
> NUIuAUUATI
> 6C8
> AuttArIC
> Int
> UIN
> Utawlt
> APOy
> Urmr
> UTIhrMt +144290
> CAUTTUTTN
> OSU
> 50
> N


*Note: Sharesout is counted in millions on Brain*

*
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> stage
> IS
> 05
> Aggregate Data
> Sharpe
> TUrnover
> Ciness
> Returns
> Orawdown
> Margin
> 2.18
> 5.269
> 3.28
> 28.329
> 22.31%
> 107.64900
> Year
> Sharpe
> Tumover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.95
> 5.5930
> 二91
> 34.62-
> 1.70
> 123.81
> 118
> 73
> 2012
> 2.95
> 5.093
> 一56
> 29.91
> 5.73
> 117.5
> 1519
> 777
> 7013
> 22-
> 5.043
> 3.25
> 26.36-
> 112
> 10_.55
> 1511
> 371
> 2014
> 1.95
> 5.453
> 2-7
> 20.10--
> 7.00
> 73.30:
> 1-91
> 397
> 2015
> 0.03
> 5.753
> 0.02
> 1.09-7
> 22.31
> 3.30:
> 1373
> 10ED
> 2016
> 212
> 5.043
> 3.08
> 26-2-
> 7.30
> 10-.90:
> 1560
> 1009
> 2017
> 3.0-
> 5.313
> 5.36
> -5.517
> 7.15
> 175.17::
> 2016
> 96_
> 2013
> 192
> 一981
> 3.02
> 23.87
> 7.95
> 115,33:
> 2031
> 973
> 2012
> 2.5
> 5.113
> 一49
> 357
> 13.3-
> 141.32:
> 1976
> 1027
> 2020
> 1.43
> 5.373
> 1.33
> 2239
> 10.153
> 33:
> 1952
> 1059
> 7021
> 9-0
> 5.037
> 31.37
> 43372
> 2.301
> 527.62:
> 1971
> 1053
*

因为文中论证了换手率因子与市值的负相关性，所以我对市值进行分组再通过group_neutralize降低市值对换手率因子的影响，可以看出alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> SITUUO !
> SLIZ
> 5T73
> Sukma
> RESULTS
> LSRI
> ed
> OSOOOC
> Chart
> 1881
> Tot
> Ee]
> CO
> 3-
> A
> JOT
> TIII
> MUUTRUIUATWNI@
> TUAATONI@
> &1+1151118
> s
> AaT
> Dlawl
> Noply
> TUTTO 
> Volutsharoscut 1i2
> Rup utrallzt
> SanltUrTOp
> bCetlran (Cap , CanR O.1
> 7TNe
> SCUO
> 7 +
> o( a&
> ssnely



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marain
> 2.67
> 6.069
> 4.29
> 32.219
> 13.469
> 106.25900
> Year
> Sharpe
> Tumover
> Fitness
> Retums
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.21
> 6.319
> 5,45
> 36,133
> 4,6053
> 114,455
> 1394
> 756
> 2012
> 3.23
> 5.761
> 5,65
> 32,999
> 4,499
> 114.565
> 1505
> 791
> 2013
> 2.64
> 5.731
> 一11
> 30.234
> 4.625
> 105.514
> 1503
> 379
> 2014
> 2.92
> 6.2197
> 一-3
> 28,756
> 5.7895
> 92.67.9
> 177
> 910
> 2015
> 1,38
> 6.471
> 2'
> 20,97
> 13,46
> 64.77
> 1330
> 1048
> 2016
> 3.29
> 5.011
> 5,64
> 36,639
> 5.105
> 122.005
> 1634
> 935
> 2017
> 7.31
> 5.041
> 502
> 39,359
> 5,3795
> 131.92
> 1934
> 935
> 2018
> 2.50
> 5.329
> 一.10
> 33,599
> 7.1545
> 115.3
> 1997
> 1007
> 2019
> 3.05
> 5.0317
> 5,-0
> 38,876
> 11,0655
> 128.84
> 1959
> 10-
> 2020
> 1,11
> 6.357
> 1,27
> 16,31
> 9,811
> 51.385
> 1918
> 1093
> 2021
> 6.11
> 5.791
> 17,03
> 97.133
> 2.1455
> 335.72:
> 1952
> 1062


文章还对换手率因子进行了样本期长度的敏感性测试，发现用5天左右的长度能使回归因子收益率以及IC,IR达到最佳。所以，我将alpha的样本期长度从一个月（22个交易日）改为5天，可以看到alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> o
> CATCIN
> Chart
>  Uwcuo
> to
> Fg Ce
> CU
> ] [If
> Cggo
> SUIUAOe
> 62C
> TRUNCATION
> Isty
> UO1
> MA Mo
> Uul
> NOy
> Irmw
> Taloshriyt +111:
> RTO FutrT-LCnurmer,5
> LUCtTane (CAPI,
> TNRC
> N
> SCUO
> *0



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> TurnoVer
> Finess
> Relurns
> Drawdown
> Margin
> 2.90
> 13.989
> 4.81
> 38.449
> 10.049
> 55.01%00
> Year
> Sharpe
> Tumover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.27
> 13.743
> 5.57
> 39,84
> 4,73
> 57,99
> 117
> 733
> 2012
> 3.78
> 13.635
> 6.38
> 38,845
> 4.101
> 55.995
> 1525
> 771
> 2013
> 3.15
> 12.539
> 5.11
> 33.-0
> 5.10*
> 52.66*
> 1525
> 356
> 2014
> 2.32
> 14,321
> 3.39
> 23.14
> 5.369
> 37.975
> 143
> 90
> 2015
> 2,13
> 15.233
> 31
> 31,095
> 7,081
> 10,8
> 1373
> 1065
> 2016
> 3.33
> 13.883
> 5.71
> 39.365
> 5.055
> 55.71
> 1695
> 97_
> 2017
> 2.79
> 13.239
> 一91
> 41.16
> 10.0_95
> 62.01
> 1992
> 935
> 2018
> 3.30
> 13.161
> 6.15
> 45.72
> 6.5193
> 69.505
> 2010
> 99
> 2019
> 3.79
> 13.691
> 7.50
> 53.545
> 9,89
> 78.22*
> 1989
> 101
> 2020
> 114
> 13.91
> 1-1
> 21.3355
> 9.3555
> 30.67
> 195-
> 1057
> 2021
> 5.62
> 12.439
> 15.11
> 90.33
> 1.2235
> 125.334
> 1973
> 1046


最后，文中描述如果从收益率的角度来说换手率和换手率序列标准差较好，如果从稳定性的角度来说换手率的乖离率和换手率序列标准差的乖离率较好。


> [!NOTE] [图片 OCR 识别内容]
> Sattos
> CUTITTIISOINO
> Kogat
> Chart
> T-
> TTMT T
> Tn504
> LUT
> UCI
> TI
> SITAIATO
> TUtCATIC
> UJU
> LTTTIo
> TeTa
> 
> II
> Ug
> TITT
> To4rMJ
> Il
> (_*d_de(tu noer 51/1_Jtd_do(tumer 500)1;
> OTTuT AIIIsIIa
> UUCLAICaN(Ca !
> 0]; ,0.19;
> T
> 50
> 750
> IUTCI1
> 5Pnl 1TOI
> Urto
> +a



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> 05
> Aggregate Data
> Sharpe
> Turnover
> Finess
> Returns
> Drawdown
> Margin
> 2.96
> 26.899
> 2.98
> 27.339
> 12.389
> 20.329000
> Year
> Sharpe
> Turnover
> Fitness
> Returs
> Drawuown
> Margin
> Long Count
> Short Count
> 2011
> 2.30
> 26,479
> 2.53
> 24.209
> 3.749
> 13.285
> 1413
> 737
> 2012
> 3.97
> 26,019
> 1,24
> 29.613
> 3.6330
> 22.775
> 1519
> 776
> 2013
> 3.35
> 27,554
> 3.35
> 27.584
> 3.333
> 19.95,。
> 1530
> 852
> 2014
> 2,11
> 27,459
> 1,43
> 13.5130
> 4,303
> 9.345
> 1521
> 366
> 2015
> 2.83
> 29.985
> 3,05
> 33.33
> 12381
> 222-5
> 148-
> 95
> 2016
> 4.15
> 26.599
> 4.89
> 35.94
> 一459
> 27.79
> 1719
> 950
> 2017
> 2.65
> 25,39北
> 2.72
> 26.753
> 5.2030
> 21.075
> 1953
> 1022
> 2018
> 一7
> 25.269
> 一95
> 3577
> 2.903
> 2332
> 1992
> 1012
> 2019
> 1,23
> 26,549
> 5.13
> 39.07
> 3.3635
> 29.344
> 1962
> 1040
> 2020
> 0.27
> 27,459
> 0,03
> 3.2035
> 9.1930
> 2.335
> 1935
> 1075
> 2021
> 2.37
> 27.179
> 2.93
> 29.533
> 1.729
> 21.72
> 1969
> 1055


从结果可以看出，虽然换手率乖离率因子的收益率不如换手率因子，但是该因子在更多的年份有更小的Drawdown, 因而有更平滑的PnL曲线和更高的Sharpe，与论文中的结论一致。

相关数据集：Price Volume Data for Equity

疑问与讨论：

1. 换手率因子如果在A股市场验证有效，是否在其他市场也是有效的？
2. 有什么方法可以进一步改进换手率因子Alpha使其可以达到Robust Universe Return?


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> 05
> PASS
> FulL
> Robust universe rerurns Of 10.7896Is below CutOff of 15.3896 (~095 OfAlohaj。
> WARNING
> 3 PENDING


---

## 讨论与评论 (18)

### 评论 #1 (作者: KJ42842, 时间: 2年前)

为了使该alpha可以提交，又做了些分析研究。

由于Robust Universe Return不够，说明在CHN的真实交易当中所能实现的return与原return相距较大。那么最直接可以想到的原因(假设)是由于alpha做空了很多市值较小流动性较低的股票获得的return无法在真实市场中做空获得，导致这部分return在Robust Universe 中无法实现。

为了验证我的假设，最直观的方法是通过观察原alpha分布中换手率较高的是否是无法做空的股票，但是鉴于我们无法直接对原始分布和值域进行直接的观察，我记起来论文中有这样一张表格，我们可以对换手率的数值大小以及分布情况有一个大致的感知。


> [!NOTE] [图片 OCR 识别内容]
> 困表3:
> 各一级行业 turn
> Im; bias_
> tUIn
> Im std_
> tUIn
> 1m; bias_std_turn_Im 中位数比较 (2016/12/30)
> 2.09
> turn_Im
> std_turn_Im
> -0.3
> bias_turn_Im(右轴)
> bias_std_turn_Im(右轴)
> -0.4
> 1.59
> -0.5
> 0%
> -0.6
> -0.7
> 0.59
> -0.8
> 0.0%
> -0.9
> 蓑
> 浆  n  干 吴
> 们  g0
> s
> 冶
> 类 卅  婆 &#卉d爿 H
> 裟
> 蠡
> 叟  兴
> 笨
> 慧
> 然
> 黧$鞲
> - 忠
> }
> 欲  v
> 钛
> 簋
> 
> 。


由于该表格是行业并且是一个月的换手率的均值，所以我们可以感知到个股换手率之间的差异会比文中指出的行业间的更大，便容易导致alpha集中做空少部分大换手率的小股票获得大部分的Return。另外，由于换手率的天然属性便是小市值股票的换手率高，大市值的公司换手率低(如文中计算表明，换手率因子与市值呈负相关)，使该换手率alpha会做空小市值公司。以上两点从数值上和逻辑上与我的假设相呼应。

接下来，我通过了一些实验来验证我的假设。

我将原alpha进行3次乘方，这样可以进一步使个股间换手率的差异加剧，原因可以参考下图


> [!NOTE] [图片 OCR 识别内容]
> 10
> powerlrank,1)
> powerlrank,21
> 08
> powerlrank, 31
> powerlrank, 4)
> powerlrank;0 51
> 0.6
> powerlrank,0 .2)
> `
> 04
> 0.2
> 00
> 500
> 1000
> 1500
> 2000
> 2500
> 3000
> socks


可以看到3次方比均匀分布在较大值与较小值间的差距会变大，曲线在首端变缓末端变陡，这样会让alpha加大力度集中做空换手率高的小盘股。


> [!NOTE] [图片 OCR 识别内容]
> S !
> Lat
> RESUCT
> LEARN
> CHNOTITOPOC0
> 99
> Well golon
> Chart
> 1!
> TeAT
> Fl {ot
> Eutty
> e01
> 
> 7'
> Noa
> TT
> VOI
> TITTUIUATONI
> UMOUING
> DUCU6
> O
> Valowlt
> 4」 IArteu
> SIII-TRaTUTVT,51 ;
> VL4 TtUTt41 ]
> RoTl
> 4ramtJ
> LNe
> 0h1+
> o



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> IS
> 0S
> PuSS
> FAIL
> Robust universe returns Of 8.6196 is below CUtOff Of 25.1396 (40 Of Alphal。
> WARNING
> 3 PENDING


我可以看到新alpha的Return大幅度提升，而Robust Universe Return却进一步下降。以上的实验基本可以验证了我的假设。

那么接下来针对该假设做出对应的改进方案。

我先尝试用Rank来改变原alpha的分布，希望使weight可以不集中分布在换手率高的小股票。 Rank 将alpha的原始值分布转化成了0-1之间的均匀分布，也将alpha的绝对数值转化为了相对位置关系，缺点是丢失了原始值信息或降低原alpha的表现，优点是一方面减小weight的集中，也可以减少极端值对weight的影响，还可以验证原alpha的鲁棒性。


> [!NOTE] [图片 OCR 识别内容]
> T07
> !
> '
> N
> C+
> N
> '
> !
> RESULT
> IF
> 541140
> TUNO7180NOI
> C
> e
>  Chart
> 140701410
> Kat Eoe
> 
> 0411411
> T0!
> A
> 4o
> TTO
> Ut
> At
> @ |
> Kmtt
> l
> Ta9748704100
> S
> Turtwoy
> Ulu In  LUT *14382831 ;
> 5La
> Tu 
> cran { turnoter,3/;
> rwup uTeulIJ(UI
> UIrat(cum
> Tult O1
> 0 /;
> SI
> O
> TO
> 0 T



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> OS
> 8PASS
> Fitness Of 2.42 Is above CUtOffof1.
> Turnoverof 11.329015above CUOffOT 196。
> Turnoyerot 11.329615 below CUtOfOT 7096
> Weigntis ell distributed over instruments。
> Rerurns Of 18.469615 above CUtoff 01 896
> Sub-universe Sharpe Ot 1.65 Isabove CUtOfOf 1.22
> Robust universe Sharpe Of 1.5215 above cutoff OT 0.80 (4036 Or Alpha)
> Robustunierse returns Oi 9.1696Isabove CUoffoi7.3896 (2095 OfAlonaj
> 2 FuIL
> Sharpe O1 1.991s below cutoffof 2.07。
> ISladder Snarpe OT 1.26 Is OelOw CUtOffOT 2.07Torladderyearz; 2/18/2021,2/19/2019,
> WURNNG
> 3 PENDING


可以看到rank使原alpha的表现大幅降低，虽然使得以通过Robust Universe Return，但是使Sharpe降低到线下。

于是，我重新使用power把rank之后的分布拉的陡峭以提高表现，


> [!NOTE] [图片 OCR 识别内容]
> a
> Ca|
> 0
> FFSIII T 
> 54
> LnCme
> CIOO |TOC
> Chart
> Lt
> 8
> Ttl
> 7+
> 0
> OUUTRATION
> TRUNAION
> IM
> 1
> N
> T&
> Koo
> 人0
> UITRT
> 521toshyit *74414591 ;
> HIU
> Foryrum_CtTur5/;
> Arron nt rlUyIM
> hsrltrpl
> TI
> 41'u
> 94
> (
> etaw



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
>  Stage
> 0S
> PASS
> Sharpe of 2.41is above CutOff Or 2.07.
> Ftness Of 3.30Isaoove CutOffof1.
> Turnover of 11.3796 5above CUtOff OT 196
> Turnover of 11.3796is below CutOff Of 709。
> Weignt is Well distributed over instruments。
> Returns Of 23.4696 Is aboVe CUtOff Oi 896。
> SUb-unierse
> Sharpe Of 2.05 is above cUtOff Of 1.48。
> Robustunierse Sharpe Oi
> .86 is above CutOff Of 0.96 (4096 Of Alpha)。
> Robust universe returns Of 11.1596 Is above CUtOff Of 9.3896 (4095 Of Alpha)。
> FAIL
> [SIadder Snarpe of
> Is Delow CutOffoi 2.07 forIadder
> 2:2/18/2021..2/19/2019
> WARNING
> 3 PENDING
> 1.74
> year


可以看到alpha表现如期上升，但是IS ladder sharpe还差一点。这时我想起文中有提到，换手率因子在大盘股中效果较差，但在中小盘股中效果很好。


> [!NOTE] [图片 OCR 识别内容]
> 由于换手率因子的分层测试结果与回归法结果并不完全一致。我们想要更全面地了解这种
> 差异因何而产生。图表106中的结果是由 WLS 回归产生 (用个股流通市值的平方根作为
> 权重。具体描述参见笫二章 "单因子测试流程"  的笫一小节 "回归法"  中测试模型构建方
> 法的第5点)〉我们将 WLS 回归改成 OLS 回归,
> 回归测试结果对比显示在图表110中。
> 通过观察可以发现 ,
> 在 OLS 回归下所有换手率类因子的效果都有所提升。这也和换手率
> 因子的特点有关-一在大盘股中效果较差。在中。小盘股中效果很好。并且 OLS 回归下
> bias_turn_Im
> bias_std_turn_Im 因子的效果是好于 turn_Im
> std_turn_Im 因子的,可
> 以从某种程度上说明,
> bias_turn_
> bias_std_turn_Im 因子在大盘股中失效得更严重。
> 1m


于是我尝试通过right_tail操作符将换手率最低的大盘股剔除的方法来进一步提升Sharpe表现。


> [!NOTE] [图片 OCR 识别内容]
> S
> I
> S(。
> 8
> 
> m@
> Shu7
> 
> UL
> LEARN
> CHNOTITORO00
> C646490 Nyll Slmlatlae
> Chart
> OIsCt
> Te
> Tn Ltolt
> uCIO
> Uus
> TO
> ITAUT
> ToAT
> TU
> 46
> 0
> 0420
> T
> TOU/sharsct 'IC;
> Inl
> rIpht_tl(po(rank(ts
> Ol7tIrRr 5 aInleo401;
> RTOUP MutrlIIL+I7na1
> Wchetlran(Cap
> TaNR"
> #1J;
> 1M
> L
> 111C
> 2
> Olth  hMa Inob
> okdwnoos



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Stage
> IS
> O5
> Aggregate Data
> Sharpe
> TUrnOVer
> Finess
> Rerurns
> Drawdown
> Margin
> 2.62
> 16.629
> 3.19
> 24.649
> 8.4496
> 29.66
> Year
> Sharpe
> Tumover
> Fitness
> Returs
> Drawuown
> Margin
> Long Count
> Short Count
> 2011
> 317
> 17.65
> 3.86
> 26.2255
> 3.253
> 29.72
> 983
> 80
> 2012
> 3.23
> 17.233
> 3.73
> 22.23
> 3.95
> 25.355
> 053
> 85
> 2013
> 2.55
> 18.011
> 2.88
> 22.955
> 1.1855
> 25.13
> 1101
> 896
> 201-
> 2.23
> 17.451
> 2.25
> 17.059
> 5.309
> 19.53:
> 1115
> 9
> 2015
> 2.36
> 16.9410
> 2.81
> 24.1055
> 5.521
> 28.466
> 1172
> 952
> 2016
> 3.33
> 15.4-3
> 一63
> 29.31
> -91
> 33,61::
> 1259
> 1006
> 201
> 2,57
> 16.301
> 312
> 26.6755
> 1429
> 32.73
> 1396
> 1112
> 2013
> 2.80
> 15.47
> 3.71
> 27.15
> 一55
> 35.12::
> 1390
> 1122
> 2019
> 3.82
> 15,791
> 5.83
> 36.72
> 7.691
> 46.52
> 1373
> 1108
> 2020
> 0.65
> 16.201
> 0-7
> 8.34
> 3449
> 10.30:
> 1377
> 1115
> 2021
> 5.3.
> 16.1730
> 10.40
> 61.335
> 141
> 75.8
> 1381
> 1120
> 9ooo



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> 0S
> 10PASS
> Sharpe ci 2.6215 above Cutoff oi 2.07.
> Fitness Of 3.19 Is above cUtOff of1。
> Turnoverof 16,629615 above CutoffOT 196。
> Turnoverof 16,629615 below Cutoffof 7096
> Welgntis ell distributed overinstruments。
> Returns Of 24.6496 I5 above CUtOff Ot 896
> Sub-universe Sharpe Of 2.33is above CUtOffof 1,6。
> Robustunlerse Sharpe oi
> .84is above CUtOff Of 1.05 (4096 Of Alpha)。
> Robustunlverse returns Of 11.1996Isabove cUtOff of 9.8696 (4095 Ot Alphaj
> IS ladder Sharpe Of 2.49 is above CUtOff Of 2.37 for ladder year 4: 2/18/2021..,2/19/2017。
> WARNING
> 3 PENDING


这次终于得到了可以提交的Alpha!

Note: 通过二次power后right_tail最小值0.03可以剔除掉Top3000中500只左右的股票，而不是rank均匀分布的100只，可以在 Long/Short Count的数值中看出。因为二次power改变了rank的均匀分布，使近原点部分的斜率降低，如前文的power分布图所示。

最后我好奇如果仅通过power把rank拉到更高的次数来提高表现，是否也可以达到提交标准？


> [!NOTE] [图片 OCR 识别内容]
> 1
> C
> d
> C
> T
> T
> 4
> TESULTS
> IsR
> C
> CITTNISNA
> Co
> N
> Chart
> Ucucr*
> ITN 7
> Ngut
> 1E
> T
> TUeAIN
> 4TUTA
> UCA
> JRUNAIC@
> Ia
> aUaTs
> Ot Nsls
> SNholo
> go
> A
> turTVI
> ToLuotshsout  1i54
> 61
> por ( rnh |nt rmr5
> ROUP Crutrl2sIml
> LJCCTIm
> b。1 '1
> 3L`
> Cscer1
> 70
> Toa
> UILIe Uu



> [!NOTE] [图片 OCR 识别内容]
> 叫
> IS Summary
> Stage
> 0S
> Aggregate Data
> Sharpe
> TUrnVer
> Finess
> Returns
> Drawdown
> Margin
> 2.75
> 11.749
> 4.18
> 28.909
> 8.889
> 49.249000
> Year
> Sharpe
> Tumover
> Fitnoss
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 3.30
> 11,535
> 5,13
> 30.7730
> 3.593
> 53.36
> 1383
> 767
> 2012
> 3.43
> 11.3197
> 5.12
> 27.039
> 4,2335
> -7.72
> 1489
> 807
> 2013
> 2.79
> 12,4593
> 2.21
> 23.529
> 4.319
> 25.77
> 1529
> 352
> 201
> 2.48
> 12.551
> 3.13
> 20.6030
> 6.5235
> 32.83:
> 1517
> 872
> 2015
> 292
> 13.1393
> 55
> 31,359
> 5.35
> -3.52:
> 15-9
> 339
> 2016
> 3.3
> 11,6633
> 5,41
> 32.8590
> 5,7155
> 56.37
> 1717
> 952
> 201
> 36
> 10.9615
> 105
> 39.47
> 5.085
> 3377
> 19_1
> 1039
> 2013
> 2.33
> 10.639
> 2,56
> 31,279
> 5.259
> 58.36
> 1952
> 1052
> 2019
> 3.80
> 11.525
> 6,83
> 41,023
> 8.1035
> 71.22:
> 1937
> 1065
> 2020
> 0.71
> 11.7_97
> 0.5-
> 10.189
> 8,383
> 17.3:
> 1932
> 1079
> 2021
> 5,00
> 10.6635
> 11,64
> 67.7530
> 1,563
> 127.12
> 1979
> 1045



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> IS
> 05
> 10PASS
> Sharpe 012.7515above CUOffOr 2.07.
> Fitness Of 4.18is above CUtOffOf1
> Turnover of 11.7496is above cutoff of 196。
> Turnoverof 11.749615 below cUtOff of 7096
> Welgntis well distributed overinstruments。
> Rerurns Of 28.90961s above Cutoff oi 896
> Sub-universe Sharpe Of 2.38 is above CUtOffOf 1.68.
> Robust universe Sharpe Of 1,98is above CutOff OT 1.10 (4036 OTAlpha)。
> Robust unierse returns Of 12.0796 isabove CUtOffOf 11.5696 (403 OiAlphaj
> IS ladder Sharpe Of 2.51 is above CUtOff Of 2.37 for ladder year 4: 2/18/2021...2/19/2017.
> MURNNG
> 3 PENDING


如我所料，事实证明这样得到的表现更好！

---

### 评论 #2 (作者: WL13229, 时间: 2年前)

非常经典的案例教学。可以作为如何improve robust universe的经典案例

---

### 评论 #3 (作者: ZY44667, 时间: 2年前)

请教一下，Robust Universe Return检测是在测什么？

---

### 评论 #4 (作者: KJ42842, 时间: 2年前)

[ZY44667](/hc/en-us/profiles/16101087052439-ZY44667)

Robust Universe Return 是在评估alpha在中国真实市场中有限的做空渠道下的表现，而pnl显示的回测表现是所有股票都可以按alpha值做空的理想环境中的表现。

---

### 评论 #5 (作者: ZY44667, 时间: 2年前)

> Robust Universe Return 是在评估alpha在中国真实市场中有限的做空渠道下的表现，而pnl显示的回测表现是所有股票都可以按alpha值做空的理想环境中的表现。

感谢解答，明白了

---

### 评论 #6 (作者: JY65385, 时间: 2年前)

图片里的字好小，图片为什么放不大？

---

### 评论 #7 (作者: KJ42842, 时间: 2年前)

[JY65385](/hc/en-us/profiles/14208769357847-JY65385) 可以ctrl+放大浏览器

---

### 评论 #8 (作者: TT24714, 时间: 2年前)

樓主這篇寫得真好，感謝您的分享

---

### 评论 #9 (作者: ST31184, 时间: 2年前)

感谢分享，很有帮助

---

### 评论 #10 (作者: SK24143, 时间: 2年前)

写的非常精彩

---

### 评论 #11 (作者: NK94992, 时间: 2年前)

I need to teach me🙏🙏

---

### 评论 #12 (作者: LH43889, 时间: 2年前)

Thanks for sharing~

---

### 评论 #13 (作者: LL29756, 时间: 2年前)

现在按照图示代码，最终结果仍是robust universe sharp和robust universe return不达标，请问还有什么方法可以调整使之可以提交

---

### 评论 #14 (作者: PP55193, 时间: 2年前)

每年的市场行情不同，今年有效的Alpha明年可能会失效，该如何进一步提升robust universe sharp呢？像今年多了22年的数据之后此Alpha的robust universe sharp 就又通过不了了，大抵是22年此Alpha有较多做空盈利.....

---

### 评论 #15 (作者: KJ42842, 时间: 2年前)

[PP55193](/hc/en-us/profiles/23422193000343-PP55193)

因子失效来自于量化研究捕捉市场不有效性的本质。该贴的意义不在于提交这个换手率因子，而是在展现通过读论文/研报做量化研究的整个过程，以及让大家理解什么是CHN市场的robust universe。提升robust universe的方法本质在于如何做空的盈利是否可以实现，因为现实中在国内做空小微股盈利本来就难以实现。所以在CHN可以多研究和关注通过多头赚钱的Alpha,更具有实际意义。

---

### 评论 #16 (作者: 顾问 WX84677 (Rank 69), 时间: 1年前)

[KJ42842](/hc/en-us/profiles/12429216262167-KJ42842)  精彩，感谢分享！

---

### 评论 #17 (作者: PP47528, 时间: 1年前)

借鉴文中rank和power的方法，果然我的alpha，Robust Universe Return解决了，感谢

---

### 评论 #18 (作者: TL72031, 时间: 1年前)

感谢分享！power + ts_rank 这个想法对我在其他 universe 的 alpha 设计也提供了很大的帮助！

---

