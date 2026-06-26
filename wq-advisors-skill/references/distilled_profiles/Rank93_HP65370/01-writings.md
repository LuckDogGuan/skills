# 顾问 HP65370 (Rank 93) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 HP65370 (Rank 93) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: Machine Alpha 基础知识1：什么是Alpha模板
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

### 帖子 #2: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #3: 4、 **减少生产相关性**
- **主帖链接**: [L2] Reduce Production Correlations.md
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

### 帖子 #4: 4、 **减少生产相关性**
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

### 帖子 #5: replace 操作符的理解与运用
- **主帖链接**: https://support.worldquantbrain.com[L2] replace 操作符的理解与运用_35191104743447.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #6: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
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

### 帖子 #7: PnL = ∑(Robustness * Creativity)
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

### 帖子 #8: 【分析】Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md
- **讨论数**: 4


> [!NOTE] [图片 OCR 识别内容]
> Wotloquant 启动 !
> 分析1
> 交一个怎样的 & 能提升六维数据之定性定量分析
> IL47973
> 罗超林


[图片 (图片已丢失)]

在定性定量分析六维数据之前，如果你还不知道啥是genius等级和六维数据，建议去看以一下
 [【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板 – WorldQuant BRAIN]([Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md)  这一篇帖子，有解释了genius定级优胜制和六维数据字面意思，为此帖子做铺垫，和有几率增强六维某些数据的小tips；
        当然还有一些所见即所得的alpha 和 邪修alpha模板(没有)，以及包括一些点塔方法，不可否认的是，帖子内容的点塔方法有混塔嫌疑，没事。同上帖子还有一种明显的混塔方式(会多出一至两个op) 以及 一种隐形的 (不完全，存在小幅度扰动) 混塔方式 (至少多出两个op)，当然还有两种 非显非隐 纯点塔 (与混塔毫无干系) 方法，会大程度降低pc，且不会浪费操作符. 能不能看出来并想到就看自己了 .

[图片 (图片已丢失)]

写这个帖子的初衷是来源于 在冲刺genius等级时，我至少是想要保住我的 Operators per Alpha 和 Fields per Alpha 的. 
        有一天 (前两周)，我在操作自己产出的alpha时，发现有些 alpha 的操作符是大于我的 Operators per Alpha 的，此时我就在想，使用自己未使用的操作符作用在此 alpha 上会让此 alpha 信号变得更好时，我应该把 未使用过的操作符 加之在哪里 (操作符少于Operators per Alpha的alpha上还是大于亦或者是等于) 更加合适或者说怎么来降低 Operators per Alpha 的增大程度. [图片 (图片已丢失)]

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 《喜羊羊与灰太狼》
> 中惬意音乐响起令人放松的蟹螺湾椰树


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> )
> 欲将操作符分配与放置于后验&对前验0的平均操作符的变化程度是否有关?


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 第 genius 季度 ,我巳经在 worldquant 上提交了 N 个a, 将这 N 个a
> 按照某种顺序排列 ,便可得到 Q 序列.记为:
> )
> CN.
> 每个Q平均操作符数量 (不重复计数) Nop_per_alpha 计算公式为:
> N
> N
> Operators_count
> OP_per_alpha
> N
> k=1
> Operators_count 表示第k个 a 的操作符数量.
> C1'
> 02
> 03〉
> 其中 Ok



> [!NOTE] [图片 OCR 识别内容]
> 每个Q平均字段数量 (不重复计数) Nfield_per_alpha 计算公式为:
> Nfield_per_alpha
> Fields_count
> N
> k=l
> Fields_count
> 表示第尼个a 的字段数量.
> 其中 0k



> [!NOTE] [图片 OCR 识别内容]
> 记
> alpha 表示衡量 Q 的 OP_per_alpha 的变化程度 ,公式为:
> OP_per_alpha
> abs (OP_per_alphal
> OP_per_alpha)
> 其中 OP_per_alpha' 表示新增 &后的平均操作符数量。
> 现要提交两个&,一个0的操作符数小于X记为 QOperators_count
> 另外一
> N+I
> 个&的操作符数大于孓记为 QOperators_count
> 为了方便起见 ,我们不妨令已经
> 提交的 N 个c的平均操作符数量记为孓 ,现要增加 M 个操作符.
> Dop_per
> N+2



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> X
> 将这 MI 个操作符作用于 QwtI , 记L =孓+
> 此公
> N + 1
> 式一是为了方便观察先后作用,二是简化表达式 ,便会得到
> Ck



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> MI
> 十
> M
> N +1
> (N+I+ _
> N+2)
> OP_per_alpha'
> 二
> Ixtl +
> N + 1
> N + 2
> LNtI
> M+2



> [!NOTE] [图片 OCR 识别内容]
> 将这 M 个操作符作用于 Qwt2 , 会得到



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> MI
> 十
> M
> N +1
> (N+1, N+2T)
> OP_per_alpha'
> Ixt2 + N+I
> N + 2
> Lx+2
> M+I



> [!NOTE] [图片 OCR 识别内容]
> 通过化简 ,可以得到
> (N+It, Nt2) OP_Per_
> alpha
> (N+I,N+t2t) OP_Per_
> alpha'
> 也即
> (N+I+, N+2)
> Aop_per_alpha
> (NtI, N+2+ )
> Aop_per_alpha
> 说明操作符作用于某种类型的 & 并不会改变前验 a 的变化程度 .
> 以上证明也只是能说明操作符全部作用于小于或大于X的 Q, 不会改变
> 前验 Q 变化程度 ,还无法说明作用在等于X身上或每种类型作用若干操作符
> 会不会该改变前验 Q 的变化程度.
  
> [!NOTE] [图片 OCR 识别内容]
> 下面我们直接采用后验来证明操作符无论怎么作用于 Q, 对前验 Q 的变
> 化程度没有任何影响 .
> 若此 genils 季度 ,接下来总共还会交0个a,其中小于 等于和大于孓的
> Q分别有4,e,f个 ,有 def = 0等式成立 ,其等式中省略加法运算符号 ,采
> 用抽代并置表示加法.
  
> [!NOTE] [图片 OCR 识别内容]
> N+a
> N+d+e
> N+dtetf
> Operators_count
> Operators_count
> Operators_count
> 不妨记
> Qk
> :
> Qk
> k=N+I
> k=N+d+I
> k=Ntdtetl



> [!NOTE] [图片 OCR 识别内容]
> 分别表示为小于。等于和大于X的操作符数量之和 .同样地 ,现要增加 I 个操作符.
  
> [!NOTE] [图片 OCR 识别内容]
> N+a+etf
> Aop_per_alpha
> abs
> aOperators_count
> M - 孓.0
> /(N + 0) -孓
> K=N+I



> [!NOTE] [图片 OCR 识别内容]
> 从 Aop_per_alpha 公式可以看出干扰 Q 的 Operators per AIpha 的变化程度
> 跟0的操作符总数量。增加的 M 个操作符数量,
> 此 genius 赛季巳交a和操作符
> 数量有关 ,与这 MI 个操作符如何分配和放置无关 .


[图片 (图片已丢失)]

通过计算知道，将操作符分配与放置于后验alpha对前验alpha的平均操作符变化程度无关 . 
        虽无关，但在操作符对后验alpha影响小时，建议将其放置在性能相对而言不那么好的alpha身上，理应当让好鱼卖一个好的价钱 .

[图片 (图片已丢失)]

[图片 (图片已丢失)]  
> [!NOTE] [图片 OCR 识别内容]
> 《天堂度假村》前前右旁的小草地树林


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 二。六维数据定性分析


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 若两个函数&与h有相同的趋势 ,
> 则认为它们在趋势上对等,记为 8~-h.
> 在不考虑 genils 等级时 ,记 fscore 为个人总得分 , rank 为最终评级得分
> fscore
> rank , 也就是说 fscore 趋势与rank 相同 =
> fscore 便与最终得分有相同的效
> 果可作为最终评分 .
  
> [!NOTE] [图片 OCR 识别内容]
> 定性分析 ,记 Operators per Alpha  Operators used -
> Fields per Alpha`
> Rieldsused ,
> Community activity 和 Max simulation streak 分别表示六维的  每
> 个c的平均(去重)操作符数量。操作符的去重使用个数。每个Q 的平均(去重)字
> 段数量,
> 字段使用(去重)数量 rank [社区活跃程度]和最大连续回测天数 ,下面
> 使用简写 ,比如:最大连续回测天数记为 MIsS . 对于六维排名下面给出两种排名方
> 法,一种不需要量纲 .
  
> [!NOTE] [图片 OCR 识别内容]
> 第一种便是 rank , rank 是一个减函数,排名也是一个减函数 .由于 OpA
> 与FPA 越小越好 (有些会为0 ,需排除0) ,所以使用 rank 时尽量保持属于],
> 所以排名为
  
> [!NOTE] [图片 OCR 识别内容]
> rank
> rank
> rank(Ou)
> rank
> rank(Fu) + rank(Ca)
> rank(MIss)
> 十
> OpA2
> 1十
> FPA2
  
> [!NOTE] [图片 OCR 识别内容]
> 这样子是比较合理的 ,
> 按照权重来。每一个维度都是等权的 ,逻辑也是非常清晰的 .
  
> [!NOTE] [图片 OCR 识别内容]
> 但是需要注意的是当 OPA 和FA的数值为 0时,在内层 rank 时应设置为最
> 后一名 .
> 第二种是常用的标准化后加权求和 ,核心思想是:先消除不同指标的量纲
> 和尺度差异 ,再根据指标的重要性赋予权重 ,最后合并成一个综合得分 fscore
  
> [!NOTE] [图片 OCR 识别内容]
> 1.最小-最大归一化 ( Min
> Mac Normalization) , 又称为 [0 ,1]标准化 .
> 公式为
> X
> 3
> 3
> 其中,3表示原始数据 ,
> 是数据中的最小值 ,
> 是数据中的最大值 ,3'
> 是归一化之后的数据 .
> ?min
> ?max
> ?min
> RCmax
  
> [!NOTE] [图片 OCR 识别内容]
> 2.乏
> Score (标准差 )标准化
> 3 一 L
> 乙 =
> 几
> 其中 M: 该指标平均值,
> M = 1
> di
> 
> i=1
> 几
> 1
> O:
> 该指标标准差 ,
> O =
> Di -p)2
> 几
> i=1
  
> [!NOTE] [图片 OCR 识别内容]
> 3.赋予权重分配+综合得分
> fscore , 使用 [0 ,1]标准化公式 ,每个维度都分
> 配在 [0 ,1] ,六个维度使用等权 ,这里同样需要考虑当3' =0时的特殊情况 .
  
> [!NOTE] [图片 OCR 识别内容]
> SCOre
> dimension
> (1 - OpA)
> Ou' + (1 -FA)+ F' + Ca' + Mss'
> i=1
  
> [!NOTE] [图片 OCR 识别内容]
> 最后 rank(fscore ) 即可得出排名 .
  
> [!NOTE] [图片 OCR 识别内容]
> 第三种是我自己想的 ,感觉有一丢丢意义 ,于是在这里说一下,首先去掉
> 些异常值 (在逻辑自洽这块其实应该不要丢弃最好 ,因为每一个顾问的数
> 据都是真实的 ,不存在说是异常的 ),综合得分 fscore -
> 1.找出六维每个维度所有顾问的平均值丛或中位数;
> 几
> 山=1
> Ri
> 几
> i=1
> 2.使用最小公倍数 LCM 方法计算每个维度的权重 weight;
> weight
> LCM(opA; Nou
> NEu; Mca) MMsg)/
> Ri
> 几
> 2二1
> UFpA '
  
> [!NOTE] [图片 OCR 识别内容]
> 3.对于 OpA 和 FPA 数据使用关于均值对称反转 ,取 OpA ' 和 FPA' ,其
> 他维度都有 D' = 2 ;
> OPA
> 二
> 0 , OPA'
> 二 0
> FPA
> 二
> 0 ,RPA' =0
> OPAT
> OpA
> FPA'
> 一
> FPA
> 4.
> 计权重综合得分 fscore =
> fscore
> weight;
> dimension
> 2=1
> 最后 rank(fscore) 即可得出排名 .
> WopA
> WopA
> MppA
> NFpA



> [!NOTE] [图片 OCR 识别内容]
> C
> 欧拉乘积
> 1
> $(8) =
> 工
> 8
> 1-0
> p prime
  
> [!NOTE] [图片 OCR 识别内容]
> 《欧拉乘积公式》以此可证明素数无穷


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 三 六维数据定量分析


[图片 (图片已丢失)]

[图片 (图片已丢失)]

先说结论:  分而治之！分为三部分，1. Max simulation streak (最大连续回测天数) 保持回测不要断；2. 在社区有效学习；3. 其他四维为一块，如果操作符还未使用完，可以刷，看看上面的结论，操作符放在哪儿效果都是一样的，尽量交能够降低自己的平均操作符和平均字段，从rank来说，优先保证 Operators per Alpha  和 Fields per Alpha 的增量降低，然后再是 Fields used，因为 Operators per Alpha  和 Fields per Alpha 的密度更高，做好一次性rank可以上升好几名 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 定量分析 .在数学中, rank 犹如是一个 bug 的存在 ,
> 因为 rank 算是一个
> 指标器 ,
> 可以帮助进行排名 ,但是又没有办法去(计)量化细化它 ,只能类比
> 趋势.
> 由于不好量化 rank , 定性分析第一种方法有内置 ralk , 当有一个维度的
> rank 较低时 ,十分干扰整个排名 ,所以舍弃;第二种方法比较常规且好 ,我们
> 使用笫三种方法来定量分析 .
  
> [!NOTE] [图片 OCR 识别内容]
> 1.
> 计算每个维度的均值丛;
> [bopd] = 5, [bou] = 100, [LEpA]
> 二
> 4, [MRu] = 300, [bca]
> 二
> 25,
> 二150
> 2.计算每个维度的权重 weight;
> LCI
> Nou '
> NRui Hca' |Mss _
> 二 300
> weightopa
> 60, veight
> Ou
> 二
> 3, weightpo4
> 75, veight
> Fu
> 1, weightca
> 12, weight
> U85
> 2
> [Muss
> WopA '
> IFpA '
  
> [!NOTE] [图片 OCR 识别内容]
> 3.计算每个维度应该被权重值?';
> OpA' = 6.6 , Ou'
> 二
> 68 , FPA' = 6.5 , Fu'
> 二
> 260
> Ca'
> 二
> 3
> MIss
> -
> 88
> 4.计算综合得分 fscore;
> fscore
> 
> 60 .6.6 十3 .68+75 .6.5+1
> 260+12
> 33+2.88
> 二
> 1919.5


---

### 帖子 #9: 根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的_35129651186967.md
- **讨论数**: 90

## 引言：为什么我们要关心 PC？

 **降低 PC 是提升收益和保证账号健康的最重要因素之一** 。

1. PC的高低直接影响个人短期（base payment)和长期收入 (quarterly payment),
2. PC的高低间接影响Value Factor，从而再次影响收入
3. 高PC alpha 无法入库，无法参与比赛，长期提交大量高pc alpha，可能会导致账户封禁

## 一、理解Product Correlation

### 什么是 Product Correlation（PC）？

PC 衡量一个 alpha 与平台中其他 顾问提交的alpha 的相关性，其计算公式和自相关类似，为最近四年PNL 每日变化（diff）的皮尔逊相关性系数。

### PC高低与收入的关系

顾问提交的alpha被平台接收后，会进行多次筛选以决定是否对平台有用，其中最重要的筛选就是PC。当PC大于0.7，则被认为是相同/及其相近的alpha，则该alpha不会被平台采用，因此也不会有机会获得任何weight。在顾问协议中披露的每日base payment 计算公式中也明确提到与base payment与PC的负相关性。通常来说，当pc< 0.5 会被认为是比较独特的因子，从而会获得更高的base payment，也更有机会被基金经理采纳而获得weight，进而获得更高的quarterly payment。

而更低的PC也意味着更低的SC，组合的correlation 越低，也会进一步提升组合的整体多样性表现，从而获得更好的value factor。从个人经验看，在点塔的时候偶尔提交了更高的pc alpha，相应的该月份的vf就会受到影响。不知道平台在计算vf的时候是否对高pc有额外的惩罚系数。

### 举例说明PC高低与收入的实证

Alpha 1： PC 0.49的SA，获得了58.97的 base payment


> [!NOTE] [图片 OCR 识别内容]
> anonymoUs
> Super
> ACTIVE
> 08/30/2025 EDT
> JPN
> TOP1600
> 0.31
> 0.49



> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 08/30/2025
> Super:
> 58.97
> Regular:
> 7.94
> Total:
> 66.91
> 40
> 20
> 28.
> 29.
> 30.
> 31 _
> 1.Sep
> 2.Sep
> Aug
> Aug
> Aug
> Aug


Alpha 2：SAC 期间的一个表现更好的alpha，PC 0.68，只获得了9.69 USD的收入。而7月14日一个0.73的pc 只获得了5.4USD的收入。对不起当时0.9+的VF


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/19/2025
> Super:
> 9.69
> Regular:
> 8.10
> 15
> Total:
> 17.79
> 10
> 14.Jul
> 15.Jul
> 16.Jul
> 17.JUl
> 18.Jul
> 19.Jul
> 20.Jul


# **二、如何检查PC并降低PC的实操**

**获取PC的代码：论坛有很多，部分同学反馈没有权限，已更新在评论区**

[[链接已屏蔽])

**几个注意事项：**

1. 不建议直接只用check submission的接口，会更慢，因为要检查其他的测试比如自相关，而自相关等检测都可以在本地完成，效率更高
2. 该接口也会限流，甚至影响提交alpha，建议做一些在本地的限流，这样不触发平台限流，从而获得整体的结果最优（代码如下，可以自己调整睡眠时间）
3. 极少数情况会pc通过但是提交失败，这是因为pc是用的缓存数据，在pc检查和提交之间如果别人交了类似的会在提交时候出现pc不过的情况，但这种情况极少极少。

```
s = login()start_time = datetime.now()pass_pc_ids = []last_request_time = datetime.now()max_sleep_time = 60 * 60 # 最大睡眠时间1小时current_sleep_time = 60 # 初始睡眠时间60秒定义重连时间间隔reconnect_interval = timedelta(hours=3.5)for id in batch_ids:# 检查是否需要重新登录current_time = datetime.now()if current_time - start_time >= reconnect_interval:s = login()start_time = current_time# 记录请求开始时间request_start_time = datetime.now()# 调用 get_prod_corrpc = get_prod_corr(s, id)# 记录请求结束时间request_end_time = datetime.now()request_duration = (request_end_time - request_start_time).total_seconds()# 检查相关性if pc > 0.7:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['PROD Correlation'])elif pc >0.5:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['ace_tag'])else:result = get_simulation_result_json(s,id)selection = result['selection']['code']tag_value = ['PC 0.5','Ready to Submit']name_value = result['name']if "own" in selection:color = 'GREEN'count = count+1else:color = 'None'combo = result['combo']['code']while len(selection)<100:selection = selection + selectionwhile len(combo)<100:combo = combo + combo set_alpha_properties(s,id,name_value,selection_desc=selection,combo_desc=combo,tags=tag_value,color=color)pass_pc_ids.append(id)print(id,pc)# 计算上次请求到本次请求的时间间隔time_since_last_request = (request_start_time - last_request_time).total_seconds()# 如果请求时间明显增加，调整睡眠时间if request_duration > current_sleep_time * 1.5:current_sleep_time = min(max_sleep_time, current_sleep_time * 2)else:current_sleep_time = 60 # 如果请求时间正常，恢复默认睡眠时间# 更新上次请求时间last_request_time = request_start_time# 等待当前睡眠时间time.sleep(current_sleep_time)print(len(pass_pc_ids))
```

## 三、如何降低 PC？

Global 论坛有一篇外区的帖子，有些内容是很有可取之处的

- [Reduce Production Correlations. – WorldQuant BRAIN]([L2] Reduce Production Correlations_29301199149463.md)

### 避免使用过于常见的 signal

- 如单纯的暴力一二三阶，没有任何自己的迭代

### 增加创新表达方式

- 多尝试非线性组合、二阶交叉项、相对排名等。使用sigmoid，sign power，ts linear window等做一些数学变换
- 尝试使用target tvr的几个operator来降低tvr的同时也会变化pnl从而降低pc （但有时会反而提高，因为别人也使用了该方法提交过）

### 尝试多种region，unvierse和netralization 方式

- 一些高pc的因子，在变换了中性化，unvierse和regioin后会有意想不到的收获，而这个可以代码工程化完成

### 多尝试新的数据集

- 当有新的数据集，新的unvnierse和新的region的时候是pc最低的时候，如TOPDIV3000，最近新上的数据集等

### 使用独特的分组方式

- 最常见的是group datafield （如other455），bucket分组

### 当然王牌还是有自己的模版和自制数据

### 如何快速总结已经提交alpha的PC：

在alphas菜单中点击submitted，选中select column 勾选product correlation，已经提交alpha的PC一目了然


> [!NOTE] [图片 OCR 识别内容]
> 鬯2
> Simulate
> Alphas
> Leamn
> Data
> Labs
> Genius
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> 《
> Refer a friend
> Select Columns
> Summany
> Properties
> Settings
> Perommance
> Alphas
> Nams
> SzazUs
> Resion
> Instrument TypE
> Sharpe
> Rezurns
> Competi-ion
> Catesory
> Universe
> Delay
> Pnl
> Turnoer
> Page size
> Typ=
> Color
> Decay
> Neutralization
> Drawdown
> Marsin
> Fllter
> LansuaEs
> TaE
> Truncation
> Unit Handlins
> Fitnsss
> Book Sizs
> Date Submit-ed (EST]
> Hidgzn
> NaN Handlins
> Pasteurization
> ~oun
> Shor Count
> Select Columns
> Turnover
> Tag
> Favorite
> Sharo 50
> Sharpe 125
> S-ar Date (EST
> Sharpe 250
> Sharpe 500
> 22
> See
> OSIIS Razio
> Pre Close Sharpe
> 4.974
> Pre-Close Razio
> Self-Correlation
> Prod-Correlation
> Reset
> Apply
> Lns


最后祝大家新的赛季VF和Genius双高！如果对你有用还请点赞评论！

---

### 帖子 #10: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 1000

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #11: 【日常生活贴】我的量化日记第三季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **讨论数**: 1021

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #12: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #13: 【日常生活贴】我的量化日记第二季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **讨论数**: 1004

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #14: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #15: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **讨论数**: 1408

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #16: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 1132

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #17: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
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

### 帖子 #18: 如何更优雅地避免触发限流获取Prod Correlation代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何更优雅地避免触发限流获取Prod Correlation代码优化_33823038097303.md
- **讨论数**: 11

WorldQuant Brain 平台需要计算资源的API大部分都做了限流处理, 其中的Prod Correlation是一个,也是我们日常提交alpha前经常要check的, 下面将剖析其http限流机制及如何优雅的避免触发限流。

首先,第一步分析数据。我们分析下获取Prod Correlation时服务端返回的内容,如下图所示:


> [!NOTE] [图片 OCR 识别内容]
> 常规
> 肴求 URL
> https:l/apiworldquantbraincomlalphas/OVGAjEg/correlations/prod
>  求方法
> GET
> 穴恋忙码
> 200 OK
> 远程垅址
> 35.175.81.19;443
> 用站点策绛
> strict-origin-when-cross-origin
> 晌应楸头
> ACCEss-Control-AIIow-Credentials
> TTUE
> ACCESS-Control-Allow-Origin
> https:/ Iplatform worldquantbraincom
> ACCESS-Controi-E ooss
> Headers
> LocationRetry-After
> Allow
> GET HEAD; OPTIONS
> Content Language
> Zh-cn
> ContentLength
> Content Type
> text/html; Charset=UTF-B
> Date
> Wled  30 Ju
> 202513:03:04 GMT
> Ratemit-Lmit
> Ratelimit-Remaining
> Ratelmit-Reset
> Retry-utter
> 1.0
> Strict-Transport-Security
> max-age=31536000; includeSubDomains
> Vary
> AcCEpt-Language
> Cookie
> Origin
> X-Frame-Options
> SAMEORIGIN
> X-Ratelmt-LimtMinute
> XRatelmtReamalhing-Winute
> Nary


显而易见,第一个框里的数值含义如下

RateLimit-Limit: 速率限制数为60

RateLimit-Remaining: 速率限制剩余58

RateLimit-Reset: 速率限制重置 56 秒后

Retry-After: 1秒 (请在1秒后再发起请求获取结果, 别蛮干, 蛮干触发429)

第二个框则是辅助信息,表示每分钟限制请求60次及剩余请求次数

了解了以上信息, 我们就可以根据服务端的要求来优雅地发起请求获取结果了。

第二步,处理数据:

1.在服务端返回200时获取上述信息:

if resp.status_code == 200:

ProdCorrRemainTimes = int(resp.headers.get("RateLimit-Remaining", 0))

ProdCorrResetTime = time.time() + int(resp.headers.get("RateLimit-Reset", 60))

2.在请求url前判断是否还有请求次数剩余, 如已快耗尽则等待重置后再发起请求:

if ProdCorrRemainTimes <= 3 and ProdCorrResetTime - time.time() > 0:

print(f"剩余Prod Correlation查询次数: {ProdCorrRemainTimes}, 重置时间: {ProdCorrResetTime - time.time()} 秒后.")

sleep(max(3, ProdCorrResetTime - time.time()))

多线程并发请自行加锁,只要两步即可避免触发限流,本人实现的效果如下图:


> [!NOTE] [图片 OCR 识别内容]
> 获取Prod Correlation: https: //api .worldquantbrain .comalphas/dp717Nw/correlations /prod 剩余Prod Correlation杳询次效:
> 牵胄时间:  18.6529541815625
> 获取Prod Correlation:
> /|api.worldquantbrain.comalphas /dP7ITNw/correlations/prod 剩余Prod Correlation查询次数:  54,
> 重置时间:
> 999544382095337
> 疆
> 获取Prod Corpelation: https: //api.worldquantbrain.comlalphas /dp7I7Nu/correlations/prod 剩余Prod Correlation杳询次效:
> 垂置时间:  3.999412775039673
> 获取Prod Correlation: https: / /api
> Idquantbrain.comlalphas /JP7I7Nw/correlations /prod 剩余Prod Correlation查询次效:
> 重置时间:  0.9994614124298896  秒后
> 获取Prod Correlation: https: /lapi
> Idquantbrain.comalphas /dp7I7Iw/correlations /prod 剩余Prod Correlation耷询次效: 59。重置时间:  56.99948204620361
> 获取Prod Correlation:
> : / |api.worldquantbrain.comlalphas/dP7I7Mw/correlations /prod 剩余Prod Correlation查询次敛:
> 重置时间;  53.99942398071289
> 稚:
> Mlpha: dP7ITIN Prod Correlation:
> 7658
> plpha: Gzjldil6 PPAC_Corr:
> 43576396351629637
> Code
> ts_quantile(oth455_partner_nzv_p58_9200_N4_pca_factl_Value
> Oth455_partner n2v_058 9200M4pCa fact3_Value
> description
> None
> aperatorCount
> 获取Prod Corpelation: https: / |api.Norldquantbrain.comlalphas /G2jMdNG/correlations/prod 剩余Prod Correlation查询次敢:  57
> 重苴时间:  53.983994483947754  秒后
> 获取Prod Correlation: https: //api.worldquantbrain.comalphas /G2jMdNG/correlations/prod 剩余Prod Correlation f询次效:
> 重置时间:  49.99974870681763  秒后
> 获取Prod Correlation: https: //api.worldquantbrain.comalphas/ozjMd NG/correlations /prod 剩余Prod Correlation杳 询次敛:  56,
> 单苴时间:  46.9998300075531
> 获取Prod Correlation: https: //api
> Idquantbrain.comlalphas /GzjMdNG/correlations/prod 剩余Prod Correlation查询次效:  55,
> 重置时间:  43.99961996078491
> :
> 获取Prod Corpelation: https: / /api.worldquantbrain.comalphas /62jMdNG/corelations/prod 剩余Prod Correlation耷询次敛:  54,
> 申肖时间:  48.99939489364624
> 获取Prod Correlation: https: //api
> Idquantbrain.comalphas / G2jMNdlG/correlations /prod 剩余Prod Correlation查询次效:
> 53,重置时间:  36.99938488006592
> $:
> 获取Prod Correlation: https: //api.worldquantbrain.comalphas/G2jMdNG/correlations /prod 剩余Prod Correlation杳询次敛:
> 事宵时间:  33.99967898236084  秒后
> 获取Prod Correlation:
> : /|api.Norldquantbrain.comalphas / GZjMdNG/correlations/prod 剩余Prod Correlation查询次': 5I
> 重置时间:  30.999419927597046  秒后
> Nlpha: GjMdHG Prod Corpelation:
> 9866
> https
> https
> https


获取几百个未触发429限流情况, 也不用定期暂停, 当然如果蛮干如下图:


> [!NOTE] [图片 OCR 识别内容]
> 获取Prod Correlation: https: //api.orldquantbrain.comalphas /G7lajmP /correlations /prod 剩余Prod Correlation杳询次效:  2。幸胄时间:  18.998452186584473  秒后
> 获取Prod Correlation: https: / |api.worldquantbrain.comlalphas /G7Lajmp /correlations /prod 剩余Prod Correlation查询次效: 0。重置时间:
> 17.998653173446655
> 秒后
> 获取Prod Correlation: https: / /api.worldquantbrain.comalphas/671ajmp /correlations/prod 剩余Prod Correlation杳询次敛: 1。事邕时间:
> 17.998456716537476
> 秒后
> 人获得Prod Correlation: https: / |api.worldquantbrain.comlalphas /G7lajmp /correlations /prod 失败 (状态码:  429):
> messaBe
> API rate Iimit exceeded"


当然,这只是服务端http限流机制,后台计算端也有限流机制,我们无法获取到后台反馈,也无法突破计算端的限流, 也就是说获取多了也会很慢, 但处理后就不至于被服务端直接掐断,还是有意义的。

除了Prod Correlation, Self Correlation等也一样的限流: 每分钟60次, 60秒重置次数, 当然Self Correlation可以本地计算, 说到这, 随便提一下,之前论坛或培训提供的Self Correlation本地计算代码在提交过PPAC alpha后会出现计算不正确的情况, 研究后发现,源代码这块逻辑问题:


> [!NOTE] [图片 OCR 识别内容]
> def load_data(tag=None
> 加载效据。
> 此函效会检查效据是否已经存在。如果不存在。则从 API 下载数据井保存到指定路径。
> Args:
> (str): 数据标记。默认为 None。
> TAII
> 读取pickle文件
> Os_alpha_ids
> Ioad_obj(str(cfB.data_path
> 05_alpha_ids
> Os_alpha_pnls
> load_obj(str(cfg.data_path
> Os_alpha_pnls
> Ppac_alpha_ids
> load_obj(str ( CfB.data_path
> Ppac_alpha_ids
> 根据t筛选alpha
> pnls
> PPAC'
> for
> item in
> 05_alpha_ids:
> alpha_ids [item]
> [alpha for
> alpha
> 05_alpha
> ids [item] 讦
> alpha
> in ppac_alpha_ids]
> elif tag==
> Selfcorr
> for item
> O5_alpha_ids:
> 05_alpha
> ids [item]
> [alpha
> for alpha
> Os_alpha_ids [item] 讦
> alpha
> not
> ppac_alpha
> id51
> else:
> O5_alpha_ids
> 05_alpha_ids
> t昭
> tag =


自相关计算需要包含PPAC alpha, 注释掉后计算结果与网页提供的一致, 大家可以尝试下。如果代码已更新请忽略。

另外本地计算自相关也需要去获取pnl, 这个也是有限流机制的, 不同的是限制数值:2000次每小时,重置时间也比较长而已。所以本地自相关只是计算在本地,数据还是得去服务端取的。

另外作为刚入量化交易三个多月的小白,给新人整理了平台提交回测时显示的所有TIPS:

1. Try submitting Alphas with lower Turnover.  
   → [Turnover]( [[链接已屏蔽]) )

2. Try creating Alphas using Datasets with high Dataset Value Score, to reduce the Prod Correlation (for ex Earnings Datasets, Macro Datasets, Insider Datasets).  
   → [Datasets]( [[链接已屏蔽]) ) | [Earnings Datasets]( [[链接已屏蔽]) ) | [Macro Datasets]( [[链接已屏蔽]) ) | [Insider Datasets]( [[链接已屏蔽]) )

3. Explore various Transformational Operators and Cross Sectional Operators.  
   → [Transformational Operators]( [[链接已屏蔽]) ) | [Cross Sectional Operators]( [[链接已屏蔽]) )

4. Experiment with Neutralization Settings. Check out this Forum post.  
   → [Forum post]( [[链接已屏蔽]) )

5. Check out these Tips to improve the simulated Returns of the Alphas.  
   → [Tips]( [[链接已屏蔽]) )

6. Truncation helps in controlling the stock weight in the Alpha simulation. Read this Forum post to understand why.  
   → [Forum post]( [[链接已屏蔽]) )

7. Try working on Delay 0 Alphas. This Forum post may help you.  
   → [Forum post]( [[链接已屏蔽]) )

8. Check out the Learn section on SuperAlpha and helpful Tips to construct SuperAlphas and potentially increase your compensation!  
   → [SuperAlpha]( [[链接已屏蔽]) ) | [helpful Tips]( [[链接已屏蔽]) )

9. Automate your research, check out Brain API.  
   → [Brain API]( [[链接已屏蔽]) )

10. Check out Getting Started page and Courses to boost your knowledge for Alpha research!  
    → [Getting Started]( [[链接已屏蔽]) ) | [Courses]( [[链接已屏蔽]) )

11. Explore Vector Datafields, for example Social Media, for more info check page on Vector Datafields.  
    → [Social Media]( [[链接已屏蔽]) ) | [page on Vector Datafields]( [[链接已屏蔽]) )

12. Explore Group Datafields - create your own groups for Alpha Neutralization, for more info check Documentation.  
    → [Documentation]( [[链接已屏蔽]) )

13. Try ensuring coverage by backfilling Datafields and the final Alpha using Operators such as ts_backfill, group_backfill, group_extra.  
    → [backfilling]( [[链接已屏蔽]) ) | [ts_backfill]( [[链接已屏蔽]) ) | [group_backfill]( [[链接已屏蔽]) ) | [group_extra]( [[链接已屏蔽]) )

14. Try using exit triggers (e.g. stop-loss) to close position while using trade_when Operator.  
    → [trade_when Operator]( [[链接已屏蔽]) )

15. Try out Model Datasets. You should start by looking for fields with the words “rate” or “rank” in their names - maybe it is already an Alpha?  
    → [Model Datasets]( [[链接已屏蔽]) )

16. PE ratio can be a good measurement to generate Alphas. Calculate estimated PE ratio using EPS estimates of either EPS Estimate Model Dataset or Scorings Dataset and price fields of basedata (Price Volume Data for Equity)  
    → [EPS Estimate Model Dataset]( [[链接已屏蔽]) ) | [Scorings Dataset]( [[链接已屏蔽]) ) | [Price Volume Data for Equity]( [[链接已屏蔽]) )

17. You may utilize the seasonality Datafields in Research Indicators to improve details in your ideas/signals.  
    → [Research Indicators]( [[链接已屏蔽]) )

18. Country and Sector Neutralizations generally both work well, though we recommend you to try other groups as well.

19. Along with close or returns, it turns out that using vwap (Volume Weighted Average Price) with your Alpha also tends to give good results.

20. To achieve reasonable Margin rates, you are advised to use the following Operators: hump_decay, ts_decay_linear, and ts_decay_exp_window.

21. Social Sentiment indicators help investors identify information in social media that could cause a stock’s price to increase or decrease in the near future - take a look at Social Media Datasets and experiment with them in your Alphas!  
    → [Social Media Datasets]( [[链接已屏蔽]) )

22. Use Ravenpack News Data to develop a wide variety of Alphas - momentum, event based or D0 Alphas with high Sharpe and Turnover.  
    → [Ravenpack News Data]( [[链接已屏蔽]) )

23. Check out Model Datasets - try to compare model's predictions with returns using ts_corr and ts_regression Operators!  
    → [Model Datasets]( [[链接已屏蔽]) )

24. Check out Analyst Datasets - try to capture direct and indirect signals to predict returns: how does the Datafield changes affects returns? which fields directly correlate with returns?  
    → [Analyst Datasets]( [[链接已屏蔽]) )

25. You have an option to use Option Dataset! OptionBreakeven, CallBreakeven, and PutBreakeven can be used to measure the pricing tension between the buyer and seller.  
    → [Option Dataset]( [[链接已屏蔽]) )

26. Submit 4 Alphas and, if available, 1 SuperAlpha, each day, to improve the Quantity Factor of your score.

27. Submit Alphas with low Correlation to your other Alphas.

28. Diversify your Alphas, use larger Universes, different Regions (esp. non-US) and delays (esp. Delay 1)

29. Try less explored Datasets or old Datasets but using new ideas.

30. Try reading new research papers, blogs and apply these ideas in the Alpha expression, check out Research Papers for Consultants.  
    → [Research Papers for Consultants]( [[链接已屏蔽]) )

31. Check out the alpha examples here. Can you improve these alphas and submit?  
    → [here]( [[链接已屏蔽]) )

32. Submit Alphas that retain at least 70% of their Sharpe in the Sub-Universe or Super-Universe.

33. Focus on improving Alphas by refining your ideas, not by adding or fitting parameters, factors or reversion elements.

34. Restrict your parameter search to simple & reasonable ones. For example 5, 20, 60, 120, 252 in case of days, instead of 37, 14 etc.

35. Novelty of ideas will help you reduce correlation with others work. Try Operators & Settings you haven’t used before. Detailed documentation on Operators is available here : Detailed Operator Descriptions.  
    → [Detailed Operator Descriptions]( [[链接已屏蔽]) )

36. Try using x = ts_step(1) Operator as a parameter in ts_regression, then x will be time variable.

37. Use trade_when or hump Operators to reduce Turnover of your Alphas.

38. Use days_from_last_change() Operator to catch fast decaying signals.

39. Try to reduce Turnover of illiquid part of the Universe by using Operator rank(). As a proxy for liquidity you can use cap or average volume.

40. Try to use bucket() Operator to neutralize your Alpha using custom groups.  
    → [bucket()]( [[链接已屏蔽]) )

41. Try to use vector_neut Operator to neutralize your signal to market factors.  
    → [vector_neut]( [[链接已屏蔽]) )

42. Try to compare Broker Estimates with company fundamentals to create an Alpha!  
    → [Broker Estimates]( [[链接已屏蔽]) )

43. Company Fundamental Data For Equity have well structured Datafields which are mostly scores, you can use common Time Series Operators like ts_rank, ts_zscore or measuring the ts_delta of the fields.  
    → [Fundamental Data For Equity]( [[链接已屏蔽]) )

44. Try using Employee Data to evaluate company well-being (how does company's care for employees impact it's performance?)  
    → [Employee Data]( [[链接已屏蔽]) )

希望大家喜欢!

---

### 帖子 #19: 1. 下载/增量更新download_data(session, flag_increment=True)Self-correlation 0.7691 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.这是代码计算结果：alpha_id:  XgQqkZda self_corr:  0.7691116930719178alpha_id = "XgQqkZda"Self-correlation is 0.4589, which is above cutoff of 0.7, or Sharpe is better by 10.0% or more.这是代码计算结果：alpha_id:  zq6wpknV self_corr:  0.48371278563080605alpha_id = "zq6wpknV"加载数据os_alpha_ids, os_alpha_rets = load_data(tag='SelfCorr')self_corr = calc_self_corr(    session,    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)print("alpha_id: ", alpha_id, "self_corr: ", self_corr)
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

### 帖子 #20: 这个因子到底能不能交？（下） 【传奇耐打王系列一】
- **主帖链接**: https://support.worldquantbrain.com[L2] 这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md
- **讨论数**: 24

上一篇在这： [[L2] 这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md-这个因子到底能不能交-上-传奇耐打王系列一]([L2] 这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md)

刚刚更新的combine证明我的思路大体应该是正确的：


> [!NOTE] [图片 OCR 识别内容]
> AIP
> Nmno tAl
> NIONI a(T
> C-IrTIITTSC
> T ATIHII
> UMTNTTIRNT21V
> Eligibility Criteria
> O
> CFen
> U
> Cn
> SIgnL
> 1Tn7IFrrort
> Fymmids Complsted
> IUs ULCIL
> ThITPI
> Wha FeTormaTCe
> 2.15
> CLemmm
> Combinod Soloced Aloh Prrtormancn
> mch Tocmo
> Combined Power PolMlpha Partormanco
> 2.22


那接下来我们就继续讨论啦！

说完了必须指标，我们该讨论优化指标了。优化指标就是在完成必须指标的基础上好中选优，位次越靠前优先度越高：

1.低相关（先pc后（sc或ppac））

2.sharpe和fitness的21年和22年优秀

3.sharpe和fitness逐年优秀

4.margin的21年和22年达标

5.margin的逐年达标

6.margin的21年和22年优秀

7.margin的逐年优秀

8.margin和return越高越好

9.turnover围绕在12%

10.drawdown越低越好

11.多空优秀

这里大家可以看到，我把低相关放到了第一位。首先，为什么追求pc低。很多时候我们都说，pc低可遇不可求，所以我们先拿准自己的池子，对sc做出要求。这里我们可以类比，每个人的池子是小池子，你提交上去的池子是世坤的池子，是大池子。你想把sc降低，那世坤也想把属于他的sc（pc）降低呀。

鑫佬名言：你做了别人没做过的（pc低），这对于世坤来说，就是杰出的贡献。

为什么说base主要看pc，这就是世坤衡量你贡献的主要指标。

在pc足够低的情况下，我认为可以相对忽略更优质的指标，优先选择pc低。

鑫佬名言：pc0.5以下就是极品，0.3以下已经是极品中的极品。

我当时交了一个0.2几的pc，是我成为有条件顾问后单日base首次破3。

以下举例一个我最近刚交的ra：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> N3ILT
> RrsNR
> CTTTILaU
> FTIIIFFTINT
> mII
> ARUNOMNUATI
> 2.29
> 5.419
> 3.813
> SE沾
> 11.8993
> IsT0
> TT
> OS
> T
> TCo
> 4A191
> hMre
> T
> 071T21 「T
> R7111
>  kg4
> UItot
> at
> N
> Chart
> I'Est HillT' Cnstrimer
> ATIMAI
> _匕
> 0.,76
> 904
> 7.18N
> 12,58m
> Correlation
> IoLC
> CALT219
> PI
> C-~TAIOI[
> Testing Status
> I1 FENCINL
> PdCrIalon
> ITu SuIinoII
> 0.3656
> 0.3925
> n]T


毫无疑问，赚的多而且对vf和combine有极大的帮助

再次强调，一定要满足基础要求！基础要求不满足不要看pc！

但我还在论坛里看到另外一个ppa大佬的经验分享（具体一下子找不到了，在这里对您表示感谢）：pc高说明什么？说明交的人多。交的人多从概率上说明这个因子值得信赖，否则为什么别人看到了高相关还交呢？我觉得这也是有道理的。

因此我觉得pc是一个很主观的东西，就是每个人心中要有符合自己个人的阈值。我一般不会在官方要求上再加一个自己的高要求（比如有的大佬pc0.6以上就不交），但对于一个小白来说，我还是更加重表现，比如下面这个ppa，也是我最近交的：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> N3ILT
> 41+7891757
> CTTTILaU
> TITH
> UAUTUUNUCOAL/
> SINVJaVIOC
> 3,33
> 5.354
> 6,115
> 1.253
> 24%
> 5T4
>  
> U4
> 11443
> OV
> 47
>  Hr
> TI7r
> TSITaln[
> Uge
> 2
> 7
> Ct
> Chart
> Ie? O
> CUIISISTIP
> AIreMLOu
> HD
> 二 FSI
> 15
> 4.975
> 1.719
> 1T
> Correlation
> Iron TT7
> 0.2975
> ~0.1253
> 05 Testing Slalus
> 1CTllsn
> PeOI
> UIIICI CI
> L u
> AMm。I IL
> 09065
> 0,4723
> 941451
> 247


虽然pc非常高，但是表现我很认可，再加上sc也不错，对于我的池子有不小的帮助，我会果断地提交它。

也有人问我sc的阈值，说实话，我也是按照官方的来的。甚至有时候，我会因为sharpe提高百分之十而提交不满足pc或者sc的因子，这都是需要根据表现来进行考虑的。

这里我详细解答为什么我会提交这样的因子。首先，提交这样的因子对combine的帮助很可能是负的。但是对于vf而言，如果你觉得这个因子你稳赚，那提交了就是正的收益。可能对于这个时期的我，我的目标是优先冲击vf高，所以为了收益我希望我有更多稳定赚的因子，所以我会提交。这是对于我个人现阶段的影响之下我的选择。

这里说一个我建议的阈值，我在组sa时发现，sc控制在0.55到0.6时往往可以实现因子的表现最大化。所以我觉得如果你要设置一个个人的sc阈值，0.6就已经很好了。对于像我一样的大部分小白，只跑一二三阶，我们能挖到低相关是存在很大一部分的运气成分。如果把阈值设置的太低，会导致我们无法提交足够数量的因子。数量同样也是一个重要的维度，因此我不建议自己设置太低的阈值。

在讨论接下来的指标之前，我先对这个顺序做解释。为什么sharpe和fitness在margin和return之前？因为稳定是一个因子非常非常重要的因素！！！划重点！！！

游戏王名言：因子一定是先稳而后赚。

我们的基础要求中有一个margin达标，margin达标说明已经能大概率赚钱了。接下来我们的目标就是要让因子稳定赚钱。稳定赚钱的因子我们称之为“印钞机”。我可以允许我一次赚的不多，但我一定要一直赚！！！稳定赚钱的因子对于vf和combine的帮助是超级大的。

接下来我们来说指标。我都是先写21年和22年表现好，而后才是逐年表现好。大家都希望逐年表现好。但除非顶尖高手我们都做不到逐年都好。因此关注最近两年是很重要的。为什么因子会不断地挖出来，不断地退役，就是因为因子具有时效性。这个因子现在在市场里如鱼得水，说不定半年后就变成错误信号了。最近两年的信号相对之前的几年肯定是最具有参考性的。如果有个因子前面表现很不错，然后最近两年开始下滑，我个人认为这是很需要警惕的。下面是我的例子：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> nNRA
> RrsNR
> CTTTILaU
> rT NTI,
> FFMIpm'
> U-mrsl
> C UIJL
> Code
> 15 Summary
> NTINTT 
> 4.80
> 34.91N
> ,46
> 39
> 1=
> SIIUOUI
> Uat
> T
> M
> 3
> Tmo
> T
> sa
> Cno Alah
> Chart
> Hls:naUtrallzed
> CVEU
> 3.519
> 10.829
> SO
> 6,20650
> Isbahilf' canstiner
> ATINCICTT
> F Lutuleer PnL
> In aImt CrsTJIIEIFT
> 26.299
> 8.425
> 3.399
> 6.4190
> Correlation
> 15 Testing Status
> eLCTrlotlc
> yr
> otm


这是我挖出来的一个ra，乍一看，基础要求都满足，sharpe和fitness还高的离谱。但是我们细看21年和22年，这两年的margin从合格走向不合格。用大家常说的一个词叫做：圆顶。这种就是圆顶因子我们看不到它往上增长的趋势了。对于usa地区而言，这几年行情好，很多因子都是翘头趋势。这个因子反而是圆顶。对此，只能说等到os更新的时候，对这个因子再次回测，看看这个因子到底跑的怎么样。现阶段肯定是不建议提交的，亏钱的几率非常的大。

所以，如果指标不是年年好，那就专注21年和22年。

游戏王名言：好的因子不应该受到任何特定事件的冲击，比如20年的疫情。

如果实在不能平滑向上，那就优先翘头而不是圆顶。

那什么才叫年年好呢？

从13年开始就有数据的，delay1的地区（我才刚开始尝试d0在此不做判断），对于sharpe而言，都大于1已经很不错了。有的人会问：是否允许有负的sharpe？我个人是允许的，只要不要发生在21年和22年。同时，负的幅度不要太大，一般就是-0.5以内。但凡比较大的负值，pnl看起来都会有些抽象，已经不满足我们的必须指标中的“pnl平滑”了。还有的人会说：这个因子有几年只有零点几的sharpe，能接受吗？这个时候最好的办法就是看这几年的margin。如果margin在这几年依旧达标，说明这个因子表现不是特别好、信号不是很强的时候依旧可以赚钱，那这个因子是值得肯定的。

可是有很多这样的问题：这个因子从18年开始才有数据，数据很漂亮，能不能交？

我的建议是，数据覆盖不超过8年的，都尽量不要交。意思就是，最多允许从15年开始有数据。

但这里提到一点，weijie老师在因子模版的帖子里的一个评论针对snt27的模版的有提到，观察数据更新频率，不失为一个好的因子。这里我只能说高手仁者见仁了。Snt27我至今都存着没敢交。

游戏王名言：如果你十年是逐年大于1，那5年是不是起码得逐年大于2？这甚至还只是一个下限，实际应该更加高。

我的建议就是，你把下面的滑动窗口视图拉大到有数据的那几年看看，是否符合我前面提到的必须要求？举例来说：


> [!NOTE] [图片 OCR 识别内容]
> UTTRA
> rJuno
> CTtR
> UTLIT-GU
> UTrt
>  TTTT
> 「
> TTIIFFI
> Coce
> Summar
> TJlI?N
> UII
> GRs
> ATIIIL
> 2.979
> 1.73
> 8.77%
> 3.41沆
> 59 C19
> T
> L
> UaS
> T
> N
> Rm
> 449
> ao
> U
> 5TIII
> |!$
> [
> Lsoaar
> 。
> Cna AI I
> Chart
> TII 51
> Ris eulnllied
> 295
> 4.4
> 265 
> 29.933e
> Inrestabllity
> CUIISITIIP
> 91 TTrPML
> IThIm CrrTIAHFm
> 2.843
> 909
> 3.809
> 55.56e
> Correlation
> IS Testing Status
> Tl Crrlalc



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> O0OK
> UOOK
> Mayq
> Sep"19
> Nay 20
> Jan 
> lan 22
> Sop22
> Jan'23
> PnL
> RIsk Neutralized Pn
> Investability Constraned Pn
> Sep
> May
> Ser
> Na


拉大之后，我们能看到这个pnl并不是很平滑，而且也是圆顶的（其实指标也看的出来），这个因子就不值得信赖了。

接下来我们来解析turnover。Turnover为什么不是越低越好？反而是维持在12%？这里我们要强调一个点。股票、期货等等，我们追求的是一个对冲的思想。我们通过合理的做多做空，来实现对市场变化的应变。大家可以理解为，如果我的turnover非常低，只有百分之一点几，那这只股票基本上一年下来就不交易多少次，更多的就变成了极其稳定的持仓，这和对冲流动的思想是相违背的。

游戏王名言：turnover很低的因子，我都不知道它赚的是什么钱。

Weijie老师名言：turnover 5%以下的因子，都是“死鱼”因子。

你要问这个12%的标准怎么来的，说实话我也不知道，就像各个地区的margin最低标准一样，我也不清楚怎么算出来的。但我们把turnover控制在一个良好的范围，就是为了能让因子的表现更加稳定（这也是出自一位大佬的总结，名字我也给忘了，在这里表示道歉和感谢）。其他表现几乎一致的情况下，能积极对冲的因子一定会比死鱼因子更加值得信赖的。

于我个人的理解，就是一般情况下控制在5%以上20%以下都是ok的。每个人可以根据自己的需要进行调整。什么叫进行调整？以我自己为例，我一开始做usa的时候，交了非常多换手率只有百分之一点几的超级死鱼因子。当时我的想法就是为了尽可能拔高margin。后来我意识到这种想法是错误的时候，鑫佬建议我提交一些换手率较高的因子来使combine的表现获得提升，因此接下来我就交了不少margin只有万分之五到十，但是turnover有20%到30%的因子。大家可以理解为我用刚刚达标的因子着重的提高turnover了。但这只是权宜之计，并不是值得学习的行为。

那有的兄弟会问，对于高换手的主题呢？

这里我必须得和大家讲述一下turnover和return，margin的关系。

我们都说，这是一个跷跷板，return一定，turnover越高margin越低。对于超高换手率，比如40%到50%，如果你的return一样可以做到40%，那我觉得这个因子你提交完全ok的，这一定是一个不错的因子。但如果你的return只有15%，换手率还如上，那我觉得这就是一个亏钱因子了。为啥换手率高会亏钱？因为每一次换手都有手续费呀。换的越多手续费越多。你的因子赚的钱都不够交手续费，那只有亏钱的道理。

但是对于死鱼因子，我自己有一个不太一样的看法。在你对于一个因子的质量实在是拿不准的时候，死鱼因子就是一个很好的提交方式。你通过把turnover压得很低来大幅度提高margin，让因子的样本内表现看起来相对还可以。同时，由于是死鱼因子，搞笑一点来说，就算是亏钱因子，也亏不了多少钱，因为你的因子几乎不交易（令人哑然失笑）。因此，换手率极低并非完全不可取，还是那句话，你需要依你自己的情况而定。

对于drawdown这个指标，没有什么特殊的情况，肯定越低越好。但大家肯定遇到过下面这个样子的因子：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> Irto  Iy
> Nnu nul
> Cn R
> UTGI
> nNRA
> RrsNR
> CTTTILaU
> FTIIFFI711
> CTmNSI
> Coce
> Summary
> CUIT
> JIJV
> 41I1TNIMaAINTaL .
> MIMTII
> GR
> Aret?uU
> 22
> 2.45
> 21,91%
> 11459
> 59,49mm
> 16
> T
> Las
> T
> N
> Ro
> 14
> 2
> 
> [
> Lnear
> !
> TI TM
> Oo 
> 41
> Chart
> Jg
> Ta
> 
> Hsk MeULTAUIZEU
> 0.54
> 833%
> 11.055
> 2263-0
> Iet F
> OITTTTTPI
> AIrotdteDu
> 3.29-0
> 16.409
> 15.213
> 99747
> Correlation
> Os Testing Status
> Corlalc
> 1


这个因子的drawdown很高，都有百分之十了，这时候我们到底如何考虑呢？

我个人的建议就是：return覆盖drawdown，margin覆盖turnover

只要return比drawdown高，margin比turnover高，我觉得可以尝试。比如我这个因子，return20%以上显著大于turnover，这个是没问题的。

当然，这个因子大家能看到，多空并不是特别平衡。明显做多大于做空。所以这个因子赚的是多头的钱，相较于其他的多空平衡的因子就不是那么稳定了。

那到底多空要怎么看呢？这里我们也分三个点，这三个点平行考虑，不分先后。对于多空都很重要：

1. 多加空能覆盖universe是比较好的
2. 多基本上等于空
3. 多空不要浮动变化。什么是不要浮动变化呢？举例来说，比如TOP3000的universe，一个因子，一开始多空都是九百到一千，过了两年变成一千五到一千六，过了两年变成九百到一千。这说明这个因子选股经常选到具备某些特征的股票，这些股票不是每次都可以挤到TOP3000，挤进去的时候多空就拉起来，挤不进去就下降。相对来说稳健性依旧比不上多空不浮动的因子

所以我刚刚举例的这个drawdown很高的因子，几乎三点都不满足。不过就像排序一样，多空只要不是赌博，就可以放在最后考虑。问题不大（自我安慰）。

看到这里肯定很多朋友有疑问了。传奇耐打王难道不看performance comparison吗？

肯定要看的，接下来我们就来详细解析这个该怎么看。

答案：同优化指标。

意思就是，并不是说真的是“四绿两红”才能交，也不是“四绿中的至少两绿”才能交。判断逻辑与之前是一致的。首先sharpe和fitness肯定越高越好，但如果一个加一个减怎么办，那就算净值，净值更优的排更靠前。我基本上只重点关注这两个值，对于return和margin，只要持续保持达标以上，我觉得加加减减并不关键。还是游戏王那句话，我们要的是——稳赚！！！同理，turnover保持12%浮动，drawdown尽可能降低（偶尔有的因子拉起来一点问题都不大）。所以，这个performance comparison我觉得并不是判断的关键。下面拿一个因为performance comparison阻止我提交的因子举例：


> [!NOTE] [图片 OCR 识别内容]
> INm
> 2,30
> 643
> 2]
> 357泗
> 66
> 11.10
> 7 e
> ol4e
> 
> Tag
> N
> TU
> NU TCtCn
> 0+
> gse
> 28
> Cen Nohe
> Chyrt
> IntlCnnrlrai-
> AAIIOIAI』
> 4,033
> 2.769
> 2,384
> 13.6954
> Te LLIIy CrIoTsUF
> Correlaton
> 944』!


这个因子看起来都挺漂亮的，是一个ra，但是我的performance comparison显示是全红（真的心碎）。因此这个因子我最终放弃了。

大家不要觉得我粘贴出来的因子看起来质量都不错。我自己也交了不少sharpe只有不到1.3，fitness0.5出头的ppa，这些都没有绝对的标准。还是那句话，看你自己的需要。对于提交因子这件事情，大家一定要管得住自己的手，在保持理性的前提下，再做提交的思考。毕竟我们为的不是那一天得多少base，而是为了未来的每天都有更多base。

以上是对于因子提交的优化指标的讨论。到此这个系列暂时就完结了。如果对您有帮助，请留下您宝贵的赞。

如有不正之处，恳请佬们批评指正。大家有什么问题，或者还有什么没有归纳到位的地方，都可以在评论区留言提出。或者你带着你的因子截个图放到评论区，问问传奇耐打王能不能交，我也是非常乐意解答的。

最后祝大家都能vf1.0，combine节节高。

---

### 帖子 #21: 【经验分享】我的上分之路：Gold→Master→Grandmaster经验分享
- **主帖链接**: 【经验分享】我的上分之路GoldMasterGrandmaster经验分享.md
- **讨论数**: 37

大家好，我是25年参加了IQC之后在7月1日左右拿到顾问权限的，刚开始什么都不懂，连ppa是什么都不知道，也不知道六维是什么，拿到权限的7天后才提交了自己的第一个顾问因子，最后也是从新手课和众多大佬的经验帖子里面逐渐熟悉规则，在789三个月里成功从gold冲到master，10 11 12三个月从master冲上了grandmaster。(一)Gold→Master在最终结算的时候我的六维:我的提交与回测系统：我在7月，只做了eur和usa两个地区，一共提交了55个alpha，采用的是传统一二三阶代码，完全没有修改，但是最多只会做到二阶；在8月，做了glb、eur、asi，一共提交了73个alpha,由于传统二阶代码会严重拉跨平均操作符和平均字段，于是我逐渐舍弃二阶，并修改一阶中的模板；在9月，只做了usa这一个地区，由于时间不充裕，只交了23个alpha，延续了8月的风格，以压操作符和字段为主。我的combine:当时也是很惊讶能有这么高，更新到6月也就是iqc期间，我的combine是0.34,第二次更新到7月，记得好像是1.2，第三次更新到8月，combine最高来到了2.38;提交的核心标准是margin要达标，turnover不能过高，其他的综合来看，觉得不是很难看就交了，除了二阶里面的group类型字段，几乎没有做过双字段的alpha。(点塔图没有找到)（二）Master→Grandmaster最终结算的时候我的六维、combine、塔图:相比于上个赛季，我的工作流变化挺大的，1、提前过滤字段在传统一阶回测的时候经常会遇到缺数据的字段，这样既浪费了回测数量，也严重影响了我的心情，于是我以一个塔为单位，例如把一个region内所有归属于model的全部字段直接回测，提前把那些缺数据的字段拉黑，提高了后续回测任务的效率，并利用数据库来记录，判断缺数据的字段也很简单，利用api获取回测出来的alpha的每年的sharpe有多少个0就行了。2、优化模板流在传统的一阶回测或者是论坛中的一些模板，其大多都有个共性，也就是探索度太大了，在有限的回测次数内，出货效率很低，并且类似的模板对同一个字段跑出来的alpha的相关性过高，有时会花费过多回测数量在一个难以出货的字段上面，于是我做出改进，把每个模板 的探索度降为1，具体做法为：固定时间参数，固定操作符，比如group_op(ts_op(x,day),group),day我会取一个固定的值，group我只在market,industry,sector,subindustry中选一个，group_op我一般在group_rank,group_zscore,group_neutralize中选一个，ts_op也一样。目的是在较少的回测数量内挖掘出一个字段的基础信号，哪怕是微小信号也好。其次，把这些表达式批量写入数据库，每一组回测完后就回填数据，计算相关性，并做好标记以免重复回测。3、对alpha的初加工对上述回测完的alpha进行进一步的改进，设立了一个评分机制，同一个数据字段内的alpha为一组，对组内的alpha以sharpe、fitness、margin为指标进行打分，选取分值最高的并且相关性小于0.5的那个进入下一步的加工环节，传统的二阶是对所有sharpe、fitness满足条件的alpha进行提升，可是在同一个数据字段内的alpha本身相关性就很高，可能交了一个alpha后其他alpha可能都交不了了，为何不选择一个最好的来做二阶呢。加工我采用的是：遍历中性化、遍历时间参数、非线性变换、是否保留ts_backfill和winsorize；其中遍历时间参数以等差数列进行遍历，大约需要多回测9次，非线性变换主要包括tanh,sqrt,log,signed_power,arc_cos,exp；再批量把这些操作于这个分值最高的alpha上并写进数据库自动回测。4、对alpha的细加工对于初加工的alpha，我会人工去把它们组合起来，比如在最佳中性化下运用最佳的时间参数并看是否需要结合非线性变换，并确认是否需要删除多余操作符，把这样的表达式拿去平台回测，并进行细微的优化，比如turnover过高，我会加decay，weight超了，想办法去降。5、回测数量的分配每天回测就5000次，我们应该规划好这些次数拿来做什么，我是多塔同时出发，8个槽或者glb的四个槽，每一个槽都会回测不一样的塔，避免在一个难出的塔上面一直耗下去，在点亮了塔之后便停掉跑其他的，直到全部点亮或者点不亮时才会回去做一些好出的塔比如model、pv等凑数量。其他的基本和Q3一样，比如提交标准没变，combine更新到11月，其最高combine来到了3.02，点塔也是一个月最多三个地区，每个地区在一个月内我会尽可能交三十多个，平均一天3个加一个superalpha，唯一的变数是在12月，我只做了两个地区，usa的d0和d1，平均每天只交了2个加一个superalpha，同样的在Q3的最后一月，提交的数量相较于上个月少了很多，两次都导致我的vf骤降，combine微跌，但是影响这两个指标变化的因素有很多，我也不知道为什么会这样。踩过的坑：对于新人来说，冲刺master或者grandmaster的第一阻碍或许是最大连续回测天数，我最初没有看懂这个以至于到了顾问阶段回测天数断了，若是中途断了就需要在六维的其他方面花费更多的精力。思考&改进：有些模板彼此间就有很强的相关性，做出来的alpha彼此间大概率也是高相关性，可以计算单个数据字段内alpha间互相的相关性，利用多组数据，找到均值比较高的那组，删去指标较差的那个模板，以此来简化模板流。（还没有时间做）总结：想要在genius中获得高评级，点塔、六维、combine缺一不可，核心都是在有限的回测次数内做出大量优质alpha。===============================================最后祝愿大家所愿皆所得，vf wf combine base genius全都升！

---

### 帖子 #22: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【经验分享】我的上分之路GoldMasterGrandmaster经验分享_38932709256727.md
- **讨论数**: 37

大家好，我是25年参加了IQC之后在7月1日左右拿到顾问权限的，刚开始什么都不懂，连ppa是什么都不知道，也不知道六维是什么，拿到权限的7天后才提交了自己的第一个顾问因子，最后也是从新手课和众多大佬的经验帖子里面逐渐熟悉规则，在789三个月里成功从gold冲到master，10 11 12三个月从master冲上了grandmaster。

**(一)Gold→Master**

在最终结算的时候我的六维:


> [!NOTE] [图片 OCR 识别内容]
> 编辑六维指标 
> 编辑六维指标数据
> Operator Count:
> Operator
> 69
> 4.2
> Field Count:
> Field
> 200
> 1.7
> Community Activity:
> Max Simulation Streak:
> 25
> 89
> 更新排名
> 以 Expert 为 Universe
> 以 Master 为 Universe
> Grandmaster 为 Universe
> 总排名:279/699
> 总排名:309
> 279
> 总排名:107
> 70
> Operator Count: 455 名
> Operator Count: 347 名
> Operator Count: 109名
> Operator
> 454名
> Operator
> 210名
> Operator AVg: 48名
> Field Count: 661 名
> Field Count: 395 名
> Field Count: 104 名
> Field AVg: 260名
> Field AVg: 103名
> Field AVg: 25 名
> Community Activity: 356名
> Community Activity: 291 名
> Community Activity: 92 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Max Simulation Streak: 1135 名
> Max Simulation Streak: 526 名
> Max Simulation Streak: 110名
> Total Rank: 3322名
> Total Rank: 1873名
> Total Rank: 489名
> AVg:
> AVg:
> AVg:
> AVg:


**我的提交与回测系统：**

我在7月，只做了eur和usa两个地区，一共提交了55个alpha，采用的是传统一二三阶代码，完全没有修改，但是最多只会做到二阶；在8月，做了glb、eur、asi，一共提交了73个alpha,由于传统二阶代码会严重拉跨平均操作符和平均字段，于是我逐渐舍弃二阶，并修改一阶中的模板；在9月，只做了usa这一个地区，由于时间不充裕，只交了23个alpha，延续了8月的风格，以压操作符和字段为主。

**我的combine:**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.16
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.38


当时也是很惊讶能有这么高，更新到6月也就是iqc期间，我的combine是0.34,第二次更新到7月，记得好像是1.2，第三次更新到8月，combine最高来到了2.38;提交的核心标准是margin要达标，turnover不能过高，其他的综合来看，觉得不是很难看就交了，除了二阶里面的group类型字段，几乎没有做过双字段的alpha。

(点塔图没有找到)

**（二）Master** → **Grandmaster**

最终结算的时候我的六维、combine、塔图:


> [!NOTE] [图片 OCR 识别内容]
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.69
> 125
> 1.34
> Fields used
> Community activity
> Max simulation streak
> 311
> 48.4
> 181



> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 3.02



> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> CHN
> KOR
> TN
> HKG
> JPN
> AMR
> Analyst
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 10
> 14
> 14
> 10
> 13
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


相比于上个赛季，我的工作流变化挺大的，

**1、提前过滤字段**

在传统一阶回测的时候经常会遇到缺数据的字段，这样既浪费了回测数量，也严重影响了我的心情，于是我以一个塔为单位，例如把一个region内所有归属于model的全部字段直接回测，提前把那些缺数据的字段拉黑，提高了后续回测任务的效率，并利用数据库来记录，判断缺数据的字段也很简单，利用api获取回测出来的alpha的每年的sharpe有多少个0就行了。

**2、优化模板流**

在传统的一阶回测或者是论坛中的一些模板，其大多都有个共性，也就是探索度太大了，在有限的回测次数内，出货效率很低，并且类似的模板对同一个字段跑出来的alpha的相关性过高，有时会花费过多回测数量在一个难以出货的字段上面，于是我做出改进，把每个模板 的探索度降为1，具体做法为：固定时间参数，固定操作符，比如group_op(ts_op(x,day),group),day我会取一个固定的值，group我只在market,industry,sector,subindustry中选一个，group_op我一般在group_rank,group_zscore,group_neutralize中选一个，ts_op也一样。目的是在较少的回测数量内挖掘出一个字段的基础信号，哪怕是微小信号也好。

其次，把这些表达式批量写入数据库，每一组回测完后就回填数据，计算相关性，并做好标记以免重复回测。

**3、对alpha的初加工**

对上述回测完的alpha进行进一步的改进，设立了一个评分机制，同一个数据字段内的alpha为一组，对组内的alpha以sharpe、fitness、margin为指标进行打分，选取分值最高的并且相关性小于0.5的那个进入下一步的加工环节，传统的二阶是对所有sharpe、fitness满足条件的alpha进行提升，可是在同一个数据字段内的alpha本身相关性就很高，可能交了一个alpha后其他alpha可能都交不了了，为何不选择一个最好的来做二阶呢。

加工我采用的是：遍历中性化、遍历时间参数、非线性变换、是否保留ts_backfill和winsorize；其中遍历时间参数以等差数列进行遍历，大约需要多回测9次，非线性变换主要包括tanh,sqrt,log,signed_power,arc_cos,exp；再批量把这些操作于这个分值最高的alpha上并写进数据库自动回测。

**4、对alpha的细加工**

对于初加工的alpha，我会人工去把它们组合起来，比如在最佳中性化下运用最佳的时间参数并看是否需要结合非线性变换，并确认是否需要删除多余操作符，把这样的表达式拿去平台回测，并进行细微的优化，比如turnover过高，我会加decay，weight超了，想办法去降。

**5、回测数量的分配**

每天回测就5000次，我们应该规划好这些次数拿来做什么，我是多塔同时出发，8个槽或者glb的四个槽，每一个槽都会回测不一样的塔，避免在一个难出的塔上面一直耗下去，在点亮了塔之后便停掉跑其他的，直到全部点亮或者点不亮时才会回去做一些好出的塔比如model、pv等凑数量。

其他的基本和Q3一样，比如提交标准没变，combine更新到11月，其最高combine来到了3.02，点塔也是一个月最多三个地区，每个地区在一个月内我会尽可能交三十多个，平均一天3个加一个superalpha，唯一的变数是在12月，我只做了两个地区，usa的d0和d1，平均每天只交了2个加一个superalpha，同样的在Q3的最后一月，提交的数量相较于上个月少了很多，两次都导致我的vf骤降，combine微跌，但是影响这两个指标变化的因素有很多，我也不知道为什么会这样。

**踩过的坑：**

对于新人来说，冲刺master或者grandmaster的第一阻碍或许是最大连续回测天数，我最初没有看懂这个以至于到了顾问阶段回测天数断了，若是中途断了就需要在六维的其他方面花费更多的精力。

**思考&改进：**

有些模板彼此间就有很强的相关性，做出来的alpha彼此间大概率也是高相关性，可以计算单个数据字段内alpha间互相的相关性，利用多组数据，找到均值比较高的那组，删去指标较差的那个模板，以此来简化模板流。（还没有时间做）

**总结：**

想要在genius中获得高评级，点塔、六维、combine缺一不可，核心都是在有限的回测次数内做出大量优质alpha。

===============================================

最后祝愿大家所愿皆所得，vf wf combine base genius全都升！

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《【Alpha灵感】基于MCP提交的3个Short Interest 因子》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】基于MCP提交的3个Short Interest 因子.md
- **评论时间**: 9个月前

感谢大佬的分享，我也用的deepseek，前段时间太忙没有花很多时间在mcp上，但是我觉得我也有点像楼主评论区所说的差不多，对数据字段还有模板的研究不是那么透彻，自然对mcp的训练和提问上有点生涩；楼主分享的内容给了我对mcp的一定的启发，待我去实践实践

---

### 探讨 #2: 关于《【Alpha灵感】基于MCP提交的3个Short Interest 因子》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】基于MCP提交的3个Short Interest 因子_34407581314583.md
- **评论时间**: 9个月前

感谢大佬的分享，我也用的deepseek，前段时间太忙没有花很多时间在mcp上，但是我觉得我也有点像楼主评论区所说的差不多，对数据字段还有模板的研究不是那么透彻，自然对mcp的训练和提问上有点生涩；楼主分享的内容给了我对mcp的一定的启发，待我去实践实践

---

### 探讨 #3: 关于《【ValueFactor涨分宝典】一个月从0.5→0.99的涨分之旅论坛精选》的评论回复
- **帖子链接**: [Commented] 【ValueFactor涨分宝典】一个月从05099的涨分之旅论坛精选.md
- **评论时间**: 10个月前

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------感谢大佬分享，我现在对于何为好的alpha有了清晰的认识，我最近一次更新vf从0.5跌到了0.25，看着每天超低的base心灰意冷，读了大佬的帖子我备受鼓舞，以后要坚持多交alpha，多交好的alpha,同时我阅读了游戏王worldquant brain赛博游戏王的sa帖子，收获颇丰，相信不久的将来我的vf一定会有质的提升！！！--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #4: 关于《【ValueFactor涨分宝典】一个月从0.5→0.99的涨分之旅论坛精选》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【ValueFactor涨分宝典】一个月从05099的涨分之旅论坛精选_34283569758999.md
- **评论时间**: 10个月前

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------感谢大佬分享，我现在对于何为好的alpha有了清晰的认识，我最近一次更新vf从0.5跌到了0.25，看着每天超低的base心灰意冷，读了大佬的帖子我备受鼓舞，以后要坚持多交alpha，多交好的alpha,同时我阅读了游戏王worldquant brain赛博游戏王的sa帖子，收获颇丰，相信不久的将来我的vf一定会有质的提升！！！--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #5: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年11月27日

由于当时这几天去旅游了，遂将这几天的补上

今天交满了，交了4个jpn的ppa，涉及fundamental,analyst,model,instituitons，可谓是把分散化做到了极致，但是sharpe还是偏低了，在jpn好难做出那些sharpe高的alpha啊，可能是我实力还不够，交的是asi的sa

今日base指标：

sa：54.59dao  交的是asi notown 520，感觉base和我vf0,91差不了多少

ra:6.12dao 稍微比前几天高了1dao

================================坚持！=====================================

---

### 探讨 #6: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年11月28日

这个月快结束了，于是交了一个jpn 的own sa来稳一稳combinde，同时交了2个amr的ppa来提升一下我的六维，现在交的是之前的库存，而现在开始是为了下个月的d0做准备，已经跑出很多可以提交的alpha了

今日base指标:

sa:8.21dao  jpn own 不是35，单5，都能达到这个base，比三五只低一两刀

ra:2.98dao  这个月最低的base，现原形了，希望下次我的vf还能上0.9

===============================坚持！-===============================

---

### 探讨 #7: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年11月29日

今天不知不觉就交满了，交了4个amr的ppa，涉及fundamental,institutions,和两个analyst，发现我的存货还挺多的，交了这些还有三十多个可以立马提交的，看来下个赛季不用愁了，但是剩下的指标肯定没有这个月提交的好，还是要做一些取舍的，顺便交了1个amr的own sa

今日base指标：

sa:8.09dao  同样的单5，差不多8dao左右了，还是很有性价比

ra:6.51dao  看来交满了还是给的挺多的，但是我现在平均一天就交个3.5个吧，交满确实很吃力

===================================坚持！=================================

---

### 探讨 #8: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：22025年11月30日

今天是这个月的最后一天了，今天结束这个赛季的combine就定型了，今天交了一个asi的model ra和一个amr的analyst和model的ppa，隔了十多天又再次交了一个asi的，主要是这个ra是存货，等到下一次交这个alpha估计几个月之后了吧，担心prod涨上去就干脆交了，又交了一个asi的notown 520

今日base指标：

sa:57.62dao  asi notown 520 fitness也是有8了

ra:4.28dao

==============================坚持！=========================================

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月01日

今天是这个月第一天，我也是打算开始做d0了，先把前几天回测出来的存货交一下，交的是两个usa d0 model和fundamental的，其中有一个alpha的sharpe甚至大于4，fitness大于3，可惜只是个ppa啊，也是第一次做出is这么好看的alpha，也是希望os不要太拉跨了，今天sa也交的是asi 520

今日base指标：

sa:53.77dao asi notown 520 略有下降

ra:4.51dao  交的alpha的prod都有点高了

====================================坚持!==================================

---

### 探讨 #10: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月02日

今天交满了，依然交的usa d0 的model pv other，都是ppa，sa还是asi notown 520,而且最近发现asi有了一个新的测试，发现以前屯的520都不能用了，还是很苦恼，又得重新开始做，d0一个月只能交30个，我还得合计合计该交些什么，金字塔是肯定不用担心的了，那就尽可能多的分散化一点吧，目前就准备点analyst fundamental other model  pv news这6个数据集的，d0的小数据集实在不敢碰，而且现在做也没什么意思

今日base指标：

sa:56.15dao asi notown 520  指标没有昨天的好

ra:4.6dao  乘数还是太低了

===========================坚持！====================================

---

### 探讨 #11: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月03日

今天还是坚持交满，交的是usa d0的两个model，一个ppa和一个ra，以及fundamental和pv的ppa，还是坚持在d0全部做成atom，不想去混信号，而且我发现我刚成为顾问的那三个月只做出来了一个ra，而现在做ra还是很简单的，一路走下来我还是一直在进步的，要继续保持一股学习的劲，今天的sa也是asi的520

今日base指标：

sa:52.27dao  asi notown 520，我发现最近的sa都是一天高一天低的很有规律，而且呈现的是下降趋势

ra:4.94dao

=============================坚持！=====================================

---

### 探讨 #12: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月04日

今天没有交满，其实这几天交的都是上个月跑的存货，这几天确实没有多少时间，太忙了，期末周也快到了，但是我的工作流已经很完备了，今天交的两个option的usa d0的ppa，用的是魔改论坛模板的，质量非常好，但是prod太高了，我甚至觉得我都快被踢出群了，因为usa的prod实在太高了，外加准备冲grandmaster又要保持多提交

今日base指标：

sa:54.54dao  交的asi notown 520，fitness甚至到了12，

ra:4.83dao  非常稳定，不多不少的

=============================坚持！====================================

---

### 探讨 #13: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月05日

今天交了usa d0 的option model news，现在把option的塔已经点掉了，最近都打算每天交三个alpha了，值得庆幸的是今天我的weight终于突破0了，来到了0.01，还是很惊喜的，从6月成为有条件顾问参加iqc以来过了这么久，终于来了，今天交了一个asi的520,fitness有8.53，我交的520的指标都很好，margin高，近两年来无衰减，希望不要对我的vf和combine造成较大的影响吧

今日base指标：

sa:52.10dao  越来越低了，不会后面会跌破50dao吧，其实拿这么多已经足够了

ra:4.52dao

==================================坚持!=================================

---

### 探讨 #14: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月06日

今天终于有时间写量化日记了，于是把之前的补上，一次性写了10条，今天交的是usa d0的三个ppa，涉及一个other一个fundamental一个model,从前天起就彻底结束对usa d0的回测了，算了一下，开始usa d0的回测也就8天吧，交满30个戳戳有余的，算上相关性问题，下赛季应该还有十多个的存货，出货率还是很不错的，而且后4天也是开了5个槽给eur d0跑，但是这一周的prod确实超标了，估计马上就收到警告了，准备下一周开始ind的回测和提交，来降低一下prod，但是还要在交10个usa d0，prod真是令人头大啊，在小地区一点也不用考虑prod的问题，怎么跑都是低相关性

---

### 探讨 #15: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月07日

今天交了3个alpha，包括usa d0的2个analyst的ppa，和一个asi的not own 520，以前总觉得analyst很好跑，觉得是仅次于model的第二好跑的数据集，可是这个赛季我发现analyst数据集不仅多，还比较难出货，对usa d0 analyst单槽回测了8天，只找到4个稍微好一点的ppa，然而other都找到了十个，同样体现于amr和jpn

今日base指标:

sa:54.63dao  asi not own 520，今天是连续上涨的第三天

ra:3.93dao rabase也是第一次跌到4dao以下了

===============================坚持！=====================================

---

### 探讨 #16: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月08日

今天开始限流了，平时我都会跑到2w个以上的，突然砍了一半要好好适应一下了，而且今天更新combine了，意料之中的涨了，因为我10月交了一百个alpha，涉及usa eur asi，都是大区，而且做的还算好，涨了大概0.6左右，但是下一次更新大概率是跌的，因为我交了amr和jpn，第一次做小地区，个人感觉jpn做的很不好，而且参加了aiac，交了很多差的sa，而且交了很多520,只希望不要暴跌就好了

今日base指标：

sa:54.67dao  连续四天上涨了，很好看的一个上涨曲线

ra:5.49dao 一个other一个analyst，把usa d0 analyst的塔点掉了，到目前为止点了56个塔了，现在倒不着急了，不过今天交两个竟然比平时交四个还要多

==================================坚持！====================================

---

### 探讨 #17: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月09日

最近在跑IND,analyst pv fundamental news model五个数据集各一个槽来跑，跑了接近两天了，只有model一个数据集有一阶跑完就有PASS的alpha，还不少，我随便找了几个去测相关性，不是0.95+就是0.85＋的，我寻思着我也没有全用传统一阶啊，pc都这么高，真的好难跑啊，不过现在只是初筛，还没有进行二阶变换，先跑一跑再说，最近几天就先交着usa d0的存货吧，还能交个3天左右，做完usa d0之后打算交ind或者eur d0了，但是做eur d0的化这个月只能交60个，上个月交了100个，感觉变化幅度有点大，对我之后的vf有负面效果

=================================坚持！======================================

---

### 探讨 #18: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月10日

今天交了3个alpha，一个asi的520的not own以及两个usa d0的other数据集的，最近没货了，故打算之后每天就交两个ra/ppa和一个ppa，毕竟现在已经点了56个塔了，点塔倒没有什么问题，六维和combine也看得过去，想囤一囤留给下一个赛季交，况且上个月交了100个，提交alpha的数量不能急剧下降，先缓降一下

今日base指标：

sa:54.68dao   依旧在54dao左右，还能吃几天的notown就要开始交own的sa了

ra:4.56dao

====================================坚持！================================

---

### 探讨 #19: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月11日

今天交了三个alpha，一个asi的520的not own和两个usa d0的other以及model，唯一的缺点就是sharpe太低了，不过上周我的pc超了，这周要保持低pc，我交完了才发现sa也算d0的额度，可是现在已经交了30个了，导致我不能交sa来稳combine了，天塌的，下次更新到12月岂不是我的combine和vf不保了，而且自我感觉我交的质量不好，而且还说去做eurd0的，没想到这个每月30个的额度还不分地区，明明已经跑了好几天的eur d0，挖到了几十个ra/ppa准备交的时候发现交不了，现在除了ind已经没货了，可是ind风险也太高了，于是转向usa d1，刚好还差4个塔顺手给点掉，问题是现在没有存货，只能翻翻垃圾交了

=====================================坚持!================================

---

### 探讨 #20: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月12日

今天只交了两个了，一个asi的520的not own sa和一个usa d1的analyst数据集的ppa，这个月剩下的日子打算在usa d1交上30个alpha就足够了，现在开始慢慢跑，现在交的都是存货里面的垃圾，剩下的own额度就交usa d1的sa吧，这几天还在拉数据库，要先跑一下裸字段，之后才能正式开始跑，这样能直接把缺数据的字段给排除掉，导致现在的进度一直为0。

今日base指标：

sa:53.87dao  差不多

ra:1,93dao  骤降，直接减半了，最低的一次

======================================坚持！=================================

---

### 探讨 #21: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月13日

今天也交了两个apha，一个usa的own双五，现在不追求三五了，两者的base对于我这个vf来说就是一两dao的差距，没必要废那么多功夫，我现在追求高margin，其次，我今天交了一个anayst+earnings的双字段alpha，其实不想交双字段的，确实是没办法就交了，指标还行的，还能接受吧，今天交了之后后面就没有存货了，虽然还有几个，但是质量实在太差，sharpe连1.2都没有，pc也高。

到这个赛季结束，我得交9个own和9个notown，usa的现在的alpha不算user和iqc交的一共有一百个了，足够我交很多ownsa了

=================================坚持！======================================

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月14日

今天交了两个alpha，一个是asi的520 not own的，我发现我最近交的asi的sa真的太多了，不过这个月也就只做了usa d1 和d0，之后交了一个usa d1的model，昨天跑了5000次，出了十多个可以交的，还算不错，就是pc大多数都高于了0.7，应该是模板不具有独特性还有就是这些字段都被别人用的太多了，因为我昨天跑的是model和option的，还没有测option有多少可以交的，不过应该也能有几个吧，这样来说就算限制了5000个回测我应该也是有生存的余地了

昨日base指标：

sa:8.04dao 我倒是很惊讶，usa d1双五都能拿这么多，可是usa d1的sa我做不出三五

ra：1.91dao  习惯了，交一个而且没有乘数是这样的

=====================================坚持！=====================================

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

我的量化日记

日期：2025年12月15日

今天终于交了四个alpha了，交的是一个usa d1 的own sa 双5，不过都是几个月前的库存了，自从限流了之后再也没有跑过sa，先把库存交完了再说吧，另外交的三个ppa是usa d1的model和imbalance，今天把imbalance的塔点掉了，那截至目前为止点了57个塔了，还剩三个，估计一个星期之内能点完。今天vf更新了，不过我发现变化不大，应该微跌了，昨天交的一个usa d1 ppa只有1.81dao，而前天同样的usa d1 ppa确有1.91dao，现在vf是0.89dao，那我估计我是0.88 0.87 0.86的样子吧，不过我10月的combine大涨了，vf确降了，太难受了！

============================坚持！=====================================

---

### 探讨 #24: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月1日（回忆版）

今天交了3个eur的ra/ppa和一个eur的555

region universe sharpe fitness margin

EUR TOP2500 5.9200 5.9600 0.0020

EUR TOP2500 3.3200 2.6000 0.0018

EUR TOP2500 2.7600 2.1900 0.0021

EUR TOP2500 2.7600 1.9100 0.0012

今日base指标：

sa:33.1刀，0.89vf，赛季第一天三五就能达到这么高，有点不理解

ra:4.46刀

================================越努力，越幸运=============================

---

### 探讨 #25: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月2日（回忆版）

今天又交了3个eur的ppa/ra，和一个eur555,感觉最近交的alpha质量都很好啊

region universe sharpe fitness margin

EUR TOP2500 6.0600 5.9500 0.0019

EUR TOP2500 2.6800 2.0300 0.0012

EUR TOP2500 2.5800 1.7100 0.0016

EUR TOP2500 1.9700 1.2100 0.0011

今日base指标：

sa:9.72刀,同样的三五，都是own，昨天和今天就差了好几倍，因为昨天大家只能交own的，今天开始才能交not own的

ra:3.49刀,蚊子腿罢了

==============================越努力，越幸运=============================

---

### 探讨 #26: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月3日（回忆版）

今天和前两天一样，三个eur的ppa/ra，一个eur的own 555，做的很分散，基本上都涉及不同的数据集

region universe sharpe fitness margin

EUR TOP2500 6.6200 6.0600 0.0017

EUR TOP2500 2.1800 1.4600 0.0021

EUR TOP2500 1.7600 1.1000 0.0015

EUR TOP2500 1.6400 0.8900 0.0013

今日base指标：

sa:20.32刀,交的是own eur 555，同样的表现，比昨天高了一倍还要多

ra:3.70刀，没有做主题，就值这个价

==============================越努力，越幸运=============================

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月4日（回忆版）

今天交了3个eur的ppa/ra，希望能稳住这个节奏，还交了一个asi的not own553，这几天对eur的margin不太满意

region universe sharpe fitness margin

ASI MINVOL1M 7.1600 8.0800 0.0025

EUR TOP2500 2.1400 1.4000 0.0021

EUR TOP2500 2.0900 1.3000 0.0012

EUR TOP2500 2.0300 1.1100 0.0012

今日base指标：

sa:54.02刀，爽啊，asi not own 553，要的就是这个感觉

ra:3.68刀，没记错这几都在交了些ra吧，还是这么低

===========================越努力，越幸运==============================

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月5日（回忆版）

今天开始就交不动了，限制5000回测还是太吃力了，没有存货可交了，点塔可是个大问题，今天交了一个eur的own sa 555

region universe sharpe fitness margin

EUR TOP2500 6.2300 5.3300 0.0015

EUR TOP2500 2.0300 1.3200 0.0010

今日base指标：

sa:15.86刀，交的是eur own 555，奇数日交的sa的base越来越少了，看起来马上要回归正常水平了

ra:1.9刀，只交了一个就直接锐减啊

=============================越努力，越幸运===========================

---

### 探讨 #29: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月6日（回忆版）

开始限制只能交ind地区的ppa了，没办法，只能全力以赴点ind的塔了，但就是pc太高了，进攻ind的第一天还没有看到一个pc小于0.7的可以交的，顺便今天交了一个asi的not own  553

region universe sharpe fitness margin

ASI MINVOL1M 7.2200 7.5700 0.0022

IND TOP500 3.7500 5.0700 0.0054

今日base指标：

sa:55.5刀,交的是asi not own 553，交的还是存货，最近都不用回测sa

ra:3.68刀，相较于昨天交的eur，带了主题的比没有主题的还是多了个一倍

=============================越努力，越幸运==============================

---

### 探讨 #30: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月7日（回忆版）

又是缺粮的一天，今天交了一个eur的ra来过过渡，顺便降低一下平均prod，交了一个eur own 555

region universe sharpe fitness margin

EUR TOP2500 6.9300 6.5000 0.0018

EUR TOP2500 1.9400 1.1100 0.0012

今日base指标：

sa：9.94刀，eur的own的555，最近eur的三五存货交完了，要重新回测了，但是我发现现在比以前更难出三五，测了几十个都没出

ra:1.94刀,太少了太少了

==============================越努力，越幸运==============================

---

### 探讨 #31: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月8日(回忆版)

今天只交了两个alpha，一个asi的not own 553,还有一个ind的model ppa;

指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 8.4200 8.3400 0.0020

IND TOP500 1.9500 2.5800 0.0035

今日base指标：

sa:56.32刀,553的威力还是猛

ra:6.32刀，给的真多，就交一个就给这么多，太阳出西边出来了

===========================越努力，越幸运====================================

---

### 探讨 #32: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月9日（回忆版）

今天依旧交了两个alpha，库存已经没有了，相冲grandmaster还是有点难度啊，点塔是个大问题，交的是ind的ppa的model，指标非常爆炸，sa交的是eur的own的55吧，没有去追求555了，没啥意义

指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.9800 5.9200 0.0023

IND TOP500 3.5300 4.4900 0.0032

今日base指标：

sa:10.43刀，交的是eur own 557,拿那么多也算可以的了

ra:3.09刀，不错啊，之前交一个就1.9刀，进步了不少

=================================越努力，越幸运=============================

---

### 探讨 #33: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月10日（回忆版）

今天交了3个alpha,有进步了，交的是2个ind的ppa，之后还交了一个asi的not own 553，还是很不错的，ind的ppa还是特别好做，就是robust难搞

今日指标：

region universe sharpe fitness margin

ASI MINVOL1M 10.5100 10.6700 0.0021

IND TOP500 2.2000 2.0800 0.0071

IND TOP500 1.5300 1.3200 0.0033

今日base指标：

sa:9.71刀，原来交的时候交错了，交上去pc变成0.31了，错失好几十刀，太心痛了

ra:4.28刀，

===================================越努力，越幸运=============================

---

### 探讨 #34: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月11日（回忆版）

今天竟然交满了，为了点塔，把前几天回测的货拿出来跑一跑出来了一大堆，交了4个ind的ppa，和一个asi not own 553，

指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.3000 5.5000 0.0022

IND TOP500 2.3900 2.1600 0.0016

IND TOP500 1.9200 1.8200 0.0020

IND TOP500 1.7700 1.3400 0.0018

IND TOP500 1.3500 1.5900 0.0143

今日base指标：

sa:56.31刀，给力了，爽爽爽，asi not own 553

ra:4.58刀，四个才这么少一点，以前四个可是能有7 8 刀的啊

=================================越努力，越幸运================================

---

### 探讨 #35: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月12日（回忆版）

今天依旧交满了，很开心啊，快速点塔追上大部队，今天交的是4个ind的ppa，还有就是一个asi的not own 553，因为感觉快更新vf了，对vf没有什么把握，先把not own交完了再说，

今日指标：

region universe sharpe fitness margin

ASI MINVOL1M 7.1700 8.2800 0.0027

IND TOP500 3.1800 3.9100 0.0030

IND TOP500 1.9100 1.9100 0.0028

IND TOP500 1.8500 1.8200 0.0026

IND TOP500 1.6000 1.3700 0.0024

今日base指标：

sa:53.41刀,比昨天的asi not own 553少了3刀啊，不知道为什么

ra:4.77刀，比昨天略多一点点

===============================越努力，越幸运==================================

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月13日（回忆版）

今天交满了，今天是交满的第三天了，依旧4个ind的ppa加一个eur的own 557，表现依旧很强啊今天

今日指标如下：

region universe sharpe fitness margin

EUR TOP2500 7.8900 9.5400 0.0038

IND TOP500 3.2400 2.9000 0.0016

IND TOP500 2.7800 3.1200 0.0037

IND TOP500 2.3300 3.5800 0.0168

IND TOP500 2.0100 1.7900 0.0016

今日base指标如下：

sa:8.55刀，交的eur own 557，base是显著下降啊，不过就算交的是555，也就估计10刀左右吧

ra:4.83刀，每天都在上升，但是没有什么用

==============================越努力，越幸运================================

---

### 探讨 #37: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月14日（回忆版）

今天没有交满了，今天交的是ind的3个ppa，和一个asi 的not own 的553,总计一共4个，前面交的太猛了，需要缓冲以下子了，

今日指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.7400 6.1800 0.0023

IND TOP500 2.8700 3.1600 0.0024

IND TOP500 1.7600 1.7600 0.0022

IND TOP500 1.5300 1.1300 0.0056

今日base指标如下：

sa:53.54刀，交的还是asi的not own 553，最近都在交asi,正好马上要出glb的theme了，准备not own转战glb试试

ra:4.03刀，下降了

==========================越努力，越幸运===============================

---

### 探讨 #38: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月15日（回忆版）

今天交了3个alpha，都是ind地区的，包括两个ind ppa和一个ind own sa，ind的sa指标看着特别舒服，margin和fitness看着都特别高，

alpha指标如下：

region universe sharpe fitness margin

IND TOP500 6.0900 10.3900 0.0080

IND TOP500 2.7500 2.9500 0.0024

IND TOP500 1.6400 1.9500 0.0097

今日base指标如下：

sa:8.55刀，上个月这个时候同样的双五要比这个低一点，交的是ind的own 557，

ra:3.37刀，两个alpha

================================越努力，越幸运==================================

---

### 探讨 #39: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月16日（回忆版）

今天同样交了3个alpha，包括两个ind的ppa点塔和一个asi的not own 553，此时ind地区的塔基本上1点的差不多了，没一个塔点了就撤，剩下的留给下一个赛季，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.0800 5.3200 0.0022

IND TOP500 2.4000 2.5000 0.0022

IND TOP500 1.9900 2.6200 0.0149

今日base指标如下：

sa:53.51dao,交的是asi的not own 553，相比前几天少了两三刀的样子

ra:3.88dao，比昨天高，估计是pc有点低

=============================也越努力，越幸运===============================

---

### 探讨 #40: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月17日（回忆版）

今天仍然交了3个alpha，交了两个ind的ppa和一个ind的own sa，ind到现在已经交了二十多个了，model还有十多个存货没有交，打算再交几个model的来稳一稳凑够30个，

今日alpha指标如下：

region universe sharpe fitness margin

IND TOP500 6.3600 9.9400 0.0064

IND TOP500 2.7600 2.7800 0.0043

IND TOP500 2.3500 2.3400 0.0033

今日base指标如下：

sa:8.76dao，可能是要多了一点，无关大雅，交的own sa ind 557，也就这样

ra:4.37dao，比前几天交的大概多了不到一刀的样子

==============================越努力，越幸运=============================

---

### 探讨 #41: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月18日（回忆版）

今天只交了两个alpha，交的是一个ind的ra，还有交的一个是glb的not own 553，之前一直没有在glb做过sa，今天去试了试，大概回测50个，找到了一个553，也是第一次在除了asi之外做出了一个553，但是指标并没有asi那样高，

今日alpha指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 6.3400 5.3400 0.0015

IND TOP500 1.2300 1.0600 0.0111

今日base指标如下：

sa:56.43dao，glb的not own 553确实要比asi的高个一两刀吧，但是效果也不是很明显

ra:1.97刀，果然，交的少就是给的少

==========================越努力，越幸运==========================

---

### 探讨 #42: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月19日（回忆版）

今天只交了两个alpha，同样是交的ind的一个ra，还有一个ind的sa，现在做ind的own sa有点困难了，做了一百多个才出了一个pc小于0.7的，这样有点难搞哦，ind的ra提交也快进入尾声了，已经在做glb了，glb回测真啊，很难回测完

今日alpha指标如下:

region universe sharpe fitness margin

IND TOP500 5.2100 7.2600 0.0039

IND TOP500 2.3400 2.1100 0.0016

今日base指标如下:

sa:8.69dao,交的是ind own 557，竟然比平时交的双五又要多一点了

ra:3.61dao，交一个竟然比前几天交两个甚至三个还要多，估计是pc比较低吧，搞不懂

=============================越努力，越幸运=============================

---

### 探讨 #43: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月20日（回忆版）

今天交了3个alpha，其中包括两个ind的ra，和一个asi的not own 553，到目前为止点了14个塔了，点塔好困难啊，而且glb只开放了四个塔的ppa，这不就是变相的只能做ra了吗，可是现在做ra好困难，很多存货都没有了，点到60个塔也太难了，时间和精力花在这上面的时间只能越来越多，但是一个gm也给的多啊，只要有机会，还是要继续冲gm的，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 6.5400 5.8800 0.0016

IND TOP500 1.9400 1.5800 0.0028

IND TOP500 1.8400 1.7900 0.0059

今日base指标如下;

sa:58.47dao，交的是asi 的not own 553，也是第一次553拿到这么高，有点高兴

ra:350dao，交了两个

============================越努力，越幸运===============================

---

### 探讨 #44: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月21日（回忆版）

今天交了两个alpha,也是过了十多天再次交eur啊，交的是一个eur的ra和一个eur的own sa，主要是glb出的货不多，而且质量是真的很差，所以交了一个eur的ra点了两个塔，现在我点到16个塔了，长路慢慢啊，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.5300 5.2500 0.0020

EUR TOP2500 1.9400 1.4200 0.0025

今日base指标如下:

sa:8.74dao,还行吧，就这个水平，就只有那么多

ra:1.93dao，一个，大多数情况就是这么多，没有主题

=================================越努力，越幸运=============================

---

### 探讨 #45: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月22日

今天交了四个alpha，其中有三个ind的ra，以及一个asi的not own 553，虽然现在ppa主题在glb，但是那些数据集出不了什么特别好的alpha，于是我就继续去做ind，做ra来点点塔，争取再多点一两个，glb暂时先不交，看情况，

今日alpha指标如下:

region universe sharpe fitness margin

ASI MINVOL1M 7.4100 7.1400 0.0019

IND TOP500 2.6600 2.3200 0.0015

IND TOP500 2.0400 1.7700 0.0017

IND TOP500 1.5800 1.5100 0.0061

今日base指标如下：

sa:56.25dao,交的是asi 的not own 553

ra:4.51dao,交了三个非主题ind 的ra

=================================越努力，越幸运==================================

---

### 探讨 #46: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月23日

今天就只交了两个alpha了，交的是一个glb的主题ppa和一个ind的own sa,ind的sa我是把那些os表现不好的打上标，之后选alpha的时候就不选这些，不然看着太难受了，这样做出来的sa看着还挺漂亮的，glb还是得交着走啊，这个月就开eur ind glb这三个地区吧，剩下这几天要多交glb的ra啊，不然交的太少了容易炸，

今日alpha指标如下：

region universe sharpe fitness margin

IND TOP500 5.4100 7.7200 0.0041

GLB MINVOL1M 2.1700 1.3400 0.0009

今日base指标如下：

sa:8.4dao,交的Ind own sa 557，目前不想去刻意做三五，就回测十多个交了就好了

ra:2.39dao，一个glb的主题ppa，没有主题差不多应该1.9刀的样子

=================================越努力，越幸运==============================

---

### 探讨 #47: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月24日

今天交了4个alpha，其中包括一个asi的not own 553和两个glb的ra以及一个glb的ppa，glb的点塔之路好漫长，回测太慢了一点也不想做，外加只能四个槽，ra也不好做，而且做出来的margin都好低，为了点塔只能适度交一些margin789之类的了，希望后面能够多产出一些margin高的，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.5500 6.1400 0.0027

GLB MINVOL1M 2.3000 1.3600 0.0008

GLB MINVOL1M 2.0300 1.1500 0.0008

GLB MINVOL1M 1.3800 0.9100 0.0046

今日base指标：

sa:54.67dao,交的是asi的not own 553,还是牺牲了一些表现，更新os之后23年的质量实在是太差了

ra:3.47dao，交了两个ra和一个ppa

=================================越努力，越幸运================================

---

### 探讨 #48: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

我的量化日记

日期：2026年1月25日

今天终于是交满了，今天交了4个glb的alpha，有三个glb的ra以及一个glb的ppa,还交了一个eur的own 557，目前已经点了19个塔，这个月的目标是希望能够点到23个，下个月春节没有多少时间去点塔了，这个月多点一点，后面就没有什么时间了，glb还能再点几个，ind也还能点，eur等主题ppa吧，没有的话就放在下个月吧，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.2200 5.6700 0.0028

GLB MINVOL1M 2.8800 1.9100 0.0009

GLB MINVOL1M 2.3000 1.2300 0.0013

GLB MINVOL1M 1.6700 0.8300 0.0012

GLB MINVOL1M 1.6500 1.0800 0.0010

今日base指标：

sa:8.22dao,交的是eur own 557,

ra:4.41dao交的是3个ra和一个主题ppa

=================================越努力，越幸运================================

---

### 探讨 #49: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

我的量化日记

日期：2026年1月26日

今天又是交满了的一天，今天交了5个alpha，包括一个asi的not own 553，以及一个glb的ra和三个Ind的ra，终于又是交满了，这个月快结束了，开了三个地区，必须要快点点完，还要多交一点，ind就这样了，eur不想点了，就好好做一下glb吧，

今日alpha指标：

region universe sharpe fitness margin

ASI MINVOL1M 5.5500 5.1400 0.0017

IND TOP500 2.6400 3.2100 0.0035

GLB MINVOL1M 2.0700 1.2500 0.0010

IND TOP500 2.0100 1.7300 0.0017

IND TOP500 1.9300 1.7900 0.0039

今日base指标：

sa:52.4dao,今天太少了，越来越少了，交的asi的not own 553

ra:6.8dao，最多的一天，交14个ra

===================================越努力，越幸运=============================

---

### 探讨 #50: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

我的量化日记

日期：2026年1月27日

今天只交了三个alpha,包括eur的own 557,以及两个glb的ra，glb交的alpha的margin都不行啊，但是为了点塔我还是交了吧，做eur不作glb是因为懒，eur的好做，glb的太难做了，随便测一下eur的pc小于0.7的就好了，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.3000 5.1000 0.0021

GLB MINVOL1M 2.1500 1.3800 0.0011

GLB MINVOL1M 1.9300 1.2300 0.0013

今日base指标如下：

sa:8.35dao,交的是eur的own 557,正常水平

ra:2.58dao,这也太少了，而且还是两个glb的ra，给这么少看都不想看

==========================越努力，越幸运=============================

---

### 探讨 #51: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

我的量化日记

日期：2026年1月28日

今天我交了4个alpha，其中包括asi的not own 553，以及三个glb的ra,现在还在疯狂的点glb的塔，不想交ppa只好全部去做ra了，不做ppa主要是因为那些数据集太ex了，出来的质量太差了而且出货率太感人了，与其花费这个精力还不如直接去做ra来的舒坦一点，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.7700 6.0000 0.0022

GLB MINVOL1M 2.2500 1.3000 0.0007

GLB MINVOL1M 1.8900 1.3200 0.0012

GLB MINVOL1M 1.4500 1.1300 0.0012

今日base指标如下：

sa:53.12dao,比上次稍微多了一点点而已，交的是asi的not own 553，趁着vf还不算低赶紧的去交一点，先甜后苦

ra:4.42dao，三个，这么多，还算可以的了

================================越努力，越幸运==========================

---

### 探讨 #52: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

我的量化日记

日期：2026年1月29日

今天我只交了两个alpha,因为确实不想多做了，这个pc获取的太慢了，根本就没心情去等，就交了一个eur的own sa557和一个glb的ra来摆一摆吧，想等哪天prod获取不那么久了再开始多交一点，要快快修复啊，太难熬了，这个限流太让人头大了，什么也干不了，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.9600 5.9000 0.0020

GLB MINVOL1M 2.8100 1.4000 0.0005

今日base指标如下：

sa:8.27dao,交的是eur的own sa557,已经过了很久很久没有交555了，我现在交own的话就每天回测一轮25个随便交一个比较好的就好了

ra:2.57dao，还不错，平时交一个只有1.9dao的样子

===============================越努力，越幸运===============================

---

### 探讨 #53: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

我的量化日记

日期：2026年1月30日

今天我交了4个alpha,都是在早上1点，12点开始提交的，晚上忘记交了，主要是不想去等获取pc，今天早上起来开始搓alpha，搓出来了三个glb的ra，于是开始提交，一直没有交上去，本来打算交满的，因为这个月快结束了，glb的点塔任务还空余了一点，想抓紧点的，结果根本就交不上去，交的是3个glb的ra，和一个asi的not own 553,

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 6.4300 6.9500 0.0023

GLB MINVOL1M 2.9500 2.0900 0.0010

GLB MINVOL1M 2.3600 1.4100 0.0007

GLB MINVOL1M 1.8700 1.0500 0.0006

今日base指标：

sa:53.4dao，基本上交的是asi的not own 553，也就是这个水平吧

ra:5.39dao，交了三个，这么多还不错哦

==================================越努力，越幸运=========================

---

### 探讨 #54: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月8日

在连续了7天交满alpha的情况下今天断了，只交了2个ppa和一个own sa，指标如下：

USA  Statistical  4.85  11.48%  15.83%  14.51‱  4.13

EUR  Subindustry  1.44  7.00%  10.01%   13.98‱  1.08

USA  Statistical  1.49  3.42%  6.85%  9.97‱  0.78

============================坚持！=========================

---

### 探讨 #55: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月9日

今天交了2个ppa和一个sa，指标如下：

EUR  Subindustry  5.43  18.02%  9.17%  39.29‱  6.52

EUR  Subindustry  1.65  3.41%  5.30%  12.87‱  0.86

USA  Crowding Factors  1.30  13.34%  17.25%  15.47‱  1.14

这段时间在编写自己的工作流，正好把数据库建立起来，没有多少时间调试alpha，导致alpha提交数量太少了

=======================================坚持！====================================

---

### 探讨 #56: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月10日

连续三天只交了2个ppa和sa了，ra越来越难出了目前主要集中火力做usa和eur的d1，有空也会做asi的d1，打算的是10月把usa eur asi的d1的塔点了，顺带做点glb

今日指标如下：

2.05  5.34%  8.49%  12.58‱  1.34

EUR  Fast Factors  7.10  15.27%  11.96%  25.54‱  7.85

USA Subindustry  1.51  4.52%  3.43%  26.31‱  0 .91

======================================坚持！===============================

---

### 探讨 #57: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月11日

今天终于是交满了，只可惜全是ppa，好久都没有出ra了，数据库也是建好了，方便了许多，工作流也是建好了，但是还不够稳定，后面还是要慢慢完善以下，今日alpha指标如下：

USA  Subindustry  1.24  4.53%  8.91%  10.17‱  0.75

USA  RAM  1.43  8.38%  8.36%  20.04‱  1.17

USA  Subindustry  1.35  4.92%  3.86%  25.49‱  0.85

USA  Subindustry  2.27  5.25%  3.24%  32.43‱  1.47

EUR  Statistical  5.69  11.62%  13.67%  16.99‱  5.25

======================================坚持！====================================

---

### 探讨 #58: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月12日

今天做的是usa的instituions，还是比较难做，还是做出来了3个atom，还有一个本该是option的ra的，结果交的时候不小心把描述写了交成ppa了，这个月一个not own都还没有交，才拿到not own权限还在研究，后面慢慢交一点not own的了，今日指标如下：

USA  RAM  1.93  3.60%  4.17%  17.26‱  1.04

EUR  Statistical  6.97  13.01%  13.18%  19.74‱  6.92

USA  Subindustry  1.74  3.39%  2.99%  22.68‱  0.91

USA  Statistical  1.78  8.82%  8.08%  21.83‱  1.50

USA  Industry  1.29  4.09%  2.39%  34.13‱  0.74

=================================坚持！======================================

---

### 探讨 #59: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月13日

今天在服务器特别卡的情况下还是交满了，交了四个ppa和一个ra，其中交了3个eur的imbalance数据集的alpha成功点亮imbalance的塔，虽然imbalance的数据集很少，但质量也是非常不错的，但是我也有点忧虑，ppa的sharpe能达到4＋，这种alpha真的没有问题吗？

==============================坚持！=======================================

---

### 探讨 #60: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月15日

今天交了2个ppa，一个ra，一个own sa，2个eur的fundamental数据集，和一个usa的analyst数据集的，指标如下:

EUR Market  1.98  6.61%  2.24%  59.12‱  1.44

EUR Subindustry  1.47   3.91%  4.15%  18.84‱  0.82

EUR Statistical  6.24  10.38%  14.99%  13.85‱  5.19

USA Subindustry  1.87  5.55%  8.25%  13.45‱  1.25

====================坚持！==================================

---

### 探讨 #61: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月14日

今天成功交满，交的是4个ppa和own的sa，4个ppa全是asi地区的，提交速度也是非常快，其中有2个imbalance数据集的，一个fundamental数据集的，还有一个broker数据集的，缺点就是turnover有点低了，margin也低了，指标如下：

ASI  Statistical  2.61  3.80%  7.51%  10.10‱  1.44

ASI  Statistical  1.65  2.79%  5.46%  10.24‱  0.78

ASI  Fast Factors  1.56  4.17%  9.78   %8.52‱   0.90

ASI  Industry  1.49  3.72%  9.25%   8.05‱   0.81

================================坚持！===================================

---

### 探讨 #62: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月16日

今天交了2个ppa和1个sa，今天是有not own以来第一次组出来了三五，但是还没打算交，想等vf更新了再交试试，现在vf0.41，很大一部分的影响是iqc期间，第一次更新vf是0.25，现在每天basepayment在3美元以上，但也是真不多啊，还是期待vf快点更新

===============================坚持！===================================

---

### 探讨 #63: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月17日

今天交了4个alpha,其中一个sa，一个ra,两个ppa，还是没交满，产率真的有点低了，也不想交存货，第一存货大多数是analyst,fundamental,model这种大数据集的，之前已经交了很多了，第二就是pc还是有点偏高，平台终于不卡顿了，可以从ASI转战到USA和EUR地区了，今天交的ra指标：

USA  Crowding Factors  1.76   4.01%  7.55%  10.62‱  1.00

====================================坚持！====================================

---

### 探讨 #64: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月18日

今天交了4个ppa和一个superalpha，最近开始点小数据的塔了，alpha是真的难出啊，就算出了也是高turnover低fitness低margin的，都引发提交焦虑了，又相交又不想交，但是我还是觉得diversity是比较重要的，还是交了，指标如下：

USAStatistical1.76  3.20%  15.29%  4.18‱  0.81

USAStatistical1.46  3.47%  7.48%   9.29‱  0.77

USASubindustry1.93  4.97%  9.53%  10.43‱  1.22

EURFast Factors1.45  2.29%   5.77%  7.91‱  0.62

================================坚持！=================================

---

### 探讨 #65: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月19日

今天是做小数据集的第二天，虽说小数据集难做，但是出的货也不少，就是质量实在是不好，今天仍然是交满了，并且一次性提交了两个ra,可以说还是有进步的，指标如下：

USA   Statistical  1.67  10.48%  11.82%  17.73‱   1.53

USA   Subindustry  1.72  5.02%  4.54%  22.14‱   1.09

ASI   Statistical   1.21  3.40%  6.54%   10.41‱   0.63

ASI   Slow + Fast Factors   1.38   2.78%  5.85%  9.49‱  0.65

================================坚持！============================

---

### 探讨 #66: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月20日

今天是做小数据集的第3天，今天仍然是交满了，交了4个ppa，很遗憾没有做出ra，质量总体来说算不错的了，就是returns和fitness偏低了，我最近的回测框架也差不多优化结束了，效率还是杠杠的，有空可以分享出来，指标如下：

USA  Statistical  1.55  2.40%  4.41%1  0.88‱  0.68

USA  Subindustry  1.17   4.31%  7.03%  12.25‱  0.69

USA  Subindustry   1.58  4.75%  4.55%  20.87‱  0.97

USA  Market   1.79   5.71%   20.67%   5.53‱   0.94

============================坚持！===============================

---

### 探讨 #67: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月21日

今天是做小数据集的第4天，今天交了3个ppa,质量大不如以前了，因为剩下的这些数据集太难出货了，至此，USA的小数据集完成了80%了，现在开始了对EUR的进攻，并且我找到了一个新的思路，待我尝试尝试看看效果怎么样，今日指标如下，margin普遍拉跨，后面要多交高margin来和这些alpha中和一下：

EUR  Subindustry  1.82  7.54%  20.47%  7.36‱  1.10

USA  RAM  3.61  9.88%  32.02%  6.17‱  2.01

USA  Statistical   1.25  2.98%  9.88%  6.03‱  0.61

===========================坚持！===================================

---

### 探讨 #68: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月22日

今日交了三个alpha,其中2个ppa,一个sa，依旧在做小数据集，做出来了一个social的，产量明显跟不上了，最近很吃力啊，指标如下：

USA  Sector  1.91   6.17%   9.27%   13.30‱   1.34

USA  Slow + Fast Factors   5.46   13.29%   11.72%   22.69‱   5.63

EUR  Subindustry   1.24  9.20%   18.89%   9.74‱   0.87

===============================坚持！==================================

---

### 探讨 #69: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月23日

今天交了四个alpha，其中3个ppa，一个sa，做的是eur的analyst和model，做小数据集实在做不下去了，做一做大数据集缓缓气。今天也是更新vf了！vf从0.5-0.25-0.41-0.91,终于出狱了，还是听weijie老师的多交atom管用，严格控制质量。

今日base记录：

ra:5.18   2个主题加一个非主题，fitness:1.39 1.82  1.93

sa:9.13  双5

下一日交一个三五试试水，ra base应该是被fitness抬高的

===============================坚持！========================

---

### 探讨 #70: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月24日

今天交了5个alpha，其中3个ppa，一个ra，一个sa，今天base还算客观，今天是小数据集混合大数据集一起提交，本来想全部交主题的，但是突然忘了。

今日base记录：

ra:7.15     2个主题加2个非主题，平均fitness:1.1,感觉是今天的pc要低一点给的多一点

sa:14.37  做的是eur not own 三五，fitness只有5，感觉比预期的要低

=============================坚持！======================================

---

### 探讨 #71: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月25日

今天也是交了5个alpha，4个ppa和1个sa，感觉更新了vf动力都增加了许多，愿意花更多时间在wq上了，今天交的也是大数据集和小数据集混合，只想快速结束usa和eur的小数据集，点着太痛苦了。

今日base记录：

ra:4.33     4个非主题，平均fitness有1.4，不知道为啥这么少啊

sa:20.16  eur own 三五,而且是665，比555要多5刀左右，下一天再交fitness高一点的三五试试水

============================坚持！=======================================

---

### 探讨 #72: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

我的量化日记

日期：2025年10月26日

今天交了3个ppa和一个own的eur 三五，其中三个ppa点了一个eur的other的塔，指标都还好，pc稍微有点高。

今日bsae指标:

sa:11.55刀   775 eur own

ra:8.43  平均fitness 2.1

今天sa的fitness高了竟然还那么低，而ra的base是目前最高的，可见fitness对base的影响还是有的

=================================坚持！=================================

---

### 探讨 #73: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

我的量化日记

日期：2025年10月27日

今天交了3个alpha，两个ra和一个sa,两个ra都是eur的model的，存货比较少了，不得不交一点model的，快到月末了，也快结束小数据集的点塔任务了。

今日base指标：

sa: 11.52刀 交的是eur own 565,比昨天交的差了一点居然拿到的钱差不多，基本一样

ra:4.15 平均fitness 1.5 pc也不高啊，而且两个都是ra，拿那么少也很惊讶

===========================坚持！========================================

---

### 探讨 #74: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

我的量化日记

日期：2025年10月28日

今天交了5个alpha，有3个ppa，一个ra，一个sa，其中有两个eur 的institutions的ppa和一个usa analyst的ppa，sa交的是eur own 三五，ra 是usa的earnings的二阶，这个二阶是我自己构造的二阶模版跑出来的，最近产量慢慢跟上来了。

今日base指标：

sa:9.74刀  665三五都这么不值钱了吗，出奇的低，这和我第一天交997有什么区别啊，

ra:6.05刀  中规中距吧，没有做主题，这个base也差不多是我的平均水平了

下一步目标是做ASI了，但是我跑起来vector的一直报错，小数据集大多数都是vector，有点难受

=============================坚持！================================

---

### 探讨 #75: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

我的量化日记

日期：2025年10月29日

今天交了6个alpha，多交了一个ra啊，太心疼了，今天交的很杂，包括insiders institutions short earnings analyst的都交了，主要是下个月开始ppa只能用风险中性化了，吓得我只好把数据库里面存的alpha拿出来交了，本来打算这些小地区留着下一个赛季点塔用的，我看着换风险中性化之后指标下降的比较多，就干脆这个赛季一并点掉，下一个赛季再想想办法吧，交着交着就忘记自己交了多少个了。

今日base指标：

sa：18.91刀,前几天三五的base一直在下降，今天也是扬眉吐气了一次了，今天搓出来了一个glb的765，还是glb的sa赚钱啊

ra:5.92刀 平均水平，知足了

=====================================坚持！===============================

---

### 探讨 #76: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记

日期：2026年03月01日

今天交了1个因子，交了1个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.8300 5.3900 0.0031

今日base指标如下:

sa:1.49dao

ra:1.61dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #77: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记

日期：2026年03月02日

今天交了2个因子，交了2个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.8300 4.8000 0.0027

GLB MINVOL1M 2.7400 2.0500 0.0015

今日base指标如下:

sa:1.78dao

ra:1.5dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #78: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记

日期：2026年03月03日

今天交了5个因子，交了5个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.9000 4.6100 0.0026

GLB MINVOL1M 1.9300 1.4100 0.0020

GLB MINVOL1M 1.7200 1.7000 0.0021

GLB MINVOL1M 1.3100 0.9300 0.0023

GLB MINVOL1M 1.1800 1.0500 0.0017

今日base指标如下:

sa:1.76dao

ra:1.65dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #79: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记

日期：2026年03月04日

今天交了3个因子，交了3个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.5600 4.1200 0.0023

GLB MINVOL1M 2.5000 1.6400 0.0014

GLB MINVOL1M 1.5500 1.0500 0.0011

今日base指标如下:

sa:1.54dao

ra:1.72dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #80: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记

日期：2026年03月05日

今天交了3个因子，交了3个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 5.8300 4.5100 0.0016

GLB MINVOL1M 1.3100 1.2300 0.0031

GLB MINVOL1M 1.2500 0.7300 0.0019

今日base指标如下:

sa:1.67dao

ra:1.47dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #81: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月15日

今天交了5个因子，交了2个glb的alpha，和3个EUR的alpha,指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 6.2900 5.1500 0.0017

EUR TOP2500 2.8900 2.0600 0.0010

EUR TOP2500 2.4300 1.6700 0.0009

EUR TOP2500 1.6600 1.1900 0.0010

GLB TOPDIV3000 1.6000 0.9300 0.0009

今日base指标如下:

sa:1.63dao

ra:1.64dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #82: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月16日

今天交了5个因子，交了1个glb的alpha，4个hkg的alpha指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 5.2000 4.1800 0.0017

HKG TOP800 2.0000 2.2600 0.0042

HKG TOP800 1.9400 1.7700 0.0033

HKG TOP800 1.6600 1.6100 0.0022

HKG TOP800 1.6600 1.5800 0.0080

今日base指标如下:

sa:1.65dao

ra:1.51dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #83: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月17日

今天交了5个因子，交了1个glb的alpha，以及4个hkg的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 5.4200 4.0500 0.0016

HKG TOP800 2.2100 2.3700 0.0025

HKG TOP800 1.5800 1.5200 0.0128

HKG TOP800 1.4400 1.1400 0.0059

HKG TOP800 1.4200 1.1300 0.0015

今日base指标如下:

sa:1.68dao

ra:1.6dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #84: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月18日

今天交了5个因子，交了1个eur的alpha，4个hkg的alpha,指标如下：

region universe sharpe fitness margin

EUR TOP2500 6.0600 5.9200 0.0019

HKG TOP800 1.9800 2.5900 0.0086

HKG TOP800 1.9400 1.6800 0.0037

HKG TOP800 1.8500 1.8700 0.0079

HKG TOP800 1.5300 1.4200 0.0042

今日base指标如下:

sa:1.69dao

ra:1.54dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #85: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月19日

今天交了5个因子，交了1个eur的alpha，4个hkg的alpha，指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.0000 5.3000 0.0042

HKG TOP800 1.9700 2.1700 0.0024

HKG TOP800 1.6900 1.4000 0.0014

HKG TOP800 1.6100 1.4200 0.0058

HKG TOP800 1.4000 1.5200 0.0041

今日base指标如下:

sa:1.54dao

ra:1.47dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #86: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月20日

今天交了5个因子，交了1个eur的alpha，4个hkg的alpha，指标如下：

region universe sharpe fitness margin

EUR TOP2500 6.7400 6.2600 0.0017

HKG TOP800 2.0500 2.4700 0.0041

HKG TOP800 2.0500 2.0000 0.0039

HKG TOP800 1.3300 1.0100 0.0023

HKG TOP800 1.2100 0.8300 0.0021

今日base指标如下:

sa:1.51dao

ra:1.64dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #87: 关于《2026/03/06》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记（回忆版）

日期：2026年02月21日

今天交了5个因子，交了5个hkg的alpha，指标如下：

region universe sharpe fitness margin

HKG TOP800 4.0300 5.6400 0.0068

HKG TOP800 1.9800 1.9900 0.0020

HKG TOP800 1.9500 2.3100 0.0031

HKG TOP800 1.7700 1.5100 0.0020

HKG TOP800 1.6200 1.3200 0.0022

今日base指标如下:

sa:1.67dao

ra:1.45dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================

---

### 探讨 #88: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

25/9/18

今天只交了一个USA的ppa，指标如下：

1.72   sharpe

4.69%  returns

3.87%  turnover

24.24‱    margin

1.05    fitness

turnover偏低了，生产相关性还是很高，自己开发的模板中有生产相关性低的alpha但操作符很多，而且产出率比较低，经常断交，并且为了保持住6维，很难做取舍，后面要多学习多做低相关性低操作符的alpha

---

### 探讨 #89: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

25/9/19

今天交了一个USA的ppa,指标如下：

1.78 sharpe

3.63% returns

17.37% turnover

4.17‱ margin

0.81 fitness

除了sharpe各指标都不好，因为想着看能不能冲下榜，还是没忍住交了，通过调ts_target_tvr_decay在提高margin的同时会损失大部分的sharpe，同时要想想办法去提高alpha的产率了，或许不应该着急，沉下心来用心去研究alpha

---

### 探讨 #90: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

2025年9月21日

今天也只交了一个ppa

USA

1.40    sharpe

5.03%   returns

10.77%  turnover

9.34‱    margin

0.89    fitness

断粮有点难受，外加vf0.41，即使比上次0.25的高，但base没有什么变化，但也不能只在意base，还是要只交好的，不能交差的，等把iqc期间交的差的因子都滚动掉我的vf会迎来晴天的。

---

### 探讨 #91: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

日期：2025年9月22日

今天是连续回测的第82天，因为iqc结束断了一周，导致我的连续回测天数很拉跨，在genius上面的竞争很难受，但好在接近3个月的坚持与努力，排名也是维持在了master的要求附近（不包括grandmaster 的情况下）

今天交了一个ppa：

USA

1.55     sharpe

4.87%   returns

4.64%   turnover

20.98‱    margin

0.97   fitness

质量不算好，但还过的去，另外最近在尝试新的模板，我发现这个模板出的货普遍生产相关性比较低，质量也说的过去，这给了我一定的自信心

---

### 探讨 #92: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

日期：2025年9月23日

连续十天每天只交一个alphal了，不知道这样的日子能维持到什么时候，交的少会影响vf，看来后面几天我要多交一点了，把前面囤的没有交的再拿来测一测相关性

今日alpha：

Sharpe：

1.44

Turnover：

17.63%

Fitness：

1.08

Returns：

10.00%

Drawdown:

10.05%

Margin:

11.34‱

仍然是个ppa，希望明天我能多交一点，每天都在进步！

---

### 探讨 #93: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月24日

今天是连续回测的84天，目前在回测usa地区的risk数据集，发现我所使用的模板回测出来的alpha其大多数sharpe是负的，并且正的sharpe竟然没有大于1的，而负的sharpe可以达到-1.91，我果断将所有的负sharpe的alpha全部反转，得到了许多比较优质的alpha，并且prod相关性还是比较低的

---

### 探讨 #94: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月25日

今天是我连续回测的第85天

最近遇到了瓶颈，很难找到prod比较低的alpha，也不愿意交比较高的prod的alpha了，而且经过一个早上和一个晚上，我的genius排名又降了6名，而目前而言前310才有希望进master，而我现在276，每天都这么降的话进master还是有点悬，还得继续努力啊

---

### 探讨 #95: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月26日

今天是我坚持连续回测的85天，再撑几天这个赛季就结束了，希望排名和combine能保住master，一直看着排名唰唰下降心里还是很难受，现在在master的universe内排282，还是特别危险，而且还要谨防有些人最后来偷塔

====================================================================

---

### 探讨 #96: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

25/9/18

今天只交了一个USA的ppa，指标如下：

1.72   sharpe

4.69%  returns

3.87%  turnover

24.24‱    margin

1.05    fitness

turnover偏低了，生产相关性还是很高，自己开发的模板中有生产相关性低的alpha但操作符很多，而且产出率比较低，经常断交，并且为了保持住6维，很难做取舍，后面要多学习多做低相关性低操作符的alpha

---

### 探讨 #97: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

25/9/19

今天交了一个USA的ppa,指标如下：

1.78 sharpe

3.63% returns

17.37% turnover

4.17‱ margin

0.81 fitness

除了sharpe各指标都不好，因为想着看能不能冲下榜，还是没忍住交了，通过调ts_target_tvr_decay在提高margin的同时会损失大部分的sharpe，同时要想想办法去提高alpha的产率了，或许不应该着急，沉下心来用心去研究alpha

---

### 探讨 #98: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月21日

今天也只交了一个ppa

USA

1.40    sharpe

5.03%   returns

10.77%  turnover

9.34‱    margin

0.89    fitness

断粮有点难受，外加vf0.41，即使比上次0.25的高，但base没有什么变化，但也不能只在意base，还是要只交好的，不能交差的，等把iqc期间交的差的因子都滚动掉我的vf会迎来晴天的。

---

### 探讨 #99: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

日期：2025年9月22日

今天是连续回测的第82天，因为iqc结束断了一周，导致我的连续回测天数很拉跨，在genius上面的竞争很难受，但好在接近3个月的坚持与努力，排名也是维持在了master的要求附近（不包括grandmaster 的情况下）

今天交了一个ppa：

USA

1.55     sharpe

4.87%   returns

4.64%   turnover

20.98‱    margin

0.97   fitness

质量不算好，但还过的去，另外最近在尝试新的模板，我发现这个模板出的货普遍生产相关性比较低，质量也说的过去，这给了我一定的自信心

---

### 探讨 #100: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

日期：2025年9月23日

连续十天每天只交一个alphal了，不知道这样的日子能维持到什么时候，交的少会影响vf，看来后面几天我要多交一点了，把前面囤的没有交的再拿来测一测相关性

今日alpha：

Sharpe：

1.44

Turnover：

17.63%

Fitness：

1.08

Returns：

10.00%

Drawdown:

10.05%

Margin:

11.34‱

仍然是个ppa，希望明天我能多交一点，每天都在进步！

---

### 探讨 #101: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月24日

今天是连续回测的84天，目前在回测usa地区的risk数据集，发现我所使用的模板回测出来的alpha其大多数sharpe是负的，并且正的sharpe竟然没有大于1的，而负的sharpe可以达到-1.91，我果断将所有的负sharpe的alpha全部反转，得到了许多比较优质的alpha，并且prod相关性还是比较低的

---

### 探讨 #102: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月25日

今天是我连续回测的第85天

最近遇到了瓶颈，很难找到prod比较低的alpha，也不愿意交比较高的prod的alpha了，而且经过一个早上和一个晚上，我的genius排名又降了6名，而目前而言前310才有希望进master，而我现在276，每天都这么降的话进master还是有点悬，还得继续努力啊

---

### 探讨 #103: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月26日

今天是我坚持连续回测的85天，再撑几天这个赛季就结束了，希望排名和combine能保住master，一直看着排名唰唰下降心里还是很难受，现在在master的universe内排282，还是特别危险，而且还要谨防有些人最后来偷塔

====================================================================

---

### 探讨 #104: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月27日

今天是我连续回测的第86天了，目前genuis排在第296，在master的边缘徘徊，最后这几天不得不冲刺了，不然迟早会掉出master的，翻翻库存，多交一点alpha，能加几名算几名，大家也要一起努力啊！

=============================坚持！！！===============================================

---

### 探讨 #105: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

我的量化日记

日期：2025年9月28日

今天是我坚持连续回测的第87天了，我想了一下，最后三天或者两天的时间内想要冲刺genuis的唯一方法就是多交低op的alpha来降低avg op了，这个赛季交的alpha还是有点少了，毕竟刚结束iqc初来乍到走了很多坑，能到达这个排名心里已经算很满足了，现在坚持每天交满四个alpha，最后是否能到master就看运气了

---

### 探讨 #106: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月1日

今天交了四个alpha，其中两个ra和两个ppa，其sahrpe,returns,turnover,margin,fitness如下：

USA

1.68

4.89%

6.93%

14.11‱

1.05

USA

2.48

114.24%

7.21%

316.86‱

7.50

USA

1.79

6.85%

14.54%

9.43‱

1.23

USA

1.67

7.45%

3.60%

41.41‱

1.29

====================10月平均prod:0.73,今日平均prod:0.73，较上一日进步：0========================

---

### 探讨 #107: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月2日

今天交了四个alpha，全是ppa，其sahrpe,returns,turnover,margin,fitness如下：

EUR

1.83

3.62%

4.53%

15.98‱

0.98

USA

1.75

8.45%

8.20%

20.63‱

1.44

1.93

5.74%

11.38%

10.08‱

1.31

ASI

2.09

3.93%

9.12%

8.63‱

1.17

======10月平均prod:0.7385,今日平均prod:0.7475，较上一日进步：-0.009==============

---

### 探讨 #108: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月3日

今天交了四个alpha，3个ppa一个ra，其sahrpe,returns,turnover,margin,fitness如下：

EUR：2.44  4.46%  10.86%  8.21‱  1.46

1.36  6.13%  10.74%  11.40‱  0.95

1.59  2.96%  6.03%  9.83‱  0.77

USA：1.24  27.53%  24.80%  22.20‱  1.31

======10月平均prod:0.7131,今日平均prod:0.6625，较上一日进步：0.085==============

---

### 探讨 #109: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月4日

今天交了四个alpha，2个ppa2个ra，其sahrpe,returns,turnover,margin,fitness如下：

EUR:1.37  3.68%  3.23%  22.77‱  0.74

1.65  4.60%  10.38%  8.86‱  1.00

1.50  2.81%  4.22%  13.31‱  0.71

ASI:  2.02  4.06%  9.09%  8.93‱  1.15

=========10月平均prod:0.6960,今日平均prod:0.645，较上一日进步：0.0175==============

---

### 探讨 #110: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月5日

今天交了四个alpha，全是ppa，其sahrpe,returns,turnover,margin,fitness如下：

1.36  12.30%  3.99%  61.62‱   1.35

1.44  2.88%  5.07%  11.34‱  0.69

1.46  3.02%  6.56%  9.21‱  0.72

2.26  5.45%  27.68%  3.94‱  1.00

=========10月平均prod:0.6693,今日平均prod:0.5625，较上一日进步：0.0825==============

---

### 探讨 #111: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月6日

今天交了四个alpha，其中有3个ppa，1个ra,其sharpe,returns,turnover,margin,fitness的指标如下：

1.58  8.09%  6.50%  24.90‱  1.27

1.36  30.17%  5.86%  102.93‱  2.11

1.21  20.97%  4.56%  91.99‱  1.57

1.48  6.13%  16.79%  7.30‱  0.89

===============10月平均prod:6636  ，今日平均prod:0.635,较上一日进步：-0.425===============

---

### 探讨 #112: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

我的量化日记

日期：2025年10月7日

今天交了三个alpha，其中有1个ppa，2个ra,其sharpe,returns,turnover,margin,fitness的指标如下：

1.95  3.50%   10.35%   6.76‱   1.03

1.63   5.65%   10.30%   10.97‱   1.10

1.68  5.65%   9.70%   11.66‱   1.13

===============10月平均prod:6639  ，今日平均prod:0.6666,较上一日进步：-0.031===============

---

### 探讨 #113: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: [Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享.md
- **评论时间**: 9个月前

感谢大佬的分享，我认真地看完了，文章的风格独特且美观，我也收获了很多，对于alpha的研究豁然开朗，有了不一样的见解，并且，此前一直没有想过用a=表达式1；表达式2（a)；这样也可以降操作符，突然感觉自己损失了很多；再者，对于在表达式中再加一个字段有时可以改良alpha的性能，以及我们可以自创数据字段，这些为我后面的研究带来了启迪性的作用

---

### 探讨 #114: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **评论时间**: 9个月前

感谢大佬的分享，我认真地看完了，文章的风格独特且美观，我也收获了很多，对于alpha的研究豁然开朗，有了不一样的见解，并且，此前一直没有想过用a=表达式1；表达式2（a)；这样也可以降操作符，突然感觉自己损失了很多；再者，对于在表达式中再加一个字段有时可以改良alpha的性能，以及我们可以自创数据字段，这些为我后面的研究带来了启迪性的作用

---

### 探讨 #115: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 如何利用tvr操作符与alpha起舞论坛精选.md
- **评论时间**: 9个月前

感谢大佬的分享，要不是大佬分享我还不会注意到有这个操作符，以前都专注于交低turnover的alpha，以至于交了很多3%甚至2%的alpha，自从听了weijie老师的讲解，才开始反思其为什么turnover会这么低，于是我会对每个低turnover并且margin足够高的alpha根据大佬的讲解套ts_target_tvr_decay以提高turnover并尽可能使margin保持在合理范围内

---

### 探讨 #116: 关于《如何利用tvr操作符与alpha起舞论坛精选》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何利用tvr操作符与alpha起舞论坛精选_34562640928023.md
- **评论时间**: 9个月前

感谢大佬的分享，要不是大佬分享我还不会注意到有这个操作符，以前都专注于交低turnover的alpha，以至于交了很多3%甚至2%的alpha，自从听了weijie老师的讲解，才开始反思其为什么turnover会这么低，于是我会对每个低turnover并且margin足够高的alpha根据大佬的讲解套ts_target_tvr_decay以提高turnover并尽可能使margin保持在合理范围内

---

### 探讨 #117: 关于《连续三个季度蝉联Master，我的佛系Genius之旅经验分享》的评论回复
- **帖子链接**: [Commented] 连续三个季度蝉联Master我的佛系Genius之旅经验分享.md
- **评论时间**: 10个月前

感谢大佬的经验分享，我现在开始注重六维开始压per了，不过现在达到master要点30个塔，有必要为了点塔交那种比较差的alpha吗，就比如数据缺失或者turnover高amrgin低的这种影响vluefactor，交了这种alpha总觉得污染了我的池子，但是不交又觉得难以点到30个塔

---

### 探讨 #118: 关于《连续三个季度蝉联Master，我的佛系Genius之旅经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 连续三个季度蝉联Master我的佛系Genius之旅经验分享_33628502441751.md
- **评论时间**: 11个月前

感谢大佬的经验分享，我现在开始注重六维开始压per了，不过现在达到master要点30个塔，有必要为了点塔交那种比较差的alpha吗，就比如数据缺失或者turnover高amrgin低的这种影响vluefactor，交了这种alpha总觉得污染了我的池子，但是不交又觉得难以点到30个塔

---
