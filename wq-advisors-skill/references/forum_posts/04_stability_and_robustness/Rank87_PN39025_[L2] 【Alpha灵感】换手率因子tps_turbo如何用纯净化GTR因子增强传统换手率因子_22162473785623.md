# 【Alpha灵感】换手率因子tps_turbo：如何用纯净化GTR因子增强传统换手率因子

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】换手率因子tps_turbo如何用纯净化GTR因子增强传统换手率因子_22162473785623.md
- **作者**: WM13885
- **发布时间/热度**: 2 years ago, 得票: 14

## 帖子正文

**Reference:**

1. 东吴证券：换手率变化率的稳定 GTR 选股因子绩效月报 20240229

2. 东吴证券：《换手率变化率的稳定 GTR 因子——助推换手率的所有家族成员》

**核心交易idea**

- 文章表明，GTR(The Stability of the Growth Rate of Turnover Rate) ，即“换手率变化率的标准差”，是基于换手率变化率具有加速意义的同时，为其构建稳定性的新换手率因子GTR不仅能够提供换手率变化率平均值所不能提供的信息，同时也能够覆盖大部分平均值带来的信息，以下为构建方式：


> [!NOTE] [图片 OCR 识别内容]
> 基于换手率变化率所具有的加M度意义,
> 再加上裁们所构建因子具备的稳定性,
> 们称新因子为换手率变化宰的稳定 GIR。 新因子最终的构建方式如下:
> 1)
> 每一交易日,计算每#换手率娈化率-今#换手率1昨日换手率 1;
> 2)
> 每月月底。回溯所有股禀过去20个交易日,计算20个交易日的换手率变化率
> 的标准差:
> 每只般票。得到换手率变化率栋准差后,再做横截面市值中性化处理
> 即为所
> 有股栗当月的因子值 GIR(Ihe Stability of the Groith Rate of Tutorer Rate)。


- 纯净优加法

将使用GTR因子对传统换手率因子Turn20，即20日换手率均值，做提纯。

1. 第一步


> [!NOTE] [图片 OCR 识别内容]
> 纯净优加法的具体步骧可分为两步=
> 第一步是对因子做日频层面的纯净化:
> (1)  纯净化换手率(甘频):去除换手率中与换手率变化率相重合部分的信息。洚
> 日度的换手率因子作为因变量 (y); 日度的换手率变化率因子作为自变量 (8)。每天在


**
> [!NOTE] [图片 OCR 识别内容]
> 全祥本做带截距项的一元线性回归。
> 回归方程即: y-atbxtE。
> 回归后
> 取出每天的残差
> 部分。作为当天的纯净化换手率值。即去除了换手率变化率影响后的传统换手率_
> (?)
> 纯净化换手率变化率
> (日频):  去除换手率变化率中与换手率相重合部分的
> 倍息。将日度的换手率变化宰因子作为因变量(y),日度的换手率因子作为自变量(8),
> 每天在全样本做带崴距项的一元线性回归
> 回归方程即: sFatbxtc。 回归后。取出每天
> 的残差部分一
> 作为当天的纯净化换手率娈化率值,即去除了换手率影响后的换手率变化
> 率
**

关键为a0 = 日频换手率因子，b0=日频换手率的变化率因子，相互使用回归方程，剔除重叠信息，拿到提纯后的a1和b1。

2. 第二步


> [!NOTE] [图片 OCR 识别内容]
> 纯净优加法的第二步,
> 是用纯净化后的日频换手宰。换手宰变化率计算新的纯净因
> 子
> Iu?O. SIR, GIR
> 并相加。对于 IPS_Iurbo 来说:
> (1)8月月底:
> 回溯所有股票过去20 个交易日;计算20个交易日的纯净换手率
> 的平均值一一纯净 Tunz0:
> (3)8月月底:
> 回溯所有股票过去 20 个交易日 =
> 计算20 个交易日的纯净换手宰
> 变化率的标准差一
> 纯净 GIR;
> (3)每只股禀
> 得到纯净月度因子后。
> 再做横截面市值中性化与横截面栋准化处
> 搜
> 洚纯净 Tunz0 与纯净 GIR 等权相加
> 侵得到了 IPS_
> Turbo_


**数据**

换手率 = volume/sharesout ，这里volume的数据集为可代替数据

例如：

pv27_buy_volume_med_order

pv27_buy_volume_small_order

**Universe**

CHN Equity Top3000

**Neutralization**

Industry，文章表示换手率因子受行业风格及板块影响，后面测试确实industry是表现最好的。

**Operator**

文章明确提到提纯概念，并且提供了相应的方程，可以发现与brain平台的regression_neut operator相似，其次，文章中多次提到需要对截面做市值的中性化处理，所以对提纯后的两个换手率因子再次对市值提纯，并在最后做了group_neutralize处理

**绩效**

Turn20：

**
> [!NOTE] [图片 OCR 识别内容]
> Egate Data
> Sharpe
> TUITNTI
> Fitmac
> TTITT
> Drawidor
> Maren
> 2.13
> 4.3796
> 3.01
> 24.96%
> 18.5996
> 114.249000
> Year
> Sharpe
> Tumower
> Fitress
> Returs
> Drawdown
> Margin
> Count
> Short Count
> 2712
> 3.10
> -5:
> .2
> 5.01%
> 120.25:
> 1573
> 2713
> 2.20
> 327:
> 3.01
> 2.-5
> 1.97%
> 121.325:
> 13
> 271-
> 2.71
> ?
> 3.5
> 2.35
> 5.773
> 115.355:
> 1131
> 34
> 715
> 1.9
> JJ
> 0.78
> 1
> 5
> 2.3;:
> 1
> 133
> 2716
> _.3
> 一|
> 470
> 32.12沾
> 3.65
> 153.355:
> 16-
> 2717
> 2-
> 35:
> 3.7
> 5.753
> 155.225:
> 271
> 2713
> 一 |o
> 47
> 33
> 11.-5:
> 133
> 17
> 2713
> 2.7
> 一3:
> 375
> 2.4:
> 1.73
> 13!0
> 1_3
> 134
> 2727
> 1.25
> 一73:
> TE4
> 3.11%
> EZ.SZt:
> 132
> 1335
> 2721
> 11
> 一:
> 2.41
> 24.06沾
> 3.733
> 102.455:
> 12
> 13
> 212
> E.J
> SS:
> 143
> 5.2:
> 32.3;:
> 132
> 1122
> 医 Correlation
> Self Correlation
> Hiehest Crrelazion
> L52 RUI: -
> Prod Correlatlon
> Hishes Correlaton
> L52 RUI: -
> 回 |5
> Testing Status
> PuSs
> Sarpe Of 2.1315above CUCOf of 2.07.
> Ftness cf 3.01
> a3OE ~UtCff of 1
> Tmoercf4 37%
> EbOVE CUCOff of 1%.
> Tomoe cf
> 37%
> below Cutoffof 70%
> Weisht
> JsribUed OVETins ruMets。
> RETUTRS Sr 24.9696
> 3OU'
> CUtCTof 8%。
> Sub-unierse Sharpe of 1.97is aDOVE CUtOff Of 1.3.
> RObUSt UniVersE Sarpe Of 1.65
> above CUtOf of 0.85 {4036
> JIpj。
> Robs:Universs rEtUrnsCf 10.3796
> aDOVE SU?Cff of 
> 989 {4055 Of Alpna)
> FAIL
> 15 ldder Snarpe Of 1.70is below CUtoff of 2.07 for ladder year
> 1/24/2022.
> 1/25/2020
> AeBT
> Lomg
**

**经过GTR增强后的Turn20，即TPS_Turbo：**


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Sharo
> TUTTTU
> HIUTSS
> TUTTS
> LTWOO
> IT3IT
> 2.29
> 4.3990
> 3.35
> 26.77%
> 11.339
> 121.859000
> Year
> Shamps
> Tumover
> Fitness
> Returs
> Orawdown
> Margin
> Long Count
> Short Count
> 2712
> 1 
> 一33
> 4-
> 二.4
> 一35
> 125.575:
> 1_3
> 371
> 2713
>  
> 35
> 73
> 2.54:
> 5.13
> 11.53沁:
> 157
> 3
> 71-
> 4.14
> 35.32
> 一
> 11汇:
> 133
> 8[
> 2715
> 43:
> 240
> 19.3沉
> 311
> 85.75:
> 14
> 1312
> 2715
> 77:
> 34.3沿
> 57
> 153.24;:
> 534
> 3337
> 2717
> .5
> 一2
> 44
> 3.31:
> 5.3
> 152.3;:
> 133
> 2713
> 2.1
> -31
> 3.01
> .12
> 7.21%
> 125.265:
> 2371
> 2713
> 2.35
> 23.15沽
> 1.33
> 123.705:
> 13-
> 1351
> 2727
> 一7:
> T.54
> 37
> _1
> 1910
> 13
> 2721
> TET:
> 47
> 4.7:
> 3.3
> 135.375:
> 11
> 133
> 2122
> 6.3
> ZE:
> 74.35
> 1.73
> 235.52t:
> 1325
> 1TE
> Correlation
> Self Correlation
> HiEhest Correlation
> TI
> Prod Correlation
> Hiahest Correlaton
> TI
> IS Testing Status
> PuSs
> FAIL
> I5Idde-STErDE of 1.7215 below CUtaff Of 2.07 for ladoEr _
> ES「2-1/24/2022...1/25/2020
> WJRNNG
> PENDING


可以发现各项指标有了更好的提升，最大回撤也缩小了。 **然而，可以发现 IS Ladder Sharpe 表现在20年和21年的表现并不如意，可以通过使用不同的成交量数据字段来改善。**

之后虽然在IS Ladder Shape 过了，但无奈发现prod corr 略高：


> [!NOTE] [图片 OCR 识别内容]
> 1 SUmmary
> Period
> Aggregate Data
> Snarpe
> TUITNTI
> Tnes
> TsTITT
> TaOITTT
> Marein
> 2.11
> 5.109
> 3.01
> 25.37%6
> 10.28%
> 99.470000
> Year
> Sharpe
> Tumover
> Fitness
> Returs
> Drawdown
> Long Count
> Short Count
> 2712
> 5-7:
> 42
> .2
> 5.15
> 34-3:
> 81
> JIE
> 2713
> 5C:
> 1.51
> 15.4
> 5.31
> 76.275:
> 5-3
> 271-
> 5.75:
> 472
> T.JE:
> 一57
> 34.5t:
> 54
> 2715
> 11
> E
> .E:
> 5.373
> 57.35:
> 54
> 2716
> 553:
> 430
> 34.3
> 5.23
> 12.14:
> 1-s
> SS
> 2717
> 2.2
> 55:
> 25.5
> 3.37
> 3.31:
> 177
> 2713
> 57
> 72.3:
> 3.33
> 174.3汇:
> 133J
> 1373
> 2713
> Es:
> 430
> 3
> 17.7
> 114.275:
> 13T
> 12
> 2127
> EC:
> 27.35沾
> 5
> 9:
> 135
> 175
> 2721
> 1.75
> 35
> 22
> 2.54
> 11.35
> 35.175:
> 1352
> 1354
> 272
> EZI
> JE:
> 14 
> 5。
> 53
> 133.525:
> 137
> 1353
> 医 Correlation
> Self Correlation
> Hizhest Correlation
> L35t RuT -
> Prod Correlation
> Hiahest Correlaton
> L35t RuT -
> IS Testing Status
> 12P455
> STErOE Of2.11
> aboy2 CUOfr or 2.07
> Fitness cf 3.01
> aDOVE CUtOffof1.
> TomoverOf
> 10%
> EbOVE CUCOff or 1%.
> TomoverOf
> 10%
> BElCtTcf 704。
> Weisht
> Jisribued OWETinsruTets。
> REUrns  25.3790
> 3bOWE ~UtCTof 8%
> Sb-UnNErse Sharpe Of 1.99
> aDOE SUtOffof 1.29_
> Rob_s:UTierse SETE Of
> above CUtOf of 0.84 {4056 Of Alpnaj
> Robost UniErsE
> EtUTRs Of 12.06%
> aDOVE ZUOff of 10.15% [40沁 Of Alpnal
> Selfcorrelaton
> 5027
> belowy SUOffof0.7
> Jpha subTissions
> BEIOWI
> adder Sarpe Of 2.12
> above CUtOf Of 2.07 for ladderEar 7: 1/24/2022
> 1/25/2015.
> FAIL
> Prod correlation 0.8172is abOVe CUtoff of 0.7and Sharpe not better by 10.0%
> MorE
> Wargin
> Uo-


其实换手率因子作为常见因子得到这个结果很正常，在近3年出现失效的比比皆是，最后通过微调能够达到Prod_corr 0.8左右的alpha有五六个（在微调中发现，大部分情况下能够通过增加GTR/减少Turn20的权重来实现IS Ladder Sharpe提升，但是总体表现水平均降低，也就通过牺牲前期回测水平，提高后期水平来满足条件）。比较固执，但怎么也操作不到0.7以下。于是突然想起bootcamp提到过CHN的很多因子在KOR也适用，于是转变了下思路，看下其他universe的可能性，最终成功提交alpha。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST
> Region
> Universe
> Sharpe
> Retums
> Tumover
> Search
> Select
> Select
> Select
> Search
> Select
> Select
> e-吕>
> e-吕>
> e-吕> |
> Select
> alpha_Ps_trbO
> RsEUET
> ACTNE
> 03118/2024EOT
> KO
> TOPGOD
> Tag
 
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Th3=
> TICTUIIE
> Ftmc
> TeTIIn
> T
> 1.97
> 10.029
> 2.8
> 25.40%
> 21.089
> 50.6
> Year
> Shame
> Tumower
> Fitness
> Returs
> Orawdown
> Margi
> Long Count
> Short Count
> 212
> ZE5
> 1JEJ:
> 47
> 4-:
> 1.23
> 7E 239:
> 23
> 213
> 1137:
> 1.TE
> 15-2:
> 1.2
> 333:
> 11』
> E3:
> 10:
> 5.63
> 73.11:
> 212
> 315
> 1705:
> 1.-5
> 13.73:
> 3.33
> 3 :
> 316
> 33
> 1E3
> 3
> 38:
> 2717
> 17.47:
> .s
> 475:
> 7.57
> 055:
> 33
> 2713
> 132:
> 15.E7:
> 15.73
> 173:
> 2S
> 213
> ES:
> 1.1E
> 1301:
> 5.33
> 2654:
> 4
> 227
> 31
> CS:
> .30
> 05:
> 5.723
> 76.515:
> 2721
> 53:
> .10
> 3553:
> 5.3
> 7 :
> ZSE
> 22
> 3Ei:
> 332
> 12225:
> 7.53
> 38553f:
> 3TE
> 25
> 11216"


---

## 讨论与评论 (2)

### 评论 #1 (作者: ZM32460, 时间: 2 years ago)

感谢你的分享。 你能分享一下 alpha 表达式吗？ 谢谢

---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

感觉做得有点急躁了，template过于简单，可能大概率无法过滤出有效的信息。还需要更多努力

---

