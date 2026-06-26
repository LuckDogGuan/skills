# 顾问 LD22811 (Rank 39) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 LD22811 (Rank 39) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: PPA活动主题限制下，提交ra点塔的一点心得。
- **主帖链接**: PPA活动主题限制下提交ra点塔的一点心得.md
- **讨论数**: 15

新季度没多久就开始实行ppa主题活动了，只能在活动区域提交ppa。1月份我做了两个地区的alpha，usa d1和ind，usa在活动之前点了几个塔，活动开始之后又坚持了几天交ra觉得有点累就去了ind活动，活动前期没有在意atom，等我意识到这个问题之后已经交了30个pv塔，所以在活动结束之后我坚持补了20个atom-ra，然后又回usa点亮了剩下的塔，没有去参加GLB活动。两个区应该是一共点了24个塔，100个alpha左右。参加活动的ppa也都满足ra标准，只是有些豁免了pc提交。这里面应该有超过一半的alpha是经过我手动优化的。脚本或者ai想直接跑出各项属性都让人满意的alpha还是很少的，更别说全要满足ra标准了。主要优化的思路是修正fail和wraing，比如流动性不足用group_neutralize、切换股票池。权重问题调整回填日期，增加交易条件，或者也可以切换股票池，sharpe、fitness值不足使用signed_power操作符。tvr和margin不合格时调整decay，或者使用ts_target_tvr_decay 、ts_decay_linear尝试调整。PC大于0.7时候可以尝试开启max-trade切换股票池，调整decay，调整ts的时间窗口，分组中性等多种方法，调整结果需要一点运气，一般来说alpha足够好有降低性能的空间而pc值没有特别高的时候都能降低到0.7以下。

---

### 帖子 #2: PPA活动主题限制下，提交ra点塔的一点心得。
- **主帖链接**: https://support.worldquantbrain.comPPA活动主题限制下提交ra点塔的一点心得_38121310515223.md
- **讨论数**: 15

新季度没多久就开始实行ppa主题活动了，只能在活动区域提交ppa。1月份我做了两个地区的alpha，usa d1和ind，usa在活动之前点了几个塔，活动开始之后又坚持了几天交ra觉得有点累就去了ind活动，活动前期没有在意atom，等我意识到这个问题之后已经交了30个pv塔，所以在活动结束之后我坚持补了20个atom-ra，然后又回usa点亮了剩下的塔，没有去参加GLB活动。 
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2026-01,January 1st. 2026
> March 31st, 2026
> Category
> USA
> GlB
> EUR
> ASI
> CHN
> KOR
> TN
> INO
> Analys:
> Broker
> Earnings
> Fundamental
> Imbalanze
> Insizlers
> Institions
> Nlacro
> MadEl
> NEws
> 03i3n
> C-her
> Price VlUME
> Risk
> SEntiMEMT
> Shait In-erEs
> Social Media
 两个区应该是一共点了24个塔，100个alpha左右。参加活动的ppa也都满足ra标准，只是有些豁免了pc提交。这里面应该有超过一半的alpha是经过我手动优化的。脚本或者ai想直接跑出各项属性都让人满意的alpha还是很少的，更别说全要满足ra标准了。

主要优化的思路是修正fail和wraing，比如流动性不足用group_neutralize、切换股票池。权重问题调整回填日期，增加交易条件，或者也可以切换股票池，sharpe、fitness值不足使用signed_power操作符。

tvr和margin不合格时调整decay，或者使用ts_target_tvr_decay 、ts_decay_linear尝试调整。

PC大于0.7时候可以尝试开启max-trade切换股票池，调整decay，调整ts的时间窗口，分组中性等多种方法，调整结果需要一点运气，一般来说alpha足够好有降低性能的空间而pc值没有特别高的时候都能降低到0.7以下。

---

### 帖子 #3: How to Improve After Cost Performance置顶的
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

### 帖子 #4: How to Improve After Cost Performance置顶的
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

### 帖子 #5: Machine Alpha 基础知识1：什么是Alpha模板
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

### 帖子 #6: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #7: WEIGHT CONCENTRATION ERROR? QUICK OPERATOR FIXES
- **主帖链接**: https://support.worldquantbrain.com[L2] WEIGHT CONCENTRATION ERROR QUICK OPERATOR FIXES_36663845173911.md
- **讨论数**: 53

***“Weight is too strongly concentrated or too few instruments are assigned weight.”***

Interpretation:
Your alpha assigns extreme, unstable, or overly selective values thus weight piles into a small subset of stocks.

Below is a suggestion of  **operators** that
push the operators towards stability,wider coverage and broader value distributions thus reducing over-concentration and even turnover in the process:

🔰 ***ts_backfill(x,d,k=1)*** 
 *Function* :
Replaces missing or recent invalid values (NaNs) with older valid values.

*How it reduces concentration:*

When an alpha has NaNs on many stocks,those stocks receive zero weights.The few remaining stocks take all the weight thus the weight concentration warning/fail.
 This operator thus prevents NaNs from zeroing out or dropping instruments, which would concentrate weight on fewer stocks.

🔰 ***kth_element(x, d, k=1)***

*Function* :
Retrieves the k-th valid historical value of x from the past d days (ignoring NaNs or ignored values).
Kinda similar as a backfill operator

*How it reduces concentration:* 
Same effect as backfill but more targeted—ensures more instruments have stable values, reducing missing/volatile entries that cause weight piling.

🔰 ***days_from_last_change(x)*** 
 *Function* :
Counts how many days have elapsed since the last change in value of x.

*How it reduces concentration:*

Frequent changes causes constant turnover/ frequent alpha oscillations therefore weight jumps to a few names

This operators thus helps hold positions longer and prevents frequent position flipping into a small subset of names

🔰 ***last_diff_value(x, d)*** 
 *Function* :
Returns the last non-zero difference over d days.

*How it reduces concentration:* 
Useful for detecting true changes vs noise. Helps suppress tiny noisy signals that create spikes which concentrates weight on a small number of stocks.

🔰 ***truncate(x, maxPercent = 0.5)*** 
 *Function* :
Limits the proportion of stocks that can take extreme values.

*How it reduces concentration:* 
Directly prevents the alpha from giving outsized signals to only a few stocks → ensures more uniform cross-sectional weight.

🔰 ***ts_weighted_delay(x, k)*** 
 *Function* :
Blends today's value with yesterday’s using weight k:

Where k close to:

1 → behaves like identity

0 → behaves like delay (yesterday's value)

*How it reduces concentration:* 
Smoothes spikes by preventing extreme day-to-day jumps that cause weights to pile onto a few names
It makes weights drift gradually therefore reducing both turnover and concentration.

🔰 ***ts_decay_exp_window(x, d, factor)*** 
 *Function* :
Computes an exponentially weighted average of the past d days:

*How it reduces concentration*

Smooths noisy inputs (returns, spreads, microstructure features) thus extreme values are averaged out.This generates fewer drastic cross-sectional outliers therefore less concentrated weights
It creates slow-moving, stable alphas, which naturally distribute weight more evenly.

🔰 ***clamp(x, lower, upper)*** 
 *Function* :
Limits values between lower and upper bounds:

if x > upper: x = upper
if x < lower: x = lower

*How  it reduces concentration*

Hard-caps extreme values hence no instruments have explosive alpha scores
This makes cross-sectional weights naturally flatter
It is one of the strongest tools to avoid concentration warnings.

🔰 ***left_tail and right_tail*** 
 *Function* :
left_tail(x, maximum) → NaN or truncate values above max

right_tail(x, minimum) → NaN or truncate values below min

*How they reduce concentration*

These operators remove or neutralize extreme tail values.
Without them, outliers dominate the rank thus high concentration.
By cutting tails, your alpha gives more balanced signals across the universe.

🔰 ***group_normalize(x, group)*** 
 *Function* :
Normalizes alpha within each group (industry, sector, volatility bucket etc):

x_group = x - mean(x in group)
scale if needed

*How it reduces concentration*

Prevents:

↔entire industries from getting overweighted

↔structural biases (e.g., value-heavy sectors dominating)

It therefore creates a more diversified weight distribution across sectors.

🔰 ***keep(x, f,period)*** 
 *Function* :
Hold x for a set number of days after f stops changing.

if f changes: reset counter  
if counter < period: use x  
else: output NaN

*How it reduces concentration*

It forces persistence in alpha signals thus avoids daily reactive swings
This creates a smoother cross-sectional behavior  that leads to fewer outliers
You  therefore get stable, low-turnover alpha with broad participation.

🔰 ***trade_when(x, y, z)*** 
 *Function* :
Update alpha only when x triggers, exit on z, else hold previous value:

if exit condition: alpha = NaN  
elif trade condition: alpha = y  
else: alpha = previous value

*How it reduces concentration*

By holding previous alpha when signal is weak:weight stays spread and no rapid swing into a small group of instruments.
Turnover also drops sharply.
Trade_when strongly stabilizes your alpha.

These are just some of the operators with detailed explanations of how they reduce weight concentration in alphas.
Hope you will implement them in your alpha research.
If you found this helpful,be sure to leave a  **LIKE** , **FOLLOW** the conversation and leave your  **SUGGESTION** and  **FEEDBACK** in the comments below  so that others can draw inspiration from you!.
 ***CIAO*** ✌

---

### 帖子 #8: PnL = ∑(Robustness * Creativity)
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

### 帖子 #9: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 959

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #10: 【日常生活贴】我的量化日记第三季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **讨论数**: 742

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #11: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #12: 【日常生活贴】我的量化日记第二季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **讨论数**: 930

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #13: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 660

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #14: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #15: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #16: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第十季.md
- **讨论数**: 583

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第九季.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #17: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 1018

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #18: 零基础考研失败应届生的一点经验经验分享
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

### 帖子 #19: 二季度了2个月，和大家分享一些alpha挖掘的思路经验分享
- **主帖链接**: 二季度了2个月和大家分享一些alpha挖掘的思路经验分享.md
- **讨论数**: 18

2026 年第二赛季已进入收官倒计时，相信大家都在为最后的点塔和赛季排名做最后冲刺。这赛季我在多个地区实战验证，踩过坑也总结出了一套可复制的 alpha 挖掘和点塔方法。今天严格按照自己的工作流，经验分享出来，希望能帮到大家，也欢迎在评论区交流指正。1. 根据华子哥插件和网页的提交数据初步判断优质的数据集和字段先筛数据再干活，是所有工作的前提。每天早上我会花 30 分钟做数据勘探，绝不盲目写代码。华子哥插件优先找绿色数据集这是华子哥通过GM权限通过SA筛选ra收集到的数据判断出的优质ALPHA比例高的数据集，其次看适合的中性化配合网页端提交数据看全局：1.寻找提交较多的数据集/字段，你大概率也可以在这个数据集里找出可提交的alpha；2.寻找新的宇宙/数据集，这里的alpha相关性较低，竞争少。2. AI 帮助生成初始信号AI 是最高效的初始信号生成器，能帮我们快速扩大信号池。我的使用流程非常明确：确定优质数据集后，给 AI 输入标准化 prompt：明确要求生成0 阶信号，仅使用基础变换（rank、ts_rank、delta、log 等）指定地区、数据集和核心字段范围要求 AI 为每个信号附上一句话经济逻辑解释要求输出平台支持的标准语法，可直接复制运行关键原则：AI 生成的信号 90% 都是垃圾，我们只需要从中筛选出 3-5 个有逻辑、回测基础表现不错的信号，作为后续优化的起点。不要迷信 AI 给出的高夏普，大概率是过拟合。3. 纯粹的 0 阶模板寻找优质字段信号很多人看不起 0 阶模板，但真正能长期稳定的 alpha，80% 都源于 0 阶信号。我常用的0阶段模板：最原始的字段回填\去极值；字段ts_rank；字段AB除法运算；字段AB减法运算。我的标准操作：对每个新数据集，先跑一遍所有字段的纯 0 阶信号筛选出夏普 > 0.8、fit>0.5的字段，建立自己的 "种子字段库"所有后续的高阶变换和组合，都基于这些种子字段展开不要追求复杂的数学公式，最简单的信号往往最有效。这赛季我多个表现最好的 alpha，都是纯 0 阶的原始字段 rank。4. 123 阶模板其实非常好，是放大信号最好的工具这是被绝大多数人严重低估的神器。123 阶模板是比绝大多数人自己写的高阶模板效果都好。5. 123 阶模板生成的 alpha 用 AI 帮助优化当你用 123 阶模板得到基础 alpha 后，用 AI 进行优化能大幅提高效率。我常用的 AI 优化方向：参数调优：让 AI 在合理范围内遍历窗口大小、权重系数等参数，目标是提高夏普、降低换手率噪声过滤：加入流动性过滤、涨跌停过滤、异常值剔除等条件，减少信号噪声特征组合：将几个相关性低的基础信号进行加权组合，生成更稳定的复合信号持仓周期优化：测试不同调仓频率，找到该信号的最优持仓周期6. 提高自己手搓修正 alpha 性能的能力，自己动手比 AI 快AI 是工具，但不能代替人的思考。手搓 alpha 的能力才是量化顾问的核心竞争力，而且在很多关键场景下，自己动手比 AI 快得多。AI 的局限性在于它不懂信号背后的经济逻辑。当一个信号表现不佳时，AI 只能盲目尝试各种变换，而你可以通过分析市场结构和数据特性，快速定位问题并修正。我的建议：每天至少花 1 小时手搓 alpha，保持对数据和市场的敏感度深入理解每个信号的经济逻辑，知道它为什么赚钱，什么时候会失效针对不同地区的市场特点，手动调整信号的适用条件7. 1 个月最好只做 2~3 个地区，以 atom 为主，部分数据集需要混量价信号大胆去混8. 提交标准很重要，宁愿少交不要交一堆垃圾这是最后一条，也是最重要的一条。提交垃圾 alpha 不仅浪费你的时间，还会降低你的审核通过率和优先级。我目前提交标准：满足RA基本要求，也就是华子哥插件看过去0fail，近2年指标越高越好，参与ppa主题时pc值是次要标准，更关注alpha本身性能。以上就是我成为顾问这大半年来总结的 经验。量化没有捷径，AI 能提高效率，但不能代替思考。希望大家都能在赛季末挖到更多优质 alpha，点塔成功！附上6月2号的点塔图，不过我踩了个大坑，6月1号上午发晕交了个asi，给季度结算埋了个大雷，不知道comb分还能不能保住，只能静观其变了。

---

### 帖子 #20: 二季度了2个月，和大家分享一些alpha挖掘的思路经验分享
- **主帖链接**: https://support.worldquantbrain.com二季度了2个月和大家分享一些alpha挖掘的思路经验分享_40929650605207.md
- **讨论数**: 18

2026 年第二赛季已进入收官倒计时，相信大家都在为最后的点塔和赛季排名做最后冲刺。这赛季我在多个地区实战验证，踩过坑也总结出了一套可复制的 alpha 挖掘和点塔方法。今天严格按照自己的工作流，经验分享出来，希望能帮到大家，也欢迎在评论区交流指正。

## 1. 根据华子哥插件和网页的提交数据初步判断优质的数据集和字段

**先筛数据再干活，是所有工作的前提** 。每天早上我会花 30 分钟做数据勘探，绝不盲目写代码。

华子哥插件优先找绿色数据集这是华子哥通过GM权限通过SA筛选ra收集到的数据判断出的优质ALPHA比例高的数据集，其次看适合的中性化

配合网页端提交数据看全局：1.寻找提交较多的数据集/字段，你大概率也可以在这个数据集里找出可提交的alpha；2.寻找新的宇宙/数据集，这里的alpha相关性较低，竞争少。

## 2. AI 帮助生成初始信号

AI 是最高效的初始信号生成器，能帮我们快速扩大信号池。我的使用流程非常明确：

确定优质数据集后，给 AI 输入标准化 prompt：

- 明确要求生成 **0 阶信号** ，仅使用基础变换（rank、ts_rank、delta、log 等）
- 指定地区、数据集和核心字段范围
- 要求 AI 为每个信号附上 **一句话经济逻辑解释**
- 要求输出平台支持的标准语法，可直接复制运行

**关键原则** ：AI 生成的信号 90% 都是垃圾，我们只需要从中筛选出 3-5 个有逻辑、回测基础表现不错的信号，作为后续优化的起点。不要迷信 AI 给出的高夏普，大概率是过拟合。

## 3. 纯粹的 0 阶模板寻找优质字段信号

很多人看不起 0 阶模板，但 **真正能长期稳定的 alpha，80% 都源于 0 阶信号** 。

我常用的0阶段模板：最原始的字段回填\去极值；字段ts_rank；字段AB除法运算；字段AB减法运算。

我的标准操作：

- 对每个新数据集，先跑一遍所有字段的纯 0 阶信号
- 筛选出夏普 > 0.8、fit>0.5的字段，建立自己的 "种子字段库"
- 所有后续的高阶变换和组合，都基于这些种子字段展开

不要追求复杂的数学公式，最简单的信号往往最有效。这赛季我多个表现最好的 alpha，都是纯 0 阶的原始字段 rank。

## 4. 123 阶模板其实非常好，是放大信号最好的工具

这是被绝大多数人严重低估的神器。 **123 阶模板是比绝大多数人自己写的高阶模板效果都好** 。

## 5. 123 阶模板生成的 alpha 用 AI 帮助优化

当你用 123 阶模板得到基础 alpha 后，用 AI 进行优化能大幅提高效率。

我常用的 AI 优化方向：

- **参数调优** ：让 AI 在合理范围内遍历窗口大小、权重系数等参数，目标是提高夏普、降低换手率
- **噪声过滤** ：加入流动性过滤、涨跌停过滤、异常值剔除等条件，减少信号噪声
- **特征组合** ：将几个相关性低的基础信号进行加权组合，生成更稳定的复合信号
- **持仓周期优化** ：测试不同调仓频率，找到该信号的最优持仓周期

## 6. 提高自己手搓修正 alpha 性能的能力，自己动手比 AI 快

AI 是工具，但不能代替人的思考。 **手搓 alpha 的能力才是量化顾问的核心竞争力** ，而且在很多关键场景下，自己动手比 AI 快得多。

AI 的局限性在于它不懂信号背后的经济逻辑。当一个信号表现不佳时，AI 只能盲目尝试各种变换，而你可以通过分析市场结构和数据特性，快速定位问题并修正。

我的建议：

- 每天至少花 1 小时手搓 alpha，保持对数据和市场的敏感度
- 深入理解每个信号的经济逻辑，知道它为什么赚钱，什么时候会失效
- 针对不同地区的市场特点，手动调整信号的适用条件

## 7. 1 个月最好只做 2~3 个地区，以 atom 为主，部分数据集需要混量价信号大胆去混

## 8. 提交标准很重要，宁愿少交不要交一堆垃圾

这是最后一条，也是最重要的一条。 **提交垃圾 alpha 不仅浪费你的时间，还会降低你的审核通过率和优先级** 。

我目前提交标准：满足RA基本要求，也就是华子哥插件看过去0fail，近2年指标越高越好，参与ppa主题时pc值是次要标准，更关注alpha本身性能。

以上就是我成为顾问这大半年来总结的 经验。量化没有捷径，AI 能提高效率，但不能代替思考。希望大家都能在赛季末挖到更多优质 alpha，点塔成功！附上6月2号的点塔图，不过我踩了个大坑，6月1号上午发晕交了个asi，给季度结算埋了个大雷，不知道comb分还能不能保住，只能静观其变了。


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GU
> EUR
> CAN
> NOR
> TWNN
> JPN
> AR
> D
> MEA
> anahst
> ol=r
> Earninss
> Fundamsnzs
> Imtslance
> ITIaEr
> Insilin
> Mscro
> N3el
> NEs
> 0otion
> O-her
> Price Vclume
> Fisk
> SEniTET
> ShorIn-eres
> Social Ie3a
  
> [!NOTE] [图片 OCR 识别内容]
> Signals
> 235
> Reached Grandmaster
> 220
> Pyramids Completed
> 60
> Reached Grandmaster
> Combined Alpha Performance
> 2.35
> Reached Grandmaster
> Combined Selected Alpha Performance
> 2.72
> Reached Grandmaster
> Combined Power Pool Alpha Performance
> 1.69
> 0.31 more to Grandmaster
> Combined Osmosis Performance
> -0.21
> 0.71 more to Expert


---

### 帖子 #21: 作为一个gold级别的新人,我是怎么点满60个塔经验分享
- **主帖链接**: 作为一个gold级别的新人我是怎么点满60个塔经验分享.md
- **讨论数**: 25

我是11月18日成为顾问的新人，2025Q4有42天时间，交数量倒是满足MS级别了，但是12月的comb分0分，VF由于11月不够20天没有出分。提交的alpha质量应该是好坏都有，当时很多知识都不了解，胡乱提交的。2026年1月我之前发了一个PPA活动主题限制下，提交ra点塔的一点心得。 – WorldQuant BRAIN帖子，alpha提交策略成熟了一些，1月comb也刷新到了1.49，VF第一次出分0.80。3月5日我的点塔数也60个了，达到了GM标准，看了华子哥插件是国区第4达标的，全球前十也只有我是个小GOLD，许愿马上刷新的comb分能上2.0。主要经验是多做RA，跟活动的话交优质ppa，ppa就别太关注pc了。

---

### 帖子 #22: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。
- **主帖链接**: https://support.worldquantbrain.com作为一个gold级别的新人我是怎么点满60个塔经验分享_38844379720727.md
- **讨论数**: 25

我是11月18日成为顾问的新人，2025Q4有42天时间，交数量倒是满足MS级别了，但是12月的comb分0分，VF由于11月不够20天没有出分。提交的alpha质量应该是好坏都有，当时很多知识都不了解，胡乱提交的。

2026年1月我之前发了一个 [PPA活动主题限制下，提交ra点塔的一点心得。 – WorldQuant BRAIN](PPA活动主题限制下提交ra点塔的一点心得_38121310515223.md) 帖子，alpha提交策略成熟了一些，1月comb也刷新到了1.49，VF第一次出分0.80。 
> [!NOTE] [图片 OCR 识别内容]
> Gsnius level: Gold
> I TTJC' Gol
> CUTtCUTCTCni: NIrh3151 2026
> Eligibility Criteria
> 7026 41.Iru 15t 2036
> Irc31s 2036
> S
> nr
> TTFTTm
> Sgnals
> 249
> Rached Crrdmrl
> Pramids ComPersJ
> Rached Crrdmrl
> TONh NS
> Alha Performance
> 1.49
> 151 TJr
> ITTam
> Combined Selected Alpha Performance
> TRNCT「CICCTR
> CombnsJ Fower PoolAlpha Ferforman-s
> 0.45
  
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2026-01,January 155 2026
> March 315t, 2026
> Cateyon
> U5
> GU
> EUR
> CHN
> NOOR
> TN
> Anayys
> 3O =
> Earr nEs
> FundaTsTts
> ImTaIT=
> IO
> Inaions
> a
> Idsl
> Nsws
> Cation
> Dher
> Price Volune
> Ris
> TTmn
> SorIntsrsst
> Sciallls-la


3月5日我的点塔数也60个了，达到了GM标准，看了华子哥插件是国区第4达标的，全球前十也只有我是个小GOLD，许愿马上刷新的comb分能上2.0。

主要经验是多做RA，跟活动的话交优质ppa，ppa就别太关注pc了。

---

### 帖子 #23: 痛失GM，新手的Q1总结经验分享
- **主帖链接**: 痛失GM新手的Q1总结经验分享.md
- **讨论数**: 9

先上最终成绩，comb分差了0.05。1月份的时候我发了个点塔帖子，当时comb还是1.5分，1月comb出分变成了2.08当时真的挺有信心的，但是因为ra做的比较多平均操作符比较高所以3月份乘着ppa主题放水，3月份交了许多低操作符的ppa，最终排名其实入围GM行列了，但没想到2月的comb分掉了下来。新人冲击GM失败，有懊恼也有收获吧，达到了MS级别开放了很多新权限Q2我还会继续努力的。说一下我的总结吧，从25年11月成为顾问以来到Q1结束，我总共开了7个地区分别是USA D0 D1,EUR D0 D1,GLB,KOR,IND。其中USA和EUR的D1我的OS应该是比较好的，而ind应该比较一般，USA和EUR的D0完全是新手阶段啥也不懂就去开了，我可以这样吹一下如果没有去碰D0我现在肯定是GM了。而2月份做的GLB和KOR应该属于偏差的成绩，把我的总comb给拉下去了。总comb分是由所有提交的区的成绩等权的，所以我的分母是7，而且优秀的分子只有USA和eur，IND、GLB、KOR属于中等偏下吧，而2个D0属于非常拉跨，所以我现在为了拯救偏差的地区每个月的sa notown额度都用来提交比较差的区而不是专注做低pc来赚BASE。同时在复盘Q1的成绩时候我在思考为什么我的总comb还不错，而ppa comb和渗透comb都不好，于是我对ppa池子进行了精选，只保留了最好的一批alpha，渗透打分同样经过人工的精选而不是脚本打分，希望下一次comb更新能有所提高。

---

### 帖子 #24: 痛失GM，新手的Q1总结经验分享
- **主帖链接**: https://support.worldquantbrain.com痛失GM新手的Q1总结经验分享_40153456172567.md
- **讨论数**: 9

先上最终成绩，comb分差了0.05。 
> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2026-01,January 1st, 2026
> March 315t. 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 360
> Reached Grandmaster
> 120
> 220
> Pyramids Completed
> 61
> Reached Grandmaster
> Combined Alpha Performance
> 1.95
> 0.05 more to Grandmaster
> Combined Selected Alpha Performance
> No matchine Alohas。 refreshed monthly
> Combined Power Pool Alpha Performance
> 1.27
> 0.73 more to Grandmaster
> Combined Osmosis Performance
> 0.22
> 0.28 more to Expert
  1月份的时候我发了个点塔帖子，当时comb还是1.5分，1月comb出分变成了2.08当时真的挺有信心的，但是因为ra做的比较多平均操作符比较高所以3月份乘着ppa主题放水，3月份交了许多低操作符的ppa，最终排名其实入围GM行列了，但没想到2月的comb分掉了下来。

新人冲击GM失败，有懊恼也有收获吧，达到了MS级别开放了很多新权限Q2我还会继续努力的。说一下我的总结吧，从25年11月成为顾问以来到Q1结束，我总共开了7个地区分别是USA D0 D1,EUR D0 D1,GLB,KOR,IND。其中USA和EUR的D1我的OS应该是比较好的，而ind应该比较一般，USA和EUR的D0完全是新手阶段啥也不懂就去开了，我可以这样吹一下如果没有去碰D0我现在肯定是GM了。而2月份做的GLB和KOR应该属于偏差的成绩，把我的总comb给拉下去了。总comb分是由所有提交的区的成绩等权的，所以我的分母是7，而且优秀的分子只有USA和eur，IND、GLB、KOR属于中等偏下吧，而2个D0属于非常拉跨，所以我现在为了拯救偏差的地区每个月的sa notown额度都用来提交比较差的区而不是专注做低pc来赚BASE。

同时在复盘Q1的成绩时候我在思考为什么我的总comb还不错，而ppa comb和渗透comb都不好，于是我对ppa池子进行了精选，只保留了最好的一批alpha，渗透打分同样经过人工的精选而不是脚本打分，希望下一次comb更新能有所提高。

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 26年Q1 Genius定级已更新Q2赛季加油.md
- **评论时间**: 2个月前

向各位GM大佬看齐！这次没能上GM。

---

### 探讨 #2: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 26年Q1 Genius定级已更新Q2赛季加油_39728814444695.md
- **评论时间**: 2个月前

向各位GM大佬看齐！这次没能上GM。

---

### 探讨 #3: 关于《A GUIDE ON OPERATORS PER ALPHA;YOU'LL LOVE IT!》的评论回复
- **帖子链接**: [Commented] A GUIDE ON OPERATORS PER ALPHAYOULL LOVE IT.md
- **评论时间**: 1个月前

good idea

---

### 探讨 #4: 关于《A GUIDE ON OPERATORS PER ALPHA;YOU'LL LOVE IT!》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] A GUIDE ON OPERATORS PER ALPHAYOULL LOVE IT_39984614202647.md
- **评论时间**: 1个月前

good idea

---

### 探讨 #5: 关于《AI/LLMs for Smart Search and Higher Simulation Yield置顶的》的评论回复
- **帖子链接**: [Commented] AILLMs for Smart Search and Higher Simulation Yield置顶的.md
- **评论时间**: 2个月前

Traditional brute-force searching within fixed parameter spaces often suffers from low efficiency and limited accuracy. Leveraging LLM-driven optimization and iterative logic refinement can effectively narrow down redundant ranges, streamline validation workflows, and boost overall operational precision in practical scenarios.

---

### 探讨 #6: 关于《AI/LLMs for Smart Search and Higher Simulation Yield置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] AILLMs for Smart Search and Higher Simulation Yield置顶的_36797616631959.md
- **评论时间**: 2个月前

Traditional brute-force searching within fixed parameter spaces often suffers from low efficiency and limited accuracy. Leveraging LLM-driven optimization and iterative logic refinement can effectively narrow down redundant ranges, streamline validation workflows, and boost overall operational precision in practical scenarios.

---

### 探讨 #7: 关于《Amazing, is this regular alpha or super alpha?》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Amazing is this regular alpha or super alpha_40888370293271.md
- **评论时间**: 22天前

very great!

---

### 探讨 #8: 关于《Getting started with India Alphas置顶的》的评论回复
- **帖子链接**: [Commented] Getting started with India Alphas置顶的.md
- **评论时间**: 2个月前

Refining Alpha logic and controlling turnover is critical for stable performance in the India stock universe. Rational parameter settings and cross-universe verification can greatly enhance Alpha robustness and long-term profitability

---

### 探讨 #9: 关于《Getting started with India Alphas置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Getting started with India Alphas置顶的_36059391387415.md
- **评论时间**: 2个月前

Refining Alpha logic and controlling turnover is critical for stable performance in the India stock universe. Rational parameter settings and cross-universe verification can greatly enhance Alpha robustness and long-term profitability

---

### 探讨 #10: 关于《How Long Did It Take You to Reach Master Rank?》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] How Long Did It Take You to Reach Master Rank_40535229293463.md
- **评论时间**: 21天前

It took me 4 months

---

### 探讨 #11: 关于《OSMOSIS POINTS ALLOCATION TIPS(GUIDANCE)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] OSMOSIS POINTS ALLOCATION TIPSGUIDANCE_40577986780695.md
- **评论时间**: 1个月前

Allocate high points to alphas with good performance is good idea

---

### 探讨 #12: 关于《Rethinking Alpha Development for Better Pool Performance》的评论回复
- **帖子链接**: [Commented] Rethinking Alpha Development for Better Pool Performance.md
- **评论时间**: 1个月前

thank you ! good idea

---

### 探讨 #13: 关于《Rethinking Alpha Development for Better Pool Performance》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Rethinking Alpha Development for Better Pool Performance_39894093253783.md
- **评论时间**: 1个月前

thank you ! good idea

---

### 探讨 #14: 关于《The Fitness Struggle: Balancing Signal Strength with Turnover》的评论回复
- **帖子链接**: [Commented] The Fitness Struggle Balancing Signal Strength with Turnover.md
- **评论时间**: 1个月前

good idea,thank you!

---

### 探讨 #15: 关于《The Fitness Struggle: Balancing Signal Strength with Turnover》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] The Fitness Struggle Balancing Signal Strength with Turnover_39951860962839.md
- **评论时间**: 1个月前

good idea,thank you!

---

### 探讨 #16: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] VF10单周期狂赚253814我的高Base骚操作大公开经验分享.md
- **评论时间**: 2个月前

羡慕，每天吃保底在哭

---

### 探讨 #17: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] VF10单周期狂赚253814我的高Base骚操作大公开经验分享_39467895537431.md
- **评论时间**: 2个月前

羡慕，每天吃保底在哭

---

### 探讨 #18: 关于《三、 **比赛经验总结**》的评论回复
- **帖子链接**: [Commented] 【AIAC20 冠军】关于比赛过程中一些经验的交流经验分享.md
- **评论时间**: 2个月前

听了大佬的分享，收获了不少新的知识，向大佬学习

---

### 探讨 #19: 关于《三、 **比赛经验总结**》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【AIAC20 冠军】关于比赛过程中一些经验的交流经验分享_39621432305175.md
- **评论时间**: 2个月前

听了大佬的分享，收获了不少新的知识，向大佬学习

---

### 探讨 #20: 关于《新代码:》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【AI打工人】代码公开0基础使用给AI流水线生成的alpha加上名字_40703455289623.md
- **评论时间**: 1个月前

感谢分享

---

### 探讨 #21: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用.md
- **评论时间**: 2 months ago

好东西，快把这个代码给我啊

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用_39466731879063.md
- **评论时间**: 2个月前

好东西，快把这个代码给我啊

---

### 探讨 #23: 关于《根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])》的评论回复
- **帖子链接**: [Commented] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的.md
- **评论时间**: 2个月前

VF掉到0.7了，收入少了很多

---

### 探讨 #24: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

================================================量化日记第七季================================

12月6日，昨天开始做ind区了，研究了很久论坛，发现自己好像走了弯路，开了太多的区，ind现在双倍而且a质量很好，继续加油加油。

================================================================================

---

### 探讨 #25: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

================================================量化日记第七季================================

12月7日，

前天看了直播，学会了mcp中这个72变的使用方法，马上就把我之前数据比较好的一个alpha因子放进去试了一下，不过模板跑出来太多了，我都不知道怎么选了！！

昨天利用模板遍历就多配置了几个数据进去，运气好还真跑出来一个，不错，看来活用MCP也不失为一种好办法！后面去论坛里面发现确实也有好多人利用MCP跑出了特别好的数据曲线，接下来我也要去好好研究一下MCP了，希望和大家一起共同进步！继续加油加油。

================================================================================

---

### 探讨 #26: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

================================================量化日记第七季================================

12月8日，

2025年12月7日，我的量化日记第七季打卡第3天

IND区双倍，真是太卷了，好多看着很漂亮的因子，都是高PC

继续加油加油。

================================================================================

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

每日记录

今天换了两个字段还是没有出货，点塔好难

=============================================

=================梦想是成为GM===================

=============================================

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

目前还在有条件顾问阶段，量化涉及的领域太广，回想刚参与时，把重点放在怎么按我的想法写代码偏离到怎么把web做的好看，转了一圈才发现又回到起点；量化的核心还是要依托平台的知识和自学；期待下月评级更新

---

### 探讨 #29: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

2026年1月20日 我的量化日记第九季 第一天==============================================================================================================================日记终于回来了。最近AI相关又开始井喷了.========================================================================================

---

### 探讨 #30: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

============================================================今天是2026年1月21日，昨天一共提交了3个alpha都是USA D1 RISK的，因为要交ra比较艰难。============================================================

---

### 探讨 #31: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

==============================================================================2026.01.21昨天第一次见到了更新OS的威力，很多alpha的OS走势都让人感到意想不到吸取教训，希望以后能做出更好的alpha===================================================================================

---

### 探讨 #32: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

===============================================================2026年1月1日新的一年，今日提交4个ind alpha and点亮anl===============================================================

---

### 探讨 #33: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

===============================================================2026年1月22日今日提交2个usa op alpha,纯ra还是太难===============================================================

---

### 探讨 #34: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

==========================================2026.01.23，可能要断粮了，USA的几个小数据集没有ppa可真难跑出来，今天只交了一个ra===================================================================================================================================================================

---

### 探讨 #35: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 5个月前

=============================================================== 2026年1月24日 usa d1 news真离谱，换了好几个数据集，一个ra也跑不出来，sharpe都不够。 ===============================================================

---

### 探讨 #36: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

2026.01.25ra挖不出来，开始组sa==================================================================================================================第九季开始===========================================================================================================================

---

### 探讨 #37: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

2026.01.26今天的交了3+1.完成任务==================================================================================================================第九季开始===========================================================================================================================

---

### 探讨 #38: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

2026.01.27今天的开始跑kor，还没找到合适的方法==================================================================================================================第九季开始===========================================================================================================================

---

### 探讨 #39: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

2026.01.28开始学习调整脚本跑出来的sa，优化到更好再提交==================================================================================================================第九季开始===========================================================================================================================

---

### 探讨 #40: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

==================================================================================2026.01.29AIAC 2.0比赛还是没什么头绪，停了会议之后准备开始着手实践一下这几天赶快把新的AIAC工作流搞定，争取尽快开始！！！===================================================================================

---

### 探讨 #41: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

=================================================================================2026.01.30今天EUR,USA分别交了2个，久违的4+1。===========================================================================================================================================================================

---

### 探讨 #42: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyYWJiODA1NC1mYTBiLTQwNDctYWMyZi00YTMxNzgzNmI5ODgGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxMRDIyODExBjsIVDoScmVzdWx0c19jb3VudGkL--0f770ec25f6757522a3a31f592ffd427aee00f77
- **评论时间**: 4个月前

=============================================================================================2026.01.31提交了1个regular alpha Prod Corr 平均值: 0.6781 Self Corr 平均值: 0.2715 Sharpe 平均值: 1.6900====================================================================================================================================================================================================

---

### 探讨 #43: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月20日 我的量化日记第九季 第一天==============================================================================================================================

日记终于回来了。最近AI相关又开始井喷了.========================================================================================

---

### 探讨 #44: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

============================================================

今天是2026年1月21日，昨天一共提交了3个alpha

都是USA D1 RISK的，因为要交ra比较艰难。

============================================================

---

### 探讨 #45: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

==============================================================================

2026.01.21

昨天第一次见到了更新OS的威力，很多alpha的OS走势都让人感到意想不到

吸取教训，希望以后能做出更好的alpha

===================================================================================

---

### 探讨 #46: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

===============================================================

2026年1月1日

新的一年，今日提交4个ind alpha and点亮anl

===============================================================

---

### 探讨 #47: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

===============================================================

2026年1月22日

今日提交2个usa op alpha,纯ra还是太难

===============================================================

---

### 探讨 #48: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

==========================================2026.01.23，可能要断粮了，USA的几个小数据集没有ppa可真难跑出来，今天只交了一个ra===================================================================================================================================================================

---

### 探讨 #49: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

=============================================================== 2026年1月24日 usa d1 news真离谱，换了好几个数据集，一个ra也跑不出来，sharpe都不够。 ===============================================================

---

### 探讨 #50: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026.01.25

ra挖不出来，开始组sa

==================================================================================

================================第九季开始=========================================

==================================================================================

---

### 探讨 #51: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026.01.26

今天的交了3+1.完成任务

==================================================================================

================================第九季开始=========================================

==================================================================================

---

### 探讨 #52: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026.01.27

今天的开始跑kor，还没找到合适的方法

==================================================================================

================================第九季开始=========================================

==================================================================================

---

### 探讨 #53: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026.01.28

开始学习调整脚本跑出来的sa，优化到更好再提交

==================================================================================

================================第九季开始=========================================

==================================================================================

---

### 探讨 #54: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

==================================================================================

2026.01.29

AIAC 2.0比赛还是没什么头绪，停了会议之后准备开始着手实践一下

这几天赶快把新的AIAC工作流搞定，争取尽快开始！！！

===================================================================================

---

### 探讨 #55: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

=================================================================================

2026.01.30

今天EUR,USA分别交了2个，久违的4+1。========================================================================================

===================================================================================

---

### 探讨 #56: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

=============================================================================================

2026.01.31提交了1个regular alpha Prod Corr 平均值: 0.6781 Self Corr 平均值: 0.2715 Sharpe 平均值: 1.6900====================================================================================================================================================================================================

---

### 探讨 #57: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

================================================量化日记第八季====================================2025.12.22日，今天尝试了eur d0 news下的数据集，不同中性化和方法都试了试，PNL线合格的a很多，但是都有报错，还在尝试调整。+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

---

### 探讨 #58: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025-12-20 
今天提交情况：
all_alpha_count: 1 ; avg_prod: 0.5458 ;
RA: 1个 ;
region: EUR ;sharpe:2.8 ; fitness:1.77 ; self_correlation:0.2667 ; prodCorrelation:0.5458 ,pyramids:['EUR/D1/ANALYST'] ;
===============================================================================================================================================================================================================================================================================================================================================================

---

### 探讨 #59: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

**2025年12月23日 周二**

假期后归来，赛季进入最后几个交易日。一切操作都趋于静止，如同大战后的战场，只等最终的清算与评定。我利用这段时间，仔细制定了2026年第一季度的详细研究计划，核心就是“横截面与时间序列信号的动态融合”。

以后常看看论坛，发发帖子。。。。持续进步！

---

### 探讨 #60: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

继续思考osmosis比赛的优化思路：打上分只是第一步，是该区域的全部alpha都打分，还是部分？如果从组合sa的角度来看，部分打分是最优策略。

=============================================

慢慢来，相信时间的力量

=====================================================

---

### 探讨 #61: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月28日 ==================================================================================

今日提交四个ra一个sa

==================================================================================

目前vf 0.50

昨天提交了四个ra一个sa

base: 1.92(ra)+1.80(sa)

==================================================================================

---

### 探讨 #62: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

======================================================================

最后几天了 塔也30+了 感觉都没什么动力了 ...只能在社区分上丑陋挣扎一下了

sharpe is ts_delta and ts_delta but returns ts_delay and ts_delay
======================================================================

---

### 探讨 #63: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

- ===================================量化日记===============================
  第八季开始！！！
  今天回测5000，提交3alpha
  ====================================================================================================================Hope high combine==================================
  ==================================================================================
  5

---

### 探讨 #64: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

- 2025年12月25日 ==================================================================================
  ==================================================================================点塔记录
  start 8:59
  usa1 IMB5
  ==================================================================================
  ==================================================================================

---

### 探讨 #65: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

- 2025年12月26日 ==================================================================================
  今日提交四个ra一个sa
  ==================================================================================
  目前vf 0.50
  昨天提交了四个ra一个sa
  base: 1.9(ra)+1.80(sa)
  ==================================================================================

---

### 探讨 #66: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

- =====================================评论区=========================================
  不知不觉都第八季了
  888，发发发
  祝大家本季度combine一起发 ===================================================================================
  17

---

### 探讨 #67: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

**量化日记 2025-11-28:**

昨天提交了一个fit<5的sa，和一个质量还算ok的ra。sa的base只有7+，ra 4.64。不知道ra是否合格。没有了课代表的vf0.5 1.5$的判定标准，只能自己多做robust测试了。sa的base出我意料的低。原来fit<5的sa，和fit>5的base差距这么大。

从明天开始，先交fit>5的sa 吧；regular alpha还是基本没有产出，希望明天有好运降临，产出突破0.

祝我明天base多多，alpha产出多多

---

### 探讨 #68: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

今日提交情况： Regular：1个 selfCorrelation: 0.66 prodCorrelation: 0.66 PPAC: 3个 selfCorrelation: 0.21 prodCorrelation: 0.49 selfCorrelation: 0.16 prodCorrelation: 0.44 selfCorrelation: 0.22 prodCorrelation: 0.44 SA：1个 selfCorrelation: 0.59 prodCorrelation: 0.59 ==============================每日分析============================= Regular已经得到了控制，SA的pc也开始向好发展 Sharpe、Fitness，Margin指标都还可以。 SA还需要进一步优化， 数据分散性还需要进一步提升 =========================尽量提高质量，保证提交数量===================

---

### 探讨 #69: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/01:

1. 今日提交 Regular Alpha 汇总:

- Region: EUR, Delay: 1, Universe: TOP2500, Self-Correlation: 0.4173, Prod-Correlation: 0.6317.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #70: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/02:

1. 今日提交 Regular Alpha 汇总:

- Region: EUR, Delay: 1, Universe: TOP2500, Self-Correlation: 0.2, Prod-Correlation: 0.6.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #71: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/03:

1. 今日提交 Regular Alpha 汇总:

- Region: EUR, Delay: 1, Universe: TOP2500, Self-Correlation: 0.3, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #72: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/04:

1. 今日提交 Regular Alpha 汇总:

- Region: EUR, Delay: 1, Universe: TOP2500, Self-Correlation: 0.5, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #73: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/05:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #74: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/06:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #75: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/07:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.3, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #76: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/08:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.1, Prod-Correlation: 0.6.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #77: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/09:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.2, Prod-Correlation: 0.3.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #78: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/10:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #79: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/11:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #80: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/12:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 0, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #81: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/13:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.1, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #82: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/14:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.8.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #83: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/15:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #84: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/16:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #85: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/17:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.1, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #86: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/18:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.1, Prod-Correlation: 0.3.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #87: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/19:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #88: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/20:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #89: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/21:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #90: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/22:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #91: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/23:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #92: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/24:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #93: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/25:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #94: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/26:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #95: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/27:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #96: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/28:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #97: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/29:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #98: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/30:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #99: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 5个月前

2025/12/31:

1. 今日提交 Regular Alpha 汇总:

- Region: USA, Delay: 1, Universe: TOP3000, Self-Correlation: 0.6, Prod-Correlation: 0.5.

2. 今日提交 Super Alpha 汇总:

- 无

==================================================================================

==================================================================================

=====================================================================

==================================================================================

==================================================================================

---

### 探讨 #100: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第六季.md
- **评论时间**: 7个月前

新顾问开始疯狂点塔，在 USA 点塔中，3天已经点完了 3个塔了，进度应该还好。加油，加油，加油！==================================

============================================================================

=============================== 无限进步 ====================================

============================================================================加油

---

### 探讨 #101: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第六季.md
- **评论时间**: 7个月前

====

今天做usa的earning的因子回测，提交了4个ppac。

大概回测了一阶6000次和二阶3000次，有几个还行的因子，prod corr控制在0.7以内。

2个一元的，2个二元的，这样我的AVG operators和avg datafields都没改变。感觉这样不行，还是要关注AVG operators和avg datafields才行。 usa地区做得差不多了，明天开始换eur地区做。

=============================================================================

---

### 探讨 #102: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++
因子做多了, 腰酸背痛的,好想买一个沙发.

---

### 探讨 #103: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

==++++++++++++++++半夜惊喜发现帖子开了，开始记录新的一季因子日记============

++++++

---

### 探讨 #104: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

今天只提交了两个ppa

一个ra，不足预期，要继续加油了++++++++++++++++++++++++++++++++++++++++++++++

++++

---

### 探讨 #105: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

======================================================================

======================================================================最后几天了，60塔，comb分都满足了随机剩下的就是优化六维了，新顾问回测天数吃了大亏

======================================================================

======================================================================

---

### 探讨 #106: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

======================================================================

======================================================================

======================================================================赛季最后几天，为了GM定级加油

======================================================================

======================================================================

======================================================================

---

### 探讨 #107: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

今天继续疯狂修正六维，争取在赛季达到了 GM 等级，再接再厉。

============================================================================
=============================== 无限进步 ====================================
============================================================================

---

### 探讨 #108: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

===============================================================

===============================================================今天交了3个r一个sa，继续努力

===============================================================

===============================================================

---

### 探讨 #109: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

===============================================================

===============================================================4个comb分数差异很大，2.08，1.19，0.39,，0为什么呢

===============================================================

===============================================================

---

### 探讨 #110: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

===============================================================

===============================================================今天交满了4+1继续努力

===============================================================

===============================================================

---

### 探讨 #111: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

===============================================================

===============================================================

===============================================================赛季末冲刺，大家加油

===============================================================

===============================================================

---

### 探讨 #112: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

================================================第十季终于开了，赛季末冲刺，加油加油========================================================================

---

### 探讨 #113: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

================================================第十季终于开了，跟着ppa活动，又到了GLB区，加油=====================================================================

---

### 探讨 #114: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

================================================第十季终于开了GLB区，news21能跑出很多===================================================================

---

### 探讨 #115: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

日常点滴记录：

MCP的API是否可以设置一层中间层代理，把很多请求拦截住，通过另外一个AI来自适应的返回JSon，减少不必要的交互，还有回测的交互。比如反复认证，回测请求总是失败。

最近我通过gemini回测达到一定批次后，总会遇到json错误，切换到新会话或者清空进程会才能正常。

-----------------------------------------------------------------------------------------------------------------------

慢即是快，相信时间的力量。

-----------------------------------------------------------------------------------------------------------------------

---

### 探讨 #116: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

==================================================================================== 2026/03/3: 这几天还是在改代码，目前小问题还非常多； 提交了一个GLB的SA，因为我提交的GLB因子质量普遍不高，SA的表现也不尽人意。

========================================================================================================================================================================

---

### 探讨 #117: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

今日提交三个因子，其中一个因子的获取方式是筛选回测过的因子中fitness负得比较多的，然后将其取反得到的，感觉自己确实遗漏了一些取反后可以表现比较好的因子，明天的计划是继续检查类似的因子，然后对信号进行加强。这个思路是逛顾问中文论坛得到的，作为新手，感觉还是不能总是埋头苦干，还是应该多看看论坛积累经验。

========================================================================================================================================================================

========================================================================================================================================================================

---

### 探讨 #118: 关于《一句话让python alpha动起来》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】一句话改造mcp支持pyhton alpha_40684608877591.md
- **评论时间**: 1个月前

感谢大佬的探索经验

---

### 探讨 #119: 关于《【经验分享】什么？菜鸡gold也能三天连续90刀+》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】什么菜鸡gold也能三天连续90刀_40639393075223.md
- **评论时间**: 28天前

很厉害

---

### 探讨 #120: 关于《一个新的免费token plan: 商汤-日日新，支持deep seek v4 flash,  附minimax2.7, gemini pro3对比经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 一个新的免费token plan 商汤-日日新支持deep seek v4 flash  附minimax27 gemini pro3对比经验分享_40372795793687.md
- **评论时间**: 1个月前

很实用的信息，感谢分享

---

### 探讨 #121: 关于《穿透参数迷雾：量化策略的敏感度分析与鲁棒性构建》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 穿透参数迷雾量化策略的敏感度分析与鲁棒性构建_39854893045655.md
- **评论时间**: 1个月前

感谢大佬分享

---
