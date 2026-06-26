# [Alpha Inspiration] Reversal During Earnings-AnnouncementsAlpha Idea

- **链接**: [L2] [Alpha Inspiration] Reversal During Earnings-AnnouncementsAlpha Idea.md
- **作者**: TN48752
- **发布时间/热度**: 2年前, 得票: 20

## 帖子正文

**Paper:** News-Driven Return Reversals: Liquidity Provision Ahead of Earnings Announcements

**Authors:** So, Wang

**Link:**  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2275982](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2275982)

Even though  [earnings announcements](https://quantpedia.com/screener/?FilterKeywords=earnings+announcement)  are anticipated events in most cases, multiple academic papers find the evidence that they still affect stock prices and therefore create a potentially profitable trading opportunity. For instance, one of the recent works shows that  [the short-term reversal](https://quantpedia.com/strategies/short-term-reversal-in-stocks/)  is much stronger around the days of earnings announcement than in other, randomly chosen periods. More precisely, the LOW-HIGH (buying past losers and selling past winners) strategy yielded an average 3-day return (the window of t-1, t, and t+1, where t is the day of earnings announcement) of 1.45% during the 1996-2011 sample period. In contrast, the average return during random pseudo-announcement periods was only 0.22% (therefore more than a six-fold difference). The phenomenon, as suggested by the authors, is related to market makers‘ decisions regarding liquidity provision (see fundamental reason). The strategy further described is carried out on the subsample of big stocks due to better liquidity.

**Fundamental reason**

In general, a reversal in the price of an asset occurs due to investors’ overreaction to asset-related news and the subsequent price correction. In this case, the most probable reason for the phenomenon, according to the authors, is the market makers’ aversion to inventory risks that tend to increase dramatically in  [the pre-announcement period](https://quantpedia.com/strategies/earnings-announcement-premium/) . Consequently, the market makers demand higher compensation for providing liquidity due to higher risk and therefore raise prices, which are expected to reverse after the earnings announcement.

**Implementation**

Firstly, the investor sorts stocks into quintiles based on firm size. Then he further sorts the stocks in the top quintile (the biggest) into quintiles based on their average returns in the 3-day window between t-4 and t-2, where t is the day of the earnings announcement. The investor goes long on the bottom quintile (past losers) and short on the top quintile (past winners) and holds the stocks during the 3-day window between t-1, t, and t+1. Stocks in the portfolios are weighted equally.

**Data**

ern3_expected_time - expected time of earnings announcement

returns - daily return

---

## 讨论与评论 (10)

### 评论 #1 (作者: AG20578, 时间: 2年前)

Hi! Thank you for sharing.

Could you kindly clarify how you are utilizing ern3_expected_time in your alpha? Are you comparing this field with some other time-related field?

---

### 评论 #2 (作者: TN48752, 时间: 2年前)

Thank you for asking. The author gives the idea of long on the bottom quintile (past losers) and short on the top quintile (past winners), so I will use -(returns) as the original alpha. Then I will nest a cross sectional function to remove the out lier. Next I use neut functions like vector neut or regression neut to neutralize return according to ern3_expected_time


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> PI_
> 175N
> 1SM
> 12SN
> ION
> 7.5OOK
> OOOK
> SOO
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> egate Data
> Sharo
> TUCII
> C-EC
> ReTUTn
> Drawaown
> Marein
> 2,52
> 69,80%
> 1,25
> 17,1396
> 9,939
> 4,9一
> 0000
> Sharpe
> Tumover
> Htness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 212
> 5,10
> 7173
> 311
> 25,73:
> 1:
> 一20:
> 113
> 1037
> 2013
> 2
> 73,555
> 34
> 10,22沁
> 33
> 2,330:
> 14
> 1107
> 21-
> 2,72
> 53,+3
> 1517:
> 一-3:
> -370:
> 1270
> 1223
> 215
> 71,35
> 13
> 034
> 2570:
> 1257
> 1255
> 2115
> 69,0555
> 1236沁
> 15:
> 5390:
> 12-5
> 1192
> 217
> 2,50
> 63,3551
> 1302:
> -9:
> 3,730:
> 1209
> 1173
> 213
> 319
> 1512:
> 3,44*
> 550:
> 124-
> 1221
> 2119
> 6,541
> 7,57:
> 7,761:
> 2,240:
> 1
> 1211
> 220
> 153
> 53,273
> 2953:
> 171:
> 540:
> 1225
> 1163
> 21
> 3
> 7,31
> 220
> 3113
> 一13:
> 3:
> 1+5
> 1410
> 2022
> 一43
> 71,50
> 31,3
> 53::
> 730
> 1579
> 151
> 医 Correlation
> Self Correlation
> Hiahes: Correlation
> Last Run:
> Add Alphato
> USt
> Open alpha details in new t3b
> Check Submission
> Submit Alpha 
> AeBr
> Yoar


The alpha signal is very clear, the alpha submit can be achieved after adding simple transaction trigger conditions to reduce turnover, or more simply using decay functions

---

### 评论 #3 (作者: AG20578, 时间: 2年前)

Thank you for clarification! Do you observe a significant change in alpha performance with and without using ern3_expected_time? I just want to understand, does this field really contributes to the signal and how.

---

### 评论 #4 (作者: TN48752, 时间: 2年前)

Actually, using -returns itself gives a very clear signal. I noticed that adding the ern3_expected_time element doesn't really improve the signal, maybe it just reduces prod corr

---

### 评论 #5 (作者: XD81759, 时间: 1年前)

AG20578, well, from my observation, like I said before, using just -returns already gives a clear signal. While adding the ern3_expected_time element, it doesn't seem to enhance the signal much. It might just help a bit with reducing prod corr. But in terms of improving the alpha performance significantly, it doesn't play a major role here. Maybe in some other scenarios or with different factor combinations, it could have more impact, but in this specific alpha, its contribution to strengthening the signal is rather limited.

---

### 评论 #6 (作者: XL31477, 时间: 1年前)

**Yeah, I agree with both  [TN48752](/hc/en-us/profiles/13714359745431-TN48752)  and  [XD81759](/hc/en-us/profiles/23494746482967-XD81759) . In this particular alpha, ern3_expected_time indeed doesn't boost the alpha performance much. It mainly seems to deal with reducing prod corr rather than strengthening the signal significantly. But we can't rule out its potential use in other setups or with different factor combos. Maybe exploring further variations could reveal more value from it.**

---

### 评论 #7 (作者: BA51127, 时间: 1年前)

Based on the discussion, it seems that the  `ern3_expected_time`  field in the alpha strategy doesn't significantly enhance the performance but may help in reducing product correlation. Here are three concise points:

1. The primary signal in this alpha comes from the -returns, and  `ern3_expected_time`  doesn't substantially improve it.
2. The field might play a more substantial role in different scenarios or with various factor combinations.
3. Further exploration of  `ern3_expected_time`  in other setups could potentially reveal additional value.

---

### 评论 #8 (作者: 顾问 CC40930 (Rank 95), 时间: 1年前)

This paper introduces an intriguing strategy based on earnings announcements and liquidity provision by market makers. The idea of using the LOW-HIGH reversal strategy (buying past losers and selling past winners) around earnings announcements is compelling, particularly given the strong evidence of return reversals. The approach of sorting stocks by size and historical returns before earnings is well thought out, and targeting large-cap stocks for liquidity reasons makes sense. The idea that market makers increase prices due to inventory risks before announcements adds a solid fundamental basis to the strategy. It would be interesting to test this strategy on more recent data to check for continued profitability.

---

### 评论 #9 (作者: KS69567, 时间: 1年前)

A convincing approach that takes use of market maker liquidity and profit releases is presented in this research. Because of the compelling evidence for return reversals, the LOW-HIGH reversal strategy—buying previous losers and selling past winners—is especially alluring around earnings events. The possibility to take advantage of market inefficiencies related to earnings releases is exceptional.

---

### 评论 #10 (作者: 顾问 ZH78994 (Rank 11), 时间: 1年前)

Thank you so much for sharing your incredible work with us! Your writing not only showcases your talent but also offers valuable insights and inspiration. I truly appreciate the time and effort you’ve put into creating something so thoughtful and meaningful. It’s clear that you have a gift for storytelling, and your work has left a lasting impression on me. Please keep sharing your wonderful creations—I’m already looking forward to your next piece! Thank you again for your generosity and dedication.

---

