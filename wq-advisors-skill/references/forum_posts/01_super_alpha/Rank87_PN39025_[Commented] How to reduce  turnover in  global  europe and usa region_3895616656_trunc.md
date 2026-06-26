# How to reduce  turnover in  global , europe and usa region ?

- **链接**: https://support.worldquantbrain.com[Commented] How to reduce  turnover in  global  europe and usa region_38956166564503.md
- **作者**: VP44724
- **发布时间/热度**: 3个月前, 得票: 3

## 帖子正文

High turnover is a common issue when developing alphas on the BRAIN platform, especially when signals react too quickly to short-term market noise. One simple and effective way to control turnover is by adjusting the simulation settings, particularly truncation and decay.

A useful starting point is to set truncation around 0.096. Truncation helps limit extreme weights in the portfolio, which reduces excessive rebalancing caused by large signal changes. By capping the position size, the strategy becomes more stable and prevents sudden shifts in allocation across stocks.

Another important parameter is decay. Applying some level of decay smooths the signal over time, which reduces the frequency of position changes. Instead of reacting immediately to every small fluctuation, the alpha gradually incorporates new information. This smoothing effect can significantly lower turnover while maintaining signal strength.

In practice, combining truncation ≈ 0.096 with a moderate decay value often leads to a better balance between performance and trading activity. Lower turnover not only improves implementation feasibility but can also help maintain stronger Sharpe ratios in many cases.

Consultants facing high turnover issues should experiment with these settings before modifying the alpha logic itself. Small adjustments in simulation parameters can sometimes make a meaningful difference in production stability and overall performance.

---

## 讨论与评论 (1)

### 评论 #1 (作者: 顾问 PN39025 (Rank 87), 时间: 2个月前)

I'm having this problem, thank you for sharing, it's quite useful for future research. Thank you, I hope you can share more good methods with me.

---

