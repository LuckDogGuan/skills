# 顾问 YH55729 (Rank 42) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 YH55729 (Rank 42) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] EUR TOPCS1600的经验解决Robust universe Sharpe  Sub-universe Sharpe  Weight concentration 问题经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (XW90844)**:
EUR TOPCS1600是最近新开放的炙手可热的universe。然而回测中经常遇到几个典型的问题：

- Robust universe Sharpe of 0.xx is below cutoff of 0.70.
- Sub-universe Sharpe of xx is below cutoff of 1.xx.
- Weight concentration xx% is above cutoff of 10% on mm/dd/yyyy.

尤其对新顾问，如果只看官方文档的解释和建议，更是一头雾水。但很多做过IND region的老顾问都明白，这是由于新区的数据覆盖率不足导致的，这次的TOPCS1600也是同理。这类问题很多靠ts_backfill和group_backfill就能解决。关键是 **分清到底是数据在哪个维度上覆盖率不足** 。

## **1. Date Coverage不足：用ts_backfill解决**

举例，imb5_score这个字段，Coverage 55%，Date coverage 100%，回测有warning “Weight is too strongly concentrated or too few instruments are assigned weight.”，表面看似乎是股票数量覆盖率不足。

但打开Visualization Chart中的Coverage Of Universe，可以看到实际覆盖率并不低（每天都在1300只股票以上），而是有特定的几天覆盖率为0。 
> [!NOTE] [图片 OCR 识别内容]
> Code
> imb5
> SCOre
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
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast
> Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> Chart
> Coverage Of Universe
> 1,000
> 500
>  Jul '14
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
>  Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
>  Jul '23
> Jan '24
> IS Testing Status
> Period
> 15
> Os
> 8 PASS
> 5WARNING
> Weight is too strongly concentrated ortoo few instruments are assigned weight。
> Delay


这种情况，简单的ts_backfill就能解决这个问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> ts_backfill
> imb5_score,
> 63)
> Simulation Settings
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
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> N Chart
> Coverage Of Universe
> 1,500
> 1,400
> 1,300
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> JUl'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul'20
> Jan '21
> Jul '21
> Jan '22
> JUl '22
> Jan '23
> Jul '23
> Jan '24


## **2. 股票数量Coverage不足：用group_backfill解决**

这是另一个基本面字段组合，回测报Robust universe Sharpe和特定日期Weight concentration问题。用同样的方法检查，发现时间序列上覆盖率没明显问题，但整体股票数量覆盖率较低（每天在800~1200只之间）。 
> [!NOTE] [图片 OCR 识别内容]
> reverse(ts
> std
> de
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUPIOIP|
> Ftness
> Returns
> OraMIdoINn
> Margin
> Simulation Settings
> 1.14
> 1.499
> 1.63
> 25.41 %
> 26.159
> 340.31%00
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
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.80
> 2.4396
> 5.58
> 49.6796
> 9.959
> 408.0096o
> 796
> 2015
> 1.79
> 1.19%
> 3.19
> 39.81%
> 12.20%6
> 667.149600
> 774
> 107
> Clone Alpha
> 2016
> 0.72
> 9896
> 0.82
> 16.1096
> 19.4490
> 162.339600
> 757
> 141
> 2017
> 68
> 1.0296
> 2.31
> 23.5596
> 9.159
> 459.639600
> 865
> 143
> 2018
> -0.97
> 8796
> '23
> -20.0796
> 25.73%
> 214.999600
> 872
> 165
> Chart
> Coverage Of Universe
> 2019
> 1.71
> 1.3796
> 80
> 33.5096
> 12.5096
> 487.519600
> 829
> 148
> 2020
> -016
> 0.849
> 10
> -5.0990
> 20.0796
> -121.119600
> 927
> 2021
> 49
> 0.6096
> 2.47
> 34.2496
> 13.5096
> 1,137
> 69600
> 954
> 24
> 2022
> 2.19
> 2.16%
> 09
> 67.56%
> 13.83%
> 626.759600
> 870
> 159
> 000
> 2023
> 0.92
> 1.4196
> 0.92
> 12.3996
> 14.989
> 176.239600
> 786
> 239
> 950
> Risk neutralized
> 900
> Aggregate Data
> Sharpe
> TITnOIe
> Fitnesc
> Retlrns
> OrlNdOWI
> Margin
> 0.60
> 1.499
> 0.58
> 11.849
> 28.239
> 158.549600
> 850
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> 22
> Jan '23
> Jul '23  Jan '24
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> 1 FAIL
> Robust universe Sharpe of 0.49 is below cUtoff of 0.70
> 5 WARNING
> Performance Comparison
> Sharpe of 1.14is below cutoff of 1.58.
> Weight concentration 36.81%
> above cUtoff of 10% on 4/12/2016.
> Rrln
> UVuAM
> Jul"


尝试应用ts_backfill后，也发现并不能增加覆盖率，Robust universe Sharpe也未改善。这就需要group_backfill了。

group_backfill(alpha, country, 126)，这种方式对覆盖率提升最多，但这种回填方式较糙，未解决Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts
> std
> deV
> group_backfill
> ts_backfill
> 126), country,
> 126 )
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TITnOVe
> Fitness
> Returns
> OraMdOINI
> Margin
> Simulation
> Settings
> 1.14
> 1.349
> 1.46
> 20.639
> 29.699
> 308.739600
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
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.70
> 2.4896
> 80
> 39.489
> 8.0996
> 318.249600
> 1097
> 256
> 2015
> 1.97
> 1.1396
> 3.14
> 31.699
> 9.1196
> 559.409600
> 1023
> 337
> Clone Alpha
> 2016
> 0.52
> 1.4190
> 0.35
> 5.5396
> 10.30%
> 78.759600
> 1062
> 315
> 2017
> 55
> 0.919
> 83
> 17.3896
> 8.439
> 381.309600
> 1214
> 290
> 2018
> 0.04
> 1.42%
> 0.01
> 0.70%
> 14.79%
> 889600
> 1318
> 228
> N Chart
> Coverage Of Universe
> 2019
> 66
> 1.1696
> 2.44
> 27.0696
> 8.6596
> 467.549600
> 1236
> 293
> 2020
> 42
> 1.15%
> 42
> 12.259
> 21.15%
> -213.929600
> 1315
> 248
> 2021
> 1.32
> 0.5596
> 2.06
> 30.3096
> 12.3896
> 1,096.429600
> 1505
> 88
> 2022
> 2.55
> 1.8196
> 58
> 59.769
> 7.8196
> 66
> 069600
> 1312
> 269
> 500
> 2023
> 0.33
> 3390
> 0.19
> 4.0290
> 18.3196
> 60.329600
> 1262
> 310
> 400
> Risk neutralized
> Aggregate Data
> Sharpe
> Trnowe
> Fitness
> RotIrn
> DraiNdoir
> Margin
> 0.55
> 1.349
> 0.46
> 8.58%
> 26.229
> 128.379600
> 300
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23
> Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run: -
> Power Pool Correlation
> Maximum
> Minimum
> Last Run: -
> IS Testing Status
> Period
> IS
> Os
> Prod Correlation
> Maximum
> Minimum
> Last Run: -
> 7 PASS
> 1FAIL
> Robust universe Sharpe of 0.56 is below cutoff of 0.70
> Long


group_backfill(alpha, subindustry, 126)，覆盖率中等提升，但这种基本面数据按照行业均值回填明显比按country回填更合理，成功解决了Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts_std_dev
> Eroup_
> backfill (ts
> backfill
> 126), subindustry,
> 126) ,
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnove
> Returns
> Drawdowr
> Margin
> Simulation Settings
> 1.45
> 1.2496
> 1.89
> 21.209
> 20.699
> 341.619600
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
> Max Position
> Equity
> EUR
> TOPCS1G00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.50
> 2.5096
> 4.36
> 37.94%
> 9.2296
> 303.719600
> 981
> 148
> 2015
> 00
> 1.1696
> 2.96
> 27.30%
> 8.2696
> 469.739600
> 1014
> 147
> Clone Alpha
> 2016
> 0.78
> 1.449
> 0.69
> 9.73%
> 11.5596
> 135.269600
> 972
> 195
> 2017
> 80
> 0596
> 2.49
> 23.95%
> 6.7396
> 455.589600
> 1130
> 168
> 2018
> 0.17
> 1.1096
> -0.08
> -2.61%
> 18.3596
> -47.599600
> 1281
> N Chart
> Coverage Of Universe
> 2019
> 2.87
> 02%6
> 98
> 37.66%
> 6.81%
> 738.029600
> 1281
> 90
> 2020
> 0.45
> 0.8596
> 0.35
> 7.55%
> 5596
> 177.659600
> 1269
> 94
> 2021
> 62
> 0.6796
> 2.42
> 27.99%
> 80%6
> 830.179600
> 1349
> 55
> 2022
> 99
> 5896
> 3.15
> 31.31%
> 11.1496
> 395.639600
> 1261
> 121
> 300
> 2023
> 0.81
> .0196
> 0.73
> 10.16%
> 16.939
> 20
> 0096oo
> 1244
> 128
> 200
> Risk neutralized
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> Returns
> DrawdOWn
> Margin
> 0.74
> 1.249
> 0.62
> 8.679
> 19.639
> 139.739600
> 1,100
> JUl'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul'23 Jan '24
> Correlation
> Self Correlation
> MaYimIm
> NIinimrm
> 13c+
> Prn
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> Fitness of
> 89 is above cUtoff of
> Turnoverof
> .24%
> above cUtoff of 1 %
> Turnoverof
> .249
> below cUtOff of 709.
> Sub-universe Sharpe of 1.19 is above CUtOff of 0.77.
> Robust universe Sharpe of 0.79 is above Cutoff of 0.70.
> Fitnes


最后应用group_backfill(alpha, group_cartesian_product(country, subindustry), 126)，取得最佳效果： 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> Os
> reVerse(ts
> std_deV
> Broup_backfill(ts_backfill
> 126)
> group
> cartesian_product (country,
> subindus
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTnOVer
> Fitness
> Returns
> DrawdOWI
> Margin
> Simulation Settings
> 1.45
> 1.339
> 2.15
> 27.499
> 41.009
> 412.659600
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
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.25
> 64%6
> 4.10
> 41.43%
> 9.44%6
> 314.439600
> 898
> 137
> 2015
> 2.28
> 0.8796
> 67
> 32.309
> 10.769
> 738.519600
> 939
> 84
> Clone Alpha
> 2016
> 38
> 51%
> 1.74
> 19.9196
> 8.79%6
> 262.919600
> 844
> 195
> 2017
> 1.46
> 0.6996
> 2.13
> 26.6496
> 8.0396
> 774.909600
> 1046
> 119
> 2018
> 06
> 16%
> .37
> 20.86%
> 9.75%
> 358.649600
> 1143
> N Chart
> Coverage Of Universe
> 2019
> 2.67
> 0696
> 4.97
> 43.2996
> 9.3596
> 818.869600
> 1085
> 94
> 2020
> 1.12
> 0996
> 62
> 26.2996
> 33.209
> -48
> 879600
> 1149
> 2021
> 93
> 5396
> .38
> 38.2996
> 11.2796
> 1,444.509600
> 1211
> 26
> 2022
> 2.43
> 2.4796
> 5.22
> 57.7296
> 9.4696
> 466.629600
> 990
> 252
> 2023
> 0.89
> .2896
> 02
> 16.4996
> 23.889
> 257.429600
> 1065
> 176
> 100
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Returns
> DrawgOWn
> Margin
> 0.80
> 1.339
> 0.80
> 12.639
> 29.099
> 189.549600
> 000
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan "17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23 Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> o
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run: Fri, 02/27/2026,2:32 AW
> 8 PASS
> Fitness of 2.15 is aboVe cUtoff of
> 0.7002
> -0.3901
> Turnover of
> .339is above cUtoff Of 1%.
> Turnoverof-
> .33%
> below cUtoff of 70%
> Sub-universe Sharpe of 1.35
> aboVe cutoff of 0.77 _
> Robust universe Sharpe of 0.82 is above cutoff of 0.70.
> Long


有兴趣的还可以看Coverage by Industry图，限于篇幅就不细说了。总的来说，建议大家对某个idea大规模回测之前，先把各种group fields都用group_backfill试一下，找到最合适的回填方式，再大规模回测。

**顾问 YH55729 (Rank 42) 的解答与建议**:
学到了，之前主要使用调trunication的参数调整weight concertration

=============================================================================


---

### 技术对话片段 2 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] EUR TOPCS1600的经验解决Robust universe Sharpe  Sub-universe Sharpe  Weight concentration 问题经验分享_38669179039255.md
- **时间**: 3个月前

**提问/主帖背景 (XW90844)**:
EUR TOPCS1600是最近新开放的炙手可热的universe。然而回测中经常遇到几个典型的问题：

- Robust universe Sharpe of 0.xx is below cutoff of 0.70.
- Sub-universe Sharpe of xx is below cutoff of 1.xx.
- Weight concentration xx% is above cutoff of 10% on mm/dd/yyyy.

尤其对新顾问，如果只看官方文档的解释和建议，更是一头雾水。但很多做过IND region的老顾问都明白，这是由于新区的数据覆盖率不足导致的，这次的TOPCS1600也是同理。这类问题很多靠ts_backfill和group_backfill就能解决。关键是 **分清到底是数据在哪个维度上覆盖率不足** 。

## **1. Date Coverage不足：用ts_backfill解决**

举例，imb5_score这个字段，Coverage 55%，Date coverage 100%，回测有warning “Weight is too strongly concentrated or too few instruments are assigned weight.”，表面看似乎是股票数量覆盖率不足。

但打开Visualization Chart中的Coverage Of Universe，可以看到实际覆盖率并不低（每天都在1300只股票以上），而是有特定的几天覆盖率为0。 
> [!NOTE] [图片 OCR 识别内容]
> Code
> imb5
> SCOre
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
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast
> Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> Chart
> Coverage Of Universe
> 1,000
> 500
>  Jul '14
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
>  Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
>  Jul '23
> Jan '24
> IS Testing Status
> Period
> 15
> Os
> 8 PASS
> 5WARNING
> Weight is too strongly concentrated ortoo few instruments are assigned weight。
> Delay


这种情况，简单的ts_backfill就能解决这个问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> ts_backfill
> imb5_score,
> 63)
> Simulation Settings
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
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> N Chart
> Coverage Of Universe
> 1,500
> 1,400
> 1,300
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> JUl'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul'20
> Jan '21
> Jul '21
> Jan '22
> JUl '22
> Jan '23
> Jul '23
> Jan '24


## **2. 股票数量Coverage不足：用group_backfill解决**

这是另一个基本面字段组合，回测报Robust universe Sharpe和特定日期Weight concentration问题。用同样的方法检查，发现时间序列上覆盖率没明显问题，但整体股票数量覆盖率较低（每天在800~1200只之间）。 
> [!NOTE] [图片 OCR 识别内容]
> reverse(ts
> std
> de
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUPIOIP|
> Ftness
> Returns
> OraMIdoINn
> Margin
> Simulation Settings
> 1.14
> 1.499
> 1.63
> 25.41 %
> 26.159
> 340.31%00
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
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.80
> 2.4396
> 5.58
> 49.6796
> 9.959
> 408.0096o
> 796
> 2015
> 1.79
> 1.19%
> 3.19
> 39.81%
> 12.20%6
> 667.149600
> 774
> 107
> Clone Alpha
> 2016
> 0.72
> 9896
> 0.82
> 16.1096
> 19.4490
> 162.339600
> 757
> 141
> 2017
> 68
> 1.0296
> 2.31
> 23.5596
> 9.159
> 459.639600
> 865
> 143
> 2018
> -0.97
> 8796
> '23
> -20.0796
> 25.73%
> 214.999600
> 872
> 165
> Chart
> Coverage Of Universe
> 2019
> 1.71
> 1.3796
> 80
> 33.5096
> 12.5096
> 487.519600
> 829
> 148
> 2020
> -016
> 0.849
> 10
> -5.0990
> 20.0796
> -121.119600
> 927
> 2021
> 49
> 0.6096
> 2.47
> 34.2496
> 13.5096
> 1,137
> 69600
> 954
> 24
> 2022
> 2.19
> 2.16%
> 09
> 67.56%
> 13.83%
> 626.759600
> 870
> 159
> 000
> 2023
> 0.92
> 1.4196
> 0.92
> 12.3996
> 14.989
> 176.239600
> 786
> 239
> 950
> Risk neutralized
> 900
> Aggregate Data
> Sharpe
> TITnOIe
> Fitnesc
> Retlrns
> OrlNdOWI
> Margin
> 0.60
> 1.499
> 0.58
> 11.849
> 28.239
> 158.549600
> 850
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> 22
> Jan '23
> Jul '23  Jan '24
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> 1 FAIL
> Robust universe Sharpe of 0.49 is below cUtoff of 0.70
> 5 WARNING
> Performance Comparison
> Sharpe of 1.14is below cutoff of 1.58.
> Weight concentration 36.81%
> above cUtoff of 10% on 4/12/2016.
> Rrln
> UVuAM
> Jul"


尝试应用ts_backfill后，也发现并不能增加覆盖率，Robust universe Sharpe也未改善。这就需要group_backfill了。

group_backfill(alpha, country, 126)，这种方式对覆盖率提升最多，但这种回填方式较糙，未解决Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts
> std
> deV
> group_backfill
> ts_backfill
> 126), country,
> 126 )
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TITnOVe
> Fitness
> Returns
> OraMdOINI
> Margin
> Simulation
> Settings
> 1.14
> 1.349
> 1.46
> 20.639
> 29.699
> 308.739600
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
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.70
> 2.4896
> 80
> 39.489
> 8.0996
> 318.249600
> 1097
> 256
> 2015
> 1.97
> 1.1396
> 3.14
> 31.699
> 9.1196
> 559.409600
> 1023
> 337
> Clone Alpha
> 2016
> 0.52
> 1.4190
> 0.35
> 5.5396
> 10.30%
> 78.759600
> 1062
> 315
> 2017
> 55
> 0.919
> 83
> 17.3896
> 8.439
> 381.309600
> 1214
> 290
> 2018
> 0.04
> 1.42%
> 0.01
> 0.70%
> 14.79%
> 889600
> 1318
> 228
> N Chart
> Coverage Of Universe
> 2019
> 66
> 1.1696
> 2.44
> 27.0696
> 8.6596
> 467.549600
> 1236
> 293
> 2020
> 42
> 1.15%
> 42
> 12.259
> 21.15%
> -213.929600
> 1315
> 248
> 2021
> 1.32
> 0.5596
> 2.06
> 30.3096
> 12.3896
> 1,096.429600
> 1505
> 88
> 2022
> 2.55
> 1.8196
> 58
> 59.769
> 7.8196
> 66
> 069600
> 1312
> 269
> 500
> 2023
> 0.33
> 3390
> 0.19
> 4.0290
> 18.3196
> 60.329600
> 1262
> 310
> 400
> Risk neutralized
> Aggregate Data
> Sharpe
> Trnowe
> Fitness
> RotIrn
> DraiNdoir
> Margin
> 0.55
> 1.349
> 0.46
> 8.58%
> 26.229
> 128.379600
> 300
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23
> Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run: -
> Power Pool Correlation
> Maximum
> Minimum
> Last Run: -
> IS Testing Status
> Period
> IS
> Os
> Prod Correlation
> Maximum
> Minimum
> Last Run: -
> 7 PASS
> 1FAIL
> Robust universe Sharpe of 0.56 is below cutoff of 0.70
> Long


group_backfill(alpha, subindustry, 126)，覆盖率中等提升，但这种基本面数据按照行业均值回填明显比按country回填更合理，成功解决了Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts_std_dev
> Eroup_
> backfill (ts
> backfill
> 126), subindustry,
> 126) ,
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnove
> Returns
> Drawdowr
> Margin
> Simulation Settings
> 1.45
> 1.2496
> 1.89
> 21.209
> 20.699
> 341.619600
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
> Max Position
> Equity
> EUR
> TOPCS1G00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.50
> 2.5096
> 4.36
> 37.94%
> 9.2296
> 303.719600
> 981
> 148
> 2015
> 00
> 1.1696
> 2.96
> 27.30%
> 8.2696
> 469.739600
> 1014
> 147
> Clone Alpha
> 2016
> 0.78
> 1.449
> 0.69
> 9.73%
> 11.5596
> 135.269600
> 972
> 195
> 2017
> 80
> 0596
> 2.49
> 23.95%
> 6.7396
> 455.589600
> 1130
> 168
> 2018
> 0.17
> 1.1096
> -0.08
> -2.61%
> 18.3596
> -47.599600
> 1281
> N Chart
> Coverage Of Universe
> 2019
> 2.87
> 02%6
> 98
> 37.66%
> 6.81%
> 738.029600
> 1281
> 90
> 2020
> 0.45
> 0.8596
> 0.35
> 7.55%
> 5596
> 177.659600
> 1269
> 94
> 2021
> 62
> 0.6796
> 2.42
> 27.99%
> 80%6
> 830.179600
> 1349
> 55
> 2022
> 99
> 5896
> 3.15
> 31.31%
> 11.1496
> 395.639600
> 1261
> 121
> 300
> 2023
> 0.81
> .0196
> 0.73
> 10.16%
> 16.939
> 20
> 0096oo
> 1244
> 128
> 200
> Risk neutralized
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> Returns
> DrawdOWn
> Margin
> 0.74
> 1.249
> 0.62
> 8.679
> 19.639
> 139.739600
> 1,100
> JUl'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul'23 Jan '24
> Correlation
> Self Correlation
> MaYimIm
> NIinimrm
> 13c+
> Prn
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> Fitness of
> 89 is above cUtoff of
> Turnoverof
> .24%
> above cUtoff of 1 %
> Turnoverof
> .249
> below cUtOff of 709.
> Sub-universe Sharpe of 1.19 is above CUtOff of 0.77.
> Robust universe Sharpe of 0.79 is above Cutoff of 0.70.
> Fitnes


最后应用group_backfill(alpha, group_cartesian_product(country, subindustry), 126)，取得最佳效果： 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> Os
> reVerse(ts
> std_deV
> Broup_backfill(ts_backfill
> 126)
> group
> cartesian_product (country,
> subindus
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTnOVer
> Fitness
> Returns
> DrawdOWI
> Margin
> Simulation Settings
> 1.45
> 1.339
> 2.15
> 27.499
> 41.009
> 412.659600
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
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.25
> 64%6
> 4.10
> 41.43%
> 9.44%6
> 314.439600
> 898
> 137
> 2015
> 2.28
> 0.8796
> 67
> 32.309
> 10.769
> 738.519600
> 939
> 84
> Clone Alpha
> 2016
> 38
> 51%
> 1.74
> 19.9196
> 8.79%6
> 262.919600
> 844
> 195
> 2017
> 1.46
> 0.6996
> 2.13
> 26.6496
> 8.0396
> 774.909600
> 1046
> 119
> 2018
> 06
> 16%
> .37
> 20.86%
> 9.75%
> 358.649600
> 1143
> N Chart
> Coverage Of Universe
> 2019
> 2.67
> 0696
> 4.97
> 43.2996
> 9.3596
> 818.869600
> 1085
> 94
> 2020
> 1.12
> 0996
> 62
> 26.2996
> 33.209
> -48
> 879600
> 1149
> 2021
> 93
> 5396
> .38
> 38.2996
> 11.2796
> 1,444.509600
> 1211
> 26
> 2022
> 2.43
> 2.4796
> 5.22
> 57.7296
> 9.4696
> 466.629600
> 990
> 252
> 2023
> 0.89
> .2896
> 02
> 16.4996
> 23.889
> 257.429600
> 1065
> 176
> 100
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Returns
> DrawgOWn
> Margin
> 0.80
> 1.339
> 0.80
> 12.639
> 29.099
> 189.549600
> 000
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan "17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23 Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> o
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run: Fri, 02/27/2026,2:32 AW
> 8 PASS
> Fitness of 2.15 is aboVe cUtoff of
> 0.7002
> -0.3901
> Turnover of
> .339is above cUtoff Of 1%.
> Turnoverof-
> .33%
> below cUtoff of 70%
> Sub-universe Sharpe of 1.35
> aboVe cutoff of 0.77 _
> Robust universe Sharpe of 0.82 is above cutoff of 0.70.
> Long


有兴趣的还可以看Coverage by Industry图，限于篇幅就不细说了。总的来说，建议大家对某个idea大规模回测之前，先把各种group fields都用group_backfill试一下，找到最合适的回填方式，再大规模回测。

**顾问 YH55729 (Rank 42) 的解答与建议**:
学到了，之前主要使用调trunication的参数调整weight concertration

=============================================================================


---

### 技术对话片段 3 (原帖: 通用 Alpha 优化与迭代工作流)
- **原帖链接**: [Commented] Gemini CLI正确开启skills以及alpha迭代优化工作流经验分享.md
- **时间**: 4个月前

**提问/主帖背景 (HZ32281)**:
首先要感谢开发AI打工人的大佬给我们带来这么好用的工具，同样，我也在第一时间使用了，尤其在看到.claude\skills文件夹的那一刻，仿佛发现了宝藏。作为Gemini CLI的高强度使用者，我就想这些skills能不能在gemini当中使用。

以防还有同学不了解Gemini CLI要怎样开启使用skills，这里就先说一下开启方式。首先，我们直接把.claude当中的skills文件夹整个复制到.gemini文件夹当中。然后我们启动Gemini CLI，在启动好后输入“/settings”，在出现的搜索框中输入“skills”，这里会看到“Enable Agent Skills”，按下回车让false变成true（因为Gemini CLI的skills是默认关闭的）。再次打开Gemini CLI时显示如下就说明开启成功了。


> [!NOTE] [图片 OCR 识别内容]
> GEMINI .md file
> 1 MCP
> SeTVeI
> 12 skills
> Type
> JOUI message
> OI
> @path/to/file


下面这篇是我今天新做的迭代优化alpha工作流，初衷是因为单纯用一个全自动生产alpha的工作流有的时候就是会差一口气，而且这个窗口已经优化迭代了差不多20轮了，肉眼可见AI已经疲惫了，而且如果继续用当前窗口跑的话会消耗更多token，效果还不好。那么我们就可以新开一个窗口，把前面得到的还差一点就能提交的alpha信号放到新窗口进行迭代优化。

最开始我是没做工作流的，每次就手打“调用适当的skills和文件夹当中的解决方案来优化alpha”。结果就是要么就是AI闷头跑，没有任何文字反馈，要么就是非常简短的英文，要么就是优化到能交就直接给你交掉了。在发布我的上一篇文章：【用Gemini CLI全自动找Alpha工作流——纯Template版】之后每天都在碰到新的问题和修改工作流，在高强度使用了两个月之后得出的最重要的结论就是：有的时候并不是我们的提示词不够精炼或者不够完善，而是我们和AI的思维方式不同。在反复碰到相同问题的时候，就应该停下来问一问AI他会这样处理的原因，以及如果要达到你想要的效果的话，这个提示词应该怎么修改。应该把他当做团队伙伴，而不仅仅只是生产工具。那么在根据碰到过的问题和AI讨论之后，最终得到了以下工作流。

# 通用 Alpha 优化与迭代工作流

## 0. 配置 (Configuration)

> **在此处修改目标 Alpha ID**

*   **Target Alpha ID**: `...........`

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢分享，这一套在ai打工人里是不是也可以用？

========================================================================


---

### 技术对话片段 4 (原帖: 通用 Alpha 优化与迭代工作流)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Gemini CLI正确开启skills以及alpha迭代优化工作流经验分享_38013614427671.md
- **时间**: 4个月前

**提问/主帖背景 (HZ32281)**:
首先要感谢开发AI打工人的大佬给我们带来这么好用的工具，同样，我也在第一时间使用了，尤其在看到.claude\skills文件夹的那一刻，仿佛发现了宝藏。作为Gemini CLI的高强度使用者，我就想这些skills能不能在gemini当中使用。

以防还有同学不了解Gemini CLI要怎样开启使用skills，这里就先说一下开启方式。首先，我们直接把.claude当中的skills文件夹整个复制到.gemini文件夹当中。然后我们启动Gemini CLI，在启动好后输入“/settings”，在出现的搜索框中输入“skills”，这里会看到“Enable Agent Skills”，按下回车让false变成true（因为Gemini CLI的skills是默认关闭的）。再次打开Gemini CLI时显示如下就说明开启成功了。


> [!NOTE] [图片 OCR 识别内容]
> GEMINI .md file
> 1 MCP
> SeTVeI
> 12 skills
> Type
> JOUI message
> OI
> @path/to/file


下面这篇是我今天新做的迭代优化alpha工作流，初衷是因为单纯用一个全自动生产alpha的工作流有的时候就是会差一口气，而且这个窗口已经优化迭代了差不多20轮了，肉眼可见AI已经疲惫了，而且如果继续用当前窗口跑的话会消耗更多token，效果还不好。那么我们就可以新开一个窗口，把前面得到的还差一点就能提交的alpha信号放到新窗口进行迭代优化。

最开始我是没做工作流的，每次就手打“调用适当的skills和文件夹当中的解决方案来优化alpha”。结果就是要么就是AI闷头跑，没有任何文字反馈，要么就是非常简短的英文，要么就是优化到能交就直接给你交掉了。在发布我的上一篇文章：【用Gemini CLI全自动找Alpha工作流——纯Template版】之后每天都在碰到新的问题和修改工作流，在高强度使用了两个月之后得出的最重要的结论就是：有的时候并不是我们的提示词不够精炼或者不够完善，而是我们和AI的思维方式不同。在反复碰到相同问题的时候，就应该停下来问一问AI他会这样处理的原因，以及如果要达到你想要的效果的话，这个提示词应该怎么修改。应该把他当做团队伙伴，而不仅仅只是生产工具。那么在根据碰到过的问题和AI讨论之后，最终得到了以下工作流。

# 通用 Alpha 优化与迭代工作流

## 0. 配置 (Configuration)

> **在此处修改目标 Alpha ID**

*   **Target Alpha ID**: `...........`

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢分享，这一套在ai打工人里是不是也可以用？

========================================================================


---

### 技术对话片段 5 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] USA analyst一些具有经济学意义的重组数据字段.md
- **时间**: 3个月前

**提问/主帖背景 (YL20168)**:
之前利用workflow对现有的数据字段进行了重组，生成了一些具有经济学意义的新的数据，有的数据直接调用老的三阶模板就可以实现效果比较好的alpha，之前用这种方式把value factor从0.27提高到了>0.8，现在把之前生成的一些新的数据分享出来：

USA analyst：

act_12m_ebi_value / act_12m_sal_value

act_12m_net_value / act_12m_bps_value

act_12m_net_value / act_12m_roa_value

act_q_eps_value / act_q_bps_value

act_12m_sal_value - act_12m_cpx_value

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v2_2360

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v2_2360

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v2_2360

anl14_actvalue_eps_fp0 / anl14_actvalue_revenue_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_ndebt_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_ndebt_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_cfps_fp0 / anl14_actvalue_eps_fp0

anl14_actvalue_cfps_fp0 / anl14_actvalue_revenue_fp0

anl14_actvalue_revenue_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_cfps_fp0 - anl14_actvalue_ndebt_fp0

anl44_2_ebitdaps_prevalue / anl44_2_bps_prevalue

anl44_2_ebitdaps_prevalue / anl44_2_nav_prevalue

anl44_2_netdebt_prevalue / anl44_2_bps_prevalue

anl44_2_netdebt_prevalue / anl44_2_nav_prevalue

anl44_2_capex_prevalue / anl44_2_ebitdaps_prevalue

anl44_2_nav_prevalue - anl44_2_netdebt_prevalue

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢分享，不过感觉还是得考虑下量纲和缩放问题，具体还得看字段本身是什么值。

==============================================


---

### 技术对话片段 6 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] USA analyst一些具有经济学意义的重组数据字段_38927191768343.md
- **时间**: 3个月前

**提问/主帖背景 (YL20168)**:
之前利用workflow对现有的数据字段进行了重组，生成了一些具有经济学意义的新的数据，有的数据直接调用老的三阶模板就可以实现效果比较好的alpha，之前用这种方式把value factor从0.27提高到了>0.8，现在把之前生成的一些新的数据分享出来：

USA analyst：

act_12m_ebi_value / act_12m_sal_value

act_12m_net_value / act_12m_bps_value

act_12m_net_value / act_12m_roa_value

act_q_eps_value / act_q_bps_value

act_12m_sal_value - act_12m_cpx_value

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v2_2360

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v2_2360

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v2_2360

anl14_actvalue_eps_fp0 / anl14_actvalue_revenue_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_ndebt_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_ndebt_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_cfps_fp0 / anl14_actvalue_eps_fp0

anl14_actvalue_cfps_fp0 / anl14_actvalue_revenue_fp0

anl14_actvalue_revenue_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_cfps_fp0 - anl14_actvalue_ndebt_fp0

anl44_2_ebitdaps_prevalue / anl44_2_bps_prevalue

anl44_2_ebitdaps_prevalue / anl44_2_nav_prevalue

anl44_2_netdebt_prevalue / anl44_2_bps_prevalue

anl44_2_netdebt_prevalue / anl44_2_nav_prevalue

anl44_2_capex_prevalue / anl44_2_ebitdaps_prevalue

anl44_2_nav_prevalue - anl44_2_netdebt_prevalue

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢分享，不过感觉还是得考虑下量纲和缩放问题，具体还得看字段本身是什么值。

==============================================


---

### 技术对话片段 7 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【WQ数据监控 v020】wqmanagerqzzio 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比代码优化.md
- **时间**: 3个月前

**提问/主帖背景 (JG15244)**:
在线地址： [[链接已屏蔽])

## 更新内容

1. 个人信息页面增加 Osmosis Rank 变化趋势图、周维度对比图。
2. 新增 consulant 页面，整合 consulant 全部信息。

## 更新截图


> [!NOTE] [图片 OCR 识别内容]
> Consultant Detail Dashboard
> REFRESH
> Merged view of ` Ieaderboard_consultant_user
> and
> leaderboard_genius_user
> RECORD
> DAT巳
> COUNTRY/REGION
> GENIUS LEVEL
> USER SEARCH
> 2026-02-23
> Select countrylregion
> Select level
> Enter WQ_ID keyword
> APPLY
> Reset
> FILTERED USERS
> CONSULTANT COVCRAGE
> GENIUS COVERAG卫
> MATCHED USERS
> COUNTRIPS
> GENIUS LEVELS
> 10,762
> 8,419
> 10,759
> 8,416
> 16
> 4
> Date 2026-02-23
> Fromn
> Fromn Ieaderboard
> UISET
> Users found i both tables On
> Distinct Countries in Curtent
> Distinct levels in current result
> leaderboard_consultant_
> UISeT
> selected date
> Tesult
> AllMetrics
> Total 10762
> No_
> User
> Country
> University
> Level
> Best Level
> Weight
> Value
> Osmosis
> Data Fields
> RA
> RA Prod
> RA SI
> Rank
> Subm
> Corr
> 6247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63372
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec.。
> GOLD
> GOLD
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> R19116
> IN
> Dr.APJ.Abdul Kalar。。
> GOLD
> GOLD
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> XL82940
> CN
> GOLD
> EXPERI
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> KE
> Jomo Kenyatta Univer。
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE
> GOLD
> GOLD
> 2.31
> 0.47
> 0.90
> 269
> 326
> 0.6803
> P24362
> CN
> TNuhan
> University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 0242372
> CN
> Harbin Engineering U。
> GOLD
> GOLD
> 0.00
> 0.93
> 0.89
> 145
> 167
> 0.6402
> 10
> 巫24675
> IN
> Deen Dayal Upadhyay.-
> GOLD
> EXPERI
> 26.63
> 0.30
> 0.88
> 1,990
> 1,755
> 0.6537
> 11
> T42173
> CN
> Arizona State Universi。
> EXPERI
> EXPERI
> 26.11
> 0.44
> 0.88
> 460
> 648
> 0.6685
> 12
> CL93587
> CN
> HangZhou Dianziuni。
> EXPERI
> EXPERI
> 14.88
> 0.28
> 0.87
> 390
> 295
> 0.6609
> 13
> J75700
> Harbin Institute Of Te。
> EXPERI
> EXPERI
> 0.00
> 0.90
> 0.87
> 124
> 106
> 0.6568
> 14
> PY32594
> CN
> Huazhong University
> EXPERI
> EXPERI
> 0.00
> 0.42
> 0.87
> 441
> 480
> 0.6867
> 15
> 2262721
> CN
> MASTER
> MASTER
> 7.37
> 0.95
> 0.87
> 405
> 316
> 0.7365
> 16
> SL10033
> University Of Internati。
> EXPERI
> MASTER
> 39.26
> 0.68
> 0.87
> 625
> 447
> 0.5676
> 17
> T12226
> CN
> GOLD
> GOLD
> 0.00
> 0.55
> 0.87
> 182
> 207
> 0.6052
> 18
> 4T26308
> IN
> Indian Institute Of Tec..
> GOLD
> MASTER
> 13.57
> 0.03
> 0.86
> 408
> 471
> 0.7073
> 19
> J025713
> KE
> CHUKA university
> EXPERI
> MASTER
> 4.72
> 0.32
> 0.86
> 1,404
> 1,498
> 0.6529
> 20
> 1053462
> CN
> NanJing Audit Univer。。。
> GOLD
> EXPERT
> 1.14
> 0.38
> 0.86
> 166
> 126
> 0.6513
> Total 10762
> 20/page
> 539
> genius



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Weekly
> R巳CORD DAT巳
> Rank
> 1.00
> 2026-02-23
> Reset
> 0.80
> 0.60
> FILTERED USERS
> GPNIUS LDVPLS
> 10,762
> 0.40
> Date 2026-02-23
> 0.33
> Distinct levels in current result
> 0.20
> 0.00
> All Metrics
> Total 10762
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 2026-02-16'
> 2026-02-17
> 2026-02-18'
> 2026-02-19'
> 2026-02-20'
> 2026-02-21'
> 2026-02-22'
> 2026-02-23'



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Daily
> R巳CORD DAT巳
> 2026-02-16
> 2026-02-22
> 3 2026-02-23
> 2026-03-01
> 2026-02-23
> Rank
> Reset
> 1.00
> 0.96
> 0.80
> FILTERED USERS
> GPNIUS LDVPLS
> 0.60
> 10,762
> Date 2026-02-23
> Distinct levels in current result
> 0.40
> 0.24
> 0.20
> All Metrics
> 0.00
> Total 10762
> 苘凶
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521



> [!NOTE] [图片 OCR 识别内容]
> 个人中心
> 退出登录
> 顾问 JG15244 (Rank 67)
> 单日最大娈化
> 当前 Weight
> 历史最高
> 今日娈化
> 0.79
> 17.60
> 17.60
> +0.00
> 日期2025-12-24
> Weight 变化趋势
> 共71犬
> 权重因子
> 19.56
> 15.00
> 11.23
> 10.00
> 5.00
> 00
> ^?
> ^9
> 8
> 8
> 2
> ^2
> 02
> 02
> 02
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> 16
> 19
> 20
> 23
> 02
> 02
> 02
> 02
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> Power
> Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 0.90
> 1.50
> 0.87
> 1.00
> 0.84
> 0.50
> 0.81
> 0.79
> 0.04
> 202508
> 202509
> 202510
> 202508
> 202509
> 202510
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 历史记录
> 共71条
> VALUE
> DA11
> 05M0515
> REGULAR
> REGULAR ALPHA
> REGULAR
> SUPER ALPH4
> SUPER ALPHA
> SUPER ALPH
> 日期
> WEIGHT
> FA CT0R
> RANk
> ALPHA 提交数
> 生产相关
> 41PH4
> 自相关
> 提交数
> 产相关
> 自相
> 2026-02-23
> 17.60
> 0.89
> 0.64
> 503
> 0.6133
> 0.3392
> 244
> 0.5860
> 0.50
> 2026-02-22
> 17.60
> 0.89
> 0.73
> 502
> 0.6131
> 0.3392
> 243
> 0.5865
> 0.50
> 2026-02-21
> 17.60
> 89
> 38
> 501
> 0.6128
> 3393
> 242
> 0.5861
> 0.50
> 2026-02-20
> 17.35
> 500
> 0.6135
> 3397
> 241
> 0.5869
> 0.50
> 2026-02-19
> 17.08
> 38
> 0.6149
> 3404
> 240
> 0.5865
> 0.50
> 2026-02-18
> 16.82
> 0.31
> 492
> 0.6174
> 3419
> 239
> 0.5875
> 0.50
> 2026-02-17
> 16.82
> 89
> 0.31
> 487
> 6204
> 3436
> 238
> 0.5873
> 0.50
> 2026-02-16
> 16.82
> 89
> 0.31
> 486
> ).6205
> 3438
> 237
> 0.5880
> 0.50
> 2026-02-15
> 16.82
> 89
> 486
> 0.6205
> 3438
> 236
> 0.5876
> 50
> 2026-02-14
> 16.64
> 89
> 485
> 1.6202
> 3439
> 234
> 0.5878
> 50
> Total 71
> Goto
> 01-06
> 01-16
> 01-18
> 01-20
> 12-17
> ~
> 12-23
> 12-25
> 12-27
> 12-29
> 12-31
> 01-02
> 01-04
> 01-08
> 01-10
> 01-12
> 01-14
> 01-22
> 01-24
> 01-26
> 01-28
> 01-30
> 02-01
> 02-03
> 02-07
> 02-11
> 02-13
> 02-21
> 合
> ~02-17
> ~02-18
> ~02-21
> ~02-22
> 2026
> 2026
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> Pool



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到曰维度
> 2026-02-16
> 2026-02-22
> 0
> 2026-02-23
> 2026-03-01
> Rank
> 1.00
> 80
> 0.64
> 60
> 0.40
> 0.20
> 0.00
> 周二
> 周三
> 周五
> 周六
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21
> ~02-16'
> ~02-17
> ~02-18
> ~02-19
> ~02-20
> ~02-22
> 2026-02-23'
> ~02-21
> 2026-
> 2026-
> 2026-
> 2026-C
> 2026-C
> 2026-C
> 2026-0


> 欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！
> 欢迎 start 和 issue ！
> 后端项目地址： [[链接已屏蔽])
> 前端项目地址： [[链接已屏蔽])

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢大佬的网站工具，非常一目了然，可以持续观察自己的渗透分走势

=====================================================================


---

### 技术对话片段 8 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【WQ数据监控 v020】wqmanagerqzzio 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比代码优化_38582852015895.md
- **时间**: 3个月前

**提问/主帖背景 (JG15244)**:
在线地址： [[链接已屏蔽])

## 更新内容

1. 个人信息页面增加 Osmosis Rank 变化趋势图、周维度对比图。
2. 新增 consulant 页面，整合 consulant 全部信息。

## 更新截图


> [!NOTE] [图片 OCR 识别内容]
> Consultant Detail Dashboard
> REFRESH
> Merged view of ` Ieaderboard_consultant_user
> and
> leaderboard_genius_user
> RECORD
> DAT巳
> COUNTRY/REGION
> GENIUS LEVEL
> USER SEARCH
> 2026-02-23
> Select countrylregion
> Select level
> Enter WQ_ID keyword
> APPLY
> Reset
> FILTERED USERS
> CONSULTANT COVCRAGE
> GENIUS COVERAG卫
> MATCHED USERS
> COUNTRIPS
> GENIUS LEVELS
> 10,762
> 8,419
> 10,759
> 8,416
> 16
> 4
> Date 2026-02-23
> Fromn
> Fromn Ieaderboard
> UISET
> Users found i both tables On
> Distinct Countries in Curtent
> Distinct levels in current result
> leaderboard_consultant_
> UISeT
> selected date
> Tesult
> AllMetrics
> Total 10762
> No_
> User
> Country
> University
> Level
> Best Level
> Weight
> Value
> Osmosis
> Data Fields
> RA
> RA Prod
> RA SI
> Rank
> Subm
> Corr
> 6247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63372
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec.。
> GOLD
> GOLD
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> R19116
> IN
> Dr.APJ.Abdul Kalar。。
> GOLD
> GOLD
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> XL82940
> CN
> GOLD
> EXPERI
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> KE
> Jomo Kenyatta Univer。
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE
> GOLD
> GOLD
> 2.31
> 0.47
> 0.90
> 269
> 326
> 0.6803
> P24362
> CN
> TNuhan
> University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 0242372
> CN
> Harbin Engineering U。
> GOLD
> GOLD
> 0.00
> 0.93
> 0.89
> 145
> 167
> 0.6402
> 10
> 巫24675
> IN
> Deen Dayal Upadhyay.-
> GOLD
> EXPERI
> 26.63
> 0.30
> 0.88
> 1,990
> 1,755
> 0.6537
> 11
> T42173
> CN
> Arizona State Universi。
> EXPERI
> EXPERI
> 26.11
> 0.44
> 0.88
> 460
> 648
> 0.6685
> 12
> CL93587
> CN
> HangZhou Dianziuni。
> EXPERI
> EXPERI
> 14.88
> 0.28
> 0.87
> 390
> 295
> 0.6609
> 13
> J75700
> Harbin Institute Of Te。
> EXPERI
> EXPERI
> 0.00
> 0.90
> 0.87
> 124
> 106
> 0.6568
> 14
> PY32594
> CN
> Huazhong University
> EXPERI
> EXPERI
> 0.00
> 0.42
> 0.87
> 441
> 480
> 0.6867
> 15
> 2262721
> CN
> MASTER
> MASTER
> 7.37
> 0.95
> 0.87
> 405
> 316
> 0.7365
> 16
> SL10033
> University Of Internati。
> EXPERI
> MASTER
> 39.26
> 0.68
> 0.87
> 625
> 447
> 0.5676
> 17
> T12226
> CN
> GOLD
> GOLD
> 0.00
> 0.55
> 0.87
> 182
> 207
> 0.6052
> 18
> 4T26308
> IN
> Indian Institute Of Tec..
> GOLD
> MASTER
> 13.57
> 0.03
> 0.86
> 408
> 471
> 0.7073
> 19
> J025713
> KE
> CHUKA university
> EXPERI
> MASTER
> 4.72
> 0.32
> 0.86
> 1,404
> 1,498
> 0.6529
> 20
> 1053462
> CN
> NanJing Audit Univer。。。
> GOLD
> EXPERT
> 1.14
> 0.38
> 0.86
> 166
> 126
> 0.6513
> Total 10762
> 20/page
> 539
> genius



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Weekly
> R巳CORD DAT巳
> Rank
> 1.00
> 2026-02-23
> Reset
> 0.80
> 0.60
> FILTERED USERS
> GPNIUS LDVPLS
> 10,762
> 0.40
> Date 2026-02-23
> 0.33
> Distinct levels in current result
> 0.20
> 0.00
> All Metrics
> Total 10762
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 2026-02-16'
> 2026-02-17
> 2026-02-18'
> 2026-02-19'
> 2026-02-20'
> 2026-02-21'
> 2026-02-22'
> 2026-02-23'



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Daily
> R巳CORD DAT巳
> 2026-02-16
> 2026-02-22
> 3 2026-02-23
> 2026-03-01
> 2026-02-23
> Rank
> Reset
> 1.00
> 0.96
> 0.80
> FILTERED USERS
> GPNIUS LDVPLS
> 0.60
> 10,762
> Date 2026-02-23
> Distinct levels in current result
> 0.40
> 0.24
> 0.20
> All Metrics
> 0.00
> Total 10762
> 苘凶
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521



> [!NOTE] [图片 OCR 识别内容]
> 个人中心
> 退出登录
> 顾问 JG15244 (Rank 67)
> 单日最大娈化
> 当前 Weight
> 历史最高
> 今日娈化
> 0.79
> 17.60
> 17.60
> +0.00
> 日期2025-12-24
> Weight 变化趋势
> 共71犬
> 权重因子
> 19.56
> 15.00
> 11.23
> 10.00
> 5.00
> 00
> ^?
> ^9
> 8
> 8
> 2
> ^2
> 02
> 02
> 02
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> 16
> 19
> 20
> 23
> 02
> 02
> 02
> 02
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> Power
> Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 0.90
> 1.50
> 0.87
> 1.00
> 0.84
> 0.50
> 0.81
> 0.79
> 0.04
> 202508
> 202509
> 202510
> 202508
> 202509
> 202510
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 历史记录
> 共71条
> VALUE
> DA11
> 05M0515
> REGULAR
> REGULAR ALPHA
> REGULAR
> SUPER ALPH4
> SUPER ALPHA
> SUPER ALPH
> 日期
> WEIGHT
> FA CT0R
> RANk
> ALPHA 提交数
> 生产相关
> 41PH4
> 自相关
> 提交数
> 产相关
> 自相
> 2026-02-23
> 17.60
> 0.89
> 0.64
> 503
> 0.6133
> 0.3392
> 244
> 0.5860
> 0.50
> 2026-02-22
> 17.60
> 0.89
> 0.73
> 502
> 0.6131
> 0.3392
> 243
> 0.5865
> 0.50
> 2026-02-21
> 17.60
> 89
> 38
> 501
> 0.6128
> 3393
> 242
> 0.5861
> 0.50
> 2026-02-20
> 17.35
> 500
> 0.6135
> 3397
> 241
> 0.5869
> 0.50
> 2026-02-19
> 17.08
> 38
> 0.6149
> 3404
> 240
> 0.5865
> 0.50
> 2026-02-18
> 16.82
> 0.31
> 492
> 0.6174
> 3419
> 239
> 0.5875
> 0.50
> 2026-02-17
> 16.82
> 89
> 0.31
> 487
> 6204
> 3436
> 238
> 0.5873
> 0.50
> 2026-02-16
> 16.82
> 89
> 0.31
> 486
> ).6205
> 3438
> 237
> 0.5880
> 0.50
> 2026-02-15
> 16.82
> 89
> 486
> 0.6205
> 3438
> 236
> 0.5876
> 50
> 2026-02-14
> 16.64
> 89
> 485
> 1.6202
> 3439
> 234
> 0.5878
> 50
> Total 71
> Goto
> 01-06
> 01-16
> 01-18
> 01-20
> 12-17
> ~
> 12-23
> 12-25
> 12-27
> 12-29
> 12-31
> 01-02
> 01-04
> 01-08
> 01-10
> 01-12
> 01-14
> 01-22
> 01-24
> 01-26
> 01-28
> 01-30
> 02-01
> 02-03
> 02-07
> 02-11
> 02-13
> 02-21
> 合
> ~02-17
> ~02-18
> ~02-21
> ~02-22
> 2026
> 2026
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> Pool



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到曰维度
> 2026-02-16
> 2026-02-22
> 0
> 2026-02-23
> 2026-03-01
> Rank
> 1.00
> 80
> 0.64
> 60
> 0.40
> 0.20
> 0.00
> 周二
> 周三
> 周五
> 周六
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21
> ~02-16'
> ~02-17
> ~02-18
> ~02-19
> ~02-20
> ~02-22
> 2026-02-23'
> ~02-21
> 2026-
> 2026-
> 2026-
> 2026-C
> 2026-C
> 2026-C
> 2026-0


> 欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！
> 欢迎 start 和 issue ！
> 后端项目地址： [[链接已屏蔽])
> 前端项目地址： [[链接已屏蔽])

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢大佬的网站工具，非常一目了然，可以持续观察自己的渗透分走势

=====================================================================


---

### 技术对话片段 9 (原帖: Extra Vars (Provider specific))
- **原帖链接**: [Commented] 【新手向】打造经济实用型打工人-为AI打工人配置优惠的coding plan.md
- **时间**: 4个月前

**提问/主帖背景 (YH47265)**:
自从AI打工人发布以来，我一直在用它优化因子，效果很不错，比自己的工作流效果要好。

但打工人默认用kimi或者deepseek的api，用token计费，以我自己为例，优化一个因子（不论是否成功）大概5块钱，有些肉疼。

根据我自己使用体验，使用免费的iflow等api效果一般，还是得付费，但考虑用量和性价比，我选择了GLM的coding-plan最便宜的一档，最低20一个月，不到一天的base，每五小时120次对话次数，量大管饱。而且适配claude code很不错，算是国产模型里面性价比较高的。同样还有minimax，也有类似套餐可以选择。

由于打工人默认是kimi和ds二选一，需要修改下文件夹里的step4，才能加入其他选项，这里直接给出代码，即插即用，方便不会代码的朋友使用：

# SetAPI_And_Check_MoonShot.py
import os
import sys
import subprocess
import time

# Ensure openai is installed
try:
    from openai import OpenAI
except ImportError:
    print("正在安装 openai 依赖包...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import OpenAI

def set_windows_env_var(name, value):
    """Set a user-level environment variable on Windows using PowerShell."""
    if not value:
        return
    # Escape double quotes for PowerShell
    value_escaped = value.replace('"', '`"')
    ps_command = f'[Environment]::SetEnvironmentVariable("{name}", "{value_escaped}", "User")'
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_command]
    try:
        subprocess.check_call(cmd)
        print(f"✅ 环境变量已设置: {name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ 设置失败 {name}: {e}")

def get_provider_config():
    print("\n请选择您要使用的 API 提供商:")
    print("1. Kimi (Moonshot) - [platform.moonshot.cn]")
    print("2. DeepSeek (深度求索) - [platform.deepseek.com]")
    print("3. GLM (智谱清言) - [open.bigmodel.cn]")

    while True:
        choice = input("\n请输入序号 (1、2 或 3): ").strip()
        if choice == "1":
            return {
                "name": "Moonshot (Kimi)",
                "site": "platform.moonshot.cn",
                "list_base_url": " [[链接已屏蔽]) ",
                "anthropic_base_url": " [[链接已屏蔽]) ",
                "extra_envs": {}
            }
        elif choice == "2":
            return {
                "name": "DeepSeek",
                "site": "platform.deepseek.com",
                "list_base_url": " [[链接已屏蔽]) ",
                "anthropic_base_url": " [[链接已屏蔽]) ",
                "extra_envs": {
                    "API_TIMEOUT_MS": "900000",
                    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
                    "ANTHROPIC_SMALL_FAST_MODEL": "{model}"
                }
            }
        elif choice == "3":
            return {
                "name": "GLM",
                "site": "open.bigmodel.cn",
                "list_base_url": " [[链接已屏蔽]) ",
                "anthropic_base_url": " [[链接已屏蔽]) ",
                "extra_envs": {
                    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
                }
            }
        else:
            print("输入无效，请重新输入。")

def main():
    print("=== Claude Code API 多模型配置工具 ===")

    # 1. Select Provider
    config = get_provider_config()

    # 2. Get API Key
    print(f"\n您选择了 {config['name']}。")
    print(f"请前往官网 {config['site']} 申请 API Key。")
    api_key = input(f"请输入您的 API Key (sk-...): ").strip()
    if not api_key:
        print("API Key 不能为空。")
        return

# 3. Initialize Client to fetch models
    print(f"\n正在连接 {config['name']} API 以获取可用模型列表...")
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=config['list_base_url'],
        )

        model_list = client.models.list()
        model_data = model_list.data

        if not model_data:
            print("未找到可用模型，请检查您的 API Key 或配置。")
            return

# 4. List and Select Model
        print(f"\n可用模型列表:")
        sorted_models = sorted(model_data, key=lambda m: m.id)
        for i, model in enumerate(sorted_models):
            print(f"[{i}] {model.id}")

        selection = input("\n请输入序号选择默认模型 (例如 0): ").strip()
        try:
            index = int(selection)
            if 0 <= index < len(sorted_models):
                selected_model = sorted_models[index].id
                print(f"已选择模型: {selected_model}")
            else:
                print("无效的序号。")
                return
        except ValueError:
            print("输入无效，请输入数字。")
            return

except Exception as e:
        print(f"\n❌ API 连接失败: {e}")
        print("无法连接到服务器。请检查网络或 API Key。")
        return

# 5. Configure Environment Variables
    print("\n正在配置全局环境变量 (Windows User Scope)...")

    # Core Anthropic Vars
    set_windows_env_var("ANTHROPIC_BASE_URL", config['anthropic_base_url'])
    set_windows_env_var("ANTHROPIC_AUTH_TOKEN", api_key)

    # Model Vars (Standard)
    # Applying selected model to all Standard Roles
    set_windows_env_var("ANTHROPIC_MODEL", selected_model)
    set_windows_env_var("ANTHROPIC_DEFAULT_OPUS_MODEL", selected_model)
    set_windows_env_var("ANTHROPIC_DEFAULT_SONNET_MODEL", selected_model)
    set_windows_env_var("ANTHROPIC_DEFAULT_HAIKU_MODEL", selected_model)
    set_windows_env_var("CLAUDE_CODE_SUBAGENT_MODEL", selected_model)

# Extra Vars (Provider specific)
    for key, val_template in config['extra_envs'].items():
        val = val_template.format(model=selected_model) # Format if placeholder exists
        set_windows_env_var(key, val)

print("\n✨ 配置完成！")
    print("************************************************")
    print(f" 提供商: {config['name']}")
    print(f" 模型  : {selected_model}")
    print(f" 接口  : {config['anthropic_base_url']}")
    print("************************************************")
    print("⚠️ 请注意：请务必 关闭并重新打开 您的终端窗口，以应用新的环境变量。")

if __name__ == "__main__":
    main()

使用时先运行step4，选择模型，填入API，即可享受经济实用型打工人了。如果想使用其他家的模型（只要支持claude code均可），直接让AI去修改即可，这里也给出提示词：

分析@Step4_SetAPI_And_Check_LLMModel.py

维持其他功能不变，修改这个文件，目标：支持第3个API 提供商GLM，配置相关变量ANTHROPIC_AUTH_TOKEN

ANTHROPIC_BASE_URL  [[链接已屏蔽])

CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 1

根据模型的具体参数修改上面三行即可。

**顾问 YH55729 (Rank 42) 的解答与建议**:
太好了，终于找到了便宜的使用打工人的方案，用kimi的api实在是太贵了

-----------------------------------------------------------------------------------------------------


---

### 技术对话片段 10 (原帖: Extra Vars (Provider specific))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【新手向】打造经济实用型打工人-为AI打工人配置优惠的coding plan_38009162109079.md
- **时间**: 4个月前

**提问/主帖背景 (YH47265)**:
自从AI打工人发布以来，我一直在用它优化因子，效果很不错，比自己的工作流效果要好。

但打工人默认用kimi或者deepseek的api，用token计费，以我自己为例，优化一个因子（不论是否成功）大概5块钱，有些肉疼。

根据我自己使用体验，使用免费的iflow等api效果一般，还是得付费，但考虑用量和性价比，我选择了GLM的coding-plan最便宜的一档，最低20一个月，不到一天的base，每五小时120次对话次数，量大管饱。而且适配claude code很不错，算是国产模型里面性价比较高的。同样还有minimax，也有类似套餐可以选择。

由于打工人默认是kimi和ds二选一，需要修改下文件夹里的step4，才能加入其他选项，这里直接给出代码，即插即用，方便不会代码的朋友使用：

# SetAPI_And_Check_MoonShot.py
import os
import sys
import subprocess
import time

# Ensure openai is installed
try:
    from openai import OpenAI
except ImportError:
    print("正在安装 openai 依赖包...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import OpenAI

def set_windows_env_var(name, value):
    """Set a user-level environment variable on Windows using PowerShell."""
    if not value:
        return
    # Escape double quotes for PowerShell
    value_escaped = value.replace('"', '`"')
    ps_command = f'[Environment]::SetEnvironmentVariable("{name}", "{value_escaped}", "User")'
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_command]
    try:
        subprocess.check_call(cmd)
        print(f"✅ 环境变量已设置: {name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ 设置失败 {name}: {e}")

def get_provider_config():
    print("\n请选择您要使用的 API 提供商:")
    print("1. Kimi (Moonshot) - [platform.moonshot.cn]")
    print("2. DeepSeek (深度求索) - [platform.deepseek.com]")
    print("3. GLM (智谱清言) - [open.bigmodel.cn]")

    while True:
        choice = input("\n请输入序号 (1、2 或 3): ").strip()
        if choice == "1":
            return {
                "name": "Moonshot (Kimi)",
                "site": "platform.moonshot.cn",
                "list_base_url": " [[链接已屏蔽]) ",
                "anthropic_base_url": " [[链接已屏蔽]) ",
                "extra_envs": {}
            }
        elif choice == "2":
            return {
                "name": "DeepSeek",
                "site": "platform.deepseek.com",
                "list_base_url": " [[链接已屏蔽]) ",
                "anthropic_base_url": " [[链接已屏蔽]) ",
                "extra_envs": {
                    "API_TIMEOUT_MS": "900000",
                    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
                    "ANTHROPIC_SMALL_FAST_MODEL": "{model}"
                }
            }
        elif choice == "3":
            return {
                "name": "GLM",
                "site": "open.bigmodel.cn",
                "list_base_url": " [[链接已屏蔽]) ",
                "anthropic_base_url": " [[链接已屏蔽]) ",
                "extra_envs": {
                    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
                }
            }
        else:
            print("输入无效，请重新输入。")

def main():
    print("=== Claude Code API 多模型配置工具 ===")

    # 1. Select Provider
    config = get_provider_config()

    # 2. Get API Key
    print(f"\n您选择了 {config['name']}。")
    print(f"请前往官网 {config['site']} 申请 API Key。")
    api_key = input(f"请输入您的 API Key (sk-...): ").strip()
    if not api_key:
        print("API Key 不能为空。")
        return

# 3. Initialize Client to fetch models
    print(f"\n正在连接 {config['name']} API 以获取可用模型列表...")
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=config['list_base_url'],
        )

        model_list = client.models.list()
        model_data = model_list.data

        if not model_data:
            print("未找到可用模型，请检查您的 API Key 或配置。")
            return

# 4. List and Select Model
        print(f"\n可用模型列表:")
        sorted_models = sorted(model_data, key=lambda m: m.id)
        for i, model in enumerate(sorted_models):
            print(f"[{i}] {model.id}")

        selection = input("\n请输入序号选择默认模型 (例如 0): ").strip()
        try:
            index = int(selection)
            if 0 <= index < len(sorted_models):
                selected_model = sorted_models[index].id
                print(f"已选择模型: {selected_model}")
            else:
                print("无效的序号。")
                return
        except ValueError:
            print("输入无效，请输入数字。")
            return

except Exception as e:
        print(f"\n❌ API 连接失败: {e}")
        print("无法连接到服务器。请检查网络或 API Key。")
        return

# 5. Configure Environment Variables
    print("\n正在配置全局环境变量 (Windows User Scope)...")

    # Core Anthropic Vars
    set_windows_env_var("ANTHROPIC_BASE_URL", config['anthropic_base_url'])
    set_windows_env_var("ANTHROPIC_AUTH_TOKEN", api_key)

    # Model Vars (Standard)
    # Applying selected model to all Standard Roles
    set_windows_env_var("ANTHROPIC_MODEL", selected_model)
    set_windows_env_var("ANTHROPIC_DEFAULT_OPUS_MODEL", selected_model)
    set_windows_env_var("ANTHROPIC_DEFAULT_SONNET_MODEL", selected_model)
    set_windows_env_var("ANTHROPIC_DEFAULT_HAIKU_MODEL", selected_model)
    set_windows_env_var("CLAUDE_CODE_SUBAGENT_MODEL", selected_model)

# Extra Vars (Provider specific)
    for key, val_template in config['extra_envs'].items():
        val = val_template.format(model=selected_model) # Format if placeholder exists
        set_windows_env_var(key, val)

print("\n✨ 配置完成！")
    print("************************************************")
    print(f" 提供商: {config['name']}")
    print(f" 模型  : {selected_model}")
    print(f" 接口  : {config['anthropic_base_url']}")
    print("************************************************")
    print("⚠️ 请注意：请务必 关闭并重新打开 您的终端窗口，以应用新的环境变量。")

if __name__ == "__main__":
    main()

使用时先运行step4，选择模型，填入API，即可享受经济实用型打工人了。如果想使用其他家的模型（只要支持claude code均可），直接让AI去修改即可，这里也给出提示词：

分析@Step4_SetAPI_And_Check_LLMModel.py

维持其他功能不变，修改这个文件，目标：支持第3个API 提供商GLM，配置相关变量ANTHROPIC_AUTH_TOKEN

ANTHROPIC_BASE_URL  [[链接已屏蔽])

CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 1

根据模型的具体参数修改上面三行即可。

**顾问 YH55729 (Rank 42) 的解答与建议**:
太好了，终于找到了便宜的使用打工人的方案，用kimi的api实在是太贵了

-----------------------------------------------------------------------------------------------------


---

### 技术对话片段 11 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-01-29

每日1+1，1SA+1RA，VF0.88，base10-12刀，稳稳的幸福

------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 12 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-01-30

统计了下目前更新OS的因子表现，12月和1月较11月及之前有了很大进步，期待VF和combine进一步提升。

------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 13 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026年1月31日

今日交了4个ra+1个sa，就是prod-corr限流实在是耽误事

----------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 14 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-5（补）

新的日记贴终于来了，上一个日记贴就写了一天的，赶紧补一补吧，好好写日记是非常好的习惯～

==========================================================================

==========================================================================


---

### 技术对话片段 15 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-6（补）

这个季度目标就是master，以及尽可能提高VF，目前进度还可以。30个塔已经点完了，combine也有1.4.

==========================================================================

==========================================================================


---

### 技术对话片段 16 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-7（补）

2月的vf更新的太早了，1月vf拿到了0.9，但只拿了三周的高base就结束了。不知道3月什么时候更新呀

==========================================================================

==========================================================================


---

### 技术对话片段 17 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-8（补）

最近交因子比较费劲，老断粮，多学习下论坛经验，提升下工作流吧

==========================================================================

==========================================================================


---

### 技术对话片段 18 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-9（补）

又断粮了，继续努力吧

==========================================================================

==========================================================================


---

### 技术对话片段 19 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-10（补）

不知道这个月的cobine performance能否上2，最近交的还不错，不过60个金字塔不是目前我能做到的

==========================================================================

==========================================================================


---

### 技术对话片段 20 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-11（补）

终于结束了断粮，美国的model出货率还不错～

==========================================================================

==========================================================================


---

### 技术对话片段 21 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-12（补）

美国是这个季度才开始做的，还得再多交一些，要不然区域的整体表现不够稳定

==========================================================================

==========================================================================


---

### 技术对话片段 22 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-13（补）

最近使用AI优化因子还比较有心得，感谢论坛分析得大佬们

==========================================================================

==========================================================================


---

### 技术对话片段 23 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-14（补）

看大佬分享，想要保持高vf，每个月的数量要尽量差不多，这个月稍微少了点，半个月才30来个因子，还得再加把劲

==========================================================================

==========================================================================


---

### 技术对话片段 24 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-15（补）

每天等待vf和combine更新，很焦虑啊

==========================================================================

==========================================================================


---

### 技术对话片段 25 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-16（补）

vf低，每天就5刀左右，赶紧更新吧。。

==========================================================================

==========================================================================


---

### 技术对话片段 26 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-17（补）

USA再交一交，再去补补IND吧，IND才交了30来个，还是不够稳定

==========================================================================

==========================================================================


---

### 技术对话片段 27 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-18（补）

combine终于更新了，小涨一点，再接再厉

==========================================================================

==========================================================================


---

### 技术对话片段 28 (原帖: Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。)
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
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-19

今天居然交满了4个ra和1个sa，真是难得啊

==========================================================================

==========================================================================


---

### 技术对话片段 29 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 YH55729 (Rank 42) 的解答与建议**:
2026-3-4

新的日记贴来了，继续记录。最近渗透分波动还可以，但是上限不高，最高才0.8，不知道怎样才能继续提升整体水平

=============================================================================


---

### 技术对话片段 30 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【经验分享】成为顾问一个月拿下Daily Osmosis Rank全球第一名经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (JM19072)**:
作为一名新手，第一次更新分数，碰巧拿到Daily Osmosis Rank为0.97分的全球并列第一，还是比较激动的，趁热来记录一下。


> [!NOTE] [图片 OCR 识别内容]
> 40T
> Value
> Oaily
> Factor
> Facor
> USIOSI5
> R1
> n


实话实说，我个人是不太确定为什么我能拿到这个分数的，甚至在半个月之前都不知道Osmosis怎么弄。多亏了我的朋友ZY36280帮助，我才入门，他的帖子对我启发也挺大，还有个人感触比较深的一些大佬的有关帖子，我一并放在下面链接中，朋友们可以在下面链接中看一看，希望对大家有帮助。

回到Osmosis，因为刚成为顾问不久，交的alpha以ppa为主，而且主要做月度主题，所以区域比较零散，往往每个区域仅仅能凑够10个提交最低标准，本想着拿个低保就可以，没想到给了我这么高的分数，所以我想我的一些思路和方向应该起码是对的。

- 提交alpha的标准要尽量高，这是基础。①我一般以Sharp 1.5，Fitness 1，为第一标准，没有的话就递减1，这样得到一批基础数值比较高的alpha。②再看拟合的曲线，如果是近几年横盘的曲线就不要了，因为Osmosis评分对近几年（我主要看21-23这三年）的表现很看重。③Performance Comparison曲线，只提交有提升的alpha，当然为了点塔，我也交小幅下降的。所以根据这些标准，我每天最多交2个，没有符合标准的我也会空仓不交。
- Osmosis打分，首先按指标排个序，然后看曲线和表格，近几年横盘甚至下降的剔除，或者为了凑个数打个比较低的分。然后按照指标顺序，把alpha页面截个屏投给AI，让AI帮我打分。打分权重，我比较看重Sharp、Fitness和Margin这三个，所以按3、0.3、0.2，其他占0.2，（这里可能不太对，欢迎大佬指正），总分100000，让AI给出每个的分数，然后我在此基础上稍微修正一下。
- 最近在尝试链接中的流程自动打分，试用过一次，很节省时间和精力，大家也可以尝试一下。


> [!NOTE] [图片 OCR 识别内容]
> 1NTT
> TI
> 4
> TMO


总之，alpha指标是基础，选择最高标准交。近几年表现比历史表现更重要。

[成为expert，vf连续三个月上0.9！！！ – WorldQuantBrain-CN](../顾问 MS51256 (Rank 28)/[Commented] 成为expertvf连续三个月上09经验分享.md)

[vf猛增0.48->0.98，第一次SA拿满60刀 – WorldQuantBrain-CN](../顾问 MS51256 (Rank 28)/[Commented] 成为expertvf连续三个月上09经验分享.md)

[【Community Leader -因子筛选与组合⭐】判断因子是否可以提交，稳住你的combine – WorldQuantBrain-CN](../顾问 LY85808 (Rank 86)/[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md)

[【Community Leader -因子筛选与组合⭐】维持高combine的秘密——基于近四个月提交的因子分析 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md)

[Osmosis competition 打分V2-精细化筛选alpha池 – WorldQuantBrain-CN](../顾问 LZ63377 (Rank 33)/[L2] Osmosis competition 打分V2-精细化筛选alpha池.md)

**顾问 YH55729 (Rank 42) 的解答与建议**:
想问下大佬，每个区域只赋10个因子左右，会不会OS不够稳定？

==============================================


---

### 技术对话片段 31 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】成为顾问一个月拿下Daily Osmosis Rank全球第一名经验分享_38898494065943.md
- **时间**: 3个月前

**提问/主帖背景 (JM19072)**:
作为一名新手，第一次更新分数，碰巧拿到Daily Osmosis Rank为0.97分的全球并列第一，还是比较激动的，趁热来记录一下。


> [!NOTE] [图片 OCR 识别内容]
> 40T
> Value
> Oaily
> Factor
> Facor
> USIOSI5
> R1
> n


实话实说，我个人是不太确定为什么我能拿到这个分数的，甚至在半个月之前都不知道Osmosis怎么弄。多亏了我的朋友ZY36280帮助，我才入门，他的帖子对我启发也挺大，还有个人感触比较深的一些大佬的有关帖子，我一并放在下面链接中，朋友们可以在下面链接中看一看，希望对大家有帮助。

回到Osmosis，因为刚成为顾问不久，交的alpha以ppa为主，而且主要做月度主题，所以区域比较零散，往往每个区域仅仅能凑够10个提交最低标准，本想着拿个低保就可以，没想到给了我这么高的分数，所以我想我的一些思路和方向应该起码是对的。

- 提交alpha的标准要尽量高，这是基础。①我一般以Sharp 1.5，Fitness 1，为第一标准，没有的话就递减1，这样得到一批基础数值比较高的alpha。②再看拟合的曲线，如果是近几年横盘的曲线就不要了，因为Osmosis评分对近几年（我主要看21-23这三年）的表现很看重。③Performance Comparison曲线，只提交有提升的alpha，当然为了点塔，我也交小幅下降的。所以根据这些标准，我每天最多交2个，没有符合标准的我也会空仓不交。
- Osmosis打分，首先按指标排个序，然后看曲线和表格，近几年横盘甚至下降的剔除，或者为了凑个数打个比较低的分。然后按照指标顺序，把alpha页面截个屏投给AI，让AI帮我打分。打分权重，我比较看重Sharp、Fitness和Margin这三个，所以按3、0.3、0.2，其他占0.2，（这里可能不太对，欢迎大佬指正），总分100000，让AI给出每个的分数，然后我在此基础上稍微修正一下。
- 最近在尝试链接中的流程自动打分，试用过一次，很节省时间和精力，大家也可以尝试一下。


> [!NOTE] [图片 OCR 识别内容]
> 1NTT
> TI
> 4
> TMO


总之，alpha指标是基础，选择最高标准交。近几年表现比历史表现更重要。

[成为expert，vf连续三个月上0.9！！！ – WorldQuantBrain-CN]([L2] 成为expertvf连续三个月上09经验分享_38720223996439.md)

[vf猛增0.48->0.98，第一次SA拿满60刀 – WorldQuantBrain-CN]([L2] 成为expertvf连续三个月上09经验分享_38720223996439.md)

[【Community Leader -因子筛选与组合⭐】判断因子是否可以提交，稳住你的combine – WorldQuantBrain-CN]([L2] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md)

[【Community Leader -因子筛选与组合⭐】维持高combine的秘密——基于近四个月提交的因子分析 – WorldQuant BRAIN]([L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md)

[Osmosis competition 打分V2-精细化筛选alpha池 – WorldQuantBrain-CN]([L2] Osmosis competition 打分V2-精细化筛选alpha池_37306268304791.md)

**顾问 YH55729 (Rank 42) 的解答与建议**:
想问下大佬，每个区域只赋10个因子左右，会不会OS不够稳定？

==============================================


---

### 技术对话片段 32 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (HP65370)**:
大家好，我是25年参加了IQC之后在7月1日左右拿到顾问权限的，刚开始什么都不懂，连ppa是什么都不知道，也不知道六维是什么，拿到权限的7天后才提交了自己的第一个顾问因子，最后也是从新手课和众多大佬的经验帖子里面逐渐熟悉规则，在789三个月里成功从gold冲到master，10 11 12三个月从master冲上了grandmaster。

**(一)Gold→Master**

在最终结算的时候我的六维:


> [!NOTE] [图片 OCR 识别内容]
> 编辑六维指标 
> 编辑六维指标数据
> Operator Count:
> Operator
> 69
> 4.2
> Field Count:
> Field
> 200
> 1.7
> Community Activity:
> Max Simulation Streak:
> 25
> 89
> 更新排名
> 以 Expert 为 Universe
> 以 Master 为 Universe
> Grandmaster 为 Universe
> 总排名:279/699
> 总排名:309
> 279
> 总排名:107
> 70
> Operator Count: 455 名
> Operator Count: 347 名
> Operator Count: 109名
> Operator
> 454名
> Operator
> 210名
> Operator AVg: 48名
> Field Count: 661 名
> Field Count: 395 名
> Field Count: 104 名
> Field AVg: 260名
> Field AVg: 103名
> Field AVg: 25 名
> Community Activity: 356名
> Community Activity: 291 名
> Community Activity: 92 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Max Simulation Streak: 1135 名
> Max Simulation Streak: 526 名
> Max Simulation Streak: 110名
> Total Rank: 3322名
> Total Rank: 1873名
> Total Rank: 489名
> AVg:
> AVg:
> AVg:
> AVg:


**我的提交与回测系统：**

我在7月，只做了eur和usa两个地区，一共提交了55个alpha，采用的是传统一二三阶代码，完全没有修改，但是最多只会做到二阶；在8月，做了glb、eur、asi，一共提交了73个alpha,由于传统二阶代码会严重拉跨平均操作符和平均字段，于是我逐渐舍弃二阶，并修改一阶中的模板；在9月，只做了usa这一个地区，由于时间不充裕，只交了23个alpha，延续了8月的风格，以压操作符和字段为主。

**我的combine:**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.16
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.38


当时也是很惊讶能有这么高，更新到6月也就是iqc期间，我的combine是0.34,第二次更新到7月，记得好像是1.2，第三次更新到8月，combine最高来到了2.38;提交的核心标准是margin要达标，turnover不能过高，其他的综合来看，觉得不是很难看就交了，除了二阶里面的group类型字段，几乎没有做过双字段的alpha。

(点塔图没有找到)

**（二）Master** → **Grandmaster**

最终结算的时候我的六维、combine、塔图:


> [!NOTE] [图片 OCR 识别内容]
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.69
> 125
> 1.34
> Fields used
> Community activity
> Max simulation streak
> 311
> 48.4
> 181



> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 3.02



> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> CHN
> KOR
> TN
> HKG
> JPN
> AMR
> Analyst
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 10
> 14
> 14
> 10
> 13
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


相比于上个赛季，我的工作流变化挺大的，

**1、提前过滤字段**

在传统一阶回测的时候经常会遇到缺数据的字段，这样既浪费了回测数量，也严重影响了我的心情，于是我以一个塔为单位，例如把一个region内所有归属于model的全部字段直接回测，提前把那些缺数据的字段拉黑，提高了后续回测任务的效率，并利用数据库来记录，判断缺数据的字段也很简单，利用api获取回测出来的alpha的每年的sharpe有多少个0就行了。

**2、优化模板流**

在传统的一阶回测或者是论坛中的一些模板，其大多都有个共性，也就是探索度太大了，在有限的回测次数内，出货效率很低，并且类似的模板对同一个字段跑出来的alpha的相关性过高，有时会花费过多回测数量在一个难以出货的字段上面，于是我做出改进，把每个模板 的探索度降为1，具体做法为：固定时间参数，固定操作符，比如group_op(ts_op(x,day),group),day我会取一个固定的值，group我只在market,industry,sector,subindustry中选一个，group_op我一般在group_rank,group_zscore,group_neutralize中选一个，ts_op也一样。目的是在较少的回测数量内挖掘出一个字段的基础信号，哪怕是微小信号也好。

其次，把这些表达式批量写入数据库，每一组回测完后就回填数据，计算相关性，并做好标记以免重复回测。

**3、对alpha的初加工**

对上述回测完的alpha进行进一步的改进，设立了一个评分机制，同一个数据字段内的alpha为一组，对组内的alpha以sharpe、fitness、margin为指标进行打分，选取分值最高的并且相关性小于0.5的那个进入下一步的加工环节，传统的二阶是对所有sharpe、fitness满足条件的alpha进行提升，可是在同一个数据字段内的alpha本身相关性就很高，可能交了一个alpha后其他alpha可能都交不了了，为何不选择一个最好的来做二阶呢。

加工我采用的是：遍历中性化、遍历时间参数、非线性变换、是否保留ts_backfill和winsorize；其中遍历时间参数以等差数列进行遍历，大约需要多回测9次，非线性变换主要包括tanh,sqrt,log,signed_power,arc_cos,exp；再批量把这些操作于这个分值最高的alpha上并写进数据库自动回测。

**4、对alpha的细加工**

对于初加工的alpha，我会人工去把它们组合起来，比如在最佳中性化下运用最佳的时间参数并看是否需要结合非线性变换，并确认是否需要删除多余操作符，把这样的表达式拿去平台回测，并进行细微的优化，比如turnover过高，我会加decay，weight超了，想办法去降。

**5、回测数量的分配**

每天回测就5000次，我们应该规划好这些次数拿来做什么，我是多塔同时出发，8个槽或者glb的四个槽，每一个槽都会回测不一样的塔，避免在一个难出的塔上面一直耗下去，在点亮了塔之后便停掉跑其他的，直到全部点亮或者点不亮时才会回去做一些好出的塔比如model、pv等凑数量。

其他的基本和Q3一样，比如提交标准没变，combine更新到11月，其最高combine来到了3.02，点塔也是一个月最多三个地区，每个地区在一个月内我会尽可能交三十多个，平均一天3个加一个superalpha，唯一的变数是在12月，我只做了两个地区，usa的d0和d1，平均每天只交了2个加一个superalpha，同样的在Q3的最后一月，提交的数量相较于上个月少了很多，两次都导致我的vf骤降，combine微跌，但是影响这两个指标变化的因素有很多，我也不知道为什么会这样。

**踩过的坑：**

对于新人来说，冲刺master或者grandmaster的第一阻碍或许是最大连续回测天数，我最初没有看懂这个以至于到了顾问阶段回测天数断了，若是中途断了就需要在六维的其他方面花费更多的精力。

**思考&改进：**

有些模板彼此间就有很强的相关性，做出来的alpha彼此间大概率也是高相关性，可以计算单个数据字段内alpha间互相的相关性，利用多组数据，找到均值比较高的那组，删去指标较差的那个模板，以此来简化模板流。（还没有时间做）

**总结：**

想要在genius中获得高评级，点塔、六维、combine缺一不可，核心都是在有限的回测次数内做出大量优质alpha。

===============================================

最后祝愿大家所愿皆所得，vf wf combine base genius全都升！

**顾问 YH55729 (Rank 42) 的解答与建议**:
太厉害了，第一个季度就能master，第二个季度就能GM，简直不敢想啊

==============================================


---

### 技术对话片段 33 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享_38932709256727.md
- **时间**: 3个月前

**提问/主帖背景 (HP65370)**:
大家好，我是25年参加了IQC之后在7月1日左右拿到顾问权限的，刚开始什么都不懂，连ppa是什么都不知道，也不知道六维是什么，拿到权限的7天后才提交了自己的第一个顾问因子，最后也是从新手课和众多大佬的经验帖子里面逐渐熟悉规则，在789三个月里成功从gold冲到master，10 11 12三个月从master冲上了grandmaster。

**(一)Gold→Master**

在最终结算的时候我的六维:


> [!NOTE] [图片 OCR 识别内容]
> 编辑六维指标 
> 编辑六维指标数据
> Operator Count:
> Operator
> 69
> 4.2
> Field Count:
> Field
> 200
> 1.7
> Community Activity:
> Max Simulation Streak:
> 25
> 89
> 更新排名
> 以 Expert 为 Universe
> 以 Master 为 Universe
> Grandmaster 为 Universe
> 总排名:279/699
> 总排名:309
> 279
> 总排名:107
> 70
> Operator Count: 455 名
> Operator Count: 347 名
> Operator Count: 109名
> Operator
> 454名
> Operator
> 210名
> Operator AVg: 48名
> Field Count: 661 名
> Field Count: 395 名
> Field Count: 104 名
> Field AVg: 260名
> Field AVg: 103名
> Field AVg: 25 名
> Community Activity: 356名
> Community Activity: 291 名
> Community Activity: 92 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Max Simulation Streak: 1135 名
> Max Simulation Streak: 526 名
> Max Simulation Streak: 110名
> Total Rank: 3322名
> Total Rank: 1873名
> Total Rank: 489名
> AVg:
> AVg:
> AVg:
> AVg:


**我的提交与回测系统：**

我在7月，只做了eur和usa两个地区，一共提交了55个alpha，采用的是传统一二三阶代码，完全没有修改，但是最多只会做到二阶；在8月，做了glb、eur、asi，一共提交了73个alpha,由于传统二阶代码会严重拉跨平均操作符和平均字段，于是我逐渐舍弃二阶，并修改一阶中的模板；在9月，只做了usa这一个地区，由于时间不充裕，只交了23个alpha，延续了8月的风格，以压操作符和字段为主。

**我的combine:**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.16
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.38


当时也是很惊讶能有这么高，更新到6月也就是iqc期间，我的combine是0.34,第二次更新到7月，记得好像是1.2，第三次更新到8月，combine最高来到了2.38;提交的核心标准是margin要达标，turnover不能过高，其他的综合来看，觉得不是很难看就交了，除了二阶里面的group类型字段，几乎没有做过双字段的alpha。

(点塔图没有找到)

**（二）Master** → **Grandmaster**

最终结算的时候我的六维、combine、塔图:


> [!NOTE] [图片 OCR 识别内容]
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.69
> 125
> 1.34
> Fields used
> Community activity
> Max simulation streak
> 311
> 48.4
> 181



> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 3.02



> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> CHN
> KOR
> TN
> HKG
> JPN
> AMR
> Analyst
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 10
> 14
> 14
> 10
> 13
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


相比于上个赛季，我的工作流变化挺大的，

**1、提前过滤字段**

在传统一阶回测的时候经常会遇到缺数据的字段，这样既浪费了回测数量，也严重影响了我的心情，于是我以一个塔为单位，例如把一个region内所有归属于model的全部字段直接回测，提前把那些缺数据的字段拉黑，提高了后续回测任务的效率，并利用数据库来记录，判断缺数据的字段也很简单，利用api获取回测出来的alpha的每年的sharpe有多少个0就行了。

**2、优化模板流**

在传统的一阶回测或者是论坛中的一些模板，其大多都有个共性，也就是探索度太大了，在有限的回测次数内，出货效率很低，并且类似的模板对同一个字段跑出来的alpha的相关性过高，有时会花费过多回测数量在一个难以出货的字段上面，于是我做出改进，把每个模板 的探索度降为1，具体做法为：固定时间参数，固定操作符，比如group_op(ts_op(x,day),group),day我会取一个固定的值，group我只在market,industry,sector,subindustry中选一个，group_op我一般在group_rank,group_zscore,group_neutralize中选一个，ts_op也一样。目的是在较少的回测数量内挖掘出一个字段的基础信号，哪怕是微小信号也好。

其次，把这些表达式批量写入数据库，每一组回测完后就回填数据，计算相关性，并做好标记以免重复回测。

**3、对alpha的初加工**

对上述回测完的alpha进行进一步的改进，设立了一个评分机制，同一个数据字段内的alpha为一组，对组内的alpha以sharpe、fitness、margin为指标进行打分，选取分值最高的并且相关性小于0.5的那个进入下一步的加工环节，传统的二阶是对所有sharpe、fitness满足条件的alpha进行提升，可是在同一个数据字段内的alpha本身相关性就很高，可能交了一个alpha后其他alpha可能都交不了了，为何不选择一个最好的来做二阶呢。

加工我采用的是：遍历中性化、遍历时间参数、非线性变换、是否保留ts_backfill和winsorize；其中遍历时间参数以等差数列进行遍历，大约需要多回测9次，非线性变换主要包括tanh,sqrt,log,signed_power,arc_cos,exp；再批量把这些操作于这个分值最高的alpha上并写进数据库自动回测。

**4、对alpha的细加工**

对于初加工的alpha，我会人工去把它们组合起来，比如在最佳中性化下运用最佳的时间参数并看是否需要结合非线性变换，并确认是否需要删除多余操作符，把这样的表达式拿去平台回测，并进行细微的优化，比如turnover过高，我会加decay，weight超了，想办法去降。

**5、回测数量的分配**

每天回测就5000次，我们应该规划好这些次数拿来做什么，我是多塔同时出发，8个槽或者glb的四个槽，每一个槽都会回测不一样的塔，避免在一个难出的塔上面一直耗下去，在点亮了塔之后便停掉跑其他的，直到全部点亮或者点不亮时才会回去做一些好出的塔比如model、pv等凑数量。

其他的基本和Q3一样，比如提交标准没变，combine更新到11月，其最高combine来到了3.02，点塔也是一个月最多三个地区，每个地区在一个月内我会尽可能交三十多个，平均一天3个加一个superalpha，唯一的变数是在12月，我只做了两个地区，usa的d0和d1，平均每天只交了2个加一个superalpha，同样的在Q3的最后一月，提交的数量相较于上个月少了很多，两次都导致我的vf骤降，combine微跌，但是影响这两个指标变化的因素有很多，我也不知道为什么会这样。

**踩过的坑：**

对于新人来说，冲刺master或者grandmaster的第一阻碍或许是最大连续回测天数，我最初没有看懂这个以至于到了顾问阶段回测天数断了，若是中途断了就需要在六维的其他方面花费更多的精力。

**思考&改进：**

有些模板彼此间就有很强的相关性，做出来的alpha彼此间大概率也是高相关性，可以计算单个数据字段内alpha间互相的相关性，利用多组数据，找到均值比较高的那组，删去指标较差的那个模板，以此来简化模板流。（还没有时间做）

**总结：**

想要在genius中获得高评级，点塔、六维、combine缺一不可，核心都是在有限的回测次数内做出大量优质alpha。

===============================================

最后祝愿大家所愿皆所得，vf wf combine base genius全都升！

**顾问 YH55729 (Rank 42) 的解答与建议**:
太厉害了，第一个季度就能master，第二个季度就能GM，简直不敢想啊

==============================================


---

### 技术对话片段 34 (原帖: 【经验分享】新人如何Combine 2.3， VF 0.9经验分享)
- **原帖链接**: [Commented] 【经验分享】新人如何Combine 23 VF 09经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (ZZ51745)**:
首先明确一点，提交的质量才是最重要的

我是11月中才成为顾问的，那时候算是最后的好日子了，回测数还没有限制，每天可以大量的回测，各种想法都可以试试，然后优中选优，每天只提交最好的，下面的Combine就是一月的时候刷新的，对应我11月的提交，应该算是很不错的了


> [!NOTE] [图片 OCR 识别内容]
> 2
> Combined Alpha Performance
> 2.47
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 1.79
> 0.5


然后到12月，增加了回测数量的限制，那时候就感觉回测数不够用了，经常跑一半就用完了，要等第二天，很多想法也没办法尝试了，提交的质量比起11月肯定是下滑的。

再加上还要兼顾点塔，我当时想着至少把塔点到master试试，所以很多时候为了点塔质量低的也就交了，可惜最后虽然塔点够了，六维却不够，别说master了，连expert都没选上，可惜可惜。

这是前几天刷新的，对应11月，12月的提交，可以看到，数据明显是降低了，我自己也早就觉得这次数据肯定是要降的。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.3
> Reached Grandmaster
> Combined Selected Alpha Performance
> No matching Alphas; refreshed monthly
> Combined Power Pool Alpha Performance
> 1.54


至于VF，也是刷新了两次了，从默认的0.5 ，第一次刷新是0.8，前几天第二次刷是0.9，感觉这个就不只是表现，还有时间积累了，可能持续提交高质量的，VF才会一直保持高位吧

至于我提交的底线呢，Sharpe Fitness 越高越好这不用说，主要是 Turnover要求是3-50，最后是Margin，这个要看不同的地区，普遍比较高的地区底线就是10，差一些的地区底线是5，这是真的底线了，低于这个的基本不会交，只有一两个为了点塔交过。

总之，结合我自己的情况以及论坛里各个大佬的观点呢，提交的质量肯定是影响Combine 的重要因素，只不过现在WQ平台的限制越来越多，而且还有点塔的要求，我自己也有为了点塔放弃底线的例子，这些各方面的取舍只能是各位自行选择了。

**顾问 YH55729 (Rank 42) 的解答与建议**:
好厉害啊，学习了，同样是新人，目前combine才1.4，vf上了0.88又掉下去了。

=============================================================================


---

### 技术对话片段 35 (原帖: 【经验分享】新人如何Combine 2.3， VF 0.9经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】新人如何Combine 23 VF 09经验分享_38376574647447.md
- **时间**: 4个月前

**提问/主帖背景 (ZZ51745)**:
首先明确一点，提交的质量才是最重要的

我是11月中才成为顾问的，那时候算是最后的好日子了，回测数还没有限制，每天可以大量的回测，各种想法都可以试试，然后优中选优，每天只提交最好的，下面的Combine就是一月的时候刷新的，对应我11月的提交，应该算是很不错的了


> [!NOTE] [图片 OCR 识别内容]
> 2
> Combined Alpha Performance
> 2.47
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 1.79
> 0.5


然后到12月，增加了回测数量的限制，那时候就感觉回测数不够用了，经常跑一半就用完了，要等第二天，很多想法也没办法尝试了，提交的质量比起11月肯定是下滑的。

再加上还要兼顾点塔，我当时想着至少把塔点到master试试，所以很多时候为了点塔质量低的也就交了，可惜最后虽然塔点够了，六维却不够，别说master了，连expert都没选上，可惜可惜。

这是前几天刷新的，对应11月，12月的提交，可以看到，数据明显是降低了，我自己也早就觉得这次数据肯定是要降的。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.3
> Reached Grandmaster
> Combined Selected Alpha Performance
> No matching Alphas; refreshed monthly
> Combined Power Pool Alpha Performance
> 1.54


至于VF，也是刷新了两次了，从默认的0.5 ，第一次刷新是0.8，前几天第二次刷是0.9，感觉这个就不只是表现，还有时间积累了，可能持续提交高质量的，VF才会一直保持高位吧

至于我提交的底线呢，Sharpe Fitness 越高越好这不用说，主要是 Turnover要求是3-50，最后是Margin，这个要看不同的地区，普遍比较高的地区底线就是10，差一些的地区底线是5，这是真的底线了，低于这个的基本不会交，只有一两个为了点塔交过。

总之，结合我自己的情况以及论坛里各个大佬的观点呢，提交的质量肯定是影响Combine 的重要因素，只不过现在WQ平台的限制越来越多，而且还有点塔的要求，我自己也有为了点塔放弃底线的例子，这些各方面的取舍只能是各位自行选择了。

**顾问 YH55729 (Rank 42) 的解答与建议**:
好厉害啊，学习了，同样是新人，目前combine才1.4，vf上了0.88又掉下去了。

=============================================================================


---

### 技术对话片段 36 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】第一个35SA的生成之路-你认为的好对SA来说不一定真的好_39035430170135.md
- **时间**: 3个月前

**提问/主帖背景 (ZM10537)**:
今天我做出了第一个35的SA，本篇文章记录自己的思考过程，也希望能为朋友们带来一点制作SA的灵感。先说结论：
 **做SA并不是要选择一批很好的因子，而是要选择一批组合起来很好的因子，并不需要其中每个因子的效果都很优秀** 。

最开始我还是跟随着原来的思路，选择自认为表现好的因子，于是有了以下selection：
 
> [!NOTE] [图片 OCR 识别内容]
> Selection Expression
> not(own )
> & in(classifications,
> ATON"
> (turnover
> 8.05
> turnover
> 0.1)
> (turnover
> 0.12
> && turnover
> 0.17)
> (turnover
> 0.19 &&
> turnover
> 0.25)
> && (prod_correlation
> 8.05
> && prod_correlation
> 8.5)
> 跽 (self_correlation
> 8.5)
> & (operator_Count
> 10)
> (simoid(turnover)
> Sqrt (add (abs (Iong
> Count
> short_count), 1) )
> Sqrt (operator
> Count))
> RunSlecton
> Combo Expression
 
咋一看还挺像一回事，选择ATOM，保证每个因子都不混信号；保证较低的pc与sc；较低的操作符数量并且惩罚高操作符，避免每个因子过拟合；惩罚高turnover；惩罚多空差值更大的保证每个因子多空尽量保持均衡。看起来是选择了一批不错的因子，然而组合后并不好。
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sh3「0
> TUFMOIEr
> TMeSs
> RetUFn
> UraVUTIT
> Marein
> 3.67
> 9.6896
> 3.04
> 8.56%
> 2.209
> 17.699600
 
查看select all窗口查看，发现绝大多数的因子的margin都很低，但是作为一个expert，我能动用的因子其实并不多，因此我做了第一个改动，将ATOM删掉，不选了！
 
> [!NOTE] [图片 OCR 识别内容]
> not
> Own )
> 龊 in(classifications
> "ATON"
> (turnover
> 8.05 &&
> turnover
> 0.1)
> (turnover
> 0.12 &&
> turnover
> 0.17)
> (turnover
> O.19  &
> turnover
> 0.25 )
> 龊 (prod_correlation
> 8.05 && prod_correlation
> 0.5)
> 龊 (self_correlation
> 8.5)
> 龊 (operator
> Count
> 10)
> Qsigmoid
> turnover
> Sqrt (add(abs(1ong_
> Count
> short_Count),
> 1 )
> Sqrt (operator
> count /
 
然而并没有什么变化。很正常，因为顾问大多数做的其实都是ATOM。在因子有限的情况下，这个限制变化并不大。于是有了第二个改动，根据游戏王的框架，从数据种类入手。
 
> [!NOTE] [图片 OCR 识别内容]
> Selection Expression
> not (own)
> 龊 in(classifications,
> ATON"
> i(datacategories,
> "fundamental"
> in(datacategories,
> analyst
> in(datacategories,
> model
> in(datacategories,
> Tews
> in(datacategories,
> pisk"
> in(datacategories
> (turnover
> 8.05 &&
> turnover
> 0.1)
> (turnover
> 0.12
> 龊 turnover
> 0.17)
> (turnover
> 0.19
> 龊 turnover
> 0.25)
> (prod_
> correlation
> 05 && prod_correlation
> 8.5)
> (self
> correlation
> 8.5)
> 龊 (operator_Count
> 10)
> (datafield
> Count
> (sigmoid(turnover)
> Sqrt (add (ab5
> count-short_count ),
> 1) )
> sqrt (operator_count )
> RUSletlom
> Iong
 
有变化，但变化不大。
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> 05
> Aggregate Data
> Sharpe
> JUTICE
> Fitness
> Re-urns
> OTaWOUVn
> MarEin
> 3.94
> 10.629
> 3.17
> 8.079
> 1.6796
> 15.209600
 
可以发现，在分子部分我能做的其实不多了，在本身因子权限就非常有限的情况下，我现在能修改的就是分母以及参数。对于分母来说，惩罚高turnover，惩罚多空差距过大，惩罚操作符数量过多，第一个与第三个能优化的不多（其实能优化，后面就优化了），于是对第二个进行了多空差值进行修改，在游戏王的帖子中，我发现有直接使用long_count进行惩罚，我进行了尝试，于是有了接下来的版本：
 
> [!NOTE] [图片 OCR 识别内容]
> Selection Expression
> not(Own)
> 龊 in(classifications,
> ATON"
> in(datacategories,
> fundamental
> i(datacategories
> analyst"
> i(datacategories
> model
> i(datacategories
> news
> i(datacategories,
> "pisk"
> i(datacategories
> (turnover
> 8.05 &&
> turnover
> 0.1)
> (turnover
> 0.12  &
> turnover
> 0.17)
> (turnover
> O.19  &
> turnover
> 0.25)
> 龊 (prod_correlation
> 8.05 && prod_correlation
> 0.5)
> 龊 (self_correlation
> 8.5)
> Operator
> Count
> 10)
> ! (datafield_
> Count
> 〈二3〉
> (sigmoid
> turnover )
> 5qrt (LonB_
> Count )
> sqrt (operator
> Count
 
立竿见影啊！fitness大提升！从双3变成双4了。我将这个变化交给了AI，AI这么回答我： **你这条 selection 可能不是在筛“单个质量最高的因子”，而是在筛“更适合做等权组合的一批因子”。** 
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sharpe
> TITMTIIE
> Fitnas
> FSTIC
> DCammOo
> Marein
> 4.23
> 10.6996
> 4.06
> 11.5396
> 2.0996
> 21.579600
 
于是我将对operator的惩罚变成了对pc的惩罚，因为 **pc越低组合效果越好** 。于是有了接下来的版本。
 
> [!NOTE] [图片 OCR 识别内容]
> Selection Expression
> not
> Own )
> 龊 in(classifications,
> ATON" )
> i(datacategories
> "fundamental"
> in(datacategories,
> analyst
> in(datacategories,
> model
> in(datacategories_
> news
> in(datacategories,
> risk"
> in(datacategories_
> (turnover
> 8.05 &&
> turnover
> 0.1)
> (turnover
> 0.12 &&
> turnover
> 0.17)
> (turnover
> 0.19 &&
> turnover
> 0.25 )
> 16
> 跽 (prod_
> correlation
> 8.05 && prod_correlation
> 8.5)
> 跽 (self
> correlation
> 跽 (operator
> Count
> 10)
> & (datafield_
> Count
> (simoid(turnover)
> sqrt(Iong_count)
> sigmoid (prod_correlation )
 
立竿见影啊！效果又好了一大截！
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sharpe
> TUITnUIE[
> Cte
> eTITn =
> Drswoown
> Warain
> 4.82
> 11.329
> 4.52
> 11.00%
> 1.81%
> 19.459600
 
接下来我对turnover进行了修改，从惩罚高turnover变成了惩罚距离turnover中心点更远的。
 
> [!NOTE] [图片 OCR 识别内容]
> Selection Expression
> not(own)
> 龊 in(classifications,
> ATON )
> i(datacategories,
> fundamental"
> 11 in(datacategories,
> analyst
> in(datacategories
> model
> 1 in(datacategories
> Tews
> in(datacategories,
> pisk"
> in(datacategories,
> (turnover
> 8.05 && turnover
> 0.1)
> 11 (turnover
> 0.12
> & turnover
> 0.17)
> 15
> (turnover
> 0.19
> turnover
> 0.25)
> && (prod
> correlation
> && prod_correlation
> 8.5)
> (self
> correlation
> 8.5)
> && (operator
> Count
> 10)
> && (datafield
> Count
> 〈二3
> (simoid(abs (turnover-O.1) )
> sqrt(long_count )
> simoid(prod
> correlation) )
 
并没有什么效果。这更加说明了 **看起来更好的因子，可能对SA并不好** 。
 
> [!NOTE] [图片 OCR 识别内容]
> 叫
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sharoe
> UTICEI
> TItnEs
> TeCUTI
> F3MOOVT
> Marain
> 4.78
> 11.419
> 4.50
> 11.0896
> 1.7896
> 19.439600
 
selection在当前思路下几乎没有优化空间了，怎么办呢？只能修改Selection Limit，于是我将limit从30增加到了50。
效果爆炸！简直不可思议！
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> TUITnUIE[
> Titne
> ReTUTn
> OCa
> Warain
> 5.40
> 10.489
> 5.54
> 13.159
> 1.349
> 25.099600
> Snror
 
但是很可惜的是pc超了，距离35一步之遥。查看selected alphas，只有48个被选中了，分母的惩罚几乎无意义，于是我放宽了pc（反正分母对pc做了惩罚）。
 
> [!NOTE] [图片 OCR 识别内容]
> not(own )
> & in(classifications,
> ATON"
> in(datacategories,
> fundamental"
> i(datacategories,
> analyst"
> i(datacategories,
> model"
> in(datacategories_
> news
> in(datacategories, "risk"
> in(datacategories_
> (turnover
> 8.05
> turnover
> 0.1)
> (turnover
> 0.12
> & turnover
> 0.17)
> (turnover
> 0.19
> & turnover
> 0.25)
> & (prod_correlation
> 8.05
> 8& prod_correlation
> 8.6)
> 跽 (self_correlation
> 8.5)
> & (operator_Count
> 10)
> & (datafield
> Count
> 〈二3〉
> (5i
> ab5 (turnover-O.1) )
> sqrt(long_count )
> sigmoid(prod_corpelation )
> pv
> Bmoid
 
效果更加爆炸了！简直不可思议！
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sharoe
> UTICEI
> Fitness
> TeCUTI
> F3MOOVT
> Marain
> 6.15
> 10.199
> 6.71
> 14.9096
> 2.5696
> 29.249600
 
修改一下combo，pc也过了。于是第一个35就产生了。
我将思考过程交给了AI，AI告诉我： **Selection 的最优，不一定是更严，而可能是更宽但更均衡。** 
如果本贴能为各位朋友带来一丝丝灵感，不胜荣幸。

**顾问 YH55729 (Rank 42) 的解答与建议**:
学习一下，一直不敢做not own的sa，怕影响vf

==========================================================================


---

### 技术对话片段 37 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【课代表】【轻松点击即可完成参赛】CA 降维  多指标聚类数评判  KMeans  层次  DBSCAN 聚类的 Osmosis 点数分配工具经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (XX42289)**:
# 特此感谢 [BJ65592](/hc/en-us/profiles/34337104554903-BJ65592) 的付出。

```
import urllib.parseimport loggingimport numpy as npimport pandas as pdfrom datetime import datetimefrom sklearn.preprocessing import StandardScaler, RobustScalerfrom sklearn.cluster import KMeans, DBSCAN, AgglomerativeClusteringfrom sklearn.metrics import silhouette_score, calinski_harabasz_scorefrom sklearn.decomposition import PCA# 假设该库返回requests.Session对象from machine_lib import login  def get_history_alpha_ids(s, region, start_date, limit=50, offset=0):    """    从接口分页获取指定地区、指定日期后的alpha数据    :param s: requests.Session对象，已完成登录的会话    :param region: 地区大写：USA, EUR ... ...    :param start_date: 过滤日期，获取该日期之后的因子    :param limit: 每页获取的数量    :param offset: 分页偏移量    :return: 包含alpha的id和各类is指标的列表    """    alphas_data = []    # 对日期字符串进行URL编码，避免特殊字符影响请求    start_date_str = urllib.parse.quote(start_date.astimezone().isoformat(timespec='seconds'))    # 分页获取数据    while True:        url = (            f"[链接已屏蔽]            f"limit={limit}&offset={offset}"            f"&dateCreated%3E={start_date_str}"            f"&settings.region={region}"            f"&status!=UNSUBMITTED%1FIS-FAIL"            f"&hidden=false"            f"&order=-dateSubmitted"        )        try:            resp = s.get(url)            if resp.status_code != 200:                print(f"请求出错，状态码：{resp.status_code}")                break            data = resp.json()            results = data.get("results", [])            alphas_data.extend(results)            # 判断是否获取完所有数据，是则退出循环            if offset + len(results) >= data.get("count", 0) or len(results) < limit:                break            offset += limit        except Exception as e:            print(f"数据获取异常，异常信息：{e}")            break    # 提取需要的指标数据    alpha_metrics = []    for item in alphas_data:        # 检查is中的关键指标是否存在，避免键缺失报错        is_data = item.get('is', {})        metrics = {            'id': item['id'],            'fitness': is_data.get('fitness', 0.0),            'longCount': is_data.get('longCount', 0.0),            'shortCount': is_data.get('shortCount', 0.0),            'turnover': is_data.get('turnover', 0.0),            'returns': is_data.get('returns', 0.0),            'drawdown': is_data.get('drawdown', 0.0),            'margin': is_data.get('margin', 0.0),            'sharpe': is_data.get('sharpe', 0.0)        }        alpha_metrics.append(metrics)    if not alpha_metrics:        print("错误：没有获取到有效的alpha数据")        return []    return alpha_metricsdef determine_clusters_multi_criteria(X, min_clusters=5, max_clusters=50):    """    多指标确定聚类数（结合轮廓系数、CH指数，同时限制聚类数范围）    :param X: 标准化后的特征数据    :param min_clusters: 最小聚类数（避免过少）    :param max_clusters: 最大聚类数（避免过多）    :return: 最终聚类数量    """    if len(X) <= min_clusters:        return len(X)  # 样本数少于最小聚类数时，取样本数    # 限制聚类数范围：2 ~ 样本数（但不超过max_clusters，不低于min_clusters）    cluster_range = range(max(2, min_clusters), min(max_clusters + 1, len(X)))    scores = []    for k in cluster_range:        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')        labels = kmeans.fit_predict(X)        # 轮廓系数：衡量聚类紧密度和分离度，越接近1越好        sil_score = silhouette_score(X, labels)        # CH指数：数值越大表示聚类效果越好（类内紧密，类间分离）        ch_score = calinski_harabasz_score(X, labels)        # 综合得分（归一化后加权，可调整权重）        scores.append({            'k': k,            'sil': sil_score,            'ch': ch_score,            # 权重可调整，平衡轮廓系数和CH指数的影响            'composite': 0.4 * sil_score + 0.6 * (ch_score / 100000)        })    # 转换为DataFrame方便排序    score_df = pd.DataFrame(scores)    # 按综合得分降序排序，取第一个作为最佳聚类数    best_k = score_df.sort_values('composite', ascending=False)['k'].iloc[0]    # 兜底：确保聚类数在合理范围    best_k = max(min_clusters, min(best_k, max_clusters))    return best_kdef cluster_alphas_improved(alpha_metrics, use_pca=True, cluster_algorithm='kmeans'):    """    改进的聚类逻辑：支持PCA降维、多种聚类算法、多指标确定聚类数    :param alpha_metrics: alpha的指标数据    :param use_pca: 是否使用PCA降维（处理特征冗余）    :param cluster_algorithm: 聚类算法（kmeans/agglomerative/dbscan）    :return: 选中的alpha列表（每个聚类fitness最大）    """    # 转换为DataFrame方便处理    df = pd.DataFrame(alpha_metrics)    # 定义用于聚类的特征列    feature_cols = ['longCount', 'shortCount', 'turnover', 'returns', 'drawdown', 'margin', 'sharpe']    # 提取特征数据，处理缺失值（填充0）    X = df[feature_cols].fillna(0).values    # 改进1：使用RobustScaler标准化（抗异常值，比StandardScaler更适合金融数据）    scaler = RobustScaler()  # 替代StandardScaler，对异常值不敏感    X_scaled = scaler.fit_transform(X)    # 改进2：PCA降维（处理特征冗余，减少噪声）    if use_pca and len(feature_cols) > 2:        # 保留95%的方差，自动确定降维后的维度        pca = PCA(n_components=0.95, random_state=42)        X_processed = pca.fit_transform(X_scaled)        print(f"PCA降维后，特征维度从{len(feature_cols)}变为{X_processed.shape[1]}")    else:        X_processed = X_scaled    # 改进3：多指标确定聚类数（避免聚类数过少）    best_k = determine_clusters_multi_criteria(X_processed, min_clusters=5, max_clusters=50)    print(f"改进后确定的最佳聚类数量：{best_k}")    # 改进4：支持多种聚类算法（KMeans/层次聚类/DBSCAN）    if cluster_algorithm == 'kmeans':        # KMeans：适合球形分布，速度快        cluster_model = KMeans(n_clusters=best_k, random_state=42, n_init='auto')        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'agglomerative':        # 层次聚类：不假设球形分布，更灵活        cluster_model = AgglomerativeClustering(n_clusters=best_k)        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'dbscan':        # DBSCAN：无需指定聚类数，自动识别密度聚类（适合非球形分布）        # eps和min_samples可调整：eps越大，聚类数越少；min_samples越大，聚类数越多        cluster_model = DBSCAN(eps=0.5, min_samples=5)        df['cluster'] = cluster_model.fit_predict(X_processed)        # DBSCAN的-1表示噪声点，单独处理为一个聚类        noise_cluster = df['cluster'].max() + 1        df.loc[df['cluster'] == -1, 'cluster'] = noise_cluster        best_k = len(df['cluster'].unique())        print(f"DBSCAN聚类后实际聚类数量：{best_k}")    # 每个聚类中选择fitness最大的alpha    selected_alphas = []    for cluster in df['cluster'].unique():        cluster_df = df[df['cluster'] == cluster]        # 取fitness最大的行        best_alpha = cluster_df.loc[cluster_df['fitness'].idxmax()]        selected_alphas.append(best_alpha.to_dict())    return selected_alphasif __name__ == '__main__':    # 配置参数：顾问相关日期、分页参数    advisor_date = datetime(2020, 1, 1)  # 成为顾问的日期，用于过滤该日期之后的因子    page_limit = 100  # 每页获取的alpha数量    page_offset = 0   # 分页起始偏移量    target_region = "EUR"  # 目标地区    # 初始化登录会话    session = login()    logging.info("登录成功，开始获取alpha数据")    # 获取alpha的指标数据    alpha_metrics_list = get_history_alpha_ids(        s=session,        region=target_region,        start_date=advisor_date,        limit=page_limit,        offset=page_offset    )    # 校验数据是否有效    if not alpha_metrics_list:        print("程序终止：未获取到有效alpha数据")        exit(1)    # 执行聚类并选择每个类别中fitness最大的alpha    selected_alpha_list = cluster_alphas_improved(        alpha_metrics=alpha_metrics_list,        use_pca=True,        cluster_algorithm='kmeans'    )    # 校验聚类结果    if not selected_alpha_list:        print("程序终止：聚类后未选中任何alpha")        exit(1)    # 计算平均权重并分配分数（总分为100000）    total_selected = len(selected_alpha_list)    per_alpha_weight = 1.0 / total_selected if total_selected > 0 else 0.0    total_allocated_score = 0    # 遍历选中的alpha，输出信息并计算分数    for alpha_info in selected_alpha_list:        alpha_score = int(per_alpha_weight * 100000)        print(            f"Alpha ID：{alpha_info['id']} | "            f"Fitness值：{alpha_info['fitness']} | "            f"所属聚类：{alpha_info['cluster']} | "            f"分配分数：{alpha_score}"        )        # 如需调用接口更新分数，取消以下注释        update_url = f"[链接已屏蔽]        session.patch(update_url, json={"osmosisPoints": alpha_score})        total_allocated_score += alpha_score    # 处理四舍五入导致的分数偏差    score_deviation = 100000 - total_allocated_score    if score_deviation != 0:        print(f"\n因四舍五入产生分数偏差：{score_deviation}分，已将偏差分加到第一个Alpha上")        # 修正第一个Alpha的分数        first_alpha_score = int(per_alpha_weight * 100000) + score_deviation        print(f"第一个Alpha {selected_alpha_list[0]['id']} 的最终分数：{first_alpha_score}")        total_allocated_score = 100000    # 输出最终分配结果    print(f"\n分数分配完成：总分配分数 {total_allocated_score} 分，无分数损耗")
```

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢课代表，准备拿点渗透分了

===================================================================================


---

### 技术对话片段 38 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【课代表】【轻松点击即可完成参赛】CA 降维  多指标聚类数评判  KMeans  层次  DBSCAN 聚类的 Osmosis 点数分配工具经验分享_37023499938327.md
- **时间**: 3个月前

**提问/主帖背景 (XX42289)**:
# 特此感谢 [BJ65592](/hc/en-us/profiles/34337104554903-BJ65592) 的付出。

```
import urllib.parseimport loggingimport numpy as npimport pandas as pdfrom datetime import datetimefrom sklearn.preprocessing import StandardScaler, RobustScalerfrom sklearn.cluster import KMeans, DBSCAN, AgglomerativeClusteringfrom sklearn.metrics import silhouette_score, calinski_harabasz_scorefrom sklearn.decomposition import PCA# 假设该库返回requests.Session对象from machine_lib import login  def get_history_alpha_ids(s, region, start_date, limit=50, offset=0):    """    从接口分页获取指定地区、指定日期后的alpha数据    :param s: requests.Session对象，已完成登录的会话    :param region: 地区大写：USA, EUR ... ...    :param start_date: 过滤日期，获取该日期之后的因子    :param limit: 每页获取的数量    :param offset: 分页偏移量    :return: 包含alpha的id和各类is指标的列表    """    alphas_data = []    # 对日期字符串进行URL编码，避免特殊字符影响请求    start_date_str = urllib.parse.quote(start_date.astimezone().isoformat(timespec='seconds'))    # 分页获取数据    while True:        url = (            f"[链接已屏蔽]            f"limit={limit}&offset={offset}"            f"&dateCreated%3E={start_date_str}"            f"&settings.region={region}"            f"&status!=UNSUBMITTED%1FIS-FAIL"            f"&hidden=false"            f"&order=-dateSubmitted"        )        try:            resp = s.get(url)            if resp.status_code != 200:                print(f"请求出错，状态码：{resp.status_code}")                break            data = resp.json()            results = data.get("results", [])            alphas_data.extend(results)            # 判断是否获取完所有数据，是则退出循环            if offset + len(results) >= data.get("count", 0) or len(results) < limit:                break            offset += limit        except Exception as e:            print(f"数据获取异常，异常信息：{e}")            break    # 提取需要的指标数据    alpha_metrics = []    for item in alphas_data:        # 检查is中的关键指标是否存在，避免键缺失报错        is_data = item.get('is', {})        metrics = {            'id': item['id'],            'fitness': is_data.get('fitness', 0.0),            'longCount': is_data.get('longCount', 0.0),            'shortCount': is_data.get('shortCount', 0.0),            'turnover': is_data.get('turnover', 0.0),            'returns': is_data.get('returns', 0.0),            'drawdown': is_data.get('drawdown', 0.0),            'margin': is_data.get('margin', 0.0),            'sharpe': is_data.get('sharpe', 0.0)        }        alpha_metrics.append(metrics)    if not alpha_metrics:        print("错误：没有获取到有效的alpha数据")        return []    return alpha_metricsdef determine_clusters_multi_criteria(X, min_clusters=5, max_clusters=50):    """    多指标确定聚类数（结合轮廓系数、CH指数，同时限制聚类数范围）    :param X: 标准化后的特征数据    :param min_clusters: 最小聚类数（避免过少）    :param max_clusters: 最大聚类数（避免过多）    :return: 最终聚类数量    """    if len(X) <= min_clusters:        return len(X)  # 样本数少于最小聚类数时，取样本数    # 限制聚类数范围：2 ~ 样本数（但不超过max_clusters，不低于min_clusters）    cluster_range = range(max(2, min_clusters), min(max_clusters + 1, len(X)))    scores = []    for k in cluster_range:        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')        labels = kmeans.fit_predict(X)        # 轮廓系数：衡量聚类紧密度和分离度，越接近1越好        sil_score = silhouette_score(X, labels)        # CH指数：数值越大表示聚类效果越好（类内紧密，类间分离）        ch_score = calinski_harabasz_score(X, labels)        # 综合得分（归一化后加权，可调整权重）        scores.append({            'k': k,            'sil': sil_score,            'ch': ch_score,            # 权重可调整，平衡轮廓系数和CH指数的影响            'composite': 0.4 * sil_score + 0.6 * (ch_score / 100000)        })    # 转换为DataFrame方便排序    score_df = pd.DataFrame(scores)    # 按综合得分降序排序，取第一个作为最佳聚类数    best_k = score_df.sort_values('composite', ascending=False)['k'].iloc[0]    # 兜底：确保聚类数在合理范围    best_k = max(min_clusters, min(best_k, max_clusters))    return best_kdef cluster_alphas_improved(alpha_metrics, use_pca=True, cluster_algorithm='kmeans'):    """    改进的聚类逻辑：支持PCA降维、多种聚类算法、多指标确定聚类数    :param alpha_metrics: alpha的指标数据    :param use_pca: 是否使用PCA降维（处理特征冗余）    :param cluster_algorithm: 聚类算法（kmeans/agglomerative/dbscan）    :return: 选中的alpha列表（每个聚类fitness最大）    """    # 转换为DataFrame方便处理    df = pd.DataFrame(alpha_metrics)    # 定义用于聚类的特征列    feature_cols = ['longCount', 'shortCount', 'turnover', 'returns', 'drawdown', 'margin', 'sharpe']    # 提取特征数据，处理缺失值（填充0）    X = df[feature_cols].fillna(0).values    # 改进1：使用RobustScaler标准化（抗异常值，比StandardScaler更适合金融数据）    scaler = RobustScaler()  # 替代StandardScaler，对异常值不敏感    X_scaled = scaler.fit_transform(X)    # 改进2：PCA降维（处理特征冗余，减少噪声）    if use_pca and len(feature_cols) > 2:        # 保留95%的方差，自动确定降维后的维度        pca = PCA(n_components=0.95, random_state=42)        X_processed = pca.fit_transform(X_scaled)        print(f"PCA降维后，特征维度从{len(feature_cols)}变为{X_processed.shape[1]}")    else:        X_processed = X_scaled    # 改进3：多指标确定聚类数（避免聚类数过少）    best_k = determine_clusters_multi_criteria(X_processed, min_clusters=5, max_clusters=50)    print(f"改进后确定的最佳聚类数量：{best_k}")    # 改进4：支持多种聚类算法（KMeans/层次聚类/DBSCAN）    if cluster_algorithm == 'kmeans':        # KMeans：适合球形分布，速度快        cluster_model = KMeans(n_clusters=best_k, random_state=42, n_init='auto')        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'agglomerative':        # 层次聚类：不假设球形分布，更灵活        cluster_model = AgglomerativeClustering(n_clusters=best_k)        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'dbscan':        # DBSCAN：无需指定聚类数，自动识别密度聚类（适合非球形分布）        # eps和min_samples可调整：eps越大，聚类数越少；min_samples越大，聚类数越多        cluster_model = DBSCAN(eps=0.5, min_samples=5)        df['cluster'] = cluster_model.fit_predict(X_processed)        # DBSCAN的-1表示噪声点，单独处理为一个聚类        noise_cluster = df['cluster'].max() + 1        df.loc[df['cluster'] == -1, 'cluster'] = noise_cluster        best_k = len(df['cluster'].unique())        print(f"DBSCAN聚类后实际聚类数量：{best_k}")    # 每个聚类中选择fitness最大的alpha    selected_alphas = []    for cluster in df['cluster'].unique():        cluster_df = df[df['cluster'] == cluster]        # 取fitness最大的行        best_alpha = cluster_df.loc[cluster_df['fitness'].idxmax()]        selected_alphas.append(best_alpha.to_dict())    return selected_alphasif __name__ == '__main__':    # 配置参数：顾问相关日期、分页参数    advisor_date = datetime(2020, 1, 1)  # 成为顾问的日期，用于过滤该日期之后的因子    page_limit = 100  # 每页获取的alpha数量    page_offset = 0   # 分页起始偏移量    target_region = "EUR"  # 目标地区    # 初始化登录会话    session = login()    logging.info("登录成功，开始获取alpha数据")    # 获取alpha的指标数据    alpha_metrics_list = get_history_alpha_ids(        s=session,        region=target_region,        start_date=advisor_date,        limit=page_limit,        offset=page_offset    )    # 校验数据是否有效    if not alpha_metrics_list:        print("程序终止：未获取到有效alpha数据")        exit(1)    # 执行聚类并选择每个类别中fitness最大的alpha    selected_alpha_list = cluster_alphas_improved(        alpha_metrics=alpha_metrics_list,        use_pca=True,        cluster_algorithm='kmeans'    )    # 校验聚类结果    if not selected_alpha_list:        print("程序终止：聚类后未选中任何alpha")        exit(1)    # 计算平均权重并分配分数（总分为100000）    total_selected = len(selected_alpha_list)    per_alpha_weight = 1.0 / total_selected if total_selected > 0 else 0.0    total_allocated_score = 0    # 遍历选中的alpha，输出信息并计算分数    for alpha_info in selected_alpha_list:        alpha_score = int(per_alpha_weight * 100000)        print(            f"Alpha ID：{alpha_info['id']} | "            f"Fitness值：{alpha_info['fitness']} | "            f"所属聚类：{alpha_info['cluster']} | "            f"分配分数：{alpha_score}"        )        # 如需调用接口更新分数，取消以下注释        update_url = f"[链接已屏蔽]        session.patch(update_url, json={"osmosisPoints": alpha_score})        total_allocated_score += alpha_score    # 处理四舍五入导致的分数偏差    score_deviation = 100000 - total_allocated_score    if score_deviation != 0:        print(f"\n因四舍五入产生分数偏差：{score_deviation}分，已将偏差分加到第一个Alpha上")        # 修正第一个Alpha的分数        first_alpha_score = int(per_alpha_weight * 100000) + score_deviation        print(f"第一个Alpha {selected_alpha_list[0]['id']} 的最终分数：{first_alpha_score}")        total_allocated_score = 100000    # 输出最终分配结果    print(f"\n分数分配完成：总分配分数 {total_allocated_score} 分，无分数损耗")
```

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢课代表，准备拿点渗透分了

===================================================================================


---

### 技术对话片段 39 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (JR23144)**:
大家好

年前 kunqi 老师邀请我做个分享，说实话，过年期间走亲访友多喝了几杯，一直没腾出空来。今天终于坐在屏幕前，想着老生常谈的套路大家在论坛也看腻了，那我就分享一点我不一样的“打怪升级”经历和最近的 Alpha 巧思。

按照国际惯例，先上战绩镇楼：


> [!NOTE] [图片 OCR 识别内容]
> BRNR
> Ganius
> Awarded to
> on
> achieving
> EXPERT
> EXPERT Level
> 2025 Quarter 3
> LEVEL
> CERTIFICATE
> Authorized and presented by
> Nitish Maini
> Cnet stratsgy Othcer ot Wcrldcuant
> ESNSESLNWVS CXPERTGENUS EXPERTGENIUS EXPERT GENIUS



> [!NOTE] [图片 OCR 识别内容]
> BRAII
> Ganius
> Awarded to
> onachieving
> GRAND
> GRAND MASTER Level
> MASTER
> 2025 Quarter 4
> LEVEL
> CERTIFICATE
> Nuthorizedand presenteq by
> Nitish Maini
> Cet stratsgy Othcer ot Wcrldouant



> [!NOTE] [图片 OCR 识别内容]
> B人
> Ganius
> Awarded to
> On
> achieving
> GRAND
> GRAND MASTER Level
> MASTER
> 2026 Quarter
> LEVEL
> CERTIFICATE
> Authorizedand presented by
> Nitish Maini
> Cniaf Strategy Otticerot Worldouar


- **段位记录：**  一次Expert 两次定级 Grand Master
- **VF 更新记录：** 4-6月 0.5 ， 7月0.95， 8月0.92， 9月0.99， 10月0.97， 11月 0.85 12月 0.88 ,1月0.98 , 2月0.77
- **阶段性收益：**  在 Expert 阶段拿过 347 刀的季度奖，一次gm季度奖公布下来是8090刀。
- **日收益** ： 高的时候 一天100$,低的时候一天十几刀。
  
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 09/2912025
> Super:
> 55.25
> Regular;
> 5.76
> Total:
> 110.00999999999999
> May
> May
  
> [!NOTE] [图片 OCR 识别内容]
> Ill
> 02/15/2025
> Super:
> 7.27
> Regular:
> 3.80
> Total:
> 11.27

- **时间投入** ：每天投入大概3-4小时。

#### 1. 背景：一个退居18线小城的前大厂程序员

和很多金融、金工科班出身的大佬不同，我以前其实是个在互联网大厂里“拧螺丝”的程序员。后来为了更好的生活节奏，退居到了一个18线小城市。

小城市好是好，但想拿到一线城市的薪资水平并不容易。直到我接触了 WorldQuant BRAIN。它给我提供了一个绝佳的杠杆： **用纯粹的代码和逻辑，去对冲地理位置带来的劣势。**  从写业务代码到写因子，这中间虽然有壁垒，但大厂经历留给我的数据敏感度和抗压能力，是我能一路冲到 GM 的基本盘。

#### 2. 新形势下的心态：接受 VF 的“玄学”，拿稳能拿的钱

在论坛里，大家总喜欢看那些一路高歌猛进的完美剧本。但我今天想分享点真实的痛点。

不知道大家有没有同感： **每次要更新季度奖的时候，那个月的 VF 就不高。**  就像我现在的 0.77，说不心痛是假的。在新规和当下多变的市场形态下，一味地去死磕、焦虑这个波动，其实非常内耗。

我的策略是： **底线思维，稳吃保底。**  既然高 VF 有时候看天吃饭，那就在日常把基础的 Alpha 数量和质量打扎实。不要等到季度末才去突击，而是把力气匀在平时，保证即使在 VF 表现拉胯的月份，依然有 10几刀 这样的保底饭钱收益托底。心态稳了，回测的手才不会抖。

#### 3. 拒绝同质化：分享一个突破瓶颈的 Alpha 巧思

官方老师特意嘱咐我分享一点“不一样”的方法。那我就把我压箱底的一个小技巧拿出来： **特定场景下的冷门算子降维打击。**

大家在写因子或者用 AI 优化时，遇到 Vector（向量）数据，是不是下意识就敲  `vec_sum()`  或者  `vec_avg()` ？不可否认它们很好用，但在寻找极值信号时，它们会让你的 Alpha 变得平庸。

**我的巧思是：**  当你外层使用的是求极小的相关算子（如  `ts_min()` ,  `ts_arg_min()` ,  `group_min()` ）时，内层的向量处理一定要配合使用  **`vec_min()`** ；同理，外层是寻找极大值的逻辑时，内层配合  **`vec_max()`** 。

不要小看这一步替换。在我的单变量回测中，把原本的  `vec_sum()`  换成同向匹配的  `vec_min()` ， **Sharpe 直接从 1.73 跃升到了 1.81，Fitness 突破 1.05** 。这种底层逻辑的纯粹性，往往能帮你避开拥挤的赛道，拿到那些别人忽略的高质量信号。

#### 4. 写在最后

量化这条路，有时候很像我们古代历史里的王朝更迭（对，我平时挺喜欢研究三国，南北朝，唐宋明清历史的哈哈），有盛世也有低谷。重要的不是你一时冲得有多高，而是你能在这个牌桌上坐多久。

祝大家在新的一年里，都能找到属于自己的 Alpha 节奏，咱们一起在马年多赚钱，VF 早日重回巅峰！

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢大佬分享，对于vec操作符的使用，我也挺有体会的。让ai去鉴别哪个字段适合哪个操作符，效果还不错


---

### 技术对话片段 40 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享_38927243023383.md
- **时间**: 3个月前

**提问/主帖背景 (JR23144)**:
大家好

年前 kunqi 老师邀请我做个分享，说实话，过年期间走亲访友多喝了几杯，一直没腾出空来。今天终于坐在屏幕前，想着老生常谈的套路大家在论坛也看腻了，那我就分享一点我不一样的“打怪升级”经历和最近的 Alpha 巧思。

按照国际惯例，先上战绩镇楼：


> [!NOTE] [图片 OCR 识别内容]
> BRNR
> Ganius
> Awarded to
> on
> achieving
> EXPERT
> EXPERT Level
> 2025 Quarter 3
> LEVEL
> CERTIFICATE
> Authorized and presented by
> Nitish Maini
> Cnet stratsgy Othcer ot Wcrldcuant
> ESNSESLNWVS CXPERTGENUS EXPERTGENIUS EXPERT GENIUS



> [!NOTE] [图片 OCR 识别内容]
> BRAII
> Ganius
> Awarded to
> onachieving
> GRAND
> GRAND MASTER Level
> MASTER
> 2025 Quarter 4
> LEVEL
> CERTIFICATE
> Nuthorizedand presenteq by
> Nitish Maini
> Cet stratsgy Othcer ot Wcrldouant



> [!NOTE] [图片 OCR 识别内容]
> B人
> Ganius
> Awarded to
> On
> achieving
> GRAND
> GRAND MASTER Level
> MASTER
> 2026 Quarter
> LEVEL
> CERTIFICATE
> Authorizedand presented by
> Nitish Maini
> Cniaf Strategy Otticerot Worldouar


- **段位记录：**  一次Expert 两次定级 Grand Master
- **VF 更新记录：** 4-6月 0.5 ， 7月0.95， 8月0.92， 9月0.99， 10月0.97， 11月 0.85 12月 0.88 ,1月0.98 , 2月0.77
- **阶段性收益：**  在 Expert 阶段拿过 347 刀的季度奖，一次gm季度奖公布下来是8090刀。
- **日收益** ： 高的时候 一天100$,低的时候一天十几刀。
  
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 09/2912025
> Super:
> 55.25
> Regular;
> 5.76
> Total:
> 110.00999999999999
> May
> May
  
> [!NOTE] [图片 OCR 识别内容]
> Ill
> 02/15/2025
> Super:
> 7.27
> Regular:
> 3.80
> Total:
> 11.27

- **时间投入** ：每天投入大概3-4小时。

#### 1. 背景：一个退居18线小城的前大厂程序员

和很多金融、金工科班出身的大佬不同，我以前其实是个在互联网大厂里“拧螺丝”的程序员。后来为了更好的生活节奏，退居到了一个18线小城市。

小城市好是好，但想拿到一线城市的薪资水平并不容易。直到我接触了 WorldQuant BRAIN。它给我提供了一个绝佳的杠杆： **用纯粹的代码和逻辑，去对冲地理位置带来的劣势。**  从写业务代码到写因子，这中间虽然有壁垒，但大厂经历留给我的数据敏感度和抗压能力，是我能一路冲到 GM 的基本盘。

#### 2. 新形势下的心态：接受 VF 的“玄学”，拿稳能拿的钱

在论坛里，大家总喜欢看那些一路高歌猛进的完美剧本。但我今天想分享点真实的痛点。

不知道大家有没有同感： **每次要更新季度奖的时候，那个月的 VF 就不高。**  就像我现在的 0.77，说不心痛是假的。在新规和当下多变的市场形态下，一味地去死磕、焦虑这个波动，其实非常内耗。

我的策略是： **底线思维，稳吃保底。**  既然高 VF 有时候看天吃饭，那就在日常把基础的 Alpha 数量和质量打扎实。不要等到季度末才去突击，而是把力气匀在平时，保证即使在 VF 表现拉胯的月份，依然有 10几刀 这样的保底饭钱收益托底。心态稳了，回测的手才不会抖。

#### 3. 拒绝同质化：分享一个突破瓶颈的 Alpha 巧思

官方老师特意嘱咐我分享一点“不一样”的方法。那我就把我压箱底的一个小技巧拿出来： **特定场景下的冷门算子降维打击。**

大家在写因子或者用 AI 优化时，遇到 Vector（向量）数据，是不是下意识就敲  `vec_sum()`  或者  `vec_avg()` ？不可否认它们很好用，但在寻找极值信号时，它们会让你的 Alpha 变得平庸。

**我的巧思是：**  当你外层使用的是求极小的相关算子（如  `ts_min()` ,  `ts_arg_min()` ,  `group_min()` ）时，内层的向量处理一定要配合使用  **`vec_min()`** ；同理，外层是寻找极大值的逻辑时，内层配合  **`vec_max()`** 。

不要小看这一步替换。在我的单变量回测中，把原本的  `vec_sum()`  换成同向匹配的  `vec_min()` ， **Sharpe 直接从 1.73 跃升到了 1.81，Fitness 突破 1.05** 。这种底层逻辑的纯粹性，往往能帮你避开拥挤的赛道，拿到那些别人忽略的高质量信号。

#### 4. 写在最后

量化这条路，有时候很像我们古代历史里的王朝更迭（对，我平时挺喜欢研究三国，南北朝，唐宋明清历史的哈哈），有盛世也有低谷。重要的不是你一时冲得有多高，而是你能在这个牌桌上坐多久。

祝大家在新的一年里，都能找到属于自己的 Alpha 节奏，咱们一起在马年多赚钱，VF 早日重回巅峰！

**顾问 YH55729 (Rank 42) 的解答与建议**:
感谢大佬分享，对于vec操作符的使用，我也挺有体会的。让ai去鉴别哪个字段适合哪个操作符，效果还不错


---

### 技术对话片段 41 (原帖: 使用mcp+ai挖掘alpha过程中节约token的小技巧经验分享)
- **原帖链接**: [Commented] 使用mcpai挖掘alpha过程中节约token的小技巧经验分享.md
- **时间**: 4个月前

**提问/主帖背景 (SZ83096)**:
在AI对话/API调用中，Token的消耗由三部分组成，形成一个“上下文窗口”：

**总消耗Token = [输入Token] + [输出Token]**

1. **输入Token** ：
   - 你提交给AI的所有内容： **系统提示词 + 对话历史 + 本次问题/指令** 。
   - 这些都会被模型“阅读”和处理。
2. **输出Token** ：
   - AI根据你的输入 **新生成** 的回复内容。
   - 你要求AI生成的文字越多，输出Token就越多。

输入的token，我观察过AI调用 mcp的过程中，函数返回的内容，有一些是不必要的，比如

get_simulate_result函数，回测完成时，请求后返回给AI 的内容如下：


> [!NOTE] [图片 OCR 识别内容]
> Collapse
> Called MCP tool
> get_simulate_
> result
> "location"
> "https: //api.worldquantbrain. com/simulations / 28U8FggQg5d08 "
> Iwait"
> false
> "location"
> "https : //api.worldquantbrain. com/simulations / 2Y6Y10971
> T57]0"
> Istatus"
> compiul T
> id"
> 2YGYI
> "type"
> IREC
> walpha_id"
> }
> {
> "location"
> 』gbrain. com/simulations / 2JXNOZgr
> r9e
> Istatus"
> "C
> id"
> I2JXNC
> "type"
> IREC
> Ialpha_id"
> }
> {
> "location"
> ugbrain. com/simulations /2iWZEGaul' 思
> Su[cp"
> Istatus"
> "C
> id"
> I2iWZE
> [
> Uny"


可以修改函数返回的内容， 如下图： 这样，AI 获得的输入内容，应该是会减少的，而且，也不会缺少关键信息


> [!NOTE] [图片 OCR 识别内容]
> Called MCP tool
> get_simulate_result
> location"
> "https : //api.worldquantbrain. com/simulations
> /2CFARWTtB4dHI A
> "max_polls"
> 30
> "poll_interval":
> 60
> Iwait"
> true
> "location"
> "https : //api.worldquantbrain. com/simulations /:
> TIgw'
> Istatus"
> completed"
> "children_found"=
> 8
> "children"
> {
> Istatus"
> Compl
> Ialpha_id"
> "omQ!
> }
> {
> Istatus"
> Compl
> Ialpha_id"
> IomQ
> }
> {
> "status"
> compu
> Ialpha_id"
> Om0


get_alpha_details 的返回内容，也可以进行裁剪，比如，只返回下面的内容

```
{  "id": "xxx",  "settings": {    "region": "GLB",    "universe": "MINVOL1M",    "delay": 1,    "decay": 8,    "neutralization": "REVERSION_AND_MOMENTUM",    "truncation": 0.01,    "pasteurization": "ON",    "unitHandling": "VERIFY",    "nanHandling": "ON",    "maxTrade": "ON"  },  "regular": {    "code": "xxx",    "operatorCount": xx  },  "dateCreated": "2026-01-29T04:14:53-05:00",  "classifications": [    {      "id": "DATA_USAGE:SINGLE_DATA_SET",      "name": "Single Data Set Alpha"    }  ],  "is": {    "longCount": 4448,    "shortCount": 4466,    "turnover": 0.0614,    "returns": 0.0474,    "drawdown": 0.0921,    "margin": 0.001543,    "sharpe": 0.97,    "fitness": 0.6,    "glbAmer": {      "sharpe": 0.97    },    "glbApac": {      "sharpe": 0.32    },    "glbEmea": {      "sharpe": 0.52    },    "checks": [      {        "name": "LOW_SHARPE",        "result": "FAIL",        "limit": 1.58,        "value": 0.97      },      {        "name": "LOW_FITNESS",        "result": "FAIL",        "limit": 1,        "value": 0.6      },      {        "name": "LOW_GLB_AMER_SHARPE",        "result": "FAIL",        "limit": 1,        "value": 0.97      },      {        "name": "LOW_GLB_EMEA_SHARPE",        "result": "FAIL",        "limit": 1,        "value": 0.52      },      {        "name": "LOW_GLB_APAC_SHARPE",        "result": "FAIL",        "limit": 1,        "value": 0.32      },      {        "name": "LOW_TURNOVER",        "result": "PASS",        "limit": 0.01,        "value": 0.0614      },      {        "name": "HIGH_TURNOVER",        "result": "PASS",        "limit": 0.7,        "value": 0.0614      },      {        "name": "CONCENTRATED_WEIGHT",        "result": "PASS"      },      {        "name": "LOW_SUB_UNIVERSE_SHARPE",        "result": "PASS",        "limit": 0.34,        "value": 0.98      },      {        "name": "LOW_2Y_SHARPE",        "result": "FAIL",        "value": 1.48,        "limit": 1.58      },      {        "name": "MATCHES_PYRAMID",        "pyramids_name": [          "GLB/D1/OTHER"        ]      }    ]  }}
```

同理，get_operators, get_datasets, get_datafields  这些函数可以优化下输出，只返回你认为需要给AI的内容

我观察过优化输出后，相同的时间内，token消耗的速度确实会慢一些（可能是错觉？）

小伙伴们可以试试，前后对比下token的消耗情况

**顾问 YH55729 (Rank 42) 的解答与建议**:
学到了，感谢分享，最近用打工人做因子，token花的肉疼。

------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 42 (原帖: 使用mcp+ai挖掘alpha过程中节约token的小技巧经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 使用mcpai挖掘alpha过程中节约token的小技巧经验分享_38013569192983.md
- **时间**: 4个月前

**提问/主帖背景 (SZ83096)**:
在AI对话/API调用中，Token的消耗由三部分组成，形成一个“上下文窗口”：

**总消耗Token = [输入Token] + [输出Token]**

1. **输入Token** ：
   - 你提交给AI的所有内容： **系统提示词 + 对话历史 + 本次问题/指令** 。
   - 这些都会被模型“阅读”和处理。
2. **输出Token** ：
   - AI根据你的输入 **新生成** 的回复内容。
   - 你要求AI生成的文字越多，输出Token就越多。

输入的token，我观察过AI调用 mcp的过程中，函数返回的内容，有一些是不必要的，比如

get_simulate_result函数，回测完成时，请求后返回给AI 的内容如下：


> [!NOTE] [图片 OCR 识别内容]
> Collapse
> Called MCP tool
> get_simulate_
> result
> "location"
> "https: //api.worldquantbrain. com/simulations / 28U8FggQg5d08 "
> Iwait"
> false
> "location"
> "https : //api.worldquantbrain. com/simulations / 2Y6Y10971
> T57]0"
> Istatus"
> compiul T
> id"
> 2YGYI
> "type"
> IREC
> walpha_id"
> }
> {
> "location"
> 』gbrain. com/simulations / 2JXNOZgr
> r9e
> Istatus"
> "C
> id"
> I2JXNC
> "type"
> IREC
> Ialpha_id"
> }
> {
> "location"
> ugbrain. com/simulations /2iWZEGaul' 思
> Su[cp"
> Istatus"
> "C
> id"
> I2iWZE
> [
> Uny"


可以修改函数返回的内容， 如下图： 这样，AI 获得的输入内容，应该是会减少的，而且，也不会缺少关键信息


> [!NOTE] [图片 OCR 识别内容]
> Called MCP tool
> get_simulate_result
> location"
> "https : //api.worldquantbrain. com/simulations
> /2CFARWTtB4dHI A
> "max_polls"
> 30
> "poll_interval":
> 60
> Iwait"
> true
> "location"
> "https : //api.worldquantbrain. com/simulations /:
> TIgw'
> Istatus"
> completed"
> "children_found"=
> 8
> "children"
> {
> Istatus"
> Compl
> Ialpha_id"
> "omQ!
> }
> {
> Istatus"
> Compl
> Ialpha_id"
> IomQ
> }
> {
> "status"
> compu
> Ialpha_id"
> Om0


get_alpha_details 的返回内容，也可以进行裁剪，比如，只返回下面的内容

```
{  "id": "xxx",  "settings": {    "region": "GLB",    "universe": "MINVOL1M",    "delay": 1,    "decay": 8,    "neutralization": "REVERSION_AND_MOMENTUM",    "truncation": 0.01,    "pasteurization": "ON",    "unitHandling": "VERIFY",    "nanHandling": "ON",    "maxTrade": "ON"  },  "regular": {    "code": "xxx",    "operatorCount": xx  },  "dateCreated": "2026-01-29T04:14:53-05:00",  "classifications": [    {      "id": "DATA_USAGE:SINGLE_DATA_SET",      "name": "Single Data Set Alpha"    }  ],  "is": {    "longCount": 4448,    "shortCount": 4466,    "turnover": 0.0614,    "returns": 0.0474,    "drawdown": 0.0921,    "margin": 0.001543,    "sharpe": 0.97,    "fitness": 0.6,    "glbAmer": {      "sharpe": 0.97    },    "glbApac": {      "sharpe": 0.32    },    "glbEmea": {      "sharpe": 0.52    },    "checks": [      {        "name": "LOW_SHARPE",        "result": "FAIL",        "limit": 1.58,        "value": 0.97      },      {        "name": "LOW_FITNESS",        "result": "FAIL",        "limit": 1,        "value": 0.6      },      {        "name": "LOW_GLB_AMER_SHARPE",        "result": "FAIL",        "limit": 1,        "value": 0.97      },      {        "name": "LOW_GLB_EMEA_SHARPE",        "result": "FAIL",        "limit": 1,        "value": 0.52      },      {        "name": "LOW_GLB_APAC_SHARPE",        "result": "FAIL",        "limit": 1,        "value": 0.32      },      {        "name": "LOW_TURNOVER",        "result": "PASS",        "limit": 0.01,        "value": 0.0614      },      {        "name": "HIGH_TURNOVER",        "result": "PASS",        "limit": 0.7,        "value": 0.0614      },      {        "name": "CONCENTRATED_WEIGHT",        "result": "PASS"      },      {        "name": "LOW_SUB_UNIVERSE_SHARPE",        "result": "PASS",        "limit": 0.34,        "value": 0.98      },      {        "name": "LOW_2Y_SHARPE",        "result": "FAIL",        "value": 1.48,        "limit": 1.58      },      {        "name": "MATCHES_PYRAMID",        "pyramids_name": [          "GLB/D1/OTHER"        ]      }    ]  }}
```

同理，get_operators, get_datasets, get_datafields  这些函数可以优化下输出，只返回你认为需要给AI的内容

我观察过优化输出后，相同的时间内，token消耗的速度确实会慢一些（可能是错觉？）

小伙伴们可以试试，前后对比下token的消耗情况

**顾问 YH55729 (Rank 42) 的解答与建议**:
学到了，感谢分享，最近用打工人做因子，token花的肉疼。

------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 43 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 关于ts_decay_linear的妙用.md
- **时间**: 4个月前

**提问/主帖背景 (FF56620)**:
之前对于ts_decay_linear的使用，一直停留在降低turnover上，最近的几个alpha，给了我一些不一样的经验


> [!NOTE] [图片 OCR 识别内容]
> 005
> 仳
> HUO A(PIa LO a LISt
> 003
> HUO AIPIa LO a CISt
> 叫
> IS Summary
> Period
> IS
> 05
> IS Summary
> Period
> IS
> 05
> 自
> Single Data Set Alpha
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.00
> 0.00%
> 0.00%
> 0.00%
> 0.00%oo
> 1.96
> 1.86%
> 1.15
> 4.28%
> 2.459
> 46.08%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 0.00
> 0.009
> 0.00
> 0.009
> 0.00%
> 0.00%oo
> 2014
> 2.68
> 2.29%
> 1.78
> 5.509
> 1.15%
> 48
> 2%oo
> 1223
> 6816
> 2015
> 0.00
> 009
> 00
> 00%
> 009
> 0O%oo
> 2015
> 1.61
> 1.749
> 0.91
> 3.989
> 589
> 45.839。
> 1435
> 6937
> 2016
> 0.00
> 0.009
> 00
> 00%
> 009
> 0O%oo
> 2016
> 0.50
> 1.649
> 0.15
> 1.159
> 2.45%
> 14.0596oo
> 1430
> 6651
> 2017
> 0.00
> 00%
> 00
> 00%
> .009
> 00%oo
> 2017
> 99
> 1.729
> 02
> 3.309
> 0.88%
> 38.29%o。
> 1511
> 6884
> 2018
> 0.00
> 0.00%
> 00
> 0.00%
> 00%
> 00%oo
> 2018
> 1.27
> 1.76%
> 0.56
> 2.47%
> 1.839
> 28.06%o。
> 1583
> 7486
> 2019
> 0.00
> 0.009
> 0.00
> 0.00%
> 0.009
> 0.009oo
> 2019
> 0.68
> 1.87%
> 0.21
> 1.239
> 1.61%
> 13.2
> %oo
> 1453
> 6961
> 2020
> 0.00
> 009
> 00
> 00%
> 009
> 0O%oo
> 2020
> 2.87
> 1.9796
> 2.22
> 7.4796
> 1.339
> 75.989o。
> 1518
> 7220
> 2021
> 00
> 00%
> 00
> 00%
> 00%
> 00%oo
> 2021
> 4.02
> .859
> 3.61
> 10.08%
> 1.459
> 108.79%o。
> 1952
> 8677
> 2022
> 0.00
> 0.009
> 00
> 00%
> .009
> 00%oo
> 2022
> 1.60
> 1.849
> 3.90%
> 1.379
> 42.2790。
> 1856
> 8411
> 2023
> 0.00
> 0.00%
> 00
> 00%
> .009
> 00%oo
> 2023
> 2.13
> 1.929
> 1.21
> 4.01 %
> 1.039
> 41.64%o。
> 687
> 7391
> AMER
> Correlation
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.69
> 0.989
> 0.85
> 3.199
> 3.269
> 64.91%o。
> Self Correlation
> Maximum
> Minimum
> Last Run:


我最开始得到的是右边的一个alpha，其表达式结构为

-ts_decay_linear(ts_corr(x, y), 20), 63)，但是可以看到，其turnover很低，也就是“死鱼”，我就想，是不是ts_decay_linear的关系，让他turnover这么低，于是我就把ts_decay_linear去掉，使用-ts_corr(x, y), 20)进行回测， 结果得到左边这样一个结果。

这对我来说是反直觉的，因为我一直理解ts_decay_linear只是一个降低turnover的operator，而这里，却让一个死信号活了过来，经过和AI的探讨，发现，原来我使用的x和y都是低频更新的内容，而对于这样的信号，ts_decay_linear主要起到的作用是，它提升“有效观测密度”，也就是说，在季度周期内，只要有几次ts_corr(x,y,20)有结果，最终就能形成一个连续值，也就是说，ts_decay_linear不只是可降低turnover，还能处理低频数据，让它活过来。

基于这个理论，我又在USA另外一个表达式中得到了类似的结果，表达式结构为：

ts_decay_linear(vec_max(x) - vec_min(x),  20)，左边为不带ts_decay_linear的结果，右边则是使用了ts_decay_linear后的结果

可以猜想，vec_max(x) - vec_min(x)大多数情况下，结构都为0，而通过ts_decay_linear的处理，捕捉到其中的不同值，从而形成一个连续的信号

表现如图：


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> IS Summary
> Period
> IS
> 05
> 1.51
> 8.52%
> 1.02
> 5.670
> 5.399
> 13.31%o。
> 自
> Single Data Set Alpha
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2014
> 0.09
> 9.11%
> 0.01
> 0.27%
> 2.669
> 60%oo
> 1237
> 987
> 0.00
> 0.009
> 0.00%
> 0.00%
> 0.00%oo
> 2015
> 1.34
> 9.069
> 0.72
> 3.58%
> 899
> 7.90%oo
> 1254
> 1007
> 2016
> 2.48
> 8.659
> .85
> 6.949
> 1.749
> 16.06%o。
> 1213
> 961
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2017
> 0.74
> 8.669
> 0.29
> 1.92%
> 1.829
> 4.4290。
> 1187
> 920
> 2014
> 0.00
> 0.00%
> 0.00
> 0.00%
> 00%
> 0O%oo
> 2018
> 68
> 9.569
> .10
> 5.33%
> 2.739
> 11.159oo
> 1218
> 1001
> 2015
> 0.00
> 0.009
> 00
> 00%
> 009
> 009oo
> 2019
> 0.06
> 7.85%
> 0.01
> 0.20%
> 3.41%
> 0.52%。
> 1284
> 1051
> 2016
> 0.00
> 0.0096
> 0.00
> 0.009
> 0.009
> 009oo
> 2020
> 0.66
> 8.289
> 0.33
> 3.12%
> 2.96%
> 7.539600
> 1293
> 1002
> 2017
> 00
> 0.009
> 0.00
> 0.009
> 0.00%
> 0O%oo
> 2021
> 3.24
> 8.21%
> 3.61
> 15.51%
> 909
> 37.799o。
> 1489
> 1249
> 2018
> 0.00
> 0.009
> 00
> 0.009
> .009
> 0.00%oo
> 2022
> 1.85
> 8.129
> .60
> 9.32%
> 4.75%
> 22.96%o。
> 1557
> 1262
> 2019
> 00
> 0.009
> 00
> 00%
> 00%
> 009ooo
> 2023
> 2.58
> 7.739
> 2.44
> 11.189
> 3.329
> 28.939o。
> 1402
> 1011
> 2020
> 0.00
> 0.0096
> 00
> 00%
> 0.009
> 0.0096oo
> 2021
> 00
> 0.009
> 00
> 0.00%
> 0.00%
> 009ooo
> Risk neutralized
> 2022
> 00
> 0.009
> 00
> 0.00%
> 0.009
> 0O%oo
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2023
> 00
> 0.009
> 0.00
> 0.00%
> 00%
> 009ooo
> 0.78
> 8.529
> 0.32
> 2.169
> 8.609
> 5.06%oo
> Investability constrained
> Correlation
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.30
> 5.939
> 0.78
> 4.479
> 6.239
> 15.06%oo
> Self Correlation
> Maximum
> Minimum
> Last Run:


同时，我认为，ts_decay_linear(vec_max(x) - vec_min(x),  d) 会是一个处理vector数据的不错的模板，欢迎大家交流心得

**顾问 YH55729 (Rank 42) 的解答与建议**:
我感觉调turn还是tradewhen最好用，不过比较麻烦，得试不同的开闭条件，也不一定稳健。下回试试ts_decay_linear

===========================================================================


---

### 技术对话片段 44 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 关于ts_decay_linear的妙用_38021301172759.md
- **时间**: 4个月前

**提问/主帖背景 (FF56620)**:
之前对于ts_decay_linear的使用，一直停留在降低turnover上，最近的几个alpha，给了我一些不一样的经验


> [!NOTE] [图片 OCR 识别内容]
> 005
> 仳
> HUO A(PIa LO a LISt
> 003
> HUO AIPIa LO a CISt
> 叫
> IS Summary
> Period
> IS
> 05
> IS Summary
> Period
> IS
> 05
> 自
> Single Data Set Alpha
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.00
> 0.00%
> 0.00%
> 0.00%
> 0.00%oo
> 1.96
> 1.86%
> 1.15
> 4.28%
> 2.459
> 46.08%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 0.00
> 0.009
> 0.00
> 0.009
> 0.00%
> 0.00%oo
> 2014
> 2.68
> 2.29%
> 1.78
> 5.509
> 1.15%
> 48
> 2%oo
> 1223
> 6816
> 2015
> 0.00
> 009
> 00
> 00%
> 009
> 0O%oo
> 2015
> 1.61
> 1.749
> 0.91
> 3.989
> 589
> 45.839。
> 1435
> 6937
> 2016
> 0.00
> 0.009
> 00
> 00%
> 009
> 0O%oo
> 2016
> 0.50
> 1.649
> 0.15
> 1.159
> 2.45%
> 14.0596oo
> 1430
> 6651
> 2017
> 0.00
> 00%
> 00
> 00%
> .009
> 00%oo
> 2017
> 99
> 1.729
> 02
> 3.309
> 0.88%
> 38.29%o。
> 1511
> 6884
> 2018
> 0.00
> 0.00%
> 00
> 0.00%
> 00%
> 00%oo
> 2018
> 1.27
> 1.76%
> 0.56
> 2.47%
> 1.839
> 28.06%o。
> 1583
> 7486
> 2019
> 0.00
> 0.009
> 0.00
> 0.00%
> 0.009
> 0.009oo
> 2019
> 0.68
> 1.87%
> 0.21
> 1.239
> 1.61%
> 13.2
> %oo
> 1453
> 6961
> 2020
> 0.00
> 009
> 00
> 00%
> 009
> 0O%oo
> 2020
> 2.87
> 1.9796
> 2.22
> 7.4796
> 1.339
> 75.989o。
> 1518
> 7220
> 2021
> 00
> 00%
> 00
> 00%
> 00%
> 00%oo
> 2021
> 4.02
> .859
> 3.61
> 10.08%
> 1.459
> 108.79%o。
> 1952
> 8677
> 2022
> 0.00
> 0.009
> 00
> 00%
> .009
> 00%oo
> 2022
> 1.60
> 1.849
> 3.90%
> 1.379
> 42.2790。
> 1856
> 8411
> 2023
> 0.00
> 0.00%
> 00
> 00%
> .009
> 00%oo
> 2023
> 2.13
> 1.929
> 1.21
> 4.01 %
> 1.039
> 41.64%o。
> 687
> 7391
> AMER
> Correlation
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.69
> 0.989
> 0.85
> 3.199
> 3.269
> 64.91%o。
> Self Correlation
> Maximum
> Minimum
> Last Run:


我最开始得到的是右边的一个alpha，其表达式结构为

-ts_decay_linear(ts_corr(x, y), 20), 63)，但是可以看到，其turnover很低，也就是“死鱼”，我就想，是不是ts_decay_linear的关系，让他turnover这么低，于是我就把ts_decay_linear去掉，使用-ts_corr(x, y), 20)进行回测， 结果得到左边这样一个结果。

这对我来说是反直觉的，因为我一直理解ts_decay_linear只是一个降低turnover的operator，而这里，却让一个死信号活了过来，经过和AI的探讨，发现，原来我使用的x和y都是低频更新的内容，而对于这样的信号，ts_decay_linear主要起到的作用是，它提升“有效观测密度”，也就是说，在季度周期内，只要有几次ts_corr(x,y,20)有结果，最终就能形成一个连续值，也就是说，ts_decay_linear不只是可降低turnover，还能处理低频数据，让它活过来。

基于这个理论，我又在USA另外一个表达式中得到了类似的结果，表达式结构为：

ts_decay_linear(vec_max(x) - vec_min(x),  20)，左边为不带ts_decay_linear的结果，右边则是使用了ts_decay_linear后的结果

可以猜想，vec_max(x) - vec_min(x)大多数情况下，结构都为0，而通过ts_decay_linear的处理，捕捉到其中的不同值，从而形成一个连续的信号

表现如图：


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> IS Summary
> Period
> IS
> 05
> 1.51
> 8.52%
> 1.02
> 5.670
> 5.399
> 13.31%o。
> 自
> Single Data Set Alpha
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2014
> 0.09
> 9.11%
> 0.01
> 0.27%
> 2.669
> 60%oo
> 1237
> 987
> 0.00
> 0.009
> 0.00%
> 0.00%
> 0.00%oo
> 2015
> 1.34
> 9.069
> 0.72
> 3.58%
> 899
> 7.90%oo
> 1254
> 1007
> 2016
> 2.48
> 8.659
> .85
> 6.949
> 1.749
> 16.06%o。
> 1213
> 961
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2017
> 0.74
> 8.669
> 0.29
> 1.92%
> 1.829
> 4.4290。
> 1187
> 920
> 2014
> 0.00
> 0.00%
> 0.00
> 0.00%
> 00%
> 0O%oo
> 2018
> 68
> 9.569
> .10
> 5.33%
> 2.739
> 11.159oo
> 1218
> 1001
> 2015
> 0.00
> 0.009
> 00
> 00%
> 009
> 009oo
> 2019
> 0.06
> 7.85%
> 0.01
> 0.20%
> 3.41%
> 0.52%。
> 1284
> 1051
> 2016
> 0.00
> 0.0096
> 0.00
> 0.009
> 0.009
> 009oo
> 2020
> 0.66
> 8.289
> 0.33
> 3.12%
> 2.96%
> 7.539600
> 1293
> 1002
> 2017
> 00
> 0.009
> 0.00
> 0.009
> 0.00%
> 0O%oo
> 2021
> 3.24
> 8.21%
> 3.61
> 15.51%
> 909
> 37.799o。
> 1489
> 1249
> 2018
> 0.00
> 0.009
> 00
> 0.009
> .009
> 0.00%oo
> 2022
> 1.85
> 8.129
> .60
> 9.32%
> 4.75%
> 22.96%o。
> 1557
> 1262
> 2019
> 00
> 0.009
> 00
> 00%
> 00%
> 009ooo
> 2023
> 2.58
> 7.739
> 2.44
> 11.189
> 3.329
> 28.939o。
> 1402
> 1011
> 2020
> 0.00
> 0.0096
> 00
> 00%
> 0.009
> 0.0096oo
> 2021
> 00
> 0.009
> 00
> 0.00%
> 0.00%
> 009ooo
> Risk neutralized
> 2022
> 00
> 0.009
> 00
> 0.00%
> 0.009
> 0O%oo
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2023
> 00
> 0.009
> 0.00
> 0.00%
> 00%
> 009ooo
> 0.78
> 8.529
> 0.32
> 2.169
> 8.609
> 5.06%oo
> Investability constrained
> Correlation
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.30
> 5.939
> 0.78
> 4.479
> 6.239
> 15.06%oo
> Self Correlation
> Maximum
> Minimum
> Last Run:


同时，我认为，ts_decay_linear(vec_max(x) - vec_min(x),  d) 会是一个处理vector数据的不错的模板，欢迎大家交流心得

**顾问 YH55729 (Rank 42) 的解答与建议**:
我感觉调turn还是tradewhen最好用，不过比较麻烦，得试不同的开闭条件，也不一定稳健。下回试试ts_decay_linear

===========================================================================


---

### 技术对话片段 45 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: [Commented] 分享一个自用的AI点塔工作流.md
- **时间**: 3个月前

**提问/主帖背景 (MC42701)**:
用前准备：wqb-MCP + 任何一款AI编辑器 + APP（找灵感）

# AI 点塔工作流：

这部分主要向AI介绍固定的点塔工作流。

1. 确定要点的塔

1. 明确当前工作的股票池：region/delay/universe

2. 选择要点的塔，依据：简单性优先和未点优先

- 简单性：使用`get_datasets` MCP-tool，参数选择alpha数量倒序，通常alpha数量越多，对应dataset越简单。

- 未点：使用`get_pyramid_alphas` MCP-tool，获取当前塔的alpha数量，如果一个塔的alpha数量小于3个，那么这个塔未点。

3. 确定要点的塔：典型的方法是，首先筛选简单的dataset，然后在其中找到未点的塔。

2. 确定回测数据集并搜集该数据集的alpha模板

1. 确定回测数据集：4参数`region/delay/universe/dataset`。注意：最后的dataset用小写字母

2. 获取alpha模板：这步很随意，通常使用`Alpha-Idear` MCP 生成多个alpha模板，或是查找本地模板库，找到数据类型相匹配的模板。

- 使用`alpha_idear` MCP ：输入4参数，等待返回模板

- 查找本地模板：使用能读取Excel文件的工具，本地模板库

3. 依据回测结果筛选有信号的模板

1. 对每一个模板，选择合适的参数，形成一个alpha表达式，使用`create_multi_simulate` MCP-tool 进行回测。注意：每一次`multi-simulate`最多只能回测5个alpha表达式，超过将触发限流

2. 对所有的表达式的回测结果对比分析，优先筛选夏普绝对值大于0.7的模板（如果夏普为负且绝对值大于0.7，说明信号需要反向）

3. 确定所选择的有信号的模板

4. 拓展模板，输出可回测挖掘的模板

1. 回测模板中alpha表达式数量限制：一个模板中所有参数乘积为alpha总数，不得超过6000个。

2. 合理替换模板中的参数：

- 字段参数：如果只用到一个字段，那么该字段可用直接使用对应数据集中的全部同类型字段

- 时间参数：如果使用到`ts_op`，那么其中输入的时间窗口也可替换

- 类别参数：如果使用到`group_op`，那么其中输入的组类别也可替换，这通常替换为`pv1`数据集中的`group`字段。

- 操作符参数：还可以将`vec_avg`替换为`vec_sum`。

3. 生成该模板的表达式，并注明参数

5. 生成Alpha表达式模板

我是把APP里面的“找灵感”功能给扣下来弄成了一个AI可调用的MCP的，然后AI就可以自动去找灵感了，这里要说一个可能的bug：

让AI调用`get_datasets`工具的时候，我一开始是返回：


> [!NOTE] [图片 OCR 识别内容]
> "delay":
> "instrument
> type":  "EQUITY"
> "pegion"
> IUSA"
> Iuniverse"
> "T0P3000"
> 响应
> errop":
> IAn
> unexpected error
> occurred: 400 Client
> Error: Bad
> Request
> for
> Url:
> https: //api
> Worldquantbrain.com /data-sets?
> instrumentTypesEQUITY&regionsUSA&delay=I&universe=TOP3OO
> O8themeALL


然后开始debug，最终发现是url多了个”theme=ALL"，去掉后就正常了：
 
> [!NOTE] [图片 OCR 识别内容]
> wqb-platformlget_datasets
> 'delay":
> "pegion"
> IEUR"
> Iuniverse"
> ITOPCS16OO"
> 响应
> "count"
> 129
> "results":
> "id": "analystlO"
> "name"
> "Performance-Weighted Analyst
> Estimates"
> "description"
> "This dataset
> provides
> smart
> estimates,|"
> Which
> are intelligently weighted averages
> 0f financial
> forecasts
> from institutional
> analysts.
> Individual
> analyst
> forecasts
> are weighted based
> On
> tWO
> key factors:
> the
> analyst's historical
> performance
> SCOTe
> the
> pecency
> 0f
> their
> estimate.
> This approach
> aims
> to
> create
> more
> accurate
> consensUs
> forecast by giving
> greater
> importance to estimates
> from
> historically
> proven
> timely analysts
> Ipatonnnv"
> and
> and
 然后是我让AI跑出来的一个power pool alpha：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> ZOOOK
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Risk Neutralized Pnl
> IS Testing Status
> Period
> 15
> 05
> 6 PASS
> 5WARNING
> 6 PENDING


最后说一下我的感想吧，AI发展的非常迅速，半年前这种活AI还不能胜任，而现在却完全不一样了。工作中一定不能拒绝/抵制AI，而是要正确看待，合理使用！

**顾问 YH55729 (Rank 42) 的解答与建议**:
学习了，看看能不能优化进我的工作流里

==============================================


---

### 技术对话片段 46 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 分享一个自用的AI点塔工作流_38870096703639.md
- **时间**: 3个月前

**提问/主帖背景 (MC42701)**:
用前准备：wqb-MCP + 任何一款AI编辑器 + APP（找灵感）

# AI 点塔工作流：

这部分主要向AI介绍固定的点塔工作流。

1. 确定要点的塔

1. 明确当前工作的股票池：region/delay/universe

2. 选择要点的塔，依据：简单性优先和未点优先

- 简单性：使用`get_datasets` MCP-tool，参数选择alpha数量倒序，通常alpha数量越多，对应dataset越简单。

- 未点：使用`get_pyramid_alphas` MCP-tool，获取当前塔的alpha数量，如果一个塔的alpha数量小于3个，那么这个塔未点。

3. 确定要点的塔：典型的方法是，首先筛选简单的dataset，然后在其中找到未点的塔。

2. 确定回测数据集并搜集该数据集的alpha模板

1. 确定回测数据集：4参数`region/delay/universe/dataset`。注意：最后的dataset用小写字母

2. 获取alpha模板：这步很随意，通常使用`Alpha-Idear` MCP 生成多个alpha模板，或是查找本地模板库，找到数据类型相匹配的模板。

- 使用`alpha_idear` MCP ：输入4参数，等待返回模板

- 查找本地模板：使用能读取Excel文件的工具，本地模板库

3. 依据回测结果筛选有信号的模板

1. 对每一个模板，选择合适的参数，形成一个alpha表达式，使用`create_multi_simulate` MCP-tool 进行回测。注意：每一次`multi-simulate`最多只能回测5个alpha表达式，超过将触发限流

2. 对所有的表达式的回测结果对比分析，优先筛选夏普绝对值大于0.7的模板（如果夏普为负且绝对值大于0.7，说明信号需要反向）

3. 确定所选择的有信号的模板

4. 拓展模板，输出可回测挖掘的模板

1. 回测模板中alpha表达式数量限制：一个模板中所有参数乘积为alpha总数，不得超过6000个。

2. 合理替换模板中的参数：

- 字段参数：如果只用到一个字段，那么该字段可用直接使用对应数据集中的全部同类型字段

- 时间参数：如果使用到`ts_op`，那么其中输入的时间窗口也可替换

- 类别参数：如果使用到`group_op`，那么其中输入的组类别也可替换，这通常替换为`pv1`数据集中的`group`字段。

- 操作符参数：还可以将`vec_avg`替换为`vec_sum`。

3. 生成该模板的表达式，并注明参数

5. 生成Alpha表达式模板

我是把APP里面的“找灵感”功能给扣下来弄成了一个AI可调用的MCP的，然后AI就可以自动去找灵感了，这里要说一个可能的bug：

让AI调用`get_datasets`工具的时候，我一开始是返回：


> [!NOTE] [图片 OCR 识别内容]
> "delay":
> "instrument
> type":  "EQUITY"
> "pegion"
> IUSA"
> Iuniverse"
> "T0P3000"
> 响应
> errop":
> IAn
> unexpected error
> occurred: 400 Client
> Error: Bad
> Request
> for
> Url:
> https: //api
> Worldquantbrain.com /data-sets?
> instrumentTypesEQUITY&regionsUSA&delay=I&universe=TOP3OO
> O8themeALL


然后开始debug，最终发现是url多了个”theme=ALL"，去掉后就正常了：
 
> [!NOTE] [图片 OCR 识别内容]
> wqb-platformlget_datasets
> 'delay":
> "pegion"
> IEUR"
> Iuniverse"
> ITOPCS16OO"
> 响应
> "count"
> 129
> "results":
> "id": "analystlO"
> "name"
> "Performance-Weighted Analyst
> Estimates"
> "description"
> "This dataset
> provides
> smart
> estimates,|"
> Which
> are intelligently weighted averages
> 0f financial
> forecasts
> from institutional
> analysts.
> Individual
> analyst
> forecasts
> are weighted based
> On
> tWO
> key factors:
> the
> analyst's historical
> performance
> SCOTe
> the
> pecency
> 0f
> their
> estimate.
> This approach
> aims
> to
> create
> more
> accurate
> consensUs
> forecast by giving
> greater
> importance to estimates
> from
> historically
> proven
> timely analysts
> Ipatonnnv"
> and
> and
 然后是我让AI跑出来的一个power pool alpha：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> ZOOOK
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Risk Neutralized Pnl
> IS Testing Status
> Period
> 15
> 05
> 6 PASS
> 5WARNING
> 6 PENDING


最后说一下我的感想吧，AI发展的非常迅速，半年前这种活AI还不能胜任，而现在却完全不一样了。工作中一定不能拒绝/抵制AI，而是要正确看待，合理使用！

**顾问 YH55729 (Rank 42) 的解答与建议**:
学习了，看看能不能优化进我的工作流里

==============================================


---

### 技术对话片段 47 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 新人期升段失败 vf05-093的个人小结.md
- **时间**: 4个月前

**提问/主帖背景 (JZ61289)**:
首先，我是11月初成为顾问的，也就是说我大约有50+天时间的新手期，我当时定下的目标是vf0.7，rank来到ex，最终一个超出预期 ，一个未达预期 。也算是中规中矩吧 。

关于vf，主要就是参考论坛之前dalao的分享帖的经验，多交ra和atom，高fit，关注最近两年 的数据，margin>10，因此也可以看到我50+天也就交了120个alpha。平均每天才3个不到。虽然保证了一点质量，但是也为我这赛季没有升段埋下了一点伏笔。


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Factor
> Factor
> 1261289 (Me)
> 0.00
> 0.93



> [!NOTE] [图片 OCR 识别内容]
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> 显示排名列表 
> Genius level: Gold
> Best level: Gold
> Current quarterend: March 31st. 2026
> COUD
> Eligibility Criteria
> 2025-04, October 1st  2025
> December 315t, 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 120
> 100 more to Grandmaster
> 120
> 220
> Pyramids Completed
> 31
> 29 more to Grandmaster
> Combined Alpha Performance
> 1.8
> 0.2 more to Grandmaster
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 1.59


其次是升段，关于升段，六维，3个combine，提交数，点塔数4个都有要求，我个人认为不追求grandmaster的情况下，难度排名是六维>conbine>点塔>提交数，我q4赛季没有升段的主要原因就是没有参透六维，导致六维基本各项排名都很靠后。

主要有3点：

1.过于追求ra，ppa并没有交多少，q4赛季的时候，新人期还是有ppa豁免的，ppa算是新人福利，我却没有把握住，ppa既可以帮我点塔，也可以帮我增加使用的op和filed的数量。

2.过于注重ra质量，而忽略了单个alpha的op和field的使用数量，这也是过拟合的一种表现，可以看到我的平均操作符和平均field都是比较大的，在六维排名中相当靠后。

3.只看论坛，不发帖不评论，导致社区分也不高。


> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st. 2025
> December 31st 2025
> Operators per Alpha
> Operators Used
> Fields per Alpha
> 5.93
> 58
> 1.51
> Fields Used
> Community activity
> Max simulation streak
> 116
> 10.4
> 111


总结：新手期一定要好好利用ppa!

**顾问 YH55729 (Rank 42) 的解答与建议**:
同样是新人，第一次能上0.9真是太厉害了，我才0.88还差一些，学习了。

-----------------------------------------------------------------------------------------------------


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新人期升段失败 vf05-093的个人小结_38121900955415.md
- **时间**: 4个月前

**提问/主帖背景 (JZ61289)**:
首先，我是11月初成为顾问的，也就是说我大约有50+天时间的新手期，我当时定下的目标是vf0.7，rank来到ex，最终一个超出预期 ，一个未达预期 。也算是中规中矩吧 。

关于vf，主要就是参考论坛之前dalao的分享帖的经验，多交ra和atom，高fit，关注最近两年 的数据，margin>10，因此也可以看到我50+天也就交了120个alpha。平均每天才3个不到。虽然保证了一点质量，但是也为我这赛季没有升段埋下了一点伏笔。


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Factor
> Factor
> 1261289 (Me)
> 0.00
> 0.93



> [!NOTE] [图片 OCR 识别内容]
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> 显示排名列表 
> Genius level: Gold
> Best level: Gold
> Current quarterend: March 31st. 2026
> COUD
> Eligibility Criteria
> 2025-04, October 1st  2025
> December 315t, 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 120
> 100 more to Grandmaster
> 120
> 220
> Pyramids Completed
> 31
> 29 more to Grandmaster
> Combined Alpha Performance
> 1.8
> 0.2 more to Grandmaster
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 1.59


其次是升段，关于升段，六维，3个combine，提交数，点塔数4个都有要求，我个人认为不追求grandmaster的情况下，难度排名是六维>conbine>点塔>提交数，我q4赛季没有升段的主要原因就是没有参透六维，导致六维基本各项排名都很靠后。

主要有3点：

1.过于追求ra，ppa并没有交多少，q4赛季的时候，新人期还是有ppa豁免的，ppa算是新人福利，我却没有把握住，ppa既可以帮我点塔，也可以帮我增加使用的op和filed的数量。

2.过于注重ra质量，而忽略了单个alpha的op和field的使用数量，这也是过拟合的一种表现，可以看到我的平均操作符和平均field都是比较大的，在六维排名中相当靠后。

3.只看论坛，不发帖不评论，导致社区分也不高。


> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st. 2025
> December 31st 2025
> Operators per Alpha
> Operators Used
> Fields per Alpha
> 5.93
> 58
> 1.51
> Fields Used
> Community activity
> Max simulation streak
> 116
> 10.4
> 111


总结：新手期一定要好好利用ppa!

**顾问 YH55729 (Rank 42) 的解答与建议**:
同样是新人，第一次能上0.9真是太厉害了，我才0.88还差一些，学习了。

-----------------------------------------------------------------------------------------------------


---
