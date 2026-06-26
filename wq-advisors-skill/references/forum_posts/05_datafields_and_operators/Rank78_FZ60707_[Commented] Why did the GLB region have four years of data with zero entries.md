# Why did the GLB region have four years of data with zero entries?

- **链接**: [Commented] Why did the GLB region have four years of data with zero entries.md
- **作者**: XW25488
- **发布时间/热度**: 1个月前, 得票: 8

## 帖子正文

Hello everyone, I encountered the problem shown in the image when testing GLB. The values ​​for 2014-2017 were all 0. Is this normal? 
> [!NOTE] [图片 OCR 识别内容]
> Year
> Shamps
> Turover
> Fitnzss
> Retums
> Drawdown
> Margin
> Long Count
> Short Count
> 201-
> 0.O0
> 0.3035
> 0.07
> 0.03
> 0.039
> 0OOXo:
> 2015
> 0.30
> 0.3095
> 0.03
> 0.039
> 0.038
> 2016
> 0.O0
> 0.3095
> 0.03
> 0.039
> 11N
> 2017
> 0.37
> 0.303
> 71
> 3.039
> 11
> 2018
> 73
> 255:
> 439
> 918?
> 2270
> 13
> 2019
> 803
> 0.75
> 43-
> E39:
> 7.17:
> 5J27
> 3327
> 2020
> I
> -1722
> 19.759
> -31.235
> 5-53
> 3235
> 2021
> 14
> 10.593
> 272
> 23.13
> 3.059
> S120
> _5
> JTJ
> 2022
> 72
> 11.573
> 3.57
> 26.53
> TE39
> 4E.158:
> 5303
> 435
> 2023
> 03
> 5095
> 0.13
> 1.91
> 7.479
> S:
> 5243
> 3830


-----------------------------------------

Update & Summary for the thread:

1. **Known Data Gaps:**  I've confirmed that the following datafields have missing data for the period in question: GLB-earnings6 and EUR-snt26.
2. **Operator Lookback Mismatch:**  The problem can also be caused by operators. If an operator uses a long lookback window that requires data from before a datafield's coverage starts, it cannot generate a valid signal, which also results in zero positions and zero metrics.

---

## 讨论与评论 (12)

### 评论 #1 (作者: TL72720, 时间: 2个月前)

Hi XW25488, that's an interesting observation. Zero entries for that period in the GLB region could stem from several factors, such as data availability issues, a period of market inactivity in that specific region, or perhaps the specific data source you're using doesn't cover that timeframe for GLB. Have you checked if there were any known data breaks or reporting changes for that region around 2014-2017?

---

### 评论 #2 (作者: 顾问 PN39025 (Rank 87), 时间: 2个月前)

This is normal because some datasets only have data measured from 2017 to now, so there is no information before that. If you are sure your alpha is okay, then submit it.

---

### 评论 #3 (作者: KP26017, 时间: 2个月前)

The most common cause is that your alpha uses a data field or operator with a lookback window that requires historical data going back further than your earliest available data point. If your dataset only starts providing coverage from 2017 or 2018, and your operators require say 252 days of history to initialize, the simulation has no valid signal to generate for the earlier years and defaults to zero positions and zero metrics.

For GLB specifically, many data fields — particularly alternative data, certain model datasets, and some fundamental fields — have coverage start dates well after 2014. The simulation period starts at 2014 but the data simply doesn't exist yet for those years.

---

### 评论 #4 (作者: 顾问 RM79380 (Rank 81), 时间: 2个月前)

This tells us that this is a straight line alpha. Try backfilling your data or avoid that datasets.

---

### 评论 #5 (作者: YD84002, 时间: 2个月前)

The early years (2014–2017) show zeros because the backtest likely started in 2018, or the strategy generated no trades/signals before that year.

---

### 评论 #6 (作者: MY82844, 时间: 2个月前)

Is that because of the short date coverage? What is the coverage from the data explorer? 
> [!NOTE] [图片 OCR 识别内容]
> Dale
> Coverage
> Coverage
> 95沁
> 1003
> 9
> 10090
> 95沁
> 1003


====================================================================

"Pain + Reflection = Progress"

====================================================================

---

### 评论 #7 (作者: 顾问 CT48231 (Rank 2), 时间: 2个月前)

As i know, the datafields you used to create the alpha has no trading data from 2014 to 2017. this is normal. but notify datafield that only has trading data of 2-3 year (2021-2023). It maybe overfit

---

### 评论 #8 (作者: TL72720, 时间: 2个月前)

Hi XW25488, that's an interesting observation. Zero entries for GLB in that period could stem from a few things: perhaps data availability issues for that specific region during those years, or it might indicate a period where no relevant securities were present or actively traded in our universe for that region. Have you checked if there were any known data feed interruptions or significant market structural changes for GLB around that time frame?

---

### 评论 #9 (作者: 顾问 FZ60707 (Rank 78), 时间: 2个月前)

Yes, this is completely normal. This GLB dataset does not contain any entries for the 2014–2017 period, likely because the data coverage starts after 2017. In other words, those years fall outside the dataset's available time range — effectively, the dataset didn't exist or wasn't populated back then.

---

### 评论 #10 (作者: NT63388, 时间: 1个月前)

This is a normal issue, especially with new datasets.
Personally, I avoid working with new datasets because they haven't been evaluated over a long period, so there is always a possibility of them being decommissioned (DECOM).

---

### 评论 #11 (作者: 顾问 JN96079 (Rank 44), 时间: 1个月前)

That's true. There is no data to backtest for those years with the datafield; either it's a new datafield on the platform, or it came into existence after those years with zero metrics.

^^JN

---

### 评论 #12 (作者: DT49505, 时间: 21天前)

Thanks for raising this, i would like to know it too!

---

