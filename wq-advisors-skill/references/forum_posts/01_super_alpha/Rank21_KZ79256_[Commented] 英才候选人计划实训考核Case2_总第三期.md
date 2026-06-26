# 英才候选人计划实训考核（Case2）_总第三期

- **链接**: [Commented] 英才候选人计划实训考核Case2_总第三期.md
- **作者**: WL13229
- **发布时间/热度**: 2年前, 得票: 3

## 帖子正文

1. Performance面板截图，选择相关方向的文章

2.找到论文\研报，发布新的一篇《Alpha灵感》文章在 **中文论坛（注意不是顾问论坛）** ，附链接，且 **严禁抄袭，勿与已发布在 [《Alpha灵感》合集中的选题]([L2] 【Alpha灵感启示录】100 从论文到alpha的复现持续更新收录中Pinned论坛精选_19348865150743.md) 重复。**

《Alpha灵感》文章中必须包含的内容

- 核心交易idea是什么？
- 是否找到数据：
- 是否找到Universe: 例如TOP 200, （一般金融论文都会明确说出其适用的股票类型）
- 是否找到Neutralization: Sector (Smart Search)
- 使用什么operator
- 核心Alpha的Expression（可选）
- 绩效（需保证Sharpe至少大于1.3，Fitness至少大于0.6，Turnover低于45%，高于5%；通过PROD相关性测试）

3. Template分析，阐述其抽象后可以提取什么信息，不同条件下的搜索空间可能有多大，有什么独特的操作，适用什么universe,周期等。

4.  **本次作业硬性要求至少成功提交一个Alpha** ，请提供截图。

5. 总结反思（代码较上次有什么功能提升、debug经历、模板适合的数据类型、模板的改进方向等）

---

## 讨论与评论 (75)

### 评论 #1 (作者: WL13229, 时间: 2年前)

**示例：**

1.可以看出，期权数据和分析师数据都用得较少，我选择阅读 [Research paper 53: Textual Sentiment, Option Characteristics, and Stock Return Predictability](../顾问 CC40930 (Rank 95)/[Commented] Research Paper 53 Textual Sentiment Option Characteristics and Stock Return Predictability.md)  
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> CIIC
> Orilldown
> Fundumenllww
> TIor
> Nodddo
> Rlk dJuu
> Wolul Jutu
> Ucro JurJ
> uT41
> Anlistdl
> Optondsto
> Sentlmtni dal


2.《Alpha灵感》文章（仅供示例）： [【Alpha灵感】A股换手率类因子 – WorldQuant BRAIN](../顾问 WX84677 (Rank 69)/[Commented] 【Alpha灵感】A股换手率类因子.md)

3. Template分析

```
residual_of_A = ts_regression(A,B,750);group_rank(-ts_regression(C,residual_of_A,750),densify(pv13_r2_liquid_min5_sector))
```

抽象来看，该模板用B对A进行提纯，将被提纯的部分拿来对C进一步提纯，并在分组排序。该模板认为，最后提纯出来的事情可以对股价有预测效应。该Alpha在长周期中尝试出现了效果，独特的分组可能会提升表现。

4.  
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Show
> OUT Of 1.156
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Unierse
> Delay
> Sharpe
> Returns
> Turnover
> Search
> Selecr
> Selecr
> Selecr
> Search
> Selecr
> Selecr
> Selecr
> 2.吕>1
> 2.吕>1
> 2.吕>1
> Selecr
> 苫
> 50.542230.7_。
> Resular
> ACTIVE
> 12/19/2023 EST
> US
> T0PZOO
> Tag


5.总结反思

---

### 评论 #2 (作者: KJ42842, 时间: 2年前)

每周四晚8pm-9pm设有与课程相配套的Office Hour，欢迎对课上以及作业内容有疑问的同学参加，注册 [链接](https://worldquant.zoom.us/meeting/register/tJctcu-pqjwuGNcf2F-ukY3hUqWrliPiKhZc)

Note: Office Hour不要求全程参加，解答完问题的同学根据自己时间安排自行下线即可。

---

### 评论 #3 (作者: YW93864, 时间: 2年前)

大家好，这是我本周的交付内容，本周提交3个alpha，复现并优化得到两个，抽象化得到一个。

**1. Performance面板**  
> [!NOTE] [图片 OCR 识别内容]
> US
> 314ph3
> (g0Lolull Nphl



> [!NOTE] [图片 OCR 识别内容]
> Vel 0a
> Furdm I 4


我的alpha在USA比较多，而CHN非常少。因此本周我还是以CHN为主。考虑到之前所有量化相关经历，都没有做过分析师相关的alpha，所以本周以分析师alpha为主。

**2. 【Alpha灵感】**

**链接为： [【Alpha灵感】分析师的“真知灼见” – WorldQuant BRAIN]([L2] 【Alpha灵感】分析师的真知灼见_20089517507735.md)**

**3. Template抽象化**

首先简述一下，具象复现出来的因子：大致逻辑是从分析师预期中，剥离动量因素的影响，这个因素是来自于内幕交易的，既有长期也有短期。主要是先选取一种分析师数据，再定义长期动量和短期动量因子，分别做截面回归进行剥离，从而发现那些预期变化大而涨跌幅小（没有被提前内幕交易）的股票。

一级抽象：将原有的一致预期净利润替换为相同数据集下的预期数据，此处是other41。Brain还有好多CHN分析师数据，还在尝试。在使用api不断simulate后，发现该数据集也只有净利润相关的三个字段比较好，说明模板具有一定特异性。这里我先后提交了两个，一个是PAFR，另一个是预期惯性因子，详情可移步前文链接，这一部分的绩效在该文章中有展示，两个因子虽然隶属同一数据源且构造算法90%相似，但最后相关性较低。

二级抽象：核心思路是假设分析师的一致预期准确，现在有一家A公司的预期层面有重大变化，但有可能被内幕交易消化掉，因此我们需要找到那些有预期层面有明显变化的，而内幕交易者关注不到的股票。 **防止微观变动影响到中观层面判断。** 微观层面可以进一步用技术指标刻画，除了截面上剥离它，还可以从时序上剥离。

1）那么我这里做的处理是找了另一个有分析师数据的数据集，求算过去一段时间内的均值，再对一些技术指标进行时序回归取残差，效果非常好。当然model216的分析师数据本身就有非常明显的信号，只是容易出现robust universe检测不达标的情况，不过大部分只差一点，在不断simulation后，有两个可以直接提交的，有几个在微调参数后，也能提交，但参数比较极端。总之，整体上还是有稳健的。


> [!NOTE] [图片 OCR 识别内容]
> 4,00OK
> 3,00OK
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



> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Highest Correlation
> 0.306
> Prod Correlation
> Highest Correlation
> 0.7


prod corr高可能是技术指标用的比较多导致的，但处于0.6-0.7之间，最后也通过了测试。

**4. 提交截图**


> [!NOTE] [图片 OCR 识别内容]
> MachineAlpha4
> Regular
> ACTIVE
> 12/24/2023 EST
> CHN
> T0P3000
> MachineAlpha3
> Regular
> ACTIVE
> 12/24/2023 EST
> CHN
> T0P2000
> MachineAlphaz
> Regular
> ACTIVE
> 12/23/2023 EST
> CHN
> TOP2000


**5. 反思**

工程上：本周找了先前提交的simulation丢失现象，发现是因为同一个表达式重复回测的问题。然后平台似乎会先查找有没有测过这个alpha，如果测过完全一样的，则返回之前的alpha_id，如果没有，再开始回测。另外。本周把requests的status_code了解了一下，优化了提交错误表达式无法向我报错的问题。

研究上：本周主要挖掘了分析师alpha，但分析师alpha其实在样本外2021年后至今，有因为市场风格切换的失效问题。我觉得后续优化思路是，1）再尝试分析师数据和不同的数据的组合，依靠其他数据的稳健性叠加分析师数据的强信号；2）寻找不同的分组，剥离市场风格的影响，我这次提交的一个因子还是会受到2015年的影响，暂时没有找到处理这个问题地良好方法，但也不想过拟合2015年，所以提交了，但后续还需要进一步思考如何避免风格切换的风险

问题：1）我在本次测试中获得了很多有潜力的因子，部分只是相差及格标准0.01-0.05不等因而不能提交，部分是因为提交了一个，导致其余相关性变高无法提交。请问老师或者同学对于这些剩余的因子有没有好的处理方法，如何进一步利用它们？

---

### 评论 #4 (作者: YH69102, 时间: 2年前)

1.可以看出，Price volume data和 analysis data都用的较少。选择阅读：东方证券-因子选股系列之九十四：UMR2.0，风险溢价视角下的动量反转统一框架再升级。


> [!NOTE] [图片 OCR 识别内容]
> Click to drill down
> Alphas
> CHN
> Delay 1
> Fundamental ata
> Prlice volume data
> Model data


2.《Alpha灵感》文章： [[L2] 【Alpha灵感】UMR20风险溢价视角下的动量反转统一框架_20088908680087.md?page=1#community_comment_20089744914199]([L2] 【Alpha灵感】UMR20风险溢价视角下的动量反转统一框架_20088908680087.md?page=1#community_comment_20089744914199)

3.3. Template分析：

```
risk = ts_mean(R,20) - R;f = ts_sum(risk * A,20);
```

抽象来看本文旨在通过寻求一种风险的度量手段R,来描述当日的风险水平。进而通过一个统一的公式自动选择动量还是反转。R 的可选范围有turnover,volatility of volume or price.

A则是对股票收益的估计(原文中使用 returns - index_returns),可以替换为其他内容。

用rank(f) 或者 -ts_regression(returns,f,d)作为最终的alpha.

4.

在不同的市场下测试，发现在CHN和GLB都能找到alpha 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Show
> 10
> out of 42
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
> Select
> Select
> Search
> Select
> Select
> @.8>1
> @.8>1
> e.8>1
> Select
> UMR of GLB
> Regular
> ACTIVE
> 12/24/2023 EST
> GLB
> TOP3000
> UMR
> Regular
> ACTIVE
> 12/24/2023 EST
> CHN
> T0P2000
> Tag


5. 总结反思（代码较上次有什么功能提升、debug经历、模板适合的数据类型、模板的改进方向等）

代码：

把原来需要一次做完所有simulation后再返回结果的，改为了每隔一定次数将所用datafields、alpha_id保存至excel文件，方便于之后的筛选。

模版适合的数据集:

主要考虑固定A后，筛选R。在GLB下将search设置为volatility、coverage>80%。发现有近3000个数据集且分散在很多种dataset中. 然后发现直接搜risk可以缩小很多范围。

模版改进方向：

可以将ts_sum改为ts_decay_exp_window 或者 在计算Risk时 考虑引入论文中提到的特殊日子（在CHN上没提升，说不定其他市场适用）。

---

### 评论 #5 (作者: YL93001, 时间: 2年前)

1、我的面板中各类数据的alpha都比较少，我选择了东吴金工的《 **信息分布均匀度，基于高频波动率的选股因子** 》


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> Alphas
> CHN
> Delay
> Other
> Fundamental data
> Price volume data
> Model data


2、文章链接： [【Alpha灵感】信息分布均匀度，基于高频波动率的选股因子 – WorldQuant BRAIN]([L2] 【Alpha灵感】信息分布均匀度基于高频波动率的选股因子_20073476508055.md?page=1#community_comment_20100077495191)

3、模板本质上提取了一个数据的标准差除以一个数据的均值，我们可以称之为某个数据的均匀度，对于波动率的信息，经过试验在短周期的效果比较好，我试验了波动率的大约5000个数据，可以提交的alpha数量在20-30个左右；对于其他类型的数据，可以根据数据的特性选择相应的周期，对数据作上述的均匀化处理，可能也会有比较好的效果。

4、alpha提交截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Show
> 10
> out of 30
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
> Select
> Select
> Search
> Select
> Select
> e.吕>1
> e.吕>1
> e.吕>1
> Select
> turnovertvoltality
> Regular
> ACTIVE
> 12/22/2023 EST
> CHN
> T0P3000
> voltality
> Regular 
> ACTIVE
> 12/20/2023 EST
> CHN
> T0P3000
> Tag


5、总结反思：本次我对ace的代码进行了重构与重写，简化了许多步骤，也使自己的代码结构更清晰。在代码效率方面来讲，相比于一次跑5000个simulate，个人认为像在需要短时间内产出结果的project中，1000个左右跑一次可能效率更高一些，一方面simulate时间变短，得到1000个结果后就可以对其中的结果进行分析，同时电脑再跑下1000个alpha。关于本次的均匀度模板，我认为对量价类数据都可以进行尝试，可能会得到一些不错的结果。

---

### 评论 #6 (作者: JL23162, 时间: 2年前)

1.我的面板情况如下


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> CHN
> WA
> GLB



> [!NOTE] [图片 OCR 识别内容]
> PreVloUs perlod
> |070112023
> 11/15/2023
> 0591.00
> Yearto date
> 11/13/2023
> 12/24/2023
> US$6.11
> Total
> 11/13/2023
> 12/24/2023
> 05$6.11
> Distribution of Active Alphas
> Click to drill down
> Alphas
> CLB
> Delay
> Model data
> alphas
> (6796 of GLB Delay 1)
> No limits for data categories with <30 Alphas_
> Model data


因此选择GLB方面的MODEL data算是涉及一个全新的领域

2.文章链接 [[L2] 【Alpha灵感】在GLB Universe实现基于草木皆兵逻辑构建alpha_20101484394903.md]([L2] 【Alpha灵感】在GLB Universe实现基于草木皆兵逻辑构建alpha_20101484394903.md)

3.使用的模板在alpha灵感中 继续修改了均值与异常值的定义标准 使用了新的operator

随后在仅57个（精心挑选）的数据中挖出了5个alpha

4.alpha提交截图


> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> ACTIVE
> 12/20/2023 EST 
> GLB
> MINVOLIM
> 2.19
> 10.09%6
> 37.139
> anonymous
> Regular
> ACTIVE
> 12/20/2023 EST
> GLB
> MINVOLIM
> 1.99
> 9.28%
> 24.649
> anonymous
> Regular
> ACTIVE
> 12/20/2023 EST
> GLB
> MINVOLIM
> 2.65
> 11.76%
> 34.880
> anonymous
> Regular
> ACTIVE
> 12/20/2023 EST
> GLB
> MINVOLIM
> .93
> 11.76%
> 42.650
> anonymous
> Regular
> ACTIVE
> 12/20/2023 EST
> GLB
> MINVOLIM
> 2.14
> 9.40%
> 29.220


5.总结反思

总的来讲 一个优秀的模板 远比大批量的回测方便，如果有优秀的先验知识，那么产出的alpha也会比较容易，上面这里的57个数据 实际上是归属于同一个数据集Growth Valuation Model 在代码方面现在比较依赖先验知识的输入 现在做的确实是human+machine 但是不能纯挂机，我个人是比较偏向于做GA那种可以挂在服务器上每天挖4个因子的，总的来说，课程帮助很大，不仅是对于worldquant这个平台的因子挖掘，实际上在实盘操作中，这些知识也是可以迁移使用的，不过对于alpha的报酬我仍有疑问，我这里一天提交了4个alpha并且是GLB的乘五倍积分，实际上，只收获了4.11u，感觉收益较低

---

### 评论 #7 (作者: WL13229, 时间: 2年前)

[JL23162](/hc/en-us/profiles/18456131969431-JL23162)

这位同学的作业做得很漂亮。有几点感受可以跟您分享。

1. 纯挂机的，我们未来会有课程继续分享，欢迎您持续参与本计划。

2. 您提到知识的迁移使用，这个确实是非常重要的，这个也会是同学们参与此计划的主要收获之一。

3. 关于收入，我看到您的Alpha总数并不多。收入会在您有一个季度的持续表现（即20个不同自然日都有Alpha提交）之后有明显改变。届时，如果您可以获得比0.5更高的value factor score，相信您的收入会比目前明显增加。总而言之，BRAIN系统需要您有一定活跃的历史，才能给您合理地计算并赋值。另外，可以参考这篇文章👉 **[如何提高研究顾问收入]([L2] 如何提高研究顾问收入_19382864029079.md)**

---

### 评论 #8 (作者: BX78946, 时间: 2年前)

1. Performance面板截图 
> [!NOTE] [Pasted Graphic.png OCR 识别内容]
> Fundamentaldata
> Price Volume data
> News data
> Modeldata
> Risk ata
> Optio.
> Social media data


红色部分是USA的news data和fundamental data，这次我选择了CHN市场的price volume data。

2. alpha灵感帖子链接 [[L2] 【Alpha灵感】上下影线蜡烛好还是威廉好_20090584979479.md灵感-上下影线-蜡烛好还是威廉好-]([L2] 【Alpha灵感】上下影线蜡烛好还是威廉好_20090584979479.md)

3. 这个template原本的含义是通过分析市场参与者的心理状态来找到投资策略，例如如果股票在某段上涨行情中出现了较长的上影线，则我们往往认为该股当前的卖压较大，空头势力占优，上涨行情即将结束。而所提到的蜡烛和威廉的区别只在于衡量的标准是开盘价和收盘价的极值还是只看收盘价。这个策略也算是一个典型的reversion的策略。最后ubl用的zscore我感觉是为了标准化蜡烛上影线和威廉下影线，使得他们是同一个量纲，可以直接进行加法的操作，用其他的cross sectional operator应该也是可以的。原本我以为这个用了很经典的量价的datafield是通不过prod_corr测试的，没想到只是复现了原本研报的idea的alpha就可以直接提交。


> [!NOTE] [Pasted Graphic 2.png OCR 识别内容]
> Chart
> Pnl
> 15M
> 12.5M
> 10M
> 7,50OK
> 5,00OK
> 2,5OOK
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


这是提交后的corr的测试，提交之前忘了截图了


> [!NOTE] [Pasted Graphic 3.png OCR 识别内容]
> Correlation
> Self Correlation
> Highest Correlation
> Last Run: Mon, 12/25/2023,10:29 AM
> 0.594
> 名字
> Universe
> Correlation
> Sharpe
> Returns
> Turnover
> Fitness
> Margin
> anonymous (current)
> T0P3000
> 1.00
> 2.75
> 19.35%
> 23.55%
> 2.49
> 16.43%。。
> anonymous
> TOP3000
> 0.59
> 2.13
> 9.359
> 11.76%
> 1.84
> 15.899o。
> anonymous
> TOP3000
> 0.37
> 3.43
> 19.679
> 39.599
> 2.42
> 9.949o。
> anonymous
> TOP3000
> 0.35
> 3.02
> 13.899
> 13.15%
> 3.10
> 21.1390。
> anonymous
> TOP3000
> 0.27
> 2.76
> 18.509
> 23.849
> 2.43
> 15.51%oo
> anonymous
> TOP3000
> 0.23
> 2.72
> 16.839
> 19.46%
> 2.53
> 17.309o。
> Prod Correlation
> Highest Correlation
> Last Run: Mon, 12/25/2023,10:29 AM
> 0.7
> I0Ok


这里原本的蜡烛上影线和威廉下影线的定义是：

```
candle_up = high - max(open, close); William_down = close - low;
```

抽象来看的话，主要是先得到一个变化度，再对这个变化度进行reversion操作。这里的变量很多，我的选择是舍弃掉了open 和 close，把这两个影线都规定成 (high - low)/2，然后分别对high，low进行搜索，要是遇到了vector的话，high就用vec_max，low就用vec_min。但是这样的话其实和原本的影线的定义不是特别相符。当然也可以固定住high，low，然后搜索open，close。这里我纠结的一点就是，原本的这四个data filed都是针对与股票的，相互加减都有意义。要是我固定某两个值，去搜索其他的，很大可能他们之间互相的加减没有经济学的含义。不知道有没有什么方法可以解决这个问题。

4. 后来根据上面的抽象后的模版用api进行模拟，这次还是只得到了很多过不了correlation的alpha。感觉可能是因为，尽管这个idea的表达式看起来很多，但是核心思想还只是得到高位和低位之间的变化度，这个idea的泛化性太强了，导致类似的idea很多。还有可能就是我这种搜索并没有用到很好的先验知识，感觉盲目的直接搜索还是不太好。


> [!NOTE] [Pasted Graphic 4.png OCR 识别内容]
> Select
> Name
> ^
> Competition
> Type
> Status
> Date Created
> Region
> Universe
> Sharpe
> Returns
> Turnover ~Color
> Tag
> Columns
> (EST)
> Search
> Select
> Select
> Select
> Search
> Select
> Select
> e.8〉1
> e8〉1
> e8>1
> Select
> Select
> anonymous
> Regular
> ACTIVE
> 12/24/2023 EST
> CHN
> TOP3000
> anonymoUs
> Regular
> ACTIVE
> 12/23/2023 EST
> CHN
> TOP3000


5. 本来这次我是想选择一篇论文从头开始自己找alpha，但是尝试了一段时间以后没找到表现特别好的就放弃了，还是找了一篇研报进行复现。还是希望自己以后能够多尝试从论文找alpha，这样的话idea的创新性可能会好很多，能过correlation测试的alpha也会多一些。在跑代码的过程中，获取prod_corr的时候有时候会出现“Error while decoding prod_corr JSON for alpha XXXXXXX: Invalid or empty JSON”，还没有解决这个问题。还有一次性太多次请求prod_corr的时候，会出现“Error while fetching prod_corr for alpha XXXXXX: 429 Client Error: Too Many Requests for url:”，不知道有没有好的解决方法。

---

### 评论 #9 (作者: WL13229, 时间: 2年前)

[BX78946](/hc/en-us/profiles/16297370627607-BX78946)

您好，请不要对每个Alpha都请求corr.每小时的请求总数在千次级别。

对于第三个问题，我建议您可以把high open close low全部换掉，放到option data数据集去搜。因为option data也是一种价量数据。然后随机抽取四个不同的东西。或者你先根据option的各类数据先分四个组。

---

### 评论 #10 (作者: ZC80223, 时间: 2年前)

1.我的面板情况如下


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> USA
> CHN
> 22:14
> 岂
> O
> F  9 囤 N
> "
> V
> G%C 阴
> 入英  豳
> 2023/12/21


2、alpha灵感帖子链接： [[L2] 【Alpha灵感】基于反事实模拟的中国股市涨跌停板磁吸效应研究_20051302553879.md]([L2] 【Alpha灵感】基于反事实模拟的中国股市涨跌停板磁吸效应研究_20051302553879.md)

3、

av = vec_avg{x};#vector数据降维
        bv = vec_avg{y};#vector数据降维

signal = (shrt5_limit_down_price - vec_min(pv27_s_dq_low)) < (shrt5_limit_up_price - vec_max(pv27_s_dq_high)) ? -1 : 1;   #构造磁吸方向信号

Prob_trade = 1 / (1 + exp(-(-0.13 + 1.6 * 0.697 + 0.1 * bv + -0.15 * signal)));#构造基于交易活跃度信号的磁吸概率
        Prob_estimate = 1 / (1 + exp(-(-0.08 + 1.6 * 0.697 + 0.013 * av + -0.15 * signal)));#构造基于估值难度信号的磁吸概率
        trade_when(or((shrt5_limit_down_price - vec_min(pv27_s_dq_low)) <0.1,(shrt5_limit_up_price - vec_max(pv27_s_dq_high))<0.1),-rank(Prob_estimate + Prob_trade),-1) #根据文中对于研究对象的定义是股票涨跌停价9%左右样本，个人认为磁吸是反转策略，标志着非理性行为。对于高概率的上涨股票应该做空，下跌股票应该做多。

4、alpha结果，目前还在跑，首次遇到了生成expression高达58w的窘境，采用评论区留言的pv27作为重点生成对象，目前表达式降至19740个。有没有进一步减少范围的小tips？挖出了1个可用的但没过prod corr


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
> 2,00OK
> 1,5OOK
> 1,00OK
> SOOK
> 08/28/2013
> Is PnL: 0.00
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
> 0.0096
> 00
> 00N
> 0.0096
> 0.009600
> 2012
> 0.00
> 0096
> 009
> 0.0096
> 0.009600
> 2013
> 0.00
> 0.0096
> 00N
> 0.0096
> 0.009600
> 2014
> 0096
> 009
> 0.0096
> 009600
> 2015
> 0,UU
> 0096
> 0.009
> 0.0096
> 0.009600
> 2016
> 0.00
> 0096
> 00
> 0.009
> 0096
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
> 20.77%6
> 1.1796
> 29.709600
> 765
> 776


补充下，虽然这个idea没找到prod corr过的alpha，但其他idea有通过的。


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> SROW
> DUt OT
> Date Created (ESTJ: 12/28/2023-01/0,
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (ESTI
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Searcn
> SeNeC
> SeNeC
> SeNeC
> 12/28/2023
> 01/03 
> SeNeC
> SeNeC
> e.6>1
> e.6>1
> e.6>1
> SeNeC
> anonymous
> R=EUIar
> ACTIVE
> 12/31/2023 ET
> CHI
> TOP3UOT
> anonymous
> Reaular
> ACTIVE
> 12/30/2023 EST
> CHN
> T0P3000


5、感想

如果有2个以上的datafield，组合的可能性实在太多了，目前仍在摸索技巧中。关于template的有效性有了比较真实的感悟，如果一个template对该数据集无效，那么会出现大量的alpha结果是负值，1000个结果也找不到任何一个形态看上去合理的alpha。这时候需要思考策略是否是理解错了，需要进一步理解。

---

### 评论 #11 (作者: OA92025, 时间: 2年前)

老师，您好~我还是没有解决上周的问题。我的alpha在API提交了simulation之后，查询到‘Location’，打开后status是“complete”，而且也能查询并返回alpha的pnl表现等详情。但是在alpha列表仍然不会显示。排除了您说的1. alpha表达式错误（否则status会是 Error， 而我的是complete）2. sign in不成功（我的是201，是成功了的）这是为什么啊。。。

---

### 评论 #12 (作者: WL13229, 时间: 2年前)

[OA92025](/hc/en-us/profiles/18197007430167-OA92025)

1. 请使用print打印一下你每次simulate的Alpha表达式。

2.如果这个Alpha在之前simulate过，是不会更新数字的。

---

### 评论 #13 (作者: WL13229, 时间: 2年前)

[ZC80223](/hc/en-us/profiles/16412175793303-ZC80223)

请在Alpha灵感帖子或者您的回帖评论中增加Alpha绩效的截图

关于搜索空间过大的问题，这个是一个量化研究中面临的非常真实的问题。我觉得您对自己模板抽象后的理解还不够深入，请继续从数学角度，思考您的模板可以提取什么信息。欢迎跟帖讨论

---

### 评论 #14 (作者: YJ78324, 时间: 2年前)

**【Performance面板】**


> [!NOTE] [图片 OCR 识别内容]
> USA
> CHN


本次选取的研报是：东方证券因子选股系列之九十四：UMR2.0—风险溢价视角下的动量反转统一框架再升级

今天才发现，这篇研报选取的跟  YH69102 同学是一样，不过我也在其基础上提交了Alpha，也是CHN上的第一个Alpha。

**【Alpha灵感】**

分享链接： [【Alpha灵感】UMR2.0——风险溢价视角下的动量反转统一框架 – WorldQuant BRAIN]([L2] 【Alpha灵感】UMR20风险溢价视角下的动量反转统一框架_20101783750167.md)

**【Template构建与优化】**

本篇文章的核心在于以时序均值调整后的风险指标来加权个股每日的溢价，并以此构建统一的动量反转因子。

由此可以构建模板，其中天数60由研报中推荐给出，mkt的计算可以参考 [BRAIN小贴士(这里有你想要的硬核内容！持续周更中） – WorldQuant BRAIN]([L2] 【学习资料】BRAIN小贴士这里有你想要的硬核内容持续周更中Pinned_15152019662487.md)  中沪深300指标的计算：

```
R = {risk} / close;Risk = ts_mean(R, 60) - R;f = ts_decay_linear(Risk * (returns - mkt), 60);rank(f)
```

之后我对比了一下上式中f的计算，发现不计算超额收益时的效果会更好，所以修改模板为：

```
 f = ts_decay_linear(Risk * returns, 60);
```

在这里，我们搜索以volatility作为关键词进行搜索，以其作为每日风险指标，可以得到最佳结果如下：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1GN
> 15N
> 14N
> 13N
> 12N
> 11N
> 1ON
> 9,0OOK
> 80OOK
> 7,00OK
> 04/24/2015
> IS Pnl: 6,795.63k
> 5,00OK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> Jul '11
> Jan '12
> Jul '12
> Jan '13
> Jul '13
> Jan '14
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jul '20
> Jan '21



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
> Drawdown
> Margin
> 2.79
> 11.23%
> 3.30
> 17.53%
> 16.23%
> 31.229600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2011
> 3.42
> 12.8796
> 3.96
> 17.2796
> 5.48%
> 26.849600
> 1071
> 1078
> 2012
> 6.16
> 10.6096
> 9.44
> 29.3796
> 2.23%
> 55.419600
> 1142
> 1157
> 2013
> 2.91
> 10.5396
> 3.26
> 15.7196
> 4.27%
> 29.859600
> 1192
> 1193
> 2014
> 0.53
> 9.71%
> 0.26
> 3.01%
> 8.54%
> 6.199600
> 1185
> 1205
> 2015
> 1.14
> 12.9296
> 1.10
> 12.1196
> 16.23%
> 18.749600
> 1212
> 1216
> 2016
> 4.76
> 9.81%
> 68
> 24.6496
> 3.48%
> 50.249600
> 1338
> 1333
> 2017
> 3.52
> 9.839
> 4.35
> 19.1096
> 3.98%
> 38.869600
> 1486
> 1494
> 2018
> 4.17
> 13.9696
> 5.28
> 22.35%
> 1.91%
> 32.039600
> 1504
> 1501
> 2019
> 2.77
> 12.0296
> 2.87
> 13.4696
> 3.90%
> 22.409600
> 1501
> 1502
> 2020
> 1.28
> 10.3196
> 1.13
> 9.7796
> 7.13%
> 18.959600
> 1506
> 1502
> 2021
> 13.07
> 12.1296
> 34.65
> 87.8596
> 0.37%6
> 145.009600
> 1509
> 1514


可以看到因子的表现不错，可惜并不能通过prod相关性测试。

这里我考虑对因子进行融合，考虑到这个是利用量价数据的因子，所以考虑添加基本面因子进行融合。

这里的基本面因子我采用第一周的模板进行搜索：

```
rank(group_neutralize({field} - last_diff_value({field}, 5), bucket(rank(cap), range="0.1, 1, 0.1")));
```

参考上周结果，最佳的因子在回测最近的两年表现稍差没能通过测试，而此次的量价因子在这个周期表现较好，考虑将两个因子融合：

```
power(alpha_1, 2) + power(alpha_2, 2)
```

最终我们拿到了一个可以提交的Alpha


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 13M
> 12N
> 11M
> 1OM
> 9,00OK
> 8,0OOK
> 03/14/2017
> ISPnl: 7,912.171
> 7,00OK
> OOOK
> 5,OOOK
> 4,0OOK
> 3,00OK
> 2,00OK
> T,OOOK
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
> 叫 OS Summary
> Period
> IS
> 05
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> 02/14/2021 EST
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Pre-Close Sharpe
> Pre-Close Ratio
> Self-Correlation
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
> 4.53
> 11.489
> 5.07
> 15.6396
> 3.02%6
> 27.249600
> 970
> 1028
> 2012
> 6.40
> 10.5596
> 8.41
> 21.5796
> 1.35%
> 40.9
> %o0
> 1103
> 1134
> 2013
> 3.80
> 11.5096
> 4.21
> 15.3796
> 2.38%6
> 26.729600
> 1153
> 1226
> 2014
> 2.36
> 10.6696
> 1.96
> 8.659
> 4.69%6
> 16.249600
> 1144
> 1233
> 2015
> 0.54
> 12.3896
> 0.30
> 3.8596
> 8.38%
> 6.229600
> 1193
> 1215
> 2016
> 4.47
> 13.119
> 5.07
> 16.8796
> 2.41%6
> 25.759600
> 1314
> 1337
> 2017
> 4.19
> 10.1296
> 5.01
> 17.8796
> 2.85%
> 35.329600
> 1414
> 1502
> 2018
> 4.23
> 11.8096
> 5.06
> 17.8796
> 1.56%
> 30.289600
> 1399
> 1574
> 2019
> 3.12
> 12.7996
> 2.96
> 11.4896
> 4.46%
> 17.949600
> 1396
> 1584
> 2020
> 1.32
> 12.479
> 1.08
> 8.38%
> 5.55%
> 13.449600
> 1395
> 1568
> 2021
> 13.68
> 12.399
> 33.28
> 74.0096
> 0.44%
> 119.469600
> 1367
> 1583
> Correlation
> Self Correlation
> Highest Correlation
> Last Run: Mon; 12/25/2023,10:43 PN
> Prod Correlation
> Highest Correlation
> Last Run: Mon, 12/25/2023,10:43 PM
> 0.7



> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> ACTIVE
> 12/20/2023 EST
> CHN
> TOP3000


【总结】

通过本周的任务，一方面进一步优化了代码的易用性，可以通过配置文件完成自动化搜索。


> [!NOTE] [图片 OCR 识别内容]
> fields_configs:
> field:
> fields_count:
> 1888
> fields_confrg:
> instrument_type:
> 'EQUITY"
> 3天前
> region:
> "CHN"
> delay:
> universe
> "TOP3888"
> search: "volatility"
> alpha_conf rg:
> template:
> {field}
> close;
> Risk
> ts_mean(R,
> 68)
> R;
> ts_decay_Iinear(risk
> (returns),
> 60);
> rank(f)
> Vector_operator:
> field:
> Vec
> aVg({x})
> config:
> type:
> REGULAR"
> settings
> instrumentType:
> "EQUITY"
> region:
> CHN"
> universe:
> "T0P3080"
> delay:
> decay
> neutralization:
> IMARKET"
> truncation:
> 8.88
> pasteurization:
> "ON"
> unitHandling:
> 'VERIFY"
> nanHandling:
> TOFF"
> Ianguage:
> "FASTEXPR"
> Visualization:
> False
> Ou
> imu_
 另一方面我也在思考，对于单一一个因子没法满足要求时，可以考虑与其他大类的因子进行融合。进一步，可以将有潜力的因子PNL拿到，之后对自相关性不高的因子进行组合，尝试出可以通过的融合因子。

---

### 评论 #15 (作者: YW54232, 时间: 2年前)

【Performance面板】
 
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> USA
> GWN
 【Alpha灵感】

[[L2] 【Alpha灵感】高低位放量因子_20108973243671.md]([L2] 【Alpha灵感】高低位放量因子_20108973243671.md)

【Template分析】

alpha = low_event * vol_event == 1 ? -expression : 0;

因子背后的逻辑是在low和volatility事件都触发时进行交易和调仓，那么调仓的权重就是可以搜索的点。我思考的是在低位放量时，什么权重对这个事件而言是一个利好，因此可以在公司基本面数据中进行搜索。搜索中发现net profit能很好的契合我们的需求，所以作为expression信号的核心。

但是因为这个因子和volatility有着强相关性，所以不可避免在2015年A股股灾时有着很差的表现。我花费了两天事件去思考如何“规避”股灾，用了tips15进行尝试，但是发现结果是不robust的，也通不过universe robust测试。

我在此之间其实花费的大量时间去寻找一些能规避2015股灾的因子，但其实效果都不显著。所以要从底层逻辑进行思考，是不是我们这个因子本身并不robust。volatility本质也是和动量相关的，如果混合一些动量相关的判别会不会有好的改善。

于是我对alpha里加入一小部分close price相关的动量因子

ts_rank( (vec_avg(mdl14_2_d1_close_price) - close ),60)

的权重，顺利通过了测试！连2015的回撤也小了很多。结果也是非常的robust。


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 4.04
> 38.329
> 3.77
> 33.409
> 16.789
> 17.439600



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> ZSM
> ZOM
> 15M
> 1OM
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
> Select
> Select
> Select
> Search
> Select
> Select
> anonymous
> Regular
> ACTIVE
> 12/27/2023 EST
> CHN
> TOP3000


【总结反思】

这个alpha的创建过程让我想到一句话：不识庐山真面目，只缘身在此山中。我们不能为了改善因子的test而去改变，这样往往是很低效的，我也为此付出了大量的时间，结果找到方法后很快就改进成功了。关注因子本身和市场的逻辑，往往比只去关注PNL图那一点回撤和缺陷更有用。但是Tips 15对股灾的规避依然是很不错的方法，虽然这次没有完全使用上，但我也尝试了比如股灾中使用更强化的表达式等方法，确实对回撤有所改善。

---

### 评论 #16 (作者: WL13229, 时间: 2年前)

[YW54232](/hc/en-us/profiles/13837011976855-YW54232)

您的思考是非常深入的。很高兴看到您有所收获。确实如此，在股灾中直接平仓，这种方法是饮鸩止渴的。如果把策略换成在股灾中切换成其他的Alpha。可能会有不错的收获

---

### 评论 #17 (作者: FP65798, 时间: 2年前)

1.Performance面板截图
 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> USA
> Delay
> Fundamental data
> Model data
> Picevolume data
> Option data
> 15 alphas
> (12%of USA Delay 1)
> No limits for data categories With <30 Alphas.
> Other
> Analystdata
> Social media da。
> Option data
> Risk data
> News data
> Macro data


Option因子还比较少，故我选择option相关的研报进行研究。

2.新发布【Alpha灵感】
 [【Alpha灵感】关于未来的股票回报，个股期权波动率Smirk告诉了我们什么？]([L2] 【Alpha灵感】关于未来的股票回报个股期权波动率Smirk告诉了我们什么_20163362610711.md) 
参考文献： [Research Paper 20](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1107464)  : What Does Individual Option Volatility Smirk Tell Us About Future Equity Returns?

3.Template分析

```
diff = {x1} - {x2}
```


> [!NOTE] [图片 OCR 识别内容]
> dataset_id
> selected
> datasets_df.id.values.tolist()
> len(datafields_df )
> print (dataset_id)
> 0Os
> 0Os
> 1589
> [ 'option3o
> optionll
> optionl
> option4
> option6
> Optiong
> optiong
 Template是很简单的两数据做差，原因子是call和put期权隐含波动率做差，可以推广为两种波动率数据做差，甚至是两种同一单位的数据做差，都有可能蕴含有价值的信息。

如果限制在期权空间，前项固定，后项变化，则数据量为1509。进一步限制，后项我们只用opt4_put_vola_{x1}d， opt4_{x2}_put_vola_delta{x3}这样名称的数据，数据量缩减为1040。
 
> [!NOTE] [图片 OCR 识别内容]
> X1:
> [30,
> 91,
> 122,
> 152,
> 182,
> 273,
> 365]
> X2:
> [30,
> 91,
> 122,
> 152,
> 182,273,
> 547,730]
> 18
> X3:
> [20,
> 25,30,
> 35,
> 45,58,
> 55,
> 68,65,
> 70,
> 75,80]
> 13
> total number:
> 1848
> 60,
> 60,
> 365,
> 40,


4.成功提交Alpha截图 
> [!NOTE] [图片 OCR 识别内容]
> submit_result
> {alpha_id:
> ace. submit_alpha(s, alpha_id) for alpha_id in passed_alphas
> }
> submit_result
> 186s
> { 'aNw2ROX
> True,
> qn3kagE
> False}
  
> [!NOTE] [图片 OCR 识别内容]
> SKEW_Human
> Regular 
> ACTIVE
> 12/27/2023 EST
> USA
> 70P3000
> SKEWMachine
> Regular
> ACTIVE
> 12/27/2023 EST
> USA
> 70P3000
 最终使用Machine挖掘成功提交一个alpha，在做【Alpha灵感】过程中利用纯Human方式成功提交一个alpha。

5.总结反思
代码新增data id字段筛选模块，已初步掌握Human+Machine发掘因子流程，期待进一步的学习。

---

### 评论 #18 (作者: JT89676, 时间: 2年前)

**1. Performance**  **面板** 
 **[图片 (图片已丢失)]**

之前的alpha主要集中在USA地区，本次选择CHN利用基本面数据实现一个可以提交的alpha，并根据抽象的模版用machine搜索其它有提交潜力的alpha。

**2.【**  **Alpha**  **灵感】**

**链接为：**  **[[L2] 【Alpha灵感】从布林带到估值异常因子_20235808598423.md]([L2] 【Alpha灵感】从布林带到估值异常因子_20235808598423.md)**

**3. Template**  **分析**

```
a = ts_zscore(D, 252);a1 = group_neutralize(a, bucket(rank(cap), range="0.1,1,0.1"));a2 = group_neutralize(a1, subindustry);b = ts_zscore(cap, 252);b1 = group_neutralize(b, subindustry);regression_neut(a2, b1)
```

文章的原始alpha选择的D为PE（BRAIN平台对应选取的数据字段为fnd72_s_pit_or_is_q_spe_si），主要逻辑是股票的估值PE具有均值回复特性，可以仿照经典均值回复布林带的构造方法，构造估值布林带模型，如果某股票的估值处于异常区间且其基本面不发生大的变化，未来的EP有很大概率回归正常区间。此外，为了剔除行业层面估值逻辑改变的影响，用到了行业市值中性化处理，并在横截面上作regression，复现的alpha可以提交。Machine搜索阶段使用Earnings Quality数据集和Comprehensive Fundamental Data数据集中的字段对D进行填充并测试，找到一些可以通过IS测试的字段，但是Self Correlation和Prod Correlation都比较高，如下图所示，这样的alpha有32个（其中有些字段本来就是一个系列的，如mdl25_is_41v和mdl25_is_9v），使用的字段为 mdl25_is_41v、mdl25_rd_9v、mdl25_73v、fnd72_s_pit_or_is_q_net_income_bef_mi等。


> [!NOTE] [图片 OCR 识别内容]
> 压 Lorrelatlon
> Self Correlation
> HDHCSC COrrClUON
> L0
> 0
> 1 QgOII
> 0.775
> Prod Correlation
> HBhC S
> OTTCIIUIOT
> LustHUn
> Mon  01/01/2024。1208 PW
> IS Testing Status
> I0PASS
> Sharpe of 3.59
> above cutotfof 207.
> Of3.16
> 3hOI
> CItmtl
> TMTnOer
> 7.539
> abowe Cutoft
> Turnove
> 53%6
> hoO Ctot
> 7035
> Welght
> distributed
> nstrumens
> Rotlrn
> +719
> abore Cutott
> SUD unwerse Sharpe
> CUroffof 2,2
> RahwIs Inierce
> curofrof
> (409 of Alpha)
> Robustuniyerse rpurns
> 349
> aboe cutoffof
> 88% (406 OfAlphal
> lacder Sharpe cf 3,58
> ahove CUtoffof 2,37 forladderyear
> 2/18/2021
> 2/19/2019
> WARNING
> Fness
> JbOVE
> Shrpe
> 300



> [!NOTE] [图片 OCR 识别内容]
> JTCTTOU
> hZUUI
> UNISUUAIITTVC
> 130112123 LST
> TC?TU0
> S21
> 75
> JTUTIOU
> R-UUUI
> JNSUUINIIITUL
> 1231'12 CST
> T7-190
> 139
> 7.5E
> UTIUIIU:
> Ruul
> UNSUUNIII TUL
> 12'3142323 EST
> TC33190
> 5TIC
> 5
> ITUITIOU
> q3BWUI
> JNISUIOIIIIUL
> 1231123EST
> T7-TNn
> 571
> 5
> ATNIIIC
> R2BUUI
> UNSUIBAIIIEL
> 1312723E5
> 72339
> 32
> T
> ANINTII
> hRUHI
> INSUBNITTEC
> 1231723E5T
> T31n
> I0 35
> 9439
> nnorymols
> RRUUI
> UINSUBNITTEC
> 1151351
> TT
> TII
> !
> JnonTTOU'
> h PULF
> UINSUBNITTEC
> 14150341
> TJMTUI
>  C
> e
> OTIITTOI
> 片 TIT
> UNSUNNITTTP
> 1'
> TJUIII
> 1 !
> TUI
> unCNTTOU
> hDUL
> UNTUNNITTTC
> 1!L '
> TUUII
> 11]
> Uy4
> OUt 
> N


**4. 提交截图**

**
> [!NOTE] [图片 OCR 识别内容]
> Select COIUITIS
> Name
> Ccnpeirion
> SaS
> Cate CrEJtEJ EST
> IT ;arSl
> RetITs
> TIIIE
> splerr
> JTOTITICU
> HC Jlur
> ACTIUIT
> 1293152L39 EST
> CHN
> TCPSJCI
> TD
> Reg 5
> Sharr?
**

**5. 反思**

本次使用的模版还是比较简单，Machine搜索时产生的alpha的Self Correlation和Prod Correlation都比较高。本次还优化了自动化提交脚本，统一了模版字段替换函数的调用过程。

---

### 评论 #19 (作者: WL13229, 时间: 2年前)

[JT89676](/hc/en-us/profiles/18490343365399-JT89676)

有点好奇，corr高的情况如何克服的。最后是通过什么改进进行了提交。另外就是，可以考虑分析师的数据

---

### 评论 #20 (作者: TG50517, 时间: 2年前)

1. 本人的Performance面板截图，选择Fundamental data的文章“New Evidence on the Relation Between the Enterprise Multiple and Average Stock Returns”。


> [!NOTE] [图片 OCR 识别内容]
> Neduu
> NCJeldu
> Pte volume Uul』
> Fundmtnizl d;1
> UoWVIT O0u
> SNIPL4.111
> ETIIII 9+
> SDIIIILUJtl
> Reedy
> Ctr


2. 新的《Alpha灵感》文章链接：

[[L2] 【Alpha灵感】企业倍数与平均股票回报率之间关系的新证据_20240820051607.md]([L2] 【Alpha灵感】企业倍数与平均股票回报率之间关系的新证据_20240820051607.md)

3. 核心思路很简单，构造“Enterprise Multiple”，然后数值低的做多，数值高的做空。而

```
Enterprise Multiple = Enterprise Value / EBITDA
```

所以只需要搜索“Enterprise Value”的Datafields {A}，以及“EBITDA”的Datafields {B}，从而

```
Signal = group_rank(ts_rank(-rank(A)/rank(B),5),industry)
```

然而，搜索到的{A}含有242个Datafield，{B}含有680个Datafield，二者有超过16万种组合，空间太大，不值得全部回测。


> [!NOTE] [图片 OCR 识别内容]
> Enlerprise
> [I.
> Value
> luncamonal
> uncamontal72
> 15121
> Ind72_ul_OI_Cr
> Nerpiise
> TAIUP
> Markel Cap
> 09119
> lundamenal
> TUACAION|
> USA
> TOP3DOO
> VECTOR
> 0.8738
> OUIUN
> gala
> CompiehensIv0。
> EqUI
> Penodic
> enerprse
> [id;
> tunoamenal
> 'tundamenal72
> 15922
> fnd72
> LDt_OT_Cr
> T2m_cash_Hloww
> VaUe 85
> 'name;
> fundamenal
> tundamenla
> USA
> TOP3OOD
> IATRI
> 0.7114
> multple of
> 038
> Comprehensive。
> 242 rOws
> 13 columns
> len(enterprise_value_df)
> 242



> [!NOTE] [图片 OCR 识别内容]
> price
> [I ;
> tundamenel
> clviced by
> fundamenal72
> 14988
> fndT2_pit_Or_CT_
> low_Pt
> cbida
> EBITDAper
> 090
> funcamental
> fundameneal
> USA
> TOP3OO0
> VECTOR
> 0.8224
> 02
> 909T
> Comprehensive
> Earings
> belore
> fid:
> fundamenal
> ITCTRSL
> fundamenal72
> 15116
> 5d72_pi_Or_CI_
> cbitda_
> OS_CJP_otpond_
> funcamontal
> TUDJATCMaI
> USA
> TOP30OO
> VECTOR
> 0.6326
> 10+05
> name
> dala
> Ceplecation
> Comprehensive。
> 680 Tows
> 13 columns
> len (ebitda
> df)
> 680


这时发现，有些数据同时包含“ev”和“ebitda”，也就是把“Enterprise Multiple”算好了，这样就可以直接拿来用。不过使用的时候需要注意，有的数据计算的是“ev/ebitda”，有的是“ebitda/ev”，在表达式中加上适当的处理就可以套用同一个模板。
适用的Universe和Neutralization在《Alpha灵感》文章中已有讨论，不再赘述。

4. 成功提交的Alpha截图如下。


> [!NOTE] [图片 OCR 识别内容]
> 副川
> IS Testing Status
> Period
> 05
> 10PASS
> Sharpe Of 2.20is above cUtoff of 1.58
> Fitness Of 1.65 is above cUtoffof1。
> Turnoverof 12,57915above CUOfFOT 19,
> Turnover of 12.579Is below cutoff of 70%。
> Weightis well distributed over instruments
> Sub-universe Sharpe Of 1.41is above cUtOffof 0.95
> Self-correlation 0.3806 is below cUtoff of 0.7.
> Prod correlation 0,5647is below CUOfFOT 0.7
> Alpha submissions
> below quota Of4。
> IS ladder Sharpe of 2.66 is above cUtoff of 2.37 for ladder year 2; 2/16/2021..,2/17/2019。
> 1WARNING



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> 2.20
> 12.579
> 1.65
> 7.039
> 2.829
> 11.189600
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
> 3.91
> 21.31%
> 3.64
> 18.45%
> 2.1496
> 17.32"0
> 488
> 509
> 2012
> 2.67
> 15.5990
> 8.049
> 1.7090
> 10.32"20
> 656
> 696
> 2013
> 2.81
> 13.2296
> 2.25
> 8.499
> 1.8196
> 12.83"
> 780
> 2014
> 2.33
> 12.029
> 5.73%
> 4896
> 9.53n0
> 822
> 869
> 2015
> 0.36
> 11.929
> 0.39
> 2.5996
> 2.8296
> 4.3500
> 861
> 934
> 2016
> 1,65
> 11,4096
> ,04
> 4,939
> 9590
> 8.65noo
> 890
> 955
> 2017
> 1,07
> 10,4796
> 0,47
> 2,469
> 1.3490
> 4.7Onn
> 912
> 966
> 2018
> 1,60
> 11,1096
> 0,91
> 089
> 1.2796
> 7.36
> 948
> 1023
> 2019
> 1,91
> 10,689
> 1,31
> 5,909
> 8096
> 11,05"an
> 969
> 1028
> 2020
> 2.61
> 10.439
> 2.48
> 11.319
> 1.7196
> 21.6ga
> 1018
> 1118
> 2021
> 5.75
> 9.699
> 7.79
> 22.959
> 3696
> 47.3940
> 1093
> 1145



> [!NOTE] [图片 OCR 识别内容]
> SCLCCL ColJI
> Name
> Type
> Ctas
> Dale Creaed (ESTI
> RatTn 5
> TrNCT
> Nmwm
> Fitness
> ACTNE
> C
> Ruln
> ACTI
> 12/30/2023EST
> TTS
> I CT
> F
> 11 1』
> RCT
> Shnt
> Tmin



> [!NOTE] [图片 OCR 识别内容]
> Self
> COTr
> prod
> COFT
> delta_sharpe
> delta_
> tUrnOVer
> delta_fitness
> delta_returns
> delta_
> drawdown
> delta_margin
> 3806
> 0.5647
> 0.01
> -0.03
> 0.01


5. 总结反思。

首先，本人的量化研究理念是从一个比较简单，蕴含明确经济学逻辑的Idea出发，然后再一步步优化，在优化的过程中也要保证逻辑的清晰可靠，这样可有效避免Overfitting，所以选择的论文Idea往往比较简单。今后也要尝试更加复杂的论文。

然后，在代码方面，本人在上次作业的基础上，把相关代码写进了一个Python Library中，这样用到哪个函数就可以直接调用，更加方便。

---

### 评论 #21 (作者: OA92025, 时间: 2年前)

paper：华泰单因子测试之换手率类因子（林晓明）

idea：计算每日换手率，以其过去一个月（22个交易日）的移动平均作为因子，再做“市值cap”分组的中性化处理（利用bucket）

1.python暴力循环：

利用循环设置decay、universe和neutral的方式，寻找最大的fitness。如果当前的fitness更大，就把setting记录下来。（很缓慢，而且有的提交不上去，需要用异常捕获，防止中断）


> [!NOTE] [图片 OCR 识别内容]
> 5
> for decay
> in tqdm(range(l,30) ):
> 6
> for neutrl
> in
> [
> INDUSTRY
> SUBINDUSTRY
> MARKET
> NONE
> SECTOR
> ]:
> for
> trunc
> in
> np.arange(0,0.1,0.005 )
> 8
> for
> uni
> in
> [
> T0P3800
> TOPIOgO
> TOP5OO
> TOP2Oo' ]:
> 9
> simulation
> data
> {
> 0
> regular
> "turnover=volume
> (1ooooeo*sharesout ) ; IrIna
> 1
> settings
> {



> [!NOTE] [图片 OCR 识别内容]
> Spyder (Python 3.10)
> 文件(F)  编辑(E)  查找(5) 源代码(C)  运行(R)  调试(D)  控制台(0) 项目()  工具[T 查看(V 帮助(H)
> 血 日  旦
>  Q   C [
> @ ! ^八
> 四/ ^雷
> D: Iupps
> unaconda  Spyder
> Codes
> D: |南京大学1职业发展 | Jorldquant Brainl1000次. D
> 帮助来源于
> 控制台
> 对象
> crawler. Dy X
> 1000次。
> 义
> 87
> datasets_df[ 'region' ]
> settings[ 'region' ]
> 使用方法
> 88
> datasets_df[ 'delay' ]
> settings [ ' delay
> 89
> datasets_df[ 'universe' ]
> settings [ 'universe' ]
> 在这里你可以通过在编辑器或者终端中按 Ctrltl
> 90
> 来获得任何对象的帮助信息。
> 91
> return
> datasets df
> 帮助信息可以在
> 个对象之后加上一个左圆括号
> 92
> 的时候自动显示。你可以在_工具>偏好设置>
> 93
> #%%
> 帮助中激活此行为。
> 94
> fitness=s
> 95
> for decay
> in tqdm(range(l,30)):
> 第一次使用 Spyder? 请阅读教程
> 96
> for neutrl
> in
> [
> INDUSTRY
> SUBINDUSTRY
> MARKET
> NONE
> SECTOR
> ]:
> 97
> for
> trunc
> in
> np.arange(0,0
> 0.005 )
> 98
> for
> uni
> in
> [
> TOP3800
> TOPIOgO
> TOP5OO
> TOP2Oo' ]:
> 99
> simulation data
> {
> 180
> regular
> "turnover=volume
> (leeeeea*sharesout ) ; IrInalpha=-ts
> mean(returns*turnover, 22) ; Ir Ingroup_ne
> 101
> settings
> {
> 102
> decay
> decay
> 103
> 'delay
> 1,
> 104
> 'instrumentType
> "EQUITY"
> 105
> 'Language
> "FASTEXPR
> 106
> nanHandling
> "OFF"
> 107
> 'neutralization
> neutrl,
> 帮助 |娈量浏览器 |绘图
> 文件
> 108
> 'pasteurization
> "ON"
> 109
> region
> "CHN
> 控制台 I/A X
> 110
> truncation
> trunc,
> 1000次.py' )
> 111
> unitHandling
> "VERIFY"
> 0%1
> 0/29 [80:00〈?, ?i/s]201
> 112
> universe
> uni,
> 400
> 113
> 'visualization
> False},
> 400
> 114
> type
> "REGULAR"
> 400
> 115
> }
> 201
> 116
> 480
> 117
> simulation_response
> s . post( 'https: LLapi.worLdquantbrain. gomLsimulations
> jsonssimulation_data)
> 480
> 118
> print(simulation_response. status
> code)
> 400
> 119
> simulation_progress
> Url
> simulation_response .headers [ ' Location' ]
> 201
> 120
> While
> True
> 480
> 121
> simulation_progress
> S.get(simulation_progress_url )
> 480
> 122
> if simulation_progress .headers .get( "Retry-After
> 0)
> 0:
> 400
> 123
> break
> 201
> 124
> sleep(float (simulation_progress .headers[ "Retry-After"]))
> 480
> 125
> alpha_id
> simulation_progress .json( ) [ "alpha" ]
> 400
> 126
> alpha
> S.get( "hts:
> Lapi.WorLdquantbrain.comlalphasL"
> alpha_id)
> 400
> 127
> i fitnesscalpha.json() [
> is '][ 'fitness' ]:
> 201
> 128
> fitness=alpha.json() [ 'is '][ 'fitness
> 1
> 480
> 129
> record=simulation data
> 400
> 130
> except:
> 400
> 131
> pass
> 201
> 132
> 480
> 133
> 400
> 134
> #%%
> 400
> IPython控制台|历吏
> conda:
> base  (Python
> 3.10.9)
> Completions:
> conda (base)
> LSP: Python
> Line 134,
> Col 1
> UIF-8
> CRLE
>  
> Jem  639
> 23:59
> Q 搜索
> ^
> IMl   英  拼  谷 d)囱
> 2024/1/1
> Djy
> .1,
> try:


2.最终的最优结果：（相关性也可提交）


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
> CHN
> TOP3000
> Fast Expression
> 0.095
> Subindustry
> On
> Off
> Verify



> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 12/18/2023 EST
> anonymous
> Add Alphato a List
> 区 Open alpha details in new tab
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
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawqOwn
> Margin
> 3.49
> 14.46%
> 5.48
> 35.61%
> 10.20%
> 49.26900
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2011
> 3.43
> 15.06%
> 4.71
> 28.37%6
> 3.73%
> 37.679600
> 1272
> 878
> 2012
> 4.22
> 14.22%
> 6.44
> 33.15%
> 3.81%
> 46.629600
> 1368
> 928
> 2013
> 3.33
> 13.52%
> 5.31
> 34.36%
> 4.22%
> 50.829600
> 1417
> 964
> 2014
> 2.99
> 13.28%
> 4.16
> 25.75%
> 5.16%
> 38.790000
> 1417
> 971
> 2015
> 4.11
> 14.93%
> 7.95
> 55.91%
> 3.37%
> 74.9
> 9300
> 1449
> 989
> 2016
> 4.79
> 14.54%
> 8.25
> 43.08%
> 4.40%
> 59.259600
> 1600
> 1069
> 2017
> 3.51
> 13.95%
> 5.24
> 31.13%
> 3.90%
> 44.629600
> 1793
> 1187
> 2018
> 5.39
> 15.47%
> 9.44
> 47.43%
> 2.49%
> 61.330000
> 1782
> 1222
> 2019
> 4.56
> 15.16%
> 7.74
> 43.63%
> 4.43%
> 57.589600
> 1793
> 1210
> 2020
> 0.53
> 14.65%
> 0.38
> 7.43%
> 10.08%
> 10.149600
> 1796
> 1215
> 2021
> 2.36
> 14.31%
> 3.95
> 40.03%
> 2.41%
> 55.979600
> 1872
> 1152
> Correlation
> Check Submission
> Submit Alpha
 3.反思：

太慢了太慢了！！！（4个半小时，提交了约500次）


> [!NOTE] [图片 OCR 识别内容]
> 3
> print("PnL retrieved")
> 4
> 在这里你可以通过在编辑器或者终端中按 Ctrltl
> 5
> #%%获.Checks酌结果
> 来获得任何对象的帮助信息。
> 6
> is_checks_response
> 5.
> (f"https:
> Lapi.WorLdquantbrain.comlalphasLfalpha
> jd}Lcheck
> 帮助信息可以在-个对象之后加上一个左圆括号
> 7
> pint(is
> Checks
> pesponse
> 的时候自动显示。
> 你可以在工具>偏好设置>
> 8
> #%%  获取所有满足条件alpha
> 帮助中激活此行为。
> 9
> settings
> { 'region
> ASI
> delay
> '1'
> universe
> ILLIQUID_MINVOLIM
> 'inlstrumentType
> EQUITY' }
> 第一次使用 Spyder? 请阅读教程
> 1
> def
> datasets(session, settings):
> 2
> url
> "https: LLapiworLdquantbrain. ComLdata-Sets?"
> 十
> 3
> f"instrumentType={settings[ ' instrumentType ' ] }@ion={settings [ 'region ' ] }8delay={settings[ ' delay ' ]}&universe={setti
> 4
> result
> session. get(url)
> 5
> datasets df
> pd .DataFrame(result.json() [ 'results' ])
> 6
> datasets_df[ ' instrumentType
> settings[ 'instrumentType' ]
> 7
> datasets_df[ 'region
> 1
> settings[ 'region
> 8
> datasets_df[ ' delay' ]
> settings [ ' delay
> 9
> datasets_df[ 'universe
> ]
> settings[ 'universe' ]
> 1
> return datasets df
> 2
> 帮助 |变量浏览器 |绘图 |文件
> 3
> #%%
> 4
> fitness=5
> 控制台 I/4 X
> 5
> for decay
> in tqdm(range(1,30)):
> 401
> 6
> for
> neutrl
> in
> [
> INDUSTRY
> SUBINDUSTRY
> MARKET
> NONE
> SECTOR' ]:
> 401
> 7
> for
> trunc
> in
> np.arange(0,0.1,0.005 )
> 100%
> 9/29
> [4:52:18<00:00,
> 66
> 795/i]401
> 8
> for
> uni
> in
> ['TOP3800
> TOPIOgO
> TOP5OO
> TOP2O0' ] :
> 9
> simulation data
> {
> regular
> "turnover=voLume/ (loooooo*sharesout ) ; IrInalpha=-ts_mean(returns*turnover, 22) ; |rIngroup_ne
> In
> [28]:
> 1
> settings
> {
> 2
>  decay
> decay,
> 3
>  delay
> 1,
> 4
> instrumentType
> "EQUITY"
> 5
> Language
> "FASTEXPR
> 6
> 'nanHandling
> "OFF
> 7
> neutralization
> neutrl,
> 8
> 'pasteurization
> "ON"
> 9
> 'region
> "CHN"
> truncation
> trunc,
> 1
> unitHandling
> "VERIFY"
> 2
> universe
> uni,
> 3
> 'visualization
> False},
> type
> "REGULAR"
> 5
> get
> Bet


其实后来想到：

a. 可以先再brain上面模拟一下，得出大致的区间范围，可以减少循环。

b. 也不用每次记录fitness，不用每次查询结果（每次查询都要耗时很多），只需要又submission的记录，然后最后在alpha list里面，按照fitness和sharpe来排序，选最高的提交就行了。


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
> Selec
> SeleC
> Selec
> Search
> SeleC
> Selec
> e8〉1
> e.8〉1
> e.8〉1
> SeleCt
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.61
> 35.14%6
> 24.0296
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.61
> 35.14%6
> 24.0296
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.61
> 35.14%6
> 24.02%
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.61
> 35.149
> 24.02%6
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.61
> 35.10%
> 24.01%
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.61
> 35.149
> 24.02%6
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.49
> 35.97%
> 22.93%6
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 3.49
> 35.97%6
> 22.93%6
> Tag


---

### 评论 #22 (作者: ZL89083, 时间: 2年前)

1,这是我的performance面板


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> Alphas
> USA
> Delay 1


我选择用fundamental方面的文章

2，论文链接：  [**https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3292675**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3292675)

3，寻找template

论文的大概意思就是由于商誉容易被投资者忽视，且不可评估，商誉/销售额这个指标虽然包含了公司价值的信息，但是股市对这些信息反应不足，这个指标其实是一个reversal的指标。但是由于并购行为周期比较长，因此论文里提出了结合量价信息与商誉销售比结合的方式构造因子。所以这个template其实是一种将基本面与量价信息结合的方法。其好处有二：1，提高因子的turnover 2,用量价信息加强并验证基本面的信息。我继续寻找有关setting的信息。并在论文里找到了industry分组的信息，推断股票池为Top500，这让我确定了setting。另外，文章提及了使用排序的方法构建组合，所以operater是以rank为基础。我依照文章构建了一个alpha,表现如下： 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.79
> 26.749
> 0.97
> 7.899
> 5.339
> 5.909600
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.79
> 26.749
> 0.97
> 7.899
> 5.339
> 5.909600


sharpe大于1.3，fitness高于0.6，turnover也低于45%，但是correlation为0.8，所以我改变了一下分组方式，改成了pv13_com_page_rank，这降低了相关性，而且适当提高了fitness。

4，template分析。

这个template基本上确定是用两个基本面的数据作为自由度，固定量价的指标，否则搜素强度太大，我就用search法搜索了fundamental的数据，然后用随机抽样的方式抽取了两次，每次50个，一共搜索2500次。在machine的过程中，我发现提交的alpha基本是正的收益，说明这个template是比较不错的，最后搜集的alpha表现如下。


> [!NOTE] [图片 OCR 识别内容]
> regular_code
> ftness
> returns
> drawdown
> margin
> sharpe
> IS_ladder_sharpe_status
> i
> ZjNZRWZ
> my_group=bucket(rank(pv13_com_page_rank),range。。
> 1.21
> 0.1054
> 0.1155
> 0.000783
> 10364903
> 1.93
> PASS
> NngzOMW
> my_group=bucket(rank(pv13_h_min24_5OO_sector)..
> 1.19
> 0.1031
> 0.1112
> 0.000774
> 10142671
> 1.91
> PASS
> JnrzZAe
> my_group=bucket(rank(pv13_com_page_rank)range..
> 1.18
> 0.1034
> 0.0902
> 0.000737
> 10174415
> 1.95
> PASS
> ZNzqwn
> my_group=bucket(rank(pv13_com_page_rank)range..
> 1.15
> 0.1046
> 0.1005
> 0.000753
> 10285782
> 1.87
> PASS
> nnrqbMM
> my_group=bucket(rank(pv13_com_page_rank)range..
> 1.15
> 0.1039
> 0.1279
> 0.000758
> 10219702
> 1.86
> PASS
> XkMZITI
> my_group=bucket(rank(pv13_com_page_rank)range..
> 1.14
> 0.1024
> 0.1234
> 0.000732
> 10073447
> 1.89
> PASS
> Ln3zek6
> my_group=bucket(rank(pv13_com_page_rank)range..
> 1.11
> 0.1005
> 0.0910
> 0.000737
> 9890037
> 1.83
> PASS
> pnl


差不多fitness在0.95以上的我都human式的跑了一下，基本都可以提交，最终改进了相关性和fitness后提交了三个，后续还可以继续搜索


> [!NOTE] [图片 OCR 识别内容]
> GOOOK
> 40OOK
> ZOOOK
> 03/12/2012
> ISPnl -152.42k
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
> 20
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> 2.02
> 31.519
> 1.14
> 10.129
> 6.349
> 6.43900
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> dd Alphato a List
> Check Submission
> Submit Alpha
> OAAN



> [!NOTE] [图片 OCR 识别内容]
> 6,0OOK
> 40OOK
> ZOOOK
> 04/13/2011
> 5Pnl: 27.95K
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
> 叫
> IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> 1.94
> 30.789
> 1.03
> 8.609
> 6.629
> 5.599600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> udd Alphatoa List
> Check Submission
> Submit Alpha
> Year



> [!NOTE] [图片 OCR 识别内容]
> GOOOK
> 40OOK
> 2,0OOK
> 06/20/2011
> 5 Pnl: -140.49K
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
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrhs
> Drawgown
> Margin
> 1.93
> 26.939
> 1.21
> 10.549
> 11.559
> 7.839600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> Add Alpha to
> LISt
> Check Submission
> Submit Alpha


说明还是比较成功的，虽然fitness都不算高

---

### 评论 #23 (作者: ZZ51944, 时间: 2年前)

## Performance面板截图


> [!NOTE] [图片 OCR 识别内容]
> ~lick to drill down
> USA
> 40 alphas
> (87%6 ofall Alphas)
> USA
> CHN


对于USA和CHN市场探索较多，多为量价和基本面数据。

选择的文章：做学术研究时总结的常用技术指标

## 《Alpha灵感》链接

[【Alpha灵感】常见技术指标在A股测试 – WorldQuant BRAIN]([L2] 【Alpha灵感】常见技术指标在A股测试_20247158390295.md)

## Template分析

生成了 [国家，股票池，中性化] 的三元组，其他使用默认参数，对于已经计算好的10个技术指标（实际上有13个值），以及其不同的数学计算直接进行暴力搜索。

全部的搜索空间 8*5*8*13*6=4000，但是因为股票池并不那么重要，所以先舍去了这个条件，对于表现较好的组合再进行股票池以及其他参数的调优。

## 提交Alpha截图

## 
> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> ACTIVE
> 01/01/2024 EST
> CHN
> TOP2000
 
 总结反思

这次主要是学习了如何提高代码的鲁棒性，自动解决一些跳过的问题。

模板改进方向：

横向的改进：加入更多技术指标和技术指标信息提取的数学表达式；

纵向：尝试技术指标调优；

---

### 评论 #24 (作者: WX16829, 时间: 2年前)

作业提交

1.Performance面板：可以看出在USA delay 1中基本面数据和其他类数据相对用得较少，我选择阅读Research paper 18 : Earnings Volatility, Ambiguity, and Crisis-Period Stock Returns


> [!NOTE] [图片 OCR 识别内容]
> Distribution Of Active Alphas
> Cli  t JrillJar
> 0?1 CJ
> Aely: Cae
> 011
> Wodsll
> Ueydl 
> Senllneaalu
> Sc-lyluedydb
> TunrTehIuI
> edh
> G?TIrTJI


2.《Alpha灵感》文章：市场危机下盈利波动、不确定性与股价回报

[[L2] 【Alpha灵感】市场危机下盈利波动不确定性与股价回报_20103734605591.md?page=1#community_comment_20230670783767]([L2] 【Alpha灵感】市场危机下盈利波动不确定性与股价回报_20103734605591.md?page=1#community_comment_20230670783767)

3.Template分析：从文章中所提示的数据特征已可直接构造出一个可提交的alpha，并比较容易地抽象得到以下模板：

crisis_ind==FALSE ? normal_factor : ts_delay(crisis_factor,days)

该模板的含义是：当股价处在正常水平时，使用一般的基本面因子进行预测和交易；当股价进入危机时刻后，使用危机前能够预测危机中股价变动的因子进行交易。

从以上模板中可以看出，因子的泛化可以从三个维度考虑：

- normal_factor：这类因子的选择比较多，感觉上一般表现不错的基本面因子均可以考虑，最简单的方法就是将论文提供的Fundamental28中的特征（一共有超过2000个）进行尝试，其他fundamental dataset或analyst dataset中的特征因子也可考虑。
- crisis_factor：文章中给出oth401_game_eps_vol这个特征构造crisis factor,其核心是认为公司危机前经营上面的波动与危机中的股价变化存在较强的关联性，在other401这个数据集中除了盈利波动外，其他与经营相关的波动特征（例如gross margin vol,Cash Flow Variability,SG&A Volatility等）均可考虑放入模板中测试。
- crisis_ind:这部分目前还没有想到相对固定的模板进行泛化，但除了股价波动这个方法外，违约距离（default distance）、CDS违约特征等均对于危机的判断有比较密切的关联，在平台上也可以找到相关的数据特征进行尝试。

总体上，该模板的泛化能力还是比较强的，可以进行尝试的方向和数据集比较多。该模板的使用的数据以基本面特征数据为主，因子换手率一般相对比较低，同时基本面的特征对同一行业内的公司具有较高的可比性，因此做neutralization或分组时多倾向考虑选择INDUSTRY或SUBINDUSTRY等行业相关的分组类型。

4.提交截图：提交了两个因子，一个是通过人工得到的，另一个是通过模板泛化后找到的。


> [!NOTE] [图片 OCR 识别内容]
> UuUeyha L
> ]
> ++1
> 1s
> n
> 757


5.总结反思

在研究方面，主要是花时间研究了通过论文的核心思想如何构造合适的模板，一开始的时候研究方面有偏差，花了不少时间在如何提前判断危机的来临，这个难度确实比较大。后面改为判断是否已出现危机为条件，难度大幅下降了，模板很快地确定下来，第一个因子也较为顺利的提交。因此，判断和选择合适的方向对于因子的研究是十分重要的。

在代码方面，基本沿用了上次的模板，使用Fundamental28的特征逐个放入模板尝试不同的normal_factor，从结果上看不少也可达到可提交的标准，且有一些因子的绩效较第一个因子有明显的提升。对于crisis_factor和crisis_ind初步人工尝试了一下，也能找到一些可提交的因子。如果同时变动三个维度，搜索空间会很大（Fundamental28里面已经有2000多特征），所以后续考虑的方向是如何降低搜索范围，可考虑的方向是先找到绩效较好的normal_factor,过滤后再尝试与不同的crisis_factor和crisis_ind进行组合（这两个维度相对的搜索空间会小一些），看一下最后能否得到其他的有效因子。

另外，在灵感文章后所提的意见中关于不同类型alpha直接连接的问题，这个确实在设计时没有意识到，但目前所使用的normal_factor和crisis_factor外层都是使用了rank这个operator,算是有点歪打正着吧，后续在泛化的过程中这个问题确实需要注意。

对于robust的问题，这个也是一个很好的需改进方向，目前在设计因子中对这方面考虑的并不多，后续这个方向还需要在进一步改进。

---

### 评论 #25 (作者: WD77850, 时间: 2年前)

- 1.Performance 截图
  - 这是我的performance截图，因为量价因子提交较少，故选择量价因子进行研究。 
> [!NOTE] [图片 OCR 识别内容]
> Distribution Of Active Alphas
> Click to drill down
> Model data
> Rce volume data
> Fndamental data
> @ption data
> Socal media data
> News data

- 2. alpha 灵感 湘财证券-多因子量化选股系列之四：新技术因子的研究与测试
  - [Alpha 灵感 湘财证券-多因子量化选股系列之四：新技术因子的研究与测试 – WorldQuant BRAIN]([L2] 【Alpha 灵感】多因子量化选股系列之四新技术因子的研究与测试_20251795571351.md)
- 3. Template 分析
  - 抽象得到以下模板（由于因子衡量非流动性，故选择非流动性池，并选择行业中性化。基于检测中出现的集中性问题，加入winsorize控制集中性）
  - group_backfill(winsorize(-ts_mean(A,30)/ts_mean(B,30),std = 4.0), industry, 20, std = 4.0)
  - 原模板已经可以得到一个可提交的因子。抽象的模板表示了B因子在一段时期内的信息对A因子在一段时间内的影响变化，刻画了非流动性指标。很容易得到B一般是与股票日交易额相关的数据，A则一般是与收益率相关的数据。选择多个相关data set进行遍历，替换为oth143_sell_tier1_volume获得了更好的因子表现。经改进后因子通过了测试可以提交 
> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Data
> 留 Competitions (2)
> Events
> Learn
> Refer
> 3
> friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Show
> 10
> out Of 172
> Date Created (EST): 12/31/2023-12/3 _
> X
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
> Select
> Select
> 12/31/2023
> 12/31
> Select
> Select
> e.8>1
> e.吕>1
> e.8〉1
> Select
> anonymous
> Regular
> ACTIVE
> 12/31/2023 EST
> USA
> ILLIQUID_MINV.
> 1.92
> 11.609
> 27.819
> Tag
  
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

- 总结反思：本次作业出现了一些设备问题导致平台操作出现了一些问题，幸好后续找到了替代办法。本次作业试了4篇研报才终于得到一个可以提交的因子。我认为有以下两点教训：1.尽量不要试图在平台上构建以分钟为维度或使用较多日详细交易订单数据的高频因子，特别是出现多个数据段的时候迁移到低频的方法效果也不佳。2.原本template效果较差的时候替换相似数据大概率效果也不佳，反而会浪费大量时间模拟。代码效率：API使用过程中发现在get dataset结果中找到需要的data set 的id比较困难，于是添加了根据名字找id的方法简化了流程。 
> [!NOTE] [图片 OCR 识别内容]
> In
> [4]:
> def get_id_from_name (session;
> settings,
> dataset _
> nale _
> Ur1
> 'https: //api. worIdquantbrain。
> data-sets?
> [
> instrumentType= {settings [' instrumentType' ]} &region= {settings [' region' ] } &delay= {settings [' delay' ] } &universe= {settings [' universe' ]}
> result
> 二
> session。
> (ur1)
> datasets
> resllt. json () [' results']
> for
> dataset
> i datasets:
> i dataset [' name' ]
> 二二
> dataset_
> name
> return
> dataset [' id' ]
> return
> None
> # find
> dataset_
> nale
> to_find
> ESG
> SCores
> dataset_id
> get_id_from_name ($,
> settings;
> dataset_
> nale
> to_find)
> if dataset_id:
> print (f"Ihe ID for
> {dataset_name_
> to_find}
> is:
> {dataset_id}
> else:
> print (f"No dataset
> with the
> name
> {dataset
> name
> to_find}
> found。
> Ihe ID for
> ESG
> SCOLeS
> is:
> analystll
> Ihe ID for
> ESG
> SCOreS
> is: analystll
> COm/
> get

- 后续可能改进方向：研报提到了可以通过市值对数中性化和五组分层进行多空组合。本人不太了解如何使用operator进行这些操作，尝试过使用对logcap 进行bucket分组再group中性化，但是效果不佳。欢迎大家指导。

---

### 评论 #26 (作者: HW97336, 时间: 2年前)

1、performance面板

这是在美国市场上的Alpha，在中国市场上只提交过一个Alpha，所以这次尝试在构建中国市场上的量价Alpha


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click
> drin down
> Anh
> 01 |
> NJyldT
> ug
> FuralrnWlluia
> SrlllorUII
> Roner14


2、新的《Alpha灵感》文章链接：

[【Alpha灵感】隔夜“拉锯战”和渔利因子](http://support.worldquantbrain.com[L2] 【Alpha灵感】隔夜拉锯战和渔利因子_20251308691735.md)

3、寻找template

首先对于这种量价Alpha提取模板有些困难，一方面是这个Alpha的思路是隔夜和盘中的价格矫正过程，因此似乎不能放弃“隔夜”和“盘中”这两个概念，而隔夜涨跌和盘中涨跌只对于可交易金融资产有效，另一方面是数据集可替换性不大，基本上是开盘和收盘的某个指标，我归纳的template如下：

```
ret_oc = C/O-1;ret_co = O/ts_delay(C)-1;NR = ts_sum(ret_co>0&&ret_oc<0?1:0,22)/22;PR = ts_sum(ret_co<0&&ret_oc>0?1:0,22)/22;group = bucket(rank(cap),range='0,1,0.1');group_neutralize(rank(NR)+rank(-PR),group)
```

其中C表示收盘指标，O表示开盘指标，原文主要思想是隔夜投资者和盘中投资者的对抗，盘中投资者倾向于过度矫正“错误定价”，之后会出现回归现象，NR衡量了盘中投资者过度压低价格的比例，回归意味着涨，因此是正向因子，PR衡量了盘中投资者过度抬高价格的比例，回归意味着跌，因此是负向因子

我先在A股市场复现了研报，成功提交，之后通过搜索“open”和“close”，发现了一些适用于美国的option和news方面的数据，但并不多（中国几乎没有），而且不能两两随意组合，否则没有意义，所以手动配对了数据，最终试了10组，都无法提交，有两组有明显信号，都是价格数据，但是需要手动优化，这个模板不好扩展，也许像开盘收盘的期权隐含波动率或者期货的价格可以一试，但是并没有找到数据。

4、这是中国市场上成功提交的Alpha


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
> Fitness
> Tag
> Search
> Selec
> Selec
> Selec
> Search
> Selec
> Selec
> e.吕>1
> e.g>1
> e.8>
> e.g>1
> Selec
> anonymoUs
> Regular
> ACTIVE
> 12/31/2023 EST
> CHN
> T0P3000
  
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 80OK
> 5,00OK
> 4,0OOK
> 2,00OK
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan'16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21



> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.64
> 7.789
> 2.49
> 11.109
> 4.999
> 28.519600
  
> [!NOTE] [图片 OCR 识别内容]
> OS Testing Status
> 11 PENDING
> Sub-universe Sharpe check pending:
> Rank sharpe check pending:
> Drawdown check pending。
> Sharpe check pending:
> New high check pending。
> Memory usage check pending:
> Super-universe Sharpe check pending:
> IS sharpe check pending:
> Weight concentration test pending_
> Production correlation check pending:
> Self-correlation check pending:


5、总结

本周规范了自己的代码库，单独写了一个模板生成的函数，添加了检测是否能提交的函数，以及把提取alpha的信息和模拟alpha分离开

对于模板前面也已经提到了一些想法，我想知道这种模板能不能突破隔夜和盘中的概念，改成其他可扩展的形式呢？以及这次的模板不能直接机械地排列组合，效率太低，一些无意义的组合（比如期权价格收盘价和开盘新闻情绪值的组合）大概率不会有好的表现，因此还是需要人为地组合同一类的open和close，显得有点笨拙，不知道有没有什么好的建议

---

### 评论 #27 (作者: XC63878, 时间: 2年前)

**1.Performance**  **面板截图**

**
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Clicktodnlldown
**

**2.Alpha**  **灵感**

链接： [【Alpha灵感】将隔夜涨跌变为有效的选股因子]([L2] 【Alpha灵感】将隔夜涨跌变为有效的选股因子_20252684454295.md)

idea：在隔夜涨跌幅的基础上，利用成交量的信息，计算隔夜涨跌幅与昨日换手率的相关系数。通过两者的相关性来衡量知情交易者和市场有效性的强弱。

数据：open、close、pv27_turnover_d

Universe: CHN TOP3000

Neutralization：subindustry

**3.Template**  **分析**

corr = ts_corr(A,B,20);

group_neutralize(corr, bucket(rank(cap), range="0, 1, 0.1"));

该模版考虑两个变量之间的相关性，通过这种相关性来反应市场的某种性质或者某一类股票的性质。

**4.**  **成功提交的Alpha**

**
> [!NOTE] [图片 OCR 识别内容]
> 囱囟 IS Testing Status
> 10PuSS
> Shurpc or240
> ObOCCuoftof 2.07.
> Firess 012
> AbovC Cutoffor
> Turnoveror 13.645
> C
> Cuoffof 1%
> Turnoer or 13.645
> beloCuor
> 709
> WeEhE
> WeldisribucJornsumn;
> Reurrs
> 4896
> Jbo
> Sub unNCrse ShorPCOf2.33
> UCt
> CUOAfOf 1.47.
> Robust UrNCrse ShATDC 011.13
> ObOC CUEOAot 0.96 (-04oi Alphol
> RobJstUrnr-
> TCUTT5
> 519
>  
> CUtofof 3.799(40*or Aphol
> ladder Sharpe or265
> 022
> Cutotior237+orIddryeor2 2/18/2021.2/19/2019
> AJd Alphato
> Uis
> Openalphadetals
> Te4 T
> Check Submission
> Submit Alpha
> CUO
**

**5.**  **总结**

本次作业尝试了好几篇论文/研报，存在以下问题

（1）论文/研报本身的灵感很好，但难以在BRAIN平台上找到所需要的数据集，导致无法复现；

（2）论文/研报本身的灵感很好，也能较好地复现，但很难通过prod_corr检测；

（3）论文/研报本身的灵感很好，但复现的效果并不理想。

大多数是第（2）种情况，对于这种情况，如果只是利用machine替换相关变量，仍然还是无法通过prod_corr检测，可能对运算符进行替换的效果更好一点。对于第（1）种情况，可以通过替代变量去构造所需要的数据，但能满足的还是少数。而且自己对Fields确实不太熟悉，有些Fields的Description很笼统。对于第（3）种情况，可能是论文/研报中的某些细节没有写出来，导致无法精确的复现，但论文/研报所表达的经济学原理和逻辑也是很有价值的。

---

### 评论 #28 (作者: SL57524, 时间: 2年前)

1. Performance面板截图，选择相关方向的文章


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> USA
> EHN


2.《Alpha灵感》文章

[【Alpha灵感】Research Paper 22 Overnight returns, daytime rev...]([L2] 【Alpha灵感】Research Paper 22 Overnight returns daytime reversals and future stock returns_20239918193303.md)

[【Alpha灵感】 计数启发法]([L2] 【Alpha灵感】 计数启发法_20237862981399.md)

[【Alpha灵感】东吴证券的几种换手率因子]([L2] 【Alpha灵感】东吴证券的几种换手率因子_20255074372375.md)

3. Template分析，阐述其抽象后可以提取什么信息，不同条件下的搜索空间可能有多大，有什么独特的操作，适用什么universe,周期等。

我尝试的这3篇文章可以提取到2个Template：

第一个来源于 [【Alpha灵感】Research Paper 22 Overnight returns, daytime rev...]([L2] 【Alpha灵感】Research Paper 22 Overnight returns daytime reversals and future stock returns_20239918193303.md) ：

找到某种可以代表“异常”的指标，异常是由于两种状态的连续所体现，对于这种异常分别在月的层次进行计数，用年的层面作为基准值进行比较。

第二个来源于 [【Alpha灵感】 计数启发法]([L2] 【Alpha灵感】 计数启发法_20237862981399.md) ，就是针对投资者可能会关注的某个指标，当这个指标相比整体表现超过一定阈值的时候加入计数，在过往的时间段里总和这些技术，加权时注重权重的衰减。这个template可以提取一些股民/机构可以直观/比较经常关注的信息。除了原文的量价指标，目前认为在“新闻”方面这个template可以发挥用处，目前正在用machine对新闻进行搜索，其他量价数据没有搜到可以通过检验的。

关于计数启发法，帖子底下有一些老师同学的留言，我会重新向这些方面尝试优化。

这两个Alpha灵感有相似之处，但是我觉得我所提取的东西并不够抽象化，我感觉找到一个能用的（高成功率）的抽象化模版并不容易，比如老师课上所言的“2次提纯”，这个东西看起来既一定实际意义，又感觉很玄学。

现在我能做的用Machine辅助自己 只能是有明确数据方向的尝试，更像是一种调参，而不是一种Template。

4. Alpha截图


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


这个alpha来自 [【Alpha灵感】Research Paper 22 Overnight returns, daytime rev...]([L2] 【Alpha灵感】Research Paper 22 Overnight returns daytime reversals and future stock returns_20239918193303.md) ，但无论如何改进都无法通过correlation，不知道能不能算勉强完成本次作业。

5. 总结反思

最大的反思在于为什么无法找到可以提交的Alpha

（1）

我发现在USA市场，从论坛的research paper中找到论文，有一些被大家做过的比较多，有一些比如和ESG相关的 ，只在最近几年效果比较好。如果在SSRN上找JFE和J F的这种论文，不知道到底该如何搜索，很多搜出来的论文并不是论坛那种数据鲜明的实证资产定价文章，又有很多论文用的数据都是创新性难以复现的。

在CHN市场，研报方面，Wind等找到的研报很多都是高频的，这些“分钟”数据我尝试迁移到低频但是基本做不出来（希望未来老师可以提供一些迁移的策略、例子），剩下的研报除了那种“N个相似类的因子效果检测”，大多数做出来都是correlation很高的。当然我也看到评论区很多同学都能做出来很好的结果，我认为还有以下几条的原因。

（2）对Fast Expression 和 dataset 不够熟悉。除了阅读论文，我尝试过程中大多数时间花在了如何写fast expression 上，而且常常写出来的表达式无法准确表达文章观点。也因为这个原因，我对Alpha的改进不能得心应手，无法完整的根据一种猜想——验证的逻辑 去细节上、符号上挖掘alpha的本质表现，比如像在 [【Alpha灵感】A股换手率类因子](../顾问 WX84677 (Rank 69)/[Commented] 【Alpha灵感】A股换手率类因子.md) 中老师所示范的那样。我近期会对所有Fast Expression操作符系统学习一下，借Office Hour的机会攻克这一部分问题。

（3）

近期通过《因子投资 方法与实践》这本书对整个因子投资有一定全貌的认知，包括这些天找论文、研报，对常见的分组排序，Fama Macbeth 回归检验， 提纯之后纯净因子表现，正交化等有一定的认知，知道这类论文、研报的论证思路和方式。

希望老师课上可以讲述一些 关于我们的Alpha提交之后，在Protfolio Manager那边如何组合的一些介绍，以及这种组合和SuperAlpha的相似点，从而完善对于因子投资的全貌了解。

---

### 评论 #29 (作者: FL11741, 时间: 2年前)

1.如图，这次在option，analyst和sentiment方向都有尝试 
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> Alphas
> USA
> Delay
> Price Volume data
> Model data
> Fundamental data
> Other
> Social media data
> News data
> Option data


2. [【Alpha灵感】 Implied Volatility Skew – WorldQuant BRAIN]([L2] 【Alpha灵感】 Implied Volatility Skew_20255825146647.md)

Template分析：

仅就这篇post的template而言，还是比较浅显死板的：

(put_vola-call_vola)/(put_vola+call_vola) 将其中put_vola和call_vola换成不同的时间段和strike level，没有抽象化的提升。我只想到根据相关研报尝试不同表达式，例如Put Call Ratio等。

另外根据另一篇研报，得到了一个抽象的不错的模版：

λ = ESG ratings， sentiment ∈ [ -1 , 1 ]

（1 + λ * sentiment）*（1 + λ * negative sentiment）

做了一些尝试，结果发现我跑的ESG ratings数据字段有信号的都在疫情期间栽倒了LoL，所以没有采用那一篇，其他ESG相关的不是打分类型的数据的暂时没有进一步尝试。

4. Post的correlation过高了，暂时没有进一步降低的计划，不过我另起炉灶交了几个 
> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Sharpe
> Returns
> Turnover
> Fitness
> Color
> Search
> Selec
> Selec
> Selec
> Search
> Selec
> e.g>1
> e.吕>1
> e.吕>1
> @.8〉1
> Selec
> anonymous
> Regular
> ACTIVE
> 12/31/2023 EST
> USA
> anonymous
> Regular
> ACTIVE
> 12/29/2023 EST
> USA
> anonymous
> Regular
> ACTIVE
> 12/27/2023 EST
> USA
> anonymous
> Regular
> ACTIVE
> 12/27/2023 EST
> USA
> 210
> Regular
> ACTIVE
> 12/27/2023 EST
> USA
> Purple


5. 总结与反思：

在case2中遇到的主要问题：

1. 时效性：研报策略在疫情期间失效，甚至有巨大回撤。
2. 数据集与策略复杂性：一些研报的策略公式非常复杂，相应对数据集要求也非常苛刻。例如在实现分析师预测分歧中蕴含的alpha时，按照研报策略需要对同一分析师的基本面数据预测做追踪得到时序数据，再在分析师之间做随机森林回归，但这些可能在平台上较难实现。我选用了分析师预期标准差作为简单替代，有一定信号，但不足达到以提交标准。
3. 对自己不常用的数据方向的不熟悉：缺少对其他方向的基本逻辑和知识的整体认知给我在读研报以及尝试实现带来了很大阻力，希望在期末过后能够投入更多时间精力去学习了解。

关于程序实现上的进展：

上次pre中提到的simulation单独做成程序已经实现，核心思路是将simulation和get result放在两组子进程中，主进程用于用户交互。交互方面可以实现读取新数据进行插队或者正常排队，simulation和get result的开始、暂停、停止功能，以及实时进度的手动刷新。能够满足包括断网，自动登出，计算机睡眠等断点续接情况，意外关闭会丢失前50个待测simulation data和alpha id（可以规避但考虑到潜在的运行效率问题就不做实现了），并将目前我还未知的异常情况写入错误报告中并将simulation data分类为错误表达式或未知错误并返还。总之，现在已经能满足simulation高效率连续运行超过一天。已知问题：get result除了correlation一小时上限150次以外，在加了进程锁和sleep延时后依然偶尔会得到status code 429，在跑universe较小的simulation时，可能导致get result速率追不上simulation。

---

### 评论 #30 (作者: WL13229, 时间: 2年前)

[FL11741](/hc/en-us/profiles/18515544005527-FL11741)

同学您好，看到您写道“由于数据集缺失不同strike level下的成交量及open interest数据，并不能够还原”。

建议您多多尝试，在BRAIN平台有着非常多的option数据，尤其美国区域中option4和option6这一数据集是非常全面的。您说的数据，我本人都有做过，建议多多探索。

---

### 评论 #31 (作者: AZ81686, 时间: 2年前)

1. Performance面板: 可以看出，期权数据，我选择阅读期权方面的论文 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> USA
> Delay 1
> News data
> Analyst data
> Modeldata
> Othep
> Socal media data
> Rrice Volume data
> Fundamental data
> Sholt Interest data
> @ptfon data
> Earnings
 2.《Alpha灵感》文章: 【Alpha灵感】Volatility Spreads and Expected Stock Returns

3. 核心template

```
spread = x_of_A - x_of_B
```

抽象来看，A和B可以是两种方向相反的东西，在论文中是call和put；或者也可以是有lead-lag关系的东西，如realized volatility和implied volatility; 这里面x需要相同是保证比较的是同一个东西，如波动率，才有“经济学含义”

4.成功提交 
> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> ACTIVE
> 01/02/2024 EST
> USA
> ILLIQUID_MINV.


5. 反思疑惑：在尝试过程中发现market / sector中性化的结果比industry/subindustry的表现要好；在可视化分析中可以看到一些行业的pnl表现突出，一些行业的avg size稍大；意味着因子对行业存在暴露；这种暴露是应该坚决消除的？还是可以作为一种smart择"行业"的方案？ 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Average Size By Industry
> Office Furnishings
> Internet
> Alternative Energy
> Biotechnology
> Coal
> Pharmaceuticals
> Investment Companies
> Oil & Gas Services
> Pipelines
> Oil & Gas
> Office & Business Equipment
> Transportation
> Mining
> Advertising
> Software
> Electric
> Chemicals
> Commercial Services
> Healthcare Services
> Internet
> Iron & Steel
> Biotechnology
> Banks
> Forest Products & Paper
> Retail
> Pharmaceuticals
> Packaging & Containers
> Media
> Insurance
> Electronics
> Household Products & Wares
> Diversified Financial Services
> Metal Fabrication & Hardware
> Beverages
> Healthcare Products
> REITS
> Leisure Time
> Semiconductors
> Oil & Gas
> Machinery Construction & Mining
> Miscellaneous Manufacturing
> Auto Parts & Equipment
> 1/3
  
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl By Industry
> 5,00OK
> 2,5OOK
> 2012
> 2014
> 2016
> 2018
> 2020
> Pnl : 2
> Software
> Electric
> Chemicals
> Commercial Services
> Healthcare Services
> Internet
> Iron & Steel
> Biotechnology
> Banks
> Foroct Prndiirtc 又 Panor
> 1/8


---

### 评论 #32 (作者: WL13229, 时间: 2年前)

[AZ81686](/hc/en-us/profiles/14380385958679-AZ81686)

这样的思考非常深入，是我们乐于见到的。我们不妨从另外一个角度来看看这个问题。

1. 在尝试过程中发现market / sector中性化的结果比industry/subindustry的表现要好。

这个观察，我认为和图片相印证后，应该可以得出一个推论：在neutralization之后，你的Alpha目前可能将仓位更多地集中到了某些行业。你可以使用一个group_rank，会得到类似的验证。

2.进一步的思考。

```
spread = x_of_A - x_of_B
```

如果你不加任何平滑的话，这个值可能在某些行业就是会很高的。例如如果我们在全市场的角度讨论资产负债率，那么银行业的整体资产负债率就是很高的。可能全市场资产负债率最高的100家里，有70家都是银行业的公司。那么当你在使用Market Neu的时候，实际上你只是选择了做多某些行业，然后做空某些行业指数。当然，需要点赞的是，这个Alpha也对其精选出来的行业做了合理的资本权重分配，否则不会有很好的IS表现。

这当然也是一种投资的方式，这种方式也是无可厚非的。但是，你需要考虑的是，这是不是你想通过本Alpha实现的目的？如果您只想拥有一个获得好的IS回报的Alpha，那么恭喜你，你已经实现了这个目标。如果你是想通过spread，在每个行业中都识别出“好股票”和“坏股票”，那么这个任务是还没有完成的，还有工作要做。

总结来说，并没有说“这种暴露是应该坚决消除的”。而应该是，我们去了解了这个Alpha在做什么，怎么赚钱，它的特性是什么。这样我们才可以在后续做SuperAlpha的时候，取得预期的效果。

毕竟，我们所作的所有工作，都是为了获得一个“近似于或者好于IS表现的OS”

---

### 评论 #33 (作者: ML15895, 时间: 2年前)

1.  **Performance面板截图** ：比较空白，所以没有限制什么方向。


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> Model data
> Fundamental dafa


2.  **[[Alpha灵感]凸显理论](../顾问 MQ62208 (Rank 29)/[L2] 【Alpha灵感】凸显理论Salience Theory.md)** ，浏览了Brain平台上的alpha灵感合集，再结合网上随机搜索，随机找到了这几篇研报，平台上类似思想的Alpha灵感是 [这篇]([L2] 【Alpha灵感】根据草木皆兵因子的文字描述进行量化实现_19298826598423.md)  （估计也是prod corr高的来源）

3. T **emplate**  **分析及探索：**

- 从Alpha灵感中的初步实现的结果分析，可以看到STT2效果最好，于是选取这一模式，我理解的是凸显理论可以抽象理解成寻找因子偏离均值的异常值，再根据这些异常值权重和因子的协方差进行多头和空头的选取 template的表达式为：
  ```
  delta=0.7;theta=0.1;factor={datafield}; market_factor = group_mean(factor, 1, market);sigma = abs(factor - market_factor) / (abs(factor) + abs(market_factor) + theta);days = 22;k = ts_rank(-sigma, days)*days;k_1 = if_else(k==0, 1, k);weight = power(delta, ts_rank(k_1, days)) / ts_mean(power(delta, ts_rank(k_1, days)), days);ST = ts_covariance(weight, factor, days);signal = group_neutralize(zscore(-ST), bucket(rank(cap), range="0, 1, 0.1"));signal
  ```
  其中{datafield}为datafield，主要用到category==pv的价量数据，也尝试使用了analyst数据，如果是vector，先使用vec_sum进行降维。
- Template更新历史：
  1) 初步的Template通过IS的测试的不多，只有一个，是价量数据，所以简化模版再尝试，首先想到简化凸显性排序的计算，不改为整数，直接取[0,1]+1，这样的结果是测试速度加快，通过IS测试的个数增加。暂时放弃分析analyst数据，主要针对价量数据。
  2) 顺着这个方向将weight计算和最后的标准化排序调换顺序，进一步简化操作，同时发现vec_vag会更有效一点，所以改用这个操作符进行降维。
  3) 由于初始模版是月频调仓，不知道怎么在Brain平台上实现，所以在计算因子凸显性的时候直接选取截面rank，得到这个模版之后，可以通过IS测试的数量增加到十个左右，但是由于这个alpha主要用到价量数据，可提交的数据字段主要和成交量和换手率有关，prod corr均超过0.75。
  这个版本下的模版是
  ```
  delta=0.7;factor = {datafield}; weight = power(delta, rank(factor)) / ts_mean(power(delta, rank(factor)), 22);ST = ts_covariance(weight, sigma, 22);signal = group_neutralize(zscore(-ST), bucket(rank(cap), range="0, 1, 0.1"));signal
  ```
  可以得到如下结果，可惜还差一点就可以提交，而且corr>0.7， alpha表达式和结果如下
  
> [!NOTE] [图片 OCR 识别内容]
> Simulation 1
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> CHN/D1/T0P3000
> Convert to Multi-Simulation
> delta=0.7;
> sigma
> Vec_avg (pvz7_buy_value_small_order) ;
> 2SM
> weight
> power(delta,
> rank(sigma))
> ts_mean (power (delta,
> rank(sigma) ) ,
> 22);
> ST
> ts_covariance (weight,
> sigma,
> 22) ;
> signal
> group_neutralize (Zscore (ST) ,
> bucket
> rank(cap)
> range="0,
> 1,
> 0.1") );
> 2OM
> signal
> 15M
> 10M
> 5,0OOK
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
> Clone this Alpha in a new tab
> 吝
> 3.36  12.5195.3231.34911.53%50.12%o。
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> PASS
> FAlL
> Robust universe returns Of 10.34% is below cutoff of 12.54% (40% of Alpha):
> 3 PENDING
 4) 根据sharpe排序找了上面这个结果之后，感觉这个信号真的还不错，感觉放弃有点可惜。所以这两周没有放弃一直在尝试，之前主要是在TOP3000选股，然后试了一下2000也有差不多的信号，突然想到如果是小市值的股票，凸显性有没有可能会更明显。于是使用trade_when 通过rank(cap)选取小市值股票，然后修改group_neutralize的group最终获取一个可以提交的alpha，表现截图如下:
  
> [!NOTE] [图片 OCR 识别内容]
> 2SM
> ZOM
> 15M
> 10/20/2015
> IS Pnl。 13.61M
> 1OM
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
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.48
> 20.329 4.50 33.93929.05933.409o。
  
> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Highest Correlation
> Last Run: Wed, 01/03/2024,3:29 PM
> 0.7
> I0Ok
> IOk
> 寰
> Ik
> 昱
> 100
> %
> 10
> 8?
> 09
> 09 0?0?0?0^0? 0o 0?
> 09 ^9
> 0?"
> 0一
> IS Testing Status
> 13 PASS
> -0.9
> -0.7
> -0.5
> -0.4
> 0.8
> -0.3
> -0.2
> -0.1
> 0.4..
> 0.1. _
> 0.2..
> 0.7 ..
> 0.8.
> 0.9.
> $
> 0.0.
> 0.5.
> -1.0
> -0.9.
> -0.8.
> -0.7 
> -0.6.
> -0.5.
> -0.4.
> -0.3..
> -0.2..


4.  **提交截图** ： 
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
> STR
> Regular
> ACTIVE
> 01/02/2024 EST
> CHN
> TOP3000
> Tag


5.  **总结反思** ：

- 功能提升：增加批量获取alpha中通过IS以及corr测试的expression
- 模版适合的数据类型以及改进方向：目前看来是用于价量数据，同时看到评论区有同学是用ts_corr(A,B,d)的模版更抽象，考虑直接抽象成ts_covariance(A,B,d)，不过目前还没有尝试，同时考虑替换group_neutralize的group字段
- 反思总结：
  1）对于template的抽象还需要努力，经验不足导致不知道该怎么抽象，所以template比较复杂。
  2）没有实现两个或者多个datafields组合，搜索空间有限。思考：如何进行group字段的提取。
  3）看到有信号但是prod corr高，甚至产生>0.9的prod corr，我想这说明这是一个实现简单，并且比较有效的因子，作为初学者可以积累一些这方面的素材，所以还是决定死磕这篇研报，最终也找到可以提交的因子还是比较高兴的。缺点就是时间花费太多，可能会错过一些机会。Brain平台上也有提到reduce prod corr的 [帖子](../顾问 PN39025 (Rank 87)/[L2] [BRAIN TIPS] How do you reduce correlation of a good alpha.md) 。希望自己能够继续努力，与君共勉。

---

### 评论 #34 (作者: WL13229, 时间: 2年前)

@ [OA92025](/hc/en-us/profiles/18197007430167-OA92025)

同学您好，本次课程的要求是。发一篇新的idea post。您没有在本次作业的时候发新的post,请关注此问题。

---

### 评论 #35 (作者: AZ81686, 时间: 2年前)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)

关于“

```
spread = x_of_A - x_of_B
```

如果你不加任何平滑的话，这个值可能在某些行业就是会很高的。”

进一步发展，可以想象，如果我们是想用spread = call的隐含波动率 - put的隐含波动率来作为“情绪方向”的话，会有有个问题就是波动率均值大的股票/行业，计算得到的spread也是相对较大；那么从收益来源的角度，其实这个spread不仅赚的是情绪方向判定的钱，还take了大波动率本身的risk (进而risk premium)

---

### 评论 #36 (作者: WL13229, 时间: 2年前)

[AZ81686](/hc/en-us/profiles/14380385958679-AZ81686)

确实如此，所以在visualization的界面就看到了对某些行业的结果。看看有没有提供capital by sector的图像。或许会有更多启发

---

### 评论 #37 (作者: 顾问 KZ79256 (Rank 21), 时间: 2年前)

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

### 评论 #38 (作者: WL13229, 时间: 2年前)

[顾问 KZ79256 (Rank 21)](/hc/en-us/profiles/13609593802263-顾问 KZ79256 (Rank 21))

看得出来做了有用的工作，才把corr降下来的。值得学习交流。均值加上标准差，即得到一个标准差之后的值。这个Alpha的本质似乎是对某个特征，基于某个条件，进行大小的调整。

---

### 评论 #39 (作者: YW27566, 时间: 2年前)

1.Performance面板中基本面数据较多，尝试使用其他方向的较另类数据  
> [!NOTE] [图片 OCR 识别内容]
> AIII1s
> US
> Prlce Volume data
> TIIH1t
> (OolUSA Dely
> No Imits Ior dala catcgorics wth <30 Alphas。
> Prce woume dt
> Maipldl
> GundamenUL data
> Nes1
> Opliondl
> Delay


2. 发布的alpha灵感链接： [[L2] 【Alpha灵感】Option-Implied Volatility Measures and Stock Return Predictability_21110734836887.md]([L2] 【Alpha灵感】Option-Implied Volatility Measures and Stock Return Predictability_21110734836887.md)

skew=opt4_273_call_vola_delta25-opt4_273_put_vola_delta50，遍历得出较长的期限，otm call和atm put的组合方式效果更好

3.template: alpha=zscore(A-B);regression_neut(alpha,log(cap));regression_neut(alpha,log(volume))

4. 提交截图：


> [!NOTE] [图片 OCR 识别内容]
> option_skew_al
> Regular
> ACTIVE
> 02/04/2024 EST
> USA
> TOP3000


5. 总结反思：对因子进行提纯，标准化，中性化设置等操作后有助于改进alpha，需要针对alpha特点多进行尝试。不合适的提纯，分组方式会削弱alpha表现

---

### 评论 #40 (作者: WL13229, 时间: 2年前)

[YW27566](/hc/en-us/profiles/18162425397783-YW27566)

谢谢分享。请问Template是这样吗

> alpha=zscore(A-B);regression_neut(alpha,log(cap));regression_neut(alpha,log(volume))

如果是这样的话，中间对于cap的提纯是没用上的，因为它的结果没有被一个变量承接。最后您的Alpha和下面这个是一样的。

```
alpha=zscore(A-B);regression_neut(alpha,log(volume))
```

---

### 评论 #41 (作者: ZF71008, 时间: 2年前)

1. Performance 截图 
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Cickto drilldown
> MI
> Dely 1
> RICeOIUC Jla
> Oonu
> Furdamentaldo
> Uoueldl


新手上路，目前我提交的alpha很少，下一个策略的选择空间很大，但是model data相对较少，因此这篇笔记从这里下手搜索相关research paper。

开始的时候在平台dataset相关说明里找model相关data，主要检索了cash flow相关的几篇文献，但是其中有一篇提到一句（也有可能是误解了） cash flow相关因子可靠性有争议，自己也没能总结出什么有价值的表达式，就放弃了这个方向。正巧论坛新post了《量化研究推荐论文》这个版块，真的是非常便捷。花了些时间阅读了Research Paper 52: Skewness Preference and Market Anomalies。有些因子测试无法通过corr测试，后来发现论坛此文已经被挖掘过了。为了避免重复，最后选择了这篇文献提到的一篇引用，其中涉及了一种衡量异常的方法：JACKPOT.

引用文献如下：

Conrad, Jennifer, Nishad Kapadia, and Yuhang Xing, 2014, Death and jackpot: Why do individual investors hold overpriced stocks?, Journal of Financial Economics 113, 455–475.

1. 提交：

《Alpha灵感》JACKPOT因子

[[L2] 【Alpha灵感】JACKPOT因子_21119177808663.md]([L2] 【Alpha灵感】JACKPOT因子_21119177808663.md)

1. Template分析：

我目前的理解，JACKPOT因子实际上是构建alpha的一部分，可以和很多其他因素一同构建为一个完整的模板。比如上面提到的Research Paper 52: Skewness Preference and Market Anomalies中，可以构建 MIS * JACKPOT 模板。所以搜索空间还是还是很大的，后续我会继续在USA market/D1 尝试挖掘。

1. 成功提交一个alpha，在《Alpha灵感》JACKPOT因子中有部分截图


> [!NOTE] [图片 OCR 识别内容]
> JCLOnUTLTUFR
> TeEular
> ACTIL
> 020-202-EST
> ILLIOUID_



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 4B
> GOOD
> Total Unsubmitted Alphas
> 8,382
> Total Active Alphas
> 14
> BCELENIT
> SFLCTLCULAA
> Total Decommissioned Alphas
> Total Alphas
> 8,396
> 0.46
>   英  拼
> 谷 q
> 匈
> 2024/2/5
 之前的截图：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 3,281
> Total Active Alphas
> 13
> Total Decommissioned Alphas
> Total Alphas
> 3,294
> 8.36
> ^  英  拼 谷 C V
> 2024/1/30


1. 总结反思：

从文献中总结表达式的能力还很欠缺，需要熟悉对operator以及dataset的使用。接下来准备尝试训练一下chatgpt来辅助总结研报的能力。

---

### 评论 #42 (作者: WL13229, 时间: 2年前)

[ZF71008](/hc/en-us/profiles/20098272506775-ZF71008)

谢谢这位同学的分享。可以分享一下您的《Alpha灵感》JACKPOT因子的链接吗？这会帮助我们尽快Approve这篇帖子。

---

### 评论 #43 (作者: DK85731, 时间: 2年前)

- Performance 截图
- 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Distribution of Active Alphas
> Click to drill down
> Alphas
> USA
> Delay
> Price VOlUNe data
> Fndamental data
> Opton dala
> Newsdata

- Alpha灵感:  [[L2] 【Alpha灵感】Improved Version of Attention Implied Volatility Spreads and Stock Return_21120326355479.md]([L2] 【Alpha灵感】Improved Version of Attention Implied Volatility Spreads and Stock Return_21120326355479.md)
- 模板分析与表现见于 Alpha 灵感文中
- 反思：在撰写本篇评论时无意间发现上期有同学使用了类似的题目 :【Alpha灵感】Volatility Spreads and Expected Stock Returns , 预计前篇同学提交的alpha为同一赛道，导致我有很多因子被一个alpha卡在了0.7的corr ：(。 但细细看来内容也不尽相同，我选取的论文为在之前 Volatility Spreads and Expected Stock Returns 的基础上，运用其他信息进一步优化  。但与此同时，我也发现即使主要因子类似，但在通过其他有效因子进行filter之后，corr也会出现显著降低，故在一些常用因子的基础上使用不常使用的data field进行优化应该也是一个值得尝试的方向。

---

### 评论 #44 (作者: SK24143, 时间: 2年前)

1.performance面板截图


> [!NOTE] [图片 OCR 识别内容]
> Distribution Of Active Alphas
> Click to drill down
> USA
> 11 alphas
> (85% ofall Alphas)
> USA
> CN


由于是新手小白，提交的不多，CHN提交的相对较少，最终选择了东吴证券的一篇研报

2.《Alpha灵感》新价量相关性RPV因子  [《Alpha灵感》新价量相关性RPV因子 – WorldQuant BRAIN]([L2] 【Alpha灵感】新价量相关性RPV因子_21120825510551.md)

3. 这个template感觉并不太好进行泛化，因为它考虑的是日内和夜间的一个共同作用，但是我还是试了一下抽象化，试图找到一些与夜间收益率相关的量，其中主要是volume相关的，但试了感觉不太好。

change = open-ts_delay(close,1);

a = ts_corr(change,volume_datafield,60);group_neutralize(a,bucket(rank(cap),range='0,1,0.1'))

4.alpha截图


> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> ACTIVE
> 02/05/2024 EST
> CHN
> TOP3000


5.总结与反思

代码方面加上了转化vector的一个函数。在模板方面从研报中得出的太过具体，感觉不好泛化，以后要进一步提高抽取模板的能力。在找论文的时候发现有些观点很难实现，所以感觉找好论文和研报也很关键。下一步准备寻找更多的论文和研报进行尝试，进一步加强实现各种复杂的fast expression的能力，以及提高模板提取能力。

---

### 评论 #45 (作者: YZ64617, 时间: 2年前)

Peformance截图

在开始作业之前，没有 alpha。

现在的


> [!NOTE] [图片 OCR 识别内容]
> Q Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Distribution of Active Alphas
> Click to drill Oown
> USA


alpha灵感： [【Alpha灵感】Non-Linear Factor Returns in the U.S. Equity Market – WorldQuant BRAIN]([L2] 【Alpha灵感】Non-Linear Factor Returns in the US Equity Market_21126691730839.md)

这篇论文的非线性公式，可以适用于5类factor，我目前只实验了P/E和PM，另外3种完全没有时间去尝试。

公式模板就是按照论文创建创建一个factor，然后使用这个factor，创建3个纬度的变量；之后，将3个变量权重相加。【注意】权重可能是负数，所以，我是通过尝试，确定了第3项是负的。

```
a = 1/PE类datafield；（倒数，构成factor。price momentum则是log）根据论文公式，创建出s1，s2，s3（有完整版，有简化版）signal = s1 + s1 - s3
```

如果需要，可以使用grouping。我使用了下面这种

```
group = bucket(rank(cap), range="0, 1, 0.1");s = group_neutralize(a, group);
```

我通过datafield搜索PE和PM的所有相关数据，获得

- PE-Matrix数据：4147
- PE-Vector：1259
- PM-Vector：541
- PM-Matrix：1541

经过测试universe=Slow Factors表现会更好。USA TOP3000 （ILLIQ效果也不错）。

基于上面这些datafield，一共生成了14968个alpha，截止目前，完成了8900个，耗时21小时，还在跑。也许是因为alpha略微复杂了一点，速度明显比之前刷了1万次模拟慢了很多很多。

目前有100左右通过IS Testing，但是，死在了self corr上，因为我已经提交了2个alpha。对于PE数据，Product Corr和Self Corr是两大难题。不过已经满足，每一个dataset中的PEdatafields是相关度很高的，所以也造成了这样的结果。不过，等所有alpha都跑完，其他dataset的alpha应该还会有几个可以提交。

这周，提交了3个alpha


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST]
> Region
> Universe
> Returns
> Turnover
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.5 >
> 巳.5>1
> 巳.5>1
> SeeC
> anonymous
> Regular
> ACTIVE
> 02/04/2024 EST
> USA
> TOP300O
> mdl77,
> anonymous
> Regular
> ACTIVE
> 02/04/2024 EST
> USA
> TOP3000
> a0/69,
> anonymoUs
> Regular
> ACTIVE
> 02/03/2024 EST
> CHN
> TOP300O
> md1122,
> Sharpe
> Tag


### 

### 思考和一些感想

需求越来越多，所以，考虑整理和优化一下python的函数功能。例如，根据settings或/和search词找dataset和datafield；当大批量simulation的时候，定时或者人工触发从IS alpha中找到alpha的结果，尤其是通过IS testing的；Check simulation和检查corr的函数（没想明白这些返回值应该处理到什么程度）

在手工调试alpha的时候，一点点摸索出了一些思路。对于模版的通用书写规则，感觉需要固定。例如，alpha可以写出不同层级，初级版a1=一个信号，如果表现不好，升级到第二版：a1=***；a2=function(a1)，之后还可以升级为第三版，还可以添加grouping，而grouping方法还可以有不同的版本。这样，可以编出一套逻辑，通过通用的模版，挖掘alpha。

读论文，收获很大，不知不觉领会了一些技巧。其实，灵感论文是我读的第3篇。第一篇读的是“A Fibonacci Heap based Ensemble Model for Stock Price Prediction”，论坛推荐的论文，同时还推荐的dataset。但是，最后也没有搞明白如何去ensemble dataset.id=mdl122的datafield。mdl122就是一个坑，通过descroption无法获得任何有价值的信息，我试探的跑了9000多个simulation，最高的sharpe是1.5，只能放弃。很好奇其他大神是怎么试探出来的。ensemble有对应的brain的operator可以组合出来吗？

关于alpha的优化，我的这个论文总结出来的公式，还有3类factor我可以尝试。那它的模版，也许套用到其他factor上也会有效。另外，还是对于一些operators理解不深，敏锐度不够。

---

### 评论 #46 (作者: XZ75239, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Distribution of Active Alphas
> Clickto drilldown
> USA
> alphas
> 1% ofall Alphas}
> USA
> CHN


之前提交中国市场基本面相关的因子比较少，于是读了这篇论文《SmallMinusBig Predicts BettingAgainstBeta: Implications for
International Equity Allocation and Market Timing》并在中国市场实践，论文大意是如果前段时间小市值表现得好，那么市场流动性会增加从而导致BAB策略更加奏效？

我在中国市场试了一下做多低beta，做空高beta的策略，并没有奏效，做多高beta反而有信号。然后我加上了前段时间小市值表现得好的条件，然而也并没有奏效。。。

但是我没放弃，联想到最近国内市场，2024经历了2023年的小市值狂欢后开局惨淡，只有国家队拉住的大市值股票让中小值股票既亏alpha又亏beta，很多因子都失效了，本周一还迎来了千股跌停的奇观。我还是很想知道小市值狂欢后，资金去哪儿了，什么策略还能奏效呢？

于是我的template是：returns_c=-group_mean(returns,rank(cap)>0.8?1:0,market)+group_mean(returns,rank(cap)<0.2?1:0,market);

ts_sum(returns_c,5)>0?factor1:factor2

然后试了一系列因子，提交了两个


> [!NOTE] [图片 OCR 识别内容]
> 鬯婴
> Simulate
> Alphas
> Data
> 智 Competitions (4)
> Events
> Leamn
> 号
> Refer a friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> OUt Of 37
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (ESTI
> Region
> Unierse
> Sharpe
> Returns
> Turnover
> Tag
> Search
> See
> See
> See
> Search
> See
> See
> e.>
> e.>
> e.>
> See
> HOMWr?
> RESJlaT
> ACTIVE
> 02/01/2024E57
> CHN
> 7023000
> Homswork
> Regular
> ACTIVE
> 02/0112024 EST
> CHN
> TOPOOO


思考：也许可以再试试当交易集中度过高/市场全面大跌等等情况下因子如何切换能够避过大回撤，同时考虑到中国无法卖空，可以手动构造买股票卖空指数的策略看看真实效果。。

这是我发的帖子。。。

【alpha灵感】小市值狂欢之后什么策略有效？

[[L2] 【Alpha灵感】小市值狂欢之后什么策略有效_21145402272663.md]([L2] 【Alpha灵感】小市值狂欢之后什么策略有效_21145402272663.md)

---

### 评论 #47 (作者: WL13229, 时间: 2年前)

[XZ75239](/hc/en-us/profiles/13987002908183-XZ75239)

不用担心，可以就分享你读的那篇文章，或者尝试了哪些factor。另外，其实自己的idea就已经是一个很好的帖子了，你已经是一个创作人。相信很多同学都会想看到你的分享。

---

### 评论 #48 (作者: WL13229, 时间: 2年前)

[YZ64617](/hc/en-us/profiles/4527497709335-YZ64617)

很高兴你已经逐渐领悟到了一种搜索的方向及尝试通用的搜索方式。这就是Template的进阶版。不过这类的实施，需要在大回测资源和对数据有更多理解的时候，效率更高。

---

### 评论 #49 (作者: EC34309, 时间: 2年前)

1. Performance面板截圖，選擇相關方向的文章

For some reason I couldn't find the original screenshot, but my alpha distribution was lacking CHN market alpha, so I chose a paper focusing on CHN.

1. 【华泰金工林晓明团队】基于遗传规划的一致预期因子挖掘

[[L2] 【Alpha灵感】基于遗传规划的一致预期因子挖掘_21146151322519.md]([L2] 【Alpha灵感】基于遗传规划的一致预期因子挖掘_21146151322519.md)

核心交易idea是什麼？

The change of EPS estimate by analysts positively correlates returns.

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


Insufficient, 3 additional hypotheses are suggested.

1.Combining smart estimate growth with the growth next yr sector percentile earnings provides a view of expected growth against current valuation.

2.A high earnings yield alongside expected sector-leading growth for the next year could signal potential for returns.

3.Changes in Mean of Estimations of Returns on Equity - upcoming 2 years could correlate with return.

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


1. Template分析，闡述其抽象後可以提取什麼信息，不同條件下的搜索空間可能有多大，有什麼獨特的操作，適用什麼universe,週期等。

1. analyst EPS estimate:

A consistent opinion on a prediction by the analyst correlates with return.

Increasing the search space to any analyst prediction.

1. Compounding analyst estimates
2. Compounding estimates with robust fundamentals

It is worth mentioning I originally wish to come up with a complementary alpha to stabilize this alpha using sentimental data, but it seems that it is not easy to come up with a sentiment alpha in CHN that is profitable enough, perhaps suggesting the relative lack of impact in social media compared to other markets.

4.本次作業硬性要求至少成功提交一個Alpha，請提供截圖。

screenshot provided above.

1. 總結反思（程式碼較上次有什麼功能提升、debug經驗、模板適合的資料類型、模板的改進方向等）

Summary of my workflow:

1. Generate alpha ideas from papers and generative AI.
2. Implement those ideas
3. Superimpose alphas with weak correlations

I wasted a lot of them on generating those ideas. I believe this could be improved by solely focusing on the passage that talks about the variables related to returns.

Questions:

1. I believe I still lack the skill to effectively use fast expression, as I still use a limited set of operators. I would very much appreciate any tricks to smooth the curves (ideally lots of them).
2. I also struggle to interpret using residual/vector neutralization, is it correct to interpret that if the residual/unexplainable return implies the stock has excess return which is more than enough to compensate for the risk? Then why not just long the residual instead, but the implementation for the factor model seems to be different.

market_ret = ts_product(1+group_mean(returns,1,market),250)-1;

rfr = vec_avg(fnd6_newqeventv110_optrfrq);

expected_return = rfr+beta_last_360_days_spy*(market_ret-rfr);

actual_return = ts_product(returns+1,250)-1;

actual_return-expected_return

From “Alpha Examples for Silver Users”

I couldn’t understand why this is the correct implementation, I would be very grateful if anyone could give me a detailed explanation.

---

### 评论 #50 (作者: YL37225, 时间: 2年前)

大家好，我本周尝试复现一篇论文的alpha，但是还没有得到可提交的alpha
1.performance面板


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to crilldown
> TIo
> Utlo
> HurJRCCJ
> SooUOeC C


之前提交过的alpha并不多。
2.选择阅读的论文

site:  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2472571](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2472571) 
Are Cash Flows Better Stock Return Predictors than Profits?
3.论文主要说明直接现金流法得到的 Net Cash Flows from Operations after Financing Activities除以total asset，能比较好地预测股票收益。
我的template形式如下：

#data fields

x1=sales;

x2=fnd65_allcap_sedol_salerec;

x3=revenue;

x4=cash;

x5=vec_avg(fnd6_cogss);

x6=vec_avg(fnd6_newqeventv110_xsgaq);

x7=fnd23_intfvm_bpao;

x8=fnd72_s_pit_or_cf_q_cf_change_in_inventories;

x9=fnd3_A_int_exp;

x10=vec_avg(fnd72_pit_or_is_q_is_inc_tax_exp_other_comp_inc);

x11=vec_avg(fnd72_pit_or_bs_a_bs_tot_asset);

#fast expression

y=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10;

z=y/x11;

# z=(cashflow_op + cashflow_fin) / mdf_tas;

# 首先，使用quantile运算符对x进行分位数排名

z_quantile = quantile(z, driver = uniform);

# 定义两个阈值，用于识别前10%和后10%

lower_bound = 0.1;

upper_bound = 0.9;

# 为排名前10%的股票分配正权重，排名后10%的股票分配负权重

# 使用条件表达式，其余保持为0（不投资）

weights = if_else(z_quantile <= lower_bound, -z, if_else(z_quantile >= upper_bound, z, 0));

# 输出加权后的Alpha值

weights;

4.目前的结果如下：
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawCOwn
> MarEin
> 3.20
> 36.979
> 3.30
> 39.439
> 4.959
> 21.339600
  
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 3,00OK
> 25OOK
> ZOOOK
> 1,5OOK
> 1,00OK
> 中 )
> 圈 I [
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



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 5PASS
> Sharpe Of 3.20 is above CUtOff Of 1.58.
> Fitness of 3.30 is above cutoff oT1.
> Turnover of 36.979 is above CUtoff OT 1%
> TurnoveroT 36.979 is below CUtOff ot 709
> Sub-universe Sharpe Of 2.51 is above CUtOff Of 1.39.
> 2FAIL
> Weight is too strongly concentrated
> Ortoo few instruments are
> assigned welght。
> IS ladder Sharpe of 0 is below cutoff of 1.58 for ladderyear 2: 1/20/2022...1/21/2020.
> 1 WARNING
> 3 PENDING


有一些指标似乎表现还挺好，但是我还不太明白前面为什么曲线是平的？可能我对平台的一些理解还不对，请大家指证。

---

### 评论 #51 (作者: WL13229, 时间: 2年前)

@ [YL37225](/hc/en-us/profiles/17548796152983-YL37225)

还烦请将阅读的论文分享成一篇文档发送至中文论坛

---

### 评论 #52 (作者: WL13229, 时间: 2年前)

[EC34309](/hc/en-us/profiles/13557080755991-EC34309)

您好。看到您使用了GPT的帮助，这是非常好的，它会很有效地帮助你。

1. 关于Alpha Example. 它是基于CAPM模型进行的。它认为由CAPM模型计算出来的return应该为股票的“真实价值return”。但是如果股票的market return高于CAPM模型算出的return，则说明市场给了该股票更高的溢价，它会有momentum的趋势继续上涨。希望这样的解释能给您帮助。

2.

> I wasted a lot of them on generating those ideas. I believe this could be improved by solely focusing on the passage that talks about the variables related to returns.

我猜想您说的是，您希望复现这篇研报的工作流程。它确实是有难度的，先从简单的做起，一步步来。

3. 以下是一些通用的residual概念：在回归中，如果将变量A做为因变量Y，变量B作为自变量X。将A和B做个回归，那么residual就代表了，A的变动中，无法被B解释的那一部分。

---

### 评论 #53 (作者: DZ54968, 时间: 2年前)

1.由于刚成为顾问，各板块Alpha都比较少，由于Model类相关Alpha最少，因此我选择阅读Research Paper 27: Earnings Uncertainty and Attention

2.《Alpha灵感》文章：【Alpha灵感】盈利不确定性和公司关注度

3. Template分析

a = group_rank(ts_regression(zscore(ts_mean(-A,T)), zscore(B), T, lag=63, rettype=2), densify(market));

b = group_neutralize(a, bucket(rank(cap), range='0.1,1,0.1'));

trade_when(C>ts_mean(C, 21), b, abs(returns)>0.1)

该模板对预处理后的两变量进行相关性分析，后采用group和trade_when进行过滤，以预测价格飘移趋势。

4.Alpha提交

虽然本周已尽力尝试，但未能得到可提交Alpha。表现相对较好的Alpha截图如下：


> [!NOTE] [图片 OCR 识别内容]
> TUHUUIIA
> BRAII
> Simulate
> Alphas
> Data
> [ Competitions (3)
> Events
> 0 Learn
> Refer
> friend
> Simulation
> Simulation 2
> Simulation
> Simulation
> CODE
> RESULTS
> LEARN
> Settings
> USA/D1/TOP3000
> Conyert to Multi-SImulatlon
> Chart
> Pnl
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELY
> USA
> TOP3OOO
> SOO
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 0,08
> OOOK
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PENOD
> YEARS
> MONTIIS
> Verth
> SOOK
> Apply
> Saye a5 Default
> TOOO
> SJOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022


5.总结反思

由于对平台运算符和数据不够熟悉，手工构建的模板可能并不足以挖掘有效Alpha。即使尝试了无数种datafield和参数组合，仍然无法获得有效Alpha。总结反思失败教训，一方面认为对于论文的理解不够，没有从中提炼出较好的策略模板，导致纯靠机器暴力挖掘也无法得到可以提交的Alpha；另一方面对于平台使用的熟练度不够，对于数学运算符和数据集的理解不够深入，导致难以复现论文思路或者实现自己对于策略的一些想法。之后的改进方向将从多读论文体会不同论文的策略思想，并多亲手实践，尽可能快地构建自己的alpha模板

---

### 评论 #54 (作者: WL13229, 时间: 2年前)

[DZ54968](/hc/en-us/profiles/18130763917463-DZ54968)

烦请附上《Alpha灵感》的链接，便于我们快速审核

---

### 评论 #55 (作者: DZ54968, 时间: 2年前)

补充【Alpha灵感】链接： [【Alpha灵感】盈利不确定性和公司关注度 – WorldQuant BRAIN]([L2] 【Alpha灵感】盈利不确定性和公司关注度_21149732774039.md)

---

### 评论 #56 (作者: WL13229, 时间: 2年前)

[DZ54968](/hc/en-us/profiles/18130763917463-DZ54968)

辛苦在原评论或灵感文章中，分享一些关于check list的内容。例如

《Alpha灵感》文章中必须包含的内容

- 核心交易idea是什么？
- 是否找到数据：
- 是否找到Universe: 例如TOP 200, （一般金融论文都会明确说出其适用的股票类型）
- 是否找到Neutralization: Sector (Smart Search)
- 使用什么operator
- 核心Alpha的Expression（可选）
- 绩效

---

### 评论 #57 (作者: QH29412, 时间: 2年前)

1. Performance面板截图。选择了USA，TOP3000 
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> USA
> CHN

2. 《Alpha灵感》文章- [Back to Fundamentals: The Accrual-Cash Flow Correlation, the Inverted-U Pattern, and Stock Returns](/hc/en-us/community/posts/16412726318231-Research-Raper-22-Back-to-Fundamentals-The-Accrual-Cash-Flow-Correlation-the-Inverted-U-Pattern-and-Stock-Returns)
3. Template分析，文章中说accruals 和employment growth rate，accrual 和 CFO 的负相关性, 都对returns 有很强的预测能力。所以同时满足横截面分析和时间序列分析操作，ts_regression 和regression_neut 都有效果。
4. 
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
> 2.92
> 63.499
> 1.12
> 9.269
> 3.46%
> 2.929o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2012
> 4.22
> 64.50%
> 1.71
> 10.569
> 1.21%
> 3.2890。
> 1455
> 1603
> Long
  
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,00OK
> 4,00OK
> 2,00OK
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

5. 目前alpha还在优化中，turnover 略高，Prod correlation 0.8353 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
6. 我是用postman 做自动化，个人觉得程序提交simulation比较适合去降低prod corr，搜索范围比较小。前期还在构建框架的时候，搜索范围太大。

fnd6_idit

---

### 评论 #58 (作者: WL13229, 时间: 2年前)

@ [QH29412](/hc/en-us/profiles/18659551926295-QH29412)

烦请发布一篇《Alpha灵感》的文章，阐述一下研究过程。

《Alpha灵感》文章中必须包含的内容

- 核心交易idea是什么？
- 是否找到数据：
- 是否找到Universe: 例如TOP 200, （一般金融论文都会明确说出其适用的股票类型）
- 是否找到Neutralization: Sector (Smart Search)
- 使用什么operator
- 核心Alpha的Expression（可选）
- 绩效（需保证Sharpe至少大于1.3，Fitness至少大于0.6，Turnover低于45%，高于5%；通过PROD相关性测试）

---

### 评论 #59 (作者: SW14484, 时间: 2年前)

1. Performance面板截图 
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> USA
> CHN


不难发现，我的Alpha分布主要是在USA分区，所以我这次选择CHN分区

1. 我找的是一篇研报：A 股反转之力的微观来源

并发布在了中文论坛里的【Alpha 灵感】：

[[L2] 【Alpha灵感】A 股反转之力的微观来源_22071441537303.md]([L2] 【Alpha灵感】A 股反转之力的微观来源_22071441537303.md)

1. Template分析：

我的抽象Alpha Template如下：

x = vec_sum(A)  

# 计算x的某个百分比值  
y1 = ts_percentage(x, window_size, percentage=percentage1)  
y2 = ts_percentage(x, window_size, percentage=percentage2)  

# 根据条件计算加权和  
M_high = ts_sum(if_else(x > y1, B, 0), window_size)  
M_low = ts_sum(if_else(x < y2, B, 0), window_size)  

# 计算Alpha值  
Alpha = M_high - M_low  

# 返回Alpha的相反数  
return -Alpha

这里的核心的Template其实就是根据论文里的Idea，按照不同的分位数得到两个次一级的Alpha: A和B，而这两个Alpha衡量的是相反的信息，所以通过计算A-B，得到反转的Alpha因子。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 15M
> 1OM
> 5,0OOK
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



> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> TRAIN
> TEST
> IS
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.50
> 11.869
> 3.44
> 23.609
> 9.809
> 39.799o。


1. 成功提交的Alpha:


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
> Select
> Select
> Select
> Search
> Select
> Select
> anonymoUs
> Regular
> ACTIVE
> 03/13/2024 EDT
> CHN
> TOP3000


5.总结和反思

1）之前急于开始用machine进行搜索，但是没有深入研究template，最后浪费了许多时间，还是应该多花时间在template背后的经济学原理，而不是大力出奇迹上。有一个疑问是如何提升特定日期的 [IS ladder Sharpe](/hc/en-us/articles/6726865162903)  ，有几个Alpha因为这个原因 过不了。

2）代码提升：进行了提取相关信息包括sharpe等信息，但是有个问题是如何提取IS Testing Status部分的信息，因为它每次运行的输出其实不是确定的。

---

### 评论 #60 (作者: WL13229, 时间: 2年前)

[SW14484](/hc/en-us/profiles/20580045390871-SW14484)

其实IS Ladder不通过，是一个很强的提示，即其在最近一段时间内表现不佳。因此我还是建议从idea出发去修改它。首先我建议使用visualization的功能，查看近几年表现不佳是某些市值层面的失效的还是行业的失效。之后尝试使用vector neutral去中和这个特点。另外的思路是，这个本质是一个反转的策略，不妨和其他反转策略的思路结合起来。

---

### 评论 #61 (作者: WL13229, 时间: 2年前)

[BC25356](/hc/en-us/profiles/13921805253911-BC25356)

关于疑问一，self corr和prod corr往往需要额外触发，才能得到结果。其实理论上，对于每个Alpha,即便你不进行任何IS的checks，你都可以写代码发送提交请求，只是服务器会拒绝而已。

关于疑问二，返回location即等于网站上点击simulate后出现了进度条，使用for 函数在出现了进度条后即进行下一个，并不需要等待Alpha运行结束，这样并不会慢。再次表达我的个人意见，我认为在发送Alpha这个阶段使用多线程是没有必要的。

---

### 评论 #62 (作者: BC25356, 时间: 2年前)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)

谢谢您的解答。

关于疑问一：我这样理解，并不能通过check里面对应的值来判断，是否可以提交alpha。因为self corr和prod corr往往需要额外触发，所以他们一定是Fail的。但是我们可以判断一些指标，如果这些指标都通过了，我们把这些alpha选出来，在网页是确认提交。是否正确？

关于疑问二：请您看下，我修改前的代码。因为在修改前，我一个小时只能跑120个alphas左右。一个小时为3600秒，而我从发送reques，并等到.json["alpha]的结果，才会进行下一个。从发送到得到结果，需要25～35秒。所以一个小时大致会有120个alpha被发送，并得到alpha id。当代码在跑，我打开网页还可以继续开8~9个simulations，所以我觉得是我代码的问题，请老师帮我看下。

---

### 评论 #63 (作者: WL13229, 时间: 2年前)

[BC25356](/hc/en-us/profiles/13921805253911-BC25356)

您说的大致正确。

关于疑问一，并非“一定是Fail”，而是大部分时候可能是空值（在不触发前），确实也在技术效果上跟fail没有什么差别。手动提交是可以的。查看API的相关帖子，你可以看到修改Alpha颜色的code,你可以把这种有高潜力的Alpha标记颜色，方便后续手动检查。

关于疑问二，你可以参考我们在课上提供过的一个解决方案。即您不需要等待.json["alpha"]的结果出来，您只需要在运行下面这一行不报错的情况下，就应该发送下一个Alpha了。不需要使用while true去等.json["alpha"]的结果出来。


> [!NOTE] [图片 OCR 识别内容]
> 修改后:
> Jef
> SImulate
> aLpha(5 ;
> SImulation
> Uata)
> sinulation_response
> post( httns; Llani,wopldquanthrain . comlsimwlations
> 15onssimulation_data)
> Suimulation
> NOO465
> Ul
> SImulation
> IOSNI5e
> headers [
> Locationn
> While True:
> Sinulation
> progress
> get (simulation
> progress_url)
> 1f Simulation
> Drogress
> headers.get( Retpy-After
> break
> print("sleeping for
> Simulation_progress .headers [
> Retry-After ]
> SeCOnUS
> Sleep ( float (simulation
> progress . headers ["Retry
> After
> alpha_id
> simulation_progress.Json() [
> aUpha
> alpha
> get("https; LLapiopldqwantbcain Conlalphas("
> alpha_id)
> peturn alpha_id
> alpha


后面再从IS列表批量取得Alpha performance

---

### 评论 #64 (作者: YZ31807, 时间: 2年前)

1.Alpha面板


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> USA
> CHN
 可见在CHN较少，于是本周尝试了CHN地区的alpha

2.Alpha灵感文章

[../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】估值因子_22130841774359.md](../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】估值因子_22130841774359.md)

3.template分析

D=RANK(A)*ts_rank(B*C)

group_neutralize(D，mygroup)

其中A是基本面相关Alpha，B与C是根据研报引入的估值类因子BP和SP的实现。

随后，利用上周使用的模板进行大批量回测。在筛选数据时，主要针对BP/SP因子中的组成进行组合筛选，在约500个样本中得到了可以提交的alpha。

4.提交截图


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
> Search
> Selec
> Selec
> Selec
> Search
> CHN
> Selec
> e.吕> |
> anonymous
> Regular
> ACTI
> 03/16/2024 EDT
> CHN
> TOP3000
> 4.59


5.总结反思

在本周我优化了我的上周的模板，使得在筛选alpha中能自动保存alpha的list。在进行alpha构建时，采用了中性化以及与基本面因子结合的办法提高了alpha表现。对于API有一个小小的疑问，可以直接使用API筛选出合格的alpha并且直接提交吗？

---

### 评论 #65 (作者: BC25356, 时间: 2年前)

1. 因为刚开始做研究，所以都是蓝海，选择了最近特别感兴趣，高估值与成长性的话题，所以我选择了

[../顾问 JG15244 (Rank 67)/[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md](../顾问 JG15244 (Rank 67)/[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md)


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> Alphas
> USA
> Delay 1
> Fundamental ata
> News ata
> Rrce volume data
> Social media data
> Model data


2.【Alpha灵感】高估值与融资决策

[../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】高估值与融资决策_22155076343831.md](../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】高估值与融资决策_22155076343831.md)

3. Template分析

```
condition = rank(A);trade_when(condition > 0.8, group_rank(B, group), -1)
```

**抽象** ：通过A进行选股，根据B，进行做空。

**适用Universe** ：因为文章中多次提到small size和High tech innovation company，所以我选择TOP3000

4.  
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
> e.8>1
> e.8〉1
> e.8>1
> Select
> anonymous
> Regular 
> ACTIVE
> 03/17/2024 EDT
> USA
> TOP3000
> Tag


5.

- **代码改进：** 从一个小时跑120个到900个Alpha的突破（其实就是一个循环的改变）；并返回alpha结果时候，自动标记可以提交的alpha
- **debug经历：** 卡在获取Location上，一直报proxyerror，最后通过continue很快解决
- **Template改进** ：1. 我想继续深挖论文研究Momentum方向；2. 对于现在的Reversal模版，我觉得可以在对B数据进行深度研究

---

### 评论 #66 (作者: WL13229, 时间: 2年前)

[YZ31807](/hc/en-us/profiles/18243220367511-YZ31807)

一个很完整的作业。是可以用API筛选并提交的，但是我建议在研究的初期，还是通过手动提交比较好，可以人为最后做一次检查和思考。另外，如果担心Alpha淹没在列表中，可以对pass IS Test的Alpha进行颜色的修改，很快就能筛选出来了。

---

### 评论 #67 (作者: WM13885, 时间: 2年前)

**1. alpha 面板截图（作业完成后）：**


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Distribution of Active Alphas
> Click to Jrill Oown
> CHN
> USu
> KOR
> alphas
> (7 OTall Alphasi
> KOR


结论：什么alpha都缺
 **2. post**

【Alpha灵感】换手率因子tps_turbo：如何用纯净化GTR因子增强传统换手率因子

[../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】换手率因子tps_turbo如何用纯净化GTR因子增强传统换手率因子_22162473785623.md](../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】换手率因子tps_turbo如何用纯净化GTR因子增强传统换手率因子_22162473785623.md)

**3.template分析：** 
因为参考的文章对同样的template做不同的operator下的处理，如均值，标准差，市值提纯，中性化的处理等，所以核心template还是:
a = {volume_element}/sharesout
目前感觉换手率因子的可代替的数据字段或者template本身无法做到特别抽象，也想过做booster，比如拿基本面因子做一个b =（1+rank（{fundamental}））然后去做a*b组合，但试着跑了500个，并不是很理想。

**4. alpha提交截图：**


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> OUt Of 14
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (ESTI
> Region
> Unierse
> Sharpe
> Returns
> Turnover
> Search
> Selecr
> Selecr
> Selecr
> Searc
> Selecr
> Selecr
> 8.吕 >1
> 8.吕 >1
> 8.吕 >1
> Selecr
> alpha_tps_TUrbo
> RESJlaT
> ACTIVE
> 0311812024EDT
> KOR
> T0?500
> Tag


**5.总结：** 
这周代码上面做了很多优化，做了模块化提高了效率，多了上面提到的可以做数据字段组合的功能。同时，做了把表现结果导入cvs的功能，尤其是在我筛选IS_Ladder_Shape value 的时候很省时间。但发现如果在跑simulation的时候去拿结果返还的id和数据会导致回测变慢，并且10个回测额占不满，多线程是否能解决这个问题？而在simulation跑完后去fetch is alpha performance似乎不能拿到所有实时的数据？导出来的并不是刚跑完的数据，而是前段时间的。

可以改进的方向：
对代码和理解论文/研报，template的构建做更深的研究，是否能在不同settings（universe）下多次回测？同时做一个更多指标的可视化，导入csv或者能够直接对value做筛选的功能。

---

### 评论 #68 (作者: WH24469, 时间: 2年前)

**1．Performance面板**

目前提交的alpha较少，所以没有数据偏向，选择阅读：Overnight returns, daytime reversals, and future stock returns

**2．Alpha灵感**

链接为： [【Alpha灵感】隔夜与日内拉锯战暗藏的信息 – WorldQuant BRAIN](../顾问 PN39025 (Rank 87)/[L2] 【Alpha灵感】隔夜与日内拉锯战暗藏的信息_22174527569303.md)

1. **Template分析**

首先是将数据抽象化，将close替换为（close+vwap）/2，一方面降低数据的prodC，一方面又将volume的信息融合进来。

其次是对回归的抽象化，文章中采用将AB_NR、AB_PR等指标对各项公司的相关基本面指标进行回归，但本人采用将收益率剔除这部分情绪波动的信息，再剔除风险类信息，得到最终指标，意在筛选出那些不受市场情绪影响的，能带来稳定收益的标的。

抽象化后，不近价格会受到隔夜回报的影响，同时成交量中的信息也会对价格造成印象，此外，情绪波动造成的价格波动在市场中带来的影响并不会长期存在，经过纠正后便会回到正常水平。

**4．提交截图**

目前prodC还未达标，且turnover处于65%左右，还在进一步优化，不知道是否是有其他consultant已经提交过这篇论文的alpha了，但论坛并未搜索到相关帖子。

**5.反思**

此次复现过程中，有遇到数据不知道怎么找，表达式不知道怎么用的情况，对brain平台的使用还不够熟练。此外，复现过程中使用无人挖掘的数据较少，更多的使用的是常规使用的数据及operators，导致总是面临prodC不达标的情况，后期需要提升自己使用新operators和datasets的能力。

---

### 评论 #69 (作者: WL13229, 时间: 2年前)

[WM13885](/hc/en-us/profiles/20518086330647-WM13885)

感觉做得有点急躁了，template过于简单，可能大概率无法过滤出有效的信息。还需要更多努力.

"也想过做booster，比如拿基本面因子做一个b =（1+rank（{fundamental}））然后去做a*b组合，"

我认为这样的做法并不是什么booster，相反，这似乎有不小的overfitting风险

---

### 评论 #70 (作者: WL13229, 时间: 2年前)

[WH24469](/hc/en-us/profiles/13991511763607-WH24469)

可以使用trade when的方式，仅在某些情况，例如市场波动大的时候再交易，可以显著降低turnover。

---

### 评论 #71 (作者: SW49904, 时间: 2年前)

抱歉有些超出DDL提交，我的灵感来自于文章： [https://www.damray.com/FileUpload/OfficeFile/76df04556ba547f8a84d062e2b4dfb19.pdf](https://www.damray.com/FileUpload/OfficeFile/76df04556ba547f8a84d062e2b4dfb19.pdf)  ，主要基于六种常见的股票投资策略，包括KDJ指标、蜡烛图和蜡烛图形态等。

我希望通过多因子模型结合不同的技术指标，以提高对股票价格走势的预测能力。KDJ指标可以帮助确定股票的超买和超卖位置，蜡烛图可以帮助识别市场的趋势和反转点，蜡烛图形态可以进一步增强对价格趋势的判断。例如，在KDJ指标显示股票处于超买状态时，如果出现了反转型的蜡烛图形态，如倒锤子或射击之星，那么这可能是一个更可靠的卖出信号。

我构造的Alpha主要形态如下：

*W1* *-(close-low)/(high-low)+ *W2* *-(high-open)/close+ *W3* *ts_mean(-(close-low)/(high-low), 10)，其中前两项我经过消融测试发现在sharpe和fitness的表现上是1+1>2的，而第三项主要是用来降低turnover的。


> [!NOTE] [图片 OCR 识别内容]
> LPh
> Prl Plot
> 105411
> +
> 
> LON_SHHPE
> PsSs
>  NN
> 4400
> HIINES
> P-ss
> 1UIIU
> TOOO
> LOw_TURNOIER
> PSc
> 001O0
> TURNOVCR
> Puss
> 0TIN
> 05135
> CONCEITRATED_EICHT
> IS
> Nal
> Nal
> LOW_RETURNS
> Pss
> 3280
> E15
> LOI_SUB_UNIVERSE_SHRPE
> P-ss
> 2IIIU
> O UTU
> LO ROBUST UIVERSE SHRPE
> Pc
> GSTO
> ROBUST_UNIVERSE
> rTURNS
> Poss 01312
> 0.133
> SELF_CORHELTION
> PENOING
> Nul
> Nal
> PROD_CORREL-TION
> PENDING
> Nal
> Nal
> ILCULI SUHIIISSIUN
> FSS
> 4CID
> LCUJ
> NATCHES_CONFETTION
> IRNING
> Nal
> Nal
> LADDER_SHRPE
> 1.9JU
> ITCHES THEIES
> IIRNINC
> Nl
> Nl
> Date
> Fetrleyed
> AChn:
> Pnl Plot
> 1s411
> 1nit
> VTUr
> LOI
> SHARPC
> Puss
> 3500
> LOW_FITNESS
> Puss
> 10100
> LOW_TURNOVER
> Puss
> 0.01
> 06373
> HIGH_TURNOCR
> Pss
> 0TD
> 0EJT
> COWCZNTRATED_VCIGHT
> Pss
> Nal
> Nal
> LON_SUB_UNNERSE_SHARPE
> Pss
> 1JAII
> SELF_CORRELATION
> 0.7409
> FROD_CORRELATION
> PENDING
> Nal
> PEGULAR_SUBIISSION
> Puss
> 00000
> LaTCHES_COPETITION
> WNING
> Nal
> Nal
> LJDDER_SHARPE
> Puss
> 257
> 2EON
> IATCHES_THEMES
> WRNING
> N
> N
> Mlr
> NGT
> 42012-0130
> 40120
> 70+5-05
> 701直-0
> 7022
> ~01-21
> 05-1
> -0121
> 201 08
> 2012
> 2015
> 2022


对于universe我主要对比了中美市场，经过多次对于Alpha表达式以及Neutralization的调整，我发现该Alpha在CHN中似乎无法避免2015年的股灾，因此我最终选择了USA，并通过循环搜索来找到合适的Nrutralization（Subindustry）和Universe （TOP3000）。

从上述checks中我们可以发现，现在的自相关性非常高，这是令我很头疼的，我没有太好的解决办法，只能通过加入一个自由项到这个多因子模型中，类似于 *W1* *-(close-low)/(high-low)+ *W2* *-(high-open)/close+ *W3* *ts_mean(-(close-low)/(high-low), 10)+0.1*epsilon，而后我通过暴力搜素可以使得Alpha通关的epsilon最终得到提交如下：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> DnL
> TOM
> OOOK
> OOOK
> OOOK
> OOOK
> Jan '13
> 40'14
> Jan '15
> Jan'15
> Jan'17
> J3n'13
> Jan '19
> Jan'20
> J3n'21
> Jan '22
> ~ WVOOVVS
> 转到"设置"以激活 Windows。
> Hide test period
> Submit Alpha
  
> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down


反思：我觉得自己用的方法非常笨，其中我也尝试了其他方向的文章比如舆情等，但是构造出因子的表现并没有达到预期，甚至没有什么优化空间，这让我非常头疼。而对于量价数据相关的文章，构造出了很多在IS阶段通过测试的因子，再最终的test却总有不同的指标无法通过筛选，目前除了用一些暴力和简单的方法，自己并没有太多思路，还很迷茫。

---

### 评论 #72 (作者: ZY25767, 时间: 2年前)

大家好，这是我本周的交付内容，本周提交了很多实验的alpha，但是没有得到一个好的alpha，因为不太知道怎么把python转换成fast expression

1. Performance面板截图，选择相关方向的文章


> [!NOTE] [图片 OCR 识别内容]
> C
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Distribution of Active Alphas
> Click to drill down
> USA


2.《Alpha灵感》文章

Cranes among chickens: The general-attention-grabbing effect of daily price limits in China’s stock market

[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4073997](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4073997)

This paper examines the general-attention-grabbing effect of daily price limits in China’s stock market. We calculate the proportion of stocks that hit daily price limits and use it to construct a proxy of absolute price limits beta to measure the sensitivity of stock returns to daily price limits. We find that stocks with higher absolute price limits beta attract more investors’ attention and have lower future returns. We show that the predictive power of absolute price limits beta cannot be explained by other stock characteristics. The general-attention-grabbing effect is stronger among stocks that are heavily invested by retail investors.

**Keywords:**  Chinese Stock Market, Daily Price Limits, General-Attention-Grabbing Effect

```
ZT = (stock_close - stock_open) / stock_open
```

```
number_of_stocks = ZT.T.count()ZT = abs(ZT) >= 0.09number_of_stocks_toomuch = ZT.T.sum()factor = number_of_stocks_toomuch / number_of_stocksfactor.replace(np.nan, 0, inplace = True)
```

说白了。

一个指标ZT：涨跌停股票占比。

因子值：股票对ZT的敏感程度（用回归系数来衡量）

```
model = sm.OLS(Y_subset, X_with_const)regression_results = model.fit()results[end_date] = regression_resultsprint(regression_results.params)
```

总结与反思：

对Fast Expression 和 dataset 不够熟悉。除了阅读论文，我尝试过程中大多数时间花在了如何写fast expression 上，而且常常写出来的表达式无法准确表达文章观点。希望可以等我有了我的consultant之后可以更加好的去请教。

---

### 评论 #73 (作者: DL92496, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Clicktodrildown
> FundNIUI
> Woldyl
> ToUNT
> SCCII TrCJan
> N4 ultl
> Ulon o1u


1. Performance 面板截图，选择期权相关的文章

2.文章题目：The Information Content of Option Demand（ [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2005763](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2005763) ）

3. Template分析

rank(-ts_regression(returns, ts_delta(opt6_ioc,day_decay),y)-ts_regression(returns, power(ts_delta(opt6_ioc,day_decay),2) , y))

文章中提出了Total call option interest 因子的变化率和收益呈现负向关趋势，因此建立上述Alpha Template，并使用python扫描不同的回归天数y。


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 11 PASS
> FAI
> Prod correlation 0.7645 is above Cutoff of 0.7and Sharpe not better by 10.0% Ormore
> WARNING


扫描后依然无法满足Prod correlation的结果。

4.失败原因分析

可能需要引入交易条件，正在探索交易条件判断的因子。

---

### 评论 #74 (作者: WL13229, 时间: 2年前)

[DL92496](/hc/en-us/profiles/13716888353687-DL92496)

请发送一篇《Alpha灵感》文章

---

### 评论 #75 (作者: DL55804, 时间: 2年前)

1、我的面板如下，我选择论文《Limit Order Clustering and Stock Price Movements》 **限价订单聚集对股票价格的影响。**


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> ASI
> CHN
> GLB
> USA


2、【Alpha灵感】限价订单聚集对股票价格的影响

文章链接： [../顾问 PN39025 (Rank 87)/[Commented] 【Alpha灵感】限价订单聚集对股票价格的影响.md](../顾问 PN39025 (Rank 87)/[Commented] 【Alpha灵感】限价订单聚集对股票价格的影响.md)

3、

价格聚集效应：投资者的限价订单倾向于在整数价格点（如X.0）及其附近聚集。这些聚集的限价订单形成了价格支撑或压力，使得股票价格在这些点附近表现出特定的波动模式。

价格波动效应：当股票价格略高于整数价格点时（如收盘价为X.1），次日股票价格更有可能上涨；而当股票价格略低于整数价格点时（如收盘价为X.9），次日股票价格更有可能下跌。这是由于整数价格点附近的限价订单对价格形成了支撑或压制。

策略：在收盘价略高于价格点时（如X.5），买入该股票并持有至次日，预期股票价格将会上涨。在收盘价略低于价格点时（如X.5），卖出该股票并持有至次日，预期股票价格将会下跌。

4、alpha提交截图


> [!NOTE] [图片 OCR 识别内容]
> alpha00z0
> ReBUlar
> ACTIVE
> 07/16/2024 EDT
> GLB
> MINVOLIM
> a1pha0019
> Regular
> ACTIVE
> 07/16/2024 EDT
> ASI
> MINVOLIN


5、总结反思：

反思与总结：

1. 剔除极端的信号。
2. 剔除价格较大和较小的股票，价格较小的股票，本身的数值就很重要了，价格较大的股票，小数点后的数值没那么重要。
3. back_fill降低换手率。
4. 使用信号过去的标准差，增强信号，交易信号过去波动大的信号，波动大的信号更容易可能是更有效的信号。

---

