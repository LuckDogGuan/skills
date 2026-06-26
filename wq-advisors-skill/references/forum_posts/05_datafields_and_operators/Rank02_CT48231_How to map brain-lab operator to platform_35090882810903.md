# How to map brain-lab operator to platform

- **链接**: https://support.worldquantbrain.comHow to map brain-lab operator to platform_35090882810903.md
- **作者**: 顾问 CT48231 (Rank 2)
- **发布时间/热度**: 9个月前, 得票: 7

## 帖子正文

Hi there, anyone can tell me how to use operator in brain lab to create alpha in platform? Thank you

---

## 讨论与评论 (7)

### 评论 #1 (作者: YZ51589, 时间: 9个月前)

Can we create Alpha in brain lab? I thought is a platform to analysis data field. More for data analysis and feature engineering rather than create alpha expression

Also brain lab is very slow, a little bit complex process could cause long time freezing.

Anyway I don't know whether you could, but even it allow I wouldn't use that .

Good luck to us

---

### 评论 #2 (作者: AG14039, 时间: 9个月前)

Brain Lab is mainly designed for data exploration, field analysis, and feature engineering rather than direct alpha expression building. While you could technically piece together some logic there, it’s not the intended use—it’s more of a research sandbox than an alpha creation environment. On top of that, as you mentioned, the platform can be slow and even freeze when handling complex operations, which makes it inefficient for alpha development. So even if it’s possible, it’s generally better to stick to BRAIN proper for alpha expressions and use Brain Lab only as a supporting tool for data insights.

---

### 评论 #3 (作者: LB76673, 时间: 9个月前)

In Brain Lab, operators are the building blocks of alphas. You combine datasets (like price, volume, fundamentals) with operators (such as  `rank` ,  `zscore` ,  `decay_linear` ,  `ts_mean` ) to transform raw fields into predictive signals. For example,  `rank(ts_mean(close,10))`  builds a short-term momentum alpha. Start by picking a dataset field, apply a time-series operator to capture dynamics, then normalize with rank or zscore. The goal is to test small, simple expressions first, then refine by adding neutralization or decay for stability.

---

### 评论 #4 (作者: AS13853, 时间: 9个月前)

This is from my side ,Brain Lab is mainly a data exploration and feature engineering tool. Operators in Brain Lab (like  `rank` ,  `zscore` ,  `ts_mean` ,  `decay_linear` ) let you transform raw datasets—price, volume, or fundamentals—into usable signals. While you can experiment with combinations in Brain Lab to understand how a field behaves, the actual alpha creation is better done in the main platform (BRAIN)

---

### 评论 #5 (作者: SR82953, 时间: 9个月前)

Brain lab is primarily for visualizing datafields values and compare among them. You can not work with operators in brain lab to create alphas. For that purpose consultant can use ACE API. You can find it here, Learn/Documentation/BRAIN API.

---

### 评论 #6 (作者: AG14039, 时间: 8个月前)

Exactly — Brain Lab is best thought of as a sandbox for exploration. You can use operators like  `rank` ,  `zscore` ,  `ts_mean` , or  `decay_linear`  to experiment with raw datasets and see how transformations behave. It’s great for feature engineering and testing ideas quickly, but the final alpha construction, scaling, neutralization, and portfolio integration should be done in the main BRAIN platform for proper production-level validation.

---

### 评论 #7 (作者: AG14039, 时间: 8个月前)

Exactly — Brain Lab is mainly a visualization and exploration tool. It lets you inspect and compare data field values, but it doesn’t support building alphas with operators. For alpha creation, consultants should use the ACE API, which provides full functionality for applying operators, transformations, and building production-ready signals. Documentation is available under Learn → Documentation → BRAIN API.

---

