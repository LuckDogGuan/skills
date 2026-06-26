# 顾问 JG15244 (Rank 67) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 JG15244 (Rank 67) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: Getting started with Analyst DatasetsResearch
- **主帖链接**: https://support.worldquantbrain.com[L2] Getting started with Analyst DatasetsResearch_25238159368215.md
- **讨论数**: 35

**Tips for getting started with  [Analyst]([链接已屏蔽])  Datasets:**

- Analyst datasets have well-structured data fields that can be considered as analysts’ sentiment scores for various fundamental ratios. Common time series and cross-sectional operations such as ts_rank, zscore, or rank can be applied to these fields.
- Comparing analyst scores on the same fundamental ratio from two different time periods can provide useful signals. For this purpose, you can use the ts_delta operator.
- General guidance for using the group operators on model data fields includes trying the following: group_rank, group_neutralize, group_normalize, and group_zscore.
- Since some analyst datasets indirectly seeks to predict returns, you can assess their potential predictive power by taking the correlation of data fields with returns/close prices.
- Analyst datasets can be large and serve as signals that seeks to predict potential returns. Therefore, ts_delta can be useful for this dataset. For instance, changes in EPS can detect earning surprises.
  - When calculating differences, be cautious of stock-split events when dealing with this kind of dataset.
- To reduce exposure to groups, group_neutralize can be helpful.
  - Country and sector neutralizations generally work well, though we recommend trying other groups as well.

**Example Alpha Ideas:**

- Check differences between estimates of long-term versus short-term horizons, and set reversal or momentum signals based on which time horizon is higher. The same idea can apply to comparisons between estimates and actuals.
- Assign Alphas based directly on the estimates, or delta(estimates), or correlation(estimates, returns on the same horizon).
- Assign Alphas in the event of high dispersion among estimates or estimates of different time horizons.

**Recommended Datasets:**

- [Fundamental Analyst Estimates]([链接已屏蔽])
- [Analyst Estimate Daily Data]([链接已屏蔽])
- [ESG scores]([链接已屏蔽])
- [Analyst Estimate Daily Data]([链接已屏蔽])
- [Analyst estimates & financial ratios]([链接已屏蔽])
- [Broker Estimates]([链接已屏蔽])
- [Alternative Analyst Investment Insight Data]([链接已屏蔽])

---

### 帖子 #2: How to Improve After Cost Performance置顶的
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

### 帖子 #4: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
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

### 帖子 #5: Maximizing Combined Alpha Performance: Key Strategies and Insights
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

### 帖子 #6: QuantGo Kit：基于Grafana的WorldQuant量化可视化篇代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] QuantGo Kit基于Grafana的WorldQuant量化可视化篇代码优化_37495033591447.md
- **讨论数**: 5


> [!NOTE] [图片 OCR 识别内容]
> Value-at-Risk
> (Vaz)
> 
> Mean
> Probability
> 一8
> CVaRB
> LOss
> VaRp


## **一、2026 开端**

本篇是基于上篇  **[QuantGo Kit：基于Go开发的WorldQuant量化工具箱篇]([Commented] QuantGo Kit基于Go开发的WorldQuant量化工具箱篇代码优化_37163832225943.md)**  存入数据库数据做 Grafana可视化，多维度查看和分析自己做过的 Alpha，以及 操作符Op 和 Combine & vf & wf 等数据 .


> [!NOTE] [图片 OCR 识别内容]
> Quantco Kit: 基于Co开发的WorldQuant量化工具箱篇
> 代码优化
> 顾问 ML47973 (Rank 100)
> QuantGo Kit 为何诞生?
> 去年十月,说错了。今年十月, WorldQuant 围区的
> Drod
> COII
> 比赛启动后。我创建了第一个文件夹;
> 写了个计箅平均
> Drod_
> COII
> 的小工具
> 随着需求增多;一个个独立的小程序相继诞生
> 每个都待在各自的文
> 件夹里
> 很快问题浮现:  文件夹海洋让我迷失方向。相似的命名让查找娈得困难;  想要对比多个程序效果时,不得不
> 开启数个VSCode窗口。管理成本陡增
> 于是,
> 一个想法诞生:  为什么不让它们和谐共处?  将所有工具集成到统一框架下,
> 一键运行
> 即时对比 .当
> 这个工具箱逐渐成型时,我想
> 也许其他人也会需要这样的便利 
> 就这样, Quant * Go Kit 诞生了


Grafana 官方下载中心： `[链接已屏蔽]  ，我选择下载Grafana到本地，可以不使用Docker启动 . 默认访问地址  `[链接已屏蔽] ，首次登录账号/密码  `admin/admin`  .


> [!NOTE] [图片 OCR 识别内容]
> GrafanaLabs
> Products
> Open Source
> Solutions
> Leam
> Docs
> Downloads
> Contact Us
> Signin
> Grafana
> Overview
> Grafana project
> Grafana Alerting
> Download
> Download Grafana
> Nightly Builds
> Grafana Cloud
> You
> can USe
> Grafana Cloud to avoid installing; maintaining; and scaling Your own instance of Grafana. Create a free account to get started, which includes free forever access to
> 10k series Prometheus metrics; 5068 logs, 50GB traces; & more。
> Version:
> 12.3.
> Edition:
> Enterprise
> The Enterprise Edition is the default and recommended edition.
> It includes all the features of the OSS Edition; can be used for free and can be upgraded to the full
> Enterprise feature set, including support for Enterprise plugins.
> License:
> Grafana Labs License
> Release Date:
> December 17, 2025
> Release Info:
> Linux
> Windows
> Mac
> Docker
> Linux on ARNIG4
> Pricing


## 

## **二、Visual Layout**

从大布局来看，Grafana - WorldQuant 项目下包括

1. Alpha Quant (Alpha信息数据)

2. Combin & vf & wf (Alpha表现 / Value_Factor / Weight_Factor)

3. Op Informatization (季度性操作符Op信息)

4. Pyramid alpha distribution (季度 | 非季度性 金字塔数据)

四大板块信息 .


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dashboards
> Ai &
> 8|众
> 首页 〉仪表板
> 搜索
> CtrItk
> 十 ~
> 仪表板
> 新建
> 创建并管理仪表板,以将您的数据可视化
> 搜索仪表板
> 按标签筛选
> 已加星标
> 排序
> 名称
> 标签
> WorldQuant
> Alpha Quant
> 器 Combine & Vf & Wf
> 器 Op Informatization
> 品 Pyramid alpha distribution
> CloudVendor Classified Files
> Riemann's Ideas & Analysis


其中，Alpha Quant 共包括 6个 Row, 分别是 理论与可投资术语、已提交的全部alpha(包括隐藏和sa)、GroupBy 分组、Ts_Mean 时序均值、Value Factor 潜在可能影响情况 与 Osmosis Competition 2025 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dladrrggglalpha-quant?orgld=
> &from= 2025-02-13T16:00:00.000Z8to=nowatimezone=browsergvar-alphalD=&var-type=s
> all8var-geniusquarter=S_all8var-region= $_
> Ai
> 8 |众
> 首页
> 仪表板
> WorldQuant
> Alpha Quant
> 搜索。
> CtrI-k
> 十 ~
> 0
> 添加
> 设置
> 退出编辑
> 保存仪表板
> AlphalD
> 输入数值
> TYPE
> AIl
> GENIUS季度
> AlI
> REGION
> AlI X
> UNIVERSE
> AlI X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> All X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> (1panel)
> 已提交的全部alpha(包括隐藏和sa)
> Danels)
> GroupBy 分组
> (6 panels)
> Ts_Mean 时序均值
> (5 panels)
> Value Factor 潜在可能影响情况
> Danels)
> Osmosis Competition 2025
> (5 panels)


[图片 (图片已丢失)]

Combin & vf & wf 有3个数据表，数据来源于 weight_value_factor 和 combined_alpha_performance 表，可以分析Combine、wf何时开始有数据，以及变化情况 .


> [!NOTE] [图片 OCR 识别内容]
> 首页
> 仪表板
> WorldQuant
> Combine & Vf & Wf
> Q 搜索
> CtrItk
> 十 ~
> 19
> 编辑
> 导出
> 分享
> Combine & Vf & wf
> Vf & Combine update
> Combine
> Time
> 10
> 12
> 13
> Value_factor
> 0.86
> 0.71
> 0.75
> 0.48
> 0.72
> 0.44
> 0.57
> combined_alpha_performance
> 2.14
> 2.39
> 2.03
> 1.71
> 1.78
> 1.84
> combined_selected_alpha_performance
> 1.47
> 1.32
> combined_power_pool_alpha_performance
> 1.79
> 1.45
> 1.53
> 1.63
> 1.72
> genius_level
> Grand Master
> Calculation_date
> 2025-06-28
> 2025-07-20 2025-08-07
> 2025-08-19
> 2025-09-11
> 2025-09-20
> 2025-10-06
> 2025-10-25  2025-11-20
> 2025-11-21 2025-12-08  2025-12-162026-01-06
> Vf & Combine '折'线图
> 2.6
> 0,86
> 2,39
> 24
> 0,8
> 2.14
> 22
> 0.75
> 2.03
> 0.72
> 0.71
> 0
> 1,84
> 1.79
> 1.,78
> 1.71
> 1.721.8
> 1.63
> 06
> 53
> 0.57
> 1.6
> 1.45
> 1.321.4
> 0.5
> 48
> 0.44
> 1.18
> 1.2
> 04
> 06/28
> 07/05
> 07/12
> 07/19
> 07/26
> 08/02
> 08/09
> 08/16
> 08/23
> 08/30
> 09/06
> 09/13
> 09/20
> 09/27
> 10/04
> 10/11
> 10/18
> 10/25
> 11/01
> 11/08
> 11/15
> 11/22
> 11/29
> 12/06
> 12/13
> 12/20
> 12/27
> 01/03
> Value_factor
> combined_alpha_performance
> combined_selected_alpha_performance
> combined_power_pool_alpha_
> performance
> 1.18


[图片 (图片已丢失)]

Op Informatization 板块目前只包括 operators 表数据，只存了一个图表，支持操作符 / 操作符类别 / Scope 类别 / Genius等级 / Genius季度 等过滤，这个板块我想要做的是 等季度更新之后，再做一个比较的图表，比如: 2025-Q4 与 2026-Q1 操作符比较，掉级导致操作符少了哪些 信息 .


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dladgzmgm/op-informatization?orgld = 18from=now-Gh8to=nowgtimezone=browsergvar-OpName=&var-Category=$
> all8var-Scope=$_
> all8var-Geniuslevel= $_
> alI8Var。。
> A》 &
> 8 |众
> 首页
> 仪表板
> WorldQuant
> Op Informatization
> 搜索。
> CtrI-k
> 十~
> 编辑
> 导出
> 分享
> 操作符名
> 输入数值
> 操作符类别
> AII
> Scope类别
> AlI
> Genius等级
> AlI X
> Genius季度 0
> AlI X
> Op操作符表
> name
> category
> SCODe
> definition
> en_description
> Cn
> add
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> addlxi
> Y, filter
> falsel X + Y
> Add all inputs (at least 2 inputs required). If filter
> true  filterall
> eXP
> Arithmetic
> ["COMBO
> "REGULAR" "SELECTION"]
> eXP(X)
> Natural exponential function: e^x
> multiply
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> multiply(x ,y
> filter-false), X
> Multiply all inputs. At least 2 inputs are required. Filter sets the
> sign
> Arithmetic
> ["COMBO
> "REGULAR" "SELECTION"]
> sign(x)
> 讦 input
> 0, return 1; if input
> 0, return -1; if input
> 0, return 0;
> sUbtract
> Arithmetic
> ["COMBO"
> REGULAR" "SELECTION"]
> subtractlx, Y, filter-false), X -Yy
> X-Y.If filter
> true, filter all input NaN to 0 before
> subtracting
> pasteurize
> Arithmetic
> ["COMBO" "REGULAR"]
> pasteurizelx)
> Set to NaN 讦f Xis INF or if the underlying instrument is notin the
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> Iog(x)
> Natural logarithm. For example: Log(high llow) uses natural logal
> purify
> Arithmetic
> ["COMBO
> "REGULAR", "SELECTION"]
> purify(x)
> Clear infinities (+inf, -inf) by replacing with NaN
> arc_tan
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> arc_tan(x)
> This operator does inverse tangent of input
> log


## **三、详细说明 Alpha Quant 板块**

Alpha Quant 板块 数据来源于 active_alpha_list 数据大表，其中包括了几乎alpha接口的所有数据，不包括 alpha Pnl 数据，然后


> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> AlI
> REGION
> AIl
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> All X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值


**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> OYmgll2
> TYPE 0
> AII X
> GENIUS季度
> AII
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE @
> AII X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
**

**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> AII
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AII X
> STATUS
> AlI X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 样本内-单位收益;非使用例: !二 5%0
> 理论与可投资术语
> panel)
**

**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> OYmgll2
> TYPE 0
> AII
> GENIUS季度
> AlI
> REGION
> AII X
> UNIVERSE
> AIl
> DELAY
> AIl
> NEUTRALIZATION
> AII
> MAX TRADE 0
> AII X
> STATUS
> DECOMMISSIONED X
> xQ
> SHARPE 0
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> Selected (1)
> 理论与可投资术语
> panel)
> AII
> 已提交的全部alpha(包括隐藏和sa)
> ACTIVE
> Submitted Alphas (同网页端)
> DECOMMISSIONED
> 100
> UNSUBMITTED
**

过滤字段 包括 AlphaID 可以查询某一个alpha的信息，TYPE分类 ra 与 sa，alpha 属于哪个大区、股票池、延迟处理 和 中性化等等，以及 Alpha的状态，还有 alpha满足 sharpe、fitness、returns 和 margin 等等，所有过滤条件对 Alpha Quant 板块所有数据图表支持查询过滤 .


> [!NOTE] [图片 OCR 识别内容]
> 首页
> 仪表板
> WorldQuant
> Alpha Quant
> Q 搜索
> CtrItk
> 十 `
> |
> 编辑
> 导出
> 分享
> AlphalD
> 输入数值
> TYPE @
> AIl
> GENIUS季度 @
> AlI
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY @
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AI
> STATUS @
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 25-02-15
> 2025-03-11
> 2025-04-04
> 2025-04-28
> 2025-05-22
> 2025-06-15
> 2025-07-09
> 2025-08-02
> 2025-08-26
> 2025-09-19
> 2025-10-13
> 2025-11-06
> 2025-11-30
> 2025-12-24
> Submitted Alphas (每日提交和累计总和)
> 800
> 700
> 600
> 500
> 400
> 300
> 200
> 100
> 02/14
> 03/01
> 03/16
> 03/31
> 04/15
> 04/30
> 05/15
> 05/30
> 06/14
> 06/29
> 07/14
> 07/29
> 08/13
> 08/28
> 09/12
> 09/27
> 10/12
> 10/27
> 11/11
> 11/26
> 12/11
> 12/26
> 每曰提交数
> 暴计总和
> 已提交全部alpha(包括sa)
> id 5
> type ?
> author
> instrument_type ?
> region ?
> universe 5
> delay ?
> decay
> neutralization
> truncat
> OmWI2gQk
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
> TOP5O0
> 18
> MARKET
> OmWlJNmG
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> ILLIQUID_MINVOLIM
> STATISTICAL
> ONK3wVq
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> INDUSTRY
> OVaRQV8
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> STATISTICAL
> OXNXEI2
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> SUBINDUSTRY
> OY32dmq
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> 100
> SUBINDUSTRY
> 0Ymgll2
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> SUBINDUSTRY
> 13eKO8R
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR
> T0P2500
> 10
> SUBINDUSTRY
> 1837Vr0
> PFFIII 40
> AAI ^7072
> FOIIITV
> FUNI
> TODnnnl
> FOOIININIC
> active regular alpha
> active superalpha
> id
> region
> universe
> delay
> decay ?
> neutralizatior
> type
> author
> instrument_type
> region
> O1ZJp7r
> ASI
> MINVOLIM
> INDUSTRY
> OmWI2gQk
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
>  OJO3AgP
> GLB
> TOP3O00 
> 10
> REVERSION_AND_MC
> 2rkLkpVW
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
> OJYZYOV
> USA
> TOP3000
> SECTOR
> 3v1gVle
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR
> OL53m3p 
> EUR
> TOP2500
> SUBINDUSTR
> 58XG3NJo
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> JPN
> 0LgKQ7q
> GLB
> TOP3000
> SUBINDUSTA
> GQSZrRE
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> OUzrgk 
> USA
> TOP3O00 
> STATISTICA
> GXmeKNYp
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> Om352Irr
> USA
> ILLIQUID_MINVOLIM
> STATISTICA
> GXOKW3k5
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR


已提交的全部alpha(包括隐藏和sa)  包括（日期已经匹配了美国夏冬令时）5个图标，总体来说就是描述随着日期 Alpha 的提交量，以及已经提交的所有 Alpha 列表，还有就是分成 ra 与 sa 的两个小图表 .

其中 Submitted Alphas (同网页端) 图表就是模仿 WorldQuantBrain  [performance]([链接已屏蔽])  做的，不过比平台多了一些查询功能 (图表太多，下面就不展示过滤功能了)，平台只显示了整体每一天总的提交量，无法区分ra 与 sa分别交了多少， 交的是哪个Region的，Grafana支持 Type 与 Region 等过滤查询 .


> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE
> SUDer
> GENIUS季度
> All
> REGION 0
> AII
> UNIVERSE
> AII
> DELAY
> AlI X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AII X
> STATUS
> AII
> SHARPE 0
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN 0
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 0.4
> 0.2
> '025-07-02
> 2025-07-15
> 2025-07-28
> 2025-08-10
> 2025-08-23
> 2025-09-05
> 2025-09-18
> 2025-10-01
> 2025-10-14
> 2025-10-27
> 2025-11-09
> 2025-11-22
> 2025-12-05
> 2025-12-18



> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> All
> REGION
> HKG
> UNIVERSE
> AlI X
> DELAY 0
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE
> AII X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 2.5
> 0.5
> 2025-10-13
> 2025-10-17
> 2025-10-21
> 2025-10-25
> 2025-10-29
> 2025-11-02
> 2025-11-06
> 2025-11-10
> 2025-11-14
> 2025-11-18
> 2025-11-22
> 2025-11-26
> 2025-11-30
> 2025-12


[图片 (图片已丢失)]

GroupBy 分组 Row 就是将 Alpha 按照 Region / Neutralization / Universe / Delay / Decay 分组，可以查看 Alpha 大体主要是交在了哪些 Region / Neutralization 等 .


> [!NOTE] [图片 OCR 识别内容]
> GroupBy 分组
> Region
> Decay (count > 5)
> 350
> 250
> 300
> 200
> 250
> 200
> 150
> 150
> 100
> 100
> 50
> 50
> USA
> EUR
> ASI
> GLB
> KOR
> JPN
> CHN
> AMR
> HKG
> TNN
> IND
> 10
> 16
> 20
> 30
> 40
> 60
> 100
> 200
> 512
> Universe
> Neutralization
> 300
> 300
> 250
> 200
> 200
> 150
> 100
> 100
> 50
> Type
> Delay
> regularalpha
> ra
> atom
> Ppa
> 无延迟
> superalpha
> 有延迟
> 128
> 256
> 512
> 1.02
> 512
> MINVOLIM
> TOP1OOO
> TOP1200
> TOP16OO
> TOP2OOOU
> TOP2500
> TOP3000
> 400
> TOPSOO
> TOP8OO
> MINVOLIM
> TOPGOO
> RAM
> Statistical
> Factors
> Factors
> Factors
> Market
> Sector
> Industry
>  Subindustry
> Factors
> None
> TOPC
> Fast
> Fast 
> Crowding
> Slow
> ILLIQUID_
> SIOW


从上面图表中，我能够很清楚的知道，主要交的 Alpaha 在 USA / TOP3000 / Subindustry / decay = 4，这个也正是符合最开始做 WorldQuant 时，国区老师们交我们 setting 的参数 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Ts_Mean 时序均值
> 日度因子指标均值
> 140%
> 400 %oo
> 120%
> 100%
> 300 %00
> 80%
> 200 %oo
> 60%
> 40%
> 100 %oo
> 20%
> 0%
> 9o00
> 02/14
> 03/13
> 04/07
> 05/02
> 05/27
> 06/21
> 07117
> 08/12
> 9/06
> 10/01
> 10/26
> 11/20
> 12/15
> sharpe
> fitness
> turnoVer
> drawdown
> 「eturns
> margin
> 月度因子指标均值
> Name
> Max
> Mean
> 25%
> 50 %00
> sharpe
> 2.15
> 1.72
> fitness
> 1.82
> 1.50
> 20%
> 50 %oo
> turnoVer
> 0.223
> 0.157
> 1.5
> 40 %ooo
> drawdown
> 24.7%
> 12.5%
> 159
> returns
> 20.1%
> 13.8%
> 30 %oo
> margin
> (右侧Y轴)
> 61.9 %00
> 41.4 %00
> 109
> 20 %oo
> 0.5
> 5%
> 10 %oo
> 9o00
> 2025-02
> 2025-03
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
> 2026-01
> 月度因子指标均值
> 2.2
> 25%
> GO %ooo
> 20%
> 50 %ooo
> 1.8
> 40 Vooo
> 16
> 15 %
> 30 %oo
> 10%
> 20 %oo
> 02/14
> 03/01
> 03/16
> 03/31
> 04/15
> 04/30
> 05/15
> 05/30
> 06/14
> 06/29
> 07/14
> 07/29
> 08/13
> 08/28
> 09/12
> 09/27
> 10/12
> 10/27
> 11/11
> 11/26
> 12111
> 12/26
> sharpe
> fitness
> turnoVer
> drawdown
> 「eturns
> margin
> 季度因子指标均值
> 50 %00
> Name
> Max
> Mean
> 20%
> 1.75
> sharpe
> 1.86
> 1.68
> 50 %oo
> 1.5
> ftness
> 1.70
> 1.48
> 159
> tUrnOVeT
> 20.6%
> 15.9%
> 1.25
> 40 %oo
> drawdown
> 16.4%
> 12.9%
> 30 %oo
> 「etUrns
> 16.1%
> 14.0%
> 109
> 0.75
> margin
> (右侧Y轴)
> 57.9 %oo
> 40.6 %00
> 20 %0o
> 0.5
> 59
> 10 %0o
> 0.25
> 9000
> 2025-01
> 2025-02
> 2025-03
> 2025-04
> 2026-01
> 年度因子指标均值
> 1.75
> Name
> Max
> Mean
> 15%
> 35 %oo
> Sharpe
> 1.71
> 1.55
> 1.5
> 30 %oo
> fitness
> 1.47
> 1.37
> 12.5%
> 1.25
> tUTIOVeT
> 15.7%
> 14.4%
> 25 %00
> 10%
> drawdown
> 16.4%
> 14.8%
> 20 %oo
> 「EtUrns
> 13.5%
> 13.4%
> 7.5%
> 0.75
> IIIUIIIL
> 15 %00
> margin
> (右侧Y轴)
> 38.0 %oo
> 33.5 %00
> 5%
> 0.5
> 10 %0
> 2.5%
> 0.25
> 5 %ooa
> 0%
> Vooo
> 2025年
> 2026年


Ts_Mean 时序均值 Row 记录了 Alpha 主要指标的均值，包括 sharpe、fitness、turnover 和 margin， 以此来分析 vf 可能和哪些数据有关，或者与哪些数据的组合有关 (这块是我想要做的)，你想要单独比较某列数据，你就
 
> [!NOTE] [图片 OCR 识别内容]
> 月度因子指标均值
> 51.9 93
> Name
> Max
> Mean
> 50 %0o
> sharpe
> 2.15
> 1.72
> 55.2 %
> 52.1
> fitness
> 1.82
> 1.50
> 48.2 %ooo
> 50 %000
> 45.7 %oco
> tUrnoVer
> 0.223
> 0.157
> 40 %ooo
> grawdown
> 24.7%
> 12.5%
> 35.9 %
> 35.8 %
> returns
> 20.1%
> 13.8%
> 29.1 %ooo
> 30 %oo
> 26.7 Socs
> margin
> (右侧Y轴)
> 61.9 %oo
> 41.4 %0
> 22.0 %co
> 22.2 %ooo
> 20 %0o
> 10 %ooo
> 9o00
> 2025-02
> 2025-03
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
> 2026-01


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 潜在可能影响情况
> 季度型滑动窗口因子指标均值
> 5O %ooo
> Name
> Max
> Mean
> 17.5%
> 1.75
> sharpe
> 1.86
> 1.72
> 50 %oo
> 15%
> 1.5
> fitness
> 1.74
> 1.52
> turnoVer
> 18.1%
> 16.0%
> 12.5%
> 1.25
> 40 %ooo
> drawdown
> 16.5%
> 12.7%
> 10%
> 30 %oo
> returns
> 16.8%
> 14.4%
> 7.5%
> 0.75
> margln
> (右侧〈轴〉
> 57.3 %00
> 44.2 %0
> 20 %oo
> 5%
> 0.5
> 10 %oo
> 2.5%
> 0.25
> 0oo
> %oo
> 2025-020304
> 2025-030405
> 2025-040506
> 2025-050607
> 2025-060708
> 2025-070809
> 2025-080910
> 2025-091011
> 2025-101112
> 普通
> 有条件
> 正式顾问指标均值
> 209
> 000
> Name
> Max
> Mean
> G00
> 1.75
> 17.59
> alpha因子数量
> 588
> 263
> 50 %oo
> 500
> sharpe
> 1.82
> 1.76
> 1.5
> 15%
> fitness
> 1.67
> 1.58
> 40 %oo
> 1.25 400
> 12.590
> turnOVeT
> (右侧Y轴)
> 18.6%
> 16.5%
> 10%
> 30 %oo
> drawdown
> 13.8%
> 11.9%
> 300
> returns
> 15.9%
> 14.8%
> 0.75
> 7.5%
> 20
> 200
> margin
> (右侧Y轴)
> 57.1 %oo
> 47.7 %00
> 0.5
> 5%
> sharpe_std
> 0.944
> 0.585
> 100
> 10 %00
> 0.25
> 2.59
> returns_std
> 11.1%
> 9.61%
> 0%
> 9000
> 通顾问
> 有条件顾问
> 正式顾问
> 正式研究顾问前后指标均值
> Name
> Max
> Mean
> 1.75
> G00
> 15%
> 50 %0
> alpha因子数量
> 588
> 395
> 1.5
> 500
> sharpe
> 1.78
> 1.73
> 12.5%
> 7.25
> 40 %ooo
> ftness
> 1.66
> 1.53
> 400
> 109
> tUrnOVeT
> (右则Y轴)
> 16.5%
> 15.9%
> 30 %0
> drawdown
> 13.8%
> 12.5%
> 300
> 7.5%
> 0.75
> returns
> 15.8%
> 14.3%
> 20 %oo
> 200
> 59
> margin
> (右侧Y轴)
> 54.9 %0o
> 43.5 %00
> 05
> 0.25
> 100
> 2.5%
> 10 %0
> 00o
> Vooo
> 成为顾问前
> 成为顾问后


Value Factor 潜在可能影响情况 Row 记录了 vf 可能会被什么数据影响，以及 vf 是按照 季度型滑动，所以我记录了 2025-040506， 2025-070809 这样的均值数据 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Osmosis Competition 2025 All Alpha
> id 9
> regular_code ?
> osmosis_points ?
> region ?
> universe ?
> neutralization
> OXNXEI2
> if_else(pvl3_reve
> al >=0,1,21
> if_e
> 2000
> USA
> TOP3000
> SUBINDUSTRY
> QNRTLqQ
> std_dev(mdl77
> tOr_as
> 2000
> USA
> TOP3000
> SUBINDUSTRY
> 1YQIAjvz
> jump_decay(pv87_ivy_opr
> Ivcallmputs3, 60, sensiti
> 0.1)
> 2000
> USA
> TOP3O00
> REVERSION_AND_MC
> 2AmOQYZ
> ts_sum(lanl4_
> gric_low)
> 31l4_[OLa
> 951
> group
> lensify(close 2000
> USA
> TOP3000
> SUBINDUSTRY
> REORbA1
> Win
> backfill(implied_volatility_call 180
> 10,2), std
> 9),C2000
> USA
> TOP3O00
> SUBINDUSTRY
> SEGaPpk
> grOUP
> rallze
> tincome_
> T,densify 2000
> USA
> TOP3000
> SUBINDUSTRY
> SGZrgIN
> sentiment
> delay
> 21,20); Vhat
> ression(volume sentimE 2000
> USA
> TOP3O00
> SUBINDUSTRY
> GGKISVE
> ts_sumlpowerlpower(zsco
> delay(powe
> DS「
> 0000
> USA
> TOP3000
> SECTOR
> 7LVLKKZ
> ts_sum((anl4_gric_hi
> 9014
> anl4_tot
> Iow  78)
> 000
> USA
> TOP3000
> SUBINDUSTRY
> group by Region
> group_by Universe
> alpha_count
> 175K
> alpha_count
> 100K
> total_points
> total_
> points
> 150K
> avg_points
> avg_points
> 80K
> 125K
> 60 K
> 1O0K
> 75 K
> 40K
> 50K
> 20K
> 25K
> USA
> GLB
> EUR
> ASI
> MINVOLIM
> TOP3000
> TOP2500
> ILLIQUID_MINVOLIN
> group_by Neutralization
> group_by Decay
> 150k
> alpha
> CoUnt
> 120K
> gecay
> total_points
> alpha_count
> 125K
> 100K
> avg_points
> total_points
> 100K
> avg_points
> 80K
> 75 K
> 60 k
> 50K
> 40k
> 25k
> 20k
> 2K 2K 2K 2K 2K 2K 2K 2K 2K
> 2K10K10K 2K 2K 2K 2K 2K 2K 2K 2K
> gric
> FAST
> INDUSTRY
> FAST
> SUBINDUSTRY
> MARKET
> SECTOR
> MOMENTUM
> CROWDING
> STATISTICAL
> SLOW_AND
> REVERSION_AND


Osmosis Competition 2025 Row 记录了  Osmosis 比赛 被选中的 Alpha，以及 Alpha 被分配了多少分，以及按照某些字段分组图标.
 
> [!NOTE] [图片 OCR 识别内容]
> https:/Iplatform worldquantbrain.com/competition/0C2025
> 出 AI 众
> { |众
> WORL
> 鬯"
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> { Competitions (5)
> Community
> @ $ & 三
> This competition starts on December 15th, 2025 at 1:00:00 PM CST and ends on January Sth, 2026 at 12:59:59 PM CST。 
> Osmosis Competition
> Score
> Leaderboard
> Guidelines
> FAQ
> OSMOSIs
> 2025
> 2025-26
> Aggregate by:
> University
> Country
> Region
> Filter
> Rank
> User
> Total
> Combo IR
> Alphas
> Points
> Daily
> Combo IR
> Alphas
> Points
> Daily
> Combo IR
> Alphas
> Scoreas
> Rank
> USA
> Allocated
> PNL USA
> Rank
> GLB
> Allocated
> PNL GLB
> Rank
> EUR
> on Dec
> USA
> USA
> GLB
> GLB
> EUR
> 29th
> 顾问 ML47973 (Rank 100) (Me)
> 63,183
> 98,529
> 50
> 100,000
> 68,392
> 99,529
> 10
> 100,000
> 61,655
> 51,805
> DA98440
> 78,562
> 82,353
> 100,000
> 19,767
> 37,562
> 100,000
> 34,785
> 85,740
> 儿71699
> 77,823
> 97,059
> 100,000
> -14,867
> 93,321
> 100,000
> -31,197
> 76,895
> X42289
> 76,265
> 64,706
> 100,000
> 29,421
> 97,959
> 100,000
> 10,707
> 78,339
> AM112075
> 75,547
> 93,934
> 26
> 100,000
> 48,545
> 89,425
> 100,000
> -38,506
> 74,368
> Y815978
> 74,474
> 99,265
> 25
> 100,000
> -15,368
> 53,432
> 100,000
> -4,331
> 99,278
> 0X52484
> 73,278
> 88,971
> 20
> 100,000
> 17,561
> 82,746
> 20
> 100,000
> 8,101
> 72,744
> User


USA 分配了50个 Alpha, GLB分配了10个 Alpha，都是均分 .  从结果上来看，USA 和 GLB 的 Combo IR Rank 都还不错 .

## **四、**  **智源勘探 (Intellisource Prospecting)**

Grafana - WorldQuant 项目我还想要补全，但是还未完成的 :

1. 为了方便同时查看所有 Alpha 的 PnL 数据，可以使用 Grafana 的 JSON API 插件，通过登录 WorldQuant Brain 账号直接接入数据 . 只要在插件中配置好 PnL 接口（例如： `[链接已屏蔽] ），并利用  `alpha_id`  变量，理论上就能在同一个面板中动态展示不同 Alpha 的 PnL . 但我对 API 返回的数据格式不太熟悉，不确定在 Grafana 中具体应该如何配置查询和字段映射 . 如果有类似的经验或成功配置过，欢迎在评论区分享，非常感谢！

2. Value_Factor (vf) 这个数据，大家都比较关心，在排除他人影响的情况下，想要通过自己的 sharpe、fitness、 returns 和 margin 等数据构建某种线性 | 非线性函数，拟合自己的 vf，得到一个大致接近有预测自己下一次的 函数 .

3. 补全 Alpha Quant 板块的 理论与可投资术语 Row，使用 轻量级标记语言 Markdown 丰富，可以写记录 一些公式 比如：sharpeRatio = (Rp - Rf) / σp ，Equal Weight PnL、Combo PnL、Investability Constrained PnL 和 Risk Neutralized PnL曲线图表，记录它们之间的关系，比如，当 Max Trade = OFF 时，Combo PnL 与 Investability Constrained PnL 走势背驰意味着什么 等等，方便大家记录和学习 .

## **五、**  **Grafana Visualization JSON 共享**

当下载好 Grafana 后， 接上篇下载数据进数据库并导入评论区 Grafana JSON 数据，便可以多维度查看和分析自己的 Alpha 啦 .

---

### 帖子 #7: 4、 **减少生产相关性**
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

### 帖子 #8: 4、 **减少生产相关性**
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

### 帖子 #9: Research Paper: Overvalued Equity and Financing DecisionsPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md
- **讨论数**: 0

**Abstract:**

We test whether and how equity overvaluation affects corporate financing decisions using an ex ante misvaluation measure that filters firm scale and growth prospects from market price. We find that equity issuance and total financing increase with equity overvaluation; but only among overvalued stocks; and that equity issuance is more sensitive than debt issuance to misvaluation. Consistent with managers catering to maintain overvaluation and with investment scale economy effects, the sensitivity of equity issuance and total financing to misvaluation is stronger among firms with potential growth opportunities (low book-to-market, high R&D, or small size) and high share turnover.

Key ideas:

- Page 3 paragraph 3
- Page 42 paragraph 4
- Page 43 paragraph 2

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

debt issuance

fnd23_debt_issuance

[**Fundamental23**]([链接已屏蔽])

higher score indicates higher levels of equity

issuance

mdl23_bk_net_equity_financ

[**Model23**]([链接已屏蔽])

Author: Ming Dong, David A. Hirshleifer, Siew Hong Teoh

Year : 2012

Link:  [[链接已屏蔽])

---

### 帖子 #10: WorldQuant Brain Lab 复制粘贴限制：自动化代码输入方案
- **主帖链接**: https://support.worldquantbrain.com[L2] WorldQuant Brain Lab 复制粘贴限制自动化代码输入方案_32983618750999.md
- **讨论数**: 2

最近，WorldQuant 推出了 Lab 实验室环境，但其采用远程桌面方式且禁用了复制粘贴功能，这给习惯使用 AI 辅助编程的开发者带来了巨大的效率挑战。本文将介绍一个基于 Python 的自动化解决方案，帮助各位顾问重获高效的编程体验。

## 问题背景

在 AI 辅助编程时代，开发者习惯了：

1. 使用 AI 生成代码
2. 复制代码到开发环境
3. 调试和优化

但在 WorldQuant Brain Lab 中，第二步被阻断了。为了解决这个问题，我们可以利用 Python 的自动化能力，模拟人工键盘输入，实现代码的自动输入。

## 技术方案

### 1. 环境准备

首先需要安装必要的 Python 包：

```
pip install pyautogui
```

### 2. 核心代码实现

创建  `auto_input.py`  文件：

```
import time
import pyautogui
import sys
import os

class RemoteCodeInput:
    def __init__(self, wait_time=10, char_delay=0.05, line_delay=0.5):
        """
        初始化远程代码输入工具

        Args:
            wait_time: 等待切换窗口的时间（秒）
            char_delay: 字符间延迟时间（秒）
            line_delay: 行间延迟时间（秒）
        """
        self.wait_time = wait_time
        self.char_delay = char_delay
        self.line_delay = line_delay

        # 设置pyautogui的安全设置
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = self.char_delay

    def read_code_file(self, file_path: str) -> str:
        """读取代码文件内容"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"找不到文件: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def type_with_delay(self, text: str):
        """带延迟地输入文本"""
        for char in text:
            pyautogui.write(char)
            time.sleep(self.char_delay)

    def handle_indentation(self, line: str) -> str:
        """处理缩进，将tab转换为空格"""
        return line.replace('\t', '    ')

    def type_code(self, code: str):
        """模拟键盘输入代码"""
        print(f"请在 {self.wait_time} 秒内切换到目标窗口...")
        time.sleep(self.wait_time)

        lines = code.split('\n')
        total_lines = len(lines)

        for i, line in enumerate(lines, 1):
            line = self.handle_indentation(line)

            if not line.strip():
                pyautogui.press('enter')
                time.sleep(self.line_delay)
                continue

            self.type_with_delay(line)
            pyautogui.press('enter')
            time.sleep(self.line_delay)

            if i % 5 == 0:
                print(f"进度: {i}/{total_lines} 行 ({(i/total_lines*100):.1f}%)")

def main():
    if len(sys.argv) < 2:
        print("使用方法: python auto_input.py <代码文件路径> [字符延迟(秒)] [行延迟(秒)]")
        return

    code_file = sys.argv[1]
    char_delay = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02
    line_delay = float(sys.argv[3]) if len(sys.argv) > 3 else 0.02

    input_bot = RemoteCodeInput(char_delay=char_delay, line_delay=line_delay)

    try:
        code = input_bot.read_code_file(code_file)

        print("即将开始输入以下代码:")
        print("="*50)
        print(code)
        print("="*50)
        print(f"当前设置:")
        print(f"- 字符延迟: {char_delay}秒")
        print(f"- 行延迟: {line_delay}秒")
        confirm = input("是否继续? (y/n): ")

        if confirm.lower() != 'y':
            print("已取消操作")
            return

        input_bot.type_code(code)
        print("\n代码输入完成!")

    except Exception as e:
        print(f"发生错误: {str(e)}")

    except KeyboardInterrupt:
        print("\n用户中断操作")

if __name__ == "__main__":
    main()
```

## 使用方法

### 1. 基本用法

```
python auto_input.py <代码文件路径> [字符延迟] [行延迟]
```

例如：

```
python auto_input.py my_code.py 0.02 0.02
```

### 2. 推荐的工作流程

1. 在本地编写代码并保存为文件
2. 打开 WorldQuant Brain Lab 远程桌面
3. 在远程桌面中打开一个文本编辑器
4. 运行自动输入工具
5. 在等待时间内切换到远程桌面的文本编辑器
6. 等待代码自动输入完成
7. 将代码从文本编辑器复制到 Jupyter Notebook

## 工具特点

1. **安全性**

1. **灵活性**

1. **用户友好**

## 使用建议

1. **速度调整**

1. **错误处理**

1. **最佳实践**

## 总结

这个自动化工具有效解决了 WorldQuant Brain Lab 中的代码输入问题，让开发者能够继续保持高效的 AI 辅助开发工作流。虽然不是完美的解决方案，但在当前条件下，它提供了一个实用的权衡方案，既保证了平台的安全性要求，又提高了开发效率。

希望这个工具能帮助更多的 WorldQuant Brain 顾问提升开发效率！

---

### 帖子 #11: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
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

### 帖子 #12: 【alpha灵感】A股恐慌度因子在美股的应用
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

### 帖子 #13: 计算与给定字段相同数据集的使用数据字段的相似度scs = get_data_field_similar('anll1_2_2pme', 'USA', 1, 'T0P3000', same_data_set=True)print(scs)计算两个字段之间的相似度brain=Brain(region='USA', delay=1, universe='T0P3000')print(calc_data_field_mean_corr(brain,'anl11_2_1pme', 'anl11_2_2pme'))
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Brain Labs】实现在Brain Labs中计算数据字段的相关性修改版v2代码优化_33638658994711.md
- **讨论数**: 8

通过在Brain Labs中计算数据字段之间的相关性，可找到与我们已经提交过的数据字段类似的数据字段，进行替换来找到新的Alpha。

以下是实现在Brain Labs中计算字段相似性的代码，希望对大佬们有所帮助。

```
from brain import Brainfrom brain.errors import UnexpectedStatusfrom typing import Optionalimport numpy as npimport pandas as pdimport timeimport osdef calc_mean_corr(df1, df2) -> float:    timeS = time.time()    # 行对齐和列对齐（按 index 和 columns）    df1, df2 = df1.align(df2, join='inner', axis=0)    df1, df2 = df1.align(df2, join='inner', axis=1)    corrs = []    for col in df1.columns:        s1 = df1[col]        s2 = df2[col]        # 对齐非 NaN 的值        valid = s1.notna() & s2.notna()        s1_valid = s1[valid]        s2_valid = s2[valid]        if len(s1_valid) < 2 or s1_valid.std() == 0 or s2_valid.std() == 0:            continue        corr = s1_valid.corr(s2_valid)        if not np.isnan(corr):            corrs.append(corr)    print(f"calc self corr cost {time.time() - timeS} seconds")    if corrs:        return float(np.mean(corrs))    else:        return np.nandef save_df(region: str, delay: int, universe: str, data_field: str, df: pd.DataFrame):    dir_path = os.path.abspath('.')    file_path = os.path.join(dir_path, "dataframe", region, str(delay), universe, f"{data_field}.csv")    os.makedirs(os.path.dirname(file_path), exist_ok=True)    df.to_csv(file_path)    print(f"saved to {file_path}")def get_df(region: str, delay: int, universe: str, data_field: str) -> Optional[pd.DataFrame]:    dir_path = os.path.abspath('.')    file_path = os.path.join(dir_path, "dataframe", region, str(delay), universe, f"{data_field}.csv")    if os.path.exists(file_path):        return pd.read_csv(file_path, index_col=0, parse_dates=True)    return Nonedef filter_by_dates(df: pd.DataFrame, dates: list):    mask = pd.Series(True, index=df.index)    for op, date_str in dates:        date = pd.to_datetime(date_str)        if op == '>':            mask &= df.index > date        elif op == '>=':            mask &= df.index >= date        elif op == '<':            mask &= df.index < date        elif op == '<=':            mask &= df.index <= date        elif op == '==':            mask &= df.index == date        elif op == '!=':            mask &= df.index != date        else:            raise ValueError(f"Unsupported operator: {op}")    return df[mask]def get_df_if_exist(brain: Brain, data_field, dates: Optional[list] = None):    df = get_df(str(brain.region), brain.delay, str(brain.universe), data_field.id)    if df is not None:        if dates:            return filter_by_dates(df, dates)        return df    while True:        try:            df = brain.get_data_frame(data_field)        except UnexpectedStatus:            continue        except Exception as e:            print(e)            continue        else:            break    save_df(str(brain.region), brain.delay, str(brain.universe), data_field.id, df)    if dates:        return filter_by_dates(df, dates)    return dfdef calc_data_field_mean_corr(brain: Brain, data_field1: str, data_field2: str):    data_field1 = brain.get_data_field(data_field1)    data_field2 = brain.get_data_field(data_field2)    df1 = get_df_if_exist(brain, data_field1)    df2 = get_df_if_exist(brain, data_field2)    return calc_mean_corr(df1, df2)def get_data_field_similar(datafield: str, region: str, delay: int, universe: str, same_data_set: bool = True, dates: Optional[list] = None, target_type: list = ["MATRIX"]):    brain = Brain(region=region, delay=delay, universe=universe)    datafield = brain.get_data_field(datafield)    dataframe = get_df_if_exist(brain, datafield, dates=dates)    now_dataset = datafield.dataset.id    datasets = brain.get_data_sets()    datasets = datasets.results    datasetsId = [dataset.id for dataset in datasets]    if same_data_set:        datasetsId = [now_dataset]    dataCorr = []    for dataset in datasetsId:        datafields = brain.get_data_fields(data_set=dataset)        datafieldsId = [datafield.id for datafield in datafields.results if datafield.type in target_type]        for datafield in datafieldsId:            datafield = brain.get_data_field(datafield)            dataframeN = get_df_if_exist(brain, datafield, dates=dates)            selfcorr = calc_mean_corr(dataframe, dataframeN)            dataCorr.append({                'id': datafield,                'sc': selfcorr,            })    return pd.DataFrame(dataCorr).sort_values(by='sc', ascending=False)
```

使用方法如下:

```
# 计算与给定字段相同数据集的使用数据字段的相似度scs = get_data_field_similar('anll1_2_2pme', 'USA', 1, 'T0P3000', same_data_set=True)print(scs)# 计算两个字段之间的相似度brain=Brain(region='USA', delay=1, universe='T0P3000')print(calc_data_field_mean_corr(brain,'anl11_2_1pme', 'anl11_2_2pme'))
```

由于计算时发现不设置时间范围计算全量数据一次需要接近30s, 设置为大于2021年的数据后，时间为13秒左右，可以根据需要自行修改，默认只计算同数据集字段，same_data_set设置为False，将计算当前region-delay-universe的所有数据字段与给的数据字段的相似度。

相似度计算函数使用DataFrame自带的corr函数，可以根据需要自行修改calc_mean_corr函数来满足自己的要求。

使用代码时可以单独开启一个jupyter文件然后运行，实测就算关掉Brain Labs界面计算还会继续，也就是可以在晚上开始计算几个想计算的数据字段相似度，第二天就基本能看到结果了。

以下为计算结果:

由于计算时间太长，所有只选取了当前数据集的10个数据字段。可以发现使用全量数据计算anl11_2_1pme与anl11_2_pme的相似度为0.57，而大于2021年数据计算出为0.49还是有一定的误差。


> [!NOTE] [图片 OCR 识别内容]
> SCS
> data
> field_similar("anlll
> 2_2pme
> USA
> 1,
> T0P3000
> print (sCs
> brain
> Brain (region= 'USA
> delay=l;
> universe=' T0P3000
> print (calc_data_field_mean_corr(brain;
> anlll
> 2_Ipme
> anll1
> 2_Zpme' ) )
> anlll
> 2_Zpme
> analystll
> Calc
> Self
> COTI
> COSt
> 12.6117556095123295
> Calc Self
> COrr
> COSt
> 12.6700372695922855
> calc self
> COTF
> COst
> 12.815838336944585
> Calc self
> COTI
> COst
> 12.7351031303405765
> calc self
> COTI
> COSt
> 14.0531449317932135
> Calc Self
> COrr
> COSt
> 14.2117724418640145
> calc self
> COTF
> COst
> 13.9583809375762945
> Calc Self
> COTI
> COst
> 14.2266893386840825
> calc self
> COTI
> COSt
> 14.2195904254913335
> Calc Self
> COTI
> COSt
> 13.9569535255432135
> id
> SC
> anll1
> 2_2pme
> 1.000000
> anlll
> 2_Ipme
> 0.491526
> anlll
> 2 2tic
> 0.463154
> anllI
> 22
> 0.330435
> anlll
> 2_39
> 0.277872
> anlIl
> 2_29
> 0.263194
> anlll 2_19
> 0.187412
> anllI
> 2_3e
> 0.130620
> anlll
> 2 le
> 0.114858
> anlll 2 Itic
> 0.109822
> Calc Self
> COrr
> COSt
> 15.1421022415161135
> 0.5706013982446931
> get


可以发现anl11_2_2pme与anl11_2_pme有0.82的相似度，还是很高了，但是这是我随便选的，没有使用过。


> [!NOTE] [图片 OCR 识别内容]
> 日
> +
> &
> 口
> 凹
> Code
> Notebook C
> Cluster
> Python 3 (ipykernel)
> 11/T0P3000
> A/I/T0P3000/an111
> Company
> name
> CSV
> Name
> Modified
> Calc
> Self
> COTI
> COSt
> 9.3469376564025885
> anl11_2_le.csV
> 9hago
> SaVe
> to
> /mnt/custom-file-systems /efs /fs -0a9c53e05417598fa_fsap-Oeb4elef5d316f1b8 /dataframe /US
> anlll_Z_19.csV
> 9ha90
> A/I/TOP3OOO/anlIlcreptcesgerle .CsV
> Calc Self corr
> COSt
> 10.2125208377838135
> anl11_2_Ipme.csV
> 9hago
> Save
> t0
> /mnt/custom-file-systems /efs /fs - 0a9C53e05417598fa
> Oeb4elef5d316f1b8 /dataframe /US
> 田 anlll_2_IticcsV
> 9ha90
> A/I/TOP3OOO/anlll_creptcesgerlg
> CSV
> calc
> Self Corr
> COSt
> 10.2548635005950935
> anl11_22e.CsV
> 9hago
> Save
> to
> /mnt/custom-file-systems /efs /fs - 0a9C53205417598fa
> Oeb4elef5d316f1b8 /dataframe/US
> anlll_2_2g.CSV
> 9ha90
> A/I/TOP3OOO/anlll_creptcesgerlpme
> CSV
> Calc
> Self
> COTI
> COSt
> 10.6469922065734865
> anlll_22pme csV
> 9hago
> Save
> to
> /mnt/custom-file-systems /efs /fs - 0a9c53205417598fa_fsap-Oeb4elefsd316f1b8 /dataframe /Us
> 田 anlll_2_Ztic CsV
> 9ha90
> A/I/TOP3OOO/anlII_creptcesgerltic .csV
> a0l11_2_3e.CSV
> 9hago
> Calc
> Self
> COTI
> COSt
> 10.2657704353332525
> SaVe
> to /mnt/custom-file-systems /efs /fs- 0a9C53e05417598fa_fsap-Oeb4elefsd316f1b8 /dataframe
> anl11_2_39.CsV
> 9ha90
> A/I/TOP3OOO/anlIlcreptcesgerze .CsV
> anlll_23pme.csV
> 8ha90
> CalC Self corr
> COSt
> 10.3563883304595955
> id
> SC
> 田 anlll_2_3ticcsV
> 8ha90
> anlll_2_2pme
> 1.000000
> anl11_2_e.CsV
> 8ha90
> 15
> anlll
> 2_pme
> 0.827962
> anl11_2_9.CsV
> 10
> anlll 2 3pme
> 0.618368
> anlll 2
> Ipme
> 0.491526
> anlll_2gse.CSV
> 8ha90
> anlIl 2 2tic
> 0.463154
> 田 anlll_2_pme.csv
> 8ha90
> anlll
> 2_95e
> 0.439470
> anlll_2_region.csv
> 8ha90
> :
> anlll
> 22e
> 0 .330435
> anlll_2_tic
> 0.302962
> anlll_2_ticcsV
> 8ha90
> anlll
> 0.294157
> anlll_cit_totalcor。
> 8hag0
> anlll 2_39
> 0.277872
> 47
> anlll_Creptcesgerlpme
> 0.274874
> anlll_cit_totalcor。。
> anlll 2_29
> 0.263194
> 0 )10155
> fsap-
> fsap-
> /US
> Sha9o
> Sha9o


修正:

根据weijie老师建议增加了数据的缓存，只保留了MATRIX数据，可以根据需要修改。

经过测试修改为缓存数据后，数据的计算时间变成了2s，不知道是不是因为晚上的时候服务器快一点，所以直接将dates默认参数改为None，可以根据需要修改。

改进建议:

1. 获取的数据字段一次的最大数目为10000，不知道是否存在超过10000个数据字段的数据集，如果存在可能返回的数据字段不全。

2. 获取数据字段时可以根据用户alpha数目或者用户数排序，或者根据covrage过滤等，以获得更优的数据字段。

3. 可以保存已经计算过的相似度到一个文件中，避免重复计算。

---

### 帖子 #14: 【YZ工程优化系列】YZ72256-使用API自动完成submit
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

### 帖子 #15: 【哥布林】杂论1：关于setting配置和ops选择使用方面的个人经验
- **主帖链接**: https://support.worldquantbrain.com[L2] 【哥布林】杂论1关于setting配置和ops选择使用方面的个人经验_35698887416983.md
- **讨论数**: 2

本帖整理了一些之前遇到过的问题和个人经验，如有帮助，不胜感激

1.Q：prod corr有办法通过换操作符降低吗？

A：可以通过尝试替换相似运算符来降低生产相关性。例如对于fnd类数据，ts_scale, ts_rank, ts_quantile(包含所有的三种driver), ts_zscore这几个运算符在IS指标上可近似视为等效，但在prod corr的表现上却不尽相同，一般会出现0.05-0.15之间的浮动

2.Q：如何选择universe？

A：默认以当前region最大的universe作为起跑线，当发现sub-universe呈现更高的sharpe时，再切换到更高层的universe，既能在较大程度上保持原universe的IS指标的同时，又能获得更低的prod corr。

3.Q：如何选择truncation？

A：默认使用0.1，以获得最大的IS指标。遭遇weight concentration问题时，直接降低到0.01，如果发现IS指标提升，且weight concentration得到缓解，则还可以尝试"蚊子腿策略"，再稀释到0.001。其余区间值，只在解决weight问题时微调使用

4.Q：如何选择risk neut？

A：使用RAM, Statical, Crowding作为默认neut选项。

如果这三种risk neut的IS指标对比，其中任意一种neut显示出比另外两种neut好很多的情况，则可尝试Fast；

如果Fast的IS指标好于或接近前三种neut，可再继续尝试Slow；

当Fast和Slow的指标相差不多时，才尝试Fast+Slow；

如果三种neut显示结果相近，则选择IS指标最佳的即可，无需再尝试Fast(除非为了降低prod corr愿意大幅牺牲指标)

5.一些运算符使用经验？

- 当使用ts_std_dev能体现出接近ra的指标时，基本可以确定在ts系列运算符中，使用这个运算符必定是最优解(至少对expert及以下，非rsk类数据是符合这个规律的吧)

- 当low sub-universe， high turnover和weight concentration同时出现时，可尝试使用winsorize

- 反转信号的方法可以有很多种，例如reverse，inverse，ts_arg_max，ts_arg_min，ts_max，ts_min，rank，group_rank，做比率等

- 优先尝试关联运算符，例如ts_mean呈现不错的表现时，ts_av_diff可能会出现更优的表现

---

### 帖子 #16: 【工具优化】华子哥插件的FireFox版本经验分享
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

### 帖子 #17: 根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的_35129651186967.md
- **讨论数**: 30

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

### 帖子 #18: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **讨论数**: 1057

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #19: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #20: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #21: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 1018

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #22: print('retrying in', result.headers["retry-after"], 'seconds')
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

### 帖子 #23: 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回
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

### 帖子 #24: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
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

### 帖子 #25: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #26: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
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

### 帖子 #27: 使用[ClickHouse📕]建设你的大型数据库
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

### 帖子 #28: 华为云沃土云创计划——领取401元代金券（可免费购买Flexus服务器）
- **主帖链接**: https://support.worldquantbrain.com[L2] 华为云沃土云创计划领取401元代金券可免费购买Flexus服务器_28322890747799.md
- **讨论数**: 3

最近在寻找服务器的时候发现华为云的一个福利，分享给大家，下面是具体的步骤：

1.首先需要一个华为云账号，没有可以通过这个链接注册： [[链接已屏蔽])

2.注册账号之后加入沃土计划，通过下面的链接进入，需三种个人开发者方向即可，加入后，就可以申请一张401元的代金券，现在是100%通过，链接： [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 沃士云创计划
> 沃士云创计划是华为云开发者使能计划。面向企业。高校。个人三个方向
> 使能方向
> 企业
> 高校
> 个人
> 伎能企业基于华为云进行技术创新。对企业基于华为云服务。 工冥
> 伎能高校及科砑院所基于华为云开展计算机。软件工程
> 软件开
> 伎能开发人员学习华为云相关技术。使用华为云服务。开发平台]
> 或平台的开发提供赋能与支持。并向开发者提供产品畿力认证。为
> 发。云计算  大数捂。人工智能等相关学科的人才培养
> 字术砑究
> 干发工具
> 获取华为云开发者认证。
> 通辽认证的产品_
> 服务或解夹方案提供营销支持_
> 和科砑创新活动。
> 立加入
> 老 加入
> 学莜加入
> 了解详情
> 立加入


3. 加入之后，就可以申请代金券了，选择 学习代金券(云服务)，点击申请即可。


> [!NOTE] [图片 OCR 识别内容]
> 总笕
> 沃土云创计划-个人 V
> 开岌空间
> 权*
> 权益配颧
> 发放方式
> 操作
> 开发工兵
> 应用答垂
> 孝试诋扣券 (个人方问]
> 1张
> 黹足条件刍动岌放
> 洋悻
> $请
> 沃士云创
> 亓源生恋痄 c建-空
> 20,000元
> $请通过入工岌放
> 歙动答垂
> 讦枚益
> 开源代金券
> 60,000元任务
> $请通过刍动岌放
> 洋悻
> $请
> 非+樾芒
> 开共刳
> 学习代佥券 (云服务)
> 1张
> 满足条件自动岌放
> 由请
> 绊~
> 艾袤
> 学习代金券 (沙箱实验 }
> 黹足条件刍动岌放
> 洋情
> 由请
> 支持与分析
> 设n


4. 领券成功后，可以通过下面这个链接直达服务器购买页面，点击购买就可以根据自己的需求选择服务器： [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 区皿
> 华北-北京四
>  -上
> 华幸广州
> 中国香巷
> 呔新加坡
> 不区域!云服务产品之间内*不通;  诗就近选择靠近]业务的区域。可e少网笨时延。捉G问)簋。
> 亚-莉1坛区实
> 在"/访问+国大陆区焱窘户峁场景下。
> 可能出玑网。延近和芸包。推荐面向海外客户对跨境网绪质要求倘的业务傲用
> 镜-
> 应用宽恁
> 系统镜-
> 私有`箧
> 共享`恁
> IndoNfs SereT
> Huawel Cloud Euleros
> Centos
> Ubuntu
> Debian
> Centos StreaM
> 2016标准笱
> 32
> 22.04
> 120
> Ubuqtu是-热 HLinu行砭2
> 是-款开放源代码的矢芰软 。基FDebian Unux怍系巯。|舄用和急定均非学出色
> 井刍拥有'弭大5-寻
> 实例规格
> 2核
> 261
> 2核
> 261
> 2核
> 2C8
> 2核
> 4CiB
> 2核
> 4GiB
> 2核
> 4GiB
> 系统盂
> 40 GIB
> 系橘
> 40 GiB
> 系 盘
> 50 GiB
> 系盏
> 50 GiB
> 系充盏
> 70 GiB
> 系盘
> 80 GiB
> 烽苣带宽
> Nbps
> i_芹竞
> Ubps
> 峰宦带竞
> Mbps
> 烽葸带宽
> Mbps
> -直荒
> Ubps
> 峰值带竞
> Mbps
> G7包
> 200 GB
> 流显包
> 400 GB
> 流@包
> GO0GB
> G2
> 400 GB
> 流显包
> 1,000 GB
> 蔬髭
> 1,200 GB
> 半41.62 |
> 半55.02归
> 半75.05 斥
> 半62.25 /月
> 半107.91归
> 半139.941
> 豕笠荛用: 半36.80


5.选择好机器之后，点击立即购买，到支付页面选择代金券。我是因为已经使用过了，代金券还没用的情况下，下面会有一张401的代金券，点击选中就可以免费购买。

**
> [!NOTE] [图片 OCR 识别内容]
> 购买Flexus云务
> 以下订单中。最近的订单将于 2024/12/13 23:59:59 GMT+OB:00 后超对宅动取消
> 请及讨支付。
> 云服务订单
> 订单号
> 订单类型
> 产品奘型
> 服务提供方
> 订单金额
> 应付金额
> C52412061729UY1AN
> 新购
> 华为云Flexus云服务 Flexus
> 华;云
> +348.10
> 半348.10
> 云市场代金券
> 激活代金券
> 可用(0)
> 全[1)
> 半99.00
> L@
> 有效至2025/02/21
> 满100.00可用
> 适贮显
> 使用限制
> 洋S规则
> 支付方式  *请线上合同请款
> 您需支付: 半348.10
> 余额在线支付
> 余额支付
> 玑金佘额;
> 芈0.00
> 在线支付
> 使用等三方在筏支付半348.10
> 贡持
> 等穸科在线付方式
**

**方案：**

- 选择2核1G配置
- 首次购买12个月（约348元）
- 追加1个月续费（也可以稍微付几块钱续费2个月）
- 总计可使用13个月

关于机器配置，之前香港和新加坡有1核0.5G的机器，如果选择这个配置最多可以购买17个月，所以不着急使用云服务器的同学可以稍微等一下，后面或许还会补货。

---

### 帖子 #29: 💻如何使用天翼云主机进行云端程序挂载
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何使用天翼云主机进行云端程序挂载_25891396254231.md
- **讨论数**: 4

本文不构成任何推荐，仅是经验分享，不涉及付费内容。

**Step1:进入免费试用中心👉点击链接 [免费试用中心 - 天翼云 (ctyun.cn)]([链接已屏蔽])**

**Step2:选择“个人认证”，并选择1核4G电脑**


> [!NOTE] [图片 OCR 识别内容]
> 免费试用
> 情遘云产品免J试用
> 豉豆方展。贫完为止
> 舌动拗则>
> 在此镝入趄要搜索豹内客
> 搜窝
> 筛选条件
> 清裤选条仵
> 53通用型云主机1核16
> 53通用型云主机1核26
> 镜像服务
> 用户认证类型
> 拓』音+RnDgR53e
> 环dt3与!
> OqRSC
> TnMNDOCz-NL7们 
> 菁墙昃立用
> 955O片
> 气/(丘L
> 企业认证
> 个人认证
> 观袼
> 1716
> 观掐
> 1526
> 慎逆7
> 5#
> 40G
> s坑基
> 40G
> 公共镇瘭奂梨哿憔
> 产品_别
> 带宽
> 1005
> 带竟
> Tbps
> 计
> 个人认证
> 个 人认l
> 介(U2
> 仔
> 欤揠库
> 免费试用2个月
> 免费试用1个月
> 长期免费试用
> 己-10,004
> 己:10,001
> 网培
> 安全及笞理
> 试用辕识
> 立剧试用
> 试用簌T
> 立8试用
> 试用狨
> 丽{订购


**Step3：选择Windows2019主机。**  
> [!NOTE] [图片 OCR 识别内容]
> 53通用型云主机1核26
> 贵州1-可用区1
> 规格选择
> 1核26
> Windows 2019 DataCente
> Centos7.5 64位(406)
> Das_AHcloud_V3.0.3.2.1_ASTACK_X8G_VRAS_VS.OROI COOSPCI02_tyy_230531(406)
> .00元
> Centos7.9 64位(406)
> Debian8.6 32位(406)
> Windows 2016 DataCenter 64位中文版(406)
> 翼视捷智云版-免费20方(406)
> Centos6.8 64位(406)
> Windows 2019 DataCenter 64位中文版2022(406)


**Step4:等待开通完毕**


> [!NOTE] [图片 OCR 识别内容]
> 岙
> 空利台
> 皿用中0
> 』订革'汀讲佾
> 玎革号:20250825142034021007
> 汀荤=; ;J
> i)  2025-0825142037
> 产新o  202492514.20:3
> T+19
> GTTo
> 开遁
> HEI
> 己下4
> 拜遁中
> 已尧氐
> he
> ITT{
> J
> &1
> JUI
> 1!T-
> 产8
> 玎蜚
> [
> CIo
> 52
> JLUILASSUITLOIA|
> TLCO 兀
> 己苎


**Step5:等待开通完毕后，进入控制台更改密码，并按照指示进行登陆。**


> [!NOTE] [图片 OCR 识别内容]
> 弹性云主机
> 可以21935云主玑。
> 也HTGAFUIDI Sg3GBRT
> 7rNT
> Ut性云士u
> 如塞云主
> L亚5 +丘;
> ]6
> 1竹-
> 0u
> 斥有坛行垃$
> NI
> OH
> LRN憧
> IPbf
> HqIt
> CCUEIhIAYeIUIU
> TCPUs|2G
> 4131256731
> 0459
> 可眍1
> 失
> UN
> 45493231-42224197
> TJo
> 192661IT7
> 54301引胡
> 刨柜?
> 亓玑
> [苎
> 蛮-1膏
> 讽汀
> [*切
> 呙f@


**Step6:进入远程电脑（主机）后，下载Microsoft Edge浏览器，并下载VS Code.  [vscode+python+jupyter环境搭建_哔哩哔哩_bilibili]([链接已屏蔽])**

提示：也可以在本地电脑下载好vs code后把安装包复制到云电脑上

---

### 帖子 #30: 💻如何免费领取阿里无影云电脑使用
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何免费领取阿里无影云电脑使用_25889938244375.md
- **讨论数**: 3

为了让大家在大数据时代顺利上云，提供如下教程供大家参考，不构成任何商业推荐。

1，下载 [阿里无影云电脑客户端]([链接已屏蔽])

2，打开下载好的无影云电脑客户端选择 **个人版云电脑** 使用支付宝二维码扫码登陆得到以下页面


> [!NOTE] [图片 OCR 识别内容]
> 中国电信 14:10
> N%k矧
> 83
> 首页
> @
> 建议您尽快完成实名认证
> 完成后有机会免费领取800小时云电脑时长包(有效期三个月)*;
> 可后续加购个人云电脑。
> 免费领取参与资格:  您的手机号绑定的所有阿里云账号此前均末参与过无影云电脑
> (专业版)  和无影云电脑〈标准版) 的免费试用活动。也未购买过云电脑。
> 用户EA50
> 贝订购1兑换
> 0 >
> 个人云电脑
> 管理镜像
> 为获得最佳使用体验
> 推荐丕载丞影客巳端连接云电脑
> Joo
> 暂无云电脑
> 去开通
> 家庭群组分配的云电脑
> 云电脑
> 家庭
> 我的账号


3，手机上完成上图顶部实名认证免费领取800小时云电脑试用

4，配置选择2核4G,机房选择离所在地最近的地区，系统镜像选择Windows

- 注意：选择云电脑而 **不是ECS云服务器**

5，完成免费试用云电脑领取后，使用支付宝重新扫码登陆阿里无影云电脑客户端

6，通过客户端连接云电脑开始使用


> [!NOTE] [图片 OCR 识别内容]
> 无影云电脑
> [
> 00
> 个人云电脑
> 运行中
> 云电脑基础款
> 订购云电脑
> 电源
> 更新
> 管理
> 团队分配的云电脑
> 暂无团队为您分配电脑。可主动申请加入


---

### 帖子 #31: 如何更优雅地避免触发限流获取Prod Correlation代码优化
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
   → [Tips]( [../顾问 CA42779 (Rank 49)/[Commented] [BRAIN TIPS] 5 ways to potentially increase returns of an alpha_8833033953559.md](../顾问 CA42779 (Rank 49)/[Commented] [BRAIN TIPS] 5 ways to potentially increase returns of an alpha_8833033953559.md) )

6. Truncation helps in controlling the stock weight in the Alpha simulation. Read this Forum post to understand why.  
   → [Forum post]( [[链接已屏蔽]) )

7. Try working on Delay 0 Alphas. This Forum post may help you.  
   → [Forum post]( [../顾问 CC40930 (Rank 95)/[Commented] [BRAIN TIPS] Seven Tips for Creating Delay-0 D0 Alphas_9223578608663.md](../顾问 CC40930 (Rank 95)/[Commented] [BRAIN TIPS] Seven Tips for Creating Delay-0 D0 Alphas_9223578608663.md) )

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

### 帖子 #32: 💻如何设置云电脑之京东云？
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何设置云电脑之京东云_25880682394263.md
- **讨论数**: 4

本文旨在帮助大家顺畅设置云电脑，不构成任何商业推荐，请自行选择合适的方案。

**免费试用7天： [官网试用中心-京东云 (jdcloud.com)]([链接已屏蔽])**

**
> [!NOTE] [图片 OCR 识别内容]
> 云产品体验库
> 丰富。安全
> 稳定的试用产品库,
> 满足您的需求。试用后仍可参与新人秒杀活动。
> 查看试用规则
> 热门推荐
> 弹性计算
> 存储
> 安全
> 人工智能
> 开发与运维
> 企业碰用
> 数据库
> 网络
> 容器和中间件
> 云主机 2核4G5M
> 云主机 2核4G5M
> 云电脑 4核86
> 轻量云主机2核2G3M
> 爆款机型。极致性价比。轻量建站
> 爆款机型
> 极致性价比,轻量建站
> 即开即用的"云上电脑"
> 不受时间
> 地
> 预装建站
> 电商
> 办公
> CRM等精选
> 应用部署。开发必选
> 应用部署
> 开发必选
> 点。设备限制,随时随地使用
> 软件。即开即用
> 配置 2核4G5M
> 配置 2核4G5M
> 10M基础带宽
> 2核26 _
> 406硬盘
> 存储 40G HDD
> 存储 60G HDD
> 无界高2办公
> 3/带宽。2006流量/月
> 续费低至4折
> 续费享优惠
> 即开即用
> 续费享优惠
> 免费试用30天
> 免费试用7天
> 免费试用7天
> 免费试用7天
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 鼍
**

**付费版本：** 丰俭由人，实测最低版本 2C2G1M （38/年）或3M（58/年）都可以顺畅运行并调试代码。传送门链接: [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 爆品秒杀。下单领1000京豆
> 下单金额大于100元。 可抽奖领1000京豆_
> 瓜分200万京豆
> 活动规则
> 轻量 2核26 低至36元
> 轻量云主机 2核46 SM 1年
> 轻量云主机 2核46 SM 3年
> 轻量4核166 1年13年
> 超值!中午12点
> 晚上12点加库存
> 热销机型。
> 即开即用
> 超值推荐!
> 热销机型,
> 即开即用;
> 超值推荐!
> 热门游戏,
> 一键部署!
> 规格
> 2C26-406 SSD系统盘-3M
> 规格
> 2C46-606 SSD系统盘-5M
> 规格
> 2C46-606 SSD系统盘-5Mi
> 规格
> 4C166-1006 SSD系统盘-5 ~
> 时长 1年
> 时长 1年
> 时长
> 3年
> 时长 1年
> 56元1年
> 限购1台
> 新人专享
> 158元1年
> 限购1台
> 新人专享
> 618元/3年
> 限购1台
> 新人专享
> 518元/1年
> 限购1台
> 新人专享
> 原价522.72元/年
> 原价849.72元年
> 原e2459.+6元年
> 原价19944元+年
> 已抢:
> 609
> 已抢:
> 22%
> 已抢:
> 12%
> 已抢:
> 12%
> 立即秒杀
> 立即秒杀 
> 立即秒杀 
> 立即秒杀


选择所在城市最近的节点，选择windows server镜像，完成购买后，登录控制台，


> [!NOTE] [图片 OCR 识别内容]
> 京东云
> 品 云服务 `
> 佥概览
> 全站搜索
> 费用
> 工单
> 产品与服务
> 运维管理
> 安全管理
> 十新建
> 常用服务
> 云主机 CVM
> 原生容器
> 私有网络
> 云硬盘
> 对象存储
> 云搜索 Elasticsearch
> 云缓存 Redis
> 添加常用服务
> 请输入关键词
> 如云主机
> 最近访问:  轻量云主机
> 已开通服务
> 华北-北京
> 华东-宿迁
> 华东-上海
> 华南-广州
> 私有网络
> 1110
> 轻量云主机
> 1/100
> 云主机
> 华北-北京
> 华东-宿迁
> 华东-上海
> 华南-广州
> 总数量 (个)
> 运行中
> 即将过期
> 己过期
> 报警实例
> 0
> 0
> 0
> 0
> https:/Ilavm-console jdcloud.com/lavm/list


进入轻量云主机，重置主机密码, 充值密码后请先通过网页登录，选择VNC方式登录后。会弹出是否允许发现网络，选择是。设置完成后建议重启云电脑


> [!NOTE] [图片 OCR 识别内容]
> C乐云
> W  飞服劣 `
> 仙t笕
> 全站搜察
> (
> 贵用
> L单
> 笛条
> 渠迫官埋
> 灼物牛
> ()
> blngshul115
> 轻量云主机
> 网站搭建
> 搭建开发环境
> 搭建常用办公软件
> 主机列表
> 网站搭建
> 最佳实践
> 常见问题
> 镜像列表
> 使用镜像可以快速搭建您的个人博客 企业网站。电子商务平合
> 论坛等网站;  如果您需要手
> 使用WordPress镜像搭建网站
> 如何更换主机的镜像
> SSH密钥
> 动部署网站。可以参考最佳实践部署静态网站和部署Nodejs SSR应用。
> 使用Ghost镜像搭建博客系统
> 使用WebTerminal登录主机
> 推荐镜像
> 使用PrestaShop搭建跨境电商平台
> 修改防火墙端口号
> Ghost博客系
> Prestashop
> 部署静态网站
> 网站备案操作说明
> WordPress
> =Bhost
> 统
> 电商平台
> 手动搭建WordPress应用
> 轻量云主机如何备份
> 部署Nodejs SSR应用
> 轻量云主机超过流量包后如何计费
> 轻量云主机支持的镜像说明
> 视频演示专区 
> 关机
> 
> 重启
> 重置密码
> 华北-北京
> 华南-广州
> 华东-宿迁
> 创建
> 实例名称
> 请输入实例名称。
> I0
> 重装系统
> 实例0
> 实例名称
> 镜像名称
> 配置
> 状态
> 地址
> 计费
> 续费
> 升级套餐
> Windows Server
> CPU: 2核
> 运行中
> 104.
> 到期时间:  2025-08-1023:59:59
> 登录
> 2019数据中心版
> 内存:  268
> 更多
> 1/
> 64位中文版
> 带宽: 1Mbps
> 共1条
> 10条顷


远程登录云主机： [登录Windows实例--云主机 CVM-帮助文档-京东云 (jdcloud.com)]([链接已屏蔽])

建议使用（Windows）远程登录或（Mac）Remost Desktop 进行登录，输入上图中你的公网IP，用户名（默认Administrator）和密码，即可连接登录。至此完成云电脑的设置，在云电脑上搭建所需python环境即可

---

### 帖子 #33: 1. 下载/增量更新download_data(session, flag_increment=True)Self-correlation 0.7691 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.这是代码计算结果：alpha_id:  XgQqkZda self_corr:  0.7691116930719178alpha_id = "XgQqkZda"Self-correlation is 0.4589, which is above cutoff of 0.7, or Sharpe is better by 10.0% or more.这是代码计算结果：alpha_id:  zq6wpknV self_corr:  0.48371278563080605alpha_id = "zq6wpknV"加载数据os_alpha_ids, os_alpha_rets = load_data(tag='SelfCorr')self_corr = calc_self_corr(    session,    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)print("alpha_id: ", alpha_id, "self_corr: ", self_corr)
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

### 帖子 #34: 【Brain Lab】利用Brain Lab进行字段剪枝
- **主帖链接**: 【Brain Lab】利用Brain Lab进行字段剪枝.md
- **讨论数**: 0

> 利用Brain Lab进行字段相关性剪枝，很久之前就有这个想法了，也研究了一段时间，但是没有成功实现，最后会附上我的代码。思路来源一阶回测完进入二阶中间可以进行相关性剪枝。论坛中“点塔王”，大语言模型驱动寻找最相关的字段。weijie老师之前提到的根据一个已经提交的alpha通过相关性找到另一个可以提交的alpha。思路来源就是上述内容，除了对回测完的一阶alpha进行相关性剪枝外，完全可以在一阶回测之前对字段进行相关性剪枝，有些字段之间存在很高的相似性，如果都进行回测的话会浪费一定的回测资源，而有些字段描述非常相近（或者不具备任何含义的无用描述），通过大语言模型进行相关性寻找的话，其实是不准确的，所以个人认为对字段进行相关性剪枝还是很有必要的。代码（存在一定的问题）参考来源：FS29418大佬的帖子：[L2] 【Brain Labs】实现在Brain Labs中计算数据字段的相关性修改版v2代码优化_33638658994711.md如果你要把代码写入到brain lab中，可以看一下这个篇大佬的帖子：[L2] WorldQuant Brain Lab 复制粘贴限制自动化代码输入方案_32983618750999.md目前存在的问题：1. 相关性计算时间过长，计算每对字段时大约会耗时3-4秒左右，如果要计算200个字段的相关性，那么就需要计算200*（200-1）/2次，相当于59700秒，16个多小时。2. 如果采用贪心的算法的话，可能会减少一定的计算时间，但是只能保证局部最优，或者可以一部分一部分的计算，也只能保证局部最优。3. 使用lab时卡顿还是挺明显的，且如果notebook正在运行，但是关闭了brain lab的浏览器，一定时间后（这个具体是多少没有测过）再重新打开，正在运行的notebook会被关闭，某些情况下网络不稳定，brain lab也会自己断掉...（有些折磨）4. 除了计算时间问题外，内存消耗也是一个大问题，单个字段的csv文件大约在40mb左右，如果要计算的字段数量过多的话，会直接导致内存溢出（即使brain lab已经给了16g的内存）...（好像可以改为流式加载，需要计算时再读取，计算完后直接释放，但是我没实现...太菜了求放过）from brain import Brainfrom brain.errors import UnexpectedStatusfrom typing import Optionalimport numpy as npimport pandas as pdimport timeimport osimport loggingimport gcfrom concurrent.futures import ThreadPoolExecutor# 可配置的日志与缓存控制try:import pyarrow  # noqa: F401HAS_PARQUET = Trueexcept Exception:HAS_PARQUET = FalseVERBOSE = os.environ.get("CORR_VERBOSE", "0").lower() in ("1", "true", "yes", "y")_logger = logging.getLogger(__name__)if VERBOSE and not _logger.handlers:logging.basicConfig(level=logging.INFO)# 进程内 DataFrame 内存缓存，减少重复磁盘 IO_MEM_CACHE: dict = {}def calc_mean_corr(df1, df2) -> float:t0 = time.time()# 对齐：一次性按行、列取交集并对齐if df1 is None or df2 is None:return np.nancommon_rows = df1.index.intersection(df2.index)common_cols = df1.columns.intersection(df2.columns)if len(common_rows) == 0 or len(common_cols) == 0:return np.nan# 替换无穷为 NaN，避免下游计算发散，并降精度到 float32 加速与省内存df1a = df1.loc[common_rows, common_cols].replace([np.inf, -np.inf], np.nan).astype(np.float32, copy=False)df2a = df2.loc[common_rows, common_cols].replace([np.inf, -np.inf], np.nan).astype(np.float32, copy=False)# 仅在“同一位置同时非空”的样本上计算：both_non_na = df1a.notna() & df2a.notna()valid_counts = both_non_na.sum(axis=0)mask_enough = valid_counts >= 2  # 至少 2 个有效样本才能计算相关# 在有效样本上计算列标准差，排除零方差列，避免 0/0 产生 invalid 警告df1_masked = df1a.where(both_non_na)df2_masked = df2a.where(both_non_na)std1 = df1_masked.std(axis=0, ddof=1)std2 = df2_masked.std(axis=0, ddof=1)mask_nonzero = (std1 > 0) & (std2 > 0)col_mask = mask_enough & mask_nonzeroif not col_mask.any():return np.nancols = df1a.columns[col_mask]df1f = df1a[cols]df2f = df2a[cols]with np.errstate(invalid='ignore', divide='ignore'):corrs = df1f.corrwith(df2f, axis=0)result = float(corrs.dropna().mean()) if corrs.notna().any() else np.nanif VERBOSE:_logger.info("calc_mean_corr cost %.4fs on %d/%d cols", time.time() - t0, int(col_mask.sum()), len(common_cols))return resultdef save_df(region: str, delay: int, universe: str, data_field: str, df: pd.DataFrame):# 统一缓存目录结构root = os.path.abspath('.')base_dir = os.path.join(root, "dataframe", region, str(delay), universe)os.makedirs(base_dir, exist_ok=True)parquet_path = os.path.join(base_dir, f"{data_field}.parquet")csv_path = os.path.join(base_dir, f"{data_field}.csv")try:if HAS_PARQUET:df.to_parquet(parquet_path, index=True)else:df.to_csv(csv_path)except Exception:# 兜底：若 Parquet 写入失败，回退到 CSVdf.to_csv(csv_path)def get_df(region: str, delay: int, universe: str, data_field: str) -> Optional[pd.DataFrame]:root = os.path.abspath('.')base_dir = os.path.join(root, "dataframe", region, str(delay), universe)parquet_path = os.path.join(base_dir, f"{data_field}.parquet")csv_path = os.path.join(base_dir, f"{data_field}.csv")df = None# 优先读取 Parquet（若存在）if os.path.exists(parquet_path):try:df = pd.read_parquet(parquet_path)except Exception:df = None# 回退到 CSVif df is None and os.path.exists(csv_path):try:df = pd.read_csv(csv_path, index_col=0, parse_dates=True)except Exception:df = Noneif df is not None:# 确保索引为 DatetimeIndex，避免日期比较异常if not isinstance(df.index, pd.DatetimeIndex):try:df.index = pd.to_datetime(df.index, errors='coerce')except Exception:passreturn dfreturn Nonedef filter_by_dates(df: pd.DataFrame, dates: list):mask = pd.Series(True, index=df.index)for op, date_str in dates:date = pd.to_datetime(date_str)if op == '>':mask &= df.index > dateelif op == '>=':mask &= df.index >= dateelif op == '<':mask &= df.index < dateelif op == '<=':mask &= df.index <= dateelif op == '==':mask &= df.index == dateelif op == '!=':mask &= df.index != dateelse:raise ValueError(f"Unsupported operator: {op}")return df[mask]def get_df_if_exist(brain: Brain, data_field, dates: Optional[list] = None, use_mem_cache: bool = True):passkey = (str(brain.region), brain.delay, str(brain.universe), data_field.id)# 先查进程内缓存，避免重复磁盘/网络 IOif use_mem_cache and key in _MEM_CACHE:df_cached = _MEM_CACHE[key]return filter_by_dates(df_cached, dates) if dates else df_cached# 本地缓存（磁盘）df = get_df(key[0], key[1], key[2], key[3])if df is not None:if use_mem_cache:_MEM_CACHE[key] = dfreturn filter_by_dates(df, dates) if dates else df# 远端获取，并写入本地与内存缓存while True:try:df = brain.get_data_frame(data_field)except UnexpectedStatus:time.sleep(0.2)continueexcept Exception as e:if VERBOSE:_logger.warning("get_data_frame error: %s", e)time.sleep(0.2)continueelse:breaksave_df(key[0], key[1], key[2], key[3], df)if use_mem_cache:_MEM_CACHE[key] = dfreturn filter_by_dates(df, dates) if dates else dfdef calc_data_field_mean_corr(brain: Brain, data_field1: str, data_field2: str):data_field1 = brain.get_data_field(data_field1)data_field2 = brain.get_data_field(data_field2)df1 = get_df_if_exist(brain, data_field1)df2 = get_df_if_exist(brain, data_field2)return calc_mean_corr(df1, df2)def get_data_field_similar(datafield: str, region: str, delay: int, universe: str, same_data_set: bool = True, dates: Optional[list] = None, target_type: list = ["MATRIX"]):brain = Brain(region=region, delay=delay, universe=universe)datafield = brain.get_data_field(datafield)dataframe = get_df_if_exist(brain, datafield, dates=dates)now_dataset = datafield.dataset.iddatasets = brain.get_data_sets()datasets = datasets.resultsdatasetsId = [dataset.id for dataset in datasets]if same_data_set:datasetsId = [now_dataset]dataCorr = []for dataset in datasetsId:datafields = brain.get_data_fields(data_set=dataset)datafieldsId = [datafield.id for datafield in datafields.results if datafield.type in target_type]for datafield in datafieldsId:datafield = brain.get_data_field(datafield)dataframeN = get_df_if_exist(brain, datafield, dates=dates)selfcorr = calc_mean_corr(dataframe, dataframeN)dataCorr.append({'id': datafield,'sc': selfcorr,})return pd.DataFrame(dataCorr).sort_values(by='sc', ascending=False)def pairwise_corr_in_dataset(region: str,delay: int,universe: str,dataset_id: str,*,dates: Optional[list] = None,target_type: list = ["MATRIX"],threshold: Optional[float] = None,use_abs: bool = False,) -> pd.DataFrame:"""计算指定数据集内所有字段两两之间的相似度（使用 calc_mean_corr 定义），并按阈值筛选。参数:region, delay, universe: Brain 环境参数dataset_id: 数据集 ID（如 datafield.dataset.id）dates: 可选的日期过滤 [(op, "YYYY-MM-DD"), ...]target_type: 用于筛选字段类型，默认 ["MATRIX"]threshold: 可选阈值；若提供，将筛选 (use_abs==False: corr>=threshold；use_abs==True: abs(corr)>=threshold)use_abs: 是否按绝对值阈值筛选返回:DataFrame，列为 ["id1", "id2", "corr" ]，每行对应一个字段对，按 corr 降序排序。"""brain = Brain(region=region, delay=delay, universe=universe)# 拉取候选字段 ID 列表datafields = brain.get_data_fields(data_set=dataset_id)field_ids = [f.id for f in datafields.results if f.type in target_type]n = len(field_ids)total_pairs = n * (n - 1) // 2if total_pairs > 0:print(f"[corr] dataset={dataset_id}: {n} fields, {total_pairs} pairs to compute...")else:print(f"[corr] dataset={dataset_id}: {n} fields, no pairs to compute.")# 预取所有 DataFrame，利用本地与内存缓存items = []  # [(id, df)]for fid in field_ids:df_obj = brain.get_data_field(fid)df = get_df_if_exist(brain, df_obj, dates=dates)items.append((fid, df))processed_pairs = 0progress_step = max(1, total_pairs // 20)  # 约 5% 一个进度点next_mark = progress_stepresults = []for i in range(n):id1, df1 = items[i]for j in range(i + 1, n):  # 上三角，避免重复/自相关id2, df2 = items[j]corr = calc_mean_corr(df1, df2)if np.isnan(corr):processed_pairs += 1if processed_pairs >= next_mark or processed_pairs == total_pairs:print(f"[corr] progress: {processed_pairs}/{total_pairs} ({processed_pairs/total_pairs:.1%})")next_mark += progress_stepcontinueok = Trueif threshold is not None:ok = (abs(corr) >= threshold) if use_abs else (corr >= threshold)if ok:results.append({"id1": id1, "id2": id2, "corr": float(corr)})processed_pairs += 1if processed_pairs >= next_mark or processed_pairs == total_pairs:print(f"[corr] progress: {processed_pairs}/{total_pairs} ({processed_pairs/total_pairs:.1%})")next_mark += progress_stepif not results:return pd.DataFrame(columns=["id1", "id2", "corr"])  # 空结果df_res = pd.DataFrame(results)# 排序：按 corr 降序（如需按绝对值，可手动 df_res.assign(ac=abs(df_res.corr)).sort_values('ac', ascending=False)）df_res = df_res.sort_values(by="corr", ascending=False).reset_index(drop=True)return df_resdef _ensure_dir(p: str):dirpath = os.path.dirname(p)# 当传入的路径不包含目录（例如仅为 'out.csv'）时，dirname 为空字符串，此时无需创建目录if not dirpath:returnos.makedirs(dirpath, exist_ok=True)def _append_rows_csv(file_path: str, rows: list, write_header: bool):if not rows:returndf_chunk = pd.DataFrame(rows)df_chunk.to_csv(file_path, mode='a', header=write_header, index=False)def pairwise_corr_in_dataset_streaming(region: str,delay: int,universe: str,dataset_id: str,*,dates: Optional[list] = None,target_type: list = ["MATRIX"],threshold: Optional[float] = None,less_than: bool = True,output_path: Optional[str] = None,chunk_size: int = 1000,gc_every: int = 10,prefetch: int = 4,) -> str:"""内存友好的两两相关流式计算：只筛选“低于阈值”的相关性（不按绝对值），分批写入 CSV 结果，避免内存溢出。参数:region, delay, universe, dataset_id: 环境与数据集dates: 时间过滤条件列表target_type: 候选字段类型过滤，默认 ["MATRIX"]threshold: 阈值（当 less_than=True 时，筛 corr < threshold；当 threshold 为 None，输出全部）less_than: 是否按 corr < threshold 进行筛选（不使用绝对值）output_path: 输出 CSV 路径；未指定则自动生成至 results/pairwise_corr 下chunk_size: 每批累计多少条结果写盘gc_every: 每处理多少个外层字段触发一次 gc.collect()返回:最终结果 CSV 文件路径"""brain = Brain(region=region, delay=delay, universe=universe)# 获取候选字段datafields = brain.get_data_fields(data_set=dataset_id)field_ids = [f.id for f in datafields.results if f.type in target_type]n = len(field_ids)total_pairs = n * (n - 1) // 2if total_pairs > 0:print(f"[corr-stream] dataset={dataset_id}: {n} fields, {total_pairs} pairs to compute...")else:print(f"[corr-stream] dataset={dataset_id}: {n} fields, no pairs to compute.")if output_path is None:root = os.path.abspath('.')base_dir = os.path.join(root, 'results', 'pairwise_corr', region, str(delay), universe)tag = f"lt_{threshold}" if threshold is not None and less_than else "all"output_path = os.path.join(base_dir, f"{dataset_id}_{tag}.csv")_ensure_dir(output_path)file_exists = os.path.exists(output_path)if not file_exists:# 写表头_append_rows_csv(output_path, [{"id1": "", "id2": "", "corr": ""}], write_header=True)# 清空刚写入的空行with open(output_path, 'w', encoding='utf-8') as fw:fw.write('id1,id2,corr\n')file_exists = Truebuffer = []processed_pairs = 0progress_step = max(1, total_pairs // 20)  # 约 5% 一个进度点next_mark = progress_stepfor i, fid1 in enumerate(field_ids):df1 = get_df_if_exist(brain, brain.get_data_field(fid1), dates=dates, use_mem_cache=False)# 预取 df2，隐藏 IO 延迟start_j = i + 1end_j = nif start_j >= end_j:if gc_every and (i + 1) % gc_every == 0:gc.collect()continueprefetch = max(1, int(prefetch))def load_df2(j_idx: int):fid = field_ids[j_idx]return fid, get_df_if_exist(brain, brain.get_data_field(fid), dates=dates, use_mem_cache=False)with ThreadPoolExecutor(max_workers=prefetch) as ex:pending = {}initial = min(prefetch, end_j - start_j)for k in range(initial):j_idx = start_j + kpending[j_idx] = ex.submit(load_df2, j_idx)next_submit = start_j + initialj = start_jwhile j < end_j:# 取回当前 j 的 df2（确保按顺序处理，便于进度统计与缓冲写入）if j not in pending:pending[j] = ex.submit(load_df2, j)fid2, df2 = pending.pop(j).result()corr = calc_mean_corr(df1, df2)if not np.isnan(corr):if threshold is None or (less_than and corr < threshold) or (not less_than and corr >= threshold):buffer.append({"id1": fid1, "id2": fid2, "corr": float(corr)})processed_pairs += 1if len(buffer) >= chunk_size:_append_rows_csv(output_path, buffer, write_header=False)buffer.clear()if processed_pairs >= next_mark or processed_pairs == total_pairs:print(f"[corr-stream] progress: {processed_pairs}/{total_pairs} ({processed_pairs/total_pairs:.1%})")next_mark += progress_step# 补提交新的预取任务if next_submit < end_j:pending[next_submit] = ex.submit(load_df2, next_submit)next_submit += 1j += 1if gc_every and (i + 1) % gc_every == 0:gc.collect()if buffer:_append_rows_csv(output_path, buffer, write_header=False)return output_pathpairwise_corr_in_dataset_streaming(region='USA',delay=1,universe='T0P3000',dataset_id='anll1_2_2pme',threshold=0.8,less_than=True,output_path='results/pairwise_corr/USA/1/T0P3000/anll1_2_2pme_lt_0.5.csv',chunk_size=1000,gc_every=10,)总之，个人感觉这个方向还不错，但是brain lab存在一定的问题，以及个人的问题，没有完全实现，如果你可以再此方向上有所成功，希望能够分享一下，不胜感激。

---

### 帖子 #35: 【Brain Lab】利用Brain Lab进行字段剪枝
- **主帖链接**: https://support.worldquantbrain.com【Brain Lab】利用Brain Lab进行字段剪枝_34888787908631.md
- **讨论数**: 0

> 利用Brain Lab进行字段相关性剪枝，很久之前就有这个想法了，也研究了一段时间，但是没有成功实现，最后会附上我的代码。

**思路来源**

1. 一阶回测完进入二阶中间可以进行相关性剪枝。
2. 论坛中“点塔王”，大语言模型驱动寻找最相关的字段。
3. weijie老师之前提到的根据一个已经提交的alpha通过相关性找到另一个可以提交的alpha。

思路来源就是上述内容，除了对回测完的一阶alpha进行相关性剪枝外，完全可以在一阶回测之前对字段进行相关性剪枝，有些字段之间存在很高的相似性，如果都进行回测的话会浪费一定的回测资源，而有些字段描述非常相近（或者不具备任何含义的无用描述），通过大语言模型进行相关性寻找的话，其实是不准确的，所以个人认为对字段进行相关性剪枝还是很有必要的。

**代码（存在一定的问题）**

参考来源： [FS29418](/hc/zh-cn/profiles/28884318315799-FS29418) 大佬的帖子： [[L2] 【Brain Labs】实现在Brain Labs中计算数据字段的相关性修改版v2代码优化_33638658994711.md]([L2] 【Brain Labs】实现在Brain Labs中计算数据字段的相关性修改版v2代码优化_33638658994711.md)

如果你要把代码写入到brain lab中，可以看一下这个篇大佬的帖子： [[L2] WorldQuant Brain Lab 复制粘贴限制自动化代码输入方案_32983618750999.md]([L2] WorldQuant Brain Lab 复制粘贴限制自动化代码输入方案_32983618750999.md)

目前存在的问题：

1. 相关性计算时间过长，计算每对字段时大约会耗时3-4秒左右，如果要计算200个字段的相关性，那么就需要计算200*（200-1）/2次，相当于59700秒，16个多小时。

2. 如果采用贪心的算法的话，可能会减少一定的计算时间，但是只能保证局部最优，或者可以一部分一部分的计算，也只能保证局部最优。

3. 使用lab时卡顿还是挺明显的，且如果notebook正在运行，但是关闭了brain lab的浏览器，一定时间后（这个具体是多少没有测过）再重新打开，正在运行的notebook会被关闭，某些情况下网络不稳定，brain lab也会自己断掉...（有些折磨）

4. 除了计算时间问题外，内存消耗也是一个大问题，单个字段的csv文件大约在40mb左右，如果要计算的字段数量过多的话，会直接导致内存溢出（即使brain lab已经给了16g的内存）...（好像可以改为流式加载，需要计算时再读取，计算完后直接释放，但是我没实现...太菜了求放过）

```
from brain import Brainfrom brain.errors import UnexpectedStatusfrom typing import Optionalimport numpy as npimport pandas as pdimport timeimport osimport loggingimport gcfrom concurrent.futures import ThreadPoolExecutor# 可配置的日志与缓存控制try:    import pyarrow  # noqa: F401    HAS_PARQUET = Trueexcept Exception:    HAS_PARQUET = FalseVERBOSE = os.environ.get("CORR_VERBOSE", "0").lower() in ("1", "true", "yes", "y")_logger = logging.getLogger(__name__)if VERBOSE and not _logger.handlers:    logging.basicConfig(level=logging.INFO)# 进程内 DataFrame 内存缓存，减少重复磁盘 IO_MEM_CACHE: dict = {}def calc_mean_corr(df1, df2) -> float:    t0 = time.time()    # 对齐：一次性按行、列取交集并对齐    if df1 is None or df2 is None:        return np.nan    common_rows = df1.index.intersection(df2.index)    common_cols = df1.columns.intersection(df2.columns)    if len(common_rows) == 0 or len(common_cols) == 0:        return np.nan    # 替换无穷为 NaN，避免下游计算发散，并降精度到 float32 加速与省内存    df1a = df1.loc[common_rows, common_cols].replace([np.inf, -np.inf], np.nan).astype(np.float32, copy=False)    df2a = df2.loc[common_rows, common_cols].replace([np.inf, -np.inf], np.nan).astype(np.float32, copy=False)    # 仅在“同一位置同时非空”的样本上计算：    both_non_na = df1a.notna() & df2a.notna()    valid_counts = both_non_na.sum(axis=0)    mask_enough = valid_counts >= 2  # 至少 2 个有效样本才能计算相关    # 在有效样本上计算列标准差，排除零方差列，避免 0/0 产生 invalid 警告    df1_masked = df1a.where(both_non_na)    df2_masked = df2a.where(both_non_na)    std1 = df1_masked.std(axis=0, ddof=1)    std2 = df2_masked.std(axis=0, ddof=1)    mask_nonzero = (std1 > 0) & (std2 > 0)    col_mask = mask_enough & mask_nonzero    if not col_mask.any():        return np.nan    cols = df1a.columns[col_mask]    df1f = df1a[cols]    df2f = df2a[cols]    with np.errstate(invalid='ignore', divide='ignore'):        corrs = df1f.corrwith(df2f, axis=0)    result = float(corrs.dropna().mean()) if corrs.notna().any() else np.nan    if VERBOSE:        _logger.info("calc_mean_corr cost %.4fs on %d/%d cols", time.time() - t0, int(col_mask.sum()), len(common_cols))    return resultdef save_df(region: str, delay: int, universe: str, data_field: str, df: pd.DataFrame):    # 统一缓存目录结构    root = os.path.abspath('.')    base_dir = os.path.join(root, "dataframe", region, str(delay), universe)    os.makedirs(base_dir, exist_ok=True)    parquet_path = os.path.join(base_dir, f"{data_field}.parquet")    csv_path = os.path.join(base_dir, f"{data_field}.csv")    try:        if HAS_PARQUET:            df.to_parquet(parquet_path, index=True)        else:            df.to_csv(csv_path)    except Exception:        # 兜底：若 Parquet 写入失败，回退到 CSV        df.to_csv(csv_path)def get_df(region: str, delay: int, universe: str, data_field: str) -> Optional[pd.DataFrame]:    root = os.path.abspath('.')    base_dir = os.path.join(root, "dataframe", region, str(delay), universe)    parquet_path = os.path.join(base_dir, f"{data_field}.parquet")    csv_path = os.path.join(base_dir, f"{data_field}.csv")    df = None    # 优先读取 Parquet（若存在）    if os.path.exists(parquet_path):        try:            df = pd.read_parquet(parquet_path)        except Exception:            df = None    # 回退到 CSV    if df is None and os.path.exists(csv_path):        try:            df = pd.read_csv(csv_path, index_col=0, parse_dates=True)        except Exception:            df = None    if df is not None:        # 确保索引为 DatetimeIndex，避免日期比较异常        if not isinstance(df.index, pd.DatetimeIndex):            try:                df.index = pd.to_datetime(df.index, errors='coerce')            except Exception:                pass        return df    return Nonedef filter_by_dates(df: pd.DataFrame, dates: list):    mask = pd.Series(True, index=df.index)    for op, date_str in dates:        date = pd.to_datetime(date_str)        if op == '>':            mask &= df.index > date        elif op == '>=':            mask &= df.index >= date        elif op == '<':            mask &= df.index < date        elif op == '<=':            mask &= df.index <= date        elif op == '==':            mask &= df.index == date        elif op == '!=':            mask &= df.index != date        else:            raise ValueError(f"Unsupported operator: {op}")    return df[mask]def get_df_if_exist(brain: Brain, data_field, dates: Optional[list] = None, use_mem_cache: bool = True):    pass    key = (str(brain.region), brain.delay, str(brain.universe), data_field.id)    # 先查进程内缓存，避免重复磁盘/网络 IO    if use_mem_cache and key in _MEM_CACHE:        df_cached = _MEM_CACHE[key]        return filter_by_dates(df_cached, dates) if dates else df_cached    # 本地缓存（磁盘）    df = get_df(key[0], key[1], key[2], key[3])    if df is not None:        if use_mem_cache:            _MEM_CACHE[key] = df        return filter_by_dates(df, dates) if dates else df    # 远端获取，并写入本地与内存缓存    while True:        try:            df = brain.get_data_frame(data_field)        except UnexpectedStatus:            time.sleep(0.2)            continue        except Exception as e:            if VERBOSE:                _logger.warning("get_data_frame error: %s", e)            time.sleep(0.2)            continue        else:            break    save_df(key[0], key[1], key[2], key[3], df)    if use_mem_cache:        _MEM_CACHE[key] = df    return filter_by_dates(df, dates) if dates else dfdef calc_data_field_mean_corr(brain: Brain, data_field1: str, data_field2: str):    data_field1 = brain.get_data_field(data_field1)    data_field2 = brain.get_data_field(data_field2)    df1 = get_df_if_exist(brain, data_field1)    df2 = get_df_if_exist(brain, data_field2)    return calc_mean_corr(df1, df2)def get_data_field_similar(datafield: str, region: str, delay: int, universe: str, same_data_set: bool = True, dates: Optional[list] = None, target_type: list = ["MATRIX"]):    brain = Brain(region=region, delay=delay, universe=universe)    datafield = brain.get_data_field(datafield)    dataframe = get_df_if_exist(brain, datafield, dates=dates)    now_dataset = datafield.dataset.id    datasets = brain.get_data_sets()    datasets = datasets.results    datasetsId = [dataset.id for dataset in datasets]    if same_data_set:        datasetsId = [now_dataset]    dataCorr = []    for dataset in datasetsId:        datafields = brain.get_data_fields(data_set=dataset)        datafieldsId = [datafield.id for datafield in datafields.results if datafield.type in target_type]        for datafield in datafieldsId:            datafield = brain.get_data_field(datafield)            dataframeN = get_df_if_exist(brain, datafield, dates=dates)            selfcorr = calc_mean_corr(dataframe, dataframeN)            dataCorr.append({                'id': datafield,                'sc': selfcorr,            })    return pd.DataFrame(dataCorr).sort_values(by='sc', ascending=False)def pairwise_corr_in_dataset(    region: str,    delay: int,    universe: str,    dataset_id: str,    *,    dates: Optional[list] = None,    target_type: list = ["MATRIX"],    threshold: Optional[float] = None,    use_abs: bool = False,) -> pd.DataFrame:    """    计算指定数据集内所有字段两两之间的相似度（使用 calc_mean_corr 定义），并按阈值筛选。    参数:        region, delay, universe: Brain 环境参数        dataset_id: 数据集 ID（如 datafield.dataset.id）        dates: 可选的日期过滤 [(op, "YYYY-MM-DD"), ...]        target_type: 用于筛选字段类型，默认 ["MATRIX"]        threshold: 可选阈值；若提供，将筛选 (use_abs==False: corr>=threshold；use_abs==True: abs(corr)>=threshold)        use_abs: 是否按绝对值阈值筛选    返回:        DataFrame，列为 ["id1", "id2", "corr" ]，每行对应一个字段对，按 corr 降序排序。    """    brain = Brain(region=region, delay=delay, universe=universe)    # 拉取候选字段 ID 列表    datafields = brain.get_data_fields(data_set=dataset_id)    field_ids = [f.id for f in datafields.results if f.type in target_type]    n = len(field_ids)    total_pairs = n * (n - 1) // 2    if total_pairs > 0:        print(f"[corr] dataset={dataset_id}: {n} fields, {total_pairs} pairs to compute...")    else:        print(f"[corr] dataset={dataset_id}: {n} fields, no pairs to compute.")    # 预取所有 DataFrame，利用本地与内存缓存    items = []  # [(id, df)]    for fid in field_ids:        df_obj = brain.get_data_field(fid)        df = get_df_if_exist(brain, df_obj, dates=dates)        items.append((fid, df))    processed_pairs = 0    progress_step = max(1, total_pairs // 20)  # 约 5% 一个进度点    next_mark = progress_step    results = []    for i in range(n):        id1, df1 = items[i]        for j in range(i + 1, n):  # 上三角，避免重复/自相关            id2, df2 = items[j]            corr = calc_mean_corr(df1, df2)            if np.isnan(corr):                processed_pairs += 1                if processed_pairs >= next_mark or processed_pairs == total_pairs:                    print(f"[corr] progress: {processed_pairs}/{total_pairs} ({processed_pairs/total_pairs:.1%})")                    next_mark += progress_step                continue            ok = True            if threshold is not None:                ok = (abs(corr) >= threshold) if use_abs else (corr >= threshold)            if ok:                results.append({"id1": id1, "id2": id2, "corr": float(corr)})            processed_pairs += 1            if processed_pairs >= next_mark or processed_pairs == total_pairs:                print(f"[corr] progress: {processed_pairs}/{total_pairs} ({processed_pairs/total_pairs:.1%})")                next_mark += progress_step    if not results:        return pd.DataFrame(columns=["id1", "id2", "corr"])  # 空结果    df_res = pd.DataFrame(results)    # 排序：按 corr 降序（如需按绝对值，可手动 df_res.assign(ac=abs(df_res.corr)).sort_values('ac', ascending=False)）    df_res = df_res.sort_values(by="corr", ascending=False).reset_index(drop=True)    return df_resdef _ensure_dir(p: str):    dirpath = os.path.dirname(p)    # 当传入的路径不包含目录（例如仅为 'out.csv'）时，dirname 为空字符串，此时无需创建目录    if not dirpath:        return    os.makedirs(dirpath, exist_ok=True)def _append_rows_csv(file_path: str, rows: list, write_header: bool):    if not rows:        return    df_chunk = pd.DataFrame(rows)    df_chunk.to_csv(file_path, mode='a', header=write_header, index=False)def pairwise_corr_in_dataset_streaming(    region: str,    delay: int,    universe: str,    dataset_id: str,    *,    dates: Optional[list] = None,    target_type: list = ["MATRIX"],    threshold: Optional[float] = None,    less_than: bool = True,    output_path: Optional[str] = None,    chunk_size: int = 1000,    gc_every: int = 10,    prefetch: int = 4,) -> str:    """    内存友好的两两相关流式计算：只筛选“低于阈值”的相关性（不按绝对值），分批写入 CSV 结果，避免内存溢出。    参数:        region, delay, universe, dataset_id: 环境与数据集        dates: 时间过滤条件列表        target_type: 候选字段类型过滤，默认 ["MATRIX"]        threshold: 阈值（当 less_than=True 时，筛 corr < threshold；当 threshold 为 None，输出全部）        less_than: 是否按 corr < threshold 进行筛选（不使用绝对值）        output_path: 输出 CSV 路径；未指定则自动生成至 results/pairwise_corr 下        chunk_size: 每批累计多少条结果写盘        gc_every: 每处理多少个外层字段触发一次 gc.collect()    返回:        最终结果 CSV 文件路径    """    brain = Brain(region=region, delay=delay, universe=universe)    # 获取候选字段    datafields = brain.get_data_fields(data_set=dataset_id)    field_ids = [f.id for f in datafields.results if f.type in target_type]    n = len(field_ids)    total_pairs = n * (n - 1) // 2    if total_pairs > 0:        print(f"[corr-stream] dataset={dataset_id}: {n} fields, {total_pairs} pairs to compute...")    else:        print(f"[corr-stream] dataset={dataset_id}: {n} fields, no pairs to compute.")    if output_path is None:        root = os.path.abspath('.')        base_dir = os.path.join(root, 'results', 'pairwise_corr', region, str(delay), universe)        tag = f"lt_{threshold}" if threshold is not None and less_than else "all"        output_path = os.path.join(base_dir, f"{dataset_id}_{tag}.csv")    _ensure_dir(output_path)    file_exists = os.path.exists(output_path)    if not file_exists:        # 写表头        _append_rows_csv(output_path, [{"id1": "", "id2": "", "corr": ""}], write_header=True)        # 清空刚写入的空行        with open(output_path, 'w', encoding='utf-8') as fw:            fw.write('id1,id2,corr\n')        file_exists = True    buffer = []    processed_pairs = 0    progress_step = max(1, total_pairs // 20)  # 约 5% 一个进度点    next_mark = progress_step    for i, fid1 in enumerate(field_ids):        df1 = get_df_if_exist(brain, brain.get_data_field(fid1), dates=dates, use_mem_cache=False)        # 预取 df2，隐藏 IO 延迟        start_j = i + 1        end_j = n        if start_j >= end_j:            if gc_every and (i + 1) % gc_every == 0:                gc.collect()            continue        prefetch = max(1, int(prefetch))        def load_df2(j_idx: int):            fid = field_ids[j_idx]            return fid, get_df_if_exist(brain, brain.get_data_field(fid), dates=dates, use_mem_cache=False)        with ThreadPoolExecutor(max_workers=prefetch) as ex:            pending = {}            initial = min(prefetch, end_j - start_j)            for k in range(initial):                j_idx = start_j + k                pending[j_idx] = ex.submit(load_df2, j_idx)            next_submit = start_j + initial            j = start_j            while j < end_j:                # 取回当前 j 的 df2（确保按顺序处理，便于进度统计与缓冲写入）                if j not in pending:                    pending[j] = ex.submit(load_df2, j)                fid2, df2 = pending.pop(j).result()                corr = calc_mean_corr(df1, df2)                if not np.isnan(corr):                    if threshold is None or (less_than and corr < threshold) or (not less_than and corr >= threshold):                        buffer.append({"id1": fid1, "id2": fid2, "corr": float(corr)})                processed_pairs += 1                if len(buffer) >= chunk_size:                    _append_rows_csv(output_path, buffer, write_header=False)                    buffer.clear()                if processed_pairs >= next_mark or processed_pairs == total_pairs:                    print(f"[corr-stream] progress: {processed_pairs}/{total_pairs} ({processed_pairs/total_pairs:.1%})")                    next_mark += progress_step                # 补提交新的预取任务                if next_submit < end_j:                    pending[next_submit] = ex.submit(load_df2, next_submit)                    next_submit += 1                j += 1        if gc_every and (i + 1) % gc_every == 0:            gc.collect()    if buffer:        _append_rows_csv(output_path, buffer, write_header=False)    return output_pathpairwise_corr_in_dataset_streaming(    region='USA',    delay=1,    universe='T0P3000',    dataset_id='anll1_2_2pme',    threshold=0.8,    less_than=True,    output_path='results/pairwise_corr/USA/1/T0P3000/anll1_2_2pme_lt_0.5.csv',    chunk_size=1000,    gc_every=10,)
```

总之，个人感觉这个方向还不错，但是brain lab存在一定的问题，以及个人的问题，没有完全实现，如果你可以再此方向上有所成功，希望能够分享一下，不胜感激。

---

### 帖子 #36: 【Community Leader - 可视化alpha打分工具 】可视化分析你的alpha，并进行打分，助力Osmosis比赛！
- **主帖链接**: 【Community Leader - 可视化alpha打分工具 】可视化分析你的alpha并进行打分助力Osmosis比赛.md
- **讨论数**: 1

先看效果图拥有的功能：可视化alpha之间的相关性，支持自主调节相关性阈值自主删除/恢复 alpha自主删除alpha之间的连线查看某个alpha的详细指标（无pnl）对alpha平均分配点数按照聚簇分配点数导出/导入分配结果TODO：根据pyr、指标等对alpha进行分类自主进行alpha分类按照分类进行点数分配权重点数分配支持pnl的展示再说下点数分配的思路出发点：最开始的思路是，根据相关性筛选出一个彼此相关性最低的alpha集合，赋予大权重，然后筛选集合内每一个alpha相关性较高的几个alpha赋予较低权重，用来增强这个独特alpha的信号，但是从图中可以看出来，alpha与alpha之间的相关性并没有很高....个人认为这个工具还是挺有用的，未来逐步完善的话，应用到own super alpha上也是一个不错的选择。下面直接献上代码：前端代码<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Alpha相关性网络图</title><script src="[链接已屏蔽] {margin: 0;padding: 0;box-sizing: border-box;}body {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;background: #1a1a2e;color: #eee;overflow: hidden;}#container {display: flex;height: 100vh;}#control-panel {width: 300px;background: #16213e;padding: 20px;overflow-y: auto;box-shadow: 2px 0 10px rgba(0,0,0,0.3);}#graph-container {flex: 1;position: relative;}h1 {font-size: 20px;margin-bottom: 20px;color: #00d9ff;border-bottom: 2px solid #00d9ff;padding-bottom: 10px;}.control-group {margin-bottom: 20px;}.control-group label {display: block;margin-bottom: 8px;font-size: 14px;color: #aaa;}input[type="range"] {width: 100%;height: 6px;border-radius: 3px;background: #0f3460;outline: none;-webkit-appearance: none;}input[type="range"]::-webkit-slider-thumb {-webkit-appearance: none;width: 16px;height: 16px;border-radius: 50%;background: #00d9ff;cursor: pointer;}input[type="file"] {width: 100%;padding: 10px;background: #0f3460;border: 1px solid #00d9ff;border-radius: 5px;color: #eee;cursor: pointer;}button {width: 100%;padding: 10px;margin-top: 10px;background: #00d9ff;border: none;border-radius: 5px;color: #16213e;font-weight: bold;cursor: pointer;transition: all 0.3s;}button:hover {background: #00b8d4;transform: translateY(-2px);box-shadow: 0 4px 8px rgba(0, 217, 255, 0.3);}button:disabled {background: #555;cursor: not-allowed;transform: none;}.value-display {display: inline-block;float: right;color: #00d9ff;font-weight: bold;}.stats {background: #0f3460;padding: 15px;border-radius: 5px;margin-top: 20px;}.stats div {margin: 8px 0;font-size: 13px;}.stats .stat-label {color: #aaa;}.stats .stat-value {color: #00d9ff;font-weight: bold;float: right;}svg {width: 100%;height: 100%;background: #1a1a2e;}.node {cursor: move;transition: all 0.2s;}.node circle {fill: #00d9ff;stroke: #fff;stroke-width: 2px;transition: all 0.3s;}.node:hover circle {fill: #ff6b6b;r: 14;}.node.highlighted circle {fill: #ffd700;r: 16;stroke-width: 3px;}.node text {font-size: 11px;fill: #eee;pointer-events: none;text-anchor: middle;}.link {stroke: #555;stroke-opacity: 0.6;cursor: pointer;transition: all 0.3s;}.link:hover {stroke: #00d9ff;stroke-opacity: 1;stroke-width: 3px;}.link.selected {stroke: #ff6b6b;stroke-opacity: 1;}.link.highlighted {stroke: #ffd700;stroke-opacity: 1;stroke-width: 4px;}.mode-indicator {position: absolute;top: 20px;left: 20px;background: rgba(22, 33, 62, 0.9);padding: 10px 20px;border-radius: 5px;font-size: 14px;border: 2px solid #00d9ff;}.instructions {background: #0f3460;padding: 15px;border-radius: 5px;margin-top: 20px;font-size: 12px;line-height: 1.8;}.instructions h3 {color: #00d9ff;margin-bottom: 10px;font-size: 14px;}.instructions ul {list-style: none;padding-left: 0;}.instructions li {margin: 5px 0;color: #aaa;}.instructions li:before {content: "▸ ";color: #00d9ff;}#info-tooltip {position: absolute;background: rgba(22, 33, 62, 0.95);padding: 10px 15px;border-radius: 5px;pointer-events: none;display: none;border: 1px solid #00d9ff;font-size: 12px;max-width: 200px;}.clear-float::after {content: "";display: table;clear: both;}.list-section {background: #0f3460;border-radius: 5px;margin-top: 20px;overflow: hidden;}.list-header {background: #16213e;padding: 12px 15px;cursor: pointer;display: flex;justify-content: space-between;align-items: center;border-bottom: 1px solid #00d9ff;}.list-header:hover {background: #1a2845;}.list-header h3 {color: #00d9ff;font-size: 14px;margin: 0;}.list-header .toggle-icon {color: #00d9ff;font-size: 12px;transition: transform 0.3s;}.list-header .toggle-icon.collapsed {transform: rotate(-90deg);}.list-content {max-height: 300px;overflow-y: auto;padding: 10px;}.list-content.collapsed {display: none;}.list-item {padding: 8px 10px;margin: 5px 0;background: #16213e;border-radius: 3px;font-size: 12px;display: flex;justify-content: space-between;align-items: center;transition: background 0.2s;cursor: pointer;}.list-item:hover {background: #1a2845;}.list-item.highlighted {background: #00d9ff;color: #16213e;}.list-item.highlighted .item-name,.list-item.highlighted .item-value {color: #16213e;}.list-item .item-name {color: #eee;flex: 1;}.list-item .item-value {color: #00d9ff;font-weight: bold;margin-left: 10px;}.list-item.positive .item-value {color: #4caf50;}.list-item.negative .item-value {color: #ff6b6b;}.search-box {width: 100%;padding: 8px;margin: 5px 0;background: #16213e;border: 1px solid #00d9ff;border-radius: 3px;color: #eee;font-size: 12px;}.search-box:focus {outline: none;border-color: #00b8d4;}.list-empty {text-align: center;color: #aaa;padding: 20px;font-size: 12px;}.list-content::-webkit-scrollbar {width: 6px;}.list-content::-webkit-scrollbar-track {background: #16213e;}.list-content::-webkit-scrollbar-thumb {background: #00d9ff;border-radius: 3px;}.list-content::-webkit-scrollbar-thumb:hover {background: #00b8d4;}.restore-btn {width: auto;min-width: 40px;padding: 5px 10px;margin: 0;background: #4caf50;border: none;border-radius: 3px;color: white;font-size: 18px;font-weight: bold;cursor: pointer;transition: all 0.2s;}.restore-btn:hover {background: #45a049;transform: scale(1.1);}.deleted-item {align-items: flex-start;}.allocation-section {background: #0f3460;padding: 15px;border-radius: 5px;margin-top: 20px;}.allocation-section h3 {color: #00d9ff;margin-bottom: 15px;font-size: 14px;}.allocation-stats {margin-bottom: 15px;}.allocation-stats div {margin: 8px 0;font-size: 13px;}.allocation-input {width: 80px;padding: 4px 6px;background: #16213e;border: 1px solid #00d9ff;border-radius: 3px;color: #eee;font-size: 12px;text-align: right;}.allocation-input:focus {outline: none;border-color: #00b8d4;}.allocation-input.warning {border-color: #ff9800;}.allocation-input.error {border-color: #ff6b6b;}.allocation-buttons {display: flex;gap: 10px;margin-top: 10px;}.allocation-buttons button {flex: 1;padding: 8px;margin: 0;font-size: 12px;}.node.has-allocation circle {stroke: #ffd700;stroke-width: 3px;}.node-allocation-label {font-size: 10px;fill: #ffd700;font-weight: bold;text-anchor: middle;}#detail-panel {position: absolute;top: 20px;right: 20px;width: 400px;max-height: 80vh;background: rgba(22, 33, 62, 0.98);border: 2px solid #00d9ff;border-radius: 8px;padding: 20px;display: none;overflow-y: auto;box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);z-index: 1000;}#detail-panel::-webkit-scrollbar {width: 6px;}#detail-panel::-webkit-scrollbar-track {background: #16213e;}#detail-panel::-webkit-scrollbar-thumb {background: #00d9ff;border-radius: 3px;}.detail-header {display: flex;justify-content: space-between;align-items: center;margin-bottom: 15px;padding-bottom: 10px;border-bottom: 2px solid #00d9ff;}.detail-header h2 {color: #00d9ff;font-size: 18px;margin: 0;}.close-btn {background: none;border: none;color: #ff6b6b;font-size: 24px;cursor: pointer;padding: 0;width: 30px;height: 30px;line-height: 30px;text-align: center;border-radius: 50%;transition: all 0.3s;}.close-btn:hover {background: #ff6b6b;color: #fff;transform: rotate(90deg);}.detail-section {margin-bottom: 15px;}.detail-section h3 {color: #00d9ff;font-size: 14px;margin-bottom: 10px;}.detail-row {display: flex;justify-content: space-between;padding: 6px 0;border-bottom: 1px solid #0f3460;font-size: 13px;}.detail-row:last-child {border-bottom: none;}.detail-label {color: #aaa;font-weight: 500;}.detail-value {color: #eee;text-align: right;max-width: 60%;word-break: break-all;}.detail-value.positive {color: #4caf50;}.detail-value.negative {color: #ff6b6b;}.detail-code {background: #0f3460;padding: 10px;border-radius: 5px;font-family: 'Courier New', monospace;font-size: 11px;color: #eee;max-height: 200px;overflow-y: auto;word-break: break-all;white-space: pre-wrap;}</style></head><body><div id="container"><div id="control-panel"><h1>Alpha相关性网络图</h1><div class="control-group"><label>加载数据文件 (JSON):</label><input type="file" id="fileInput" accept=".json"></div><div class="control-group"><label>相关性阈值: <span class="value-display" id="thresholdValue">0.50</span></label><input type="range" id="threshold" min="0" max="1" step="0.01" value="0.5"></div><div class="control-group"><label>节点距离力: <span class="value-display" id="distanceValue">20</span></label><input type="range" id="linkDistance" min="5" max="500" step="5" value="20"></div><div class="control-group"><label>节点排斥力: <span class="value-display" id="chargeValue">-50</span></label><input type="range" id="chargeStrength" min="-600" max="-10" step="5" value="-50"></div><div class="control-group"><button id="addLinkBtn">连线模式: OFF</button><button id="removeLinkBtn">删除连线模式: OFF</button><button id="removeNodeBtn">删除节点模式: OFF</button><button id="resetBtn">重置布局</button></div><div class="stats"><div class="clear-float"><span class="stat-label">节点数量:</span><span class="stat-value" id="nodeCount">0</span></div><div class="clear-float"><span class="stat-label">连线数量:</span><span class="stat-value" id="linkCount">0</span></div><div class="clear-float"><span class="stat-label">当前区域:</span><span class="stat-value" id="regionInfo">-</span></div></div><div class="allocation-section"><h3>点数分配</h3><div class="allocation-stats"><div class="clear-float"><span class="stat-label">总点数:</span><span class="stat-value" id="totalPoints">100,000</span></div><div class="clear-float"><span class="stat-label">已分配:</span><span class="stat-value" id="allocatedPoints">0</span></div><div class="clear-float"><span class="stat-label">剩余:</span><span class="stat-value" id="remainingPoints">100,000</span></div></div><div class="allocation-buttons"><button id="saveAllocationBtn">保存分配</button><button id="loadAllocationBtn">加载分配</button></div><div class="allocation-buttons"><button id="clearAllocationBtn" style="background: #ff6b6b;">清空分配</button><button id="autoAllocateBtn" style="background: #4caf50;">平均分配</button></div><div class="allocation-buttons"><button id="clusterAllocateBtn" style="background: #9c27b0;">按簇分配</button></div><input type="file" id="allocationFileInput" accept=".json" style="display: none;"></div><!-- 簇信息列表 --><div class="list-section" id="clusterSection" style="display: none;"><div class="list-header" onclick="toggleList('clusterList')"><h3>簇信息 (阈值: <span id="clusterThreshold">0.50</span>)</h3><span class="toggle-icon" id="clusterListIcon">▼</span></div><div class="list-content" id="clusterList"><div id="clusterInfo"></div></div></div><div class="instructions"><h3>操作说明</h3><ul><li>拖动节点改变位置</li><li>鼠标悬停查看详情</li><li>点击连线模式后，点击两个节点添加连线</li><li>点击删除模式后，点击连线删除</li><li>调整阈值过滤显示的连线</li><li>滚轮缩放，拖动画布平移</li><li>在Alpha列表中输入点数进行分配</li></ul></div><!-- Alpha列表 --><div class="list-section"><div class="list-header" onclick="toggleList('alphaList')"><h3>Alpha列表</h3><span class="toggle-icon" id="alphaListIcon">▼</span></div><div class="list-content" id="alphaList"><input type="text" class="search-box" id="alphaSearch" placeholder="搜索Alpha ID..."><div id="alphaListContent"><div class="list-empty">未加载数据</div></div></div></div><!-- 连线列表 --><div class="list-section"><div class="list-header" onclick="toggleList('linkList')"><h3>连线信息 (按相关性排序)</h3><span class="toggle-icon" id="linkListIcon">▼</span></div><div class="list-content" id="linkList"><input type="text" class="search-box" id="linkSearch" placeholder="搜索Alpha ID..."><div id="linkListContent"><div class="list-empty">未加载数据</div></div></div></div><!-- 已删除节点列表 --><div class="list-section"><div class="list-header" onclick="toggleList('deletedNodesList')"><h3>已删除节点</h3><span class="toggle-icon collapsed" id="deletedNodesListIcon">▼</span></div><div class="list-content collapsed" id="deletedNodesList"><div id="deletedNodesContent"><div class="list-empty">无已删除节点</div></div></div></div></div><div id="graph-container"><div class="mode-indicator" id="modeIndicator">正常模式</div><svg id="network"></svg><div id="info-tooltip"></div><!-- Alpha详细信息面板 --><div id="detail-panel"><div class="detail-header"><h2 id="detailAlphaId">Alpha 详情</h2><button class="close-btn" onclick="closeDetailPanel()">×</button></div><div id="detailContent"></div></div></div></div><script>// 全局变量let graphData = { nodes: [], links: [] };let originalData = { nodes: [], links: [] };let deletedNodes = []; // 记录已删除的节点let simulation;let svg, g, link, node;let zoom; // 保存zoom引用let mode = 'normal'; // 'normal', 'addLink', 'removeLink', 'removeNode'let selectedNode = null;let currentThreshold = 0.5;// 点数分配相关let allocations = {}; // { alphaId: points }const TOTAL_POINTS = 100000;let clusters = []; // 存储簇信息// 初始化SVGfunction initSVG() {const container = d3.select('#graph-container');const width = container.node().clientWidth;const height = container.node().clientHeight;svg = d3.select('#network').attr('width', width).attr('height', height);// 添加缩放和平移zoom = d3.zoom().scaleExtent([0.1, 4]).on('zoom', (event) => {g.attr('transform', event.transform);});svg.call(zoom);g = svg.append('g');// 添加连线组和节点组g.append('g').attr('class', 'links');g.append('g').attr('class', 'nodes');}// 初始化力导向图function initSimulation() {const width = svg.node().clientWidth;const height = svg.node().clientHeight;simulation = d3.forceSimulation().force('link', d3.forceLink().id(d => d.id).distance(20)).force('charge', d3.forceManyBody().strength(-50)).force('center', d3.forceCenter(width / 2, height / 2)).force('collision', d3.forceCollide().radius(20)).force('x', d3.forceX(width / 2).strength(0.05)).force('y', d3.forceY(height / 2).strength(0.05));}// 更新图形function updateGraph() {// 过滤连线const filteredLinks = originalData.links.filter(l =>Math.abs(l.correlation) >= currentThreshold);graphData = {nodes: originalData.nodes.map(n => ({...n})),links: filteredLinks.map(l => ({...l}))};// 更新连线link = g.select('.links').selectAll('line').data(graphData.links, d => `${d.source.id || d.source}-${d.target.id || d.target}`);link.exit().remove();const linkEnter = link.enter().append('line').attr('class', 'link').attr('stroke-width', d => Math.abs(d.correlation) * 3).on('click', onLinkClick).on('mouseover', showLinkTooltip).on('mouseout', hideTooltip);link = linkEnter.merge(link);// 更新节点node = g.select('.nodes').selectAll('g').data(graphData.nodes, d => d.id);node.exit().remove();const nodeEnter = node.enter().append('g').attr('class', 'node').call(d3.drag().on('start', dragstarted).on('drag', dragged).on('end', dragended)).on('click', onNodeClick).on('mouseover', showNodeTooltip).on('mouseout', hideTooltip);nodeEnter.append('circle').attr('r', 10);nodeEnter.append('text').attr('dy', 25).text(d => d.name);// 添加点数标签nodeEnter.append('text').attr('class', 'node-allocation-label').attr('dy', -15);node = nodeEnter.merge(node);// 更新节点样式和点数标签node.classed('has-allocation', d => allocations[d.id] > 0);node.select('.node-allocation-label').text(d => allocations[d.id] ? allocations[d.id].toLocaleString() : '');// 更新力导向图simulation.nodes(graphData.nodes);simulation.force('link').links(graphData.links);simulation.alpha(1).restart();simulation.on('tick', () => {link.attr('x1', d => d.source.x).attr('y1', d => d.source.y).attr('x2', d => d.target.x).attr('y2', d => d.target.y);node.attr('transform', d => `translate(${d.x},${d.y})`);});updateStats();updateAlphaList();updateLinkList();}// 节点拖拽function dragstarted(event, d) {if (!event.active) simulation.alphaTarget(0.3).restart();d.fx = d.x;d.fy = d.y;}function dragged(event, d) {d.fx = event.x;d.fy = event.y;}function dragended(event, d) {if (!event.active) simulation.alphaTarget(0);}// 节点点击事件function onNodeClick(event, d) {event.stopPropagation();if (mode === 'addLink') {if (!selectedNode) {selectedNode = d;d3.select(this).select('circle').style('fill', '#ffd700');updateModeIndicator(`已选择: ${d.name}，请选择第二个节点`);} else if (selectedNode.id !== d.id) {// 添加新连线addLink(selectedNode, d);// 重置选择node.selectAll('circle').style('fill', '#00d9ff');selectedNode = null;updateModeIndicator('连线模式: 选择两个节点以添加连线');}} else if (mode === 'removeNode') {// 删除节点removeNode(d);} else {// 正常模式，显示详细信息showDetailPanel(d);}}// 连线点击事件function onLinkClick(event, d) {event.stopPropagation();if (mode === 'removeLink') {removeLink(d);}}// 添加连线function addLink(source, target) {const existingLink = originalData.links.find(l =>(l.source === source.id && l.target === target.id) ||(l.source === target.id && l.target === source.id));if (!existingLink) {originalData.links.push({source: source.id,target: target.id,correlation: 0.5,value: 0.5});updateGraph();}}// 删除连线function removeLink(link) {const sourceId = link.source.id || link.source;const targetId = link.target.id || link.target;originalData.links = originalData.links.filter(l => {const lSource = l.source.id || l.source;const lTarget = l.target.id || l.target;return !((lSource === sourceId && lTarget === targetId) ||(lSource === targetId && lTarget === sourceId));});updateGraph();}// 删除节点function removeNode(nodeToRemove) {const nodeId = nodeToRemove.id;// 找到要删除的节点const nodeData = originalData.nodes.find(n => n.id === nodeId);if (!nodeData) return;// 找到与该节点相关的连线const relatedLinks = originalData.links.filter(l => {const sourceId = l.source.id || l.source;const targetId = l.target.id || l.target;return sourceId === nodeId || targetId === nodeId;});// 保存到deletedNodes数组deletedNodes.push({node: {...nodeData},links: relatedLinks.map(l => ({source: l.source.id || l.source,target: l.target.id || l.target,correlation: l.correlation,value: l.value})),deletedAt: new Date().toLocaleString()});// 删除与该节点相关的所有连线originalData.links = originalData.links.filter(l => {const sourceId = l.source.id || l.source;const targetId = l.target.id || l.target;return sourceId !== nodeId && targetId !== nodeId;});// 删除节点originalData.nodes = originalData.nodes.filter(n => n.id !== nodeId);updateGraph();updateDeletedNodesList();}// 恢复节点function restoreNode(index) {if (index < 0 || index >= deletedNodes.length) return;const deletedItem = deletedNodes[index];// 检查节点是否已存在if (originalData.nodes.find(n => n.id === deletedItem.node.id)) {alert('该节点已存在！');return;}// 恢复节点originalData.nodes.push({...deletedItem.node});// 恢复连线（只恢复两端节点都存在的连线）deletedItem.links.forEach(link => {const sourceExists = originalData.nodes.find(n => n.id === link.source);const targetExists = originalData.nodes.find(n => n.id === link.target);if (sourceExists && targetExists) {// 检查连线是否已存在const linkExists = originalData.links.find(l => {const lSource = l.source.id || l.source;const lTarget = l.target.id || l.target;return (lSource === link.source && lTarget === link.target) ||(lSource === link.target && lTarget === link.source);});if (!linkExists) {originalData.links.push({...link});}}});// 从deletedNodes中移除deletedNodes.splice(index, 1);updateGraph();updateDeletedNodesList();}// 定位并高亮节点function locateNode(nodeId) {// 移除所有高亮if (node) {node.classed('highlighted', false);}if (link) {link.classed('highlighted', false);}d3.selectAll('.list-item').classed('highlighted', false);// 查找目标节点const targetNode = graphData.nodes.find(n => n.id === nodeId);if (!targetNode) {console.log('节点未找到:', nodeId);return;}// 确保节点有位置信息if (targetNode.x === undefined || targetNode.y === undefined) {console.log('节点位置未初始化');return;}// 高亮节点if (node) {node.filter(d => d.id === nodeId).classed('highlighted', true);}// 计算缩放和平移const width = svg.node().clientWidth;const height = svg.node().clientHeight;const scale = 2.0;const x = width / 2 - targetNode.x * scale;const y = height / 2 - targetNode.y * scale;// 应用平滑过渡svg.transition().duration(750).call(zoom.transform,d3.zoomIdentity.translate(x, y).scale(scale));// 3秒后移除高亮setTimeout(() => {if (node) {node.classed('highlighted', false);}}, 3000);}// 定位并高亮连线function locateLink(sourceId, targetId) {// 移除所有高亮if (node) {node.classed('highlighted', false);}if (link) {link.classed('highlighted', false);}d3.selectAll('.list-item').classed('highlighted', false);// 查找两个节点const sourceNode = graphData.nodes.find(n => n.id === sourceId);const targetNode = graphData.nodes.find(n => n.id === targetId);if (!sourceNode || !targetNode) {console.log('节点未找到:', sourceId, targetId);return;}// 确保节点有位置信息if (sourceNode.x === undefined || targetNode.x === undefined) {console.log('节点位置未初始化');return;}// 高亮两个节点if (node) {node.filter(d => d.id === sourceId || d.id === targetId).classed('highlighted', true);}// 高亮连线if (link) {link.filter(l => {const lSource = l.source.id || l.source;const lTarget = l.target.id || l.target;return (lSource === sourceId && lTarget === targetId) ||(lSource === targetId && lTarget === sourceId);}).classed('highlighted', true);}// 计算两个节点的中心点const centerX = (sourceNode.x + targetNode.x) / 2;const centerY = (sourceNode.y + targetNode.y) / 2;// 计算缩放和平移const width = svg.node().clientWidth;const height = svg.node().clientHeight;const scale = 2.0;const x = width / 2 - centerX * scale;const y = height / 2 - centerY * scale;// 应用平滑过渡svg.transition().duration(750).call(zoom.transform,d3.zoomIdentity.translate(x, y).scale(scale));// 3秒后移除高亮setTimeout(() => {if (node) {node.classed('highlighted', false);}if (link) {link.classed('highlighted', false);}}, 3000);}// 显示提示信息function showNodeTooltip(event, d) {const tooltip = d3.select('#info-tooltip');tooltip.style('display', 'block').html(`<strong>${d.id}</strong>`).style('left', (event.pageX + 10) + 'px').style('top', (event.pageY - 10) + 'px');}function showLinkTooltip(event, d) {const tooltip = d3.select('#info-tooltip');const sourceId = d.source.id || d.source;const targetId = d.target.id || d.target;tooltip.style('display', 'block').html(`<strong>相关性</strong><br>${sourceId} ↔ ${targetId}<br>系数: ${d.correlation.toFixed(4)}`).style('left', (event.pageX + 10) + 'px').style('top', (event.pageY - 10) + 'px');}function hideTooltip() {d3.select('#info-tooltip').style('display', 'none');}// 显示Alpha详细信息面板function showDetailPanel(nodeData) {const panel = document.getElementById('detail-panel');const titleElement = document.getElementById('detailAlphaId');const contentElement = document.getElementById('detailContent');titleElement.textContent = `Alpha: ${nodeData.id}`;// 构建详细信息 HTMLlet html = '';// 基本信息html += '<div class="detail-section">';html += '<h3>基本信息</h3>';if (nodeData.create_dt) {html += `<div class="detail-row"><span class="detail-label">创建时间:</span><span class="detail-value">${nodeData.create_dt}</span></div>`;}if (nodeData.region) {html += `<div class="detail-row"><span class="detail-label">Region:</span><span class="detail-value">${nodeData.region}</span></div>`;}if (nodeData.universe) {html += `<div class="detail-row"><span class="detail-label">Universe:</span><span class="detail-value">${nodeData.universe}</span></div>`;}if (nodeData.delay !== null && nodeData.delay !== undefined) {html += `<div class="detail-row"><span class="detail-label">Delay:</span><span class="detail-value">${nodeData.delay}</span></div>`;}if (nodeData.decay !== null && nodeData.decay !== undefined) {html += `<div class="detail-row"><span class="detail-label">Decay:</span><span class="detail-value">${nodeData.decay}</span></div>`;}if (nodeData.neutralization) {html += `<div class="detail-row"><span class="detail-label">Neutralization:</span><span class="detail-value">${nodeData.neutralization}</span></div>`;}if (nodeData.operatorCount !== null && nodeData.operatorCount !== undefined) {html += `<div class="detail-row"><span class="detail-label">操作符数量:</span><span class="detail-value">${nodeData.operatorCount}</span></div>`;}html += '</div>';// 性能指标html += '<div class="detail-section">';html += '<h3>性能指标</h3>';if (nodeData.sharpe !== null && nodeData.sharpe !== undefined) {const sharpeClass = nodeData.sharpe > 0 ? 'positive' : (nodeData.sharpe < 0 ? 'negative' : '');html += `<div class="detail-row"><span class="detail-label">Sharpe:</span><span class="detail-value ${sharpeClass}">${nodeData.sharpe?.toFixed(4) || '-'}</span></div>`;}if (nodeData.fitness !== null && nodeData.fitness !== undefined) {const fitnessClass = nodeData.fitness > 0 ? 'positive' : (nodeData.fitness < 0 ? 'negative' : '');html += `<div class="detail-row"><span class="detail-label">Fitness:</span><span class="detail-value ${fitnessClass}">${nodeData.fitness?.toFixed(4) || '-'}</span></div>`;}if (nodeData.returns !== null && nodeData.returns !== undefined) {const returnsClass = nodeData.returns > 0 ? 'positive' : (nodeData.returns < 0 ? 'negative' : '');html += `<div class="detail-row"><span class="detail-label">Returns:</span><span class="detail-value ${returnsClass}">${nodeData.returns?.toFixed(4) || '-'}</span></div>`;}if (nodeData.turnover !== null && nodeData.turnover !== undefined) {html += `<div class="detail-row"><span class="detail-label">Turnover:</span><span class="detail-value">${nodeData.turnover?.toFixed(4) || '-'}</span></div>`;}if (nodeData.margin !== null && nodeData.margin !== undefined) {html += `<div class="detail-row"><span class="detail-label">Margin:</span><span class="detail-value">${nodeData.margin?.toFixed(4) || '-'}</span></div>`;}if (nodeData.drawdown !== null && nodeData.drawdown !== undefined) {const drawdownClass = nodeData.drawdown < 0 ? 'negative' : '';html += `<div class="detail-row"><span class="detail-label">Drawdown:</span><span class="detail-value ${drawdownClass}">${nodeData.drawdown?.toFixed(4) || '-'}</span></div>`;}if (nodeData.longCount !== null && nodeData.longCount !== undefined) {html += `<div class="detail-row"><span class="detail-label">Long Count:</span><span class="detail-value">${nodeData.longCount?.toFixed(2) || '-'}</span></div>`;}if (nodeData.shortCount !== null && nodeData.shortCount !== undefined) {html += `<div class="detail-row"><span class="detail-label">Short Count:</span><span class="detail-value">${nodeData.shortCount?.toFixed(2) || '-'}</span></div>`;}html += '</div>';// 点数分配if (allocations[nodeData.id]) {html += '<div class="detail-section">';html += '<h3>点数分配</h3>';html += `<div class="detail-row"><span class="detail-label">已分配点数:</span><span class="detail-value positive">${allocations[nodeData.id].toLocaleString()}</span></div>`;html += '</div>';}// 表达式if (nodeData.code) {html += '<div class="detail-section">';html += '<h3>表达式</h3>';html += `<div class="detail-code">${nodeData.code}</div>`;html += '</div>';}contentElement.innerHTML = html;panel.style.display = 'block';}// 关闭详细信息面板function closeDetailPanel() {document.getElementById('detail-panel').style.display = 'none';}// 更新统计信息function updateStats() {document.getElementById('nodeCount').textContent = graphData.nodes.length;document.getElementById('linkCount').textContent = graphData.links.length;}// 更新模式指示器function updateModeIndicator(text) {document.getElementById('modeIndicator').textContent = text;}// 切换列表显示function toggleList(listId) {const list = document.getElementById(listId);const icon = document.getElementById(listId + 'Icon');if (list.classList.contains('collapsed')) {list.classList.remove('collapsed');icon.classList.remove('collapsed');} else {list.classList.add('collapsed');icon.classList.add('collapsed');}}// 更新Alpha列表function updateAlphaList() {const container = document.getElementById('alphaListContent');if (originalData.nodes.length === 0) {container.innerHTML = '<div class="list-empty">未加载数据</div>';return;}const searchTerm = document.getElementById('alphaSearch').value.toLowerCase();const filteredNodes = originalData.nodes.filter(n =>n.id.toLowerCase().includes(searchTerm));if (filteredNodes.length === 0) {container.innerHTML = '<div class="list-empty">未找到匹配的Alpha</div>';return;}container.innerHTML = filteredNodes.sort((a, b) => a.id.localeCompare(b.id)).map(node => `<div class="list-item" onclick="event.target.tagName !== 'INPUT' && locateNode('${node.id}')"><span class="item-name">${node.id}</span><input type="number"class="allocation-input"value="${allocations[node.id] || 0}"min="0"max="${TOTAL_POINTS}"placeholder="0"onchange="updateAllocation('${node.id}', this.value)"onclick="event.stopPropagation()"></div>`).join('');}// 更新连线列表function updateLinkList() {const container = document.getElementById('linkListContent');if (graphData.links.length === 0) {container.innerHTML = '<div class="list-empty">当前阈值下无连线</div>';return;}const searchTerm = document.getElementById('linkSearch').value.toLowerCase();const filteredLinks = graphData.links.filter(l => {const sourceId = (l.source.id || l.source).toLowerCase();const targetId = (l.target.id || l.target).toLowerCase();return sourceId.includes(searchTerm) || targetId.includes(searchTerm);});if (filteredLinks.length === 0) {container.innerHTML = '<div class="list-empty">未找到匹配的连线</div>';return;}// 按相关性绝对值排序const sortedLinks = filteredLinks.sort((a, b) =>Math.abs(b.correlation) - Math.abs(a.correlation));container.innerHTML = sortedLinks.map(link => {const sourceId = link.source.id || link.source;const targetId = link.target.id || link.target;const corr = link.correlation;const className = corr > 0 ? 'positive' : 'negative';return `<div class="list-item ${className}" onclick="locateLink('${sourceId}', '${targetId}')"><span class="item-name">${sourceId} ↔ ${targetId}</span><span class="item-value">${corr.toFixed(4)}</span></div>`;}).join('');}// 更新已删除节点列表function updateDeletedNodesList() {const container = document.getElementById('deletedNodesContent');if (deletedNodes.length === 0) {container.innerHTML = '<div class="list-empty">无已删除节点</div>';return;}container.innerHTML = deletedNodes.map((item, index) => `<div class="list-item deleted-item"><div style="flex: 1;"><div class="item-name">${item.node.id}</div><div style="font-size: 10px; color: #888; margin-top: 2px;">${item.deletedAt} | ${item.links.length}条连线</div></div><button class="restore-btn" onclick="restoreNode(${index})" title="恢复节点">↻</button></div>`).join('');}// 控制面板事件document.getElementById('fileInput').addEventListener('change', function(e) {const file = e.target.files[0];if (file) {const reader = new FileReader();reader.onload = function(event) {try {const data = JSON.parse(event.target.result);originalData = {nodes: data.nodes.map(n => ({...n})),links: data.links.map(l => ({...l}))};document.getElementById('regionInfo').textContent = data.region || '-';updateGraph();} catch (err) {alert('文件解析失败: ' + err.message);}};reader.readAsText(file);}});document.getElementById('threshold').addEventListener('input', function(e) {currentThreshold = parseFloat(e.target.value);document.getElementById('thresholdValue').textContent = currentThreshold.toFixed(2);updateGraph();});document.getElementById('linkDistance').addEventListener('input', function(e) {const value = parseInt(e.target.value);document.getElementById('distanceValue').textContent = value;simulation.force('link').distance(value);simulation.alpha(1).restart();});document.getElementById('chargeStrength').addEventListener('input', function(e) {const value = parseInt(e.target.value);document.getElementById('chargeValue').textContent = value;simulation.force('charge').strength(value);simulation.alpha(1).restart();});document.getElementById('addLinkBtn').addEventListener('click', function() {if (mode === 'addLink') {mode = 'normal';this.textContent = '连线模式: OFF';this.style.background = '#00d9ff';selectedNode = null;if (node) node.selectAll('circle').style('fill', '#00d9ff');updateModeIndicator('正常模式');} else {mode = 'addLink';this.textContent = '连线模式: ON';this.style.background = '#4caf50';document.getElementById('removeLinkBtn').textContent = '删除连线模式: OFF';document.getElementById('removeLinkBtn').style.background = '#00d9ff';document.getElementById('removeNodeBtn').textContent = '删除节点模式: OFF';document.getElementById('removeNodeBtn').style.background = '#00d9ff';updateModeIndicator('连线模式: 选择两个节点以添加连线');}});document.getElementById('removeLinkBtn').addEventListener('click', function() {if (mode === 'removeLink') {mode = 'normal';this.textContent = '删除连线模式: OFF';this.style.background = '#00d9ff';updateModeIndicator('正常模式');} else {mode = 'removeLink';this.textContent = '删除连线模式: ON';this.style.background = '#ff6b6b';document.getElementById('addLinkBtn').textContent = '连线模式: OFF';document.getElementById('addLinkBtn').style.background = '#00d9ff';document.getElementById('removeNodeBtn').textContent = '删除节点模式: OFF';document.getElementById('removeNodeBtn').style.background = '#00d9ff';selectedNode = null;if (node) node.selectAll('circle').style('fill', '#00d9ff');updateModeIndicator('删除连线模式: 点击连线以删除');}});document.getElementById('removeNodeBtn').addEventListener('click', function() {if (mode === 'removeNode') {mode = 'normal';this.textContent = '删除节点模式: OFF';this.style.background = '#00d9ff';updateModeIndicator('正常模式');} else {mode = 'removeNode';this.textContent = '删除节点模式: ON';this.style.background = '#ff9800';document.getElementById('addLinkBtn').textContent = '连线模式: OFF';document.getElementById('addLinkBtn').style.background = '#00d9ff';document.getElementById('removeLinkBtn').textContent = '删除连线模式: OFF';document.getElementById('removeLinkBtn').style.background = '#00d9ff';selectedNode = null;if (node) node.selectAll('circle').style('fill', '#00d9ff');updateModeIndicator('删除节点模式: 点击节点以删除');}});document.getElementById('resetBtn').addEventListener('click', function() {if (node) {node.each(d => {d.fx = null;d.fy = null;});simulation.alpha(1).restart();}});// 点数分配相关函数function updateAllocation(alphaId, value) {const points = parseInt(value) || 0;allocations[alphaId] = points;updateAllocationStats();updateGraph();}function updateAllocationStats() {const allocated = Object.values(allocations).reduce((sum, val) => sum + val, 0);const remaining = TOTAL_POINTS - allocated;document.getElementById('allocatedPoints').textContent = allocated.toLocaleString();document.getElementById('remainingPoints').textContent = remaining.toLocaleString();// 更新颜色提示const remainingElement = document.getElementById('remainingPoints');if (remaining < 0) {remainingElement.style.color = '#ff6b6b';} else if (remaining === 0) {remainingElement.style.color = '#4caf50';} else {remainingElement.style.color = '#00d9ff';}}function saveAllocation() {const allocationData = {totalPoints: TOTAL_POINTS,allocatedPoints: Object.values(allocations).reduce((sum, val) => sum + val, 0),timestamp: new Date().toISOString(),region: document.getElementById('regionInfo').textContent,allocations: allocations,details: originalData.nodes.map(node => ({alphaId: node.id,alphaName: node.name,points: allocations[node.id] || 0})).filter(item => item.points > 0)};const blob = new Blob([JSON.stringify(allocationData, null, 2)], { type: 'application/json' });const url = URL.createObjectURL(blob);const a = document.createElement('a');a.href = url;a.download = `alpha_allocation_${allocationData.region}_${Date.now()}.json`;a.click();URL.revokeObjectURL(url);alert(`分配方案已保存！\n已分配: ${allocationData.allocatedPoints.toLocaleString()}\n共 ${allocationData.details.length} 个Alpha`);}function loadAllocation(data) {if (data.allocations) {allocations = {...data.allocations};// 检查是否是按簇分配的数据（通过检查是否有明显的簇结构）// 重新计算簇信息以便显示if (originalData.nodes.length > 0) {clusters = findClusters();if (clusters.length > 1 || (clusters.length === 1 && clusters[0].length < originalData.nodes.length)) {displayClusterInfo();}}updateAllocationStats();updateGraph();updateAlphaList();alert(`分配方案已加载！\n已分配: ${Object.values(allocations).reduce((sum, val) => sum + val, 0).toLocaleString()}`);}}function clearAllocation() {if (confirm('确定要清空所有点数分配吗？')) {allocations = {};updateAllocationStats();updateGraph();updateAlphaList();hideClusterInfo();}}function autoAllocatePoints() {const nodeCount = originalData.nodes.length;if (nodeCount === 0) {alert('请先加载Alpha数据！');return;}if (confirm(`将 ${TOTAL_POINTS.toLocaleString()} 点数平均分配给 ${nodeCount} 个Alpha？\n每个约 ${Math.floor(TOTAL_POINTS / nodeCount).toLocaleString()} 点`)) {allocations = {};const pointsPerNode = Math.floor(TOTAL_POINTS / nodeCount);let remaining = TOTAL_POINTS - (pointsPerNode * nodeCount);originalData.nodes.forEach((node, index) => {allocations[node.id] = pointsPerNode + (index < remaining ? 1 : 0);});updateAllocationStats();updateGraph();updateAlphaList();}}// 使用并查集检测连通分量（簇）function findClusters() {if (originalData.nodes.length === 0) {return [];}// 构建当前阈值下的邻接表const adjacencyList = {};originalData.nodes.forEach(node => {adjacencyList[node.id] = [];});// 只考虑满足当前阈值的连线originalData.links.forEach(link => {if (Math.abs(link.correlation) >= currentThreshold) {const sourceId = link.source.id || link.source;const targetId = link.target.id || link.target;adjacencyList[sourceId].push(targetId);adjacencyList[targetId].push(sourceId);}});// DFS查找连通分量const visited = {};const clusters = [];function dfs(nodeId, cluster) {visited[nodeId] = true;cluster.push(nodeId);adjacencyList[nodeId].forEach(neighborId => {if (!visited[neighborId]) {dfs(neighborId, cluster);}});}originalData.nodes.forEach(node => {if (!visited[node.id]) {const cluster = [];dfs(node.id, cluster);clusters.push(cluster);}});// 按簇大小降序排序clusters.sort((a, b) => b.length - a.length);return clusters;}// 按簇分配点数function clusterAllocatePoints() {if (originalData.nodes.length === 0) {alert('请先加载Alpha数据！');return;}// 检测簇clusters = findClusters();if (clusters.length === 0) {alert('未检测到任何节点！');return;}// 生成簇信息摘要const clusterSummary = clusters.map((cluster, index) =>`簇${index + 1}: ${cluster.length}个节点`).join('\n');const message = `检测到 ${clusters.length} 个簇（当前阈值: ${currentThreshold.toFixed(2)}）\n\n` +clusterSummary +`\n\n将 ${TOTAL_POINTS.toLocaleString()} 点数按簇分配？\n` +`每簇约 ${Math.floor(TOTAL_POINTS / clusters.length).toLocaleString()} 点`;if (confirm(message)) {allocations = {};const pointsPerCluster = Math.floor(TOTAL_POINTS / clusters.length);let remainingPoints = TOTAL_POINTS - (pointsPerCluster * clusters.length);clusters.forEach((cluster, clusterIndex) => {// 给每个簇分配点数（前几个簇多分配1点以用完剩余点数）const clusterPoints = pointsPerCluster + (clusterIndex < remainingPoints ? 1 : 0);// 在簇内平均分配const pointsPerNode = Math.floor(clusterPoints / cluster.length);let clusterRemaining = clusterPoints - (pointsPerNode * cluster.length);cluster.forEach((nodeId, nodeIndex) => {allocations[nodeId] = pointsPerNode + (nodeIndex < clusterRemaining ? 1 : 0);});});updateAllocationStats();updateGraph();updateAlphaList();displayClusterInfo();}}// 显示簇信息function displayClusterInfo() {const clusterSection = document.getElementById('clusterSection');const clusterInfoDiv = document.getElementById('clusterInfo');const clusterThresholdSpan = document.getElementById('clusterThreshold');if (clusters.length === 0) {clusterSection.style.display = 'none';return;}clusterSection.style.display = 'block';clusterThresholdSpan.textContent = currentThreshold.toFixed(2);const clusterDetails = clusters.map((cluster, index) => {const clusterPoints = cluster.reduce((sum, nodeId) => sum + (allocations[nodeId] || 0), 0);const avgPoints = Math.floor(clusterPoints / cluster.length);const nodeList = cluster.slice(0, 5).join(', ') + (cluster.length > 5 ? '...' : '');return `<div class="list-item" style="flex-direction: column; align-items: flex-start;"><div style="width: 100%; display: flex; justify-content: space-between; margin-bottom: 5px;"><span style="color: #00d9ff; font-weight: bold;">簇${index + 1}</span><span style="color: #4caf50;">${clusterPoints.toLocaleString()}点</span></div><div style="font-size: 11px; color: #aaa;">节点数: ${cluster.length} | 平均: ${avgPoints.toLocaleString()}点/节点</div><div style="font-size: 10px; color: #666; margin-top: 3px;">${nodeList}</div></div>`;}).join('');clusterInfoDiv.innerHTML = clusterDetails;}// 隐藏簇信息（当清空或平均分配时）function hideClusterInfo() {document.getElementById('clusterSection').style.display = 'none';clusters = [];}// 点数分配按钮事件document.getElementById('saveAllocationBtn').addEventListener('click', saveAllocation);document.getElementById('loadAllocationBtn').addEventListener('click', function() {document.getElementById('allocationFileInput').click();});document.getElementById('allocationFileInput').addEventListener('change', function(e) {const file = e.target.files[0];if (file) {const reader = new FileReader();reader.onload = function(event) {try {const data = JSON.parse(event.target.result);loadAllocation(data);} catch (err) {alert('文件解析失败: ' + err.message);}};reader.readAsText(file);}e.target.value = ''; // 清空input，允许重复加载同一文件});document.getElementById('clearAllocationBtn').addEventListener('click', clearAllocation);document.getElementById('autoAllocateBtn').addEventListener('click', () => {autoAllocatePoints();hideClusterInfo();});document.getElementById('clusterAllocateBtn').addEventListener('click', clusterAllocatePoints);// 搜索框事件document.getElementById('alphaSearch').addEventListener('input', updateAlphaList);document.getElementById('linkSearch').addEventListener('input', updateLinkList);// 初始化initSVG();initSimulation();// 窗口大小改变时重新调整window.addEventListener('resize', () => {const container = d3.select('#graph-container');const width = container.node().clientWidth;const height = container.node().clientHeight;svg.attr('width', width).attr('height', height);simulation.force('center', d3.forceCenter(width / 2, height / 2));simulation.alpha(1).restart();});</script></body></html>后端代码import pymysqlimport jsonimport numpy as npimport pandas as pdimport osfrom typing import List, Dict, Optional, Tuplefrom datetime import datetimefrom itertools import combinationsDB_CONFIG = {# 京东云ip'host': '111.111.111.111','user': 'root','password': 'root','database': 'root','charset': 'utf8'}class AlphaSubmitDB:"""Alpha提交数据库操作类"""def __init__(self):self.config = DB_CONFIGdef get_connection(self):"""获取数据库连接"""return pymysql.connect(**self.config)def get_by_region(self, region: str, limit: Optional[int] = None) -> List[Dict]:"""根据region获取alpha数据Args:region: 地区代码，如 'USA', 'CHN' 等limit: 限制返回的记录数量，默认返回所有Returns:包含alpha记录的字典列表"""conn = self.get_connection()cursor = conn.cursor(pymysql.cursors.DictCursor)try:sql = "SELECT * FROM alpha_submit WHERE region = %s ORDER BY create_dt DESC"if limit:sql += f" LIMIT {limit}"cursor.execute(sql, (region,))results = cursor.fetchall()return resultsfinally:cursor.close()conn.close()def parse_pnl_data(self, pnl_json: str) -> pd.Series:"""解析pnl JSON数据，返回pandas SeriesArgs:pnl_json: pnl的JSON字符串Returns:以日期为索引，pnl为值的Series"""if not pnl_json:return pd.Series()pnl_data = json.loads(pnl_json)records = pnl_data.get('records', [])dates = [record[0] for record in records]pnls = [record[1] for record in records]return pd.Series(pnls, index=pd.to_datetime(dates))def calculate_correlations_by_region(self, region: str) -> pd.DataFrame:"""计算指定region下所有alpha之间的皮尔逊相关系数Args:region: 地区代码，如 'USA', 'CHN' 等Returns:相关系数矩阵DataFrame"""print(f"正在获取 {region} 地区的alpha数据...")alphas = self.get_by_region(region)print(f"共获取 {len(alphas)} 个alpha")if len(alphas) < 2:print("alpha数量少于2个，无法计算相关性")return pd.DataFrame()# 构建pnl矩阵print("正在解析pnl数据...")pnl_dict = {}valid_alphas = []for alpha in alphas:alpha_id = alpha['id']pnl_series = self.parse_pnl_data(alpha.get('pnl'))if len(pnl_series) > 0:pnl_dict[alpha_id] = pnl_seriesvalid_alphas.append(alpha)print(f"有效alpha数量: {len(valid_alphas)}")if len(valid_alphas) < 2:print("有效alpha少于2个，无法计算相关性")return pd.DataFrame()# 转换为DataFramepnl_df = pd.DataFrame(pnl_dict)# 使用前向填充处理缺失值，然后shift(1)# 这样做的原因：避免使用未来信息，计算t日的相关性时使用t-1日的数据pnl_df = pnl_df.ffill().shift(1)# 计算收益率（pnl的差分）print("正在计算收益率...")alpha_rets = pnl_df.diff()print("正在计算相关系数矩阵...")corr_matrix = alpha_rets.corr(method='pearson')return corr_matrixdef save_correlation_to_file(self, corr_matrix: pd.DataFrame, region: str):"""将相关系数矩阵保存到CSV文件Args:corr_matrix: 相关系数矩阵region: 地区代码，用于生成文件名"""# 获取当前脚本所在目录current_dir = os.path.dirname(os.path.abspath(__file__))filename = f'alpha_correlation_{region}.csv'filepath = os.path.join(current_dir, filename)corr_matrix.to_csv(filepath)print(f"相关系数矩阵已保存到 {filepath}")return filepathdef get_high_correlation_pairs_from_matrix(self, corr_matrix: pd.DataFrame,threshold: float = 0.8) -> List[Tuple[str, str, float]]:"""从相关系数矩阵中获取高相关性的alpha对Args:corr_matrix: 相关系数矩阵threshold: 相关系数阈值Returns:高相关性的alpha对列表 [(alpha_id_1, alpha_id_2, correlation), ...]"""high_corr_pairs = []alpha_ids = corr_matrix.index.tolist()for i, alpha1 in enumerate(alpha_ids):for alpha2 in alpha_ids[i+1:]:corr_value = corr_matrix.loc[alpha1, alpha2]if not np.isnan(corr_value) and abs(corr_value) >= threshold:high_corr_pairs.append((alpha1, alpha2, corr_value))# 按相关系数绝对值降序排列high_corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)return high_corr_pairsdef export_network_data(self, corr_matrix: pd.DataFrame, region: str, threshold: float = 0.0):"""将相关系数矩阵导出为网络图所需的JSON格式Args:corr_matrix: 相关系数矩阵region: 地区代码threshold: 相关系数阈值，低于此值的边不会被包含（默认0表示导出所有）Returns:JSON文件路径"""current_dir = os.path.dirname(os.path.abspath(__file__))# 重新获取alpha详细数据alphas = self.get_by_region(region)alpha_dict = {alpha['id']: alpha for alpha in alphas}# 构建节点数据（包含详细信息）nodes = []alpha_ids = corr_matrix.index.tolist()for alpha_id in alpha_ids:alpha_info = alpha_dict.get(alpha_id, {})node = {'id': alpha_id,'name': alpha_id,'create_dt': str(alpha_info.get('create_dt', '')),'region': alpha_info.get('region', ''),'universe': alpha_info.get('universe', ''),'delay': alpha_info.get('delay'),'decay': alpha_info.get('decay'),'neutralization': alpha_info.get('neutralization', ''),'code': alpha_info.get('code', ''),'operatorCount': alpha_info.get('operatorCount'),'turnover': alpha_info.get('turnover'),'returns': alpha_info.get('returns'),'margin': alpha_info.get('margin'),'sharpe': alpha_info.get('sharpe'),'fitness': alpha_info.get('fitness'),'drawdown': alpha_info.get('drawdown'),'longCount': alpha_info.get('longCount'),'shortCount': alpha_info.get('shortCount')}nodes.append(node)# 构建边数据 - 导出所有边，让前端控制显示links = []for i, alpha1 in enumerate(alpha_ids):for alpha2 in alpha_ids[i+1:]:corr_value = corr_matrix.loc[alpha1, alpha2]if not np.isnan(corr_value) and abs(corr_value) >= threshold:links.append({'source': alpha1,'target': alpha2,'correlation': float(corr_value),'value': float(abs(corr_value))  # 用于边的粗细})# 构建完整数据network_data = {'nodes': nodes,'links': links,'region': region,'threshold': threshold}# 保存为JSON文件filename = f'alpha_network_{region}.json'filepath = os.path.join(current_dir, filename)with open(filepath, 'w', encoding='utf-8') as f:json.dump(network_data, f, indent=2, ensure_ascii=False)print(f"网络数据已保存到 {filepath}")return filepath# 使用示例if __name__ == "__main__":db = AlphaSubmitDB()# 指定要分析的regionregions = ['GLB']  # 可以分析多个regionfor region in regions:print("=" * 60)print(f"开始处理 {region} 地区的alpha相关性...")print("=" * 60)# 计算该region下所有alpha的相关系数矩阵corr_matrix = db.calculate_correlations_by_region(region)if not corr_matrix.empty:# 保存到文件filename = db.save_correlation_to_file(corr_matrix, region)# 导出网络图数据（导出所有边，由前端页面控制阈值过滤）json_file = db.export_network_data(corr_matrix, region, threshold=0.0)print(f"\n相关系数矩阵维度: {corr_matrix.shape}")print("\n相关系数矩阵预览:")print(corr_matrix.iloc[:5, :5])  # 显示前5x5# 获取高相关性的alpha对print("\n" + "=" * 60)print("高相关性alpha对 (|相关系数| >= 0.8):")high_corr_pairs = db.get_high_correlation_pairs_from_matrix(corr_matrix, threshold=0.8)if high_corr_pairs:for i, (alpha1, alpha2, corr) in enumerate(high_corr_pairs[:10], 1):print(f"{i}. {alpha1} <-> {alpha2}: {corr:.4f}")else:print("未发现高相关性的alpha对")print(f"\n{region} 地区处理完成！\n")else:print(f"{region} 地区没有足够的数据进行相关性分析\n")我预先已经将数据保存到数据库了，各位大佬可以自行进行修改代码，保证导出的格式一致即可：{"nodes": [{"id": "alpha的ID","name": "alpha的ID","create_dt": "创建时间字符串","region": "地区代码","universe": "universe","delay": 延迟值,"decay": 衰减值,"neutralization": "中性化方式","code": "alpha代码","operatorCount": 操作符数量,"turnover": 换手率,"returns": 回报率,"margin": margin值,"sharpe": sharpe比率,"fitness": 适应度,"drawdown": 回撤,"longCount": 多头数量,"shortCount": 空头数量}// ... 更多节点],"links": [{"source": "源alpha的ID","target": "目标alpha的ID","correlation": 0.85,  // 实际相关系数值（可正可负）"value": 0.85         // 相关系数的绝对值（用于边的粗细）}// ... 更多边],"region": "GLB","threshold": 0.0}打分代码打分代码就不贴了，论坛中有很多，读取导出的点数分配文件即可。

---

### 帖子 #37: 【Community Leader - 可视化alpha打分工具 】可视化分析你的alpha，并进行打分，助力Osmosis比赛！
- **主帖链接**: https://support.worldquantbrain.com【Community Leader - 可视化alpha打分工具 】可视化分析你的alpha并进行打分助力Osmosis比赛_37217049607831.md
- **讨论数**: 1

先看效果图


> [!NOTE] [图片 OCR 识别内容]
> Alpha相关性网络图
> 正常模式
> Alpha: ZbdPPWK
> 加载数据文件 (JSON:
> 基本信息
> 选择文件
> alpha
> network_USAjson
> 创建时间:
> 2025-12-2011:10:01
> EdGSIJ
> VITGIV
> 相关性阈值:
> 0.60
> NGgITST
> Region:
> USA
> 855
> TIOZE
> UOC
> Universe:
> TOP3OO0
> EPnglaM
> BYZFZr
> ZI3nlad
> Delay:
> 节点距离力:
> nIsgq
> '21
> Decay:
> RRnga3j
> Iaxa
> 855
> Neutralization:
> STATISTICAL
> bo9Grg
> QBBIqZw
> 节点排斥力:
> 155
> IZRIR
> TXGONb
> 操作符数虽:
> ZbdPPU
> 933E19
> 855
> OWPMAp2
> IZRPLR
> GRIO3I
> 性能指标
> Ozihl
> 38621
> 连线模式: OFF 
> AbNOEd
> Zmjqlz
> WE2qObQ
> Sharpe:
> 1.9100
> Fitness:
> 1.3200
> SIRRN
> 删除连线模式: OFF
> 855
> EdDs9
> KqqAgmOI
> Returns:
> 0.1134
> QOMLXQ
> XNbXOpl
> Tumover:
> 0.2375
> 删除节点模式: OFF
> URUZRUR
> TN03
> Vtjplr 855
> LgEqeljg
> bKdldz
> 8435
> 52002a0
> Margin:
> 0.0010
> 重置布局
> OOVPMI
> JobNlS
> AINgKg
> Drawdown:
> 0.0493
> BSSGNS9r
> dlple
> Xgyb
> AG35gQ
> OpKoNlAn55
> Long Count:
> 1478.00
> WPGOPY
> pNse'|
> nNPpel
> ggKGI9
> 854
> LGZOAOSS  ISGIIIN
> Short Count
> 1653.00
> 节点数量:
> 117
> RINEa
> IGapk
> QGKqmog
> LOIKKGG
> 连线数量:
> 153
> ASVWKd AGvYzky
> 点数分配
> 855
> 当前区域:
> USA
> NIwGITNq
> NIkeAPt
> GgSNVG
> 己分点数:
> 855
> 1303
> QUVM
> VSING
> OproGgq
> YSGPyPo
> XhYa
> 衷达式
> 点数分配
> KV2qzml
> PpeAIjV
> Ta
> ztegtry
> AT
> 9IOUP
> GGgqo
> TO
> TeU-us
> U LSUII
> 总点数: 100,000
> PPmlpq
> XqXUI
> Ukq
> GNINnIpl
> VkRbe33
> BpISy
> 己分配: 100,000
> 854
> SpP7SLm
> 剩余:
> Teg C
> VOLLOHa
> OkANPS
> NJJEKB
> auprlqz
> 保存分配
> 加载分配
> XOMpNB5
> Indsn
> OWJOYZn
> 2OgOMb
> GOKOr
> 清空分配
> 平均分配 
> JaITI
> VkkGBelo
> Gmpzllqx
> IGOpOPz
> JIgGY
> 按簇分配
> Azojry
> Zmgoll
> UgSme
> 1122k
> WONOWjd
> IIVEO
> B29jk6q
> C8yJ1gk
> 操作说明
> ESwsjpm
> QGETZOW
> agx0o2
> 拖动节点改娈位置
> SEqIEOK
> 854
> 鼠标恳停查看详情
> OPXOIJBT
> dGSKSV
> ZIgOo
> WARpel
> 点击连线模式后;点击两个节点添加
> RRIxl8a
> 连线
> 点击副除模式后。点击连线除
> 调整阈值过滤显示的连线
> 滚轮缩放。拖动画布平移
> like it Re it Iove it
> RgPo
> g3zPS5KIZT
> mS6OA5
> 4F1
> hey


拥有的功能：

- 可视化alpha之间的相关性，支持自主调节相关性阈值
- 自主删除/恢复 alpha
- 自主删除alpha之间的连线
- 查看某个alpha的详细指标（无pnl）
- 对alpha平均分配点数
- 按照聚簇分配点数
- 导出/导入分配结果

TODO：

- 根据pyr、指标等对alpha进行分类
- 自主进行alpha分类
- 按照分类进行点数分配
- 权重点数分配
- 支持pnl的展示

再说下点数分配的思路出发点：

最开始的思路是，根据相关性筛选出一个彼此相关性最低的alpha集合，赋予大权重，然后筛选集合内每一个alpha相关性较高的几个alpha赋予较低权重，用来增强这个独特alpha的信号，但是从图中可以看出来，alpha与alpha之间的相关性并没有很高....

个人认为这个工具还是挺有用的，未来逐步完善的话，应用到own super alpha上也是一个不错的选择。

下面直接献上代码：

**前端代码**

```
<!DOCTYPE html><html lang="zh-CN"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>Alpha相关性网络图</title>    <script src="[链接已屏蔽]    <style>        * {            margin: 0;            padding: 0;            box-sizing: border-box;        }        body {            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;            background: #1a1a2e;            color: #eee;            overflow: hidden;        }        #container {            display: flex;            height: 100vh;        }        #control-panel {            width: 300px;            background: #16213e;            padding: 20px;            overflow-y: auto;            box-shadow: 2px 0 10px rgba(0,0,0,0.3);        }        #graph-container {            flex: 1;            position: relative;        }        h1 {            font-size: 20px;            margin-bottom: 20px;            color: #00d9ff;            border-bottom: 2px solid #00d9ff;            padding-bottom: 10px;        }        .control-group {            margin-bottom: 20px;        }        .control-group label {            display: block;            margin-bottom: 8px;            font-size: 14px;            color: #aaa;        }        input[type="range"] {            width: 100%;            height: 6px;            border-radius: 3px;            background: #0f3460;            outline: none;            -webkit-appearance: none;        }        input[type="range"]::-webkit-slider-thumb {            -webkit-appearance: none;            width: 16px;            height: 16px;            border-radius: 50%;            background: #00d9ff;            cursor: pointer;        }        input[type="file"] {            width: 100%;            padding: 10px;            background: #0f3460;            border: 1px solid #00d9ff;            border-radius: 5px;            color: #eee;            cursor: pointer;        }        button {            width: 100%;            padding: 10px;            margin-top: 10px;            background: #00d9ff;            border: none;            border-radius: 5px;            color: #16213e;            font-weight: bold;            cursor: pointer;            transition: all 0.3s;        }        button:hover {            background: #00b8d4;            transform: translateY(-2px);            box-shadow: 0 4px 8px rgba(0, 217, 255, 0.3);        }        button:disabled {            background: #555;            cursor: not-allowed;            transform: none;        }        .value-display {            display: inline-block;            float: right;            color: #00d9ff;            font-weight: bold;        }        .stats {            background: #0f3460;            padding: 15px;            border-radius: 5px;            margin-top: 20px;        }        .stats div {            margin: 8px 0;            font-size: 13px;        }        .stats .stat-label {            color: #aaa;        }        .stats .stat-value {            color: #00d9ff;            font-weight: bold;            float: right;        }        svg {            width: 100%;            height: 100%;            background: #1a1a2e;        }        .node {            cursor: move;            transition: all 0.2s;        }        .node circle {            fill: #00d9ff;            stroke: #fff;            stroke-width: 2px;            transition: all 0.3s;        }        .node:hover circle {            fill: #ff6b6b;            r: 14;        }        .node.highlighted circle {            fill: #ffd700;            r: 16;            stroke-width: 3px;        }        .node text {            font-size: 11px;            fill: #eee;            pointer-events: none;            text-anchor: middle;        }        .link {            stroke: #555;            stroke-opacity: 0.6;            cursor: pointer;            transition: all 0.3s;        }        .link:hover {            stroke: #00d9ff;            stroke-opacity: 1;            stroke-width: 3px;        }        .link.selected {            stroke: #ff6b6b;            stroke-opacity: 1;        }        .link.highlighted {            stroke: #ffd700;            stroke-opacity: 1;            stroke-width: 4px;        }        .mode-indicator {            position: absolute;            top: 20px;            left: 20px;            background: rgba(22, 33, 62, 0.9);            padding: 10px 20px;            border-radius: 5px;            font-size: 14px;            border: 2px solid #00d9ff;        }        .instructions {            background: #0f3460;            padding: 15px;            border-radius: 5px;            margin-top: 20px;            font-size: 12px;            line-height: 1.8;        }        .instructions h3 {            color: #00d9ff;            margin-bottom: 10px;            font-size: 14px;        }        .instructions ul {            list-style: none;            padding-left: 0;        }        .instructions li {            margin: 5px 0;            color: #aaa;        }        .instructions li:before {            content: "▸ ";            color: #00d9ff;        }        #info-tooltip {            position: absolute;            background: rgba(22, 33, 62, 0.95);            padding: 10px 15px;            border-radius: 5px;            pointer-events: none;            display: none;            border: 1px solid #00d9ff;            font-size: 12px;            max-width: 200px;        }        .clear-float::after {            content: "";            display: table;            clear: both;        }        .list-section {            background: #0f3460;            border-radius: 5px;            margin-top: 20px;            overflow: hidden;        }        .list-header {            background: #16213e;            padding: 12px 15px;            cursor: pointer;            display: flex;            justify-content: space-between;            align-items: center;            border-bottom: 1px solid #00d9ff;        }        .list-header:hover {            background: #1a2845;        }        .list-header h3 {            color: #00d9ff;            font-size: 14px;            margin: 0;        }        .list-header .toggle-icon {            color: #00d9ff;            font-size: 12px;            transition: transform 0.3s;        }        .list-header .toggle-icon.collapsed {            transform: rotate(-90deg);        }        .list-content {            max-height: 300px;            overflow-y: auto;            padding: 10px;        }        .list-content.collapsed {            display: none;        }        .list-item {            padding: 8px 10px;            margin: 5px 0;            background: #16213e;            border-radius: 3px;            font-size: 12px;            display: flex;            justify-content: space-between;            align-items: center;            transition: background 0.2s;            cursor: pointer;        }        .list-item:hover {            background: #1a2845;        }        .list-item.highlighted {            background: #00d9ff;            color: #16213e;        }        .list-item.highlighted .item-name,        .list-item.highlighted .item-value {            color: #16213e;        }        .list-item .item-name {            color: #eee;            flex: 1;        }        .list-item .item-value {            color: #00d9ff;            font-weight: bold;            margin-left: 10px;        }        .list-item.positive .item-value {            color: #4caf50;        }        .list-item.negative .item-value {            color: #ff6b6b;        }        .search-box {            width: 100%;            padding: 8px;            margin: 5px 0;            background: #16213e;            border: 1px solid #00d9ff;            border-radius: 3px;            color: #eee;            font-size: 12px;        }        .search-box:focus {            outline: none;            border-color: #00b8d4;        }        .list-empty {            text-align: center;            color: #aaa;            padding: 20px;            font-size: 12px;        }        .list-content::-webkit-scrollbar {            width: 6px;        }        .list-content::-webkit-scrollbar-track {            background: #16213e;        }        .list-content::-webkit-scrollbar-thumb {            background: #00d9ff;            border-radius: 3px;        }        .list-content::-webkit-scrollbar-thumb:hover {            background: #00b8d4;        }        .restore-btn {            width: auto;            min-width: 40px;            padding: 5px 10px;            margin: 0;            background: #4caf50;            border: none;            border-radius: 3px;            color: white;            font-size: 18px;            font-weight: bold;            cursor: pointer;            transition: all 0.2s;        }        .restore-btn:hover {            background: #45a049;            transform: scale(1.1);        }        .deleted-item {            align-items: flex-start;        }        .allocation-section {            background: #0f3460;            padding: 15px;            border-radius: 5px;            margin-top: 20px;        }        .allocation-section h3 {            color: #00d9ff;            margin-bottom: 15px;            font-size: 14px;        }        .allocation-stats {            margin-bottom: 15px;        }        .allocation-stats div {            margin: 8px 0;            font-size: 13px;        }        .allocation-input {            width: 80px;            padding: 4px 6px;            background: #16213e;            border: 1px solid #00d9ff;            border-radius: 3px;            color: #eee;            font-size: 12px;            text-align: right;        }        .allocation-input:focus {            outline: none;            border-color: #00b8d4;        }        .allocation-input.warning {            border-color: #ff9800;        }        .allocation-input.error {            border-color: #ff6b6b;        }        .allocation-buttons {            display: flex;            gap: 10px;            margin-top: 10px;        }        .allocation-buttons button {            flex: 1;            padding: 8px;            margin: 0;            font-size: 12px;        }        .node.has-allocation circle {            stroke: #ffd700;            stroke-width: 3px;        }        .node-allocation-label {            font-size: 10px;            fill: #ffd700;            font-weight: bold;            text-anchor: middle;        }        #detail-panel {            position: absolute;            top: 20px;            right: 20px;            width: 400px;            max-height: 80vh;            background: rgba(22, 33, 62, 0.98);            border: 2px solid #00d9ff;            border-radius: 8px;            padding: 20px;            display: none;            overflow-y: auto;            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);            z-index: 1000;        }        #detail-panel::-webkit-scrollbar {            width: 6px;        }        #detail-panel::-webkit-scrollbar-track {            background: #16213e;        }        #detail-panel::-webkit-scrollbar-thumb {            background: #00d9ff;            border-radius: 3px;        }        .detail-header {            display: flex;            justify-content: space-between;            align-items: center;            margin-bottom: 15px;            padding-bottom: 10px;            border-bottom: 2px solid #00d9ff;        }        .detail-header h2 {            color: #00d9ff;            font-size: 18px;            margin: 0;        }        .close-btn {            background: none;            border: none;            color: #ff6b6b;            font-size: 24px;            cursor: pointer;            padding: 0;            width: 30px;            height: 30px;            line-height: 30px;            text-align: center;            border-radius: 50%;            transition: all 0.3s;        }        .close-btn:hover {            background: #ff6b6b;            color: #fff;            transform: rotate(90deg);        }        .detail-section {            margin-bottom: 15px;        }        .detail-section h3 {            color: #00d9ff;            font-size: 14px;            margin-bottom: 10px;        }        .detail-row {            display: flex;            justify-content: space-between;            padding: 6px 0;            border-bottom: 1px solid #0f3460;            font-size: 13px;        }        .detail-row:last-child {            border-bottom: none;        }        .detail-label {            color: #aaa;            font-weight: 500;        }        .detail-value {            color: #eee;            text-align: right;            max-width: 60%;            word-break: break-all;        }        .detail-value.positive {            color: #4caf50;        }        .detail-value.negative {            color: #ff6b6b;        }        .detail-code {            background: #0f3460;            padding: 10px;            border-radius: 5px;            font-family: 'Courier New', monospace;            font-size: 11px;            color: #eee;            max-height: 200px;            overflow-y: auto;            word-break: break-all;            white-space: pre-wrap;        }    </style></head><body>    <div id="container">        <div id="control-panel">            <h1>Alpha相关性网络图</h1>                        <div class="control-group">                <label>加载数据文件 (JSON):</label>                <input type="file" id="fileInput" accept=".json">            </div>            <div class="control-group">                <label>                    相关性阈值: <span class="value-display" id="thresholdValue">0.50</span>                </label>                <input type="range" id="threshold" min="0" max="1" step="0.01" value="0.5">            </div>            <div class="control-group">                <label>                    节点距离力: <span class="value-display" id="distanceValue">20</span>                </label>                <input type="range" id="linkDistance" min="5" max="500" step="5" value="20">            </div>            <div class="control-group">                <label>                    节点排斥力: <span class="value-display" id="chargeValue">-50</span>                </label>                <input type="range" id="chargeStrength" min="-600" max="-10" step="5" value="-50">            </div>            <div class="control-group">                <button id="addLinkBtn">连线模式: OFF</button>                <button id="removeLinkBtn">删除连线模式: OFF</button>                <button id="removeNodeBtn">删除节点模式: OFF</button>                <button id="resetBtn">重置布局</button>            </div>            <div class="stats">                <div class="clear-float">                    <span class="stat-label">节点数量:</span>                    <span class="stat-value" id="nodeCount">0</span>                </div>                <div class="clear-float">                    <span class="stat-label">连线数量:</span>                    <span class="stat-value" id="linkCount">0</span>                </div>                <div class="clear-float">                    <span class="stat-label">当前区域:</span>                    <span class="stat-value" id="regionInfo">-</span>                </div>            </div>            <div class="allocation-section">                <h3>点数分配</h3>                <div class="allocation-stats">                    <div class="clear-float">                        <span class="stat-label">总点数:</span>                        <span class="stat-value" id="totalPoints">100,000</span>                    </div>                    <div class="clear-float">                        <span class="stat-label">已分配:</span>                        <span class="stat-value" id="allocatedPoints">0</span>                    </div>                    <div class="clear-float">                        <span class="stat-label">剩余:</span>                        <span class="stat-value" id="remainingPoints">100,000</span>                    </div>                </div>                <div class="allocation-buttons">                    <button id="saveAllocationBtn">保存分配</button>                    <button id="loadAllocationBtn">加载分配</button>                </div>                <div class="allocation-buttons">                    <button id="clearAllocationBtn" style="background: #ff6b6b;">清空分配</button>                    <button id="autoAllocateBtn" style="background: #4caf50;">平均分配</button>                </div>                <div class="allocation-buttons">                    <button id="clusterAllocateBtn" style="background: #9c27b0;">按簇分配</button>                </div>                <input type="file" id="allocationFileInput" accept=".json" style="display: none;">            </div>            <!-- 簇信息列表 -->            <div class="list-section" id="clusterSection" style="display: none;">                <div class="list-header" onclick="toggleList('clusterList')">                    <h3>簇信息 (阈值: <span id="clusterThreshold">0.50</span>)</h3>                    <span class="toggle-icon" id="clusterListIcon">▼</span>                </div>                <div class="list-content" id="clusterList">                    <div id="clusterInfo"></div>                </div>            </div>            <div class="instructions">                <h3>操作说明</h3>                <ul>                    <li>拖动节点改变位置</li>                    <li>鼠标悬停查看详情</li>                    <li>点击连线模式后，点击两个节点添加连线</li>                    <li>点击删除模式后，点击连线删除</li>                    <li>调整阈值过滤显示的连线</li>                    <li>滚轮缩放，拖动画布平移</li>                    <li>在Alpha列表中输入点数进行分配</li>                </ul>            </div>            <!-- Alpha列表 -->            <div class="list-section">                <div class="list-header" onclick="toggleList('alphaList')">                    <h3>Alpha列表</h3>                    <span class="toggle-icon" id="alphaListIcon">▼</span>                </div>                <div class="list-content" id="alphaList">                    <input type="text" class="search-box" id="alphaSearch" placeholder="搜索Alpha ID...">                    <div id="alphaListContent">                        <div class="list-empty">未加载数据</div>                    </div>                </div>            </div>            <!-- 连线列表 -->            <div class="list-section">                <div class="list-header" onclick="toggleList('linkList')">                    <h3>连线信息 (按相关性排序)</h3>                    <span class="toggle-icon" id="linkListIcon">▼</span>                </div>                <div class="list-content" id="linkList">                    <input type="text" class="search-box" id="linkSearch" placeholder="搜索Alpha ID...">                    <div id="linkListContent">                        <div class="list-empty">未加载数据</div>                    </div>                </div>            </div>            <!-- 已删除节点列表 -->            <div class="list-section">                <div class="list-header" onclick="toggleList('deletedNodesList')">                    <h3>已删除节点</h3>                    <span class="toggle-icon collapsed" id="deletedNodesListIcon">▼</span>                </div>                <div class="list-content collapsed" id="deletedNodesList">                    <div id="deletedNodesContent">                        <div class="list-empty">无已删除节点</div>                    </div>                </div>            </div>        </div>        <div id="graph-container">            <div class="mode-indicator" id="modeIndicator">正常模式</div>            <svg id="network"></svg>            <div id="info-tooltip"></div>                        <!-- Alpha详细信息面板 -->            <div id="detail-panel">                <div class="detail-header">                    <h2 id="detailAlphaId">Alpha 详情</h2>                    <button class="close-btn" onclick="closeDetailPanel()">×</button>                </div>                <div id="detailContent"></div>            </div>        </div>    </div>    <script>        // 全局变量        let graphData = { nodes: [], links: [] };        let originalData = { nodes: [], links: [] };        let deletedNodes = []; // 记录已删除的节点        let simulation;        let svg, g, link, node;        let zoom; // 保存zoom引用        let mode = 'normal'; // 'normal', 'addLink', 'removeLink', 'removeNode'        let selectedNode = null;        let currentThreshold = 0.5;                // 点数分配相关        let allocations = {}; // { alphaId: points }        const TOTAL_POINTS = 100000;        let clusters = []; // 存储簇信息        // 初始化SVG        function initSVG() {            const container = d3.select('#graph-container');            const width = container.node().clientWidth;            const height = container.node().clientHeight;            svg = d3.select('#network')                .attr('width', width)                .attr('height', height);            // 添加缩放和平移            zoom = d3.zoom()                .scaleExtent([0.1, 4])                .on('zoom', (event) => {                    g.attr('transform', event.transform);                });            svg.call(zoom);            g = svg.append('g');            // 添加连线组和节点组            g.append('g').attr('class', 'links');            g.append('g').attr('class', 'nodes');        }        // 初始化力导向图        function initSimulation() {            const width = svg.node().clientWidth;            const height = svg.node().clientHeight;            simulation = d3.forceSimulation()                .force('link', d3.forceLink().id(d => d.id).distance(20))                .force('charge', d3.forceManyBody().strength(-50))                .force('center', d3.forceCenter(width / 2, height / 2))                .force('collision', d3.forceCollide().radius(20))                .force('x', d3.forceX(width / 2).strength(0.05))                .force('y', d3.forceY(height / 2).strength(0.05));        }        // 更新图形        function updateGraph() {            // 过滤连线            const filteredLinks = originalData.links.filter(l =>                 Math.abs(l.correlation) >= currentThreshold            );            graphData = {                nodes: originalData.nodes.map(n => ({...n})),                links: filteredLinks.map(l => ({...l}))            };            // 更新连线            link = g.select('.links')                .selectAll('line')                .data(graphData.links, d => `${d.source.id || d.source}-${d.target.id || d.target}`);            link.exit().remove();            const linkEnter = link.enter()                .append('line')                .attr('class', 'link')                .attr('stroke-width', d => Math.abs(d.correlation) * 3)                .on('click', onLinkClick)                .on('mouseover', showLinkTooltip)                .on('mouseout', hideTooltip);            link = linkEnter.merge(link);            // 更新节点            node = g.select('.nodes')                .selectAll('g')                .data(graphData.nodes, d => d.id);            node.exit().remove();            const nodeEnter = node.enter()                .append('g')                .attr('class', 'node')                .call(d3.drag()                    .on('start', dragstarted)                    .on('drag', dragged)                    .on('end', dragended))                .on('click', onNodeClick)                .on('mouseover', showNodeTooltip)                .on('mouseout', hideTooltip);            nodeEnter.append('circle')                .attr('r', 10);            nodeEnter.append('text')                .attr('dy', 25)                .text(d => d.name);            // 添加点数标签            nodeEnter.append('text')                .attr('class', 'node-allocation-label')                .attr('dy', -15);            node = nodeEnter.merge(node);                        // 更新节点样式和点数标签            node.classed('has-allocation', d => allocations[d.id] > 0);            node.select('.node-allocation-label')                .text(d => allocations[d.id] ? allocations[d.id].toLocaleString() : '');            // 更新力导向图            simulation.nodes(graphData.nodes);            simulation.force('link').links(graphData.links);            simulation.alpha(1).restart();            simulation.on('tick', () => {                link                    .attr('x1', d => d.source.x)                    .attr('y1', d => d.source.y)                    .attr('x2', d => d.target.x)                    .attr('y2', d => d.target.y);                node.attr('transform', d => `translate(${d.x},${d.y})`);            });            updateStats();            updateAlphaList();            updateLinkList();        }        // 节点拖拽        function dragstarted(event, d) {            if (!event.active) simulation.alphaTarget(0.3).restart();            d.fx = d.x;            d.fy = d.y;        }        function dragged(event, d) {            d.fx = event.x;            d.fy = event.y;        }        function dragended(event, d) {            if (!event.active) simulation.alphaTarget(0);        }        // 节点点击事件        function onNodeClick(event, d) {            event.stopPropagation();                        if (mode === 'addLink') {                if (!selectedNode) {                    selectedNode = d;                    d3.select(this).select('circle').style('fill', '#ffd700');                    updateModeIndicator(`已选择: ${d.name}，请选择第二个节点`);                } else if (selectedNode.id !== d.id) {                    // 添加新连线                    addLink(selectedNode, d);                    // 重置选择                    node.selectAll('circle').style('fill', '#00d9ff');                    selectedNode = null;                    updateModeIndicator('连线模式: 选择两个节点以添加连线');                }            } else if (mode === 'removeNode') {                // 删除节点                removeNode(d);            } else {                // 正常模式，显示详细信息                showDetailPanel(d);            }        }        // 连线点击事件        function onLinkClick(event, d) {            event.stopPropagation();                        if (mode === 'removeLink') {                removeLink(d);            }        }        // 添加连线        function addLink(source, target) {            const existingLink = originalData.links.find(l =>                (l.source === source.id && l.target === target.id) ||                (l.source === target.id && l.target === source.id)            );            if (!existingLink) {                originalData.links.push({                    source: source.id,                    target: target.id,                    correlation: 0.5,                    value: 0.5                });                updateGraph();            }        }        // 删除连线        function removeLink(link) {            const sourceId = link.source.id || link.source;            const targetId = link.target.id || link.target;                        originalData.links = originalData.links.filter(l => {                const lSource = l.source.id || l.source;                const lTarget = l.target.id || l.target;                return !((lSource === sourceId && lTarget === targetId) ||                         (lSource === targetId && lTarget === sourceId));            });                        updateGraph();        }        // 删除节点        function removeNode(nodeToRemove) {            const nodeId = nodeToRemove.id;                        // 找到要删除的节点            const nodeData = originalData.nodes.find(n => n.id === nodeId);            if (!nodeData) return;                        // 找到与该节点相关的连线            const relatedLinks = originalData.links.filter(l => {                const sourceId = l.source.id || l.source;                const targetId = l.target.id || l.target;                return sourceId === nodeId || targetId === nodeId;            });                        // 保存到deletedNodes数组            deletedNodes.push({                node: {...nodeData},                links: relatedLinks.map(l => ({                    source: l.source.id || l.source,                    target: l.target.id || l.target,                    correlation: l.correlation,                    value: l.value                })),                deletedAt: new Date().toLocaleString()            });                        // 删除与该节点相关的所有连线            originalData.links = originalData.links.filter(l => {                const sourceId = l.source.id || l.source;                const targetId = l.target.id || l.target;                return sourceId !== nodeId && targetId !== nodeId;            });                        // 删除节点            originalData.nodes = originalData.nodes.filter(n => n.id !== nodeId);                        updateGraph();            updateDeletedNodesList();        }        // 恢复节点        function restoreNode(index) {            if (index < 0 || index >= deletedNodes.length) return;                        const deletedItem = deletedNodes[index];                        // 检查节点是否已存在            if (originalData.nodes.find(n => n.id === deletedItem.node.id)) {                alert('该节点已存在！');                return;            }                        // 恢复节点            originalData.nodes.push({...deletedItem.node});                        // 恢复连线（只恢复两端节点都存在的连线）            deletedItem.links.forEach(link => {                const sourceExists = originalData.nodes.find(n => n.id === link.source);                const targetExists = originalData.nodes.find(n => n.id === link.target);                                if (sourceExists && targetExists) {                    // 检查连线是否已存在                    const linkExists = originalData.links.find(l => {                        const lSource = l.source.id || l.source;                        const lTarget = l.target.id || l.target;                        return (lSource === link.source && lTarget === link.target) ||                               (lSource === link.target && lTarget === link.source);                    });                                        if (!linkExists) {                        originalData.links.push({...link});                    }                }            });                        // 从deletedNodes中移除            deletedNodes.splice(index, 1);                        updateGraph();            updateDeletedNodesList();        }        // 定位并高亮节点        function locateNode(nodeId) {            // 移除所有高亮            if (node) {                node.classed('highlighted', false);            }            if (link) {                link.classed('highlighted', false);            }            d3.selectAll('.list-item').classed('highlighted', false);                        // 查找目标节点            const targetNode = graphData.nodes.find(n => n.id === nodeId);            if (!targetNode) {                console.log('节点未找到:', nodeId);                return;            }                        // 确保节点有位置信息            if (targetNode.x === undefined || targetNode.y === undefined) {                console.log('节点位置未初始化');                return;            }                        // 高亮节点            if (node) {                node.filter(d => d.id === nodeId).classed('highlighted', true);            }                        // 计算缩放和平移            const width = svg.node().clientWidth;            const height = svg.node().clientHeight;            const scale = 2.0;            const x = width / 2 - targetNode.x * scale;            const y = height / 2 - targetNode.y * scale;                        // 应用平滑过渡            svg.transition()                .duration(750)                .call(                    zoom.transform,                    d3.zoomIdentity.translate(x, y).scale(scale)                );                        // 3秒后移除高亮            setTimeout(() => {                if (node) {                    node.classed('highlighted', false);                }            }, 3000);        }        // 定位并高亮连线        function locateLink(sourceId, targetId) {            // 移除所有高亮            if (node) {                node.classed('highlighted', false);            }            if (link) {                link.classed('highlighted', false);            }            d3.selectAll('.list-item').classed('highlighted', false);                        // 查找两个节点            const sourceNode = graphData.nodes.find(n => n.id === sourceId);            const targetNode = graphData.nodes.find(n => n.id === targetId);                        if (!sourceNode || !targetNode) {                console.log('节点未找到:', sourceId, targetId);                return;            }                        // 确保节点有位置信息            if (sourceNode.x === undefined || targetNode.x === undefined) {                console.log('节点位置未初始化');                return;            }                        // 高亮两个节点            if (node) {                node.filter(d => d.id === sourceId || d.id === targetId)                    .classed('highlighted', true);            }                        // 高亮连线            if (link) {                link.filter(l => {                    const lSource = l.source.id || l.source;                    const lTarget = l.target.id || l.target;                    return (lSource === sourceId && lTarget === targetId) ||                           (lSource === targetId && lTarget === sourceId);                }).classed('highlighted', true);            }                        // 计算两个节点的中心点            const centerX = (sourceNode.x + targetNode.x) / 2;            const centerY = (sourceNode.y + targetNode.y) / 2;                        // 计算缩放和平移            const width = svg.node().clientWidth;            const height = svg.node().clientHeight;            const scale = 2.0;            const x = width / 2 - centerX * scale;            const y = height / 2 - centerY * scale;                        // 应用平滑过渡            svg.transition()                .duration(750)                .call(                    zoom.transform,                    d3.zoomIdentity.translate(x, y).scale(scale)                );                        // 3秒后移除高亮            setTimeout(() => {                if (node) {                    node.classed('highlighted', false);                }                if (link) {                    link.classed('highlighted', false);                }            }, 3000);        }        // 显示提示信息        function showNodeTooltip(event, d) {            const tooltip = d3.select('#info-tooltip');            tooltip.style('display', 'block')                .html(`<strong>${d.id}</strong>`)                .style('left', (event.pageX + 10) + 'px')                .style('top', (event.pageY - 10) + 'px');        }        function showLinkTooltip(event, d) {            const tooltip = d3.select('#info-tooltip');            const sourceId = d.source.id || d.source;            const targetId = d.target.id || d.target;            tooltip.style('display', 'block')                .html(`<strong>相关性</strong><br>${sourceId} ↔ ${targetId}<br>系数: ${d.correlation.toFixed(4)}`)                .style('left', (event.pageX + 10) + 'px')                .style('top', (event.pageY - 10) + 'px');        }        function hideTooltip() {            d3.select('#info-tooltip').style('display', 'none');        }        // 显示Alpha详细信息面板        function showDetailPanel(nodeData) {            const panel = document.getElementById('detail-panel');            const titleElement = document.getElementById('detailAlphaId');            const contentElement = document.getElementById('detailContent');                        titleElement.textContent = `Alpha: ${nodeData.id}`;                        // 构建详细信息 HTML            let html = '';                        // 基本信息            html += '<div class="detail-section">';            html += '<h3>基本信息</h3>';            if (nodeData.create_dt) {                html += `<div class="detail-row">                    <span class="detail-label">创建时间:</span>                    <span class="detail-value">${nodeData.create_dt}</span>                </div>`;            }            if (nodeData.region) {                html += `<div class="detail-row">                    <span class="detail-label">Region:</span>                    <span class="detail-value">${nodeData.region}</span>                </div>`;            }            if (nodeData.universe) {                html += `<div class="detail-row">                    <span class="detail-label">Universe:</span>                    <span class="detail-value">${nodeData.universe}</span>                </div>`;            }            if (nodeData.delay !== null && nodeData.delay !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">Delay:</span>                    <span class="detail-value">${nodeData.delay}</span>                </div>`;            }            if (nodeData.decay !== null && nodeData.decay !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">Decay:</span>                    <span class="detail-value">${nodeData.decay}</span>                </div>`;            }            if (nodeData.neutralization) {                html += `<div class="detail-row">                    <span class="detail-label">Neutralization:</span>                    <span class="detail-value">${nodeData.neutralization}</span>                </div>`;            }            if (nodeData.operatorCount !== null && nodeData.operatorCount !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">操作符数量:</span>                    <span class="detail-value">${nodeData.operatorCount}</span>                </div>`;            }            html += '</div>';                        // 性能指标            html += '<div class="detail-section">';            html += '<h3>性能指标</h3>';            if (nodeData.sharpe !== null && nodeData.sharpe !== undefined) {                const sharpeClass = nodeData.sharpe > 0 ? 'positive' : (nodeData.sharpe < 0 ? 'negative' : '');                html += `<div class="detail-row">                    <span class="detail-label">Sharpe:</span>                    <span class="detail-value ${sharpeClass}">${nodeData.sharpe?.toFixed(4) || '-'}</span>                </div>`;            }            if (nodeData.fitness !== null && nodeData.fitness !== undefined) {                const fitnessClass = nodeData.fitness > 0 ? 'positive' : (nodeData.fitness < 0 ? 'negative' : '');                html += `<div class="detail-row">                    <span class="detail-label">Fitness:</span>                    <span class="detail-value ${fitnessClass}">${nodeData.fitness?.toFixed(4) || '-'}</span>                </div>`;            }            if (nodeData.returns !== null && nodeData.returns !== undefined) {                const returnsClass = nodeData.returns > 0 ? 'positive' : (nodeData.returns < 0 ? 'negative' : '');                html += `<div class="detail-row">                    <span class="detail-label">Returns:</span>                    <span class="detail-value ${returnsClass}">${nodeData.returns?.toFixed(4) || '-'}</span>                </div>`;            }            if (nodeData.turnover !== null && nodeData.turnover !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">Turnover:</span>                    <span class="detail-value">${nodeData.turnover?.toFixed(4) || '-'}</span>                </div>`;            }            if (nodeData.margin !== null && nodeData.margin !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">Margin:</span>                    <span class="detail-value">${nodeData.margin?.toFixed(4) || '-'}</span>                </div>`;            }            if (nodeData.drawdown !== null && nodeData.drawdown !== undefined) {                const drawdownClass = nodeData.drawdown < 0 ? 'negative' : '';                html += `<div class="detail-row">                    <span class="detail-label">Drawdown:</span>                    <span class="detail-value ${drawdownClass}">${nodeData.drawdown?.toFixed(4) || '-'}</span>                </div>`;            }            if (nodeData.longCount !== null && nodeData.longCount !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">Long Count:</span>                    <span class="detail-value">${nodeData.longCount?.toFixed(2) || '-'}</span>                </div>`;            }            if (nodeData.shortCount !== null && nodeData.shortCount !== undefined) {                html += `<div class="detail-row">                    <span class="detail-label">Short Count:</span>                    <span class="detail-value">${nodeData.shortCount?.toFixed(2) || '-'}</span>                </div>`;            }            html += '</div>';                        // 点数分配            if (allocations[nodeData.id]) {                html += '<div class="detail-section">';                html += '<h3>点数分配</h3>';                html += `<div class="detail-row">                    <span class="detail-label">已分配点数:</span>                    <span class="detail-value positive">${allocations[nodeData.id].toLocaleString()}</span>                </div>`;                html += '</div>';            }                        // 表达式            if (nodeData.code) {                html += '<div class="detail-section">';                html += '<h3>表达式</h3>';                html += `<div class="detail-code">${nodeData.code}</div>`;                html += '</div>';            }                        contentElement.innerHTML = html;            panel.style.display = 'block';        }        // 关闭详细信息面板        function closeDetailPanel() {            document.getElementById('detail-panel').style.display = 'none';        }        // 更新统计信息        function updateStats() {            document.getElementById('nodeCount').textContent = graphData.nodes.length;            document.getElementById('linkCount').textContent = graphData.links.length;        }        // 更新模式指示器        function updateModeIndicator(text) {            document.getElementById('modeIndicator').textContent = text;        }        // 切换列表显示        function toggleList(listId) {            const list = document.getElementById(listId);            const icon = document.getElementById(listId + 'Icon');                        if (list.classList.contains('collapsed')) {                list.classList.remove('collapsed');                icon.classList.remove('collapsed');            } else {                list.classList.add('collapsed');                icon.classList.add('collapsed');            }        }        // 更新Alpha列表        function updateAlphaList() {            const container = document.getElementById('alphaListContent');                        if (originalData.nodes.length === 0) {                container.innerHTML = '<div class="list-empty">未加载数据</div>';                return;            }            const searchTerm = document.getElementById('alphaSearch').value.toLowerCase();            const filteredNodes = originalData.nodes.filter(n =>                 n.id.toLowerCase().includes(searchTerm)            );            if (filteredNodes.length === 0) {                container.innerHTML = '<div class="list-empty">未找到匹配的Alpha</div>';                return;            }            container.innerHTML = filteredNodes                .sort((a, b) => a.id.localeCompare(b.id))                .map(node => `                    <div class="list-item" onclick="event.target.tagName !== 'INPUT' && locateNode('${node.id}')">                        <span class="item-name">${node.id}</span>                        <input type="number"                                class="allocation-input"                                value="${allocations[node.id] || 0}"                               min="0"                               max="${TOTAL_POINTS}"                               placeholder="0"                               onchange="updateAllocation('${node.id}', this.value)"                               onclick="event.stopPropagation()">                    </div>                `).join('');        }        // 更新连线列表        function updateLinkList() {            const container = document.getElementById('linkListContent');                        if (graphData.links.length === 0) {                container.innerHTML = '<div class="list-empty">当前阈值下无连线</div>';                return;            }            const searchTerm = document.getElementById('linkSearch').value.toLowerCase();            const filteredLinks = graphData.links.filter(l => {                const sourceId = (l.source.id || l.source).toLowerCase();                const targetId = (l.target.id || l.target).toLowerCase();                return sourceId.includes(searchTerm) || targetId.includes(searchTerm);            });            if (filteredLinks.length === 0) {                container.innerHTML = '<div class="list-empty">未找到匹配的连线</div>';                return;            }            // 按相关性绝对值排序            const sortedLinks = filteredLinks.sort((a, b) =>                 Math.abs(b.correlation) - Math.abs(a.correlation)            );            container.innerHTML = sortedLinks.map(link => {                const sourceId = link.source.id || link.source;                const targetId = link.target.id || link.target;                const corr = link.correlation;                const className = corr > 0 ? 'positive' : 'negative';                                return `                    <div class="list-item ${className}" onclick="locateLink('${sourceId}', '${targetId}')">                        <span class="item-name">${sourceId} ↔ ${targetId}</span>                        <span class="item-value">${corr.toFixed(4)}</span>                    </div>                `;            }).join('');        }        // 更新已删除节点列表        function updateDeletedNodesList() {            const container = document.getElementById('deletedNodesContent');                        if (deletedNodes.length === 0) {                container.innerHTML = '<div class="list-empty">无已删除节点</div>';                return;            }            container.innerHTML = deletedNodes.map((item, index) => `                <div class="list-item deleted-item">                    <div style="flex: 1;">                        <div class="item-name">${item.node.id}</div>                        <div style="font-size: 10px; color: #888; margin-top: 2px;">                            ${item.deletedAt} | ${item.links.length}条连线                        </div>                    </div>                    <button class="restore-btn" onclick="restoreNode(${index})" title="恢复节点">↻</button>                </div>            `).join('');        }        // 控制面板事件        document.getElementById('fileInput').addEventListener('change', function(e) {            const file = e.target.files[0];            if (file) {                const reader = new FileReader();                reader.onload = function(event) {                    try {                        const data = JSON.parse(event.target.result);                        originalData = {                            nodes: data.nodes.map(n => ({...n})),                            links: data.links.map(l => ({...l}))                        };                        document.getElementById('regionInfo').textContent = data.region || '-';                        updateGraph();                    } catch (err) {                        alert('文件解析失败: ' + err.message);                    }                };                reader.readAsText(file);            }        });        document.getElementById('threshold').addEventListener('input', function(e) {            currentThreshold = parseFloat(e.target.value);            document.getElementById('thresholdValue').textContent = currentThreshold.toFixed(2);            updateGraph();        });        document.getElementById('linkDistance').addEventListener('input', function(e) {            const value = parseInt(e.target.value);            document.getElementById('distanceValue').textContent = value;            simulation.force('link').distance(value);            simulation.alpha(1).restart();        });        document.getElementById('chargeStrength').addEventListener('input', function(e) {            const value = parseInt(e.target.value);            document.getElementById('chargeValue').textContent = value;            simulation.force('charge').strength(value);            simulation.alpha(1).restart();        });        document.getElementById('addLinkBtn').addEventListener('click', function() {            if (mode === 'addLink') {                mode = 'normal';                this.textContent = '连线模式: OFF';                this.style.background = '#00d9ff';                selectedNode = null;                if (node) node.selectAll('circle').style('fill', '#00d9ff');                updateModeIndicator('正常模式');            } else {                mode = 'addLink';                this.textContent = '连线模式: ON';                this.style.background = '#4caf50';                document.getElementById('removeLinkBtn').textContent = '删除连线模式: OFF';                document.getElementById('removeLinkBtn').style.background = '#00d9ff';                document.getElementById('removeNodeBtn').textContent = '删除节点模式: OFF';                document.getElementById('removeNodeBtn').style.background = '#00d9ff';                updateModeIndicator('连线模式: 选择两个节点以添加连线');            }        });        document.getElementById('removeLinkBtn').addEventListener('click', function() {            if (mode === 'removeLink') {                mode = 'normal';                this.textContent = '删除连线模式: OFF';                this.style.background = '#00d9ff';                updateModeIndicator('正常模式');            } else {                mode = 'removeLink';                this.textContent = '删除连线模式: ON';                this.style.background = '#ff6b6b';                document.getElementById('addLinkBtn').textContent = '连线模式: OFF';                document.getElementById('addLinkBtn').style.background = '#00d9ff';                document.getElementById('removeNodeBtn').textContent = '删除节点模式: OFF';                document.getElementById('removeNodeBtn').style.background = '#00d9ff';                selectedNode = null;                if (node) node.selectAll('circle').style('fill', '#00d9ff');                updateModeIndicator('删除连线模式: 点击连线以删除');            }        });        document.getElementById('removeNodeBtn').addEventListener('click', function() {            if (mode === 'removeNode') {                mode = 'normal';                this.textContent = '删除节点模式: OFF';                this.style.background = '#00d9ff';                updateModeIndicator('正常模式');            } else {                mode = 'removeNode';                this.textContent = '删除节点模式: ON';                this.style.background = '#ff9800';                document.getElementById('addLinkBtn').textContent = '连线模式: OFF';                document.getElementById('addLinkBtn').style.background = '#00d9ff';                document.getElementById('removeLinkBtn').textContent = '删除连线模式: OFF';                document.getElementById('removeLinkBtn').style.background = '#00d9ff';                selectedNode = null;                if (node) node.selectAll('circle').style('fill', '#00d9ff');                updateModeIndicator('删除节点模式: 点击节点以删除');            }        });        document.getElementById('resetBtn').addEventListener('click', function() {            if (node) {                node.each(d => {                    d.fx = null;                    d.fy = null;                });                simulation.alpha(1).restart();            }        });        // 点数分配相关函数        function updateAllocation(alphaId, value) {            const points = parseInt(value) || 0;            allocations[alphaId] = points;            updateAllocationStats();            updateGraph();        }        function updateAllocationStats() {            const allocated = Object.values(allocations).reduce((sum, val) => sum + val, 0);            const remaining = TOTAL_POINTS - allocated;                        document.getElementById('allocatedPoints').textContent = allocated.toLocaleString();            document.getElementById('remainingPoints').textContent = remaining.toLocaleString();                        // 更新颜色提示            const remainingElement = document.getElementById('remainingPoints');            if (remaining < 0) {                remainingElement.style.color = '#ff6b6b';            } else if (remaining === 0) {                remainingElement.style.color = '#4caf50';            } else {                remainingElement.style.color = '#00d9ff';            }        }        function saveAllocation() {            const allocationData = {                totalPoints: TOTAL_POINTS,                allocatedPoints: Object.values(allocations).reduce((sum, val) => sum + val, 0),                timestamp: new Date().toISOString(),                region: document.getElementById('regionInfo').textContent,                allocations: allocations,                details: originalData.nodes.map(node => ({                    alphaId: node.id,                    alphaName: node.name,                    points: allocations[node.id] || 0                })).filter(item => item.points > 0)            };                        const blob = new Blob([JSON.stringify(allocationData, null, 2)], { type: 'application/json' });            const url = URL.createObjectURL(blob);            const a = document.createElement('a');            a.href = url;            a.download = `alpha_allocation_${allocationData.region}_${Date.now()}.json`;            a.click();            URL.revokeObjectURL(url);                        alert(`分配方案已保存！\n已分配: ${allocationData.allocatedPoints.toLocaleString()}\n共 ${allocationData.details.length} 个Alpha`);        }        function loadAllocation(data) {            if (data.allocations) {                allocations = {...data.allocations};                                // 检查是否是按簇分配的数据（通过检查是否有明显的簇结构）                // 重新计算簇信息以便显示                if (originalData.nodes.length > 0) {                    clusters = findClusters();                    if (clusters.length > 1 || (clusters.length === 1 && clusters[0].length < originalData.nodes.length)) {                        displayClusterInfo();                    }                }                                updateAllocationStats();                updateGraph();                updateAlphaList();                alert(`分配方案已加载！\n已分配: ${Object.values(allocations).reduce((sum, val) => sum + val, 0).toLocaleString()}`);            }        }        function clearAllocation() {            if (confirm('确定要清空所有点数分配吗？')) {                allocations = {};                updateAllocationStats();                updateGraph();                updateAlphaList();                hideClusterInfo();            }        }        function autoAllocatePoints() {            const nodeCount = originalData.nodes.length;            if (nodeCount === 0) {                alert('请先加载Alpha数据！');                return;            }                        if (confirm(`将 ${TOTAL_POINTS.toLocaleString()} 点数平均分配给 ${nodeCount} 个Alpha？\n每个约 ${Math.floor(TOTAL_POINTS / nodeCount).toLocaleString()} 点`)) {                allocations = {};                const pointsPerNode = Math.floor(TOTAL_POINTS / nodeCount);                let remaining = TOTAL_POINTS - (pointsPerNode * nodeCount);                                originalData.nodes.forEach((node, index) => {                    allocations[node.id] = pointsPerNode + (index < remaining ? 1 : 0);                });                                updateAllocationStats();                updateGraph();                updateAlphaList();            }        }        // 使用并查集检测连通分量（簇）        function findClusters() {            if (originalData.nodes.length === 0) {                return [];            }            // 构建当前阈值下的邻接表            const adjacencyList = {};            originalData.nodes.forEach(node => {                adjacencyList[node.id] = [];            });            // 只考虑满足当前阈值的连线            originalData.links.forEach(link => {                if (Math.abs(link.correlation) >= currentThreshold) {                    const sourceId = link.source.id || link.source;                    const targetId = link.target.id || link.target;                    adjacencyList[sourceId].push(targetId);                    adjacencyList[targetId].push(sourceId);                }            });            // DFS查找连通分量            const visited = {};            const clusters = [];            function dfs(nodeId, cluster) {                visited[nodeId] = true;                cluster.push(nodeId);                                adjacencyList[nodeId].forEach(neighborId => {                    if (!visited[neighborId]) {                        dfs(neighborId, cluster);                    }                });            }            originalData.nodes.forEach(node => {                if (!visited[node.id]) {                    const cluster = [];                    dfs(node.id, cluster);                    clusters.push(cluster);                }            });            // 按簇大小降序排序            clusters.sort((a, b) => b.length - a.length);                        return clusters;        }        // 按簇分配点数        function clusterAllocatePoints() {            if (originalData.nodes.length === 0) {                alert('请先加载Alpha数据！');                return;            }            // 检测簇            clusters = findClusters();                        if (clusters.length === 0) {                alert('未检测到任何节点！');                return;            }            // 生成簇信息摘要            const clusterSummary = clusters.map((cluster, index) =>                 `簇${index + 1}: ${cluster.length}个节点`            ).join('\n');            const message = `检测到 ${clusters.length} 个簇（当前阈值: ${currentThreshold.toFixed(2)}）\n\n` +                           clusterSummary +                           `\n\n将 ${TOTAL_POINTS.toLocaleString()} 点数按簇分配？\n` +                           `每簇约 ${Math.floor(TOTAL_POINTS / clusters.length).toLocaleString()} 点`;            if (confirm(message)) {                allocations = {};                const pointsPerCluster = Math.floor(TOTAL_POINTS / clusters.length);                let remainingPoints = TOTAL_POINTS - (pointsPerCluster * clusters.length);                clusters.forEach((cluster, clusterIndex) => {                    // 给每个簇分配点数（前几个簇多分配1点以用完剩余点数）                    const clusterPoints = pointsPerCluster + (clusterIndex < remainingPoints ? 1 : 0);                                        // 在簇内平均分配                    const pointsPerNode = Math.floor(clusterPoints / cluster.length);                    let clusterRemaining = clusterPoints - (pointsPerNode * cluster.length);                    cluster.forEach((nodeId, nodeIndex) => {                        allocations[nodeId] = pointsPerNode + (nodeIndex < clusterRemaining ? 1 : 0);                    });                });                updateAllocationStats();                updateGraph();                updateAlphaList();                displayClusterInfo();            }        }        // 显示簇信息        function displayClusterInfo() {            const clusterSection = document.getElementById('clusterSection');            const clusterInfoDiv = document.getElementById('clusterInfo');            const clusterThresholdSpan = document.getElementById('clusterThreshold');                        if (clusters.length === 0) {                clusterSection.style.display = 'none';                return;            }            clusterSection.style.display = 'block';            clusterThresholdSpan.textContent = currentThreshold.toFixed(2);                        const clusterDetails = clusters.map((cluster, index) => {                const clusterPoints = cluster.reduce((sum, nodeId) => sum + (allocations[nodeId] || 0), 0);                const avgPoints = Math.floor(clusterPoints / cluster.length);                const nodeList = cluster.slice(0, 5).join(', ') + (cluster.length > 5 ? '...' : '');                                return `<div class="list-item" style="flex-direction: column; align-items: flex-start;">                    <div style="width: 100%; display: flex; justify-content: space-between; margin-bottom: 5px;">                        <span style="color: #00d9ff; font-weight: bold;">簇${index + 1}</span>                        <span style="color: #4caf50;">${clusterPoints.toLocaleString()}点</span>                    </div>                    <div style="font-size: 11px; color: #aaa;">                        节点数: ${cluster.length} | 平均: ${avgPoints.toLocaleString()}点/节点                    </div>                    <div style="font-size: 10px; color: #666; margin-top: 3px;">                        ${nodeList}                    </div>                </div>`;            }).join('');            clusterInfoDiv.innerHTML = clusterDetails;        }        // 隐藏簇信息（当清空或平均分配时）        function hideClusterInfo() {            document.getElementById('clusterSection').style.display = 'none';            clusters = [];        }        // 点数分配按钮事件        document.getElementById('saveAllocationBtn').addEventListener('click', saveAllocation);                document.getElementById('loadAllocationBtn').addEventListener('click', function() {            document.getElementById('allocationFileInput').click();        });                document.getElementById('allocationFileInput').addEventListener('change', function(e) {            const file = e.target.files[0];            if (file) {                const reader = new FileReader();                reader.onload = function(event) {                    try {                        const data = JSON.parse(event.target.result);                        loadAllocation(data);                    } catch (err) {                        alert('文件解析失败: ' + err.message);                    }                };                reader.readAsText(file);            }            e.target.value = ''; // 清空input，允许重复加载同一文件        });                document.getElementById('clearAllocationBtn').addEventListener('click', clearAllocation);        document.getElementById('autoAllocateBtn').addEventListener('click', () => {            autoAllocatePoints();            hideClusterInfo();        });        document.getElementById('clusterAllocateBtn').addEventListener('click', clusterAllocatePoints);        // 搜索框事件        document.getElementById('alphaSearch').addEventListener('input', updateAlphaList);        document.getElementById('linkSearch').addEventListener('input', updateLinkList);        // 初始化        initSVG();        initSimulation();        // 窗口大小改变时重新调整        window.addEventListener('resize', () => {            const container = d3.select('#graph-container');            const width = container.node().clientWidth;            const height = container.node().clientHeight;                        svg.attr('width', width).attr('height', height);            simulation.force('center', d3.forceCenter(width / 2, height / 2));            simulation.alpha(1).restart();        });    </script></body></html>
```

**后端代码**

```
import pymysqlimport jsonimport numpy as npimport pandas as pdimport osfrom typing import List, Dict, Optional, Tuplefrom datetime import datetimefrom itertools import combinationsDB_CONFIG = {   # 京东云ip   'host': '111.111.111.111',   'user': 'root',   'password': 'root',   'database': 'root',   'charset': 'utf8'}class AlphaSubmitDB:    """Alpha提交数据库操作类"""       def __init__(self):        self.config = DB_CONFIG       def get_connection(self):        """获取数据库连接"""        return pymysql.connect(**self.config)       def get_by_region(self, region: str, limit: Optional[int] = None) -> List[Dict]:        """        根据region获取alpha数据               Args:            region: 地区代码，如 'USA', 'CHN' 等            limit: 限制返回的记录数量，默认返回所有                   Returns:            包含alpha记录的字典列表        """        conn = self.get_connection()        cursor = conn.cursor(pymysql.cursors.DictCursor)               try:            sql = "SELECT * FROM alpha_submit WHERE region = %s ORDER BY create_dt DESC"            if limit:                sql += f" LIMIT {limit}"                       cursor.execute(sql, (region,))            results = cursor.fetchall()            return results        finally:            cursor.close()            conn.close()       def parse_pnl_data(self, pnl_json: str) -> pd.Series:        """        解析pnl JSON数据，返回pandas Series               Args:            pnl_json: pnl的JSON字符串                   Returns:            以日期为索引，pnl为值的Series        """        if not pnl_json:            return pd.Series()               pnl_data = json.loads(pnl_json)        records = pnl_data.get('records', [])               dates = [record[0] for record in records]        pnls = [record[1] for record in records]               return pd.Series(pnls, index=pd.to_datetime(dates))       def calculate_correlations_by_region(self, region: str) -> pd.DataFrame:        """        计算指定region下所有alpha之间的皮尔逊相关系数               Args:            region: 地区代码，如 'USA', 'CHN' 等                   Returns:            相关系数矩阵DataFrame        """        print(f"正在获取 {region} 地区的alpha数据...")        alphas = self.get_by_region(region)        print(f"共获取 {len(alphas)} 个alpha")               if len(alphas) < 2:            print("alpha数量少于2个，无法计算相关性")            return pd.DataFrame()               # 构建pnl矩阵        print("正在解析pnl数据...")        pnl_dict = {}        valid_alphas = []               for alpha in alphas:            alpha_id = alpha['id']            pnl_series = self.parse_pnl_data(alpha.get('pnl'))                       if len(pnl_series) > 0:                pnl_dict[alpha_id] = pnl_series                valid_alphas.append(alpha)               print(f"有效alpha数量: {len(valid_alphas)}")               if len(valid_alphas) < 2:            print("有效alpha少于2个，无法计算相关性")            return pd.DataFrame()               # 转换为DataFrame        pnl_df = pd.DataFrame(pnl_dict)               # 使用前向填充处理缺失值，然后shift(1)        # 这样做的原因：避免使用未来信息，计算t日的相关性时使用t-1日的数据        pnl_df = pnl_df.ffill().shift(1)               # 计算收益率（pnl的差分）        print("正在计算收益率...")        alpha_rets = pnl_df.diff()               print("正在计算相关系数矩阵...")        corr_matrix = alpha_rets.corr(method='pearson')               return corr_matrix       def save_correlation_to_file(self, corr_matrix: pd.DataFrame, region: str):        """        将相关系数矩阵保存到CSV文件               Args:            corr_matrix: 相关系数矩阵            region: 地区代码，用于生成文件名        """        # 获取当前脚本所在目录        current_dir = os.path.dirname(os.path.abspath(__file__))               filename = f'alpha_correlation_{region}.csv'        filepath = os.path.join(current_dir, filename)               corr_matrix.to_csv(filepath)        print(f"相关系数矩阵已保存到 {filepath}")        return filepath       def get_high_correlation_pairs_from_matrix(self, corr_matrix: pd.DataFrame,                                               threshold: float = 0.8) -> List[Tuple[str, str, float]]:        """        从相关系数矩阵中获取高相关性的alpha对               Args:            corr_matrix: 相关系数矩阵            threshold: 相关系数阈值                   Returns:            高相关性的alpha对列表 [(alpha_id_1, alpha_id_2, correlation), ...]        """        high_corr_pairs = []        alpha_ids = corr_matrix.index.tolist()               for i, alpha1 in enumerate(alpha_ids):            for alpha2 in alpha_ids[i+1:]:                corr_value = corr_matrix.loc[alpha1, alpha2]                if not np.isnan(corr_value) and abs(corr_value) >= threshold:                    high_corr_pairs.append((alpha1, alpha2, corr_value))               # 按相关系数绝对值降序排列        high_corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)        return high_corr_pairs       def export_network_data(self, corr_matrix: pd.DataFrame, region: str, threshold: float = 0.0):        """        将相关系数矩阵导出为网络图所需的JSON格式               Args:            corr_matrix: 相关系数矩阵            region: 地区代码            threshold: 相关系数阈值，低于此值的边不会被包含（默认0表示导出所有）                   Returns:            JSON文件路径        """        current_dir = os.path.dirname(os.path.abspath(__file__))               # 重新获取alpha详细数据        alphas = self.get_by_region(region)        alpha_dict = {alpha['id']: alpha for alpha in alphas}               # 构建节点数据（包含详细信息）        nodes = []        alpha_ids = corr_matrix.index.tolist()        for alpha_id in alpha_ids:            alpha_info = alpha_dict.get(alpha_id, {})            node = {                'id': alpha_id,                'name': alpha_id,                'create_dt': str(alpha_info.get('create_dt', '')),                'region': alpha_info.get('region', ''),                'universe': alpha_info.get('universe', ''),                'delay': alpha_info.get('delay'),                'decay': alpha_info.get('decay'),                'neutralization': alpha_info.get('neutralization', ''),                'code': alpha_info.get('code', ''),                'operatorCount': alpha_info.get('operatorCount'),                'turnover': alpha_info.get('turnover'),                'returns': alpha_info.get('returns'),                'margin': alpha_info.get('margin'),                'sharpe': alpha_info.get('sharpe'),                'fitness': alpha_info.get('fitness'),                'drawdown': alpha_info.get('drawdown'),                'longCount': alpha_info.get('longCount'),                'shortCount': alpha_info.get('shortCount')            }            nodes.append(node)               # 构建边数据 - 导出所有边，让前端控制显示        links = []        for i, alpha1 in enumerate(alpha_ids):            for alpha2 in alpha_ids[i+1:]:                corr_value = corr_matrix.loc[alpha1, alpha2]                if not np.isnan(corr_value) and abs(corr_value) >= threshold:                    links.append({                        'source': alpha1,                        'target': alpha2,                        'correlation': float(corr_value),                        'value': float(abs(corr_value))  # 用于边的粗细                    })               # 构建完整数据        network_data = {            'nodes': nodes,            'links': links,            'region': region,            'threshold': threshold        }               # 保存为JSON文件        filename = f'alpha_network_{region}.json'        filepath = os.path.join(current_dir, filename)               with open(filepath, 'w', encoding='utf-8') as f:            json.dump(network_data, f, indent=2, ensure_ascii=False)               print(f"网络数据已保存到 {filepath}")        return filepath# 使用示例if __name__ == "__main__":    db = AlphaSubmitDB()       # 指定要分析的region    regions = ['GLB']  # 可以分析多个region       for region in regions:        print("=" * 60)        print(f"开始处理 {region} 地区的alpha相关性...")        print("=" * 60)               # 计算该region下所有alpha的相关系数矩阵        corr_matrix = db.calculate_correlations_by_region(region)               if not corr_matrix.empty:            # 保存到文件            filename = db.save_correlation_to_file(corr_matrix, region)                       # 导出网络图数据（导出所有边，由前端页面控制阈值过滤）            json_file = db.export_network_data(corr_matrix, region, threshold=0.0)                       print(f"\n相关系数矩阵维度: {corr_matrix.shape}")            print("\n相关系数矩阵预览:")            print(corr_matrix.iloc[:5, :5])  # 显示前5x5                       # 获取高相关性的alpha对            print("\n" + "=" * 60)            print("高相关性alpha对 (|相关系数| >= 0.8):")            high_corr_pairs = db.get_high_correlation_pairs_from_matrix(corr_matrix, threshold=0.8)                       if high_corr_pairs:                for i, (alpha1, alpha2, corr) in enumerate(high_corr_pairs[:10], 1):                    print(f"{i}. {alpha1} <-> {alpha2}: {corr:.4f}")            else:                print("未发现高相关性的alpha对")                       print(f"\n{region} 地区处理完成！\n")        else:            print(f"{region} 地区没有足够的数据进行相关性分析\n")
```

我预先已经将数据保存到数据库了，各位大佬可以自行进行修改代码，保证导出的格式一致即可：

```
{  "nodes": [    {      "id": "alpha的ID",      "name": "alpha的ID",      "create_dt": "创建时间字符串",      "region": "地区代码",      "universe": "universe",      "delay": 延迟值,      "decay": 衰减值,      "neutralization": "中性化方式",      "code": "alpha代码",      "operatorCount": 操作符数量,      "turnover": 换手率,      "returns": 回报率,      "margin": margin值,      "sharpe": sharpe比率,      "fitness": 适应度,      "drawdown": 回撤,      "longCount": 多头数量,      "shortCount": 空头数量    }    // ... 更多节点  ],  "links": [    {      "source": "源alpha的ID",      "target": "目标alpha的ID",      "correlation": 0.85,  // 实际相关系数值（可正可负）      "value": 0.85         // 相关系数的绝对值（用于边的粗细）    }    // ... 更多边  ],  "region": "GLB",  "threshold": 0.0}
```

**打分代码**

打分代码就不贴了，论坛中有很多，读取导出的点数分配文件即可。

---

### 帖子 #38: 【MYSQL】（一）将自己权限内的数据集和数据字段保存到本地mysql
- **主帖链接**: 【MYSQL】一将自己权限内的数据集和数据字段保存到本地mysql.md
- **讨论数**: 3

> 这篇帖子主打一个开箱即用，复制建表语句执行后，直接执行对应的方法即可
> 之前在论坛里也借鉴过很多大佬的方法，但有些地方因为配置不同所以会有问题
> 这里已经将每个模块尽可能的独立出来了

## 1. 保存自己权限内的数据集datasets

### （1）数据集表

这里的保存逻辑是id、region、delay、universe按一条数据来算。

```
CREATE TABLE `datasets` (  `id` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'id',  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'name',  `description` text COLLATE utf8_unicode_ci COMMENT '详细描述',  `category` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '类别',  `subcategory` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '子类别',  `region` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'region',  `delay` int(11) DEFAULT NULL COMMENT 'delay',  `universe` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'universe',  `coverage` double DEFAULT NULL COMMENT '覆盖率',  `valueScore` double DEFAULT NULL COMMENT '价值分',  `userCount` int(11) DEFAULT NULL COMMENT '用户数量',  `alphaCount` int(11) DEFAULT NULL COMMENT 'Alpha 数量',  `fieldCount` int(11) DEFAULT NULL COMMENT '字段数量',  `pyramidMultiplier` double DEFAULT NULL COMMENT 'pyramid 倍数',  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间，自动更新',  UNIQUE KEY `idx_unique_dataset` (`id`,`region`,`delay`,`universe`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='数据集';
```

### （2）保存方法

```
region_values = ["USA", "GLB", "EUR", "ASI"]delay_values = {    "USA": [0, 1],    "GLB": [1],    "EUR": [0, 1],    "ASI": [1]}universe_values = {    "USA": ["TOP3000", "TOP1000", "TOP500", "TOP200", "ILLIQUID_MINVOL1M", "TOPSP500"],    "GLB": ["TOP3000", "MINVOL1M"],    "EUR": ["TOP1200", "TOP800", "TOP400", "ILLIQUID_MINVOL1M"],    "ASI": ["MINVOL1M", "ILLIQUID_MINVOL1M"]}DB_CONFIG = {    'host': '',    'user': '',    'password': '',    'database': '',    'charset': 'utf8'}def save_datasets():    url = "[链接已屏蔽]    connection = pymysql.connect(**DB_CONFIG)    cursor = connection.cursor()    total_num = 0    for region in region_values:        for delay in delay_values[region]:            for universe in universe_values[region]:                params = {                    "region": region,                    "delay": delay,                    "universe": universe,                    "instrumentType": "EQUITY",                }                response = s.get(url, params=params)                data = response.json().get('results', [])                if not data:                    continue                for item in data:                    id = item.get('id')                    name = item.get('name')                    description = item.get('description')                    category_id = item.get('category', {}).get('id')                    subcategory_id = item.get('subcategory', {}).get('id')                    region = item.get('region')                    delay = item.get('delay')                    universe = item.get('universe')                    coverage = item.get('coverage')                    value_score = item.get('valueScore')                    user_count = item.get('userCount')                    alpha_count = item.get('alphaCount')                    field_count = item.get('fieldCount')                    pyramid_multiplier = item.get('pyramidMultiplier')                    sql = """                    INSERT INTO datasets (                        id, name, description, category, subcategory, region, delay, universe,                         coverage, valueScore, userCount, alphaCount, fieldCount, pyramidMultiplier                    ) VALUES (                        %s, %s, %s, %s, %s, %s, %s, %s,                         %s, %s, %s, %s, %s, %s                    )                    ON DUPLICATE KEY UPDATE                         name = VALUES(name),                        description = VALUES(description),                        category = VALUES(category),                        subcategory = VALUES(subcategory),                        region = VALUES(region),                        delay = VALUES(delay),                        universe = VALUES(universe),                        coverage = VALUES(coverage),                        valueScore = VALUES(valueScore),                        userCount = VALUES(userCount),                        alphaCount = VALUES(alphaCount),                        fieldCount = VALUES(fieldCount),                        pyramidMultiplier = VALUES(pyramidMultiplier)                    """                    cursor.execute(sql, (                        id, name, description, category_id, subcategory_id, region, delay, universe,                         coverage, value_score, user_count, alpha_count, field_count, pyramid_multiplier                    ))                connection.commit()                print(f"成功保存{region} {delay} {universe}的数据集: {len(data)}条")                total_num += len(data)    cursor.close()    connection.close()    print(f"共保存 {total_num} 条数据集")
```

### （3）自行根据json扩展

```
{  "count": 52,  "results": [    {      "id": "analyst11",      "name": "ESG scores",      "description": "Environmental Social Governance scores that exhibit significance with respect to financial metrics - different scores according to grouping and weighing.",      "category": { "id": "analyst", "name": "Analyst" },      "subcategory": { "id": "analyst-esg", "name": "ESG" },      "region": "USA",      "delay": 0,      "universe": "TOP3000",      "coverage": 0.6818,      "valueScore": 3.0,      "userCount": 11,      "alphaCount": 17,      "fieldCount": 197,      "pyramidMultiplier": 1.7,      "themes": [],      "researchPapers": [        {          "type": "discussion",          "title": "Getting started with Analyst Datasets",          "url": "../顾问 CC40930 (Rank 95)/[Commented] Getting started with Analyst DatasetsResearch.md"        }      ]    },    ...    ...  ]}
```

## 2. 保存自己权限内的数据字段data_fields

### （1）数据字段表

保存逻辑同数据集表

```
CREATE TABLE `datafields` (  `id` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '主键 ID',  `description` text COLLATE utf8_unicode_ci COMMENT 'KPI 描述',  `dataset` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '数据集 ID',  `category` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '类别 ID',  `subcategory` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '子类别 ID',  `region` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'region',  `delay` int(11) DEFAULT NULL COMMENT 'delay',  `universe` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'universe',  `type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '矩阵类型',  `coverage` double DEFAULT NULL COMMENT '覆盖率',  `user_count` int(11) DEFAULT NULL COMMENT '用户数量',  `alpha_count` int(11) DEFAULT NULL COMMENT 'Alpha 数量',  `pyramid_multiplier` double DEFAULT NULL COMMENT 'pyramid 倍数',  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间，自动更新',  UNIQUE KEY `idx_unique_dataset` (`id`,`region`,`delay`,`universe`,`dataset`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='字段表';
```

### （2）保存方法

```
def save_data_fields():    url = "[链接已屏蔽]    connection = pymysql.connect(**DB_CONFIG)    cursor = connection.cursor()    total_num = 0    sql_query = """        SELECT id, region, delay, universe        FROM datasets;    """    cursor.execute(sql_query)    results = cursor.fetchall()    for row in results:        params = {            "dataset.id": row[0],      # Dataset ID            "region": row[1],          # Region            "delay": row[2],           # Delay            "universe": row[3],        # Universe            "instrumentType": "EQUITY",  # 固定值            "limit": 50,               # 固定值            "offset": 0                # 固定值        }        count = s.get(url, params=params).json()['count']        for offset in range(0, count, 50):            params['offset'] = offset            response = s.get(url, params=params)            data = response.json().get('results', [])            if not data:                continue            batch_values = []            for item in data:                batch_values.append((                    item.get('id'),                    item.get('description'),                    item.get('dataset', {}).get('id'),                    item.get('category', {}).get('id'),                    item.get('subcategory', {}).get('id'),                    item.get('region'),                    item.get('delay'),                    item.get('universe'),                    item.get('type'),                    item.get('coverage'),                    item.get('userCount'),                    item.get('alphaCount'),                    item.get('pyramidMultiplier')                ))            sql = """                INSERT INTO datafields (                    id, description, dataset, category, subcategory,                     region, delay, universe, type, coverage, user_count,                     alpha_count, pyramid_multiplier                ) VALUES (                    %s, %s, %s, %s, %s,                     %s, %s, %s, %s, %s, %s,                     %s, %s                )                ON DUPLICATE KEY UPDATE                    description = VALUES(description),                    dataset = VALUES(dataset),                    category = VALUES(category),                    subcategory = VALUES(subcategory),                    region = VALUES(region),                    delay = VALUES(delay),                    universe = VALUES(universe),                    type = VALUES(type),                    coverage = VALUES(coverage),                    user_count = VALUES(user_count),                    alpha_count = VALUES(alpha_count),                    pyramid_multiplier = VALUES(pyramid_multiplier);            """            cursor.executemany(sql, batch_values)            connection.commit()            total_num += count        print(f"成功保存{params['dataset.id']} {params['region']} {params['delay']} {params['universe']}的数据字段: {count}条")    cursor.close()    connection.close()    print(f"共保存 {total_num} 条数据字段")
```

### （3）自行根据json扩展

```
{  "count": 197,  "results": [    {      "id": "anl11_1e",      "description": "Aggregate KPI for Pollution Prevention & Environmental Remediation",      "dataset": { "id": "analyst11", "name": "ESG scores" },      "category": { "id": "analyst", "name": "Analyst" },      "subcategory": { "id": "analyst-esg", "name": "ESG" },      "region": "USA",      "delay": 0,      "universe": "TOP3000",      "type": "MATRIX",      "coverage": 0.6396,      "userCount": 1,      "alphaCount": 1,      "pyramidMultiplier": 1.7,      "themes": []    },    ...    ...  ]}
```

> 后续计划：
> 目标：开箱可用，每隔功能模块尽可能独立。
> IMPORTANT：
> 1. 优化顾问的一二三阶模板，这会将全部代码最后放到最后一篇帖子中。
> 2. 构建模板填充模板：将自己的alpha模板已经需要遍历的数据集或字段填充好，程序将自行运行。
> POINT：
> 1. 定时任务，保证云服务器上账号始终保持登录状态。
> 2. 独立的check方法，24小时不停的check新提交过的alpha已经已经check过的alpha，并将其结果保存到mysql数据库中。
> 3. 优化 multi_simulate 方法，暂时想的是多线程提交以及保存提交记录。
> 4. 消息推送：报错推送、任务完成（simulate、check）推送。
> 5. AI 方面还在研究...

---

### 帖子 #39: 【MYSQL】（一）将自己权限内的数据集和数据字段保存到本地mysql
- **主帖链接**: https://support.worldquantbrain.com【MYSQL】一将自己权限内的数据集和数据字段保存到本地mysql_29466218553367.md
- **讨论数**: 3

> 这篇帖子主打一个开箱即用，复制建表语句执行后，直接执行对应的方法即可
> 之前在论坛里也借鉴过很多大佬的方法，但有些地方因为配置不同所以会有问题
> 这里已经将每个模块尽可能的独立出来了

## 1. 保存自己权限内的数据集datasets

### （1）数据集表

这里的保存逻辑是id、region、delay、universe按一条数据来算。

```
CREATE TABLE `datasets` (  `id` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'id',  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'name',  `description` text COLLATE utf8_unicode_ci COMMENT '详细描述',  `category` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '类别',  `subcategory` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '子类别',  `region` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'region',  `delay` int(11) DEFAULT NULL COMMENT 'delay',  `universe` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'universe',  `coverage` double DEFAULT NULL COMMENT '覆盖率',  `valueScore` double DEFAULT NULL COMMENT '价值分',  `userCount` int(11) DEFAULT NULL COMMENT '用户数量',  `alphaCount` int(11) DEFAULT NULL COMMENT 'Alpha 数量',  `fieldCount` int(11) DEFAULT NULL COMMENT '字段数量',  `pyramidMultiplier` double DEFAULT NULL COMMENT 'pyramid 倍数',  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间，自动更新',  UNIQUE KEY `idx_unique_dataset` (`id`,`region`,`delay`,`universe`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='数据集';
```

### （2）保存方法

```
region_values = ["USA", "GLB", "EUR", "ASI"]delay_values = {    "USA": [0, 1],    "GLB": [1],    "EUR": [0, 1],    "ASI": [1]}universe_values = {    "USA": ["TOP3000", "TOP1000", "TOP500", "TOP200", "ILLIQUID_MINVOL1M", "TOPSP500"],    "GLB": ["TOP3000", "MINVOL1M"],    "EUR": ["TOP1200", "TOP800", "TOP400", "ILLIQUID_MINVOL1M"],    "ASI": ["MINVOL1M", "ILLIQUID_MINVOL1M"]}DB_CONFIG = {    'host': '',    'user': '',    'password': '',    'database': '',    'charset': 'utf8'}def save_datasets():    url = "[链接已屏蔽]    connection = pymysql.connect(**DB_CONFIG)    cursor = connection.cursor()    total_num = 0    for region in region_values:        for delay in delay_values[region]:            for universe in universe_values[region]:                params = {                    "region": region,                    "delay": delay,                    "universe": universe,                    "instrumentType": "EQUITY",                }                response = s.get(url, params=params)                data = response.json().get('results', [])                if not data:                    continue                for item in data:                    id = item.get('id')                    name = item.get('name')                    description = item.get('description')                    category_id = item.get('category', {}).get('id')                    subcategory_id = item.get('subcategory', {}).get('id')                    region = item.get('region')                    delay = item.get('delay')                    universe = item.get('universe')                    coverage = item.get('coverage')                    value_score = item.get('valueScore')                    user_count = item.get('userCount')                    alpha_count = item.get('alphaCount')                    field_count = item.get('fieldCount')                    pyramid_multiplier = item.get('pyramidMultiplier')                    sql = """                    INSERT INTO datasets (                        id, name, description, category, subcategory, region, delay, universe,                         coverage, valueScore, userCount, alphaCount, fieldCount, pyramidMultiplier                    ) VALUES (                        %s, %s, %s, %s, %s, %s, %s, %s,                         %s, %s, %s, %s, %s, %s                    )                    ON DUPLICATE KEY UPDATE                         name = VALUES(name),                        description = VALUES(description),                        category = VALUES(category),                        subcategory = VALUES(subcategory),                        region = VALUES(region),                        delay = VALUES(delay),                        universe = VALUES(universe),                        coverage = VALUES(coverage),                        valueScore = VALUES(valueScore),                        userCount = VALUES(userCount),                        alphaCount = VALUES(alphaCount),                        fieldCount = VALUES(fieldCount),                        pyramidMultiplier = VALUES(pyramidMultiplier)                    """                    cursor.execute(sql, (                        id, name, description, category_id, subcategory_id, region, delay, universe,                         coverage, value_score, user_count, alpha_count, field_count, pyramid_multiplier                    ))                connection.commit()                print(f"成功保存{region} {delay} {universe}的数据集: {len(data)}条")                total_num += len(data)    cursor.close()    connection.close()    print(f"共保存 {total_num} 条数据集")
```

### （3）自行根据json扩展

```
{  "count": 52,  "results": [    {      "id": "analyst11",      "name": "ESG scores",      "description": "Environmental Social Governance scores that exhibit significance with respect to financial metrics - different scores according to grouping and weighing.",      "category": { "id": "analyst", "name": "Analyst" },      "subcategory": { "id": "analyst-esg", "name": "ESG" },      "region": "USA",      "delay": 0,      "universe": "TOP3000",      "coverage": 0.6818,      "valueScore": 3.0,      "userCount": 11,      "alphaCount": 17,      "fieldCount": 197,      "pyramidMultiplier": 1.7,      "themes": [],      "researchPapers": [        {          "type": "discussion",          "title": "Getting started with Analyst Datasets",          "url": "[L2] Getting started with Analyst DatasetsResearch_25238159368215.md"        }      ]    },    ...    ...  ]}
```

## 2. 保存自己权限内的数据字段data_fields

### （1）数据字段表

保存逻辑同数据集表

```
CREATE TABLE `datafields` (  `id` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '主键 ID',  `description` text COLLATE utf8_unicode_ci COMMENT 'KPI 描述',  `dataset` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '数据集 ID',  `category` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '类别 ID',  `subcategory` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '子类别 ID',  `region` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'region',  `delay` int(11) DEFAULT NULL COMMENT 'delay',  `universe` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'universe',  `type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '矩阵类型',  `coverage` double DEFAULT NULL COMMENT '覆盖率',  `user_count` int(11) DEFAULT NULL COMMENT '用户数量',  `alpha_count` int(11) DEFAULT NULL COMMENT 'Alpha 数量',  `pyramid_multiplier` double DEFAULT NULL COMMENT 'pyramid 倍数',  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间，自动更新',  UNIQUE KEY `idx_unique_dataset` (`id`,`region`,`delay`,`universe`,`dataset`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='字段表';
```

### （2）保存方法

```
def save_data_fields():    url = "[链接已屏蔽]    connection = pymysql.connect(**DB_CONFIG)    cursor = connection.cursor()    total_num = 0    sql_query = """        SELECT id, region, delay, universe        FROM datasets;    """    cursor.execute(sql_query)    results = cursor.fetchall()    for row in results:        params = {            "dataset.id": row[0],      # Dataset ID            "region": row[1],          # Region            "delay": row[2],           # Delay            "universe": row[3],        # Universe            "instrumentType": "EQUITY",  # 固定值            "limit": 50,               # 固定值            "offset": 0                # 固定值        }        count = s.get(url, params=params).json()['count']        for offset in range(0, count, 50):            params['offset'] = offset            response = s.get(url, params=params)            data = response.json().get('results', [])            if not data:                continue            batch_values = []            for item in data:                batch_values.append((                    item.get('id'),                    item.get('description'),                    item.get('dataset', {}).get('id'),                    item.get('category', {}).get('id'),                    item.get('subcategory', {}).get('id'),                    item.get('region'),                    item.get('delay'),                    item.get('universe'),                    item.get('type'),                    item.get('coverage'),                    item.get('userCount'),                    item.get('alphaCount'),                    item.get('pyramidMultiplier')                ))            sql = """                INSERT INTO datafields (                    id, description, dataset, category, subcategory,                     region, delay, universe, type, coverage, user_count,                     alpha_count, pyramid_multiplier                ) VALUES (                    %s, %s, %s, %s, %s,                     %s, %s, %s, %s, %s, %s,                     %s, %s                )                ON DUPLICATE KEY UPDATE                    description = VALUES(description),                    dataset = VALUES(dataset),                    category = VALUES(category),                    subcategory = VALUES(subcategory),                    region = VALUES(region),                    delay = VALUES(delay),                    universe = VALUES(universe),                    type = VALUES(type),                    coverage = VALUES(coverage),                    user_count = VALUES(user_count),                    alpha_count = VALUES(alpha_count),                    pyramid_multiplier = VALUES(pyramid_multiplier);            """            cursor.executemany(sql, batch_values)            connection.commit()            total_num += count        print(f"成功保存{params['dataset.id']} {params['region']} {params['delay']} {params['universe']}的数据字段: {count}条")    cursor.close()    connection.close()    print(f"共保存 {total_num} 条数据字段")
```

### （3）自行根据json扩展

```
{  "count": 197,  "results": [    {      "id": "anl11_1e",      "description": "Aggregate KPI for Pollution Prevention & Environmental Remediation",      "dataset": { "id": "analyst11", "name": "ESG scores" },      "category": { "id": "analyst", "name": "Analyst" },      "subcategory": { "id": "analyst-esg", "name": "ESG" },      "region": "USA",      "delay": 0,      "universe": "TOP3000",      "type": "MATRIX",      "coverage": 0.6396,      "userCount": 1,      "alphaCount": 1,      "pyramidMultiplier": 1.7,      "themes": []    },    ...    ...  ]}
```

> 后续计划：
> 目标：开箱可用，每隔功能模块尽可能独立。
> IMPORTANT：
> 1. 优化顾问的一二三阶模板，这会将全部代码最后放到最后一篇帖子中。
> 2. 构建模板填充模板：将自己的alpha模板已经需要遍历的数据集或字段填充好，程序将自行运行。
> POINT：
> 1. 定时任务，保证云服务器上账号始终保持登录状态。
> 2. 独立的check方法，24小时不停的check新提交过的alpha已经已经check过的alpha，并将其结果保存到mysql数据库中。
> 3. 优化 multi_simulate 方法，暂时想的是多线程提交以及保存提交记录。
> 4. 消息推送：报错推送、任务完成（simulate、check）推送。
> 5. AI 方面还在研究...

---

### 帖子 #40: 【Super Alpha Competition】As of now, what is your Performance Comparison in the SAC competition?
- **主帖链接**: 【Super Alpha Competition】As of now what is your Performance Comparison in the SAC competition.md
- **讨论数**: 6

I'm from Group G2. So far, I've participated in three types of competitions: Simple Alphas, Risk Neutralized, and Power Pool. Up to now, in my Performance Comparison, the IS score is 67470, the sharpe ratio is 16.61, the fitness is 20.16, and the margin is 31.48. However, I haven't won any weekly awards in the previous three weeks. Perhaps my OS performance isn't good enough. Could you give me some suggestions for improvement? Could you list your performance details below? (It would be best to upload pictures.)


> [!NOTE] [图片 OCR 识别内容]
> Performance Comparison
> Delay-1 Score
> Betore SUOIIISSIOII
> After SUbmissIOn
> Chanee
> L3S RUT: SUn
> 06/2212025,6-0_ Pu
> 67,374
> 65,971
> -1,403
> Aggregate Data
> Sharpe
> TUITnUET
> Fines
> ETIITn S
> Drawoown
> Marain
> 16.61
> -0.47
> 11.70 %
> -0.21
> 20.16,.0.65
> 18.42 %,.3.16
> 0.55 %,-0.03
> 31.48 %oo
> Uu
> IS Performance After Submission (Super Alpha Competition 2025 alphas)
> umhine
> Perrorra
> 431=
> ShOr
> Fr 31
> Super Alpha Compe-i-ion 2025 alphas。 Submittina this
> 3Ipha WIII not efect -hE
> CuThInEr
> DerorIIarcE
> VUUI
> TThEr
> Year
> TINOeT
> Ftness
> Returns
> Drawdown
> Marqin
> 2013
> 15.06
> ~0.12
> 1351 %
> ~0.61
> 1.11
> 0.13
> 17.443
> -0.73
> 0.2495
> 001
> 25.81 %
> 000
> 2011
> 23.00
> ~0.63
> 12.02 %
> ~0.23
> 23.51
> ~1.14
> 20.72 %
> -0.35
> 0.09
> 0.01
> 34.475
> 020
> 2015
> 20.71
> ~0.57
> 11.26 %
> ~0.24
> 27.43
> ~1.32
> 21.93 %
> -0.25
> 0.1495
> 0O0
> 38.93
> 0.36
> 2015
> 20.23
> ~033
> 0.25
> 25.19
> -0.54
> 1933%
> 0.25
> 01
> 0.03
> 34.295
> 0.32
> 2017
> 20.11
> ~0.30
> 1127 %
> 0.25
> 2343
> 021
> 16.97%
> 0.03
> 0.1295
> 0O0
> 30.1250
> 0.50
> 2013
> 1.17
> 04
> 11.52 %
> 0.21
> 20.86
> -0.53
> 17.22%
> -01
> 0.15
> 0O0
> 23.30汩
> 0.35
> 2019
> 15.55
> ~0.75
> 11.59 %
> 0 -
> 1325
> 0.93
> 16.91 %5
> 0.13
> 0.12
> 0O0
> 29.18 %
> 0.23
> 2020
> 13.03
>  4
> 11.86 %
> 0.23
> 15.5
> -0.53
> 17.33%
> 0.01
> 1S
> 0.03
> 30.155
> 0.54
> 2021
> 14.47
> ~0.47
> 1133 %
> ~0.16
> 1322
> 0.55
> 19.82%
> 0.09
> 0.31 95
> 0O0
> 34.995
> 0.65
> 2022
> 12.55
> 0.21
> 11.47 %
> 0.23
> 1429
> -0.10
> 16.20%
> 0.30
> 0.29
> 001
> 23.25 汩
> 1.08
> 2023
> 14.41
> 1.30
> 11.93 %
> ~0.24
> 135
> 1.94
> 11.05~
> 0.46
> 0.06 9
> 001
> 18.5250
> 112
> Pnl
> aIphas
> Sharpe
> 1131



> [!NOTE] [图片 OCR 识别内容]
> PnL
> 1SM
> 17M
> GN
> 1SM
> 14N
> 13N
> 12M
> 1N
> OM
> OOOK
> OOOK
> 70OOK
> OOOK
> OOOK
> OOOK
> OOOK
> OOOK
> OO[
> 02125/2013
> Pnl Before Submission: 255.38<
> Pnl After Submission:
> 242.75
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022


---

### 帖子 #41: 【Super Alpha Competition】As of now, what is your Performance Comparison in the SAC competition?
- **主帖链接**: https://support.worldquantbrain.com【Super Alpha Competition】As of now what is your Performance Comparison in the SAC competition_32972576056343.md
- **讨论数**: 6

I'm from Group G2. So far, I've participated in three types of competitions: Simple Alphas, Risk Neutralized, and Power Pool. Up to now, in my Performance Comparison, the IS score is 67470, the sharpe ratio is 16.61, the fitness is 20.16, and the margin is 31.48. However, I haven't won any weekly awards in the previous three weeks. Perhaps my OS performance isn't good enough. Could you give me some suggestions for improvement? Could you list your performance details below? (It would be best to upload pictures.)


> [!NOTE] [图片 OCR 识别内容]
> Performance Comparison
> Delay-1 Score
> Betore SUOIIISSIOII
> After SUbmissIOn
> Chanee
> L3S RUT: SUn
> 06/2212025,6-0_ Pu
> 67,374
> 65,971
> -1,403
> Aggregate Data
> Sharpe
> TUITnUET
> Fines
> ETIITn S
> Drawoown
> Marain
> 16.61
> -0.47
> 11.70 %
> -0.21
> 20.16,.0.65
> 18.42 %,.3.16
> 0.55 %,-0.03
> 31.48 %oo
> Uu
> IS Performance After Submission (Super Alpha Competition 2025 alphas)
> umhine
> Perrorra
> 431=
> ShOr
> Fr 31
> Super Alpha Compe-i-ion 2025 alphas。 Submittina this
> 3Ipha WIII not efect -hE
> CuThInEr
> DerorIIarcE
> VUUI
> TThEr
> Year
> TINOeT
> Ftness
> Returns
> Drawdown
> Marqin
> 2013
> 15.06
> ~0.12
> 1351 %
> ~0.61
> 1.11
> 0.13
> 17.443
> -0.73
> 0.2495
> 001
> 25.81 %
> 000
> 2011
> 23.00
> ~0.63
> 12.02 %
> ~0.23
> 23.51
> ~1.14
> 20.72 %
> -0.35
> 0.09
> 0.01
> 34.475
> 020
> 2015
> 20.71
> ~0.57
> 11.26 %
> ~0.24
> 27.43
> ~1.32
> 21.93 %
> -0.25
> 0.1495
> 0O0
> 38.93
> 0.36
> 2015
> 20.23
> ~033
> 0.25
> 25.19
> -0.54
> 1933%
> 0.25
> 01
> 0.03
> 34.295
> 0.32
> 2017
> 20.11
> ~0.30
> 1127 %
> 0.25
> 2343
> 021
> 16.97%
> 0.03
> 0.1295
> 0O0
> 30.1250
> 0.50
> 2013
> 1.17
> 04
> 11.52 %
> 0.21
> 20.86
> -0.53
> 17.22%
> -01
> 0.15
> 0O0
> 23.30汩
> 0.35
> 2019
> 15.55
> ~0.75
> 11.59 %
> 0 -
> 1325
> 0.93
> 16.91 %5
> 0.13
> 0.12
> 0O0
> 29.18 %
> 0.23
> 2020
> 13.03
>  4
> 11.86 %
> 0.23
> 15.5
> -0.53
> 17.33%
> 0.01
> 1S
> 0.03
> 30.155
> 0.54
> 2021
> 14.47
> ~0.47
> 1133 %
> ~0.16
> 1322
> 0.55
> 19.82%
> 0.09
> 0.31 95
> 0O0
> 34.995
> 0.65
> 2022
> 12.55
> 0.21
> 11.47 %
> 0.23
> 1429
> -0.10
> 16.20%
> 0.30
> 0.29
> 001
> 23.25 汩
> 1.08
> 2023
> 14.41
> 1.30
> 11.93 %
> ~0.24
> 135
> 1.94
> 11.05~
> 0.46
> 0.06 9
> 001
> 18.5250
> 112
> Pnl
> aIphas
> Sharpe
> 1131



> [!NOTE] [图片 OCR 识别内容]
> PnL
> 1SM
> 17M
> GN
> 1SM
> 14N
> 13N
> 12M
> 1N
> OM
> OOOK
> OOOK
> 70OOK
> OOOK
> OOOK
> OOOK
> OOOK
> OOOK
> OO[
> 02125/2013
> Pnl Before Submission: 255.38<
> Pnl After Submission:
> 242.75
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022


---

### 帖子 #42: 【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？
- **主帖链接**: 【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用.md
- **讨论数**: 30

【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？昨天突发奇想，想加一个每日base排行榜，但不知道会有多少同学支持使用，毕竟人数太少的话，就没有实际意义了，所以如果你支持并且会使用的话，希望留下你的评论。初步构想每日金额由自己手动输入上传。【为增加可信度，允许上传截图（不强制）（提供ID水印，防止被二次盗取使用）】可选匿名（wq_id）。除base外，同时关联vf、osm信息（可选展示）、提交的alpha指标【同样允许上传截图】开放范围：1. 仅对当日上传了base信息的用户展示。2. 仅对指定参与用户开放。存在的作用1. 可以清晰看到其他同学的收益。2. 关联vf、osm、alpha指标后，可以对后续在什么vf + osm下提交何种alpha更易拿到高base有一个大概的认知。3. 收集数据量够多后或许可以拟合出一个base函数来计算预期收益。最后欢迎评论区讨论，base榜存在的合理性，你是否会上传数据并使用它，不同意见的设计方案等等。

---

### 帖子 #43: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用_39466731879063.md
- **讨论数**: 30

### 【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？

昨天突发奇想，想加一个每日base排行榜，但不知道会有多少同学支持使用，毕竟人数太少的话，就没有实际意义了，所以如果你支持并且会使用的话，希望留下你的评论。

### 初步构想

- 每日金额由自己手动输入上传。【为增加可信度，允许上传截图（不强制）（提供ID水印，防止被二次盗取使用）】

- 可选匿名（wq_id）。
- 除base外，同时关联vf、osm信息（可选展示）、提交的alpha指标【同样允许上传截图】
- 开放范围：1. 仅对当日上传了base信息的用户展示。2. 仅对指定参与用户开放。

#### 

### 存在的作用

1. 可以清晰看到其他同学的收益。

2. 关联vf、osm、alpha指标后，可以对后续在什么vf + osm下提交何种alpha更易拿到高base有一个大概的认知。

3. 收集数据量够多后或许可以拟合出一个base函数来计算预期收益。

### 最后

欢迎评论区讨论，base榜存在的合理性，你是否会上传数据并使用它，不同意见的设计方案等等。

---

### 帖子 #44: 【WQ Manager】大更新！新增Base Payment排行榜！
- **主帖链接**: 【WQ Manager】大更新新增Base Payment排行榜.md
- **讨论数**: 11

继【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？需求调研后，Base Payment 排行榜也是正式上线了！访问地址：[链接已屏蔽] 华子哥插件直达使用方式1. 点击右下角加号 ➕，再点击BASEPAY，进入 Base Payment Dashboard 页面2. 初次进入需要设置设置自己的验证口令，每8小时需要重新验证一次（暂时没有提供修改入口，忘记了话请联系作者）目前依旧没有设置账号的概念，仅对base-payment页面及其接口设置权限验证3. 上传自己的数据1. 当且仅当你上传了自己的数据后，才可以查看其他人的数据，不想让别人知道ID的话可以选择匿名。2. 左上角选择不同的时间，可以上传不同时间的数据。3. 上传图片可以增加可信性。温馨提示：为保护其他人的权益，恳请您不要胡乱上传数据，证伪假数据后，将被禁止访问wqmanager！后续1. 未避免账号密码泄露，网站不会提供一键上传操作，后续会有插件佬和好心人开发对应的插件，敬请期待。2. 后续计划同时展示当日提交alpha的具体指标，如sharpe、fitness等等。3. base功能尚处于初步阶段，可能存在bug和功能缺陷，恳请您使用后积极提出疑问和建议。欢迎大家使用共建！祝大家base节节高！

---

### 帖子 #45: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【WQ Manager】大更新新增Base Payment排行榜_39907023480599.md
- **讨论数**: 11

继  [【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？](【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用_39466731879063.md)  需求调研后，Base Payment 排行榜也是正式上线了！

访问地址： [[链接已屏蔽]) OR 华子哥插件直达

### 使用方式

1. 点击右下角加号 ➕，再点击BASEPAY，进入 Base Payment Dashboard 页面
 
> [!NOTE] [图片 OCR 识别内容]
> Base Payment Dashboard
> 更新上传
> Refresh
> 快来看看大佬们今天都赚了多少刀乐吧!
> PROFILE
> RECORD DAT巳
> PERMISS10N GATE
> 2026-04-21
> 已上传2026-04-21,
> 可查看该日数据
> TRENDS
> GENIUS
> Daily Insight Dashboard
> 2026-04-21
> 展开
> NOTICE
> VALUE
> Base Payment Leaderboard
> Total 7
> COMBINED
> No
> Date
> User
> Total Payment
> Regular Payment
> Super Payment
> Regular Count
> Count
> Value Factor
> Daily Osmosis Rank
> CONSULTANT
> 2026-04-21
> D27384
> 11.34
> 2.90
> 8.44
> 0.96
> 0.3.
> OSMOSIS
> 2026-04-21
> DA98440
> 10.03
> 2.36
> 7.67
> 0.93
> 0.1.
> 2026-04-21
> PP26750
> 9.83
> 3.06
> 6.77
> 1.00
> 0.0:
> BASEPAY
> 2026-04-21
> 0X52484
> 9.23
> 4.03
> 5.20
> 0.94
> HOME
> 2026-04-21
> 匿名用户
> 8.81
> 4.24
> 4.57
> 0.8
> 0.31
> 2026-04-21
> LX57490
> 4.33
> 1.81
> 2.52
> 0.75
> 0.1'
> FEEDBACK
> 2026-04-21
> 顾问 顾问 JG15244 (Rank 67) (Rank 67)
> 3.58
> 1.71
> 1.87
> 0.74
> 0.1
> Total 7
> Super
> SOIpage
 
2. 初次进入需要设置设置自己的验证口令，每8小时需要重新验证一次（暂时没有提供修改入口，忘记了话请联系作者）

> 目前依旧没有设置账号的概念，仅对base-payment页面及其接口设置权限验证


> [!NOTE] [图片 OCR 识别内容]
> Base Payment 访问验证
> 诸输入 Base Payment 页面访问口令
> 请输入访问口令
> 取消
> 验证井进入


3. 上传自己的数据

> 1. 当且仅当你上传了自己的数据后，才可以查看其他人的数据，不想让别人知道ID的话可以选择匿名。
> 2. 左上角选择不同的时间，可以上传不同时间的数据。
> 3. 上传图片可以增加可信性。
> 温馨提示：为保护其他人的权益，恳请您不要胡乱上传数据，证伪假数据后，将被禁止访问wqmanager！


> [!NOTE] [图片 OCR 识别内容]
> Base Payment Dal
> 2026-04-21
> 更新上传
> Refresh
> 更新 Base Payment
> 快来看看大佬们今天都赚了多少刀乐吧!
> 为保障信息准确有效。请您奶实填写;
> 此举既惠及他人;
> 也便利自身。
> 温馨提示:  不要乱填哦;乱填会被禁止访问网站喔!
> R巳CORD
> DAT巳
> 隐私设置
> 2026-04-21
> 展示方式
> 不匿名 (展示 WQ_ID)
> 匿名 (仅显示"匿名用户 )
> 收益与数量
> Daily Insight Dashboard
> 2026-04-21
> 展开
> Regular Payment
> Super Payment
> 1.71
> 1.87
> Regular Count
> Super Count
> Base Payment Leaderboard
> Total 7
> Value Factor
> Daily Osmosis Rank
> 0.74
> 0.17
> No
> Date
> UIe
> Factor
> Daily Osmosis Rank
> 图片上传(可选) [抓有截图可信度更高! ]
> 2026-04-21
> D27384
> 0.96
> 0.3.
> 支持最多9张图片。单张不超过 IOMB。
> 2026-04-21
> DA98440
> 0.93
> 0.1.
> 2026-04-21
> PP26750
> 1.00
> 0.0{
> 2026-04-21
> 0X5248
> 0.94
> 0.1
> 取消
> 更新
> 2026-04-21
> 匿名用户
> 0.81
> 0.31
> 2026-04-21
> LX57490
> 4.33
> 1.81
> 2.52
> 0.75
> 0.1
> 2026-04-21
> 顾问 顾问 JG15244 (Rank 67) (Rank 67)
> 3.58
> 1.71
> 1.87
> 0.74
> 0.1
> Total 7
> User
> SOIpage


### 后续

1. 未避免账号密码泄露，网站不会提供一键上传操作，后续会有插件佬和好心人开发对应的插件，敬请期待。

2. 后续计划同时展示当日提交alpha的具体指标，如sharpe、fitness等等。

3. base功能尚处于初步阶段，可能存在bug和功能缺陷，恳请您使用后积极提出疑问和建议。

**欢迎大家使用共建！祝大家base节节高！**

---

### 帖子 #46: 【WQ数据监控 v0.1.0】wqmanager.qzz.io  版本更新！ 快来看看本次 value factor 和 combined 更新情况吧！
- **主帖链接**: 【WQ数据监控 v010】wqmanagerqzzio  版本更新 快来看看本次 value factor 和 combined 更新情况吧.md
- **讨论数**: 4

应PP26750、LX57490需求，新增 vf 和 comb 分析。在线地址：[链接已屏蔽]更新内容：1. 个人中心页面增加 vf 和 comb 变化趋势图。2. 新增 vf 和 comb 变化统计，可从多维度查看更新情况。3. 新增 favicon.ico 图标。value factor 和 combined 页面需从右下角菜单进入快来视奸各位大佬的 vf 和 comb 吧！😆部分截图：value factor 和 combined 页面 wq_id 还有点击事件，不要遗漏了！欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！欢迎 start 和 issue ！

---

### 帖子 #47: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【WQ数据监控 v010】wqmanagerqzzio  版本更新 快来看看本次 value factor 和 combined 更新情况吧_38353367804695.md
- **讨论数**: 4

> 应 [PP26750](/hc/en-us/profiles/28829349427607-PP26750) 、 [LX57490](/hc/en-us/profiles/31184455301399-LX57490) 需求，新增 vf 和 comb 分析。

## 

在线地址： [[链接已屏蔽])

## 更新内容：

1. 个人中心页面增加 vf 和 comb 变化趋势图。

2. 新增 vf 和 comb 变化统计，可从多维度查看更新情况。

3. 新增 favicon.ico 图标。

> value factor 和 combined 页面需从右下角菜单进入
> 快来视奸各位大佬的 vf 和 comb 吧！😆

部分截图：


> [!NOTE] [图片 OCR 识别内容]
> 个人中心
> 登出
> 顾问 顾问 JG15244 (Rank 67) (Rank 67)
> 单日最大变化
> 当前 Weight
> 历史最高
> 今日娈化
> 0.79
> 16.52
> 16.52
> +0.00
> 日期2025-12-24
> Weight 变化趋势
> 共60犬
> 权重因子
> 18.00
> 15.00
> 12.00
> 10.16
> 9.00
> 6.00
> 3.00
> 0.00
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> 0
> Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 0.90
> 1.50
> 0.87
> 1.00
> 0.84
> 0.50
> 0.81
> 0.79
> 0.04
> 202508
> 202509
> 202510
> 202508
> 202509
> 202510
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 历史记录
> 共60条
> VALU E
> REGULA R
> 41PH4
> REGULAR ALPHA 生
> REG ULAR ALPHA
> SUPER ALPHA 提
> SUPER ALPHA 生产相
> S UPER ALPHA 自
> 日期
> WEIGHT
> FACTOR
> 提交数
> 产相关
> 自相关
> 交数
> 关
> 相关
> 2026-02-12
> 16.52
> 0.89
> 484
> 0.6204
> 0.3441
> 233
> 0.5882
> 0.5083
> 2026-02-11
> 16.52
> 482
> 0.6216
> 0.3449
> 232
> 0.5879
> 0.5077
> 2026-02-10
> 16.52
> 480
> 0.6216
> 0.3451
> 231
> 0.5884
> 0.5081
> 2026-02-09
> 16.52
> 479
> 0.6216
> 0.3452
> 230
> 0.5882
> 0.5075
> 2026-02-08
> 15.96
> 478
> 0.6216
> 0.3451
> 229
> 0.5889
> 0.5079
> 2026-02-07
> 15.96
> 477
> 0.6220
> 0.3453
> 228
> 0.5887
> 0.5073
> 2026-02-06
> 15.96
> .92
> 476
> 0.6225
> 0.3456
> 227
> 0.5898
> 0.5083
> 2026-02-05
> 15.35
> 0.92
> 475
> 0.6230
> 0.3458
> 226
> 0.5907
> 0.5098
> 2026-02-04
> 15.29
> 92
> 473
> 6230
> 0.3459
> 225
> 0.5910
> 0.5102
> 2026-02-03
> 15.29
> 0.92
> 471
> 0.6235
> 0.3460
> 224
> 0.5908
> 0.5096
> Total 60
> Goto
> 12-15
> 12-17
> 12-19
> 12-23
> 12-25
> 12-27
> 12-29
> 12-31
> 01-02
> 01-04
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-20
> 01-22
> 01-24
> 01-26
> 01-28
> 01-30
> 02-01
> 詈
> 02-05
> 02-07
> 02-09
> 02-11
> 12-21



> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化分析
> 刷新数据
> 固定对比 ` leaderboard_consultant_user ` 在2026-02-10与2026-02-11的数据
> 排除基准日和目标日 value_factor 都为 0.5 的数据
> 基准日:
> 2026-02-10
> 目标日:  2026-02-11
> 可对比用户
> 上升 /下降 /持平
> 最大上升
> 4,462
> 2276/2095/91
> 0.8400
> 日标日8,287
> 基准日8,274
> 新增13,
> 缺失0
> 最大下降 -0.8400
> 变化分布 (change= 目标日
> 基准日)
> 用户数
> 1,200
> 1,000
> 800
> 600
> 400
> 200
> 用户娈化明细
> 共4462人
> 娈化值降序
> 国家1地区
> Genius 等级
> 应用
> 清空
> 排名
> 用户
> 等级
> 囝家/地区
> 大学
> 基准日
> VALUE FACTOR
> 目侨日
> VALUE FACTOR
> 变化值
> 型65050
> GOLD
> CN
> Xi'an Jiaotong University
> 0.0600
> 0.9000
> +0.8400
> GN67910
> GOLD
> KE
> 0.1200
> 0.8900
> +0.7700
> 堕64030
> GOLD
> IN
> CTAE; Udaipur
> 0.0800
> 0.8300
> +0.7500
> LC97552
> GOLD
> CN
> 0.0100
> 0.7500
> +0.7400
> South China Agricultural
> 22568
> GOLD
> CN
> 0800
> 0.8200
> +0.7400
> University
> Y26332
> GOLD
> 0800
> 0.8100
> +0.7300
> LW29329
> GOLD
> .0700
> .8000
> +0
> 7300
> 222384
> GOLD
> CN
> Zhengzhou University
> 0.2300
> 0.9500
> +0.7200
> Dedan Kimathi University Of
> E11875
> EXPERI
> KE
> 0.2400
> 0.9500
> +0.7100
> Technology
> 10
> 4742510
> GOLD
> IN
> 0.0400
> 0.7400
> +0.7000
> 11
> CL8GO6Z
> GOLD
> CN
> Zhengzhou University
> 0.1900
> 0.8900
> +0.7000
> Hanoi University Of Science and
> 12
> H079370
> GOLD
> VN
> 0.2100
> 0.8900
> +0.6800
> Technology
> 13
> 冗57189
> EXPERT
> CN
> Harbin Institute Of Technology
> 0.2500
> 0.9300
> +0.6800
> 14
> 425939
> GOLD
> KE
> CHUKA university
> 0.1800
> 0.8600
> +0.6800
> 15
> 0L34206
> GOLD
> KE
> 0800
> 0.7500
> +0.6700
> 16
> 2225272
> GOLD
> CN
> 0.0800
> 0.7500
> +0.6700
> 17
> 亚87508
> GOLD
> KE
> MIOI
> University
> 0.3100
> 0.9800
> +0.6700
> 18
> WT5O902
> GOLD
> TH
> University Of Southern California
> 0.0200
> 0.6900
> +0.6700
> 19
> LY52585
> GOLD
> CN
> 0.0800
> 0.7400
> +0.6600
> 20
> T46032
> GOLD
> VN
> Foreign Trade University; Hanoi
> 0.0600
> 0.7100
> +0.6500
> Total 4462
> 224
> ~0.6720
> ~0.5040
> ~0.3360
> ~0.1680
> ~0.0000
> ~0.1680
> ~0.3360
> ~0.5040
> 0.5040~0.6720
> ~0.8400
> ~0.1680~C
> 0.0000~C
> 0.3360~C
> 0.6720~C
> 1.8400~
> ~0.6720~
> -0.5040~一
> 1.3360~一
> 0.1680~



> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化分析
> 刷新数据
> 固定对比 ` leaderboard_genius_user ` 在 2026-02-10与2026-02-11的数据
> 开
> 排除基淮日和目标日 Combined Alpha 都为0
> 排除基准日和目标日 Power Pool 都为0
> 排除基准日和目标日 Selected Alpha 都为0
> 基准日:  2026-02-10
> 目标日:
> 2026-02-11
> 可对比用户
> 新增
> 缺失
> 2,684
> 22/6
> 日标日10,639/基准日10,623
> 仅统计固定日期下三项 combined 完整的用户
> Combined Alpha
> Power Pool
> Selected Alpha
> 目标均值
> 0.3848
> 目标均值
> 0.0001
> 目标均值
> 0.0583
> 基准均值
> 0.4500
> 基准均值
> 0.0305
> 基准均值
> 0.2311
> 平均娈化
> -0.0652
> 平均娈化
> -0.0304
> 平均娈化
> -0.1728
> 上升7下降/持平
> 989/1660/35
> 上升7下降/持平
> 1154/1494/36
> 上升7下降/持平
> 675/1957/52
> 变化分布
> Combined Alpha
> 用户数
> 2,100
> 1,800
> 1,500
> 1,200
> 900
> 600
> 300
> 用户娈化明细
> 共2684人
> 国家1地区
> Genius 等级
> 应用
> 清空
> ALPHA 基准日
> ALPHA 目标日
> ALPHA 变化值
> POWERPOOL 基准
> P0 WERP00L
> 目标
> POWERPOOL 变化
> S巳LE C
> 排名
> 用户
> 级
> 囝家/地区
> 日
> 值
> 78552
> GOLD
> KE
> -1.2500
> 1.1400
> +2.3900
> 2.3100
> 0.0500
> +2.2600
> 工C97552
> GOLD
> CN
> 0.3300
> 1.5800
> +1.9100
> -1.9400
> 0.0800
> +1.8600
> 4S39500
> GOLD
> TTN
> 0.3800
> 2.2200
> +1.8400
> 0.4900
> 1.4000
> +0.9100
> 27568
> GOLD
> CN
> -1.2900
> 0.4300
> +1.7200
> -1.0800
> 0.5700
> +1.6500
> J10294
> GOLD
> CN
> 0.6300
> 1.0500
> +1.6800
> 0.6300
> 1.0600
> +1.6900
> YC28355
> EXPERT
> TTN
> 0.5200
> 2.0900
> +1.5700
> 0.5700
> 1.4100
> +0.8400
> 斑44463
> GOLD
> TTN
> 0.2100
> 1.7400
> +1.5300
> -0.1300
> 1.1500
> +1.2800
> L082224
> GOLD
> KE
> 0.9000
> 0.5600
> +1.4600
> 0.6500
> 0.4300
> 0.2200
> LN33832
> GOLD
> KE
> 0.1600
> 1.2000
> +1.3600
> 0.7400
> 0.8100
> +0.0700
> 10
> 亟23328
> GOLD
> KE
> -0.7000
> 0.6500
> +1.3500
> -2.0300
> 0.4500
> +2.4800
> 11
> NLG5170
> GOLD
> VN
> -1.2800
> 0.0400
> +1.3200
> 0.3600
> 0.1400
> 0.2200
> 12
> WL8OOOe
> GOLD
> TT
> -1.2800
> 0.0100
> +1.2900
> 0.0900
> 0.3000
> +0.3900
> 13
> R13444
> GOLD
> KE
> 0.6900
> 0.5200
> +1.2100
> 0.7200
> 0.5500
> +0.1700
> 14
> }30528
> GOLD
> KE
> 0.8600
> 0.3100
> +1.1700
> -1.6100
> 0.0200
> +1.5900
> 15
> MY82844
> EXPERT
> CN
> 0.8400
> 1.9300
> +1.0900
> 0.7600
> 1.7100
> +0.9500
> 16
> 855718
> GOLD
> KE
> 2.6100
> 1.5200
> +1.0900
> 2.4900
> 1.4700
> +1.0200
> 17
> 卫C43564
> GOLD
> KE
> 0.4000
> 0.6700
> +1.0700
> -1.0000
> 1.1100
> +2.1100
> 18
> R619358
> GOLD
> KE
> 2.1900
> 1.1200
> +1.0700
> 2.2000
> 1.6000
> +0.6000
> 19
> J14356
> GOLD
> KE
> -2.1500
> 1.1000
> +1.0500
> -2.2600
> -1.5200
> +0
> .7400
> 20
> XY20037
> GOLD
> CN
> 0.0800
> 0.9400
> +1.0200
> 0.0300
> 0.5300
> +0.5600
> Total 2684
> 135
> -2.4160
> -1.8820
> ~1.3480
> -0.8140
> -0.2800
> ~0.2540
> ~0.7880
> ~1.3220
> 1.8560
> ~2.3900
> 0.7880~
> 1.3220~
> -2.9500~
> .8820~
> 0.2800~
> 0.2540~
> 1.8560
> -2.4160~
> -1.3480~
> ~0.8140~



> [!NOTE] [图片 OCR 识别内容]
> D27384趋势详情
> 用户娈化明细
> 共4462人
> 变化值降序
> 国家1地区
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> PoWET PoOI
> Selected Alpha
> 排名
> 用户
> Combined
> 娈化值
> 1.00
> 0.19
> H65050
> +0.84
> 0.00
> 0.80
> GN67910
> -0.30
> +0.7T
> 0.60
> K64030
> -0.60
> +0.75
> 0.40
> -0.90
> 工C97552
> +0.74
> 区间:202509
> 202510
> 202511
> 0.20
> 0.14
> 更新时间:2026-01-07
> T27568
> 202508
> 202509
> 202510
> 202509
> 202510
> +0.74
> Combined Alpha: -1.13
> 202509
> 202510
> 202511
> 202510
> 202511
> 202510
> 202511
> 202512
> Power Pool: -1.23
> 202511
> 202512
> XL26332
> Selected Alpha: 0.00
> +0.73
> LWI29329
> +0.73
> LD22384
> GOLD
> CN
> Zhengzhou University
> 0.23
> 0.95
> +0.72
> Dedan Kimathi University Of 
> 11875
> EXPERT
> KE
> 0.24
> 0.95
> +0.71
> Technology
> 10
> 4T42510
> GOLD
> IN
> 0.04
> 0.74
> +0.70
> 11
> CL8G067
> GOLD
> CN
> 'Zhengzhou University
> 0.19
> 0.89
> +0.70
> Hanoi University Of Science and
> 12
> 79370
> GOLD
> VN 
> 0.21
> 0.89
> +0.68
> Technology
> 13
> 卫57189
> EXPERT
> CN
> Harbin Institute Of Technology^
> 0.25
> 0.93
> +0.68
> 14
> 425939
> GOLD
> KE 
> CHUKA university
> 0.18
> 0.86
> +0.68
> 15
> 0L34206
> GOLD
> KE 
> 0.08
> 0.75
> +0.6T


> **value factor 和 combined 页面 wq_id 还有点击事件，不要遗漏了！**

欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！

欢迎 start 和 issue ！

---

### 帖子 #48: 【WQ数据监控 v0.2.0】wqmanager.qzz.io 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比。代码优化
- **主帖链接**: 【WQ数据监控 v020】wqmanagerqzzio 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比代码优化.md
- **讨论数**: 12

在线地址：[链接已屏蔽]更新内容个人信息页面增加 Osmosis Rank 变化趋势图、周维度对比图。新增 consulant 页面，整合 consulant 全部信息。更新截图欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！欢迎 start 和 issue ！后端项目地址：[链接已屏蔽]前端项目地址：[链接已屏蔽]

---

### 帖子 #49: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【WQ数据监控 v020】wqmanagerqzzio 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比代码优化_38582852015895.md
- **讨论数**: 12

在线地址： [[链接已屏蔽])

## 更新内容

1. 个人信息页面增加 Osmosis Rank 变化趋势图、周维度对比图。
2. 新增 consulant 页面，整合 consulant 全部信息。

## 更新截图


> [!NOTE] [图片 OCR 识别内容]
> Consultant Detail Dashboard
> REFRESH
> Merged view of ` Ieaderboard_consultant_user
> and
> leaderboard_genius_user
> RECORD
> DAT巳
> COUNTRY/REGION
> GENIUS LEVEL
> USER SEARCH
> 2026-02-23
> Select countrylregion
> Select level
> Enter WQ_ID keyword
> APPLY
> Reset
> FILTERED USERS
> CONSULTANT COVCRAGE
> GENIUS COVERAG卫
> MATCHED USERS
> COUNTRIPS
> GENIUS LEVELS
> 10,762
> 8,419
> 10,759
> 8,416
> 16
> 4
> Date 2026-02-23
> Fromn
> Fromn Ieaderboard
> UISET
> Users found i both tables On
> Distinct Countries in Curtent
> Distinct levels in current result
> leaderboard_consultant_
> UISeT
> selected date
> Tesult
> AllMetrics
> Total 10762
> No_
> User
> Country
> University
> Level
> Best Level
> Weight
> Value
> Osmosis
> Data Fields
> RA
> RA Prod
> RA SI
> Rank
> Subm
> Corr
> 6247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63372
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec.。
> GOLD
> GOLD
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> R19116
> IN
> Dr.APJ.Abdul Kalar。。
> GOLD
> GOLD
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> XL82940
> CN
> GOLD
> EXPERI
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> KE
> Jomo Kenyatta Univer。
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE
> GOLD
> GOLD
> 2.31
> 0.47
> 0.90
> 269
> 326
> 0.6803
> P24362
> CN
> TNuhan
> University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 0242372
> CN
> Harbin Engineering U。
> GOLD
> GOLD
> 0.00
> 0.93
> 0.89
> 145
> 167
> 0.6402
> 10
> 巫24675
> IN
> Deen Dayal Upadhyay.-
> GOLD
> EXPERI
> 26.63
> 0.30
> 0.88
> 1,990
> 1,755
> 0.6537
> 11
> T42173
> CN
> Arizona State Universi。
> EXPERI
> EXPERI
> 26.11
> 0.44
> 0.88
> 460
> 648
> 0.6685
> 12
> CL93587
> CN
> HangZhou Dianziuni。
> EXPERI
> EXPERI
> 14.88
> 0.28
> 0.87
> 390
> 295
> 0.6609
> 13
> J75700
> Harbin Institute Of Te。
> EXPERI
> EXPERI
> 0.00
> 0.90
> 0.87
> 124
> 106
> 0.6568
> 14
> PY32594
> CN
> Huazhong University
> EXPERI
> EXPERI
> 0.00
> 0.42
> 0.87
> 441
> 480
> 0.6867
> 15
> 2262721
> CN
> MASTER
> MASTER
> 7.37
> 0.95
> 0.87
> 405
> 316
> 0.7365
> 16
> SL10033
> University Of Internati。
> EXPERI
> MASTER
> 39.26
> 0.68
> 0.87
> 625
> 447
> 0.5676
> 17
> T12226
> CN
> GOLD
> GOLD
> 0.00
> 0.55
> 0.87
> 182
> 207
> 0.6052
> 18
> 4T26308
> IN
> Indian Institute Of Tec..
> GOLD
> MASTER
> 13.57
> 0.03
> 0.86
> 408
> 471
> 0.7073
> 19
> J025713
> KE
> CHUKA university
> EXPERI
> MASTER
> 4.72
> 0.32
> 0.86
> 1,404
> 1,498
> 0.6529
> 20
> 1053462
> CN
> NanJing Audit Univer。。。
> GOLD
> EXPERT
> 1.14
> 0.38
> 0.86
> 166
> 126
> 0.6513
> Total 10762
> 20/page
> 539
> genius



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Weekly
> R巳CORD DAT巳
> Rank
> 1.00
> 2026-02-23
> Reset
> 0.80
> 0.60
> FILTERED USERS
> GPNIUS LDVPLS
> 10,762
> 0.40
> Date 2026-02-23
> 0.33
> Distinct levels in current result
> 0.20
> 0.00
> All Metrics
> Total 10762
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 2026-02-16'
> 2026-02-17
> 2026-02-18'
> 2026-02-19'
> 2026-02-20'
> 2026-02-21'
> 2026-02-22'
> 2026-02-23'



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Daily
> R巳CORD DAT巳
> 2026-02-16
> 2026-02-22
> 3 2026-02-23
> 2026-03-01
> 2026-02-23
> Rank
> Reset
> 1.00
> 0.96
> 0.80
> FILTERED USERS
> GPNIUS LDVPLS
> 0.60
> 10,762
> Date 2026-02-23
> Distinct levels in current result
> 0.40
> 0.24
> 0.20
> All Metrics
> 0.00
> Total 10762
> 苘凶
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521



> [!NOTE] [图片 OCR 识别内容]
> 个人中心
> 退出登录
> 顾问 顾问 JG15244 (Rank 67) (Rank 67)
> 单日最大娈化
> 当前 Weight
> 历史最高
> 今日娈化
> 0.79
> 17.60
> 17.60
> +0.00
> 日期2025-12-24
> Weight 变化趋势
> 共71犬
> 权重因子
> 19.56
> 15.00
> 11.23
> 10.00
> 5.00
> 00
> ^?
> ^9
> 8
> 8
> 2
> ^2
> 02
> 02
> 02
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> 16
> 19
> 20
> 23
> 02
> 02
> 02
> 02
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> Power
> Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 0.90
> 1.50
> 0.87
> 1.00
> 0.84
> 0.50
> 0.81
> 0.79
> 0.04
> 202508
> 202509
> 202510
> 202508
> 202509
> 202510
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 历史记录
> 共71条
> VALUE
> DA11
> 05M0515
> REGULAR
> REGULAR ALPHA
> REGULAR
> SUPER ALPH4
> SUPER ALPHA
> SUPER ALPH
> 日期
> WEIGHT
> FA CT0R
> RANk
> ALPHA 提交数
> 生产相关
> 41PH4
> 自相关
> 提交数
> 产相关
> 自相
> 2026-02-23
> 17.60
> 0.89
> 0.64
> 503
> 0.6133
> 0.3392
> 244
> 0.5860
> 0.50
> 2026-02-22
> 17.60
> 0.89
> 0.73
> 502
> 0.6131
> 0.3392
> 243
> 0.5865
> 0.50
> 2026-02-21
> 17.60
> 89
> 38
> 501
> 0.6128
> 3393
> 242
> 0.5861
> 0.50
> 2026-02-20
> 17.35
> 500
> 0.6135
> 3397
> 241
> 0.5869
> 0.50
> 2026-02-19
> 17.08
> 38
> 0.6149
> 3404
> 240
> 0.5865
> 0.50
> 2026-02-18
> 16.82
> 0.31
> 492
> 0.6174
> 3419
> 239
> 0.5875
> 0.50
> 2026-02-17
> 16.82
> 89
> 0.31
> 487
> 6204
> 3436
> 238
> 0.5873
> 0.50
> 2026-02-16
> 16.82
> 89
> 0.31
> 486
> ).6205
> 3438
> 237
> 0.5880
> 0.50
> 2026-02-15
> 16.82
> 89
> 486
> 0.6205
> 3438
> 236
> 0.5876
> 50
> 2026-02-14
> 16.64
> 89
> 485
> 1.6202
> 3439
> 234
> 0.5878
> 50
> Total 71
> Goto
> 01-06
> 01-16
> 01-18
> 01-20
> 12-17
> ~
> 12-23
> 12-25
> 12-27
> 12-29
> 12-31
> 01-02
> 01-04
> 01-08
> 01-10
> 01-12
> 01-14
> 01-22
> 01-24
> 01-26
> 01-28
> 01-30
> 02-01
> 02-03
> 02-07
> 02-11
> 02-13
> 02-21
> 合
> ~02-17
> ~02-18
> ~02-21
> ~02-22
> 2026
> 2026
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> Pool



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到曰维度
> 2026-02-16
> 2026-02-22
> 0
> 2026-02-23
> 2026-03-01
> Rank
> 1.00
> 80
> 0.64
> 60
> 0.40
> 0.20
> 0.00
> 周二
> 周三
> 周五
> 周六
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21
> ~02-16'
> ~02-17
> ~02-18
> ~02-19
> ~02-20
> ~02-22
> 2026-02-23'
> ~02-21
> 2026-
> 2026-
> 2026-
> 2026-C
> 2026-C
> 2026-C
> 2026-0


> 欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！
> 欢迎 start 和 issue ！
> 后端项目地址： [[链接已屏蔽])
> 前端项目地址： [[链接已屏蔽])

---

### 帖子 #50: 【WQ数据监控】wqmanager.qzz.io 一览wq-leaderboard数据
- **主帖链接**: 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据.md
- **讨论数**: 24

项目介绍定时拉取平台的数据并存储，进行可视化展示。目前主要进行weight变化、alpha提交情况进行展示，后续会逐步增加更多指标、维度的数据展示（欢迎提出你的需求）。目前项目仅需通过WQ_ID即可进行登录，目前个性化展示的内容较少，暂未增加账号系统。先已将所有国区ID加入登录名单项目地址在线地址：[链接已屏蔽]后端项目地址：[链接已屏蔽]前端项目地址：[链接已屏蔽]欢迎 start 和 issue部分内容截图欢迎大家体验，提出需求、bug、优化。

---

### 帖子 #51: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据_38121748548759.md
- **讨论数**: 24

### 项目介绍

定时拉取平台的数据并存储，进行可视化展示。

目前主要进行weight变化、alpha提交情况进行展示，后续会逐步增加更多指标、维度的数据展示（欢迎提出你的需求）。

目前项目仅需通过WQ_ID即可进行登录，目前个性化展示的内容较少，暂未增加账号系统。

> 先已将所有国区ID加入登录名单

### 项目地址

在线地址： [[链接已屏蔽])

后端项目地址： [[链接已屏蔽])

前端项目地址： [[链接已屏蔽])

> 欢迎 start 和 issue

### 部分内容截图


> [!NOTE] [图片 OCR 识别内容]
> 你好。J615244
> 7天
> 15天
> 30天
> 登出
> 数据概览
> 总用户数
> 总ALPHA 数
> 总 INEIG HT
> 数据总量
> 8,169
> 3,264,520
> 128,002.04
> 933,274
> +86变化量
> +37870娈化量
> -1595.64变化量
> 最新数据 2026-02-02 (平台间)
> 选择国家/地区点击标签切换  (至少选择一
> ALL 全部总和
> VN 越南
> IN
> 印度
> CN 中国大陆
> TW
> 中国台湾
> KE 肯尼亚
> GB  英国
> KR 韩国
> ID 印度尼西亚
> SG 新加坡
> HK 中国香港
> MY 马来西亚
> US 美国
> TH 泰国
> AM 亚美尼亚
> HU
> 匈牙利
> NG 尼日利亚
> 国家/地区 Weight 娈化趋势
> 凶 乜03
> 十国大陆
> Weight Factor
> 7538.34
> 7000
> 6000
> 5000
> 4000
> 国家/地区Weight
> 用户Weight
> Genius等级Weight变化
> 越南
> 82688.07
> 眈
> {33369
> 1214.89
> 4007.60
> GRANDMASTER
> VN
> 3062.85(3.6%)
> CN
> 1214.89(100.096)
> 222.67(5.996)
> s
> 人数75
> 7天内娈化
> 印度
> 28303.63
> HN
> HN46545
> 193.97
> IN
> 854.63(2.996)
> TN
> 26.43(15.89)
> 13676.43
> MASTER
> 186.83(-1.496)
> MASTER
> 人数249
> 7天内变化
> 中国大陆
> 7117.74
> DD
> DD65284
> 340.15
> CN
> 1719.36 (31.896)
> TN
> 26.38 (8.496)
> EXPERT
> 18913.41
> 501.96 (-2.696)
> EPERT
> 人数675
> 中国台湾
> 4205.63
> CC
> 顾问 CC40930 (Rank 95)
> 177.58
> 7天内变化
> TTN
> 211.79(5.3961
> TTN
> 19.52(12.三
> GOLD
> 91404.62
> 肯尼亚
> 3081.81
> MC
> MC44186
> 149.35
> 1096.39(1.296)
> K卫
> 341.03(12.496)
> TTV
> 17.03(12.99)
> GSLC
> 人数7167
> 7天内变化
> 英国
> 1085.36
> CT
> 顾问 CT68712 (Rank 27)
> 93.72
> GB
> 6.12 (-0.696)
> TTN
> 16.62(21.6%)
> 01-06
> 01-07
> 01-10
> 01-14
> 01-16'
> 01-17
> 01-04
> 01-05 
> 01-08
> 01-09
> 01-11
> 01-12〉
> 01-13
> 01-15>
> 01-18
> 01-19
> 01-20〉
> 01-21
> 01-22'
> 01-23〉
> 01-24
> 01-25〉
> 01-26'
> 01-27〉
> 01-28
> 01-29〉
> 01-30
> 01-31
> 02-01>
> 02-02
> 3961
  
> [!NOTE] [图片 OCR 识别内容]
> Genius 分析仪表盘
> 刷新数据
> 按 Genius 等级与国家追踪 weight 变化与位置
> 时间范围
> GENIUS 等级
> 国家/地区
> 2026-01-01
> 至
> 2026-03-31
> GRANDMASTER
> CN
> 应用筛选
> 覆盖用户数
> 平均变化
> 中位数变化
> 极值变化区间
> 47
> +7.57
> +5.82
> 0.00
> N
> 31.74
> 总量趋势
> 娈化量分布
> Genius Weight 总和变化
> 凶 乜03
> 娈化量分布
> GRANDMASTER-CN
> Weight 总和
> 20
> 1357.97
> 1300.00
> 15
> 1200.00
> 10
> 1100.00
> 1000.00
> 916.65
> ~2
> @
> 0
> 41
> 个人娈化明细
> 共47人
> 娈化量降序
> 排名
> 用户
> 等级
> 国家
> 起始 WEIGHT
> 当前
> WEIGHT
> 变化量
> 位蹩
> HZ69256
> GRANDMASTER
> CN
> 70.64
> 102.38
> +31.74
> 100.009
> Q068782
> GRANDMASTER
> CN
> 52.72
> 78.47
> +25.75
> 97.839
> ZL35633
> GRANDMASTER
> CN
> 31.81
> 50.55
> +18.74
> 95.659
> WX16829
> GRANDMASTER
> CN
> 106.25
> 124.35
> +18.10
> 93.489
> 顾问 JY88060 (Rank 85)
> GRANDMASTER
> CN
> 33.77
> 51.37
> +17.60
> 1.309
> 0231817
> GRANDMASTER
> CN
> 39.25
> 56.06
> +16.81
> 89.139
> J16510
> GRANDMASTER
> CN
> 39.93
> 56.71
> +16.78
> 696
> 8A51127
> GRANDMASTER
> Cl
> 42.51
> 59.12
> +16.61
> 84.789
> 10
> Aoopzro
> GRNOMAsTER
> CN
> 3215
> 4085
> 41330
> '
> 8259
> 11
> XM75236
> GRANDMASTER
> CN
> 36.44
> 49.36
> +12.92
> 78.269
> 12
> XX42289
> GRANDMASTER
> CN
> 28.65
> 41.37
> +12.72
> 76.099
> 13
> 1479055
> GRANDMASTER
> CN
> 27.01
> 39.35
> +12.34
> 73.919
> 14
> 5283096
> GRANDMASTER
> CN
> 23.16
> 33.61
> +10.45
> 71.749
> 15
> K279256
> GRANDMASTER
> CN
> 120.75
> 130.97
> 10.22
> 69.579
> 16
> 顾问 YH25030 (Rank 31)
> GRANDMASTER
> CN
> 15.81
> 24.52
> 8.71
> 67.399
> 17
> 4871859
> GRANDMASTER
> CN
> 12.21
> 20.67
> 8.46
> 65.229
> 18
> M688592
> GRANDMASTER
> CN
> 26.14
> 33.86
> +7.72
> 63.049
> 19
> INX84677
> GRANDMASTER
> CN
> 17.75
> 25.39
> +7.64
> 60.879
> 20
> NV19619
> GRANDMASTER
> CN
> 20.94
> 28.14
> +7.20
> 58.709
> Total 47
> 0.00~3.97
> 3.97~7.93
> 7.93~11.90
> .90~15.87
> 15.87~19.84
> 19.84~23.80
> 23.80~27.77
> 27.77~31.74
> 01-14〉
> 01-09
> 01-10〉
> 言
> 01-13
> 01-15
> 01-16〉
> 01-17
> 01-18
  
> [!NOTE] [图片 OCR 识别内容]
> 趋势分析
> 查看各国家/地区的 Alpha 提交数量变化趋势 (每天疑似会有alpha消失。暂不确定是因为账号封禁还是alpha退役导致)
> 选择季度:
> 2026-01
> 显示项:
> RA提交
> SA提交
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> IN 印度
> KE 肯尼亚
> CN 中国大陆
> TW 中国台湾
> KR 韩国
> GB 英国
> SG 新加坡
> MY 马来西亚
> NG
> 尼日利亚
> US 美国
> HK 中国香港
> ID  印度尼西亚
> TH
> 泰国
> HU 匈牙利
> AM 亚美尼亚
> Consultant-Alpha 提交数量变化趋势 (2026-01)
> 凶乜93
> CN 中国大陆 R4变化
> CN $国大陆 $4变化
> 娈化二
> 1950
> 1800
> 1500
> 1200
> 900
> 600
> 300
> 选择季度:
> 2026-01
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> CN 中国大陆
> KE 肯尼亚
> IN
> 印度
> TW 中国台湾
> NG 尼日利亚
> KR 韩国
> GB 英国
> MY 马来西亚
> SG 新加坡
> US 美国
> TH
> HK 中国香港
> HU 匈牙利
>  ID 印度尼西亚
> AM 亚美尼亚
> Genius-Alpha提交数量变化趋势 (2026-01)
> 凶乜03
> CN 十国大陆 Alpha数量变化
> Alpha变化量
> 2500
> 2000
> 1500
> 1000
> 500
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-07
> 01-08
> 01-09
> 01-10
> 01-12'
> 01-13 '
> 01-14>
> 01-15
> 01-16
> 01-17
> 01-18
> 01-19
> 01-20
> 01-24>
> 01-25 
> 01-26 
> 01-28
> 01-29〉
> 01-30
> 01-06
> 01-17
> 01-21 
> 01-22
> 01-23
> 01-27
> 01-31
> 02-01
> 02-02
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-06
> 01-07>
> 01-08
> 01-09'
> 01-10
> 01-11
> 01-12〉
> 01-13〉
> 01-14
> 01-15
> 01-16 '
> 01-17
> 01-18
> 01-19'
> 01-20
> 01-21>
> 01-22〉
> 01-23
> 01-24〉
> 01-25〉
> 01-26
> 01-27〉
> 01-28
> 01-29'
> 01-30
> 01-37
> 02-01
> 02-02〉


> 欢迎大家体验，提出需求、bug、优化。

---

### 帖子 #52: 【因子挖掘方式】一二三阶 OR 自创模板 ？
- **主帖链接**: 【因子挖掘方式】一二三阶 OR 自创模板.md
- **讨论数**: 1

从接触wq到现在也8个多月了，一直有一个疑惑，现在大家是一直沿用一二三阶模板进行因子的挖掘，还是自己写模板，进行挖掘呢？又或者将一二三阶抽象为框架，将自己写的初步模板当做零阶进入一二三阶框架进行整合呢？哪种出货率更高呢？只使用一二三阶感觉总归会有上限，而自己写模板，是不是又会导致一批因子的相关性会很高呢？感觉自己写模板+一二三阶会是一个比较好的方向。不知道大家有没有将AI给出的因子模板进行挖掘呢，开始的时候有过这种想法，但是一直没有去实践，有没有大佬给点意见呢？

---

### 帖子 #53: 【因子挖掘方式】一二三阶 OR 自创模板 ？
- **主帖链接**: https://support.worldquantbrain.com【因子挖掘方式】一二三阶 OR 自创模板_33036057429911.md
- **讨论数**: 1

从接触wq到现在也8个多月了，一直有一个疑惑，现在大家是一直沿用一二三阶模板进行因子的挖掘，还是自己写模板，进行挖掘呢？又或者将一二三阶抽象为框架，将自己写的初步模板当做零阶进入一二三阶框架进行整合呢？哪种出货率更高呢？

只使用一二三阶感觉总归会有上限，而自己写模板，是不是又会导致一批因子的相关性会很高呢？感觉自己写模板+一二三阶会是一个比较好的方向。

不知道大家有没有将AI给出的因子模板进行挖掘呢，开始的时候有过这种想法，但是一直没有去实践，有没有大佬给点意见呢？

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《alpha 模拟高效篇》的评论回复
- **帖子链接**: [Commented] alpha 模拟高效篇.md
- **评论时间**: 1 year ago

佬现在是不是还是iqc顾问呀，只有三个槽。如果是有条件顾问的话，8*10个槽，回测量一版要在2.5w/天，才算可以的。可以看看论坛里的关于wqb的分享，是一个大佬开源的python包。

最后祝佬，vf1.0！

==========================================

原来，让内心强大，我只需要看到自己，接纳我还不能做的，欣赏我已经做到的。 ---维吉尼亚·萨提亚-

==========================================

---

### 探讨 #2: 关于《alpha 模拟高效篇》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] alpha 模拟高效篇_33036460396567.md
- **评论时间**: 1年前

佬现在是不是还是iqc顾问呀，只有三个槽。如果是有条件顾问的话，8*10个槽，回测量一版要在2.5w/天，才算可以的。可以看看论坛里的关于wqb的分享，是一个大佬开源的python包。

最后祝佬，vf1.0！

==========================================

原来，让内心强大，我只需要看到自己，接纳我还不能做的，欣赏我已经做到的。 ---维吉尼亚·萨提亚-

==========================================

---

### 探讨 #3: 关于《Are some of the Alphas submitted as powerpool alphas noise?》的评论回复
- **帖子链接**: [Commented] Are some of the Alphas submitted as powerpool alphas noise.md
- **评论时间**: 1年前

Don't submit these alphas. Even though they perform excellently in terms of return, fitness, or margin, if the PNL (Profit and Loss) curve is not normal, you should not submit them. It will seriously damage your value factory.

---

### 探讨 #4: 关于《Are some of the Alphas submitted as powerpool alphas noise?》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Are some of the Alphas submitted as powerpool alphas noise_32098070589335.md
- **评论时间**: 1年前

Don't submit these alphas. Even though they perform excellently in terms of return, fitness, or margin, if the PNL (Profit and Loss) curve is not normal, you should not submit them. It will seriously damage your value factory.

---

### 探讨 #5: 关于《First Alpha in EUR region》的评论回复
- **帖子链接**: [Commented] First Alpha in EUR region.md
- **评论时间**: 1年前

Congratulations, I also tried some on EUR-TOP2500, but many alphas got the "Sub-universe Sharpe of 0.5 is below cutoff of 0.74." error, I don't know how to optimize it, can you help me?

---

### 探讨 #6: 关于《First Alpha in EUR region》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] First Alpha in EUR region_30098892113559.md
- **评论时间**: 1年前

Congratulations, I also tried some on EUR-TOP2500, but many alphas got the "Sub-universe Sharpe of 0.5 is below cutoff of 0.74." error, I don't know how to optimize it, can you help me?

---

### 探讨 #7: 关于《目录结构》的评论回复
- **帖子链接**: [Commented] Gemini CLI 结合 MCP 工具的探索经验分享.md
- **评论时间**: 10 months ago

设置环境变量的命令

$env:GOOGLE_CLOUD_PROJECT="你的项目ID"

============================================

不论斟满的是什么，都要——干杯！ ---吉皮乌斯诗-

============================================

---

### 探讨 #8: 关于《目录结构》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md
- **评论时间**: 10个月前

设置环境变量的命令

$env:GOOGLE_CLOUD_PROJECT="你的项目ID"

============================================

不论斟满的是什么，都要——干杯！ ---吉皮乌斯诗-

============================================

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享.md
- **评论时间**: 5个月前

TT大佬，学习了！

---

### 探讨 #10: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享_37661413598231.md
- **评论时间**: 5个月前

TT大佬，学习了！

---

### 探讨 #11: 关于《General Discussion-说任何你想说的话置顶的》的评论回复
- **帖子链接**: [Commented] General Discussion-说任何你想说的话置顶的.md
- **评论时间**: 1年前

太好了有这么一个单独的论坛，可以畅所欲言，不然大量重复低质量的帖子和评论充斥着之前的论坛，有些时候找篇帖子，找个评论可费劲了。感谢weijie老师为中国区的付出！

=======================================================================
没有幸福像这种幸福：寂静的清晨，来自河流的光，周末就在眼前。 ---詹姆斯·索特-
=======================================================================

---

### 探讨 #12: 关于《General Discussion-说任何你想说的话置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] General Discussion-说任何你想说的话置顶的_32984741297815.md
- **评论时间**: 1年前

太好了有这么一个单独的论坛，可以畅所欲言，不然大量重复低质量的帖子和评论充斥着之前的论坛，有些时候找篇帖子，找个评论可费劲了。感谢weijie老师为中国区的付出！

=======================================================================
没有幸福像这种幸福：寂静的清晨，来自河流的光，周末就在眼前。 ---詹姆斯·索特-
=======================================================================

---

### 探讨 #13: 关于《Getting started with India Alphas置顶的》的评论回复
- **帖子链接**: [Commented] Getting started with India Alphas置顶的.md
- **评论时间**: 7个月前

There are only 500 stocks in the IND, so why is the simulation speed slower than that of the AMR which includes 600 stocks?

---

### 探讨 #14: 关于《Getting started with India Alphas置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Getting started with India Alphas置顶的_36059391387415.md
- **评论时间**: 7个月前

There are only 500 stocks in the IND, so why is the simulation speed slower than that of the AMR which includes 600 stocks?

---

### 探讨 #15: 关于《Key Insights for India alphas》的评论回复
- **帖子链接**: [Commented] Key Insights for India alphas.md
- **评论时间**: 7个月前

Thanks for sharing.

What do you think of the overall survival (OS) performance of IND alpha?

---

### 探讨 #16: 关于《Key Insights for India alphas》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Key Insights for India alphas_36172722618903.md
- **评论时间**: 7个月前

Thanks for sharing.

What do you think of the overall survival (OS) performance of IND alpha?

---

### 探讨 #17: 关于《MCP结合论文实践经验分享》的评论回复
- **帖子链接**: [Commented] MCP结合论文实践经验分享.md
- **评论时间**: 7个月前

看最后的pnl图线，是一个非常好的alpha！

有几个疑问，我看文中提到的示例alpha表达式中，还存在pv类型的字段，这个字段是怎么来的呢？

贴主，是否分享一下提问的具体呀。

---

### 探讨 #18: 关于《MCP结合论文实践经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] MCP结合论文实践经验分享_36221002981271.md
- **评论时间**: 7 months ago

看最后的pnl图线，是一个非常好的alpha！

有几个疑问，我看文中提到的示例alpha表达式中，还存在pv类型的字段，这个字段是怎么来的呢？

贴主，是否分享一下提问的具体呀。

---

### 探讨 #19: 关于《Navigating Trade-offs in Alpha Development》的评论回复
- **帖子链接**: [Commented] Navigating Trade-offs in Alpha Development.md
- **评论时间**: 1年前

Among multiple indicators, I think fitness is the most important. It is a comprehensive reflection of multiple indicators. Next is margin. A high margin represents higher returns. However, margin depends on turnover, return, and drawdown. Different regions should have different numerical thresholds for margin, and you need to decide this on your own. In short, a single indicator cannot directly determine the quality of this alpha. Multiple indicators are needed for evaluation.

---

### 探讨 #20: 关于《Navigating Trade-offs in Alpha Development》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Navigating Trade-offs in Alpha Development_32120930759063.md
- **评论时间**: 1年前

Among multiple indicators, I think fitness is the most important. It is a comprehensive reflection of multiple indicators. Next is margin. A high margin represents higher returns. However, margin depends on turnover, return, and drawdown. Different regions should have different numerical thresholds for margin, and you need to decide this on your own. In short, a single indicator cannot directly determine the quality of this alpha. Multiple indicators are needed for evaluation.

---

### 探讨 #21: 关于《One Alpha submitted in different region》的评论回复
- **帖子链接**: [Commented] One Alpha submitted in different region.md
- **评论时间**: 1年前

I think this is a very good operation. If your alpha performs well in the "USA" region and also shows good performance in the "GLB" region, it indicates that this alpha is extremely stable and has a more pronounced investment effect. However, it is necessary to be cautious about preventing overfitting and maintaining a low level of correlation.

---

### 探讨 #22: 关于《One Alpha submitted in different region》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] One Alpha submitted in different region_32144831395991.md
- **评论时间**: 1年前

I think this is a very good operation. If your alpha performs well in the "USA" region and also shows good performance in the "GLB" region, it indicates that this alpha is extremely stable and has a more pronounced investment effect. However, it is necessary to be cautious about preventing overfitting and maintaining a low level of correlation.

---

### 探讨 #23: 关于《Suggestion: Option to Refine or Unsubmit an Alpha Before Its  Compensated/Paid》的评论回复
- **帖子链接**: [Commented] Suggestion Option to Refine or Unsubmit an Alpha Before Its  CompensatedPaid.md
- **评论时间**: 7个月前

Good idea. I often make incorrect submissions due to code errors or accidental slips of the hand.

---

### 探讨 #24: 关于《Suggestion: Option to Refine or Unsubmit an Alpha Before Its  Compensated/Paid》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Suggestion Option to Refine or Unsubmit an Alpha Before Its  CompensatedPaid_36117965917463.md
- **评论时间**: 7个月前

Good idea. I often make incorrect submissions due to code errors or accidental slips of the hand.

---

### 探讨 #25: 关于《依次添加到总列表中》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】复现2023年因子日历论坛精选.md
- **评论时间**: 1年前

大受震撼！！！！！！！！！！！！！！！！！！！！！

震撼之情，已经不知道怎么表达了，只能说一句，大佬牛逼！

期待大佬成功正式顾问，加入研究小组，带来更加精彩的分享！

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================

---

### 探讨 #26: 关于《依次添加到总列表中》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】复现2023年因子日历论坛精选_33049767468055.md
- **评论时间**: 1年前

大受震撼！！！！！！！！！！！！！！！！！！！！！

震撼之情，已经不知道怎么表达了，只能说一句，大佬牛逼！

期待大佬成功正式顾问，加入研究小组，带来更加精彩的分享！

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【哥布林】基于IND Region的Regular Alpha古法手搓技巧经验分享.md
- **评论时间**: 7个月前

好棒的帖子，帮助非常的多，不仅对ind这个地区有较深的理解，而且对平台的运算符、中性化、check指标好深的理解哇。

ind刚出来的时候，跑过几天，速度感觉很慢，也没有出货（我是默认打开的maxtrade、中性化使用的subindustry，侧面印证了贴主的正确性）。

等后面回测数量真的限制后，再去探索一下ind！

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【哥布林】基于IND Region的Regular Alpha古法手搓技巧经验分享_36222781155607.md
- **评论时间**: 7个月前

好棒的帖子，帮助非常的多，不仅对ind这个地区有较深的理解，而且对平台的运算符、中性化、check指标好深的理解哇。

ind刚出来的时候，跑过几天，速度感觉很慢，也没有出货（我是默认打开的maxtrade、中性化使用的subindustry，侧面印证了贴主的正确性）。

等后面回测数量真的限制后，再去探索一下ind！

---

### 探讨 #29: 关于《分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)》的评论回复
- **帖子链接**: [Commented] 【学习笔记】Gold普遍有权限的Operator 4.md
- **评论时间**: 1年前

收益良多啊，扫清了很多之前模糊的内容。

有个问题想问一下：

这个为什么可以统计最低点出现的频率

```
# 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)
```

---

### 探讨 #30: 关于《分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【学习笔记】Gold普遍有权限的Operator 4_29518553347991.md
- **评论时间**: 1年前

收益良多啊，扫清了很多之前模糊的内容。

有个问题想问一下：

这个为什么可以统计最低点出现的频率

```
# 分析最低点出现的频率low_point_frequency = ts_arg_min(close, 30)
```

---

### 探讨 #31: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/10经过前面几天的折磨和捣鼓，基本上算是搭建了一套适合的自己的搜索、回测、check、提交的全流程，也算是终于有产出了。后续计划：1. 继续优化自己的回测流程。2. 寻找新的模板，魔改论坛中的模板。3. 尝试读论文和研报，集合AI尝试性的创造一些新的模板。

---

### 探讨 #32: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/12今天有一件重大的事情，value factory 更新了，这次更新的事24年10、11、12月份的（听各位大佬说的），but我的value factory并没有变化，可能是提交alpha不够多，也可能是质量不太行，大概提交了30左右吧，质量的话从base payment上看，一个alpha的话只有1.4左右，所以质量并不是很高。这次更新有很多大佬都拿到了0.9以上，大于有30多位，！！！还有以为女生大佬竟然拿到了1.0，太强了，期待下一次的更新，这段时间要多交点alpha，希望下次我能提升到0.7左右吧，加油！今天提交了1alpha，还是再试水，拿到了1.51，超过了1.5也就说说明质量还算可以，继续加油，争取明天提交两个。嘿嘿。

---

### 探讨 #33: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/14今天参加了顾问小组的第一次课，收获了非常多，见识到了非常多厉害的大佬和新人大佬。总结出了下面几个点：1. 一定要将回测量上去，回测量上去了出货、出好的alpha可能性才会更大。可以看看获奖的人，回测多的人一般都会有几个其它的奖项。所以一定要优化回测的方法，可以使用wqb，或者自己写多线程，其中有一位大佬提到不用多线程也可以，就是不断的发送alpha，达到100个后服务器拒收，就重新存回去，然后每个1秒就重新发一个，这样也可以达到100%的使用效率。非常好的观点。2. 三阶模板的含金量还在上升，但是不能死跑，需要理解三阶模板的意义，然后优化改进一下，这个邮件里有提到一些，也可以加入自己的观点，会有不一样的收获。上面提到也就是我接下来要做的。说说今日提交的alpha和base payment吧，依旧是只提交了1个，但是这次只拿到了1.49，低于了1.5，说明这个alpha很差了，不是基本不赚钱了而是直接赔钱了，但这已经是我当前存货里面最好的了，那么剩下的基本上也不用交了，等把三阶模板优化好再看情况吧。

---

### 探讨 #34: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/17坏消息：已经断粮了...尝试了一下会议上提到了交换一阶和二阶，但是跑了一些ASI的字段，效果很差...也尝试了一些老虎哥新出的在EUR的模板，把全部字段跑了一遍，一个出了都没有...为啥呀，为啥老虎哥能出我的就出不了呀，猜测是setting不同，或者有什么其它的优化...再尝试优化一下一二三阶模板吧，按照会议上一位大佬说的，对于时序数据，多套基层时序op，再尝试一下吧...好消息：使用wbq，这几天基本上将回测打满了，大约在2-3w左右，相对比与之前的1w都不到，是跟很大的提升，必须要把回测量上去了，出货的可能性才会更大。

---

### 探讨 #35: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/18今天eur更新了一个新的区域top2500，连夜挖了一下，基本上没出货，有些前面表现很好后面之久直接平了，不知道怎么优化，看到的大佬可以给下改进方法，万分感激。一个小发现：genius里面的数据，有的是你提交alpha就直接更新，有的是第二天统计后才更新。今日work：跑了老虎哥之前的双字段回归的模板，USA下跑了两个数据集risk和earning，没出货，但看到之前有老跑了400个字段，出了100alpha，属实震惊了，可能数据集没选对吧，希望大佬给点提示。EUR下跑了老虎哥的新模板，TOP1200和TOP2500都跑完了，TOP1200没出货，TOP2500出了两个，表现一般，还需要优化。今天payment：提交了1个ASI的，pro0.5多，表现一般般，以为收益会高一点点，没想到依旧是1.51，哎库存就剩了一个EUR的了，明天交完又断粮了。

---

### 探讨 #36: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/19昨日战绩：提交了一个的EUR TOP2500拿到了 1.76，是迄今为止提交一个alpha拿到过最多的base pay。今日工作：重新优化一二三阶模板，因为看到QQ大佬说，仅跑一二三阶模板，vf就拿到了0.9，（我之前没有将一二三阶跑完，以为烂大街的东西...）现在在优化的基础上完完全全的把所有的数据跑一遍，看看情况。

---

### 探讨 #37: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/20今日收入：交了一个EUR-TOP2500的因子，拿到了1.72，感觉还不错，但是fitness和margin都不高，prod0.5左右，拿到1.7感觉是倍数高的原因。今日工作：昨天开始跑的一二三阶-EUR-analyst14，一阶数量并不多，二阶也很少，但是三阶段组合出的因子就非常多了，要跑很久，现在还没有跑完，等跑完统计一下出了多少个可以提交的alpha吧，初步看了一下出货还挺多的。遇到了一个wqb的bug，查询alpha的时候传入东八区的时间会异常，例如“2025-02-10T14:55:12+08:00”，但是传入西五区的时间就不会，“2025-02-19T01:55:12-05:00”，研究后发现，wq平台对于url中的“+”不会正常解析，也就说，如果你直接将拼接好的url发送到wq服务器请求，wq服务器时解析不了其中的“+”，如果你再发送请求前就解析好了，那么是没问题的。该问题已联系wqb的作者，且已进行了修复。

---

### 探讨 #38: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/21今日收入：<2，炸了，前两天只交一个可以拿到1.7左右，今天直接交满了四个，直接炸了，这四个的表现和之前的两个差不多，但是前两个是单数据集的，这四个里面三个是三数据集的，一个双数据集的，直接炸了，感觉下次vf更新要暴跌了，可怜，难道说单数据集的alpha要远优于多数据集的吗？还是因为这四个因子表现确实不行呢...今日工作：无新内容，继续跑EUR-TOP2500

---

### 探讨 #39: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/22今日收入：依旧是1个EUR-TOP2500的alpha，收入1.52，奇怪提交一个可以拿到1.5，提交四个却连2都拿不了...今日工作：ERU-TOP2500-analyst14已经跑完了，共提交8个alpha。后面先不打算跑ERU-TOP2500地区的了，先跑跑ASI地区的吧，发现ASI的速度是ERU速度的1/3。

---

### 探讨 #40: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/23今日收入：1.4，提交的事EUR-TOP2500-analyst14跑出来的最后一个alpha，表现很差...感觉EUR地区的alpha质量普遍不高，是我的问题还是这个地区就是这样。今日工作：ASI - 1 - MINVOL1M-analyst14已经跑了38%了，一阶段到现在为止仅出了一个可提交的alpha，且表现不好，等明天再看看情况吧，ASI跑的巨慢，速度仅有EUR的1/3，出货也不多，堪忧呀，感觉马上就要断粮了。

---

### 探讨 #41: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/25今日收入：一个ASI的alpha，收入1.54，表现一般般，没库存了，要断粮咯...今日工作：之前跑的ASI的analyst14不知道因为什么原因中断了，只能重新跑了，重新跑的时候，虽然我使用了random来打乱顺序，但还是出现了大量的重复，所以决定不重新跑了，跑下analyst15试试看。另外，不打算跑第三阶段了，仅跑一二阶段工作量就巨大，270多个字段，一阶段就会出现7万多个alpha，太多了，尤其是ASI跑的还巨慢....

---

### 探讨 #42: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/2/26昨天断粮了，今天交了一个EUR的单因子alpha，相关性很低，只有0.46，指标表现一般，但是突破了我1个alpha的最高收入记录，回测数量也达到了最高，来到了33.6k。今日收入：1个EUR-TOP2500的单因子alpha，0.5vf，1.98$，是我交1个alpha以来拿到的最高记录。今日工作：依旧在跑EUR-TOP2500-anl，数量有点多，感觉要四五天才能跑完。听说eur地区最近会上theme，这应该是加入wq以来第一次碰到theme，不知道具体是个什么情况，期待。

---

### 探讨 #43: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/3/4有段时间没更新日记了，一方面因为断粮，一方面因为最近有点忙。今日收入：4.08，一个EUR的alpha，因为theme的加成，直接来到了4.08，达到了历史新高，舒服了。看了眼日记，发现在theme加成的影响下，很多很多大佬的日收入都达到了80+，太羡慕了，最近马上要更新combine和vf了，但是我交的alpha还是非常少，上次更新的时候vf就没更新依旧是0.5，不知道这次会不会更新，希望能高一点点，上香~今日工作：前段时间发现，使用wqb回测的时候，有时候会莫名其妙中断，且没有回测地址，也看不到是因为什么原因出错中断了，今天把wqb回测方法中的“出错不中断”参数开启了，看看后面还会不会出现同样的问题。

---

### 探讨 #44: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/3/8这次真清楚的感受到单字段因子的厉害了，昨天交了4个单字段的因子，拿了5.7刀，今天交了3个多字段的因子，只拿了2刀，指标表现上看多字段的因子会更好，但是最后的base pay明显的低了很多，看来以后得提交策略要改变一下了，单字段>多字段，没货的情况下，多字段每天只交一个是最优解了。vf 0.5。

---

### 探讨 #45: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/3/12回顾一下这段时间的alpha提交，除了开始时的其它地区提交了几个外，在eur top2500出来后，以及后面eur的theme出来后，提交的全是eur地区，当然这段时间内eur地区确实容易出货，但是只提交一个地区的alpha是不符合alpha分散策略的，主要是alpha的挖掘模板有点问题，当前是按照地区或者说是按照数据集id来进行挖掘的，后面需要优化一下，改进成一次挖掘任务要从多个不同地区的不同数据集中获取字段，进行挖掘，这样大概率会出现多个地区的alpha，加入计划，等这次的vf更新后，好好优化一下代码。

---

### 探讨 #46: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/3/18vf 0.22，提交了3个alpha，base 1.18，看来vf低了，不管提交几个，base都会在很低的小范围内徘徊，像我，vf0.22，基本上就在1.2上下不超0.1徘徊了...昨天完成了多地区的回测，但是库存还有好多个eur的alpha没有提交，今天check一下，看看昨天跑的其它地区有没有产出吧。发现一个问题，一阶段出现的可提交的因子，提交一个后，基本上不会影响其它可提交的因子，或者说相关性增加不大，但是二阶段、三阶段的可提交因子，提交一个后，基本上就会死一大片了，self相关性基本上就来到了0.9左右，（我着重看过，不是相同的字段）这是不是一定程度上说了，二阶段三阶段出的因子其中的字段并不是主信号，而是一个副信号呢...

---

### 探讨 #47: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/3/27vf 0.22 日常坐牢，不管交多少个 base 都超不过 1.2 ...终于解锁 sa 了，听大佬们说 sa 非常有助于提升 vf，看来要好好研究下 sa 的写法了，需要迫切提升 vf 不想再坐牢了刚好收到了 vf 提升计划的邀请，已报名！勿辜负！

---

### 探讨 #48: 关于《统计每天提交的from collections import defaultdictfrom datetime import datetime按日期分组date_groups = defaultdict(list)for alpha in all_alpha_list:if alpha.get("dateSubmitted"):提取日期部分（去掉时间）date_str = alpha["dateSubmitted"].split("T")[0]date_groups[date_str].append(alpha)生成按日期统计的报告for date, alphas in sorted(date_groups.items(), reverse=True):print(f"今天是{date}, 一共提交了 {len(alphas)} 个alpha")for i, alpha in enumerate(alphas, 1):sharpe = round(alpha["is"]["sharpe"], 2)fitness = round(alpha["is"]["fitness"], 2)region = alpha["settings"]["region"]alpha_type = alpha["type"]turnover = round(alpha["is"]["turnover"] * 100, 2)returns = round(alpha["is"]["returns"] * 100, 2)drawdown = round(alpha["is"]["drawdown"] * 100, 2)margin = round(alpha["is"]["margin"] * 10000, 2)print(f"    第{i}个: type={alpha_type},  region={region}, sharpe={sharpe}, fitness={fitness}, "f"turnover={turnover}, returns={returns}, drawdown={drawdown}, margin={margin}")print('''--------------------------------------------------------------------------------------------------------------没有平坦的大道，只有不畏劳苦沿着陡峭山路攀登的人，才有希望达到光辉的顶点。''')print()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXXeDIeho6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMjkxMTQ2NTg0NzkzODMtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjglODAlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYTBiZmI1YS1jYWU3LTQ3MGUtOTEwMC1kYmUyYWQyZjQwMmIGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxKRzE1MjQ0BjsIVDoScmVzdWx0c19jb3VudGkQ--78f238d3d5962b931804e9de39d6fc7d496bcd46
- **评论时间**: 1年前

2025/04/11顾问 顾问 JG15244 (Rank 67) (Rank 67) 的量化日记。-------------------------------------------------vf 又更新了，这次来到了 0.44（12,1,2），还好有提升，之前是 0.22（11,12,1），0.22的时候三个月总共我只提交了30多个alpha，这次0.44总共提交了50个alpha，看来 vf 和数量还是有关系的，3月份提交了大量的eur地区以及部分asi地区的alpha，但是质量非常一般，不知道下次更新到3月份的时候 vf 会不会又跌回去，接下来的时间将重心着重放到 usa 地区吧！今天尝试了一下开启 max 选项，发现跑出来的 alpha 质量非常好，但是出货率确实也比较低。

---

### 探讨 #49: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/10

经过前面几天的折磨和捣鼓，基本上算是搭建了一套适合的自己的搜索、回测、check、提交的全流程，也算是终于有产出了。


> [!NOTE] [图片 OCR 识别内容]
> [root@ece-77846 firal
> chire」 # Ppthor
> I_Script
> USEI
> 顾问 顾问 JG15244 (Rank 67) (Rank 67)
> tokerl
> erpir
> 14400.0}
> permissiors
> ["CONSILTAKI
> "IILTI_SIIILSTIOIT
> PROD_SFILS"
> 飚`咫虹
> TIS[i
> IZSTIONJ'
> 'IORIIsr
> aet_fieldids () 方法
> 开始获取数据字段。
> 功获取[34
> 10P3000的
> 197条
> [Sa
> TOP3000
> 868籴
> [3』
> TOP30OOE
> 2538籴
> 取[3乌
> IOP30OO
> 107籴
> TGP300
> TOP3000
> TOP3OO0
> TOP3000
> [S』
> TGP300
> TGP300
> TOP3000
> TOP300C
> TGP300
> TOP3000
> 488
> [S』
> TOP3OO0
> 获取I32
> TOP3OOOE
> 获取[34
> TP3000的
> 488籴
> I6P3000的
> 21蜍
> 苡功获取[3』
> T0P3000的=
> 1?籴
> fieldids
> 方法执行完
> 取数据字段  &454条-
> 在执行proces3_
> datafields
> 预处理数据字段
> PrOcess_datafields
> 方法执-
> 共预处理数据字段  1016? 条
> 正在执行eenerate_expressions_
> T1tli_fields
> ()方法
> 组合生成表二
> Senerate
> epres310IIS_
> Hitll_fields
> ()方法执行完毕
> 共生成  1016?  个表达式
> 初始aecay 追加完成
> deca
> 则池组
> 113
> 回测池
> POoL
> tasl
> Dost
> dole
> Pool
> taak &
> SiIlllate
> dole
> POoL
> task
> Post dole
> POol
> taak &
> SiIlllate
> dole
> SeT



> [!NOTE] [图片 OCR 识别内容]
> 检查10个alpha =
> ZOZITINI,
> ZOZPIi
> 3921183
> 3921230;
> 392LJJe
> 39211
> 3922130
> 392SI0;
> 3929103,
> 392a迟0
> 检查10个alpha
> 392eT
> 392[#环,
> 392L gIe;
> 392u2p0,
> 3924006,
> 392IIa0,
> 3924630,  39247a8,
> 3924Rn,
> 3924112
> 处理upha
> 3921826  时发生错误=
> Eypectirg
> le
> lire
> C0I1III
> char 0〉
> 在进行二
> 重试
> 橙查10 ^
> aIpla
> 3924152,
> 3925
> 2;
> 3923826
> 392H 56
> 392250,
> 39J210e,
> 39J5kS;   39JJIbG
> 39Jkgd0
> 39J42
> 检查
> aLPIal
> [卫0,
> 39J缸叮
> TTT6
> 3901310,
> 39Ob1a2
> 390Eoxe-
> 3908Ro
> 3g0Jdse
> 390k730,
> 3gOLJbe
> 检查10个alpha
> 3gO0GVZ
> 3SOogdz
> 39Ooyl0,
> 3gOdJalT,
> 3gOae
> 3SHJ[4a0;
> 39+48
> 3grnR0,
> 395710,
> 39xep2
> Pha
> 5Q16p5
> 8瓯
> CORRELSTIOI=O. 4977
> FROD_CORRELSTIOI=0
> STAT[8=S[J2C区88
> 检查10-
> aIpla
> 5Ql6p35
> 5lr匹
> SQIbkaJ
> 501
> 50119J6
> 501136
> 5l19u
> SQLogo,
> SQlrglk
> SQlrlzz
> 检查10-
> aIpla
> SQIrgl5,
> 501j66
> 5022801
> 502281[,
> SO2gL4r;
> SQ2alzk;
> 5023021,
> 50253112,
> 5Q2b5,
> 502471
> 检查10 -
> aIpla
> 50211}
> 502k琏二
> 5020672
> SQ2OBT6
> SQ2PPi」
> SQ2Q2R1
> SQ2RoTo
> 50239趾
> SQ2ur1
> SQ270
> E查10个
> Pha
> SQaglgk
> 5049245,
> SQalloall
> SQdri86
> SOARRP 二
> SQdrOk5
> 5Qai75
> SQdgB[
> 50do1  ;
> SQdarNT
> Ipha Gr25x
> 3E
> CORREI
> IOI=D. 5022
> 'ROD_CORREL
> Ol=0
> 66GG
> STeT[J8=3[22E38
> 检查10-
> Pha
> SQax2k
> QT2r65
> SQTSreJ
> 5Qi5q1
> Br2ladp
> Br21a6
> Gr22}
> Gr25x8J, 6r2787,
> 6r280哑
> IIpla
> Gr2Bn
> SELE
> CORRELSTIOI=O. 5466
> PROD_CORRELATIOIT0. 6889
> STeT[J8=3[22E38
> Ilpha
> Gr2Lw2
> SELE
> RURREL
> STIOIJ=0. 5283
> PRUD
> CORRELSTIOI=O. 6794;
> STAT[8=S[J2C区88
> 检查
> aIpla
> Gr2gdrg
> Gr2Bn
> Gr2aBp
> Gr2B?AJ
> Gr2jdap
> Gr2JB
> Gr2kiGL
> Gr2LPar
> Gr2Li
> fr2lL
> 检查10个alpha
> Gr2O5F
> Gr2aGng
> Gr2dZ2G
> Gr2wr l
> 6r221R
> GrLlai
> GrL?aoL,
> GrLeBIP
> GrLa367,
> GrLOIIS
> 检查10个alpha
> GrLgf 证
> GrLHa0,
> GrLTRSp
> GrLzf} E
> Grl2noE
> GrlIZaLT
> Grl62虹
> GrlTTLJLE
> Brl8SE
> GrlloP0


后续计划：

1. 继续优化自己的回测流程。

2. 寻找新的模板，魔改论坛中的模板。

3. 尝试读论文和研报，集合AI尝试性的创造一些新的模板。

---

### 探讨 #50: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/12

今天有一件重大的事情，value factory 更新了，这次更新的事24年10、11、12月份的（听各位大佬说的），but我的value factory并没有变化，可能是提交alpha不够多，也可能是质量不太行，大概提交了30左右吧，质量的话从base payment上看，一个alpha的话只有1.4左右，所以质量并不是很高。

这次更新有很多大佬都拿到了0.9以上，大于有30多位，！！！还有以为女生大佬竟然拿到了1.0，太强了，期待下一次的更新，这段时间要多交点alpha，希望下次我能提升到0.7左右吧，加油！

今天提交了1alpha，还是再试水，拿到了1.51，超过了1.5也就说说明质量还算可以，继续加油，争取明天提交两个。嘿嘿。

---

### 探讨 #51: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/14

今天参加了顾问小组的第一次课，收获了非常多，见识到了非常多厉害的大佬和新人大佬。

总结出了下面几个点：

1. 一定要将回测量上去，回测量上去了出货、出好的alpha可能性才会更大。可以看看获奖的人，回测多的人一般都会有几个其它的奖项。所以一定要优化回测的方法，可以使用wqb，或者自己写多线程，其中有一位大佬提到不用多线程也可以，就是不断的发送alpha，达到100个后服务器拒收，就重新存回去，然后每个1秒就重新发一个，这样也可以达到100%的使用效率。非常好的观点。

2. 三阶模板的含金量还在上升，但是不能死跑，需要理解三阶模板的意义，然后优化改进一下，这个邮件里有提到一些，也可以加入自己的观点，会有不一样的收获。

上面提到也就是我接下来要做的。

说说今日提交的alpha和base payment吧，依旧是只提交了1个，但是这次只拿到了1.49，低于了1.5，说明这个alpha很差了，不是基本不赚钱了而是直接赔钱了，但这已经是我当前存货里面最好的了，那么剩下的基本上也不用交了，等把三阶模板优化好再看情况吧。

---

### 探讨 #52: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/17

坏消息：

已经断粮了...

尝试了一下会议上提到了交换一阶和二阶，但是跑了一些ASI的字段，效果很差...

也尝试了一些老虎哥新出的在EUR的模板，把全部字段跑了一遍，一个出了都没有...为啥呀，为啥老虎哥能出我的就出不了呀，猜测是setting不同，或者有什么其它的优化...

再尝试优化一下一二三阶模板吧，按照会议上一位大佬说的，对于时序数据，多套基层时序op，再尝试一下吧...

好消息：

使用wbq，这几天基本上将回测打满了，大约在2-3w左右，相对比与之前的1w都不到，是跟很大的提升，必须要把回测量上去了，出货的可能性才会更大。

---

### 探讨 #53: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/18

今天eur更新了一个新的区域top2500，连夜挖了一下，基本上没出货，有些前面表现很好后面之久直接平了，不知道怎么优化，看到的大佬可以给下改进方法，万分感激。


> [!NOTE] [图片 OCR 识别内容]
> 1ON
> 12/06/2017
> TralnDnL  9,412.84
> 8OOOK
> OOOK
> 40OOK
> 20OOK
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


一个小发现：genius里面的数据，有的是你提交alpha就直接更新，有的是第二天统计后才更新。

今日work：

跑了老虎哥之前的双字段回归的模板，USA下跑了两个数据集risk和earning，没出货，但看到之前有老跑了400个字段，出了100alpha，属实震惊了，可能数据集没选对吧，希望大佬给点提示。

EUR下跑了老虎哥的新模板，TOP1200和TOP2500都跑完了，TOP1200没出货，TOP2500出了两个，表现一般，还需要优化。

今天payment：

提交了1个ASI的，pro0.5多，表现一般般，以为收益会高一点点，没想到依旧是1.51，哎库存就剩了一个EUR的了，明天交完又断粮了。

---

### 探讨 #54: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/19

昨日战绩：

提交了一个的EUR TOP2500拿到了 1.76，是迄今为止提交一个alpha拿到过最多的base pay。


> [!NOTE] [图片 OCR 识别内容]
> Single Data Set Alpha
> Pyramid theme: EURIDIIANALYST X1.6
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> 1.97
> 11.719
> 1.10
> 3.8796
> 3.369
> 6.609600


今日工作：

重新优化一二三阶模板，因为看到QQ大佬说，仅跑一二三阶模板，vf就拿到了0.9，（我之前没有将一二三阶跑完，以为烂大街的东西...）现在在优化的基础上完完全全的把所有的数据跑一遍，看看情况。

---

### 探讨 #55: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/20

今日收入：

交了一个EUR-TOP2500的因子，拿到了1.72，感觉还不错，但是fitness和margin都不高，prod0.5左右，拿到1.7感觉是倍数高的原因。

今日工作：

昨天开始跑的一二三阶-EUR-analyst14，一阶数量并不多，二阶也很少，但是三阶段组合出的因子就非常多了，要跑很久，现在还没有跑完，等跑完统计一下出了多少个可以提交的alpha吧，初步看了一下出货还挺多的。

遇到了一个wqb的bug，查询alpha的时候传入东八区的时间会异常，例如“2025-02-10T14:55:12+08:00”，但是传入西五区的时间就不会，“2025-02-19T01:55:12-05:00”，研究后发现，wq平台对于url中的“+”不会正常解析，也就说，如果你直接将拼接好的url发送到wq服务器请求，wq服务器时解析不了其中的“+”，如果你再发送请求前就解析好了，那么是没问题的。该问题已联系wqb的作者，且已进行了修复。


> [!NOTE] [图片 OCR 识别内容]
> apiworldquantbrain com/users/selflalphas?dateCreatedy= 2025-02-10114:55:12-08:008dateCreated <2025-02-19122:35:05-08:008drder=dateCr.
> 压 V %
> @
> 8 |
> 器
> 臼 JBINFO
> 技术文档
> 臼 AII具
> 口 魔法梯子
> 口 智慧工地
> 口学
> 口 工具
> 口  论文
> 口 游戏
> 口  运营一体化
> 臼
> worldquant
> 口 gulimall
> 够 Refer a friend
> 2025年假调休安排。
> FeHelper
> 排序:
> 默认
> 升序O
> 降序0
> 乱码修正
> 元数据
> 折叠所有
> 下载JSON
> {高级定制
> 隐藏
> COUT
> 10000
> next
> "htln;LLani
> JLLgqynzbsa迎卫
> Com:443LusersLselflalphas?dateCreated咝3C2025-02-19122934355
> 0-0833
> 0adateCreatedm3e=2025-02-1011493455亟3412-0843400Liit=lloffset=lRordersdatecreated
> Drevious
> IUIII
> reSuIts



> [!NOTE] [图片 OCR 识别内容]
> 畎11325
> 已发布0.2.5,修复了刚才的问题
> 现在用+时区没问
> 题了
> 谢谢大佬


---

### 探讨 #56: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/21

今日收入：

<2，炸了，前两天只交一个可以拿到1.7左右，今天直接交满了四个，直接炸了，这四个的表现和之前的两个差不多，但是前两个是单数据集的，这四个里面三个是三数据集的，一个双数据集的，直接炸了，感觉下次vf更新要暴跌了，可怜，难道说单数据集的alpha要远优于多数据集的吗？还是因为这四个因子表现确实不行呢...

今日工作：

无新内容，继续跑EUR-TOP2500

---

### 探讨 #57: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/22

今日收入：

依旧是1个EUR-TOP2500的alpha，收入1.52，奇怪提交一个可以拿到1.5，提交四个却连2都拿不了...

今日工作：

ERU-TOP2500-analyst14已经跑完了，共提交8个alpha。

后面先不打算跑ERU-TOP2500地区的了，先跑跑ASI地区的吧，发现ASI的速度是ERU速度的1/3。

---

### 探讨 #58: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/23

今日收入：

1.4，提交的事EUR-TOP2500-analyst14跑出来的最后一个alpha，表现很差...

感觉EUR地区的alpha质量普遍不高，是我的问题还是这个地区就是这样。

今日工作：

ASI - 1 - MINVOL1M-analyst14已经跑了38%了，一阶段到现在为止仅出了一个可提交的alpha，且表现不好，等明天再看看情况吧，ASI跑的巨慢，速度仅有EUR的1/3，出货也不多，堪忧呀，感觉马上就要断粮了。

---

### 探讨 #59: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/25

今日收入：

一个ASI的alpha，收入1.54，表现一般般，没库存了，要断粮咯...

今日工作：

之前跑的ASI的analyst14不知道因为什么原因中断了，只能重新跑了，重新跑的时候，虽然我使用了random来打乱顺序，但还是出现了大量的重复，所以决定不重新跑了，跑下analyst15试试看。

另外，不打算跑第三阶段了，仅跑一二阶段工作量就巨大，270多个字段，一阶段就会出现7万多个alpha，太多了，尤其是ASI跑的还巨慢....

---

### 探讨 #60: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/2/26

昨天断粮了，今天交了一个EUR的单因子alpha，相关性很低，只有0.46，指标表现一般，但是突破了我1个alpha的最高收入记录，回测数量也达到了最高，来到了33.6k。

今日收入：

1个EUR-TOP2500的单因子alpha，0.5vf，1.98$，是我交1个alpha以来拿到的最高记录。

今日工作：

依旧在跑EUR-TOP2500-anl，数量有点多，感觉要四五天才能跑完。

听说eur地区最近会上theme，这应该是加入wq以来第一次碰到theme，不知道具体是个什么情况，期待。

---

### 探讨 #61: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/3/4

有段时间没更新日记了，一方面因为断粮，一方面因为最近有点忙。

今日收入：

4.08，一个EUR的alpha，因为theme的加成，直接来到了4.08，达到了历史新高，舒服了。

看了眼日记，发现在theme加成的影响下，很多很多大佬的日收入都达到了80+，太羡慕了，最近马上要更新combine和vf了，但是我交的alpha还是非常少，上次更新的时候vf就没更新依旧是0.5，不知道这次会不会更新，希望能高一点点，上香~

今日工作：

前段时间发现，使用wqb回测的时候，有时候会莫名其妙中断，且没有回测地址，也看不到是因为什么原因出错中断了，今天把wqb回测方法中的“出错不中断”参数开启了，看看后面还会不会出现同样的问题。

---

### 探讨 #62: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/3/8

这次真清楚的感受到单字段因子的厉害了，昨天交了4个单字段的因子，拿了5.7刀，今天交了3个多字段的因子，只拿了2刀，指标表现上看多字段的因子会更好，但是最后的base pay明显的低了很多，看来以后得提交策略要改变一下了，单字段>多字段，没货的情况下，多字段每天只交一个是最优解了。

vf 0.5。

---

### 探讨 #63: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/3/12

回顾一下这段时间的alpha提交，除了开始时的其它地区提交了几个外，在eur top2500出来后，以及后面eur的theme出来后，提交的全是eur地区，当然这段时间内eur地区确实容易出货，但是只提交一个地区的alpha是不符合alpha分散策略的，主要是alpha的挖掘模板有点问题，当前是按照地区或者说是按照数据集id来进行挖掘的，后面需要优化一下，改进成一次挖掘任务要从多个不同地区的不同数据集中获取字段，进行挖掘，这样大概率会出现多个地区的alpha，加入计划，等这次的vf更新后，好好优化一下代码。

---

### 探讨 #64: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/3/18

vf 0.22，提交了3个alpha，base 1.18，看来vf低了，不管提交几个，base都会在很低的小范围内徘徊，像我，vf0.22，基本上就在1.2上下不超0.1徘徊了...

昨天完成了多地区的回测，但是库存还有好多个eur的alpha没有提交，今天check一下，看看昨天跑的其它地区有没有产出吧。

发现一个问题，一阶段出现的可提交的因子，提交一个后，基本上不会影响其它可提交的因子，或者说相关性增加不大，但是二阶段、三阶段的可提交因子，提交一个后，基本上就会死一大片了，self相关性基本上就来到了0.9左右，（我着重看过，不是相同的字段）这是不是一定程度上说了，二阶段三阶段出的因子其中的字段并不是主信号，而是一个副信号呢...

---

### 探讨 #65: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/3/27

vf 0.22 日常坐牢，不管交多少个 base 都超不过 1.2 ...

终于解锁 sa 了，听大佬们说 sa 非常有助于提升 vf，看来要好好研究下 sa 的写法了，需要迫切提升 vf 不想再坐牢了

刚好收到了 vf 提升计划的邀请，已报名！勿辜负！

---

### 探讨 #66: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025/04/11

顾问 顾问 JG15244 (Rank 67) (Rank 67) 的量化日记。

-------------------------------------------------

vf 又更新了，这次来到了 0.44（12,1,2），还好有提升，之前是 0.22（11,12,1），0.22的时候三个月总共我只提交了30多个alpha，这次0.44总共提交了50个alpha，看来 vf 和数量还是有关系的，3月份提交了大量的eur地区以及部分asi地区的alpha，但是质量非常一般，不知道下次更新到3月份的时候 vf 会不会又跌回去，接下来的时间将重心着重放到 usa 地区吧！

今天尝试了一下开启 max 选项，发现跑出来的 alpha 质量非常好，但是出货率确实也比较低。

---

### 探讨 #67: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025年7月17日

断了，呜呜呜，这个赛季本来想拿满一个每天都提交的成就的，可惜今天工作太多了，没来得及提交，随便选了一个可以submit的，可惜corr没过.......

唉，以后要前一天的晚上提交好，这样第二天的白天才会有更多的时间来选择好的提交！

好在最近也是把regular、super的全套流程+数据库的方式都跑通了。

最近新出的app还没研究，后面要找时间慢慢研究一下，感觉会有非常大的提升。

=======================================================================
问题的答案不在脑子里，只有行动才能找到答案。 ---埃克哈特·托利-
=======================================================================

---

### 探讨 #68: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025年7月21日

最近又更新了一次vf，距离上次更新仅仅20天。

这次的更新来到了 0.96，比之上次降低了 0.01，这次更新的时间范围 3、4、5，ppa的打击还没有完全到来，但是从第一次更新 ppa的comb来看（0.89），vf 距离暴跌也差不多了，还有sac的打击也没有到来...

这次国区vf 0.9 以上的足足有90多位，真的是蒸蒸日上了！国区牛逼！

最近虽然吧regular、super 的回测框架都搭建好了，但是regular基本上还是不出货呀，偶尔的ppa质量也堪忧，根本不敢交，super组别人的因子上双5其实还比较容易（可能都是过拟合，hhhh），但是组自己的话上双5就比较困难了。这配额是真难搞哇。

最近抽点时间研究一下使用lab来看数据的分布，然后借助app来分析。

---

### 探讨 #69: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025年7月28号

ra和ppa的出货基本无了，感觉方法错了。。。

sa正常提交，后面如果vf降低的话就尽量的提交own的sa，一方面自己提交ra都是经过了自己的质量把控，质量相对来说比较好一点，同时也可以增加not(own)的配额，等vf升高的时候，就可以猛猛赚钱了，嘿嘿。

7月份马上就要结束了，接下来重新改变一下策略，同时预留出一部分槽位专门留给lab+app的测试，定向暴破pyr，希望能够有所收获吧。

=======================================================================
教育就是一棵树摇动另一棵树，一朵云推动另一朵云，一个灵魂唤醒另一个灵魂。 ---雅斯贝尔斯-
=======================================================================

---

### 探讨 #70: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月4日

最近开始跑 amr 地区了，跑的速度是真快啊，感觉如果 all in 跑的话，每天破 5 万不是问题。

跑了一些也发现了一些问题，amr 的很多alpha 的 sharpe 都低，之前跑四大区的时候，fitness 和 sharpe 几乎相同，即使不同也不会差很多，但是 amr 有的 fitness 很高，但是 sharpe 就过不了标准了，好在最近小地区也开放了 ppa 的提交规则。

还有一个很奇怪的现象，最开始是开启了 maxtrade 选项的，但是后面微调的时候，关掉回测了一下，发现结果直接是相反的...，暂不清楚是个例还是什么情况，现在已经新增一批关闭 maxtrade 选项，等回测后看一下情况。

还有最近平台提交是真的慢....

另外最近开始很多新人为了点塔，都开始做 d0 区域的了，不知道这是好事还是坏事，等后面更新 combine 和 value factory后看看吧。

---

### 探讨 #71: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月9日

今天ra新高了，50多刀，这是高vf后第一次这么高的收益。

今天提交了一个usa、3个amr的ppa。给了50.03刀。

然后sa是提交了一个3个5的not own，只给36.14刀。sa给的很低了，按道理说这种纸面数据的sa，在我这个vf下，怎么着也得给40刀+了，之前确实也会给到40刀+，但是最近有几个的数据跟之前一致，但是给的就在36、37刀附近了，感觉是os爆炸了...

另外虽然交了小地区给的钱比较多，但是小地区确实是不稳定，尽量还是挑好的交，不然到时候vf就爆炸了。

=======================================================================
卧看满天云不动，不知云与我俱东。 ---陈与义-
=======================================================================

---

### 探讨 #72: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月11日

今天收入再破新高，来到了97.06。

今日提交情况是4个amr的ppa，1个not own的sa。

ra给了58.34。今天提交的全是atom的alpha，乘数都在1.8、1.7，结合昨天的情况可以看出来，其实并不是小地区给的钱多，只是小地区的乘数高而已，如果乘数不高即使是小地区也不会给多少钱。

sa今天跟之前一样，看来又是os炸了，3个5的super alpha按理说可以拿到40+的，但是只给了38左右....

今天听大佬们谈论起来，突然发现，其实这个阶段是不应该跑小地区的，也不应该交小地区，因为小地区部稳定，不仅会搞崩vf，也会搞崩comb，而comb崩了的话，那么genius等级基本上就追不上去了...

但是反过来说，因为上次vf更新时0.97，这次来到了0.96，而且comb有降低，所以如果下次vf更新低了的话，也拿不到钱了，感觉分成了genius派和vf派了，一个拿季度奖，一个拿basepayment....但也不排除有真大佬两者都兼顾...

算了不想那么多了，amr交都交了，那就交到底吧，尽量多交点稳定一点，后面也交几个amr的sa，来稳定一下，只有这个办法了。

global的比赛开了，今天刚改好代码框架，感觉得2-3天后才能出货，等等看吧。

---

### 探讨 #73: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月12日

今天收入回归正常，62.54。

今天的提交情况是3个amr的ppa，一个own的sa。

先说ra，ppa的限额终于来了，非 atom 的ppa每日只能提交一个了，感觉大大降低了靠ppa来刷pyr的情况。

今天之所以提交了3个ra，是因为时间来不及了，导致最后一个没提交上去....

3个ra给了46.97，感觉还不错，跟前几天相比的话属于正常水平。

今天是一个own的sa，可惜prodcorr没有在0.5以下，不过出乎意料的是竟然给了15多，这个真出乎意料了，之前只会给9左右，可能这个os比较好吧，哈哈哈哈哈。

另外，不知道为什么昨天把usa的槽位给了glb后，amr的回测竟然莫名其妙停掉了，停了半天才发现，啊啊啊啊，看来又没有机会竞争双周会的奖了。

再说下glb的出货情况，昨天到今天一个没出，我跑的topdiv3000这个池子，看大佬们都在跑min那个池子，等我这个再跑个两天看看情况，如果还是不出货的话，我也换到min池子看看。

再就是global的比赛，好像大多数大佬都不太想参与，怕搞崩掉genius，不够我倒是还挺想参与一下，可惜不出货....真的是旱的旱死，涝的涝死。

---

### 探讨 #74: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月13日

今日收益又高回去了...有点离谱，今天只提交了一个sa、两个ra，竟然给了92.49美金。

前两天以为ra的收益主要受theme的乘数控制，今天仔细回顾了一下之前提交的pc的值，发现ra的收益受pc控制也挺高的，但是谁的权重更多，这个倒是还不清楚。

说下今天的提交情况：

一个 not own 的 asi 的 super alpha，pc在0.49多，给了41.15，相比之前提交的算比较好的了，但是8月份asi的ra几乎没有提交，后面需要补一下asi的ra和eur的ra了，amr的sa还没有跑出3个5的，还需要再等等看。

ra是提交了两个amr的ppa，给了51.34，这个算比较多的了，毕竟只提交了2个，之前都是4个或者3个，今天提交两个后，其实为了避免ppa的额度超了，本来也打算之后每天也就只提交1个或者2个，现在看来没什么问题。

再说下gla的回测情况，回测速度依旧很慢，依旧是不出货，我跑的事topdiv3000，明天看一下会不会出货，不出的话，先把universe换一下试试看，如果这周剩下的时间依旧不出的话，就暂时放弃glb了，先去跑跑asi和eur了。

另外我目前是直接回测二阶的alpha，发现有点问题，其实应该是先回测一阶，然后选取有信号的进行二阶回测，但是目前的框架，不是很方便的把一阶回测的取出来，回测框架后面还需要再优化一下，这个暂时是想放到下个月或者下个赛季了...最近都没有时间大改。

---

### 探讨 #75: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月14日

今日收益63.19美金，正常水平。

今日提交情况，2个ppa的amr，一个own的sa。

2个ppa的amr，收入和昨天基本相同，49.53美金，新出的ppa的规则是，小地区有限额的10个，只有当这个ppa不属于ra，也部署atom的时候，才会占用10的名额。

一个not own的sa，今天sa的prodcorr没有小于0.5，所以只给了13.66美金，正常水平了。

再说下glb的出货情况，topdiv3000依旧是一个没出，转战MINVOL1M了，如果再不出的话，就先放弃了，先去泡eur和usa了，asi先不跑了，asi最近好像要出新的theme了，等出了再跑asi。

感觉要稍微转变一下跑glb的策略了，先在其他区域跑某个数据集，如果出货了再去glb上跑，这样glb出货的概率可能会大些，不然glb跑的实在是太慢太难出货了。

---

### 探讨 #76: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月15日

今天收益只有40.62美金了，降低了很多，一度让我以为vf更新了...

今天提交情况，依旧是2个amr的ppa，一个sa。

ra一共给了30.8美金，并不是很多，提交的质量不是很高，但是今天点亮了2个amr的pyr，还是不错的。

sa提交的是一个not own的双8，但是prod>0.5的，只给了9美金，比较少了，昨天提交的own还不如今天提交的呢，都给了13美金，有点奇怪。

最近sa一直没有跑出prod小于0.5的，之前的存货也都交光了，后面sa很难再拿到高收益了。

最近想要重新优化一下回测框架，现在是只回测2阶段的，但是需要回测很多的alpha，这是一个大问题，后面要优化成，先跑一阶，然后选取好的再跑二阶段。

glb今晚看一下，如果还是不出货的话，就停了，改去跑eur了，赶在asi的them出来之前跑一些，然后再跑asi。

mcp最近又更新了，感觉已经跟不上了...好着急好着急。

---

### 探讨 #77: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月16日

今日收入48.64美金，处于正常水平。

今天提交了1个glb的比赛因子，2个amr的ppa，ra一共是给了27.96美金，是最近这段时间里最低的一次了，glb的因子pc是0.9，乘数是1.4，amr的与之前相同，看来pc的高的惩罚还是很高啊，而且混交的话好像确实会有影响。

sa提交的是一个not own的eur的pc0.61的，按照之前的算，一般会在9-12美金左右，但是今天给了20.68美金，实属震惊我了，不知道为什么会突然这么高，难道真是os很好吗？（这个就不可知了）

glb换了min后，出货还可以，既然提交了glb的alpha，那么就跑下去吧，尽量多交一点，不过这个月eur的ra估计就没时间交了，后面要去跑asi，不够eur交了不少sa，应该不会炸吧。

回测框架也再优化了，最后还是打算改成1阶回测，2阶优化，现在每批回测完后，将回调得到url保存下来，然后定时取给alpha打上name，然后二阶优化的时候，根据name来取出来，进入二阶，预计下周搞定。

明天有课，是将mcp的，期待一下，感觉mcp用好了的话，绝对是一大助力！

---

### 探讨 #78: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月17日

今日收入40.13美金，处于较低水平。

今天提交的是1个ra，一个sa。

ra是一个glb的比赛因子，给了3.84美金，质量一般，pc很高，pc达到了0.9，高pc的惩罚确实很严重，今天没有提交继续amr的因子。

sa提交的是一个not own的asi的，fitness>5，pc<0.5但是sharpe是4.89，给了36.29美金，看来想要拿高收益，sharpe和fitness都要>5才可以。

今天vf1.0的大佬又拿到了100美金+，羡慕了，祈祷自己的vf下次更新不会炸掉吧。

最近找到了一个好的筛选相关性的方法，还在处于实验阶段，希望能够有效。

mcp的课记错了，是下周，狠狠期待一下。

---

### 探讨 #79: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月19日

vf的更新结果出来了，0.96->0.92，这个变化其实是可以接受的，已经有预感vf会下降了....

今日收益83.47美金，ra收益54.15美金，sa收益29.32美金。

今天总的收益虽然很高，但是主要是因为ra拉上去的，只看sa的话，29是完全不够看的。

说下今天提交情况3个amr的ppa，都是高乘数、低pc，给了54.15，这个其实比较满足的，毕竟现在vf只有0.92了。还是那句话，乘数和pc对base影响比重非常大，交满的影响其实不是特别大。

sa的提交情况是一个not own的amr的35，但是只给了29,，这有点疑惑，因为昨天的sa是一个own的amr的35，却给了40+，不是昨天的太好了，就是今天的sa炸了...

再吐槽一下lab真难用啊，没有terminal，只能用notebook跑，但是关闭了Brian lab后，notebook就不跑了...

感觉严重影响进度了，已经卡了好几天了...

有没有大佬给我支点招啊。

---

### 探讨 #80: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026-01-21

今天挑挑拣拣交了一个ind的not own的sa，发现出了os后not own的sa后期的走向直接平了....之前表现很好的sa，现在都不敢交了，但是not own的sa却很少出现这个问题，难道是外面的ra质量真的太差了吗...

更新os后，之前的存货都没了，还要再重新回测一遍咯。

今天还交了一个比赛的glb 的alpha，表现一般，但是可以点塔也就交上去了。

==============================越努力，越幸运==============================

---

### 探讨 #81: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026/1/22

提交情况：

PPA：1个

区域：GLB

Sharpe1.11  Turnover  9.75%  Fitness  0.52  Returns  2.72%  Drawdown  4.74%  Margin  5.59‱

SA：1个

区域：ASI

Sharpe  4.15  Turnover  14.70%  Fitness  3.42  Returns  9.99%  Drawdown  1.59%  Margin  13.58‱

=====================================================================

成全我的不是生活，而是我自己的选择。 ---卡尔·荣格-

=====================================================================

---

### 探讨 #82: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

每日记录2026/01/26
提交情况:
[PPA,RA]: 1个
区域:[GLB]
Sharpe 1.17 Turnover 4.05% Fitness 0.68 Returns 4.26% Drawdown 8.22% Margin 21.02‱ 
[SA]: 1个
Sharpe 3.16 Turnover 12.40% Fitness 3.21 Returns 12.90% Drawdown 2.55% Margin 20.81‱ 
====================================
“成功的关键在于相信自己有成功的能力。”——拿破仑·希尔
====================================

---

### 探讨 #83: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

每日记录 2026/01/27
提交情况:
[PPA]: 1 个
区域:[GLB]
Sharpe 1.06 Turnover 5.03% Fitness 0.58 Returns 3.80% Drawdown 9.85% Margin 15.10‱
[SA]: 1 个
区域:[IND]
Sharpe 5.40 Turnover 14.98% Fitness 6.39 Returns 20.98% Drawdown 2.35% Margin 28.02‱
=====================================================================
“最困难之时，就是离成功不远之日。”—— 拿破仑
=====================================================================

---

### 探讨 #84: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

每日记录2026/01/28
提交情况:
[PPA]: 1个
区域:[GLB]
Sharpe 1.11 Turnover 31.90% Fitness 0.72 Returns 13.47% Drawdown 35.81% Margin 8.44‱ 
[SA]: 1个
区域:[IND]
Sharpe 3.15 Turnover 11.70% Fitness 3.06 Returns 11.76% Drawdown 2.71% Margin 20.10‱ 
=====================================================================
“人生在勤，不索何获。”——张衡
=====================================================================

---

### 探讨 #85: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

每日记录2026/01/29
提交情况:
[PPA,RA]: 0个
区域:[GLB,USA,EUR,IND]
Sharpe 无 Turnover 无 Fitness 无 Returns 无 Drawdown 无 Margin 无 
[SA]: 1个
区域:[IND]
Sharpe 6.39 Turnover 17.80% Fitness 8.21 Returns 29.38% Drawdown 2.69% Margin 33.01‱ 
=====================================================================
“志不强者智不达，言不信者行不果。”——墨子
=====================================================================

---

### 探讨 #86: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

每日记录2026/02/01
提交情况:
[PPA,RA]: 1个
区域:[GLB]
Sharpe 1.33 Turnover 17.93% Fitness 1.09 Returns 12.06% Drawdown 15.28% Margin 13.45‱ 
[SA]: 1个
区域:[IND]
Sharpe 7.15 Turnover 8.96% Fitness 13.16 Returns 42.33% Drawdown 3.51% Margin 94.45‱ 
=====================================================================
“卓越的人一大优点是：在不利与艰难的遭遇里百折不挠。”——贝多芬
=====================================================================

---

### 探讨 #87: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

每日记录2026/01/30
提交情况:
[PPA,RA]: 0个
区域:[GLB,USA,EUR,IND]
Sharpe 无 Turnover 无 Fitness 无 Returns 无 Drawdown 无 Margin 无 
[SA]: 1个
区域:[IND]
Sharpe 5.58 Turnover 11.74% Fitness 8.24 Returns 27.27% Drawdown 2.47% Margin 46.43‱ 
=====================================================================
“生活就像海洋，只有意志坚强的人，才能到达彼岸。”——马克思
=====================================================================

---

### 探讨 #88: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

每日记录2026/01/31
提交情况:
[PPA,RA]: 1个
区域:[IND]
Sharpe 1.87 Turnover 8.25% Fitness 1.64 Returns 9.59% Drawdown 6.47% Margin 23.26‱ 
[SA]: 1个
区域:[IND]
Sharpe 3.61 Turnover 14.38% Fitness 3.05 Returns 10.28% Drawdown 2.07% Margin 14.30‱ 
=====================================================================
“古之立大志者，不惟有超世之才，亦必有坚韧不拔之志。”——苏轼
=====================================================================

---

### 探讨 #89: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/04

量化日记竟然出第二季了，不得不说第一季的效果太好了，从日记中了解了很多大佬的工作，学到了太多东西了。

最近有点糟心，买的服务器一直因为磁盘IO超限从而宕机，好几天了，已经在想办法解决了，最近几天都没有提交ra，希望能尽快搞定服务器的事，太影响效率了。

sa的比赛开始，我是g2，simple真是天崩开局，大力出奇迹直接选了1000个，fitness直接干到13多了，分数也到了34w多，但是衰减特别明显，os爆炸。

不知道sa的比赛，对于我这种不同sa也没做过sa的小白来说，究竟是好事还是坏事，希望不要把vf搞炸了。

说下今天收益：

vf 0.88

sa 9.66$

---

### 探讨 #90: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/04

Super Alpha Competition 第二天，依旧g2 simple继续坐牢。

有几点疑惑：

1. simple 不是已经提纯后的主信号吗，按道理说已经排除了混信号、过拟合的等不好的alpha，但是看select出来的alpha的指标都比较差，且租出来的super alpha衰减也很厉害，尤其是最后两三年，感觉很明显的过拟合导致，不清楚是simple本身就是这样的还是我个人的select和combo有问题呢？

2. 现在有一个很害怕的地方，我之前没有提交过super alpha，且已知super alpha对value factory的影响比重较大，而且现在提交的simple组出来的alpha质量较差，会不会直接把value factory搞炸掉？

3. 基于第二点，对于g2组的人来说，是不是可直接放弃simple的super alpha，做剩下的5个类别，去和做6个类别的super alpha博弈，但是比赛提供的分数计算规则中没有找到最后计算分数的时候，每个类别对分数的影响，是等权还是求和？（但是我已经交了两个simple的super alpha了，已经停不下来了...）

隐约感觉super alpha competition是一个双刃剑了...

今日收益：

1sa  9.55$

---

### 探讨 #91: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/06

1. 终于把服务器因为数据量太多导致宕机的问题解决掉了，开始正常回测了。

2. 基本上每天都在手搓super alpha，质量一般且效率很低，在simple下基本上都是大力飞砖，select 数量直接拉满，后面还是要把super alpha的代码补充完善一下。

3. 优化了check脚本，使用直接调用官方的check方法，不需要传入description，check结果也会返回self corr、prod corr、ppac corr，只要regular和ppac满足一个提交就会返回success，然后将结果保存到数据库中，在根据具体的corr值进行筛选，如果都满足的话就可以一鱼两吃咯（不清楚一鱼两吃是否有严重后果影响）。

4. 借助xx课代表的自动提交代码，今天第一次实现了一鱼两吃，开心。

今日收入：

value factory：0.88

2 regular alpha：4.91$

1 super alpha：9.43$

---

### 探讨 #92: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/16

今天终于达成master了，alpha的数量和pyr都够了，后面还会更新一次comb，希望不要把我的master梦打碎了。

今日提交情况：

regular：eur - ram - ppa -> 7.34$

super：eur -> 9.24$

=======================================================================
一切幸福都并非没有烦恼，而一切逆境也绝非没有希望。 ---弗朗西斯·培根-
=======================================================================

---

### 探讨 #93: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/17

今天小红书有好几个人咨询wq兼职的事情，但是介绍之后就没有后续，不知道是话术的问题还是怎么回事，至今没有成功转化一个。

今日提交情况：

regular：eur - ram - ppa -> 6.81$

super：eur -> 9.08$

=======================================================================
保持渴望，保持同他人的联结，在平凡的日常中寻找自己感兴趣的事，留意别人忽视的东西。​​​ ---罗伯·沃克-
=======================================================================

---

### 探讨 #94: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/20

最近工作有点忙就没有交regular alpha，只交了一个super alpha。

今日提交情况：

super：asi -> 9.06$

=======================================================================

我现在正年轻，我愿意自己的青春在一种激荡的生活中度过；我愿意过一种充满创造乐趣、更为纯洁的生活。 ​​​ ---路遥-

=======================================================================

---

### 探讨 #95: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/22

今天没来得及交super alpha，只交了一个非theme的regular alpha。

我也有weight了，0.01，听老师说多交usa地区的alpha，weight增长才会比较快，但是usa地区的我交的真不多，且按照课代表的理论，你提交的因子，至少要有os后才会有可能被pm选择进入实盘，看了一下我的usa地区有os的alpha，寥寥几个，但质量好像都不错，os的fitness都可以2.多，这几个因子还是从alpha模板大师中魔改出来，看来前辈们的智慧还是非常有用的，后面也要多从模板中魔改一下，刚好最近想新增一个alpha模拟的数据库表，更方便了。

今日提交情况：

regular：asi -> 2.18$（非theme）

=======================================================================

我们的焦虑不是来自于对未来的思考，而是来自于想要控制它。 ---纪伯伦-

=======================================================================

---

### 探讨 #96: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025-10-13

量化日记第五季都来了，时间好快啊，来wq都1年了。

q3季度已经定级结束了，最后还是保住了master，这个赛季要争取一下gm，也想去gm的山顶看看风景，这个赛季要多点塔，将任务重心放到点塔上面，comb已经很长时间没有掉下2了，感觉保持正常的提交质量，comb应该不会有太大的波动了。

近期平台一直在引导用户一段时间着重做一个区域的alpha，甚至是某几个dataset、某几个

neutralization的alpha，最近也是一直跟着平台的方向走，出什么theme就去做什么theme，嘿嘿，虽然吃到theme了，但是base并没有太大的波动，应该是因为fitness和prodcorr不够的原因。

最近有个想法，目前一直都是在做region下最大的universe，是不是也应该做一下其他的universe呢，目前想到的方法和roubtstest差不多，将可以提交的alpha遍历一下universe，不够这样好像是存在过拟合的风险，所以目前是将接近满足提交条件的alpha更换universe后重新回测，然后再选取可以提交的，一定程度上可以降低过拟合的风险。

---

### 探讨 #97: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/23

惊到了，第八季日记才开1天，就已经480条评论了。

说下近期情况吧，近期都是每天只提交一个sa，ra很少提交了，上周不小心收到了pc的警告邮件，这周就只交了1个ra。最近在跑ind，开了maxtrade真的好难出货哇，不开又担心质量不好，难搞哦。

没想到这次比赛的daliy竟然是日更的，看起来想每日的盈亏了，降低的回测算力都扔这上面了。

昨天晚上刚完成了分数的分配，今天还没有更新出分数，等等明天吧，希望明天可以更新出分数。

============================================================

---

### 探讨 #98: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/24

放弃ind了，重新回到glb，争取年前多交点glb的alpha。

今天提交了一个sa+一个ra，sa是eur的，sa的bug终于修复了，ra交的事glb的。

今晚有gem的会，积极参与！！！！！！！！！！！

============================================================

每个故事必须按照自己的方式、自己的时间节奏缓缓展开。 ---谢丽尔·桑德伯格-

============================================================

---

### 探讨 #99: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 减少无效回测经验分享.md
- **评论时间**: 7个月前

不错的分享，在进行回测之前对数据进行清理，这是一个非常正常的方向，感觉可以进行共建，制定一个共同认可的规则“何为无效数据”、“何为低/中/高质量数据”，将数据集分给不同的顾问进行回测，（当然不同genius等级的顾问可能会有不同的数据权限等其他问题，如果可以的话这些可以再详细讨论一下）然后共建出一个通用的数据集信息。

---

### 探讨 #100: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 减少无效回测经验分享_36248601073175.md
- **评论时间**: 7个月前

不错的分享，在进行回测之前对数据进行清理，这是一个非常正常的方向，感觉可以进行共建，制定一个共同认可的规则“何为无效数据”、“何为低/中/高质量数据”，将数据集分给不同的顾问进行回测，（当然不同genius等级的顾问可能会有不同的数据权限等其他问题，如果可以的话这些可以再详细讨论一下）然后共建出一个通用的数据集信息。

---

### 探讨 #101: 关于《登录系统s = login()获取数据字段df = get_datafields(s, dataset_id='analyst4', region='USA', universe='TOP3000', delay=1)数据预处理pc_fields = process_datafields(df)》的评论回复
- **帖子链接**: [Commented] 多阶任务拆分与MySQL管理经验分享代码优化.md
- **评论时间**: 1年前

大佬这套流程下来每天的回测量在多少左右呢？

我也曾想过将一阶二阶的表达式存入数据库中，然后回测的时候从数据库中取出来，但是从数据库中取数这一过程随着数据量的增加，时间也会变长。看您上面的代码里的流程中从数据库中取出表达式后，回测完成后会再更新这一批数据，这里又增加了时间的损耗，个人感觉效率上会有所影响。可以分享下每天的回测量嘛。

---

### 探讨 #102: 关于《登录系统s = login()获取数据字段df = get_datafields(s, dataset_id='analyst4', region='USA', universe='TOP3000', delay=1)数据预处理pc_fields = process_datafields(df)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 多阶任务拆分与MySQL管理经验分享代码优化_32603028529175.md
- **评论时间**: 1年前

大佬这套流程下来每天的回测量在多少左右呢？

我也曾想过将一阶二阶的表达式存入数据库中，然后回测的时候从数据库中取出来，但是从数据库中取数这一过程随着数据量的增加，时间也会变长。看您上面的代码里的流程中从数据库中取出表达式后，回测完成后会再更新这一批数据，这里又增加了时间的损耗，个人感觉效率上会有所影响。可以分享下每天的回测量嘛。

---

### 探讨 #103: 关于《如何在云服务器上24小时运行代码》的评论回复
- **帖子链接**: [Commented] 如何在云服务器上24小时运行代码.md
- **评论时间**: 1年前

你好，我在使用zellij的时候，有些快捷键跟vscode快捷键冲突了，请问你是怎么解决的。

---

### 探讨 #104: 关于《如何在云服务器上24小时运行代码》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何在云服务器上24小时运行代码_29031525682199.md
- **评论时间**: 1年前

你好，我在使用zellij的时候，有些快捷键跟vscode快捷键冲突了，请问你是怎么解决的。

---

### 探讨 #105: 关于《我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化》的评论回复
- **帖子链接**: [Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化.md
- **评论时间**: 1年前

非常好的分享，从ai生成的alpha表达式来看，看起来是非常符合wq平台的规则。我之前也有通过将operate、fields和一些文章喂给ai，然后向其询问alpha模板，但是发现ai给出的模板绝大多数都是动量方向的模板，且有些时候使用的表达式也不知wq平台上存在的。不知道大佬有没有遇到过这些问题呢。

同时想问一句，这个是私人的嘛。

==========================================

山教会我，所有的选择都是相连的。海教会我，所有的命运都是起伏的。​ ​​​ ---库索-

==========================================

---

### 探讨 #106: 关于《我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化_33016862088599.md
- **评论时间**: 1年前

非常好的分享，从ai生成的alpha表达式来看，看起来是非常符合wq平台的规则。我之前也有通过将operate、fields和一些文章喂给ai，然后向其询问alpha模板，但是发现ai给出的模板绝大多数都是动量方向的模板，且有些时候使用的表达式也不知wq平台上存在的。不知道大佬有没有遇到过这些问题呢。

同时想问一句，这个是私人的嘛。

==========================================

山教会我，所有的选择都是相连的。海教会我，所有的命运都是起伏的。​ ​​​ ---库索-

==========================================

---

### 探讨 #107: 关于《求教，这个alpha还能救一下么》的评论回复
- **帖子链接**: [Commented] 求教这个alpha还能救一下么.md
- **评论时间**: 1年前

差的有点太多了，差的少的话，我记得论坛里有帖子说可以优化一下，可以在搜索栏里搜搜看。

---

### 探讨 #108: 关于《求教，这个alpha还能救一下么》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 求教这个alpha还能救一下么_31017228094615.md
- **评论时间**: 1年前

差的有点太多了，差的少的话，我记得论坛里有帖子说可以优化一下，可以在搜索栏里搜搜看。

---

### 探讨 #109: 关于《组super alpha时所有可用的属性经验分享》的评论回复
- **帖子链接**: [Commented] 组super alpha时所有可用的属性经验分享.md
- **评论时间**: 10个月前

theme这个还真没有用过，大佬可以说下theme这个可以怎么使用吗，有什么值吗。

---

### 探讨 #110: 关于《组super alpha时所有可用的属性经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 组super alpha时所有可用的属性经验分享_34178199290135.md
- **评论时间**: 10个月前

theme这个还真没有用过，大佬可以说下theme这个可以怎么使用吗，有什么值吗。

---

### 探讨 #111: 关于《经验分享｜PPAC全球第三名，回馈社区经验分享》的评论回复
- **帖子链接**: [Commented] 经验分享PPAC全球第三名回馈社区经验分享.md
- **评论时间**: 1年前

全是干货，收获颇多，看来alpha的多样性、低相关性无论是在比赛中还是日常的提高value factory中都起着至关重要的作用。

期待大佬value factory更新后直达 1.0 !!!!

---

### 探讨 #112: 关于《经验分享｜PPAC全球第三名，回馈社区经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **评论时间**: 1年前

全是干货，收获颇多，看来alpha的多样性、低相关性无论是在比赛中还是日常的提高value factory中都起着至关重要的作用。

期待大佬value factory更新后直达 1.0 !!!!

---
