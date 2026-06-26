# 【Alpha 模板】ASI推出新的universes：TOP500，成功点亮Risk Pyramid

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha 模板】ASI推出新的universesTOP500成功点亮Risk Pyramid_40020159075607.md
- **作者**: WL58980
- **发布时间/热度**: 2个月前, 得票: 20

## 帖子正文

就在前几天ASI推出了新的universes：TOP500，抱着试一试的心态成功点亮了Risk Pyramid，所以给大家分享一下这个模板。 
> [!NOTE] [图片 OCR 识别内容]
> ASIIDI/Risk
> Submissions: 3
> Active
> Clickto view datasets


模板如下：

```
-<group_operator/>(<time_series_operator/>(<data_field/>, <days/>),exchange)
```

其中：

1、group_operator使用的是group_neutralize，大家可以尝试一下其他的；

2、time_series_operator选择的是last_diff_value，ts_backfill，ts_decay_linear，ts_sum，ts_ir，ts_mean等；

3、data_field选择的是ASI / D1 / TOP500 / risk70;

4、days可以是63,126,252。

Alphas表现展示(开了maxtrade表现也相差无几)：


> [!NOTE] [图片 OCR 识别内容]
> 3=
> 252),
> 252
> ;group_neut
> Theme: AlI regions/D1 Power Pool Apr ` 26 21
> Single Data Set Alpha
> Simulation Settings
> Power Pool Alpha
> Pyramid theme: ASIIDI/RISK X1
> Instrument Type:
> Equity
> Neutralization:SIOW
> Fast
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> RetUrhs
> DrawdOwh
> Margin
> Region:
> ASI
> Factors
> 1.63
> 21.729
> 1.25
> 12.76%
> 11.949
> 11.759600
> Universe:
> TOPSOO
> Pasteurization:
> On
> Language:
> Fast Expression
> Lookback:
> Decay:
> Max Trade:
> Off
> Delay:
> Max Position:
> Off
> Year
>  Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Truncation:
> 2014
> 2.15
> 23.2595
> 1.82
> 16.7595
> 5.3795
> 14.419o00
> 257
> 263
> 2015
> 1.75
> 23.81%
> 1.35
> 14.159
> 5.689
> 11.90Y6oo
> 262
> 255
> 2016
> 1.15
> 22.80%5
> 0.72
> 8.8795
> 6.52%
> 7.7830
> 260
> 260
> Clone Alpha
> 2017
> 2.88
> 23.03%
> 2.70
> 20.20%
> 3.599
> 17.549ooo
> 263
> 256
> 2018
> 1.40
> 22.73%
> 1.04
> 12.509
> 4.0495
> 11.003oo
> 260
> 264
> Chart
> Pnl
> 2019
> 1.39
> 22.4995
> 0.93
> 10.1395
> 4.99%5
> 9.019o00
> 262
> 270
> 2020
> 1.08
> 19.8596
> 0.72
> 8.82%
> 11.22%
> 8.893o0
> 299
> 293
> 2021
> 1.75
> 19.5095
> 1.49
> 13.99%
> 5.839
> 14.359600
> 303
> 299
> 2022
> 0.93
> 19.6795
> 0.55
> 7.0895
> 4.78%
> 7.20300
> 277
> 276
> 2023
> 1.91
> 9.959
> 1.65
> 14.86%
> 4.1495
> 14.89300
> 278
> 278



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 05
> group
> 252), exchange
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: ASIIDIIRISK X1
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 1.73
> 20.299
> 1.61
> 17.679
> 18.349
> 17.429600
> Instrument Type:
> Equity
> Truncation:
> 0,06
> Region:
> A5I
> Neutralization:
> Fast Factors
> Universe:
> TOPSOO
> Pasteurization:
> 0n
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> Language:
> Fast Expression
> Lookback:
> Decay:
> Max Trade:
> Off
> 2014
> 1.81
> 25.16%
> 1.73
> 22.86%
> 14.27%
> 18
> 79oo0
> 294
> 226
> Delay:
> Vax Position:
> Off
> 2015
> 2.07
> 21.79%
> 1.88
> 17.94%
> 3.23%
> 16.479600
> 281
> 236
> 2016
> 0.69
> 22.119
> 0.42
> 8.29%
> 17.38%
> 7.503oo
> 294
> 227
> 2017
> 2.48
> 21.1496
> 2.53
> 22.0495
> 5.30%5
> 20.86900
> 296
> 223
> Clone Alpha
> 2018
> 2.52
> 20.1495
> 2.87
> 26.08%
> 02%
> 25
> 03ooo
> 299
> 225
> 2019
> 1.17
> 19.86%
> 0.81
> 9.459
> 3.449
> 9.51900
> 294
> 238
> Chart
> Pnl
> 2020
> -0.11
> 17.3695
> 0.03
> 1.2095
> 18.3495
> -1.38300
> 320
> 271
> 2021
> 3.16
> 17.66%
> 4.16
> 30.5496
> 4.58%
> 34.59300
> 334
> 268
> 2022
> 2.26
> 18.839
> 2.51
> 23.249
> 82%
> 24.68900
> 303
> 249
> 2023
> 1.55
> 18.63%
> 1.44
> 16.0995
> 6.3595
> 17.279600
> 314
> 242


由于TOP500是最近新推出的，所以相关性还是比较低的，如果大家觉得这个模板对你有所帮助，请点点赞，后续将继续为大家分享模板。

---

## 讨论与评论 (7)

### 评论 #1 (作者: XW25488, 时间: 1个月前)

谢谢分享，老师速度还是很快啊

---

### 评论 #2 (作者: LG87838, 时间: 1个月前)

感谢分享，对点塔太有帮助了。

忽略了小铃铛，那就一定要多看看顾问中文论坛，两个都不看，大概率要忽略了很多重要的信息了。

============================================================================

慢慢来，详细时间的力量。

============================================================================

---

### 评论 #3 (作者: HY22845, 时间: 1个月前)

非常感谢，帮助我挖到了ASI的第一个阿尔法！

---

### 评论 #4 (作者: JL52079, 时间: 1个月前)

大佬 我用您的模板跑risk70跑出来的turnover特别高，70%多，有什么方法解决吗？或者有什么具体的risk数据集推荐吗？感谢大佬分享，祝大佬常驻GM！
=============================== Just do it ！===============================

---

### 评论 #5 (作者: LL49894, 时间: 1个月前)

ASI真是不好做啊

---

### 评论 #6 (作者: XW23690, 时间: 1个月前)

感谢分享 ASI是真的难做呀！

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #7 (作者: 顾问 MZ45384 (Rank 51), 时间: 18天前)

这么简洁的模板居然还能出这么多ra，难道小宇宙真是一片蓝海。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

