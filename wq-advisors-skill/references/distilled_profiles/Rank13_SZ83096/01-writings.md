# 顾问 SZ83096 (Rank 13) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 SZ83096 (Rank 13) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: ACE 的ＳＡ天天交
- **主帖链接**: ACE 的ＳＡ天天交.md
- **讨论数**: 0

==================================================================

每天的SA都在提交，挑尽量好的交，你們呢？

G2组这周是ACE主题，做起来感觉也还行吧，和SIMPLE差不多

=========================================================

---

### 帖子 #2: ACE 的ＳＡ天天交
- **主帖链接**: https://support.worldquantbrain.comACE 的ＳＡ天天交_33263093280919.md
- **讨论数**: 0

==================================================================

每天的SA都在提交，挑尽量好的交，你們呢？

G2组这周是ACE主题，做起来感觉也还行吧，和SIMPLE差不多

=========================================================

---

### 帖子 #3: ASI robust FAIL优化小技巧
- **主帖链接**: ASI robust FAIL优化小技巧.md
- **讨论数**: 6

robust 测试是什么：（结合AI和官方文档的理解）

**稳健宇宙测试** 是一种严格健壮性评估方法，旨在确保Alpha因子在不同市场范围
和规模条件下都能保持稳定优异的表现。

brain 平台要求robust 合格的条件是：

```
收益保持率 ≥ 90% : 在调整后的可扩展的universe上的收益至少达到原始提交版本的90%sharpe >=90: 在调整后的可扩展的universe上的sharpe至少达到原始提交版本
```

理解了robust 的概念后，开始尝试优化alpha的robust 过提交标准：

如图： 这是优化前的初始alpha，is指标都不错，但是robust Sharpe和robust returns都差一些，没法提交。


> [!NOTE] [图片 OCR 识别内容]
> #second_order
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.79
> 4.869
> 1.01
> 3.999
> 2.839
> 16.399o。
> imulal [
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Instrur
> 鼍
> 3u
> 0ou
> 禺
> 03m
> Jasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2013
> 0.55
> 5.96%6
> 0.18
> 1.309
> 2.3990
> 4.37260。
> 1432
> 1294
> Equity
> u 』
> 罾0鼍罾
> Jn
> On
> Verify
> On
> 2014
> 1.81
> 4.4796
> .01
> 3.92%
> 1.37%6
> 17.56960
> 1673
> 1473
> 2015
> 1.04
> 4.87%
> 0.45
> 2.34%
> 1.48%
> 9.62900
> 1758
> 1538
> 2016
> 47
> 4.48%
> 0.74
> 3.159
> 1.2090
> 14.069oo
> 690
> 1477
> Clone Alpha 
> 2017
> 2.78
> 4.92%
> 87
> 5.68%
> 1.03%
> 23.07960
> 1723
> 1520
> 2018
> 3.09
> 4.74%
> 2.32
> 7.02%
> 1.01%
> 29.63%600
> 1984
> 1762
> 2019
> 1.14
> 4.71%
> 0.50
> 2.4596
> 1.759
> 10.419oo
> 1758
> 1610
> Chart
> Pnl
> 2020
> 46
> 5.08%
> 0.76
> 3.41%
> 2.83%
> 13.4290
> 1910
> 639
> 2021
> 2.66
> 5.12%
> 1.75
> 5.42%
> 1.14%
> 21.16%0。
> 2400
> 2091
> 2022
> 2.17
> 4.36%
> 44
> 5.49%
> 1.56%
> 25.18%o0
> 2232
> 1945
> 2023
> 1.94
> 4.97%
> -1.18
> -4.63%
> 0.99%
> -18.61%00
> 1964
> 1668
> 300OK
> 2,00OK
> Correlation
> OOOK
> Self Correlation
> Naximum
> Minimum
> Last Run:
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
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 1
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8
> PASS
> 2 FAIL
> Robust universe Sharpe of 1.45 is below cutoff of 1.61 (90% of Alpha):
> Robust universe returns of 3.51% is below cutoff of 3.599 (909 of Alpha):
> Properties
> Last saved Mon; 11/17/2025,7.15 PM
> 2MNARNING


优化1: 尝试了用power ，参数设置3 （参考论坛优化robust 的），没有明显改善


> [!NOTE] [图片 OCR 识别内容]
> #Second
> 0rder
> 眼 Single Data Set Alpha
> 3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.09
> 5.339
> 1.37
> 5.389
> 3.649
> 20.199oo
> power(b,3)
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> mulation
> Settings
> 2013
> 0.52
> 6.55%
> 0.18
> 1.47%
> 3.64%
> 4.48900
> 1458
> 1267
> Instrument Type
> Region
> IInivorse
> aqwane
> Dpraw
> Dolaw
> Triratinn
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 2.13
> 95%
> 1.40
> 5.43%
> 1.75%
> 21.93900
> 1763
> 1383
> Equity
> ASI
> On
> On
> Verify
> On
> 2015
> 28
> 5.26%
> 0.66
> 3.33%
> 80%
> 12.679600
> 1868
> 1428
> 2016
> 28
> 6996
> 0.63
> 3.01%
> 48%
> 12.829600
> 1789
> 1379
> 2017
> 3.08
> 5.28%
> 2.39
> 7.53%
> 66%
> 28.5490
> 1805
> 1438
>  Clone Alpha
> 2018
> 3.23
> 5.11%
> 2.59
> 8.06%
> 1.1796
> 31.5190o
> 2078
> 668
> 2019
> 2.43
> 5.22%
> 1.73
> 34%
> 29%
> 24.319600
> 1858
> 1510
> 2020
> 2.54
> 5.80%
> 87
> 80%
> 2.81%
> 23.45900
> 2028
> 1521
> Chart
> Pnl
> 2021
> 3.44
> 5.6996
> 2.72
> 84%
> 1.319
> 27.5790
> 2567
> 1924
> 2022
> 60
> 4.82%6
> 0.96
> 4.50%
> 2.34%
> 18.64900
> 2404
> 1773
> 2023
> 1.73
> 5.4496
> -1.13
> 38%
> 1.069
> -19.78900
> 2116
> 1516
> Correlation
> Z,OOOK
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
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
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8 PASS
> 2 FAIL
> Robust universe Sharpe Of 1.63 is below cutoff of 1.88 (90% of Alpha).
> Properties
> Last Saved Mon; 11/17/2025,7:15 PM
> Robust universe returns of 4.40% is below cutoff of 4.849 (90% of Alpha).
> 2WARNING
> Name
> Category
> 5 PENDING
> Currently 'anonymous'
> None


原alpha最后一步是neut 操作，想了下，更换下power和 group_op的处理顺序后，结果如下，robust returns 过了，但是robust sharpe 还是没改善


> [!NOTE] [图片 OCR 识别内容]
> 卧
> Single Data Set Alpha
> d=power(a,3) ;
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> bgroup_mean
> d,1,industry )-d;b
> 2.19
> 4.91%
> 1.41
> 5.189
> 3.089
> 21.129o。
> Sharpe
> Turnover
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.25
> 5.949
> 0.06
> 0.64%
> 2.96%
> 2.17900
> 1504
> 1222
> Instrument Type
> Region
> Universe
> Language
> hSr
> Q圜g
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 89
> 4.5596
> 1.11
> 4.35%
> 1.169
> 19.139600
> 1764
> 1382
> Equity
> ASI
> MINVOLIM
> Fast Expression
> On
> On
> Verify
> On
> 2015
> 1.57
> 4.819
> 0.86
> 3.72%
> 29%6
> 15.49900
> 1845
> 1451
> 2016
> 54
> 4.37%
> 0.81
> 3.44%
> 1.12%
> 15.76900
> 1765
> 1402
> 2017
> 3.72
> 99%
> 2.97
> 7.97%
> 02%
> 31.92900
> 1787
> 1456
> Clone Alpha 
> 2018
> 3.84
> 4.78%
> 3.27
> 9.05%
> 0.99%6
> 37.88900
> 2068
> 1678
> 2019
> 60
> 4.79%
> 0.89
> 3.84%
> 1.16%
> 16.05900
> 1856
> 1512
> 2020
> 2.24
> 5.32%
> 51
> 5.67%
> 3.08%
> 21.30900
> 2016
> 1533
> N Chart
> Pnl
> 2021
> 3.18
> 5.15%
> 2.34
> 6.79%
> 1.12%
> 26.35900
> 2541
> 1949
> 2022
> 2.67
> 4.44%
> 96
> 77%
> 80%
> 30.549600
> 2374
> 1803
> 2023
> 2.04
> 5.139
> -1.36
> -5.52%
> 1.049
> -21.5190o
> 2064
> 1568
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
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
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0s
> Performance Comparison
> Last Run:
> 9 PASS
> 1 FAIL
> Robust universe Sharpe of 1.83 is below cutoff of 1.97 (90% of Alpha)。
> Properties
> Last saved Mon 11/17/2025,7.15 PM
> 2 WARNING
> Name
> Category
> 5 PENDING
> Year
> Fitness


根据字段的定义和labs中查看了字段的分布，值范围，了解到 字段的值范围在0-10；

想了下，是否可以过滤掉一些影响robust sharpe信号的数据（可能过拟合？）

尝试了用tail处理，robust sharpe有比较明显的改善，如图：


> [!NOTE] [图片 OCR 识别内容]
> #SeCond
> Order
> A Single Data Set Alpha
> d-power(tail(a, lower
> 0,
> Upper
> 9, newval
> 01,31;
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Roturns
> Drawdown
> Margin
> bgroup_mean(d,
> industry )-d;b
> 2.31
> 5.049
> 1.56
> 5.71%
> 3.1296
> 22.649o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Cour
> 2013
> 0.55
> 6,25%
> 0.20
> 59%
> 3.12%
> 5.119oo
> 1553
> 117
> Uzation
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 1.91
> 4.799
> 1.15
> 4.5790
> 0.939
> 19.089o
> 1862
> 128
> On
> On
> VeriTy
> On
> 2015
> 4,77%
> 1.17
> 65%
> +40%
> 19.489oo
> 1899
> 139
> 2016
> 0.92
> 4.269
> 0.38
> 089
> 2.119
> 9.7793
> 1810
> 135
> 2017
> 08
> 99%
> 3.46
> 8.98%
> 0.91%
> 36.049oo
> 1831
> 141
> Clone Alpha
> 2018
> 3.92
> 4.78%
> 3.39
> 9.349
> 1.219
> 39.053o
> 2152
> 159
> 2019
> 2.19
> 4,88%
> 1.48
> 5.70%
> 1.,019
> 23.39o
> 1921
> 144
> 2020
> 2.97
> 5.68%
> 2.36
> 7.909
> 2.270
> 27.829o
> 2104
> 144
> Chart
> Pnl
> 2021
> 2.93
> 5,36%
> 2.11
> 6.479
> 1.13%
> 24.17966
> 2782
> 170
> 2022
> 2.44
> 4.809
> 1.74
> 6.359
> 2.009
> 26.479o
> 2540
> 163
> 2023
> 5,279
> ~0.81
> 299
> 1.199
> 16.29%e。
> 2152
> 148
> 40OOK
> Correlation
> ZOOOK
> Self Correlation
> Matmum
> Minimum
> Last Run;
> Power Pool Correlation
> MaMmUm
> MnImUm
> Last Run;
> Jan '14
> Jan '15
> Jan '16
> jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Malmum
> MinImUT
> Last Run:
> IS Testing Status
> Period
> I5
> 0S
> Performance Comparison
> Last Run;
> 9PASS
> Sharpe of 2.31is above cutoff ot
> .58。
> Fitness of 1.56 is above cUtoff ot 1
> Turnover ol
> 04%
> above Cutoff Of 1%。
> Properties
> Last saved Mon 11/17/2025,7.15P1
> Turnoverof
> 049
> below
> Of 709
> Weightis well distributed over instruments.
> Name
> Category
> Sub universe Sharpe of 0.98 is above cutoff of 0.68。
> Robust universe returns of 5.44% Is above cutoff of
> 14% (90% ofAlpha)。
> Currently anonymous'
> None
> Sharpe of 2.41is above cutoff of
> 58
> Pyramid theme ASIIDIISHORTINTEREST matches with multiplier of 1.3. Effective pyramid count for Genius is
> Tags
> Color
> FAIL
> Selectladd tags
> None
> Robust universe Sharpe of 2.05 is below cutoff of 2.08 (909 of Alpha)
> Long
> CUtoff
> year


最后，凭直觉用quantile 变换下分布，robust pass


> [!NOTE] [图片 OCR 识别内容]
> power(tail
> a, lOwer
> Upper
> 9,
> newval
> 01,3);
> ] Single Data Set Alpha
> bgroup
> mean (d,1
> industry)-d;
> ts_mean (X,60)
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> quantile (b,
> driver
> gaussian,
> Sigma
> 1.0 )
> 2.38
> 4.579
> 1.50
> 4.959
> 2.739
> 21.69%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> imulation Settings
> 2013
> 0.05
> 5.72%
> 0.00
> 0.11%
> 2.73%
> 0.38900
> 1385
> 1341
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
> 2.39
> 4.30%
> 1.51
> 4.98%
> 0.829
> 23.20900
> 1598
> 1548
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.66
> 4.4796
> .81
> 5.78%
> 0.929
> 25.889600
> 1648
> 1648
> 2016
> .20
> 4.01%
> 0.53
> 2.44%
> 8496
> 12.14%00
> 1602
> 1565
> 2017
> 4.39
> 4.63%
> 3.61
> 8.47%
> 0.91%
> 36.57900
> 1642
> 1601
> Clone Alpha 
> 2018
> 3.24
> 4.36%
> 2.38
> 6.73%
> 099
> 30.87900
> 869
> 1877
> 2019
> 2.57
> 4.28%
> 1.71
> 5.51%
> 0.879
> 25.73900
> 1683
> 1684
> 2020
> 3.21
> 4.899
> 2.37
> 6.84%
> 79%
> 27.96900
> 853
> 1696
> N
> Chart
> Pnl
> 2021
> 2.85
> 88%
> 89
> 5.51%
> 00%6
> 22.59900
> 2314
> 2177
> 2022
> 86
> 4.24%
> 02
> 3.79%
> 66%
> 17.88900
> 2127
> 2051
> 2023
> 2.89
> 4.419
> 2.24
> -7.48%
> .16%
> -33.90900
> 1883
> 1748
> Correlation
> Z,OOOK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
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
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 10 PASS
> 2WARNING
> Competition Al Alphas Competition 2025 does not match.
> Properties
> Last saved Mon, 11/17/2025,12:59 PM
> Theme IND Region Theme does not match with multiplier of 2。
> 5 PENDING
> Name
> Cateeorv


这个alpha op数6个，有亿点点多，尝试去掉power  ，robust也是能过的，优化完成✅


> [!NOTE] [图片 OCR 识别内容]
> d=(tail(a
> LOWer
> Upper
> newval
> 01 )
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> b=group_mean
> d,1, industry )-d;
> 2.37
> 4.569
> 1.48
> 4.909
> 2.819
> 21.47900
> quantile(b,
> driver
> gaussian,
> Sigma
> 1.01
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Urawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.11
> 5.72%
> 0.02
> 0.25%
> 2.81%
> 0.89900
> 1385
> 1341
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
> 2.41
> 4.29%
> 52
> 4.98%
> 0.80%
> 23.20900
> 1606
> 1540
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 63
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.79
> 4.46%
> 94
> 6.04%
> 0.92%
> 27.07900
> 1656
> 1640
> 2016
> 1.19
> 4.029
> 0.52
> 2.39%
> 909
> 11.9090o
> 1611
> 1556
> 2017
> 4.29
> 4.62%
> 3.47
> 8.20%
> 0.96%
> 35.52900
> 651
> 1591
> Clone Alpha 
> 2018
> 3.20
> 4.36%
> 33
> 6.61%
> 03%
> 30.33900
> 867
> 1879
> 2019
> 2.52
> 4.28%
> 65
> 5.39%6
> 0.88%
> 25.21900
> 686
> 682
> 2020
> 3.16
> 87%6
> 2.31
> 69%
> 7996
> 27.509oo
> 853
> 696
> Chart
> Pnl
> 2021
> 2.70
> 4.88%
> 1.75
> 5.24%6
> 9996
> 21.46900
> 2319
> 2172
> 2022
> 89
> 4.2596
> 05
> 3.84%
> 709
> 18.08300
> 2139
> 2039
> 2023
> 3.03
> 4.43%
> 2.39
> 7.78%
> 1.15%
> 35.07900
> 1887
> 1745
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
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
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Performance Comparison
> Last Run:
> 10 PASS
> 2 WARNING
> 5 PENDING
> Properties
> Last saved Mon; 11/17/2025,8:17 PM
> Name
> Category
> Currently 'anonymous'
> NOne


结束语：

```
这个alpha，是需要反转的，考虑到我group_mean op这个季度还没用到，所以，我把 -group_neutralize 换成了group_mean(d,1,group)-d (来着研究小组同学的讨论分享，感谢) 
```

---

### 帖子 #4: ASI robust FAIL优化小技巧
- **主帖链接**: https://support.worldquantbrain.comASI robust FAIL优化小技巧_36383377642391.md
- **讨论数**: 6

robust 测试是什么：（结合AI和官方文档的理解）

**稳健宇宙测试** 是一种严格健壮性评估方法，旨在确保Alpha因子在不同市场范围
和规模条件下都能保持稳定优异的表现。

brain 平台要求robust 合格的条件是：

```
收益保持率 ≥ 90% : 在调整后的可扩展的universe上的收益至少达到原始提交版本的90%sharpe >=90: 在调整后的可扩展的universe上的sharpe至少达到原始提交版本
```

理解了robust 的概念后，开始尝试优化alpha的robust 过提交标准：

如图： 这是优化前的初始alpha，is指标都不错，但是robust Sharpe和robust returns都差一些，没法提交。


> [!NOTE] [图片 OCR 识别内容]
> #second_order
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.79
> 4.869
> 1.01
> 3.999
> 2.839
> 16.399o。
> imulal [
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Instrur
> 鼍
> 3u
> 0ou
> 禺
> 03m
> Jasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2013
> 0.55
> 5.96%6
> 0.18
> 1.309
> 2.3990
> 4.37260。
> 1432
> 1294
> Equity
> u 』
> 罾0鼍罾
> Jn
> On
> Verify
> On
> 2014
> 1.81
> 4.4796
> .01
> 3.92%
> 1.37%6
> 17.56960
> 1673
> 1473
> 2015
> 1.04
> 4.87%
> 0.45
> 2.34%
> 1.48%
> 9.62900
> 1758
> 1538
> 2016
> 47
> 4.48%
> 0.74
> 3.159
> 1.2090
> 14.069oo
> 690
> 1477
> Clone Alpha 
> 2017
> 2.78
> 4.92%
> 87
> 5.68%
> 1.03%
> 23.07960
> 1723
> 1520
> 2018
> 3.09
> 4.74%
> 2.32
> 7.02%
> 1.01%
> 29.63%600
> 1984
> 1762
> 2019
> 1.14
> 4.71%
> 0.50
> 2.4596
> 1.759
> 10.419oo
> 1758
> 1610
> Chart
> Pnl
> 2020
> 46
> 5.08%
> 0.76
> 3.41%
> 2.83%
> 13.4290
> 1910
> 639
> 2021
> 2.66
> 5.12%
> 1.75
> 5.42%
> 1.14%
> 21.16%0。
> 2400
> 2091
> 2022
> 2.17
> 4.36%
> 44
> 5.49%
> 1.56%
> 25.18%o0
> 2232
> 1945
> 2023
> 1.94
> 4.97%
> -1.18
> -4.63%
> 0.99%
> -18.61%00
> 1964
> 1668
> 300OK
> 2,00OK
> Correlation
> OOOK
> Self Correlation
> Naximum
> Minimum
> Last Run:
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
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 1
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8
> PASS
> 2 FAIL
> Robust universe Sharpe of 1.45 is below cutoff of 1.61 (90% of Alpha):
> Robust universe returns of 3.51% is below cutoff of 3.599 (909 of Alpha):
> Properties
> Last saved Mon; 11/17/2025,7.15 PM
> 2MNARNING


优化1: 尝试了用power ，参数设置3 （参考论坛优化robust 的），没有明显改善


> [!NOTE] [图片 OCR 识别内容]
> #Second
> 0rder
> 眼 Single Data Set Alpha
> 3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.09
> 5.339
> 1.37
> 5.389
> 3.649
> 20.199oo
> power(b,3)
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> mulation
> Settings
> 2013
> 0.52
> 6.55%
> 0.18
> 1.47%
> 3.64%
> 4.48900
> 1458
> 1267
> Instrument Type
> Region
> IInivorse
> aqwane
> Dpraw
> Dolaw
> Triratinn
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 2.13
> 95%
> 1.40
> 5.43%
> 1.75%
> 21.93900
> 1763
> 1383
> Equity
> ASI
> On
> On
> Verify
> On
> 2015
> 28
> 5.26%
> 0.66
> 3.33%
> 80%
> 12.679600
> 1868
> 1428
> 2016
> 28
> 6996
> 0.63
> 3.01%
> 48%
> 12.829600
> 1789
> 1379
> 2017
> 3.08
> 5.28%
> 2.39
> 7.53%
> 66%
> 28.5490
> 1805
> 1438
>  Clone Alpha
> 2018
> 3.23
> 5.11%
> 2.59
> 8.06%
> 1.1796
> 31.5190o
> 2078
> 668
> 2019
> 2.43
> 5.22%
> 1.73
> 34%
> 29%
> 24.319600
> 1858
> 1510
> 2020
> 2.54
> 5.80%
> 87
> 80%
> 2.81%
> 23.45900
> 2028
> 1521
> Chart
> Pnl
> 2021
> 3.44
> 5.6996
> 2.72
> 84%
> 1.319
> 27.5790
> 2567
> 1924
> 2022
> 60
> 4.82%6
> 0.96
> 4.50%
> 2.34%
> 18.64900
> 2404
> 1773
> 2023
> 1.73
> 5.4496
> -1.13
> 38%
> 1.069
> -19.78900
> 2116
> 1516
> Correlation
> Z,OOOK
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
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
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8 PASS
> 2 FAIL
> Robust universe Sharpe Of 1.63 is below cutoff of 1.88 (90% of Alpha).
> Properties
> Last Saved Mon; 11/17/2025,7:15 PM
> Robust universe returns of 4.40% is below cutoff of 4.849 (90% of Alpha).
> 2WARNING
> Name
> Category
> 5 PENDING
> Currently 'anonymous'
> None


原alpha最后一步是neut 操作，想了下，更换下power和 group_op的处理顺序后，结果如下，robust returns 过了，但是robust sharpe 还是没改善


> [!NOTE] [图片 OCR 识别内容]
> 卧
> Single Data Set Alpha
> d=power(a,3) ;
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> bgroup_mean
> d,1,industry )-d;b
> 2.19
> 4.91%
> 1.41
> 5.189
> 3.089
> 21.129o。
> Sharpe
> Turnover
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.25
> 5.949
> 0.06
> 0.64%
> 2.96%
> 2.17900
> 1504
> 1222
> Instrument Type
> Region
> Universe
> Language
> hSr
> Q圜g
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 89
> 4.5596
> 1.11
> 4.35%
> 1.169
> 19.139600
> 1764
> 1382
> Equity
> ASI
> MINVOLIM
> Fast Expression
> On
> On
> Verify
> On
> 2015
> 1.57
> 4.819
> 0.86
> 3.72%
> 29%6
> 15.49900
> 1845
> 1451
> 2016
> 54
> 4.37%
> 0.81
> 3.44%
> 1.12%
> 15.76900
> 1765
> 1402
> 2017
> 3.72
> 99%
> 2.97
> 7.97%
> 02%
> 31.92900
> 1787
> 1456
> Clone Alpha 
> 2018
> 3.84
> 4.78%
> 3.27
> 9.05%
> 0.99%6
> 37.88900
> 2068
> 1678
> 2019
> 60
> 4.79%
> 0.89
> 3.84%
> 1.16%
> 16.05900
> 1856
> 1512
> 2020
> 2.24
> 5.32%
> 51
> 5.67%
> 3.08%
> 21.30900
> 2016
> 1533
> N Chart
> Pnl
> 2021
> 3.18
> 5.15%
> 2.34
> 6.79%
> 1.12%
> 26.35900
> 2541
> 1949
> 2022
> 2.67
> 4.44%
> 96
> 77%
> 80%
> 30.549600
> 2374
> 1803
> 2023
> 2.04
> 5.139
> -1.36
> -5.52%
> 1.049
> -21.5190o
> 2064
> 1568
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
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
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0s
> Performance Comparison
> Last Run:
> 9 PASS
> 1 FAIL
> Robust universe Sharpe of 1.83 is below cutoff of 1.97 (90% of Alpha)。
> Properties
> Last saved Mon 11/17/2025,7.15 PM
> 2 WARNING
> Name
> Category
> 5 PENDING
> Year
> Fitness


根据字段的定义和labs中查看了字段的分布，值范围，了解到 字段的值范围在0-10；

想了下，是否可以过滤掉一些影响robust sharpe信号的数据（可能过拟合？）

尝试了用tail处理，robust sharpe有比较明显的改善，如图：


> [!NOTE] [图片 OCR 识别内容]
> #SeCond
> Order
> A Single Data Set Alpha
> d-power(tail(a, lower
> 0,
> Upper
> 9, newval
> 01,31;
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Roturns
> Drawdown
> Margin
> bgroup_mean(d,
> industry )-d;b
> 2.31
> 5.049
> 1.56
> 5.71%
> 3.1296
> 22.649o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Cour
> 2013
> 0.55
> 6,25%
> 0.20
> 59%
> 3.12%
> 5.119oo
> 1553
> 117
> Uzation
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 1.91
> 4.799
> 1.15
> 4.5790
> 0.939
> 19.089o
> 1862
> 128
> On
> On
> VeriTy
> On
> 2015
> 4,77%
> 1.17
> 65%
> +40%
> 19.489oo
> 1899
> 139
> 2016
> 0.92
> 4.269
> 0.38
> 089
> 2.119
> 9.7793
> 1810
> 135
> 2017
> 08
> 99%
> 3.46
> 8.98%
> 0.91%
> 36.049oo
> 1831
> 141
> Clone Alpha
> 2018
> 3.92
> 4.78%
> 3.39
> 9.349
> 1.219
> 39.053o
> 2152
> 159
> 2019
> 2.19
> 4,88%
> 1.48
> 5.70%
> 1.,019
> 23.39o
> 1921
> 144
> 2020
> 2.97
> 5.68%
> 2.36
> 7.909
> 2.270
> 27.829o
> 2104
> 144
> Chart
> Pnl
> 2021
> 2.93
> 5,36%
> 2.11
> 6.479
> 1.13%
> 24.17966
> 2782
> 170
> 2022
> 2.44
> 4.809
> 1.74
> 6.359
> 2.009
> 26.479o
> 2540
> 163
> 2023
> 5,279
> ~0.81
> 299
> 1.199
> 16.29%e。
> 2152
> 148
> 40OOK
> Correlation
> ZOOOK
> Self Correlation
> Matmum
> Minimum
> Last Run;
> Power Pool Correlation
> MaMmUm
> MnImUm
> Last Run;
> Jan '14
> Jan '15
> Jan '16
> jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Malmum
> MinImUT
> Last Run:
> IS Testing Status
> Period
> I5
> 0S
> Performance Comparison
> Last Run;
> 9PASS
> Sharpe of 2.31is above cutoff ot
> .58。
> Fitness of 1.56 is above cUtoff ot 1
> Turnover ol
> 04%
> above Cutoff Of 1%。
> Properties
> Last saved Mon 11/17/2025,7.15P1
> Turnoverof
> 049
> below
> Of 709
> Weightis well distributed over instruments.
> Name
> Category
> Sub universe Sharpe of 0.98 is above cutoff of 0.68。
> Robust universe returns of 5.44% Is above cutoff of
> 14% (90% ofAlpha)。
> Currently anonymous'
> None
> Sharpe of 2.41is above cutoff of
> 58
> Pyramid theme ASIIDIISHORTINTEREST matches with multiplier of 1.3. Effective pyramid count for Genius is
> Tags
> Color
> FAIL
> Selectladd tags
> None
> Robust universe Sharpe of 2.05 is below cutoff of 2.08 (909 of Alpha)
> Long
> CUtoff
> year


最后，凭直觉用quantile 变换下分布，robust pass


> [!NOTE] [图片 OCR 识别内容]
> power(tail
> a, lOwer
> Upper
> 9,
> newval
> 01,3);
> ] Single Data Set Alpha
> bgroup
> mean (d,1
> industry)-d;
> ts_mean (X,60)
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> quantile (b,
> driver
> gaussian,
> Sigma
> 1.0 )
> 2.38
> 4.579
> 1.50
> 4.959
> 2.739
> 21.69%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> imulation Settings
> 2013
> 0.05
> 5.72%
> 0.00
> 0.11%
> 2.73%
> 0.38900
> 1385
> 1341
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
> 2.39
> 4.30%
> 1.51
> 4.98%
> 0.829
> 23.20900
> 1598
> 1548
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.66
> 4.4796
> .81
> 5.78%
> 0.929
> 25.889600
> 1648
> 1648
> 2016
> .20
> 4.01%
> 0.53
> 2.44%
> 8496
> 12.14%00
> 1602
> 1565
> 2017
> 4.39
> 4.63%
> 3.61
> 8.47%
> 0.91%
> 36.57900
> 1642
> 1601
> Clone Alpha 
> 2018
> 3.24
> 4.36%
> 2.38
> 6.73%
> 099
> 30.87900
> 869
> 1877
> 2019
> 2.57
> 4.28%
> 1.71
> 5.51%
> 0.879
> 25.73900
> 1683
> 1684
> 2020
> 3.21
> 4.899
> 2.37
> 6.84%
> 79%
> 27.96900
> 853
> 1696
> N
> Chart
> Pnl
> 2021
> 2.85
> 88%
> 89
> 5.51%
> 00%6
> 22.59900
> 2314
> 2177
> 2022
> 86
> 4.24%
> 02
> 3.79%
> 66%
> 17.88900
> 2127
> 2051
> 2023
> 2.89
> 4.419
> 2.24
> -7.48%
> .16%
> -33.90900
> 1883
> 1748
> Correlation
> Z,OOOK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
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
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 10 PASS
> 2WARNING
> Competition Al Alphas Competition 2025 does not match.
> Properties
> Last saved Mon, 11/17/2025,12:59 PM
> Theme IND Region Theme does not match with multiplier of 2。
> 5 PENDING
> Name
> Cateeorv


这个alpha op数6个，有亿点点多，尝试去掉power  ，robust也是能过的，优化完成✅


> [!NOTE] [图片 OCR 识别内容]
> d=(tail(a
> LOWer
> Upper
> newval
> 01 )
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> b=group_mean
> d,1, industry )-d;
> 2.37
> 4.569
> 1.48
> 4.909
> 2.819
> 21.47900
> quantile(b,
> driver
> gaussian,
> Sigma
> 1.01
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Urawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.11
> 5.72%
> 0.02
> 0.25%
> 2.81%
> 0.89900
> 1385
> 1341
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
> 2.41
> 4.29%
> 52
> 4.98%
> 0.80%
> 23.20900
> 1606
> 1540
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 63
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.79
> 4.46%
> 94
> 6.04%
> 0.92%
> 27.07900
> 1656
> 1640
> 2016
> 1.19
> 4.029
> 0.52
> 2.39%
> 909
> 11.9090o
> 1611
> 1556
> 2017
> 4.29
> 4.62%
> 3.47
> 8.20%
> 0.96%
> 35.52900
> 651
> 1591
> Clone Alpha 
> 2018
> 3.20
> 4.36%
> 33
> 6.61%
> 03%
> 30.33900
> 867
> 1879
> 2019
> 2.52
> 4.28%
> 65
> 5.39%6
> 0.88%
> 25.21900
> 686
> 682
> 2020
> 3.16
> 87%6
> 2.31
> 69%
> 7996
> 27.509oo
> 853
> 696
> Chart
> Pnl
> 2021
> 2.70
> 4.88%
> 1.75
> 5.24%6
> 9996
> 21.46900
> 2319
> 2172
> 2022
> 89
> 4.2596
> 05
> 3.84%
> 709
> 18.08300
> 2139
> 2039
> 2023
> 3.03
> 4.43%
> 2.39
> 7.78%
> 1.15%
> 35.07900
> 1887
> 1745
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
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
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Performance Comparison
> Last Run:
> 10 PASS
> 2 WARNING
> 5 PENDING
> Properties
> Last saved Mon; 11/17/2025,8:17 PM
> Name
> Category
> Currently 'anonymous'
> NOne


结束语：

```
这个alpha，是需要反转的，考虑到我group_mean op这个季度还没用到，所以，我把 -group_neutralize 换成了group_mean(d,1,group)-d (来着研究小组同学的讨论分享，感谢) 
```

---

### 帖子 #5: HCAC的select怎么选比较好啊
- **主帖链接**: HCAC的select怎么选比较好啊.md
- **讨论数**: 1

大佬们，HCAC的select表达式，turnover 分层不好筛选alpha,选出来的太少了，有更好的分层选择方法吗？做出来的alpha,相关性都好高的，级别都是6.x的，和G2之前几个主题的相比，相关性高了好多啊，完全看不到做出prod<0.5的sa的希望。☹️

---

### 帖子 #6: HCAC的select怎么选比较好啊
- **主帖链接**: https://support.worldquantbrain.comHCAC的select怎么选比较好啊_32985027758999.md
- **讨论数**: 1

大佬们，HCAC的select表达式，turnover 分层不好筛选alpha,选出来的太少了，有更好的分层选择方法吗？做出来的alpha,相关性都好高的，级别都是6.x的，和G2之前几个主题的相比，相关性高了好多啊，完全看不到做出prod<0.5的sa的希望。☹️

---

### 帖子 #7: HCAC的池子有多少个alpha?
- **主帖链接**: HCAC的池子有多少个alpha.md
- **讨论数**: 0

HCAC 池子的alpha有多少个啊？我昨晚上提交了1个HCAC 的sa,200多个alpha组成的。然后剩下的该主题的super alpha，以及昨晚到早上跑出来的alph，全部自相关0.6以上，晴天霹雳了! 感觉ＨＣＡＣ主题比之前的所有G2主题都要难了

---

### 帖子 #8: HCAC的池子有多少个alpha?
- **主帖链接**: https://support.worldquantbrain.comHCAC的池子有多少个alpha_33006388441367.md
- **讨论数**: 0

HCAC 池子的alpha有多少个啊？我昨晚上提交了1个HCAC 的sa,200多个alpha组成的。然后剩下的该主题的super alpha，以及昨晚到早上跑出来的alph，全部自相关0.6以上，晴天霹雳了! 感觉ＨＣＡＣ主题比之前的所有G2主题都要难了

---

### 帖子 #9: 批量检查表达式是否已存在
- **主帖链接**: MCP 工具优化实践create_multiSim 函数重构.md
- **讨论数**: 0

在使用pip安装 cnhkmcp MCP 脚本进行 WorldQuant BRAIN 平台的 Alpha 研究时，我发现 create_multi_simulation 函数存在一些设计上的不足，影响了批量研究效率。下面记录了我对该函数的重构优化过程。

## 原始函数的五大问题

#### 1. 阻塞式等待设计

原始函数提交后会阻塞等待所有子模拟完成才返回结果：

# 原始函数会阻塞等待所有子模拟完成

return await _wait_for_multisimulation_completion(location, len(alpha_expressions))

问题：提交后必须等待 8+ 分钟才能返回，容易导致客户端响应超时

#### 2. 缺乏参数校验（无效配置直接发送）

原始默认参数：

```
    neutralization: str = "NONE"    truncation: float = 0.0    nan_handling: str = "OFF"    max_trade: str = "OFF"
```

问题：neutralization="NONE" 几乎不使用；无 decay 值校验；无 truncation 校验，模型可能陷入循环微调。

#### 3. 无表达式校验机制（浪费请求配额）

问题：语法错误的表达式直接发送到平台；无法提前发现算术运算符违规；错误信息不友好。

#### 4. 无去重机制（资源浪费）

问题：同一批次内重复的表达式会重复提交；历史已回测的表达式无法识别；无法区分"回测中"和"已完成"状态。

#### 5. 缺乏可追溯性（难以排查问题）

问题：无日志记录，难以追踪回测历史，无法快速定位失败的回测任务。

---

### 帖子 #10: 批量检查表达式是否已存在
- **主帖链接**: https://support.worldquantbrain.comMCP 工具优化实践create_multiSim 函数重构_40123947595671.md
- **讨论数**: 0

在使用pip安装 cnhkmcp MCP 脚本进行 WorldQuant BRAIN 平台的 Alpha 研究时，我发现 create_multi_simulation 函数存在一些设计上的不足，影响了批量研究效率。下面记录了我对该函数的重构优化过程。

## 原始函数的五大问题

#### 1. 阻塞式等待设计

原始函数提交后会阻塞等待所有子模拟完成才返回结果：

# 原始函数会阻塞等待所有子模拟完成

return await _wait_for_multisimulation_completion(location, len(alpha_expressions))

问题：提交后必须等待 8+ 分钟才能返回，容易导致客户端响应超时

#### 2. 缺乏参数校验（无效配置直接发送）

原始默认参数：

```
    neutralization: str = "NONE"    truncation: float = 0.0    nan_handling: str = "OFF"    max_trade: str = "OFF"
```

问题：neutralization="NONE" 几乎不使用；无 decay 值校验；无 truncation 校验，模型可能陷入循环微调。

#### 3. 无表达式校验机制（浪费请求配额）

问题：语法错误的表达式直接发送到平台；无法提前发现算术运算符违规；错误信息不友好。

#### 4. 无去重机制（资源浪费）

问题：同一批次内重复的表达式会重复提交；历史已回测的表达式无法识别；无法区分"回测中"和"已完成"状态。

#### 5. 缺乏可追溯性（难以排查问题）

问题：无日志记录，难以追踪回测历史，无法快速定位失败的回测任务。

---

### 帖子 #11: USA_risk64短年份数据-20251019
- **主帖链接**: USA_risk64短年份数据-20251019.md
- **讨论数**: 0

[

'rsk64_accounting_financialoperations_remained',

'rsk64_accounting_financialoperations_removed',

'rsk64_brand_reputation_added',

'rsk64_brand_reputation_remained',

'rsk64_brand_reputation_removed',

'rsk64_debt_financing_added',

'rsk64_debt_financing_changed',

'rsk64_debt_financing_remained',

'rsk64_economy_politicalenvironment_changed',

'rsk64_economy_politicalenvironment_remained',

'rsk64_economy_politicalenvironment_removed',

'rsk64_employment_personnel_added',

'rsk64_employment_personnel_remained',

'rsk64_employment_personnel_removed',

'rsk64_environmental_social_added',

'rsk64_environmental_social_remained',

'rsk64_environmental_social_removed',

'rsk64_innovation_r_d_added',

'rsk64_innovation_r_d_changed',

'rsk64_innovation_r_d_removed',

'rsk64_litigation_legalliabilities_added',

'rsk64_litigation_legalliabilities_remained',

'rsk64_litigation_legalliabilities_removed',

'rsk64_sales_marketing_added',

'rsk64_sales_marketing_remained',

'rsk64_sales_marketing_removed',

'rsk64_shareprice_shareholderrights_changed',

'rsk64_shareprice_shareholderrights_remained',

'rsk64_taxation_governmentincentives_added',

'rsk64_taxation_governmentincentives_remained',

'rsk64_taxation_governmentincentives_removed'

]

---

### 帖子 #12: USA_risk64短年份数据-20251019
- **主帖链接**: https://support.worldquantbrain.comUSA_risk64短年份数据-20251019_35731971776407.md
- **讨论数**: 0

[

'rsk64_accounting_financialoperations_remained',

'rsk64_accounting_financialoperations_removed',

'rsk64_brand_reputation_added',

'rsk64_brand_reputation_remained',

'rsk64_brand_reputation_removed',

'rsk64_debt_financing_added',

'rsk64_debt_financing_changed',

'rsk64_debt_financing_remained',

'rsk64_economy_politicalenvironment_changed',

'rsk64_economy_politicalenvironment_remained',

'rsk64_economy_politicalenvironment_removed',

'rsk64_employment_personnel_added',

'rsk64_employment_personnel_remained',

'rsk64_employment_personnel_removed',

'rsk64_environmental_social_added',

'rsk64_environmental_social_remained',

'rsk64_environmental_social_removed',

'rsk64_innovation_r_d_added',

'rsk64_innovation_r_d_changed',

'rsk64_innovation_r_d_removed',

'rsk64_litigation_legalliabilities_added',

'rsk64_litigation_legalliabilities_remained',

'rsk64_litigation_legalliabilities_removed',

'rsk64_sales_marketing_added',

'rsk64_sales_marketing_remained',

'rsk64_sales_marketing_removed',

'rsk64_shareprice_shareholderrights_changed',

'rsk64_shareprice_shareholderrights_remained',

'rsk64_taxation_governmentincentives_added',

'rsk64_taxation_governmentincentives_remained',

'rsk64_taxation_governmentincentives_removed'

]

---

### 帖子 #13: USA_socialmedia_单字段回测pnl异常字段记录-20251019
- **主帖链接**: USA_socialmedia_单字段回测pnl异常字段记录-20251019.md
- **讨论数**: 1

```
['vec_avg(scl4_quote_total_tb)', 'vec_avg(scl4_question_likes_fb)', 'vec_avg(scl4_includes_question_total_tb)', 'vec_avg(scl4_audio_total_tb)', 'vec_avg(scl4_includes_link_total_gp)', 'vec_avg(scl4_video_total_gp)', 'vec_avg(scl4_video_total_tb)', 'vec_avg(scl39_top5_people_also_watch_ticker_ii)', 'vec_avg(scl4_comments_total_gp)', 'vec_avg(scl4_includes_question_total_gp)', 'vec_avg(scl4_call_to_comment_total_tb)', 'vec_avg(scl4_includes_link_actions_total_ig)', 'vec_avg(scl4_plusones_total_gp)', 'vec_avg(scl4_offer_total_fb)', 'vec_avg(scl4_other_shares_fb)', 'vec_avg(scl4_text_total_gp)', 'vec_avg(scl4_includes_question_actions_total_ig)', 'vec_avg(scl4_reblogs_total_tb)', 'vec_avg(scl4_reshares_total_gp)', 'vec_avg(scl4_posts_total_gp)', 'vec_avg(scl4_offer_comments_fb)', 'vec_avg(scl4_answer_total_tb)', 'vec_avg(scl4_chat_total_tb)', 'vec_avg(scl4_call_to_reblog_total_tb)', 'vec_avg(scl4_offer_shares_fb)', 'vec_avg(scl4_actions_total_gp)', 'vec_avg(scl4_likes_total_tw)', 'vec_avg(scl4_includes_link_total_tb)', 'vec_avg(scl4_other_total_fb)', 'vec_avg(scl4_question_comments_fb)', 'vec_avg(scl4_other_likes_fb)', 'vec_avg(scl4_call_to_like_total_tb)', 'vec_avg(scl4_link_total_tb)', 'vec_avg(scl4_offer_likes_fb)', 'vec_avg(scl4_other_comments_fb)', 'vec_avg(scl4_question_shares_fb)', 'vec_avg(scl4_includes_link_media_total_ig)', 'vec_avg(scl4_includes_hashtag_total_tb)', 'vec_avg(scl4_includes_hashtag_total_gp)', 'vec_avg(scl4_photo_total_gp)', 'vec_avg(scl4_question_total_fb)', 'vec_avg(scl4_includes_question_media_total_ig)']
```


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 1
> Vec_avg (scl4_question
> likes_fb )
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> ulation Settings
> 0.39
> 27.389
> 0.27
> 12.96%
> 50.71%
> 9.46%0。
> ;trument Type
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
> uity
> USA
> TOP3000
> Fast Expression
> 0.08
> None
> On
> On
> Verify
> On
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Cc
> 2013
> -0.41
> 30.68%
> -0.18
> -5.85%
> 15.43%
> 3.81%o0
> 154
> 2014
> 0.86
> 37.28%
> -0.70
> -24.68%
> 40.40%
> -13.249o。
> 81
> 2015
> 1.51
> 4.46%
> 3.41
> 63.75%
> 25.92%
> 285.64%oo
> Clone Alpha
> 2016
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2017
> 00
> 0.00%
> 0.00
> 00%
> 0.00%
> 0.009oo
> 2018
> 00
> .00%
> 00
> .009
> .00%
> 00%oo
> Chart
> Pnl
> 2019
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2020
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2021
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.009
> 0.009oo
> 2022
> 0.00
> .00%
> 00
> 0.00%
> 0.00%
> 0.00%oo
> 2023
> 0.00
> 00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.88
> 27.389
> 0.87
> 26.91%
> 41.799
> 19.66%0。
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
> Pnl
> Risk Neutralized Pnl
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:



> [!NOTE] [图片 OCR 识别内容]
> Code
> Is Summary
> Period
> IS 
> 05
> avg (SCZ4_includes_question_total_gp )
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> nulation
> Settings
> 0.04
> 16.459
> 0.01
> 0.649
> 29.71%
> 0.789o。
> strument Type
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
> juity
> USA
> TOP3000
> Fast Expression
> 0.08
> None
> On
> On
> Verify
> On
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.09
> 21.95%
> -0.71
> 9.40%
> 13.42%
> 8.56900
> 147
> 789
> 2014
> 0.21
> 18.60%
> 0.07
> -2.06%
> 8.44%
> 2.219600
> 190
> 800
> 2015
> 0.09
> 19.65%
> 0.02
> 0.83%
> 7.29%
> 0.85960o
> 240
> 815
> Clone Alpha
> 2016
> -1.40
> 22.35%
> -1.11
> 13.98%
> 16.44%
> -12.51%00
> 282
> 817
> 2017
> 0.31
> 18.28%
> 0.13
> 3.08%
> 12.19%
> 3.379600
> 143
> 892
> 2018
> 0.71
> 16.71%
> 0.55
> 9.94%
> 8.24%
> 11.9090。
> 89
> 778
> Chart
> Pnl
> 2019
> 1.17
> 5.45%
> 1.35
> 16.72%
> 11.00%
> 61.32900
> 365
> 161
> 2020
> 0.03
> 1.93%
> 0.01
> 0.85%
> 20.25%
> 8.859o0
> 2021
> 00
> 0.00%
> 00
> 009
> 0.00%
> 00%oo
> 2022
> 00
> 0.00%
> 00
> 0.00%
> 0.00%
> 009oo
> 2023
> 00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 00?ooo
> 2,00OK
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.16
> 16.45%
> 0.05
> 1.929
> 19.149
> 2.33900
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
> Pnl
> Risk Neutralized Pnl
> Correlation
> VeC_


---

### 帖子 #14: USA_socialmedia_单字段回测pnl异常字段记录-20251019
- **主帖链接**: https://support.worldquantbrain.comUSA_socialmedia_单字段回测pnl异常字段记录-20251019_35734548869911.md
- **讨论数**: 1

```
['vec_avg(scl4_quote_total_tb)', 'vec_avg(scl4_question_likes_fb)', 'vec_avg(scl4_includes_question_total_tb)', 'vec_avg(scl4_audio_total_tb)', 'vec_avg(scl4_includes_link_total_gp)', 'vec_avg(scl4_video_total_gp)', 'vec_avg(scl4_video_total_tb)', 'vec_avg(scl39_top5_people_also_watch_ticker_ii)', 'vec_avg(scl4_comments_total_gp)', 'vec_avg(scl4_includes_question_total_gp)', 'vec_avg(scl4_call_to_comment_total_tb)', 'vec_avg(scl4_includes_link_actions_total_ig)', 'vec_avg(scl4_plusones_total_gp)', 'vec_avg(scl4_offer_total_fb)', 'vec_avg(scl4_other_shares_fb)', 'vec_avg(scl4_text_total_gp)', 'vec_avg(scl4_includes_question_actions_total_ig)', 'vec_avg(scl4_reblogs_total_tb)', 'vec_avg(scl4_reshares_total_gp)', 'vec_avg(scl4_posts_total_gp)', 'vec_avg(scl4_offer_comments_fb)', 'vec_avg(scl4_answer_total_tb)', 'vec_avg(scl4_chat_total_tb)', 'vec_avg(scl4_call_to_reblog_total_tb)', 'vec_avg(scl4_offer_shares_fb)', 'vec_avg(scl4_actions_total_gp)', 'vec_avg(scl4_likes_total_tw)', 'vec_avg(scl4_includes_link_total_tb)', 'vec_avg(scl4_other_total_fb)', 'vec_avg(scl4_question_comments_fb)', 'vec_avg(scl4_other_likes_fb)', 'vec_avg(scl4_call_to_like_total_tb)', 'vec_avg(scl4_link_total_tb)', 'vec_avg(scl4_offer_likes_fb)', 'vec_avg(scl4_other_comments_fb)', 'vec_avg(scl4_question_shares_fb)', 'vec_avg(scl4_includes_link_media_total_ig)', 'vec_avg(scl4_includes_hashtag_total_tb)', 'vec_avg(scl4_includes_hashtag_total_gp)', 'vec_avg(scl4_photo_total_gp)', 'vec_avg(scl4_question_total_fb)', 'vec_avg(scl4_includes_question_media_total_ig)']
```


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 1
> Vec_avg (scl4_question
> likes_fb )
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> ulation Settings
> 0.39
> 27.389
> 0.27
> 12.96%
> 50.71%
> 9.46%0。
> ;trument Type
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
> uity
> USA
> TOP3000
> Fast Expression
> 0.08
> None
> On
> On
> Verify
> On
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Cc
> 2013
> -0.41
> 30.68%
> -0.18
> -5.85%
> 15.43%
> 3.81%o0
> 154
> 2014
> 0.86
> 37.28%
> -0.70
> -24.68%
> 40.40%
> -13.249o。
> 81
> 2015
> 1.51
> 4.46%
> 3.41
> 63.75%
> 25.92%
> 285.64%oo
> Clone Alpha
> 2016
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2017
> 00
> 0.00%
> 0.00
> 00%
> 0.00%
> 0.009oo
> 2018
> 00
> .00%
> 00
> .009
> .00%
> 00%oo
> Chart
> Pnl
> 2019
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2020
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2021
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.009
> 0.009oo
> 2022
> 0.00
> .00%
> 00
> 0.00%
> 0.00%
> 0.00%oo
> 2023
> 0.00
> 00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.88
> 27.389
> 0.87
> 26.91%
> 41.799
> 19.66%0。
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
> Pnl
> Risk Neutralized Pnl
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:



> [!NOTE] [图片 OCR 识别内容]
> Code
> Is Summary
> Period
> IS 
> 05
> avg (SCZ4_includes_question_total_gp )
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> nulation
> Settings
> 0.04
> 16.459
> 0.01
> 0.649
> 29.71%
> 0.789o。
> strument Type
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
> juity
> USA
> TOP3000
> Fast Expression
> 0.08
> None
> On
> On
> Verify
> On
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.09
> 21.95%
> -0.71
> 9.40%
> 13.42%
> 8.56900
> 147
> 789
> 2014
> 0.21
> 18.60%
> 0.07
> -2.06%
> 8.44%
> 2.219600
> 190
> 800
> 2015
> 0.09
> 19.65%
> 0.02
> 0.83%
> 7.29%
> 0.85960o
> 240
> 815
> Clone Alpha
> 2016
> -1.40
> 22.35%
> -1.11
> 13.98%
> 16.44%
> -12.51%00
> 282
> 817
> 2017
> 0.31
> 18.28%
> 0.13
> 3.08%
> 12.19%
> 3.379600
> 143
> 892
> 2018
> 0.71
> 16.71%
> 0.55
> 9.94%
> 8.24%
> 11.9090。
> 89
> 778
> Chart
> Pnl
> 2019
> 1.17
> 5.45%
> 1.35
> 16.72%
> 11.00%
> 61.32900
> 365
> 161
> 2020
> 0.03
> 1.93%
> 0.01
> 0.85%
> 20.25%
> 8.859o0
> 2021
> 00
> 0.00%
> 00
> 009
> 0.00%
> 00%oo
> 2022
> 00
> 0.00%
> 00
> 0.00%
> 0.00%
> 009oo
> 2023
> 00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 00?ooo
> 2,00OK
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.16
> 16.45%
> 0.05
> 1.929
> 19.149
> 2.33900
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
> Pnl
> Risk Neutralized Pnl
> Correlation
> VeC_


---

### 帖子 #15: VF更新了，你们的VF如何？
- **主帖链接**: VF更新了你们的VF如何.md
- **讨论数**: 0

====================================================================

4月份交的alpha确实很一般，vf跌了一些。需要反思，总结。

uu们呢？有涨vf的分享下经验吗？

祝小伙伴们vf up up up!

====================================================================

---

### 帖子 #16: VF更新了，你们的VF如何？
- **主帖链接**: https://support.worldquantbrain.comVF更新了你们的VF如何_33128565084823.md
- **讨论数**: 0

====================================================================

4月份交的alpha确实很一般，vf跌了一些。需要反思，总结。

uu们呢？有涨vf的分享下经验吗？

祝小伙伴们vf up up up!

====================================================================

---

### 帖子 #17: WorldQuant BRAIN MCP 工具调用架构升级：从 Stdio 到 HTTP API代码优化
- **主帖链接**: WorldQuant BRAIN MCP 工具调用架构升级从 Stdio 到 HTTP API代码优化.md
- **讨论数**: 4

## 背景

在  CLI 进行 WorldQuant BRAIN 平台的 Alpha 研究时，我最初采用 MCP (Model Context Protocol) 的 Stdio Transport 协议。这种方式虽然简单，但在实际使用中频繁出现连接中断问题，导致 AI 自动化任务被迫停止，需要人工介入重启服务。

经过分析，问题的根源在于 Stdio 协议的特性：MCP Server 作为 CLI 的子进程运行，当 CLI 会话超时、网络波动或进程资源竞争时，Stdio 管道容易断裂，导致整个工具链失效。

解决方案是将 MCP 架构从 Stdio Transport 升级为 HTTP API，实现服务进程与 CLI 的解耦。

---

### 帖子 #18: WorldQuant BRAIN MCP 工具调用架构升级：从 Stdio 到 HTTP API代码优化
- **主帖链接**: https://support.worldquantbrain.comWorldQuant BRAIN MCP 工具调用架构升级从 Stdio 到 HTTP API代码优化_40150797833239.md
- **讨论数**: 4

## 背景

在  CLI 进行 WorldQuant BRAIN 平台的 Alpha 研究时，我最初采用 MCP (Model Context Protocol) 的 Stdio Transport 协议。这种方式虽然简单，但在实际使用中频繁出现连接中断问题，导致 AI 自动化任务被迫停止，需要人工介入重启服务。

经过分析，问题的根源在于 Stdio 协议的特性：MCP Server 作为 CLI 的子进程运行，当 CLI 会话超时、网络波动或进程资源竞争时，Stdio 管道容易断裂，导致整个工具链失效。

解决方案是将 MCP 架构从 Stdio Transport 升级为 HTTP API，实现服务进程与 CLI 的解耦。

---

### 帖子 #19: 计算置信度
- **主帖链接**: https://support.worldquantbrain.com[L2] Alpha PNL 合法性检测【自动剔除 厂 Alpha等无效Alpha实现高效率剪枝】代码优化_32761924007703.md
- **讨论数**: 25

在进行培训代码回测时，我发现一个规律：如果一个 Alpha 在一阶回测时表现为 “厂” Alpha（指 PNL 呈现特定不良模式），那么基于这个 Alpha 进行后续的二阶、三阶优化或组合，其结果大概率仍然是“厂”Alpha。因此，我认为有必要在初步筛选阶段就将这类 Alpha 剔除。


> [!NOTE] [图片 OCR 识别内容]
> ts_delay ( fnd6_nitq/ fnd6_cptnewq_ceqq,
> 240
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> RetUrhs
> DrawdOwh
> Margin
> Simulation Settings
> 2.62
> 5.729
> 5.85
> 62.409
> 13.239
> 218.339600
> Instrument Type:
> Equity
> Truncation:
> 0.08
> 这个
> alpha 的各个指标都很高
> Region:
> ASI
> Neutralization:
> Subindustry
> Universe:
> MINVOLIM
> Pasteurization:
> On
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Language:
> Fast Expression
> NaN
> Handling:
> 0n
> Decay:
> Unit Handling:
> Verify
> 2013
> 2.03
> 3.4595
> 3.52
> 37.5495
> 13.2395
> 218.33900
> Max Trade:
> On
> 2014
> 0.00
> 0.0095
> 0.00
> 00%
> 00%
> 0.00Soo
> 2015
> 0.00
> 0.0095
> U.UU
> 0.009
> 0.0095
> 00Dooo
> 2016
> 0.00
> 0.0095
> 0,0095
> 0.009
> 0.00Soo
> Clone Alpha 
> 2017
> 0.00
> 0.009
> 0,0095
> 0Oo
> 0.00Soo
> 但
> PNL 是不合法的
> 2018
> 0.00
> 0.0095
> U.UU
> 0.0095
> 0.0095
> 00Dooa
> N
> Chart
> Pnl
> 2019
> 0.00
> 000
> 00O
> 0Oo
> 0OSoo
> 2020
> 0.00
> 0.0095
> U.UU
> 0.0095
> 009
> 00Dooa
> 2021
> 0.00
> 0.0095
> 0.00
> 0.009
> 0.0095
> 00Dooo
> 2022
> 0.009
> 0OSoo
> 下面的提交按钮
> 2023
> 有瞧候熊是趟的
> 0.00
> 0.0095
> 0.0095
> 但是实际点击后是通过不了的
> Risk neutralized
> Aggregate Data
> Sharpe
> TurhoVer
> Fitness
> Returns
> Drawdown
> Margin
> 2.16
> 5.72%
> 4.39
> 51.66%
> 13.43%
> 180.749600
> Delay:
> 0OYooo


两个步骤，就能开箱即用

**1.** 新建一个名为 **pnl_test.py**  的Python 文件  **，粘贴下列代码（并修改登录信息为你的实际登录信息）**

```
import osfrom dotenv import load_dotenvimport loggingimport timeimport requestsfrom machine_lib import *class cfg:    env_path = "user.env"    load_dotenv(dotenv_path=env_path)    username = os.environ["USER_NAME"]    password = os.environ["PASSWORD"]def sign_in(username, password):    s = requests.Session()    s.auth = (username, password)    try:        response = s.post('[链接已屏蔽])        response.raise_for_status()        logging.info("Successfully signed in")        return s    except requests.exceptions.RequestException as e:        logging.error(f"Login failed: {e}")        return Nonedef wait_get(url: str, max_retries: int = 10) -> "Response":    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef check_consecutive_non_zero_values(alpha_id, data, required_streak=200):    if not data or len(data) < required_streak:        return True    def check_column(column_data):        if len(column_data) < required_streak:            return True        current_streak_count = 0        current_streak_value = None        for value in column_data:            if value != 0:                if value == current_streak_value:                    current_streak_count += 1                else:                    current_streak_value = value                    current_streak_count = 1            else:                current_streak_value = None                current_streak_count = 0            if current_streak_count >= required_streak:                return False        return True    column1_values = []    column2_values = []    for row in data:        if len(row) >= 3:            column1_values.append(row[1])            column2_values.append(row[2])        else:            pass    if column1_values and column2_values:        is_col1_all_zeros = all(v == 0 for v in column1_values)        is_col2_all_zeros = all(v == 0 for v in column2_values)        if is_col1_all_zeros or is_col2_all_zeros:            print(alpha_id, "不合法")            return False    if not check_column(column1_values):        print(alpha_id, "不合法")        return False    if not check_column(column2_values):        print(alpha_id, "不合法")        return False    print(alpha_id, "通过")    return Truedef get_alpha_pnl_legal(alpha_id: str) -> bool:    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    records = pnl["records"]    return check_consecutive_non_zero_values(alpha_id, records)def get_alpha_pnl_legal_list(fo_tracker: list) -> list:    global sess    sess = sign_in(cfg.username, cfg.password)    fo_tracker =[fo for fo in fo_tracker if get_alpha_pnl_legal(fo[0])]    return fo_trackersess = sign_in(cfg.username, cfg.password)
```

**2.  在notebook中** 修改其中筛选第一次回测完的Alpha

```
fo_tracker = get_alphas("06-12", "06-13", 1, 0.7, "ASI", 200, "track")# 添加以下几行import pnl_testf_num = len(fo_tracker)print(f_num,"个alpha 进行pnl合法检测，请耐心等待")fo_tracker = pnl_test.get_alpha_pnl_legal_list(fo_tracker)print(f_num -len(fo_tracker),"个不合法的pnl,已被剔除" )
```

**希望这个小脚本能帮你提升回测效率。** 
 **觉得还行？一个小赞就能让我动力满满，一起day day Alpha！**

---

### 帖子 #20: How to Improve After Cost Performance置顶的
- **主帖链接**: [L2] How to Improve After Cost Performance置顶的.md
- **讨论数**: 228

Improving After Cost Performance plays an important role in improving Combined Alpha Performance. In this post, we will share some tips to improve on  [***After-cost Sharpe ratio***](/hc/en-us/articles/25960264611351-What-s-After-cost-Sharpe-ratio) .

1. **Manage Turnover** : Consider both average daily and maximum daily turnover. Use daily turnover plots to identify turnover peaks. Try to reduce high peaks of turnover, even if the average daily turnover is already low.
   
> [!NOTE] [图片 OCR 识别内容]
> Average Turnover is Iow, but max turnoveris high:
> Average Turnoveris the same, max turnover is lower
> Chart
> Turnoer
> Chart
> Turnover
> L0
> 38
> 36。
> Jul 1
> Jon't
> Jan 15
> Jults
> Jull6
> Jun 1
> Jul
> Jan *18
> Jultg
> Jnn1g
> Jn'20
> Jonl
> Jan'15
> Jul15
> Jan"6
> Jult6
> Jul
> Jn'13
> Jonlg
> Jol1g
> Jn 20 Jul 20
> J|
> O
> Jul
> JTo
> u
 Use tradewhen, hump, ts_target_tvr_delta_limit, ts_delta_limit operators to control turnover.
2. **Optimize Alpha Weights Distribution** : Ensure the distribution of Alpha weights by capitalization is balanced. Use visualization tools to check the size by capitalization, ensuring it is evenly distributed or skewed towards high-capitalization stocks.
   
> [!NOTE] [图片 OCR 识别内容]
> Size is skewed to low capitalization part of universe (0-20%)=
> Size is skewed to high capitalization part of universe (80-100%):
> Chart
> UETAe SZe Cy LA9It
> Iaton
> N Chart
> uVeraBe SIZe By Capital
> ALTC
> OILTC
> 0201
> GC
> L5
> AFTm
> 741
> 05T
> 0-209
> 20-409
> 40-605
> 60-805
> 801009
> 020
> 20405
> UFT;
> 60-809
> 87-1009
> LatICn

3. **Ensure High Coverage** : Focus on maintaining good coverage, especially in the liquid part of the universe. Coverage (long plus short count) should be at least half of the universe and should come from liquid stocks. Short count should not be much higher than long count.
   
> [!NOTE] [图片 OCR 识别内容]
> Long count
> short count less then half of Universe size (TOP3000), short count greater then long count:
> Vear
> TIOVer
> Ftnoss
> Returns
> Drawdown
> Count
> Short Count
> 712
> -0.80
> 5J.5:
> 0.3
> 1031
> 9.571
> 一:
> 353
> 3013
> 61,83
> 9,57
> 339
> 3.135
> 71-
> 0.02
> 5J.41:
> -0.275
> 10.731
> 02
> 7015
> 0,75
> 60,949
> 33
> 7003
> 375
> 393
> 5-3
> 7016
> 0.13
> 51.35?
> 00-
> 28035
> 19.3191
> 0.31
> 411
> 533
> -017
> 0.53
> 61,73
> 01-
> 一03
> 5.2491
> 13
> 390
> 5
> 7013
> 1 4
> 60.30
> 0.3-
> 20.755
> 1-191
> 6.31
> 397
> 5-
> 2019
> 1_
> 59.52
> 0.3-
> 70.6293
> 53
> 5
> 2020
> 62.66
> 13.2540
> 77.-59
> 33525
> 392
> SD
> Long count + short count close to Universe size (TOP3000), long count approx. equal to short count
> Year
> TUINOVeT
> Ftness
> Returs
> Drawdown
> Maryin
> Cont
> Short Count
> 201
> -9
> 74034
> 1.10
> 1-:
> 3.15
> 90
> 151
> 1+35
> 2013
> 2.5
> 73.59
> 1345
> 375
> 655
> 1557
> 1474
> 201-
> 73-5:
> 1.70
> 335:
> 525
> 1
> 1535
> 1433
> 21
> 73.55;:
> 17:
> 495
> 3::
> 51
> 122
> 2015
> 73.37:
> 057
> 1 -3:
> -15
> 3::
> 53
> S
> 7017
> 73.33
> 51:
> 477
> 1.55
> 53
> 1493
> 3013
> 7354
> 0
> 1255
> 50
> 49
> 153
> 1517
> 2013
> 72.351
> D0i
> 0.75:
> 955
> 021s
> 1525
> 1510
> 2027
> 412
> 75.97:
> 73.51:
> 一5
> 21.3::
> 1-
> 1453
> Sharp
> Marmn
> L9
> 5。
> Sharpe
> Long

4. **Evaluate Sub-Universe Performance** : Check sub-universe test results and avoid submitting. Alphas that only just pass the Sub-universe Sharpe test. You can also construct your own sub-universe tests using fields from the Universe dataset to evaluate performance across all sub-universes.
   
> [!NOTE] [图片 OCR 识别内容]
> Original alpha. USA/dI/TOP3OOO/Market:
> signal
> tsdecaylinear(-returns, 5);
> alpha
> scale(group_neutralize(signal
> subindustry));
> alpha
> Aggregate Data
> Sharpe
> TUTnOET
> FIIES =
> TETUPI=
> LRaVCC
> Marain
> 1.90
> 73.66%
> 0.90
> 16.43%
> 9.169
> 4.469000
> Apply TOPSOO sub-universe test using 'tOp5OO' data field:
> Signal
> tsdecay linear(-
> returns _
> 5);
> alpha
> Scale
> Broup_neutralize(signal_
> subindustry));
> top500>0
> alpha
> han
> ABgreBate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drswoown
> Marain
> 1.17
> 73.319
> 0.47
> 11.6796
> 11.769
> 3.180000

5. **Turn on Max Trade option for ASI Alphas** : The Max Trade option must be set to ON for all Alphas in the ASI region. This setting optimizes ASI Alphas and improves After Cost Performance at combo level.

---

### 帖子 #21: Lab中处理Vector数据的一种方法代码优化
- **主帖链接**: [L2] Lab中处理Vector数据的一种方法代码优化.md
- **讨论数**: 0

这几天使用Lab时发现在可视化Vector数据时会报错，我的方法是定义一些函数，然后在读取原始数据后对Vector数据处理并进行可视化。

**1. 定义函数**

```
def vec_sum(x):    if isinstance(x, (list, np.array):        return np.sum(x)    return np.nandef vec_count(x):    if isinstance(x, (list, np.array):        return len(x)    return np.nandef vec_max(x):    if isinstance(x, (list, np.array):        return np.max(x)    return np.nan
```

**2. 可视化时调用**

```
model_field_df = brain.get_data_frame(brain.get_data_field("close"), universe="TOP3000", dates=[(">", "2021-01-01")]vec_processed_df = model_field_df.map(vec_max)visualizations.plot_values_distribution([vec_processed_df], names=["close values distribution"], nbins=100)
```

函数我只定义了几个常用的，各位可以根据自己的需求扩展。这个方法比较方便，输入一次后未来的代码修改量很小，某种程度也避免了Lab输入的效率低和复制粘贴不方便的问题。

以上就是我的方法，希望能帮助到大家。最后祝各位研究和投资顺利！

---

### 帖子 #22: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: [L2] Machine Alpha 基础知识1什么是Alpha模板.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #23: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #24: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: [L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #25: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #26: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 进阶知识2如何优化Alpha模板中的参数案例续_28133464556311.md
- **讨论数**: 2

各位研究顾问，大家好。承接上文👉 [Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一](../顾问 JR23144 (Rank 6)/[Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一_27789509613335.md)  我们讨论了如何使用爬山算法（梯度下降）来找到局部最优点的参数。您可能已经熟悉了整体概念。然而，即使在引入随机重启的情况下改变了最初的爬山算法，仍然有改进的空间，因为每次重启并没有利用先前的信息。今天，我们将通过探索几种可以增强算法的修改来结束这一话题的简单讨论。🚀

### 普通随机爬山算法的基本结构

1. **初始化** ：从初始参数开始。
2. **评估** ：回测表达式并获得其适应度。
3. **选择** ：通过随机选择一个不同的参数来识别邻近组合。
4. **比较** ：重新回测更新后的表达式并获得其适应度。
5. **更新** ：如果邻近表达式显示出更好的适应度，则将当前选择更新为这个新参数集。
6. **迭代** ：重复评估、选择、比较和更新步骤，直到在n次迭代后没有进一步的改进。
7. **重启** ：重复上述步骤m次。这是重启机制。

### 智能重启 🔄

要考虑的第一个修改是确保在第七步的每次重启中，算法都会探索以前未遇到的新区域。为实现这一点，您可以在步骤三和四中实现一个参数计数器，每次选择并模拟一个选项时计数器递增。在第七步重启时，不要随机从可用集合中抽取选项，而是使用计数器的逆作为选择的概率。此修改确保每次重启都会选择在先前试验中未探索过的参数。🧠

一些人可能会问：“为什么只创建一个计数器？为什么不设计一个更智能的方法，将Alpha绩效信息入未来的概率中呢？”这是个好主意！具体怎么实现呢？欢迎大家在下面讨论您的想法！💡

### 直线路径可能不是最佳路径 🌄

正如一些人指出的那样，随机爬山算法的贪婪特性使其过于关注即时改进，从而可能忽略更优的曲线路径。有些人建议使用模拟退火作为替代，因为它在探索期间会容忍挫折，这有助于达到全局最优。为了使随机爬山算法达到类似的效果，您可以在步骤四中引入一些白噪声。这增加了选择“最佳”邻居的随机性。

有时，“最佳”邻居的适应度可能在短期内不佳，但在未来步骤中有更好的解决方案潜力！您还可以设计动态噪声，在早期阶段引入更多白噪声，并在后期逐渐减少——类似于模拟退火中的温度衰减。❄️🔥

这篇文章总结了关于爬山算法及其在Alpha研究中的应用的小系列。如果您对这些主题感兴趣，请留下评论告诉我们！💬

更多类似原文，可关注全球顾问论坛👉 [[Alpha Machine] How do you improve random-hill-climbing optimization](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Machine] How do you improve random-hill-climbing optimization被推荐的Alpha Template_27789493782935.md)

Credit to:YW42946

---

### 帖子 #27: Maximizing Combined Alpha Performance: Key Strategies and Insights
- **主帖链接**: https://support.worldquantbrain.com[L2] Maximizing Combined Alpha Performance Key Strategies and Insights_28436901080471.md
- **讨论数**: 60

The Combined Alpha Performance Score is a critical metric for reaching higher tiers in the BRAIN Genius Program. It measures how effectively your submitted Alphas work together, balancing individual performance and the synergy between them. Here’s a detailed breakdown of the factors influencing this score and strategies to improve it.

### **1. What Influences Combined Alpha Performance?**


> [!NOTE] [图片 OCR 识别内容]
> The combined Sharpe (Sc) of your Alphas is determined by three key factors:
> Average Sharpe (Sa): Higher Sharpe ratios for individual Alphas lead to a stronger combined
> SCOre
> Number of Alphas (n): Increasing the number of Alphas boosts performance, especially
> When they are uncorrelated。
> Correlation (p): Lower correlation between Alphas enhances diversification, improving the
> combined Sharpe.
> The combined Sharpe can be approximated by:
> Sa
> Sc
> 1 +
> 阮p
 ​​

### **2. Effects of Key Parameters**

**
> [!NOTE] [图片 OCR 识别内容]
> Impact of Correlation (p):
> Uncorrelated Alphas (p
> 0)
> The combined Sharpe scales with the square root of the number of Alphas
> providing
> significant diversification benefits.
> Highly Correlated Alphas (p
> 1):
> The combined Sharpe equals the average Sharpe (Sa), as diversification effects disappear。
> RSa'
**


> [!NOTE] [图片 OCR 识别内容]
> Impact of Number of Alphas (n):
> Adding more Alphas significantly improves the combined Sharpe When correlation is low. However;
> the benefit diminishes as correlation increases.
> Below is a table
> showing how the combined Sharpe changes with different values of n (number of
> Alphas) and p (correlation) , assuming an average Sharpe (Sa) of 1:
> Number
> Of
> Correlation
> Correlation
> Correlation
> Correlation
> Correlation
> Correlation
> Alphas
> 0.0
> 0.1
> 0.3
> 0.5
> 0.7
> 1.0
> 1.000
> 1.000
> 1.000
> 1.000
> 1.000
> 1.000
> 5
> 2.236
> 1.890
> 1.508
> 1.291
> 1.147
> 1.000
> 10
> 3.162
> 2.294
> 1.644
> 1.348
> 1.170
> 1.000
> 20
> 4.472
> 2.626
> 1.728
> 1.380
> 1.183
> 1.000
> 50
> 7.071
> 2.911
> 1.785
> 1.400
> 1.190
> 1.000
> 100
> 10.000
> 3.029
> 1.805
> 1.407
> 1.193
> 1.000


### **3. Strategies to Boost Combined Alpha Performance**

#### **1. Focus on Low-Correlation Alphas**

**
> [!NOTE] [图片 OCR 识别内容]
> Reduce pairwise correlation (p) by diversifying strategies, datasets, and regions。
> Use operators like  group_neutralize
> and
> group_rank
> to achieve orthogonality。
**

#### **2. Submit Uncorrelated Alphas Across Pyramids**

- Spread Alphas across multiple pyramids to mitigate drawdowns in any single pyramid.

#### **3. Increase the Number of Alphas**

- Add more Alphas to your submission pool, ensuring they remain sufficiently uncorrelated.

#### **4. Prioritize High OS Sharpe Ratios**

- Validate Alphas with the  **Test Period**  and Robustness Tests to avoid overfitting.
- Keep Alpha expressions simple and explainable to enhance  **out-of-sample**  (OS) performance.

### **4. Practical Insights from the Data**

- Submitting  **10 uncorrelated Alphas**  can improve the combined Sharpe by over  **200%**  compared to submitting a single Alpha.
- As correlation increases, the combined Sharpe converges to the average Sharpe, limiting diversification benefits.

### **Final Thoughts**

Maximizing Combined Alpha Performance requires a balance of high individual Sharpe ratios, low correlation, and an appropriately sized Alpha pool. By focusing on orthogonality and robustness, you can unlock the full potential of diversification, build resilience, and climb to higher tiers in the BRAIN Genius Program.

Let’s collaborate and share ideas! How do you ensure low correlation and high OS Sharpe in your submissions? Drop your tips and strategies in the comments below!

---

### 帖子 #28: Python Alpha 平台限制粗略小结，请大佬指正
- **主帖链接**: https://support.worldquantbrain.com[L2] Python Alpha 平台限制粗略小结请大佬指正_40742727142679.md
- **讨论数**: 13

Python Alpha 平台限制总结
1. Region 限制
- 支持: USA ✅, EUR ✅, ASI ✅, AMR ✅
- 不支持: MEA ❌ (无法创建/运行)
- 不确定: JPN, GLO 等
2. 数据字段类型限制
- 支持: MATRIX 类型 ✅（2D 数组 [lookback, n_instruments]）
- 不支持: VECTOR 类型 ❌（需要 vec_sum/vec_avg 聚合，Python 无法处理）
- 不支持: GROUP 类型 ❌
- int32 数据字段有 sentinel 值（-2147483648），需要用 get_missing_value() 或手动替换为 NaN
3. Lookback 限制
- lookback 必须 ≤ 115（120 直接 FAIL）
- 安全值：110（115 偶发 FAIL）
- 原始的 FastExpr 实际上有无限历史窗口，Python 只能看到 110 行
- 可以用 store 参数（dims="xi"）随时间累积更多数据，但初始窗口仍需 lookback 参数
4. 时间段限制
- testPeriod 必须 ≤ P6Y0M（超过6年直接 FAIL）
- 但 startDate/endDate 可以覆盖整个回测区间（如 2014-01-01 到 2023-12-31）
5. 参数限制
- unitHandling 和 nanHandling 必须省略（不传参），PYTHON 语言不支持这两个参数
- language 固定为 "PYTHON"
- maxTrade/maxPosition 等可选
6. 代码限制
- 只能 from brain.alphas import alpha 在同一个 cell/文件中
- 不能 import Brain, BrainCache, SimulationSettings 等 — 它们在服务器端不可用
- 数据数组是只读的 — 修改前必须 .copy()
- 返回类型必须是 float32 ndarray，形状 [n_instruments]
- np.nanmean/np.nanstd 在某些数据字段（如 opt23_volivcallmputs5, coverage=0.5）上使用其结果作为 np.clip 的上下界会导致 FAIL — 原因是 int32 sentinel 值被转换为 float64 后的极端值污染了统计计算
- 解决方法：使用 IQR 分位数（np.percentile）替代 mean/std 做 winsorize
7. 性能差异
- 转换后的 Python Alpha 通常能达到原版 FastExpr 的 60-80% Sharpe（由于 lookback 缩短和操作符的 numpy 近似实现）
- Train 段性能接近原版，Test 段衰减更明显（lookback 限制导致信号在测试期质量下降）
8. 错误诊断限制
- Python Alpha 失败时只返回 status: FAIL，没有详细的运行时错误日志
- 只能通过反复实验来排除问题

---

### 帖子 #29: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location']
- **主帖链接**: https://support.worldquantbrain.com[L2] Super alpha全自动回测代码--开箱即用代码优化_32637672256663.md
- **讨论数**: 30

功能省流：随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。

特点：整合了中文论坛中的super alpha代码，点击即用

感谢顾问 JL16510 (Rank 18)大佬的多线程回测代码，感谢WP88606大佬的随机生成表达式代码。我对这两篇代码做了整合，并做了一些调整，目前用该代码生成提交了几个比赛的super alpha，指标都还可以，遂分享给大家，希望能有所帮助！

有用的话还请帮忙点个小赞！

回测程序（运行这个）superAlpha.py

```
import threadingfrom machine_lib import *import randomimport selection_expressions as seneutralization_list = ["NONE","MARKET","SECTOR","INDUSTRY","SUBINDUSTRY"]conditions = [    se.category_conditions(),    se.color_conditions(),    se.neutralization_conditions(neutralization_list),    se.datacategories_conditions(),    se.datacategory_count_conditions(),    se.dataset_count_conditions(),    se.datafield_count_conditions(),    se.long_count_conditions(),    se.short_count_conditions(),    se.operator_count_conditions(),    se.prod_correlation_conditions(),    se.self_correlation_conditions(),    se.truncation_conditions(),    se.turnover_conditions(),    se.os_start_date_conditions]weight_expressions = se.weight_expressions()# 貌似author的选项用不了def author_setting():    # 从这些条件中随机选择1-2个 拼接起来返回    author_option = ["author_returns_to_drawdown>2&&","author_returns_to_drawdown<4&&","author_fitness >= 2&&","author_sharpe >= 2&&"]    # 随机选择1到2个条件    selected_conditions = random.sample(author_option, random.randint(1, 2))    # 拼接条件字符串    result = ''.join(selected_conditions)    return resultdef find_selection_expression():    condition_length = random.randint(1, 3)    condition_list = random.sample(conditions, condition_length)    choice_conditions = []    for condition in condition_list:        if callable(condition):            condition = condition()        choice_conditions.append(random.choice(condition))    choice_weight_expression = random.choice(weight_expressions)    # author_exp = author_setting()    select_expression = "not(own)&&"+"in(classifications, 'POWER_POOL')&&" + ' * '.join([f'({exp})' for exp in (choice_conditions + [choice_weight_expression])])    with open('select_expression.txt', 'a') as f:        f.write(select_expression + '\n')    return select_expressiondef get_combo_code_list():    time_windows1 = [60,120,250,500]    selected_window1 = random.choice(time_windows1)    time_windows2 = [250, 500]    selected_window2 = random.choice(time_windows2)    ret = ['1',           f'stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, {selected_window2}); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr',           ]    return retdef multi_simulate2_sa(alpha_pools, neut, region, universe, start):    global s    s = login()    brain_api_url = '[链接已屏蔽]    limit_of_concurrent_simulations = len(alpha_pools[0])    alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]    end = len(alpha_pools_2)    print(f'length:{len(alpha_pools_2)}, start:{start}')    counter: int = start    lock = threading.Lock()    def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):        while True:            global s            lock.acquire()            nonlocal counter            if counter > end - 1:                lock.release()                break            if (counter - start) % 250 == 0:  # re-login after every 60 multi_sims                s = login()            local_counter = counter            counter += 1            lock.release()            task = pools[local_counter]            sim_data_list = generate_sim_data_sa(task, region, universe, neut)            sim_data=sim_data_list[0]            try:                simulation_response = s.post('[链接已屏蔽] json=sim_data)                print(simulation_response)                simulation_progress_url = simulation_response.headers['Location']                # simulation_progress_url = simulation_response.headers.get('location')            except:                print(" loc key error")                sleep(60)                s = login()            print(f"task {local_counter} post done")            try:                while True:                    simulation_progress = s.get(simulation_progress_url)                    if simulation_progress.headers.get("Retry-After", 0) == 0:                        break                    # print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")                    sleep(float(simulation_progress.headers["Retry-After"]))                status = simulation_progress.json().get("status", 0)                if status != "COMPLETE":                    print(f"Not complete : {simulation_progress_url}")                #alpha_id = simulation_progress.json()["alpha"]                # children = simulation_progress.json().get("children", 0)                # children_list = []                # for child in children:                #     child_progress = s.get(brain_api_url + "/simulations/" + child)                #     alpha_id = child_progress.json()["alpha"]                #                #     set_alpha_properties(s,                #             alpha_id,                #             name = "saTest",                #             color = None,)            except KeyError:                print(f"look into: {simulation_progress_url}")            except Exception as e:                print(f"An error occured:{e}")            print(f"task {local_counter} simulate done")    t = []    for i in range(limit_of_concurrent_simulations):        t.append(threading.Thread(target=sim_task))        t[i].start()    for i in range(limit_of_concurrent_simulations):        t[i].join()    print("Simulate done")def generate_sim_data_sa(alpha_list, region, uni, neut):    sim_data_list = []    for selection_exp, combo_exp in alpha_list:        print(selection_exp)        print(combo_exp)        simulation_data = {            'type': 'SUPER',            'settings': {                'instrumentType': 'EQUITY',                'region': region,                'universe': uni,                'delay': 1,                'decay': 6,                'neutralization': neut,                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'ON',                'selectionHandling': random.choice(['POSITIVE','Non-Zero']),                'selectionLimit': random.choice([100,200,500]),                'language': 'FASTEXPR',                'visualization': False,            },            'selection': selection_exp,            'combo': combo_exp}        sim_data_list.append(simulation_data)    return sim_data_listif __name__ == '__main__':    while True:        selection_exp = []        exp = find_selection_expression()        selection_exp.append(exp)        combo_exp = get_combo_code_list()        sa_list = [(i, j) for i in selection_exp for j in combo_exp]        print(len(sa_list))        print(sa_list[0])        pools = load_task_pool(sa_list, 1, 3)        # print(pools[0])        region_dict = {"usa": ("USA", ["TOP3000", "TOP1000","TOP500", "TOP200"]),                       "asi": ("ASI", ["MINVOL1M"]),                       "eur": ("EUR", ["TOP2500", "TOP1200","TOP800", "TOP400"]),                       "glb": ("GLB", ["TOP3000", 'MINVOL1M']),                       "hkg": ("HKG", ["TOP800", "TOP500"]),                       "twn": ("TWN", ["TOP500", "TOP100"]),                       "jpn": ("JPN", ["TOP1600", "TOP1200"]),                       "kor": ("KOR", ["TOP600"]),                       "chn": ("CHN", ["TOP2000U"]),                       "amr": ("AMR", ["TOP600"])                       }        norm_opt = ["INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"]        risk_opt = ["FAST", "SLOW", "SLOW_AND_FAST"]        r1 = ['STATISTICAL']        cr = ["CROWDING"]        co = ["COUNTRY"]        no = ["NONE"]        neut_opt = {"USA": norm_opt + cr + risk_opt + r1,                    "GLB": co + r1,                    "EUR": co + cr + norm_opt + risk_opt + r1,                    "ASI": co + cr + norm_opt + risk_opt + no,                    "CHN": norm_opt + cr + risk_opt + r1,                    "KOR": norm_opt,                    "TWN": norm_opt,                    "HKG": norm_opt,                    "JPN": norm_opt,                    "AMR": ["COUNTRY"] + norm_opt,                    }        regi = ['usa','asi','eur','glb']        random.shuffle(regi)        for k in regi:            for i in region_dict[k][1][:1]:                print(i)                for j in neut_opt[k.upper()]:                    print(j, region_dict[k][0])                    multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)
```

然后是随机生成selection表达式的代码，放到selection_expressions.py中

```
import datetimedef category_conditions():    values = "NONE", "PRICE_REVERSION", "PRICE_MOMENTUM", "VOLUME", "FUNDAMENTAL", "ANALYST", "PRICE_VOLUME", "RELATION", "SENTIMENT"    return [f"category == \"{value}\"" for value in values]def color_conditions():    values = "NONE", "RED", "YELLOW", "GREEN", "BLUE", "PURPLE"    return [f"category == \"{value}\"" for value in values]def dataset_conditions(dataset):    return [f"in(datasets, \"{dataset}\")"]def favorite_conditions():    return [f"favorite", "not(favorite)"]def long_count_conditions():    return [f"long_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]def short_count_conditions():    return [f"short_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]def name_conditions(name):    return [f"name == \"{name}\""]def neutralization_conditions(neutralizes):    return [f"neutralization == \"{value}\"" for value in neutralizes]def operator_count_conditions():    return [f"operator_count <= {cnt}" for cnt in [1, 2, 4, 6, 8, 10]]def tags_conditions(tag):    return [f"in(tags, \"{tag}\")"]def truncation_conditions():    return [f"truncation <= {value}" for value in [0.01, 0.05, 1]]def turnover_conditions():    return [f"turnover < {value}" for value in [0.05, 0.1, 0.2, 0.3, 0.7]]def universe_conditions(universes):    return [f"universe == \"{value}\"" for value in universes]def universe_size_conditions(size=1000):    return [f"universe_size(universe) >= {size}"]def datafields_conditions(field):    return [f"in(datafields, \"{field}\")"]def dataset_count_conditions():    return [f"dataset_count <= {value}" for value in [1, 2, 3, 10]]def self_correlation_conditions():    return [f"self_correlation <= {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]def prod_correlation_conditions():    return [f"prod_correlation < {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]def os_start_date_conditions():    today = datetime.datetime.today()    delta_days = [7, 14, 30, 60, 90, 120, 180, 360, 3600]    dates = [(today-datetime.timedelta(day)).strftime('%Y-%m-%d')             for day in delta_days]    return [f"os_start_date > \"{date}\"" for date in dates]def datacategories_conditions():    values = "analyst, broker, earnings, fundamental, imbalance, insiders, institutions, \        macro, model, news, option, other, pv, risk, sentiment, shortinterest, socialmedia".split(',')    return [f"in(datacategories, \"{value.strip()}\")" for value in values]def datacategory_count_conditions():    return [f"datacategory_count <= {value}" for value in [1, 2, 3, 10]]def datafield_count_conditions():    return [f"datafield_count <= {value}" for value in [1, 2, 3, 5, 10]]def weight_expressions():    return [        "turnover", '10-turnover',        '10000-abs(long_count-short_count)', 'long_count+short_count', 'long_count', 'short_count',        '10-dataset_count',        '2-self_correlation',        '2-prod_correlation',        '100-datafield_count',        '1'    ]
```

运行 superAlpha.py就可以开始自动回测啦~

当然该代码还有很多小问题，希望大佬们可以继续完善！

都看到这了，点个赞再走吧~~

---

### 帖子 #30: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
- **主帖链接**: [L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation.md
- **讨论数**: 73

一句话总结该活动：直接在评论区评论，分享你的模板。

> ```
> 被审核通过者将获得BRAIN纪念品一份（下图背包）优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至8.31日23：59（以服务器时间为准） [图片 (图片已丢失)]

活动要求：参赛同学可发布多个模板参赛， **必须展示下列所有元素** 。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。

- 模板
  - **模板中的变量必须使用< />进行声明，不符合语法规则的评论无法参评**
  - 需阐述具体变量赋值，如operator类别、数据集id、地区等
  - 阐述搜索空间的大小
  - 阐述模板的idea，implement细节（即哪步是数据处理，哪步是主信号）
  - 产出效果（回测：Alpha数量，可以仅展示比率）
  - 建议其他顾问未来尝试的探索方向

> **再次强调，必须至少展示上述所有信息👆先到先得！有些模板过于类似的将不再被批复，建议大家快快抓住机会！**

---

### 帖子 #31: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
- **主帖链接**: https://support.worldquantbrain.com[L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **讨论数**: 30

一句话总结该活动：直接在评论区评论，分享你的模板。

> ```
> 被审核通过者将获得BRAIN纪念品一份（下图背包）优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至8.31日23：59（以服务器时间为准） 
> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> aRNIN
> BRAIN Backpack


活动要求：参赛同学可发布多个模板参赛， **必须展示下列所有元素** 。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。

- 模板
  - **模板中的变量必须使用< />进行声明，不符合语法规则的评论无法参评**
  - 需阐述具体变量赋值，如operator类别、数据集id、地区等
  - 阐述搜索空间的大小
  - 阐述模板的idea，implement细节（即哪步是数据处理，哪步是主信号）
  - 产出效果（回测：Alpha数量，可以仅展示比率）
  - 建议其他顾问未来尝试的探索方向

> **再次强调，必须至少展示上述所有信息👆先到先得！有些模板过于类似的将不再被批复，建议大家快快抓住机会！**

---

### 帖子 #32: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template_35294898626711.md
- **讨论数**: 23

1. 模板内容及效果

基本模板：

```
ts_covariance(<datafield1>,<datafield2>,<days>)
```

其中datafield1/datafield2均选自Sentiment21 dataset。

这个idea的出现其实是因为我用了Genius rank插件发现自己没用过ts_covariance。在论坛里直接搜索了ts_covariance试图省事想直接找个模板套用，跳出来的是Weijie老师之前发过的一系列" **推荐使用的数据 USA D1 TOP3000 NEWS12__partXXX（未检查数据类型）** "的帖子。News数据集和Sentiment数据集有一定相似性，所以为了降低Corr我就又找了个还没什么人用的Sentiment21数据集跑了跑，效果还是可以的。

这个基础模板只算是个一阶模板，大家外面可以自行再套signed_power/hump/trade_when等等进行进一步优化。除此之外我为了优化六维没有进一步再加operator优化效果了。下图是我在EUR/TOP2500提交的其中两个Alpha示例


> [!NOTE] [图片 OCR 识别内容]
> 431I
> 4OOJK
> SO
> UIT
> LCJK
> MOCK
> 15水
> LI[IK
> IS Summary
> eTodl
> 昵 Single Dara Set Alpha
> ReglrAph
> Fam !theme; EURIDIISENTIMENT .1 +
> APTCUaUC Dald
> TCTNNo
> TC
> 11.0296
> 1.01
> 5.1395
> 3.5896
> 9.319o



> [!NOTE] [图片 OCR 识别内容]
> 4SUOK
> 403ok
> 35OOK
> ZSUOK
> 203oK
> 1.SUK
> 1,03Ok
> I5 Summary
> Penod
> @SIngle Oata Set Mlpha
> B Power Pool Apha
> eBVlaTAInha
> Pram !theme; EURIOIISENTIUENT . 4
> AUITCIaLC
> 1,76
> 10,549
> 1,10
> 4,919
> 2,459
> 9,24900
> J UUI


虽然模板简单，跑出来效果还是不错的，交出来的alpha还能当RA，说明新数据集跑的人应该不多。

2.模板内容分析

```
ts_covariance(y, x, d) 
```

协方差(covariance)是衡量两个变量如何一起变动的统计量。如果两个变量倾向于同时高于或低于它们的平均值，则协方差为正。如果一个变量倾向于高于其平均值而另一个变量倾向于低于其平均值，则协方差为负。 
> [!NOTE] [图片 OCR 识别内容]
> 其数学公式如下:
> Cov(r, X)t
> C
> (yi - Ya)(i - X)
> 4
> it-4+1
> 其中:
> yi 和 ?i 分别是时间序列Y和X 在时间点  i 的值。
> Ya 是时间序列Y在过去
> 个周期 (从
> t-0+1
> 到 t
> 的平均值。
> Xd 是时间序列 X在过去
> 个周期 (从
> t-4+1
> 到
> 的平均值。
> 是计算协方差的时间窗口或回顾期 (lookback period)
> 简单来说。计算步骤如下:
> 确定时间窗口:  获取 y 和
> 在最近
> 天的数据。
> 计算各自的平均值:  分别计算这
> 天内
> 的平均值
> 和
> 的平均值 (Xd)。
> 计算每曰偏差:  对于这
> 天中的每一天。计算当天的
> 值与 Ya 的差值。以及当天
> 值与
> Ld 的差值。
> 计算偏差乘积之和:  将每天计算出的两个差值相乘。然后将这
> 天的乘积全部加起来。
> 求平均:  将上一步得到的总和除以
> 得到最终的协方差值。


比如说我们的alpha是

```
-ts_covariance(负面情绪，正面情绪，d)
```

那么，当d天内负面情绪得分明显降低，正面情绪得分明显升高时，这个表达式的值就会明显增大提示做多；反之则提示做空。

3.个人对该模板的想法

其实一开始我在脑补跑这个模板的结果的时候，还以为这个模板跑出来alpha的会是turnover非常高的alpha(捕捉短期情绪的剧烈波动从而做多/做空)。但最后根据结果来看，单就这个模板而言days较短时跑出的alpha结果都比较一般。我最后交的几个alpha 的days 都是设定在63/252/504等等中长期时间。

我简单查了一篇文献来寻找原因(还没仔细读)

**Investor Sentiment in Asset Pricing Models: A Review of Empirical Evidence**

文献中提到

> The prevalence of the reversal effect of the sentiment, which means that the impact of sentiment on returns usually was reversed  **with the same magnitude after 4 or 5 days** .

所以我猜，我设想的那种短期的这种剧烈情绪波动可以用来设计一些均值回归的alpha来获利？

4.总结

可以看到这个模板最初的idea其实只是来源于论坛的老帖子，只是换了个新dataset就跑出了不错的结果，这对大家来说都是一个比较简单易行的方法，可以多多尝试。

同时，我这个模板其实只是一个非常原始的想法，肯定还有很大的提升空间，也欢迎大家一起发表意见！

---

### 帖子 #33: 【alpha灵感】A股恐慌度因子在美股的应用
- **主帖链接**: [L2] 【alpha灵感】A股恐慌度因子在美股的应用.md
- **讨论数**: 17

📈【A股恐慌度因子在美股的应用】💡

大家好！今天我要分享一个超有趣的因子——恐慌度因子
这个因子是可以直接提交的哦，并且具有非常强的经济学意义。

m_ret = group_mean(returns, rank(ts_mean(cap, 20)), market);

horro = abs(returns - m_ret) / (abs(returns)+abs(m_ret)+0.1);

horro_day = ts_mean(horro, 22);

ret_std = ts_std_dev(returns, 22);

adj_ret = horro_day * ret_std * returns;

adj_ret_mean = ts_mean(adj_ret, 22);

adj_ret_std = ts_std_dev(adj_ret, 22);

horro_std_bonus = zscore(adj_ret_mean) + zscore(adj_ret_std);

-horro_std_bonus

🔍  **因子构成解析** ：

1. **m_ret** ：计算股票收益的组内均值，基于市值排名和市场的平均收益。
2. **horro** ：衡量个股收益与组内均值的偏离程度，反映恐慌情绪。
3. **horro_day** ：对恐慌情绪进行22天的移动平均，平滑数据。
4. **ret_std** ：计算22天的收益标准差，衡量波动性。
5. **adj_ret** ：结合恐慌情绪和波动性，调整收益。
6. **adj_ret_mean**  和  **adj_ret_std** ：分别计算调整后收益的均值和标准差。
7. **horro_std_bonus** ：将调整后收益的均值和标准差进行标准化，并相加，得到最终的因子值。

💡  **为什么这个因子能赚钱？**

- **做多因子值越大** ：意味着恐慌情绪较低，收益稳定，适合做多。
- **做空因子值越小** ：意味着恐慌情绪较高，收益波动大，适合做空。

因子表现：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 5,OOOK
> Sep '17
> Jan '18
> May '18
> Sep'18
> Jan '19
> '19
> Sep '19
> May '20
> Sep '20
> Jan '21
> May '21
> Sep'21
> Jan '22
> '22
> May
> May



> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> IS
> 0S
> Excellent
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> MarEin
> 1.25
> 13.539
> 2.03
> 35.689
> 39.849
> 52.739600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
>  Short Count
> 2017
> 0.22
> 13.33%
> -0.13
> -4.399
> 12.77%
> 6.5990
> 2315
> 780
> 2018
> 0.57
> 12.65%
> 0.58
> 13.0796
> 20.03%
> 20.5496o
> 2291
> 825
> 2019
> 2.59
> 13.3996
> 5.14
> 48.8796
> 12.5596
> 73.00960
> 2297
> 808
> 2020
> 0.70
> 12.53%6
> 0.90
> 20.8390
> 28.51%6
> 33.349600
> 2255
> 844
> 2021
> 14.5896
> 2.41
> 51.5596
> 24.73%
> 70.709603
> 2375
> 773
> 2022
> 2.59
> 15.35%6
> 6.05
> 83.8796
> 16.36%
> 109.249000
> 2221
> 915



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Settings
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
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Industry
> On
> On
> Verify


---

### 帖子 #34: 【alpha灵感】A股恐慌度因子在美股的应用
- **主帖链接**: https://support.worldquantbrain.com[L2] 【alpha灵感】A股恐慌度因子在美股的应用_29327820720151.md
- **讨论数**: 17

📈【A股恐慌度因子在美股的应用】💡

大家好！今天我要分享一个超有趣的因子——恐慌度因子
这个因子是可以直接提交的哦，并且具有非常强的经济学意义。

m_ret = group_mean(returns, rank(ts_mean(cap, 20)), market);

horro = abs(returns - m_ret) / (abs(returns)+abs(m_ret)+0.1);

horro_day = ts_mean(horro, 22);

ret_std = ts_std_dev(returns, 22);

adj_ret = horro_day * ret_std * returns;

adj_ret_mean = ts_mean(adj_ret, 22);

adj_ret_std = ts_std_dev(adj_ret, 22);

horro_std_bonus = zscore(adj_ret_mean) + zscore(adj_ret_std);

-horro_std_bonus

🔍  **因子构成解析** ：

1. **m_ret** ：计算股票收益的组内均值，基于市值排名和市场的平均收益。
2. **horro** ：衡量个股收益与组内均值的偏离程度，反映恐慌情绪。
3. **horro_day** ：对恐慌情绪进行22天的移动平均，平滑数据。
4. **ret_std** ：计算22天的收益标准差，衡量波动性。
5. **adj_ret** ：结合恐慌情绪和波动性，调整收益。
6. **adj_ret_mean**  和  **adj_ret_std** ：分别计算调整后收益的均值和标准差。
7. **horro_std_bonus** ：将调整后收益的均值和标准差进行标准化，并相加，得到最终的因子值。

💡  **为什么这个因子能赚钱？**

- **做多因子值越大** ：意味着恐慌情绪较低，收益稳定，适合做多。
- **做空因子值越小** ：意味着恐慌情绪较高，收益波动大，适合做空。

因子表现：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 5,OOOK
> Sep '17
> Jan '18
> May '18
> Sep'18
> Jan '19
> '19
> Sep '19
> May '20
> Sep '20
> Jan '21
> May '21
> Sep'21
> Jan '22
> '22
> May
> May



> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> IS
> 0S
> Excellent
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> MarEin
> 1.25
> 13.539
> 2.03
> 35.689
> 39.849
> 52.739600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
>  Short Count
> 2017
> 0.22
> 13.33%
> -0.13
> -4.399
> 12.77%
> 6.5990
> 2315
> 780
> 2018
> 0.57
> 12.65%
> 0.58
> 13.0796
> 20.03%
> 20.5496o
> 2291
> 825
> 2019
> 2.59
> 13.3996
> 5.14
> 48.8796
> 12.5596
> 73.00960
> 2297
> 808
> 2020
> 0.70
> 12.53%6
> 0.90
> 20.8390
> 28.51%6
> 33.349600
> 2255
> 844
> 2021
> 14.5896
> 2.41
> 51.5596
> 24.73%
> 70.709603
> 2375
> 773
> 2022
> 2.59
> 15.35%6
> 6.05
> 83.8796
> 16.36%
> 109.249000
> 2221
> 915



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Settings
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
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Industry
> On
> On
> Verify


---

### 帖子 #35: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Lucky】为七十二变加上WQB回测配置--进行批量回测经验分享_36864734537879.md
- **讨论数**: 6

72 变是一个十分好用的工具，但是生成的 json 是没有回测配置的

> e.g.

> 
> [!NOTE] [图片 OCR 识别内容]
> 人9OOJIV
>  ]
> ATa_geVe4teU0133101131301
> "group_neutralize (rank(ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry)"'
> "group_neutralize( rank (ts_backfill (workforce_pillar_composite_score,
> 30) ) ,
> industry )
> "group_neutralize (rank(ts_backfill(anl8l_confidence_level_percent , 30)), industry)
> "group_neutralize ( rank (ts_std_dev (mdl177_liqcoeff,
> 21)
> /
> ts_mean (mdl177_liqcoeff
> 126) ),
> industry)",
> "group_neutralize ( rank
> ts_backfill(sustainability_sector_percentile,
> 30) ) ,
> industry)


为了提升回测效率，设计了一个脚本，将七十二变生成的 json转换成成 WQB 能直接回测的带回测配置的json

> e.g.
> 
> [!NOTE] [图片 OCR 识别内容]
> "type"
> 
> IREGULAR"
> settings":
> {
> "instrumentType":
> IEQUITYI
> 11
> "region":
> IND"
> Iuniverse":
> ITOP5OO"
> "delay":
> 1,
> "decay":
> 5 
> Ineutralization":
> IFASTI
> Itruncation": 0.08,
> 'pasteurization":
> ION"'
> ItestPeriod":
> IIPOYOMII
> "unitHandling":
> IVERIFYI
> "nanHandling
> IOFFI
> 11
> "language"
> 
> FASTEXPR"
> IVisualization":
> false
> }
> regular":
> "group_neutralize ( rank (ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry )
> Ivariant":
> "FASTI


设置好回测配置 & 文件输入输出的路径之后，即可生成可直接在 WQB 回测的 JSON。即可批量回测七十二变输出的变体了。

以下是实现代码

```
import jsondef convert_expressions(input_file, output_file, custom_settings):try:withopen(input_file, 'r') asf:expressions=json.load(f)output_data= []forexprinexpressions:alpha_object= {"type": "REGULAR","settings": custom_settings,"regular": expr}output_data.append(alpha_object)withopen(output_file, 'w') asf:json.dump(output_data, f, indent=2)print(f"Successfully converted {len(expressions)} expressions.")print(f"Output saved to '{output_file}'")exceptFileNotFoundError:print(f"Error: Input file not found at '{input_file}'")exceptjson.JSONDecodeError:print(f"Error: Could not decode JSON from '{input_file}'")exceptExceptionase:print(f"An unexpected error occurred: {e}")if __name__ == "__main__":# --- 请在这里自定义参数 ---# --- 以下为示例参数 ---default_settings= {"instrumentType": "EQUITY","region": "IND","universe": "TOP500","delay": 1,"decay": 5,"neutralization": "FAST","truncation": 0.08,"pasteurization": "ON","testPeriod": "P0Y0M","unitHandling": "VERIFY","nanHandling": "OFF","language": "FASTEXPR","visualization": False}INPUT_JSON_PATH='七十二变/输出/文件.json'OUTPUT_JSON_PATH='加上回测配置/文件/的输出路径.json'convert_expressions(INPUT_JSON_PATH, OUTPUT_JSON_PATH, default_settings)
```

---

### 帖子 #36: 【YZ工程优化系列】YZ72256-使用API自动完成submit
- **主帖链接**: [L2] 【YZ工程优化系列】YZ72256-使用API自动完成submit.md
- **讨论数**: 1

针对由于系统bug、某地区或某时间段扎堆submit、同时check的人数太多导致submit经常超时的情况，推荐 **使用api进行alpha的提交** 。如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

首先先定义一个submit函数对一个alpha进行submit提交，返回提交的结果result。本函数 **感谢ZZ13271老虎哥** 在研究小组群中的api接口代码提供，我只是在其基础上进行了再次加工。

```
def submit(s, alpha_id):    try:        result =s.post(f"[链接已屏蔽])    except:        print('重新登陆')        s = login()        result =s.post(f"[链接已屏蔽])    while True:        if "retry-after" in result.headers:            print(f'{alpha_id} submiting {datetime.now()}')            sleep(120)            time.sleep(float(result.headers["Retry-After"]))            try:                result = s.get(f"[链接已屏蔽])            except:                print('重新登陆')                s = login()        else:            break    return result
```

接着针对多个alpha以及alpha提交失败或超时等多个情况进行处理和异常输出。

```
def submit_alpha(alphaid_list):    s = login()    for alphaid in alphaid_list:        count = 1        while True:            print(f"开始第 {count} 次提交 {alphaid}")            res = submit(s, alphaid)            if res.text:                try:                    res = res.json()                    break                except:                    print('当前有submit任务正在进行中，sleeping 2 min')                    sleep(120)            else:                print(f"第 {count} 次提交超时")                count += 1        # 若是输入alphaid错误        if 'detail' in res and res['detail'] == 'Not found.':            print(f"{alphaid} 错误")            continue               # 检查submit情况        submitted = True        for item in res['is']['checks']:            if item['name'] == 'ALREADY_SUBMITTED':                submitted = False                print(f"{alphaid} 已经提交过了")                break            if item['result'] == 'FAIL':                submitted = False                print(f"{alphaid} 的 {item['name']} 检查不通过, limit = {item['limit']} , value = {item['value']}")                break        if submitted:            print(f'{alphaid}提交成功')
```

上述代码我使用了四种情况进行检验，第一则为错误的alpha id，第二是不用check就存在fail的alpha，第三是已经提交了的alpha，第四是corr错误的alpha，第五则是正常提交的alpha。

```
alphaid_list = ['1234567', 'M7vxRkr', 'pj2aoNq', 'O7daGpd', 'vj7Eowa']submit_alpha(alphaid_list)
```

最终运行结果如下：


> [!NOTE] [图片 OCR 识别内容]
> aIphaid_Iist
> ['1234567
> N7XRkr
> 0j2a0119
> 07daGpd
> VjTEOIa
> submit_alpha (alphaid_list l
> [33]
> 3-11-3.35
> b'{"User
> {"id"
> 1272256"}」
> tokzn'
> {"expiny
> 14438.3},
> Dermissions
> COIISULTAIIT
> 开始第
> 次提交
> 1234557
> 1234557
> 错误
> 开始第
> 次提交
> N7VXRkr
> ITVRkr
> LADDER SHARPE
> 捡查不通过,
> limit
> 1.53
> ValUe
> 3.5
> 开始第
> 次提交
> PjzaoNq
> PJzaoNq 已经提交过
> 开始第
> 次提交
> 074aG30
> 07JaGpd submizing
> 2325-
> 01-15
> 21:02:20
> 505324
> 07daGpd submiting 2025-O1-I5  21:04:22.812891
> O7daGpd submiting
> 2825-81-15
> 21:86:25.113949
> 07daGpd submiting 2025-01-15
> 21:98:27.297258
> 07daGpd submiting
> 2025-81-15  21;10:33
> 994252
> 次提交超时
> 开始第
> 次提交
> 07J2G30
> 07JaGpC
> submizing 2025-01-15  21:12:36.839294
> 07daGpd submiting
> 2325-
> 01-15
> 21:14:39
> 370928
> 07daGpd 的 PROD_CORRELATION 捡查不通过
> Iimit
> 07
> Va_UE
> 0.7293
> 开始第
> 次提交
> Vj7EOWa
> VjEOwa submiting 2025-01-15  21:16:42.030661
> VJTEOwa submiting 2025-81-15
> 21:18:44.247943
> VjEOwa submiting 2025-0I-15  21:20:46.512882
> VJTEOwa submiting
> 2825-81-15
> 21:22:48
> 579339
> VjEOwa submiting 2025-0I-I5  21:24:50.878326
> 次提交超时
> VJTEOwa submiting 2025-81-15
> 21:3:32
> 948596
> 2 次提三
> 超时
> 开始第
> 次提交
> Vj7EOWa
> VjTEOwa
> 经提交过
> OupUT is truncated; Vew Os
> Scrolloble element Oropen i
> ttedto Adjust cell output Settings:


耗时38分钟，前面三种都是秒过的，后边两种由于需要check出fail因此基本都是耗时近20分钟，经两次submit之后才完成，其中提交的那个因子并没有直接返回提交成功，而是在重新submit之后返回它已经是已提交状态了。

最后祝大家每天因子多多，base多多，value up up。我是YZ72256，如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

---

### 帖子 #37: 【YZ工程优化系列】YZ72256-使用API自动完成submit
- **主帖链接**: https://support.worldquantbrain.com[L2] 【YZ工程优化系列】YZ72256-使用API自动完成submit_29242440942359.md
- **讨论数**: 1

针对由于系统bug、某地区或某时间段扎堆submit、同时check的人数太多导致submit经常超时的情况，推荐 **使用api进行alpha的提交** 。如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

首先先定义一个submit函数对一个alpha进行submit提交，返回提交的结果result。本函数 **感谢ZZ13271老虎哥** 在研究小组群中的api接口代码提供，我只是在其基础上进行了再次加工。

```
def submit(s, alpha_id):    try:        result =s.post(f"[链接已屏蔽])    except:        print('重新登陆')        s = login()        result =s.post(f"[链接已屏蔽])    while True:        if "retry-after" in result.headers:            print(f'{alpha_id} submiting {datetime.now()}')            sleep(120)            time.sleep(float(result.headers["Retry-After"]))            try:                result = s.get(f"[链接已屏蔽])            except:                print('重新登陆')                s = login()        else:            break    return result
```

接着针对多个alpha以及alpha提交失败或超时等多个情况进行处理和异常输出。

```
def submit_alpha(alphaid_list):    s = login()    for alphaid in alphaid_list:        count = 1        while True:            print(f"开始第 {count} 次提交 {alphaid}")            res = submit(s, alphaid)            if res.text:                try:                    res = res.json()                    break                except:                    print('当前有submit任务正在进行中，sleeping 2 min')                    sleep(120)            else:                print(f"第 {count} 次提交超时")                count += 1        # 若是输入alphaid错误        if 'detail' in res and res['detail'] == 'Not found.':            print(f"{alphaid} 错误")            continue               # 检查submit情况        submitted = True        for item in res['is']['checks']:            if item['name'] == 'ALREADY_SUBMITTED':                submitted = False                print(f"{alphaid} 已经提交过了")                break            if item['result'] == 'FAIL':                submitted = False                print(f"{alphaid} 的 {item['name']} 检查不通过, limit = {item['limit']} , value = {item['value']}")                break        if submitted:            print(f'{alphaid}提交成功')
```

上述代码我使用了四种情况进行检验，第一则为错误的alpha id，第二是不用check就存在fail的alpha，第三是已经提交了的alpha，第四是corr错误的alpha，第五则是正常提交的alpha。

```
alphaid_list = ['1234567', 'M7vxRkr', 'pj2aoNq', 'O7daGpd', 'vj7Eowa']submit_alpha(alphaid_list)
```

最终运行结果如下：


> [!NOTE] [图片 OCR 识别内容]
> aIphaid_Iist
> ['1234567
> N7XRkr
> 0j2a0119
> 07daGpd
> VjTEOIa
> submit_alpha (alphaid_list l
> [33]
> 3-11-3.35
> b'{"User
> {"id"
> 1272256"}」
> tokzn'
> {"expiny
> 14438.3},
> Dermissions
> COIISULTAIIT
> 开始第
> 次提交
> 1234557
> 1234557
> 错误
> 开始第
> 次提交
> N7VXRkr
> ITVRkr
> LADDER SHARPE
> 捡查不通过,
> limit
> 1.53
> ValUe
> 3.5
> 开始第
> 次提交
> PjzaoNq
> PJzaoNq 已经提交过
> 开始第
> 次提交
> 074aG30
> 07JaGpd submizing
> 2325-
> 01-15
> 21:02:20
> 505324
> 07daGpd submiting 2025-O1-I5  21:04:22.812891
> O7daGpd submiting
> 2825-81-15
> 21:86:25.113949
> 07daGpd submiting 2025-01-15
> 21:98:27.297258
> 07daGpd submiting
> 2025-81-15  21;10:33
> 994252
> 次提交超时
> 开始第
> 次提交
> 07J2G30
> 07JaGpC
> submizing 2025-01-15  21:12:36.839294
> 07daGpd submiting
> 2325-
> 01-15
> 21:14:39
> 370928
> 07daGpd 的 PROD_CORRELATION 捡查不通过
> Iimit
> 07
> Va_UE
> 0.7293
> 开始第
> 次提交
> Vj7EOWa
> VjEOwa submiting 2025-01-15  21:16:42.030661
> VJTEOwa submiting 2025-81-15
> 21:18:44.247943
> VjEOwa submiting 2025-0I-15  21:20:46.512882
> VJTEOwa submiting
> 2825-81-15
> 21:22:48
> 579339
> VjEOwa submiting 2025-0I-I5  21:24:50.878326
> 次提交超时
> VJTEOwa submiting 2025-81-15
> 21:3:32
> 948596
> 2 次提三
> 超时
> 开始第
> 次提交
> Vj7EOWa
> VjTEOwa
> 经提交过
> OupUT is truncated; Vew Os
> Scrolloble element Oropen i
> ttedto Adjust cell output Settings:


耗时38分钟，前面三种都是秒过的，后边两种由于需要check出fail因此基本都是耗时近20分钟，经两次submit之后才完成，其中提交的那个因子并没有直接返回提交成功，而是在重新submit之后返回它已经是已提交状态了。

最后祝大家每天因子多多，base多多，value up up。我是YZ72256，如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

---

### 帖子 #38: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享_36617664667159.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo](../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo)
> 结合我最近参加的新顾问培课程中关于如何利用MCP来开发、优化alpha等内容，发表我的经验，顺便谈点感想。

作为新顾问的一份子，尤其代表零编程基础和零金融学基础的双小白，刚入门的我，只能靠模仿论坛中各位大佬，用他们现有的代码，跑论坛中现有的模板，虽然是“抄作业”，但我觉得完全不丢人，因为我相信没有谁与生俱来就拥有这能力，都是从模仿开始。于是我便靠着现有资源（三阶模板）每天碰碰运气，这样做的结果是一天有一天没，两天打渔三天晒网，不是跑不出来，而是跑出来的相关性太高。特别是11月开始深挖IND地区的时候，断粮了...


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Regular
> Regular
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
> 儿52079 (Me)
> 0,00
> 0.50
> 0,37
> 0.19
> 0,00
> 0,00
> Tot
> policable
> Mainlar
> Super
> Super
> Super



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 转为正式顾问


直到11月8日，参加了新顾问的线上培训，课程上老师分享了很多能提高效率的工具和方法，其中包括了如何用MCP开发alpha模板，如何用app来实现全流程自动化。又恰逢IND地区开放，于是我决定，为了提升我的研究能力，接下来一段时间专注于IND地区的alpha开发（尽管不建议新手跑IND），当然我的方法也从开始的三阶代码换成了MCP和APP工具。

经过小半个月在IND地区的实践，发现挖出来的alpha老是出现几种问题，总结如下：

- 现有模板跑出来的相关性过高，shi都吃不上一口热的；
- 相关性低的，非常容易出现“Robust universe Sharpe of  **XX**  is below cutoff of  **X** .”
- 其他常见问题。

在拜读了大量论坛经验帖子后，决定将相关性太高的alpha直接放弃，于是乎突破点就集中在了如何解决Robust universe Sharpe过低上面，这里要特别感谢ZX12447大佬的分享，让我有了灵感，再结合MCP的智慧，创建了一个专门用于优化Robust universe Sharpe的工作流。基于该工作流，我成功优化几个alpha，解决了Robust universe Sharpe不达标的问题。

优化前问题：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> OOOK
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
> Pnl
> Inyestability Constrained Pnl
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 05
> 9PASS
> Sharoe oT 3.25
> abOVe CUOffcf 1.58
> Finess of 3.11 isabove Cutoffof 1.
> Turnover of 15,60%
> abore CUtof of 196,
> Turpoverof 15.60%
> below CUOffof 4096.
> INeisht is WelI distribu-ed oerinstruments
> Sub-universe Sharpe CT 1.4isaboire Cutoff ot 0.96.
> 2year Sharpe Of 2.58 is
> bore Cutoff of 1.58,
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier oT -
> Effective Pyramid coun-for Genius is
> These -hemes mazch with the followinE multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The finalthEME Multiplizris 2
> 1FAIL
> Robust universe Sharpe Of 0.98
> below CUTOfOf1.
> 4PENDING
 优化后效果：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> TOM
> 5OOOK
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
> Pnl
> Inyestability Constrained
> Pn
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10PASS
> Sharpe OT 3.21
> aboVe cUOff of
> Fizness of 3,01isaboire Cutoff of -
> Turnoverof 18.2896
> aboie CUtoTf 196
> Turnover of 18.28%
> below CUOff of 40%
> Weisht is WEIl distrbuzed overinstruments。
> Sub-universe Sharpe
> 1.43
> bove Cutof of 0.95,
> Robust uniers=
> Of 1.01
> abore Cutoff ot
> 2year Sharpe Of 2.15 is above CutOff of 一
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier or
> Effectiye Pyramid Counzfor Genius
> These themes mazch with the followine multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The final theme multiplieris 2
> PENDING
> Shrpe


虽然这个alpha最终因相关性过高而未被提交，但是这是我用工作流成功优化的第一个alpha，所以将它作为代表案例展示出来。任务完成后，我让MCP将本次优化过程总结成了工作流，并且每次基于该工作流成功优化后将案例添加进工作流中。


> [!NOTE] [图片 OCR 识别内容]
> 9
> 你说
> 很好请将本次对话总结为优化robust的工作流
> API请求
> 50.0054
> Roo 说
> 我来为您创建
> 完整的IN0地区Robust universe Sharpe优化工作流文档。
> 检查点
> [
> 需要新建文件
> IND_Robust_Sharpe_优化工作流 .md
> +212
> -0巴
> 二
> API请求
> 50.0033
> 任务完咸


从这以后（11月23日），我竟然恢复了口粮，并且开始提交纯ra（之前都是ppa），今天（27日）提交了3个ra，所以借用论坛一位大佬的话“ *要重视你生产的每一个alpha* ”，因为它可能就是你下一个成功提交的对象。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod
> IESTI
> Correlation
> Correlation
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.6> 1
> e.6> 1
> e6>1
> SeeC
> e.6 >
> e.6 >
> anonymOUs
> Reaular
> ACTTVE
> 11/2712025 EST
> IND
> TOPSOO
> 0.58
> 0.61
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> 0.30
> 0.68
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> ReadyToSubmit
> 0.14
> 0.66
> anonymoUs
> Regular
> ACTIVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.41
> 0.49
> anonymOUs
> Reaular
> ACTTVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.13
> 0.70
> anonymoUs
> Reaular
> ACTTVE
> 11/25/2025 EST
> IND
> TOPSOO
> O.00
> 0.65
> anonymOUs
> Reaular
> ACTTVE
> 11/23/2025 EST
> IND
> TOPSOO
> 0.02
> 0.68
> anonymoUs
> ACTTVE
> 11/02/2025 EST
> IND
> TOPSOO
> O.00
> 0.17
> Reaular


最后送给诸君一句话并附上工作流：
 **The journey of a thousand miles begins with one step. JUST DO IT.**

```
# IND地区Robust Universe Sharpe优化工作流## 问题背景在IND地区alpha开发中，经常遇到**Robust universe Sharpe略低于1.0**的问题，导致无法提交。本工作流基于社区经验和实际案例，提供系统化的解决方案。## 工作流概览```mermaidgraph TD    A[诊断问题] --> B{分析差距}    B -->|差距<0.1| C[轻度优化]    B -->|差距>0.1| D[重度优化]    C --> E[时间参数调整]    C --> F[运算符优化]    D --> G[结构重构]    E --> H[测试验证]    F --> H    G --> H    H --> I{是否达标}    I -->|是| J[提交准备]    I -->|否| C```## 诊断阶段### 1. 问题识别```python# 检查Robust universe Sharpe指标LOW_ROBUST_UNIVERSE_SHARPE:  - result: FAIL  - limit: 1.0  - value: 0.98  # 差距0.02```### 2. 差距分析- **轻度问题**: 差距 < 0.1 (推荐本工作流)- **重度问题**: 差距 > 0.1 (建议重构alpha逻辑)## 优化工具箱### 核心优化方法#### 1. 时间参数调整 (最有效)```python# 原始ts_backfill(x, 60) → ts_backfill(x, 75)group_backfill(x, sector, 120) → group_backfill(x, sector, 275)# 推荐参数范围- ts_backfill: 60 → 75, 90, 120- group_backfill: 120 → 180, 252, 275```#### 2. 运算符增强```python# 添加稳定性运算符group_zscore(x, sector)        # 标准化信号ts_scale(x, 0.5)               # 时间序列缩放signed_power(x, 0.6)           # 符号幂变换```#### 3. 中性化优化```python# 尝试不同中性化组合group_neutralize(x, industry)group_neutralize(x, sector)group_neutralize(x, subindustry)group_neutralize(x, market)  # 对模型数据类Alpha特别有效```**中性化策略选择指南**：- **模型数据类Alpha**：优先尝试MARKET中性化- **基本面数据类Alpha**：优先尝试SECTOR/INDUSTRY中性化- **技术指标类Alpha**：根据数据特性选择合适的中性化层级#### 4. 截尾处理优化```python# 调整winsorize参数winsorize(x, std=4) → winsorize(x, std=3)winsorize(x, std=4) → winsorize(x, std=5)```## 实战案例### 案例1：IND地区imb5_score优化**原始alpha (FAIL)**```pythonfilled_score = ts_backfill(imb5_score, 60);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);signed_alpha = signed_power(neutralized, 0.5);final_alpha = group_backfill(signed_alpha,sector,120,std=4);final_alpha```- Robust Sharpe: 0.98 (FAIL)**优化版本1 (PASS)**```python3```- Robust Sharpe: 1.02 (PASS)**优化版本2 (简化版)**```pythonfilled_score = ts_backfill(imb5_score, 75);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);final_alpha = group_backfill(neutralized,sector,275,std=4);final_alpha```- Robust Sharpe: 1.01 (PASS)### 案例2：IND地区score_analyst_estimate_revisions优化（中性化策略优化）**原始alpha (FAIL)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 138), std=0.92), 108), 0.8), densify(sector))```- Robust Sharpe: 0.99 (FAIL)- 数据字段：score_analyst_estimate_revisions (覆盖率86.45%，金字塔乘数1.6)**优化版本 (PASS)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 150), std=0.85), 120), 0.8), densify(market))```- **关键优化**：中性化从SECTOR改为MARKET- **参数调整**：ts_backfill(138→150), ts_zscore(108→120), winsorize(std=0.92→0.85)- **性能提升**：  - Robust Sharpe: 0.99 → 1.11 (+12.1%)  - PnL: 11,095,177 → 12,997,115 (+17.1%)  - Sharpe: 2.56 → 2.62 (+2.3%)  - Fitness: 2.06 → 2.51 (+21.8%)  - 周转率: 16.63% → 13.66% (-17.9%)**核心洞察**：对于IND地区的模型数据类Alpha，MARKET中性化配合适当的时间窗口调整能有效提升Robust Sharpe表现，同时改善整体性能指标。## 系统化优化流程### 步骤1：基础诊断1. 运行原始alpha获取基准数据2. 记录所有检查项结果3. 重点关注Robust universe Sharpe差距### 步骤2：轻度优化 (差距<0.1)```python# 第一轮：时间参数调整尝试组合：- ts_backfill(60→75), group_backfill(120→275)- ts_backfill(60→90), group_backfill(120→252)- ts_backfill(60→120), group_backfill(120→180)```### 步骤3：运算符增强```python# 第二轮：添加稳定性运算符在group_neutralize后添加：- group_zscore(x, sector)- ts_scale(x, 0.5)- signed_power(x, 0.6)```### 步骤4：参数微调```python# 第三轮：参数优化调整：- winsorize std参数 (3,4,5)- signed_power指数 (0.5,0.6,0.7)- decay值 (0,5,20)```### 步骤5：验证与选择1. 比较所有优化版本的性能2. 选择运算符最少的版本3. 确保其他指标不受影响## 避免过拟合原则### 运算符数量控制- **理想**: 3-5个运算符- **可接受**: 6-8个运算符  - **风险**: >8个运算符### 经济意义保持- 每次优化应有合理的金融解释- 避免单纯为了提升指标而堆砌运算符- 保持alpha逻辑的简洁性和可解释性## IND地区特殊注意事项### 数据特性- Universe: 仅支持TOP500- 中性化选项有限- 数据字段相对较少### 优化策略1. **优先时间参数调整** - 对IND地区最有效2. **谨慎使用复杂运算符** - 避免过拟合3. **关注数据质量** - IND地区数据相对稀疏## 成功指标### 主要目标- ✅ Robust universe Sharpe ≥ 1.0- ✅ 其他检查项全部PASS- ✅ 运算符数量控制在合理范围### 次要目标  - 📈 IS Sharpe保持或提升- 💰 PnL表现稳定- 🔄 Turnover在合理范围内## 工具与资源### BRAIN平台工具- `get_platform_setting_options()` - 获取有效设置- `create_simulation()` - 测试优化版本- `get_alpha_details()` - 分析详细结果### 社区经验- **group_backfill/ts_backfill** - 时间参数调整最有效- **group_zscore** - 增强信号稳定性- **winsorize** - 处理异常值- **避免过度复杂化** - 保持alpha简洁## 总结本工作流通过**系统化的诊断→优化→验证**流程，有效解决IND地区Robust universe Sharpe问题。基于成功案例经验，关键优化策略包括：1. **精准诊断** - 明确问题差距和数据类型2. **中性化策略优化** - 根据数据类型选择合适的中性化层级3. **时间参数调整** - 适当延长时间窗口增强稳定性4. **避免过拟合** - 保持alpha逻辑简洁性和经济意义### 成功案例验证**score_analyst_estimate_revisions优化案例**证明了：- **MARKET中性化**对模型数据类Alpha效果显著- **参数微调**能同时提升多个性能指标- **整体性能提升**：Robust Sharpe +12.1%，PnL +17.1%，Fitness +21.8%通过这个方法，可以将接近达标的alpha（如0.98-0.99）成功优化到合格水平（≥1.0），同时显著提升整体性能表现。
```

---

### 帖子 #39: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #40: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #41: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第十季.md
- **讨论数**: 583

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第九季.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #42: 【日常生活贴】我的量化日记第十季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #43: print('retrying in', result.headers["retry-after"], 'seconds')
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md
- **讨论数**: 8

### 一.原有痛点

1.网页端速度慢,灵活性差,字段不全或不可自定义(比如看最后两年sharpe或low_2_year_shape等),不便筛选

2.一二三阶段那种跑批同时进行的时候,最好打tag,api打tag影响回测速率

3.alpha之间互相对比困难,例如来自相同核心field的筛选问题

### 二.解决方案

使用数据库,本方案采用的结构化数据库MySQL,也有同学使用的Mongo等非结构化的,这个我抛砖引玉,欢迎讨论

我这边独特的字段如下

1.tags,自己打标签.multi_simulate的时候,可以获取到progress_urls,把这些url和应该打的标签在代码中存起来推到redis中,另起一个任务专门负责根据这些url获取其alpha的id,进而和tag建立关系,再转存到MySQL中

2.check_status.接口获取信息到的check信息中,存在fail的,这个字段就为fail,否则就是pending,只有pending的alpha才需要后面check

3.low_2y_sharpe.这个字段是single的dataset独有,能获取到就赋值,获取不到就补1.不是补0,因为为0的需要将check_status变为fail

4.is_ladder_sharpe,不是single的dataset,则有这个字段,同样的,能获取到就赋值,获取不到就补1.不是补0,因为为0的需要将check_status变为fail

5.is_submit.记录是否提交的信息.0未提交,1已提交.值得注意的是,这个字段还能解决如何科学存货.按自己的提交标准,check完以后把is_submit字段赋值为2-10之间的数值.比如我,2为优秀10为垃圾,中间酌情.

### 三.核心代码

api代码在下一条评论,这里似乎放不下

MySQL表结构如下:

-- worldquant.alpha_data definition

CREATE TABLE `alpha_data` (

`id` varchar(10) NOT NULL DEFAULT '',

`exp` varchar(2000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,

`original_field` varchar(100) DEFAULT NULL,

`dateCreated` datetime DEFAULT NULL,

`region` varchar(10) DEFAULT NULL,

`universe` varchar(50) DEFAULT NULL,

`sharpe` float DEFAULT NULL,

`fitness` float DEFAULT NULL,

`turnover` float DEFAULT NULL,

`longCount` int DEFAULT NULL,

`shortCount` int DEFAULT NULL,

`returns` float DEFAULT NULL,

`drawdown` float DEFAULT NULL,

`margin` float DEFAULT NULL,

`delay` int DEFAULT NULL,

`decay` int DEFAULT NULL,

`neutralization` varchar(20) DEFAULT NULL,

`truncation` float DEFAULT NULL,

`pasteurization` varchar(10) DEFAULT NULL,

`unitHandling` varchar(10) DEFAULT NULL,

`visualization` varchar(10) DEFAULT NULL,

`tags` varchar(100) DEFAULT NULL,

`check_status` varchar(20) DEFAULT NULL,

`is_submit` tinyint DEFAULT NULL,

`low_2y_sharpe` float DEFAULT NULL,

`is_ladder_sharpe` float DEFAULT NULL,

PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

ARSET=utf8mb3;

---

### 帖子 #44: 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回_28969108137623.md
- **讨论数**: 3

## 一.Redis简单介绍

Redis（Remote Dictionary Server）是一个开源的高性能键值存储系统。它支持多种数据结构，如字符串（Strings）、列表（Lists）、集合（Sets）、有序集合（Sorted Sets）、哈希表（Hashes）等。Redis不仅支持简单的键值对存储，还提供了丰富的操作接口，使其在各种应用场景中都能发挥重要作用。

笔者使用的主要是Lists,实现先入先出构建回测池(lpush),先入后出实现插队(rpush)

撤回功能可通过推送过去的json队列的时候加上一些标签信息,然后写专门的读取小功能实现撤回(笔者暂未有空实现)

## 二.具体场景和实现

### 2.1 redis安装

结合第一篇 [[L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md]([L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md)

需要安装mysql和redis,为了简易安装,我使用了宝塔面板(这就不过多介绍了)

### 2.2 推送任务范例

```
total_results = []with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:    with conn.cursor() as cursor:        for dataset_id in dataset_ids:            sql = ("select t.field,t.type "                    f"from worldquant.{region}_DELAY1 t "                    f"where t.datasets = '{dataset_id}' "                    f"order by t.alphaCount desc "                    "limit 2000 "                    "OFFSET 0"                )            cursor.execute(sql)            results = cursor.fetchall()            total_results.extend(results)# 上面是mysql获取字段和字段类型(这意味着我已经提前把datasets信息搬回来自己的库了)
```

```
pc_fields = []for result in total_results:    if result[1] == 'MATRIX':         # 这里写自己的代码模板    elif result[1] == 'VECTOR':        for item in get_vec_fields([result[0]]):        # 这里写自己的代码模板            first_order = first_order_factory(pc_fields, ts_ops)    so_alpha_list = []for exp in first_order:    so_alpha_list.append([exp, 6])
```

```
r = redis.StrictRedis(host='host', port=6379, password='......', db=0, decode_responses=True)end_info = {    'task_type': 'end',    'task_name': 'news18,79,50一级'}# r.rpush("alpha_pools", json.dumps(end_info))for i in range(0, len(so_alpha_list), 100):    pool = {        "settings": settings,        "alpha_list": so_alpha_list[i:i+100],    }    r.lpush("alpha_pools", json.dumps(pool))r.lpush("alpha_pools", json.dumps(end_info))
```

可以看到,①字段也是本地采集好的②每次推出去的任务都可以改模板,也就是生产alpha表达式和回测任务是解耦的③end_info 等间歇的信息作用,是可以在回测的时候,当读取到这个信息的时候代表任务结束,可以进行自己的通知提醒(笔者采用的阿里云的短信提醒,不贵.有小伙伴用的免费的邮件提醒)

---

### 帖子 #45: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
- **主帖链接**: [L2] 【构建自己的代码框架系列】第03篇--除了自己的alpha信息你到底在MySQL需要存哪些数据暨API代码分享.md
- **讨论数**: 2

## 往期回顾

- [【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha](../顾问 SD17531 (Rank 15)/[Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha.md)
- [【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回](../顾问 PN39025 (Rank 87)/[Commented] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回.md)

## 一.所有的dataset信息

注意一定要爬取description,因为后续可以把这个字段喂给大模型

表结构:

-- worldquant.data_sets definition

CREATE TABLE `data_sets` (
  `data_set_id` varchar(100) NOT NULL,
  `delay` tinyint NOT NULL DEFAULT '1',
  `region` varchar(100) NOT NULL,
  `universe` varchar(100) NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `description` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description_cn` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `pyramid_multiplier` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `user_count` int DEFAULT NULL,
  `value_score` tinyint DEFAULT NULL,
  `alpha_count` int DEFAULT NULL,
  `field_count` int DEFAULT NULL,
  `score` tinyint DEFAULT NULL,
  PRIMARY KEY (`data_set_id`,`delay`,`region`,`universe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='所有的数据集信息,关注中文描述';

api:

```
def get_data_sets(s, region, delay, universe):    """    获取所有的data_sets信息写入MySQL    :param s: requests.session()    :param region: region    :param delay: delay    :param universe: universe    :return: data_sets_list,每个data_set是一个dict,包含data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&limit=20"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    data_sets_list = []    for x in range(0, count, 20):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            data_sets_list.append(                {                    'data_set_id': result['id'],                    'category_id': result['category']['id'],                    'description': result['description'],                    'name': result['name'],                    'pyramid_multiplier': result['pyramidMultiplier'],                    'coverage': result['coverage'],                    'user_count': result['userCount'],                    'value_score': result['valueScore'],                    'alpha_count': result['alphaCount'],                    'field_count': result['fieldCount'],                }            )        time.sleep(4)    return data_sets_list
```

```
if __name__ == "__main__":    s = login()    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        data_sets = get_data_sets(s, region, delay, universe)        with conn.cursor() as cursor:            for data_set in data_sets:                sql = (                    f"insert into worldquant.data_sets(region,delay,universe,data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                    "on duplicate key update category_id=%s,description=%s,name=%s,pyramid_multiplier=%s,coverage=%s,user_count=%s,value_score=%s,alpha_count=%s,field_count=%s"                )                sql_params = (                    region, delay, universe, data_set['data_set_id'], data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count'],                    data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count']                )                cursor.execute(sql, sql_params)        conn.commit()
```

## 二.分地区的field信息

这个所有地区可以合并在一个表格,但是我还没改,暂时按不同地区不同delay分表的
表结构:

-- worldquant.hkg_delay1 definition

CREATE TABLE `hkg_delay1` (
  `field` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `delay` char(1) DEFAULT NULL,
  `universe` varchar(100) DEFAULT NULL,
  `datasets` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `userCount` int DEFAULT NULL,
  `alphaCount` int DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

api:

```
def get_fields(s, dataset_id, region, delay, universe):    """    给定data_sets的id,以及参数region,delay,universe,返回符合条件的data_sets里面的fields    :param s: requests.session()    :param dataset_id: data_sets的id    :param region: region    :param delay: delay    :param universe: universe    :return: fields,每个field是一个dict,包含field_type和field_id    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    datafields_list = []    for x in range(0, count, 50):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            field_type = result['type']            field_id = result['id']            description = result['description']            coverage = result['coverage']            userCount = result['userCount']            alphaCount = result['alphaCount']            datafields_list.append({'field_type': field_type, 'field_id': field_id, 'description': description,'coverage': coverage, 'userCount': userCount, 'alphaCount': alphaCount})    return datafields_list
```

```
if __name__ == "__main__":    s = login()    dataset_ids = [        'other128',        'other16',    ]    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        for dataset_id in dataset_ids:            fields = get_fields(s, dataset_id, region, delay, universe)            with conn.cursor() as cursor:                for item in fields:                    sql = (                        f"insert into worldquant.{region}_DELAY1(field,description,region,delay,universe,datasets,type,coverage,userCount,alphaCount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                        "on duplicate key update description=%s,region=%s,delay=%s,universe=%s,datasets=%s,type=%s,coverage=%s,userCount=%s,alphaCount=%s"                    )                    sql_params = (                        item['field_id'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount']                    )                    cursor.execute(sql, sql_params)            conn.commit()
```

---

### 帖子 #46: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第03篇--除了自己的alpha信息你到底在MySQL需要存哪些数据暨API代码分享_29022968451223.md
- **讨论数**: 2

## 往期回顾

- [【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha]([L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md)
- [【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回]([L2] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回_28969108137623.md)

## 一.所有的dataset信息

注意一定要爬取description,因为后续可以把这个字段喂给大模型

表结构:

-- worldquant.data_sets definition

CREATE TABLE `data_sets` (
  `data_set_id` varchar(100) NOT NULL,
  `delay` tinyint NOT NULL DEFAULT '1',
  `region` varchar(100) NOT NULL,
  `universe` varchar(100) NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `description` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description_cn` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `pyramid_multiplier` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `user_count` int DEFAULT NULL,
  `value_score` tinyint DEFAULT NULL,
  `alpha_count` int DEFAULT NULL,
  `field_count` int DEFAULT NULL,
  `score` tinyint DEFAULT NULL,
  PRIMARY KEY (`data_set_id`,`delay`,`region`,`universe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='所有的数据集信息,关注中文描述';

api:

```
def get_data_sets(s, region, delay, universe):    """    获取所有的data_sets信息写入MySQL    :param s: requests.session()    :param region: region    :param delay: delay    :param universe: universe    :return: data_sets_list,每个data_set是一个dict,包含data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&limit=20"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    data_sets_list = []    for x in range(0, count, 20):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            data_sets_list.append(                {                    'data_set_id': result['id'],                    'category_id': result['category']['id'],                    'description': result['description'],                    'name': result['name'],                    'pyramid_multiplier': result['pyramidMultiplier'],                    'coverage': result['coverage'],                    'user_count': result['userCount'],                    'value_score': result['valueScore'],                    'alpha_count': result['alphaCount'],                    'field_count': result['fieldCount'],                }            )        time.sleep(4)    return data_sets_list
```

```
if __name__ == "__main__":    s = login()    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        data_sets = get_data_sets(s, region, delay, universe)        with conn.cursor() as cursor:            for data_set in data_sets:                sql = (                    f"insert into worldquant.data_sets(region,delay,universe,data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                    "on duplicate key update category_id=%s,description=%s,name=%s,pyramid_multiplier=%s,coverage=%s,user_count=%s,value_score=%s,alpha_count=%s,field_count=%s"                )                sql_params = (                    region, delay, universe, data_set['data_set_id'], data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count'],                    data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count']                )                cursor.execute(sql, sql_params)        conn.commit()
```

## 二.分地区的field信息

这个所有地区可以合并在一个表格,但是我还没改,暂时按不同地区不同delay分表的
表结构:

-- worldquant.hkg_delay1 definition

CREATE TABLE `hkg_delay1` (
  `field` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `delay` char(1) DEFAULT NULL,
  `universe` varchar(100) DEFAULT NULL,
  `datasets` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `userCount` int DEFAULT NULL,
  `alphaCount` int DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

api:

```
def get_fields(s, dataset_id, region, delay, universe):    """    给定data_sets的id,以及参数region,delay,universe,返回符合条件的data_sets里面的fields    :param s: requests.session()    :param dataset_id: data_sets的id    :param region: region    :param delay: delay    :param universe: universe    :return: fields,每个field是一个dict,包含field_type和field_id    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    datafields_list = []    for x in range(0, count, 50):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            field_type = result['type']            field_id = result['id']            description = result['description']            coverage = result['coverage']            userCount = result['userCount']            alphaCount = result['alphaCount']            datafields_list.append({'field_type': field_type, 'field_id': field_id, 'description': description,'coverage': coverage, 'userCount': userCount, 'alphaCount': alphaCount})    return datafields_list
```

```
if __name__ == "__main__":    s = login()    dataset_ids = [        'other128',        'other16',    ]    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        for dataset_id in dataset_ids:            fields = get_fields(s, dataset_id, region, delay, universe)            with conn.cursor() as cursor:                for item in fields:                    sql = (                        f"insert into worldquant.{region}_DELAY1(field,description,region,delay,universe,datasets,type,coverage,userCount,alphaCount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                        "on duplicate key update description=%s,region=%s,delay=%s,universe=%s,datasets=%s,type=%s,coverage=%s,userCount=%s,alphaCount=%s"                    )                    sql_params = (                        item['field_id'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount']                    )                    cursor.execute(sql, sql_params)            conn.commit()
```

---

### 帖子 #47: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: [L2] 【环境配置】在Nvim中配置MCP的方法经验分享.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #48: 【经验分享】尝试Python alpha经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【经验分享】尝试Python alpha经验分享_40737593669911.md
- **讨论数**: 7

通过阅读官方资料 [Getting Started with Brain Python Alphas | WorldQuant BRAIN]([链接已屏蔽]) 
对python alpha有一定的认知。
主要是装饰器，每个 Alpha 都是一个带有装饰的 Python 函数。装饰器声明要加载哪些数据字段，哪些存储变量要跨时间持久化

```
@alpha(
    data=["returns"],
    store=["my_state"],
)
def my_alpha(data, store) -> npt.NDArray[np.float32]:
    # data.returns — shape [lookback_window, n_instruments], float32
    # data.universe — shape [lookback_window, n_instruments] (always available, int: 1 = in, 0 = out)
    #
    # store.my_state — initialized to None, persists across time steps

    signal = -np.nanmean(data.returns, axis=0)
    return signal.astype(np.float32)
```

from brain.alphas import alpha
import numpy as np
import numpy.typing as npt

def pasteurize(a: npt.NDArray[np.float32], u: npt.NDArray) -> npt.NDArray[np.float32]:
    a = np.where(u == 1, a, np.nan)
    return a

def neutralize_scale(a: npt.NDArray[np.float32]) -> npt.NDArray[np.float32]:
    a = a - np.nanmean(a)
    scale = np.nansum(np.abs(a))
    if scale > 0:
        a = a / scale
    return a

def _ts_zscore(arr: npt.NDArray[np.float64], axis: int = 0) -> npt.NDArray[np.float64]:
    mean = np.nanmean(arr, axis=axis, keepdims=True)
    std = np.nanstd(arr, axis=axis, keepdims=True)
    zscore = (arr[-1:] - mean) / std
    zscore = np.where(std == 0, np.nan, zscore)
    return zscore.squeeze(axis=axis)

def _rank(arr: npt.NDArray) -> npt.NDArray[np.float64]:
    finite = np.where(np.isnan(arr), -np.inf, arr)
    ranks = np.argsort(np.argsort(finite)).astype(np.float64)
    ranks = np.where(np.isnan(arr), np.nan, ranks)
    return ranks

def _scale(arr: npt.NDArray, scale: float = 1.0, longscale: float = 1.0, shortscale: float = 1.0) -> npt.NDArray[np.float32]:
    arr = arr.copy()
    pos_mask = arr > 0
    neg_mask = arr < 0

pos_sum = np.nansum(np.abs(arr[pos_mask]))
    if pos_sum > 0:
        arr[pos_mask] = arr[pos_mask] / pos_sum * longscale * scale

neg_sum = np.nansum(np.abs(arr[neg_mask]))
    if neg_sum > 0:
        arr[neg_mask] = arr[neg_mask] / neg_sum * shortscale * scale

return arr.astype(np.float32)

@alpha(
    data=["industry_broker_concentration_index_2", "industry_broker_concentration_index"],
    store=[],
)
def akor2pxx(data, store) -> npt.NDArray[np.float32]:
    idx2 = data.industry_broker_concentration_index_2
    idx = data.industry_broker_concentration_index

ratio = idx2 / idx

zscore = _ts_zscore(ratio, axis=0)

ranked = _rank(zscore)

signal = -1.0 * _scale(ranked, scale=2, longscale=3, shortscale=1)

signal = pasteurize(signal, data.universe[-1])
    signal = neutralize_scale(signal)

return signal.astype(np.float32)
这个是example

from os.path import expanduser
import json
import requests
import datetime as dt
from time import sleep
import sys

def login():
    with open(expanduser('brain_credentials.txt')) as f:
        credentials = json.load(f)
    username, password = credentials
    s = requests.Session()
    s.auth = (username, password)
    print(username, file=sys.stderr)
    response = s.post(' [[链接已屏蔽]) ')
    print(response.content, file=sys.stderr)
    print(dt.datetime.now(), file=sys.stderr)
    return s

def simulate(s, code, region, universe, delay=1, decay=6, neut='SUBINDUSTRY', truncation=0.08, pasteurization='ON', looback=256):
    simulation_data = {
        'type': 'REGULAR',
        'settings': {
            'instrumentType': 'EQUITY',
            'region': region, 
            'universe': universe, 
            'delay': delay,
            'decay': decay, 
            'neutralization': neut,
            'truncation': truncation,
            'pasteurization': pasteurization,
            'language': 'PYTHON',
            'lookback': looback,
            'visualization': False,
        },
        'regular': code
    }

print("Sending simulation request...", file=sys.stderr)
    simulation_response = s.post(' [[链接已屏蔽]) ', json=simulation_data)
    print("Status:", simulation_response.status_code, file=sys.stderr)
    print("Response:", simulation_response.content, file=sys.stderr)

    if simulation_response.status_code == 201:
        progress = simulation_response.headers.get('Location')
        print("Location:", progress, file=sys.stderr)
        if progress:
            while True:
                simulation_progress = s.get(progress)
                retry_after = simulation_progress.headers.get("Retry-After", 0)
                if retry_after == 0 or retry_after == "0":
                    break
                print("Sleeping for " + str(retry_after) + " seconds", file=sys.stderr)
                sleep(float(retry_after))

            status = simulation_progress.json().get("status", 0)
            print("Status:", status, file=sys.stderr)
            if status == "COMPLETE" or status == "WARNING":
                data = simulation_progress.json()
                print("Simulation complete!")
                print(json.dumps(data, indent=2))
                return data
            else:
                print("Not complete : %s" % progress, file=sys.stderr)
                print(json.dumps(simulation_progress.json(), indent=2), file=sys.stderr)
                return simulation_progress.json()
    else:
        print("Error creating simulation", file=sys.stderr)
        return None

if __name__ == '__main__':
    s = login()
    with open('./alpha_example.py', 'r') as f:
        code = f.read()
    result = simulate(s, code, 'USA', 'TOP3000', delay=0, decay=6, neut='STATISTICAL', truncation=0.08, pasteurization='ON', looback=256)
    if result:
        with open('simulation_result.json', 'w') as f:
            json.dump(result, f, indent=2)
        print("Result saved to simulation_result.json")
这个是回测代码，就可以让AI来生产python alpha

---

### 帖子 #49: 【课代表📕】关于2阶段的改进，字段方向Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【课代表】关于2阶段的改进字段方向Alpha Template_31503981064087.md
- **讨论数**: 8

在这里推荐大家可以加入更多新颖的bucket，这里以split为例

bucket(rank(split), range='0.1, 1, 0.1')


> [!NOTE] [图片 OCR 识别内容]
> Simulate Field
> Field description
> Category: Price Volume
> Price Volume
> Type: Matrix
> Stock split ratio
> Region
> Delay
> Universe
> Pyramid Theme
> Theme
>  Coverage
> Users
> Alphas
> Multiplier
> USA
> TOP3000
> 1.1
> 100%
> 803
> 8309
> Show all settings


“Stock split ratio” 就是 “股票分割比率”

我猜测不同分割比率的股票可能会有相似性，就需要去做组内的中性化。

这是我用这个group做出来的某个因子，三条线都非常稳健，大家可以尝试加入自己的二阶段！


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.61
> 3.659
> 9.76
> 91.349
> 27.059
> 500.019600
> Year
>  Sharpe
> Trnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> .0096
> 00%
> 0.009
> 0.003ooa
> 2014
> 0.0096
> 00%
> 00%
> 0.003oo
> 2015
> 2.39
> 3.3196
> 4.19
> 38.4696
> 8.009
> 232.74360
> 622
> 250
> 2016
> .90
> 2.4396
> 3.05
> 32.1796
> 15.6096
> 264.869600
> 1619
> 282
> 2017
> 0.42
> 2.8696
> 0.28
> ~5.7096
> 14.6096
> 39.82900
> 1758
> 264
> 2018
> 3.20
> 2.7996
> ,35
> 49.2496
> 10.70%6
> 353.
> 33600
> 899
> 318
> 2019
> 2.89
> 3.28%6
> 5.53
> 47.4996
> 10.039
> 289.479600
> 2012
> 241
> 2020
> 0.46
> 3.98%6
> 0.50
> 14.9796
> 31.139
> 75.29300
> 2103
> 194
> 2021
> -7.44
> 3.5496
> 30.34
> 207.92%6
> 8.87%6
> -1,175.77960
> 2179
> 256
> 2021
> 3.22
> 3.9096
> 8.13
> 79.7696
> 16.899
> 409.179600
> 2466
> 328
> 2022
> 5.12
> 3.4096
> 16.03
> 122.51%
> 8.809
> 719.969600
> 2555
> 352
> 2023
> 6.61
> 3.95%
> 32.15
> 295.7196
> 15.3596
> 1,497.829600
> 2344
> 300
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.11
> 3.659
> 5.80
> 43.51%
> 11.92%
> 238.169600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.73
> 2.31%
> 5.98
> 60.02%
> 23.71%
> 520.499600



> [!NOTE] [图片 OCR 识别内容]
> ZON
> 10N
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



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> 1S
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.07
> 3.24%
> 3.88
> 43.93%
> 33.66%
> 271.019600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2013
> 0.00
> 0.00%
> 0.00
> 0,00q
> 0.009
> 0.003oo
> 2014
> 0096
> 0,00q
> 0.009
> 0.003ooa
> 2015
> 2.39
> 3.31%6
> 4.19
> 38.4696
> 8.009
> 232.749o00
> 622
> 250
> 2016
> 1.90
> 2.43%
> 3.05
> 32.1796
> 15.60%
> 264.86900
> 1619
> 282
> 2017
> -0.42
> 2.86%
> -0.28
> -5.7096
> 14.6090
> 39.823600
> 1758
> 264
> 2018
> 3.20
> 2.7996
> 49.2496
> 10.7096
> 353.
> 39o00
> 899
> 318
> 2019
> 2.89
> 3.2896
> 5.63
> 47.49N6
> 10.0396
> 289.479o00
> 2012
> 241
> 2020
> 0.46
> 3.9896
> 0.50
> 14.9796
> 31.1396
> 75.299600
> 2103
> 194
> 2021
> -7.44
> 3.5496
> 30.34
> -207.92%6
> 8.8796
> 1,175.779600
> 2179
> 256
> 2021
> 3.22
> 3.90%
> 8.13
> 79.
> 6%6
> 16.8996
> 409.
> 79oo0
> 2466
> 328
> 2022
> 5.12
> 3.4096
> 16.03
> 122.5196
> 8.809
> 719.96960o
> 2555
> 352
> 2023
> 6.61
> 3.9596
> 32.15
> 295.7196
> 15.3596
> 1,497.829300
> 2344
> 300
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.93
> 3.24%
> 2.69
> 24.20%
> 13.16%
> 149.28900
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawCOwn
> Margin
> 1.73
> 2.16%
> 2.60
> 28.13%
> 34.09%
> 260.289600


---

### 帖子 #50: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
- **主帖链接**: [L2] 代码分享拉取某个category下的全部dataset并实现批量生产数据预处理备战Pyramid.md
- **讨论数**: 5

```
分享代码给所有冲刺Pyramid的同学，分享不易，感谢点赞评论
```

这套代码结合了三阶框架和ACE Library，之前我们在跑单数据集的时候经常会放弃一些小数据集，从而可能错失一些有效的字段。本代码可以批量拉取某个category下的字段，并进行一定的筛选。

- **核心代码：获取全部datasets**

```
def get_datasets(    s,    instrument_type: str = 'EQUITY',    region: str = 'USA',    delay: int = 1,    universe: str = 'TOP3000'):    brain_api_url = "[链接已屏蔽]    url = brain_api_url + "/data-sets?" +\        f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"    result = s.get(url)    datasets_df = pd.DataFrame(result.json()['results'])    return datasets_df
```

- 筛选需要的category和coverage等信息

```
region = "JPN"region_code = "jpn"universe = "TOP1600"delay = 1datasets_df = get_datasets(s,region='JPN',delay=1,universe='TOP1600')pd.set_option('display.max_columns', None)  # 显示所有列pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值# select needed datasetsselected_datasets_df = datasets_df[    (datasets_df["delay"] == delay) &    (datasets_df["coverage"] > 0.5) & (datasets_df["coverage"] <= 1) &    (datasets_df["fieldCount"] > 0) & (datasets_df["fieldCount"] < 2000) &    (datasets_df["region"] == region) &    (datasets_df["universe"] == universe) &    (datasets_df["userCount"] > 0) & (datasets_df["userCount"] < 100) &    (datasets_df["valueScore"] > 1) & (datasets_df["valueScore"] < 10) &    (datasets_df["category"].apply(lambda x: x.get("id") if isinstance(x, dict) else None) == "analyst")    #(datasets_df["category"]  'analyst')    #datasets_df["name"].str.contains('news', case=False) &    #((datasets_df["category"] == 'analyst') | (datasets_df["category"] == 'analyst'))].sort_values(by=['valueScore'], ascending=False)print(selected_datasets_df)
```

- 批量预处理数据，生成数据大表，这里的作用等价于老师在论坛写的推荐数据

```
reset_fleg = 0for dataset_id in selected_datasets_df['id']:    df1 = get_datafields(s, dataset_id = dataset_id, region= region, universe=universe, delay=delay)    pd.set_option('display.max_columns', None)  # 显示所有列    pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值    df2 = df1[df1['type'] == 'MATRIX']    df3 = df1[df1['type'] == 'VECTOR']    #df4 = df1[df1['type'] == 'GROUP']    try:        print(len(data))        if reset_fleg == 1:            data = []      except NameError:        data = []    if len(df2)>0:        matrix_fields_1 = process_datafields(df1, "matrix")        data.extend(matrix_fields_1)    if len(df3)>0:        vector_fields_1 = process_datafields(df1, "vector")           data.extend(vector_fields_1)    print(dataset_id,'执行完毕')print(len(data))
```

剩下的工作就是套在不同的模版中了，祝大家早日达到MASTER!

---

### 帖子 #51: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
- **主帖链接**: https://support.worldquantbrain.com[L2] 代码分享拉取某个category下的全部dataset并实现批量生产数据预处理备战Pyramid_28040550959511.md
- **讨论数**: 5

```
分享代码给所有冲刺Pyramid的同学，分享不易，感谢点赞评论
```

这套代码结合了三阶框架和ACE Library，之前我们在跑单数据集的时候经常会放弃一些小数据集，从而可能错失一些有效的字段。本代码可以批量拉取某个category下的字段，并进行一定的筛选。

- **核心代码：获取全部datasets**

```
def get_datasets(    s,    instrument_type: str = 'EQUITY',    region: str = 'USA',    delay: int = 1,    universe: str = 'TOP3000'):    brain_api_url = "[链接已屏蔽]    url = brain_api_url + "/data-sets?" +\        f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"    result = s.get(url)    datasets_df = pd.DataFrame(result.json()['results'])    return datasets_df
```

- 筛选需要的category和coverage等信息

```
region = "JPN"region_code = "jpn"universe = "TOP1600"delay = 1datasets_df = get_datasets(s,region='JPN',delay=1,universe='TOP1600')pd.set_option('display.max_columns', None)  # 显示所有列pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值# select needed datasetsselected_datasets_df = datasets_df[    (datasets_df["delay"] == delay) &    (datasets_df["coverage"] > 0.5) & (datasets_df["coverage"] <= 1) &    (datasets_df["fieldCount"] > 0) & (datasets_df["fieldCount"] < 2000) &    (datasets_df["region"] == region) &    (datasets_df["universe"] == universe) &    (datasets_df["userCount"] > 0) & (datasets_df["userCount"] < 100) &    (datasets_df["valueScore"] > 1) & (datasets_df["valueScore"] < 10) &    (datasets_df["category"].apply(lambda x: x.get("id") if isinstance(x, dict) else None) == "analyst")    #(datasets_df["category"]  'analyst')    #datasets_df["name"].str.contains('news', case=False) &    #((datasets_df["category"] == 'analyst') | (datasets_df["category"] == 'analyst'))].sort_values(by=['valueScore'], ascending=False)print(selected_datasets_df)
```

- 批量预处理数据，生成数据大表，这里的作用等价于老师在论坛写的推荐数据

```
reset_fleg = 0for dataset_id in selected_datasets_df['id']:    df1 = get_datafields(s, dataset_id = dataset_id, region= region, universe=universe, delay=delay)    pd.set_option('display.max_columns', None)  # 显示所有列    pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值    df2 = df1[df1['type'] == 'MATRIX']    df3 = df1[df1['type'] == 'VECTOR']    #df4 = df1[df1['type'] == 'GROUP']    try:        print(len(data))        if reset_fleg == 1:            data = []      except NameError:        data = []    if len(df2)>0:        matrix_fields_1 = process_datafields(df1, "matrix")        data.extend(matrix_fields_1)    if len(df3)>0:        vector_fields_1 = process_datafields(df1, "vector")           data.extend(vector_fields_1)    print(dataset_id,'执行完毕')print(len(data))
```

剩下的工作就是套在不同的模版中了，祝大家早日达到MASTER!

---

### 帖子 #52: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **讨论数**: 30

### 先赞后看,养成好习惯.

## 1 . 来时路

背景: 普通SqlBoy

成为顾问:2024年11月07日

VF变化: 0.5 → 0.77 → 0.99 → 0.99

Genius级别: 2024Q4 Expert, 2025Q1 GM

目前Combine: 2.11 select: 1.86

## 

## 2. 野蛮交

去年最后一个季度未能完全搞清Genius决胜规则,所以在计算出有机会交满220个达到GM基准线后,就每天4个,足100后每天交SA
此时是不太讲质量的,平均fit<1.5,但讲究如下两点

- 点金字塔,做好风格切换
- 小地区保证做超过10个

以上两点,已有vf0.99和Combine证明基本正确

> 做不出模板,做不出手工Alpha,你就保证风格多样(我就是)
> 小地区要么不做,要么多做

## 

## 3. 狂敛财

> 声明: 以下行为有一定风险,还需时间验证

拥有SA权限以后,在一个地区超过80个alpha以后,可以开启稳定挣base模式

SA要挣钱,基本要求是fit>5,prod<0.7,实测vf0.99的话,base至少45刀


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/13/2025
> Super:
> 49.18
> 5O
> Regular:
> 4.35
> Total:
> 53.53
> <<@
> SN _
> SN _
> p ppe
> 
> 8"
> 90
> 6 ^8'38:
> :
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> ADr
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar


记住, ***一条都不能破,且超标太高意义不大***

> 本来SA的fit都超过5了,你就这么有自信他的OS也能这么好?
> 既然如此,还往上飙意义在哪儿?几乎必然过拟合
> 从奖赏机制上也看得出来开,fit飚上去base打不满
> 但是prod降下来却能打满.但是很难,性价比又低

那么,怎么挣这个钱呢?

这里提供一个简单的思路.

收集select表达式20个.中性化也有10种,comb表达式来个20个,

一共就有了400个SA,全部跑完算self_cor即可.

随着持续提交,加上染色等,SA数量会远超400.

假设获得50个可交alpha,这时候怎么交呢?

***计算互相之间的self_cor,用最大团算法获取最长可交子集!!!***

## 4. 少年归

随着持续的挖掘和学习,有时候是知道哪些是正确的事情的
比如:

```
交fitness高的alpha
```

```
多做基本面的alpha
```

```
交有经济学意义的alpha
```

```
多交ATOM
```

```
多做SA
```

不是不想做啊,有时候真的难啊,感慨 **站着说话不腰疼** 啊.

做不到怎么办?

> **如果你不知道你做什么,那么你就想想你最讨厌什么,然后努力朝相反的方向奔跑**

坚持不做错误的事情,必将收获好的回报

我是WorldQuant中国区顾问,我 **庄严承诺** :

- 不混信号 !
- 不一直在同一个池子挖呀挖呀挖 !
- 不一个模板跑一年 !
- 不交自己都不相信的alpha !
- 不拒绝学习,不在比赛躺平,不忽略平台指引 !!!

---

### 帖子 #53: 使用[ClickHouse📕]建设你的大型数据库
- **主帖链接**: [L2] 使用[ClickHouse]建设你的大型数据库.md
- **讨论数**: 3

**ClickHouse**  是一个开源的列式数据库管理系统（DBMS），专为在线分析处理（OLAP）场景设计。ClickHouse 以其卓越的查询性能和高效的数据压缩能力而闻名，特别适合处理大规模数据的实时分析查询。

相比  **MySQL** ，ClickHouse 的列式存储和高效压缩使其在大规模数据分析场景下查询性能提升数十倍；相比  **MongoDB** ，ClickHouse 对复杂 SQL 查询和聚合操作的支持更强大，适合实时分析和高性能 OLAP 场景。

本文将持续更新，但不保证能连载完毕，因为我也是刚开始用这个东西，现学现卖

**前置准备：下载clickhouse并安装**

[[ClickHouse📕]Download and Install CK – WorldQuant BRAIN](/hc/en-us/community/posts/29266868911383--ClickHouse-Download-and-Install-CK) 

 **第一步：创建表，每一个表的内容都不一样，需要进行存储，下面是每一个你需要创建的表。** 。

[[ClickHouse📕]table: submitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266765833239--ClickHouse-table-submitted)

[[ClickHouse📕]table: pnls – WorldQuant BRAIN](/hc/en-us/community/posts/29266954512663--ClickHouse-table-pnls)

[[ClickHouse📕]table: fields – WorldQuant BRAIN](/hc/en-us/community/posts/29266990090263--ClickHouse-table-fields)

[[ClickHouse📕]table: unsubmitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266971586327--ClickHouse-table-unsubmitted)

第二步：导入数据

To Be Continue....

您的点赞就是我最大的动力

---

### 帖子 #54: 使用[ClickHouse📕]建设你的大型数据库
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用[ClickHouse]建设你的大型数据库_29266895095063.md
- **讨论数**: 3

**ClickHouse**  是一个开源的列式数据库管理系统（DBMS），专为在线分析处理（OLAP）场景设计。ClickHouse 以其卓越的查询性能和高效的数据压缩能力而闻名，特别适合处理大规模数据的实时分析查询。

相比  **MySQL** ，ClickHouse 的列式存储和高效压缩使其在大规模数据分析场景下查询性能提升数十倍；相比  **MongoDB** ，ClickHouse 对复杂 SQL 查询和聚合操作的支持更强大，适合实时分析和高性能 OLAP 场景。

本文将持续更新，但不保证能连载完毕，因为我也是刚开始用这个东西，现学现卖

**前置准备：下载clickhouse并安装**

[[ClickHouse📕]Download and Install CK – WorldQuant BRAIN](/hc/en-us/community/posts/29266868911383--ClickHouse-Download-and-Install-CK) 

 **第一步：创建表，每一个表的内容都不一样，需要进行存储，下面是每一个你需要创建的表。** 。

[[ClickHouse📕]table: submitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266765833239--ClickHouse-table-submitted)

[[ClickHouse📕]table: pnls – WorldQuant BRAIN](/hc/en-us/community/posts/29266954512663--ClickHouse-table-pnls)

[[ClickHouse📕]table: fields – WorldQuant BRAIN](/hc/en-us/community/posts/29266990090263--ClickHouse-table-fields)

[[ClickHouse📕]table: unsubmitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266971586327--ClickHouse-table-unsubmitted)

第二步：导入数据

To Be Continue....

您的点赞就是我最大的动力

---

### 帖子 #55: print(pools[0])
- **主帖链接**: https://support.worldquantbrain.com[L2] 多线程遍历回测super alpha代码优化_31527668843671.md
- **讨论数**: 21

def multi_simulate2_sa(alpha_pools, neut, region, universe, start):
    global s

s = login()

brain_api_url = ' [[链接已屏蔽]) '

limit_of_concurrent_simulations = len(alpha_pools[0])

alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]
    # print(alpha_pools_2)

end = len(alpha_pools_2)

print(f'length:{len(alpha_pools_2)}, start:{start}')
    counter: int = start
    lock = threading.Lock()

def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):
        while True:
            global s
            lock.acquire()
            nonlocal counter
            if counter > end - 1:
                lock.release()
                break
            if (counter - start) % 250 == 0:  # re-login after every 60 multi_sims
                s = login()
            local_counter = counter
            counter += 1
            lock.release()
            task = pools[local_counter]
            sim_data_list = generate_sim_data_sa(task, region, universe, neut)
            sim_data=sim_data_list[0]
            try:
                simulation_response = s.post(' [[链接已屏蔽]) ', json=sim_data)
                simulation_progress_url = simulation_response.headers['Location']
                # simulation_progress_url = simulation_response.headers.get('location')
            except:
                print(" loc key error")
                sleep(600)
                s = login()

print(f"task {local_counter} post done")

try:
                while True:
                    simulation_progress = s.get(simulation_progress_url)
                    if simulation_progress.headers.get("Retry-After", 0) == 0:
                        break
                    # print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
                    sleep(float(simulation_progress.headers["Retry-After"]))

status = simulation_progress.json().get("status", 0)
                if status != "COMPLETE":
                    print(f"Not complete : {simulation_progress_url}")

"""
                #alpha_id = simulation_progress.json()["alpha"]
                children = simulation_progress.json().get("children", 0)
                children_list = []
                for child in children:
                    child_progress = s.get(brain_api_url + "/simulations/" + child)
                    alpha_id = child_progress.json()["alpha"]

set_alpha_properties(s,
                            alpha_id,
                            name = "%s"%name,
                            color = None,)
                """
            except KeyError:
                print(f"look into: {simulation_progress_url}")
            except:
                print("other")

print(f"task {local_counter} simulate done")

t = []
    for i in range(limit_of_concurrent_simulations):
        t.append(threading.Thread(target=sim_task))
        t[i].start()

for i in range(limit_of_concurrent_simulations):
        t[i].join()

print("Simulate done")

def generate_sim_data_sa(alpha_list, region, uni, neut):
    sim_data_list = []
    for selection_exp, combo_exp in alpha_list:
        # print(selection_exp)
        # print(combo_exp)
        simulation_data = {
            'type': 'SUPER',
            'settings': {
                'instrumentType': 'EQUITY',
                'region': region,
                'universe': uni,
                'delay': 1,
                'decay': 6,
                'neutralization': neut,
                'truncation': 0.08,
                'pasteurization': 'ON',
                'unitHandling': 'VERIFY',
                'nanHandling': 'ON',
                'selectionHandling': 'POSITIVE',
                'selectionLimit': 1000,
                'language': 'FASTEXPR',
                'visualization': False,
            },
            'selection': selection_exp,
            'combo': combo_exp}

sim_data_list.append(simulation_data)
    return sim_data_list

```
import threading
```

```
from machine_lib import *
```

selection_exp=['turnover<0.15']
combo_exp=['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr);maxCorr = reduce_max(ic); 1 - maxCorr']
sa_list=[(i,j) for i in selection_exp for j in combo_exp]
print(len(sa_list))
print(sa_list[0])

pools = load_task_pool(sa_list, 1, 3)
# print(pools[0])
region_dict = {"usa": ("USA", ["TOP3000", "TOP1000", "TOP500", "TOP200"]),
               "asi": ("ASI", ["MINVOL1M"]),
               "eur": ("EUR", ["TOP2500","TOP1200", "TOP800", "TOP400"]),
               "glb": ("GLB", ["TOP3000", 'MINVOL1M']),
               "hkg": ("HKG", ["TOP800", "TOP500"]),
               "twn": ("TWN", ["TOP500", "TOP100"]),
               "jpn": ("JPN", ["TOP1600", "TOP1200"]),
               "kor": ("KOR", ["TOP600"]),
               "chn": ("CHN", ["TOP2000U"]),
               "amr": ("AMR", ["TOP600"])}

norm_opt=["INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"]
risk_opt=["FAST","SLOW","SLOW_AND_FAST"]
r1=['STATISTICAL']
cr=["CROWDING"]
co=["COUNTRY"]
no=["NONE"]
neut_opt={"USA":norm_opt+cr+risk_opt+r1,
          "GLB":co+r1,
          "EUR":co+cr+norm_opt+risk_opt+r1,
"ASI":co+cr+norm_opt+risk_opt+no,
"CHN":norm_opt+cr+risk_opt+r1,
          "KOR":norm_opt,
          "TWN":norm_opt,
          "HKG":norm_opt,
          "JPN":norm_opt,
          "AMR": ["COUNTRY"]+norm_opt,
          }

regi = ['usa']
for k in regi:
    for i in region_dict[k][1][:1]:
        print(i)
        for j in neut_opt[k.upper()]:
            print(j, region_dict[k][0])
            multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)

最后说明，该代码的多线程部分是由一位大佬编写，用于回测regler alpha，曾经分享在学习群，我在此基础改编成用于回测super alpha。如果本人看到此贴请留下相关链接，后续加上相关信息。

---

### 帖子 #56: 增量下载数据download_data(flag_increment=True)
- **主帖链接**: https://support.worldquantbrain.com[L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md
- **讨论数**: 30

基于  [顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97))  发现的本地计算自相关性方法的落地，self-corr只计算本region里提交的所有alphas

首先一些函数，由于有函数说明，这里就不详细展开了

```
import requestsimport pandas as pdimport loggingimport timeimport requestsfrom typing import Optional, Tuplefrom typing import Tuple, Dict, Listfrom typing import Union, List, Tuplefrom concurrent.futures import ThreadPoolExecutorimport picklefrom collections import defaultdictimport numpy as npfrom tqdm import tqdmfrom pathlib import Pathdef sign_in(username, password):    s = requests.Session()    s.auth = (username, password)    try:        response = s.post('[链接已屏蔽])        response.raise_for_status()        logging.info("Successfully signed in")        return s    except requests.exceptions.RequestException as e:        logging.error(f"Login failed: {e}")        return Nonedef save_obj(obj: object, name: str) -> None:    """    保存对象到文件中，以 pickle 格式序列化。    Args:        obj (object): 需要保存的对象。        name (str): 文件名（不包含扩展名），保存的文件将以 '.pickle' 为扩展名。    Returns:        None: 此函数无返回值。    Raises:        pickle.PickleError: 如果序列化过程中发生错误。        IOError: 如果文件写入过程中发生 I/O 错误。    """    with open(name + '.pickle', 'wb') as f:        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)def load_obj(name: str) -> object:    """    加载指定名称的 pickle 文件并返回其内容。    此函数会打开一个以 `.pickle` 为扩展名的文件，并使用 `pickle` 模块加载其内容。    Args:        name (str): 不带扩展名的文件名称。    Returns:        object: 从 pickle 文件中加载的 Python 对象。    Raises:        FileNotFoundError: 如果指定的文件不存在。        pickle.UnpicklingError: 如果文件内容无法被正确反序列化。    """    with open(name + '.pickle', 'rb') as f:        return pickle.load(f)   def wait_get(url: str, max_retries: int = 10) -> "Response":    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。       Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。       Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    df = df[['Date', alpha_id]]    return dfdef get_alpha_pnls(    alphas: list[dict],    alpha_pnls: Optional[pd.DataFrame] = None,    alpha_ids: Optional[dict[str, list]] = None) -> Tuple[dict[str, list], pd.DataFrame]:    """    获取 alpha 的 PnL 数据，并按区域分类 alpha 的 ID。    Args:        alphas (list[dict]): 包含 alpha 信息的列表，每个元素是一个字典，包含 alpha 的 ID 和设置等信息。        alpha_pnls (Optional[pd.DataFrame], 可选): 已有的 alpha PnL 数据，默认为空的 DataFrame。        alpha_ids (Optional[dict[str, list]], 可选): 按区域分类的 alpha ID 字典，默认为空字典。    Returns:        Tuple[dict[str, list], pd.DataFrame]:            - 按区域分类的 alpha ID 字典。            - 包含所有 alpha 的 PnL 数据的 DataFrame。    """    if alpha_ids is None:        alpha_ids = defaultdict(list)    if alpha_pnls is None:        alpha_pnls = pd.DataFrame()       new_alphas = [item for item in alphas if item['id'] not in alpha_pnls.columns]    if not new_alphas:        return alpha_ids, alpha_pnls       for item_alpha in new_alphas:        alpha_ids[item_alpha['settings']['region']].append(item_alpha['id'])    fetch_pnl_func = lambda alpha_id: _get_alpha_pnl(alpha_id).set_index('Date')    with ThreadPoolExecutor(max_workers=10) as executor:        results = executor.map(fetch_pnl_func, [item['id'] for item in new_alphas])    alpha_pnls = pd.concat([alpha_pnls] + list(results), axis=1)    alpha_pnls.sort_index(inplace=True)    return alpha_ids, alpha_pnlsdef get_os_alphas(limit: int = 100, get_first: bool = False) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    retries = 0    total_alphas = 100    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url = f"[链接已屏蔽]        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphas[:total_alphas]def calc_self_corr(    alpha_id: str,    os_alpha_rets: pd.DataFrame | None = None,    os_alpha_ids: dict[str, str] | None = None,    alpha_result: dict | None = None,    return_alpha_pnls: bool = False,    alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    print(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corrdef download_data(flag_increment=True):    """    下载数据并保存到指定路径。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        flag_increment (bool): 是否使用增量下载，默认为 True。    """    if flag_increment:        try:            os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))            os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))            ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))            exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]        except Exception as e:            logging.error(f"Failed to load existing data: {e}")            os_alpha_ids = None            os_alpha_pnls = None            exist_alpha = []            ppac_alpha_ids = []    else:        os_alpha_ids = None        os_alpha_pnls = None        exist_alpha = []        ppac_alpha_ids = []           if os_alpha_ids is None:        alphas = get_os_alphas(limit=100, get_first=False)    else:        alphas = get_os_alphas(limit=30, get_first=True)       alphas = [item for item in alphas if item['id'] not in exist_alpha]    ppac_alpha_ids += [item['id'] for item in alphas for item_match in item['classifications'] if item_match['name'] == 'Power Pool Alpha']               os_alpha_ids, os_alpha_pnls = get_alpha_pnls(alphas, alpha_pnls=os_alpha_pnls, alpha_ids=os_alpha_ids)    save_obj(os_alpha_ids, str(cfg.data_path / 'os_alpha_ids'))    save_obj(os_alpha_pnls, str(cfg.data_path / 'os_alpha_pnls'))    save_obj(ppac_alpha_ids, str(cfg.data_path / 'ppac_alpha_ids'))    print(f'新下载的alpha数量: {len(alphas)}, 目前总共alpha数量: {os_alpha_pnls.shape[1]}')def load_data(tag=None):    """    加载数据。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        tag (str): 数据标记，默认为 None。    """    os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))    os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))    ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))    if tag=='PPAC':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha in ppac_alpha_ids]    elif tag=='SelfCorr':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha not in ppac_alpha_ids]    else:        os_alpha_ids = os_alpha_ids    exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]    os_alpha_pnls = os_alpha_pnls[exist_alpha]    os_alpha_rets = os_alpha_pnls - os_alpha_pnls.ffill().shift(1)    os_alpha_rets = os_alpha_rets[pd.to_datetime(os_alpha_rets.index)>pd.to_datetime(os_alpha_rets.index).max() - pd.DateOffset(years=4)]    return os_alpha_ids, os_alpha_rets
```

首先把上述函数拷贝出来

在配置的cfg里添加账户和密码以及os_alpha保存的路径

```
class cfg:    username = ""    password = ""    data_path = Path('.')sess = sign_in(cfg.username, cfg.password)
```

增量下载OS数据，下载好的数据将会保存在data_path里

```
# 增量下载数据download_data(flag_increment=True)
```

之后加载数据，计算corr。

其中`load_data`函数里有一个可选参数tag。来区分获得alpha，

如果设置tag='PPAC'则只获取PPAC池子里的alpha，

如果设置tag='SelfCorr'则只获取除了PPAC池子里的其他alpha

如果不设置或者 设置为None，则获取所有提交的alpha

calc_self_corr返回最大的自相关性

```
alpha_id = 'OJwdKNb'os_alpha_ids, os_alpha_rets = load_data()calc_self_corr(    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)
```

我在此选了两个例子用以展示结果

第一个 例子是一个`厂alpha`


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 30OOK
> OOOK
> OOOK
> Jan '14
> Jan'15
> Jan'16
> Jan '17
> Jan '18
> Jan'19
> Jan '20
> Jan '21
> Jan '23
> Pnl
> Jan 22


其wq平台的线上self-corr如下


> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> [aimUm
> [inimUT
> 0.0719
> -0.0715
> 名字
> Unlyerse
> Correlaton
> Sharpe
> Returns
> Tumovar
> Htess
> Margln
> ATOITITOUIS
> current)
> TOP3O00
> 1.0000
> 6.32
> 255.44%
> 30.05%6
> 18.43
> 170.029
> anonyymous
> TOPIOOO
> 0.0719
> 2.59
> 12014
> 7.1395
> 2.33
> 33.539
> aOTIMOUs
> TOP230
> 0.0634
> 2.52
> 10.744
> 13.3591
> 2.30
> 11.53922
> aROTIIOUs
> TOP3OO
> 0.0525
> 3.8-
> 13.134
> 11.3695
> 3.34
> 2.059
> TyMOUs
> TOP3OI
> 0.0495
> 5.53
> 10.944
> 10.8793
> 5.17
> 20.1292
> anOnyMOUs
> ILLIQUID_MINVOLIII
> 0.0399
> 3.96
> 3.734
> 12.5595
> 3.29
> 13.79923
> L2st


通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha
> OJWdKMb
> O5_alpha_ids,
> O5_alpha_rets
> load_data
> Selfcorr
> Calc_self_corr(
> alpha_id-alpha_id,
> O5_alpha
> rets=os_alpha
> pets,
> O5_alpha_ids=os_alpha_ids,
> 3ZKROG
> 0719
> IMOOON
> 0.0684
> Xn68QGb
> 0526
> Oogjjpb
> 0.0496
> gnrlMpl
> 0399
> RdgYkao
> 0587
> AkYpgIw
> 0.0604
> KkGPBJI
> 0655
> SMVZb2I
> 0.0703
> KO3M3eB
> 0715
> Length: 367
> dtype:
> float64
> 叩.float64(8.07191757289855728)
> (tn=


其线上PPAC结果为： Power Pool correlation 0.0356 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.

通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> OJWdKMb
> O5_alpha_ids,
> O5_alpha
> pets
> load_data
> PPAC
> Calc_self
> Corr(
> alpha_id-alpha_id,
> O5_alpha_rets=os_alpha_
> pets
> O5_alpha_ids=os_alpha_ids,
> WL8EVgX
> 0356
> V0a7JR2
> 0.0291
> ONjAqWb
> 0269
> O8nlN3q
> 0.0260
> pSeGPvv
> 0222
> aVNJAdI
> 0286
> SjbrMGN
> 0.0231
> X1Z08Y]
> 0247
> e6813诏
> 0.0267
> WgBar7e
> -0.0314
> Length: 61,
> dtype:
> f1oat64
> 叩.float64(8.03561886586891495)
> (tD8=


第二个 例子是一个正常的例子


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> PIL
> LOOOK
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> 2023


其wq平台的线上self-corr如下 
> [!NOTE] [图片 OCR 识别内容]
> 名宇
> UnNerse
> Correlatlon
> Sharpe
> Returns
> TurNOVer
> Hltness
> Margln
> anonymous (current)
> TOP3000
> 1.0000
> 1.51
> 6.329
> 3.0396
> 1.07
> 41.708
> anONNMOUs
> TOP300
> 0.5243
> 11.034
> 7.230
> 172
> 305292
> anOnyMOUs
> TOF3JOO
> 0.5241
> 10.244
> 4.9055
> 11.80922
> anonymous
> TOP300
> 0.5051
> 34
> 11.744
> 11.303
> 3.30
> 20.779323
> anOnyMOUs
> TOF3JOO
> 0.-931
> 153
> 12.12北
> 10.7350
> 1.57
> 22.499522
> anONNMOUs
> TOP300
> 0.4453
> 4.16
> 19.254
> 10.8130
> 5.15
> 35.52933


通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> 1P13*52
> O5_alpha_ids,
> O5_alpha
> pets
> load_data (ta=
> Selfcorr
> Calc
> cor(
> alpha_id-alpha_id,
> O5_alpha_rets=os_alpha_rets,
> Os_alpha_ids=os_alpha_ids,
> 146]
> IXqSZMJ
> 0.5243
> ANKqaGE
> 0.5241
> OLOAgYI
> 0.5061
> EIMGbe]
> 4901
> PZAVYRL
> 0.4463
> LnOZEYG
> 0.3494
> MbAGKZ8
> 0.3495
> Mbgzgjr
> 0.3523
> XkGORLS
> 0.3719
> JnLZlnl
> 0.3952
> Length: 386, dtype:
> float64
> m.float64 (0.524288988654845 )
> Self


其线上PPAC结果为： Power Pool correlation 0.4901 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.

通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> JPY3*52
> 05_alpha_ids,
> O5_alpha
> load_data
> PPAC
> Calc_self_corr(
> alpha_id-alpha_id,
> O5_alpha
> rets=os_alpha_rets,
> O5_alpha_ids=os_alpha_ids,
> OWZzzan
> 4901
> AOnjj8e
> 0.4667
> aVNJAdI
> 4495
> 3jLrp8e
> 0.4468
> YxdOKRV
> 0.4382
> ONnJOEV
> 0.0129
> GbuPrwG
> 0186
> PBKaEWN
> -0.0220
> XIBQVIJ
> -0.0322
> 15j7091
> -0.0604
> Length:
> 61, dtype: float64
> m.float64(9.4980856236004994)
> pots
> (tn=


---

### 帖子 #57: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 组sa时如何选取高质量因子经验分享_32034293019671.md
- **讨论数**: 24

如题，在顾问群中发现很多刚开始组sa的顾问，不清楚select的具体选择方式。本帖给出对应规则以及一些例子。

对于expert及以上顾问来说，筛选因子的第一步是用自己的因子，还是组别人的。这个可以通过own和not(own）进行筛选。

第二步，降低选到的因子是过拟合的，或者混信号的概率，可以通过operator_count限制op数量，dataset_count限制数据集数量。

（第二点五步，如果想要选取特定category，特定color或者特定tag的因子，也可以进行筛选。研究小组中有大佬提出过利用color和tag对于因子进行分组，从而按组select的方式）

第三步，选低相关因子：从分散化角度来说,我们自然希望选出的因子相关性较低,这个可以从prod_correlation参数进行控制（selfcor也可以，但是这个是小于等于prod的，不够准确）

第四步，选老顾问/组合表现较好顾问的因子：平台提供了许多因子owner的相关数据参数，可以根据参数进行筛选，主要包括成为顾问的时长，顾问地区，该顾问的sharpe，fit等等

第五步，按照表现选因子。出于防止过拟合和刻意筛选的角度，我们不能够直接选高sharpe，高fit的好（not for sure）因子，平台提供了几个字段帮助我们筛选因子，包括turnover，truncation，long和short count等等，按照每个字段的范围进行分组选因子可以大幅降低重复筛选的概率，从而降低相关性。

前边几步是筛选的过程，对于筛选的权重我们也可以进行调整。

例如：我们可以按照turnover的大小进行赋权，对于turnover较高的因子赋予更小的 权重（在select表达式后加上/turnover即可），此步需要根据个人需求进行修改。

总结：

以上几步是我在筛选中的思考流程，更为详细具体的可以参考 [Selection Expression | WorldQuant BRAIN]([链接已屏蔽]) ，针对因子选择的流程需要发挥主观能动性，多想多试，才能选出最适合的因子。以下几个案例是我在研究小组发过的select表达式总结，可以基于这三类，对于参数与权重进行调整，从而实现更好的组合。在自动化跑sa的时候，也可以按照不同的“模块”进行组装（但要注意条件不能太苛刻，至少得选出10个因子才能开始跑。）

(own&& ( (turnover>0.03&&turnover<0.05)||(turnover<0.13&&turnover>0.1)||(turnover<0.17&&turnover>0.15) || ((turnover>0.17&&turnover<0.20)))&&(operator_count<18)&&prod_correlation<0.7)/(sigmoid(turnover)*sigmoid(prod_correlation)*log(long_count))

(
not(own)&& 
((turnover<0.12&&turnover>0.09)||(turnover<0.15&&turnover>0.13)||(turnover<0.19&&turnover>0.16))
&&(operator_count<8)
&&(prod_correlation<0.4&&prod_correlation>0.0)
&&(dataset_count<=2)
) 
/(turnover*tanh(turnover)*sigmoid(self_correlation)*sigmoid(prod_correlation)*abs(long_count-short_count))

(own&&(turnover<0.07||(turnover<0.25&&turnover>0.2)))/(sigmoid(turnover)*sigmoid(prod_correlation))

---

### 帖子 #58: 给新手跑region和dataset的小建议
- **主帖链接**: https://support.worldquantbrain.com[L2] 给新手跑region和dataset的小建议_28467103126679.md
- **讨论数**: 8

我是一个 ***10月25日*** 才加入顾问计划的新人，经过非常非常多的尝试，每天花费了大量时间后， ***现在因子交了167个，金字塔完成了48个。*** 

前期新人跑数据挖掘遇到的大问题就是， **region** 的选择和 **dataset** 的选择，因为每个类型的数据集和每个地区的难度都是不一样的，所以前期新人更适合选一些简单的region或者dataset。

接下来我将分享一下我个人的一些心得体会，希望对新人有所帮助。

## 首先是region的选择。

region一共有10个，分别是：USA, GLB, EUR, ASI, CHN, KOR, TWN, JPN, HKG, AMR。

```
REGION_LIST = ['USA', 'GLB', 'EUR', 'ASI', 'CHN', 'KOR', 'TWN', 'JPN', 'HKG', 'AMR']
```

他们的简单程度我认为是

ASI > USA > TWN > EUR > GLB > JPN = CHN = HKG > KOR > AMR （都是delay 1的）

## 然后是category的选择

category一共有16个，分别是：pv, fundamental, analyst, socialmedia, news, option, model, shortinterest, institutions, other, sentiment, insiders, earnings, macro, imbalance, risk。

```
DATASET_CATEGORY_LIST = ['pv', 'fundamental', 'analyst', 'socialmedia', 'news', 'option', 'model', 'shortinterest', 'institutions', 'other', 'sentiment', 'insiders', 'earnings', 'macro', 'imbalance', 'risk']
```

他们的简单程度我认为是

model > pv > analyst = fundamental > other > option > institutions = news = insiders = sentiment > macro = risk = shortinterest = socialmedia > earnings > imbalance （都是delay 1的）

另外不建议新手去做delay 0的，我跑了近50万个都没有一个可以交的。

---

### 帖子 #59: 【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化
- **主帖链接**: 【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化.md
- **讨论数**: 16

fit>5,prod小于5的SA,是小伙伴们都追求的梦中SA。那么如何快速找到有比较大的可能可以调整到低于0.5的SA进行调整呢？

这里的思路是：

```
1、获取已有的SA列表（包含详细信息）；（代码回测super alpha，    这样你就可以有超级多的superalpha 选择了）2、检查自相关性（参考 顾问 KZ79256 (Rank 21) 大佬的帖子），如果自相关超过5，就跳过检查生产相关3、检查生产相关性，并获取每个相关性区间的alpha数，最后存入本地文件。  根据check结果，选择fit>5, 0.4-0.5区间，0.5-0.6区间相对较少的SA，尝试降低prod,   这样成功的概率会比较高。
```

代码如下：（本地自相关性的计算，这里就不详细描述了，可自行参考  **顾问 KZ79256 (Rank 21)** 大佬的帖子 ； [看这里](../顾问 KZ79256 (Rank 21)/本地0误差计算自相关性【即插即用版】代码优化.md) )

```
    # 加载本地pnl数据    os_alpha_ids, os_alpha_rets = load_data()    start=0    # alpha_infos是个列表，列表中是每个alpha的详细信息，可通过get_alpha函数获取    alpha_infos = alpha_infos[start:]    for i  in range(0,len(alpha_infos)):         alpha_info=alpha_infos[i]         alpha_id=alpha_info["id"]         print(f"begin check id :{i+start}, {alpha_id}")         # append_to_file 函数是个记录日志的函数         append_to_file("check.log",f"begin check id :{i+start}, {alpha_id} ",True)         date_create=alpha_info["dateCreated"]         fitness = alpha_info['is']['fitness']         sharpe = alpha_info['is']['sharpe']         turnover = alpha_info['is']['turnover']         margin = alpha_info['is']['margin']         drawdown = alpha_info['is']['drawdown']         returns = alpha_info['is']['returns']         region = alpha_info['settings']['region']         checks=alpha_info["is"]["checks"]         LOW_2Y_SHARPE=0         for item in checks:             if item["name"] == LOW_2Y_SHARPE:                 LOW_2Y_SHARPE=item["value"]         #检查自相关         corr_id,corr_value=calc_self_corr( alpha_id, os_alpha_rets,  os_alpha_ids,None,True,None)         f = float(corr_value)         rounded_f = round(f, 4)         if   rounded_f >=0.5:             print(f"selfcorr more than 0.5,and self > 0.7 ;switch {alpha_id};  self:{rounded_f}")             set_alpha_properties(alpha_id=alpha_id, name=f"SELF_CORR_{rounded_f}", color="BLUE")             continue         num4_num5=0         num5_num6=0         num6_num7=0         while True:         # 获取prod 相关性值            response=my_get(f"[链接已屏蔽])            if response != None:                try:                    res=response.json()                    prod=res["max"]                    for list_ in res["records"]:                    # 获取相关性在0.4-0.5区间的alpha数                        if list_[0] == 0.4 and list_[1] == 0.5:                            num4_num5=list_[2]                    # 获取相关性在0.5-0.6区间的alpha数                        if list_[0] == 0.5 and list_[1] == 0.6:                            num5_num6=list_[2]                    # 获取相关性在0.6-0.7区间的alpha数                        if list_[0] == 0.6 and list_[1] == 0.7:                            num6_num7=list_[2]                    break                except Exception as e:                    print(f"get prod failed,try again")            sleep(10)         if  fitness > 5 and prod < 0.5 and sharpe >5 and LOW_2Y_SHARPE >=5:             print(f"begin submit alpha: {alpha_id}")             append_to_file("submit.log",f"fit>5,prod<5的alpha id: {alpha_id}",True)             #submit_alpha(s,alpha_id)         com_des=alpha_info["combo"]["description"]         select_des=alpha_info["selection"]["description"]         set_alpha_properties(alpha_id,f"PROD_{str(prod)}","RED")         a=json.dumps([alpha_id,f"self:{rounded_f}",f"prod:{prod}",{"num4_num5":num4_num5,"num5_num6":num5_num6,"num6_num_7":num6_num7,"fitness":fitness,"sharpe":sharpe,"turnover":turnover,"drowdown":drawdown,"returns":returns,"region":region}])         append_to_file("res.txt",a,True)    print(f"finish check")
```

check的结果res.txt如下：


> [!NOTE] [图片 OCR 识别内容]
> 2025-06-12
> 17:18:49.033085
> ["ZdwgZj3"
> Iself
> 0.4133"
> prod
> 0.5911"
> {"num4_num5"
> 12
> Inum5
> nUNIG "
> InUmG
> nUII_7" :
> Ifitness"
> 6.97
> "sharpe"
> 5.88 ,
> IturnoVer"
> 0.1201 ,
> Idrowdown
> 0206
> "returns
> 0.1754
> "region
> "USA" }]
> 2025-06-12
> 17:20:41.196934
> ["mOAPIGS"
> Isel
> :0.4013"
> prod: 0 .5793"
> {"numy_num5"
> 15,
> num5_num6"
> numG_num_ 7" :
> Ifitness
> 6 .87,
> larpe
> 5.85
> IturnoVer"
> 0.1209
> Idrowdown
> 0.0219
> Ireturns
> 0.1726
> "region
> "USA" }]
> 2025-06-12
> 17:23:05
> 790562
> [ "ZXREaqw
> Iself: 0.4629"
> prod: 0
> 5445"
> {"numy_num5"
> 38
> "num5_num6 "
> 2,
> "numG_num_ 7"
> Ifitness"
> 6.75
> "sharpe"
> 6.15
> IturnoVer"
> 0.0957
> Idrowdown
> 0153
> "returns
> 0.1509
> "region
> IEUR" } ]
> 2025-06-12
> 17:25:26.983654
> ["7VOdAEZ"
> Iself: 0.4146"
> 'prod: 0 .6266"
> {"numy_num5"
> 8181,
> num5_num6"
> "num6_num_7" :
> 1,
> Ifitness"
> 5.27,
> "sharpe"
> 6.12,
> IturnoVer"
> 0.1773
> Idrowdown "
> 0.01
> 39
> Ireturns
> 0.1314
> "region"
> IUSA" }]
> 2025-06-12
> 17:35:47.662261
> ["EgYgQkg"
> Iself
> 0.3476"
> prod
> 0.5529"
> {"num4_num5"
> num5
> num6 "
> num6
> nUm_ 7"
> Ifitness"
> 5.2,
> sharpe"
> 6.38
> IturnoVer"
> 0.1901
> Idrowdown
> 0094
> returns
> 0.1265
> Iregion"
> "USA"}]
> 2025-06-12
> 17:36:08
> 724525
> ["601v677"
> Iself
> 0.3422"
> prod
> 0.5644"
> {"numy_num5"
> 99
> num5_num6"
> numG_num_ 7"
> Ifitness
> 5.18
> Isharpe"
> 5.72,
> IturnoVer"
> 0.1869
> Idrowdown
> 0.0166
> Ireturns
> 0.1532
> "region
> "USA" }]
> 2025-06-12
> 17:38
> 54.367124 ["0N90932
> Iself: 0 .3721"
> "prod : 0.5908"
> {"numy_num5"
> 349
> InUm5_nUIG I
> 9,
> InumG_num_ 7"
> Ifitness"
> 4.84,
> "sharpe"
> 5.15
> IturnoVer"
> 0.1589
> Idrowdown
> 0182
> Ireturns
> 0.1399
> "region
> "USA"}]
> 2025-06-12
> 17:42
> 44.985536
> ["LIGXVJL"
> Iself: 0 .391
> prod
> 0.4393"
> {"numy_num5"
> 3,
> Inum5
> nUIIG "
> numG_num_7" :
> Ifitness"
> 4.73 ,
> "sharpe"
> 5.0
> IturnoVer"
> 0.0739
> Idrowdown
> 0.0174
> II
> eturns
> I118
> "region
> EUR" }]
> 2025-06-12
> 17:44:37.705004
> ["JWmYXLO"
> Iself
> 0.4454"
> prod : 0 .565"
> {"numy_num5"
> 108
> Inum5
> nUNIG "
> InUmG
> nUII_7" :
> Ifitness"
> 7.03
> Isharpe"
> 6.21,
> IturnoVer"
> 0.0984
> Idrowdown
> 0.0181
> "returns
> 0.1604
> "region
> "EUR"}]
> 2025-06-12
> 17:47:18.424709
> ["SASGeWN
> Iself
> 4633"
> prod
> 0.5423"
> {"numy_num5"
> 33,
> num5_
> nUNIG "
> 2,
> numG_num_ 7"
> Ifitness
> 6.37,
> sharpe
> 5.95
> urnover"
> 0.0703
> Idrowdown
> 0.015
> Ireturns
> 0.1433
> region
> "EUR" }]
> 2025-06-12
> 17:50:06.590224
> ["BEGqWoq
> Iself: 0.4086"
> prod: 0 .6122"
> {"numy_num5"
> 103
> nUI5
> num6 "
> nUNIG
> nUm_ 7"
> 1'
> Ifitness"
> 6.07
> "sharpe"
> 5.6
> IturnoVer"
> 0.121
> Idrowdown
> 0.0147
> Ireturns
> 0.1469
> "region
> IUSA" }]
> 2025-06-12
> 17:52:35
> 750664
> ["YEknGGJ"
> Iself: 0.4068"
> prod: 0 .6149"
> {"numy_num5"
> 124,
> num5_num6
> num6
> num_ 7"
> 1'
> Ifitness"
> 5.92,
> "sharpe"
> 5.51,
> IturnoVer"
> 0.122,
> Idrowdown
> 0.0156
> Ireturns
> 0.1445
> "region
> IUSA"}]
> 2025-06-12
> 18:32:54.321300
> ["Zdlwe63"
> Iself: 0.4085"
> "prod: 0 .6151"
> {"numy_num5"
> 93
> Inum5_num6"
> "numG_num_7" :
> Ifitness"
> "sharpe"
> 5.51,
> IturnoVer"
> 0.1219
> Idrowdown
> 0.0152
> Ireturns
> 0.1439
> "region
> "USA"}]
> 2025-06-12
> 18:39:08.416169
> ["ZdlZEaj
> Iself: 0.4129"
> "prod : 0.596"
> {"numy_num5"
> 62
> InUm5
> num6 "
> InUmG
> num_ 7" :
> Ifitness "
> 5.29 ,
> "sharpe"
> 5.11,
> IturnoVer"
> 0.1218 ,
> Idrowdown
> 0.0171
> Ireturns
> 0.1341
> "region
> IUSA" }]
> 2025-06-12
> 18:42:23.858889
> ["pMZAqGb"
> Iself: 0 .3559"
> "prod : 0 .67"
> {"numy_num5"
> 149
> InUm5_nUIG I
> 4 ,
> InUmG
> num_ 7"
> 1,
> Ifitness
> 5.21, "sharpe
> 5.47
> IturnoVer"
> 0.1463
> Idrowdown
> 0.0219
> Ireturns
> 0.1329
> "region
> IUSA"}]
> 2025-06-12
> 18:45:46.290898
> ["oJzemx2"
> Iself: 0 .3826"
> prod: 0 .635"
> {"numy_num5"
> 489
> num5_
> nUNIG "
> numG_num_7" :
> 1 ,
> Ifitness"
> 5.14,
> "sharpe"
> 5.32,
> IturnoVer"
> 0.1502,
> Idrowdown
> 0187
> Ireturns
> 0.1401
> "region
> "USA"}]
> 2025-06-12
> 18:48:48.395563 ["RlaQaqn
> Iself
> 0.3853"
> "prod: 0 .6169"
> {"numy_num5"
> 531
> nUI5_numG "
> numG_num_ 7" :
> 2,
> Ifitness"
> 5.0
> "sharpe"
> 5.25
> IturnoVer"
> 0.1592,
> Idrowdown
> 0.0197
> "returns
> 0.1444
> "region
> "USA"}]
> 2025-06-12
> 18:50:58.108834
> ["JWXqnM2
> Iself: 0 .3758"
> "prod : 0.58"
> {"num4_num5"
> 236
> InUm5
> num6 "
> InUmG
> num_ 7" :
> Ifitness
> 4.9,
> Isharpe"
> 5.19
> IturnoVer"
> 0.1588
> drowdown
> 0.0178
> returns
> 0.1413
> "region"
> "USA"}]
> 2025-06-12
> 18:56:43.916195
> [ "OMmOKGg
> Iself: 0 .3666"
> "prod : 0.5845 "
> {"numy_num5"
> 200
> InUm5
> num6 "
> InumG_num_ 7"
> Ifitness"
> 4.85
> "sharpe"
> 5.16
> IturnoVer"
> 0 .
> 1582
> Idrowdown
> 0168
> Ireturns
> 0.1399
> ion
> "USA"}]
> 2025-06-12
> 18:59:15.633807
> ["x2zOpPq
> Iself: 0 .3717"
> prod: 0 .5384"
> {"numy_num5"
> 151 ,
> num5_num6
> 9,
> nUNIG
> num_ 7" :
> 0,
> Ifitness"
> 4.82,
> "sharpe"
> 5.13
> IturnoVer"
> 0.154,
> Idrowdown
> 0.0153
> Ireturns
> 136
> Iregion
> IUSA"}]
> 2025-06-12
> 19:03:20.155199
> ["WoXqNTP"
> Iself: 0 .3962"
> "prod: 0 .6529"
> {"numy_num5"
> 140
> nUI5_numG "
> numG_num_7" :
> 1,
> Ifitness"
> 4.81
> "sharpe"
> 5.14
> IturnoVer"
> 0.159
> Idrowdown "
> 0.018
> Ireturns
> 0.1394
> "region
> IUSA" }]
> 2025-06-12
> 19:06:23.912914 ["ggKWJwO"
> Iself: 0 .391"
> "prod
> 0.4393"
> numy_num5"
> num5_
> nUIIG "
> numG_num_7" :
> Ifitness"
> 4.73 ,
> Isharpe"
> 5.0
> IturnoVer"
> 0.0739
> Idrowdown
> 0.0174
> II
> eturns
> I118
> region"
> EUR" }]
> 2025-06-12
> 19:12:50.852481
> ["TVXANBV"
> Iself: 0 .3786"
> "prod: 0 .5838"
> {"numy_num5"
> 231,
> InUm5_nUIG I
> 9,
> InumG_num_ 7"
> Ifitness"
> 4.7, "sharpe
> 5.06
> IturnoVer"
> 0.1595
> Idrowdown
> 0179
> "returns
> 0.1379
> "region
> "USA"}]
> 2025-06-12
> 19:15:50.158108 ["IZng8MQ"
> Iself: 0.4047"
> prod: 0.4842"
> {"numy_num5"
> 1,
> num5_
> nUNIG "
> numG_num_7" :
> Ifitness"
> 5.01,
> "sharpe"
> 5.19
> IturnoVer"
> 0.1264,
> Idrowdown
> 0.0146
> Ireturns
> 1178
> "region
> ASI" }]
> 2025-06-12
> 19:19:19.434581
> ["0J9A276"
> Iself: 0.4639"
> "prod: 0 .5369"
> {"numy_num5"
> 22,
> Inum5_num6"
> "numG_num_7" :
> Ifitness"
> 4.59
> "sharpe"
> 4.94,
> IturnoVer"
> 0.0779
> Idrowdown "
> 0.0161
> "returns
> 0.1081
> "region
> "EUR"}]
> 2025-06-12
> 19:24:21.991511
> ["kWLblek"
> Iself: 0.445"
> prod
> 0.6031
> {"
> numy_num5"
> 300
> num5_num6"
> 9,
> numG_num_ 7"
> 1 ,
> Ifitness
> 4.5,
> "sharpe"
> 4.75
> IturnoVer"
> 0.0779
> Idrowdown
> 0.0254
> Ireturns
> 0.1122
> region
> "EUR" }]
> 2025-06-12
> 19:32:32.859106
> ["0J9A276"
> Iself: 0.4639"
> "prod: 0.5369"
> {"numy_num5"
> 22,
> Inum5_num6"
> 2,
> "numG_num_7" :
> Ifitness
> 4.59
> Isharpe"
> 4.94
> IturnoVer"
> 0.0779
> Idrowdown
> 0161
> "returns
> 0.1081
> "region
> EUR" }]
> 2025-06-12
> 19:32:46.939500
> ["kWLblek"
> Iself: 0.445"
> prod : 0 .6031"
> numy_num5"
> 300
> num5_num6"
> numG_num_7"
> 1 ,
> Ifitness"
> 4.5,
> "sharpe"
> 4.75
> IturnoVer"
> 0.0779
> "drowdown
> 0.0254
> Ireturns
> 0.1122,
> Iregion"
> "EUR"}]
> 32,
> 91,
> ureg


**⚠️⚠️：**

**在降低prod时，注意不要过拟合 ：）**

---

### 帖子 #60: 【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化
- **主帖链接**: https://support.worldquantbrain.com【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化_32763493267863.md
- **讨论数**: 16

fit>5,prod小于5的SA,是小伙伴们都追求的梦中SA。那么如何快速找到有比较大的可能可以调整到低于0.5的SA进行调整呢？

这里的思路是：

```
1、获取已有的SA列表（包含详细信息）；（代码回测super alpha，    这样你就可以有超级多的superalpha 选择了）2、检查自相关性（参考 顾问 KZ79256 (Rank 21) 大佬的帖子），如果自相关超过5，就跳过检查生产相关3、检查生产相关性，并获取每个相关性区间的alpha数，最后存入本地文件。  根据check结果，选择fit>5, 0.4-0.5区间，0.5-0.6区间相对较少的SA，尝试降低prod,   这样成功的概率会比较高。
```

代码如下：（本地自相关性的计算，这里就不详细描述了，可自行参考  **顾问 KZ79256 (Rank 21)** 大佬的帖子 ； [看这里]([L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md) )

```
    # 加载本地pnl数据    os_alpha_ids, os_alpha_rets = load_data()    start=0    # alpha_infos是个列表，列表中是每个alpha的详细信息，可通过get_alpha函数获取    alpha_infos = alpha_infos[start:]    for i  in range(0,len(alpha_infos)):         alpha_info=alpha_infos[i]         alpha_id=alpha_info["id"]         print(f"begin check id :{i+start}, {alpha_id}")         # append_to_file 函数是个记录日志的函数         append_to_file("check.log",f"begin check id :{i+start}, {alpha_id} ",True)         date_create=alpha_info["dateCreated"]         fitness = alpha_info['is']['fitness']         sharpe = alpha_info['is']['sharpe']         turnover = alpha_info['is']['turnover']         margin = alpha_info['is']['margin']         drawdown = alpha_info['is']['drawdown']         returns = alpha_info['is']['returns']         region = alpha_info['settings']['region']         checks=alpha_info["is"]["checks"]         LOW_2Y_SHARPE=0         for item in checks:             if item["name"] == LOW_2Y_SHARPE:                 LOW_2Y_SHARPE=item["value"]         #检查自相关         corr_id,corr_value=calc_self_corr( alpha_id, os_alpha_rets,  os_alpha_ids,None,True,None)         f = float(corr_value)         rounded_f = round(f, 4)         if   rounded_f >=0.5:             print(f"selfcorr more than 0.5,and self > 0.7 ;switch {alpha_id};  self:{rounded_f}")             set_alpha_properties(alpha_id=alpha_id, name=f"SELF_CORR_{rounded_f}", color="BLUE")             continue         num4_num5=0         num5_num6=0         num6_num7=0         while True:         # 获取prod 相关性值            response=my_get(f"[链接已屏蔽])            if response != None:                try:                    res=response.json()                    prod=res["max"]                    for list_ in res["records"]:                    # 获取相关性在0.4-0.5区间的alpha数                        if list_[0] == 0.4 and list_[1] == 0.5:                            num4_num5=list_[2]                    # 获取相关性在0.5-0.6区间的alpha数                        if list_[0] == 0.5 and list_[1] == 0.6:                            num5_num6=list_[2]                    # 获取相关性在0.6-0.7区间的alpha数                        if list_[0] == 0.6 and list_[1] == 0.7:                            num6_num7=list_[2]                    break                except Exception as e:                    print(f"get prod failed,try again")            sleep(10)         if  fitness > 5 and prod < 0.5 and sharpe >5 and LOW_2Y_SHARPE >=5:             print(f"begin submit alpha: {alpha_id}")             append_to_file("submit.log",f"fit>5,prod<5的alpha id: {alpha_id}",True)             #submit_alpha(s,alpha_id)         com_des=alpha_info["combo"]["description"]         select_des=alpha_info["selection"]["description"]         set_alpha_properties(alpha_id,f"PROD_{str(prod)}","RED")         a=json.dumps([alpha_id,f"self:{rounded_f}",f"prod:{prod}",{"num4_num5":num4_num5,"num5_num6":num5_num6,"num6_num_7":num6_num7,"fitness":fitness,"sharpe":sharpe,"turnover":turnover,"drowdown":drawdown,"returns":returns,"region":region}])         append_to_file("res.txt",a,True)    print(f"finish check")
```

check的结果res.txt如下：


> [!NOTE] [图片 OCR 识别内容]
> 2025-06-12
> 17:18:49.033085
> ["ZdwgZj3"
> Iself
> 0.4133"
> prod
> 0.5911"
> {"num4_num5"
> 12
> Inum5
> nUNIG "
> InUmG
> nUII_7" :
> Ifitness"
> 6.97
> "sharpe"
> 5.88 ,
> IturnoVer"
> 0.1201 ,
> Idrowdown
> 0206
> "returns
> 0.1754
> "region
> "USA" }]
> 2025-06-12
> 17:20:41.196934
> ["mOAPIGS"
> Isel
> :0.4013"
> prod: 0 .5793"
> {"numy_num5"
> 15,
> num5_num6"
> numG_num_ 7" :
> Ifitness
> 6 .87,
> larpe
> 5.85
> IturnoVer"
> 0.1209
> Idrowdown
> 0.0219
> Ireturns
> 0.1726
> "region
> "USA" }]
> 2025-06-12
> 17:23:05
> 790562
> [ "ZXREaqw
> Iself: 0.4629"
> prod: 0
> 5445"
> {"numy_num5"
> 38
> "num5_num6 "
> 2,
> "numG_num_ 7"
> Ifitness"
> 6.75
> "sharpe"
> 6.15
> IturnoVer"
> 0.0957
> Idrowdown
> 0153
> "returns
> 0.1509
> "region
> IEUR" } ]
> 2025-06-12
> 17:25:26.983654
> ["7VOdAEZ"
> Iself: 0.4146"
> 'prod: 0 .6266"
> {"numy_num5"
> 8181,
> num5_num6"
> "num6_num_7" :
> 1,
> Ifitness"
> 5.27,
> "sharpe"
> 6.12,
> IturnoVer"
> 0.1773
> Idrowdown "
> 0.01
> 39
> Ireturns
> 0.1314
> "region"
> IUSA" }]
> 2025-06-12
> 17:35:47.662261
> ["EgYgQkg"
> Iself
> 0.3476"
> prod
> 0.5529"
> {"num4_num5"
> num5
> num6 "
> num6
> nUm_ 7"
> Ifitness"
> 5.2,
> sharpe"
> 6.38
> IturnoVer"
> 0.1901
> Idrowdown
> 0094
> returns
> 0.1265
> Iregion"
> "USA"}]
> 2025-06-12
> 17:36:08
> 724525
> ["601v677"
> Iself
> 0.3422"
> prod
> 0.5644"
> {"numy_num5"
> 99
> num5_num6"
> numG_num_ 7"
> Ifitness
> 5.18
> Isharpe"
> 5.72,
> IturnoVer"
> 0.1869
> Idrowdown
> 0.0166
> Ireturns
> 0.1532
> "region
> "USA" }]
> 2025-06-12
> 17:38
> 54.367124 ["0N90932
> Iself: 0 .3721"
> "prod : 0.5908"
> {"numy_num5"
> 349
> InUm5_nUIG I
> 9,
> InumG_num_ 7"
> Ifitness"
> 4.84,
> "sharpe"
> 5.15
> IturnoVer"
> 0.1589
> Idrowdown
> 0182
> Ireturns
> 0.1399
> "region
> "USA"}]
> 2025-06-12
> 17:42
> 44.985536
> ["LIGXVJL"
> Iself: 0 .391
> prod
> 0.4393"
> {"numy_num5"
> 3,
> Inum5
> nUIIG "
> numG_num_7" :
> Ifitness"
> 4.73 ,
> "sharpe"
> 5.0
> IturnoVer"
> 0.0739
> Idrowdown
> 0.0174
> II
> eturns
> I118
> "region
> EUR" }]
> 2025-06-12
> 17:44:37.705004
> ["JWmYXLO"
> Iself
> 0.4454"
> prod : 0 .565"
> {"numy_num5"
> 108
> Inum5
> nUNIG "
> InUmG
> nUII_7" :
> Ifitness"
> 7.03
> Isharpe"
> 6.21,
> IturnoVer"
> 0.0984
> Idrowdown
> 0.0181
> "returns
> 0.1604
> "region
> "EUR"}]
> 2025-06-12
> 17:47:18.424709
> ["SASGeWN
> Iself
> 4633"
> prod
> 0.5423"
> {"numy_num5"
> 33,
> num5_
> nUNIG "
> 2,
> numG_num_ 7"
> Ifitness
> 6.37,
> sharpe
> 5.95
> urnover"
> 0.0703
> Idrowdown
> 0.015
> Ireturns
> 0.1433
> region
> "EUR" }]
> 2025-06-12
> 17:50:06.590224
> ["BEGqWoq
> Iself: 0.4086"
> prod: 0 .6122"
> {"numy_num5"
> 103
> nUI5
> num6 "
> nUNIG
> nUm_ 7"
> 1'
> Ifitness"
> 6.07
> "sharpe"
> 5.6
> IturnoVer"
> 0.121
> Idrowdown
> 0.0147
> Ireturns
> 0.1469
> "region
> IUSA" }]
> 2025-06-12
> 17:52:35
> 750664
> ["YEknGGJ"
> Iself: 0.4068"
> prod: 0 .6149"
> {"numy_num5"
> 124,
> num5_num6
> num6
> num_ 7"
> 1'
> Ifitness"
> 5.92,
> "sharpe"
> 5.51,
> IturnoVer"
> 0.122,
> Idrowdown
> 0.0156
> Ireturns
> 0.1445
> "region
> IUSA"}]
> 2025-06-12
> 18:32:54.321300
> ["Zdlwe63"
> Iself: 0.4085"
> "prod: 0 .6151"
> {"numy_num5"
> 93
> Inum5_num6"
> "numG_num_7" :
> Ifitness"
> "sharpe"
> 5.51,
> IturnoVer"
> 0.1219
> Idrowdown
> 0.0152
> Ireturns
> 0.1439
> "region
> "USA"}]
> 2025-06-12
> 18:39:08.416169
> ["ZdlZEaj
> Iself: 0.4129"
> "prod : 0.596"
> {"numy_num5"
> 62
> InUm5
> num6 "
> InUmG
> num_ 7" :
> Ifitness "
> 5.29 ,
> "sharpe"
> 5.11,
> IturnoVer"
> 0.1218 ,
> Idrowdown
> 0.0171
> Ireturns
> 0.1341
> "region
> IUSA" }]
> 2025-06-12
> 18:42:23.858889
> ["pMZAqGb"
> Iself: 0 .3559"
> "prod : 0 .67"
> {"numy_num5"
> 149
> InUm5_nUIG I
> 4 ,
> InUmG
> num_ 7"
> 1,
> Ifitness
> 5.21, "sharpe
> 5.47
> IturnoVer"
> 0.1463
> Idrowdown
> 0.0219
> Ireturns
> 0.1329
> "region
> IUSA"}]
> 2025-06-12
> 18:45:46.290898
> ["oJzemx2"
> Iself: 0 .3826"
> prod: 0 .635"
> {"numy_num5"
> 489
> num5_
> nUNIG "
> numG_num_7" :
> 1 ,
> Ifitness"
> 5.14,
> "sharpe"
> 5.32,
> IturnoVer"
> 0.1502,
> Idrowdown
> 0187
> Ireturns
> 0.1401
> "region
> "USA"}]
> 2025-06-12
> 18:48:48.395563 ["RlaQaqn
> Iself
> 0.3853"
> "prod: 0 .6169"
> {"numy_num5"
> 531
> nUI5_numG "
> numG_num_ 7" :
> 2,
> Ifitness"
> 5.0
> "sharpe"
> 5.25
> IturnoVer"
> 0.1592,
> Idrowdown
> 0.0197
> "returns
> 0.1444
> "region
> "USA"}]
> 2025-06-12
> 18:50:58.108834
> ["JWXqnM2
> Iself: 0 .3758"
> "prod : 0.58"
> {"num4_num5"
> 236
> InUm5
> num6 "
> InUmG
> num_ 7" :
> Ifitness
> 4.9,
> Isharpe"
> 5.19
> IturnoVer"
> 0.1588
> drowdown
> 0.0178
> returns
> 0.1413
> "region"
> "USA"}]
> 2025-06-12
> 18:56:43.916195
> [ "OMmOKGg
> Iself: 0 .3666"
> "prod : 0.5845 "
> {"numy_num5"
> 200
> InUm5
> num6 "
> InumG_num_ 7"
> Ifitness"
> 4.85
> "sharpe"
> 5.16
> IturnoVer"
> 0 .
> 1582
> Idrowdown
> 0168
> Ireturns
> 0.1399
> ion
> "USA"}]
> 2025-06-12
> 18:59:15.633807
> ["x2zOpPq
> Iself: 0 .3717"
> prod: 0 .5384"
> {"numy_num5"
> 151 ,
> num5_num6
> 9,
> nUNIG
> num_ 7" :
> 0,
> Ifitness"
> 4.82,
> "sharpe"
> 5.13
> IturnoVer"
> 0.154,
> Idrowdown
> 0.0153
> Ireturns
> 136
> Iregion
> IUSA"}]
> 2025-06-12
> 19:03:20.155199
> ["WoXqNTP"
> Iself: 0 .3962"
> "prod: 0 .6529"
> {"numy_num5"
> 140
> nUI5_numG "
> numG_num_7" :
> 1,
> Ifitness"
> 4.81
> "sharpe"
> 5.14
> IturnoVer"
> 0.159
> Idrowdown "
> 0.018
> Ireturns
> 0.1394
> "region
> IUSA" }]
> 2025-06-12
> 19:06:23.912914 ["ggKWJwO"
> Iself: 0 .391"
> "prod
> 0.4393"
> numy_num5"
> num5_
> nUIIG "
> numG_num_7" :
> Ifitness"
> 4.73 ,
> Isharpe"
> 5.0
> IturnoVer"
> 0.0739
> Idrowdown
> 0.0174
> II
> eturns
> I118
> region"
> EUR" }]
> 2025-06-12
> 19:12:50.852481
> ["TVXANBV"
> Iself: 0 .3786"
> "prod: 0 .5838"
> {"numy_num5"
> 231,
> InUm5_nUIG I
> 9,
> InumG_num_ 7"
> Ifitness"
> 4.7, "sharpe
> 5.06
> IturnoVer"
> 0.1595
> Idrowdown
> 0179
> "returns
> 0.1379
> "region
> "USA"}]
> 2025-06-12
> 19:15:50.158108 ["IZng8MQ"
> Iself: 0.4047"
> prod: 0.4842"
> {"numy_num5"
> 1,
> num5_
> nUNIG "
> numG_num_7" :
> Ifitness"
> 5.01,
> "sharpe"
> 5.19
> IturnoVer"
> 0.1264,
> Idrowdown
> 0.0146
> Ireturns
> 1178
> "region
> ASI" }]
> 2025-06-12
> 19:19:19.434581
> ["0J9A276"
> Iself: 0.4639"
> "prod: 0 .5369"
> {"numy_num5"
> 22,
> Inum5_num6"
> "numG_num_7" :
> Ifitness"
> 4.59
> "sharpe"
> 4.94,
> IturnoVer"
> 0.0779
> Idrowdown "
> 0.0161
> "returns
> 0.1081
> "region
> "EUR"}]
> 2025-06-12
> 19:24:21.991511
> ["kWLblek"
> Iself: 0.445"
> prod
> 0.6031
> {"
> numy_num5"
> 300
> num5_num6"
> 9,
> numG_num_ 7"
> 1 ,
> Ifitness
> 4.5,
> "sharpe"
> 4.75
> IturnoVer"
> 0.0779
> Idrowdown
> 0.0254
> Ireturns
> 0.1122
> region
> "EUR" }]
> 2025-06-12
> 19:32:32.859106
> ["0J9A276"
> Iself: 0.4639"
> "prod: 0.5369"
> {"numy_num5"
> 22,
> Inum5_num6"
> 2,
> "numG_num_7" :
> Ifitness
> 4.59
> Isharpe"
> 4.94
> IturnoVer"
> 0.0779
> Idrowdown
> 0161
> "returns
> 0.1081
> "region
> EUR" }]
> 2025-06-12
> 19:32:46.939500
> ["kWLblek"
> Iself: 0.445"
> prod : 0 .6031"
> numy_num5"
> 300
> num5_num6"
> numG_num_7"
> 1 ,
> Ifitness"
> 4.5,
> "sharpe"
> 4.75
> IturnoVer"
> 0.0779
> "drowdown
> 0.0254
> Ireturns
> 0.1122,
> Iregion"
> "EUR"}]
> 32,
> 91,
> ureg


**⚠️⚠️：**

**在降低prod时，注意不要过拟合 ：）**

---

### 帖子 #61: PnL = ∑(Robustness * Creativity)
- **主帖链接**: 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md
- **讨论数**: 36

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


---

### 帖子 #62: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md
- **讨论数**: 36

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


---

### 帖子 #63: 【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化
- **主帖链接**: 【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化.md
- **讨论数**: 3

之前自动化回测superalpha的时候，发现有时候select条件可能过于严，导致跑出来的sa,select的数量过少，一直想给回测的代码加上确认select数量不低于指定阈值的功能，上周末终于实现了，有需要的小伙伴可以参考下：

```
def get_super_selection_count(    simulation_data):    """    向 api.worldquantbrain.com 发送 GET 请求，获取 count 字段值simulation_data 是个dict，回测superalpha时的 json 参数值    """    url = "[链接已屏蔽]    global s    select=simulation_data["selection"]    region=simulation_data["settings"]["region"]    delay= simulation_data["settings"]["delay"]    instrumentType=simulation_data["settings"]["instrumentType"]    limit=10    selectionLimit=simulation_data["settings"]["selectionLimit"]    selectionHandling= simulation_data["settings"]["selectionHandling"]    select_endoce=urllib.parse.quote(select)    print("select_count:")    querys=f"settings.instrumentType={instrumentType}&settings.region={region}&settings.delay={str(delay)}&limit={str(limit)}&selectionLimit={str(selectionLimit)}&selectionHandling={selectionHandling}&selection={select_endoce}"    try:        response = s.get(f"{url}{querys}",timeout=15)        if response != None:            json_response = response.json()            return json_response["count"]  # 返回 count 字段值    except requests.exceptions.RequestException as e:        print(f"请求失败: {e}")        return None    except ValueError:        print("响应内容不是合法的 JSON")        return None
```

上面的函数放到代码中，然后在发送回测super alpha之前，加上以下代码：

```
alpha_lowset_num=100       select_count=get_super_selection_count(sim_data)if select_count != None and select_count < alpha_lowset_num :    print(f"select alpha 数量少于 {alpha_lowset_num},跳过回测 {select_count},switch")    print(json.dumps(sim_data_list))   # 下面再添加一行代码，用于跳出你本次回测这个superalpha 的代码，比如continue 等
```


> [!NOTE] [图片 OCR 识别内容]
> brain_api_url
> https: //api .worldquantbrain. com
> def
> submit_task(task,
> X,
> y):
> nonlocal
> last_login_time
> nonlocal
> active_tasks
> nonlocal
> tasks_to_submit
> global
> 讦f
> 
> 11:
> if y not in [1,2]:
> append_to_file(sim_log,f" SWITCH pool {X} task {y}" )
> return
> 31nonr
> [11oCc1 m
> 104
> f"tosllon; lonCtoI)7
> 凸 讨
> Ioct 笃 [7介0061
> 笃 [公 +osl
> sim_data_list
> energte_sim_data(task, region,
> universe
> neut, limit_alpha_num)
> sim_data_list
> sim_data_list_[O]
> #print(sim_data_list )
> select_count-get_super_selection_count(sim_data_list)
> print(select_count)
> if select_count
> !=
> None and select_count
> 100
> append_to_file(sim
> f"select less
> 190, continue:
> count:
> {select_count} , switch
> )
> append_to_file("select_to_low. txt" , json . dumps(sim_data_list))
> return
> simulation_response-my_post(url=-f' {brain_api_url}/simulations
> data-sim_data_list, sim_log-sim
> timeout=ls)
> print(url)
> print(sim_data_list)
> if simulation_response
> None
> try:
> simulation_progress_url
> simulation_response.headers[ ' Location
> 」
> active_tasks . append((x ,
> y,
> simulation_progress_url 
> time.time(), task))
> print(f"pool
> len 。
> {lencalpha_pools )} pool: {x}
> task {y} post
> done
> append_to_file(sim
> f"pool len:
> {len(alpha_pools )} pool: {X}
> task {y} post done
> )
> except Exception as e:
> 109,
> 1o9
> 109,


---

### 帖子 #64: 【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化
- **主帖链接**: https://support.worldquantbrain.com【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化_32985437982231.md
- **讨论数**: 3

之前自动化回测superalpha的时候，发现有时候select条件可能过于严，导致跑出来的sa,select的数量过少，一直想给回测的代码加上确认select数量不低于指定阈值的功能，上周末终于实现了，有需要的小伙伴可以参考下：

```
def get_super_selection_count(    simulation_data):    """    向 api.worldquantbrain.com 发送 GET 请求，获取 count 字段值simulation_data 是个dict，回测superalpha时的 json 参数值    """    url = "[链接已屏蔽]    global s    select=simulation_data["selection"]    region=simulation_data["settings"]["region"]    delay= simulation_data["settings"]["delay"]    instrumentType=simulation_data["settings"]["instrumentType"]    limit=10    selectionLimit=simulation_data["settings"]["selectionLimit"]    selectionHandling= simulation_data["settings"]["selectionHandling"]    select_endoce=urllib.parse.quote(select)    print("select_count:")    querys=f"settings.instrumentType={instrumentType}&settings.region={region}&settings.delay={str(delay)}&limit={str(limit)}&selectionLimit={str(selectionLimit)}&selectionHandling={selectionHandling}&selection={select_endoce}"    try:        response = s.get(f"{url}{querys}",timeout=15)        if response != None:            json_response = response.json()            return json_response["count"]  # 返回 count 字段值    except requests.exceptions.RequestException as e:        print(f"请求失败: {e}")        return None    except ValueError:        print("响应内容不是合法的 JSON")        return None
```

上面的函数放到代码中，然后在发送回测super alpha之前，加上以下代码：

```
alpha_lowset_num=100       select_count=get_super_selection_count(sim_data)if select_count != None and select_count < alpha_lowset_num :    print(f"select alpha 数量少于 {alpha_lowset_num},跳过回测 {select_count},switch")    print(json.dumps(sim_data_list))   # 下面再添加一行代码，用于跳出你本次回测这个superalpha 的代码，比如continue 等
```


> [!NOTE] [图片 OCR 识别内容]
> brain_api_url
> https: //api .worldquantbrain. com
> def
> submit_task(task,
> X,
> y):
> nonlocal
> last_login_time
> nonlocal
> active_tasks
> nonlocal
> tasks_to_submit
> global
> 讦f
> 
> 11:
> if y not in [1,2]:
> append_to_file(sim_log,f" SWITCH pool {X} task {y}" )
> return
> 31nonr
> [11oCc1 m
> 104
> f"tosllon; lonCtoI)7
> 凸 讨
> Ioct 笃 [7介0061
> 笃 [公 +osl
> sim_data_list
> energte_sim_data(task, region,
> universe
> neut, limit_alpha_num)
> sim_data_list
> sim_data_list_[O]
> #print(sim_data_list )
> select_count-get_super_selection_count(sim_data_list)
> print(select_count)
> if select_count
> !=
> None and select_count
> 100
> append_to_file(sim
> f"select less
> 190, continue:
> count:
> {select_count} , switch
> )
> append_to_file("select_to_low. txt" , json . dumps(sim_data_list))
> return
> simulation_response-my_post(url=-f' {brain_api_url}/simulations
> data-sim_data_list, sim_log-sim
> timeout=ls)
> print(url)
> print(sim_data_list)
> if simulation_response
> None
> try:
> simulation_progress_url
> simulation_response.headers[ ' Location
> 」
> active_tasks . append((x ,
> y,
> simulation_progress_url 
> time.time(), task))
> print(f"pool
> len 。
> {lencalpha_pools )} pool: {x}
> task {y} post
> done
> append_to_file(sim
> f"pool len:
> {len(alpha_pools )} pool: {X}
> task {y} post done
> )
> except Exception as e:
> 109,
> 1o9
> 109,


---

### 帖子 #65: 【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享
- **主帖链接**: 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享.md
- **讨论数**: 15

今天是第4天了吧，对于为啥连续几天SA 都拿满60刀，我自己也挺困惑的。说说我的SA 怎么做的吧，小伙伴们应该感兴趣吧，我也不确定是不是正确的道路。

这个思路是我ACE主题（上周）最后几天手搓SA的时候，灵光一闪想到的。得益于游戏王的turnover分层思想，我一开始想着turnover分层的，但是ACE主题，turnover分层选择的结果不是很理想。看了learn的文档，尝试了下datacategories 分层，从我最熟悉datacategories开始尝试，试了下，效果挺好的。后面我尝试了不同datacategories的组合，可能是我选的datacategories 表现比较好，组合起来都挺不错的。

昨天 7月7号的SA 选择的思路

```
1、我先看看主题和🔝的这个datacategories 有多少alpha，然后我给datacategories 限制条件，比如op，turnover，prod，设置个大概的范围，看这个datacategories有多少，然后决定要不要再更细致的分层。这样完成了一个datacategories2、然后继续另一个独立的datacategories 设置，和第一个一样。3、最后2个或者2个以上的datacategories 加起来（|| 连接，）这样就相当于你保证选择了不同的datacategories 。
```

最后给大家看看最近4天的SA base吧

[图片 (图片已丢失)]

如果我的分享对你有帮助，记得点赞哦～～

---

### 帖子 #66: 【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享
- **主帖链接**: https://support.worldquantbrain.com【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享_33316845356439.md
- **讨论数**: 15

今天是第4天了吧，对于为啥连续几天SA 都拿满60刀，我自己也挺困惑的。说说我的SA 怎么做的吧，小伙伴们应该感兴趣吧，我也不确定是不是正确的道路。

这个思路是我ACE主题（上周）最后几天手搓SA的时候，灵光一闪想到的。得益于游戏王的turnover分层思想，我一开始想着turnover分层的，但是ACE主题，turnover分层选择的结果不是很理想。看了learn的文档，尝试了下datacategories 分层，从我最熟悉datacategories开始尝试，试了下，效果挺好的。后面我尝试了不同datacategories的组合，可能是我选的datacategories 表现比较好，组合起来都挺不错的。

昨天 7月7号的SA 选择的思路

```
1、我先看看主题和🔝的这个datacategories 有多少alpha，然后我给datacategories 限制条件，比如op，turnover，prod，设置个大概的范围，看这个datacategories有多少，然后决定要不要再更细致的分层。这样完成了一个datacategories2、然后继续另一个独立的datacategories 设置，和第一个一样。3、最后2个或者2个以上的datacategories 加起来（|| 连接，）这样就相当于你保证选择了不同的datacategories 。
```

最后给大家看看最近4天的SA base吧


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/04/2025
> Super:
> 60.00
> Regular:
> 9.59
> Total:
> 69.59
> 40
> 20
> 2.Jul
> 3.Jul
> 4.Jul
> 5.Jul
> 6.Jul
> 7.Jul
> Period
> Regular
> Super
> Total


如果我的分享对你有帮助，记得点赞哦～～

---

### 帖子 #67: 【ValueFactor预测器】滚动3个月SA，掌握你最近3个月提交alpha情况_python版代码优化
- **主帖链接**: 【ValueFactor预测器】滚动3个月SA掌握你最近3个月提交alpha情况_python版代码优化.md
- **讨论数**: 9

首先感谢weijie老师提出的idea:

选择你最近3个月提交的alpha 组SA，根据SA的表现衡量你过去3个月提交的alpha的质量，sa的表现可以视作value factor的预告。之后，你提交的alpah，需要和过去3个月组合的sa的相关性低。

那么如何滚动3个月的alpha组合sa呢？

根据alpha提交的时间，添加年份-月份的tags，然后在组sa的时候，选择tags是指定月份的alpha，进行回测，根据sa的表现，衡量你最近3个月提交的sa质量，代码如下：

```
import jsonimport sysimport timefrom datetime import datetimefrom time import sleepimport requestsfrom requests.adapters import HTTPAdapterfrom requests.packages.urllib3.util.retry import Retrydef load_config(file_path):    """从指定路径f加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user=config["user"]passwd=config["password"]def login():    username = user    password =  passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    max_try = 3    retry=0    while True:        try:            response = s.post('[链接已屏蔽])            if response.status_code  in [200,201]:                print(f"login success")                return s        except Exception as e:            print(f"login err :{e}")            print(f"login failed ,sleep 5 ,try again")            sleep(5)        retry +=1        if retry > max_try:            break    return Nonedef get_submited_alphas_three_month(s,start_date,end_date,region,only_ppa=True):    # only_ppa 设置是否只获取ppa的alpha设置tags，后续组sa时根据tags值的年份月份筛选    print(f"正在获取{start_date}到{end_date}内，{region}地区的ppa alpha")    url=f"[链接已屏蔽]    count=0    print(url)    count=s.get(url).json()['count']    print(count)    alpha_list=[]    for i in range(0,count,100):        url=f"[链接已屏蔽]        response=s.get(url).json()        for alpha in response['results']:            if only_ppa:                flag=0                for item in alpha["classifications"]:                    if item['name']=='Power Pool Alpha':                        flag=1                        break                if flag==1:                    alpha_list.append(alpha)            else:                alpha_list.append(alpha)    print(f"在时间范围{start_date}到{end_date}内，{region}地区，获取了 {len(alpha_list)}个ppa alpha")    return alpha_list# 对所有alpha 在原有tags列表上增加年份+月份的tags，如2025-05def set_alpha_property_list(s,alpha_list):    count = 0    for alpha in alpha_list:        alpha_id=alpha['id']        print(f"正在设置第{count}个alpha 的属性,{alpha_id}; 总alpha数量{len(alpha_list)}")        tags=alpha['tags']        name=alpha['name']        date_created=alpha['dateCreated']        color=alpha['color']        description=alpha['regular']['description']        dt = datetime.fromisoformat(date_created.replace('Z', '+00:00'))        year_month = dt.strftime('%Y-%m')  # "2025-07"        print(year_month)        if year_month in tags:            continue        else:            tags.append(year_month)        category=alpha['category']        if category is None:            category=None        if color is None:            color=None        if name is None:            name=None        print(tags)        params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": description},        "combo": {"description": description},        "selection": {"description": description}}        response = s.patch( "[链接已屏蔽] + alpha_id, json=params)        # print(response.json())        sleep(1)        count+=1    return Truedef make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade):    simulation_data={    "type": "SUPER",    "settings": {        "maxTrade": maxtrade,        "nanHandling": "ON",        "instrumentType": "EQUITY",        "delay": delay,        "universe": universe,        "truncation": 0.08,        "unitHandling": "VERIFY",        "selectionLimit": select_num,        "selectionHandling": select_handle,        "testPeriod": "P0D",        "componentActivation": "IS",        "pasteurization": "ON",        "region": region,        "language": "FASTEXPR",        "decay": decay,        "neutralization": neut_,        "visualization": False    },    "combo": str(combo),    "selection": select}    return simulation_datadef simulate_sa(s,simulation_data):    brain_api_url = '[链接已屏蔽]    try:        simulation_response=s.post(f'{brain_api_url}/simulations',json=simulation_data)        # print(simulation_response.json())    except Exception as e:        print(f"模拟sa失败:{e}")        return None    simulation_progress_url = simulation_response.headers['Location']    print(simulation_progress_url)    while True:        simulation_progress_response=s.get(simulation_progress_url)        retry_after = simulation_progress_response.headers.get("Retry-After", 0)        if str(retry_after) == '0':            status = simulation_progress_response.json().get("status", "not_found")            if status == "COMPLETE":                res_=simulation_progress_response.json()                alpha_id=res_["alpha"]                print(f"最近3个月的ppa组成的sa模拟完成,alpha_id:{alpha_id}")                break        else:            print(f"processing,begin sleep {float(retry_after)}")            time.sleep(float(retry_after))    return alpha_id# 对指定日期范围内的ppa 设置年月标签来确认是否是指定时间范围的ppas = login()#设置你想滚动组合sa的月份start_date='2025-04-01'end_date='2025-06-30'data_range=['2025-04','2025-05','2025-06']# 地区，universeregion='USA'universe='TOP3000'delay=1decay=0select_handle='POSITIVE'select_num=300maxtrade='ON'alpha_list=get_submited_alphas_three_month(s,start_date,end_date,region)print(f"在时间范围{start_date}到{end_date}内，提交了 {len(alpha_list)}个ppa alpha")print(alpha_list[0]['id'],)set_alpha_property_list(s,alpha_list)select=f'(own) && ((in(tags,"{data_range[0]}")) || (in(tags,"{data_range[1]}"))|| (in(tags,"{data_range[2]}")))'print(select)combo=1alpha_ids=[]for decay in  [0]:    ##可根据需要对多种neut回测查看sa表现    for neut_ in  ["CROWDING","REVERSION_AND_MOMENTUM"]:        simulation_data=make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade)        alpha_id=simulate_sa(s,simulation_data)        alpha_ids.append(alpha_id)print(f"完成回测,alpha_id如下")print(alpha_ids)print(f"最近3个月， {region} 提交的ppa 组合的sa表现如下")for alpha_id in alpha_ids:    res=s.get(f"[链接已屏蔽])    res_json=res.json()    sharpe=res_json['is']['sharpe']    fitness=res_json['is']['fitness']    return_=res_json['is']['returns']    drawdown=res_json['is']['drawdown']    margin=res_json['is']['margin']    turnover=res_json['is']['turnover']    neut=res_json['settings']['neutralization']    decay=res_json['settings']['decay']    print(f"{alpha_id}: sharpe: {sharpe}, fitness: {fitness}, return: {return_}, drawdown: {drawdown}, margin: {margin}, turnover: {turnover}, neut: {neut},decay: {decay}")
```

输出结果如下：

```
完成回测,alpha_id如下['12Q7xez', 'E2XGKG0']最近3个月提交的ppa USA 组合的sa表现如下12Q7xez: sharpe: 3.71, fitness: 5.36, return: 0.2609, drawdown: 0.0647, margin: 0.00873, turnover: 0.0598, neut: CROWDING,decay: 0E2XGKG0: sharpe: 4.11, fitness: 5.85, return: 0.2533, drawdown: 0.0429, margin: 0.006105, turnover: 0.083, neut: REVERSION_AND_MOMENTUM,decay: 0
```

---

### 帖子 #68: 【ValueFactor预测器】滚动3个月SA，掌握你最近3个月提交alpha情况_python版代码优化
- **主帖链接**: https://support.worldquantbrain.com【ValueFactor预测器】滚动3个月SA掌握你最近3个月提交alpha情况_python版代码优化_33715194478615.md
- **讨论数**: 9

首先感谢weijie老师提出的idea:

选择你最近3个月提交的alpha 组SA，根据SA的表现衡量你过去3个月提交的alpha的质量，sa的表现可以视作value factor的预告。之后，你提交的alpah，需要和过去3个月组合的sa的相关性低。

那么如何滚动3个月的alpha组合sa呢？

根据alpha提交的时间，添加年份-月份的tags，然后在组sa的时候，选择tags是指定月份的alpha，进行回测，根据sa的表现，衡量你最近3个月提交的sa质量，代码如下：

```
import jsonimport sysimport timefrom datetime import datetimefrom time import sleepimport requestsfrom requests.adapters import HTTPAdapterfrom requests.packages.urllib3.util.retry import Retrydef load_config(file_path):    """从指定路径f加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user=config["user"]passwd=config["password"]def login():    username = user    password =  passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    max_try = 3    retry=0    while True:        try:            response = s.post('[链接已屏蔽])            if response.status_code  in [200,201]:                print(f"login success")                return s        except Exception as e:            print(f"login err :{e}")            print(f"login failed ,sleep 5 ,try again")            sleep(5)        retry +=1        if retry > max_try:            break    return Nonedef get_submited_alphas_three_month(s,start_date,end_date,region,only_ppa=True):    # only_ppa 设置是否只获取ppa的alpha设置tags，后续组sa时根据tags值的年份月份筛选    print(f"正在获取{start_date}到{end_date}内，{region}地区的ppa alpha")    url=f"[链接已屏蔽]    count=0    print(url)    count=s.get(url).json()['count']    print(count)    alpha_list=[]    for i in range(0,count,100):        url=f"[链接已屏蔽]        response=s.get(url).json()        for alpha in response['results']:            if only_ppa:                flag=0                for item in alpha["classifications"]:                    if item['name']=='Power Pool Alpha':                        flag=1                        break                if flag==1:                    alpha_list.append(alpha)            else:                alpha_list.append(alpha)    print(f"在时间范围{start_date}到{end_date}内，{region}地区，获取了 {len(alpha_list)}个ppa alpha")    return alpha_list# 对所有alpha 在原有tags列表上增加年份+月份的tags，如2025-05def set_alpha_property_list(s,alpha_list):    count = 0    for alpha in alpha_list:        alpha_id=alpha['id']        print(f"正在设置第{count}个alpha 的属性,{alpha_id}; 总alpha数量{len(alpha_list)}")        tags=alpha['tags']        name=alpha['name']        date_created=alpha['dateCreated']        color=alpha['color']        description=alpha['regular']['description']        dt = datetime.fromisoformat(date_created.replace('Z', '+00:00'))        year_month = dt.strftime('%Y-%m')  # "2025-07"        print(year_month)        if year_month in tags:            continue        else:            tags.append(year_month)        category=alpha['category']        if category is None:            category=None        if color is None:            color=None        if name is None:            name=None        print(tags)        params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": description},        "combo": {"description": description},        "selection": {"description": description}}        response = s.patch( "[链接已屏蔽] + alpha_id, json=params)        # print(response.json())        sleep(1)        count+=1    return Truedef make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade):    simulation_data={    "type": "SUPER",    "settings": {        "maxTrade": maxtrade,        "nanHandling": "ON",        "instrumentType": "EQUITY",        "delay": delay,        "universe": universe,        "truncation": 0.08,        "unitHandling": "VERIFY",        "selectionLimit": select_num,        "selectionHandling": select_handle,        "testPeriod": "P0D",        "componentActivation": "IS",        "pasteurization": "ON",        "region": region,        "language": "FASTEXPR",        "decay": decay,        "neutralization": neut_,        "visualization": False    },    "combo": str(combo),    "selection": select}    return simulation_datadef simulate_sa(s,simulation_data):    brain_api_url = '[链接已屏蔽]    try:        simulation_response=s.post(f'{brain_api_url}/simulations',json=simulation_data)        # print(simulation_response.json())    except Exception as e:        print(f"模拟sa失败:{e}")        return None    simulation_progress_url = simulation_response.headers['Location']    print(simulation_progress_url)    while True:        simulation_progress_response=s.get(simulation_progress_url)        retry_after = simulation_progress_response.headers.get("Retry-After", 0)        if str(retry_after) == '0':            status = simulation_progress_response.json().get("status", "not_found")            if status == "COMPLETE":                res_=simulation_progress_response.json()                alpha_id=res_["alpha"]                print(f"最近3个月的ppa组成的sa模拟完成,alpha_id:{alpha_id}")                break        else:            print(f"processing,begin sleep {float(retry_after)}")            time.sleep(float(retry_after))    return alpha_id# 对指定日期范围内的ppa 设置年月标签来确认是否是指定时间范围的ppas = login()#设置你想滚动组合sa的月份start_date='2025-04-01'end_date='2025-06-30'data_range=['2025-04','2025-05','2025-06']# 地区，universeregion='USA'universe='TOP3000'delay=1decay=0select_handle='POSITIVE'select_num=300maxtrade='ON'alpha_list=get_submited_alphas_three_month(s,start_date,end_date,region)print(f"在时间范围{start_date}到{end_date}内，提交了 {len(alpha_list)}个ppa alpha")print(alpha_list[0]['id'],)set_alpha_property_list(s,alpha_list)select=f'(own) && ((in(tags,"{data_range[0]}")) || (in(tags,"{data_range[1]}"))|| (in(tags,"{data_range[2]}")))'print(select)combo=1alpha_ids=[]for decay in  [0]:    ##可根据需要对多种neut回测查看sa表现    for neut_ in  ["CROWDING","REVERSION_AND_MOMENTUM"]:        simulation_data=make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade)        alpha_id=simulate_sa(s,simulation_data)        alpha_ids.append(alpha_id)print(f"完成回测,alpha_id如下")print(alpha_ids)print(f"最近3个月， {region} 提交的ppa 组合的sa表现如下")for alpha_id in alpha_ids:    res=s.get(f"[链接已屏蔽])    res_json=res.json()    sharpe=res_json['is']['sharpe']    fitness=res_json['is']['fitness']    return_=res_json['is']['returns']    drawdown=res_json['is']['drawdown']    margin=res_json['is']['margin']    turnover=res_json['is']['turnover']    neut=res_json['settings']['neutralization']    decay=res_json['settings']['decay']    print(f"{alpha_id}: sharpe: {sharpe}, fitness: {fitness}, return: {return_}, drawdown: {drawdown}, margin: {margin}, turnover: {turnover}, neut: {neut},decay: {decay}")
```

输出结果如下：

```
完成回测,alpha_id如下['12Q7xez', 'E2XGKG0']最近3个月提交的ppa USA 组合的sa表现如下12Q7xez: sharpe: 3.71, fitness: 5.36, return: 0.2609, drawdown: 0.0647, margin: 0.00873, turnover: 0.0598, neut: CROWDING,decay: 0E2XGKG0: sharpe: 4.11, fitness: 5.85, return: 0.2533, drawdown: 0.0429, margin: 0.006105, turnover: 0.083, neut: REVERSION_AND_MOMENTUM,decay: 0
```

---

### 帖子 #69: 【实战记录】基于信号灯系统的 Alpha 自动化研究——EUR fund_holdings_panel 数据集探索
- **主帖链接**: 【实战记录】基于信号灯系统的 Alpha 自动化研究EUR fund_holdings_panel 数据集探索.md
- **讨论数**: 1

### 前言

本文记录了使用"信号灯系统"进行 Alpha 研究的完整实战过程。该系统源自社区帖子《用AI 跑了几百次回测还找不到优质信号》，核心思路是用统计学方法指导 AI 的探索方向。

**原帖链接** :  [[L2] 【经验分享】用AI 跑了几百次回测还找不到优质信号到底是池塘没鱼还是鱼饵不对燃烧token给 AI 装上导航置顶的论坛精选.md]([L2] 【经验分享】用AI 跑了几百次回测还找不到优质信号到底是池塘没鱼还是鱼饵不对燃烧token给 AI 装上导航置顶的论坛精选.md)

### 一、研究背景

**数据集** : EUR/TOP2500/fund_holdings_panel（30个字段）

#### 信号灯系统简介

- 🟢 GREEN: 方向有信号，加码深挖
- 🟡 YELLOW: 有潜力但证据不足，谨慎继续
- 🔴 RED: 信号弱，做结构性改动
- ⚫ DEAD: 及时止损，换方向

### 二、研究过程

#### 第一轮：广泛探索（27个表达式）

均值 Sharpe: -0.24，最高: 0.64

 **信号灯: 🔴 RED → 行动: 结构性改动**

字段分析发现 holder_account_total 最差(Sharpe=-0.88)，应放弃

#### 第二轮：聚焦潜力字段（28个表达式）

均值 Sharpe: 0.27，最高: 0.97

 **关键发现** : stable_boundary_trade_count_21d 字段有显著信号

#### 第三轮：深度优化（20个表达式）

通过 2Y_SHARPE 检查: 9个

#### 第四轮：参数微调

最高 Sharpe: 0.93，2Y_SHARPE: 2.28

### 三、最终成果

**最佳表达式** :

```
ts_decay_linear(group_zscore(vec_avg(stable_boundary_trade_count_21d), sector), 20)
```

Sharpe=0.93, 2Y_SHARPE=2.28, Fitness=0.48

#### 高潜力表达式列表

表达式
Sharpe
2Y_SHARPE

ts_decay_linear(group_zscore(...), 20)
0.93
2.28

group_zscore(ts_decay_linear(..., 20), sector)
0.93
2.27

group_zscore(ts_decay_linear(..., 60), sector)
0.92
2.27

ts_mean(group_zscore(...), 20)
0.91
2.27

ts_decay_linear(group_zscore(...), 60)
0.91
2.44

### 四、信号灯系统验证

轮次
均值Sharpe
信号灯
行动

第一轮
-0.24
🔴 RED
结构性改动

第二轮
0.27
🟡 YELLOW
继续深挖

第三轮
0.39
🟡 YELLOW
参数优化

第四轮
0.84
🟢 GREEN
完成

### 五、关键发现

1. 有效信号字段: stable_boundary_trade_count_21d（稳定边界交易计数）
2. 最佳算子组合: ts_decay_linear + group_zscore
3. 经济学解释: 该字段代表基金的持久性仓位变化，反映机构投资者信息优势

### 六、信号灯系统价值

- 避免盲目探索，明确指导方向调整
- 区分"数据没信号"和"表达式没写对"
- 防误杀护栏，不过早放弃有潜力方向

### 七、致谢

感谢原帖作者分享的信号灯系统思路！

**原帖链接** :  [点击查看原帖]([L2] 【经验分享】用AI 跑了几百次回测还找不到优质信号到底是池塘没鱼还是鱼饵不对燃烧token给 AI 装上导航置顶的论坛精选.md)

---

### 帖子 #70: 【实战记录】基于信号灯系统的 Alpha 自动化研究——EUR fund_holdings_panel 数据集探索
- **主帖链接**: https://support.worldquantbrain.com【实战记录】基于信号灯系统的 Alpha 自动化研究EUR fund_holdings_panel 数据集探索_41049370096663.md
- **讨论数**: 1

### 前言

本文记录了使用"信号灯系统"进行 Alpha 研究的完整实战过程。该系统源自社区帖子《用AI 跑了几百次回测还找不到优质信号》，核心思路是用统计学方法指导 AI 的探索方向。

**原帖链接** :  [[L2] 【经验分享】用AI 跑了几百次回测还找不到优质信号到底是池塘没鱼还是鱼饵不对燃烧token给 AI 装上导航置顶的论坛精选_39319955780887.md]([L2] 【经验分享】用AI 跑了几百次回测还找不到优质信号到底是池塘没鱼还是鱼饵不对燃烧token给 AI 装上导航置顶的论坛精选_39319955780887.md)

### 一、研究背景

**数据集** : EUR/TOP2500/fund_holdings_panel（30个字段）

#### 信号灯系统简介

- 🟢 GREEN: 方向有信号，加码深挖
- 🟡 YELLOW: 有潜力但证据不足，谨慎继续
- 🔴 RED: 信号弱，做结构性改动
- ⚫ DEAD: 及时止损，换方向

### 二、研究过程

#### 第一轮：广泛探索（27个表达式）

均值 Sharpe: -0.24，最高: 0.64

 **信号灯: 🔴 RED → 行动: 结构性改动**

字段分析发现 holder_account_total 最差(Sharpe=-0.88)，应放弃

#### 第二轮：聚焦潜力字段（28个表达式）

均值 Sharpe: 0.27，最高: 0.97

 **关键发现** : stable_boundary_trade_count_21d 字段有显著信号

#### 第三轮：深度优化（20个表达式）

通过 2Y_SHARPE 检查: 9个

#### 第四轮：参数微调

最高 Sharpe: 0.93，2Y_SHARPE: 2.28

### 三、最终成果

**最佳表达式** :

```
ts_decay_linear(group_zscore(vec_avg(stable_boundary_trade_count_21d), sector), 20)
```

Sharpe=0.93, 2Y_SHARPE=2.28, Fitness=0.48

#### 高潜力表达式列表

表达式
Sharpe
2Y_SHARPE

ts_decay_linear(group_zscore(...), 20)
0.93
2.28

group_zscore(ts_decay_linear(..., 20), sector)
0.93
2.27

group_zscore(ts_decay_linear(..., 60), sector)
0.92
2.27

ts_mean(group_zscore(...), 20)
0.91
2.27

ts_decay_linear(group_zscore(...), 60)
0.91
2.44

### 四、信号灯系统验证

轮次
均值Sharpe
信号灯
行动

第一轮
-0.24
🔴 RED
结构性改动

第二轮
0.27
🟡 YELLOW
继续深挖

第三轮
0.39
🟡 YELLOW
参数优化

第四轮
0.84
🟢 GREEN
完成

### 五、关键发现

1. 有效信号字段: stable_boundary_trade_count_21d（稳定边界交易计数）
2. 最佳算子组合: ts_decay_linear + group_zscore
3. 经济学解释: 该字段代表基金的持久性仓位变化，反映机构投资者信息优势

### 六、信号灯系统价值

- 避免盲目探索，明确指导方向调整
- 区分"数据没信号"和"表达式没写对"
- 防误杀护栏，不过早放弃有潜力方向

### 七、致谢

感谢原帖作者分享的信号灯系统思路！

**原帖链接** :  [点击查看原帖]([L2] 【经验分享】用AI 跑了几百次回测还找不到优质信号到底是池塘没鱼还是鱼饵不对燃烧token给 AI 装上导航置顶的论坛精选_39319955780887.md)

---

### 帖子 #71: ❌ 不允许 - 服务器端不可用
- **主帖链接**: 【经验分享】Python Alpha 快速上手指南 - 从踩坑到成功回测.md
- **讨论数**: 1

## 背景

最近在学习 Python Alpha，通过阅读官方文档和论坛前辈的经验帖，成功完成了第一个 Python Alpha 的回测。本文整理了学习过程中的关键经验和踩过的坑，希望对后来者有帮助。

## 参考资料

感谢以下资料的作者：

- 官方文档： [Getting Started with Brain Python Alphas]([链接已屏蔽])
- [Python Alpha 平台限制粗略小结，请大佬指正](../顾问 RM49262 (Rank 30)/[Commented] Python Alpha 平台限制粗略小结请大佬指正.md)  - 非常详细的限制总结
- [经验分享-尝试Python alpha]([L2] 【经验分享】尝试Python alpha经验分享_40737593669911.md)  - 包含完整的代码示例

## 核心限制（踩坑重点！）

### 1. 参数限制 - 最容易踩的坑

**unitHandling 和 nanHandling 必须省略！**  这是我踩的第一个大坑。

```
# ❌ 错误写法 - 会导致 400 错误
settings = {
    "unitHandling": "OFF",
    "nanHandling": "OFF",
    ...
}

# ✅ 正确写法 - 不要传这两个参数
settings = {
    "lookback": 110,
    "language": "PYTHON",
    ...
}
```

### 2. lookback 限制

- 必须 ≤ 115，超过直接 FAIL
- 建议用  **110** （115 偶发 FAIL）
- 与 FastExpr 无限历史窗口不同，Python 只能看到 lookback+1 行数据

### 3. 数据类型限制

- 支持：MATRIX 类型 ✅
- 不支持：VECTOR 类型 ❌（需要 vec_avg 聚合，Python 无法处理）
- 不支持：GROUP 类型 ❌
- int32 字段有 sentinel 值（-2147483648），需要手动替换为 NaN

### 4. 代码限制

```
# ✅ 允许
from brain.alphas import alpha
import numpy as np

# ❌ 不允许 - 服务器端不可用
from brain import Brain, BrainCache
from brain.models import SimulationSettings
```

其他要点：

- 数据数组 **只读** ，修改前必须  `.copy()`
- 返回必须是  **float32 ndarray** ，形状  `[n_instruments]`

## 完整的 Python Alpha 模板

```
from brain.alphas import alpha
import numpy as np
import numpy.typing as npt

def pasteurize(a, u):
    a = a.copy()
    a[~u.astype(bool)] = np.nan
    return a

def neutralize(a):
    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)
    return a - np.mean(a0)

def scale(a):
    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)
    norm = np.linalg.norm(a0, ord=1)
    return a / norm if norm > 0 else a

@alpha(data=["returns"], store=[])
def my_alpha(data, store) -> npt.NDArray[np.float32]:
    signal = -np.nanmean(data.returns, axis=0)
    signal = pasteurize(signal, data.universe[-1])
    signal = scale(neutralize(signal))
    return signal.astype(np.float32)
```

## 验证结果

使用上述模板成功完成回测：

- Alpha ID: d5Qp1GWv
- Sharpe: 0.63
- Turnover: 0.25

## 总结

Python Alpha 虽然有一些限制，但灵活性更高。关键要点：

1. **unitHandling 和 nanHandling 不要传**
2. **lookback ≤ 115**
3. **只 import alpha**
4. **数据只读，返回 float32**

希望这篇分享对大家有帮助！欢迎交流讨论。

---

### 帖子 #72: ❌ 不允许 - 服务器端不可用
- **主帖链接**: https://support.worldquantbrain.com【经验分享】Python Alpha 快速上手指南 - 从踩坑到成功回测_40934305707159.md
- **讨论数**: 1

## 背景

最近在学习 Python Alpha，通过阅读官方文档和论坛前辈的经验帖，成功完成了第一个 Python Alpha 的回测。本文整理了学习过程中的关键经验和踩过的坑，希望对后来者有帮助。

## 参考资料

感谢以下资料的作者：

- 官方文档： [Getting Started with Brain Python Alphas]([链接已屏蔽])
- [Python Alpha 平台限制粗略小结，请大佬指正]([L2] Python Alpha 平台限制粗略小结请大佬指正_40742727142679.md)  - 非常详细的限制总结
- [经验分享-尝试Python alpha]([L2] 【经验分享】尝试Python alpha经验分享_40737593669911.md)  - 包含完整的代码示例

## 核心限制（踩坑重点！）

### 1. 参数限制 - 最容易踩的坑

**unitHandling 和 nanHandling 必须省略！**  这是我踩的第一个大坑。

```
# ❌ 错误写法 - 会导致 400 错误
settings = {
    "unitHandling": "OFF",
    "nanHandling": "OFF",
    ...
}

# ✅ 正确写法 - 不要传这两个参数
settings = {
    "lookback": 110,
    "language": "PYTHON",
    ...
}
```

### 2. lookback 限制

- 必须 ≤ 115，超过直接 FAIL
- 建议用  **110** （115 偶发 FAIL）
- 与 FastExpr 无限历史窗口不同，Python 只能看到 lookback+1 行数据

### 3. 数据类型限制

- 支持：MATRIX 类型 ✅
- 不支持：VECTOR 类型 ❌（需要 vec_avg 聚合，Python 无法处理）
- 不支持：GROUP 类型 ❌
- int32 字段有 sentinel 值（-2147483648），需要手动替换为 NaN

### 4. 代码限制

```
# ✅ 允许
from brain.alphas import alpha
import numpy as np

# ❌ 不允许 - 服务器端不可用
from brain import Brain, BrainCache
from brain.models import SimulationSettings
```

其他要点：

- 数据数组 **只读** ，修改前必须  `.copy()`
- 返回必须是  **float32 ndarray** ，形状  `[n_instruments]`

## 完整的 Python Alpha 模板

```
from brain.alphas import alpha
import numpy as np
import numpy.typing as npt

def pasteurize(a, u):
    a = a.copy()
    a[~u.astype(bool)] = np.nan
    return a

def neutralize(a):
    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)
    return a - np.mean(a0)

def scale(a):
    a0 = np.nan_to_num(a, nan=0, posinf=0, neginf=0)
    norm = np.linalg.norm(a0, ord=1)
    return a / norm if norm > 0 else a

@alpha(data=["returns"], store=[])
def my_alpha(data, store) -> npt.NDArray[np.float32]:
    signal = -np.nanmean(data.returns, axis=0)
    signal = pasteurize(signal, data.universe[-1])
    signal = scale(neutralize(signal))
    return signal.astype(np.float32)
```

## 验证结果

使用上述模板成功完成回测：

- Alpha ID: d5Qp1GWv
- Sharpe: 0.63
- Turnover: 0.25

## 总结

Python Alpha 虽然有一些限制，但灵活性更高。关键要点：

1. **unitHandling 和 nanHandling 不要传**
2. **lookback ≤ 115**
3. **只 import alpha**
4. **数据只读，返回 float32**

希望这篇分享对大家有帮助！欢迎交流讨论。

---

### 帖子 #73: 使用mcp+ai挖掘alpha过程中节约token的小技巧经验分享
- **主帖链接**: 使用mcpai挖掘alpha过程中节约token的小技巧经验分享.md
- **讨论数**: 8

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

---

### 帖子 #74: 使用mcp+ai挖掘alpha过程中节约token的小技巧经验分享
- **主帖链接**: https://support.worldquantbrain.com使用mcpai挖掘alpha过程中节约token的小技巧经验分享_38013569192983.md
- **讨论数**: 8

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

---

### 帖子 #75: 📊 2025年Value Factor趋势分析报告
- **主帖链接**: 利用brain mcp的 value factor traendScore 分析alpha提交情况.md
- **讨论数**: 6

今天老师培训，mcp新增的value factor traendScore 可以回顾总结下自己提交alpha的分散性，数量，以及atom 比例。有点想知道每3个月的alpha提交对比情况。由于使用mcp的tools来获取每3个月提交的alpha数据，等待的时间过长了。我自己把mcp 分析value factor traendScore的相关代码拷贝了出来，自己修改了下。先通过脚本获取了AI分析需要的数据，然后再让mcp根据已获取的数据来分析每3个月的value factor traendScore情况，对比。具体结果如下：
# 📊 2025年Value Factor趋势分析报告

## 数据概览

| 时间范围 | 多样性分数 | 总Alpha数 | Atom标签数 | 金字塔类别数 | S_A      | S_P    | S_H |
|----------    |-----------------|----------------|------------------|--------------------|----------|----------|--------|
| **2-4月** |      0.052     |       85        |     42             |      18              | 0.494  | 0.123  | 0.856 |
| **3-5月** |      0.066     |      113       |     56             |      22              | 0.496  | 0.151  | 0.888 |
| **4-6月** |      0.089     |      130       |     83             |      23              |  0.638 | 0.158  | 0.881 |
| **5-7月** |      0.131     |      129       |     100           |      28              | 0.775  | 0.192  | 0.882 |
| **6-8月** |      0.175     |      139       |     109           |      36              | 0.784  | 0.247  | 0.903 |

```
关键趋势分析1. 多样性分数 (Diversity Score)整体趋势: 持续上升，表现优异2-4月 → 6-8月: 从0.052提升到0.175 (+236.5%)最大提升: 5-7月期间 (+47.2%)平均月增长率: 约39.4%2. Alpha数量变化波动特点: 85 → 113 → 130 → 129 → 139策略转变: 从数量转向质量，显示策略优化过程质量提升: 在数量增长中保持高质量3. Atom标签比例 (S_A)2-4月: 49.4% (基础水平)3-5月: 49.6% (小幅提升)4-6月: 63.8% (大幅提升)5-7月: 77.5% (峰值)6-8月: 78.4% (保持高位)4. 金字塔覆盖率 (S_P)2-4月: 12.3% (18/146)3-5月: 15.1% (22/146)4-6月: 15.8% (23/146)5-7月: 19.2% (28/146)6-8月: 24.7% (36/146) ⭐5. 分布均匀性 (S_H)整体趋势: 持续提升2-4月: 85.6%6-8月: 90.3% (+5.5%)
```

2.19号成为有条件顾问，到目前为止一共经历了4次vf更新，vf 均保持0.9+，我的alpha提交策略应该是走在正确的道路上的；

希望上面的分析总结，能给小伙伴们一些启发，也祝各位小伙伴的VF +++

---

### 帖子 #76: 📊 2025年Value Factor趋势分析报告
- **主帖链接**: https://support.worldquantbrain.com利用brain mcp的 value factor traendScore 分析alpha提交情况_34408473241623.md
- **讨论数**: 6

今天老师培训，mcp新增的value factor traendScore 可以回顾总结下自己提交alpha的分散性，数量，以及atom 比例。有点想知道每3个月的alpha提交对比情况。由于使用mcp的tools来获取每3个月提交的alpha数据，等待的时间过长了。我自己把mcp 分析value factor traendScore的相关代码拷贝了出来，自己修改了下。先通过脚本获取了AI分析需要的数据，然后再让mcp根据已获取的数据来分析每3个月的value factor traendScore情况，对比。具体结果如下：
# 📊 2025年Value Factor趋势分析报告

## 数据概览

| 时间范围 | 多样性分数 | 总Alpha数 | Atom标签数 | 金字塔类别数 | S_A      | S_P    | S_H |
|----------    |-----------------|----------------|------------------|--------------------|----------|----------|--------|
| **2-4月** |      0.052     |       85        |     42             |      18              | 0.494  | 0.123  | 0.856 |
| **3-5月** |      0.066     |      113       |     56             |      22              | 0.496  | 0.151  | 0.888 |
| **4-6月** |      0.089     |      130       |     83             |      23              |  0.638 | 0.158  | 0.881 |
| **5-7月** |      0.131     |      129       |     100           |      28              | 0.775  | 0.192  | 0.882 |
| **6-8月** |      0.175     |      139       |     109           |      36              | 0.784  | 0.247  | 0.903 |

```
关键趋势分析1. 多样性分数 (Diversity Score)整体趋势: 持续上升，表现优异2-4月 → 6-8月: 从0.052提升到0.175 (+236.5%)最大提升: 5-7月期间 (+47.2%)平均月增长率: 约39.4%2. Alpha数量变化波动特点: 85 → 113 → 130 → 129 → 139策略转变: 从数量转向质量，显示策略优化过程质量提升: 在数量增长中保持高质量3. Atom标签比例 (S_A)2-4月: 49.4% (基础水平)3-5月: 49.6% (小幅提升)4-6月: 63.8% (大幅提升)5-7月: 77.5% (峰值)6-8月: 78.4% (保持高位)4. 金字塔覆盖率 (S_P)2-4月: 12.3% (18/146)3-5月: 15.1% (22/146)4-6月: 15.8% (23/146)5-7月: 19.2% (28/146)6-8月: 24.7% (36/146) ⭐5. 分布均匀性 (S_H)整体趋势: 持续提升2-4月: 85.6%6-8月: 90.3% (+5.5%)
```

2.19号成为有条件顾问，到目前为止一共经历了4次vf更新，vf 均保持0.9+，我的alpha提交策略应该是走在正确的道路上的；

希望上面的分析总结，能给小伙伴们一些启发，也祝各位小伙伴的VF +++

---

### 帖子 #77: 回测遇到difficult ,took too much resource 怎么办？代码优化
- **主帖链接**: 回测遇到difficult took too much resource 怎么办代码优化.md
- **讨论数**: 7

平台更新或者服务不稳定的时候，代码回测时会经常遇到下面2种回测ERROR的情况：

第一种：

```
{    "id": "xxx",    "type": "REGULAR",    "status": "ERROR",    "message": "There was an error while running the simulation.Please try again or contact BRAIN support if this problem persists."}
```

第二种：

```
{"id": "xxx","type": "REGULAR","status": "ERROR","message": "Your simulation probably took too much resource."}
```

第一种，一般是平台的原因导致的，回测的表达式是没问题的。如果经常遇到这种而不处理直接跳过，可能会遗漏一些有信号的alpha。可以在遇到的时候，将表达式存到json文件，后续补统一回测。

第二种，可能是平台的问题，也可能是表达式确实消耗的资源过大。这种错误，可以通过减少子槽的个数来避免，具体减到多少，看实际情况，一般见到6，7个子槽，就可以了。

分享下代码判断上面2种错误的处理

```
def append_to_jsonl(filename, data):"""追加数据到JSONL文件"""withopen(filename, 'a', encoding='utf-8') as f:    json.dump(data, f, ensure_ascii=False)    f.write('\n') # 每行一个JSON对象
```

```
length=len(simulation_progress.json()["children"])for child_ in range(0,length):    child=simulation_progress.json()["children"][child_]    try:        res=my_get(f"[链接已屏蔽])        err_mes1='There was an error while running the simulation. Please try again or contact BRAIN support if this problem persists'        err_mes2="Your simulation probably took too much resource"        if res.json()["status"] == "ERROR" :            if err_mes1 in res.json()['message']:                append_to_jsonl('brain_difficult.json',[region,universe,neut,alpha_pools[tx][ty]])            if err_mes2 in res.json()['message']:                append_to_jsonl('brain_too_much_resource.json',[region,universe,neut,alpha_pools[tx][ty]])
```

---

### 帖子 #78: 回测遇到difficult ,took too much resource 怎么办？代码优化
- **主帖链接**: https://support.worldquantbrain.com回测遇到difficult took too much resource 怎么办代码优化_36355931527703.md
- **讨论数**: 7

平台更新或者服务不稳定的时候，代码回测时会经常遇到下面2种回测ERROR的情况：

第一种：

```
{    "id": "xxx",    "type": "REGULAR",    "status": "ERROR",    "message": "There was an error while running the simulation.Please try again or contact BRAIN support if this problem persists."}
```

第二种：

```
{"id": "xxx","type": "REGULAR","status": "ERROR","message": "Your simulation probably took too much resource."}
```

第一种，一般是平台的原因导致的，回测的表达式是没问题的。如果经常遇到这种而不处理直接跳过，可能会遗漏一些有信号的alpha。可以在遇到的时候，将表达式存到json文件，后续补统一回测。

第二种，可能是平台的问题，也可能是表达式确实消耗的资源过大。这种错误，可以通过减少子槽的个数来避免，具体减到多少，看实际情况，一般见到6，7个子槽，就可以了。

分享下代码判断上面2种错误的处理

```
def append_to_jsonl(filename, data):"""追加数据到JSONL文件"""withopen(filename, 'a', encoding='utf-8') as f:    json.dump(data, f, ensure_ascii=False)    f.write('\n') # 每行一个JSON对象
```

```
length=len(simulation_progress.json()["children"])for child_ in range(0,length):    child=simulation_progress.json()["children"][child_]    try:        res=my_get(f"[链接已屏蔽])        err_mes1='There was an error while running the simulation. Please try again or contact BRAIN support if this problem persists'        err_mes2="Your simulation probably took too much resource"        if res.json()["status"] == "ERROR" :            if err_mes1 in res.json()['message']:                append_to_jsonl('brain_difficult.json',[region,universe,neut,alpha_pools[tx][ty]])            if err_mes2 in res.json()['message']:                append_to_jsonl('brain_too_much_resource.json',[region,universe,neut,alpha_pools[tx][ty]])
```

---

### 帖子 #79: 如何保持回测不中断代码优化
- **主帖链接**: 如何保持回测不中断代码优化.md
- **讨论数**: 2

在并发限制相同的情况下，如何保持回测不中断，稳定每日的回测量？这里分享下我的方法。

由于我个人使用的是linux系统来跑脚本的，但是考虑到可能比较多的人是用windows系统的，所以，除了linux系统的方法，也会分享下windows系统回测不中断的方法

**针对linux 系统：**

在linux系统上，通过下面的命令，可以查到回测的进程是否在运行中

```
(my_worldquanbrain) [root@VMxxx]# ps -ef |grep {回测脚本的名字}|grep -v greproot      803874       1  0 20:59 ?        00:00:03 python second_order.py
```

那么，可以通过定时任务 判断脚本进程，那么通过下面的脚本，就可以在回测脚本挂了的情况下，启动另外一个回测脚本运行，这里我的回测脚本完整路径是 /root/world_quan/start_new_py.sh

```
#!/bin/bashnum=$(ps -ef |grep py|grep {脚本的文件名}|grep -v grep | wc -l )＃如果num w为0，说明回测的脚本进程没有运行中if [ $num -eq 0 ];then    source  /root/my_worldquanbrain/bin/activate # 加载python虚拟环境    cd  /root/my_worldquanbrain/dir1 # 进入脚本所在目录    nohup python 新的回测脚本文件名 >>2.log 2>&1 & #启动新的回测脚本在后台运行    # 启动新的回测脚本后，将启动脚本重命名，避免重复启动    mv /root/world_quan/start_new_py.sh /root/world_quan/start_new_py.sh.bakfi
```

将上面的脚本放入定时任务中运行：

```
echo "*/1  * * * * bash -c -l 'sh /root/world_quan/start_new_py.sh'"
```

**针对windows系统：**

我用的是pycharm软件跑脚本的，这里以pycharm举例子，我当前在pycharm 中运行了

回测脚本1.py ，同时我还把下面的脚本也启动，当回测脚本1.py 进程挂了之后，这个脚本会启动新的回测脚本2.py继续新的回测

```
import psutilimport osimport subprocessimport time#　判断回测脚本是否在运行中def is_script_running(script_name):    for process in psutil.process_iter(['pid', 'name', 'cmdline']):        if process.info['name'] == 'python.exe' or process.info['name'] == 'pythonw.exe':            if process.info['cmdline'] and script_name in process.info['cmdline'][1]:                return True    return Falsedef start_script(script_path):    try:    # 获取脚本所在的目录        script_dir = os.path.dirname(script_path)        # 获取脚本的名称        script_name = os.path.basename(script_path)        # 切换到脚本所在的目录        os.chdir(script_dir)        # 创建一个文件来保存输出        log_file = os.path.join(script_dir, 'log.log')        with open(log_file, 'a') as f:            # 启动脚本并将输出重定向到文件            process = subprocess.Popen(                ['python', script_name],                    cwd=script_dir,                   stdout=f,                   stderr=subprocess.STDOUT              )        print(f"Started script: {script_path}")        print(f"Output will be logged to: {log_file}")    except Exception as e:        print(f"Failed to start script: {e}")script_name = '回测脚本1.py'＃　备用的回测脚本路径script_path = r'D:\PycharmProjects\worldquantbrain\src\usa\analystxx\回测脚本2.py'while True:    if is_script_running(script_name):        print(f"{script_name} is running.")    else:        print(f"{script_name} is not running. Starting the script...")        start_script(script_path)        break    time.sleep(60)
```

还有个优化回测速度的tip:

有时候一个回测的post 持续了很久都没完成，怎么办？我一般是在发送post成功后，记录url，pool ID，task id的同时也把发送post的时间记录下来，每次判断post是否成功了的同时，也会判断下这个post simulate持续的时间多长了，如果超过我设置的时长，我就delete掉这个post,同时记录下delete 的simulate task到文件中，后续统一重新跑下这些task.


> [!NOTE] [图片 OCR 识别内容]
> VVL LUUuaIULaLy)
> ]#
> Cat
> active_second_pool.txt
> [[379
> 0
> 'https : / /api
> Worldquantbrain . com /simulations /2dUIO03524YO8MmQGFR3KWUI
> 1744466754.9898155]
> [377
> 1,
> "https : / /api
> Worldquantbrain
> Com/simula
> tions /26xBxTSrV4J4SYRdrAfaEzK"
> 1744466760.7057726]
> [377
> 2,
> "https: //api
> worldquantbrain . com/simulations /3gQGLFfXI4EMcamlmynFsNh
> 1744466778 .849996
> 3]
> [377
> 3
> "https:
> /api
> worldquantbrain _
> com/simulations /4erXHegXRSG3CyVSyhA33ZK"
> 1744466780 .369543]
> [377
> 4
> "https:
> /api .worldquantbrain . com/simu
> lations /
> IYEPj9S3ESaUbdNI3q5XcCQL '
> 1744466782.7577677] _
> [377 
> 5
> "https: / /api
> worldquantbrain . com /
> simuiations /3ZSGOMIqd4HTbSVIONgektwb"
> 1744466800.39
> 69886]
> [377
> 6
> "https:
> /api
> woridquantbrain-
> Com/
> simuiations /ZkZgUfcyg5jugxmySdtVMwp"
> 1744466805 .7206995]
> [377
> 7
> https:
> /api. worldquantbrain . com
> /simulations /34f5Zhhl84ItaaWnJoVdqzJ"
> 1744466829.6342309]
> [377
> 8
> "https:
> /api
> Worldquantbrain _
> com/simulations
> ZmOplTeayynLgSRVAciioAF
> 1744466831
> 368594]
> [377
> 9
> "https:
> /api
> Worldquantbrain _
> com/simulations /3ABs4r52D5jdbeBtMgOQSSR"
> 1744466835.3777065]1
> CmV_Worldauanbrain ) [root@VM-4-1G-opencloudos
> option8
> other  universe1#


如果我的分享对你有帮助，帮忙点个赞，谢谢~~

---

### 帖子 #80: 如何保持回测不中断代码优化
- **主帖链接**: https://support.worldquantbrain.com如何保持回测不中断代码优化_31365306856855.md
- **讨论数**: 2

在并发限制相同的情况下，如何保持回测不中断，稳定每日的回测量？这里分享下我的方法。

由于我个人使用的是linux系统来跑脚本的，但是考虑到可能比较多的人是用windows系统的，所以，除了linux系统的方法，也会分享下windows系统回测不中断的方法

**针对linux 系统：**

在linux系统上，通过下面的命令，可以查到回测的进程是否在运行中

```
(my_worldquanbrain) [root@VMxxx]# ps -ef |grep {回测脚本的名字}|grep -v greproot      803874       1  0 20:59 ?        00:00:03 python second_order.py
```

那么，可以通过定时任务 判断脚本进程，那么通过下面的脚本，就可以在回测脚本挂了的情况下，启动另外一个回测脚本运行，这里我的回测脚本完整路径是 /root/world_quan/start_new_py.sh

```
#!/bin/bashnum=$(ps -ef |grep py|grep {脚本的文件名}|grep -v grep | wc -l )＃如果num w为0，说明回测的脚本进程没有运行中if [ $num -eq 0 ];then    source  /root/my_worldquanbrain/bin/activate # 加载python虚拟环境    cd  /root/my_worldquanbrain/dir1 # 进入脚本所在目录    nohup python 新的回测脚本文件名 >>2.log 2>&1 & #启动新的回测脚本在后台运行    # 启动新的回测脚本后，将启动脚本重命名，避免重复启动    mv /root/world_quan/start_new_py.sh /root/world_quan/start_new_py.sh.bakfi
```

将上面的脚本放入定时任务中运行：

```
echo "*/1  * * * * bash -c -l 'sh /root/world_quan/start_new_py.sh'"
```

**针对windows系统：**

我用的是pycharm软件跑脚本的，这里以pycharm举例子，我当前在pycharm 中运行了

回测脚本1.py ，同时我还把下面的脚本也启动，当回测脚本1.py 进程挂了之后，这个脚本会启动新的回测脚本2.py继续新的回测

```
import psutilimport osimport subprocessimport time#　判断回测脚本是否在运行中def is_script_running(script_name):    for process in psutil.process_iter(['pid', 'name', 'cmdline']):        if process.info['name'] == 'python.exe' or process.info['name'] == 'pythonw.exe':            if process.info['cmdline'] and script_name in process.info['cmdline'][1]:                return True    return Falsedef start_script(script_path):    try:    # 获取脚本所在的目录        script_dir = os.path.dirname(script_path)        # 获取脚本的名称        script_name = os.path.basename(script_path)        # 切换到脚本所在的目录        os.chdir(script_dir)        # 创建一个文件来保存输出        log_file = os.path.join(script_dir, 'log.log')        with open(log_file, 'a') as f:            # 启动脚本并将输出重定向到文件            process = subprocess.Popen(                ['python', script_name],                    cwd=script_dir,                   stdout=f,                   stderr=subprocess.STDOUT              )        print(f"Started script: {script_path}")        print(f"Output will be logged to: {log_file}")    except Exception as e:        print(f"Failed to start script: {e}")script_name = '回测脚本1.py'＃　备用的回测脚本路径script_path = r'D:\PycharmProjects\worldquantbrain\src\usa\analystxx\回测脚本2.py'while True:    if is_script_running(script_name):        print(f"{script_name} is running.")    else:        print(f"{script_name} is not running. Starting the script...")        start_script(script_path)        break    time.sleep(60)
```

还有个优化回测速度的tip:

有时候一个回测的post 持续了很久都没完成，怎么办？我一般是在发送post成功后，记录url，pool ID，task id的同时也把发送post的时间记录下来，每次判断post是否成功了的同时，也会判断下这个post simulate持续的时间多长了，如果超过我设置的时长，我就delete掉这个post,同时记录下delete 的simulate task到文件中，后续统一重新跑下这些task.


> [!NOTE] [图片 OCR 识别内容]
> VVL LUUuaIULaLy)
> ]#
> Cat
> active_second_pool.txt
> [[379
> 0
> 'https : / /api
> Worldquantbrain . com /simulations /2dUIO03524YO8MmQGFR3KWUI
> 1744466754.9898155]
> [377
> 1,
> "https : / /api
> Worldquantbrain
> Com/simula
> tions /26xBxTSrV4J4SYRdrAfaEzK"
> 1744466760.7057726]
> [377
> 2,
> "https: //api
> worldquantbrain . com/simulations /3gQGLFfXI4EMcamlmynFsNh
> 1744466778 .849996
> 3]
> [377
> 3
> "https:
> /api
> worldquantbrain _
> com/simulations /4erXHegXRSG3CyVSyhA33ZK"
> 1744466780 .369543]
> [377
> 4
> "https:
> /api .worldquantbrain . com/simu
> lations /
> IYEPj9S3ESaUbdNI3q5XcCQL '
> 1744466782.7577677] _
> [377 
> 5
> "https: / /api
> worldquantbrain . com /
> simuiations /3ZSGOMIqd4HTbSVIONgektwb"
> 1744466800.39
> 69886]
> [377
> 6
> "https:
> /api
> woridquantbrain-
> Com/
> simuiations /ZkZgUfcyg5jugxmySdtVMwp"
> 1744466805 .7206995]
> [377
> 7
> https:
> /api. worldquantbrain . com
> /simulations /34f5Zhhl84ItaaWnJoVdqzJ"
> 1744466829.6342309]
> [377
> 8
> "https:
> /api
> Worldquantbrain _
> com/simulations
> ZmOplTeayynLgSRVAciioAF
> 1744466831
> 368594]
> [377
> 9
> "https:
> /api
> Worldquantbrain _
> com/simulations /3ABs4r52D5jdbeBtMgOQSSR"
> 1744466835.3777065]1
> CmV_Worldauanbrain ) [root@VM-4-1G-opencloudos
> option8
> other  universe1#


如果我的分享对你有帮助，帮忙点个赞，谢谢~~

---

### 帖子 #81: 测测你最近2周提交的ra,ppa prod平均值
- **主帖链接**: 测测你最近2周提交的rappa prod平均值.md
- **讨论数**: 0

代码如下：

```
from requests.adapters import HTTPAdapterfrom urllib3.util.retry import Retryimport timeimport requestsimport jsonfrom typing import Dict, Listimport sysdef load_config(file_path):    """从指定路径加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user = config["user"]passwd = config["password"]def login():    username = user    password = passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    response = s.post('[链接已屏蔽])    print(response.content)    print("ok")    return ss=login()def wait_get(url: str, max_retries: int = 10):    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。    Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。    Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = s.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef get_os_alphas(start,end,total_alphas,limit: int = 100, get_first: bool = False,region=None) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url_ = f"[链接已屏蔽]        if region !=None:            url_=f"{url_}&settings.region={region}"        url = f"{url_}&dateSubmitted%3E{start}T04:00:00.000Z&dateSubmitted%3C{end}T04:00:00.000Z&order=-dateSubmitted"        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphasstart='2025-07-01'end='2025-09-25'submit_alphas = get_os_alphas(start=start,end=end,total_alphas=500)prod_count=0alpha_count=0for alpha in submit_alphas:    prod_count +=alpha["is"]["prodCorrelation"]    alpha_count +=1avg_prod=round(prod_count/alpha_count,4)print(f"avg prod: {avg_prod}")
```


> [!NOTE] [图片 OCR 识别内容]
> Fetching alphas
> from
> offset
> 0
> to
> 100
> Fetching alphas
> from
> offset
> 100 to 200
> avg prod:
> 0.6048


---

### 帖子 #82: 测测你最近2周提交的ra,ppa prod平均值
- **主帖链接**: https://support.worldquantbrain.com测测你最近2周提交的rappa prod平均值_35211934881943.md
- **讨论数**: 0

代码如下：

```
from requests.adapters import HTTPAdapterfrom urllib3.util.retry import Retryimport timeimport requestsimport jsonfrom typing import Dict, Listimport sysdef load_config(file_path):    """从指定路径加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user = config["user"]passwd = config["password"]def login():    username = user    password = passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    response = s.post('[链接已屏蔽])    print(response.content)    print("ok")    return ss=login()def wait_get(url: str, max_retries: int = 10):    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。    Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。    Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = s.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef get_os_alphas(start,end,total_alphas,limit: int = 100, get_first: bool = False,region=None) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url_ = f"[链接已屏蔽]        if region !=None:            url_=f"{url_}&settings.region={region}"        url = f"{url_}&dateSubmitted%3E{start}T04:00:00.000Z&dateSubmitted%3C{end}T04:00:00.000Z&order=-dateSubmitted"        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphasstart='2025-07-01'end='2025-09-25'submit_alphas = get_os_alphas(start=start,end=end,total_alphas=500)prod_count=0alpha_count=0for alpha in submit_alphas:    prod_count +=alpha["is"]["prodCorrelation"]    alpha_count +=1avg_prod=round(prod_count/alpha_count,4)print(f"avg prod: {avg_prod}")
```


> [!NOTE] [图片 OCR 识别内容]
> Fetching alphas
> from
> offset
> 0
> to
> 100
> Fetching alphas
> from
> offset
> 100 to 200
> avg prod:
> 0.6048


---

### 帖子 #83: 从数据库读取，import sqlite3def query_entry(db_path, tablename,order):    """    根据键查询数据库中的记录。    :param db_path: SQLite 数据库文件路径    ：tablename ： 表名    :param order: 要查询的键 的id    :return: 对应的值，如果不存在则返回 None    """    print(db_path)    print(f"从db中 获取alpha,需要{order}")    conn = sqlite3.connect(db_path)    cursor = conn.cursor()    print(db_path)    print(tablename)    cursor.execute(f"SELECT value FROM \"{tablename}\" WHERE id=?", (order,))    result = cursor.fetchone()    if result is None:        print(f"获取失败：{order} {result}")    else:        print(f"获取成功：{order} {result}")    conn.close()    return result[0] if result else None从数据库读取child id并设置属性：（部分代码）def process_child_simulate_reult( db,tablename,alpha_name,tag,order_id,ok_file,failed_to_get_resul):    brain_api_url = 'https://api.worldquantbrain.com'    if os.path.exists(order_file):        with open(order_file, "r") as f:            order_id = int(f.read().strip())  从文件中读取 order    else:        order_id=order_id    while True:  无限循环        simulate_ids_str = query_entry(db, table, order_id)        if not simulate_ids_str:            print(f"未找到 ID，等待 5 分钟后重试...")            append_to_file(log_file, f"未找到 ID {order}，等待 2 分钟后重试...")            sleep(120)  等待 2 分钟            continue  继续下一次循环        只有在成功获取数据后才更新 order        try:            simulate_ids = json.loads(simulate_ids_str)  确保 simulate_ids_str 有效        except json.JSONDecodeError:            print(f"解析 JSON 失败: {simulate_ids_str}")            append_to_file(log_file, f"解析 JSON 失败: {simulate_ids_str}")            将失败的 simulate_ids_str 写入文件            append_to_file(failed_to_get_result, simulate_ids_str)            order_id += 1            continue  跳过当前循环，继续尝试        更新 order 并写入文件        order_id += 1  更新 order        with open(order_file, "w") as f:            f.write(str(order_id))  将当前 order 写入文件        alpha_infos=[]        for simulate_id in simulate_ids:           child_progress =my_req(request_method="get",url=f"{brain_api_url}/simulations/{simulate_id}",timeout=15)            if child_progress == None:                print(f"处理 {simulate_id} 时发生错误")                print("跳过这个采集.")                append_to_file(log_file, f"处理 {simulate_id} 时发生错误: ")                append_to_file(failed_to_process_url, f"{brain_api_url}/simulations/{simulate_id}")                continue            try:                print(f"{brain_api_url}/simulations/{simulate_id}")                append_to_file(log_file, f"{brain_api_url}/simulations/{simulate_id}")                alpha_id = child_progress.json()["alpha"]                alpha_properties_json =  {                      "color": "RED",                       "name": "xxx",                       "tags":["xxx"],                       "category": None,                       "regular": {"description": description},                        "combo": {"description": "None"},                       "selection": {"description":"None"},                       }                reponse =my_req(request_method="patch",url=f"https://api.worldquantbrain.com/alphas/{alpha_id}",json_data=alpha_properties_json,timeout=15)                if res == None:                    print(f" {alpha_id} get alpha detail,set alpha_name failed,switch")                    continue            except Exception as e:                print(f"处理 {simulate_id} 时发生错误: {e}")                print("跳过这个采集.")                append_to_file(log_file, f"处理 {simulate_id} 时发生错误: {e}")                append_to_file(failed_to_process_url, f"{brain_api_url}/simulations/{simulate_id}")                sleep(5)
- **主帖链接**: 程序遇到http类错误 4xx5xx怎么处理代码优化.md
- **讨论数**: 2

最近经常有小伙伴提到遇到429错误，偶尔也遇到5xx错误。就我个人的理解，429是限频返回的错误,可通过调整自己代码中接口请求的频率，且代码需要兼容处理这类错误。5xx类错误，是服务器出现异常导致的，需要客户端进行重试。

在brain的各类接口中，最经常调用的几个接口有

```
1、回测 post 请求接口：/simulations2、打tag 的patch 请求接口3、其他get请求，get回测接口，get alpha详情等接口4、登录认证接口
```

关于登录认证接口，有小伙伴反馈遇到过429错误，我个人是没有遇到过的，但是有遇到5xx错误，登录429的问题，可以参考课代表新发的帖子，我自己也是使用全局变量来避免频繁登录的。

我之前修改为全局变量session的时候，还遇到一个错误，忘记在需要调用session的函数中增加 global s这行代码了，导致回测中断了几个小时。小伙伴们如果也修改为用全局变量session,记得避过这个坑~~

1,2,3接口，请求的时候经常会遇到各种http错误，为了避免重复的处理错误的代码，我把reqest请求和处理错误的代码封装到了一个函数中，在发起请求的时，直接调用该函数即可，函数如下：

该函数考虑了session过期 401 错误，429 限频，5xx错误的处理，后续如果有新的错误需要特殊处理，可直接在函数中增加对新错误的处理。

```
import requestsimport timefrom requests.exceptions import Timeout,HTTPError,RequestExceptiondef my_req(request_method,url,json_data=None,timeout=None):"""request_method 可选值： post,get,patch  ;stringurl: 请求的Urljson_data: json格式的请求参数timeout: 请求超时的时间设置，int"""   # 使用全局的session    global s    retries=0    max_retries=3    while retries < max_retries:        try:            # 发送回测请求（使用全局变量的s ）            if request_method == "post" and json_data != None:                response = s.post(url, json=json_data, timeout=timeout if timeout is not None else 15)            # 设置alpha 属性            elif request_method == "patch" and json_data  != None:                response = s.patch(url, json=json_data)            elif request_method == "get":                       #其他get请求                response = s.get(url,timeout=timeout if timeout is not None else 15)            try:                response.raise_for_status()                # 没有错误，直接返回结果                return response            except HTTPError as http_err:                if response.status_code == 401 or "Unauthorized" in str(http_err):                    print(f" status code:{response.status_code} 未认证,relogin")                    print("401未认证，尝试重新登录...")                    try:                        new_session = login()                        if new_session != None:                            s = new_session                    # 重置retries或继续使用剩余次数                    # retries = 0  # 可选：重新登录后重置计数器                    except Exception as e:                        print(f"登录失败: {str(e)}")                        retries += 1                    continue                elif response.status_code ==403 or "403 " in str(http_err):                    print(f"status code:{response.status_code} Forbidden 无权限访问（认证成功但权限不足）,{response.content},break")                    return None                elif response.status_code in [429,500,502,503,504]:                    wait = 2 ** retries  # 指数退避                    print(f"status code: {response.status_code} ,{response.content} ,sleep 5 and retry" )                    time.sleep(wait)                    retries += 1                else:                    raise http_err        except Timeout as e:            print(f"timeout err {e}, sleep 30 and retry")            retries += 1            time.sleep(5)        except RequestException as e:            print(f"请求失败: {str(e)}")            retries += 1            time.sleep(5)        except Exception as e:            print(f"error err {e} ,exit get request")            print(f"未知错误: {str(e)}")            retries += 1            # return None    print(f"达到最大重global session试次数 {max_retries}，放弃请求")    return None
```

如何使用该函数：

```
# 发送回测请求：reponse =my_req(request_method="post",url=url,json_data=sim_data_list,timeout=15)# 设置属性：reponse =my_req(request_method="patch",url=url,json_data=alpha_properties_json,timeout=15)# 其他get请求reponse =my_req(request_method="get",url=url,timeout=15)后续根据response 结果处理：if response !=None:#请求成功：  xxxelse:# 请求失败：# 如果是回测 请求没有成功，我最后是把任务重新加回队列；  yyy
```

还有个问题，如果同时开2个脚本设置属性，是一定会遇到429限频错误的。我是只跑1个脚本单独设置属性，函数每次调用一次设置属性，就sleep 1-2s，持续24小时运行。

---

### 帖子 #84: 从数据库读取，import sqlite3def query_entry(db_path, tablename,order):    """    根据键查询数据库中的记录。    :param db_path: SQLite 数据库文件路径    ：tablename ： 表名    :param order: 要查询的键 的id    :return: 对应的值，如果不存在则返回 None    """    print(db_path)    print(f"从db中 获取alpha,需要{order}")    conn = sqlite3.connect(db_path)    cursor = conn.cursor()    print(db_path)    print(tablename)    cursor.execute(f"SELECT value FROM \"{tablename}\" WHERE id=?", (order,))    result = cursor.fetchone()    if result is None:        print(f"获取失败：{order} {result}")    else:        print(f"获取成功：{order} {result}")    conn.close()    return result[0] if result else None从数据库读取child id并设置属性：（部分代码）def process_child_simulate_reult( db,tablename,alpha_name,tag,order_id,ok_file,failed_to_get_resul):    brain_api_url = 'https://api.worldquantbrain.com'    if os.path.exists(order_file):        with open(order_file, "r") as f:            order_id = int(f.read().strip())  从文件中读取 order    else:        order_id=order_id    while True:  无限循环        simulate_ids_str = query_entry(db, table, order_id)        if not simulate_ids_str:            print(f"未找到 ID，等待 5 分钟后重试...")            append_to_file(log_file, f"未找到 ID {order}，等待 2 分钟后重试...")            sleep(120)  等待 2 分钟            continue  继续下一次循环        只有在成功获取数据后才更新 order        try:            simulate_ids = json.loads(simulate_ids_str)  确保 simulate_ids_str 有效        except json.JSONDecodeError:            print(f"解析 JSON 失败: {simulate_ids_str}")            append_to_file(log_file, f"解析 JSON 失败: {simulate_ids_str}")            将失败的 simulate_ids_str 写入文件            append_to_file(failed_to_get_result, simulate_ids_str)            order_id += 1            continue  跳过当前循环，继续尝试        更新 order 并写入文件        order_id += 1  更新 order        with open(order_file, "w") as f:            f.write(str(order_id))  将当前 order 写入文件        alpha_infos=[]        for simulate_id in simulate_ids:           child_progress =my_req(request_method="get",url=f"{brain_api_url}/simulations/{simulate_id}",timeout=15)            if child_progress == None:                print(f"处理 {simulate_id} 时发生错误")                print("跳过这个采集.")                append_to_file(log_file, f"处理 {simulate_id} 时发生错误: ")                append_to_file(failed_to_process_url, f"{brain_api_url}/simulations/{simulate_id}")                continue            try:                print(f"{brain_api_url}/simulations/{simulate_id}")                append_to_file(log_file, f"{brain_api_url}/simulations/{simulate_id}")                alpha_id = child_progress.json()["alpha"]                alpha_properties_json =  {                      "color": "RED",                       "name": "xxx",                       "tags":["xxx"],                       "category": None,                       "regular": {"description": description},                        "combo": {"description": "None"},                       "selection": {"description":"None"},                       }                reponse =my_req(request_method="patch",url=f"https://api.worldquantbrain.com/alphas/{alpha_id}",json_data=alpha_properties_json,timeout=15)                if res == None:                    print(f" {alpha_id} get alpha detail,set alpha_name failed,switch")                    continue            except Exception as e:                print(f"处理 {simulate_id} 时发生错误: {e}")                print("跳过这个采集.")                append_to_file(log_file, f"处理 {simulate_id} 时发生错误: {e}")                append_to_file(failed_to_process_url, f"{brain_api_url}/simulations/{simulate_id}")                sleep(5)
- **主帖链接**: https://support.worldquantbrain.com程序遇到http类错误 4xx5xx怎么处理代码优化_32183927990935.md
- **讨论数**: 2

最近经常有小伙伴提到遇到429错误，偶尔也遇到5xx错误。就我个人的理解，429是限频返回的错误,可通过调整自己代码中接口请求的频率，且代码需要兼容处理这类错误。5xx类错误，是服务器出现异常导致的，需要客户端进行重试。

在brain的各类接口中，最经常调用的几个接口有

```
1、回测 post 请求接口：/simulations2、打tag 的patch 请求接口3、其他get请求，get回测接口，get alpha详情等接口4、登录认证接口
```

关于登录认证接口，有小伙伴反馈遇到过429错误，我个人是没有遇到过的，但是有遇到5xx错误，登录429的问题，可以参考课代表新发的帖子，我自己也是使用全局变量来避免频繁登录的。

我之前修改为全局变量session的时候，还遇到一个错误，忘记在需要调用session的函数中增加 global s这行代码了，导致回测中断了几个小时。小伙伴们如果也修改为用全局变量session,记得避过这个坑~~

1,2,3接口，请求的时候经常会遇到各种http错误，为了避免重复的处理错误的代码，我把reqest请求和处理错误的代码封装到了一个函数中，在发起请求的时，直接调用该函数即可，函数如下：

该函数考虑了session过期 401 错误，429 限频，5xx错误的处理，后续如果有新的错误需要特殊处理，可直接在函数中增加对新错误的处理。

```
import requestsimport timefrom requests.exceptions import Timeout,HTTPError,RequestExceptiondef my_req(request_method,url,json_data=None,timeout=None):"""request_method 可选值： post,get,patch  ;stringurl: 请求的Urljson_data: json格式的请求参数timeout: 请求超时的时间设置，int"""   # 使用全局的session    global s    retries=0    max_retries=3    while retries < max_retries:        try:            # 发送回测请求（使用全局变量的s ）            if request_method == "post" and json_data != None:                response = s.post(url, json=json_data, timeout=timeout if timeout is not None else 15)            # 设置alpha 属性            elif request_method == "patch" and json_data  != None:                response = s.patch(url, json=json_data)            elif request_method == "get":                       #其他get请求                response = s.get(url,timeout=timeout if timeout is not None else 15)            try:                response.raise_for_status()                # 没有错误，直接返回结果                return response            except HTTPError as http_err:                if response.status_code == 401 or "Unauthorized" in str(http_err):                    print(f" status code:{response.status_code} 未认证,relogin")                    print("401未认证，尝试重新登录...")                    try:                        new_session = login()                        if new_session != None:                            s = new_session                    # 重置retries或继续使用剩余次数                    # retries = 0  # 可选：重新登录后重置计数器                    except Exception as e:                        print(f"登录失败: {str(e)}")                        retries += 1                    continue                elif response.status_code ==403 or "403 " in str(http_err):                    print(f"status code:{response.status_code} Forbidden 无权限访问（认证成功但权限不足）,{response.content},break")                    return None                elif response.status_code in [429,500,502,503,504]:                    wait = 2 ** retries  # 指数退避                    print(f"status code: {response.status_code} ,{response.content} ,sleep 5 and retry" )                    time.sleep(wait)                    retries += 1                else:                    raise http_err        except Timeout as e:            print(f"timeout err {e}, sleep 30 and retry")            retries += 1            time.sleep(5)        except RequestException as e:            print(f"请求失败: {str(e)}")            retries += 1            time.sleep(5)        except Exception as e:            print(f"error err {e} ,exit get request")            print(f"未知错误: {str(e)}")            retries += 1            # return None    print(f"达到最大重global session试次数 {max_retries}，放弃请求")    return None
```

如何使用该函数：

```
# 发送回测请求：reponse =my_req(request_method="post",url=url,json_data=sim_data_list,timeout=15)# 设置属性：reponse =my_req(request_method="patch",url=url,json_data=alpha_properties_json,timeout=15)# 其他get请求reponse =my_req(request_method="get",url=url,timeout=15)后续根据response 结果处理：if response !=None:#请求成功：  xxxelse:# 请求失败：# 如果是回测 请求没有成功，我最后是把任务重新加回队列；  yyy
```

还有个问题，如果同时开2个脚本设置属性，是一定会遇到429限频错误的。我是只跑1个脚本单独设置属性，函数每次调用一次设置属性，就sleep 1-2s，持续24小时运行。

---

### 帖子 #85: 统计当月每个地区已提交了多少个纯ppa
- **主帖链接**: 统计当月每个地区已提交了多少个纯ppa.md
- **讨论数**: 3

平台对四大地区提交的纯ppa 限制每个月10个；小地区总共10个；区分D0，D1；

由于我没提交D0 alpha,所以代码没区分D0，D1，默认统计的都是D1的。

```
import requestsimport timefrom typing import Dict, List, Tuplefrom requests.adapters import HTTPAdapterfrom urllib3.util.retry import Retryimport jsonimport sysdef load_config(file_path):    """从指定路径加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user = config["user"]passwd = config["password"]def login():    username = user    password = passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    response = s.post('[链接已屏蔽])    print(response.content)    print("ok")    return ss=login()# get submit alphadef write_json_array(file_path, data):    """将整个JSON数组写入指定文件"""    with open(file_path, 'w') as file:        json.dump(data, file, indent=4)def read_json_array(file_path):    """从文件中读取整个JSON数组"""    try:        with open(file_path, 'r') as file:            return json.load(file)    except FileNotFoundError:        print(f"Error: File '{file_path}' not found.")        return None    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        return Nonedef wait_get(url: str, max_retries: int = 10):    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。    Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。    Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = s.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef get_os_alphas(start,end,total_alphas,limit: int = 100, get_first: bool = False,region=None) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    retries = 0    # total_alphas = 100    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url_ = f"[链接已屏蔽]        if region !=None:            url_=f"{url_}&settings.region={region}"        url = f"{url_}&dateSubmitted%3E{start}T04:00:00.000Z&dateSubmitted%3C{end}T04:00:00.000Z&order=-dateSubmitted"        print(url)        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphas#def is_prune_ppa(pyramids,classifications):    ppa_flag=False    effective = pyramids['effective']    for item in classifications:        if item['id'] == "POWER_POOL:POWER_POOL_ELIGIBLE":            ppa_flag= True            break    if  effective == 2 and  ppa_flag:        return True    else:        return False# 设置获取的alpha 时间范围start='2025-10-01'end='2025-10-09'submit_alphas = get_os_alphas(start=start,end=end,total_alphas=500)# 设置要统计的月份prune_ppa_time = '2025-10'write_json_array(f"submit_alphas_{start}_{end}.json", submit_alphas)# 这里根据自己有提交alpha的月份 增删地区；region_alpha ={    'USA':{'prune_ppa_num':0, "alphas":[]},    'EUR':{'prune_ppa_num':0, "alphas":[]},    "GLB":{'prune_ppa_num':0, "alphas":[]},    "ASI":{'prune_ppa_num':0, "alphas":[]},    "AMR":{'prune_ppa_num':0, "alphas":[]},}region_alpha_2 ={    'USA':{'prune_ppa_num':0},    'EUR':{'prune_ppa_num':0},    "GLB":{'prune_ppa_num':0},    "ASI":{'prune_ppa_num':0},    "AMR":{'prune_ppa_num':0},}for alpha in submit_alphas:    region=alpha['settings']['region']    pyramids=alpha['pyramidThemes']    dateSubmitted=alpha['dateSubmitted']    classifications=alpha['classifications']    if  is_prune_ppa(pyramids, classifications) and prune_ppa_time in dateSubmitted:        region_alpha[region]['prune_ppa_num'] +=1        region_alpha[region]['alphas'].append(alpha)        region_alpha_2[region]['prune_ppa_num'] += 1write_json_array(f"prune_ppa_detail_{prune_ppa_time}.json", region_alpha)write_json_array(f'prune_ppa_summary_{prune_ppa_time}.json',region_alpha_2)
```

结果如下：


> [!NOTE] [图片 OCR 识别内容]
> 25-10.json
> prune_ppa_summary_2025-10.json
> TUSA"
> "prune_ppa_num"
> }
> TEUR"
> "prune_ppa_num"
> }
> "GLB":
> {
> "prune_ppa
> num
> }
> TASI"
> "prune_ppa_num
> }
> TAIR"
> "prune_ppa_num
> Microsoft Remote Desktop


---

### 帖子 #86: 统计当月每个地区已提交了多少个纯ppa
- **主帖链接**: https://support.worldquantbrain.com统计当月每个地区已提交了多少个纯ppa_35512222559639.md
- **讨论数**: 3

平台对四大地区提交的纯ppa 限制每个月10个；小地区总共10个；区分D0，D1；

由于我没提交D0 alpha,所以代码没区分D0，D1，默认统计的都是D1的。

```
import requestsimport timefrom typing import Dict, List, Tuplefrom requests.adapters import HTTPAdapterfrom urllib3.util.retry import Retryimport jsonimport sysdef load_config(file_path):    """从指定路径加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user = config["user"]passwd = config["password"]def login():    username = user    password = passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    response = s.post('[链接已屏蔽])    print(response.content)    print("ok")    return ss=login()# get submit alphadef write_json_array(file_path, data):    """将整个JSON数组写入指定文件"""    with open(file_path, 'w') as file:        json.dump(data, file, indent=4)def read_json_array(file_path):    """从文件中读取整个JSON数组"""    try:        with open(file_path, 'r') as file:            return json.load(file)    except FileNotFoundError:        print(f"Error: File '{file_path}' not found.")        return None    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        return Nonedef wait_get(url: str, max_retries: int = 10):    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。    Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。    Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = s.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef get_os_alphas(start,end,total_alphas,limit: int = 100, get_first: bool = False,region=None) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    retries = 0    # total_alphas = 100    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url_ = f"[链接已屏蔽]        if region !=None:            url_=f"{url_}&settings.region={region}"        url = f"{url_}&dateSubmitted%3E{start}T04:00:00.000Z&dateSubmitted%3C{end}T04:00:00.000Z&order=-dateSubmitted"        print(url)        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphas#def is_prune_ppa(pyramids,classifications):    ppa_flag=False    effective = pyramids['effective']    for item in classifications:        if item['id'] == "POWER_POOL:POWER_POOL_ELIGIBLE":            ppa_flag= True            break    if  effective == 2 and  ppa_flag:        return True    else:        return False# 设置获取的alpha 时间范围start='2025-10-01'end='2025-10-09'submit_alphas = get_os_alphas(start=start,end=end,total_alphas=500)# 设置要统计的月份prune_ppa_time = '2025-10'write_json_array(f"submit_alphas_{start}_{end}.json", submit_alphas)# 这里根据自己有提交alpha的月份 增删地区；region_alpha ={    'USA':{'prune_ppa_num':0, "alphas":[]},    'EUR':{'prune_ppa_num':0, "alphas":[]},    "GLB":{'prune_ppa_num':0, "alphas":[]},    "ASI":{'prune_ppa_num':0, "alphas":[]},    "AMR":{'prune_ppa_num':0, "alphas":[]},}region_alpha_2 ={    'USA':{'prune_ppa_num':0},    'EUR':{'prune_ppa_num':0},    "GLB":{'prune_ppa_num':0},    "ASI":{'prune_ppa_num':0},    "AMR":{'prune_ppa_num':0},}for alpha in submit_alphas:    region=alpha['settings']['region']    pyramids=alpha['pyramidThemes']    dateSubmitted=alpha['dateSubmitted']    classifications=alpha['classifications']    if  is_prune_ppa(pyramids, classifications) and prune_ppa_time in dateSubmitted:        region_alpha[region]['prune_ppa_num'] +=1        region_alpha[region]['alphas'].append(alpha)        region_alpha_2[region]['prune_ppa_num'] += 1write_json_array(f"prune_ppa_detail_{prune_ppa_time}.json", region_alpha)write_json_array(f'prune_ppa_summary_{prune_ppa_time}.json',region_alpha_2)
```

结果如下：


> [!NOTE] [图片 OCR 识别内容]
> 25-10.json
> prune_ppa_summary_2025-10.json
> TUSA"
> "prune_ppa_num"
> }
> TEUR"
> "prune_ppa_num"
> }
> "GLB":
> {
> "prune_ppa
> num
> }
> TASI"
> "prune_ppa_num
> }
> TAIR"
> "prune_ppa_num
> Microsoft Remote Desktop


---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《clarification on group datafield》的评论回复
- **帖子链接**: [Commented] clarification on group datafield.md
- **评论时间**: 1年前

Hello, friend. On the Genius , when counting "how many fields each Alpha factor uses," **all fields explicitly appearing in the Alpha expression are typically counted**, regardless of whether they are used for calculation, grouping, or filtering.

**Specifically for your example `group_rank(datafield, exchange)`:** 
1. **`datafield`**: This is the primary calculation field. It will definitely be counted. 
2. **`exchange`**: This is the grouping field (`group by`). Although not directly computed, it is **an integral part of the Alpha's logic**. The Alpha’s result relies on ranking grouped by `exchange`.

**Thus, this Alpha `group_rank(datafield, exchange)` will be counted as using 2 data fields: `datafield` and `exchange`.**

*To summarize, in Genius, commonly used groups like **country, exchange, sector, industry, and subindustry** will also be counted within the number of fields used by a single Alpha. This impacts the **fields per alpha** metric.*

---

### 探讨 #2: 关于《clarification on group datafield》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] clarification on group datafield_32666842600087.md
- **评论时间**: 1年前

Hello, friend. On the Genius , when counting "how many fields each Alpha factor uses," **all fields explicitly appearing in the Alpha expression are typically counted**, regardless of whether they are used for calculation, grouping, or filtering.

**Specifically for your example `group_rank(datafield, exchange)`:** 
1. **`datafield`**: This is the primary calculation field. It will definitely be counted. 
2. **`exchange`**: This is the grouping field (`group by`). Although not directly computed, it is **an integral part of the Alpha's logic**. The Alpha’s result relies on ranking grouped by `exchange`.

**Thus, this Alpha `group_rank(datafield, exchange)` will be counted as using 2 data fields: `datafield` and `exchange`.**

*To summarize, in Genius, commonly used groups like **country, exchange, sector, industry, and subindustry** will also be counted within the number of fields used by a single Alpha. This impacts the **fields per alpha** metric.*

---

### 探讨 #3: 关于《Combined alpha performance and combined selected alpha performance》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Combined alpha performance and combined selected alpha performance_32658322195095.md
- **评论时间**: 1年前

Friend, **Combined Alpha Performance** measures the overall out-of-sample (OS) performance of all the alphas you submitted. **Combined Selected Alpha Performance** measures the OS performance of the alphas selected by the platform.

To maintain strong results:  

1. **Consistently submit high-quality alphas**;  

2. Ensure **stable quality across all regions** where you submit alphas — performance is calculated with **equal weighting per region**;  

3. **Balance quality across regions** to achieve equilibrium.

---

### 探讨 #4: 关于《COMBINED评分纳入更多的手续费应该如何应对？》的评论回复
- **帖子链接**: [Commented] COMBINED评分纳入更多的手续费应该如何应对.md
- **评论时间**: 5个月前

感觉开maxtrade提交会比较符合实际的margin情况的，

对combine 的稳定会有一定的帮助。

========================================

---

### 探讨 #5: 关于《COMBINED评分纳入更多的手续费应该如何应对？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] COMBINED评分纳入更多的手续费应该如何应对_37006696024087.md
- **评论时间**: 5个月前

感觉开maxtrade提交会比较符合实际的margin情况的，

对combine 的稳定会有一定的帮助。

========================================

---

### 探讨 #6: 关于《Community Activity Score 的增与减？》的评论回复
- **帖子链接**: [Commented] Community Activity Score 的增与减.md
- **评论时间**: 1年前

===================================================================================

active的显示的分数是rank后的，别人的active增加了，你没有增加，排名就下降，active 分数将会降低。

==============================================================================

---

### 探讨 #7: 关于《Community Activity Score 的增与减？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Community Activity Score 的增与减_32984804292375.md
- **评论时间**: 1年前

===================================================================================

active的显示的分数是rank后的，别人的active增加了，你没有增加，排名就下降，active 分数将会降低。

==============================================================================

---

### 探讨 #8: 关于《How to Improve After Cost Performance置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] How to Improve After Cost Performance置顶的_29647491881623.md
- **评论时间**: 1年前

Thank you for sharing the tips on optimizing post-fee costs. Especially the test regarding the sub-universe. Could you explain in more detail how to use the two operators  `ts_target_tvr_delta_limit`  and  `ts_delta_limit`  to optimize   [***After-cost Sharpe ratio***](/hc/en-us/articles/25960264611351-What-s-After-cost-Sharpe-ratio) ? Thank you！

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] osmosisPoints一键清零代码.md
- **评论时间**: 3个月前

感谢虎哥！

---

### 探讨 #10: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] osmosisPoints一键清零代码_39225136138263.md
- **评论时间**: 3个月前

感谢虎哥！

---

### 探讨 #11: 关于《Q2 Final Push: Know Where You Really Stand in Tie-Breaker Rankings》的评论回复
- **帖子链接**: [Commented] Q2 Final Push Know Where You Really Stand in Tie-Breaker Rankings.md
- **评论时间**: 1年前

Powerful breakdown of tie-breaker mechanics! 💎 This hierarchy of criteria finally clarifies *where* to allocate effort for max ranking upside.

---

### 探讨 #12: 关于《Q2 Final Push: Know Where You Really Stand in Tie-Breaker Rankings》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Q2 Final Push Know Where You Really Stand in Tie-Breaker Rankings_32824115946391.md
- **评论时间**: 1年前

Powerful breakdown of tie-breaker mechanics! 💎 This hierarchy of criteria finally clarifies *where* to allocate effort for max ranking upside.

---

### 探讨 #13: 关于《Question about the combined power pool index will be calculated for the level ranking in Q2 2025 or the level ranking in Q3 2025》的评论回复
- **帖子链接**: [Commented] Question about the combined power pool index will be calculated for the level ranking in Q2 2025 or the level ranking in Q3 2025.md
- **评论时间**: 1年前

hello ,According to the last global network meeting, the PPAC's combined performance will be included in the Q3 Genius Combine.

hope you have a good performance in genius ranking.

---

### 探讨 #14: 关于《Question about the combined power pool index will be calculated for the level ranking in Q2 2025 or the level ranking in Q3 2025》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Question about the combined power pool index will be calculated for the level ranking in Q2 2025 or the level ranking in Q3 2025_32817540072727.md
- **评论时间**: 1年前

hello ,According to the last global network meeting, the PPAC's combined performance will be included in the Q3 Genius Combine.

hope you have a good performance in genius ranking.

---

### 探讨 #15: 关于《SA日入50刀，如何把握好SuperAlphaCompetition经验分享》的评论回复
- **帖子链接**: [Commented] SA日入50刀如何把握好SuperAlphaCompetition经验分享.md
- **评论时间**: 1年前

==================================================================================

厉害的！！祝大佬vf节节高！！希望我也能每天收入这么高。大佬的regular alpha收入也好高啊，羡慕

=================================================================================

---

### 探讨 #16: 关于《SA日入50刀，如何把握好SuperAlphaCompetition经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] SA日入50刀如何把握好SuperAlphaCompetition经验分享_32630124449559.md
- **评论时间**: 1年前

==================================================================================

厉害的！！祝大佬vf节节高！！希望我也能每天收入这么高。大佬的regular alpha收入也好高啊，羡慕

=================================================================================

---

### 探讨 #17: 关于《Updated Brain API Settings for Alpha Research》的评论回复
- **帖子链接**: [Commented] Updated Brain API Settings for Alpha Research.md
- **评论时间**: 1年前

Excellent consolidation of region-specific parameters! 🚀 This will save countless hours in cross-market alpha testing. Three key observations for optimization:**

1. **Neutralization Asymmetry**  

   - US notably lacks `COUNTRY` neutralization (vs. EUR/GLB/ASI), suggesting domestic factors dominate.  

   - China/Korea/TW/HK/Japan omit `STATISTICAL` neutralization – is this due to data constraints or strategy design?

2. **Liquidity Thresholds**  

   `ILLIQUID_MINVOL1M` appears in US/EUR/ASI but not emerging markets. Critical for small-cap strategies!

3. **Actionable Tips**  

   ```python  

   # Pro optimization: Chain neutralizations for crowded regions (e.g. EUROPE)  

   neutralize(["SECTOR", "STATISTICAL", "CROWDING"], inplace=True)  

   ```

---

### 探讨 #18: 关于《Updated Brain API Settings for Alpha Research》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Updated Brain API Settings for Alpha Research_32555127334807.md
- **评论时间**: 1年前

Excellent consolidation of region-specific parameters! 🚀 This will save countless hours in cross-market alpha testing. Three key observations for optimization:**

1. **Neutralization Asymmetry**  

   - US notably lacks `COUNTRY` neutralization (vs. EUR/GLB/ASI), suggesting domestic factors dominate.  

   - China/Korea/TW/HK/Japan omit `STATISTICAL` neutralization – is this due to data constraints or strategy design?

2. **Liquidity Thresholds**  

   `ILLIQUID_MINVOL1M` appears in US/EUR/ASI but not emerging markets. Critical for small-cap strategies!

3. **Actionable Tips**  

   ```python  

   # Pro optimization: Chain neutralizations for crowded regions (e.g. EUROPE)  

   neutralize(["SECTOR", "STATISTICAL", "CROWDING"], inplace=True)  

   ```

---

### 探讨 #19: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] VF098Expert直升Grandmaster我是怎么做的.md
- **评论时间**: 5个月前

expert 升GM，每个赛季都有这种跨跃式升级的强者，真的佩服！！

=================== 点塔困难户 ===============================

=================== alpha难产户 ===============================

---

### 探讨 #20: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] VF098Expert直升Grandmaster我是怎么做的_37555582592023.md
- **评论时间**: 5个月前

expert 升GM，每个赛季都有这种跨跃式升级的强者，真的佩服！！

=================== 点塔困难户 ===============================

=================== alpha难产户 ===============================

---

### 探讨 #21: 关于《WHAT IS THE DIFFERENCE BETWEEN BASE TAGED OPERATORS AND GENIUS TAGGED OPERATORS?》的评论回复
- **帖子链接**: [Commented] WHAT IS THE DIFFERENCE BETWEEN BASE TAGED OPERATORS AND GENIUS TAGGED OPERATORS.md
- **评论时间**: 1年前

The basic operators are available to all users — both regular and Genius-level — as part of the Brain backtesting platform. In contrast, **Genius-labeled operators** are exclusive to users at the **Gold level and above** (including Gold, Expert, Master, and Grandmaster tiers).

Moreover, the set of available Genius operators may vary — even among users within the same tier or across different Genius levels. Generally speaking, higher Genius tiers grant access to a broader range of Genius operators.

---

### 探讨 #22: 关于《WHAT IS THE DIFFERENCE BETWEEN BASE TAGED OPERATORS AND GENIUS TAGGED OPERATORS?》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] WHAT IS THE DIFFERENCE BETWEEN BASE TAGED OPERATORS AND GENIUS TAGGED OPERATORS_32484818126999.md
- **评论时间**: 1年前

The basic operators are available to all users — both regular and Genius-level — as part of the Brain backtesting platform. In contrast, **Genius-labeled operators** are exclusive to users at the **Gold level and above** (including Gold, Expert, Master, and Grandmaster tiers).

Moreover, the set of available Genius operators may vary — even among users within the same tier or across different Genius levels. Generally speaking, higher Genius tiers grant access to a broader range of Genius operators.

---

### 探讨 #23: 关于《YOU DECIDE! What topics do you want???》的评论回复
- **帖子链接**: [Commented] YOU DECIDE What topics do you want.md
- **评论时间**: 1年前

I hope the BRAIN platform can provides more  tips about operation usage . And another one is if  the Gold tier offer expanded dataset options? Alternatively, could datasets be refreshed quarterly without requiring a successful Genius tier upgrade?

Provides some tips on how to test the alpha 's robust

---

### 探讨 #24: 关于《YOU DECIDE! What topics do you want???》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] YOU DECIDE What topics do you want_29837364620695.md
- **评论时间**: 1年前

I hope the BRAIN platform can provides more  tips about operation usage . And another one is if  the Gold tier offer expanded dataset options? Alternatively, could datasets be refreshed quarterly without requiring a successful Genius tier upgrade?

Provides some tips on how to test the alpha 's robust

---

### 探讨 #25: 关于《3. 保留原有连续非零值检查》的评论回复
- **帖子链接**: [Commented] [代码优化]只有IS两年数据或少于剔除办法代码优化.md
- **评论时间**: 1年前

============================================================

大佬，你终于把这个过滤的代码发贴了，我等了好久，差点以为无了。

感谢分享～～～

============================================================

---

### 探讨 #26: 关于《3. 保留原有连续非零值检查》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [代码优化]只有IS两年数据或少于剔除办法代码优化_33131173409175.md
- **评论时间**: 1年前

============================================================

大佬，你终于把这个过滤的代码发贴了，我等了好久，差点以为无了。

感谢分享～～～

============================================================

---

### 探讨 #27: 关于《优化布局》的评论回复
- **帖子链接**: [Commented] [代码优化]样本内外分布一致性分析月份对比代码分享代码优化.md
- **评论时间**: 1年前

==========================================================

大佬🐮，感谢分享，我已经提前用上大佬的代码了，很好用，可以直观看到自己每个月的提交的alpha对比情况，有助于分析提交的alpha，找出不足之处进行改进。

祝大佬vf 节节高。

==========================================================

---

### 探讨 #28: 关于《优化布局》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [代码优化]样本内外分布一致性分析月份对比代码分享代码优化_33128160209175.md
- **评论时间**: 1年前

==========================================================

大佬🐮，感谢分享，我已经提前用上大佬的代码了，很好用，可以直观看到自己每个月的提交的alpha对比情况，有助于分析提交的alpha，找出不足之处进行改进。

祝大佬vf 节节高。

==========================================================

---

### 探讨 #29: 关于《【Alpha灵感】Stock Market's reaction to liquidity shocksAlpha Template》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】Stock Markets reaction to liquidity shocksAlpha Template.md
- **评论时间**: 1年前

大佬，请教下："使用标准化 amihud 与 amihud 本身在两个月内的时间序列相关性，这样就能创建一个可以独立提交的 alpha。” 这个是基于什么考虑的呢？是论文中提到的还是？我不是很理解您是怎么想到这个数据处理的方法的？

======================================================================

---

### 探讨 #30: 关于《【Alpha灵感】Stock Market's reaction to liquidity shocksAlpha Template》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】Stock Markets reaction to liquidity shocksAlpha Template_32546137590039.md
- **评论时间**: 1年前

大佬，请教下："使用标准化 amihud 与 amihud 本身在两个月内的时间序列相关性，这样就能创建一个可以独立提交的 alpha。” 这个是基于什么考虑的呢？是论文中提到的还是？我不是很理解您是怎么想到这个数据处理的方法的？

======================================================================

---

### 探讨 #31: 关于《【Alpha灵感】基于short interest数据的跨交易所组合案例》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】基于short interest数据的跨交易所组合案例.md
- **评论时间**: 8个月前

写得很有启发意义，感谢分享

----------------------------------------------------------- 学习，进步 ------------------------------------------------------

---

### 探讨 #32: 关于《【Alpha灵感】基于short interest数据的跨交易所组合案例》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】基于short interest数据的跨交易所组合案例_35577573602455.md
- **评论时间**: 8个月前

写得很有启发意义，感谢分享

----------------------------------------------------------- 学习，进步 ------------------------------------------------------

---

### 探讨 #33: 关于《【genius】如何在 Genius 级别范围内获得更高的季度付款》的评论回复
- **帖子链接**: [Commented] 【genius】如何在 Genius 级别范围内获得更高的季度付款.md
- **评论时间**: 1年前

==============================================================================

好详细的季度奖分析啊，感谢分享

每天都在挖坑，却一无所获，好想每天都能挖到多多的alpha 啊！

==============================================================================

---

### 探讨 #34: 关于《【genius】如何在 Genius 级别范围内获得更高的季度付款》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【genius】如何在 Genius 级别范围内获得更高的季度付款_33037373635223.md
- **评论时间**: 1年前

==============================================================================

好详细的季度奖分析啊，感谢分享

每天都在挖坑，却一无所获，好想每天都能挖到多多的alpha 啊！

==============================================================================

---

### 探讨 #35: 关于《【MCP实战】利用MCP工具，将weight 从 40%+优化到满足提交要求的真实案例分享》的评论回复
- **帖子链接**: [Commented] 【MCP实战】利用MCP工具将weight 从 40优化到满足提交要求的真实案例分享.md
- **评论时间**: 7个月前

厉害 优秀的帖子 学习了 后续实践复现下 感谢分享

---

### 探讨 #36: 关于《【MCP实战】利用MCP工具，将weight 从 40%+优化到满足提交要求的真实案例分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【MCP实战】利用MCP工具将weight 从 40优化到满足提交要求的真实案例分享_35731558272023.md
- **评论时间**: 7个月前

厉害 优秀的帖子 学习了 后续实践复现下 感谢分享

---

### 探讨 #37: 关于《【Template by Tiger】 关于news21中的fast_d1的一个思路》的评论回复
- **帖子链接**: [Commented] 【Template by Tiger】 关于news21中的fast_d1的一个思路.md
- **评论时间**: 6个月前

虎哥威武！

==================================================================================

---

### 探讨 #38: 关于《【Template by Tiger】 关于news21中的fast_d1的一个思路》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Template by Tiger】 关于news21中的fast_d1的一个思路_37256491735959.md
- **评论时间**: 6个月前

虎哥威武！

==================================================================================

---

### 探讨 #39: 关于《【基于相关性剪枝】完整代码代码优化》的评论回复
- **帖子链接**: [Commented] 【基于相关性剪枝】完整代码代码优化.md
- **评论时间**: 11个月前

大佬，你这里是根据第一个alpha来判断后续其他alpha于它的相关性 ，选择是保留还是剔除的吗？那么这种方法选出来选择保存的alpha,是否会很依赖于与第一个alpha的相关性？导致更优秀的alpha由于与第一个alpha的相关性而剔除？

================================================================================

---

### 探讨 #40: 关于《【基于相关性剪枝】完整代码代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【基于相关性剪枝】完整代码代码优化_33498292829591.md
- **评论时间**: 11个月前

大佬，你这里是根据第一个alpha来判断后续其他alpha于它的相关性 ，选择是保留还是剔除的吗？那么这种方法选出来选择保存的alpha,是否会很依赖于与第一个alpha的相关性？导致更优秀的alpha由于与第一个alpha的相关性而剔除？

================================================================================

---

### 探讨 #41: 关于《【新人指南】到底要交什么样的Alpha？置顶的》的评论回复
- **帖子链接**: [Commented] 【新人指南】到底要交什么样的Alpha置顶的.md
- **评论时间**: 1年前

[TD37298](/hc/zh-cn/profiles/26582306929687-TD37298) ： 可以做下各种中性化测试，decay衰退测试以及官方推荐的rank,sign测试，提交alpha前，做下这些测试，看各种中心化和decay下alpha的表现是否一致。

------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #42: 关于《【新人指南】到底要交什么样的Alpha？置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【新人指南】到底要交什么样的Alpha置顶的_32226888249239.md
- **评论时间**: 1年前

[TD37298](/hc/zh-cn/profiles/26582306929687-TD37298) ： 可以做下各种中性化测试，decay衰退测试以及官方推荐的rank,sign测试，提交alpha前，做下这些测试，看各种中心化和decay下alpha的表现是否一致。

------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #43: 关于《【新人第一关】如何度过找不到Alpha的困难期》的评论回复
- **帖子链接**: [Commented] 【新人第一关】如何度过找不到Alpha的困难期.md
- **评论时间**: 1年前

请问怎么操作呢？在本地日志打印记录可以吧

---

### 探讨 #44: 关于《【新人第一关】如何度过找不到Alpha的困难期》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【新人第一关】如何度过找不到Alpha的困难期_28915310428311.md
- **评论时间**: 1年前

请问怎么操作呢？在本地日志打印记录可以吧

---

### 探讨 #45: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

量化日记Day1

今天是2025.3.14号，距离我成为有条件顾问已经23天了，一共提交了30个alpha。

目前跑了USA,EUR,ASI这3个地区的fnd,model,analyst数据集，感觉这这几个Categories还是比较容易出alpha得，就是prod相关性太高了，经常需要手动调整降低prod 。

下一步想先继续研究下operate 的用法和一些其他类型的数据集适用template，比如新闻，情绪方面的dateset，感觉直接用工厂代码回测，可能比较难出alpha。

希望明天能有跑出新的好alpha,~~

---

### 探讨 #46: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025.3.20

1、昨天误交了一个self 0.8的，还交了一个新signal ，self0.3的，base只有 $1.58。警惕： 以后提交alpha,务必check self先，不要直接提交。

2、最近get到了performance的正确用法，今天还挖到了一个self 0.2的新alpha，调整了下提交了，希望明天base能好看些

---

### 探讨 #47: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天测试了提交1个之前已经提交过的alpha参加power alpha competition，小修了下，self是0.94，今天的base是1.46！！实践证明，即使是比赛降低了规则，单独一个pool 放比赛的alpha，也不要提交self超过7的！！否则后果严重

---

### 探讨 #48: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025.4.16:

感觉陷入瓶颈了，alpha好难挖，需要学习学习再学习！！

---

### 探讨 #49: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-22 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.699 ;
RA: 0个 ;
PPA: 3个 ;
region: ASI ;sharpe:1.25 ; fitness:0.85 ; self_correlation:0.118 ; prodCorrelation:0.6737 ,pyramids:['ASI/D1/MACRO'] ;
region: GLB ;sharpe:1.13 ; fitness:0.7 ; self_correlation:0.2256 ; prodCorrelation:0.6603 ,pyramids:['GLB/D1/MACRO'] ;
region: GLB ;sharpe:1.72 ; fitness:1.71 ; self_correlation:0.3495 ; prodCorrelation:0.763 ,pyramids:['GLB/D1/EARNINGS'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 4.72 ;
fitness: 5.16 ;
self: 0.6524 ;
prodCorrelation: 0.665 ;

---

### 探讨 #50: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-23 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.6986 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:1.46 ; fitness:0.91 ; self_correlation:0.4752 ; prodCorrelation:0.6986 ,pyramids:['GLB/D1/MODEL'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 4.69 ;
fitness: 6.25 ;
self: 0.6808 ;
prodCorrelation: 0.6914 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #51: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-24 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.62335 ;
RA: 0个 ;
PPA: 4个 ;
region: GLB ;sharpe:1.6 ; fitness:1.3 ; self_correlation:0.4455 ; prodCorrelation:0.6887 ,pyramids:['GLB/D1/INSTITUTIONS'] ;
region: EUR ;sharpe:1.13 ; fitness:0.65 ; self_correlation:0.2721 ; prodCorrelation:0.6143 ,pyramids:['EUR/D1/INSTITUTIONS'] ;
region: EUR ;sharpe:1.09 ; fitness:0.67 ; self_correlation:0.1608 ; prodCorrelation:0.4232 ,pyramids:['EUR/D1/INSTITUTIONS'] ;
region: GLB ;sharpe:1.64 ; fitness:1.5 ; self_correlation:0.2087 ; prodCorrelation:0.7672 ,pyramids:['GLB/D1/RISK'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 7.85 ;
fitness: 10.13 ;
self: 0.3539 ;
prodCorrelation: 0.3539 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #52: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-25 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.5075999999999999 ;
RA: 0个 ;
PPA: 3个 ;
region: EUR ;sharpe:1.06 ; fitness:0.84 ; self_correlation:0.145 ; prodCorrelation:0.5001 ,pyramids:['EUR/D1/OPTION'] ;
region: GLB ;sharpe:1.14 ; fitness:1.11 ; self_correlation:0.2051 ; prodCorrelation:0.4945 ,pyramids:['GLB/D1/INSTITUTIONS'] ;
region: EUR ;sharpe:1.13 ; fitness:0.92 ; self_correlation:0.1519 ; prodCorrelation:0.5282 ,pyramids:['EUR/D1/INSTITUTIONS'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 7.7 ;
fitness: 8.28 ;
self: 0.2943 ;
prodCorrelation: 0.344 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #53: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-26 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.7449250000000001 ;
RA: 2个 ;
region: EUR ;sharpe:1.75 ; fitness:1.61 ; self_correlation:0.3036 ; prodCorrelation:0.6698 ,pyramids:['EUR/D1/RISK'] ;
region: EUR ;sharpe:2.66 ; fitness:2.0 ; self_correlation:0.6464 ; prodCorrelation:0.7229 ,pyramids:['EUR/D1/ANALYST'] ;
PPA: 2个 ;
region: GLB ;sharpe:1.28 ; fitness:0.71 ; self_correlation:0.3298 ; prodCorrelation:0.7471 ,pyramids:['GLB/D1/INSTITUTIONS'] ;
region: EUR ;sharpe:2.49 ; fitness:1.58 ; self_correlation:0.724 ; prodCorrelation:0.8399 ,pyramids:['EUR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.63 ;
fitness: 5.0 ;
self: 0.6251 ;
prodCorrelation: 0.6251 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #54: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

----------------------------------橘子的量化日记 -------------------------------------
 2025-11-27 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.49433333333333335 ;
RA: 0个 ;
PPA: 3个 ;
region: ASI ;sharpe:1.18 ; fitness:0.93 ; self_correlation:0.0884 ; prodCorrelation:0.2178 ,pyramids:['ASI/D1/INSTITUTIONS'] ;
region: GLB ;sharpe:1.49 ; fitness:0.88 ; self_correlation:0.3656 ; prodCorrelation:0.8201 ,pyramids:['GLB/D1/PV', 'GLB/D1/INSTITUTIONS'] ;
region: EUR ;sharpe:1.21 ; fitness:0.67 ; self_correlation:0.2046 ; prodCorrelation:0.4451 ,pyramids:['EUR/D1/SOCIALMEDIA'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.54 ;
fitness: 6.48 ;
self: 0.3789 ;
prodCorrelation: 0.3995 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #55: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

----------------------------------橘子的量化日记 -------------------------------------
 2025-11-28 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.6806000000000001 ;
RA: 2个 ;
region: EUR ;sharpe:2.04 ; fitness:1.17 ; self_correlation:0.3924 ; prodCorrelation:0.6942 ,pyramids:['EUR/D1/SOCIALMEDIA', 'EUR/D1/RISK'] ;
region: EUR ;sharpe:1.79 ; fitness:1.03 ; self_correlation:0.3188 ; prodCorrelation:0.6813 ,pyramids:['EUR/D1/MACRO', 'EUR/D1/MODEL'] ;
PPA: 1个 ;
region: ASI ;sharpe:1.01 ; fitness:0.61 ; self_correlation:0.3176 ; prodCorrelation:0.6663 ,pyramids:['ASI/D1/INSTITUTIONS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.2 ;
fitness: 5.01 ;
self: 0.4689 ;
prodCorrelation: 0.4689 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #56: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-29 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4 ;
RA: 0个 ;
PPA: 1个 ;
region: ASI ;sharpe:1.36 ; fitness:1.18 ; self_correlation:0.145 ; prodCorrelation:0.4 ,pyramids:['ASI/D1/INSTITUTIONS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 7.34 ;
fitness: 7.47 ;
self: 0.4703 ;
prodCorrelation: 0.4703 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #57: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-30 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.5617 ;
RA: 0个 ;
PPA: 1个 ;
region: EUR ;sharpe:1.33 ; fitness:0.85 ; self_correlation:0.271 ; prodCorrelation:0.5617 ,pyramids:['EUR/D1/PV'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 6.04 ;
fitness: 5.62 ;
self: 0.6829 ;
prodCorrelation: 0.6829 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #58: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-01 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.24939999999999998 ;
RA: 0个 ;
PPA: 3个 ;
region: AMR ;sharpe:1.01 ; fitness:0.67 ; self_correlation:0.1186 ; prodCorrelation:0.248 ,pyramids:['AMR/D1/INSTITUTIONS'] ;
region: AMR ;sharpe:1.02 ; fitness:0.64 ; self_correlation:0.1356 ; prodCorrelation:0.2311 ,pyramids:['AMR/D1/INSTITUTIONS'] ;
region: AMR ;sharpe:1.1 ; fitness:0.88 ; self_correlation:0.1601 ; prodCorrelation:0.2691 ,pyramids:['AMR/D1/INSTITUTIONS'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 8.35 ;
fitness: 13.54 ;
self: 0.3263 ;
prodCorrelation: 0.4845 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #59: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-02 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.3403666666666667 ;
RA: 1个 ;
region: EUR ;sharpe:1.66 ; fitness:1.04 ; self_correlation:0.3475 ; prodCorrelation:0.4688 ,pyramids:[ 'EUR/D1/MODEL'] ;
PPA: 2个 ;
region: ASI ;sharpe:1.17 ; fitness:0.99 ; self_correlation:0.0641 ; prodCorrelation:0.2236 ,pyramids:['ASI/D1/INSTITUTIONS', 'ASI/D1/SHORTINTEREST'] ;
region: AMR ;sharpe:1.26 ; fitness:0.94 ; self_correlation:0.2353 ; prodCorrelation:0.3287 ,pyramids:['AMR/D1/FUNDAMENTAL'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 4.13 ;
fitness: 5.3 ;
self: 0.4536 ;
prodCorrelation: 0.4831 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #60: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-03 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.43665 ;
RA: 1个 ;
region: GLB ;sharpe:2.22 ; fitness:1.91 ; self_correlation:0.1751 ; prodCorrelation:0.5547 ,pyramids:['GLB/D1/MACRO'] ;
PPA: 3个 ;
region: AMR ;sharpe:1.06 ; fitness:0.65 ; self_correlation:0.3245 ; prodCorrelation:0.4243 ,pyramids:['AMR/D1/ANALYST'] ;
region: GLB ;sharpe:1.49 ; fitness:1.24 ; self_correlation:0.262 ; prodCorrelation:0.5603 ,pyramids:['GLB/D1/MODEL'] ;
region: AMR ;sharpe:1.3 ; fitness:1.33 ; self_correlation:0.1075 ; prodCorrelation:0.2073 ,pyramids:['AMR/D1/PV'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.85 ;
fitness: 5.11 ;
self: 0.6702 ;
prodCorrelation: 0.6702 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #61: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-04 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.6665333333333333 ;
RA: 0个 ;
PPA: 3个 ;
region: GLB ;sharpe:1.66 ; fitness:0.84 ; self_correlation:0.1783 ; prodCorrelation:0.6865 ,pyramids:['GLB/D1/MODEL'] ;
region: EUR ;sharpe:1.67 ; fitness:1.4 ; self_correlation:0.274 ; prodCorrelation:0.9047 ,pyramids:['EUR/D1/SOCIALMEDIA', 'EUR/D1/MODEL'] ;
region: AMR ;sharpe:1.21 ; fitness:0.85 ; self_correlation:0.1846 ; prodCorrelation:0.4084 ,pyramids:['AMR/D1/ANALYST'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 4.3 ;
fitness: 5.26 ;
self: 0.4361 ;
prodCorrelation: 0.4361 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #62: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-05 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.44272500000000004 ;
RA: 2个 ;
region: AMR ;sharpe:1.59 ; fitness:1.16 ; self_correlation:0.3046 ; prodCorrelation:0.4765 ,pyramids:['AMR/D1/OTHER'] ;
region: GLB ;sharpe:2.0 ; fitness:1.58 ; self_correlation:0.4237 ; prodCorrelation:0.6824 ,pyramids:['GLB/D1/PV', 'GLB/D1/MACRO'] ;
PPA: 2个 ;
region: AMR ;sharpe:1.05 ; fitness:0.9 ; self_correlation:0.1607 ; prodCorrelation:0.2649 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.56 ; fitness:1.39 ; self_correlation:0.1897 ; prodCorrelation:0.3471 ,pyramids:['AMR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.64 ;
fitness: 5.25 ;
self: 0.6959 ;
prodCorrelation: 0.6959 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #63: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-06 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.3492333333333333 ;
RA: 0个 ;
PPA: 3个 ;
region: AMR ;sharpe:1.21 ; fitness:0.9 ; self_correlation:0.2254 ; prodCorrelation:0.3361 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.01 ; fitness:0.7 ; self_correlation:0.1808 ; prodCorrelation:0.3455 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.09 ; fitness:0.72 ; self_correlation:0.2509 ; prodCorrelation:0.3661 ,pyramids:['AMR/D1/FUNDAMENTAL'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 4.21 ;
fitness: 5.38 ;
self: 0.4857 ;
prodCorrelation: 0.4857 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #64: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-07 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4301 ;
RA: 0个 ;
PPA: 1个 ;
region: AMR ;sharpe:1.09 ; fitness:0.99 ; self_correlation:0.1532 ; prodCorrelation:0.4301 ,pyramids:['AMR/D1/PV', 'AMR/D1/OPTION'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 6.12 ;
fitness: 7.4 ;
self: 0.4167 ;
prodCorrelation: 0.4298 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #65: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-08 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.2722 ;
RA: 0个 ;
PPA: 1个 ;
region: AMR ;sharpe:1.07 ; fitness:1.06 ; self_correlation:0.1301 ; prodCorrelation:0.2722 ,pyramids:['AMR/D1/OPTION'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 7.04 ;
fitness: 6.92 ;
self: 0.2799 ;
prodCorrelation: 0.2865 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #66: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-09 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.3009 ;
RA: 0个 ;
PPA: 1个 ;
region: AMR ;sharpe:1.15 ; fitness:1.05 ; self_correlation:0.082 ; prodCorrelation:0.3009 ,pyramids:[ 'AMR/D1/ANALYST'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 8.03 ;
fitness: 8.3 ;
self: 0.4513 ;
prodCorrelation: 0.4513 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #67: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-10 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.3559 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:1.12 ; fitness:0.92 ; self_correlation:0.1217 ; prodCorrelation:0.3559 ,pyramids:['GLB/D1/ANALYST'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 5.07 ;
fitness: 5.08 ;
self: 0.4824 ;
prodCorrelation: 0.4824 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #68: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-11 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.5759 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:1.39 ; fitness:1.21 ; self_correlation:0.3732 ; prodCorrelation:0.5759 ,pyramids:['GLB/D1/FUNDAMENTAL'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.56 ;
fitness: 5.26 ;
self: 0.6138 ;
prodCorrelation: 0.6138 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #69: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-12 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.5959666666666666 ;
RA: 1个 ;
region: GLB ;sharpe:2.13 ; fitness:1.15 ; self_correlation:0.3281 ; prodCorrelation:0.6933 ,pyramids:['GLB/D1/ANALYST'] ;
PPA: 2个 ;
region: GLB ;sharpe:1.27 ; fitness:0.73 ; self_correlation:0.2515 ; prodCorrelation:0.4246 ,pyramids:['GLB/D1/MODEL'] ;
region: GLB ;sharpe:1.31 ; fitness:0.68 ; self_correlation:0.3273 ; prodCorrelation:0.67 ,pyramids:[ 'GLB/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 7.23 ;
fitness: 7.05 ;
self: 0.2022 ;
prodCorrelation: 0.4813 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #70: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-13 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.6604 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:2.06 ; fitness:1.11 ; self_correlation:0.5875 ; prodCorrelation:0.6604 ,pyramids:[ 'GLB/D1/ANALYST'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 8.52 ;
fitness: 8.9 ;
self: 0.4068 ;
prodCorrelation: 0.4335 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #71: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-14 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.822 ;
RA: 0个 ;
PPA: 1个 ;
region: EUR ;sharpe:2.52 ; fitness:1.6 ; self_correlation:0.6524 ; prodCorrelation:0.822 ,pyramids:['EUR/D1/RISK'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 7.45 ;
fitness: 8.53 ;
self: 0.3235 ;
prodCorrelation: 0.4091 ;

---

### 探讨 #72: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-15 
今天提交情况：
all_alpha_count: 0 ; avg_prod: 0 ;
RA: 0个 ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 5.47 ;
fitness: 5.34 ;
self: 0.4228 ;
prodCorrelation: 0.4828 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #73: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月5日

==================================================================================

ra没有产出的一天，sa正常提交了。感觉最近的回测脚本bug越来越多了，用的也不是很顺手，需要找时间优化下了

==================================================================================

---

### 探讨 #74: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月6日

==================================================================================

还是没有ra没有产出的一天，只提交了一个SA，丧气满满😧

等待q2级别结果中.....

==================================================================================

---

### 探讨 #75: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月7日

==================================================================================

拼拼凑凑，提交了一个RA，还有比赛的一个SA，丧气满满😧

等待q2级别结果中.....

==================================================================================

---

### 探讨 #76: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月8日

==================================================================================

工作好忙啊～～

晚上下班后抽时间微调了下SA ，提交了

RA 实在没有跑出好的，也没时间找了，就先这样吧

等待q2级别结果中.....

==================================================================================

---

### 探讨 #77: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月9日

==================================================================================

今天有了点时间，又是寻寻觅觅找RA中度过，提交了个一般的RA。

比赛SA正常提交。ATOM的SA PROD相关性都好低啊

等待q2级别结果中.....

==================================================================================

---

### 探讨 #78: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月10日

==================================================================================

现在每天尽量1个RA，1个SA了。没有找到比较好的模版，RA产生还是不理想，sad

等待q2级别结果中.....

==================================================================================

---

### 探讨 #79: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月11日

==================================================================================

定级结果出来了，顺利晋升～～

新级别的操作符和数据集好多啊，要改machine_lib 了，好想重构下整个流程框架，实现自动化一二阶啊

今天保持1个RA，1个SA 提交记录。

==================================================================================

---

### 探讨 #80: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月12日

==================================================================================

看了下操作符，好多陌生的啊，需要调整下框架，对操作符减枝下，分批回测了。

今天周六，对操作符梳理 了一遍，初步分好了不同批次的op 。明天要重新思考下实现整个回测流程自动化的代码框架了

今天保持1个RA，1个SA 提交记录。

==================================================================================

---

### 探讨 #81: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025年7月13日

==================================================================================

今天完成了整个一阶回测自动化，24小时回测的初步代码版本。以后有新增的模版，只需要按照格式生成回测表达式文件，然后放到回测目录下，更改下任务列表文件就可以了，再也不用手动切换不同模版回测，切换不同地区回测了～～～～～～～～～～～～～～～～～

今天保持1个RA，1个SA 提交记录。

==================================================================================

---

### 探讨 #82: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025年7月14日 我的量化日记 ==================================================================================

今天提交了2个usa 的ra, model+nws,指标还可以，Prod<0.7的；

super 这几天提交的都是own 的，ASI地区的，质量一般。

=============================保证提交质量，提交数量====================================

---

### 探讨 #83: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-01 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.619775 ;
RA: 3个 ;
region: GLB ;sharpe:2.39 ; fitness:1.7 ; self_correlation:0.3427 ; prodCorrelation:0.6934 ,pyramids:['GLB/D1/PV', 'GLB/D1/ANALYST'] ;
region: AMR ;sharpe:1.66 ; fitness:1.22 ; self_correlation:0.6946 ; prodCorrelation:0.6946 ,pyramids:[ 'AMR/D1/MODEL'] ;
region: AMR ;sharpe:1.75 ; fitness:1.22 ; self_correlation:0.2812 ; prodCorrelation:0.5785 ,pyramids:['AMR/D1/PV', 'AMR/D1/MODEL'] ;
PPA: 1个 ;
region: GLB ;sharpe:1.04 ; fitness:0.66 ; self_correlation:0.1973 ; prodCorrelation:0.5126 ,pyramids:['GLB/D1/SOCIALMEDIA', 'GLB/D1/SENTIMENT'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 4.57 ;
fitness: 5.86 ;
self: 0.5918 ;
prodCorrelation: 0.5918 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #84: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-02 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.622325 ;
RA: 1个 ;
region: GLB ;sharpe:2.49 ; fitness:1.25 ; self_correlation:0.5865 ; prodCorrelation:0.723 ,pyramids:['GLB/D1/SENTIMENT', 'GLB/D1/ANALYST'] ;
PPA: 3个 ;
region: GLB ;sharpe:1.38 ; fitness:0.79 ; self_correlation:0.2766 ; prodCorrelation:0.4637 ,pyramids:['GLB/D1/EARNINGS'] ;
region: GLB ;sharpe:1.54 ; fitness:1.54 ; self_correlation:0.4362 ; prodCorrelation:0.6361 ,pyramids:['GLB/D1/EARNINGS'] ;
region: GLB ;sharpe:1.68 ; fitness:1.08 ; self_correlation:0.2984 ; prodCorrelation:0.6665 ,pyramids:['GLB/D1/SOCIALMEDIA', 'GLB/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.8 ;
fitness: 6.33 ;
self: 0.6602 ;
prodCorrelation: 0.6602 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #85: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-03 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.48777499999999996 ;
RA: 0个 ;
PPA: 4个 ;
region: AMR ;sharpe:1.03 ; fitness:0.65 ; self_correlation:0.1392 ; prodCorrelation:0.3449 ,pyramids:['AMR/D1/NEWS'] ;
region: GLB ;sharpe:1.68 ; fitness:1.51 ; self_correlation:0.5797 ; prodCorrelation:0.6091 ,pyramids:['GLB/D1/MACRO'] ;
region: GLB ;sharpe:1.44 ; fitness:1.23 ; self_correlation:0.5369 ; prodCorrelation:0.6293 ,pyramids:['GLB/D1/SOCIALMEDIA', 'GLB/D1/MACRO'] ;
region: GLB ;sharpe:1.19 ; fitness:0.61 ; self_correlation:0.1783 ; prodCorrelation:0.3678 ,pyramids:['GLB/D1/EARNINGS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 6.0 ;
fitness: 6.48 ;
self: 0.6636 ;
prodCorrelation: 0.6636 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #86: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-04 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.4814333333333334 ;
RA: 1个 ;
region: AMR ;sharpe:1.64 ; fitness:1.17 ; self_correlation:0.5504 ; prodCorrelation:0.6049 ,pyramids:['AMR/D1/PV', 'AMR/D1/MODEL'] ;
PPA: 2个 ;
region: GLB ;sharpe:1.45 ; fitness:0.82 ; self_correlation:0.304 ; prodCorrelation:0.634 ,pyramids:['GLB/D1/PV', 'GLB/D1/RISK'] ;
region: AMR ;sharpe:1.26 ; fitness:1.02 ; self_correlation:0.1255 ; prodCorrelation:0.2054 ,pyramids:['AMR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.54 ;
fitness: 5.09 ;
self: 0.6766 ;
prodCorrelation: 0.6761 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #87: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-05 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.702675 ;
RA: 3个 ;
region: GLB ;sharpe:2.04 ; fitness:1.58 ; self_correlation:0.1217 ; prodCorrelation:0.6815 ,pyramids:['GLB/D1/RISK', 'GLB/D1/MODEL'] ;
region: GLB ;sharpe:2.15 ; fitness:1.19 ; self_correlation:0.1775 ; prodCorrelation:0.6837 ,pyramids:['GLB/D1/PV', 'GLB/D1/RISK'] ;
region: GLB ;sharpe:2.11 ; fitness:1.8 ; self_correlation:0.623 ; prodCorrelation:0.6454 ,pyramids:['GLB/D1/MACRO', 'GLB/D1/SENTIMENT'] ;
PPA: 1个 ;
region: IND ;sharpe:1.79 ; fitness:1.59 ; self_correlation:0.0 ; prodCorrelation:0.8001 ,pyramids:[ 'IND/D1/MODEL'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.57 ;
fitness: 6.81 ;
self: 0.4751 ;
prodCorrelation: 0.4751 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #88: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-06 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.6546750000000001 ;
RA: 2个 ;
region: IND ;sharpe:1.65 ; fitness:1.23 ; self_correlation:0.1269 ; prodCorrelation:0.3571 ,pyramids:['IND/D1/INSTITUTIONS'] ;
region: IND ;sharpe:1.74 ; fitness:1.35 ; self_correlation:0.0 ; prodCorrelation:0.5973 ,pyramids:['IND/D1/MODEL'] ;
PPA: 2个 ;
region: IND ;sharpe:1.28 ; fitness:1.12 ; self_correlation:0.2559 ; prodCorrelation:0.7414 ,pyramids:[ 'IND/D1/OTHER'] ;
region: IND ;sharpe:1.64 ; fitness:1.22 ; self_correlation:0.0 ; prodCorrelation:0.9229 ,pyramids:['IND/D1/MODEL'] ;

Superalpha:
region: IND  ;
is 指标:
sharpe: 7.34 ;
fitness: 12.88 ;
self: 0.0164 ;
prodCorrelation: 0.5152 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #89: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-01-07 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.3545 ;
RA: 2个 ;
region: IND ;sharpe:1.65 ; fitness:1.48 ; self_correlation:0.1381 ; prodCorrelation:0.2442 ,pyramids:[ 'IND/D1/OTHER'] ;
region: IND ;sharpe:2.33 ; fitness:2.29 ; self_correlation:0.1622 ; prodCorrelation:0.4715 ,pyramids:[ 'IND/D1/ANALYST'] ;
PPA: 2个 ;
region: IND ;sharpe:1.25 ; fitness:0.79 ; self_correlation:0.2436 ; prodCorrelation:0.3225 ,pyramids:['IND/D1/INSTITUTIONS'] ;
region: IND ;sharpe:1.1 ; fitness:1.03 ; self_correlation:0.1453 ; prodCorrelation:0.3798 ,pyramids:['IND/D1/OPTION'] ;

Superalpha:
region: IND  ;
is 指标:
sharpe: 6.12 ;
fitness: 8.49 ;
self: 0.3725 ;
prodCorrelation: 0.478 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #90: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

20250530 --

最近一直在摸索自己的模板，现有的模板已经无法产出了。希望能早点摸索出有新产出的模板。

昨天提交了一个sa超过0.7prod的，fit>5的，发现prod 惩罚也挺厉害的，少了接近2/3的base;看来还是要提交fit>5且prod<7的sa，才能有比較高的base了。

新上綫使用的labs，好卡啊，半个多小时才完成一个例子的实验，希望早点优化好，能流畅使用~~

---

### 探讨 #91: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

20250531  昨天提交了1个sa，20刀，勉强凑出来个ra，质量过得去，但是对performance增益基本无，还是提交了，已经断货好久了，只能保证不提交质量不过关的了。 坚持坚持~~继续探索新模板~~ sa 比赛要开始了，base多多来吧，我这有大大的口袋，装得下。

----------------------------------------------------------------------------

---

### 探讨 #92: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-01

今天的regular alpha没有提交，因为没有可以提交的，太难了啊！

还是继续探索自己的template中，希望早日解脱没有余粮的日子。

今天提交了最后一个sa的存货，优质sa，期待中午的base！

--------------------------------------------------------------------------

---

### 探讨 #93: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

20250602
难过，早上想check一个superalpha的时候，不小心点了提交，这是一个不符合我提交要求，回报低于10％的superalpha，而且，最大提交独立集明天不知道要减少多少比这个sa更好的sa，却由于相关性问题无法提交。

ra还是没有稳定的产出，继续探索模版。

---

### 探讨 #94: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-03

端午节过去了，3天埋头研究，还是没有弄出可产出的模版，好难啊。

今天交了一个regular alpha，表现应该还算合格。sa的比赛alpha，昨晚跑出来的sa，早上check，都过不了相关性检测，还没提交今天的sa，要是晚点还是没有合格的可提交的比赛sa，就只能提交下自己的非比赛sa了。

老爷保号，我的模板能产出多多。

-----------------------------------------

---

### 探讨 #95: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-03 晚上

晚上提交了一个ra，手误提交了一个烂的superalpha， ) : ;唉，一言难尽。今天的ra质量还可以，就是相关性挺高的。暂时没有挖出新的ra，只能翻翻垃圾堆，找下表现好的，超过已提交sharpe10%的alpha，提交了；

今天学到比较有用的知识是研究小组里面大佬们给讲解select 和combo的权重问题理解；解决了一些困惑。还是有一些疑惑的，关于sa的select部分。但是相比昨天，感觉对sa的select,combo规则理解更深入了一些了。

希望明天能有新产出的ra，sa。

---

### 探讨 #96: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025年0604 晚上 今天的superalpha提交了，fit7.x,prod 6.x, 非常感谢研究小组的同学和大佬对创建sa的讨论，让我今天终于感觉有点入门superalpha了，创建出来好多个趋势直线向上的pnl superalpha,后面几年的表现也没有衰退（G2组的sa,组出来普遍后面几年衰退明显），而且相关性也能过关，大部分0.6-0.7，偶尔有0.5几的prod，fit也都在5以上。不过我今天已经提交了sa了，后面再搓出比较好的，也没法交了。prod相关性变化太快了了。有信心明天继续创建出优秀的sa了，好开心。 今天的regular alpha还没着落呢，继续加油~~~~

---

### 探讨 #97: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-06 早上

昨天下午和晚上，提交了今天的superalpha, asi地区的，质量可以，我估计和昨天的sa base差不多。还提交了2个regular alpha，都是ppac标准的，质量在及格线的标准吧，不是特别好。现在每天都在想办法降低per op。之后还得将未使用的op也尽量用上，增加op数。

昨晚上的全球superalpha会议，学到了不少sa的combo使用方法，希望今天能搞出个质量好的 低corr sa来。

==============================================================

---

### 探讨 #98: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-06 晚上

下午更新的base，sa比预期的少了一些些，看了下各个指标，怀疑是self corr高了些，导致base少了点；

下午更新了combine，和上次没啥大区别，比较稳定。6号的sa ，下午提交了个fit>5,prod<5的，期待明天的base;没新的产出，从今天开始提交ppac标准的alpha了，alpha的质量算是在合格线的标准吧，今天提交了4个ra。明天继续挖挖挖，加油~~

================================================================================

---

### 探讨 #99: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================

2025-06-07  提交了1个sa和3个ppac标准的ra。

现有的template产出还是基本无，还是没有找到新的稳定产出的模板，继续摸索更换模板，加油

====================================================================================

---

### 探讨 #100: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================

2025-06-08

折腾了很久，弄出来一个prod<0.5,fit>5的sa，提交了，base还不错，sac比赛真是对非master,grandmaster的高vf人群的福利比赛！

提交了2个regular alpha,ppac标准的，prod<7的。

现有模板产出还不行，都得手动查找和调整，哎，心累

====================================================================================

---

### 探讨 #101: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================

2025-06-09

SAC G2的主题更换到risk neut了。这个主题的sa，性能都明显比simple好，随便组以下，最近几年的表现都很不错。手动回测了，知道一个prod 5.x的sa。sa的回测手动很费人力。晚上用了半个多小时的时间，把之前的sa代码，select,combo等都调整了下，用代码跑起来了。

晚上睡前看了下，找到一个prod<5，fit>5，性能中等的SA!赶紧提交了，比较手慢无。

regular alpha还是无产出，焦虑

提交了2个regular alpha,ppac标准的，prod<7的。

现有模板产出还不行，都得手动查找和调整，哎，心累

====================================================================================

---

### 探讨 #102: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

======================================================

2025-06-10

哎，晚上調整了好久，好不容易弄出个prod<0.5的sa，质量中等吧，没有及时提交，想着修改下select，看看能不能优化下，结果等回测完，发现没有优化到，想着直接原来那个提交算了。再次单独check了下prod,还是4.7x,就提交了，结果发现提交上去后，prod变成5.5了！晴天霹雳，以后再也不乱搞了，一旦发现质量过得去，prod<5的sa，立马提交！这个sa的base，才12刀，对比之前prod<0.5的四十多刀，简直令人心塞

=============================================================================

---

### 探讨 #103: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025-06-11：

今天提交了1个RAM主题的RA，自相关0.40，prod 0.64,指标如下,base有8.9刀，看来RAM的加成确实很厉害，希望接下来主题区间能每天都有可提交的RAM alpha.


> [!NOTE] [图片 OCR 识别内容]
> 015 SUmmary
> Perlod
> 15 
> Theme: RAM Neutralization Theme X2
> Single Data Set Alpha
> Pyramid theme: EURIDIIFUNDAMENTAL X1.1
> Iggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.81
> 6.55%
> 1.09
> 4.54%
> 3.35%
> 13.86%o。


比赛的SA，提交了个加分不高的，但是base比较高的SA，开心～～

努力找alpha,优化六维指标，希望能上M（可能性比较小 (( ; ）

==================================================================================

---

### 探讨 #104: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

=================================================================================

=================================================================================

2025年6月12号

ra还是零星产出，每天都在发愁明天哪里来的ra 提交呢？还得努力优化六维。

今天simple 上周主题的sa比赛结果出来了，课代表还真是强啊，小组第二名！

向课代表学习，加油呀，顾问 顾问 SZ83096 (Rank 13) (Rank 13) !

=================================================================================================================================================================

---

### 探讨 #105: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================

2025-06-13 晚上

昨天提交了比赛sa，和3个prod超过0.7的ppac，prod高的base惩罚真高啊，但是为了六维，还是提交了。

上周六开始换了新模板，每天有1,2个产出吧，但是可能是使用的操作符计算复杂度非常高，昨天的回测量才1.6万，等有空了得看看是不是代码有问题还是op导致的回测慢。

明天的sa，晚上也提交了，sac比赛真是gold的福利局~~~

明天的ra，还在调整中~~

================================================================================

---

### 探讨 #106: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==============================================================================

2025-06-14

今天提交了一个比赛的sa，5.2的fit，加分不多，pnl趋势整体向上，但是prod比较低。

出来玩，没有多少时间可以调整ra，只匆忙交了一个相关性比较高的ppac，质量过关.

希望每天都能至少交一个suepralpha alpha和一个regular alpha，come on !

=============================================================================

---

### 探讨 #107: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================

量化日记 2025年6月15号：

今天提交完最后一个risk 主题的superalpha，和2个Prod < 7的regular alpha（吃老本 ((: ）;预计明天的base会比较高，开心~~~~~~~~~~~~~

弄完后就出去玩啦~~~

================================================================================

---

### 探讨 #108: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================

2025年6月16号 量化日记

今天提交了1个SA和1个regular alpha，保持每天1个SA 和1个RA 的节奏。

每天中午1点30分看着昨天提交的alpha的base，真开心啊~~~

================================================================================

---

### 探讨 #109: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

===============================================================================

2025年6月17号

regular alpha一直基本产出很少，还剩半个月就定级了，还得优化下6维指标，但是没有可以提交的 ra，ppac，捉急啊！

super alpha 比赛真好啊，每天一个sa，美滋滋

==================================================================================

---

### 探讨 #110: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月18号

今天是回程的时间，在高铁上提交了美东时间18号的SA 和2个高prod 的ppac，regular alpha的产出一如即往的稳定，基本没有，等周末了要重新规划下模版了，哎，挖矿难，难于上青天

==================================================================================

---

### 探讨 #111: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月19号

美东19号的sa 提交了，预计base应该不错。

今天的regular alpha还没有着落呢。

genius排名，持续掉，还是得交质量合格的regular啊，优化六维指标 ::(

==================================================================================

---

### 探讨 #112: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月20号

今天弄不出pc<0.5的sa了， 提交了一个prod 0.55,returns 23%的sa。

regular alpha,提交了一个pc 小于0.7的，质量ok

继续优化六维的一天

==================================================================================

---

### 探讨 #113: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月21号

真是令人意外，pc 为0.55的SA ,有40刀的base。猜测是returns毕竟高？之前没有提交过这么高returns的sA ,今天依然找不出prod<0.5的，提交了个returns 29的SA，验证下猜想。

昨天的ra，1个8.5刀，美滋滋；

今天也是努力优化六维的一天，提交了4个质量很一般的ra。☹️

==================================================================================

---

### 探讨 #114: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月22号

昨天的猜测有应该有一半的概率是准的。pc 6.x，returns 29，base有34刀，比一般pc>0.5,fit>5的sa 的20刀，还是base增加挺明显的。

昨天的4个ra，base 9.78刀，哎，好低啊，坚持✊

今天也是努力优化六维的一天 ☹️

==================================================================================

---

### 探讨 #115: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月23号

今天的sa base很nice😄。 G2开始HCAC主题的一周，头秃，alpha数量少，相关性好高啊，先手动搓几个试试看吧。

今天也是努力优化六维的一天 ☹️

==================================================================================

---

### 探讨 #116: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月24号

今天只提交了一个SA，returns比较高，6.x的prod,base还不错。

不想交自己都觉得不行的alpha了，暂停提交吧。看啥时候排名不行了再提交，实在没有好的regular alpha可提交的。

今天是一直刷genius排名，关注排名跌了多少的一天 ☹️

==================================================================================

---

### 探讨 #117: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月25号

昨天提交的SA，base暴跌。对比了下昨天和前天提交的SA，没看出太大的差别，is指标，pnl走势以及prod corr，基本没明显差别，但是base暴跌，怀疑是自相关超过0.5了，以后提交SA，尽量提交自相关小于5的SA 吧。

继续手搓SA ～～

今天也是一直刷genius排名，关注排名跌了多少的一天 ☹️

==================================================================================

---

### 探讨 #118: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月26号

昨天提交了1个fit>5,prod 6.x的SA，1个ra；SA 的base nice；ra的质量堪忧，base有点低。

提交self corr <0.5,returns >15,质量过关的SA ，base一般都挺不错的。

今天也是努力优化六维的一天 ☹️

==================================================================================

---

### 探讨 #119: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月27号

今天没提交ra，只提交了1个super alpha。晚上在各种调整SA的时候，想努力把self corr降低 到 0.5以下，出乎意料得弄出来个fit>5,prod<5的SA ......

生活处处有惊喜

今天看排名，没有跌那么快了，暂停ra的提交

==================================================================================

---

### 探讨 #120: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月28号

第二季度还有3天，3天就结束了！！！希望能升级M ，努力保住当前排名中。

今天的回测持续异常，4个小时了，只成功了500多个 alpha。

superalpha的回测似乎不受影响，先弄下sa,把今天的sa提交了先。

==================================================================================

---

### 探讨 #121: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================================================

2025年6月29号

第二季度还有2天，2天就结束了！！！希望能升级M ，努力保住当前排名中。

今天更新vf了！降低了0.01，比预期的好很多，开心～～

今天的SA和RA还没着落呢，我挖挖挖，努力的挖，吭哧吭哧吭哧

==================================================================================

---

### 探讨 #122: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

================================================================================== 2025年6月30号 第二季度还有1天，1天就结束了！！！希望能升级M ，努力保住当前排名中。 早上交了HCAC 主题的最后sa，质量合格吧，但是不算很优秀。self corr低于0.5的，希望base好看些。 为了保住6维，提交了2个ra，质量过关。不是近期挖出来的，翻垃圾堆发现的！真是处处有惊喜～～ ==================================================================================

---

### 探讨 #123: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-09 
今天提交情况：
RA: 0个 ;
PPA: 3个 ;
region: USA ;sharpe:1.08 ; fitness:0.77 ; self_correlation:0.2859 ; prodCorrelation:0.6864 ,pyramids:['USA/D1/MACRO'] ;
region: AMR ;sharpe:1.32 ; fitness:0.92 ; self_correlation:0.0557 ; prodCorrelation:0.7997 ,pyramids:['AMR/D1/RISK'] ;
region: AMR ;sharpe:1.7 ; fitness:1.37 ; self_correlation:0.2128 ; prodCorrelation:0.8185 ,pyramids:['AMR/D1/RISK'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 6.86 ;
fitness: 7.88 ;
self: 0.292 ;
prodCorrelation: 0.292 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #124: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-10 
今天提交情况：
RA: 1个 ;
region: AMR ;sharpe:1.6 ; fitness:1.28 ; self_correlation:0.2026 ; prodCorrelation:0.5159 ,pyramids:['AMR/D1/PV', 'AMR/D1/RISK'] ;
PPA: 3个 ;
region: AMR ;sharpe:1.22 ; fitness:0.78 ; self_correlation:0.1862 ; prodCorrelation:0.2251 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.37 ; fitness:0.89 ; self_correlation:0.2059 ; prodCorrelation:0.2599 ,pyramids:['AMR/D1/PV', 'AMR/D1/ANALYST'] ;
region: GLB ;sharpe:1.54 ; fitness:1.2 ; self_correlation:0.3977 ; prodCorrelation:0.5762 ,pyramids:['GLB/D1/FUNDAMENTAL'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 7.42 ;
fitness: 8.32 ;
self: 0.4063 ;
prodCorrelation: 0.482 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #125: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-11 
今天提交情况：
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:1.7 ; fitness:0.99 ; self_correlation:0.2039 ; prodCorrelation:0.5745 ,pyramids:['GLB/D1/RISK', 'GLB/D1/OPTION'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.36 ;
fitness: 5.94 ;
self: 0.6445 ;
prodCorrelation: 0.6445 ;

---

### 探讨 #126: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-12 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: AMR ;sharpe:1.16 ; fitness:0.93 ; self_correlation:0.2197 ; prodCorrelation:0.2197 ,pyramids:[ 'AMR/D1/SENTIMENT'] ;
region: AMR ;sharpe:1.15 ; fitness:1.04 ; self_correlation:0.2168 ; prodCorrelation:0.2168 ,pyramids:['AMR/D1/SENTIMENT'] ;
region: AMR ;sharpe:1.22 ; fitness:0.91 ; self_correlation:0.4121 ; prodCorrelation:0.4121 ,pyramids:['AMR/D1/SENTIMENT'] ;
region: GLB ;sharpe:1.17 ; fitness:0.84 ; self_correlation:0.148 ; prodCorrelation:0.3594 ,pyramids:['GLB/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.3 ;
fitness: 5.04 ;
self: 0.4003 ;
prodCorrelation: 0.4003 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #127: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-13 
今天提交情况：
RA: 3个 ;
region: USA ;sharpe:1.76 ; fitness:1.44 ; self_correlation:0.4782 ; prodCorrelation:0.487 ,pyramids:['USA/D1/OPTION'] ;
region: USA ;sharpe:1.88 ; fitness:1.62 ; self_correlation:0.6212 ; prodCorrelation:0.6802 ,pyramids:['USA/D1/OPTION'] ;
region: USA ;sharpe:2.0 ; fitness:2.31 ; self_correlation:0.617 ; prodCorrelation:0.6835 ,pyramids:['USA/D1/OPTION'] ;
PPA: 1个 ;
region: AMR ;sharpe:1.17 ; fitness:0.9 ; self_correlation:0.3119 ; prodCorrelation:0.594 ,pyramids:['AMR/D1/NEWS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.04 ;
fitness: 5.37 ;
self: 0.4715 ;
prodCorrelation: 0.4727 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #128: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-14 
今天提交情况：
RA: 0个 ;
PPA: 2个 ;
region: USA ;sharpe:1.57 ; fitness:0.93 ; self_correlation:0.4081 ; prodCorrelation:0.5932 ,pyramids:['USA/D1/ANALYST'] ;
region: USA ;sharpe:1.21 ; fitness:1.13 ; self_correlation:0.2096 ; prodCorrelation:0.5914 ,pyramids:['USA/D1/ANALYST'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.74 ;
fitness: 5.92 ;
self: 0.2426 ;
prodCorrelation: 0.388 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #129: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-10-15 
今天提交情况：
RA: 0个 ;
PPA: 1个 ;
region: USA ;sharpe:1.4 ; fitness:1.34 ; self_correlation:0.2482 ; prodCorrelation:0.6589 ,pyramids:['USA/D1/MACRO', 'USA/D1/FUNDAMENTAL'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.94 ;
fitness: 6.62 ;
self: 0.2873 ;
prodCorrelation: 0.2924 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #130: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-16 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4712 ;
RA: 1个 ;
region: EUR ;sharpe:1.84 ; fitness:1.17 ; self_correlation:0.1804 ; prodCorrelation:0.4712 ,pyramids:['EUR/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.85 ;
fitness: 6.49 ;
self: 0.6881 ;
prodCorrelation: 0.6881 ;

---

### 探讨 #131: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-17 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.3388 ;
RA: 0个 ;
PPA: 1个 ;
region: AMR ;sharpe:1.22 ; fitness:0.89 ; self_correlation:0.2309 ; prodCorrelation:0.3388 ,pyramids:['AMR/D1/NEWS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 6.0 ;
fitness: 6.81 ;
self: 0.5722 ;
prodCorrelation: 0.5722 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #132: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-18 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.1492 ;
RA: 0个 ;
PPA: 1个 ;
region: AMR ;sharpe:1.0 ; fitness:0.81 ; self_correlation:0.1095 ; prodCorrelation:0.1492 ,pyramids:['AMR/D1/SENTIMENT'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.93 ;
fitness: 5.26 ;
self: 0.6259 ;
prodCorrelation: 0.6259 ;

---

### 探讨 #133: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-19 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.5458 ;
RA: 1个 ;
region: EUR ;sharpe:2.13 ; fitness:1.16 ; self_correlation:0.2667 ; prodCorrelation:0.5458 ,pyramids:['EUR/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 5.37 ;
fitness: 5.41 ;
self: 0.4738 ;
prodCorrelation: 0.4738 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #134: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-20 
今天提交情况：
all_alpha_count: 0 ; avg_prod: 0 ;
RA: 0个 ;
PPA: 0个;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 9.23 ;
fitness: 9.81 ;
self: 0.3403 ;
prodCorrelation: 0.4774 ;

---

### 探讨 #135: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-21 
今天提交情况：
all_alpha_count: 0 ; avg_prod: 0 ;
RA: 0个 ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 7.93 ;
fitness: 9.12 ;
self: 0.4993 ;
prodCorrelation: 0.4993 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #136: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-22 
今天提交情况：
all_alpha_count: 0 ; avg_prod: 0 ;
RA: 0个 ;
PPA: 0个;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.2 ;
fitness: 5.49 ;
self: 0.6315 ;
prodCorrelation: 0.6315 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #137: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6 months ago

-----------------------------------橘子的量化日记 -------------------------------------
 2025-12-23 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4022 ;
RA: 1个 ;
region: GLB ;sharpe:1.84 ; fitness:1.39 ; self_correlation:0.2605 ; prodCorrelation:0.4022 ,pyramids:['GLB/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 4.18 ;
fitness: 5.31 ;
self: 0.4246 ;
prodCorrelation: 0.4246 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #138: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-09 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4543 ;
RA: 0个 ;
PPA: 1个 ;
region: ASI ;sharpe:1.72 ; fitness:1.37 ; self_correlation:0.2457 ; prodCorrelation:0.4543 ,pyramids:['ASI/D1/PV', 'ASI/D1/OTHER'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 4.5 ;
fitness: 5.01 ;
self: 0.6579 ;
prodCorrelation: 0.6579 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #139: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-10 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.5865 ;
RA: 1个 ;
region: EUR ;sharpe:1.58 ; fitness:1.18 ; self_correlation:0.441 ; prodCorrelation:0.5865 ,pyramids:['EUR/D1/MODEL'] ;
PPA: 0个;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 6.66 ;
fitness: 8.38 ;
self: 0.2877 ;
prodCorrelation: 0.2877 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #140: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-11 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.3645 ;
RA: 0个 ;
PPA: 1个 ;
region: EUR ;sharpe:1.4 ; fitness:0.7 ; self_correlation:0.1487 ; prodCorrelation:0.3645 ,pyramids:['EUR/D1/PV', 'EUR/D1/NEWS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.09 ;
fitness: 5.43 ;
self: 0.6928 ;
prodCorrelation: 0.6928 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #141: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-12 
今天提交情况：
all_alpha_count: 2 ; avg_prod: 0.6476999999999999 ;
RA: 2个 ;
region: ASI ;sharpe:2.1 ; fitness:1.07 ; self_correlation:0.3058 ; prodCorrelation:0.6917 ,pyramids:['ASI/D1/OTHER'] ;
region: ASI ;sharpe:1.73 ; fitness:1.09 ; self_correlation:0.1347 ; prodCorrelation:0.6037 ,pyramids:['ASI/D1/PV', 'ASI/D1/OTHER'] ;
PPA: 0个;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.83 ;
fitness: 5.29 ;
self: 0.6758 ;
prodCorrelation: 0.6856 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #142: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-13 
今天提交情况：
all_alpha_count: 2 ; avg_prod: 0.5973999999999999 ;
RA: 1个 ;
region: EUR ;sharpe:1.82 ; fitness:1.1 ; self_correlation:0.2797 ; prodCorrelation:0.6253 ,pyramids:['EUR/D1/MODEL'] ;
PPA: 1个 ;
region: EUR ;sharpe:1.13 ; fitness:0.53 ; self_correlation:0.1786 ; prodCorrelation:0.5695 ,pyramids:[ 'EUR/D1/OTHER'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 6.94 ;
fitness: 6.63 ;
self: 0.2304 ;
prodCorrelation: 0.2665 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #143: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-14 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4781 ;
RA: 0个 ;
PPA: 1个 ;
region: EUR ;sharpe:1.09 ; fitness:0.8 ; self_correlation:0.13 ; prodCorrelation:0.4781 ,pyramids:['EUR/D1/SHORTINTEREST', 'EUR/D1/OTHER'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 7.66 ;
fitness: 6.96 ;
self: 0.1802 ;
prodCorrelation: 0.2773 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #144: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-15 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.6808 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:1.74 ; fitness:0.98 ; self_correlation:0.1805 ; prodCorrelation:0.6808 ,pyramids:['GLB/D1/PV', 'GLB/D1/RISK'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.34 ;
fitness: 5.25 ;
self: 0.4354 ;
prodCorrelation: 0.4354 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #145: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-16 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.6893333333333334 ;
RA: 2个 ;
region: ASI ;sharpe:2.47 ; fitness:1.58 ; self_correlation:0.1543 ; prodCorrelation:0.7239 ,pyramids:['ASI/D1/SHORTINTEREST'] ;
region: EUR ;sharpe:1.58 ; fitness:1.11 ; self_correlation:0.4916 ; prodCorrelation:0.6853 ,pyramids:['EUR/D1/SHORTINTEREST']  ;
PPA: 1个 ;
region: ASI ;sharpe:1.17 ; fitness:1.07 ; self_correlation:0.4921 ; prodCorrelation:0.6588 ,pyramids:['ASI/D1/RISK', 'ASI/D1/SENTIMENT'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 6.94 ;
fitness: 8.19 ;
self: 0.396 ;
prodCorrelation: 0.4293 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #146: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-17 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.8054 ;
RA: 0个 ;
PPA: 1个 ;
region: ASI ;sharpe:1.39 ; fitness:1.05 ; self_correlation:0.355 ; prodCorrelation:0.8054 ,pyramids:['ASI/D1/SHORTINTEREST'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 6.53 ;
fitness: 7.85 ;
self: 0.4464 ;
prodCorrelation: 0.4966 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #147: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-18 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.2698 ;
RA: 0个 ;
PPA: 1个 ;
region: ASI ;sharpe:1.29 ; fitness:0.98 ; self_correlation:0.0968 ; prodCorrelation:0.2698 ,pyramids:['ASI/D1/NEWS'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 4.89 ;
fitness: 5.42 ;
self: 0.5982 ;
prodCorrelation: 0.6544 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #148: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-19 
今天提交情况：
all_alpha_count: 2 ; avg_prod: 0.4854 ;
RA: 0个 ;
PPA: 2个 ;
region: EUR ;sharpe:1.04 ; fitness:0.62 ; self_correlation:0.2075 ; prodCorrelation:0.6491 ,pyramids:['EUR/D1/MACRO'] ;
region: ASI ;sharpe:1.08 ; fitness:0.86 ; self_correlation:0.1144 ; prodCorrelation:0.3217 ,pyramids:['ASI/D1/NEWS'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.5 ;
fitness: 6.75 ;
self: 0.2437 ;
prodCorrelation: 0.2816 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #149: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-20 
今天提交情况：
all_alpha_count: 2 ; avg_prod: 0.48885 ;
RA: 0个 ;
PPA: 2个 ;
region: EUR ;sharpe:1.19 ; fitness:1.0 ; self_correlation:0.1742 ; prodCorrelation:0.4998 ,pyramids:['EUR/D1/INSIDERS'] ;
region: EUR ;sharpe:1.1 ; fitness:0.66 ; self_correlation:0.1191 ; prodCorrelation:0.4779 ,pyramids:['EUR/D1/INSIDERS'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 4.89 ;
fitness: 5.06 ;
self: 0.5176 ;
prodCorrelation: 0.5851 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #150: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-11-21 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.5484333333333333 ;
RA: 0个 ;
PPA: 3个 ;
region: GLB ;sharpe:1.54 ; fitness:1.3 ; self_correlation:0.36 ; prodCorrelation:0.6925 ,pyramids:['GLB/D1/EARNINGS'] ;
region: GLB ;sharpe:1.21 ; fitness:0.78 ; self_correlation:0.1013 ; prodCorrelation:0.4561 ,pyramids:['GLB/D1/EARNINGS'] ;
region: EUR ;sharpe:1.17 ; fitness:0.7 ; self_correlation:0.2482 ; prodCorrelation:0.4967 ,pyramids:['EUR/D1/INSIDERS'] ;

Superalpha:
region: USA  ;
is 指标:
sharpe: 6.01 ;
fitness: 6.81 ;
self: 0.2685 ;
prodCorrelation: 0.4191 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #151: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-02-25 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.608475 ;
RA: 4个 ;
region: USA ;sharpe:1.82 ; fitness:1.72 ; self_correlation:0.3124 ; prodCorrelation:0.6075 ,pyramids:['USA/D1/FUNDAMENTAL'] ;
region: USA ;sharpe:1.59 ; fitness:1.0 ; self_correlation:0.5059 ; prodCorrelation:0.6995 ,pyramids:['USA/D1/INSIDERS'] ;
region: EUR ;sharpe:1.68 ; fitness:1.08 ; self_correlation:0.5107 ; prodCorrelation:0.595 ,pyramids:['EUR/D1/ANALYST'] ;
region: USA ;sharpe:1.58 ; fitness:1.18 ; self_correlation:0.2185 ; prodCorrelation:0.5319 ,pyramids:[ 'USA/D1/FUNDAMENTAL'] ;
PPA: 0个;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.57 ;
fitness: 5.23 ;
self: 0.6485 ;
prodCorrelation: 0.6403 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #152: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-02-26 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.696 ;
RA: 1个 ;
region: EUR ;sharpe:1.78 ; fitness:1.06 ; self_correlation:0.6916 ; prodCorrelation:0.696 ,pyramids:[ 'EUR/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.87 ;
fitness: 6.0 ;
self: 0.6953 ;
prodCorrelation: 0.6953 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #153: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-02-27 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.5942000000000001 ;
RA: 1个 ;
region: EUR ;sharpe:1.87 ; fitness:1.12 ; self_correlation:0.3708 ; prodCorrelation:0.4828 ,pyramids:['EUR/D1/ANALYST'] ;
PPA: 3个 ;
region: EUR ;sharpe:1.18 ; fitness:0.67 ; self_correlation:0.2098 ; prodCorrelation:0.4736 ,pyramids:[ 'EUR/D1/NEWS'] ;
region: EUR ;sharpe:1.19 ; fitness:0.77 ; self_correlation:0.6634 ; prodCorrelation:0.6912 ,pyramids:['EUR/D1/RISK'] ;
region: EUR ;sharpe:1.36 ; fitness:0.67 ; self_correlation:0.7292 ; prodCorrelation:0.7292 ,pyramids:['EUR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.26 ;
fitness: 5.18 ;
self: 0.6712 ;
prodCorrelation: 0.6712 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #154: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-02-28 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.5056 ;
RA: 0个 ;
PPA: 1个 ;
region: EUR ;sharpe:1.36 ; fitness:1.04 ; self_correlation:0.2732 ; prodCorrelation:0.5056 ,pyramids:['EUR/D1/OPTION', 'EUR/D1/NEWS'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.53 ;
fitness: 5.44 ;
self: 0.3027 ;
prodCorrelation: 0.4163 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #155: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-01 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4171 ;
RA: 0个 ;
PPA: 1个 ;
region: EUR ;sharpe:1.31 ; fitness:0.64 ; self_correlation:0.1647 ; prodCorrelation:0.4171 ,pyramids:['EUR/D1/ANALYST'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 7.56 ;
fitness: 6.8 ;
self: 0.3781 ;
prodCorrelation: 0.4898 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #156: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-02 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.429 ;
RA: 1个 ;
region: EUR ;sharpe:1.67 ; fitness:1.29 ; self_correlation:0.1957 ; prodCorrelation:0.429 ,pyramids:['EUR/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: N/A  ;
is 指标:
sharpe: N/A ;
fitness: N/A ;
self: N/A ;
prodCorrelation: N/A ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #157: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-03 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.6548999999999999 ;
RA: 2个 ;
region: EUR ;sharpe:1.65 ; fitness:1.03 ; self_correlation:0.4833 ; prodCorrelation:0.6305 ,pyramids:['EUR/D1/ANALYST'] ;
region: EUR ;sharpe:1.72 ; fitness:1.13 ; self_correlation:0.2148 ; prodCorrelation:0.6845 ,pyramids:['EUR/D1/NEWS'] ;
PPA: 2个 ;
region: GLB ;sharpe:1.57 ; fitness:1.61 ; self_correlation:0.4485 ; prodCorrelation:0.6847 ,pyramids:['GLB/D1/RISK'] ;
region: EUR ;sharpe:1.1 ; fitness:0.55 ; self_correlation:0.3355 ; prodCorrelation:0.6199 ,pyramids:['EUR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.25 ;
fitness: 4.48 ;
self: 0.6633 ;
prodCorrelation: 0.6633 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #158: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-04 
今天提交情况：
all_alpha_count: 2 ; avg_prod: 0.5211 ;
RA: 1个 ;
region: EUR ;sharpe:1.87 ; fitness:1.2 ; self_correlation:0.3836 ; prodCorrelation:0.6962 ,pyramids:['EUR/D1/MODEL'] ;
PPA: 1个 ;
region: EUR ;sharpe:1.45 ; fitness:0.85 ; self_correlation:0.1805 ; prodCorrelation:0.346 ,pyramids:['EUR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.07 ;
fitness: 4.67 ;
self: 0.698 ;
prodCorrelation: 0.698 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #159: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-05 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.4440666666666666 ;
RA: 0个 ;
PPA: 3个 ;
region: GLB ;sharpe:1.51 ; fitness:1.73 ; self_correlation:0.3871 ; prodCorrelation:0.5114 ,pyramids:['GLB/D1/ANALYST'] ;
region: GLB ;sharpe:1.27 ; fitness:1.12 ; self_correlation:0.1765 ; prodCorrelation:0.3954 ,pyramids:['GLB/D1/FUNDAMENTAL'] ;
region: EUR ;sharpe:1.23 ; fitness:0.87 ; self_correlation:0.1519 ; prodCorrelation:0.4254 ,pyramids:['EUR/D1/ANALYST'] ;

Superalpha: 0 个
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #160: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-06 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.7231749999999999 ;
RA: 1个 ;
region: EUR ;sharpe:1.61 ; fitness:1.61 ; self_correlation:0.6761 ; prodCorrelation:0.6761 ,pyramids:['EUR/D1/PV', 'EUR/D1/ANALYST'] ;
PPA: 3个 ;
region: GLB ;sharpe:1.51 ; fitness:1.49 ; self_correlation:0.6839 ; prodCorrelation:0.6839 ,pyramids:['GLB/D1/FUNDAMENTAL'] ;
region: EUR ;sharpe:1.31 ; fitness:0.78 ; self_correlation:0.4454 ; prodCorrelation:0.6694 ,pyramids:['EUR/D1/RISK'] ;
region: EUR ;sharpe:1.54 ; fitness:1.22 ; self_correlation:0.4825 ; prodCorrelation:0.8633 ,pyramids:['EUR/D1/RISK'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.91 ;
fitness: 4.13 ;
self: 0.6914 ;
prodCorrelation: 0.6914 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #161: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-07 
今天提交情况：
all_alpha_count: 2 ; avg_prod: 0.3735 ;
RA: 0个 ;
PPA: 2个 ;
region: GLB ;sharpe:1.2 ; fitness:1.23 ; self_correlation:0.1169 ; prodCorrelation:0.295 ,pyramids:['GLB/D1/OTHER'] ;
region: EUR ;sharpe:1.22 ; fitness:0.8 ; self_correlation:0.165 ; prodCorrelation:0.452 ,pyramids:['EUR/D1/FUNDAMENTAL'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.59 ;
fitness: 3.95 ;
self: 0.6904 ;
prodCorrelation: 0.6904 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #162: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-08 
今天提交情况：
all_alpha_count: 4 ; avg_prod: 0.421925 ;
RA: 4个 ;
region: AMR ;sharpe:1.6 ; fitness:1.37 ; self_correlation:0.2991 ; prodCorrelation:0.371 ,pyramids:['AMR/D1/RISK'] ;
region: EUR ;sharpe:1.7 ; fitness:1.03 ; self_correlation:0.3992 ; prodCorrelation:0.5551 ,pyramids:['EUR/D1/NEWS'] ;
region: AMR ;sharpe:1.58 ; fitness:1.29 ; self_correlation:0.3717 ; prodCorrelation:0.4693 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.62 ; fitness:1.35 ; self_correlation:0.1689 ; prodCorrelation:0.2923 ,pyramids:['AMR/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 5.03 ;
fitness: 5.1 ;
self: 0.4548 ;
prodCorrelation: 0.4887 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #163: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-09 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.2309 ;
RA: 1个 ;
region: AMR ;sharpe:1.58 ; fitness:1.25 ; self_correlation:0.1186 ; prodCorrelation:0.2309 ,pyramids:['AMR/D1/RISK'] ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.74 ;
fitness: 7.12 ;
self: 0.3421 ;
prodCorrelation: 0.3897 ;

---

### 探讨 #164: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-10 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.63 ;
RA: 1个 ;
region: EUR ;sharpe:1.79 ; fitness:1.23 ; self_correlation:0.3142 ; prodCorrelation:0.63 ,pyramids:['EUR/D1/OTHER'] ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 7.34 ;
fitness: 6.45 ;
self: 0.4557 ;
prodCorrelation: 0.4679 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #165: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-11 
今天提交情况：
all_alpha_count: 3 ; avg_prod: 0.5005333333333334 ;
RA: 3个 ;
region: EUR ;sharpe:1.61 ; fitness:1.32 ; self_correlation:0.2209 ; prodCorrelation:0.4839 ,pyramids:['EUR/D1/NEWS'] ;
region: EUR ;sharpe:1.6 ; fitness:1.01 ; self_correlation:0.2211 ; prodCorrelation:0.524 ,pyramids:['EUR/D1/ANALYST'] ;
region: EUR ;sharpe:1.75 ; fitness:1.19 ; self_correlation:0.2019 ; prodCorrelation:0.4937 ,pyramids:['EUR/D1/ANALYST'] ;
PPA: 0个;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.44 ;
fitness: 5.36 ;
self: 0.4162 ;
prodCorrelation: 0.4162 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #166: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-12 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.4952 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:1.05 ; fitness:0.75 ; self_correlation:0.2489 ; prodCorrelation:0.4952 ,pyramids:['GLB/D1/ANALYST'] ;

Superalpha:
region: GLB  ;
is 指标:
sharpe: 6.86 ;
fitness: 6.85 ;
self: 0.4795 ;
prodCorrelation: 0.4965 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #167: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2026-03-13 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.6145 ;
RA: 0个 ;
PPA: 1个 ;
region: GLB ;sharpe:2.27 ; fitness:3.17 ; self_correlation:0.4698 ; prodCorrelation:0.6145 ,pyramids:['GLB/D1/RISK'] ;

----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #168: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-07 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: EUR ;sharpe:1.62 ; fitness:1.52 ; self_correlation:0.1109 ; prodCorrelation:0.5086 ,pyramids:['EUR/D1/SENTIMENT'] ;
region: GLB ;sharpe:1.03 ; fitness:0.65 ; self_correlation:0.173 ; prodCorrelation:0.931 ,pyramids:['GLB/D1/SHORTINTEREST', 'GLB/D1/SOCIALMEDIA'] ;
region: GLB ;sharpe:2.15 ; fitness:1.28 ; self_correlation:0.3008 ; prodCorrelation:0.981 ,pyramids:['GLB/D1/EARNINGS'] ;
region: GLB ;sharpe:1.3 ; fitness:0.94 ; self_correlation:0.411 ; prodCorrelation:0.849 ,pyramids:['GLB/D1/EARNINGS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.5 ;
fitness: 6.3 ;
self: 0.1957 ;
prodCorrelation: 0.4687 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #169: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-08 
今天提交情况：
RA: 1个 ;
region: EUR ;sharpe:2.13 ; fitness:1.41 ; self_correlation:0.1337 ; prodCorrelation:0.6761 ,pyramids:[ 'EUR/D1/EARNINGS'] ;
PPA: 3个 ;
region: EUR ;sharpe:1.96 ; fitness:1.27 ; self_correlation:0.6821 ; prodCorrelation:0.8785 ,pyramids:['EUR/D1/MACRO'] ;
region: AMR ;sharpe:1.64 ; fitness:1.37 ; self_correlation:0.0 ; prodCorrelation:0.8479 ,pyramids:['AMR/D1/MODEL'] ;
region: EUR ;sharpe:1.68 ; fitness:0.97 ; self_correlation:0.1571 ; prodCorrelation:0.6871 ,pyramids:['EUR/D1/SENTIMENT'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.75 ;
fitness: 5.16 ;
self: 0.644 ;
prodCorrelation: 0.644 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #170: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-09 
今天提交情况：
RA: 1个 ;
region: AMR ;sharpe:1.75 ; fitness:1.51 ; self_correlation:0.0 ; prodCorrelation:0.6285 ,pyramids:['AMR/D1/RISK', 'AMR/D1/MODEL'] ;
PPA: 3个 ;
region: AMR ;sharpe:1.19 ; fitness:0.82 ; self_correlation:0.5868 ; prodCorrelation:0.5868 ,pyramids:['AMR/D1/RISK', 'AMR/D1/MODEL'] ;
region: AMR ;sharpe:1.32 ; fitness:1.22 ; self_correlation:0.0 ; prodCorrelation:0.2162 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.07 ; fitness:0.88 ; self_correlation:0.0 ; prodCorrelation:0.4421 ,pyramids:['AMR/D1/RISK'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 6.94 ;
fitness: 9.17 ;
self: 0.2743 ;
prodCorrelation: 0.2743 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #171: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-10 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: GLB ;sharpe:2.07 ; fitness:1.58 ; self_correlation:0.9199 ; prodCorrelation:0.9199 ,pyramids:['GLB/D1/ANALYST'] ;
region: GLB ;sharpe:1.19 ; fitness:0.92 ; self_correlation:0.2246 ; prodCorrelation:0.5757 ,pyramids:['GLB/D1/ANALYST'] ;
region: EUR ;sharpe:1.56 ; fitness:1.5 ; self_correlation:0.2003 ; prodCorrelation:0.568 ,pyramids:['EUR/D1/IMBALANCE'] ;
region: GLB ;sharpe:1.08 ; fitness:0.82 ; self_correlation:0.301 ; prodCorrelation:0.6056 ,pyramids:['GLB/D1/PV', 'GLB/D1/SHORTINTEREST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.45 ;
fitness: 5.88 ;
self: 0.643 ;
prodCorrelation: 0.643 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #172: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-11 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: AMR ;sharpe:1.1 ; fitness:0.7 ; self_correlation:0.0038 ; prodCorrelation:0.2415 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.43 ; fitness:1.51 ; self_correlation:-0.0404 ; prodCorrelation:0.1938 ,pyramids:['AMR/D1/ANALYST'] ;
region: AMR ;sharpe:1.13 ; fitness:0.87 ; self_correlation:0.0358 ; prodCorrelation:0.2655 ,pyramids:['AMR/D1/FUNDAMENTAL'] ;
region: AMR ;sharpe:1.05 ; fitness:0.67 ; self_correlation:0.0092 ; prodCorrelation:0.1983 ,pyramids:['AMR/D1/RISK', 'AMR/D1/IMBALANCE'] ;

Superalpha:
region: ASI  ;
is 指标:
sharpe: 5.7 ;
fitness: 6.62 ;
self: 0.2886 ;
prodCorrelation: 0.3624 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #173: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-12 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: EUR ;sharpe:1.11 ; fitness:0.57 ; self_correlation:0.3563 ; prodCorrelation:0.6682 ,pyramids:['EUR/D1/EARNINGS'] ;
region: GLB ;sharpe:1.29 ; fitness:0.82 ; self_correlation:0.386 ; prodCorrelation:0.9259 ,pyramids:['GLB/D1/NEWS'] ;
region: GLB ;sharpe:1.24 ; fitness:0.7 ; self_correlation:0.286 ; prodCorrelation:0.8075 ,pyramids:['GLB/D1/NEWS'] ;
region: ASI ;sharpe:1.5 ; fitness:1.2 ; self_correlation:0.3637 ; prodCorrelation:0.5623 ,pyramids:['ASI/D1/PV', 'ASI/D1/NEWS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.09 ;
fitness: 5.69 ;
self: 0.6175 ;
prodCorrelation: 0.6174 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #174: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-13 
今天提交情况：
RA: 1个 ;
region: EUR ;sharpe:1.58 ; fitness:1.12 ; self_correlation:0.2025 ; prodCorrelation:0.4315 ,pyramids:['EUR/D1/INSTITUTIONS'] ;
PPA: 3个 ;
region: GLB ;sharpe:2.07 ; fitness:1.8 ; self_correlation:0.2274 ; prodCorrelation:0.7968 ,pyramids:['GLB/D1/SOCIALMEDIA', 'GLB/D1/ANALYST'] ;
region: AMR ;sharpe:1.15 ; fitness:0.74 ; self_correlation:0.1635 ; prodCorrelation:0.5573 ,pyramids:['AMR/D1/NEWS'] ;
region: AMR ;sharpe:1.5 ; fitness:1.2 ; self_correlation:0.4194 ; prodCorrelation:0.8324 ,pyramids:['AMR/D1/FUNDAMENTAL'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 5.9 ;
fitness: 9.56 ;
self: 0.2143 ;
prodCorrelation: 0.4791 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #175: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-14 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: AMR ;sharpe:1.23 ; fitness:0.83 ; self_correlation:0.0302 ; prodCorrelation:0.1442 ,pyramids:['AMR/D1/SENTIMENT'] ;
region: AMR ;sharpe:1.26 ; fitness:1.08 ; self_correlation:0.0468 ; prodCorrelation:0.6995 ,pyramids:['AMR/D1/IMBALANCE', 'AMR/D1/OTHER'] ;
region: AMR ;sharpe:1.32 ; fitness:0.94 ; self_correlation:0.0045 ; prodCorrelation:0.3948 ,pyramids:['AMR/D1/FUNDAMENTAL'] ;
region: AMR ;sharpe:1.06 ; fitness:0.73 ; self_correlation:-0.0701 ; prodCorrelation:0.2069 ,pyramids:['AMR/D1/NEWS'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.44 ;
fitness: 5.93 ;
self: 0.6636 ;
prodCorrelation: 0.6636 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #176: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-15 
今天提交情况：
RA: 3个 ;
region: AMR ;sharpe:1.74 ; fitness:1.38 ; self_correlation:0.0102 ; prodCorrelation:0.6355 ,pyramids:['AMR/D1/OTHER'] ;
region: GLB ;sharpe:2.83 ; fitness:2.11 ; self_correlation:0.3344 ; prodCorrelation:0.6655 ,pyramids:['GLB/D1/PV', 'GLB/D1/ANALYST'] ;
region: AMR ;sharpe:1.78 ; fitness:1.85 ; self_correlation:0.0232 ; prodCorrelation:0.4437 ,pyramids:['AMR/D1/IMBALANCE', 'AMR/D1/SENTIMENT'] ;
PPA: 1个 ;
region: GLB ;sharpe:1.09 ; fitness:0.7 ; self_correlation:0.2757 ; prodCorrelation:0.7277 ,pyramids:['GLB/D1/SOCIALMEDIA'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 6.34 ;
fitness: 9.67 ;
self: 0.4576 ;
prodCorrelation: 0.4576 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #177: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-16 
今天提交情况：
RA: 2个 ;
region: AMR ;sharpe:1.83 ; fitness:1.47 ; self_correlation:0.5044 ; prodCorrelation:0.6886 ,pyramids:[ 'AMR/D1/MODEL'] ;
region: EUR ;sharpe:2.08 ; fitness:1.17 ; self_correlation:0.304 ; prodCorrelation:0.5292 ,pyramids:['EUR/D1/INSIDERS', 'EUR/D1/ANALYST'] ;
PPA: 2个 ;
region: AMR ;sharpe:1.74 ; fitness:1.6 ; self_correlation:0.0519 ; prodCorrelation:0.8789 ,pyramids:['AMR/D1/OTHER'] ;
region: EUR ;sharpe:1.49 ; fitness:0.75 ; self_correlation:0.2335 ; prodCorrelation:0.6159 ,pyramids:['EUR/D1/INSIDERS', 'EUR/D1/ANALYST'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 4.86 ;
fitness: 5.13 ;
self: 0.6903 ;
prodCorrelation: 0.6903 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #178: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-17 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: AMR ;sharpe:1.62 ; fitness:1.54 ; self_correlation:0.0987 ; prodCorrelation:0.1868 ,pyramids:['AMR/D1/SENTIMENT'] ;
region: AMR ;sharpe:1.04 ; fitness:0.79 ; self_correlation:0.1367 ; prodCorrelation:0.2847 ,pyramids:[ 'AMR/D1/OPTION'] ;
region: EUR ;sharpe:1.85 ; fitness:1.72 ; self_correlation:0.3612 ; prodCorrelation:0.4745 ,pyramids:['EUR/D1/IMBALANCE'] ;
region: AMR ;sharpe:1.37 ; fitness:1.6 ; self_correlation:0.0364 ; prodCorrelation:0.1678 ,pyramids:['AMR/D1/SOCIALMEDIA'] ;

Superalpha:
region: AMR  ;
is 指标:
sharpe: 5.68 ;
fitness: 8.39 ;
self: 0.4385 ;
prodCorrelation: 0.4714 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #179: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

-----------------------------------橘子的量化日记 -------------------------------------
 2025-09-18 
今天提交情况：
RA: 0个 ;
PPA: 4个 ;
region: AMR ;sharpe:1.34 ; fitness:1.07 ; self_correlation:0.1898 ; prodCorrelation:0.5914 ,pyramids:['AMR/D1/NEWS'] ;
region: AMR ;sharpe:1.27 ; fitness:1.18 ; self_correlation:0.1775 ; prodCorrelation:0.646 ,pyramids:['AMR/D1/MODEL'] ;
region: AMR ;sharpe:1.17 ; fitness:0.76 ; self_correlation:0.0929 ; prodCorrelation:0.1618 ,pyramids:['AMR/D1/EARNINGS'] ;
region: AMR ;sharpe:1.31 ; fitness:1.18 ; self_correlation:0.1304 ; prodCorrelation:0.2588 ,pyramids:['AMR/D1/INSIDERS', 'AMR/D1/OPTION'] ;

Superalpha:
region: EUR  ;
is 指标:
sharpe: 5.04 ;
fitness: 5.12 ;
self: 0.5231 ;
prodCorrelation: 0.6613 ;
----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #180: 关于《【顾问好文，限时置顶】关于新Consultant提升每日paid的一些建议经验分享》的评论回复
- **帖子链接**: [Commented] 【顾问好文限时置顶】关于新Consultant提升每日paid的一些建议经验分享.md
- **评论时间**: 1年前

我想问下，我刚成为consulant，我有一些相关性6.x的 可提交的alpha，fitness 大约2，margin 大约15% ，目前我暂时没有其他模版的alpha可提交，我要可以提交这些相关性6.x的alpha 还是暂停提交呢?

---

### 探讨 #181: 关于《【顾问好文，限时置顶】关于新Consultant提升每日paid的一些建议经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【顾问好文限时置顶】关于新Consultant提升每日paid的一些建议经验分享_27599176068503.md
- **评论时间**: 1年前

我想问下，我刚成为consulant，我有一些相关性6.x的 可提交的alpha，fitness 大约2，margin 大约15% ，目前我暂时没有其他模版的alpha可提交，我要可以提交这些相关性6.x的alpha 还是暂停提交呢?

---

### 探讨 #182: 关于《一键检验alpha稳定性代码优化》的评论回复
- **帖子链接**: [Commented] 一键检验alpha稳定性代码优化.md
- **评论时间**: 1 year ago

用了一段时间了，非常有用！我根据自己的需要，修改为Multi simulate了，用了这个测试后，再也不用对自己提交的alpha质量如何感到困惑了。感谢大佬的分享，祝大佬月月vf1.00，季季GM。

-----------------------------------------------------------------------------------------------------------

---

### 探讨 #183: 关于《一键检验alpha稳定性代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 一键检验alpha稳定性代码优化_32008506789655.md
- **评论时间**: 1年前

用了一段时间了，非常有用！我根据自己的需要，修改为Multi simulate了，用了这个测试后，再也不用对自己提交的alpha质量如何感到困惑了。感谢大佬的分享，祝大佬月月vf1.00，季季GM。

-----------------------------------------------------------------------------------------------------------

---

### 探讨 #184: 关于《为什么implied_volatility_call_120/parkinson_volatility_120调整后就能过？》的评论回复
- **帖子链接**: [Commented] 为什么implied_volatility_call_120parkinson_volatility_120调整后就能过.md
- **评论时间**: 1年前

SC38173

这个应该是用户阶段才能通过的吧，我试了下，用户阶段是可以的


> [!NOTE] [图片 OCR 识别内容]
> C|731
> (
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 7 PASS
> REGION
> UNIVERSE
> DELAY
> Sharpe of 1.54is above cutoff of 1.25.
> Fitness of 1.06 is above cutoff of1.
> USA
> TOP1000
> Turnoverof 25.079 is above cUtoff of 1% _
> Turnover of 25.0796 is below cutoff of 70%.
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 1.42 is above cUtoff Of 0.82.
> Subindustry
> 0.08
> Competition Challenge matches。
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> FAIL
> On
> Verify
> On
> YEARS
> MONTHS
> Self-correlation 0.8604 is above cUtoff of 0.7
> Sharpe not better by 10
> Saveas Default
> Apply
> Performance Comparison
> trade_When (Volume
> advzo,
> implied_Volatility_call_128/
> parkinson_volatility_120=
> -1)
> 3
> Chart
> Pnl
> Clone this Alphain a newtab
> and


---

### 探讨 #185: 关于《为什么implied_volatility_call_120/parkinson_volatility_120调整后就能过？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 为什么implied_volatility_call_120parkinson_volatility_120调整后就能过_29140117326103.md
- **评论时间**: 1年前

SC38173

这个应该是用户阶段才能通过的吧，我试了下，用户阶段是可以的


> [!NOTE] [图片 OCR 识别内容]
> C|731
> (
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 7 PASS
> REGION
> UNIVERSE
> DELAY
> Sharpe of 1.54is above cutoff of 1.25.
> Fitness of 1.06 is above cutoff of1.
> USA
> TOP1000
> Turnoverof 25.079 is above cUtoff of 1% _
> Turnover of 25.0796 is below cutoff of 70%.
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 1.42 is above cUtoff Of 0.82.
> Subindustry
> 0.08
> Competition Challenge matches。
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> FAIL
> On
> Verify
> On
> YEARS
> MONTHS
> Self-correlation 0.8604 is above cUtoff of 0.7
> Sharpe not better by 10
> Saveas Default
> Apply
> Performance Comparison
> trade_When (Volume
> advzo,
> implied_Volatility_call_128/
> parkinson_volatility_120=
> -1)
> 3
> Chart
> Pnl
> Clone this Alphain a newtab
> and


---

### 探讨 #186: 关于《为什么有些人有那么多alpha可以挖呢？ 我ppa都 1 的相关性了》的评论回复
- **帖子链接**: [Commented] 为什么有些人有那么多alpha可以挖呢 我ppa都 1 的相关性了.md
- **评论时间**: 1年前

==============================================================

我已经2个月没有明显产出了，焦虑，下个季度咋提交啊。好想做梦能梦到个模版啊。

==============================================================

---

### 探讨 #187: 关于《为什么有些人有那么多alpha可以挖呢？ 我ppa都 1 的相关性了》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 为什么有些人有那么多alpha可以挖呢 我ppa都 1 的相关性了_33039213327255.md
- **评论时间**: 1年前

==============================================================

我已经2个月没有明显产出了，焦虑，下个季度咋提交啊。好想做梦能梦到个模版啊。

==============================================================

---

### 探讨 #188: 关于《关于缺失年份数据的整理（小于5年）【USA】【TOP3000】【anl】》的评论回复
- **帖子链接**: [Commented] 关于缺失年份数据的整理小于5年【USA】【TOP3000】【anl】.md
- **评论时间**: 10个月前

哇塞，真的很需要，感谢虎哥分享！

---

### 探讨 #189: 关于《关于缺失年份数据的整理（小于5年）【USA】【TOP3000】【anl】》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 关于缺失年份数据的整理小于5年【USA】【TOP3000】【anl】_33785792432919.md
- **评论时间**: 10个月前

哇塞，真的很需要，感谢虎哥分享！

---

### 探讨 #190: 关于《如何利用tvr操作符与alpha起舞论坛精选》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何利用tvr操作符与alpha起舞论坛精选_34562640928023.md
- **评论时间**: 9个月前

好强大，学习了，刷新我对降低turnover的操作符的认知了

---

### 探讨 #191: 关于《如何自动化高效率筛选出值得check submission的alpha》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiXeSrOQxo6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAd9odHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjg4Nzg1MjQwMjExNDMtJUU1JUE2JTgyJUU0JUJEJTk1JUU4JTg3JUFBJUU1JThBJUE4JUU1JThDJTk2JUU5JUFCJTk4JUU2JTk1JTg4JUU3JThFJTg3JUU3JUFEJTlCJUU5JTgwJTg5JUU1JTg3JUJBJUU1JTgwJUJDJUU1JUJFJTk3Y2hlY2stc3VibWlzc2lvbiVFNyU5QSU4NGFscGhhBjsIVDoOc2VhcmNoX2lkSSIpOTI2MmFlNDktY2RjMi00ZjMxLWE1ZTMtMGI0OTUzYzM4YTNlBjsIRjoJcmFua2kMOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMU1o4MzA5NgY7CFQ6EnJlc3VsdHNfY291bnRpHA%3D%3D--9a7afdd5d663314c98338bf9bb34957db746596b
- **评论时间**: 1年前

RX97746 : 应该是回测结束时，获取回测alpha id后，注入name

---

### 探讨 #192: 关于《如何自动化高效率筛选出值得check submission的alpha》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何自动化高效率筛选出值得check submission的alpha_28878524021143.md
- **评论时间**: 1年前

RX97746 : 应该是回测结束时，获取回测alpha id后，注入name

---

### 探讨 #193: 关于《src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    ...    获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...])》的评论回复
- **帖子链接**: [Commented] 构建 724 小时不间断 Alpha 回测系统基于 Celery 和动态任务队列的架构分享代码优化.md
- **评论时间**: 1年前

===================================================================================

感谢分享，我最近也想搞个类似的管理alpha，自动回测的系统。现有的代码，总是需要人为介入，切换模版，检查回测情况，挺麻烦的。

请问大佬，你搭建这样一套系统，花了多久时间啊？容易搭建不？

===================================================================================

---

### 探讨 #194: 关于《src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    ...    获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...])》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 构建 724 小时不间断 Alpha 回测系统基于 Celery 和动态任务队列的架构分享代码优化_33040125516311.md
- **评论时间**: 1年前

===================================================================================

感谢分享，我最近也想搞个类似的管理alpha，自动回测的系统。现有的代码，总是需要人为介入，切换模版，检查回测情况，挺麻烦的。

请问大佬，你搭建这样一套系统，花了多久时间啊？容易搭建不？

===================================================================================

---

### 探讨 #195: 关于《构建自已的Template同时，并行回测Alpha Machine的一二三阶程序代码优化》的评论回复
- **帖子链接**: [Commented] 构建自已的Template同时并行回测Alpha Machine的一二三阶程序代码优化.md
- **评论时间**: 1年前

新思路，在alpha 表达式层面对alpha进行区别，挺好的

---

### 探讨 #196: 关于《构建自已的Template同时，并行回测Alpha Machine的一二三阶程序代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 构建自已的Template同时并行回测Alpha Machine的一二三阶程序代码优化_30609613199895.md
- **评论时间**: 1年前

新思路，在alpha 表达式层面对alpha进行区别，挺好的

---

### 探讨 #197: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 近8000刀Master赚到了GM的Quarterly Payment论坛精选.md
- **评论时间**: 16天前

感谢分享！这个收入水平对 Master 档位很有参考价值。

有两个点想请教：

1. Value Factor 从 0.96 → 0.97 → 0.99 的提升过程中，除了你提到的筛选标准，是否有刻意控制提交数量或调整提交节奏？

2. Q2 Weight Factor 回落后，你是否尝试过主动"降档"（减少提交、调整策略）来避免进一步下滑，还是继续按原有节奏推进？

---

### 探讨 #198: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 近8000刀Master赚到了GM的Quarterly Payment论坛精选_41000341056791.md
- **评论时间**: 16天前

感谢分享！这个收入水平对 Master 档位很有参考价值。

有两个点想请教：

1. Value Factor 从 0.96 → 0.97 → 0.99 的提升过程中，除了你提到的筛选标准，是否有刻意控制提交数量或调整提交节奏？

2. Q2 Weight Factor 回落后，你是否尝试过主动"降档"（减少提交、调整策略）来避免进一步下滑，还是继续按原有节奏推进？

---
