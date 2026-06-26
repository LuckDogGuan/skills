# Research Paper: Bid and Ask Prices of Index Put Options: Which Predicts the Underlying Stock Returns?Pinned

- **链接**: https://support.worldquantbrain.com[L2] Research Paper Bid and Ask Prices of Index Put Options Which Predicts the Underlying Stock ReturnsPinned_15233936157847.md
- **作者**: NL41370
- **发布时间/热度**: 6 months ago, 得票: 19

## 帖子正文

**Abstract:**

In this study, we separately estimate the implied volatility from the bid and ask prices of deep out-of-the-money (OTM) put options on the S&P500 index. We find that the implied volatility of ask prices has stronger predictive power for stock returns than does the implied volatility of bid prices. We identify two sources of the better performance of the ask price implied volatility: one is its stronger predictive power during economic recessions and in the presence of increasing intermediary capital risk, and the other is its richer information about the future market variance risk premium.

Key ideas:

- Page 9 paragraph 2
- Page 11 paragraph 2

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

ask price

opt4_ask

[**Option4**](https://platform.worldquantbrain.com/data/data-sets/option4)

bid price

opt4_bid

[**Option4**](https://platform.worldquantbrain.com/data/data-sets/option4)

Author: Jian Chen, Yangshu Liu

Year: 2020

Link:  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3285854](https://ssrn.com/abstract=3285854)

---

## 讨论与评论 (1)

### 评论 #1 (作者: TN67143, 时间: 2 years ago)

Hi,

Can we analyze this paper in the following ways?

1. From the first sentence of the abstract, the author wrote: In this study, we separately estimate the implied volatility from the bid and ask prices of deep out-of-the-money (OTM) put options on the S&P500 index.

From my limited perspective, the central themes of this paper is implied volatility. They are a predictive signal of future prices movement. We can look further in details at Investopedia:  [https://www.investopedia.com/terms/i/iv.asp](https://www.investopedia.com/terms/i/iv.asp) .
We could build high quality Alphas formulas from this signal. They are positively associated with the outlook of the security. The higher the implied volatility, the more prospective the outlook of the securities are.

There are multiples ways to estimates the implied volatility of a security. Here, the authors calculate two estimates of them using the bid prices and ask prices of the put options.

The instruments space to look at is deep out-of-the-money (OTM) put options on the S&P500 index. This shall be a quite extreme space to look at, since they represent periods when the present market prices of the options are far below the designated prices, showing a considerable gap between expectation and realized prices of the base instrument.

2. In the second sentence, the authors wrote: We find that the implied volatility of ask prices has stronger predictive power for stock returns than does the implied volatility of bid prices.

Here, among implied volatility estimates of ask prices and bid prices, the authors find that the estimates using ask prices has stronger predictive power than put prices when predicting stock returns.

This may help us to follow more at the implied volatility using ask prices.

Here, we could potentially identify our intial sources for Alphas development: implied_volatility_ask_prices.

There are multiple ways to calculate the implied volatility of an instruments when knowing their prices. One of them could be refer from Black-Scholes formulas.

But the investors tend to buy options when the respective implied volatility is low, forecasting an increase in the options' price, reflecting a positive outlook for the future movements and so on (We can examine further at the above article on Investopedia). This may signal a positive correlation between the options ask and bid prices and implied volatility.

From the postive and predictive association of implied volatility, we can infer the positive association of option bid and ask prices with the stock market returns.

This resulting our initial Alphas formulas: opt4_ask or opt4_bid.

This datafield usage is both available and minimal to our GLB region and the current MAPC competitions.

From this positive association of opt4_ask, opt4_bid datafields, we could further enhance our signals with suitable operators usages.

3. In the final sentence of the abstract, the authors wrote: We identify two sources of the better performance of the ask price implied volatility: one is its stronger predictive power during economic recessions and in the presence of increasing intermediary capital risk, and the other is its richer information about the future market variance risk premium.

To add more information, the authors present two other supporting factors that could enhance this relationship:
a. During economic recessions and in the presence of increasing intermediary.
b. Richer information about the future market variance risk premium.

4. Overall, this paper present us with two positive association datafields with stock returns: opt4_ask (ask price) and opt4_bid (bid price).

What do you think about the above analysis?

Thank you.

---

