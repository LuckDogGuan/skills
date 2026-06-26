# [Sharing] Tips to Bypass Fundamental Dataset Limit

- **链接**: https://support.worldquantbrain.com[Commented] [Sharing] Tips to Bypass Fundamental Dataset Limit_34336141625623.md
- **作者**: LD50548
- **发布时间/热度**: 10个月前, 得票: 55

## 帖子正文

Previously, I encountered an overuse error with fundamental data because the ratio of alpha using fundamentals exceeded 30%, which prevented me from submitting further. Later, I found a solution by splitting the alpha ideas and combining them with other datasets such as Price Volume or Analyst. This way, I could maintain the main signal while reducing the fundamental ratio below the limit.

In addition, I also experimented with transforming fundamental signals to lower their dataset recognition rate. This approach allowed me to submit again normally without significantly reducing the alpha’s performance.

---

## 讨论与评论 (8)

### 评论 #1 (作者: TP85668, 时间: 10个月前)

This is a very practical tip. Many users face the same issue with fundamental dataset limits, and your approach of splitting signals and mixing with other datasets like Price-Volume or Analyst is both creative and effective. It not only keeps the core strength of the fundamental signal but also ensures compliance with submission rules. The idea of transforming fundamental signals to reduce dataset recognition is also smart, as it shows how preprocessing can help bypass technical constraints without hurting performance. Thanks for sharing — it’s a useful lesson for anyone designing alphas with heavy fundamental usage.

---

### 评论 #2 (作者: ZK79798, 时间: 10个月前)

Thanks for sharing! Your solution to handle the fundamental ratio limit is really insightful and gives me useful ideas.

---

### 评论 #3 (作者: NT84064, 时间: 10个月前)

This is a very practical and useful share. The dataset ratio limit for fundamentals can feel restrictive, especially since fundamentals often provide strong orthogonal signals compared to pure price-volume factors. Your suggestion of blending them with price or analyst datasets is smart because it not only lowers the fundamental ratio but can also improve robustness through diversification. I’ve also found that transformations like  `delta(fundamental, d)`  or cross-sectional operations like  `group_neutralize(fundamental, industry)`  sometimes make the system categorize the signal differently, thereby reducing recognition as “pure” fundamentals. Another trick is layering fundamental features within composite expressions—e.g.,  `rank(fundamental) * zscore(volume)` —which balances dataset contributions. Have you tested whether certain smoothing or non-linear operators (like  `signed_power`  or  `log` ) also reduce dataset ratio classification? That could be another way to make fundamentals usable while staying compliant.

---

### 评论 #4 (作者: 顾问 HY90970 (Rank 54), 时间: 9个月前)

But, this practice may impact the value factor negatively. It is not recommended to do so until alpha is based on some ratio or idea.

---

### 评论 #5 (作者: AG14039, 时间: 9个月前)

This is a very practical insight. Fundamental signals often face strict ratio limits, yet they provide valuable orthogonal information beyond price-volume factors. Blending fundamentals with price or analyst datasets is smart—it lowers the fundamental ratio while adding diversification and robustness. Techniques like  `delta(fundamental, d)`  or cross-sectional operations such as  `group_neutralize(fundamental, industry)`  can also influence how the system classifies the signal, sometimes making it less “pure” fundamental. Another effective approach is embedding fundamentals within composite expressions—for example,  `rank(fundamental) * zscore(volume)` —to balance contributions. Additionally, experimenting with smoothing or non-linear operators like  `signed_power`  or  `log`  might further help manage dataset classification while keeping fundamentals in play.

---

### 评论 #6 (作者: AG14039, 时间: 9个月前)

This is a highly practical suggestion. Many participants struggle with fundamental dataset limits, and your approach of splitting signals and blending them with Price-Volume or Analyst datasets is both clever and effective. It preserves the core predictive power of fundamentals while staying within submission rules. Transforming fundamentals to reduce dataset recognition is another smart tactic, demonstrating how preprocessing can navigate technical constraints without compromising performance. A very useful lesson for anyone designing alphas with significant fundamental exposure.

---

### 评论 #7 (作者: RP41479, 时间: 9个月前)

Practical tip! Splitting fundamental signals and mixing with Price-Volume or Analyst datasets preserves core strength while complying with limits. Transforming fundamentals to reduce dataset recognition is smart preprocessing, helping maintain performance despite constraints—valuable insight for alpha design.

---

### 评论 #8 (作者: 顾问 HY90970 (Rank 54), 时间: 9个月前)

Hi @LD50548 !

Is dataset limit applicable only for fundamental or for other data categories also? Can anyone please answer.

---

