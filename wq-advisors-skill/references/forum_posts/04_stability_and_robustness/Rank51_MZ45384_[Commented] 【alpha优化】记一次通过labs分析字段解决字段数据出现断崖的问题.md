# 【alpha优化】记一次通过labs分析字段，解决字段数据出现"断崖"的问题

- **链接**: [Commented] 【alpha优化】记一次通过labs分析字段解决字段数据出现断崖的问题.md
- **作者**: YW84713
- **发布时间/热度**: 6个月前, 得票: 9

## 帖子正文

找到一个信号，但发现数据在尾部时pnl走势变平

通过labs观察字段数据分布发现，在20年后数据呈现整体性断崖式骤跌，怀疑这部分数据影响了后续的表现


> [!NOTE] [图片 OCR 识别内容]
> 2020


字段经过ts_backfill处理仍不能解决问题


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 300OK
> 2,0OOK
> 0OOK
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
> Investa
> Constrained Pnl
> o IS
> Testing Status
> Period
> TRAIN
> TEST
> 0S
> 7 PASS
> 1 FAIL
> IS ladder Sharpe of 0.56 is below cutoff of 1.58 for ladderyear 2: 1/20/2023.
> 1/21/2021.
> Jbility


但在group_backfill之后，问题得到解决


> [!NOTE] [图片 OCR 识别内容]
> 0OOK
> ZOOOK
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
> Investability Constrained Pnl
> IS Testing Status
> Period
> TRAIN
> TEST
> 05
> 8 PASS
> 1 WARNING


推测：

1. ts_backfill时，因为断崖后数据呈现急速回涨的情况，出现na数据被填入了之前的差值，不符合期望值，导致后续数据出现被污染的情况

2. group_backfill不一样，会取组中非na值的Winsorized 均值，就让数据更均衡

---

## 讨论与评论 (3)

### 评论 #1 (作者: CY96125, 时间: 5个月前)

这个思路真的给我打开了，之前一直想要学习lab，看来在干中学才是真正能够提升自己的方式。言尽于此，感谢大佬的分享，我想在之后的研究中我也会常用lab，走上量化的正轨

---

### 评论 #2 (作者: YY31580, 时间: 5个月前)

感谢分享！很有帮助

---

### 评论 #3 (作者: 顾问 MZ45384 (Rank 51), 时间: 5个月前)

A new feature noted. group_backfill以组中非nan的Winsorized 均值回填让数据更均衡，可解决数据出现断崖的情况。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

