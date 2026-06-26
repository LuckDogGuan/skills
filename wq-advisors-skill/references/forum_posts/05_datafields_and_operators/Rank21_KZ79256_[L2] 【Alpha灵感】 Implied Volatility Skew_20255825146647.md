# 【Alpha灵感】 Implied Volatility Skew

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】 Implied Volatility Skew_20255825146647.md
- **作者**: FL11741
- **发布时间/热度**: 2 years ago, 得票: 3

## 帖子正文

论文题目：What Does Individual Option Volatility Smirk Tell Us about Future Equity Returns?

作者：Yuhang Xing, Xiaoyan Zhang and Rui Zhao

链接： [What Does Individual Option Volatility Smirk Tell Us About Future Equity Returns? by Xiaoyan Zhang, Rui Zhao, Yuhang Xing :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1107464)

摘要：
The shape of the volatility smirk has significant cross-sectional predictive power for future 
equity returns. Stocks exhibiting the steepest smirks in their traded options underperform 
stocks with the least pronounced volatility smirks in their options by around 10.9% per year on a risk-adjusted basis. This predictability persists for at least six months, and firms with the steepest volatility smirks are those experiencing the worst earnings shocks in the following quarter. The results are consistent with the notion that informed traders with negative news prefer to trade out-of-the-money put options, and that the equity market is slow in incorporating the information embedded in volatility smirks.

Datafield：opt4_30_put_vola, opt4_30_call_vola

Universe：Top 3000

Neutralizaton：Market （搜索Sector，Industry均无结果）

Alpha表达式：（put_vola - call_vola）/ (put_vola / 2 + call_vola / 2)

回测结果：


> [!NOTE] [图片 OCR 识别内容]
> S,00OK
> OOOK
> 4,0OOK
> Z,0OOK
> 0/09/2012
> US Pn  1,902.82K
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
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
> 1.73
> 20.51%
> 1.28
> 11.229
> 6.449
> 10.959600


---

## 讨论与评论 (4)

### 评论 #1 (作者: FL11741, 时间: 2 years ago)

改进建议：上述Alpha的correlation较高，进一步探究可以参考论文：

[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2591775](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2591775)

其中对于相似想法的论文做了非常清晰的总结概括，涵盖多个不同的表达式，但比较遗憾的是，该论文本身的idea由于数据集缺失不同strike level下的成交量及open interest数据，并不能够还原。

---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

同学您好，看到您写道“由于数据集缺失不同strike level下的成交量及open interest数据，并不能够还原”。

建议您多多尝试，在BRAIN平台有着非常多的option数据，尤其美国区域中option4和option6这一数据集是非常全面的。您说的数据，我本人都有做过，建议多多探索。

---

### 评论 #3 (作者: FL11741, 时间: 2 years ago)

好的，我之前完全没有接触过期权，可能有些数据的说明不能够完全理解被我忽略掉了，之后会去研究的，谢谢老师！

---

### 评论 #4 (作者: WL13229, 时间: 2 years ago)

[FL11741](/hc/en-us/profiles/18515544005527-FL11741)

[【Alpha灵感】关于未来的股票回报，个股期权波动率Smirk告诉了我们什么？]([L2] 【Alpha灵感】关于未来的股票回报个股期权波动率Smirk告诉了我们什么_20163362610711.md)

您可以参考一下这篇post，有些不错的讨论

---

