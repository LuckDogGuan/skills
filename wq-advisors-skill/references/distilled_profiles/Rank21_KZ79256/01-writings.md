# 顾问 KZ79256 (Rank 21) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 KZ79256 (Rank 21) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: 25Q3顾问提交情况播报（每日更新）
- **主帖链接**: https://support.worldquantbrain.com[L2] 25Q3顾问提交情况播报每日更新_33266491538199.md
- **讨论数**: 96

本贴使用Genius排行榜及Consultant排行榜数据，对以下指标进行统计：

- 本季度有提交、今日有提交、提交满20天（定级基准）的顾问人数
- SA、RA提交情况（数量和平均相关性）
- RA平均操作符数量、平均字段数量

并且每种指标分别对以下群体统计：

- 今日有提交的顾问
- 今日有提交且Combined Alpha Performance>=2的顾问
- 今日有提交且Combined Selected Alpha Performance>=2的顾问
- 今日有提交且Value Factor>=0.95的顾问

本贴每日更新。如有疑问、指标建议、排版建议等，欢迎留言讨论，欢迎写下你对数据的敏锐洞察！

---

### 帖子 #2: BRAIN API及日常回测时常见的报错代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md
- **讨论数**: 5

以下是一些可能的错误消息，它们的可能原因以及解决方案：

- **1. **Attempted to use unknown variable**尝试使用未知变量**

- 数据不可用
   - 表达式中包含了一个不可用的变量。检查你的变量是否有拼写错误，或者你是否在设置中使用了正确的区域。提示：如果在表达式中正确使用，数据字段和操作符的字体颜色会显示为蓝色。

- **2. **Unexpected end of input**意外的输入结束**

- 语法错误，Alpha没有结尾
   - 一个常见的语法错误通常来自于最后一行的Alpha缺少括号或缺少分号。
   - 例如："rank(sales/assets" 会引发此错误

- **3. **Expression cannot be empty**表达式不能为空**

- 在最后一行加分号
   - 该错误通常在用户将他们的alpha分配给一个变量，但实际上没有在之后调用它时引发。
   - 例如： "alpha = -ts_delta(close,5);" 会引发错误，但 "alpha = -ts_delta(close,5); alpha" 就不会。

- **4. **Illegal group index value, cannot exceed number of elements****

- Group operator没有加densify
   - 为确保平台的高性能，在模拟过程中对组索引的值进行检查。索引值不应超过所有索引组所属的元素数量。如果引发错误消息，那么可能是组的索引在某个操作符中使用的不是密集的（非密集索引看起来像[0, 5, 8, 26, 107]）。在这种情况下，使用"densify(group)"会有所帮助。

- **5. **Illegal group index value, cannot be negative**非法的组索引值，不能为负**

- 非法的grouping值
   - 我们不允许组索引的值为负，要解决这个问题，试试使用densify操作符。且自定义分组的时候不能有负值

- **6. **Got invalid value for attribute "lookback", must be constant or string****

- "lookback" 得到无效值，必须为常量或字符串
   - 当你试图在操作符的 "lookback" 字段中使用非常量或字符串，或者当你错误地排列参数时，会引发此错误。
   - 例如："ts_rank(sales/assets, days_from_last_change(sales))" 会引发错误

- **7. **Grouping data used outside of group operator**在group operator外部使用grouping数据**

- 分组数据只能在组操作符中使用。如果你试图在其他地方使用组数据，就会引发此错误。
   - 例如："ts_delta(industry, 5)" 会引发错误

- **8. **Cumulative lookback of expression exceeds available history**表达式的累积回看超过了可用的历史**

- lookback区间非法
   - 由于数据历史的限制，如果你试图回看超过我们可以提供的范围，就会引发此错误。注意，考虑的累积回看是表达式中使用的最高回看。
   - 例如：ts_rank(ts_mean(close,20),20) 会有40的累积回看。

- **9. **You have reached the limit of concurrent simulations. Please wait for previous simulations to finish****

- 一个用户只能同时simulate10个；你已经达到了并行回测的限制。请等待之前的回测完成
   - 你一次只能模拟有限数量的alpha，所以如果你试图模拟超过这个数量，就会引发此错误。你必须等待你之前的一个模拟完成才能继续。

- **10. **Invalid number of inputs: X, should be exactly Y input(s)****

- 有参数未输入
    - 当你提供的输入数量多于或少于所需数量时，会引发此错误。
    - 例如：无论是 "group_mean(sales/assets, market)" 还是 "group_mean(sales/assets, 1, market, 1)" 都会引发此错误。正确的表达式应该是："group_mean(sales/assets, 1, market)"

- **11. **超时登出：Http Error****

- 所有用户每4个小时or提交过多错误simulation会被强制登出。需要书写代码捕捉错误并随时重登，同时需要保证任务的断点续传。

- ***12.* “回测应该回测了3000多个实例，但由于某种原因，丢失了1700个实例。已经设置了一个sleep函数，以防止访问次数过多，并一直在监视status_code以查找错误。但依然出现此问题，如何解决？”**

- simulation_response.status_code为201并不代表你的Alpha运行没有问题，运行有问题的Alpha就是会被丢失的。您可以运行一下下列代码，体会一下错误的来源：

```
simulation_data = {    'type': 'REGULAR',    'settings': {        'instrumentType': 'EQUITY',        'region': 'USA',        'universe': 'TOP3000',        'delay': 1,        'decay': 15,        'neutralization': 'SUBINDUSTRY',        'truncation': 0.08,        'pasteurization': 'ON',        'unitHandling': 'VERIFY',        'nanHandling': 'OFF',        'language': 'FASTEXPR',        'visualization': False,    },    'regular': 'high-close+dfd'}simulation_response = s.post('[链接已屏蔽] json=simulation_data)print(simulation_response.status_code)print(s.get(simulation_response.headers['Location']).json())print(f'status: {s.get(simulation_response.headers["Location"]).json()["status"]}')
```

- ***13.***  **“不确定SLOW+FAST参数的代码”/“不确定Neutralize选项country/region参数的代码”**

*- "* SLOW_AND_FAST"

*- "* COUNTRY"

- ***14.***  **”当使用模板进行模拟时，结果不好，有些时间点显示出平坦的曲线，表明该模型在那些时间没有股票选择能力。“**

- 请手动找到这个Alpha进行查看。在网页浏览器入“ [[链接已屏蔽]) 即可以看到它的表现。一般这种Alpha的出现是因为使用Alpha前的数据处理工作还不够好。

- ***15.***  **"目前我的代码在运行1000次成功回测的时间大概是2个小时到2个半小时之间，这是一个正常的速度吗？"**

-速度是正常的。看到您也获得了一个新可提交的Alpha,从效率上看，大约1000次simulation获得一个Alpha也是正常的效率，这个说明您的模板选择和数据选择都比较合适。另外一个检测自己速度是否合适的方法就是，回到网页界面，尝试手动simulate一下Alpha,如果会报错“too many simulation at a time”，这就说明代码正在全力工作，占用完了十个线程，算是高效了。

- **16. Correlation获取超时**

-用户只能在60分钟内发送150 correlation requests。不要对每个simulated的Alpha都request

- 17. 如何在JupyterNotebook实现多线程和随时插队？

下面这个代码可能可以提供一些思路：

在JupyterNote Book 的第一个cell

```
import timeimport threadingimport requestsclass RequestThread(threading.Thread):    def __init__(self, urls):        threading.Thread.__init__(self)        self.urls = urls    def send_request(self, url):        print(f'Sending request to {url}')        response = requests.get(url)        # handle your response here        time.sleep(5)    def run(self):        i = 0        while i < len(self.urls):            self.send_request(self.urls[i])            i += 1           urls = ['[链接已屏蔽] '[链接已屏蔽] '[链接已屏蔽] = RequestThread(urls)request_thread.start()
```

接着可以随时跑其他cell

```
urls.append('[链接已屏蔽])
```

或者，可以把所有待simulate的Alpha全部先放到一个csv文件，然后用另外一个notebook去读这个csv文件，不断发出Alpha到服务器中。简而言之，将csv文件作为不同notebook的交互点（中转站）

---

### 帖子 #3: How to Improve After Cost Performance置顶的
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

### 帖子 #4: Lab中处理Vector数据的一种方法代码优化
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

### 帖子 #5: Lab中处理Vector数据的一种方法代码优化
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

### 帖子 #6: Machine Alpha 基础知识1：什么是Alpha模板
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

### 帖子 #7: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #8: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
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

### 帖子 #9: Maximizing Combined Alpha Performance: Key Strategies and Insights
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

### 帖子 #10: Research Paper 53: Textual Sentiment, Option Characteristics, and Stock Return Predictability
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper 53 Textual Sentiment Option Characteristics and Stock Return Predictability_15770194203159.md
- **讨论数**: 21

**Abstract:**

We distill sentiment from a huge assortment of NASDAQ news articles by means of machine learning methods and examine its predictive power in single-stock option markets and equity markets. We provide evidence that single-stock options react to contemporaneous sentiment. Next, examining return predictability, we discover that while option variables indeed predict stock returns, sentiment variables add further informational content. In fact, both in a regression and a trading context, option variables orthogonalized to public and sentimental news are even more informative predictors of stock returns. Distinguishing further between overnight and trading-time news, we find the first to be more informative. From a statistical topic model, we uncover that this is attributable to the differing thematic coverage of the alternate archives. Finally, we show that sentiment disagreement commands a strong positive risk premium above and beyond market volatility and that lagged returns predict future returns in concentrated sentiment environments.

Key ideas:

- Page 12 paragraph 2
- Page 17 Hypothesis 1
- Page 18 Hypothesis 2
- Page 20 Hypothesis 3
- Page 23 Hypothesis 4
- Page 27 Hypothesis 5
- Page 28 Hypothesis 6

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

implied volatility

opt4_vola_10d

[**Option4**]([链接已屏蔽])

put price

opt4_put_pre_122d

[**Option4**]([链接已屏蔽])

call price

opt4_call_pre_122d

[**Option4**]([链接已屏蔽])

Author: Cathy Chen, Matthias R. Fengler, Wolfgang Karl Härdle, Yanchu Liu

Year: 2018

Link:  [[链接已屏蔽])

---

### 帖子 #11: Research Paper 72: Testing for Asset Price Bubbles using Options Data
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper 72 Testing for Asset Price Bubbles using Options Data_16412791948695.md
- **讨论数**: 29

**Abstract**

We present a new approach to identifying asset price bubbles based on options data. We estimate asset bubbles by exploiting the differential pricing between put and call options. We apply our methodology to two stock market indexes, the S&P 500 and the Nasdaq-100, and two technology stocks, Amazon and Facebook, over the 2014-2018 sample period. We find that, while indexes do not exhibit significant bubbles, Amazon and Facebook show frequent and significant bubbles. The estimated bubbles tend to be associated with high trading volume and earning announcement days. Since our approach can be implemented in real time, it is useful to both policy-makers and investors. As an illustration we consider two case studies: the Nasdaq dot-com bubble (between 1999 to 2002) and GameStop (between December 2020 and January 2021). In both cases we identify significant and persistent bubbles.

Author: Nicola Fusari, Robert Jarrow, Sujan Lamichhane

Year: 2020

Link:  [[链接已屏蔽])

Key ideas and Comments from WorldQuant:

- Page 11 Paragraph 2
- Page 22 Paragraph 2,3
- Page 25 Paragraph 1
- Page 28 Paragraph 2

**Term**

**Data field**

**Dataset**

option

fnd6_optgr

[Company Fundamental Data for Equity]([链接已屏蔽])

call option

call_breakeven_10

[Options Analytics]([链接已屏蔽])

---

### 帖子 #12: self corr计算的代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] self corr计算的代码优化_32893337921943.md
- **讨论数**: 2

感恩大佬发布了准确计算self corr的代码

经过长时间的使用, 对于自己经常需要用的功能,我也补充了一些进入到代码里面, 分享给各位朋友参考.

1.优化打印逻辑, 原先的代码里面会打印出多个corr来,实际上我更关心的是最大的corr数值,所以修改了.

2.除了最大的corr,实际上我还关心最小的corr,因为在实际情况中,有时候我们需要一下reverse,把原先的负数sharpe变为正数,所以我会看一下sharpe为负数时,最小的corr数值是多少.

参考实现如下:

```
def calc_self_corr(    alpha_id: str,    os_alpha_rets: pd.DataFrame | None = None,    os_alpha_ids: dict[str, str] | None = None,    alpha_result: dict | None = None,    return_alpha_pnls: bool = False,    alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    # 找到相关性序列    correlation_series = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4)    # 获取最大的相关性数值    max_correlation = correlation_series.iloc[0]    min_correlation = correlation_series.iloc[-1]    # 打印最大的相关性数值    print('max_correlation: '+ str(max_correlation))    print('min_correlation: '+ str(min_correlation))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corr
```

3.因为每次交完alpha以后,原先计算过self corr的需要进行更新,每次才能跟服务器下载PNL会花很多时间,所以我把PNL数据直接存储本地了.实现代码如下:

```
def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    df = df[['Date', alpha_id]]    return dfdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """带数据库缓存的PNL获取函数"""    # 先尝试从数据库获取    db_data = get_pnl_from_db(alpha_id)    if db_data:        pnl_dict = json.loads(db_data["pnl_data"])        df = pd.DataFrame(pnl_dict['records'],                         columns=[item['name'] for item in pnl_dict['schema']['properties']])    else:        # 从API获取        pnl = wait_get(f"[链接已屏蔽]).json()        # 存储到数据库        region = wait_get(f"[链接已屏蔽]).json()['settings']['region']        if not save_pnl_to_db(alpha_id, region, pnl):            logging.warning(f"Failed to save PNL data for {alpha_id} to DB")               df = pd.DataFrame(pnl['records'],                         columns=[item['name'] for item in pnl['schema']['properties']])       df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    return df[['Date', alpha_id]]def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """带数据库缓存的PNL获取函数"""    # 先尝试从数据库获取    if check_alpha_exists(alpha_id):        conn = get_db_conn()        try:            with conn.cursor() as cursor:                sql = "SELECT pnl_data FROM alpha_pnl WHERE alpha_id = %s"                cursor.execute(sql, (alpha_id,))                result = cursor.fetchone()                pnl = json.loads(result['pnl_data'])        finally:            conn.close()    else:        # 从API获取并保存到数据库        pnl = wait_get(f"[链接已屏蔽]).json()        region = wait_get(f"[链接已屏蔽]).json()['settings']['region']        save_alpha_pnl(alpha_id, pnl, region)       # 保持原有处理逻辑不变    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    return df[['Date', alpha_id]]
```

4.因为我的alpha数据也是直接存在了本地服务器,所以在打印alpha的时候,我希望能够直观地打印出alpha的表达式和sharpe,fitness等数据,针对自己的数据库数据格式,采用了打印的方式,部分代码如下:

```
def print_dict_info(data):    print("exp:")    print(data['exp'])    headers = [        'sharpe',        'fitness',        'returns',        'margin',        'turnover',        'drawdown',        'longCount',        'shortCount',        'first_datafield'    ]    values = [        data['sharpe'],        data['fitness'],        f"{data['returns'] * 100:.2f}%",        f"{data['margin'] * 10000:.2f}‱",        f"{data['turnover'] * 100:.2f}%",        f"{data['drawdown'] * 100:.2f}%",        data['longCount'],        data['shortCount'],        data['first_datafield']    ]    row = " | ".join([f"{header}: {value}" for header, value in zip(headers, values)])    print(row)
```

大概的打印内容如下:

```
Fetching alphas from offset 0 to 30新下载的alpha数量: 0, 目前总共alpha数量: 359max_correlation: 0.1373min_correlation: -0.047536e****** self_corr: 0.13729466200741886exp:#ASI_1******s1;process1 = ts_z*****************4), 22);sharpe: 5.18 | fitness: 2.61 | returns: 12.40% | margin: 5.08‱ | turnover: 48.84% | drawdown: 2.04% | longCount: 1611 | shortCount: 1616 | first_datafield: None
```

5.这部分满足相关性要求的alphaid,如果数量很多的话,我会单独打印出来,然后使用navicat进行查看.

6.有时候下载的数据量是巨大的,那么中断的情况不在少数,jupyter里面打印会有问题,导致打印界面中断.所以我在确保代码稳定运行的情况下,直接忽略了报错,使用以下代码:

```
import warningswarnings.filterwarnings('ignore')
```

7.其实还有很多可以优化的地方,比如可以直接根据alpha的sharpe大于还是小于0,来判断符合corr标准的alpha.当sharpe小于0 时,需要获取的是最小corr,而不是最大corr.但是太懒了,就没有怎么写这些新的逻辑实现.

希望以上思路能够给大家提供一点点帮助.

---

### 帖子 #13: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location']
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

### 帖子 #14: Understanding ts_zscore.Research
- **主帖链接**: https://support.worldquantbrain.com[L2] Understanding ts_zscoreResearch_25502968546583.md
- **讨论数**: 26

The  [Z-Score]([L2] Understanding Z-Score OperatorsResearch_24912183913495.md) , a powerful statistical measure for standardizing data, extends to time-series data as ts_zscore.

**How is ts_zscore calculated?**

The ts_zscore operator calculates the time-series Z-score. The formula for `ts_zscore` is:

```
ts_zscore = (x - ts_mean(x, n)) / ts_stddev(x, n)
```

Where:

- `x` is the time-series data,
- `ts_mean(x, n)` is the moving average over 'n' periods, and
- `ts_stddev(x, n)` is the moving standard deviation over 'n' periods.

The `ts_zscore` is a dynamic measure that calculates the Z-score for a data point relative to the mean and standard deviation over a specified 'n' period.

**Getting started with ts_zscore.**

While ‘ts_zscore’ is a powerful tool, you need to keep a few considerations in mind when using it::

- If you apply `ts_zscore` to a constant, the standard deviation will be zero, and the `ts_zscore` will be undefined.
- You need to base the choice of 'n' on the frequency of the data. For daily data, you might choose 'n' as 252 (trading days in a year) for a yearly Z-score or 21 (trading days in a month) for a monthly Z-score.

**Potential sources of ideas**

With a clear understanding of the ts_zscore operator, it's now time to explore its practical applications:

- **Comparing different data fields.**  By calculating the `ts_zscore` for different data fields (like ratios, indicators, or Alphas), you can effectively compare these different measures. For instance, `ts_zscore(x, n) - ts_zscore(y, n)` can give a comparative measure of 'x' and 'y' over 'n' period.
- **Comparing same data field with different time periods.**  You can compare the `ts_zscore` of the same data field using different time periods. For instance, to compare the yearly Z-score with the monthly Z-score of a data field 'x', one can use ts_zscore(x, 252) - ts_zscore(x, 21)
- **Event triggering.**  You can use `ts_zscore` as an event trigger in your Alphas. For example, you may want to trigger a signal when the absolute `ts_zscore` of a data field is greater than 3. For instance, `event = abs(ts_zscore(x,n))>3; trade_when(event, signal, -1)` would trigger a signal when the event condition is met.
- **Filtering outliers.**  You can use `ts_zscore` to filter outliers in your data. For instance, `ts_zscore(x,n)>5? nan: x` to replace all data points where the `ts_zscore` is greater than 5 with NaN, effectively filtering these outliers from your data.

**✨Stay tuned**  for next week's discussion, where the focus will be on understanding group_zscore and its applications.

---

### 帖子 #15: Understanding Z-Score OperatorsResearch
- **主帖链接**: https://support.worldquantbrain.com[L2] Understanding Z-Score OperatorsResearch_24912183913495.md
- **讨论数**: 7

**How is Z-Score calculated?**

Z-score is a statistical tool that indicates how many standard deviations a data point lies from the average of a group of values. Essentially, it measures how unusual a data point is in relation to the mean, making it a handy tool for understanding deviation and comparison.

The formula to calculate a Z-score is:

```
Z-score = (x - mean(x)) / stddev(x)
```

Where:

- x is an individual data point
- mean(x) is the average of the data set
- std(x) is the standard deviation of the data set

**Characteristics of Z-Score**

- By this definition, the mean of the Z-scores in a distribution is always 0, and the standard deviation is always 1.
- A Z-score tells you how many standard deviations a particular data point is from the mean. If the Z-score is positive, the data point is above the mean, and if it's negative, it's below the mean.
- Z-scores may be especially useful for normalizing and comparing different data fields for different stocks or different data fields. They allow researchers to calculate the probability of a score occurring within a standard normal distribution and compare two scores that are from different samples (which may have different means and standard deviations).

**Getting started with Z-Score**

While Z-score is a powerful tool, there may be a few things to consider when using it:

- **Distribution of data.**  Z-scores assume a Gaussian distribution of the data. However, not all data follows this distribution. If the distribution of your data significantly deviates from a normal distribution (for example, if it has high skewness), the Z-score may not be the best measure to use.
- **Data transformations.**  If the data doesn't follow a Gaussian distribution, you might need to transform it before calculating the Z-score. Common transformations include the logarithmic transformation (log(1+x)) or hyperbolic tangent (tanh), among others.
- **Use of median.**  In the presence of outliers or skewed data, using the median instead of the mean might be more appropriate as the median is less sensitive to extreme values.
- **Winsorization.**  This is a method to limit the influence of outliers in your data. For example, you could cap all Z-scores above 4 or below -4 at 4 and -4, respectively. This method can effectively limit extreme values in the data, but remember that it can also change the mean value of the results: `abs(zscore(x))>4? 4*sign(zscore(x)) : zscore(x)`
- **Correlation.** The correlation between two variables 'x' and 'y' is the same as the correlation between the Z-scores of 'x' and 'y'. This property makes the Z-score a powerful tool to measure the relationship between variables.

**✨Stay tuned**  for next week's discussion, where the focus will be on understanding ts_zscore and its applications in time-series data.

---

### 帖子 #16: [BRAIN TIPS] How do you reduce correlation of a good alpha?
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] How do you reduce correlation of a good alpha_8046468280727.md
- **讨论数**: 14

This is a common problem many researchers face in their alpha research — you are not alone. First, let’s look at the good side of the problem. If the correlation between alphas is high, that means you have probably implemented similar ideas, so it is unlikely that you did something wrong. Your idea and implementation should be sound (assuming the original alpha had good performance).

So if you are new researcher, you should keep the idea around because it can be used for different alphas. Those alphas can be a variation of the current alpha using:

- *Different data fields:*  You might try to use an equivalent data field first (such as “high,” “low” or “open” to replace “close”).
- *Different operator:*  Again start with something you find similar in practice, building your own library of similarity that could further help you reduce max correlation.
- *Different grouping:*  This is powerful approach, but don’t create an arbitrary group just for the sake of reducing correlation.

The reason to try something equivalent first is to reduce the chance that you distort the implementation of your original idea. Maintain the purity of the idea rather than complicate it unnecessarily for the sake of correlation fitting (which is considered bad practice).

Of course, the best way to reduce max correlation is to think outside of the box. That is true research.

---

### 帖子 #17: [SuperAlpha]SELECTION框架-v2经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] [SuperAlpha]SELECTION框架-v2经验分享_33745533142679.md
- **讨论数**: 21

本文是 [组sa时如何选取高质量因子？ – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 组sa时如何选取高质量因子经验分享_32034293019671.md) 的优化版本，增加了一些额外的筛选项与选择思路，剔除了筛选权重排列，并使用额外的筛选条件进行替代。

以下正文：

## **select流程**

第一步：own or not own，对于expert及以上顾问适用

第二步：选择因子种类，sac2025中提供了很多可以按照因子种类进行筛选的语句，可以直接复制来用。主要包含两类，一类是因子的类别，例如atom，ppac。例：

```
in(classifications, "ATOM")
```

```
in(classifications, "POWER_POOL")
```

第三步：因子的设置。sac中有一周主题叫做风险中性化，需要用使用风险中性化的因子，这个思路感觉很好（因为在ra层面已经中性掉一些风险），也可以根据自己需求进行选择：

```
((neutralization == 'SLOW') || (neutralization == 'FAST') || (neutralization == 'SLOW_AND_FAST') || (neutralization == 'CROWDING') || (neutralization == 'STATISTICAL') || (neutralization == 'REVERSION_AND_MOMENTUM'))
```

使用常规的4个中性化亦可。

第四步：因子的类别。大家在日常跑因子的时候会感觉一些“小众”数据集跑出来的效果一般，这一步可以选取特定的数据类型。思路来源于橘子姐，在此表示感谢。例：

```
&&(in(datacategories, "fundamental")||in(datacategories, "analyst")||in(datacategories, "model")||in(datacategories, "news")||in(datacategories, "other")||in(datacategories, "risk")||in(datacategories, "pv"))
```

至于选择哪些类别，可以按需进行。例如：我想选一些差异较大的类别，那么可以选择fnd和socialmeida，如果我想针对基本面进行选择，则可以囊括fnd，anl，ern。

第五步：分层方式：之前的版本中提出用turnover进行分层，理由是一个因子的turnover不能反映因子的表现，但turnover可以把因子池划分成若干个区间，每次取不同的区间可以避免重复选取。除去turnover之外，也可以按照long count，short count进行分层。count数也不能反映因子表现，但可以分层。例：

```
turnover<0.1&&turnover>0.05
```

```
long_count>1000&&long_count<1200
```

```
a=sqrt(long_count*short_count);a>1000&&a<1200
```

第六步：相关性限制

经与weijie老师讨论，一味地选取低相关性可能不是很好的选择。因为有些好的因子被反复选到后相关性提高，初步的解决方式是利用prodcor和selfcor进行类似powerpool的双重选择。例：

```
((prod_correlation<0.6&&prod_correlation>0.1)&&(self_correlation<0.3&&self_correlation>0.05))  
```

第七步：运算符与字段个数选择。我们早就知道，过多的op和过多的字段不可避免地会带来过拟合，之前的版本中只是选择了op数目进行限制，这是有偏颇的。一阶因子的稳定度不如二阶，有些字段信号强到甚至可以“裸交”，但质量一般。为了剔除掉这些因子，可以采用op数目上下界+字段个数上界的方式进行选择。例：

```
&&(operator_count<=8)&&(operator_count>=2)&&(datafield_count<=3)
```

第八步：decay和truncation选择。这一步的目的是剔除掉一些没有经济学含义，靠着一味调整decay从而实现提交的因子。decay可以选择0,1,3,5,20等有经济学含义的参数。而不是17,29这种没有实质含义的参数。至于truncation，这是为了满足weight分布所做，truncation太高的ppa可能会有weight的warning，从而使得sa的weight不被均匀分布。例：

```
&&(decay<=5)&&(truncation<=0.1)  
```

第九步：universe选择。usa，asi等地区都有illliquid的universe，这些地区的因子大多是靠着低流动性挣钱，会造成maxtrade线和pnl的分歧，在费后表现也没有保障，可以通过universe参数剔除。

```
&&(universe=='TOP2500')
```

第十步：检查选择出的因子。注意：

## **选择过细等于不选择**

## **设置selectlimit不如设置更多的条件**

下边给出一些实例：

(

not(own)&&

((turnover<0.08&&turnover>0.06)

||(turnover<0.13&&turnover>0.11)

)

&&(in(datacategories, "fundamental")

||in(datacategories, "analyst")

||in(datacategories, "model")

||in(datacategories, "news")

||in(datacategories, "other")

||in(datacategories, "risk")

||in(datacategories, "pv"))

&&(operator_count<=8)

&&(operator_count>=2)

&&(datafield_count<=4)

&&((prod_correlation<0.5&&prod_correlation>0.1)

&&(self_correlation<0.4&&self_correlation>0.05))

&&(decay<=5)

&&(universe=='TOP2500')

&&(truncation<=0.1)

)

(in(classifications, "ATOM")&&((neutralization == 'SLOW') || (neutralization == 'FAST') || (neutralization == 'SLOW_AND_FAST') || (neutralization == 'CROWDING') || (neutralization == 'STATISTICAL') || (neutralization == 'REVERSION_AND_MOMENTUM'))

&&(prod_correlation<0.47&&prod_correlation>0.1)

&&((turnover<0.09&&turnover>0.07)

||(turnover<0.15&&turnover>0.13)

||(turnover<0.20&&turnover>0.18))

&&(operator_count<=10)

&&(operator_count>=3)

&&(dataset_count<=4)

&&(universe!='ILLIQUID_MINVOL1M')

&&(decay==0||decay==1||decay==3||decay==5)

&&(truncation<=0.1)

)

仅供参考，祝各位select愉快：）

---

### 帖子 #18: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
- **主帖链接**: https://support.worldquantbrain.com[L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **讨论数**: 73

一句话总结该活动：直接在评论区评论，分享你的模板。

> ```
> 被审核通过者将获得BRAIN纪念品一份（下图背包）优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至8.31日23：59（以服务器时间为准） 
> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> aRNIN
> BRAIN Backpack


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

### 帖子 #19: 【Alpha 灵感】多因子量化选股系列之四：新技术因子的研究与测试
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha 灵感】多因子量化选股系列之四新技术因子的研究与测试_20251795571351.md
- **讨论数**: 1

- alpha 灵感 湘财证券-多因子量化选股系列之四：新技术因子的研究与测试
  - 核心 idea： 本研报对两个传统因子换手率因子和非流动性因子进行了改进。
  - 1 换手率类因子的改进 ： 研报中对传统的换手率稳定性因子进行了改进，定义换手率异变系数因子为 std(最近一段时间换手率序列)/mean(最近一段时间换手率序列)， 表示在一定换手率均值的情况下更好的表现换手率的波动性。我尝试了用数据库中的turnover rate和构造volume/shares(或者sharesout) 来表示换手率，但因子初始效果经过调整后效果很不理想。
  - 2 非流动性因子的改进：研报中对传统的非流动性因子进行了改进，定义改进因子为 mean(最近一段时间日绝对收益率序列)/mean(最近一段时间日成交额序列)。非流动性因子通过单位成交额对绝对收益的影响，来衡量股票交易对市场的冲击，用于刻画股票的非流动性，非流动性越高，流动性风险越大。而改进因子基于成交额对绝对收益的影响具有一段时间的连贯性，可以更好的衡量分子或分母一段时间的缩小或扩大。 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 8,0OOK
> 6,00OK
> 4,00OK
> 2,00OK
> 2013
> 2015
> 2017
> 2019
> 2021

  - 因子调整：由于因子衡量非流动性，故选择非流动性池，并选择行业中性化。基于检测中出现的集中性问题，加入winsorize控制集中性，并使用group_backfill 对NAN值回填行业均值。机器处理：选择多个相关data set进行遍历，替换为oth143_sell_tier1_volume获得了更好的因子表现。经改进后因子通过了测试可以提交 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 12/31/2023 EST
> anonymous
> Add Alpha to a List
> Open alpha details in new tab 
> IS Testing Status
> N
> 11 PASS
> Sharpe of 1.92 is above cutoff of 1.58.
> Fitness of 1.24 is above cutoff of 1.
> Turnover of 27.81% is above cUtoff of 1%.
> Turnover of 27.819 is below cUtoff of 700.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 1.31 is above cutoff of 0.79。
> Most illiquid 50% instruments after cost Sharpe of 1.31 is above cutoff of 0.68 (1.29 original universe after cost Sharpe):
> Self-correlation 0.5452 is below cUtoff of 0.7.
> Prod correlation 0.6334 is below cutoff of 0.7
> Alpha submissions 0 below quota of 4.
> IS ladder Sharpe of 2.94 is above cutoff of 2.37 for ladderyear 2: 2/16/2021...2/17/2019.
> 2 WARNING
> 0
> Performance Comparison
> Last Run:
> Check Submission
> Submit Alpha

  - 后续可能改进方向：研报提到了可以通过市值对数中性化和五组分层进行多空组合。本人不太了解如何使用operator进行这些操作，欢迎大家指导。

---

### 帖子 #20: 【Alpha灵感】 看不见的负担
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】 看不见的负担_19137319051671.md
- **讨论数**: 2

Title：The invisible burden

Author : Xin Liu, Chengxi (Adam) Yin, Weinan Zheng

Year : 2020

Link :  **[[链接已屏蔽])**

**概述：我们研究商誉（并购（M&As）产生的无形资产的重要形式）在资产定价中的作用。 我们发现，商誉与销售额之比对美国股票横截面回报率具有强烈的负向预测作用，尤其是在进行跨行业并购的公司和首席执行官过于自信的公司中。 在调整共同因素后，它仍然是股票回报的经济和统计显着预测因子。 我们的研究结果表明，商誉除以销售额包含了有关公司价值的信息，而股票市场对此信息反应不足，因为商誉的公允价值是不可观察且难以评估的。**

**Alpha idea :**

***主要考虑用*  *Brain*  *平台上的*  *goodwill*  *和*  *sales*  *的比值来构建*  *alpha*  *。***

我们推测GTS高的股票后续回报应该较低。回测的表现与我们的假设一致。

考虑到收购行为不会经常发生且立刻生效，所以把数据在较长时间上取平均值。

所有股票按照  pv13_h2_sector 分组并rank。得到初始的alpha。

```
my_group=bucket(rank(pv13_h2_sector),range="0.1,0.9,0.1");GTS_grouped = -group_rank(ts_mean(goodwill,252)   /ts_mean(sales,252),                          my_group                          ) ;GTS_grouped
```


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
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
> TOPSO0
> Fast Expression
> 0.08
> Subindustry
> Off
> Verify
> 叫
> IS Summary
> Average
> Stage
> 05
> Aggregate Data
> Sharpe
> TUrnover
> Fitness
> RetUrn5
> Draoown
> Margin
> 1.41
> 3.099
> 1.05
> 6.91 %
> 4.48%
> 44.689o0
> Chart
> Pnl
> 3,00OK
> Z,50OK
> ZOOOK
> SOOK
> DOOK
> SOOK
> May '16
> SeP "16
> Ja1'17
> Sep
> Ja0'18
> Maiy '18
> jan '19
> MMay'19
> Sep '19
> '20
> Sep '20
> Jan '21
> May
> Se0
> Nay


虽然可提交但表现一般。

为了进一步提升alpha的表现，我希望改进此alpha的turnover。此时alpha的turnover非常低，我想这应该是alpha错过了许多短期的信号导致的。尝试将原alpha与rank(ts_delta(close,2)) 相乘来反映股票在短期回归均值的趋势。

在加入均值因子后，turnover增加过多，所以考虑增加一些decay来优化alpha。

```
my_group=bucket(rank(pv13_h2_sector),range=“0.1,0.9,0.1”);GTS_grouped=-group_rank(ts_mean(goodwill,252)/ts_mean(sales,252),my_group) ;GTS_grouped * rank(ts_delta(ts_decay_exp_window(close,15,factor=0.4),2)) 
```


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
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
> TOPSO0
> Fast Expression
> 0.08
> Industry
> On
> Off
> Verify
> IS Summary
> Excellent
> Stage
> 05
> Aggregate Data
> Sharpe
> Turnove
> Fitress
> Returns
> Drawcown
> Margin
> 2.20
> 12.599
> 2.16
> 12.109
> 4.16%
> 19.23%o。
> N Chart
> Pnl
> 5,OOOK
> DOOK
> 300OK
> 2.OOOK
> DOOK
> Jan'17
> May'17
> Jan'18
> Jan '19
> 20
> Jan "21
> Nay
> Sep
> Sep
> May
> SeD
> Nay
> Sep
> Nay
> Sep


此时再回顾整个alpha发现使用的主要数据为goodwill和sales，两者在不同行业中表现形式不同，但这个区别已经由group_rank去除。所以Setting中再次做中心化不仅效果不大，而且可能使资金过于平均。
于是关闭了中心化并。最后对alpha各部分做调整（将group换成pv13_h_min24_500_sector），并对最终结果取幂。

```
my_group=bucket(rank(pv13_h_min24_500_sector),  range=“0.1,0.9,0.1”);GTS_grouped=-group_rank(ts_mean(goodwill,252)/ts_mean(sales,63),my_group) ;alpha = GTS_grouped * rank(ts_delta(ts_decay_exp_window(close,10,factor=0.5),2)) +0.4 ;sign(alpha) * power(abs(alpha),2.5)
```


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
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
> TOPSOO
> Fast Exoression
> 0.05
> None
> On
> Off
> Verify
> IS Summary
> Spectacular
> Stage
> 05
> Aggregate Data
> 5harpe
> TUrnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.80
> 14.039
> 3.30
> 47.059
> 36.01%
> 67.059oo
> N Chart
> Pnl
> 15W
> 1OM
> 10/15/2018
> IS Pnl: 7,102.19K
> DOOK
> Majy ' 15
> Sep '16
> Jan '17
> May '17
> Jan "18
> May '18
> Sep '18
> Jan '19
> May
> Sep '19
> May '20
> Sep
> Jan '21
> Sep


最后产生了一个效果不错的alpha

---

### 帖子 #21: 【Alpha灵感】 计数启发法
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】 计数启发法_20237862981399.md
- **讨论数**: 5

西南证券因子选股系列：计数启发法与加权盈利频率


> [!NOTE] [图片 OCR 识别内容]
> Ungeheuer and Weber (2021), Chesney et al. (2019)的研究表明计数启发法的证据有
> 助于推断股票市场 ,
> 而 Holzmeister et al. (2020) and Huberet al. (2019)的研究指出 ,正负
> 收益的频率是投资者收益分布最显著的特征
> 本文在这些研究之上细化投资心理过程 ,本文
> 认为投资者简单关注股票正负收益的频率。并且收益大于一定阈值的天数更能受到关注。
> 第一, 投资者对股票 "正负"  收益的判断标准往往取决于超额收益而不是绝对收益,超
> 额收益为股票收益减基准收益 ,大多数投资者将大盘收益作为基准。例如,当天 Wind 全 A
> 涨 2%,股票 A 当天收益率1%,股票 B当天收益率 3%。对于投资者而言,虽然股票 A 本
> 身收益率为正,但相对大盘有负的超额收益。则投资者往往对当天股票 A 收益的评价为负面
> 而非正面。
> 第二,投资者对股票 "正负" 收益的判断存在阈值。例如 ,股票 A 超额收益 0.05%,从
> 投资者心理角度出发往往认为股票 A 的收益并无较大波动,一般不会将当天股票 A 的正收
> 益计数。
> 基于上述分析 ,
> 假设投资者计算股票前一个回望期每日
> 正收益》 的数量,
> 并根据超额
> 收益大于一定阈值的天数比例进行投资,我们可以得到一个盈利频率指标。盈利频率定义如
> 下:
> Mit
> Zjzl
> fit
> 二
> 其中 Mi [是股票1在第[个回望期的天数, [i ]是股票 j的第 j个日超额收益。
> Iri
> 指示函数, [.]大于U时为1,否则为0。分子表示回望期中 [i.]大于 U的天数之和。
> Irijzu
> Mit
> j表示


取阈值为 2%，取回望期为 40 天。

在此基础上考虑对更近期的收益情况施加更大的权重。

因此，我们对构造的盈利频率进一步优化，采用衰退指数加权，使得最近的收益计数获

得最大的权重，而最远的收益计数获得最小的权重


> [!NOTE] [图片 OCR 识别内容]
> Wj *
> FW
> 'j1
> 芒
> it
> t_j
> 0.52
> (1)
> 我们采用半衰期指数权重 W对 Iri j进行加权。权重因子如式(1)所示,2表示半衰期,
> 取窗口期的一半
> (TI2)
> ' j曰权重为Wdecayj ' tj表示]曰到当前时刻 [的天数。
> Mit
> Irijzu_
> Mit
> Waecayj


采用申万一级行业对因子值进行行业中性化


> [!NOTE] [图片 OCR 识别内容]
> 同时,采用申万一级行业对因子值进行行业中性化:
> 一级行业31个
> 12
> f二
> Industry
> 米
> Ri + a + 8
> 亡L
> 取残差8作为行业中性化后的因子值。


猜想加权盈利频率因子与股票下期收益率负相关，研报给出表现：


> [!NOTE] [图片 OCR 识别内容]
> 图 6:  多空组合净值变化图
> 30
> 25
> 20
> 15
> 10
> 5
> 0
> 8
> 原始因子
> 行业中性化
> 数据来源: Wind,
> 西南证券整理
> 
> 2019-11-19
> 04
> 2010-12-30
> 2011-12-23
> 2013-12-23
> 2014-12-16
> 2015-12-10
> 2016-12-05
> 
> 2018-11-22
> 2020-11-16
> 2021-11-11
> 2022-11-
> 熹


在平台中我使用如下方法表示：


> [!NOTE] [图片 OCR 识别内容]
> Settings 
> CHN/D1/TOP3000
> Convert to
> Multi-Simulation
> 1
> Num
> if_else
> returns
> group_mean (returns , 1,market )-0.01,
> 1,
> 0);
> 2
> Percent
> ts_decay_exp_window (Num ,
> 40,
> factor
> 0.96,
> nan
> True);
> 3
> group_neutralize
> Percent , pvl3_h_minz_sector)


第一行 ：取在过去的40天 个股表现超过大盘2%的个数

第二行： 进行衰减，近期权重更大

第三行： 行业中性化

但是结果却是完全PnL反向变动，这种加+ - 号无法改变，都是向下的


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> -ZOM
> 4OM
> GOM
> 8OM
> 10OM
> 120M
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021


我认为这个计数启发法的模版可以用于其他变量的machine探究，但是我不知道为何此处无法复现研报结果，因此发帖求助

---

### 帖子 #22: 【Alpha灵感】A 股反转之力的微观来源
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】A 股反转之力的微观来源_22071441537303.md
- **讨论数**: 5

【Alpha灵感】A 股反转之力的微观来源

1. 题目：A 股反转之力的微观来源
2. 作者：魏建榕
3. 链接： [[链接已屏蔽])
4. Alpha Idea:

初级版本：


> [!NOTE] [图片 OCR 识别内容]
> 步骤1
> 对选定股票 $,
> 回溯取其过去20日的数据;
> 步骤2
> 计算股票 $每日的平均单笔成交金额
> (成交金额1成交笔数 );
> 步骤3
> 单笔成交金额高的 10个交易曰,涨跌幅加总,
> 记作 M_high;
> 步骤 4
> 单笔成交金额低的10个交易日,涨跌幅加总,
> 记作 M_low;
> 步骤 $
> 理想反转因子 M=M_high-M_low ;
> 步骤6
> 对所有股票,都进行以上操作,计算各自的理想反转因子 M。


后续作者没有使用单出的中位数，而是使用了其他分位数：


> [!NOTE] [图片 OCR 识别内容]
> 表2:
> 新 W 式切割的操作步骤 (以1/16分位为例 )
> 步骤1
> 对选定股票 $,回溯取其过去20日的数据;
> 步骤2
> 计算股票$每日的逐笔成交金额分布的 1/16 分位值;
> 步骤3
> 1/16 分位值高的 10个交易曰,涨跌幅加总,记作 M_high;
> 步骤4
> 1/16 分位值低的 10个交易曰,涨跌幅加总,记作 M_low;
> 步骤$
> 理想反转因子 M=M_high-M_low ;
> 步骤6
> 对所有股票,都进行以上操作,计算各自的理想反转因子 M。


1. Idea分析 
> [!NOTE] [图片 OCR 识别内容]
> 图3:  逐笔成交金额的金字塔 (全部 A股,
> 2013-2018 )
> 半90,000
> A股逐笔成交金字塔
> 半80,000
> 绘图:  开源金工团队
> 半70,000
> 半60,000
> 半50,000
> 90%分位:  45000元
> 羊40,000
> 半30,000
> 809分位:  24000元
> 半20,000
> 平均值: 21000元
> 半10,000
> 中位数:  8000元
> 半0


作者的灵感来源于上面这张逐笔成交金额的金字塔图，其中横向红色柱子的长度代表该金额水平上的成交笔数。 从形状上看，这是一个畸形的金字塔，底部极宽，顶部极窄。其表征的含义是，大 多数被撮合成功的成交，其成交金额都是很小的，中位数在 0.8 万元，2.4 万元是 80% 分位，4.5 万元已经是 90%分位，10 万元以上的成交几乎是凤毛麟角。在图 3 中， 最显眼的红点是金字塔的重心(即平均值)，意义是全部 A 股在此 6 年间的平均每笔 成交金额为 2.1 万，这个金额已接近 80%分位值。

进一步，不妨设想，对于每一个股票、每一个交易日，都分别画一个类似的金字塔(形态会略显毛糙)，W 式切割等于是说: 回看过去20个交易日，然后比较每日金字塔的重心(平均值)高低，取重心高的10 日的涨跌幅加 总得到 M_high，重心低的 10 日则得到 M_low。在这个图象之下，重心代表了交易行为的什么特征呢? 答案是相当模糊的，原因就在于，平均值是一个很弱的统计量，重心(平均单笔成交金额)提高，有可能是因为大单成交增加了有可能是因为小单成交减少了，也有可能是大单被更被更大的大单替代了。换言之，从均值出发，很难反推关于逐笔成交金额原始分布的细节信息。顺着这一思路，为了使W式切割能够得到更多的微观信息，考虑用分位数代替平均值，作为新的切割标准

1. 数据集

可以使用的datafield包括：

**A-shares Trade Data**  :  pv27_s_li_initiativesellamount;

**A-shares Trade Data**  : pv27_s_li_largebuyrate;

**A-shares Trade Data**  : pv27_s_li_entrustbuymoney;

使用的universe:

TOP3000

使用的Neutralization：

Industry

使用的operator：

vec_sum；

ts_sum;

ts_ medium;

ts_percentage;

1. 实现结果： 
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.1812.0292.9222.399
> 1
> 1.84937.279。
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 3.26
> 12.349
> 4.52
> 23.989
> 3.36%
> 38.879600
> 1215
> 1084
> 2013
> 2.34
> 12.10%
> 3.06
> 21.429
> 4.42%
> 35.409o。
> 1292
> 1090
> 2014
> 0.93
> 11.61%
> 0.74
> 7.95%
> 8.37%
> 13.709o。
> 1299
> 1089
> 2015
> 2.58
> 11.86%
> 4.15
> 32.389
> 5.389
> 54.609o。
> 1297
> 1142
> 2016
> 3.82
> 11.999
> 5.88
> 29.609
> 3.529
> 49.39900
> 1457
> 1212
> 2017
> 2.45
> 11.589
> 3.27
> 22.28%
> 5.30%
> 38.499o。
> 1616
> 1364
> 2018
> 4.16
> 12.129
> 7.16
> 37.05%
> 2.64%
> 61.139o。
> 1611
> 1392
> 2019
> 4.89
> 12.28%
> 8.68
> 39.36%
> 3.28%
> 64.099o。
> 1651
> 1351
> Year


---

### 帖子 #23: 【alpha灵感】A股恐慌度因子在美股的应用
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

### 帖子 #24: 【Alpha灵感】A股换手率类因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】A股换手率类因子_18600255773719.md
- **讨论数**: 18

标题：华泰单因子测试之换手率类因子

作者：林晓明

概述：该篇论文作者构建了近N个月每日换手率均值，标准差，及衍生的换手率乖离率等12个基于换手率的因子，首先分析了这些因子行业间的差异以及与市值因子的相关性，然后使用回归法和分层回测等因子测试流程中的因子收益率,t值,IC值等系统地验证了换手率因子在A股市场中的有效性。

Alpha Idea:

直接将论文中构建的因子原封不动的用Fast Expression实现。


> [!NOTE] [图片 OCR 识别内容]
> 图表1:
> 华泰单因子测试一换手率因子及其描述
> 大类因子
> 具体因子
> 因子描述
> turn_Im
> 个股最近 N 个月内日均换手率
> turn_3m
> N=l,
> turn_Gm
> bias_turn_Im
> 个股最近 N 个月内日均换手率除以最近2年内日均换手率
> 再减去1
> bias_turn_3m
> N=l,
> 换手率因子
> bias_turn Gm
> (Turnover
> std_turn_Im
> 个股最近 N 个月内日换手率序列的标准差
> Factor)
> std_turn_3m
> N=l, 3,
> std_turn_Gm
> bias_std turn Im
> 个股最近 N 个月内日换手率序列的标准差除以最近2年内日换手率序列的标
> bias_std_turn_3m
> 准差,
> 再减去1
> bias_std_turn Gm
> N=1, 3,


由于论文中论证了换手率因子的行业差异，所以我们选用Industry中性化，可以看出该alpha表现出明显的信号。


> [!NOTE] [图片 OCR 识别内容]
> 5|?
> S2
> 11
> .
> AESULTs
> LC
> Sotts
> CHIIOTITOPJD00
> 04014 MVU Sonwlatoa
> Chart
> UNcUCT
> 4T1
> Kl L
> Tl
> oCI
> [o
> 1o
> NUIuAUUATI
> 6C8
> AuttArIC
> Int
> UIN
> Utawlt
> APOy
> Urmr
> UTIhrMt +144290
> CAUTTUTTN
> OSU
> 50
> N


*Note: Sharesout is counted in millions on Brain*

*
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> stage
> IS
> 05
> Aggregate Data
> Sharpe
> TUrnover
> Ciness
> Returns
> Orawdown
> Margin
> 2.18
> 5.269
> 3.28
> 28.329
> 22.31%
> 107.64900
> Year
> Sharpe
> Tumover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.95
> 5.5930
> 二91
> 34.62-
> 1.70
> 123.81
> 118
> 73
> 2012
> 2.95
> 5.093
> 一56
> 29.91
> 5.73
> 117.5
> 1519
> 777
> 7013
> 22-
> 5.043
> 3.25
> 26.36-
> 112
> 10_.55
> 1511
> 371
> 2014
> 1.95
> 5.453
> 2-7
> 20.10--
> 7.00
> 73.30:
> 1-91
> 397
> 2015
> 0.03
> 5.753
> 0.02
> 1.09-7
> 22.31
> 3.30:
> 1373
> 10ED
> 2016
> 212
> 5.043
> 3.08
> 26-2-
> 7.30
> 10-.90:
> 1560
> 1009
> 2017
> 3.0-
> 5.313
> 5.36
> -5.517
> 7.15
> 175.17::
> 2016
> 96_
> 2013
> 192
> 一981
> 3.02
> 23.87
> 7.95
> 115,33:
> 2031
> 973
> 2012
> 2.5
> 5.113
> 一49
> 357
> 13.3-
> 141.32:
> 1976
> 1027
> 2020
> 1.43
> 5.373
> 1.33
> 2239
> 10.153
> 33:
> 1952
> 1059
> 7021
> 9-0
> 5.037
> 31.37
> 43372
> 2.301
> 527.62:
> 1971
> 1053
*

因为文中论证了换手率因子与市值的负相关性，所以我对市值进行分组再通过group_neutralize降低市值对换手率因子的影响，可以看出alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> SITUUO !
> SLIZ
> 5T73
> Sukma
> RESULTS
> LSRI
> ed
> OSOOOC
> Chart
> 1881
> Tot
> Ee]
> CO
> 3-
> A
> JOT
> TIII
> MUUTRUIUATWNI@
> TUAATONI@
> &1+1151118
> s
> AaT
> Dlawl
> Noply
> TUTTO 
> Volutsharoscut 1i2
> Rup utrallzt
> SanltUrTOp
> bCetlran (Cap , CanR O.1
> 7TNe
> SCUO
> 7 +
> o( a&
> ssnely



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marain
> 2.67
> 6.069
> 4.29
> 32.219
> 13.469
> 106.25900
> Year
> Sharpe
> Tumover
> Fitness
> Retums
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.21
> 6.319
> 5,45
> 36,133
> 4,6053
> 114,455
> 1394
> 756
> 2012
> 3.23
> 5.761
> 5,65
> 32,999
> 4,499
> 114.565
> 1505
> 791
> 2013
> 2.64
> 5.731
> 一11
> 30.234
> 4.625
> 105.514
> 1503
> 379
> 2014
> 2.92
> 6.2197
> 一-3
> 28,756
> 5.7895
> 92.67.9
> 177
> 910
> 2015
> 1,38
> 6.471
> 2'
> 20,97
> 13,46
> 64.77
> 1330
> 1048
> 2016
> 3.29
> 5.011
> 5,64
> 36,639
> 5.105
> 122.005
> 1634
> 935
> 2017
> 7.31
> 5.041
> 502
> 39,359
> 5,3795
> 131.92
> 1934
> 935
> 2018
> 2.50
> 5.329
> 一.10
> 33,599
> 7.1545
> 115.3
> 1997
> 1007
> 2019
> 3.05
> 5.0317
> 5,-0
> 38,876
> 11,0655
> 128.84
> 1959
> 10-
> 2020
> 1,11
> 6.357
> 1,27
> 16,31
> 9,811
> 51.385
> 1918
> 1093
> 2021
> 6.11
> 5.791
> 17,03
> 97.133
> 2.1455
> 335.72:
> 1952
> 1062


文章还对换手率因子进行了样本期长度的敏感性测试，发现用5天左右的长度能使回归因子收益率以及IC,IR达到最佳。所以，我将alpha的样本期长度从一个月（22个交易日）改为5天，可以看到alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> o
> CATCIN
> Chart
>  Uwcuo
> to
> Fg Ce
> CU
> ] [If
> Cggo
> SUIUAOe
> 62C
> TRUNCATION
> Isty
> UO1
> MA Mo
> Uul
> NOy
> Irmw
> Taloshriyt +111:
> RTO FutrT-LCnurmer,5
> LUCtTane (CAPI,
> TNRC
> N
> SCUO
> *0



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> TurnoVer
> Finess
> Relurns
> Drawdown
> Margin
> 2.90
> 13.989
> 4.81
> 38.449
> 10.049
> 55.01%00
> Year
> Sharpe
> Tumover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.27
> 13.743
> 5.57
> 39,84
> 4,73
> 57,99
> 117
> 733
> 2012
> 3.78
> 13.635
> 6.38
> 38,845
> 4.101
> 55.995
> 1525
> 771
> 2013
> 3.15
> 12.539
> 5.11
> 33.-0
> 5.10*
> 52.66*
> 1525
> 356
> 2014
> 2.32
> 14,321
> 3.39
> 23.14
> 5.369
> 37.975
> 143
> 90
> 2015
> 2,13
> 15.233
> 31
> 31,095
> 7,081
> 10,8
> 1373
> 1065
> 2016
> 3.33
> 13.883
> 5.71
> 39.365
> 5.055
> 55.71
> 1695
> 97_
> 2017
> 2.79
> 13.239
> 一91
> 41.16
> 10.0_95
> 62.01
> 1992
> 935
> 2018
> 3.30
> 13.161
> 6.15
> 45.72
> 6.5193
> 69.505
> 2010
> 99
> 2019
> 3.79
> 13.691
> 7.50
> 53.545
> 9,89
> 78.22*
> 1989
> 101
> 2020
> 114
> 13.91
> 1-1
> 21.3355
> 9.3555
> 30.67
> 195-
> 1057
> 2021
> 5.62
> 12.439
> 15.11
> 90.33
> 1.2235
> 125.334
> 1973
> 1046


最后，文中描述如果从收益率的角度来说换手率和换手率序列标准差较好，如果从稳定性的角度来说换手率的乖离率和换手率序列标准差的乖离率较好。


> [!NOTE] [图片 OCR 识别内容]
> Sattos
> CUTITTIISOINO
> Kogat
> Chart
> T-
> TTMT T
> Tn504
> LUT
> UCI
> TI
> SITAIATO
> TUtCATIC
> UJU
> LTTTIo
> TeTa
> 
> II
> Ug
> TITT
> To4rMJ
> Il
> (_*d_de(tu noer 51/1_Jtd_do(tumer 500)1;
> OTTuT AIIIsIIa
> UUCLAICaN(Ca !
> 0]; ,0.19;
> T
> 50
> 750
> IUTCI1
> 5Pnl 1TOI
> Urto
> +a



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> 05
> Aggregate Data
> Sharpe
> Turnover
> Finess
> Returns
> Drawdown
> Margin
> 2.96
> 26.899
> 2.98
> 27.339
> 12.389
> 20.329000
> Year
> Sharpe
> Turnover
> Fitness
> Returs
> Drawuown
> Margin
> Long Count
> Short Count
> 2011
> 2.30
> 26,479
> 2.53
> 24.209
> 3.749
> 13.285
> 1413
> 737
> 2012
> 3.97
> 26,019
> 1,24
> 29.613
> 3.6330
> 22.775
> 1519
> 776
> 2013
> 3.35
> 27,554
> 3.35
> 27.584
> 3.333
> 19.95,。
> 1530
> 852
> 2014
> 2,11
> 27,459
> 1,43
> 13.5130
> 4,303
> 9.345
> 1521
> 366
> 2015
> 2.83
> 29.985
> 3,05
> 33.33
> 12381
> 222-5
> 148-
> 95
> 2016
> 4.15
> 26.599
> 4.89
> 35.94
> 一459
> 27.79
> 1719
> 950
> 2017
> 2.65
> 25,39北
> 2.72
> 26.753
> 5.2030
> 21.075
> 1953
> 1022
> 2018
> 一7
> 25.269
> 一95
> 3577
> 2.903
> 2332
> 1992
> 1012
> 2019
> 1,23
> 26,549
> 5.13
> 39.07
> 3.3635
> 29.344
> 1962
> 1040
> 2020
> 0.27
> 27,459
> 0,03
> 3.2035
> 9.1930
> 2.335
> 1935
> 1075
> 2021
> 2.37
> 27.179
> 2.93
> 29.533
> 1.729
> 21.72
> 1969
> 1055


从结果可以看出，虽然换手率乖离率因子的收益率不如换手率因子，但是该因子在更多的年份有更小的Drawdown, 因而有更平滑的PnL曲线和更高的Sharpe，与论文中的结论一致。

相关数据集：Price Volume Data for Equity

疑问与讨论：

1. 换手率因子如果在A股市场验证有效，是否在其他市场也是有效的？
2. 有什么方法可以进一步改进换手率因子Alpha使其可以达到Robust Universe Return?


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> 05
> PASS
> FulL
> Robust universe rerurns Of 10.7896Is below CutOff of 15.3896 (~095 OfAlohaj。
> WARNING
> 3 PENDING


---

### 帖子 #25: 【Alpha灵感】Improved Version of "Attention: Implied Volatility Spreads and Stock Return"
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Improved Version of Attention Implied Volatility Spreads and Stock Return_21120326355479.md
- **讨论数**: 1

- 论文概述：使用SEC的EDGAR日志文件中新颖直接的投资者关注度衡量方法，研究者重新检验了通过投资者关注度视角的看涨-看跌隐含波动率差对股票回报的可预测性。研究发现，随着投资者关注度的提高，波动率差的回报预测性变得更加明显，这为信息交易假说提供了有力的证据，而不是错误定价假说。更重要的是，研究记录了基于波动率差和高关注度的投资组合的构建和盈利能力。一个在最受投资者关注和波动率差最大的股票上做多，在最受关注和波动率差最小的股票上做空的投资组合，能够产生2.43%的月度Fama-French 5因子alpha值。
- 论文链接： [[链接已屏蔽])
- 核心idea：投资者关注度较高的股票，若同时出现较大的期权implied volatility的spread，则有可能为informed trader在进行提前买入期权以获得最大化收益，可以预计股票在未来一段时间内走高
- 期权波动率数据选取：  opt4_call_vola_30d ，opt4_put_vola_30d 等不同期限的期权波动率数据
- 交易者关注度数据选取：brain平台具有类似SEC的EDGAR日志文件的data field Search Engine Data，但由于其coverage的时间极为短暂，仅在2021年后有大量数据，故需要采取替代数据以量度交易者关注度，本次论文选取 交易热度因子： volume/cap，与交易者情绪因子：mws85_sentiment 来取代交易者热度因子
- 该论文并未回测策略，故在其中并未找到Universe: TOP 200 or Neutralization
- 核心Alpha的 Expression1: (设置交易热度的threshold)

```
ratio_1 = rank_by_side( opt4_put_vega_60d - opt4_call_vega_60d);ratio_2 = rank(volume/cap);ratio_1 * ((rank(ratio_2 )>0.9))
```

- 核心Alpha的 Expression 2:(设置期权spread的threshold)

```
ratio_1 = rank_by_side( opt4_put_vega_60d - opt4_call_vega_60d);ratio_2 = rank(volume/cap);ratio_1 * ((rank(ratio_1)>0.9) || (rank(ratio_1)<0.1)) * ratio_2 
```

- 回测表现：
- Expression1 在如下setting的情况下，取得的最好表现为：


> [!NOTE] [图片 OCR 识别内容]
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILLIQUID_MINVOLIM
> NEUTRAUIZATION
> DECAY
> TRUNCATION
> Market
> 0.04
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> SaVe a5 Default
> Apply



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.77
> 53.739
> 1.26
> 27.149
> 39.33%
> 10.109oo
> Year
> Sharpe
> TuIOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 4.12
> 47.82%
> 4.47
> 56.289
> 7.01%
> 23.539600
> 1724
> 228
> 2013
> 1.34
> 45.73%
> 0.77
> 15.03%
> 5.78%
> 6.579600
> 1857
> 2012
> 3.52
> 57.11%
> 3.18
> 46.509
> 7.25%
> 16.299300
> 1724
> 448
> 2015
> 3.55
> 61.24%
> 3.18
> 48.99%
> 7.18%
> 16.00960o
> 694
> 2016
> 0.50
> 62.9495
> 0.25
> 10.55%
> 19.1395
> 3.359300
> 1372
> 759
> 2017
> 0.19
> 56.23%
> 0.04
> 2.249
> 11.849
> 0.809300
> 719
> 1356
> 2018
> 1.04
> 52.9395
> 0.52
> 13.119
> 9.25%
> 4.959300
> 1572
> 2019
> 1.57
> 49.27%
> 1.04
> 21.77%
> 13.73%
> 8.849600
> 905
> 1232
> 2020
> 0.52
> 51.34%
> 0.26
> 12.78%
> 24.09%5
> 4.989600
> 1544
> 550
> 2021
> 2.19
> 51.90%
> .86
> 37.29%
> 20.60%
> 14.379600
> 2151
> 329
> 2022
> 7.59
> 57.9695
> 12.44
> 151.749
> 249
> 52.369600
> 2510
> 158



> [!NOTE] [图片 OCR 识别内容]
> PASS
> 2 FALL
> Most illiquid 50% instruments after cost Sharpe of 0.75 is below cutoff of 0.79 (1.51 original universe after cost
> Sharpel
> IS ladder Sharpe of 1.56 is below cutoff of 1.58 for ladder year 2: 1/24/2022...1/25/2020。
> WARNING
> 3 PENDING


- Expression2 在如下setting的情况下，取得的最好表现为：


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILLIQUID_MINVOLIM
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 0.04
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> Apply
> 5aVe 35 Default



> [!NOTE] [图片 OCR 识别内容]
> Start Date
> Snarpe
> Turhover
> Fitness
> Returns
> Drawdown
> Margin
> 01/23/2022 Cr
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> 05/15 Ratio
> Pre Close Sharpe
> PreClose Ratio
> Self-Correlation
> Year
> Sharpe
> TUIOVeT
> Fitness
> Returns
> DrawdOwn
> Margmn
> Long Count
> Short Count
> 2012
> 4.67
> 50.90%
> 3.85
> 34.5795
> 4.20%
> 13.589600
> 1595
> 359
> 2013
> 2.09
> 55.25%
> 0.98
> 12.159
> 2.2796
> 4.40960o
> 634
> 378
> 2014
> 5.51
> 61.00%
> 429
> 36.9595
> 4.38%
> 12.1
> 90o
> 1579
> 593
> 2015
> 4.44
> 62.7695
> 3.16
> 31.6990
> 4.24%
> 10.
> 090o
> 622
> 543
> 2016
> 1.55
> 64.,09%
> 0.76
> 15.4795
> 8.72%
> 4.839600
> 531
> 501
> 2017
> 0.71
> 57.85%
> 0.20
> 4.68%
> 3.73%
> .629600
> 1579
> 497
> 2018
> 2.89
> 49.21%
> 23.10%
> 5.22%
> 9.399600
> 1762
> 435
> 2019
> 47.1495
> 0.34
> 7.6795
> 73%
> 3.259600
> 1730
> 407
> 2020
> 56.46%
> 0.77
> 17.1795
> 849
> 0830o
> 1477
> 518
> 2021
> 2.36
> 54.23%
> 1.52
> 22.48%
> 8.28%
> 8.299600
> 1858
> 522
> 2022
> 6.50
> 53.80%
> 7.85
> 78.53%
> 0.96%
> 29.19900
> 2185
> 483


（该因子已提交）

- 思考：该因子主要从detect informed trader的角度进行思考，并对option implied volatility 所提供的信号进行进一步的优化，进而得到了有效因子。本文作者由该模板，从不同角度思考后提取出满足提交条件的两个有效因子。而detect informed trader 在中国市场应有着更加重要的作用，但需对隐含波动率与交易者热度两个基础因子进行一定程度的替代，正如本文前半部分所做的那样，该潜在扩展有待读者深思。
- 代码总结反思： 进行2450次参数调优与数据替换的simulation，共用时两个小时，暂时未发现性能局限，故短时间内将保持原模板。平台将自动统计因子表现，故在因子同质的基础上，建议直接使用sharpe/turnover排序选取最有效的因子，而非耗费时间在提取因子回报上

---

### 帖子 #26: 【Alpha灵感】JACKPOT因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】JACKPOT因子_21119177808663.md
- **讨论数**: 1

论文标题：Death and jackpot: Why do individual investors hold overpriced stocks?,

引用出处：

Conrad, Jennifer, Nishad Kapadia, and Yuhang Xing, 2014, Death and jackpot: Why do individual investors hold overpriced stocks?, Journal of Financial Economics 113, 455–475.

核心idea：

"Jackpot"是一个特定的指标或条件，用来描述一家公司在连续12个月（从t+1到t+12月）的复合回报率达到或超过100%时。如果满足这个条件，那么"jackpot"的值为1，否则为0。

对于在接下来的12个月内退市的公司，如果没有完整的12个月数据，那么会使用可用的月份数据来计算回报率，并且会对任何在CRSP（中心研究共享计划）上报告的退市回报进行调整。这意味着，尽管公司可能没有完成整个12个月的运营或因为退市而提前结束，但它们的回报率仍然可以根据实际运营的月份来评估，并根据其退市时的回报进行相应的调整。

简而言之，"jackpot"是一个用于衡量公司在特定时间内是否实现极高回报率的指标，反映了公司在该期间的财务表现是否异常突出。

关于数据：

我目前可以找到最有价值的信息是针对于US stock market，非小范围eg.TOP200.

核心alpha expression:

我觉得本文最大的创新性就是提出了一个异常衡量指标叫Jackpot。根据其定义，转换为brain fast expression有：

// 计算过去12个月的连续复合回报率

compound_return = power(1 + returns, 12) - 1;

// 判断是否达到100%的回报率，是则为1，否则为0

jackpot_indicator = if_else(compound_return >= 1, 1, 0);

绩效：

上面的indicator用在哪里/与谁结合给了模板挖掘很大的空间，这里我跳出了文献的研究范围，为了简单，研究了与RETURN结合的效果，需要调参以通过corr检验，并且成功找到一个可以提交的alpha：


> [!NOTE] [图片 OCR 识别内容]
> SHIR E
> ITUUESS
> IROVBR
> IROVBR
> TED_RIOUERSE_SHQUID_UNSRELATIORRELATIOLLBUISSIOIPETIT虫
> THISER_SIARPIodel
> Pss
> P155
> P55
> P155
> Pss
> PuSS
> P455
> PEMDINC
> PEMDING
> P55
> TRING
> TARMING
> FIL
> UGGEL
> PSS
> PHSS
> PJSS
> PSS
> PSS
> PASS
> PASS
> PENDING
> PEIDIIC
> PASS
> KARVING
> IARING
> FAIL
> L:QRaPpg
> Pss
> PSS
> Pss
> PASS
> Pss
> PASS
> PSS
> PEMDIG
> PEMDING
> PSS
> TARTING
> TRIMG
> PSS
> ddqazi
> PJSS
> PsS
> P455
> PJSS
> PSS
> PisS
> P4S5
> PEMDIIC
> PEMDIUC
> PASS
> IRIuC
> IARINC
> FAIL
> 02oPGC
> 56 PSS
> Puss
> Pss
> PsS
> Pss
> PSS
> PSS
> PEDING
> PENDING
> PSS
> TRING
> TARMING
> FIl
> fliegop
> P4S5
> PusS
> P4S5
> PJSS
> PHSS
> PASS
> PASS
> PEIDIIC
> PEIDIIC
> PASS
> TARIC
> IARIIC
> FAIL
> El:3QRSJ


这里是提交了alpha后的截图，所以corr肯定过不了了


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 8 PASS
> Sharpe of 2.12 is above cutoff of 1.58.
> Fitness of 1.86 is above CUtOff of 1.
> Turnover Of 56.6296 is above CUtOff Of 196.
> Turnover of 56.6296 Is below CUtoff of 7096
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 1.52 is above cutoff of 0.87.
> Most illiquid 5096 instruments after cost Sharpe Of 1.7 is above cutoff of 0.99 (1.89 original universe after cost
> Sharpe)。
> IS ladder Sharpe of 2.61 is above CUtoff of 2.37 for ladder year 2: 1/23/2022。
> 1/24/2020.
> WARNING
> 3 PENDING
> Self-correlation check pending
> Production correlation check pending:
> Alpha submissions quota check pending:



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.12
> 56.629
> 1.86
> 43.709
> 22.669
> 15.44900
> Year
> Sharpe
> Trover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2012
> 3.36
> 58.6296
> 3.56
> 65.6696
> 8.3596
> 22.209023
> 998
> 626
> 2013
> 1.75
> 58.6196
> 1.28
> 31.409
> 17.0196
> 10.71903
> 1153
> 729
> 201
> 3.6-
> 58.0990
> 3.94
> 68.1190
> 7.7796
> 23.45903
> 1291
> 832
> 2015
> 1.79
> 56.9090
> 1.31
> 30.539
> 9.0690
> 10.7390
> 1357
> 857
> 2016
> 0.90
> 57,0396
> 0.53
> 20,0890
> 17.1396
> 7,0490
> 1334
> 856
> 2017
> 1,81
> 56,95%
> 1,42
> 35,0596
> 12.5696
> 12.319030
> 1272
> 894
> 2018
> 2.29
> 56.8496
> 1.92
> 40.8596
> 14,49%6
> 14.37905
> 1364
> 851
> 2019
> 0.98
> 54.4996
> 0.63
> 22.2796
> 14.0896
> 7903
> 1379
> 813
> 2020
> 2.70
> 55.2296
> 2.92
> 65.539
> 17.7196
> 23.729023
> 1467
> 705
> 2021
> 2.24
> 53.93960
> 2.28
> 55.669
> 10.1696
> 20.629o3
> 1569
> 768
> 2022
> 5.30
> 50.1196
> 7.03
> 88.2490
> 2.0296
> 35,22903
> 1701
> 836



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 12/30/2021
> Pnl: 42.81M
> 3ON
> ZOM
> TON
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022


---

### 帖子 #27: 【Alpha灵感】Non-Linear Factor Returns in the U.S. Equity Market
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Non-Linear Factor Returns in the US Equity Market_21126691730839.md
- **讨论数**: 1

论文标题：Non-Linear Factor Returns in the U.S. Equity Market

论文链接： [[链接已屏蔽])

从论文的研读和实现，花了不少时间。中间又借助于ChatGPT去理解一些金融概念。所以，都分享在这里。

## 摘要：

We examine non-linear return-to-characteristic relationships for five equity market factors: Value, Momentum, Small Size, Low Beta, and Profitability. Our research employs monthly returns and characteristics for the largest one thousand U.S. stocks from 1964 to 2023 with a focus on average active returns over the last twenty years. Beyond simplicity in modeling the return generating process we find no reason to assume a linear relationship between characteristics and security returns. Allowance for non-linearity leads to increases in Information Ratios for factor portfolios neutralized with respect to non-linear as well as linear exposure to the other factors. The return to the pure Profitability characteristic across stocks is highly non-linear, as is the alpha return within the Low Beta portfolio. Non-linearity of the Small Size return across the largest one thousand stocks is complex and changed around the turn of the century. Over the last twenty years, the return to earnings yield has been flat across the entire Value spectrum.

这篇论文研究了 **五个股票市场因子（价值、动量、小盘股、低贝塔和盈利能力）** 与回报之间的非线性关系。研究使用了1964年至2023年 **美国最大一千家股票** 的月度回报和特征数据，重点关注过去二十年的平均主动回报。在对回报生成过程进行简化建模的基础上，研究发现没有理由假设特征与证券回报之间存在线性关系。对非线性的允许导致了在与其他因素的非线性以及线性敞口中中性化的因子投资组合的信息比率增加。在股票中，纯盈利特征的回报非常非线性，低贝塔投资组合内的阿尔法回报也是如此。在最大的一千支股票中，小盘股回报的非线性复杂，并在世纪之交左右发生了变化。过去二十年中，整个价值范围内的盈利收益率保持不变。

我对于Beta不是理解接，所以，搜了一下，如下。

### 贝塔Beta的概念 - 来自ChatGPT

在金融领域，贝塔（Beta）通常用来衡量一个资产或投资组合相对于市场整体的价格波动情况。贝塔值大于1表示资产或投资组合的价格波动幅度较市场更大，而贝塔值小于1则表示波动幅度较市场小。

低贝塔（Low Beta）指的是那些相对于市场整体波动较小的资产或投资组合。这类资产可能受市场波动的影响较小，通常被认为具有相对较低的风险。投资者可能会将低贝塔资产纳入他们的投资组合，以寻求更加稳定和相对低风险的回报。

举例来说，假设有一支股票的贝塔为0.8，而市场整体的波动为1.0。这表示该股票相对于市场整体的波动较小，它的价格相对稳定。如果市场上涨1%，那么该股票可能只会上涨0.8%，而如果市场下跌1%，该股票可能只会下跌0.8%。这种相对较小的波动特征使得该股票被认为是低贝塔资产。

- 低贝塔股票：
- - 优势： 低贝塔股票通常相对较稳定，波动性较小，适合那些追求相对低风险、稳定回报的投资者。
  - 劣势： 在市场上涨时，低贝塔股票可能表现相对较弱，因为它们的涨幅通常小于市场平均水平。
- 高贝塔股票：
- - 优势： 高贝塔股票在市场上涨时可能表现更为出色，其回报通常高于市场平均水平。
  - 劣势： 高贝塔股票在市场下跌时可能波动较大，风险相对较高，不适合所有投资者，尤其是那些追求资产保值和相对低风险的投资者。

## 公式

文字提到了线形公式，最后证明很多东西线形公式是无法解释的。这个公式和Fama French factor model类似。通过对其中2个factor的复现，信号是有的，但是远远无法满足需求。


> [!NOTE] [图片 OCR 识别内容]
> Linear Fector PortfolioReturns
> This section introduces econometric methodologies used throughout the paper icluding
> multivariate linear regressions, and then presents the results for non-linear cubic regressions。
> The
> five-factor Fama and Macbeth (1973) linear regression specification is
> ri = GSi,i+C2Sz,i +C3S3,i +C4
> +Cs Ss,i + 8i
> SAi


这个公式的解读：

这五组分数分别对 **应于盈利收益率（即倒数的滚动市盈率）、对数价格动量、负对数市值、负的滚动36个月市场贝塔以及前一年度的毛利率** 。 The five sets of scores in Equation 1, are standardized characteristics to earnings yield (i.e.,  **inverse trailing P/E** ),  **log price momentum** ,  **negative log market capitalization, negative trailing 36-month market beta, and prior-year gross-margin** .

这些特征每个月都进行横截面标准化，使其成为加权均值为零、单位方差的变量。标准化的目的是使得这些特征在横截面上具有可比性，即它们的尺度相同，便于进行比较和分析。

之后，作者又给出了非线性公式


> [!NOTE] [图片 OCR 识别内容]
> NgnLinearFactor PortfolgRetrng
> Non-linear returns within factor portfolios Use an expansion Of Equation
> 1 tat includes
> orthogonalized squared and cubed characteristic scores for each factor. The non-pure single-factor
> portfolio regression specification is
> ri =
> 18+2.32+2383 +81
> where $; is the scored characteristic, and $2 is based on the squared characteristic。
> As described
> j the Technical Appendix, the squared characteristic is analytically orthogonalized to the linear
> SCOre。
> making
> 让
> cross-sectionally
> uncorrelated.
> The
> cubed
> characteristic。
> 83
> is jointly
> orthogonalized to both the linear score and squared characteristics。
> The squared and cubed terms
> 讥 Equation
> 3
> are rescored after orthogonalization to
> 8
> weighted
> mean Of zero and
> weighted
> Variance Of one。
> Ihe orthogonalization process adds precision to the examination Of non-linear
> return
> patterns using cubic regressions because the right-hand side variables would otherwise be
> highly correlated leading to larger correlations in realized portfolio returns. Specifically, the slope
> coefficients,
> 4
> 22
> and
> 33 边 Equation
> 3
> are
> equivalently estimated by three individual
> univariate regressions。
> As with Equation 1 , an intercept term i included is exactly zero, Or equal


重点是，非线性公式不再是5个factor的组合，而是一个factor构成的非线性公式。所以，理论上，可以使用5个factor，构成5个非线形公式 - 5个alpha 策略。

需要注意的是，作者在Appendix中，给出了非线形公式的详细推导，如下


> [!NOTE] [图片 OCR 识别内容]
> The cubed score transformation that is orthogonal to just te linear Score is
> 8
> bit more
> complicated to solve algebraically but can be shown to be
> 8;
> Kurt Si
> Skew
> 83i
> 1/2
> (Tail
> 
> Skew?
> (A15)
> The cubed score transformation that is jointly orthogonal to both the linear score and the squared
> transformation s2i in involves substantial algebra, but can be solved as
> 8
> 一
> Kurt Si
> Skew-Y (52
> 
> Skew -1)
> 831
> 1/2
> (A16)
> Tail
> 
> -Y (Kurt - 2 Skew + Skew-l))
> Hyper
> Skew (Kurt -1)
> Where
> 7
> 一
> (A17)
> Kurt
> 
> Skew? -1
> For example, for a normal distribution with Skew
> 二
> 0, Kurt = 3,
> Hyper
> 二
> 0, and Tail
> 二
> 15,both
> Equations A15 and 416 both simplify to
> Kurtz
> Kurtz
> Skew?
  
> [!NOTE] [图片 OCR 识别内容]
> We first derive a transformation of squared score thatis orthogonal to linear score and has weighted
> ZerO mean and unit Variance。
> With some algebra it can be shown that
> 8
> Skew $;-1
> 82i
> 1/2
> (A13)
> Kurt
> 
> Skew -1)
> has these properties. For example, for a normal distribution with Skew = 0 and Kurt = 3, Equation
> A13 simplifies to
> 82i =
> 疙(?-》
> (A14)


## alpha相关

USA TOP3000 （虽然abstract说作者是用的1000家美国最大股票，实际TOP3000表现更好）NEUTRALIZATION：Slow Factors

数据集可以是5类，如论文所述（已黑体）。我选用了P/E类的数据和Price Momentum，分别构建了2个非线形公式，信号都非常强烈，几乎是可以直接提交的程度。

- P/E: anl69_best_pe_ratio

可能由于P/E数据太过于热门，correlation是一个很大的问题。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> egate Data
> TUTTOTPI
> FTness
> Returns
> ROIO
> Warain
> 3.55
> 50.14%
> 1.50
> 9.00%
> 4.15%
> 3.599oo
> Year
> Turnover
> Fitness
> Returns
> Orawdown
> Margin
> Long Count
> Count
> 2012
> 50.8130
> 2.92
> 12.22%
> 0.509
> 4.812
> 1525
> 1533
> 2013
> 50.853
> 2.85
> 10.75%
> 0.559
> 4.23wee
> 1535
> 1553
> 2014
> 50.1330
> 54%
> 2.219
> 61%a
> 1533
> 1553
> 2015
> 50.23%0
> 67%
> 5795
> 3.45pe
> 1570
> 1557
> 2016
> 4.33
> 50.183
> 3.48%
> 059
> r
> 1562
> 1555
> 2017
> 4.42
> 51.6030
> 1.70
> 63%
> 059
> 96 
> 1543
> 1557
> 2018
> 1.74
> 50.3330
> 0.48
> 89%
> 1.759
> 54ee
> 1549
> 1570
> 2019
> 49.405
> 7.049
> .499
> 8Soe
> 1553
> 1554
> 2020
> 2.75
> 49.11%0
> 1.31
> 11.09%
> 4.159
> 5Zew
> 1555
> 1545
> 2021
> 3.24
> 48.755
> 12.47%
> 349
> 1Ze
> 1547
> 1601
> 2022
> 49.713
> 2.53
> 07骀
> 559
> OGev
> 1520
> 1623
> ABSr
> SIPC
> Sharpe
> Shoft



> [!NOTE] [图片 OCR 识别内容]
> 心耻
> 鬯A
> Simulate
> Alphas
> Data
> 舀 Competitions (4)
> Events
> Learn
> 呆 Refer
> friend
> Simulation
> Simulation 2
> CODE
> RESULTS
> LEARN
> DuT4
> Settings
> USA/D1/TOP3000
> Conyert to Multi-Simulation
> Correlatlon
> Self Correlation
> Tlahesc
> LaSt RUn
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> Prod Correlation
> Hlghest Correlatlon
> LaSt RUn
> REGION
> UNIVERSE
> DELY
> USA
> TOP3OO0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> IS Testing Status
> SIow Factors
> 0.1
> PASS
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> FAIL
> YEARS
> MONTHS
> Verity
> Off
> Prod Correlation
> 868715 above Cutoff ot 0.7and Sharoe not better by 10.055 Ormore。
> WARMNC
> Saye as
> Default
> Apply
> Performance Comparison
> LaSt RUn
> Properties
> Last SaVeJ SUn, 02104'2024
> 11.00 PN
> Name
> Category
> Currently 'anonymOlls'
> NOne
> Clonethis Alphain
> newtab
> Cannot submit Nlpha: 
> test failed


改进：之后，我通过grouping，成功提交了基于P/E的alpha。

感慨一下写出那些数学公式的人，竟然真的可以创建出一个还可以的alpha。

---

### 帖子 #28: 【Alpha灵感】Option-Implied Volatility Measures and Stock Return Predictability
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Option-Implied Volatility Measures and Stock Return Predictability_21110734836887.md
- **讨论数**: 2

论文题目：Option-Implied Volatility Measures and Stock Return Predictability
by X Fu, YE Arisoy, MB Shackleton, M Umutlu - academia.edu

论文概述：文中作者通过构建三大类衡量波动率价差构建的思路来构建交易策略,这三大类包括了call和put波动率价差, OTM call/put和ATM call/put隐含波动率价差以及隐波和实波价差。作者后续基于这三大类价差，又构建了六种不同的价差计算方式：
（1）IVatm,call-IVatm,put

（2）IVotm,put-IVatm,call

（3）[(IVitm,put+IVotm,call)-(IVitm,call+IVotm,put)]/2

（4）IVotm,call-IVatm,call

（5）IVotm,put-IVatm,put

（6）RV-IVatm

最后作者根据价差高低进行排序构建多空交易策略

数据集：Volatility Data，Implied Volatility and Pricing for Equity Options

其中包含了很多不同的volatility和implied volatility的类型可供选择，如opt4_273_put_vola_delta30，表示虚值0.3期限为273的put

根据论文中作者提供的spread构建思路对这些符合条件的数据遍历，并对alpha进行cap，volume中性化处理，可以得到符合提交要求的alpha


> [!NOTE] [图片 OCR 识别内容]
> 15M
> 12.5M
> 1OM
> 7,50OK
> 5,0OOK
> 05/14/2014
> IS Pnl: 4,605.85K
> 2,5OOK
> 2014
> 2016
> 2018
> 2020
> 2022



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.3636.72%1.6317.589610.4899.579600



> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Highest Correlation
> Last Run: Sun, 02/04/2024,11:33 PM
> 0.6
> 1OOM
> TM
> -0.2.-0.1
> 鬓
> Alphas: 19 895
> 1Ok
> 昱
> 皂
> 100
> 01
> 0@0?
> 09
> 0?
> ~
> 0.
> O'
> 0
> ~0.8
> 0.6
> 0.5
> ~0.4
> 0.2.
> -0.7.


---

### 帖子 #29: 【Alpha灵感】Research Paper 22 Overnight returns, daytime reversals, and future stock returns
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Research Paper 22 Overnight returns daytime reversals and future stock returns_20239918193303.md
- **讨论数**: 1

两种不同的客户往往主导着隔夜和日间交易时段，这两种投资者群体的持续过剩需求可能会造成每天的“拉锯战”，导致两个时期的回报逆转模式反复出现。例如，隔夜客户的过度需求可能倾向于将价格拉向一个方向，最终导致开盘价格与相反客户的观点不一致。因此，这些持反对意见的客户可能会在日间交易中拉回价格，并在当天收盘时出现交易日逆转。


> [!NOTE] [图片 OCR 识别内容]
> Close
> ?
> RET_OCid
> Open
> 1
> Pid
  
> [!NOTE] [图片 OCR 识别内容]
> 1十
> RET_
> 1
> I+RET_OCid
> RETid
> COid


先通过日间间隔、日内开收盘价算出daytime returns 和overnight returns

将 一个a negative daytime reversal 定义为 a positive overnight return that is followed by a negative  daytime return.

计算负逆转negative daytime reversal 的天数与第t个月的总交易日数的比率，并将该变量表示为NR

而负反转的异常频率AB_NR =  NR除以过去12个月的NR

最终作者指出，由于在daytime 交易者的过度反应，AB_NR越高，未来回报越高


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAN
> Simulate
> Alphas
> Data
> " Competitions (2)
> Events
> Learn
> y
> Refer a friend
> Simulation 10
> Simulation 5
> Simulation 9
> Simulation 12
> Simulation 13
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation
> 1
> RET_OCplUSI
>  (close) / (open) ;
> Chart
> Pnl
> 2
> RET_OC
> RET_OCplusI
> 1;
> 3
> RETplUSI
> (close) / (ts_delay (close,1) ) ;
> 4
> RET_CO
> (RETplusI / RET_OCplus1 )
> 1;
> 5
> # We define
> negative daytime
> reversal
> as
> positive overnight
> return that
> is
> 9,00OK
> followed by
> negative daytime
> return.
> NUM
> if_else(and ( RET_CO
> 0, RET_OC
> <
> 0),
> 1, 0);
> 8 0OOK
> NR
> Sum(NUM,
> 20)/20;
> 8
> AB NR
> NR/ts_mean (NR,
> 240);
> #stocks
> involved
> in
> more
> intense tug of
> War,
> proxied by
> higher monthly
> 7,00OK
> frequency of
> these negative daytime reversals,
> have significantly higher future
> returns.
> 6,00OK
> 10
> 0.5xrank (-returns ) +0.5*rank
> AB NR)
> 5,00OK
> 4 0OOK
> 3,00OK
> Z,0OOK
> 1,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Clone this Alphain a new tab
> Example
> SMate
> Visualization
> $
> Add Alpha to
> List
> Check Submission
> Submit Alpha 
> MM
> tS_s


最后得出的alpha ，但这个alpha 需要和-returns（或者其他指标）拼在一起才能提交，但是他的corr很高，之前被别人提交过


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAN
> Simulate
> Alphas
> Data
> " Competitions (2)
> Events
> Learn
> y
> Refer a friend
> PROD CORRELATION:
> Maximum Pearson correlation coefficient from
> Simulation 10
> Simulation 5
> Simulation 9
> Simulation 12
> Simulation 13
> comparing a given alpha to all other alphas
> LEARN
> DATA
> ANOIYIOUS
> TOPSUUO
> submitted byall WorldQuant BRAIN users
> 2./9
> 539.8200
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation
> 1
> RET_OCplUSI
>  (close) / (open) ;
> Prod Correlation
> Highest Correlation
> Last Run: Sat; 12/30/2023,7:34 PM
> 2
> RET_OC
> RET_OCplusI
> 1;
> 3
> RETplUSI
> (close) / (ts_delay (close,1) ) ;
> 1
> 4
> RET_CO
> (RETplusI / RET_OCplus1 )
> 1;
> 5
> # We define
> negative daytime
> reversal
> as
> positive overnight
> return that
> is
> IOOM
> followed by
> negative daytime
> return.
> NUM
> if_else(and ( RET_CO
> 0, RET_OC
> <
> 0),
> 1, 0);
> NR
> Sum(NUM,
> 20)/20;
> IM
> 8
> AB NR
> NR/ts_mean (NR,
> 240);
> #stocks
> involved
> in
> more
> intense tug of
> War,
> proxied by
> higher monthly
> 鼍
> frequency of
> these negative daytime reversals,
> have significantly higher future
> IOk
> returns.
> 晷
> 10
> 0.5xrank (-returns ) +0.5*rank
> AB NR)
> }
> 100
> 02
> 0? &? 0? 0^
> 0 0?
> 09
> 9
> @
> 03
> 0@一
> 8:
> 0:
> IS Testing Status
> PASS
> Sharpe Of 2.38 is above cUtoff of 1.58_
> Fitness of 1.05 is above Cutoff of 1
> Turnover of 49.179 is above cUtoff of 19_
> Clone this Alphain a new tab
> Turnover of 49.179 is below CUtoff of 709
> Example
> SMate
> Visualization
> T
> Add Alpha to
> List
> Check Submission
> Submit Alpha 
> tS_s
> -0.9
> -0.8
> -0.7
> -0.6
> -0.5
> -0.4
> -0.3
> -0.1
> 0.0
> 0.5
> 0.8
> 1.0
> :
> -0.1.
> 0.2..
> 3
> 0.4.
> 0.7..
> 0.8.
> 0.9..
> 0.0.
> -1.0.
> %
> -0.4.
> -0.3.
> 3
> -0.9.
> -0.7.


单独的AB_NR表现如下：
 
> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation
> 1
> RET_OCplusI
> (close) / (open) ;
> Chart
> Pnl
> 2
> RET_OC
> RET_OCplUSI
> 1;
> 3
> RETplUSI
> (close) / (ts_delay ( close,1) ) ;
> 4
> C0
> (RETplusI / RET_OCplus1 )
> 1;
> 5
> # We define
> negative daytime
> reversal
> as
> positive overnight
> return
> that
> is
> followed by
> a
> negative daytime
> return。
> NUM
> if_else(and (RET_CO
> 0, RET_OC
> <01,
> 1,
> 0);
> 3,500K
> NR
> Sum(NUM,
> 20)/20;
> 8
> AB_NR
> NR/
> mean (NR,
> 240);
> 9
> #stocks
> involved
> in
> more intense tug
> 0f
> War, proxied by
> higher monthly
> 3,000K
> frequency of these negative daytime reversals,
> have significantly higher future
> returns.
> 10
> AB NR
> 2,50OK
> Z,0OOK
> 1,5OOK
> 1,00OK
> SOOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Clone this Alphain a new tab
> Example
> Simulate
> Visualization
> T
> Add Alpha to a List
> Check Submission
> SUbmtApha
> RET_C
> tS_5
> ts_r


采用其他指标替代- returns可以降低correlation, 但是我的疑惑在于，实际上这个idea本身包含的这个东西（AB- NR）其实是没有达到特别好的要求的。在Brain平台中，发现某个idea不能提交，然后再补充一个东西使得其可以提交，但在这个因子被实盘使用时，难道不是有效的只有原本的idea部分？

那么实际上有很多研报和论文中有效的因子都是通过不了全部检验的，那么这样不会导致在最后用一个复杂多因子模型的时候，缺失那些重要的，但是单独使用表现不佳的因子？

换句话说，有很多研报和论文构建的是多因子模型，如果想要复现这些观点，该如何在Brain中表达？

---

### 帖子 #30: 【Alpha灵感】UMR2.0，风险溢价视角下的动量反转统一框架
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】UMR20风险溢价视角下的动量反转统一框架_20088908680087.md
- **讨论数**: 2

文章：东方证券-因子选股系列之九十四：UMR2.0，风险溢价视角下的动量反转统一框架再升级

核心idea :

“高风险高收益”是萦绕在每个市场交易者耳边的话语，我们对这一现象做了一个简单的测试。 我们以波动率作为股票价格波动风险的代理指标，在每个月末将股票按当月的日度收益波动率从 低到高排序分为十组，检验各组内股票当月相对于市场的超额收益。从下面左图可以看到，波动 率较高(第 10 组)的股票当月平均跑赢市场 11%，收益非常可观，这确实验证了高风险下能够 获得高收益的现象，这可观的收益也解释了为什么很多短线交易者对于高波动股票的投机交易十 分热衷。同时也可以看到，高风险的股票在下个月的收益情况，如上面右图所示。波动率较高的 股票在下月平均跑输市场 1.2%。这一现象告诉我们高风险下能够获得高收益，但是这种高收益往 往是通过承担高风险带来的，因而其难以持续且未来呈现出强反转的特征。

反转因子和动量因子由每日的收益拼接组合而成，其中每个交易日都可能由于其风险水平的高低 而体现出不同的动量或反转的效应，我们可以深入到每个交易日对其展开更细粒度的探索。我们 设想高风险日获得的收益往往是承担风险带来的，其更多源于投资者过度自信导致的价格反应过 度，因此未来更倾向于反转效应，而低风险日获得的收益并不源于承担高风险，因此未来更偏向 于动量效应，所以我们可以用每日的风险水平相对高低来调整其日度收益，再重新合成得到一个 统一的动量反转因子。

数据集：日间波动率容易计算。日内波动率所需的分钟数据没有找到，考虑使用

mdl175_realizedvolatility代替。文中用到的特定指数的回报也没有找到，使用了

A-shares Index Data   中的pv25_d1_s_dq_close（vector）根据数据集名称和解释认为这可能是不同指数每日的收盘价。

核心表达式：


> [!NOTE] [图片 OCR 识别内容]
> Zlt-dtlRi
> Riskt
> Rt



> [!NOTE] [图片 OCR 识别内容]
> 12.5M
> Rl
> md1175_realizedvolatility;
> risk
> ts_mean (RI, 20)
> Rl;
> alpha
> SUm
> risk
> (returns),20);
> 10M
> group_rank(
> alpha ,
> bucket
> rank(cap) , range=
> 0.1,1,0.1')
> 7,5OOK
> 5,00OK
> 2,5OOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.05
> 14.83% 3.24
> 16.71 % 7.809
> 22.549oo
> Clone this Alphain a new tab
> Example
> SmUate
> Visualization
> Add Alpha to a List
> Check Submission
> Submit Alpha 
> tS_%


可以看到信号比较明显。

文中还提到不同日期的收益率不能直接相比，需要减去当日的指数收益率


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/TOP2000
> Convert to Multi-Simulation
> 1
> turnover
> Volume
> (sharesout
> *1000000);
> o IS Summary
> Period
> IS
> 05
> 2
> Rl
> mdl175_realizedvolatility;
> 3
> risk
> ts_mean (RI, 20)
> Rl;
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 4
> mkt_ret-vec_avg (pvz5_dl_s_dq_close) /ts_delay (vec_avg (pv25_dl_S_dq_close) ,1)-1;
> 3.12
> 14.61 %
> 3.26
> 15.99%
> 7.649
> 21.899oo
> 5
> 6
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 7
> alpha
> ts
> SUI
> risk
> (returns
> mkt_ret) , 20);
> 8
> group_rank
> 2011
> 3.94
> 14.589
> 4.16
> 16.229
> 1.179
> 22.25%。
> 973
> 972
> 9
> alpha,
> 10
> bucket
> rank(cap) , range='0.1,1,0.1')
> 2012
> 4.81
> 14.129
> 5.61
> 19.23%
> 2.5796
> 27.249o。
> 967
> 964
> 11
> 2013
> 3.51
> 14.33%
> 3.66
> 15.60%
> 1.52%
> 21.789o。
> 965
> 945
> 2014
> 3.06
> 14.099
> 2.99
> 13.489
> 2.70%
> 19.14%。
> 958
> 947
> 2015
> 1.67
> 14.749
> 1.53
> 12.30%
> 7.649
> 16.69%o。
> 952
> 941
> 2016
> 4.80
> 14.279
> 5.99
> 22.249
> 1.969
> 31.18%o。
> 939
> 938
> 2017
> 3.20
> 15.009
> 3.02
> 13.38%
> 1.90%
> 17.83%0。
> 867
> 865
> 2018
> 3.08
> 15.75%
> 2.93
> 14.24%
> 1.96%
> 18.089o。
> 890
> 870
> 2019
> 4.11
> 14.599
> 4.95
> 21.19%
> 2.659
> 29.049o。
> 909
> 910
> 2020
> 1.24
> 14.709
> 0.94
> 8.4796
> 5.1796
> 11.539。
> 868
> 863
> 2021
> 5.59
> 14.31%
> 9.53
> 41.599
> 0.78%
> 58.129o。
> 735
> 719
> Clone this Alphain a new tab
> Correlation
> Example
> Sim Utate
> Visualization
> 甲
> Add Alpha to a List
> Check Submission
> Submit Alpha


加入后alpha又稍有提升，但prod corr未达标。


> [!NOTE] [图片 OCR 识别内容]
> UMR 因子的底层构建逻辑可以总结为
> 高风险日可能更偏反转,低风险日可能更偏动量 
> 但是
> 动量不一定都出现在低风险曰,而反转也不一定都出现在高风险日,如下图所示会存在些日期
> 高风险带上偏动量的例外,高风险与反转 
> 低风险与动量之间并不完全是充要关系。
> 高风险日
> 可能更偏反转,
> 低风险日可能更偏动量
> 是正常交易日中以交易博弈行为占主导的日期才满足的
> 规律。但是不以交易博弈行为占主导的日期
> 它的高风险就不一定体现出反转,而有可能体现出
> 动量。
> 图4:
> UMR 因子逻辑的例外情况
> 偏动量
> 高风险但偏动量
> 低风险
> 高风险
> 低风险但偏反转
> 偏反转


在一些特殊的时间 原有的权重并不适用，所以对最终加入了情绪因素，获得了可提交alpha.

这里也尝试了文中提到的时间半衰的权重倾斜，但效果不如直接取均值。

考虑引入盈利公告的发布日期也没有提升。

该策略的核心思路在与找到一个衡量风险的量R（alpha中用的是mdl175_realizedvolatility）

后续考虑验证该策略在其他市场的效果，比如用implied volatility或情绪热度 带入R

---

### 帖子 #31: 【Alpha灵感】UMR2.0——风险溢价视角下的动量反转统一框架
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】UMR20风险溢价视角下的动量反转统一框架_20101783750167.md
- **讨论数**: 4

**【标题】** 东方证券因子选股系列之九十四：UMR2.0——风险溢价视角下的动量反转统一框架再升级

**【作者】** 杨怡玲

**【因子描述】**

高风险日获得的收益往往是承担风险带来的，其更多源于投资者过度自信导致的价

格反应过度，因此未来更倾向于反转效应，而低风险日获得的收益并不源于承担高

风险，因此未来更偏向于动量效应，我们以时序均值调整后的风险指标来加权个股

每日的溢价，并以此构建统一的动量反转因子。

研报当中首先定义了风险系数Risk：


> [!NOTE] [图片 OCR 识别内容]
> S-t-dtlRi
> Riskt
> R


其中的R为股票每日的风险指标，之后根据d日平均值进行调整，。当股票的风险低于其过去一段时间的均值时，我们认为当日为低风险日，调整后取值为正，而当股票的风险高于过去一段时间的均值时，我们认为当日为高风险日，调整后取值为负。

之后通过用调整后的风险系数来对股票的历史收益溢价进行加权，我们认为低风险日的溢价有动量而高风险日的溢价为反转，因此历史溢价以风险系数加权后，可以得到统一的动量反转因子：


> [!NOTE] [图片 OCR 识别内容]
> f =
> X-t-mtiRiski ` (ri
> Tkti)


关于股票的每日风险指标R，研报当中给出以下变量：


> [!NOTE] [图片 OCR 识别内容]
> 表1:  日度风险代理变量
> 类
> 风险指标
> 指标计箅方式
> 日度
> 真实波动
> 曰度真实波动前收盘价
> 日度
> 换手率
> 总成交量流通股本
> 日内
> 大单买入均价偏离
> abs((大单买入金额 /大单买入量) - WAP) /WNAP
> 日内
> 小单主动买入占比
> 日内小单主动买入金额总成交额
> 日内
> 平均单笔成交量
> sqrt(总成交量旧内成交笔数)
> 分钟高频
> 早盘尾盘成交占比
> 开盘半小时成交额+尾盘半小时成交额
> 流通市值
> 分钟高频
> 分钟收益波动率
> 剔除开盘 5 分钟的5分钟收益率的波动率
> 分钟高频
> 分钟收益偏度
> 剔除开盘 5分钟的5分钟收益率的偏度
> 数据来源; Wind, 东方证券研宄所


进行Alpha研究时，这里采用真实波动进行尝试：


> [!NOTE] [图片 OCR 识别内容]
> TIQX
> (hight
> lowt' abs(hight
> closet-i), abs(lowt
> closet-i)
> closet-I
> TR


**【因子模拟】**

针对上述定义的因子和公式进行计算，设置如下


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
> Sector
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> On
> Verify
> Off
> Save as Default
> Apply
> Chart
> 2SN
> 71
> 11311
> 125N
> OIAOT
> 15 PIL 8,7226.
> 7SOO
> SOOO
> 2SOL
> I |'
> Jan T
> Jul12
> lan '13
> J
> MU15
> Jo16
> J
> Jan'g
> Juld
> IS Summary
> PTnn
> 433T02at[
> LTomTu
> 2.79
> 12.009
> 4.65
> 34.68%
> 12.5096
> 57,79900
> 50
> TUIO
> 111455
> Rlus
> OrJw
> Iarw
> Lo COU
> Shol CMI
> 2NT
> 1317
> 12,12
> 7TC
> TU
> T
> LU
> 4224
> 2.97
> 5EFSR
> ZOI
> 17-
> TTC
> TT TS
> J9Fg
> TLU
> 4111144
> 01T
> 5!
> 205
> 1339
> T
> 901
> 7
> 1131
> 45'c
> 3.05
> 82
> 15
> 2A
> 411
> STe
> 1E4t
> 07
> IA
> 1
> l
> III
> TCCI
> 700
> 1153
> 17.39
> 11.015
> 20
> 131 1T
> LC


可以看到该因子在A股市场中表现良好，但可惜没有通过Prod相关性测试。

**【讨论】**

后续的扩展研究中，可以考虑尝试不同的风险度量，例如不同周期的波动率，或价格偏离程度等。

---

### 帖子 #32: 【Alpha灵感】上下影线，蜡烛好还是威廉好？
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】上下影线蜡烛好还是威廉好_20090584979479.md
- **讨论数**: 6

【上下影线，蜡烛好还是威廉好？】

1. 灵感解释

蜡烛图是一种有力的技术分析方法，被广泛应用于金融市场的研究分析中。与其他技术分析工具一样，蜡烛图形态重在分析市场参与者的心理状态，能够生动形象地刻画出交易者行为随市场行情发展而逐渐演变的过程。众多经验表明，蜡烛图技术在市场择时方面行之有效。就以最简单的“蜡烛图上影线”为例，若股票在某段上涨行情中出现了较长的上影线，则我们往往认为该股当前的卖压较大，空头势力占优，上涨行情即将结束。下图是对这个现象的举例：


> [!NOTE] [图片 OCR 识别内容]
> 图 1展示了上证指数在 2019 年4季度的某段行情走势图中20191014,
> 20191105.
> 20191217  这3  根蜡烛线,均位于上涨行情中,但当日都出现了较长的上影线;
> 果不其
> 然,指数在未来几个交易日内均出现了较大幅度的下跌,如20191014后的4个交易曰,
> 上证指数累计下跌2.32%。
> 图1:  上证指数蜡烛图举例 (2019/10/10-2019/12/25 )
> 20191014
> 20191217
> 20191105
> 数据来源:
> Wind 资讯,
> 东吴证券研究所


2. 选股因子

1）蜡烛上下影线选股因子


> [!NOTE] [图片 OCR 识别内容]
> (1)每个交易曰 ,计算每只股票当日的上下影线,并做标准化,方法为除以过去
> 5个交易日上
> 下影线的平均值,即
> 当日上影线
> 蜡烛上影线=最高价-ma*(开盘价;收盘价);标准化蜡烛上影线-迂丢5目影线的平均僵
> 当日下影线
> 蜡烛下影线=mi(开盘价,收盘价)-最低价; 标准化蜡烛下影线二:
> 讨去5日下影线的平均值
> (2)每月月底,回溯过去20个交易曰,每只股票都计算其每曰标准化蜡烛上影线
> 的平均值。标准差,得到两个因子,分别简称为蜡烛上_mean, 蜡烛上_std,
> 代表了蜡
> 烛图上影线中蕴藏的选股信息;  同样计算 20 个标准化蜡烛下影线的平均值。标准差,
> 分别记为蜡烛下_mean. 蜡烛下_std;
> (3)下月月初,将所有样本按因子值从小到大排序,等分为10组 (分组1因子值
> 最小,分组10因子值最大 )。每组等权买入组内相应股票,持有至月底平仓; 重复上述
> 步骤。


原文构造的是一个月度因子，但是我不是很清楚我们平台能否这样做（我感觉我们平台能实现的一般都是日度的，高频和月度的不知道怎么实现）。我们可以将这个因子迁移成日度的，，会发现蜡烛上_std的结果还是有信号的：


> [!NOTE] [图片 OCR 识别内容]
> 5,00OK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> 1,00OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> w IS Summary
> Period
> 15
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.07
> 16.13%
> 0.66
> 6.06%
> 1
> 4.070
> 7.51%o。


2）威廉上下影线选股因子


> [!NOTE] [图片 OCR 识别内容]
> 除了蜡烛图上下影线之外,威廉指标 (Larry Williams; 1973 )也常被用来衡量市场
> 的超买超卖现象,以一段时间内的空方力量 (最高价-收盘价)与多空总力量 (最高价
> 
> 最低价 )之比,来研判市场的未来走势。威廉指标的具体计算公式为:
> 威廉指标= (最高价-收盘价 ) / (最高价-最低价)
> 根据蜡烛图上下影线与威廉指标的定义,我们可以发现,两者在对市场买卖力量的
> 理解上存在一定差异:
> (1)蜡烛图以 "皿9x(开盘价,收盘价)" 为基准,认为 "最高价-m8x(开盘价,收盘价)"
> 为卖压,
> "min(开盘价,收盘价)-最低价》  为买气;
> (2)而威廉指标以《收盘价》 为基准,认为 《最高价-收盘价》。 为卖压,
> 4收盘价-
> 最低价》
> 为买气。


根据这个，可以构造威廉上下影线


> [!NOTE] [图片 OCR 识别内容]
> (1)每个交易日 ,参照威廉指标的定义,以当日收盘价为基准 ,修改每只股票上,
> 下影线的计算方法,并将结果称为 《威廉上影线  和 "威廉下影线" ,即
> 威廉上影线=最高价-收盘价
> 威廉下影线=收盘价-最低价
> (2)将每曰的威廉上
> 下影线标准化,方法同样为除以过去5 个交易日上。下影
> 线的平均值,即
> 当日上影线
> 当日下影线
> 标准化威廉上影线.
> 标准化威廉下影线==
> 过去5日上影线的平均值
> 过去5日下影线的平均值
> (3)每月月底,回溯过去20个交易日,每只股票都计算其20个标准化威廉上影
> 线的平均值。标准差,得到两个因子,分别简称为威廉上_mean, 威廉上_std;  计算20
> 个标准化威廉下影线的平均值。标准差,分别记为威廉下_mean, 威廉下_std;
> (4)下月月初,将所有样本按因子值从小到大排序,做5分组回测; 每月月底均
> 重复上述步骤。


其中，威廉下_mean的结果不错


> [!NOTE] [图片 OCR 识别内容]
> 8,00OK
> 6,00OK
> 4,00OK
> 2,00OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> o IS Summary
> Period
> 15
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.46
> 36.679
> 0.81
> 11.21%
> 16.109
> 6.11 %oo


3）上下影线综合因子 UBL

通过结合蜡烛影线和威廉影线的结果，可以构造因子UBL：


> [!NOTE] [图片 OCR 识别内容]
> (1)每月月底,分别将所有股票的蜡烛上_std。威廉下
> mean
> 因子做市值中性化处
> 理,将得到的结果记为蜡烛上_std_desize  威廉下_mean_desize;
> (2)采用最简单的方式综合上述两个因子的信息,  将蜡烛上_std_desize 和威廉下
> mean_desize 分别横截面标准化,等权线性相加得到上下影线综合因子
> UBL ( Up and
> Bottom Shadow Line ),
> 即
> UBL
> 芊
> Zscore(蜡烛上_std_desize)
> zscore(威廉下_mean_desize)



> [!NOTE] [图片 OCR 识别内容]
> 15M
> 12.5M
> 10M
> 7,50OK
> 5,0OOK
> 2,50OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> 叫 IS Summary
> Period
> 15
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.75
> 23.559
> 2.49
> 19.359
> 10.569
> 16.439o0


3. 总结

这个alpha用的基本都是price volume数据集中的数据。文中有个表格说明了这个alpha在整个a股中的表现比较好，所以我们用top3000这个universe。并且文中也提到了一级行业对这个alpha的影响，所以我们采用industry中性化

---

### 帖子 #33: 【Alpha灵感】东吴证券的几种换手率因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】东吴证券的几种换手率因子_20255074372375.md
- **讨论数**: 0

东吴证券在“技术分析拥抱选股因子”系列研究中构建了若干换手率因子，本帖对这些“换手率”相关因子进行梳理。


> [!NOTE] [图片 OCR 识别内容]
> 表1:  东吴金工 "换手率因子》  相关研究
> 数据
> 因子名称
> 对应研报
> 发布日期
> 传统换手率因子
> 日频
> 换手率变化率因子
> 《量价配合视角下的新换手率因子》
> 2020/11/30
> 量稳换手率因子
> 《量稳换手率选股因子一一量小。量缩,都不如量稳? 》
> 2021/5/15
> 优加换手率因子
> 《优加换手率一一解决1+1<2的难题》
> 2021/8/19
> 分钟
> 换手率分布均匀度因子
> 《换手率分布均匀度,基于分钟成交量的选股因子》
> 2021/3/1
> 换手率变化率
> 量稳换手率
> 日频
> 本报告
> 2021/12/07
> 研究思路的结合
> 数据来源:  东吴证券研究所整理


其中“换手率分布均匀度”高频因子似乎已经有同学在论坛中发表了。

我在此对剩下几个做一些复现。换手率因子大同小异，该部分因子correlation极高，非常拥挤，个人无法找到降低Correlation的调整空间

1.传统的换手率因子（量小换手率）

每月月底计算每只股票过去 20 个交易日的日均换手率，做市值中性化处理，记为传统换手率因子（量小换手率）


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/T0P3000
> Convert to Multi-Simulation 
> 1
> -ts
> mean (volume/sharesout ,
> 20)
> Chart
> Pnl
> 2
> #量小换手率
> 3
> #Robust universe Sharpe of
> 0.68
> is below cutoff of 1.15
> (40% of Alpha)
> #Robust
> universe
> returns  0f
> 4.17% is below cutoff of 8.208
> (40%
> 0f
> Alpha) .
> 17.5M
> 15M
> 12.5M
> 1OM
> 7,500K
> 50OOK
> 2,5OOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Clone this Alphain a new tab


2.换手率变化率因子：

换手率变化率因子的构造步骤如下：

（1）每月月底，回溯所有股票过去 20 个交易日，计算每个交易日的换手率变化率

=当日换手率/基准换手率-1；

（2）其中，基准换手率的计算方法为，再往前取 X 个交易日，计算这 X 个交易日

换手率的平均值；X 暂时取为 40；

（3）每只股票，得到 20 日换手率变化率后，计算它们的平均值，再做横截面市值

中性化处理，即为所有股票当月的因子值，记为换手率变化率 PctTurn20 因子。


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/T0P3000
> Convert to
> Multi-Simulation 
> Currentchange
> Volume/sharesout;
> Chart
> Pnl
> 2
> Standardchange
> delay (ts_mean (volume/sharesout, 40),20);
> 3
> Factor
> ts_mean
> Currentchange
> Standardchange)
> 1,
> 20);
> -Factor
> ZOM
> 17.5M
> 15M
> 12.5M
> 10M
> 7,5OOK
> 5,0OOK
> 2,50OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> ts_C


3.量稳换手率因子

每月月底，回溯每只股票过去 20 个交易日，计算 20 日换手率的标准差；在横截面上做市值中性化处理，得到所有股票当月的因子值，记为量稳换手率因子

在利用换手率对股票进行分析时，换手率的绝对数值固然重要，但其稳定性更不容忽视。在月度选股上，如果我们发现一只股票的换手率很高，不可轻易将其归为空头，若它每天都能保持同样的高换手，则这只股票下个月仍有较大的概率上涨


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/T0P3000
> Convert to Multi-Simulation 
> 1
> -ts_std_dev (volume/sharesout
> 20
> Chart
> Pnl
> 2
> #量稳换手率
> 3
> #Robust
> universe
> returns
> 0f
> 10.648
> is below Cutoff
> Of 13.68%
> (40% of Alpha)
> ZSM
> ZOM
> 15M
> 1OM
> 5,0OOK
> 12/22/2011
> IS Pnl: 2,515.17K
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Clone this Alphain a new tab


3. 优加换手率因子：

如何将“量小”与“量稳”2个换手率因子进行有效组合？

简单的 量小+量稳或者量稳/量小，组合因子的效果，其实都不如单独的量稳换手率因子

原因在于：

两个因子双重分组的结果，与单因子的回测表现产生了矛盾。就单个因子而言，量稳、量小因子的 IC 均为负数，表明量越稳、量越小的股票，未来表现越好。因此，在双重分组下，我们理应期待图 7 的左上角，即同时满足“量最稳”、“量最小”的股票年化收益最高。然而，根据实际统计结果，我们却看到收益最高的区域，更偏向于图 7 的左下角。除此之外，在量的稳定性较差的分组中，即图 7 的右半部分，从上到下，随着量的逐渐增大，各个分组的收益逐渐降低，这个现象符合预期；但在图 7 的左半部分、量的稳定性较强的分组中，随着量的逐渐增大，各个分组的收益却呈现上升趋势，即在量较稳的分组中，量越大的股票，未来表现反而越好，这一点与传统量小换手率因子的逻辑矛盾。


> [!NOTE] [图片 OCR 识别内容]
> 图7:  量小。量稳双重分组下各组的年化收益
> 量最稳
> 先按照"量稳"分组
> 从小到大
> 量最不稳
> 分组1
> 分组2
> 分组3
> 分组4
> 分组5
> 分组6
> 分组7
> 分组8
> 分组9
> 分组10
> 量最小
> 分组1
> 36.24%
> 23.94%
> 22.24%
> 22.40%
> 20.86%
> 18.58%
> 18.06%
> 8.95%
> 9.85%
> 1.72%
> 分组2
> 37.98%
> 29.64%
> 27.76%
> 17.20%
> 19.93%
> 13.96%
> 10.14%
> 16.49%
> 6.79%
> 0.19%
> 分组3
> 33.80%
> 27.80%
> 22.74%
> 16.08%
> 16.22%
> 16.13%
> 17.07%
> 15.82%
> 8.40%
> 1.63%
> 再按照
> 分组4
> 36.11%
> 24.91%
> 17.93%
> 19.51%
> 14.44%
> 18.28%
> 12.27%
> 11.26%
> 9.98%
> -1.02%
> 6量小〉
> 分组5
> 32.04%
> 29.10%
> 27.51%
> 22.39%
> 17.19%
> 14.05%
> 17.34%
> 13.48%
> 10.96%
> -1.679
> 分组
> 分组6
> 38.02%
> 29.62%
> 21.14%
> 23.22%
> 19.41%
> 13.65%
> 12.17%
> 12.83%
> 7.59%
> -1.98%
> 从小到
> 大
> 分组7
> 39.50%
> 34.35%
> 24.21%
> 21.00%
> 23.01%
> 18.75%
> 18.51%
> 10.70%
> 6.96%
> -3.18%
> 分组8
> 33.51%
> 29.54%
> 24.58%
> 18.03%
> 19.70%
> 22.32%
> 13.29%
> 14.41%
> 7.14%
> -7.53%
> 分组9
> 38.84%
> 26.790/
> 25.45%
> 25.23%
> 22.86%
> 18.51%
> 14.80%
> 10.70%
> 6.41%
> -12.95%
> 量最大
> 分组10
> 39.04%
> 35.14%
> 30.12%
> 27.079
> 25.24%
> 21.779
> 9.82%
> 7.28%
> 3.02%
> -24.39%
> 数据来源:
> Wind 资讯,东吴证券研究所


对于这种问题，文中提出使用优加法进行组合：


> [!NOTE] [图片 OCR 识别内容]
> 3.3.
> 量小与量稳的正确结合方式一一优加法
> 根据上述现象,
> 我们提出一种新的组合方式:
> (1)每月月底。计算所有股票的量小因子 Turnz0 和量稳因子 STR;
> (2)先将所有样本按照量稳因子从小到大排序,
> 打分1,2,.
> N-IN,
> N 为当期样
> 本数量,
> 记为 "得分1"; 为了方便表述,
> 暂且假定 N 为偶数;
> (3)取量稳因子排名靠前的  50%样本,
> 再将它们按照量小因子从大到小排序,打
> 1,2,
> ,N/2 ,
> 记为 "得分2";
> r得分1 + <得分2" ,
> 即为这些股票的最终得分=
> (4)对于量稳因子排名靠后的  500样本,则将它们按照量小因子从小到大排序,
> 打分1,2,.
> ,NI2,
> 记为 "得分3"; 这些股票的最终得分为 "得分1 + "得分3";
> (5)所有样本的上述最终得分,
> 即为新因子的因子值;  按照因子值对所有样本排
> 序,做10分组回测;  其中,最终得分最小的为多头,最终得分最大的为空头,即新因子
> 的 IC 应当为负。
> 我们把上述方法称为"优加法" ,得到的新因子命名为"优加换手率因子》 ,简称 UTR
> 因子 ( U-Turnover Rate )。
> 在《优加法"  中,最关键的是步骤(3),它实现了 "在量较稳
> 的样本中,我们希望量反而越大越好》  的目的。
> 正所谓富水长流,方能财源广进:  富水
> 即量大,长流则代表量稳;只有持续稳定的输出,才有可能为我们带来源源不断的收益。
> 而步骤(4)则与传统的多因子组合方式-致,按照两个单因子原本的方向进行了组合



> [!NOTE] [图片 OCR 识别内容]
> 1
> Volumestable
> ts_std_dev (volume/sharesout
> 20) ;
> N
> N Lnart
> Pnl
> 2
> MeanVolumestable
> ts_mean (group_mean ( Volumestab
> 1,market ), 40);
> 3
> #量稳换手率
> 4
> #Robust
> universe
> returns
> 0f
> 10.648
> is below Cutoff
> Of 13.68% (40% of Alpha).
> 5
> 6
> 7
> VolumeSmall
> ts_mean (volume/sharesout ,
> 20) ;
> 1OM
> 8
> #量小换手率
> 9
> #Robust universe Sharpe of
> 0.68
> is
> below cutoff of
> 1.15
> (40% of Alpha)
> 10
> #Robust
> universe
> returns
> 0f
> 4.178 is below cutoff
> 0f
> 8.20% (40% of
> Alpha)
> 11
> 800OK
> 12
> 13
> Condition
> Volumestable
> MeanVolumestable;
> 14
> Scorel
> rank (-Volumesmall ) +rank ( Volumestable) ;
> 15
> Scorez
> rank ( VolumeSmall ) +rank
> Volumestable) ;
> 6,0OOK
> 16
> Express
> =-rank (if_else( Condition,
> Scorel,
> Scorez) );
> 17
> 18
> 19
> group
> bucket ( rank(cap ) , range='0,1,0.1');
> 4,00OK
> 20
> group_neutralize ( Express , group) ;
> 21
> # "优加法
> 东吴证券《优加换手率  解决  1+1<2 的难题》
> 22
> 2,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Clone this Alphain a new tab
> le,


4.

量稳换手率的变化率

（1）每月月底，回溯每只股票过去 20 个交易日，计算 20 日换手率的标准差，为

当月换手率波动率；

（2）再往前取 X 个交易日，计算这 X 个交易日换手率的标准差，为基准换手率波

动率；X 暂取 40；

（3）计算换手率波动率的变化率=当月换手率波动率/基准换手率波动率-1，再做横

截面市值中性化处理，即得到所有股票当月的因子值，记为量稳换手率变化率  因

子。


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/T0P3000
> Convert to
> Multi-Simulation 
> Chart
> Pnl
> Currentdev
> ts_std_dev (volume/sharesout ,
> 20);
> 2
> Standarddev
> ts_delay (ts_std_dev (volume/sharesout , 40),20) ;
> 3
> Factor
> (Currentdev
> Standarddev )
> 1;
> rank ( Factor)
> 8,0OOK
> 6,0OOK
> 4 0OOK
> 2,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021


---

### 帖子 #34: 【Alpha灵感】从ICIR角度探讨风格因子的均值回复性
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】从ICIR角度探讨风格因子的均值回复性_19524432578967.md
- **讨论数**: 0

**文章**

广发证券多因子Alpha系列报告之（十二）——从ICIR角度探讨风格因子的均值回复性

**摘要**

> 从理论上来讲，任何一类风格因子都不可能长期产生稳定的Alpha，因此从长期来看风格因子必定存在“均值回复”特性；另一方面，由于市场对于一种风格的消化和体现往往需要一个过程，加之市场参与者并非完全理性人，常常出现跟风现象，因此短期来看，市场风格往往出现“惯性”特征！为了挖掘A股市场的风格轮动规律，报告结合不同的统计工具，对风格因子的轮动规律进行分析。
> 我们运用不同对因子IC序列进行分析，发现因子当期IC与因子之前一段观察期以内的ICIR存在显著的负相关关系，从而证明因子的有效性存在一定的均值回复性。报告设计了相应的因子择时策略，长期来看，我们假定采用的9类因子均为有效的Alpha因子，因此择时策略主要针对各因子的权重进行调整，调整的依据是各因子之间的ICIR相对大小比较。


> [!NOTE] [图片 OCR 识别内容]
> 表 2. Alpha 因子 ICIR 最佳观察期
> 因子
> 因子 ICIR 观察期 (月)
> 1个月成交金额
> 换手率
> 10
> 一个月股价反转
> 三个月股价反转
> 8
> 六个月股价反转
> 8
> 流通市值
> 8
> EP
> SP
> BP
> 数据来源:  广发证券研究发展中心,
> Wind数据库


**在Brain平台上复刻**

上文为提供了有效的理论基础，说明了在2012年前后中国A股市场中的风格因子均值回复现象较为明显，其根据 **ICIR值** 制定的轮动策略取得了不错的效果。

由此，来看一看这个思路是否能在过去一段时间能够找到长期有效的因子。

1. 首先面临的问题就是数据问题，有些数据如换手，EP 等数据在CHN是缺失的，故主要考虑测试USA的因子
2. 其次的问题是Brain平台不能很有效地计算比较传统的IC值序列，其要求在截面上取出股票池中所有股票当期因子值与下期收益，进行相关性计算（根据需要选择Spearman或Pearson相关系数）。在Brain平台的主要任务是找出每个alpha的在每个股票上的特异性，因此考虑使用上期因子序列与本期收益率序列，计算其相关系数（目前ts_corr()只支持Pearson相关系数）。此外，这里的超参数较难确定，没有文献可以依据，暂设为90，也就是三个月。
3. 最后根据IC值序列，通过ts_ir()函数就可求得ICIR值了。取其相反数即认为其具有均值回复性，否则为趋势跟随性。同样的这里的时间超参数同样难以确定，暂定为90。
4. 细节上，因子序列常需要进行以下额外操作：（1）（中位数或zscore）去极值；（2）行业市值中性化（利用ts_regression（也设90的参数）和group_neutralize函数可实现）

于是我们得到Brain伪代码

```
-ts_ir(ts_corr(ts_returns(vwap, 30), ts_delay(ts_regression(group_neutralize(zscore(test_alpha), market), cap, 90), 30), 90), 90)
```

```
'settings': {    'instrumentType': 'EQUITY',    'region': 'USA',    'universe': 'TOP3000',    'delay': 1,    'decay': 0,    'neutralization': 'Market',    'truncation': 0.1,    'pasteurization': 'ON',    'unitHandling': 'VERIFY',    'nanHandling': 'OFF',    'language': 'FASTEXPR',    'visualization': False,}
```

将以下Brain平台数据代入进行检验

- 换手率  -  oth466_rt_turn_rate
- 流通市值  -  cap
- 一月成交金额  -  ts_sum(vwap * volume, 30)
- EP  -  mdl57_ep_ratio

**测试结果与调参 - 以换手为例**

首先发现结果并不理想，发现基本上国内的报告很多都是月频处理的，将其直接迁移到这里也许并不妥当，由此，删去市值中性化的操作（即ts_regression函数部分）


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> Pu
> 50呸
> 25呸
> 25
> I
> 50[正
> 2012
> 2013
> 2011
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021


可以看到因子的表现好了很多，不过可以注意到，此时表达式的方向已经变为正了（说明存在趋势跟随性），其仅在2016，2018，2020表现不错，其他时候表现平庸


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pn工
> 叩哑
> 叩呕
> W
> 2012
> 2013
> 2011
> 2015
> 2016
> 20I7
> 2018
> 2019
> 2020
> 2021
> NM


最后，对表达式进行微调，并加入止损条件 returns > -0.1，可以得到以下结果

```
returns > -0.1 ? (ts_ir(ts_corr(ts_returns(vwap, 30), ts_delay(group_neutralize((oth466_rt_turn_rate), market), 30), 90), 90)) : -1
```


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pu
> 叩呕
> 5,叩哑
> 叩呕
> 3,000
> 2,叩哑
> 1,00呸
> HN
> 2012
> 2013
> 2011
> 2015
> 2016
> 20I7
> 2018
> 2019
> 2020
> 2021



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Assregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drarrdown
> Iargin
> 0.95
> 11.50%
> 0.68
> 6.45%
> 10.44%
> 11.229600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 211
> 8
> 11.82%
> 一0.15
> -2.0%
> 4.70%
> 469600
> I461
> 1404
> 202
> 1.18
> 10.52%
> 081
> 5.94%
> 83%
> 39600
> 14
> 121
> 2013
> 2.10
> 8.08%
> 1.85
> 9.72%
> 2.87%
> 079000
> 120
> 1565
> 2014
> 1.78
> 10.44%
> 1.56
> 9.65%
> 5.04%
> 18.4899600
> 1382
> 1474
> 2015
> 0.38
> 1.84%
> 0.15
> 2.52%
> 3.61%
> 3.189600
> 1435
> 1486
> 2016
> 0.9
> 10.23%
> 079
> 8.l%
> 6.4%
> 16.549600
> 1120
> 14
> 217
> 05
> 9.17%
> 015
> 2.o%
> 3.11%
> 449000
> 1485
> 1497
> 2018
> 077
> 10.59%
> 047
> 4.1%
> 8.94%
> T49oo
> 1287
> 1649
> 2019
> 1.31
> 14.09%
> 1.20
> 11.88%
> 6.4%
> 16.869600
> 1317
> 1616
> 2%
> 工6
> 14.74%
> 1.68
> 14.49%
> 7.72%
> 19.679600
> 18
> 1679
> 22
> 一2.58
> 10.28%
> -85
> 4.21%
> 3.39%
> 一4.149600
> 181
> 1446


从上述结果可以看出，此因子除去一些微小的波动外，总体来说一致性较好，回撤和换手也较小。但同时收益和夏普都不太理想。由于时间有限，期望之后能够对其改进，获得更好的结果。最后是改进思路。

**改进思路**

1. 尝试更多的风格因子
2. 利用Consultant Python api来批量生成表达式，从而能求得两个合适的时间长度超参数
3. 同样的，由于这里借用了传统的ICIR思想，而其又常以月频进行探究，因此，是否计算IC的两个序列的时间差也需要进行改变。同样可由较为粗放的遍历方法，大致探究一下

---

### 帖子 #35: 【Alpha灵感】从布林带到估值异常因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】从布林带到估值异常因子_20235808598423.md
- **讨论数**: 1

标题：东吴证券：“基本面选股因子 ”系列（一） 从布林带到估值异常因子

作者：高子剑 张翔宇

概述：布林带是经典的均值回复策略，使用价格的滚动均值作为中枢，2倍滚动标准差作为带宽，用中枢加减带宽分别构筑上轨、下轨。股价突破上轨时为卖出信号、突破下轨时为买入信号、回归中枢时为平仓信号。布林带策略中认为部分资产的价格存在均值回复的特性，而在选股研究领域，发现有一个指标也存在类似的属性——股票的估值PE。文章探讨了估值的均值回复特性，并利用这一特性构建估值偏离因子。

Alpha Idea:

1.估值偏离因子EPD

仿照经典均值回复布林带的构造方法，构造估值布林带模型，用过去一段时间EP的均值、标准差分别构造估值中枢、带宽与上、下轨，如果某只股票当前的EP位于上轨以上或者下轨以下的部分，认为该股票的估值处于异常区间，如果其基本面不发生大的变化，未来的EP有很大概率回归正常区间。


> [!NOTE] [图片 OCR 识别内容]
> 图3:  基于估值的布林带模型结构
> 异常区间
> EP 上轨
> EP 中轨
> EP 下轨
> 异常区间



> [!NOTE] [图片 OCR 识别内容]
> 1 .
> 确定计算估值偏离所用的时间窗口252个交易日
> 2.
> 计算时间窗口内 EP 的均值1EP,252与标准差06P,252
> 3.
> 计算当期EP 相对历史中枢的偏离程度EP_d
> EPlatest
> NEP,252
> BP_d =
> OEP,252
> 其中 E 采用 EPttm,
> NEP;252是 EP 过去252个交易曰的均值,
> OEP,252是 EP 过去
> 252个交易日的标准差。


为了剔除行业层面估值逻辑改变代理的影响，接下来对𝐸𝑃_𝑑进行行业市值中性化处理，在横截面上回归行业哑变量以及标准化流通市值，其中流通市值经过box-cox标准化处理，取残差得到估值偏离因子EPD。复现结果如下，可以提交。


> [!NOTE] [图片 OCR 识别内容]
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
> CHN
> TOP3000
> Fast Expression
> 0.01
> Industry
> On
> Off
> Verify


```
a = ts_zscore(fnd72_s_pit_or_is_q_spe_si, 252);a1 = group_neutralize(a, bucket(rank(cap), range="0.1,1,0.1"));a2 = group_neutralize(a1, subindustry);b = ts_zscore(cap, 252);b1 = group_neutralize(b, subindustry);regression_neut(a2, b1)
```


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.89
> 6.789
> 3.60
> 10.68%
> 4.109
> 31.499o。
> Chart
> Pnl
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 7.31
> 7.56%
> 8.21
> 15.76%
> 0.609
> 41.72%00
> 709
> 773
> 2012
> 6.08
> 7.259
> 6.68
> 15.079
> 0.999
> 41.57960。
> 887
> 955
> 7,50OK
> 2013
> 5.15
> 6.449
> 5.00
> 11.80%
> 1.199
> 36.63%0。
> 1061
> 1133
> 2014
> 1.05
> 5.959
> 0.44
> 2.159
> 1.749
> 7.239。
> 1066
> 1131
> 5,00OK
> 2015
> 2.03
> 7.099
> 1.59
> 7.699
> 4.109
> 21.679o0
> 1034
> 1139
> 2016
> 3.48
> 6.249
> 2.84
> 8.339
> 0.76%
> 26.73%00
> 1156
> 1279
> 2,50OK
> 2017
> 5.27
> 6.759
> 5.21
> 12.209
> 0.999
> 36.13900
> 1254
> 1381
> 2018
> 4.75
> 7.01%
> 4.87
> 13.129
> 1.029
> 37.449o。
> 1309
> 1445
> 2019
> 3.71
> 6.829
> 3.50
> 11.109
> 2.98%
> 32.539o。
> 1337
> 1449
> 2020
> 2.55
> 7.379
> 2.12
> 8.659
> 3.26%
> 23.4790
> 1328
> 1409
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2021
> 9.83
> 3.029
> 16.06
> 33.359
> 0.51%
> 220.979o0
> 1426
> 1241



> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Testing Status
> Period
> IS
> 05
> 10 PASS
> Sharpe of 3.89 is above CUtoff of 2.07.
> Fitness of 3.60is above cutoff of 1
> Turnover of 6.789 is above cutoff of 1%.
> Turnover of 6.78% is below cutoff of 709_
> Weight is well distributed over instruments。
> Returns of 10.68% is above cutoff of 8%.
> Sub-universe Sharpe Of 3.53 is above cutoff of 2.38.
> Robust universe Sharpe of 1.71 is above cutoff of 1.56 (40% of Alpha):
> Robust universe returns Of 10.16% is above cutoff of 4.27% (40% of Alpha):
> IS ladder Sharpe of 3.09 is above cutoff of 2.37 for ladder year 2: 2/18/2021...2/19/2019.



> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Search
> Select
> Select
> Select
> Search
> Select
> Select
> @.8>1
> e.8>1
> e.8>1
> Select
> anonymoUs
> Regular
> ACTIVE
> 12/31/2023 EST
> CHN
> TOP3000
> Tag


2.缓慢偏离因子EPDS

下面是对EPD因子的改进，估值偏离 EPD因子认为：当前估值水平大幅偏离历史中枢的股票是 “异常 ”的股票， 但存在一些 “强势股 ”、 “崩盘股 ”，这些股票估值的偏离并不能称之为 “异常 ”，因为他们的估值逻辑已经完全被改变，在未来不太可能再回到 “正常 ”区间。它们更偏向于趋势突破而非均值回复，EPD因子往往高估了这些股票的“异常”。因此提出可能的股票估值逻辑被改变概率的代理指标：


> [!NOTE] [图片 OCR 识别内容]
> 1 .
> 股票过去一段时间价格走势的强度1,126
> 涨跌幅更极端的股票估值逻辑被改变的概率较大
> 2.
> 股票过去一段时间价格走势的稳定性0+,126
> 过去涨 (跌)幅更平稳的股票相对而言市场分歧度较小,意味着市场对涨跌幅的认
> 可度高, 其估值逻辑被改变的概率较大。
> 我们用过去一段时间的信息比率衡量股票估值逻辑被改变的概率:
> Ur,126
> [尺 =
> Or,126
> 其中1,126是股票收益率过去 126个交易日的均值, Or,126是股票收益率过去 126个
> 交易日的标准差。


IR绝对值较高的公司估值逻辑被改变的概率更大，更偏趋势突破，其 “异常 ”被 EPD因子高估。在横截面上，用当期 EPD 因子值 (带截距项 )回归当期的 IR 取残差作为估值缓慢偏离因子 EPDS。

---

### 帖子 #36: 【Alpha灵感】信息分布均匀度，基于高频波动率的选股因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】信息分布均匀度基于高频波动率的选股因子_20073476508055.md
- **讨论数**: 4

**文章：** 【东吴金工】信息分布均匀度，基于高频波动率的选股因子

**核心idea：**

（1）每月月底，回溯所有股票过去 20 个交易日，每个交易日都利用分钟数据，计
算日内分钟涨跌幅的标准差，记为每日的高频波动率 Vol_daily；

（2）每只股票，计算 20 个 ol_daily 的标准差，记为该股票当月每日波动率的波
动 std（Vol_daily）；

（3）每只股票，计算 20 个 ol_daily 的平均值，衡量该股票当月每日波动率的平
均水平 mean（Vol_daily）；将 std（ ol_daily）除以 mean（ ol_daily），再做市值中性化
处理，得到每只股票的信息分布均匀度 UID 因子。

**每日波动率的波动 std（Vol_daily）的含义** ：我们认为该指标能够
反映股票在过去 20 个交易日的信息分布均匀程度；假设某只股票在过去 20 个交易日中
的信息总量是一定的，若在某几个交易日发生了信息冲击，即在这几个交易日中的某些
时点，信息流入的速度突然加快、流入的信息量突然增大，那么这几个交易日的波动率
 vol_daily 就会明显高于其他交易日，这就会导致在过去 20 个交易日中，每日波动率的
波动 std（ vol_daily）也比较大；因此，频繁发生信息冲击的股票，或者说信息分布越不
均匀的股票，std（vol_daily）就会越大；顺带着，我们猜测 std（ vol_daily）的方向应
当与传统波动率因子一致，即 IC 为负。

**最终的信息分布均匀度 UID 因子，要除以每日波动率的平均水平：** 我们认为，std（vol_daily）应当与 mean（ vol_daily）高度正相关，即本身波动越大的股票，波动的波动也倾向于越大，因此需要将 std（ vol_daily）除以 mean（ vol_daily），做标准化处理。

**数据集：** 由于brain平台中没有高频数据，无法精确计算每日高频波动率，我找到了波动率相关的数据集mdl175_realizedvolatility。

**Universe** ：CHN TOP3000

**Neutralization** ：经过试验，各settings的Neutralization结果差别不大，除此之外需对因子做市值中性化。

**Operator** ：ts_std_dev，ts_mean，regression_neut

考虑到UID因子可能受到传统波动率因子的影响。因此，我们将 UID 因子对 vol20 因子（过去 20日的日收益率标准差）做正交化处理，取残差进行预测，得到结果如下：


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS 
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.67
> 14.149
> 2.42
> 11.659
> 19.81%
> 16.489600



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 7,50OK
> 08/30/2017
> ISPn: 6,349.33k
> 5,0OOK
> 2,50OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21


可以看到该alpha表现很不错，已经达到了可提交的状态，相关性检验也都通过，但是还存在一个较大的回撤。这是由于2015年中国市场的股灾导致的，当时的换手率值会显著高于平时的值，在我之前发布的《量稳换手率STR》文章中，研报曾提到将 STR 因子对 Vol20 做正交化处理，选股能力也十分不错，于是我将换手率因子与波动率因子做线性组合之后，希望可以改善当时的情况，得到结果如下：


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS 
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 4.70
> 12.809
> 6.21
> 22.359
> 11.88%
> 34.939600



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 15M
> 1OM
> 5,0OOK
> Jan '12
> Jan '13
> Jan '14
> '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan


这时可以看出，不仅仅是drawdown减小，其余指标也得到了大幅提升，同时也达到了可以提交的标准！

同时我试验了小贴士中若跌停股票较多，则停止一段时间的交易，那样即使可以将drawdown的时间段pnl变为一条直线，但效果依旧不尽人意，这也许就是过度overfitting某个时期的坏结果，通过与该alpha内在逻辑有关联的alpha来优化alpha表现反而会得到意想不到的结果。

---

### 帖子 #37: 【Alpha灵感】偏斜性偏好和市场异象
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】偏斜性偏好和市场异象_19507603510039.md
- **讨论数**: 0

论文标题：Skewness Sentiment and Market Anomalies

作者：Alok Kumar, Mehrshad Motahari, Richard Taffler

年份：2022

Link： [[链接已屏蔽])

Alpha Inspiration：论文中的研究表明，投资者对偏态的偏好是导致各种市场异象的一个重要因素。文章中使用基于11种著名异象策略的综合错价衡量方法，展示了与市场异象的错价成分相关的回报可预测性在具有更高特异性偏态的公司中更强。这种可预测性差异是由具有高偏态的公司在做空异象组合中表现更差所驱动的。偏态并不影响做多异象组合的表现。来自一家零售经纪公司的投资组合持有数据显示，对偏态偏好较强的投资者倾向于在做空异象组合中分配相对更大的权重。

相关数据集：

oth41_s_tech_skewness

mdl175_revs10

策略构建及其表现：

文章提出市场异象的错价成分相关的回报和特异性偏态与股价间具有一定相关性。基于这点，我们通过相关数据集计算出偏度和回报特征，由于数据集只在CHN市场可进行回测，于是我们使用rank（-feature）在A股市场中对两个特征进行数据探索（使用负号的原因在于仅对特征回测都出现相似的平滑的斜率为负的曲线）：

回报的预测性：


> [!NOTE] [图片 OCR 识别内容]
> 12M
> 1OM
> 8,00OK
> 6,0OOK
> 4,00OK
> 2,0OOK
> 11/25/2011
> MMFIS PnL: 1,103.41K
> NumlyNp


偏度的预测性：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,0OOK
> 5,0OOK
> 4,0OOK
> 3,00OK
> 05/29/2014
> IS Pnl: 2,359.12K
> 2,00OK
> 1,00OK
> FNYIM


我们发现，市场异象的错价成分相关的回报和特异性偏态均对股价有一定的预测作用，其中回报的预测性较强，波动相对较小。

基于论文中的假设：市场异常的定价偏差成分与未来收益之间的负相关关系在具有较高特质性偏斜的股票中更强，我们构建量化策略如下：

偏斜性分析：对每只股票的偏斜性进行分类。通常，正偏斜表示潜在的高回报但高风险，而负偏斜则相反。这里，偏斜性特征计算我们使用oth41_s_tech_skewness。

回报率分析：分析历史回报率，特别是在不同的市场情况下股票的表现；识别历史上表现良好（或不佳）的股票。

组合构建：根据偏斜性和历史回报率创建两个股票组合：一个专注于高偏斜性且历史回报率较差的股票（类似于上述的空头组合），另一个专注于低偏斜性且历史回报率较好的股票（类似于多头组合）。

策略回测表现：


> [!NOTE] [图片 OCR 识别内容]
> 14M
> 12M
> 1OM
> 80OOK
> 6,0OOK
> 4,00OK
> 2,00OK
> 05/11/2012
> ISPn: 1,931.771
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS 
> 0s
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.89
> 27.61 %
> 1.44
> 15.94%
> 12.089
> 11.549600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.14
> 29.30%
> 1.48
> 13.9796
> 3.3296
> 9.549600
> 1062
> 1039
> 2012
> 3.17
> 28.539
> 2.73
> 21.1996
> 4.5596
> 14.869600
> 1141
> 1121
> 2013
> 2.88
> 26.98%
> 2.49
> 20.149
> 3.769
> 14.939600
> 1208
> 1157
> 2014
> 2.19
> 26.499
> 1.65
> 14.999
> 5.2596
> 11.329600
> 1213
> 1159
> 2015
> 2.05
> 27.190
> 2.05
> 27.209
> 12.0896
> 20.019600
> 1224
> 1196
> 2016
> 2.39
> 26.579
> 2.06
> 19.78%
> 3.1196
> 14.899600
> 1356
> 1302
> 2017
> 0.43
> 26.71%
> 0.15
> 3.1796
> 5.359
> 2.379600
> 1507
> 1468
> 2018
> 1.32
> 27.5996
> 0.79
> 9.9496
> 5.5796
> 7.219600
> 1508
> 1493
> 2019
> 3.94
> 29.559
> 3.73
> 26.559
> 3.8096
> 17.979600
> 1515
> 1467
> 2020
> 0.18
> 27.779
> 0.05
> 1.8596
> 7.0096
> 1.339600
> 1542
> 1467
> 2021
> -0.64
> 26.80%
> -0.39
> -9.71%
> 5.329
> -7.259600
> 1521
> 1501



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> PASS
> Fitness of 1.44is above cutoff of 1.
> Turnoverof 27.619 is above cUtoff of 19.
> Turnoverof 27.619 is below cutoff of 709
> Weight is well distributed over instruments。
> Returns of 15.949 is above cutoff of 8%.
> Sub-universe Sharpe of 1.68 is above cutoff of 1.16。
> Robust universe Sharpe of 1.13 is above cutoff of 0.76 (4006 of Alpha).
> Robust universe returns of 8.630 is above cUtoff of 6.380 (4096 of Alpha)。
> 2 FAIL
> Sharpe of 1.89 is below cutoff of 2.07.
> IS ladder Sharpe of 1.35 is below cUtoff of 2.07 for ladderyear 2: 2/18/2021...2/19/2019.
> WARNING
> 3 PENDING


回测结果显示，策略具有相对较好的表现，不足在于Sharpe表现较低，特定年份Sharpe不达标，我们尝试通过调整参数、分组中性化等方式进行优化，优化后的策略表现如下：


> [!NOTE] [图片 OCR 识别内容]
> UURLUUUA
> BRAN
> Simulate
> Alphas
> Data
> 留 Competitions (2)
> Events
> Learn
> Refer a friend
> Simulation 1
> Simulation 12
> Simulation 10
> Simulation 14
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> CHN/D1 /T0P3000
> Convert to Multi-Simulation
> Jucket
> Chart
> Pnl
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> 15M
> CHN
> T0P3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 12.5M
> Industry
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> 1OM
> On
> Verify
> Off
> 7,50OK
> Save as Default
> Apply
> 5,00OK
> 2,50OK
> 08/12/2011
> O  775.99K
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS 
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.32
> 29.92%
> 1.81
> 18.24%
> 10.429
> 12.199600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.24
> 31.51%
> 1.53
> 14.629
> 3.4396
> 9.289600
> 1063
> 1038
> 2012
> 3.31
> 30.859
> 2.73
> 21.049
> 4.2696
> 13.649600
> 1141
> 1121
> 2013
> 3.04
> 29.249
> 2.57
> 20.89%
> 3.609
> 14.299600
> 1206
> 1159
> 2014
> 3.61
> 28.88%
> 3.15
> 22.049
> 2.8796
> 15.269600
> 1212
> 1160
> 2015
> 2.64
> 29.390
> 2.79
> 32.73%
> 10.4296
> 22.279600
> 1225
> 1196
> 2016
> 2.46
> 28.899
> 2.04
> 19.78%
> 3.3396
> 13.699600
> 1357
> 1301
> 2017
> 0.84
> 28.959
> 0.37
> 5.52%
> 3.290
> 3.829600
> 1506
> 1468
> 2018
> 1.83
> 30.08%
> 1.18
> 12.529
> 5.8296
> 8.339600
> 1510
> 1491
> 2019
> 3.92
> 31.829
> 3.50
> 25.309
> 3.899
> 15.909600
> 1515
> 1467
> 2020
> 0.41
> 30.05%
> 0.15
> 4.0096
> 7.5196
> 2.669600
> 1541
> 1469
> 2021
> 2.53
> 29.579
> 2.27
> 23.72%
> 1.949
> 16.049600
> 1514
> 1508



> [!NOTE] [图片 OCR 识别内容]
> PASS
> Sharpe of 2.32is above cutoff of 2.07
> Fitness of 1.81 is above cUtoff of 1.
> Turnover of 29.929 is above cUtoff of 19
> Turnoverof 29.929 is below cUtoff of 709.
> Weight is well distributed over instruments。
> Returns of 18.249 is above cutoff of 8%.
> Sub-universe Sharpe of 2.11 is above cutoff of 1.42.
> Robust universe Sharpe of 1.33 is above cutoff of 0.93 (409 of Alpha):
> Robust universe returns of 9.739 is above cutoff of 7.30% (409 of Alpha):
> FAIL
> IS ladder Sharpe of 1.70 is below cutoff of 2.07 for ladder year 2: 2/18/2021...2/19/2019.


优化后的策略Sharpe得到了明显的改进，验证了该策略在A股市场上的有效性，但仍存在特定年份夏普不达标的问题。

疑问与思考：

1、如何解决上述问题使因子可提交？

2、如何分两步对alpha赋值，例如如果信号A出现，则做多（关于alpha的表达式）；如果信号B出现，则做空（关于alpha的表达式）。这里的做多和做空该如何表达

---

### 帖子 #38: 【Alpha灵感】关于未来的股票回报，个股期权波动率Smirk告诉了我们什么？
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】关于未来的股票回报个股期权波动率Smirk告诉了我们什么_20163362610711.md
- **讨论数**: 10

参考文献： **[Research Paper 20]([链接已屏蔽])  : What Does Individual Option Volatility Smirk Tell Us About Future Equity Returns?**

1.核心idea

期权波动率 **s**  **mirk** 对股票未来回报有显著的预测能力，此值越小股票未来表现越好。

2.数据搜寻
 
> [!NOTE] [图片 OCR 识别内容]
> Opr4
> VOIa_300
> Imolied volailiy oratthe money-forward C3llopions wih
> Ilari 
> 3u
> 1ED
> expirstioncf 30 days
> opt4_PU_vola_3Od
> ImolieJ volstiliy orat-hs-mone-orwrd Put Options with
> Matrix
> 349
> expiration cf 30 days
> Cal
 搜关键词implied volatility找到了最切近文章描述的数据，但文章里用的是out-of-the-money put options，平台库里似乎只有at-the-money的，目前还不懂out-the-money与at-the-money的区别。

3.Alpha构建
 
> [!NOTE] [图片 OCR 识别内容]
> We calculate our implied volatility smirk measure for firm
> ial week +
> SKEW .
> as the
> difference   between the  implied
> Volatilities
> O[ OTM
> puls and
> ATM calls;
> denoted  by
> VOLOTP
> and
> VOLATC
> respectively。 That is
> (1)
> SKEW ;
> VOLOTNP
> VOLATNC
> A put option is defined as OTM when the ratio Of strike price to the stock
> is lower than
> 0.95 (but higher than 0.80), and a call option is defined as ATM when the ratio Of strike
> t0 the stock price is between 0.95 and 1.05
> To ensure that the
> options have enough liquidity;
> WVe
> only include options with time to expiration between 10 and 60 days。
> We compute the
> weekly SKEW by averaging daily SKEW over a week (Tuesday close to Tuesday close)
> price
> price


SKEW因子的构建很简单，只需call和put隐含波动率做差
 
> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1ITOP3000
> iVATM
> Opt4_call
> Vola_3od;
> iVOTM
> opt4_put_vola_3od;
> SKEW
> iVvOTM
> IVATM;
> SKEN


之前搜索到的两数据只在USA有，所以直接在USA TOP3000尝试。Neutralization使用Subindustry。

4.绩效
 
> [!NOTE] [图片 OCR 识别内容]
> q,Mok
> IS Summary
> Period
> BOJ
> ABBreBate Data
> h3TO
> LUT
> AT
> eT[
> UTaWJOWT
> Ia「C
> TOJ
> 2.29
> 54.2996
> 1.02
> 10.7996
> 7.1896
> 3.98900
> 6,OJOK
> 5PuSS
> Year
> Sharpe
> TIOeT
> Ftness
> Retwrns
> Dawdow
> Margin
> Long Count
> Short Count
> 3
> 2 FAIL
> 7371
> 335
> 51.974
> 19.75
> 2133
> 7.5
> 135
> 1771
> 40ok
> 2712
> 30.45*
> 2
> 16.3
> 200
> 6-5
> 73-7
> 1175
> Sub-uriverse Sarpe Of 0.69
> below cUoffof 0,99
> IS ladder
> OT 1.24
> DElow CUOTTOT
> 58 for laddcryear 2. 2/16/2021..2/17/2019
> 3 O
> 2013
> 303
> _
> 1.31
> 10 -7
> 19
> 75
> 13
> 1135
> VoTCINTC0
> FTLNIA I
> mTR
> 2OJJ
> 201-
> 505
> 5932
> 277
> 1732
> T02
> 602
> T-0
> 1233
> 0.8
> 1Ook
> 2015
> 30-
> 52274
> T0 94
> 25-
> 55151
> 1401
> 1253
> 2016
> 51,37
> 036
> 573
> -05
> 1.371
> 225
> 12o5
> 2017
> 070
> 02
> D
> 32
> 3
> 11
> 1391
> 1
> 2012
> 701
> TOIT
> 2019
> 2018
> 3
> 1
> 34
> 2944
> 581?
> 157
> Uh
> 2019
> =
> 4303
> 1
> 103
> 3-5
> 4555
> 1517
> IS Summary
> UOO
> 2020
> -
> 5-3
> 607
> 4Se
> 0
> T=
> AErBtEDn
> 2.49
> 115,9796
> 0.75
> 10,6496
> 3,809
> +839o
> 721
> 31
> 517
> 3994
> 5ES
> ~14,69
> 127
> Tor
> Sharce
> UIT


初步尝试信号很明显，但是Turnover过高使得Margin也比较低。
Decay 0-->4, Turnover下降为原来的一半，Margin也提升了2倍多，Fitness大于1。
但还有2个FAIL且PC未通过。
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> PnLByCapltalzatlon
> 6OJOK
> 2750
> 5CJOK
> 270J
> 「7T
> O3r18'207
> Pl +7
> 3,717.3
> 2,550
> 0705.
> 4574
> Z404
> O3
> 3,0JUn
> 10 bCah
> 590
> SO
> ~743.97
> 00100
> 51775
> ZOOK
> 7,U
> alpha
> Broup_extra(alpha_
> 1, subindustry);
> condition
> or(rank(cap
> 〈8.4,
> rank(cap) >0.85);
> 250]
> condition?alpha
> Nal
> 201
> 2013
> 7019
> 2012
> 2013
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 7021
> Pnl +?
> 020g
> 20+09
> 40-609
> GO-BOq
> 80-10030


进一步利用可视化工具发现中市值对PnL的贡献为负，且coverage波动较大，于是加入如图操作。已得到可提交且通过PC测试的alpha。
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> TMa
> Prod CmrInn
> ADTeDLe Dnt
> 2.21
> 42.199
> 1.16
> 11.32%6
> 4.379
> 5.379003
> TD
> 
> 
> e
> N
> Ueot
> OM
>  a ot
> m
> 21
> +
> 5
> 量
> 1
> SS
> 5:
> +05
> 
> 979:
> 0
> 77T
> '17
> 2
> 5
> 〈
> Testing Status
> 55
> O
> 5
> ? Puss
>  ?IIC
> PEONC
> Sd AInhIq』 Ln
> OnAlhAroIyury Ul
> Check Submlsslon
> Submlt Alpha


---

### 帖子 #39: 【Alpha灵感】凸显理论（Salience Theory）
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

### 帖子 #40: 【Alpha灵感】基于反事实模拟的中国股市涨跌停板磁吸效应研究
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】基于反事实模拟的中国股市涨跌停板磁吸效应研究_20051302553879.md
- **讨论数**: 9

**研报出处：**

[计量经济学报]([链接已屏蔽])  ››  [2021, Vol. 1]([链接已屏蔽])  ››  [Issue (1)]([链接已屏蔽])  : 217-232. DOI:  [10.12012/2020-0008-16]([链接已屏蔽])

**作者简介:**

陆昌, 研究方向: 市场微观结构、投资者行为，中国科学院数学与系统科学研究院

刘洋, 博士, 研究方向: 实证资产定价、投资者情绪，中国科学院大学

杨晓光, 研究员, 研究方向: 应用经济学、博弈论，易方达基金管理有限公司

**Alpha Inspiration 描述**

中国股票市场涨跌停板前存在磁吸效应，并且跌停前更强；估值难度、交易活跃程度越高的股票，其磁吸效应越强；相比于开盘股价即接近涨跌停板价的情况，盘中股价接近涨跌停板价的情况下磁吸效应更强。

基于以下三条假设构造alpha

假设H1 在中国的A股市场上, 涨跌停板附近存在磁吸效应.

假设H2 估值更困难和交易更活跃的股票在涨跌停板处的磁吸效应更强.

假设H2.1 股票的估值难度越高, 其涨跌停板处的磁吸效应越强;

假设H2.2 股票的交易越活跃, 其涨跌停板处的磁吸效应越强.

假设H3 相较于开盘股价就接近涨跌停板价的情况, 盘中股价才接近涨跌停板价的情况下涨跌停板处的磁吸效应更强.

定义估值难度： 总市值越小、市盈率越高、不派发股息、股价与每股派息的比例越高的股票, 估值难度较大

定义交易活跃度：交易金额越高、换手率越高的股票，交易越活跃

**构造步骤：**

#### 1. 计算磁吸效应

- **涨跌停接近度** ：计算股价距离涨跌停板的百分比。

#### 2. 估值难度指标

- **估值难度** ：综合考虑总市值、市盈率、股息派发情况和股价与每股派息比例来构建一个估值难度指标。
- 
> [!NOTE] [图片 OCR 识别内容]
> Prob( Reach_Limilit) = Logistic(Bo + BiTheo_
> Probit + BnIIard;i
> 二 Cit)
> Prob
> Reuch
> Limiti.t) 是股票在时间t达到涨跌停板的概率。
> The0_
> Probit 是理论上的股票达到涨跌停板钓概率
> 可以裉据过去的数据铳计得
> Hardit 表示股票的估值难虎_
> 通过市值大小 (IIT)
> 市盈率 (卫卫;{)
> 是否派
> 息 (No_Divij) 以及价格与每股派息比例 (Price_Diviit) 来表征。
> Bo; Bi Bz 是模型参数。通过逻辑回归拟合得到
> Cit
> 是误差项


#### 3. 交易活跃度指标

- **交易活跃度** ：通过交易金额和换手率来衡量。
- 
> [!NOTE] [图片 OCR 识别内容]
> Prob
> Reuch_Limili.t)
> Logistic( Bo + BiTheo_Probijt + BzTradeiit +
> Eit
> Prob( Reach_Limilit) 和 Tleo
> Probit 的定义与上文相同。
> Tradeit 表示股票为交易活跃度
> 通过交易金额 (lmounlit) 和换手率
> Turnoverit) 来表征
> B, BI, B 和 ci,t 的定义同上。


#### 4. 综合磁吸效应指标

- **综合指标** ：结合涨跌停接近度、估值难度和交易活跃度，使用加权公式计算综合磁吸效应指标。

#### 5. 生成交易信号

- 高估值难度和高交易活跃度的股票，如果有高概率接近涨跌停板，可以考虑作为买入或卖出的信号

#### 6. 考虑开盘和盘中情况

- 根据假设 H3，可以为开盘时接近涨跌停板的股票和盘中接近涨跌停板的股票分别设定不同的阈值。

**template表达式**

av = vec_avg{x};#vector数据降维
        bv = vec_avg{y};#vector数据降维

signal = (shrt5_limit_down_price - vec_min(pv27_s_dq_low)) < (shrt5_limit_up_price - vec_max(pv27_s_dq_high)) ? -1 : 1;   #构造磁吸方向信号

Prob_trade = 1 / (1 + exp(-(-0.13 + 1.6 * 0.697 + 0.1 * bv + -0.15 * signal)));#构造基于交易活跃度信号的磁吸概率
        Prob_estimate = 1 / (1 + exp(-(-0.08 + 1.6 * 0.697 + 0.013 * av + -0.15 * signal)));#构造基于估值难度信号的磁吸概率
        trade_when(or((shrt5_limit_down_price - vec_min(pv27_s_dq_low)) <0.1,(shrt5_limit_up_price - vec_max(pv27_s_dq_high))<0.1),-rank(Prob_estimate + Prob_trade),-1) #根据文中对于研究对象的定义是股票涨跌停价9%左右样本，个人认为磁吸是反转策略，标志着非理性行为。对于高概率的上涨股票应该做空，下跌股票应该做多。


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> aV
> Vec
> aVg(pV27_
> ;_price_div_dps) ;
> bV
> Vec_aVg(pvz7_s_dq_turn );
> 1.29
> 10.089
> 1.28
> 12.309
> 22.839
> 24.41900
> sinal
> shrts
> limit_down_price-Vec_min (pvz7_s_dq_Iow ) ) < (shrts_limit_
> up_price
> Vec
> max(pV27_S
> Prob_trade
> I/ (Itexp(- (-0.13+1.6*0.697+0.1*bV+-0.15*signal ) ) );
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> Prob_estimate
> 1/ (Itexp ( - (-8.88+1.6*8.697+8.013
> aVt-0.15*signal) ) )
> 2011
> 3.06
> 8.7296
> 3.23
> 13.91%
> 1.5696
> 31.89900
> 582
> 572
> Simulation Settings
> 2012
> 2.20
> 8.1796
> 2.01
> 10.43%
> 2.36%
> 25.529600
> 632
> 627
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
> Unit Handl
> 2013
> 0.79
> 9.3996
> 0.57
> 6.4096
> 7.5696
> 13,639600
> 716
> 703
> Equity
> CHN
> T0P2000
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Verify
> 2014
> 1.46
> 9.839
> 1.37
> 11.07%6
> 5.75%
> 22.529600
> 738
> 745
> 2015
> 1.09
> 13.3796
> -1.28
> -18.5096
> 22.83%
> 27.679600
> 665
> 729
> 2016
> 1.34
> 11.5696
> 1.45
> 14.58%6
> 9.26%
> 25.229600
> 734
> 768
> Clone Alpha
> 2017
> 3.87
> 10.5396
> 6.27
> 32.85%6
> 3.46%
> 62.409600
> 854
> 869
> 2018
> 2.66
> 8.839
> 3.42
> 20.68%
> 5.74%6
> 46,839600
> 900
> 890
> 2019
> 2.46
> 9.289
> 3.22
> 21.41%
> 8.82%
> 46.129600
> 938
> 909
> Chart
> Pnl
> 2020
> 0.32
> 10.7996
> 0.17
> 3.36%
> 8.34%6
> 6,239600
> 909
> 880
> 2021
> 5.78
> 10.189
> 12.97
> 62.96%
> 2.69%
> 123.749600
> 875
> 848
> Correlation
> 7,50OK
> Self Correlation
> Highest Correlation
> Last Run:
> 5,00OK
> Prod Correlation
> Highest Correlation
> Last Run:
> 250OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Performance Comparison


**数据集**

**Dataset**

A-shares Trade Data

**FIELD**

1. pv27_s_price_div_dps
2. pv27_s_dq_turn

**Dataset**

Daily Price Limit Data

**FIELD**

1. shrt5_limit_down_price
2. shrt5_limit_up_price

经过对pv27及相关的挖掘，最终挖掘出了一个可提交的alpha，但很遗憾，该alpha没过prod corr


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> Chart
> Pnl
> 4,50OK
> 4,0OOK
> 3,50OK
> 3,00OK
> 250OK
> 2,0OOK
> 1,50OK
> 1,00OK
> SOOK
> 08/28/2013
> ISs PnL: 0.00
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> Add Alphato a List
> Openalpha details in newtab
> Check Submission
> Submit Alpha



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> 4.03
> 13.159
> 3.96
> 12.729
> 1.86%
> 19.349600
> Year
> Sharpe
> TUrOVeT
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2011
> 0.00
> 0096
> 009
> 0.0096
> 0.009600
> 2012
> 0096
> 009
> 0.0096
> 009600
> 2013
> 0096
> 009
> 0.0096
> 0.009600
> 2014
> 0096
> 009
> 0.0096
> 009600
> 2015
> 0,UU
> 0.0090
> 000
> 0.0UYo
> 009600
> 2016
> 0090
> 0.00%
> 0.0090
> 009600
> 2017
> 6.23
> 12.269
> 6.78
> 14.82%6
> 0.8796
> 24.
> 69600
> 916
> 918
> 2018
> 3.82
> 12.3196
> 3,46
> 10.28%6
> 1.7296
> 16.699600
> 751
> 756
> 2019
> 4.07
> 13.7496
> 3.89
> 12.5496
> 1.4196
> 18.249600
> 700
> 706
> 2020
> 2.89
> 14.2796
> 2.63
> 11.83%6
> 1.6296
> 16.579600
> 741
> 747
> 2021
> 4.43
> 13.9996
> 5.40
> 20.77%
> 1.1796
> 29.709600
> 765
> 776


---

### 帖子 #41: 【Alpha灵感】基于遗传规划的一致预期因子挖掘
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】基于遗传规划的一致预期因子挖掘_21146151322519.md
- **讨论数**: 0

核心交易idea是什麼？

遗传规划是一种启发式的公式演化技术，通过模拟自然界中遗传进化的过程来逐渐生成契合特定目标的公式群体，适合进行因子挖掘。本文运用遗传规划挖掘一致预期因子，是遗传规划系列研究的第四篇报告。实现层面，本文针对一致预期数据的特点量身定制数据处理方案，适配了遗传规划中的矩阵运算算法，使得短时间内进行大量因子挖掘成为可能。结果层面，本文展示了挖掘出的11个因子及其测试结果，因子可解释性较高，我们也对因子的构建逻辑和模式进行了详细分析。

遗传编程选择的一个α变量被使用，即分析师对每股收益估算的变化与收益正相关。

是否找到數據：

mdl26_ep_yield_smartestimate_fy1

是否找到Universe: 例如TOP 200, （一般金融論文都會明確說出其適用的股票類型）

All A shares.

是否找到Neutralization: Sector (Smart Search)

Market

使用什麼operator

group_rank

績效（需保證Sharpe至少大於1.3，Fitness至少大於0.6，Turnover低於45%，高於5%；透過PROD相關性測試） 
> [!NOTE] [图片 OCR 识别内容]
> 11NI
> 1OM
> 9,00OK
> 8,OOOK
> 7,00OK
> 6,00OK
> 5,00OK
> 4,000K
> 3,000K
> 2,0OOK
> 1,00OK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> IS Summary
> Period
> IS 
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.80
> 18.94%
> 1.48
> 12.76%
> 12.83%
> 13.48%0。


建议另外三个假设。

1.将智能估算增长与明年行业百分位收益增长相结合，提供了一个预期增长与当前估值对比的视角。

2.高收益率加上预期的明年行业领先增长，可能预示着回报的潜力。

3.股本回报率估算均值的变化 - 接下来的两年可能与回报率相关。

Final result:


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 15M
> 12.5M
> 10M
> 7,50OK
> 5,00OK
> 2,5OOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> IS
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.93
> 14.959 3.17
> 17.539 8.139
> 23.46%0。
  
> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> Highest Correlation
> Last Run: Mon, 02/05/2024,6:39 PM
> -0.053
> Prod Correlation
> Highest Correlation
> Last Run: Mon, 02/05/2024,6:39 PM
> 0.7
> I0Ok
> IOk
> 寰
> Ik
> 罡
> 100
> }
> 10
> 9
> 9
> 0
> 8
> 02
> 0?
> 0
> 0
> ^9
> C"
> 9
> 9
> 8:
> C"
> 9"
> 0*
> 0
> 0
> 0
> 0
> 0
> -0.7
> -0.6
> -0.5
> 0.5
> 0.6
> 0.7
> -0.4
> -0.3
> -0.2
> -0.1
> 0.0
> 0.1
> 0.4
> -0.1.
> 0.0..
> 0.2..
> 0.1..
> 0.3.
> 0.4.
> 0.5..
> 0.7
> -1.0.
> -0.7.
> -0.4.
> -0.3.
> -0.2.


Additional data:

mdl26_grwth_nxt_yr_sctr_prcntl_rnngs

anl14_mean_roe_fy2

---

### 帖子 #42: 【Alpha灵感】基于遗憾规避逻辑近似构建因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】基于遗憾规避逻辑近似构建因子_19114210824215.md
- **讨论数**: 8

标题：Alpha掘金系列之四：基于逐笔成交数据的遗憾规避因子

作者：高智威

概述：

- 该理论认为非理性的投资者在做决策时,会倾向于避免产生后悔情绪并追求自豪感,避免承认之前的决策失误。例如,投资者不愿卖出下跌浮亏的股票,是为了避免由于失败投资所导致的遗憾和痛苦心情。我们认为,同样地，当投资者卖掉手中股票后发现其开始不断上涨时，也会为了避免产生遗憾和后悔情绪,从而不会考虑再将其买回

Alpha Idea:

- **原研报逻辑**
- 1.利用逐笔成交数据，标记主动买卖单
- 2.根据主动买卖，确定总体方向
- 3.与收盘价比较，确定总体盈亏占比
- **使用数据**
- 成交量/价 ，买卖单号 共四列数据
- 偏差：数据颗粒度小，细节更多

- **构建近似逻辑**
- 1.利用ohclv数据，将涨跌情况，标记为主动买卖单占比
- 2.根据涨跌方向，确定总体方向
- 3.与当前收盘价比较，确定相对当前盈亏占比
- **使用近似数据**
- 开高收低成交量
- 偏差：数据颗粒度大，损失价格变动细节

由于原研报中研究范围为A股市场，并且使用的是逐笔交易数据，考虑到worldquant平台并没有A股的ILLIQUID_MINVOL_1M这个选项，因此使用美股作为替换

setting使用如下


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILLIQUID_MINVOLIM
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.04
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> On
> Verify
> Off
> Save as Default
> Apply


而原研报中构建了四个因子
 
> [!NOTE] [图片 OCR 识别内容]
> 买入浮亏占比因子
> (HCVOL )
> ZNvolumebuyi
> HCVOL
> total Dolume
> 卖出反弹占比因子 (LCVOL):
> LCVOL
> XN volumeselli
> Isellisclose
> totalvolme
> 买入浮亏偏离因子
> (HCP):
> YDrcebuy * Iclose
> HCP
> Close
> 卖出反弹偏离因子 (LCP):
> Bpriceselli
> LCP
> Close
> Ipbuyzclose
> Ipsellicclose


我挑选其中的HCVOL与LCP进行构建

而由于逐笔交易数据中，可以根据订单号的先后出现顺序来决定主动买单与卖单的方向，实际平台中并没有提供类似的数据，那么我构建因子只能使用近似逻辑如下

volsig = (close > ts_delay(close ,1) ? volume : -volume ) > 0;

构建主动买入成交量，即 
> [!NOTE] [图片 OCR 识别内容]
> XNvolumebuyi


同理构建

midprice =  ( close + open)/2 ;

sellprice = close < ts_delay(close , 1) ? midprice : 0 ;

即主动卖出


> [!NOTE] [图片 OCR 识别内容]
> SNTriceselli


其中使用midprice=  ( close + open)/2而不是直接使用close，是由于高频数据中，买卖价格不是全部分布在close这个价位上的，因此取开盘与收盘的平均价，作为实际交易中逐笔数据近似成交的平均价

构建的HCVOL因子表现如下


> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/DIIILLIQUID_MINVOLIM
> Convert to Multi-Simulation
> Volsig
> (close
> ts_delay (close
> 1)
> Volume
> -Volume
> 8;
> Chart
> Pnl
> Volmov
> ts
> sum(ts_delta(volsJg
> 1) ,5 ) ;
> VoImov
> ts
> SUI
> Volume, 5 )
> 3,00OK
> 2,00OK
> M
> 1,00OK
> 2013
> 2015
> 2017
> 2019
> 2021
> Clone this Alphain a newtab
> Example
> ma
> Vsuallization
> Check Submission
> Submit Alpha
> INWIN



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Stage
> IS
> 05
> Aggregate
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Data
> 0.78150.22960.134.15912.13960.559600


 
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 2 PASS
> 6 FAIL
> Sharpe of 0.78 is below cutoff of 1.58.
> Fitness of 0.13 is below cutoff of 1.
> Turnover of 150.229 is above cUtoff of 700.
> Weight concentration 44.00% is above cUtoff of 10% on 3/13/2015.
> Sub-universe Sharpe of 0.2 is below cutoff of 0.32.
> IS ladder Sharpe of 1.39 is below cutoff of 1.58 for ladder year 2: 2/16/2021...2/17/2019
> 1 WARNING
> 3 PENDING
 可以看到，HCVOL因子虽有一定的盈利能力，但是实际上距离提交最低阈值相差甚远

而LCP因子构建如下


> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/DIIILLIQUID
> MINVOLIM
> Convert to Multi-Simulation
> midprice
> close
> open )/2
> N Chart
> Pnl
> 2
> sellprice
> close
> delay(close
> 1)
> midprice
> 8
> ts
> sum(sellprice
> 30)
> Close
> 12.5M
> 10M
> 7,50OK
> 5,0OOK
> 2,50OK
> 2013
> 2015
> 2017
> 2019
> 2021
> Clonethis Alphain a newtab
> Example
> Simulate
> Visualization
> t
> Check Submission
> Submit Alpha
> tS_



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Stage
> IS
> @
> Aggregate
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> Data
> 1.5926.6991.2115.40910.56911.549600



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 7 PASS
> 1 FAIL
> IS ladder Sharpe of 1.55 is below cutoff of 1.58 for ladder year 8: 2/16/2021
> 2/17/2013.
> 1 WARNING
> 3 PENDING


可以看到，该因子的表现十分优异，并且距离提交仅有一步之遥，那么有什么办法可以修改该因子使得其通过IS呢？

---

### 帖子 #43: 【Alpha灵感】处置效应下的换手率因子策略分析
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】处置效应下的换手率因子策略分析_19149488926103.md
- **讨论数**: 0

【基础信息】

行为金融学认为人为投资是存在非理性的，并提出和论证过“处置效应”——人们对损失的厌恶远胜于他们对收益的喜爱，从而有理由相信通过量化交易克服该种“人性”从而盈利。

首先提到V型处置效应：股票盈利时，持有者往往倾向于止盈变现收益，且盈利越大出售意愿越强；而当股票浮亏时且亏损幅度变大，持有者倾向于止损，这种倾向于出售盈亏幅度较大的行为规律在理论上被称为“ V 型处置效应”。


> [!NOTE] [图片 OCR 识别内容]
> 卖出可能性
> LOSS
> Gain
> 损失
> 收益


而处置效应的存在会带来更高的换手率，当股票换手率越高，说明人们对投机泡沫价值的判断差异就越大，股票被高估的可能性就越大，因此未来的收益会显著降低。我们可以获得一个简单直接的理论——换手率与收益率负相关，即股票的流动性越好，未来的期望收益率越低。

【参考论文】

广发证券研报《基于 V 型处置效应的择时研究》，2019

华泰证券研报《华泰单因子测试之换手率类因子》，2016

【策略一——V型处置效应】

1、思路

比较t时刻和60日前的股价变化幅度，n = 60

用t日成交量/在外流通股表示换手率

减少序列的非平稳性；且以前5日的平均损益作为参照

交易考虑了A股的涨跌停限制，通过截面标准化提高因子的稳健性

2、不同市场回测情况


> [!NOTE] [图片 OCR 识别内容]
> 2OOO
> 80OOK
> 1TNN :
> DUOO
> ,OOOK
> 1,0OOk
> 2 OOOR
> Jan 17
> Jnd
> Jantg
> ln CU
> Jan2
> Jan 1
> 130'13
> Jang
> lan '20
> Jan  71
> CHNIDIITOP3OOO
> USAIDIITOP3OOO
> OOO


VNSP因子在美国股市这个不设涨跌停的市场，表现远不如A股。

原因分析：A股追涨杀跌的情绪更浓,涨跌幅限制，使得利空消息不能短期充分定价

中国市场IS结果：

**
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Spectacular
> Stage
> IS
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.1714.9003.0328.99910.95938.909600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2016
> 3.51
> 13.60%
> 5.63
> 35.04%
> 5.1
> 51.519600
> 1561
> 776
> 2017
> 2.03
> 13.21%
> 3.00
> 28.90%
> 9.28%
> 43.779600
> 1977
> 775
> 2018
> 3.00
> 15.32%
> 4.58
> 35.72%
> 4.16%
> 46.639600
> 1894
> 845
> 2019
> 2.43
> 14.959
> 3.59
> 32.579
> 7.9596
> 43.579600
> 1884
> 864
> 2020
> 0.67
> 17.35%
> 0.52
> 10.65%
> 8.9496
> 12.289600
> 1861
> 827
> 2021
> 2.05
> 15.71%
> 3.16
> 37.299
> 5.0796
> 47.479600
> 1937
> 728
**

3、不足分析

VNSP因子的sharpe和returns不够稳健，自相关问题需要注意

**
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> IS
> 0S
> 8 PASS
> Sharpe of 1.88 is above CUtoff of 1.62_
> Fitness of 2.60 is above cutoff of 1
> Turnoverof 11.499 is above cutoff of 1%.
> Turnover of 11.499 is below cutoff of 709.
> Weight is well distributed over instruments
> Returns of 23.989 is above cutoff of 6.30%.
> Sub-universe Sharpe of 1.79 is above CUtOff of 1.15.
> Competition Challenge matches。
> 2 FAIL
> Robust universe Sharpe of 0.27 is below cUtoff of 0.75 (409 of Alpha):
> Robust universe returns of 1.570 is below cutoff of 9.590 (409 of Alpha):
> PENDING
> Self-correlation check pending:
**

**【策略二——换手率与收益负相关应用】**

1、思路和所需数据

思路

（1）换手率因子各行业之间有差异，需要进行中性化处理

（2）由于该理论是经典因子，可能需要对基础因子进行衍生，以丰富的适配当下的行情。研报中也有提及换手率类的因子在单调性上表现得并不好，而衍生的乖离率类因子有较好的单调性表现， **猜测原因是换手率小的股票有一部份是大市值的股票，根据经典的小市值策略，这类股票收益率并不好** 。

所需数据

（1）换手率=某一段时期内的成交量/可流通股数×100%

（2）为符合中国市场，需要做“涨停不买入，跌停不卖出”的限制，因此用上开盘价和收盘价

3、回测情况

分别试了1天换手率、1个月日换手率平均值、1个月日换手率标准差，其中1个月日换手率标准差的综合表现最好


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> Pnl
> T0M
> 750OK
> S,OOOK
> 25OOK
> Jul'16
> Jan '17
> Jul"17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jul'20
> Jan '21


**
> [!NOTE] [图片 OCR 识别内容]
> 叫
> IS Summary
> Spectacular
> Stage
> IS
> OS
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.51
> 12.3193.62
> 26.01910.869 42.259600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2016
> 2.64
> 11.2496
> 3.55
> 22.6296
> 4.70%6
> 40.249600
> 1655
> 955
> 2017
> 3.65
> 10.6996
> 6.44
> 38.929
> 4.5496
> 72.819600
> 1935
> 977
> 2018
> 2.11
> 12.60%6
> 2.82
> 22.4890
> 4.9196
> 35.699600
> 1945
> 977
> 2019
> 2.53
> 12.5696
> 3.65
> 26.169
> 10.8696
> 41.65960o
> 1905
> 1016
> 2020
> 0.87
> 14.29%6
> 0,71
> 9,639
> 7.9796
> 13.48960
> 1878
> 1036
> 2021
> 11.60
> 13.86%6
> 32.00
> 105.49%
> 0.98%6
> 152.179600
> 1898
> 1020
**

出现1error：

- Robust universe returns of  **5.85%** is below cutoff of  **10.40%** (40% of Alpha).

4、不足分析

中国市场在真实情况下有做空限制（尤其本因子聚焦在市值较小流动性较低的股票），难点在处理Robust universe returns和Robust universe Sharpe。如何剔除这部分数据并达到submission没有写出很好的策略。

---

### 帖子 #44: 【Alpha灵感】将隔夜涨跌变为有效的选股因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】将隔夜涨跌变为有效的选股因子_20252684454295.md
- **讨论数**: 6

标题：如何将隔夜涨跌变为有效的选股因子？——基于对知情交易者信息优势的刻画

作者：国盛金工  沈芷琦、刘富兵

概述：

通常情况下，我们可以通过开盘是否跳空，猜测昨晚是否有重要消息。若没有隔夜信息，则理论上来讲，股票今日的开盘价应该大致等于昨日的收盘价；因此若观察到股价在开盘有大幅跳空，我们就可以推断，大概率存在隔夜信息。此时，再回头观察昨日的换手率，因为A股市场并不是完全有效的，部分投资者可能具有信息优势，因此若昨日换手率较高，那么相对于换手率较低的交易日，这些有信息优势的投资者（简称“知情交易者”）就更有可能提前获取了隔夜信息，在当日盘中就进行了相应的操作，这就意味着这只股票的市场有效性较弱。


> [!NOTE] [图片 OCR 识别内容]
> 图表14:
> 新因子的经济学含义
> 大跳空对应高换手,
> 则两个序列的相关系数高
> 因子位大
> 反推
> 开盘跳空幅度大
> 有隔夜信息
> 若昨日换手率高
> 则信息泄露的可能性较大,
> 市场有效性弱
> 知情交易者提前行动
> 资料来源:
> wind,
> 国盛证券研究所


idea：

在对隔夜涨跌幅的基础上，利用成交量的信息，计算隔夜涨跌幅与昨日换手率的相关系数，构造新的因子。该因子衡量了知情交易者信息优势的大小，也反映了市场有效性的强弱。

构建因子步骤：

（1）每月月底，每只股票回溯过去20个交易日，计算每日隔夜涨跌幅绝对值与昨日换手率的相关系数；

（2）做横截面市值中性化处理。

数据：open、close、pv27_turnover_d

版本1：

overnightRet = open/ts_delay(close,1) - 1;

turnover = vec_avg(pv27_turnover_d);

corr = ts_corr(overnightRet,ts_delay(turnover,1),20);

group_neutralize(rank(corr), bucket(rank(cap), range="0, 1, 0.1"));


> [!NOTE] [图片 OCR 识别内容]
> eao
> UOUIT
> (N/81/1049330
> UJUH[
> uss LTo]lu
> LU[
> JLe
> EEgoTLornlUt;elaunw;la
> O_na
> tou 「a
> 8
> 15 Summan
> uege
> IOo
> 1175
> C99
> 1
> T0.SOo


可以看出，有比较明显的信号，prod_corr也较低，但2015年下半年经历了大幅的下撤，仍然有两项达不到提交的标准。


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 8P455
> 2FalL
> Sharpecr1.99
> EelowCuohor207.
> Rcrurnsor6,8990
> belowy CUoffor8%


版本2：

overnightRet = open/ts_delay(close,1) - 1;

turnover = vec_avg(pv27_turnover_d);

corr = ts_corr(overnightRet,ts_delay(turnover,1),20);

group_neutralize(power(rank(corr), 0.1), bucket(rank(cap), range="0, 1, 0.1"));


> [!NOTE] [图片 OCR 识别内容]
> (INt1/1041400
> OT Ctta
> lrrT
> TUI
> ureUI7+ rm
> stltLEtet Tsr] (Trmo L
> Ctpme+L-l toeor
> Summary
> ITR
> esoooo
> 240
> 13.649
> 200
> 9.489
> 11,14*
> 389



> [!NOTE] [图片 OCR 识别内容]
> Pro C
> COTTCIALIOI
> Hirhe 
> CrrlI[
> 01/02/2021.331PN
> 0.6
> TOOK
> TOK
> 
> 0
> 0 &
> 05
> 回 IS
> Testing Status
> 70Pu55
> Sharpe OT240
> JUPC
> CUtOTof 207。
> Fi:nesot2
> 403
> Cuoffor
> TNC T
> 13,619
> I
> T
> Turno
> 13.649
> Eel3w CJofof 70%
> Welzh:
> CITICUCCOCFITUICnS
> eUrI
> 485
> OL Oe
> Curot
> SUC UnRaTC
> Sharpe of233
> A3CCUofor1.47
> Robusturmers
> 1.13
> J3OCUOH
> 0,961-01
> HIpTJ]
> RcbJsurrers
> UAC
> 6.519
> CUSof3.799120
> Tphaj
> IodderShJrpCor 2.65
> UC
> CUofof 2,3710 Iodderyeor
> 2/18/2021,2/19/2019,
> O
> 3 List
> Open alpha detals
> Rnal
> Check Submission
> Submit Alpha
> ~06
> 00
> ~0.T
> 00
> 04.
> 0.T
> ~0.g。
> ~0.6
> ~0.6
> 1,0
> 09
> Sorp
> 50


对相关性corr做了简单改进后，alpha可以提交。

总结：

报告中的逻辑清晰新颖，使用非常基础的量价数据反应了知情交易者和市场有效性的信息。

此外，研报中还提到了其他的改进方法，例如对隔夜涨跌幅加绝对值、对隔夜跳空因子 abs_OvernightRet_desize做正交化取残差等，但复现的效果反而没有上面的好。

---

### 帖子 #45: 【Alpha灵感】小市值狂欢之后什么策略有效？
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】小市值狂欢之后什么策略有效_21145402272663.md
- **讨论数**: 3

联想到最近国内市场，2024经历了2023年的小市值狂欢后开局惨淡，很多因子都失效了，本周一还迎来了千股跌停的奇观。我想试试小市值狂欢后，资金去哪儿了，什么策略还能奏效呢？

构造小市值对比大市值的平均收益差距以切换因子，随缘试了一些，提交了一个，添加切换条件后对比单纯的反转因子或R因子各自都有提升：

R=rank(ts_regression(returns,group_mean(returns,1,market),22,lag=0,rettype=6));

returns_c=-group_mean(returns,rank(cap)>0.8?1:0,market)+group_mean(returns,rank(cap)<0.2?1:0,market);

ts_sum(returns_c,5)>0?rank(zscore(vwap/close)*rank(ts_delta(volume,3))):rank(R)


> [!NOTE] [图片 OCR 识别内容]
> ZOM
> 1SM
> 1OM
> 5,00OK
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> o IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 5.31
> 50.579
> 3.93
> 27.729
> 12.089
> 10.969600


---

### 帖子 #46: 【Alpha灵感】市场危机下盈利波动、不确定性与股价回报
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】市场危机下盈利波动不确定性与股价回报_20103734605591.md
- **讨论数**: 2

论文题目：Earnings Volatility, Ambiguity, and Crisis-Period Stock Returns

核心idea:

在市场危机下常规的基本面因子对于股价的预测往往会失效。该论文发现，当在发生危机前公司的盈利波动比较大的情况下，投资者在危机中会对公司提出更高的风险溢价，从而推动公司的股价下滑。但是，在常规的市场环境中，盈利波动与股价涨跌的关系并不明显。因此，盈利的稳定性可以用于预测危机中因投资者担忧所导致的股价变化。

数据：

根据brain平台所建议使用的字段构建alpha


> [!NOTE] [图片 OCR 识别内容]
> Term
> Datafield
> Dataset
> Carnings Volatility oth4ol_game_
> Cps
> VOI
> Other4ol
> earning
> 1028
> annsztc
> ValuC_052013 Fundamentalzg


Universe和Neutralization的选择：

论文除了删除了一些异常值和退市的公司样本数据外，没有其他特别的筛选条件，并且对1982年和2008年美国市场的两次危机进行研究。因此选择了USA TOP3000作为Universe

Neutralization的选择则考虑了因子构建主要使用了基本面的数据，对于此类数据不同行业间的可比性相对会比较差，因此尽量采用细分行业进行中性化处理，选择了SUBINDUSTRY进行Neutralization。

因子的构建：

1、开始时，未考虑市场危机的影响，仅使用常规的盈利数据字段fnd28_annsttc_value_05201a即可比较容易的构建了一个常规因子（normal_factor）：


> [!NOTE] [图片 OCR 识别内容]
> Prol CnrrelTm
> Hisahest Correla-ion
> Lt I
> 12/25/2023,10:22 3N
> DJO
> 0.9
> 100I
> DJO
> 訾
> DJO
> 昱
> 100
> CJOn
> D0l
> 0 。
> 0 02 0?
> 0  09
> 03  09
> 27
> 7011
> 7711
> 271
> 2715
> 277
> 2018
> 7713
> 2727
> 7721
> IS Testing Status
> IS Summary
> Period
> F455
> FLl_
> Aggreaate Data
> SIaTC
> TUFMCIE
> TIIe
> RECUTIS
> UFaWUIIT
> Marein
> 2.10
> 22.7496
> 1.01
> 5.2996
> 3.3496
> 4.659600
> FrzJ
> OTTEISIF
> 0.8121
> 三-E
> CUCft0.72n3Sharpsnor Lszer Oy
> 0.
> TTTIE
> Add Alpha
> List
> Open al2h3 Jetails
> 03 +h
> Check Subrlsslon
> Submlt Aloha
> Won
> 03
> 0.0..
> 0.4.


但存在两个问题：（1）prod corr很高，没法达到提交标准，表明简单的使用该数据构建因子很容易与平台上其他的因子产生冲突;（2）论文中的核心要点完全没有涉及，没有利用市场危机与盈利波动的关系构造因子。

2、尝试利用论文的要点构造因子，一个比较直接的想法是当危机来临前使用盈利波动作为危机因子（crisis_factor）,其他情况使用normal_factor:

pre_crisis_ind==FALSE ? normal_factor : crisis_factor

但这会产生一个严重问题，如何判断什么时候是危机来临前呢？也就是pre_crisis_ind应该如何表示？论文直接使用1982和2008年两段危机进行研究，但如果是构造因子的话就显得事后诸葛，除非使用未来函数，但这样做出来的因子毫无意义。

为了解决这个困难，尝试从另外一个角度思考。虽然在危机来临前难以判断危机的出现，但危机出现后判断市场是否在危机中相对是比较容易的，当在危机中时，使用来临前盈利波动作为crisis_factor,因子的表达式可以改为：

crisis_ind==FALSE ? normal_factor : ts_delay(crisis_factor,days)

crisis_ind可以通过股价波动是否升高超过了某个阈值确定。按照以上思路构建的因子测试结果如下：


> [!NOTE] [图片 OCR 识别内容]
> 回 |5
> Testing Status
> 400ok
> 10F4SS
> Sharpe of 2.42i aboe ~Utofor
> 3,030*
> Ti-n
> 1.24
> 371'
> Cuefff
> Turn sr
> 22.045
> abOVE CUCff; 1%_
> TuFT
> -22.043
> bEIIL:f--705
> 2,00ok
> WeishtisVs
> UITCUE TrIs-rUMEN
> Sub-Urive se Sharpe
> 1 4iE3
> Ufr
> 1.05
> SEltCorrelarion
> 4316
> 匕21
> CLtCff0.7
> DJoK
> [d Coprelaip
> 6724i bEIIJf07.
> Alpha sutmissions
> TEIJJ 
> adderSarpe 12.65
> -
> CUtCff237trladderyear2 2/16/2021...2/1712019.
> WJRNING
> 272
> 7011
> 7711
> 271
> 7
> 2017
> -018
> 7713
> 7727
> 7721
> IS Summary
> Period
> Aggregate Data
> Sharpe
> TICMC
> UraMurn
> Marein
> 2.42
> 22.0490
> 1.24
> 5.8196
> 2.3390
> 5.789
> Add Alpha 
> as
> 00273l073 detalls
> 03 +
> Check Submlsslon
> Submlt Aloha


可以看到，因子的sharpe和fitness均有了较为明显的提升，最关键的是prod corr大幅下降，达到了可提交的标准。

---

### 帖子 #47: 【Alpha灵感】常见技术指标在A股测试
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】常见技术指标在A股测试_20247158390295.md
- **讨论数**: 2

## 核心思想

对8常见的技术指标进行了测试。

1. ATR 
> [!NOTE] [图片 OCR 识别内容]
> 1.计算每曰的真实范围 (TR)
> TRi
> max(Hi, Ci-l) - min(Li, Ci-l)
> 其中
> TRi 是策
> 8的真实范围
> I 是第
> 8的最高价
> Li 是第i日的最低价
> Ci-l 是第i- 1日的收盔价
> 2.计算TR的移动平均僮 (ATR)
> ATR =
> STR;
> 其中n 是移动乎均期数。通常敢14

2. MACD 
> [!NOTE] [图片 OCR 识别内容]
> MACD (Moving Average Convergence Divergence) 是-
> -种常用的技术分析指
> 标
> 用于研究股票价袼的动态。
> MACD指标的计算方法如下:
> 1.计算128EMA (指数移动平均数)  和268EMA:
> EMAI2
> X EM Ayesterday.l2
> X CIsprctoday
> 努
> 罗
> EM A26
> X EM Ayesterday: 26
> CIsprcioday
> 27
> 27
> 其中, Clsprc是曰收盔价=
> 2.计算DIF
> (差离倌)
> DIF = EMA12
> EMA2G
> 计算DEA (差离平均僮)
> DEA =
> BDEAX 8/10)
> 今BDIF X
> 2110)
> 计算MAC0柱: MACD = 2*(DIF-DEA)

3. SMI 
> [!NOTE] [图片 OCR 识别内容]
> SMI措标 (Stochastic Momentum Index) 是一和技术分析工具
> 用于测量资产的
> 动量和超买超卖情沉。它基于随机振荡器的原理
> 通过比较当前价格和一定周期内
> 的最高最低价格来确定市场的动量
> SMIN]计算包括以下几个步骤:
> 1.计算Typical Price (典型价格)
> text{TyPICa
> Price}
> fracitext{最高价}
> Iex{最低价}
> Iext盏价}31
> 2.计算Raw Stochastic (原始随杌指标)
> [textfRaw Stochastic}
> Ifrac{text{Typical Price}
> Itext{ 最低价期内的最低价}ite刈{最高价n期内的最
> 高价} - Itext{最低价n期内的最低价}} Itimes 100]
> 其中,
> ()为设定的周期
> 3.计算%K值:
> [OK = Iext{Raw Stochastic}
> ItextfnlgKRaw Stochastic的]简单
> 移动平均}]
> 4.计算%0值:
> [9D = Itext{ObKhn期简单移动平坳]
> 5.计算SM1指标:
> [textfSMI} = OK - 90]
> SMI的取值范围通常在-100到+100之间。超过+40被认为是超买
> 低于-40被认为是
> 超卖。投资者可以根据SMI的数僮和变化趋势来制定买卖决策。例如。当SMI超买

4. Aroon 
> [!NOTE] [图片 OCR 识别内容]
> Aroon是-
> -种技术分祈指标
> 用于衡量价格趋势的强度和趋势变化的时间。
> 它由两
> 个线条组成:
> Aroon Up和Aroon Down。
> Aroon Up测量了价格在一定时间范围内创造新高低的能力,
> 它的取值范围是0到
> 100。当Aroon Up接近100时
> 表示价格创造了新高低。并豆趋势较为强劲。相
> 当Aroon Up接近0时。表示价格末能创造新高低。趋势较弱。
> 遥过比较Aroon Up和Aroon Down的]数值
> 可以判断价袼趋势的方向和骚度。如果
> Aroon Up高于Aroon Down, 表示价格趋势向上;  如果Aroon Down高于Aroon
> Up, 表示价格趋势向下。
> 同时。 Aroon指标还可以用来识别价格趋势的娈化。例如
> 当Aroon Up和Aroon Down交叉时。可能预示着趋势的反转或变化。
> Aroon Up:
> Since n-day High
> Aroon Up
> X100
> Aroon DOWn.
> 7
> Days Since n-day Low
> Aroon Down
> X100
> 其中
> 1是时间周期 (例如。25天或者50天)
> Since n-day High是从呋
> 内的最高价到今天的天数, Days Since n-day Low 是从天内最低价到今天的
> 天数
> Days
> Days

5. ADX 
> [!NOTE] [图片 OCR 识别内容]
> ADX (Average Directional Index, 平均趋向指数)  是一种常用的技术分析指标;
> 主要用于衡量股票价格的趋势5度12。
> ADX的J计算方法如下:
> 1.计算正方向指标 (+DI) 和负方向指标 (DI)
> 2.计算方向索引 (DX)
> I+DI
> -DI
> DX
> X100
> +DI + -DI
> 3.计算ADX:
> ADX =
> 180x;
> 其牛
> ^你选择的时间周期 (例如
> 14天或者20天)
> ADX指标的数值范围在0至100之间3 =
> 通常
> ADX超过30代表汇价E进入趋势
> 而
> 低于30则表示汇价在区间内波动。
> 当A0X超过30时
> ADX的读值越大。说明价格
> 趋势越明显
> 衡量价格趋势5度时
> 霓对比近几天的A0X读数。观察指标趋于上
> 升或下降
> 需要u调的是_
> 虽然A0X衡量的勺是是趋势的强度
> 但它并不能确定价格趋势的方向
> 它可以用来发现市场是在区间震荡
> 还是开始了一个新的趋势12

6. Bollinger Bands 
> [!NOTE] [图片 OCR 识别内容]
> Bollinger Bands (布林带)  是一种常用的技术分析指标
> WJohn Bollingeri1980
> 年提出12
> 布林带的主要思想是利用移动平均线以及标准差预估出价值带
> 鉴于价
> 袼是环绕价值上下波动的。上突破该带即为超买。下突破该带印为超卖
> 以此来判
> 断价格与价值的相对位置'2=
> 布林带由三条线组成125=
> 1.中轨线 (Middle Line)
> N8的移动乎均线 (SMABEMA)
> 2.上轨线 (Upper Line)
> 中轨线
> N8的标准差
> 3。下轨线
>  LOWeI
> Line)
> 中轨线
> N日的标准差
> 其中
> N是你选择的时间周期 (例如。20天)
> 当价袼连触及上部布林线时
> 可能表明出现超买信号。如果价格连续触及下部布
> 林线
> 则可能表明出现超卖信号=
> 布林带的扩大和收缩可以反映市场的波动性。
> 当布林带扩大时
> 可能表示市场开始了单边趋势;  当布林带收缩时。可能表示市场
> 从拉倬或下跌中开始逐步走向乎稳
> 开始横盘震荡的趋势'
> 以下是布林带的计算公式12
> 1.布林十线 (Middle Line):
> Middle Line
> N日的移动平均线
> 2.布林上轨 (Upper Line):
> Upper Line = Middle Line + N日 的标谁差
> 3.布林下轨 (Lower Line):
> Lower Line = Middle Line - N日 的标谁差

7. Chaikin Volatility 
> [!NOTE] [图片 OCR 识别内容]
> Chaikin Volatility (Chaikin波动率)  是
> -种常用的技术分析指标
> 用于衡量股票价
> 格的波动性。 Chaikin Volatility的]计算方法如下:
> 1.计算每9的High-Low:
> High-Low
> Hiprc
> Loprc
> 其牛
> Hiprc是曰最高价。 Loprc是曰最低价。
> 2.计簟High-LowHJEMA:
> High-Low + (n - 1) X EMAyesterday. Hieh-Low
> LOW
> 其中
> [你选择的时间周期
> 3.计算Chaikin Volatility
> EMAHih-c
> LOW,LOUaY
> EMAHieh-Low=
> Uays J0
> Chaikin Volatility
> 100
> days a80
> EMAHiehl
> EMAHieh-Low;

8. EMV 
> [!NOTE] [图片 OCR 识别内容]
> EMV (Ease OfMovement Value) 是
> -种常用的技术分析指标
> 用于衡量股票价格
> 的变动容易程度
> EMVN]计算方法如下
> 1.计算十位价格
> Hiprcioday
> Loprcoday
> Hiprcyesterday
> Loprcyesterd
> Midpoint Move
> 其牛
> Hiprc是日最高价。 Loprc是曰最低价=
> 2.计算箱体比卒 (Box Ratio)
> Volumetoday/108
> Box Ratio
> Hiprctoday
> Loprctoday
> 其牛, Volume是曰交易量_
> 3.计算EMV:
> Midpoint Move
> EMV
> Box Ratio

9. Candlestick 
> [!NOTE] [图片 OCR 识别内容]
> Candlestick
> 蜡烛线表示:
> 实体 (Body)
> Open; CIose
> 影线 (Wick)
> High
> LOW
> 2.计算典型价格 (Typical Price)
> High + Low +
> Typical Price
> 3.计算实体 (Body)
> 如果 Close
> Open
> 实体是空心 (白色或透明)
> 表上涨。
> 如果 Close
> Open, 实体是实心 (黑色或填充的觑色)
> 表示下跌
> 实体的上端是 Close
> 下端是 Open。
> 4.计算影线 (Wick)
> 上影线 (Upper Wick)
> High - Max(Open; Close)
> 下影线
> 1LOWeI
> Wick)
> Min(Open, Close)
> LOW
> Close

10. MFI 
> [!NOTE] [图片 OCR 识别内容]
> MFI指标的计算步骤如下=
> 1.计算典型价格 (Typical Price)
> 典型价格是最高你。最低价和收盘价的平均
> 值。它可以用以下公式表示:
> [ Typical Price
> Irac{{High
> LOW
> Close}}{3} ]
> 其中
> (High)表示最高价,
> (Low )表示最低价
> (Close)表示收盏价。
> 2.计算原始资金流量 (Raw Money Flow)
> 原始资金流量是典型价格乘以成交
> 量。它可以用以下公式表示:
> [ Rawl Moneyl FloW
> Typical Price times Volume
> 其中
> (Volume)表示成交量
> 3.计算资金流入和资金流出:  根据典型价格的芟化惰沉
> 殊定资金流入和资金流
> 出的条件。通常情况下
> 当典型价格上升时
> 资金流入;  当典型价格下降时
> 资金流出。
> 4.计算资金比卒 (Money Ratio)
> 资金比孪是资金流入的累积和与资金流出的
> 累积和的比率。它可以用以下公式表示:
> Moneyl Ratio
> Irac{{sum Positivel Money Flow}K{{sum Nsgativel Moneyl
> Flow}} ]
> 其中
> (sum Positivel Moneyl Flow ) 表示资金流入的累积和,
> (Isum Negativel
> Money Flow) 表示资金流出的累积和。


## 实现

使用Machine辅助，并选出其中表现较好的alpha进行进一步调优

- 数据：基本量价数据
- 国家：无特定，全跑了一遍
- Universe：无特定范围，全都跑了一遍
- Neutralization: 无特定，全都跑了一遍
- operator：计算所有技术指标，并计算（5/12/20/26)的 均值/标准差/均值偏离度/标准差偏离度/偏度

## 结果

对表现较好的alpha再进行人工调优，得到了可以提交的alpha：


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.1411.3591.788.62911.18915.209600



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> OOOK
> 4,0OOK
> 2,0OOK
> 03/21/2013
> ISPnL: 825.92k
> 2013
> 2015
> 2017
> 2019
> 2021


#### 进一步优化思路

对于每一个指标的参数进行调参尝试；

对于范围类的指标，尝试多样化的数学组合方式。

---

### 帖子 #48: 【Alpha灵感】慢慢走还是过山车？
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】慢慢走还是过山车_19393270812311.md
- **讨论数**: 5

## 论文题目

- Da, Zhi, Umit G. Gurun, and Mitch Warachka. "Frog in the pan: Continuous information and momentum."  *R__eview of Financial Studies*  27.7 (2014): 2171-2218.
- Huang, Simon. "The momentum gap and return predictability."  *Review of Financial Studies* , forthcoming (2021).

## 论文概述

文章都是在描述投资者对股票动量效应的关注度和其影响因素。

其中，Da,Zhi (2014) 认为动量的积累路径很重要。如果股票A的走势是每天稳定1%的上涨，而另一只股票B每天都在大涨大跌，那么在两只股票总收益率一样的情况下，投资者会更注意到股票B。对此。他们提出了一个新的指标，信息离散度（ID），来衡量股票价格波动的特性。他们发现，信息离散度较小，即股价波动较连续的股票，投资者反应会不足。 从整个长期角度来说，Huang (2021) 强调了动量缺口对股票动量效应的影响。动量缺口是通过比较不同股票在特定时间段内收益的分布差异来定义的。Huang 发现，当动量缺口较大时，动量效应表现较差。因此，选择在动量缺口不高的情况下实施动量策略可以提高策略的表现。

## Alpha灵感

由于两篇文章涉及到的核心思想是短期与长期数据的波动性对于动量效应的负面影响，而A股市场的反转效应要远远强于动量效应，故认为可以利用两篇文章的思路来强化A股的反转因子表现

- **ID：**
  - ID = sign(过去一段时间的收益率) × (这段时间内下跌交易日% - 这段时间内上涨收益日%)
  - 并没有想到怎样可以在brain平台上表示一段时间的下跌日期和上涨日期数量？我在这里用变异系数来衡量，变异系数越大越离散，越小越连续
- **动量缺口：** 定义为全部股票 t-12 至 t-2 月累计收益的四分位差（或者 90% 分位数减 10% 分位数，二者高度相关）

## Alpha构建

根据华泰单因子测试之动量因子文章，参考其他alpha idea中提供的构建动量反转因子的思路。这里选取其中表现较为突出的一个进行原始策略构建。

原始alpha表现如图所示：


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/TOP3000
> Convert to Multi-Simulation
> 15M
> LANGUAGE
> INSTRUMENT TYPE
> 10M
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> 5,0OOK
> CHN
> T0P3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 0.08
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> On
> Verify
> Off
> 00
> IS Summary
> Period
> IS
> 05
> Save as Default
> Apply
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 22
> internal=ts_delay (ts_percentage ( returns , 60
> percentage=0. 9)-ts_percentage
> 2.45
> 18.509  3.07  29.089
> 14.599  31.439o。
> (returns , 60, percentage=o.1) ,40);
> 23
> CV=ts_std_dev ( (close/open
> 1) ,
> 20) /ts_mean ( (close/open
> 1),20);
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 24
> alphazts
> sum(-returns, 20) ;
> 25
> group_neutralize (alpha, bucket
> rank (cap)
> range='0.1,1,0.1');
> 2011
> 2.33
> 18.849
> 2.55
> 22.539
> 4.949
> 23.92%。
> 1156
> 994
> 26
> 2012
> 3.92
> 18.759
> 5.41
> 35.749
> 5.1596
> 38.1390。
> 1237
> 1059
> Clone this Alphain a new tab
> 2013
> 2.22
> 18.35%
> 2.65
> 26.099
> 5.559
> 28.4390。
> 1353
> 1029
> Example
> Simulate
> Visualization
> Add Alpha to a List
> Check Submission
> Suomit Alpha


### 在原始Alpha上增加变异系数指标

采用变异系数，由于变异系数越大越离散，越小越连续，这里的思路是如果股票离散程度较小（即投资者未完全反映）而引发的动量效应上涨会在未来反转，加入测试后，可以看到因子的表现显著提高

```
CV=ts_std_dev((close/open-1),20)/ts_mean((close/open-1),20)

```


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/TOP3000
> Convert to Multi-Simulation
> ZSM
> internal=ts_delay ( ts_percentage ( returns , 60_
> percentage=0. 9)-ts_percentage
> (returns, 60,percentage=0.1),40);
> ZOM
> 2
> CV=ts_std_dev ( (close
> open
> 1) ,
> 20 ) /ts_mean ( (close/open
> 11,201;
> 3
> alphasts
> sum(-returns, 20 )*abs ( I/CV) ;
> group_neutralize (alpha, bucket
> rank (cap
> range=
> 0.1,1,0.1'));
> 15M
> 5
> 6
> 10M
> 5,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o IS Summary
> Period
> IS
> 09
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.05
> 22.149
> 4.03
> 38.749
> 11.379
> 35.00%oo
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> Clone this Alphain a new tab
> 2011
> 2.68
> 22.199
> 2.98
> 27.379
> 5.049
> 24.679o。
> 1134
> 1015
> 
> C0
> 厂n
> AA ^Oni
> Cqn
> 2
> 刁「ol
> 4
> nnn
> Long


### 在原始Alpha上增加动量缺口排名

动量缺口窗口设置为60，思路是动量缺口越大，股票越有可能反转，结果发现并没有对因子的表现显著提高，如果改变想法为trade_when条件，可能会有更好的结果

```
internal=ts_delay(ts_percentage(returns,60,percentage=0.9)-ts_percentage(returns,60,percentage=0.1),40);

```


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/D1/T0P3000
> Convert to Multi-Simulation
> 1OM
> internal=ts_delay (ts_percentage (returns , 60,
> percentage=0. 9)-ts_percentage
> (returns , 60,percentage=0.1) ,40) ;
> 2
> CV-ts_std_dev ( (close/open
> 1) ,
> 20 ) /ts_mean
>  (close/open
> 1),20);
> 3
> alpha=ts
> SUM
> -returns
> 20
> *rank
> internal) ;
> 5,00OK
> 4
> group_neutralize (alpha, bucket ( rank(cap) , range='0.1,1,0.1'));
> 5
> 6
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.47
> 18.799  3.04
> 28.44%
> 12.419  30.289o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.66
> 18.949
> 3.00
> 24.109
> 4.0596
> 25.449o。
> 1035
> 1080
> 2012
> 3.71
> 19.51%
> 4.91
> 34.11%
> 4.70%
> 34.969。
> 1176
> 1097
> 2013
> 2.59
> 18.81%
> 3.27
> 29.999
> 4.54%
> 31.8990
> 1339
> 1042
> 2014
> 2.68
> 18.379
> 3.11
> 24.669
> 6.77%
> 26.859oo
> 1333
> 1043
> Clone this Alphain a new tab
> 2015
> 2.68
> 17.839
> 4.06
> 40.90%
> 5.139
> 45.889。
> 1346
> 1065


### 同时考虑两因素

同时加入两因素进入反转因子后，发现因子表现进一步提高，这与我们的想法一致


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHNID1ITOP3000
> Convert to Multi-Simulation
> internal=ts_delay (ts_percentage ( returns , 60,
> percentage=0. 9)-ts_percentage
> 2SM
> (returns, 60, percentage=0.1) ,40) ;
> 2
> CV-ts_std_dev ( (close
> open
> 1)
> 20) /ts_mean ( (close/open
> 1),20);
> 3
> alphazts
> SUM
> -returns
> 20
> *rank
> internal)xabs ( I/CV) ;
> ZOM
> 4
> group_neutralize(alpha, bucket
> rank(cap) , range='0.1,1,0.1'))
> 5
> 15M
> 6
> 10M
> 5,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 90
> IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.17
> 22.189
> 4.30
> 40.729
> 13.329
> 36.71 %oo
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone this Alpha in a new tab
> 2011
> 3.20
> 22.529
> 3.83
> 32.249
> 3.999
> 28.639o。
> 1066
> 1048


下方第一张图是原策略，而第二张图是增强后的策略。根据visualization可以看到，该增强反转信号策略还是集中作用在小市值股票上。对于其他市值股票也有一定的增强作用。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl By Capitalization
> 12.5M
> 1OM
> 7,5OOK
> 5,00OK
> 2,50OK
> 2012
> 2014
> 2016
> 2018
> 2020



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl By Capitalization
> 17.5M
> 15M
> 12.5M
> 1OM
> 7.5OOK
> 5,00OK
> 2,5OOK
> 2012
> 2014
> 2016
> 2018
> 2020


## 疑问

**如何对ID再定义** ：这里采用了价格的离散系数作为ID的代替变量，也可以如传统量价策略一样采用数量指标进行定义（如20天内换手率标准差？）。或许还有更好的优化方式。

**有没有更适配的反转因子** ：本例所给出的反转因子较为简单，也许和其他反转因子配合能有更好的表现

**改为交易信号而非因子本身** ：由于本身依托于反转因子，在反转因子表现不佳的大市场环境中其劣势也会被放大，我在想如果作为交易信号，来判断是动量还是反转可能有更好的表现。

---

### 帖子 #49: 【Alpha灵感】新闻动量文章启发的反转策略实现
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】新闻动量文章启发的反转策略实现_19353819839639.md
- **讨论数**: 6

标题：The Momentum of News

作者：Ying Wang, Bohui Zhang, and Xiaoneng Zhu

来源：Research papers for users：Research Paper 1

概述：

根据原文，过去有积极消息的股票，更有可能在未来产生积极消息，将好消息五分之一投资组合中的多头头寸与坏消息投资组合中的空头头寸相结合的交易策略会有超额收益。

我对其中的idea进行了尝试，但效果并不好，我猜想是因为只根据新闻情绪排序，没有将新闻情绪和真实收益构建起联系，之后考虑了二者相关性的因子，经过一些尝试发现效果也不佳，此时我想到了回归方法，也联想到了“残差”这一反转策略中的常用因子，于是我放弃动量思路，尝试构建反转策略

相关数据集：returns、volume、cap、snt_buzz_ret

Alpha Idea：

1、直接想法

将returns对前一天的情绪值做回归，残差大表示收益过高，未来有回落的倾向，策略为做空残差大的股票，做多残差小的股票，同时按市值分组中性化，setting设置为subindustry中性化，decay=20，降低换手率

表达式：

ehat=ts_regression(returns,ts_delay(snt_buzz_ret,1),120);

alpha=group_neutralize(-ehat,bucket(rank(cap),range='0,1,0.1'));

alpha


> [!NOTE] [图片 OCR 识别内容]
> TOM
> 8,00OK
> OOOK
> 4,0OOK
> 2,00OK
> 0N
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o
> IS Summary
> Period
> I5S
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.34
> 35.05%
> 0.76
> 11.399
> 15.159
> 6.509600
> MMAVAIl


可以看到是有信号的，但初次尝试效果不佳


> [!NOTE] [图片 OCR 识别内容]
> 4 PASS
> Turnover of 35.059 is above cUtoff of 1 %_
> Turnoverof 35.059 is below cutoff of 709.
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 0.88 is above CUtOff of 0.58。
> 3 FAIL
> Sharpe of 1.34is below CUtOff Of 1.58.
> Fitness Of 0.76 is below CUtoff of 1.
> IS ladder Sharpe of 1.09 is below CUtoff of 1.58 for ladder year 2: 2/16/2021...2/1712019.


2、考虑volume因子

受到Alpha灵感系列的启发，可以考虑volume的影响，如果当天volume相比于过去较大，说明市场过热，returns在之后更有可能回落

表达式：

ehat=ts_regression(returns,ts_delay(snt_buzz_ret,1),120);

alpha=group_neutralize(-ehat*ts_rank(volume,5),bucket(rank(cap),range='0,1,0.1'));

alpha


> [!NOTE] [图片 OCR 识别内容]
> 1OM
> 9,00OK
> S,00OK
> 7,00OK
> 5,00OK
> 5,00OK
> 4,00OK
> 3,000K
> 2,0OOK
> 1,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 0
> IS Summary
> Period
> IS
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.17
> 31.299
> 0.65
> 9.769
> 19.91%
> 6.24900
> ONNNN


纳入ts_rank(volume,5)后，结果却变差了，不符合直觉

3、考虑对volume回归

考虑把volume也纳入回归中，即先将volume对snt_buzz_ret回归，得到残差vhat，再将returns对vhat回归，得到残差ehat，效果等同于returns对volume和snt_buzz_ret进行二元回归，可以更好地衡量returns的偏离程度

表达式：

vhat=ts_regression(volume,ts_delay(snt_buzz_ret,1),120);

ehat=ts_regression(returns,vhat,120);

alpha=group_neutralize(-ehat*ts_rank(volume,5),bucket(rank(cap),range='0,1,0.1'));

alpha


> [!NOTE] [图片 OCR 识别内容]
> 8,00OK
> 7,00OK
> 6,00OK
> 5,OOOK
> 4,0OOK
> 3,00OK
> 2,0OOK
> 10OOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o IS Summary
> Period
> IS
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> 1.43
> 31.28%
> 0.77
> 8.999
> 9.51 %
> 5.759600


可以看到相较于开始的策略，主要是降低了回撤

4、设置退出条件

注意到小市值股票在这个策略中波动很大，考虑加入退出条件abs(returns)>0.1，类似于设置涨跌停板

表达式：

vhat=ts_regression(volume,ts_delay(snt_buzz_ret,1),120);

ehat=ts_regression(returns,vhat,120);

alpha=group_neutralize(-ehat*ts_rank(volume,5),bucket(rank(cap),range='0,1,0.1'));

trade_when(1,alpha,abs(returns)>0.1)


> [!NOTE] [图片 OCR 识别内容]
> 1OM
> 9,00OK
> S,00OK
> 7,00OK
> OOOK
> 5,0OOK
> 4,0OOK
> 3,000K
> 2,00OK
> ,OOOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o IS Summary
> Period
> IS
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.03
> 42.509
> 1.05
> 11.379
> 4.879
> 5.35900


发现此时alpha已经可以提交！


> [!NOTE] [图片 OCR 识别内容]
> 7 PASS
> Sharpe of 2.03 is above CUtOff of 1.58。
> Fitness of 1.05 is above CUtoff of 1.
> Turnover of 42.509 is above cutoff of 1%.
> Turnover of 42.509 is below cUtOff of 709
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 1.58 is above CUtOff Of 0.88.
> IS ladder Sharpe of 3.10 is above cUtOff of 2.37 for ladder year 2: 2/16/2021...2/17/2019.。


如果把ts_rank(volume,5)放在group_neutralize()外面，可以得到略好的表现，整体来看，这个策略收益很多来自小市值股票，同时波动较大，行业表现也有些集中于某个行业


> [!NOTE] [图片 OCR 识别内容]
> 1OM
> S,00OK
> 5,00OK
> 4,00OK
> 2,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> o IS Summary
> Period
> IS
> Os
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.09
> 42.24%
> 1.11
> 12.029
> 5.549
> 5.69900



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl By Capitalization
> 3,00OK
> 2,50OK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> Pnl ; 2
> 0-209
> 20-409
> 40-609
> 60-809
> 80-1009


**
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl By Sector
> 3,00OK
> 2,50OK
> 2,0OOK
> 1,5OOK
> 1,00OK
> SOOK
> SOOK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> Pnl : 2
> Technology
> Utilities
> Basic Materials
> Consumer Non-Cyclicals
> Communications
> Financial
> Consumer Cyclicals
> Industrial
> Energy
> Diversified
> Funds
> Government
**

5、设置进入条件

如果加入进入条件abs(returns)<0.075，同时setting设置为sector中性化，表现会大幅提升！同时行业集中问题得到缓解，小市值股票波动也有所降低！经过尝试，进入条件设为returns小于0.04~0.09都是能提高表现的，0.07~0.08相对更好。

表达式：

vhat=ts_regression(volume,ts_delay(snt_buzz_ret,1),120);

ehat=ts_regression(returns,vhat,120);

alpha=group_neutralize(-ehat*ts_rank(volume,5),bucket(rank(cap),range='0,1,0.1'));

trade_when(abs(returns)＜0.075,alpha,abs(returns)>0.1)


> [!NOTE] [图片 OCR 识别内容]
> 12N
> 1ON
> 8,00OK
> OOOK
> 4,00K
> 2,0OOK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> o IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.28
> 37.509
> 1.46
> 15.409
> 6.249
> 8.219600



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl By Capitalization
> 4,00OK
> 3,000K
> 2,00OK
> 1,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl By Sector
> 4,00OK
> 3,000K
> Z,0OOK
> 1,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> Pnl : 2
> Technology
> Utilities
> Basic Materials
> Consumer Non-Cyclicals
> Communications
> Financial
> Consumer Cyclicals
> Industrial
> Diversified
> Funds
> Government
> Energy


**疑问：**

- 如果不添加abs(returns)<0.075进入条件，这个alpha在小市值股票上的表现波动很大，以及行业有些集中，有哪些改进方案？
- 像abs(returns)<0.075这样的进入条件为什么能大幅提升alpha表现？这是一种过拟合还是说有相应的逻辑？直观上似乎是改善了小市值股票的表现？
- 反转策略似乎总是伴随着高换手率，除了decay，还有哪些降低换手率的办法呢？

---

### 帖子 #50: 【Alpha灵感】盈利不确定性和公司关注度
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】盈利不确定性和公司关注度_21149732774039.md
- **讨论数**: 1

标题：Earnings Uncertainty and Attention

作者：Badrinath Kottimukkalur

概述：该篇论文主要研究盈利不确定性与对随后盈利公告的关注之间的关系，以及这种关系如何影响股票价格对盈利的反应。论文提到，对盈利的较低关注会导致股票价格的反应不足，这在盈利公告后的价格持续漂移（PEAD）中得到了体现。在低不确定性公司中PEAD更强，与它们的股票价格对盈利反应不足更加一致。

Alpha idea：基于fscore_quality、fam_earn_change_pct构建盈利不稳定性指标，基于volume与mdl25_rdv421_71v构建关注度指标，对二者进行回归分析，基于回归结果预测是否出现持续性价格飘移，进而抓住市场价格走势。

所用数据：fscore_quality、mdl25_rdv421_71v、volume

首先我们测试关注度指标和盈利不稳定性指标：


> [!NOTE] [图片 OCR 识别内容]
> [1 ^
> 
> /1103
> e」
> 21CC( 
> 」
> 
> Simulation
> Simulation 2
> Simulation 3
> Simulation 4
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1 /T0P3000
> Convert to Multi-Simulation
> N Chart
> Pnl
> ANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 3EGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> VEUTRALIZATION
> DECAY
> TRUNCATION
> 1,00OK
> Subindustry
> 0.08
> ASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> SOOK
> YEARS
> MONTHS
> On
> Verify
> Off
> 02/06/2012
> Pnl: 150.12K
> Save as Default
> Apply
> O
> ~SOOK
> OOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 乡
> Mkr



> [!NOTE] [图片 OCR 识别内容]
> CU!
> 31111010
> 22 /143
> COCO
> 6
> C CTVCU1C1()
> C VC113
> [
> LCOII
> 11
> 1 |119
> Simulation 1
> Simulation 2
> Simulation 3
> Simulation 4
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1 /T0P3000
> Convert to Multi-Simulation
> N Chart
> Pnl
> ANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 3EGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> 2,00OK
> VEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.08
> 1,500K
> ASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> 1,000K
> Save as Default
> Apply
> SOOK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022


可以看出，二者在测试中具有较高的相关性，进而我们对二者进行中心化和排序处理，并对其回归分析：


> [!NOTE] [图片 OCR 识别内容]
> 导入收藏夹
> Dell
> McAfee Security
> Gmail
> 地图
> YoUTube
> G三
> 资讯
> 翻译
> CIQ
> The Zephir。
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Data
> Competitions (3)
> Events
> Learn
> &
> Refer a friend
> Simulation 1
> Simulation 2
> Simulation 3
> Simulation 4
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1/TOP3000
> Convert to Multi-Simulation 
> 21
> N
> Chart
> Pnl
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 2,00OK
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> 1,750K
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 1,50OK
> Market
> 20
> 0.08
> 1,250K
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> 1,00OK
> Wlu
> 750K
> Save as Default
> Apply
> SOOK
> 25OK
> WI
> -25OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Clone this Alphain a new tab
> Pro:
> NW


可以看出，盈利不稳定性和关注度的关联性对于价格走势具有一定的预测作用，考虑到不同规模公司受关注度不同，我们对该alpha进行group分组处理并用trade_when进一步过滤受过高关注或过低关注的公司，策略改进后表现如下：


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Data
> { Competitions (3)
> Events
> Learn
> Refer a friend
> Simulation 1
> Simulation 2
> 又
> Simulation 3
> Simulation 4
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1 /T0P3000
> Convert to Multi-Simulation
> N Chart
> Pnl
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> 2,5OOK
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 20
> 0.08
> 2,0OOK
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> 1,50OK
> Save as Default
> Apply
> 1,00OK
> SOOK
> O
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAN
> Simulate
> CAlphas
> Data
> 留 Competitions (3)
> Events
> Learn
> !
> Refer a friend
> Simulation 1
> Simulation 2
> Simulation 3
> Simulation 4
> CODE
> RESULTS
> LEARN
> DAT
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation 
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.95
> 12.619
> 0.47
> 3.159
> 5.679
> 4.999600
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 0.98
> 13.0196
> 0.45
> 2.7396
> 1.6196
> 4.209600
> 359
> 359
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> 2013
> 0.23
> 12.739
> 0.05
> 0.549
> 2.4996
> 0.859600
> 366
> 367
> 2014
> 1.74
> 11.889
> 0.97
> 3.9096
> 1.6796
> 6.579600
> 394
> 401
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 2015
> 1.32
> 12.349
> 0.77
> 4.259
> 2.769
> 899600
> 404
> 406
> Market
> 20
> 0.08
> 2016
> 0.02
> 13.7996
> 0.00
> 0.109
> 5.0596
> 0.159600
> 382
> 382
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> 2017
> 00
> 12.049
> 0.47
> 2.809
> 1.839
> 4.659600
> 397
> 394
> YEARS
> MONTHS
> On
> Verify
> Off
> 2018
> 0.17
> 12.109
> 0.03
> -0.469
> 3.399
> 0.769600
> 364
> 365
> 2019
> 0.93
> 11.869
> 0.43
> 2.679
> 1.8796
> 4.5096oo
> 392
> 391
> Save as Default
> Apply
> 2020
> 0.55
> 13.8796
> 0.25
> 2.839
> 3.0796
> 4.089600
> 420
> 419
> 2021
> 3.17
> 12.569
> 3.16
> 12.45%
> 1.369
> 19.839600
> 417
> 417
> 2022
> -1.03
> 14.429
> -0.61
> -4.98%
> 1.479
> -6.9
> 9600
> 379
> 394
> Correlation


可以看出，策略经过改进后具有更加稳定的信号，但仍存在Sharpe较低等缺陷。考虑到识别公司盈利不稳定性和价格飘移现象可以考虑采用多种数据，后续可以考虑使用不同的数据字段并修改特征构造方式，对Alpha进一步提纯以增强表现。

问题与思考：

在手工构建Alpha时，在使用group和trade_when处理后有一定改进作用，但仍不理想，有什么思路可以进一步增强人工构建Alpha的表现。

---

### 帖子 #51: 【Alpha灵感】通过期权隐含价格与股票市场价格的差异寻找投资机会
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】通过期权隐含价格与股票市场价格的差异寻找投资机会_19140570265367.md
- **讨论数**: 2

- **论文题目** ：Do Option-Based Measures of Stock Mispricing Find Investment Opportunities or Market Frictions？( [来源](/hc/en-us/community/posts/13654829566103-Research-paper-8-Do-Option-Based-Measures-of-Stock-Mispricing-Find-Investment-Opportunities-or-Market-Frictions-) ）
  **作者** ：Martijn Cremersa,Ruslan Goyenkob,Paul Schultza, and Stephen Szaurab
  **论文概述** ：该论文提出了基于期权数据的三类可能的交易策略，包括期权隐含价格与股价差异的IPD策略、看涨与看跌期权银行波动率差异偏离度的策略以及基于期权交易量和股票交易量比率的O/S策略。论文指出这些交易策略在市值较小和难以做空的股票的效果比较显著。
- **Alpha Inspiration 描述** 尝试使用论文所建议的 **IPD** 策略的核心思想构建因子。IPD（Implied price difference）是指通过Black-Scholes模型计算期权隐含的股票价格，按照该价格与股票实际市场价格差异的大小构建投资组合，同时考虑了期权的活跃度，通过未平仓头寸（open interest）在一段时间内进行加权平均对价格差异进行一定的调整。
- **Brain平台提供的参考数据集** Term                                                          Datafield                Dataset
  at-the-money call option implied volatility  mdl77_atmcallvol   model77
  **implied stock price                                  mdl169_cpl           model169**
  option volume                                            opt6_cvolu              option6
  其中IPD策略主要相关的是mdl169_cpl
- **因子的初步探索与构建** 根据IPD策略的主要思想，通过隐含价格与实际价格差异初步构建因子。由于文中指出该类策略在市值较小、流动性比较差和难以做空的股票中效果比较显著，因此平台中股票池的设置为ILLIQUID_MINVOL1M，其余按照如下默认设置：
  
> [!NOTE] [图片 OCR 识别内容]
> LIGUIIGE
> INSTRUENT TE
> Fst Fxpresson
> Frlly
> IGGIOIN
> UNIEAS 
> USs
> ILLIOUID_MINIOLTN
> DELY
> NEUTRALIZATION
> Subindustn
> OECAY
> TRUNCATION
> 0.1
> PASTEURIZATION
> UNIT HANDLING
> Verlf;
> NO TOUDUIIC
> Saye a5 Default
 因子的初步设计与测试结果：
  
> [!NOTE] [图片 OCR 识别内容]
> 序号
> 因子
> Sharpe ratio
> Fitness
> Turnover
> 1
> mdllGg_cpl-close
> 0.14
> 0.04
> 2.11%
> 2
> rank(mdllGg_cpl-close)
> 0.13
> 0.04
> 2.22%
> (尝试消除因子1中可能的极端值的影响)
> 3
> rank(ts_rank(mdllGg_cpl-close;22))
> 1.83
> 0.81
> 48.44%
> (增加论文中提到 1个月内变化的考虑)
 从上表可以看到，第三个因子的效果比较显著。除了Fitness以外，其他的指标均已达到可提交的标准。针对第三个因子，对neutralization、decay、和ts_rank中回溯时段长度三个关键参数的设置进行调整和测试,但fitness均未出现明显的改善。

- ****数据分布特征的探索和改进****  利用平台上提供的Visualization功能对mdl169_cpl的数据分布进行探索：
  
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Coverage OfUniverse
> 2,500
> 2.400
> 2,300
> 2,200
> 2012
> 2014
> 2016
> 2018
> 2020

  发现该数据域的coverage在测试期间出现了较大幅度的波动，估计是部分的数据出现缺失所导致，尝试使用ts_backfill进行改进，但效果仍然不明显
  
> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> Stage
> 15
> 0S
> BRAIN
> Simulate
> C Alphas
> Aggregate
> Data
> CODE
> RESULTS
>  Settings
> Sharpe
> Turnover
> Fitness
> Ts_backfilllrank(ts_rank(mdl169_CpI-CIose , 22)),1261
> 1.83
> 48.4496
> 0.81
> RCtupns
> Drawgown
> Marsin
> 9.43%
> 8.48%
> 3.89%

  寻找数据集中其他类似的数据域，找到另外一个类似的数据域mdl169_backfill_cpl，该数据域的coverage除了个别日期外，较mdl169_cpl更为平稳，其可视化分析结果如下：
  
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Coverage OfUniverse
> T0O0
> 2012
> 2014
> 2016
> 2018
> 2020

  使用该数据域代替mdl169_cpl,利用ts_backfill处理个别日期的缺失值，并对neutralization、decay、和ts_rank中回溯时段长度三个关键参数的设置进行调整和测试，获得了一个可提交因子：
  ```
  alpha = ts_backfill(rank(ts_rank(mdl169_backfill_cpl - close, 60)), 20)
  ```
  表现如下：
  
> [!NOTE] [图片 OCR 识别内容]
> WORLOOUANT
> Aggregate Data
> PRAIN
> Sharoe
> Turnoyer
> HIthess
> Slrulation 6
> 3.77
> 37.31%
> 1.96
> CODE
> RESULTS
> Settings
> RetUrns
> Dradown
> Margin
> 10.06%
> 3.74%
> 5.39%
> LNGUAGE
> INSTRUMENT TYPE
> Fus. Expressiur
> Euuily
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> REGION
> UNIERSE
> 2011
> 5.58
> 36.8296
> 4.49
> 17.1595
> 0.75绗
> U5:
> ILLIOJID_INOLII
> 2012
> 7.00
> 35,755
> 4,57
> 15,9395
> 0.81
> DELAY
> NEUTRALIZATION
> 2013
> 5,31
> 34,5695
> 3.55
> 11.5995
> 0.81(
> Slawy Factors
> 2014
> 5,35
> 33.1855
> 3.31
> 12.5995
> 1,185
> DECAY
> TRUNCATION
> 2015
> 4.42
> 34.779
> 2.35
> 9.809
> 1.36~
> 0.1
> 2016
> 4,58
> 39,6995
> 2.38
> 10,5895
> 0,85%
> PRSTFURIZRTION
> UNIT HANDLING
> 2017
> 2.82
> 38.3096
> 1.11
> 5.9795
> 1.56q
> On
> Werify
> 2018
> 1,13
> 40.3655
> 0.30
> 2.7595
> 2.28氽
> NAN HANDLING
> 2019
> 1,11
> 38,229
> 0.31
> 3.0595
> 3,749
> Otf
> 2020
> 2.43
> 40.98%
> 1.25
> 10.9795
> 2.02q
> Save a5 Default
> 2021
> 4.90
> 41.8895
> 3.73
> 24.2995
> 0.709

- ****进一步改进：**** 考虑两个常见的改进方向：
  1. 设置止损条件，当前一天的跌幅超过9%时止损。
  2. 以行业维度对结果进行排序。
  改进后的因子表达式：
  
> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/DI/ILLIQUID_MINVOLTM
> signal
> tS_backtilllgroup_rank (ts_
> rank (mdl169_backtill_CpL-Close,
> 601,
> Industry
> returns
> 0.09
> signal
> 201;
 改进后的因子表现得到了进步一的提升：
  
> [!NOTE] [图片 OCR 识别内容]
> Stage
> 15
> 0S
> N Chart
> Pnl
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> 4.25
> 47.299
> 2.21
> Rerurns
> Drawoon
> Marein
> 10N
> 12.749
> 3.55%
> 5.39%
> 7,50OK
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> 2011
> 4.20
> 50.4955
> 2.10
> 12.689
> 1.60珩
> 5,OOOK
> 2012
> 4.77
> 44.139
> 2.62
> 13.3391
> 1.223
> 2013
> 5,82
> 41.6255
> 4.12
> 15.2095
> 0,6536
> 2,50OK
> 2014
> 5.21
> 41.9255
> 3.82
> 15.884
> 0.93
> 2015
> 4.81
> 45.9895
> 2.54
> 12.529
> 0.94
> 2016
> 3,51
> 49,7755
> 1,57
> 9.9595
> 2.91珩
> 2012
> 2014
> 2016
> 2018
> 2020
> 2017
> 3.31
> 45.535
> 1.39
> 8084
> 1.41驮
> 2018
> 2.24
> 50.466
> 0.80
> 6.4735
> 1.572
> 2019
> 2,61
> 18,1555
> 1,09
> 8.5095
> 3.55 
> 9
> 2020
> 4.92
> 55.569
> 3.13
> 22.4594
> 1.66弘
> 2021
> 8,09
> 51.235
> 5,76
> 35.7895
> 0.553
> Check Submission
> Submit Alpha

- **后续的思考：** 1. 因子的turnover较高，尝试通过decay、ts_mean等方法改进，但会导致sharpe出现较大幅度的下降，可以尝试其他的方式优化？
  2. 论文中提到通过未平仓头寸对差异值进行加权，研究过程中曾将pcr_oi_all等加入因子中进行尝试但初步效果不太明显，后续可进一步考虑？
  3. 论文最后提到Double Sorts的方法，可尝试结合3种策略研究产生表现更好的因子，初步尝试使用IPD+Skewness组合以及IPD+Skewness+O/S组合，初步效果反而不如只使用IPD，这个方向可继续探索？

---

### 帖子 #52: 【Alpha灵感】高/低位放量因子
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】高低位放量因子_20108973243671.md
- **讨论数**: 5

**灵感来源：**

【国盛金工 量价选股】高/低位放量：从事件驱动到选股因子

**因子描述：**

高、低位放量是技术分析中经典的价量形态，通常被用于择时或事件驱动类型的研究。

高、低位放量都是有效的事件，若股价触发“高位放量”形态，往往预示着主力资金开始出货，股票未来下跌的概率较大；反之若触发“低位放量”形态，则通常表明主力资金开始进场，股票未来有正向超额。更进一步，我们发现对于“放量”的判断，将“换手率放大”改为“股价波动率放大”，高、低位放量事件的回测效果更佳。

我们将同时满足以下2个条件的事件定义为 **“低位放量”事件** ：

（1）当日收盘价处于过去120个交易日的10%分位数及以下；

（2）当日换手率高于过去120个交易日换手率的均值+2倍标准差。

类似地，将同时满足以下2个条件的事件定义为 **“高位放量”事件** ：

（1）当日收盘价处于过去120个交易日的90%分位数及以上；

（2）当日换手率高于过去120个交易日换手率的均值+2倍标准差。

主要有以下两点结论：

（1）高、低位放量都是有效的事件，若股价触发“低位放量”形态，则未来有正向超额，反之若触发“高位放量”形态，未来有负向超额；

（2）从未来30个交易日的平均累计收益和胜率上来看，高、低位放量事件的有效性，都是波动率版本优于换手率版本。

**因子构建：**

我尚未在A股市场找到日频的波动率指标，因此我使用20天的波动率mdl175_volatility并放宽时间窗口到120天，构建mdl175_volatility和ts_mean(mdl175_volatility,120)的比较，来制作volitility的trigger。对于低位和高位，分别用less(close, (ts_min(close,120)+ts_mean(close,120)/2))，less((ts_max(close,120)+ts_mean(close,120)/2), close)作为trigger。

但完成因子构建后出现了问题，交易的触发条件有了，但是研报中未直接给出权重的分配。进行一些尝试后，我先直接使用volalility作为权重，构建了


> [!NOTE] [图片 OCR 识别内容]
> IoW
> eVent
> less(close,
> (ts_min(close, 120 )+ts_
> mean(close, 120)/2) );
> high_event
> less((ts_max(close, 120 ) +ts_mean(close,120)/2), close);
> VOI
> eVent
> less(ts_std_dev (mdl175_volatility,120)*2
> ts_mean
> (md1175_volatility, 120 ) , mdl175_volatility );
> expression
> mdl175_volatility;
> hV
> high_event
> Vol_event
> 二二
> 1
> expression
> 0;
> IOW
> eVent
> Vol_event
> 二二
> 1
> ?
> -expression
> hV



> [!NOTE] [图片 OCR 识别内容]
> 12M
> 10M
> 8,00OK
> 6,00OK
> 4,00OK
> 2,00OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21


可以看到，因子受到了2015年系统性股灾的极大影响，但是Sharpe值依然能满足本次challenge要求


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0o
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.97
> 27.379
> 1.46
> 15.019
> 35.659
> 10.96900


同时Prod Corr也能满足要求。

但是同时发现购买权重的设置也有一定的讲究。如果直接设置为1，甚至也能有一个不错的结果


> [!NOTE] [图片 OCR 识别内容]
> 8,00OK
> 7,000K
> 6,00OK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> 05/20/2011
> IS Pnl: 17.82k
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21



> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.75
> 20.299
> 1.20
> 9.609
> 29.51%
> 9.46%00


但很明显，依然无法规避15年股灾的影响。

我尝试了论坛里的tips，把股灾中权重设置为NaN，但效果甚微。

此时我在想，如果结合其他因子，比如收益偏度因子


> [!NOTE] [图片 OCR 识别内容]
> 1
> IOW
> eVent
> less(close,
> (ts_min(close, 120 )+ts_
> mean(close,120)/2) );
> 2
> high_event
> less ( (ts_max(close, 120 )+ts_
> mean(close,120)/2), close);
> 3
> Vol_event
> less(ts_std_dev (mdl175_volatility, 120 )*1.5
> ts_mean (mdl175_volatility, 120 ) , mdl175_volatility) ;
> IOW
> eVent
> Vol_event
> 二二
> 1
> ?
> 0
> rank(-vec_avg(oth4l_s_tech_skewness ) *mdl175_revs1o



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 7,000K
> 6,00OK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,000K
> 06/30/2011
> IS Pnl。 424.82K
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21


股灾的回撤得到了一定的改善

但比较可惜依然没有达到提交要求


> [!NOTE] [图片 OCR 识别内容]
> PASS
> 3 FAIL
> Sharpe Of 1.76 is below CUtoff Of 2.07.
> Weight concentration 43.919 is above cUtoff of 10% on 3/26/2019.
> IS ladder Sharpe of 1.78 is below Cutoff Of 2.07 for ladder year 3: 2/18/2021...2/19/2018.


可以改进的地方有很多，比如我不是使用真实的百分位作为高低位判据，而是直接使用了mean和high,low的均值。并且使用频率过低的波动性因子可能会显著影响结果表现。同时我对于使用的权重没有很好的想法，正在使用GA进行一些自动化的探索。

在重新选择中性化参数，以及使用rank等对权重进行重整化之后，现有的结果如下


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 15M
> 12.5M
> 1OM
> 7,50OK
> 5,00OK
> 2,50OK
> 07/03/2012
> IsDnL: 2,422.65K
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> '16



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 15M
> 12.5M
> 1OM
> 7,50OK
> 04/27/2015
> IsPnl; 6,607.29K
> 5,00OK
> 2,50OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21



> [!NOTE] [图片 OCR 识别内容]
> IS
> Testing Status
> 8 PASS
> 2 FAIL
> Robust universe Sharpe Of 1.10 is below cutoff Of 1.26 (40% Of Alpha):
> Robust universe returns Of 6.69% is below cutoff of 7.34% (40% of Alpha).
> 1 WARNING
> 3 PENDING


已经非常接近提交条件。但我尚未能解决股灾中的权重分配问题。

一些题外话，我在前天发布了一个关于收益偏度的alpha灵感，但现在依然没有出现。我不确定是没有通过审核还是我没有发布成功，不知道有没有一些办法得知自己的帖子是否“已发布”，谢谢老师们的帮助。

---

### 帖子 #53: PnL = ∑(Robustness * Creativity)
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

### 帖子 #54: 【SuperAlpha灵感】因子择时模型Alpha Template
- **主帖链接**: [L2] 【SuperAlpha灵感】因子择时模型Alpha Template.md
- **讨论数**: 32

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

### 帖子 #55: 【SuperAlpha灵感】因子择时模型Alpha Template
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

### 帖子 #56: 【YZ工程优化系列】YZ72256-使用API自动完成submit
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

### 帖子 #57: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享_36617664667159.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [[链接已屏蔽])
> 结合我最近参加的新顾问培课程中关于如何利用MCP来开发、优化alpha等内容，发表我的经验，顺便谈点感想。

作为新顾问的一份子，尤其代表零编程基础和零金融学基础的双小白，刚入门的我，只能靠模仿论坛中各位大佬，用他们现有的代码，跑论坛中现有的模板，虽然是“抄作业”，但我觉得完全不丢人，因为我相信没有谁与生俱来就拥有这能力，都是从模仿开始。于是我便靠着现有资源（三阶模板）每天碰碰运气，这样做的结果是一天有一天没，两天打渔三天晒网，不是跑不出来，而是跑出来的相关性太高。特别是11月开始深挖IND地区的时候，断粮了...


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Regular
> Regular
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> 儿52079 (Me)
> 0,00
> 0.50
> 0,37
> 0.19
> 0,00
> 0,00
> Tot
> policable
> Mainlar
> Super
> Super
> Super



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 转为正式顾问


直到11月8日，参加了新顾问的线上培训，课程上老师分享了很多能提高效率的工具和方法，其中包括了如何用MCP开发alpha模板，如何用app来实现全流程自动化。又恰逢IND地区开放，于是我决定，为了提升我的研究能力，接下来一段时间专注于IND地区的alpha开发（尽管不建议新手跑IND），当然我的方法也从开始的三阶代码换成了MCP和APP工具。

经过小半个月在IND地区的实践，发现挖出来的alpha老是出现几种问题，总结如下：

- 现有模板跑出来的相关性过高，shi都吃不上一口热的；
- 相关性低的，非常容易出现“Robust universe Sharpe of  **XX**  is below cutoff of  **X** .”
- 其他常见问题。

在拜读了大量论坛经验帖子后，决定将相关性太高的alpha直接放弃，于是乎突破点就集中在了如何解决Robust universe Sharpe过低上面，这里要特别感谢ZX12447大佬的分享，让我有了灵感，再结合MCP的智慧，创建了一个专门用于优化Robust universe Sharpe的工作流。基于该工作流，我成功优化几个alpha，解决了Robust universe Sharpe不达标的问题。

优化前问题：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained Pnl
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 05
> 9PASS
> Sharoe oT 3.25
> abOVe CUOffcf 1.58
> Finess of 3.11 isabove Cutoffof 1.
> Turnover of 15,60%
> abore CUtof of 196,
> Turpoverof 15.60%
> below CUOffof 4096.
> INeisht is WelI distribu-ed oerinstruments
> Sub-universe Sharpe CT 1.4isaboire Cutoff ot 0.96.
> 2year Sharpe Of 2.58 is
> bore Cutoff of 1.58,
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier oT -
> Effective Pyramid coun-for Genius is
> These -hemes mazch with the followinE multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The finalthEME Multiplizris 2
> 1FAIL
> Robust universe Sharpe Of 0.98
> below CUTOfOf1.
> 4PENDING
 优化后效果：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> TOM
> 5OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained
> Pn
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10PASS
> Sharpe OT 3.21
> aboVe cUOff of
> Fizness of 3,01isaboire Cutoff of -
> Turnoverof 18.2896
> aboie CUtoTf 196
> Turnover of 18.28%
> below CUOff of 40%
> Weisht is WEIl distrbuzed overinstruments。
> Sub-universe Sharpe
> 1.43
> bove Cutof of 0.95,
> Robust uniers=
> Of 1.01
> abore Cutoff ot
> 2year Sharpe Of 2.15 is above CutOff of 一
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier or
> Effectiye Pyramid Counzfor Genius
> These themes mazch with the followine multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The final theme multiplieris 2
> PENDING
> Shrpe


虽然这个alpha最终因相关性过高而未被提交，但是这是我用工作流成功优化的第一个alpha，所以将它作为代表案例展示出来。任务完成后，我让MCP将本次优化过程总结成了工作流，并且每次基于该工作流成功优化后将案例添加进工作流中。


> [!NOTE] [图片 OCR 识别内容]
> 9
> 你说
> 很好请将本次对话总结为优化robust的工作流
> API请求
> 50.0054
> Roo 说
> 我来为您创建
> 完整的IN0地区Robust universe Sharpe优化工作流文档。
> 检查点
> [
> 需要新建文件
> IND_Robust_Sharpe_优化工作流 .md
> +212
> -0巴
> 二
> API请求
> 50.0033
> 任务完咸


从这以后（11月23日），我竟然恢复了口粮，并且开始提交纯ra（之前都是ppa），今天（27日）提交了3个ra，所以借用论坛一位大佬的话“ *要重视你生产的每一个alpha* ”，因为它可能就是你下一个成功提交的对象。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod
> IESTI
> Correlation
> Correlation
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.6> 1
> e.6> 1
> e6>1
> SeeC
> e.6 >
> e.6 >
> anonymOUs
> Reaular
> ACTTVE
> 11/2712025 EST
> IND
> TOPSOO
> 0.58
> 0.61
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> 0.30
> 0.68
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> ReadyToSubmit
> 0.14
> 0.66
> anonymoUs
> Regular
> ACTIVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.41
> 0.49
> anonymOUs
> Reaular
> ACTTVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.13
> 0.70
> anonymoUs
> Reaular
> ACTTVE
> 11/25/2025 EST
> IND
> TOPSOO
> O.00
> 0.65
> anonymOUs
> Reaular
> ACTTVE
> 11/23/2025 EST
> IND
> TOPSOO
> 0.02
> 0.68
> anonymoUs
> ACTTVE
> 11/02/2025 EST
> IND
> TOPSOO
> O.00
> 0.17
> Reaular


最后送给诸君一句话并附上工作流：
 **The journey of a thousand miles begins with one step. JUST DO IT.**

```
# IND地区Robust Universe Sharpe优化工作流## 问题背景在IND地区alpha开发中，经常遇到**Robust universe Sharpe略低于1.0**的问题，导致无法提交。本工作流基于社区经验和实际案例，提供系统化的解决方案。## 工作流概览```mermaidgraph TD    A[诊断问题] --> B{分析差距}    B -->|差距<0.1| C[轻度优化]    B -->|差距>0.1| D[重度优化]    C --> E[时间参数调整]    C --> F[运算符优化]    D --> G[结构重构]    E --> H[测试验证]    F --> H    G --> H    H --> I{是否达标}    I -->|是| J[提交准备]    I -->|否| C```## 诊断阶段### 1. 问题识别```python# 检查Robust universe Sharpe指标LOW_ROBUST_UNIVERSE_SHARPE:  - result: FAIL  - limit: 1.0  - value: 0.98  # 差距0.02```### 2. 差距分析- **轻度问题**: 差距 < 0.1 (推荐本工作流)- **重度问题**: 差距 > 0.1 (建议重构alpha逻辑)## 优化工具箱### 核心优化方法#### 1. 时间参数调整 (最有效)```python# 原始ts_backfill(x, 60) → ts_backfill(x, 75)group_backfill(x, sector, 120) → group_backfill(x, sector, 275)# 推荐参数范围- ts_backfill: 60 → 75, 90, 120- group_backfill: 120 → 180, 252, 275```#### 2. 运算符增强```python# 添加稳定性运算符group_zscore(x, sector)        # 标准化信号ts_scale(x, 0.5)               # 时间序列缩放signed_power(x, 0.6)           # 符号幂变换```#### 3. 中性化优化```python# 尝试不同中性化组合group_neutralize(x, industry)group_neutralize(x, sector)group_neutralize(x, subindustry)group_neutralize(x, market)  # 对模型数据类Alpha特别有效```**中性化策略选择指南**：- **模型数据类Alpha**：优先尝试MARKET中性化- **基本面数据类Alpha**：优先尝试SECTOR/INDUSTRY中性化- **技术指标类Alpha**：根据数据特性选择合适的中性化层级#### 4. 截尾处理优化```python# 调整winsorize参数winsorize(x, std=4) → winsorize(x, std=3)winsorize(x, std=4) → winsorize(x, std=5)```## 实战案例### 案例1：IND地区imb5_score优化**原始alpha (FAIL)**```pythonfilled_score = ts_backfill(imb5_score, 60);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);signed_alpha = signed_power(neutralized, 0.5);final_alpha = group_backfill(signed_alpha,sector,120,std=4);final_alpha```- Robust Sharpe: 0.98 (FAIL)**优化版本1 (PASS)**```python3```- Robust Sharpe: 1.02 (PASS)**优化版本2 (简化版)**```pythonfilled_score = ts_backfill(imb5_score, 75);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);final_alpha = group_backfill(neutralized,sector,275,std=4);final_alpha```- Robust Sharpe: 1.01 (PASS)### 案例2：IND地区score_analyst_estimate_revisions优化（中性化策略优化）**原始alpha (FAIL)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 138), std=0.92), 108), 0.8), densify(sector))```- Robust Sharpe: 0.99 (FAIL)- 数据字段：score_analyst_estimate_revisions (覆盖率86.45%，金字塔乘数1.6)**优化版本 (PASS)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 150), std=0.85), 120), 0.8), densify(market))```- **关键优化**：中性化从SECTOR改为MARKET- **参数调整**：ts_backfill(138→150), ts_zscore(108→120), winsorize(std=0.92→0.85)- **性能提升**：  - Robust Sharpe: 0.99 → 1.11 (+12.1%)  - PnL: 11,095,177 → 12,997,115 (+17.1%)  - Sharpe: 2.56 → 2.62 (+2.3%)  - Fitness: 2.06 → 2.51 (+21.8%)  - 周转率: 16.63% → 13.66% (-17.9%)**核心洞察**：对于IND地区的模型数据类Alpha，MARKET中性化配合适当的时间窗口调整能有效提升Robust Sharpe表现，同时改善整体性能指标。## 系统化优化流程### 步骤1：基础诊断1. 运行原始alpha获取基准数据2. 记录所有检查项结果3. 重点关注Robust universe Sharpe差距### 步骤2：轻度优化 (差距<0.1)```python# 第一轮：时间参数调整尝试组合：- ts_backfill(60→75), group_backfill(120→275)- ts_backfill(60→90), group_backfill(120→252)- ts_backfill(60→120), group_backfill(120→180)```### 步骤3：运算符增强```python# 第二轮：添加稳定性运算符在group_neutralize后添加：- group_zscore(x, sector)- ts_scale(x, 0.5)- signed_power(x, 0.6)```### 步骤4：参数微调```python# 第三轮：参数优化调整：- winsorize std参数 (3,4,5)- signed_power指数 (0.5,0.6,0.7)- decay值 (0,5,20)```### 步骤5：验证与选择1. 比较所有优化版本的性能2. 选择运算符最少的版本3. 确保其他指标不受影响## 避免过拟合原则### 运算符数量控制- **理想**: 3-5个运算符- **可接受**: 6-8个运算符  - **风险**: >8个运算符### 经济意义保持- 每次优化应有合理的金融解释- 避免单纯为了提升指标而堆砌运算符- 保持alpha逻辑的简洁性和可解释性## IND地区特殊注意事项### 数据特性- Universe: 仅支持TOP500- 中性化选项有限- 数据字段相对较少### 优化策略1. **优先时间参数调整** - 对IND地区最有效2. **谨慎使用复杂运算符** - 避免过拟合3. **关注数据质量** - IND地区数据相对稀疏## 成功指标### 主要目标- ✅ Robust universe Sharpe ≥ 1.0- ✅ 其他检查项全部PASS- ✅ 运算符数量控制在合理范围### 次要目标  - 📈 IS Sharpe保持或提升- 💰 PnL表现稳定- 🔄 Turnover在合理范围内## 工具与资源### BRAIN平台工具- `get_platform_setting_options()` - 获取有效设置- `create_simulation()` - 测试优化版本- `get_alpha_details()` - 分析详细结果### 社区经验- **group_backfill/ts_backfill** - 时间参数调整最有效- **group_zscore** - 增强信号稳定性- **winsorize** - 处理异常值- **避免过度复杂化** - 保持alpha简洁## 总结本工作流通过**系统化的诊断→优化→验证**流程，有效解决IND地区Robust universe Sharpe问题。基于成功案例经验，关键优化策略包括：1. **精准诊断** - 明确问题差距和数据类型2. **中性化策略优化** - 根据数据类型选择合适的中性化层级3. **时间参数调整** - 适当延长时间窗口增强稳定性4. **避免过拟合** - 保持alpha逻辑简洁性和经济意义### 成功案例验证**score_analyst_estimate_revisions优化案例**证明了：- **MARKET中性化**对模型数据类Alpha效果显著- **参数微调**能同时提升多个性能指标- **整体性能提升**：Robust Sharpe +12.1%，PnL +17.1%，Fitness +21.8%通过这个方法，可以将接近达标的alpha（如0.98-0.99）成功优化到合格水平（≥1.0），同时显著提升整体性能表现。
```

---

### 帖子 #58: 【学习资料】BRAIN小贴士(这里有你想要的硬核内容！持续周更中）Pinned
- **主帖链接**: https://support.worldquantbrain.com[L2] 【学习资料】BRAIN小贴士这里有你想要的硬核内容持续周更中Pinned_15152019662487.md
- **讨论数**: 37

该帖子将被用来记录BRAIN团队提供的小贴士，欢迎跟帖评论、提问。

[香港地区的同学如何登陆？ – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[L2] 香港地区的同学如何登陆_31134702342167.md)

---

### 帖子 #59: 【工具优化】华子哥插件的FireFox版本经验分享
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

### 帖子 #60: 3E large 3C less
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

### 帖子 #61: 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案
- **主帖链接**: [L2] 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案.md
- **讨论数**: 1

首先感谢 XZ23611 分享的帖子：
“ [【提升Check Submission效率】一些可以提升Check Submission的Tips，效率提高10倍以上](../worldquant brain赛博游戏王/[Commented] 【提升Check Submission效率】本地计算自相关和提高check的tips效率提高10倍以上代码优化.md?page=1#community_comment_28755853659031) ”其中分享的代码非常实用。一般情况下，使用这套代码本地计算self-correlation值与Brain 平台计算的结果值，一般只会有 0.02~0.05 的差异，对于实战完全够用。

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

### 帖子 #62: 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案_29002502448279.md
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

### 帖子 #63: assuming final_example_alpha_list is your listfunction to divide the list into chunksdef divide_chunks(alpha_list_with_settings, n):    looping till length l    for i in range(0, len(alpha_list_with_settings), n):        yield alpha_list_with_settings[i:i + n]divide the list into chunks of size 10n = 10chunks = list(divide_chunks(final_example_alpha_list, n))print each chunkfor i, chunk in enumerate(chunks):    print(f"Chunk {i+1}:")    print(chunk)    print("\n")
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md
- **讨论数**: 15

**【重要】使用API请关闭VPN！使用API请关闭VPN！使用API请关闭VPN！**

目前API已经基本可以实现平台上所有的靠鼠标点击的功能了吧，这些是我的总结。有些功能可能没有总结到，欢迎大家配合这篇文章一起使用👉 [Brain API技巧：如何挖掘API](../顾问 FX25214 (Rank 22)/[L2] Brain API技巧如何挖掘API代码优化_20309362198679.md)


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Consultant program
> Events
> Refer a friend
> SignIn
> Sign In
> Email
> Email field empty
> Password
> Forgot password
> Sigm
> Don't have an account? Sign Up here
> Having trouble signing in? Contact support


**STEP 1:Authentication 登录账号** 

- 描述: Authenticates the user using the /authentication endpoint 使用/authentication端点进行身份验证
- **每个登录Session有效期为4小时，请检查你的代码切勿频繁登录，24小时内登录超过25次将会冻结账户**
- Input: A POST request to the /authentication endpoint with a basic authorization header (username and password) 向/authentication端点发送带有用户名和密码的POST请求
- Output: On success, it returns a JSON Web Token (JWT). If biometrics sign-in is enabled, it returns a 401 status code and a header location。成功后，返回一个JSON Web Token (JWT)。 **如果系统启用了生物识别登录（针对非中国大陆用户），它将返回401状态代码和一个header位置。这个header位置是一个链接（or QR code)，需要扫码完成。**
- Code:

```
import requests
#建议将用户名密码放到另外的文件内存储
# Define the path to the text file that store your username and password, the first line should be your username and second line to be your password.
file_path = "credentials.txt"

# Initialize variables to hold the username and password
username = ""
password = ""

# Open the file and read the lines
with open(file_path, "r") as file:
    username = file.readline().strip()  # Read the first line for the username and strip newline characters
    password = file.readline().strip()  # Read the second line for the password and strip newline characters# Create a session to persistently store the headers s = requests.Session() # Save credentials into session s.auth = (username, password) # Send a POST request to the /authentication API response = s.post('[链接已屏蔽])
```

**一种解决超时登出的解决方案（超过4小时会登录session会过期）**

```
def sign_in(credentials_path):    import requests    from time import sleep    # Initialize variables to hold the username and password    username = ""    password = ""    # Open the credentials file and read the username and password    try:        with open(credentials_path, "r") as file:            username = file.readline().strip()  # Read the first line for the username and strip newline characters            password = file.readline().strip()  # Read the second line for the password and strip newline characters    except FileNotFoundError:        print(f"Error: The file '{credentials_path}' was not found.")        return None    except Exception as e:        print(f"An error occurred while reading the credentials file: {e}")        return None    # Create a session to persistently store the headers    s = requests.Session()    # Save credentials into the session    s.auth = (username, password)    while True:        try:            # Send a POST request to the /authentication API            response = s.post('[链接已屏蔽])            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx            print("Authentication successful.")            break  # Exit the loop on success        except requests.HTTPError as e:            print(f"HTTP error occurred: {e}. Retrying...")  # Provide more specific error message            sleep(10)        except Exception as e:            print(f"Error during authentication: {e}. Trying to login again.")            sleep(10)    return ssession = sign_in("path/to/your/credentials.txt")
```

```
while True:    s = sign_in("path/to/your/credentials.txt")    try:        #Run Alpha code        print("running")    except:        print('connection down')        s = sign_in()
```

```

```

**STEP 1.1 Get Dataset like Data Explorer**  查找数据集


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> Region
> Delay
> Universe
> Data
> Datasets
> USA
> TOP3000
> Search
> Category
> Coverage; %
> Value score
> Alphas
> Users
> Name; description
> AlLcategories
> to
> 100
> to
> to
> t0
> Clear
> Dataset
> Fields
> Coverage
> Value Score
> Users
> Alphas
> Research Papers
> Analyst Estimate Data for Equity
> 350
> 609
> 3727
> 55502
> Report Footnotes
> 318
> 41%
> 3832
> 31093
> Company Fundamental Data for Equity
> 886
> 749
> 23292
> 674330
> [1],[2],[3], [4]
> Fundamental Scores
> 31%
> 151
> 674
> [1]
> Systematic Risk Metrics
> 16
> 779
> 1681
> 5455
> US News Data
> 322
> 80%
> 5373
> 43803
> Ravenpack News Data
> 75
> 689
> 645
> 8842
> [1],[2],[3],[4]
> Volatility Data
> 64
> 699
> 2437
> 30093
> Options Analytics
> 74
> 709
> 2204
> 10859
> [1],[2],[3]
> Price Volume Data for Equity
> 18
> 1009
> 26455
> 828156
> [1],[2],[3],[4],[5],[6],
> [7],[8],[9],[10], [11],
> [12]


- Description: 返回DataFrame文件
- **要注意数据集的Universe、REGION的DELAY的设定，不同的设定的数据集是不同的**
- **可以通过对返回的df内的category、name、description等字段进行筛选，找到所有相关的数据集**
- Input: session, settings (which includes region, delay, universe, instrumentType)
- Output: DataFrame
- Code:

```
#Example setting
settings = {'region': 'ASI', 'delay': '1', 'universe': 'ILLIQUID_MINVOL1M', 'instrumentType': 'EQUITY'}

def get_datasets(session, settings):
    url = "[链接已屏蔽] +\
        f"instrumentType={settings['instrumentType']}®ion={settings['region']}&delay={settings['delay']}&universe={settings['universe']}"
    result = session.get(url)
    datasets_df = pd.DataFrame(result.json()['results'])
    datasets_df['instrumentType'] = settings['instrumentType']
    datasets_df['region'] = settings['region']
    datasets_df['delay'] = settings['delay']
    datasets_df['universe'] = settings['universe']
    return datasets_df
```

**Get Datafield like Data Explorer**  获取所有满足条件的数据字段及其ID

 
> [!NOTE] [图片 OCR 识别内容]
> !C匕骘_
> BRNf
> Simulate
> CAlphas
> Learn
> Data
> 罟
> Competitions (0)
> {8 Team
> Community
> Consultant program
> Region
> Universe
> Data
> Datasets
> Analyst Estimate Data for Equity
> USA
> TOP3000
> Fields
> Description
> Search
> Coverage; %
> Type
> Alphas
> Users
> Name; description
> to
> 100
> All
> to
> to
> Clear 
> Field
> Description
> Type
> Coverage
> Users
> Alphas
> adjysted_Detincome 止
> Adjusted net income
> forecast type (revisionlnewl.)
> Matrix
> 879
> 390
> 1186
> anl4_ads1detailafv1 10_bk
> Broker name (int)
> Vector
> 699
> 30
> anl4_ads1detailafv1 10_estvalue
> Estimation Value
> Vector
> 699
> 17
> 38
> anl4_ads1detailafv1 10_person
> Broker Id
> Vector
> 699
> anl4_ads1detailafv1 10_prevval
> The previous estimation of finanicial item
> Vector
> 699
> 15
> 32
> anl4_ads1detailqfv1 10_bk
> Broker name (int)
> Vector
> 6396
> 19
> anl4_ads1detailqfv1 10_estvalue
> Estimation Value
> Vector
> 639
> 10
> anl4_ads1detailqfv1 10_person
> Broker Id
> Vector
> 639
> 2
> anl4_ads1detailqfv1 10_prewal
> The previous estimation of finanicial item
> Vector
> 639
> 10
> anl4_adxqfv110_down
> Number of lower estimations
> Vector
> 709
> 12
> anl4_adxqfv1 10_high
> The highest estimation
> Vector
> 709
> 11
> https:/ /platform worldquantbrain.com /data/data-setslanalyst4idata-fieldsyanl4_adjusted_netincome_ft
> Delay
> anl4
 

- Description: 根据Dataset id来获取数据字段
- **Dataset ID可以通过前步的df内获取，或者在平台网页上，鼠标放到相应的dataset上，在左下角即可看到data set id和datafield id**
- **要多注意data field的category和operator的匹配，尤其MATRIX和VECTOR的比较**
- Input: s, instrument_type, region, delay, universe, dataset_id, search
- Output: 返回DataFrame
- Code:

```
def get_datafields(
    s,
    instrument_type: str = 'EQUITY',
    region: str = 'USA',
    delay: int = 1,
    universe: str = 'TOP3000',
    dataset_id: str = '',
    search: str = ''
):
    if len(search) == 0:
        url_template = "[链接已屏蔽] +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50" +\
            "&offset={x}"
        count = s.get(url_template.format(x=0)).json()['count'] 
    else:
        url_template = "[链接已屏蔽] +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&limit=50" +\
            f"&search={search}" +\
            "&offset={x}"
        count = 100

    datafields_list = []
    for x in range(0, count, 50):
        datafields = s.get(url_template.format(x=x))
        datafields_list.append(datafields.json()['results'])
    datafields_list_flat = [item for sublist in datafields_list for item in sublist]

    datafields_df = pd.DataFrame(datafields_list_flat)
    return datafields_df
```

 **STEP 2: Simulating an Alpha**  回测Alpha


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> :
> Competitio
> Simulation 1
> Settings
> USA/D1/TOP3000
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save as Default
> Apply
> 20
> 21
> 22
> regular
> expression
> Clone this Alphaina new tab
> Example
> Simulate


- **描述: 用于回测Alphas, 一个完整的alpha（JSON）包括Settings （JSON）和 表达式（regular字段）组成，通过API 将这个alpha POST到服务器，成功的POST将获得一个在服务器的url （‘Location’）并获得回测进度条。**
- Input: A POST request to the /simulations endpoint with a JSON object that includes the settings of the simulation and the expression 向/simulations端点发送包含回测设置和表达式的JSON对象的POST请求
- Output: On success, it returns a URL in the HTTP response header Location. This URL can be used to check the progress of the simulation 成功后，它在HTTP响应头Location中返回一个URL。此URL可用于检查回测的进度；如果没有检查到Location ，则说明你的Alpha发送产生了错误。请检查常见错误👉 [BRAIN API及日常回测时常见的错误 – WorldQuant BRAIN]([L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md)
- **在大规模回测中，建议您将回测的Alphas List，回测时间和是否成功回测（lcoation url）存储在一个文件中（csv，json或其他格式），以方便debug和管理**
- Code:

```
simulation_data = {
    'type': 'REGULAR',
    'settings': {
        'instrumentType': 'EQUITY',
        'region': 'USA',
        'universe': 'TOP3000',
        'delay': 1,
        'decay': 15,
        'neutralization': 'SUBINDUSTRY',
        'truncation': 0.08,
        'pasteurization': 'ON',
        'unitHandling': 'VERIFY',
        'nanHandling': 'OFF',
        'language': 'FASTEXPR',
        'visualization': False,
    },
    'regular': 'close'
}
simulation_response = s.post('[链接已屏蔽] json=simulation_data)
```

 **STEP3: Alpha Simulation Status and Results Retrieval**  Alpha回测状态和结果检索


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> 159
> Simulations usually take a few minutes Ormore:
> Click here to cancel the simulation.
> TIP
> Submit Alphas with Iow Correlation to your other Alphas。
> Properties
> Simulate to saVe
> Name
> Category
> Currently 'anonymous'
> None
> Color
> Selectladd tags
> None
> Description
> Description
> Tags


- **描述：检查alpha回测的进度并检索结果, 一个成功的回测会获得一个服务器内的URL，在response里的‘Location'字段可以获得该URL，复制到浏览器内也可以访问。**
- **如果alpha 表达式有误或已经存在历史的回测中，将不会得到此URL，则回测失败。同时回测的最大上限为10个，所以在POST的任务中，如果FAIL则可以设置sleep一段时间后重试。**
- Input: A GET request to the URL returned when sending an alpha for simulation 向发送alpha模拟时返回的URL发送GET请求
- Output: If the alpha is still simulating, a Retry-After header is returned. Once the simulation finishes, the response includes a JSON object from which you can retrieve the alpha id 如果alpha仍在模拟中，返回Retry-After头。回测完成后，响应包含一个JSON对象，您可以从中检索alpha id （注意alpha id为7位，如：m8qlQZ1）
- Code:

```
from time import sleep

simulation_progress_url = simulation_response.headers['Location']
finished = False
while True:
    simulation_progress = s.get(simulation_progress_url)
    if simulation_progress.headers.get("Retry-After", 0) == 0:
        break
    print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
    sleep(float(simulation_progress.headers["Retry-After"]))
print("Alpha done simulating, getting alpha details")
alpha_id = simulation_progress.json()["alpha"]
alpha = s.get("[链接已屏蔽] + alpha_id)
print(alpha.json())
```

 **STEP 4: Record Sets of Alpha Simulations**  Alpha PnL绩效历史


> [!NOTE] [图片 OCR 识别内容]
> -SOOK
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Needs
>  IS
> Period
> TRAIN
> TEST
> IS
> O
> Improvement
> Summary
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.20
> 1.149
> -0.08
> -1.909
> 28.549
> -33.389600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2017
> 1.77
> 1.229
> 1.71
> 11.709
> 4.159
> 191.279000
> 1096
> 1936
> 2018
> 0.20
> 1.199
> 0.08
> 1.7896
> 10.019
> 29.789000
> 1093
> 1955
> 2019
> 0.04
> 0.899
> 0.01
> 0.289
> 6.0596
> 6.389600
> 1057
> 1979
> 2020
> -1.23
> 1.229
> -1.43
> -16.989
> 25.269
> -277.490000
> 1014
> 2020
> 2021
> 6.29
> 1.559
> 16.28
> -83.709
> 4.509
> -1,081.04900
> 1048
> 2035
> Long


- Description: Retrieves record sets containing the information about simulations 获取PnL图表的信息
- Input: A GET request to the /alphas/<alpha_id>/recordsets/<record set name> endpoint 向/alphas/<alpha_id>/recordsets/<record set name>端点发送GET请求
- Output: Returns a record set containing the information about your simulations for each trading day 返回日度级别的PnL信息
- Code:

```
from time import sleep

finished = False
while True:
    pnl = s.get("[链接已屏蔽] + alpha_id + "/recordsets/pnl")
    if pnl.headers.get("Retry-After", 0) == 0:
        break
    print("Sleeping for " + pnl.headers["Retry-After"] + " seconds")
    sleep(float(pnl.headers["Retry-After"]))
print("PnL retrieved")
```

 **Alpha Management**  获取特定alpha的表现

- Description: Manages alphas
- Input: A GET request to the /alphas/<alpha id> endpoint 向/alphas/<alpha id>端点发送GET请求
- Output: Returns a JSON object representing the alpha 返回Json文件，包含Alpha的所有信息，以下很多的功能都由此延申。
- ```
  alpha = s.get("[链接已屏蔽] + alpha_id)
  ```

 **STEP 5 Alpha List 批量获取已经完成回测的结果**

**
> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> :
> Competitions (0)
> {8 Team
> Community
> Consultant program
> 三
> 0 Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Size
> 10
> out of 51
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Search
> Select
> Selec
> Selec
> Search
> Selec
> Select
> e〉 1
> e8〉 1
> e8〉 1
> Select
> anonymous
> Regular
> UNSUBMITTED
> 07/30/2024 EDT
> USA
> TOP3000
> 0.32
> 3.189
> 1.159
> anonymous
> Regular
> UNSUBMITTED
> 07/10/2024 EDT
> USA
> TOP3000
> 1.39
> 7.299
> 1.579
> anonymous
> Regular
> UNSUBMITTED
> 07/10/2024 EDT
> USA
> TOP3000
> 1.34
> 7.0996
> 1.769
> anonymous
> Regular
> UNSUBMITTED
> 05/20/2024 EDT
> USA
> T0P3000
> 1.53
> 5.229
> 3.479
> anonymous
> Regular
> UNSUBMITTED
> 05/20/2024 EDT
> USA
> TOP3000
> 1.31
> 4.449
> 3.489
> anonymous
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 0.96
> 2.859
> 20.009
> anonymous
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 1.17
> 3.189
> 17.199
> anonymoUs
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 1.06
> 3.749
> 15.639
>  | | |
> 0oOI I3
> UNSIBNITTED
> OC /1 1 /00/
> C
> TO03O
> C 1O0
> CC0
> Page
> Tag
**

- ```
  Description: Retrieves records in the IS and OS Alpha list 获取所有在IS和OS列表的Alpha信息。这可以帮助你批量筛选出STEP2-3中，哪些回测是有信号的。建议将回测结果和之前的alpha list进行交叉比较（setting和regular （表达式）相同即为同一个alpha）
  ```
- ```
  未提交的alpha stage value是IS，已提交的stage 字段value是OS
  ```
- ```
  Input: session, total_alphas, limit
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to fetch a specific number of IS alphas (`total_alphas`) using pagination.
def get_n_is_alphas(session, total_alphas, limit=100):
    fetched_alphas = []
    offset = 0

    # Keep fetching alphas until the required number of alphas is reached or no more alphas are available.
    while len(fetched_alphas) < total_alphas:
        response = session.get(
            f"[链接已屏蔽]
        )
        alphas = response.json()["results"]
        fetched_alphas.extend(alphas)
        if len(alphas) < limit:
            break
        offset += limit
    return fetched_alphas[:total_alphas]
```

```

```

```
Check result of Checks 获得Checks的结果
```

- ```
  Description: 向/alphas/<alpha id>/check端点发送GET请求
  ```
- ```
  Input: alpha id
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  is_checks_response = session.get(f"[链接已屏蔽])
  ```

```

```

```
Check Self Correlation 自相关性检查
```

- ```
  Description: Retrieves self-correlation result by alpha_id 根据Alpha_id检查自相关性
  ```
- ```
  Input: session, alpha_id, max_retries
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to retrieve self correlation for the given alpha ID.
def get_self_corr(session, alpha_id):
    response = session.get(f"[链接已屏蔽])
    if response.status_code == 200 and "records" in response.json():
        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]
        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)
        return self_corr_df
    else:
        return pd.DataFrame(columns=["correlation"])

# Function that retries fetching self correlation for the given alpha ID up to `max_retries` times.
def get_self_corr_with_retries(session, alpha_id, max_retries=3):
    retry_count = 0
    while retry_count < max_retries:
        try:
            self_corr_df = get_self_corr(session, alpha_id)
            if not self_corr_df.empty:
                return self_corr_df
        except json.JSONDecodeError:
            pass
        retry_count += 1
        time.sleep(1)  # Wait for 1 second before the next retry
    return pd.DataFrame(columns=["correlation"])
```

```

```

```
Check Prod Correlation 全局相关性检查
```

- ```
  Description: Retrieves prod-correlation result by alpha_id 根据Alpha_id检查全局相关性
  ```
- ```
  Input: session, alpha_id, max_retries
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to retrieve prod correlation for the given alpha ID.
def get_prod_corr(session, alpha_id):
    try:
        response = session.get(f"[链接已屏蔽])
        response.raise_for_status()
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            print(f"Error while decoding prod_corr JSON for alpha {alpha_id}: Invalid or empty JSON")
            return pd.DataFrame(columns=["alphas", "max"])

        if "records" in response_data:
            columns = [dct["name"] for dct in response_data["schema"]["properties"]]
            prod_corr_df = pd.DataFrame(response_data["records"], columns=columns)
            return prod_corr_df
    except requests.HTTPError as e:
        print(f"Error while fetching prod_corr for alpha {alpha_id}: {e}")
    return pd.DataFrame(columns=["alphas", "max"])

# Function that retries fetching prod correlation for the given alpha ID up to `max_retries` times.
def get_prod_corr_with_retries(session, alpha_id, max_retries=3):
    retry_count = 0
    while retry_count < max_retries:
        try:
            prod_corr_df = get_prod_corr(session, alpha_id)
            if not prod_corr_df.empty:
                return prod_corr_df
        except json.JSONDecodeError:
            pass
        retry_count += 1
        time.sleep(1)  # Wait for 1 second before the next retry
    return pd.DataFrame(columns=["alphas", "max"])
```

```

```

```
Change Alpha properties 给Alpha更改设置，例如改名字，改颜色等
```

- ```
  Description: Change the Alpha's Property 向/alphas/<alpha id>端点发送patch请求
  ```
- ```
  Input: session, alpha_id, color or new_name
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to update the color of an alpha with the given color.
def update_alpha_color(session, alpha_id, color):
    update_data = {"color": color}
    response = session.patch(f"[链接已屏蔽] json=update_data)
    return response.status_code == 200

# Function to update the name of an alpha with the given name.
def update_alpha_name(session, alpha_id, new_name):
    update_data = {"name": new_name}
    response = session.patch(f"[链接已屏蔽] json=update_data)
    return response.status_code == 200
```

```

```

```
Get Performance Comparison 获取Performance Comparison的结果
```

- ```
  Description: Returns performance comparison for merged performance check 向/alphas/alpha_id/before-and-after-performance端点发送GET请求
  ```
- ```
  Input: s, alpha_id, team_id (optional), competition (optional)
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
def performance_comparison(s, alpha_id, team_id:Optional[str] = None, competition:Optional[str] = 'ACE2023'):
    """
    Returns performance comparison for merged performance check
    """
    if competition is not None:
        part_url = f'competitions/{competition}'
    elif team_id is not None:
        part_url = f'teams/{team_id}'
    else:
        part_url = 'users/self'
    while True:
        result = s.get(
            f"[链接已屏蔽] + alpha_id + "/before-and-after-performance"
        )
        if "retry-after" in result.headers:
            time.sleep(float(result.headers["Retry-After"]))
        else:
            break
    if result.json().get("stats", 0) == 0:
        return {}
    if result.status_code != 200:
        return {}

    return result.json()
```

```

```

```
补充：Multi-Simulation对应UI中的
```

```
    multisimulation_data = [        {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': 'USA',                'universe': 'TOP3000',                'delay': 1,                'decay': 15,                'neutralization': 'SUBINDUSTRY',                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'OFF',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': 'close'        },        {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': 'USA',                'universe': 'TOP3000',                'delay': 1,                'decay': 15,                'neutralization': 'SUBINDUSTRY',                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'OFF',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': 'open'        },        # Add more simulation data as needed    ]    # Send multisimulation request    multisimulation_response = s.post('[链接已屏蔽] json=multisimulation_data)    # Check response    if multisimulation_response.status_code == 201:        print("Multisimulation request sent successfully.")    else:        print("Error in sending multisimulation request.")
```

```
使用get方法获取multi Alpha的结果，其children的结果即为单个Alpha的Location,再对每个使用get方法，即可获得单个Alpha的id
```

```

```

```

```

```
设置Log来记录操作
```

```
import logging# Create a loggerlogger = logging.getLogger('my_logger')# Set the level of the logger. This can be DEBUG, INFO, WARNING, ERROR, or CRITICALlogger.setLevel(logging.INFO)# Create a file handler that logs even debug messageshandler = logging.FileHandler('my_log.log')handler.setLevel(logging.INFO)# Create a formatter and add it to the handlerformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')handler.setFormatter(formatter)# Add the handler to the loggerlogger.addHandler(handler)# Log some messageslogger.info('This is an info message')logger.warning('This is a warning message')logger.error('This is an error message')logger.critical('This is a critical message')
```

```
获取所有本人可用的operator
```

```
# 获取个人所使用的operatordef get_user_operator(session):    import pandas as pd    result = session.get("[链接已屏蔽])    df = pd.DataFrame(result.json())    return df
```

```

```

---

### 帖子 #64: 【日常生活贴】我的量化日记第二季
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第二季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #65: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 986

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #66: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **讨论数**: 1168

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #67: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 479

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #68: 步骤2: 计算残差与X平方的协方差
- **主帖链接**: [L2] 【有奖】SuperAlpha征文分享你独到的selection和combination方法.md
- **讨论数**: 49

一句话总结该活动：直接在评论区评论，分享高质量selection或者combo。

> ```
> 被审核通过者将获得BRAIN纪念品一份优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至6.14日23：59（以服务器时间为准）

活动要求：参赛同学可发布多个idea参赛，可以是selection idea或者combo idea；必须展示setting。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。


> [!NOTE] [图片 OCR 识别内容]
> S~A吣I
> BRAINI


> 纪念品图

再次强调🎇

**被审核通过者将获得BRAIN纪念品一份
优秀分享更有机会将获得50USD的一次性津贴。**

---

### 帖子 #69: print('retrying in', result.headers["retry-after"], 'seconds')
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

### 帖子 #70: 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回
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

### 帖子 #71: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
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

### 帖子 #72: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #73: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #74: 一种随机生成 SuperAlpha，进行机器回测的方式代码优化
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

### 帖子 #75: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
- **主帖链接**: https://support.worldquantbrain.com[L2] 代码分享拉取某个category下的全部dataset并实现批量生产数据预处理备战Pyramid_28040550959511.md
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

### 帖子 #76: 使用[ClickHouse📕]建设你的大型数据库
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

### 帖子 #77: 增加vf的一个技巧 0.04->0.65->0.95, 提交前先计算“综合得分”
- **主帖链接**: https://support.worldquantbrain.com[L2] 增加vf的一个技巧 004-065-095 提交前先计算综合得分_34405014378135.md
- **讨论数**: 21

原来vf一直升不上去，最高都不到0.5，在vf0.04的时候通过Weijie老师提升vf一对一的指导，从0.04升到0.65，这次提升到0.95.

主要的思路是对提交的alpha数组进行排序。由于os与sharpe, fitness, margin, returns正相关，与turnover负相关，所以我们可以得到一个与os正相关的综合得分， **做得细致的同学还可以计算每一列里面的方差，越小也是越稳定。**

最后根据综合得分，对要提交的alpha进行综合得分降序排序。 先从排序最高的alpha开始提交。例如：有100个可以提交的alpha,可以提交综合得分前10位的alpha.

以下是相关的函数，仅供参考。

```
def calculate_composite_score(arr):    """     计算综合得分，考虑各字段与 os 的关系     :param arr: 输入的数组，包含 sharpe, turnover, fitness, margin, returns     :return: 综合得分    """    sharpe, turnover, fitness, margin, returns = arr[:, 2], arr[:, 3], arr[:, 4], arr[:, 5], arr[:, 10]    # 归一化处理    sharpe_norm = (sharpe - np.min(sharpe)) / (np.max(sharpe) - np.min(sharpe))    turnover_norm = (turnover - np.min(turnover)) / (np.max(turnover) - np.min(turnover))    fitness_norm = (fitness - np.min(fitness)) / (np.max(fitness) - np.min(fitness))    margin_norm = (margin - np.min(margin)) / (np.max(margin) - np.min(margin))    returns_norm = (returns - np.min(returns)) / (np.max(returns) - np.min(returns))    # 由于 turnover 与 os 负相关，其他与 os 正相关    return sharpe_norm - turnover_norm + fitness_norm + margin_norm + returns_normdef sort_by_composite_score(arr):    """    根据综合得分对数组进行降序排序    :param arr: 输入的数组    :return: 排序后的数组    """    composite_score = calculate_composite_score(arr)    sorted_indices = np.argsort(composite_score)[::-1]    # 将综合得分添加到原数组的最后一列    arr_with_score = np.column_stack((arr, composite_score))    return arr_with_score[sorted_indices]def sort_alpha_by_composite_score(arr):    alphas = np.array([sublist[:11] for sublist in arr], dtype=object)    return sort_by_composite_score(alphas)
```

---

### 帖子 #78: 一、从数据出发，依靠简单模版遍历搜索
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何找到更多alpha的思考新手进阶篇系列 - 第一篇单数据字段_27319802497687.md
- **讨论数**: 21

> **记得老师在上课时候讲过alpha research的两个主要脉络，从Idea出发和从Data出发，两种方式都可以找到alpha，而两种能力都具备一定是不断学习的方向。本文就从这两方面来分享一些如何提高alpha产量的思考和心得，也欢迎大家留言讨论！**

---

### 帖子 #79: 过滤掉 Python 内置函数和关键字
- **主帖链接**: https://support.worldquantbrain.com[L2] 用python ast提取表达式中operator和datafield的方法代码优化_30870358077463.md
- **讨论数**: 7

python ast可以自动解析符合python规范的代码表达式. 因此把我们的alpha转换成python可以理解的方式就能解析了, 这样避免了每次字符串的解析(写正则表达式之类). 可以用来在跑模版的时候检测datafield是否符合规范, 也可以用来统计自己使用的各种datafield, operators频率.

代码如下:

import ast

import re

def parse_alpha(alpha_expression):

"""

Parses an alpha expression and extracts operators and data fields.

This function processes a given alpha expression by converting ternary expressions,

fixing indentation errors, and parsing it into an abstract syntax tree (AST). It then

traverses the AST to extract operators and data fields, while filtering out defined

variables, NaN values, and Python built-in functions and keywords.

Args:

alpha_expression (str): The alpha expression to be parsed.

Returns:

dict: A dictionary containing two lists:

- 'operators': A list of unique operators (function and method names) found in the expression.

- 'data_fields': A list of unique data fields (variable names) found in the expression, excluding defined variables and NaN values.

"""

# 处理三元表达式

alpha_expression = alpha_expression.replace('?',' if ').replace(':',' else ')

# 处理和python内置逻辑表达式冲突

alpha_expression = re.sub(r'\band\b', 'and_', alpha_expression) # 替换独立的 'and'

alpha_expression = re.sub(r'\band\(', 'and_(', alpha_expression) # 替换 'and('

alpha_expression = re.sub(r'\bor\b', 'or_', alpha_expression) # 替换独立的 'or'

alpha_expression = re.sub(r'\bor\(', 'or_(', alpha_expression) # 替换 'or('

# 处理逻辑表达式

alpha_expression = alpha_expression.replace('!',' not ').replace('&&',' and ')

# 处理range="0.1,1,0.1" 类似表达式

alpha_expression = re.sub(r'"([^"]*)"', "0", alpha_expression)

# 处理缩进错误，尝试修复

alpha_expression = "\n".join(line.strip() for line in alpha_expression.splitlines())

# 解析表达式为抽象语法树 (AST)

tree = ast.parse(alpha_expression)

# 提取 operators 和 data fields

operators = set()

data_fields = set()

# 提取过程中定义的变量

defined_variables = set()

# 遍历 AST

for node in ast.walk(tree):

# 提取赋值语句中的变量名

ifisinstance(node, ast.Assign):

for target in node.targets:

ifisinstance(target, ast.Name):

defined_variables.add(target.id) # 记录定义的变量名

# 提取函数调用 (operators)

ifisinstance(node, ast.Call):

ifisinstance(node.func, ast.Name):

operators.add(node.func.id) # 函数名

elifisinstance(node.func, ast.Attribute):

operators.add(node.func.attr) # 方法名

# 提取变量名 (data fields)

ifisinstance(node, ast.Name):

data_fields.add(node.id) # 变量名

# 提取三元条件表达式

ifisinstance(node, ast.IfExp):

# 提取条件部分

ifisinstance(node.test, ast.Compare):

for comparator in node.test.comparators:

ifisinstance(comparator, ast.Name):

data_fields.add(comparator.id)

# 提取 if 部分

ifisinstance(node.body, ast.Name):

data_fields.add(node.body.id)

# 提取 else 部分

ifisinstance(node.orelse, ast.Name):

data_fields.add(node.orelse.id)

# 过滤掉过程中定义的变量

data_fields = data_fields - defined_variables

# 过滤掉特殊变量nan

data_fields = data_fields - set(['nan','true','false'])

# 过滤掉 Python 内置函数和关键字

builtin_functions = set(dir(__builtins__)) # Python 内置函数

operators = operators - builtin_functions # 去掉内置函数

data_fields = data_fields - builtin_functions - operators # 去掉内置函数

return {'operators':list(operators),"data_fields":list(data_fields)}

目前这个版本我自己用着是没发现什么解析错误的问题. 欢迎大家指正.

---

### 帖子 #80: [SuperAlpha] Not Own Selection的一二三....N阶分层框架Alpha Template
- **主帖链接**: [SuperAlpha] Not Own Selection的一二三N阶分层框架Alpha Template.md
- **讨论数**: 16

作为一个GM, 有大量的not own alpha可用, 但是之前的我的框架回测的alpha由于selection比较固定, 导致有大量的自相关性, 且出货率不高游戏王的SELECTION框架-v2的选择感觉又太手工, 没法大规模回测, 而且分层思想感觉没有贯彻到底(xixi)这时我想起了weijie老师经常说起的分层思想, 因此这里我借助分层思想做了一个Selection的框架.核心思想:通过Datasets和turnover将我可以使用的alpha按30个一组分层, 之后按照一组(一阶), 两组(二阶), 三组(三阶),..., 进行回测. combo统一使用combo_a(alpha), 其他的设置也都是固定的一个, 没有遍历, 因为本身selection的可遍历空间已经足够大了搜索空间: 无穷无尽, 我现在通过随机数随机找了200301个二阶的准备回测(只有selection的改变)效果:在EUR区域通过二阶回测, 回测37428个, 目前fit>5的有29243个, 因子之间的相关性也相对较低.做法: 这里就不放完整的代码, 有兴趣的自己开发第一步, 对可用的alpha进行分层标识在这里我的想法是通过alpha所属的Datasets和turnover将我可以使用的alpha按30个一组分层, 然后记录下来相关selection, 具体形式大致为 ((in(datasets, "xxxx")) && (turnover>=xxxx) && (turnover<xxxx))我是将分层结果保存在数据库, 大致结构如下具体做法, 是通过run selection提供的按钮从turnover从小到大获取30个因子. 代码如下def get_select_alphas(select_expr):# API 端点 URLurl = "[链接已屏蔽] 请求参数params = {"limit": 100,"offset": 0,"status": "ACTIVE","settings.delay": cfg.delay,"settings.instrumentType": "EQUITY","settings.region": cfg.region,"order": "-selected.weight","hidden": "false","selection": f'({select_expr}) * (1-turnover)',"selectionHandling": "POSITIVE","selectionLimit": 100}full_url = f"{url}?{urlencode(params)}"response = wqapi.wait_get(full_url)response = response.json()return responsedef get_layering_data(item_dataset):select_dataset = f'in(datasets, "{item_dataset}")'turnover_lower = -np.infturnover_upper = np.infselect_layering_data = []while True:turnover_upper = np.infselect_turnover_lower = '' if turnover_lower == -np.inf else f'turnover>={turnover_lower}'select_turnover_upper = '' if turnover_upper == np.inf else f'turnover<{turnover_upper}select_layering = ' && '.join([item for item in [select_dataset, select_turnover_lower, select_turnover_upper] if item])select_expr = ' && '.join([f'({item})' for item in [select_base, select_layering] if item])response = get_select_alphas(select_expr)if response['count'] == 0:breakresults = pd.DataFrame(response['results'])results = pd.concat([pd.json_normalize(results['selected']), pd.json_normalize(results['is'])], axis=1)# print(f"Dataset: {item_dataset}, Count: {results.shape[0]}, Turnover Lower: {turnover_lower}, Turnover Upper: {turnover_upper}")if results.shape[0] <= 45:select_layering_data.append((select_dataset, round(turnover_lower,5), np.inf, results.shape[0]))breakwhile True:turnover_upper = round(results.iloc[29].turnover+0.00005,5)select_count = results[results.turnover < turnover_upper].shape[0]select_layering_data.append((select_dataset, round(turnover_lower,5), round(turnover_upper,5), select_count))results = results[results.turnover >= turnover_upper].copy().reset_index(drop=True)turnover_lower = turnover_upperif (response['count']< 100) and (results.shape[0] <= 45):select_layering_data.append((select_dataset, round(turnover_lower,5), np.inf, results.shape[0]))breakif results.shape[0] < 35:breakif response['count'] < 100:breakreturn select_layering_data# futures = []# select_layering_data = []# task_list = datasets.copy()# task_list = sorted(task_list)# pbar = tqdm(total=len(task_list), desc="Processing tasks")# with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:#     while task_list or futures:#         while task_list and len(futures) < MAX_WORKERS:#             item_dataset = task_list.pop(0)#             futures.append(executor.submit(get_layering_data, item_dataset))#         done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)#         for d in done:#             futures.remove(d)#             item_res = d.result()#             doc_id = f"{cfg.region}_{cfg.delay}"#             doc = collection_layering.find_one({'id': doc_id}, {'_id': 0, 'values.date': 1})#             max_date = max(v['date'] for v in doc['values'])#             collection_layering.update_one(#                 {'id': doc_id},#                 {#                     '$push': {'values.$[v].values': {'$each': item_res}},#                     '$set': {'datasets_num': len(task_list)+len(futures), 'time': datetime.now().strftime('%Y%m%d-%H%M%S')}#                 },#                 array_filters=[{'v.date': max_date}]#             )#             # select_layering_data.extend(d.result())#             pbar.update(1)#             # if total_success % 20 == 0 or total_success == len(task_list):#             #     # cfg.log_message('info', f"并发进度: {total_success}/{len(task_list)}")#             #     print(f"并发进度: {total_success}/{len(task_list)}")# pbar.close()对于USA或者EUR这样的大区, 大概1-2h就可以遍历完.当然我用的是turnover来辅助分层, 你也可以用long或short来分层.第二步, 组合因子因为我们已经得到所有alpha的分层情况了, 之后我们可以选取其中一个, 或者两两组合, 或者随机选三个组合, 以此类推. 这样在选择因子里各个类型的因子的个数大致是相等的目前我是选择其中两个进行组合的, 像EUR区域的话因子通过分层大概是3523组, 排列组合C(3523, 2)就在6,304,003个待回测的因子的量级了,  你可以从中去挑选一些保持大规模回测, 基本上是测不完的大致代码如下from itertools import combinations, productdef combination(n, k):# 确保k不大于n，且为非负整数if k < 0 or k > n:return 0# 优化计算，取较小的k值if k > n - k:k = n - kresult = 1for i in range(k):result = result * (n - i) // (i + 1)return resultdef get_layering_expr(item_data):select_dataset, turnover_lower, turnover_upper = item_data.dataset, item_data.turnover_lower, item_data.turnover_upper# select_dataset = f'in(datasets, "{item_dataset}")'select_turnover_lower = '' if turnover_lower == -np.inf else f'turnover>={turnover_lower}'select_turnover_upper = '' if turnover_upper == np.inf else f'turnover<{turnover_upper}'layering_expr = ' && '.join([f"({item})" for item in [select_dataset, select_turnover_lower, select_turnover_upper] if item])return layering_exprdef combine_expr_k(df, k=2, subset_size=10):get_subset_expr = lambda x: random.sample(x, min(len(x), subset_size))# 按 dataset 分组grouped = df.groupby("dataset")["expr"].apply(list).to_dict()datasets = list(grouped.keys())results = []for ds_combo in combinations(datasets, k):# # 每个 dataset 取一条，做笛卡尔积# for pick in product(*(get_subset_expr(grouped[ds]) for ds in ds_combo)):#     results.append(" || ".join(f"({e})" for e in pick))full_product = list(product(*(grouped[ds] for ds in ds_combo)))subset_product = list(product(*(get_subset_expr(grouped[ds]) for ds in ds_combo)))k = len(subset_product)# 从完整笛卡尔积中随机采样 k 个sampled_product = random.sample(full_product, min(k, len(full_product)))results.extend([" || ".join(f"({e})" for e in pick) for pick in sampled_product])return resultsdoc_id = f"{cfg.region}_{cfg.delay}"doc = collection_layering.find_one({'id': doc_id}, {'_id': 0, 'values': 1,})['values']max_date = max(v['date'] for v in doc)select_layering_data = [v for v in doc if v['date'] == max_date][0]['values']select_layering_data = pd.DataFrame(select_layering_data, columns=['dataset', 'turnover_lower', 'turnover_upper', 'count'])select_layering_data = select_layering_data.drop_duplicates()select_layering_data['expr'] = select_layering_data.apply(get_layering_expr, axis=1)select_layering_data = select_layering_data.query('count>=15').reset_index(drop=True)layering_expr = combine_expr_k(select_layering_data, k=2, subset_size=10)layering_expr = [f"({item}) && ({select_base})" for item in layering_expr]这里展示最近一次提交的因子(((in(datasets, "pv1")) && (turnover>=0.18545) && (turnover<0.18615)) || ((in(datasets, "pv96")) && (turnover>=0.05095) && (turnover<0.06815))) && base_selection这里的base_selection是一些提前筛选的条件, 具体的可参考游戏王的帖子进行相应的改动, 例如prod_correlation, datafield_count, operator_count等第三步, 大规模回测+Check仅供参考，祝各位select愉快：）

---

### 帖子 #81: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[SuperAlpha] Not Own Selection的一二三N阶分层框架Alpha Template_35377811169175.md
- **讨论数**: 16

作为一个GM, 有大量的not own alpha可用, 但是

- 之前的我的框架回测的alpha由于selection比较固定, 导致有大量的自相关性, 且出货率不高
- 游戏王的 [SELECTION框架-v2]([L2] [SuperAlpha]SELECTION框架-v2经验分享_33745533142679.md) 的选择感觉又太手工, 没法大规模回测, 而且分层思想感觉没有贯彻到底(xixi)

这时我想起了weijie老师经常说起的分层思想, 因此这里我借助分层思想做了一个Selection的框架.

**核心思想:** 通过Datasets和turnover将我可以使用的alpha按30个一组分层, 之后按照一组(一阶), 两组(二阶), 三组(三阶),..., 进行回测. combo统一使用combo_a(alpha), 其他的设置也都是固定的一个, 没有遍历, 因为本身selection的可遍历空间已经足够大了

**搜索空间** : 无穷无尽, 我现在通过随机数随机找了200301个二阶的准备回测(只有selection的改变)

**效果:**  在EUR区域通过二阶回测, 回测37428个, 目前fit>5的有29243个, 因子之间的相关性也相对较低.

**做法: 这里就不放完整的代码, 有兴趣的自己开发**

**第一步, 对可用的alpha进行分层标识**

在这里我的想法是通过alpha所属的Datasets和turnover将我可以使用的alpha按30个一组分层, 然后记录下来相关selection, 具体形式大致为 ((in(datasets, "xxxx")) && (turnover>=xxxx) && (turnover<xxxx))

我是将分层结果保存在数据库, 大致结构如下


> [!NOTE] [图片 OCR 识别内容]
> i: ObjectId(
> 68b111382d420537436057e6
> TEUR_In
> values
> Array (1)
> 日: Object
> date
> 20250829
> Values
> Array
> (3523)
> Array
> (4)
> 0: "in(datasets;
> analyst35")
> 1:  Infinity
> 2: Infinity
> 1: Array
> (4)
> Array (4)
> 0: "in(datasets, ranalystll")
> 10085
> 0.16175
> 3: Array
> Array (4)
> 0: "in(datasets;
> ranalystll" )
> 1:  0.27345
> 2: Infinity
> 3:  26
> 63


具体做法, 是通过run selection提供的按钮从turnover从小到大获取30个因子. 代码如下

```
def get_select_alphas(select_expr):    # API 端点 URL    url = "[链接已屏蔽]    # 请求参数    params = {        "limit": 100,        "offset": 0,        "status": "ACTIVE",        "settings.delay": cfg.delay,        "settings.instrumentType": "EQUITY",        "settings.region": cfg.region,        "order": "-selected.weight",        "hidden": "false",        "selection": f'({select_expr}) * (1-turnover)',        "selectionHandling": "POSITIVE",        "selectionLimit": 100    }    full_url = f"{url}?{urlencode(params)}"    response = wqapi.wait_get(full_url)    response = response.json()    return responsedef get_layering_data(item_dataset):    select_dataset = f'in(datasets, "{item_dataset}")'    turnover_lower = -np.inf    turnover_upper = np.inf    select_layering_data = []    while True:        turnover_upper = np.inf        select_turnover_lower = '' if turnover_lower == -np.inf else f'turnover>={turnover_lower}'        select_turnover_upper = '' if turnover_upper == np.inf else f'turnover<{turnover_upper}        select_layering = ' && '.join([item for item in [select_dataset, select_turnover_lower, select_turnover_upper] if item])        select_expr = ' && '.join([f'({item})' for item in [select_base, select_layering] if item])        response = get_select_alphas(select_expr)        if response['count'] == 0:            break        results = pd.DataFrame(response['results'])        results = pd.concat([pd.json_normalize(results['selected']), pd.json_normalize(results['is'])], axis=1)        # print(f"Dataset: {item_dataset}, Count: {results.shape[0]}, Turnover Lower: {turnover_lower}, Turnover Upper: {turnover_upper}")        if results.shape[0] <= 45:            select_layering_data.append((select_dataset, round(turnover_lower,5), np.inf, results.shape[0]))            break        while True:            turnover_upper = round(results.iloc[29].turnover+0.00005,5)            select_count = results[results.turnover < turnover_upper].shape[0]            select_layering_data.append((select_dataset, round(turnover_lower,5), round(turnover_upper,5), select_count))            results = results[results.turnover >= turnover_upper].copy().reset_index(drop=True)            turnover_lower = turnover_upper            if (response['count']< 100) and (results.shape[0] <= 45):                select_layering_data.append((select_dataset, round(turnover_lower,5), np.inf, results.shape[0]))                break            if results.shape[0] < 35:                break        if response['count'] < 100:            break    return select_layering_data
```

```
# futures = []# select_layering_data = []# task_list = datasets.copy()# task_list = sorted(task_list)# pbar = tqdm(total=len(task_list), desc="Processing tasks")# with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:#     while task_list or futures:#         while task_list and len(futures) < MAX_WORKERS:#             item_dataset = task_list.pop(0)#             futures.append(executor.submit(get_layering_data, item_dataset))#         done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)#         for d in done:#             futures.remove(d)#             item_res = d.result()#             doc_id = f"{cfg.region}_{cfg.delay}"#             doc = collection_layering.find_one({'id': doc_id}, {'_id': 0, 'values.date': 1})#             max_date = max(v['date'] for v in doc['values'])#             collection_layering.update_one(#                 {'id': doc_id},#                 {#                     '$push': {'values.$[v].values': {'$each': item_res}},#                     '$set': {'datasets_num': len(task_list)+len(futures), 'time': datetime.now().strftime('%Y%m%d-%H%M%S')}#                 },#                 array_filters=[{'v.date': max_date}]#             )#             # select_layering_data.extend(d.result())#             pbar.update(1)#             # if total_success % 20 == 0 or total_success == len(task_list):#             #     # cfg.log_message('info', f"并发进度: {total_success}/{len(task_list)}")#             #     print(f"并发进度: {total_success}/{len(task_list)}")# pbar.close()
```

对于USA或者EUR这样的大区, 大概1-2h就可以遍历完.

当然我用的是turnover来辅助分层, 你也可以用long或short来分层.

**第二步, 组合因子**

因为我们已经得到所有alpha的分层情况了, 之后我们可以选取其中一个, 或者两两组合, 或者随机选三个组合, 以此类推. 这样在 **选择因子里各个类型的因子的个数大致是相等的**

目前我是选择其中两个进行组合的, 像EUR区域的话因子通过分层大概是3523组, 排列组合C(3523, 2)就在6,304,003个待回测的因子的量级了,  你可以从中去挑选一些保持大规模回测, 基本上是测不完的

大致代码如下

```
from itertools import combinations, productdef combination(n, k):    # 确保k不大于n，且为非负整数    if k < 0 or k > n:        return 0    # 优化计算，取较小的k值    if k > n - k:        k = n - k    result = 1    for i in range(k):        result = result * (n - i) // (i + 1)    return resultdef get_layering_expr(item_data):    select_dataset, turnover_lower, turnover_upper = item_data.dataset, item_data.turnover_lower, item_data.turnover_upper    # select_dataset = f'in(datasets, "{item_dataset}")'    select_turnover_lower = '' if turnover_lower == -np.inf else f'turnover>={turnover_lower}'    select_turnover_upper = '' if turnover_upper == np.inf else f'turnover<{turnover_upper}'    layering_expr = ' && '.join([f"({item})" for item in [select_dataset, select_turnover_lower, select_turnover_upper] if item])    return layering_exprdef combine_expr_k(df, k=2, subset_size=10):    get_subset_expr = lambda x: random.sample(x, min(len(x), subset_size))    # 按 dataset 分组    grouped = df.groupby("dataset")["expr"].apply(list).to_dict()    datasets = list(grouped.keys())    results = []    for ds_combo in combinations(datasets, k):        # # 每个 dataset 取一条，做笛卡尔积        # for pick in product(*(get_subset_expr(grouped[ds]) for ds in ds_combo)):        #     results.append(" || ".join(f"({e})" for e in pick))        full_product = list(product(*(grouped[ds] for ds in ds_combo)))        subset_product = list(product(*(get_subset_expr(grouped[ds]) for ds in ds_combo)))        k = len(subset_product)        # 从完整笛卡尔积中随机采样 k 个        sampled_product = random.sample(full_product, min(k, len(full_product)))        results.extend([" || ".join(f"({e})" for e in pick) for pick in sampled_product])    return results
```

```
doc_id = f"{cfg.region}_{cfg.delay}"doc = collection_layering.find_one({'id': doc_id}, {'_id': 0, 'values': 1,})['values']max_date = max(v['date'] for v in doc)select_layering_data = [v for v in doc if v['date'] == max_date][0]['values']select_layering_data = pd.DataFrame(select_layering_data, columns=['dataset', 'turnover_lower', 'turnover_upper', 'count'])select_layering_data = select_layering_data.drop_duplicates()select_layering_data['expr'] = select_layering_data.apply(get_layering_expr, axis=1)select_layering_data = select_layering_data.query('count>=15').reset_index(drop=True)layering_expr = combine_expr_k(select_layering_data, k=2, subset_size=10)layering_expr = [f"({item}) && ({select_base})" for item in layering_expr]
```

这里展示最近一次提交的因子

> (((in(datasets, "pv1")) && (turnover>=0.18545) && (turnover<0.18615)) || ((in(datasets, "pv96")) && (turnover>=0.05095) && (turnover<0.06815))) && base_selection

这里的base_selection是一些提前筛选的条件, 具体的可参考游戏王的帖子进行相应的改动, 例如prod_correlation, datafield_count, operator_count等


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Selection Expression
> Aggregate Data
> SharOE
> TUFNOIE
> FIMESs
> TeCUTI
> UraVuoII
> IaTeIn
> (((i(datasets,
> PVI
> (turnover〉=g
> 18545 )
> (turnoverco.18615)
> ((i(datasets,
> pvg6"
> (turnover
> 7.27
> 11.439
> 8.44
> 16.8496
> 1.1496
> 29.469600
> Combo Expression
> Sharpe
> TuIOVeF
> Returns
> Drawdown
> Marqin
> LoNg Count
> Short Count
> COmbo_
> (alpha,
> nlength
> 252
> mode
> alBOI
> 2013
> 0.031
> 0.00
> 0.031
> 0.0093
> 0UFSoo
> simulation Settings
> 2014
> 8.71
> 11.254
> 10.44
> 17.32北
> 0.4895
> 31.535o0
> 1275
> 1255
> Instrument Type
> Region
> UnNerse
> LangUage
> Decay
> Delay
> Truncation
> Neutralizatjon
> Pasteuriatijon
> NaN Handling
> Unit Handling
> MaxTrade
> 2015
> 9.3
> 11.604
> 11.15
> 17.954
> 0.9393
> 30.955600
> 1335
> 1332
> Equi?
> EUR
> TOPZSO
> Fast Expression
> 001
> Country | Resion
> Verify
> 2015
> 8.36
> 12111
> 11.30
> 20.334
> 0.4493
> 33.58550
> 1335
> 1341
> 2017
> 12.174
> 13.774
> 0.-295
> 22.52oo
> 138
> 1457
> 2013
> 5.-5
> 12.531
> 14034
> 0.7391
> 22.-300
> 1532
> 1430
> Clone Alpha
> 2013
> 5.3-
> 12.274
> 13034
> 0.7995
> 1.1350
> 1441
> 1393
> 2020
> 5.71
> 10.514
> 17.534
> 5995
> 33.635600
> 1442
> 1325
> 021
> 3.20
> 3.224
> 3004
> 0.329
> 19.455800
> 1531
> 1322
> Chart
> PIL
> 2021
> 7.75
> 10.334
> 9.37
> 13.254
> 1.1995
> 33.715600
> 1515
> 1452
> 2022
> 7.21
> 134
> 19.514
> 3895
> 41.355o0
> 1523
> 1335
> 2023
> 10.74
> 3.521
> 14.55
> 23.354
> 0.1191
> 330
> 1556
> 1215
> 1SM
> 1OM
> Risk neutralized
> Aggregate Data
> TaT
> TUITMTTIP
> Fines
> ETIITnS
> CCam
> Marain
> OOOK
> 5.40
> 11.43%
> 5.82
> 10.34%
> 1.379
> 18.089600
> Investability constrained
> 201
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Aggregate Data
> Sharpe
> TUCnOE
> Fitnes
> AI
> 诗求监视器
> apiworldquantbrain com
> 展开
>  空
> 5.71
> 7.27%
> 5.80
> Combo Pnl
> Equal Ielight Pnl
> Correlation
> Self Correlation
> Naximum
> IIIMINUIT
> LaSt RUn:
> OS Testing Status
> Period
> Prod Correlation
> 1airUIT
> NininIT
> 1
> Run; Fri。10/03/2025,5.27 PW
> 11 PENDING
> 0.4830
> -0.5291
> DOM
> Selected Alphas
> 76 Alphas have beEn selected
> Viewall
> 1Ok
> Name
> Universe
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Marqin
> 
> 100
> anonymoUs
> T0P1200
> 171
> 13.5093
> 7.104
> 842*
> 7.545600
> EROTITOUs
> TP1200
> 13.5895
> 6.554
> 3.56*
> 7.1586o0
> aROTIMOUs
> TP1200
> 13.5695
> 1.04
> 5.174
> 226*
> 5.575600
> 0.01
> ERONNMOUs
> T0P1200
> 13.5593
> 11.711
> 9
> 12.535600
> 03
> 01
> 0?
> 05
> 0@
> 09
> 09'
> 03
> 8?
> 06
> 0
> 03
> 02'
> aROTIMOUs
> TP1200
> 13.5895
> 043
> 484*
> 6ER6oo
> Properties
> 73151E1
> 09123/2025,4.33 Pr
> Name
> Category
> CurrentlyanonymOUsi
> None
> Tags
> Color
> Selectaddtags
> NonE
> Short descriptions ofyour Selection Expression and Combo Expression are required to submit this SuperAlpha
> Description Of Selection Expression*
> 798
> 100 character minimum
> The expression aims to select promising alphas from
> larger pool. It has to main conditions joined by an '&&' . The first condition is
> disjunction ( | |) oftWO SUb
> Conditions:
> Ihenthe datasetis
> "pvl",turnoveris between 0.18545 and 0.18615 _
> LI
> Lic
> 」;
> C4'
> 0Coo
> C
> 4C04 [
> Description of Combo Expressionx
> 586
> 100Character IinimUm
> The expression
> Combo_alalpha, nlength
> 252, mode
> 'algo1) ` is
> combination type expression. Its core idea is to assign weights
> and combine multiple alphas into
> composite signal. Here
> alpha
> represents the alphas to be combined
> nlength = 252
> likely
> inoicates
> time
> related parameter SUCh a5
> lookback period,
> mode
> 31801'
> specifies the algorithm or method to be used for
> !;-+;-
> | 
> Ctrto
> ,'
> L;+
> +;
> u+i|
> Ver
> Ftres
> ~0,6
> 0.8
> 0.4
> 0.0
> 04
> ~0.1
> 0.4 .
> 0.5
> 0,6.。
> 0.7.
> 0.8
> O。1
> 0.2
> 0.3
> 0.9..
> 0,0
> ~1.0
> ~0.5
> Mon。
> and


**第三步, 大规模回测+Check**

仅供参考，祝各位select愉快：）

---

### 帖子 #82: [分析王]基于已提交因子分析EUR D1 第1弹
- **主帖链接**: [分析王]基于已提交因子分析EUR D1 第1弹.md
- **讨论数**: 0

通过某种方式可以拿到平台已提交的因子的一些IS, OS和setting. 这里就开一个系列分析一下今天首先来分析一下EUR D1区域, 共302014因子首先是提交日期大部分的因子都提交于ppa开始之后---接下来是已提交因子的IS指标分布已提交因子的OS指标分布sharpe的os近似正态了...OS/IS分布---因子所用的ops个数----Universe分布TOP1200比较高的原因是,之前最多只有TOP1200----neutralization分布基本上不相伯仲---最后是 corr第一弹简单的分析就到这里,  后面慢慢找角度分析吧

---

### 帖子 #83: [分析王]基于已提交因子分析EUR D1 第1弹
- **主帖链接**: https://support.worldquantbrain.com[分析王]基于已提交因子分析EUR D1 第1弹_35611561508375.md
- **讨论数**: 0

通过某种方式可以拿到平台已提交的因子的一些IS, OS和setting. 这里就开一个系列分析一下

今天首先来分析一下EUR D1区域, 共302014因子

首先是提交日期


> [!NOTE] [图片 OCR 识别内容]
> Histogram of Date Submitted
> 100000
> 80000
> 50000
> 
> 40000
> 20000
> 2021-122022-062022-122023-062023-122024-06 2024-122025-06
> Date SUbmltted


大部分的因子都提交于ppa开始之后

---

### 帖子 #84: 【Alpha灵感】“球队硬币”因子构建
- **主帖链接**: 【Alpha灵感】球队硬币因子构建.md
- **讨论数**: 2

研报标题：方正证券 - 个股动量效应的识别及“球队硬币”因子 构建——多因子选股系列研究之四

作者：曹春晓，方正金融工程团队

概述：将股票划分为“球队”和“硬币”类股票，进行反转或不反转处理

**1.1 Alpha Idea:**

**背景**

*抛硬币* ：由于人们对抛硬币的概率可知，所以当上一次抛出为正面时，下一次猜测倾向于反面。人们会以“反转”的眼光来看待“抛硬币”

*猜球队夺冠* ：由于新赛季开始且球队磨合情况不了解，所以通常使用历史成绩考察不同球队，倾向于猜测上赛季的冠军，依旧会在本赛季夺冠。人们会以“动量”的眼光来看待“球队夺冠”。

**然而，对于股票来说，为了获得更多的收益，通常会发生过度买卖，使得“硬币”和“球队”的股票结果正好相反，即**

- “球队”股票：最终可能实际发生的是反转效应。
- “硬币”股票：最终可能实际发生的是动量效应。

同时， **认为波动率和换手率的变化量可以代表一支股票表现的“可知性”** ，即更像硬币还是更像球队。即

- 波动率低，表明股价走势相对稳定，投资者对其未来趋势做出判断也更加容易
- 换手率降低，则表示投资者对股票的意见分歧逐渐减少，也是“可知性”提高 的表现。

因此

- 波动率低的股票和换手率下降的股票，“可知性”更高， 属于硬币类型的股票，未来发生动量效应的概率更大
- 波动率高的股票和换手率增长的股票，“可知性”更低，属于球队类型的股票，未来发生反转效应的概率更大。

**1.2 主要数据字段** ：close, open, volume/cap
 **1.3 主要运算符** ：normalize, ts_mean, ts_std_dev
 **1.4 Universe** : CHN TOP3000

**2. 因子构建**

本文介绍的 **“球队硬币”因子** 由三个因子（ **“修正日间反转”因子、“修正日内反转”因子和 “修正隔夜反转”因子** ）构成。每个因子由两类因子（ **波动率处理和换手率处理** ）加和而成。

具体代码如下：

```
turnover_rate = volume/cap;turnover_rate_delta = turnover_rate - ts_delay(turnover_rate, 1);daynei_yield = close/open-1; close_delay = ts_delay(close, 1);night_yield = open/close_delay - 1;day_yield = close/close_delay-1; time = 20;# “修正日间反转”因子# “日间反转-波动翻转”因子day_yield_mean = ts_mean(day_yield, time); # 日间收益率day_yield_std = ts_std_dev(day_yield, time); # 日间波动率factor1 = if_else(normalize(day_yield_std, useStd = false)>0, -day_yield_mean, day_yield_mean);# “日间反转-换手翻转”因子factor2 = if_else(normalize(turnover_rate_delta, useStd = false)>0, -day_yield_mean, day_yield_mean);# “修正日内反转”因子# “日内反转-波动翻转”因子daynei_yield_mean = ts_mean(daynei_yield, time); daynei_yield_std = ts_std_dev(daynei_yield, time); factor3 = if_else(normalize(daynei_yield_std, useStd = false)>0, -daynei_yield_mean, daynei_yield_mean);# “日内反转-换手翻转”因子factor4 = if_else(normalize(turnover_rate_delta, useStd = false)>0, -daynei_yield_mean, daynei_yield_mean);# “修正隔夜反转”因子# “隔夜距离”因子night_dis = abs(normalize(night_yield, useStd = false));night_dis_mean = ts_mean(night_dis, time); night_dis_std = ts_std_dev(night_dis, time); # “隔夜反转-波动翻转”因子factor5 = if_else(normalize(night_dis_std, useStd = false)>0, -night_dis_mean, night_dis_mean);# # “隔夜反转-换手翻转”因子turnover_dis = abs(normalize(ts_delay(turnover_rate, 1) - ts_delay(turnover_rate, 2), useStd = false));factor6 = if_else(normalize(turnover_dis, useStd = false)>0, -night_dis_mean, night_dis_mean);# “球队硬币”因子factor1 + factor2 + factor3 + factor4 + factor5 + factor6
```

经过其他处理后，以下是回测绩效


> [!NOTE] [图片 OCR 识别内容]
> 7,50OK
> 5,00OK
> 2,50OK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> 2.90
> 16.28%
> 2.31
> 10.329
> 6.129
> 12.689600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2012
> 6.81
> 16.119
> 7.05
> 17.29%6
> 0.72%
> 21.479000
> 1145
> 1158
> 2013
> 2.27
> 15.2296
> 1.50
> 6.69%
> 2.3796
> 8.790000
> 1181
> 1204
> 2014
> 4.96
> 15.129
> 4.76
> 13.9496
> 1.1196
> 18.449000
> 1192
> 1198
> 2015
> 0.11
> 16.85%6
> 0.02
> 0.59%6
> 6.1296
> 0.709o00
> 1227
> 1216
> 2016
> 4.01
> 16.04%
> 3.69
> 13.55%
> 2.0296
> 16.899000
> 1334
> 1338
> 2017
> 4.15
> 16.48%
> 3.84
> 14.08%
> 1.559
> 17.099o0o
> 1484
> 1497
> 2018
> 3.58
> 15.929
> 2.84
> 10.01%
> 1.4996
> 12.57
> O00
> 1489
> 1517
> 2019
> 3.43
> 16.119
> 2.92
> 11.649
> 1.53%
> 14.459000
> 1490
> 1514
> 2020
> 1.82
> 17.36%
> 1.16
> 7.01%
> 3.3296
> 8,089000
> 1486
> 1526
> 2021
> 2.11
> 17.5496
> 1.47
> 8.529
> 2.2796
> 9,7
> Oooo
> 1501
> 1542
> 2022
> -0.71
> 18.529
> -0.24
> -2.0996
> 0.7096
> -2.269000
> 1523
> 1536



> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Highest Correlation
> Last Run: ThU, 02/01/2024,10:10 PM
> 0.7
> 10Ok
> 1Ok
> 7k
> 鬓
> 100
> 昱
> 8
> 10
> 09'
> 0^
> 0?
> 3"
> 0^
> 0?
> 0.2


---

### 帖子 #85: 【Alpha灵感】“球队硬币”因子构建
- **主帖链接**: https://support.worldquantbrain.com【Alpha灵感】球队硬币因子构建_21109320413335.md
- **讨论数**: 2

研报标题：方正证券 - 个股动量效应的识别及“球队硬币”因子 构建——多因子选股系列研究之四

作者：曹春晓，方正金融工程团队

概述：将股票划分为“球队”和“硬币”类股票，进行反转或不反转处理

**1.1 Alpha Idea:**

**背景**

*抛硬币* ：由于人们对抛硬币的概率可知，所以当上一次抛出为正面时，下一次猜测倾向于反面。人们会以“反转”的眼光来看待“抛硬币”

*猜球队夺冠* ：由于新赛季开始且球队磨合情况不了解，所以通常使用历史成绩考察不同球队，倾向于猜测上赛季的冠军，依旧会在本赛季夺冠。人们会以“动量”的眼光来看待“球队夺冠”。

**然而，对于股票来说，为了获得更多的收益，通常会发生过度买卖，使得“硬币”和“球队”的股票结果正好相反，即**

- “球队”股票：最终可能实际发生的是反转效应。
- “硬币”股票：最终可能实际发生的是动量效应。

同时， **认为波动率和换手率的变化量可以代表一支股票表现的“可知性”** ，即更像硬币还是更像球队。即

- 波动率低，表明股价走势相对稳定，投资者对其未来趋势做出判断也更加容易
- 换手率降低，则表示投资者对股票的意见分歧逐渐减少，也是“可知性”提高 的表现。

因此

- 波动率低的股票和换手率下降的股票，“可知性”更高， 属于硬币类型的股票，未来发生动量效应的概率更大
- 波动率高的股票和换手率增长的股票，“可知性”更低，属于球队类型的股票，未来发生反转效应的概率更大。

**1.2 主要数据字段** ：close, open, volume/cap
 **1.3 主要运算符** ：normalize, ts_mean, ts_std_dev
 **1.4 Universe** : CHN TOP3000

**2. 因子构建**

本文介绍的 **“球队硬币”因子** 由三个因子（ **“修正日间反转”因子、“修正日内反转”因子和 “修正隔夜反转”因子** ）构成。每个因子由两类因子（ **波动率处理和换手率处理** ）加和而成。

具体代码如下：

```
turnover_rate = volume/cap;turnover_rate_delta = turnover_rate - ts_delay(turnover_rate, 1);daynei_yield = close/open-1; close_delay = ts_delay(close, 1);night_yield = open/close_delay - 1;day_yield = close/close_delay-1; time = 20;# “修正日间反转”因子# “日间反转-波动翻转”因子day_yield_mean = ts_mean(day_yield, time); # 日间收益率day_yield_std = ts_std_dev(day_yield, time); # 日间波动率factor1 = if_else(normalize(day_yield_std, useStd = false)>0, -day_yield_mean, day_yield_mean);# “日间反转-换手翻转”因子factor2 = if_else(normalize(turnover_rate_delta, useStd = false)>0, -day_yield_mean, day_yield_mean);# “修正日内反转”因子# “日内反转-波动翻转”因子daynei_yield_mean = ts_mean(daynei_yield, time); daynei_yield_std = ts_std_dev(daynei_yield, time); factor3 = if_else(normalize(daynei_yield_std, useStd = false)>0, -daynei_yield_mean, daynei_yield_mean);# “日内反转-换手翻转”因子factor4 = if_else(normalize(turnover_rate_delta, useStd = false)>0, -daynei_yield_mean, daynei_yield_mean);# “修正隔夜反转”因子# “隔夜距离”因子night_dis = abs(normalize(night_yield, useStd = false));night_dis_mean = ts_mean(night_dis, time); night_dis_std = ts_std_dev(night_dis, time); # “隔夜反转-波动翻转”因子factor5 = if_else(normalize(night_dis_std, useStd = false)>0, -night_dis_mean, night_dis_mean);# # “隔夜反转-换手翻转”因子turnover_dis = abs(normalize(ts_delay(turnover_rate, 1) - ts_delay(turnover_rate, 2), useStd = false));factor6 = if_else(normalize(turnover_dis, useStd = false)>0, -night_dis_mean, night_dis_mean);# “球队硬币”因子factor1 + factor2 + factor3 + factor4 + factor5 + factor6
```

经过其他处理后，以下是回测绩效


> [!NOTE] [图片 OCR 识别内容]
> 7,50OK
> 5,00OK
> 2,50OK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> 2.90
> 16.28%
> 2.31
> 10.329
> 6.129
> 12.689600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2012
> 6.81
> 16.119
> 7.05
> 17.29%6
> 0.72%
> 21.479000
> 1145
> 1158
> 2013
> 2.27
> 15.2296
> 1.50
> 6.69%
> 2.3796
> 8.790000
> 1181
> 1204
> 2014
> 4.96
> 15.129
> 4.76
> 13.9496
> 1.1196
> 18.449000
> 1192
> 1198
> 2015
> 0.11
> 16.85%6
> 0.02
> 0.59%6
> 6.1296
> 0.709o00
> 1227
> 1216
> 2016
> 4.01
> 16.04%
> 3.69
> 13.55%
> 2.0296
> 16.899000
> 1334
> 1338
> 2017
> 4.15
> 16.48%
> 3.84
> 14.08%
> 1.559
> 17.099o0o
> 1484
> 1497
> 2018
> 3.58
> 15.929
> 2.84
> 10.01%
> 1.4996
> 12.57
> O00
> 1489
> 1517
> 2019
> 3.43
> 16.119
> 2.92
> 11.649
> 1.53%
> 14.459000
> 1490
> 1514
> 2020
> 1.82
> 17.36%
> 1.16
> 7.01%
> 3.3296
> 8,089000
> 1486
> 1526
> 2021
> 2.11
> 17.5496
> 1.47
> 8.529
> 2.2796
> 9,7
> Oooo
> 1501
> 1542
> 2022
> -0.71
> 18.529
> -0.24
> -2.0996
> 0.7096
> -2.269000
> 1523
> 1536



> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Highest Correlation
> Last Run: ThU, 02/01/2024,10:10 PM
> 0.7
> 10Ok
> 1Ok
> 7k
> 鬓
> 100
> 昱
> 8
> 10
> 09'
> 0^
> 0?
> 3"
> 0^
> 0?
> 0.2


---

### 帖子 #86: 【Community Leader-因子筛选与组合】对SA Not Own Selection的一二三....N阶分层框架的逐阶筛选
- **主帖链接**: 【Community Leader-因子筛选与组合】对SA Not Own Selection的一二三N阶分层框架的逐阶筛选.md
- **讨论数**: 0

我之前发了一个对于Not Own SA的一二三阶分层框架,并实现了在二阶时可以有无限多的因子回测. 现在我在EUR区域回测140054, 已经检查了3w, 还有6w个sa(fit>5)的因子等待检测相关性.受限于即将到来的回测限制, 有个问题就是如何可以只回测可能达到35的因子.我从RA的一二三阶受到启发, 发现对于RA的一二三阶剪枝其实也可以用于SA的一二三阶分层框架, 这里简单介绍一下思路.对于一阶SA(不懂的可以看一下原帖)其实数量并不多, EUR D1这样的大区我筛出来才3523个SA. 对一阶进行全部回测, 之后根据一阶表现进行剪枝, 选择相对较好的一阶因子进行组合得到二阶, 这样就可以减少直接回测二阶的负担. 理论依据来源于, 如果你combo选择的是1, 那么两个一阶SA因子的组合大概率和两个单独的回测的平均差不多.剪枝的方法有筛选出一阶fit>x的, x可以指定, 这样就避免了把垃圾的分层带入二阶计算不同一阶之间的相关性, 选取相关性小的部分进行优先组合排除掉高Prod的一阶因子当然还有其他的剪枝方法, 完全可以参考RA的剪枝方法. 而且SA的剪枝相比于RA的剪枝相对更简单与可靠

---

### 帖子 #87: 【Community Leader-因子筛选与组合】对SA Not Own Selection的一二三....N阶分层框架的逐阶筛选
- **主帖链接**: https://support.worldquantbrain.com【Community Leader-因子筛选与组合】对SA Not Own Selection的一二三N阶分层框架的逐阶筛选_36840466359575.md
- **讨论数**: 0

我之前发了一个对于 [Not Own SA的一二三阶分层框架,]([SuperAlpha] Not Own Selection的一二三N阶分层框架Alpha Template_35377811169175.md)  并实现了在二阶时可以有无限多的因子回测. 现在我在EUR区域回测140054, 已经检查了3w, 还有6w个sa(fit>5)的因子等待检测相关性.

受限于即将到来的回测限制, 有个问题就是如何可以只回测可能达到35的因子.

我从RA的一二三阶受到启发, 发现对于RA的一二三阶剪枝其实也可以用于SA的一二三阶分层框架, 这里简单介绍一下思路.

对于一阶SA(不懂的可以看一下原帖)其实数量并不多, EUR D1这样的大区我筛出来才3523个SA. 对一阶进行全部回测, 之后根据一阶表现进行剪枝, 选择相对较好的一阶因子进行组合得到二阶, 这样就可以减少直接回测二阶的负担. 理论依据来源于, 如果你combo选择的是1, 那么两个一阶SA因子的组合大概率和两个单独的回测的平均差不多.

剪枝的方法有

- 筛选出一阶fit>x的, x可以指定, 这样就避免了把垃圾的分层带入二阶
- 计算不同一阶之间的相关性, 选取相关性小的部分进行优先组合
- 排除掉高Prod的一阶因子

当然还有其他的剪枝方法, 完全可以参考RA的剪枝方法. 而且SA的剪枝相比于RA的剪枝相对更简单与可靠

---

### 帖子 #88: 【ValueFactor预测器】基于Performance评估alpha表现代码优化
- **主帖链接**: 【ValueFactor预测器】基于Performance评估alpha表现代码优化.md
- **讨论数**: 1

首先感谢weijie老师提出的idea:之前的实现都是基于SA实现的, 不过这样有以下几个可能问题无法考虑已提交SA的影响中心化的选择对于结果有一定影响无法综合考虑所有的region所以我觉得是不是可以根据Performance来评估alpha的表现关于如何使用已提交alpha来估算Performance, 可参看这里这样的话, 就可以考虑所有的RA和SA综合考虑不同region速度更快不过, 目前VF和指标的关系还不是很明确代码如下已提交因子的数据采集这里不在赘述, 最后形成这样的一个dataframe, 必须包含以下几列, 包含RA和SA首先通过之前的贴子里的estimate_performance_func估算某三个月某个region-delay下已提交的所有alpha的综合性能接着平等考虑每个region-delay下的结果, 形成这个时间段下所有的已提交的SA和RA的综合Performancedef calc_region_delay(data):local_pnls, local_ret, item_metric = estimate_performance_func(data)item_metric['pnl'] = local_ret.cumsum().to_dict()item_metric['alphaId'] = f"{data['region'].iloc[0]}-{data['delay'].iloc[0]}"return pd.DataFrame([item_metric])def calc_all_region_delay(calc_data):calc_data = calc_data.groupby(['region', 'delay']).apply(calc_region_delay)local_pnls, local_ret, item_metric = estimate_performance_func(calc_data)item_metric['pnl'] = local_ret.cumsum().to_dict()item_metric['alphaId'] = f"{data['region'].iloc[0]}-{data['delay'].iloc[0]}"return pd.DataFrame([item_metric])data = data.sort_values('dateSubmitted')data['year_month'] = data['dateSubmitted'].dt.to_period('M')year_month = sorted(data['year_month'].unique())metric = []for i in range(len(year_month)-2):calc_data = data[data['year_month'].isin([year_month[i], year_month[i+1], year_month[i+2]])]calc_data = calc_data.groupby(['region', 'delay']).apply(calc_region_delay)local_pnls, local_ret, item_metric = estimate_performance_func(calc_data)item_metric['pnl'] = local_ret.cumsum().to_dict()item_metric['month_end'] = year_month[i+2]item_metric = pd.DataFrame([item_metric])metric.append(item_metric)metric = pd.concat(metric, axis=0).reset_index(drop=True)这里需要提供一个vf的数据vf = {'2025-05': 0.75, '2025-04':0.91, '2025-03':0.96, '2025-02': 0.9, '2025-01':0.73, '2024-12':0.77}vf = pd.Series(vf, name='vf')vf.index = pd.to_datetime(vf.index).to_period('M')metric = metric.merge(vf, left_on='month_end', right_index=True, how='left')metric = metric[metric['month_end']>=pd.to_datetime('2024-12').to_period('M')].reset_index(drop=True)绘制pnl图plt.figure(figsize=(10, 6))for item, item_month_end, item_vf in zip(metric.pnl, metric.month_end, metric.vf):item = pd.Series(item)item.index = pd.to_datetime(item.index)plt.plot(item.index, item.values, label=f'{item_month_end}: {item_vf:.2f}')# item.plot(label=item.name, figsize=(10, 6))plt.legend(loc='upper left', frameon=False, prop=font_prop18, bbox_to_anchor=(0, 1))plt.xlabel('Date', fontproperties=font_prop20)plt.ylabel('Pnl', fontproperties=font_prop20)plt.xticks(rotation=45, fontproperties=font_prop18)plt.yticks(fontproperties=font_prop18)plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_ticks_position('both')  # 在x轴的上下两边都显示刻度plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度for spine in plt.gca().spines.values():spine.set_linewidth(2)plt.gca().tick_params(direction='in', length=6, width=2)  # length是刻度的长度，width是刻度的宽度plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')指标和vf的关系plot_cols = ['sharpe', 'turnover', 'returns', 'fitness', 'drawdown', 'margin',]plt.figure(figsize=(2*5, 3*5))for idx, col in enumerate(plot_cols):plt.subplot(3, 2, idx+1)plt.scatter(metric['vf'], metric[col])# 标记最近两个月的metric值colors = ['blue', 'red']for i, item_metric in metric.iloc[-2:].reset_index().iterrows():plt.axhline(item_metric[col], color=colors[i], linestyle='--', lw=1, label=f'{item_metric.month_end}: {item_metric[col]:3f}')plt.legend(loc='best', frameon=False, prop=font_prop16)plt.xlabel('VF', fontproperties=font_prop20)plt.ylabel(col, fontproperties=font_prop20)plt.xticks(fontproperties=font_prop18)plt.yticks(fontproperties=font_prop18)plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_ticks_position('both')  # 在x轴的plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度for spine in plt.gca().spines.values():spine.set_linewidth(2)plt.gca().tick_params(direction='in', length=6, width=2)plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')plt.tight_layout()很奇怪, vf和sharpe还有点负相关=.=!!可能vf是样本外的数据?, 或者vf只是个排名?, 还需要进一步查看, 或许看一下yearly-stats是不是更好一点上述的时间都代表所述三个月的最后一个月

---

### 帖子 #89: 【ValueFactor预测器】基于Performance评估alpha表现代码优化
- **主帖链接**: https://support.worldquantbrain.com【ValueFactor预测器】基于Performance评估alpha表现代码优化_33825528566423.md
- **讨论数**: 1

首先感谢weijie老师提出的idea:

之前的实现都是基于SA实现的, 不过这样有以下几个可能问题

- 无法考虑已提交SA的影响
- 中心化的选择对于结果有一定影响
- 无法综合考虑所有的region

所以我觉得是不是可以根据Performance来评估alpha的表现

关于如何使用已提交alpha来估算Performance, 可参看 [这里](基于已提交alpha估算Performance代码优化_33824958369559.md)

这样的话, 就可以

- 考虑所有的RA和SA
- 综合考虑不同region
- 速度更快

不过, 目前VF和指标的关系还不是很明确

代码如下

已提交因子的数据采集这里不在赘述, 最后形成这样的一个dataframe, 必须包含以下几列, 包含RA和SA


> [!NOTE] [图片 OCR 识别内容]
> data[ [ 'alphald'
> datesubmitted
> pnl
> sharpe
> fitness
> turnover
> returns
> Margin'
> dradorn
> 0Os
> alphald
> dateSubmitted
> sharpe
> ftess
> turover
> Teturls
> margin
> dradown
> XIgQVI
> 2025-04-06
> {2010-04-14:nan "2010-04-15': nan '2010-0
> 2.01
> 1.42
> 0.1154
> 0.0625
> 0.001084
> 0.0389
> OISJGXY
> 2025-04-06
> {2010-04-14:nan "2010-04-15': nan '2010-0
> 1.68
> 1.44
> 0.1305
> 0.0958
> 0.001468
> 0.0594
> RAWewNz
> 2025-04-06
> {2010-04-14:nan '2010-04-15': nan '2010-0
> 223
> 1.44
> 0.2071
> 0.0869
> 0.000839
> 0.0383
> VOnOvqb
> 2025-04-06
> {2010-04-14:nan 2010-04-15': nan '2010-0。
> 1.85
> 1.57
> 0.0395
> 0.0900
> 0.004554
> 0.0665
> abdZp5
> 2025-04-06
> {2010-04-14:nan "2010-04-15': nan '2010-0
> 4.46
> 385
> 0.0776
> 0.0933
> 0.002406
> 0.0183
> 1399
> PATOOpL
> 2025-07-30
> {2013-01-21':00'2013-01-22:8368.0'201.
> 1.80
> 1.16
> 0.1255
> 0.0522
> 0.000832
> 0.0340
> 1400
> INjKaqz
> 2025-07-30
> {2013-01-21':00'2013-01-22:21054.0,"20:
> 1.88
> 1.17
> 0.1103
> 0.0486
> 0.000882
> 0.0387
> 1401
> PATZZnW
> 2025-07-30
> {2013-01-21:0.0,'2013-01-22:853.0,'2013。。
> 1.97
> 1.17
> 0.0631
> 0.0444
> 0.001407
> 0.0245
> 1402
> vojkdk
> 2025-07-30
> {2013-01-21:00,"2013-01-22':-508000'2:
> 1.02
> 1.18
> 0.2476
> 03323
> 0.002684
> 0.4667
> 1403
> 32759U
> 2025-07-30
> {2013-01-21:nan "2013-01-22':00'2013-0
> 409
> 4.16
> 0.1317
> 0.1361
> 0.002068
> 00277
> 1118 rows
> columns
> pnl


首先通过之前的贴子里的estimate_performance_func估算某三个月某个region-delay下已提交的所有alpha的综合性能

接着平等考虑每个region-delay下的结果, 形成这个时间段下所有的已提交的SA和RA的综合Performance

```
def calc_region_delay(data):    local_pnls, local_ret, item_metric = estimate_performance_func(data)    item_metric['pnl'] = local_ret.cumsum().to_dict()    item_metric['alphaId'] = f"{data['region'].iloc[0]}-{data['delay'].iloc[0]}"    return pd.DataFrame([item_metric])def calc_all_region_delay(calc_data):    calc_data = calc_data.groupby(['region', 'delay']).apply(calc_region_delay)    local_pnls, local_ret, item_metric = estimate_performance_func(calc_data)    item_metric['pnl'] = local_ret.cumsum().to_dict()    item_metric['alphaId'] = f"{data['region'].iloc[0]}-{data['delay'].iloc[0]}"    return pd.DataFrame([item_metric])
```

```
data = data.sort_values('dateSubmitted')data['year_month'] = data['dateSubmitted'].dt.to_period('M')year_month = sorted(data['year_month'].unique())metric = []for i in range(len(year_month)-2):    calc_data = data[data['year_month'].isin([year_month[i], year_month[i+1], year_month[i+2]])]    calc_data = calc_data.groupby(['region', 'delay']).apply(calc_region_delay)    local_pnls, local_ret, item_metric = estimate_performance_func(calc_data)    item_metric['pnl'] = local_ret.cumsum().to_dict()    item_metric['month_end'] = year_month[i+2]    item_metric = pd.DataFrame([item_metric])    metric.append(item_metric)metric = pd.concat(metric, axis=0).reset_index(drop=True)
```

这里需要提供一个vf的数据

```
vf = {'2025-05': 0.75, '2025-04':0.91, '2025-03':0.96, '2025-02': 0.9, '2025-01':0.73, '2024-12':0.77}vf = pd.Series(vf, name='vf')vf.index = pd.to_datetime(vf.index).to_period('M')metric = metric.merge(vf, left_on='month_end', right_index=True, how='left')metric = metric[metric['month_end']>=pd.to_datetime('2024-12').to_period('M')].reset_index(drop=True)
```

绘制pnl图

```
plt.figure(figsize=(10, 6))for item, item_month_end, item_vf in zip(metric.pnl, metric.month_end, metric.vf):    item = pd.Series(item)    item.index = pd.to_datetime(item.index)    plt.plot(item.index, item.values, label=f'{item_month_end}: {item_vf:.2f}')    # item.plot(label=item.name, figsize=(10, 6))plt.legend(loc='upper left', frameon=False, prop=font_prop18, bbox_to_anchor=(0, 1))plt.xlabel('Date', fontproperties=font_prop20)plt.ylabel('Pnl', fontproperties=font_prop20)plt.xticks(rotation=45, fontproperties=font_prop18)plt.yticks(fontproperties=font_prop18)plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_ticks_position('both')  # 在x轴的上下两边都显示刻度plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度for spine in plt.gca().spines.values():    spine.set_linewidth(2)plt.gca().tick_params(direction='in', length=6, width=2)  # length是刻度的长度，width是刻度的宽度plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')  
```


> [!NOTE] [图片 OCR 识别内容]
> Ie7
> 2024-12:0.77
> 1.2
> 2025-01:0.73
> 2025-02:0.90
> 2025-03:0.96
> 2025-04:0.91
> 2025-05:0.75
> 忌
> 0.6
> 2025-06: nall
> 2025-07: nan
> 0.3
> Date
> 2016-07-17
> 2022-01-07
> 2013-10-21
> 2019-04-13


指标和vf的关系

```
plot_cols = ['sharpe', 'turnover', 'returns', 'fitness', 'drawdown', 'margin',]plt.figure(figsize=(2*5, 3*5))for idx, col in enumerate(plot_cols):    plt.subplot(3, 2, idx+1)    plt.scatter(metric['vf'], metric[col])    # 标记最近两个月的metric值    colors = ['blue', 'red']    for i, item_metric in metric.iloc[-2:].reset_index().iterrows():        plt.axhline(item_metric[col], color=colors[i], linestyle='--', lw=1, label=f'{item_metric.month_end}: {item_metric[col]:3f}')    plt.legend(loc='best', frameon=False, prop=font_prop16)    plt.xlabel('VF', fontproperties=font_prop20)    plt.ylabel(col, fontproperties=font_prop20)    plt.xticks(fontproperties=font_prop18)    plt.yticks(fontproperties=font_prop18)    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))    plt.gca().xaxis.set_ticks_position('both')  # 在x轴的    plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度    for spine in plt.gca().spines.values():        spine.set_linewidth(2)    plt.gca().tick_params(direction='in', length=6, width=2)    plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')plt.tight_layout()
```


> [!NOTE] [图片 OCR 识别内容]
> 8.8
> 0.165
> 0.150
> 8.0
> 2025-06:0.163371
> 詈
> 
> 0.135
> 2025-07:0.169481
> 7.2
> 0.120
> 2025-06:9.139539
> 2025-07:8.962392
> 0.105
> 0.72
> 0.78
> 0.84
> 0.90
> 0.72
> 0.78
> 0.84
> 90
> 96
> TE
> TE
> 0.13
> 8.0
> 0.12
> 7.2
> 
> 0.11
> 鲁
> 6.4
> 0.10
> 5.6
> 2025-06:0.122011
> 2025-06:7.898325
> 2025-07:0.123720
> 2025-07:7.657435
> 72
> 0.78
> 0.84
> 0.90
> 0.72
> 0.78
> 0.84
> 0.90
> TE
> TE
> 2025-06:0.007365
> 2025-07:0.009269
> 0.014
> 0.0021
> 0.012
> 0.0018
> 
> 0.010
> 
> 0.0015
> 0.008
> 0.0012
> 2025-06:0.001421
> 2025-07:0.001430
> 006.52
> 0.78
> 0.84
> 0.90
> 96
> 0.72
> 0.78
> 0.84
> 0.90
> 0.96
> VF
> T


很奇怪, vf和sharpe还有点负相关=.=!!

可能vf是样本外的数据?, 或者vf只是个排名?, 还需要进一步查看, 或许看一下yearly-stats是不是更好一点

上述的时间都代表所述三个月的最后一个月

---

### 帖子 #90: 【插件】genius operators使用情况分析
- **主帖链接**: 【插件】genius operators使用情况分析.md
- **讨论数**: 2

插件地址： [[链接已屏蔽])

在插件中增加了对于operators使用情况的分析

使用说明

- 打开genius页面，可以看到会增加了两个按钮，其中`运算符分析`是抓取此时已提交的alpha进行分析.`显示运算符分析`是调用之前抓取的分析结果. [图片 (图片已丢失)]
- 无论点击以上哪一个按钮都会在该页面的底部显示一个使用表格, 表格右上角是分析的时间.PS:运算符分析按钮需要等待片刻 [图片 (图片已丢失)]
- 可以通过点击表头以实现Count排序 [图片 (图片已丢失)]

下一步

- 目前没有做抓取的进度条

情况说明

- 需要在genius页面刷新一下，才能看到按钮，具体原因正在排查
- 由于`-`在表达式里可以用作reverse和subtract两个用处,不太好判断是哪个,所以统一为subtract

---

### 帖子 #91: 【插件】genius operators使用情况分析
- **主帖链接**: https://support.worldquantbrain.com【插件】genius operators使用情况分析_28982066443799.md
- **讨论数**: 2

插件地址： [[链接已屏蔽])

在插件中增加了对于operators使用情况的分析

使用说明

- 打开genius页面，可以看到会增加了两个按钮，其中`运算符分析`是抓取此时已提交的alpha进行分析.`显示运算符分析`是调用之前抓取的分析结果. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> 驯Ganlus
> Displaying quarter:
> 2025-01 (Current)
> 运算符分析
> 显示运算符分析

- 无论点击以上哪一个按钮都会在该页面的底部显示一个使用表格, 表格右上角是分析的时间.PS:运算符分析按钮需要等待片刻 
> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 2025-01-05103:36.49.3882
> Category
> Definition
> Count
> Arithmetic
> add(x, Y filter
> false); X+y
> Arithmetic
> eXP(X)
> Arithmetic
> multiplyfx,y
> filterzfalse), X
> Arithmetic
> Signfx)
> Arithmetic
> subtractfx, Y, filterzfalse). X -Y
> Arithmetic
> pasteurizelx)
> Arithmetic
> Jog(X)
> Arithmetic
> purify(x)

- 可以通过点击表头以实现Count排序 
> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 2025-01-05703:36:49.3882
> Category
> Definition
> Count
> Time Series
> _quantilelx,d, driver-"gaussian" )
> Arithmetic
> densifylx)
> Logical
> inputl
> inputz
> Time Series
> tS_corrfx; Y,d)
> Time Series
> [S_ZSCOre(X, d)
> Time Series
> backfill(x lookback = d, k=1, ignore="NAN")
> Cross Sectional
> winsorizelx, std=4)
> Vector
> VeC_minfx)


下一步

- 目前没有做抓取的进度条

情况说明

- 需要在genius页面刷新一下，才能看到按钮，具体原因正在排查
- 由于`-`在表达式里可以用作reverse和subtract两个用处,不太好判断是哪个,所以统一为subtract

---

### 帖子 #92: 【插件】Genius Rank分析代码优化
- **主帖链接**: 【插件】Genius Rank分析代码优化.md
- **讨论数**: 35

插件地址： [[链接已屏蔽])

在插件中增加了对于genius rank的分析，这里非常感谢  [XX42289](/hc/en-us/profiles/14187300941847-XX42289)  提供的 [python分析代码]([L2] 【课代表】最新genius排名模拟代码_29383292162199.md)

使用说明

- 安装完插件后，打开genius页面（如果没有可以刷新一下，这可能和WQ的加载逻辑相关，后续会进行fix），可以看到会增加了两个按钮，其中`排名分析`是抓取排行榜的数据进行分析.`显示排名分析`是调用之前抓取的分析结果（自己的排名数据）. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> Gnius
> Displaying quarter:
> 2025-01 (Curren)
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析

- 无论点击以上哪一个按钮都会在该页面的按钮的下面显示一个自己的分析表格, 表格右上角是分析的时间.PS:排名分析按钮需要等待片刻（抓取时按钮上显示抓取的进度） 
> [!NOTE] [图片 OCR 识别内容]
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> Genius Rank Analysis
> 2025-01-25112:48:02.2082
> 我的排名信息
> 2025-01-2571243.022082
> 总人数:5691 人
> 可能的基准人数:936人
> (交够40个)
> 名个Level 满足的人数 _
> 最终的人数:
> For Expert: 721 /187
> For Master: 22194
> For Grandmaster: 0119
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171/187
> 总排名:15/94
> 总排名:0119
> Operator Count: 533名
> Operator Count: 21 名
> Operator Count:
> Operator AVE: 3名
> Operator AVE: 1 名
> Operator AVg:
> Field Count: 705 名
> Field Count: 23 多
> Field Count:
> Field AVB: 2名
> Field AVg:
> Field AVg:
> Community Activity: 81 名
> Community Activiny: 15 名
> Community Activity:
> Completed Referrals: 58 名
> Completed Referrals: 2 多
> Completed Referrals; 1 名
> Max Simulation Streak: 310名
> Max Simulation Streak: 18 名
> Max Simulation Streak:
> TotalRank; 1692 多
> Tota
> Rank: 81 名
> Tota
> Rank:
> Current level;: Gold
> Best leyel: Gold
> Current quarterend: March 31st. 2025
> COUO

- 此外，还可将鼠标移动到排行榜上的UserId处展示他人的分析数据 
> [!NOTE] [图片 OCR 识别内容]
> X42289 排名信息
> 总人数:5691 人
> Aggregate by:
> 可能的基准人数:936  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 721/187
> For Master: 22194
> For Grandmaster: 0/19
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171187
> 总排名:4194
> 总排名:0/19
> Operator Count: 199名
> Operator Count: 13名
> Operator Count: 1 名
> Operator
> 17名
> Operator
> 2名
> Operator
> 1名
> Rank
> User
> Field Count: 423名
> Field Count: 23名
> Field Count:
> 名
> Field
> 18名
> Field
> 名
> Field
> Community Activity: 20名
> Community Activity: 3名
> Community Activity:
> Completed Referrals: 12名
> Completed Referrals: 1 名
> Completed Referrals:
> 名
> 1,090
> 1279256
> Max Simulation Streak:
> Max Simulation Streak: 16
> Max Simulation Streak:
> 273名
> Total Rank: 962名
> Total Rank: 59名
> Total Rank: 7名
> XP21
> 042289
> Maser
> Maser
> 117
> 0.00
> AVB:
> AVE: 
> AVg:
> AVB: -
> AVg:
> AVB: -


---

### 帖子 #93: 【插件】Genius Rank分析代码优化
- **主帖链接**: https://support.worldquantbrain.com【插件】Genius Rank分析代码优化_29496672188951.md
- **讨论数**: 35

插件地址： [[链接已屏蔽])

在插件中增加了对于genius rank的分析，这里非常感谢  [XX42289](/hc/en-us/profiles/14187300941847-XX42289)  提供的 [python分析代码]([L2] 【课代表】最新genius排名模拟代码_29383292162199.md)

使用说明

- 安装完插件后，打开genius页面（如果没有可以刷新一下，这可能和WQ的加载逻辑相关，后续会进行fix），可以看到会增加了两个按钮，其中`排名分析`是抓取排行榜的数据进行分析.`显示排名分析`是调用之前抓取的分析结果（自己的排名数据）. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> Gnius
> Displaying quarter:
> 2025-01 (Curren)
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析

- 无论点击以上哪一个按钮都会在该页面的按钮的下面显示一个自己的分析表格, 表格右上角是分析的时间.PS:排名分析按钮需要等待片刻（抓取时按钮上显示抓取的进度） 
> [!NOTE] [图片 OCR 识别内容]
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> Genius Rank Analysis
> 2025-01-25112:48:02.2082
> 我的排名信息
> 2025-01-2571243.022082
> 总人数:5691 人
> 可能的基准人数:936人
> (交够40个)
> 名个Level 满足的人数 _
> 最终的人数:
> For Expert: 721 /187
> For Master: 22194
> For Grandmaster: 0119
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171/187
> 总排名:15/94
> 总排名:0119
> Operator Count: 533名
> Operator Count: 21 名
> Operator Count:
> Operator AVE: 3名
> Operator AVE: 1 名
> Operator AVg:
> Field Count: 705 名
> Field Count: 23 多
> Field Count:
> Field AVB: 2名
> Field AVg:
> Field AVg:
> Community Activity: 81 名
> Community Activiny: 15 名
> Community Activity:
> Completed Referrals: 58 名
> Completed Referrals: 2 多
> Completed Referrals; 1 名
> Max Simulation Streak: 310名
> Max Simulation Streak: 18 名
> Max Simulation Streak:
> TotalRank; 1692 多
> Tota
> Rank: 81 名
> Tota
> Rank:
> Current level;: Gold
> Best leyel: Gold
> Current quarterend: March 31st. 2025
> COUO

- 此外，还可将鼠标移动到排行榜上的UserId处展示他人的分析数据 
> [!NOTE] [图片 OCR 识别内容]
> X42289 排名信息
> 总人数:5691 人
> Aggregate by:
> 可能的基准人数:936  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 721/187
> For Master: 22194
> For Grandmaster: 0/19
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171187
> 总排名:4194
> 总排名:0/19
> Operator Count: 199名
> Operator Count: 13名
> Operator Count: 1 名
> Operator
> 17名
> Operator
> 2名
> Operator
> 1名
> Rank
> User
> Field Count: 423名
> Field Count: 23名
> Field Count:
> 名
> Field
> 18名
> Field
> 名
> Field
> Community Activity: 20名
> Community Activity: 3名
> Community Activity:
> Completed Referrals: 12名
> Completed Referrals: 1 名
> Completed Referrals:
> 名
> 1,090
> 1279256
> Max Simulation Streak:
> Max Simulation Streak: 16
> Max Simulation Streak:
> 273名
> Total Rank: 962名
> Total Rank: 59名
> Total Rank: 7名
> XP21
> 042289
> Maser
> Maser
> 117
> 0.00
> AVB:
> AVE: 
> AVg:
> AVB: -
> AVg:
> AVB: -


---

### 帖子 #94: 模拟一个简单的数据库
- **主帖链接**: 【插件】中文论坛中文搜索支持.md
- **讨论数**: 5

众所周不知，WQ论坛对于中文搜索支持度不是很高，导致我平时搜索的时候有点难受，所以我在现有的插件里添加了对于中文搜索的支持。

插件地址： [[链接已屏蔽])

原理：通过爬虫抓取中文论坛的相关帖子，构建数据库，之后使用关键词进行匹配

使用方法：

- 安装插件后在设置页面填写调用的api地址。PS：为防止滥用（毕竟有调用的次数），该api地址目前暂时只向研究小组提供。不过可以根据后面的提供的方式自行构建自己的api地址


> [!NOTE] [图片 OCR 识别内容]
> 中文搜索4P1地址
> Enter api address
> Save


- 之后再搜索界面就会出现中文搜索的按钮


> [!NOTE] [图片 OCR 识别内容]
> Worldouant GRAIN
> SearCh TeSUIs
> By Type
> Try searchinganother keyword.Browse Help Center
> 中撰:中证
> ANPeS IO)
> Articles (0I
> Communty {OI


- 点击这一按钮，等待片刻，即可完成搜索。PS:点击结果时请用中间点击，否则将会在该页面打开帖子，导致搜索结果不见


> [!NOTE] [图片 OCR 识别内容]
> WorldountBAIN
> U
> By Type
> results for "中证" in 中文论坛
> WhRt
> 请问BRAIN平台提供指数的数据吗?  例如沪深300,中证500
> Worlcuant BRAIN
> Communt
> qzie
> AIyRes O
> 吗?  例如深300
> 中证500
> Articles (OI
> Communty
> [Alpha灵感]根据"草木皆兵"因子的文宇描逑进行显化实现
> Worloouant BRAIN
> Communn
> 中女论坛
> 年量价因孑表现色
> 中证500坞强组合乩恭
> (alpha灵感] 华泰单因子测试之波动率困子
> WoruORul
> CTUM
> 中文论坛
> 益率序列标准差
> 对于中证全抬日收益率迸行-元


---

### 帖子 #95: 模拟一个简单的数据库
- **主帖链接**: https://support.worldquantbrain.com【插件】中文论坛中文搜索支持_28949459874071.md
- **讨论数**: 5

众所周不知，WQ论坛对于中文搜索支持度不是很高，导致我平时搜索的时候有点难受，所以我在现有的插件里添加了对于中文搜索的支持。

插件地址： [[链接已屏蔽])

原理：通过爬虫抓取中文论坛的相关帖子，构建数据库，之后使用关键词进行匹配

使用方法：

- 安装插件后在设置页面填写调用的api地址。PS：为防止滥用（毕竟有调用的次数），该api地址目前暂时只向研究小组提供。不过可以根据后面的提供的方式自行构建自己的api地址


> [!NOTE] [图片 OCR 识别内容]
> 中文搜索4P1地址
> Enter api address
> Save


- 之后再搜索界面就会出现中文搜索的按钮


> [!NOTE] [图片 OCR 识别内容]
> Worldouant GRAIN
> SearCh TeSUIs
> By Type
> Try searchinganother keyword.Browse Help Center
> 中撰:中证
> ANPeS IO)
> Articles (0I
> Communty {OI


- 点击这一按钮，等待片刻，即可完成搜索。PS:点击结果时请用中间点击，否则将会在该页面打开帖子，导致搜索结果不见


> [!NOTE] [图片 OCR 识别内容]
> WorldountBAIN
> U
> By Type
> results for "中证" in 中文论坛
> WhRt
> 请问BRAIN平台提供指数的数据吗?  例如沪深300,中证500
> Worlcuant BRAIN
> Communt
> qzie
> AIyRes O
> 吗?  例如深300
> 中证500
> Articles (OI
> Communty
> [Alpha灵感]根据"草木皆兵"因子的文宇描逑进行显化实现
> Worloouant BRAIN
> Communn
> 中女论坛
> 年量价因孑表现色
> 中证500坞强组合乩恭
> (alpha灵感] 华泰单因子测试之波动率困子
> WoruORul
> CTUM
> 中文论坛
> 益率序列标准差
> 对于中证全抬日收益率迸行-元


---

### 帖子 #96: 【本地Corr增强版】本地预估Prod Corr最大值的下限代码优化
- **主帖链接**: 【本地Corr增强版】本地预估Prod Corr最大值的下限代码优化.md
- **讨论数**: 10

众所周知，Prod Corr请求的越多，限速越严重，一小时Check不了几个。而本地Self Corr有时候又有点局限。
所以我就打起了之前进行过Prod Corr的Pnl曲线，以期望用这些Pnl曲线进一步预估Prod Corr。

首先，从最简单的例子入手，假设已知变量a和变量b的相关系数为x，变量b和变量c的相关系数为y，则变量a与变量c的相关系数z的范围为 xy-sqrt(1-x^2)sqrt(1-y^2)<= z <= xy+sqrt(1-x^2)sqrt(1-y^2)

类比我们的任务，a其实是Prod Pool里面的某条Pnl，b是一个之前进行过Prod Corr的Pnl曲线，c是我们想求的Pnl曲线。

Prod Pool是由无数条类似的a的Pnl曲线构成的A。之前进行过Prod Corr的Pnl曲线也有很多（构成了数据集B）。由于A和B都有很多线，c和A的相关系数范围很大，而且不好计算（我也不会求bushi，以下是deepseek的解答


> [!NOTE] [图片 OCR 识别内容]
> 裉据问题荏还;将娈量关系类-到Pnl#线为栏关系效范匿分,$:
> 相关系数范围的推导过程:
> 基本前提设定:
> 设数据集8中每条历史Pnl曲线bj与Prod Pool A中所育曲线的最大相关系数为P1, 即:
> 298
> Cotr(a: bj) = Pi
> (4bj E Bj
> 324
> 设目标茁线c与每个b;的相关系数为Py ,  即:
> Corr(c bj) = Pz .
> 2三元协方差矩阵约束:
> 对每个三元组(a;: bj: c), 其协方差矩阵需满足半正定性
> 由此可推得Corr(a;: C)的范围为=
> PIp
> V(I-p(I-p)S Corai: cCp:p
> V(I-p(l-P)
> 3.全局范围综合:
> SFProd Pool A牛存在无数条#线a;。而c与A的整体枵关系数最大值为:
> @ Corr(ai: C。
> 该最大值的可能范围需对所有b
> 8对应的三元组范围歌极值
> 即:
> 苑围
> [min (pip3
> V(I-P)(I-p)).
> Iax (PIp
> V(I-P)(1-p))]
> 最终答案:
> 目标曲线CSFrod Pool A牛 #线的殂兴系数最大值的可能范围为
> 1(p:p
> P(I- 0)),器(p1p
> '(1-P)(l
> P))]


这个范围起始快接近-1到1了。因此这个范围其实没有什么作用

但是我们关注的是Prod Corr的最大值而非他的范围，尤其是Prod Corr>0.7的。

那么其实我们可以将上述范围的左边界，从取最小值改成取最大值。此时就是预估的Prod Corr的下限

举个不太恰当的例子，假设Prod Pool是个水果市场，我们进行过Prod Corr的是一个水果经销商。我们的任务是批量进一点某种苹果，但是我们不知道该去哪。如果我们在水果经销商处找到了相同品种的，而水果经销商又告诉我们他的水果从水果市场的某个摊位上买的，那就意味着我们到这个摊位上买的话大概率有我们要的水果。只要这个概率高于0.7，我们就去那买。而在我们的corr上，如果这个概率高于0.7，我们就不会进行prod corr检测，而这个概率就是通过最开始的不等式确定的。

至于实践上非常简单，当然首先你得有保存下来的进行过Prod corr的曲线和相应的corr，之后借用我之前的 [本地Self Corr计算代码](本地0误差计算自相关性【即插即用版】代码优化.md) ，计算因子和进行过Prod corr的曲线的相关性，通过不等式获取最小值的集合，取最小值集合的最大值作为本地预估Prod Corr最大值的下限。如果这个下限大于0.7，我们不进行Prod Corr检测。用以减少Check的次数。

```
def calc_prod_min_corr(    alpha_id: str,    know_rets: pd.DataFrame | None = None,    know_corr: pd.Series | None = None,    alpha_result: dict | None = None,    alpha_pnls: pd.DataFrame | None = None):    if alpha_result is None:        alpha_result = cfg.sess.get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    # alpha_rets = alpha_pnls.pct_change(axis=0, fill_method=None)    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    y = know_rets.corrwith(alpha_rets)    corr_min = y*know_corr - np.sqrt(1-know_corr**2)*np.sqrt(1-y**2)    corr_max = y*know_corr + np.sqrt(1-know_corr**2)*np.sqrt(1-y**2)    return corr_min.max()
```

这个过程非常像大家用的Corr的剪枝。

当然我这个东西是不是合理还需要讨论（计算速度和剔除的效率上），或者有其他更好的利用方式也欢迎讨论。

或者多人共建一个已交alpha的pnl库可能更有效率🤣

---

### 帖子 #97: 【本地Corr增强版】本地预估Prod Corr最大值的下限代码优化
- **主帖链接**: https://support.worldquantbrain.com【本地Corr增强版】本地预估Prod Corr最大值的下限代码优化_31431137051927.md
- **讨论数**: 10

众所周知，Prod Corr请求的越多，限速越严重，一小时Check不了几个。而本地Self Corr有时候又有点局限。
所以我就打起了之前进行过Prod Corr的Pnl曲线，以期望用这些Pnl曲线进一步预估Prod Corr。

首先，从最简单的例子入手，假设已知变量a和变量b的相关系数为x，变量b和变量c的相关系数为y，则变量a与变量c的相关系数z的范围为 xy-sqrt(1-x^2)sqrt(1-y^2)<= z <= xy+sqrt(1-x^2)sqrt(1-y^2)

类比我们的任务，a其实是Prod Pool里面的某条Pnl，b是一个之前进行过Prod Corr的Pnl曲线，c是我们想求的Pnl曲线。

Prod Pool是由无数条类似的a的Pnl曲线构成的A。之前进行过Prod Corr的Pnl曲线也有很多（构成了数据集B）。由于A和B都有很多线，c和A的相关系数范围很大，而且不好计算（我也不会求bushi，以下是deepseek的解答


> [!NOTE] [图片 OCR 识别内容]
> 裉据问题荏还;将娈量关系类-到Pnl#线为栏关系效范匿分,$:
> 相关系数范围的推导过程:
> 基本前提设定:
> 设数据集8中每条历史Pnl曲线bj与Prod Pool A中所育曲线的最大相关系数为P1, 即:
> 298
> Cotr(a: bj) = Pi
> (4bj E Bj
> 324
> 设目标茁线c与每个b;的相关系数为Py ,  即:
> Corr(c bj) = Pz .
> 2三元协方差矩阵约束:
> 对每个三元组(a;: bj: c), 其协方差矩阵需满足半正定性
> 由此可推得Corr(a;: C)的范围为=
> PIp
> V(I-p(I-p)S Corai: cCp:p
> V(I-p(l-P)
> 3.全局范围综合:
> SFProd Pool A牛存在无数条#线a;。而c与A的整体枵关系数最大值为:
> @ Corr(ai: C。
> 该最大值的可能范围需对所有b
> 8对应的三元组范围歌极值
> 即:
> 苑围
> [min (pip3
> V(I-P)(I-p)).
> Iax (PIp
> V(I-P)(1-p))]
> 最终答案:
> 目标曲线CSFrod Pool A牛 #线的殂兴系数最大值的可能范围为
> 1(p:p
> P(I- 0)),器(p1p
> '(1-P)(l
> P))]


这个范围起始快接近-1到1了。因此这个范围其实没有什么作用

但是我们关注的是Prod Corr的最大值而非他的范围，尤其是Prod Corr>0.7的。

那么其实我们可以将上述范围的左边界，从取最小值改成取最大值。此时就是预估的Prod Corr的下限

举个不太恰当的例子，假设Prod Pool是个水果市场，我们进行过Prod Corr的是一个水果经销商。我们的任务是批量进一点某种苹果，但是我们不知道该去哪。如果我们在水果经销商处找到了相同品种的，而水果经销商又告诉我们他的水果从水果市场的某个摊位上买的，那就意味着我们到这个摊位上买的话大概率有我们要的水果。只要这个概率高于0.7，我们就去那买。而在我们的corr上，如果这个概率高于0.7，我们就不会进行prod corr检测，而这个概率就是通过最开始的不等式确定的。

至于实践上非常简单，当然首先你得有保存下来的进行过Prod corr的曲线和相应的corr，之后借用我之前的 [本地Self Corr计算代码](本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md) ，计算因子和进行过Prod corr的曲线的相关性，通过不等式获取最小值的集合，取最小值集合的最大值作为本地预估Prod Corr最大值的下限。如果这个下限大于0.7，我们不进行Prod Corr检测。用以减少Check的次数。

```
def calc_prod_min_corr(    alpha_id: str,    know_rets: pd.DataFrame | None = None,    know_corr: pd.Series | None = None,    alpha_result: dict | None = None,    alpha_pnls: pd.DataFrame | None = None):    if alpha_result is None:        alpha_result = cfg.sess.get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    # alpha_rets = alpha_pnls.pct_change(axis=0, fill_method=None)    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    y = know_rets.corrwith(alpha_rets)    corr_min = y*know_corr - np.sqrt(1-know_corr**2)*np.sqrt(1-y**2)    corr_max = y*know_corr + np.sqrt(1-know_corr**2)*np.sqrt(1-y**2)    return corr_min.max()
```

这个过程非常像大家用的Corr的剪枝。

当然我这个东西是不是合理还需要讨论（计算速度和剔除的效率上），或者有其他更好的利用方式也欢迎讨论。

或者多人共建一个已交alpha的pnl库可能更有效率🤣

---

### 帖子 #98: 转换为 Pandas DataFrame
- **主帖链接**: 【网页监控】基于Streamlit和数据库的网页监控进程代码优化.md
- **讨论数**: 6

由于我是基于数据库跑alpha的，每次想监控跑了多少，还有多少没跑，程序是不是在运行，都要用相应的代码在数据库或者命令行中运行。为了便捷我使用Streamlit做了个网页来查看运行情况（可能需要公共ip）

其中Streamlit是一个非常简单的制作网页的方法，在访问网页时调用后端python代码实时渲染网页，通过st.write可以向网页中写入dataframe，st.markdown向网页写入markdown语法

**一些库的导入和侧边栏制作**

因为我用的时mongo数据库管理alpha，可以适时改写成自己的

```python

import streamlit as st

from streamlit_extras.colored_header import colored_header

from streamlit_option_menu import option_menu

from streamlit_extras.badges import badge

# from streamlit_card import card

import pandas as pd

import numpy as np

from pymongo import MongoClient, UpdateOne

from pymongo import errors

from datetime import datetime

import pytz

import json

#侧边栏制作

with st.sidebar:

select_option = option_menu(

"WQB-监控",

[

"数据库监控",

"收入监控",

],

icons=[

'house',

'arrow-repeat',

],

menu_icon="boxes", default_index=0

)

if select_option == "数据库监控":

这个网页你想做的内容

其余同理

```

**首先是程序监控**

效果如下

[图片 (图片已丢失)]

通过下述代码，可以获得正在运行的程序，注意第一行的command应该改成你程序运行命令，以显示你正在运行的程序

```python

command = 'ps aux | grep "python main.py --action" | grep -v grep'

result = subprocess.run(command, shell=True, text=True, capture_output=True)

# 解析输出

data = []

for line in result.stdout.strip().split("\n"):

parts = line.split(maxsplit=10)  # 解析 ps aux 的格式

if len(parts) == 11:  # 确保解析正确

data.append(parts)

# 定义列名（ps aux 的标准列）

columns = ["USER", "PID", "CPU%", "MEM%", "VSZ", "RSS", "TTY", "STAT", "START", "TIME", "COMMAND"]

# 转换为 Pandas DataFrame

df = pd.DataFrame(data, columns=columns)

colored_header(label=f"程序监控",description="",color_name="red-70")

st.write(df)

```

**接下来是数据库alpha状态监控**

效果如下

[图片 (图片已丢失)]

我把alpha用两个标识，一个是alpha state（用于描述该alpha是什么状态，等待运行，正在运行，运行完毕，正在获取is数据，获取完毕，以及因为各种原因丢弃的alpha和运行失败的），一个是bs stage（目前的alpha属于第几阶段，或者模板是什么）

目前我在自动跑regular alpha和super alpha，所以会有两个数据库要监视

通过mongo查询相应的alpha状态，然后写入网页，这样我就可以通过看pending，running来查看还有多少要运行，正在跑的alpha的状态

由于每个人的思路不太一样，这里就只是抛砖引玉，不放具体的代码了，写入的核心还是st.markdown，st.write

**收入监控**

效果展示

[图片 (图片已丢失)]

这部分的核心主要是把每天的收入实时展示，我也可以不用因为收入专门查看网页了，并且按照base payment的计算方式展示出相应的影响因素，为了后续分析收入提供便利

这部分代码也不展示了，只是说一下思路

按钮可以使用

cols = st.columns(3)

cols[0].button("刷新收入数据", on_click=reload_fee_data, use_container_width=True)

**当然也可以监控更多的东西，但是我现在没有想到还要弄啥监控，慢慢更这个帖子吧**

---

### 帖子 #99: 转换为 Pandas DataFrame
- **主帖链接**: https://support.worldquantbrain.com【网页监控】基于Streamlit和数据库的网页监控进程代码优化_30329770583959.md
- **讨论数**: 6

由于我是基于数据库跑alpha的，每次想监控跑了多少，还有多少没跑，程序是不是在运行，都要用相应的代码在数据库或者命令行中运行。为了便捷我使用Streamlit做了个网页来查看运行情况（可能需要公共ip）

其中Streamlit是一个非常简单的制作网页的方法，在访问网页时调用后端python代码实时渲染网页，通过st.write可以向网页中写入dataframe，st.markdown向网页写入markdown语法

**一些库的导入和侧边栏制作**

因为我用的时mongo数据库管理alpha，可以适时改写成自己的

```python

import streamlit as st

from streamlit_extras.colored_header import colored_header

from streamlit_option_menu import option_menu

from streamlit_extras.badges import badge

# from streamlit_card import card

import pandas as pd

import numpy as np

from pymongo import MongoClient, UpdateOne

from pymongo import errors

from datetime import datetime

import pytz

import json

#侧边栏制作

with st.sidebar:

select_option = option_menu(

"WQB-监控",

[

"数据库监控",

"收入监控",

],

icons=[

'house',

'arrow-repeat',

],

menu_icon="boxes", default_index=0

)

if select_option == "数据库监控":

这个网页你想做的内容

其余同理

```

**首先是程序监控**

效果如下


> [!NOTE] [图片 OCR 识别内容]
> WQB- 监控
> 程序监控
> 数据库监控
> PID
> action
> UISeI_
> Collection_
> name
> 收入监控
> 193873
> TUIn
> 193874
> get
> 458295
> TUIn
> 458296
> get


通过下述代码，可以获得正在运行的程序，注意第一行的command应该改成你程序运行命令，以显示你正在运行的程序

```python

command = 'ps aux | grep "python main.py --action" | grep -v grep'

result = subprocess.run(command, shell=True, text=True, capture_output=True)

# 解析输出

data = []

for line in result.stdout.strip().split("\n"):

parts = line.split(maxsplit=10)  # 解析 ps aux 的格式

if len(parts) == 11:  # 确保解析正确

data.append(parts)

# 定义列名（ps aux 的标准列）

columns = ["USER", "PID", "CPU%", "MEM%", "VSZ", "RSS", "TTY", "STAT", "START", "TIME", "COMMAND"]

# 转换为 Pandas DataFrame

df = pd.DataFrame(data, columns=columns)

colored_header(label=f"程序监控",description="",color_name="red-70")

st.write(df)

```

**接下来是数据库alpha状态监控**

效果如下


> [!NOTE] [图片 OCR 识别内容]
> WQB-监控
> 数据库: WQBGeniusQl
> 数据库监控
> 收入监控
> alpha state
> Pending
> Running
> Run_Done
> Check_Done
> Dropout_ZYSHARPE
> Dropout_Fitness
> Dropout_Stock
> Run_Error
> 些数字
> bs stage
> 999
> 些数字
> 数据库: WQBSAQI
> alpha state
> Run_Done
> Check_Done
> Run Errol
> bs stage
> Pending
> Running


我把alpha用两个标识，一个是alpha state（用于描述该alpha是什么状态，等待运行，正在运行，运行完毕，正在获取is数据，获取完毕，以及因为各种原因丢弃的alpha和运行失败的），一个是bs stage（目前的alpha属于第几阶段，或者模板是什么）

目前我在自动跑regular alpha和super alpha，所以会有两个数据库要监视

通过mongo查询相应的alpha状态，然后写入网页，这样我就可以通过看pending，running来查看还有多少要运行，正在跑的alpha的状态

由于每个人的思路不太一样，这里就只是抛砖引玉，不放具体的代码了，写入的核心还是st.markdown，st.write

**收入监控**

效果展示


> [!NOTE] [图片 OCR 识别内容]
> WQB-监控
> 收入监控
> 数据库监控
> 刷新收入数据
> 收入监控
> 抓取的美东时间:2025-02-28
> SUPERAlpha
> Tee
> SUDer
> TyDE
> aUtHOI
> dateSubmitted
> themes
> pyramids
> alphald
> regIon
> Unlerse
> Ttness
> delay
> prodCorrelation
> ValueFactor
> 131
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-28
> 1.0
> OLELnd2
> USA
> T0P3000
> 5.99
> 0.6738
> 0.77
> 5.38
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-27
> OLIIXaXL
> USA
> T0P3000
> 5.24
> 0.679
> 0.77
> 5.11
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-26
> 1.0
> ANPmEdE
> USA
> T0P3000
> 5.07
> 0.5992
> 0.77
> 5.09
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-25
> 1.0
> PRNrKAJ
> USA
> T0P3000
> 5.77
> 0.675
> 0.77
> 5.49
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-24
> 1.0
> IdWOMENI
> USA
> T0P3000
> 7.02
> 0.6863
> 0.77
> REGULAR Alpha
> Tee_regUlar
> TDe
> JUthOI
> JateSubmitteo
> Themes
> pyramids
> alphald
> reSIOI
> Unwerse
> Titness
> delay
> prodCorrelation
> ValueFactor
> 4.26
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-26
> 1.0
> 28b3YW1
> EUR
> T0P2500
> 1.09
> 0.6929
> 0.77
> 3.98
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-27
> 1.0
> KONVWOO
> EUR
> T0P2500
> 1.12
> 0.6993
> 0.77
> 1an
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-28
> 1.0
> X3V1ZVn
> EUR
> T0P2500
> 1.09
> 0.5627
> 077


这部分的核心主要是把每天的收入实时展示，我也可以不用因为收入专门查看网页了，并且按照base payment的计算方式展示出相应的影响因素，为了后续分析收入提供便利

这部分代码也不展示了，只是说一下思路

按钮可以使用

cols = st.columns(3)

cols[0].button("刷新收入数据", on_click=reload_fee_data, use_container_width=True)

**当然也可以监控更多的东西，但是我现在没有想到还要弄啥监控，慢慢更这个帖子吧**

---

### 帖子 #100: 分享：用 Python 调用 Zendesk Community API 获取帖子、评论并发布内容的完整流程
- **主帖链接**: 分享用 Python 调用 Zendesk Community API 获取帖子评论并发布内容的完整流程.md
- **讨论数**: 1

分享：用 Python 调用 Zendesk Community API 获取帖子、评论并发布内容的完整流程最近我整理了一套用 Python 访问 Zendesk Community 的方法，包括读取论坛 topic 下的帖子、获取帖子详情、批量获取评论、保存数据，以及在有权限的情况下通过 API 发布新帖子。这里把完整流程记录下来，供需要做内容整理、论坛检索或个人知识归档的同学参考。本文只讨论官方 API 和正常登录态下的使用方式。实际能否读取、评论或发帖，取决于当前账号权限、目标 topic 的权限设置，以及 Zendesk Help Center session 是否有效。一、常用 Community API 总览Zendesk Community 常用接口主要包括 topic、post、comment 三类。功能接口获取所有 topicsGET /api/v2/community/topics.json获取指定 topic 信息GET /api/v2/community/topics/{topic_id}.json获取指定 topic 下的帖子GET /api/v2/community/topics/{topic_id}/posts.json获取单个帖子详情GET /api/v2/community/posts/{post_id}.json获取某个帖子的评论GET /api/v2/community/posts/{post_id}/comments.json搜索社区帖子GET /api/v2/help_center/community_posts/search.json获取当前 Help Center sessionGET /api/v2/help_center/sessions.json创建新帖子POST /api/v2/community/posts.json其中，读取内容主要用 GET；发布内容主要用 POST。使用 cookie session 发 POST 请求时，通常还需要从/api/v2/help_center/sessions.json获取 CSRF token。二、建立登录 session首先需要完成 WorldQuant Brain 登录，然后通过 support authentication 链路进入 Zendesk Help Center。示例代码如下：import os
import httpx

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

for key in ["http_proxy", "https_proxy", "all_proxy", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"]:
    os.environ.pop(key, None)

os.environ["NO_PROXY"] = "localhost,127.0.0.1,::1,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12"

auth = (username, password)

client = httpx.Client(
    follow_redirects=False,
    timeout=30,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
)

r = client.post("[链接已屏蔽] auth=auth)
print("login:", r.status_code, r.url)

r = client.get(
    "[链接已屏蔽]
    "?return_to=https%3A%2F%2Fsupport.worldquantbrain.com%2Fhc%2Fen-us%2Fcommunity%2Ftopics"
)

print("support redirect:", r.status_code, r.headers.get("location"))

while r.status_code in (301, 302, 303, 307, 308):
    location = r.headers.get("location")
    if not location:
        break
    r = client.get(location)
    print("redirect:", r.status_code, r.url, r.headers.get("location"))

print(r.status_code)
print(r.text[:1000])如果最后返回真实论坛页面，说明 session 可能已经建立成功。如果返回Just a moment...、challenges.cloudflare.com或Enable JavaScript and cookies to continue，说明请求被 Cloudflare challenge 拦截，当前不是目标内容。三、获取 topic 下的帖子列表假设已经知道 topic id，可以直接获取该 topic 下的帖子。TOPIC_ID = 32983704970903

r = client.get(
    f"[链接已屏蔽]
    params={
        "page[size]": 10,
        "sort_by": "recent_activity"
    }
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])如果请求成功，返回 JSON 中通常包含posts字段。每个 post 里会包含帖子 id、标题、正文、作者、创建时间、更新时间、评论数、投票数等信息。可以这样提取基础字段：data = r.json()
posts = data.get("posts", [])

for post in posts:
    print("=" * 80)
    print("id:", post.get("id"))
    print("title:", post.get("title"))
    print("html_url:", post.get("html_url"))
    print("created_at:", post.get("created_at"))
    print("updated_at:", post.get("updated_at"))
    print("comment_count:", post.get("comment_count"))
    print("vote_sum:", post.get("vote_sum"))四、处理分页：获取 topic 下所有帖子Zendesk API 可能会分页返回结果。如果帖子很多，不能只请求第一页，需要检查meta.has_more和links.next。def fetch_all_topic_posts(client, topic_id, page_size=100):
    url = f"[链接已屏蔽]
    params = {
        "page[size]": page_size,
        "sort_by": "recent_activity"
    }

    all_posts = []

    while url:
        r = client.get(url, params=params)
        print("GET:", r.status_code, r.url)

        head = r.text[:500]

        if "Just a moment" in head or "challenges.cloudflare.com" in head:
            raise RuntimeError("请求被 Cloudflare challenge 拦截。")

        if "<html" in head.lower():
            raise RuntimeError("返回了 HTML 页面，可能未登录或被跳转到 access 页面。")

        r.raise_for_status()
        data = r.json()

        posts = data.get("posts", [])
        all_posts.extend(posts)

        meta = data.get("meta") or {}
        links = data.get("links") or {}

        if meta.get("has_more"):
            url = links.get("next")
            params = None
        else:
            url = None

    return all_posts


posts = fetch_all_topic_posts(client, TOPIC_ID)
print("total posts:", len(posts))五、获取单个帖子详情如果已经知道 post id，可以读取单个帖子详情。POST_ID = 40373405530647

r = client.get(
    f"[链接已屏蔽]
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])

data = r.json()
post = data.get("post", {})

print("title:", post.get("title"))
print("details:", post.get("details"))
print("html_url:", post.get("html_url"))注意：details字段通常是 HTML。如果想转成纯文本，可以用 BeautifulSoup。from bs4 import BeautifulSoup

html = post.get("details") or ""
text = BeautifulSoup(html, "html.parser").get_text("\\n", strip=True)

print(text)六、获取某个帖子的评论评论接口是：GET /api/v2/community/posts/{post_id}/comments.json示例：POST_ID = 40373405530647

r = client.get(
    f"[链接已屏蔽]
    params={
        "page[size]": 100,
        "include": "users"
    }
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])如果成功，返回 JSON 通常包含comments字段。可以这样解析：data = r.json()
comments = data.get("comments", [])
users = data.get("users", [])

user_map = {u.get("id"): u for u in users}

for c in comments:
    author = user_map.get(c.get("author_id"), {})
    print("=" * 80)
    print("comment id:", c.get("id"))
    print("author:", author.get("name") or c.get("author_id"))
    print("created_at:", c.get("created_at"))
    print("updated_at:", c.get("updated_at"))
    print("body:", c.get("body"))评论正文通常也可能是 HTML，可以继续用 BeautifulSoup 转为纯文本。from bs4 import BeautifulSoup

for c in comments:
    html = c.get("body") or ""
    text = BeautifulSoup(html, "html.parser").get_text("\\n", strip=True)
    print(text)七、分页获取某个帖子的所有评论如果一个帖子评论很多，也需要分页。def fetch_all_post_comments(client, post_id, page_size=100):
    url = f"[链接已屏蔽]
    params = {
        "page[size]": page_size,
        "include": "users"
    }

    all_comments = []
    all_users = {}

    while url:
        r = client.get(url, params=params)
        print("GET:", r.status_code, r.url)

        head = r.text[:500]

        if "Just a moment" in head or "challenges.cloudflare.com" in head:
            raise RuntimeError("请求被 Cloudflare challenge 拦截。")

        if "<html" in head.lower():
            raise RuntimeError("返回了 HTML 页面，可能未登录或被跳转到 access 页面。")

        r.raise_for_status()
        data = r.json()

        for u in data.get("users", []):
            all_users[u.get("id")] = u

        all_comments.extend(data.get("comments", []))

        meta = data.get("meta") or {}
        links = data.get("links") or {}

        if meta.get("has_more"):
            url = links.get("next")
            params = None
        else:
            url = None

    return all_comments, all_users


comments, users = fetch_all_post_comments(client, POST_ID)
print("total comments:", len(comments))八、批量获取某个 topic 下所有帖子和评论如果想把一个 topic 下的所有帖子和评论都保存下来，可以先获取所有帖子，再逐个获取评论。from bs4 import BeautifulSoup

def html_to_text(html):
    return BeautifulSoup(html or "", "html.parser").get_text("\\n", strip=True)


def collect_topic_posts_with_comments(client, topic_id):
    posts = fetch_all_topic_posts(client, topic_id)

    result = []

    for index, post in enumerate(posts, start=1):
        post_id = post.get("id")
        print(f"[{index}/{len(posts)}] fetching comments for post:", post_id)

        comments, users = fetch_all_post_comments(client, post_id)

        user_map = {uid: user for uid, user in users.items()}

        item = {
            "post_id": post_id,
            "title": post.get("title"),
            "html_url": post.get("html_url"),
            "created_at": post.get("created_at"),
            "updated_at": post.get("updated_at"),
            "vote_sum": post.get("vote_sum"),
            "comment_count": post.get("comment_count"),
            "details_html": post.get("details"),
            "details_text": html_to_text(post.get("details")),
            "comments": []
        }

        for c in comments:
            author = user_map.get(c.get("author_id"), {})
            item["comments"].append({
                "comment_id": c.get("id"),
                "author_id": c.get("author_id"),
                "author_name": author.get("name"),
                "created_at": c.get("created_at"),
                "updated_at": c.get("updated_at"),
                "body_html": c.get("body"),
                "body_text": html_to_text(c.get("body")),
            })

        result.append(item)

    return result


dataset = collect_topic_posts_with_comments(client, TOPIC_ID)
print("posts collected:", len(dataset))九、保存为 JSONJSON 适合保留完整结构，包括每个帖子下面的评论列表。import json

with open("zendesk_topic_posts_with_comments.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print("saved to zendesk_topic_posts_with_comments.json")十、保存为 CSVCSV 更适合用 Excel 或 pandas 查看。可以把每一条评论展开成一行。如果某个帖子没有评论，也保留一行帖子信息。import csv

with open("zendesk_topic_posts_with_comments.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "post_id",
            "title",
            "html_url",
            "post_created_at",
            "post_updated_at",
            "vote_sum",
            "comment_count",
            "post_text",
            "comment_id",
            "comment_author_name",
            "comment_created_at",
            "comment_updated_at",
            "comment_text",
        ]
    )

    writer.writeheader()

    for post in dataset:
        comments = post.get("comments") or []

        if not comments:
            writer.writerow({
                "post_id": post.get("post_id"),
                "title": post.get("title"),
                "html_url": post.get("html_url"),
                "post_created_at": post.get("created_at"),
                "post_updated_at": post.get("updated_at"),
                "vote_sum": post.get("vote_sum"),
                "comment_count": post.get("comment_count"),
                "post_text": post.get("details_text"),
                "comment_id": "",
                "comment_author_name": "",
                "comment_created_at": "",
                "comment_updated_at": "",
                "comment_text": "",
            })
        else:
            for c in comments:
                writer.writerow({
                    "post_id": post.get("post_id"),
                    "title": post.get("title"),
                    "html_url": post.get("html_url"),
                    "post_created_at": post.get("created_at"),
                    "post_updated_at": post.get("updated_at"),
                    "vote_sum": post.get("vote_sum"),
                    "comment_count": post.get("comment_count"),
                    "post_text": post.get("details_text"),
                    "comment_id": c.get("comment_id"),
                    "comment_author_name": c.get("author_name"),
                    "comment_created_at": c.get("created_at"),
                    "comment_updated_at": c.get("updated_at"),
                    "comment_text": c.get("body_text"),
                })

print("saved to zendesk_topic_posts_with_comments.csv")十一、搜索社区帖子除了遍历 topic，也可以直接用搜索接口查关键词。例如搜索某个 topic 内包含 alpha 的帖子：r = client.get(
    "[链接已屏蔽]
    params={
        "query": "alpha",
        "topic": TOPIC_ID,
    }
)

print(r.status_code)
print(r.headers.get("content-type"))
print(r.text[:2000])这个方式适合查找某个关键词相关的历史讨论，比如 alpha 表达式、operator、simulation、submission、decay、neutralization 等。十二、发布新帖子发帖前建议先获取 CSRF token。session_r = client.get("[链接已屏蔽])

print(session_r.status_code)
print(session_r.headers.get("content-type"))
print(session_r.text[:1000])

session_r.raise_for_status()
csrf = session_r.json()["current_session"]["csrf_token"]然后构造请求头和 payload。headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-CSRF-Token": csrf,
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"[链接已屏蔽]
    "Origin": "[链接已屏蔽]
}

payload = {
    "post": {
        "title": "测试发帖：API 连通性检查",
        "details": "<p>这是通过 Zendesk Community API 发布的测试内容。</p>",
        "topic_id": TOPIC_ID,
    },
    "notify_subscribers": False,
}

r = client.post(
    "[链接已屏蔽]
    json=payload,
    headers=headers,
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])成功时一般返回201 Created，响应里会包含新帖子的id和html_url。十三、回复帖子评论如果账号有评论权限，也可以通过 API 给帖子添加评论。评论接口通常是：POST /api/v2/community/posts/{post_id}/comments.json示例：POST_ID = 40373405530647

payload = {
    "comment": {
        "body": "<p>这是通过 API 发布的一条测试评论。</p>"
    }
}

r = client.post(
    f"[链接已屏蔽]
    json=payload,
    headers=headers,
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])如果返回201，说明评论发布成功。如果返回403，通常表示当前账号没有评论权限、CSRF/session 不完整，或者目标帖子不允许评论。十四、常见状态码含义状态码常见含义200GET 请求成功，正常返回数据。201POST 创建成功，例如成功发帖或成功评论。401未认证，当前请求没有有效登录态。403已被拒绝，常见原因是账号无权限、CSRF 缺失、session 不完整或 topic/post 不允许操作。404资源不存在，或者当前账号无权看到该资源。422请求格式不合法，例如 title 为空、details 不合法、topic_id 不可用。429请求过快，触发 rate limit，需要降低频率。十五、排查 403 的建议遇到403 Forbidden时，不要只看状态码，建议把响应内容也打印出来。print("status:", r.status_code)
print("final url:", r.url)
print("content-type:", r.headers.get("content-type"))
print("headers:", dict(r.headers))
print("body head:", r.text[:2000])可以按下面几种情况判断：如果返回 JSON，并明确写着 forbidden 或 not allowed，大概率是账号或 topic 权限不足。如果返回 HTML，并且是 access/login 页面，说明 support session 没有建立成功。如果返回Just a moment...或challenges.cloudflare.com，说明请求被 Cloudflare challenge 拦截。如果 GET 能成功但 POST 失败，优先检查 CSRF token、Origin、Referer 和账号发帖权限。如果同一个账号在浏览器里也看不到发帖或评论入口，那么 API 通常也不会允许发帖或评论。十六、推荐的完整封装下面是一个更完整的工具类写法，适合后续复用。import json
import csv
from bs4 import BeautifulSoup


class ZendeskCommunityClient:
    def __init__(self, client, base_url="[链接已屏蔽]):
        self.client = client
        self.base_url = base_url.rstrip("/")

    def _check_response(self, r):
        head = r.text[:500]

        if "Just a moment" in head or "challenges.cloudflare.com" in head:
            raise RuntimeError("请求被 Cloudflare challenge 拦截。")

        if "<html" in head.lower():
            raise RuntimeError("返回了 HTML 页面，可能未登录或被跳转到 access 页面。")

        r.raise_for_status()
        return r

    def html_to_text(self, html):
        return BeautifulSoup(html or "", "html.parser").get_text("\\n", strip=True)

    def get_csrf_token(self):
        r = self.client.get(f"{self.base_url}/api/v2/help_center/sessions.json")
        self._check_response(r)
        return r.json()["current_session"]["csrf_token"]

    def get_topic_posts(self, topic_id, page_size=100):
        url = f"{self.base_url}/api/v2/community/topics/{topic_id}/posts.json"
        params = {
            "page[size]": page_size,
            "sort_by": "recent_activity"
        }

        all_posts = []

        while url:
            r = self.client.get(url, params=params)
            self._check_response(r)

            data = r.json()
            all_posts.extend(data.get("posts", []))

            meta = data.get("meta") or {}
            links = data.get("links") or {}

            if meta.get("has_more"):
                url = links.get("next")
                params = None
            else:
                url = None

        return all_posts

    def get_post_comments(self, post_id, page_size=100):
        url = f"{self.base_url}/api/v2/community/posts/{post_id}/comments.json"
        params = {
            "page[size]": page_size,
            "include": "users"
        }

        all_comments = []
        users = {}

        while url:
            r = self.client.get(url, params=params)
            self._check_response(r)

            data = r.json()

            all_comments.extend(data.get("comments", []))

            for user in data.get("users", []):
                users[user.get("id")] = user

            meta = data.get("meta") or {}
            links = data.get("links") or {}

            if meta.get("has_more"):
                url = links.get("next")
                params = None
            else:
                url = None

        return all_comments, users

    def collect_topic(self, topic_id):
        posts = self.get_topic_posts(topic_id)
        result = []

        for i, post in enumerate(posts, start=1):
            post_id = post.get("id")
            print(f"[{i}/{len(posts)}] post_id={post_id}")

            comments, users = self.get_post_comments(post_id)

            result.append({
                "post_id": post_id,
                "title": post.get("title"),
                "html_url": post.get("html_url"),
                "created_at": post.get("created_at"),
                "updated_at": post.get("updated_at"),
                "vote_sum": post.get("vote_sum"),
                "comment_count": post.get("comment_count"),
                "details_html": post.get("details"),
                "details_text": self.html_to_text(post.get("details")),
                "comments": [
                    {
                        "comment_id": c.get("id"),
                        "author_id": c.get("author_id"),
                        "author_name": (users.get(c.get("author_id")) or {}).get("name"),
                        "created_at": c.get("created_at"),
                        "updated_at": c.get("updated_at"),
                        "body_html": c.get("body"),
                        "body_text": self.html_to_text(c.get("body")),
                    }
                    for c in comments
                ],
            })

        return result

    def create_post(self, topic_id, title, html_details, notify_subscribers=False):
        csrf = self.get_csrf_token()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-CSRF-Token": csrf,
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{self.base_url}/hc/en-us/community/topics/{topic_id}",
            "Origin": self.base_url,
        }

        payload = {
            "post": {
                "title": title,
                "details": html_details,
                "topic_id": int(topic_id),
            },
            "notify_subscribers": notify_subscribers,
        }

        r = self.client.post(
            f"{self.base_url}/api/v2/community/posts.json",
            json=payload,
            headers=headers,
        )

        self._check_response(r)
        return r.json().get("post")

    def create_comment(self, post_id, html_body):
        csrf = self.get_csrf_token()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-CSRF-Token": csrf,
            "X-Requested-With": "XMLHttpRequest",
            "Origin": self.base_url,
        }

        payload = {
            "comment": {
                "body": html_body
            }
        }

        r = self.client.post(
            f"{self.base_url}/api/v2/community/posts/{post_id}/comments.json",
            json=payload,
            headers=headers,
        )

        self._check_response(r)
        return r.json().get("comment")


zc = ZendeskCommunityClient(client)

dataset = zc.collect_topic(32983704970903)

with open("topic_dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)十七、使用建议只保存自己有权限访问的内容。不要公开用户名、密码、cookie、CSRF token 或 session 信息。批量获取时建议降低请求频率，不要对论坛造成压力。如果需要长期归档，建议保存 JSON，因为 JSON 能保留帖子与评论的层级关系。如果需要人工分析，建议额外导出 CSV，方便用 Excel、pandas 或数据库处理。发帖或评论前，建议先用一条简短测试内容确认权限。整体来说，读取论坛内容的核心是 topic、post、comment 三层结构；发帖和评论的核心是有效登录态、CSRF token 和目标板块权限。只要这三点满足，使用官方 API 对论坛内容进行整理和发布会比较直接。

---

### 帖子 #101: 分享：用 Python 调用 Zendesk Community API 获取帖子、评论并发布内容的完整流程
- **主帖链接**: https://support.worldquantbrain.com分享用 Python 调用 Zendesk Community API 获取帖子评论并发布内容的完整流程_40458235734295.md
- **讨论数**: 1

## 分享：用 Python 调用 Zendesk Community API 获取帖子、评论并发布内容的完整流程

最近我整理了一套用 Python 访问 Zendesk Community 的方法，包括读取论坛 topic 下的帖子、获取帖子详情、批量获取评论、保存数据，以及在有权限的情况下通过 API 发布新帖子。这里把完整流程记录下来，供需要做内容整理、论坛检索或个人知识归档的同学参考。

本文只讨论官方 API 和正常登录态下的使用方式。实际能否读取、评论或发帖，取决于当前账号权限、目标 topic 的权限设置，以及 Zendesk Help Center session 是否有效。

### 一、常用 Community API 总览

Zendesk Community 常用接口主要包括 topic、post、comment 三类。

功能
接口

获取所有 topics
 `GET /api/v2/community/topics.json` 

获取指定 topic 信息
 `GET /api/v2/community/topics/{topic_id}.json` 

获取指定 topic 下的帖子
 `GET /api/v2/community/topics/{topic_id}/posts.json` 

获取单个帖子详情
 `GET /api/v2/community/posts/{post_id}.json` 

获取某个帖子的评论
 `GET /api/v2/community/posts/{post_id}/comments.json` 

搜索社区帖子
 `GET /api/v2/help_center/community_posts/search.json` 

获取当前 Help Center session
 `GET /api/v2/help_center/sessions.json` 

创建新帖子
 `POST /api/v2/community/posts.json` 

其中，读取内容主要用 GET；发布内容主要用 POST。使用 cookie session 发 POST 请求时，通常还需要从  `/api/v2/help_center/sessions.json`  获取 CSRF token。

### 二、建立登录 session

首先需要完成 WorldQuant Brain 登录，然后通过 support authentication 链路进入 Zendesk Help Center。示例代码如下：

```
import os
import httpx

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

for key in ["http_proxy", "https_proxy", "all_proxy", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"]:
    os.environ.pop(key, None)

os.environ["NO_PROXY"] = "localhost,127.0.0.1,::1,192.168.0.0/16,10.0.0.0/8,172.16.0.0/12"

auth = (username, password)

client = httpx.Client(
    follow_redirects=False,
    timeout=30,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    },
)

r = client.post("[链接已屏蔽] auth=auth)
print("login:", r.status_code, r.url)

r = client.get(
    "[链接已屏蔽]
    "?return_to=https%3A%2F%2Fsupport.worldquantbrain.com%2Fhc%2Fen-us%2Fcommunity%2Ftopics"
)

print("support redirect:", r.status_code, r.headers.get("location"))

while r.status_code in (301, 302, 303, 307, 308):
    location = r.headers.get("location")
    if not location:
        break
    r = client.get(location)
    print("redirect:", r.status_code, r.url, r.headers.get("location"))

print(r.status_code)
print(r.text[:1000])
```

如果最后返回真实论坛页面，说明 session 可能已经建立成功。如果返回  `Just a moment...` 、 `challenges.cloudflare.com`  或  `Enable JavaScript and cookies to continue` ，说明请求被 Cloudflare challenge 拦截，当前不是目标内容。

### 三、获取 topic 下的帖子列表

假设已经知道 topic id，可以直接获取该 topic 下的帖子。

```
TOPIC_ID = 32983704970903

r = client.get(
    f"[链接已屏蔽]
    params={
        "page[size]": 10,
        "sort_by": "recent_activity"
    }
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])
```

如果请求成功，返回 JSON 中通常包含  `posts`  字段。每个 post 里会包含帖子 id、标题、正文、作者、创建时间、更新时间、评论数、投票数等信息。

可以这样提取基础字段：

```
data = r.json()
posts = data.get("posts", [])

for post in posts:
    print("=" * 80)
    print("id:", post.get("id"))
    print("title:", post.get("title"))
    print("html_url:", post.get("html_url"))
    print("created_at:", post.get("created_at"))
    print("updated_at:", post.get("updated_at"))
    print("comment_count:", post.get("comment_count"))
    print("vote_sum:", post.get("vote_sum"))
```

### 四、处理分页：获取 topic 下所有帖子

Zendesk API 可能会分页返回结果。如果帖子很多，不能只请求第一页，需要检查  `meta.has_more`  和  `links.next` 。

```
def fetch_all_topic_posts(client, topic_id, page_size=100):
    url = f"[链接已屏蔽]
    params = {
        "page[size]": page_size,
        "sort_by": "recent_activity"
    }

    all_posts = []

    while url:
        r = client.get(url, params=params)
        print("GET:", r.status_code, r.url)

        head = r.text[:500]

        if "Just a moment" in head or "challenges.cloudflare.com" in head:
            raise RuntimeError("请求被 Cloudflare challenge 拦截。")

        if "<html" in head.lower():
            raise RuntimeError("返回了 HTML 页面，可能未登录或被跳转到 access 页面。")

        r.raise_for_status()
        data = r.json()

        posts = data.get("posts", [])
        all_posts.extend(posts)

        meta = data.get("meta") or {}
        links = data.get("links") or {}

        if meta.get("has_more"):
            url = links.get("next")
            params = None
        else:
            url = None

    return all_posts

posts = fetch_all_topic_posts(client, TOPIC_ID)
print("total posts:", len(posts))
```

### 五、获取单个帖子详情

如果已经知道 post id，可以读取单个帖子详情。

```
POST_ID = 40373405530647

r = client.get(
    f"[链接已屏蔽]
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])

data = r.json()
post = data.get("post", {})

print("title:", post.get("title"))
print("details:", post.get("details"))
print("html_url:", post.get("html_url"))
```

注意： `details`  字段通常是 HTML。如果想转成纯文本，可以用 BeautifulSoup。

```
from bs4 import BeautifulSoup

html = post.get("details") or ""
text = BeautifulSoup(html, "html.parser").get_text("\\n", strip=True)

print(text)
```

### 六、获取某个帖子的评论

评论接口是：

```
GET /api/v2/community/posts/{post_id}/comments.json
```

示例：

```
POST_ID = 40373405530647

r = client.get(
    f"[链接已屏蔽]
    params={
        "page[size]": 100,
        "include": "users"
    }
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])
```

如果成功，返回 JSON 通常包含  `comments`  字段。可以这样解析：

```
data = r.json()
comments = data.get("comments", [])
users = data.get("users", [])

user_map = {u.get("id"): u for u in users}

for c in comments:
    author = user_map.get(c.get("author_id"), {})
    print("=" * 80)
    print("comment id:", c.get("id"))
    print("author:", author.get("name") or c.get("author_id"))
    print("created_at:", c.get("created_at"))
    print("updated_at:", c.get("updated_at"))
    print("body:", c.get("body"))
```

评论正文通常也可能是 HTML，可以继续用 BeautifulSoup 转为纯文本。

```
from bs4 import BeautifulSoup

for c in comments:
    html = c.get("body") or ""
    text = BeautifulSoup(html, "html.parser").get_text("\\n", strip=True)
    print(text)
```

### 七、分页获取某个帖子的所有评论

如果一个帖子评论很多，也需要分页。

```
def fetch_all_post_comments(client, post_id, page_size=100):
    url = f"[链接已屏蔽]
    params = {
        "page[size]": page_size,
        "include": "users"
    }

    all_comments = []
    all_users = {}

    while url:
        r = client.get(url, params=params)
        print("GET:", r.status_code, r.url)

        head = r.text[:500]

        if "Just a moment" in head or "challenges.cloudflare.com" in head:
            raise RuntimeError("请求被 Cloudflare challenge 拦截。")

        if "<html" in head.lower():
            raise RuntimeError("返回了 HTML 页面，可能未登录或被跳转到 access 页面。")

        r.raise_for_status()
        data = r.json()

        for u in data.get("users", []):
            all_users[u.get("id")] = u

        all_comments.extend(data.get("comments", []))

        meta = data.get("meta") or {}
        links = data.get("links") or {}

        if meta.get("has_more"):
            url = links.get("next")
            params = None
        else:
            url = None

    return all_comments, all_users

comments, users = fetch_all_post_comments(client, POST_ID)
print("total comments:", len(comments))
```

### 八、批量获取某个 topic 下所有帖子和评论

如果想把一个 topic 下的所有帖子和评论都保存下来，可以先获取所有帖子，再逐个获取评论。

```
from bs4 import BeautifulSoup

def html_to_text(html):
    return BeautifulSoup(html or "", "html.parser").get_text("\\n", strip=True)

def collect_topic_posts_with_comments(client, topic_id):
    posts = fetch_all_topic_posts(client, topic_id)

    result = []

    for index, post in enumerate(posts, start=1):
        post_id = post.get("id")
        print(f"[{index}/{len(posts)}] fetching comments for post:", post_id)

        comments, users = fetch_all_post_comments(client, post_id)

        user_map = {uid: user for uid, user in users.items()}

        item = {
            "post_id": post_id,
            "title": post.get("title"),
            "html_url": post.get("html_url"),
            "created_at": post.get("created_at"),
            "updated_at": post.get("updated_at"),
            "vote_sum": post.get("vote_sum"),
            "comment_count": post.get("comment_count"),
            "details_html": post.get("details"),
            "details_text": html_to_text(post.get("details")),
            "comments": []
        }

        for c in comments:
            author = user_map.get(c.get("author_id"), {})
            item["comments"].append({
                "comment_id": c.get("id"),
                "author_id": c.get("author_id"),
                "author_name": author.get("name"),
                "created_at": c.get("created_at"),
                "updated_at": c.get("updated_at"),
                "body_html": c.get("body"),
                "body_text": html_to_text(c.get("body")),
            })

        result.append(item)

    return result

dataset = collect_topic_posts_with_comments(client, TOPIC_ID)
print("posts collected:", len(dataset))
```

### 九、保存为 JSON

JSON 适合保留完整结构，包括每个帖子下面的评论列表。

```
import json

with open("zendesk_topic_posts_with_comments.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print("saved to zendesk_topic_posts_with_comments.json")
```

### 十、保存为 CSV

CSV 更适合用 Excel 或 pandas 查看。可以把每一条评论展开成一行。如果某个帖子没有评论，也保留一行帖子信息。

```
import csv

with open("zendesk_topic_posts_with_comments.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "post_id",
            "title",
            "html_url",
            "post_created_at",
            "post_updated_at",
            "vote_sum",
            "comment_count",
            "post_text",
            "comment_id",
            "comment_author_name",
            "comment_created_at",
            "comment_updated_at",
            "comment_text",
        ]
    )

    writer.writeheader()

    for post in dataset:
        comments = post.get("comments") or []

        if not comments:
            writer.writerow({
                "post_id": post.get("post_id"),
                "title": post.get("title"),
                "html_url": post.get("html_url"),
                "post_created_at": post.get("created_at"),
                "post_updated_at": post.get("updated_at"),
                "vote_sum": post.get("vote_sum"),
                "comment_count": post.get("comment_count"),
                "post_text": post.get("details_text"),
                "comment_id": "",
                "comment_author_name": "",
                "comment_created_at": "",
                "comment_updated_at": "",
                "comment_text": "",
            })
        else:
            for c in comments:
                writer.writerow({
                    "post_id": post.get("post_id"),
                    "title": post.get("title"),
                    "html_url": post.get("html_url"),
                    "post_created_at": post.get("created_at"),
                    "post_updated_at": post.get("updated_at"),
                    "vote_sum": post.get("vote_sum"),
                    "comment_count": post.get("comment_count"),
                    "post_text": post.get("details_text"),
                    "comment_id": c.get("comment_id"),
                    "comment_author_name": c.get("author_name"),
                    "comment_created_at": c.get("created_at"),
                    "comment_updated_at": c.get("updated_at"),
                    "comment_text": c.get("body_text"),
                })

print("saved to zendesk_topic_posts_with_comments.csv")
```

### 十一、搜索社区帖子

除了遍历 topic，也可以直接用搜索接口查关键词。例如搜索某个 topic 内包含 alpha 的帖子：

```
r = client.get(
    "[链接已屏蔽]
    params={
        "query": "alpha",
        "topic": TOPIC_ID,
    }
)

print(r.status_code)
print(r.headers.get("content-type"))
print(r.text[:2000])
```

这个方式适合查找某个关键词相关的历史讨论，比如 alpha 表达式、operator、simulation、submission、decay、neutralization 等。

### 十二、发布新帖子

发帖前建议先获取 CSRF token。

```
session_r = client.get("[链接已屏蔽])

print(session_r.status_code)
print(session_r.headers.get("content-type"))
print(session_r.text[:1000])

session_r.raise_for_status()
csrf = session_r.json()["current_session"]["csrf_token"]
```

然后构造请求头和 payload。

```
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-CSRF-Token": csrf,
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"[链接已屏蔽]
    "Origin": "[链接已屏蔽]
}

payload = {
    "post": {
        "title": "测试发帖：API 连通性检查",
        "details": "<p>这是通过 Zendesk Community API 发布的测试内容。</p>",
        "topic_id": TOPIC_ID,
    },
    "notify_subscribers": False,
}

r = client.post(
    "[链接已屏蔽]
    json=payload,
    headers=headers,
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])
```

成功时一般返回  `201 Created` ，响应里会包含新帖子的  `id`  和  `html_url` 。

### 十三、回复帖子评论

如果账号有评论权限，也可以通过 API 给帖子添加评论。评论接口通常是：

```
POST /api/v2/community/posts/{post_id}/comments.json
```

示例：

```
POST_ID = 40373405530647

payload = {
    "comment": {
        "body": "<p>这是通过 API 发布的一条测试评论。</p>"
    }
}

r = client.post(
    f"[链接已屏蔽]
    json=payload,
    headers=headers,
)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print(r.text[:2000])
```

如果返回  `201` ，说明评论发布成功。如果返回  `403` ，通常表示当前账号没有评论权限、CSRF/session 不完整，或者目标帖子不允许评论。

### 十四、常见状态码含义

状态码
常见含义

 `200` 
GET 请求成功，正常返回数据。

 `201` 
POST 创建成功，例如成功发帖或成功评论。

 `401` 
未认证，当前请求没有有效登录态。

 `403` 
已被拒绝，常见原因是账号无权限、CSRF 缺失、session 不完整或 topic/post 不允许操作。

 `404` 
资源不存在，或者当前账号无权看到该资源。

 `422` 
请求格式不合法，例如 title 为空、details 不合法、topic_id 不可用。

 `429` 
请求过快，触发 rate limit，需要降低频率。

### 十五、排查 403 的建议

遇到  `403 Forbidden`  时，不要只看状态码，建议把响应内容也打印出来。

```
print("status:", r.status_code)
print("final url:", r.url)
print("content-type:", r.headers.get("content-type"))
print("headers:", dict(r.headers))
print("body head:", r.text[:2000])
```

可以按下面几种情况判断：

- 如果返回 JSON，并明确写着 forbidden 或 not allowed，大概率是账号或 topic 权限不足。
- 如果返回 HTML，并且是 access/login 页面，说明 support session 没有建立成功。
- 如果返回  `Just a moment...`  或  `challenges.cloudflare.com` ，说明请求被 Cloudflare challenge 拦截。
- 如果 GET 能成功但 POST 失败，优先检查 CSRF token、Origin、Referer 和账号发帖权限。
- 如果同一个账号在浏览器里也看不到发帖或评论入口，那么 API 通常也不会允许发帖或评论。

### 十六、推荐的完整封装

下面是一个更完整的工具类写法，适合后续复用。

```
import json
import csv
from bs4 import BeautifulSoup

class ZendeskCommunityClient:
    def __init__(self, client, base_url="[链接已屏蔽]):
        self.client = client
        self.base_url = base_url.rstrip("/")

    def _check_response(self, r):
        head = r.text[:500]

        if "Just a moment" in head or "challenges.cloudflare.com" in head:
            raise RuntimeError("请求被 Cloudflare challenge 拦截。")

        if "<html" in head.lower():
            raise RuntimeError("返回了 HTML 页面，可能未登录或被跳转到 access 页面。")

        r.raise_for_status()
        return r

    def html_to_text(self, html):
        return BeautifulSoup(html or "", "html.parser").get_text("\\n", strip=True)

    def get_csrf_token(self):
        r = self.client.get(f"{self.base_url}/api/v2/help_center/sessions.json")
        self._check_response(r)
        return r.json()["current_session"]["csrf_token"]

    def get_topic_posts(self, topic_id, page_size=100):
        url = f"{self.base_url}/api/v2/community/topics/{topic_id}/posts.json"
        params = {
            "page[size]": page_size,
            "sort_by": "recent_activity"
        }

        all_posts = []

        while url:
            r = self.client.get(url, params=params)
            self._check_response(r)

            data = r.json()
            all_posts.extend(data.get("posts", []))

            meta = data.get("meta") or {}
            links = data.get("links") or {}

            if meta.get("has_more"):
                url = links.get("next")
                params = None
            else:
                url = None

        return all_posts

    def get_post_comments(self, post_id, page_size=100):
        url = f"{self.base_url}/api/v2/community/posts/{post_id}/comments.json"
        params = {
            "page[size]": page_size,
            "include": "users"
        }

        all_comments = []
        users = {}

        while url:
            r = self.client.get(url, params=params)
            self._check_response(r)

            data = r.json()

            all_comments.extend(data.get("comments", []))

            for user in data.get("users", []):
                users[user.get("id")] = user

            meta = data.get("meta") or {}
            links = data.get("links") or {}

            if meta.get("has_more"):
                url = links.get("next")
                params = None
            else:
                url = None

        return all_comments, users

    def collect_topic(self, topic_id):
        posts = self.get_topic_posts(topic_id)
        result = []

        for i, post in enumerate(posts, start=1):
            post_id = post.get("id")
            print(f"[{i}/{len(posts)}] post_id={post_id}")

            comments, users = self.get_post_comments(post_id)

            result.append({
                "post_id": post_id,
                "title": post.get("title"),
                "html_url": post.get("html_url"),
                "created_at": post.get("created_at"),
                "updated_at": post.get("updated_at"),
                "vote_sum": post.get("vote_sum"),
                "comment_count": post.get("comment_count"),
                "details_html": post.get("details"),
                "details_text": self.html_to_text(post.get("details")),
                "comments": [
                    {
                        "comment_id": c.get("id"),
                        "author_id": c.get("author_id"),
                        "author_name": (users.get(c.get("author_id")) or {}).get("name"),
                        "created_at": c.get("created_at"),
                        "updated_at": c.get("updated_at"),
                        "body_html": c.get("body"),
                        "body_text": self.html_to_text(c.get("body")),
                    }
                    for c in comments
                ],
            })

        return result

    def create_post(self, topic_id, title, html_details, notify_subscribers=False):
        csrf = self.get_csrf_token()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-CSRF-Token": csrf,
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{self.base_url}/hc/en-us/community/topics/{topic_id}",
            "Origin": self.base_url,
        }

        payload = {
            "post": {
                "title": title,
                "details": html_details,
                "topic_id": int(topic_id),
            },
            "notify_subscribers": notify_subscribers,
        }

        r = self.client.post(
            f"{self.base_url}/api/v2/community/posts.json",
            json=payload,
            headers=headers,
        )

        self._check_response(r)
        return r.json().get("post")

    def create_comment(self, post_id, html_body):
        csrf = self.get_csrf_token()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-CSRF-Token": csrf,
            "X-Requested-With": "XMLHttpRequest",
            "Origin": self.base_url,
        }

        payload = {
            "comment": {
                "body": html_body
            }
        }

        r = self.client.post(
            f"{self.base_url}/api/v2/community/posts/{post_id}/comments.json",
            json=payload,
            headers=headers,
        )

        self._check_response(r)
        return r.json().get("comment")

zc = ZendeskCommunityClient(client)

dataset = zc.collect_topic(32983704970903)

with open("topic_dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)
```

### 十七、使用建议

- 只保存自己有权限访问的内容。
- 不要公开用户名、密码、cookie、CSRF token 或 session 信息。
- 批量获取时建议降低请求频率，不要对论坛造成压力。
- 如果需要长期归档，建议保存 JSON，因为 JSON 能保留帖子与评论的层级关系。
- 如果需要人工分析，建议额外导出 CSV，方便用 Excel、pandas 或数据库处理。
- 发帖或评论前，建议先用一条简短测试内容确认权限。

整体来说，读取论坛内容的核心是 topic、post、comment 三层结构；发帖和评论的核心是有效登录态、CSRF token 和目标板块权限。只要这三点满足，使用官方 API 对论坛内容进行整理和发布会比较直接。

---

### 帖子 #102: 本地0误差计算自相关性【即插即用版】代码优化
- **主帖链接**: 本地0误差计算自相关性【即插即用版】代码优化.md
- **讨论数**: 64

基于顾问 WL27618 (Rank 97)发现的本地计算自相关性方法的落地，self-corr只计算本region里提交的所有alphas首先一些函数，由于有函数说明，这里就不详细展开了import requestsimport pandas as pdimport loggingimport timeimport requestsfrom typing import Optional, Tuplefrom typing import Tuple, Dict, Listfrom typing import Union, List, Tuplefrom concurrent.futures import ThreadPoolExecutorimport picklefrom collections import defaultdictimport numpy as npfrom tqdm import tqdmfrom pathlib import Pathdef sign_in(username, password):s = requests.Session()s.auth = (username, password)try:response = s.post('[链接已屏蔽])response.raise_for_status()logging.info("Successfully signed in")return sexcept requests.exceptions.RequestException as e:logging.error(f"Login failed: {e}")return Nonedef save_obj(obj: object, name: str) -> None:"""保存对象到文件中，以 pickle 格式序列化。Args:obj (object): 需要保存的对象。name (str): 文件名（不包含扩展名），保存的文件将以 '.pickle' 为扩展名。Returns:None: 此函数无返回值。Raises:pickle.PickleError: 如果序列化过程中发生错误。IOError: 如果文件写入过程中发生 I/O 错误。"""with open(name + '.pickle', 'wb') as f:pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)def load_obj(name: str) -> object:"""加载指定名称的 pickle 文件并返回其内容。此函数会打开一个以 `.pickle` 为扩展名的文件，并使用 `pickle` 模块加载其内容。Args:name (str): 不带扩展名的文件名称。Returns:object: 从 pickle 文件中加载的 Python 对象。Raises:FileNotFoundError: 如果指定的文件不存在。pickle.UnpicklingError: 如果文件内容无法被正确反序列化。"""with open(name + '.pickle', 'rb') as f:return pickle.load(f)def wait_get(url: str, max_retries: int = 10) -> "Response":"""发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。Args:url (str): 目标 URL。max_retries (int, optional): 最大重试次数，默认为 10。Returns:Response: 请求的响应对象。"""retries = 0while retries < max_retries:while True:simulation_progress = sess.get(url)if simulation_progress.headers.get("Retry-After", 0) == 0:breaktime.sleep(float(simulation_progress.headers["Retry-After"]))if simulation_progress.status_code < 400:breakelse:time.sleep(2 ** retries)retries += 1return simulation_progressdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:"""获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，并将其转换为 pandas DataFrame 格式，方便后续数据处理。Args:alpha_id (str): Alpha 的唯一标识符。Returns:pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。"""pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])df = df.rename(columns={'date':'Date', 'pnl':alpha_id})df = df[['Date', alpha_id]]return dfdef get_alpha_pnls(alphas: list[dict],alpha_pnls: Optional[pd.DataFrame] = None,alpha_ids: Optional[dict[str, list]] = None) -> Tuple[dict[str, list], pd.DataFrame]:"""获取 alpha 的 PnL 数据，并按区域分类 alpha 的 ID。Args:alphas (list[dict]): 包含 alpha 信息的列表，每个元素是一个字典，包含 alpha 的 ID 和设置等信息。alpha_pnls (Optional[pd.DataFrame], 可选): 已有的 alpha PnL 数据，默认为空的 DataFrame。alpha_ids (Optional[dict[str, list]], 可选): 按区域分类的 alpha ID 字典，默认为空字典。Returns:Tuple[dict[str, list], pd.DataFrame]:- 按区域分类的 alpha ID 字典。- 包含所有 alpha 的 PnL 数据的 DataFrame。"""if alpha_ids is None:alpha_ids = defaultdict(list)if alpha_pnls is None:alpha_pnls = pd.DataFrame()new_alphas = [item for item in alphas if item['id'] not in alpha_pnls.columns]if not new_alphas:return alpha_ids, alpha_pnlsfor item_alpha in new_alphas:alpha_ids[item_alpha['settings']['region']].append(item_alpha['id'])fetch_pnl_func = lambda alpha_id: _get_alpha_pnl(alpha_id).set_index('Date')with ThreadPoolExecutor(max_workers=10) as executor:results = executor.map(fetch_pnl_func, [item['id'] for item in new_alphas])alpha_pnls = pd.concat([alpha_pnls] + list(results), axis=1)alpha_pnls.sort_index(inplace=True)return alpha_ids, alpha_pnlsdef get_os_alphas(limit: int = 100, get_first: bool = False) -> List[Dict]:"""获取OS阶段的alpha列表。此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。Args:limit (int, optional): 每次请求获取的alpha数量限制。默认为100。get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。Returns:List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。"""fetched_alphas = []offset = 0retries = 0total_alphas = 100while len(fetched_alphas) < total_alphas:print(f"Fetching alphas from offset {offset} to {offset + limit}")url = f"[链接已屏蔽] = wait_get(url).json()if offset == 0:total_alphas = res['count']alphas = res["results"]fetched_alphas.extend(alphas)if len(alphas) < limit:breakoffset += limitif get_first:breakreturn fetched_alphas[:total_alphas]def calc_self_corr(alpha_id: str,os_alpha_rets: pd.DataFrame | None = None,os_alpha_ids: dict[str, str] | None = None,alpha_result: dict | None = None,return_alpha_pnls: bool = False,alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:"""计算指定 alpha 与其他 alpha 的最大自相关性。Args:alpha_id (str): 目标 alpha 的唯一标识符。os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。Returns:float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。"""if alpha_result is None:alpha_result = wait_get(f"[链接已屏蔽]).json()if alpha_pnls is not None:if len(alpha_pnls) == 0:alpha_pnls = Noneif alpha_pnls is None:_, alpha_pnls = get_alpha_pnls([alpha_result])alpha_pnls = alpha_pnls[alpha_id]alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]# os_alpha_rets = os_alpha_rets.replace(0, np.nan)# alpha_rets = alpha_rets.replace(0, np.nan)print(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()if np.isnan(self_corr):self_corr = 0if return_alpha_pnls:return self_corr, alpha_pnlselse:return self_corrdef download_data(flag_increment=True):"""下载数据并保存到指定路径。此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。Args:flag_increment (bool): 是否使用增量下载，默认为 True。"""if flag_increment:try:os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]except Exception as e:logging.error(f"Failed to load existing data: {e}")os_alpha_ids = Noneos_alpha_pnls = Noneexist_alpha = []ppac_alpha_ids = []else:os_alpha_ids = Noneos_alpha_pnls = Noneexist_alpha = []ppac_alpha_ids = []if os_alpha_ids is None:alphas = get_os_alphas(limit=100, get_first=False)else:alphas = get_os_alphas(limit=30, get_first=True)alphas = [item for item in alphas if item['id'] not in exist_alpha]ppac_alpha_ids += [item['id'] for item in alphas for item_match in item['classifications'] if item_match['name'] == 'Power Pool Alpha']os_alpha_ids, os_alpha_pnls = get_alpha_pnls(alphas, alpha_pnls=os_alpha_pnls, alpha_ids=os_alpha_ids)save_obj(os_alpha_ids, str(cfg.data_path / 'os_alpha_ids'))save_obj(os_alpha_pnls, str(cfg.data_path / 'os_alpha_pnls'))save_obj(ppac_alpha_ids, str(cfg.data_path / 'ppac_alpha_ids'))print(f'新下载的alpha数量: {len(alphas)}, 目前总共alpha数量: {os_alpha_pnls.shape[1]}')def load_data(tag=None):"""加载数据。此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。Args:tag (str): 数据标记，默认为 None。"""os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))if tag=='PPAC':for item in os_alpha_ids:os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha in ppac_alpha_ids]elif tag=='SelfCorr':for item in os_alpha_ids:os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha not in ppac_alpha_ids]else:os_alpha_ids = os_alpha_idsexist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]os_alpha_pnls = os_alpha_pnls[exist_alpha]os_alpha_rets = os_alpha_pnls - os_alpha_pnls.ffill().shift(1)os_alpha_rets = os_alpha_rets[pd.to_datetime(os_alpha_rets.index)>pd.to_datetime(os_alpha_rets.index).max() - pd.DateOffset(years=4)]return os_alpha_ids, os_alpha_rets首先把上述函数拷贝出来在配置的cfg里添加账户和密码以及os_alpha保存的路径class cfg:username = ""password = ""data_path = Path('.')sess = sign_in(cfg.username, cfg.password)增量下载OS数据，下载好的数据将会保存在data_path里# 增量下载数据download_data(flag_increment=True)之后加载数据，计算corr。其中`load_data`函数里有一个可选参数tag。来区分获得alpha，如果设置tag='PPAC'则只获取PPAC池子里的alpha，如果设置tag='SelfCorr'则只获取除了PPAC池子里的其他alpha如果不设置或者 设置为None，则获取所有提交的alphacalc_self_corr返回最大的自相关性alpha_id = 'OJwdKNb'os_alpha_ids, os_alpha_rets = load_data()calc_self_corr(alpha_id=alpha_id,os_alpha_rets=os_alpha_rets,os_alpha_ids=os_alpha_ids,)我在此选了两个例子用以展示结果第一个 例子是一个`厂alpha`其wq平台的线上self-corr如下通过上述代码本地计算的结果如下其线上PPAC结果为： Power Pool correlation 0.0356 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.通过上述代码本地计算的结果如下第二个 例子是一个正常的例子其wq平台的线上self-corr如下通过上述代码本地计算的结果如下其线上PPAC结果为： Power Pool correlation 0.4901 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.通过上述代码本地计算的结果如下

---

### 帖子 #103: 增量下载数据download_data(flag_increment=True)
- **主帖链接**: https://support.worldquantbrain.com本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md
- **讨论数**: 30

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

### 帖子 #104: 检测alpha是否可以用于本赛季代码优化
- **主帖链接**: 检测alpha是否可以用于本赛季代码优化.md
- **讨论数**: 1

众所周知，还有几天就定级了，到时候运算符和数据集都会重新随机。那么就会导致库存里的alpha报销。因此，我优化了一下 [顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97)) 的提供的 [ast解析表达式的代码](../顾问 MS51256 (Rank 28)/[Commented] 用python ast提取表达式中operator和datafield的方法代码优化.md) ，从而可以用于检测alpha是否可以用于本赛季。

原理，使用ast解析表达式里的ops和fields，和自己可用的进行比较

```
import astimport reimport keyworddef parse_alpha(alpha_expression: str) -> dict[str, list[str]]:    """解析表达式并提取操作符和数据字段。    该函数用于解析输入的表达式字符串，进行预处理、AST解析，并提取其中的操作符和数据字段。    它会过滤掉无效的数据字段（如Python关键字、已定义变量等），并保留操作符的顺序和重复项。    Args:        alpha_expression (str): 输入的表达式字符串。    Returns:        Dict[str, List[str]]: 包含操作符和数据字段的字典。            - 'operators': 提取的操作符列表，保留顺序和重复项。            - 'data_fields': 提取的有效数据字段列表，已过滤无效项。    """    # 运算符预处理    replacements = [        (r'\b(or)\b', 'logical_or'),  # 保护逻辑函数名        (r'\b(and)\b', 'logical_and'),        (r'\&\&', ' and '),          # 转换运算符        (r'\|\|', ' or '),        (r'(?<!\=)\!(?!\=)', ' not '),        (r'\?', ' if '),        (r'\:', ' else '),        (r'\bNaN\b', '0')           # 处理特殊常量    ]    for pattern, repl in replacements:        alpha_expression = re.sub(pattern, repl, alpha_expression)    # 清理注释和字符串    alpha_expression = re.sub(r'(?m)^\s*(//|#).*\n?', '', alpha_expression)    alpha_expression = re.sub(r'"([^"]*)"', "0", alpha_expression)    # 处理和 python 内置逻辑表达式冲突    alpha_expression = re.sub(r'\band\(', 'and_(', alpha_expression)  # 替换 'and('    alpha_expression = re.sub(r'\bor\(', 'or_(', alpha_expression)  # 替换 'or('    # 合并多行没有分号的表达式    lines = alpha_expression.splitlines()    merged_lines = []    temp_line = ""    for line in lines:        stripped_line = line.strip()        if stripped_line and not stripped_line.endswith(';'):  # 如果行不以分号结尾            temp_line += " " + stripped_line  # 合并到上一行        else:            if temp_line:  # 如果存在合并的内容                merged_lines.append(temp_line.strip())  # 添加到结果中            merged_lines.append(stripped_line)  # 添加当前行            temp_line = ""  # 清空临时合并内容    # 如果最后一行没有以分号结尾，确保它被处理    if temp_line:        merged_lines.append(temp_line.strip())    alpha_expression = "\n".join(line.strip() for line in merged_lines)    # 解析AST    tree = ast.parse(alpha_expression)       operator_map = {        ast.Add: 'add', ast.Sub: 'subtract',        ast.Mult: 'multiply', ast.Div: 'divide',        ast.Pow: 'power', ast.USub: 'reverse',        ast.Lt: 'less', ast.Gt: 'greater',        ast.LtE: 'less_equal', ast.GtE: 'greater_equal',        ast.Eq: 'equal', ast.NotEq: 'not_equal',        ast.And: 'and', ast.Or: 'or',        ast.Not: 'not'    }    operators = []  # 改为列表    data_fields = [] # 改为列表    defined_vars = set()    for node in ast.walk(tree):        # 变量定义检测        if isinstance(node, ast.Assign):            for target in node.targets:                if isinstance(target, ast.Name):                    defined_vars.add(target.id)        # 函数调用捕获        if isinstance(node, ast.Call):            if isinstance(node.func, ast.Name):                func_name = node.func.id                # 恢复原始函数名                if func_name.lower() == 'logical_or':                    func_name = 'or'                elif func_name.lower() == 'logical_and':                    func_name = 'and'                operators.append(func_name)            elif isinstance(node.func, ast.Attribute):                operators.append(node.func.attr)        # 运算符捕获        if isinstance(node, (ast.BinOp, ast.UnaryOp, ast.Compare, ast.BoolOp)):            ops = []            if isinstance(node, ast.BinOp):                ops = [node.op]            elif isinstance(node, ast.UnaryOp):                ops = [node.op]            elif isinstance(node, ast.Compare):                ops = node.ops            elif isinstance(node, ast.BoolOp):                ops = [node.op]                       for op in ops:                if type(op) in operator_map:                    operators.append(operator_map[type(op)])        # 三元运算符标记        if isinstance(node, ast.IfExp):            operators.append('if_else')        # 变量名收集        if isinstance(node, ast.Name):            data_fields.append(node.id)    # 数据字段过滤    exclude_keywords = set(keyword.kwlist) | {'True', 'False', 'None'}    operators_set = set(operators)  # 用于过滤同名字段    valid_data = [        fieldforfieldindata_fields        iffieldnotindefined_vars        and field not in {'nan', 'true', 'false'}        and field not in exclude_keywords        and field not in operators_set    ]    return {        'operators': operators,           # 保留原始顺序和重复        'data_fields': valid_data          # 已过滤无效项但保留重复    }def identify_state(regular):    res = parse_alpha(regular)    return len(set(res['data_fields'])-set(fields)) + len(set(res['operators'])-set(ops))
```

优化后的代码可以检测到里面所有的运算符，运算符数量可以和wq官方给的完全一致。且经过了我之前提交的非一二三阶复杂的alpha表达式的验证。

之后获取自己的ops和fields，以及alpha的regular。由于我是用mongo数据库管理的alpha

所以代码没法照抄，但是可以经过修改移植到自己的体系

```
    group_datafields, datafields = loadAset_data()    fields = set(datafields['id'].tolist() + group_datafields['id'].tolist())    ops = set(cfg.OPS_LIST)    print(f"{len(fields)} fields, {len(ops)} ops")    print(f"查询到的 的alphas数量 {collection.count_documents({})}")    results = list(collection.find({'genius_state':'Old'}, {"_id":1, "alpha_id":1, 'regular':"$sim_data.regular", 'ops': "$info.operatorCount"}))    results = pd.DataFrame(results)    print(f"查询语句Old待更新的 {results.shape}")    results['notcounts'] = results['regular'].parallel_apply(identify_state)    print(f"notcounts的情况 {results['notcounts'].value_counts()}")    results = results.query('notcounts==0')       batch_size = 10000    total_updated = 0    # 获取 _id 列表    id_list = results['_id'].to_list()    # 分批更新    for i in tqdm(range(0, len(id_list), batch_size)):        batch = id_list[i:i + batch_size]        result = collection.update_many(            {'_id': {'$in': batch}},  # 匹配 _id 在当前批次中的文档            {'$set': {'genius_state': 'Current'}}  # 更新 genius_state 和 user_idx        )        total_updated += result.modified_count
```

---

### 帖子 #105: 检测alpha是否可以用于本赛季代码优化
- **主帖链接**: https://support.worldquantbrain.com检测alpha是否可以用于本赛季代码优化_31078279668119.md
- **讨论数**: 1

众所周知，还有几天就定级了，到时候运算符和数据集都会重新随机。那么就会导致库存里的alpha报销。因此，我优化了一下 [顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97)) 的提供的 [ast解析表达式的代码]([L2] 用python ast提取表达式中operator和datafield的方法代码优化_30870358077463.md) ，从而可以用于检测alpha是否可以用于本赛季。

原理，使用ast解析表达式里的ops和fields，和自己可用的进行比较

```
import astimport reimport keyworddef parse_alpha(alpha_expression: str) -> dict[str, list[str]]:    """解析表达式并提取操作符和数据字段。    该函数用于解析输入的表达式字符串，进行预处理、AST解析，并提取其中的操作符和数据字段。    它会过滤掉无效的数据字段（如Python关键字、已定义变量等），并保留操作符的顺序和重复项。    Args:        alpha_expression (str): 输入的表达式字符串。    Returns:        Dict[str, List[str]]: 包含操作符和数据字段的字典。            - 'operators': 提取的操作符列表，保留顺序和重复项。            - 'data_fields': 提取的有效数据字段列表，已过滤无效项。    """    # 运算符预处理    replacements = [        (r'\b(or)\b', 'logical_or'),  # 保护逻辑函数名        (r'\b(and)\b', 'logical_and'),        (r'\&\&', ' and '),          # 转换运算符        (r'\|\|', ' or '),        (r'(?<!\=)\!(?!\=)', ' not '),        (r'\?', ' if '),        (r'\:', ' else '),        (r'\bNaN\b', '0')           # 处理特殊常量    ]    for pattern, repl in replacements:        alpha_expression = re.sub(pattern, repl, alpha_expression)    # 清理注释和字符串    alpha_expression = re.sub(r'(?m)^\s*(//|#).*\n?', '', alpha_expression)    alpha_expression = re.sub(r'"([^"]*)"', "0", alpha_expression)    # 处理和 python 内置逻辑表达式冲突    alpha_expression = re.sub(r'\band\(', 'and_(', alpha_expression)  # 替换 'and('    alpha_expression = re.sub(r'\bor\(', 'or_(', alpha_expression)  # 替换 'or('    # 合并多行没有分号的表达式    lines = alpha_expression.splitlines()    merged_lines = []    temp_line = ""    for line in lines:        stripped_line = line.strip()        if stripped_line and not stripped_line.endswith(';'):  # 如果行不以分号结尾            temp_line += " " + stripped_line  # 合并到上一行        else:            if temp_line:  # 如果存在合并的内容                merged_lines.append(temp_line.strip())  # 添加到结果中            merged_lines.append(stripped_line)  # 添加当前行            temp_line = ""  # 清空临时合并内容    # 如果最后一行没有以分号结尾，确保它被处理    if temp_line:        merged_lines.append(temp_line.strip())    alpha_expression = "\n".join(line.strip() for line in merged_lines)    # 解析AST    tree = ast.parse(alpha_expression)       operator_map = {        ast.Add: 'add', ast.Sub: 'subtract',        ast.Mult: 'multiply', ast.Div: 'divide',        ast.Pow: 'power', ast.USub: 'reverse',        ast.Lt: 'less', ast.Gt: 'greater',        ast.LtE: 'less_equal', ast.GtE: 'greater_equal',        ast.Eq: 'equal', ast.NotEq: 'not_equal',        ast.And: 'and', ast.Or: 'or',        ast.Not: 'not'    }    operators = []  # 改为列表    data_fields = [] # 改为列表    defined_vars = set()    for node in ast.walk(tree):        # 变量定义检测        if isinstance(node, ast.Assign):            for target in node.targets:                if isinstance(target, ast.Name):                    defined_vars.add(target.id)        # 函数调用捕获        if isinstance(node, ast.Call):            if isinstance(node.func, ast.Name):                func_name = node.func.id                # 恢复原始函数名                if func_name.lower() == 'logical_or':                    func_name = 'or'                elif func_name.lower() == 'logical_and':                    func_name = 'and'                operators.append(func_name)            elif isinstance(node.func, ast.Attribute):                operators.append(node.func.attr)        # 运算符捕获        if isinstance(node, (ast.BinOp, ast.UnaryOp, ast.Compare, ast.BoolOp)):            ops = []            if isinstance(node, ast.BinOp):                ops = [node.op]            elif isinstance(node, ast.UnaryOp):                ops = [node.op]            elif isinstance(node, ast.Compare):                ops = node.ops            elif isinstance(node, ast.BoolOp):                ops = [node.op]                       for op in ops:                if type(op) in operator_map:                    operators.append(operator_map[type(op)])        # 三元运算符标记        if isinstance(node, ast.IfExp):            operators.append('if_else')        # 变量名收集        if isinstance(node, ast.Name):            data_fields.append(node.id)    # 数据字段过滤    exclude_keywords = set(keyword.kwlist) | {'True', 'False', 'None'}    operators_set = set(operators)  # 用于过滤同名字段    valid_data = [        fieldforfieldindata_fields        iffieldnotindefined_vars        and field not in {'nan', 'true', 'false'}        and field not in exclude_keywords        and field not in operators_set    ]    return {        'operators': operators,           # 保留原始顺序和重复        'data_fields': valid_data          # 已过滤无效项但保留重复    }def identify_state(regular):    res = parse_alpha(regular)    return len(set(res['data_fields'])-set(fields)) + len(set(res['operators'])-set(ops))
```

优化后的代码可以检测到里面所有的运算符，运算符数量可以和wq官方给的完全一致。且经过了我之前提交的非一二三阶复杂的alpha表达式的验证。

之后获取自己的ops和fields，以及alpha的regular。由于我是用mongo数据库管理的alpha

所以代码没法照抄，但是可以经过修改移植到自己的体系

```
    group_datafields, datafields = loadAset_data()    fields = set(datafields['id'].tolist() + group_datafields['id'].tolist())    ops = set(cfg.OPS_LIST)    print(f"{len(fields)} fields, {len(ops)} ops")    print(f"查询到的 的alphas数量 {collection.count_documents({})}")    results = list(collection.find({'genius_state':'Old'}, {"_id":1, "alpha_id":1, 'regular':"$sim_data.regular", 'ops': "$info.operatorCount"}))    results = pd.DataFrame(results)    print(f"查询语句Old待更新的 {results.shape}")    results['notcounts'] = results['regular'].parallel_apply(identify_state)    print(f"notcounts的情况 {results['notcounts'].value_counts()}")    results = results.query('notcounts==0')       batch_size = 10000    total_updated = 0    # 获取 _id 列表    id_list = results['_id'].to_list()    # 分批更新    for i in tqdm(range(0, len(id_list), batch_size)):        batch = id_list[i:i + batch_size]        result = collection.update_many(            {'_id': {'$in': batch}},  # 匹配 _id 在当前批次中的文档            {'$set': {'genius_state': 'Current'}}  # 更新 genius_state 和 user_idx        )        total_updated += result.modified_count
```

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《1，2，3月value factor更新，国区进步最快的10位顾问经验分享》的评论回复
- **帖子链接**: [Commented] 123月value factor更新国区进步最快的10位顾问经验分享.md
- **评论时间**: 1年前

不会用扣子空间做的网页展示吧，😏

==============================================

---

### 探讨 #2: 关于《1，2，3月value factor更新，国区进步最快的10位顾问经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 123月value factor更新国区进步最快的10位顾问经验分享_32732928355223.md
- **评论时间**: 1年前

不会用扣子空间做的网页展示吧，😏

==============================================

---

### 探讨 #3: 关于《Concept of Simulation Streak (suprising number)》的评论回复
- **帖子链接**: [Commented] Concept of Simulation Streak suprising number.md
- **评论时间**: 1年前

This is because you haven't conducted any simulations this quarter, so the count defaults to 0. You will get a specific number once you perform a simulation.

==================================================================================

---

### 探讨 #4: 关于《Concept of Simulation Streak (suprising number)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Concept of Simulation Streak suprising number_33167520236055.md
- **评论时间**: 1年前

This is because you haven't conducted any simulations this quarter, so the count defaults to 0. You will get a specific number once you perform a simulation.

==================================================================================

---

### 探讨 #5: 关于《Understanding group_zscoreResearch》的评论回复
- **帖子链接**: [Commented] Understanding group_zscoreResearch.md
- **评论时间**: 1年前

Nice post! The explanation of `group_zscore` and its applications is really helpful. I especially like how you combined it with `ts_zscore`—that’s a clever approach for standardizing data across both time and groups. It would be great to see more examples or case studies on implementing this in real-world scenarios, maybe even some challenges that come with using `group_zscore` in practice.

---

### 探讨 #6: 关于《Understanding group_zscoreResearch》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Understanding group_zscoreResearch_25970747246103.md
- **评论时间**: 1年前

Nice post! The explanation of `group_zscore` and its applications is really helpful. I especially like how you combined it with `ts_zscore`—that’s a clever approach for standardizing data across both time and groups. It would be great to see more examples or case studies on implementing this in real-world scenarios, maybe even some challenges that come with using `group_zscore` in practice.

---

### 探讨 #7: 关于《依次添加到总列表中》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】复现2023年因子日历论坛精选.md
- **评论时间**: 1年前

火钳刘明

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================

---

### 探讨 #8: 关于《依次添加到总列表中》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】复现2023年因子日历论坛精选_33049767468055.md
- **评论时间**: 1年前

火钳刘明

==========================================

允许自己接受平常的、无聊的小东西带给你的刹那震撼。 ---安迪·沃霍尔-

==========================================

---

### 探讨 #9: 关于《【Alpha灵感】振幅因子的切割》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】振幅因子的切割.md
- **评论时间**: 2年前

我想问一下如何在brain平台上实现选择收盘价较高的n天的振幅的均值哇

---

### 探讨 #10: 关于《【Alpha灵感】振幅因子的切割》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】振幅因子的切割_19135894021527.md
- **评论时间**: 2年前

我想问一下如何在brain平台上实现选择收盘价较高的n天的振幅的均值哇

---

### 探讨 #11: 关于《【PPAC】比赛中的相关性如何影响Base payment？》的评论回复
- **帖子链接**: [Commented] 【PPAC】比赛中的相关性如何影响Base payment.md
- **评论时间**: 1年前

PPAC的因子，如果你的因子没有过传统的检测，会导致corr=0。如果过了传统检测才会显示corr。

========================================

那么意味着corr=0的有可能在未来不太好，虽然base高。当然这是一些片面想法，毕竟我也交着corr=0的alpha

========================================

个人认为单纯是技术原因导致的

---

### 探讨 #12: 关于《【PPAC】比赛中的相关性如何影响Base payment？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【PPAC】比赛中的相关性如何影响Base payment_31248622176791.md
- **评论时间**: 1年前

PPAC的因子，如果你的因子没有过传统的检测，会导致corr=0。如果过了传统检测才会显示corr。

========================================

那么意味着corr=0的有可能在未来不太好，虽然base高。当然这是一些片面想法，毕竟我也交着corr=0的alpha

========================================

个人认为单纯是技术原因导致的

---

### 探讨 #13: 关于《获得地区信息current_dir = os.getcwd()operator_datafields_dir = os.path.join(current_dir, 'OperatorAndDataFields')datafields_excel_path = os.path.join(operator_datafields_dir, 'datafields_GLB_1_TOP3000.csv')usa_analyst7_datafields = pd.read_csv(datafields_excel_path)usa_analyst7_datafields = usa_analyst7_datafields[    (usa_analyst7_datafields['type'] != 'GROUP')]usa_analyst7_datafields = usa_analyst7_datafields[usa_analyst7_datafields['coverage'] >= 0.5]usa_analyst7_datafields = usa_analyst7_datafields[usa_analyst7_datafields['userCount'] > 2]usa_analyst7_datafields = usa_analyst7_datafields[usa_analyst7_datafields['alphaCount'] > 2]usa_analyst7_datafields.reset_index(drop=True, inplace=True)model = SentenceTransformer('FinLang/finance-embeddings-investopedia')获取所有description内容，去除缺失值descriptions = usa_analyst7_datafields['description'].dropna().tolist()生成所有description的向量description_embeddings = model.encode(descriptions, show_progress_bar=True)保存向量到Semantic_Embeddings_Data文件夹embeddings_dir = os.path.join(current_dir, 'Semantic_Embeddings_Data')os.makedirs(embeddings_dir, exist_ok=True)embeddings_path = os.path.join(embeddings_dir, 'datafields_GLB_1_TOP3000' + '_embeddings.npy')np.save(embeddings_path, description_embeddings)print(f"已保存description_embeddings到 {embeddings_path}")》的评论回复
- **帖子链接**: [Commented] 【全自动搜索字段】语义搜索可用字段代码优化.md
- **评论时间**: 1年前

看这查询貌似是当个单词,如果是两个不想关单词的话,能不能解决哇

---

### 探讨 #14: 关于《获得地区信息current_dir = os.getcwd()operator_datafields_dir = os.path.join(current_dir, 'OperatorAndDataFields')datafields_excel_path = os.path.join(operator_datafields_dir, 'datafields_GLB_1_TOP3000.csv')usa_analyst7_datafields = pd.read_csv(datafields_excel_path)usa_analyst7_datafields = usa_analyst7_datafields[    (usa_analyst7_datafields['type'] != 'GROUP')]usa_analyst7_datafields = usa_analyst7_datafields[usa_analyst7_datafields['coverage'] >= 0.5]usa_analyst7_datafields = usa_analyst7_datafields[usa_analyst7_datafields['userCount'] > 2]usa_analyst7_datafields = usa_analyst7_datafields[usa_analyst7_datafields['alphaCount'] > 2]usa_analyst7_datafields.reset_index(drop=True, inplace=True)model = SentenceTransformer('FinLang/finance-embeddings-investopedia')获取所有description内容，去除缺失值descriptions = usa_analyst7_datafields['description'].dropna().tolist()生成所有description的向量description_embeddings = model.encode(descriptions, show_progress_bar=True)保存向量到Semantic_Embeddings_Data文件夹embeddings_dir = os.path.join(current_dir, 'Semantic_Embeddings_Data')os.makedirs(embeddings_dir, exist_ok=True)embeddings_path = os.path.join(embeddings_dir, 'datafields_GLB_1_TOP3000' + '_embeddings.npy')np.save(embeddings_path, description_embeddings)print(f"已保存description_embeddings到 {embeddings_path}")》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【全自动搜索字段】语义搜索可用字段代码优化_31552800099479.md
- **评论时间**: 1年前

看这查询貌似是当个单词,如果是两个不想关单词的话,能不能解决哇

---

### 探讨 #15: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

2025-02-17

在库里找了一个交了，开始记录历史提交数据，看能不能弄个面向base payment的因子筛选方式🤣

[图片 (图片已丢失)]

---

### 探讨 #16: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

今日交了一个eur alpha，收入3.98。eur给的钱确实比其他区域的多

一个sa，收入6.38，目前sa自动化挖的程序出结果还可以，不过目前主要针对usa，等其他区域交的比较多了也开始弄

---

### 探讨 #17: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

[图片 (图片已丢失)] 3.2号交了3个regular，赚了8，在交比较高fitness的时候也在找高得margin交

super依旧稳定，每天6，基本上都是我现在能交的最高的fitness了，可能得改一下自动程序以增加多样性，不过现在有一堆sa等待这check。。。

[图片 (图片已丢失)]

---

### 探讨 #18: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

3.3号交了一个regular，赚了4，腰斩了，可能是eur交的人多了，而且我这次交的不是atom，corr还比较大

也交了一个super，稳定6

---

### 探讨 #19: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

2025-03-16

ra断粮了，sa正常提交，vf从0.77降到了0.73

正在准备ra的自动调整程序，打算从数据库里筛选出一些corr低，但是差一点的因子，通过自动调整程序调整到可以提交，希望能做到吧

--------------------------------------------------------------------------------------------------------------

Passion

---

### 探讨 #20: 关于《对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values())》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **评论时间**: 1年前

2025-03-17

ra通过自动调整程序提交了一个，sa正常提交

目前自动调整还是在遍历Neutralization和decay，得想想怎么把sign_power之类的纳入其中以应对不同的差一点的因子。

--------------------------------------------------------------------------------------------------------------

---

### 探讨 #21: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025-02-17

在库里找了一个交了，开始记录历史提交数据，看能不能弄个面向base payment的因子筛选方式🤣


> [!NOTE] [图片 OCR 识别内容]
> data.query ( 'type=="SUPER"
> ) .merge(payment [ [ ' datesubmitted
> fee_super' ]],
> On
> datesubmitted
> hoW=
> left
> ). sort_values (
> dateSu
> tpe
> datesubmitted
> themes
> Pyramids
> alphald
> region
> universe
> fitness
> prodCorrelation
> ValueFactor
> fee_super
> SUPER
> 2025-02-11
> 1.0
> 1.0
> AOABalQ
> USA
> TOP3000
> 3.81
> 0.4335
> 0.77
> 4.95
> SUPER
> 2025-02-15
> 1.0
> 1.0
> bbZJgol
> USA
> TOP30O0
> 2.61
> 0.5942
> 0.77
> 3.65
> SUPER
> 2025-02-16
> 1.0
> 1.0
> OLOASYI
> USA
> TOP30O0
> 3.30
> 0.6252
> 0.77
> 3.95
> SUPER
> 2025-02-17
> 1.0
> 1.0
> 3XWBavz
> USA
> TOP3000
> 2.46
> 0.6729
> 0.77
> NaN
> data.query (
> type=="REGULAR"
> merge(payment [ [ ' datesubmitted' _
> fee_
> regular' ]],
> Oh
> datesubmitted
> how=
> left
> ).sort_values (
> de
> tpe
> datesubmitted
> themes
> Pyramids
> alphald
> region
> universe
> fitness
> prodCorrelation
> ValueFactor
> fee_
> regular
> REGULAR
> 2025-02-10
> 1.0
> 1.1
> GdNgqdJ
> USA
> T0P3000
> 1.72
> 0.6953
> 0.77
> 2.75
> REGULAR
> 2025-02-11
> 1.0
> 1.1
> YSezqXG
> USA
> T0P3000
> 1.57
> 0.6934
> 0.77
> 2.93
> REGULAR
> 2025-02-15
> 1.0
> 1.1
> ONPNOqR
> USA
> T0P3000
> 1.42
> 0.4519
> 0.77
> 3.62
> REGULAR
> 2025-02-16
> 1.0
> 1.1
> ANKqaGE
> USA
> TOP3OOO
> 1.69
> 0.6697
> 0.77
> 2.57
> REGULAR
> 2025-02-17
> 1.0
> 1.1
> Qbd8OXW
> USA
> TOP3OOO
> 1.45
> 0.6976
> 0.77
> NaN
> delay
> delay


---

### 探讨 #22: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今日交了一个eur alpha，收入3.98。eur给的钱确实比其他区域的多

一个sa，收入6.38，目前sa自动化挖的程序出结果还可以，不过目前主要针对usa，等其他区域交的比较多了也开始弄

---

### 探讨 #23: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前


> [!NOTE] [图片 OCR 识别内容]
> fee_regular
> type
> author
> dateSubmitted
> themes
> pyramids
> alphald
> region
> universe
> fitness
> delay
> prodCorrelation
> ValueFactor
> 8.07
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-02
> 2.0
> 1.3
> ANZYOWQ
> EUR
> T0P2500
> 1.4
> 0.6909
> 0.77
> 8.07
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-02
> 2.0
> 1.1
> ONVNdmJ
> EUR
> TOP2500
> 1.33
> 0.5933
> 0.77
> 8.07
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-02
> 1.5
> 1.0
> koOgG7P
> EUR
> T0P2500
> 1.87
> 0.6171
> 0.77
 3.2号交了3个regular，赚了8，在交比较高fitness的时候也在找高得margin交

super依旧稳定，每天6，基本上都是我现在能交的最高的fitness了，可能得改一下自动程序以增加多样性，不过现在有一堆sa等待这check。。。


> [!NOTE] [图片 OCR 识别内容]
> SUDer
> type
> author
> dateSubmitted
> themes
> Pyramids
> alphald
> region
> universe
> fitness
> delay
> prodCorrelation
> ValueFactor
> 6.31
> SUPER
> K279256
> 2025-03-02
> 1.0
> 1.0
> WZanLEd
> USA
> T0P3000
> 5.75
> 0.6668
> 0.77
> 5.67
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-01
> 1.0
> KNSGkPp
> USA
> TOP3000
> 5.86
> 0.6736
> 0.77
> 5.86
> SUPER
> K279256
> 2025-02-28
> 1.0
> 1.0
> oLglndz
> USA
> TOP3000
> 5.99
> 0.6738
> 0.77
> 6.38
> SUPER
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-02-27
> 1.0
> 1.0
> OLWXaXl
> USA
> TOP3000
> 6.24
> 0.679
> 0.77
> fee
> 1.0


---

### 探讨 #24: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

3.3号交了一个regular，赚了4，腰斩了，可能是eur交的人多了，而且我这次交的不是atom，corr还比较大

也交了一个super，稳定6

---

### 探讨 #25: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025-03-16

ra断粮了，sa正常提交，vf从0.77降到了0.73

正在准备ra的自动调整程序，打算从数据库里筛选出一些corr低，但是差一点的因子，通过自动调整程序调整到可以提交，希望能做到吧

--------------------------------------------------------------------------------------------------------------

Passion

---

### 探讨 #26: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

2025-03-17

ra通过自动调整程序提交了一个，sa正常提交

目前自动调整还是在遍历Neutralization和decay，得想想怎么把sign_power之类的纳入其中以应对不同的差一点的因子。

--------------------------------------------------------------------------------------------------------------

---

### 探讨 #27: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天是2025-03-25, 一共提交了 5 个alpha

第1个: type=REGULAR,  region=USA, sharpe=1.77, fitness=1.89, turnover=10.75, returns=14.26, drawdown=11.29, margin=26.54

第2个: type=REGULAR,  region=USA, sharpe=1.81, fitness=1.99, turnover=8.05, returns=15.13, drawdown=11.44, margin=37.59

第3个: type=REGULAR,  region=USA, sharpe=2.15, fitness=2.71, turnover=25.44, returns=40.49, drawdown=14.77, margin=31.83

第4个: type=REGULAR,  region=USA, sharpe=2.43, fitness=5.06, turnover=5.56, returns=54.15, drawdown=30.21, margin=194.8

第5个: type=SUPER,  region=USA, sharpe=4.72, fitness=4.47, turnover=19.86, returns=17.83, drawdown=3.15, margin=17.96

--------------------------------------------------------------------------------------------------------------

Passion 冲冲冲！

---

### 探讨 #28: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

改好了PPAC的检验程序，抓取pnl只做本地的self-corr，之后计算提交后会不会提分

也改好了PPAC的自动提交程序，先设置属性，之后提交

--------------------------------------------------------------------------------------------------------------

Passion 冲冲冲！

---

### 探讨 #29: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

[顾问 SZ83096 (Rank 13)](/hc/en-us/profiles/29001331587351-顾问 SZ83096 (Rank 13))  我个人觉得提交之前修改过的alpha虽然base不太好看，但是比赛的话要看OS分数，而提交过的alpha尤其是已经出了OS的alpha，是已经经过检验的alpha，在一定程度上比其他alpha更容易拿到高的OS分数。不过为了兼顾base，可以多提交几个，然后选择一下那个进入Pool。当然也可以找些灵感的alpha，毕竟都是经过检验的alpha了。以上是我的拙见。

--------------------------------------------------------------------------------------------------------------

Passion 冲冲冲！

---

### 探讨 #30: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

推荐大家用数据库跑alpha，把跑完的保存起来，除了可以用于日后的分析，还可以对一些不好的进行微调，已经应对一些情况。比如这次比赛，我从我的数据库里通过条件筛选，可以拿到341736个alpha，而我只需要通过fitness降序或者sharpe降序排列之后，从头到尾一个一个交，就会比较快捷，而不是跑完一批就废掉一批。或者要批量往回取。

--------------------------------------------------------------------------------------------------------------

Passion 冲冲冲！

---

### 探讨 #31: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前


> [!NOTE] [图片 OCR 识别内容]
> fee_regular
> type
> author
> dateSubmitted
> themes
> pyramids
> alphald
> region
> universe
> fitness
> delay
> prodCorrelation
> ValueFactor
> 8.96
> REGULAR
> K279256
> 2025-03-25
> 1.0
> 1.5
> OWnJOEV
> USA
> T0P3000
> 2.71
> 0.3778
> 0.73
> 8.96
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-25
> 1.0
> 1.4
> O8nWN3q
> USA
> T0P3000
> 5.06
> 0.9723
> 0.73
> 8.96
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-25
> 1.0
> 1.3
> OWZ2zan
> USA
> TOP3000
> 1.89
> 1.0
> 0.73
> 8.96
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-25
> 1.0
> 1.3
> PgKaEWW
> USA
> TOP3000
> 1.99
> 0.6955
> 0.73
> 6.72
> REGULAR
> K279256
> 2025-03-26
> 1.0
> 1.1
> WbPjPSp
> USA
> T0P3000
> 1.81
> 0.6194
> 0.73
> 6.72
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-26
> 1.2
> XJOAVZO
> USA
> T0P3000
> 22.55
> 0.9809
> 0.73
> 6.72
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-26
> 1.0
> 1.3
> Gjwmlmy
> USA
> TOP3000
> 1.79
> 0.7722
> 0.73
> 6.72
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-26
> 1.0
> 1.2
> 9WkqIxo
> USA
> TOP3000
> 1.72
> 0.7198
> 0.73
> 1.0


这是这两天交因子的结果图，昨天的base降了，还是得找些低corr的因子交来保证比较高的base，毕竟这比赛已经把提交标准放松，而且pool也可以自选了，得优化一下提交的代码了，为了拿到高base

--------------------------------------------------------------------------------------------------------------

Passion 冲冲冲！

---

### 探讨 #32: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前


> [!NOTE] [图片 OCR 识别内容]
> fee_regular
> type
> author
> dateSubmitted
> themes
> pyramids
> alphald
> region
> universe
> fitness
> delay
> prodCorrelation
> ValueFactor
> 6.63
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-27
> 1.0
> 1.3
> eQWX2bG
> USA
> T0P3000
> 1.6
> 0.0
> 0.73
> 6.63
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-27
> 1.0
> 1.3
> GbwPrwG
> USA
> TOP3000
> 1.61
> 0.6693
> 0.73
> 6.63
> REGULAR
> K279256
> 2025-03-27
> 1.0
> 1.1
> PSeGPvv
> USA
> TOP3000
> 2.1
> 0.65
> 0.73
> 6.63
> REGULAR
> K279256
> 2025-03-27
> 1.0
> 1.1
> GKLRYSP
> USA
> TOP3000
> 1.89
> 0.6783
> 0.73


这是昨天提交的因子，稳定在了6.6. 平台是不是有问题第一个因子我在因子界面做prod corr是0.8，但是在submit的页面却显示0. 我目前打算把pool的self corr降低到0.4来获取更加稳定的因子组合

--------------------------------------------------------------------------------------------------------------

Passion 冲冲冲！

---

### 探讨 #33: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天更新了combined，比上次降低了,但还是在1之上，有大概率能拿到master了。

希望明天定级能定到master

----------------------------------------------------------------------------------------------------------------------------------------------
Passion！！！

---

### 探讨 #34: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

昨天的钱出来了，基本稳定在了7-8美元，没明白为什么有的prod corr是0，但是在alpha页面检查prod的时候又有，是不是有bug了

 
> [!NOTE] [图片 OCR 识别内容]
> fee_regulal type
> author
> dateSubmitted
> themes
> pyramids
> alphald
> region
> universe
> fitness
> delay
> prodCorrelation
> ValueFactor
> 8.25
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-29
> 1.0
> 11
> dKSXSjW
> USA
> TOP3000
> 2.1
> 0.0
> 0.73
> 8.25
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-29
> 1.0
> 1.1
> mYLBWVP
> USA
> TOP3000
> 1.59
> 0.0
> 0.73
> 8.25
> REGULAR
> K279256
> 2025-03-29
> 1.0
> 11
> VORIpwa
> USA
> T0P3000
> 1.65
> 0.73
> 8.25
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-29
> 1.0
> 1.1
> WbOLnwQ
> USA
> T0P3000
> 2.17
> 0.73
> 7.36
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-30
> 1.0
> 11
> 15j7091
> USA
> TOP3000
> 1.47
> 0.73
> 7.36
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-30
> 1.0
> 1.1
> SjbrMGN
> USA
> TOP3000
> 1.48
> 0.8904
> 0.73
> 7.36
> REGULAR
> K279256
> 2025-03-30
> 1.0
> 1.1
> XIGZALb
> USA
> T0P3000
> 2.73
> 0.0
> 0.73
> 7.36
> REGULAR
> 顾问 顾问 KZ79256 (Rank 21) (Rank 21)
> 2025-03-30
> 1.0
> 1.1
> dKXNYS」
> USA
> T0P3000
> 1.93
> 0.9028
> 0.73
 ----------------------------------------------------------------------------------------------------------------------------------------------
Passion！！！

---

### 探讨 #35: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

我从数据库里挑选出以往sharpe比较高的，改了一下maxTrade，之后让他跑，希望能赶上新的theme。2倍加成呢/

不得不说，数据库大法好！！！

----------------------------------------------------------------------------------------------------------------------------------------------
Passion！！！

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

今天突然发现平台吞了运算符了, 本地分析167个运算符都用了, 结果genius显示只用了162个, 还不知道是哪些没用, 哭死, 哇哇哇 
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st 2025
> December 31st 2025
> Operators per Alpha
> Operators UsEC
> Fields per Alpha
> 2.31
> 162
> 1.14
> Fields Used
> Community activity
> Max simulation streak
> 270
> 29.6
> 300
 ============================================================================
=============================== HOPE HIGH Genius===============================
============================================================================

---

### 探讨 #37: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

开始交D0的因子了,昨天交了4个usa 的d0 ppa的因子拿了24🔪. py加成挺大了. 加油跑,这个月把d0的因子交到20个,避免影响vf和combine

============================================================================
=============================== 无限进步 ====================================
============================================================================

---

### 探讨 #38: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

genius分级结束,拿到了梦寐以求的GM, 调整代码和数据, 跑之前没跑的因子

============================================================================
=============================== 冲冲冲 ====================================
============================================================================

---

### 探讨 #39: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

昨天交了4个D0的alpha拿了24.57, 基本年份都是全的,而且有上涨的趋势

============================================================================
=============================== 冲冲冲 ====================================
============================================================================

---

### 探讨 #40: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

======================================================================

重新搭建了一个回测系统,前后端分离, 可以更方便的控制每个回测进程了, 下一步就准备把app里的功能弄成自动化流程到框架里, 希望能在过年弄完把
======================================================================

---

### 探讨 #41: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

======================================================================

OS更新后, pnl获取不了了, 以前的存货直接报废, 太难了

======================================================================

---

### 探讨 #42: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

======================================================================

VF从0.23到了0.9了, 终于把难过的时间熬过了, chn d0就是一个坑, 不要碰

======================================================================

---

### 探讨 #43: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

跑了两天终于跑出了一个EUR的RA, 好难哇, 还有一些可能可以优化为RA的, 抓紧看看能不能弄出个优化程序 
> [!NOTE] [图片 OCR 识别内容]
> ABBregate
> Dat
> TUIMU
> VaruT
> 2.04
> 5.65%
> 1.81
> 9.7996
> 7.2496
> 34.6-
> 9oo
> Sharpe
> Tumower
> T5
> Returns
> Orawdown
> Marmln
> Lon Cont
> 201-
> 13
> 5.135
> 1.5
> 85
> 905
> 29.03
> 1163
> 2015
> 21
> -
> 10.35
> 3.155
> 11-
> 1093
> 2015
> 1.1
> -9
> 7.75
> 5.745
> 702
> 1839
> 2017
> 5.57
> 7.115
> 3.93
> 75.5:
> 1115
> 2013
> 3
> 7.14
> 10.225
> 2339
> 16.9
> _
> 3
> 159
> 1.73
> 1.315
> 1.77
> +5.3-
> 1179
> 2020
> 0.4
> 5.115
> 2.56
> 5.3-5
> 9.71
> 021
> 1
> .355
> 10.5
> 1.33
> 1.33:
> 1158
> 021
> 一
> 342:
> LU
> ~1_.762
> 112
> 202
> 5.53
> 15.883
> 1725
> 56.903
> 1073
> 2023
> 1305
> 1.15
> 33
> 707
> 10.33
> Risk neutralized
> ABaregate Data
> 0.90
> 5.6590
> 0.46
> 3.26%6
> 5.0390
> 11.529600
> Investability constrained
> AEsregate Data
> 1.68
> 3.9790
> 1.34
> 7.9496
> 6.3196
> 40.049600
> 匡 Correlation
> Self Correlation
> TATTTIUITT
> T
> 1| TUTI
> Povier
> Correlation
> TATTTIUITT
> TI
> 11| TUIII
> Prod Correlation
> TATTTIUITT
> TI
> L15PII:AL
> 011917071
> 547 PN
> 0.5828
> 0.5077


----------------------------保证提交质量，提交数量---------------------------------------

---

### 探讨 #44: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

这两天交的sa的prodcorr都做到了小于0.5，平均每天是50刀。似乎prodcorr<0.5并不是很难达到的事。平白无故浪费了之前的机会。

同时发现eur的sa比较好出，机器昨天也跑了一个小于0.5的，但是fitness只有5.05，基本没有加分，遂放弃

--------------------------------------------------------------------------------------------------------

---

### 探讨 #45: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

昨天交了一个SA一个RA

SA是fit>5,corr<0.5的拿了50刀，发现corr<0.5也不是特别难

RA是个ppa的因子拿了5.10，因为corr也低于0.5导致的。

改了改插件代码，方便赛季末的使用

---

### 探讨 #46: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

插件代码更新了一下，更方便的针对性的提升指标

===================不混信号、不过拟合、多样性、稳健性===================

---

### 探讨 #47: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

SA fit>5 corr<0.5可以先用机器跑，很容易就能拿到corr在0.5~0.6的因子，再用signed_power就可以降低到0.5以下。

用这个方法，我这几天基本交的都是corr<0.5的因子

===================不混信号、不过拟合、多样性、稳健性===================

---

### 探讨 #48: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

今天尝试发现，把前两周的SA拿出来改个类别大概率还是一个低corr的SA因子，今天用这个方法一次就成功了。加油，冲

===================不混信号、不过拟合、多样性、稳健性===================

---

### 探讨 #49: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

还是照常1个sa+1个ra, sa拿了51🔪, ra只有2🔪(由于prod corr比较高)

抽空把插件完善了完善, 仔细看了一下数据, 感觉我很多方面还有点薄弱. 首先就是模板的利用上,我现在还是基于123阶的, 抽空改改

===================不混信号、不过拟合、多样性、稳健性===================

---

### 探讨 #50: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

这段时间在想用数据能不能拟合出SAC的评分方式,结果mae有300+, 换换算法, 增加一些数据吧

--------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #51: 关于《【日常生活贴】我的量化日记第六季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

今天终于把aiac的代码跑通了, 准备回测一批数据, 然后组组sa, 不知道能不能赶的上.

不得不说, 好麻烦哇, 要把好多代码从我的代码库里解耦出来

====================================冲冲冲==================================

---

### 探讨 #52: 关于《【有奖】SuperAlpha征文：分享你独到的selection和combination方法！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXurydgx06D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAeJodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzI0NTExMjQzMTI1OTktLSVFNiU5QyU4OSVFNSVBNSU5Ni1TdXBlckFscGhhJUU1JUJFJTgxJUU2JTk2JTg3LSVFNSU4OCU4NiVFNCVCQSVBQiVFNCVCRCVBMCVFNyU4QiVBQyVFNSU4OCVCMCVFNyU5QSU4NHNlbGVjdGlvbiVFNSU5MiU4Q2NvbWJpbmF0aW9uJUU2JTk2JUI5JUU2JUIzJTk1BjsIVDoOc2VhcmNoX2lkSSIpNjk4OTNjYzUtZTAwOS00NzIxLTlkY2ItMTA3NGNjYWM1OGZmBjsIRjoJcmFua2kIOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMS1o3OTI1NgY7CFQ6EnJlc3VsdHNfY291bnRpIg%3D%3D--b53649417fc55c3fa30d22b4a177f02039fa1950
- **评论时间**: 1年前

SETTING：SELCTIONS:(in(classifications, "SIMPLE"))*(in(datacategories, "pv"))上限设的1000，只有764个因子符合COMBO:w1 = combo_a(alpha, nlength = 40, mode = 'algo1');w2 = combo_a(alpha, nlength = 160, mode = 'algo1');w3 = combo_a(alpha, nlength = 252, mode = 'algo1');scale(w1) + scale(w2) + scale(w3)----selection的原因，本身selection比较长，之后由于选不到1000个因子，就等效于上述selection主要是为了选择和量价相关的因子combo的方法设计的原理用于考虑短时combo_a的权重和长时combo_a的组合，借鉴了两个方面之前SA培训的时候把不同的algo进行综合的方式机器学习提取特征时通常会考虑不同时长的特征，来捕捉相应的信息如果直接用combo_a(alpha, nlength = 250, mode = 'algo1')的结果如下用考虑了短时combo_a的权重和长时combo_a的组合的结果如下（0.89是因为我交了一个在此基础上降corr的因子导致的，原始应为0.53左右我在此基础上用了signed_power(scale(w1) + scale(w2) + scale(w3),2)，来降低corr，降到了0.47看来新combo比原来只有一点点提升，区别不大2333 =_=!!, 应该是eur数据的simple类的因子本身是基于eur Top1200, 放在了TOP2500导致的

---

### 探讨 #53: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md
- **评论时间**: 1年前

SETTING：


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
> Instrument Type
> Region
> Universe
> Lanquage
> Decay
> Delay
> Truncation
>  Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> SUR
> TCP250
> Fas- Epression
> 0.01
> Rul
> Verfy


SELCTIONS:

(in(classifications, "SIMPLE"))*(in(datacategories, "pv"))

上限设的1000，只有764个因子符合

COMBO:

w1 = combo_a(alpha, nlength = 40, mode = 'algo1');

w2 = combo_a(alpha, nlength = 160, mode = 'algo1');

w3 = combo_a(alpha, nlength = 252, mode = 'algo1');

scale(w1) + scale(w2) + scale(w3)

----

selection的原因，本身selection比较长，之后由于选不到1000个因子，就等效于上述selection

主要是为了选择和量价相关的因子

combo的方法设计的原理用于考虑短时combo_a的权重和长时combo_a的组合，借鉴了两个方面

- 之前SA培训的时候把不同的algo进行综合的方式
- 机器学习提取特征时通常会考虑不同时长的特征，来捕捉相应的信息

如果直接用combo_a(alpha, nlength = 250, mode = 'algo1')的结果如下


> [!NOTE] [图片 OCR 识别内容]
> C(
> IS Summary
> Period
> TRAIN
> TEST
> Aggregate Data
> Sa「CE
> TUFNOIEI
> FMES
> TC-UTR
> UF3MOWn
> Marein
> 9.67
> 13.459
> 11.71
> 19.7296
> 1.4296
> 29.329600
> Combo Expression
> Year
> Sharpe
> Turnover
> Ftnoss
> Returns
> Orawdown
> Marqin
> LOnO Count
> combo_a(alpha,
> nlength
> 250
> mode
> alBOI
> 2013
> 0.00
> 0.0090
> 0.30
> 0.0050
> 0.00*
> 0.OOK
> Simulation Settings
> 231-
> 14.36
> 13.2935
> 20.32
> 25.5251
> 52兆
> -0.07:
> 1309
> Instrument Type
> Region
> Unmerse
> LangUage
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> 2015
> 12.87
> 13.35
> 17.34
> -.194
> 033*
> 35.33
> 1350
> Equi?i
> EUR
> TOPZSOD
> Fast Expression
> 3.01
> SJM
> 0f
> Verify
> 2015
> 12.56
> 13.9-5
> 17.12
> 25.9130
> 033*
> 6K
> 1352
> 2317
> 13.06
> 14.8755
> 14.31
> 19.3750
> 0.19*
> 25.05
> 1471
> 2013
> 11.32
> 14.965
> 13.24
> 20.453
> 0315
> 27.397
> 1459
> Clone Alpha
> 2019
> 10.5-
> 13.4535
> 12.35
> 13.4750
> 026*
> 27.45:
> 1435
> 2020
> 7.73
> 12.0255
> 19.1151
> 0.73*
> 31.513
> 139-
> 201
> 2
> 11.3750
> -3.54
> 30.82]
> 0.05*
> 5422
> 459
> Hide test period
> Test period and overall stats are hidden by default when test period is specified.
> 2021
> 5.79
> 12.1935
> 5.7
> 12.4051
> 55北
> 20.3-:
> 1459
> 2022
> 3.91
> 12.5395
> 3.47
> 9.375
> 1.42*
> 15.751
> 450
> Chart
> Pnl
> 2023
> 12.16
> 13.5290
> 11.79
> 12.7230
> 0.07沁
> 13.817
> 13361
> Investability constrained
> Aggregate Data
> Sharpe
> TUITnUET
> Timas
> REIICns
> UCadTIIT
> Warain
> 6.84
> 7.66%
> 7.22
> 13.92%
> 1.51%
> 36.349600
> 1SM
> TOM
> 医 Correlation
> 5,0OOK
> Self Correlation
> Waximur
> Winimup
> Last Run:
> Jul'13
> Jan '14
> Jul'14
> Jan '15
> Jul'15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan'13
> Ju1'18
> Jan '19
> Jul'19
> Jan '20
> Jul 20
> Jan 21
> Jul'21
> Jan '22
> Jul 22
> Jan '23
> Prod Correlation
> LIam IF
> Winimum
> C3
> TUn
> Sa-。06/07/2025。11.23 PN
> ComboPnl
> Equal Weight Pnl
> Investability Constrained Pnl
> 0.8526
> -0.5626
> DON
> IS Testing Status
> Period
> TRAIN
> TEST
> 1N
> 寰
> TOk
> 8 PASS
> 罡
> 100
> PENDING
> Alphas
> Selected Alphas
> 764 Alphas Kave been selectEd
> Vew a


用考虑了短时combo_a的权重和长时combo_a的组合的结果如下（0.89是因为我交了一个在此基础上降corr的因子导致的，原始应为0.53左右


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> TRAIN
> TEST
> Sel
> egate Data
> Sh3rO
> LUTTCE
> Fness
> T2tUFII
> UTaWOUF
> Warain
> 10.01
> 14.26%
> 12.30
> 21.5396
> 1.5396
> 30.209600
> CoI
> Year
> Sharpe
> Turnover
> Ftnoss
> Returns
> Drawdown
> Marqin
> LOnO Count
> Short C
> CONbO
> a(alpha, nlength
> mode
> alB01' );
> combo_a(alpha, nlength
> 160,
> mode
> a1801
> 2013
> 11.99
> 13.429
> 1.71
> 23.0350
> 0215
> 34.32
> 311
> Combo_a(alpha,
> nlength
> 252_
> mode
> a1801
> 231-
> 15.73
> 13.5035
> 23.57
> 3.125
> 041*
> 4.51:
> 340
> Scale(WI)
> scale(w2)
> Scale(W3)
> 2015
> 11.73
> 13.909
> 15.45
> 23.3930
> 0.46沁
> 34.517
> 350
> Simulation Settings
> 201
> 1.3
> 14_55
> 17.30
> 27.1530
> 034*
> 33.057
> 1349
> Instrument Type
> Region
> Unmerse
> LangUage
> Decay
> Velay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> 25.993:
> 2317
> 13.45
> 15.9035
> 15.53
> 21.4550
> 021*
> 453
> Equi?i
> EUR
> TOPZSOD
> Fast Expression
> 3.01
> SJM
> 0f
> Verify
> 2013
> 11.26
> 15.3990
> 13.31
> 21.50G5
> 034*
> 27.93
> 456
> 2019
> 10.75
> 13.993
> 12.7
> 19.745
> 23北
> 23.-1:
> 2020
> 12.9155
> 19.5151
> 0.57*
> 3:
> 375
> Clone Alpha
> 201
> 15.79
> 11.9750
> 3.19
> 3.336
> 011
> 55.55-
> 1443
> 2021
> 5.57
> 13.1755
> 5.70
> 13.305
> 0.72*
> 20.193
> 493
> 2022
> 4.09
> 13.5255
> 3.53
> 10.753
> 53北
> 15.793
> 452
> Hide test period
> Test period and overall stats are hidden by default when test period is specified.
> 2023
> 13.565
> 14.8790
> 15.86
> 19.453
> 03
> 25.21
> 1349
> Chart
> Pnl
> Investability constrained
> Aggregate Data
> Sharpe
> TUITNOE
> Tins
> REIICns
> UCadTIIT
> Warain
> 7.12
> 7.7796
> 7.86
> 15.22%
> 1.2796
> 39.199600
> 1SM
> 医 Correlation
> TOM
> Self Correlation
> Waximur
> Winimup
> L3stRun: Sa。06/07/2025。11.06 PW
> 0.8963
> -0.0866
> OOO
> Prod Correlation
> LIam IF
> IinimFT
> 1
> TUn
> 06/07/2025。11.06 Pw
> Jul '13
> Jan '14
> Jul '14
> Jan '15
> Jul'15
> Jan '165
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul'19
> Jan '20
> Jul 20
> Jan  21
> Jul'21
> Jan '22
> Jul 22
> Jan '23
> 0.8963
> -0.5624
> ComboPnl
> Equal Weight Pnl
> Investability Constrained Pnl
> Performance Comparison
> ABBT
> Ssr


我在此基础上用了signed_power(scale(w1) + scale(w2) + scale(w3),2)，来降低corr，降到了0.47

看来新combo比原来只有一点点提升，区别不大2333 =_=!!, 应该是eur数据的simple类的因子本身是基于eur Top1200, 放在了TOP2500导致的

---

### 探讨 #54: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 9个月前

[LK12887](/hc/en-us/profiles/32199366315159-LK12887)  请截图，直接问，我也不知道是啥原因

---------------------------------------------------------------------------------------------------

---

### 探讨 #55: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 9个月前

[YH47265](/hc/en-us/profiles/31706852029335-YH47265)

> 一是默认的参与排名的提交数量设置为40，这个依据是什么呀？改这个感觉排名变化很大。

这个40是初始为了保险由课代表设置的，随后就沿用了。现在你可以参考 HQ17963大佬的 [25Q3顾问提交情况播报（每日更新）]([L2] 25Q3顾问提交情况播报每日更新_33266491538199.md) 文章获取Q3满足的人数，从而调整提交个数

> 二是关于排名规则的，比如有4000人达标参与排名，按照2%的GM人数，有80个名额，但很可能没有这么多达标的GM，比如只有60人达标。剩下20人去参加M的竞争了。但是M本身按8%算是320个名额，空出的20个GM名额会匀给M吗？变成340？

剩下的20人和满足M的人一起竞争M的8%的名额，不存在M名额的变动，以此类推。

因此，不关注六维极有可能满足GM或M的标准，但是最终定级为Gold

---

### 探讨 #56: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 9个月前

[顾问 YH25030 (Rank 31)](/hc/en-us/profiles/28941108652823-顾问 YH25030 (Rank 31))

> 其中排名分析分两步，第一步是抓取数据基本分析，第二步是深度抓取。我理解第一步是六维排名。对于第二步，我没有弄明白具体是什么含义，感觉是剔除一些不活跃的顾问。

第一步抓取的Genius的排行榜，第二步深度抓取的是Consultant排行榜，把二者合并起来，方便查看不同人的WF，VF等信息

---

### 探讨 #57: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 9个月前

[顾问 RM49262 (Rank 30)](/hc/en-us/profiles/32668684211991-顾问 RM49262 (Rank 30))

> 想请问一下，插件中以Expert/Master/Grandmaster为universe的最下面那个total rank是什么意思呢？是指1.signal 2.pyramid 3.performance三选一  这三个条件均满足某个universe标准的人中我六维的综合排名吗？还是其他什么意思呢。谢谢！

total rank是你所有六维的rank的数值加和，用于在Universe里排名

可以通过插件设置页面选择考不考虑performance

---

### 探讨 #58: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 9个月前

[HS55260](/hc/en-us/profiles/29795741334551-HS55260)

> 麻烦问一下例如Exper的总排名，包含M和GM的大佬吗？

Exper的总排名为满足Exper条件所有人的排名，因此包含M和GM。但有可能会出现部分M或GM在Exper的排名可能比你低的情况。

---

### 探讨 #59: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 9个月前

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

> 为什么排名列表和下面具体的不按照combine排名的名次会有差异呢？

没看懂

---

### 探讨 #60: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 8个月前

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

因为计算逻辑不同, 下面的是以每个满足等级需求的为Universe, 进行排序的, 低等级的Universe里包含高等级的人一起排序

上面的是先计算能定级到GM的人, 之后把这部分排除, 再找能定级到M的人, 以此类推

---

### 探讨 #61: 关于《【超精简版】24小时全自动check super alpha的prod corr代码优化》的评论回复
- **帖子链接**: [Commented] 【超精简版】24小时全自动check super alpha的prod corr代码优化.md
- **评论时间**: 10个月前

佬,你的代码怎么复制上来的哇,还有高亮

======================================冲冲冲======================================

---

### 探讨 #62: 关于《【超精简版】24小时全自动check super alpha的prod corr代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【超精简版】24小时全自动check super alpha的prod corr代码优化_33869593860119.md
- **评论时间**: 10个月前

佬,你的代码怎么复制上来的哇,还有高亮

======================================冲冲冲======================================

---

### 探讨 #63: 关于《1. 遍历分页 API，收集所有用户数据import os.pathdef fetch_all_data(s):    offset = 0    limit = 30    all_data = []    while True:        response = s.get(f"{base_url}?limit={limit}&offset={offset}&order%3D-fieldAvg&aggregate=user", )        data = response.json()        if "results" in data:            all_data.extend(data["results"])            offset += limit            print(f"Fetched {offset} records")            if offset >= data["count"]:                break        else:            print("Error fetching data")            break        time.sleep(0)    保存为CSV文件    df = pd.DataFrame(all_data)    df.to_csv("all_users_data.csv", index=False)    print("Data saved to all_users_data.csv")    return df2. 获取自己的用户数据中的leaderboard部分def fetch_self_data(s):    response = s.get("https://api.worldquantbrain.com/users/self/consultant/summary")    self_data = response.json().get("leaderboard", {})    return self_data3. 绘制直方图并高亮自己所在位置def plot_histogram(df, self_data, col):    获取 fieldAvg 数据    field_avg_data = df[col].dropna()    绘制直方图    plt.figure(figsize=(10, 6))    n, bins, patches = plt.hist(field_avg_data, bins=30, color="blue", edgecolor="black", alpha=0.7)    确定自己在哪个柱子中    self_field_avg = self_data.get(col)    for i in range(len(bins) - 1):        if bins[i] <= self_field_avg < bins[i + 1]:            patches[i].set_facecolor("red")            break    图表设置    plt.xlabel(f"{col}")    plt.ylabel("Frequency")    plt.title(f"Distribution of {col} with Self Highlighted")    plt.show()def rank(df, self_data, cols):    计算自己的排名    self_rank = {}    tt_rk = 0    for col in cols:        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            self_val = self_data.get(col)            rank = (df[col] > self_val).sum() + 1            self_rank[col] = str(int(rank))        elif col in ["operatorAvg", "fieldAvg"]:            self_val = self_data.get(col)            rank = (df[col] < self_val).sum() + 1            self_rank[col] = str(int(rank))        tt_rk += rank    self_rank["total_rank"] = tt_rk    return self_rankdef calculate_ranks(df, cols):    创建一个新的DataFrame来存储排名    rank_df = pd.DataFrame(index=df.index, columns=cols)    遍历每一列    for col in cols:        计算排名，对于数值越大越好的列，使用df[col].rank(method='max', ascending=False)        对于数值越小越好的列，使用df[col].rank(method='min', ascending=True)        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=False).apply(lambda x: int(x))        elif col in ["operatorAvg", "fieldAvg"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=True).apply(lambda x: int(x))        del rank_df[col]    rank_df['total_rank'] = rank_df.sum(axis=1)    return rank_dfif __name__ == '__main__':    import json    import time    import numpy as np    import requests    import pandas as pd    import matplotlib.pyplot as plt    pd.set_option('expand_frame_repr', False)    pd.set_option('display.max_rows', 50000)    参数设置    user_id = 'XX12345'  你的ID    username = "user"    password = "password"    mode = 'grandmaster'  'expert', 'master', 'grandmaster'    draw_plots = False  是否画图    print_info = True  是否打印信息    quarter_pay_num = 40  假设满足季度奖励的人需要交满40个    s = requests.Session()    s.auth = (username, password)    response = s.post('https://api.worldquantbrain.com/authentication')    response_content = response.content    response_str = response_content.decode('utf-8')    response_dict = json.loads(response_str)    user_id = response_dict['user']['id']    API的基本信息    base_url = "https://api.worldquantbrain.com/consultant/boards/genius"    执行步骤    if os.path.exists("all_users_data.csv"):        df = pd.read_csv("all_users_data.csv")    else:        df = fetch_all_data(s)    df = fetch_all_data(s)    df.reset_index(drop=True, inplace=True)    self_data = fetch_self_data(s)    self_data = df.loc[df['user']==user_id].to_dict(orient='records')[0]    print(self_data)    if draw_plots:        plot_histogram(df, self_data, "operatorCount")        plot_histogram(df, self_data, "operatorAvg")        plot_histogram(df, self_data, "fieldCount")        plot_histogram(df, self_data, "fieldAvg")        plot_histogram(df, self_data, "communityActivity")        plot_histogram(df, self_data, "completedReferrals")        plot_histogram(df, self_data, "maxSimulationStreak")    再计算一下自己每个标签的百分比排名    my_rank = rank(df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    if print_info:        print("GOLD总人数:", len(df))        print(f"可能满足季度奖金的总人数（交满{quarter_pay_num}个）:", len(df[df['alphaCount']>quarter_pay_num]))        print("以下是你各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")    cols = ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",            "maxSimulationStreak"]    rank_df = calculate_ranks(df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals", 'maxSimulationStreak']],                       on='user', how='left')    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorAvg", "fieldAvg"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    if mode == 'expert':        rank_df = rank_df[rank_df['alphaCount'] >= 20]        rank_df = rank_df[rank_df['pyramidCount'] >= 10]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 0.5) | (rank_df['combinedSelectedAlphaPerformance'] >= 0.5)]    elif mode == 'master':        rank_df = rank_df[rank_df['alphaCount'] >= 120]        rank_df = rank_df[rank_df['pyramidCount'] >= 30]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 1) | (rank_df['combinedSelectedAlphaPerformance'] >= 1)]    elif mode == 'grandmaster':        rank_df = rank_df[rank_df['alphaCount'] >= 220]        rank_df = rank_df[rank_df['pyramidCount'] >= 60]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 2) | (rank_df['combinedSelectedAlphaPerformance'] >= 2)]    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print("|+=+==+=+=以下是按照gold为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print("我的排名:", my_total_rank)        print(f"满足{mode}条件的总人数:", len(rank_df))        if mode == 'grandmaster':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.02))        elif mode == 'master':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.08))        elif mode == 'expert':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.20))        my_alphaCount = self_data.get('alphaCount')        my_pyramidCount = self_data.get('pyramidCount')        my_combinedAlphaPerformance = self_data.get('combinedAlphaPerformance')        my_combinedSelectedAlphaPerformance = self_data.get('combinedSelectedAlphaPerformance')        alphaCount_tag, pyramidCount_tag, combinedAlphaPerformance_tag, total_rank_tag = False, False, False, False        if mode == 'grandmaster':            if my_alphaCount >= 220:                alphaCount_tag = True            if my_pyramidCount >= 60:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 2 or my_combinedSelectedAlphaPerformance >= 2:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'master':            if my_alphaCount >= 120:                alphaCount_tag = True            if my_pyramidCount >= 30:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 1 or my_combinedSelectedAlphaPerformance >= 1:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'expert':            if my_alphaCount >= 20:                alphaCount_tag = True            if my_pyramidCount >= 10:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 0.5 or my_combinedSelectedAlphaPerformance >= 0.5:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        if alphaCount_tag and pyramidCount_tag and combinedAlphaPerformance_tag and total_rank_tag:            print(f"恭喜你大概率可以成为【{mode}】")        else:            if not alphaCount_tag:                print(f"你的alphaCount为{my_alphaCount}, 未达到{mode}标准")            if not pyramidCount_tag:                print(f"你的pyramidCount为{my_pyramidCount}, 未达到{mode}标准")            if not combinedAlphaPerformance_tag:                print(                    f"你的combinedAlphaPerformance为{max(my_combinedAlphaPerformance, my_combinedSelectedAlphaPerformance)}, 未达到{mode}标准")            if not total_rank_tag:                print(f"你的总排名为{my_total_rank}, 未达到{mode}标准")            print("同志还需努力！！！")    rank_df = calculate_ranks(rank_df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance',         "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",         'maxSimulationStreak']],                       on='user', how='left')    再计算一下自己每个标签的百分比排名    my_rank = rank(rank_df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(        lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv(        f'temp/rank相对等级{mode}.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(f"|+=+==+=+=以下是按照{mode}为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print(f"满足{mode}总人数:", len(rank_df))        print(f"以下是你在{mode}池子里的各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")        print(f"以{mode}作为池子的总排名：", my_total_rank)》的评论回复
- **帖子链接**: [Commented] 分享一个超好用的genius排行分析工具代码优化.md
- **评论时间**: 1年前

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)

operatorCount是越大越好，不过课代表的代码把其改成排名，越大排名越小，所以最后是排名越小越好

operatorAvg是指单个alpha里的Operator越少越好

fieldCount也是越大越好，和operatorCount同理

fieldAvg是指单个alpha里的field越少越好

communityActivity：指的是论坛活跃度，别人点赞你的评论或post，你可以增加活跃度，同样也是越大越好

completedReferrals：是完成推荐的人数，越大越好，同理operatorCount

maxSimulationStreak：是指最长的联系回测时间，越大越好，同理operatorCount

建议认真看一下genius的QA。。。

---

### 探讨 #64: 关于《1. 遍历分页 API，收集所有用户数据import os.pathdef fetch_all_data(s):    offset = 0    limit = 30    all_data = []    while True:        response = s.get(f"{base_url}?limit={limit}&offset={offset}&order%3D-fieldAvg&aggregate=user", )        data = response.json()        if "results" in data:            all_data.extend(data["results"])            offset += limit            print(f"Fetched {offset} records")            if offset >= data["count"]:                break        else:            print("Error fetching data")            break        time.sleep(0)    保存为CSV文件    df = pd.DataFrame(all_data)    df.to_csv("all_users_data.csv", index=False)    print("Data saved to all_users_data.csv")    return df2. 获取自己的用户数据中的leaderboard部分def fetch_self_data(s):    response = s.get("https://api.worldquantbrain.com/users/self/consultant/summary")    self_data = response.json().get("leaderboard", {})    return self_data3. 绘制直方图并高亮自己所在位置def plot_histogram(df, self_data, col):    获取 fieldAvg 数据    field_avg_data = df[col].dropna()    绘制直方图    plt.figure(figsize=(10, 6))    n, bins, patches = plt.hist(field_avg_data, bins=30, color="blue", edgecolor="black", alpha=0.7)    确定自己在哪个柱子中    self_field_avg = self_data.get(col)    for i in range(len(bins) - 1):        if bins[i] <= self_field_avg < bins[i + 1]:            patches[i].set_facecolor("red")            break    图表设置    plt.xlabel(f"{col}")    plt.ylabel("Frequency")    plt.title(f"Distribution of {col} with Self Highlighted")    plt.show()def rank(df, self_data, cols):    计算自己的排名    self_rank = {}    tt_rk = 0    for col in cols:        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            self_val = self_data.get(col)            rank = (df[col] > self_val).sum() + 1            self_rank[col] = str(int(rank))        elif col in ["operatorAvg", "fieldAvg"]:            self_val = self_data.get(col)            rank = (df[col] < self_val).sum() + 1            self_rank[col] = str(int(rank))        tt_rk += rank    self_rank["total_rank"] = tt_rk    return self_rankdef calculate_ranks(df, cols):    创建一个新的DataFrame来存储排名    rank_df = pd.DataFrame(index=df.index, columns=cols)    遍历每一列    for col in cols:        计算排名，对于数值越大越好的列，使用df[col].rank(method='max', ascending=False)        对于数值越小越好的列，使用df[col].rank(method='min', ascending=True)        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=False).apply(lambda x: int(x))        elif col in ["operatorAvg", "fieldAvg"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=True).apply(lambda x: int(x))        del rank_df[col]    rank_df['total_rank'] = rank_df.sum(axis=1)    return rank_dfif __name__ == '__main__':    import json    import time    import numpy as np    import requests    import pandas as pd    import matplotlib.pyplot as plt    pd.set_option('expand_frame_repr', False)    pd.set_option('display.max_rows', 50000)    参数设置    user_id = 'XX12345'  你的ID    username = "user"    password = "password"    mode = 'grandmaster'  'expert', 'master', 'grandmaster'    draw_plots = False  是否画图    print_info = True  是否打印信息    quarter_pay_num = 40  假设满足季度奖励的人需要交满40个    s = requests.Session()    s.auth = (username, password)    response = s.post('https://api.worldquantbrain.com/authentication')    response_content = response.content    response_str = response_content.decode('utf-8')    response_dict = json.loads(response_str)    user_id = response_dict['user']['id']    API的基本信息    base_url = "https://api.worldquantbrain.com/consultant/boards/genius"    执行步骤    if os.path.exists("all_users_data.csv"):        df = pd.read_csv("all_users_data.csv")    else:        df = fetch_all_data(s)    df = fetch_all_data(s)    df.reset_index(drop=True, inplace=True)    self_data = fetch_self_data(s)    self_data = df.loc[df['user']==user_id].to_dict(orient='records')[0]    print(self_data)    if draw_plots:        plot_histogram(df, self_data, "operatorCount")        plot_histogram(df, self_data, "operatorAvg")        plot_histogram(df, self_data, "fieldCount")        plot_histogram(df, self_data, "fieldAvg")        plot_histogram(df, self_data, "communityActivity")        plot_histogram(df, self_data, "completedReferrals")        plot_histogram(df, self_data, "maxSimulationStreak")    再计算一下自己每个标签的百分比排名    my_rank = rank(df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    if print_info:        print("GOLD总人数:", len(df))        print(f"可能满足季度奖金的总人数（交满{quarter_pay_num}个）:", len(df[df['alphaCount']>quarter_pay_num]))        print("以下是你各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")    cols = ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",            "maxSimulationStreak"]    rank_df = calculate_ranks(df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals", 'maxSimulationStreak']],                       on='user', how='left')    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorAvg", "fieldAvg"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    if mode == 'expert':        rank_df = rank_df[rank_df['alphaCount'] >= 20]        rank_df = rank_df[rank_df['pyramidCount'] >= 10]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 0.5) | (rank_df['combinedSelectedAlphaPerformance'] >= 0.5)]    elif mode == 'master':        rank_df = rank_df[rank_df['alphaCount'] >= 120]        rank_df = rank_df[rank_df['pyramidCount'] >= 30]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 1) | (rank_df['combinedSelectedAlphaPerformance'] >= 1)]    elif mode == 'grandmaster':        rank_df = rank_df[rank_df['alphaCount'] >= 220]        rank_df = rank_df[rank_df['pyramidCount'] >= 60]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 2) | (rank_df['combinedSelectedAlphaPerformance'] >= 2)]    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print("|+=+==+=+=以下是按照gold为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print("我的排名:", my_total_rank)        print(f"满足{mode}条件的总人数:", len(rank_df))        if mode == 'grandmaster':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.02))        elif mode == 'master':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.08))        elif mode == 'expert':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.20))        my_alphaCount = self_data.get('alphaCount')        my_pyramidCount = self_data.get('pyramidCount')        my_combinedAlphaPerformance = self_data.get('combinedAlphaPerformance')        my_combinedSelectedAlphaPerformance = self_data.get('combinedSelectedAlphaPerformance')        alphaCount_tag, pyramidCount_tag, combinedAlphaPerformance_tag, total_rank_tag = False, False, False, False        if mode == 'grandmaster':            if my_alphaCount >= 220:                alphaCount_tag = True            if my_pyramidCount >= 60:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 2 or my_combinedSelectedAlphaPerformance >= 2:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'master':            if my_alphaCount >= 120:                alphaCount_tag = True            if my_pyramidCount >= 30:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 1 or my_combinedSelectedAlphaPerformance >= 1:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'expert':            if my_alphaCount >= 20:                alphaCount_tag = True            if my_pyramidCount >= 10:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 0.5 or my_combinedSelectedAlphaPerformance >= 0.5:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        if alphaCount_tag and pyramidCount_tag and combinedAlphaPerformance_tag and total_rank_tag:            print(f"恭喜你大概率可以成为【{mode}】")        else:            if not alphaCount_tag:                print(f"你的alphaCount为{my_alphaCount}, 未达到{mode}标准")            if not pyramidCount_tag:                print(f"你的pyramidCount为{my_pyramidCount}, 未达到{mode}标准")            if not combinedAlphaPerformance_tag:                print(                    f"你的combinedAlphaPerformance为{max(my_combinedAlphaPerformance, my_combinedSelectedAlphaPerformance)}, 未达到{mode}标准")            if not total_rank_tag:                print(f"你的总排名为{my_total_rank}, 未达到{mode}标准")            print("同志还需努力！！！")    rank_df = calculate_ranks(rank_df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance',         "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",         'maxSimulationStreak']],                       on='user', how='left')    再计算一下自己每个标签的百分比排名    my_rank = rank(rank_df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(        lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv(        f'temp/rank相对等级{mode}.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(f"|+=+==+=+=以下是按照{mode}为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print(f"满足{mode}总人数:", len(rank_df))        print(f"以下是你在{mode}池子里的各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")        print(f"以{mode}作为池子的总排名：", my_total_rank)》的评论回复
- **帖子链接**: [Commented] 分享一个超好用的genius排行分析工具代码优化.md
- **评论时间**: 1年前

[JH44290](/hc/en-us/profiles/28903565485847-JH44290)  因为新的Q2赛季没有completedReferrals这个维度了，如果你想查看Q1的成绩不如等到明天就公布了，Q2的成绩现在查看没有意义，大家还没把代码debug好。
=========================================================================

---

### 探讨 #65: 关于《1. 遍历分页 API，收集所有用户数据import os.pathdef fetch_all_data(s):    offset = 0    limit = 30    all_data = []    while True:        response = s.get(f"{base_url}?limit={limit}&offset={offset}&order%3D-fieldAvg&aggregate=user", )        data = response.json()        if "results" in data:            all_data.extend(data["results"])            offset += limit            print(f"Fetched {offset} records")            if offset >= data["count"]:                break        else:            print("Error fetching data")            break        time.sleep(0)    保存为CSV文件    df = pd.DataFrame(all_data)    df.to_csv("all_users_data.csv", index=False)    print("Data saved to all_users_data.csv")    return df2. 获取自己的用户数据中的leaderboard部分def fetch_self_data(s):    response = s.get("https://api.worldquantbrain.com/users/self/consultant/summary")    self_data = response.json().get("leaderboard", {})    return self_data3. 绘制直方图并高亮自己所在位置def plot_histogram(df, self_data, col):    获取 fieldAvg 数据    field_avg_data = df[col].dropna()    绘制直方图    plt.figure(figsize=(10, 6))    n, bins, patches = plt.hist(field_avg_data, bins=30, color="blue", edgecolor="black", alpha=0.7)    确定自己在哪个柱子中    self_field_avg = self_data.get(col)    for i in range(len(bins) - 1):        if bins[i] <= self_field_avg < bins[i + 1]:            patches[i].set_facecolor("red")            break    图表设置    plt.xlabel(f"{col}")    plt.ylabel("Frequency")    plt.title(f"Distribution of {col} with Self Highlighted")    plt.show()def rank(df, self_data, cols):    计算自己的排名    self_rank = {}    tt_rk = 0    for col in cols:        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            self_val = self_data.get(col)            rank = (df[col] > self_val).sum() + 1            self_rank[col] = str(int(rank))        elif col in ["operatorAvg", "fieldAvg"]:            self_val = self_data.get(col)            rank = (df[col] < self_val).sum() + 1            self_rank[col] = str(int(rank))        tt_rk += rank    self_rank["total_rank"] = tt_rk    return self_rankdef calculate_ranks(df, cols):    创建一个新的DataFrame来存储排名    rank_df = pd.DataFrame(index=df.index, columns=cols)    遍历每一列    for col in cols:        计算排名，对于数值越大越好的列，使用df[col].rank(method='max', ascending=False)        对于数值越小越好的列，使用df[col].rank(method='min', ascending=True)        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=False).apply(lambda x: int(x))        elif col in ["operatorAvg", "fieldAvg"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=True).apply(lambda x: int(x))        del rank_df[col]    rank_df['total_rank'] = rank_df.sum(axis=1)    return rank_dfif __name__ == '__main__':    import json    import time    import numpy as np    import requests    import pandas as pd    import matplotlib.pyplot as plt    pd.set_option('expand_frame_repr', False)    pd.set_option('display.max_rows', 50000)    参数设置    user_id = 'XX12345'  你的ID    username = "user"    password = "password"    mode = 'grandmaster'  'expert', 'master', 'grandmaster'    draw_plots = False  是否画图    print_info = True  是否打印信息    quarter_pay_num = 40  假设满足季度奖励的人需要交满40个    s = requests.Session()    s.auth = (username, password)    response = s.post('https://api.worldquantbrain.com/authentication')    response_content = response.content    response_str = response_content.decode('utf-8')    response_dict = json.loads(response_str)    user_id = response_dict['user']['id']    API的基本信息    base_url = "https://api.worldquantbrain.com/consultant/boards/genius"    执行步骤    if os.path.exists("all_users_data.csv"):        df = pd.read_csv("all_users_data.csv")    else:        df = fetch_all_data(s)    df = fetch_all_data(s)    df.reset_index(drop=True, inplace=True)    self_data = fetch_self_data(s)    self_data = df.loc[df['user']==user_id].to_dict(orient='records')[0]    print(self_data)    if draw_plots:        plot_histogram(df, self_data, "operatorCount")        plot_histogram(df, self_data, "operatorAvg")        plot_histogram(df, self_data, "fieldCount")        plot_histogram(df, self_data, "fieldAvg")        plot_histogram(df, self_data, "communityActivity")        plot_histogram(df, self_data, "completedReferrals")        plot_histogram(df, self_data, "maxSimulationStreak")    再计算一下自己每个标签的百分比排名    my_rank = rank(df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    if print_info:        print("GOLD总人数:", len(df))        print(f"可能满足季度奖金的总人数（交满{quarter_pay_num}个）:", len(df[df['alphaCount']>quarter_pay_num]))        print("以下是你各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")    cols = ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",            "maxSimulationStreak"]    rank_df = calculate_ranks(df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals", 'maxSimulationStreak']],                       on='user', how='left')    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorAvg", "fieldAvg"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    if mode == 'expert':        rank_df = rank_df[rank_df['alphaCount'] >= 20]        rank_df = rank_df[rank_df['pyramidCount'] >= 10]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 0.5) | (rank_df['combinedSelectedAlphaPerformance'] >= 0.5)]    elif mode == 'master':        rank_df = rank_df[rank_df['alphaCount'] >= 120]        rank_df = rank_df[rank_df['pyramidCount'] >= 30]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 1) | (rank_df['combinedSelectedAlphaPerformance'] >= 1)]    elif mode == 'grandmaster':        rank_df = rank_df[rank_df['alphaCount'] >= 220]        rank_df = rank_df[rank_df['pyramidCount'] >= 60]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 2) | (rank_df['combinedSelectedAlphaPerformance'] >= 2)]    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print("|+=+==+=+=以下是按照gold为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print("我的排名:", my_total_rank)        print(f"满足{mode}条件的总人数:", len(rank_df))        if mode == 'grandmaster':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.02))        elif mode == 'master':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.08))        elif mode == 'expert':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.20))        my_alphaCount = self_data.get('alphaCount')        my_pyramidCount = self_data.get('pyramidCount')        my_combinedAlphaPerformance = self_data.get('combinedAlphaPerformance')        my_combinedSelectedAlphaPerformance = self_data.get('combinedSelectedAlphaPerformance')        alphaCount_tag, pyramidCount_tag, combinedAlphaPerformance_tag, total_rank_tag = False, False, False, False        if mode == 'grandmaster':            if my_alphaCount >= 220:                alphaCount_tag = True            if my_pyramidCount >= 60:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 2 or my_combinedSelectedAlphaPerformance >= 2:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'master':            if my_alphaCount >= 120:                alphaCount_tag = True            if my_pyramidCount >= 30:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 1 or my_combinedSelectedAlphaPerformance >= 1:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'expert':            if my_alphaCount >= 20:                alphaCount_tag = True            if my_pyramidCount >= 10:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 0.5 or my_combinedSelectedAlphaPerformance >= 0.5:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        if alphaCount_tag and pyramidCount_tag and combinedAlphaPerformance_tag and total_rank_tag:            print(f"恭喜你大概率可以成为【{mode}】")        else:            if not alphaCount_tag:                print(f"你的alphaCount为{my_alphaCount}, 未达到{mode}标准")            if not pyramidCount_tag:                print(f"你的pyramidCount为{my_pyramidCount}, 未达到{mode}标准")            if not combinedAlphaPerformance_tag:                print(                    f"你的combinedAlphaPerformance为{max(my_combinedAlphaPerformance, my_combinedSelectedAlphaPerformance)}, 未达到{mode}标准")            if not total_rank_tag:                print(f"你的总排名为{my_total_rank}, 未达到{mode}标准")            print("同志还需努力！！！")    rank_df = calculate_ranks(rank_df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance',         "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",         'maxSimulationStreak']],                       on='user', how='left')    再计算一下自己每个标签的百分比排名    my_rank = rank(rank_df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(        lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv(        f'temp/rank相对等级{mode}.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(f"|+=+==+=+=以下是按照{mode}为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print(f"满足{mode}总人数:", len(rank_df))        print(f"以下是你在{mode}池子里的各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")        print(f"以{mode}作为池子的总排名：", my_total_rank)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 分享一个超好用的genius排行分析工具代码优化_27535685082135.md
- **评论时间**: 1年前

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)

operatorCount是越大越好，不过课代表的代码把其改成排名，越大排名越小，所以最后是排名越小越好

operatorAvg是指单个alpha里的Operator越少越好

fieldCount也是越大越好，和operatorCount同理

fieldAvg是指单个alpha里的field越少越好

communityActivity：指的是论坛活跃度，别人点赞你的评论或post，你可以增加活跃度，同样也是越大越好

completedReferrals：是完成推荐的人数，越大越好，同理operatorCount

maxSimulationStreak：是指最长的联系回测时间，越大越好，同理operatorCount

建议认真看一下genius的QA。。。

---

### 探讨 #66: 关于《1. 遍历分页 API，收集所有用户数据import os.pathdef fetch_all_data(s):    offset = 0    limit = 30    all_data = []    while True:        response = s.get(f"{base_url}?limit={limit}&offset={offset}&order%3D-fieldAvg&aggregate=user", )        data = response.json()        if "results" in data:            all_data.extend(data["results"])            offset += limit            print(f"Fetched {offset} records")            if offset >= data["count"]:                break        else:            print("Error fetching data")            break        time.sleep(0)    保存为CSV文件    df = pd.DataFrame(all_data)    df.to_csv("all_users_data.csv", index=False)    print("Data saved to all_users_data.csv")    return df2. 获取自己的用户数据中的leaderboard部分def fetch_self_data(s):    response = s.get("https://api.worldquantbrain.com/users/self/consultant/summary")    self_data = response.json().get("leaderboard", {})    return self_data3. 绘制直方图并高亮自己所在位置def plot_histogram(df, self_data, col):    获取 fieldAvg 数据    field_avg_data = df[col].dropna()    绘制直方图    plt.figure(figsize=(10, 6))    n, bins, patches = plt.hist(field_avg_data, bins=30, color="blue", edgecolor="black", alpha=0.7)    确定自己在哪个柱子中    self_field_avg = self_data.get(col)    for i in range(len(bins) - 1):        if bins[i] <= self_field_avg < bins[i + 1]:            patches[i].set_facecolor("red")            break    图表设置    plt.xlabel(f"{col}")    plt.ylabel("Frequency")    plt.title(f"Distribution of {col} with Self Highlighted")    plt.show()def rank(df, self_data, cols):    计算自己的排名    self_rank = {}    tt_rk = 0    for col in cols:        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            self_val = self_data.get(col)            rank = (df[col] > self_val).sum() + 1            self_rank[col] = str(int(rank))        elif col in ["operatorAvg", "fieldAvg"]:            self_val = self_data.get(col)            rank = (df[col] < self_val).sum() + 1            self_rank[col] = str(int(rank))        tt_rk += rank    self_rank["total_rank"] = tt_rk    return self_rankdef calculate_ranks(df, cols):    创建一个新的DataFrame来存储排名    rank_df = pd.DataFrame(index=df.index, columns=cols)    遍历每一列    for col in cols:        计算排名，对于数值越大越好的列，使用df[col].rank(method='max', ascending=False)        对于数值越小越好的列，使用df[col].rank(method='min', ascending=True)        if col in ["operatorCount", "fieldCount", "communityActivity", "completedReferrals", "maxSimulationStreak"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=False).apply(lambda x: int(x))        elif col in ["operatorAvg", "fieldAvg"]:            rank_df[f"{col}_rank"] = df[col].rank(method='min', ascending=True).apply(lambda x: int(x))        del rank_df[col]    rank_df['total_rank'] = rank_df.sum(axis=1)    return rank_dfif __name__ == '__main__':    import json    import time    import numpy as np    import requests    import pandas as pd    import matplotlib.pyplot as plt    pd.set_option('expand_frame_repr', False)    pd.set_option('display.max_rows', 50000)    参数设置    user_id = 'XX12345'  你的ID    username = "user"    password = "password"    mode = 'grandmaster'  'expert', 'master', 'grandmaster'    draw_plots = False  是否画图    print_info = True  是否打印信息    quarter_pay_num = 40  假设满足季度奖励的人需要交满40个    s = requests.Session()    s.auth = (username, password)    response = s.post('https://api.worldquantbrain.com/authentication')    response_content = response.content    response_str = response_content.decode('utf-8')    response_dict = json.loads(response_str)    user_id = response_dict['user']['id']    API的基本信息    base_url = "https://api.worldquantbrain.com/consultant/boards/genius"    执行步骤    if os.path.exists("all_users_data.csv"):        df = pd.read_csv("all_users_data.csv")    else:        df = fetch_all_data(s)    df = fetch_all_data(s)    df.reset_index(drop=True, inplace=True)    self_data = fetch_self_data(s)    self_data = df.loc[df['user']==user_id].to_dict(orient='records')[0]    print(self_data)    if draw_plots:        plot_histogram(df, self_data, "operatorCount")        plot_histogram(df, self_data, "operatorAvg")        plot_histogram(df, self_data, "fieldCount")        plot_histogram(df, self_data, "fieldAvg")        plot_histogram(df, self_data, "communityActivity")        plot_histogram(df, self_data, "completedReferrals")        plot_histogram(df, self_data, "maxSimulationStreak")    再计算一下自己每个标签的百分比排名    my_rank = rank(df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    if print_info:        print("GOLD总人数:", len(df))        print(f"可能满足季度奖金的总人数（交满{quarter_pay_num}个）:", len(df[df['alphaCount']>quarter_pay_num]))        print("以下是你各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")    cols = ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",            "maxSimulationStreak"]    rank_df = calculate_ranks(df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals", 'maxSimulationStreak']],                       on='user', how='left')    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorAvg", "fieldAvg"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    if mode == 'expert':        rank_df = rank_df[rank_df['alphaCount'] >= 20]        rank_df = rank_df[rank_df['pyramidCount'] >= 10]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 0.5) | (rank_df['combinedSelectedAlphaPerformance'] >= 0.5)]    elif mode == 'master':        rank_df = rank_df[rank_df['alphaCount'] >= 120]        rank_df = rank_df[rank_df['pyramidCount'] >= 30]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 1) | (rank_df['combinedSelectedAlphaPerformance'] >= 1)]    elif mode == 'grandmaster':        rank_df = rank_df[rank_df['alphaCount'] >= 220]        rank_df = rank_df[rank_df['pyramidCount'] >= 60]        rank_df = rank_df[            (rank_df['combinedAlphaPerformance'] >= 2) | (rank_df['combinedSelectedAlphaPerformance'] >= 2)]    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv('temp/rank预计排名（非官方，仅供参考）.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print("|+=+==+=+=以下是按照gold为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print("我的排名:", my_total_rank)        print(f"满足{mode}条件的总人数:", len(rank_df))        if mode == 'grandmaster':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.02))        elif mode == 'master':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.08))        elif mode == 'expert':            print(f'你想成为【{mode}】', "至少要排名在:", threshold := int(len(df[df['alphaCount']>40]) * 0.20))        my_alphaCount = self_data.get('alphaCount')        my_pyramidCount = self_data.get('pyramidCount')        my_combinedAlphaPerformance = self_data.get('combinedAlphaPerformance')        my_combinedSelectedAlphaPerformance = self_data.get('combinedSelectedAlphaPerformance')        alphaCount_tag, pyramidCount_tag, combinedAlphaPerformance_tag, total_rank_tag = False, False, False, False        if mode == 'grandmaster':            if my_alphaCount >= 220:                alphaCount_tag = True            if my_pyramidCount >= 60:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 2 or my_combinedSelectedAlphaPerformance >= 2:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'master':            if my_alphaCount >= 120:                alphaCount_tag = True            if my_pyramidCount >= 30:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 1 or my_combinedSelectedAlphaPerformance >= 1:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        elif mode == 'expert':            if my_alphaCount >= 20:                alphaCount_tag = True            if my_pyramidCount >= 10:                pyramidCount_tag = True            if my_combinedAlphaPerformance >= 0.5 or my_combinedSelectedAlphaPerformance >= 0.5:                combinedAlphaPerformance_tag = True            if my_total_rank < threshold:                total_rank_tag = True        if alphaCount_tag and pyramidCount_tag and combinedAlphaPerformance_tag and total_rank_tag:            print(f"恭喜你大概率可以成为【{mode}】")        else:            if not alphaCount_tag:                print(f"你的alphaCount为{my_alphaCount}, 未达到{mode}标准")            if not pyramidCount_tag:                print(f"你的pyramidCount为{my_pyramidCount}, 未达到{mode}标准")            if not combinedAlphaPerformance_tag:                print(                    f"你的combinedAlphaPerformance为{max(my_combinedAlphaPerformance, my_combinedSelectedAlphaPerformance)}, 未达到{mode}标准")            if not total_rank_tag:                print(f"你的总排名为{my_total_rank}, 未达到{mode}标准")            print("同志还需努力！！！")    rank_df = calculate_ranks(rank_df.set_index('user'), cols)    rank_df = pd.merge(rank_df, df[        ['user', 'alphaCount', 'pyramidCount', 'combinedAlphaPerformance', 'combinedSelectedAlphaPerformance',         "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",         'maxSimulationStreak']],                       on='user', how='left')    再计算一下自己每个标签的百分比排名    my_rank = rank(rank_df, self_data,                   ["operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"])    rank_df['预测排名（不准，以官方为准）'] = rank_df['total_rank'].rank(method='min', ascending=True).apply(        lambda x: int(x))    rank_df[['user', '预测排名（不准，以官方为准）', 'alphaCount', 'pyramidCount', "operatorCount", "operatorAvg", "fieldCount", "fieldAvg", "communityActivity", "completedReferrals",                    "maxSimulationStreak"]].to_csv(        f'temp/rank相对等级{mode}.csv', index=False, encoding='gbk')    my_total_rank = (rank_df['total_rank'] < my_rank['total_rank']).sum()    if print_info:        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(f"|+=+==+=+=以下是按照{mode}为universe计算的排名=+==+=+==+=+|")        print("|+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+=+==+|")        print(user_id)        print(f"满足{mode}总人数:", len(rank_df))        print(f"以下是你在{mode}池子里的各项的排名:")        for k, v in my_rank.items():            print(f"{k}: {v}, 越小越好")        print(f"以{mode}作为池子的总排名：", my_total_rank)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 分享一个超好用的genius排行分析工具代码优化_27535685082135.md
- **评论时间**: 1年前

[JH44290](/hc/en-us/profiles/28903565485847-JH44290)  因为新的Q2赛季没有completedReferrals这个维度了，如果你想查看Q1的成绩不如等到明天就公布了，Q2的成绩现在查看没有意义，大家还没把代码debug好。
=========================================================================

---

### 探讨 #67: 关于《如何遍历，从而不遗漏每一种可能？代码优化》的评论回复
- **帖子链接**: [Commented] 如何遍历从而不遗漏每一种可能代码优化.md
- **评论时间**: 1年前

我想问一下

```
INSTRUMENT_TYPE_LIST = ['EQUITY', 'CRYPTO']
```

中的CRYPTO是新的运算逻辑吗，是更高级的用户可以用的吗

---

### 探讨 #68: 关于《如何遍历，从而不遗漏每一种可能？代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何遍历从而不遗漏每一种可能代码优化_27454625698199.md
- **评论时间**: 1年前

我想问一下

```
INSTRUMENT_TYPE_LIST = ['EQUITY', 'CRYPTO']
```

中的CRYPTO是新的运算逻辑吗，是更高级的用户可以用的吗

---

### 探讨 #69: 关于《按缓存的分数排序》的评论回复
- **帖子链接**: [Commented] 我的Alpha综合得分排序函数迭代之路从算术平均到几何平均经验分享.md
- **评论时间**: 7个月前

[[Commented] 英才候选人计划实训考核Case5__202403期作业提交处_20852222347159.md]([Commented] 英才候选人计划实训考核Case5__202403期作业提交处_20852222347159.md) 

古早有一个课的作业就是开发相应的评价函数, 博主也可以看看, 连接在上面

---

### 探讨 #70: 关于《按缓存的分数排序》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 我的Alpha综合得分排序函数迭代之路从算术平均到几何平均经验分享_35719491683479.md
- **评论时间**: 7个月前

[[Commented] 英才候选人计划实训考核Case5__202403期作业提交处_20852222347159.md]([Commented] 英才候选人计划实训考核Case5__202403期作业提交处_20852222347159.md) 

古早有一个课的作业就是开发相应的评价函数, 博主也可以看看, 连接在上面

---

### 探讨 #71: 关于《本地Self Correlation检查的实现与改进（本地存储，仅增量拉取进一步提升效率，适用Super Alpha）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiXde4f6Bs6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAmYBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzMwNjgzNzgyMDgzOTkxLSVFNiU5QyVBQyVFNSU5QyVCMFNlbGYtQ29ycmVsYXRpb24lRTYlQTMlODAlRTYlOUYlQTUlRTclOUElODQlRTUlQUUlOUUlRTclOEUlQjAlRTQlQjglOEUlRTYlOTQlQjklRTglQkYlOUItJUU2JTlDJUFDJUU1JTlDJUIwJUU1JUFEJTk4JUU1JTgyJUE4LSVFNCVCQiU4NSVFNSVBMiU5RSVFOSU4NyU4RiVFNiU4QiU4OSVFNSU4RiU5NiVFOCVCRiU5QiVFNCVCOCU4MCVFNiVBRCVBNSVFNiU4RiU5MCVFNSU4RCU4NyVFNiU5NSU4OCVFNyU4RSU4Ny0lRTklODAlODIlRTclOTQlQThTdXBlci1BbHBoYQY7CFQ6DnNlYXJjaF9pZEkiKTY5ODkzY2M1LWUwMDktNDcyMS05ZGNiLTEwNzRjY2FjNThmZgY7CEY6CXJhbmtpDjoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDEtaNzkyNTYGOwhUOhJyZXN1bHRzX2NvdW50aSI%3D--2f743131532d3003642123d4068b8dbbc4c79fa0
- **评论时间**: 1年前

self-corr计算的是同一region的结果，目前的代码比较的是所有region的，可能还需要在加上一个判断region的。--------------------------------------------------------------------------------------------------------------Passion

---

### 探讨 #72: 关于《本地Self Correlation检查的实现与改进（本地存储，仅增量拉取进一步提升效率，适用Super Alpha）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiXde4f6Bs6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAmYBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzMwNjgzNzgyMDgzOTkxLSVFNiU5QyVBQyVFNSU5QyVCMFNlbGYtQ29ycmVsYXRpb24lRTYlQTMlODAlRTYlOUYlQTUlRTclOUElODQlRTUlQUUlOUUlRTclOEUlQjAlRTQlQjglOEUlRTYlOTQlQjklRTglQkYlOUItJUU2JTlDJUFDJUU1JTlDJUIwJUU1JUFEJTk4JUU1JTgyJUE4LSVFNCVCQiU4NSVFNSVBMiU5RSVFOSU4NyU4RiVFNiU4QiU4OSVFNSU4RiU5NiVFOCVCRiU5QiVFNCVCOCU4MCVFNiVBRCVBNSVFNiU4RiU5MCVFNSU4RCU4NyVFNiU5NSU4OCVFNyU4RSU4Ny0lRTklODAlODIlRTclOTQlQThTdXBlci1BbHBoYQY7CFQ6DnNlYXJjaF9pZEkiKTY5ODkzY2M1LWUwMDktNDcyMS05ZGNiLTEwNzRjY2FjNThmZgY7CEY6CXJhbmtpDjoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDEtaNzkyNTYGOwhUOhJyZXN1bHRzX2NvdW50aSI%3D--2f743131532d3003642123d4068b8dbbc4c79fa0
- **评论时间**: 1年前

另外，同一region的SA和RA之间也是要检查相关性的。看代码好像只是在RA之间或者SA之间检查，由于get_submitted_all只能返回一种类型的alpha--------------------------------------------------------------------------------------------------------------Passion

---

### 探讨 #73: 关于《本地Self Correlation检查的实现与改进（本地存储，仅增量拉取进一步提升效率，适用Super Alpha）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiXde4f6Bs6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAmYBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzMwNjgzNzgyMDgzOTkxLSVFNiU5QyVBQyVFNSU5QyVCMFNlbGYtQ29ycmVsYXRpb24lRTYlQTMlODAlRTYlOUYlQTUlRTclOUElODQlRTUlQUUlOUUlRTclOEUlQjAlRTQlQjglOEUlRTYlOTQlQjklRTglQkYlOUItJUU2JTlDJUFDJUU1JTlDJUIwJUU1JUFEJTk4JUU1JTgyJUE4LSVFNCVCQiU4NSVFNSVBMiU5RSVFOSU4NyU4RiVFNiU4QiU4OSVFNSU4RiU5NiVFOCVCRiU5QiVFNCVCOCU4MCVFNiVBRCVBNSVFNiU4RiU5MCVFNSU4RCU4NyVFNiU5NSU4OCVFNyU4RSU4Ny0lRTklODAlODIlRTclOTQlQThTdXBlci1BbHBoYQY7CFQ6DnNlYXJjaF9pZEkiKTY5ODkzY2M1LWUwMDktNDcyMS05ZGNiLTEwNzRjY2FjNThmZgY7CEY6CXJhbmtpDjoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDEtaNzkyNTYGOwhUOhJyZXN1bHRzX2NvdW50aSI%3D--2f743131532d3003642123d4068b8dbbc4c79fa0
- **评论时间**: 1年前

MH33574因为是本地计算还是挺快的就没有做进一步的区分个人感觉还是需要区分一下，因为其他区域的alpha的pnl会影响本区域的self-corr，可能导致过高的错估self-corr。并不是快不快的问题

---

### 探讨 #74: 关于《本地Self Correlation检查的实现与改进（本地存储，仅增量拉取进一步提升效率，适用Super Alpha）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 本地Self Correlation检查的实现与改进本地存储仅增量拉取进一步提升效率适用Super Alpha代码优化_30683782083991.md
- **评论时间**: 1 year ago

self-corr计算的是同一region的结果，目前的代码比较的是所有region的，可能还需要在加上一个判断region的。

--------------------------------------------------------------------------------------------------------------

Passion

---

### 探讨 #75: 关于《本地Self Correlation检查的实现与改进（本地存储，仅增量拉取进一步提升效率，适用Super Alpha）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 本地Self Correlation检查的实现与改进本地存储仅增量拉取进一步提升效率适用Super Alpha代码优化_30683782083991.md
- **评论时间**: 1 year ago

另外，同一region的SA和RA之间也是要检查相关性的。看代码好像只是在RA之间或者SA之间检查，由于get_submitted_all只能返回一种类型的alpha

--------------------------------------------------------------------------------------------------------------

Passion

---

### 探讨 #76: 关于《本地Self Correlation检查的实现与改进（本地存储，仅增量拉取进一步提升效率，适用Super Alpha）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 本地Self Correlation检查的实现与改进本地存储仅增量拉取进一步提升效率适用Super Alpha代码优化_30683782083991.md
- **评论时间**: 1 year ago

[MH33574](/hc/en-us/profiles/25669350433175-MH33574)

```
因为是本地计算还是挺快的就没有做进一步的区分
```

个人感觉还是需要区分一下，因为其他区域的alpha的pnl会影响本区域的self-corr，可能导致过高的错估self-corr。并不是快不快的问题

---

### 探讨 #77: 关于《本地存储alpha信息的数据库表设计，附源码代码优化》的评论回复
- **帖子链接**: [Commented] 本地存储alpha信息的数据库表设计附源码代码优化.md
- **评论时间**: 1年前

用mongo的话可以直接存json格式的,不需要预先定义表之类的,比较方便把

=============================================================

---

### 探讨 #78: 关于《本地存储alpha信息的数据库表设计，附源码代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 本地存储alpha信息的数据库表设计附源码代码优化_31570875902103.md
- **评论时间**: 1年前

用mongo的话可以直接存json格式的,不需要预先定义表之类的,比较方便把

=============================================================

---

### 探讨 #79: 关于《求教，这个alpha还能救一下么》的评论回复
- **帖子链接**: [Commented] 求教这个alpha还能救一下么.md
- **评论时间**: 1年前

感觉有点难了，差了一半 ，试试遍历一下中性化？

实在不行就放弃，api搜索alpha快，而且我看好像是iqc的consultant，还没有prod corr，更容易了

巧了，居然是校友🤣🤣

---

### 探讨 #80: 关于《求教，这个alpha还能救一下么》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 求教这个alpha还能救一下么_31017228094615.md
- **评论时间**: 1年前

感觉有点难了，差了一半 ，试试遍历一下中性化？

实在不行就放弃，api搜索alpha快，而且我看好像是iqc的consultant，还没有prod corr，更容易了

巧了，居然是校友🤣🤣

---

### 探讨 #81: 关于《用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享》的评论回复
- **帖子链接**: [Commented] 用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享.md
- **评论时间**: 1年前

虽然Self 不含 Power Pool，但是prod包含Power Pool。所以当一个因子用power pool交了之后，该因子没法通过正常的方式提交（因为prod 不过）

=============================================================

---

### 探讨 #82: 关于《用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享_32272027850775.md
- **评论时间**: 1年前

虽然Self 不含 Power Pool，但是prod包含Power Pool。所以当一个因子用power pool交了之后，该因子没法通过正常的方式提交（因为prod 不过）

=============================================================

---

### 探讨 #83: 关于《**Alpha主机专业**》的评论回复
- **帖子链接**: [Commented] 组装Alpha主机炸毁同事第一代.md
- **评论时间**: 1年前

如果没有数据库,只想批量发回测,我感觉也可以用玩客云,可以运行python,咸鱼市场才二三十,哈哈哈哈,仅供参考,没有测试

---

### 探讨 #84: 关于《**Alpha主机专业**》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 组装Alpha主机炸毁同事第一代_30219424049943.md
- **评论时间**: 1年前

如果没有数据库,只想批量发回测,我感觉也可以用玩客云,可以运行python,咸鱼市场才二三十,哈哈哈哈,仅供参考,没有测试

---

### 探讨 #85: 关于《自动提交Alpha的接口》的评论回复
- **帖子链接**: [Commented] 自动提交Alpha的接口.md
- **评论时间**: 1年前

话说为什么会有两轮提交哇，一个是post一个是get，是要排除什么特殊情况哇

==============================================================================

---

### 探讨 #86: 关于《自动提交Alpha的接口》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 自动提交Alpha的接口_29237419248279.md
- **评论时间**: 1 year ago

话说为什么会有两轮提交哇，一个是post一个是get，是要排除什么特殊情况哇

==============================================================================

---

### 探讨 #87: 关于《Example usage:》的评论回复
- **帖子链接**: [Commented] 英才候选人计划实训考核Case1.md
- **评论时间**: 2年前

1.最近的截图（需包括时间）


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> Achievements
> Status
> 20
> 4%
> 1
> GOOD
> Total Unsubmitted Alphas
> 2,361
> Total Active Alphas
> 67
> @
> BCELLENT
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 2,428
> 15:45
> 2024年1月248
> 星期
> View


2.下周二前的截图（需显示时间）


> [!NOTE] [图片 OCR 识别内容]
> 0
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 98
> 1
> Total Unsubmitted Alphas
> 3,471
> Total Active Alphas
> 67
> GOOD
> EXCELLENT
> SPECTACULAR
> 4
> Total Decommissioned Alphas
> Total Alphas
> 3,538
> 10:48
> 2024年1月288
> 星期日


3.截图显示你的code **连续不停（不可中断，代码需能handle各类报错）** 提交了1000个simulation。请自行考虑，如何print合适的信息，证明已经提交了1000个Alpha.这种技能会使得你的code更加易读，也能帮助你在代码运行时了解其状态。


> [!NOTE] [图片 OCR 识别内容]
> 170
> a11_data
> []
> 171
> for tmp_I
> i
> price_list.id:
> 172
> regular
> 173
> m_minus
> ts_mean ({tmp_I},
> 38)
> ts_mean({tmp_I}, 10);
> 174
> delta
> (ts_max(m_minus, 10) -m_minus ) / (ts_max(m_minus , 18)-ts_min(m_minus ,10) );
> 175
> PCY
> 8.2*deltato. 8*ts_delay (delta,1);
> 176
> signal
> -close /Vwap;
> 177
> trade_When (PCY>ts_delay (PCY,1) ,
> signal,
> -1);
> 11 11II
> 178
> 179
> simulation_data
> Cfg.simulation_data
> 188
> simulation_data[ 'regular' ]
> regular
> 
> 181
> 182
> region
> USA
> 183
> simulation_data[ ' settings ' ][ 'delay' ]
> 184
> simulation_data[ 'settings ' ][ 'decay' ]
> 185
> simulation_data[ ' settings ' ][ 'truncation
> 9.01
> 186
> 187
> for universe
> in cfg.REGION_UNIVERSE:
> 188
> region,
> universe
> universe
> 189
> simulation_data[ 'settings ' ][ 'region
> ]
> 198
> simulation_data[ 'settings ' ] [ 'universe
> ]
> universe
> 191
> for neutralization in cfB
> NEUTRALIZATION[region]
> 192
> simulation_data[ ' settings ' ][ 'neutralization' ]
> neutralization
> 193
> all_data.append (copy . deepcopy
> simulation_data) )
> 194
> 195
> Parallel(n_jobs=lo) (delayed
> corr) (item_data)
> for item_data
> in tqdm(all_data[658+18+119:]) )
> 196
> # for
> item_data
> in tqdm(all_data)
> 197
> print
> get
> corr(item_data))]
> 问题
> 辙出
> 端口
> JUPYTER
> 调试控制台
> SCreen
> 十~
> 0  画
> error_job
> result(self.timeout )
> File
>  /root /miniconda3 /envs /torch/lib /python3 .8/site-packages /joblib /parallel.py'
> line 736, in
> result
> return self
> return
> or_raise(
> File
>  /root /miniconda3 /envs /torch/lib /python3 .8/site-packages /joblib /parallel.Py'
> line 754, in _return_
> or_raise
> raise self
> result
> KeyError:
> alpha
> 0%
> 39/11421 [01:01〈5:88:16,
> 1.58s /
> (tf) root@autodl-container-4d6411b93c-659112ec:~/autodl
> 'worldquant# /root/miniconda3/envs/torch/bin/python /root/autodl
> worldquant/class.Py
> 〈Response [2812>
> 188%
> 18/18[88:32<80:80,
> 3.22s/i]
> 189%
> loLla [ea: 3200.89
> 2GsLitl
> 1%
> 90/11421 [04:82〈18:34:44,
> 3.365/1
> region
> Bet
> Bet
> Bet
> '让]
> tIP
> tIP


4. 总结反思，需包含至少四个方面的反思：代码效率、debug经历、模板适合的数据类型、模板的改进方向。多写不限，字数不少于300字。

- 代码效率: 10线程并行，1.5h模拟了1k+, 由于没有获取FAIL的performance，所以速度上可能比较快
- debug经历: 由于之前用过api调过参，所以直接改的，bug比较少
- 模板：使用的是 【Alpha灵感】基于量价信息的可靠投资信号 里面的模板

```
    m_minus = ts_mean({tmp_1}, 30) - ts_mean({tmp_1}, 10);    delta = (ts_max(m_minus,10)-m_minus)/(ts_max(m_minus,10)-ts_min(m_minus,10));    PCY = 0.2*delta+0.8*ts_delay(delta,1);    signal = -close/vwap;    trade_when(PCY>ts_delay(PCY,1), signal, -1);
```

通过get_datafields(s, instrument_type='EQUITY', region='USA', delay=1, universe='TOP3000', search='price')获取和price相关的数据，然后注意替换里面的tmp_1。由于没有调参，使得部分测试部分指标不达标
 
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.58
> 25.309
> 0.86
> 7.439
> 4.26%
> 5.889600


- 模板的改进方向

可以通过该方法快速确定，部分适宜的字段。然后调整里面的部分参数，使得整体结果走向更好

可以修改signal的组成方式

---

### 探讨 #88: 关于《英才候选人计划实训考核（Case1）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 英才候选人计划实训考核Case1_19831590714135.md
- **评论时间**: 2年前

1.最近的截图（需包括时间）


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> Achievements
> Status
> 20
> 4%
> 1
> GOOD
> Total Unsubmitted Alphas
> 2,361
> Total Active Alphas
> 67
> @
> BCELLENT
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 2,428
> 15:45
> 2024年1月248
> 星期
> View


2.下周二前的截图（需显示时间）


> [!NOTE] [图片 OCR 识别内容]
> 0
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 98
> 1
> Total Unsubmitted Alphas
> 3,471
> Total Active Alphas
> 67
> GOOD
> EXCELLENT
> SPECTACULAR
> 4
> Total Decommissioned Alphas
> Total Alphas
> 3,538
> 10:48
> 2024年1月288
> 星期日


3.截图显示你的code **连续不停（不可中断，代码需能handle各类报错）** 提交了1000个simulation。请自行考虑，如何print合适的信息，证明已经提交了1000个Alpha.这种技能会使得你的code更加易读，也能帮助你在代码运行时了解其状态。


> [!NOTE] [图片 OCR 识别内容]
> 170
> a11_data
> []
> 171
> for tmp_I
> i
> price_list.id:
> 172
> regular
> 173
> m_minus
> ts_mean ({tmp_I},
> 38)
> ts_mean({tmp_I}, 10);
> 174
> delta
> (ts_max(m_minus, 10) -m_minus ) / (ts_max(m_minus , 18)-ts_min(m_minus ,10) );
> 175
> PCY
> 8.2*deltato. 8*ts_delay (delta,1);
> 176
> signal
> -close /Vwap;
> 177
> trade_When (PCY>ts_delay (PCY,1) ,
> signal,
> -1);
> 11 11II
> 178
> 179
> simulation_data
> Cfg.simulation_data
> 188
> simulation_data[ 'regular' ]
> regular
> 
> 181
> 182
> region
> USA
> 183
> simulation_data[ ' settings ' ][ 'delay' ]
> 184
> simulation_data[ 'settings ' ][ 'decay' ]
> 185
> simulation_data[ ' settings ' ][ 'truncation
> 9.01
> 186
> 187
> for universe
> in cfg.REGION_UNIVERSE:
> 188
> region,
> universe
> universe
> 189
> simulation_data[ 'settings ' ][ 'region
> ]
> 198
> simulation_data[ 'settings ' ] [ 'universe
> ]
> universe
> 191
> for neutralization in cfB
> NEUTRALIZATION[region]
> 192
> simulation_data[ ' settings ' ][ 'neutralization' ]
> neutralization
> 193
> all_data.append (copy . deepcopy
> simulation_data) )
> 194
> 195
> Parallel(n_jobs=lo) (delayed
> corr) (item_data)
> for item_data
> in tqdm(all_data[658+18+119:]) )
> 196
> # for
> item_data
> in tqdm(all_data)
> 197
> print
> get
> corr(item_data))]
> 问题
> 辙出
> 端口
> JUPYTER
> 调试控制台
> SCreen
> 十~
> 0  画
> error_job
> result(self.timeout )
> File
>  /root /miniconda3 /envs /torch/lib /python3 .8/site-packages /joblib /parallel.py'
> line 736, in
> result
> return self
> return
> or_raise(
> File
>  /root /miniconda3 /envs /torch/lib /python3 .8/site-packages /joblib /parallel.Py'
> line 754, in _return_
> or_raise
> raise self
> result
> KeyError:
> alpha
> 0%
> 39/11421 [01:01〈5:88:16,
> 1.58s /
> (tf) root@autodl-container-4d6411b93c-659112ec:~/autodl
> 'worldquant# /root/miniconda3/envs/torch/bin/python /root/autodl
> worldquant/class.Py
> 〈Response [2812>
> 188%
> 18/18[88:32<80:80,
> 3.22s/i]
> 189%
> loLla [ea: 3200.89
> 2GsLitl
> 1%
> 90/11421 [04:82〈18:34:44,
> 3.365/1
> region
> Bet
> Bet
> Bet
> '让]
> tIP
> tIP


4. 总结反思，需包含至少四个方面的反思：代码效率、debug经历、模板适合的数据类型、模板的改进方向。多写不限，字数不少于300字。

- 代码效率: 10线程并行，1.5h模拟了1k+, 由于没有获取FAIL的performance，所以速度上可能比较快
- debug经历: 由于之前用过api调过参，所以直接改的，bug比较少
- 模板：使用的是 【Alpha灵感】基于量价信息的可靠投资信号 里面的模板

```
    m_minus = ts_mean({tmp_1}, 30) - ts_mean({tmp_1}, 10);    delta = (ts_max(m_minus,10)-m_minus)/(ts_max(m_minus,10)-ts_min(m_minus,10));    PCY = 0.2*delta+0.8*ts_delay(delta,1);    signal = -close/vwap;    trade_when(PCY>ts_delay(PCY,1), signal, -1);
```

通过get_datafields(s, instrument_type='EQUITY', region='USA', delay=1, universe='TOP3000', search='price')获取和price相关的数据，然后注意替换里面的tmp_1。由于没有调参，使得部分测试部分指标不达标
 
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.58
> 25.309
> 0.86
> 7.439
> 4.26%
> 5.889600


- 模板的改进方向

可以通过该方法快速确定，部分适宜的字段。然后调整里面的部分参数，使得整体结果走向更好

可以修改signal的组成方式

---

### 探讨 #89: 关于《返回Alpha的相反数》的评论回复
- **帖子链接**: [Commented] 英才候选人计划实训考核Case2_总第三期.md
- **评论时间**: 2年前

1. Performance面板截图，目前我的因子在CHN里面很少


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> CHN
> Delay
> alphas
> 809 of CHN)
> Delay1 
>  Delay0


2.找到论文\研报，发布新的一篇《Alpha灵感》文章在 **中文论坛（注意不是顾问论坛）** ， [【Alpha灵感】球队硬币因子构建.md](【Alpha灵感】球队硬币因子构建.md)

（si，写完才发现和alpha灵感里的重了=.=!!!）

3. Template分析

我用了两个template

第一个是在原始的球队硬币因子的基础上更改输入字段，和mean的时间

第二个是将收益率替换为任意信号（如101因子等），通过波动率和换手率反转部分信号

```
day_yield = {signal}day_yield_mean = ts_mean(day_yield, time); # 日间收益率day_yield_std = ts_std_dev(day_yield, time); # 日间波动率factor1 = if_else(normalize(day_yield_std, useStd = false)>0, -day_yield_mean, day_yield_mean);# “日间反转-换手翻转”因子factor2 = if_else(normalize(turnover_rate_delta, useStd = false)>0, -day_yield_mean, day_yield_mean);factor1+factor2
```

4.  **本次作业硬性要求至少成功提交一个Alpha** ，请提供截图。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Search
> Selec
> SeleC
> Selec
> Search
> Selec
> Selec
> anonyIoUS
> Regular
> ACTI
> 02/03/2024 EST
> CHN
> TOP3000
> anonyIoUS
> Regular
> ACTI
> 02/01/2024 EST
> CHN
> TOP3000


5. 总结反思（代码较上次有什么功能提升、debug经历、模板适合的数据类型、模板的改进方向等）

- 代码较上次有什么功能提升：将构造和测试分离，插队和sql存储，之后需要将multi模拟加入进去，进一步加速模拟速度。
- 模板的改进方向：第2个模板还没搜到合适的

---

### 探讨 #90: 关于《返回Alpha的相反数》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 英才候选人计划实训考核Case2_总第三期_19992945218711.md
- **评论时间**: 2年前

1. Performance面板截图，目前我的因子在CHN里面很少


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> CHN
> Delay
> alphas
> 809 of CHN)
> Delay1 
>  Delay0


2.找到论文\研报，发布新的一篇《Alpha灵感》文章在 **中文论坛（注意不是顾问论坛）** ， [【Alpha灵感】球队硬币因子构建_21109320413335.md](【Alpha灵感】球队硬币因子构建_21109320413335.md)

（si，写完才发现和alpha灵感里的重了=.=!!!）

3. Template分析

我用了两个template

第一个是在原始的球队硬币因子的基础上更改输入字段，和mean的时间

第二个是将收益率替换为任意信号（如101因子等），通过波动率和换手率反转部分信号

```
day_yield = {signal}day_yield_mean = ts_mean(day_yield, time); # 日间收益率day_yield_std = ts_std_dev(day_yield, time); # 日间波动率factor1 = if_else(normalize(day_yield_std, useStd = false)>0, -day_yield_mean, day_yield_mean);# “日间反转-换手翻转”因子factor2 = if_else(normalize(turnover_rate_delta, useStd = false)>0, -day_yield_mean, day_yield_mean);factor1+factor2
```

4.  **本次作业硬性要求至少成功提交一个Alpha** ，请提供截图。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Search
> Selec
> SeleC
> Selec
> Search
> Selec
> Selec
> anonyIoUS
> Regular
> ACTI
> 02/03/2024 EST
> CHN
> TOP3000
> anonyIoUS
> Regular
> ACTI
> 02/01/2024 EST
> CHN
> TOP3000


5. 总结反思（代码较上次有什么功能提升、debug经历、模板适合的数据类型、模板的改进方向等）

- 代码较上次有什么功能提升：将构造和测试分离，插队和sql存储，之后需要将multi模拟加入进去，进一步加速模拟速度。
- 模板的改进方向：第2个模板还没搜到合适的

---

### 探讨 #91: 关于《piece_1 = 提纯(B,A,d)piece_2 = 提纯(C,piece_1,d)piece_3 = 分组比较(-piece_2,grouping)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 英才候选人计划实训考核Case4__202401期作业提交处_20565001927063.md
- **评论时间**: 2年前

由于本周忙于其他事情，这次的模板就是基于老师课上讲的模板，换了数据集，加上了vector数据

**1.**

operators分类

d = ['1', '5', '10', '20', '40', '60', '120', '225', '660']

puri = ['ts_regression', 'regression_neut', 'vector_neut', 'group_vector_neut', 'ts_corr', 'ts_co_kurtosis', 'ts_co_skewness']

comp = ['group_neutralize', 'group_normalize', 'group_rank', 'group_scale', 'group_zscore']

grouping = [

'market',

'industry',

'subindustry',

'sector',

'densify(pv13_r2_liquid_min2_sector)',

'densify(pv13_r2_min10_1000_sector)',

'bucket(rank(cap), range="0,1,0.1")',

'bucket(rank(assets), range="0,1,0.1")',

'bucket(rank(beta_last_30_days_spy), range="0,1,0.1")',

]

vec_op = ['vec_avg','vec_min','vec_max','vec_count','vec_norm','vec_sum','vec_range','vec_ir','vec_skewness','vec_kurtosis', 'vec_percentage', 'vec_powersum', 'vec_stddev'] # 'vec_choose', 'vec_percentage',

**2.模板**

vhat=ts_regression(B,A,120); ehat=ts_regression(C,vhat,120); group_neutralize(-ehat,bucket(rank(cap), rang='0,1,0.1'))

在原始的news18数据集上进行GA

新模板

group_neutralize(ts_co_skewness(rp_nip_inverstor,ts_co_skewness(vec_max(nws18_qep),rp_css_ratings,225),225),bucket(rank(beta_last_30_days_spy), range="0,1,0.1"))

具体的优化过程：

1. 确定覆盖率及turnover (data_df.longCount+data_df.shortCount>1000) & (data_df.turnover<0.7)

2. 在1的条件加上sharpe/fitness，几轮

3. 选取表现好的，差别大的alpha，手动调整部分参数（这一部分后续可以尝试使用机器来做）


> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> ACTIVE
> 02/26/2024 EST
> USA
> T0P3000
> anonyIOUS
> Regular
> ACTIVE
> 02/26/2024 EST
> USA
> T0P3000
> anonyIOUS
> Regular
> ACTIVE
> 02/26/2024 EST
> USA
> T0P3000
> anonyIOUS
> Regular
> ACTIVE
> 02/26/2024 EST
> USA
> T0P3000


**3.**

总结与反思：

由于我是在原始的new18数据集上依据GA重新调整模板，因此我觉得GA可以根据筛选条件之类的随机方式，在原始的数据集上生成新的可以提交的alpha

---

### 探讨 #92: 关于《Calculate rolling correlation over a window of two years-400个交易日至500个交易日rolling_correlation = final_df.rolling(window=400).corr()This gives a MultiIndex DataFrame where level 0 is the date and level 1 is the column pair.You can access the correlation for a specific pair like this:Access the correlations for 'value_main' columncorrelation_main = rolling_correlation.xs('value_main', level=1)correlation_main.plot()》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 英才候选人计划实训考核Case5__202403期作业提交处_20852222347159.md
- **评论时间**: 2 years ago

**T**  **ask 1: Fitness Score**  **设定**

我的score分为两部分，一部分针对alpha本身进行衡量，一部分针对alpha提交前后alpha库的变化进行衡量

为了解决OS/IS的问题，我利用课上老师说的蒙特卡洛模拟的思想，随机在打乱时序的每日盈亏数据（pnl.diff()）中选择252*2个数据，构成一条新的pnl曲线后计算相应的sharpe等信息。共随机选择1000次，以获得多次的均值和标准差。

- 针对alpha本身的score

```
Corr = 1.55-self_corr_maxS = sharpe.mean()/sharpe.std()T = max([turnover.mean(),0.125])D = drawdown.mean()*100alpha_base_score = S*Corr/(T*D)
```

Corr中利用1.55来激励自相关系数在0.55之下的alpha；好的alpha应该在随机选择时保持高的sharpe和低的波动，因此用sharpe的信息比率作为S；T和fitness里的一致；D衡量了平均的撤回率

- 针对alpha提交的score

在针对alpha提交的score中，我先通过beforePnL和afterPnL计算出提交过后pnl的变化曲线（即

(diffPnL = afterPnL.diff()-beforePnL.diff())。好的提交alpha应该可以改善pnl曲线，即diffPnL应该有信号。类似的score的定义如下

```
S = sharpe.mean()D = drawdown.mean()*100alpha_compare_score = S/(D)
```

由于根据pnl曲线没办法计算turnover所以没有turnover

- 整体score

```
score = alpha_base_score*alpha_compare_score
```

当score>0时，应该就可以提交

- 还要检验margin的数值

**Task 2: 研究框架和方法**

本次课程学习到的研究框架

通过阅读论文或研报获取alpha ===> 抽象为template，在相近的数据集里搜索alpha ===> 抽象为更一般的template后利用GA在其他数据集里搜索更优的template

缺失部分：之前对于可提交的alpha没有关注提交过后alpha库的影响，没有去做主题

**Task 3: 现有代码的整合**

目前代码可以大致分为几部分

- 根据regular的回测和提取信息程序
- GA的构造程序
- 其他的构造程序（搜索相近数据集里的alpha）
- 数据表征程序
- score程序
- superalpha构造和测试程序

---

### 探讨 #93: 关于《解决网页出现"WorldQuant BRAIN is experiencing some difficulties"导致的回测中断代码优化》的评论回复
- **帖子链接**: [Commented] 解决网页出现WorldQuant BRAIN is experiencing some difficulties导致的回测中断代码优化.md
- **评论时间**: 1年前

mark了，哪天放插件里去😏

==================================================================================

---

### 探讨 #94: 关于《解决网页出现"WorldQuant BRAIN is experiencing some difficulties"导致的回测中断代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 解决网页出现WorldQuant BRAIN is experiencing some difficulties导致的回测中断代码优化_33170238135959.md
- **评论时间**: 1年前

mark了，哪天放插件里去😏

==================================================================================

---
