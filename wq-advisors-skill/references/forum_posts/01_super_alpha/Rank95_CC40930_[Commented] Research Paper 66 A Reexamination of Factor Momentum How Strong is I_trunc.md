# Research Paper 66: A Reexamination of Factor Momentum: How Strong is It?

- **链接**: https://support.worldquantbrain.com[Commented] Research Paper 66 A Reexamination of Factor Momentum How Strong is It_17611143426327.md
- **作者**: KA64574
- **发布时间/热度**: 2年前, 得票: 6

## 帖子正文

**Abstract:**

Recent studies show that most financial market anomalies exhibit a momentum effect. Based on two datasets, i) an original 22-factor sample and ii) a more comprehensive 187-factor sample, we find that factor momentum effect is weak at the individual factor level. In both samples, only about 22-27% of the factors exhibit strong return continuation and dominate the factor momentum portfolio while the remaining factors do not. The factor momentum strategies do not outperform the corresponding long-only strategies in either sample. The choice of factors affects the ability of factor momentum to explain individual stock momentum.

Author : Minyou Fan, Youwei Li, Ming Liao, Jiadong Liu

Year : 2022

Link :  **[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3844484](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3844484)**

**Key ideas and Comments from WorldQuant:**

- Page 2 paragraph 3
- Page 7 paragraph 2
- Page 14 paragraph 3

**Term**

**Data field**

**Dataset**

Price momentum

oth545_mpd

[**other545**](https://platform.worldquantbrain.com/data/data-sets/other545?delay=1&instrumentType=EQUITY&limit=20&offset=0&region=USA&universe=TOP3000)

Earnings momentum

mdl169_backfill_currentpricelevelannual

[**model169**](https://platform.worldquantbrain.com/data/data-sets/model169/?delay=1&instrumentType=EQUITY&limit=20&offset=0&region=USA&universe=TOP3000)

---

## 讨论与评论 (30)

### 评论 #1 (作者: TN67143, 时间: 2年前)

Hi,

Can we analyze the abstract of this paper in the following ways?

1. In the first sentence of the paper, the author wrote: Recent studies show that most financial market anomalies exhibit a momentum effect.

This can show that, based on the literature review of recent studies and research, it can be found that their exist a momentum effect in the anomal phenomenon occurring in most financial markets.

These anomalies can be seen as contained anomal information that is irregular to observe in the market (market inefficiencies) that may be the material to build Alphas signals (momentum signals).

2. In the second sentence of the paper, the author wrote: Based on two datasets, i) an original 22-factor sample and ii) a more comprehensive 187-factor sample, we find that factor momentum effect is weak at the individual factor level.

Here, to examine the effects of momentum on stock returns, the authors try to look for evidences in two datasets: 
i) A smaller original sample that contains 22 momentum factors
ii) And a more comprehensive sample that contains 187 momentum factors.

Upon data analysis of the two above datasets, they find a weak effect that momentum has on the stock returns, at each invidual factor.

This may suggest that momentum-related factors are weakly positively associated with stocks returns. Therefore, we could either use momentum directly as a predictive signal, or their correlation with stock returns as stock weights allocation.

Here, to find respective datasets that contain momentum information in each region, besides the suggested ones (Price momentum (oth545_mpd)), we might use the search functions: (here, since we are on the MAPC that build Alphas in the GLB regions, we shall look at them briefly as an example, other momentum datafields for other regions can be found by selecting their respective regions near the search bar.)  [https://platform.worldquantbrain.com/data/search/data-fields?delay=1&instrumentType=EQUITY&limit=20&offset=0®ion=GLB&search=momentum&universe=TOP3000](https://platform.worldquantbrain.com/data/search/data-fields?delay=1&instrumentType=EQUITY&limit=20&offset=0%C2%AEion=GLB&search=momentum&universe=TOP3000) .

3. In the third sentence of the abstract, the authors wrote: In both samples, only about 22-27% of the factors exhibit strong return continuation and dominate the factor momentum portfolio while the remaining factors do not.

Here, they show that only about 22-27% of the examined factors show strong effects on the stock returns.

This means that, upon finding the characteristics of these factors, we can find ways to filter the more effective factors and improve our Alphas.

4. In the fourth sentence of the paragraph, the authors wrote: The factor momentum strategies do not outperform the corresponding long-only strategies in either sample.

This shall indicate that the factor momentum strategies (that use a set of momentum factors) produce less efficient returns than the long-only strategies (that only long the stocks, all positive weights stocks allocated, with positive outlook for all stocks).

This shall mean that we somehow need to find the most effective momentum factors to use, and upon finding our weights of the Alphas afterwards, we can use the abs operators to convert the weights into positive and make them long-only portfolio.

5. In the fifth sentence, the authors wrote: The choice of factors affects the ability of factor momentum to explain individual stock momentum.

Here, they further reaffirm the set of more effective momentum factors chosen from the original sets of factors. If we can find some ways to filter these factors, we could possibly improve the performance of our Alphas.

To finalize, momentum factors might have slight positive correlation with the stock returns. We can improve the momentum-based Alphas performance by choosing the strongest factors and convert them into all-long strategies.

This shall be realized briefly by an Alphas formula: abs(momentum),

with momentum representing the respective datafields that contain momentum information.

What do you think about the above process?

Thank you.

---

### 评论 #2 (作者: DK20528, 时间: 1年前)

This paper offers a timely and critical reassessment of factor momentum, a concept that has gained traction in asset pricing and portfolio construction. By revisiting the strength and persistence of factor momentum, the authors contribute to an important dialogue about its robustness and practical significance in financial markets.

**Strengths:**

1. **Critical Reexamination** : The study challenges established assumptions about factor momentum, encouraging a deeper understanding of its mechanisms and limitations.
2. **Quantitative Depth** : The methodology, particularly if it employs advanced econometric models or long-term datasets, likely strengthens the reliability of the findings.
3. **Market Relevance** : Factor momentum is increasingly used in systematic strategies, making this reevaluation highly relevant for both academics and practitioners.

**Potential Areas for Further Development:**

1. **Scope of Factors** : Clarifying which factors (e.g., value, size, quality) are included in the analysis and how their momentum effects vary could provide additional granularity.
2. **Cross-Market Comparison** : Expanding the study to include global markets or emerging economies might highlight whether factor momentum behaves consistently across different regions.
3. **Temporal Dynamics** : Investigating whether the strength of factor momentum changes during different market regimes (e.g., bull vs. bear markets) could add valuable context.
4. **Practical Implications** : Providing actionable insights for portfolio managers, such as risk management strategies when utilizing factor momentum, would enhance the study's applicability.

This research is an important contribution to the ongoing exploration of factor-based investing, offering fresh perspectives on the validity and utility of factor momentum in a rapidly evolving market landscape.

---

### 评论 #3 (作者: XL31477, 时间: 1年前)

[TN67143](/hc/en-us/profiles/14032371578903-TN67143) , your analysis is quite comprehensive and makes a lot of sense. You've done a great job of breaking down the paper's key points. Regarding using the search function to find momentum datafields, that's a useful tip. And your idea about improving Alphas by choosing the strongest factors and converting to long-only strategies is valid. However, DK20528 also makes some good points about areas for further development in the paper. Overall, it's a great discussion and helps us understand factor momentum better. Keep it up!

---

### 评论 #4 (作者: SJ17125, 时间: 1年前)

This paper critically reassesses factor momentum, challenging established views and offering valuable insights into its strength and persistence. By using advanced econometric models and long-term datasets, the study enhances the reliability of its findings. The growing relevance of factor momentum in systematic strategies makes this research timely for both academics and practitioners. Further exploration of specific factors, cross-market comparisons, and temporal dynamics would deepen the analysis. The study provides important perspectives on the practical use and limitations of factor momentum in modern finance.

---

### 评论 #5 (作者: BA51127, 时间: 1年前)

The paper "A Reexamination of Factor Momentum: How Strong is It?" offers a critical look at the effectiveness of factor momentum in asset pricing, especially in light of its recent struggles. It highlights that while momentum strategies have gained traction, their performance may not be as robust as previously thought, particularly when considering different factors. The authors suggest that understanding which factors contribute most effectively to momentum could enhance investment strategies. Additionally, exploring how these factors behave across various market conditions and regions could provide deeper insights into their applicability. Overall, this research is timely and relevant for investors looking to refine their approaches in a changing market landscape.

---

### 评论 #6 (作者: AT56452, 时间: 1年前)

[TN67143](/hc/en-us/profiles/14032371578903-TN67143)  - You broke down the explanation into an expression form astutely. This is the process I usually follow and I think it's correct only. Also, your explanation helped me with the paper. Thanks!

---

### 评论 #7 (作者: XD81759, 时间: 1年前)

Hey, this research paper is quite interesting. It shows factor momentum effect is weak at individual factor level. Just like it says, only around 22-27% of factors have strong return continuation. And the factor momentum strategies don't outperform long-only ones. When we build our own strategies on Brain platform, we should carefully consider these findings, especially when choosing factors. Maybe focus on those with stronger momentum shown in the study.

---

### 评论 #8 (作者: HY45205, 时间: 1年前)

Thank you for taking the time to share your thoughts and insights. It's always valuable to see different perspectives and learn from the experiences of others in the community. Your contribution not only adds depth to the discussion but also inspires others to engage and share their ideas as well. This kind of knowledge exchange is what makes a community thrive and grow stronger. Whether it's an innovative approach, a thoughtful question, or simply an observation, each piece of input helps build a richer understanding for everyone involved. I truly appreciate the effort you’ve put into crafting your post—it’s clear that a lot of thought and expertise went into it. Please keep sharing your ideas and discoveries, as they are incredibly helpful for others who may be exploring similar topics. Once again, thank you for being an active and thoughtful member of the community!

---

### 评论 #9 (作者: AT56452, 时间: 1年前)

Recent studies have examined the prevalence of momentum effects across various financial market anomalies. An analysis utilizing two datasets—one comprising 22 factors and another encompassing 187 factors—reveals that the factor momentum effect is relatively weak at the individual factor level. Specifically, only about 22% to 27% of these factors demonstrate strong return continuation, thereby dominating the factor momentum portfolio, while the majority do not exhibit significant momentum. Furthermore, factor momentum strategies do not outperform corresponding long-only strategies in either dataset. The selection of factors also influences the capacity of factor momentum to explain individual stock momentum.

---

### 评论 #10 (作者: AT56452, 时间: 1年前)

Momentum effects are commonly observed across various financial market anomalies, indicating that assets with superior past performance tend to continue outperforming in the short term. This phenomenon has been documented in numerous studies, highlighting its significance in asset pricing and investment strategies. However, the strength and consistency of these momentum effects can vary depending on the specific factors and time periods analyzed. Understanding the prevalence and characteristics of momentum is crucial for investors seeking to capitalize on these patterns.

---

### 评论 #11 (作者: AT56452, 时间: 1年前)

When examining factor momentum at the individual factor level, research indicates that the effect is relatively weak. In both the 22-factor and 187-factor samples, only a minority of factors exhibit strong return continuation. This suggests that while momentum may be present in aggregate, it is not uniformly distributed across all factors. Investors should exercise caution when implementing momentum-based strategies, as the effectiveness may be limited to specific factors rather than being a universal characteristic.

---

### 评论 #12 (作者: AT56452, 时间: 1年前)

Within factor momentum portfolios, approximately 22% to 27% of factors demonstrate strong return continuation, effectively dominating the portfolio's performance. This concentration implies that a small subset of factors significantly contributes to the overall momentum effect, while the majority have minimal impact. Identifying and focusing on these dominant factors could enhance the effectiveness of momentum-based investment strategies. However, the challenge lies in accurately identifying these factors in advance.

---

### 评论 #13 (作者: AT56452, 时间: 1年前)

Factor momentum strategies have been found to underperform when compared to corresponding long-only strategies. This underperformance raises questions about the practical benefits of implementing factor momentum strategies, especially considering the additional complexity and potential costs involved. Investors may need to reassess the value of incorporating factor momentum into their investment approaches, given that simpler long-only strategies may yield superior returns.

---

### 评论 #14 (作者: AT56452, 时间: 1年前)

The choice of factors significantly affects the ability of factor momentum strategies to explain individual stock momentum. Certain factors may align more closely with stock momentum patterns, enhancing explanatory power, while others may not. This variability underscores the importance of careful factor selection in the development of momentum-based strategies. A nuanced understanding of which factors are most relevant can lead to more effective investment decisions.

---

### 评论 #15 (作者: AT56452, 时间: 1年前)

The findings on factor momentum suggest that investors should exercise caution when developing momentum-based strategies. Given the weak effect at the individual factor level and the underperformance relative to long-only strategies, reliance solely on factor momentum may not yield the desired outcomes. A more comprehensive approach that considers multiple factors and market conditions may be necessary to achieve optimal results.

---

### 评论 #16 (作者: AT56452, 时间: 1年前)

Market conditions play a crucial role in the effectiveness of momentum strategies. The performance of these strategies can vary significantly across different market environments, such as bull or bear markets. Investors should be aware of the current market context and adjust their strategies accordingly to mitigate potential risks associated with momentum investing.

---

### 评论 #17 (作者: AT56452, 时间: 1年前)

Implementing momentum strategies requires careful risk management, especially considering the potential for significant drawdowns during market reversals. Investors should employ risk mitigation techniques, such as diversification and stop-loss mechanisms, to protect against adverse market movements that can negatively impact momentum-based portfolios.

---

### 评论 #18 (作者: AT56452, 时间: 1年前)

The strength and prevalence of momentum effects can evolve over time due to changes in market dynamics, investor behavior, and economic conditions. Continuous monitoring and analysis are essential to understand current momentum patterns and adjust investment strategies accordingly. Staying informed about recent developments can help investors capitalize on emerging opportunities and avoid potential pitfalls associated with outdated momentum assumptions.

---

### 评论 #19 (作者: AT56452, 时间: 1年前)

Combining momentum with other investment factors, such as value or quality, may enhance portfolio performance. Multi-factor strategies can provide diversification benefits and improve risk-adjusted returns by capturing different dimensions of asset pricing anomalies. Investors should consider integrating momentum with complementary factors to develop more robust investment strategies that can withstand various market conditions.

---

### 评论 #20 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

**Thank you for sharing this insightful paper!**

The finding that only 22-27% of factors exhibit strong return continuation is surprising. It raises questions about the selection process for factors in momentum strategies. Would focusing on more robust factors or incorporating additional filters improve the performance of factor momentum portfolios?

---

### 评论 #21 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

Moreover, the comparison between factor momentum and long-only strategies is thought-provoking.

The underperformance of factor momentum strategies suggests potential limitations in their design. Exploring hybrid approaches that combine factor momentum with other strategies might offer better results. Has anyone tested such combinations in their Alpha development?

---

### 评论 #22 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

The paper highlights how the composition of factor portfolios affects their explanatory power. It would be intriguing to analyze whether certain sectors or regions show stronger momentum effects at the individual stock level. This could help refine the application of factor momentum strategies.

---

### 评论 #23 (作者: 顾问 CC40930 (Rank 95), 时间: 1年前)

This paper explores the momentum effect in financial market anomalies, specifically focusing on factor momentum. Using two datasets—one with 22 factors and another with 187 factors—the study finds that the factor momentum effect is weak at the individual factor level. Only a small portion (22-27%) of factors show strong return continuation and drive the momentum portfolio's performance, while the remaining factors do not contribute significantly. Additionally, factor momentum strategies do not outperform long-only strategies in either dataset, and the choice of factors influences the ability of factor momentum to explain individual stock momentum.

---

### 评论 #24 (作者: VP21767, 时间: 1年前)

This paper reexamines factor momentum effects across 22-factor and 187-factor samples. It finds that only 22-27% of factors exhibit strong momentum and dominate portfolios, while most factors show weak effects. Factor momentum strategies fail to outperform simple long-only strategies in either sample, highlighting the critical role of factor selection in driving stock momentum. The study suggests that factor momentum is highly dependent on specific factors, limiting its effectiveness in broader applications.

---

### 评论 #25 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

The paper's finding that factor momentum is weak at the individual factor level but still present in a small subset is intriguing. This suggests that selecting the right factors is critical for effective momentum strategies. Has anyone tried combining  `oth545_mpd`  with other datasets to enhance signal strength?

---

### 评论 #26 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

The observation that factor momentum strategies do not outperform long-only strategies is surprising. It highlights the importance of thoroughly testing factor combinations. Incorporating  `mdl169_backfill_currentpricelevelannual`  for earnings momentum could add another layer of insight. Any suggestions on how to pair earnings momentum with price momentum effectively?

---

### 评论 #27 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

This study provides valuable insights into the limitations of factor momentum. It would be interesting to explore whether combining weak factors in a diversified portfolio might still yield significant results. How has the community approached similar challenges in other datasets?

---

### 评论 #28 (作者: 顾问 HD25387 (Rank 65), 时间: 1年前)

The choice of factors appears to play a crucial role in the success of momentum strategies. For those working on this, do you think the weakness in factor momentum at the individual level could be mitigated by using more advanced neutralization techniques or by focusing on specific regions?

---

### 评论 #29 (作者: AK98027, 时间: 1年前)

This paper investigates the "factor momentum" effect, where past performance of investment factors predicts future factor performance.

Analyzing a large set of factors, the study finds that:

- **Weak Individual Factor Momentum:**  Most individual factors do not exhibit strong momentum.
- **Performance Driven by Few Factors:**  Only a small subset of factors (22-27%) significantly contribute to the overall factor momentum effect.
- **Limited Outperformance:**  Factor momentum strategies generally do not outperform simple long-only strategies.
- **Factor Selection Matters:**  The specific factors included in the portfolio significantly impact the ability of factor momentum to explain stock momentum.

These findings suggest that the factor momentum effect may be driven by a limited number of factors and its practical significance for investment strategies may be limited.

---

### 评论 #30 (作者: KS69567, 时间: 1年前)

This study re-examines factor momentum, challenging accepted wisdom and offering new insights into its robustness and durability. By utilising sophisticated econometric methods and large historical datasets, the study provides solid and trustworthy results. This work is especially pertinent for both scholarly research and real-world applications as factor momentum becomes more and more important in systematic investing methods. Opportunities for more research into particular components, cross-market behaviours, and the evolution of momentum effects across time are also highlighted in the report. These insights contribute to a nuanced understanding of the applicability and boundaries of factor momentum in contemporary financial practice.

---

