# 【Alpha灵感】Volatility Spreads and Expected Stock Returns

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Volatility Spreads and Expected Stock Returns_20265313128215.md
- **作者**: AZ81686
- **发布时间/热度**: 2 years ago, 得票: 8

## 帖子正文

标题：Volatility Spreads and Expected Stock Returns

作者：Turan G. Bali, Armen Hovakimian

链接： [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1481279](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1029197)

Abstract:

We examine the relation between expected future volatility (options' implied volatility) and the cross-section of expected returns. A trading strategy buying stocks in the highest implied volatility quintile and shorting stocks in the lowest implied volatility quintile generates insignificant returns. A similar strategy using one-month lagged realized volatility generates significantly negative returns. To investigate the differences and interactions between alternative measures of total risk, we estimate three principal components based on realized volatility, call implied and put implied volatility. Long-short trading strategies generate significant returns only for the second and the third principal components. We find that the second principal component is related to the realized-implied volatility spread which can be viewed as a proxy for volatility risk. We find that the third principal component is related to the call-put implied volatility spread that reflects future price increase of the underlying stock.

有用的变量及观点：Call Implied Volatility–Put IV spread (proxy for jump risk); Realized Vol–IV spread (proxy for volatility risk); 上述的risks有补偿; The double sorts on the volatility spreads clearly indicate that jump risk and volatility risk are distinct in the cross sectional pricing of individual stocks；trading volume of options is found to be informative for the future volume and volatility of underlying stocks；The signifificance of information spillover is stronger in options/stocks with higher volatility spreads.


> [!NOTE] [图片 OCR 识别内容]
> Table 2
> Fama-MacBeth Regressions of Stock Returns on Realized and
> Implied Volatilities
> Coeff。
> f-Stat。
> Coeff。
> f-Stat。
> Coeff。
> t-Stat。
> Coeff。
> f-Stat。
> Intercept
> 0.014
> 2.7
> 0.013
> 1.7
> 0.017
> 2.3
> 0.009
> 1.7
> Realized
> 0.011
> 0.9
> 0.014
> 一2.3
> Volatility
> Call Volatility
> 0.008
> 一0.4
> 0.124
> 6.4
> Put Volatility
> 0.017
> -0.9
> 0.101
> 6.1


Universe：小市值/top3000; Neu: Market

数据： Volatility Data中的historical_volatility，implied_volatility_call；implied_volatility_put和volume

核心Expressions/Operators:  Call Implied Volatility–Put IV spread (proxy for jump risk); Realized Vol–IV spread (proxy for volatility risk)


> [!NOTE] [图片 OCR 识别内容]
> 12.5M
> 10M
> 7,500K
> 5,00OK
> 2,5OOK
> 2013
> 2015
> 2017
> 2019
> 2021
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.6620.3791.4515.48910.12915.209o。
  
> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Highest Correlation
> Last Run: Tue, 01/02/2024,7:05 PM
> 0.6
> IOOM
> IM
> 訾
> IOk
> 昱
> }
> 100
> 89
> 82
> 0?2
> 0?
> 01
> ^9
> 9
> 01
> 8
> -0.9
> -0.8
> 令
> -0.5
> -0.3
> 0.0
> 0.3
> 0.6
> 0.8
> 0.9
> -0.2
> -0.1
> 0.1
> 0.4
> 0.9...
> -0.1. .
> 0.5..
> 0.8..
> 0.0.
> 0.1. 
> 0.2.
> 0.3.
> 0.4.
> 0.6.
> -1.0.
> -0.9.
> -0.7 .
> 8
> -0.5.
> -0.4.
> -0.2.
> -0.3


---

## 讨论与评论 (2)

### 评论 #1 (作者: Nguyen Dang Huynh(HN14753), 时间: 2 years ago)

你好，我不太明白alpha背后的含义。 您能否分享有关想法实施过程的详细信息？ 如果你能分享 alpha 表达式那就太好了。 谢谢

---

### 评论 #2 (作者: AZ81686, 时间: 2 years ago)

[Nguyen Dang Huynh(HN14753)](/hc/en-us/profiles/13678373208599-Nguyen-Dang-Huynh-HN14753)  谢谢你的跟踪，我感觉可以直接看回归结果table2截图，作者是发现：1、如果只是拿单独一个波动去回归，结果是不显著的；2、如果三个一起回归，结果三个波动都显著；你可以看回归系数，realized vol, call vol都是正，put vol的系数是负；所以进一步的他做了个“包装”，给出了两个新变量：(realized vol - option implied vol)和(call vol - put vol) [可以观察下回归系数正负和新变量设置之间的关系]

---

