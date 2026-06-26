# [BRAIN LAB实战]记录一次借助Labs优化GLB alpha的过程经验分享

- **链接**: https://support.worldquantbrain.com[BRAIN LAB实战]记录一次借助Labs优化GLB alpha的过程经验分享_34752699977111.md
- **作者**: 顾问 SZ83096 (Rank 13)
- **发布时间/热度**: 9个月前, 得票: 82

## 帖子正文

首先这个alpha的来源，是参考了老虎哥的这个帖子 ： ➡️  [使用MCP来帮助自己手搓Alpha]([L2] 使用MCP来帮助自己手搓Alpha经验分享_34127707784343.md)

**感谢老虎哥的分享！**

想点下earnings数据集，先看了下数据集的字段，发现直接用machine_lib套一二阶，可能不太行，群里咨询了下小伙伴，有热心的小伙伴提示可以参考下这篇帖子。万分感谢！

看了这篇帖子后，我直接原表达式在GLB ，ASI ,EUR回测了下，发现，ASI地区指标ok，但是robust指标 FAIL了，而且robust指标距离pass 的值还是挺大的，就先放弃了。EUR基本没有信号，而GLB地区的，信号还是挺强的，如下：


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 0.96
> 6.21%
> 0.38
> 1.99%
> 4.939
> 6.4096o。
> nulation Settings
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Istrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2013
> -1.28
> 7.13%
> -0.56
> -2.39%
> 2.929
> 6.70%o
> 4735
> 2498
> juity
> GLB
> MINVOLIM
> Fast Expression
> 10
> 0.08
> Statistical
> On
> On
> Verify
> On
> 2014
> 1.36
> 6.01%6
> 0.61
> 2.5596
> 2.0296
> 8.4996o0
> 5114
> 2963
> 2015
> 66
> 5.6996
> 0.90
> 3.66%
> 2.17%
> 12.88%00
> 5307
> 3065
> 2016
> 2.27
> 5.56%
> .33
> 4.31%
> .33%
> 15.49960
> 5163
> 2918
> Clone Alpha 
> 2017
> 1.01
> 6.0796
> 0.35
> 1.5296
> 0.9096
> 5.02%oo
> 5378
> 3017
> 2018
> 43
> 5.46%
> 0.65
> 2.55%
> .25%
> 9.339600
> 5858
> 3211
> 2019
> 1.34
> 6.78%
> 0.64
> 2.82%
> .26%
> 8.329600
> 5571
> 2843
> Chart
> Pnl
> 2020
> 0.42
> 7.44%
> 0.11
> 0.91%
> .60%
> 2.449o0
> 5755
> 2983
> 2021
> 0.38
> 6.52%
> 0.10
> 0.9396
> 2.4996
> 2.859oo
> 6772
> 3857
> 2022
> 2.26
> 5.62%6
> 51
> 5.5696
> 2.239
> 19.78900
> 6695
> 3573
> 2023
> 4.23
> 5.76%
> -4.65
> -15.08%
> 0.92%
> 52.36900
> 5948
> 3337
> OOOK
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.48
> 2.19%
> 0.11
> 0.63%
> 3.169
> 5.7890
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
> APAC
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.12
> 2.60%
> 0.39
> 1.49%
> 1.80%
> 11.46%o。
> Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> EMEA
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.19
> 1.43%
> -0.02
> -0.139
> 2.539
> -1.859oo
> IS Testing Status
> Period
> IS
> 0S
> Correlation
> 5 PASS
> Self Correlation
> Maximum
> Minimum
> Last Run:
> 5 FAIL
> Sharpe of 0.96 is below cutoff of 1.58_
> Fitness of 0.38 is below cutoff of 1.
> AMER Sharpe of 0.48 is below cutoff of 1 _
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> EMEA Sharpe of -0.19 is below cutoff of 1_
> Sub-universe Sharpe of 0.33 is below cutoff of 0.34.
> 2year Sharpe Of 0.78 is below cutoff of 1.58。


接下来是尝试优化指标

# 1. 修改了下neu 为country后，达到ppa的指标（prod 相关性0.9+），如下，但是三条pnl线中，EMEA 线偏离比较大，sharpe -0.35


> [!NOTE] [图片 OCR 识别内容]
> Ayreyoe Dul
> Sr
> Turno
> Timy
> IIII
> OrAJon
> 1.13
> 2.3696
> 0.65
> 4.1396
> 7.2896
> 35.01900
> Simulution Settings
> Yo
> Shalne
> Turnoe
> Cness
> Rewns
> Urawuown
> Varon
> Lorg Caun
> Short Coun
> Intruneny
> Rog
> Uoga
> LNoUop
> Dca
> Olay
> TNNton
> Noulrolizolon
> Paslourizo
> NN Hno
> Unt Handling
> A Troda
> 2OI」
> 072
> 2
> 0.30
> 222
> JO
> 1
> 65
> o
> [qu
> GR
> MIOCI
> ClEpon
> Og
> CormryRewon
> Q
> Q
> Uerily
> ON
> 70
> 11
> 12
> Osn
> 335
> 11
> 7
> TO
> R0
> 2s
> 021
> 113
> OO
> 103
> 576
> +1 C
> 7191
> 1022
> 2016
> 281
> M
> 258
> 976
> 69
> 16]12
> 699
> 952
> Clone Aloha 
> 101
> 75
> 067
> 31
> 195
> S3SC
> 71
> 105
> 2018
> 093
> 0.96
> 5
> 26
> 1093
> 767
> 1
> 1019
> 355
> 081
> !
> 166
> 0
> 725
> 978
> Chart
> pnl
> 2020
> 055
> 95
> @
> 35
> 302
> 470
> 769
> 979
> 2021
> 159
> 311
> 11a
> 6!
> 260
> 4145
> 8
> 120
> 2022
> 231
> 9
> 192
> 893
> 405
> 4512
> 49510
> 1519
> 002
> 3
> 1.55
> 0
> 1495
> 129*
> 412586
> 7957
> 927
> 20oor
> AMER
> ARsregote Dat
> SC
> Turnoc
> I(
> Aelurn
> Oruny
> UII
> 0.78
> 0.7496
> 0.26
> 1.39%
> 5.0196
> 37.3990o
> O
> 2015
> OU
> 2017
> 2015
> 2019
> 2020
> 2021
> 0
> 0
> APAC
> ARIrCRC Dt
> SLJF
> Turnoyc
> TIt
> Relurn
> Orondoy
> 1,21
> 1.1196
> 0,61
> 3.2296
> 3.9596
> 57.929606
> OL
> RIsk Neutrallzed pnl
> Investability Constralned Pnl
> ANER Pnl
> APACPnl
> EMEAPL
> JA
> TORVDa
> SI
> Turnoyc
> Tr
> Retyrny
> OrondOAT
> URN
> -0.35
> 0.509
> -0.07
> -0.4996
> 7.579
> -19.379600
> IS Testing Status
> Perod
> 15
> 
> Risk neutralized
> ARsregute Data
> Sc
> Twoe
> Te
> RIn
> Oroog^
> Im
> 0.52
> 2.3696
> 0.14
> 0.899
> 4.9296
> 7.53900
> 70455
> WARNING
> SNOIC0'1.13oelow Cuollo' 1.58
> Investability constrained
> Flnessal 0.65,s LtIow Gtolal 1
> ARIrCgote Daw
> SI
> TUno
> TIt
> Relyrn
> Orodon
> U
> A Rsrprof07815bdlow cutolfol 1
> 1,16
> 2.0396
> 0.68
> 4.2696
> 6.4496
> 41.90806
> EMEA Shrpeol 0JSis below cutolfol1
> LII
> U


# 2. 初步尝试了下修改settings参数和 操作符参数，没有改善。考虑到这条线明显和其他pnl线偏离比较多，怀疑是不是异常值导致的，于是我去lab看了下数据的一些可视化指标，发现，关于最高覆盖率 top5的股票，有一个明显和其他值差距过大的，如下：


> [!NOTE] [图片 OCR 识别内容]
> @
> @ $::O
> 田曰, 爷
> 圃
> How do the ern3_pre_interval Values change over time for the top 5 instruments with the highest coverage?
> 2I~2
> EQ0000000000745862
> EQ0000000000799175
> EQ0000000001767064
> -500
> EQ0000000002458219
> EQ0000000002546993
> -1000
> 詈
> -1500
> -2000
> 2500
> 201
> 2016
> 2018
> 2020
> 2022
> Date
> This plot can help you identifytrends; patterns; and anomalies inthe raw ern3_pre_interval Values


# 3.  于是想着，是不是排除掉一些明显偏离其他值过大的股票看看

通过if_else 判断小于-512，-252，-120 ...  时，设置值为nan，过滤掉这些值后，再进行其他操作符处理；

经过测试，发现当过滤掉大于-150时，is指标比较好,如下：


> [!NOTE] [图片 OCR 识别内容]
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Sh
> Simulation Settings
> 2013
> 1.45
> 2.51%
> 0.78
> 3.6096
> 1.22%
> 28.62%00
> 5378
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max
> Trade
> 2014
> 1.03
> 1.11%
> 0.42
> 2.099
> 2.35%
> 37.765o0
> 6271
> Equity
> GLB
> MINVOLIM
> Fast Expression
> 0.08
> Country
> Region
> On
> On
> Verify
> On
> 2015
> 0.16
> 00%
> .03
> 0.5496
> 4.06%
> 10.86%00
> 6144
> 2016
> 2.26
> 1.01%
> 50
> 5.4996
> 24%
> 108.95900
> 6019
> 2017
> 49
> 1.07%
> 0.71
> 2.80%6
> 1.24%
> 52.509oo
> 6158
> Clone Alpha
> 2018
> 1.41
> 0.76%
> 0.79
> 3.9296
> 2.07%
> 103.51%0
> 6053
> 2019
> 1.61
> 2.72%
> .04
> 5.26%
> 2.32%
> 38.62900
> 6529
> 2020
> 0.87
> 2.97%
> 0.50
> 4.0896
> 2.96%
> 27.46900
> 7428
> N Chart
> Pnl
> 2021
> 1.79
> 2.20%
> 37
> 7.3796
> 2.50%
> 66.989o0
> 8526
> 2022
> 2.75
> 2.44%
> .58
> 11.019
> 2.57%
> 90.35900
> 8231
> 2023
> -2.76
> 20%
> 2.49
> 10.1496
> 08%
> 68.G0Soo
> 7960
> Z,OOOK
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.18
> 0.579
> 0.48
> 2.10%
> 4.859
> 73.81%o。
> Jan '14
> Jan '15
> Jan "16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> APAC
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.17
> 0.799
> 0.53
> 2.590
> 2.85%
> 65.72%o。
> Pnl
> Risk Neutralized Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> EMEA
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.25
> 0.409
> -0.04
> -0.26%
> 4.970
> -12.899E
> IS Testing Status
> Period
> IS
> 0s
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.83
> 1.769
> 0.26
> 1.21%
> 1.859
> 13.77
> 8 PASS
> AMER Sharpe of 1.18 is above cutoff of 1.
> APAC Sharpe of 1.17 is above CUtoff of 1.
> TurnoVerof 1.76% is aboVe cutoff of
> %
> Correlation
> Turnoverof 1.76% is below cutoff of 70%.
> Weight is well distributed over instruments_
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Sub-universe Sharpe of 0.97 is above cutoff of 0.48.
> 2year Sharpe of 2.18 is above CUtoff of 1.58.
> Pyramid theme GLB/DI/EARNINGS matches with multiplier of 1
> ffective pyramid count for Genius is 1
> 3 WARNING
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Sharpe of 1.37 is below cutoff of
> .58.
> Fitness Of 0.82 Is below cutoff of 1.
> EMEA Sharpe of -0.25 is below cutoff of1.
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> 5 PENDING
> %oo


优化前后的指标对比：


> [!NOTE] [图片 OCR 识别内容]
> is指标
> 优化前
> 优化后
> risk
> 优化前
> 优化后
> sharpe
> 1.13
> 1.37
> sharpe
> 0.52
> 0.83
> fitness
> 0.65
> 0.82
> fitness
> 0.14
> 1.76
> returns
> 4.13
> 4.43
> returns
> 0.89
> 0.269
> drawdowns
> 7.28
> 4.06
> drawdowns
> 4.92
> 1.85%
> margin
> 38.01
> 50.28
> margin
> 7.53
> 13.779600



> [!NOTE] [图片 OCR 识别内容]
> AMER:
> 优化前
> 优化后
> APAC:
> 优化前
> 优化后
> sharpe
> 0.78
> 1.18
> sharpe
> 1.21
> 1.17
> fitness
> 0.26
> 0.48
> fitness
> 0.61
> 0.53
> returns
> 1.39%
> 2.19
> returns
> 3.22%
> 2.59%
> drawdowns
> 5.019
> 4.85%
> drawdowns
> 3.95%
> 2.85%
> margin
> 37.39%0。
> 73.819o。
> margin
> 57.92%。
> 65.72%0。
> EMEA:
> 优化前
> 优化后
> sharpe
> -0.35%
> -0.25%
> fitness
> -0.07%
> -0.04%
> returns
> -0.49%
> -0.26%
> drawdowns
> 7.57%
> 4.97%
> margin
> -19.379o。
> -12.89%o0


# 4. 优化后，turnover比较低了，考虑到之前老师说过，turnover过低的alpha，并不好，且lab中显示，该字段的turnover基本有10%左右，于是想着看看能不能提升下turnover


> [!NOTE] [图片 OCR 识别内容]
> How often do ern3
> pre_interval Values update?
> 
> 0.5
> Llwull
> 2014
> 2016
> 2010
> 2020
> 2022
> Date


参考了下面的这篇帖子的思路， **感谢顾问 QX52484 (Rank 35) 小伙伴的分享！**

[如何利用tvr操作符与alpha起舞]([Commented] 如何利用tvr操作符与alpha起舞论坛精选_34562640928023.md)

利用ts_target_tvr_decay(x, lambda_min=0, lambda_max=1, target_tvr=0.1) 操作符将 **turnover从 1.17% 提高到了4.66%** （参数设置为lambda_min=0, lambda_max=1, target_tvr=0.1） **以及8.14%**  （参数设置为lambda_min=0, lambda_max=5, target_tvr=0.1），同时 **sharpe指标和fitness，returns都得到了显著的提升** ，而且 **prod corr从0.9009下降到了0.7655** ！真是令人惊喜的意外啊（感谢小伙伴在论坛分享的各种帖子！）

参数设置为  **lambda_min=0, lambda_max=1, target_tvr=0.1**  的 alpha指标如下：


> [!NOTE] [图片 OCR 识别内容]
> X Single Data Set Alpha
> E Power Pool Alpha
> Pyramid theme: GLB/DI/EARNINGS X1
> Aggregate Data
> Sharpe
> TVTnOVe
> Fitness
> Rotlrn
> Drawdown
> Margin
> 1.55
> 4.669
> 1.15
> 6.859
> 4.849
> 29.449o。
> Year
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> Simulation Settings
> 2013
> 2.16
> 4.17%
> 58
> 6.66%
> 23%
> 31.98%0
> 5424
> 1797
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 58
> 3.13%
> 0.20
> 1.51%
> 3.61%
> 9.6290
> 6379
> 1698
> Equity
> GLB
> MINVOLIM
> Fast Expression
> 0.08
> Country / Region
> On
> On
> Verify
> On
> 2015
> 0.29
> 3.53%
> 0.08
> 0.97%
> 3.05%
> 5.4820
> 6270
> 2102
> 2016
> 2.13
> 4.36%
> 1.67
> 7.65%
> 1.76%
> 35.0890
> 6109
> 1972
> 2017
> 2.39
> 3.72%
> 60
> 5.57%
> .43%
> 29.9690
> 6281
> 2113
> Clone Alpha
> 2018
> 1.17
> 2.69%
> 0.63
> 3.65%
> 2.09%
> 27.179o0d
> 6176
> 2893
> 2019
> 2.07
> 5.79%
> 7.56%
> 95%
> 26.130
> 6648
> 1766
> 2020
> 1.76
> 6.579
> 83
> 13.51%
> 84%
> 40.51%ooo
> 7584
> 1154
> N Chart
> Pnl
> 2021
> 2.12
> 65%
> 2.04
> 11.53%
> 3.15%
> 40.8590
> 8720
> 1909
> 2022
> 81
> 92%
> 1.72
> 11.23%
> 3.81%
> 32.479o0
> 8570
> 1697
> 2023
> 42
> 7.31%
> 25
> -9.72%
> 55%
> 26.60oood
> 8187
> 1097
> OOOK
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.31
> 1.51%
> 0.77
> 4.279
> 6.449
> 56.409oo
> OOOK
> APAC
> Aggregate Data
> Sharpe
> Turnover
> FItness
> Returns
> Drawdown
> Margin
> 1.38
> 2.149
> 0.60
> 2.399
> 2.48%
> 22.31%o。
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> EMEA
> Aggregate Data
> Sharpe
> TVnOVe
> CtnPs5
> Returns
> Drawdowr
> Margin
> 0.13
> 1.009
> 0.02
> 0.20%
> 3.949
> 3.949o。
> OS Testing Status
> Period
> 05 
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdowp
> Margin
> 0.70
> 4.66%
> 0.23
> 1.329
> 2.749
> 5.689o。
> 11 PENDING
> l
> Correlation
> Self Correlation
> Maximum
> WinimUm
> Last
> SUn, 09/0712025,1.57 AN
> 0.3290
> -0.0833
> Power Pool Correlation
> Maximum
> Minimum
> La5t
> Run; Sun 09/07/2025,1.57 AN
> 0.3022
> -0.2657
> Prod Correlation
> Maximum
> Minimum
> Last Run: SUn, 09/07/2025,1.56 AN
> 0.7655
> -0.6536
> Long
> RUn


**参数设置为** 

**lambda_min=0, lambda_max=5, target_tvr=0.1 的alpha图如下：**

**
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.55
> 8.149
> 1.14
> 6.81%
> 4.879
> 16.739。。
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> Simulation Settings
> 2013
> 2.33
> 7.48%
> 1.76
> 7.15%
> 1.199
> 19.129600
> 5437
> 1795
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 0.68
> 6.6696
> 0.26
> 1.7796
> 3.4996
> 5.3190
> 6335
> 1742
> Equity
> GLB
> MINVOLIM
> Fast Expression
> 0.08
> Country
> Region
> On
> On
> Verify
> On
> 2015
> 0.17
> 7.32%
> 0.04
> 0.56%
> 3.3796
> 53900
> 6224
> 2148
> 2016
> 2.15
> 7.96%6
> 68
> 7.63%
> 1.709
> 19.
> 79600
> 6082
> 1999
> 2017
> 2.40
> 7.43%
> 1.61
> 5.66%
> 449
> 15.2490。
> 6232
> 2163
> Clone Alpha 
> 2018
> 1.18
> 7.34%
> 0.64
> 3.66%
> 2.05%
> 96%600
> 6148
> 2922
> 2019
> 1.97
> 9.04%
> 49
> 7.19%6
> 98%
> 15.91%0
> 6644
> 1770
> 2020
> 1.72
> 9.1796
> 1.76
> 13.1496
> 4.8796
> 28.64960。
> 7566
> 1172
> N Chart
> Pnl
> 2021
> 2.17
> 8.96%
> 2.11
> 11.7796
> 2.76%
> 26.26%0
> 8710
> 1918
> 2022
> 1.81
> 9.88%
> 1.71
> 11.20%
> 3.87%
> 22.679600
> 8538
> 1730
> 2023
> 80
> 10.84%
> 82
> -12.73%
> 65%
> 23.5096oo
> 8112
> 1173
> 5,00OK
> AMER
> 2,5OOK
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.33
> 2.949
> 0.78
> 4.299
> 5.76%
> 29.149o。
> APAC
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
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.38
> 3.169
> 0.60
> 2.369
> 2.499
> 14.93%。
> Pnl
> Risk Neutralized Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> EMEA
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.11
> 2.039
> 0.01
> 0.169
> 4.01%
> 1.539。
> 41 IS Testing Status
> Period
> IS
> 0s
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.68
> 8.149
> 0.22
> 1.299
> 2.61%
> 3.1796。
> 9 PASS
> Fitness of 1.14 is above cutoff of 1
> AMER Sharpe of 1.33 is above cutoff of 1
> APAC Sharpe of 1.38 is above cutoff of 1
> Correlation
> Turnover of 8.149 is above cutoff of 1%
> Turnover of 8.149 is below cutoff of 709-
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Weight is well distributed over instruments_
> Universe Charne Of 145is
> hOVe Cutoff of0
> Year
> Long
> SUb
**

到此，alpha优化结束。

（可能你会问，我咋提交了turnover较低的那个alpha，只能说：指标过于相似导致我复制错alpha_id了！我发现的时候，程序还在提交，赶紧去页面把description 去掉了，想让服务器提交失败，结果晚了，10几秒就交上去了...... 😭😭😭 ）

---

## 讨论与评论 (14)

### 评论 #1 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

膜橘子姐🍊🍊🍊！很有启发性的worldquantLab实战分享，作为一个还在摸索中的小gold，虽然有些操作细节看不太懂，但您的整个优化思路让我学到了一些东西

1. **了解alpha数据** ：看到Robust指标fail没有直接放弃，而是通过数据可视化精准定位到异常值问题，这个思路真的值得学习；
2. **操作符优化alpha** ：用if_else过滤极端值操作，看到优化前后对比图的时候我有些惊讶，效果也非常不错；
3. **小gold思考** ：考虑到turnover过低的问题，用ts_target_tvr_decay操作符来调节，最终各项指标全面提升，看来这个操作符值得小gold好好学习一下！

最后提交错版本太真实了😂 ，小gold也时有发生这种情况。

---

### 评论 #2 (作者: SZ83119, 时间: 9个月前)

哈哈，最后一段太逗了^_^

---

### 评论 #3 (作者: LR93609, 时间: 9个月前)

来自深圳的盛赞

女神橘子姐，青春永驻，GM高挂

我一直以为ts_target_tvr_decay(x, lambda_min=0, lambda_max=1, target_tvr=0.1)是用来降低turnover的，

过程中用过几次，效果很一般，碰到turnover过大的，用了之后指标一泻千里，就弃置不用了，感觉上很复杂，可能是我生平喜欢简洁，看到这么复杂的一时难以接受，至今也没用过这个。

没想到还可以用来提升turnover，真真是见识了，后面我再碰到turnover过低的，尤其在1%附近的，一定要试验一下。

之前碰到类似的问题，都是调decay，或者是上power增强，今天又发现一个新的途径

------------------------------------------------------------------------------------------------------------------

凡事发生，皆利于我；愿我所愿，尽是美好

------------------------------------------------------------------------------------------------------------------

---

### 评论 #4 (作者: AH18340, 时间: 9个月前)

感谢橘子姐的分享，之前以为ts_target_tvr_decay这个是降低turnover的，没想道还能升turnover,真是学到了。

但是这步通过if_else 判断小于-512，-252，-120 ...  时，设置值为nan这个会不会是在做拟合的行为。

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #5 (作者: 顾问 QP72475 (Rank 84), 时间: 9个月前)

感谢，正在学习lab。

---

### 评论 #6 (作者: BL72197, 时间: 9个月前)

非常有用，我也是通过ts_target_tvr_decay来提升turnover的方法来救活了死鱼，然后提交了，感谢大佬分享！！！

---

### 评论 #7 (作者: AM12075, 时间: 9个月前)

通过if_else 判断小于-512，-252，-120 ...  时，设置值为nan，过滤掉这些值后，再进行其他操作符处理。能否说一下这里具体是怎么过滤的呢。lambda_min=0, lambda_max=5, target_tvr=0.1 ，另外lambda_max的含义是什么呢？设置成5有什么特别的原因吗，和1相比有很大变化吗？

=============================================================================

---

### 评论 #8 (作者: 顾问 SJ65808 (Rank 20), 时间: 9个月前)

感谢大佬分享，ts_target_tvr_decay居然还能这么用，真的很有启发

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #9 (作者: 顾问 MS51256 (Rank 28), 时间: 9个月前)

感谢橘子姐的分享，橘子姐写论文真可爱哈哈哈

ts_target_tvr_decay 这几个降低tvr的op 我感觉效果都不是很好

可能是我使用的方法还存在问题，感谢楼上的分享 我去实操试试

==========================================================
==========================================================

---

### 评论 #10 (作者: 顾问 MZ45384 (Rank 51), 时间: 8个月前)

"通过if_else 判断小于-512，-252，-120 ...  时，设置值为nan，过滤掉这些值"

真的学到了，原来可以这样处理极端值， ts_target_tvr_decay我也一直在用，自从看到起舞那篇帖子后。

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #11 (作者: JQ70858, 时间: 7个月前)

想要降低操作符，搜到了这里。要学的还很多。。感谢分享。

---

### 评论 #12 (作者: MZ35432, 时间: 7个月前)

“通过if_else 判断小于-512，-252，-120 ...  时，设置值为nan，过滤掉这些值后，再进行其他操作符处理”

我想问问这里的小于的这些值是从哪里得到的？我看了下图两眼一抹黑 不知道这些值从哪里来的？

---

### 评论 #13 (作者: HL64570, 时间: 5个月前)

感谢分享，Brain Labs真的非常有用！ 我最近已经离不开它了。

---

### 评论 #14 (作者: FF65210, 时间: 5个月前)

感谢橘子姐的分享，我想开GLB区的alpha了，正开始摸索中，您的经验给我很大的帮助，tur这个操作符我确实用的很少，学习了。

---

