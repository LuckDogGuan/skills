# 多图解析USA最新3x High Turnover Theme国区提交现况

- **链接**: https://support.worldquantbrain.com多图解析USA最新3x High Turnover Theme国区提交现况_39822852669079.md
- **作者**: 顾问 RM49262 (Rank 30)
- **发布时间/热度**: 2个月前, 得票: 53

## 帖子正文

如果你还不知道目前USA地区3x theme的标准是什么，这里就先带你回顾一下：

**基础标准（必须符合）：**

1. 换手率 > 20%
2. High Turnover returns ratio > 0.75 OR Pnl realization < 20 (这两个都是针对3x theme的新检测，其中前者多重回测就能看见是否符合，后者需要单独回测才能看见结果)

此外，还有四个 **子主题** ，每两周轮换一次(每个人顺序不同，具体参考小铃铛中通知的顺序)，在 **符合基础标准** 的前提下，需要在对应的时间内 **符合下述一个子主题** 的标准即可：

1. RAM中性化高换手(Orthogonal HTVR Theme)：使用RAM作为中性化即可
2. 可投资性高换手(Investable HTVR Theme)：(Max Trade Sharpe > 2.0 且 Max Trade turnover > 20%)  或者  (Max Position Sharpe > 2.0 且 Max Position turnover > 20%)
3. 费后sharpe高换手(After Cost HTVR Theme) ：After cost Sharpe > 1.0 (新检测会自动计算)
4. 高流动性高换手(Liquid HTVR Theme) ：必须通过 Liquid High Turnover tests:
   (TOP200 Sharpe > 1) 以及 (TOP500 and TOP200 Sharpe ratio > 0.7)

目前这个高换手主题已经进入了第三周，我在SA中进行了以下筛选

```
(in(classifications,"HIGH_TURNOVER:AFTER_COST") ||in(classifications,"HIGH_TURNOVER:INVESTABLE") ||in(classifications,"HIGH_TURNOVER:ORTHOGONAL") ||in(classifications,"HIGH_TURNOVER:LIQUID") )&& in(classifications,"REGULAR") 
```

对目前 **国区已经提交的Theme RA** 进行了简单的分析，这里分享给大家。

首先是难度，根据提交情况来看，截止0417，国区 D1一共提交了96个theme RA，其中：

1. Liquid High Turnover (14)
2. Investable High Turnover (22)
3. Orthogonal High Turnover (40)
4. After Cost High Turnover (65)

> 注：同一个RA可能同时符合多个theme

而在D0，theme RA的数量则更少，只有8个，其中：

1. Liquid High Turnover (3)
2. After Cost High Turnover (6)
3. Investable High Turnover (7)

上述提交数量大致反映了各个子主题的难度。因此，当轮到较难的主题时，可以适当考虑跳过，毕竟难度还是有的。

而在使用的数据大类方面，D1 theme RA的主要构成是：

Price Volume (38)
Fundamental (25)
Analyst (17)
Risk (13)
Model (11)
Social Media (6)
Sentiment (5)
Earnings (4)
Macro (4)
Option (4)
Other (4)
Imbalance (2)
Insiders (2)
Institutions (2)
Short Interest (2)
News (1)

> 注：同一个RA可能同时属于多个category/dataset

数据集方面，D1 theme RA使用数量排名靠前的主要是以下数据集：

pv1 (33)
analyst69 (11)
fundamental6 (11)
socialmedia12 (6)
fundamental17 (5)
analyst10 (4)
model77 (4)
risk70 (4)
analyst16 (3)
analyst4 (3)
earnings27 (3)
other551 (3)
analyst15 (2)
analyst82 (2)
analyst9 (2)
fundamental23 (2)
fundamental94 (2)
imbalance5 (2)
insiders3 (2)
model109 (2)
model165 (2)
model230 (2)
option23 (2)
pv103 (2)
pv47 (2)
pv87 (2)
risk60 (2)
risk71 (2)
risk72 (2)
sentiment26 (2)
sentiment27 (2)
short_interest_pred (2)

...

针对那些使用较多的数据集，大家可以多探索探索。至于其余数据集，基本是大家八仙过海，各显神通。

这些D1 theme RA的is 数据分布如下图：


> [!NOTE] [图片 OCR 识别内容]
> Universe
> Neutralization
> Value
> Count
> Value
> Count
> TOP3000
> 71
> 73.96%
> REVERSION_AND_MOMENTUM
> 40
> 41.67%
> ILLIQUID_MINVOLIM
> 20
> 20.83%
> STATISTICAL
> 26
> 27.08%
> TOPIOOO
> 5.21%
> SUBINDUSTRY
> 12
> 12.50%
> INDUSTRY
> 5
> 5.21%
> CROWDING
> 4.17%
> SLOW
> 3
> 3.12%
> FAST
> 3
> 3.12%
> MARKET
> 2
> 2.08%
> SLOW_AND_FAST
> 1.06%
  
> [!NOTE] [图片 OCR 识别内容]
> is.sharpe
> 96/96
> is.fitness
> 96/96
> istupnover
> 96/96
> 12
> 25
> 20
> 10
> 20
> 15
> 15
> 10
> 10
> 1.65
> 1.93
> 2.20
> 2.76
> 1.03
> 1.28
> 1.54
> 1.79
> 2.04
> 21.55
> 31.43
> 41.30
> 51.17
> 61.05
> MEAN
> MEDIAN
> STD
> MIN
> MEAN
> MEDIAN
> ST0
> MIN
> MEAN
> MEDIAN
> STD
> MIN
> 2.194
> 2.195
> 0.360
> 1.580
> 1.261
> 1.180
> 日.263
> 1.000
> 33.892
> 29.430
> 12.994
> 20.310
> P25
> P75
> MAX
> COUNT
> P25
> P75
> MAX
> COUNT
> P25
> P75
> MAX
> COUNT
> 1.927
> 2.390
> 3.710
> 96
> 1.070
> 1.373
> 2.330
> 96
> 23.975
> 40.380
> 69.960
> 96
> is.drawdown
> 96/96
> is.returns
> %)
> 96/96
> is.margin (bs)
> 96/96
> 25
> 20
> 20
> 20
> 15
> 15
> 15
> 10
> 10
> 10
> 2.28
> 6.71
> 11.14
> 15.57
> 20.00
> 11.68
> 17.48
> 23.29
> 29.10
> 40
> 6.96
> 10.53
> 14.09
> 17.66
> MEAN
> MEDIAN
> STD
> MIN
> MEAN
> MEDIAN
> ST0
> MIN
> MEAN
> MEDIAN
> STD
> MIN
> 800
> 5.480
> 5.036
> 1.160
> 11.526
> 9.725
> 074
> 4.890
> 7.214
> 385
> 3.988
> 2.290
> P25
> P75
> MAX
> COUNT
> P25
> P75
> MAX
> COUNT
> P25
> P75
> MAX
> COUNT
> 3.335
> 8.293
> 27.680
> 96
> 7.405
> 14.543
> 4.760
> 96
> 5.180
> 7.478
> 31.720
> 96
  
> [!NOTE] [图片 OCR 识别内容]
> regular. operatorCount
> 96/96
> 30
> 25
> 20
> 15
> 10
> 2.96
> 1.07
> 19.18
> 27.29
> MEAN
> MEDIAN
> STD
> MIN
> 11.042
> 8.000
> 9.158
> 1.000
> P25
> P75
> MAX
> COUNT
> 6.000
> 13.000
> 52.000
> 96



> [!NOTE] [图片 OCR 识别内容]
> 5.6
> fundamental
> REVERSION_AND_HOMENTUH
> 19,85020+6681
> 041.67)
> analyst
> 15+53013.8991
> Single Data Set:
> Yes
> 063
> 5o
> Fisk
> TOP3OOO
> (9.039)
> 71(73.968)
> STATISTICAL
> 02,09
> All
> Alphas (96)
> OFF
> (1008)
> IaCr0
> (86+468)
> [2]
> Regular Alpha: Yes
> 96(100%)
> model
> 6+58
> (6,868)
> sentiment
> SUBINDUSTRY
> 30
> 0421)
> [12
> insiders
> (2.003]
> ibalance
> T
> INDUSTRY
> 
> SOCialmedia
> Joao
> SLON
> 3.1221
> other
> Single
> Qata
> Set: Mo
> (2.68)
> (36.468)
> ILLIOUID_MINVOLII
> CROWOING
> Shortinterest
> (20,838)
> Dews
> (0.525)
> FAST
> aption
> 1.5
> 5U
> (13.549)
> MARKET
> earnings
> TOPI0g0
> 0851
> 003
> (5.279)
> SLON_AND_FAST
> Institutions
> (1.045)
> 0.755
> (8.78%)
 之前weijie老师也提到过，可以把个人换手率分成10组，来评估换手的提升是否稳定带来了return的提升，斜率高的话，最总体表现增益更好。这里我们借用类似的概念，来看一下国区theme RA的收益率随着换手提升的变化情况。


> [!NOTE] [图片 OCR 识别内容]
> Turnover Vs Returns
> 15 turnover deciles
> mean returns (linear regression]
> SLOPE [B]
> Returns by Turnover Decile (%)
> 0.175555
> 44.02%
> 40.00%
> 35.00%
> 0.8048
> 30
> 00%
> 00%
> 16.46%
> P_VALUE
> 20.00%
> 12.67%
> 35%
> <0.001
> 15.00%
> 11.87%
> 11.33%
> 10.59%
> 12.12%
> 8.97%
> 8.07%
> 8.76%
> 10.00%
> 『
> SAMPLES
> BINS
> 5.00%
> 96
> 10
> 00%
> 26%
> 0
> 02
> 03
> 04
> 05
> 06
> 07
> 08
> 09
> 010
> 越高,
> 20.76% (10)
> 22.13%(10]
> 24.06% (9)
> 26.208  (10)
> 27.898
> (9)
> 31.52% (11)
> 34.12%(8]
> 40
> 93%(10]
> 49.56% (9)
> 62.01% (10]
> turnover
> mean returns
> 越高 [slope=0.175555,统计显著
> [p<0.05]]
> Returns
> Vs Turnover With linear
> fit
> Deciles
> fit
> (B=0.1756)
> 17.00
> 16.00
> 15.00
> 8
> 14.00
> 13.00
> 
> 12.00
> `
> 11.00
> 10.00
> 00
> 8.00
> 20
> 00
> 25.00
> 30.00
> 35.00
> 40.00
> 45.00
> 50
> 00
> 55.00
> 60.00
> 65.00
> aV9
> turnover
> (%)


总的来说，可以看到线性趋势，但斜率不是很高。因此，吃theme 的base固然爽，但也不要忘记注意return/margin的情况。

**后面再贴一下d0 RA 的相关数据供大家参考**


> [!NOTE] [图片 OCR 识别内容]
> Universe
> Neutralization
> Value
> Count
> Value
> Count
> TOP3O00
> 87.50%
> STATISTICAL
> 62.50%
> ILLIQUID_MINVOLIM
> 12.50%
> FAST
> 25.00%
> NOME
> 12.50%
  
> [!NOTE] [图片 OCR 识别内容]
> is.sharpe
> 818
> is.fitness
> 8/8
> is.turnover
> 2.0
> 2.0
> 1.5
> 1.5
> 1.5
> 1.0
> 1.0
> 0.5
> 3.16
> 3.85
> .19
> 1.51
> 1.63
> 1.7
> 2.26
> 32.43
> 48.59
> 18.76
> 56.92
> MEAN
> MEDIAN
> ST0
> MIN
> MEAN
> MEDIAN
> STD
> MIN
> MEAN
> MEDIAN
> ST0
> MIN
> 3.719
> 860
> 日.542
> 2.730
> 1.719
> 1.670
> 0.220
> 1.
> 500
> 44
> 871
> 47.220
> 13.645
> 22.580
> P25
> P75
> NAX
> COUIIT
> P25
> P75
> HAX
> COUNT
> P25
> P75
> MAX
> COUNT
> 3.395
> 950
> 520
> 1.532
> 855
> 2.060
> 36.438
> 51.965
> 64
> 580
> is.drawdown
> 818
> is.returns (%)
> 818
> is.margin (bs)
> 2.0
> 3.0
> 2.0
> 2.5
> 1.5
> 1.5
> 2.0
> 1.0
> 1.5
> 1 .0
> 1.0
> 0.5
> 2.0
> .83
> O
> 10.15
> 13.8
> 10.03
> 18.98
> 11
> 3.98
> 6.17
> HEAN
> MEDIAN
> STD
> MIN
> MEAN
> MEDIAN
> STD
> MIN
> MEAN
> MEDIAN
> STD
> MIN
> 2.374
> 1.935
> 1.347
> 1.140
> 9.988
> 7.950
> 5.215
> 820
> 464
> 280
> 1.371
> 3.010
> P25
> P75
> HAX
> COUNIT
> P25
> P75
> IAX
> COUNT
> P25
> P75
> MAX
> COUNT
> 1.505
> 2.808
> 5.250
> 7.380
> 9.320
> 22.280
> 3.500
> 4.855
> 900
  
> [!NOTE] [图片 OCR 识别内容]
> pegular. operatorCount
> 8/8
> 1.5
> 1.0
> 0.5
> 17.91
> 24.61
> 31.31
> 38.0_
> 44.72
> MEAII
> MEDIAN
> STD
> MIN
> 28.500
> 23.500
> 13.049
> 17.000
> P25
> P75
> IAX
> COUNT
> 18.750
> 34.500
> 51.000
  
> [!NOTE] [图片 OCR 识别内容]
> model
> 3.5(43.754)
> STATISTICAL
> 462.5〉
> T0P3000
> (87.5)
> AZZ Alphas (8)
> Single Data Set: Mo
> OFF
> Regular Alpha:
> Yes
> (1008)
> (1005)
> 8(100%)
> (100%)
> 3.5
> (43.75)
> FAST
> (258)
> ILLIQUID_MINVOLIN
> NOM
> fundamental
> (12.55)
> (12.5)
> (12.5)
> Dv
  
> [!NOTE] [图片 OCR 识别内容]
> Turnover Vs Returns
> 1S turnover deciles
> mean returns (Iinear regresslon]
> SLOPE [B]
> Retupns by
> Turnover
> Decile
> 0.277117
> 24
> 06%
> 22.28
> 00%
> 0.5258
> 00%
> 11.90%
> P-VALUE
> 10.00%
> 0.042
> 8.46%
> 8.10%
> 80%
> 49%
> 82%
> 05%
> 00
> SAMPLES
> BINS
> 8 /8
> 008
> -1.788
> 02
> 03
> 08
> 010
> 越高;
> 22.58%
> (1)
> 32.05% (1)
> 37.90% (1)
> 44.63% (1)
> 49.81% (1)
> 50.22% (1)
> 57.20%
> (1)
> 58%
> (1)
> turnoVer
> Iean returns
> 越高 [slope=0.277117,统计显著
> [ps0.05]]
> Returns
> VS
> Turnover With linear fit (%)
> Deciles
> fit (8=0.2771]
> 25.00
> 20.00
> 8
> 15.00
> 
> 10.00
> 嚣
> 5.00
> 0.00
> 20.00
> 25.00
> 35.00
> 40.00
> 45.00
> 50.00
> 55.00
> 60.00
> 65.00
> avg turnover


---

## 讨论与评论 (5)

### 评论 #1 (作者: JR57542, 时间: 2个月前)

太可怕了这个主题，可以看得出比较高质量的数据集都是pv1
analyst69 
fundamental6 ，这几个。楼主做的可视化展示确实不错，能直观的看到总体情况

---

### 评论 #2 (作者: XC66172, 时间: 2个月前)

使用SA来倒推哪个数据集容易出theme ra. 学到了~~

==========================================

FIGHTING LABUBU!

==========================================

---

### 评论 #3 (作者: MY82844, 时间: 2个月前)

大佬做结合SA的功能做主题，太强了，思路打开

```
in(classifications,"HIGH_TURNOVER:AFTER_COST") ||in(classifications,"HIGH_TURNOVER:INVESTABLE") ||in(classifications,"HIGH_TURNOVER:ORTHOGONAL") ||in(classifications,"HIGH_TURNOVER:LIQUID")
```

==============================================================================

Reflection + Pain = Progress

==============================================================================

---

### 评论 #4 (作者: AK76468, 时间: 2个月前)

====================================================================================

这个筛选方式真是学到了，以前还在想Theme应该怎么去筛选，原来是在Classification里筛选。官方文档好像确实没有针对性的说明，在大佬这里学到了。

====================================================================================

---

### 评论 #5 (作者: MY82844, 时间: 1个月前)

在pv20, pv87跑出一些可以过test的，但是after cost sharpe很多是负数，怎么破?

==============================================================================

Reflection + Pain = Progress

==============================================================================

---

