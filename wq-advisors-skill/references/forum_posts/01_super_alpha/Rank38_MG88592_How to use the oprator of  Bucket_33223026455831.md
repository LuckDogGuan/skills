# How to use the oprator of  “Bucket”？

- **链接**: https://support.worldquantbrain.comHow to use the oprator of  Bucket_33223026455831.md
- **作者**: 顾问 MG88592 (Rank 38)
- **发布时间/热度**: 1年前, 得票: 91

## 帖子正文

### **DEF：bucket(rank(x), range="0, 1, 0.1" or buckets = "2,5,6,7,10")

1.  `rank(x)`  Function**

- **Purpose** : Performs cross-sectional ranking on the variable  `x` , returning the rank of each stock at a given time point (normalized to  `[0,1]`  or  `[1,N]` ).
- **Example** :
  ```
  rank(close)  # Ranks stocks based on closing price
  ```
  - By default,  `rank()`  returns a percentile rank in the range  `[0,1]`  (where 0 is the minimum and 1 is the maximum).

### **2.  `bucket(rank(x), range="...")`  Function**

- **Purpose** : Divides the result of  `rank(x)`  into  **quantile buckets**  for group analysis (e.g., deciles, quintiles).
- **Parameters** :
  - `range="0,1,0.1"`  → Divides the range from 0 to 1 into steps of 0.1 (i.e., 10 equal buckets).
  - `buckets="2,5,6,7,10"`  → Custom bucket boundaries (e.g., 2%, 5%, 6%, 7%, 10% percentiles).
- **Examples** :
  ```
  bucket(rank(close), range="0,1,0.1")  # Splits into 10 equal groups
  bucket(rank(pe_ratio), buckets="0.2,0.5,0.8")  # Splits into 4 groups (<20%, 20-50%, 50-80%, >80%)
  ```

### **3. Practical Applications in WorldQuant Brain**

#### **Example 1: Splitting Market Cap into 5 Groups**

```
# Computes market cap ranking and splits into 5 equal buckets  
bucket(rank(market_cap), range="0,1,0.2")  
```

- **Output** : Each stock is assigned a value between 0-0.2, 0.2-0.4, ..., 0.8-1, representing its quantile group.

#### **Example 2: Custom Grouping (e.g., Extreme Values Separately)**

```
# Splits PE ratio into low, medium, and high groups  
bucket(rank(pe_ratio), buckets="0.3,0.7")  
```

- **Grouping Logic** :
  - `pe_ratio`  rank <30% → Low PE group
  - 30% ≤  `pe_ratio`  rank <70% → Medium PE group
  - `pe_ratio`  rank ≥70% → High PE group

### **4. Common Use Cases**

- **Factor Stratified Backtesting** : Divides stocks into groups based on a factor (e.g., momentum, valuation) to analyze performance.
- **Outlier Handling** : Uses  `bucket()`  to identify extreme values (e.g., top/bottom 10% of stocks).
- **Portfolio Construction** : Selects stocks in specific quantiles (e.g., top 20% low-volatility stocks).

### **5. Key Notes**

- **`rank()`  is cross-sectional by default**  (ranks all stocks daily).
- **`bucket()`  uses left-inclusive, right-exclusive boundaries**  (e.g.,  `[0,0.2)`  includes 0 but excludes 0.2).
- **WorldQuant Brain may support different parameter formats** —check platform docs or use  `help(bucket)`  for syntax.

---

## 讨论与评论 (6)

### 评论 #1 (作者: JO96892, 时间: 1年前)

This was veery helpful a lot.

---

### 评论 #2 (作者: 顾问 NP52721 (Rank 88), 时间: 1年前)

> that's very clearly explain

---

### 评论 #3 (作者: AY28568, 时间: 1年前)

The  `bucket()`  function groups ranked data into quantiles or custom ranges for better analysis and portfolio grouping is Very useful.

---

### 评论 #4 (作者: DH50715, 时间: 1年前)

This could really help.

---

### 评论 #5 (作者: NT84064, 时间: 10个月前)

The  `bucket()`  operator is very useful when you need to discretize a continuous factor into quantile-based groups for stratified analysis or targeted selection. Since  `rank()`  normalizes values to [0,1], applying  `bucket(rank(x), range="start,end,step")`  allows you to split the factor into evenly spaced bins, while  `buckets="p1,p2,...,pn"`  lets you define custom percentile cutoffs for more nuanced grouping. This is especially helpful for building long-short strategies based on extremes (e.g., top decile vs. bottom decile) or for isolating middle groups to test factor monotonicity. You can also combine  `bucket()`  with conditional logic to run group-specific transformations — for instance, applying a momentum calculation only to low-volatility buckets. Just be mindful of how boundaries are treated (left-inclusive, right-exclusive) and verify that your universe size supports the granularity you choose, as very small buckets may cause instability in thin universes.

---

### 评论 #6 (作者: LB76673, 时间: 9个月前)

This post is very helpful for anyone who wants to apply  `bucket()`  correctly for factor testing and alpha design.

---

