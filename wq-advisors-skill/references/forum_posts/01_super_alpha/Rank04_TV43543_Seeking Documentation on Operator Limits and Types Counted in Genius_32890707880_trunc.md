# Seeking Documentation on Operator Limits and Types Counted in Genius

- **链接**: https://support.worldquantbrain.comSeeking Documentation on Operator Limits and Types Counted in Genius_32890707880983.md
- **作者**: 顾问 TV43543 (Rank 4)
- **发布时间/热度**: 1年前, 得票: 14

## 帖子正文

Hello everyone,

I'm exploring the use of operators in Genius and would like to know if there are any official documents that clearly outline the following:

1. The maximum number of operators a single account (nick) can use, support API ?.
2. Which operators are counted for Genius and which are not.
3. If my alpha uses operators not counted for Genius, will my op/alpha metric increase?

Thanks

---

## 讨论与评论 (14)

### 评论 #1 (作者: KK61864, 时间: 1年前)

Hii   [顾问 TV43543 (Rank 4)](/hc/en-us/profiles/10872909017239-顾问 TV43543 (Rank 4))

Maximum number of operators that can be used is around  **167 at Grand Master level and around 134 at Master level.**

For Genius -  **Regular operators are counted.Combo and Selection operatorsare** not counted.

All operators applied to alpha are counted, this affects operator/alpha, **if you use more operators then operator/alpha will increase.**

---

### 评论 #2 (作者: NT63388, 时间: 1年前)

@ [顾问 TV43543 (Rank 4)](/hc/en-us/profiles/10872909017239-顾问 TV43543 (Rank 4)) 
All of your questions are actually answered in the Genius guidelines above.

You can refer to:

1. The maximum number of operators a single account (nick) can use, support API?
=> Depending on the Genius level (Gold, Expert, Master, GrandMaster), the maximum number of operators (OP) that can be used varies. Additionally, even within the same level, there might be slight differences in the number of OPs. You can refer to the list of usable operators at:  [https://platform.worldquantbrain.com/learn/operators](https://platform.worldquantbrain.com/learn/operators)

2. Which operators are counted for Genius and which are not?
=> From the list of operators in the answer to question 1 above, operators used for Super-Alpha are not counted (this is a new update for Genius this time).

3. If my alpha uses operators not counted for Genius, will my op/alpha metric increase?
=> It will be counted.

---

### 评论 #3 (作者: SK90981, 时间: 1年前)

Efficient operator usage is key! At Genius, focus on regular operators since combo/selection aren’t counted. Balance is crucial for operator/alpha.

---

### 评论 #4 (作者: SP39437, 时间: 1年前)

The maximum number of operators you can use depends on your Genius level. For example, GrandMaster-level consultants can access around 167 operators, while Master-level users have access to approximately 134. Note that even within the same tier, there might be slight variations depending on updates or permissions. You can always check your eligible operators here:  [https://platform.worldquantbrain.com/learn/operators](https://platform.worldquantbrain.com/learn/operators) .

When it comes to Genius metrics, only regular operators are counted. Combo and Selection operators—commonly used in SuperAlphas—do not count toward your Genius operator total. However, all operators used in any alpha submission will still affect your operator-per-alpha (OP/Alpha) metric. That means using non-Genius operators can still increase your OP/Alpha ratio, even if they don’t help your Genius score directly.

Question:
Have you found an efficient way to keep your OP/Alpha low while still maintaining signal quality and diversity for Genius ranking?

---

### 评论 #5 (作者: TP19085, 时间: 1年前)

The number of operators available in the Genius platform depends on your level. For instance, GrandMaster-level users typically have access to around 167 operators, while Master-level users can use about 134. These counts may vary slightly depending on recent updates or individual permissions. To see your specific set, you can check directly at:  [https://platform.worldquantbrain.com/learn/operators](https://platform.worldquantbrain.com/learn/operators) .

Importantly, only  **regular operators**  count toward your  **Genius operator total** . Combo and Selection operators—used mainly in SuperAlpha development—don’t contribute to Genius progress, but they  *do*  affect your  **Operator per Alpha (OP/Alpha)**  metric. So, even though they don’t raise your Genius score, overusing them can still impact leaderboard efficiency.

Keeping OP/Alpha low while maintaining diversity and signal quality is a balancing act. One method is to build layered logic using multi-functional operators like  `decay_linear` ,  `rank` , or  `ts_corr` , which offer depth without bloating the operator count.

What techniques have worked best for you in optimizing this trade-off between complexity and efficiency?

---

### 评论 #6 (作者: AK52014, 时间: 1年前)

Your operator access depends on Genius level—GrandMasters get ~167, Masters ~134. Only regular operators count toward Genius metrics, but all affect OP/Alpha. How do you maintain low OP/Alpha while ensuring strong, diverse signals?

---

### 评论 #7 (作者: QZ67721, 时间: 1年前)

Hello, the previous consultant has mentioned that  **Grand Master users have full access to all operators (167 operators in total)** , and  **Master users have 134 operators** . I’d like to add that  **Expert users have approximately 110 operators** , while  **Gold users have around 79 operators** —these are estimates based on the number of operators I personally have access to.

Additionally, in the Genius ranking, only  **regular operators and regular/combo operators**  are counted towards the operator count. This means only the operators used in your submitted regular alphas will be included in your Genius metrics. Submitting super alphas does NOT affect your Genius operator data.

Therefore, feel free to use a diverse range of operators in your regular alphas to enhance your Genius ranking.

---

### 评论 #8 (作者: NS62681, 时间: 1年前)

Since Genius level controls how many operators you can use 167 for GrandMasters, 134 for Masters and only regular ones affect the Genius score, how do you manage OP/Alpha without sacrificing signal strength or variety?

---

### 评论 #9 (作者: SR82953, 时间: 1年前)

Among the three alpha structures (regular, selection, and combo), only operators used in regular alphas contribute to your operator count for Genius. You can find a detailed table of all operators along with their usage scope under the  **Learn > Operators**  tab on the platform. Also, the maximum number of operators you’re allowed to use is tied to your current Genius level—the higher your level, the more operators you can access.

---

### 评论 #10 (作者: SY65468, 时间: 1年前)

According to prior insights, Grand Master users enjoy full access to all 167 operators, while Master-level users typically have around 134. . These figures may vary slightly, but they offer a general sense of tier-based progression. It’s crucial to note that only  **regular operators**  are counted toward your Genius operator total.  **Combo**  and  **Selection operators** , which play a more specialized role in SuperAlpha construction, are excluded from Genius progression. This distinction is vital when tracking advancement, as it clarifies which operators genuinely influence your Genius metrics.

---

### 评论 #11 (作者: AY28568, 时间: 1年前)

Good question! Knowing how many operators you can use and which ones count for Genius is really helpful. Right now, there isn't one official document that explains everything clearly. Some details are in the Genius FAQs, or you can ask support for help. Usually, only certain types of operators (like math, logic, or time-based ones) are counted for Genius. Others, like constants or simple values, may not be counted. If you use operators that aren’t counted, your op/alpha number probably won’t go up. It would be great if they share a clear list soon to help everyone.

---

### 评论 #12 (作者: AK98027, 时间: 1年前)

Balancing OP/Alpha with strong, diverse signals is definitely a challenge. I try to limit the number of nested and high-complexity operators while focusing on combinations that are both interpretable and effective. Using regular operators creatively helps keep OP/Alpha low without sacrificing performance. It’s also helpful to revisit and simplify alphas periodically as operator access grows with Genius level.

---

### 评论 #13 (作者: TP19085, 时间: 10个月前)

You’ve laid it out well! The Genius platform operator count indeed depends on your tier, with GrandMasters typically having access to a broader set (around 167) compared to Masters (around 134). Checking the official operators page is always a smart move to see your current pool.

The nuance about only regular operators counting toward Genius progress—while combo and selection operators still influence your OP/Alpha metric—is key. This means balancing your alpha complexity is essential: you want to keep OP/Alpha low for leaderboard efficiency but can’t simply avoid combo or selection operators since they’re crucial for building sophisticated Super Alphas.

A solid technique I’ve seen is leveraging multi-purpose operators like  **decay_linear** ,  **rank** , or  **ts_corr** , which pack several effects into a single operator, reducing operator bloat. Layering logic this way keeps your expressions efficient without sacrificing richness or signal diversity.

What’s your go-to strategy for balancing operator usage with maintaining strong, varied signals?

---

### 评论 #14 (作者: TP19085, 时间: 10个月前)

Exactly—you’ve summarized it well. Genius operator count depends on tier: GrandMasters usually access around 167 operators, while Masters have roughly 134, with the official operators page providing the most accurate snapshot.

The key nuance is that only  **regular operators**  count toward Genius progress, while combo and selection operators still influence your  **OP/Alpha**  metric. This makes balancing alpha complexity essential: you want low OP/Alpha for leaderboard efficiency but can’t avoid combo/selection operators, which are crucial for rich, sophisticated Super Alphas.

A practical approach is leveraging  **multi-purpose operators**  like  `decay_linear` ,  `rank` , or  `ts_corr` , which combine multiple effects into a single operator. Layering logic this way keeps expressions efficient while preserving diversity and signal richness.

How do you typically balance operator usage with maintaining both strong performance and signal variety?

---

