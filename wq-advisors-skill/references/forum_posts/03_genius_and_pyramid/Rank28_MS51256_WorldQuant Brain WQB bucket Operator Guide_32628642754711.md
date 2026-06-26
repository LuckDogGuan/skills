# WorldQuant Brain (WQB) bucket Operator Guide

- **链接**: https://support.worldquantbrain.comWorldQuant Brain WQB bucket Operator Guide_32628642754711.md
- **作者**: 顾问 MS51256 (Rank 28)
- **发布时间/热度**: 1年前, 得票: 55

## 帖子正文

The  `bucket`  operator in  **WorldQuant Brain (WQB)**  is used for binning numerical data, similar to  `pd.cut`  or  `pd.qcut`  in Python. It maps values into specified bins and returns the corresponding bin labels.

## **Two Main Ways to Use  `bucket`**

### **1. Uniform Binning ( `range`  parameter)**

**Syntax:**

```
bucket(rank(x), range="min, max, step")
```

- **`min`** : Starting value (lower bound).
- **`max`** : Ending value (upper bound).
- **`step`** : Bin width (interval size).

**Example:**

```
# Bins rank(x) into [0, 1] with step=0.1 (bins: 0, 0.1, 0.2, ..., 1.0)
bucket(rank(x), range="0, 1, 0.1")
```

**Output:**

- If  `rank(x) = 0.35`  → assigned to bin  `0.3` .
- If  `rank(x) = 0.89`  → assigned to bin  `0.8` .

### **2. Custom Binning ( `buckets`  parameter)**

**Syntax:**

```
bucket(x, buckets="a,b,c,d,...")
```

- **`buckets`** : Custom bin edges (arbitrary values).
- Data is assigned to intervals:  `[a,b)` ,  `[b,c)` ,  `[c,d)` , etc.

**Example:**

```
# Bins x into custom buckets: 2,5,6,7,10
bucket(x, buckets="2,5,6,7,10")
```

**Output:**

- If  `x = 1`  → returns  `2`  (since  `1 < 2` , defaults to the first edge).
- If  `x = 4`  → returns  `5`  ( `2 ≤ 4 < 5` ).
- If  `x = 6.5`  → returns  `7`  ( `6 ≤ 6.5 < 7` ).
- If  `x = 10`  → returns  `10`  ( `7 ≤ 10 ≤ 10` ).

## **Common Use Cases**

### **1. Uniform Binning (Standardization)**

```
# Normalizes factor values to [0,1] and bins into 10 equal-width intervals
bucket(rank(x), range="0, 1, 0.1")
```

### **2. Custom Grouping (e.g., Market Cap Segmentation)**

```
# Groups stocks by market cap (small, mid, large)
bucket(market_cap, buckets="1e9,1e10,1e11")
```

- `market_cap < 1e9`  →  `1e9`  (small-cap).
- `1e9 ≤ market_cap < 1e10`  →  `1e10`  (mid-cap).
- `market_cap ≥ 1e10`  →  `1e11`  (large-cap).

## **Key Notes**

1. **`rank(x)`  Usage** :
   - `rank(x)`  converts  `x`  into percentile ranks (0~1), making it easier to standardize binning.
   - Without  `rank` ,  `bucket(x, range="...")`  bins raw values directly.
2. **Edge Handling** :
   - Values outside  `range`  or  `buckets`  default to the nearest bin.
   - Example ( `bucket(x, range="0,1,0.1")` ):
   - `x = -0.1`  →  `0` .
   - `x = 1.2`  →  `1` .
3. **Return Value** :
   - Returns the  **right edge**  of the bin (e.g.,  `0.3`  means  `[0.2, 0.3)` ).

## **Summary Table**

Method
Syntax
Use Case

 **Uniform Binning** 
 `bucket(rank(x), range="min,max,step")` 
Standardized binning (e.g., factor normalization)

 **Custom Binning** 
 `bucket(x, buckets="a,b,c,...")` 
Business logic grouping (e.g., market cap t

---

## 讨论与评论 (1)

### 评论 #1 (作者: SK90981, 时间: 1年前)

The bucket operator in WQB efficiently bins numerical data into fixed or custom intervals, aiding factor normalization and smart groupings like market cap segmentation for better alpha modeling.

---

