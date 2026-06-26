# Using ts_rank to Detect Momentum Reversals

- **链接**: https://support.worldquantbrain.com[Commented] Using ts_rank to Detect Momentum Reversals_35293195202327.md
- **作者**: AK98027
- **发布时间/热度**: 8个月前, 得票: 22

## 帖子正文

Instead of raw returns, computing  `ts_rank(price, N)`  can highlight overextended moves in both directions.
Combining it with  `ts_arg_min(volatility, M)`  helps identify recent calm periods before rebounds.
I’ve found this approach often improves OS Sharpe without overfitting short spikes.

---

## 讨论与评论 (2)

### 评论 #1 (作者: 顾问 YL20193 (Rank 37), 时间: 8个月前)

tiebreaker..........

---

### 评论 #2 (作者: HN45379, 时间: 8个月前)

That’s a clever technique — using ts_rank to gauge relative positioning within a time window gives a much smoother perspective than raw returns. Pairing it with ts_arg_min(volatility, M) adds an interesting contrarian angle, catching reversals right after stable phases. I like how this balances signal timing and robustness without overreacting to short-term noise. Definitely worth experimenting with different lookback combinations to fine-tune the sensitivity!

---

