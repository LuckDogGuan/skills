# 顾问 AM60509 (Rank 61) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 AM60509 (Rank 61) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: A Practical Framework for Building and Optimizing Alpha Signals)
- **原帖链接**: [Commented] A Practical Framework for Building and Optimizing Alpha Signals.md
- **时间**: 1年前

**提问/主帖背景 (VP21767)**:
**Hello everyone,**

Many of you have shared your approaches to building alpha, but for new consultants, it can still feel quite challenging. In this post, I’d like to share the process I’ve been using to create alpha.

### **1. Simulate Raw Data**

The first step is to simulate raw data instead of collecting real-world data.

**Objective:**  Create a standardized dataset that accurately reflects the structure and characteristics of the financial market to serve as input for alpha development.

**Method:**

- Use simulation tools or historical data as sources to generate price and trading volume data.
- Include basic components such as opening price (open), highest price (high), lowest price (low), closing price (close), and trading volume (volume).

### **2. Build Alpha Signals Using Mathematical Operators**

From raw data, alpha signals are generated using quantitative operations:

**Steps:**

- Utilize basic operators from a list, such as  `log_diff` ,  `abs` ,  `nan_out` ,  `max` ,  `min` , or  `multiply` , to transform raw data into signals.
- Combine nonlinear functions like  `exp` ,  `log` , or conditional logic ( `cond ? expr1 : expr2` ) to create more complex and market-appropriate signals.

**Example:**

- `alpha_1 = log_diff(close)`
- `alpha_2 = max(high, low)`
- `alpha_3 = multiply(log_diff(close), log_diff(volume))`

### **3. Inner Correlation Testing**

Once the alpha signals are built, conduct an inner correlation test to eliminate redundant signals.

**Implementation:**

- Use the  **inner correlation index**  (pre-calculated in the alpha list) to evaluate the degree of correlation between alpha signals.
- Remove redundant or overlapping signals with a correlation higher than 0.7.

**Principles:**

- Retain complex or effective alpha signals.
- Remove simple signals, such as raw data ( `log_diff` ,  `abs` , etc.), if they don’t provide additional value.

### **4. Combine Alpha Signals to Create New Signals**

After filtering the alpha signals, I combine the remaining ones using basic mathematical operations to create new alpha signals.

**Basic Operations:**

- **Addition (+):**  Aggregating signals.
- **Subtraction (-):**  Analyzing differences.
- **Multiplication (*):**  Amplifying signals.
- **Division (/):**  Calculating ratios.

This combination process helps uncover more complex relationships between signals and enhances predictive value.

### **Benefits of This Process**

1. **Signal Optimization:**  Reduces redundancy and focuses on independent, effective signals.
2. **Improved Predictive Value:**  Combining alpha signals generates stronger and more flexible predictive signals.
3. **Increased Submission Count:**  By creating new alpha signals through the combination of existing ones, the number of alpha submissions increases significantly while maintaining low redundancy.
4. **Systematic Process:**  A clear, repeatable, and scalable process that can adapt to new market conditions.

This framework ensures that the final alpha portfolio is both streamlined and highly independent, optimizing the quality and quantity of signals, thereby enhancing effectiveness in financial markets.

👉  **If you find this post helpful, please like, share, and follow this post. Don’t hesitate to leave a comment below so we can exchange more ideas about useful frameworks for Alpha research!**

**顾问 AM60509 (Rank 61) 的解答与建议**:
The goal here is to generate a  **standardized dataset**  that mimics the structure and behavior of financial market data, without relying on real-world data.As you improve your alpha strategies, consider focusing on risk management techniques. Strategies like  **drawdown control** ,  **risk parity** , and  **volatility targeting**  can be vital in ensuring that your strategies perform well in different market conditions.


---

### 技术对话片段 2 (原帖: A Practical Framework for Building and Optimizing Alpha Signals)
- **原帖链接**: https://support.worldquantbrain.com[Commented] A Practical Framework for Building and Optimizing Alpha Signals_29271577776791.md
- **时间**: 1年前

**提问/主帖背景 (VP21767)**:
**Hello everyone,**

Many of you have shared your approaches to building alpha, but for new consultants, it can still feel quite challenging. In this post, I’d like to share the process I’ve been using to create alpha.

### **1. Simulate Raw Data**

The first step is to simulate raw data instead of collecting real-world data.

**Objective:**  Create a standardized dataset that accurately reflects the structure and characteristics of the financial market to serve as input for alpha development.

**Method:**

- Use simulation tools or historical data as sources to generate price and trading volume data.
- Include basic components such as opening price (open), highest price (high), lowest price (low), closing price (close), and trading volume (volume).

### **2. Build Alpha Signals Using Mathematical Operators**

From raw data, alpha signals are generated using quantitative operations:

**Steps:**

- Utilize basic operators from a list, such as  `log_diff` ,  `abs` ,  `nan_out` ,  `max` ,  `min` , or  `multiply` , to transform raw data into signals.
- Combine nonlinear functions like  `exp` ,  `log` , or conditional logic ( `cond ? expr1 : expr2` ) to create more complex and market-appropriate signals.

**Example:**

- `alpha_1 = log_diff(close)`
- `alpha_2 = max(high, low)`
- `alpha_3 = multiply(log_diff(close), log_diff(volume))`

### **3. Inner Correlation Testing**

Once the alpha signals are built, conduct an inner correlation test to eliminate redundant signals.

**Implementation:**

- Use the  **inner correlation index**  (pre-calculated in the alpha list) to evaluate the degree of correlation between alpha signals.
- Remove redundant or overlapping signals with a correlation higher than 0.7.

**Principles:**

- Retain complex or effective alpha signals.
- Remove simple signals, such as raw data ( `log_diff` ,  `abs` , etc.), if they don’t provide additional value.

### **4. Combine Alpha Signals to Create New Signals**

After filtering the alpha signals, I combine the remaining ones using basic mathematical operations to create new alpha signals.

**Basic Operations:**

- **Addition (+):**  Aggregating signals.
- **Subtraction (-):**  Analyzing differences.
- **Multiplication (*):**  Amplifying signals.
- **Division (/):**  Calculating ratios.

This combination process helps uncover more complex relationships between signals and enhances predictive value.

### **Benefits of This Process**

1. **Signal Optimization:**  Reduces redundancy and focuses on independent, effective signals.
2. **Improved Predictive Value:**  Combining alpha signals generates stronger and more flexible predictive signals.
3. **Increased Submission Count:**  By creating new alpha signals through the combination of existing ones, the number of alpha submissions increases significantly while maintaining low redundancy.
4. **Systematic Process:**  A clear, repeatable, and scalable process that can adapt to new market conditions.

This framework ensures that the final alpha portfolio is both streamlined and highly independent, optimizing the quality and quantity of signals, thereby enhancing effectiveness in financial markets.

👉  **If you find this post helpful, please like, share, and follow this post. Don’t hesitate to leave a comment below so we can exchange more ideas about useful frameworks for Alpha research!**

**顾问 AM60509 (Rank 61) 的解答与建议**:
The goal here is to generate a  **standardized dataset**  that mimics the structure and behavior of financial market data, without relying on real-world data.As you improve your alpha strategies, consider focusing on risk management techniques. Strategies like  **drawdown control** ,  **risk parity** , and  **volatility targeting**  can be vital in ensuring that your strategies perform well in different market conditions.


---

### 技术对话片段 3 (原帖: Advise needed for Boosters)
- **原帖链接**: [Commented] Advise needed for Boosters.md
- **时间**: 1年前

**提问/主帖背景 (SD99406)**:
Hello Consultants,

I would like to ask that I have read that use booster and also in webinars also our mentor used booster. So my question is that is there any criteria for booster meaning that PnL gaph should be increasing, specific levels of Sharpe and Fitness or any other criteria.

How should I come to know that opeator(datafield) is a booster

**顾问 AM60509 (Rank 61) 的解答与建议**:
To determine if a data field (operator) can act as a booster, you should consider the following steps:

**1.Test the alpha with and without the operator**

**2.Analyze the relevance of the data field**

**3.Ensure no overfitting**

**Keep the return/ drawdown ratio as high as possible,**

**Focus on   Return/Drawdown ratio >2 for sustainable results**


---

### 技术对话片段 4 (原帖: Advise needed for Boosters)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Advise needed for Boosters_29286699135767.md
- **时间**: 1年前

**提问/主帖背景 (SD99406)**:
Hello Consultants,

I would like to ask that I have read that use booster and also in webinars also our mentor used booster. So my question is that is there any criteria for booster meaning that PnL gaph should be increasing, specific levels of Sharpe and Fitness or any other criteria.

How should I come to know that opeator(datafield) is a booster

**顾问 AM60509 (Rank 61) 的解答与建议**:
To determine if a data field (operator) can act as a booster, you should consider the following steps:

**1.Test the alpha with and without the operator**

**2.Analyze the relevance of the data field**

**3.Ensure no overfitting**

**Keep the return/ drawdown ratio as high as possible,**

**Focus on   Return/Drawdown ratio >2 for sustainable results**


---

### 技术对话片段 5 (原帖: ATOM AMA 2024 - Ask me Anything被推荐的)
- **原帖链接**: [Commented] ATOM AMA 2024 - Ask me Anything被推荐的.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Hi everyone,

We are hosting an AMA (Ask Me Anything) session on the BRAIN forum for the ATOM competition. This is an opportunity for you to ask any questions you may have about the competition, and for our expert team to anything on your mind.

We understand that the competition can be challenging, and we want to ensure that you have the information and support you need to succeed.

Ask away!

**顾问 AM60509 (Rank 61) 的解答与建议**:
how to create alphas on GLB region using ESG factors?What operators can be used?


---

### 技术对话片段 6 (原帖: ATOM AMA 2024 - Ask me Anything被推荐的)
- **原帖链接**: [Commented] ATOM AMA 2024 - Ask me Anything被推荐的.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Hi everyone,

We are hosting an AMA (Ask Me Anything) session on the BRAIN forum for the ATOM competition. This is an opportunity for you to ask any questions you may have about the competition, and for our expert team to anything on your mind.

We understand that the competition can be challenging, and we want to ensure that you have the information and support you need to succeed.

Ask away!

**顾问 AM60509 (Rank 61) 的解答与建议**:
how to check weekly rank in atom competition?


---

### 技术对话片段 7 (原帖: ATOM AMA 2024 - Ask me Anything被推荐的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] ATOM AMA 2024 - Ask me Anything被推荐的_26942011289751.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Hi everyone,

We are hosting an AMA (Ask Me Anything) session on the BRAIN forum for the ATOM competition. This is an opportunity for you to ask any questions you may have about the competition, and for our expert team to anything on your mind.

We understand that the competition can be challenging, and we want to ensure that you have the information and support you need to succeed.

Ask away!

**顾问 AM60509 (Rank 61) 的解答与建议**:
how to create alphas on GLB region using ESG factors?What operators can be used?


---

### 技术对话片段 8 (原帖: ATOM AMA 2024 - Ask me Anything被推荐的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] ATOM AMA 2024 - Ask me Anything被推荐的_26942011289751.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Hi everyone,

We are hosting an AMA (Ask Me Anything) session on the BRAIN forum for the ATOM competition. This is an opportunity for you to ask any questions you may have about the competition, and for our expert team to anything on your mind.

We understand that the competition can be challenging, and we want to ensure that you have the information and support you need to succeed.

Ask away!

**顾问 AM60509 (Rank 61) 的解答与建议**:
how to check weekly rank in atom competition?


---

### 技术对话片段 9 (原帖: BRAIN Genius: Improving Combined Alpha Performance被推荐的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] BRAIN Genius Improving Combined Alpha Performance被推荐的_27758121327639.md
- **时间**: 1年前

**提问/主帖背景 (Aziz Ansari)**:
[Combined Alpha Performance](/hc/en-us/articles/26715994416535-What-is-Combined-Alpha-Performance)  is an important eligibility criterion for achieving higher tiers in the BRAIN Genius Program. In this post, let’s explore potential ways of improving this score.


> [!NOTE] [图片 OCR 识别内容]
> How does correlation affect Combined Alpha Performance?
> Based on modern
> portfolio theory, along with some assumptions, the combined Sharpe Of yoUT
> submitted Alphas can be approximated as:
> S
> Here
> 5is Sharpe Of combined Alphas
> Sais average Sharpe Of submitted Alphas
> is number of submitted Alphas,and
> is average pair-wise correlation af submitted Alphas
> Case 1: Let's consider a Case Where
> ~ 0, thatis, uncorrelated Alphas are submitted
> Substitutingthe value of
> in the equation gives
> favourable outcome:
> ViSa
> This is helpful as SubmittingWgreWncorrelated Alphas Improyes the combined Nlphaperformance:
> Case 2: Let's consider a Case Where
> that is, highly correlated Alphas are submitted
> Substitutingthe value of
> in the above equation; gives the
> following Sharpe Of combined Alpha:


This implies that submitting highly correlated Alphas keeps combined Sharpe closer to average Sharpe of the Alphas.


> [!NOTE] [图片 OCR 识别内容]
> Actionable tips to potentially improve Combined Alpha
> Performance
> Increasing average Sharpe 5:


- To enhance the combined performance, it’s important to focus on the OS (Out-of-Sample) Sharpe ratio of the submitted Alphas. Overfitting during the IS period can lead to misleading performance metrics, which don’t generalize well to new data
- Overfitting can be limited by leveraging the  [Test period]([L2] [BRAIN TIPS] How can I use the test period to improve the OS performance of my Alpha_22205077935895.md)  feature, conducting  [Robustness Tests]([L2] Robustness Test_25238340364695.md) , and keeping your Alpha expressions explainable.


> [!NOTE] [图片 OCR 识别内容]
> Decrease inner correlation acro5s Alphas


- Adding noise to an Alpha to try to achieve lower correlation is often ineffective, as all Alphas may still have poor performance simultaneously in the OS period if the underlying signal degrades
- Instead of relying on noise to reduce correlation, focus on  [achieving orthogonality]([L2] [BRAIN TIPS] How do you reduce correlation of a good alpha_8046468280727.md)  through innovative use of operators and diverse datasets, ensuring that signals remain distinct and robust
- Submitting uncorrelated Alphas in different pyramids is also essential for building a robust Alpha pool, ensuring resilience to drawdowns in any single pyramid

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thanks for the information. There are two ways to increase combined alpha performance

1.Increase average Sharpe

2.Decrease correlation across alphas

Avoiding overfitting and focusing on Out-of-Sample (OS) Sharpe ratios is crucial for achieving sustainable Alpha performance.

@ [AS34048](/hc/en-us/profiles/5633388217879-AS34048) 
Each pyramid counts has equal value as far as qualifying criteria for Genius Level is concerned. However, each pyramid has a different multiplier ,so your base payments might differ


---

### 技术对话片段 10 (原帖: Can I use Trade_when to decease the Turnover?)
- **原帖链接**: [Commented] Can I use Trade_when to decease the Turnover.md
- **时间**: 1年前

**提问/主帖背景 (TL67839)**:
In my understanding, The Turnover is too high means the trading frequency is too high. So, I want to set some limitations for my alpha and don't allow it to trade at any time.

For example, my original alpha is:

```
Hello World.
```

And then, my new alpha is:

```
triggerTradeExp = (rank(volume) > 0.5)AlphaExp= Hello World.triggerExitExp = (rank(volume) <= 0.5)trade_when(triggerTradeExp, AlphaExp, triggerExitExp)
```

I thought this would reduce the trading frequency and reduce the Turnover, but it didn't. Sometimes, it even increased the turnover. I don't know what is the problem. Does anyone know this?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Yes, Trade_When can be used to reduce turnover. It only executes if condition is true and in other cases the alpha remains the same,no new assignment occurs.


---

### 技术对话片段 11 (原帖: Can I use Trade_when to decease the Turnover?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Can I use Trade_when to decease the Turnover_27675353441431.md
- **时间**: 1 year ago

**提问/主帖背景 (TL67839)**:
In my understanding, The Turnover is too high means the trading frequency is too high. So, I want to set some limitations for my alpha and don't allow it to trade at any time.

For example, my original alpha is:

```
Hello World.
```

And then, my new alpha is:

```
triggerTradeExp = (rank(volume) > 0.5)AlphaExp= Hello World.triggerExitExp = (rank(volume) <= 0.5)trade_when(triggerTradeExp, AlphaExp, triggerExitExp)
```

I thought this would reduce the trading frequency and reduce the Turnover, but it didn't. Sometimes, it even increased the turnover. I don't know what is the problem. Does anyone know this?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Yes, Trade_When can be used to reduce turnover. It only executes if condition is true and in other cases the alpha remains the same,no new assignment occurs.


---

### 技术对话片段 12 (原帖: Apply trade_when for Entry and Exit)
- **原帖链接**: [Commented] Can you use multiple trade_when operators.md
- **时间**: 1年前

**提问/主帖背景 (IH10395)**:
Just a simple example I won't actually use. Let's say I decide to go long when volume is above average:

trade_when(volume>adv20, 1, -1)

And go short where the close is lower than the open:

trade_when(close<open, -1, -1)

It doesn't seem to me the second expression has any effect. How do I do this?

**顾问 AM60509 (Rank 61) 的解答与建议**:
You can use multiple  `trade_when`  operators to structure complex strategies with different trade conditions for entry and exit. For instance, separate  `trade_when`  operators can handle long and short signals or combined entry conditions using logical operators like  `and`  or  `or` . Ensure logical consistency to avoid conflicts, such as simultaneous opposing signals or inefficient execution. I would suggest not using multiple trade_when as it might result in overfitting


---

### 技术对话片段 13 (原帖: Apply trade_when for Entry and Exit)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Can you use multiple trade_when operators_23832489212055.md
- **时间**: 1年前

**提问/主帖背景 (IH10395)**:
Just a simple example I won't actually use. Let's say I decide to go long when volume is above average:

trade_when(volume>adv20, 1, -1)

And go short where the close is lower than the open:

trade_when(close<open, -1, -1)

It doesn't seem to me the second expression has any effect. How do I do this?

**顾问 AM60509 (Rank 61) 的解答与建议**:
You can use multiple  `trade_when`  operators to structure complex strategies with different trade conditions for entry and exit. For instance, separate  `trade_when`  operators can handle long and short signals or combined entry conditions using logical operators like  `and`  or  `or` . Ensure logical consistency to avoid conflicts, such as simultaneous opposing signals or inefficient execution. I would suggest not using multiple trade_when as it might result in overfitting


---

### 技术对话片段 14 (原帖: COMING UP WITH LOW TURNOVER ALPHAS)
- **原帖链接**: [Commented] COMING UP WITH LOW TURNOVER ALPHAS.md
- **时间**: 1年前

**提问/主帖背景 (FM59649)**:
Here are some structured ideas for crafting low-turnover alphas:

### **1. Valuation-Based Alpha**

**Concept:** 
Stocks with attractive valuation metrics tend to outperform over the long term.

#### Steps:

1. **Inputs:**  Use fundamental data such as price-to-earnings (P/E), price-to-book (P/B), EV/EBITDA, and maybe Earnings per share ratios.
2. **Signal Construction:**  Rank stocks based on the inverse of these metrics (lower is better).For instance,            ValuationSignal = −P/E Ratio
3. You can try to use a multi-quarter average of the valuation metric to smooth out anomalies.

### **2. Earnings Growth Consistency**

**Concept:** 
Companies with consistent earnings growth often sustain their performance over time.

#### Steps:

1. **Inputs:**  Use quarterly EPS (earnings per share) growth data.
2. **Signal Construction:**  Calculate the standard deviation of EPS growth over the past few quarters. Rank stocks based on lower standard deviations. GrowthStabilitySignal = −StdDev(EPSGrowth)
3. **Combine:**  Add a filter for stocks with positive earnings growth to exclude declining performers.

Stable earnings growth often translates into predictable stock returns, reducing the need for frequent rebalancing.

### **3. Dividend Yield Stability**

**Concept:** 
Stocks with stable or growing dividends tend to attract long-term investors, creating consistent price support.

#### Steps:

1. **Inputs:**  Use dividend yield and dividend payout ratios.
2. **Signal Construction:**  Rank stocks based on dividend yield, adjusted for payout ratio stability. DividendSignal = DividendYield×(1−StdDev(PayoutRatio))
3. **Sector Neutrality:**  Adjust for sector biases, as dividend yields vary significantly across industries.

### **4. Long-Term Momentum**

**Concept:** 
Stocks with strong performance over long horizons (e.g., 12 months) often continue to perform well.

#### Steps:

1. **Inputs:**  Use 12-month price returns, excluding the most recent month to avoid short-term reversals.
2. **Signal Construction:**  LongTermMomentum=(Price(t​)−Price(t−12M​))/Price(t−12M​​)
3. **Normalization:**  Normalize across the universe to ensure comparability.

Momentum signals based on longer horizons require less frequent rebalancing, inherently lowering turnover.

### **5. Capital Efficiency**

**Concept:** 
Firms that efficiently utilize capital for growth are rewarded over the long term.

#### Steps:

1. **Inputs:**  Use ROIC (Return on Invested Capital) and WACC (Weighted Average Cost of Capital).
2. **Signal Construction:**  EfficiencySignal=ROIC−WACC

Capital-efficient companies exhibit enduring advantages, reducing the need for frequent adjustments.

### **General Best Practices for Low Turnover Alphas**

1. **Long Lookback Windows:**  Use longer periods (e.g., 1–3 years) for data calculations to reduce signal volatility.
2. **Signal Smoothing:**  Apply exponential moving averages (EMAs) or rolling averages to smooth noisy signals.
3. **Cross-Sectional Neutralization:**  Rank signals across the universe to avoid drastic changes due to market-wide movements.
4. **Transaction Cost Analysis:**  Optimize rebalancing frequency by balancing predictive power against trading costs.
5. **Risk Management:**  Neutralize market, sector, and also try risk-based neutralization factors like slow,fast, and slow and fast factors

Creating low-turnover alphas requires designing signals that emphasize stable, persistent patterns rather than short-term fluctuations.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing your ideas.Use of trade_when operator with a suitable condition can help reduce turnover.In addition to this,using ts_target_tvr_hump operator can help reduce turnover and create low turnover alphas.


---

### 技术对话片段 15 (原帖: COMING UP WITH LOW TURNOVER ALPHAS)
- **原帖链接**: https://support.worldquantbrain.com[Commented] COMING UP WITH LOW TURNOVER ALPHAS_29456089587095.md
- **时间**: 1年前

**提问/主帖背景 (FM59649)**:
Here are some structured ideas for crafting low-turnover alphas:

### **1. Valuation-Based Alpha**

**Concept:** 
Stocks with attractive valuation metrics tend to outperform over the long term.

#### Steps:

1. **Inputs:**  Use fundamental data such as price-to-earnings (P/E), price-to-book (P/B), EV/EBITDA, and maybe Earnings per share ratios.
2. **Signal Construction:**  Rank stocks based on the inverse of these metrics (lower is better).For instance,            ValuationSignal = −P/E Ratio
3. You can try to use a multi-quarter average of the valuation metric to smooth out anomalies.

### **2. Earnings Growth Consistency**

**Concept:** 
Companies with consistent earnings growth often sustain their performance over time.

#### Steps:

1. **Inputs:**  Use quarterly EPS (earnings per share) growth data.
2. **Signal Construction:**  Calculate the standard deviation of EPS growth over the past few quarters. Rank stocks based on lower standard deviations. GrowthStabilitySignal = −StdDev(EPSGrowth)
3. **Combine:**  Add a filter for stocks with positive earnings growth to exclude declining performers.

Stable earnings growth often translates into predictable stock returns, reducing the need for frequent rebalancing.

### **3. Dividend Yield Stability**

**Concept:** 
Stocks with stable or growing dividends tend to attract long-term investors, creating consistent price support.

#### Steps:

1. **Inputs:**  Use dividend yield and dividend payout ratios.
2. **Signal Construction:**  Rank stocks based on dividend yield, adjusted for payout ratio stability. DividendSignal = DividendYield×(1−StdDev(PayoutRatio))
3. **Sector Neutrality:**  Adjust for sector biases, as dividend yields vary significantly across industries.

### **4. Long-Term Momentum**

**Concept:** 
Stocks with strong performance over long horizons (e.g., 12 months) often continue to perform well.

#### Steps:

1. **Inputs:**  Use 12-month price returns, excluding the most recent month to avoid short-term reversals.
2. **Signal Construction:**  LongTermMomentum=(Price(t​)−Price(t−12M​))/Price(t−12M​​)
3. **Normalization:**  Normalize across the universe to ensure comparability.

Momentum signals based on longer horizons require less frequent rebalancing, inherently lowering turnover.

### **5. Capital Efficiency**

**Concept:** 
Firms that efficiently utilize capital for growth are rewarded over the long term.

#### Steps:

1. **Inputs:**  Use ROIC (Return on Invested Capital) and WACC (Weighted Average Cost of Capital).
2. **Signal Construction:**  EfficiencySignal=ROIC−WACC

Capital-efficient companies exhibit enduring advantages, reducing the need for frequent adjustments.

### **General Best Practices for Low Turnover Alphas**

1. **Long Lookback Windows:**  Use longer periods (e.g., 1–3 years) for data calculations to reduce signal volatility.
2. **Signal Smoothing:**  Apply exponential moving averages (EMAs) or rolling averages to smooth noisy signals.
3. **Cross-Sectional Neutralization:**  Rank signals across the universe to avoid drastic changes due to market-wide movements.
4. **Transaction Cost Analysis:**  Optimize rebalancing frequency by balancing predictive power against trading costs.
5. **Risk Management:**  Neutralize market, sector, and also try risk-based neutralization factors like slow,fast, and slow and fast factors

Creating low-turnover alphas requires designing signals that emphasize stable, persistent patterns rather than short-term fluctuations.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing your ideas.Use of trade_when operator with a suitable condition can help reduce turnover.In addition to this,using ts_target_tvr_hump operator can help reduce turnover and create low turnover alphas.


---

### 技术对话片段 16 (原帖: Congratulations to our Global ATOM winners!)
- **原帖链接**: [Commented] Congratulations to our Global ATOM winners.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:
[图片 (图片已丢失)]

**顾问 AM60509 (Rank 61) 的解答与建议**:
Congratulations to all the winners of the Global ATOM competition!  Your hard work and dedication have  paid off. Thank you, WorldQuant BRAIN, for organizing such a great platform for learning and growth.


---

### 技术对话片段 17 (原帖: Congratulations to our Global ATOM winners!)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Congratulations to our Global ATOM winners_28386256322967.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:

> [!NOTE] [图片 OCR 识别内容]
> NTOM
> 2024
> TOP 10 WINNERS
> 1st
> 器
> Yuqi Liu
> 2nd
> Thanh Nguyen
> Sra
> Ritesh Palawat
> 4th
> Dat Nguyen
> Sth
> Wenqian Dai
> Lingyu Zhang
> Ajay Bagul
> SaadKhan
> Leich Mugoh
> 1Oth
> Kuan Hung Kuo
> CONGRATULATIONS!
> ERAN


**顾问 AM60509 (Rank 61) 的解答与建议**:
Congratulations to all the winners of the Global ATOM competition!  Your hard work and dedication have  paid off. Thank you, WorldQuant BRAIN, for organizing such a great platform for learning and growth.


---

### 技术对话片段 18 (原帖: Curious Case of Genius Levels: How Performance Metrics Align with Promotion Thresholds)
- **原帖链接**: [Commented] Curious Case of Genius Levels How Performance Metrics Align with Promotion Thresholds.md
- **时间**: 1年前

**提问/主帖背景 (MG52134)**:
As we gear up for the next quarter, the system of determining Genius Levels has sparked some interesting questions about performance, thresholds, and career progression. Here's a quick breakdown:

The Genius Levels are distributed as follows:

- **2% Grand Master (GM)**
- **8% Master**
- **20% Expert**
- **70% Gold**

A unique aspect of this system is the stability it offers:

- If a consultant underperforms in a given quarter, their level only degrades after being in the same category for  **two consecutive quarters** .

But here's where curiosity kicks in:
What happens when a  **Gold member outperforms expectations and makes it to the top 2% in a quarter** ?

In theory, their performance qualifies them for a  **Grand Master**  promotion. However, the 2% GM threshold might already be met by existing members, meaning no immediate promotion can occur. Similarly, a GM-level consultant performing poorly in Q1 2025 won't immediately lose their spot unless they fail to meet expectations for two consecutive quarters.

This creates a dynamic where performance doesn’t always guarantee immediate progression, highlighting the balance between opportunity and system stability.

It’s a fascinating structure that rewards consistency and ensures fair competition while also keeping the stakes high. What are your thoughts on this approach? Does it encourage sustained excellence, or could it be more flexible for extraordinary performances?

Let’s discuss!

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for raising this point. Reshuffling occurs after each quarter, so even if you reached Grand Master (GM) last quarter, you could drop to Gold the next.

Users who have been simulating alphas for a long time have an edge on some of the tie breaker criteria like simulation streak which can be seen in the case of the top performers from vietnam which have simulation streak ranging from few hundreds to over 1000 days


---

### 技术对话片段 19 (原帖: Curious Case of Genius Levels: How Performance Metrics Align with Promotion Thresholds)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Curious Case of Genius Levels How Performance Metrics Align with Promotion Thresholds_29279520798999.md
- **时间**: 1年前

**提问/主帖背景 (MG52134)**:
As we gear up for the next quarter, the system of determining Genius Levels has sparked some interesting questions about performance, thresholds, and career progression. Here's a quick breakdown:

The Genius Levels are distributed as follows:

- **2% Grand Master (GM)**
- **8% Master**
- **20% Expert**
- **70% Gold**

A unique aspect of this system is the stability it offers:

- If a consultant underperforms in a given quarter, their level only degrades after being in the same category for  **two consecutive quarters** .

But here's where curiosity kicks in:
What happens when a  **Gold member outperforms expectations and makes it to the top 2% in a quarter** ?

In theory, their performance qualifies them for a  **Grand Master**  promotion. However, the 2% GM threshold might already be met by existing members, meaning no immediate promotion can occur. Similarly, a GM-level consultant performing poorly in Q1 2025 won't immediately lose their spot unless they fail to meet expectations for two consecutive quarters.

This creates a dynamic where performance doesn’t always guarantee immediate progression, highlighting the balance between opportunity and system stability.

It’s a fascinating structure that rewards consistency and ensures fair competition while also keeping the stakes high. What are your thoughts on this approach? Does it encourage sustained excellence, or could it be more flexible for extraordinary performances?

Let’s discuss!

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for raising this point. Reshuffling occurs after each quarter, so even if you reached Grand Master (GM) last quarter, you could drop to Gold the next.

Users who have been simulating alphas for a long time have an edge on some of the tie breaker criteria like simulation streak which can be seen in the case of the top performers from vietnam which have simulation streak ranging from few hundreds to over 1000 days


---

### 技术对话片段 20 (原帖: Dataset Deepdives - News87 (Smart Conference call transcript data)被推荐的Research)
- **原帖链接**: [Commented] Dataset Deepdives - News87 Smart Conference call transcript data被推荐的Research.md
- **时间**: 1年前

**提问/主帖背景 (AC28031)**:
Conference calls, also known as analyst/earnings calls, are significant events for public companies and investors to discuss in detail the firm’s fiscal quarter, as well as projected financial performance and future business insights. Thus, these events may contain impactful information related to the firm’s stock price such as new information, sentiment, surprise, reaction, etc.

This article will discuss potentially unique Alphas using "News87" dataset named “Smart Conference Call Transcript Data” for Global region.

**Dataset Highlight**

- The "News87" dataset is classified under the Analyst category > Analyst Estimate subcategory.
- Data Type: VECTOR type only
- Regions: USA D-1 & D-0. GLB D-1
- At the time of writing, "News87" is quite under-explored by the consultant community in GLB region compared to Analyst category in general (table below). This makes "News87" potential source for creating low-correlation Alphas. Info on GLB Alphas in the dataset at the time of publishing:

[图片 (图片已丢失)]

- The ideas discussed below can be used to create Alphas in both USA and GLB Regions. It is encouraged for consultants to submit Alphas especially in GLB Region for this dataset.

**Dataset Feature**

1. **Low frequency, low coverage.**  Conference calls aren't mandatory, but most public companies hold them, usually within one month after the completion of the quarter, following the quarterly earnings announcement. Thus, a quarterly frequency is typically observed, and at least a 63-day backfill is recommended.
2. **Participants and Sections concepts.** Given the conference calls' nature in business presentations & discussions, there are various objects regarding the call participants and presentation sections that are seen across the "News87" dataset.
3. **Structured into three statistical groups: Basic Stats, Readability Score, and Sentiment Score.**  These metrics are extracted from calls that are recorded and broadcasted live on the internet. Vendors transcribe the calls into written text for investors to consume, and advanced measurement such as NLP algorithm are applied to derive various statistics.

1. Basic Stats:General basic count and its derived values of information including:

*Ex: "mws87_numvswordsratioceoqa" is the Number of numerical words divided by number of all words spoken by CEO in Q&A*

1. Readability Score:There are many numeric test indices, calculated from the number of characters, words, sentences, etc... from textual transcript, indicating linguistic complexity across Participants and Sections. The values of these data ranging from 0 to 100 and specific test indices provided by "News87 dataset are listed below:

*Ex: "mws87_oper_fre_qa" is The Flesch Reading Ease score of the operator in Q&A*

1. Sentiment Score:for various Participants under different Sections.

*Ex: "mws87_corppart_sent_score_qa: is The sentiment score of corporate participants in Q&A*

**Usage Advice**

1. Check coverage, as different fields within the dataset may vary given their economic implications. For example, analysts may seldom talk, or the CEO not attending the meeting may lead to lower coverage for certain fields.
2. It is always advisable to use ts_backfill() operator for all datafields in this dataset. Backfilling at least one or two quarters and removing outliers by winsorize, truncating, etc.., especially for sentiment data, are recommended.
3. Time series operators may be useful given the different base value of sentiment of different markets, companies and individuals.
4. Earnings conference data can serve as a long-term signal, similar to fundamental data as its contain sentiment, reaction, etc.. factors derived from latest business and financial discussion information.
5. Try applying this to different universes in the GLB region to achieve low correlation and maximize value scores.

- **Sample Alpha Ideas**

1. Tone and Sentiment: Conference call linguistic tone of the dialogue between management and analysts may predict abnormal returns. The below can be starting points:

See Papers:  [Earnings conference calls and stock returns: The incremental informativeness of textual tone]([链接已屏蔽])

1. Financial reporting readability: Consistent and low financial report readability impeding the efficient and accurate assimilation of information into stock prices, less understandable reporting are associated with greater equity mispricing and momentum effect.

See Papers:  [Annual report readability and equity mispricing]([链接已屏蔽])

**Alpha Performance and Correlation** Below is the performance of a Single Dataset Alpha idea implemented on this dataset in the GLB Region. 
High Margin with Low production correlation is easily achievable if one creates Alphas using this dataset.
 [图片 (图片已丢失)]

**Call for Action**

*Comment below if you found this post helpful and were able to submit at least one Alpha using this dataset* .

Feel free to ask any questions in case of any doubts! We also look forward to hearing if you would like similar notes on other datasets.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing such a comprehensive and insightful post on the "News87" dataset! This is really insightful and the ideas are amazing. The detailed breakdown of the 'News87' dataset and its potential applications for creating low-correlation Alphas in the GLB region is quite valuable.

[AC28031](/hc/en-us/profiles/10267557338007-AC28031) :Can you suggest a sample template for this dataset


---

### 技术对话片段 21 (原帖: Dataset Deepdives - News87 (Smart Conference call transcript data)被推荐的Research)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Dataset Deepdives - News87 Smart Conference call transcript data被推荐的Research_28234460258327.md
- **时间**: 1年前

**提问/主帖背景 (AC28031)**:
Conference calls, also known as analyst/earnings calls, are significant events for public companies and investors to discuss in detail the firm’s fiscal quarter, as well as projected financial performance and future business insights. Thus, these events may contain impactful information related to the firm’s stock price such as new information, sentiment, surprise, reaction, etc.

This article will discuss potentially unique Alphas using "News87" dataset named “Smart Conference Call Transcript Data” for Global region.

**Dataset Highlight**

- The "News87" dataset is classified under the Analyst category > Analyst Estimate subcategory.
- Data Type: VECTOR type only
- Regions: USA D-1 & D-0. GLB D-1
- At the time of writing, "News87" is quite under-explored by the consultant community in GLB region compared to Analyst category in general (table below). This makes "News87" potential source for creating low-correlation Alphas. Info on GLB Alphas in the dataset at the time of publishing:


> [!NOTE] [图片 OCR 识别内容]
> Dataset
> Users
> Alphas
> Fields
> Alphaluser
> Alphalfield
> GLB
> 39% coverage
> Value Score 5
> Neis87
> 44
> 138
> 201
> Analyst category (Average)
> 430
> 157


- The ideas discussed below can be used to create Alphas in both USA and GLB Regions. It is encouraged for consultants to submit Alphas especially in GLB Region for this dataset.

**Dataset Feature**

1. **Low frequency, low coverage.**  Conference calls aren't mandatory, but most public companies hold them, usually within one month after the completion of the quarter, following the quarterly earnings announcement. Thus, a quarterly frequency is typically observed, and at least a 63-day backfill is recommended.
2. **Participants and Sections concepts.** Given the conference calls' nature in business presentations & discussions, there are various objects regarding the call participants and presentation sections that are seen across the "News87" dataset.
3. **Structured into three statistical groups: Basic Stats, Readability Score, and Sentiment Score.**  These metrics are extracted from calls that are recorded and broadcasted live on the internet. Vendors transcribe the calls into written text for investors to consume, and advanced measurement such as NLP algorithm are applied to derive various statistics.

1. Basic Stats:General basic count and its derived values of information including:

*Ex: "mws87_numvswordsratioceoqa" is the Number of numerical words divided by number of all words spoken by CEO in Q&A*

1. Readability Score:There are many numeric test indices, calculated from the number of characters, words, sentences, etc... from textual transcript, indicating linguistic complexity across Participants and Sections. The values of these data ranging from 0 to 100 and specific test indices provided by "News87 dataset are listed below:

*Ex: "mws87_oper_fre_qa" is The Flesch Reading Ease score of the operator in Q&A*

1. Sentiment Score:for various Participants under different Sections.

*Ex: "mws87_corppart_sent_score_qa: is The sentiment score of corporate participants in Q&A*

**Usage Advice**

1. Check coverage, as different fields within the dataset may vary given their economic implications. For example, analysts may seldom talk, or the CEO not attending the meeting may lead to lower coverage for certain fields.
2. It is always advisable to use ts_backfill() operator for all datafields in this dataset. Backfilling at least one or two quarters and removing outliers by winsorize, truncating, etc.., especially for sentiment data, are recommended.
3. Time series operators may be useful given the different base value of sentiment of different markets, companies and individuals.
4. Earnings conference data can serve as a long-term signal, similar to fundamental data as its contain sentiment, reaction, etc.. factors derived from latest business and financial discussion information.
5. Try applying this to different universes in the GLB region to achieve low correlation and maximize value scores.

- **Sample Alpha Ideas**

1. Tone and Sentiment: Conference call linguistic tone of the dialogue between management and analysts may predict abnormal returns. The below can be starting points:

See Papers:  [Earnings conference calls and stock returns: The incremental informativeness of textual tone]([链接已屏蔽])

1. Financial reporting readability: Consistent and low financial report readability impeding the efficient and accurate assimilation of information into stock prices, less understandable reporting are associated with greater equity mispricing and momentum effect.

See Papers:  [Annual report readability and equity mispricing]([链接已屏蔽])

**Alpha Performance and Correlation** Below is the performance of a Single Dataset Alpha idea implemented on this dataset in the GLB Region. 
High Margin with Low production correlation is easily achievable if one creates Alphas using this dataset.
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Awerage
> Single Data Set Alpha
> Dyramid theme: GLBIDIIAnalyst *1.5
> Aggregate Data
> 31aroE
> UPICNe|
> FiznEss
> ECUTI
> UTaWOUF
> Warain
> 1.89
> 3.27%
> 1.07
> 4.0196
> 2.8296
> 24.549000
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Frness
> REIICn
> Oraroin
> Warain
> 1.58
> 3.2796
> 0.58
> 1.699
> 1.649
> 10.359600
>  Correlation
> Self Correlation
> Natirum
> Ninimum
> Last Run:
> Prod
> [sTIIT
> [inimUT
> Lt RMn:
> 12/03120245-09
> Correlation
> 0.3881
> -0.2380
> TU


**Call for Action**

*Comment below if you found this post helpful and were able to submit at least one Alpha using this dataset* .

Feel free to ask any questions in case of any doubts! We also look forward to hearing if you would like similar notes on other datasets.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing such a comprehensive and insightful post on the "News87" dataset! This is really insightful and the ideas are amazing. The detailed breakdown of the 'News87' dataset and its potential applications for creating low-correlation Alphas in the GLB region is quite valuable.

[AC28031](/hc/en-us/profiles/10267557338007-AC28031) :Can you suggest a sample template for this dataset


---

### 技术对话片段 22 (原帖: Dataset Deepdives - Option23 (Option Implied Volatility and Greeks)被推荐的)
- **原帖链接**: [Commented] Dataset Deepdives - Option23 Option Implied Volatility and Greeks被推荐的.md
- **时间**: 1年前

**提问/主帖背景 (AC28031)**:
Options are an excellent dataset for conducting  *HUMAN based research* . In this article, we will discuss various potential Alphas that can be generated using the ‘Options23’ dataset.

**Dataset Highlights:**

- The ‘Options23’ dataset has 1,936 data fields with both matrix and vector data types.
- The dataset is only available for the USA Region.
- At the time of writing, only 424 Alphas are submitted using this dataset, making it slightly unexplored by the consultant community.

**Introduction:**

Although creating Alphas with a HUMAN approach from a dataset with 2k data fields may seem daunting, it is almost always the case that if you take a closer look at the data, a well-structured approach for generating Alphas with clear hypothesis can be formulated.

As previously discussed, when conducting human-based research, it is crucial to step back and create organized notes on accessing the dataset to formulate logical and non-random hypotheses. This article is one such example of dataset notes for the ‘Options23’ dataset that can help in creating Alphas:

**DATASET NOTES:**

1. The dataset has options data like implied volatility, option greeks, strike prices, etc from  **5 DIFFERENT DATA SOURCES** . Thus one must ensure that while using comparison fields within the dataset, the datasource must ideally remain the same to have a fair comparison.

1. For the aforementioned data sources, the dataset includes both raw values and derived values of various options data. The derived values are primarily weighted averages of Implied Volatility and Option Greeks, using either of the following as weights across multiple data sources:
   1. Volume
   2. Open Interest
2. For the aforementioned data sources and weighted average values, the options data values are calculated at various levels of moneyness. The moneyness levels are highlighted based off a suffix in the datafield from 0 to 9. Below is the list of the options data available in the various order of moneyness levels as highlighted in the datafields:
   1. 0: all
   2. 1: near in and out
   3. 2: near out and in
   4. 3: out
   5. 4: near
   6. 5: in
   7. 6: far out
   8. 7: near out
   9. 8: near in
   10. 9: deep in

Eg: The datafiled ‘opt23_ise_trans_iv_weight_avg_volivput9’ resembles Weighted average Implied volatility for  **deep in-the-money**  put options. Volume is used as weights.

1. Below are the metrics that are available in the dataset from the datasources mentioned in Point 1, across the derived metrics (Point 2) as well as at various moneyness levels (Point 3):
   1. Option Greeks ( [Delta]([链接已屏蔽]) ,  [Gamma]([链接已屏蔽]) ,  [Theta]([链接已屏蔽]) ,  [Vega]([链接已屏蔽]) ,  [Rho]([链接已屏蔽]) )
   2. [Implied Volatility]([链接已屏蔽])

1. Values that are only available for the various datasources but the fields for which Point 2 and 3 derived values are not relevant are:
   1. [Strike Prices]([链接已屏蔽])
   2. [Volume]([链接已屏蔽])
   3. [Open Interest]([链接已屏蔽])
   4. [Options Close Price (Valid*close)]([链接已屏蔽])

**SAMPLE ALPHA IDEAS:**

**Using the above dataset notes, one can create various Alphas across the 1936 datafields. Some of the ideas are listed below**

1. *Change in Implied Volatility (IV)*
   The changes in IV could hint a change in demand for call and put options, which could hint a change about the sentiment of a stock.
   1. Change in Call IV
   2. Change in Put IV
   3. Change in Call IV – Change in Put IV

1. *Volatility skew*
   The volatility skew resembles the difference in Implied Volatility (IV) between out of the money (OTM), at the money (ATM) and in the money (ITM) options. If investors expect a significant price movement in one direction, these investors would be willing to pay more for options that would profit from this move. Search “Volatility Skew” on your browser and read how can this impact stock prices in various instances.

1. *Ratio of Option Volumes to Stock Volumes. (O/S Volume ratio)*
   High conviction traders are more likely to take a view in the options market, which could tell us how strongly investors feel about a stock. The below may be used as a starting point:
   1. 5 day/22 day average of the O/S Volume ratio
   2. Change of the O/S Volume ratio
   3. 5 day O/S Volume ratio relative to 21 day O/S Volume ratio

**Call for Action:**

*Comment below if you found this post helpful and were able to submit atleast one Alpha using this dataset* . 

Feel free to ask any questions in case of any doubts! We also look forward to hearing if you would like similar notes on other datasets.

**顾问 AM60509 (Rank 61) 的解答与建议**:
The dataset notes are detailed and provide clear guidance on leveraging the ‘Options23’ dataset for Alpha generation. The sample ideas, like changes in implied volatility and especially volatility skew, are practical starting points. I particularly like the focus on volatility skew and the O/S Volume ratio as indicators of market sentiment. These insights provide a solid foundation for exploring this dataset further and creating actionable trading strategies.


---

### 技术对话片段 23 (原帖: Dataset Deepdives - Option23 (Option Implied Volatility and Greeks)被推荐的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Dataset Deepdives - Option23 Option Implied Volatility and Greeks被推荐的_27569589603863.md
- **时间**: 1年前

**提问/主帖背景 (AC28031)**:
Options are an excellent dataset for conducting  *HUMAN based research* . In this article, we will discuss various potential Alphas that can be generated using the ‘Options23’ dataset.

**Dataset Highlights:**

- The ‘Options23’ dataset has 1,936 data fields with both matrix and vector data types.
- The dataset is only available for the USA Region.
- At the time of writing, only 424 Alphas are submitted using this dataset, making it slightly unexplored by the consultant community.

**Introduction:**

Although creating Alphas with a HUMAN approach from a dataset with 2k data fields may seem daunting, it is almost always the case that if you take a closer look at the data, a well-structured approach for generating Alphas with clear hypothesis can be formulated.

As previously discussed, when conducting human-based research, it is crucial to step back and create organized notes on accessing the dataset to formulate logical and non-random hypotheses. This article is one such example of dataset notes for the ‘Options23’ dataset that can help in creating Alphas:

**DATASET NOTES:**

1. The dataset has options data like implied volatility, option greeks, strike prices, etc from  **5 DIFFERENT DATA SOURCES** . Thus one must ensure that while using comparison fields within the dataset, the datasource must ideally remain the same to have a fair comparison.

1. For the aforementioned data sources, the dataset includes both raw values and derived values of various options data. The derived values are primarily weighted averages of Implied Volatility and Option Greeks, using either of the following as weights across multiple data sources:
   1. Volume
   2. Open Interest
2. For the aforementioned data sources and weighted average values, the options data values are calculated at various levels of moneyness. The moneyness levels are highlighted based off a suffix in the datafield from 0 to 9. Below is the list of the options data available in the various order of moneyness levels as highlighted in the datafields:
   1. 0: all
   2. 1: near in and out
   3. 2: near out and in
   4. 3: out
   5. 4: near
   6. 5: in
   7. 6: far out
   8. 7: near out
   9. 8: near in
   10. 9: deep in

Eg: The datafiled ‘opt23_ise_trans_iv_weight_avg_volivput9’ resembles Weighted average Implied volatility for  **deep in-the-money**  put options. Volume is used as weights.

1. Below are the metrics that are available in the dataset from the datasources mentioned in Point 1, across the derived metrics (Point 2) as well as at various moneyness levels (Point 3):
   1. Option Greeks ( [Delta]([链接已屏蔽]) ,  [Gamma]([链接已屏蔽]) ,  [Theta]([链接已屏蔽]) ,  [Vega]([链接已屏蔽]) ,  [Rho]([链接已屏蔽]) )
   2. [Implied Volatility]([链接已屏蔽])

1. Values that are only available for the various datasources but the fields for which Point 2 and 3 derived values are not relevant are:
   1. [Strike Prices]([链接已屏蔽])
   2. [Volume]([链接已屏蔽])
   3. [Open Interest]([链接已屏蔽])
   4. [Options Close Price (Valid*close)]([链接已屏蔽])

**SAMPLE ALPHA IDEAS:**

**Using the above dataset notes, one can create various Alphas across the 1936 datafields. Some of the ideas are listed below**

1. *Change in Implied Volatility (IV)*
   The changes in IV could hint a change in demand for call and put options, which could hint a change about the sentiment of a stock.
   1. Change in Call IV
   2. Change in Put IV
   3. Change in Call IV – Change in Put IV

1. *Volatility skew*
   The volatility skew resembles the difference in Implied Volatility (IV) between out of the money (OTM), at the money (ATM) and in the money (ITM) options. If investors expect a significant price movement in one direction, these investors would be willing to pay more for options that would profit from this move. Search “Volatility Skew” on your browser and read how can this impact stock prices in various instances.

1. *Ratio of Option Volumes to Stock Volumes. (O/S Volume ratio)*
   High conviction traders are more likely to take a view in the options market, which could tell us how strongly investors feel about a stock. The below may be used as a starting point:
   1. 5 day/22 day average of the O/S Volume ratio
   2. Change of the O/S Volume ratio
   3. 5 day O/S Volume ratio relative to 21 day O/S Volume ratio

**Call for Action:**

*Comment below if you found this post helpful and were able to submit atleast one Alpha using this dataset* . 

Feel free to ask any questions in case of any doubts! We also look forward to hearing if you would like similar notes on other datasets.

**顾问 AM60509 (Rank 61) 的解答与建议**:
The dataset notes are detailed and provide clear guidance on leveraging the ‘Options23’ dataset for Alpha generation. The sample ideas, like changes in implied volatility and especially volatility skew, are practical starting points. I particularly like the focus on volatility skew and the O/S Volume ratio as indicators of market sentiment. These insights provide a solid foundation for exploring this dataset further and creating actionable trading strategies.


---

### 技术对话片段 24 (原帖: Details on the Upcoming Combined PowerPool Alpha Performance Metric?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Details on the Upcoming Combined PowerPool Alpha Performance Metric_32229909238679.md
- **时间**: 1年前

**提问/主帖背景 (AK40989)**:
I heard during the recent webinar that  *Combined PowerPool Alpha Performance*  will soon be displayed on the Genius page and will be  **evaluated for the current Quarter 2** .

Since PowerPool alphas are becoming the new standard across all regions, I’m just trying to better understand what kind of metric they’re planning to introduce — I didn’t quite catch that part during the webinar.

If anyone has more clarity or context around how this will work or how it might influence Genius evaluation, would really appreciate the insights!

**顾问 AM60509 (Rank 61) 的解答与建议**:
[AK40989](/hc/en-us/profiles/26422151767703-AK40989)   
I watched the webinar very closely and clearly remember what was told.

This feature will be introduced in Q2 2025 and criteria for selection for each of the levels would be similar to Combined Alpha Performance and Combined Selected Alpha Performance ie if  **Combined Power Pool Performance must be 0.5 for Expert ,1.0 for Master and 2.0 for GrandMaster**


---

### 技术对话片段 25 (原帖: Earnings Announcement data)
- **原帖链接**: [Commented] Earnings Announcement data.md
- **时间**: 1年前

**提问/主帖背景 (AT20552)**:
Hi all, I was wondering if there is any variable for the earnings announcement date. I was trying to find it however was unable to do so. If any of you is aware of any data that conveys the date of earnings announcement or maybe something like trading days till next earnings announcement or trading days since last earnings announcement, please let me know. Thanks

**顾问 AM60509 (Rank 61) 的解答与建议**:
There are quite a few useful suggestions already. As others mentioned, the earnings3 or earnings4 datasets are good places to look when your account's at consultant level. Also, trying fields like ern3_next_interval from the ern3 dataset could work


---

### 技术对话片段 26 (原帖: Earnings Announcement data)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Earnings Announcement data_28354916155159.md
- **时间**: 1年前

**提问/主帖背景 (AT20552)**:
Hi all, I was wondering if there is any variable for the earnings announcement date. I was trying to find it however was unable to do so. If any of you is aware of any data that conveys the date of earnings announcement or maybe something like trading days till next earnings announcement or trading days since last earnings announcement, please let me know. Thanks

**顾问 AM60509 (Rank 61) 的解答与建议**:
There are quite a few useful suggestions already. As others mentioned, the earnings3 or earnings4 datasets are good places to look when your account's at consultant level. Also, trying fields like ern3_next_interval from the ern3 dataset could work


---

### 技术对话片段 27 (原帖: From Data to Trade: A Machine Learning Approach to Quantitative Trading)
- **原帖链接**: [Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

The paper efficiently tackles common alpha features and explores diverse methods to extract and normalize them. (Co-authored by ChatGPT)

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you so much for providing this research paper "Machine Learning approach to quantitative trading".To start with making models based on machine learning start with Big data and machine learning based model dataset. It comes under model category.


---

### 技术对话片段 28 (原帖: From Data to Trade: A Machine Learning Approach to Quantitative Trading)
- **原帖链接**: https://support.worldquantbrain.com[Commented] From Data to Trade A Machine Learning Approach to Quantitative Trading_25238140123799.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

The paper efficiently tackles common alpha features and explores diverse methods to extract and normalize them. (Co-authored by ChatGPT)

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you so much for providing this research paper "Machine Learning approach to quantitative trading".To start with making models based on machine learning start with Big data and machine learning based model dataset. It comes under model category.


---

### 技术对话片段 29 (原帖: How can you avoid overfitting?)
- **原帖链接**: [Commented] How can you avoid overfitting.md
- **时间**: 1年前

**提问/主帖背景 (KA64574)**:
We have to accept the fact that fitting is a part of the alpha creation process. As a result, overfitting is also part of the game. The most important way to control for overfitting is by doing disciplined research.

Is overfitting bad? Yes, it is. However, random data mining research without ideas is even worse. Robust alphas require good ideas and rigorous testing. Here are some of the tests you can use to reduce the chance for overfitting and improve the robustness of your alphas.

- Rank test (turn alpha to rank)
- Binary test (turn alpha to -1, 1)
- Sub/super universe test

Don’t limit yourself to what is listed here. There are tests that can be done based on your creativity and experience; the more you do the better. By the way, random backtest is often not very applicable due to changing market conditions.

Here are some other tips and tricks:

- Often it is not a good idea to concentrate weight on volatile stocks.
- Reduce your exposure to factors.
- Don’t choose the best; the second best often has less overfitting tendency.
- Don’t fit tests. No test is bad. Fitting to tests is also bad.
- Don’t select. If you have to choose between using 4 or 6-day decays, you can use 5 or simply take the alpha average of 4 and 6 days.
- Don’t fail in to the excellent/superior trap. What you see based on IS performance. The main question is, “Can that performance hold?”
- Be courteous to other people and share ideas and good advice.

Using the test period feature in settings to prevent overfitting:

Using simulation settings, you can divide your In-Sample (IS) period into a Train and Test period. The Train period can be utilized to develop your Alphas and SuperAlphas, while the Test period is ideal for validating them. An Alpha developed based on the simulation results of Training Period and performs well in both periods is likely a strong candidate for submission and may have avoided overfitting.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Use normal look back periods like 5,20,60,252 in your alpha and also stop fine tuning parameters like powers etc. excessively


---

### 技术对话片段 30 (原帖: How can you avoid overfitting?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How can you avoid overfitting_8209806533015.md
- **时间**: 1 year ago

**提问/主帖背景 (KA64574)**:
We have to accept the fact that fitting is a part of the alpha creation process. As a result, overfitting is also part of the game. The most important way to control for overfitting is by doing disciplined research.

Is overfitting bad? Yes, it is. However, random data mining research without ideas is even worse. Robust alphas require good ideas and rigorous testing. Here are some of the tests you can use to reduce the chance for overfitting and improve the robustness of your alphas.

- Rank test (turn alpha to rank)
- Binary test (turn alpha to -1, 1)
- Sub/super universe test

Don’t limit yourself to what is listed here. There are tests that can be done based on your creativity and experience; the more you do the better. By the way, random backtest is often not very applicable due to changing market conditions.

Here are some other tips and tricks:

- Often it is not a good idea to concentrate weight on volatile stocks.
- Reduce your exposure to factors.
- Don’t choose the best; the second best often has less overfitting tendency.
- Don’t fit tests. No test is bad. Fitting to tests is also bad.
- Don’t select. If you have to choose between using 4 or 6-day decays, you can use 5 or simply take the alpha average of 4 and 6 days.
- Don’t fail in to the excellent/superior trap. What you see based on IS performance. The main question is, “Can that performance hold?”
- Be courteous to other people and share ideas and good advice.

Using the test period feature in settings to prevent overfitting:

Using simulation settings, you can divide your In-Sample (IS) period into a Train and Test period. The Train period can be utilized to develop your Alphas and SuperAlphas, while the Test period is ideal for validating them. An Alpha developed based on the simulation results of Training Period and performs well in both periods is likely a strong candidate for submission and may have avoided overfitting.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Use normal look back periods like 5,20,60,252 in your alpha and also stop fine tuning parameters like powers etc. excessively


---

### 技术对话片段 31 (原帖: How do you guys get good with Alphas?)
- **原帖链接**: [Commented] How do you guys get good with Alphas.md
- **时间**: 1年前

**提问/主帖背景 (JP51577)**:
Hi guys! I just wanted to ask about the best way about learning about Alphas. I've been actively on the platform for a few days, but so far I've only managed to submit 1 Alpha, with a few of my unsubmitted ones very close to passing all tests (usually it's the sharpe that's super close to the threshold). I've watched the training videos, and also read the documents, been to the forums, but I don't seem to understand them much as well to apply them into my Alpha simulations, even the super beginner ones.

To those who've managed to consistently submit Alphas, reached silver/gold level, or managed to understand how Alphas work and are able to consistently apply the skills to improving your Alphas - how did you guys do it?

I would love to have some tips and tricks as I'm feeling super lost and demotivated. Thank you!

**顾问 AM60509 (Rank 61) 的解答与建议**:
Go through the Videos and documentation given on the learn section and also go through the articles.Focus on one region say USA initially to make your alphas and start with simpler datasets like price/volume and fundamental


---

### 技术对话片段 32 (原帖: How do you guys get good with Alphas?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How do you guys get good with Alphas_20797812617367.md
- **时间**: 1年前

**提问/主帖背景 (JP51577)**:
Hi guys! I just wanted to ask about the best way about learning about Alphas. I've been actively on the platform for a few days, but so far I've only managed to submit 1 Alpha, with a few of my unsubmitted ones very close to passing all tests (usually it's the sharpe that's super close to the threshold). I've watched the training videos, and also read the documents, been to the forums, but I don't seem to understand them much as well to apply them into my Alpha simulations, even the super beginner ones.

To those who've managed to consistently submit Alphas, reached silver/gold level, or managed to understand how Alphas work and are able to consistently apply the skills to improving your Alphas - how did you guys do it?

I would love to have some tips and tricks as I'm feeling super lost and demotivated. Thank you!

**顾问 AM60509 (Rank 61) 的解答与建议**:
Go through the Videos and documentation given on the learn section and also go through the articles.Focus on one region say USA initially to make your alphas and start with simpler datasets like price/volume and fundamental


---

### 技术对话片段 33 (原帖: How to Improve After Cost Performance置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How to Improve After Cost Performance置顶的_29647491881623.md
- **时间**: 1年前

**提问/主帖背景 (Di Sheng Tan)**:
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

**顾问 AM60509 (Rank 61) 的解答与建议**:
To improve after cost performance ,make low turnover alphas ideally in the range of 10-15% or even below.

Check sub universe sharpe performance to make sure signal performance doesnt dip


---

### 技术对话片段 34 (原帖: How to Improve After Cost Performance置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How to Improve After Cost Performance置顶的_29647491881623.md
- **时间**: 1年前

**提问/主帖背景 (Di Sheng Tan)**:
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

**顾问 AM60509 (Rank 61) 的解答与建议**:
3 ways to improve after cost performance are:-

1.Reduce turnover.

Lesser is the turnover ,better is the after cost performance

Ideal turnover should be less than 15% expect for news datasets for which turnover around 25% is fine

2.Improve Sub Universe Sharpe

Better is the sub universe sharpe ,better is the after cost performance

3.Use Investability Constrained Metric

Better and higher is the performance as shown by the investability constrained metric better will be the after cost performance


---

### 技术对话片段 35 (原帖: How to increase Sharpe without overfitting?)
- **原帖链接**: [Commented] How to increase Sharpe without overfitting.md
- **时间**: 1年前

**提问/主帖背景 (HN80189)**:
I tried to increase my Sharpe, but only can increase it if I sum 2 alphas. I know it's not good but don't know other way. Anyone have tip for me?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Change the lookback period settings to simpler values like 20,60,252. You can also alter the decay settings. Use different time series operators like rank operator instead of quantile operator


---

### 技术对话片段 36 (原帖: How to increase Sharpe without overfitting?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How to increase Sharpe without overfitting_27841757470359.md
- **时间**: 1年前

**提问/主帖背景 (HN80189)**:
I tried to increase my Sharpe, but only can increase it if I sum 2 alphas. I know it's not good but don't know other way. Anyone have tip for me?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Change the lookback period settings to simpler values like 20,60,252. You can also alter the decay settings. Use different time series operators like rank operator instead of quantile operator


---

### 技术对话片段 37 (原帖: How to reduce self correlation  and production correlation)
- **原帖链接**: [Commented] How to reduce self correlation  and production correlation.md
- **时间**: 1年前

**提问/主帖背景 (RB25229)**:
Self correlation and production correlation depends on the your creative ideas to create alphas. Try to diversify for alphas as much as you can. it will reduce your production and self correlation as well.

NOTE - Also keep track that you are not overfitting the signal  just to  pass the submission tests..😣

LETS GROW TOGHETHER.....😊

**顾问 AM60509 (Rank 61) 的解答与建议**:
Try to work on different universe settings within the same region.Try different neutralization settings.Try different regions say China,Hong Kong,Taiwan.You also use different grouping fields if you are using group Cartesian operator


---

### 技术对话片段 38 (原帖: How to reduce self correlation  and production correlation)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How to reduce self correlation  and production correlation_26750743873943.md
- **时间**: 1年前

**提问/主帖背景 (RB25229)**:
Self correlation and production correlation depends on the your creative ideas to create alphas. Try to diversify for alphas as much as you can. it will reduce your production and self correlation as well.

NOTE - Also keep track that you are not overfitting the signal  just to  pass the submission tests..😣

LETS GROW TOGHETHER.....😊

**顾问 AM60509 (Rank 61) 的解答与建议**:
Try to work on different universe settings within the same region.Try different neutralization settings.Try different regions say China,Hong Kong,Taiwan.You also use different grouping fields if you are using group Cartesian operator


---

### 技术对话片段 39 (原帖: How to select best alpha for superalpha.)
- **原帖链接**: [Commented] How to select best alpha for superalpha.md
- **时间**: 1年前

**提问/主帖背景 (PT88153)**:
Hey Community, Can anyone suggest how to select best alpha for the Superalpha which has low co-orelation and high fitness.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Focusing on diversity, low correlation, and strong OS performance ensures a balanced and high-performing portfolio.Have you considered testing variations in weightings or applying clustering methods to refine your selections further


---

### 技术对话片段 40 (原帖: How to select best alpha for superalpha.)
- **原帖链接**: https://support.worldquantbrain.com[Commented] How to select best alpha for superalpha_29160840959127.md
- **时间**: 1年前

**提问/主帖背景 (PT88153)**:
Hey Community, Can anyone suggest how to select best alpha for the Superalpha which has low co-orelation and high fitness.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Focusing on diversity, low correlation, and strong OS performance ensures a balanced and high-performing portfolio.Have you considered testing variations in weightings or applying clustering methods to refine your selections further


---

### 技术对话片段 41 (原帖: I want to learn)
- **原帖链接**: [Commented] I want to learn.md
- **时间**: 1年前

**提问/主帖背景 (AH55751)**:
Can I use mobile phone to learn?

**顾问 AM60509 (Rank 61) 的解答与建议**:
You can use either a computer and mobile to create alphas on brain platform.I have personally created alphas with both of them but it is easier with the laptop.


---

### 技术对话片段 42 (原帖: I want to learn)
- **原帖链接**: https://support.worldquantbrain.com[Commented] I want to learn_23526172472855.md
- **时间**: 1年前

**提问/主帖背景 (AH55751)**:
Can I use mobile phone to learn?

**顾问 AM60509 (Rank 61) 的解答与建议**:
You can use either a computer and mobile to create alphas on brain platform.I have personally created alphas with both of them but it is easier with the laptop.


---

### 技术对话片段 43 (原帖: IN TIE BREAKER CRITERIA WHAT EXACTLY DOES ONE HAS TO DO TO INCREASE HIS COMUNITY ACTIVITY?)
- **原帖链接**: [Commented] IN TIE BREAKER CRITERIA WHAT EXACTLY DOES ONE HAS TO DO TO INCREASE HIS COMUNITY ACTIVITY.md
- **时间**: 1年前

**提问/主帖背景 (CM45657)**:
In tie breaker i have been experiencing challeges in tha community activity  part.. guide me to the strategies one use for his community activity to increase

**顾问 AM60509 (Rank 61) 的解答与建议**:
The number of likes on your comments and posts help increase community activity.

The comments need to be 100 characters or more to qualify so as to contribute to community activity.


---

### 技术对话片段 44 (原帖: IN TIE BREAKER CRITERIA WHAT EXACTLY DOES ONE HAS TO DO TO INCREASE HIS COMUNITY ACTIVITY?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] IN TIE BREAKER CRITERIA WHAT EXACTLY DOES ONE HAS TO DO TO INCREASE HIS COMUNITY ACTIVITY_29204783096087.md
- **时间**: 1年前

**提问/主帖背景 (CM45657)**:
In tie breaker i have been experiencing challeges in tha community activity  part.. guide me to the strategies one use for his community activity to increase

**顾问 AM60509 (Rank 61) 的解答与建议**:
The number of likes on your comments and posts help increase community activity.

The comments need to be 100 characters or more to qualify so as to contribute to community activity.


---

### 技术对话片段 45 (原帖: Incorporating Volatility into Chinese Market Trades)
- **原帖链接**: [Commented] Incorporating Volatility into Chinese Market Trades.md
- **时间**: 1年前

**提问/主帖背景 (SA89201)**:
One of the bronze alpha ideas involved going long on the stocks with low volume in the Chinese market and short on those with high volume. One of the suggestions for improving the alpha suggested incorporating volatility, but I'm not sure which datasets tell us about volatility in the Chinese market (all the obvious volatility ones seem to only exist for the US market). Any help here would be appreciated!

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to introduce volatility into the alpha ,multiply the alpha by rank(ts_stddev(returns,25) or rank (ts_stddev(alpha1,lookback period) where alpha1 is the alpha expression


---

### 技术对话片段 46 (原帖: Incorporating Volatility into Chinese Market Trades)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Incorporating Volatility into Chinese Market Trades_23726331730327.md
- **时间**: 1年前

**提问/主帖背景 (SA89201)**:
One of the bronze alpha ideas involved going long on the stocks with low volume in the Chinese market and short on those with high volume. One of the suggestions for improving the alpha suggested incorporating volatility, but I'm not sure which datasets tell us about volatility in the Chinese market (all the obvious volatility ones seem to only exist for the US market). Any help here would be appreciated!

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to introduce volatility into the alpha ,multiply the alpha by rank(ts_stddev(returns,25) or rank (ts_stddev(alpha1,lookback period) where alpha1 is the alpha expression


---

### 技术对话片段 47 (原帖: Key points about alpha decay and signal robustness:)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Key points about alpha decay and signal robustness_30216887734167.md
- **时间**: 1年前

**提问/主帖背景 (LM22798)**:
- **Impact on performance:**
  As alpha decays, the profitability of a trading strategy decreases, impacting the overall investment returns.
- **Causes of alpha decay:**
  - **Market crowding:**  When many investors start using the same signal, the market price quickly adjusts to reflect the information, eliminating the opportunity for abnormal returns.
  - **Market efficiency:**  As more information becomes available, the market becomes more efficient, making it harder to identify profitable anomalies.
  - **Signal degradation:**  Over time, the underlying factors driving the signal may change, causing its predictive power to weaken.
- **Signal robustness:**
  A robust signal is one that maintains its predictive power even when widely used, resisting significant degradation from market crowding.

**顾问 AM60509 (Rank 61) 的解答与建议**:
As alpha (the excess return of a strategy above the benchmark) decays, the returns diminish, resulting in lower profitability. When a strategy loses its edge, it no longer provides the same returns it once did.This decline is often driven by market crowding, where widespread use of the same signal erodes its edge, and increasing market efficiency, which makes profitable anomalies harder to find


---

### 技术对话片段 48 (原帖: Machine Learning for Stock Selection)
- **原帖链接**: [Commented] Machine Learning for Stock Selection.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Talks about general machine structures, and proposed solutions to overfitting.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thanks for sharing the article. To start with making models using machine learning, use Big data and machine learning based model dataset. It comes under model category.


---

### 技术对话片段 49 (原帖: Machine Learning for Stock Selection)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Machine Learning for Stock Selection_25238140293143.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Talks about general machine structures, and proposed solutions to overfitting.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thanks for sharing the article. To start with making models using machine learning, use Big data and machine learning based model dataset. It comes under model category.


---

### 技术对话片段 50 (原帖: Mistakes I Made in Q4 2024 and What You Should Avoid to Reach Higher Levels)
- **原帖链接**: [Commented] Mistakes I Made in Q4 2024 and What You Should Avoid to Reach Higher Levels.md
- **时间**: 1年前

**提问/主帖背景 (PP87148)**:
In Q4 2024, despite creating the highest number of signals, I ended up in the Expert level. Here are the key mistakes I made and lessons for fellow consultants:

1. **Focusing too much on quantity** : I thought the tie-breaker criteria would only apply if consultants had the same signals and pyramids. This was wrong. Quality matters more than quantity.
2. **Ignoring tie-breaker criteria** : Once you qualify for a level, tie-breakers decide your final position. I missed this critical point, which impacted my ranking.
3. **Excessive fields per alpha** : Though 400+ fields seem good, my field-per-alpha ratio was high (6+), which negatively affected my alpha’s quality.
4. **Too many operators** : Though 80+ operators seem good, the high operator-per-alpha count (10+) worked against me.
5. **Lack of community engagement** : Not being active in the community also set me back, as it's essential for building connections and improving.

**Focus on quality, reduce redundancy, stay active in the community, and always consider tie-breaker criteria to avoid repeating my mistakes.**

**顾问 AM60509 (Rank 61) 的解答与建议**:
It’s critical to remember that high-quality outputs lead to better rankings, especially when tie-breakers come into play. Many people tend to overemphasize pyramids and the number of alphas, but the tie-breaking criteria are far more crucial.

I also qualified for Master Level but got only Gold.

@ [PP87148](/hc/en-us/profiles/11771952650775-PP87148)  I sympthasize with you


---

### 技术对话片段 51 (原帖: Mistakes I Made in Q4 2024 and What You Should Avoid to Reach Higher Levels)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Mistakes I Made in Q4 2024 and What You Should Avoid to Reach Higher Levels_29205896033175.md
- **时间**: 1年前

**提问/主帖背景 (PP87148)**:
In Q4 2024, despite creating the highest number of signals, I ended up in the Expert level. Here are the key mistakes I made and lessons for fellow consultants:

1. **Focusing too much on quantity** : I thought the tie-breaker criteria would only apply if consultants had the same signals and pyramids. This was wrong. Quality matters more than quantity.
2. **Ignoring tie-breaker criteria** : Once you qualify for a level, tie-breakers decide your final position. I missed this critical point, which impacted my ranking.
3. **Excessive fields per alpha** : Though 400+ fields seem good, my field-per-alpha ratio was high (6+), which negatively affected my alpha’s quality.
4. **Too many operators** : Though 80+ operators seem good, the high operator-per-alpha count (10+) worked against me.
5. **Lack of community engagement** : Not being active in the community also set me back, as it's essential for building connections and improving.

**Focus on quality, reduce redundancy, stay active in the community, and always consider tie-breaker criteria to avoid repeating my mistakes.**

**顾问 AM60509 (Rank 61) 的解答与建议**:
It’s critical to remember that high-quality outputs lead to better rankings, especially when tie-breakers come into play. Many people tend to overemphasize pyramids and the number of alphas, but the tie-breaking criteria are far more crucial.

I also qualified for Master Level but got only Gold.

@ [PP87148](/hc/en-us/profiles/11771952650775-PP87148)  I sympthasize with you


---

### 技术对话片段 52 (原帖: Momentum in Prices and Volume of Trades)
- **原帖链接**: [Commented] Momentum in Prices and Volume of Trades.md
- **时间**: 1年前

**提问/主帖背景 (KS69567)**:
This study reveals a key relationship between  **past trading volume**  and both  **momentum**  and  **value**  strategies, highlighting its predictive power for future stock performance. Specifically, firms with high  **past turnover ratios**  (indicative of higher trading volume) tend to exhibit  **glamour**  characteristics, earn lower future returns, and experience more  **negative earnings surprises** . Conversely, firms with low turnover ratios align with  **value**  characteristics, earn higher future returns, and show more  **positive earnings surprises**  over the next eight quarters.

Furthermore, past trading volume is a strong predictor of both the  **magnitude**  and  **persistence**  of  **price momentum** . The study finds that  **momentum effects**  tend to reverse over a five-year horizon, with high-volume winners and low-volume losers experiencing  **faster reversals** .

The study’s findings provide several deeper insights into the relationship between  **past trading volume** ,  **momentum** , and  **value**  strategies, with implications for both asset pricing and investment strategies:

1. **Momentum and Value Strategies** : The study shows that  **high past trading volume**  correlates with stocks exhibiting  **glamour characteristics** , which tend to earn  **lower future returns** . On the other hand,  **low past trading volume**  is associated with stocks that have  **value characteristics** , which historically generate  **higher future returns** . This suggests that investors who focus on high-volume stocks may be chasing recent price gains (glamour), while those focusing on low-volume stocks may be buying underappreciated or undervalued assets.
2. **Earnings Surprises** : The study also highlights that firms with  **high past trading volume**  tend to have  **more negative earnings surprises**  in the following quarters, while firms with  **low past trading volume**  tend to experience  **more positive earnings surprises** . This is important for forecasting earnings results, as  **momentum stocks**  are often priced with overly optimistic expectations, leading to negative earnings surprises, while  **value stocks**  may be underappreciated, leading to positive surprises.
3. **Price Momentum and Reversals** : The study shows that  **price momentum**  effects (where stocks continue to move in the same direction) tend to reverse over time, particularly within a  **five-year horizon** . Stocks with  **high volume**  that have been  **winners**  (rising prices) are likely to experience  **faster reversals** , while  **low-volume losers**  (declining stocks) also experience reversals. This insight challenges traditional momentum strategies and emphasizes that the persistence of price momentum is temporary, especially for stocks with extreme trading volumes.
4. **Intermediate-Horizon Underreaction and Long-Horizon Overreaction** : The findings effectively reconcile the  **underreaction**  and  **overreaction**  effects observed in asset pricing. At shorter horizons (e.g., intermediate-term), stocks with high trading volume may be subject to underreaction, where market prices fail to fully adjust to new information, creating opportunities for momentum. However, over longer horizons, the  **overreaction**  effect takes hold, where stocks that have experienced momentum begin to experience reversals as the market corrects itself, indicating  **market inefficiency** .

### Implications for Investment Strategies:

- **Trading Volume as a Signal** : Traders and investors can use past trading volume as a signal to gauge potential future returns and adjust their portfolios accordingly. High-volume stocks may indicate a  **momentum**  strategy, while low-volume stocks could align with a  **value**  strategy.
- **Timing of Momentum Strategies** : The study suggests that momentum strategies should be adjusted over time, with caution for longer-term holding periods.  **Faster reversals**  in high-volume winners and low-volume losers suggest that  **momentum strategies**  may need to be shortened in duration to avoid losses from price corrections.
- **Predictive Power for Earnings** : Past trading volume could be integrated into  **earnings prediction models** . High-volume stocks may have a higher probability of negative earnings surprises, while low-volume stocks may signal potential positive earnings surprises.
- **Enhancing Risk-Adjusted Returns** : By incorporating insights from past volume trends, investors can better manage risk and improve the risk-adjusted returns of their momentum and value strategies. Recognizing when momentum is likely to reverse or when value opportunities are undervalued based on volume trends can lead to more informed decision-making.

These findings underscore the importance of  **trading volume**  as a significant factor in understanding and predicting stock performance, and offer actionable insights for adjusting both  **momentum**  and  **value**  strategies to align with market dynamics and time horizons.

Overall, the findings suggest that  **past trading volume**  plays a critical role in explaining the dynamics between  **intermediate-horizon underreaction**  (where market prices fail to fully adjust to new information) and  **long-horizon overreaction**  (where prices correct due to overreaction to past trends). These insights help to reconcile and better understand the behavior of stocks over different time horizons, offering valuable implications for developing  **momentum and value-based strategies** .

**顾问 AM60509 (Rank 61) 的解答与建议**:
**momentum**   strategies highlight its high predictive power for future stock performance.

alpha1=alpha+ts_delta(alpha,d) is a way to implement momentum strategy.

where alpha=original alpha expression

d=number of days


---

### 技术对话片段 53 (原帖: Momentum in Prices and Volume of Trades)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Momentum in Prices and Volume of Trades_29301176116759.md
- **时间**: 1年前

**提问/主帖背景 (KS69567)**:
This study reveals a key relationship between  **past trading volume**  and both  **momentum**  and  **value**  strategies, highlighting its predictive power for future stock performance. Specifically, firms with high  **past turnover ratios**  (indicative of higher trading volume) tend to exhibit  **glamour**  characteristics, earn lower future returns, and experience more  **negative earnings surprises** . Conversely, firms with low turnover ratios align with  **value**  characteristics, earn higher future returns, and show more  **positive earnings surprises**  over the next eight quarters.

Furthermore, past trading volume is a strong predictor of both the  **magnitude**  and  **persistence**  of  **price momentum** . The study finds that  **momentum effects**  tend to reverse over a five-year horizon, with high-volume winners and low-volume losers experiencing  **faster reversals** .

The study’s findings provide several deeper insights into the relationship between  **past trading volume** ,  **momentum** , and  **value**  strategies, with implications for both asset pricing and investment strategies:

1. **Momentum and Value Strategies** : The study shows that  **high past trading volume**  correlates with stocks exhibiting  **glamour characteristics** , which tend to earn  **lower future returns** . On the other hand,  **low past trading volume**  is associated with stocks that have  **value characteristics** , which historically generate  **higher future returns** . This suggests that investors who focus on high-volume stocks may be chasing recent price gains (glamour), while those focusing on low-volume stocks may be buying underappreciated or undervalued assets.
2. **Earnings Surprises** : The study also highlights that firms with  **high past trading volume**  tend to have  **more negative earnings surprises**  in the following quarters, while firms with  **low past trading volume**  tend to experience  **more positive earnings surprises** . This is important for forecasting earnings results, as  **momentum stocks**  are often priced with overly optimistic expectations, leading to negative earnings surprises, while  **value stocks**  may be underappreciated, leading to positive surprises.
3. **Price Momentum and Reversals** : The study shows that  **price momentum**  effects (where stocks continue to move in the same direction) tend to reverse over time, particularly within a  **five-year horizon** . Stocks with  **high volume**  that have been  **winners**  (rising prices) are likely to experience  **faster reversals** , while  **low-volume losers**  (declining stocks) also experience reversals. This insight challenges traditional momentum strategies and emphasizes that the persistence of price momentum is temporary, especially for stocks with extreme trading volumes.
4. **Intermediate-Horizon Underreaction and Long-Horizon Overreaction** : The findings effectively reconcile the  **underreaction**  and  **overreaction**  effects observed in asset pricing. At shorter horizons (e.g., intermediate-term), stocks with high trading volume may be subject to underreaction, where market prices fail to fully adjust to new information, creating opportunities for momentum. However, over longer horizons, the  **overreaction**  effect takes hold, where stocks that have experienced momentum begin to experience reversals as the market corrects itself, indicating  **market inefficiency** .

### Implications for Investment Strategies:

- **Trading Volume as a Signal** : Traders and investors can use past trading volume as a signal to gauge potential future returns and adjust their portfolios accordingly. High-volume stocks may indicate a  **momentum**  strategy, while low-volume stocks could align with a  **value**  strategy.
- **Timing of Momentum Strategies** : The study suggests that momentum strategies should be adjusted over time, with caution for longer-term holding periods.  **Faster reversals**  in high-volume winners and low-volume losers suggest that  **momentum strategies**  may need to be shortened in duration to avoid losses from price corrections.
- **Predictive Power for Earnings** : Past trading volume could be integrated into  **earnings prediction models** . High-volume stocks may have a higher probability of negative earnings surprises, while low-volume stocks may signal potential positive earnings surprises.
- **Enhancing Risk-Adjusted Returns** : By incorporating insights from past volume trends, investors can better manage risk and improve the risk-adjusted returns of their momentum and value strategies. Recognizing when momentum is likely to reverse or when value opportunities are undervalued based on volume trends can lead to more informed decision-making.

These findings underscore the importance of  **trading volume**  as a significant factor in understanding and predicting stock performance, and offer actionable insights for adjusting both  **momentum**  and  **value**  strategies to align with market dynamics and time horizons.

Overall, the findings suggest that  **past trading volume**  plays a critical role in explaining the dynamics between  **intermediate-horizon underreaction**  (where market prices fail to fully adjust to new information) and  **long-horizon overreaction**  (where prices correct due to overreaction to past trends). These insights help to reconcile and better understand the behavior of stocks over different time horizons, offering valuable implications for developing  **momentum and value-based strategies** .

**顾问 AM60509 (Rank 61) 的解答与建议**:
**momentum**   strategies highlight its high predictive power for future stock performance.

alpha1=alpha+ts_delta(alpha,d) is a way to implement momentum strategy.

where alpha=original alpha expression

d=number of days


---

### 技术对话片段 54 (原帖: Passing the IS-Ladder Sharpe ?)
- **原帖链接**: [Commented] Passing the IS-Ladder Sharpe.md
- **时间**: 1年前

**提问/主帖背景 (RD14646)**:
The  **IS-Ladder Sharpe**  test tends to be one of the most formidable criteria in creating a submittable alpha. Over the past couple of months, I have found a few solutions to aid in passing the test but would like the community to share their approach to tackling this.

My solutions are as follows:

1. **Self-Boosting:** I tend to create alphas with the rank operator generally, so this particular technique might aid in similar settings. The expression looks something like (alpha) * (1 + alpha).
   It is different from a simple squared alpha because it helps maintain an amicable weight distribution but also strengthens the extreme long and short signals.
2. **Division over Multiplication:**  The above method might yet fail to pass the IS-Ladder Sharpe test by some margin. Attempting to further strengthen the extreme long and short signals might just do the trick. We may try something like (alpha) * (0.5 + alpha), but I have found (alpha) / ( N - alpha) easier to work with. N can be kept large to reduce the effect. However, N always has to be > 1 to prevent undefined behavior. I tend to use values of 1.5 and 2 mostly, but in extreme cases, 1.1 helps too.
3. **Try all groupings:** Get the best from the lot and try back with methods 1 and 2.

Eager to hear your suggestions and opinions.

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to improve is ladder sharpe ratio,focus on improving your overall sharpe ratio .Use simpler lookback periods like,20,60,252 and simpler exponents.Try to implement simple and robust ideas with single datasets


---

### 技术对话片段 55 (原帖: Passing the IS-Ladder Sharpe ?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Passing the IS-Ladder Sharpe_28514143456407.md
- **时间**: 1年前

**提问/主帖背景 (RD14646)**:
The  **IS-Ladder Sharpe**  test tends to be one of the most formidable criteria in creating a submittable alpha. Over the past couple of months, I have found a few solutions to aid in passing the test but would like the community to share their approach to tackling this.

My solutions are as follows:

1. **Self-Boosting:** I tend to create alphas with the rank operator generally, so this particular technique might aid in similar settings. The expression looks something like (alpha) * (1 + alpha).
   It is different from a simple squared alpha because it helps maintain an amicable weight distribution but also strengthens the extreme long and short signals.
2. **Division over Multiplication:**  The above method might yet fail to pass the IS-Ladder Sharpe test by some margin. Attempting to further strengthen the extreme long and short signals might just do the trick. We may try something like (alpha) * (0.5 + alpha), but I have found (alpha) / ( N - alpha) easier to work with. N can be kept large to reduce the effect. However, N always has to be > 1 to prevent undefined behavior. I tend to use values of 1.5 and 2 mostly, but in extreme cases, 1.1 helps too.
3. **Try all groupings:** Get the best from the lot and try back with methods 1 and 2.

Eager to hear your suggestions and opinions.

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to improve is ladder sharpe ratio,focus on improving your overall sharpe ratio .Use simpler lookback periods like,20,60,252 and simpler exponents.Try to implement simple and robust ideas with single datasets


---

### 技术对话片段 56 (原帖: Power of Information Coefficient (IC) and Breadth(B) for Investors)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Power of Information Coefficient IC and BreadthB for Investors_30199742337431.md
- **时间**: 1年前

**提问/主帖背景 (GS28828)**:
As per the paper written by Richard Girnold and Kahn

Information Ratio = Information Coefficient  x  √ Breadth

IR = IC × √B

IR evaluates an investors skill in generating excess returns adjusted for risk

IC measures the correlation between the alpha values (predicted returns) and the future returns of assets. It helps assess how well an alpha factor predicts future performance. This is explained with simplified example of two stocks ABC and XYZ. If stock ABC has a high positive alpha and stock XYZ has a negative alpha, and their future returns match these predictions, then IC will be high.

B is the measure of number of independent bets that are made.

Quantitative investors often have an advantage in achieving high breadth (B) over other investors

But when it comes to IC which is a measure of skill ,there are many investors who are better at making predictions of future returns .

I am interested to know your views on whether, in the future, quantitative investors will beat most of the other investors in IC score as well.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Information Coefficient tells us about the skill of the manager who is managing the funds.Higher the IC ,more is the skill of the manager in generating alpha.Breadth depends on number of bets made during the year.

IR=IC *TC*BR^0.5

IC=Information Coefficient

TC=Transfer Coefficient

BR=Breadth

IR=Information Ratio.

Higher the Information Ratio ,better it is


---

### 技术对话片段 57 (原帖: Recipe for Quantitative Trading with Machine Learning)
- **原帖链接**: [Commented] Recipe for Quantitative Trading with Machine Learning.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Impressive neural network structure proposed for extracting trading signals. While replication on BRAIN may be challenging, the experiment design offers valuable insights to learn from

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing this fascinating research and providing the link to such an insightful paper. You can use the dataset Big data and machine learning based model (part of the model group) to create machine learning based models


---

### 技术对话片段 58 (原帖: Recipe for Quantitative Trading with Machine Learning)
- **原帖链接**: [Commented] Recipe for Quantitative Trading with Machine Learning.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Impressive neural network structure proposed for extracting trading signals. While replication on BRAIN may be challenging, the experiment design offers valuable insights to learn from

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Nice research article. To start making machine learning models, start with Big data and machine learning based model dataset. It comes under model category,


---

### 技术对话片段 59 (原帖: Recipe for Quantitative Trading with Machine Learning)
- **原帖链接**: [Commented] Recipe for Quantitative Trading with Machine Learning.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Impressive neural network structure proposed for extracting trading signals. While replication on BRAIN may be challenging, the experiment design offers valuable insights to learn from

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Key contributions of the paper include:

- Using  **recurrent neural networks (RNNs)**  for market return forecasting.
- Proposing an algorithm to simultaneously predict price levels and directions.
- Introducing autonomous pattern generation to learn traditional analyst-defined shapes.
- Applying  **complex network analysis**  to detect stock price fluctuation patterns.


---

### 技术对话片段 60 (原帖: Recipe for Quantitative Trading with Machine Learning)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Recipe for Quantitative Trading with Machine Learning_25238156762135.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Impressive neural network structure proposed for extracting trading signals. While replication on BRAIN may be challenging, the experiment design offers valuable insights to learn from

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing this fascinating research and providing the link to such an insightful paper. You can use the dataset Big data and machine learning based model (part of the model group) to create machine learning based models


---

### 技术对话片段 61 (原帖: Recipe for Quantitative Trading with Machine Learning)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Recipe for Quantitative Trading with Machine Learning_25238156762135.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Impressive neural network structure proposed for extracting trading signals. While replication on BRAIN may be challenging, the experiment design offers valuable insights to learn from

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Nice research article. To start making machine learning models, start with Big data and machine learning based model dataset. It comes under model category,


---

### 技术对话片段 62 (原帖: Recipe for Quantitative Trading with Machine Learning)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Recipe for Quantitative Trading with Machine Learning_25238156762135.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Impressive neural network structure proposed for extracting trading signals. While replication on BRAIN may be challenging, the experiment design offers valuable insights to learn from

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Key contributions of the paper include:

- Using  **recurrent neural networks (RNNs)**  for market return forecasting.
- Proposing an algorithm to simultaneously predict price levels and directions.
- Introducing autonomous pattern generation to learn traditional analyst-defined shapes.
- Applying  **complex network analysis**  to detect stock price fluctuation patterns.


---

### 技术对话片段 63 (原帖: Reduce correlation by combining some fields from other datasets)
- **原帖链接**: [Commented] Reduce correlation by combining some fields from other datasets.md
- **时间**: 1年前

**提问/主帖背景 (LN92324)**:
Hi everyone. While generating alpha I found that some datasets have much higher correlations than others. Should I reduce the correlations of those alphas by combining some Fields from other datasets in the same category? Or from other datasets in different categories? Will this cause performance degradation on the OS?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Combining alphas in order to reduce correlation is a better way than overfitting the alphas but still not the best way.Try to use single dataset alphas and if you are forced to use to combine alphas ,then combine alphas using the same dataset


---

### 技术对话片段 64 (原帖: Reduce correlation by combining some fields from other datasets)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Reduce correlation by combining some fields from other datasets_27630690341399.md
- **时间**: 1年前

**提问/主帖背景 (LN92324)**:
Hi everyone. While generating alpha I found that some datasets have much higher correlations than others. Should I reduce the correlations of those alphas by combining some Fields from other datasets in the same category? Or from other datasets in different categories? Will this cause performance degradation on the OS?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Combining alphas in order to reduce correlation is a better way than overfitting the alphas but still not the best way.Try to use single dataset alphas and if you are forced to use to combine alphas ,then combine alphas using the same dataset


---

### 技术对话片段 65 (原帖: Reduce of Prodution Corelation.)
- **原帖链接**: [Commented] Reduce of Prodution Corelation.md
- **时间**: 1年前

**提问/主帖背景 (PT88153)**:
Hey Community, Can anyone explain what are the best practice to reduce thr production corelation in regular alpha.

**顾问 AM60509 (Rank 61) 的解答与建议**:
1.Try using different operators under the same category type like ts_quantile,ts_zscore,ts_scale,ts_rank

2.Try using same alpha in less explored regions like China,GLB,Taiwan etc.

3.Try using different neutralization settings

4.If you are using group_cartesian_product,try different grouping category.


---

### 技术对话片段 66 (原帖: Reduce of Prodution Corelation.)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Reduce of Prodution Corelation_29220154233367.md
- **时间**: 1年前

**提问/主帖背景 (PT88153)**:
Hey Community, Can anyone explain what are the best practice to reduce thr production corelation in regular alpha.

**顾问 AM60509 (Rank 61) 的解答与建议**:
1.Try using different operators under the same category type like ts_quantile,ts_zscore,ts_scale,ts_rank

2.Try using same alpha in less explored regions like China,GLB,Taiwan etc.

3.Try using different neutralization settings

4.If you are using group_cartesian_product,try different grouping category.


---

### 技术对话片段 67 (原帖: reducing production correlation without reducing sharpe or fitness much)
- **原帖链接**: [Commented] reducing production correlation without reducing sharpe or fitness much.md
- **时间**: 1年前

**提问/主帖背景 (SM60004)**:
How to reduce production correlation from 0.9 to 0.6 without reducing sharpe or fitness much. If we should use grouping, how to use that...not able to understand

**顾问 AM60509 (Rank 61) 的解答与建议**:
To reduce prod correlation,one can alter neutralization settings .Altering decay settings also helps.Use different fields to group the data using group rank , group neutralize operators


---

### 技术对话片段 68 (原帖: reducing production correlation without reducing sharpe or fitness much)
- **原帖链接**: https://support.worldquantbrain.com[Commented] reducing production correlation without reducing sharpe or fitness much_19609241215511.md
- **时间**: 1年前

**提问/主帖背景 (SM60004)**:
How to reduce production correlation from 0.9 to 0.6 without reducing sharpe or fitness much. If we should use grouping, how to use that...not able to understand

**顾问 AM60509 (Rank 61) 的解答与建议**:
To reduce prod correlation,one can alter neutralization settings .Altering decay settings also helps.Use different fields to group the data using group rank , group neutralize operators


---

### 技术对话片段 69 (原帖: Regarding Research Paper)
- **原帖链接**: [Commented] Regarding Research Paper.md
- **时间**: 1年前

**提问/主帖背景 (AP57950)**:
There must be a detailed approach of studying any research paper, and applying it in the alpha models. The platform must initiate few related videos.

**顾问 AM60509 (Rank 61) 的解答与建议**:
**Before Reading :**

- Understand the concept of the operators (time series, non-time series and group operators). This helps to get the sense of the functionality and power of the operators to combine later .

**Read :**

- Read Abstract, Introduction, Conclusion and then Main body
- The implementation of the paper into an alpha may not be straightforward , but you will still be able to understand ideas and concepts that will help you build better alphas

**Formulate :**

- Formulate the idea in the sense of if-then rules, combine with your knowledge of the operators and data fields


---

### 技术对话片段 70 (原帖: Regarding Research Paper)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Regarding Research Paper_28409449721879.md
- **时间**: 1年前

**提问/主帖背景 (AP57950)**:
There must be a detailed approach of studying any research paper, and applying it in the alpha models. The platform must initiate few related videos.

**顾问 AM60509 (Rank 61) 的解答与建议**:
**Before Reading :**

- Understand the concept of the operators (time series, non-time series and group operators). This helps to get the sense of the functionality and power of the operators to combine later .

**Read :**

- Read Abstract, Introduction, Conclusion and then Main body
- The implementation of the paper into an alpha may not be straightforward , but you will still be able to understand ideas and concepts that will help you build better alphas

**Formulate :**

- Formulate the idea in the sense of if-then rules, combine with your knowledge of the operators and data fields


---

### 技术对话片段 71 (原帖: Regarding the turnover.)
- **原帖链接**: [Commented] Regarding the turnover.md
- **时间**: 1年前

**提问/主帖背景 (PT88153)**:
Hey Community, can anyone suggest what are best bracket for the  **turnover** is best ?

**顾问 AM60509 (Rank 61) 的解答与建议**:
It is a good practice to keep the turnover  **below 30%** . So you can keep your turnover window between  **10% to 30%.One can use trade_when operator to reduce turnover .Use of ts_target_tvr_hump can also be employed to reduce turnover to the desired range**


---

### 技术对话片段 72 (原帖: Regarding the turnover.)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Regarding the turnover_29256018448279.md
- **时间**: 1年前

**提问/主帖背景 (PT88153)**:
Hey Community, can anyone suggest what are best bracket for the  **turnover** is best ?

**顾问 AM60509 (Rank 61) 的解答与建议**:
It is a good practice to keep the turnover  **below 30%** . So you can keep your turnover window between  **10% to 30%.One can use trade_when operator to reduce turnover .Use of ts_target_tvr_hump can also be employed to reduce turnover to the desired range**


---

### 技术对话片段 73 (原帖: Some of my learnings)
- **原帖链接**: [Commented] Some of my learnings.md
- **时间**: 1年前

**提问/主帖背景 (RP25658)**:
I have been using BRAIN platform from last 10 to 15 days now, I would like to share some of my learnings which might help newly joined users to start creating profitable alphas.

- After achieving min sharpe and fitness, improve returns

- consider using rank, ts_rank, zscore and ts_zscore to remove outliers

- Momentum Alphas
    - BRAIN platform are set to long-short neutral setting, makes it harder to capture momentum signal compared to long-only alphas
    - Use trade_when() or conditional operators
    - Set neutralization to "None"
    - Less volatile stocks perform well in momentum Alphas
    - Use liquid universe like TOP500
    - Volatility can be captured when using datasets from “Systematic Risk Metrics”

- Using hump operation
    - Each instrument could have a variable threshold based on liquidity/market-cap/volatility of the stock
    - Can use single threshold value for a group (subindustry/sector/custom group).
    - Increasing the threshold values either uniformly or not uniformly after ranking the instruments on the basis of a few factors (market-cap/volatility) can help.

- Evaluating new datasets
    - Simulate the below expression in “None” neutralization and decay 0 setting
    - datafield

- Weight Test Failure
    - Test is ought to fail when number of stocks is < 10
    - Use rank(), group_rank(), zscore, scale to handle the outliers
    - Use ts_backfill() or group_backfill() to increase the number of tradable stocks

- Alpha Development Cycle
    - Alpha idea → Finding operators and data → Simulate → Revise

- Working on News Dataset
    - trade_when(ed, alpha, exit)
    - ed: event detection, identify the day on which news related to that stock is occurring (by checking NaN)
    - alpha: position can be taken based on percent change after news
    - holding: can hold for remaining days
    - Example: news_tot_ticks, news_pct_5_min,-1, news_tot_ticks is non-NaN when news has occurred
    - NOTE: There are different ways for event detection, alpha and exit (like decaying alpha or setting threshold)

- Setting predetermined Stop loss
    - Exiting at 10% profit or loss
    - close_at_event = trade_when(event, close, -1);
    - alpha = trade_when(event, signal, abs(close - close_at_event) / close > .1);
    - alpha

- How to increase returns?
    - increase volatility of your alpha
    - work with smaller universe
    - increase turnover
    - try using news and analyst datasets

- Alpha signal smoothing
    - smoothing means lessen effects of extreme values
    - Transformational Operators: arc_tan, tanh, log, s_log_1p, sigmoid
    - Cross sectional Operators: zscore, rank
    - Time series Operators: ts_mean(alpha, N), ts_decay_linear...

- Move out of COMFORT ZONE
    - Working with the same data fields will not get you value adding alphas
    - Explore new datasets

- Creating Delay-0 Alphas
    - Use D0 data fields when using news or sentiment dataset
    - D0 works good for smaller universe (TOP500)
    - D0 works well for low turnover alphas; using fundamental or analyst dataset

- Reduce correlation
    - Use different operators
    - Use different grouping
    - Use alternative operators like high/open/low instead of close

- How to get Higher Sharpe?
    - Increase returns
    - Reduce volatility

- Day count
    - 22 is one month
    - 66 is one quarter
    - 264 is one year

- Trading top or bottom quintile/decile improves performance
    - rank(alpha) >= 0.8 ? 1 : (rank(alpha) <= 0.2 ? -1 : 0)
    - Buy top 20% and sell bottom 20%
    - You may have to increase the universe to pass the "Weight Test"

- Trading volume (liquidity) is average turnover
    - turnover = volume / sharesout

- Use ts_mean() or ts_sum() to reduce turnover when using a volatile data field

- To increase turnover you can add below expression depending on the situation
    > rank(mdf_pgn) or 
    > rank(-mdf_pgn)

- When not able to pass sharpe or fitness test due to marginal difference
    > Use ts_mean instead of ts_sum and vice versa

*This would be a developing list, will keep this updated as I learn more from this platform*

**顾问 AM60509 (Rank 61) 的解答与建议**:
In my opinion, it is easier to create alphas in lesser known regions like China, Taiwan, Korea as compared to USA due to correlation factor. So I suggest start with fundamental datasets like price volume, model, fundamental metric in these regions.


---

### 技术对话片段 74 (原帖: Some of my learnings)
- **原帖链接**: [Commented] Some of my learnings.md
- **时间**: 1年前

**提问/主帖背景 (RP25658)**:
I have been using BRAIN platform from last 10 to 15 days now, I would like to share some of my learnings which might help newly joined users to start creating profitable alphas.

- After achieving min sharpe and fitness, improve returns

- consider using rank, ts_rank, zscore and ts_zscore to remove outliers

- Momentum Alphas
    - BRAIN platform are set to long-short neutral setting, makes it harder to capture momentum signal compared to long-only alphas
    - Use trade_when() or conditional operators
    - Set neutralization to "None"
    - Less volatile stocks perform well in momentum Alphas
    - Use liquid universe like TOP500
    - Volatility can be captured when using datasets from “Systematic Risk Metrics”

- Using hump operation
    - Each instrument could have a variable threshold based on liquidity/market-cap/volatility of the stock
    - Can use single threshold value for a group (subindustry/sector/custom group).
    - Increasing the threshold values either uniformly or not uniformly after ranking the instruments on the basis of a few factors (market-cap/volatility) can help.

- Evaluating new datasets
    - Simulate the below expression in “None” neutralization and decay 0 setting
    - datafield

- Weight Test Failure
    - Test is ought to fail when number of stocks is < 10
    - Use rank(), group_rank(), zscore, scale to handle the outliers
    - Use ts_backfill() or group_backfill() to increase the number of tradable stocks

- Alpha Development Cycle
    - Alpha idea → Finding operators and data → Simulate → Revise

- Working on News Dataset
    - trade_when(ed, alpha, exit)
    - ed: event detection, identify the day on which news related to that stock is occurring (by checking NaN)
    - alpha: position can be taken based on percent change after news
    - holding: can hold for remaining days
    - Example: news_tot_ticks, news_pct_5_min,-1, news_tot_ticks is non-NaN when news has occurred
    - NOTE: There are different ways for event detection, alpha and exit (like decaying alpha or setting threshold)

- Setting predetermined Stop loss
    - Exiting at 10% profit or loss
    - close_at_event = trade_when(event, close, -1);
    - alpha = trade_when(event, signal, abs(close - close_at_event) / close > .1);
    - alpha

- How to increase returns?
    - increase volatility of your alpha
    - work with smaller universe
    - increase turnover
    - try using news and analyst datasets

- Alpha signal smoothing
    - smoothing means lessen effects of extreme values
    - Transformational Operators: arc_tan, tanh, log, s_log_1p, sigmoid
    - Cross sectional Operators: zscore, rank
    - Time series Operators: ts_mean(alpha, N), ts_decay_linear...

- Move out of COMFORT ZONE
    - Working with the same data fields will not get you value adding alphas
    - Explore new datasets

- Creating Delay-0 Alphas
    - Use D0 data fields when using news or sentiment dataset
    - D0 works good for smaller universe (TOP500)
    - D0 works well for low turnover alphas; using fundamental or analyst dataset

- Reduce correlation
    - Use different operators
    - Use different grouping
    - Use alternative operators like high/open/low instead of close

- How to get Higher Sharpe?
    - Increase returns
    - Reduce volatility

- Day count
    - 22 is one month
    - 66 is one quarter
    - 264 is one year

- Trading top or bottom quintile/decile improves performance
    - rank(alpha) >= 0.8 ? 1 : (rank(alpha) <= 0.2 ? -1 : 0)
    - Buy top 20% and sell bottom 20%
    - You may have to increase the universe to pass the "Weight Test"

- Trading volume (liquidity) is average turnover
    - turnover = volume / sharesout

- Use ts_mean() or ts_sum() to reduce turnover when using a volatile data field

- To increase turnover you can add below expression depending on the situation
    > rank(mdf_pgn) or 
    > rank(-mdf_pgn)

- When not able to pass sharpe or fitness test due to marginal difference
    > Use ts_mean instead of ts_sum and vice versa

*This would be a developing list, will keep this updated as I learn more from this platform*

**顾问 AM60509 (Rank 61) 的解答与建议**:
[DK20528](/hc/en-us/profiles/24602396283031-DK20528)

Use operators which can substitute each other without decreasing performance. zscore, quantile, rank, scale can be used interchangeably with minor changes to performance but drastic reduction of correlation drastically. Use of different grouping fields can also reduce correlation


---

### 技术对话片段 75 (原帖: Some of my learnings)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Some of my learnings_17542707569815.md
- **时间**: 1年前

**提问/主帖背景 (RP25658)**:
I have been using BRAIN platform from last 10 to 15 days now, I would like to share some of my learnings which might help newly joined users to start creating profitable alphas.

- After achieving min sharpe and fitness, improve returns

- consider using rank, ts_rank, zscore and ts_zscore to remove outliers

- Momentum Alphas
    - BRAIN platform are set to long-short neutral setting, makes it harder to capture momentum signal compared to long-only alphas
    - Use trade_when() or conditional operators
    - Set neutralization to "None"
    - Less volatile stocks perform well in momentum Alphas
    - Use liquid universe like TOP500
    - Volatility can be captured when using datasets from “Systematic Risk Metrics”

- Using hump operation
    - Each instrument could have a variable threshold based on liquidity/market-cap/volatility of the stock
    - Can use single threshold value for a group (subindustry/sector/custom group).
    - Increasing the threshold values either uniformly or not uniformly after ranking the instruments on the basis of a few factors (market-cap/volatility) can help.

- Evaluating new datasets
    - Simulate the below expression in “None” neutralization and decay 0 setting
    - datafield

- Weight Test Failure
    - Test is ought to fail when number of stocks is < 10
    - Use rank(), group_rank(), zscore, scale to handle the outliers
    - Use ts_backfill() or group_backfill() to increase the number of tradable stocks

- Alpha Development Cycle
    - Alpha idea → Finding operators and data → Simulate → Revise

- Working on News Dataset
    - trade_when(ed, alpha, exit)
    - ed: event detection, identify the day on which news related to that stock is occurring (by checking NaN)
    - alpha: position can be taken based on percent change after news
    - holding: can hold for remaining days
    - Example: news_tot_ticks, news_pct_5_min,-1, news_tot_ticks is non-NaN when news has occurred
    - NOTE: There are different ways for event detection, alpha and exit (like decaying alpha or setting threshold)

- Setting predetermined Stop loss
    - Exiting at 10% profit or loss
    - close_at_event = trade_when(event, close, -1);
    - alpha = trade_when(event, signal, abs(close - close_at_event) / close > .1);
    - alpha

- How to increase returns?
    - increase volatility of your alpha
    - work with smaller universe
    - increase turnover
    - try using news and analyst datasets

- Alpha signal smoothing
    - smoothing means lessen effects of extreme values
    - Transformational Operators: arc_tan, tanh, log, s_log_1p, sigmoid
    - Cross sectional Operators: zscore, rank
    - Time series Operators: ts_mean(alpha, N), ts_decay_linear...

- Move out of COMFORT ZONE
    - Working with the same data fields will not get you value adding alphas
    - Explore new datasets

- Creating Delay-0 Alphas
    - Use D0 data fields when using news or sentiment dataset
    - D0 works good for smaller universe (TOP500)
    - D0 works well for low turnover alphas; using fundamental or analyst dataset

- Reduce correlation
    - Use different operators
    - Use different grouping
    - Use alternative operators like high/open/low instead of close

- How to get Higher Sharpe?
    - Increase returns
    - Reduce volatility

- Day count
    - 22 is one month
    - 66 is one quarter
    - 264 is one year

- Trading top or bottom quintile/decile improves performance
    - rank(alpha) >= 0.8 ? 1 : (rank(alpha) <= 0.2 ? -1 : 0)
    - Buy top 20% and sell bottom 20%
    - You may have to increase the universe to pass the "Weight Test"

- Trading volume (liquidity) is average turnover
    - turnover = volume / sharesout

- Use ts_mean() or ts_sum() to reduce turnover when using a volatile data field

- To increase turnover you can add below expression depending on the situation
    > rank(mdf_pgn) or 
    > rank(-mdf_pgn)

- When not able to pass sharpe or fitness test due to marginal difference
    > Use ts_mean instead of ts_sum and vice versa

*This would be a developing list, will keep this updated as I learn more from this platform*

**顾问 AM60509 (Rank 61) 的解答与建议**:
In my opinion, it is easier to create alphas in lesser known regions like China, Taiwan, Korea as compared to USA due to correlation factor. So I suggest start with fundamental datasets like price volume, model, fundamental metric in these regions.


---

### 技术对话片段 76 (原帖: Some of my learnings)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Some of my learnings_17542707569815.md
- **时间**: 1年前

**提问/主帖背景 (RP25658)**:
I have been using BRAIN platform from last 10 to 15 days now, I would like to share some of my learnings which might help newly joined users to start creating profitable alphas.

- After achieving min sharpe and fitness, improve returns

- consider using rank, ts_rank, zscore and ts_zscore to remove outliers

- Momentum Alphas
    - BRAIN platform are set to long-short neutral setting, makes it harder to capture momentum signal compared to long-only alphas
    - Use trade_when() or conditional operators
    - Set neutralization to "None"
    - Less volatile stocks perform well in momentum Alphas
    - Use liquid universe like TOP500
    - Volatility can be captured when using datasets from “Systematic Risk Metrics”

- Using hump operation
    - Each instrument could have a variable threshold based on liquidity/market-cap/volatility of the stock
    - Can use single threshold value for a group (subindustry/sector/custom group).
    - Increasing the threshold values either uniformly or not uniformly after ranking the instruments on the basis of a few factors (market-cap/volatility) can help.

- Evaluating new datasets
    - Simulate the below expression in “None” neutralization and decay 0 setting
    - datafield

- Weight Test Failure
    - Test is ought to fail when number of stocks is < 10
    - Use rank(), group_rank(), zscore, scale to handle the outliers
    - Use ts_backfill() or group_backfill() to increase the number of tradable stocks

- Alpha Development Cycle
    - Alpha idea → Finding operators and data → Simulate → Revise

- Working on News Dataset
    - trade_when(ed, alpha, exit)
    - ed: event detection, identify the day on which news related to that stock is occurring (by checking NaN)
    - alpha: position can be taken based on percent change after news
    - holding: can hold for remaining days
    - Example: news_tot_ticks, news_pct_5_min,-1, news_tot_ticks is non-NaN when news has occurred
    - NOTE: There are different ways for event detection, alpha and exit (like decaying alpha or setting threshold)

- Setting predetermined Stop loss
    - Exiting at 10% profit or loss
    - close_at_event = trade_when(event, close, -1);
    - alpha = trade_when(event, signal, abs(close - close_at_event) / close > .1);
    - alpha

- How to increase returns?
    - increase volatility of your alpha
    - work with smaller universe
    - increase turnover
    - try using news and analyst datasets

- Alpha signal smoothing
    - smoothing means lessen effects of extreme values
    - Transformational Operators: arc_tan, tanh, log, s_log_1p, sigmoid
    - Cross sectional Operators: zscore, rank
    - Time series Operators: ts_mean(alpha, N), ts_decay_linear...

- Move out of COMFORT ZONE
    - Working with the same data fields will not get you value adding alphas
    - Explore new datasets

- Creating Delay-0 Alphas
    - Use D0 data fields when using news or sentiment dataset
    - D0 works good for smaller universe (TOP500)
    - D0 works well for low turnover alphas; using fundamental or analyst dataset

- Reduce correlation
    - Use different operators
    - Use different grouping
    - Use alternative operators like high/open/low instead of close

- How to get Higher Sharpe?
    - Increase returns
    - Reduce volatility

- Day count
    - 22 is one month
    - 66 is one quarter
    - 264 is one year

- Trading top or bottom quintile/decile improves performance
    - rank(alpha) >= 0.8 ? 1 : (rank(alpha) <= 0.2 ? -1 : 0)
    - Buy top 20% and sell bottom 20%
    - You may have to increase the universe to pass the "Weight Test"

- Trading volume (liquidity) is average turnover
    - turnover = volume / sharesout

- Use ts_mean() or ts_sum() to reduce turnover when using a volatile data field

- To increase turnover you can add below expression depending on the situation
    > rank(mdf_pgn) or 
    > rank(-mdf_pgn)

- When not able to pass sharpe or fitness test due to marginal difference
    > Use ts_mean instead of ts_sum and vice versa

*This would be a developing list, will keep this updated as I learn more from this platform*

**顾问 AM60509 (Rank 61) 的解答与建议**:
[DK20528](/hc/en-us/profiles/24602396283031-DK20528)

Use operators which can substitute each other without decreasing performance. zscore, quantile, rank, scale can be used interchangeably with minor changes to performance but drastic reduction of correlation drastically. Use of different grouping fields can also reduce correlation


---

### 技术对话片段 77 (原帖: Optimize portfolio allocation to limit the number of positions)
- **原帖链接**: [Commented] Struggling to get decent Sharpe Without High Turnover.md
- **时间**: 1年前

**提问/主帖背景 (AJ82399)**:
How to reduce turnover while keeping sharpe in the same range?

**顾问 AM60509 (Rank 61) 的解答与建议**:
You can use ts_target_tvr_hump to reduce turnover. Alternatively you can use trade_when operator to reduce turnover. I personally use ts_target_tvr_hump


---

### 技术对话片段 78 (原帖: Optimize portfolio allocation to limit the number of positions)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Struggling to get decent Sharpe Without High Turnover_26863694299799.md
- **时间**: 1年前

**提问/主帖背景 (AJ82399)**:
How to reduce turnover while keeping sharpe in the same range?

**顾问 AM60509 (Rank 61) 的解答与建议**:
You can use ts_target_tvr_hump to reduce turnover. Alternatively you can use trade_when operator to reduce turnover. I personally use ts_target_tvr_hump


---

### 技术对话片段 79 (原帖: The 101 ways to measure portfolio performance.)
- **原帖链接**: [Commented] The 101 ways to measure portfolio performance.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Proposes multiple approaches to evaluate portfolio performance, can be used as machine-driven research's fitness function.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thanks for the article.
The paper categorizes performance measures into key classifications based on their computational approach:

Some of them are:-

Asset Selection vs. Market Timing: Differentiating between measures focused on picking individual assets and those evaluating timing decisions.
Standardized vs. Individualized: Examining generalizable metrics versus those tailored to specific portfolios or objectives.


---

### 技术对话片段 80 (原帖: The 101 ways to measure portfolio performance.)
- **原帖链接**: https://support.worldquantbrain.com[Commented] The 101 ways to measure portfolio performance_25238156125207.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Proposes multiple approaches to evaluate portfolio performance, can be used as machine-driven research's fitness function.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thanks for the article.
The paper categorizes performance measures into key classifications based on their computational approach:

Some of them are:-

Asset Selection vs. Market Timing: Differentiating between measures focused on picking individual assets and those evaluating timing decisions.
Standardized vs. Individualized: Examining generalizable metrics versus those tailored to specific portfolios or objectives.


---

### 技术对话片段 81 (原帖: THE NEW  PYRAMID COUNT UPDATE)
- **原帖链接**: https://support.worldquantbrain.com[Commented] THE NEW  PYRAMID COUNT UPDATE_31665283177623.md
- **时间**: 1年前

**提问/主帖背景 (CM45657)**:
### **Thresholds for Q2 2025 (One-Time Change):**

- **Expert:**  10 pyramids → unchanged
- **Master:**   *30 → 20 pyramids*
- **Grandmaster:**   *60 → 50 pyramids*

### **Key Rule Changes Effective April 1, 2025:**

- **One Alpha can now contribute to a maximum of 2 Genius pyramids.**
- **If an Alpha is used in more than 2 pyramids** , it will  **not count**  toward any Genius pyramids.
- However, such Alphas  **still count**  toward:
  - Base payments
- signal
- - Combined Alpha performance
  - Tie-breaker criteria

### **Neutralization Fields Exception:**

- Neutralizations (e.g., sector, industry, exchange, etc.)  **do NOT**  count as extra pyramids.
- Example: If an alpha uses 2 pyramids + subindustry neutralization →  **still eligible**  for Genius pyramids.

### **No Change to Payments:**

- Pyramid multipliers and base payment calculations are  **unchanged** .

Want help optimizing your alphas under this new rule

**顾问 AM60509 (Rank 61) 的解答与建议**:
Each Alpha can now contribute to a maximum of two Genius pyramids. If used in more than two, it won’t count toward Genius pyramid thresholds, though it still contributes to base payments, signal strength, and tie-breaker metrics.


---

### 技术对话片段 82 (原帖: Time Spent on WQ Alphas)
- **原帖链接**: [Commented] Time Spent on WQ Alphas.md
- **时间**: 1年前

**提问/主帖背景 (NH16784)**:
Hi,

Since the start of the Genius program, I've been spending a significant amount of time on WQ. I typically dedicate more than 4 hours a day to fixing 4 alphas for submission. For challenging datasets, this time can extend beyond 6 hours a day.

By " **fixing** ," I mean refining alphas that already exhibit acceptable performance (Sharpe ratio and 2-year Sharpe ratio greater than 1.2) to meet the submission requirements.

I'm curious about the average time you spend on this process as well. Additionally, I would greatly appreciate any suggestions on how to optimize the efficiency of this "fixing" process.

Thank you for your time and insights.

**顾问 AM60509 (Rank 61) 的解答与建议**:
I have personally put all nighters to create 4 alphas and 1 super alpha .There is lot of dedication involved in the process of creating alphas.Sometimes a good alpha can be cracked in a matter of minutes but sometimes it can extend to few hours.

Use of Brain API can help reduce research time


---

### 技术对话片段 83 (原帖: Time Spent on WQ Alphas)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Time Spent on WQ Alphas_29271712184471.md
- **时间**: 1年前

**提问/主帖背景 (NH16784)**:
Hi,

Since the start of the Genius program, I've been spending a significant amount of time on WQ. I typically dedicate more than 4 hours a day to fixing 4 alphas for submission. For challenging datasets, this time can extend beyond 6 hours a day.

By " **fixing** ," I mean refining alphas that already exhibit acceptable performance (Sharpe ratio and 2-year Sharpe ratio greater than 1.2) to meet the submission requirements.

I'm curious about the average time you spend on this process as well. Additionally, I would greatly appreciate any suggestions on how to optimize the efficiency of this "fixing" process.

Thank you for your time and insights.

**顾问 AM60509 (Rank 61) 的解答与建议**:
I have personally put all nighters to create 4 alphas and 1 super alpha .There is lot of dedication involved in the process of creating alphas.Sometimes a good alpha can be cracked in a matter of minutes but sometimes it can extend to few hours.

Use of Brain API can help reduce research time


---

### 技术对话片段 84 (原帖: USE OF DATA ANALYSIS TOOLS IN QUANTITATIVE TRADING)
- **原帖链接**: [Commented] USE OF DATA ANALYSIS TOOLS IN QUANTITATIVE TRADING.md
- **时间**: 1年前

**提问/主帖背景 (AC34118)**:
### **Data Analysis and Visualization Libraries** :

- **Pandas** : For handling and analyzing time series data, working with data frames.
- **NumPy** : Used for numerical operations and managing large datasets of numbers.
- **Matplotlib**  &  **Seaborn** : For creating static, animated, and interactive visualizations. They are especially useful in visualizing stock price trends, histograms, and scatter plots.
- **Plotly** : A more advanced visualization tool that allows for interactive charts and plots, useful for displaying large datasets interactively.

### **Quantitative and Statistical Libraries** :

- **SciPy** : Used for advanced statistical functions such as optimization, integration, interpolation, eigenvalue problems, and more.
- **Statsmodels** : Provides classes and functions for statistical models, including time series analysis, regression models, and hypothesis testing.
- **TA-Lib** : A library for technical analysis that includes over 150 indicators like moving averages, RSI, MACD, and more.
- **PyPortfolioOpt** : For portfolio optimization, focusing on risk-return analysis, mean-variance optimization, and other advanced techniques.

### **Backtesting Frameworks** :

- **Backtrader** : A Python-based framework for backtesting trading strategies. It supports event-driven systems, live trading, and paper trading.
- **QuantConnect** : A cloud-based algorithmic trading platform that allows for backtesting strategies in multiple asset classes (equities, forex, cryptocurrencies, etc.).
- **Zipline** : An open-source backtesting library built by Quantopian. It’s used for simulating and testing algorithmic trading strategies in Python.
- **Quantlib** : A library for quantitative finance, providing tools for pricing derivatives, calculating risk metrics, and other financial applications.

### **Machine Learning and AI Libraries** :

- **Scikit-learn** : A versatile library for machine learning that provides tools for classification, regression, clustering, and more.
- **TensorFlow**  &  **Keras** : Deep learning libraries often used for complex market prediction tasks, such as using neural networks to forecast asset prices or optimize portfolios.
- **XGBoost** : A powerful library for gradient boosting, widely used in structured data prediction tasks like asset price forecasting.
- **LightGBM** : Another gradient boosting framework optimized for speed and performance, especially for large datasets.
- **Fast.ai** : A library that simplifies deep learning and machine learning workflows, often used in algorithmic trading research.

### **Database Management Systems** :

- **SQL** : Structured Query Language is essential for managing relational databases, querying historical market data, and integrating with trading systems.
- **MongoDB** : A NoSQL database that stores data in flexible, JSON-like documents, often used for unstructured or semi-structured data like market sentiment or social media feeds.
- **PostgreSQL** : A powerful relational database management system that’s often used for large-scale financial data analysis.

### **Data Providers and APIs** :

- **Quandl** : Provides access to financial, economic, and alternative datasets, and can be integrated with Python for data analysis.
- **Alpha Vantage** : Offers free and premium APIs for stock data, forex, and cryptocurrencies, often used in algorithmic trading strategies.
- **Yahoo Finance API** : Provides historical and real-time financial data, which can be accessed through libraries like  `yfinance`  in Python.
- **Bloomberg Terminal** : Offers comprehensive financial data, news, and analysis tools, widely used by institutional traders.
- **Interactive Brokers API** : Used to access real-time market data, execute trades, and perform other trading functions programmatically.

### **Cloud Platforms for Data Storage and Processing** :

- **AWS (Amazon Web Services)** : Provides cloud storage, computing power (e.g., EC2), and big data processing tools (e.g., AWS Lambda, Redshift).
- **Google Cloud Platform (GCP)** : Offers similar services, including BigQuery for large-scale data analysis and machine learning models.
- **Microsoft Azure** : Provides a variety of data storage and computing tools suitable for quantitative trading algorithms and data analysis.

### **High-Frequency Trading (HFT) Tools** :

- **Kdb+/q** : A high-performance time-series database and query language designed for handling massive datasets, commonly used in HFT environments.
- **FIX Protocol** : A messaging protocol used for electronic trading, ensuring fast and efficient order execution in algorithmic and high-frequency trading.

### **Risk Management Tools** :

- **RiskMetrics** : A risk management tool used for portfolio risk analysis, including value-at-risk (VaR), stress testing, and more.
- **VaR (Value-at-Risk) Models** : Calculating the potential loss in value of an asset or portfolio based on historical or simulated data.
- **Monte Carlo Simulation** : A method used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables.

### **Quantitative Trading Platforms** :

- **MetaTrader 4/5 (MT4/MT5)** : Popular among retail forex traders, these platforms offer backtesting, strategy development, and execution tools.
- **TradeStation** : A platform for strategy development and backtesting in stocks, options, and futures markets.
- **NinjaTrader** : A trading platform with robust backtesting and charting tools, often used in futures and forex markets.

These tools and libraries help quantitative traders analyze large datasets, build predictive models, optimize strategies, manage risk, and execute trades. The choice of tool depends on the type of strategy being developed, the asset classes being traded, and the trader's technical expertise.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Great rundown of popular backtesting frameworks! Backtrader, QuantConnect, Zipline, and Quantlib offer a range of tools for testing and validating trading strategies, from event-driven systems to cloud-based platforms and open-source libraries.


---

### 技术对话片段 85 (原帖: USE OF DATA ANALYSIS TOOLS IN QUANTITATIVE TRADING)
- **原帖链接**: https://support.worldquantbrain.com[Commented] USE OF DATA ANALYSIS TOOLS IN QUANTITATIVE TRADING_29269838227735.md
- **时间**: 1年前

**提问/主帖背景 (AC34118)**:
### **Data Analysis and Visualization Libraries** :

- **Pandas** : For handling and analyzing time series data, working with data frames.
- **NumPy** : Used for numerical operations and managing large datasets of numbers.
- **Matplotlib**  &  **Seaborn** : For creating static, animated, and interactive visualizations. They are especially useful in visualizing stock price trends, histograms, and scatter plots.
- **Plotly** : A more advanced visualization tool that allows for interactive charts and plots, useful for displaying large datasets interactively.

### **Quantitative and Statistical Libraries** :

- **SciPy** : Used for advanced statistical functions such as optimization, integration, interpolation, eigenvalue problems, and more.
- **Statsmodels** : Provides classes and functions for statistical models, including time series analysis, regression models, and hypothesis testing.
- **TA-Lib** : A library for technical analysis that includes over 150 indicators like moving averages, RSI, MACD, and more.
- **PyPortfolioOpt** : For portfolio optimization, focusing on risk-return analysis, mean-variance optimization, and other advanced techniques.

### **Backtesting Frameworks** :

- **Backtrader** : A Python-based framework for backtesting trading strategies. It supports event-driven systems, live trading, and paper trading.
- **QuantConnect** : A cloud-based algorithmic trading platform that allows for backtesting strategies in multiple asset classes (equities, forex, cryptocurrencies, etc.).
- **Zipline** : An open-source backtesting library built by Quantopian. It’s used for simulating and testing algorithmic trading strategies in Python.
- **Quantlib** : A library for quantitative finance, providing tools for pricing derivatives, calculating risk metrics, and other financial applications.

### **Machine Learning and AI Libraries** :

- **Scikit-learn** : A versatile library for machine learning that provides tools for classification, regression, clustering, and more.
- **TensorFlow**  &  **Keras** : Deep learning libraries often used for complex market prediction tasks, such as using neural networks to forecast asset prices or optimize portfolios.
- **XGBoost** : A powerful library for gradient boosting, widely used in structured data prediction tasks like asset price forecasting.
- **LightGBM** : Another gradient boosting framework optimized for speed and performance, especially for large datasets.
- **Fast.ai** : A library that simplifies deep learning and machine learning workflows, often used in algorithmic trading research.

### **Database Management Systems** :

- **SQL** : Structured Query Language is essential for managing relational databases, querying historical market data, and integrating with trading systems.
- **MongoDB** : A NoSQL database that stores data in flexible, JSON-like documents, often used for unstructured or semi-structured data like market sentiment or social media feeds.
- **PostgreSQL** : A powerful relational database management system that’s often used for large-scale financial data analysis.

### **Data Providers and APIs** :

- **Quandl** : Provides access to financial, economic, and alternative datasets, and can be integrated with Python for data analysis.
- **Alpha Vantage** : Offers free and premium APIs for stock data, forex, and cryptocurrencies, often used in algorithmic trading strategies.
- **Yahoo Finance API** : Provides historical and real-time financial data, which can be accessed through libraries like  `yfinance`  in Python.
- **Bloomberg Terminal** : Offers comprehensive financial data, news, and analysis tools, widely used by institutional traders.
- **Interactive Brokers API** : Used to access real-time market data, execute trades, and perform other trading functions programmatically.

### **Cloud Platforms for Data Storage and Processing** :

- **AWS (Amazon Web Services)** : Provides cloud storage, computing power (e.g., EC2), and big data processing tools (e.g., AWS Lambda, Redshift).
- **Google Cloud Platform (GCP)** : Offers similar services, including BigQuery for large-scale data analysis and machine learning models.
- **Microsoft Azure** : Provides a variety of data storage and computing tools suitable for quantitative trading algorithms and data analysis.

### **High-Frequency Trading (HFT) Tools** :

- **Kdb+/q** : A high-performance time-series database and query language designed for handling massive datasets, commonly used in HFT environments.
- **FIX Protocol** : A messaging protocol used for electronic trading, ensuring fast and efficient order execution in algorithmic and high-frequency trading.

### **Risk Management Tools** :

- **RiskMetrics** : A risk management tool used for portfolio risk analysis, including value-at-risk (VaR), stress testing, and more.
- **VaR (Value-at-Risk) Models** : Calculating the potential loss in value of an asset or portfolio based on historical or simulated data.
- **Monte Carlo Simulation** : A method used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables.

### **Quantitative Trading Platforms** :

- **MetaTrader 4/5 (MT4/MT5)** : Popular among retail forex traders, these platforms offer backtesting, strategy development, and execution tools.
- **TradeStation** : A platform for strategy development and backtesting in stocks, options, and futures markets.
- **NinjaTrader** : A trading platform with robust backtesting and charting tools, often used in futures and forex markets.

These tools and libraries help quantitative traders analyze large datasets, build predictive models, optimize strategies, manage risk, and execute trades. The choice of tool depends on the type of strategy being developed, the asset classes being traded, and the trader's technical expertise.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Great rundown of popular backtesting frameworks! Backtrader, QuantConnect, Zipline, and Quantlib offer a range of tools for testing and validating trading strategies, from event-driven systems to cloud-based platforms and open-source libraries.


---

### 技术对话片段 86 (原帖: Using Genetic Algorithms to Find Technical Trading Rules: A Comment on Risk Adjustment)
- **原帖链接**: [Commented] Using Genetic Algorithms to Find Technical Trading Rules A Comment on Risk Adjustment.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Genetic algorithm is a useful optimizing algorithm, and risk adjustment is an important concept in trading. This paper uses Genetic programming to do research on risk adjustment.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing this paper! The use of genetic programming to optimize trading rules highlights its adaptability for complex financial problems.

Genetic programming is indeed a powerful tool for discovering non-linear patterns in data.

Here are several strategies to address overfitting in this context:

1.Cross Validation

2.Regularization

3.Fitness Function Modification


---

### 技术对话片段 87 (原帖: Using Genetic Algorithms to Find Technical Trading Rules: A Comment on Risk Adjustment)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Using Genetic Algorithms to Find Technical Trading Rules A Comment on Risk Adjustment_25238156621975.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Genetic algorithm is a useful optimizing algorithm, and risk adjustment is an important concept in trading. This paper uses Genetic programming to do research on risk adjustment.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
Thank you for sharing this paper! The use of genetic programming to optimize trading rules highlights its adaptability for complex financial problems.

Genetic programming is indeed a powerful tool for discovering non-linear patterns in data.

Here are several strategies to address overfitting in this context:

1.Cross Validation

2.Regularization

3.Fitness Function Modification


---

### 技术对话片段 88 (原帖: Value factor & weight factor)
- **原帖链接**: [Commented] Value factor  weight factor.md
- **时间**: 1年前

**提问/主帖背景 (SV11672)**:
"What strategies or datasets would you recommend for further improving my Alpha performance, considering I have already submitted over 1700 regular and super alphas with a weight factor of 4.86?"

**顾问 AM60509 (Rank 61) 的解答与建议**:
I have submitted 250 alphas over past 4 months but my weight factor is still 0 and value factor remains at 0.5.Can anyone please suggest any methods to improve these factor so that my payouts will increase.


---

### 技术对话片段 89 (原帖: Value factor & weight factor)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Value factor  weight factor_29270495128087.md
- **时间**: 1年前

**提问/主帖背景 (SV11672)**:
"What strategies or datasets would you recommend for further improving my Alpha performance, considering I have already submitted over 1700 regular and super alphas with a weight factor of 4.86?"

**顾问 AM60509 (Rank 61) 的解答与建议**:
I have submitted 250 alphas over past 4 months but my weight factor is still 0 and value factor remains at 0.5.Can anyone please suggest any methods to improve these factor so that my payouts will increase.


---

### 技术对话片段 90 (原帖: When calculating annual return and drawdown, why do we divide by 0.5?)
- **原帖链接**: [Commented] When calculating annual return and drawdown why do we divide by 05.md
- **时间**: 1年前

**提问/主帖背景 (HD13438)**:
I did chatgpt for this, and it said that it's assumed that half of the capital would be active on average. If it was true, how would it make sense? we put the entire capital (booksize) on investment, then why would we assume only the half capital being active?

Could the reason be - we are not putting back the surplus(per day) on investment, that's why we're doubling the return (0.5 in denominator), coz we could have made more if we put that surplus too?

Also another doubt is that, I don't understand the margin formula.

Margin = Pnl / totaldollarsTraded
if it's total dollars traded(sum of all trades), then in the example given, it's shown as 40% and return shown is 11%, it won't be possible I think. So explain margin to me too. 

Thanks in advance.

**顾问 AM60509 (Rank 61) 的解答与建议**:
The assumption of dividing by 0.5 for annual return and drawdown is because in practice, not all capital is constantly in action. Some might be in cash or reserved


---

### 技术对话片段 91 (原帖: When calculating annual return and drawdown, why do we divide by 0.5?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] When calculating annual return and drawdown why do we divide by 05_27690484170391.md
- **时间**: 1年前

**提问/主帖背景 (HD13438)**:
I did chatgpt for this, and it said that it's assumed that half of the capital would be active on average. If it was true, how would it make sense? we put the entire capital (booksize) on investment, then why would we assume only the half capital being active?

Could the reason be - we are not putting back the surplus(per day) on investment, that's why we're doubling the return (0.5 in denominator), coz we could have made more if we put that surplus too?

Also another doubt is that, I don't understand the margin formula.

Margin = Pnl / totaldollarsTraded
if it's total dollars traded(sum of all trades), then in the example given, it's shown as 40% and return shown is 11%, it won't be possible I think. So explain margin to me too. 

Thanks in advance.

**顾问 AM60509 (Rank 61) 的解答与建议**:
The assumption of dividing by 0.5 for annual return and drawdown is because in practice, not all capital is constantly in action. Some might be in cash or reserved


---

### 技术对话片段 92 (原帖: Why Does Sharpe Ratio Drop in a Smaller Universe, and How to Improve It?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Why Does Sharpe Ratio Drop in a Smaller Universe and How to Improve It_30173890382487.md
- **时间**: 1年前

**提问/主帖背景 (PH56640)**:
When building an alpha, the Sub-Universe Sharpe is usually around 1.5, which is well above the 0.7 threshold. However, when testing on a smaller universe(top1000, top500, ...), the ratio (Sharpe new universe) / (Sharpe origin) often drops below 0.5. Is this reasonable? Can you suggest ways to improve the Sharpe ratio for a smaller universe?

**顾问 AM60509 (Rank 61) 的解答与建议**:
Ideally use single data set alphas to improve sub universe sharpe and reduce overfitting.

Use the visualization option to compare sharpe by capitalization.It should be evenly distributed with at least 20% in Large cap category

When you reduce the universe of assets, the sample size for your alpha model shrinks. The smaller the universe, the less data you have to train and test your model, and that often leads to  **increased volatility**  in returns and a  **lower Sharpe ratio.**


---

### 技术对话片段 93 (原帖: YOU DECIDE! What topics do you want???)
- **原帖链接**: https://support.worldquantbrain.com[Commented] YOU DECIDE What topics do you want_29837364620695.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:

> [!NOTE] [图片 OCR 识别内容]
> WORIOOUAN
> BR^Ik
> Your Feedback Matters! 
> What topics do you want to
> See on OUr forum?


**顾问 AM60509 (Rank 61) 的解答与建议**:
Please post something on how to create alphas using others dataset category in USA,ASI and EUR region


---

### 技术对话片段 94 (原帖: YOU DECIDE! What topics do you want???)
- **原帖链接**: https://support.worldquantbrain.com[Commented] YOU DECIDE What topics do you want_29837364620695.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:

> [!NOTE] [图片 OCR 识别内容]
> WORIOOUAN
> BR^Ik
> Your Feedback Matters! 
> What topics do you want to
> See on OUr forum?


**顾问 AM60509 (Rank 61) 的解答与建议**:
i am interested in below topics:

1.How to create delay 0 alphas in usa and eur region

2.How to use short_interest dataset to create alphas  in usa and euro region


---

### 技术对话片段 95 (原帖: YOU DECIDE! What topics do you want???)
- **原帖链接**: https://support.worldquantbrain.com[Commented] YOU DECIDE What topics do you want_29837364620695.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:

> [!NOTE] [图片 OCR 识别内容]
> WORIOOUAN
> BR^Ik
> Your Feedback Matters! 
> What topics do you want to
> See on OUr forum?


**顾问 AM60509 (Rank 61) 的解答与建议**:
There are few posts that I want to on forum

1.how to improve value factor

2.how to improve weight factor

3.how to improve Combined alpha performance to above 2

4.how to improve Combined Selected alpha performance to above 2

5. Discussion on how world quant can reduce time taken to simulate and submit alphas


---

### 技术对话片段 96 (原帖: [Alpha Template] How can you utilize DuPont Analysis to create AlphasAlpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [Alpha Template] How can you utilize DuPont Analysis to create AlphasAlpha Template_28298364912151.md
- **时间**: 1年前

**提问/主帖背景 (YW42946)**:
Hey Consultants,

Today, let’s delve into how to uncover Alpha ideas using the renowned  **DuPont Analysis Framework** . DuPont Analysis, also known as the DuPont Identity, is a financial performance framework that dissects the components of  **Return on Equity (ROE)**  to give deeper insights into a company's financial health and operational efficiency. This method allows analysts to understand the underlying factors driving a company's ROE.

### 📐  **Basic ROE Formula**

The basic formula for ROE is:

> ROE=Net Income / Equity

### 🔍  **DuPont Analysis Components**

DuPont Analysis expands this formula into three key components:

1. **Profit margin** : Reflects the company's ability to convert sales into net income.
   1. Profit margin=Net income / Sales
2. **Asset turnover** : Measures how efficiently the company uses its assets to generate sales.
   1. Asset turnover=Sales / Total assets
3. **Equity multiplier** : Indicates the company's financial leverage. It shows how much of the company's assets are from shareholders' equity.
   1. Equity multiplier=Total assets / Shareholders’ equity

### 🔗  **Extended DuPont Formula**

By combining these three components, we get the extended DuPont formula for ROE:

> ROE=(Net Income / Sales)×(Sales / Total Assets)×(Total Assets / Shareholders’ Equity)

Simplified version as below:

> ROE=Profit Margin×Asset Turnover×Equity Multiplier

### 📊 Sample Template

From here, you can start brainstorming relevant Alpha ideas. For example, consider a scenario where companies have similar ROE growth rates but drastically different Profit Margin improvements.

One potential template you can use is:

> group_zscore(subtract(ts_zscore(<some_roe_data>, <days>), ts_zscore(<some_profit_margin_data>, <days>)), industry)

This template captures the industry-normalized difference between the time-series normalized ROE and Profit Margin.

Or, you can structure it as:

> <group_compare_op_1>(<diff_op>(<ts_compare_op_1>(<some_roe_data>, <days_1>), <ts_compare_op_2>(<some_profit_margin_data>, <days_2>)), <group_1>)

✨  **Key Points:**

- **Data Flexibility:**  Notice that both ROE data and Profit Margin data aren't defined. You can explore using historical data, forward estimates, or a combination of both, depending on your hypothesis.
- **Abstract Operators:**  All operators and group data become abstract choices, each embodying the economic intuition behind the original selection. For instance,  `<group_compare_op_1>`  might initially use  `group_zscore` , but other valid options could include  `group_rank` , which also compares the instrument to its peers within  `<group_1>` .

💡  **Discussion Prompt:**

Can you think of any other Alpha ideas derived from the DuPont Framework? Share your innovative ideas and approaches below! 💬

After reading this, you can understand how to  **hypothesize based on a well-known financial theory** , create an  **implementation** , and  **test whether it captures any signal** .

Happy researching! 🚀

**顾问 AM60509 (Rank 61) 的解答与建议**:
3 way  Du Pont Model is given below :-

ROE=Profit Margin× Asset Turnover× Equity Multiplier

5 way  Du Pont Model is given below :-

ROE=Tax burden× Interest burden × EBIT Margin × Asset Turnover× Equity Multiplier

Detailed explanation of the above 5 way model

1. Tax Burden = Net Income ÷ Pre-Tax Income
2. Asset Turnover = Revenue ÷ Average Total Assets
3. Financial Leverage Ratio = Average Total Assets ÷ Average Shareholders’ Equity
4. Interest Burden = Pre-Tax Income ÷ Operating Income
5. Operating Margin = Operating Income ÷ Revenue


---

### 技术对话片段 97 (原帖: [BRAIN TIPS] Finding Alphas: Fundamental and Model Data)
- **原帖链接**: [Commented] [BRAIN TIPS] Finding Alphas Fundamental and Model Data.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
[链接已屏蔽]

In the book “Finding Alphas”, Chapter 19 “Financial Statement Analysis”  **[1]**  and Chapter 20 “Fundamental Analysis and Alpha Research”  **[2]**  introduce the data available in financial statements and discusses the ways to perform financial statement analysis.

**Financial statement data**

Financial statements consist of the four main statements (balance sheet, income statement, cash flow statement, statement of shareholders’ equity) and the notes to these financial statements, which represent a summary of a company’s financial health. The former is found in the in the  [***Company Fundamental Data for Equity***]([链接已屏蔽])  dataset, while the latter is in the  [***Report Footnotes***]([链接已屏蔽])  dataset.

1. **Balance Sheet:**  The balance sheet offers a financial snapshot of an entity at a particular point in time. It is represented by the balance sheet equation: Asset = Liabilities + Equity. Both  ***assets***  and  ***equity***  are data fields available on BRAIN, while liabilities can usually be represented by  ***debt*** . On the top of that, you can also derive liabilities by taking  ***assets - equity*** .
2. **Income Statement:**  The income statement reflects changes in the balance sheet from one period to the next. It can be represented by Revenue–Expenses = Net Income. Both  ***revenue***  and  ***net income***  are data fields available on BRAIN, while you can derive the expenses by taking  ***revenue - net income*** .
3. **Cash Flow Statement:** The cash flow statement describes the sources of the change in a company’s cash balance from one period to the next. For example,  ***cashflow = cash – ts_delay(cash, 252)*** , which means that cash flow movement for the year is equal to the cash balance at the end of the current year less the cash balance at the end of the earlier year.
4. **Statement of Shareholders’ Equity:**  The statement of shareholders’ equity shows the change in the equity section of the balance sheet during the given period. Shareholders’ equity ( ***equity*** ) includes common equity ( ***fnd6_ceq*** ) and retained earnings ( ***retained_earnings*** ).

Financial statement analysis

There are financial measures available in the Company Fundamental Data for Equity dataset and the Model Data dataset that can be considered when constructing fundamental Alphas.

1. **Profitability:**  gross margin ( ***mdf_grm*** )
2. **Liquidity:**  current ratio ( ***mdf_ccr*** )
3. **Solvency:**  debt / equity ratio ( ***mdf_deq*** )
4. **Cash flow:**  cash flow from operations ( ***mdf_coa*** )
5. **Growth:**  net income / total assets ( ***income / assets*** )
6. **Valuation:**  price/book ratio ( ***mdf_pbk*** ),

Rather than just accepting the data in the financial statements, you also need the ability to understand and interpret them in depth. For example, profit consists of two parts: the actual cash flow generated from operations ( ***mdf_coa*** ) and the accrual amount calculated by the management/accountants ( ***mdf_rev-mdf_coa*** ). Since the accrual amount is subject to some variance, the actual cash flow of the company can be a better indicator of the company’s performance. In fact, a study by Sloan et al. (2011) found that cash-based profits are a stronger predictor of future corporate performance than accrual-based profits including accruals. When judging a company’s quality and profitability, it is important to analyze accounting events.

In addition, analyzing fundamental data can offer ideas for alternative stock classifications when doing Alpha research. Depending on financial performance, companies can be classified as value stocks or growth stocks, and companies can also be classified according to their leverage ratio. These various classification criteria allow you to further refine your position by classifying companies, neutralizing them according to each classification, and so on.

[**[1] Finding Alphas: Chapter 19. Financial Statement Analysis**]([链接已屏蔽])

[**[2] Finding Alphas: Chapter 20. Fundamental Analysis and Alpha Research**]([链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to make alphas on model data,start with machine learning dataset using fields like mdl110_score,mdl110_value,mdl_analyst_sentiment


---

### 技术对话片段 98 (原帖: [BRAIN TIPS] Finding Alphas: Fundamental and Model Data)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [BRAIN TIPS] Finding Alphas Fundamental and Model Data_20051403346583.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
[链接已屏蔽]

In the book “Finding Alphas”, Chapter 19 “Financial Statement Analysis”  **[1]**  and Chapter 20 “Fundamental Analysis and Alpha Research”  **[2]**  introduce the data available in financial statements and discusses the ways to perform financial statement analysis.

**Financial statement data**

Financial statements consist of the four main statements (balance sheet, income statement, cash flow statement, statement of shareholders’ equity) and the notes to these financial statements, which represent a summary of a company’s financial health. The former is found in the in the  [***Company Fundamental Data for Equity***]([链接已屏蔽])  dataset, while the latter is in the  [***Report Footnotes***]([链接已屏蔽])  dataset.

1. **Balance Sheet:**  The balance sheet offers a financial snapshot of an entity at a particular point in time. It is represented by the balance sheet equation: Asset = Liabilities + Equity. Both  ***assets***  and  ***equity***  are data fields available on BRAIN, while liabilities can usually be represented by  ***debt*** . On the top of that, you can also derive liabilities by taking  ***assets - equity*** .
2. **Income Statement:**  The income statement reflects changes in the balance sheet from one period to the next. It can be represented by Revenue–Expenses = Net Income. Both  ***revenue***  and  ***net income***  are data fields available on BRAIN, while you can derive the expenses by taking  ***revenue - net income*** .
3. **Cash Flow Statement:** The cash flow statement describes the sources of the change in a company’s cash balance from one period to the next. For example,  ***cashflow = cash – ts_delay(cash, 252)*** , which means that cash flow movement for the year is equal to the cash balance at the end of the current year less the cash balance at the end of the earlier year.
4. **Statement of Shareholders’ Equity:**  The statement of shareholders’ equity shows the change in the equity section of the balance sheet during the given period. Shareholders’ equity ( ***equity*** ) includes common equity ( ***fnd6_ceq*** ) and retained earnings ( ***retained_earnings*** ).

Financial statement analysis

There are financial measures available in the Company Fundamental Data for Equity dataset and the Model Data dataset that can be considered when constructing fundamental Alphas.

1. **Profitability:**  gross margin ( ***mdf_grm*** )
2. **Liquidity:**  current ratio ( ***mdf_ccr*** )
3. **Solvency:**  debt / equity ratio ( ***mdf_deq*** )
4. **Cash flow:**  cash flow from operations ( ***mdf_coa*** )
5. **Growth:**  net income / total assets ( ***income / assets*** )
6. **Valuation:**  price/book ratio ( ***mdf_pbk*** ),

Rather than just accepting the data in the financial statements, you also need the ability to understand and interpret them in depth. For example, profit consists of two parts: the actual cash flow generated from operations ( ***mdf_coa*** ) and the accrual amount calculated by the management/accountants ( ***mdf_rev-mdf_coa*** ). Since the accrual amount is subject to some variance, the actual cash flow of the company can be a better indicator of the company’s performance. In fact, a study by Sloan et al. (2011) found that cash-based profits are a stronger predictor of future corporate performance than accrual-based profits including accruals. When judging a company’s quality and profitability, it is important to analyze accounting events.

In addition, analyzing fundamental data can offer ideas for alternative stock classifications when doing Alpha research. Depending on financial performance, companies can be classified as value stocks or growth stocks, and companies can also be classified according to their leverage ratio. These various classification criteria allow you to further refine your position by classifying companies, neutralizing them according to each classification, and so on.

[**[1] Finding Alphas: Chapter 19. Financial Statement Analysis**]([链接已屏蔽])

[**[2] Finding Alphas: Chapter 20. Fundamental Analysis and Alpha Research**]([链接已屏蔽])

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to make alphas on model data,start with machine learning dataset using fields like mdl110_score,mdl110_value,mdl_analyst_sentiment


---

### 技术对话片段 99 (原帖: [BRAIN TIPS] Momentum Alphas)
- **原帖链接**: [Commented] [BRAIN TIPS] Momentum Alphas.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Momentum alpha captures short-term consistent trends and exits your position when there is a momentum shift. As a reminder, if there is bullish sentiment around the overall market, the majority of stocks will show good performances and if there is bearish sentiment overall, the opposite is true.

The alphas we build on the BRAIN platform are set to long-short neutral setting. It is harder to capture momentum signals in this setting compared to long-only alphas because if all the stocks are doing well, chances are you will take losses in the long-short neutral setting as you will be shorting some stocks.

Here are some examples of the same momentum alpha’s IS summaries with/without neutralization settings.


> [!NOTE] [image OCR 识别内容]
> IS Summary
> SDCUCUIJI
> StaBe
> AIIreWALe Datu
> 1,39
> 1.8996
> 2.82
> 51.59%
> 28.92%
> 5,463.209o00
> (entalization settny to "None)
> IS Summary
> Needs moroement
> StaBe
> Aggrcatc Oati
> 0.44
> 3.08%
> 0.23
> 3.50%
> 7.80%
> 226.60%oo
> (~eutralizationl setting
> rarket)


###### 

However, there are still ways to capture momentum signals.

In order to do that, sophisticated risk controls must be taken into account. This implies that momentum alphas perform well when the stock is less volatile.

Try initiating with trade_when operator or conditional operator to create an expression to specify entry expression or conditional expression to capture the momentum in your alphas. High volatility represents fluctuation on the stock price and thus fits more on reversion alphas.

As for the recommendation on datasets, market volatility can be captured when using datasets from “Systematic Risk Metrics”. News dataset and sentiment datasets can also be some excellent ways to capture momentum shift.

Lastly, try liquid universe like TOP500 when building your momentum alphas. Evidence shows that there is negative correlation between liquidity risk and momentum strategies  *(Asness, 2009)* .

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to introduce momentum factor into the alpha expression,add alpha=alpha+ts_delta(alpha,lookbackperiod) into the model


---

### 技术对话片段 100 (原帖: [BRAIN TIPS] Momentum Alphas)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [BRAIN TIPS] Momentum Alphas_15238206653975.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
Momentum alpha captures short-term consistent trends and exits your position when there is a momentum shift. As a reminder, if there is bullish sentiment around the overall market, the majority of stocks will show good performances and if there is bearish sentiment overall, the opposite is true.

The alphas we build on the BRAIN platform are set to long-short neutral setting. It is harder to capture momentum signals in this setting compared to long-only alphas because if all the stocks are doing well, chances are you will take losses in the long-short neutral setting as you will be shorting some stocks.

Here are some examples of the same momentum alpha’s IS summaries with/without neutralization settings.


> [!NOTE] [image OCR 识别内容]
> IS Summary
> SDCUCUIJI
> StaBe
> AIIreWALe Datu
> 1,39
> 1.8996
> 2.82
> 51.59%
> 28.92%
> 5,463.209o00
> (entalization settny to "None)
> IS Summary
> Needs moroement
> StaBe
> Aggrcatc Oati
> 0.44
> 3.08%
> 0.23
> 3.50%
> 7.80%
> 226.60%oo
> (~eutralizationl setting
> rarket)


###### 

However, there are still ways to capture momentum signals.

In order to do that, sophisticated risk controls must be taken into account. This implies that momentum alphas perform well when the stock is less volatile.

Try initiating with trade_when operator or conditional operator to create an expression to specify entry expression or conditional expression to capture the momentum in your alphas. High volatility represents fluctuation on the stock price and thus fits more on reversion alphas.

As for the recommendation on datasets, market volatility can be captured when using datasets from “Systematic Risk Metrics”. News dataset and sentiment datasets can also be some excellent ways to capture momentum shift.

Lastly, try liquid universe like TOP500 when building your momentum alphas. Evidence shows that there is negative correlation between liquidity risk and momentum strategies  *(Asness, 2009)* .

**顾问 AM60509 (Rank 61) 的解答与建议**:
In order to introduce momentum factor into the alpha expression,add alpha=alpha+ts_delta(alpha,lookbackperiod) into the model


---

### 技术对话片段 101 (原帖: [IQC2024] how to improve OS performance and avoid overfitting)
- **原帖链接**: [Commented] [IQC2024] how to improve OS performance and avoid overfitting.md
- **时间**: 1年前

**提问/主帖背景 (ML65849)**:
Hello, I'm Minki Lee, a researcher from the BRAIN team at WorldQuant Korea.

IQC's Stage 2.1 is nearing its end. Just like in Stage 1, the OS score plays a significant role in Stage 2 as well. Therefore, I recommend that you take some time to review your alpha pool and work on improving your OS score.

**What is the OS score?**

On the BRAIN platform, we have been providing simulations with a total of five years of data from early 2017 to early 2022 to users at the User level. Therefore, most users will strive to find alphas that generate profits during this In-Sample period. However, while trying to improve performance during this period, it is possible to unintentionally create overfitting that makes it appear as if the alpha is performing well, by taking long positions in companies that performed well in the stock market during this period, and short positions in companies that declined.

However, what is more important than the performance during this period is whether the alpha can generate signals in the future. Therefore, it is necessary to evaluate the performance from early 2022 to the present (Out-Sample period) and determine if the performance during this period is also good. In particular, in IQC2024, a higher weight is given to the OS score than the IS (In-Sample) score, and teams that submit alphas that are not overfit or underfit are evaluated more favorably.

**Methods to improve the OS score**

However, it is not easy to determine which alpha is overfitting since we cannot accurately predict the future. We only have a period of about five years, and we can only observe that period, so overfitting occurs more frequently than we think.

Just like evaluating the performance of alphas with Sharpe ratio, the performance of OS can also be evaluated with Sharpe ratio. However, it is known that the OS Sharpe ratio of alphas submitted by consultants generally falls short of the IS Sharpe ratio. The figure below shows the result of combining 30 randomly selected alphas from the In-Sample period until mid-2020 into a super alpha with equal weight. (You can also create such a super alpha once you switch to a consultant.) You can see that the performance of the combined alpha deteriorates as soon as the Out-Sample period begins. Despite the fact that these alphas were created by consultants with more experience than common users and were subjected to more strict criteria, the fact that such results occur implies that it is easy to fall into the trap of overfitting in alpha research more than you thought.


> [!NOTE] [图片 OCR 识别内容]
> 3013
> 30J
> 1UJ
> 100
> 50
> 4 OOO
> 30O
> 7217
> 1,409
> 2016
> 7019


However, it is not easy to determine whether your alpha is overfitting or not. An alpha can either accurately reflect signals or not. Therefore, we can consider and express the future performance of alphas as follows:


> [!NOTE] [图片 OCR 识别内容]
> In-Sample period


If an alpha effectively captures signals, it can show good performance in the OS. Even if the signals temporarily show poor performance, they can recover their profitability in the long term. However, if an alpha is overfit and lacks signals, it will randomly fluctuate around a return of 0 in the OS. Considering these factors together, for an alpha that is potentially overfit and uncertain, we can expect its future performance to be lower on average than the IS but still higher than 0.

In such a situation, what can be done to improve the OS performance of a merged alpha? One good approach is to include alphas in your alpha pool that reflect various risks, aiming to make the overall performance as close to the average as possible. As the alphas encompass diverse risks with low correlation, the standard deviation will decrease, resulting in OS returns closer to the average (positive) and a lower standard deviation, leading to a higher OS Sharpe ratio.

In addition, good alphas that are not overfit are known to have the following characteristics:

- They have simple and concise ideas with underlying economic insights.
- They are not sensitive to small changes in data or parameters.
- They work well across multiple universes.
- They work well across different regions.

**Practices that can have a negative impact on OS performance**

Using a single formula repeatedly across multiple alphas can have a detrimental effect on OS performance. Let's consider an example. The following alpha was created for the In-Sample period from 2016 to 2021. It was a fairly strong alpha with a Sharpe ratio of 2.07 and a fitness of 1.70.


> [!NOTE] [图片 OCR 识别内容]
> 4077
> 3TS.
> 350
> 3750
> 3OuJ
> 2.750
> TCOJ
> 2250.
> ZO.
> 7750
> 1.5005
> TSJ
> T000
> TCJI
> SOJr
> L'I
> N'17
> Con 17
> Nro
> Sp  18
> lan '1C
> 1*19
> Sep '19
> C6


The performance of this alpha during the out-of-sample period would have been poor. Although this is an extreme example, this alpha exhibited very poor OS performance with a Sharpe ratio of -3.22 and a fitness of -5.77 during the OS period.


> [!NOTE] [图片 OCR 识别内容]
> ~ OJOK
> 375OK
> 35NOk
> 3750
> 30O
> 275OK
> 2SOOK
> 275OK
> 2NJOK
> 750
> 1sok
> 475OK
> OOOK
> TSJ
> JulE
> n 17
> Jul '
> C
> In0
> TO
> n
> 011
> U


Although the OS performance is not good, discovering this signal and observing its strong performance during the IS period can incentivize participants in the IQC competition to create alphas by simply mixing this signal with other signals. Here is an example of another alpha created by mixing this signal with other signals:


> [!NOTE] [图片 OCR 识别内容]
> 375J
> 354
> J29
> 1011
> ?55J
> 2SOOK
> 225J
> ZMK
> 1154k
> 1S
> 135J
> 1OJJ


This alpha visually appears to be exposed to a similar level of risk as some of the leading alphas. However, the correlation between these two alphas is 0.59, which is below the threshold of 0.7. Therefore, it can be submitted separately. Additionally, considering that the IS performance of this alpha is not bad, users may want to submit it.

However, when two similar alphas are submitted together, the negative signal in this alpha will have a higher weight in the merged alpha, resulting in a more detrimental impact on the OS performance.

Of course, this alpha highlights the negative effects of signal mixing because its OS performance is particularly poor. However, even if an alpha has good OS performance, if it has a high correlation with other alphas in the alpha pool, it can increase the standard deviation of the merged alpha and consequently have a negative impact on the OS performance.

In this post, we explored more practical ways to improve the OS score in IQC. If you have any questions or would like to know more, please leave a comment, and I will be happy to respond.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Use simple ideas using only single data set to avoid overfitting and improve OS Performance. Avoid fine tuning parameters like lookback period,powers etc.


---

### 技术对话片段 102 (原帖: [IQC2024] how to improve OS performance and avoid overfitting)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [IQC2024] how to improve OS performance and avoid overfitting_24305473573911.md
- **时间**: 1年前

**提问/主帖背景 (ML65849)**:
Hello, I'm Minki Lee, a researcher from the BRAIN team at WorldQuant Korea.

IQC's Stage 2.1 is nearing its end. Just like in Stage 1, the OS score plays a significant role in Stage 2 as well. Therefore, I recommend that you take some time to review your alpha pool and work on improving your OS score.

**What is the OS score?**

On the BRAIN platform, we have been providing simulations with a total of five years of data from early 2017 to early 2022 to users at the User level. Therefore, most users will strive to find alphas that generate profits during this In-Sample period. However, while trying to improve performance during this period, it is possible to unintentionally create overfitting that makes it appear as if the alpha is performing well, by taking long positions in companies that performed well in the stock market during this period, and short positions in companies that declined.

However, what is more important than the performance during this period is whether the alpha can generate signals in the future. Therefore, it is necessary to evaluate the performance from early 2022 to the present (Out-Sample period) and determine if the performance during this period is also good. In particular, in IQC2024, a higher weight is given to the OS score than the IS (In-Sample) score, and teams that submit alphas that are not overfit or underfit are evaluated more favorably.

**Methods to improve the OS score**

However, it is not easy to determine which alpha is overfitting since we cannot accurately predict the future. We only have a period of about five years, and we can only observe that period, so overfitting occurs more frequently than we think.

Just like evaluating the performance of alphas with Sharpe ratio, the performance of OS can also be evaluated with Sharpe ratio. However, it is known that the OS Sharpe ratio of alphas submitted by consultants generally falls short of the IS Sharpe ratio. The figure below shows the result of combining 30 randomly selected alphas from the In-Sample period until mid-2020 into a super alpha with equal weight. (You can also create such a super alpha once you switch to a consultant.) You can see that the performance of the combined alpha deteriorates as soon as the Out-Sample period begins. Despite the fact that these alphas were created by consultants with more experience than common users and were subjected to more strict criteria, the fact that such results occur implies that it is easy to fall into the trap of overfitting in alpha research more than you thought.


> [!NOTE] [图片 OCR 识别内容]
> 3013
> 30J
> 1UJ
> 100
> 50
> 4 OOO
> 30O
> 7217
> 1,409
> 2016
> 7019


However, it is not easy to determine whether your alpha is overfitting or not. An alpha can either accurately reflect signals or not. Therefore, we can consider and express the future performance of alphas as follows:


> [!NOTE] [图片 OCR 识别内容]
> In-Sample period


If an alpha effectively captures signals, it can show good performance in the OS. Even if the signals temporarily show poor performance, they can recover their profitability in the long term. However, if an alpha is overfit and lacks signals, it will randomly fluctuate around a return of 0 in the OS. Considering these factors together, for an alpha that is potentially overfit and uncertain, we can expect its future performance to be lower on average than the IS but still higher than 0.

In such a situation, what can be done to improve the OS performance of a merged alpha? One good approach is to include alphas in your alpha pool that reflect various risks, aiming to make the overall performance as close to the average as possible. As the alphas encompass diverse risks with low correlation, the standard deviation will decrease, resulting in OS returns closer to the average (positive) and a lower standard deviation, leading to a higher OS Sharpe ratio.

In addition, good alphas that are not overfit are known to have the following characteristics:

- They have simple and concise ideas with underlying economic insights.
- They are not sensitive to small changes in data or parameters.
- They work well across multiple universes.
- They work well across different regions.

**Practices that can have a negative impact on OS performance**

Using a single formula repeatedly across multiple alphas can have a detrimental effect on OS performance. Let's consider an example. The following alpha was created for the In-Sample period from 2016 to 2021. It was a fairly strong alpha with a Sharpe ratio of 2.07 and a fitness of 1.70.


> [!NOTE] [图片 OCR 识别内容]
> 4077
> 3TS.
> 350
> 3750
> 3OuJ
> 2.750
> TCOJ
> 2250.
> ZO.
> 7750
> 1.5005
> TSJ
> T000
> TCJI
> SOJr
> L'I
> N'17
> Con 17
> Nro
> Sp  18
> lan '1C
> 1*19
> Sep '19
> C6


The performance of this alpha during the out-of-sample period would have been poor. Although this is an extreme example, this alpha exhibited very poor OS performance with a Sharpe ratio of -3.22 and a fitness of -5.77 during the OS period.


> [!NOTE] [图片 OCR 识别内容]
> ~ OJOK
> 375OK
> 35NOk
> 3750
> 30O
> 275OK
> 2SOOK
> 275OK
> 2NJOK
> 750
> 1sok
> 475OK
> OOOK
> TSJ
> JulE
> n 17
> Jul '
> C
> In0
> TO
> n
> 011
> U


Although the OS performance is not good, discovering this signal and observing its strong performance during the IS period can incentivize participants in the IQC competition to create alphas by simply mixing this signal with other signals. Here is an example of another alpha created by mixing this signal with other signals:


> [!NOTE] [图片 OCR 识别内容]
> 375J
> 354
> J29
> 1011
> ?55J
> 2SOOK
> 225J
> ZMK
> 1154k
> 1S
> 135J
> 1OJJ


This alpha visually appears to be exposed to a similar level of risk as some of the leading alphas. However, the correlation between these two alphas is 0.59, which is below the threshold of 0.7. Therefore, it can be submitted separately. Additionally, considering that the IS performance of this alpha is not bad, users may want to submit it.

However, when two similar alphas are submitted together, the negative signal in this alpha will have a higher weight in the merged alpha, resulting in a more detrimental impact on the OS performance.

Of course, this alpha highlights the negative effects of signal mixing because its OS performance is particularly poor. However, even if an alpha has good OS performance, if it has a high correlation with other alphas in the alpha pool, it can increase the standard deviation of the merged alpha and consequently have a negative impact on the OS performance.

In this post, we explored more practical ways to improve the OS score in IQC. If you have any questions or would like to know more, please leave a comment, and I will be happy to respond.

**顾问 AM60509 (Rank 61) 的解答与建议**:
Use simple ideas using only single data set to avoid overfitting and improve OS Performance. Avoid fine tuning parameters like lookback period,powers etc.


---

### 技术对话片段 103 (原帖: Print dates and values of outliers)
- **原帖链接**: [Commented] [Quant Playlist] Detecting Outliers in Real Market Data.md
- **时间**: 1年前

**提问/主帖背景 (SY38692)**:
## **Detecting Outliers in Real Market Data**

In this post, we will collect real stock price data and apply various outlier detection techniques (IQR, Z-Score, LOF, Isolation Forest) to identify anomalies.

### **1. Data Collection and Preprocessing**

Using the  `yfinance`  library, we collect stock price data and calculate returns based on it.

```
import yfinance as yf
import pandas as pd

# Data collection
ticker = "AAPL"  # Apple stock
data = yf.download(ticker, start="2018-01-01", end="2023-01-01")["Close"]

# Calculate returns
returns = data.pct_change().dropna()
returns.name = "Returns"

print("Returns Head:\n", returns.head())

```

### **2. Outlier Detection Using IQR (Interquartile Range)**

The IQR method detects outliers based on quartiles. It is a simple statistical technique that considers data outside the IQR range as outliers.

```
# Calculate IQR
Q1 = returns.quantile(0.25)
Q3 = returns.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers_iqr = returns[(returns < lower_bound) | (returns > upper_bound)]

# Print dates and values of outliers
print("IQR Outliers:")
for date, value in outliers_iqr.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **3. Outlier Detection Using Z-Score**

The Z-Score method measures how many standard deviations a data point is away from the mean. Typically, values where Z>3Z > 3 or Z<−3Z < -3 are considered outliers.

```
from scipy.stats import zscore

# Calculate Z-Score
z_scores = zscore(returns)
outliers_zscore = returns[abs(z_scores) > 3]

# Print dates and values of outliers
print("Z-Score Outliers:")
for date, value in outliers_zscore.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **4. Outlier Detection Using LOF (Local Outlier Factor)**

LOF compares the density of a data point with its neighbors to detect outliers. Data points with lower density are identified as outliers.

```
from sklearn.neighbors import LocalOutlierFactor

# LOF model
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outliers_lof = lof.fit_predict(returns.values.reshape(-1, 1))

# Detect outliers
outliers_lof_index = returns.index[outliers_lof == -1]
lof_outliers = returns.loc[outliers_lof_index]

# Print dates and values of outliers
print("LOF Outliers:")
for date, value in lof_outliers.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **5. Outlier Detection Using Isolation Forest**

Isolation Forest detects outliers by randomly isolating data points. Points that are easier to isolate (shorter separation cost) are considered outliers.

```
from sklearn.ensemble import IsolationForest

# Isolation Forest model
iso_forest = IsolationForest(contamination=0.05, random_state=42)
outliers_iso = iso_forest.fit_predict(returns.values.reshape(-1, 1))

# Detect outliers
outliers_iso_index = returns.index[outliers_iso == -1]
iso_outliers = returns.loc[outliers_iso_index]

# Print dates and values of outliers
print("Isolation Forest Outliers:")
for date, value in iso_outliers.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **Conclusion**

In financial data outlier detection using Python, selecting the appropriate technique based on the data characteristics and analysis goals is crucial.

- **IQR and Z-Score** : Suitable for simple outlier detection based on data distribution.
- **LOF and Isolation Forest** : Effective for identifying non-linear and complex outliers.

Compare the results of each method to improve data quality and enhance model performance. If you have additional questions or topics you'd like to explore, feel free to ask! 😊

**顾问 AM60509 (Rank 61) 的解答与建议**:
An outlier is a data point that differs significantly from the other observations in a dataset. It may be unusually high or low compared to the expected range or pattern.

In financial time series, outliers can represent critical events such as market crashes, fraud, or system errors

By implementing IQR, Z-Score, LOF, and Isolation Forest, the analysis reveals the nuanced approaches to identifying unusual market behaviors.


---

### 技术对话片段 104 (原帖: Print dates and values of outliers)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [Quant Playlist] Detecting Outliers in Real Market Data_28868094639767.md
- **时间**: 1年前

**提问/主帖背景 (SY38692)**:
## **Detecting Outliers in Real Market Data**

In this post, we will collect real stock price data and apply various outlier detection techniques (IQR, Z-Score, LOF, Isolation Forest) to identify anomalies.

### **1. Data Collection and Preprocessing**

Using the  `yfinance`  library, we collect stock price data and calculate returns based on it.

```
import yfinance as yf
import pandas as pd

# Data collection
ticker = "AAPL"  # Apple stock
data = yf.download(ticker, start="2018-01-01", end="2023-01-01")["Close"]

# Calculate returns
returns = data.pct_change().dropna()
returns.name = "Returns"

print("Returns Head:\n", returns.head())

```

### **2. Outlier Detection Using IQR (Interquartile Range)**

The IQR method detects outliers based on quartiles. It is a simple statistical technique that considers data outside the IQR range as outliers.

```
# Calculate IQR
Q1 = returns.quantile(0.25)
Q3 = returns.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detect outliers
outliers_iqr = returns[(returns < lower_bound) | (returns > upper_bound)]

# Print dates and values of outliers
print("IQR Outliers:")
for date, value in outliers_iqr.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **3. Outlier Detection Using Z-Score**

The Z-Score method measures how many standard deviations a data point is away from the mean. Typically, values where Z>3Z > 3 or Z<−3Z < -3 are considered outliers.

```
from scipy.stats import zscore

# Calculate Z-Score
z_scores = zscore(returns)
outliers_zscore = returns[abs(z_scores) > 3]

# Print dates and values of outliers
print("Z-Score Outliers:")
for date, value in outliers_zscore.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **4. Outlier Detection Using LOF (Local Outlier Factor)**

LOF compares the density of a data point with its neighbors to detect outliers. Data points with lower density are identified as outliers.

```
from sklearn.neighbors import LocalOutlierFactor

# LOF model
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outliers_lof = lof.fit_predict(returns.values.reshape(-1, 1))

# Detect outliers
outliers_lof_index = returns.index[outliers_lof == -1]
lof_outliers = returns.loc[outliers_lof_index]

# Print dates and values of outliers
print("LOF Outliers:")
for date, value in lof_outliers.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **5. Outlier Detection Using Isolation Forest**

Isolation Forest detects outliers by randomly isolating data points. Points that are easier to isolate (shorter separation cost) are considered outliers.

```
from sklearn.ensemble import IsolationForest

# Isolation Forest model
iso_forest = IsolationForest(contamination=0.05, random_state=42)
outliers_iso = iso_forest.fit_predict(returns.values.reshape(-1, 1))

# Detect outliers
outliers_iso_index = returns.index[outliers_iso == -1]
iso_outliers = returns.loc[outliers_iso_index]

# Print dates and values of outliers
print("Isolation Forest Outliers:")
for date, value in iso_outliers.items():
    print(f"Date: {date}, Outlier Value: {value}")

```

### **Conclusion**

In financial data outlier detection using Python, selecting the appropriate technique based on the data characteristics and analysis goals is crucial.

- **IQR and Z-Score** : Suitable for simple outlier detection based on data distribution.
- **LOF and Isolation Forest** : Effective for identifying non-linear and complex outliers.

Compare the results of each method to improve data quality and enhance model performance. If you have additional questions or topics you'd like to explore, feel free to ask! 😊

**顾问 AM60509 (Rank 61) 的解答与建议**:
An outlier is a data point that differs significantly from the other observations in a dataset. It may be unusually high or low compared to the expected range or pattern.

In financial time series, outliers can represent critical events such as market crashes, fraud, or system errors

By implementing IQR, Z-Score, LOF, and Isolation Forest, the analysis reveals the nuanced approaches to identifying unusual market behaviors.


---

### 技术对话片段 105 (原帖: [Quant Playlist] Portfolio Optimization: Concepts and Key Models)
- **原帖链接**: [Commented] [Quant Playlist] Portfolio Optimization Concepts and Key Models.md
- **时间**: 1年前

**提问/主帖背景 (SY38692)**:
## **Portfolio Optimization: Concepts and Key Models**

Hello, today's topic is portfolio optimization. Below is the prepared agenda:

### **Agenda**

- What is Portfolio Optimization?
  - Definition of Portfolio Optimization
  - Objectives of Portfolio Optimization

- Key Theories and Models
  - Markowitz Mean-Variance Optimization
  - Black-Litterman Model
  - Risk Parity

## **1. What is Portfolio Optimization?**

#### **Definition of Portfolio Optimization**

Portfolio optimization is a methodology used to allocate assets in a way that maximizes an investor's expected returns or minimizes risks. It considers asset returns, volatility, and correlations to effectively achieve investment objectives.

#### **Objectives of Portfolio Optimization**

- **Balance Between Risk and Return**
  - Maximize returns for a given level of risk or minimize risk for a target return.
- **Maximize Diversification Effects**
  - Utilize correlations among assets to enhance the benefits of diversification and reduce portfolio risk.
- **Tailored Asset Allocation for Investment Goals**
  - Design customized portfolios based on the investor's risk tolerance, investment horizon, and expected returns.

## **2.  Key Theories and Models**

#### **(1) Markowitz Mean-Variance Optimization**

Developed by Harry Markowitz in 1952, this foundational model of Modern Portfolio Theory (MPT) optimizes the balance between returns and risks across assets to construct an efficient portfolio.

**Key Concepts** :

- **Expected Portfolio Return** :
  Weighted average of individual asset returns.


> [!NOTE] [图片 OCR 识别内容]
> Lp
> Uilli
> i1
> Hp: Expected return of the portfolio
> Ui: Weight of asseti
> Li: Expected return of asset


- **Portfolio Risk (Variance)** :
  Weighted combination of asset variances and covariances.


> [!NOTE] [图片 OCR 识别内容]
> D =
> UiWjOij
> 1
> jL
> 43: Portfolio variance (risk)
> Oij: Covariance between asset iand asset j


**Efficient Frontier:**

- Represents the portfolios offering maximum returns for a given risk level or minimum risk for a given return level.

**Constraints** :

- Total asset weights sum to 100%.


> [!NOTE] [图片 OCR 识别内容]
> Ui


- Individual asset weights must be non-negative.


> [!NOTE] [图片 OCR 识别内容]
> Ui
> 二0
> Vi


#### **(2) Black-Litterman Model**

Developed by Fischer Black and Robert Litterman in the 1990s, this model combines market equilibrium and investor beliefs to provide more stable and realistic portfolio allocations.

**Key Concepts:**

- **Market Equilibrium** :
  Asset weights in the market portfolio are proportional to their market capitalization.
- **Investor Beliefs** :
  Incorporates subjective views on expected returns and risks for specific assets or sectors.

**Model Structure:**

- Combines market equilibrium returns (π) with investor beliefs to calculate adjusted expected returns.:


> [!NOTE] [图片 OCR 识别内容]
> E[#
> T 十T . PI . (Q-1 . (Q -卫.T))
> 卫[#: New expected returns
> Market equilibrium expected returns
> 卫: View matrix (reflects investor opinions on specific assets)
> 0
> Investor views (expected returns for assets based on Views)
> Q: Uncertainty in views (confidence in investor opinions)
> T: Market
> uncertainty adjustment factor


**Advantages:**

- Integrates market data with subjective views for realistic portfolios.
- Prevents extreme portfolio weights, ensuring stability.

#### **(3) Risk Parity**

Risk Parity is an asset allocation strategy designed to equalize the contribution of each asset to the overall portfolio risk. This approach lowers the weight of volatile assets while increasing the weight of less volatile assets to enhance stability.

**Key Concepts** :

- **Risk Contribution** :
  Measures each asset's contribution to the total portfolio risk.


> [!NOTE] [图片 OCR 识别内容]
> RCi
> Ui
> Owi
> RCi: Risk contribution Of asset i
> Ui: Weight of asset i
> Op: Portfolio standard deviation
> Q0e


- **Objective** :
  Equalize risk contributions across all assets.


> [!NOTE] [图片 OCR 识别内容]
> RCI
> RC2
> RCn


**Advantages** :

- Reduces the impact of highly volatile assets.
- Delivers stable performance even in volatile markets.

**Optimization Problem** :

- **Objective Function** : Adjust weights to ensure equal risk contributions.


> [!NOTE] [图片 OCR 识别内容]
> Iinimize
> RCi


### 

Portfolio optimization is a critical tool for achieving an investor’s risk tolerance and return objectives.

1. **Markowitz Mean-Variance Optimization**  optimizes the trade-off between risk and return and provides optimal asset allocation through the efficient frontier.
2. **Black-Litterman Model**  integrates market equilibrium and investor beliefs for realistic portfolio construction.
3. **Risk Parity**  balances risk contributions to enhance portfolio stability.

By selecting the appropriate model and applying it effectively, you can design sophisticated and reliable asset allocation strategies. Explore various strategies and apply them in practice to achieve your investment goals!

**顾问 AM60509 (Rank 61) 的解答与建议**:
The content provides a solid foundation for understanding key approaches to asset allocation.

Portfolio optimization is essential for achieving the optimal risk-return balance, a core aspect of quantitative finance.

Markowitz Mean-Variance Optimization (MVO) is one of the foundational models in portfolio theory. It aims to find the optimal portfolio that offers the highest return for a given level of risk or the lowest risk for a given level of return


---

### 技术对话片段 106 (原帖: [Quant Playlist] Portfolio Optimization: Concepts and Key Models)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [Quant Playlist] Portfolio Optimization Concepts and Key Models_28867925453463.md
- **时间**: 1年前

**提问/主帖背景 (SY38692)**:
## **Portfolio Optimization: Concepts and Key Models**

Hello, today's topic is portfolio optimization. Below is the prepared agenda:

### **Agenda**

- What is Portfolio Optimization?
  - Definition of Portfolio Optimization
  - Objectives of Portfolio Optimization

- Key Theories and Models
  - Markowitz Mean-Variance Optimization
  - Black-Litterman Model
  - Risk Parity

## **1. What is Portfolio Optimization?**

#### **Definition of Portfolio Optimization**

Portfolio optimization is a methodology used to allocate assets in a way that maximizes an investor's expected returns or minimizes risks. It considers asset returns, volatility, and correlations to effectively achieve investment objectives.

#### **Objectives of Portfolio Optimization**

- **Balance Between Risk and Return**
  - Maximize returns for a given level of risk or minimize risk for a target return.
- **Maximize Diversification Effects**
  - Utilize correlations among assets to enhance the benefits of diversification and reduce portfolio risk.
- **Tailored Asset Allocation for Investment Goals**
  - Design customized portfolios based on the investor's risk tolerance, investment horizon, and expected returns.

## **2.  Key Theories and Models**

#### **(1) Markowitz Mean-Variance Optimization**

Developed by Harry Markowitz in 1952, this foundational model of Modern Portfolio Theory (MPT) optimizes the balance between returns and risks across assets to construct an efficient portfolio.

**Key Concepts** :

- **Expected Portfolio Return** :
  Weighted average of individual asset returns.


> [!NOTE] [图片 OCR 识别内容]
> Lp
> Uilli
> i1
> Hp: Expected return of the portfolio
> Ui: Weight of asseti
> Li: Expected return of asset


- **Portfolio Risk (Variance)** :
  Weighted combination of asset variances and covariances.


> [!NOTE] [图片 OCR 识别内容]
> D =
> UiWjOij
> 1
> jL
> 43: Portfolio variance (risk)
> Oij: Covariance between asset iand asset j


**Efficient Frontier:**

- Represents the portfolios offering maximum returns for a given risk level or minimum risk for a given return level.

**Constraints** :

- Total asset weights sum to 100%.


> [!NOTE] [图片 OCR 识别内容]
> Ui


- Individual asset weights must be non-negative.


> [!NOTE] [图片 OCR 识别内容]
> Ui
> 二0
> Vi


#### **(2) Black-Litterman Model**

Developed by Fischer Black and Robert Litterman in the 1990s, this model combines market equilibrium and investor beliefs to provide more stable and realistic portfolio allocations.

**Key Concepts:**

- **Market Equilibrium** :
  Asset weights in the market portfolio are proportional to their market capitalization.
- **Investor Beliefs** :
  Incorporates subjective views on expected returns and risks for specific assets or sectors.

**Model Structure:**

- Combines market equilibrium returns (π) with investor beliefs to calculate adjusted expected returns.:


> [!NOTE] [图片 OCR 识别内容]
> E[#
> T 十T . PI . (Q-1 . (Q -卫.T))
> 卫[#: New expected returns
> Market equilibrium expected returns
> 卫: View matrix (reflects investor opinions on specific assets)
> 0
> Investor views (expected returns for assets based on Views)
> Q: Uncertainty in views (confidence in investor opinions)
> T: Market
> uncertainty adjustment factor


**Advantages:**

- Integrates market data with subjective views for realistic portfolios.
- Prevents extreme portfolio weights, ensuring stability.

#### **(3) Risk Parity**

Risk Parity is an asset allocation strategy designed to equalize the contribution of each asset to the overall portfolio risk. This approach lowers the weight of volatile assets while increasing the weight of less volatile assets to enhance stability.

**Key Concepts** :

- **Risk Contribution** :
  Measures each asset's contribution to the total portfolio risk.


> [!NOTE] [图片 OCR 识别内容]
> RCi
> Ui
> Owi
> RCi: Risk contribution Of asset i
> Ui: Weight of asset i
> Op: Portfolio standard deviation
> Q0e


- **Objective** :
  Equalize risk contributions across all assets.


> [!NOTE] [图片 OCR 识别内容]
> RCI
> RC2
> RCn


**Advantages** :

- Reduces the impact of highly volatile assets.
- Delivers stable performance even in volatile markets.

**Optimization Problem** :

- **Objective Function** : Adjust weights to ensure equal risk contributions.


> [!NOTE] [图片 OCR 识别内容]
> Iinimize
> RCi


### 

Portfolio optimization is a critical tool for achieving an investor’s risk tolerance and return objectives.

1. **Markowitz Mean-Variance Optimization**  optimizes the trade-off between risk and return and provides optimal asset allocation through the efficient frontier.
2. **Black-Litterman Model**  integrates market equilibrium and investor beliefs for realistic portfolio construction.
3. **Risk Parity**  balances risk contributions to enhance portfolio stability.

By selecting the appropriate model and applying it effectively, you can design sophisticated and reliable asset allocation strategies. Explore various strategies and apply them in practice to achieve your investment goals!

**顾问 AM60509 (Rank 61) 的解答与建议**:
The content provides a solid foundation for understanding key approaches to asset allocation.

Portfolio optimization is essential for achieving the optimal risk-return balance, a core aspect of quantitative finance.

Markowitz Mean-Variance Optimization (MVO) is one of the foundational models in portfolio theory. It aims to find the optimal portfolio that offers the highest return for a given level of risk or the lowest risk for a given level of return


---

### 技术对话片段 107 (原帖: [Quant Playlist] Tests of Statistical Hypotheses)
- **原帖链接**: [Commented] [Quant Playlist] Tests of Statistical Hypotheses.md
- **时间**: 1年前

**提问/主帖背景 (SY38692)**:
## **Tests of Statistical Hypotheses**

Hello. The topic is statistical hypothesis testing. The agenda prepared is as follows.

### Agenda

1. Concepts of statistical hypothesis testing
2. Types of hypotheses
3. Procedures for hypothesis testing
4. Major statistical testing methods

## **1. Concept of statistical hypothesis testing**

Statistical hypothesis testing is a method of evaluating the validity of a hypothesis based on data. It is a key tool for using sample data to confirm whether a hypothesis about a population is correct or to test differences between different groups.

Hypothesis testing is mainly used in the following situations:

- Test the mean, proportion, or variance of a specific population
- Compare the differences between two groups.
- Examine the relationship between variables.

## **2. Types of Hypotheses**

#### **(1) Null Hypothesis (H₀)**

- Indicates a basic assumption or current state.
- Takes the form "no difference" or "no effect."
- Example: The means of the two groups are the same.

#### **(2) Alternative Hypothesis (H₁)**

- The opposite hypothesis to the Null Hypothesis.
- It has the form "There is a difference" or "There is an effect."
- Example: The means of the two groups are different.

## **3. Hypothesis testing procedure**

#### **(1) Hypothesis setting**

- Define H₀ and H₁.

#### **(2) Setting the Significance Level (α)**

- The probability of allowing an error, usually 0.05 (5%), is used.
- If α = 0.05, it means that there is a 5% chance of rejecting the wrong H₀.

#### **(3) Calculating test statistics**

- Calculate statistics (T-statistic, Z-statistic, etc.) from data.

#### **(4) Calculating the P-value**

- The probability that the observed result would occur under H₀.
- If P-value < α, reject H₀.

#### **(5) Drawing a conclusion.**

- Evaluate the validity of the hypothesis by rejecting or failing to reject H₀.

## **4. Major statistical testing methods**

#### **(1) T-Test**

The T-test is a statistical test used to compare differences between means.

**1. One-Sample T-Test**

```
pythonfrom scipy.stats import ttest_1sampdata = [177, 179, 181, 178, 182]t_stat, p_value = ttest_1samp(data, 180)
```

**2. Independent Two-Sample T-Test**

```
pythonfrom scipy.stats import ttest_indgroup1 = [177, 179, 181, 178, 182]group2 = [170, 172, 174, 171, 173]t_stat, p_value = ttest_ind(group1, group2)
```

**3. Paired T-Test**

```
pythonfrom scipy.stats import ttest_relbefore = [177, 179, 181, 178, 182]after = [175, 177, 179, 176, 180]t_stat, p_value = ttest_rel(before, after)
```

#### **(2) ANOVA (Analysis of Variance)**

ANOVA is used to test the difference in means among three or more groups.

**1. One-Way ANOVA**

```
pythonfrom scipy.stats import f_onewaygroup1 = [177, 179, 181, 178, 182]group2 = [170, 172, 174, 171, 173]group3 = [165, 167, 169, 166, 168]f_stat, p_value = f_oneway(group1, group2, group3)
```

**2. Two-Way ANOVA**

#### **(3) Chi-Square Test**

The Chi-Square Test compares observed frequencies with expected frequencies in categorical data.

**1. Test of independence.**

```
pythonfrom scipy.stats import chi2_contingencydata = [[10, 20], [20, 40]]chi2, p_value, _, _ = chi2_contingency(data)
```

**2. Goodness-of-fit test.**

#### **(4) Correlation Test**

The Correlation Test evaluates the linear relationship between two variables.

**1. Pearson Correlation**

```
pythonfrom scipy.stats import pearsonrx = [1, 2, 3, 4, 5]y = [2, 4, 6, 8, 10]corr, p_value = pearsonr(x, y)
```

**2. Spearman Correlation**

```
pythonfrom scipy.stats import spearmanrcorr, p_value = spearmanr(x, y)
```

**3. Kendall Correlation**

```
pythonfrom scipy.stats import kendalltaucorr, p_value = kendalltau(x, y)
```

Statistical hypothesis testing plays a crucial role in data analysis, providing tools to evaluate the validity of a hypothesis based on data. It is essential to select an appropriate testing method and draw reliable conclusions based on the significance level and P-value. By leveraging these testing methods, you can produce more robust and meaningful analytical results!

**顾问 AM60509 (Rank 61) 的解答与建议**:
Statistical hypothesis testing is a fundamental concept in inferential statistics. It allows researchers to make decisions or inferences about a population based on sample data

The  **Goodness-of-Fit test**   is commonly used when you want to test if a sample data follows a hypothesized distribution (like a normal distribution, uniform distribution, etc.).


---

### 技术对话片段 108 (原帖: [Quant Playlist] Tests of Statistical Hypotheses)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [Quant Playlist] Tests of Statistical Hypotheses_28867911294999.md
- **时间**: 1年前

**提问/主帖背景 (SY38692)**:
## **Tests of Statistical Hypotheses**

Hello. The topic is statistical hypothesis testing. The agenda prepared is as follows.

### Agenda

1. Concepts of statistical hypothesis testing
2. Types of hypotheses
3. Procedures for hypothesis testing
4. Major statistical testing methods

## **1. Concept of statistical hypothesis testing**

Statistical hypothesis testing is a method of evaluating the validity of a hypothesis based on data. It is a key tool for using sample data to confirm whether a hypothesis about a population is correct or to test differences between different groups.

Hypothesis testing is mainly used in the following situations:

- Test the mean, proportion, or variance of a specific population
- Compare the differences between two groups.
- Examine the relationship between variables.

## **2. Types of Hypotheses**

#### **(1) Null Hypothesis (H₀)**

- Indicates a basic assumption or current state.
- Takes the form "no difference" or "no effect."
- Example: The means of the two groups are the same.

#### **(2) Alternative Hypothesis (H₁)**

- The opposite hypothesis to the Null Hypothesis.
- It has the form "There is a difference" or "There is an effect."
- Example: The means of the two groups are different.

## **3. Hypothesis testing procedure**

#### **(1) Hypothesis setting**

- Define H₀ and H₁.

#### **(2) Setting the Significance Level (α)**

- The probability of allowing an error, usually 0.05 (5%), is used.
- If α = 0.05, it means that there is a 5% chance of rejecting the wrong H₀.

#### **(3) Calculating test statistics**

- Calculate statistics (T-statistic, Z-statistic, etc.) from data.

#### **(4) Calculating the P-value**

- The probability that the observed result would occur under H₀.
- If P-value < α, reject H₀.

#### **(5) Drawing a conclusion.**

- Evaluate the validity of the hypothesis by rejecting or failing to reject H₀.

## **4. Major statistical testing methods**

#### **(1) T-Test**

The T-test is a statistical test used to compare differences between means.

**1. One-Sample T-Test**

```
pythonfrom scipy.stats import ttest_1sampdata = [177, 179, 181, 178, 182]t_stat, p_value = ttest_1samp(data, 180)
```

**2. Independent Two-Sample T-Test**

```
pythonfrom scipy.stats import ttest_indgroup1 = [177, 179, 181, 178, 182]group2 = [170, 172, 174, 171, 173]t_stat, p_value = ttest_ind(group1, group2)
```

**3. Paired T-Test**

```
pythonfrom scipy.stats import ttest_relbefore = [177, 179, 181, 178, 182]after = [175, 177, 179, 176, 180]t_stat, p_value = ttest_rel(before, after)
```

#### **(2) ANOVA (Analysis of Variance)**

ANOVA is used to test the difference in means among three or more groups.

**1. One-Way ANOVA**

```
pythonfrom scipy.stats import f_onewaygroup1 = [177, 179, 181, 178, 182]group2 = [170, 172, 174, 171, 173]group3 = [165, 167, 169, 166, 168]f_stat, p_value = f_oneway(group1, group2, group3)
```

**2. Two-Way ANOVA**

#### **(3) Chi-Square Test**

The Chi-Square Test compares observed frequencies with expected frequencies in categorical data.

**1. Test of independence.**

```
pythonfrom scipy.stats import chi2_contingencydata = [[10, 20], [20, 40]]chi2, p_value, _, _ = chi2_contingency(data)
```

**2. Goodness-of-fit test.**

#### **(4) Correlation Test**

The Correlation Test evaluates the linear relationship between two variables.

**1. Pearson Correlation**

```
pythonfrom scipy.stats import pearsonrx = [1, 2, 3, 4, 5]y = [2, 4, 6, 8, 10]corr, p_value = pearsonr(x, y)
```

**2. Spearman Correlation**

```
pythonfrom scipy.stats import spearmanrcorr, p_value = spearmanr(x, y)
```

**3. Kendall Correlation**

```
pythonfrom scipy.stats import kendalltaucorr, p_value = kendalltau(x, y)
```

Statistical hypothesis testing plays a crucial role in data analysis, providing tools to evaluate the validity of a hypothesis based on data. It is essential to select an appropriate testing method and draw reliable conclusions based on the significance level and P-value. By leveraging these testing methods, you can produce more robust and meaningful analytical results!

**顾问 AM60509 (Rank 61) 的解答与建议**:
Statistical hypothesis testing is a fundamental concept in inferential statistics. It allows researchers to make decisions or inferences about a population based on sample data

The  **Goodness-of-Fit test**   is commonly used when you want to test if a sample data follows a hypothesized distribution (like a normal distribution, uniform distribution, etc.).


---

### 技术对话片段 109 (原帖: 【Alpha Inspiration Collections】- Continuously Update置顶的Alpha Idea)
- **原帖链接**: [Commented] 【Alpha Inspiration Collections】- Continuously Update置顶的Alpha Idea.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
The goal of this event is not just about creating alphas, but also fostering a collaborative environment where we can all learn from each other. We strongly believe that collective intelligence is far stronger than individual intellect, and we can't wait to see the synergy that will arise from this event.

Let's start sharing, learning, and growing together!

**[COLLECTIONS]**

- [[Alpha Inspiration] R&D Expenditures and Stock Returns – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] RD Expenditures and Stock ReturnsAlpha Idea.md)
- [[Alpha Inspiration] From Fund Holdings to Alpha – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] From Fund Holdings to AlphaAlpha Idea.md)
- [[Alpha Inspiration] Trade Momentum – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Trade MomentumAlpha Idea.md)
- [[Alpha Inspiration] Combining Fundamental FSCORE and Equity Short-Term Reversals – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Combining Fundamental FSCORE and Equity Short-Term ReversalsAlpha Idea.md)
- [[Alpha Inspiration] Is the Stock in trending? – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Is the Stock in trendingAlpha Idea.md)
- [[Alpha Inspiration] Downside Beta – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Downside BetaAlpha Idea.md)
- [[Alpha Inspiration] Reversal During Earnings-Announcements – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Reversal During Earnings-AnnouncementsAlpha Idea.md)
- [[Alpha Inspiration] Credit Quality Improvement – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Credit Quality ImprovementAlpha Idea.md)
- [[Alpha Inspiration] Donchian Channels – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Donchian ChannelsAlpha Idea.md)
- [[Alpha Inspiration] 12 Month Cycle in Cross-Section of Stocks Returns – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] 12 Month Cycle in Cross-Section of Stocks ReturnsAlpha Idea.md)
- [[Alpha Inspiration] Compound Annual Growth Rate (CAGR) – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Compound Annual Growth Rate CAGRAlpha Idea.md)
- [[Alpha Inspiration] Annuity Method of Depreciation – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Annuity Method of DepreciationAlpha Idea.md)
- [[Alpha Inspiration] Short Interest Effect – Long-Short Version – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Short Interest Effect  Long-Short VersionAlpha Idea.md)
- [[Alpha Inspiration] Post-Earnings Announcement Effect – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Post-Earnings Announcement EffectAlpha Idea.md)
- [[Alpha Inspiration] Beneish M-score – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Beneish M-scoreAlpha Idea.md)
- [[Alpha Inspiration] Currency Momentum Factor – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Currency Momentum FactorAlpha Idea.md)
- [[Alpha Inspiration] Low-volatility anomaly – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Low-volatility anomalyAlpha Idea.md)
- [[Alpha Inspiration] Fung and Hsieh 7-factor model – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Inspiration] Fung and Hsieh 7-factor modelAlpha Idea.md)

**[HOW]**

- Share an article that you have read in the form of a forum post (👉NewPost) and the Alpha inspiration you gained from it and find the related data set / data field to support your idea.
- You can also choose to implement this idea and verify whether it has a signal.
- You are not required to share the Alpha code expression in the post; however, it is not forbidden.
- We encourage you to discuss the posts, explore and improve Alpha inspiration together. Our researchers will also reply to your questions online and give guidance and suggestions.

**[POSTING REQUIREMENTS]**

- **Subject requirements:** Start with [Alpha Inspiration], briefly describing the core idea.
- **Suggested body:**

- Title and author of the article
- Alpha Inspiration description
- Related dataset
- (OPTIONAL) Current performance of P&L or matrix
- Questions and improvement ideas
- Attach TAG: Alpha Idea

**[SWAG]**

- All users who meet the posting requirements and pass the publication audit could receive an item of swag sent by BRAIN after the event ends on 4/30.
- Re-posting of ideas that have been published will not pass the review.

**顾问 AM60509 (Rank 61) 的解答与建议**:
This event emphasizes  **collaboration**  and the power of collective intelligence, which is incredibly exciting. Sharing ideas and inspirations for creating Alphas while learning from others can truly elevate the process of discovering new strategies

Starting with fundamental and analyst datasets is a smart move, especially when looking for less competitive opportunities.


---

### 技术对话片段 110 (原帖: 【Alpha Inspiration Collections】- Continuously Update置顶的Alpha Idea)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha Inspiration Collections】- Continuously Update置顶的Alpha Idea_21034828812183.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
The goal of this event is not just about creating alphas, but also fostering a collaborative environment where we can all learn from each other. We strongly believe that collective intelligence is far stronger than individual intellect, and we can't wait to see the synergy that will arise from this event.

Let's start sharing, learning, and growing together!

**[COLLECTIONS]**

- [[Alpha Inspiration] R&D Expenditures and Stock Returns – WorldQuant BRAIN]([L2] [Alpha Inspiration] RD Expenditures and Stock ReturnsAlpha Idea_23474153293207.md)
- [[Alpha Inspiration] From Fund Holdings to Alpha – WorldQuant BRAIN]([L2] [Alpha Inspiration] From Fund Holdings to AlphaAlpha Idea_23439882899991.md)
- [[Alpha Inspiration] Trade Momentum – WorldQuant BRAIN]([L2] [Alpha Inspiration] Trade MomentumAlpha Idea_23422021382423.md)
- [[Alpha Inspiration] Combining Fundamental FSCORE and Equity Short-Term Reversals – WorldQuant BRAIN]([L2] [Alpha Inspiration] Combining Fundamental FSCORE and Equity Short-Term ReversalsAlpha Idea_23410929308951.md)
- [[Alpha Inspiration] Is the Stock in trending? – WorldQuant BRAIN]([L2] [Alpha Inspiration] Is the Stock in trendingAlpha Idea_23189062385815.md)
- [[Alpha Inspiration] Downside Beta – WorldQuant BRAIN]([L2] [Alpha Inspiration] Downside BetaAlpha Idea_23169073293079.md)
- [[Alpha Inspiration] Reversal During Earnings-Announcements – WorldQuant BRAIN]([L2] [Alpha Inspiration] Reversal During Earnings-AnnouncementsAlpha Idea_23152464526359.md)
- [[Alpha Inspiration] Credit Quality Improvement – WorldQuant BRAIN]([L2] [Alpha Inspiration] Credit Quality ImprovementAlpha Idea_22954622296855.md)
- [[Alpha Inspiration] Donchian Channels – WorldQuant BRAIN]([L2] [Alpha Inspiration] Donchian ChannelsAlpha Idea_22698431404439.md)
- [[Alpha Inspiration] 12 Month Cycle in Cross-Section of Stocks Returns – WorldQuant BRAIN]([L2] [Alpha Inspiration] 12 Month Cycle in Cross-Section of Stocks ReturnsAlpha Idea_22669238853527.md)
- [[Alpha Inspiration] Compound Annual Growth Rate (CAGR) – WorldQuant BRAIN]([L2] [Alpha Inspiration] Compound Annual Growth Rate CAGRAlpha Idea_22666070312343.md)
- [[Alpha Inspiration] Annuity Method of Depreciation – WorldQuant BRAIN]([L2] [Alpha Inspiration] Annuity Method of DepreciationAlpha Idea_22584944428823.md)
- [[Alpha Inspiration] Short Interest Effect – Long-Short Version – WorldQuant BRAIN]([L2] [Alpha Inspiration] Short Interest Effect  Long-Short VersionAlpha Idea_22552235242903.md)
- [[Alpha Inspiration] Post-Earnings Announcement Effect – WorldQuant BRAIN]([L2] [Alpha Inspiration] Post-Earnings Announcement EffectAlpha Idea_22533162481815.md)
- [[Alpha Inspiration] Beneish M-score – WorldQuant BRAIN]([L2] [Alpha Inspiration] Beneish M-scoreAlpha Idea_22498529784471.md)
- [[Alpha Inspiration] Currency Momentum Factor – WorldQuant BRAIN]([L2] [Alpha Inspiration] Currency Momentum FactorAlpha Idea_22498347519511.md)
- [[Alpha Inspiration] Low-volatility anomaly – WorldQuant BRAIN]([L2] [Alpha Inspiration] Low-volatility anomalyAlpha Idea_22453395841175.md)
- [[Alpha Inspiration] Fung and Hsieh 7-factor model – WorldQuant BRAIN]([L2] [Alpha Inspiration] Fung and Hsieh 7-factor modelAlpha Idea_22394208583703.md)

**[HOW]**

- Share an article that you have read in the form of a forum post (👉NewPost) and the Alpha inspiration you gained from it and find the related data set / data field to support your idea.
- You can also choose to implement this idea and verify whether it has a signal.
- You are not required to share the Alpha code expression in the post; however, it is not forbidden.
- We encourage you to discuss the posts, explore and improve Alpha inspiration together. Our researchers will also reply to your questions online and give guidance and suggestions.

**[POSTING REQUIREMENTS]**

- **Subject requirements:** Start with [Alpha Inspiration], briefly describing the core idea.
- **Suggested body:**

- Title and author of the article
- Alpha Inspiration description
- Related dataset
- (OPTIONAL) Current performance of P&L or matrix
- Questions and improvement ideas
- Attach TAG: Alpha Idea

**[SWAG]**

- All users who meet the posting requirements and pass the publication audit could receive an item of swag sent by BRAIN after the event ends on 4/30.
- Re-posting of ideas that have been published will not pass the review.

**顾问 AM60509 (Rank 61) 的解答与建议**:
This event emphasizes  **collaboration**  and the power of collective intelligence, which is incredibly exciting. Sharing ideas and inspirations for creating Alphas while learning from others can truly elevate the process of discovering new strategies

Starting with fundamental and analyst datasets is a smart move, especially when looking for less competitive opportunities.


---

### 技术对话片段 111 (原帖: 【Alpha Template Collections】- Continuously UpdatePinnedAlpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha Template Collections】- Continuously UpdatePinnedAlpha Template_24472586368279.md
- **时间**: 1 year ago

**提问/主帖背景 (YW42946)**:
Hello, Community!

An Alpha template is a structured approach used to discover Alpha signals. It's built on a foundation of economic logic and involves a sequence of operators designed to hone in on the template's idea.

A key feature of Alpha templates is their adaptability, allowing for the interchange of certain options to discover new Alphas. This flexibility enables the exploration of a vast "Alpha Space," offering myriad of potential combinations to discover many good Alphas.

Check out the collections and example below:

**Collections:**

- [[Alpha Template] Time-Series Sentiment Comparison Template – WorldQuant BRAIN]([L2] [Alpha Template] Time-Series Sentiment Comparison TemplateAlpha Template_24756474790551.md)
- [[Alpha Template] Understanding Time-Series Profit to Size Comparison Template – WorldQuant BRAIN]([L2] [Alpha Template] Understanding Time-Series Profit to Size Comparison TemplateAlpha Template_24931371359639.md)
- [[Alpha Template] How can you leverage option Greeks to create Alphas – WorldQuant BRAIN]([L2] [Alpha Template] How can you leverage option Greeks to create AlphasAlpha Template_25102833580567.md)
- [[Alpha Template] How can you adopt CAPM to other data – WorldQuant BRAIN]([L2] [Alpha Template] How can you adopt CAPM to other dataAlpha Template_25274612269335.md)
- [[Alpha Template] Potential Steps to Further Leverage CAPM Beta – WorldQuant BRAIN]([L2] [Alpha Template] Potential Steps to Further Leverage CAPM BetaAlpha Template_25445040263191.md)
- [[Alpha Template] How can you use estimate and actual earnings data to create Alphas – WorldQuant BRAIN]([L2] [Alpha Template] How can you use estimate and actual earnings data to create AlphasAlpha Template_25775603889431.md)
- [[Alpha Template] How do you utilize different periods of estimation – WorldQuant BRAIN]([L2] [Alpha Template] How do you utilize different periods of estimationAlpha Template_27963407565975.md)
- [[Alpha Template] How can you utilize DuPont Analysis to create Alphas – WorldQuant BRAIN]([Commented] [Alpha Template] How can you utilize DuPont Analysis to create AlphasAlpha Template_28298364912151.md)
- [[Alpha Template] How can you utilize the Gordon Growth Model to create Alphas – WorldQuant BRAIN]([L2] [Alpha Template] How can you utilize the Gordon Growth Model to create Alphas被推荐的Alpha Template_28676006454167.md)
- [[Alpha Template] How can you utilize the PEG to create Alphas – WorldQuant BRAIN]([Commented] [Alpha Template] How can you utilize the PEG to create AlphasAlpha Template_29985532824343.md)

**Example:**

Let's consider a basic example to illustrate the idea, given the hypothesis that a company's stock price may trend upward if its EPS has a strong trend compared to its peers. One implementation may look like the following:

> group_rank(ts_rank(eps, 252, industry)

The above expression is straightforward:

- First, it computes the company's EPS's time-series rank. The larger the value, the higher the company's EPS compared to its past.
- Secondly, it normalizes for industry effect by applying a group_rank. The larger the value, the higher the company's EPS growth compared to its peers.

You can generalize the Alpha into the following:

> <group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>), <group>)

The above has the following components:

- <company_fundamentals>: Originally, the implementation uses EPS based on the hypothesis, but this idea can easily expand to other fundamental data, such as DPS, CPS, BPS, EBIT, sales, etc.
- <ts_compare_op>: It uses ts_rank in the original implementation. There may be several alternative time-series operators that serve a similar purpose, such as ts_zscore, ts_delta, ts_avg_diff, etc.
- <group_compare_op>:  It uses group_rank. Similar to the <ts_compare_op> case, you can also consider group_zscore, group_neutralize to control for a given group's effect.
- <days>, <group>: You can also change the <ts_compare_op>'s lookback days, or the peer's definition for the <group_compare_op>.

This modular approach allows the template to be highly customizable. Each step is interchangeable and can be tailored to suit the specific nuances of your Alpha's hypothesis.

The Alpha template isn't just a method but a journey through the Alpha Space, seeking that optimal combination that lights up the path to more Alpha submissions.

I hope this gives you some idea about the Alpha template. Feel free to share your thoughts and dive deeper into this fascinating topic!

**顾问 AM60509 (Rank 61) 的解答与建议**:
This article shines by presenting a well-structured and innovative framework for Alpha creation. Its modular design empowers analysts to adapt the method to a wide array of financial metrics and market conditions, fostering creativity in hypothesis testing. I especially like how you highlighted their flexibility, making it easy to adapt them for different hypotheses and data types.

The example using EPS trends, combined with the use of  **group_rank**  and  **ts_rank**  **,**  provides a clear and practical illustration of how to implement these ideas effectively.


---
