# 顾问 MQ62208 (Rank 29) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 MQ62208 (Rank 29) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

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

### 帖子 #2: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
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

### 帖子 #3: Maximizing Combined Alpha Performance: Key Strategies and Insights
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

### 帖子 #4: 【alpha灵感】A股恐慌度因子在美股的应用
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

### 帖子 #5: 【Alpha灵感】凸显理论（Salience Theory）
- **主帖链接**: [L2] 【Alpha灵感】凸显理论Salience Theory.md
- **讨论数**: 4

研报题目：1. 行为金融新视角——“凸显性收益”因子 STR（招商证券， 2022年12月14日）2. 凸显理论之 A 股“价”“量”应用（广发证券，2023年3月23日）研报简介：传统的资产定价模型通常假设投资者完全理性并且能够利用市场上所有的可得信 息， 但在实际投资中， 大多数投资者对资产进行定价时往往会受隐形的“心理权 重”影响。因此，基于凸显理论（Salience Theory）对投资者进行投资决策时的心理权重进行了定量描绘，构建了“凸显性收益”因子 STR，当 STR 为显著正时，投资者往往过度关注股票的上涨潜力，从而成为风险寻求者；当投资者过分关注股票的负收益并强调其下行风险时， STR 显著为负，相关的股票可能面临低估。第二篇中结合了A股市场的涨跌幅限制和高换手率等市场特征，构建凸显因子。核心交易idea：根据凸显理论构建STR，通过排序做多STR低的股票，做空STR高的股票执行策略。1. 计算股票日收益率的凸显性系数sigma2. 根据sigma计算凸显性权重weight3. 计算STR因子感兴趣的话，具体公式可以参考第一篇研报的公式（4-6）数据字段：returns, volume, sharesoutSimulation设置：Alpha表达式和表现：1. 原始STR表现（Pnl, IS Summary)可以看到时有信号的，同时prod corr较高， 所以还要改进。2. 根据第二篇研报，引入换手率3. 用与换手率之间的协方差替换与日收益率之间的关系：4.引入涨跌幅限制：总结与反思：1. 总的来说，凸显理论用的数据字段和操作符比较简单，但是可以看到还是比较有效的，搜了一下Brain平台少有涉及这一理论的，所以还是值得分享一下。2. 这个方法主要是做月度调仓，想问问大家怎么能够实现，看到keep这个操作符，但是没有想到如何实操。3. 这个思路想法简单，做法也容易实现，这可能是prod corr较高的原因之一，对于减少这个方法的prod corr试了一些方法，由于没有更多的知识，效果都不太好有点可惜，希望大家如果能够继续在这个方向上能提交alpha，可以评论区留言告知，我也希望学习到多一些的经验。

---

### 帖子 #6: 【Alpha灵感】凸显理论（Salience Theory）
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】凸显理论Salience Theory_20262909489431.md
- **讨论数**: 4

- **研报题目** ：
  1. 行为金融新视角——“凸显性收益”因子 STR（招商证券， 2022年12月14日）
  2. 凸显理论之 A 股“价”“量”应用（广发证券，2023年3月23日）
- **研报简介** ：
  传统的资产定价模型通常假设投资者完全理性并且能够利用市场上所有的可得信 息， 但在实际投资中， 大多数投资者对资产进行定价时往往会受隐形的“心理权 重”影响。因此，基于凸显理论（Salience Theory）对投资者进行投资决策时的心理权重进行了定量描绘，构建了“凸显性收益”因子 STR，当 STR 为显著正时，投资者往往过度关注股票的上涨潜力，从而成为风险寻求者；当投资者过分关注股票的负收益并强调其下行风险时， STR 显著为负，相关的股票可能面临低估。第二篇中结合了A股市场的涨跌幅限制和高换手率等市场特征，构建凸显因子。
- **核心交易idea** ：根据凸显理论构建STR，通过排序做多STR低的股票，做空STR高的股票执行策略。
  1. 计算股票日收益率的凸显性系数sigma
  2. 根据sigma计算凸显性权重weight
  3. 计算STR因子
  感兴趣的话，具体公式可以参考第一篇研报的公式（4-6）
- **数据字段** ：returns, volume, sharesout
- **Simulation设置** ：
  
> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> CHN
> TOP3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 5
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> On
> Verify
> Off
> SaVe as Default
> Apply

- Alpha表达式和表现：
  1. 原始STR
  
> [!NOTE] [图片 OCR 识别内容]
> Jelta
> 0.7;
> theta
> 0.1;
> market_return
> group_median
> Teturns
> market)
> sigma
> ab5
> Teturns
> market_return)
> (ab5
> returns 1
> abs (market_return
> theta 1
> Jays
> 22;
> k = ts_rank (-sigma;
> days I+days;
> K_l = iT_else (k==0
> 1, kI;
> weight
> power (delta,
> tS_rank (k_l
> Jays) )
> ts_meanl power (delta,
> ts_rank (k_I,  Jays/
> days)
> STR
> covariance Iweight ,
> returns
> days) ;
> qroup_neutralize (ZSCore (-STR)
> bucket ( rank (capI ,
> range='0,
> 1, 0.1')
 表现（Pnl, IS Summary)
  
> [!NOTE] [图片 OCR 识别内容]
> 161
> 15I
> 41
> 131
> 12N
> 1OI
> ODOK
> OODK
> ODOK
> ODOK
> ODOK
> ODOK
> OODK
> ODOK
> ODOK
> OOOK
> Jul'11
> Jan '12
> Jul '12
> Jan '13
> Jul'13
> Jan '14
> Jul '14
> Jan '15
> Jul'15
> Jan '15
> Ju1'16
> Jan'17
> Jul'17
> Jan 18
> Jul'18
> Jan '19
> Jul'19
> Jul 20
> Jan 21
> IS Summary
> Period
> Aggregate Data
> Snarpe
> TUrnOVer
> FItness
> ReUrns
> CTIIIO
> Marain
> 2.04
> 15.87%
> 2.09
> 16.68%
> 19.78%
> 21.01%oo
> URN  N
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> STJTOL
> VUTIOUE |
> LICTIES '
> RETUIRS
> UTJIOTITI
> Nariln
> 2.04
> 15.87%
> 2.09
> 16.68%
> 19.78%
> 21.01%o。
> Year
> Sharpe
> Turnover
> Htness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2011
> 2.15
> 16.039
> 705
> 14.70%
> 3.52%
> 18.2554
> 1113
> 1035
> 2012
> 4.15
> 15.5295
> 542
> 25.45%
> 2.99%
> 34.09532
> 1200
> 1094
> 2013
> 2.37
> 15.459
> 2.55
> 19.46%
> 4.52%
> 25.1954
> 1273
> 1103
> 201
> 3.46
> 15.2795
> 4.25
> 23.02%
> 3.41%
> 30.155
> 1277
> 1103
> 2015
> 0.22
> 16.3395
> 003
> 2.47%
> 19.78%
> 3.01533
> 1245
> 1133
> 201
> 3.33
> 15.349
> 21.94%
> 3.14%
> 27.7053
> 1405
> 1251
> 2017
> 2.54
> 15.559
> 7.37
> 20.04]
> 4.27%
> 25.5954
> 1575
> 1401
> 2013
> 3.22
> 16.2595
> 3.83
> 23.74%
> 2.24%
> 29.2252
> 565
> 1434
> 2019
> 3.42
> 16.209
> 4.20
> 24.45]
> 3.14%
> 30.1355
> 1615
> 1334
> 2020
> 1.24
> 16.0795
> 1.14
> 13.68%
> 15.31%
> 17.02533
> 1633
> 1372
> 2021
> 1.07
> 16.3395
> 1.03
> 15.22%
> 3.17%
> 18.57535
> 1601
> 1417
> 医 Correlation
> Self Correlation
> HBhest Correlatlon
> LaSt RJn
> Prod Correlation
> HlBhest Correlation
> LasC RUn: Tue
> 01/0212024.11.47 PM
> Lonq
 可以看到时有信号的，同时prod corr较高， 所以还要改进。
  2. 根据第二篇研报， **引入换手率
  
> [!NOTE] [图片 OCR 识别内容]
> Jelta
> 0.7;
> theta
> 0.1;
> market_return
> 9roup
> median ( returns
> TaTket;
> 5iqma
> ab5 (returns
> market_return)
> (abs (returns)
> ab5 (market_return !
> thetal
> turnover
> Lume
> SharesoUt;
> market
> turnover
> qroup
> mean ( turnover;
> market)
> sigma
> abs (turnover
> market_turnover
> 1ab5
> tUrnoverI
> abs (market
> turnover
> theta1
> Jays
> 22;
> ts_rank (-sigma,
> days / +days;
> k_1 = if_else(k==0
> 儿;
> weight
> powerldelta,
> ts_rank (k_1,
> days 1
> Mean ( power
> delta,
> rank (k_1i  Jays/'
> Jays
> STT
> Covariance (weight
> returns
> days ;
> group_neutralize
> ZSCOre |-STTI ,
> bucket ( rank (capl ,
> range=
> 1, 0.1'1
**  
> [!NOTE] [图片 OCR 识别内容]
> 1ONI
> 9 OOOK
> ODOK
> ODOK
> ODOK
> 5OOOK
> ODOK
> 3ODOK
> ODOK
> ODOK
> Jul'11
> Jan '12
> Jul'12
> Jan '13
> Jul '13
> Jan '14
> JU1'14
> Jan '15
> Jul'15
> Jan '16
> Jan'17
> 117
> Jan 18
> Jul'18
> Jan '19
> Jul 19
> Jul'20
> Jan
> IS Summary
> Period
> Aggregate Data
> Sharpe
> TUTNTIe
> FItness
> Returns
> Drwdown
> Margln
> 1.91
> 14.46%
> 1.74
> 11.97%
> 15.80%
> 16.56900
> JJUI
> JJUl
 3. 用 **与换手率之间的协方差** 替换与日收益率之间的关系：
  
> [!NOTE] [图片 OCR 识别内容]
> delta
> 0.7;
> theta
> 0.1;
> market
> return
> 9roup_median (returns, market);
> 5igma
> abs ( returns
> market_return)
> (abs (returns)
> abs (market
> returnl
> thetal ;
> turnover
> Volume/ sharesout;
> market_turnover
> qroup_mean ( turnover,
> market);
> abs ( turnover
> narket
> turnover
> (abs (turnover
> abs (market_turnover )
> thetal ;
> 22;
> ts_rank(-5igma, days /*days;
> K_l = iT_else (k==0
> 1, kl
> weight
> power (delta,
> ts_rank (k_I, Jays/)
> tS_mean
> power (delta,
> ts_rank (k_I
> Jays) )
> days
> # STT
> ts_covariance (weight ,
> returns
> days) ;
> STTZ
> ts_Covariance (weight,
> turnover Jays);
> 9roup_neutralize ( ZSCore (-STTZI ,
> bucket ( rank (cap)
> range='0,
> 0.1') 1
> sigma
> days

  
> [!NOTE] [图片 OCR 识别内容]
> 22N
> ZON
> 8M
> 16N
> 4 |
> 121|
> 1ONI
> ODOK
> OODK
> OODK
> OODK
> Jul'11
> Jan '12
> Jul'12
> Jan '13
> Jul'13
> Jan '14
> Jul '14
> Jan '15
> Jul'15
> Jan '15
> JuI'16
> Jan'17
> Jul'17
> Jan'18
> Jul'18
> Jan '19
> Jul 20
> Jan
> IS Summary
> Period
> Aggregate Data
> Snarpe
> TUrnOVer
> TITICSc
> ReUrns
> CTIIIO
> Marain
> 2.92
> 10.83%
> 4.13
> 24.99%
> 16.14%
> 46.179o0
> J4119
 4.  **引入涨跌幅限制** ：
  
> [!NOTE] [图片 OCR 识别内容]
> delta
> 0.7;
> theta
> 0.1;
> turnover
> V0lume
> Sharesout;
> market
> turnover
> group_mean (turnover;
> market;
> 5iqma
> abs (turnover
> market
> turnover
> (abs (turnover)
> ab5 (market
> turnover
> theta)
> Sigma
> if_elselabs
> returns
> >0.1,
> 305
> returns 1+1000,
> turnover ;
> Jays
> 22;
> ts_rank (-sigma,
> Jays 1+day5 ;
> K_l = ir_else (k==0
> 1, ki;
> weight
> power(delta,
> ts_rank (k_1,
> Jays/
> mean (power
> delta,
> ts_rank (k_1,
> day5 /
> Jays
> STV
> Covariance (weight;
> returns
> days ;
> group_neutralize (ZsCore(-STV)
> bucket ( rank ( capI
> range='0,
> 1,0.1'1
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Snarpe
> TITMIIPI
> FItRess
> Returns
> Drloown
> Wargln
> -0.43
> 15.88%
> -0.16
> -2.18%
> 54.97%
> -2.74900
> Year
> Sharpe
> TurnOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.25
> 16.1595
> 11.50%
> 2.53%
> 14.24532
> 1105
> 1045
> 2012
> 15.919
> 5.53%
> 4.22%
> 2053
> 1153
> 1133
> 2013
> 205
> 16.2795
> 9.09%
> 1.72%
> 11.17533
> ZO0
> 1131
> 2014
> 1.70
> 15.7395
> 1.14
> 7.03%
> 2.75%
> 9453
> 1213
> 1170
> 2015
> 16.029
> 5.37
> 23.00%
> 30.59%
> 34.9455
> 1170
> 1253
> 2015
> 0.25
> 15.5395
> 0.99%
> 03%
> 2720
> 1375
> 1293
> 2017
> 15.3095
> 1.53
> 10.75%
> 3.52%
> 14.04532
> 552
> 1423
> 2013
> 15.589
> 0.31
> +38%
> 7.53%
> 4.3150
> 1501
> 1503
> 2019
> 3.49
> 16.0095
> 3.42
> 15.33%
> 15.38%
> 19.1752
> 501
> 1502
> 2020
> 16.179
> 17.12%
> 15.91%
> 21.1855
> 1481
> 1530
> 2021
> 15.539
> 0.21
> 3.28%
> 1.47%
> 1855
> 1534
> 1490
> Correlation
> Self Correlation
> NlBhest Correlatlon
> LaSt RUn
> Prod Correlation
> HBhest Correlatlon
> Last Run: Wed, 0110312024,12.07 ANI
> 0.6


- ****总结与反思：**** 1. 总的来说，凸显理论用的数据字段和操作符比较简单，但是可以看到还是比较有效的，搜了一下Brain平台少有涉及这一理论的，所以还是值得分享一下。
  2. 这个方法主要是做月度调仓，想问问大家怎么能够实现，看到keep这个操作符，但是没有想到如何实操。
  3. 这个思路想法简单，做法也容易实现，这可能是prod corr较高的原因之一，对于减少这个方法的prod corr试了一些方法，由于没有更多的知识，效果都不太好有点可惜，希望大家如果能够继续在这个方向上能提交alpha，可以评论区留言告知，我也希望学习到多一些的经验。

---

### 帖子 #7: 【YZ工程优化系列】YZ72256-使用API自动完成submit
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

### 帖子 #8: print('retrying in', result.headers["retry-after"], 'seconds')
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

### 帖子 #9: 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回
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

### 帖子 #10: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
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

### 帖子 #11: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享
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
> 顾问 MG88592 (Rank 38)
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

### 帖子 #12: 使用[ClickHouse📕]建设你的大型数据库
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

### 帖子 #13: 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法
- **主帖链接**: 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法.md
- **讨论数**: 8

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

### 帖子 #14: 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法
- **主帖链接**: https://support.worldquantbrain.com【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法_35799099514647.md
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


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《[经验分享踩过的坑] 优化筛选alpha的方法》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [经验分享踩过的坑] 优化筛选alpha的方法_28230705623575.md
- **评论时间**: 1年前

这是check alphas接口还是提交 alphas 的接口？

---

### 探讨 #2: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md
- **评论时间**: 1 year ago

华子哥写的这个插件确实牛逼，响应那句科技造福于人类。使用真的很方便，直接能看到自己目前的等级。希望华哥后续还能整出其他方便快捷的小插件。这是位前端大佬，膜拜大佬，感谢大佬。

---

### 探讨 #3: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

量化学习日记

由于value factor 太低导致每天只有一美元，痛定思痛总结了下，

提高value factor 实用技巧：

1. Focus on Low Correlation 专注于低相关性
2. Create Single-Dataset Alphas 创建单数据集 Alpha
3. Turnover and Sharpe Improvements 降低换手率和夏普改进
4. Explore New Datasets 探索新数据集
5. Avoid Overfitting 避免过拟合

---

### 探讨 #4: 关于《完成当前池后，保存进度》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 基于三阶模板的一些优化_28293182637463.md
- **评论时间**: 1年前

感谢博主分享

---
