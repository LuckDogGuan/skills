# 顾问 MG88592 (Rank 38) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 MG88592 (Rank 38) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: CombineHow to use “group_cartesian_product(g1, g2)” to create a alpha?
- **主帖链接**: CombineHow to use group_cartesian_productg1 g2 to create a alpha.md
- **讨论数**: 8

Thegroup_cartesian_product(g1, g2)operator in WorldQuant's Alpha Research Platform performs a Cartesian product operation between two groups of factors (g1 and g2).Here are some commonly usedgroupfields in WorldQuantBraincountry,industry,subindustry,sector,market....Functionality:It creates all possible combinations between the factors in group g1 and the factors in group g2For each combination, it generates a new factor that represents the interaction between the two original factorsThis is useful for exploring potential interactions between different sets of factors# Example usage:g1 = [factor1, factor2]  # First group of factorsg2 = [factor3, factor4]  # Second group of factorsresult = group_cartesian_product(g1, g2)  # Will produce factor1*factor3, factor1*factor4, factor2*factor3, factor2*factor4When to use:When you want to systematically test interactions between two distinct sets of factorsFor exhaustive combination testing between different factor categoriesTo explore potential multiplicative relationships between factors

---

### 帖子 #2: CombineHow to use “group_cartesian_product(g1, g2)” to create a alpha?
- **主帖链接**: https://support.worldquantbrain.comCombineHow to use group_cartesian_productg1 g2 to create a alpha_33370333775767.md
- **讨论数**: 8

The  `group_cartesian_product(g1, g2)`  operator in WorldQuant's Alpha Research Platform performs a Cartesian product operation between two groups of factors (g1 and g2).

Here are some commonly used  `group`  fields in WorldQuantBrain

country,industry,subindustry,sector,market....

**Functionality:**

- It creates all possible combinations between the factors in group g1 and the factors in group g2
- For each combination, it generates a new factor that represents the interaction between the two original factors
- This is useful for exploring potential interactions between different sets of factors

**# Example usage:
g1 = [factor1, factor2]  # First group of factors
g2 = [factor3, factor4]  # Second group of factors
result = group_cartesian_product(g1, g2)  # Will produce factor1*factor3, factor1*factor4, factor2*factor3, factor2*factor4**

**When to use:**

- When you want to systematically test interactions between two distinct sets of factors
- For exhaustive combination testing between different factor categories
- To explore potential multiplicative relationships between factors

---

### 帖子 #3: How to Use the `normalize` Operator for Data Standardization
- **主帖链接**: How to Use the normalize Operator for Data Standardization.md
- **讨论数**: 3

Hi everyone! Today I want to share a very practical operator called `normalize` that helps standardize data for quantitative analysis. Standardization is a common preprocessing step, and here's a detailed guide on how to use it.Basic FunctionalityThe `normalize(x, useStd = false, limit = 0.0)` operator performs the following operations:1. Calculates the mean of all valid alpha values for a given date2. Subtracts this mean from each elementParameter Explanation- `useStd` (default false):- When true, calculates the standard deviation and scales the results by it- `limit` (default 0.0):- When not 0.0, clips the results to the range [-limit, +limit]Usage ExamplesFor a given date with input values x = [3,5,6,2], we calculate:- Mean = 4- Standard deviation ≈ 1.82Example 1:Mean normalization only```normalize(x, useStd = false, limit = 0.0)= [3-4, 5-4, 6-4, 2-4]= [-1, 1, 2, -2]```Example 2: Z-score standardization with std deviation```normalize(x, useStd = true, limit = 0.0)= [-1/1.82, 1/1.82, 2/1.82, -2/1.82]≈ [-0.55, 0.55, 1.1, -1.1]```Example 3: With value limitingIf we set limit=1.0:```normalize(x, useStd = true, limit = 1.0)= Clips [-0.55, 0.55, 1.1, -1.1] to [-1,1] range= [-0.55, 0.55, 1.0, -1.0]```Practical ApplicationsThis operator is particularly useful for:1. Comparing data with different scales2. Preprocessing inputs for machine learning models3. Removing bias from datasetsHope you find this explanation helpful! Feel free to discuss any questions in the comments.

---

### 帖子 #4: How to Use the `normalize` Operator for Data Standardization
- **主帖链接**: https://support.worldquantbrain.comHow to Use the normalize Operator for Data Standardization_32981699966103.md
- **讨论数**: 3

Hi everyone! Today I want to share a very practical operator called `normalize` that helps standardize data for quantitative analysis. Standardization is a common preprocessing step, and here's a detailed guide on how to use it.

**Basic Functionality**

The `normalize(x, useStd = false, limit = 0.0)` operator performs the following operations:

1. Calculates the mean of all valid alpha values for a given date
2. Subtracts this mean from each element

**Parameter Explanation**

- `useStd` (default false): 
  - When true, calculates the standard deviation and scales the results by it
- `limit` (default 0.0):
  - When not 0.0, clips the results to the range [-limit, +limit]

**Usage Examples**

For a given date with input values x = [3,5,6,2], we calculate:
- Mean = 4
- Standard deviation ≈ 1.82

Example 1:  **Mean normalization only** 
```
normalize(x, useStd = false, limit = 0.0) 
= [3-4, 5-4, 6-4, 2-4] 
= [-1, 1, 2, -2]
```

**Example 2: Z-score standardization with std deviation** 
```
normalize(x, useStd = true, limit = 0.0) 
= [-1/1.82, 1/1.82, 2/1.82, -2/1.82] 
≈ [-0.55, 0.55, 1.1, -1.1]
```

**Example 3: With value limiting** 
If we set limit=1.0:
```
normalize(x, useStd = true, limit = 1.0)
= Clips [-0.55, 0.55, 1.1, -1.1] to [-1,1] range
= [-0.55, 0.55, 1.0, -1.0]
```

Practical Applications

This operator is particularly useful for:
1. Comparing data with different scales
2. Preprocessing inputs for machine learning models
3. Removing bias from datasets

Hope you find this explanation helpful! Feel free to discuss any questions in the comments.

---

### 帖子 #5: How to use the oprator of  “Bucket”？
- **主帖链接**: How to use the oprator of  Bucket.md
- **讨论数**: 6

DEF：bucket(rank(x), range="0, 1, 0.1" or buckets = "2,5,6,7,10")1.rank(x)FunctionPurpose: Performs cross-sectional ranking on the variablex, returning the rank of each stock at a given time point (normalized to[0,1]or[1,N]).Example:rank(close)# Ranks stocks based on closing priceBy default,rank()returns a percentile rank in the range[0,1](where 0 is the minimum and 1 is the maximum).2.bucket(rank(x), range="...")FunctionPurpose: Divides the result ofrank(x)intoquantile bucketsfor group analysis (e.g., deciles, quintiles).Parameters:range="0,1,0.1"→ Divides the range from 0 to 1 into steps of 0.1 (i.e., 10 equal buckets).buckets="2,5,6,7,10"→ Custom bucket boundaries (e.g., 2%, 5%, 6%, 7%, 10% percentiles).Examples:bucket(rank(close),range="0,1,0.1")# Splits into 10 equal groupsbucket(rank(pe_ratio),buckets="0.2,0.5,0.8")# Splits into 4 groups (<20%, 20-50%, 50-80%, >80%)3. Practical Applications in WorldQuant BrainExample 1: Splitting Market Cap into 5 Groups# Computes market cap ranking and splits into 5 equal bucketsbucket(rank(market_cap),range="0,1,0.2")Output: Each stock is assigned a value between 0-0.2, 0.2-0.4, ..., 0.8-1, representing its quantile group.Example 2: Custom Grouping (e.g., Extreme Values Separately)# Splits PE ratio into low, medium, and high groupsbucket(rank(pe_ratio),buckets="0.3,0.7")Grouping Logic:pe_ratiorank <30% → Low PE group30% ≤pe_ratiorank <70% → Medium PE grouppe_ratiorank ≥70% → High PE group4. Common Use CasesFactor Stratified Backtesting: Divides stocks into groups based on a factor (e.g., momentum, valuation) to analyze performance.Outlier Handling: Usesbucket()to identify extreme values (e.g., top/bottom 10% of stocks).Portfolio Construction: Selects stocks in specific quantiles (e.g., top 20% low-volatility stocks).5. Key Notesrank()is cross-sectional by default(ranks all stocks daily).bucket()uses left-inclusive, right-exclusive boundaries(e.g.,[0,0.2)includes 0 but excludes 0.2).WorldQuant Brain may support different parameter formats—check platform docs or usehelp(bucket)for syntax.

---

### 帖子 #6: Splits PE ratio into low, medium, and high groups
- **主帖链接**: https://support.worldquantbrain.comHow to use the oprator of  Bucket_33223026455831.md
- **讨论数**: 6

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

### 帖子 #7: SA日入50刀，如何把握好SuperAlphaCompetition经验分享
- **主帖链接**: SA日入50刀如何把握好SuperAlphaCompetition经验分享.md
- **讨论数**: 23

大家好，我是顾问 顾问 MG88592 (Rank 38) (Rank 38)，目前Genius等级为Gold，Value Factor（VF）为0.95，分组G4。今天想和大家分享一下最近SuperAlpha比赛的Base Payment情况，并总结一些实用经验。

**收益表现** 
得益于SAC策略，近四天的SuperAlpha Base日均收益达到50美元，相比之前提升了两到三倍！研究小组已经公开了SuperAlpha的收益公式，这里结合我的实际数据验证一下：

**关键发现**

1. **Value Factor决定上限** ：VF 0.99或1.0的选手，提交Fitness>5且Prod Corr<0.5的sa时，基本能拿到顶格Base。
2. **我的收益天花板** ：由于VF仅0.95，我的单日Base上限约为50美元。
   [图片 (图片已丢失)]  [图片 (图片已丢失)]
   **数据实证**
   以下是近期的具体指标（Prod Corr均<0.5）：
   - Fitness 8.48 | PC 0.49 → Base 46.76
   - Fitness 7.92 | PC 0.49 → Base 50.99
   - Fitness 5.46 | PC 0.49 → Base 47.15
   - Fitness 6.80 | PC 0.47 → Base 50.15
   今天提交的pc有点拉垮，可以预见base打对折。
   **核心结论**
   - **PC的优先级高于Fitness** ：当Fitness>5后，进一步升高对Base影响极小，而降低PC能显著提升收益（例如PC从0.49降至0.47时Base增加）。
   - **策略建议** ：不必盲目追求高Fitness或加分，优先控制PC<0.5才是收益最大化的关键。
   希望对大家有所启发，欢迎交流优化思路！
   **希望您顺手点个小赞，祝您base多多！**
   更新昨日sa pc0.6+。base仅有15刀

---

### 帖子 #8: SA日入50刀，如何把握好SuperAlphaCompetition经验分享
- **主帖链接**: https://support.worldquantbrain.comSA日入50刀如何把握好SuperAlphaCompetition经验分享_32630124449559.md
- **讨论数**: 23

大家好，我是顾问 顾问 MG88592 (Rank 38) (Rank 38)，目前Genius等级为Gold，Value Factor（VF）为0.95，分组G4。今天想和大家分享一下最近SuperAlpha比赛的Base Payment情况，并总结一些实用经验。

**收益表现** 
得益于SAC策略，近四天的SuperAlpha Base日均收益达到50美元，相比之前提升了两到三倍！研究小组已经公开了SuperAlpha的收益公式，这里结合我的实际数据验证一下：

**关键发现**

1. **Value Factor决定上限** ：VF 0.99或1.0的选手，提交Fitness>5且Prod Corr<0.5的sa时，基本能拿到顶格Base。
2. **我的收益天花板** ：由于VF仅0.95，我的单日Base上限约为50美元。
   
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 75
> 06/03/2025
> Super:
> 47.15
> 50
> Regular:
> 7.80
> Total:
> 54.949999999999996
> 25
> 31. May
> Jun
> 2.Jun
> 3.Jun
> Jun
> 5.jun
  
> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
>  Status
> Created (EST)
> Region
> Universe
> Delay
> Submission Date
> Self-
> Prod-
> (EST)
> Correlation
> Correlation
> SearCh
> Super Alpha
> Selec
> Selec
> SearCh
> Selec
> Selec
> Selec
> Selec
> Search
> e.吕>1
> e.吕>1
> 0.63
> Super
> ACTIVE
> 06/06/2025 EDT
> ASl
> MINVOLIM
> 06/06/2025 EDT
> 0.32
> 0.63
> Super
> ACTIVE
> 6/05/2025 EDT
> USA
> T0P3000
> 6/05/2025 EDT
> 0.1 /
> 0.41
> 0.48
> Super
> ACTIVE
> 6/04/2025 EDT
> EUR
> TOP2500
> 6/04/2025 EDT
> 0.49
> 0.49
> 0.5002
> Super
> ACTIVE
> 06/03/2025 EDT
> EUR
> TOP2500
> 06/03/2025 EDT
> 0.36
> 0.49
> 0.48
> Super
> ACTIVE
> 06/02/2025 EDT
> EUR
> TOP2500
> 06/02/2025 EDT 
> 0.35
> 0.49
> Date
> Tag

   **数据实证**
   以下是近期的具体指标（Prod Corr均<0.5）：
   - Fitness 8.48 | PC 0.49 → Base 46.76
   - Fitness 7.92 | PC 0.49 → Base 50.99
   - Fitness 5.46 | PC 0.49 → Base 47.15
   - Fitness 6.80 | PC 0.47 → Base 50.15
   今天提交的pc有点拉垮，可以预见base打对折。
   **核心结论**
   - **PC的优先级高于Fitness** ：当Fitness>5后，进一步升高对Base影响极小，而降低PC能显著提升收益（例如PC从0.49降至0.47时Base增加）。
   - **策略建议** ：不必盲目追求高Fitness或加分，优先控制PC<0.5才是收益最大化的关键。
   希望对大家有所启发，欢迎交流优化思路！
   **希望您顺手点个小赞，祝您base多多！**
   更新昨日sa pc0.6+。base仅有15刀

---

### 帖子 #9: ValueFactor更新，本次国区0.9+人数翻倍了！看看谁涨的最快！经验分享
- **主帖链接**: ValueFactor更新本次国区09人数翻倍了看看谁涨的最快经验分享.md
- **讨论数**: 4

昨日Base出现了很多一柱擎天的大佬，今天抽空分析了一下两期vf的变化值，统计如下：


> [!NOTE] [图片 OCR 识别内容]
> CN Consultant Distribution of ValueFactor Pre-update Version
> Total >=0.9:37 USerS
> 1400
> 1359
> (including
> With Vf=l.01
> 1200
> 1000
> 兽
> 800
> 5
> 
> 400
> 200
> ValueFactor Range
> 0.1-0.2
> 0.2-0.3
> 0.7-0.8
> 0.0-0.1
> 9-1.0
> 0.3-0.
> 0.4-0.
> 0.5-0.
> 0.6-0.
> @



> [!NOTE] [图片 OCR 识别内容]
> CN Consultant Distribution of ValueFactor Post-update version
> Total > =0.9:74 Users
> 1222
> (including
> With Vf=l.01
> 1200
> I000
> 800
> 兽
> 5
> 500
> 
> 400
> 200
> ValueFactor Range
> 0.1-0.2
> 0.6-0.7
> 0.7-0.8
> 9-1.0
> 0.0-0.1
> 0.2-0.
> 0.3-0.
> 0.4-0.
> 0.5-0.
> @
 

 
> [!NOTE] [图片 OCR 识别内容]
> ValueFactor Distribution Comparison
> (Original Vs Updated Data)
> Growth Rate by Segment
> %1
> 137
> 1400
> Original (N=1754)
> +100.0%
> 100%
> Updated (N=17751
> 1200
> 80%
> I000
> 50%
> +54.39
> +52.6%
> 鸶
> 800
> 鼍
> +50.0%
> +47.4%
> 
> 500
> 
> 40%
> +33.3%
> +31.6%
> 20%
> 400
> +14.5%
> +12.5%
> 200
> +25
> +35
> +12
> +13
> +20
> +16
> +18
> -10.1%
> 30
> ValueFactor Range
> ValueFactor Range
> 0.6-0.7
> 0.6-0.7
> 0.0-0.1
> 0.1-0.2
> .4-0.5
> 0.5-0.6
> 0.7-0.8
> .9-1.0
> 0.0-0.1
> 0.1-0.2
> 0.4-0.5
> 0.5-0.6
> 0.7-0.8
> .9-1.0
> 0.2-0.
> 0.2-0.
> 0.3-0.
> 0.8-0.
> 0.8-0.


国区vf0.9➕人数实现了翻倍，由37人增长至74人。

此外恭喜以下30位顾问，vf取得巨大提升！

尤其是第一名vf整整提升了0.91！！！恐怖如斯

 
> [!NOTE] [图片 OCR 识别内容]
> 提升最太的30个用户:
> USeI
> ValUeFactor
> 014
> ValUeFactor
> DEI
> Change
> XY56645
> 0.010
> 0.920
> 0.910
> ZZ88928
> 0.130
> 0.930
> 0.800
> JX14975
> 0.020
> 0.810
> 0.790
> C151884
> 0.100
> 0.850
> 0.750
> 'C99622
> 030
> 0.770
> 0.740
> 040395
> 0.090
> 0.820
> 0.730
> SII66069
> 0.020
> 0.740
> 0.720
> FC40923
> 0.120
> 0.800
> 680
> ZL34763
> 0.100
> 0.750
> 0.650
> F667373
> 0.030
> 680
> 659
> 124469
> 0.180
> 800
> 620
> TL42173
> 060
> 670
> 0.610
> K257392
> 0.240
> 840
> 0.600
> I31730
> 030
> 630
> 0.600
> 1551256
> 0.340
> 910
> 0.570
> 2V96737
> 0.430
> 0.990
> 0.560
> 川N78881
> 150
> 700
> 0.550
> Y815978
> 0.450
> 990
> 0.540
> TX98685
> 060
> 600
> 0.540
> JT77454
> 0.070
> 580
> 0.510
> H93328
> 0.500
> 000
> 0.500
> YY91783
> 0.370
> 0.870
> 0.500
> 5224058
> 0.500
> 990
> 0.490
> 1H45966
> 0.500
> 990
> 0.490
> KT24822
> 0.500
> 980
> 480
> ZN43612
> 0.250
> 0.730
> 480
> 11Y56787
> 0.160
> 640
> 480
> 5T25014
> 0.020
> 0.500
> 0.480
> LN26328
> 0.310
> 0.780
> 0.470
> 丫C66172
> 0.500
> 0.970
> 0.470


---

### 帖子 #10: ValueFactor更新，本次国区0.9+人数翻倍了！看看谁涨的最快！经验分享
- **主帖链接**: https://support.worldquantbrain.comValueFactor更新本次国区09人数翻倍了看看谁涨的最快经验分享_33588380916503.md
- **讨论数**: 4

昨日Base出现了很多一柱擎天的大佬，今天抽空分析了一下两期vf的变化值，统计如下：


> [!NOTE] [图片 OCR 识别内容]
> CN Consultant Distribution of ValueFactor Pre-update Version
> Total >=0.9:37 USerS
> 1400
> 1359
> (including
> With Vf=l.01
> 1200
> 1000
> 兽
> 800
> 5
> 
> 400
> 200
> ValueFactor Range
> 0.1-0.2
> 0.2-0.3
> 0.7-0.8
> 0.0-0.1
> 9-1.0
> 0.3-0.
> 0.4-0.
> 0.5-0.
> 0.6-0.
> @



> [!NOTE] [图片 OCR 识别内容]
> CN Consultant Distribution of ValueFactor Post-update version
> Total > =0.9:74 Users
> 1222
> (including
> With Vf=l.01
> 1200
> I000
> 800
> 兽
> 5
> 500
> 
> 400
> 200
> ValueFactor Range
> 0.1-0.2
> 0.6-0.7
> 0.7-0.8
> 9-1.0
> 0.0-0.1
> 0.2-0.
> 0.3-0.
> 0.4-0.
> 0.5-0.
> @
 

 
> [!NOTE] [图片 OCR 识别内容]
> ValueFactor Distribution Comparison
> (Original Vs Updated Data)
> Growth Rate by Segment
> %1
> 137
> 1400
> Original (N=1754)
> +100.0%
> 100%
> Updated (N=17751
> 1200
> 80%
> I000
> 50%
> +54.39
> +52.6%
> 鸶
> 800
> 鼍
> +50.0%
> +47.4%
> 
> 500
> 
> 40%
> +33.3%
> +31.6%
> 20%
> 400
> +14.5%
> +12.5%
> 200
> +25
> +35
> +12
> +13
> +20
> +16
> +18
> -10.1%
> 30
> ValueFactor Range
> ValueFactor Range
> 0.6-0.7
> 0.6-0.7
> 0.0-0.1
> 0.1-0.2
> .4-0.5
> 0.5-0.6
> 0.7-0.8
> .9-1.0
> 0.0-0.1
> 0.1-0.2
> 0.4-0.5
> 0.5-0.6
> 0.7-0.8
> .9-1.0
> 0.2-0.
> 0.2-0.
> 0.3-0.
> 0.8-0.
> 0.8-0.


国区vf0.9➕人数实现了翻倍，由37人增长至74人。

此外恭喜以下30位顾问，vf取得巨大提升！

尤其是第一名vf整整提升了0.91！！！恐怖如斯

 
> [!NOTE] [图片 OCR 识别内容]
> 提升最太的30个用户:
> USeI
> ValUeFactor
> 014
> ValUeFactor
> DEI
> Change
> XY56645
> 0.010
> 0.920
> 0.910
> ZZ88928
> 0.130
> 0.930
> 0.800
> JX14975
> 0.020
> 0.810
> 0.790
> C151884
> 0.100
> 0.850
> 0.750
> 'C99622
> 030
> 0.770
> 0.740
> 040395
> 0.090
> 0.820
> 0.730
> SII66069
> 0.020
> 0.740
> 0.720
> FC40923
> 0.120
> 0.800
> 680
> ZL34763
> 0.100
> 0.750
> 0.650
> F667373
> 0.030
> 680
> 659
> 124469
> 0.180
> 800
> 620
> TL42173
> 060
> 670
> 0.610
> K257392
> 0.240
> 840
> 0.600
> I31730
> 030
> 630
> 0.600
> 1551256
> 0.340
> 910
> 0.570
> 2V96737
> 0.430
> 0.990
> 0.560
> 川N78881
> 150
> 700
> 0.550
> Y815978
> 0.450
> 990
> 0.540
> TX98685
> 060
> 600
> 0.540
> JT77454
> 0.070
> 580
> 0.510
> H93328
> 0.500
> 000
> 0.500
> YY91783
> 0.370
> 0.870
> 0.500
> 5224058
> 0.500
> 990
> 0.490
> 1H45966
> 0.500
> 990
> 0.490
> KT24822
> 0.500
> 980
> 480
> ZN43612
> 0.250
> 0.730
> 480
> 11Y56787
> 0.160
> 640
> 480
> 5T25014
> 0.020
> 0.500
> 0.480
> LN26328
> 0.310
> 0.780
> 0.470
> 丫C66172
> 0.500
> 0.970
> 0.470


---

### 帖子 #11: AIAC 2025的一些小 Tips
- **主帖链接**: https://support.worldquantbrain.com[L2] AIAC 2025的一些小 Tips_36141016690199.md
- **讨论数**: 3

1. 关于 ra 打 tag 问题

所有提交的 ra 都必须打上父 alpha id 的 tag，有条件的话最好 check 一下，会出现 "Eligible to be a component alpha in AIAC2025 Super Alpha." 的 pass。


> [!NOTE] [图片 OCR 识别内容]
> 11PASS
> Turnover of 5.79% is above cUtoff of 1%.
> Turnoverof 5.79% is below cutoff of 709.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 0.88 is above cUtoff of 0.55.
> Self-correlation is 0.1065, Which is above cUtoff of 0.7, or Sharpe is better by 10.0% or more:
> Data overuse check passed.
> Alpha submissions 2 below quota of 4.
> 2 year Sharpe of 1.68 is above cutoff of 1.58.
> Power Pool correlation 0.0913 is below cutoff of 0.5,or Sharpe is better by 10.0% or more。
> Pyramid theme USAIOIMODELmatches with multiplierof 1,3. Effective pyramid count for Genius is 1.
> Eligible to be a component alpha in AIAC2025 Super Alpha.


以下是一个 ppa 提交后，正确打 tag 的示例。实测发现，ra 是可以提交后再补 tag 的。


> [!NOTE] [图片 OCR 识别内容]
> 匕 Properties
> Last saved Wed, 11/05/2025,3:52 PM
> Name
> Category
> Currently 'anonymous'
> None
> Tags
> Color
> GXmVo8gl
> PowerPoolSelected
> 又
> None
> Description
> 891
> 100 character minimum


2. 关于 sa 打 tag 的问题

sa 的 select 语句中必须要有 in(tags, ${parent_alpha_id})，其中 ${parent_alpha_id} 必须是 ra 提交时打上的 tag，以下是一个 sa 的示例：


> [!NOTE] [图片 OCR 识别内容]
> Code
> Selection Expression
> 1
> in(tags, "VRWrPgLG"))
> Combo Expression


**sa 提交前必须先打好 parent alpha Id 的 tag 和所使用的大模型的 tag，记住！是必须提交前先打好tag！提交前先打好tag** ！提交后补 tag 是不算比赛 alpha 的（别问我是怎么知道的。。）以下是 sa 提交前的 tag 示例：


> [!NOTE] [图片 OCR 识别内容]
> Name
> Category
> XgGO9X8a
> None
> Tags
> Color
> VRWrPgLG
> 又
> Qwen3-max 义
> None


最好在提交前 check 一次，会有 “Competition Al Alphas Competition 2025 matches.” 的 pass


> [!NOTE] [图片 OCR 识别内容]
> 9 PASS
> Sharpe Of 3.25 is above cutoff of 1.58.
> Fitness of 2.82is above cUtoff of 1.
> Turnoverof 6.44% is above cutoff of 2%
> Turnover of 6.44% is below cUtoff of 400
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 2.28 is above cUtoff of 1.41.
> This alpha is self SuperAlpha。
> IS ladder Sharpe of 3.24 is above cutoff of 2.02 for ladder year 2: 1/20/2023..1/21/2021.
> Competition Al Alphas Competition 2025 matches。


3. 比赛过程中的小心得

每天的前四个 ra 可以正常按自己赛季节奏，该点塔点塔，该做 theme 做 theme。交够 4 个后， **尽量多交** 通过父 ra 衍生出来的子 ra，把父 ra 对应的 tag 池子做大，这样 sa select 的时候才有操作空间。

像我之前有一天交了 68 个 alpha，多交池子大了，sa 就好做了。


> [!NOTE] [图片 OCR 识别内容]
> 11/02/2025
> Submitted Alphas: 68


---

### 帖子 #12: AI比赛参考工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] AI比赛参考工作流_35831427191703.md
- **讨论数**: 15

千万不能思维受限


> [!NOTE] [图片 OCR 识别内容]
> Start
> USer
> provides seed
> alpha id
> Authenticate with BRAIN
> and LLM gateway
> Analysil phase
> Fetch alpha details
> code and se
> ttings
> 2. Identify operators and
> data fields Used
> Core research LOOD
> 4.AI powered reflection
> LLLLiHor
> Fetch context for each
> LLM experiment
> b. Query API for all related
> Generate performance
> component from BRAIN API
> summary and next steps
> alphas by tag
> comparison graphs
> 4. Call LLM to generate
> 5. Select new champion
> economic rationale
> for next iteration
> Output
> group of variation
> Step 3 - Al powered
> alphas
> End result
> family
> ideation
> of optimized alphas
> SuperAlpha
> 3.3 Settings variation
> 3.2 Data field variation
> 3.1 Operator variation
> Generate new alpha
> expressions
> Simulate evaluate and
> Simulate on BRAIN
> With parent id
> Retrieve performance
> results
> Performance results
> Tag


如果觉得阅读有困难，可以复制下面代码，到 [[链接已屏蔽])  生成高清流程图

```
graph TDA[Start - user provides seed alpha id] --> B[Authenticate with BRAIN and LLM gateway]subgraph AnalysisPhase [Analysis phase]  direction TB  C1[1. Fetch alpha details - code and settings]  C2[2. Identify operators and data fields used]  C3[3. Fetch context for each component from BRAIN API]  C4[4. Call LLM to generate economic rationale]  C1 --> C2 --> C3 --> C4endB --> C1subgraph CoreLoop [Core research loop]  direction TB  I{Step 3 - AI powered ideation}  I --> V1[3.1 Operator variation]  I --> V2[3.2 Data field variation]  I --> V3[3.3 Settings variation]  V1 --> G[Generate new alpha expressions]  V2 --> G  V3 --> G  subgraph SimEvalTag [3. Simulate evaluate and tag for each generated expression]    direction TB    S1[a. Simulate on BRAIN]    S2[b. Tag with parent id]    S3[c. Retrieve performance results]    S1 --> S2 --> S3  end  G --> SimEvalTag  S3 --> R[Performance results]  subgraph ReflectViz [4. AI powered reflection and visualization]    direction TB    N1[a. LLM experiment summary and next steps]    N2[b. Query API for all related alphas by tag]    N3[c. Generate performance comparison graphs]  end  R --> ReflectViz  ReflectViz --> CH[5. Select new champion for next iteration]  CH --> IendC4 --> ICH --> OUT[Output - group of variation alphas - End result - family of optimized alphas - SuperAlpha]
```

---

### 帖子 #13: BRAIN Genius: Improving Combined Alpha Performance被推荐的
- **主帖链接**: https://support.worldquantbrain.com[L2] BRAIN Genius Improving Combined Alpha Performance被推荐的_27758121327639.md
- **讨论数**: 60

[Combined Alpha Performance](/hc/en-us/articles/26715994416535-What-is-Combined-Alpha-Performance)  is an important eligibility criterion for achieving higher tiers in the BRAIN Genius Program. In this post, let’s explore potential ways of improving this score.


> [!NOTE] [图片 OCR 识别内容]
> How does correlation affect Combined Alpha Performance?
> Based on modern
> portfolio theory, along with some assumptions, the combined Sharpe Of yoUT
> submitted Alphas can be approximated as:
> S
> Here
> 5is Sharpe Of combined Alphas
> Sais average Sharpe Of submitted Alphas
> is number of submitted Alphas,and
> is average pair-wise correlation af submitted Alphas
> Case 1: Let's consider a Case Where
> ~ 0, thatis, uncorrelated Alphas are submitted
> Substitutingthe value of
> in the equation gives
> favourable outcome:
> ViSa
> This is helpful as SubmittingWgreWncorrelated Alphas Improyes the combined Nlphaperformance:
> Case 2: Let's consider a Case Where
> that is, highly correlated Alphas are submitted
> Substitutingthe value of
> in the above equation; gives the
> following Sharpe Of combined Alpha:


This implies that submitting highly correlated Alphas keeps combined Sharpe closer to average Sharpe of the Alphas.


> [!NOTE] [图片 OCR 识别内容]
> Actionable tips to potentially improve Combined Alpha
> Performance
> Increasing average Sharpe 5:


- To enhance the combined performance, it’s important to focus on the OS (Out-of-Sample) Sharpe ratio of the submitted Alphas. Overfitting during the IS period can lead to misleading performance metrics, which don’t generalize well to new data
- Overfitting can be limited by leveraging the  [Test period](../顾问 CC40930 (Rank 95)/[Commented] [BRAIN TIPS] How can I use the test period to improve the OS performance of my Alpha_22205077935895.md)  feature, conducting  [Robustness Tests](../顾问 CC40930 (Rank 95)/[Commented] Robustness Test_25238340364695.md) , and keeping your Alpha expressions explainable.


> [!NOTE] [图片 OCR 识别内容]
> Decrease inner correlation acro5s Alphas


- Adding noise to an Alpha to try to achieve lower correlation is often ineffective, as all Alphas may still have poor performance simultaneously in the OS period if the underlying signal degrades
- Instead of relying on noise to reduce correlation, focus on  [achieving orthogonality](../顾问 AM60509 (Rank 61)/[L2] [BRAIN TIPS] How do you reduce correlation of a good alpha_8046468280727.md)  through innovative use of operators and diverse datasets, ensuring that signals remain distinct and robust
- Submitting uncorrelated Alphas in different pyramids is also essential for building a robust Alpha pool, ensuring resilience to drawdowns in any single pyramid

---

### 帖子 #14: How to Improve After Cost Performance置顶的
- **主帖链接**: [L2] How to Improve After Cost Performance置顶的.md
- **讨论数**: 228

Improving After Cost Performance plays an important role in improving Combined Alpha Performance. In this post, we will share some tips to improve on  [***After-cost Sharpe ratio***](/hc/en-us/articles/25960264611351-What-s-After-cost-Sharpe-ratio) .

1. **Manage Turnover** : Consider both average daily and maximum daily turnover. Use daily turnover plots to identify turnover peaks. Try to reduce high peaks of turnover, even if the average daily turnover is already low.
   
> [!NOTE] [图片 OCR 识别内容]
> Average Turnover is Iow, but max turnoveris high:
> Average Turnoveris the same, max turnover is lower
> Chart
> Turnoer
> Chart
> Turnover
> L0
> 38
> 36。
> Jul 1
> Jon't
> Jan 15
> Jults
> Jull6
> Jun 1
> Jul
> Jan *18
> Jultg
> Jnn1g
> Jn'20
> Jonl
> Jan'15
> Jul15
> Jan"6
> Jult6
> Jul
> Jn'13
> Jonlg
> Jol1g
> Jn 20 Jul 20
> J|
> O
> Jul
> JTo
> u
 Use tradewhen, hump, ts_target_tvr_delta_limit, ts_delta_limit operators to control turnover.
2. **Optimize Alpha Weights Distribution** : Ensure the distribution of Alpha weights by capitalization is balanced. Use visualization tools to check the size by capitalization, ensuring it is evenly distributed or skewed towards high-capitalization stocks.
   
> [!NOTE] [图片 OCR 识别内容]
> Size is skewed to low capitalization part of universe (0-20%)=
> Size is skewed to high capitalization part of universe (80-100%):
> Chart
> UETAe SZe Cy LA9It
> Iaton
> N Chart
> uVeraBe SIZe By Capital
> ALTC
> OILTC
> 0201
> GC
> L5
> AFTm
> 741
> 05T
> 0-209
> 20-409
> 40-605
> 60-805
> 801009
> 020
> 20405
> UFT;
> 60-809
> 87-1009
> LatICn

3. **Ensure High Coverage** : Focus on maintaining good coverage, especially in the liquid part of the universe. Coverage (long plus short count) should be at least half of the universe and should come from liquid stocks. Short count should not be much higher than long count.
   
> [!NOTE] [图片 OCR 识别内容]
> Long count
> short count less then half of Universe size (TOP3000), short count greater then long count:
> Vear
> TIOVer
> Ftnoss
> Returns
> Drawdown
> Count
> Short Count
> 712
> -0.80
> 5J.5:
> 0.3
> 1031
> 9.571
> 一:
> 353
> 3013
> 61,83
> 9,57
> 339
> 3.135
> 71-
> 0.02
> 5J.41:
> -0.275
> 10.731
> 02
> 7015
> 0,75
> 60,949
> 33
> 7003
> 375
> 393
> 5-3
> 7016
> 0.13
> 51.35?
> 00-
> 28035
> 19.3191
> 0.31
> 411
> 533
> -017
> 0.53
> 61,73
> 01-
> 一03
> 5.2491
> 13
> 390
> 5
> 7013
> 1 4
> 60.30
> 0.3-
> 20.755
> 1-191
> 6.31
> 397
> 5-
> 2019
> 1_
> 59.52
> 0.3-
> 70.6293
> 53
> 5
> 2020
> 62.66
> 13.2540
> 77.-59
> 33525
> 392
> SD
> Long count + short count close to Universe size (TOP3000), long count approx. equal to short count
> Year
> TUINOVeT
> Ftness
> Returs
> Drawdown
> Maryin
> Cont
> Short Count
> 201
> -9
> 74034
> 1.10
> 1-:
> 3.15
> 90
> 151
> 1+35
> 2013
> 2.5
> 73.59
> 1345
> 375
> 655
> 1557
> 1474
> 201-
> 73-5:
> 1.70
> 335:
> 525
> 1
> 1535
> 1433
> 21
> 73.55;:
> 17:
> 495
> 3::
> 51
> 122
> 2015
> 73.37:
> 057
> 1 -3:
> -15
> 3::
> 53
> S
> 7017
> 73.33
> 51:
> 477
> 1.55
> 53
> 1493
> 3013
> 7354
> 0
> 1255
> 50
> 49
> 153
> 1517
> 2013
> 72.351
> D0i
> 0.75:
> 955
> 021s
> 1525
> 1510
> 2027
> 412
> 75.97:
> 73.51:
> 一5
> 21.3::
> 1-
> 1453
> Sharp
> Marmn
> L9
> 5。
> Sharpe
> Long

4. **Evaluate Sub-Universe Performance** : Check sub-universe test results and avoid submitting. Alphas that only just pass the Sub-universe Sharpe test. You can also construct your own sub-universe tests using fields from the Universe dataset to evaluate performance across all sub-universes.
   
> [!NOTE] [图片 OCR 识别内容]
> Original alpha. USA/dI/TOP3OOO/Market:
> signal
> tsdecaylinear(-returns, 5);
> alpha
> scale(group_neutralize(signal
> subindustry));
> alpha
> Aggregate Data
> Sharpe
> TUTnOET
> FIIES =
> TETUPI=
> LRaVCC
> Marain
> 1.90
> 73.66%
> 0.90
> 16.43%
> 9.169
> 4.469000
> Apply TOPSOO sub-universe test using 'tOp5OO' data field:
> Signal
> tsdecay linear(-
> returns _
> 5);
> alpha
> Scale
> Broup_neutralize(signal_
> subindustry));
> top500>0
> alpha
> han
> ABgreBate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drswoown
> Marain
> 1.17
> 73.319
> 0.47
> 11.6796
> 11.769
> 3.180000

5. **Turn on Max Trade option for ASI Alphas** : The Max Trade option must be set to ON for all Alphas in the ASI region. This setting optimizes ASI Alphas and improves After Cost Performance at combo level.

---

### 帖子 #15: How to Improve After Cost Performance置顶的
- **主帖链接**: https://support.worldquantbrain.com[L2] How to Improve After Cost Performance置顶的_29647491881623.md
- **讨论数**: 149

Improving After Cost Performance plays an important role in improving Combined Alpha Performance. In this post, we will share some tips to improve on  [***After-cost Sharpe ratio***](/hc/en-us/articles/25960264611351-What-s-After-cost-Sharpe-ratio) .

1. **Manage Turnover** : Consider both average daily and maximum daily turnover. Use daily turnover plots to identify turnover peaks. Try to reduce high peaks of turnover, even if the average daily turnover is already low.
   
> [!NOTE] [图片 OCR 识别内容]
> Average Turnover is Iow, but max turnoveris high:
> Average Turnoveris the same, max turnover is lower
> Chart
> Turnoer
> Chart
> Turnover
> L0
> 38
> 36。
> Jul 1
> Jon't
> Jan 15
> Jults
> Jull6
> Jun 1
> Jul
> Jan *18
> Jultg
> Jnn1g
> Jn'20
> Jonl
> Jan'15
> Jul15
> Jan"6
> Jult6
> Jul
> Jn'13
> Jonlg
> Jol1g
> Jn 20 Jul 20
> J|
> O
> Jul
> JTo
> u
 Use tradewhen, hump, ts_target_tvr_delta_limit, ts_delta_limit operators to control turnover.
2. **Optimize Alpha Weights Distribution** : Ensure the distribution of Alpha weights by capitalization is balanced. Use visualization tools to check the size by capitalization, ensuring it is evenly distributed or skewed towards high-capitalization stocks.
   
> [!NOTE] [图片 OCR 识别内容]
> Size is skewed to low capitalization part of universe (0-20%)=
> Size is skewed to high capitalization part of universe (80-100%):
> Chart
> UETAe SZe Cy LA9It
> Iaton
> N Chart
> uVeraBe SIZe By Capital
> ALTC
> OILTC
> 0201
> GC
> L5
> AFTm
> 741
> 05T
> 0-209
> 20-409
> 40-605
> 60-805
> 801009
> 020
> 20405
> UFT;
> 60-809
> 87-1009
> LatICn

3. **Ensure High Coverage** : Focus on maintaining good coverage, especially in the liquid part of the universe. Coverage (long plus short count) should be at least half of the universe and should come from liquid stocks. Short count should not be much higher than long count.
   
> [!NOTE] [图片 OCR 识别内容]
> Long count
> short count less then half of Universe size (TOP3000), short count greater then long count:
> Vear
> TIOVer
> Ftnoss
> Returns
> Drawdown
> Count
> Short Count
> 712
> -0.80
> 5J.5:
> 0.3
> 1031
> 9.571
> 一:
> 353
> 3013
> 61,83
> 9,57
> 339
> 3.135
> 71-
> 0.02
> 5J.41:
> -0.275
> 10.731
> 02
> 7015
> 0,75
> 60,949
> 33
> 7003
> 375
> 393
> 5-3
> 7016
> 0.13
> 51.35?
> 00-
> 28035
> 19.3191
> 0.31
> 411
> 533
> -017
> 0.53
> 61,73
> 01-
> 一03
> 5.2491
> 13
> 390
> 5
> 7013
> 1 4
> 60.30
> 0.3-
> 20.755
> 1-191
> 6.31
> 397
> 5-
> 2019
> 1_
> 59.52
> 0.3-
> 70.6293
> 53
> 5
> 2020
> 62.66
> 13.2540
> 77.-59
> 33525
> 392
> SD
> Long count + short count close to Universe size (TOP3000), long count approx. equal to short count
> Year
> TUINOVeT
> Ftness
> Returs
> Drawdown
> Maryin
> Cont
> Short Count
> 201
> -9
> 74034
> 1.10
> 1-:
> 3.15
> 90
> 151
> 1+35
> 2013
> 2.5
> 73.59
> 1345
> 375
> 655
> 1557
> 1474
> 201-
> 73-5:
> 1.70
> 335:
> 525
> 1
> 1535
> 1433
> 21
> 73.55;:
> 17:
> 495
> 3::
> 51
> 122
> 2015
> 73.37:
> 057
> 1 -3:
> -15
> 3::
> 53
> S
> 7017
> 73.33
> 51:
> 477
> 1.55
> 53
> 1493
> 3013
> 7354
> 0
> 1255
> 50
> 49
> 153
> 1517
> 2013
> 72.351
> D0i
> 0.75:
> 955
> 021s
> 1525
> 1510
> 2027
> 412
> 75.97:
> 73.51:
> 一5
> 21.3::
> 1-
> 1453
> Sharp
> Marmn
> L9
> 5。
> Sharpe
> Long

4. **Evaluate Sub-Universe Performance** : Check sub-universe test results and avoid submitting. Alphas that only just pass the Sub-universe Sharpe test. You can also construct your own sub-universe tests using fields from the Universe dataset to evaluate performance across all sub-universes.
   
> [!NOTE] [图片 OCR 识别内容]
> Original alpha. USA/dI/TOP3OOO/Market:
> signal
> tsdecaylinear(-returns, 5);
> alpha
> scale(group_neutralize(signal
> subindustry));
> alpha
> Aggregate Data
> Sharpe
> TUTnOET
> FIIES =
> TETUPI=
> LRaVCC
> Marain
> 1.90
> 73.66%
> 0.90
> 16.43%
> 9.169
> 4.469000
> Apply TOPSOO sub-universe test using 'tOp5OO' data field:
> Signal
> tsdecay linear(-
> returns _
> 5);
> alpha
> Scale
> Broup_neutralize(signal_
> subindustry));
> top500>0
> alpha
> han
> ABgreBate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drswoown
> Marain
> 1.17
> 73.319
> 0.47
> 11.6796
> 11.769
> 3.180000

5. **Turn on Max Trade option for ASI Alphas** : The Max Trade option must be set to ON for all Alphas in the ASI region. This setting optimizes ASI Alphas and improves After Cost Performance at combo level.

---

### 帖子 #16: Lab中处理Vector数据的一种方法代码优化
- **主帖链接**: [L2] Lab中处理Vector数据的一种方法代码优化.md
- **讨论数**: 0

这几天使用Lab时发现在可视化Vector数据时会报错，我的方法是定义一些函数，然后在读取原始数据后对Vector数据处理并进行可视化。

**1. 定义函数**

```
def vec_sum(x):    if isinstance(x, (list, np.array):        return np.sum(x)    return np.nandef vec_count(x):    if isinstance(x, (list, np.array):        return len(x)    return np.nandef vec_max(x):    if isinstance(x, (list, np.array):        return np.max(x)    return np.nan
```

**2. 可视化时调用**

```
model_field_df = brain.get_data_frame(brain.get_data_field("close"), universe="TOP3000", dates=[(">", "2021-01-01")]vec_processed_df = model_field_df.map(vec_max)visualizations.plot_values_distribution([vec_processed_df], names=["close values distribution"], nbins=100)
```

函数我只定义了几个常用的，各位可以根据自己的需求扩展。这个方法比较方便，输入一次后未来的代码修改量很小，某种程度也避免了Lab输入的效率低和复制粘贴不方便的问题。

以上就是我的方法，希望能帮助到大家。最后祝各位研究和投资顺利！

---

### 帖子 #17: Lab中处理Vector数据的一种方法代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] Lab中处理Vector数据的一种方法代码优化_33741724514455.md
- **讨论数**: 0

这几天使用Lab时发现在可视化Vector数据时会报错，我的方法是定义一些函数，然后在读取原始数据后对Vector数据处理并进行可视化。

**1. 定义函数**

```
def vec_sum(x):    if isinstance(x, (list, np.array):        return np.sum(x)    return np.nandef vec_count(x):    if isinstance(x, (list, np.array):        return len(x)    return np.nandef vec_max(x):    if isinstance(x, (list, np.array):        return np.max(x)    return np.nan
```

**2. 可视化时调用**

```
model_field_df = brain.get_data_frame(brain.get_data_field("close"), universe="TOP3000", dates=[(">", "2021-01-01")]vec_processed_df = model_field_df.map(vec_max)visualizations.plot_values_distribution([vec_processed_df], names=["close values distribution"], nbins=100)
```

函数我只定义了几个常用的，各位可以根据自己的需求扩展。这个方法比较方便，输入一次后未来的代码修改量很小，某种程度也避免了Lab输入的效率低和复制粘贴不方便的问题。

以上就是我的方法，希望能帮助到大家。最后祝各位研究和投资顺利！

---

### 帖子 #18: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: [L2] Machine Alpha 基础知识1什么是Alpha模板.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #19: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #20: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: [L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #21: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #22: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 进阶知识2如何优化Alpha模板中的参数案例续_28133464556311.md
- **讨论数**: 2

各位研究顾问，大家好。承接上文👉 [Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一](../顾问 JR23144 (Rank 6)/[Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一_27789509613335.md)  我们讨论了如何使用爬山算法（梯度下降）来找到局部最优点的参数。您可能已经熟悉了整体概念。然而，即使在引入随机重启的情况下改变了最初的爬山算法，仍然有改进的空间，因为每次重启并没有利用先前的信息。今天，我们将通过探索几种可以增强算法的修改来结束这一话题的简单讨论。🚀

### 普通随机爬山算法的基本结构

1. **初始化** ：从初始参数开始。
2. **评估** ：回测表达式并获得其适应度。
3. **选择** ：通过随机选择一个不同的参数来识别邻近组合。
4. **比较** ：重新回测更新后的表达式并获得其适应度。
5. **更新** ：如果邻近表达式显示出更好的适应度，则将当前选择更新为这个新参数集。
6. **迭代** ：重复评估、选择、比较和更新步骤，直到在n次迭代后没有进一步的改进。
7. **重启** ：重复上述步骤m次。这是重启机制。

### 智能重启 🔄

要考虑的第一个修改是确保在第七步的每次重启中，算法都会探索以前未遇到的新区域。为实现这一点，您可以在步骤三和四中实现一个参数计数器，每次选择并模拟一个选项时计数器递增。在第七步重启时，不要随机从可用集合中抽取选项，而是使用计数器的逆作为选择的概率。此修改确保每次重启都会选择在先前试验中未探索过的参数。🧠

一些人可能会问：“为什么只创建一个计数器？为什么不设计一个更智能的方法，将Alpha绩效信息入未来的概率中呢？”这是个好主意！具体怎么实现呢？欢迎大家在下面讨论您的想法！💡

### 直线路径可能不是最佳路径 🌄

正如一些人指出的那样，随机爬山算法的贪婪特性使其过于关注即时改进，从而可能忽略更优的曲线路径。有些人建议使用模拟退火作为替代，因为它在探索期间会容忍挫折，这有助于达到全局最优。为了使随机爬山算法达到类似的效果，您可以在步骤四中引入一些白噪声。这增加了选择“最佳”邻居的随机性。

有时，“最佳”邻居的适应度可能在短期内不佳，但在未来步骤中有更好的解决方案潜力！您还可以设计动态噪声，在早期阶段引入更多白噪声，并在后期逐渐减少——类似于模拟退火中的温度衰减。❄️🔥

这篇文章总结了关于爬山算法及其在Alpha研究中的应用的小系列。如果您对这些主题感兴趣，请留下评论告诉我们！💬

更多类似原文，可关注全球顾问论坛👉 [[Alpha Machine] How do you improve random-hill-climbing optimization](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Machine] How do you improve random-hill-climbing optimization被推荐的Alpha Template_27789493782935.md)

Credit to:YW42946

---

### 帖子 #23: Maximizing Combined Alpha Performance: Key Strategies and Insights
- **主帖链接**: https://support.worldquantbrain.com[L2] Maximizing Combined Alpha Performance Key Strategies and Insights_28436901080471.md
- **讨论数**: 60

The Combined Alpha Performance Score is a critical metric for reaching higher tiers in the BRAIN Genius Program. It measures how effectively your submitted Alphas work together, balancing individual performance and the synergy between them. Here’s a detailed breakdown of the factors influencing this score and strategies to improve it.

### **1. What Influences Combined Alpha Performance?**


> [!NOTE] [图片 OCR 识别内容]
> The combined Sharpe (Sc) of your Alphas is determined by three key factors:
> Average Sharpe (Sa): Higher Sharpe ratios for individual Alphas lead to a stronger combined
> SCOre
> Number of Alphas (n): Increasing the number of Alphas boosts performance, especially
> When they are uncorrelated。
> Correlation (p): Lower correlation between Alphas enhances diversification, improving the
> combined Sharpe.
> The combined Sharpe can be approximated by:
> Sa
> Sc
> 1 +
> 阮p
 ​​

### **2. Effects of Key Parameters**

**
> [!NOTE] [图片 OCR 识别内容]
> Impact of Correlation (p):
> Uncorrelated Alphas (p
> 0)
> The combined Sharpe scales with the square root of the number of Alphas
> providing
> significant diversification benefits.
> Highly Correlated Alphas (p
> 1):
> The combined Sharpe equals the average Sharpe (Sa), as diversification effects disappear。
> RSa'
**


> [!NOTE] [图片 OCR 识别内容]
> Impact of Number of Alphas (n):
> Adding more Alphas significantly improves the combined Sharpe When correlation is low. However;
> the benefit diminishes as correlation increases.
> Below is a table
> showing how the combined Sharpe changes with different values of n (number of
> Alphas) and p (correlation) , assuming an average Sharpe (Sa) of 1:
> Number
> Of
> Correlation
> Correlation
> Correlation
> Correlation
> Correlation
> Correlation
> Alphas
> 0.0
> 0.1
> 0.3
> 0.5
> 0.7
> 1.0
> 1.000
> 1.000
> 1.000
> 1.000
> 1.000
> 1.000
> 5
> 2.236
> 1.890
> 1.508
> 1.291
> 1.147
> 1.000
> 10
> 3.162
> 2.294
> 1.644
> 1.348
> 1.170
> 1.000
> 20
> 4.472
> 2.626
> 1.728
> 1.380
> 1.183
> 1.000
> 50
> 7.071
> 2.911
> 1.785
> 1.400
> 1.190
> 1.000
> 100
> 10.000
> 3.029
> 1.805
> 1.407
> 1.193
> 1.000


### **3. Strategies to Boost Combined Alpha Performance**

#### **1. Focus on Low-Correlation Alphas**

**
> [!NOTE] [图片 OCR 识别内容]
> Reduce pairwise correlation (p) by diversifying strategies, datasets, and regions。
> Use operators like  group_neutralize
> and
> group_rank
> to achieve orthogonality。
**

#### **2. Submit Uncorrelated Alphas Across Pyramids**

- Spread Alphas across multiple pyramids to mitigate drawdowns in any single pyramid.

#### **3. Increase the Number of Alphas**

- Add more Alphas to your submission pool, ensuring they remain sufficiently uncorrelated.

#### **4. Prioritize High OS Sharpe Ratios**

- Validate Alphas with the  **Test Period**  and Robustness Tests to avoid overfitting.
- Keep Alpha expressions simple and explainable to enhance  **out-of-sample**  (OS) performance.

### **4. Practical Insights from the Data**

- Submitting  **10 uncorrelated Alphas**  can improve the combined Sharpe by over  **200%**  compared to submitting a single Alpha.
- As correlation increases, the combined Sharpe converges to the average Sharpe, limiting diversification benefits.

### **Final Thoughts**

Maximizing Combined Alpha Performance requires a balance of high individual Sharpe ratios, low correlation, and an appropriately sized Alpha pool. By focusing on orthogonality and robustness, you can unlock the full potential of diversification, build resilience, and climb to higher tiers in the BRAIN Genius Program.

Let’s collaborate and share ideas! How do you ensure low correlation and high OS Sharpe in your submissions? Drop your tips and strategies in the comments below!

---

### 帖子 #24: 4、 **减少生产相关性**
- **主帖链接**: https://support.worldquantbrain.com[L2] Reduce Production Correlations_29301199149463.md
- **讨论数**: 66

Reducing production correlation in  **regular alphas**  is crucial for creating a diversified and robust strategy that avoids overfitting and ensures better out-of-sample performance. Here are some best practices to reduce production correlation:

### 1.  **Diversify Data Sources**

- **Use Multiple Data Types** : Integrating different types of data such as  **price data** ,  **fundamental data** ,  **alternative data** , and  **sentiment data**  can help create factors that capture different market dynamics.
- **Cross-Asset Signals** : Consider using signals from multiple asset classes (e.g., equities, commodities, bonds) to create alphas that are less likely to be highly correlated.

### 2.  **Factor Neutralization**

- **Industry, Sector, or Size Neutralization** : By neutralizing factors such as  **sector** ,  **industry** , or  **size** , you can ensure that the factors are not overly sensitive to these systematic effects. This helps in reducing common exposures that might lead to high correlation.
- **Group Neutralization** : Using neutralization techniques, such as  `group_coalesce` , helps eliminate correlations related to factors like  **market capitalization** ,  **geographic region** , or  **sector** .

### 3.  **Adjust Factor Construction**

- **Use Different Factor Combinations** : Combine factors in various ways to capture diverse relationships. For instance, combining  **momentum**  with  **value**  and  **volatility**  can help reduce overlap and correlation between them.
- **Rotating Factor Models** : Apply different sets of factors across different periods, or dynamically select factors based on current market conditions. This can help avoid periods where certain factors become highly correlated due to macroeconomic or market events.

### 4.  **Regularize and Penalize Correlated Factors**

- **L1/L2 Regularization** : Apply regularization techniques like  **Lasso (L1)**  or  **Ridge (L2)**  regularization to reduce the weights of correlated factors, which can help in decreasing redundancy in the alpha model.
- **Correlation Penalty** : Explicitly penalize high correlation between factors during the optimization process. By incorporating a penalty term for correlation in the objective function, you can minimize redundant factors.

### 5.  **Clustering and Factor Selection**

- **Factor Clustering** : Perform  **hierarchical clustering**  or  **principal component analysis (PCA)**  to group factors based on their correlation structure. You can then select a diverse set of representative factors from each cluster to build the final alpha.
- **Use Unique, Uncorrelated Factors** : After clustering, identify the factors with the most unique signals. Incorporating these into your alpha can reduce the risk of overlapping information.

### 6.  **Independent and Unique Signal Generation**

- **Non-Linear Features** : Consider generating non-linear features or using models that can capture complex interactions between signals (such as  **random forests** ,  **boosting methods** , or  **neural networks** ). These models can produce signals that are less correlated with traditional linear factors.
- **Alternative Metrics** : Use less conventional metrics such as  **tweet sentiment** ,  **web traffic** , or  **geospatial data**  in combination with traditional factors. These may provide additional insights that are less correlated with typical market drivers.

### 7.  **Backtest with Multiple Regions or Timeframes**

- **Cross-Market Testing** : Run your alphas in different markets (e.g., USA, Europe, Asia) to check if they exhibit correlation patterns. This can help identify when certain alphas are more likely to perform well or be dominated by global trends.
- **Out-of-Sample Validation** : Test your alphas on different time periods and market conditions (e.g., different economic cycles) to ensure robustness and minimize the likelihood of overfitting to specific market regimes.

### 8.  **Dynamic Adjustments and Risk Management**

- **Dynamic Weights** : Adjust the weights of different alphas dynamically based on their recent performance, volatility, or correlation with the market. This approach helps in reducing the concentration of risk.
- **Risk-Based Position Sizing** : Use risk-based position sizing to ensure that no single factor or alpha dominates the portfolio, thus reducing the potential for large exposures to highly correlated alphas.

### 9.  **Monitor and Optimize in Real-Time**

- **Real-Time Performance Monitoring** : Continuously monitor the performance of alphas and their correlation with each other in real-time. This allows you to make timely adjustments to reduce redundancy or mitigate correlation spikes.
- **Optimization over Rolling Windows** : Use  **rolling window optimization**  to adjust for changing correlation patterns over time. This ensures the alpha remains adaptive to evolving market conditions.

By applying these best practices, you can create a more  **diversified and robust alpha** , reducing correlation between factors and improving overall portfolio performance. Regularly evaluating and adapting the factors, as well as incorporating multiple data sources and modeling techniques, will help ensure that your alphas maintain their effectiveness in a dynamic market environment.

---

### 帖子 #25: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location']
- **主帖链接**: https://support.worldquantbrain.com[L2] Super alpha全自动回测代码--开箱即用代码优化_32637672256663.md
- **讨论数**: 30

功能省流：随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。

特点：整合了中文论坛中的super alpha代码，点击即用

感谢顾问 JL16510 (Rank 18)大佬的多线程回测代码，感谢WP88606大佬的随机生成表达式代码。我对这两篇代码做了整合，并做了一些调整，目前用该代码生成提交了几个比赛的super alpha，指标都还可以，遂分享给大家，希望能有所帮助！

有用的话还请帮忙点个小赞！

回测程序（运行这个）superAlpha.py

```
import threadingfrom machine_lib import *import randomimport selection_expressions as seneutralization_list = ["NONE","MARKET","SECTOR","INDUSTRY","SUBINDUSTRY"]conditions = [    se.category_conditions(),    se.color_conditions(),    se.neutralization_conditions(neutralization_list),    se.datacategories_conditions(),    se.datacategory_count_conditions(),    se.dataset_count_conditions(),    se.datafield_count_conditions(),    se.long_count_conditions(),    se.short_count_conditions(),    se.operator_count_conditions(),    se.prod_correlation_conditions(),    se.self_correlation_conditions(),    se.truncation_conditions(),    se.turnover_conditions(),    se.os_start_date_conditions]weight_expressions = se.weight_expressions()# 貌似author的选项用不了def author_setting():    # 从这些条件中随机选择1-2个 拼接起来返回    author_option = ["author_returns_to_drawdown>2&&","author_returns_to_drawdown<4&&","author_fitness >= 2&&","author_sharpe >= 2&&"]    # 随机选择1到2个条件    selected_conditions = random.sample(author_option, random.randint(1, 2))    # 拼接条件字符串    result = ''.join(selected_conditions)    return resultdef find_selection_expression():    condition_length = random.randint(1, 3)    condition_list = random.sample(conditions, condition_length)    choice_conditions = []    for condition in condition_list:        if callable(condition):            condition = condition()        choice_conditions.append(random.choice(condition))    choice_weight_expression = random.choice(weight_expressions)    # author_exp = author_setting()    select_expression = "not(own)&&"+"in(classifications, 'POWER_POOL')&&" + ' * '.join([f'({exp})' for exp in (choice_conditions + [choice_weight_expression])])    with open('select_expression.txt', 'a') as f:        f.write(select_expression + '\n')    return select_expressiondef get_combo_code_list():    time_windows1 = [60,120,250,500]    selected_window1 = random.choice(time_windows1)    time_windows2 = [250, 500]    selected_window2 = random.choice(time_windows2)    ret = ['1',           f'stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, {selected_window2}); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr',           ]    return retdef multi_simulate2_sa(alpha_pools, neut, region, universe, start):    global s    s = login()    brain_api_url = '[链接已屏蔽]    limit_of_concurrent_simulations = len(alpha_pools[0])    alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]    end = len(alpha_pools_2)    print(f'length:{len(alpha_pools_2)}, start:{start}')    counter: int = start    lock = threading.Lock()    def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):        while True:            global s            lock.acquire()            nonlocal counter            if counter > end - 1:                lock.release()                break            if (counter - start) % 250 == 0:  # re-login after every 60 multi_sims                s = login()            local_counter = counter            counter += 1            lock.release()            task = pools[local_counter]            sim_data_list = generate_sim_data_sa(task, region, universe, neut)            sim_data=sim_data_list[0]            try:                simulation_response = s.post('[链接已屏蔽] json=sim_data)                print(simulation_response)                simulation_progress_url = simulation_response.headers['Location']                # simulation_progress_url = simulation_response.headers.get('location')            except:                print(" loc key error")                sleep(60)                s = login()            print(f"task {local_counter} post done")            try:                while True:                    simulation_progress = s.get(simulation_progress_url)                    if simulation_progress.headers.get("Retry-After", 0) == 0:                        break                    # print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")                    sleep(float(simulation_progress.headers["Retry-After"]))                status = simulation_progress.json().get("status", 0)                if status != "COMPLETE":                    print(f"Not complete : {simulation_progress_url}")                #alpha_id = simulation_progress.json()["alpha"]                # children = simulation_progress.json().get("children", 0)                # children_list = []                # for child in children:                #     child_progress = s.get(brain_api_url + "/simulations/" + child)                #     alpha_id = child_progress.json()["alpha"]                #                #     set_alpha_properties(s,                #             alpha_id,                #             name = "saTest",                #             color = None,)            except KeyError:                print(f"look into: {simulation_progress_url}")            except Exception as e:                print(f"An error occured:{e}")            print(f"task {local_counter} simulate done")    t = []    for i in range(limit_of_concurrent_simulations):        t.append(threading.Thread(target=sim_task))        t[i].start()    for i in range(limit_of_concurrent_simulations):        t[i].join()    print("Simulate done")def generate_sim_data_sa(alpha_list, region, uni, neut):    sim_data_list = []    for selection_exp, combo_exp in alpha_list:        print(selection_exp)        print(combo_exp)        simulation_data = {            'type': 'SUPER',            'settings': {                'instrumentType': 'EQUITY',                'region': region,                'universe': uni,                'delay': 1,                'decay': 6,                'neutralization': neut,                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'ON',                'selectionHandling': random.choice(['POSITIVE','Non-Zero']),                'selectionLimit': random.choice([100,200,500]),                'language': 'FASTEXPR',                'visualization': False,            },            'selection': selection_exp,            'combo': combo_exp}        sim_data_list.append(simulation_data)    return sim_data_listif __name__ == '__main__':    while True:        selection_exp = []        exp = find_selection_expression()        selection_exp.append(exp)        combo_exp = get_combo_code_list()        sa_list = [(i, j) for i in selection_exp for j in combo_exp]        print(len(sa_list))        print(sa_list[0])        pools = load_task_pool(sa_list, 1, 3)        # print(pools[0])        region_dict = {"usa": ("USA", ["TOP3000", "TOP1000","TOP500", "TOP200"]),                       "asi": ("ASI", ["MINVOL1M"]),                       "eur": ("EUR", ["TOP2500", "TOP1200","TOP800", "TOP400"]),                       "glb": ("GLB", ["TOP3000", 'MINVOL1M']),                       "hkg": ("HKG", ["TOP800", "TOP500"]),                       "twn": ("TWN", ["TOP500", "TOP100"]),                       "jpn": ("JPN", ["TOP1600", "TOP1200"]),                       "kor": ("KOR", ["TOP600"]),                       "chn": ("CHN", ["TOP2000U"]),                       "amr": ("AMR", ["TOP600"])                       }        norm_opt = ["INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"]        risk_opt = ["FAST", "SLOW", "SLOW_AND_FAST"]        r1 = ['STATISTICAL']        cr = ["CROWDING"]        co = ["COUNTRY"]        no = ["NONE"]        neut_opt = {"USA": norm_opt + cr + risk_opt + r1,                    "GLB": co + r1,                    "EUR": co + cr + norm_opt + risk_opt + r1,                    "ASI": co + cr + norm_opt + risk_opt + no,                    "CHN": norm_opt + cr + risk_opt + r1,                    "KOR": norm_opt,                    "TWN": norm_opt,                    "HKG": norm_opt,                    "JPN": norm_opt,                    "AMR": ["COUNTRY"] + norm_opt,                    }        regi = ['usa','asi','eur','glb']        random.shuffle(regi)        for k in regi:            for i in region_dict[k][1][:1]:                print(i)                for j in neut_opt[k.upper()]:                    print(j, region_dict[k][0])                    multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)
```

然后是随机生成selection表达式的代码，放到selection_expressions.py中

```
import datetimedef category_conditions():    values = "NONE", "PRICE_REVERSION", "PRICE_MOMENTUM", "VOLUME", "FUNDAMENTAL", "ANALYST", "PRICE_VOLUME", "RELATION", "SENTIMENT"    return [f"category == \"{value}\"" for value in values]def color_conditions():    values = "NONE", "RED", "YELLOW", "GREEN", "BLUE", "PURPLE"    return [f"category == \"{value}\"" for value in values]def dataset_conditions(dataset):    return [f"in(datasets, \"{dataset}\")"]def favorite_conditions():    return [f"favorite", "not(favorite)"]def long_count_conditions():    return [f"long_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]def short_count_conditions():    return [f"short_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]def name_conditions(name):    return [f"name == \"{name}\""]def neutralization_conditions(neutralizes):    return [f"neutralization == \"{value}\"" for value in neutralizes]def operator_count_conditions():    return [f"operator_count <= {cnt}" for cnt in [1, 2, 4, 6, 8, 10]]def tags_conditions(tag):    return [f"in(tags, \"{tag}\")"]def truncation_conditions():    return [f"truncation <= {value}" for value in [0.01, 0.05, 1]]def turnover_conditions():    return [f"turnover < {value}" for value in [0.05, 0.1, 0.2, 0.3, 0.7]]def universe_conditions(universes):    return [f"universe == \"{value}\"" for value in universes]def universe_size_conditions(size=1000):    return [f"universe_size(universe) >= {size}"]def datafields_conditions(field):    return [f"in(datafields, \"{field}\")"]def dataset_count_conditions():    return [f"dataset_count <= {value}" for value in [1, 2, 3, 10]]def self_correlation_conditions():    return [f"self_correlation <= {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]def prod_correlation_conditions():    return [f"prod_correlation < {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]def os_start_date_conditions():    today = datetime.datetime.today()    delta_days = [7, 14, 30, 60, 90, 120, 180, 360, 3600]    dates = [(today-datetime.timedelta(day)).strftime('%Y-%m-%d')             for day in delta_days]    return [f"os_start_date > \"{date}\"" for date in dates]def datacategories_conditions():    values = "analyst, broker, earnings, fundamental, imbalance, insiders, institutions, \        macro, model, news, option, other, pv, risk, sentiment, shortinterest, socialmedia".split(',')    return [f"in(datacategories, \"{value.strip()}\")" for value in values]def datacategory_count_conditions():    return [f"datacategory_count <= {value}" for value in [1, 2, 3, 10]]def datafield_count_conditions():    return [f"datafield_count <= {value}" for value in [1, 2, 3, 5, 10]]def weight_expressions():    return [        "turnover", '10-turnover',        '10000-abs(long_count-short_count)', 'long_count+short_count', 'long_count', 'short_count',        '10-dataset_count',        '2-self_correlation',        '2-prod_correlation',        '100-datafield_count',        '1'    ]
```

运行 superAlpha.py就可以开始自动回测啦~

当然该代码还有很多小问题，希望大佬们可以继续完善！

都看到这了，点个赞再走吧~~

---

### 帖子 #26: Vscode自动提示operator代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] Vscode自动提示operator代码优化_33274404140439.md
- **讨论数**: 10

有时候一边写代码一边查opeartor网页会非常打断思路, 我们可以基于自己的 JSON 文档开发一个轻量级的 VSCode 插件，提供 **悬停文档** 和 **自动补全** 功能，用于自定义的 **数据字段** 和 **运算符** ，。

 
> [!NOTE] [图片 OCR 识别内容]
> field-operator-hints
> Welcome
> 1U
> test py
> t
> ts_arg
> Iax
> ts_arg_max(x,
> ts_arg_min
> ts_av_diff
> Time Series
> ts_backfill
> ts
> Returns the relative index of the max Value in the tme
> ts
> Count_nans
> series for the past d days
> If the current day has the max
> ts
> covariance
> Value for the past d days, i returns 0.If previous day
> ts_decay
> linear
> has the max Value for the past d days; j returns
> ts_delay
> ts_delta
> ts_ir
> ts
> kurtosis
> test py
> LCOFr
 

大家可以在vscode搜我编译好的插件试一下.

 
> [!NOTE] [图片 OCR 识别内容]
> EXTENSIONS: MARKETPLACE
> brain_s
> brain_snippet
> 2ms
> Worldquant brain platform datafiel..
> Roshameow
> Restart Extensions
> {
> 氐
 
加载自己的opeartors. 像这样, 在这里添加自己的json路径.

 
> [!NOTE] [图片 OCR 识别内容]
> field-operator-hints
> EXTENSIONS: MARKETPLACE
> Welcome
> package.json
> 田 Extension: brain_snippet
> test:py
> Settings
> 义
> brain_
> Jext:Roshameow field-operator-hints
> Setting Found
> brain_snippet
> 2ms
> User
> Workspace
> Backup and Sync Settings
> Worldquant brain platform datafiel..
> Roshameow
> Extensions (1)
> 品
> Field Operator Hints: Custom Operator JSON Path
> Path to a custom operator JSON file (absolute or workspace-relative path)
> 唱
> 囚


---

### 帖子 #27: [AIAC 2025 比赛] 迭代法寻找集合中Score最高SA
- **主帖链接**: https://support.worldquantbrain.com[L2] [AIAC 2025 比赛] 迭代法寻找集合中Score最高SA_36169526810519.md
- **讨论数**: 3

最近一直在参加AIAC比赛，在此分享一些构建 SA（Super Alpha） 的实践与思考，望各位前辈大佬多多指教。

**比赛的核心规则：**

1. 选出parent Alpha；
2. 基于parent Alpha，利用AI生成child Alphas；
3. 使用child Alphas构建SA参赛。

**遭遇的困难：**

我遇到的主要问题是 child Alphas 产出数量不足，导致备选池深度不够，难以组合出高分的 SA。

要从根本上解决这一问题，关键在于优化 prompt 以提升 child Alphas 的产出效率。

然而比赛时间紧迫，我必须在现有条件下，基于已生成的 child Alphas 尽可能构建出高分的  SA，否则连完赛都成问题。 *（此前比赛规则尚未调整，每天只能提交 1 个 SA， 现在规则已改为每天最多可交 4 个）*

**小池子高 score 解决方案：**

由于不清楚比赛对 SA 评分的具体规则，一通摸索后，最终我还是决定采用迭代法：

1. 先从池子中选出 10 个child Alphas，构建基础 SA；（我选了self-cor 最低的10个，并遍历了全部 risk neutralization，选择 score 最高的作为基础 SA）
2. 从剩余 alpha 中逐一遍历，每次选取一个追加到 SA 中并重新回测；(self-cor 低者优先)
3. 若回测后 score 提升，则保留该 alpha；反之则剔除；
4. 如此循环，直至处理完池中所有 child Alphas。

**具体实现（手搓）：**

由于所有 child Alphas 均带有 tag 标记，可通过  `in(tags, "A") ` 表达式筛选出所有component child Alphas。

同时，利用 alpha 的 color 属性标记其状态：color == "BLUE" 表示当前迭代中临时选中，color == "GREEN" 表示最终入选。

SA 的 selection 表达式示例如下：

> `in(tags, "parent_alpha_id") && (color == "GREEN" || color == "BLUE")`

**总结：**

通过迭代法，我确实找到了 score 优于直接全选的SA组合。过程中观察到以下现象，供大家参考：

1. 多数情况下，Sharpe 和 Fitness 越高，score 也越高；
2. 追加的 Alpha 若其 PNL 曲线走势与当前最高分 SA 的 PNL 曲线差异明显，则往往能提高 score 或降低 prod-correlation；
3. 追加的 Alpha 若使用与 SA 现有component Alphas 不同的 Dataset，则往往能显著提升 score。

由于数据样本有限，上述观察仅供参考，尚不足以形成定论，恳请老师和各位批评指正。

---

### 帖子 #28: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
- **主帖链接**: [L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation.md
- **讨论数**: 73

一句话总结该活动：直接在评论区评论，分享你的模板。

> ```
> 被审核通过者将获得BRAIN纪念品一份（下图背包）优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至8.31日23：59（以服务器时间为准） [图片 (图片已丢失)]

活动要求：参赛同学可发布多个模板参赛， **必须展示下列所有元素** 。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。

- 模板
  - **模板中的变量必须使用< />进行声明，不符合语法规则的评论无法参评**
  - 需阐述具体变量赋值，如operator类别、数据集id、地区等
  - 阐述搜索空间的大小
  - 阐述模板的idea，implement细节（即哪步是数据处理，哪步是主信号）
  - 产出效果（回测：Alpha数量，可以仅展示比率）
  - 建议其他顾问未来尝试的探索方向

> **再次强调，必须至少展示上述所有信息👆先到先得！有些模板过于类似的将不再被批复，建议大家快快抓住机会！**

---

### 帖子 #29: 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法
- **主帖链接**: https://support.worldquantbrain.com[L2] 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法_35799099514647.md
- **讨论数**: 8

```
以下是详细说明，帮助您参加比赛。

1. 使用 ACE 库来模拟生成的 Alphas。
2. 使用每个子 Alphas 的父 Alphas ID 来标记每个子 Alpha。
3. 为子 Alpha 添加描述。
4. 模拟和标记的示例逻辑：

#### **提交要求**
1. **SuperAlphas** 必须使用链接到相同父 Alpha ID 的子 Alphas 构建。
2. 通过平台表单提交您的**SuperAlphas**和机器（代码）。
3. 仅考虑您**最后一次机器提交**。

---

### 帖子 #30: 【Alpha模版】模版群助我60天点亮60个塔Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha模版】模版群助我60天点亮60个塔Alpha Template_35253150989719.md
- **讨论数**: 87

**一、前言**

**我是一位freshman，7月1日转正，至今提交295个atom，点亮64座塔。**


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-23 July 1s,2025
> SEptember 30-h,2025
> Gold
> Erpert
> Master
> Grandas-er
> Signals
> 295
> Reached Grandmaster
> Pyramids Completed
> 64
> Reached Grandmaster
> Combined Alpha Performance
> 1.1
> 0.9 more to Grandmaster
> Combined Selected Alpha Performance
> 3.09
> Reached Grandmaster
> Combined Power Pool Alpha Performance
> 1.67



> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st 2025
> September 3oth, 2025
> Operazors pEr Alpna
> Operators Used
> Fields per Alpha
> 3.18
> 81
> 1.55
> Fielos USEJ
> Communizyaczivity
> Waxsinulati?nstreak
> 317
> 35.3
> 215
> Simulationactiviey
> Submissionactiit
> AUE
> Sep
> AUE
> Sep



> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st 2025
> September 3oth, 2025
> Catego
> US
> eIR
> CHN
> L3S
> 3O =
> Esp nEs
> FundaTsta
> ImTaIT=
> IO
> Inaions
> Nro
> Nodsl
> Nsws
> T3t27
> Price Voluns
> Ris
> TTmn
> MOTCITETESC
> Sciallls-la


**二、方法论**

1. 经济学原理是静态框架，而股市运行于人性的动态博弈之中。  
2. 任何超额收益（Alpha）一旦被广泛追逐，便会因拥挤而失效。  
3. 故兵无常势，水无常形，唯有因时应变者，方能持续制胜。

**具体做法：**

**1. 穷举所有：** 挑选可用的模版。比如，一元、二元或三元模版

**2. 避免重复：** 从模版层降低相关性。比如scale、rank、zscore等单操作符模版，多数情况下是重复的，不要堆叠，浪费回测资源。

**3. 先随机再深入：** 首先，对准一个想要点亮的数据集；先用shuffle的方法，随机取样80个组合，计算每个模版的因子密度；如果某个模版因子密度大，就深入挖掘。

[参考虎哥模版实证及其改进效果评价](../顾问 MZ45384 (Rank 51)/[Commented] 【Alpha灵感】虎哥模版实证及其改进效果评价Alpha Template_33768594280343.md)

**三、模版框架（举例）**

**1. 一元模版（模版层面尽量不要有重复，从模版底层降低self-corr）**

```
for a in data_fields:    if index == 0:        # 斜率        expr = f"ts_regression(ts_zscore({a}, 500), ts_step(1), 500, rettype=2)"        factor_expressions.append(expr)    elif index == 1:        # 增长率        expr = f"ts_delta(ts_delta({a}, 252)/ts_delay({a}, 252),252)"        factor_expressions.append(expr)    elif index == 2:        # 增长率        expr = f"ts_delta({a}, 252)/ts_delay({a}, 252)"        factor_expressions.append(expr)    elif index == 3:        # 自回归斜率        expr = f"ts_regression(ts_delta({a}, 252), ts_delta({a}, 500), 500, rettype=2)"        factor_expressions.append(expr)    elif index == 4:        # 平方动量        expr = f"ts_mean(signed_power(ts_delta({a}, 252), 2), 500)"        factor_expressions.append(expr)    elif index == 5:        # 衰减加权动量        expr = f"ts_decay_linear(ts_delta({a}, 252), 500)"        factor_expressions.append(expr)    elif index == 6:        # 排名反转        expr = f"reverse(ts_rank(ts_zscore({a}, 500), 500))"        factor_expressions.append(expr)    elif index == 7:        # 对数平滑        expr = f"log(abs(ts_delta({a}, 500)) + 0.000001)"        factor_expressions.append(expr)    elif index == 8:        # 符号保留幂        expr = f"signed_power(ts_delta({a}, 500), 2)"        factor_expressions.append(expr)    elif index == 9:        # 差分层叠        expr = f"ts_delta(ts_delta({a}, 252), 500)"        factor_expressions.append(expr)
```

**2. 二元模版（降self-corr）**

```
    for a, b in combinations(data_fields, 2):        if index == 0:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500)"            factor_expressions.append(expr)        elif index == 1:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500, rettype=2)"            factor_expressions.append(expr)        elif index == 2:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500, rettype=6)"            factor_expressions.append(expr)        elif index == 3:            expr = f"ts_regression({a}, {b}, 252, rettype=2)"            factor_expressions.append(expr)        elif index == 4:            expr = f"ts_regression({a}, {b}, 500, rettype=2)"            factor_expressions.append(expr)        elif index == 5:            expr = f"regression_neut(s_log_1p({a}), s_log_1p({b}))"            factor_expressions.append(expr)        elif index == 6:            expr = f"vector_neut({a}, {b})"            factor_expressions.append(expr)        elif index == 7:            expr = f"ts_delta_limit({a}, {b}, limit_volume=0.1)"            factor_expressions.append(expr)        else:            continue
```

**3. 三元模版（去self-corr）**

```
    for a, b, c in combinations(data_fields, 3):
        if index == 0:
            # 联合中性化：a 在 b 和 c 上的向量正交
            expr = f"vector_neut(vector_neut({a}, {b}), {c})"
        elif index == 1:
            # 分层回归残差（先对 b 中性化，再对 c）
            expr = f"regression_neut(regression_neut({a}, {b}), {c})"
        elif index == 2:
            # 带约束的时序变化（delta limit，以 b 和 c 的均值为基准）
            expr = f"ts_delta_limit({a}, ({b} + {c}) / 2, limit_volume=0.1)"
        elif index == 3:
            # 三变量时序相关性（a 与 b 的相关性，用 c 作权重或窗口调节）
            expr = f"ts_corr(ts_zscore({a}, 252), ts_zscore({b}, 252), 252) * {c}"
        elif index == 4:
            # 动态排序择时（a 在 b 和 c 构成的分组中做 ts_rank）
            expr = f"ts_rank(group_mean({a}, {b}), 500) * {c}"  # 假设 b 为分组字段
        elif index == 5:
            # 三重交互项（非线性放大）
            expr = f"ts_zscore({a}, 500) * ts_zscore({b}, 500) * ts_zscore({c}, 500)"
        elif index == 6:
            # 条件切换（c 为条件，选择 a 或 b）
            expr = f"if_else({c} > ts_mean({c}, 500), {a}, {b})"
        else:
            continue  # 超出范围跳过
```

**四、应用举例（CHN很难，但实际上也扛不住几次冲锋，突破只是时间问题）**

**1.analyst举例**  
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 0827/2025 EOT
> anonymOUs
> Udd Nphato a Ust
> Code
> IS Summary
> Period
> aIeC
> aVB(a_
> Data SEtJphs
> Powver Pool Hphs
> Pyrsmidthems: CHNDTIANALYST 1.
> bts_decay_Iinear(a;126)
> ts_decay_exP_window(a,
> 252
> factor
> 951;
> siened_power (b,0.5)
> Agaregate
> Uata
> SHelo
> 1.13
> 10.08%
> 1.11
> 12.1796
> 17.39%
> 24.1596o0
> SIIUIatIOn
> Settings
> Year
> Sharpe
> TurOVeT
> Fltss
> Rtur
> Uawdown
> Marln
> Long Cnt
> Short Cot
> Istrut Type
> Regl
> Uelse
> Language
> Ia
> Dlay
> Truncatlon
> Neutrallatlon
> Pastewrtato
> HaN Hanlng
> UnltHandlng
> Max Trate
> EaJi?
> TLN
> TOFZJ
> HasUTEsSIUT
> 7.03
> Crowwire Factors
> TT
> 2013
> 231
> 13.88:
> 250
> 12
> 7.375
> 35.+:
> 201-
> 03
> 11.09::
> 1
> 8.115
> 1.3:
> 2015
> 126
> 1.20:
> 155
> 8.105
> 30.74:
> 15
> 2015
> 353
> 13.5::
> 2233
> 3.235
> 一7:
> 1
> Clone Alpha
> 2017
> 715
> 13.55::
> 1 2
> 7.32
> 37:
> 2013
> 5:
> 12
> 7.395
> 5:
> 13
> N Chart
> Prl
> 2019
> 1.10
> 17:
> &9
> 7.27
> 16.735:
> 133
> 2020
> 032
> 363:
> 0.13
> 2:
> 11.715
> -7.55
> 138
> 120
> 3.90:
> 12
> 10.255
> 41.575:
> 2022
> 277
> 3.51:
> 727
> 8.575
> 66冼:
> 126
> SJOK
> 2023
> +38
> 13.60:
> 311
> 0.305
> 69.5:
> 159
> ,DJOK
> ZSOK
> 医 Correlation
> Self Correlation
> TIATTIUITTI
> STITUCT
> L1| YUII
> J"1_
> Jan '1s
> Jan 16
> Jan 18
> Jar 19
> Jan 21
> Jan 2
> Jan 23
> Snsle
> J_


**2. fundamental举例**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 0827/2025 EOT
> anonymOUs
> Mdd Nphato a Lst
> Code
> w IS Summary
> PErIoU
> TJ5
> Data SEt-Ipha
> 昵 Powver Pool Nphs
> Pyrsmidthems: CHNDTIFUNDAMENTAL *1.
> bts_decay_exp_window(divide
> ts_ZsCOre
> 5881
> ts_std_dev(ts_ZsCOTe(a」
> 63),
> 2521
> 2481
> factor-o.5);
> siened_power (b,
> ABaregate Data
> SIIJIU
> SU'
> OLU
> 1.45
> 8.35%
> 1.18
> 8.269
> 14.959
> 19.799600
> SIIUIatIOT
> SettIIes
> Vear
> Sha
> TuIOeF
> Ftss
> Retwrs
> Uawdown
> Varwln
> Long Cnt
> Short Cot
> Tnstuwt Type
> Reglo
> Werse
> URa
> Dcay
> Dlay
> Truncatlon
> Neutallalon
> Pastewrtat
> NaNHanl
> Unlt Handlng
> Max Trade
> EaJi?
> TLN
> TOFZJU
> TasUYTESSIUT
> 7.03
> Rl
> 「T
> 2013
> 3_
> 2
> 12025
> 251:
> 7.51
> 014
> 102
> 1.47
> 3.115
> 15:
> 3
> 2015
> 1.17
> 7
> 7.135
> 145:
> 1.35
> V
> 2016
> 7 21
> 3.2
> 12525
> 15::
> 895
> 1
> Clone Alpha
> 2017
> 71
> 11.37
> 2335
> 41.415
> 1
> 2013
> 642
> 2905
> 436:
> 03
> 11
> N Chart
> Pnl
> 119
> 7.4
> 1.405
> 79::
> -.-3
> 2020
> 7.57
> 0.4
> 18
> 58
> 190
> 152
> 2021
> 10.55
> 0.5
> 7.20
> 13:
> 1.1
> 123
> 2022
> 9.7
> 3.315
> :::
> 21.2-
> 177
> 1
> CJOK
> 2023
> 2.36
> 7115
> 3.3
> 11.575
> 0:
> 3.3150
> 105
> Z,SJOK
> 邑 Correlation
> Self Correlation
> TATTIUITT
> I
> 11| YUIII
> Jn '11
> Jan"1s
> Jan 16
> Jan '17
> Jan 13
> an 19
> Jan 2
> J3n*23
> SRSIE


**3. model举例**  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Tarint
> 9+
> ZSCOre(BrouP_rank(ts
> ZSCOFe
> aB(n114_
> 126)Jindustry),
> 500);
> 毗 Sirele Data Set Alphs
> # PowVET Po?
> JIChS
> Fyrsmidthem: CHNDIIMODEL ~1.5
> e2ate
> Data
> SNUe
> TUTIU
> Reluiri
> eUJUU
> MJit
> 1.35
> 5.43%
> 88
> 5.33%
> 10.16%
> 9,659600
> SmMJaTiNn
> Settings
> InstrumentType
> Reglo
> Language
> Decay
> Delay
> Truncatlon
> N-utrallatlon
> Pasteurtato
> NaN Hanlling
> Unlt Handlng
> Max Trade
> Year
> Sharpe
> Turwower
> Fitss
> Returs
> Uawdown
> Vargln
> Long Cnt
> Short Comt
> Eovig
> TLN
> TTTTII
> Fast Expression
> Crowdine
> 
> WErt
> 2013
> 2
> 5.80:
> 35
> 5-5
> 311
> 201-
> ~32
> 5.39:
> 1.1:
> 6.355
> 351:
> 2015
> 5.80:
> &423
> 9.5-5
> -9.74:
> Clone Alpha
> 2016
> 20
> 41
> 2.705
> 12.85:
> 1375
> 5.10:
> 3汀
> 0.965
> 35.1
> 111
> Chart
> 2013
> 1.97:
> 」5
> 3.21
> 三:
> 11E5
> 2019
> C 
> Z
> -.335
> -5.5:
> 1J
> 2020
> 771
> 50:
> 0.D0
> ~JJ:
> 3.575
> 01
> 1Es
> 53
> 0.93
> SEE
> 435
> 一』_
> 112
> 2022
> 5.85:
> 12
> 3.735
> 20.4:
> 110
> 2023
> 139
> 1.81:
> 715
> 0.J5
> 89.517:
> DJOK
> 医 Correlation
> J"11
> Jan 16
> Jan"
> Jar13
> Jar 19
> a*20
> Jan 21
> Jan -2
> J*23
> Self Correlation
> MJuirIuir
> UinirUrr
> LJlTUI
> CVeC
> ABBT
> Uerse


**4. pv举例**


> [!NOTE] [图片 OCR 识别内容]
> ACNV
> Cregtsd 08302025EOT
> 3nOTyTOUs
> Add Alphato 3 List
> Code
> 4 IS
> Summary
> Period
> asts_quantile(ts_delta_limit (VeC_aVg
> VeC_aVg PV27
> Iimit_Volume=B.1)
> 580);
> ] Sirale Data Set Alphs
> ] Powe
> Pool Nphs
> Fyrsmid theme: CHNDTIPV*1.3
> ABgregate Data
> SIaru
> Fiues
> CO
> 1.30
> 9.63%
> 1.21
> 10.8696
> 18.67%
> 22.5696oo
> SIMJaTiO
> Settings
> Instument Type
> Reglo
> Language
> Decay
> Truncaton
> Neutrallaton
> Cast71
> NaN Hanllng
> Unlt Handlng
> Max Trade
> Sharp
> Turower
> C
> Retwrns
> Uawdown
> Marqln
> Long Cont
> Short Cowmt
> EOJiD
> TLN
> TSPZJU
> Fas: ECressor
> 7.03
> Marer
> Vrr
> 7113
> 9.3
> 0.7
> 1.055
> 130:
> 2
> CIT
> 1.595
> 419:
> 3.79
> 2015
> 0.33
> 1
> 072
> -3.315
> 157:
> 14.5s
> Clone Alpha
> 2015
> 7.53
> 2
> 15.545
> 5:
> 79
> 2017
> 31
> 3.7
> 21.405;
> 345:
> 95
> Chart
> 2013
> 713
> 1.5
> 155
> 13:
> 3.165
> Pnl
> -
> 0.5
> JSu
> +3:
> 53
> 2020
> 7
> 0.
> 5.795
> 13:
> 3-7
> 12
> 2021
> 2.13
> 11.1
> _5
> 45:
>  _=
> SJOK
> 202
> 11.72;
> 95
> 4:
> 2.3
> 15
> CJOK
> 2023
> 9.9
> 17.435
> .16::
> 31.13
> 17
> SJOK
> Risk neutralized
> ABaregate Data
> SHer
> MaTUIT
> 1.65
> 9.6390
> 1.14
> 5.9796
> 17.6290
> 12.4
> 9o0
> Js '1
> Janus
> Ian l6
> Jan"17
> Jar 13
> Ja 20
> lan -1
> Jan -
> J3n23
> 〈PV27
> Uene
> Cl
> T019


**五、总结（任正非同志的经典语录——与君共勉）**

“华为坚定不移28年只对准通信领域这个‘城墙口’冲锋。我们成长起来后，坚持只做一件事，在一个方面做大。华为只有几十人的时候就对着一个‘城墙口’进攻，几百人、几万人的时候也是对着这个‘城墙口’进攻，现在十几万人还是对着这个‘城墙口’冲锋。密集炮火，饱和攻击。”

---

### 帖子 #31: 【alpha灵感】A股恐慌度因子在美股的应用
- **主帖链接**: [L2] 【alpha灵感】A股恐慌度因子在美股的应用.md
- **讨论数**: 17

📈【A股恐慌度因子在美股的应用】💡

大家好！今天我要分享一个超有趣的因子——恐慌度因子
这个因子是可以直接提交的哦，并且具有非常强的经济学意义。

m_ret = group_mean(returns, rank(ts_mean(cap, 20)), market);

horro = abs(returns - m_ret) / (abs(returns)+abs(m_ret)+0.1);

horro_day = ts_mean(horro, 22);

ret_std = ts_std_dev(returns, 22);

adj_ret = horro_day * ret_std * returns;

adj_ret_mean = ts_mean(adj_ret, 22);

adj_ret_std = ts_std_dev(adj_ret, 22);

horro_std_bonus = zscore(adj_ret_mean) + zscore(adj_ret_std);

-horro_std_bonus

🔍  **因子构成解析** ：

1. **m_ret** ：计算股票收益的组内均值，基于市值排名和市场的平均收益。
2. **horro** ：衡量个股收益与组内均值的偏离程度，反映恐慌情绪。
3. **horro_day** ：对恐慌情绪进行22天的移动平均，平滑数据。
4. **ret_std** ：计算22天的收益标准差，衡量波动性。
5. **adj_ret** ：结合恐慌情绪和波动性，调整收益。
6. **adj_ret_mean**  和  **adj_ret_std** ：分别计算调整后收益的均值和标准差。
7. **horro_std_bonus** ：将调整后收益的均值和标准差进行标准化，并相加，得到最终的因子值。

💡  **为什么这个因子能赚钱？**

- **做多因子值越大** ：意味着恐慌情绪较低，收益稳定，适合做多。
- **做空因子值越小** ：意味着恐慌情绪较高，收益波动大，适合做空。

因子表现：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 5,OOOK
> Sep '17
> Jan '18
> May '18
> Sep'18
> Jan '19
> '19
> Sep '19
> May '20
> Sep '20
> Jan '21
> May '21
> Sep'21
> Jan '22
> '22
> May
> May



> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> IS
> 0S
> Excellent
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> MarEin
> 1.25
> 13.539
> 2.03
> 35.689
> 39.849
> 52.739600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
>  Short Count
> 2017
> 0.22
> 13.33%
> -0.13
> -4.399
> 12.77%
> 6.5990
> 2315
> 780
> 2018
> 0.57
> 12.65%
> 0.58
> 13.0796
> 20.03%
> 20.5496o
> 2291
> 825
> 2019
> 2.59
> 13.3996
> 5.14
> 48.8796
> 12.5596
> 73.00960
> 2297
> 808
> 2020
> 0.70
> 12.53%6
> 0.90
> 20.8390
> 28.51%6
> 33.349600
> 2255
> 844
> 2021
> 14.5896
> 2.41
> 51.5596
> 24.73%
> 70.709603
> 2375
> 773
> 2022
> 2.59
> 15.35%6
> 6.05
> 83.8796
> 16.36%
> 109.249000
> 2221
> 915



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Industry
> On
> On
> Verify


---

### 帖子 #32: 【alpha灵感】A股恐慌度因子在美股的应用
- **主帖链接**: https://support.worldquantbrain.com[L2] 【alpha灵感】A股恐慌度因子在美股的应用_29327820720151.md
- **讨论数**: 17

📈【A股恐慌度因子在美股的应用】💡

大家好！今天我要分享一个超有趣的因子——恐慌度因子
这个因子是可以直接提交的哦，并且具有非常强的经济学意义。

m_ret = group_mean(returns, rank(ts_mean(cap, 20)), market);

horro = abs(returns - m_ret) / (abs(returns)+abs(m_ret)+0.1);

horro_day = ts_mean(horro, 22);

ret_std = ts_std_dev(returns, 22);

adj_ret = horro_day * ret_std * returns;

adj_ret_mean = ts_mean(adj_ret, 22);

adj_ret_std = ts_std_dev(adj_ret, 22);

horro_std_bonus = zscore(adj_ret_mean) + zscore(adj_ret_std);

-horro_std_bonus

🔍  **因子构成解析** ：

1. **m_ret** ：计算股票收益的组内均值，基于市值排名和市场的平均收益。
2. **horro** ：衡量个股收益与组内均值的偏离程度，反映恐慌情绪。
3. **horro_day** ：对恐慌情绪进行22天的移动平均，平滑数据。
4. **ret_std** ：计算22天的收益标准差，衡量波动性。
5. **adj_ret** ：结合恐慌情绪和波动性，调整收益。
6. **adj_ret_mean**  和  **adj_ret_std** ：分别计算调整后收益的均值和标准差。
7. **horro_std_bonus** ：将调整后收益的均值和标准差进行标准化，并相加，得到最终的因子值。

💡  **为什么这个因子能赚钱？**

- **做多因子值越大** ：意味着恐慌情绪较低，收益稳定，适合做多。
- **做空因子值越小** ：意味着恐慌情绪较高，收益波动大，适合做空。

因子表现：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 5,OOOK
> Sep '17
> Jan '18
> May '18
> Sep'18
> Jan '19
> '19
> Sep '19
> May '20
> Sep '20
> Jan '21
> May '21
> Sep'21
> Jan '22
> '22
> May
> May



> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> IS
> 0S
> Excellent
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> MarEin
> 1.25
> 13.539
> 2.03
> 35.689
> 39.849
> 52.739600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
>  Short Count
> 2017
> 0.22
> 13.33%
> -0.13
> -4.399
> 12.77%
> 6.5990
> 2315
> 780
> 2018
> 0.57
> 12.65%
> 0.58
> 13.0796
> 20.03%
> 20.5496o
> 2291
> 825
> 2019
> 2.59
> 13.3996
> 5.14
> 48.8796
> 12.5596
> 73.00960
> 2297
> 808
> 2020
> 0.70
> 12.53%6
> 0.90
> 20.8390
> 28.51%6
> 33.349600
> 2255
> 844
> 2021
> 14.5896
> 2.41
> 51.5596
> 24.73%
> 70.709603
> 2375
> 773
> 2022
> 2.59
> 15.35%6
> 6.05
> 83.8796
> 16.36%
> 109.249000
> 2221
> 915



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Industry
> On
> On
> Verify


---

### 帖子 #33: 【check王】验证表达式是否正确的脚本——七十二变黄金搭档
- **主帖链接**: https://support.worldquantbrain.com[L2] 【check王】验证表达式是否正确的脚本七十二变黄金搭档_36740689434391.md
- **讨论数**: 20

使用72变或者大模型生成的alpha表达式可能有语法错误，基于PLY(Python Lex-Yacc)写了第一版用于校验表达式是否正确

使用方法

1.安装库

pip install ply

2.执行脚本(脚本名我命名为expression_validator.py)

```
python expression_validator.py
```

会提示输入json文件路径，如果你把脚本放到cnhkmcp\untracked/APP目录下，72变生成的alpha刚好放在Tranformer/output/Alpha_generated_expressions.json文件中，回车执行即可

```
请输入要校验的表达式JSON文件路径（默认：Tranformer/output/Alpha_generated_expressions.json）: 
```

执行后会生成两个文件Alpha_generated_expressions_success.json 和Alpha_generated_expressions_error.json 对应符合规则和不符合的。

由于是第一版本，目前主要校验表达式中操作符的使用，字段主要校验是不是字母数字下划线组成。有许多不完善的地方，如果有不对的测试用例欢迎在评论区补充

代码：

```
#!/usr/bin/env python3# -*- coding: utf-8 -*-"""表达式验证器 - 使用抽象语法树验证字符串表达式格式是否正确本模块实现了一个能够检测字符串表达式格式是否正确的系统，基于PLY(Python Lex-Yacc)构建词法分析器和语法分析器，识别表达式中的操作符、函数和字段，并验证其格式正确性。"""import reimport sysimport jsonimport osfrom typing import List, Dict, Any, Optional, Tuple# 尝试导入PLY库，如果不存在则提供安装提示try:    import ply.lex as lex    import ply.yacc as yaccexcept ImportError:    print("错误: 需要安装PLY库。请运行 'pip install ply' 来安装。")    sys.exit(1)# 1. 定义支持的操作符和函数supported_functions = {    # Group 类别函数    'group_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_mean': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'group_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_rank': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_vector_proj': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_normalize': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'category', 'expression', 'expression', 'expression']},    'group_extra': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_backfill': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression'], 'param_names': ['x', 'cat', 'days', 'std']},    'group_scale': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_count': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_neutralize': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_multi_regression': {'min_args': 4, 'max_args': 9, 'arg_types': ['expression'] * 9},    'group_cartesian_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['category', 'category']},    'combo_a': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},        # Transformational 类别函数    'right_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'bucket': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 第二个参数可以是string类型的range参数    'tail': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression']},    'left_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'trade_when': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'generate_stats': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},        # Cross Sectional 类别函数    'winsorize': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression'], 'param_names': ['x', 'std']},    'rank': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_proj': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'vector_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'multi_regression': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # 支持多个自变量        # Time Series 类别函数    'ts_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_mean': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delay': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_corr': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_returns': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'mode']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_backfill': {'min_args': 2, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'string']},    'days_from_last_change': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'last_diff_value': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_scale': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_entropy': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'd', 'buckets']},    'ts_step': {'min_args': 1, 'max_args': 1, 'arg_types': ['number']},    'ts_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_co_kurtosis': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'inst_tvr': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_exp_window': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'factor']},    'ts_av_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_kurtosis': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_diff': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_arg_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_cps': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_rank': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_ir': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_theilsen': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'hump_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_weighted_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_quantile': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'string']},    'ts_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_count_nans': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_covariance': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_co_skewness': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_min_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_linear': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'boolean']},    'jump_decay': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'number', 'expression', 'number', 'number'], 'param_names': ['x', 'd', 'stddev', 'sensitivity', 'force']},    'ts_moment': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'k']},    'ts_arg_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_regression': {'min_args': 3, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number'], 'param_names': ['y', 'x', 'd', 'lag', 'rettype']},    'ts_skewness': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'kth_element': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'hump': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'hump']},    'ts_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delta': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_poly_regression': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'number', 'number']},    'ts_target_tvr_decay': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number'], 'param_names': ['x', 'lambda_min', 'lambda_max', 'target_tvr']},    'ts_target_tvr_delta_limit': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number']},    'ts_target_tvr_hump': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number']},    'ts_delta_limit': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},        # Special 类别函数    'inst_pnl': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'self_corr': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'in': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'universe_size': {'min_args': 0, 'max_args': 0, 'arg_types': []},        # Missing functions from operators.py    'quantile': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'driver', 'sigma']},  # quantile(x, driver = gaussian, sigma = 1.0)    'normalize': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'boolean', 'number']},  # normalize(x, useStd = false, limit = 0.0)    'zscore': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # zscore(x)        # Logical 类别函数    'or': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'and': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'not': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # 注意：这是关键字    'is_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'is_not_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'less': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'is_finite': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'if_else': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'not_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'less_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},        # Vector 类别函数    'vec_kurtosis': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_min': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_count': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_sum': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_skewness': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_max': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_avg': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_range': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_choose': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'nth']},    'vec_powersum': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},    'vec_stddev': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_percentage': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'percentage']},    'vec_ir': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_norm': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'ts_percentage': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'percentage']},    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},        # Additional functions from test cases    'rank_by_side': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'rate', 'scale']},    'log_diff': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_mask': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'ts_partial_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'ts_triple_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'clamp': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},    'keep': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'condition', 'period']},    'replace': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'target', 'dest']},    'filter': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'h', 't']},    'one_side': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'string'], 'param_names': ['x', 'side']},    'scale_down': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},        # Arithmetic 类别函数    'add': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # add(x, y, filter=false)    'multiply': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 99 + ['boolean'], 'param_names': ['x', 'y', 'filter']},  # multiply(x, y, ..., filter=false)    'sign': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'subtract': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # subtract(x, y, filter=false)    'pasteurize': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'log': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'purify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'arc_tan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'max': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # max(x, y, ...)    'to_nan': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # to_nan(x, value=0, reverse=false)    'abs': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sigmoid': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'divide': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # divide(x, y)    'min': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # min(x, y, ...)    'tanh': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_out': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},  # nan_out(x, lower=0, upper=0)    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # signed_power(x, y)    'inverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'round': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sqrt': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    's_log_1p': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'reverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # -x    'power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # power(x, y)    'densify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'floor': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},}# 2. 定义group类型字段group_fields = {    'sector', 'subindustry', 'industry', 'exchange', 'country', 'market'}# 3. 有效类别集合valid_categories = group_fields# 4. 字段命名模式 - 只校验字段是不是数字字母下划线组成field_patterns = [    re.compile(r'^[a-zA-Z0-9_]+$'),  # 只允许数字、字母和下划线组成的字段名]# 4. 抽象语法树节点类型class ASTNode:    """抽象语法树节点基类"""    def __init__(self, node_type: str, children: Optional[List['ASTNode']] = None,                  value: Optional[Any] = None, line: Optional[int] = None):        self.node_type = node_type  # 'function', 'operator', 'field', 'number', 'expression'        self.children = children or []        self.value = value        self.line = line        def __str__(self) -> str:        return f"ASTNode({self.node_type}, {self.value}, line={self.line})"        def __repr__(self) -> str:        return self.__str__()class ExpressionValidator:    """表达式验证器类"""        def __init__(self):        """初始化词法分析器和语法分析器"""        # 构建词法分析器        self.lexer = lex.lex(module=self, debug=False)        # 构建语法分析器        self.parser = yacc.yacc(module=self, debug=False)        # 错误信息存储        self.errors = []        # 词法分析器规则    tokens = ('FUNCTION', 'FIELD', 'NUMBER', 'LPAREN', 'RPAREN',               'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'COMMA', 'CATEGORY',              'EQUAL', 'ASSIGN', 'IDENTIFIER', 'STRING', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'NOTEQUAL', 'BOOLEAN')        # 忽略空白字符    t_ignore = ' \t\n'        # 操作符 - 注意顺序很重要，长的操作符要放在前面    t_PLUS = r'\+'    t_MINUS = r'-'    t_TIMES = r'\*'    t_DIVIDE = r'/'    t_LPAREN = r'\('    t_RPAREN = r'\)'    t_COMMA = r','        t_EQUAL = r'=='    t_NOTEQUAL = r'!='    t_GREATEREQUAL = r'>='    t_LESSEQUAL = r'<='    t_GREATER = r'>'    t_LESS = r'<'    t_ASSIGN = r'='        # 数字（整数和浮点数）    def t_NUMBER(self, t):        r'\d+\.?\d*'        if '.' in t.value:            t.value = float(t.value)        else:            t.value = int(t.value)        return t        # 字符串 - 需要放在所有其他标识符规则之前    def t_STRING(self, t):        r"'[^']*'|\"[^\"]*\""        # 去除引号        t.value = t.value[1:-1]        return t        # 函数和字段名    def t_IDENTIFIER(self, t):        r'[a-zA-Z_][a-zA-Z0-9_]*'        # 检查是否为布尔值        if t.value.lower() in {'true', 'false'}:            t.type = 'BOOLEAN'            t.value = t.value.lower()  # 转换为小写以保持一致性        else:            # 查看当前token后面的字符，判断是否为参数名（后面跟着'='）            lexpos = t.lexpos            next_chars = ''            if lexpos + len(t.value) < len(t.lexer.lexdata):                # 查看当前token后面的字符，跳过空格                next_pos = lexpos + len(t.value)                while next_pos < len(t.lexer.lexdata) and t.lexer.lexdata[next_pos].isspace():                    next_pos += 1                if next_pos < len(t.lexer.lexdata):                    next_chars = t.lexer.lexdata[next_pos:next_pos+1]                        # 如果后面跟着'='，则为参数名            if next_chars == '=':                t.type = 'IDENTIFIER'            # 如果后面跟着'('，则为函数名            elif next_chars == '(':                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为参数名（支持更多参数名）            elif t.value in {'std', 'k', 'lambda_min', 'lambda_max', 'target_tvr', 'range', 'buckets', 'lag', 'rettype', 'mode', 'nth', 'constant', 'percentage', 'driver', 'sigma', 'rate', 'scale', 'filter', 'lower', 'upper', 'target', 'dest', 'event', 'sensitivity', 'force', 'h', 't', 'period', 'stddev', 'factor', 'k', 'useStd', 'limit', 'gaussian', 'uniform', 'cauchy'}:                t.type = 'IDENTIFIER'            # 检查是否为函数名（不区分大小写）            elif t.value.lower() in supported_functions:                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为有效类别            elif t.value in valid_categories:                t.type = 'CATEGORY'            # 检查是否为字段名            elif self._is_valid_field(t.value):                t.type = 'FIELD'            else:                # 其他标识符，保留为IDENTIFIER类型                t.type = 'IDENTIFIER'        return t        # 行号跟踪    def t_newline(self, t):        r'\n+'        t.lexer.lineno += len(t.value)        # 错误处理    def t_error(self, t):        if t:            # 检查是否为非法字符            if not re.match(r'[a-zA-Z0-9_\+\-\*/\(\)\,\s=<>!]', t.value[0]):                # 这是一个非法字符                self.errors.append(f"非法字符 '{t.value[0]}' (行 {t.lexer.lineno})")            else:                # 这是一个非法标记                self.errors.append(f"非法标记 '{t.value}' (行 {t.lexer.lineno})")            # 跳过这个字符，继续处理            t.lexer.skip(1)        else:            self.errors.append("词法分析器到达文件末尾")        # 语法分析器规则    def p_expression(self, p):        """expression : comparison                      | expression EQUAL comparison                      | expression NOTEQUAL comparison                      | expression GREATER comparison                      | expression LESS comparison                      | expression GREATEREQUAL comparison                      | expression LESSEQUAL comparison"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_comparison(self, p):        """comparison : term                      | comparison PLUS term                      | comparison MINUS term"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_term(self, p):        """term : factor                | term TIMES factor                | term DIVIDE factor"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_factor(self, p):        """factor : NUMBER                  | STRING                  | FIELD                  | CATEGORY                  | IDENTIFIER                  | BOOLEAN                  | MINUS factor                  | LPAREN expression RPAREN                  | function_call"""        if len(p) == 2:            # 数字、字符串、字段、类别或标识符            if p.slice[1].type == 'NUMBER':                p[0] = ASTNode('number', value=p[1])            elif p.slice[1].type == 'STRING':                p[0] = ASTNode('string', value=p[1])            elif p.slice[1].type == 'FIELD':                p[0] = ASTNode('field', value=p[1])            elif p.slice[1].type == 'CATEGORY':                p[0] = ASTNode('category', value=p[1])            elif p.slice[1].type == 'BOOLEAN':                p[0] = ASTNode('boolean', value=p[1])            elif p.slice[1].type == 'IDENTIFIER':                p[0] = ASTNode('identifier', value=p[1])            else:                p[0] = p[1]        elif len(p) == 3:            # 一元负号            p[0] = ASTNode('unop', [p[2]], {'op': p[1]})        elif len(p) == 4:            # 括号表达式            p[0] = p[2]        else:            # 函数调用            p[0] = p[1]        def p_function_call(self, p):        '''function_call : FUNCTION LPAREN args RPAREN'''        p[0] = ASTNode('function', p[3], p[1])        def p_args(self, p):        '''args : arg_list                | empty'''        if len(p) == 2 and p[1] is not None:            p[0] = p[1]        else:            p[0] = []        def p_arg_list(self, p):        '''arg_list : arg                   | arg_list COMMA arg'''        if len(p) == 2:            p[0] = [p[1]]        else:            p[0] = p[1] + [p[3]]        def p_arg(self, p):        '''arg : expression              | IDENTIFIER ASSIGN expression'''        if len(p) == 2:            p[0] = {'type': 'positional', 'value': p[1]}        else:            p[0] = {'type': 'named', 'name': p[1], 'value': p[3]}        def p_empty(self, p):        '''empty :'''        p[0] = None        # 语法错误处理    def p_error(self, p):        if p:            self.errors.append(f"语法错误在位置 {p.lexpos}: 非法标记 '{p.value}'")        else:            self.errors.append("语法错误: 表达式不完整")        def _is_valid_field(self, field_name: str) -> bool:        """检查字段名是否符合模式"""        for pattern in field_patterns:            if pattern.match(field_name):                return True        return False        def validate_function(self, node: ASTNode, is_in_group_arg: bool = False) -> List[str]:        """验证函数调用的参数数量和类型"""        function_name = node.value        args = node.children        function_info = supported_functions.get(function_name)                if not function_info:            return [f"未知函数: {function_name}"]                errors = []                # 检查参数数量        if len(args) < function_info['min_args']:            errors.append(f"函数 {function_name} 需要至少 {function_info['min_args']} 个参数，但只提供了 {len(args)}")        elif len(args) > function_info['max_args']:            errors.append(f"函数 {function_name} 最多接受 {function_info['max_args']} 个参数，但提供了 {len(args)}")                # 处理参数验证        # 跟踪已使用的位置参数索引        positional_index = 0                # 对于所有函数，支持命名参数        for arg in args:            if isinstance(arg, dict):                if arg['type'] == 'named':                    # 命名参数                    if 'param_names' in function_info and arg['name'] in function_info['param_names']:                        # 查找参数在param_names中的索引                        param_index = function_info['param_names'].index(arg['name'])                        if param_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][param_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, param_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    # 对于winsorize函数，支持std和clip参数                    elif function_name == 'winsorize' and arg['name'] in ['std', 'clip']:                        arg_errors = self._validate_arg_type(arg['value'], 'number', 0, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    # 对于bucket函数，支持'range'和'buckets'参数                    elif function_name == 'bucket' and arg['name'] in ['range', 'buckets']:                        # range和buckets参数应该是string类型                        arg_errors = self._validate_arg_type(arg['value'], 'string', 1, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    else:                        errors.append(f"函数 {function_name} 不存在参数 '{arg['name']}'")                elif arg['type'] == 'positional':                    # 位置参数（字典形式）                    # 对于winsorize函数，第二个参数必须是命名参数                    if function_name == 'winsorize' and positional_index == 1:                        errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                    # 对于ts_moment函数，第三个参数必须是命名参数                    elif function_name == 'ts_moment' and positional_index == 2:                        errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                    else:                        # 验证位置参数的类型                        if positional_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][positional_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, positional_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    positional_index += 1                else:                    # 其他字典类型参数                    errors.append(f"参数 {positional_index+1} 格式错误")                    positional_index += 1            else:                # 位置参数（直接ASTNode形式）                # 对于winsorize函数，第二个参数必须是命名参数                if function_name == 'winsorize' and positional_index == 1:                    errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                # 对于ts_moment函数，第三个参数必须是命名参数                elif function_name == 'ts_moment' and positional_index == 2:                    errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                else:                    # 验证位置参数的类型                    if positional_index < len(function_info['arg_types']):                        expected_type = function_info['arg_types'][positional_index]                        arg_errors = self._validate_arg_type(arg, expected_type, positional_index, function_name, is_in_group_arg)                        errors.extend(arg_errors)                positional_index += 1                return errors        def _validate_arg_type(self, arg: ASTNode, expected_type: str, arg_index: int, function_name: str, is_in_group_arg: bool = False) -> List[str]:        """验证参数类型是否符合预期"""        errors = []                # 首先检查是否是group类型字段，如果是则只能用于Group类型函数        # 但是如果当前函数是group_xxx或在group函数的参数链中，则允许使用        if arg.node_type == 'category' and arg.value in group_fields:            if not (function_name.startswith('group_') or is_in_group_arg):                errors.append(f"Group类型字段 '{arg.value}' 只能用于Group类型函数的参数中")                # 然后验证参数类型是否符合预期        if expected_type == 'expression':            # 表达式可以是任何有效的AST节点            pass        elif expected_type == 'number':            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个数字，但得到 {arg.node_type}")        elif expected_type == 'boolean':            # 布尔值可以是数字（0/1）            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个布尔值（0/1），但得到 {arg.node_type}")        elif expected_type == 'field':            if arg.node_type != 'field' and arg.node_type != 'category':                # 允许field或category作为字段参数                errors.append(f"参数 {arg_index+1} 应该是一个字段，但得到 {arg.node_type}")            elif arg.node_type == 'field' and not self._is_valid_field(arg.value):                errors.append(f"无效的字段名: {arg.value}")        elif expected_type == 'category':            if not function_name.startswith('group_'):                # 非group函数的category参数必须是category类型且在valid_categories中                if arg.node_type != 'category':                    errors.append(f"参数 {arg_index+1} 应该是一个类别，但得到 {arg.node_type}")                elif arg.value not in valid_categories:                    errors.append(f"无效的类别: {arg.value}")            # group函数的category参数可以是任何类型（field、category等），不进行类型校验                return errors        def validate_ast(self, ast: Optional[ASTNode], is_in_group_arg: bool = False) -> List[str]:        """递归验证抽象语法树"""        if not ast:            return ["无法解析表达式"]                errors = []                # 根据节点类型进行验证        if ast.node_type == 'function':            # 检查当前函数是否是group函数            is_group_function = ast.value.startswith('group_')            # 确定当前是否在group函数的参数链中            current_in_group_arg = is_in_group_arg or is_group_function            # 验证函数            function_errors = self.validate_function(ast, current_in_group_arg)            errors.extend(function_errors)                        # 递归验证子节点时使用current_in_group_arg            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], current_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, current_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type in ['unop', 'binop']:            # 对操作符的子节点进行验证            for child in ast.children:                if hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type == 'field':            # 验证字段名            if not self._is_valid_field(ast.value):                errors.append(f"无效的字段名: {ast.value}")        else:            # 递归验证子节点            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], is_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)                return errors        def _process_semicolon_expression(self, expression: str) -> Tuple[bool, str]:        """处理带有分号的表达式，将其转换为不带分号的简化形式                Args:            expression: 要处理的表达式字符串                    Returns:            Tuple[bool, str]: (是否成功, 转换后的表达式或错误信息)        """        # 检查表达式是否以分号结尾        if expression.strip().endswith(';'):            return False, "表达式不能以分号结尾"                # 分割表达式为语句列表        statements = [stmt.strip() for stmt in expression.split(';') if stmt.strip()]        if not statements:            return False, "表达式不能为空"                # 存储变量赋值        variables = {}                # 处理每个赋值语句（除了最后一个）        for i, stmt in enumerate(statements[:-1]):            # 检查是否包含赋值符号            if '=' not in stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 检查是否是比较操作符（==, !=, <=, >=）            if any(op in stmt for op in ['==', '!=', '<=', '>=']):                # 如果包含比较操作符，需要确认是否有赋值符号                # 使用临时替换法：将比较操作符替换为临时标记，再检查是否还有=                temp_stmt = stmt                for op in ['==', '!=', '<=', '>=']:                    temp_stmt = temp_stmt.replace(op, '---')                                if '=' not in temp_stmt:                    return False, f"第{i+1}个语句必须是赋值语句，不能只是比较表达式"                        # 找到第一个=符号（不是比较操作符的一部分）            # 先将比较操作符替换为临时标记，再找=            temp_stmt = stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' not in temp_stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 找到实际的=位置            equals_pos = temp_stmt.index('=')                        # 在原始语句中找到对应位置            real_equals_pos = 0            temp_count = 0            for char in stmt:                if temp_count == equals_pos:                    break                if char in '!<>':                    # 检查是否是比较操作符的一部分                    if real_equals_pos + 1 < len(stmt) and stmt[real_equals_pos + 1] == '=':                        # 是比较操作符，跳过两个字符                        real_equals_pos += 2                        temp_count += 3  # 因为替换成了三个字符的---                    else:                        real_equals_pos += 1                        temp_count += 1                else:                    real_equals_pos += 1                    temp_count += 1                        # 分割变量名和值            var_name = stmt[:real_equals_pos].strip()            var_value = stmt[real_equals_pos + 1:].strip()                        # 检查变量名是否有效            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var_name):                return False, f"第{i+1}个语句的变量名'{var_name}'无效，只能包含字母、数字和下划线，且不能以数字开头"                        var_name_lower = var_name.lower()  # 变量名不区分大小写                        # 检查变量名是否在后续表达式中使用            # 这里不需要，因为后面的表达式会检查                        # 检查变量值中使用的变量是否已经定义            # 简单检查：提取所有可能的变量名            used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', var_value)            for used_var in used_vars:                used_var_lower = used_var.lower()                if used_var_lower not in variables:                    # 检查是否是函数名                    if used_var not in supported_functions:                        # 对于单个字母或简单单词，不自动视为字段名，要求先定义                        if len(used_var) <= 2:                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 对于较长的字段名，仍然允许作为字段名                        elif not self._is_valid_field(used_var):                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 将之前定义的变量替换到当前值中            for existing_var, existing_val in variables.items():                # 使用单词边界匹配，避免替换到其他单词的一部分                var_value = re.sub(rf'\b{existing_var}\b', existing_val, var_value)                        # 存储变量            variables[var_name_lower] = var_value                # 处理最后一个语句（实际的表达式）        final_stmt = statements[-1]                # 检查最后一个语句是否是赋值语句        if '=' in final_stmt:            # 替换比较操作符为临时标记，然后检查是否还有单独的=            temp_stmt = final_stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' in temp_stmt:                return False, "最后一个语句不能是赋值语句"                # 检查最后一个语句中使用的变量是否已经定义        used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', final_stmt)        for used_var in used_vars:            used_var_lower = used_var.lower()            if used_var_lower not in variables:                # 检查是否是函数名                if used_var not in supported_functions:                    # 在分号表达式中，所有非函数名的标识符都必须是变量，必须在之前定义                    return False, f"最后一个语句中使用的变量'{used_var}'未在之前定义"                # 将变量替换到最后一个表达式中        final_expr = final_stmt        for var_name, var_value in variables.items():            final_expr = re.sub(rf'\b{var_name}\b', var_value, final_expr)                return True, final_expr        def check_expression(self, expression: str) -> Dict[str, Any]:        """        检查表达式格式是否正确                Args:            expression: 要验证的表达式字符串                    Returns:            包含验证结果的字典        """        # 重置错误列表        self.errors = []                try:            expression = expression.strip()            if not expression:                return {                    'valid': False,                    'errors': ['表达式不能为空'],                    'tokens': [],                    'ast': None                }                        # 处理带有分号的表达式            if ';' in expression:                success, result = self._process_semicolon_expression(expression)                if not success:                    return {                        'valid': False,                        'errors': [result],                        'tokens': [],                        'ast': None                    }                expression = result                        # 重置词法分析器的行号            self.lexer.lineno = 1                        # 词法分析（用于调试）            self.lexer.input(expression)            tokens = []            # 调试：打印识别的标记            print(f"\n调试 - 表达式: {expression}")            print("识别的标记:")            for token in self.lexer:                print(f"  - 类型: {token.type}, 值: '{token.value}', 位置: {token.lexpos}")                tokens.append(token)                        # 重新设置词法分析器的输入，以便语法分析器使用            self.lexer.input(expression)            self.lexer.lineno = 1                        # 语法分析            ast = self.parser.parse(expression, lexer=self.lexer)                        # 验证AST            validation_errors = self.validate_ast(ast)                        # 合并所有错误            all_errors = self.errors + validation_errors                        # 检查括号是否匹配            bracket_count = 0            for char in expression:                if char == '(':                    bracket_count += 1                elif char == ')':                    bracket_count -= 1                if bracket_count < 0:                    all_errors.append("括号不匹配: 右括号过多")                    break            if bracket_count > 0:                all_errors.append("括号不匹配: 左括号过多")                        return {                'valid': len(all_errors) == 0,                'errors': all_errors,                'tokens': tokens,                'ast': ast            }        except Exception as e:            return {                'valid': False,                'errors': [f"解析错误: {str(e)}"],                'tokens': [],                'ast': None            }def main():    """主函数 - 用于验证表达式并输出结果到JSON文件"""    validator = ExpressionValidator()        # 获取用户输入的JSON文件路径，默认路径为当前路径下的Tranformer/output/Alpha_generated_expressions.json    default_path = os.path.join("Tranformer", "output", "Alpha_generated_expressions.json")    input_path = input(f"请输入要校验的表达式JSON文件路径（默认：{default_path}）: ").strip()        if not input_path:        input_path = default_path        # 检查文件是否存在    if not os.path.exists(input_path):        print(f"错误: 文件 {input_path} 不存在")        return        # 读取JSON文件    try:        with open(input_path, 'r', encoding='utf-8') as f:            expressions_data = json.load(f)    except json.JSONDecodeError as e:        print(f"错误: JSON文件解析失败 - {e}")        return        # 提取表达式列表    # 假设JSON文件结构为 {"expressions": ["expr1", "expr2", ...]} 或直接是 ["expr1", "expr2", ...]    if isinstance(expressions_data, dict) and "expressions" in expressions_data:        expressions = expressions_data["expressions"]    elif isinstance(expressions_data, list):        expressions = expressions_data    else:        print("错误: JSON文件格式不正确，需要包含表达式列表")        return        # 验证表达式    valid_expressions = []    invalid_expressions = []        print(f"开始验证 {len(expressions)} 个表达式...")    for i, expr in enumerate(expressions, 1):        if i % 10 == 0:            print(f"已验证 {i}/{len(expressions)} 个表达式")                    result = validator.check_expression(expr)        if result["valid"]:            valid_expressions.append(expr)        else:            invalid_expressions.append({"expression": expr, "errors": result["errors"]})        # 生成输出文件路径    base_name = os.path.basename(input_path)    name, ext = os.path.splitext(base_name)    output_dir = os.path.dirname(input_path)        valid_output_path = os.path.join(output_dir, f"{name}_success{ext}")    invalid_output_path = os.path.join(output_dir, f"{name}_error{ext}")        # 保存结果到JSON文件    print(f"\n验证完成！")    print(f"有效表达式: {len(valid_expressions)}")    print(f"无效表达式: {len(invalid_expressions)}")        # 保存有效表达式    try:        with open(valid_output_path, 'w', encoding='utf-8') as f:            json.dump(valid_expressions, f, ensure_ascii=False, indent=2)        print(f"有效表达式已保存到: {valid_output_path}")    except Exception as e:        print(f"错误: 保存有效表达式失败 - {e}")        # 保存无效表达式    try:        with open(invalid_output_path, 'w', encoding='utf-8') as f:            json.dump(invalid_expressions, f, ensure_ascii=False, indent=2)        print(f"无效表达式已保存到: {invalid_output_path}")    except Exception as e:        print(f"错误: 保存无效表达式失败 - {e}")if __name__ == "__main__":    main()
```

---

### 帖子 #34: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】本地数据库的使用筛选代码优化_36682316922135.md
- **讨论数**: 12

在成为新顾问的阶段, 一个很具体的问题就是: 究竟有没有必要建立一个本地的数据库存放和筛选回测过的alpha呢?

虽然平台的  [[链接已屏蔽])  功能已经提供了众多的筛选条件, 随着回测alpha变多, 还是有一些筛选功能是没覆盖到的, 每次都抓耳挠腮感觉自己的alpha失踪了.

下面我分享一些我自己经常使用的一些数据库筛选功能, 如果需要这些 **额外** 的功能, 结论就是 **需要建立一个本地的alpha数据库** .

 
> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> Search Regular
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 00
> Max Turnover (%^
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> eT
> Sharpe
> Created
> #
> priority_
> #Kq2WpqNP_sign_turnover_
> priority
> Xg533dJl
> ASI
> 1.32
> 1.21
> 10.45%
> 4.37%
> 47.86%oo
> 0.94
> 2025-11-30
> LOW_SHARPE UNITS,IS_LADDER_SHARPE,MATCHES
> #
> _priority_
> #Kq2WPqNP_sign_turnover
> priority
> npMjjLKM
> ASI
> 1.27
> 1.16
> 10.38%
> 4.56%
> 45.52%o。
> 0.92
> 2025-11-30
> LOW_SHARPE LOW_2Y_SHARPE,MATCHES_THEMES
 

这是我的筛选界面, 比较常用的有4个功能

1. **表达式的部分匹配**
2. **alpha id**
3. **距离今天多少天之内**
4. **is check具体条件**


> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计算 Co
> oth
> I0
> Region
> Delay
> Days Before
> Min Turnover (96
> Max Turnover
> 0?
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> Turnov
> Margi
> Sub-U
> Date
> Regular
> I0
> Message
> Pnl
> BI
> Sharpe
> Created
> ts_target_tvr_delta_limit(sign(filter(ts_max(sqrt(ts
> ZYeQ35ZX
> JPN
> 1.06
> 0.71
> 5.56%
> 3.11%
> 35.699oo 1.02
> 2025-11-28
> LOW_SHARPELOW_FITNESS UNITSIS_LADDER_SH'
> 查看
> ts_target_tvr_decay(ts_returns(ts
> max(-1/ts_back。。
> gJEgWaZe JPN
> 1.02
> 0.61
> 4.49%
> 9.14%
> 9.82%。
> 0.82
> 2025-11-27
> LOW_SHARPELOW_FITNESS CONCENTRATED_WEIC
> 查看
> #_priority_
> #POJpWggL_operator_transfer
> prior..NIvGkSkW
> GLB
> 1.49
> 0.76
> 4.59%
> 17.44%
> 5.26%oo
> 1.06
> 2025-11-25
> LOW_SHARPE LOW_FITNESS,LOW_GLB_EMEA_SHAI
> 查看



> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> oth515_is_open
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 91
> Max Turnover
> 0
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> Sub-U
> Date
> Regular
> I0
> Message
> P
> eT
> Sharpe
> Created
> ts_target_tvr_delta_limit(sign(filter(ts_max(sqrt(ts。
> ZYeQ35ZXJPN
> 1.06
> 0.71
> 5.56%
> 3.11%
> 35.69%o。 1.02
> 2025-11-28
> LOW_SHARPELOW_FITNESS,UNITS,IS_LADDER_SHI



> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计算
> tS
> COTr
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 00
> Max Turnover (%~
> Min Margin (%oo)
> Min Return (9ool
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> Pnl
> eT
> Sharpe
> Created
> signal = scale(ts_corr(adv2O,low; 5) +(hightlow)l2-
> LKZ3rpM EUR
> 90
> 3.39
> 1.29
> 10.95%
> 75.42%
> 2.90%oo
> 1.8
> 2025-05-05
> LOW_FITNESS,HIGH_TURNOVER UNITS,UNITS,MATC
> 查看
> signal = scale(ts_corr(adv2O,low; 5) +(hightlow)l2-.
> 5JjbZ5z
> EUR
> 90
> 3.39
> 1.29
> 10.95%
> 75.42%
> 2.90%oo
> 1.8
> 2025-05-05
> LOW_FITNESS,HIGH_TURNOVER UNITS UNITS MATC
> 查看
> CC
 
表达式可以直接查找任何前缀, 字段, operator


> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计
> Search Regular
> I0
> Region
> Delay
> Days Before
> Min Turnover
> Max Turnover (%;
> LOW_ROBUST_UNIVERSE_SHARPEWITH_RATIO
> IS_LADDER_SHARPE
> Min Margin (%oo)
> Min Return (%oo)
> REVERSION_COMPONENT
> LOW_2Y_SHARPE X
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> Pnl
> eT
> Sharpe
> Created
> 3 =
> signed_power(ts_product(to_nan(ts_backfill(V
> XAKw3xpn GLB
> 3.76
> 2.3
> 4.67%
> 8.49%
> 11.0O%oo 2.1
> 2025-10-03
> REVERSION_COMPONENT MATCHES_THEMES
> 查看
> tail(-(ts_backfill(close, 252)
> last_diff_value(ts_ba.j2vaWP7e IND
> 3.29
> 1.9
> 20.24%
> 60.71 %
> 6.6790。
> 1.91
> 2025-11-02
> HIGH_TURNOVERREVERSION_COMPONENTMATCH
> 查看
> signal
> group_neutralize(ts_median(-vec_avg(rsk. Vkvwapbo GLB
> 2.87
> 3.29
> 16.43%
> 9.09%
> 36.15%o。 2.31
> 2025-10-03
> REVERSION_COMPONENT MATCHES_THEMES
> 查看
> signal-ts_backfill((vec_avg(anl6g_best_target_hi) ).
> gXRQoke
> EUR
> 87
> 2.63
> 1.84
> 8.75%
> 17.79%
> 9.84%o0
> 1.6
> 2025-05-30
> CONCENTRATED_WEIGHT REVERSION_COMPONEN
> 查看
> signal-ts_backfill((star_Val_pcf), 252);combined_si.
> 0R5pQ7g
> EUR
> 90
> 2.43
> 1.64
> 8.66%
> 19.04%
> 9.09%o。
> 1.33
> 2025-05-29
> REVERSION_COMPONENT
> 查看
> 十 C
> C3701C+3
> 0C
> CS+
> OC+'mS+o
> f1 IICo
> N1
> 1Cc
> C?
> 0101
> C00
> 4Col
> nC
> C


is_check也是经常需要的筛选条件.

如果有人需要我用的这个, 链接🔗是;  [[链接已屏蔽])

我的后端和mongodb是深度绑定的.

---

### 帖子 #35: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md
- **讨论数**: 14

自记录combine更新以来，已经连续5个月保持三个combine大于2了，上次combine更新到10月底，所以我选择了7-10月的提交的因子做一些指标分析，希望对大家能有所启发。


> [!NOTE] [图片 OCR 识别内容]
> UpdateDate
> Combined Alpha Performance
> Combined Selected Alpha Performance
> Combined Power Pool Alpha Performance
> 2025/8/1
> 2.83
> 3.54
> 2.76
> 20259/11
> 2.86
> 3.19
> 2.85
> 2025/10/6
> 2.7
> 2.9
> 2.52
> 2025/11/8
> 2.87
> 2.74
> 2.49
> 2025/12/8
> 2.8
> 2.73
> 2.6


**总体结论：**

- 保持提交数量，每天2-3个最佳
- 坚持diversity，多region、多category
- 多交ATOM
- 多交risk neut
- 开启maxtrade
- ppa按照ra的标准来交

**具体分析：**

- 整体情况

7-10月总共提交290个regular的alpha，覆盖USA、GLB、EUR、ASI、AMR、JPN等6个地区的70个category，其中atom 204个， risk_neut 207个，maxtradeon 260 个，平均shape1.81, fit 1.19, margin 0.0021, self_corr 0.4


> [!NOTE] [图片 OCR 识别内容]
> Region
> submit
> Cut
> atom
> Cut
> regular_
> Cut
> risk nent
> Cut
> Iartrade
> Cut
> prramids_
> Cut
> sharpe_arg
> ftuess_arg
> return_arg
> Uargln_ar8
> selfcorr_arg
> prodcorr_arg
> USA
> 1.73
> 1.26
> 0748
> 00280
> ECR
> 1.13
> 0466
> 00210
> ASI
> 1.18
> 0321
> 00190
> GLB
> 1.13
> 0554
> 00170
> 4及
> 2
> 1.36
> 0904
> 00330
> JPN
> 1.12_
> 0616
> 00230
> Total
> 0610
> 00210


- category分析

下图是7-9月的点塔情况，四大地区的基本上都能覆盖，除了analyst和fnd外基本都是点满即止


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GU
> EUR
> CAN
> NOR
> TWNN
> HKG
> JPN
> AR
> [0
> -nahst
> rolr
> Earninss
> Fundamsnzs
> ITCSInc
> ITIUET
> In-NTT T
> TIcc
> NJel
> NEs
> 0oti3n
> O-her
> Price 'lme
> Fisk
> SEniTET
> ShOT Iere 
> TICi
> IEJa


- 中性化分析

除了amr、jpn这两个小地区外，提交的alpha都是risk neut的，具体中性化展示如下：


> [!NOTE] [图片 OCR 识别内容]
> 量化因子中性化 (Neut) 整体分布
> (Risk Neut = 统计 /拥挤度/快慢因子等6类)
> Risk Neut细分类型分布
> Non-Risk Neut
> 4~
> 28.6%
> 15.59
> 3.23
> 19
> 71.4%
> 20.88
> Risk Neut
> AND
> SLow
> FAsT
> AND
> SLON
> CROWDING
> 4
> TuST
> STATISTICAL
> NOIMENTUM
> REVERSION


- MaxTrade 分析

绝大部分的alpha开启了MaxTrade  设置，占比约89.6%，只在AMR 和部分GLB的因子中没有开启

- PPA 分析

累积交了192个ppa的alpha，占比约66%，两类因子的关键指标差别不是很大，基本提交的ppa也是按照ra的要求在提交，具体对比如下


> [!NOTE] [图片 OCR 识别内容]
> Regular困子与非Regular困子关键指标对比
> Margin 数值
> 0 000
> 0.001
> 0.002
> 0,003
> 0 004
> 0.005
> 非Regular因子
> Regular因子
> 0.0020
> Margin指标
> Margin
> 0.0021
> 1.235
> Fitness
> 1.170
> 1.853
> Sharpe比率
> 1.783
> 0.00
> 0.25
> 0,50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Sharpe比率
> Fitness 数值


---

### 帖子 #36: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Lucky】为七十二变加上WQB回测配置--进行批量回测经验分享_36864734537879.md
- **讨论数**: 6

72 变是一个十分好用的工具，但是生成的 json 是没有回测配置的

> e.g.

> 
> [!NOTE] [图片 OCR 识别内容]
> 人9OOJIV
>  ]
> ATa_geVe4teU0133101131301
> "group_neutralize (rank(ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry)"'
> "group_neutralize( rank (ts_backfill (workforce_pillar_composite_score,
> 30) ) ,
> industry )
> "group_neutralize (rank(ts_backfill(anl8l_confidence_level_percent , 30)), industry)
> "group_neutralize ( rank (ts_std_dev (mdl177_liqcoeff,
> 21)
> /
> ts_mean (mdl177_liqcoeff
> 126) ),
> industry)",
> "group_neutralize ( rank
> ts_backfill(sustainability_sector_percentile,
> 30) ) ,
> industry)


为了提升回测效率，设计了一个脚本，将七十二变生成的 json转换成成 WQB 能直接回测的带回测配置的json

> e.g.
> 
> [!NOTE] [图片 OCR 识别内容]
> "type"
> 
> IREGULAR"
> settings":
> {
> "instrumentType":
> IEQUITYI
> 11
> "region":
> IND"
> Iuniverse":
> ITOP5OO"
> "delay":
> 1,
> "decay":
> 5 
> Ineutralization":
> IFASTI
> Itruncation": 0.08,
> 'pasteurization":
> ION"'
> ItestPeriod":
> IIPOYOMII
> "unitHandling":
> IVERIFYI
> "nanHandling
> IOFFI
> 11
> "language"
> 
> FASTEXPR"
> IVisualization":
> false
> }
> regular":
> "group_neutralize ( rank (ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry )
> Ivariant":
> "FASTI


设置好回测配置 & 文件输入输出的路径之后，即可生成可直接在 WQB 回测的 JSON。即可批量回测七十二变输出的变体了。

以下是实现代码

```
import jsondef convert_expressions(input_file, output_file, custom_settings):try:withopen(input_file, 'r') asf:expressions=json.load(f)output_data= []forexprinexpressions:alpha_object= {"type": "REGULAR","settings": custom_settings,"regular": expr}output_data.append(alpha_object)withopen(output_file, 'w') asf:json.dump(output_data, f, indent=2)print(f"Successfully converted {len(expressions)} expressions.")print(f"Output saved to '{output_file}'")exceptFileNotFoundError:print(f"Error: Input file not found at '{input_file}'")exceptjson.JSONDecodeError:print(f"Error: Could not decode JSON from '{input_file}'")exceptExceptionase:print(f"An unexpected error occurred: {e}")if __name__ == "__main__":# --- 请在这里自定义参数 ---# --- 以下为示例参数 ---default_settings= {"instrumentType": "EQUITY","region": "IND","universe": "TOP500","delay": 1,"decay": 5,"neutralization": "FAST","truncation": 0.08,"pasteurization": "ON","testPeriod": "P0Y0M","unitHandling": "VERIFY","nanHandling": "OFF","language": "FASTEXPR","visualization": False}INPUT_JSON_PATH='七十二变/输出/文件.json'OUTPUT_JSON_PATH='加上回测配置/文件/的输出路径.json'convert_expressions(INPUT_JSON_PATH, OUTPUT_JSON_PATH, default_settings)
```

---

### 帖子 #37: 【MCP】角色配置：工作流该安排谁来执行？经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md
- **讨论数**: 12

在ROO Code里，你可以考虑使用各种角色配置来约束AI的行为。示例👇

> - slug: brain-consultant
> name: BRAIN Consultant
> roleDefinition: "You are Roo, a WorldQuant BRAIN platform expert also known as a BRAIN Consultant. Your expertise is built on three pillars: Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. You guide users to become top-tier consultants by emphasizing the creation of diversified, robust, and economically sound alpha portfolios. Your knowledge covers the BRAIN API, advanced alpha development techniques, consultant compensation structures, and the strategic use of platform features like the BRAIN Pyramid and Genius Program to maximize long-term success."
> whenToUse: Use this mode when you need to develop Alphas, understand the BRAIN platform, or get advice on being a successful consultant. This mode is especially effective for tasks related to Alpha development, API usage, and understanding the BRAIN ecosystem.
> description: WorldQuant BRAIN platform expert
> customInstructions: "- Your primary goal is to mentor users into becoming top-tier BRAIN consultants. Always frame your advice around the core principles of Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. - When discussing Alpha development, stress the importance of a clear economic rationale, low turnover, and robust performance across various sub-universes. Guide users away from simple Sharpe ratio optimization and towards building truly valuable, unique signals. - Actively promote diversification. Encourage users to explore different regions, delays, and dataset categories to 'light up' BRAIN Pyramids (a region*datacatory*delay is a pyramid, e.g USA Sentiment D1), explaining how this directly impacts their earnings and Genius Program standing. - Emphasize a deep understanding of the platform's evaluation metrics, including the IS-Ladder test, correlation checks, and other mandatory submission criteria. - Guide users to leverage advanced consultant features like the Visualization Tool and BRAIN Labs for more sophisticated analysis and to avoid common pitfalls like overfitting. - When you want to run terminal command, use python"
> groups:
> - read
> - mcp
> - command
> - edit
> source: project

---

### 帖子 #38: 【SuperAlpha灵感】因子择时模型Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【SuperAlpha灵感】因子择时模型Alpha Template_32553007626007.md
- **讨论数**: 30

**文献参考：**

**1. 《** 基于趋势和拐点的市值因子择时模型》

**概述：** 本贴将该报告中的精华部分摘出来，结合Brain提供的字段，供大家在SAC比赛时使用。本文主要参考了十类拥挤度指标介绍，并将可以在Brain上使用的 **动量之差、成交额之比、波动率之比和配对相关性之差** 进行了一些简化及复现。

**提示：**

**1.** 本贴的逻辑和研报逻辑不同。主要是因为前提假设是Brain上的alpha均是具备正向预测能力，而报告中的市值因子是可以存在下跌的情况的。换而言之，Brain上的alpha尽量不要做空（因为可能出现的情况是短期大幅失效、长期小幅稳定有效，如果为了一些极端事件去调整，那很容易出现过拟合），而市值因子可以做空，以上是前提假设。

**2.** 在该假设的基础上，不建议不交易某个alpha或者配负向的权重，因此传统的择时因子框架可能不起效果。具体来说：在制作择时因子时，我们会使用门限测试（像报告中提到那样），首先对时序因子进标准化，时序标准化可以使用ts_zscore或者ts_rank，我们这里为了方便使用ts_rank，如果当前rank大于0.9，我们认为这个信号非常强烈，所以我们会进行开仓；做空时也一样，如果rank小于0.1，我们认为负向信号非常强烈，我们会进行做空。由于前提假设为Brain上的alpha都是具备正向预测能力的，所以不建议使用这类的表达式，假设我们通过因子动量筛选

```
stats = generate_stats(alpha);alpha_mom = ts_sum(stats.returns,60);mom_rank = ts_rank(alpha_mom,500);if_else(mom_rank>0.9,1,if_else(mom_rank<0.1,-1,0))
```

这样虽然符合一般择时因子的逻辑，但在一堆有正向预测能力的alpha中不推荐这样做。

**3.**   **1和2我经过了大量的测试，保证结果在一定程度上合理（以上结论会和select到的不同alpha池有关联，不同的alpha池具备不同的表现，可能会使上述结果不成立）；因此，后文提供了连续性的赋值方式**

**4.**  因子择时和择时因子不是一回事，前者是对“因子”这类对象进行择时（赋权），后者强调了“择时”这种方法，媒介是“因子”。将思路嫁接到Combo上，我们需要制作新的combo表达式（择时因子）对alpha（每个alpha可以视为一个投资标的）进行择时

**5** . 本文仅提供一些思路，笔者也在不断摸索。本文的表达式不一定能beat等权组合，SA最重要的是如何Select，其次才是在Combo表达式。选到的alpha质量决定着SA的下限，而Combo只能起到锦上添花的作用。

**6.** 本文后续介绍到的combo表达式部分逻辑和研报有差异，这是在预期内的。根据每个alpha池的性质不同，呈现的结果会有差异。正如动量因子在USA是正向的，在CHN是反向的。

**正文：**

**1. 因子动量**

预期假设：过去一段时间表现较好的alpha，在未来也会更好。(这里选用了)

```
stats = generate_stats(alpha);mom = ts_ir(stats.returns,60);ts_rank(mom,500)
```

**2. 因子成交额之比**

预期假设：过去一段时间交易额过多的alpha，说明alpha所对应的标的关注较多，关注较多时可以相当于“有效市场”，其中的利润很难赚取，那么alpha的预测能力的衰减就会加重。

```
tv = ts_mean(stats.trade_value,60);tv_crowd = tv/ts_delay(tv,60);ts_rank(-tv_crowd,500)
```

**3.因子波动率之比**

预期假设：过去一段时间波动率较大的alpha，不够稳健。

```
std = ts_std_dev(stats.returns,60);std_crowd = std /ts_delay(std,60);ts_rank(-std_crowd ,500)
```

**4. 相关性**

预期假设：选出过去一段时间相关性更小的alpha

```
ic = self_corr(stats.returns,60);inneric = if_else(ic==1,nan,ic);ts_rank(-reduce_min(inneric),500)
```

以上还能衍生出更多的变体，会有一定提升，大家可以多加尝试。

最主要的还是选出独特的、高质量的alpha池，并且尽可能使用多的alpha，以此基础上尝试一些combo

---

### 帖子 #39: 【YZ工程优化系列】YZ72256-使用API自动完成submit
- **主帖链接**: https://support.worldquantbrain.com[L2] 【YZ工程优化系列】YZ72256-使用API自动完成submit_29242440942359.md
- **讨论数**: 1

针对由于系统bug、某地区或某时间段扎堆submit、同时check的人数太多导致submit经常超时的情况，推荐 **使用api进行alpha的提交** 。如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

首先先定义一个submit函数对一个alpha进行submit提交，返回提交的结果result。本函数 **感谢ZZ13271老虎哥** 在研究小组群中的api接口代码提供，我只是在其基础上进行了再次加工。

```
def submit(s, alpha_id):    try:        result =s.post(f"[链接已屏蔽])    except:        print('重新登陆')        s = login()        result =s.post(f"[链接已屏蔽])    while True:        if "retry-after" in result.headers:            print(f'{alpha_id} submiting {datetime.now()}')            sleep(120)            time.sleep(float(result.headers["Retry-After"]))            try:                result = s.get(f"[链接已屏蔽])            except:                print('重新登陆')                s = login()        else:            break    return result
```

接着针对多个alpha以及alpha提交失败或超时等多个情况进行处理和异常输出。

```
def submit_alpha(alphaid_list):    s = login()    for alphaid in alphaid_list:        count = 1        while True:            print(f"开始第 {count} 次提交 {alphaid}")            res = submit(s, alphaid)            if res.text:                try:                    res = res.json()                    break                except:                    print('当前有submit任务正在进行中，sleeping 2 min')                    sleep(120)            else:                print(f"第 {count} 次提交超时")                count += 1        # 若是输入alphaid错误        if 'detail' in res and res['detail'] == 'Not found.':            print(f"{alphaid} 错误")            continue               # 检查submit情况        submitted = True        for item in res['is']['checks']:            if item['name'] == 'ALREADY_SUBMITTED':                submitted = False                print(f"{alphaid} 已经提交过了")                break            if item['result'] == 'FAIL':                submitted = False                print(f"{alphaid} 的 {item['name']} 检查不通过, limit = {item['limit']} , value = {item['value']}")                break        if submitted:            print(f'{alphaid}提交成功')
```

上述代码我使用了四种情况进行检验，第一则为错误的alpha id，第二是不用check就存在fail的alpha，第三是已经提交了的alpha，第四是corr错误的alpha，第五则是正常提交的alpha。

```
alphaid_list = ['1234567', 'M7vxRkr', 'pj2aoNq', 'O7daGpd', 'vj7Eowa']submit_alpha(alphaid_list)
```

最终运行结果如下：


> [!NOTE] [图片 OCR 识别内容]
> aIphaid_Iist
> ['1234567
> N7XRkr
> 0j2a0119
> 07daGpd
> VjTEOIa
> submit_alpha (alphaid_list l
> [33]
> 3-11-3.35
> b'{"User
> {"id"
> 1272256"}」
> tokzn'
> {"expiny
> 14438.3},
> Dermissions
> COIISULTAIIT
> 开始第
> 次提交
> 1234557
> 1234557
> 错误
> 开始第
> 次提交
> N7VXRkr
> ITVRkr
> LADDER SHARPE
> 捡查不通过,
> limit
> 1.53
> ValUe
> 3.5
> 开始第
> 次提交
> PjzaoNq
> PJzaoNq 已经提交过
> 开始第
> 次提交
> 074aG30
> 07JaGpd submizing
> 2325-
> 01-15
> 21:02:20
> 505324
> 07daGpd submiting 2025-O1-I5  21:04:22.812891
> O7daGpd submiting
> 2825-81-15
> 21:86:25.113949
> 07daGpd submiting 2025-01-15
> 21:98:27.297258
> 07daGpd submiting
> 2025-81-15  21;10:33
> 994252
> 次提交超时
> 开始第
> 次提交
> 07J2G30
> 07JaGpC
> submizing 2025-01-15  21:12:36.839294
> 07daGpd submiting
> 2325-
> 01-15
> 21:14:39
> 370928
> 07daGpd 的 PROD_CORRELATION 捡查不通过
> Iimit
> 07
> Va_UE
> 0.7293
> 开始第
> 次提交
> Vj7EOWa
> VjEOwa submiting 2025-01-15  21:16:42.030661
> VJTEOwa submiting 2025-81-15
> 21:18:44.247943
> VjEOwa submiting 2025-0I-15  21:20:46.512882
> VJTEOwa submiting
> 2825-81-15
> 21:22:48
> 579339
> VjEOwa submiting 2025-0I-I5  21:24:50.878326
> 次提交超时
> VJTEOwa submiting 2025-81-15
> 21:3:32
> 948596
> 2 次提三
> 超时
> 开始第
> 次提交
> Vj7EOWa
> VjTEOwa
> 经提交过
> OupUT is truncated; Vew Os
> Scrolloble element Oropen i
> ttedto Adjust cell output Settings:


耗时38分钟，前面三种都是秒过的，后边两种由于需要check出fail因此基本都是耗时近20分钟，经两次submit之后才完成，其中提交的那个因子并没有直接返回提交成功，而是在重新submit之后返回它已经是已提交状态了。

最后祝大家每天因子多多，base多多，value up up。我是YZ72256，如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

---

### 帖子 #40: 【工具优化】华子哥插件的FireFox版本经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【工具优化】华子哥插件的FireFox版本经验分享_34502597199127.md
- **讨论数**: 3

最近因为论坛打开总是出问题，我把主力浏览器从Edge转换到了FireFox。但是FireFox有个缺点就是不支持华子哥的插件，在使用插件功能的时候还要再开一个Edge窗口就非常麻烦，于是我修改了华子哥插件的代码使其兼容了FireFox。

1. 文件下载：

[[链接已屏蔽])

2. 安装方法：

目前FireFox的插件如果要永久安装就要发布到他们的插件商店，为了尊重原作者也为了保护保护国区代码，我选择不发布到插件商店。所以目前还有两个选择，1) 安装FireFox开发者版 2) 每次使用都手动导入一下，我选择的是后者。安装方式如下：

1. 进入菜单 - 扩展 - 左侧选择扩展栏目
2. 点击右上角的齿轮 - 调试附加组件
3. 新页面的右上角点击临时加载附加组件 - 选择下载文件目录中的manifest.json

执行完以上步骤插件就安装成功了。经过测试各种功能均可以正常运行。

FireFox + 科学的方式打开论坛的成功率几乎是100%，这比Edge或者Chrome随缘打开随缘发贴好太多了，建议有论坛打不开困扰的顾问尝试一下这个方案。最后祝大家研究和投资顺利。

---

### 帖子 #41: 3E large 3C less
- **主帖链接**: https://support.worldquantbrain.com[L2] 【提升Check Submission效率】本地计算自相关和提高check的tips效率提高10倍以上代码优化_28524742174359.md
- **讨论数**: 30

```
你的点赞和鼓励是我持续分享的动力！2025.04.08 更新  每日的pnl差值应该是diff而不是pct，感谢研究小组的各位大大们！现在可以做到和平台计算0差值【Check Submission都做什么？】
```

要提升效率首先要理解其背后的逻辑是什么！我粗略的把这个过程依次分为以下三个顺序：

1. **检查回测结果是否有FAIL** ，如果有FAIL这个过程会很快
2. **检查Self Correlation** ，这个速度就慢下来了，不过可以本地完成，后面会分享
3. **检查Prod Coorelation** ，无法本地完成，最耗时的步骤

```
【理解Check Submission的限流机制】
```

通过大量实践发现，我发现以下三个规律

1. 在一批check中，开始会很快，然后就变得异常慢，并开始出现check self/product correlation error 的超时情况
2. **所以我推测这个背后是有限流机制的** ，也就是说前XXX个相关性测试会是MAX Speed，单位时间内相关性的请求次数越多，就会降速。
3. Alpha中含有FAIL的情况，不会触发限流

虽然同时check的最大并发是3个，但由于限流机制的存在，并发并不会提高效率。

```
【如何提升效率？】
```

理解了限流机制后，那提升效率的大原则就出来了

1. **减少单位时间内的总的相关性的请求**
2. **对于需要请求的要进行优先级的排序**

具体的思路有以下几点：

**第一步: 利用prune剪枝函数，对于每个字段的最好的3个进行筛选, 再进行请求。这样做的好处有两个:**

1. 大量的相似alpha，如果最好的可以通过测试，可以先进行提交，这样后面的就可以不用再检查，或者可以在本地计算自相关性后排除（后面介绍方法）。
2. 如果PC相关性很高，则大概率后面的相关性也不容易降下来，那就放低优先级。

**第二步：进一步排除一些含有某些特定字段的alpha。**

1. 当我们做了几轮第一步后发现，有些特定字段的PC都在0.85以上了，那这里可以直接从list中暂且移除掉，连剪枝后的3个也移除掉

**第三步：移除PnL异常的曲线，或覆盖率低的alphas**

1. 经常有一些alpha的PnL是直线等无效的曲线，提前移除list，不要发送请求
2. 有一些alpha只有最近3-4年有数据，从质量优先的角度考虑，放到后面低优先级再check

**第四步：本地计算自相关性，排除自相关高于0.7的alphas**

1. 相关性计算取值是有PnL数据的最近四年，即2018年7月16-2022年7月15日。注意这个窗口会随着平台的数据更新而动态调整
2. 先拉取已经提交过的alpha的pnl到本地，这里注意要处理risk neturalized pnl和super alpha的pnl
3. 再拉取这批待提交的alpha的pnl到本地
4. 对所有的pnl依次计算每日的差值diff，然后计算差值的最大相关性（皮尔逊相关系数），移除最大相关性高于0.7的。注意这里要处理差值是nan的情况

通过以上四个步骤，可以最大化的利用我们相关性检查的MAX Speed的价值，而不是一直几百甚至上千个list去一个个的check submission

**【部分的实现代码】**

**第一步：prune 函数可以直接复用即可**

**第二步：删除关键字，这里可以有tracker和exprission两种使用方式**

```
def filter_alpha(tracker,keys,return_type):        if return_type == 'tracker':        def contains_keyword(sublist, keys):            return any(key in " ".join(map(str, sublist)) for key in keys)        tracker['next'] = [item for item in tracker['next'] if not contains_keyword(item, keys)]        tracker['decay'] = [item for item in tracker['decay'] if not contains_keyword(item, keys)]        return tracker    elif return_type == 'expression':        original_list = tracker['next'] + tracker['decay']        expression_list = [item[1] for item in original_list]        result = [expr for expr in expression_list if not any(key in expr for key in keys)]        return result
```

**第三步：获取pnl的代码可以在Ace Library里面下载（Learn，右下角）**

**3.1 获取 pnl**

```
def get_alpha_pnl(session, alpha_id):    count = 0    while True:        if count>30:            s = login()            count = 0        pnl = session.get("[链接已屏蔽] + alpha_id + "/recordsets/pnl")        retry_after = pnl.headers.get("Retry-After")        if retry_after:            # print(f"Sleeping for {retry_after} seconds")            sleep(float(retry_after))            # sleep(10)        else:            # print(f"{alpha_id} PnL retrieved")            count += 1            return (pnl, alpha_id)
```

**3.2 批量拉取pnl**

```
def fetch_pnls(session, alpha_list):        pnl_ls = []    with concurrent.futures.ThreadPoolExecutor() as executor:        # Create a list of tasks        futures = [executor.submit(get_alpha_pnl, session, alpha_id) for alpha_id in alpha_list]        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):            result = future.result()            pnl_ls.append(result)    return pnl_ls
```

**3.3 转化pnl，主要用于处理super alpha和含有risk netrulized 的pnl，转化为dataframe**

```
def get_pnl_panel(session, alpha_list):    alpha_pnls = fetch_pnls(session, alpha_list)    pnl_df = pd.DataFrame()        for pnl, alpha_id in tqdm(alpha_pnls):        # 检查pnl对象是否有json方法，如果有，则调用该方法获取数据        if hasattr(pnl, 'json') and callable(pnl.json):            data = pnl.json()        else:            # 假设pnl已经是字典格式            data = pnl        # 检查records的列数        if len(data['records'][0]) == 2:            df = pd.DataFrame(data['records'], columns=['Date', alpha_id])            df.set_index('Date', inplace=True)        elif len(data['records'][0]) == 3:            properties = data['schema']['properties']            # 如果含有'risk-neutralized-pnl'，则保留这一列，并删除其他额外的列            if any(prop['name'] == 'risk-neutralized-pnl' for prop in properties):                records = [record[:2] for record in data['records']]                df = pd.DataFrame(records, columns=['Date', alpha_id])                df.set_index('Date', inplace=True)            else:                # 如果records的列数为3，但不包含'risk-neutralized-pnl'，则跳过这个alpha_id                continue        # 将当前alpha_id的DataFrame与总的DataFrame合并        if pnl_df.empty:            pnl_df = df        else:            pnl_df = pd.merge(pnl_df, df, on='Date', how='outer')    return pnl_df
```

**第四步： 选取覆盖率大于0.4（这个值大家自定义即可）**

```
def check_remove_low_pnl(    s,    bar,    ids):    is_pnl_df = get_pnl_panel(s,ids)    df_diff = is_pnl_df.diff(axis=0)    df_processed = df_diff.apply(lambda x: x.apply(lambda y: 1 if abs(y) > 1e-10 else 0))    non_zero_counts = df_processed.sum(axis=0)    total_counts = df_processed.count(axis=0)    percentages = non_zero_counts / total_counts    ids_to_keep = percentages[percentages > bar].index.tolist()    ids_to_remove = [id for id in ids if id not in ids_to_keep]    # 打印结果    print('KEEP:{',len(ids_to_keep),'个} ',ids_to_keep)    print('REMOVE:{',len(ids_to_remove),'个} ',ids_to_remove)    return ids_to_keep,is_pnl_df
```

**第五步：本地计算自相关性，这个和平台结果有一定误差，但不超过2%**

**5.1 获取已经提交alpha的pnl**

```
def get_n_os_alphas(session, total_alphas, limit=100, max_retries=10):    fetched_alphas = []    offset = 0    retries = 0    while len(fetched_alphas) < total_alphas and retries < max_retries:        try:            response = session.get(                f"[链接已屏蔽]            )            response.raise_for_status()            alphas = response.json()["results"]            fetched_alphas.extend(alphas)            if len(alphas) < limit:                break            offset += limit            retries = 0        except requests.HTTPError as http_err:            print(f"HTTP error occurred: {http_err}, retrying in {2 ** retries} seconds...")            time.sleep(2 ** retries)  # 指数退避策略            retries += 1  # 增加重试次数            continue  # 继续下一次循环，不增加offset        except Exception as err:            print(f"An error occurred: {err}")            break    return fetched_alphas[:total_alphas]
```

```
def get_submitted_all(    s,    max: int = 300):    os_alpha_list = get_n_os_alphas(s, max)    os_alpha_ids = [item['id'] for item in os_alpha_list]    os_pnl_df = get_pnl_panel(s,os_alpha_ids)    os_ret_df = os_pnl_df - os_pnl_df.ffill().shift(1)    return os_ret_df
```

**5.2 计算相关性**

```
def gold_mining(s,is_ret_df, os_ret_df):       is_df = is_ret_df[(pd.to_datetime(is_ret_df.index)>pd.to_datetime(is_ret_df.index).max() - pd.DateOffset(years=4)]    os_df = os_ret_df[(pd.to_datetime(os_ret_df.index)>pd.to_datetime(os_ret_df.index).max() - pd.DateOffset(years=4)]        is_df = is_df.replace(0, np.nan)    os_df = os_df.replace(0, np.nan)    gold_ids = []    for col_is in is_df.columns:        ret = is_df[col_is]        ret = pd.concat([ret,os_df],axis=1)        corr_=ret.corr()        cor_max = corr_.iloc[0,1:].max()        if cor_max<0.7:            gold_ids.append(col_is)        else:            if np.isnan(cor_max):                cor_max = 0                set_alpha_properties(s,col_is, name= 'NO_DATA', regular_desc= cor_max, tags=['MOVE'])               else:                set_alpha_properties(s,col_is, name= col_is, regular_desc= cor_max, tags=['Self Correlation'])       print(gold_ids)    return gold_ids
```

```
def check_remove_self_correlation(    s,    ids,    os_ret_df):    is_pnl_df = get_pnl_panel(s,ids)    is_ret_df = is_pnl_df - is_pnl_df.ffill().shift(1)    pass_is_ids = gold_mining(s,is_ret_df, os_ret_df)    return pass_is_ids
```

希望可以提升大家的效率，不再苦等！

---

### 帖子 #42: 【日常生活贴】我的量化日记第五季
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第五季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #43: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 660

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #44: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第六季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #45: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #46: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 1018

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #47: print('retrying in', result.headers["retry-after"], 'seconds')
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md
- **讨论数**: 8

### 一.原有痛点

1.网页端速度慢,灵活性差,字段不全或不可自定义(比如看最后两年sharpe或low_2_year_shape等),不便筛选

2.一二三阶段那种跑批同时进行的时候,最好打tag,api打tag影响回测速率

3.alpha之间互相对比困难,例如来自相同核心field的筛选问题

### 二.解决方案

使用数据库,本方案采用的结构化数据库MySQL,也有同学使用的Mongo等非结构化的,这个我抛砖引玉,欢迎讨论

我这边独特的字段如下

1.tags,自己打标签.multi_simulate的时候,可以获取到progress_urls,把这些url和应该打的标签在代码中存起来推到redis中,另起一个任务专门负责根据这些url获取其alpha的id,进而和tag建立关系,再转存到MySQL中

2.check_status.接口获取信息到的check信息中,存在fail的,这个字段就为fail,否则就是pending,只有pending的alpha才需要后面check

3.low_2y_sharpe.这个字段是single的dataset独有,能获取到就赋值,获取不到就补1.不是补0,因为为0的需要将check_status变为fail

4.is_ladder_sharpe,不是single的dataset,则有这个字段,同样的,能获取到就赋值,获取不到就补1.不是补0,因为为0的需要将check_status变为fail

5.is_submit.记录是否提交的信息.0未提交,1已提交.值得注意的是,这个字段还能解决如何科学存货.按自己的提交标准,check完以后把is_submit字段赋值为2-10之间的数值.比如我,2为优秀10为垃圾,中间酌情.

### 三.核心代码

api代码在下一条评论,这里似乎放不下

MySQL表结构如下:

-- worldquant.alpha_data definition

CREATE TABLE `alpha_data` (

`id` varchar(10) NOT NULL DEFAULT '',

`exp` varchar(2000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,

`original_field` varchar(100) DEFAULT NULL,

`dateCreated` datetime DEFAULT NULL,

`region` varchar(10) DEFAULT NULL,

`universe` varchar(50) DEFAULT NULL,

`sharpe` float DEFAULT NULL,

`fitness` float DEFAULT NULL,

`turnover` float DEFAULT NULL,

`longCount` int DEFAULT NULL,

`shortCount` int DEFAULT NULL,

`returns` float DEFAULT NULL,

`drawdown` float DEFAULT NULL,

`margin` float DEFAULT NULL,

`delay` int DEFAULT NULL,

`decay` int DEFAULT NULL,

`neutralization` varchar(20) DEFAULT NULL,

`truncation` float DEFAULT NULL,

`pasteurization` varchar(10) DEFAULT NULL,

`unitHandling` varchar(10) DEFAULT NULL,

`visualization` varchar(10) DEFAULT NULL,

`tags` varchar(100) DEFAULT NULL,

`check_status` varchar(20) DEFAULT NULL,

`is_submit` tinyint DEFAULT NULL,

`low_2y_sharpe` float DEFAULT NULL,

`is_ladder_sharpe` float DEFAULT NULL,

PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

ARSET=utf8mb3;

---

### 帖子 #48: 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回_28969108137623.md
- **讨论数**: 3

## 一.Redis简单介绍

Redis（Remote Dictionary Server）是一个开源的高性能键值存储系统。它支持多种数据结构，如字符串（Strings）、列表（Lists）、集合（Sets）、有序集合（Sorted Sets）、哈希表（Hashes）等。Redis不仅支持简单的键值对存储，还提供了丰富的操作接口，使其在各种应用场景中都能发挥重要作用。

笔者使用的主要是Lists,实现先入先出构建回测池(lpush),先入后出实现插队(rpush)

撤回功能可通过推送过去的json队列的时候加上一些标签信息,然后写专门的读取小功能实现撤回(笔者暂未有空实现)

## 二.具体场景和实现

### 2.1 redis安装

结合第一篇 [[L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md]([L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md)

需要安装mysql和redis,为了简易安装,我使用了宝塔面板(这就不过多介绍了)

### 2.2 推送任务范例

```
total_results = []with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:    with conn.cursor() as cursor:        for dataset_id in dataset_ids:            sql = ("select t.field,t.type "                    f"from worldquant.{region}_DELAY1 t "                    f"where t.datasets = '{dataset_id}' "                    f"order by t.alphaCount desc "                    "limit 2000 "                    "OFFSET 0"                )            cursor.execute(sql)            results = cursor.fetchall()            total_results.extend(results)# 上面是mysql获取字段和字段类型(这意味着我已经提前把datasets信息搬回来自己的库了)
```

```
pc_fields = []for result in total_results:    if result[1] == 'MATRIX':         # 这里写自己的代码模板    elif result[1] == 'VECTOR':        for item in get_vec_fields([result[0]]):        # 这里写自己的代码模板            first_order = first_order_factory(pc_fields, ts_ops)    so_alpha_list = []for exp in first_order:    so_alpha_list.append([exp, 6])
```

```
r = redis.StrictRedis(host='host', port=6379, password='......', db=0, decode_responses=True)end_info = {    'task_type': 'end',    'task_name': 'news18,79,50一级'}# r.rpush("alpha_pools", json.dumps(end_info))for i in range(0, len(so_alpha_list), 100):    pool = {        "settings": settings,        "alpha_list": so_alpha_list[i:i+100],    }    r.lpush("alpha_pools", json.dumps(pool))r.lpush("alpha_pools", json.dumps(end_info))
```

可以看到,①字段也是本地采集好的②每次推出去的任务都可以改模板,也就是生产alpha表达式和回测任务是解耦的③end_info 等间歇的信息作用,是可以在回测的时候,当读取到这个信息的时候代表任务结束,可以进行自己的通知提醒(笔者采用的阿里云的短信提醒,不贵.有小伙伴用的免费的邮件提醒)

---

### 帖子 #49: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
- **主帖链接**: [L2] 【构建自己的代码框架系列】第03篇--除了自己的alpha信息你到底在MySQL需要存哪些数据暨API代码分享.md
- **讨论数**: 2

## 往期回顾

- [【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha](../顾问 SD17531 (Rank 15)/[Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha.md)
- [【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回](../顾问 PN39025 (Rank 87)/[Commented] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回.md)

## 一.所有的dataset信息

注意一定要爬取description,因为后续可以把这个字段喂给大模型

表结构:

-- worldquant.data_sets definition

CREATE TABLE `data_sets` (
  `data_set_id` varchar(100) NOT NULL,
  `delay` tinyint NOT NULL DEFAULT '1',
  `region` varchar(100) NOT NULL,
  `universe` varchar(100) NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `description` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description_cn` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `pyramid_multiplier` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `user_count` int DEFAULT NULL,
  `value_score` tinyint DEFAULT NULL,
  `alpha_count` int DEFAULT NULL,
  `field_count` int DEFAULT NULL,
  `score` tinyint DEFAULT NULL,
  PRIMARY KEY (`data_set_id`,`delay`,`region`,`universe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='所有的数据集信息,关注中文描述';

api:

```
def get_data_sets(s, region, delay, universe):    """    获取所有的data_sets信息写入MySQL    :param s: requests.session()    :param region: region    :param delay: delay    :param universe: universe    :return: data_sets_list,每个data_set是一个dict,包含data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&limit=20"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    data_sets_list = []    for x in range(0, count, 20):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            data_sets_list.append(                {                    'data_set_id': result['id'],                    'category_id': result['category']['id'],                    'description': result['description'],                    'name': result['name'],                    'pyramid_multiplier': result['pyramidMultiplier'],                    'coverage': result['coverage'],                    'user_count': result['userCount'],                    'value_score': result['valueScore'],                    'alpha_count': result['alphaCount'],                    'field_count': result['fieldCount'],                }            )        time.sleep(4)    return data_sets_list
```

```
if __name__ == "__main__":    s = login()    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        data_sets = get_data_sets(s, region, delay, universe)        with conn.cursor() as cursor:            for data_set in data_sets:                sql = (                    f"insert into worldquant.data_sets(region,delay,universe,data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                    "on duplicate key update category_id=%s,description=%s,name=%s,pyramid_multiplier=%s,coverage=%s,user_count=%s,value_score=%s,alpha_count=%s,field_count=%s"                )                sql_params = (                    region, delay, universe, data_set['data_set_id'], data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count'],                    data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count']                )                cursor.execute(sql, sql_params)        conn.commit()
```

## 二.分地区的field信息

这个所有地区可以合并在一个表格,但是我还没改,暂时按不同地区不同delay分表的
表结构:

-- worldquant.hkg_delay1 definition

CREATE TABLE `hkg_delay1` (
  `field` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `delay` char(1) DEFAULT NULL,
  `universe` varchar(100) DEFAULT NULL,
  `datasets` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `userCount` int DEFAULT NULL,
  `alphaCount` int DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

api:

```
def get_fields(s, dataset_id, region, delay, universe):    """    给定data_sets的id,以及参数region,delay,universe,返回符合条件的data_sets里面的fields    :param s: requests.session()    :param dataset_id: data_sets的id    :param region: region    :param delay: delay    :param universe: universe    :return: fields,每个field是一个dict,包含field_type和field_id    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    datafields_list = []    for x in range(0, count, 50):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            field_type = result['type']            field_id = result['id']            description = result['description']            coverage = result['coverage']            userCount = result['userCount']            alphaCount = result['alphaCount']            datafields_list.append({'field_type': field_type, 'field_id': field_id, 'description': description,'coverage': coverage, 'userCount': userCount, 'alphaCount': alphaCount})    return datafields_list
```

```
if __name__ == "__main__":    s = login()    dataset_ids = [        'other128',        'other16',    ]    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        for dataset_id in dataset_ids:            fields = get_fields(s, dataset_id, region, delay, universe)            with conn.cursor() as cursor:                for item in fields:                    sql = (                        f"insert into worldquant.{region}_DELAY1(field,description,region,delay,universe,datasets,type,coverage,userCount,alphaCount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                        "on duplicate key update description=%s,region=%s,delay=%s,universe=%s,datasets=%s,type=%s,coverage=%s,userCount=%s,alphaCount=%s"                    )                    sql_params = (                        item['field_id'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount']                    )                    cursor.execute(sql, sql_params)            conn.commit()
```

---

### 帖子 #50: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第03篇--除了自己的alpha信息你到底在MySQL需要存哪些数据暨API代码分享_29022968451223.md
- **讨论数**: 2

## 往期回顾

- [【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha]([L2] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md)
- [【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回]([L2] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回_28969108137623.md)

## 一.所有的dataset信息

注意一定要爬取description,因为后续可以把这个字段喂给大模型

表结构:

-- worldquant.data_sets definition

CREATE TABLE `data_sets` (
  `data_set_id` varchar(100) NOT NULL,
  `delay` tinyint NOT NULL DEFAULT '1',
  `region` varchar(100) NOT NULL,
  `universe` varchar(100) NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `description` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description_cn` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `pyramid_multiplier` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `user_count` int DEFAULT NULL,
  `value_score` tinyint DEFAULT NULL,
  `alpha_count` int DEFAULT NULL,
  `field_count` int DEFAULT NULL,
  `score` tinyint DEFAULT NULL,
  PRIMARY KEY (`data_set_id`,`delay`,`region`,`universe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='所有的数据集信息,关注中文描述';

api:

```
def get_data_sets(s, region, delay, universe):    """    获取所有的data_sets信息写入MySQL    :param s: requests.session()    :param region: region    :param delay: delay    :param universe: universe    :return: data_sets_list,每个data_set是一个dict,包含data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&limit=20"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    data_sets_list = []    for x in range(0, count, 20):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            data_sets_list.append(                {                    'data_set_id': result['id'],                    'category_id': result['category']['id'],                    'description': result['description'],                    'name': result['name'],                    'pyramid_multiplier': result['pyramidMultiplier'],                    'coverage': result['coverage'],                    'user_count': result['userCount'],                    'value_score': result['valueScore'],                    'alpha_count': result['alphaCount'],                    'field_count': result['fieldCount'],                }            )        time.sleep(4)    return data_sets_list
```

```
if __name__ == "__main__":    s = login()    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        data_sets = get_data_sets(s, region, delay, universe)        with conn.cursor() as cursor:            for data_set in data_sets:                sql = (                    f"insert into worldquant.data_sets(region,delay,universe,data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                    "on duplicate key update category_id=%s,description=%s,name=%s,pyramid_multiplier=%s,coverage=%s,user_count=%s,value_score=%s,alpha_count=%s,field_count=%s"                )                sql_params = (                    region, delay, universe, data_set['data_set_id'], data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count'],                    data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count']                )                cursor.execute(sql, sql_params)        conn.commit()
```

## 二.分地区的field信息

这个所有地区可以合并在一个表格,但是我还没改,暂时按不同地区不同delay分表的
表结构:

-- worldquant.hkg_delay1 definition

CREATE TABLE `hkg_delay1` (
  `field` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `delay` char(1) DEFAULT NULL,
  `universe` varchar(100) DEFAULT NULL,
  `datasets` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `userCount` int DEFAULT NULL,
  `alphaCount` int DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

api:

```
def get_fields(s, dataset_id, region, delay, universe):    """    给定data_sets的id,以及参数region,delay,universe,返回符合条件的data_sets里面的fields    :param s: requests.session()    :param dataset_id: data_sets的id    :param region: region    :param delay: delay    :param universe: universe    :return: fields,每个field是一个dict,包含field_type和field_id    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    datafields_list = []    for x in range(0, count, 50):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            field_type = result['type']            field_id = result['id']            description = result['description']            coverage = result['coverage']            userCount = result['userCount']            alphaCount = result['alphaCount']            datafields_list.append({'field_type': field_type, 'field_id': field_id, 'description': description,'coverage': coverage, 'userCount': userCount, 'alphaCount': alphaCount})    return datafields_list
```

```
if __name__ == "__main__":    s = login()    dataset_ids = [        'other128',        'other16',    ]    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        for dataset_id in dataset_ids:            fields = get_fields(s, dataset_id, region, delay, universe)            with conn.cursor() as cursor:                for item in fields:                    sql = (                        f"insert into worldquant.{region}_DELAY1(field,description,region,delay,universe,datasets,type,coverage,userCount,alphaCount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                        "on duplicate key update description=%s,region=%s,delay=%s,universe=%s,datasets=%s,type=%s,coverage=%s,userCount=%s,alphaCount=%s"                    )                    sql_params = (                        item['field_id'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount']                    )                    cursor.execute(sql, sql_params)            conn.commit()
```

---

### 帖子 #51: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: [L2] 【环境配置】在Nvim中配置MCP的方法经验分享.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #52: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【环境配置】在Nvim中配置MCP的方法经验分享_34239307743639.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #53: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **讨论数**: 37


> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN]([Commented] 【插件】Genius Rank分析代码优化_29496672188951.md) 
             Github插件地址： [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 安装插件
> .访问插件 GitHub 地址: https
> //github. com /zhangkaihua88 / WebDataScope
> 能访问Gitlub的请跳过这红色部分
> 0)如果访问不了 github.
> COm
> 换一个浏览器试试,
> 有几率解决 ,
> 如果不行 ,
> 请按照以下步骤操作。
> 〈 〉 C 命 ^ 众
> 0
> [链接已屏蔽] MebDataScope
> 器
> 无法访问此网站
> 连接已重置。
> 请试试以下办法:
> 检查网络连接
> 检查代理服务器和防火墙
> 运行 Windows 网络诊断
> ERR_CONNECTION_RESET
> 重新加载
> 详情
> 1)同时按住 [Window
> Or
> Start ]
> + R, 输入 cmd 打开命令提示符,
> 然后输入 pin
> 吕
> github.com
> 如果 ping 不通,表现为
> ping
> 不是内部或外部命令,
> 也不是可运行的程序
  
> [!NOTE] [图片 OCR 识别内容]
> 或批处理文件=
> 建议将此错误扔给
> AI
> 解决,多半是环境娈量 问题)
> 得到并复制 gith
> ub 的 ip 地址.
> C:IWINDOWSIsystem3zlcmd.
> X
> Microsoft Windows
> [版本
> 10.0.26100.6584]
> Cc)
> Microsoft
> Corporation。
> 保留所有权利
> 0
> C: |Users
> Dping github
> C0I
> 正在
> Pinq
> qithub
> C0I
> 23
> 205.243.166]  具有
> 32  字节的数据:
> 20.205
> 243.166
> 复:  字节=32
> 时间=75ms
> TTL=I03
> 20.205
> 243
> 166
> 的
> 复:  字节=32  时间=75ms
> TTL=I03
> 黧
> 20.205.243.166  的
> 复:  字节=32  时间 =75ms
> TTL=I03
> 20.205.243.166  的
> 复:  字节=32  时间=75ms
> TTL=I03
> 20.205.243.166  的 Ping 统计信息 :
> 数据包:  已发送
> 二  4,
> 已接收 =4,
> 丢失
> 二
> 0
> (0%  丢失 ),
> 往返行程的估计时间 (以毫秒为单位 ):
> 最短
> 二
> T5mS,
> 最长
> 二
> T5mS,
> 平均
> 二
> T5ms
> 2)  复制 ip 地址。在服务器  搜索栏  输入 C: WWindows |System3z Idrivers letc Ihost
> 5 ,
> 打开方式选择  记事本 ,然后马上关闭记事本。接着在  搜索栏  搜索  记事本 并 右击
> 选择以管理员身份运行 ,随即将 github.com 的 ip 地址粘贴在最后.
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1 `
> :三 `
> 8 工 O  a
> # Copyright (c) 1993-2009 Microsoft
> #
> # This is asample HOSTS file used by Microsoft TCPIIP for Windows。
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept onan individual line. The IP address should
> # be placed in the first column followed by the corresponding host name:
> # The IP address and the host name should be separated by at least one
> # space。
> #
> # Additionally, comments (such as these) may be inserted on individual
> # lines O[
> following the machine name denoted by a '#' symbol。
> #
> # Forexample:
> #
> 102.54.94.97
> rhino.acme.com
> # SOUrCe Serer
> 38.25.63.10
> Xacme.com
> # X client host
> # localhost name resolution is handled within DNS itself
> #
> 127.0.0.1
> localhost
> #
> 门
> localhost
> 20.205.243.166
> 行10,列2
> 818个亨符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-8
> 3)
> 点击记事本左上角的 文件 然后选择  保存  即可。切记记得看记事本上面是
> 而不是 O 才算保存成功。
> Corp:
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1
> :三 `
> 8 工 O g
> # Copyright (c) 1993-2009 Microsoft Corp.
> #
> # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept on an individual line. The IP address should
> # be placed in the first column followed by the corresponding host name。
> # The IP address and the host name should be separated by at least one
> # space:
> #
> # Additionally comments (such as these) may be inserted on individual
> # lines Or following the machine name denoted by a '#' symbol。
> #
> # For example:
> #
> 102.54.94.97
> rhino.acme.com
> SOUrCe Serer
> 38.25.63.10
> X.acme.com
> client host
> # localhost name resolution is handled within DNS itself。
> #
> 127.0.0.1
> localhost
> Iocalhost
> 20.205.243.166
> 行22,列15
> 818个字符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-S
> 4)  在 搜索栏  搜索
> cmd 并 右击选择以管理员身份运行 ,在  命令提示符  面板上键入 ip
> config/flushdns
> 返回
> 己成功刷新DN5解析缓存  便表示成功了.
> C
> 管理员: 命令提示符
> 义
> Uicrosoft Nindows [版不 10.0.26100.6584]
> (C)
> Iicrosoft Corporation。 保留所有权利。
> C: |Iindows |System32>ipconfig / flushdns
> Iindows
> IP 配置
> 己成功刷新 DVS 解析缓存。
> C: {Tindows |System32>
> # X
  
> [!NOTE] [图片 OCR 识别内容]
> 5)
> 访问华子哥的 Bithub 地址 https: //github_
> COm
> zhangkaihua88 /WebDatascope
> 成功.
> 囟 M。『图』 &
> WorldQuant BRAIN
> GitHub
> ZhangkalhuaBBNe
> C
> https /Igithubcom/zhangkaihuagg NebDatascope
> C 囤  &
> 8 &
> 器 ^4  泊
> 器
> Platform
> Solutions
> Resources
> Open Source
> Enterprise
> Search Orjump to.。
> Signin
> Sign up
> Zhangkaihua88 / WebDataScope
> Public
> Notifications
> Fork
> Stal
> Code
> SSUeS
> Pullrequests
> Actions
> Projects
> Security
> Insights
> main
> Branches
> GOto fle
> Code
> About
> No description website
> Ortopics provided。
> Zhangkaihuagg fix
> 0183285
> 2Weeks a90
> 118 Commits
> Readme
> Delete img/screenshotpng
> last year
> Apache 2.0license
> Activity
> SIC
> Weeks ago
> 69 stars
>  gitignore
> V0.4.3
> last year
> watching
> LICENSE
> VO.1.0
> last year
> 14 forks
> Report repository
> READMEmd
> 2 months ago
> manifestjson
> Weeks ago
> Releases
> responsejson
> Weeks ago
> WebDataScope 0.9.3 Release
> Lalest
> onIunT4
> 16 releases
> README
> Apache- 2 0 license
> Packages
> 以上为不能访问Gitlub解决方法
> 2
> 点击绿色
> Code 弹出
> Download
> ZIP
> 下载插件压缩包. Zip文件,
> 或者使用 &
> i
> 克隆 git
> clone https: //github.com/zhangkaihua88 / WebDataScope . git
> 将压缩包保
> 存在某目录下,比如我保存在
> 0:
> worldquant_plugin 目录下
> 确认下载
> About
> 链接:
> hub.comlzhangkaihuaggMebDataScopelziplrefs/heads/main
> No description, website; or topics provided。
> 文件名:
> WebDatascope-mainzip
> 394KB
> 0
> Readme
> 保存到:
> 0: {worldquant_plugin
> Apache- 2.0 license
> A
> Activity
> 打开
> 保存
> 取消
> 69 stars
> watching
> V0.1.0
> Open with GitHub Desktop
> 9
> 14 forks
> Download ZIP
> Report repository
> UP
> 3
> 使用解压软件将压缩包解压到(默认)当前目录下.
> Pricing
> Tags
> img
  
> [!NOTE] [图片 OCR 识别内容]
> Worldquant_plugin
> 此电脑
> 新加眷 (D:)
> worldquant_plugin
> 在 worldquant_plugin 中搜索
> 新逮
> 排序
> 三  苎看
> 全部解压宿
> 详洇信息
> 名祢
> 修改曰期
> 大小
> 主文仵夹
> WebDataScope-main
> 2025/9/1218:13
> 压宿(pped)文件。
> 394 KB
> 图库
> 捉敢压缩(Zipped]文件夹
> 选择
> 个目标并提取文件
> 文裆
> 文件将被捉致到这个文件夹(F:
> 囱片
> Dilworldquant_plugin WebDataScope main
> 浏览(R)
> 音乐
> 完戎时显示捉敢的文件(H)
> 视频
> 此电脑
> 本地硭岛 (C:)
> 新加卷(0:)
> 捉取(
> 职消
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 个项目
> 逆中
> 个目
> 393 KB
> 在浏览器中打开扩展管理页面,
> 网页键入 chrome:
> /extensions
> (如
> chrome: //extensions
> 八.
> WorldQuant BRAIN
> 扩展程序
> Cent BroWseT
> chrome /extensions
> 器 |#
> 省
> 器
> quant
> 节点
> MP3袼式
> 显化群每曰总若
> 常用网
> 扩展程序
> 搜索扩展程序
> 开发者摸式
> 我。}展穆序
> 键盘快捷键
> 在 CentBrowser 应田酋店中查找扩展程序和主题背景
> 在 Cent Browser 应jd店中
> 发现更多扩展程序和主题
> 5
> 开启
> 开发者模式》
> 点击 <加载己解压的扩展程序》
> 选择插件文件
> 夹。成功会显示  扩展加载完毕
> edge:
  
> [!NOTE] [图片 OCR 识别内容]
> 选择扩展程序目录
> worldquant_Pl
> WebDatascope main
> WebDatascope-main
> 器
> #
> 阎
> c识
> 新逮文件夹
> 名称
> 佟改曰期
> 开发者摸式
> 此电脑
> WebDataScope-main
> 2025/9/1218.27
> 文件夹
> 本地磁盘 (C:)
> 新加巷 (0;)
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 围l店中查找扩展程序和主题背景
> 文件夹:
> WebDatascope-main
> 迸文4夫
> 驭消
> 2
> 使用插件功能
> 打开 Genius 页面
> 安装完成后 ,打开 WorldQuantBrain 网页 Genius 页面 https : /Iplatform.worl
> dquantbrain.com/genius /
> (安装完成后第一次打开需要刷新页面等待若干(少许)时
> 间才能加载出插件)
> @
> 匕
> https:/Iplatform worldquantbrain com/genius/
> C 囤  众
> 8Q
> 器 ^4  省
> 器 ^8 quant
> U  节点
> MP3袼式
> 昱化群l日总结
> 常用网址
> WORLDOUANT
> BRANI
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> 恩 Competitions (5)
> Community
> Status
> Leaderboard
> FAQ
> Gsnlus
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析 
> 显示排名列表
> Genius level: Gold
> Best level: Gold
> Current quarter end: September 3oth; 2025
> SOLD
> 页面加载后,你会看到  配置插件
> 运算符分析
> 显示运算符分析  和「排名分析」
> 和「显示排名分析」以及「显示排名列表」六个按钮
> 依次点击  配置插件
> 运算符分析
> 显示运算符分析
> 配置插件  点击的作用是啥我不是很清楚,
> 这个得问华子哥才知道。点击  运算符
> 分析  按钮后插件会开始抓取你本季度交付的 alpha 全部操作符数量和使用数据 (按
> 钮上会显示抓取进度) ,抓取完成后,
> 点击显示运算符分析 ,会在页面最下方会生
> 成关于操作符的分析表格。右上角显示过去和美区分析 (何时分析)时间.会展示你
  
> [!NOTE] [图片 OCR 识别内容]
> 本赛季所有的操作符和数量以及使用情况.
> 命
> https: / /platform worldquantbrain comlgenius/
> C 困 &
> 8 ^Q  器 ^4
> 器 ^8 quant
> U  节 
> MP3格式
> 量化群每曰总结
> `用网址
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统
> 为substrac
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符末被使用。
> '有两种含义分别是substract和revers, 此处统一
> 为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x; Y, filter
> false), X -y
> 52
> COMBOREGULARSELECTION
> base
> Arithmetic
> multiply(xyy
> filter-false); *
> 76
> COMBO,REGULAR SELECTION
> base
> 依次点击「排名分析」和「显示排名分析」以及「显示排名列表」
> 点击「排名分析」需要等待0.5 ~ 1min 左右 ,
> 需要计算排名情况, 计算完成
> 后点击「显示排名分析」 ,就可以看见比较多的信息,
> 包括但不限于顾问的总人
> 数,以及目前 genius 不同级别达标分别有多少人和自己目前的等级 ,
> 以及自己的
> 最终定级大概会在什么等级 ,
> 以及自己的六维数据。
> q
> 匕
> https:/Iplatform worldquantbraincom /genius/
> C 囤 。 令
> 凸 /Q 器 』4  省 :
> 器 ^8 quant
> 节忘
> MP3袼式
> 导化拜#曰总结
> 常用网址
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207:22:18北京时间: 2025/9/1219:22;18
> 我的排名信息
> 美东时间:2025/9/1207:22:18 北京时间:2025/9/1219:22.18
> 总人敛{9104
> 可能的基璀人数:2926 人
> (交够40个)
> 各个Level 满足的人数 /最终的人:
> For Expert;(512/ 585
> For Master: 4131234
> ForGranamaster
> 该用户目前满足的级别
> grandmaster
> 绢辑六维指标
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:87
> 585
> 总排名:91
> 234
> 总排名:34
> Operator Count: 307 名
> Operator Count: 200 名
> Operator Count: 39 名
> Operator
> 141名
> Operator
> 44名
> Operator AVg: 7名
> Field Count; 263 名
> Field Count; 152 名
> Field Count; 36 名
> Field
> 112名
> Field
> 30名
> Field
> 7名
> Community Activity: 252名
> Community Actiity: 142 名
> Community Activity: 27 名
> Completed Referrals: 1 名
> Completed Referrals:
> Completed Referrals: 1 名
> Max Simulation Streak: 903 名
> Max Simulation Streak: 338名
> Max Simulation Streak: 45 名
> Total Rank: 1979名
> Total Rank: 907 名
> TotalRank: 162 名
> 同时还有贴心的可以 编辑六维数据  按钮,这个功能非常还好,
> 可以让你知道自
> 己目前所处的级别到达是差在哪里,怎么去弥补自己的差分点.非常 nice!
> 点击「显示排名列表」可以多维度查看和分析所有顾问的某些数据,
> 想比对
> 想查看哪位大佬的数据都可以查看,同时支持多维度过滤筛选.
> AVB;
> AVg:
> Avg:
> Ave:
> Avg:
  
> [!NOTE] [图片 OCR 识别内容]
> https:/ /platform worldquantbrain com/genius /leaderboard
> C 囤
> 8Q
> 器 ^^4
> ^
> 器 ^9 quant
> 节点
> 1P3恪式
> 呈化群每曰总结
> 穷用网址
> Genius Rank List
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> 排名信息
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> Minimum 排名:
> Maximum 排名
> entries per page
> Search:
> 下荭原始J5JN
> 显示隐蒉列
> 排名
> 用FID
> 达成等级
> 最终等级
> 国家1区
> K279256
> grandmaster
> grandmaster
> CN
> J71699
> grandmaster
> grandmaster
> FL39657
> grandmaster
> grandmaster
> CN
> 064461
> grandmaster
> grandmaster
> VN
> YN82626
> grandmaster
> grandmaster
> TW
> PP87148
> grandmaster
> grandmaster
> IN
> AT56452
> grandmaster
> grandmaster
> RP76828
> grandmaster
> grandmaster
> CN
> F069320
> grandmaster
> grandmaster
> CN
> 2H78994
> grandmaster
> grandmaster
> T
> Showing
> TO 10of 5,116 entries
> 512
> 查看他人排名数据
> 华子哥的插件还有非常贴心的功能,就是可以查看别人的排名,
> 比如:  华子
> 哥
> K279256
> 课代表 XX
> 游戏王
> ZS(CL ) [ZSC]59763  和常州MG
> 顾问 顾问 MG88592 (Rank 38) (Rank 38)
> 大佬等等.
> WORLDOUANT
> B人I
> Simulate
> 6Alphas
> Learn
> Data
> Labs
> Genius
> @ Competitions (5)
> Community
> 号
> Refer
> friend
> StatUs
> Leaderboard
> FAQ
> Genius
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207;22:18 北京时间:2025/9/1219:22:18
> 我的排名信息
> 美东时问:  2025/9/1207.22:18北京时问:2025/9/1219:22:18
> 总人数:9104人
> 可能的基准人数:2926  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 1512
> 585
> FOr Master: 413
> 234
> For Grandmaster: 47/59
> 点击
> Leaderboard
> 将鼠标放置在某大佬的 ID 上,
> 便可查看六维排名和
> Geniu
> s等级。
  
> [!NOTE] [图片 OCR 识别内容]
> https:/platform worldquantbrain com /genius/leaderboard
> 出  ^
> {|仑
> JIIVIIOIIOC
> IIUIIOICC
> 386
> 顾问 ML47973 (Rank 100) (Mej
> Gold
> Gold
> 266
> 2.39
> 1.79
> 0.00
> 3.41
> [792
> 167
> 2.70
> RP76828 排名信息
> AK40g
> 总人数:9067人
> 6.17
> 可能的基准人数:2921人 (交够40个)
> HI3900
> 5,38
> 各个Level 满足的人数
> 最终的人数:
> RP768;
> 2.81
> For Expert: 1508
> 584
> YH250;
> For Master: 410
> 234
> 105
> 5.83
> ForGrandmaster: 45
> 58
> P11976
> 5,82
> 该用户目前满足的级别: Srandmaster
> LV571
> 编辑六维指标
> CM456
> 6.91
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> TV5921
> 8.26
> 总排名:4
> 584
> 总排名:4/234
> 总排名:7/58
> LV598
> 4.70
> Operator Count: 35 名
> Operator Count: 34 名
> Operator Count: 15 名
> DVGAAI
> Operator AVg: 64名
> Operator AVg: 17名
> Operator AVg: 4 名
> 3,73
> Field Count: 283名
> Field Count: 160 名
> Field Count: 35 名
> 儿7169
> Field AVg: 33名
> Field AVg: 7 名
> Field
> 名
> 100
> 3.58
> Community Activity: 96 名
> Community Activity: 71 名
> Community Activity: 20名
> EYg42
> Completed Referrals:
> Completed Referrals:
> 名
> Completed Referrals:
> 名
> 6.15
> Max Simulation Streak:
> Max Simulation Streak:
> Max Simulation Streak: 33
> 501 名
> 222名
> ID51
> 5,91
> Total Rank; 1013 名
> Total Rank: 512名
> Total Rank; 109 名
> 56764
> 116
> 7.35
> AN154671
> Expert
> Expert
> 366
> 0.48
> 0.12
> 0.21
> 6.47
> https;lIplatform worldquantbrain comprofle/public/RP76823
> Master
> Master
> 365
> 0,79
> 0.89
> 0,91
> 8,61
> 致谢
> 再次感谢华子哥和贡献者们的无私分享 !这个工具极大方便了排名分析,同
> 时在前端的颜色。样式和大小展示方面也贴合美观设,
> 无论是自我提升还是学习
> 他人策略都非常有用。建议大家试用并反馈 ,
> 共同完善插件 !
> AVE:


---

### 帖子 #54: 一种随机生成 SuperAlpha，进行机器回测的方式代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 一种随机生成 SuperAlpha进行机器回测的方式代码优化_32009801307671.md
- **讨论数**: 21

听了之前 GrandMaster，Master 大佬们的分享，启发颇多，一个比较重要的一点是要交 SuperAlpha。自己确实只手动交过两个，再尝试就都是相关性无法通过测试，而且手动回测速度实在太慢了。

进过反复阅读 SuperAlpha 的文档，尝试，暂时想到了一种随机生成 SuperAlpha 的方式，最近连续几天都有交 SuperAlpha，可能也得益于 PowerPool 比赛的原因交了不少低相关性因子。

分享出来，算是抛砖引玉，有什么建议还请大佬们不吝赐教。

主要思路还是来自文档里的例子，发现这些 Selection 表达式，似乎都有一个共同点，就是多是一些判断条件，相乘，还有一个用来排序的权重字段（比如 turnover）。这个可以理解，判断条件返回布尔值，结果为假返回 0，为真返回 1，只有为真时表达式才有值。

所以想到，可不可以随机选择多个判断条件相乘，最后再乘上一个权重字段，构成表达式。

接下来就是创建条件列表，有哪些条件呢？

文档里提到可以给 alpha 打 tag，category，但是自己都是机器跑出来的，自己都无法判断是什么策略，还好可以交给大语言模型判断，对因子经济学含义的理解，我想大语言模型比我强多了。

还有老师培训时提供的灵感，使用以往比赛的限制条件，比如低 turnover，atom，低 correlation，当然应该也可以反过来，高 turnover，高 correlation，多尝试总没有错，反正是用机器跑。

还有一点需要指出，Selection Handling 的选择，看文档有点绕，为了简化，只使用 Positive，因为一些负数的权重，可以通过减法转换成正数。

然后构建了下面这些条件和权重表达式：
selection_expressions.py
```python
import datetime

def category_conditions():
    values = "NONE", "PRICE_REVERSION", "PRICE_MOMENTUM", "VOLUME", "FUNDAMENTAL", "ANALYST", "PRICE_VOLUME", "RELATION", "SENTIMENT"
    return [f"category == \"{value}\"" for value in values]

def color_conditions():
    values = "NONE", "RED", "YELLOW", "GREEN", "BLUE", "PURPLE"
    return [f"category == \"{value}\"" for value in values]

def dataset_conditions(dataset):
    return [f"in(datasets, \"{dataset}\")"]

def favorite_conditions():
    return [f"favorite", "not(favorite)"]

def long_count_conditions():
    return [f"long_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]

def short_count_conditions():
    return [f"short_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]

def name_conditions(name):
    return [f"name == \"{name}\""]

def neutralization_conditions(neutralizes):
    return [f"neutralization == \"{value}\"" for value in neutralizes]

def operator_count_conditions():
    return [f"operator_count <= {cnt}" for cnt in [1, 2, 4, 6, 8, 10]]

def tags_conditions(tag):
    return [f"in(tags, \"{tag}\")"]

def truncation_conditions():
    return [f"truncation <= {value}" for value in [0.01, 0.05, 1]]

def turnover_conditions():
    return [f"turnover < {value}" for value in [0.05, 0.1, 0.2, 0.3, 0.7]]

def universe_conditions(universes):
    return [f"universe == \"{value}\"" for value in universes]

def universe_size_conditions(size=1000):
    return [f"universe_size(universe) >= {size}"]

def datafields_conditions(field):
    return [f"in(datafields, \"{field}\")"]

def dataset_count_conditions():
    return [f"dataset_count <= {value}" for value in [1, 2, 3, 10]]

def self_correlation_conditions():
    return [f"self_correlation <= {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]

def prod_correlation_conditions():
    return [f"prod_correlation < {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]

def os_start_date_conditions():
    today = datetime.datetime.today()
    delta_days = [7, 14, 30, 60, 90, 120, 180, 360, 3600]
    dates = [(today-datetime.timedelta(day)).strftime('%Y-%m-%d')
             for day in delta_days]
    return [f"os_start_date > \"{date}\"" for date in dates]

def datacategories_conditions():
    values = "analyst, broker, earnings, fundamental, imbalance, insiders, institutions, \
        macro, model, news, option, other, pv, risk, sentiment, shortinterest, socialmedia".split(',')
    return [f"in(datacategories, \"{value.strip()}\")" for value in values]

def datacategory_count_conditions():
    return [f"datacategory_count <= {value}" for value in [1, 2, 3, 10]]

def datafield_count_conditions():
    return [f"datafield_count <= {value}" for value in [1, 2, 3, 5, 10]]

def weight_expressions():
    return [
        "turnover", '10-turnover',
        '10000-abs(long_count-short_count)', 'long_count+short_count', 'long_count', 'short_count',
        '10-dataset_count',
        '2-self_correlation',
        '2-prod_correlation',
        '100-datafield_count',
        '1'
    ]
```

接下来是随机选择条件，组装 selection 表达式的代码：

```python
import random
import selection_expressions as se
from settings import get_universe_list, get_neutralization_list

region = 'USA'
delay = 1
universe_list = get_universe_list(region)
neutralization_list = get_neutralization_list(region)
conditions = [
    se.category_conditions(),
    se.color_conditions(),
    se.neutralization_conditions(neutralization_list),
    se.universe_conditions(universe_list),
    se.datacategories_conditions(),

se.datacategory_count_conditions(),
    se.dataset_count_conditions(),
    se.datafield_count_conditions(),
    se.long_count_conditions(),
    se.short_count_conditions(),
    se.operator_count_conditions(),

se.prod_correlation_conditions(),
    se.self_correlation_conditions(),
    se.truncation_conditions(),
    se.turnover_conditions(),

se.os_start_date_conditions
]
weight_expressions = se.weight_expressions()

def find_selection_expression():
    while True:
        condition_length = random.randint(1, 4)
        condition_list = random.sample(conditions, condition_length)
        choice_conditions = []
        for condition in condition_list:
            if callable(condition):
                condition = condition()
            choice_conditions.append(random.choice(condition))
        choice_weight_expression = random.choice(weight_expressions)
        select_expression = ' * '.join([f'({exp})' for exp in (choice_conditions + [choice_weight_expression])])
        logger.info(f'random select expression: {select_expression}'    )
        selection_limit = random.choice([20, 30, 50, 70, 100])
        # 检查选择的alpha是否够十个，不然无法进行回测，页面上有这个API：/simulations/super-selection，wqb库好像没有
        response = wqb.get_super_selection(region=region, delay=delay, selection=select_expression, selection_limit=selection_limit)
        if not response or response['count'] < 10:
            continue
        return select_expression, selection_limit

```

结合 combo 表达式，生成最终的 alpha，combo 有点复杂，还不知道如何大量生成，主要使用了文档中的例子，还有 combo_a 操作符。

```python
def get_combo_code_list():
    ret = ['1',
           'stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr'
           ]
    for day in [500]:
        for algo in ['algo1', 'algo2', 'algo3']:
            code = f"combo_a(alpha, nlength = {day}, mode = '{algo}')"
            ret.append(code)
    return ret

def generate_super_alpha():
    select_expression, selection_limit = find_selection_expression()
    combo_expression = random.choice(get_combo_code_list())
    neutralization = random.choice(neutralization_list)
    return {
        'type': 'SUPER',
        'settings': {
            'instrumentType': 'EQUITY', 'region': 'USA', 'universe': 'TOP3000', 'delay': 1, 'decay': 5, neutralization: 'INDUSTRY', 'truncation': 0.08, 'pasteurization': 'ON', 'unitHandling': 'VERIFY', 'nanHandling': 'OFF', 'language': 'FASTEXPR', 'visualization': False, 'testPeriod': 'P2Y', 'maxTrade': 'ON', 'selectionHandling': 'POSITIVE', 'selectionLimit': selection_limit
        },
        'combo': combo_expression,
        'selection': select_expression
    }
    return {
        "type": "SUPER",
        "settings": {

},
        "combo": combo_expression,
        "selection": select_expression
    }
```
总之，这样生成的SuperAlpha应该还是非常有限的，可能过一段时间就会枯竭了，还需要不断的添加新的低相关性的RegularAlpha才可能延续。combo表达式对PNL影响比较大，还有待学习。

---

### 帖子 #55: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
- **主帖链接**: [L2] 代码分享拉取某个category下的全部dataset并实现批量生产数据预处理备战Pyramid.md
- **讨论数**: 5

```
分享代码给所有冲刺Pyramid的同学，分享不易，感谢点赞评论
```

这套代码结合了三阶框架和ACE Library，之前我们在跑单数据集的时候经常会放弃一些小数据集，从而可能错失一些有效的字段。本代码可以批量拉取某个category下的字段，并进行一定的筛选。

- **核心代码：获取全部datasets**

```
def get_datasets(    s,    instrument_type: str = 'EQUITY',    region: str = 'USA',    delay: int = 1,    universe: str = 'TOP3000'):    brain_api_url = "[链接已屏蔽]    url = brain_api_url + "/data-sets?" +\        f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"    result = s.get(url)    datasets_df = pd.DataFrame(result.json()['results'])    return datasets_df
```

- 筛选需要的category和coverage等信息

```
region = "JPN"region_code = "jpn"universe = "TOP1600"delay = 1datasets_df = get_datasets(s,region='JPN',delay=1,universe='TOP1600')pd.set_option('display.max_columns', None)  # 显示所有列pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值# select needed datasetsselected_datasets_df = datasets_df[    (datasets_df["delay"] == delay) &    (datasets_df["coverage"] > 0.5) & (datasets_df["coverage"] <= 1) &    (datasets_df["fieldCount"] > 0) & (datasets_df["fieldCount"] < 2000) &    (datasets_df["region"] == region) &    (datasets_df["universe"] == universe) &    (datasets_df["userCount"] > 0) & (datasets_df["userCount"] < 100) &    (datasets_df["valueScore"] > 1) & (datasets_df["valueScore"] < 10) &    (datasets_df["category"].apply(lambda x: x.get("id") if isinstance(x, dict) else None) == "analyst")    #(datasets_df["category"]  'analyst')    #datasets_df["name"].str.contains('news', case=False) &    #((datasets_df["category"] == 'analyst') | (datasets_df["category"] == 'analyst'))].sort_values(by=['valueScore'], ascending=False)print(selected_datasets_df)
```

- 批量预处理数据，生成数据大表，这里的作用等价于老师在论坛写的推荐数据

```
reset_fleg = 0for dataset_id in selected_datasets_df['id']:    df1 = get_datafields(s, dataset_id = dataset_id, region= region, universe=universe, delay=delay)    pd.set_option('display.max_columns', None)  # 显示所有列    pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值    df2 = df1[df1['type'] == 'MATRIX']    df3 = df1[df1['type'] == 'VECTOR']    #df4 = df1[df1['type'] == 'GROUP']    try:        print(len(data))        if reset_fleg == 1:            data = []      except NameError:        data = []    if len(df2)>0:        matrix_fields_1 = process_datafields(df1, "matrix")        data.extend(matrix_fields_1)    if len(df3)>0:        vector_fields_1 = process_datafields(df1, "vector")           data.extend(vector_fields_1)    print(dataset_id,'执行完毕')print(len(data))
```

剩下的工作就是套在不同的模版中了，祝大家早日达到MASTER!

---

### 帖子 #56: 使用[ClickHouse📕]建设你的大型数据库
- **主帖链接**: [L2] 使用[ClickHouse]建设你的大型数据库.md
- **讨论数**: 3

**ClickHouse**  是一个开源的列式数据库管理系统（DBMS），专为在线分析处理（OLAP）场景设计。ClickHouse 以其卓越的查询性能和高效的数据压缩能力而闻名，特别适合处理大规模数据的实时分析查询。

相比  **MySQL** ，ClickHouse 的列式存储和高效压缩使其在大规模数据分析场景下查询性能提升数十倍；相比  **MongoDB** ，ClickHouse 对复杂 SQL 查询和聚合操作的支持更强大，适合实时分析和高性能 OLAP 场景。

本文将持续更新，但不保证能连载完毕，因为我也是刚开始用这个东西，现学现卖

**前置准备：下载clickhouse并安装**

[[ClickHouse📕]Download and Install CK – WorldQuant BRAIN](/hc/en-us/community/posts/29266868911383--ClickHouse-Download-and-Install-CK) 

 **第一步：创建表，每一个表的内容都不一样，需要进行存储，下面是每一个你需要创建的表。** 。

[[ClickHouse📕]table: submitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266765833239--ClickHouse-table-submitted)

[[ClickHouse📕]table: pnls – WorldQuant BRAIN](/hc/en-us/community/posts/29266954512663--ClickHouse-table-pnls)

[[ClickHouse📕]table: fields – WorldQuant BRAIN](/hc/en-us/community/posts/29266990090263--ClickHouse-table-fields)

[[ClickHouse📕]table: unsubmitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266971586327--ClickHouse-table-unsubmitted)

第二步：导入数据

To Be Continue....

您的点赞就是我最大的动力

---

### 帖子 #57: 使用[ClickHouse📕]建设你的大型数据库
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用[ClickHouse]建设你的大型数据库_29266895095063.md
- **讨论数**: 3

**ClickHouse**  是一个开源的列式数据库管理系统（DBMS），专为在线分析处理（OLAP）场景设计。ClickHouse 以其卓越的查询性能和高效的数据压缩能力而闻名，特别适合处理大规模数据的实时分析查询。

相比  **MySQL** ，ClickHouse 的列式存储和高效压缩使其在大规模数据分析场景下查询性能提升数十倍；相比  **MongoDB** ，ClickHouse 对复杂 SQL 查询和聚合操作的支持更强大，适合实时分析和高性能 OLAP 场景。

本文将持续更新，但不保证能连载完毕，因为我也是刚开始用这个东西，现学现卖

**前置准备：下载clickhouse并安装**

[[ClickHouse📕]Download and Install CK – WorldQuant BRAIN](/hc/en-us/community/posts/29266868911383--ClickHouse-Download-and-Install-CK) 

 **第一步：创建表，每一个表的内容都不一样，需要进行存储，下面是每一个你需要创建的表。** 。

[[ClickHouse📕]table: submitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266765833239--ClickHouse-table-submitted)

[[ClickHouse📕]table: pnls – WorldQuant BRAIN](/hc/en-us/community/posts/29266954512663--ClickHouse-table-pnls)

[[ClickHouse📕]table: fields – WorldQuant BRAIN](/hc/en-us/community/posts/29266990090263--ClickHouse-table-fields)

[[ClickHouse📕]table: unsubmitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266971586327--ClickHouse-table-unsubmitted)

第二步：导入数据

To Be Continue....

您的点赞就是我最大的动力

---

### 帖子 #58: 如何使用腾讯ima解读模板大师中的策略逻辑经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何使用腾讯ima解读模板大师中的策略逻辑经验分享_31538237807127.md
- **讨论数**: 4

对于我这样的初学者，很多模板大师中提供的模板并不能完全理解，这就像车辆改造一样，如果你连车辆的基本构造都不了解，你要如何进行改装呢

所以从我的理解来说，要想使用模板，首先要理解它的基本逻辑，而且理解了一个好的想法，也便于我们日后能够举一反三。

在身边没有老师的前提下，我们只能借助AI，而我使用的就是腾讯IMA。

我们寻找任意模板将其复制到IMA，当然他的回答是基于之前已经建立好的世坤知识库，如果有伙伴需要，后面我也会写相关的文章进行分享。


> [!NOTE] [图片 OCR 识别内容]
> my_group=bucketfrank(cap); range= *0,1,0.1"); shock=(high-ts_delaylow; 1))/ts_delay(low; 1);
> talor_shock=(shock-log(shock +
> +1))*2-log(shock+1)*2; alpha=-group_rankfts_meanftalor_shock
> 24), my_group); group_neutralizelalpha;my_group)解释-下这段代码的逻辑
 知识库是基于你喂给它的资料进行回答，回答如下：

根据文档中的操作符定义与代码逻辑，逐步解释如下：

### **分步骤解析Alpha逻辑**

#### **Step 1. 创建分组：基于市值分位**

```
my_group = bucket(rank(cap), range="0,1,0.1")

```

- **操作符逻辑**
  - `rank(cap)` ：按 **横截面排名** 将股票市值归一化到  `[0,1]` 。
  - `bucket(..., range="0,1,0.1")` ：将排名均分为  **10个分位组** ，如：0-0.1（最小10%市值）、0.1-0.2等，形成 `my_group` 分类标签。

#### **Step 2. 计算日内价格冲击**

```
shock = (high - ts_delay(low, 1)) / ts_delay(low, 1)

```

- **公式意义**
  - `ts_delay(low, 1)`  获取前一日的最低价格( `low` )。
  - `(high - 昨日low) / 昨日low` ：衡量当日最高价相对于昨日最低价的 **相对涨幅** ，反映价格在日内交易的冲击强度。

#### **Step 3. 非线性变换：泰勒展开校正**

```
talor_shock = (shock - log(shock+1)) * 2 - log(shock+1) ** 2

```

- **数学推导**
  假设对小值 `shock ≈ 0` 作泰勒展开近似（保留到二阶）：
  - `log(1+shock) ≈ shock - 0.5*shock²`
  - 代入化简后表达式近似为： `talor_shock ≈ shock²` ，其目的是 **放大正方向的大波动信号** ，降低负值的影响。
- **实际效果** ：提升极端正冲击的权重，同时抑制小幅波动的影响。

#### **Step 4. 组内反向排名构建Alpha**

```
alpha = -group_rank(ts_mean(talor_shock, 24), my_group)

```

- **操作符分解**
  - `ts_mean(..., 24)` ：计算过去24天的 `talor_shock` 均值，过滤短期波动。
  - `group_rank(..., my_group)` ：在 `my_group` 各组内，按均值做 **组内排名** （如每组10%中的个股排名）。
  - `-` 负号反转排名：使组内 **最低均值的股票获得最高Alpha值** （预期行为如：价格冲击均值低的股票未来可能反弹）。

#### **Step 5. 组内中性化处理**

```
group_neutralize(alpha, my_group)

```

- **操作符作用**
  - 以 `my_group` 分组对Alpha进行 **中性化** ，确保每个组内的总暴露为0。
  - **目的** ：消除市值分组整体对Alpha的影响，避免策略过度暴露在某一分位（如小盘股波动大）。

### **策略逻辑总结**

1. **市值分层** ：将股票按市值分成10组，控制风格暴露。
2. **信号提取** ：通过日内价格冲击的24日均值，捕捉股票波动特征。
3. **组内选股** ：选择每组中近期价格冲击均值最低的股票（目标：均值回归）。
4. **风险控制** ：通过中性化处理，剥离市值分组带来的系统性影响，提升策略纯度。

### **潜在风险与建议验证点**

1. **数据范围验证**
   - `shock` 计算中若 `high < ts_delay(low,1)` （当日最高价低于前日最低价），会导致分母可能为负值，数学上 `log(shock+1)` 可能非法。需检查数据清洗条件。
2. **组内排名方向**
   - 当前反向操作( `-group_rank` )预计捕捉反转效应，需通过回测确认效果是否符合预期。
3. **参数敏感性**
   - 分组数10、24日均值窗口需参数优化，以平衡策略稳定性和敏感性。

建议回测时关注不同市值分组的收益贡献，以验证中性化是否有效。

通过不断重复上述过程，你就可以了解许多新的策略和想法，并且一定要记住，你可以把这些回答再整理后，再度喂给IMA，这样你会逐渐把这个知识库变得强大。

---

### 帖子 #59: 1. 下载/增量更新download_data(session, flag_increment=True)Self-correlation 0.7691 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.这是代码计算结果：alpha_id:  XgQqkZda self_corr:  0.7691116930719178alpha_id = "XgQqkZda"Self-correlation is 0.4589, which is above cutoff of 0.7, or Sharpe is better by 10.0% or more.这是代码计算结果：alpha_id:  zq6wpknV self_corr:  0.48371278563080605alpha_id = "zq6wpknV"加载数据os_alpha_ids, os_alpha_rets = load_data(tag='SelfCorr')self_corr = calc_self_corr(    session,    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)print("alpha_id: ", alpha_id, "self_corr: ", self_corr)
- **主帖链接**: [L2] 本地0误差计算自相关性【即插即用版】代码优化.md
- **讨论数**: 64

基于  [顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97))  发现的本地计算自相关性方法的落地，self-corr只计算本region里提交的所有alphas

首先一些函数，由于有函数说明，这里就不详细展开了

```
import requestsimport pandas as pdimport loggingimport timeimport requestsfrom typing import Optional, Tuplefrom typing import Tuple, Dict, Listfrom typing import Union, List, Tuplefrom concurrent.futures import ThreadPoolExecutorimport picklefrom collections import defaultdictimport numpy as npfrom tqdm import tqdmfrom pathlib import Pathdef sign_in(username, password):    s = requests.Session()    s.auth = (username, password)    try:        response = s.post('[链接已屏蔽])        response.raise_for_status()        logging.info("Successfully signed in")        return s    except requests.exceptions.RequestException as e:        logging.error(f"Login failed: {e}")        return Nonedef save_obj(obj: object, name: str) -> None:    """    保存对象到文件中，以 pickle 格式序列化。    Args:        obj (object): 需要保存的对象。        name (str): 文件名（不包含扩展名），保存的文件将以 '.pickle' 为扩展名。    Returns:        None: 此函数无返回值。    Raises:        pickle.PickleError: 如果序列化过程中发生错误。        IOError: 如果文件写入过程中发生 I/O 错误。    """    with open(name + '.pickle', 'wb') as f:        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)def load_obj(name: str) -> object:    """    加载指定名称的 pickle 文件并返回其内容。    此函数会打开一个以 `.pickle` 为扩展名的文件，并使用 `pickle` 模块加载其内容。    Args:        name (str): 不带扩展名的文件名称。    Returns:        object: 从 pickle 文件中加载的 Python 对象。    Raises:        FileNotFoundError: 如果指定的文件不存在。        pickle.UnpicklingError: 如果文件内容无法被正确反序列化。    """    with open(name + '.pickle', 'rb') as f:        return pickle.load(f)   def wait_get(url: str, max_retries: int = 10) -> "Response":    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。       Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。       Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    df = df[['Date', alpha_id]]    return dfdef get_alpha_pnls(    alphas: list[dict],    alpha_pnls: Optional[pd.DataFrame] = None,    alpha_ids: Optional[dict[str, list]] = None) -> Tuple[dict[str, list], pd.DataFrame]:    """    获取 alpha 的 PnL 数据，并按区域分类 alpha 的 ID。    Args:        alphas (list[dict]): 包含 alpha 信息的列表，每个元素是一个字典，包含 alpha 的 ID 和设置等信息。        alpha_pnls (Optional[pd.DataFrame], 可选): 已有的 alpha PnL 数据，默认为空的 DataFrame。        alpha_ids (Optional[dict[str, list]], 可选): 按区域分类的 alpha ID 字典，默认为空字典。    Returns:        Tuple[dict[str, list], pd.DataFrame]:            - 按区域分类的 alpha ID 字典。            - 包含所有 alpha 的 PnL 数据的 DataFrame。    """    if alpha_ids is None:        alpha_ids = defaultdict(list)    if alpha_pnls is None:        alpha_pnls = pd.DataFrame()       new_alphas = [item for item in alphas if item['id'] not in alpha_pnls.columns]    if not new_alphas:        return alpha_ids, alpha_pnls       for item_alpha in new_alphas:        alpha_ids[item_alpha['settings']['region']].append(item_alpha['id'])    fetch_pnl_func = lambda alpha_id: _get_alpha_pnl(alpha_id).set_index('Date')    with ThreadPoolExecutor(max_workers=10) as executor:        results = executor.map(fetch_pnl_func, [item['id'] for item in new_alphas])    alpha_pnls = pd.concat([alpha_pnls] + list(results), axis=1)    alpha_pnls.sort_index(inplace=True)    return alpha_ids, alpha_pnlsdef get_os_alphas(limit: int = 100, get_first: bool = False) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    retries = 0    total_alphas = 100    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url = f"[链接已屏蔽]        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphas[:total_alphas]def calc_self_corr(    alpha_id: str,    os_alpha_rets: pd.DataFrame | None = None,    os_alpha_ids: dict[str, str] | None = None,    alpha_result: dict | None = None,    return_alpha_pnls: bool = False,    alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    print(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corrdef download_data(flag_increment=True):    """    下载数据并保存到指定路径。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        flag_increment (bool): 是否使用增量下载，默认为 True。    """    if flag_increment:        try:            os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))            os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))            ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))            exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]        except Exception as e:            logging.error(f"Failed to load existing data: {e}")            os_alpha_ids = None            os_alpha_pnls = None            exist_alpha = []            ppac_alpha_ids = []    else:        os_alpha_ids = None        os_alpha_pnls = None        exist_alpha = []        ppac_alpha_ids = []           if os_alpha_ids is None:        alphas = get_os_alphas(limit=100, get_first=False)    else:        alphas = get_os_alphas(limit=30, get_first=True)       alphas = [item for item in alphas if item['id'] not in exist_alpha]    ppac_alpha_ids += [item['id'] for item in alphas for item_match in item['classifications'] if item_match['name'] == 'Power Pool Alpha']               os_alpha_ids, os_alpha_pnls = get_alpha_pnls(alphas, alpha_pnls=os_alpha_pnls, alpha_ids=os_alpha_ids)    save_obj(os_alpha_ids, str(cfg.data_path / 'os_alpha_ids'))    save_obj(os_alpha_pnls, str(cfg.data_path / 'os_alpha_pnls'))    save_obj(ppac_alpha_ids, str(cfg.data_path / 'ppac_alpha_ids'))    print(f'新下载的alpha数量: {len(alphas)}, 目前总共alpha数量: {os_alpha_pnls.shape[1]}')def load_data(tag=None):    """    加载数据。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        tag (str): 数据标记，默认为 None。    """    os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))    os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))    ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))    if tag=='PPAC':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha in ppac_alpha_ids]    elif tag=='SelfCorr':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha not in ppac_alpha_ids]    else:        os_alpha_ids = os_alpha_ids    exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]    os_alpha_pnls = os_alpha_pnls[exist_alpha]    os_alpha_rets = os_alpha_pnls - os_alpha_pnls.ffill().shift(1)    os_alpha_rets = os_alpha_rets[pd.to_datetime(os_alpha_rets.index)>pd.to_datetime(os_alpha_rets.index).max() - pd.DateOffset(years=4)]    return os_alpha_ids, os_alpha_rets
```

首先把上述函数拷贝出来

在配置的cfg里添加账户和密码以及os_alpha保存的路径

```
class cfg:    username = ""    password = ""    data_path = Path('.')sess = sign_in(cfg.username, cfg.password)
```

增量下载OS数据，下载好的数据将会保存在data_path里

```
# 增量下载数据download_data(flag_increment=True)
```

之后加载数据，计算corr。

其中`load_data`函数里有一个可选参数tag。来区分获得alpha，

如果设置tag='PPAC'则只获取PPAC池子里的alpha，

如果设置tag='SelfCorr'则只获取除了PPAC池子里的其他alpha

如果不设置或者 设置为None，则获取所有提交的alpha

calc_self_corr返回最大的自相关性

```
alpha_id = 'OJwdKNb'os_alpha_ids, os_alpha_rets = load_data()calc_self_corr(    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)
```

我在此选了两个例子用以展示结果

第一个 例子是一个`厂alpha`


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 30OOK
> OOOK
> OOOK
> Jan '14
> Jan'15
> Jan'16
> Jan '17
> Jan '18
> Jan'19
> Jan '20
> Jan '21
> Jan '23
> Pnl
> Jan 22


其wq平台的线上self-corr如下


> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> [aimUm
> [inimUT
> 0.0719
> -0.0715
> 名字
> Unlyerse
> Correlaton
> Sharpe
> Returns
> Tumovar
> Htess
> Margln
> ATOITITOUIS
> current)
> TOP3O00
> 1.0000
> 6.32
> 255.44%
> 30.05%6
> 18.43
> 170.029
> anonyymous
> TOPIOOO
> 0.0719
> 2.59
> 12014
> 7.1395
> 2.33
> 33.539
> aOTIMOUs
> TOP230
> 0.0634
> 2.52
> 10.744
> 13.3591
> 2.30
> 11.53922
> aROTIIOUs
> TOP3OO
> 0.0525
> 3.8-
> 13.134
> 11.3695
> 3.34
> 2.059
> TyMOUs
> TOP3OI
> 0.0495
> 5.53
> 10.944
> 10.8793
> 5.17
> 20.1292
> anOnyMOUs
> ILLIQUID_MINVOLIII
> 0.0399
> 3.96
> 3.734
> 12.5595
> 3.29
> 13.79923
> L2st


通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha
> OJWdKMb
> O5_alpha_ids,
> O5_alpha_rets
> load_data
> Selfcorr
> Calc_self_corr(
> alpha_id-alpha_id,
> O5_alpha
> rets=os_alpha
> pets,
> O5_alpha_ids=os_alpha_ids,
> 3ZKROG
> 0719
> IMOOON
> 0.0684
> Xn68QGb
> 0526
> Oogjjpb
> 0.0496
> gnrlMpl
> 0399
> RdgYkao
> 0587
> AkYpgIw
> 0.0604
> KkGPBJI
> 0655
> SMVZb2I
> 0.0703
> KO3M3eB
> 0715
> Length: 367
> dtype:
> float64
> 叩.float64(8.07191757289855728)
> (tn=


其线上PPAC结果为： Power Pool correlation 0.0356 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.

通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> OJWdKMb
> O5_alpha_ids,
> O5_alpha
> pets
> load_data
> PPAC
> Calc_self
> Corr(
> alpha_id-alpha_id,
> O5_alpha_rets=os_alpha_
> pets
> O5_alpha_ids=os_alpha_ids,
> WL8EVgX
> 0356
> V0a7JR2
> 0.0291
> ONjAqWb
> 0269
> O8nlN3q
> 0.0260
> pSeGPvv
> 0222
> aVNJAdI
> 0286
> SjbrMGN
> 0.0231
> X1Z08Y]
> 0247
> e6813诏
> 0.0267
> WgBar7e
> -0.0314
> Length: 61,
> dtype:
> f1oat64
> 叩.float64(8.03561886586891495)
> (tD8=


第二个 例子是一个正常的例子


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> PIL
> LOOOK
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> 2023


其wq平台的线上self-corr如下 
> [!NOTE] [图片 OCR 识别内容]
> 名宇
> UnNerse
> Correlatlon
> Sharpe
> Returns
> TurNOVer
> Hltness
> Margln
> anonymous (current)
> TOP3000
> 1.0000
> 1.51
> 6.329
> 3.0396
> 1.07
> 41.708
> anONNMOUs
> TOP300
> 0.5243
> 11.034
> 7.230
> 172
> 305292
> anOnyMOUs
> TOF3JOO
> 0.5241
> 10.244
> 4.9055
> 11.80922
> anonymous
> TOP300
> 0.5051
> 34
> 11.744
> 11.303
> 3.30
> 20.779323
> anOnyMOUs
> TOF3JOO
> 0.-931
> 153
> 12.12北
> 10.7350
> 1.57
> 22.499522
> anONNMOUs
> TOP300
> 0.4453
> 4.16
> 19.254
> 10.8130
> 5.15
> 35.52933


通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> 1P13*52
> O5_alpha_ids,
> O5_alpha
> pets
> load_data (ta=
> Selfcorr
> Calc
> cor(
> alpha_id-alpha_id,
> O5_alpha_rets=os_alpha_rets,
> Os_alpha_ids=os_alpha_ids,
> 146]
> IXqSZMJ
> 0.5243
> ANKqaGE
> 0.5241
> OLOAgYI
> 0.5061
> EIMGbe]
> 4901
> PZAVYRL
> 0.4463
> LnOZEYG
> 0.3494
> MbAGKZ8
> 0.3495
> Mbgzgjr
> 0.3523
> XkGORLS
> 0.3719
> JnLZlnl
> 0.3952
> Length: 386, dtype:
> float64
> m.float64 (0.524288988654845 )
> Self


其线上PPAC结果为： Power Pool correlation 0.4901 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.

通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> JPY3*52
> 05_alpha_ids,
> O5_alpha
> load_data
> PPAC
> Calc_self_corr(
> alpha_id-alpha_id,
> O5_alpha
> rets=os_alpha_rets,
> O5_alpha_ids=os_alpha_ids,
> OWZzzan
> 4901
> AOnjj8e
> 0.4667
> aVNJAdI
> 4495
> 3jLrp8e
> 0.4468
> YxdOKRV
> 0.4382
> ONnJOEV
> 0.0129
> GbuPrwG
> 0186
> PBKaEWN
> -0.0220
> XIBQVIJ
> -0.0322
> 15j7091
> -0.0604
> Length:
> 61, dtype: float64
> m.float64(9.4980856236004994)
> pots
> (tn=


---

### 帖子 #60: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 组sa时如何选取高质量因子经验分享_32034293019671.md
- **讨论数**: 24

如题，在顾问群中发现很多刚开始组sa的顾问，不清楚select的具体选择方式。本帖给出对应规则以及一些例子。

对于expert及以上顾问来说，筛选因子的第一步是用自己的因子，还是组别人的。这个可以通过own和not(own）进行筛选。

第二步，降低选到的因子是过拟合的，或者混信号的概率，可以通过operator_count限制op数量，dataset_count限制数据集数量。

（第二点五步，如果想要选取特定category，特定color或者特定tag的因子，也可以进行筛选。研究小组中有大佬提出过利用color和tag对于因子进行分组，从而按组select的方式）

第三步，选低相关因子：从分散化角度来说,我们自然希望选出的因子相关性较低,这个可以从prod_correlation参数进行控制（selfcor也可以，但是这个是小于等于prod的，不够准确）

第四步，选老顾问/组合表现较好顾问的因子：平台提供了许多因子owner的相关数据参数，可以根据参数进行筛选，主要包括成为顾问的时长，顾问地区，该顾问的sharpe，fit等等

第五步，按照表现选因子。出于防止过拟合和刻意筛选的角度，我们不能够直接选高sharpe，高fit的好（not for sure）因子，平台提供了几个字段帮助我们筛选因子，包括turnover，truncation，long和short count等等，按照每个字段的范围进行分组选因子可以大幅降低重复筛选的概率，从而降低相关性。

前边几步是筛选的过程，对于筛选的权重我们也可以进行调整。

例如：我们可以按照turnover的大小进行赋权，对于turnover较高的因子赋予更小的 权重（在select表达式后加上/turnover即可），此步需要根据个人需求进行修改。

总结：

以上几步是我在筛选中的思考流程，更为详细具体的可以参考 [Selection Expression | WorldQuant BRAIN]([链接已屏蔽]) ，针对因子选择的流程需要发挥主观能动性，多想多试，才能选出最适合的因子。以下几个案例是我在研究小组发过的select表达式总结，可以基于这三类，对于参数与权重进行调整，从而实现更好的组合。在自动化跑sa的时候，也可以按照不同的“模块”进行组装（但要注意条件不能太苛刻，至少得选出10个因子才能开始跑。）

(own&& ( (turnover>0.03&&turnover<0.05)||(turnover<0.13&&turnover>0.1)||(turnover<0.17&&turnover>0.15) || ((turnover>0.17&&turnover<0.20)))&&(operator_count<18)&&prod_correlation<0.7)/(sigmoid(turnover)*sigmoid(prod_correlation)*log(long_count))

(
not(own)&& 
((turnover<0.12&&turnover>0.09)||(turnover<0.15&&turnover>0.13)||(turnover<0.19&&turnover>0.16))
&&(operator_count<8)
&&(prod_correlation<0.4&&prod_correlation>0.0)
&&(dataset_count<=2)
) 
/(turnover*tanh(turnover)*sigmoid(self_correlation)*sigmoid(prod_correlation)*abs(long_count-short_count))

(own&&(turnover<0.07||(turnover<0.25&&turnover>0.2)))/(sigmoid(turnover)*sigmoid(prod_correlation))

---

### 帖子 #61: 给新手跑region和dataset的小建议
- **主帖链接**: https://support.worldquantbrain.com[L2] 给新手跑region和dataset的小建议_28467103126679.md
- **讨论数**: 8

我是一个 ***10月25日*** 才加入顾问计划的新人，经过非常非常多的尝试，每天花费了大量时间后， ***现在因子交了167个，金字塔完成了48个。*** 

前期新人跑数据挖掘遇到的大问题就是， **region** 的选择和 **dataset** 的选择，因为每个类型的数据集和每个地区的难度都是不一样的，所以前期新人更适合选一些简单的region或者dataset。

接下来我将分享一下我个人的一些心得体会，希望对新人有所帮助。

## 首先是region的选择。

region一共有10个，分别是：USA, GLB, EUR, ASI, CHN, KOR, TWN, JPN, HKG, AMR。

```
REGION_LIST = ['USA', 'GLB', 'EUR', 'ASI', 'CHN', 'KOR', 'TWN', 'JPN', 'HKG', 'AMR']
```

他们的简单程度我认为是

ASI > USA > TWN > EUR > GLB > JPN = CHN = HKG > KOR > AMR （都是delay 1的）

## 然后是category的选择

category一共有16个，分别是：pv, fundamental, analyst, socialmedia, news, option, model, shortinterest, institutions, other, sentiment, insiders, earnings, macro, imbalance, risk。

```
DATASET_CATEGORY_LIST = ['pv', 'fundamental', 'analyst', 'socialmedia', 'news', 'option', 'model', 'shortinterest', 'institutions', 'other', 'sentiment', 'insiders', 'earnings', 'macro', 'imbalance', 'risk']
```

他们的简单程度我认为是

model > pv > analyst = fundamental > other > option > institutions = news = insiders = sentiment > macro = risk = shortinterest = socialmedia > earnings > imbalance （都是delay 1的）

另外不建议新手去做delay 0的，我跑了近50万个都没有一个可以交的。

---

### 帖子 #62: 零基础考研失败应届生的一点经验经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 零基础考研失败应届生的一点经验经验分享_30694634496663.md
- **讨论数**: 4

由于长期备考研究生，导致脑袋里除了课本知识基本什么都没有了，仅剩的一点代码基础也都忘记的差不多了，于是，只能从头开始学习，由于没有工作，因此可以把时间都投入到学习中。

首先，我先用ai搜索了量化交易的相关信息，知道了要学习哪些相关知识，然后在小破站学习了python数据分析，再结合社区论坛和用户课程大概了解了brain平台的运行流程以及如何构建alpha，也是很轻松的成为了顾问，学习了顾问培训的 课程之后，成功的提交了第一个顾问alpha，给了我很大信心，后来的学习过程中，连续看了三次不同的part1培训课程，每一次都有很大的收获，目前看完part2的顾问培训，还没有把知识完全消化。

我的建议是一定要把用户四节课和顾问的两节课琢磨透，不会的问ai，然后代码和金融基础薄弱的话，可以到小破站学习相关课程，除此之外，我还每天坚持刷力扣，提高自己对代码的理解，论坛每天没事的时候都可以逛逛，会有很多意想不到的收获。

我是成为顾问之后才开始认真投入学习的，从2月26号开始，截至目前总共提交了38个alpha,很荣幸获得了进入研究小组的资格，虽然在学习过程中会遇到各种困难，但是坚持下去总是能克服的，在这里感谢一下顾问小组里各位大佬和同学的帮助。

目前提交的alpha质量并不高，其中有8个质量不过关，其余的base payment过关了，但是不知道是不是受之前eur活动的影响，因此最近三天都没有提交alpha，同时建议各位新人一定要以质量为主。 
> [!NOTE] [图片 OCR 识别内容]
> Total Payment (AII Time): 0S$28.23
> Base Payment
> Submitted Alphas
> 03/02/2025
> Base Payment: 1.82
> Total:
> 1.82
> <@ <@
> s
> sN
> 23
> <@
> s
> 1
> ?"
> 2
> 3'
> D
> A'
> ^^'
> A
> "
> ^A
> :
> 0'
> 2:
> 1
> ^ &
> ^8.
> ^^'
> A
> '
> ^公
> ^'
> ^@"
> Displayed Period
> 02/24/2025
> 03/16/2025
> 05528.23
> Displayed Period
> 02/23/2025
> 03/16/2025
> 38
> Yesterday
> 03/16/2025
> USS0.00
> Yesterday
> 03/16/2025
> Current period
> 03/01/2025
> 04/30/2025
> 05$23.33
> Current period
> 03/01/2025
> 04/30/2025
> 30
> Previous period
> 01/01/2025
> 02/28/2025
> US$4.90
> Previous period
> 01/01/2025
> 02/28/2025
> 15
> Year to date
> 02/17/2025
> 03/16/2025
> 05$28.23
> Yearto date
> 01/01/2025
> 03/16/2025
> 45
> Total
> 02/17/2025
> 03/16/2025
> 05$28.23
> Total
> 12/30/2024
> 03/16/2025
> 45
>  Mar
>  Mar
>  Mar
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> Mar
>  Mar
>  Mar
>  Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> Mar
>  Mar
>  Feb
>  Feb
>  Mar
> Mar
> Mar
> Feb
>  Feb
> Feb
> Feb
>  Mar
> Mar
> Mar
> Mar
> Mar
> 10。



> [!NOTE] [图片 OCR 识别内容]
> Current level: Gold
> Best level: Gold
> Current quarter end: March 31st, 2025
> GOLD
> Eligibility Criteria
> 2025-01,January 1st, 2025
> March 31st, 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 38
> 82 more to Master
> 20
> 120
> 220
> Pyramids Completed
> 1
> 3 more to Expert
> 10
> 30
> Combined Alpha Performance


---

### 帖子 #63: 如何在VSCODE上安装我发现的MCP？傻瓜式教程来了经验分享
- **主帖链接**: 如何在VSCODE上安装我发现的MCP傻瓜式教程来了经验分享.md
- **讨论数**: 49

8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行！亮一个灯就行！！！！！！第一步：在Vscode商店下载Roo code插件；第二步：在终端输入pip install cnhkmcp ， pip install pydantic[email]，pip install email-validator第三步：打开mcp本地目录，找到untracked文件夹，路径应该是  site-packages/cnhkmcp/untracked第四步：找到该文件夹里的user_config.json打开编辑输入你在worldquantbrain的账号密码。第五步：打开VScode 的RooCode插件，左边导航栏袋鼠图标，配置一个api，以ds api为例（打开deepseek，右上角api开放平台，api keys，创建，复制，粘贴进来（记得充钱））。第六步：插件右上角... 选择mcp server点上两个按钮，然后编辑全局mcp。第八步：对 MCP 文件进行配置，示例配置文件如下：args 分别是两个 mcp 文件的绝对路径，command 是你 python 程序的绝对路径。请根据你电脑的具体路径进行更改。配置成功应该是两个绿灯（科学上网）如果平台连接失败，尝试安装（ ）接下来你有可以让他来帮你干活啦！快来创建你自己的量化公司，招募并培训你的员工吧！{"mcpServers": {"worldquant-brain-platform": {"command": "/opt/anaconda3/bin/python","args": ["/opt/anaconda3/lib/python3.12/site-packages/cnhkmcp/untracked/platform_functions.py"],"description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features. Includes 25+ MCP tools for authentication, simulation creation, alpha management, dataset access, performance analysis, competition management, user profile operations, forum integration, and advanced analytics."}}}

---

### 帖子 #64: Initialize forum MCP servertry:    from mcp.server.fastmcp import FastMCP    forum_mcp = FastMCP('brain_forum_server')    forum_mcp.run()except ImportError:    Fallback for testing    forum_mcp = None
- **主帖链接**: https://support.worldquantbrain.com如何在VSCODE上安装我发现的MCP傻瓜式教程来了经验分享_34064552577559.md
- **讨论数**: 49

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行！亮一个灯就行！！！！！！**

第一步：在Vscode商店下载Roo code插件；


> [!NOTE] [图片 OCR 识别内容]
> RooCODE
> Roo Code
> Costrict (prev. Cline
> 2K
> Extension name
> Roo
> com
> 740,278
> (304)
> Costrict: strict Al coder for enterp..
> zgsm-ai
> Install
> whole dev team of Alagents in your editor。
> Roo Code
> 740K
> 5
> Install
> Auto Update
> t
> Whole dev team of Alagents in
> Roo Code
> Install
> DETAILS
> FEATURES
> CHANGELOG
> Kilo Code AI Agent (..
> 193k
> 龆
> Open Source Al coding assistant f
> Kilo Code
> Install
> English
> Catala
> Deutsch
> Espanol
> Francais
> C
> Bahasa Indonesia
> Italiano
> 日本
> Marketplace


第二步：在终端输入pip install cnhkmcp ， pip install pydantic[email]，pip install email-validator


> [!NOTE] [图片 OCR 识别内容]
> PROBLEMS
> OUTPUT
> DEBUG CONSOLE
> TERMINAL
> PORTS
> JUPYTER
> python3. 13-venvshoner@lgz wq
> %
> pip install cnhkmcp
> Collect=
> cnhkmcp
> Downloading cnhkmcp-1.2.0-py3-none-any.whl.metadata
> (5.2 kB)
> Requirement
> already satisfied:
> requests>=2.28.0
> i
> /Users /shoner /venv /
> 'python3.13-venv
> /lib/python3 . 13/site-packages
> (from cnhkmcp)
> (2.32.3)
> Requirement
> already satisfied: pandas>=l.5.0
> in /Users/shoner /venv /python3. 13-venv/li
> b/python3 . 13/site-packages
> (from
> cnhkmcp)
> (2.2.3)
> Collecting selenium>=4.0.0
> from
> cnhkmcp)
> Download
> selenium-4.34.2-py3-none-any
> Whl.metadata (7.5 kB)
> Requirement
> already satisfied:
> beautifulsoup4>=4.11.0
> in
> /Users/shoner /venv / python3.1
> 3-Venv /lib/
> 'python3. 13/site-packages_
> (from cnhkmcp)
> (4.13.4)
> C〉170+1
> m0
> 千C
> Lm
> ing
> ing


第三步：打开mcp本地目录，找到untracked文件夹，路径应该是  site-packages/cnhkmcp/untracked

第四步：找到该文件夹里的user_config.json打开编辑输入你在 **worldquantbrain** 的账号密码。

第五步：打开VScode 的RooCode插件，左边导航栏袋鼠图标，配置一个api，以ds api为例（打开deepseek，右上角api开放平台，api keys，创建，复制，粘贴进来（记得充钱））。


> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十6』
> To doits magic, Roo needsan API
> We recommend using an LLM Router:
> OpenRouter
> A unified interface for LLMs
> Requesty
> optimized LLM router
> $1 free credit
> OryoU can
> bring your provider API key:
> API Provider
> Anthropic documentation
> Anthropic
> You must provide
> Valid API key。
> Anthropic API
> Enter API Key.
> API keys are stored securely in VSCode's Secret Storage
> Get Anthropic API
> Use custom base URL
> https:Ilapi.anthropic.com
> Pass Anthropic API Key as Authorization header instead of X-Api-Key
> Import Settings
> Let's 90!
> Vo muot nrovido
> 3 Tlid 4DILo
> key.
> YoUT
> Key
> Key



> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十Ht
> To doits magic, Roo needsan API
> We recommend usingan LLM Router:
> OpenRouter
> unified interface for LLMs
> Requesty
> Your optimized LLM router
> $1 free credit
> OryoU can
> bring your provider API key:
> API Provider
> DeepSeek documentation
> DeepSeek
> DeepSeek API
> API keys are stored securely in VSCode's Secret Storage
> Model
> deepseek-chat
> DeepSeek-V3 achieves a significant breakthrough in inference speed over previous
> models
> It tops the leaderboard among open-source models and rivals the most
> advanced closed-source models globally。
> Does not support images
> Does not support computer use
> Crnnnrta nrnmnt nonhinn
> Import Settings
> Let's 90!
> key:
> Key


第六步：插件右上角... 选择mcp server


> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十H 』
> submitipy
> History
> V3.25
> Modes
> MCP Servers
> Open in Editor



> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十H 』
> MCP Servers
> Done
> The Model Context Protocol enables communication With locally running MCP servers that
> provide additional tools and resources to extend Roo's capabilities. You can use community-made
> servers or ask Roo to create new tools specific to your Workflow (e.9.,
> add a tool that gets the
> latest npm docs").
> Enable MCP Servers
> Turn this ONto let Roo Use tools from connected MCP servers
> This gives Roo more capabilities. If you
> don't plan to use these extra tools, turn i OFF to help reduce API token Costs
> Enable MCP Server Creation
> Enable this to have Roo help you build new custom MCP servers. Learn about server creation
> Hint: To reduce APItoken costs, disable this setting when
> are not actively asking Roo to create a
> new MCP server。
> Edit Global MCP
> Edit Project MCP
> Refresh MCP Servers
> MCP Marketplace
> Learn more about editing MCP settings files
> VoU


点上两个按钮，然后编辑全局mcp。

第八步：对 MCP 文件进行配置，示例配置文件如下：args 分别是两个 mcp 文件的绝对路径，command 是你 python 程序的绝对路径。请根据你电脑的具体路径进行更改。


> [!NOTE] [图片 OCR 识别内容]
> mcpServers
> {
> worldquant-brain- platform
> {
> Command"
> C: |Users
> IAdministrator
> IAppData'
> ILocal | IPrograms
> IPython'
> IPython313
> Ipython.exe
> args
> "C: | Users
> IAdministrator
> IAppData | ILocal
> IPrograms
> IPython
> IPyt
> hon313 |Lib | Isite-packages | Icnhkmcp
> untracked l Iplatform_functions . Py
> ],
> "description
> "Worldouant
> BRAIN
> Platform MCP
> Server
> Comprehensive trading platform integration with
> simulation management;
> alpha operations,
> and authentication。
> Credentials
> are
> Stored
> in
> User
> config.json in
> the
> same directory
> Provides tools
> for creating
> Isimulations, checking status,
> managing alphas,
> and accessing platform
> features
> },
> worldquant-brain-forum" :
> {
> Command"
> "C: |Users | IAdministrator
> IAppData
> ILocal
> IPrograms
> IPython
> IPython313
> Ipython.exe
> "args'
> "C: | |Users
> IAdministrator
> IAppData | ILocal
> IPrograms | |Python | IPyt
> hon313|ILib |Isite-packages | Icnhkmcp'
> untracked
> forum_functions .Py'
> ]
> description"
> "Worldouant
> BRAIN
> Forum MCP
> SerVer
> Forum
> interaction
> and knowledge extraction tools
> Provides glossary access,
> forum post reading〉
> and
> community
> features
> Credentials
> are stored
> in
> user_config.json
> in
> the
> same directory
> Supports headless
> browser
> automation
> for forum scraping
> and
> content extraction


配置成功应该是两个绿灯（科学上网）

如果平台连接失败，尝试安装（ ）


> [!NOTE] [图片 OCR 识别内容]
> 才启石 Roo 0芾卟刨徒新司正又 MCT 胙方琵。
> #舨夯砧刨迕
> 捉示:  不需要 Roo 创』新 MCP 服务器时廷议关闭;
> 戒少 API Token 贳用。
> worldquant-brain-platfomm
> global
> worldquant-brain-forum
> gobal


接下来你有可以让他来帮你干活啦！快来创建你自己的量化公司，招募并培训你的员工吧！

```
{  "mcpServers": {    "worldquant-brain-platform": {      "command": "/opt/anaconda3/bin/python",      "args": [        "/opt/anaconda3/lib/python3.12/site-packages/cnhkmcp/untracked/platform_functions.py"      ],      "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features. Includes 25+ MCP tools for authentication, simulation creation, alpha management, dataset access, performance analysis, competition management, user profile operations, forum integration, and advanced analytics."    }  }}
```

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 26年Q1 Genius定级已更新Q2赛季加油_39728814444695.md
- **评论时间**: 2个月前

祝贺国区榜上有名的各位，也感谢大家一起贡献的开源社区，感谢三位老师与各位顾问的互帮互助。我们下个季度继续努力，芝麻开花节节高。

==============================

专注当下，每天进步

==============================

---

### 探讨 #2: 关于《4月combined更新，国区进步最显著的10位！经验分享》的评论回复
- **帖子链接**: [Commented] 4月combined更新国区进步最显著的10位经验分享.md
- **评论时间**: 1年前

感谢XX佬的数据统计，下次更新国区应该还是会出现许多大幅上涨的人员。
希望下一个是我。Genius计划与combine息息相关，什么都能刷 combine真的刷不了
========================================================
========================================================

---

### 探讨 #3: 关于《4月combined更新，国区进步最显著的10位！经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 4月combined更新国区进步最显著的10位经验分享_32732849016215.md
- **评论时间**: 1年前

感谢XX佬的数据统计，下次更新国区应该还是会出现许多大幅上涨的人员。
希望下一个是我。Genius计划与combine息息相关，什么都能刷 combine真的刷不了
========================================================
========================================================

---

### 探讨 #4: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] AI小白10分钟学会Gemini Chrome 插件的配置和使用.md
- **评论时间**: 3个月前

感谢分享，论坛真满是宝藏。
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #5: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] AI小白10分钟学会Gemini Chrome 插件的配置和使用_38254706003607.md
- **评论时间**: 3个月前

感谢分享，论坛真满是宝藏。
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #6: 关于《How to create Self Super Alpha》的评论回复
- **帖子链接**: [Commented] How to create Self Super Alpha.md
- **评论时间**: 1年前

Congratulations on achieving the Master level! I would like to ask if you have any good selection and combination expressions for building super alphas?

---

### 探讨 #7: 关于《How to create Self Super Alpha》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] How to create Self Super Alpha_31474919826967.md
- **评论时间**: 1年前

Congratulations on achieving the Master level! I would like to ask if you have any good selection and combination expressions for building super alphas?

---

### 探讨 #8: 关于《My WorldQuant Journey: Climbing the Ranks to Grandmaster》的评论回复
- **帖子链接**: [Commented] My WorldQuant Journey Climbing the Ranks to Grandmaster.md
- **评论时间**: 1年前

What ranges should the six tiebreaker factors be controlled within, considering that my current level is Gold?
thanks for your expression
-----------------------------------------------------------------------------------------------------------------

---

### 探讨 #9: 关于《My WorldQuant Journey: Climbing the Ranks to Grandmaster》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] My WorldQuant Journey Climbing the Ranks to Grandmaster_31538516287511.md
- **评论时间**: 1年前

What ranges should the six tiebreaker factors be controlled within, considering that my current level is Gold?
thanks for your expression
-----------------------------------------------------------------------------------------------------------------

---

### 探讨 #10: 关于《PPA活动主题限制下，提交ra点塔的一点心得。》的评论回复
- **帖子链接**: [Commented] PPA活动主题限制下提交ra点塔的一点心得.md
- **评论时间**: 3个月前

感谢大佬的分享，ra确实是需要手动搓一搓的

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #11: 关于《PPA活动主题限制下，提交ra点塔的一点心得。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] PPA活动主题限制下提交ra点塔的一点心得_38121310515223.md
- **评论时间**: 3个月前

感谢大佬的分享，ra确实是需要手动搓一搓的

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #12: 关于《self corr计算的代码优化》的评论回复
- **帖子链接**: [Commented] self corr计算的代码优化.md
- **评论时间**: 1年前

感谢小虎哥的分享，自己目前配置本地计算还存在一些问题，一直懒得去优化，下个季度得好好上心。

============================================================================
============================================================================

---

### 探讨 #13: 关于《self corr计算的代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] self corr计算的代码优化_32893337921943.md
- **评论时间**: 1年前

感谢小虎哥的分享，自己目前配置本地计算还存在一些问题，一直懒得去优化，下个季度得好好上心。

============================================================================
============================================================================

---

### 探讨 #14: 关于《Superalpha combo框架经验分享》的评论回复
- **帖子链接**: [Commented] Superalpha combo框架经验分享.md
- **评论时间**: 5个月前

感谢分享，目前论坛对select的帖子已经较为完备，对于combo的帖子比较稀缺，感谢分享。
希望有更多的人可以提出自己的combo idea 。
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #15: 关于《Superalpha combo框架经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Superalpha combo框架经验分享_33896439614231.md
- **评论时间**: 5个月前

感谢分享，目前论坛对select的帖子已经较为完备，对于combo的帖子比较稀缺，感谢分享。
希望有更多的人可以提出自己的combo idea 。
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #16: 关于《velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享》的评论回复
- **帖子链接**: [Commented] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享.md
- **评论时间**: 1年前

白兄的经历令人钦佩。从VF值0.04到0.93，没有被低谷打败，没有摆烂，而是通过不懈努力、积极学习、持续反思，逐步突破瓶颈。他的坚持和耐心最终得偿所愿，收获了成功与宝贵经验，这种精神值得我们学习。 
向白兄致敬🫡

---

### 探讨 #17: 关于《velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享_32340009231127.md
- **评论时间**: 1年前

白兄的经历令人钦佩。从VF值0.04到0.93，没有被低谷打败，没有摆烂，而是通过不懈努力、积极学习、持续反思，逐步突破瓶颈。他的坚持和耐心最终得偿所愿，收获了成功与宝贵经验，这种精神值得我们学习。 
向白兄致敬🫡

---

### 探讨 #18: 关于《[SuperAlpha]SELECTION框架-v2经验分享》的评论回复
- **帖子链接**: [Commented] [SuperAlpha]SELECTION框架-v2经验分享.md
- **评论时间**: 10个月前

震惊，感谢游戏王的付出，这篇文章值得反复观看，每次都会有心得体会。
sa确实需要多看多敲才能有更多的心得，一味的只靠代码无脑跑，迟早有吃回旋镖的那一天。

=====================================================================
=====================================================================
====================================================================

---

### 探讨 #19: 关于《[SuperAlpha]SELECTION框架-v2经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [SuperAlpha]SELECTION框架-v2经验分享_33745533142679.md
- **评论时间**: 10个月前

震惊，感谢游戏王的付出，这篇文章值得反复观看，每次都会有心得体会。
sa确实需要多看多敲才能有更多的心得，一味的只靠代码无脑跑，迟早有吃回旋镖的那一天。

=====================================================================
=====================================================================
====================================================================

---

### 探讨 #20: 关于《【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化_32763493267863.md
- **评论时间**: 1年前

感谢橘子姐的分享，十分有用，平台回测sa 检查corrlation都耗费许久的时间，这些时间都属于平白无故的浪费。
借助于橘子姐这个代码可以快速的寻找能赚更多钱的sa，让赚钱所花的时间更短。
============================================================

===========================================================

---

### 探讨 #21: 关于《依次添加到总列表中》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】复现2023年因子日历论坛精选.md
- **评论时间**: 1年前

iqc大佬吗，期待你成为正式顾问解锁权限，给咱国区带来更多更好的分享！！！！！
================================================================
================================================================

---

### 探讨 #22: 关于《依次添加到总列表中》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】复现2023年因子日历论坛精选_33049767468055.md
- **评论时间**: 1年前

iqc大佬吗，期待你成为正式顾问解锁权限，给咱国区带来更多更好的分享！！！！！
================================================================
================================================================

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Eligibility Criteria篇】一文告诉你如何GOLD直通Grandmaster上篇置顶的论坛精选_39922788056343.md
- **评论时间**: 1个月前

恭喜大佬，圆梦，有道是江山代有才人出，每个赛季都有人可以从gold直通grandmaster，相信下个赛季依然有人。
----------------------------------------------------------------------------------------------------------------
                                 祝大佬月月VF1.0！高筑墙！广积粮！缓称王！
--------------------------------------------------------------------------------------------------------------

---

### 探讨 #24: 关于《【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化》的评论回复
- **帖子链接**: [Commented] 【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化.md
- **评论时间**: 1年前

感谢橘子姐的分享，现在sa手动回测不仅等待时间长，网页还经常卡崩溃。为了微调一个参数或者稍微降低pc 可能需要坐着调好几个小时，十分恼火。
希望贴主继续分享有用的帖子，祝愿橘子姐vf继续新高。
==============================================================================

---

### 探讨 #25: 关于《【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【SA回测优化】回测前先确认selcect的alpha数量是否不低于指定的阈值代码优化_32985437982231.md
- **评论时间**: 1年前

感谢橘子姐的分享，现在sa手动回测不仅等待时间长，网页还经常卡崩溃。为了微调一个参数或者稍微降低pc 可能需要坐着调好几个小时，十分恼火。
希望贴主继续分享有用的帖子，祝愿橘子姐vf继续新高。
==============================================================================

---

### 探讨 #26: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用_39466731879063.md
- **评论时间**: 2个月前

很好的想法帮助每一位根据当下的vf和os分数判断今天的收入。
让好因子发挥更大的优势。

-------------------------------------------------------------------------------------------

慢慢来，相信时间的力量。

-------------------------------------------------------------------------------------------

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据.md
- **评论时间**: 3个月前

超级实用的工具，已集成在华子哥插件中。
感谢大佬分享。
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据_38121748548759.md
- **评论时间**: 3个月前

超级实用的工具，已集成在华子哥插件中。
感谢大佬分享。
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #29: 关于《4. 登录（关键：需两次执行登录命令）》的评论回复
- **帖子链接**: [Commented] 【工具】在opencode中使用Antigravity内模型额度详解包含如何配置mcp经验分享.md
- **评论时间**: 3个月前

学会了，感谢大佬的分享，祝您新年快乐

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #30: 关于《4. 登录（关键：需两次执行登录命令）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【工具】在opencode中使用Antigravity内模型额度详解包含如何配置mcp经验分享_38492959452823.md
- **评论时间**: 4个月前

学会了，感谢大佬的分享，祝您新年快乐

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #31: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: [Commented] 【插件】Genius Rank分析代码优化.md
- **评论时间**: 1年前

使用了这个插件才知道离下一阶段还差好几百名，还得继续努力

---

### 探讨 #32: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md
- **评论时间**: 1 year ago

使用了这个插件才知道离下一阶段还差好几百名，还得继续努力

---

### 探讨 #33: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: [Commented] 【效率王】APP-30完全自动化时代.md
- **评论时间**: 3个月前

感谢大佬的分享，ai太猛了，一定要利用好ai，不然就是ai利用我了
=================================================
=================================================
================================================

---

### 探讨 #34: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】APP-30完全自动化时代_38872307253655.md
- **评论时间**: 3个月前

感谢大佬的分享，ai太猛了，一定要利用好ai，不然就是ai利用我了
=================================================
=================================================
================================================

---

### 探讨 #35: 关于《【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template》的评论回复
- **帖子链接**: [Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template.md
- **评论时间**: 6个月前

============================================================
感谢大佬的分享，回测限制今日落地了，不用ai极有可能会被淘汰。

期待大家的下一次分享。
============================================================

---

### 探讨 #36: 关于《【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template_36671111976983.md
- **评论时间**: 6个月前

============================================================
感谢大佬的分享，回测限制今日落地了，不用ai极有可能会被淘汰。

期待大家的下一次分享。
============================================================

---

### 探讨 #37: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

昨天提交了三个因子，都是EUR TOP2500 fit和mar分别为 {1.22 ，44.90} {2.56  ，23.58 }   {1.04，42.73    }  base为1.88。质量不是很高，虽然有两个因子的margin很高，但是fitness 还是太低了。如何提高fitness 是一直困扰着我的事情。

---

### 探讨 #38: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

得益于theme的加成，今天的basepayment来到了4刀，我是交了4个EUR，其中一个是ATOM其他都是多数据集。希望再接再厉多交点ATOM的赚点低保

---

### 探讨 #39: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

断粮三天 来许个愿  让我产出一些

---

### 探讨 #40: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

昨天交了两个因子  base1.77  很一般的水平   再接再厉

---

### 探讨 #41: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

昨天提交了 两个因子 一个比赛的一个非比赛的theme 可能混交base比不混交收入低，未达到预期。趁着比赛要多点亮几个金字塔

---

### 探讨 #42: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

2025/4/17  昨天交了两个ppac 因子 收入8.09刀，最近搞不出来sa.   少赚了好多钱。============================================================================================================================================================================================================

---

### 探讨 #43: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

昨天交了 三个 base 8刀   今天断粮了

---

### 探讨 #44: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

2025/4/19昨天找了半天交了一个eur theme 7刀 一个usa super7刀 一共15刀   加油============================================================================================================================================================================================================

---

### 探讨 #45: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

2025/4/20昨天交了两个ra 一个sa  赚的显著降低了，可能是sc太高了。今天交了一个不错的sa 看看明天给多少！============================================================================================================================================================================================================

---

### 探讨 #46: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

==================================================================================================================================昨天收入只有5刀   今天交了四个theme 因子 明天看看收入情况  希望可以有所提升==================================================================================================================================

---

### 探讨 #47: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

昨天交了4个ppac 因子  只有9.9刀 可能是pc 太高了..  今天交了四个eur的 明天看看base结合了这几天的收益，以及群内各位的讨论。这个PPAC theme 如果提交Prod corr 与SELF CORR 双0的因子，给的钱都是30+刀，如果有一个pc>0.7 那就是20  两个或者PC>0.7  就是10刀左右，如果是EUR D0 或者GLB 这种pyr加成较高的，则可以达到40+刀。但是pc sc 双0 好像是没有通过检测的regular alpha  这种因子是否真的是一个对组合有优化，对combine os 和valuefactor 是否有正向的积极作用可能需要等到两个月后的更新，正好卡在了季度评比。希望不要太炸裂

---

### 探讨 #48: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

==================================================================================================================================昨天交了4个eur 因子  ra base 来到了47刀，感谢ppac,今天交了四个glb 可能不会很多 因为pc 太高了==================================================================================================================================

---

### 探讨 #49: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

g昨天提交了4个g'l'b 因子 base 9.78刀   47->9

---

### 探讨 #50: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

------------------------------------------------------------------------------------2025年，5月10日。昨天提交了4个 regular alpha ,1个 super alpha. base payment 为17.81刀，其中 regular alpha 为9.92  super  alpha 为 7.89刀，我的value factor 为0.96 这么看 两个收益都是不达标的，但是由于我只是一个gold 只靠自己的因子，组super alpha 确实难以维持，产生fitness >5  pord corr<0.7的因子好难，暴力跑了好几天也没有几个可以提交的。希望这个季度有希望成为 master 可以有更多的因子用来选择。对于目前的genius 排名，金字塔和数量明天应该就可以达标了，希望combine 给一共好分数。-----------------------------------------------------------------------------------------大家一起加油，respect！！！

---

### 探讨 #51: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

2025/5/12 ----------------------------------------------------------------------------------------------------------------------------------昨天提交的因子的base收益为 regular alpha :47.89 super alpha 11.92  总base为 59.81 距离60刀咫尺之遥！super alpha 质量不高，应该是prod corr 0.7的原因，今天提交了一个0.59 pc的super alpha  fit>5  应该可以拿到25刀+，regular alpha 必须交低self corr  prod corr 才能有高额的收益。-------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #52: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

2025/5/13 因子提交报告#### 昨天收益回顾昨天（2025年5月12日）的收益如下：- **Regular Alpha**: US$59.99- **Super Alpha**: US$21.74- **总收益**: US$31.73昨天的总收益达到了US$31.73，Super Alpha的质量有待提高，昨提交了一个prod corr为0.59的Super Alpha，fit值大于5，预计可以获得20刀以上的收益。Regular Alpha需要提交低self corr和低prod corr的因子才能获得高额的收益。今天的因子提交策略主要是优化Super Alpha的质量，同时继续提交高质量的Regular Alpha因子。通过降低self corr和prod corr，我们希望能够获得更高的收益。-------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #53: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

2025/05/14 量化日记Basepayment 情况：Regular Alpha 16 usd  Super alpha 26 usd  共42刀  300rmb4个 RA 分别是3ASI 1EUR 1GLB  Super 也是ASI(fit >5  prod corr<0.6)要多region 多category 总之尽力而为昨天更新了genius 面板  贴一下   目前各项成功达到master等级，期待两个月后combine不要让我失望 = =对于Grand Master 目前感觉毫无希望，保质保量太难了。大家共勉----------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #54: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikzMWFkODc3MC00MDZhLTRlMmEtYTlhNS05YjQ2Y2NlZTdjN2MGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNRzg4NTkyBjsIVDoScmVzdWx0c19jb3VudGka--86ba43e180805b4ad69f9cdb7a2893b6c3ce9f57
- **评论时间**: 1年前

######### 量化交易日记 - 2025年5月15日####################################日期： 2025年5月15日昨日回顾：昨天（2025年5月14日）的因子提交和收益情况如下：- Regular Alpha: US$34.43- Super Alpha: US$19.66- **总收益**: US$54.09从base图表中可以看出，Regular Alpha和Super Alpha的表现对比昨日均有所提升，特别是Regular Alpha，贡献了大部分的收益。这主要是归因于pc 0的影响。More region  More universe More Alpha   总之就是数量质量分散，继续保持

---

### 探讨 #55: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天提交了三个因子，都是EUR TOP2500 fit和mar分别为 {1.22 ，44.90} {2.56  ，23.58 }   {1.04，42.73    }  base为1.88。质量不是很高，虽然有两个因子的margin很高，但是fitness 还是太低了。如何提高fitness 是一直困扰着我的事情。

---

### 探讨 #56: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

得益于theme的加成，今天的basepayment来到了4刀，我是交了4个EUR，其中一个是ATOM其他都是多数据集。希望再接再厉多交点ATOM的赚点低保

---

### 探讨 #57: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

断粮三天 来许个愿  让我产出一些

---

### 探讨 #58: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天交了两个因子  base1.77  很一般的水平   再接再厉

---

### 探讨 #59: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天提交了 两个因子 一个比赛的一个非比赛的theme 可能混交base比不混交收入低，未达到预期。
趁着比赛要多点亮几个金字塔

---

### 探讨 #60: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/4/17  昨天交了两个ppac 因子 收入8.09刀，最近搞不出来sa.   少赚了好多钱。
====================================================================
====================================================================
====================================================================

---

### 探讨 #61: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天交了 三个 base 8刀   今天断粮了

---

### 探讨 #62: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/4/19
昨天找了半天交了一个eur theme 7刀 一个usa super7刀 一共15刀   加油  
====================================================================
====================================================================
====================================================================

---

### 探讨 #63: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/4/20
昨天交了两个ra 一个sa  赚的显著降低了，可能是sc太高了。今天交了一个不错的sa 看看明天给多少！
====================================================================
====================================================================
====================================================================

---

### 探讨 #64: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

=================================================================
=================================================================
昨天收入只有5刀   今天交了四个theme 因子 明天看看收入情况  希望可以有所提升
=================================================================
=================================================================

---

### 探讨 #65: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天交了4个ppac 因子  只有9.9刀 可能是pc 太高了..  今天交了四个eur的 明天看看base
结合了这几天的收益，以及群内各位的讨论。这个PPAC theme 如果提交Prod corr 与SELF CORR 双0的因子，给的钱都是30+刀，如果有一个pc>0.7 那就是20  两个或者PC>0.7  就是10刀左右，如果是EUR D0 或者GLB 这种pyr加成较高的，则可以达到40+刀。但是pc sc 双0 好像是没有通过检测的regular alpha  这种因子是否真的是一个对组合有优化，对combine os 和valuefactor 是否有正向的积极作用可能需要等到两个月后的更新，正好卡在了季度评比。希望不要太炸裂

---

### 探讨 #66: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

=================================================================
=================================================================
昨天交了4个eur 因子  ra base 来到了47刀，感谢ppac,今天交了四个glb 可能不会很多 因为pc 太高了
=================================================================
=================================================================

---

### 探讨 #67: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

g昨天提交了4个g'l'b 因子 base 9.78刀   47->9

---

### 探讨 #68: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

------------------------------------------------------------------------------------
2025年，5月10日。
昨天提交了4个 regular alpha ,1个 super alpha. base payment 为17.81刀，其中 regular alpha 为9.92  super  alpha 为 7.89刀，我的value factor 为0.96 这么看 两个收益都是不达标的，但是由于我只是一个gold 只靠自己的因子，组super alpha 确实难以维持，产生fitness >5  pord corr<0.7的因子好难，暴力跑了好几天也没有几个可以提交的。希望这个季度有希望成为 master 可以有更多的因子用来选择。
对于目前的genius 排名，金字塔和数量明天应该就可以达标了，希望combine 给一共好分数。
-----------------------------------------------------------------------------------------
大家一起加油，respect！！！

---

### 探讨 #69: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/5/12 ----------------------------------------------------------------------------------------------------------------------------------
昨天提交的因子的base收益为 regular alpha :47.89 super alpha 11.92  总base为 59.81 距离60刀咫尺之遥！
super alpha 质量不高，应该是prod corr 0.7的原因，今天提交了一个0.59 pc的super alpha  fit>5  应该可以拿到25刀+，regular alpha 必须交低self corr  prod corr 才能有高额的收益。
-------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #70: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/5/13 因子提交报告

#### 昨天收益回顾
昨天（2025年5月12日）的收益如下：
- **Regular Alpha**: US$59.99
- **Super Alpha**: US$21.74
- **总收益**: US$31.73

昨天的总收益达到了US$31.73，Super Alpha的质量有待提高，昨提交了一个prod corr为0.59的Super Alpha，fit值大于5，预计可以获得20刀以上的收益。Regular Alpha需要提交低self corr和低prod corr的因子才能获得高额的收益。
 
> [!NOTE] [图片 OCR 识别内容]
> EUR
> TOP2SDO
> 5-
> 11.759
> 1 +
> 1.739
> -3
> ILLIZUIDMI 
> 325
> 139
> 12
> 2295
> 256
> 61
> NIOLII
> 15350
> 36191
> 5-350
> -339
> NINVOLIN
> 015
> 634
> 5479
> 17.37
> ILLIQUID_NIV。
> 31.+19
> 3.121
> 24.209
> 20137
> 25


今天的因子提交策略主要是优化Super Alpha的质量，同时继续提交高质量的Regular Alpha因子。通过降低self corr和prod corr，我们希望能够获得更高的收益。
-------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #71: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/05/14 量化日记
Basepayment 情况：
Regular Alpha 16 usd  Super alpha 26 usd  共42刀  300rmb
4个 RA 分别是3ASI 1EUR 1GLB  Super 也是ASI(fit >5  prod corr<0.6)
 
> [!NOTE] [图片 OCR 识别内容]
> REBUlar
> ACTNE
> 05/13/2025 EDT
> EUR
> TOPZSOD
> SUDET
> ACTNE
> 05/1312025 EDT
> MNOLIII
> REEUlar
> ACTNE
> 05/13/2025 EDT
> MINNCLIII
> REEUlar
> ACTNE
> 05/13/2025 EDT
> SLB
> MINICLIII
> REEUlar
> ACTNE
> 05/13/2025 EDT
> MINNCLIII
 
要多region 多category 总之尽力而为
昨天更新了genius 面板  贴一下   目前各项成功达到master等级，期待两个月后combine不要让我失望 = =
 
> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-02 Loril 1st  2025
> June 3Oth  2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 140
> 80 more to Grandmaster
> 120
> 220
> Pyramids Completed
> 22
> 28 more to Grandmaster
> Combined Alpha Performance
> 1.57
> 0.43 more to Grandmaster
> Combined Selected Alpha Performance
> 2.2
> Reached Grandmaster
 
对于Grand Master 目前感觉毫无希望，保质保量太难了。
大家共勉
----------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #72: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

最近靴子落地，产出有限，最近三天都只交了一个SA。

=============================== 期待下一件好事   ===============================
============================================================================

---

### 探讨 #73: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

今天combine再次更新，三个指标都下降了一些。不过好消息是还>2，不至于很狼狈。希望下一次更新别让我跌出去了。
=============================== 期待下一件好事   ===============================
============================================================================

---

### 探讨 #74: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

sa pc<0.3  究竟是怎么做出来的啊

太卷了吧！！！！！
=============================== 期待下一件好事   ===============================
============================================================================

---

### 探讨 #75: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 0年前

2025 7 16
量化日记又满了，翻看大家的记录，收获了很多有用的知识。

前日提交了三个D0 一个D1给了30刀

今日又提交了三个D0一个D1 期待一下

SA开始坐牢，没有了比赛，产出就不多了

====================================================================================
====================================================================================

---

### 探讨 #76: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025年6月3日

亮化日记第2期第1记

昨天的base payment来到了94刀！历史新高。

首先是regular alpha  base payment 为47刀，分别是USA delay 0的两个因子以及EUR Delay 1的两个因子。表现不错，但是pnl年份过少，本来是想随便交上去点亮金字塔的，没想到竟然给了这么多base，满满的惊喜。

接着是SuperAlpha base payment 为46刀  fitness8  prod corr为0.48

Super alpha有钱的秘诀就是老生常谈的fitness大于5  prod corr小于0.7  0.5

Prod corr小于0.5收入比prod corr小于0.7翻倍 两倍。

希望此后收入继续新高，早日突破100刀

---

### 探讨 #77: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025年六月5日
明天就要高考了，虽然我18年就考完了，但是研究小组竟然有高中生！并且每天孜孜不倦的在不断学习进步。这个学习的精神值得我们敬佩！
昨天交了一个ra 一个sa
ra 比较抽象是 USA D0 News dataset  感觉这个数据集经常出现抽象的因子，只有两三年数据，不过增长很猛，希望os增长也猛。这个抽象因子的fit 高大5.30！ 不出意外让我获得了高base 之前一个普通因子大概只有2 3刀 交满4个也就只有10刀，如今比赛结束这个因子竟然给了我几十刀。真的如坐针毡，恐怕下下个月value factor 不如当下，一泻千里。
Super Alpha 交了一个fit≥5 prod corr≤0.5 的因子 足足给了50刀！！！！！恐怖如斯。pc≤0.5 真的是非常重要。
fitness >5 以后就没太大意义了。

---

### 探讨 #78: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

我的量化日记 2025/06/05
昨天提交的super alpha 指标为fitness5+ pc0.47 base为45刀
ra base为7.8刀。昨天提交的因子给了300多块，还是非常值得高兴的事情。

晚上吃顿好的犒劳一下。
=======================================================================================================================================================================================赚钱很重要，开心更重要=================================================

---

### 探讨 #79: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025年6月7日 高考第一天江苏大雨，十一点开始手搓sa，今天终于搓出来一个pc小于0.5的sa。fit大于5.
==================================
昨天的base 更新了ra 7刀 sa 15.99 pc没有小于0.5 直接从50刀跌到16刀

==================================

今天达成了220个提交。目前除了金字塔都已经满足了gm的条件，目前还差6个金字塔，加油！

=================================
但是六位数据目前较差，在master中排倒数了

---

### 探讨 #80: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

这几天比较忙一直忘记写日记了，来补一下作业。 15 16 17 这几天的base都不到20刀，sa很难搓出低于0.5 pc的 出现了几次sa<10 usd 对比第一周50刀base。不止是腰斩了，直接斩到脚趾头了 ====================================================================， 生命是一场盛宴 ====================================================================

---

### 探讨 #81: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

昨天没有提交比赛sa，提交了一个自己的sa，终于组出来一个低于0.5pc的sa
昨天sa base44刀。ra只有8刀，ram加成没什么感觉

===========================================================
===========================================================

---

### 探讨 #82: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

====================================================================================昨日base19刀。sa ra 都没突破10刀。 低于0.5 pc的sa 组不出来
====================================================================================

---

### 探讨 #83: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025 /6 /20
昨天base payment为48.8刀 其中sa 为ace2023的sa。pc 0.49 38刀
===================================================
===================================================
===================================================

---

### 探讨 #84: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025年6月24日
=======
昨天base收益为55刀 其中sa为47刀。ra为8刀。 
sa 得益于pc 小于0.5 可以赚点钱
今天提交了一个sa pc 0.45 希望可以多点base
==================
=================
==================

---

### 探讨 #85: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025年6月25日base 收益为50刀
sa 搓出来一个pc <0.5的。 收益还不错 最近gm排行榜太卷了
马上掉下来了
============================================
===========================================
============================================
==========================================

---

### 探讨 #86: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

赛季末的每一天都极度疯狂，昨天只交了sa，ra忘记交了 损失了好几个field count。目前排名处于吊车尾。
昨日sa。提交的eur pc 0.49。 给了44刀，还需要努力，继续加油！！！
=================================================================
=================================================================
=================================================================
=================================================================

---

### 探讨 #87: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

==================================================
==================================================
今天排名掉到41了 可能已经评不上gm了
好好沉淀一个季度吧
==================================================
==================================================

---

### 探讨 #88: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: [Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法.md
- **评论时间**: 1 year ago

**为了让相关性更低可以使用以下这些参数分成不同的层级，去筛选完全不一样的因子。** 
 **也可以取部分交集，自我微调。选择其中的一个叠加相同的条件就可以筛选出完全不一样的因子，在遍历neut 找到最低的pc 然后继续微调。**

- **selection：**
- 0.01<turnover<0.05
- 0.05<turnover<0.1
- 0.1<turnover<0.15
- ....
- 0.1<prod_corr<0.4
- 0.4<prod_corr<0.45
- 0.45<prod_corr<0.5
- ...
- ....
- op_count<3
- 3<op_count<5
- 5<op_count<8
- ....

---

### 探讨 #89: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md
- **评论时间**: 1年前

**为了让相关性更低可以使用以下这些参数分成不同的层级，去筛选完全不一样的因子。** 
 **也可以取部分交集，自我微调。选择其中的一个叠加相同的条件就可以筛选出完全不一样的因子，在遍历neut 找到最低的pc 然后继续微调。**

- **selection：**
- 0.01<turnover<0.05
- 0.05<turnover<0.1
- 0.1<turnover<0.15
- ....
- 0.1<prod_corr<0.4
- 0.4<prod_corr<0.45
- 0.45<prod_corr<0.5
- ...
- ....
- op_count<3
- 3<op_count<5
- 5<op_count<8
- ....

---

### 探讨 #90: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【经验分享】如何从expert直升GM经验分享.md
- **评论时间**: 3个月前

你真的太强了！！！！

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #91: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】如何从expert直升GM经验分享_38320422749463.md
- **评论时间**: 4个月前

你真的太强了！！！！

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #92: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享_38932709256727.md
- **评论时间**: 1个月前

==================================================================================
Life is about waiting for the right moment to act.So, RELAX.You’re not LATE. You’re not EARLY.
You are very much ON TIME, and in your, TIME ZONE Destiny set up for you.
==================================================================================

---

### 探讨 #93: 关于《【经验分享】新人如何Combine 2.3， VF 0.9经验分享》的评论回复
- **帖子链接**: [Commented] 【经验分享】新人如何Combine 23 VF 09经验分享.md
- **评论时间**: 3个月前

学会了，感谢大佬的分享，祝您新年快乐

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #94: 关于《【经验分享】新人如何Combine 2.3， VF 0.9经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】新人如何Combine 23 VF 09经验分享_38376574647447.md
- **评论时间**: 4个月前

学会了，感谢大佬的分享，祝您新年快乐

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #95: 关于《一文搞懂过拟合与欠拟合！！！》的评论回复
- **帖子链接**: [Commented] 一文搞懂过拟合与欠拟合.md
- **评论时间**: 1年前

感谢楼主的科普，在我们研究alpha时，为了让alpha过及格线不断的去增添一些不必要的op是不是就是典型的过拟合，而表现不错的alpha为了降低六维的op avg 删除一些让表现不稳定就是欠拟合。
================================================================

================================================================

---

### 探讨 #96: 关于《一文搞懂过拟合与欠拟合！！！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 一文搞懂过拟合与欠拟合_32989182997399.md
- **评论时间**: 1年前

感谢楼主的科普，在我们研究alpha时，为了让alpha过及格线不断的去增添一些不必要的op是不是就是典型的过拟合，而表现不错的alpha为了降低六维的op avg 删除一些让表现不稳定就是欠拟合。
================================================================

================================================================

---

### 探讨 #97: 关于《█████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享》的评论回复
- **帖子链接**: [Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享.md
- **评论时间**: 1年前

强如毛老师也有ra 不到5的时候，感觉还是得靠sa赚钱，但是作为一个gold ，只能望sa兴叹。

---

### 探讨 #98: 关于《█████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **评论时间**: 1 year ago

强如毛老师也有ra 不到5的时候，感觉还是得靠sa赚钱，但是作为一个gold ，只能望sa兴叹。

---

### 探讨 #99: 关于《使用Deepseek基于自建知识库进行alpha解析/模板构建——以腾讯ima为例经验分享》的评论回复
- **帖子链接**: [Commented] 使用Deepseek基于自建知识库进行alpha解析模板构建以腾讯ima为例经验分享.md
- **评论时间**: 1年前

HW93328，你好！
感谢你的分享，你这个帖子分享的内容很实用呀。我注意到你提到知识库中有一篇研报，想问一下，你是怎么把研报的内容融入到知识库中的呢？是直接把研报的文本内容复制进去，还是进行了提炼和总结呢？还有，你觉得研报在知识库中起到的作用主要是提供灵感，还是说还能在其他方面发挥作用呢？因为我是一个外行，看不懂这个研报，看了你的帖子，我也打算尝试尝试去构建自己的知识库，所以想多了解一些这方面的经验，希望能得到你的指点。
期待你的回复，祝你base多多！！！

---

### 探讨 #100: 关于《使用Deepseek基于自建知识库进行alpha解析/模板构建——以腾讯ima为例经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 使用Deepseek基于自建知识库进行alpha解析模板构建以腾讯ima为例经验分享_32093316146455.md
- **评论时间**: 1年前

HW93328，你好！
感谢你的分享，你这个帖子分享的内容很实用呀。我注意到你提到知识库中有一篇研报，想问一下，你是怎么把研报的内容融入到知识库中的呢？是直接把研报的文本内容复制进去，还是进行了提炼和总结呢？还有，你觉得研报在知识库中起到的作用主要是提供灵感，还是说还能在其他方面发挥作用呢？因为我是一个外行，看不懂这个研报，看了你的帖子，我也打算尝试尝试去构建自己的知识库，所以想多了解一些这方面的经验，希望能得到你的指点。
期待你的回复，祝你base多多！！！

---

### 探讨 #101: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 关于降Prod Correlation的实践一经验分享_39118594803095.md
- **评论时间**: 1个月前

算数操作符降低pc  arc sin arc cos arc tan以及tanh  效果都会有一些

======================================================================
sharpe is ts_delta and ts_delta but returns ts_delay and ts_delay.
======================================================================
sharpe is ts_delta and ts_delta but returns ts_delay and ts_delay.

---

### 探讨 #102: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化.md
- **评论时间**: 7个月前

感谢大佬的分享！！！！

国区大佬越来越多，无私的开源分享精神会让国区越来越强

下个季度回测数量被压缩，一定要用好ai去筛掉无效回测。太感谢了

============================================================================================================================================================================================================================================================

---

### 探讨 #103: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化_36196107273879.md
- **评论时间**: 7个月前

感谢大佬的分享！！！！

国区大佬越来越多，无私的开源分享精神会让国区越来越强

下个季度回测数量被压缩，一定要用好ai去筛掉无效回测。太感谢了

============================================================================================================================================================================================================================================================

---

### 探讨 #104: 关于《%% [markdown]登录%%def sign_in():    import requests    from time import sleep    Initialize variables to hold the username and password    #--------------------WARNING--------------------    username = "xxxxx@xxxxx.com"  NEVER SHARE YOUR USERNAME AND PASSWORD    password = "xxxxxxxxxxxxxx"   NEVER SHARE YOUR USERNAME AND PASSWORD    #--------------------WARNING--------------------    Create a session to persistently store the headers    s = requests.Session()    Save credentials into the session    s.auth = (username, password)    while True:        try:            Send a POST request to the /authentication API            response = s.post('https://api.worldquantbrain.com/authentication')            response.raise_for_status()  Raises a HTTPError if the status is 4xx, 5xx            print("Authentication successful.")            break  Exit the loop on success        except requests.HTTPError as e:            print(f"HTTP error occurred: {e}. Retrying...")  Provide more specific error message            sleep(10)        except Exception as e:            print(f"Error during authentication: {e}. Trying to login again.")            sleep(10)    return ssession = sign_in()%% [markdown]下载历史表现%%Function to fetch a specific number of IS alphas (`total_alphas`) using pagination.def get_n_os_alphas(session, total_alphas, limit=100):    fetched_alphas = []    offset = 0    Keep fetching alphas until the required number of alphas is reached or no more alphas are available.    while len(fetched_alphas) < total_alphas:        response = session.get(            f"https://api.worldquantbrain.com/users/self/alphas?stage=OS&limit={limit}&offset={offset}"        )        alphas = response.json()["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit    return fetched_alphas[:total_alphas]alpha_list_submitted = get_n_os_alphas(session, 3000)%%dump the alpha list to a JSON fileimport jsonwith open('alpha_list_submitted.json', 'w') as f:    json.dump(alpha_list_submitted, f, indent=4)%%len(alpha_list_submitted)make it to a dataframeimport pandas as pddf_alpha_list_submitted = pd.DataFrame(alpha_list_submitted)save the%% [markdown]分析1：Alpha分布图%%对于每一个region，我们画出一个直方图，展示Sharpe, turnover, return, margin, fitness每个region画一个大图，里面由相应的小图组成import matplotlib.pyplot as pltimport seaborn as snsimport numpy as npimport matplotlib.gridspec as gridspecimport matplotlib.cm as cmimport matplotlib.colors as mcolorsimport matplotlib.ticker as tickerimport matplotlib.patches as mpatcheseach alpha is a row in the dataframe, and we can get the region from the settings column Index seetings, where it is a dic and there is a key value for 'region'for each alpha, we can have performance in IS and OS, we look at the IS performance firstdef get_region(alpha_list_submitted, region):    filter the alpha_list_submitted dataframe by region    df_region = alpha_list_submitted[alpha_list_submitted['settings'].apply(lambda x: x['region'] == region)]    return df_regiondef get_performance(df_region, performance_type):    filter the performance type from the dataframe    df_performance = df_region[performance_type]    return df_performancedef get_performance_metrics(df_performance):    extract the performance metrics from the dataframe    sharpe = df_performance.apply(lambda x: x.get('sharpe', np.nan))    turnover = df_performance.apply(lambda x: x.get('turnover', np.nan))    returns = df_performance.apply(lambda x: x.get('returns', np.nan))    margin = df_performance.apply(lambda x: x.get('margin', np.nan))    fitness = df_performance.apply(lambda x: x.get('fitness', np.nan))    return sharpe, turnover, returns, margin, fitnessdef plot_performance_metrics(sharpe, turnover, returns, margin, fitness, region):    set up the figure and axes for the subplots    fig = plt.figure(figsize=(15, 10))    gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])    ax0 = fig.add_subplot(gs[0, 0])    ax1 = fig.add_subplot(gs[0, 1])    ax2 = fig.add_subplot(gs[1, 0])    ax3 = fig.add_subplot(gs[1, 1])    ax4 = fig.add_subplot(gs[2, :])    plot the histograms for each metric    sns.histplot(sharpe, bins=20, kde=True, ax=ax0)    sns.histplot(turnover, bins=20, kde=True, ax=ax1)    sns.histplot(returns, bins=20, kde=True, ax=ax2)    sns.histplot(margin, bins=20, kde=True, ax=ax3)    sns.histplot(fitness, bins=20, kde=True, ax=ax4)    set titles and labels for each subplot    ax0.set_title(f'Sharpe Ratio Distribution in {region}')    ax1.set_title(f'Turnover Distribution in {region}')    ax2.set_title(f'Returns Distribution in {region}')    ax3.set_title(f'Margin Distribution in {region}')    ax4.set_title(f'Fitness Distribution in {region}')    plt.tight_layout()    plt.show()def plot_is_os_performance_matrix(df_is_performance, df_os_performance, region):    extract the performance metrics for IS and OS    sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)    sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)    for the same histpolot, we will put the IS and OS performance in the same histogram, we can use different color for the IS and OS performance    set up the figure and axes for the subplots    fig = plt.figure(figsize=(15, 10))    gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])    ax0 = fig.add_subplot(gs[0, 0])    ax1 = fig.add_subplot(gs[0, 1])    ax2 = fig.add_subplot(gs[1, 0])    ax3 = fig.add_subplot(gs[1, 1])    ax4 = fig.add_subplot(gs[2, :])    plot the histograms for each metric    sns.histplot(sharpe_is, bins=20, kde=True, ax=ax0, color='blue', label='IS')    sns.histplot(sharpe_os, bins=20, kde=True, ax=ax0, color='orange', label='OS')    set the x-label to be the same for both IS and OS    ax0.set_xlabel('Sharpe Ratio')    ax0.legend()    sns.histplot(turnover_is, bins=20, kde=True, ax=ax1, color='blue', label='IS')    sns.histplot(turnover_os, bins=20, kde=True, ax=ax1, color='orange', label='OS')    ax1.set_xlabel('Turnover')    ax1.legend()    sns.histplot(returns_is, bins=20, kde=True, ax=ax2, color='blue', label='IS')    sns.histplot(returns_os, bins=20, kde=True, ax=ax2, color='orange', label='OS')    ax2.set_xlabel('Returns')    ax2.legend()    sns.histplot(margin_is, bins=20, kde=True, ax=ax3, color='blue', label='IS')    sns.histplot(margin_os, bins=20, kde=True, ax=ax3, color='orange', label='OS')    ax3.set_xlabel('Margin')    ax3.legend()    sns.histplot(fitness_is, bins=20, kde=True, ax=ax4, color='blue', label='IS')    sns.histplot(fitness_os, bins=20, kde=True, ax=ax4, color='orange', label='OS')    ax4.set_xlabel('Fitness')    ax4.legend()       set titles and labels for each subplot    ax0.set_title(f'Sharpe Ratio Distribution in {region}')    ax1.set_title(f'Turnover Distribution in {region}')    ax2.set_title(f'Returns Distribution in {region}')    ax3.set_title(f'Margin Distribution in {region}')    ax4.set_title(f'Fitness Distribution in {region}')    plt.tight_layout()    plt.show()获取不同region，并画出不同region的performanceregions = df_alpha_list_submitted['settings'].apply(lambda x: x['region']).unique()for region in regions:    df_region = get_region(df_alpha_list_submitted, region)    df_is_performance = get_performance(df_region, 'is')    df_os_performance = get_performance(df_region, 'os')    sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)    sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)    plot_is_os_performance_matrix(df_is_performance, df_os_performance, region)%% [markdown]分析2：Alpha趋势分布图%%画出一个不同matric跟Sharpe的散点图，并拟合出一条线，展示不同的performance跟Sharpe的关系import matplotlib.pyplot as pltimport seaborn as snsimport numpy as npimport matplotlib.gridspec as gridspecimport matplotlib.cm as cmregion = 'USA'df_region = get_region(df_alpha_list_submitted, region)df_is_performance = get_performance(df_region, 'is')df_os_performance = get_performance(df_region, 'os')sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)define a function, the take in is the sharpe_os, turnover_os, returns_os, margin_os, fitness_os; sharpe_is, turnover_is, returns_is, margin_is, fitness_isthere should be 5 subplots, and each subplot should be a scatter plot, and the x-axis is the sharpe, and the y-axis is the other performance metricsfor each subplot, show both IS and OS performance, and use different color for IS and OS performancedef plot_sharpe_vs_performance(sharpe_os, turnover_os, returns_os, margin_os, fitness_os, sharpe_is, turnover_is, returns_is, margin_is, fitness_is,region):    set up the figure and axes for the subplots    fig = plt.figure(figsize=(15, 10))    gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])    ax0 = fig.add_subplot(gs[0, 0])    ax1 = fig.add_subplot(gs[0, 1])    ax2 = fig.add_subplot(gs[1, 0])    ax3 = fig.add_subplot(gs[1, 1])    ax4 = fig.add_subplot(gs[2, :])    plot the scatter plots for each metric    sns.scatterplot(x=sharpe_os, y=turnover_os, ax=ax0, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=turnover_is, ax=ax0, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=turnover_os, ax=ax0, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=turnover_is, ax=ax0, scatter=False, color='blue')    ax0.set_xlabel('Sharpe Ratio')    ax0.set_ylabel('Turnover')    ax0.legend()    ax0.set_title(f'Sharpe Ratio vs Turnover in {region}')    sns.scatterplot(x=sharpe_os, y=returns_os, ax=ax1, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=returns_is, ax=ax1, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=returns_os, ax=ax1, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=returns_is, ax=ax1, scatter=False, color='blue')    ax1.set_xlabel('Sharpe Ratio')    ax1.set_ylabel('Returns')    ax1.legend()    ax1.set_title(f'Sharpe Ratio vs Returns in {region}')       sns.scatterplot(x=sharpe_os, y=margin_os, ax=ax2, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=margin_is, ax=ax2, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=margin_os, ax=ax2, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=margin_is, ax=ax2, scatter=False, color='blue')    ax2.set_xlabel('Sharpe Ratio')    ax2.set_ylabel('Margin')    ax2.legend()    ax2.set_title(f'Sharpe Ratio vs Margin in {region}')    sns.scatterplot(x=sharpe_os, y=fitness_os, ax=ax3, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=fitness_is, ax=ax3, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=fitness_os, ax=ax3, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=fitness_is, ax=ax3, scatter=False, color='blue')    ax3.set_xlabel('Sharpe Ratio')    ax3.set_ylabel('Fitness')    ax3.legend()    ax3.set_title(f'Sharpe Ratio vs Fitness in {region}')    sns.scatterplot(x=sharpe_os, y=sharpe_is, ax=ax4, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=sharpe_is, ax=ax4, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=sharpe_is, ax=ax4, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=sharpe_is, ax=ax4, scatter=False, color='blue')    ax4.set_xlabel('Sharpe Ratio OS')    ax4.set_ylabel('Sharpe Ratio IS')    ax4.legend()    ax4.set_title(f'Sharpe Ratio OS vs Sharpe Ratio IS in {region}')    plt.tight_layout()    plt.show()Example usageregion = 'USA'plot_sharpe_vs_performance(sharpe_os, turnover_os, returns_os, margin_os, fitness_os, sharpe_is, turnover_is, returns_is, margin_is, fitness_is, region)获取不同region，并画出不同region的performanceregions = df_alpha_list_submitted['settings'].apply(lambda x: x['region']).unique()for region in regions:    df_region = get_region(df_alpha_list_submitted, region)    df_is_performance = get_performance(df_region, 'is')    df_os_performance = get_performance(df_region, 'os')    sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)    sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)    plot_sharpe_vs_performance(sharpe_os, turnover_os, returns_os, margin_os, fitness_os, sharpe_is, turnover_is, returns_is, margin_is, fitness_is, region)%% [markdown]分析3：数据字段使用情况（分区域图）%% [markdown]![image.png](attachment:image.png)%% [markdown]![image.png](attachment:image.png)%% [markdown]![image.png](attachment:image.png)%% [markdown]总结反思》的评论回复
- **帖子链接**: [Commented] 历史Alpha可视化工具代码优化.md
- **评论时间**: 1年前

==============================================================================
==============================================================================
非常好用的一个功能，可以分地区多指标的呈现出历史的alpha信息，希望大家都配置起来，提升效率。
==============================================================================

---

### 探讨 #105: 关于《%% [markdown]登录%%def sign_in():    import requests    from time import sleep    Initialize variables to hold the username and password    #--------------------WARNING--------------------    username = "xxxxx@xxxxx.com"  NEVER SHARE YOUR USERNAME AND PASSWORD    password = "xxxxxxxxxxxxxx"   NEVER SHARE YOUR USERNAME AND PASSWORD    #--------------------WARNING--------------------    Create a session to persistently store the headers    s = requests.Session()    Save credentials into the session    s.auth = (username, password)    while True:        try:            Send a POST request to the /authentication API            response = s.post('https://api.worldquantbrain.com/authentication')            response.raise_for_status()  Raises a HTTPError if the status is 4xx, 5xx            print("Authentication successful.")            break  Exit the loop on success        except requests.HTTPError as e:            print(f"HTTP error occurred: {e}. Retrying...")  Provide more specific error message            sleep(10)        except Exception as e:            print(f"Error during authentication: {e}. Trying to login again.")            sleep(10)    return ssession = sign_in()%% [markdown]下载历史表现%%Function to fetch a specific number of IS alphas (`total_alphas`) using pagination.def get_n_os_alphas(session, total_alphas, limit=100):    fetched_alphas = []    offset = 0    Keep fetching alphas until the required number of alphas is reached or no more alphas are available.    while len(fetched_alphas) < total_alphas:        response = session.get(            f"https://api.worldquantbrain.com/users/self/alphas?stage=OS&limit={limit}&offset={offset}"        )        alphas = response.json()["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit    return fetched_alphas[:total_alphas]alpha_list_submitted = get_n_os_alphas(session, 3000)%%dump the alpha list to a JSON fileimport jsonwith open('alpha_list_submitted.json', 'w') as f:    json.dump(alpha_list_submitted, f, indent=4)%%len(alpha_list_submitted)make it to a dataframeimport pandas as pddf_alpha_list_submitted = pd.DataFrame(alpha_list_submitted)save the%% [markdown]分析1：Alpha分布图%%对于每一个region，我们画出一个直方图，展示Sharpe, turnover, return, margin, fitness每个region画一个大图，里面由相应的小图组成import matplotlib.pyplot as pltimport seaborn as snsimport numpy as npimport matplotlib.gridspec as gridspecimport matplotlib.cm as cmimport matplotlib.colors as mcolorsimport matplotlib.ticker as tickerimport matplotlib.patches as mpatcheseach alpha is a row in the dataframe, and we can get the region from the settings column Index seetings, where it is a dic and there is a key value for 'region'for each alpha, we can have performance in IS and OS, we look at the IS performance firstdef get_region(alpha_list_submitted, region):    filter the alpha_list_submitted dataframe by region    df_region = alpha_list_submitted[alpha_list_submitted['settings'].apply(lambda x: x['region'] == region)]    return df_regiondef get_performance(df_region, performance_type):    filter the performance type from the dataframe    df_performance = df_region[performance_type]    return df_performancedef get_performance_metrics(df_performance):    extract the performance metrics from the dataframe    sharpe = df_performance.apply(lambda x: x.get('sharpe', np.nan))    turnover = df_performance.apply(lambda x: x.get('turnover', np.nan))    returns = df_performance.apply(lambda x: x.get('returns', np.nan))    margin = df_performance.apply(lambda x: x.get('margin', np.nan))    fitness = df_performance.apply(lambda x: x.get('fitness', np.nan))    return sharpe, turnover, returns, margin, fitnessdef plot_performance_metrics(sharpe, turnover, returns, margin, fitness, region):    set up the figure and axes for the subplots    fig = plt.figure(figsize=(15, 10))    gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])    ax0 = fig.add_subplot(gs[0, 0])    ax1 = fig.add_subplot(gs[0, 1])    ax2 = fig.add_subplot(gs[1, 0])    ax3 = fig.add_subplot(gs[1, 1])    ax4 = fig.add_subplot(gs[2, :])    plot the histograms for each metric    sns.histplot(sharpe, bins=20, kde=True, ax=ax0)    sns.histplot(turnover, bins=20, kde=True, ax=ax1)    sns.histplot(returns, bins=20, kde=True, ax=ax2)    sns.histplot(margin, bins=20, kde=True, ax=ax3)    sns.histplot(fitness, bins=20, kde=True, ax=ax4)    set titles and labels for each subplot    ax0.set_title(f'Sharpe Ratio Distribution in {region}')    ax1.set_title(f'Turnover Distribution in {region}')    ax2.set_title(f'Returns Distribution in {region}')    ax3.set_title(f'Margin Distribution in {region}')    ax4.set_title(f'Fitness Distribution in {region}')    plt.tight_layout()    plt.show()def plot_is_os_performance_matrix(df_is_performance, df_os_performance, region):    extract the performance metrics for IS and OS    sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)    sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)    for the same histpolot, we will put the IS and OS performance in the same histogram, we can use different color for the IS and OS performance    set up the figure and axes for the subplots    fig = plt.figure(figsize=(15, 10))    gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])    ax0 = fig.add_subplot(gs[0, 0])    ax1 = fig.add_subplot(gs[0, 1])    ax2 = fig.add_subplot(gs[1, 0])    ax3 = fig.add_subplot(gs[1, 1])    ax4 = fig.add_subplot(gs[2, :])    plot the histograms for each metric    sns.histplot(sharpe_is, bins=20, kde=True, ax=ax0, color='blue', label='IS')    sns.histplot(sharpe_os, bins=20, kde=True, ax=ax0, color='orange', label='OS')    set the x-label to be the same for both IS and OS    ax0.set_xlabel('Sharpe Ratio')    ax0.legend()    sns.histplot(turnover_is, bins=20, kde=True, ax=ax1, color='blue', label='IS')    sns.histplot(turnover_os, bins=20, kde=True, ax=ax1, color='orange', label='OS')    ax1.set_xlabel('Turnover')    ax1.legend()    sns.histplot(returns_is, bins=20, kde=True, ax=ax2, color='blue', label='IS')    sns.histplot(returns_os, bins=20, kde=True, ax=ax2, color='orange', label='OS')    ax2.set_xlabel('Returns')    ax2.legend()    sns.histplot(margin_is, bins=20, kde=True, ax=ax3, color='blue', label='IS')    sns.histplot(margin_os, bins=20, kde=True, ax=ax3, color='orange', label='OS')    ax3.set_xlabel('Margin')    ax3.legend()    sns.histplot(fitness_is, bins=20, kde=True, ax=ax4, color='blue', label='IS')    sns.histplot(fitness_os, bins=20, kde=True, ax=ax4, color='orange', label='OS')    ax4.set_xlabel('Fitness')    ax4.legend()       set titles and labels for each subplot    ax0.set_title(f'Sharpe Ratio Distribution in {region}')    ax1.set_title(f'Turnover Distribution in {region}')    ax2.set_title(f'Returns Distribution in {region}')    ax3.set_title(f'Margin Distribution in {region}')    ax4.set_title(f'Fitness Distribution in {region}')    plt.tight_layout()    plt.show()获取不同region，并画出不同region的performanceregions = df_alpha_list_submitted['settings'].apply(lambda x: x['region']).unique()for region in regions:    df_region = get_region(df_alpha_list_submitted, region)    df_is_performance = get_performance(df_region, 'is')    df_os_performance = get_performance(df_region, 'os')    sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)    sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)    plot_is_os_performance_matrix(df_is_performance, df_os_performance, region)%% [markdown]分析2：Alpha趋势分布图%%画出一个不同matric跟Sharpe的散点图，并拟合出一条线，展示不同的performance跟Sharpe的关系import matplotlib.pyplot as pltimport seaborn as snsimport numpy as npimport matplotlib.gridspec as gridspecimport matplotlib.cm as cmregion = 'USA'df_region = get_region(df_alpha_list_submitted, region)df_is_performance = get_performance(df_region, 'is')df_os_performance = get_performance(df_region, 'os')sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)define a function, the take in is the sharpe_os, turnover_os, returns_os, margin_os, fitness_os; sharpe_is, turnover_is, returns_is, margin_is, fitness_isthere should be 5 subplots, and each subplot should be a scatter plot, and the x-axis is the sharpe, and the y-axis is the other performance metricsfor each subplot, show both IS and OS performance, and use different color for IS and OS performancedef plot_sharpe_vs_performance(sharpe_os, turnover_os, returns_os, margin_os, fitness_os, sharpe_is, turnover_is, returns_is, margin_is, fitness_is,region):    set up the figure and axes for the subplots    fig = plt.figure(figsize=(15, 10))    gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])    ax0 = fig.add_subplot(gs[0, 0])    ax1 = fig.add_subplot(gs[0, 1])    ax2 = fig.add_subplot(gs[1, 0])    ax3 = fig.add_subplot(gs[1, 1])    ax4 = fig.add_subplot(gs[2, :])    plot the scatter plots for each metric    sns.scatterplot(x=sharpe_os, y=turnover_os, ax=ax0, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=turnover_is, ax=ax0, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=turnover_os, ax=ax0, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=turnover_is, ax=ax0, scatter=False, color='blue')    ax0.set_xlabel('Sharpe Ratio')    ax0.set_ylabel('Turnover')    ax0.legend()    ax0.set_title(f'Sharpe Ratio vs Turnover in {region}')    sns.scatterplot(x=sharpe_os, y=returns_os, ax=ax1, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=returns_is, ax=ax1, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=returns_os, ax=ax1, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=returns_is, ax=ax1, scatter=False, color='blue')    ax1.set_xlabel('Sharpe Ratio')    ax1.set_ylabel('Returns')    ax1.legend()    ax1.set_title(f'Sharpe Ratio vs Returns in {region}')       sns.scatterplot(x=sharpe_os, y=margin_os, ax=ax2, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=margin_is, ax=ax2, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=margin_os, ax=ax2, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=margin_is, ax=ax2, scatter=False, color='blue')    ax2.set_xlabel('Sharpe Ratio')    ax2.set_ylabel('Margin')    ax2.legend()    ax2.set_title(f'Sharpe Ratio vs Margin in {region}')    sns.scatterplot(x=sharpe_os, y=fitness_os, ax=ax3, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=fitness_is, ax=ax3, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=fitness_os, ax=ax3, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=fitness_is, ax=ax3, scatter=False, color='blue')    ax3.set_xlabel('Sharpe Ratio')    ax3.set_ylabel('Fitness')    ax3.legend()    ax3.set_title(f'Sharpe Ratio vs Fitness in {region}')    sns.scatterplot(x=sharpe_os, y=sharpe_is, ax=ax4, color='orange', label='OS')    sns.scatterplot(x=sharpe_is, y=sharpe_is, ax=ax4, color='blue', label='IS')    sns.regplot(x=sharpe_os, y=sharpe_is, ax=ax4, scatter=False, color='orange')    sns.regplot(x=sharpe_is, y=sharpe_is, ax=ax4, scatter=False, color='blue')    ax4.set_xlabel('Sharpe Ratio OS')    ax4.set_ylabel('Sharpe Ratio IS')    ax4.legend()    ax4.set_title(f'Sharpe Ratio OS vs Sharpe Ratio IS in {region}')    plt.tight_layout()    plt.show()Example usageregion = 'USA'plot_sharpe_vs_performance(sharpe_os, turnover_os, returns_os, margin_os, fitness_os, sharpe_is, turnover_is, returns_is, margin_is, fitness_is, region)获取不同region，并画出不同region的performanceregions = df_alpha_list_submitted['settings'].apply(lambda x: x['region']).unique()for region in regions:    df_region = get_region(df_alpha_list_submitted, region)    df_is_performance = get_performance(df_region, 'is')    df_os_performance = get_performance(df_region, 'os')    sharpe_os, turnover_os, returns_os, margin_os, fitness_os = get_performance_metrics(df_os_performance)    sharpe_is, turnover_is, returns_is, margin_is, fitness_is = get_performance_metrics(df_is_performance)    plot_sharpe_vs_performance(sharpe_os, turnover_os, returns_os, margin_os, fitness_os, sharpe_is, turnover_is, returns_is, margin_is, fitness_is, region)%% [markdown]分析3：数据字段使用情况（分区域图）%% [markdown]![image.png](attachment:image.png)%% [markdown]![image.png](attachment:image.png)%% [markdown]![image.png](attachment:image.png)%% [markdown]总结反思》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 历史Alpha可视化工具代码优化_32602329306775.md
- **评论时间**: 1年前

==============================================================================
==============================================================================
非常好用的一个功能，可以分地区多指标的呈现出历史的alpha信息，希望大家都配置起来，提升效率。
==============================================================================

---

### 探讨 #106: 关于《print(pools[0])》的评论回复
- **帖子链接**: [Commented] 多线程遍历回测super alpha代码优化.md
- **评论时间**: 1 year ago

=================================================================
=================================================================
感谢大佬，祝愿大佬继续高base 高VF. 得偿所愿
=================================================================
=================================================================

---

### 探讨 #107: 关于《print(pools[0])》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 多线程遍历回测super alpha代码优化_31527668843671.md
- **评论时间**: 1年前

=================================================================
=================================================================
感谢大佬，祝愿大佬继续高base 高VF. 得偿所愿
=================================================================
=================================================================

---

### 探讨 #108: 关于《大家IQC都拿了多少钱啊？来写写日记吧》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgX5jc5ABw6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAddodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzA3ODcyODU1NDI0MjMtJUU1JUE0JUE3JUU1JUFFJUI2SVFDJUU5JTgzJUJEJUU2JThCJUJGJUU0JUJBJTg2JUU1JUE0JTlBJUU1JUIwJTkxJUU5JTkyJUIxJUU1JTk1JThBLSVFNiU5RCVBNSVFNSU4NiU5OSVFNSU4NiU5OSVFNiU5NyVBNSVFOCVBRSVCMCVFNSU5MCVBNwY7CFQ6DnNlYXJjaF9pZEkiKTMxYWQ4NzcwLTQwNmEtNGUyYS1hOWE1LTliNDZjY2VlN2M3YwY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDE1HODg1OTIGOwhUOhJyZXN1bHRzX2NvdW50aRo%3D--f2b7c3adf39e748091f2397ee72aed1e933a668f
- **评论时间**: 1年前

感觉IQC质量做的好，轻轻松松几十刀，比万年gold 好太多了

---

### 探讨 #109: 关于《大家IQC都拿了多少钱啊？来写写日记吧》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 大家IQC都拿了多少钱啊来写写日记吧_30787285542423.md
- **评论时间**: 1年前

感觉IQC质量做的好，轻轻松松几十刀，比万年gold 好太多了

---

### 探讨 #110: 关于《我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化》的评论回复
- **帖子链接**: [Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化.md
- **评论时间**: 1年前

非常有用的分享，想问一下楼主，这个ai给出的表达式你进行批量回测了吗？
效果咋样哇！！！！
====================================
====================================
====================================

---

### 探讨 #111: 关于《我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化_33016862088599.md
- **评论时间**: 1年前

非常有用的分享，想问一下楼主，这个ai给出的表达式你进行批量回测了吗？
效果咋样哇！！！！
====================================
====================================
====================================

---

### 探讨 #112: 关于《新手一个多月提交147个alpha的经验总结》的评论回复
- **帖子链接**: [Commented] 新手一个多月提交147个alpha的经验总结.md
- **评论时间**: 1年前

如果一直交一些质量不高的因子 那payment好像会很低，请问楼主目前basepay是多少，valuefactor是多少。

---

### 探讨 #113: 关于《新手一个多月提交147个alpha的经验总结》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 新手一个多月提交147个alpha的经验总结_29878528858135.md
- **评论时间**: 1年前

如果一直交一些质量不高的因子 那payment好像会很低，请问楼主目前basepay是多少，valuefactor是多少。

---

### 探讨 #114: 关于《增量下载数据download_data(flag_increment=True)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md
- **评论时间**: 1 year ago

=================================================================
=================================================================
感谢华博士，最近尝试将华子哥的代码加进自己的check代码中，现在放进ppa中检查，真的是非常流畅
=================================================================
=================================================================

---

### 探讨 #115: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 经验分享-Combine提升之路-过山车的经历真刺激从负数到2的来时路_39330854528151.md
- **评论时间**: 1个月前

记忆中mike哥一路走来是崎岖坎坷的，好在走出来了。
恭喜Mike老哥成功逆袭，从combine、vf双负到双高，这离不开老哥的不懈坚持和创新，也祝老哥combine、vf越来越高，加油！

====================================================================

---

### 探讨 #116: 关于《解决网页出现"WorldQuant BRAIN is experiencing some difficulties"导致的回测中断代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX3kIMKx46D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAfVodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzMxNzAyMzgxMzU5NTktJUU4JUE3JUEzJUU1JTg2JUIzJUU3JUJEJTkxJUU5JUExJUI1JUU1JTg3JUJBJUU3JThFJUIwLVdvcmxkUXVhbnQtQlJBSU4taXMtZXhwZXJpZW5jaW5nLXNvbWUtZGlmZmljdWx0aWVzLSVFNSVBRiVCQyVFOCU4NyVCNCVFNyU5QSU4NCVFNSU5QiU5RSVFNiVCNSU4QiVFNCVCOCVBRCVFNiU5NiVBRAY7CFQ6DnNlYXJjaF9pZEkiKTMxYWQ4NzcwLTQwNmEtNGUyYS1hOWE1LTliNDZjY2VlN2M3YwY7CEY6CXJhbmtpCToLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDE1HODg1OTIGOwhUOhJyZXN1bHRzX2NvdW50aRo%3D--897f3c4d41186c5fef4125b2fa8107d357dcd9b9
- **评论时间**: 1年前

感谢大佬的分享！！！！！！！

---

### 探讨 #117: 关于《解决网页出现"WorldQuant BRAIN is experiencing some difficulties"导致的回测中断代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 解决网页出现WorldQuant BRAIN is experiencing some difficulties导致的回测中断代码优化_33170238135959.md
- **评论时间**: 1年前

感谢大佬的分享！！！！！！！

---

### 探讨 #118: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 适合邮箱自动推送的平台信息经验分享.md
- **评论时间**: 3个月前

感谢大佬的分享，祝您新年快乐

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 探讨 #119: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 适合邮箱自动推送的平台信息经验分享_38472629440407.md
- **评论时间**: 4个月前

感谢大佬的分享，祝您新年快乐

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---
