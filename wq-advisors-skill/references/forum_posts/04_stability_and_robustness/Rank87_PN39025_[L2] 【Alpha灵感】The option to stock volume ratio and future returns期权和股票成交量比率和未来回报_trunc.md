# 【Alpha灵感】The option to stock volume ratio and future returns期权和股票成交量比率和未来回报率

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】The option to stock volume ratio and future returns期权和股票成交量比率和未来回报率_19137764807191.md
- **作者**: YT14523
- **发布时间/热度**: 2 years ago, 得票: 13

## 帖子正文

论文标题：The option to stock volume ratio and future returns

期权和股票成交量比率和未来回报率

作者：Travis L. Johnson, Eric C. So

概述：这篇论文讲了股票和期权的交易量对未来回报率的影响。当期权对股票交易量的比率（O/S）低时，公司的表现优于（O/S）低的时候。并且期权杠杆的加入会提供O/S强弱的信号。

Idea:

1: 初步的想法是直接使用论文中提到的O/S比率表达Alpha，我们选择期权的成交量和股票的成交量的比率。相关数据：opt4_secpr_volume; volume 
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Stage
> I5S
> 0o
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.64
> 38.3400.33
> 9.91%38.889
> 5.179600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2011
> 3.41
> 56.289
> 2.46
> 29.329
> 2.5996
> 10.429600
> 2149
> 594
> 2012
> 1.18
> 50.489
> 0.51
> 9.499
> 4.819
> 3.769600
> 2360
> 320
> 2013
> 1.24
> 50.509
> 0.52
> 8.799
> 4.689
> 3.489600
> 2385
> 322
> 2014
> 3.04
> 48.969
> 2.13
> 24.089
> 2.389
> 9.839600
> 2390
> 263
> 2015
> 2.02
> 48.869
> 1.15
> 15.809
> 4.939
> 6.479600
> 2409
> 267
> 2016
> 0.90
> 49.659
> 0.42
> 10.619
> 11.639
> 4.289600
> 2399
> 241
> 2017
> 2.36
> 47.149
> 1.39
> 16.359
> 3.359
> 6.949600
> 2398
> 254
> 2018
> 0.90
> 26.649
> 0.41
> 5.549
> 5.709
> 4.169600
> 1218
> 170
> 2019
> -0.38
> 4.349
> -0.10
> -0.889
> 3.1996
> 4.089600
> 78
> 23
> 2020
> 0.55
> 4.969
> 0.51
> 10.789
> 8.1296
> 43.489600
> 2021
> -1.91
> 7.749
> -7.92
> -215.029
> 37.839
> -555.449600
> 15
> Long
  
> [!NOTE] [图片 OCR 识别内容]
> 1OM
> 02/23/2016
> 8,00OK
> ISPnl: 8,572.04K
> 6,0OOK
> 4,0OOK
> 2,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021


结果在2017年前较好，2019-2021年之间表现很差，猜想是受到了新冠疫情的影响。

2：我们进一步加入期权杠杆，用期权价格和隐含波动率来表示，期权价格在数据搜索中没有找到合适的数据字段，因此我们决定使用隐含波动率来尝试implement alpha。相关数据：implied_volatility_call_1080; implied_volatility_put_1080

这里使用看涨和看跌期权的波动利差来表示。波动利差可以表现对该期权的预期。高利差表明看好，存在交易的可能。 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 17.5M
> 15M
> 12.5M
> 10M
> 7,50OK
> 5,00OK
> 02/24/2012
> 2,500K
> ISPn: 2,812.37k
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
  
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS
> Summary
> Stage
> I5
> Oo
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.16
> 31.609 1.71
> 19.90010.47012.599600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 3.14
> 33.499
> 3.34
> 37.949
> 9.959
> 22.669600
> 884
> 547
> 2012
> 2.75
> 31.269
> 2.28
> 21.509
> 4.649
> 13.769600
> 895
> 549
> 2013
> 1.46
> 27.539
> 0.84
> 9.059
> 7.0296
> 6.579600
> 1087
> 618
> 2014
> 4.38
> 34.769
> 4.32
> 33.749
> 4.3796
> 19.419600
> 1135
> 734
> 2015
> 3.01
> 35.21%
> 2.40
> 22.389
> 3.089
> 12.719600
> 1099
> 778
> 2016
> 0.42
> 35.109
> 0.15
> 4.219
> 9.399
> 2.409600
> 1128
> 744
> 2017
> -0.04
> 27.229
> -0.00
> -0.289
> 6.359
> -0.219600
> 1175
> 695
> 2018
> 2.12
> 25.599
> 1.97
> 22.189
> 5.719
> 17.339600
> 1231
> 738
> 2019
> 4.35
> 25.649
> 4.62
> 28.949
> 1.819
> 22.579600
> 1245
> 699
> 2020
> 1.87
> 42.079
> 1.48
> 26.249
> 10.479
> 12.489600
> 1085
> 841
> 2021
> 1.55
> 27.26%
> 1.17
> 15.619
> 3.519
> 11.459600
> 1174
> 970
 在O/S的基础上加入隐含波动率，并改进settings, 最后结果有明显改善。但在iliquid 股票池中的测试表现不太好，还需改进。

3：测试中显示：Most illiquid 50% instruments after cost Sharpe of 0.81 is below cutoff of 1 (1.91 original universe after cost Sharpe)有此问题，或许可以根据iliquid股票池进行改进。

---

## 讨论与评论 (6)

### 评论 #1 (作者: YT14523, 时间: 2 years ago)

进一步优化：sharpe ratio有明显提高 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> T5N
> 7SNNN
> SOOOK
> SOOK
> O8RSROT
> Pnl: 1,019.74
> 2012
> 2013
> 7014
> 7015
> ZOI6
> 3017
> 2016
> 7019
> 2020
> 7021
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Stage
> ABBreBate Data
> SharOe
> TUrmoyer
> HMeS 5
> RelUrns
> Oraoy
> WarRln
> 2.5330.2291.9217.4497.01%
> 11.549600


---

### 评论 #2 (作者: KJ42842, 时间: 2 years ago)

“当期权对股票交易量的比率（O/S）低时，公司的表现优于（O/S）低的时候。”

你好，感谢分享，想问下后面一个（O/S)是否应为（S/O)?

---

### 评论 #3 (作者: YT14523, 时间: 2 years ago)

抱歉，概述部分表达有误。应改为：“公司表现优于O/S 高的时候”。或是S/O低的时候。感谢指正

---

### 评论 #4 (作者: BX78946, 时间: 2 years ago)

您好，如果在回测里面测试一下，会发现opt4_secpr_volume和volume的比值非常接近1。所以O/S比率与波动利差的积

```
(opt4_secpr_volume/volume) * (implied_volatility_call_1080 - implied_volatility_put_1080)
```

和单独的波动利差

```
implied_volatility_call_1080 - implied_volatility_put_1080
```

结果几乎一模一样。请问您有没有考虑过不是用opt4_secpr_volume和volume的比值，而是用其他的方式来表达他俩之间的信息？

---

### 评论 #5 (作者: YT14523, 时间: 2 years ago)

opt4_secpr_volume和volume是两个比较符合论文的数据段，可能有更合理的数据，论文主要说明的是O/S，所以还没有使用别的方式表示这个信号；

也可能比值接近1是因为NaN值？因为后续的优化对这个比率加上了group_mean，对波动利差加上了group_extra并打开NAN HANDLING处理NaN值，之后表现会更好 
> [!NOTE] [图片 OCR 识别内容]
> 1
> group_extra(implied_volatility_call_Iogo-implied_volatility_put_1080,0.6,
> 15M
> industry
> Eroup_
> mean ( (opt4_secpr_volume
> volume),0.5,industry
> 12.5M
> 1OM
> 7,50OK
> 5,0OOK
> 2,5OOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 叫 IS Summary
> Period
> IS
> 05
> 4i
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Clone this Alphaina newtab
> 2.68
> 18.2192.71
> 18.5998.809
> 20.429600
> Example
> Simwtate
> Visualization
> Add Alphato a List
> Check Submission
> Submit Alpha


---

### 评论 #6 (作者: BX78946, 时间: 2 years ago)

好的，谢谢您的分享

---

