# EUR TOPCS1600的经验：解决Robust universe Sharpe / Sub-universe Sharpe / Weight concentration 问题经验分享

- **链接**: https://support.worldquantbrain.com[Commented] EUR TOPCS1600的经验解决Robust universe Sharpe  Sub-universe Sharpe  Weight concentration 问题经验分享_38669179039255.md
- **作者**: XW90844
- **发布时间/热度**: 3个月前, 得票: 49

## 帖子正文

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

---

## 讨论与评论 (31)

### 评论 #1 (作者: YZ97204, 时间: 3个月前)

感谢大佬的分享，内容很实用，对我帮助很大

---

### 评论 #2 (作者: WW15616, 时间: 3个月前)

学到了，前两天跑了一堆Robust有问题的，只能切回TOP2500提交。等我试试楼主的方法，感谢。

---

### 评论 #3 (作者: ML63985, 时间: 3个月前)

----------------------------------------------------------------------------------------------------------

感谢分享，原来在整体股票数量覆盖率较低时可以用group_backfill，以前一直只用ts_backfill，不知道group_backfill怎么使用，看完就懂了---------------------------------------------------------------------

---

### 评论 #4 (作者: XL27393, 时间: 3个月前)

感谢楼主分享，提个疑问希望探讨下，使用回填的方式，却增加了操作符数，这对做ppac是不是反而增加了困难

---

### 评论 #5 (作者: JC24357, 时间: 3个月前)

感谢佬的分享啊，做EUR Region的时候确实经常出现alpha表现挺好，但是会出现Robust universe Sharpe/Sub-universe Sharpe/Weight concentration检查不通过的问题，有时候也不忍心直接放弃。

这里佬提供了一个很好的思路，也就是使用backfill_op来解决这个问题。首先需要判断数据是在哪个维度上coverage不足，一般分为两个情况:

1.时间维度，可以在回测界面使用Visualization来查看Coverage Of Universe判断，这种直接使用ts_backfill就好。
2. 股票数量，如果在时间维度上没有明显问题，那就可能是整体股票数量覆盖率较低，这里使用group_backfill就更合适了。

====================== (・∀・(・∀・(・∀・*) 保持进步，保持好奇，坚持探索  ==========================

---

### 评论 #6 (作者: XX88140, 时间: 3个月前)

谢谢分享。之前对于data coverage和股票数量coverage的定义不是很明了，看了这篇文章知道如何解决这些不足的方案了！！

================================

DAY DAY UP

================================

##

---

### 评论 #7 (作者: LG87838, 时间: 3个月前)

感谢分享，group_backfill确实管用，这两天不知道怎么搞到这个运算符的。

早上看到邮件，赶紧来回复一下。

还有很多的运算符没有使用过，继续琢磨。

----------------------------------------------------------------------------------------------------------

慢慢来，相信时间的力量。

----------------------------------------------------------------------------------------------------------

---

### 评论 #8 (作者: JX39934, 时间: 3个月前)

大佬分享的这是干货啊，后面半个月的EUR主题就靠你这帮助了，我要把EUR每一个角落都点亮，猛攻

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 评论 #9 (作者: XW90844, 时间: 3个月前)

感谢大家的评论和点赞。这里只是提供个解决问题的思路，并不是万能钥匙。

group_backfill用于提升基本面类型的coverage比较合适（比如图中所示的子行业毛利率），我也用它解决过imb5、oth395等部分数据集robust universe sharpe/sub-universe sharpe的问题，但其它数据集比如情绪类的字段使用还是要慎重，要考虑回填是否真的有经济学意义。

同理，ts_backfill针对不同数据集，也有不同回填天数、甚至应不应该回填的选择。

回填也确实会增加至少一个操作符数量。

后面再分享解决robust universe sharpe/sub-universe sharpe的其它思路。

---

### 评论 #10 (作者: 顾问 MS51256 (Rank 28), 时间: 3个月前)

感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================

---

### 评论 #11 (作者: YH47265, 时间: 3个月前)

学到了，group-backfill之前确实没怎么用过，原来这么有效。

===================================================================================

---

### 评论 #12 (作者: MP35172, 时间: 3个月前)

感谢大佬的分享，都是些很直接很有用的经验啊

---

### 评论 #13 (作者: 顾问 YH55729 (Rank 42), 时间: 3个月前)

学到了，之前主要使用调trunication的参数调整weight concertration

=============================================================================

---

### 评论 #14 (作者: JL52079, 时间: 3个月前)

大佬的思路很清晰，讲清楚了在什么情况下使用ts_backfill，什么情况下使用group_backfill，进而解决EUR TOPCS1600下Robust universe Sharpe / Sub-universe Sharpe / Weight concentration 的问题，从数据层面解决了覆盖率不足的问题，保障了数据的连续性。为我这种无的放矢的新手顾问提供了很好的思路。再次感谢大佬的付出，祝评论区所有顾问同僚直通GM，常驻top1！

---

### 评论 #15 (作者: XY20037, 时间: 3个月前)

非常感谢大佬这么细致实用的经验分享！最近做 EUR TOPCS1600 时，我也频繁遇到 Robust universe Sharpe 不达标、Sub‑universe Sharpe 偏低、Weight concentration 超限这些问题，一直没找到系统的解决办法。看完才明白原来是数据覆盖率的问题，还分清了日期覆盖率用 ts_backfill、股票数量覆盖率用 group_backfill，尤其是按 country、subindustry 甚至笛卡尔积分组回填的思路，对我启发特别大。以后做 EUR 因子终于有清晰的排查方向了，期待大佬后续更多干货！

---

### 评论 #16 (作者: BW14163, 时间: 3个月前)

感谢分享，Date Coverage不足：用ts_backfill解决。股票数量Coverage不足：用group_backfill解决。实证好用，还得多读论坛，自己看半天，还是一知半解的不知大怎么用。通过看帖子，然后拿去回测实验，印象立马就加深了。

**********************************
紧跟大佬的脚步，每天坚持至少学一个知识点，尽量不混信号，不过拟合。
Prioritize diversity, strong margin, low correlation, stable diversification; strictly control costs and overfitting.
**********************************

---

### 评论 #17 (作者: ML38868, 时间: 3个月前)

感谢分享，确实遇到很多这个问题，对我这个新手来说帮大忙了

---

### 评论 #18 (作者: 顾问 MZ45384 (Rank 51), 时间: 3个月前)

虽然早就在用group_backfill了，但发现还是大佬经验丰厚，总结地周到：

Date Coverage不足：用ts_backfill解决。股票数量Coverage不足：用group_backfill解决。

感谢大佬！祝大佬VF1.

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

### 评论 #19 (作者: YQ84572, 时间: 3个月前)

很好的经验分享，和在ind区域的时候遇到的情况大差不差，eur区域虽然好一点，但是也可以处理被忽略的alpha来优化达到提交标准

===================================================================================

评论区

===================================================================================

---

### 评论 #20 (作者: XW23690, 时间: 3个月前)

感谢分享。我还发现不管是EUR还是IND，很多时候出现robust是因为pnl线和Investability constrained的线偏离，所以可以选择直接max trade = on

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #21 (作者: XW90844, 时间: 3个月前)

> [XX27743](/hc/en-us/profiles/36005730110615-XX27743)
> - 3个月前
> 感谢大佬的分享，很有收获。但我的chart表只能查看pnl、sharpe和turnover，难道是权限不足？

哈哈，兄弟来自火星？回测时要把visualization设为true

---

### 评论 #22 (作者: XX27743, 时间: 3个月前)

@ [XW90844](/hc/en-us/profiles/33554916160919-XW90844)  感谢，已经弄懂了哈哈

---

### 评论 #23 (作者: ST61360, 时间: 3个月前)

这文章写的太好，非常实用，让我真正搞懂了两个覆盖率问题。实际alpha开发中很有用。

---

### 评论 #24 (作者: ZY95930, 时间: 3个月前)

非常有用的经验分享，彻底搞清楚了数据覆盖率问题。对alpha开发有很大帮助。谢谢经验分享。

---

### 评论 #25 (作者: CZ39633, 时间: 3个月前)

====================================================================================                        感谢大佬的经验分享，这个对解决数据覆盖率的问题有很大用                                                          ================================自信人生两百年，会当水击三千里==========================

---

### 评论 #26 (作者: 顾问 FZ60707 (Rank 78), 时间: 2个月前)

感谢大佬的经验分享，提供了两种backfill的思路，来解决EUR可能出现的robust报错问题。

===================================================================================

我是评论区

===================================================================================

---

### 评论 #27 (作者: JC31003, 时间: 2个月前)

今天就卡在这个问题了，看到这篇文章真是及时雨啊，感谢作者的分享

---

### 评论 #28 (作者: XW25488, 时间: 2个月前)

非常感谢老师的分享，之前测试从没有出现过robust，现在发现还是一些策略上的字符运算还是没有配合到位。

突然发现在评论的另一位老师 [XW23690](/hc/zh-cn/profiles/32613849420311-XW23690) 说的方法也能实践：

> 感谢分享。我还发现不管是EUR还是IND，很多时候出现robust是因为pnl线和Investability constrained的线偏离，所以可以选择直接max trade = on

---

### 评论 #29 (作者: YD47986, 时间: 2个月前)

感谢大佬的解惑 确实最近全是这类问题

---

### 评论 #30 (作者: HL84989, 时间: 1个月前)

感谢大佬分享，每天学习一点点，真好

============================================================================================================================================================================================================================================================

---

### 评论 #31 (作者: 顾问 AJ39409 (Rank 41), 时间: 1个月前)

这类IS状态检测不止在EUR TOPCS1600里有，ASI地区也经常有，尤其是最近上的新universe。除了数据覆盖不足，还有一些是因为股票权重分布不均匀导致，可以用楼主的方法以外，再额外加一些if_else过滤，把一些权重低的股票排除掉即可。

signal = {s};

liq_filter = rank(ts_mean(volume, 20)) >= 0.20;

if_else(liq_filter, signal, nan)

=============================================================================

“Markets are very efficient at transferring wealth from the impatient to the patient.”
市场非常擅长把财富从没有耐心的人手里转移到有耐心的人手里。—— Warren Buffett

=============================================================================

---

