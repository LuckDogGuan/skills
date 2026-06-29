# IND感想Alpha Template

- **链接**: https://support.worldquantbrain.com[Commented] IND感想Alpha Template_36249870177687.md
- **作者**: ZX52486
- **发布时间/热度**: 7个月前, 得票: 37

## 帖子正文

1.通过线性回归拿到close与数据的残差，如果拟合得越好，则表明股价有可能在未来会下跌

data = ts_regression(ts_delta(close,1),ts_backfill(vec_avg(mdl138_qpdi3_sale_empl),66),200);

2.通过regression_proj剔除市值的影响，当市值相同时，看谁拟合更好，那么就做空，

re = data -regression_proj(data,rank(cap));

3.最后通过rank(-re)平滑权重，避免权重过于集中，当然也可以使用sigmoid(-re)

4可以延展到fnd和anl有实际意义的组合字段等

5：改进方向：能否在降低换手率的同时尽可能保持performance？

实战如下：


> [!NOTE] [图片 OCR 识别内容]
> Code
> o IS Summary
> Period
> IS
> Os
> '),280);
> pe
> data -regression_proj(data,rank
> cap
> sigmoid(-re)
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.07
> 35.82%
> 2.43
> 22.359
> 12.20%
> 12.489600
> Simulation Settings
> Instrument Type
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handl
> Year
> Sharpe
> TurOVer
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> Equity
> IND
> TOPSOO
> Fast Expression
> 20
> 0.01
> Subindustry
> On
> On
> Verify
> 2013
> 0.50
> 34.7896
> 0.18
> 4.5996
> 12.20%
> 2.649600
> 171
> 165
> 2014
> 1.37
> 34.1196
> 0.79
> 11.4696
> 8,4396
> 6.729600
> 191
> 184
> 2015
> 2.59
> 36.8696
> 1.81
> 18.0496
> 539
> 9960o
> 213
> 208
> 2016
> 3.26
> 35.8096
> 2.57
> 22.2696
> 3,4296
> 12.449600
> 212
> 206
> Clone Alpha 
> 2017
> 2.00
> 36.4496
> 1.17
> 12.5496
> 2.47%6
> 889600
> 212
> 203
> 2018
> 4.73
> 36.9296
> 4.51
> 33.6196
> 2.94%
> 18.219600
> 205
> 203
> N Chart
> Pnl
> 2019
> 3.49
> 36.1996
> 3.05
> 27.7396
> 6,1496
> 15.339600
> 210
> 206
> 2020
> 6.30
> 34.1396
> 7.04
> 42.6796
> 2.08%
> 25.019600
> 196
> 189
> 2021
> 3.58
> 35.6896
> 2.83
> 22.3496
> 2.90%
> 12.529600
> 185
> 181
> 2022
> 4.45
> 37.0596
> 3.99
> 29.7996
> 1.759
> 16.089600
> 188
> 186
> 2023
> 2.22
> 36.9996
> 1.03
> 7.8996
> 0.43%
> 4.279600
> 186
> 188
> TOM
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.96
> 13.04%
> 0.68
> 6.46%
> 27.14%
> 9.90900
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
> ACTV
> Created 11/11/2025 EST
> anonymous
> Add Alphato a List
> Code
> IS Summary
> Period
> I5S
> 05
> data
> ts
> _regression(ts_delta(close,1)_
> ts_delay (close,1),ts_backfill (dividend, 66 ),288
> Theme: IND Region Theme X2
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: INDIDIIPV X1.5
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handl
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.49
> 37.629
> 1.79
> 19.399
> 13.42%
> 10.319600
> Equity
> IND
> TOPSOO
> Fast Expression
> 25
> 0.03
> Subindustry
> On
> On
> Verify
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
> 1.85
> 41.8896
> 1.19
> 17.2496
> 6.95%
> 8.239600
> 118
> 117
> Clone Alpha
> 2014
> 2.67
> 38.1096
> 2.01
> 21.5096
> 4.99%6
> 11.289600
> 128
> 129
> 2015
> 1.74
> 38.5896
> 1.06
> 14.2496
> 13.42%6
> 7.389600
> 134
> 132
> 2016
> 1.87
> 37.5296
> 1.18
> 14.9696
> 5.91%
> 7.9
> 900
> 148
> 145
> Chart
> Pnl
> 2017
> 3.02
> 38.3396
> 2.01
> 17.039
> 2.80%
> 889600
> 140
> 140
> 2018
> 3.11
> 38.6996
> 2.50
> 25.069
> 74%6
> 12.969600
> 142
> 142
> 2019
> 3.03
> 39.0196
> 2.31
> 22.6296
> 6.2696
> 11.609600
> 154
> 154
> 15M
> 2020
> 3.36
> 36.2296
> 2.83
> 25.6496
> 3.2796
> 14.169600
> 151
> 152
> 2021
> 1.23
> 32.0396
> 65
> 8.8996
> 5.4796
> 5.5596o0
> 141
> 143
> 1OM
> 2022
> 3.44
> 35.9296
> 3.00
> 27.3296
> 2.94%
> 15.2
> 9oo
> 139
> 145
> 5,0OOK
> 2023
> 4.66
> 38.6696
> 3.01
> 16.1896
> 0.6296
> 8.379600
> 148
> 149
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
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
> 1.36
> 11.129
> 1.19
> 9.609
> 19.159
> 17.269600
> Decay



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 11/11/2025 EST
> anonymous
> Add Alphatoa List
> Code
> IS Summary
> Period
> I5S
> 05
> data
> ts
> _regression(ts_delta(close,1),ts_backfill
> Vec_aVg(mdl138
> qpdi3_sale_empl ) , 66),200
> Theme: IND Region Theme X2
> Regular Alpha
> Pyramid theme: INDIDIIMODEL X1.5
> ts_decay_
> Iinear(rank
> -re),20 -
> Pyramid theme: INDIDIIPV X1.5
> Simulation Settings
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> Instrument Type
> Region
> Universe
> Language
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handl
> 2.44
> 19.36%
> 2.13
> 14.71 %
> 8.669
> 15.209600
> Equity
> IND
> TOPSOO
> Fast Expression
> 0.08
> Subindustry
> On
> On
> Verify
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.07
> 16.6396
> 0.73
> 7.659
> 8.66%
> 9.209600
> 104
> 102
> 2014
> 2.37
> 16.3996
> 2.43
> 17.1796
> 4.33%
> 20.959600
> 103
> 103
> Clone Alpha
> 2015
> 2.64
> 17.8596
> 2.59
> 17.1396
> 4.78%
> 19.189600
> 121
> 126
> 2016
> 2.70
> 19.8996
> 2.33
> 14.8696
> 2.36%
> 14.949600
> 139
> 143
> 2017
> 2.02
> 21.7396
> 1.36
> 9.7996
> 4.26%
> 9.019600
> 140
> 145
> Chart
> Pnl
> 2018
> 3.56
> 19.9496
> 3.72
> 21.829
> 4.83%
> 21.889600
> 157
> 159
> 2019
> 2.58
> 20.2096
> 2.19
> 14.5296
> 2.759
> 14.389600
> 182
> 185
> 2020
> 3.70
> 20.0796
> 3.98
> 23.209
> 5.36%
> 23.129600
> 182
> 181
> 1OM
> 2021
> 2.51
> 20.3196
> 2.05
> 13.5696
> 2.689
> 13.359600
> 166
> 181
> 2022
> 1.44
> 20.5296
> 88
> 7.7596
> 3.80%
> 7.559600
> 190
> 192
> 5,0OOK
> 2023
> 3.46
> 18.4496
> 2.86
> 12.6196
> 0.49%
> 13.689600
> 198
> 201
> Investability constrained
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
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.44
> 10.45%
> 1.19
> 8.549
> 10.579
> 16.339600
> Decay
> Year


---

## 讨论与评论 (23)

### 评论 #1 (作者: CY96125, 时间: 7个月前)

这个模板和思路应该也能应用在其他region

---

### 评论 #2 (作者: MY82844, 时间: 7个月前)

感谢分享，感觉可能是universe比较小的缘故，performance和pc对参数变化还比较敏感

regression_proj说不定也开始试下risk factor loading

---

### 评论 #3 (作者: 顾问 YH25030 (Rank 31), 时间: 7个月前)

谢谢您的分享。想问一下，ts_regression的回测时间长吗？以前再其他其他区用过ts_regression，感觉回测时间特别长。

---

### 评论 #4 (作者: CL86067, 时间: 7个月前)

学到了，感谢大佬分享模板，感觉IND区域还是蛮不一样的，原来模板跑出好多都是robust universe sharp 不符合要求，似乎和部分股票无法做空有关系，看之前CHN区域是这样的，不知道您的这个操作，用regression_proj剔除市值的影响，是不是有助于解决这个问题呢？

---

### 评论 #5 (作者: XW23690, 时间: 7个月前)

感谢分享，思路很好：“股价与基本面过度拟合→未来回归下跌”。高换手可能是日频股价变化：ts_delta(close,1)，解决方法我暂时有以下想法，第一种是平滑滚动信号：re = ts_mean(ts_rank(-re, day), day)；第二种是加入group分组做中性化处理，我自己也测试过IND区域几乎都会降低turnover并且不丢失表现，针对longcount和shortcount较少的alpha，group_backfill(x,sector,day,std=4)很适用；第三种则是用ts_target_tvr_decay以及ts_target_tvr_hump来调整，不过容易丢失performance

---

### 评论 #6 (作者: DS48533, 时间: 7个月前)

这就是手搓党嘛，完全不懂金融的我，看着干着急，又学不会。不过尝试把你的表达式整理为参考模版，给AI作为参考好咯～

---

### 评论 #7 (作者: QY56710, 时间: 7个月前)

感谢分享.有一个小tip：Robust Sharpe较低时可以适当降低decay的值

---

### 评论 #8 (作者: ZX52486, 时间: 7个月前)

从基本面出发也能拿到一个不错的表现，但是换手率依旧很高，但同时return也高达20%


> [!NOTE] [图片 OCR 识别内容]
> 多时间序列对比 (可交互缩放)
> IM
> 3M
> GM
> 1丫
> All
> IYbSSIqM
> omSeV3w5
> Om3WdYnq
> DM
> 786V022b
> JjELmZSE
> 3qrWxkVQ
> Wjomdxrx
> pWrgEpjg
> SM
> NImoGljg
> DM
> SM
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020


而且可以明显发现在subindustry中和条件下，alpha的性能更好，使用线性衰减平滑时，性能并未明显降低


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> eXP
> fitness
> turnoVer
> margin
> neutralization
> decay
> SECTOR
> 15
> 78bVQZZb
> rank(rank(
> 3.40
> 2.35
> 0.4381
> 0.000958
> 15
> JjELmZSE
> (rank(-ts
> 3.40
> 2.35
> 0.4381
> 0.000958
> 25
> pwrgEpjg
> rank(rank(
> 2.99
> 2.22
> 0.3371
> 0.001103
> 25
> NImoGljg
> (rank(-ts_
> 2.99
> 2.22
> 0.3371
> 0.001103
> SUBINDUSTRY
> 20
> 1YbSSIqM
> rank(-tsr
> 3.58
> 2.64
> 0.3748
> 0.001089
> 15
> omSeV3w5
> rank(rankl
> 3.88
> 2.76
> 0.4330
> 0.001011
> 15
> Om3Wdynq
> (rank(-ts_
> 3.88
> 2.76
> 0.4330
> 0.001011
> 25
> 3qrWxkVQ
> rank(rank(
> 3.37
> 2.55
> 0.3366
> 0.001149
> 25
> WjQmdxrx
> (rank(-ts
> 3.37
> 2.55
> 0.3366
> 0.001149
> sharpe


---

### 评论 #9 (作者: CH92851, 时间: 7个月前)

regression_proj 可惜这个我用不了。

---

### 评论 #10 (作者: HL16690, 时间: 7个月前)

regression_proj(） 显示没有这个方法

---

### 评论 #11 (作者: BJ65592, 时间: 7个月前)

感谢大佬的分享，从邮件里看到了这篇帖子，一开始没有很看懂，仔细研究了regression操作符后大概能理解了
通过使用历史长期的数据，试图找到某个数据与股票走势相关的函数，并返回当前股价波动与函数预估出来的股价波动的差值
如果股价波动高于预估值，则说明股价被高估，应该做空，反之亦然
是一个经典的反转因子，学到了一招，再次感谢大佬！

---

### 评论 #12 (作者: HL81191, 时间: 7个月前)

非常感谢，这个模板让我第一次成功提交IND的alpha，两个星期以来我自己在IND尝试的模板总是有Robust universe Sharpe或Weight等等其他条件无法通过。而这个模板在不用上二阶三阶的情况下就能出很多指标很好的alpha，我今天直接点塔了

---

### 评论 #13 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 7个月前)

data = ts_regression(ts_delta(close,1),ts_backfill(<vec/>(<filed/>),<d1/>),200);  
re = data -regression_proj(data,rank(cap));   
rank(-re)

新模板累积中，不过我没有regression_proj和regression_neut，有其他代替吗。

==================================================================================

知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值
==================================================================================

---

### 评论 #14 (作者: ZX52486, 时间: 7个月前)

您好，一组任务的时间大概是500到600秒

---

### 评论 #15 (作者: ZX52486, 时间: 7个月前)

关于robust的问题也有这方面的考虑，CHN由于涨跌幅的限制难以做空拿到在模拟盘的收益，而IND也有相似之处，在此之前，您可以参考之前CHN的那篇帖子

---

### 评论 #16 (作者: ZX52486, 时间: 7个月前)

关于没有regression_proj和regression_neut的问题，暂时没有对策

---

### 评论 #17 (作者: HZ10678, 时间: 7个月前)

感谢分享，同样遇到不能用regression_proj的问题，在某些情况下使用regression_neut也可以优化alpha。

或者直接使用前面的代码：

data = ts_regression(ts_delta(close,1),ts_backfill(vec_avg(XXX),66),200);

很多时候也已经够用。

尝试过以下变形

data = ts_regression(ts_delta(close,1),ts_scale(ts_backfill(vec_avg(XXX),66), 252),200);

亦能减少相关性或者提高性能

---

### 评论 #18 (作者: XG98059, 时间: 7个月前)

Alpha expression includes a reversion component so we may not accept these alphas in the future, try working on different alpha ideas。想法很好，但是会有这个warining

---

### 评论 #19 (作者: HZ99685, 时间: 6个月前)

小白不理解，为什么拟合的越好未来股价可能会下跌？也有可能上涨啊？

---

### 评论 #20 (作者: WW36313, 时间: 6个月前)

您好，我想请问一下为了避免权重过于集中还有什么比较好的优化思路呢？

---

### 评论 #21 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

和模板大师里面的模板比较类似

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #22 (作者: MY82844, 时间: 5个月前)

[XG98059](/hc/en-us/profiles/34425600380695-XG98059)  应该是delta(close,1)这个片段被识别成a reversion component了

---

### 评论 #23 (作者: LJ12230, 时间: 1个月前)

感谢大佬分享!

---

