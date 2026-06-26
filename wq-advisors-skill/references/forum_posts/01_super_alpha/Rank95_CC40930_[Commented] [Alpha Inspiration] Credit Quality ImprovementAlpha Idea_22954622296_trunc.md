# [Alpha Inspiration] Credit Quality ImprovementAlpha Idea

- **链接**: https://support.worldquantbrain.com[Commented] [Alpha Inspiration] Credit Quality ImprovementAlpha Idea_22954622296855.md
- **作者**: OG25133
- **发布时间/热度**: 2年前, 得票: 9

## 帖子正文

**Textbook:** Options, Futures and Other Derivatives, Chapter 24: Credit Risk

**Author:** John C. Hull

**Link:**  Annotated PDF copy available on request from  [olly.gormley@gmail.com](mailto:olly.gormley@gmail.com)

#### **Alpha idea:**

From Section 24.2: Historical Default Probabilities:
"for investment-grade bonds, the probability of default in a year tends to be an increasing function of time... This is because the bond issuer is initially considered to be creditworthy, and the more time that elapses, the greater the possibility that its financial health will decline. For bonds with a poor credit rating, the probability of default is often a decreasing function of time......The reason here is that, for a bond with a poor credit rating, the next year or two may be critical. The longer the issuer survives, the greater the chance that its financial health improves"

**BRAIN implementation:**

Define the stock's credit quality improvement score as the decrease in the short-term default probability/medium-term default probability ratio over the last quarter, as this indicates that the probability of default slope is increasing, and hence indicates improvement in credit quality.

First iteration: Go long stocks who outperform their peers in terms of this metric.

Second iteration: After using ChatGPT to suggest possible fields that could interact with credit quality improvement, apply this strategy to stocks who have lower current dividend yield relative to their peers because they might not yet be recognized by the market as stable income-providing stocks, meaning they could be undervalued and have greater price increase from credit quality improvements.

**Dataset:** model53 (Creditworthiness Risk Measure Model)

**Performance:**


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 8,0OOK
> 6,0OOK
> 4,00OK
> 2,00OK
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
> Vhjln



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.66
> 31.059
> 1.18
> 15.649
> 8.229
> 10.089oo
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2012
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2013
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2014
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2015
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2016
> 0.62
> 33.729
> 0.24
> 4.989
> 7.099
> 2.959o。
> 312
> 341
> 2017
> 1.74
> 31.75%
> 1.10
> 12.75%
> 4.23%
> 8.0390。
> 313
> 302
> 2018
> 1.39
> 33.139
> 0.86
> 12.62%
> 5.28%
> 7.629o。
> 246
> 358
> 2019
> 1.15
> 27.01%
> 0.78
> 12.35%
> 8.22%
> 9.1490。
> 275
> 300
> 2020
> 2.94
> 30.109
> 3.12
> 33.79%
> 3.639
> 22.45900
> 261
> 308
> 2021
> 2.43
> 30.109
> 2.11
> 22.80%
> 3.709
> 15.159oo
> 316
> 308
> 2022
> -6.38
> 37.149
> -7.74
> -54.69%
> 2.949
> 29.45900
> 288
> 352
> Long


**Status:** Submitted

**Questions:** What potential weaknesses does this alpha have that could be improved?

Thanks,

Olly Gormley

---

## 讨论与评论 (17)

### 评论 #1 (作者: AG20578, 时间: 2年前)

Hi Olly,

Thank you for sharing your alpha idea! Could you kindly provide more details about the region and universe in which this alpha is implemented? Noting that the long+short count is around 600, I'm curious about the coverage of the universe.

In terms of potential areas for improvement, at first glance, it appears that this alpha concentrates on instruments with improving credit quality and lower dividend yield. This approach might result in a lack of diversification. Could you share your thoughts on this?

Looking forward to your response.

Anastasia

---

### 评论 #2 (作者: OG25133, 时间: 2年前)

Hi Anastasia. It is USA Top 3000.

I've pasted the coverage visualisations below.

The sector coverage looks fairly evenly split across 7/12 sectors with utilities, financials and diversified receiving a smaller coverage and funds and government sectors receiving no coverage.

Q. Is it important for an alpha to have some coverage across all sectors or is lack of coverage in 1/2 sectors not a critical problem?

Investment companies have by far the largest industry coverage but it looks relatively evenly split across industries also.

What are your thoughts just from looking at these visualisations?


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Coverage By Sector
> 100
> 80
> 60
> 
> 8
> 40
> 20
> Change coverage
> nonNaN coverage
> non-Zero coverage
> Financial
> Industrial
> 
> Government
> Utilities
> Materials
> Non-Cyclicals
> Communications
> Cyclicals
> Funds
> Technology
> Energy
> Consumer
> Basic 
> Consumer



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Coverage By Industry
> 100
> 80
> 60
> 
> 8
> 40
> 20
> 9
> 9
> C〉
> 9
> 9
> 9
> 9
> Change coverage
> nonNaN coverage
> non-Zero coverage
> Control
> Fund
> Fund
> Banks
> Gas
> Telecommunications
> Equipment
> Materials
> Water
> Investment
> Software
> Services
> Containers
> Wares
> Products
> Gas
> Lodging
> Construction
> Hobbies
> Companies
> Shipbuilding
> Debt 
> Equity
> Environmental
> Healthcare
> Products
> Healthcare
> Building
> Games
> Business
> Investment
> Alternative
> Packaging
> Engineering
> Household
> ToyS'
> Office



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Coverage Of Universe
> 800
> 700
> 600
> Mb
> 500
> 400
> 300
> 200
> 100
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
> NMNMNNM


---

### 评论 #3 (作者: OG25133, 时间: 2年前)

And with regards to your question, maybe I could create a custom group based on another data field which ensures broader coverage and then could apply group_rank(dividend_yield, custom_group) instead of rank(dividend_yield) as the enter condition. That way instead of considering only dividend yield rank in the market, you are considering the relative rank of the dividend yield within groups which consider this other metric, so ensuring coverage across the custom groups.

What are your thoughts?

---

### 评论 #4 (作者: OG25133, 时间: 2年前)

I am thinking that dividend yield ignores growth stocks which are reinvesting, maybe smaller market cap and higher P/E ratios so these could be prospects for the custom_group data field

---

### 评论 #5 (作者: OG25133, 时间: 2年前)

I'll test this approach and let you know the results

---

### 评论 #6 (作者: OG25133, 时间: 2年前)

I neutralised on best PE ratio. (group_neutralize(alpha, best PE ratio))

- Sharpe improved by 11%.
- Fitness improved by 5%
- Drawdown improved by 0.77%
- Slight decrease in returns of 0.96%
- Regret that I didn't submit this version of my alpha increased by 13%

This was consistent with my intuition above - thanks for guiding me in this direction.


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.85
> 32.879
> 1.24
> 14.689
> 7.45%
> 8.939o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2012
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2013
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2014
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2015
> 0.00
> 0.00%
> 0.00
> 0.00%
> 0.00%
> 0.00%oo
> 2016
> 0.80
> 35.76%
> 0.33
> 6.139
> 6.549
> 3.43%0。
> 307
> 332
> 2017
> 1.33
> 33.06%
> 0.68
> 8.639
> 4.959
> 5.2290。
> 288
> 314
> 2018
> 1.61
> 34.809
> 0.96
> 12.31%
> 4.16%
> 7.0790。
> 262
> 333
> 2019
> 1.89
> 30.079
> 1.36
> 15.57%
> 6.05%
> 10.36%o。
> 284
> 283
> 2020
> 3.54
> 31.389
> 3.52
> 31.09%
> 3.049
> 19.8290。
> 271
> 289
> 2021
> 2.16
> 31.56%
> 1.66
> 18.709
> 4.16%
> 11.859oo
> 311
> 304
> 2022
> -5.05
> 39.709
> -4.98
> -38.61%
> 2.349
> -19.45900
> 286
> 345
> Long


Some other neutralisations I tested which also improved the alpha:

- FY1 (future year) Revenue growth -- Sharpe 1.77, Fitness 1.19
- Accounts receivable turnover -- Sharpe 1.78,  Fitness 1.22

My reasoning for the above:

**Revenue growth** , like PE ratio, is another way to measure growth vs value stocks. Neutralising on revenue growth addresses this imbalance between growth and value stocks.

**Accounts Receivable Turnover (ART)** : This metric measures how efficiently a company collects revenue from its customers. High dividend yield stocks might show more consistent operational efficiency due to their mature business models and focus on maintaining stable cash flows. Neutralising on ART addresses this imbalance.

---

### 评论 #7 (作者: AG20578, 时间: 2年前)

Thank you for the update!

My primary concern is that only 20% of the universe is covered. Could you aim to increase this to 50%? Here are two suggestions:

1. Simulate alpha on a smaller universe.
2. Apply coverage filling techniques, such as group_backfill to the whole alpha

---

### 评论 #8 (作者: AG20578, 时间: 2年前)

Can you please also share the Average Size by Capitalization visualization chart?

---

### 评论 #9 (作者: OG25133, 时间: 2年前)

Thanks for the advice - I'll do these three things and get back to you

---

### 评论 #10 (作者: SB17086, 时间: 1年前)

Thanks for the advice.

---

### 评论 #11 (作者: XD81759, 时间: 1年前)

Hey, nice alpha idea there! One potential weakness could be relying too much on that specific default probability ratio change. Market conditions might impact it in unexpected ways. Also, using ChatGPT for suggesting interacting fields might not fully capture real market complexities. And just basing on lower dividend yield for the second iteration might miss other factors that truly reflect a stock's undervaluation or market recognition. Maybe testing with more diverse datasets and considering other financial metrics could improve it.

---

### 评论 #12 (作者: XL31477, 时间: 1年前)

**Hey Olly,  [XD81759](/hc/en-us/profiles/23494746482967-XD81759)  makes some good points. Yeah, relying solely on that default probability ratio change is risky as market shifts can mess it up. And ChatGPT suggestions might not cover all real-world market nuances. Also, just focusing on lower dividend yield indeed might overlook other undervaluation signs. I'd suggest exploring more financial metrics like debt-to-equity ratio or free cash flow. Plus, testing across various datasets from different time periods and regions could make the alpha more robust.**

---

### 评论 #13 (作者: BA51127, 时间: 1年前)

This discussion highlights the importance of diversification and considering multiple financial metrics when developing an alpha strategy. It also underscores the potential limitations of relying on a single data point or external suggestions without thorough market analysis. Exploring additional datasets and financial indicators could indeed enhance the robustness and applicability of the alpha idea.

---

### 评论 #14 (作者: 顾问 CC40930 (Rank 95), 时间: 1年前)

This alpha strategy seems promising by leveraging credit quality improvements to identify undervalued stocks. I like how you’re using the historical default probability and considering the dividend yield as a signal for undervaluation. It would be interesting to see how the model performs when factoring in market sentiment, as credit health can sometimes be priced in slowly. Additionally, it might be worth looking into sector-specific risks, as they can influence the credit quality improvements of companies. Overall, great approach, and I’m curious to see how it evolves!

---

### 评论 #15 (作者: 顾问 ZH78994 (Rank 11), 时间: 1年前)

Thank you so much for sharing your incredible work with us! Your writing not only showcases your talent but also offers valuable insights and inspiration. I truly appreciate the time and effort you’ve put into creating something so thoughtful and meaningful. It’s clear that you have a gift for storytelling, and your work has left a lasting impression on me. Please keep sharing your wonderful creations—I’m already looking forward to your next piece! Thank you again for your generosity and dedication.

---

### 评论 #16 (作者: AK98027, 时间: 1年前)

This alpha strategy seems promising by leveraging credit quality improvements to identify undervalued stocks. I like how you’re using the historical default probability and considering the dividend yield as a signal for undervaluation. It would be interesting to see how the model performs when factoring in market sentiment, as credit health can sometimes be priced in slowly.

---

### 评论 #17 (作者: KS69567, 时间: 1年前)

Your alpha concept is much appreciated. Regarding the universe and location where this alpha is used, could you please elaborate?

---

