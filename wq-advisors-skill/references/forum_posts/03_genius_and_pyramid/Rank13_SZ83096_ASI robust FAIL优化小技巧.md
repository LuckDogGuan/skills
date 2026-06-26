# ASI robust FAIL优化小技巧

- **链接**: ASI robust FAIL优化小技巧.md
- **作者**: 顾问 SZ83096 (Rank 13)
- **发布时间/热度**: 7个月前, 得票: 77

## 帖子正文

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

## 讨论与评论 (6)

### 评论 #1 (作者: LZ25854, 时间: 7个月前)

谢谢大佬的分享，对我这种刚入门的新手挺有启发。
以前我只知道 robust 很重要，但没真正理解。读完你的例子才感觉有些了解，原来 robust 是看你的信号在换一批股票之后还能不能维持住原来的表现。如果掉得很厉害，就说明原来的 alpha 可能有点“挑股票”，不够稳。

楼主把优化的过程写得挺清楚：先发现初版过不了 → 尝试常见的 power 调参 → 看字段范围 → 再试 tail、quantile 这种处理极端值的方法 → 最后把结构简化，结果就过了。对我这种小白来说最大的收获是：
 **不用一上来就想着高深操作，先把字段是否合理、极端值有没有影响、操作顺序是否多余这些简单的地方排查清楚，往往就能看到明显改善。**

看你最后的版本结构更简单但更稳，这点给了我新的方向：不用搞很复杂，有时候把信号弄干净就够了。

---

### 评论 #2 (作者: MY82844, 时间: 7个月前)

很有启发，power()那步让robust差值还变差了一点？感觉核心是tail()那步把9-10之间的值处理掉？

---

### 评论 #3 (作者: 顾问 YH25030 (Rank 31), 时间: 7个月前)

谢谢大佬的分享。对我来说，这篇帖子的one point就是group_mean(d,1,group)-d。准备马上尝试！

==================================================================================
Life is about waiting for the right moment to act.So, RELAX.You’re not LATE. You’re not EARLY.
You are very much ON TIME, and in your, TIME ZONE Destiny set up for you.
==================================================================================

---

### 评论 #4 (作者: 顾问 MS51256 (Rank 28), 时间: 6个月前)

**===============================顾问 MS51256 (Rank 28)的评论===============================**

**感谢橘子姐姐的分享，橘子姐姐对op的应用真的让我叹为观止！
好好研究op和字段含义才是做好研究的不二法门。

================================Do your best ================================**

---

### 评论 #5 (作者: CY96125, 时间: 6个月前)

又又又又看到橘子姐的干货文章，感谢分享，倾囊相授，向大佬看齐！

---

### 评论 #6 (作者: AL13375, 时间: 5个月前)

不愧是橘子姐！

橘子姐那句“凭借直觉”就成功搓出来了，不知道我什么时候也能有这种直觉，实在太强了！

又是柠檬精的一天。。。

---

