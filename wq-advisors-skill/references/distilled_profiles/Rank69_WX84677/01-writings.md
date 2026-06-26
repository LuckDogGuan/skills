# 顾问 WX84677 (Rank 69) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 WX84677 (Rank 69) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: How to Improve After Cost Performance置顶的
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

### 帖子 #2: Lab中处理Vector数据的一种方法代码优化
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

### 帖子 #3: Lab中处理Vector数据的一种方法代码优化
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

### 帖子 #4: Machine Alpha 基础知识1：什么是Alpha模板
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

### 帖子 #5: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #6: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
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

### 帖子 #7: Maximizing Combined Alpha Performance: Key Strategies and Insights
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

### 帖子 #8: replace 操作符的理解与运用
- **主帖链接**: [L2] replace 操作符的理解与运用.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #9: replace 操作符的理解与运用
- **主帖链接**: https://support.worldquantbrain.com[L2] replace 操作符的理解与运用_35191104743447.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #10: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location']
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

### 帖子 #11: Vscode自动提示operator代码优化
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

### 帖子 #12: [MCP]找灵感功能上手详解经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]找灵感功能上手详解经验分享_37113649831831.md
- **讨论数**: 20

最近mcp又出新功能了，马上尝试了一下。如下图选好你想要研究的地区和数据集就可以开始了，配置好key点击生成模板就能一键生成好用的模板
 
> [!NOTE] [图片 OCR 识别内容]
> NSA
> 细问比轱
> IOTTIII
> TOHIIILI
> 顾+5
> Alpha Inspiration Master (找灵感)
> model138
> ACcountlng-based
> MoCel
> LLM Settings
> Results
> 生成 Alpha 模板
> Factors
> 8a52 URL
> Sensitivity to the
> hps Ilapi moonshotcn1
> model140
> Model
> 正在生成模板这可能需要几分钟。
> Inflation Change
> Model
> Name
> Stock Selection DL
> model144
> Model
> kimi-kz-turbo-preview
> model
> APIKey
> model16
> Fundamental Scores
> Model
> 测试连接
> Return prediction
> model1 62
> Model
> from conference call
> ML/AI-Estimates for
> Simulation Settings
> model163
> Analysts' Factor
> Model
> Region
> Model
> USA
> Time-series
> model165
> prediction ofalpha
> Model
> Universe
> models
> TOP3000
> Research Analyst
> model17
> Model
> Delay
> Estimate Factors
> Fundamental &
> modelzo
> Model
> Technical Rank Model
> 开始新任务
> Alpha expression cannot be assigned to
> Template configured as operator with 20 variables
> Variable
> No classes, objects
> pointers
> OTfunctions
> 使用说明
> allowed
 生成之后我们直接下载到本地
 
> [!NOTE] [图片 OCR 识别内容]
> Resuits
> 生成 Alpha 模板
> 下载椟板到本地 d
> 以下给出 6 组可直接在平台"填空"的 a-Template。
> 每个模板均保留"插槽"一一用 <>括起
> -方便日后系统扫描。替换或贝叶斯调参。
> 所有模板已用现有 operator 拼装。可直接粘贴到研究环境缩译。
> 模板1:
> ML 模型残差动量 (分析师来源)
> 经济逻辑:  剥离行业共性后。取模型打分短期娈化。赌"模型新信息"尚末被价格充分反映。
> alpha
> [S_ZSCOre(
> group_neutralizel
> deltal
> backfill(<mdl165_analyst_layerl_or_layerz>;
> 63)
> industry
> 20
 
然后就可以结合mcp去使用了我的用法是直接让ai帮我去找合适的字段去填充模板 
> [!NOTE] [图片 OCR 识别内容]
> TCUC
> TU
> @1md 根据椟板内容的描述去获取合适的数据字段。你觉得合适的字段就放进
> ModellGs 数据字段列表
> 适用于模板AIpha生成
> 来;多一点没关系
> Thought for 2s
> [
> Analyst (分析师)  类特征
> 基于 IBES 数据]
> Read 1md
> Thought for Zs
> Layer 1 特征 (快速信号):
> mdl165_dlgibesnuggetschiwumodell_OIv
> 根据模板内容。需要获取以下几类数据字段:
> mdl165_dlgibesnuggetschiwumodelI_OzV
> modell65 ML/AI特征
> analystlquantlfundamental 三类;
> layer-I/layer-
> mdl165_dlgibesnuggetschiwumodell_IIv
> mdl165_dlgibesnuggetschiwumodelI_ZIV
> 2。基本面宇段
> leverage; market_cap; ROE 等
> mdl165_dlgibesnuggetschiwumodell_3Iv
> 3。成交量宇段
> dollar_Volume; advz0 等
> mdl165_dlgibesnuggetschiwumodell
> 4IV
> 让我先认证BRAIN平台。然后搜索这些字段:
> mdl165_dlgibesnuggetschiwumodelz_SIV
> mdl165_dlgibesnuggetschiwumodell
> GIV
> MCP Tool: worldquant-brain-platfomm
> authenticate
> mdl165_dlgibesnuggetschiwumodell
> 71V
> Thought for Zs
> mdl165_dlgibesnuggetschiwumodell
> BIV
> mdl165_dlgibesnuggetschiwumodell_gIv
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell_zV
> mdl165_
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> dlgibesnuggetschiwumodell
> mdl165_dlgibesnuggetschiwumodell
> MCP Tool: worldquant-brain-platform
> get_datafields
> mdl165_dlgibesnuggetschiwumodelz
> OIV
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodelz_12v
> Thought for 35
> mdl165_dlgibesnuggetschiwumodelz
> mdl165_dlgibesnuggetschiwumodelz_ZIV
> 让我继续搜索更多模板需要的字段:
> mdl165_dlgibesnuggetschiwumodel2_32V
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> ## Layer
> 特征 (愎速信号):
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell_O3v
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 13V
> Thought for 35
> mdl165_dlgibesnuggetschiwumodell_I4v
> mdl165_dlgibesnuggetschiwumodell_Z3V
> 让我再搜索fundamental类的model165字段:
> mdl165_dlgibesnuggetschiwumodell_33V
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 43V
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 44V
> 07]C
> 4105 CITOT +suT7 !
> ThOINht fom
 
然后根据选出来的字段往wqb里面的模板里面去选，选好之后就像下面这样
 
> [!NOTE] [图片 OCR 识别内容]
> 示例
> 双重中性化:以Analyst15为例
> 组间比较_GLB_topdiv
> 组间比较_9lb_topdiv_anl15
> 顾问分析示例
> Expression Editor
> Decode 
> Templates
> Expression Editor 
> Clear
> Configure Template: <modelA_layerl/>
> Detected Templates
> Operator
> 〈modelA_layerIl> (20)
> ZSCore(ts
> delta
> grOUP_
> ZsCOre
> 〈modeln
> Enter
> COIIa
> -separated list Of operators forthe modelA_layerl
> DalaField
> Other
> template:
> mdl165_dlgibesnuggetschiwumodelz_OlV
> 〈dayIl〉 
> mdl16s_dlgibesnuggetschiwumodelz_
> 121
> mdl165_dlgibesnuggetschiwumodelz
> DalaField
> Other
> mdl165_dlgibesnuggetschiwumodel2
> 2IV
> mdl165_dlgibesnuggetschiwumodelz_32 
> 〈day2/〉 
> Choose Operators Trom BRAIN
> DataField
> OtheT
> 11
> Grammar Rules
> 12
> CanCel
> Apply
> 13
> Block comments for multiple lines
> 14
> 15
> Statement separator (not needed for
> last line)
> 17
> Last statement is the Alpha expression for
> 18
> BRAIN simulator 
> Alpha expression cannot be assigned to
> Template configured as operator with 20 variables
> Variable 
> No classes; objects; pointers
> functions
> 使用说明
> allowed
 
然后一键开始回测就好啦

---

### 帖子 #13: 【alpha灵感】A股恐慌度因子在美股的应用
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

### 帖子 #14: 【check王】验证表达式是否正确的脚本——七十二变黄金搭档
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

### 帖子 #15: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md
- **讨论数**: 30

分享下我判断因子是否值得提交的一些经验，希望小伙伴们能有所收获。

一个因子值不值得提交，一个是看因子本身的指标，一个是对组合的增益情况。

对我个人而言，后者的重要性一般会大于因子本身的指标（这是在 **因子指标合格的情况下** 的）；

一般很难找到所有指标对performance都是正面明显的。所以你需要在各个指标之间权衡。

## 根据is performance 的正负面影响判断：

### 可提交的情况

1. fitness 是排首位的，一般fitness有明显增益，margin和sharpe的增益不明显，或者稍微一点负面影响，我会选择提交；
2. 95%的情况下，fitness 对最近3-5年 的performance 有明显的负面影响（比如-0.1），不提交;
3. sharpe 和fitness,margin有增益，但是returns稍微有些负面影响，提交；


> [!NOTE] [图片 OCR 识别内容]
> N
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 7.95
> 0,03
> 6.48 %
> -0.02
> 5.50
> 0.01
> 5.98 %
> -0.02
> 0.48 %
> 0,01
> 18.46 %oo -0.01
> 川
> IS Performance After Submission (Equity, EUR, Delay-1 alphas)
> :
> Combined performance data is shown for all Equity, EUR, Delay-1 alphas. Submitting this alpha will not effect the combined performance ofyour other alphas
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2013
> 9.23
> 0.03
> 7.71 %
> -0.03
> 6.33
> 0.00
> 5.87 %
> -0.05
> 0.19 %
> 0.00
> 15.23 %o。
> -0.07
> 2014
> 10.36
> -0.11
> 6.14 %
> 0.02
> 7.52
> -0.14
> 6.59 %
> -0.10
> 0.17 %
> 0.00
> 21.45 %o。
> -0.28
> 2015
> 7.49
> -0.06
> 6.54 %
> -0.01
> 4.93
> -0.09
> 5.42 %
> -0.10
> 0.26 %
> 0.00
> 16.59 %o。
> -0.24
> 2016
> 6.42
> 0.12
> 6.39 %
> 0.02
> 4.22
> 0.11
> 5.40 %
> 0.08
> 0.42 %
> -0.01
> 16.90 %o。
> 0.29
> 2017
> 7.27
> 0.00
> 6.37 %
> 0.02
> 3.98
> 0.00
> 3.75 %
> 0.00
> 0.14 %
> -0.01
> 11.78 %o。
> 0.05
> 2018
> 7.54
> 0.06
> 6.35 %
> 0.02
> 4.60
> 0.02
> 4.66 %
> -0.03
> 0.44 %
> -0.01
> 14.69 %o。
> -0.06
> 2019
> 8.82
> 0.10
> 6.35 %
> 0.02
> 5.69
> 0.07
> 5.20 %
> 0.00
> 0.21 %
> 0.00
> 16.39 %o。
> 0.07
> 2020
> 7.06
> 0.05
> 6.54 %
> 0.02
> 5.19
> 0.05
> 6.75 %
> 0.04
> 0.48 %
> 0.01
> 20.62 %oo
> 0.14
> 2021
> 9.60
> 0.02
> 6.18 %
> -0.02
> 7.56
> 0.00
> 7.76 %
> -0.03
> 0.15 %
> 0.00
> 25.1
> 9oo
> 0.01
> 2022
> 9.06
> 0.05
> 6.35 %
> -0.01
> 7.62
> 0.03
> 8.84 %
> -0.04
> 0.25 %
> 0.01
> 27.87 %oo
> -0.03
> 2023
> -0.93
> 0.14
> 5.07 %
> 0.00
> -0.27
> 0.07
> 1.08 %
> 0.20
> 0.29 %
> 0.00
> -4.26 %oo
> 0.78
> Pnl


### 什么情况下不会提交：

1、margin不符合地区的最低要求，不提交

3、fitness 最近几年明显负面影响，不提交( 超过1个年份<-0.1)

4、sharpe  最近几年明显负面影响 ，不提交( 超过1个年份 <-0.1)

3、多个指标对组合负面明显过大，即使自相关性低，也不提交

很难一一列举对performance 影响的所有情况，是否提交这个因子，根据组合影响，个人情况判断。

### 从因子本身的指标来看：

1、sharpe>=1 ,fitness>=0.6 的前提下

margin 必须达到各地区margin要求的最低标准，我一般要求比最低标准高万分之五（USA，eur）,glb和ASI 地区的margin有时候比较难找到超过15的，在没有选择的情况下，一般ASI 最低14，15；GLB 14，15（少部分情况下会只要求>10【点塔】）

2、pnl线的波动比较小，向上，sharpe线 **不往下走；**

3、ASI 地区 还会观察下jpn的表现，如果jpn明显表现不佳或者或者kor表现明显大于其他地区的表现，不会提交

以上是我个人的一些经验，可能考虑还欠缺一些其他的点， **如果小伙伴有其他好的 判断方法，期待你评论区的分享**

**如果想要保证combine 的稳定，我个人的经验是 绝对不要提交margin不合格、fitness 负面影响过大、最近3年sharpe 线明显下降，pnl趋于厂 的因子（个人经验）**

**最后，给大家看看我现在的combine 情况，希望国区顾问的combine 都能保持稳定增长。**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.38
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 3.17
> Reached Grandmaster
> 0.5
> Combined Power Pool Alpha Performance
> 2.63


---

### 帖子 #16: PnL = ∑(Robustness * Creativity)
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

### 帖子 #17: PnL = ∑(Robustness * Creativity)
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

### 帖子 #18: PnL = ∑(Robustness * Creativity)
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

### 帖子 #19: 【SuperAlpha灵感】因子择时模型Alpha Template
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

### 帖子 #20: 【YZ工程优化系列】YZ72256-使用API自动完成submit
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

### 帖子 #21: 【工具优化】华子哥插件的FireFox版本经验分享
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

### 帖子 #22: 3E large 3C less
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

### 帖子 #23: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 660

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #24: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #25: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #26: print('retrying in', result.headers["retry-after"], 'seconds')
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

### 帖子 #27: 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回
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

### 帖子 #28: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
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

### 帖子 #29: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #30: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #31: 一种随机生成 SuperAlpha，进行机器回测的方式代码优化
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

### 帖子 #32: 使用[ClickHouse📕]建设你的大型数据库
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

### 帖子 #33: 关于IND地区Robust universe sharpe的改善方法经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md
- **讨论数**: 11

相信有很多顾问和我一样在回测IND地区的alpha的过程中经常遇到Robust universe sharpe较低因此达不到提交要求的问题，经过不断探索社区里各位大神的建议，我发现一些有效解决这个问题的方法，但是我这里的修改方法仅供参考，而且只针对"Robust universe sharpe"这个问题，大家不要学我用了很多operater后让alpha过度拟合了。


> [!NOTE] [图片 OCR 识别内容]
> Instrument Type
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handl
> Equity
> IND
> TOP5OO
> Fast Expression
> 0.08
> Market
> On
> On
> Verify
> Clone Alpha
> N Chart
> Pnl
> 1OM
> 7,500K
> 5,00OK
> 2,5OOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> o IS
> Testing Status
> Period
> IS
> Os
> 9 PASS
> 1FAIL
> Robust universe Sharpe of 0.98 is below cutoff of 1


上图是我回测IND地区的alpha时遇到的Robust universe Sharpe的问题，Robust universe Sharpe还差一点点就达到标准，后面我发现使用以下运算符可以让这个问题得到改善:

group_backfill、group_zscore、winsorize、group_neutralize、group_rank、ts_scale、signed_power，在一个alpha使用以上这几个运算符的其中一两个就好，不建议全部使用，会有过度拟合的问题。其次，如果使用以上的运算符后还是差一点的话可以通过修改时间来解决这个问题，一般我们使用运算符中的时间大多数是252,若时间改成275或者是其他的时间可能可以改善Robust universe Sharpe的问题。不过改时间的话不利于alpha可解释性，如果是实在没法用运算符去修改了可以尝试从时间的角度去修改。还有就是修改Decay或者Truncation还有Neutralization都能帮助我们解决Robust universe alpha这个问题。


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handl
> Equity
> IND
> TOPSOO
> Fast Expression
> 0.08
> Market
> On
> On
> Verify
> Clone Alpha 
> Chart
> Pnl
> 1OM
> 7,50OK
> S,OOOK
> 2,5OOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> o
> IS Testing Status
> Period
> IS
> 0S
> 10 PASS
> 2 WARNING
> Delay


我在修改完运算符里的时间后最终我的alpha通过了Robust universe sharpe这个问题。(但是我这个alpha用了太多运算符导致了过度拟合的问题，大家不要学!!!)

---

### 帖子 #34: print(pools[0])
- **主帖链接**: https://support.worldquantbrain.com[L2] 多线程遍历回测super alpha代码优化_31527668843671.md
- **讨论数**: 21

def multi_simulate2_sa(alpha_pools, neut, region, universe, start):
    global s

s = login()

brain_api_url = ' [[链接已屏蔽]) '

limit_of_concurrent_simulations = len(alpha_pools[0])

alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]
    # print(alpha_pools_2)

end = len(alpha_pools_2)

print(f'length:{len(alpha_pools_2)}, start:{start}')
    counter: int = start
    lock = threading.Lock()

def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):
        while True:
            global s
            lock.acquire()
            nonlocal counter
            if counter > end - 1:
                lock.release()
                break
            if (counter - start) % 250 == 0:  # re-login after every 60 multi_sims
                s = login()
            local_counter = counter
            counter += 1
            lock.release()
            task = pools[local_counter]
            sim_data_list = generate_sim_data_sa(task, region, universe, neut)
            sim_data=sim_data_list[0]
            try:
                simulation_response = s.post(' [[链接已屏蔽]) ', json=sim_data)
                simulation_progress_url = simulation_response.headers['Location']
                # simulation_progress_url = simulation_response.headers.get('location')
            except:
                print(" loc key error")
                sleep(600)
                s = login()

print(f"task {local_counter} post done")

try:
                while True:
                    simulation_progress = s.get(simulation_progress_url)
                    if simulation_progress.headers.get("Retry-After", 0) == 0:
                        break
                    # print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
                    sleep(float(simulation_progress.headers["Retry-After"]))

status = simulation_progress.json().get("status", 0)
                if status != "COMPLETE":
                    print(f"Not complete : {simulation_progress_url}")

"""
                #alpha_id = simulation_progress.json()["alpha"]
                children = simulation_progress.json().get("children", 0)
                children_list = []
                for child in children:
                    child_progress = s.get(brain_api_url + "/simulations/" + child)
                    alpha_id = child_progress.json()["alpha"]

set_alpha_properties(s,
                            alpha_id,
                            name = "%s"%name,
                            color = None,)
                """
            except KeyError:
                print(f"look into: {simulation_progress_url}")
            except:
                print("other")

print(f"task {local_counter} simulate done")

t = []
    for i in range(limit_of_concurrent_simulations):
        t.append(threading.Thread(target=sim_task))
        t[i].start()

for i in range(limit_of_concurrent_simulations):
        t[i].join()

print("Simulate done")

def generate_sim_data_sa(alpha_list, region, uni, neut):
    sim_data_list = []
    for selection_exp, combo_exp in alpha_list:
        # print(selection_exp)
        # print(combo_exp)
        simulation_data = {
            'type': 'SUPER',
            'settings': {
                'instrumentType': 'EQUITY',
                'region': region,
                'universe': uni,
                'delay': 1,
                'decay': 6,
                'neutralization': neut,
                'truncation': 0.08,
                'pasteurization': 'ON',
                'unitHandling': 'VERIFY',
                'nanHandling': 'ON',
                'selectionHandling': 'POSITIVE',
                'selectionLimit': 1000,
                'language': 'FASTEXPR',
                'visualization': False,
            },
            'selection': selection_exp,
            'combo': combo_exp}

sim_data_list.append(simulation_data)
    return sim_data_list

```
import threading
```

```
from machine_lib import *
```

selection_exp=['turnover<0.15']
combo_exp=['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr);maxCorr = reduce_max(ic); 1 - maxCorr']
sa_list=[(i,j) for i in selection_exp for j in combo_exp]
print(len(sa_list))
print(sa_list[0])

pools = load_task_pool(sa_list, 1, 3)
# print(pools[0])
region_dict = {"usa": ("USA", ["TOP3000", "TOP1000", "TOP500", "TOP200"]),
               "asi": ("ASI", ["MINVOL1M"]),
               "eur": ("EUR", ["TOP2500","TOP1200", "TOP800", "TOP400"]),
               "glb": ("GLB", ["TOP3000", 'MINVOL1M']),
               "hkg": ("HKG", ["TOP800", "TOP500"]),
               "twn": ("TWN", ["TOP500", "TOP100"]),
               "jpn": ("JPN", ["TOP1600", "TOP1200"]),
               "kor": ("KOR", ["TOP600"]),
               "chn": ("CHN", ["TOP2000U"]),
               "amr": ("AMR", ["TOP600"])}

norm_opt=["INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"]
risk_opt=["FAST","SLOW","SLOW_AND_FAST"]
r1=['STATISTICAL']
cr=["CROWDING"]
co=["COUNTRY"]
no=["NONE"]
neut_opt={"USA":norm_opt+cr+risk_opt+r1,
          "GLB":co+r1,
          "EUR":co+cr+norm_opt+risk_opt+r1,
"ASI":co+cr+norm_opt+risk_opt+no,
"CHN":norm_opt+cr+risk_opt+r1,
          "KOR":norm_opt,
          "TWN":norm_opt,
          "HKG":norm_opt,
          "JPN":norm_opt,
          "AMR": ["COUNTRY"]+norm_opt,
          }

regi = ['usa']
for k in regi:
    for i in region_dict[k][1][:1]:
        print(i)
        for j in neut_opt[k.upper()]:
            print(j, region_dict[k][0])
            multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)

最后说明，该代码的多线程部分是由一位大佬编写，用于回测regler alpha，曾经分享在学习群，我在此基础改编成用于回测super alpha。如果本人看到此贴请留下相关链接，后续加上相关信息。

---

### 帖子 #35: Calculate rolling correlation over a window of two years-400个交易日至500个交易日rolling_correlation = final_df.rolling(window=400).corr()This gives a MultiIndex DataFrame where level 0 is the date and level 1 is the column pair.You can access the correlation for a specific pair like this:Access the correlations for 'value_main' columncorrelation_main = rolling_correlation.xs('value_main', level=1)correlation_main.plot()
- **主帖链接**: https://support.worldquantbrain.com[L2] 英才候选人计划实训考核Case5__202403期作业提交处_20852222347159.md
- **讨论数**: 35



---

### 帖子 #36: 【断粮急救】IND 地区 alpha 手搓至能提交的案例分享
- **主帖链接**: 【断粮急救】IND 地区 alpha 手搓至能提交的案例分享.md
- **讨论数**: 0

一、序言相信做过 IND 地区的朋友都知道，此地区挖 alpha 总有一道槛 “Robust universe Sharpe”。我也是被这个问题折磨了很久，最终结合论坛大佬的分享及自己的实践摸索，算是有了些针对性优化的套路，在此结合案例分享给大家。首先，感谢来自ZX12447的帖子：《关于IND地区Robust universe sharpe的改善方法》二、套路分享：1. 先调 Settings Neutralization，获得表现最佳的配置。2. 表达式中若没有 group_ 操作符，给表达式套上一个 group_* 操作符（遍历  group_rank、group_zscore、group_neutralize、group_normalize）分组参数用 'market'，寻找最佳表现 alpha。3. 遍历 group_ 操作符参数（market，sector，industry，subindustry）寻找最佳表现 alpha。4. 表达式中时序操作符参数微调，例如 ts_zscore, ts_mean, ts_backfill 等等，遍历有经济学含义的日期参数（5， 22， 66， 126， 252， 504），捕捉 Robust universe Sharpe 的变化趋势，再进行微调。例如 22 -> 66 -> 126 ，发现 Robust universe Sharpe 先升后降，则可继续在 22~66 之间继续寻找合适的参数。5. 尝试追加 winsorize, kth_element, ts_backfill, group_backfill 等操作符，仅对核心信号作处理。此举意在不破坏表达式逻辑的情况下进行数据优化（补全、去极值），看是否有更优表现。6. 尝试增加 signed_power 操作符，意图对不改变信号方向的前提下对信号作缩放，看能否有更优表现。7. 尝试增加 ts_mean, ts_scale, ts_quantile，此举属于最后挣扎，追加操作符后原数据分布有调整，信号原逻辑大概率已被破坏。Robust universe Sharpe > 0.85 的 alpha 可作为种子。将以上步骤过一遍，若还没有明显好转 ，建议果断放弃。另外每一步调整后记得看下 pc ，避免做无用功。三、实战案例分享：1、遍历后确认 Nuetralization 设为 SLOW 最佳，表现如下：2、遍历 group 操作符参数，发现 sector 效果更优：3、调整 kth_element 操作符参数 120 -> 504 效果更优：4、增加 group_backfill 补全数据，去除极值，优化成功：四、写在最后运用此套路，我成功调出来了四个 alpha，但鲁棒性测试表现均一般，可见有过拟合风险。此法在断粮、冲塔等不得已之时可以尝试，平日慎用。

---

### 帖子 #37: 【断粮急救】IND 地区 alpha 手搓至能提交的案例分享
- **主帖链接**: https://support.worldquantbrain.com【断粮急救】IND 地区 alpha 手搓至能提交的案例分享_37234487571479.md
- **讨论数**: 0

**一、序言**

相信做过 IND 地区的朋友都知道，此地区挖 alpha 总有一道槛 “Robust universe Sharpe”。

我也是被这个问题折磨了很久，最终结合论坛大佬的分享及自己的实践摸索，算是有了些针对性优化的套路，在此结合案例分享给大家。

首先，感谢来自 [ZX12447](/hc/zh-cn/profiles/33370816845079-ZX12447) 的帖子： [《关于IND地区Robust universe sharpe的改善方法》]([L2] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md)

**二、套路分享：**

1. 先调 Settings Neutralization，获得表现最佳的配置。

2. 表达式中若没有 group_ 操作符，给表达式套上一个 group_* 操作符（遍历  group_rank、group_zscore、group_neutralize、group_normalize）分组参数用 'market'，寻找最佳表现 alpha。

3. 遍历 group_ 操作符参数（market，sector，industry，subindustry）寻找最佳表现 alpha。

4. 表达式中时序操作符参数微调，例如 ts_zscore, ts_mean, ts_backfill 等等，遍历有经济学含义的日期参数（5， 22， 66， 126， 252， 504），捕捉 Robust universe Sharpe 的变化趋势，再进行微调。例如 22 -> 66 -> 126 ，发现 Robust universe Sharpe 先升后降，则可继续在 22~66 之间继续寻找合适的参数。

5. 尝试追加 winsorize, kth_element, ts_backfill, group_backfill 等操作符，仅对核心信号作处理。此举意在不破坏表达式逻辑的情况下进行数据优化（补全、去极值），看是否有更优表现。

6. 尝试增加 signed_power 操作符，意图对不改变信号方向的前提下对信号作缩放，看能否有更优表现。

7. 尝试增加 ts_mean, ts_scale, ts_quantile，此举属于最后挣扎，追加操作符后原数据分布有调整，信号原逻辑大概率已被破坏。

Robust universe Sharpe > 0.85 的 alpha 可作为种子。将以上步骤过一遍，若还没有明显好转 ，建议果断放弃。另外每一步调整后记得看下 pc ，避免做无用功。

**三、实战案例分享：**

1、遍历后确认 Nuetralization 设为 SLOW 最佳，表现如下：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Core
> sinal
> kth_element (enterprise_Value
> to_ebitda_current
> fndl7
> qgPOSMEn, 120,
> k"1
> lnore
> NAN 8");
> Sinale Daza Set Alpha
> Broup_neutralize(ts_quantile
> Core_signal,
> 22),
> industry )
> Aggregate Data
> 31aroE
> LUTMCNe|
> TItness
> ReTU「nS
> UrawdoIn
> IareI
> 1.94
> 16.049
> 1.41
> 8.4496
> 4.6096
> 10.539600
> Simulation Settings
> Instrument Type
> Region
> Unmerse
> Lanquage
> Decay
> Delay
> Truncation
> Meutralization
> Pasteunization
> NaN Handling
> Unit Handling
> MaTrade
> Year
> Sharpe
> Turnover
> Ftnoss
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> Equi?
> ID
> TOPSJD
> Fast Expression
> 0.03
> SOWFaCOrs
> Verify
> 2013
> 0.33
> 15.914
> 0.23
> 2.3760
> 60
> 3.7492
> 217
> 2011
> 11.934
> 12.3350
> 2934
> 21.509533
> 234
> 2015
> 1.75
> 13.324
> 7.5490
> 2.314
> 11.47923
> 256
> 241
> Clone Alpha
> 2015
> 3.22
> 12.314
> 3.24
> 12.5230
> 1.214
> 09333
> 250
> 2017
> 15.324
> 3.1635
> 3.214
> 0329
> 254
> 2013
> 15.321
> 0.73
> 5.55
> 2.751
> 639323
> 250
> 254
> Chart
> Pnl
> 2019
> 0.97
> 15.754
> 3.7455
> 2534
> 4749
> 252
> 2020
> 2.52
> 17.314
> 2.17
> 12.2031
> 554
> 13.719
> 253
> 2021
> 2.07
> 20.734
> 1.34
> 685
> 334
> 33932
> 254
> 252
> 2022
> 2.33
> 19.354
> 3.1755
> 2.134
> 39
> OOOK
> 2023
> 7.23
> 13.724
> 21.5135
> 534
> 23.039522
> 243
> SOOK
> Correlation
> Self Correlation
> WaYITUN
> UIINITUI
> Last Run:
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> CN



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> PASS
> 1FAIL
> Robust universe Sharpe f 0,87
> below CUoTof1
> WARNING
> 4PENDING


2、遍历 group 操作符参数，发现 sector 效果更优：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> core_signal
> kth_element (enterprise
> Value_
> to_ebitda
> Current / fndl7
> qgrosNgn
> 120,
> k="1"
> inore=
> NAN
> 睛sinale Data Set Alpha
> group_neutralize (ts_quantile
> Core_siBnal
> 22),
> Sector
> Aggregate Data
> Sharpe
> TUICnOE
> itne
> REIICns
> Cram
> Marein
> 1.80
> 16.169
> 1.25
> 7.779
> 4.1
> 9.629600
> Simulation Settings
> Instrument Type
> Region
> Unmerse
> Language
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> Sharpe
> TUIIOVeT
> Ftnoss
> Returns
> Drawdown
> Marqin
> Count
> Short Cownt
> Equiz
> IID
> TOPSD0
> Fast Erpression
> 0.03
> SIOW Fac-ors
> 0f
> Verify
> 2013
> 0.75
> 15.124
> 4.2755
> 1174
> 5239
> 218
> 225
> 2011
> 1.75
> 11.331
> 5.416
> 2.351
> 09333
> 233
> 2015
> 0.93
> 13.434
> 0.55
> 4.1935
> 2234
> 57292
> 254
> 245
> Clone Alpha
> 2016
> 2.35
> 12.-54
> 10.5031
> 1.144
> 17.0
> 213
> 2017
> 2.20
> 1.311
> 5.43
> 3.584
> 669323
> 254
> 2013
> 16.914
> 4950
> 2.-54
> 5.869
> 253
> 250
> Chart
> Pnl
> 2019
> 1.17
> 15.374
> 0.52
> 4.456
> 551
> 2020
> 17.954
> 253
> 13.8130
> 2.554
> 15339323
> 253
> 2021
> 2.05
> 20.944
> 1.31
> 3.5935
> 1.544
> 571
> 254
> OOOK
> 2022
> 20.124
> 1.13
> 7.316
> 2.724
> 30923
> 256
> 2023
> 一71
> 19.084
> 4.23
> 15.3630
> 0.571
> 09333
> 259
> 2-0
> 25OOK
> Correlation
> Self Correlation
> LIam IF
> IinimFT
> T
> TII:
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 8);
> Long
> C



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 9PASS
> 1FAIL
> Robust unwerss Sharpe Of0.93
> below CUOfof1
> WARNING
> PENDING


3、调整 kth_element 操作符参数 120 -> 504 效果更优：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> core_signal
> kth_element(enterprise_value
> to_ebitda
> Current / fndl7
> qgrosNgn
> 504,
> k="1
> inore
> N
> 睛sinale Data Set Alpha
> Broup_neutralize (ts_quantile
> Core_signal,
> 22),
> Sector
> Aggregate Data
> Sharpe
> TUCnOE
> itne
> REIICns
> Cram
> Marein
> 1.81
> 16.149
> 1.26
> 7.8096
> 4.50%
> 9.6
> Yooo
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Year
> TUIIOVeT
> Ftness
> Returns
> Drawdown
> Marqin
> Count
> Short Cownt
> Equiz
> IND
> TOPS0
> Fast Erpression
> 0.03
> SIOW Facors
> 0f
> Verify
> 2013
> 0.35
> 15.044
> 0-7
> 4.3155
> 534
> 009532
> 220
> 225
> 2011
> 210
> 11.343
> 3.3760
> 2.244
> 6.8-923
> 239
> 2015
> 0.95
> 13.504
> 4.0255
> 2.254
> 692
> 254
> 245
> Clone Alpha
> 2016
> 2.93
> 12.-54
> 2.33
> 11.2031
> 1.134
> 17.999532
> 213
> 201
> 27
> 15.304
> 5.706
> 3.524
> 11.019322
> 22
> 254
> 2013
> 16.344
> 5350
> 2.-04
> 939
> 253
> 250
> Chart
> Pnl
> 2019
> 114
> 15.914
> 0.53
> 4.33
> 531
> 449323
> 250
> 2020
> 2.95
> 17.914
> 53
> 13.8930
> 2.514
> 155293
> 2021
> 1.71
> 20.954
> 0.93
> 7.0355
> 1.754
> 692
> 254
> 253
> 5OOOK
> 202
> 20.144
> 1.10
> 7.1750
> 2.754
> 7.12923
> 2023
> 5.03
> 19.284
> 457
> 5.5190
> 689
> 172-932
> 250
> 239
> Z5OOK
> Correlation
> Self Correlation
> LIam IF
> CTTNIC
> -+
> TII:
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 8);
> Sharpe
> Long



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 9PASS
> 1FAIL
> Robust universe Sharpe Of 0.94
> below CUoTof1
> WARNING
> 4PENDING


4、增加 group_backfill 补全数据，去除极值，优化成功：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Core
> sinal
> kth_element (enterprise_value
> to_ebitda
> Current
> fndl7
> qgrosmEn,
> 504,
> k"1
> lnore
> NAN 8");
> Single Data Set Alpha
> B_bf_signal
> Broup_backfill
> COpe
> sinal,
> Sector
> 5td=3);
> Broup_neutralize (ts_quantile(g_bf_slnal
> 22),
> Sector
> Aggregate Data
> SIaTO
> TUTTOVE
> II2
> EUTR
> UraWJUMIT
> Marein
> 1.67
> 15.96%
> 1.11
> 7.0396
> 5.54%
> 8.8
> 9600
> Simulation Settings
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> Instrument Type
> Region
> Unmerse
> Lanquage
> Decay
> Delay
> Truncation
> Meutralization
> Pasteunization
> NaN Handling
> Unit Handling
> MaTrade
> 2013
> 0.50
> 15.444
> 0.23
> 3.456
> 544
> 443923
> 223
> Equi?y
> ID
> TOPSJD
> Fast Expression
> 0.03
> SOWFaCOrs
> 0f
> Verify
> 2011
> 11.354
> 3.2535
> 034
> 14539
> 244
> 2-2
> 2015
> 13.254
> 0.-
> 51-
> 71
> 7.7592
> 256
> 241
> 2015
> 2.93
> 12.-34
> 72
> 10.7630
> -31
> 1731933
> 2-9
> Clone Alpha
> 2017
> 2.23
> 15.534
> 1.70
> 3.5535
> 03*
> 039522
> 253
> 253
> 2013
> 16.644
> 0.51
> 4106
> 3.774
> 9392
> 253
> 250
> N Chart
> Pnl
> 2019
> 0.31
> 15.344
> 003
> 1.1255
> 354
> 429
> 255
> 243
> 2020
> 17.374
> 2.65
> 4.0355
> 334
> 15.759522
> 252
> 213
> 2021
> 127
> 20.944
> 0.54
> 5.366
> 954
> 5.11923
> 254
> 253
> 2022
> 2.44
> 20.104
> 3.3355
> 034
> 8.899523
> OOOK
> 2023
> 6.54
> 13.934
> 7.21
> 22.4050
> 0.534
> 23.609522
> 233
> OOOK
> 医 Correlation
> Self Correlation
> Waximur
> Winimun
> Last Run:
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Prod Correlation
> LIam IF
> Minimum
> Lt RIM:



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10 PASS
> Sharpe OT 1.67isaboVe CUOffof
> Finess Of1.11is
> bove Cutoffof
> Turnoverof 15,9696
> abore CUoTof 196.
> Turnover of 15.969 is below CUOff of 409
> Neishtis WelI distribu-ed owerinstruments
> Sub-unierse Sharpe OT 1.01
> aboVe CuOfof 0.49
> Robust universe Sharpe Of 1.01
> bore cutoffot1,
> 2yearSharpe Of204is
> boire Cutoff of 1.58,
> Pyramid theme INDIDTIFUNDAMENTAL Matches ith multiplierof
> .5. Effective Pyramid count for Genius is
> These hemes mazch with the followine multipliers: Scalable ATON Theme
> 2;INDIDIIFUNDAMENTAL Pyramid Theme
> 1.5,The fina
> thEME
> multipler
> 2.5


**四、写在最后**

运用此套路，我成功调出来了四个 alpha，但鲁棒性测试表现均一般，可见有过拟合风险。此法在断粮、冲塔等不得已之时可以尝试，平日慎用。

---

### 帖子 #38: 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案
- **主帖链接**: 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案.md
- **讨论数**: 1

首先感谢 XZ23611 分享的帖子：“【提升Check Submission效率】一些可以提升Check Submission的Tips，效率提高10倍以上”其中分享的代码非常实用。一般情况下，使用这套代码本地计算self-correlation值与Brain 平台计算的结果值，一般只会有 0.02~0.05 的差异，对于实战完全够用。但有个场景下，计算结果与平台结果天差地别：看以下案例：Alpha_id1 的pnl曲线：Alpha_id2 的pnl曲线：关键点就是alpha 的pnl数据日期不一致，且批量获取 pnl 时先获取了数据日期较少的alpha.这种情况下，get_pnl_panel( ) 函数中，对多个alpha的pnl_df 进行合并时，由于行数不一致，合并后的 pnl_df 会出现 Date 索引乱序。而后续计算自相关性时，pnl 数据的时序性是非常关键的，如果非时序结果自然完全不同。pnl_df 只包含 alpha1 时，print(pnl_df.index):pnl_df 合并 alpha2 后，print(pnl_df.index):解决方案：修改get_pnl_panel() 函数即可：希望遇到相同场景的伙伴，能节省调试时间，少走弯路。最后祝愿所有顾问伙伴，2025年都能收获满满~

---

### 帖子 #39: 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案
- **主帖链接**: https://support.worldquantbrain.com【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案_29002502448279.md
- **讨论数**: 1

首先感谢 XZ23611 分享的帖子：
“ [【提升Check Submission效率】一些可以提升Check Submission的Tips，效率提高10倍以上]([L2] 【提升Check Submission效率】本地计算自相关和提高check的tips效率提高10倍以上代码优化_28524742174359.md?page=1#community_comment_28755853659031) ”其中分享的代码非常实用。一般情况下，使用这套代码本地计算self-correlation值与Brain 平台计算的结果值，一般只会有 0.02~0.05 的差异，对于实战完全够用。

但有个场景下，计算结果与平台结果天差地别：

看以下案例：


> [!NOTE] [图片 OCR 识别内容]
> ids
> ['alphal
> alphaz' ]
> Checkable_ids
> check_remove_self_correlation(5,
> example_ids,
> Os_ret_df)
> example


Alpha_id1 的pnl曲线：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 3JCJ
> 7JCJ
> TU


Alpha_id2 的pnl曲线：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 4,00J
> 1[


关键点就是alpha 的pnl **数据日期不一致，** 且批量获取 pnl 时先获取了数据日期较少的alpha.

这种情况下，get_pnl_panel( ) 函数中，对多个alpha的pnl_df 进行合并时，由于行数不一致，合并后的 pnl_df 会出现 Date 索引乱序。

而后续计算自相关性时，pnl 数据的时序性是非常关键的，如果非时序结果自然完全不同。


> [!NOTE] [图片 OCR 识别内容]
> 转Ipnl
> 主契用干处理super alphat含有ris
> NPRNe
> HJpnl
> 转 Hdatatrae
> pnl panel(session
> alpha Iist)
> 40NA
> pr5
> fetch_pnls (session,
> Jlpha_list)
> pd, DataFral()
> alpha
> LOUN
> (alpha_pnls)
> 检苴p1对桌是杏有j50n方达
> 如臾夯。则涸用该方法获耶数晷
> hasattr(pnl
> J5OI
> collable(pnl.Json)
> Nat?
> json()
> 8158.
> 惧设p1己经昱宁典桕式
> Ta
> 尬 records的列战
> 1 len(data [
> records' ][]
> PdUatatrane(datal
> 「PCOFO
> COLUII
> Uale
> alpha_Id]
> df.set
> Tne
> inplace
> True)
> Plif len(data
> TeCORO
> proertins
> Hta[ 'schema
> J[ properties
> 处果合有' risk-neutralized-pol
> 0罔}
> 井{除且怕彘6列
> ay(prop
> Ial
> 「isk-neutralized-Pnl
> OPO[
> DTOIerTIes:
> TLOTUS
> [record[:7] for pecord
> in data[ records
> DtFTmPCOPO
> TILIIII
> Date
> alpha_id])
> ut.set
> Ide( Uate
> Inplace-True
> 01
> tererordslg列」9
> @不包含' risk pevtralized pnl
> NHi这 Talpha
> COTILLTIUL
> 捋~芦alpha jdgyoatafrae SgAoataframe台并
> pnl_df. empty
> merge df 后
> 作为 index 的 Dale 会乱序
> 8
> pl_Tf
> p.merBe(pnl_#f,
> Dte '
> T
> MUt
> PTI[
> pnl_df
> Rot
> Dnl
> 0]
> Onl
> Dl
> 0302
> Dl


pnl_df 只包含 alpha1 时，print(pnl_df.index):


> [!NOTE] [图片 OCR 识别内容]
> Index( ['2012-07-16'
> 2012-07-17' '
> 2012-07-18
> 2012-07-19
> 2012-07-20
> 2012-07-23
> 2012-07-24
> 2012-07-25
> 2012-07-26
> 2012-07-27
> 2022-07-01 `
> 2022-07-05
> 2022-07-06
> 2022-07-07
> 2022-07-08
> 2022-07-11
> 2022-07-12'
> 2022-07-13
> 2022-07-14
> 2022-07-15
> dtype
> object
> TAINI
> Date
> LenBth-2495 )


pnl_df 合并 alpha2 后，print(pnl_df.index):


> [!NOTE] [图片 OCR 识别内容]
> Index( [ '2012
> 07-16'
> 2012-07-17 ,
> 2012-07-18'
> 2012-07-19
> 2012-07-20
> 2012-07-23
> 2012-07-24
> 2012-07-25
> 2012-07-26
> 2012-07-27
> 2021-07-05'
> 2021-09
> 2021-11-25
> 2021-12-24'
> 2022-01-17
> 2022-02-21
> 2822-04-15
> 2022
> 05-30
> 2022-06-20
> 2022-07-04' ]
> dtype= 'object
> name=
> Date
> length=2588 )


解决方案：

修改get_pnl_panel() 函数即可：


> [!NOTE] [图片 OCR 识别内容]
> Jet get_pr_panel(sesslon,
> alpha_Iist):
> pnl
> alpha id in tqdm(alpha DnIs)
> 检芦pnl对t是否有jso方法
> 如卑有
> 则调用该方法荻取数据
> i hasattr(pnl
> Json
> Callable(pnl .Json ) :
> Jata
> json()
> 0u ;
> n设p1己经足字典概式
> Jata
> 检苴records的列数
> i len(data[ 'records ' ][0])
> pd.DataFrame (datal 'records'
> OILIIIIIC
> Date
> alpha _id1)
> df, set_inde( 'Date
> iplace=True)
> elif len(data[ records '][0])
> properties
> Jata 
> SChela
> 1[ 'properties
> 如果含有 'risk nevtralized DnI
> 则保留这
> 井掰除其他颗外伪列
> i any(prop [ name
> Tisk-neutralized
> tor prop in properties)
> TOMTO'
> [record[:2] for record
> in Jata
> FeCurus
> pd.DataFrame(records
> COLUIIIS
> Date
> alpha_id])
> df. set_index( 'Date
> inplace=True)
> 675e +
> 如果records{9}列数为3
> 但下包含'risk neutralized pnl
> 则跳过这 Falpha id
> Continwe
> 将当Halpha_idfDataFraaeSRIDataFrame合井
> pnLdf,empty:
> pnl_df
> C」Se ;
> Dd
> pd.NerRe(pnl df
> Date
> TO
> outer
> pnl_df
> pnl_df. sort_indexgJ
> peturn pnl df
> FO
> Onl
> Oml
> pnl


希望遇到相同场景的伙伴，能节省调试时间，少走弯路。

最后祝愿所有顾问伙伴，2025年都能收获满满~

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《附录：所有函数速查表》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] DCC比赛Tutorial和代码详解代码优化_38631459115543.md
- **评论时间**: 3个月前

这教程太硬核了！从环境搭建到三套工作流对比，从API详解到Smart Batching原理，把DCC比赛全流程扒得明明白白。特别是"新手路径C→进阶B→高精A"的递进设计，还有LLM异步坑、token消耗这些细节提醒，都是踩过坑才能写出来的干货。附录函数速查表更是贴心，直接当文档查。感谢整理，省了我至少一周摸索时间！

---

### 探讨 #2: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享.md
- **评论时间**: 3个月前

这反转太戏剧性了！一个月从-1.2干到3.18，简直地狱到天堂。核心教训就几条：

1. 别月底入坑新 region 当冤种；
2. 新人远离D0高难度矿区；
3. margin比sharpe/fitness更保命、地区要广撒网但也别乱开。

最反直觉的是12月fitness和sharpe反而降了，但margin够硬combine照样起飞——说明手续费意识才是真金白银。

每日2个因子节奏稳，20+地区深度铺，这路子确实扎实。

感谢分享这活生生的"全错到全对"样本。

---

### 探讨 #3: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md
- **评论时间**: 3个月前

这反转太戏剧性了！一个月从-1.2干到3.18，简直地狱到天堂。核心教训就几条：

1. 别月底入坑新 region 当冤种；
2. 新人远离D0高难度矿区；
3. margin比sharpe/fitness更保命、地区要广撒网但也别乱开。

最反直觉的是12月fitness和sharpe反而降了，但margin够硬combine照样起飞——说明手续费意识才是真金白银。

每日2个因子节奏稳，20+地区深度铺，这路子确实扎实。

感谢分享这活生生的"全错到全对"样本。

---

### 探讨 #4: 关于《【Alpha灵感】A股换手率类因子》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】A股换手率类因子.md
- **评论时间**: 1年前

[KJ42842](/hc/en-us/profiles/12429216262167-KJ42842)  精彩，感谢分享！

---

### 探讨 #5: 关于《【Alpha灵感】A股换手率类因子》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】A股换手率类因子_18600255773719.md
- **评论时间**: 1 year ago

[KJ42842](/hc/en-us/profiles/12429216262167-KJ42842)  精彩，感谢分享！

---

### 探讨 #6: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】ai推荐比率按照实际含义推荐operator经验分享_37141295460375.md
- **评论时间**: 6个月前

我也在尝试往这个方向努力，由 AI 先对数据集进行分析并输出有经济学意义的 “两两字段组合”，并推荐与之匹配的因子策略。然后再基于此去构造 alpha 表达式。

还在摸索中，感谢分享给予灵感！

============================ 积跬步，至千里 =============================

---

### 探讨 #7: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template_37117908343831.md
- **评论时间**: 6个月前

点赞评论加关注了，看着无比丰富多样，感谢分享。这就去尝试整合进自己的工作流。

============================== 积跬步，至千里 =============================

---

### 探讨 #8: 关于《【Community Leader -因子筛选与组合⭐】判断因子是否可以提交，稳住你的combine经验分享》的评论回复
- **帖子链接**: [Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md
- **评论时间**: 3个月前

这标准清晰得能当教科书了！fitness排首位、margin卡死地区底线+0.05%、sharpe≥1且fitness≥0.6才进门，最近3年任何指标明显掉链子直接pass——把"组合增益>单因子指标"的思路量化得明明白白。看完直接抄作业，感谢大佬分享！

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】提高效率之过滤出ROBUST_UNIVERSE_SHARPE高的IND alpha经验分享_37112731513879.md
- **评论时间**: 6个月前

很棒的方法，感谢分享。最近也是在跟 IND 地区死磕，结合大佬给出的工具，找待优化种子 alpha 的效率大大提升了~

=========================== 积跬步，至千里 ============================

---

### 探讨 #10: 关于《【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享》的评论回复
- **帖子链接**: [Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享.md
- **评论时间**: 6个月前

一次 SA 打满 60 刀也许是运气，连续几天每天都打满 60 刀，那就肯定是实力了！

感谢大佬无私分享自己的方法，非常受用。

我现在也是按照 datacategories 结合其他限制条件分层构建一个小池子，再组合多个小池子的方法去做 selection。真的挺容易出高表现，低相关 SA 的。

============================ 积跬步，至千里 ===========================

---

### 探讨 #11: 关于《【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享_33316845356439.md
- **评论时间**: 6个月前

一次 SA 打满 60 刀也许是运气，连续几天每天都打满 60 刀，那就肯定是实力了！

感谢大佬无私分享自己的方法，非常受用。

我现在也是按照 datacategories 结合其他限制条件分层构建一个小池子，再组合多个小池子的方法去做 selection。真的挺容易出高表现，低相关 SA 的。

============================ 积跬步，至千里 ===========================

---

### 探讨 #12: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【效率王】你说你没有模板这里你多得用不完.md
- **评论时间**: 6个月前

感谢大佬分享，第一时间实践，期待好的结果！！

---------------------------------------------------------------------------------------------------

----------------------------------- 积跬步，至千里 -------------------------------------------

---------------------------------------------------------------------------------------------------

---

### 探讨 #13: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **评论时间**: 6个月前

感谢大佬分享，第一时间实践，期待好的结果！！

---------------------------------------------------------------------------------------------------

----------------------------------- 积跬步，至千里 -------------------------------------------

---------------------------------------------------------------------------------------------------

---

### 探讨 #14: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

【量化日记 DAY1】：

新规后，因 model31 数据集权限被收走，之前的存货归零了。

外部环境总是会变化的，困难总是存在，大家都一样，不抱怨，想办法解决。

修改代码，重新选定了新的数据集，继续跑三阶模板。

皇天不负有心人，终于又出货了。

计划接下来一周，实现三阶模板自动化。解放人力后，将精力放在研究论坛中的模板大师。

各位战友，2025国服要崛起，一起加油吧！

---

### 探讨 #15: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

【量化日记 DAY2】：

今天继续用三阶模板跑 anl4 数据集，实测有坑的字段：

anl4_fcfps_flag、anl4_ffo_flag...

PNL表现：

[图片 (图片已丢失)]

进一步推断  **_flag**  后缀的字段要小心，可以考虑过滤掉先不跑，或者手动探索下数据情况。

以上分享，望能帮助战友避坑，节省时间。

---

### 探讨 #16: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

今天用量化研究小组虎哥提供的“双字段回归”模板，成功挖出不少 alpha。

相较于新手村赠送的三阶模板，此模板的优势明显：

1. 出货率高。

2. 提交后一次点亮两个金字塔，效率高。

模板如下：

group_rank(
     ts_regression (
          ts_zscore( ***matrix_data*** , 252), 
          ts_zscore(vec_sum( ***vector_data*** ), 252),
          252),
     densify(sector)
)

感谢虎哥—— **ZZ13271  [ZZ13271](/hc/en-us/profiles/27032633829527-ZZ13271)**

**祝各位伙伴，得所愿。**

---

### 探讨 #17: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

昨天跑了一堆alpha，因为不符合比赛要求，打算囤一囤。

今天 13:00 后想筛着交几个，结果一 check，全部 self-cor 不合格。

问题是，我昨天到今天 13:00，这期间也没有提交过其他 alpha 啊！？

严重怀疑，是不是调(an)整(gai)了 check 规则啊？？？

---

### 探讨 #18: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

【量化日记 DAY1】：

新规后，因 model31 数据集权限被收走，之前的存货归零了。

外部环境总是会变化的，困难总是存在，大家都一样，不抱怨，想办法解决。

修改代码，重新选定了新的数据集，继续跑三阶模板。

皇天不负有心人，终于又出货了。

计划接下来一周，实现三阶模板自动化。解放人力后，将精力放在研究论坛中的模板大师。

各位战友，2025国服要崛起，一起加油吧！

---

### 探讨 #19: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

【量化日记 DAY2】：

今天继续用三阶模板跑 anl4 数据集，实测有坑的字段：

anl4_fcfps_flag、anl4_ffo_flag...

PNL表现：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 20O
> OOK
> OO
> DO
> 2013
> 201
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022


进一步推断  **_flag**  后缀的字段要小心，可以考虑过滤掉先不跑，或者手动探索下数据情况。

以上分享，望能帮助战友避坑，节省时间。

---

### 探讨 #20: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天用量化研究小组虎哥提供的“双字段回归”模板，成功挖出不少 alpha。

相较于新手村赠送的三阶模板，此模板的优势明显：

1. 出货率高。

2. 提交后一次点亮两个金字塔，效率高。

模板如下：

group_rank(
     ts_regression (
          ts_zscore( ***matrix_data*** , 252), 
          ts_zscore(vec_sum( ***vector_data*** ), 252),
          252),
     densify(sector)
)

感谢虎哥—— **ZZ13271  [ZZ13271](/hc/en-us/profiles/27032633829527-ZZ13271)**

**祝各位伙伴，得所愿。**

---

### 探讨 #21: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天跑了一堆alpha，因为不符合比赛要求，打算囤一囤。

今天 13:00 后想筛着交几个，结果一 check，全部 self-cor 不合格。

问题是，我昨天到今天 13:00，这期间也没有提交过其他 alpha 啊！？

严重怀疑，是不是调(an)整(gai)了 check 规则啊？？？

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025-12-09

天气：晴

限流第一天，放平心态，拥抱变化。用 AI 折腾了一上午从0到1构建 alpha，结果非常让人沮丧。各种指标底下，checks 不通过，或者 PC > 0.7 ...

还是对 AI 提示词的使用经验太少，继续看论坛大佬的贴子学习吧，希望早日能搭建好自己的 AI 工作流，在新规下稳定产出 alpha。

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025-12-11

天气：小雨

AI 对 alpha 表现的优化日志：

**Date**: 2025-12-10

**Original Alpha ID**: O0aXMLkp

**Focus**: Improve 2-Year Sharpe (Target > 1.58) and Robust Universe Sharpe (Target > 1.0) using Hybrid Strategies.

## 🧪 Iteration Log (Round 4)

| Expression Description | Sharpe | 2Y Sharpe | Robust Sharpe | Result |

|------------------------|--------|-----------|---------------|--------|

| `rank(corr(75)) + rank(corr(20))` | 1.69 | 1.46 | 1.04 | **Best Combo** |

| `ts_decay_linear(rank(corr(75)), 2)` | N/A | N/A | N/A | Failed/Timeout |

| `group_rank(corr(75))` | 1.72 | 0.84 | 0.67 | High Sharpe, Low 2Y |

| `ts_zscore(decay(rank(corr(75))), 252)` | 1.23 | 0.39 | 0.64 | Failed |

| `ts_rank(corr(75), 252)` | 1.29 | 0.96 | 0.74 | Failed |

| `rank(corr(75)) - 0.5*rank(corr(252))` | 1.22 | 1.02 | 0.71 | Failed |

好奇，这样的优化方式，算不算过拟合？？

---

### 探讨 #24: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025-09-03

天气晴

Q3冲刺月了，我的策略就是点塔和尝试用不同的操作符去构建 ATOM。

今早看到回测报告，发现每小时回测量大幅下降，赶紧打开研究小组群一探究竟。

果然，大家都在吐槽。是什么比赛结算么？或是说 combine 在计算？还是测试数据该偏移了？也可能几样一起来吧。真心希望平台赚多点，然后基础设施多投入点。

对于下一次 combine 更新，内心很矛盾，既期待又焦虑。因为7月份，我开始做 AMR 地区，base 收入可观但内心忐忑，不知 combine 和 vf 能否保住，祈祷。

---

### 探讨 #25: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025-09-05

天气晴

PPA、RA 都断粮，用经典模板已经跑不出 pc < 0.5 的 alpha 了。靠着 SA 每天勉力支撑。

准备转战 JPN region D1 TOP1600，计划先跑一遍全量一阶，筛选出有信号且 pc 较低的 fields，构建 JPN “有信号子数据集”。随后，再根据 dataset 收益加成系数从高到低，在“有信号子数据集”中挑选字段，逐塔击破！

PS，怎么 OS 还不更新呢！？！

---

### 探讨 #26: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-25

上周工作太忙了，连着加班。每天投入到 wqb 的时间只有可怜的1小时，还是每天 6：00 起床挤出来的。为了备战下个赛季，现在跑的alpha全是 macro、news、sentiment 这种字段数量较少的 dataset。希望能把 model、fundamental、analyst 等已经深红的 dataset 稀释下。

=================================== 积跬步，至千里 ===================================

---

### 探讨 #27: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-26

昨天参加了国际会议，老师分享了 SAC 优化提升的方法。示例中 select expression 使用了 not(not(in(xxx)||in(xxx))) 这种写法，细想了一下。
not (in(A) & in(B))  与 not(not(in(A) || in(B))) 逻辑上是不等价的。
如果用前者构建 sa 表现不理想，试试换成后者的写法，会调整部分 select 的 alpha，表现也会有变化。
可以作为多样性的降低 pc 的方案。

================================= 积跬步，至千里 =================================

---

### 探讨 #28: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025-06-27

月底啦，ppa 6月的时间窗口马上要截止。提醒各位顾问，注意调整 POWERPOOL tag，优中选优，争取能在月度评奖中获胜~~
另外，Q2最后冲刺倒计时！还有5天！！

================================= 积跬步，至千里 =================================

---

### 探讨 #29: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12日23日

天气：晴

今天凌晨起来手搓 520 SA，从 0.35 搓到 0.2986，满心欢喜准备提交，结果出现 1 FAIL： 'Your SuperAlpha contains unauthorized component alphas, please clone this alpha and re-simulate' 。

研究小组翻聊天记录发现似乎很多人都遇到了这个问题，无解。

提了 support，等待官方答复。

============================ 积跬步，至千里 ===========================

---

### 探讨 #30: 关于《【日常生活贴】我的量化日记第四季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXdY1z1B86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzQ5OTczMzIxNzgxOTktLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOUIlOUIlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyODg1NDg4Yy1jMDE5LTRjMTMtOWEyMi01MGRkYjgxOTkxYzcGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDg0Njc3BjsIVDoScmVzdWx0c19jb3VudGkg--23bdc5ecf43ba43f1d15c9625a99c4c23b9f8ebd
- **评论时间**: 9个月前

2025-09-25天气晴Q3一直以 GM 为目标努力，金字塔还差 3 个，六维排在 75 左右，三项 combine 数据离 GM 均有差距。只剩定级前最后一次 combine 更新，需要有某项 combine 达到 GM，且六维进入前60。有希望，但不大。还有一周，把能做的做了即可。争其必然，顺其自然。

---

### 探讨 #31: 关于《【日常生活贴】我的量化日记第四季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXdY1z1B86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzQ5OTczMzIxNzgxOTktLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOUIlOUIlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyODg1NDg4Yy1jMDE5LTRjMTMtOWEyMi01MGRkYjgxOTkxYzcGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDg0Njc3BjsIVDoScmVzdWx0c19jb3VudGkg--23bdc5ecf43ba43f1d15c9625a99c4c23b9f8ebd
- **评论时间**: 8个月前

2025-10-08天气晴今天阅读了“传奇耐打王”关于alpha该不该交的帖子，受益匪浅。感恩他的无私分享，感叹咱们中文社区的分享精神。真希望什么时候我也能产出有价值的经验分享与大家。总结下 alpha 该不该交的判断标准：【必要条件】：1. PNL 平滑；2. Margin 达标（usa>5, eur>10, asi>15, glb>15），越高越好；3. sharp、fitness 达标，越高越好；4. 多空不赌博（我理解就是 (long count + short count) / universe 越高越好）【优化条件】：1. 低相关性（低 pc，低 sc）2. sharpe、fitness21年22年表现优秀（sharpe > 1）3. sharpe、fitness逐年表现优秀（sharpe > 1）4. margin21年22年表现优秀（参考必要条件的值）5. margin逐年表现优秀（参考必要条件的值）6. margin、returns 越高越好7. turnover 围绕在 12%，（低于5%的称为“死鱼因子”，看情况交）8. drawdown 越低越好9. 多空优秀（多空相加覆盖universe、多空接近、多空每年情况稳定）10. performance 不一定非要四绿两红，具体根据自己池子情况选择原贴解释详细，案例丰富，非常推荐大家阅读：《这个因子到底能不能交？（上） 【传奇耐打王系列一】》《这个因子到底能不能交？（下） 【传奇耐打王系列一】》

---

### 探讨 #32: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025-09-25

天气晴

Q3一直以 GM 为目标努力，金字塔还差 3 个，六维排在 75 左右，三项 combine 数据离 GM 均有差距。

只剩定级前最后一次 combine 更新，需要有某项 combine 达到 GM，且六维进入前60。

有希望，但不大。

还有一周，把能做的做了即可。

争其必然，顺其自然。

---

### 探讨 #33: 关于《**GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

2025-10-08

天气晴

今天阅读了“传奇耐打王”关于alpha该不该交的帖子，受益匪浅。感恩他的无私分享，感叹咱们中文社区的分享精神。真希望什么时候我也能产出有价值的经验分享与大家。

总结下 alpha 该不该交的判断标准：

【必要条件】：
1. PNL 平滑；
2. Margin 达标（usa>5, eur>10, asi>15, glb>15），越高越好；
3. sharp、fitness 达标，越高越好；
4. 多空不赌博（我理解就是 (long count + short count) / universe 越高越好）

【优化条件】：
1. 低相关性（低 pc，低 sc）
2. sharpe、fitness21年22年表现优秀（sharpe > 1）
3. sharpe、fitness逐年表现优秀（sharpe > 1）
4. margin21年22年表现优秀（参考必要条件的值）
5. margin逐年表现优秀（参考必要条件的值）
6. margin、returns 越高越好
7. turnover 围绕在 12%，（低于5%的称为“死鱼因子”，看情况交）
8. drawdown 越低越好
9. 多空优秀（多空相加覆盖universe、多空接近、多空每年情况稳定）
10. performance 不一定非要四绿两红，具体根据自己池子情况选择

原贴解释详细，案例丰富，非常推荐大家阅读：
 [《这个因子到底能不能交？（上） 【传奇耐打王系列一】》]([L2] 这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md) 
 [《这个因子到底能不能交？（下） 【传奇耐打王系列一】》]([Commented] 这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md)

---

### 探讨 #34: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: [Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法.md
- **评论时间**: 1 year ago

【思路】：基于os 表现好 regular alpha (以下简称 ra) 的特征，构建 select 表达式。

已知满足以下条件的 ra , os 表现大概率较好：

1. returns > turnover;
2. returns > drawndown;
3. PNL 数据完整
4. long_count 与 short_count 接近（多空平衡）
5. long_count、short_count 较大（覆盖面广）
6. 表达式简单，字段较少（避免过拟合，例如 PPA、ATOM）
7. turnover 低于 10% （防止计算交易手续费后亏钱）
8. alpha 在不同 neutralization

第3~7点基本可以通过 select 语句表达，第8点通过同表达式回测所有 neutralizition 来判断（不同 neutralizition PNL 走势及 sa 的六维参数相近）

select 表达式如下：

```
#  sac 主题池，属于主题的得分 1，否则得分 0.theme_score = in(classifications, "POWER_POOL");# dataset_count 挑出 dataset_count 小于等于 2 的，dataset_count 越小得分约高dataset_score = (dataset_count <= 2)*-dataset_count;# turnover 挑选 [2%~10%] 的tvr_score = (turnover >= 0.02 && turnover <= 0.1);# pnlpnl_score = (long_count >= 1000 && short_count >= 1000) * -abs(long_count-short_count) * (long_count+short_count);select_score = theme_score*dataset_score*tvr_score*pc_score*pnl_score;select_score
```

希望对各位有帮助，祝大家在 sac 中取得好成绩。

---

### 探讨 #35: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md
- **评论时间**: 1年前

【思路】：基于os 表现好 regular alpha (以下简称 ra) 的特征，构建 select 表达式。

已知满足以下条件的 ra , os 表现大概率较好：

1. returns > turnover;
2. returns > drawndown;
3. PNL 数据完整
4. long_count 与 short_count 接近（多空平衡）
5. long_count、short_count 较大（覆盖面广）
6. 表达式简单，字段较少（避免过拟合，例如 PPA、ATOM）
7. turnover 低于 10% （防止计算交易手续费后亏钱）
8. alpha 在不同 neutralization

第3~7点基本可以通过 select 语句表达，第8点通过同表达式回测所有 neutralizition 来判断（不同 neutralizition PNL 走势及 sa 的六维参数相近）

select 表达式如下：

```
#  sac 主题池，属于主题的得分 1，否则得分 0.theme_score = in(classifications, "POWER_POOL");# dataset_count 挑出 dataset_count 小于等于 2 的，dataset_count 越小得分约高dataset_score = (dataset_count <= 2)*-dataset_count;# turnover 挑选 [2%~10%] 的tvr_score = (turnover >= 0.02 && turnover <= 0.1);# pnlpnl_score = (long_count >= 1000 && short_count >= 1000) * -abs(long_count-short_count) * (long_count+short_count);select_score = theme_score*dataset_score*tvr_score*pc_score*pnl_score;select_score
```

希望对各位有帮助，祝大家在 sac 中取得好成绩。

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】菜鸟日记代码小白如何稳住6个月VF09经验分享_38767793594775.md
- **评论时间**: 3个月前

惊了，代码小白也能极限卡位GM74！零基础靠一二三阶代码，每月硬怼20塔150因子，sharpe>1、fit>0.5的底线标准卡死，小众数据集灵活取舍不纠结margin，用atom堆出组合稳健性。从手动check到MCP提效，原始人变现代人太真实。这路子野但管用，学到了！

---

### 探讨 #37: 关于《█████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享》的评论回复
- **帖子链接**: [Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享.md
- **评论时间**: 1年前

感谢毛老师无私分享！收获很大！

---

### 探讨 #38: 关于《█████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **评论时间**: 1 year ago

感谢毛老师无私分享！收获很大！

---

### 探讨 #39: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 组sa时如何选取高质量因子经验分享.md
- **评论时间**: 1年前

感谢游戏王哥的分享，期待下一篇~

---

### 探讨 #40: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 组sa时如何选取高质量因子经验分享_32034293019671.md
- **评论时间**: 1年前

感谢游戏王哥的分享，期待下一篇~

---

### 探讨 #41: 关于《经验分享｜PPAC全球第三名，回馈社区经验分享》的评论回复
- **帖子链接**: [Commented] 经验分享PPAC全球第三名回馈社区经验分享.md
- **评论时间**: 1年前

感谢大佬分享，祝后续 PPAC 常规赛，继续优胜！

---

### 探讨 #42: 关于《经验分享｜PPAC全球第三名，回馈社区经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **评论时间**: 1年前

感谢大佬分享，祝后续 PPAC 常规赛，继续优胜！

---

### 探讨 #43: 关于《这个因子到底能不能交？（下） 【传奇耐打王系列一】》的评论回复
- **帖子链接**: [Commented] 这个因子到底能不能交下 【传奇耐打王系列一】.md
- **评论时间**: 8个月前

总结整理的非常棒，还有这么多案例，太优秀啦！感恩无私分享！

---

### 探讨 #44: 关于《这个因子到底能不能交？（下） 【传奇耐打王系列一】》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md
- **评论时间**: 8 months ago

总结整理的非常棒，还有这么多案例，太优秀啦！感恩无私分享！

---
