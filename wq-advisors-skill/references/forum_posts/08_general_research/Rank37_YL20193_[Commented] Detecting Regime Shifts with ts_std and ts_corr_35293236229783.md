# Detecting Regime Shifts with ts_std and ts_corr

- **链接**: https://support.worldquantbrain.com[Commented] Detecting Regime Shifts with ts_std and ts_corr_35293236229783.md
- **作者**: AK98027
- **发布时间/热度**: 8个月前, 得票: 23

## 帖子正文

High TS volatility often signals regime change.
Computing rolling  `ts_std(signal, N)`  or correlations between signals ( `ts_corr(alpha1, alpha2, N)` ) can reveal clustering risks.
I’ve used this to dynamically adjust decay lengths and exposure caps in OS testing.

---

## 讨论与评论 (2)

### 评论 #1 (作者: 顾问 YL20193 (Rank 37), 时间: 8个月前)

tiebreaker..........

---

### 评论 #2 (作者: HN45379, 时间: 8个月前)

###### 

Great point — using ts_std and ts_corr as regime detectors is a smart and practical approach. I’ve also found that spikes in rolling volatility or sudden drops in correlation often precede structural shifts in signal behavior. Dynamically tuning decay or exposure based on these indicators can really help maintain stability during turbulent periods. It’s an elegant way to blend adaptability with quantitative discipline — thanks for sharing this insight!

---

