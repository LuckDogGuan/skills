# Best Data Sources for Out-of-Sample Edge

- **链接**: https://support.worldquantbrain.com[Commented] Best Data Sources for Out-of-Sample Edge_35086341106327.md
- **作者**: SG91420
- **发布时间/热度**: 9个月前, 得票: 23

## 帖子正文

Which dataset type (price, fundamentals, alternative) has given you the best incremental edge in OS performance?

---

## 讨论与评论 (8)

### 评论 #1 (作者: MY21251, 时间: 9个月前)

From my experience, there’s no one “best” type—each shines in different scenarios—but alternative data has given me the most surprising incremental OS edge, while fundamentals offer the steadiest. Alternative data  often isn’t priced in as quickly as price/fundamentals, so signals here hold up better OS. For example, tracking a retailer’s weekly delivery volumes let me anticipate quarterly sales beats  before earnings—way more reliable OS than just price momentum. That said, fundamentals (e.g., consistent ROE growth, stable gross margins) are the backbone: their trends are slower to reverse, so alphas built on them rarely collapse OS. Price data works for short-term signals, but it’s easier to overfit, so its OS edge is slimmer unless paired with other data. Curious if others have found specific alternative sub-types (like ESG or satellite imagery) that punch above their weight?

---

### 评论 #2 (作者: 顾问 CT48231 (Rank 2), 时间: 9个月前)

During the entire process of simulating alphas on the platform, I noticed that some datasets, particularly fundamental and price-volume, seem quite reliable, and you might consider using these ones.

---

### 评论 #3 (作者: LD50548, 时间: 9个月前)

In my experience,  **there isn’t a single dataset type that dominates OS** —it really depends on the design of the alpha and the holding horizon. That said, I’ve found that combining  **fundamentals for stability**  with  **alternative data for novelty**  tends to give the best incremental edge. Fundamentals provide the long-term anchor (less regime-sensitive), while alternative signals can capture shifts the market hasn’t fully priced in yet.

Price-based features are still useful, but as others mentioned, they’re more prone to overfitting unless carefully regularized or blended with other fields. For me, the most consistent OS edge came from  **hybrid signals** —for example, pairing earnings quality (fundamental) with sentiment or crowding (alternative). This mix helps reduce correlation and keeps the alpha resilient.

Curious if anyone has tested the new neutralization categories on these datasets—wondering if certain neutralizations improve OS robustness more for alternative vs. fundamentals

---

### 评论 #4 (作者: AG14039, 时间: 9个月前)

In my experience running alpha simulations on the platform, certain datasets—especially fundamentals and price-volume—tend to be more stable and reliable. These can serve as strong starting points when designing alphas, providing a solid foundation for building predictive signals.

---

### 评论 #5 (作者: SD92473, 时间: 9个月前)

From my experience, it really depends on the alpha theme, but in terms of  **incremental out-of-sample (OS) edge** :

- **Price data** : Most consistent and robust. Purely price/volume-based signals (momentum, mean reversion, liquidity) usually generalize better OS because they’re stable and directly tied to tradable dynamics. Downside is that they’re highly competed over, so marginal edge can be small.
- **Fundamentals** : Tend to add real incremental value when combined with price signals. Ratios like valuation, quality, and profitability can improve persistence, especially across longer horizons. OS performance is decent if you manage sector/industry biases carefully.
- **Alternative data** : Can deliver big alpha in-sample, but OS is mixed—often noisy, less liquid, or subject to revision/coverage issues. Works best as a  *complement*  to price/fundamentals rather than as a standalone driver.

---

### 评论 #6 (作者: LB76673, 时间: 9个月前)

Price datasets often provide the most consistent base signals, but they’re also the most crowded. Fundamentals tend to add longer-horizon stability, while alternative data like sentiment or short interest can provide sharper but noisier short-term edges. The best incremental OS performance usually comes from layering fundamentals or alternative data on top of price signals, since they reduce correlation and improve robustness rather than relying on price alone. The “best” really depends on how you balance horizon, turnover, and correlation, but in practice combining types often outperforms leaning on a single dataset.

---

### 评论 #7 (作者: RP41479, 时间: 9个月前)

Alt data often beats OS, fundamentals give steady trends, price signals risk overfitting. Anyone seen ESG or satellite data outperform?

---

### 评论 #8 (作者: AG14039, 时间: 8个月前)

Exactly — price datasets give a reliable foundation but are heavily used, so adding fundamentals or alternative data often creates true diversification. Fundamentals contribute longer-horizon stability, while alternative datasets like sentiment or short interest can capture sharper short-term signals. Layering these on top of price-based alphas usually improves out-of-sample performance by reducing correlation and enhancing robustness. Ultimately, the optimal mix depends on your desired horizon, turnover tolerance, and correlation targets, but multi-type combinations generally outperform single-dataset approaches.

---

