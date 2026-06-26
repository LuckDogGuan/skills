# 英才候选人计划实训考核（Case1）

- **链接**: [Commented] 英才候选人计划实训考核Case1.md
- **作者**: WL13229
- **发布时间/热度**: 2年前, 得票: 3

## 帖子正文

**必做1: 阅读 [【Alpha灵感】论文/研报合集 – WorldQuant BRAIN]([L2] 【Alpha灵感启示录】100 从论文到alpha的复现持续更新收录中Pinned论坛精选_19348865150743.md) 或者  [Research Papers for Consultants – WorldQuant BRAIN，](/hc/en-us/community/topics/12997688420247-Research-Papers-for-Consultants) 选择一个你感兴趣的Alpha作为模板,并实现对该模板的1000次以上回测。例如**

```
 Ts_Rank(rank(x), 20)
```

参考路线图(您可以使用 **[BRAIN API可以实现的功能 – WorldQuant BRAIN]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md)** 进行路线图的实现）：

- Step1: 登录账号
- Step2: 思考合适的数据字段和参数。以该模板为例，可能基本面的model data也是不错的，但时间参数可能需要至少月度以上。如果是量价数据，可能需要更短的时间周期。
- Step3: 使用 [Data Explorer](https://platform.worldquantbrain.com/data)  手动尝试几个不同类型(category)的数据集，再次深入反思该模板提取的是什么层面的信息。
- Step4: 使用代码获取该类型的所有数据集和大部分数据字段（datafield)
- Step5: 对数据进行初步处理（例如vector data需要先使用vector operator降维）
- Step6: 将数据字段插入模板，批量生成Alpha表达式。
- Step7: 将Alpha表达式附上simulation setting （这一阶段可以使用比较常见的setting，无需过度调参）
- Step8: 将Alpha发送至服务器进行simulation。常见错误debug👉 [BRAIN API及日常回测时常见的报错 – WorldQuant BRAIN]([L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md)
- Step9: 获取到所有Alpha的结果，每个Alpha至少获取到performance_comparison结果
- Step10:总结反思（代码效率、debug经历、模板适合的数据类型、模板的改进方向等）

**必做2:** 阅读👉 [量化研究推荐论文 – WorldQuant BRAIN]([L2] 量化研究推荐论文论坛精选_21004691882135.md) 中的任意一篇论文，或者自行寻找其他材料（如研报、论文），总结论文的核心思路和Alpha Idea **(注意不要和本帖子或论坛中已被发布的重复）** .

需提交的内容如下置顶评论所示：

---

## 讨论与评论 (138)

### 评论 #1 (作者: WL13229, 时间: 2年前)

**必做1：**

1.最近的截图（需包括时间） 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 10
> 1
> GOOD
> Total Unsubmitted Alphas
> 689
> Total Active Alphas
> 17
> BCELLEIIT
> SFFCTSTUISF
> Total Decommissioned Alphas
> Total Alphas
> 706
> 5.32PN
>    思
> ENG
> 12/14/2023


2.下周二前的截图（需显示时间）


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 2,170,494
> Total Active Alphas
> 1,137
> Total Decommissioned 4lphas
> Total Alphas
> 2,171,637


3.截图显示你的code **连续不停（不可中断，代码需能handle各类报错）** 提交了1000个simulation。请自行考虑，如何print合适的信息，证明已经提交了1000个Alpha.这种技能会使得你的code更加易读，也能帮助你在代码运行时了解其状态。

4. 总结反思，需包含至少四个方面的反思：代码效率、debug经历、模板适合的数据类型、模板的改进方向。多写不限，字数不少于300字。

**必做2：**

**我阅读的文章是option13：**  [Testing for Asset Price Bubbles using Options Data](../顾问 CC40930 (Rank 95)/[Commented] Research Paper 72 Testing for Asset Price Bubbles using Options Data.md)

该文章使用看涨和看跌期权之间的定价差异来估计是否出现了资产泡沫。方法论上讲，价格泡沫的产生是因为买家通常购买资产不是为了永久持有并获取其永久现金流，而是为了在未来某个时候以更高的价格将其卖出。因此，泡沫的存在与投资者对资产价格未来演变的预期密切相关。因此，期权，由于其本身具有前瞻性特质，是估计和测试其标的资产泡沫存在的天然工具。进一步来看：

论文使用看跌期权数据来估计资产的基本价值，然后利用看涨期权的市场价格与基本价值之间的差异来估计泡沫。具体步骤如下：

- 我们首先选定一个灵活的参数模型（如G-SVJD模型）来描述资产价格的演变过程。
- 接下来，我们将看跌期权的数据输入进G-SVJD模型，对股票的实际价值进行估值，原因是该论文认为：使用看跌期权计算出来的股票估值是不含“泡沫”的。
- 最后，我们将看涨期权的数据输入进G-SVJD模型，作为对股票市场价值的估计。将看涨期权计算出来的估计值和看跌期权计算出来的估计值进行相减。这个差值越大，标的股票的泡沫越大。
- 使用统计学的方法，我们可以设定出“泡沫”的门槛。例如，当“泡沫”的值超过了标的资产价格的一定比例时，我们就认为该股票出现了明显的泡沫。

Alpha Idea：使用论文提示的方法，选取合适的模型计算并识别资产泡沫。在泡沫的初期可以跟随做动量策略，后期可以做反转策略。

---

### 评论 #2 (作者: YL93001, 时间: 2年前)

1、此时simulation数目为1078 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Show
> 10
> out of 1,078
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
> Tag
> Search
> Select
> Select
> Select
> Search
> Select
> Select
> e.吕>1
> e.吕>1
> e.吕 >
> Select
> anonymoUs
> Regular
> UNSUBMITTED
> 11/28/2023 EST
> CHN
> TOP3000
> -1.12
> -7.029
> 19.4496
> anonymoUs
> Regular
> UNSUBMITTED
> 11/28/2023 EST
> CHN
> TOP3000
> -1.23
> -7.699
> 19.4696
> anonymoUs
> Regular
> UNSUBMITTED
> 11/28/2023 EST
> CHN
> TOP3000
> 2.31
> 26.619
> 22.939
> anonymoUs
> Regular
> UNSUBMITTED
> 11/28/2023 EST
> CHN
> TOP3000
> 1.62
> 18.0396
> 22.799
> anonymous
> Regular
> UNSUBMITTED
> 1/28/2023 EST
> CHN
> TOP3000
> 2.31
> 26.619
> 22.939
> anonymous
> Regular
> UNSUBMITTED
> 11/23/2023 EST
> CHN
> TOP3000
> -2.34
> -13.389
> 28.659
> anonymous
> Regular
> UNSUBMITTED
> 1/23/2023 EST
> CHN
> TOP3000
> -2.34
> -13.389
> 28.659
> anonymous
> Regular
> UNSUBMITTED
> 11/23/2023 EST
> CHN
> TOP3000
> -1.09
> -5.809
> 28.869
> anonymous
> Regular
> UNSUBMITTED
> 1/23/2023 EST
> CHN
> TOP3000
> -1.09
> -5.809
> 28.869
> anonymoUs
> Regular
> UNSUBMITTED
> 11/23/2023 EST
> CHN
> TOP3000
> -1.04
> -5.929
> 30.219
> 20:30
> Q 搜索
> ^  申  9
> 谷 d)) 匈
> 2023/12/15


2、此时simulation数目为2579


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Show
> 10
> out of 2,579
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
> anonymoUs
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.99
> -29.919
> 147.569
> anonymous
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -1.94
> -19.6896
> 145.229
> ace_tag;
> anonymoUs
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.22
> -22.789
> 142.759
> ace_tag;
> anonymoUs
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.52
> -24.849
> 147.699
> ace_tag;
> anonymous
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.43
> -23.469
> 143.139
> ace_tag;
> anonymous
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.72
> -26.049
> 148.239
> ace_tag;
> anonymous
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -0.22
> -1.029
> 5.3796
> ace_tag;
> anonymous
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.72
> -28.789
> 147.569
> ace_tag;
> anonymoUs
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.41
> -24.009
> 151.119
> ace_tag;
> anonymoUs
> Regular
> UNSUBMITTED
> 12/16/2023 EST
> CHN
> TOP3000
> -2.17
> -21.959
> 145.8796
> ace_tag;
> USD/EUR
> 20:40
> +0.90%
> Q 搜索
> C  单  9
> 谷 d) 四
> 2023/12/16
> Tag


3、每个线程10次simulation，连续跑完158个线程


> [!NOTE] [图片 OCR 识别内容]
> import time
> print(time.strftime("%Y
> %m-%d
> %H:%M: %S"
> time.Iocaltime()) )
> 0.Os
> 2023-12-16
> 17:32:42
> result
> ace. simulate_alpha_Iist_multi(s,
> alpha_list )
> print(time.strftime("%Y-%m-%d %H: %M:%S"
> time.Iocaltime()))
> 47m 0.1s
> 0%
> 0/158[00:00〈?,
> ?i/s]
> 100%
> 158/158[44:00〈00:00,
> 16.715/i]
> 2023-12-16
> 18:26:39


4、在代码效率方面，生成所有选取的datafield之后对vector数据先进行统一处理再与matrix类型数据合并，从而实现统一插入alpha表达式，再利用ace代码的框架进行多线程回测，该多线程回测效率较高。

在debug方面，注意到若同时替换alpha表达式中的两个datafield，循环生成expression list时可能会产生两个同样的alpha表达式，后期合并result时若用alpha_id做索引要先去重；以及提取数据与回测时最好把setting的参数都写在里面，更容易查看数据是否统一。

模板本身分析的是一致预期相关的数据，均属于分析师数据大类，于是我们选取一些coverage大于0.5，alphaCount小于1000的analyst类型数据来获取里面的全部datafield，回测之后发现，还是模板原来使用的分析师数据效果最好。

模板可能还有以下的改进方向：对alpha进一步做中性化或先筛选出一部分股票，再进行该alpha的交易，设置一些交易条件。

---

### 评论 #3 (作者: YW93864, 时间: 2年前)

大家好，以下是我本周交付的内容。

1.


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant BRAIN
> https: /platform worldquantbrain comalphas/unsubmitted
> 咕  A  &
> 中  仑
> 囱
> 鬯"
> UORL
> Simulate
> Nlphas
> Data
> @ Competitions (5)
> 显 
> Alphas
> Total: 3,616
> Unsubmitt
> Alpha Lists
> Unsubmited:
> 3,576
> Active:
> FIlter
> Decommissioned:
> Select Columns
> tatus
> Date Created (ESTI
> Rec
> 14:08
> 2023/12/17


2. 实际上应该模拟了3000+，暂时不确定因为什么会丢失了剩余的1700个，已经设置了sleep防止访问次数过多，以及观察status_code看是否报错；可能需要将sleep时间设置更长


> [!NOTE] [图片 OCR 识别内容]
> Total: 4,850
> Unsubmitted:
> 4,810
> Active:
> 40
> Decommissioned:



> [!NOTE] [图片 OCR 识别内容]
> for simulation_data
> in tqdm(alphal
> 1000
> Use 5imulation response
> post('https://api.worldquontbrain com/simulations
> jsonssimulation_data)
> is bady WOit 10
> Seconds
> 0no
> tpy
> Until
> is 900d
> status
> False
> While status
> True:
> Reep
> trying until
> is 9o0d
> simulation
> response
> post ('https:/Japi.worIdquantbrain
> Com/simulations
> json-simulation_data)
> if simulation_response.status
> Code
> ! 201:
> if simulation
> response.status_code
> 480
> print( Died
> break
> print(wsleep
> VOU
> COn
> Drocess
> the response further
> needed
> sleep(2o)
> else:
> SCatUs
> True
> 100y
> 1098/1800 [1:13;06<00:00
> 0qain


3. 本周心得

本周，我主要做了工程上的工作，以及对我想用的因子模板进行了适当调整。本周的宗旨是Work first, better next.

工程上，我将一些函数打包成库，方便调用，例如登录函数、获取datasets和datafields以及将alpha表现转化为dataframe面板进行可视化，整体上还是比较高效、连贯的。登录函数、获取数据函数在上次Meet up的时候，就有现成的，无需重新造轮子；我主要开发了generate_alpha和get_result函数，generate_alpha是用来生成alpha表达式的，只要将simulation_data字典放入函数，输入对应参数即可；而get_result比较复杂，一方面数据结构比较复杂，字典里面嵌套了多层的字典，另一方面返回的绩效较多，而实际上筛选alpha时无需事无巨细地将每一个指标都罗列出来，当machine alpha跑到2000+，5000+，根本无法考察每一个alpha的每一个绩效。因此我需要对指标进行筛选，首先我会考虑统计出现fail的次数，这些测试是alpha提交的基本条件，我会先观察都pass或者只出现较少fail的alpha，这样在如果有可以提交的那么直接提交，如果有fail的可以再观察其他指标进行手动优化或优化模板，示例如下；接着，我更喜欢fitness较高的alpha，再是收益较高的alpha，其他常见指标再加入考虑，最后分别按sort_value函数对合成好的dataframe进行排序。

```
#pythoncheck['result'].values.to_list().count('FAIL')
```

除此之外，我还将alpha_id考虑进来，方便在必要时候手动查看alpha表现，最后的面板如下


> [!NOTE] [图片 OCR 识别内容]
> returns
> turnover
> drawdown
> margin
> fitness   sharpe
> region
> universe
> delay
> decay
> Heu
> 117
> 0.1999
> 0.0813
> 0.2450
> 0.004922
> 2.67
> 2.11
> CTN
> T0P3000
> 128
> 0.1834
> 0.0881
> 0.2303
> 0.004164
> 2.60
> 2.15
> CN
> T0P3000
> 149
> 0.1785
> 0.0828
> 0.2445
> 0.004311
> 2.57
> 2.15
> CHN
> T0P3000
> 118
> 0.2039
> 0.0728
> 0.3155
> 0.005601
> 2.52
> 1,97
> CLN
> T0P3000
> 242
> 0.1655
> 0.0839
> 0.2422
> 0.003945
> 2.36
> 205
> CTN
> T033000


在工程上仍有需要改进的点：1）SLOW+FAST的参数代码不知道，缺少一个参数，尽管在CHN市场大概率是会使alpha表现变差的，但我仍然想尝试该参数，2）模板工程需要更加灵活，目前可能出现的问题是，当我1000次甚至更多次去simulate时，无法得知“是数据本身使模板从reversal变成了momentum，还是数据在该模板下无效”，如果是后者，那么目前的模板没有问题，但如果是前者，我需要在模拟1000次之后，将模板转换方向，重新测试部分的alpha；也许可以在使用构建表达式字符串时直接设置正负交替的alpha，但这样无法确定模板的属性是动量还是反转，这会导致alpha的可解释性变差；3）还需要进一步设计获取相关性corr接口，因为在目前返回的checks参数里，corr检测仍然是pending，需要额外的指令才可执行。

在模板选择方面，我使用了之前meet up介绍的模板，即“股票收益是球队还是硬币”，其中里面的第一个alpha“波动翻转”是个很好的模板，因为它主要是运算符，而并非像“换手反转”一样有换手率这样的数据去限定判断条件，相对来说第一个模板可玩性更高。

使用这个数据集，我目前觉得还是量价指标或技术指标更合适，因此我选用了model175数据集进行不断的simulation，这个数据我手动测试了一些，确实是有信号的。选用CHN市场，一方面是因为该模板已经在CHN市场取得了一些效果，另一方面是因为CHN独有的技术指标数据集非常丰富，如果深挖，很有可能出现相关性较低但同样有效果的alpha，还有就是方便完成第一周的任务（joke）。该模板原始设定是希望找到波动低于市场截面水平的股票，这些股票的确定性更高，而通常确定性高的股票可能因为过度关注出现超买，确定性较低类似，除了从收益角度去刻画这个现象以外，是否别的技术指标也能内蕴这样的关系？在逻辑上这看上去是说的通的。当我直接使用模板进行simulation时，会发现跑出来的结果一是不好，二是出现某些时刻平坦的曲线，说明该时刻不具备选股能力。


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> SOON
> OOON
> 75OOK
> ~TOI
> #12.5M
> ~151
> 17.5M
> ~2OI


我做了适当调整，技术指标在量价数据上进行处理后得到的，相当于已经构造了一次类似returns的部分，如果再次去求技术指标的变化，很有可能丢失信息，因此我将原先计算returns的部分替换为数据本身，再simulate几个，发现略有好转


> [!NOTE] [图片 OCR 识别内容]
> Chart
> OOOK
> 4 ODOK
> 30OOr
> 20OOK
> LOOOK
> an1
> 30'13
> Jan '14
> an'
> an't6
> lan18
> 13n419
> 3020
> PnL
> NK


但发现仍然跟大盘走势接近，因此我再neutral掉beta。最后，确实出现了一根比较好看的净值曲线


> [!NOTE] [图片 OCR 识别内容]
> Chart
> PrL
> 17,5N
> 1SN
> 12.5M
> TON
> 500
> 0OO
> SOOK
> Jan12
> Jan 13
> Jan'1
> Jan"15
> Jon '16
> Jon7
> Jon'13
> Jon'1g
> Jan 20
> Jon 21


尽管这个未达到入库标准，但该模板看上去要比之前好很多。

模板的改进思路：1）尽管已经“巧妙”地调整了一些运算符使alpha效果更好，但我观察了我自己的result_dataframe，发现只有若干个alpha效果好，而且其中大部分是在同一个datafield上调参调出来的，即该datafiled本身适用这个模板，而不是模板使用dataset，因此模板还需要更加精密地设计以便于使其能更适应整个dataset，在适应dataset之后，再去做进一步调参，优化alpha表现，可能才是有意义的

---

### 评论 #4 (作者: MM46273, 时间: 2年前)

想问一下，最近这周四门考试，下周三门考试，作业如果提交不上来怎么办？

---

### 评论 #5 (作者: YH69102, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> 标签页 ^窗口  帮助
> BK剧s
> 照 * @
> 母
> 12月15日周五  19:33
> C @  &  0
> Google
> Data
> 所有书签
> Announcements
> See all
> Notifications
> See all
> Most Recent
> Most Recent
> We analyzed youralphas
> here is a
> tailored for
> Achievement Unlocked!
> YOU!
> Achievement Unlocked!
> Research paper 69
> Callauction, continuous
> tradingand closing
> formation
> Achievement Unlocked!
> [BRAIN TIPS] Sequencing Multiple Operators inan
> Achievement Unlocked!
> Expression
> Achievement Unlocked!
> Global Delay- 1 Theme
> End OfACE 2023!
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 2
> 48
> GOOD
> BCELLENT
> Total Unsubmitted Alphas
> 2,077
> Total Active Alphas
> 40
> SPECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 2,117
> tip
> price



> [!NOTE] [图片 OCR 识别内容]
> 标签页
> 窗0
> 帮助
> %s
> @ @ % *@ ?
> 囚 &
> 12月178周日
> 15:01
> Google
> Data
> 所有书签
> Competitions (2)
> EVents
> Learn
> Refer a friend
> Announcements
> See all
> Notifications
> See all
> Most Recent
> Most Recent
> We analyzed your alphas
> here is a tip tailored for
> Achievement Unlocked!
> yoU!
> Achievement Unlocked!
> Research paper 69
> Call auction, continuous
> trading and closing price formation
> Achievement Unlocked!
> [BRAIN TIPS] Sequencing Multiple Operators inan
> Achievement Unlocked!
> Expression
> Achievement Unlocked!
> Global Delay- 1 Theme
> End OfACE 2023!
> Alphas
> See all
> Achievements
> View Achievements
> Status
> "@
> GOOD
> BxCELLENT
> Total Unsubmitted Alphas
> 7,601
> Total Active Alphas
> 40
> SPECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 7,641



> [!NOTE] [图片 OCR 识别内容]
> O_1145
> LC工 ]+/C]
> delay_increment
> 1
> signal
> ['close
> open
> high
> lOW
> 'Vwap
> 」
> With requests.Session()
> as Session:
> print (results)
> [23]
> 123m 54.15
> Python
> vrLfoldersLpLpmcsxdSnwy_mcllmtptngcwaeeegnLILipykerel
> 76805/998427731,Py:91: DeprecationWarning: Using
> method_whitelist
> With Retry is deprece
> retry_strategy
> Retry (
> Login successful
> Login successful
> Login successful
> Login successful
> Login successful
> Login successful
> Login successful
> Login successful
> Login successful
> alpha With
> Value mdl16g_cpud done simulation
> 1
> alpha have
> done simulation
> Login successful
> alpha With
> Value
> mdll6g_cpud done simulation
> 2
> alpha have done simulation
> Login successful
> alpha With
> Value mdl16g_cpud done simulation
> 3 alpha
> have
> done siulation
> alpha With
> Value mdl16g_cpud done simulation
> alpha
> have
> done simulation
> alpha With
> Value mdl16g_cpud done simulation
> 5
> alpha have
> done simulation
> Login successful
> Login successful
> Login successful
> Login successful
> Login successful
> alpha With
> Value fam_est
> rank
> done siulation
> 1310 alpha have done simulation
> reV_


总结反思：

1.代码效率：

考虑到brain平台最大可同时进行10个simulation,将开始的循环改为了并行运算大幅减少了运行时间。

2.debug经历：

requests进行登陆操作时偶尔会遇到失败的情况，构建函数在遇到某些情况的时候重新登陆。

所有用户每4个小时or提交过多错误simulation会被强制登出。所以每完成一定量的simulation后重新登陆，避免这一问题。

**Expression cannot be empty**表达式不能为空，该问题是忘加最后的表达式引发的。

3.选用模版以及适用的数据类型

参考模版为【Alpha灵感】通过期权隐含价格与股票市场价格的差异寻找投资机会

rank(ts_rank(mdl169_backfill_cpl - close, 22))

其中mdl169_backfill_cpl为隐含价格 可以用get_datafields(s,universe='ILLIQUID_MINVOL1M',search='Technical and Fundamental ranking model')

中的数据代替 其中的close 可以用一些表示价格的数据带入 由于此alpha turnover过高 ts_rank的时间 在[21,42,63] 中选择

4.后续改进思路

发现可以通过把 mdl169_backfill_cpl - close 改为 mdl169_backfill_cpl / close 大幅减少turnover 代价是减少了sharpe

想到 【Alpha灵感】分析师建议和回报率 这篇文章中提到的思路 用分析师预测价格对return回归 ， 想到可以用隐含价格对 close回归后 考虑beta值的大小

然后也可以在其他universe里进行尝试 比如GLB,寻找低相关的因子。

---

### 评论 #6 (作者: WL13229, 时间: 2年前)

[MM46273](/hc/en-us/profiles/14030346587927-MM46273)

同学您好，如果之后无法提交作业，您可能会在某个阶段被移除，需要下一期重新申请。对于下一次重新申请的同学，不建议使用完全同样的申请材料，因为我们会有更高的期待，例如期待您完成本次的作业。

---

### 评论 #7 (作者: WL13229, 时间: 2年前)

[YH69102](/hc/en-us/profiles/18490343218711-YH69102)

同学您好，感谢细心地完成了实践。根据经验，即便用户在一定量的simulation后重登录，系统依然会在你最远的一次登录4小时后登出。因此，这个解决方案可能还不够完善。您可以等待Http错误出现后，再持续地重复登录，直至成功。

---

### 评论 #8 (作者: ZC80223, 时间: 2年前)

2023.12.14


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 5,372
> Total Active Alphas
> 35
> Total Decommissioned Alphas
> Total Alphas
> 5,407
> 20:01
> 15rC 局部多云
> 入英  豳
> 2023/12/14


2023.12.18


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 7,461
> Total Active Alphas
> 35
> Total Decommissioned Alphas
> Total Alphas
> 7,496
> 11:29
> 15C 局部多云
> 英  豳
> 2023/12/18


关于确保提交不中断的机制：

1、表达式生成、simulation提交采用线程的方式


> [!NOTE] [图片 OCR 识别内容]
> def expression_generation_thread(pending_datafields_
> queue
> math_functions ,
> expressions_list ):
> While
> True:
> i not pending_datafields_queue
> empty():
> datafield_id
> pending_datafields
> queue. get()
> for
> func
> in math_functions:
> expression
> func(datafield_id)
> expressions_list.append (expression )
> 添加到列麦中
> else:
> time.sleep(1)
> 空队列时等待
> def simulation
> submission_thread
> session,
> 5imulation
> url,
> expressions_Iist,
> target
> simulation_count,
> Completed_simulations
> failed
> simulations
> While
> completed_simulations
> target
> simulation_count
> with expressions_list_Iock:
> batch_
> submit
> expressions_Iist[ : 1089]
> 可根据需要调整批次大小
> batch_
> to_submit:
> successful,
> failed
> submit_alphas (session,
> batch_to_
> submit,
> 5imulation_url )
> completed_simulations
> successful
> failed_simulations
> extend
> failed)
> With
> expressions
> Iist_Iock:
> 从列表中移除已提交的表达式
> expressions_Iist
> List(set(expressions_list)
> set (batch_to_submit )
> 等待更多麦达式生成或达到目标模拟计数
> 讦
> not
> expressions
> list
> and
> completed
> simulations
> target_simulation
> Count
> break
> time.sleep
> submission_interval )
> Completion_
> percentage
> (completed_simulations
> target_simulation
> Count )
> 100
> print(f"simulation
> completed. Success:
> {completed
> simulations},
> Failed:
> Len (failed_
> simulations ) }


2、主函数内增加断线重连的函数


> [!NOTE] [图片 OCR 识别内容]
> # Function
> reauthenticate
> needed
> def
> reauthenticate_if_needed():
> pesponse
> session
> ('https:
> /api.worldquantbrain.com /users / self
> if response.status
> Code
> 401:
> # Unauthorized,
> Session
> expired
> peturn
> start
> Session (username
> password )
> except RequestException:
> return start_session(username,
> password)
> return
> 5es5ion
> try:
> Bet


3、在表达式生成和simulation的线程中增加监听


> [!NOTE] [图片 OCR 识别内容]
> data
> thread
> Thread
> target=data_collection
> thread,
> args=
> reauthenticate_if_needed()
> fatasets_
> gata
> thread
> start()
> functions
> [ Lambda
> f' Zscore (ts
> mean({*},120))' ]
> expression_thread
> Thread
> target=expression_generation_thread,
> args=(pending_datafields_
> queue
> expression
> thread.start ( )
> target_simulation_count
> 1009
> 5imulation_url
> https : / /api.worldquantbrain
> COm/simulations
> simulation_thread
> Thread(target=simulation_submission_thread,
> args=(reauthenticate_if_needed
> 5imulation_
> thread. start
> math
 4、控制台输出


> [!NOTE] [图片 OCR 识别内容]
> Session started
> Datasets
> Ioaded
> Number
> of datasets
> Ioaded:
> 424
> Network
> error
> for expression:
> ZScore(ts_
> mean
> (anl14_recvalue_
> 120) )
> HTTPSConnectionPool (host=
> api. worldquantbrain
> COII
> port=443):
> Nax
> retries exceeded with url:
> /simulations
> (Caused
> ProxyError(
> Cannot
> Connect
> Proxy
> RemoteDisconnected (
> Remote
> end
> Closed
> connection Without response')))
> Failed submission
> for expression:
> Zscore(ts_mean (star_ebitda_analyst
> number
> fy2,128) )
> Response
> Status
> Code:
> 504
> Response
> Content:
> b'〈html>IrInheadxtitle>504 Gateway
> Time
> out</title> /head>IrInbody> Irlncenter><hl>504 Gateway
> Time
> out</hI>/center>Irln (body>Irln /html>Irln


感想：

首先看到这个控制台输出，比较无奈，目前程序还有至少2个bug：

- 目标队列应该限制了1000个simulation，实际上依次程序跑完居然simulate 1700+个，进一步需要排查门限失效原因
- 整个simulation和表达式生成做完了，程序没有自动结束，所以没有打印结果，一直处于活跃状态，需要做进程释放程序刹停，目前不知道问题出在哪，得花时间改。

关于遇到的困难和解决办法：

1、发现生成表达式虽然快，但检索datafield比较花时间，所以做了个异步，一边检索，一边就开始喂入simulation了，解决表达式列表在异步状态的去重是比较低效的。

2、api的吞吐量得测，不然会出现大量的提交不进去，有点忘了课上是怎么判定alpha已经出结果了，目前用了201、429做了response判定，约定出现429不再提交，转而提交等待队列的几个429，直到全部消化完等待队列，再提交新的。

3、单次跑下来实在有点久，可测的机会其实不是很多，所以先提交一个满足作业要求的版本，后续继续看改进。

4、关于alpha结果提取相关的逻辑都没写，关于如果遇到vector型怎么办，也没测。后面再补吧

---

### 评论 #9 (作者: WL13229, 时间: 2年前)

[YH69102](/hc/en-us/profiles/18490343218711-YH69102)

感谢您的详尽回答。通过您的回复，我总结了如下几个您提出的问题，希望有帮助。

***“回测应该回测了3000多个实例，但由于某种原因，丢失了1700个实例。已经设置了一个sleep函数，以防止访问次数过多，并一直在监视status_code以查找错误。但依然出现此问题，如何解决？”***

答：simulation_response.status_code为201并不代表你的Alpha运行没有问题，运行有问题的Alpha就是会被丢失的。您可以运行一下下列代码，体会一下错误的来源：

```
simulation_data = {    'type': 'REGULAR',    'settings': {        'instrumentType': 'EQUITY',        'region': 'USA',        'universe': 'TOP3000',        'delay': 1,        'decay': 15,        'neutralization': 'SUBINDUSTRY',        'truncation': 0.08,        'pasteurization': 'ON',        'unitHandling': 'VERIFY',        'nanHandling': 'OFF',        'language': 'FASTEXPR',        'visualization': False,    },    'regular': 'high-close+dfd'}simulation_response = s.post('https://api.worldquantbrain.com/simulations', json=simulation_data)print(simulation_response.status_code)print(s.get(simulation_response.headers['Location']).json())print(f'status: {s.get(simulation_response.headers["Location"]).json()["status"]}')
```

***"在处理 `get_result` 函数时遇到了困难，因为它的复杂性。数据结构复杂，有许多嵌套的字典，并且返回了许多性能指标。在选择指标和对dataframe排序时遇到了麻烦"***

答：嵌套的字典不应该成为一个很大的问题，可以思考如何存储字典类数据。或者摘取重要的指标，如Sharpe, Fitness等先进行存储。对于返回的嵌套的字典，你需要仔细阅读它能提供的信息，做到心中有一个基本的印象，这对以后研究和绩效分析将会有帮助。

***“遇到了一个问题，不确定是数据本身在模拟过程中使模板从反转变为动量，还是数据在模板下无效。这使得确定模板的属性变得困难。”***

答：模板本身如果是动量，那么就应该是动量。如果在替换数据字段的过程中，performance发生了反转，然后你再加一个负号上去，那么说明你已经偏离了模板本身，有走向overfitting的危险。

***“不确定SLOW+FAST参数的代码，并且缺少一个参数。”***

答：SLOW_AND_FAST

***"需要进一步设计获取相关性（corr）的接口，因为当前的corr检查仍然处于待处理状态，需要额外的指令才能执行。"***

答：检查相关性的API的使用方式已经在这个帖子提出👉 [BRAIN API可以实现的功能 – WorldQuant BRAIN]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md) ，欢迎参考。

***”当使用模板进行模拟时，结果不好，有些时间点显示出平坦的曲线，表明该模型在那些时间没有股票选择能力。“***

答：请手动找到这个Alpha进行查看。在网页浏览器输入“ [https://platform.worldquantbrain.com/alpha/AlphaID”,即可以看到它的表现。一般这种Alpha的出现是因为使用Alpha前的数据处理工作还不够好。这个我们会在未来的课程中提到，并给出一些指导建议。](https://platform.worldquantbrain.com/alpha/AlphaID%E2%80%9D,%E5%8D%B3%E5%8F%AF%E4%BB%A5%E7%9C%8B%E5%88%B0%E5%AE%83%E7%9A%84%E8%A1%A8%E7%8E%B0%E3%80%82%E4%B8%80%E8%88%AC%E8%BF%99%E7%A7%8DAlpha%E7%9A%84%E5%87%BA%E7%8E%B0%E6%98%AF%E5%9B%A0%E4%B8%BA%E4%BD%BF%E7%94%A8Alpha%E5%89%8D%E7%9A%84%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86%E5%B7%A5%E4%BD%9C%E8%BF%98%E4%B8%8D%E5%A4%9F%E5%A5%BD%E3%80%82%E8%BF%99%E4%B8%AA%E6%88%91%E4%BB%AC%E4%BC%9A%E5%9C%A8%E6%9C%AA%E6%9D%A5%E7%9A%84%E8%AF%BE%E7%A8%8B%E4%B8%AD%E6%8F%90%E5%88%B0%EF%BC%8C%E5%B9%B6%E7%BB%99%E5%87%BA%E4%B8%80%E4%BA%9B%E6%8C%87%E5%AF%BC%E5%BB%BA%E8%AE%AE%E3%80%82)

***”在做出调整和中和beta后，净值曲线也接近市场趋势。“***

答：这个观察不错，说明您已经开始思考，如何提升template。

---

### 评论 #10 (作者: WL13229, 时间: 2年前)

[ZC80223](/hc/en-us/profiles/16412175793303-ZC80223)

同学您好，

simulation_response.status_code为201并不代表你的Alpha运行没有问题，运行有问题的Alpha就是会被丢失的。status_code为201仅代表着，目前并不处于too many simulation的状态。查看alpha是否在正常simulate，您需要查看s.get(simulation_response.headers['Location']).json()这个代码中的‘status’字段

---

### 评论 #11 (作者: WL13229, 时间: 2年前)

[YL93001](/hc/en-us/profiles/18134743066519-YL93001)

谢谢您完成此次case。注意到您的代码还普遍使用ACE比赛提供的代码，个人建议您使用 [BRAIN API可以实现的功能 – WorldQuant BRAIN]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md)  API的原生功能重写。否则到后面内容越来越多时，您可能难以修改源代码。

---

### 评论 #12 (作者: JL23162, 时间: 2年前)

1与2的任务


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 1.
> GOOD
> Total Unsubmitted Alphas
> 4,345
> Total Active Alphas
> 64
> RCELLENT
> SFECTACULR
> Total Decommissioned Alphas
> Total Alphas
> 4,409
> 23:15
> &  中  拼
> 谷 4) v
> 2023/12/17



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 4@
> GOOD
> Total Unsubmitted Alphas
> 5,414
> Total Active Alphas
> 64
> RCELLENT
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 5,478
> 12:16
> ^ 中  拼 谷 d) 匈
> 2023/12/18


3.运行代码截图


> [!NOTE] [图片 OCR 识别内容]
> 控制台 2/4 X
> 31 UUI
> arpiauJlu: SIINOPVCJ JIJ
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:  3
> 当前队列位置为: 4
> 当前队列位置为:
> 当前alpha的id:nnmo783己执行完成
> 当前队列位置为:
> 当前队列位置为:
> 当前队列大小为:
> 当前队列大小为:
> 10
> 当前队列位置为:
> 当前alpha的id: 7x3Qjx8己执行完成
> 当前队列位置为:
> 当前alpha的id: dnymjoy 己 执行完成
> 当前队列位置为:
> 当前alpha的id:OnRk7xY 己 执行完成
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:
> 当前队列大小为:
> 当前队列大小为:
> 当前队列大小为:
> 10
> 当前队列位置为:
> 当前alpha的id: OnRVqKE 己 执行完成
> 当前队列位置为:
> 当前alpha的id: Bmxkjboe 执行完成
  
> [!NOTE] [图片 OCR 识别内容]
> 控制台  1/4 人
> 当前队列位置为:
> 当前alpha的id: QnoEevo己执行完成
> 当前队列位置为:  1
> 当前队列位置为:
> 当前alpha的id:ZjgrZan己执行完成
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:
> 当前alpha的id:AnekGLd己执行完成
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:
> 当前alpha的id: RNgdXSa己执行完成
> 当前队列位置为:
> 当前alpha的id: GnXkVKo己执行完成
> 当前队列位置为:
> 当前alpha的id: I7Erx5O己执行完成
> 当前队列位置为:
> 当前队列位置为:
> 当前队列位置为:
> 当前alpha的id:enNLAGg己执行完成
> 全部回测完成


4.总结反思：
当前代码效率应该是达到服务器上限的了 由于上限是10个 提交10个的同时检测是否在10个中回测完毕的 再继续添加 使得总回测队列始终保持10个
debug上 当前代码会因为网络问题断开链接 导致后续回测不了 我昨晚跑的 早上起来看只测了700个 剩下300个是今天早上补的

当前模板数据类型支持martix和vector 我的vector处理直接加入了vec avg，其他的如group数据就会直接drop掉
当前的改进方向应该是如何继续拓展迭代 使得其能够自动跑，并且检验提交，还有自动重启（不论是网络问题 还是长时间 login in的问题）当前只能指定数据字段 按照指定单个模板回测 ，还应该加入多个模板 ，以及判断通过条件数量 按照某一方向继续修改的功能

---

### 评论 #13 (作者: WL13229, 时间: 2年前)

[JL23162](/hc/en-us/profiles/18456131969431-JL23162)

很高兴看到您的代码至少已经实现了断点查找的功能，即您可以清楚地知道代码是从哪个Alpha断开的，然后继续重联。至于如何解决断线（断点）问题，您可以参考该链接👉 [BRAIN API可以实现的功能 – WorldQuant BRAIN]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md) 的更新内容之《 **一种解决超时登出的解决方案》**

---

### 评论 #14 (作者: EH13432, 时间: 2年前)

**任务提交：**


> [!NOTE] [图片 OCR 识别内容]
> Window
> Help
> 叩 』
> 8剧s
> 8
> Sat 10:11 AM
> C @  &
> 匕
> New chat
> 网易邮箱
> notion
> 腾讯企业邮箱
> 收.
> Claude
> 》
> 口 Al Bookmarks
> EnGOTACE 2023!
> ACE Seres Part 2: BUICINB Versatle Frameworks
> 2023
> 24th
> On Dealing With FX In Multi-Currency Regions
> International Quant
> International Quant
> Championship 2023
> Leaderboard
> Championship 2023
> Leaderboard
> Stage 2 (Final)
> Stage 2
> Stats
> Stats
> Rank:
> 1,259
> Rank:
> 1,626
> Score:
> 29,716
> Score:
> 3,358
> Level:
> No Level
> Level:
> No Level
> Q Alphas
> See all
> Achievements
> Vlew Achlevements
> Status
> 20
> 4R
> 10
> GOOD
> Total Unsubmitted Alphas
> 1,535
> Total Active Alphas
> 35
> BXCELLAITT
> SELICULN
> Total Decommissioned Alphas
> Total Alphas
> 1,570
> AUg
  
> [!NOTE] [图片 OCR 识别内容]
> Window
>  Help
> 8js
> Q
> 品
> Mon Dec 18 1:48 PM
> C @  众
> New chat
> 网易邮箱
> notion
>  ]腾讯企业邮箱
> 收。
> Claude
> 》 |口 All Bookmarks
> EnGOTACE 2023!
> Achevement Unocked!
> On Dealing With FX In Multi-Currency Regions
> International Quant
> International Quant
> Championship 2023
> Leaderboard
> Championship 2023
> Leaderboard
> Stage 2 (Final)
> Stage 2
> Stats
> Stats
> Rank:
> 1,259
> Rank:
> 1,626
> Score:
> 29,716
> Score:
> 3,358
> LeVel:
> No Level
> Level:
> No Level
> Q
> Alphas
> See all
> Achievements
> View Achlevements
> Status
> 20
> 4R
> 1
> GOOD
> Total Unsubmitted Alphas
> 2,820
> Total Active Alphas
> 36
> ECELLAIT
> SLECICULHH
> Total Decommissioned Alphas
> Total Alphas
> 2,856


出现链接错误，自动重连

**
> [!NOTE] [图片 OCR 识别内容]
> 389
> Alpha done simulating, getting alpha
> details
> 390
> Alpha done simulating, getting alpha details
> 391
> Alpha done
> SimU
> Ilating, getting alpha details
> 392
> Alpha done simulating, getting alpha details
> 393
> Alpha done simulating, getting
> alpha details
> 394
> Alpha done simulating, getting alpha details
> 395
> ProxyError:
> HTTPSConnectionPool (host= 'api.worldquantbrain. com
> port=443):
> Max
> retries
> exceeded With url:
> /simulations /INyGRjso4r
> 396
> ProxyError:
> HTTPSConnectionPool (host='api.Worldquantbrain.com
> port=443):
> Max retries
> exceeded With url:
> /simulations /RRSNCfjg41
> 397
> ProxyError:
> HTTPSConnectionPool (host= 'api.worldquantbrain.com
> port=443) :
> Max
> retries
> exceeded With url:
> /simulations / 41dc8x6C24
> 398
> ProxyError:
> HTTPSConnectionPool (host= 'api.Worldquantbrain. com
> port=443):
> Max retries
> exceeded
> With url:
> /simulations /3OFb7ISDRC
> 399
> ProxyError:
> HTTPSConnectionPool (host= 'api.Worldquantbrain. Com
> port=443):
> Max retries exceeded With url: /simulations/4Ayjcpz]4l
> 400
> ProxyError: HTTPSConnectionPool (host= 'api.worldquantbrain。
> port=443) :
> Max retries exceeded With url:
> /simulations /2OKgngeoa
> 401
> Alpha done
> simulating, getting
> alpha details
> 402
> ProxyError:
> HTTPSConnectionPool (host= 'api.Worldquantbrain.com
> port=443) :
> Max
> retries
> exceeded With url:
> /simulations / 450FN3bfL
> 403
> ProxyError:
> HTTPSConnectionPool (host= 'api.worldquantbrain. com
> port=443)
> Max
> retries
> exceeded
> With url:
> /simulations / 3Kd4ylgt3s
> 404
> Alpha done
> simulating, getting alpha
> details
> 405
> Alpha done simulating, getting alpha
> details
> 406
> Alpha done simulating, getting alpha
> details
> 407
> ProxyError:
> HTTPSConnectionPool (host=
> Worldquantbrain.Com
> port=443): Max retries exceeded with url:
> /simulations / 208y621940
> 408
> Alpha done simulating, getting alpha details
> 409
> Alpha done simulating, getting
> alpha details
> 410
> ProxyError: HTTPSConnectionPool (host='api.Worldquantbrain. com
> port=443)
> Max retries exceeded With url:
> /simulations / 2p72419106
> 411
> Alpha done simulating, getting alpha details
> 412
> Alpha done simulating, getting alpha
> details
> 413
> Alpha done simulating, getting alpha
> details
> 414
> Alpha done simulating, getting alpha
> details
> 415
> Alpha done simulating, getting alpha
> details
> 416
> Alpha done simulating, getting alpha details
> 417
> Alpha done simulating, getting alpha details
> 412
> 01nh3
> Tnno
> C1
> mll73+inn
> qot+inr
> 31nha
> dot311e
> COm
> api
**

单独实施1000次回测可以成功提交977次simulation


> [!NOTE] [图片 OCR 识别内容]
> main:py
> tryipynb
> tryipynb (output)
> worldquant_func py
> Apidataset ipynb
> 340
> EqIWgWL
> 949
> VSZLeIG'
> 950
> SLrWL3k'
> 951
> dnYxQSE
> 952
> pnx67Px
> 953
> 80V229a
> 954
> gmxllXe
> 955
> 'onRKUI5
> 956
> 'RNgp8gg
> 957
> WS3REEI
> 958
> YN8pVqZ'
> 959
> EqNwGmP
> 960
> 2v971ZY'
> 961
> XkVpWjl'
> 962
> OnRKGUn
> 963
> Ygpbjl'
> 964
> jnoZAe0
> 965
> dnyxley'
> 966
> 'W3pezx
> 967
> OnOaYqM
> 968
> 1007jR
> 969
> SLFWEWI
> 970
> Zjgpooj
> 971
> 0n0a075
> 972
> RNgpSaj
> 973
> MbdpgNz
> 974
> WNJLJjM
> 975
> enNOVpl'
> 976
> Zjgpdk8
> 977
> 3E17PWe


**想法记录**

本周的任务主要还是在搭建上，我构造了一些函数，如多重模拟函数——给每个可调整参数传递一个列表或值，函数可以自动组合构建alpha进行回测。最终返回alpha的id列表，以及输入id列表，可以生产is和performance corr的dataframe等等。


> [!NOTE] [图片 OCR 识别内容]
> 严 》 D 曰
> 血
> percompar_to_df (s, [ ' gmXloqg
> 'LnEplwm
> SLFwaWo
> [15]
> 1.9s
> Python
> varLfoldersLjyLdphblthg4g554d4pkqbhekcro@@@gnLILipykernel 61737/341704252.py:63:
> FutureWarning:
> The behavior of
> DataFrame concatenation With empty
> df
> pd.concat
> [df
> pd.DataFrame
> [row] ) ]
> ignore_index=True)
> id
> bookSize
> pnl
> longCount
> shortCount
> drawdown
> turnover
> returns
> margin
> sharpe
> ftness
> gmXloqg
> 4707801.0
> 374
> 359
> 0.0002
> 0.1270
> -0.0224
> -0.001012
> -0.75
> -1.48
> LnEplwm
> 3996369.0
> 34
> 0.0245
> 0.1202
> -0.0297
> -0.001044
> -1.00
> -1.67
> SLrWaWO
> 4879422.0
> 367
> 351
> 0.0052
> 0.1267
> -0.0207
> -0.000998
> -0.73
> -1.46



> [!NOTE] [图片 OCR 识别内容]
> 3二
> ['OnRA7XJ
> 0.0S
> Python
> is_Check_to
> ( ['gnX1oqg
> LnEplWm
> SLFwaWo
> ]
> 1.2s
> Python
> LOW_SHARPE
> LOW_FITNESS
> LOW_TURNOVER
> HIGH_TURNOVER
> CONCENTRATED_WEIGHT
> LOW_SUB_UNIVERSE_SHARPE
> UNITS
> SELF_CORRELAI
> gmx1oqg
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> LnEplwm
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> SLrwawo
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> Ldf


**关于登出情况的调整：**

我一开始只是简单的构造try except函数，在出现http error时候重新登陆，但后来发现登出时候的报错更为复杂，又增加了一些except再重新登陆的条件。目前运行4小时以上不会报错了，但自己也没搞明白自己的代码逻辑到底对不对。或许还是应该从状态码是否等于201来判断

**关于模版选取**

模版上，选用了新闻动量篇的思路，因为我觉得该篇在思路上本质就是情绪和交易量对回报率的回归，模版比较有行为金融学意义，且比较可以复制，故对情绪相关数据进行了一下简单的处理就代入进去了。事实上，大部分的sentiment都可以获得一个比较理想的alpha


> [!NOTE] [图片 OCR 识别内容]
> 1OM
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
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.37
> 40.25%
> 1.37
> 13.509
> 5.489
> 6.71%o。


**改进**

开始时候我没有写明白同时提交10个alpha的函数逻辑，导致生成速度很慢，一测测一天，且电脑一出现问题就容易前功尽弃。一开始想的是，打包10个alpha进一个组，再用多重模拟进行回测，现在改用多线程来处理，大大加快了测试速度。

**问题**

目前我的代码在运行1000次成功回测的时间大概是2个小时到2个半小时之间，这是一个正常的速度吗？还是可以再进行优化？

我生成dataframe的函数在alpha id列表一长就很容易报错，同样的输入有时候可以成功，有时候会报json decode error，不明白是为什么。本人没有经过系统学习过代码，不是很明白，恳请大家帮我看看。并且有什么改进的办法吗？


> [!NOTE] [图片 OCR 识别内容]
> main py
> tryipynb
> Apiipynb
> Worldquant_func.py
> Apidataset ipynb
> Api.ipynb
> MI
> '把IS_CHECK结果放到一个列表中
> is_check_to_dffa)
> 十
> Code
> 十 Markdown
> Run AlI
> 9 重启
> Clear AII Outputs
> Go To
> 变量
> :大纲
> Python 3.12
> 972 except
> JSONDecodeError
> as
> e:
> 973
> Catch JSON-related errors and raise as requests.JSONDecodeError
> 974
> This aliases json.JSONDecodeError and simplejson.JSONDecodeError
> File LLibraryLlErameworks/Python.frameworkLVersions/3,12LlibLpython3.12Ljson/
> I让
> Py:346,
> in loads(S,
> ClS,
> object_hook; parse_float,
> parse_int,
> 343 讦
> (Cls is None and object_hook is None and
> 344
> parse_int is None and parse_float is None and
> 345
> parse
> constant is None and object_pairs_hook is None and not
> K)
> 346
> return
> default_decoder. decode(s)
> 347 if Cls
> is None:
> File LLibraryLErameworksLPython.framewockLVersionsL3.12LLibLpython3.12LjsonLdecodec py:337,
> in JSONDecoder.decode (self;
> 51
> 333
> Return the
> Python representation of
> (a
> Str
> instance
> 334 containing
> a JSON document)
> 335
> 336
> 337 obj;
> end
> self. raw_decode(s,
> idx=_W(s, 0).end() )
> 338 end
> _W(s, end).end()
> File LLibraryLErameworks/Python.framewockNersions/3.12LlibLpython3,12LjsonLdecodec  py:355,
> i JSONDecoder. raw_decode (self;
> 51
> idx)
> 973
> # Catch JSON-related errors and raise
> as requests.JSONDecodeError
> 974
> # This aliases json.JSONDecodeError and simplejson.JSONDecodeError
> 915
> raise RequestsJSONDecodeError(e.msg,
> e.doc,
> 巳:
> pos)
> JSONDecodeError:
> Expecting Value:
> line
> 1 Column
> 1 (char 0)
> Output is truncated. View as a Scrollable element or open in a text editor: Adjust cell output settings:
> PRORIFMC
> OIITOIT
> DFRIIG CONGOIF
> TFPNNAI
> DOPTC
> JIIIDVTFP
> CN)


---

### 评论 #15 (作者: WL13229, 时间: 2年前)

[EH13432](/hc/en-us/profiles/13837178860951-EH13432)

非常完整的作业，令人感动。

***"目前我的代码在运行1000次成功回测的时间大概是2个小时到2个半小时之间，这是一个正常的速度吗？"***

答：速度是正常的。看到您也获得了一个新可提交的Alpha,从效率上看，大约1000次simulation获得一个Alpha也是正常的效率，这个说明您的模板选择和数据选择都比较合适。另外一个检测自己速度是否合适的方法就是，回到网页界面，尝试手动simulate一下Alpha,如果会报错“too many simulation at a time”，这就说明代码正在全力工作，占用完了十个线程，算是高效了。

***“我生成dataframe的函数在alpha id列表一长就很容易报错，同样的输入有时候可以成功，有时候会报json decode error”***

答：初步猜想，这个的原因是因为你尝试解析一些提交失败或者没有获得simulation结果的Alpha导致的。我建议你使用try方法，确定json可以解析后再放入dataframe.或者，你可以创建一个csv文件，在确定json可解析后，把json结果append到csv文件的最新一行。

---

### 评论 #16 (作者: BX78946, 时间: 2年前)

首先是上周的截图 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 10,285
> Total Active Alphas
> 93
> Total Decommissioned Alphas
> Total Alphas
> 10,378
> 20:19
> d)
> ENG
> 2023/12/14


然后是今天的截图


> [!NOTE] [图片 OCR 识别内容]
> A
> 12月18日周一
> 上午9:16
> 起始页
> SuperAlphas: Selection and Combo techniques
> Achievement Unlocked!
> ACE Series Part 2:
> Building Versatile Frameworks
> 2023 Aug 24th
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 11,613
> Total Active Alphas
> 93
> Total Decommissioned Alphas
> Total Alphas
> 11,706


最后附上连续提交1000个alpha的输出：


> [!NOTE] [图片 OCR 识别内容]
> Simulation
> sent successfully。
> Now,
> yoU
> have simulated
> 1
> alphas
> Simulation
> sent successfully。
> Now,
> you have simulated
> 2
> alphas
> Simulation
> sent successfully.
> Now,
> yOU
> have siulated
> 3 alphas
> Simulation sent successfully.
> Now,
> yOU
> have siulated
> 4 alphas
> Simulation sent successfully.
> Now
> yoU
> have
> siulated
> 5
> alphas
> Simulation
> sent successfully。
> Now,
> yoU
> have simulated
> 6 alphas
> Simulation
> sent successfully。
> Now 
> yoU
> have simulated
> 7
> alphas
> Simulation
> sent successfully。
> Now,
> yOU
> have siulated
> 8 alphas
> Simulation sent successfully.
> Now,
> yOU
> have siulated
> 9 alphas
> Simulation sent SUCCessfUlly.
> Now,
> yoU
> have
> siulated
> 10 alphas
> 429
> Sleep
> 429
> Sleep
> Simulation
> sent successfully。
> Simulation
> sent successfully。
> NOW
> yOU
> have siulated
> 1019 alphas
> Simulation sent SUCCessfUlly.
> Now,
> you have simulated
> 1020 alphas


代码方面主要是用了这个链接里的代码 [[L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md可以实现的功能]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md)  以及之前mee tup的内容，然后根据老师上课的建议内容，可以将输出的alpha的结果保存到一个csv文件中，方便进一步操作。


> [!NOTE] [图片 OCR 识别内容]
> d,type,author, settings , regular, datecreated , dateSubmitted , dateModified , name , favorite , hidden , color, category , tags , grade, stage, status, is, Os, prod , competitions , themes
> team
> O0Vgq6 , REGULAR, BX78946,
> {'instrumentType
> EQUITY'
> region
> CHN
> universe
> T0P3000
> delay
> 1,
> decay
> 4,
> neutralization
> INDUSTRY
> truncation
> 
> 0.1,
> pasteurizat
> n01190, REGULAR, BX78946,
> {'instrumentType
> EQUITY
> region
> CHN
> universe
> T0P3000
> delay
> 1,
> decay
> 4,
> neutralization
> INDUSTRY
> truncation
> 
> 0.1,
> pasteurizat
> nmk3Lq, REGULAR, BX78946, "{ 'instrumentType
> EQUITY
> region
> 
> CHN
> universe
> T0P3000
> delay
> 
> 1,
> decay' :
> 4,
> neutralization
> INDUSTRY
> truncation
> 
> 0.1,
> pasteurizat


同时我也保存了整个performance_comparison的结果进一个csv文件。虽然都没有进行进一步的操作，主要是尝试一下。然后我总是在第一次登录的时候会遇到提示"connection down, trying to login again”，这个过程有时候持续很久才会显示Response [201]登陆成功，不知道是为啥，虽然每次最后都登录进去了。

Debug经历主要还是感谢gpt等大模型工具，可以通过他们实现很多想法。

我的模版是参考的 [[L2] 【Alpha灵感】偏斜性偏好和市场异象_19507603510039.md灵感-偏斜性偏好和市场异象]([L2] 【Alpha灵感】偏斜性偏好和市场异象_19507603510039.md)  这篇文章，通过这位consultant 的想法首先构造出来

```
-rank(vec_avg(oth41_s_tech_skewness))*rank(mdl175_revs10)
```

这个alpha，然后在这个基础上加上对市值进行中心化处理，其实就已经得到了一个可以通过除了prod_corr以外所有测试的alpha了。然后对于oth41_s_tech_skewness和mdl175_revs10，我通过搜索他们的dataset，并且分别搜索了“skewness”和“return”这两个关键词，用api筛选了很多datafields，然后用这些datafields遍历组合，最后可以得到很多通过测试的alpha，但是都没有通过prod_corr相关性的检测。

后续的改进：可能是由于我筛选用了关键词搜索以后，能通过测试的alpha之间相关性都很高，所以没有办法通过prod_corr的测试。我感觉从我自身的经历来讲，想得到一个表现还可以的alpha其实没有那么难，难的是怎么能够通过所有的相关性的检验，还是需要多想多看，得到一些新的idea才可以。有可能通过暴力调参能够让检验都通过，但感觉对自身的提升也没什么帮助，希望能通过这个课程有更多的提升。

---

### 评论 #17 (作者: WL13229, 时间: 2年前)

[BX78946](/hc/en-us/profiles/16297370627607-BX78946)

您的思考非常深入。没有通过production测试的原因，主要是因为核心在于使用了下列这个为主信号的Alpha

```
rank(mdl175_revs10)
```

确实如您所说，后续您的筛选方式，大多获得的是同样的idea。其实解决此类问题，我们需要思考一下，这个template的本质是什么？当你使用两个rank相乘时，其实它的本质就变成了两个排序的交叉验证（注意，与加号不同）。且这里前面有个负号，说明这个模板在捕捉的信息是：“如果一个股票同时满足A和B，我就做空”。
因此，该模板其实泛化能力还是比较强的，只专注于return和skewness就会造成correlation高的问题。

但是需要注意的是，一昧的泛化和尝试不同数据集，或“暴力调参”，可能会使得过拟合。因此，我们在寻找A和B时，最好保证它们是在相同维度，或者是同类数据集里的。

最后多说一句，这种泛化能力强的模板，往往效率不高，尤其在面对coverage不高的数据集时，效率会大打折扣。

---

### 评论 #18 (作者: YT14523, 时间: 2年前)

1、 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 1,614
> Unsubmitted:
> 1,592
> Active:
> 22
> Decommissioned:
> 0
> 4i
> 220
> 23:50
> Q 搜索
> PC
> 英
> 谷 dx 回
> 阴
> NEW
> 2023/12/14


2、 
> [!NOTE] [图片 OCR 识别内容]
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 2,710
> Filter 
> Unsubmitted:
> 2,688
> Active:
> 22
> ItUS
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> e.8>1
> e.8>1
> e.8>1
> Select
> aTOTYIOUs
> RegWIaT
> UNSUBMIT
> 12/17/2023 EST
> CHN
> TOP2000
> 0.57
> 3.169
> 2.349
> anonymous
> Regular
> UNSUBMIT
> 12/17/2023 EST
> CHN
> TOP2000
> 0.70
> 4.31%
> 2.389
> anonymous
> Regular
> UNSUBMIT。
> 12/17/2023 EST
> CHN
> TOP2000
> 0.99
> 7.479
> 2.959
> anonymous
> Regular
> UNSUBMIT。
> 12/17/2023 EST
> CHN
> TOP2000
> 1.02
> 7.969
> 2.889
> anonymous
> Regular
> UNSUBMIT
> 12/17/2023 EST
> CHN
> TOP2000
> 1.00
> 7.509
> 2.949
> anonymous
> Regular
> UNSUBMIT.
> 12/17/2023 EST
> CHN
> TOP2000
> 0.51
> 1.919
> 2.749
> anonymous
> Regular
> UNSUBMIT。
> 12/17/2023 EST
> CHN
> TOP2000
> 0.92
> 6.679
> 3.009
> 4i
> anonymous
> Regular
> UNSUBMIT.
> 12/17/2023 EST
> CHN
> TOP2000
> -0.36
> -1.259
> 2.879
> anonymous
> Regular
> UNSUBMIT
> 12/17/2023 EST
> CHN
> TOP2000
> 0.51
> 1.819
> 2.699
> anonymous
> Regular
> UNSUBMIT。
> 12/17/2023 EST
> CHN
> TOP2000
> -0.37
> -1.389
> 2.889
> 17.19
> Q 搜索
> PC
> 英 。 dx 匈
> NEW
> 2023/12/17


3、 
> [!NOTE] [图片 OCR 识别内容]
> Welcome
> simulation py
> simulation code.ipynb
> jupyter_simulation ipynb
> C: > Users
> 86185
> PycharmProjects
> worldquant alpha
> simulation code:ipynb >
> # get datas
> 十 Code
> Markdown
> Run All
> Restart
> Clear AII Outputs
> Variables
> Outlir
> response
> Session.
> (f"https:
> api. worldquantbra
> alphas
> response.json() ["results
> 」
> fetched_alphas .extend(alphas )
> if len(alphas)
> Iimit:
> break
> offset
> +=
> Iimit
> return
> fetched_alphas [ :total_alphas ]
> IS_
> result
> n_is_alphas (s, total_alphas=2oo )
> [13]
> 74m 34.65
> Simulation sent successfully
> AIphasNum:
> 1153
> Simulation
> sent successfully
> AIphasNum:
> 1154
> Simulation
> sent successfully。
> AIphasNum:
> 1155
> Simulation
> sent successfully
> AIphasNum:
> 1156
> Simulation
> sent successfully
> AIphasNum:
> 1157
> Simulation
> sent successfully
> AIphasNum:
> 1158
> Simulation
> sent successfully
> AIphasNum:
> 1159
> Simulation
> sent successfully
> AIphasNum:
> 1160
> Simulation
> sent successfully
> AIphasNum:
> 1161
> Simulation
> sent successfully
> AIphasNum:
> 1162
> Simulation
> sent successfully。
> AIphasNum:
> 1163
> Simulation
> sent successfully
> AIphasNum:
> 1164
> Simulation
> sent successfully
> AIphasNum:
> 1165
> Simulation
> sent successfully
> AIphasNum:
> 1166
> Simulation
> sent successfully
> AIphasNum:
> 1167
> Simulation
> sent successfully
> AIphasNum:
> 1168
> Simulation
> sent successfully
> AIphasNum:
> 1169
> Simulation
> sent successfully
> AIphasNum:
> 1170
> Simulation
> sent successfully。
> AIphasNum:
> 1171
> Simulation
> sent successfully
> AIphasNum:
> 1172
> Simulation
> sent successfully
> AIphasNum:
> 1173
> Simulation
> sent successfully
> AIphasNum:
> 1174
> Simulation
> sent successfully
> AIphasNum:
> 1175
> Simulation
> sent successfully
> AIphasNum:
> 1176
> Simulation
> sent successfully
> AIphasNum:
> 1177
> Simulation
> sent successfully
> AIphasNum:
> 1178
> Simulation
> sent successfully
> AIphasNum:
> 1179
> get
> Bet


3、反思：

整个代码在原来的基础上，在simulation的循环中加入了每simulate成功除了输出successfully，再加上是第几次simulation，整体上是能成功模拟1000次以上的，但是只是将所有的dataframe呈现出来并挑选的拥有超过1000个数据字段的dataset来模拟。并且使用的数据集是A股基本面数据，从1000次simulation的结果来看这个数据并不是很适用，sharpe，return及其他指标表现都不好且不会有很大的变化，从使用的alpha表达式上看应选择与价格和成交量相关性高的数据，尝试其他数据集的效果都不是很好，因此想尝试让代码遍历所有dataset，将每一个dataset都进行模拟来寻找一个合适的数据集并进行不间断地不同数据集的模拟，但模拟需要很长时间。


> [!NOTE] [图片 OCR 识别内容]
> for
> 1
> in range(69):
> dataset_id
> all_datasets.at [i, 'id' ]
> datafields_df
> datafields(s,
> dataset_id)
> datafields_df.head()
> print(datafields_df.head())
> count
> for
> 1
> in datafields_df['id' ]:
> simulation_data
> {
> type
> REGULAR
> settings
> {
> get


并且在模拟到一半的时候出现了几种报错，表达式没有问题，也并没有超时登录


> [!NOTE] [图片 OCR 识别内容]
> # Sending
> 3
> VaLId
> response.
> 287
> raise RemoteDisconnected("Remote end closed
> connection
> Without
> 288
> response")
> 289 try:
> RemoteDisconnected:
> Remote
> end
> Closed
> connection
> Without
> response
> During handling of the
> above exception,
> another exception occurred:
> ProtocolError
> Traceback (most
> recent
> Call
> Iast )
> File
> C:WUserslgGI8SIAppDatalLocallProgramslPythonleythonzlllLiblsite-packages
> L旦
> 485 try:
> 486
> resp
> conn.urlopen(
> 487
> method=request .method,
> 488
> url=url,
> 489
> body=request .body,


效率问题上只进行换数据集的模拟还是很慢的，思考改进方法：如果要找到合适的数据并能减少不必要的模拟来提高效率，可能可以加入对alpha performance 的判断，遍历所有的dataset，如果simulate一定数量后alpha表现并不好且sharpe或return变化很小甚至为负值时，就换下一个dataset进行模拟，如果模拟的前几个表现有提升的迹象，那么就继续使用这个dataset里的数据字段。

---

### 评论 #19 (作者: YW54232, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Total: 18,396
> Unsubmitt
> Alpha Lists
> Unsubmitted:
> 18,385
> Active:
> 11
> Decommissioned:
> 0
> Can be i
> Good Alpha
> Comparison List
> Comparison List
> Total Alphas
> 8
> Total Alphas
> 20:10:21
> 岂  圈  英 5
> g
> 2023/12/17



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Total: 20,882
> Unsubmitt
> Alpha Lists
> Unsubmitted:
> 20,871
> Active:
> 11
> Filter 
> Decommissioned:
> 0
> Select Columns
> ItUS
> Date Created (EST)
> Region
> Unive
> Search
> Select
> Select
> Select
> Search
> Select
> Sele
> anonymous
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> USA
> TOP3
> anonymous
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> USA
> TOP3
> anonymous
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> USA
> TOP3
> 17:40:01
> 岂  囤  英 5
> gi
> 2023/12/18


模拟了约2500个alpha


> [!NOTE] [图片 OCR 识别内容]
> #
> Process
> the alpha_details
> as needed
> #
> This
> is just
> a
> template
> to get you started,
> you will need
> to handle exceptions
> and
> erroTs
> accordingly 
> [15]
> Simulation start
> Simulation start
> Simulation start
> Simulation start
> Simulation start
> Simulation start
> Simulation start
> Simulation start
> Alpha done simulating, getting alpha details
> Simulation start
> Alpha done simulating, getting alpha details
> Simulation start
> Alpha done simulating;
> getting alpha details
> Alpha done simulating,
> getting alpha details
> Alpha done simulating, getting alpha details
> Simulation start
> Simulation start
> Simulation start
> Alpha done simulating, getting alpha details
> Simulation start
> Alpha done simulating, getting alpha details
> Simulation start
> Alpha done simulating, getting alpha details
> Simulation start
> Alpha done simulating, getting alpha details
> Alpha done simulating, getting alpha details
> Alpha done simulating,
> getting alpha details
> Alpha done simulating;
> getting alpha details
> Alpha done simulating,
> getting alpha details
> Output is truncated:
> View as a Scrglleele elemeytoropen in a et ecr Adjust celloutput Settngs:
 可以通过直接count output里的语句得到simulation的数量。


> [!NOTE] [图片 OCR 识别内容]
> #
> Run
> the simulations using
> a
> ThreadPoolExecutor
> With concurrent .futures . ThreadPoolExecutorCmax_workers=8)
> as
> executor:
> #
> each simulation data
> to
> the simulation
> function
> futures
> {executor . submit(run_simulation ,
> data) :
> data for data
> in simulation_data_list}
> #
> As
> each simulation
> completes ,
> you
> Can
> handle
> the
> results
> here
> for
> future
> i
> concurrent .futures
> as_completed(futures):
> alpha_details
> future .result()
> #
> Process
> the alpha_details
> as
> needed
> #
> This
> is just
> a
> template
> to
> you started,
> You Will need
> to
> handle exceptions
> and
> errors
> accordingly 
> Map
> get


使用多线程来模拟，可以调整线程数量。


> [!NOTE] [图片 OCR 识别内容]
> } result3json >
> 1
> [{"id":
> ITXZAPnZ"
> Itype"
> IREGULAR"
> nauthor"
> IYW54232"
> Settings":
> {"instrumentType"
> "EQUITY"
> "region" :
> IUSA"
> universe
> "T0P3000
> delay"
> 1,
> "decay":
> 4
> Ineutralization" :
> ISUBINDUSTRY"
> "truncation": 0.1,
> "pasteurization" :
> ION"
> "unitHandling" :
> IVERIFY"
> "nanHandling" :
> IOFFI
> "language"
> "FASTEXPR"
> "Visualization" :
> false}
> "regular":
> {"code":  "signal=ts_backfill(group_rank(ts_rankC (anll4_mean_ebitda_fpz-
> close ), 60) , industry) , 20);
> returns>0 . 09
> ?
> signal:
> 一1"
> "description" :
> null ,
> "operatorCount":
> 6} ,
> Idatecreated" :
> 42023-11-23112:51:16-05:00"
> IdateSubmitted" :
> null ,
> IdateModified" :
> 42023-11-23712:51:17-05:00"
> Iname":
> null ,
> "favorite": false,
> "hidden"
> false
> ICOLor"
> null ,
> "category"
> null,
> "tags"
> []
> "grade"
> null,
> "stage"
> IIS"
> Istatus"
> IUNSUBMITTED"
> "is":
> {"pnl": 3950742,
> "booksize"
> 20000000
> "longCount":
> 1089 ,
> IshortCount"
> 1084,
> Iturnover"
> 0.2269 ,
> Ireturns":
> 0.0402,
> "drawdown" :
> 0.0508
> "margin":
> 0.000354
> "fitness": 0.5,
> "sharpe"
> 1.19
> "checks":
> [{"name" :
> ILOW_
> SHARPE"
> Iresult":
> IFAIL"
> "lii":
> 1.58
> IValue":
> 1.19}
> {"name"
> "LOW_FITNESS"
> Iresult" :
> IFAIL"
> "limi":
> 1.0
> IValue":
> 0.53
> {"name":
> "LOW_TURNOVER"
> Iresult" :
> IPASSI
> Ilini":
> 0.01
> "Value"
> 0.2269} ,
> {"name"
> "HIGH_TURNOVER"
> "result":
> "PASS"
> "limi":
> 0.1,
> "Value":
> 0.2269}
> {"name
> 11
> "CONCENTRATED_WEIGHT"
> "result":
> "PASS" },
> {"name
> "LOW_SUB_UNIVERSE_SHARPE"
> "result":
> IFAIL"
> "lii":
> 0.52,
> "Value":
> 0.33}
> {"name"
> IUNITS"
> uresult":
> IWARNING"
> "message"
> Incompatible
> unit
> for input
> at
> index
> 1,
> expected | "Unit[J| "
> found
> "Unit[csprice:1J | ""} ,
> {"name":
> ISELF_CORRELATION"
> Ipesult" :
> "PENDING" } ,
> {"name":
> "PROD_CORRELATION"
> IPesult" :
> "PENDING" } ,
> {"name":
> "REGULAR_SUBMISSION"
> "result":
> "PENDING" } ,
> {"name":
> "MATCHES_THEMES"
> Iresult" :
> IWARNINGI
> "matched":
> []
> "unmatched"
> [{"id"
> "XDg8qBw"
> Iname":
> "EUR Delayl"
> "multiplier":
> 5.0}]}
> {"nam
> ITc
> A Tnrn
> C1IAnnr
> 1 [T
> L94?
> 八
> 1。!
> JIr
> I9499
> 八
> 171
> "limit" :
> 1.58
> Ivalue":
> 0.913]3,
> IOs" :
> null
> 'prod":
> null ,
> "compet
> Tokenization is skipped for long lines for performance reasons: This can be configured via
> editor.maxTokenizationlinelength
> settings":
> {"instrumentType"
> "EQUITYI
> "region"=
> "USA"
> "universe":
> "T0P3000"
> "delay"
> 1,
> "decay"
> 4,
> Ineutralization":
> "SUBINDUSTRY"
> truncation":
> .1,
> "pasteurization"
> ION"
> "unitHandling":
> IVERIFYI
> "nanHandling"
> IOFFI
> "language":
> IFASTEXPRI
> "visualization" :
> false}
> "regular":
> {"code":
> "signalsts_backfillCgroup_rank(ts_rank( Canll4_mean_ebitda_fp3-
> close ), 60) , industry ) , 20);
> Peturns〉0. 09
> ?
> Signal:
> 一1"
> "description":
> null,
> "operatorCount" :
> 63
> "datecreated":
> 12023-11-23712:51:17-05:00"
> Idatesubmitted" :
> null ,
> "dateModified" :
> "2023-11-23712:51:18-05:00"
> "name":
> null
> Ifavorite"
> false,
> "hidden":
> false
> IColor":
> null,
> "category"
> null ,
> "tags":
> [] ,
> "grade":
> null ,
> "stage":
> IISI
> Istatus"
> IUNSUBMITTED"
> Iis":
> {"pnl":
> 5279881,
> "booksize"
> 20000000
> "longCount":
> 1054
> "shortCount":
> 1048
> Iturnover"
> 0.2313
> ureturns"
> 0.0537
> "drawdown" :
> 0.0495
> margin"
> 0.000464
> "fitness":
> 0.76
> "sharpe"
> 1.57,
> Ichecks"
> [{"name":
> ILOW_SHARPE"
> Iresult" :
> IFAIL"
> "lii":
> 1.58
> IValue"
> 1.57},
> {"name
> 1
> ILOW_FITNESS"
> Iresult"
> IFAIL"
> "limit" :
> 1.0
> "Value":
> 0.763
> {"name"
> "LOW_TURNOVER"
> uresult":
> IPASS"
> "limi":
> 0.01,
> "Value"
> 0
> 2313},
> {"name"
> "HIGH_TURNOVER"
> Iresult"
> IPASSI
> "limit":
> 0
> 1,
> "Value":
> 0.2313}
> {"name"
> ICONCENTRATED_WEIGHTI
> Iresult"
> "PASS" },
> {"name"
> "LOW_SUB_UNIVERSE_SHARPE"
> Ipesult" :
> IFAILI
> "limi":
> 0.68
> IValue"
> 0.5} ,
> {"name":
> IUNITSI
> "result":
> IWARNINGI
> "message"
> Incompatible
> unit
> for input
> at
> index
> 1, expected | "Unit[J|"
> found
> |"Unit [csprice:1J |""},
> {"name"
> "SELF_CORRELATION"
> Iresult" :
> "PENDING" } ,
> {"name"
> "PROD_CORRELATION"
> Ipesult":
> "PENDING"3 ,
> {"name":
> "REGULAR_SUBMISSION"
> uresult" :
> "PENDING"}
> {"name":
> IMATCHES_THEMES"
> Iresult"
> IWARNING"
> "matched": [],
> "unmatched":
> [{"id":
> "XD98qBw"
> Iname" :
> "EUR Delayl"
> "multiplier":
> 5.0}]},
> {"name":
> IIS_LADDER_SHARPE"
> Iresult":
> IFAILI
> "year":
> 2
> IstartDate"
> 42021-02-16"
> IendDate":
> 42019-02-17"
> lii":
> 1.58
> "Value":
> 0.81313 ,
> IO5":
> null
> 'prod" :
> null
> Competitions"
> null
> Ithemes":
> null
> Iteam"
> null}
> {"id" :
> IAnGWXTXI


能够保存模拟结果较优的alpha到json文件，进行进一步的研究和提交。

想法：

在之前的测试中，用8线程模拟2500个因子后，网络会有中断的风险，所以用2小时模拟2500因子作为一个批次是我现在的选择。

之前已经参加过线下见面会，回去之后进行了自我探索，所以可见已经进行了10k+的因子模拟，甚至于把整个datafields都跑了一遍。之前的模拟中发现了一些不能用原有模板解释，但是依然有较好效力，甚至corr并不高的因子，可以作为未来研究和进一步探索的基础。但同时也要意识到仅仅通过“遍历”去搜索因子的效率并不高，目前也只有5个左右达到提交要求并corr不高的因子。模板的选择，因子库的构建和批量回测是可以并行进行的事情。而Generation Algorithm更多是提供一个新的视角或者帮助你找到隐藏的关系，而不能指望其中的独创性。

---

### 评论 #20 (作者: WL13229, 时间: 2年前)

@ [YT14523](/hc/en-us/profiles/17370777323031-YT14523)

这个报错似乎还是session被退出的问题。尝试handle并重连，应该可以解决问题

---

### 评论 #21 (作者: WL13229, 时间: 2年前)

[YW54232](/hc/en-us/profiles/13837011976855-YW54232)

网络中断可以进行重连，我们会在下次课介绍一个可行的办法。

关于您对Alpha的思考，是正确的。这正是我们作为Human需要不断给代码赋能的地方。寻找到合适的template，是human research很重要的一部分。

---

### 评论 #22 (作者: HW97336, 时间: 2年前)

**任务提交**


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 48
> GOOD
> RCELLENT
> Total Unsubmitted Alphas
> 4,159
> Total Active Alphas
> 32
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 4,191
> 16:45
> 1009
> -5OC 局部晴朗
> @1 C
> 幻
> @ dx 英  豳
> 2023/12/18



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 囝
> 8
> GOOD
> BCELLENT
> Total Unsubmitted Alphas
> 5,359
> Total Active Alphas
> 32
> SFECTACULR
> Total Decommissioned Alphas
> Total Alphas
> 5,391
> 19:31
> 100%
> 历史最低气温
> @ & 幻 《小英  l
> 2023/12/18



> [!NOTE] [图片 OCR 识别内容]
> II
> [29]:
> temp_ate
> type
> REGULAR'
> settings
> instrumentIype
> EQUIII'
> regIOI
> USA'
> lniTerse
> 10P3000'
> delay'
> decay'
> 20
> neutralization
> 101E'
> truncation'
> 0.1,
> pastelrization
> OM'
> lnitHandling
> VERIFI'
> nanlandl
> OFE
> language
> FASIEIPR'
> Vislalization
> False;
> StaIt
> time
> a11_alpla_
> id_list, all_alpha_list, all_DC_List, a11
> Summary_dT
> Simllate_
> alphas (s, template; datarields_Iist_adj-: 1200],10)
> end
> Cime
> print
> In'
> Drint
> 总用时: {}
> h {}
> Iin
> {}
> Tormat (int ( (end-start)
> 3600) , int
> (end-Start ) %3600/
> 60) , round
> (end-start ) %3600%60,2) ) )
> SLeeping Tor 2.5 seconds
> Alpha
> done
> Simil
> ating;
> getting alpha details
> Alpha retriered
> SLeeping Tor 2.5
> seconds
> SLeeping Tor
> 5 Seconds
> Sleeping Tor
> Seconds
> Alpha
> done
> Simil
> ating;
> getting alpha details
> AIpha retrieved
> Alpha
> doIe
> Imlllating;
> getting alpha details
> Alpha retriered
> Alpha
> doIe  simllating;
> getting alpha details
> llpha Ietriered
> Alpha done simllating;
> getting alpha details
> Alpha retriered
> Alpha
> done
> Simulatins;
> getting alpha details
> AIpha retrieved
> 总用时:2 h 30 nin 59.28
> ing



> [!NOTE] [图片 OCR 识别内容]
> II
> [30]
> al1_suimmary_df
> Out [30]
> shapre
> fitness
> turnoVer
> returns
> drawdown
> margin
> mqd51WG
> -0.06
> -0.01
> 10.22%
> -0.1196
> 8.319
> 0.219600
> XeVNWqq
> 0.02
> -0.0
> 10.22%
> 0.049
> 7.769
> 0.079600
> Anecmja
> -0.07
> -0.01
> 11.099
> 0.169
> 8.689
> -0.299600
> VXZCSgG
> -0.13
> -0.02
> 10.239
> 0.369
> 5.849
> -0.709600
> JnoGIEW
> -0.62
> -0.23
> 11.189
> 1.769
> 16.809
> 3.159600
> OAXRIak
> 0.38
> 12.199
> 0.869
> 3.809
> 1.409600
> 2v9032w
> 0.79
> 0.3
> 12.199
> 1.799
> 3.429
> 2.949600
> LnEgomg
> 0.71
> 0.25
> 12.219
> 1.619
> 4.069
> 2.639600
> knvVzg6
> 0.34
> 0.08
> 12.959
> 0.729
> 5.409
> 1.119600
> QnO3wWQ
> 0.78
> 0.27
> 13.059
> 1.599
> 5.459
> 2.439600
> 1200 rows
> 6 columns


**主要函数：**

实现对simulation_data_list里的所有simulation_data同时simulate，得到alpha_id_list和alpha_list


> [!NOTE] [图片 OCR 识别内容]
> In
> [16]
> def simulate_
> I_alpha (session; Simulation_data_Iist )
> UI___ist
> ];alpha_id__ist
> - ;aIplla_Iist
> 讧 len
> Imllation_data_Iist) >10:
> raise Exception
> Te
> Can Iot simulate more than ten alphas
> at
> the
> Same time
> for
> i range (len (simlation_data_Iist) ) :
> imlilation_reSDOISE
> SESSIOI. DOST
> https: //api
> VOIIdquantbrain. Com/ simulations
> json=simulation_data_list [i-)
> i
> Location
> 皿
> Mlllation_resDOIISC. headers
> Simli_atiol_DIOgCESS_
> UI1
> simulation_response. headers [
> Location ]
> UrI_List. append
> imulation_progress_url)
> else
> print
> 运行失败的表达式:
> simulation_data_Iist[iJ-' regular' ])
> Continue
> Jinished
> False
> for Url
> 皿 UrI_Iist:
> While True:
> Imli_atiol_DIOSLeSS
> SCSSIOI.
> (ur1)
> 讧
> imlilation_DIOSLeSS. headers.
> 'Retry-After
> 01
> 二二
> 0:
> break
> print
> Sleeping for
> Simulatiol_Drogress. headers -" Retry-After
> Seconds
> sleep (float (simulation_Drogress. headers
> 'Retry-After" ]) )
> Drint
> AIpha done simulating;
> getting alpha details
> alpla_id
> ;Imlilation
> DLogLeSS.json
> ~" alpha
> alpla
> SCSSIOI.
> get
> "https:
> api. IOrIdquantbrain. com/alphas
> alpha_id)
> Drint
> Alpha retrieved
> alpha_id_Iist. append (alpha_id)
> alpha_Iist. append (alpha
> return alpha_id_Iist, alpla__ist
> get
> get


获取performance comparison和summary信息，解决登出问题


> [!NOTE] [图片 OCR 识别内容]
> In
> [17]:
> def getAlphaInfo
> S, Simllation_data_Iist )
> DC_List
> slmmary_dt
> pd. DataFrame
> COlums=- shapre
> fitness'
> tuInoTer
> LetlrIs
> drawdomn'
> margin' ])
> aIpla
> 10
> List, alpha_list
> Sinlilate
> I_alpha (S, simulation_data_Iist )
> for
> 皿 range (len (alpha_id_Iist) )
> alpla_id
> alpha_id_Iist _i] ;alpha
> alpha_List -i]
> DC
> Derformance_comparisol (s, alpha_id)
> DC_Iist. append (Dc)
> al1Info
> alpha.json () - is' 1
> IerInfo
> dict (list (allInTo. items () ) -4:10])
> df
> InfoSummary (alpha_
> id, KeyInfo)
> stimmary_df
> Dd. COICat
> SUImmaIJ_dr
> dI],
> a715=0)
> return alpla_id_Iist, alpha__ist, PC_List, Summary_dr
> def getAlphaList
> S, Simllation_data_Iist )
> alpla_id_Iist, alpha__ist, PC_List, Summary_dr
> getAlphaInfo (s,
> ImlllatioI_data_list )
> except
> while True
> sign_in 0)
> 讧 IeSDOIISE.
> Cict
> -' status_code
> =201
> break
> alpha_id_list, alpha_List, DC_List, Summary_dT
> getAlphaInfo (s, similation_data_Iist )
> return alpla_id_Iist, alpha__ist, PC_List, Summary_dr
> key
> try


最终的函数，将所有datafield套入表达式，按照10个一组simulate，得到all_alpha_id_list、all_alpha_list、all_pc_list、all_summary_df


> [!NOTE] [图片 OCR 识别内容]
> In
> [18]:
> def
> iulate
> n_alphas (s, template, datafields_Iist, n) :
> alI_alplla_id_List
> 1;a11_alpha_Iist
> -;a11_DC_List=--
> a11_slmmary_df
> pd. DataFrame
> COIums=- shapre
> fitness
> tlrnover'
> retlrIs'
> drawdomr
> margin' ])
> epochs
> len (datarields_Iist ) / /n
> Lenains
> len (datarields__ist ) %I
> for epoch 皿 range (epochs)
> print
> In'
> print
> epoch:
> epoch)
> print
> In'
> simlation_data_list
> J
> for
> 皿 range (I)
> eTDIeSSIOII
> 1"ehat=ts_regression (returns, {datarields_Iist _nxepochtjJ} , 120)
> SrOUP_ZSCOIe (tS_ZSCOIe (-ehat, 60) , subindustry)
> simlllation_data_adj
> *template,
> 米
> {'regular'
> exDIeSSIOI}
> Simllation_data_Iist. append (sim_ation_data_adj)
> alpla_id_Iist, alpha__ist, PC_List, Summary_dr
> getAlphaList (s, simlation_data_list )
> alI_alpla_id_Iist
> +二
> alpha_id_Iist
> all_alpha_ist
> 十二
> alpha_Iist
> alI_DC_Iist
> +二 DC_List
> a11_stmmary_dI
> pd. concat ( [all_summary_d-, slimmary_df],
> azis=0)
> simllation_data_list
> []
> for
> 1 in range(remains)
> CDIeSSIOI
> 5" ehat=ts_regression (retlrns; {datarields_Iist _nxepochtjJ} , 120)
> group_Zscore (tS_Zscore (-ehat, 60) , subindustry)
> simlllation_data_adj
> *Template, * {'regllar
> ETDIeSSIOI}
> simlation_data_Iist. append
> simllatiol_data_adj)
> alpla_id_1ist, alpla__ist, DC__ist, summary_dr
> getAlphaList (s,
> ;Imlllation_data_list)
> alI_alpla_id_Iist
> +二
> alpha_id_Iist
> all_alpha_Iist
> +二
> alpha_Iist
> alI_pC_Iist
> 十二
> DC_Iist
> all_summary_df
> pd. concat ( [a21
> Slimmary_d-, slimmary_dI],
> azis=0)
> return all_alpha_Id_Iist, all_alpha_List, all_DC_List, a11
> Slmmar_dr


**代码效率**

Simulate 1200个Alpha，其中每次都是同时simulate 10 个Alpha，总用时2小时31分钟，不过我将获取performance comparison和summary的数据也写在了函数中，所以使得实际运行时间偏大。如果只simulate，不实时记录数据，而是在全部simulate结束后，从列表获取这些Alpha，再依次统计数据，可能用时会更短。

**debug经历**

- 登录失败：后来发现是因为自己之前用谷歌浏览器挂了VPN，关掉就好了。
- simulation_response.headers['Location']报错：应该是如果表达式出现问题，post后simulation_response.headers里没有’Location’这一指标，因此加入if else条件语句，如果’Location’在simulation_response.headers中，就正常运行代码，如果不在就跳过该表达式，这样就可以避免个别表达式错误导致代码中断。
- 在循环中直接采用simulation_data[’regular’]=new_expression的方式生成新的simulation_data，然后走正常流程，把得到的alpha_id添加进列表，结果发现运行完后list里全是最后一个Alpha，这个问题困扰了我很久，分步print都觉得没问题，后来采用另设一个变量，不直接替换原来的，问题得到解决。
- 解决登出问题：使用try except语句，把要实际运行的代码封装成函数，try这个函数，如果登出了必然会报错，那么运行except，重新sign in()直至response为201，然后再运行上述函数，保证代码不中断。

**模板选择**

模板为：

f"ehat=ts_regression(returns,{datafields_list[n*epoch+j]},120);group_zscore(ts_zscore(-ehat,60),subindustry)"

其中datafields_list[n*epoch+j]就是我们要填入的数据，自己提前在datafields_list中存储了1200种数据，n=10表示10个Alpha为一组，epoch则表示已经simulate多少组，j是每组中的索引

数据类型使用了News、Sentment以及Social Media的数据，通过搜索先得到category，再得到数据集的id，对于Vector都采用vec_sum的方式处理，Matrix则不处理

因为之前对新闻动量有过思考，这次想要在所有相关数据上都试一试，模板主要的意思是计算当前returns的偏离，将这个偏差在时间维度上zscore，然后再在行业维度上zscore，可以得到一个信息比较丰富的指标，根据它来决定多空仓位大小

在结果中看到的确有1个能提交的Alpha，但表现只能说刚刚及格，而且提交后会较低我的performance


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> Pnl
> 8,00OK
> 7,00OK
> 6,0OOK
> 5,0OOK
> 4,0OOK
> 3,00OK
> 2,00OK
> 1,00OK
> Jan '12
> Jan '13
> Jan "14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21



> [!NOTE] [图片 OCR 识别内容]
> 7PASS
> Sharpe of 2.06 is above cutoff of 1.58.
> Fitness Of 1.02is above CUtOff of 1.
> Turnover of 38.979 is above cutoff of 1%
> Turnover of 38.979 is below cUtOff of 709.
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 1.53 is above CUtOff Of 0.89.
> IS ladder Sharpe of 1.95 is above cUtoff of 1.74 for ladderyear 9: 2/16/2021 
> .2/17/2012


模板的改进方向：直接采用decay=20的方式虽然大幅降低了换手率，但会让其他指标也变差许多，以及对于这种反转策略如果用ts_mean这样的手段很容易降低表现，未来的改进方向可能有：1、加入合适的“进入条件”，这对于降低换手率应该是最重要的；2、可以对多个变量回归；3、将该变量与其他变量正交化，剔除其他变量的影响；4、对数据本身处理，比如可以替换为变化率等等；5、和其他alpha结合，强化表现

---

### 评论 #23 (作者: WL13229, 时间: 2年前)

[HW97336](/hc/en-us/profiles/18134895192087-HW97336)

一个非常完善的流程。同样的，这个是一个比较容易泛化的Alpha。它考量了A和B的残差。其实，returns也是可以换的。换掉returns后，在同个数据集进行操作，也会获得有趣的信息。

---

### 评论 #24 (作者: ZL89083, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 2,280
> Show
> 10
> Out
> Unsubmitted:
> 2,264
> ActiVe:
> 16
> List grov
> Decommissioned:
> Select Columns
> tUs
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> SearCn
> SeeC
> SeeC
> SeeC
> SearCn
> SeeC
> SeeC
> C g
> eE>1
> eE>1
> SeeC
> anonymOUs
> Regular
> ACTIVE
> 10/30/2023 EDT
> USA
> TOPSO0
> 2.00
> 77.929
> 6.069
> anonymOUs
> Regular
> ACTIVE
> 10/30/2023 EDT
> USA
> TOPSOO
> 2.00
> 77.929
> 6.069
> 23:59
> 云
> 搜索
>  ^ W
> 产 Iul
> 谷 qx O
> 2023/12/17
> Hlter



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 3,289
> Show
> 10
> Out
> Filter
> Unsubmitted:
> 3,273
> Active:
> 16
> Select Columns
> tUS
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> Fec
> SearCn
> SeleC
> SeleC
> e.B>1
> e.B>1
> e.B>1
> SeleC
> aNOITYIOUS
> ReaI
> JNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 1.87
> 8.20%
> 4.0796
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 1.93
> 8.26%
> 3.9796
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 1.54
> 13.00%
> 10.54%
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 2.00
> 8.75%
> 4.009
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 1.99
> 9.80%
> 3.98%
> anonyMOUS
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 1.50
> 13.939
> 10.1596
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 0.20
> 1.169
> 1.2496
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 0.81
> 4.489
> 90%
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> -1.43
> 6.609
> 2.169
> anonymOUs
> Regular
> UNSUBMITTED
> 12/17/2023 EST
> CHN
> TOP3000
> 0.27
> 1.329
> 1.5996
> 
> 10:17
> 
> 搜索
> W
> N IMl 谷 qx 囟
> 2023/12/18


我用tqdm库显示回测进度


> [!NOTE] [图片 OCR 识别内容]
> SLgeR(5)
> else:
> print("Simu
> YoU
> Can
> status
> 
> 2
> 100%
> 1089/1089


我没有遇到太多bug,由于最近考试多，我就测试了一个比较简单，回测快的表达式：rank(ts_mean(alpha,20)),

然后数据选取的话，主要还是选取能与表达式结合表达一定因子逻辑的数据集，我主要选取了几个fundamental的数据集，有几个因子表现还不错，但我没有截图。

我是将alpha表现的json表达式提取出来放到一个df里面 
> [!NOTE] [图片 OCR 识别内容]
> regular_code
> ftness
> returns
> i
> OAx8OVk
> rank(ts_mean(fnd72_s_pit_or_bs_q_statutory_cap。.
> 12.60
> 0.6419
> 1007026
> rank(ts_mean(fnd72_s_pit
> bs_q_statutory_cap。
> 1259
> 0.6413
> xeVnaOJ
> rank(ts_mean(fnd72_s_pit_or_bs_a2_statutory_ca..
> 3.05
> 0.2862
> VSZmWGW
> rank(ts_mean(fnd72_s_pit
> Or_is_q_is_other_oper.
> 1.48
> 0.1662
> YNBQOYM
> rank(ts_mean(mdl175_cibb,20)]
> 1.58
> 0.1393
> EqNgYWr
> rankfts_mean(mdl175_Gdca
> -4.30
> 0.2515
> mqdxnLX
> rank(ts_mean(mdl25_bs_71v,20))
> -1.51
> 0.2574
> Nnlgkzl
> rank(ts_mean(mdl175_Gdtsvt 20))
> -7.00
> 0.3167
> JnoSaoj
> rank(ts_mean(mdl25_cb_02v,20))
> -2.38
> -0.5024
> YNBAGGW
> rank(ts_mean(fnd72_s_pit_or_bs_
> bs_plant_cons
> -1.0294
> 20))
> -8.74


---

### 评论 #25 (作者: FP65798, 时间: 2年前)

一.simulation增加情况
 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Alphas
> Seealll
> Achievements
> VewAchlevements
> Status
> Status
> 20
> 旧0
> GOOD
> Total Unsubmitted Alphas
> 440,656
> Total Unsubmitted Alphas
> 446,488
> Total ActiVe Alphas
> 153
> Total Active Alphas
> 155
> OcLLUUIT
> LTIIg
> Total Decommissioned Alphas
> Total Decommissioned Alphas
> Total Alphas
> 440,809
> Total Alphas
> 446,643
> 18:08
> [4j 英  u
> 2023/12/18
> 昌
> 13:19
> 思4j 英  豳
> 2023/12/15
 
二.code运行情况(连续不停1000个simulation)
 
> [!NOTE] [图片 OCR 识别内容]
> ETJR IILIQUJID_MINVOLIM
> CHN TOP3000
> length 0t
> aIpha
> 1051
> t[]
> print ( length of
> alpha list: Si' %len(alpha_list))
> 100
> 50/50  [15:16<00:00,
> 18.348/it]
> for
> in Lange (t)
> Tine used:
> 0.26 hours
> a+8ap
> result. append (sijulate_alpha_list_ulti (s,
> alpha_list [a:b]))
> 100N
> 50/50 [14:42<00:00,
> 1?.665/it]
> length of
> alpha Iist: 1810
> Tine used:
> 0.25 hours
> 100
> 50/50 [1:03:50<00:00,
> 76.615/it]
> 100N
> 6/6 [03:10<00:00,
> 31.685/i]
> Tine used:
> 1.0? Hours
> Tine used:
> 05 hours
> 100N
> 50150 [48:05<00:00,
> 5?.728/i]
> 1er
> alpha Iist: 1267
> Tie used:
> 0.81
> IorS
> 100
> 50/50 [15:59<00;00,
> 19. 20s/it]
> Uun:
> 1
> HTT
> 100N
> 50150 [48:24<00:00,
> 58.098/i]
> 24/50 [09;3510;24
> 025/1t]
> oue
> Noe
> T5hhocoeed
> 341
> ou
> Comcc
> TTM1
> respore'))
> Tije used:
> 0.81
> hours
> I0C
> 50/50 [15:4300;0
> 13,85s/1+]
> 1004
> 31/31 [31:58<00:00,
> 61.898 /it]
> Usno:
> U
> hus
> 0/27 [02:31?,
> ?i1s]
> Tije used:
> 54 Iotrs
> SELUICI
> JSoted
> Renotebigcommected('Reote
> Closed Corection vitout
> Degole
> detiil
> SIUULATIOI_LILIT_ERCEEDED
> 100
> 27/27 [10;11(00;00,
> 655/1t]
> Tire used; 0.17 hors
> 1i5t:
> FeSUI
> 13ap
 
三.总结反思

1. 代码效率：
   根据之前的运行经验发现，每次提交500个simulation报错的几率比较小，因为一次跑得过多容易出现“connection aborted”的情况。目前我的策略是将要跑的数据按500个一份分组，若无报错，则跑完一份后立刻提交下一份；若中途报错，就获取错误信息显示出来，接着等30分钟（因为我发现程序这边报错平台那边似乎不会立刻刹车，马上重新提交的话会导致“simulation_limit_exceeded”，所以需要等待一段时间），再重新跑一下s = ace.start_session()，再重新提交这一份的500个数据从头跑。从上面第二部分code运行情况的截图来看，这样还是比较顺畅的，每个线程也是顶满10个simulation。在此方式以及模板（见下第3小节）下，对CHN TOP3000的1051个数据，无报错跑完的时间为33.6分钟。
2. debug经历：
   在跑下面这段代码想查看simulation返回的结果时，会遇到以下报错。原因是结果里有重复项。
   目前想到的办法是在result后面加[0:100]这样的区间避开重复项。不知有没更好的办法？
   
> [!NOTE] [图片 OCR 识别内容]
> Legult_stl
> hf. prettify_result (result_ijprove [0] [0:],
> detailed
> tests
> vielf『a1se〉
> t_st2-reslllt_stl [ ((result_stl [' fitness
> (result
> st1 [ fitness]
> 0.?) )
> (result
> stl [' concentrated_leiaht' ]=='PsS8'
> Tesul
> 5t2[0:10]
> Rile
> lanaconda3lLiblsite-packages Ipandas
> core lreshape lreshape.Dy:189,
> i
> Instacler._nale_selectors (self)
> 186 Jasl. put (selector,
> True)
> 188 i Jask
> SU()
> len (self. inde}
> 189
> raise
> TaLUePrIOI
> Inder
> contains
> duplicate entries,
> Calot reshape
> 191
> Se11
> SrOUp
> indes
> COIIP
> indet
> 192 self. Jask
> Tasl
> TalueError
> Indey
> contains duplicate
> entries,
> cannot Teshane
> Tegul

3. 模板适合的数据类型：
   参考模板为 [【Alpha灵感】通过期权隐含价格与股票市场价格的差异寻找投资机会]([L2] 【Alpha灵感】通过期权隐含价格与股票市场价格的差异寻找投资机会_19140570265367.md)
   ```
   ts_backfill(group_rank(ts_rank({x}-close, 60), industry), 20)
   ```
   适合的数据类型: 价格数据（期权隐含股价，加权股价，机器学习预测股价等）
   直接通过search price获得数据
   ```
   datafields_df=hf.get_datafields(s, region='EUR', universe='ILLIQUID_MINVOL1M', delay=1, search='price')
   ```
4. 模板的改进方向：
   此模板在CHN TOP3000看起来有以下不错的表现
   
> [!NOTE] [图片 OCR 识别内容]
> pII
> book_size
> Iong
> CoUnt
> Short_Count
> tUrnOVe
> retUrns
> Crawcown
> margin
> fitness
> sharpe
> is_laddler_sharpe
> IOW_T1eS5
> Iow_
> retUrns
> IOW
> 94486151
> 20000000
> 992
> 993
> 0.7113
> 0.9929
> 0.0915
> 0.002792
> 12.83
> 10.86
> FAIL
> PS5
> PS5
> 40607046
> 20000000
> 958
> 965
> 0.4126
> 0.4257
> 0.3359
> 0.002063
> 7.26
> 7.11
> FAIL
> PASS
> PASS
> 39192771
> 20000000
> 822
> 828
> 0.4117
> 0.4119
> 0.3737
> 0.002001
> 7.00
> FAIL
> PASS
> PASS
> 39170999
> 20000000
> 321
> 830
> 0.4138
> 04116
> 0.3762
> 0.001990
> FAIL
> PASS
> PASS
> 38794916
> 20000000
> 851
> 853
> 0.4111
> 0.4077
> 0.3565
> 0.001984
> FAIL
> PASS
> PASS
> 38311379
> 20000000
> 852
> 855
> 0.4112
> 4026
> 3634
> 0.001953
> FAIL
> PASS
> PASS
> 50404313
> 20000000
> 1220
> 1215
> 0.4745
> 0.5297
> 0.3122
> 0.002233
> 6.75
> FAIL
> PS5
> PS5
> 38368734
> 20000000
> 995
> 1000
> 0.4102
> 0.4032
> 3559
> 0.001965
> 6.72
> FAIL
> PS5
> PS5
> 40474524
> 20000000
> 576
> 710
> 0.3302
> 0.4253
> 0.2120
> 0.002237
> 5.95
> FAIL
> PS5
> PS5
> 32687353
> 20000000
> 998
> 989
> 0.3040
> 0.3435
> 0.3651
> 0.002250
> 5.87
> 5.52
> FAIL
> PASS
> PS5
> 46167015
> 20000000
> 1216
> 1218
> 0.4780
> 0.4852
> 0.9580
> 0.002030
> 4.74
> 4.70
> FAIL
> PS5
> PS5
  
> [!NOTE] [图片 OCR 识别内容]
> Iow_fitness
> IOW_TeturIs
> Iow_robust_universe_
> Teturns
> low_robust_universe_sharpe
> IOW
> sharpe
> IOW
> sUb_universe_sharpe
> IO_tUTTOVeT
> matches_
> theles
> PASS
> PASS
> P45S
> PASS
> PASS
> PASS
> P45S
> WRNING
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IWAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IWAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IWAR
> PASS
> PASS
> P455
> PASS
> PASS
> P4SS
> P45S
> WRNING
> INAR
> PASS
> FASS
> P455
> PASS
> PASS
> PASS
> P455
> WRNING
> WAR
> PASS
> PASS
> P455
> PASS
> PASS
> P4SS
> P45S
> WARNING
> INAR
> FASS
> FASS
> P455
> PASS
> PASS
> PASS
> P455
> WRNING
> WAR
> PASS
> PASS
> P455
> PASS
> PASS
> P4SS
> P45S
> WRNING
> INAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IWAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IWAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IWAR
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> PASS
> WARNING
> IAR
> PASS
> PASS
> P455
> PASS
> PASS
> P45S
> P455
> WRNING
> WNAR
> PASS
> PASS
> P45S
> PASS
> PASS
> PASS
> P45S
> WRNING
> INAR
> PASS
> PASS
> P455
> PASS
> FAIL
> PASS
> P455
> WARNING
> WAR

   但由于IS ladder Sharpe Fail以及部分turnover比较高使得其无法通过。
   见下图IS ladder Sharpe Fail可能是因为18年后alpha失效了？暂不知有什么改进办法。 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> SNarC=
> LUCT
> ICIs
> eCUTI
> UTaWJUOITI
> Wareir
> 6.39
> 47.459
> 6.75
> 52.97%
> 31.2296
> 22.339600
> Sharpe
> Tumover
> Ftnoss
> Returns
> Drawdown
> Maryin
> LOng Count
> Short Count
> 711
> 1.58
> 51.3295
> 1.3
> -
> .3530
> 34755600
> SE
> 2712
> 1.75
> 52.523
> 13.5
> 31
> 1.1051
> 31.52Saoo
> 1934
> 1723
> 2713
> 1.29
> 52.173
> 12.5
> 7.32*
> 751
> 29.55
> 1152
> 271
> 5.211
> 11.51
> 72.50光
> 2.4550
> 75325
> 14
> 1151
> 2715
> 52.1193
> 1.21
> 1451
> 5.33
> 55
> 1125
> 1127
> 2315
> 1.5
> -3.313
> 14
> 4 1
> 1.3130
> 51.0253
> 125
> 1-7
> 2717
> 3.1
> 5.4595
> 3.32
> 53
> +51
> 2933
> 1311
> 11
> 2715
> 1.7
> 4.8595
> 7.25
> 5.2
> 53
> 533
> 375
> 1-7
> 2719
> 4.0295
> 42
> 1
> 5.0755
> 30753
> 1-25
> 14-1
> 2720
> 2.21
> 3.53
> 21.12
> 13.5455
> -11.51523
> 3
> 1371
> 2721
> 37.4295
> 5.37
> 32.52:
> 15
> F
> 325
> 127
> Vear
 Turnover比较高的改进思路：利用Trade_when设置合适的进场时机，具体是什么条件还需要研究；
   根据运行经验，选择合适的group_neutralize可以对alpha有比较大的提升（可能可以有效降低回撤），可以利用机器再跑下最优group_neutralize。
5. 代码改进方向
   改成断点续跑，而不是现在的报错则从每份数据组的开头重新跑。

---

### 评论 #26 (作者: WL13229, 时间: 2年前)

[ZL89083](/hc/en-us/profiles/13837026594199-ZL89083)

已经算是比较成型的作品了，虽不是最经验，但重在代码bug少

---

### 评论 #27 (作者: WL13229, 时间: 2年前)

[FP65798](/hc/en-us/profiles/17259858019735-FP65798)

非常impressive的回测次数。关于您提到的“改成断点续跑，而不是现在的报错则从每份数据组的开头重新跑。”，这个也是我非常建议的方向。可以看出您已经有相对成熟的框架，我建议将ACE代码重写，这样您可以更加清晰地进行debug，包括show result的部分。

---

### 评论 #28 (作者: WX16829, 时间: 2年前)

**作业提交**

1.程序运行前后截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> SEE
> Alphas
> See
> Stalus
> Stalus
> TJta
> Unsubmitted Jlphas
> 141,505
> TJta
> Unsubmitted Jlphas
> 142,622
> Total Active AIDTEs
> 269
> Total Active AIDTEs
> 269
> Totar
> DecommissonEd 4Iphas
> Tota
> DecommissoREd 4ph3s
> Total Jlohas
> 141,794
> Total 4l3Tas
> 142,911
> 21;22
> 22:40
> Out
> fle_I [
> 提交前截图
> 2023/12/17
> 2023/12/17
> 运行前
> 运衍后


2.本次通过程序一共运行提交了1137个因子。研究发现每个因子运行完成后json中Date Modified字段可显示因子的运行时间。运行完成后，将此字段及主要的结果输出至CSV文件保存，运行用时一共约1小时15分钟。


> [!NOTE] [图片 OCR 识别内容]
> EuPre33
> Date
> Jodified
> inlstruner regior
> UlliTEISC
> baclfill (rarll (ts
> 工a1止
> EQ[II
> [Sg
> TOP3000
> baclfill (rarl
> 工a1止
> EQ[II
> [Sg
> TOP3000
> rarll (t3_
> 工a1止
> oth432
> 303
> 023-
> EQ[II -
> [Sg
> TOP3000
> 工a1ni (+3
> 工a1k (oth432
> Titt
> 2023
> 12-
> TT09
> EQIIIT
> [Sg
> TOP3000
> baclrf111 (工a1n (+3_
> 工a1止
> 2023-12-1909:39:29-05:00
> EQIIIT
> [Sg
> TOP3000
> 1135
> ra1l {t3_
> 工a1l {0t11432
> 2023-12-一
> F08:25:01
> 05:
> EQIJITI
> [9虫
> IOP3OO0
> 1136
> t3_baclfi11 {工a1l {t3_工a1l
> 2023-12-17108:25:01
> EQIJITI
> [9虫
> TOP30n0
> 1137
> ra1li {t3_
> 工a1l {0t11432
> aaCr
> 023
> TT%:2 
> EQIJITI
> [Sg
> TOP30n0
> 1738
> t3_baclfi11 {工a1l {t3_
> IaIL
> 2023-12-1908:25:01-05:00
> EQIJITI
> [S虫
> TOP300


3.总结反思：

（1）代码效率方面，主要使用了上节课提供的模板，先将因子全部提交至平台运行，完成后再获取结果。由于平台上并行线程的限制，当发现无法提交时等待一段时间重试，总体上效率比较高。


> [!NOTE] [图片 OCR 识别内容]
> True
> While
> try:
> print("simulation
> SUbMittel
> Ton:
> Simzation_Jata
> rEEUIar'
> simlation_FEsponse
> 'post( 'https:
> apilorldquantbrain.C2m;simulations 
> json-simu_ation_CETa)
> print(simulation_Fesponse.status_Code_
> simulation_progress_url
> SImILaTIOI_
> 二1052
> head?s
> LOcation
> flzs-False
> EXCEDT:
> if =iulation
> 厂5500152
> Satus
> 332!=-29
> Connection()
> SIEEp(1O)
> f?e=
> +_:R:


（2）Debug方面，主要考虑初步建立一个简单的dataset探索的框架程序，使用rank(ts_rank({datafield},20))作为模板对dataset other432进行探索，simulation过程中使用的函数主要都是上节课提供的函数。为了后续研究和改进的方便，将数据整理数据输出至csv文件，同时每个因子包含时间标签以方便检查是否为当前程序所测试的因子。

（3）改进方向：主要有两方面：一是程序的容错性和断点续跑需要完善。在测试过程中发现先一次提交全部因子再获取结果的方法有少量因子（1-2个）提交成功，但最后获取结果时发现丢失了。因无法在提交后第一时间获得因子的alpha id,完成后手工检查比较费力，后续考虑程序中能够自动检查和重跑。（2）调参的自动化程度需要提升。目前该模板仅能支持对一个简单因子模板（包含一个可变datafield）的探索，另外setting下的decay、neutralization等设置仍然需要手动调整，这些手动调参的重复性工作后续可以考虑通过程序实现。

---

### 评论 #29 (作者: YJ78324, 时间: 2年前)

一、本次任务前后的Alpha数量截图

本次任务在代码测试和运行后提交了约2000多个Alpha


> [!NOTE] [图片 OCR 识别内容]
> UUIUOII
> 赀'a
> Simulale
> Aphas
> Dala
> Competitions (1)
> Events
> 囚 Learn
> Refer
> friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 230
> Show
> Filter
> Unsubmited
> 222
> ActiVe:
> Select Columns
> Btus
> Date Created IEST
> Region
> Universe
> Returns
> Turnover
> Tag
> Decommissioned;
> pelect
> Seaich
> Selecr
> Selec[
> e.吕> 1
> e.巳>
> ATIUMIYTTOUS
> RegUldr
> ACTIUE
> 03/01/2023 EST
> USA
> TOPIOOO
> 000
> 0.00%
> 0,009
> anonymOUs
> Resular
> ACTIVE
> 03/01/2023 EST
> USA
> TOP3OOO
> 000
> 0 0Oq
> 0.009
> anonyIOUs
> ReEUIJT
> ACTIVE
> 02/28/2023 EST
> USA
> TOP3OOO
> 0O0
> OOOqu
> 0.009
> anonymous
> Regular
> ACTIUE
> 0227/2023 EST
> USA
> TOPSOO
> 0O0
> 0.0O9
> 0,009
> anoyIOUs
> Regular
> ACTIVE
> 02/25/2023 EST
> USA
> TOPSOO
> 0O0
> 0.OOgu
> 0.009
> 17.47
> 2023/12/15
> Sharbe
> eg >



> [!NOTE] [图片 OCR 识别内容]
> 鬯
> Simulate
> Alphas
> Data
> 巴 Competitions (1)
> Events
> Leamn
> Refer
> friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 2.740
> Show
> U Fllter
> Unsubmitted
> 2,732
> Actie:
> Select Columns
> atus
> Date Created (ESTI
> Region
> Unierse
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> LPlP
> Search
> Select
> Select
> 2.g1
> Eg1
> ee
> ATIUTIIITIUUL
> ROSUIIJT
> UNSUBMIITTED
> 12/18/2023 EST
> CHN
> TOP30O0
> 2,31
> 10,5455
> 5,0195
> anonymoUs
> ReBular
> UNSUIBLIITTFT
> 12/18/2023 EST
> CHN
> TOPJOOO
> 1.70
> -5.585
> 8.73%
> anonyIoUs
> Regular
> UNSUBMITTED
> 12/18/2023 EST
> CHN
> TOP3OO0
> 2.89
> 8.46%
> 6.839
> anonymoUs
> Regular
> UNSUBIIITLL
> 12/18/2023 EST
> CHN
> T093000
> 1,76
> ~5.255
> 795
> anonynOUs
> RegUIaT
> UINCIIRLIITTFT
> 12/18/2023 EST
> CHN
> TOPJDOO
> 2.73
> 7.87玷
> 7.074
> SIOIVITIUUIt
> Regular
> UNSUBMITTED
> 12/18/2023 EST
> CHN
> T0P3000
> ~1,52
> -5,5555
> 7,039
> 正任等待 apiworldquantbraincom
> 21.38
> 英
>  dj
> 2023/12/18


二、代码连续运行情况

代码针对给定数据集共生成了1252个Alpha，这1252个Alpha使用多线程在大约在1小时内提交完成


> [!NOTE] [图片 OCR 识别内容]
> Last
> Executed
> at
> 2023-12-18 21:23:24
> in
> 1h
> Gm  565
> Login Successful ! <Response [201]〉
> Get Data Fields: 100%
> 26/26 [00:07<00:00,3.32it/s]
> Total
> Fields:
> 1252
> Finish:
> OnRLGKE
> Finish:
> 2 WN3bzvz
> Finish:
> 3 knvoGpg
> Finish:
> dnYbzPy
> Finish:
> KnVoGYL
> Finish:
> 17EVGW8
> Finish:
> XkVbzZb
> Finish:
> RN9bzVZ
> Finish:
> aNebzgl
> Finish:
> 18 17EVGN2
> Finish:
> 11 jnoAXOE
> Finish:
> 12 ZVSWWdb
> Finish:
> 13 nnmdobx



> [!NOTE] [图片 OCR 识别内容]
> Last
> Executed
> 2023-12-18
> 21:23:24
> in Ih
> Gm 565
> Finish:
> 1236 NnLVKIp
> Finish:
> 1237 NnLVPdE
> Finish:
> 1238 nnmP61z
> Finish:
> 1239 RNgGeGe
> Finish:
> 1248 bNJOawz
> Finish:
> 1241 pnxSWm3
> Finish:
> 1242 xeVblGw
> Finish:
> 1243 Mbd3806
> Finish:
> 1244 BmXZrz]
> Finish:
> 1245 3EIVGBg
> Finish:
> 1246 GRZKGBY
> Finish:
> 1247 OnOKWar
> Finish:
> 1248
> EqNRmaG
> Finish:
> 1249 enNQIBN
> Finish:
> 1250 jnogVxs
> Finish:
> 1251 WN3eyNK
> Finish:
> 1252 Jnoo3nm
> Finish Count:
> 1252


三、总结反思

3.1 代码效率

我将整体的代码分解为三个功能模块，方便后续功能的扩展：（1）WorldQuantClient：用于处理网络请求，如：登录、提交Alpha、查询Alpha等功能；（2）AlphaExpressionGenerator：根据指定的模板与规则生成Alpha表达式，其中也包括了对于Vector类型数据的处理；（3）TaskManager：通过调用前两个模块完成任务的批量提交和结果的记录

批量提交方面为了提升代码的运行效率，我这里采用了ThreadPoolExecutor线程池对于生成的Alpha表达式进行并发提交，最大线程数为WorldQuant的最大模拟次数10。在提交任务后对于所有成功的Alpha集体做一次查询，并保存结果。

3.2 调试经历

整体开发过程中遇到最多的问题还是网络请求中出现 connection aborted。针对这一情况，我对网络请求做了进一步的封装，设置重试次数与间隔时间，每次请求失败后都会重新登陆，再次尝试网络请求。

3.3 Alpha回测

本次选择的测试模板如下：

`rank(group_neutralize(x - last_diff_value(x, 5), bucket(rank(cap), range="0.1, 1, 0.1")))`

根据基本面数据的差异，按照市值进行分组中性化并进行排名，测试范围为CHN TOP3000，用于生成表达式的Data Fields来自 A-shares Fundamental Data 数据集中的1252个字段。其中针对Vector数据都采用了vec_avg方法进行聚合。

整体测试结果如图：


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> alpha_exp
> pnl
> turnoVer
> returns
> drawdown margin
> fitness
> sharpe
> EqNVZRO
> rank(group
> 8242070
> 0.0614
> 0.0866
> 0.0779
> 0.00282
> 2.4
> OAXRBrK
> rank(group
> 9826872
> 0.0591
> 0.1033
> 0.1128
> 0.003496
> 2.1
> 2.39
> SLrQVZG
> rank(group
> 9955214
> 0.06
> 0.1046
> 0.1126
> 0.003487
> 2.18
> 2.38
> EqNGJEI
> rank(group
> 5234435
> 0.0369
> 0.055
> 0.1058
> 0.00298
> 1.07
> 1.61
> OnRGEXE
> rank(group
> 7180988
> 0.0564
> 0.0755
> 0.1789
> 0.002672
> 1.22
> 1.57
> qnOWLL2 rank(grour
> 7108077
> 0.0565
> 0.0747
> 0.1827
> 0.002644
> 1.2
> 1.55
> LnEGaW
> rank(group
> 5064681
> 0.036
> 0.0532
> 0.1241
> 0.002954
> 0.9
> 1.52
> NnLQA2g rank(grour
> 6247206
> 0.0503
> 0.0656
> 0.1986
> 0.002612
> 1.04
> 1.44
> 10
> pnxP7ob
> rank(group
> 6248263
> 0.0503
> 0.0657
> 0.1985
> 0.002613
> 04
> 1.44
> 11
> 998VRbI
> rank(group
> 4424700
> 0.0524
> 0.0465
> 0.1456
> 0.001776
> 84
> 1.37
> 12
> VSZkdGV
> rank(group
> 5164619
> 0.0367
> 0.0543
> 0.2126
> 0.002959
> 85
> 1.29
> 13 |5LrQv9]
> rank(group
> 5121927
> 0.0532
> 0.0538
> 0.1367
> 0.002023
> 85
> 1.29
> 14
> rbg5RpI
> rank(group
> 5342110
> 0.0365
> 0.0561
> 0.2096
> 0.00307
> 1.28
> 15
> Nnl7R3X
> rank(group
> 5365758
> 0.0365
> 0.0564
> 0.2258
> 0.003092
> 1.26
> 16
> 7x3ZE2L
> rank(group
> 3827417
> 0.0415
> 0.0402
> 0.138
> 0.001938
> 1.25
> 17
> AneOGXe
> rank(group
> 5001601
> 0.0363
> 0.0526
> 0.2124
> 0.002899
> 1.15
> 18
> OnRrMJV
> rank(group
> 5097963
> 0.0355
> 0.0536
> 0.2047
> 0.003021
> 75
> 1.14
> 19
> YN8SIXW rank(grour
> 4747586
> 0.0507
> 0.0499
> 0.2049
> 0.001967
> 1.13
> 20 |ZSgNGbI
> rank(group
> 4350507
> 0.0716
> 0.0457
> 0.157
> 0.001278
> 64
> 1.06


这里选择其中比较高Sharpe的Alpha表达式查看了结果


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
> Drawdown  Margin
> 2.406.1492.008.66%7.79028.209600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short C
> 2011
> 4.51
> 6.589
> 4.45
> 12.1996
> 1.2596
> 37.089600
> 972
> 2012
> 4.85
> 5.45%
> 4.94
> 12.959
> 1.3096
> 47.559600
> 1073
> 2013
> 3.81
> 6.16%
> 3.79
> 12.36%
> 1.2296
> 40.099600
> 1165
> 2014
> 1.49
> 5.559
> 0.91
> 4.6396
> 4.2496
> 16.679600
> 1180
> 2015
> 2.48
> 6.2496
> 2.54
> 13.16%
> 4.2596
> 42.219600
> 1163
> 2016
> 5.01
> 5.79%
> 5.12
> 13.06%
> 1.0096
> 45.069600
> 1298
> 2017
> 3.34
> 5.21%
> 2.91
> 9.52%
> 1.2396
> 36.549600
> 1394
> 2018
> 2.01
> 6.449
> 1.53
> 7.29%
> 2.4996
> 22.679600
> 1457
> 2019
> 2.73
> 6.839
> 2.23
> 8.33%
> 2.0396
> 24.429600
> 1474
> 2020
> -1.10
> 7.35%
> 0.69
> -4.90%
> 5.0396
> -13.339600
> 1451
> 2021
> -2.27
> 6.84%
> -2.85
> -19.76%
> 2.4496
> 57.789600
> 1418



> [!NOTE] [图片 OCR 识别内容]
> o
> IS Summary
> Period
> IS 
> Os
> Aggregate
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Data
> 2.395.9192.1710.339611.289634.969600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short
> 2011
> 3.69
> 6.92%
> 3.43
> 10.80%6
> 1.20%
> 31.209600
> 972
> 2012
> 4.84
> 5.40%
> 5.03
> 13.49%
> 1.1196
> 49.949600
> 1077
> 2013
> 4.63
> 6.10%
> 4.82
> 13.5696
> 1.269
> 44.5096oo
> 1167
> 2014
> 2.68
> 5.38%
> 2.42
> 10.1796
> 5.349
> 37.799600
> 1176
> 2015
> 4.43
> 6.33%
> 6.95
> 30.78%
> 6.3796
> 97.319600
> 1162
> 2016
> 5.44
> 5.43%
> 6.99
> 20.64%
> 2.0996
> 76.049600
> 1289
> 2017
> -0.13
> 5.06%
> 0.03
> -0.55%
> 3.619
> 2.189600
> 1390
> 2018
> .93
> 5.84%
> 1.62
> 8.7796
> 2.7496
> 30.039600
> 1445
> 2019
> 1.90
> 6.12%
> 1.33
> 6.1496
> 1.9096
> 20.089600
> 1463
> 2020
> -1.42
> 6.74%
> -0.98
> -5.99%6
> 5.629
> -17.789600
> 1443
> 2021
> 4.88
> 7.01%
> 9.69
> -49.3096
> 5.1696
> -140.719600
> 1389



> [!NOTE] [图片 OCR 识别内容]
> o
> IS Summary
> Period
> IS 
> Os
> Aggregate
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Data
> 2.386.00962.1810.46%11.26934.879600 -
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short
> 2011
> 3.93
> 7.19%
> 3.81
> 11.73%
> 1.2096
> 32.619600
> 975
> 2012
> 5.18
> 5.529
> 5.57
> 14.45%
> 1.1896
> 52.379600
> 1074
> 2013
> 4.60
> 6.249
> 4.88
> 14.049
> 1.2396
> 44.969600
> 1167
> 2014
> 2.28
> 5.45%
> 1.95
> 9.1796
> 6.0596
> 33.639600
> 1175
> 2015
> 4.27
> 6.389
> 6.68
> 30.6096
> 6.3296
> 95.889600
> 1163
> 2016
> 5.43
> 5.50%6
> 7.03
> 20.93%
> 1.9296
> 76.159600
> 1290
> 2017
> 0.20
> 5.149
> 0.05
> 0.889
> 4.2596
> -3.419600
> 1387
> 2018
> 1.90
> 6.019
> 1.60
> 8.85%
> 2.7996
> 29.449600
> 1441
> 2019
> 2.00
> 6.30%
> 1.43
> 6.3796
> 1.6996
> 20.219600
> 1462
> 2020
> -1.60
> 6.66%
> -1.13
> 6.2490
> 6.0096
> -18.749600
> 1436
> 2021
> -4.53
> 5.74%
> -8.70
> -46.12%
> 4.8496
> -160.769600
> 1393
 可以看到，这几个Alpha在2020年后都出现了失效的情况，具体原因与优化方向还需要进一步分析。

3.4 改进方向

- 代码方面实现配置化，讲一些可变的参数放入YAML文件中，进一步提升自动化效率；
- 添加结果分析模块，可以针对pnl信息做进一步分析处理；
- 参考论坛中的他人经验，尝试构建Alpha模板库

---

### 评论 #30 (作者: WL13229, 时间: 2年前)

@ [WX16829](/hc/en-us/profiles/8702256081943-WX16829)

代码效率挺好的，这也是推荐的做法。至于您遇到的问题“在测试过程中发现先一次提交全部因子再获取结果的方法有少量因子（1-2个）提交成功，但最后获取结果时发现丢失了。”，您可以在获取到

```
s.get(simulation_response.headers["Location"]).json()["status"].upper() != 'ERROR'
```

之后，再提交下一个。基本到这里，你就已经能获得ID了。
关于模板的自由度提升问题，我们会在接下来的内容覆盖。

---

### 评论 #31 (作者: WL13229, 时间: 2年前)

[YJ78324](/hc/en-us/profiles/12940496308759-YJ78324)

很好的反思，这也是未来我们授课中想不断给大家提升的方向。

一些comment：

```
 last_diff_value(x, 5)
```

1. 如果是用在基本面数据集，上述的参数时间可以从5换到20、60等更长时间，因为基本面数据变动频率低。

2. 关于Alpha信号失效，尝试换个市场做一下

---

### 评论 #32 (作者: OA92025, 时间: 2年前)

1. 此时是12/18/2023 的 15:44，total alphas == 1658.


> [!NOTE] [图片 OCR 识别内容]
> [m s
> IhE
> Itmurt ARI
> ARAA4
> ARANI 41895
> TITTN
> 410tg
> IO
> CJUUIUTAII
> Lst @ Shocts Icol
> II U
> 邬? 
> [LSIaI
> Slmha
> 'OCUIHIII
> 1」 Fpnrs
> 0uarn
> 4ITN
>  lLI4
> THto
> Ruealoh 7372
> OJIIUIt
> Alohas
> UIULIIIC
> SULTIIIC
> IURNN TC]SLJUEIICIIIL KJC +
> TOT|1,558
> GITDOI Ti
> Unsubrnitled:
> 1,62T
> ETIN Aa T2E
> ]TN
>  Oule Celd CST
> Hnn
> Unmete
> Shar
> UlSOTTTTISImnedlr
> UaNT
> ILSIIICMITTI
> 1Ks
> LUIU
> 45
> 1
> TTTUJ
> ULSUENITITO
> 1118770FST
> TUNISI
> 11
> IISICMITTM
> 1283 LST
> TUPUl
> 1446
> 1b
> RR
> UASUFITTTO
> 1
> TTIAT
> 105
> 75y
> WT
> IILSIICMITTI
> TKs
> TUIU
> +10,4
> 1U5
> JITTOI
> 1
> TIA
> UILSIICMITTI
> 1027/223 {OT
> LUIU
> AST
> UTIITTUJ
> RJ
> UHSULITTTD
> 11171772 FUI
> TIIPIII
> 1415
> Ru J
> TILSIICITTI
> 142773 EC
> TUPUl
> 1S
> Rm
> 1+171FUT
> TIIAT
> +141
> JULOI,s
> N
> UI
> e


1. 实现过程：

其实，实质就是通过爬虫实现对brain平台数据的爬取。并且通过python在brain平台上实现simulation。

- Simulate并获取单个alpha的表现，实现断线重连。

F12获取网页代码，找到请求头headers，以及json查询参数（在payload中）


> [!NOTE] [图片 OCR 识别内容]
> Blocked requests
> 3rd-party requests
> 500000 ms
> 1000000 ms
> 1500000 ms
> 2000000 ms
> 2500000 ms
> 3000000 ms
> Name
> Headers
> Payload
> Preview
> Response
> { 4tprdrenO3 7ygan4hUnkbuq
> {:} 4tprdreno57gganT4hOnRGuq
> General
> {;} 4tprdreno57gganT4hOnRGuq
> Request URL:
> https:/lapiworldquantbrain co
> 2021
> {;} 4tprdreno57ggan14hOnRGuq
> m/simulations
> {;} 4tprdreno57gganT4hOnRGuq
> Kequest Method:
> POS|
> {;} 4tprdreno57ggan14hOnRGuq
> Status Code:
> 201 Created
> {;} 4tprdreno57ggan14hOnRGuq
> Remote Address:
> 3.230.56.51.443
> {;} 4tprdreno57ggan14honRGuq
> Referrer Poligy:
> strict-origin-when-cross-origin
> 05
> {} 4tprdreno57ggan14hOnRGuq
> Response Headers
> Wa/
> Access-Control-AIIow-
> true
> {}} 4tprdreno57ggan14hOnRGuq
> Credentials:
> Wa/
> Access-Control-Allow-Origin:
> https://platform worldqu
> {;} 4tprdrenos7ggan14hOnRGuq
> antbraincom
> ort Count
> {} 4tprdreno57gganT4hOnRGuq
> Access-Control-Expose-
> Location Retry-Atter
> {;} OAXMQMP
> Headers:
> 878
> {}} recordsets
> Allow
> POST, OPTIONS
> {} yearly-stats
> Content-Language:
> en
> 928
> {}
> Content-Length:
> 964
> {} OAXMQMp
> Content-Type:
> textlhtml; charset-UTF-8
> {;} authentication
> Date:
> Mon; 18 Dec 2023
> 971
> {} authentication
> 1224508CMT
> 989
> {;} authentication
> Location:
> https:/lapiworldquantbr
> {}} authentication
> aincom/simulations/4tpr
> 1069
> {;} authentication
> dreno57ggan14hOnRGuq
> {:} authentication
> Retry-Atter
> 25
> 1187
> {;} authentication
> Accept-Language; Cookie
> 10
> {;} authentication
> Vary:
> Origin
> X-Frame Options:
> SAMEORIGIN
> {} authentication
> X-Request-Id:
> 3581a24334144e+08e638
> {;} authenticatinn
> 32329947621
> C
> 
> {
> II
> ]I
> 4 {!
> O
> I
> pnl
> Vary



> [!NOTE] [图片 OCR 识别内容]
> o
> AIIUIT
> 」|7
> TsI
> NaTPINI WIUOUNIUN CIITSIat
> 8
> N
> 1+
> SIIIUlULC
> U Apho
> ComCILOJI OI
> 回  曰
> SIIUUTI 2
> ]
> TIMTTIII
> 4650175
> Solo
> ootO
> 
> JPNKas
> J
> DattoICTIJqUanlbun
> TLILIL
>  Ioom
> IIII
> U
> -」
> 
> AIaII
> Rost Rlo
> CNNJC
> [yI
> NAR
> TIIISI
> U La
> ]a
> LsttSnls:
> Tmattauli
> 2[4
> UIoCSgILEITRU
> UIo CSTgILEITRUC
> ULay
> 410034940517791461740
> NIO
> I
> Oae
> OT
> AIIISIITTAct
> OIInt
> RIIUal t
> AIItSIITct
> U
> Miots9qarEJ
> UotIS9qaIEU
> 3.49
> 14.45%
> 5.48
> 35.61%
> 10.20%
> 49.26mo
> TCIICALI
> TNIUI
> SRUe
> ISTII
> W TUg
> 9108
> I
> 
> h
> Ufeda
> NIOII
> Lom Cot
> C
> aoCI +
> 。|m
> AeSTPeaK
> 8-TA
> 4
> 1b
> U TqqecI
> ONI
> 17
> 115
> 4nt
> 
> 454!
> SU
> 202-Sa
> OMJI
> T ?1
> UJIIOI
> O IIIUII
> 1308
> 09
> O TI IIIIII
> OITIIII
> 1451
> IT
> I
> OI
> TTtT
> ITrto
> III
> UI
> SUaml
> Nh
> 7
> hary


这些是我们需要的参数。复制粘贴到本地python代码中，稍作修改，就可以实现多个alpha的爬取。

- 获取在IS中的alpha_list列表(unsubmitted)

查看list的详情，list中是1627个alpha的dictionary，包含alpha的id、regular（表达式）、setting详情、表现等数据。


> [!NOTE] [图片 OCR 识别内容]
> alpha_Iist
> 刎0 (LIst) (1621 兀奈)
> 6 可 A  #  田 Es 幸 +
> 未引 ^
> 奖
> 十小
> dict 23
> {'id':'3EGNY9O '
> type
> REGULAR'
> author
> 0492025
> settings' :{'in
> 28
> dict 23
> {'id': 'nnzEWLX'
> tyPE
> REGULAR'
> author
> 0492825
> settings' :{'in
> 29
> dict 23
> {'id':
> AnaAqlX'
> 'type
> REGULAR'
> author
> 0492025'
> settings' :{"i
> 38
> dict 23
> {'id'
> LnxooeG
> type
> REGULAR '
> author
> 0492025 '
> settings' : {'in
> dict 23
> id '
> OnzdzPI '
> type
> REGULAR'
> author
> 0492025'
> settings ' :{'in
> 32
> dict 23
> {'id'
> WNXSKAQ
> type
> REGULAR'
> author
> 0492025
> settings ' :{'in
> dict 23
> {'id' :'nnZEOXE'
> type
> REGULAR'
> author
> 0492025'
> settings' :{'in
> dict
> 23
> {'id'
> YNkeGNM'
> type
> REGULAR'
> author
> 0492025'
> settings
> :{'in
> 35
> dict
> id'
> AnaAgpd
> type
> REGULAR
> author
> 0492025
> settings' :{'in
> dict 23
> id '
> ZVZYSAP
> tyPe
> REGULAR
> author
> 0492025
> settings ' :{'in
> dict 23
> id'
> aNPpkOO'
> type
> REGULAR
> author
> 0492025
> settings' :{'in
> 38
> dict 23
> {'id':'Onlx8zs
> type
> REGULAR '
> author
> 0492025
> settings ':{'in
> 39
> dict 23
> {'id':
> OnmlLr7'
> type
> REGULAR'
> author
> 0492025'
> settings ' :{'in
> dict 23
> {'id':'7XX55Q5'
> type
> REGULAR'
> author
> 0492025'
> settings
> :{'in



> [!NOTE] [图片 OCR 识别内容]
> 833 -字典 (Dictionary} (23 元索)
> 囚 I9# C: 幸 
> 从
> author
> Str
> 0492025
> category
> NoneType
> NoneType object
> color
> NoneType
> NoneType object
> competitions
> NoneType
> NoneType object
> dateCreated
> str
> 2023-10-27711:09;89-04.88
> dateModified
> str
> 2023
> 10-27T11
> 09:10-04:80
> datesubmitted NoneType
> NoneType object
> favorite
> b0o1
> False
> Brade
> NoneType
> NoneType object
> hidden
> boo1
> False
> id
> str
> nnzEOXE
> dict
> 5225085,
> booksize
> 20000000
> IongCount
> 1557,
> shortCount
> name
> NoneType
> NoneType object
> NoneType 1
> NoneType object
> pnl


可是太慢了，现在还没有跑完，ddl快到了，就先交了，之后再补上结果。。。


> [!NOTE] [图片 OCR 识别内容]
> 帮助 |变量浏览器 |绘图
> 文件
> 控制台 I/A X
> CONCENTRATED_WEIGHT
> result
> PASS
> },
> { 'name
> LOW
> SUB
> UNIVERSE SHARPE
> result
> PASS
> Iimit'
> 0.85,
> Value
> 1.71},
> {
> name
> SELF
> CORRELATION
> result
> PENDING'},
> { 'name
> PROD_CORRELATION
> result'
> PENDING'},
> { 'name
> REGULAR SUBMISSION
> result'
> PENDING
> },
> {
> name
> LONG DURATION
> result'
> FAIL'},
> {'name
> MATCHES
> THEMES
> result
> WARNING
> matched
> [],
> unmatched
> [{'id
> V4IOkBM
> name
> Global
> Delay-1
> multiplier
> 5.0}]},
> { 'name
> IS LADDER SHARPE
> result
> PASS
> year
> 2,
> startDate
> 2021-02-16
> endDate
> 2019-02-17
> Iimit
> 2.37,
> Value
> 2.68}]},
> Os
> None,
> prod
> None _
> competitions
> None_
> themes
> None_
> team
> None}]
> In [5]: runcell(' 获取所有满足条件的aLpha' 
> '0:/南京犬学1职业
> 发展/WorLdquant
> Brain/1ooe次:py' )
> In [6]: runcell(8,
> '0:/南京犬学/职业发展/WorLdquant Brain/
> 1000次:py
> 100%
> 1627/1627[08:23<00:00,
> 3.
> 23it/s]
> In [7]: runcell(l,
> '0:/南京大学1职业发展/WorLdquant
> Brain/
> 1800次.py
> )
> IPython控制台|历史
> OI
> 3.10.9)
> Completions:
> conda (base)
> LSP: Python
> Line 64,
> Col 1
> UJIF-8
> CRLE
> `
> IIem 6


3.问题反思：一直没有弄明白，为什么我能够获取alpha列表、simulate每个alpha、获取每个alpha的表现，但是却没有真正simulate成功？也就是我的alpha提交次数还是不变，没有增加？

---

### 评论 #33 (作者: FL11741, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 4,113
> Total Active Alphas
> 53
> Total Decommissioned Alphas
> Total Alphas
> 4,166
> Br
> 18:19
> 2  5
> 谷 O) l
> CPU
> 2023/12/18



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 5,769
> Total Active Alphas
> 53
> Total Decommissioned Alphas
> Total Alphas
> 5,822
> 1715
> 22:58
> W
> 申  9
> 谷 f) p
> UPU
> 2023/12/18


因为我自己没什么基础，本着一步一个脚印的精神，这次Case1我主要把重心放在程序框架的构建上，大概有了一个整体的思路，一些细节可以之后再作补充和调整。

模版方面选择了最简单的rank(ts_backfill(x,20))，主要起到试跑程序的作用。

程序方面我主要分为三个方面：效率、功能、稳定性。首先讨论效率。效率方面在我们没有做类似于大数据量的相关性实验这些的前提下，很明显时间成本主要都在brain平台的simulation功能上，因此在效率设计方面核心应当是让平台simulation尽量保持满载状态。因此这里选择队列+多线程，alpha list进alpha id出，效果类似下载器，保持10个simulate满载。(截图选用的GLB的数据，实测跑的比CHN慢了3倍多）


> [!NOTE] [图片 OCR 识别内容]
> 72m 23s
> waiting
> processing
> finish
> fnd28_fsq1_value_031019
> fnd28_newq_value_086769
> fnd28_value_ 19514
> fnd28_wsannualstats_Value_08336
> fnd28_Value_072109
> fnd28_nddql_value_031019
> 2
> fnd28_levliqa_Value_08131a
> fnd28_Value_053769
> fnd28_value_05008
> 3
> fnd28_bdeq_value_ 181839
> fnd28_Value_ 182009
> fnd28_nddql_value_030699
> 4
> fnd28_cfsourceusea_Value_ 04440a
> fnd28_Value _05007
> fnd28_cfsourceusea_Value_ 04301a
> 5
> fnd28_nddqz_value_188549
> fnd28_Value_ 18208
> fnd28_cfq_value_041509
> 6
> fnd28_fsql_Value_025019
> fnd28_Value_08216
> fnd28_nddql_value_032499
> 7
> fnd28_nddql_value_025019
> fnd28_ishtspmnt_value_01155a
> fnd28_cfsourceusea_Value_04351a
> 8
> fnd28_pftlta_Value_08301a
> fnd28_ratesq_Value_084219
> fnd28_ratesq_Value_083219
> 9
> fnd28_fsq1_Value_030639
> fnd28_Value_ 19504
> fnd28_ratesq_Value_086769
> 10
> 1222
> 10
> 430



> [!NOTE] [图片 OCR 识别内容]
> 254m 7.Os
> Waiting
> processing
> finish
> None
> fnd17_xlcxspemtt
> fnd17_ttmtaxpd
> None
> fnd17_ttmtaxrate
> fnd17_ttmsgazrev
> None
> fnd17_vollodavg
> fnd17_ttmroipct
> None
> fnd17_zpxetniq
> fnd17_ttmrevstrt
> None
> fnd17_yield
> fnd17_ttmrevps
> 5
> None
> fnd17_voctniq
> fnd17_ttmrevpere
> None
> fnd17_zfcserpedq
> fnd17_ttmrevchg
> None
> fnd17_volldprc
> fnd17_ttmrev
> None
> fnd17_vol3mavg
> fnd17_tmrecturn
> None
> fnd17_xlcxspemtp
> fnd17_ttmpelow
> 10
> 10
> 1652


功能上，由于simulation和后续result研究的分离，并且get函数获取结果数据不会影响simulation进行（我猜），我们有充裕的时间在simulate过程中用alpha id再去获取数据以及做一些基本的处理。因此这一方面灵活度是比较高的。例如我这里做了几个定时刷新的表格，上面的截图提示simulate进度，下面的提示最近完成得到的结果，以及按照fitness排序得到实时排名最高的5个alpha。（忘记截图了，跑了一点点别的作示例）


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> datafield
> ftness
> sharpe
> turnover
> returns
> drawdown
> OnRAekd
> fnd28_value_09104
> -0.36
> -0.68
> 0.024
> -0.0357
> 0.4724
> AneVGgR
> fnd28_Value_05057a
> 0.0
> 0.03
> 0.0124
> -0.0023
> 0.491
> 2
> VXZxnXO
> fnd28_newal_value_07230a
> -0.47
> 0.66
> 0.0115
> -0.0631
> 1.0089
> 3
> Qnove75
> fnd28_keyfinancials_Value_07230a
> -0.47
> 0.66
> 0.0115
> -0.0631
> 1.0089
> NnLNMQL
> fnd28_value_03491a
> None
> 0.0
> 0.0
> 0.0
> 0.0
> gmXevQM
> fnd28_Value_05032a
> -0.03
> 0.11
> 0.0123
> -0.0084
> 0.5392
> 6
> VXZxn68
> fnd28_Value_05072a
> 0.01
> 0.05
> 0.0123
> -0.0042
> 0.5349
> KnVJeOE
> fnd28_ratesq_Value_083669
> 0.29
> 0.58
> 0.0246
> 0.0321
> 0.3101
> EqNG3VJ
> fnd28_annualgrowth_Value_08821a
> -0.27
> 0.56
> 0.0159
> -0.0288
> 0.5183
> WS3QGYV
> fnd28_Value_05062a
> -0.03
> -0.12
> 0.0124
> -0.0093
> 0.5755
> alpha_id
> datafield
> fitness
> sharpe
> turnover
> returns
> drawdown
> OAXYqwI
> fnd28_Value_09402
> 0.36
> 0.66
> 0.0196
> 0.0376
> 0.2401
> WS3Qqm2
> fnd28_Value_09202
> 0.31
> 0.56
> 0.0233
> 0.0387
> 0.2207
> 25g329d
> fnd28_newq_value_083669
> 0.29
> 0.58
> 0.0246
> 0.0321
> 0.3101
> KnVJeOE
> fnd28_ratesq_value_083669
> 0.29
> 0.58
> 0.0246
> 0.0321
> 0.3101
> aNeVp22
> income_beforeextra
> 0.25
> 0.46
> 0.0239
> 0.0379
> 0.4854
> sUCCess : 408
> fail:1


稳定性上，要保持程序稳定运行下去，需要程序很强的处理异常能力。这里我还没有做深入研究，暂时简单将所有异常一并等待，重试，跳过处理。

目前遇到的两个主要问题和对未来改进方向的想法：一个是对异常的处理比较粗糙，网页端的错误信息（simulation_limit_exceeded）目前没有拉起异常，不能打断线程进行。另一个问题就是multi-simulation的上限问题，我在文档中没有找到明确说明multi个数*child个数的上限，自己手动试测了一下，结果simulate权限被屏蔽了近两个小时:-) ，因此我目前暂时用的是跑满10个single simulation的方法。如果能确切知道multi上限，可能可以大幅度提升效率。在程序上还有一个比较重要的功能可以添加，就是像下载器那样不但可以满载运行，还可以在程序运行时实时调整队列顺序，比如将临时想测的alpha插入队列最前端等等。其他功能方面主要还是服务于ideas，暂时没有必要过多深入。

---

### 评论 #34 (作者: ZZ51944, 时间: 2年前)

### 数量截图


> [!NOTE] [图片 OCR 识别内容]
> Alpha
> 查看全部
> 成就
> 查看成就
> 地位
> 20
> 18
> GOOD
> 末提交的 Alpha 总数
> 2,336
> 活跃 Alpha 总数
> 45
> BCELLENT
> SFECTACULAR
> 退役 Alpha 总数
> 总 Alpha 数
> 2,381
> 98%电量可用。电池电量可用4小时7分钟
> World.
> Untitle:
> Jupyte.
> 工作簿
> 弄子里
> 微信
> 22:18


（今天没跑完，明早跑完了补充一个结果）


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See au
> Status
> Total Unsubmitted Alphas
> 2,497
> Total Active Alphas
> Total Decommissioned Alphas
> Total Alphas
> 2542


一次性实现截图：

（今天没跑完，明天跑完了补充一个结果）

### 
> [!NOTE] [图片 OCR 识别内容]
> 11%
> 11/101
> -22:31<3:0
> 8:18,
> 125.545/1]
> 0%
> 0/4
> -00:00<?
> ?i/5]
> 259
> 1/4 [01:05<03:17,
> 65.985/1」
> 50%
> 2/4 [01:06<00:54,
> 27.385/1]
> 759
> 3/4 -01:09〈00:16,
> 16.205/1]
> 1009
> 4/4 [02:00<00:00,
> 30.145/1]
> 129
> 12/101
> [24:37<3:0
> 6.16,
> 125.5751」
> 0%
> 0/4
> -00:00<?
> ?i/51
> 259
> 1/4 [01:19<03:59,
> 79.905/1」
> 50%
> 2/4 [01:25<01:11,
> 35.995/1]
> 759
> 3/4 -01:31<00:22,
> 22.50s /1t]
> 1009
> 4/4 [02:32〈00:00,
> 38.145/1]
> 13%
> 13/101
> [27:16<3:1
> 8:59,
> 135.68S /11
> 0%
> 0/4
> -00:00<?
> ?i/51


### 

### 总结：

- 代码效率：

1. 最大化模拟，10个同时模拟
2. 常规操作：使用并行计算、向量化操作和优化算法来提高代码的执行效率。
3. 但是，好的思路比暴力算法更有用

- Debug经历：

1. 查文档
2. 虽然有ACE框架，但是自己重写函数熟悉度更高，也不容易出bug，同时还可以更完全高效的表达思想
3. 可以用GPT-4 + Brain文档协助Debug和编写函数
4. ```
   报错RemoteDisconnected：网络原因导致的报错，有可能是因为刷新了Brain页面，还有可能因为VPN不稳定
   ```

- 模板适合的数据类型：

```
ts_skewness(vec_avg({x}),120
```


> [!NOTE] [图片 OCR 识别内容]
> ts_Skewness
> (X,
> d)
> 偏度是时间序列向量X的第三个中心标准化矩。偏度可以看作是时间序列向量X 中值分布不对称性的度量。
> 卫[(孑 -卫孑?
> 5(孑) =
> (卫[(孑-}孑)2)3/2
> 如果偏度大于零,
> 则分布为正偏态;如果它小于零,
> 则呈负偏斜;如果等于零,
> 则它是对称的。对于解释和分
> 析,
> 请关注下行风险。负偏度分布具有统计学家所说的长左尾
> 对投资者来说, 这可能意味着出现极端负面
> 结果的可能性更大。正偏度意味着频繁的小负面结果,
> 而极坏的情况不太可能发生。
> Mean
> Median
> Median
> Medan
> Mode
> Mode
> Mean
> Mode
> Positive
> Symmetrical
> Negative
> Skew
> Distribution
> Skew
> Mean


使用偏度处理新闻数据具有解释性。这可能意味着负偏态表征新闻预示着不好的情况，而正偏态则反应市场欣欣向荣。

- 模板的改进方向：
  - 添加信号：可以将个人常用信号放在一个列表中，使用循环尝试能否改进alpha的表现
  - 尝试将该模板作为一个信号，预示着某种市场情绪
  - 将不同数据字段进行数学运算后进行测试

---

### 评论 #35 (作者: WL13229, 时间: 2年前)

[OA92025](/hc/en-us/profiles/18197007430167-OA92025)

请使用相应的Alpha运行如下代码

s.get(simulation_response.headers['Location']).json()并阅读信息。里面的message应该会告诉你。大概率是你用了不合适的数据。

---

### 评论 #36 (作者: WL13229, 时间: 2年前)

[FL11741](/hc/en-us/profiles/18515544005527-FL11741)

很好的思考！特别是使用队列和插队的管理思路，将很多工作和simulation分开，非常聪明。一个multi最多有5个child

---

### 评论 #37 (作者: OA92025, 时间: 2年前)

您好老师，我是用了这个代码的，也能成功获取所有信息和表现，但是我的alpha提交次数却始终没有更新

---

### 评论 #38 (作者: TG50517, 时间: 2年前)

一、上周四晚上的截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 24,057
> Total Active
> Alphas
> 301
> Total Decommissioned Alphas
> Total Alphas
> 24,358
> 20.40
> 窦
> 4) 匈
> 2023/12/14


二、本周一晚上的截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 25,800
> Total Active Alphas
> 302
> Total Decommissioned Alphas
> Total Alphas
> 26,102
> 22:30
> 窦 {d匈
> 2023/12/18


三、在周一上午提交了1277个Alpha进行回测，把它们分为10个一组，共计128组，每次提交一组，并打印其序号(序号从0开始)，这样当序号为127的组回测完成以后，表明全部回测完成，以下是部分截图。


> [!NOTE] [图片 OCR 识别内容]
> len (simulation
> data_Iist )
> 1277
> Max_sImU
> simulation_data_list_multi[simulation_
> data_list [i:itmax_simu ]
> for
> range(0,Ien(simulation
> data_Iist ),max_simu) ]
> len (simulation_data_Iist_multi )
> 128


上面是分组的代码


> [!NOTE] [图片 OCR 识别内容]
> Error
> Resurle
> 67 &9 IO II 12I314 IS I6 17 18 I9 ZO 21
> 22 23 24 25 26 27 28 29 30 31323334 35363738394041424344 45
> 46 474849 SO 51525354 5556 57 58 59
> 68 GI 62 6364 55
> 66  6768 69 7071727374757677 78 79 &0 8182 &3 &4 85 &6
> 88 89 g091 929394 95 96 97
> 98 99 leo
> lI 102 103 194 Ios 106 107
> 188 Iog 110
> III I12
> 113114 115 115 117 I18 119
> 120  12
> 122123124125126 127
> len(result)
> 1277


上面是回测时程序打印出来的序号，以及最终得到的回测结果的个数

这里强调一下重点。为了测试程序的稳定性，在回测进行到第3组(打印出序号2)的时候，故意拔掉网线，自然这时候出现了错误，打印出“Error”，然后又插上网线，这时会打印出“Resume”，并从之前中断的那组开始重新simulate。

为了验证这个功能得到结果的正确性，回测了10个简单的Alpha，1次1个，第一次完整回测，第二次中间故意拔掉网线，然后又恢复，发现这两次得到的alpha_id完全一样，表明这个功能是可靠的。


> [!NOTE] [图片 OCR 识别内容]
> O1234567 8
> len (result )
> 18


第一次正常回测


> [!NOTE] [图片 OCR 识别内容]
> Error
> Resume
> 4S67 8
> len(result_I)
> 10


第二次中间拔掉网线，然后又恢复


> [!NOTE] [图片 OCR 识别内容]
> for
> in range(len(result))
> print(result [i] [ 'alpha_id' ])
> VXdOKRM
> mqYGwpX
> jne8lys
> onoWwj6
> en6Qgo]
> GRAK3ZG
> OnoWAWS
> IojZIAM
> Jnpomyl
> JnPOmPE
> for
> in range
> len (result_1) ) :
> print(result_I[i] [ 'alpha_id' ])
> VXdOKRM
> mqYGwpX
> jne8lys
> onoWwj6
> en6Qgo]
> GRAK3Z6
> OnoWAWS
> IojZIAM
> JnpOmyl
> JnPOmPE


这两次得到的alpha_id完全一样

四、总结反思

代码效率：这里大部分程序是我自己写的，10个Alpha为一组，一组整体提交，回测完一组并保存结果后再提交下一组，没有用到多线程，所以没有ace库里面的simulate_alpha_list_multi函数效率高，下面的改进方向就是尽可能提高代码的执行效率。

debug经历：之前没有太多的Python编程经验，所以try…except什么的都是上午边学边写。尤其是需要考虑到程序运行时可能会遇到不止一次错误，每次遇到错误都需要从断点继续运行，刚开始写的代码遇到了死循环，经过不断修改最终实现了自己想要的功能。

模板适合的数据类型：我用的模版和老师举的例子非常相似，也是最常见的ts_rank和rank等operator的组合，所以比较适合那些自身就包含公司排名信息的数据，我也是这样搜寻数据的。虽然模版很简单，经过优化以后，也能得到可以提交的Alpha，并完成提交，如下图所示。


> [!NOTE] [图片 OCR 识别内容]
> Passed Alphas;
> XeV3nlp
> Mbda]j8
> RN9b8L2
> alebn32
> OnRN3Id
> Knvrljz
> IqdGRJ
> XKVbIEm
> knvo078
> pnxSal
> dnylrd]
> GRZjNLS
> LnEIN3e
> NnLVy8
> U3b4ko
> 「b900G]
> IoOK3EN'
> nnmPRy8
> JnolPx2
> dnybglv
> GnxOpNZ
> nnmdllg
> RNgbPwe
> aNetrEI
> JnOQEmX
> Knv7ZM
> Qnob76w 
> 436022
> LnENo2
> Gnxop7z
> EqNRAYR
> SLrBOZ]
> Bbnlg
> RN9bExb
> V5ZjOL3
> SLrBnOz
> EqNROXJ
> dnybdy]
> dnyboyy
> VXZOOEJ
> GRZjPBG
> inoAYKW
> aNebQx2
> dnylv
> Jnoomdn
> 3EIXJmO
> EqNRAYP
> OnRWevk
> WN3emxd
> IoOXdEX '
> qnOHJWE
> 61J6072
> rbgodzj
> XeV3OkP
> OnRNZV
> 17EKdBX
> XkV7O5n
> 3EIVXAZ'
> pnt5mXO
> NnlabkE
> RN9bouz
> LnENOeg
> 9981069
> Inla3me
> ZjBARK8
> OnObEel
> 1b90403
> PnxR8Oj
> SLFZNRG
> ZjgAGXI
> SLrBoI]
> BAxpddq
> ZSBDjSR
> SLrzGJK '
> BmXbK7V
> SLFZION
> 75NPg
> eNGSY
> 100Z51K
> Jnol0ll
> QnObvpl
> Knvlgaz
> XkVbZGI
> XkVJELB
> nnndr5 
> 998Wlbe
> 100XB16
> JnoNazj
> Nnla]
> ZVSWXLW
> 3EIXAIQ
> KnvoJLZ
> VKZGId4
> OnRFPKR
> BOVPKMI
> Mbdakwk
> IoOX3OW'
> 'I7EVBA7
> nnmdvGi
> 3E1VMR
> aNebOJR
> XeV37Op
> aletGe0
> I7EKZZI
> LnEN'IYg
> I3b7RG
> aNebkmw'
> IoOXpVZ
> LnEZOAI
> 80Vi19a
> ZSBBFJX
> OnRLIOn
> IoOPez
> Gnx05o0
> Nnla728
> Pnx2kJE
> 7x3NekL
> EqNppxK
> 3EI9d00
> VSZjOLd
> Pnxgjak
> KnvNVJj
> OXEPZ
> nnmpwll
> OnRrgqb
> IoOX8jX
> 7x3NJr5
> Gnxbbxs
> GRZJEZO
> Gnxbzg]
> NnLaJNx
> OAxxpns
> rbgepg]
> W3PE
> Pnt5yx3
> dnyj3Qk
> Iqd6WRP
> 4532142
> mqdxKk
> Jnozpbe
> 998lyIr
> V52295b
> NnLaBGE
> jnoAedE
> gOVpgr
> TqdmJOK
> JnoNAod
> 998JdEV
> W53Y5k1
> rbgONRd
> 17EVY17'
> BAxrdZK
> 99BJEAr
> 2vgwGAy
> WN3eM3J
> AneyR7e
> ZSBBenx
> enNbbG5
> VSZrr63
> V5223b3
> bMJOVYI
> RNgbuad
> Knv703B
> ZSgbInl
> IOOXNRG
> 3EIXKjN' _
> V5228yr
> Bk800
> OnR8qIb
> AneNAoe
> Jnollle
> Pnx750]
> RlgGlee
> Rlgbsen
> GRZKVIE
> BmKble]
> bNJbwel
> AneNrQg
> 9987
> 6RZJAYG
> LNENMSe
> RIgbmod
> 3EIXVa
> VSZFEOd
> Bbbl]
> ZSBbIeE
> OnRNVPV
> ORIIIE
> EqNpk3P
> 99BWJK
> W3bJRo
> mqdmnlx
> Jnooyvl
> pb95Xao
> AnCNAOH
> COXOAZ
> Tqdml3
> GRZJGOO
> AnevqZB
> OnRHSR
> GRZJOAJ
> yN87b2]
> IOOxE3Q
> Gnxbjpo
> VSZrbIG
> VXZBBLG
> GRZrVLS
> GnxbOXG
> QnObooi
> ZVSmRJ5
> YN87b06
> OnRHSVmI
> IXPBX
> dnylAPB
> SOVjRao
> GnxIgk5
> 2VSwmy
> ZSBBe7R
> SLrB7P]
> IoONORK
> IoOxBIQ
> YNBbA8I
> BmxZ6al
> BAXXV
> nnmddql
> BmXZkAN
> EqNROXK
> Bmxjayl
> nIPKRI
> len(is
> passed
> alphas )
> 229



> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> Self_COTT
> COTT
> delta_sharpe
> delta
> turnover
> delta
> ftness
> delta_returns
> delta_drawdown
> delta_margin
> 1oOX3OI
> 0.4140
> 0.4910
> 0.01
> 0.01
> 0.01
> 0.01
> 0.0
> 0.00
> 191
> mqdmnlX
> 0.4233
> 0.5051
> 0.01
> 0,02
> 0,01
> 0.01
> 0,00
> 203
> GnXbp0
> 0.4398
> 0.5150
> 0.01
> 0.04
> 0.01
> 0.00
> JnoNazj
> 0.4563
> 0.5089
> 0.01
> 0,06
> 0,01
> 0.02
> U0
> 0,01
> 157
> enNbbGG
> 0.6561
> 0.7089
> 0.01
> 0.08
> 0.01
> 0.01
> Prod



> [!NOTE] [图片 OCR 识别内容]
> submit_id
> IoOX3QW
> ace. submit_alpha (s, submit_id )
> True



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Sharoe
> LUTnoyer
> HIUTCS5
> HeLUTnS
> UraOOT
> Wa「eT
> 2.56
> 22.8396
> 1.68
> 9.81%
> 3.68%
> 8.5gyoo


改进方向：现在遇到的问题是可以提交的Alpha太多，需要从这些Alpha里面筛选出好的Alpha，怎样判断Alpha的好坏需要一定的经验积累。另外需要把常用的程序段写为函数的形式，用到时就直接引用，这样就不需要重复造轮子。

---

### 评论 #39 (作者: OL40142, 时间: 2年前)

1. 原始


> [!NOTE] [图片 OCR 识别内容]
> 鬯嘤
> Simulate
> Alphas
> Data
> 留 Competitions (2)
> Performance
> Alphas
> Account
> Total: 575
> Unsubmitt
> Alpha Lists
> Achievements
> Unsubmitted:
> 560
> Referral Tracker
> Active:
> 15
> Decommissioned:
> Agreements
> Select Columns
> atus
> Date Created (EST)
> Sign Out
> Searcn
> Selec
> Selec
> Selec
> Searcn
> Selec
> Selec
> anonymous
> Raular
> UNSUBIITTED
> 12/01/2023 EST
> CHI
> TOP3UOJ
> 21:53
> 2023,12118


2. simulate结束之后


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Total: 1,166
> ShoW
> Unsubmited:
> 1,151
> Active:
> 15
> Select Columns
> tUS
> Decommissioned:
> CCC
> EICTJITJTs
> 二U
> UNSUBMITTED


程序内确实做了1000次simulation，但是为什么这儿没有效果？是因为alpha在simulation时出现错误了嘛？程序也没有报错？存储下来的simulation结果也正常


> [!NOTE] [图片 OCR 识别内容]
> result
> df.info()
> [1]
> 00s
> 〈C1a55
> pandas
> Core.frame
> DataFrame
> Index:
> 999 entries,
> KnVNINPL
> to YNBaNao
> Data
> columns (total
> Columns)
> Column
> Non-Null Count
> Dtype
> LOW_SHARPE
> 999
> non-null
> object
> LOI FITNESS
> 999
> nOI
> null
> object
> LOW_TURNOVER
> 999
> non-null
> object
> HIGH
> TURNOVER
> 999
> nOI
> null
> object
> CONCENTRATED_WEIGHT
> 999
> non-null
> object
> LOW_SUB_
> UNIVERSE_SHARPE
> 999
> nOI
> null
> object
> SELF_CORRELATION
> 999
> non-null
> object
> PROD CORRELATION
> 999
> nOI
> null
> object
> REGULAR_SUBMISSION
> 999
> non-null
> object
> MATCHES
> THEMES
> 999
> nOI
> null
> object
> IS_LADDER_SHARPE
> 999
> non-null
> object
> dtypes
> object(11)
> memory usage:
> 93.7+  KB


3. simulate方式：

（1）取数据集：取USA股票D1数据集

（2）取fileds：在每个数据集中，取coverage>0.5且为matrix类型的的fields


> [!NOTE] [图片 OCR 识别内容]
> settings
> {'region
> US』
> delay'
> '1'
> universe
> T0P3000
> instrumentType
> EQUITY' }
> datasets_df
> datasets(5, Settings
> datafields_df
> pd.DataFrame
> for
> in datasets_df["id"]:
> datafields
> get_datafields(s, settings, id)
> i SUM( [X
> in datafields .columns
> for
> ["id"
> "pegion"
> "delay"
> universe"
> coverage
> type"]])
> IdX
> 叩.logical
> and(datafields ["coverage
> 8.3,
> datafields["type"]
> "HATRIX"
> datafields
> datafields.loc[idx, ["id"
> region"
> delay"
> universe"]]
> datafields_df
> datafields_df
> append(datafields, inore_index=True)
> if datafields_df.shape[o]
> 〉  358:
> break
> datafields_df .head()
> 45s
> region
> delay
> universe
> a0111_2_1e
> USA
> TOP3000
> 30111_2_19
> USA
> TOP30O0
> anl11_21pme
> USA
> TOP3000
> 30111_2_1tic
> USA
> TOP30O0
> a0l11_2_Ze
> USA
> TOP3000
> Bet


（3）定义操作符

（4）生成alpha表达式

（5）并行回测，每次10个simulation


> [!NOTE] [图片 OCR 识别内容]
> import
> CUOICUI
> ent .futures
> While
> Count
> 1088:
> With
> Concurrent .futures .ThreadPoolExecutor
> executor:
> 并行
> parameters
> range (".count,
> Count+lo)
> executor
> parameters)
> 通过 map 实现并行
> 8Gm 5485
> The 971th alpha
> done
> simulating
> The
> 972th alpha
> done
> simulating
> The 973th alpha
> done
> simulating
> The
> 974th alpha
> done
> simulating
> The 975th alpha
> done
> simulating
> The
> 976th alpha
> done
> simulating
> The 977th alpha
> done
> simulating
> The
> 978th alpha
> done
> simulating
> The 979th alpha
> done
> simulating
> The
> g8oth alpha
> done
> simulating
> The g8Ith alpha
> done
> simulating
> The
> 982th alpha
> done
> simulating
> The 983th alpha
> done
> simulating
> The
> 984th alpha
> done
> simulating
> The g85th alpha
> done
> simulating
> The
> 986th alpha
> done
> simulating
> The 987th alpha
> done
> simulating
> The
> 988th alpha
> done simulatingThe
> g8gth alpha
> done simulating
> The
> ggoth alpha
> done
> simulating
> The ggIth alpha
> done
> simulating
> The
> 9g2th alpha
> done
> simulating
> The
> 9g3th alpha
> done
> simulating
> The
> 9g4th alpha
> done
> simulating
> The gg5th alpha
> done
> simulating
> The
> 9g6th alpha
> done
> simulating
> The
> 997th alpha
> done
> simulating
> The
> gggth alpha
> done
> simulating
> The gggth alpha
> done
> simulating
> The loooth alpha
> done simulatin
> do'
> Map


4. 一些进一步的思考：

现在的操作都比较简单，单个运算符、单句回测、单个datafield，只是为了尝试回测框架，很难产生有效产出

（1）operators复杂化，进行组合，实现操作

（2）datafields组合进行操作

5. 一些问题：

（1）我的alpha表达式应该没有出错，数据集也正常，且只有在s.get(simulation_response.headers["Location"]).json()["status"]==‘COMPLETED’的时候才会计数，那问题可能出在哪里？

（2）在取数据集的时候，有些fields好像没有coverage、type等参数，这些是正常的嘛？

---

### 评论 #40 (作者: WL13229, 时间: 2年前)

@ [OA92025](/hc/en-us/profiles/18197007430167-OA92025)

同学您好，simulated和submit不是一个概念，submit没有增加是正常的。只有在s.get(simulation_response.headers["Location"]).json()["status"]==‘COMPLETED’的时候才会计数。另外如果您说simulated词数没有增加的话，可能你一直都在重复simulate以前的一个Alpha。另外请通过alpha id获取表现，才能看到是否有bug。Alpha id要和performance一一对应。检查一下你的Alpha id.最好提供截图，谢谢。

---

### 评论 #41 (作者: WL13229, 时间: 2年前)

@ [OL40142](/hc/en-us/profiles/16271500817559-OL40142)

你的观察是正确的。确实只有在s.get(simulation_response.headers["Location"]).json()["status"]==‘COMPLETED’的时候才会计数。这也是为什么要大家去截图的原因。不complete的情况很多，有些是达到了最高的simulate词数，你排队没有排上，有的Alpha没有被回测。有些是你的数据点在该模板的运算下会出现很多异常值。这些都是量化研究需要考虑到的事情。我们会在第二期导航课做展示。

---

### 评论 #42 (作者: WL13229, 时间: 2年前)

@ [TG50517](/hc/en-us/profiles/8166101444887-TG50517)

非常robust的代码！！

如何挑选出适合提交的Alpha，我们在后续课程也会有专门的设计提到。敬请期待。

---

### 评论 #43 (作者: QL10983, 时间: 2年前)

这是周一时的simulation数量：


> [!NOTE] [图片 OCR 识别内容]
> 辑
> 显示
> 历史记录
> 书签
> 窗口
> 帮助
> H0Q
> LA
> 12月18日周一
> 10:25
> platform worldquantbrain.com
> 十
> WorldQuant BRAIN
> 英才候选人计划实训考核 (Case1)_202312
> WorldQuant BRAIN
> Simulate
> CAlphas
> Data
> Competitions (3)
> EVents
> Learn
> Refer a friend
> 5
> Unsubmitted
> Submitted
> Alpha Lists
> Total: 726
> Filter
> Unsubmitted:
> 712
> Active:
> 14
> AtUs
> Date Created
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> (EST)
> Plect
> Search
> Select
> Select
> e.8>1
> e.8>1
> e8>1
> Select
> Tag


这是周二的simulation数量：


> [!NOTE] [图片 OCR 识别内容]
> 编辑
> 显示
> 历史记录
> 书签 ^窗口
> 帮助
> dQ
> LA」
> Q
> 12月19日周二
> 14:19
> platform worldquantbrain.com
> Simulate
> QAlphas
> Data
> Competitions (3)
> EVents
> Learn
> y
> Refer a friend
> Consultant
> Infinity Champions 007
> Rank: 13
> 1a5
> Unsubmitted
> Alphathon 2023
> Alpha Lists
> Total: 1,802
> Alphathon 2022
> Rank: 6,983
> National Qualifier
> Filter
> Unsubmitted:
> 1,788
> Competitions
> Active:
> 14
> Btus
> Date Created
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> (EST)
> Plect
> Search
> Select
> Select
> e8〉1
> e8〉1
> e8〉1
> Select
> 300n
> Roolllar
> UNSUBMITTED
> 12/19/2023 FCT
> IICA
> TOP300
> 1 ?704
> 147904
> Tag


这个是代码日志截图：


> [!NOTE] [图片 OCR 识别内容]
> This
> is
> the Ia4ath
> term
> to Ia5ath
> 0f
> the
> simulation
> Sent
> simulation
> request, waiting
> for
> response
> Sent
> simulation
> request, waiting
> for
> response
> Sent
> simulation
> request, waiting
> for
> response
> Sent
> simulation
> request,
> waiting
> for
> response
> Sent
> simulation
> request,
> waiting
> for
> response
> Sent
> simulation
> request, waiting
> for
> response
> Sent
> simulation
> request, waiting
> for
> response
> Sent
> simulation
> request,
> waiting
> for
> response
> Sent
> simulation
> request, waiting
> for
> response
> Sent
> simulation
> request, waiting
> for
> response
> Alpha
> done
> simulating,
> getting alpha
> details
> 259e600
> Final
> Pnl
> retrieved:
> 237933.0
> Alpha
> done
> SimU
> Ilating,
> getting alpha details
> rbgggda
> Final
> Pnl
> retrieved:
> 1350475.0
> Alpha
> done
> simulating, getting alpha details
> 7X31bLZ
> Final
> Pnl
> retrieved:
> 2031431.0
> Alpha
> done
> SimU
> Ilating,
> getting alpha
> details
> EqNXWGm
> Final
> Pnl
> retrieved:
> 1047998.0
> Alpha
> done
> simulating,
> getting alpha
> details
> VSZPMIA
> Final
> Pnl
> retrieved:
> 1585612.0
> Alpha
> done
> SimU
> Ilating,
> getting alpha details
> RNSPQEZ
> Final
> Pnl
> retrieved:
> 1296456.0
> Alpha
> done
> simulating, getting alpha details
> LnE3agl
> Final
> Pnl
> retrieved:
> 1296919.0
> Alpha
> done
> simulating,
> getting alpha
> details
> XeV58vq
> Final
> Pnl
> retrieved:
> 1278903.0
> Alpha
> done
> simulating,
> getting alpha
> details
> jnooRao
> Final
> Pnl
> retrieved:
> 1135700.0
> Alpha
> done
> simulating,
> getting alpha details
> VXZejQA
> Final
> Pnl
> retrieved:
> 1149941.0


思考：

我将Brain平台的网络接口封装了几个函数来供调用，最开始会遇到效率问题，主要是循环1000次速度太慢，而且我在第一次跑的时候忘记修改参数导致所有的simulation都是一样的。后来将10次模拟进行并发，将response全部发送出去并且将报头存起来，发送完成后再以此进行结果查询从而极大提升了模拟的效率。

由于使用了平台给的结果查询示例代码进行每次查询后的等待，基本没有遇见网络问题和代码中断的问题。为了保险起见还是进行了异常捕获以防止代码异常中断。

测试过程使用了之前我发布过的文章中的思想结合ROE和PB，每次测试修改不同的时间段前的系数进行测试。因为最近时间有限，截止周二完成了1000次提交但是还未细致分析结果以及不同参数间的关系，将在后续课程进行中继续深入分析。

---

### 评论 #44 (作者: XC63878, 时间: 2年前)

1. 截图一


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Seeall
> Achievements
> Vew Acheyements
> Status
> 20
> 4日
> GOOD
> OHI
> Total Unsubmited Alphas
> 1,277
> Total Active Alphas
> Total Decommissioned Alphas
> Total Alphas
> 1,321
> 21.25
> 2023/12/14


1. 截图二


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Seeall
> Achievements
> Vew ACheyemenes
> Status
> 20
> 400
> GOOD
> LULIIT
> Total Unsubmitted Alphas
> 2,330
> Total Active Alphas
> Total Decommissloned Aphas
> Total Alphas
> 2,374
> 124+
> 2023/12/19


1. 连续1000个simulation


> [!NOTE] [图片 OCR 识别内容]
> 33/1626 (3.59;+010.40;01
> 32.4651
> Rosnonss [201]〉
> Roylrror
> TTacebycl
> LTOC 1
> TpnOm
> 357
> O]l


这一块完成的不太好。由于自己的代码中没有使用多线程，效率特别慢，基本上跑完一个Alpha要半分钟，所以要跑完1000次回测肯定会遇到登录超时的问题（如上图所示）。需要在代码中增加异常检测和断点续传的功能。

如果登录超时，报错的情况不太一致。根据观察，有时是simulation_progress_url = simulation_response.headers['Location']报错KeyError:'location';有时是报错ConnectionError: ('Connection aborted.', TimeoutError)。所以异常情况需要考虑的比较全。

为了提高处理效率，自己想到的解决方案是 **同时打开多个任务窗口** ，同时跑一样的代码（仅数据起始点不同），变相地实现并发回测Alpha。虽然也跑完了1000个回测，但实际中应该不能这么做。

1. **问题**

（1）由于“先导课”没有听，估计是自己遗漏了一些API的相关信息，比如每次登录时长限制4个小时、brain平台可同时进行10个simulation等。通过看其他同学的帖子，掌握了一些优化的方向。

（2）其他同学的回测的时长，有一个多小时的，也有两个多小时的。如果都是在同时提交10个simulation这种情况下，回测性能还与哪些因素相关呢？是Brain平台的忙闲吗？

（3）有个疑问：当前我们实现的内容，应该只是Alpha的回测，即使在1000次回测中发现了可以提交的Alpha，系统也不会自动给submit，应该还需要手动submit吧？

1. **改进方向**

（1）当前的代码效率太低，看到其他同学有用“多线程”的，对这块不是太懂，目前还在学习优化这部分程序中。

（2）模板数据类型：自己使用的模版是【Alpha灵感】A股换手率类因子，因为原表达式中有cap这个数据字段，所以是对cap进行替换。比较好的数据集应该是price volume data，但这个数据集中筛选出的cap数据太少，不到1000个。所以是在All categories中筛选的cap数据字段，这估计会影响Alpha的表现。此外，为了尽快完成作业，仅使用了matrix类型的数据，后续可以考虑使用vector数据。

（3）当前Alpha表达式的替换，仅实现了单个数据字段的替换，后续可以实现多个数据字段或者operator的替换，感觉这样应该更能够找到低correlation的Alpha。

（4）将回测结果保存为文件，便于后续再次使用。

---

### 评论 #45 (作者: WD77850, 时间: 2年前)

1 前后对比


> [!NOTE] [图片 OCR 识别内容]
> (9
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 18
> GOOD
> EXCELLENT
> Total Unsubmitted Alphas
> 1,563
> Total Active Alphas
> 35
> SPECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 1,598
> 20:54
> yd
> 3 〈'英  拼
> g) 匈
> 孕
> 2023/12/14



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> #
> 98
> GOOD
> EXCELLENT
> Total Unsubmitted Alphas
> 2,726
> Total Active Alphas
> 35
> SPECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 2,761
> 0:39
> yd
> W
> 〈  英  拼
> 4)
> 2023/12/15


2 证明连续提交 
> [!NOTE] [图片 OCR 识别内容]
> OP U
> OruOUu
> Simulation sent successfully。
> https : //api. worIdquantbrain. com/ simulations / 3mBZaubIXSeugkCe8SSZLII
> opt4_vola_365d
> Simulation
> sent slccessfillly.
> https: _
> api. WorIdquantbrain. com/ simulations
> IUTXPtSTI4NDONTOBTwX3Zh
> opt4_vola_5474
> Simulation
> sent successfully.
> https : //api. worIdquantbrain. com/ simulations /2wlOxaIQ4J193TTjxEKLF
> opt4_vola_GOd
> Simulation sent successfully。
> https : //api. worIdquantbrain. com/ simulations /Igicy2bdx4lNaKDBIOZZKab
> opt4_vola_730d
> 429
> Sleep
> Simulation sent successfully。
> https : //api. worIdquantbrain. com/ simulations /3EGU8Z3GO4ptgCpl7xeQogaR
> Opt4_vola_gld
> Simulation
> sent successfully.
> https: ^
> api. worIdquantbrain. com/ simulations / 24HngUyV4FlcgUNVJIGD7t


- 如图我修改了 get alpha的方法 并使用一个变量来计算alpha的数量 最后结果显示1000个 
> [!NOTE] [图片 OCR 识别内容]
> response
> 5.
> post
> https : //api. worIdquantbrain. com/authentication' )
> response. raise_for_status
> # Raises
> 8
> HTTPError
> if the Status
> is 4H,
> Sr
> break
> eXCeDt:
> Drint
> connection
> trying
> to Iogin again")
> sleep (10)
> Drint (response
> return
> 5
> 5
> sign_in0)
> def get_n_is_alphas (session;
> total_alphas;
> limit=l00)
> fetched_alphas
> []
> offset
> alphalilm
> mhile len (fetched_alphas)
> total_alphas:
> reSDOISe
> session。
> (f"https : //api. worIdquantbrain. Com
> USerS
> self/alphas?stage=IS&Limit= {1imit} &offset= {offset}
> alphas
> response.json ( ["results"]
> fetched_alphas. extend (alphas)
> alphalim
> +二
> len (alphas=
> # Count the total number of fetched alphas
> Offset
> 十二
> len (alphas)
> # Update offset by the number of fetched alphas
> i len (alphas)
> limit:
> break
> return fetched_alphas [ : total_alphas],
> alphalum
> IS_resllt, nlm
> _n_is_alphas ($, total_alphas=l000)
> Drint (num)
> print (IS_result )
> 〈Response
> [201]〉
> 1000
> dowI,
> get
> get

- 最后一个抓取的alpha也确实是该data set 内最后一个 
> [!NOTE] [图片 OCR 识别内容]
> DUID_IIINTOLIII
> delay
> 1,
> decay
> 10,
> neutralization
> INDUSTRI
> truncation
> 0.01,
> pasteurization
> ON
> unitHandl
> VERIF
> nanfandling'
> ON
> Ianguage'
> FASTEYPR'
> Visualization
> False}
> regular'
> code
> Vector_Ieut
> group_extra (implied_volatility_
> ?a11_1080-implied_volatility_put_1080,0_
> 5,industry) , close) *group_median ( (opt4_152_put_dis_delta50)
> (volume)
> industry)
> description'
> Non
> 3,
> operatorCount'
> 6},
> dateCreated'
> 2023-12-14108:26:28-05:00'
> dateSubmitted'
> None;
> datelodified'
> 2023-12-14108:26:29-05:00'
> 3e
> None
> favorite
> False
> Iidden
> False
> COIOr
> None
> Cateeorv
> None
> tags
> erade'
> None
> Staee
> IS'
> Status
> USUI
> ing


3 反思

我选择了【Alpha灵感】The option to stock volume ratio and future returns期权和股票成交量比率和未来回报率 作为alpha模板 并对其中opt4_secpr_volume这个字段进行替换优化。由于该数据字段于期权的价格数据有关， 所以我认为可以通过遍历一个期权价格的data set 来寻找最优数据字段。于是我选择了data set: Implied Volatility and Pricing for Equity options。 这个data set 里面的数据字段大部分与期权价格相关，数量正好有1196个。检查alpha的模拟结果，发现了Sharpe最优的数据字段 opt4_30_call_dis_delta55，这个数据表示的30天看涨期权的价差，用价差代替了原来的期权价格数据。我猜测是因为期权价差增大时同样指示了期权市场热度增大，投资者更加趋向于用期权对冲风险的现象，也符合O/S比原理的设定。该结果相较于之前选择的opt4_secpr_volume 有了较大的提升。关于代码效率的问题，我认为可以减少sleep的时间来提高。关于模板的后续改进方向，我认为可以通过加入止损条件，设置多个分组等方式进行优化。（抱歉因为最近一直在进行期末考试，没有足够的时间深入研究，下次会进行改善） 
> [!NOTE] [图片 OCR 识别内容]
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
> o IS
> Summary
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
> 2.78
> 20.349 2.61
> 17.879
> 5.639
> 17.579600
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
> 4.88
> 23.779
> 5.92
> 34.979
> 2.929
> 29.429600
> 1151
> 1185
> 2012
> 2.96
> 20.359
> 2.74
> 17.399
> 3.71%
> 17.109600
> 1161
> 1072
> 2013
> 1.77
> 19.989
> 1.17
> 8.739
> 4.459
> 8.749600
> 1285
> 963
> 2014
> 5.08
> 23.629
> 5.46
> 27.309
> 1.279
> 23.129600
> 1389
> 1107
> 2015
> 3.24
> 21.359
> 3.08
> 19.259
> 4.339
> 18.039600
> 1377
> 1163


---

### 评论 #46 (作者: WL13229, 时间: 2年前)

[WD77850](/hc/en-us/profiles/17370721245207-WD77850)

最后的Alpha没法提交吗

---

### 评论 #47 (作者: WD77850, 时间: 2年前)

本来想着比赛的时候再交的，结果刚才重新测prod correlation全变成0.9了,有人抢先交了hh

---

### 评论 #48 (作者: DZ54968, 时间: 2年前)

1、回测1000+Simulation截图


> [!NOTE] [图片 OCR 识别内容]
> OTL
> 4T
> H
> TMIARI
> IAInYTTTH/
> [ S
> AATLCIT
> ILJTL
> TPre
> B
> 
> QNws
> Ceah Cn [
> Ct
> Oten
> C JIIITH
> Alphas
> UnubMtteu
> SUbmiod
> NnhdLIyt
> Totl ?39
> C
> UnsUbI TeU
> ?3
> ArtI :
> Toct Cm
> Wic Crced  S
> He
> Unln
> ShC
> UCUT
> JUTMt
> DEaTTCsInad:
> UAASIIIUL
> TTTU
> TCM
> e
> ,(
> IIIIIITIn
> 1111221[T
> TCP
> I II
> SU|
> ICM
> __
> 41
> L
> UAUINUITTIO
> TT0L11+
> TC
> Gl
> USUUIITUC
> 14124014
> TCo7
> 111
> 152
> UAUAIIVU
> 120727 [T
> TCpI
> e
> u
> IIIIUIT
> 124121151
> TCpn
> 56114
> 2472
> NL
> Uuwltvo
> TLOLM1
> TC
> 15032
> R?L
> UAIAUIITIO
> T
> TC
> 
> UASUMITTU
> 1OAT
> TI00
> 4515
> 0574
> 49014
> T
> --1
> GTu



> [!NOTE] [图片 OCR 识别内容]
> LOIIIIrT
> Jolr
> OIYULIUITLITI!
> 3St
> MSRSUTL
> ILJTJ
> TIF TZSS
> 5
> C
> ( Nph
> Ta In /I
> G Fme
> Our
> { Erlpt AIrienl
> Alphas
> UITTHMICN
> SNHMIT
> 40411111
> Totl; 3,452
> T@ooa
> IIIIAIT
> ALLIL
> nOT
> Tlo CoanIFSTI
> Roer
> Uaet
> ShIF
> Rolutf
> Tm
> DtorlTtyoled
> VIAUATTUI
> |
> T
> 2
> TTIN
> 1213273 EST
> TOAm
> ITTTO[
> LUAUTIn
> TO
> 1
> IOJ
> LTIAUATUI
> 17
> Tr
> 9177
> 9
> LTLTII
> 1213203 EST
> TCIU
> ITTN[
> LlanIILO
> /O[
> T
> JTJ
> LVJAUATTI[
> 12173
>  
> TTO
> O
> LIUTTI
> Ju
> T
> UaU
> LUanIILO
> T44/4
> IU AC
> NI
> R
> LVJAUATTI[
> 1T137
> 19407
> T019
> 1


2、尝试保证code连续性代码截图


> [!NOTE] [图片 OCR 识别内容]
> STatUs
> Palse
> Nhile
> not
> SLatUs
> simulation_response
> post
> htps:
> Worldquantbrain. Com/simulations
> json-siulation_data)
> i simulation_response
> StatUs_
> Code
> 1二 201:
> print (f" Error
> {Sinu_ation_Lesponse. StatUs_Code
> Retrying
> in 20 seconds
> SLeep (20)
> 等待20秒后重试
> else:
> print (" Simulation
> Sent successfully
> Statts
> True
> 成功发送。跳出循环
> CrCCDt
> Lequests
> erceptions. RequestErception
> 捕获诗求异常。并在
> 定时间后亚试
> Drint
> Request failed:
> {2]
> retrying in 20 seconds
> sleep (20)
> LTy;
> /lapi


这个代码片段将会对每个id发送一个请求，并在请求失败时（例如由于服务器断开连接）等待20秒后重试。

3、总结反思

代码效率：（1）可以在使用machine前提前思考ALPHA表达式的逻辑对哪类数据比较敏感，提前思考可能会用到哪些datafeild；（2）使用多线程优化代码如下


> [!NOTE] [图片 OCR 识别内容]
> def process_simulation (data; session):
> tTy;
> Tesponse
> Session. post
> https
> /api
> Norldquantbrain  Con simulations
> Jsondata)
> LeSDOISe
> Status_
> C0d2
> 201 
> print ([
> Error {response
> statUs_Code
> else:
> Drint
> Simulation
> Sent slccessfully。
> except requests.exceptions. RequestException
> print ("Request failed;
> threads
> for
> i datafields_df['id']:
> Simulation_data
> tyne
> REGULIR'
> settings'
> InstrunentType
> EQUITI
> Legion
> USA'
> universe
> IOP3OOO
> delay
> decay
> neutralization
> SUBIIDUSTRI
> truncation
> pasteurization
> UII
> tHandling'
> TERIF'
> nanHandling
> OFF
> language
> FASTCIPR'
> risualization
> FalsC
> regular'
> f rank ({1})<5
> G?ranh
> {订)<1/6?-2score (abs (ts_delta (close
> 11:0;rank(CLose/
> thread
> threading. Thread (target-process_simulation;
> argS(simulation_data,
> 5) )
> threads.append (thread)
> Thread. starrt
> for
> thread In
> threads:
> thread. join0


模版适合的数据类型：理解我的表达式适合的数据类型需要在brain平台上多次手动尝试。例如other+number类型的数据有多种，最初表达式使用的数据集是oth41_s_tech_skewness，起初只尝试了other41中的datafield，后经过尝试方向model类数据集中也有适合的datafield。

模版的改进方向：基于Sharpe选出改进后的表达式，发现换手率有一定提高，可以进一步设置过滤条件降低换手率。


> [!NOTE] [图片 OCR 识别内容]
> 15N
> 12.5N
> 1ON
> 750OK
> OOOK
> 05/20/2013
> PnL: 4,540.0GK
> SOON
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.59
> 33.36%
> 1.87
> 17.47%
> 7.62%
> 10.479600


---

### 评论 #49 (作者: JT89676, 时间: 2年前)

1、提交结果


> [!NOTE] [图片 OCR 识别内容]
> 标签页
> 阁0
> 帮助
> &8
> 1004 [b
> 吕
> 12月198周二  18:51
> C 圉 &  9
> &
> Competitions (2]
> Events
> Learn
> Reler
> friend
> 品 ^
> {三
> Announcements
> See all
> Notifications
> SCCal
> Wost Recent
> Most Receni
> We analyzed youralphas
> here 15
> tiptallored tor
> Achievement Unlocked!
> JOU!
> AChevement Unlocked!
> Research paper 69
> Callauction continuous
> tradling and closing price formation
> Achevement Unlocked!
> [BRAIN TIPS] Sequencing Multiple Operators inan
> Achevement Unlocked!
> ExpressIOn
> Achevement Unlocked!
> Global Delay 1 Theme
> End OfACE 20231
> Q Alphas
> Seeall
> Achievements
> View Achevements
> Stalus
> 20
> 400
> GOOD
> 8v48U8IT
> Tota
> Unsubmitted Alphas
> 487
> Tota
> Actiye AIphas
> Total Decommissloned Alphas
> Total AIphas
> 501



> [!NOTE] [图片 OCR 识别内容]
> 标签页
> 囹0
> 助
> %:
> 100% 2王
> 12月198周二
> 20.41
> C p &
> 舀 Competitions (2)
> Events
> Learn
> Reler
> frend
> 虽 ^
> 8三
> Announcements
> SeCall
> Notifications
> SeCal
> MostRecent
> Most Recent
> We analyzed youralphas
> here 15
> tip tallored for
> Achleyement Unlockeo!
> yOUI
> Achleyement Unlockeo!
> Research paper 69
> Callauction  continuous
> tradlngand cosing price formation
> Achleyement Unlockeo!
> [BRAIN TIPS] Sequencing Multiple Operators in an
> Achleyement Unlockeo!
> CSSIon
> Achlevement Unlockeo!
> Global Delay-1 Theme
> End ofACE 2023!
> a Alphas
> Seeall
> Achievements
> Vew Acheyements
> Status
> 20
> 10日
> GOOD
> 8IeI
> Total Unsubmitted Alphas
> 1,747
> Total Active Alphas
> OTTt
> Total Decommissioned Alphas
> Total Alphas
> 1,761
> EDr


2、代码效率

simulation提交时由于网络拥堵可能暂时提交失败，可先sleep一段时间再进行重试，若采用单线程提交，那么sleep期间不能提交其他simulation，效率低下，因此可考虑多进程（multi-process）提交，由于此处为I/O密集型操作，不是CPU密集型操作，因此采用多线程（multi-thread）提交速度也不会差太多。（需要考虑电脑CPU的物理核心数）。


> [!NOTE] [图片 OCR 识别内容]
> data_fileds
> datafields_df ['id' ]
> to_list()
> periods
> [60,90,120
> 180]
> data_fileds_list
> list
> itertools. product (data
> fileds, periods)
> [1200:
> failed_list
> With
> Concurrent
> futures
> ProcessPoolExecutor (max_Workers=l00)
> 35
> executor:
> futures
> for
> item
> enumerate (data
> fileds_list
> futures
> append
> executor
> 5Ubmit
> run
> siulation,
> item )
> for
> future
> in concurrent.futures
> completed
> futures
> Fes
> future. result( )
> 讦
> res [1]
> False:
> failed_list
> append (res [0] )
> len (failed_list)
> 二二 0:
> print ("AII simulations
> Completed
> and sUCceed。
> else:
> print ("AlI
> 5imulatlons
> Completed
> and {}
> simulations failed。
> format
> len (failed_list)
> print (failed
> list ]



> [!NOTE] [图片 OCR 识别内容]
> 1136
> Simulation
> 1137
> sent successfully。
> 1137
> Simulation
> 1107
> sent successfully。
> 1138
> Simulation
> 1071
> sent successfully。
> 1139
> Simulation
> 1020 sent successfully。
> 1140
> Simulation
> 1119 sent successfully。
> 1141
> Simulation
> 1035
> sent successfully。
> 1142
> Simulation
> 1102
> sent successfully。
> 1143
> Simulation
> 1069 sent successfully。
> 1144
> Simulation
> 1041
> sent successfully。
> 1145
> Simulation
> 1093 sent successfully。
> 1146
> Simulation
> 1097
> sent successfully。
> 1147
> Simulation
> 1034 sent successfully。
> 1148
> Simulation
> 1062
> sent successfully。
> 1149
> Simulation
> 1046 sent successfully。
> 1150
> Simulation
> 1076 sent successfully。
> 1151
> Simulation
> 1091
> sent successfully。
> 1152
> Simulation
> 1087
> sent successfully。
> 1153
> Simulation
> 1070 sent successfully。
> 1154
> All simulations completed and
> 11
> siulations
> failed。
> 1155
> [211,
> 214,
> 221,
> 225,
> 222,
> 228,
> 231,235,
> 237,
> 239,
> 242]


3、debug经历：

某些simulation提交一直失败，重试次数太多会触发BRAIN平台/simulations接口的最大重试次数超出的错误，因此可以暂时保存提交失败的simulation。

4、模板：本次尝试的alpha为历史分位数因子，

```
ts_rank(mdl175_netprofitttm/mdl175_mktvalue, 180)
```

该因子考虑EP在过去一段历史区间中所处的分位数点，是常用的时间序列分析方法。我考虑使用数据集China Fundamentals and Technicals Model的字段进行替换，并使用[60, 90, 120, 180]的不同历史区间，分别为2、3、4、6个季度（实际按每个月的交易日来算更合理一些）。最后获取alpha的相关模拟信息，将'turnover', 'returns', 'drawdown', 'dateCreated' 等保存到csv中方便后续分析，其中valid字段根据alpha is阶段的各项check得到，若所有check均通过则check为True。


> [!NOTE] [图片 OCR 识别内容]
> import pandas
> a5
> pd
> df
> pd.DataFrame (columns= ['id''
> Code'
> pnl',
> bookSize'
> longCount'
> shortCount
> turnover'
> returns
> drawdown
> margin'
> fitness
> Sharpe
> datecreated
> 'valid'])
> for
> i
> item
> in enumerate(IS_result):
> alpha_info
> [item ['id' ],
> item [ 'regular' ] [ 'code'] ,
> item [ 'is' ] [ 'pnl'],
> item [
> is' ] [ 'bookSize' ] ,
> item [ 'is' ] ['longCount'] ,
> item [ 'is' ] ['shortCount'] ,
> item [
> is' ] ['turnover' ] ,
> item ['is'] ['returns' ],
> item [ 'is' ] [ 'drawdown'] ,
> item ['is' ] [ 'margin']
> item ['is' ] ['fitness'] ,
> item ['is' ] [ 'sharpe'],
> item [ 'dateCreated' ] ]
> check_info
> [i['name
> ]
> for
> 1
> in
> item [ 'is' ] [ 'checks']
> 讦
> i[ 'result' ]==
> FAIL']
> 讦
> len (check_info)
> 0:
> alpha_info.append (True)
> else:
> alpha_info.append ( False)
> df.loc [i]
> alpha_info
> df.to_CSV
> alphas_info.CSV
> index=False )



> [!NOTE] [图片 OCR 识别内容]
> Code
> pnl
> bookSize
> ongCount
> shortCount
> turnover
> EqNP2BR
> anklmdl175_workingcapital
> 559871
> 20OOOOOD
> 1346
> 1247
> 0.0343
> SOVx2jv
> ts_ranklmdl175_v0/10,901
> 24604054
> 20000000
> 1233
> 1405
> 0.1852
> nnm5x7q
> ts_rank(mdl175_xda, 1801
> 9235127
> 2000OOO0
> 1201
> 1205
> 0.2208
> OAxZawp
> ranklmol175_volumn3m: GC
> 21081266
> 200OOOO0
> 1298
> 1302
> 2954
> 乙gv17x
> ts_ranklmdl175_vosc 90)
> 16076653
> 20000000
> 1312
> 1327
> 0,2431
> rbgMnE
> ts_ranklmdl175_vol20, 180)
> 23713777
> 20OOOOO0
> 1231
> 1407
> 0.1107
> 5Lrd2pk
> ts_ranklmdl175
> xda, 60)
> 10547606
> 20000000
> 1198
> 1208
> 0,2456
> rbgMn2E
> ts_rank(mdl175_VrocG, 901
> 33551479
> 20OOOOO0
> 1314
> 1324
> 0.9218
> KeVpENg
> ranklmdl175_we2ofc, 60}
> 2013838
> 20000000
> 1341
> 1301
> 0.2163
> 998027e
> t_ranklmdl175_ve2at。 120)
> 13458280
> 2OOOOOOO
> 1425
> 1217
> 0.207
> jnokMZW
> Is_ranklrdl175_42a1。1801
> 11228378
> 200OOOO0
> 1425
> 1217
> 0.1737
> enNZWa0
> t rank(mdl175 ysp。 1201
> 22070985
> 20OOOOO0
> 1309
> 1329
> 0.4421
> dnYrPI2
> ls_ranklrdl 175_+0120
> 901
> 22926952
> 20000000
> 1229
> 1408
> 1348


---

### 评论 #50 (作者: HJ98329, 时间: 2年前)

参考之前文章 [[L2] 【Alpha灵感】从ICIR角度探讨风格因子的均值回复性_19524432578967.md]([L2] 【Alpha灵感】从ICIR角度探讨风格因子的均值回复性_19524432578967.md)  
的思路，决定仿照传统的因子筛选方法，即主要考虑ICIR值，来筛选出表现较佳的因子，提供的因子模板如下：

```
returns > -0.1 ? (ts_ir(ts_corr(ts_returns(vwap, 30), ts_delay(group_neutralize((data field), market), 30), 90), 90)) : -1
```

首先获取符合以下setting的数据集，而后再获取数据集下的所有字段，为简单起见，仅考虑数据类型为MATRIX的字段。


> [!NOTE] [图片 OCR 识别内容]
> i
> description
> dataset
> category
> subcategory
> region
> uniVerse
> Hpe
> CoVerage
> turnover
> UserCount
> alphaCount
> Book Value Per Share
> {'id': 'analyst14' 'name':
> analyst-analyst-
> anl14_actvalue_bvps_fyo
> analyst
> CHN
> 10P3000
> MATRIX
> 0.4375
> None
> 14
> 64
> recent last year
> Estimations of Ke。。
> estimates
> Capital Expenditures
> {'id': 'analyst14' 'name':
> analyst-analyst-
> anl14_actvalue_capex_fy0
> analyst
> CHN
> 10P3000
> MATRIX
> 0.3390
> None
> recent last year
> 'Estimations of Ke.。
> estimates
> Cash
> Per Share
> {'id': 'analyst14', 'name':
> analyst-analyst-
> anl14_actvalue_cfps_fy0
> analyst
> CHN
> TOP3000
> MATRIX
> 0.3282
> None
> 20
> recent last year
> 'Estimations of Ke.。
> estimates
> {'id': 'analyst14'; 'name':
> analyst-analyst-
> anl14_actvalue_div_fyo
> Dividend
> recent last year
> analyst
> CHN
> T0P3000
> MATRIX
> 0.2769
> None
> 26
> 'Estimations of Ke.
> estimates
> Eamings Before Interest &
> {'id': 'analyst14'; 'name':
> analyst-analyst-
> anl14_actvalue_ebit_fy0
> analyst
> CHN
> T0P3000
> MATRIX
> 0.3373
> None
> 18
> Taxes
> recent last
> 'Estimations of Ke.
> estimates
> {'id': 'pv96', 'name':
> 5521
>  pvg6_figi_map
> Figimap
> pv-price-volume
> CHN
> T0P3000
> MATRIX
> 1.0000
> None
> 'Corporate Action Datas.。.
> {'id': 'pvg6', 'name':
> 5522
> fmap
> Figimap
> pv-price-volume
> CHN
> T0P3000
> MATRIX
> 1.0000
> None
> 'Corporate Action Datas。
> {'id': 'pvg6'
> name':
> 5523
> pvg6_ticketmap
> Ticker Map
> PV
> pv-price-volume
> CHN
> TOP3000
> MATRIX
> 1.0000
> None
> 'Corporate Action Datas。
> {'id': 'socialmedia12' 'name':
> socialmedia-
> 5524
> 5c112_buzz
> relative sentiment volume
> socialmedia
> CHN
> T0P3000
> MATRIX
> 0.3872
> None
> 12
> 92
> 'Sentiment Dat。。。
> social-media
> {'id': 'socialmedia12' 'name':
> socialmedia-
> 5525
> SC/12_sentiment
> sentiment
> socialmedia
> CHN
> 10P3000
> MATRIX
> 0.3872
> None
> 23
> 'Sentiment Dat。。
> social-media
> delay
> Flow
> pvg6


利用得到的字段，插入到模板中，并结合setting，打包成包含simulation data的迭代器。

利用thread库，对循环进行（十）多线程处理的方式。由于此为IO密集型任务，理论上应该没有很大的速度差异。并且规避了在不借助其他库的情况下，multiprocessing库中的目标函数中不能包含复杂对象的问题。


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsuhmittel
> Total: 7,019
> Out
> Insuhmitted:
> 6,994
> Active:
> 25
> 3ct Columns
> Decommissionedl:
> b
> 英  瞬
> 2:34
> an0IJIh0Us
> Regular
> 星期二
> 2023/12/19
> anoIJI0Us
> Regular
> a卫0ITIII0U5
> Rerular



> [!NOTE] [图片 OCR 识别内容]
> has
> Unsuhmitted
> Suhmitt
> Total: 9,581
> Out
> Unsubmitteu:
> 9,558
> b
> Active:
> %
> lumns
> atUs
> 英  瞬
> Decommissioned:
> Clect
> 6.45
> 星期
> 4242
> UNSTB}
> 2023/12/19
> anoIJmous
> Regular
> UNSTB}



> [!NOTE] [图片 OCR 识别内容]
> KnvVrXl
> Mbdg3Kg
> Alpha
> ZjgXAjZ done simulating〉 Betting alpha details
> ZjgxAjz
> AIpha
> XeVIbRq done simulating〉 Betting alpha details
> XeVIbRq
> Alpha
> WN3YeSN done simulating,
> getting alpha details
> WN3YegN
> Alpha
>  GRZGrXL
> done simulating, Betting alpha details
> GRZGrXL
> Alpha
> nnmGPBE done simulating〉 Betting alpha details
> AIpha
> qn05011 done simulating〉 getting alpha details
> nnmGPBE
> qn05011
> Alpha
> QAXGr7G done simulating〉 Betting alpha details
> OAXGr7G
> Alpha
> SLrGgkX done simulating〉 getting alpha details
> SLrGgkX
> Alpha
> SLrGgez done simulating〉 Betting alpha details
> AIpha
> BmXrZdM done simulating〉 getting alpha details
> SLrGgez
> BmxrZdM
> Alpha
> rbg0e8] done simulating〉 Betting alpha details
> rbgoeg]
> Alpha
> 998GWZK done simulating〉 getting alpha details
> 998GW2K
> AIpha
> 9986W52 done simulating〉 getting alpha details
> 9986152
> Alpha
> ZSBAbx8 done simulating〉 Betting alpha details
> Alpha
> qnosoaj
> done simulating, Betting alpha details
> ZSBAbX8
> anosoai


由于此次是第一次运行程序，仅用了比较简略的方式捕获异常，未对异常进行处理。猜测正是由于这个原因，理论上应该得到5500个左右的回测结果，实际上，只有2500左右的alpha被上传到了brain。后续会继续细化异常处理模块，找出其中的原因，并储存下来以作参考。

总结与反思：

1. 如上，接下来继续完善异常处理模块，能够捕捉从很多个易出错的session.get()处出现的错误，从而知晓每个因子的运行情况；

2. 接下来继续完善结果查询代码，初步思路为，回测完成后，先按照回测时间判断是否为今日(最近)回测完的因子，并取出保存，再批量获取结果以及FAIL信息。对于表现较好的，再采取相关性检测；

3. 本帖回测此思路仅为示意，并不是一个很好的idea，没有结合任何主观的判断之类的东西。这方面还需日后在课上学习一下思路。

---

### 评论 #51 (作者: WL13229, 时间: 2年前)

@ [DZ54968](/hc/en-us/profiles/18130763917463-DZ54968)

请问您选择的模板是什么意思？很好奇

---

### 评论 #52 (作者: WL13229, 时间: 2年前)

[HJ98329](/hc/en-us/profiles/13955136965015-HJ98329)

这个模板似乎不错，请问最后效果如何？有没有一些比较有潜力的？

---

### 评论 #53 (作者: ZZ51944, 时间: 2年前)

补充：完成1000个alpha的截图：


> [!NOTE] [图片 OCR 识别内容]
> End OfACE 2023!
> Alphas
> See all
> Achievements
> Achievements
> Status
> 2田
> 48
> GOOD
> Total Unsubmitted Alphas
> 3,217
> Total Active Alphas
> 45
> BCELLENT
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 3,262
> WorldQu...
> Jupyter
> AlphaSu.
> 中法班签。
> 微信
> 009
> 0%C
> 中
> 掰
> View



> [!NOTE] [图片 OCR 识别内容]
> 运行
> C
> N
> 代码
> 759
> 3/4 -00:54<00:19,
> 19.705/1」
> 100%
> 4/4 _00:56<00:00,
> 14.00s /i]
> 999
> 79/80 -1:50:35<00:48,
> 48.80S/i]
> 0%
> 0/4 -00:00
> 〈?
> ?i/51
> 259
> 1/4 [00:54<02:44,
> 54.785/11
> 509
> 2/4 [00:55<00:45,
> 22.705/1]
> 759
> 3/4 -00:55<00:12,
> 12.Ggs/i]
> 100%
> 4/4 [01:45<00:00,
> 26.345/1]
> 100%
> 80/80 [1:52:22<00:00,
> 84.285/1」


问题1：切换网络位置总是会出现Remote Disconnected问题，怎么解决？

问题2：1000个总共跑了2个多小时，好像比其他人慢一些，可能的原因是什么？

---

### 评论 #54 (作者: HJ98329, 时间: 2年前)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)

刚刚又看了一眼表达式，发现写错了，应该是

```
returns > -0.1 ? (ts_ir(ts_corr(ts_returns(vwap, 1), ts_delay(group_neutralize((data field), market), 30), 90), 90)) : -1
```

由于我check results相关的代码还暂未完善，需要稍微改进一下。改进完成后会把结果发到这里的，谢谢

---

### 评论 #55 (作者: YH87923, 时间: 2年前)

很抱歉第一个任务并未完成，由于从来没有学习过任何的编程语言，所以以下呈现的编程均是由chat GPT写成，我真心希望能够尽快跟上大家的进度，请大家给予我一些学习的建议

1．任务截图

截图1：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Seeal
> Achievements
> VeACHeVemenL
> atus
> 201
> 400
> Otal Unsubmtedlphas
> 3,110
> TotalActlc Aphas
> GOOD
> TOtal Decommlssloned Alphas
> otalalpn3s
> 2236
> 夸 gj
> 1020117115
> 3.165


截图2：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> CU
> Achievements
> UC! !Chrpmrns
> SIIU
> 20
> M00
> TOJL UTSUUIIICUT
> 3.117
> olarp Mlnh7
> GOOD
> TugR
> Toal Nlphns
> 3.172
> 10311710


这次的任务中我的问题出现在step456，

- Step4: 使用代码获取该类型的所有数据集和大部分数据字段（datafield)
- Step5: 对数据进行初步处理（例如vector data需要先使用vector operator降维）
- Step6: 将数据字段插入模板，批量生成Alpha表达式。

具体截图如下：

Step4:


> [!NOTE] [图片 OCR 识别内容]
> get_datageta(5,3etting
> Fylh 
> Ae7
> TP626c1
> (aost recent
> last )
> SU
> ythonalpha
> ipynb $nt 11 Iin
> get_datasets (5,settings)
> CUers
> pythonlalpha_7.Ipynb   单兀C  工 Iine
> UrI
> hto Llocdqyantbpalq coyLdata-Sets?
> instrumntType(settines[ instrumentType ]) ion{settinp[ region ]gdlay{settinp[ delay ]Jauniversefsettines [ universe
> sesslon.Bet(urI)
> OataSets
> pd.OutaFrame(result Json()['results'])
> datasets_df[ 'instrumentType
> settinRs [ 'instruaentType ]
> 0ata5et5
> df[ region
> settIngs[ `region
> NoeError
> Tame
> pd' is
> detined
> Cel1
> TesUJt
> ROT


虽然能连续不断地输出alpha，但是并不能simulate，而且查询了发现都是同一个alpha_id


> [!NOTE] [图片 OCR 识别内容]
> Alpha 22 5imulation submitted
> Alpha  23
> 5UIULat101
> submitted
> Alpha 24 simulation submitted
> AIpha 25 simulation submitted
> AIpha
> 鄢Imulation Submitted
> AIpha 999 simulation submitted
> AIpha 1808 siulation submitted
> Total
> TOOIeI
> alpha simulations submitted
> OIII
> TINOO C
> COTOIACPt
> OPT
> TOteO UINCOeIUOUILOI


并且运行的时间也很长


> [!NOTE] [图片 OCR 识别内容]
> print(f"Total {num_sinulations} ulphn simulations submitted"
> 721m 302
> Python


Step6的代码：

尝试1：chat推荐的并行结构


> [!NOTE] [图片 OCR 识别内容]
> from time import sleep
> import multiprocessing
> def submit_alpha
> simulation(alpha )
> try:
> Code
> submit alpha
> 5imulation
> for
> Biven alpha
> Dummy
> code
> simulate alpha simulation
> sleep(l )
> Simulate
> the
> time
> taken
> for
> simulation
> print(f"alpha {alpha}
> simulation
> submitted"
> except Exception
> print (f"Error
> OCCUFred
> while
> submitting alpha simulation: {str(e)}")
> Submit
> 1888
> alpha simulations in parallel
> num_simulations
> 1888
> alpha_Iist
> [1+1
> for
> range (num_simulations
> i len(set(alpha_Iist) )
> != len(alpha_Iist):
> print("A1I alphas should be different
> else
> Poor
> multiprocessing . Pool (processessmultiprocessing
> CpU
> Count( )
> Use
> a11 available CPU
> Cores
> PooI .map
> submit_alpha_simulation,
> aIpha_Iist )
> pool
> CIose
> pool.join()
> print (f
> Total
> {num_simulations }
> alpha simulations
> submitted


尝试2：

Chat推荐的异步编程框架asyncio


> [!NOTE] [图片 OCR 识别内容]
> Submit lee8 alpha
> simulations
> and
> store
> alpha ids
> and count in
> 1ist
> num_simulations
> 1888
> alpha_Iist
> [1+1
> for i in
> range (num_simulations) ]
> alpha_id
> count Iist
> []
> i len(set
> alpha_list) )
> != len(alpha_Iist):
> print (
> AI1 alphas should be different
> eLse:
> async  def submit_simulations(alpha_Iist ):
> pesults
> asyncio.Bather (* [submit_alpha_simulation(alpha )
> for
> alpha
> in alpha_Iist])
> for
> alpha_id
> in pesults
> i alpha_id:
> Not None
> alpha_id
> count_Iist.append (
> alpha_id,
> alpha_Iist
> count (alpha
> id) )
> Run
> the simulations
> in batches
> Of 18
> batch_size
> 18
> batches
> [alpha
> Iist [i:itbatch_size ]
> for
> range(8,
> len(alpha_Iist),
> batch_size) ]
> Ioop
> asyncio.Bet_event_loop
> tasks
> [submit_simulations (batch )
> for
> batch in batches
> Ioop
> run_until
> complete(asyncio
> gather ( *tasks
> Ioop
> cIose()
> print (f"Total
> {num_simulations }
> alpha simulations
> submitted"
> print(alpha
> id_count_Iist
> await


Chat解释：代码的含义是通过使用异步编程框架asyncio来提高代码的效率和并发性能。首先，我们创建一个异步函数 submit_alpha_simulation 来模拟提交alpha simulation的过程，并使用 asyncio.sleep() 来模拟alpha simulation的耗时。然后，在主函数中使用异步函数 submit_alpha_simulation 来构建任务列表，并使用 asyncio.gather() 来同时运行多个任务。最后，我们通过分批次提交alpha simulations的方式来提高并发性能，并使用 alpha_id_count_list 列表来存储alpha_id和其运行次数。预计运行时间会明显缩短，取决于alpha simulation的耗时以及平台的响应速度。

请问有哪里可以改进吗，或者说对于python零基础的人来说，需要怎么询问chat GPT能够快速地达到改进代码效率，并且还能真正用进自己的想法。

2.学习到的内容:

（1）学会了存储alpha信息


> [!NOTE] [图片 OCR 识别内容]
> # Export alpha id and count to
> CSV file
> output_file
> 'alpha_id_counts.csV
> with open(output_file;
> W'; newline=") as file:
> writer
> CSV.writer(file)
> writerwriterow(['Alpha ID', 'Count'])
> writerwriterows(alpha_id_count_list)
> print(f" Alpha ID and count data exported to {output_file}")


（2）知道了这次中用到的代码的编程知识：

Python的HTTP请求库和处理响应的方法。
Python的数据结构和处理方法，例如列表、字典等，以及如何定义和传递参数。
Python操作数据，可以使用Pandas库进行数据处理和分析。
使用API进行数据获取，使用Pandas进行数据处理。
Python的数据处理库进行数据处理。
Python进行字符串处理，以及如何使用模板引擎来生成动态表达式。
Python的字符串处理和API调用，以及如何处理参数和设置。
Python的网络请求库，例如requests库，以及如何处理API的请求和响应。
如何解析JSON数据，以及如何提取所需信息。
Python的日志库进行日志记录。

3.Debug经历：

每一环节都有，没一个没有的。登录花了一天时间，Simulate成功第一个alpha花了两天时间，寻找批量生成的代码花了一天时间

在与大家有较大差距的情况下，希望能够跟上大家的脚步，也希望能够得到大家的指导与建议

---

### 评论 #56 (作者: WL13229, 时间: 2年前)

@ [ZZ51944](/hc/en-us/profiles/18187109975191-ZZ51944)

1. 不断尝试重连即可。最好不要用VPN

2. 不同人的Alpha长度、模板不同，计算时间自然是不同的

---

### 评论 #57 (作者: ML15895, 时间: 2年前)

1. 上周 
> [!NOTE] [图片 OCR 识别内容]
> 日期与时间
> Q 搜索
> Alphas
> See all
> Achievements
> View Achievements
> 日期与时间
> 时区
> Status
> 设置日期与时间:
> Apple (time.apple.com.)
> #
> 48
> GOOD
> BXCELLENT
> Total Unsubmitted Alphas
> 1,384
> 2023/12/14
> 下午
> 8.31.58
> Total Active Alphas
> 29
> 23年12月
> SPECTACULAR
> 二 三
> 四
> 五  六
> 12
> 11
> Total Decommissioned Alphas
> 2728
> 2930
> 1
> 10
> 2
> 4  5 6 7  8
> Total Alphas
> 1,413
> 11
> 12 13
> 14115
> 16
> 3
> 18
> 19 20
> 21
> 2223
> 8
> 午
> 4
> 7
> 5
> 25
> 26
> 27
> 28
> 29 30
> 16
> 12  3
> 4 ^5


2. 这周 
> [!NOTE] [图片 OCR 识别内容]
> 日期与时间
> 时区
> Alphas
> See all
> Achievements
> View Achievements
> 自动设置日期与时间:
> Apple (time.apple.com)
> Status
> 2023/12/19
> 上午11:35.40
> #
> 1R
> GOOD
> 2023年12月
> Total Unsubmitted Alphas
> 5,079
> 二三
> 四  五  六
> 12
> 11
> 26
> 27
> 28
> 29
> 30
> 1
> 10
> 2
> Total Active Alphas
> 29
> 3
> 4  5 6 7  8
> 3
> BXCELLENT
> SPECTACULAR
> 10
> 11
> 12
> 13
> 14
> 15
> 16
> Total Decommissioned Alphas
> 17
> 18
> 19120
> 21
> 22
> 23
> 午
> 5
> 24
> 25
> 26
> 27
> 28
> 29  30
> 6
> Total Alphas
> 5,108
> 31
> 1 2 3 45


3. 成功连续发送1000个alpha expression
 
> [!NOTE] [图片 OCR 识别内容]
> Start
> Sent
> simulation
> Simulation
> Sent
> successfully with
> datafield adv20,
> Total
> SUCCeSS
> Counts
> 1
> Simulation
> sent successfully With
> datafield
> Cap,
> Total
> SUCCeSS
> Counts
> 2
> Simulation
> sent successfully With
> datafield cLose,
> Total
> SUCCeSS
> Counts
> 3
> Simulation
> Sent
> successfully
> With
> datafield  country,
> Total
> SUCCeSS
> Counts
> 4
> Simulation
> Sent
> successfully with
> datafield
> dividend ,
> Total
> SUCCeSS
> Counts
> 5
> Simulation
> sent successfully With
> datafield exchanse,
> Total
> SUCCeSS
> Counts
> 6
> Simulation
> sent successfully With
> datafield high,
> Total
> SUCCeSS
> Counts
> 7
> Simulation
> sent successfully With
> datafield industry,
> Total
> SUCCeSS
> Counts
> 8
> Simulation
> sent successfully
> With datafield loW,
> Total
> SUCCeSS
> Counts
> 9
> Simulation
> sent successfully With
> datafield market
> Total
> SUCCeSS
> Counts
> 10
> Simulation
> Sent
> successfully with
> datafield open,
> Total
> SUCCeSS
> Counts
> 11
> Simulation
> sent successfully With
> datafield returns,
> Total
> SUCCeSS
> Counts
> 12
> Simulation
> sent successfully with
> datafield sector,
> Total
> SUCCeSS
> Counts
> 13
> Simulation
> Sent
> successfully
> With
> datafield sharesout
> Total
> SUCCeSS
> Counts
> 14
> Simulation
> Sent
> successfully with
> datafield split,
> Total
> SUCCeSS
> Counts
> 15
> Simulation
> sent successfully With
> datafield subindustry,
> Total
> SUCCeSS
> Counts
> 16
> Simulation
> sent successfully With
> datafield
> Volume
> Total
> SUCCeSS
> Counts
> 17
> Simulation
> sent successfully With datafield
> Total
> SUCCeSS
> Counts
> 18
> Simulation
> sent successfully
> With datafield mdl175_01am,
> Total
> SUCCeSS
> Counts
> 19
> Simulation
> sent successfully With
> datafield mdl175_Olame,
> Total
> SUCCeSS
> Counts
> 20
> Simulation
> Sent
> successfully with
> datafield mdl175_0lamev,
> Total
> SUCCeSS
> Counts
> 21
> Simulation
> sent successfully With
> datafield mdl175_OldtsV,
> Total
> SUCCeSS
> Counts
> 22
> Simulation
> sent successfully With
> datafield mdl175_0licc ,
> Total
> SUCCeSS
> Counts
> 23
> Simulation
> sent successfully With
> datafield mdl175_021a,
> Total
> SUCCeSS
> Counts
> 24
> Simulation
> sent successfully With
> datafield mdl175_021ame ,
> Total
> SUCCeSS
> Counts
> 25
> Simulation
> sent successfully With
> datafield mdl14_eq_idu_dl_0710f,
> Total
> SUCCeSS
> Counts
> 998
> Simulation
> sent successfully with
> datafield mdl14_eq_idu_dl_0810f
> Total
> SUCCeSS
> Counts
> 999
> Simulation
> sent successfully With
> datafield mdl14_eq_idu_dl_ogzof,
> Total
> SUCCeSS
> Counts
> 1000
> finish
> Sent
> 1000 simulation With
> 65.93
> mins
> VWap,


4. 总结反思，基本上根据 [BRAIN API可以实现的功能这个帖子]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md) 和之前workshop的经验成功运行并获取到Performance Comparison的结果。

- **代码效率** ：代码主要实现的功能是成功提交alpha expression，通过simulation_response.status_code是否等于201判断，如果不等于，等待之后再提交同一个alpha，避免字段被遗漏，等成功提交完之后过一段时间再统一获取alpha结果。后续会考虑添加检查每个alpha expression是否运行成功。个人感觉代码效率一般，运行时间较长。看大家评论可以用多线程或者并行，后续可以尝试加入。
- **debug经历** ：获取Performance Comparison是会遇到错误，多试几次之后错误消失，具体机制不是太了解，对Performance Comparison网站界面中，前后的结果以及红色绿色上升下降箭头部分的计算不是很清楚，希望李老师课上能够简单介绍一下。
- **模版适合的数据类型** ：使用了这个帖子中的模版
  ```
  ts_rank(rank(datafields), 20)
  ```
  开始选择了Global Fundamental Data，因为它的fieldCount在（CHN，delay=1，TOP3000）中有1054个字段，所以先试了这个，结果看到基本Sharpe和Returns都是负数，后来看描述发现这个数据库是基本上都是annual或者quarterly的数据，应该是使用该模版对年度数据不合适。后来使用alphaCount的数量对数据库排序，选择排名前五的数据库，Price Volume Data for Equity， China Fundamentals and Technicals Model， Company Fundamental Data for Equity， Analyst Revisions， Quant Model Data，回测结果发现model175（China Fundamentals and Technicals Model）和model26（ Analyst Revisions）中有部分关于基本面的字段能在该模版下获得大于2.07的Sharpe，所以正如李老师这个帖子所说，这个模版适用于基本面数据，后续还需要更加深入的分析。这一部分的分析主要通过观察网站的alphas list，但是这样效率低，后续希望能够写成代码，通过排序和获取字段描述实现自动化。
- **模版的改进方向** ：一些初步的想法：
  1. 通过对比两个数据库，analyst revisions能获取Sharpe>2.07的比例高，所以使用该模版之前，可考虑对数据字段做一些预处理。
  2. 通过调整ts_rank频率，扩大可用字段范围。
  3. 将这个模版变成一个signal，然后再利用其他operator处理这个signal。
  这些想法还有待进一步尝试，如果纯用代码方式，第二个是比较好修改，但是第一个和第三个想法没有那么直接，目前反而觉得从网站中打开一个simulation然后一点点试会更直接。后续希望自己的代码能够更加灵活的变动alpha，继续加油，向大家学习。

---

### 评论 #58 (作者: WL13229, 时间: 2年前)

[YH87923](/hc/en-us/profiles/16858167567639-YH87923)

可以看出，您的学习曲线还是非常陡峭的。了解了一些Python的知识。如果是Python零基础，建议看一些视频补一下Python知识→ **[Python零基础](https://www.bilibili.com/video/BV1uY411b75q?p=1&vd_source=d8812fb45dfb16ea5c50d5afa12af977)** 。

我们在明天的导航课会现场演示一个代码框架，可以参考。

---

### 评论 #59 (作者: WH24469, 时间: 2年前)

- ### 1000次提交前


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Achievements
>  SChictrnb
> CV
> 1201
> T00
> GOo0
> Toul Unuited Nphys
> 1004
> OLLACINC AA
> TOLlOtCommIssIonNIPh5
> TolalNChas
> 1,012
> 21e
> 
> 7


- ### 1000次提交后


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Achievements
> Me ACNICCICnts
> SaUs
> 20
> T00
> GOOD
> Total Unsubmited Nphas
> 2,517
> AINe NDH5
> Tptl Ornmmsslnner 4ln21
> Total Mphas
> 2,527
> ITI


- ### 已连续提交1000个alpha（这里我提交的不止1000个）


> [!NOTE] [图片 OCR 识别内容]
> Sinlition 1297
> CC
> sucCessfully:
> 115bpsice_RT_12_鬣COS
> Siulution 129
> r
> JcCsfully: 2l15_bpaaic_8_12__C0r
> Sinulition 129
> SENIt
> SUCCESsfully:
> 4125
> T 371C
> C_12_鬣
> LSTS
> 1TtO
> 130 fail: anl15_bpspics_RI_12
> este_山
> Siulation 130
> TTT
> successfll;
> 3115_bpsics_?r
> 12__Cs3_血
> Sinulitio 1301
> Set
> euccessfully:
> 3115_bpseics__12_鼻_ests_叩
> Sinulation 1302 fail: 2115_bpsgics_Rr_12_R_-0
> Sinlation 1302
> CCIT
> SUcccssfully:
> mlI5_bpszics
> Siulatiow 1303 se
> successfully: m115_bpseics_鼍_12_鼻s2
> Sinllation 1301 sent successfully; UlI5 bpszics_FI 12 p
> Siultio 1305 se
> ceesfully: 2115_bps-ies__12_7?T_der
> Sinlition 1305
> Cssfully: 2115bpsics
> RT 12
> Siulation 1507
> Gel?
> Suecessfully:
> 0115_bpscics_
> _12_』_tT_』esh
> Sinulation 130
> SCMC
> SUCCESSfully:
> 4115_bpsIcs
> C_18_鼻 }_chp
> Siultio 1593
> -
> successfuly:
> m115_hpscics_8_18_a_S_che
> Slulation 1310 fail: 5115_bpics
> 18_-_Gn_chs
> _12_w RrO
> totJl


- ### 反思

**代码效率** ：

在获取datasets和datafields时都是使用for循环，导致效率非常低，此时想到用多进程提高效率，但发现多进程的情况下找不到location，可能是由于网站不允许多进程。

**Debug经历** ：

首先是当要连续提交1000个alpha时，可能由于运行时间过长网站重启，或者过程断网了，导致出现如下error，过程中保证网络通常及限制simulation的数量就不会报错了。


> [!NOTE] [图片 OCR 识别内容]
> CpnnectionRrror
> LorctO
> oTtrn
> TineoutError (IONEO,
> 由于连接方在-段时间后没有正确答复或连接的主机没有反应。连接尝试失败。
> ION0;
> Vonei )


其次是获取数据字段的df时有时会获取到空的df，导致找不到‘id’这一列，添加一个判断df是否为空的条件，若df为空，则进行下一数据字段的获取，若df不为空，则正常运行，问题解决。


> [!NOTE] [图片 OCR 识别内容]
> ICrr[
> Trsceback
> LO +
> TRAn
> Cul1 ]4t1
> Rntcond3lliblyite pncknreslpand r
> {indere lb25e.
> T LoC
> (r1
> kiy
> nethod
> tolerance)
> ggog
> 3761
> TItUT
> Sclf
> TTTT
> Lloc (Csted_key)
> 3302
> UTCU (
> Rro
> 1anlcondaglliblsite
> DUCAUe3TDunUd
> libslindr。
> D203s.
> _lib. inder. Irderenpine.Ret_Joc ()
> TTCMM
> 4311iblyite packeesIpands{
> libs{inder.Pr
> puds。
> libe.inder. Irderenpine.ret_Joc 
> DMU
> libs{hithtable_
> CI
> helper  pi in pad.
> 1ibs. hshtable. PyobjectlsshTible.ret_ite()
> pandnrl_libslhrshtible_Clrr_helper  pri
> Dwdn
> 1ib.5ht1b1. PobjectishTabl.rt_()
> IITTTTMT :
> Ths Jb0v
> @xCCpTion
> dirct
> CJ1J
> follorinr exception:
> IITr
> TrJcbac
> IO+
> TCT
> Call 1Jst1
> {AppDrtalLocllTenp /ipykrnel
> 11696/3565420930.0
> -OOIT。
> 09213013 U
> l Tampe (len (datasete_idIist) )
> PInt (
> Ntnsets
> Lqtnsets
> i_list[dtnrets_nw]l berin
> I Ii (Jatatields d
> Oe1
> TI!
> J
> if 147
> 5
> 30OO
> SJULotou_dJ
> Ianacondaglliblsite-packapesIpandaslcore l[ra? D
> Retite 
> (ol[
> Ley
> 9+56
> i Selt
> COLTII  ACClt
> 9457
> 工eturn Sell
> Retiten_Rultilevel (key)
> 3158
> TTHeT
> Tl+
> CnITI
> nCIC
> 3459
> iterer
> STOTCT
> 940
> IUEXI
> 「Ioy
>  Ianucondagliblsite-paCkdles Ipandas lcorelinderislbuse:py
> RetIoc(salf;
> ky
> hothod
> IMTsII
> 9361
> TCtVTI
> Self。
> TTT
> loc (cstd_Ieyj
> 33o2
> UTLUI [
> eyLILO2
> 3363
> TNT
> KoError (key)
> ITOn
> 3304
> 9305
> 让 is_scalzr (key)
> {R」
> not Jlt
> IJATUU5 ;
> TCTTTNT:
> LCore
> Ret
> th
> 『



> [!NOTE] [图片 OCR 识别内容]
> Vhile si_n <=
> total
> Iama_si_nu:
> for
> datasets
> nu in range (len (datasets_id_list)):
> print (f" datasets {datasets_id_list [datasets_nu]} begin
> print (datafields_df} {datasets_nus})
> i len (datafields_df_1[datasets_num] )
> 
> 0:
> print (" #为空
> continue
> for
> in list (datafields_df_1[datasets_nu] [' i']. ralues)
> i si_n
> <二 start
> Iuu :
> Dass
> else
> simulation_data
> type
> RGUIL 岷'
> settines


最后是1000个alpha中有个很奇怪的alpha，前面很长一段时间都没有交易信号，有了交易信号后pnl跑的飞快：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> PIL
> TODOK
> OOOK
> OOOK
> LODOK
> 30OOK
> OOOK
> ODOK
> 11/2112012
> ISPnL; 0,00
> Jan '13
> Jan'14
> Jan'15
> Jan '17
> Jan'18
> Jan '19
> Jan '20
> Jan '21
> Jan'12
> J3115


适合的数据类型：

按目前回测的alpha来看，暂时还未发现适合的数据类型，但US市场的TOP3000是比TOP1000要好的。

改进方向：

现在运用的还是从第一个数据集的第一个数据字段开始从始至终逐一带入formula，所以效率较低，且需要人工记录进行到那个字段了，无法让程序自动记录并在下一次重新启动程序时继续后面的字段，所以这方面需要改进。其次是现在还只是修改了一个参数，未来可能需要进行更多种多样化的参数组合，所以还需要探索更加智能化、自动化的调参模块，实现真正的睡觉也能挖alpha，另外如果添加某些筛选阈值来记录比较优良的参数组合或formula并将其保存到一个文件中用于分析会更加易于观察alpha的特征。

---

### 评论 #60 (作者: SL57524, 时间: 2年前)

模版思路：

我选用这篇文章进行复现

1. [【Alpha灵感】股票收益是球队还是硬币？]([L2] 【Alpha灵感】股票收益是球队还是硬币_19137620283415.md)

基本思路和该Alpha灵感中相似，但略有不同

Moskowitz（2021）论述了当人们抛一枚硬币时，如果上次抛出

了正面，人们倾向于猜测下次会是反面，这是因为人们对抛硬

币这件活动本身比较了解，因此会以“反转”的眼光来看待“抛

硬币”；而当一个新赛季开始时，如果猜测哪只球队会夺冠，

由于人们对新赛季的球队成员和磨合等不是很了解，因此只能

以这些球队的历史成绩来考察它们，此时人们会猜测上赛季的

冠军，依旧将在本赛季夺冠，即人们会以“动量”的眼光来判

断“谁会夺冠”。

然而上述理论应用于股票时，却总是事与愿违。由于投资者对

动量和反转的预期，会导致其在提前采取行动时反应过度，从

而使预期发生“动量”的股票实际可能发生反转，预期发生

“反转”的股票实际可能发生动量。我们据此逻辑构造了“球

队硬币”因子。

#具体而言，我们认为波动率和换手率的变化量可以代表一支股票表现的“可知性”，即更像硬币还是更像球队。

#每月月底计算最近 20 天的日间收益率的标准差，作为当月的日间波动率,比较每只股票的日间波动率与市场截面均值的大小关系，将日间波动率小于市场均值的股票，视为“硬币”型股票

bodong = ts_std_dev(returns,20);

bodong_market = group_mean (bodong,1,market);

#计算每支股票 t 日换手率与 t-1 日换手率的差值，作为 t 日换手率的变化量。

#将每只股票的换手率变化量与当日全市场的换手率变化量的均值做比较，我们认为换手率变化量高于市场均值的股票为“球队”型股票，其未来将大概率发生反转效应；换手率变化量低于市场均值的，为“硬币”股票，未来将大概率发生动量效应。

huanshou = ts_delta(volume/ sharesout,1);

huanshou_market = group_mean (huanshou,1,market);

#找一个原本被认为是reverse的因子，然后对个股分别用这两种判断是否为“硬币”的方式进行判断，如果是硬币，未来发生动量效应的概率更大，把这些股票的Reverse因子前面加负号，对于球队类型的股票，这些因子不做处理。

但在本次作业中，为了简化，下文表达式中的name就是我想要寻找1000次的某个数据集，这个数据集应当是一个原本被认为是reverse的因子，此处仅用波动率作为判别是否是“硬币”的标准（相比研报简化）：

bodong = ts_std_dev(returns,20);bodong_market = group_mean (bodong,1,market);factor = ts_mean({},20);- if_else((bodong < bodong_market), -factor, factor)'.format(name)

【此处有待探究：如果根据原文，用两种判别硬币的方法结合起来可以达到更好效果】

紧接着我选取数据字段（即适用于作为某个反转因子的数据字段，此处可以再严格加以限制，通过预先的simulation以一定标准筛选出有作为反转因子潜力的数据字段：


> [!NOTE] [图片 OCR 识别内容]
> def get_datafields (5):
> urt_template
> https: //api.worldquantbrain com/data-fields7
> TV6InstrumentTyDC{
> EOUIT }
> fregion{'CHN' }Gdelay-{str(ll}cuniverse-{"70P3000'IGtype-{'MATRIY }Glinit-5O
> VLOTTSet{}
> count
> 5,get(uri_teplate.format (x-0)).json()
> COUnt
> datafields_list
> for
> range(0
> Count
> 501;
> dataflelds
> (url_tenplate.format (xsxJ )
> datafields_list.append (datafields.Json() [ 'resutts '1)
> dataflelds_11s1_Tlat
> [Item
> SUD1ISt
> in dataflelds_list Ior IC in 5UbLIsU1
> gataflelds_dt
> pd.DataFrame (datatlelds_lIst_Tat)
> TOATI
> datatields_df
> 4ata
> qet_datatields (5)
> Uuta  descrhel
> delny
> Coverage
> UserCoun
> alphaCount
> COUII
> 5855,0
> 5855 OOOOOO
> 5855 00OOOO
> 5855000000
> I0Ah
> 0,.827561
> 4,745346
> 24,736123
> 0,218018
> 52,026197
> 305285877
> 0.250800
> 00000O0
> 000OOOO
> 255
> 0,587850
> 0000000
> 0000000
> 50%
> 0.961800
> 000OOO0
> 00OOOOO
> 759
> 10ODOOO
> 2000000
> BOOOOOO
> ITa
> 10OOOO0
> 1966.000000
> 13979000000
> 「
> name
> 0ata.iTOC
> 10001
> 101:
> Erpression
> DOJONg
> Ts_std_deylreturns, 201;hodong_marker
> Oroup
> Tean
> (bodong.1,arket);Tactor
> ts_reanl(},
> 5imulation_Oata
> type
> REGULLR
> Settlngs
> InstrumentType
> EOUITY'
> region
> Cr
> Universe
> TOPJOO0
> detay"
> deci
> neutra117ation
> SUBINOUSTRY'
> +runcation
> 035TPUTT73100
> unitHandling
> TVERIFY
> nanhandTing
> OFF
> 'lanquaqe
> FASTEXPR
> 'Visualization
> False
> requtar
> Expressipnl
> Slmulatlon_response
> post('https: //ap1.wortdquantbramn
> Com/slmulatlons
> J501-51utatlon_data )
> simulation_progress_urt
> 5Iutation_response
> headers
> Locatlon
> finshed
> False
> uhile True
> SImutatyon_progre55
> get(simutation_progress_urll
> SIutation_progress headers qet("Retry-Atter
> OTCOK
> TeeptttoutlsIutation_proqress
> heudes (Retry-ATter1II
> print(tIC.strTtIC
> AY:id-AH:uM:45"
> LIN
> localtIme() )
> {1次纺柬
> DCt
> TOTgt(Il
> 2023:12:19-23:05:52 ]次结裒, Neu
> 2023:12:19-23:06:24  2天.裹
> 2023;12;19-23:06:573囊;neut
> 2023:12:19-23:07:20 +天诘裹
> 2023;12;19-23.07:475]
> 0
> 2023:12:19-23:0:13 6结衷, next
> 2023:12:19-23:8:50  7灰结
> 00[
> 2023:12:19-23:09:24 8结衷
> 2023:12:19-23:10:01 9次结衷, nl
> 2023:12:19-23:10:33 10次贳衷, Next
> 2023:12:19-23:10:57 11次#索
> DC [
> 2023:12:19-23:11:23  12灰r衷
> 2023:12:19-23:12:84 ]3次结索, nett
> 2023:12:19-23:12:35 14灰衷
> Tm+
> 2023:12:19-23:13:133 ]5次束
> TeXt
> 2023:12:19-23:13:45 ]6次:束
> 7077,17,1077+14+00
> 7521
> geti
> TIn
> 101
> reyl
> neyl
> ne
> neul
> Terl


然后在最简单的情况下进行1000次实验，可以看出，和评论区其他同学进行的相似，10次完成的simulation大概需要5分钟，那么1000次要超过500分钟才能完成（此处我没有继续进行1000次）：

针对于中断连接问题，我是选择在检测到异常状态之后重新登陆。我自己实验的过程中仅出现一次status 为400的情况。但根据评论区同学描述，可能还存在其他异常状态，此处可能并不完善。

针对多线程的问题，由于我之前没有学过相关内容，因此尝试复现评论区
DZ54968同学的观点，学习了thread的应用


> [!NOTE] [图片 OCR 识别内容]
> def Simulation (Expression
> Se55Ion )
> try
> response
> SesSIon.post('https: /7api
> Worldquantbrain.com/simulations
> J5on-Expression )
> response,status_code!=
> 201:
> Drint
> {response
> Status
> Code}
> leep(10)
> requests,Sesslon()
> auth
> (Username
> password )
> 「esponse
> post('https: //api
> Worldquantbrain  comyauthentication
> print (response)
> else:
> Drint
> GOOO,NCKt"
> 5Imulation_progress_Url
> 5imulation
> responseheaders
> Location
> finished
> False
> While
> True
> 5imulation
> Drogress
> get(simulation
> progress_Url)
> 1f simulation_progress
> headers.get
> Retry-Afterw
> break
> sleep(float (simulation_progres5 , headers ["Retry-After]) 
> print ("simulation
> Done
> nextw
> except requests,exceptions
> RequestEKCeption
> print(f'{e}
> thread
> Thread (target
> Simulation
> args=(Expression, 5))
> threads.append (thread )
> thread.start ( )
> for thread in threads
> thread.join( )
> /'LU(5
> Syyr
> 2023:12:19-22:36  弄990个
> 2023;12:19-22:55
> .991个
> 2023;12:19-22:36
> 第992个
> 2023:12:19-22:56  笫993个
> 2023:12:19-22:56  萧994个
> 2023;12:19-22:55
> 苇995个
> 2023+12:19-22.5639961
> 2023;12:19-22.56
> 莆9971
> 2023;12:19-22:56
> 59981
> 2023;12:19-22:56
> 苇999个
> 2023.12:19-22.56
> 410001
> 4p0
> 4o0
> 490
> 4N0
> 490
> 400
> 100
> 400
> 400
> 400
> HTTPSConnectionPoollhost='aptworldquantbrain
> D0rt-4431; Nax retrles Ccecded ith Url;
> /5Imulattons
> [Caused by
> OL「TOT
> (SSLEOFETror(8。
> [SSL: WEXPECTED_EOF_NHILE_READING]
> EOF
> OCCUTTed
> Viotation 0f DrOTOCOL
> (_551.C:10861'11
> 400
> HTTPSConnectionpool(hosT'aDI.orldquantbrain.cOm
> D0rt-4431: Nax retries eCeeOEJ UIh Ur:
> /sinulations
> (Caused Dy
> SLEFrOT(SSLEOFETroT(B
> [SSL; WEXPECTED_EOF_NHILE_READTNG]
> EOF
> OCCUrred
> Viotation Of protocol
> [_55L.C;10861')1


但出现一系列问题，目前尚在思考

---

### 评论 #61 (作者: AZ81686, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> resultl_option
> C
> result (expression_list_option*l0oo,
> neutralization="SUBINDUSTRYII
> universe='T0P3000
> decay=lo)
> #
> to_result_param (resultl_option)
> 22m 45.0s
> 100%
> 100/100
> [22:06<00:00,
> 13.275/i]
> resultl_option [999]
> 0.0S
> {'alpha_id
> :
> dnpRGSK'
> 'simulate_data': {'type':
> REGULAR
> settings
> :
> {'instrumentType':
> EQUITY' ,
> region
> 
> 'USA'
> universe' :
> T0P3000
> delay' :
> 1,
> decay
> :
> 10,
> neutralization' :
> SUBINDUSTRY'
> truncation' :
> 0.05,
> t0_
  
> [!NOTE] [图片 OCR 识别内容]
> Tab
> Window
> Help
> 99+
> 拼
> Tue Dec 19 9:3
> Gz
> A
> AIN
> Homepage
> Chair。。
> CSDN- 个人空间
>  PRL
> github-nonabelian..
> Jupyter笔记本查看器
> Insider Monkey
> Announcements
> See all
> Notifications
> See all
> Most Recent
> Most Recent
> We analyzed your alphas
> here is a tip tailored for
> Achievement Unlocked!
> YOU!
> ACE Basics: Group Training Webinar 1
> 7 Sep 2023
> Research paper 69
> Callauction, continuous
> trading and closing price formation
> SuperAlphas: Selection and Combo techniques
> [BRAIN TIPS] Sequencing Multiple Operators in an
> ACE Series Part 2:
> Building Versatile Frameworks
> Expression
> 2023 Aug 24th
> Global Delay-1 Theme
> ACE Series Part 1: Introduction to ACE 2023
> 17th
> End OfACE 2023!
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 18
> {
> GOOD
> Total Unsubmitted Alphas
> 27,119
> 们
> Aug
  
> [!NOTE] [图片 OCR 识别内容]
> rOfiles
> Tab
> Window
> Help
> 99+
> A
> Tue Dec 19 13:04
> Go
> uant BRAIN
> Homepage
> Chair。
> CSDN- 个人空间
> )
> PRL
> github-nonabelian_
> Jupyter笔记本查看器
> Insider Monkey
> Data
> Competitions (2)
> Events
> Learn
> Refer a friend
> A1
> Announcements
> See all
> Notifications
> See all
> Most Recent
> Most Recent
> We analyzed your alphas
> here is a tip tailored for
> Achievement Unlocked!
> ACE Basics: Group Training Webinar 1
> 7
> 2023
> Research paper 69
> Callauction, continuous
> trading and closing price formation
> SuperAlphas: Selection and Combo techniques
> [BRAIN TIPS] Sequencing Multiple Operators in an
> ACE Series Part 2: Building Versatile Frameworks
> Expression
> 2023 AUg 24th
> Global Delay-1 Theme
> ACE Series Part 1: Introduction to ACE 2023
> 17th
> End OfACE 2023!
> Alphas
> See all
> Achievements
> View Achievements
> 0
> Status
> 18
> [0
> GOOD
> Total Unsubmitted Alphas
> 27,119
> 4Q
> YOU!
> Sep
> Aug


总结反思:

代码功能：代码特点是将ACE help func和“BRAIN API可以实现的功能”融合，实现多线程回测和connection aborted问题解决；楼上有同学提到多线程问题，其实实测BRAIN最多可以同时simulate 50个regular alphas，不仅是10个

改进方向：断点续跑的解决方案(那其实就还涉及本地数据的管理)，alpha expression错误及其他问题的自动化handle

思考：在什么样的场景下才需要用到像这样一次性1000次simulate的功能，楼上同学好像是用简单的模版搜dataset，猜可能是来评估datafield的效用；那如果是要来优化已有的逻辑往深了做呢？如果只是改参数，似乎有"overfit"的嫌疑；如果是搜operators，那是不是就意味着需要对operators进行分组，（就像是在同一个dataset中搜相似含义的datafields) 在相似作用的operator group中搜operators；上面考虑的是operator的替换，那operator之间的嵌套逻辑应该怎么样? 还没想清楚

ps: 可以看到在代码通过[expression] * 1000生成1千个相同的表达式进行simulate后，IS alpha数没变，检查后发现系统其实会检测simulate的alpha是否和已有alpha的内容相同，如果相同就不会重新sim和创建新alpha id，而是返回旧结果（及id）

---

### 评论 #62 (作者: DZ54968, 时间: 2年前)

@ [WL13229](/hc/en-us/profiles/12285040305687-WL13229)

抱歉评论里的模版截图是另一个正在做的alpha表达式中。关于本次case中使用的alpha模版是关于市场偏斜度的group_neutralize(rank(-mdl175_revs10)+rank(-vec_avg(oth41_s_tech_skewness)), bucket(rank(cap), range='0.5, 1, 0.1'))。通过查询相关datafield更换mdl175_revs10和oth41_s_tech_skewness两类数据，寻找最优组合

---

### 评论 #63 (作者: WL13229, 时间: 2年前)

[DZ54968](/hc/en-us/profiles/18130763917463-DZ54968)

谢谢您的回答，nice!

---

### 评论 #64 (作者: WL13229, 时间: 2年前)

@ [WH24469](/hc/en-us/profiles/13991511763607-WH24469)   [SL57524](/hc/en-us/profiles/18074114880791-SL57524)

希望今天第二期导航课上，其他同学的分享能对各位的研究有所启发。我们周四还有Office Hour，即面向所有顾问的答疑时间，欢迎大家来。

---

### 评论 #65 (作者: YL37225, 时间: 2年前)

1.simulation超过1000次


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 1@
> GOOD
> BXCELLEMT
> Total Unsubmitted Alphas
> 1,350
> Total Active Alphas
> 11
> SECTACUAA
> Total Decommissioned Alphas
> Total Alphas
> 1,361
> 16:18
> @
> 4)
> 凹
> Ployar
> 2024/1/3
 2.连续提交simulation
 
> [!NOTE] [图片 OCR 识别内容]
> Cnt=cnttl
> print
> ("成功提交了:
> cnt, "次。
> ")
> time.sleep(6)
> 请注意。如果您有大量的aIpha表达式。  您可能想要添加
> 些逻辑来避免发送太多的请求
> 或者适当地处理API的速率限制。
> #Run AIpha
> code
> print ("running"
> except:
> print ( 'connection
> down
> sign_in()
> [61]
> 113m 50.6s
> 〈Response [201]〉
> Simulation
> submitted  successfully
> 成功提交了:
> 1  次。
> Simulation
> submitted successfully
> 成功提交了:
> 2  次。
> Simulation
> submitted  successfully
> 成功提交了:
> 3  次。
> Simulation
> submitted successfully_
> 成功提交了:
> 4  次。
> Simulation submitted successfully
> 成功提交了:
> 5  次。
> Simulation
> submitted successfully_
> 成功提交了:
> 6  次。
> Simulation
> submitted successfully
> 成功提交了:
> 7  次。
> Simulation
> sUbmitted
> sUCCessfully
> 成功提交了:
> 8  次。
> Simulation
> submitted  successfully
> 成功提交了:
> 9  次。
> Simulation
> submitted successfully_
> 成功提交了:
> Io 次。
> Simulation
> submitted  successfully
> 成功提交了:
> 11  次。
> Simulation
> submitted successfully_
> 成功提交了:
> 12
> 次。
> Simulation
> submitted successfully
> 成功提交了:
> 1851
> 次。
> Simulation
> submitted  successfully
> 成功提交了:
> 1852
> 次:
> Output is truncated. View as 0 Scrollableelement or open in a text editor Adjust cell output Settings -
 3.总结反思
·设置sleep似乎并不会比并行计算慢太多，自己不太擅长编程，就使用了较为简单的time.sleep(6)，不过参数的设置是经过了几次尝试得到的，更换成其他alpha或者修改simulation的设置可能会需要修改参数。

·获取到的数据字段比想象中多许多，未来完成作业我只对其中一部分进行了分析，之后可以尝试对得到的数据字段设置更加精细的筛选。
·为了解决超时登出问题所使用的while ture函数似乎导致所有的simulation模拟完之后又重新模拟第一个，这个问题我还正在解决。

---

### 评论 #66 (作者: XZ75239, 时间: 2年前)

提交作业，参考【Alpha灵感】分析师的真知灼见。考虑刻画出未提前反应在股价中的分析师信息，使用

dataset_id为"analyst14"的数据集，有数据的股票不多，大约是一个比较受分析师关注的股票池。。。

表达式粗糙地尝试了四种：

"rank(abs(ts_delta("+x+",250))/ts_delta(close,250))-0.5"

"rank(-ts_delta(close,250)/abs(ts_delta("+x+",250)))-0.5"

"rank(regression_neut(ts_delta("+x+",250),ts_delta(close,250)))-0.5"

"rank(-regression_neut(ts_delta(close,250),ts_delta("+x+",250)))-0.5"

1、截图1


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> Vew AChievements
> StatUs
> 20
> 4
> 10
> GOOD
> Total Unsubmitted Alphas
> 2,727
> Total Actie Alphas
> 65
> 83
> UCCI
> Total Decommissioned Alphas
> Total Alphas
> 2,792
> 21:20
> k
> @ @ 4j 中
> 曷
> 2024/1/23


2、截图2


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> Vew AChievements
> Status
> ?
> #0
> 1
> GOOD
> Total Unsubmitted Alphas
> 4,652
> Total Actie Alphas
> 65
> SiaENI
> UICCA
> Total Decommissioned Alphas
> Total Alphas
> 4,717
> 18;49
> @
> 0 4j 中
> 2024/1/25


3、代码截图


> [!NOTE] [图片 OCR 识别内容]
> SUCCES5
> num=g
> jo
> for ix in ids[:]:
> print("当前测试:  第" +str (j+1)+"个基本面指标
> for
> in range(4):
> print("第" +str (1+1)+"种表达式"一
> simulation_data
> simulation_data(i,idx)
> try
> simulation_
> pesponse
> post('hHs:Lei
> WOT
> Idquantbrain . comlsimulations
> json=simulation_data)
> exceot:
> S=sign_i()
> simulation_response
> 5
> post ('hLPs:LLapi
> WO
> Idquantbrain . com/simulations
> json-sZmu_azion_data)
> if simulation_response. staTUS_COGe ! -201:
> print ("mistake !
> S=sign_in()
> simulation_response
> post (
> htDS: /japi
> Wor_dquantbrain . com/simulations
> json-sImu_azion_data)
> continue
> simulatior_progress_ur]
> simulation_response . headers [
> Location
> ]
> Tinished
> False
> Waittime=0
> While True:
> simulation_progress
> 5.get(s-mu_ation_progress_url〉
> if simulation_progress .headers
> Retry-After
> Or Waittime>=60:
> break
> sleep(5)
> Iyaittimet-5
> try:
> alpha_id
> simulation_progress.json( ) ["alpha" ]
> a-pha
> ("https:/Lapi.worldquantbrain . comlalphas /
> alpha_id)
> print(alpha.json()["is" ]["sharpe"])
> SUCCeSs
> ILII+=1
> print ("当前成功测试a1pha总数]
> "+str (sUCCeSS_num) )
> eXCeDC:
> Continue
> 1+-1
> 47211535
> 第1种表达式
> 0.24
> 当前成功测试a2pha总类目
> 999
> 第2种表达式
> -8.9
> 当前成功测试apha总"目
> 1983
> 第3种表达式
> 03
> get
> get
> get


代码能力比较弱，遇到中断只好多次使用try和except，有惊无险无间断地跑完了1000次。。。

考虑改进：1、学习多线程争取跑快点；2、找到还行的夏普比后，也许可以在某个范围内调整参数和表达式直到结果更好。

小白第一次批量跑因子，感到很新奇。。感谢平台的慷慨授课，期待后续的课程~

---

### 评论 #67 (作者: QC95604, 时间: 2年前)

作业提交：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 1
> GOOD
> BCELLENT
> Total Unsubmitted Alphas
> 1,858
> Total Active Alphas
> 11
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 1,869
> 11:05
> 思 d 英  豳
> 2024/1/24



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 2田
> 48
> GOOD
> BCELLENT
> Total Unsubmitted Alphas
> 2,932
> Total Active Alphas
> 11
> SFECTACULAR
> Total Decommissioned Alphas
> Total Alphas
> 2,943
> 19:08
> 思 d 中  豳
> 2024/1/25


总结：

初次尝试使用API，确实比网页版的高效。多进程方式无法使用，但可以使用多线程，多线程的方式比for快5~6倍。

代码参考： **[BRAIN API可以实现的功能 – WorldQuant BRAIN]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md)**

**模板参考：** Research Paper 68: An Augmented q-Factor Model with Expected Growth

代码实现过程中遇到一些问题：

1、 
> [!NOTE] [图片 OCR 识别内容]
> 8%1
> 0/1050 [80:00〈?,
> ?i/s]
> 38%
> 396/1858 [18:15<38:
> 2.77s/i]
> JSONDecodeError
> Traceback (most recent
> call Iast)
> File
> LeqyestsImodels_RyigzI,
> in Response.json(self, **kwargs)
> 979 try:
> 971
> return complexjson.loads(self.text, **kwargs)
> 972 except
> JSONDecodeError as
> e:
> 973
> # Catch
> JSON-related
> errors and raise as requests.JSONDecodeError
> 974
> This
> aliases json.JSONDecodeError and simplejson.JSONDecodeError
> File
> 迦让
> Ryi525,
> in Ioads(s, encoding〉
> object_hook,
> parse_float,
> parse_int,
> parse_constant, object_pairs_hook,
> Use
> decimal, **Kw)
> 52
> i (cls
> is
> None and encoding is None and object_hook
> is
> None
> and
> 522
> parse_int is
> None
> and
> parse_float
> is None and
> 523
> parse_constant is None
> and object_pairs_hook is
> None
> 524
> and
> not
> use_decimal
> and not kw)
> 525
> return
> default_decoder . decode(s)
> 526 i cIs
> is None:
> File
> C
> Simplejsomldecoder Ry:37e
> in JsoNDecoder. decode(self,
> S」
> W
> PY3)
> 369
> str(s, self.encoding)
> 379 obj,
> end
> self.raw_decode(s)
> 371 end
> _W(s, end).end()
> File
> Simplejsonldecoder Ryi4ee_
> in JsoNDecoder. raw_decode(self,
> s, idx,
> W, _PY3)
> 399
> idx
> 十二  3
> 4ee return self
> scan_once(s,
> idx=_W(s, idx).end())
> 973
> # Catch
> JSON-related
> errors and raise
> a5
> requests.JSONDecodeError
> 974
> # This
> aliases json.JSONDecodeError and simplejson.JSONDecodeError
> 975
> raise RequestsJSONDecodeError(e.msg,
> e.
> doc,
> e. pos )
> JSONDecodeError
> Expecting Value
> line
> CoIumn
> 1 (char 8)
> Output is truncated View as a scrollable element or open in a text editor Adjust cell output Settings:
> 09,
> CIs,


解决方案：加入 try 和 except

2、 
> [!NOTE] [图片 OCR 识别内容]
> 8%1
> 8/1858 [80:80〈?, ?i/s]
> 32%
> 334/1050 [13:38<29:15,
> 2.45s/i]
> RemoteDisconnected
> Traceback
> (most recent call Iast)
> File
> connectionpool py:7ez
> in HTTPConnectionPool.urlopen(self, method,
> url, body, headers, retries, redirect,
> assert
> Same
> host, timeout, pool_timeout, release
> conn, chunked, body
> PO5]
> 702
> Make the request
> on the httplib connection object
> 77 httplib_response
> self。_make_request(
> 704
> conn,
> Ze5
> method,
> 7e6
> url,
> 797
> timeout=timeout_obj,
> 7e8
> body=body,
> 7e9
> headers=headers
> 710
> chunked=chunked,
> 711
> 713
> # If We're going to release the connection in
> finally:
> then
> 74
> the response doesn
> t need to know about the connection。 Otherwise
> 715
> # it Will
> aIso
> to release i and We'11
> have
> a double-release
> 76
> mess
> File
> C:
> connectionpool.Ryi44g
> in HTTPConnectionPool
> make_request(self,
> conn, method, urI, timeout, chunked,
> **httplib_request_kw)
> 445
> except BaseException
> 35
> e:
> 446
> # Remove the TypeError from the exception chain in
> Python
> (including for exceptions like SystemExit)
> 448
> Otherwise i Iooks Iike
> bug in the code
> 449
> six.raise_from(e, None )
> 450 except (SocketTimeout, BasesslError, SocketError)
> as e:
> 549 except MaxRetryError
> as
> e:
> 55e
> if isinstance(e.reason, ConnectTimeoutError):
> 551
> TODO:
> RemoVe
> this in
> 3.0.0:
> see #2811
> ConnectionError:
> ('Connection aborted
> RemoteDisconnected( 'Remote end closed connection without response'))
> Output is truncated.View as a scrollable element or open in a text editor Adjust cell output Settings ..
> try
> 447


尝试使用  **[BRAIN API可以实现的功能 – WorldQuant BRAIN]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md) 中所提及的“一种解决超时登出的解决方案”，但会重复运行，如下：**

**
> [!NOTE] [图片 OCR 识别内容]
> While True:
> sign_in()
> #Run Alpha
> code
> print("running.
> except:
> print( 'connection down
> sign_in()
> 〈Response [201]〉
> running-
> 32%
> 338/1050 [13:39<28:45,
> 2.42s /i]
> connection
> down
> 〈Response
> [281]>
> 〈Response [201]〉
> running
> 8%
> 88/1850[03:30〈42:32,
> 2.63s/i]
> try:
**

**为防止报错时可继续执行，在except中加入 return None，这样在运行获取报告时只有当返回不是None才加入列表**

```
def simulation_alphas(datafields):    # alpha code    s = sign_in()     # 每次函数被调用时都会执行，不知道会不会造成过度登录？先将就吧    try:        # simlation code        return alpha    except Exception as e:        print(f"Error processing: {e}")         return None  # 返回一个特殊的值表示错误
```

使用Python的`concurrent.futures`库来并行处理`simulation_alphas`函数：

```
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:    results = []    for result in tqdm.tqdm(executor.map(simulation_alphas, datafields), total=len(datafields)):        if result is not None:  # 检查结果是否是特殊的值            results.append(result)
```

最终结果耗时约50分钟：


> [!NOTE] [图片 OCR 识别内容]
> 53%
> 556/1850[24:50〈31:43,
> 3.85s /i]
> 〈Response [201]〉
> 53%
> 558/1858 [24:51〈21:43,
> 2.65s/i]
> <Response [201]〉
> 〈Response [201]〉
> 54%
> 562/1050 [25:81〈18:05,
> 2.
> 23s/i]
> 〈Response [201]〉
> 〈Response [201]
> 〈Response [201]〉
> 〈Response [201]〉
> 54%
> 564/1858 [25:89〈21:43,
> 2.68s/i]
> <Response [201]〉
> 〈Response [201]
> 〈Response [201]〉
> 54%
> 567/1858 [25:17〈22:04,
> 2.74s/i]
> 〈Response [201]〉
> 54%
> 568/1050[25:19〈28:45,
> 2.58s /i]
> 〈Response [201]〉
> 54%
> 569/1858 [25:29〈31:48,
> 3.97s/i]
> <Response [201]〉
> 〈Response [201]〉
> 54%
> 578/1050 [25:30〈27:80,
> 3.
> 38s/i]
> 〈Response [201]〉
> 〈Response [201]
> 〈Response [201]
> 〈Response [201]〉
> <Response [201]
> There are more than 500 outputs; show more (open the raw output data in a text editor)



> [!NOTE] [图片 OCR 识别内容]
> i
> Status
>  sharpe
> turnoVer
> returns
> drawdown
> margin
> fitness
> aO679MW
> UNSUBMITTED
> 521231
> -0.13
> 1.2235
> -0.0052
> 0.1412
> -0.000009
> -0.01
> Jbq7JYj
> UNSUBMITTED
> -311266
> -0.11
> 0.0379
> -0.0066
> 0.2665
> -0.000349
> -0.03
> SJYXObx
> UNSUBMITTED
> -1707125
> -0.65
> 0.069
> -0.0171
> 0.2408
> -0.000495
> -0.24
> AkgOKqe
> UNSUBMITTED
> 3058111
> -1.15
> 0.1494
> -0.0306
> 0.3333
> -0.00041
> -0.52
> 32W9a70
> UNSUBMITTED
> 3762489
> 1.41
> 0.1464
> 0.0377
> 0.044
> 0.000514
> 0.72
> 1045
> AkgrSMw
> UNSUBMITTED
> 746775
> 0.14
> 0.0247
> 0.0075
> 0.118
> 0.000606
> 0.03
> 1046
> Vd8pboG
> UNSUBMITTED
> 1771105
> 0.38
> 0.0287
> 0.0177
> 0.0889
> 0.001236
> 0.14
> 1047
> WLqZAn1
> UNSUBMITTED
> 2744275
> 28
> 0.0189
> 0.3176
> 0.0869
> 0.033595
> 4.46
> 1048
> PVNYbGX
> UNSUBMITTED
> 2718018
> 0.52
> 0.0164
> 0.0299
> 0.2056
> 0.003641
> 0.25
> 1049
> ao6Q8lv
> UNSUBMITTED
> 1879734
> 0.4
> 0.0281
> 0.0188
> 0.0977
> 0.00134
> 0.16
> 1050 rows x 9 columns
> pnl


---

### 评论 #68 (作者: WL13229, 时间: 2年前)

[QC95604](/hc/en-us/profiles/19798287001111-QC95604)

谢谢提交。看到有个Alpha表现还不错，可以提交吗？

---

### 评论 #69 (作者: ZC69109, 时间: 2年前)

```
问题1:在运行四个小时后api会断开解决：通过创建re-authenticate function每200次simulation后会重新登录问题2：遇到无法simulate的datafield时simulation断开解决：error handling，try-except-continue, 并且记录下不适用datafield问题3：当程序断开重新启动时，会重复run已经run过的datafield还未解决，不过可以通过记录datafield_df来实现问题4:  generated alpha < simulations还未解决，需要进一步阅读api使用文章
```

---

### 评论 #70 (作者: WL13229, 时间: 2年前)

[ZC69109](/hc/en-us/profiles/16836600918551-ZC69109)

请参考本帖子其他同学的作业继续精进。否则后续课程会有非常大的困难。另外每200次重新登录，并不会解决超时登出的问题。目前没有看到您连续完成1000次的证明。

---

### 评论 #71 (作者: ZF71008, 时间: 2年前)

非常感谢老师和大家的论坛分享！小白一枚，非计算机非金融背景，先来领一张第一节课的入场券。。。目前基本完成作业要求，后续有改进再更。。。

1.周四的截图 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Status
> Tolal Unsubmiwed Mlphas
> 315
> Tolal Act Alohus
> TOlu
> CccmmOm
> Wphas
> ToWalNphas
> 327
> 3244175


2.周五的截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> S
> Stalus
> Towl Unsubmed Mlphas
> 1.575
> TotalAciie Alphas
> Tola
> Decommsyloned Alpnas
> Totl Alphas
> 1.588
> 2024/1226


1. 结果

我参考的是这个模板：【Alpha灵感】 看不见的负担

主要搜索'Relationship Data for Equity'相关的datafield以替代pv13_h2_sector

设置发起1000 次Simulation，成功提交994个


> [!NOTE] [图片 OCR 识别内容]
> 99
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for 2
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for
> 2.5
> seconds
> Sleeping for 2
> seconds
> AIpha
> done
> imulating, getting alpha details
> AIpha
> retrieved
> AIpha
> done
> Imulating, getting alpha details
> AIpha
> retrieved
> AIpha
> done simulating〉 getting alpha details
> AIpha
> retrieved
> AIpha
> done
> simulating〉 getting alpha details
> AIpha
> retrieved
> AIpha done simulating〉 getting alpha details
> AIpha
> retrieved
> AIpha
> done simulating〉 getting alpha details
> AIpha
> retrieved
> AIpha
> done
> imulating, getting alpha details
> AIpha
> retrieved
> AIpha done
> imulating, getting alpha details
> AIpha
> retrieved
> AIpha
> done
> imulating, getting alpha details
> AIpha
> retrieved
> AIpha
> done
> imulating, getting alpha details
> AIpha
> retrieved
> C: IUsers Iziyif lAppData | Local | Temp |ipykernel_22
> longer exclude
> empty
> Or
> all-NA columns
> epoch:
> no


目前只是在运行过程打印了epoch信息以显示进度

其他信息作为返回值存在了列表里，需要查看再打印，如performance comparison中的部分关键信息：


> [!NOTE] [图片 OCR 识别内容]
> [36]:
> sharpe
> fitness
> turnover
> returns
> drawdown
> margin
> YOrAYBw
> 0.29
> 0.09
> 0.0127
> 0.0122
> 0.1337
> 0.001927
> MkWxVdg
> 0.30
> 0.10
> 0.0125
> 0.0128
> 0.1387
> 0.002044
> ZrSONX8
> 0.31
> 0.10
> 0.0125
> 0.0131
> 0.1387
> 0.002098
> n3JWrPI
> 0.31
> 0.10
> 0.0125
> 0.0132
> 0.1371
> 0.002114
> bvkgAap
> 0.31
> 0.10
> 0.0125
> 0.0131
> 0.1361
> 0.002099
> bvkgAb6
> 0.31
> 0.10
> 0.0125
> 0.0132
> 0.1371
> 0.002114
> ddXQvbJ
> 0.31
> 0.10
> 0.0124
> 0.0130
> 0.1387
> 0.002111
> n3JWraM
> 0.32
> 0.11
> 0.0126
> 0.0135
> 0.1375
> 0.002133
> PVWIKoK
> 0.28
> 0.08
> 0.0104
> 0.0115
> 0.1263
> 0.002201
> AKW3EVW
> 0.28
> 0.09
> 0.0105
> 0.0118
> 0.1276
> 0.002248


偶尔遇到不匹配的数据就跳过


> [!NOTE] [图片 OCR 识别内容]
> epoch:
> Failed (dropped
> QUt ,
> no Location
> header);
> my_group=bucket (rank (inst4_Fund
> pep
> hold ),range="0.1,0.9,0.1");
> GTS_grouped
> group
> rank(ts_
> mean (goodwiI, 252 ) /ts
> mean
> (sales,252) ,
> c_
> Broup )
> GTS_grouped
> Failed (dropped
> OUt,
> Location
> header ):
> Iy
> group=bucket (rank (inst4_incr_position ) , range=
> 0.1,0.9,0.1");
> GTS_grouped
> Broup
> rank(ts
> mean (goodwill, 252 ) /ts_mean (sales, 252) ,
> my_Broup )
> GTS_Brouped
> Failed (dropped
> oUt
> Location
> header);
> Iy_
> group=bucket (rank(inst4_
> ins
> pep
> hold),range=
> 0.1,0.9,8.1");
> GTS_Brouped
> Broup
> rank(ts
> Iean
> (Boodwill, 252 ) /ts_mean (sales, 252) ,
> Broup )
> GTS_grouped
> Sleeping for
> 2,5
> Seconds
> SIeeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> SIeepins For
> 2.5 seconds


测试时候遇到计算时间太久的也跳过


> [!NOTE] [图片 OCR 识别内容]
> Sleeping for 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for 2
> seconds
> Sleeping for 2.5 seconds
> Sleeping for 2
> 5 seconds
> Sleeping for 2_
> seconds
> Sleeping for
> 2.5 seconds
> Sleeping for 2
> 5 seconds
> Sleeping for 2_
> seconds
> Sleeping for 2
> 5 seconds
> Sleeping for 2.5
> Seconds
> Sleeping for 2
> seconds
> Sleeping for 2
> 5 seconds
> Simulating
> more
> than
> mins--pass
> AIpha done simulating〉
> getting
> alpha details
> KeyError:
> alpha
> encountered


1. 反思

4.1 代码效率

目前只是按照最简单的逻辑写出来了最基本的功能，不太懂线程和进程的概念。。。

写了一个循环每10个绑为一组进行处理，回到平台试图增加新的任务，error显示似乎已经达到上限 
> [!NOTE] [图片 OCR 识别内容]
> UONe US KpNaIaNeI Cao
> You have reached the lit @fCoICUIrent Slmulations: Please Wait for
> previous simulations to fnish。
> Example
> Simulate
> Visualization


并且为了缩短测试时间，设置了一个时间阈值，超过30s的alpha就先过掉了

4.2 debug经历

有时候被 KeyError: 'alpha' 中断（运行这个语句：alpha_id = progress.json()["alpha"]）；

参考论坛这篇文章《BRAIN API及日常回测时常见的报错》，老师的回答：有些Alpha虽然有location，但是不一定能返回json.当您的代码获取到location后，您需要使用get方法获取location的信息，如有返回，才能解析出json. 这意味着，有时候它的返回是None, 或者里面没有信息。

随后写了一个try except 把返回值为None的url就抛弃了。

有时候遇到很长时间的simulation（有的15分钟左右，可能是计算超时最终中断报错，返回的simulation_progress里没有“alpha“ header），大概率是因为datafield中vector的没有处理直接喂进模板导致simulation时间过长。这1000次模拟非常漫长，结果也只有40个alpha成功提交。

随后写了一个try except，把sleep30s以上的就跳过了。并且暂时先仅输入matrix类型的数据。

4.3模板适合的数据类型

当前模板数据类型仅支持martix，在预处理的时候仅检索’MATIRX’, 把vector和group都舍弃了

4.4模板的改进方向

代码的优化和效率的提升，对于我来说还有非常大的改进空间，暂且搁置。在功能方面，希望下一步可以先解决：当前模板数据类型仅支持martix，需要考虑怎么处理vector和group类型的datafield；

需要一段代码，帮助检验相关性等筛选可以提交的alpha

---

### 评论 #72 (作者: EC34309, 时间: 2年前)

**(I apologize in advance for writing this in mostly English, I understand chinese perfectly but I can't type it out efficiently.) 
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> File
> Edit
> View
> History
> Bookmarks
> Profiles
> Tab
> Window
> Help
> *
> 73%
> A
> Wed 24 Jan 5:23PM
> WorldQuant BRAIN
> 义
> 23
> platform.worldquantbrain.comlalphaslunsubmitted
> New Chrome available
> WORLDQUANT
> BRAINI
> Simulate
> Alphas
> Data
> Competitions (6)
> Events
> Learn
> ! Refer a friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 10
> out of 847
> Filter
  
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> File
> Edit
> View
> History
> Bookmarks
> Profiles
> Tab
> Window
> Help
> *
> 99%
> A
> Fri 26 Jan 7:52PM
> WorldQuant BRAIN
> X
> 2
> platform.worldquantbrain.comlalphas/unsubmitted
> New Chrome available
> WORLDQUANT
> BRAINI
> Simulate
> Alphas
> Data
> 鬯 Competitions (6)
> EVents
> Learn
> 显
> Refer a friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 30
> out of 2,234
> Filter
**

**Step2: 思考合適的資料欄位和參數。以此範本為例，可能基本面的model data也是不錯的，但時間參數可能需要至少月以上。如果是量價數據，可能需要更短的時間週期。**

我选择了 “【Alpha靈感】A股市場擁擠度因子”.

**Step3: 使用**  [**Data Explorer**](https://platform.worldquantbrain.com/data)  **手動嘗試幾個不同類型(category)的資料集，再次深入反思該範本提取的是什麼層面的資訊。/** 模板適合的資料類型

The original paper suggests a surge of volume, might imply a concentration of capital and bubbles in certain subsets of assets.

A sudden surge of volume is defined as following:

Let “2nd volume” be the mean volume of this week and “1st volume” be the mean volume of last week.

If one of the three conditions is satisfied, the current day is a score of 1, otherwise 0:

1. mean volume of this week > mean volume of last week + predefined volume
2. (mean volume of this week) / (mean volume of last week) > 2
3. mean volume of this week > mean volume of last week + predefined volume AND being the top P% in ratio (mean volume of this week) / (mean volume of last week) in a cross-section.

By searching volume on Data Explorer, the results can be divided into these broad category:

Daily volume:

- Interval volume
- Sentiment volume
- Put/call volume
- Average daily volume

The most obvious data fields, which are used in the original post.

- Relative sentiment volume

Similar logic as trade volume.

模板的改進方向:

Price Metrics/Fundamentals:

- Volume weighted average price
- Daily open/close/high/low price
- Dividend
- Stock split ratio

A surge in prices relative to fundamentals could potentially detect bubbles.

Market Share Metrics:

- Anonymous market share
- Industry/Tier 1 market share
- Concentration metrics like summation of squared market shares

A surge in retail traders can also imply bubbles.

**Step4: 使用代碼取得該類型的所有資料集和大部分資料欄位（datafield)**

**Step5: 將資料初步處理（例如vector data需要先使用vector operator降維）**

For some reason, vector and group data all use too many resources, causing a failure to simulation (for instance, vec_avg(scl12_cubealltype_buzzvec)).

Is this because I have an overseas account or is it the same for everyone?

Regardless, I wrote the appropriate if else statement to apply a vector / group operator if such data types are detected.

**Step6: 將資料欄位插入模板，批次產生Alpha表達式。**

**Step7: 將Alpha表達式附上simulation setting （這一階段可以使用比較常見的setting，無需過度調參）**

To ensure the degree of freedom in terms of simulation data, I allowed the changes on the entire simulation data instead of just the data fields, which motivated me to write a generator to prevent excessive memory usage.


> [!NOTE] [图片 OCR 识别内容]
> def
> simulation_data_generator (data_field_list,
> type_list,
> regions, universes_mapping)
> for field,type
> in Zip(data_field_list, type_list):
> for region
> i
> regions:
> for universe
> in universes_mapping.get (region
> []):
> # Create
> COPy
> of the
> simulation data dictionary With
> the updated
> region
> and universe
> i type
> IVECTOR"
> field
> fivec_avg({field})"
> i type
> IGROUPI
> field
> f"group_mean ( {field},1)"
> modified_simulation_data
> {
> type
> REGULAR'
> settings
> instrumentType'
> EQUITY'
> region
> region,
> # Set
> from
> the
> iteration
> universe
> universe,
> # Set universe
> from
> the
> iteration
> delay
> 1,
> decay
> 15,
> neutralization
> SUBINDUSTRY'
> truncation
> 0.08,
> pasteurization
> ON'
> unitHandling
> VERIFY
> nanHandling
> OFF'
> language
> KASTEXPR'
> Visualization
> False,
> regular'
> f"w
> P = 0.5;
> VOZI
> ts_mean ({field}, 5);
> VO22
> ts_mean (ts_delay ( {field} ,5),5);
> condition
> Or(voll/vol2>2,and (Vol1/v012>1.3, rank (VolI/vo12)>1-P));
> -ts_sum(if_else(condition, 1,0),20) ;
> # Yield
> the
> modified
> Simulation
> data dictionary
> yield modified_simulation_data
> region


**截圖顯示你的code連續不停（不可中斷，代碼需能handle各類報錯）**

I used multi-threading on the “simulate” function, which returns alpha id if simulation proceeds successfully. If syntax error / time-out occurs, no id would be returned.

In the multithreading function, I set up a limiter to manage workers so that it keeps the simulation number constantly on 10 (the limits). Alpha-id is recorded and returned as a list.


> [!NOTE] [图片 OCR 识别内容]
> import threading
> from queue iport Queue
> # Define the Worker
> function
> that
> Will
> simulate the data and store
> the alpha_id
> def
> simulation_Worker(simulation_data,
> 51
> thread_limiter,
> results_queue)
> With thread_limiter:
> alpha
> i
> simulate (simulation_data)
> i alpha
> i
> is
> not
> None:
> results_queue. put (alpha_id)
> def manage_simulations (generator,
> s):
> thread_limiter
> threading. Semaphore (10)
> threads
> []
> results_queue
> Queue()
> # Queue
> t0
> store
> the results
> for
> simulation_data
> in generator:
> thread
> threading. Thread (target=simulation_worker, args=(simulation_data,
> 5,
> thread_limiter,
> results_queue)
> thread.start ( )
> threads.append (thread)
> # Wait
> for
> a11 threads
> t0
> finish
> for
> thread
> i threads:
> thread.join( )
> # Retrieve
> a11 results
> from the
> queue
> results
> []
> While
> not
> results_queue.empty ():
> results.append
> results_queue.get() )
> return results
 A dataframe of performance can be generated via get_test_all.


> [!NOTE] [图片 OCR 识别内容]
> def get_test
> one(checks_json)
> # Create
> dictionary
> t0
> hold the processed
> Check
> data
> checks_dict
> {}
> for check
> in checks_json ['is' ] ['checks']:
> check_name
> check [
> name
> checks_dict [f
> {check_name}_result
> ]
> check.get
> result'
> None)
> # checks_dict [f'{check_name}_limit' ]
> check.get (
> limit
> None)
> checks_dict [f
> {check_name}_value
> check.get
> Value
> None)
> return checks_dict
> def get_test_all(model_ids)
> # Initialize
> an empty
> list
> t0
> Collect
> the
> 「OWS
> rows_list
> []
> # Loop
> over each model
> ID
> for model_id
> in model_ids:
> # Get
> the
> Checks
> for
> the
> model
> checks_json
> get_check(s, model_id)
> # Process the checks
> into
> dictionary
> Checks
> dict
> get_test_one
> checks_json )
> Add
> the model_id
> t0
> the dictionary
> checks_dict [ 'model_id']
> model_id
> # Append
> the dictionary
> t0
> OUI
> list
> 01
> 「OWS
> rOWs
> list.append (checks_dict)
> # Create
> DataFrame
> from
> the
> list
> 01
> FOWS
> df
> pd.DataFrame ( rows_list)
> return
> df
 A plot on sharpe of simulated ratio can be obtained:


> [!NOTE] [图片 OCR 识别内容]
> Histogram of LOW_SHARPE_value
> 70
> ED
> SD
> 40
> 
> 30
> 20
> 10
> LOII SHARPE Value


Unfortunately, I can't re-login continuously as an overseas account requires biometric-authentication.

總結反思，需包含至少四個面向的反思：程式碼效率、debug經驗、模板適合的資料類型、模板的改進方向。多寫不限，字數不少於300字。

“代碼效率”:

Generator on simulation_data_list greatly improves memory complexity,

I did think of writing a recursive generator as if we allow more freedom on the simulation settings, purely written nested for loport is not the best approach, but it is not that importantops at this stage.

“Debug經驗” :

I didn't encounter any significant bugs, the api is very well-written.

I did need to request the biometric authentication link and then re-login again to receive <201> response, which is the closest obstacle I encountered.

「範本適合的資料類型,範本的改進方向」: already discussed in  **Step3**

However, I wish to elaborate on the problem on the current template,

As most of the data-fields can't even reach a sharpe of 2, across different universes of CHN and USA, strongly suggest against the logic of this template.

There could be several reasons for this phenomenon:

1. Bubble/ concentration of capital detection is correct, but the momentum of the bubble carries significant risks
2. Bubble/ concentration of capital detection is incorrect, meaning volume related data can't effectively detect bubbles via the current rule.

Possible improvement could be:

1. Stricter bubble detection for more sensitive data, such that we only short when the stock is at nearly high points.
2. More relaxed detection for less sensitive data, preventing strategy with nearly one-off trade.
3. Time decay on counting “score”, as we are using ts_sum currently which has the same weight for current day and let's say the past kth day.

---

### 评论 #73 (作者: WL13229, 时间: 2年前)

[ZF71008](/hc/en-us/profiles/20098272506775-ZF71008)

看到这位同学在回测期间成功还提交了一个Alpha,祝贺！

---

### 评论 #74 (作者: WL13229, 时间: 2年前)

[EC34309](/hc/en-us/profiles/13557080755991-EC34309)

这位同学展示出了出色的代码能力和金融能力，相信后面的课程一定能给你更多启发。让我们下节课再见。

---

### 评论 #75 (作者: OD35570, 时间: 2年前)

1、

总共simulate了1000个左右的alpha，在模型意义上还有所欠缺，可能导致回测出来的结果欠佳

simulation前


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 566
> Show
> 10
> Out
> Filter
> Unsubmitted:
> 538
> Active:
> 28
> Select Columns
> ItUs
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> e:吕>1
> e.吕>1
> e.8〉1
> Select
> aTOTYITOUS
> RegOIaT
> JNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> -0.17
> -0.969
> 21.099
> anonymous
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.52
> 2.90%
> 21.459
> anonymoUs
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> -0.25
> 1.379
> 21.409
> anonymous
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.28
> -1.659
> 21.449
> anonymoUs
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> -0.19
> 1.249
> 21.349
> anonymous
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.03
> 0.179
> 21.269
> anonymoUs
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.41
> 2.599
> 21.359
> anonymous
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.25
> 1.579
> 21.31 %
> anonymoUs
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.06
> 0.4096
> 21.389
> anonymous
> Regular
> UNSUBMITTED
> 01/25/2024 EST
> USA
> TOP3000
> 0.52
> 3.209
> 21.399
> Show
> 10
> out of 538
> Prev
> 54
> Next
> 12:19
> 索
> V
> 简体
> 2024-01-26
> 月


simulation后


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 1,651
> Show
> 10
> out
> Filter
> Unsubmitted:
> 1,623
> Active:
> 28
> Select Columns
> ItUS
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> @.8>1
> e.8〉1
> e.吕>1
> Select
> ATOTYITOUS
> RegOIaT
> JNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> -0.14
> -0.969
> 21.149
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> T0P3000
> -0.55
> -4.609
> 20.869
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> 0.03
> 0.109
> 21.609
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> -0.61
> 3.7796
> 21.219
> anonymoUs
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> 0.53
> 3.929
> 21.619
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> -0.09
> -0.3096
> 21.779
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> -0.15
> -0.5096
> 22.069
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> T0P3000
> 0.12
> 0.879
> 21.009
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> -0.04
> -0.2296
> 21.329
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> -0.74
> 4.939
> 21.249
> Show
> 10
> out of 1,623
> Prev
> 163
> Next
> 13:18
> 圊 y " 9
> 又  8
> @
> l %中 S
> 2024-01-26
> 月
> Tag


2、模板的选择 ： 【alpha灵感】单因子测试之财务质量因子

```
my_group = bucket(rank(cap), range="0.1, 1, 0.1");group_neutralize(rank(mdl175_roediluted+mdl175_cashrateofsales), my_group)
```

我们考虑替换的数据字段是用相关的基本面数据作为因子来替换，从而选定了数据集fundamental28，然后选取其中的数据字段进行替换，从而组成我们等待回测的alpha字段。

3、回测具体的步骤

根据上一期同学的经验，我们考虑最大线程数为10的线程池进行回测，一次提交10个alpha进行回测，本次操作和后面的操作中貌似都没有出现bug，所以我仅仅用设置了一个try 来实现断线重连。


> [!NOTE] [图片 OCR 识别内容]
> With
> ThreadPoolExecutor (max_workers=1o)
> a5
> pool :
> for
> 1
> in alpha_list_simulation:
> pool.submit(alpha_simulation,
> i)


此外为了验证alpha的质量，我仅仅选取了 ['SHARPE','FITNESS','TURNOVER'] 这几个数据来进行导出，并且储存到Excel中方便查看。 
> [!NOTE] [图片 OCR 识别内容]
> B
> I
> R
> S
> OzlOkJq
> PBXAIgi
> gIyLbzg
> Y063450
> 32b23}
> AAJAE
> vdq3nwb
> Gz8v3nP
> 540326
> p8mbg@8
> P8Z1j@ _
> qSIVVI
> @8
> ZrSeNx0
> IrabkGN
> IrqbRkn
> QEJL5jG
> vdq3Jgz
> k0721b2
> ZOMIJoX
> Rd3nk2e
> OVpM
> SIARPE
> -0.25
> -0.11
> 0.35
> -0.15
> 0.53
> -0.17
> -0.12
> 0.66
> 0.05
> 0.05
> -0.05
> -0.15
> -0.24
> -0.11
> 0.18
> -0.
> 0.62
> 0
> 38
> 33
> 0.21
> FITMESS
> -0.07
> -0.02
> 0.12
> -0.02
> 0.22
> -0
> 04
> -0.02
> 0.29
> 0
> 01
> 0.01
> -0.01
> -0.03
> -0.07
> -0.02
> 0.04
> -0.02
> 0.28
> 0.13
> 04
> 0.05
> TURNOVBR
> 0.2128
> 0.2132
> 0.2128
> 0.2182
> 0.2106
> 0.2132
> 0.2089
> 0.2128
> 0.2119
> 0.2146
> 0.2117
> 0.2123
> 0.2115
> 0.2122
> 0.2106
> 0.2116
> 0.2116
> 0.211
> 0.2111
> 0.2142
> 0.2131
> 0


4、不足与反思

- 感觉在所挖掘的alpha在经济意义上不强，回测效果较差，仅仅有2-3个勉强sharpe达到要求，可能需要后续学习如何针对性的进行提升。
- 觉得通过大模型api的接口可以省却很多理解研报的时间，后续会往这方面多学习

---

### 评论 #76 (作者: YT47842, 时间: 2年前)

我下午提交了1200次，但是由于开始提交的时候忘记截图了，所以傍晚用同样的代码又提交。但是发现这个报错 
> [!NOTE] [图片 OCR 识别内容]
> RemoteDisconnected
> Traceback (most recent
> Call
> last)
> File LusrLlocalllibLpython3.llLsite-packagesLurllib3Lconnectionpool_py:7ge,
> in HTTPConnectionPool.url
> 789 # Make the request
> on the HTTPConnection object
> 790
> response
> self._make_request (
> 791
> conn;
> 792
> method,
> 793
> Url,
> 794
> timeout=timeout_obj,
> 795
> body=body,
> 796
> headers=headers,
> 797
> chunked-chunked,
> 798
> retriessretries,
> 799
> response_conn=response_conn,
> 800
> preload_content=preload_content,
> 801
> decode_content=decode_content,
> 802
> *response
> KW
> 803
> 805 # Everything went great!
> File LusrLlocalllibLpython3.IILsite-packagesLurllib3Lconnectionpool_py: 536,
> in HTTPConnectionPool:_ma
> 535
> 536
> response
> Conn.
> getresponse()
> 537 except (BasesSLError,
> OSError)
> a5
> 巳:
> 503 except MaxRetryError
> a5
> e:
> 504
> 讧
> isinstance(e. reason,
> ConnectTimeoutError) :
> 505
> # TODO:
> Remove
> this
> in 3.0.0:
> See #2811
> ConnectionError:
> ('Connection aborted。
> RemoteDisconnected (
> Remote end closed
> connection Without
> res
> Output is truncated. View as a Scrollable element or open in a text editor: Adjust cell output Settings:.
> try:


请问有同学遇到过类似的问题吗？
具体报错信息：ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

以下是下午提交1200次后的结果： 
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> 文件
> 编辑
> 视图
> 历史记录
> 书签
> 个人资料
> 标签页
> 窗0
> 帮助
> 43字
> @
> 2
> 38s
> 回
> 1月278周六  15:08
> Price Volu
> X
> WorldQua
> X
> WorldQua
> 义
> WorldQua
> X
> 英才候选)
> 义
> WorldQua
> X
> BRAIN AP
> X
> 唱
> ipynb
> > G 命
> platform. worldquantbrain.comlalphaslunsubmitted
> 区
> 馆 Keras入 门必看教程
> s
> Keras中文 文档
> 知
> Keras教程
> Python教程 -
> 廖雪..
> 深度学习从小白到.
> Keras教程_腾讯视频
> 所有书签
> 变量
> 泛大纲
> Python 3.11.5
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Data
> { Competitions (2)
> EVents
> Learn
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Python
> Show
> 10
> out of 1,929
> Filter


这里是提交的用时
 
> [!NOTE] [图片 OCR 识别内容]
> Alpha
> retrieved
> Alpha
> done simulating, getting alpha details
> Alpha
> retrieved
> Alpha
> done
> simulating, getting alpha details
> Alpha
> retrieved
> Alpha
> done simulating, getting alpha details
> Alpha retrieved
> Alpha
> done
> simulating, getting alpha details
> Alpha retrieved
> Alpha
> done simulating, getting alpha details
> Alpha retrieved
> Alpha done simulating, getting alpha details
> Alpha
> retrieved
> Output is truncated. View as a Srollableelement or open in a text editor: Adjust cell output Settings.
> LarLfoldersLctLgnkzgjszclggldhlhpzht4oo@@@gnlTLipykernel
> 2645/26@2660568.py:13
> FutureWarning: The
> Summary_df
> pd.concat ( [summary_df,
> df], axis=o)
> 总用时:
> 2
> h
> 48 min 58.93
> LarLfoldersLctLgnkzgjszclggldhlhpzht4o@o@@gnLILipykernel 2645/3578492456.py;33
> FutureWarning:
> The
> al1_summary_df
> pd.concat ( [all_summary_df
> summary_df] 
> aXis=0 )
 这里是提交的alpha的模拟结果
 
> [!NOTE] [图片 OCR 识别内容]
> al1_summary_df
> [11]
> 0.OS
> Python
> sharpe
> ftness
> turnover
> returns
> drawdown
> margin
> XRGrNSJ
> 1.61
> 0.72
> 0.3699
> 0.0733
> 0.0581
> 0.000396
> aoYKIP5
> 1.44
> 0.62
> 0.3445
> 0.0640
> 0.0627
> 0.000372
> 5MbEp9G
> 1.36
> 0.57
> 0.3637
> 0.0643
> 0.0607
> 0.000354
> Ek7GGbP
> 1.24
> 0.51
> 0.3059
> 0.0512
> 0.0666
> 0.000335
> gXAeBKV
> 1.50
> 0.66
> 0.3617
> 0.0693
> 0.0614
> 0.000383
> 9JvdXQ1
> 1.48
> 0.65
> 0.3432
> 0.0661
> 0.0483
> 0.000385
> Lkjmel
> 1.40
> 0.60
> 0.3676
> 0.0684
> 0.0484
> 0.000372
> WLmzjg5
> 1.61
> 0.74
> 0.3878
> 0.0809
> 0.0461
> 0.000417
> qg1YjbV
> 1.14
> 0.47
> 0.3468
> 0.0583
> 0.0658
> 0.000336
> MkWe7wL
> 0.44
> 0.18
> 0.3798
> 0.0603
> 0.2521
> 0.000318
> 1200 roWS X 6 columns
 思考：
使用的alpha表达式：

'ehat=ts_regression(returns, {datafields_list[n*epoch+j]}, 60);group_zscore(ts_zscore(-ehat, 60), subindustry)'

代码效率：
使用了10个一组的测试方法，但是感觉使用并发后代码效率会更高
debug经历：
同样遇到了simulation_progress.json()['alpha']找不到对象的问题。在报错中看出是表达式的书写有拼写错误，改正拼写错误后该错误消失；
遇到过在提交过程中有VPN被禁止的问，关掉VPN后恢复正常（但是由于之后需要使用GPT类的工具所以代理也是必须的，希望下次能够改进这个）
模版适合的数据类型：
我选用的是price volume的数据，对于vector使用vec_sum对于matrix则不做处理
模版改进的方向：
该模版由于是从论文研报合集中取得所以prod_corr比较高，后期需要从其他数据源的论文中获取一些灵感

---

### 评论 #77 (作者: QZ41342, 时间: 2年前)

1.开始提交前

共1190次


> [!NOTE] [图片 OCR 识别内容]
> WorldQuan BRAIN
> https: |platform worldquantbraincom alphas/unsubmitted
> 器"
> Osimuate
> Nphs
> Dala
> CMAIOI
> Cvens
> 0tearn
> 孚 Reler aIiend
> Alphas
> NI NII
> Submtted
> Total:
> 204
> SCN
> Unsubmitted:
> 1,190
> Actve:
> Select Coluns
> Dle Creatc (ESTI
> Dccommssioned:
> _RT_
> TBJT
> ILONTTTTTC
> 01/230-+CST
> ACDOU
> TBJIAI
> JUANITTTO
> 0122/202+CST
> CT
> Aomylar
> UISO9NIITT[
> OIRROSST
> ULIOU
> UNITTLO
> 777 T
> OACTU
> RBUr
> UIUNITTTC
> 01/2202+CST
> Ca
> 
> RcLUIr


2.提交完成后

共2214次


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant BRAIN
> https: platform worldquantbraincomjalphas/unsubmitted
> U
> 訾2
> Slmulate
> Alphas
> Data
> Competidons [3]
> Events
> 0 leamn
> Alphas
> Unsubmitted
> Submitted
> Total: 2,228
> Unsubmtted:
> 2214
> Mctve
> SMect Columns
> Date
> Decommissioned:
> OTUTITUU=
> ULSUI
> SNGUIAMITTFT
> ATOTTTTU
> Resular
> MIUIIITTI
> OT
> ANCTNU _
> ReBUla'
> UNSUAMITTTT
> C
> 300TCTU
> Resular
> UINSUAIITTFC
> ATCTTTU+
> Rebular
> UNSUIIITTLC
> CTC
> AONOUs
> RFBUIJ'
> UNSUOMITTLC
> 01/27
> 20247107
> SroN


1. 代码连续运行情况

连续完成提交1000次，后续可能考虑多进程等方法加快速度


> [!NOTE] [图片 OCR 识别内容]
> Ucl3忙 .
> 9074010400.4090002
> 2.9229751551
> ClULCUaalatsTUNUEIT 453
> alat C
> 因孑恺揠与检验:
> 998
> 994/1000 [4:00:25.00:02,
> 2.75it/s]ts_regresslon(anlg_confirotime ,anll6_medlanre
> 因孑麇揠与检猃:
> 100%
> 995/1000 [4:00;26<00:01
> 95It/5]t5_min(ts_Corr
> ltg_all_delay
> mean anl
> 因子挖搌与楹/:
> 100%
> 996/1000 [4:00:26200:01
> 3.Ilit/slts_corr (ts_regression(anllo_aftercons_median
> 因子挖搌与检验:
> 100%
> 997/1000 [4:00:26200:00,
> 3.18it/sJanlg_estinatetime^2
> 因孑挖报与检猃:
> 180%
> 998/1000 [4:00:27400:00,
> 2.79it/5]anl16_highest_normal/antio_highest_normal
> 因子挖揠与橙俭:  100%
> 999/1000 [4:00:27400:00
> 2.98it/s]ts_sto_dev(1/an11o recvalue, 10)
> 因子挖揠与检验:
> 1008
> 1000/1000 [4.00:27.00.00,
> 14.435/1t]
> (anl39


4.总结与反思

本次我参考遗传规划的方法：

（1）首先在python定义brain平台支持的运算符为python函数，使用传入数据名称，输出因子表达式；前期共定义了包括ts_mean，ts_regression等十余个函数

例如：

```
def ts_corr(x,y):    return f'ts_corr({x},{y},10)'
```

（2）在一次循环中，随机选择使用运算符的个数（设置最大个数为4以避免过拟合），然后根据算符的个数随机抽取运算符，然后根据运算符所需的数据个数随机抽取数据种类

（3）对抽取的运算符和数据进行拼接，形成完整的因子表达式

（4）对因子表达式进行检验，使用因子检验通过条件的比例作为目标函数

效果如下：


> [!NOTE] [图片 OCR 识别内容]
> result
> region
> uniVerse
> neutralization
> sharpe
> pass_ratio
> alpha_id
> regul
> SLB
> TOP30O0
> SUBINDUSTRY
> 08000
> 0.36400
> ddXrrE
> ~ts_decay_linearfreturn:
> GLB
> TOP3OOO
> SUBINDUSTRY
> 1.08000
> 0.36400
> ddXrrE
> decay_linearfreturn:
> SLB
> TOP30O0
> SUBINDUSTRY  1.07000
> 0.36400
> PWLgL
> ~ts_meanfadv20,10j*ov
> SLB
> TOP3OOO
> SUBINDUSTRY
> 1.03000
> 0.36400
> XRGIbjq
> ~ts_scale(low,10]
> SLB
> TOP30O0
> SUBINDUSTRY 0.75000
> 0.36400
> VdqxjeQ
> medianfts_min(split
> SLB
> TOP3OOO
> SUBINDUSTRY 0.30000
> 0.36400
> Ooygko
> ICap
> SLB
> TOP30O0
> SUBINDUSTRY  0.29000
> 0.36400
> WgqZXP
> regressionhwap,hig
> SLB
> T0P3000
> SUBINDUSTRY
> 0.25000
> 0.36400
> P8XpZpG
> 1/close
> SLB
> TOP30O0
> SUBINDUSTRY  0.23000
> 0.36400
> 9g1aMyP
> 1/law
> SLB
> T0P3000
> SUBINDUSTRY   0.22000
> 0.36400
> 乙-5177.
> Iopen
> SLB
> TOP30O0
> SUBINDUSTRY
> 0.22000
> 0.36400
> SJuMpJg
> 1/high
> SLB
> T0P3000
> SUBINDUSTRY
> 0.18000
> 0.36400
> eLPZOog
> ts_scale(ts_std_dev(higl
> 12
> SLB
> TOP30O0
> SUBINDUSTRY   0.14000
> 0.36400
> mZ3K3ap
> ranr(volume)
> SLB
> T0P3000
> SUBINDUSTRY   0.14000
> 0.36400
> W9qr71x
> rank(volume)trank(vo
> SLB
> TOP30O0
> SUBINDUSTRY
> 0.00000
> 0.36400
> 1J9ILbK
> rank(adv20j
> "
> SLB
> TOP3OOO
> SUBINDUSTRY
> 0.09000
> 0.36400
> Jbwayy
> ts_corrfwwap,wwap low
> SLB
> TOP30O0
> SUBINDUSTRY
> 0.13000
> 0.36400
> 6282GWE
> Volume +volume
> GLB
> TOP3OO0
> SUBINDUSTRY
> 0.18000
> 0.36400
> n3Jrll
> adv20+adv20
> SLB
> TOP30O0
> SUBINDUSTRY
> 0.28000
> 0.36400
> 1J90Y8」
> sharesouttsharesout+
> result
> 袼式:
> 965


这样的方法能够快速组合出大量的因子表达式并进行检验，但由于brain是提供表达式进行检验，无法调用常规的遗传规划库进行优化，本次的简单尝试中也没有加入优化算法的思维，导致无法快速找到较好的因子，可能会作为一个以后尝试的方向。

---

### 评论 #78 (作者: WL13229, 时间: 2年前)

[YT47842](/hc/en-us/profiles/19897065331095-YT47842)

您好，这个报错就是超时登出的错误。需要反复重连直至连通

---

### 评论 #79 (作者: SM56169, 时间: 2年前)

1.最近的截图（需包括时间）


> [!NOTE] [图片 OCR 识别内容]
> Infinity Champions 004
> Alphas
> Seeall
> Leaderboard
> Alphathon 2023
> StatUs
> Stats
> Total Unsubmitted Alphas
> 630
> Rank:
> Total Active Alphas
> 20
> Score:
> 24,707
> Total Decommissioned Alphas
> Alphas:
> 18
> Total Alphas
> 650
> Level:
> Gold
> 9:52
> 搜索
> ^  英 谷d口
> 2024/1/27


2.下周二前的截图（需显示时间）


> [!NOTE] [图片 OCR 识别内容]
> Infinity Champions 004
> Alphas
> Seeall
> Leaderboard
> Alphathon 2023
> Status
> Stats
> Total Unsubmitted Alphas
> 1,717
> Rank:
> Total Active Alphas
> 20
> Score:
> 24,707
> Total Decommissioned Alphas
> Alphas:
> 18
> Total Alphas
> 1,737
> Level:
> Gold
> 22:17
> 搜索
> ^  英 谷d幻
> 2024/1/27


3.截图显示你的code **连续不停（不可中断，代码需能handle各类报错）** 提交了1000个simulation。


> [!NOTE] [图片 OCR 识别内容]
> [9]:
> Collit
> for aatafiell
> in datafields [' 过']
> to_liet (} [:LIO0]
> try
> einulation_data_temp
> einulation
> Jata
> einlatiori_lata
> 十FTIT
> regulir '
> 士 Te_Ralll (rarll
> {latafiela} ! 
> 201
> einulation
> 工 ERTILIIzE
> post ('https: ! Sapi
> TTIII
> Uquantbrain. Conieimlatiors
> jon-eimulation_data
> telp!
> Locatior
> i einllatior
> RTIITI?F
> header2
> einulation
> TIr UTr e33
> IIIL
> einlatior_
> EepoIlee. Leader 3
> Locatior'
> fiiehel
> Fal8e
> while
> IrUe
> 8inulatior_progre33
> Set leinlatiorl_PIOSrERR_
> UII11
> i einlatiori
> proereg8. headere. get
> Retry-u ter
> brea
> 8leep {loat {eilatiori
> TIr UTr e33
> Lieader?
> Retry-u ter
> alpla_
> einlatiori
> Oereee
> 8ou (}
> aIpla
> ILPIIa
> httpe : ! Sapi
> aquantbrain. Con}alphas ;
> alpha_i
> Collit
> Prirt {cout;
> aatafiela,
> alpha. jor {} ['1'
> ['aharpe']
> BTCept
> eign_i(}
> LILILC "
> 1064
> alll4_etlley_ebitla_fyt
> 0.18
> a11
> stddey_ebitda_f5 0.42
> 06
> al14
> 8tlley_ePe_fpl
> IO6
> Ill
> tddet
> epe_f2
> 10fg
> f3
> 0Gg
> 1IT
> f5
> Ill
> 1074
> a11
> 1075
> Ill
> 10阶
> a11
> fIIET
> EPerer
> 10?
> Ill
> 3+FT
> TISr ET
> f2
> 10{
> epsrep_fp3
> 1039
> TISr ET
> t4
> I080
> al1
> tllet
> epsrep_fp5
> I081
> a11
> etddeT_
> FPerEp
> 土l
> 1082
> ail14etllet_eparer_
> A2
> Ret
> IOCI


4.总结反思，需包含至少四个方面的反思：代码效率、debug经历、模板适合的数据类型、模板的改进方向。多写不限，字数不少于300字。

代码效率：可以通过多线程提交测试任务成倍缩短总的回测时间。在连接断开的情况下，可以增加一些异常处理机制，确保测试任务能够在连接恢复后继续执行。可以考虑将测试失败的alpha信息记录下来，以便后续分析和修复。

debug经历：在回测未完成时，会提示Location字段不存在的错误，加入了检验Location字段是否存在的判断条件。

模板适合的数据类型：正向信号的基本面数据，机构调研数据，对已有的因子的结果做平滑。

模板的改进方向：模板的改进方向可以包括对不同数据选择不同的时间区间，以适应不同市场环境的变化。在显示回测结果方面，可以设计更结构化、直观的报告，包括性能指标、风险分析、交易历史等信息，提供全面的策略评估信息。此外，记录合格的alpha的相关信息，可以包括因子参数、调优结果等，有助于更深入地理解策略的表现。

---

### 评论 #80 (作者: YT47842, 时间: 2年前)

补充重跑之后的截图

提交之前 
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> 文件
> 编辑
> 视图
> 历史记录
> 书签
> 个人资料
> 标签页
> 窗口
> 帮助
> 88字
> 曰
> 0 ? Q 8
> 1月278周六  18:02
> Price Volu
> X
> Operators
> X
> WorldQua
> X
> WorldQua
> 义
> 英才候选)
> 义
> WorldQua
> X
> BRAIN AP
> 义
> 8
> ipynb
> > G  命
> @
> platform.worldquantbrain.comlalphaslunsubmitted
> 馆  Keras入 门必看教程
> Keras中i文 文档
> 知
> Keras教程
> Python教程 -廖雪.
> 深度学习从小白到.
> Keras教程_腾讯视频
> 所有书签
> 变量
> 泛大纲
> Python 3.11.5
> WORLDQUANT
> s 》 D 曰
> BRAIN
> Simulate
> Alphas
> Data
> Competitions (2)
> Events
> Learn
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> 种类
> Show
> 10
> out of 2,069
> Filter
> PNG 图像
> PNG图像
 这里是提交1080次之后的结果 
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> 文件
> 编辑
> 视图
> 历史记录
> 书签
> 个人资料
> 标签页
> 窗口
> 帮助
> 584字
> 88s
> 曰 吻 令 Q &
> 1月278周六  23:19
> Pric
> 义
> Opr
> 义
> Wo
> X
> Wo
> X
> 英 X
> Wo X
> 英 X
> BR
> X
> Q
> Connec
> python
> 侣
> > G 命
> 9
> platform.worldquantbrain.comlalphas/unsubmitted
> G   区
> ABP
> Dynb
> 馆  Keras入 门必看教程
> Keras中 文文档
> 知 Keras教程
> Python教程 -
> 廖雪。
> 深度学习从小白到.
> Keras教程_腾讯视频
> 所有书签
> 到
> 娈量
> :大纲
> Python 3.11.5
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Data
> 鬯 Competitions (2)
> EVents
> Learn
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 10
> out of 3,149
> Filter


---

### 评论 #81 (作者: YW27566, 时间: 2年前)

（1）开始simulation前的截图

```

```

（2）simulation后的截图，完成1000+


> [!NOTE] [图片 OCR 识别内容]
> 0
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 1,201
> Show
> 10
> Out
> Filter
> Unsubmitted:
> 1,189
> Active:
> 12
> 0
> Select Columns
> ItUS
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> @.8〉1
> e8〉1
> e8〉1
> Select
> anorymoUs
> RegWIaT
> JNSUBMITTED
> 01/27/2024 EST
> USA
> T0P3000
> 0.10
> 0.529
> 10.189
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> TOP3000
> 0.17
> 0.739
> 1.489
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> TOP3000
> 0.00
> 0.019
> 4.249
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> TOP3000
> -0.02
> -0.069
> 9.689
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> T0P3000
> -0.10
> -0.459
> 2.609
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> T0P3000
> -0.43
> -2.049
> 6.949
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> TOP3000
> 0.07
> 0.389
> 10.949
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> TOP3000
> -0.52
> -2.019
> 10.459
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> TOP3000
> -0.10
> -0.459
> 2.26%
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> USA
> T0P3000
> -0.24
> -1.129
> 8.799
> 1:36
> Type here to search
> 司  〈$  中 S
> 昆
> 2024/1/28
> Tag
 （3）在跑代码的过程中，每次测试都会计数来显示代码完成的进度，中间连接中断会自动重新登录账号，重新连接并且重新进行模拟测试并显示retry alpha simulation


> [!NOTE] [图片 OCR 识别内容]
> COIIDLete
> testlng alpha: rank (anLL3_CDSgICS_gr
> 12_皿_St_deV )
> rlnning alpha
> 834/2538
> AIpha qgrgrJj
> done simulating;
> getting alpha details
> complete testing alpha:rank (anlI5_dps_ind_cal_fyO_gro)
> running alpha
> -835/2538
> Alpha eLwmWj done simulating;
> getting alpha details
> complete testing alpha:rank (anl15_Cpsgics_S_18_皿_6皿_chg)
> running alpha
> 一-836/2538
> Alpha NAmOVgE done simulating;
> getting alpha details
> complete testing alpha:rank (anl15_dpsgics_gr_cal_fyl_ests
> running alpha --837/2538
> Alpha BxOGEZe done simulating;
> getting alpha details
> complete testing alpha:rank (anl15_Cpsgics_gr_12_皿_total)
> rlnning alpha
> -838/2538
> Alpha Kkd3j6x done simulating;
> getting alpha details
> coplete testing alpha:rank (anll5_Cpsgics_S_ 18_皿_Cos)
> running alpha
> -839/2538
> Alpha Ek『lYaJ done simulating,
> getting alpha details
> complete testing alpha:rank (anl15_dps_ind_cal_fyO_pe
> running alpha
> -840/2538
> already complete 840 alpha;rest
> 2s
> Alpha XIQGSSb done simulating;
> getting alpha details
> complete testing alpha:rank (anl15_cpsgics_gr
> 12_皿_tr_mean)
> running alpha
> 一-841/2538



> [!NOTE] [图片 OCR 识别内容]
> O ]
> omplete testing alpha:rank (anlI5_cpsgics_S
> 18_皿_ests_dn)
> unning alpha
> 857/2538
> Onnection aomn
> etry alpha simulation
> onnection domn
> etry alpha simulation
> onnection dom
> etry alpha simulation
> onnection dom
> etry alpha simulation


（4）总结

在代码效率提升方面，采用了multiprocessing多进程的方式同时跑多个进程来提高运行效率。通过共享内存变量来同步不同进程使用的公共计数变量和记录如果没跑通发生错误的变量list。debug方面，如果alpha没跑通就执行alpha_id = simulation_progress.json()["alpha"]会报错，所以在执行这个语句之前加入了状态查看，status=simulation_progress.json()['status']，如果显示fail就会记录错误并跳过。通过get_alpha_perform_rst函数记录下每个alpha的表现便于最后查看结果。


> [!NOTE] [图片 OCR 识别内容]
> def
> _alpha_perform_rst (alpha_detail , datafield_name) :
> alphazalpha_detail[ 'id' ]
> alpha_func=alpha_detail[ 'regular
> [
> Code
> dic_perform={ 'alpha
> alpha_func,
> datafield ' :datafield_name,
> sharpe
> alpha_detail[ 'is ' ][ 'sharpe'],
> fitness
> alpha_detail[
> is ' ][ 'fitness'],
> drawdown
> :alpha_detail [
> is ' ][ 'drawdown'],
> turnover
> alpha_detail[ 'is ' ][ 'turnover'],
> peturn
> alpha_detail [ 'is' ][ 'returns' ]}
> df_perform=pd .DataFrame ( [dic_perform] , index=[alpha] )
> return
> df_perform
> get


在模板使用上，只单纯用了rank函数为了测试跑通整个框架。直接用esg数据和eraning forecast数据表现不佳，forecast数据略好，之后可以尝试用不止用截面上的函数表达式，可以尝试时间序列上的函数如ts_rank，并尝试和其他信息结合构造出新的alpha提升效果。

---

### 评论 #82 (作者: FZ15092, 时间: 2年前)

在本次完成本次作业的调试与实际运行过程中共提交了约1500次测试

1. 代码测试与运行前


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Total: 451
> Unsubmitted。
> 436
> Active:
> 15
> Oh
> Decommissioned:
> Alpha Lists
> 20:59
> 4x 英
> 2024/1/27
> 昂


2. 测试与运行后：


> [!NOTE] [图片 OCR 识别内容]
> 0
> Alphas
> Total: 1,940
> Unsubmitted。
> 1,925
> Active:
> 15
> Oh
> Decommissioned:
> Alpha Lists
> 5:54
> 臼
> 4x 英
> 2024/1/28
> 昆


3. 代码截图

由于我的个人原因这次作业完成的较为仓促，在基本跑通代码后我优先对1000次simulate的任务进行了实现，以免剩余时间不足以及可能出现的其他报错处理，在最多线程为10的参数设置下，1000次测试任务的完成时间约40分钟。在完成了测试任务后我又对代码的信息输出部分进行了优化以体现提交进度与报错信息，优化后输出效果如下：（以一次18次的测试为例）


> [!NOTE] [图片 OCR 识别内容]
> 〈Response [201]〉
> datafields done
> Alpha_list done
> 〈Response [201]〉
> submitting alphas:
> 180%
> 18/18[80:88〈80:80,
> 1016.g1it/s]
> Alpha
> (advzo-ts_delay (advzo, 20) ) /advzo submitted successfully,
> result: <Response [201]〉
> Alpha
> (open-ts_delay (open, 20) ) /open
> submitted successfully,
> result:
> <Response [201]〉
> Alpha
> (returns-ts_delay (returns, 28) ) /returns  submitted successfully,
> result:
> <Response [201]〉
> Alpha
> (industry-ts_delay (industry, 20) ) /industry submitted successfully,
> result: <Response [201]〉
> Alpha
> (country-ts_delay (country, 20) ) /country submitted successfully,
> result: <Response [429]〉
> Alpha
> (market-ts_delay (market, 20 ) ) /market
> submitted successfully,
> result:
> <Response [201]〉
> Alpha
> (Iow-ts_delay (Iow, 28) ) /low submitted successfully,
> result: <Response [201]〉
> Alpha
> (cap-ts_delay (cap, 20) ) /cap submitted successfully,
> result:
> <Response [201]〉
> Alpha
> (high-ts_delay (high, 20) ) /high submitted successfully, result: <Response [201]〉
> Alpha
> (exchange-ts_delay (exchange, 20) ) /exchange  submitted successfully, result:
> 〈Response [201]〉
> Alpha
> (dividend-ts_delay (dividend, 28) ) /dividend
> submitted successfully,
> result:
> 〈Response [201]〉
> Alpha
> (volume-ts_delay (volume, 20) ) /volume submitted successfully,
> result:
> <Response [429]〉


4. 总结反思

在代码效率方面，Alpha提交的效率在多线程运作下已经相对较快，但我尚未对参数进行更多尝试寻找实现最优运作效率的参数，此方面也许仍有提升空间

在debug的过程中，我通过程序报错发现一个dataset的id可能对应几个不同的dataset，而在网页端搜索只能搜索到其中的一条，希望老师能够帮助解释一下这个问题


> [!NOTE] [图片 OCR 识别内容]
> id
> name
> description
> category
>  subcategory
> region
> universe
> coverage
> This is a
> Global
> global
> fundamental-
> 76
> fundamental28
> Fundamental
> fundamental
> fundamental
> fundamental-
> USA
> TOP3000
> 0.8773
> Data
> dataset
> data
> providing.
> Thisis a
> Global
> fundamental-
> 77
> fundamental28
> Fundamental
> fundamental
> fundamental
> fundamental-
> USA
> T0P3000
> 0.7760
> Data
> dataset
> data
> providing..
> This is a
> Global
> global
> fundamental-
> 78
> fundamental28
> Fundamental
> fundamental
> fundamental
> fundamental-
> USA
> TOP3000
> 0.7785
> Data
> dataset
> data
> ]
> delay
> global


因子模板方面，我使用了一个反转Alpha作为模板：

```
-(close-ts_delay(close,5))/close
```

，来自于文章《【Alpha灵感】新闻动量文章启发的反转策略实现》老师的评论区回复，老师称之为一个经典的反转策略想法。在老师题目区的想法启发下我选择了基本面数据集来套用此模板，并相应将时间参数拉长至20天（1个月），观测结果后在某些datafield上发现了一些可能存在信号的Alpha，但距离提交仍有一定差距，后续我会尝试进一步进行筛选与优化


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 7,5OOK
> 5,00OK
> 2.5OOK
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


目前在实现Alpha提交以后我还未完成Alpha的测试结果统计与筛选等功能的代码，这方面是我亟待完成的部分，希望老师和同学们多多批评指教

---

### 评论 #83 (作者: JS48146, 时间: 2年前)

运行前后截图和对比：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 3,005
> Total Active Alphas
> 56
> Total Decommissioned Alphas
> Total Alphas
> 3,061
> 533
> 8:11
> -G%C 晴朗
> 入 @ c 英  u
> 2024/1/28
> 昆



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 4,013
> Total Active Alphas
> 56
> Total Decommissioned Alphas
> Total Alphas
> 4,069
> 9:35
> -6%C 晴朗
> 入 @ <英  豳
> 2024/1/28
> 民


阅读了【Alpha灵感】分析师的真知灼见。使用的dataset为Estimations of Key Fundamentals，共包含870个datafields。

遇到问题和设计：

1. Location问题，参考老师在【BRAIN API及日常回测时常见的报错】中的回答，使用if解决。
2. 使用多线程进行simulation，参考之前同学的经验使用了10个线程。在代码中包含这一行，表示对某一个alpha完成了simulation：
3. 
> [!NOTE] [图片 OCR 识别内容]
> with Iock
> result_list. append (result)
> print (f"Finish simulating alpha {str (len (result_list)) }:
> {all_simulationi]}

4. 因为想要使用一个总的dataframe储存所有的alpha的表现，因此使用lock防止不同线程写冲突。
5. 连续运行后的结果:
6. 
> [!NOTE] [图片 OCR 识别内容]
> Finishiilutie ph1979;
> Upe
> REGULIR"
> 912Ts
> i'rumentTp
> EOTTT
> eoh
> TS
> VT
> TnP3nnO
> dl
> UeC8!
> Geurraliztiol
> SUBTTUSTRT
> Truncyto
> Dglelrizition
> UnHardline'
> IERTF}'
> JHyndliq
> laneuaee
> FJSTELPR
> SNRI17A11Nn
> 17150
> reqUlar
> Tank(abs (ts_deltalanlly_stddev_pbitdn_ty; 250111-0
> Finish siulatins alphalgs0;
> tpe
> RECULI'
> SettInys
> Instrumentipe
> BUUIT
> TeCIOI
> USy
> 071'0TSC
> TOp3OOO'
> dela
> 4291
> T1 7
> 4130T0I
> SUBUDUSIR
> TMo
> pastelrizotion
> UnitWadline
> TERIF
> JorHandln
> InquuRe
> BSIEIR'
> Visuolizution
> Pulsel
> regUlr
> Can (abs (s
> 02ltl
> (unll_hieh_roe
> p.250)1
> Finish sitlatine
> 1931
> REGTL IR
> Settinns
> TsUmentTpt
> E0TTT
> PeRion
> 151
> V13
> TOP3DOO
> dela
> UuC!
> TNUI!02HULOI
> SUBIDUSTR
> Uruneotion
> R ourizstion
> uirhurdlin'
> TETF
> Hndl n
> langu e 
> FISTEPR'
> Tslio
> Falso]
> UIL
> dolt (anll_hieh_roe
> 4p50/11-0
> [I]:
> I(result_list)
> Duc
> 1932
> Arhn
> MUIm
> (2


仍存在的问题：

实际simulation并且能够得到表现的alpha有1600+个，但是在alpha平台上看到的结果只增加了1000个，这是为什么呢。

---

### 评论 #84 (作者: PF41122, 时间: 2年前)

1. 最近的截图： 
> [!NOTE] [图片 OCR 识别内容]
> Fri Jan 26 11,33
> 收件1
> 英才
> BRl
> Worl
> Wor
> plattorm worldquantbrain comlalphaslsubmitted
> YouTuoe
> 北圄
> Home
> Solc
> Python
>  [
> Fnanclal EConor
> 鼎"
> Simulate
> Alphas
> 0ata
> Competition:
> Alphas
> Unsubmitted
> Submitted
> Total: 852
> ShOw
> Unsubmitted
> 846
> Aclive
> Select Columns
> DecommissIoned

2. Simulation后截图： 
> [!NOTE] [图片 OCR 识别内容]
> Sat Jan 27
> 20:12
> orldau
> WorldQu
> Worldau
> quantbrain.comlalphaslunsubmitted
> Home
> Solve Python
> Hac..
> Financial;
> nulate
> Alphas
> Data
> Compe
> Unsubmitted
> Submiti
> Total: 2,223
> Unsubmitted:
> 2,217
> Active:
> Decommissioned:
> 0

3. 连续simulate 1000+截图： 
> [!NOTE] [图片 OCR 识别内容]
> CheckedAlpha.to
> /Users/peterfeng /Downloads /orldquant/CheckedAlpha
> indet-False
> passed
> qroup_
> rank (T5_mean (fnd28_Value_182243
> 4881/t5_
> 爪e31
> (5ales_qrowth, 4801,bucket (rank
> Tnd23_
> lue_1822431
> range
> 11
> not
> passed
> 9roup_
> rank(ts_mean ( fnd28_
> 437012
> 18224a
> 6081/ts_
> Ie3n( 53le5_
> rowth, 6001
> bucket ( rank
> fnd28_value_
> 1822431
> range-"0.1,1
> Dot
> pas5ed
> 9roup_
> rank (ts_mean(fnd28_Value_182243
> 7281/ts_Tean (sales_growth, 7201
> bucket (rank
> fnd23_value_1822431
> ranges"0.1,1
> 1"1
> not
> pa55Cd
> 9roup_
> rank (ts_mean
> tnd28_Value_18224a
> 60I/t5
> Tean (sales
> p5,601
> bucket (rank ( +nd28
> value_1822431 , range-"0.1,1,0.1") )
> not passed
> group
> rank (Ts_mcan lfnd28_
> lUC_182243
> 1281/ts_Iean (sales_ps
> 1201
> bUcket
> rank ( fnd28_Value_1822431
> range-
> 0,1,1,0.
> 1"1 
> not passed
> 9roup
> rank (TS_mean
> Tndzo_ValUe_182243
> 1881/t5_Tean ( 53le5_
> 1801
> bUcket
> rank
> Tndzp_Value
> 1822431
> range
> 0.1,1,0.
> 1"1 1
> not passed
> qroUp
> 「ank(TS
> mean
> fndz8_
> ValUe_18224a
> 2521/ts_Iean (sales_Ds
> 2521
> bUCket
> 「ank(Tnd2g_Value
> 18224a1
> range=
> 1,1,0.
> not passed
> LO「OUP
> rank (TS_mean (fndz8_Value_182243
> 3681/ts_Iean (sales_Ds
> 3601
> bucket ( rank ( fndz8_Value
> 1822431
> range
> .11,0.
> 1"1 1
> not passed
> 5T3TT
> Working
> 1150
> 1159
> 26/81/2024 22:13:26
> Multisimulation
> request Sent SUCCeSSfully

4. 实现功能：除了基本的寻找datafield，multisimulation， check，comparison等functions外，还收集了所有simulations的结果数据，方便后期手动筛选或分析。并且simulation的结果和对应的时间会实时更新，方便追踪进度以及前期debug。
5. 代码效率：因为加了一些额外的功能，所以跑10个alpha/组的时间大概在1分半，跑1000个alpha大概在2个多小时。
6. debug经历：发现有些datafield会报错，目前的处理方法是，先simulate一遍选好的datafield，把不会报错的做成alpha expression。当然还发现中途如果电脑进入屏幕保护状态，connection会断开，并一直尝试重连，重新进入界面之后会重新连接，继续开始simulation，所以之后就取消了屏幕保护。
7. 模板适合的数据类型：模型取自 [alpha idea 看不见的负担]([L2] 【Alpha灵感】 看不见的负担_19137319051671.md) 。先通过pv13_h2_sector进行分组，然后通过goodwill和sales的比值构建alpha。目前的做法就是将goodwill和sales相关的能用的datafield进行组合来simulate，但还有疑问的就是vector或者matrix等不同的数据类型对simulation结果的影响，或者是否需要做单独的处理呢？因为是fundamental的数据，目前时间节点有按quarter设置，但尚不明确每个datafield数据的frequency以及最早的availability，应该也会影响simulation的结果。

1. 模板的改进方向：观察simulation的结果发现，ts_mean的时间取一年以内能获得更好的表现，所以下一步simulation可以将时间范围缩小到一年内。并且加入一些短期的数据是会有利于提高sharpe的，idea原文中有提到close，或许vwap，volume等也是可以尝试的。

---

### 评论 #85 (作者: 顾问 KZ79256 (Rank 21), 时间: 2年前)

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

### 评论 #86 (作者: WL13229, 时间: 2年前)

[JS48146](/hc/en-us/profiles/16529616166551-JS48146)

如果一个Alpha之前被你simulated过，它就不会在面板上增加次数了

---

### 评论 #87 (作者: EH13432, 时间: 2年前)

作业提交：

由于期末考试的原因，上次训练营只参加了先导课内容。任务已经在上次中提交，这里放一个结果，其他不再重复


> [!NOTE] [图片 OCR 识别内容]
> world_quant
> 6
> EXPLORER
> main.py
> try.ipynb
> tryipynb
> X
> worldquant_func.py
> Apidataset ipynb
> WORLD_QUANT
> 972
> Alpha done simulating, getting alpha details
> LPycache
> 973
> Alpha done simulating, getting alpha
> details
> 974
> Alpha done simulating, getting alpha
> details
> Api.ipynb
> 975
> Alpha done simulating, getting alpha
> details
> Apidataset.ipynb
> 976
> Alpha done simulating, getting alpha
> details
> is评价 Xlsx
> 977
> Alpha done simulating, getting alpha
> details
> sentiment.XlsX
> 978
> Alpha done simulating, getting alpha
> details
> tryipynb
> 979
> Alpha done simulating, getting alpha
> details
> 980
> Alpha done simulating, getting alpha
> details
> worldquant_func.py
> 981
> Alpha done simulating, getting alpha
> details
> 982
> Alpha done simulating, getting alpha
> details
> 983
> Alpha done simulating, getting alpha
> details
> 6
> 984
> Alpha done simulating, getting alpha
> details
> 985
> Alpha done simulating, getting alpha
> details
> 986
> Alpha done simulating, getting alpha
> details
> 987
> Alpha done simulating, getting alpha
> details
> 988
> Alpha done simulating, getting alpha
> details
> 989
> Alpha done simulating, getting alpha
> details
> 990
> Alpha done simulating, getting alpha
> details
> 991
> Alpha done simulating, getting alpha
> details
> 992
> Alpha done simulating, getting alpha
> details
> 993
> Alpha done simulating, getting alpha
> details
> 994
> Alpha done simulating, getting alpha
> details
> 995
> Alpha done simulating, getting alpha
> details
> 996
> Alpha done simulating, getting alpha
> details
> 997
> Alpha done simulating, getting alpha
> details
> 998
> Alpha done simulating, getting alpha
> details
> 999
> Alpha done simulating, getting alpha
> details
> 1000
> PROBLEMS
> OUTPUT
> DEBUG CONSOLE
> TERMINAL
> PORTS
> JUPYTER
> ^
> X
> /usr/local/bin /python3
> /Users/easonhao /Documents /py_Work /world_quant /worldquant_func. py
> ZSh
> (base) easonhao@EasondeMacBook-Pro world_quant % /usr/local/bin/ python3 /Users/easonhao /Documents/py_work/world_quant /worldquant_func.py
> <Response
> [201]>
> Python
> (base) easonhao@EasondeMacBook-Pro World_quant %
> QUTLINE
> TIMELINE
> 0^ 1
> Ln 1, Col 1
> Spaces: 4
> Plain Text


本次主要是进行了一些修补工作——首先改进了一下我的多重模拟函数，主要在传递参数上，我把每一个可能输入的部分全部用列表形式表达。函数中会自动遍历所有参数组合后的alpha。

另外还是在解决上次任务留下来的一些遗留问题。比如在生成is评价表和self- performance评价表时会出现jsondecodeerror：老师提供的想法很有帮助——使用try except确保json的解析可以规避问题


> [!NOTE] [图片 OCR 识别内容]
> for
> in ids:
> url
> "https: /Lapi.worldquantbrain,Com
> While
> True:
> try:
> b=s.get (url. format (i) )
> is_result=b.json()
> is_result ["id"]=i
> is
> check.append (is_result)
> break
> except JSONDecodeError:
> time.sleep (0.1)
> pass
> # 遍历结果字典列表


这是目前实现的结果，希望多多指教

---

### 评论 #88 (作者: SK24143, 时间: 2年前)

感谢worldquant平台的课程！

由于代码还没有跑完，先放个运行截图，后续补上


> [!NOTE] [图片 OCR 识别内容]
> UnsUbmltted
> SUbmItted
> Hipna DIstrIbutlon
> u
> Hipna LIsts
> Total: 1,125
> OUt
> Filter
> Unsubmitted:
> 1,113
> Active:
> 12
> ItUS
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> e.8>1
> e.8>1
> e.8>1
> Select
> anonymoUs
> RegWIaT
> UNSUBMIT。
> 01/27/2024 EST
> CHN
> TOP3000
> -0.57
> -7.529
> 7.8396
> anonymous
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.30
> -3.909
> 8.529
> anonymoUs
> Regular
> UNSUBIIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.05
> -0.449
> 7.619
> anonymous
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.69
> -9.349
> 8.169
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.06
> -0.709
> 8.199
> anonymoUs
> Regular
> UNSUBMIT.
> 01/27/2024 EST
> CHN
> TOP3000
> -0.06
> -0.569
> 8.199
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.56
> -7.129
> 8.009
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.75
> -5.929
> 7.829
> anonymous
> Regular
> UNSUBMIT。
> 01/27/2024 EST
> CHN
> TOP3000
> -0.37
> -5.149
> 8.329
> 7.25
> Q 搜索
> X
> 岛  英
> 谷 dj l
> 2024/1/28
> Tag
> ?;



> [!NOTE] [图片 OCR 识别内容]
> Alpha
> done simulating。 getting alpha
> details
> 20%
> 235/1200[10:39<40:53,
> 2.54s/i]
> AIpha
> done
> simulating, getting alpha details
> Alpha
> done simulating, getting alpha
> details
> 20%
> 239/1200[10:44〈30:22,
> 1. 90s /i]
> AIpha
> done
> simulating, getting alpha details
> 20%
> 240/1200
> [10:44<26:47
> 1.67s/让]
> AIpha
> done simulating, getting alpha
> details
> Alpha
> done simulating, getting alpha
> details
> 20%
> 243/1280
> [10:51<28:17 ,
> 1.775/让]
> AIpha
> done
> simulating, getting alpha details
> Alpha
> done simulating, getting alpha
> details
> 20%
> 245/1200[10:56〈32:00,
> 2.0Is /i]
> AIpha
> done simulating, getting alpha details
> 20%
> 246/1200 [10:57<27:07,
> 1.715/让]
> AIpha
> done simulating, getting alpha
> details
> 21%
> 247/1200[11:00〈33:43,
> 2.125 /i]
> AIpha
> done simulating, getting alpha
> details
> AIpha
> done simulating, getting alpha
> details
> Alpha
> done simulating, getting alpha
> details
> Alpha
> done simulating, getting alpha
> details
> AIpha
> done simulating, getting alpha details
> 21%
> 248/1200
> [11:11<1:10:26,
> 4.44s/i]
> Alpha
> done simulating, getting alpha
> details
> 21%
> 253/1200[11:14〈30:32,
> 1.935/i]
> Alpha
> done
> simulating, getting alpha
> details


由于自己是计算机小白，所以在代码方面向其他同学有所借鉴。使用的是多线程concurrent.futures，maxworker=10.

使用的模板是最近提交的一个因子的模板，想看一下有没有更多这样的关系，当然表达式是很简单的zscore(ts_regression({id},fnd27_s_fa_eps_diluted_valueadj,30,rettype=2))，这里选取的数据集是fundamental27的matrix类型的数据。本次进行1200次的模拟，使用的CHN市场，delay=1.

思考与总结：目前只是使用一个数据字段，而没有很多的数据同时输入，所以模型较为简单，也主要起到一个测试的作用。这个模板应该是泛化能力还可以的，但是可能单独这个模板达不到平台提交的标准，之后可以尝试更复杂的模型。要更多地总结论文研报以及其他同学的思路，以及可以恰当的使用大语言模型进行研究。

补充结果，用时80分钟，由于选取的模板不是太好，导致基本没有很好的因子，今后会在模板构建上下功夫，以下为simulate1200次之后的截图。


> [!NOTE] [图片 OCR 识别内容]
> a5
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 2,694
> OUt
> Filter
> Unsubmitted:
> 2,682
> Active:
> 12
> mns
> ItUS
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> e.8>1
> e.8>1
> e.8>1
> Select
> anonymoUs
> RegwIar
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.23
> -2.999
> 7.839
> anonymoUs
> Regular
> UNSUBMIT.
> 01/27/2024 EST
> CHN
> TOP3000
> -0.49
> -6.979
> 7.639
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.04
> -0.639
> 8.779
> anonymoUs
> Regular
> UNSUBMIT。
> 01/27/2024 EST
> CHN
> TOP3000
> 0.10
> 1.289
> 7.569
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.56
> -8.129
> 8.709
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.79
> -5.599
> 8.089
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.13
> -1.069
> 6.799
> anonymoUs
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.55
> -4.129
> 7.129
> anonymous
> Regular
> UNSUBMIT
> 01/27/2024 EST
> CHN
> TOP3000
> -0.56
> -8.019
> 8.279
> Itbrain.com 的响应。
> 13:27
> Q 搜索
> F
> 中  谷 d) 匈
> 2024/1/28
> Tag


---

### 评论 #89 (作者: YZ64617, 时间: 2年前)

模拟前


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> Out 0T
> 758
> Filter
> Select Columns
> Name
> Competition
> Iype
> Status
> Date Created (ESTI
> Region
> Universe
> Color
> Sear-h
> SPI
> SPI
> SPI
> Search
> SPI
> SPI
> SPI
> SPI
> aOnYMOUS
> Regular
> UNSUBWIITTED
> 0112712024 EST
> CHN
> TOP3OOD
> aORYMOUS
> Regular
> UNSUBWITTED
> 01'2712024 EST
> CHN
> TOP3OOD
> AnORyIOUS
> Regular
> UNSUBWIITTED
> 0112712024 EST
> CHN
> TOP3OOD
> aORYMOUS
> Regular
> UNSUBWITTED
> 01'2712024 EST
> CHN
> TOP3OOD
> aOnYMOUS
> Regular
> UNSUBWITTED
> 0112712024 EST
> CHN
> TOP3OOD
> Tag


模拟后，


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitte
> Total: 15,091
> Show
> Out 
> Unsubmitted
> 15,089
> Active:
> Select Columns
> Decommissioned:


这次一共模拟了5300多个alpha，耗时6小时


> [!NOTE] [图片 OCR 识别内容]
> 388m 50.2s
> 100%
> 5312/5312
> [6:28:48<00:00
> 4.395/i]
> completed


### 编程方面

我的步骤是

1. 抓取datafield，写了一个针对settings和dataset.id的函数，并将结果保存成csv格式
2. 使用template批量生成alpha。
3. 批量simulate所有alpha。这个过程，会处理token过期和错误。同时，将成功和失败的都记录成log，保存。
4. simulation过程，是没有alpha ID的，但是会有simulation ID。simulation ID都在第3步记录下来，生成一个URL。GET 这些url，获得alpha id/、。【遇到的问题】simulationID似乎超过一定时间就会不存在，所以，simulate了6个小时，早晨起来，进行后续的时候，alpha id很多已经无法获取了。但是，如果是短时间simulate，这个方法是没有问题的。
5. 使用alpha id，读取alpha的表现。

### 关于token过期和意外链接失效的问题的处理：

- token有效期4小时，14400秒。所以，在每simulate一个alpha的时候，检查一下是否超过一个值（例如，14000秒），如果超过，则重新生成token。
- 对于一些异常，使用try处理。


> [!NOTE] [图片 OCR 识别内容]
> def post_simulation_lists (df
> tk :
> Urs
> get_
> Zoken ( )
> Start_time
> datetime.now (1
> for
> tqdm(range (len (df)] )
> nOW_tine
> datetime.now ( )
> delta
> time
> nOW_time
> start
> time
> delta
> time
> Cconds
> 14000:
> Start_Cime
> Jatetime.now (
> get
> token()
> while
> True
> try:
> Url
> DO5t
> simulation leval(df.iloc [1] ['settings']1,
> iloc [1] ['regular'],
> tk)
> break
> except
> continue
> UrLS.append
> Urll
> return Urls
 我写了一个simulate单个alpha的函数和一个批量simulate的函数。批量simulate函数中，加入了token过期和异常处理。

我的token方式和Brain API的不同。这个是很早很早之前写的，所以就保留了下来。后期，考虑结合Brain API的session方式，对代码进行调整。

### 遇到的问题和思考

1. simluation ID的失效问题。

针对这个解决方法是， [https://api.worldquantbrain.com/users/self/alphas](https://api.worldquantbrain.com/users/self/alphas) ? ➕时间filter条，直接抓起alpha的信息。

除此之外，还可以通过Brain 平台的个人alpha页面进行filter。 [https://platform.worldquantbrain.com/alphas/unsubmitted](https://platform.worldquantbrain.com/alphas/unsubmitted)

但是，似乎Brain 平台有bug或者限制。在网页端，我无法通过performance筛选，也无法把performace显示出来。如图


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Summary
> Propertles
> Settings
> Performance
> Wme
> SzatUs
> Region
> Insrument Type
> Competition
> Category
> Universe
> Delay
> Type
> Color
> Deca
> Weutralization
> LaRBUJBC
> Tag
> Truncation
> Unit Handling
> Daze Created (ESTI
> Hdden
> NaN Handline
> Pasreurzation
> Favorite
> Reset
> Apply


由于遇到这几个特殊情况，目前还无法看到所有的5300个alpha的表现，需要对代码进行再加工。

2. 数据集和模版

我这次使用的是 model122， CHN Vector数据，D1。公式模版是单参数的，所以，并不抱很大希望有可以提交的。公式模版如下


> [!NOTE] [图片 OCR 识别内容]
> def generate_Iax(a:
> Outl
> f"-max (ts_
> ZSCOre (Vec_avg ({a}),51.
> -11"
> Outz
> f"max(ts_
> ZSCOre (Vec_avg({a}1,51,
> 11"
> Out3
> f"rank (Vec_avg({a}1)
> Out4
> f"_rank (vec_avg ( {a}) )"
> outs
> f"ts_rank (vec_avg ( {a}) ,51"
> out6
> rank(vec_avg({a}) ,51"
> out7
> Scalelts_rank ( (vec_avg( {a}) ),51,51"
> Outg
> SCalelts_rank(IVeC_
> avg({a}) ),51,51"
> Outg
> scale (rank(vec_avg ({a}) ),51"
> Outl0
> fw_ts
> Scale (rank (Vec_avg ( {a})1,51
> outll
> f"-Scale_down (rank (Vec_max({a}1  )
> Out1z
> f"scale_down
> rank(VeC
> Nax({a}11 
> Out13
> f"signlts_
> delta lvec_avg ({3}),51 )"
> out14
> f"-signlts_
> delta lVec_avg ( {a}),51 )'
> out15
> f"rank (-ts_delta(Vec_avg ( {a}),51)"
> Outl6
> f"-rank (-ts_
> delta(VeC
> avg ( {a}],511"
> return
> outly_outz
> Out3
> Out4, _
> Out5
> Out6
> Out7
> OUT8
> outg
> Outl0 
> Outll
> Out12
> 0ut13
> 0UC14
> out15
> OUtl6]
> fw_ts
> fw_ts
> f"15
> f"t5


计划任务

- 程序方面，需要再优化。例如，simulate+alpha结果这个过程，alpha结果的后续处理等。
- alpha模版方面：需要针对不同类型的dataset/datafield，使用对应的更有效的模版。这就涉及到，dataset的探索
- 每一个datafield都有它自身的各种特点。考虑将论坛的提到的6种方法加进去。也考虑做一个本地dataset的保存，方便自己打标签和快速读取。

---

### 评论 #90 (作者: DZ54968, 时间: 2年前)

1 最近的截图


> [!NOTE] [图片 OCR 识别内容]
> RLDQUANT
> RNN
> Simulate
> Alphas
> Data
> 留 Competitions (3)
> Events
> Learn
> y Refer a friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 4,241
> Show
> 10
> out
> Filter 
> Unsubmitted:
> 4,208
> Active:
> 33
> Select Columns
> ItUs
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> 0
> Plect
> Search
> Select
> Select
> erg〉 1
> e8> 1
> erg〉 1
> Select
> aTOTYIOUS
> RegOIaT
> UNSUBMITTED
> 01/26/2024 EST
> CHN
> TOP3000
> 3.59
> 10.1696
> 6.939
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> CHN
> TOP3000
> 3.59
> 10.179
> 6.889
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> CHN
> TOP3000
> 3.59
> 10.169
> 6.939
> anonymous
> Regular
> UNSUBMITTED
> 01/26/2024 EST
> USA
> TOP3000
> 0.57
> 1.389
> 6.459
> anonymous
> Regular
> UNSUBMITTED
> 01/02/2024 EST
> USA
> TOP3000
> 0.26
> 2.489
> 10.469
> anonymous
> Regular
> UNSUBMITTED
> 01/02/2024 EST
> USA
> TOP3000
> 0.44
> 4.499
> 8.149
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> USA
> TOP3000
> 0.53
> 4.489
> 1.189
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> USA
> TOP3000
> 0.80
> 3.739
> 6.669
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 0.96
> 8.619
> 4.299
> anonymous
> Regular
> UNSUBMITTED
> 01/01/2024 EST
> CHN
> TOP3000
> 0.16
> 2.369
> 35.479
> Show
> 10
> out Of 4,208
> Oe
> 421
> Next
> 5
> 15:04
> Q 搜索
> 吆
> 入
> n  G
> 谷 d 匈
> e
> 2024-01-26


2 回测1000+次后截图


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAN
> Simulate
> Alphas
> Data
> 留 Competitions (3)
> Events
> Learn
> Refer a friend
> 0
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 5,342
> Show
> 10
> 0Ut
> Filter
> Unsubmitted:
> 5,309
> Active:
> 33
> Select Columns
> ItUs
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> Flect
> Search
> Select
> Select
> e.吕>1
> e.吕>1
> e.吕>1
> Select
> JTIOTIJTTOUS
> ReBUIaT
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 0.01
> 0.0696
> 14.019
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.95
> -4.689
> 16.8396
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -1.83
> -12.259
> 12.2896
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 0.18
> 1.429
> 14.7296
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 0.22
> 1.759
> 21.0996
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.76
> -5.6896
> 20.4096
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.17
> -1.379
> 20.1696
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 0.94
> -7.8296
> 21.4296
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.81
> -6.2796
> 19.8796
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.89
> 6.539
> 20.0696
> Show
> 10
> out Of 5,309
> Prev
> 531
> Next
> 533
> CNYIJPY
> 12:24
> +0.239
> Q 搜索
> ^  申  S
> 谷 4x 匈
> 2024-01-28  昼
> Tag


3 连续提交1000+Alpha截图


> [!NOTE] [图片 OCR 识别内容]
> type
> REGULAR'
> settings
> istrumentIype
> EQUIII'
> region
> CII
> lniverse
> I0P3000'
> delay'
> decay'
> Ieutralization'
> IMDLSIRI'
> truncation
> 0.08,
> pastelrization
> ON'
> llitHandl
> TERIFI'
> nanlandl
> OFF
> language
> FASTEIPR'
> Visualization
> False;
> regular
> 1' delta
> 0.8; theta
> 1;Iarket
> Letllrn
> SLOUD
> mea11 ({1},
> market ) ; sigma
> abs ({1}
> narket_retlrn)
> (abs ({1})
> Simlation_-esDOIse
> DOst
> https: //api
> WOIIdquantbrain. Com/simulations'
> jsor-simulation_data)
> 1
> 十 ]
> print (1" 己完成第{j}次测试" )
> except
> Drint ( colnection
> domn
> S151_in0)
> 〈Response
> -2011〉
> 己完成第1次测试
> 己完成第2次测试
> 己完成第3次测试
> 己完成第4次测试
> 己完成第5次测试
> 己完成第6次测试
> 己完成第7次测试
> 己完成第8次测试
> 己完成第9次测试
> 己完成第10次测试
> 己完成第11次测试
> 己完成第12次测试
> 己完成第13次测试
> 己完成第14次测试
> 己完成第15次测试
> 己完成第16次测试
> 己完成第17次测试
> 己完成第18次测试
> 「 `[
> ing
> ing



> [!NOTE] [图片 OCR 识别内容]
> SCC LIII53
> istrumentIype
> EQUIII'
> region
> CH'
> lniverse
> I0P3000'
> delay'
> decay'
> Ieutralization'
> IIDLSTRI'
> truncation
> 0.08,
> pastelrization
> 01'
> ulitHandling'
> TERIFI'
> nanfandling'
> OFF
> language
> FASTEIPR'
> Visualization'
> False
> regllar'
> 1' delta
> 0.8; theta
> 0.1 ;Iarket_return
> Sroup_mean ( {1},
> market ) ; sigma
> abs ({1}
> narket_return)
> (abs ({1})
> 十 {
> Simlation_-esDOIse
> D0S
> https : //api. wor Idquantbrain. Com/ simulations
> json=simlation_data)
> 二 j
> 十 ]
> print (1" 己完成第{j}次测试" )
> except:
> Drint (' connection
> domn
> SisI_in()
> 己完成第1084次测试
> 己完成第1085次测试
> 己完成第1086次测试
> 己完成第1087次测试
> 己完成第1088次测试
> 己完成第1089次测试
> 己完成第1090次测试
> 己完成第1091次测试
> 己完成第1092次测试
> 己完成第1093次测试
> 己完成第1094次测试
> 己完成第1095次测试
> 己完成第1096次测试
> 己完成第1097次测试
> 己完成第1098次测试
> 己完成第1099次测试
> 己完成第1100次测试
> 己完成第1101次测试
> 己完成第1102次测试


4 总结反思

代码效率：选取datafield的数据进行挖掘时可以先关注原策略表达式本身数据具有什么特征，通过category等先进行预筛选，避免测试许多无用数据字段。

debug经历：使用API测试Alpha的过程中注意表达式换行空格等问题出现的报错

模版适合的数据类型：本次选取的是ALPHA灵感中凸显理性因子STR，在进行API挖掘时，手动在brain平台中精炼表达式对后续machine挖掘alpha具有重要作用。在测试原策略表达式时，对于用于计算的核心字段returns，先手动替换为volume、turnover（volume/sharesout）等量价层面相关的字段进行测试，观察相关类型数据字段的回测结果。再考虑使用fundamental等其他类型的字段进行测试。观察各类型测试结果后再在使用api时提取对应的datafield进行测试，能够对所做策略具有更深的理解并提高alpha挖掘效率

模版的改进方向：在数据字段替换层面，可以考虑使用双循环或多循环替换不同位置的数据字段，找出最优组合

---

### 评论 #91 (作者: DK85731, 时间: 2年前)

2401 作业提交 （网络问题提交延迟）


> [!NOTE] [图片 OCR 识别内容]
> Mph]
> [
> LIhyIT[
> NIhNOLT
> 0Uea3
> IO
> 1To
> ISTT
> 1m
> OI
> 1547MIOT
> ST
> N



> [!NOTE] [图片 OCR 识别内容]
> T035
> Nalruh
> NUU
> 1: Solio
> II
> TCo
> IISM「l
> U
> IIm2] Fl
> UT
> 1
> LU] [T
> 114212 [
> T
> 32521171
> ITaM
> 2a*|7



> [!NOTE] [图片 OCR 识别内容]
> AULTaet
> CNJU
> JTalt
> OoaA
> OtTIR
> Tl
> 
> N+
> O
> T
> Md( 
> T
> T
> OC5
> Trent
> TUOI
> Tqm(Ii):
> TIICRTTNP
> Reaco (CUTCeN
> TDIIR/
> O
> 118
> LlLUCCUpIe ITJu
> SLRJLUCJU euse
> 041/ULUeLLICCVUkLCD
> 1[
> SJI
> CCutJtu
> uLIOsIMUJutJUItToe
> CCUTet
> LumJ]
> ULULaUL esont
> [0
> TIOUO:
> Cl
> stott(occwpied_Iilil:
> CCUMI
> 11 ,Rp
> 0
> Qm
> 18+13
> 49 5Ta
> N
> I;ol
> 865
> @17
> Uu
> aatll
> Sl
> NT
> O/touu [OO:e; 14]
> 77
> 742
> 2+2s1N]


1. 总结反思，需包含至少四个方面的反思：代码效率、debug经历、模板适合的数据类型、模板的改进方向。多写不限，字数不少于300字。

代码效率：由于multiprocessing与ipynb兼容性较差，thread与windows兼容性较差，暂时采用单线程模式代替方案，设置长度为10的队列，循环检测接口可用性，待有空余时将该消息pop并simulate新factor。之后将用py进行改写以实现多线程效率提升。

Debug 经历：主要处理多线程相关问题，主要问题包括无输出不自动停止运行，且使用multiprocess出现不自动停止的bug时需restart kernel以重启，建议选取已有多线程模式进行修改，或者改用除python外的编程语言

模板合适数据类型：选取 [【Alpha灵感】振幅因子的切割]([Commented] 【Alpha灵感】振幅因子的切割.md)  作为模板来源，检验参数约束条件，确定参数迭代方向进行grid test

总结模板的改进方向：经过1000次simulation，发现同一idea下sharpe浮动空间在-1与1之间，但选取同类factor有可能改善回报与相关性，之后应该将同类因子放进同一框架进行测试

---

### 评论 #92 (作者: JH86905, 时间: 2年前)

1.开始截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 18,738
> Show
> 10
> 0Ut
> Filter
> Unsubmitted:
> 18,540
> Active:
> 186
> Select Columns
> IS
> Date Created (EST)
> Region
> Universe
> Returns
> Turnover
> Tag
> Decommissioned:
> 12
> PCC
> SCarCh
> SCCC
> SCCC
> 2.8 1
> 2.821
> 2.8 1
> Selec
> JTIOTTITIOUS
> ReBTTaT
> ONSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> -0.13
> -2.829
> 7.74%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> 0.68
> 1.90%
> 6.80%
> aCe_
> anonymoUs
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> -0.38
> -1.08%
> 7.16%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> 0.78
> 2.41%
> 9.11%
> aCe_
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> 0.30
> 7.25%
> 7.34%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> 0.28
> 5.589
> 15.789
> aCe_
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> 0.12
> 2.329
> 7.529
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> -0.01
> -0.1196
> 15.30%
> aCe_
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> 0.65
> 1.78%
> 7.65%
> aCE
> _[a,
> anonymous
> Regular
> UNSUBMITTED
> 01/24/2024 EST
> USA
> TOP3000
> -0.64
> -2.73%6
> 5.69%
> aCe_
> Show
> 10
> OUt Of 10,000
> Pov
> 1,000
> Next
> 5
> 09:10
> 搜索
> 5
> yd
> ^
> 中 谷 dx 匈
> NEW
> UV]
> 2024-1-25
> Sharpe
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'


2.API提交后的截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 22,436
> Show
> 10
> 0Ut
> Filter
> Unsubmitted:
> 22,238
> Active:
> 186
> Select Columns
> US
> Date Created (EST)
> Region
> Universe
> Returns
> Turnover
> Tag
> Decommissioned:
> 12
> PCC
> SCarCh
> SCCC
> SCCC
> 2.8 1
> 2.821
> 8.B>1
> Selec
> JTIOTTITIOUS
> ReBTTaT
> ONSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.95
> -3.53%
> 19.53%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -1.18
> -4.5496
> 24.4996
> aCe_
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.80
> -2.8496
> 12.03%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -1.43
> -5.11%
> 15.14%
> aCe_
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.79
> -2.85%
> 13.38%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.81
> -2.9696
> 15.46%
> aCe_
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.34
> 1.21%
> 13.09%
> aCE
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.48
> -1.7496
> 16.45%
> aCe_
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.72
> -2.65%
> 20.55%
> aCE
> _[a,
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> -0.30
> -1.0596
> 10.26%
> aCe_
> Show
> 10
> OUt Of 10,000
> Pov
> 1,000
> Next
> 5
> 15:52
> 搜索
> NFII
> DLV
> 中 。 q) O
> 2024-1-28
> Sharpe
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'
> taS'


3. 连续不断提交Alpha的截图


> [!NOTE] [图片 OCR 识别内容]
> print (time.strftime
> %Y-%m-%d
> %H: %M:%S' ) )
> result
> aCe
> simulate_alpha_list_
> multi(s,
> alpha_list [ :1888] , limit_of_concurrent_simulations=lo )
> print( ' success
> )
> 5
> except
> requests.exceptions . RequestException
> 35
> print(e)
> print (time.strftime (
> %Y-%m-%d
> %H: %M:%5') )
> [25]
> 2gm 53.5s
> 2824-01-28
> 16:83:31
> 188%
> 334/334
> [26:12<80
> 88
> 4.715 /i]
> SUCCeSS
> 2824-81-28
> 16:33:25
> len (result )
> [26]
> 0.Os
> 1888
> try:


4. 参考的论文：基于价量互动的选股因子，实现方式比较简单。先分别计算换手率和单日最高最低价差的滑动均值，再计算差分，之后通过其（负）相关性的程度作为Alpha信号。

5.过程记录

a)代码效率: 修改了ACE比赛的模板，使得可以同时simulate 10个Alpha，1000组左右Alpha可以在少于1小时内运行完。目前实现的功能还较为简单，只包括对于各个时序数据所选取时间的搜寻，即在人为确定适合的datafield后再进行数值搜索。目前正在加上GA功能，利用sharpe或fitness的反馈来优化搜索方向。

b)debug经历。一开始出现了链接中断导致代码运行失败的情况，后通过修改，为多线程simulate的方法加上断线重连的功能，在10秒内如果出现timeout就保存断点并再次重连。

c)模板适合的数据类型。目前的模板仅仅支持matrix数据，后续会增加对于vector数据的支持。

d)模板的改进方向。1）利用GA进行数值方面的优化。2）尝试采用不同的数据集，加大搜寻的范围。

---

### 评论 #93 (作者: YT47842, 时间: 2年前)

虽然昨天已经完成了1000次提交，但是今天修改了代码，并使用了新的alpha Expression思路。感觉比昨天有了一定的改进

这个是提交前的alpha计数
 
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> 文件
> 编辑
> 视图
> 历史记录
> 书签
> 个人资料
> 标签页
> 窗0
> 帮助
> 68字
> 
> 8us
> 曰 O ? Q %
> 1月28日周日
> 15:37
> WorldQuant BRAIN
> X
> 唱
> 〉
> G  命
> 9
> platform. worldquantbrain.comlalphas/unsubmitted
> Go
> 区
> ABP
> 馆 Keras入 门必看教程
> Keras中文文档
> 知
> Keras教程
> Python教程
> 廖雪。
> |简
> 深度学习从小白到..
> Keras教程_腾讯视频
> 所有书签
> 同变量
> :大纲
> Python 3.11.5
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Data
> : Competitions (2)
> Events
> Learn
> Q
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 10
> out of 3,309
> Filter


这个是完成1200次模拟后的alpha记录 
> [!NOTE] [图片 OCR 识别内容]
> Chrome
> 文件
> 编辑
> 视图
> 历史记录
> 书签
> 个人资料
> 标签页
> 窗0
> 帮助
> 77字
> 凹
> 8kjs
> 曰
> C ? q %
> 1月28日周日
> 17:28
> Worldauant BRAIN
> X
> {Alpha灵感]  论文/研报合集 -
> 义
> (Alpha 灵感)  技术指标类单医
> 义
> 十
> [
> > G 命
> 93
> platform.worldquantbrain.comlalphaslunsubmitted
> 区
> ABP
> 馆
> Keras入 门必看教程
> Keras中文文档
> 知 Keras教程
> Python教程 -
> 廖雪.
> 深度学习从小白到
> Keras教程_腾讯视频
> 所有书签
> :大纲
> Python 3.11.5
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Data
> : Competitions (2)
> EVents
> Learn
> lt cell output Settings
> p2/26@266@568.py:13=
> FutureWarning: The
> 1
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> 12/4110299312.py;36: FutureWarning:
> The
> Show
> 10
> out of 4,439
> Filter 
> Iszo)
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Retul


注意到提交了1200次但是只有1130次成功了，下次需要再在函数中打印出提交失败的simulate任务看看咋回事。

这个是提交用时 
> [!NOTE] [图片 OCR 识别内容]
> 88字
> %ks
> 5@
> 曰 @ ? Q &
> 1月28日周日
> 17:28
> api_python
> 唱
> Wq_api_1000.ipynb
> 』
> Wq_api_1000.ipynb
> all_summary_df
> 代码
> Markdown
> 全部运行
>  重启
> 豕清除所有输出
> 变量
> :大纲
> Python 3.11.5
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Alpha
> done simulating, getting alpha details
> Alpha
> retrieved
> Sleeping for
> 2.5
> Seconds
> Alpha
> done
> simulating, getting alpha details
> Alpha
> retrieved
> Alpha
> done simulating, getting alpha details
> Alpha
> retrieved
> Alpha
> done
> simulating, getting alpha details
> Alpha
> retrieved
> Sleeping
> for
> 2.5 seconds
> Alpha
> done simulating, getting alpha details
> Alpha
> retrieved
> Alpha
> done simulating, getting alpha details
> Alpha
> retrieved
> Alpha
> done simulating, getting alpha details
> Alpha
> retrieved
> Output is truncated. View as a Scrollable element or open in a text editor: Adjust cell output Settings.
> LarLfoldersLctLgnkzgjszclggldhlhpzht4oo@@@gnlTLipykernel  2152/26@2660568.py:13:
> FutureWarning:
> The
> summary_df
> pd.concat ( [summary_df,
> df], axis=0)
> 总用时:
> 2
> h
> 3
> min
> 20,43
> LarLfoldersLctLgnkzgjszclggldhlhpzht4ooeo@gnlILipykernel 2152/4110299312,Py:36:
> FutureWarning:
> The
> al1_summary_df
> pd. concat ( [all_summary_df, summary_df],
> aXis=0 )
> 〉 ^ ^  曰


这个是1200个alpha的performance


> [!NOTE] [图片 OCR 识别内容]
> 102字
> %ks
> 5@
> 曰 @ ? Q &
> 1月288周日
> 17:29
> api_python
> 1
> Wq_api_1OOO.ipynb
> Wq_api_1000.ipynb
> all_summary_df
> 代码
> 十
> Markdown
> 全部运行
>  重启
> 豕清除所有输出
> 变量
> :大纲
> Python 3.11.5
> 总用时:
> 2 h
> 3
> min  20.43
> LarLfoldersLctLgnkzejszclggldhlhpzht4@oo@egnLILipykernel 2152/4110299312.py;36:
> FutureWarning:
> The
> al1_summary_df
> pd. concat ( [all_summary_df, summary_df],
> aXis=0 )
> 竺 D D
> al1_sUmmary_df
> [12]
> 0.OS
> Python
> sharpe
> fitness
> turnover
> returns
> drawdown
> margin
> JbEOYrn
> 1.53
> 0.99
> 0.3920
> 0.1650
> 0.1667
> 0.000842
> WSQwn2x
> 1.57
> 1.27
> 0.3841
> 0.2525
> 0.2467
> 0.001315
> 2JzqQW5
> 1.51
> 1.17
> 0.3981
> 0.2405
> 0.2281
> 0.001209
> qgrkv3o
> 1.69
> 1.43
> 0.3559
> 0.2549
> 0.2542
> 0.001432
> TJbqOMV
> 1.52
> 1.20
> 0.3963
> 0.2484
> 0.2531
> 0.001254
> ddVdkmv
> 1.03
> 0.54
> 0.4372
> 0.1196
> 0.1695
> 0.000547
> ddVdknx
> 1.09
> 0.60
> 0.4416
> 0.1332
> 0.2173
> 0.000603
> 9J1JZGe
> 1.22
> 0.71
> 0.4440
> 0.1514
> 0.1750
> 0.000682
> pgrgYnx
> 1.07
> 0.59
> 0.4499
> 0.1363
> 0.2006
> 0.000606
> Zr3rPWY
> 0.45
> 0.22
> 0.4160
> 0.0962
> 0.6991
> 0.000463
> 1200 roWS X 6 columns


这次的模拟还获得了一个可以提交的alpha


> [!NOTE] [图片 OCR 识别内容]
> rome
> 文件
> 编辑
> 视图
> 历史记录
> 书签
> 个人资料
> 标签页
> 窗口
> 帮助
> 119字
> 8s
> 曰
> 芊 令 Q &
> 1月28日周日
> 17:33
> Worldauant BRAIN
> 义
> Worldauant BRAIN
> 义
> (Alpha灵感]  论文/研报合集
> X
> (Alpha 灵感)  技术指标类隼
> X
> 十
> l
> 0
> > G 命
> 0
> platform.worldquantbrain.comlalphas/unsubmitted
> Go
> 区
> 15
> ras入门必看教程
> Keras中i文 文档
> 知 Keras教程
> Python教程 -
> 廖雪。。
> 旧
> 深度学习从小白到.
> Keras教程_腾讯视频
> 所有书签
> :大纲
> Python 3.11.5
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Data
> 罟 Competitions (2)
> EVents
> Learn
> Python
> UNSUB
> Created 01/28/2024 EST
> anonymous
> Add Alpha to a List
> Bin
> '42
> 315
> 区 Openalpha detailsinnew ab
> 09
> 32
> 54
> Sh
> Chart
> Pnl
> '47
> '03
> ;82
> Cont
> 06
> Sel
> ZOM
> 63
> 15M
> s 》D 曰
> 1OM
> Python
> 5,00OK
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
> Check Submission
> Submit Alpha
> 25,列 1
> 空格:4  LF
> 单元格 13/13
> 0


但是后来发现这个prod_cor过高 >_<

思考：
使用的alpha因子：

"""vhat=ts_regression(scale({datafields_list[n*epoch+j]}),ts_delay(scale(snt_buzz),1),500);ehat=ts_regression(scale(returns),vhat,500);alpha=group_neutralize(-ehat*ts_rank({datafields_list[n*epoch+j]},5),bucket(rank(cap),range='0,1,0.1'));trade_when(abs(returns)<0.08,alpha,abs(returns)>0.1)"""

代码效率：
对代码做了工程上的改进，使用多线程并发，将模拟时间缩短了25%以上
debug经历：
由于昨天已经做了相关的模拟，所以今天的模拟中没有发生bug
模版适合的数据类型：
今天的因子同样选用的是price volume的数据，对于vector使用vec_sum对于matrix则不做处理
模版改进的方向：
还是prod_cor过高，感觉需要继续挖掘新的因子才能解决这个问题

---

### 评论 #94 (作者: WL13229, 时间: 2年前)

[YZ64617](/hc/en-us/profiles/4527497709335-YZ64617)

您好，查看不到performance可能有两个原因。

1。网页缩放问题，调整一下网页缩放的大小（按住control键+鼠标上下滚轮）试一试能不能显示。

2. 过往的Alpha太久了。尝试多simulate一些过第二天看看。

如果尝试上面两个还无法解决，请与我们联系。

---

### 评论 #95 (作者: YZ64617, 时间: 2年前)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)

谢谢，现在可以再页面上看到performance了。

更新一下alpha结果，有很多sharp比较高的结果，但是，基本都有一个IS Ladder Sharp不通过的问题。


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
> 01/27/2024
> 01/28
> Select
> Select
> @.8>1
> e.8>1
> e.8>1
> Select
> anonymoUs
> Regular
> UNSUBMITTED
> 01/28/2024 EST
> CHN
> TOP3000
> 3.02
> 24.75%
> 41.300
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 3.02
> 24.759
> 41.30%
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 3.00
> 24.68%
> 41.279
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3O00
> 2.98
> 28.90%
> 50.56%
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.95
> 28.75%
> 50.45%
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.93
> 27.339
> 50.26%
> anonymous
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.88
> 25.92%
> 51.709
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.88
> 24.21%
> 42.05%
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.87
> 25.12%
> 52.30%
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.86
> 26.70%
> 50.51%
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.85
> 27.109
> 50.349
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.84
> 27.029
> 50.189
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.84
> 14.44%
> 2.859
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.84
> 14.449
> 2.85%
> anonymoUs
> Regular
> UNSUBMITTED
> 01/27/2024 EST
> CHN
> TOP3000
> 2.82
> 27.00%
> 50.72%
> Tag



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> PASS
> 1 FAIL
> IS ladder Sharpe of 1.66 is below cutoff of 2.07 for ladderyear 2: 1/24/2022.
> 1/25/2020.
> 2 WARNINC
> 3 PENDING
> Performance Comparison
> Last Run:


对于这个问题，不知道如何入手解决，求建议。

---

### 评论 #96 (作者: YL37225, 时间: 2年前)

**1.alpha提交多次

 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 1@
> GOOD
> BXCELLEMT
> Total Unsubmitted Alphas
> 1,350
> Total Active Alphas
> 11
> SECTACUAA
> Total Decommissioned Alphas
> Total Alphas
> 1,361
> 16:18
> @
> 4)
> 凹
> Ployar
> 2024/1/3
  
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 2,947
> Total Active Alphas
> 11
> Total Decommissioned Alphas
> Total Alphas
> 2,958
> 9:35
> @
> 4
> 凹
> 2024/1/30
 

2.alpha的连续提交**  
> [!NOTE] [图片 OCR 识别内容]
> Cnt=cnttl
> print
> ("成功提交了:
> cnt, "次。
> ")
> time.sleep (6)
> 请注意。如果您有大量的aIpha表达式。  您可能想要添加
> 些逻辑来避免发送太多的请求
> 或者适当地处理API的速率限制。
> #Run AIpha
> code
> print ("running"
> except:
> print ( 'connection
> down
> sign_in()
> [61]
> 113m 50.6s
> 〈Response [201]〉
> Simulation
> submitted  successfully
> 成功提交了:
> 1  次。
> Simulation
> submitted successfully
> 成功提交了:
> 2  次。
> Simulation
> submitted  successfully
> 成功提交了:
> 3  次。
> Simulation
> submitted successfully_
> 成功提交了:
> 4  次。
> Simulation submitted successfully
> 成功提交了:
> 5  次。
> Simulation
> submitted successfully_
> 成功提交了:
> 6  次。
> Simulation
> submitted successfully
> 成功提交了:
> 7  次。
> Simulation
> sUbmitted
> sUCCessfully
> 成功提交了:
> 8  次。
> Simulation
> submitted  successfully
> 成功提交了:
> 9  次。
> Simulation
> submitted successfully_
> 成功提交了:
> Io 次。
> Simulation
> submitted  successfully
> 成功提交了:
> 11  次。
> Simulation
> submitted successfully_
> 成功提交了:
> 12
> 次。
> Simulation
> submitted successfully
> 成功提交了:
> 1851
> 次。
> Simulation
> submitted  successfully
> 成功提交了:
> 1852
> 次:
> Output is truncated. View as 0 Scrollableelement or open in a text editor Adjust cell output Settings: -
 
 **3.总结反思** ·批量生成alpha的过程中遇到vector数据需特殊调整，这一部分我设计的代码还不具有普适性。
·不太擅长编程，使用了较为简单的time.sleep( )而没有进行多线程的设计，后续可以进行调整。更换alpha或者修改simulation的设置可能会需要修改time.sleep( )函数的参数。·获取到的数据字段比想象中多许多，因为时间关系只对其中一部分进行了分析。
·目前我的代码中如果想，解决超时登出问题而使用while ture函数就会导致所有的simulation模拟完之后又重新模拟第一个。
·每次进行一次大规模simulation时需要耗费的时间较多，应当设计代码记录当前进度，我的代码目前还是每次又重新从第一组数据开始尝试simulation，效率很低。

---

### 评论 #97 (作者: DL55804, 时间: 2年前)

1. 开始截图，此时simulation的数目是1608 
> [!NOTE] [图片 OCR 识别内容]
> WrInnl
> LwerNe To
>  K
> 」 |uc』
> 0CT
> 10
> I
> 71024
> IUO
> TITTT
> TTA
> TTI
> AT
> TIN
> RA
> Mlphas

2. API提交后截图，此时simulation的数目是 
> [!NOTE] [图片 OCR 识别内容]
> AOha
> S
> AhyLh;
> |
> TTMIC
> TTar
> go
> IC
> 1OOIU
> INNAT
> TTaT
> r4
> I
> TOIL

3. 连续不断提交alpha的截图 
> [!NOTE] [图片 OCR 识别内容]
> 4l5
> TCP
> [3]
> Uln
> tht
> OCT
> Thd
> croon
> 0anauIII
> WInJo
> thta
> MCUII
> Sjp
> hlld
> Uinctio
> TTU TN
> U
> Th
> TerCeI
> stlp
> T
> Aeot
> Maea 
> Uln
> theta
> Dercet'
> Td
> 1.8
> MRectlo
> RraTm
> Wino
> thta
> OCM
> p
> hd
> Urrton
> 'pnu'
> UI
> Tl
> TCUI
> smp
> SA
> U
> M
> 
> Mru Im
> Lln
> theta
> ONCeI
>  Ud
> Urecqn
> Dana_Ne
> Uino
> thta
> DCO
> sp
> hd
> Uirectio
> MraTM
> I
> L
> TTCUI
> S
> Oaga
> .凸
> uU
> 
> theta
> UrCeI
> slp
> IJ
> Urectlol
> -1.0
> Nra Im
> 100

4. 反思总结——代码效率
   1. 代码的效率大约是1小时能跑1000个左右，目前的做法是使用多线程同时进行10次simulation，simulation结束后，获取alpha的表现 
> [!NOTE] [图片 OCR 识别内容]
> TU1t1510UIatJCICC]+ )
> TOeuTCLeCutormY horRCTs1e |
> Cecutor:
> N
> R
> UCCCUCOC
> SUblt(selt.SImulation;
> dict_Paraneter)
> diet_Paru-eter
> Sel.lst_Dur
> Tuure In CoCUrrent
> qULUel
> COOIeCltUtUIC
> T501t51
> LT
> appndtTuturp +TosUt
> CUCT

   2. 解决长时间运行会自动断开的问题。在simulation中，如果回测的alpha有问题，就会发生alpha_check=False，如果是连接断开，就会重新连接，因为使用的是多线程，所以考虑一旦某一个线程断开，其他线程也会断开，所以用一个reconnect_status来表示某一个线程已经再进行重新登录，其他线程只需要等待连接即可。While True确保了断开之后能重复尝试连接 
> [!NOTE] [图片 OCR 识别内容]
> Siulation(seIf
> dict_paraweter
> inde):
> print(dict_parameter)
> #@进厅4个回则
> nhile True:
> T
> siulation_data
> SeIf.CalsimulationData(self.str_type
> Self.dict_setting; Jict
> 0araR
> si-ulation_response
> utilsralpha_simulation(self.session;
> si-ulation_data)
> alpha_Chock
> utils.alpha_status
> CTCCsTUL7t101
> rosponso
> a10ha
> Check:
> alpha_id
> Utils.Bet_alpha_id(self
> 905510n
> sirulation_response)
> print( ALPHA SINULATTON FaIL)
> 4Pt
> alpha_Check
> False
> brea
> ercept:
> Self.reconnpct_status
> T
> tine.sleep(18)
> else;
> 581
> TeCoIe Ct
> status
> TU
> self.session
> utils
> connect_to_Worldquant()
> Sel+.reconnect_status
> Sa
> Ra+CR
> alpha_id
> OI


1. 具体的代码流程：产生需要回测的参数列表、登录、回测、获取表现、保存simulate的结果到csv中 
> [!NOTE] [图片 OCR 识别内容]
> self.GenerateParameter( )
> self. ConnectToWorldouant()
> self.Multisimulation()
> self.Alphaperformence()
> self.SaveResult()

2. 默认的setting为下左图所示。我认为除了region universe delay需要通过setting来进行调整，其他的部分都可以通过在alpha的表达式里，自己进行decay或者中性化，所以通常自己simulate的时候只修改三个部分，也就是下右图所示在表达式里可以自行定义，自由度更高。 
> [!NOTE] [图片 OCR 识别内容]
> DEFAULT_PICT
> SETTING
> {
> instrumentType
> EQUITY'
> region
> CHN
> universe
> T0P2000
> 'delay
> 1,
> decay
> 0
> 'neutralization
> NONE
> truncation '
> 0.02,
> dict_setting
> {
> pasteurization
> 'ON
> unitHandling
> VERIFY'
> region
> 
> CHN
> 'nanHandling
> OFF
> universe' :
> TOP2888'
> language
> FASTEXPR
> delay
> :
> 1,
> 'visualization
> False,


1. Simiulate的模板是：【Alpha灵感】凸显理论（Salience Theory）

个人感觉研报的核心应该是提出的那个凸显性，尝试使用换手率构造凸显性，其中可以用来构造凸显性的数据应该很多，包括收益率、换手率，现在感觉甚至是一些情绪指标、基本面指标都可以用来构造。 
> [!NOTE] [图片 OCR 识别内容]
> TUNOTer
> Volume / sharesout;
> market_turnover
> Broup_mean(turnover,
> Rarket);
> SiBma
> ab5 (turnover
> market_turnover)
> (abs(turnover)
> ab5 (market
> TURRONeI
> theta) ;


1. 参数调整 
> [!NOTE] [图片 OCR 识别内容]
> SLurt
> UJe
> OOUCCLL
> 010100335
> str_tpe
> COTst;5TULATTON_TPE
> Uct_settinl
> 「omon
> Unzee
> TPA C
> CeLa
> Cict_Parars
> Mo
> [5。10
> 75。30。35。40,
> 50]。
> thot
> B8。8,1。0.16
> 8,238』,
> Percent
> 4
> 8.5』,
> SLip
> h014
> 10]
> UretzoI
> [1],
> utiis.run_replay(strateeysstrateRy。
> 510-520
> 08185-02Ct
> 030a5
> Oict_settine-dict_settine
> T
> uttlmR,Tl


Window1是取一段时间signal的平均值

Theta是求凸显性的参数

Direction是信号的方向

percent可以让我们可以只交易两端的信号，

skip是考虑到像动量效应会有一些短期的反转，所以可以考虑delay一段时间的信号

hold是类似于decay的天数 
> [!NOTE] [图片 OCR 识别内容]
> SJBnal
> WIndom
> [indow
> direction
> {Jirectionj;
> Cheta
> {theta] ;
> turnover
> Volume /sharesout;
> parket_turnover
> Broup_mean(turnover,
> market);
> SiBna
> abs(turnover
> market_turnover)
> (ab5(turnover)
> abs(earket_turnover)
> theta);
> SiRnal
> ts_median(sifma,
> yindow)
> direction;
  
> [!NOTE] [图片 OCR 识别内容]
> 5S
> Int(dtct_Paraeter
> Skip  ])
> OCRCChL
> UJCt 03RaICLCTL
> OCRCCML
> ho
> Int(dict_puracter['hold ])
> Skip
> Sinal
> Ra
> 5nal;
> o]
> Sklp_sll
> 5JNpa]
> deloy(siena; Sip_period);
> stpategy
> Skip_Period
> {5kIpJ
> C40e
> Percent
> {Percen];
> NO
> {hola];
> {tp_slnn]
> 53R1a12
> 「ank(57Bna11)
> 530011
> 1f_elsc(nd ( -62
> 5tradrPreent。
> 5341012
> trade_pcrcent 8,5)
> 5301112);
> SJBnalo
> nan(s181813
> VALUeO
> reversesTrue;
> 53R1a15
> SiBn(sienalu);
> 53fna16
> SUM(S16na15
> hold_periot);
> 「30a17
> TaLeNa
> Value=0);
> SiRnal
> Sienal
> sipnal
> strateey
> 503
> atiou
  
> [!NOTE] [图片 OCR 识别内容]
> SJBnal
> WIndom
> [indow
> direction
> {Jirectionj;
> Cheta
> {theta] ;
> turnover
> Volume /sharesout;
> parket_turnover
> Broup_mean(turnover,
> market);
> SiBna
> abs(turnover
> market_turnover)
> (ab5(turnover)
> abs(earket_turnover)
> theta);
> SiRnal
> ts_median(sifma,
> yindow)
> direction;


1. 模板的改进思路： 首先是尝试很多类似成交量、换手率、成交额的数据。2. 尝试一些其他的凸显性，类似于基本面的凸显性。3. 使用一些operator让alpha更稳健，例如ts_zscore、ts_rank。
2. Debug的一些反思：由于用了相当多的try，导致debug的过程异常的艰难，现在想来每一次post或者get都应该查看status，如果报错了，根据错误信息进行debug效果应该会更好。2. 还没有想清楚如何更好地可视化performance，以提供更多地信息，方便改进alpha
3. 回测的performance存在csv中 
> [!NOTE] [图片 OCR 识别内容]
> Aa
> @ {s
> N (+
> RonC
> Jeel
> oeeeeCa
> te
> oo
> 』eo
> t
> pt
> 
> a
> T
> apFr


回测的performance存在csv中

---

### 评论 #98 (作者: SW14484, 时间: 2年前)

第一部分：

1. 不间断连续运行1064次

起始数量：530


> [!NOTE] [图片 OCR 识别内容]
> CIOMIN
> 丙~;27
> !
> ATT
> 3月68厌 06:3711
> IerlLILARNI
> ATTNITIUUANIIIL
> TLIUII.
> UIIIIOUI
> TUI t
> Uttry
> CIAIFEr t
> TTI
> QnyALUR
> TTt!5t}
> Chlallbn
> 2101+51 NT识
> N5
> LFHI5RG2
> 口 .乐卉C
> %鹊兴
> Plsimwlat
> Uhs
> CPTOC II
> 同 tnts
> Ulearn
> HtrnTrimd
> Q Alphas
> Unsubmittcd
> Submitted
> UThu Ditribution
> Aloha List
> SHIIITTT
> STT2
> LCMFC Itcn
> H
> Tlc LrRattIFCT
> RCGICT
> NT
> STpt
> TIOT
> JTTCM
> gTOICI
> PTUIOT
> UISLIIITTII
> IIAZIL |
> ILLJUIII MI
> 174
> VI
> SonymcW;
> AeRUlar
> UISIITTE[
> 031+2135551
> IL SUIOSM
> 0.11
> .71
>  TIIIII
> NTTIIII
> IIIIITPT
> 032124
> L|III 「
> 01
> II
> TDTTTCI
> TPIUIOI
> UISLIIITTTI
> IIt1
> ILLTUIIL MI `
> U
> V
> TTNIIII
> SONIH[
> USIAMITTEI
> 12931551
> TUIO SII'
> 197
> 135
> STII
> VUIII
> IIIIITPT
> 0352124 S5T
> ULJUINMII
> NOI
> I
> TOTTCI
> PHUJII
> UMISLIIITTII
> 022o !1
> ILLSUIIU LI `
> 123
> 9
> JTONYNCU;
> TMII「
> USIMITTE[
> 1131 FT
> TL TUO LIL'
> 0711
> IIIIITT
> NU
> U|IUIIU MI


截止数量：1594


> [!NOTE] [图片 OCR 识别内容]
> CIOMIN
> 丙~;27
> !
> ATT
> 3月68厌 09:4148
> lur  RN
> UITII TTIIUANTU
> CUIIIIAITIC
> IIT
> Tl
> UT
> CmnTVi =
> TTHN
> TRyAut
> t
> 5
> chalaalf:I
> TTA
> Nc
> NTIF
> H王SLSI
> 匕 .53豆
> 骣鹊哭
> Clslmtatr
> ULoh
> I F
> 固 sents
> Ulerr
> $ Rter
> TITI
> Alphas
> Unsubmiutec
> Submttcd
> Jhu Uitributian
> uloha Lrsts
> 5y
> SOTITTI
> LCIFC IC 
> LARHI
> Tl CroztpICCTI
> HCqIo7
> TTTTr
> ShTTC
>  TIN7 
> UITTCUC[
> leIne2 y
> henular
> LISIIUUIITTTO
> WIUUZL|
> ILIJUIU TI'
> 11.11
> y.42
> ToNR49
> R?ular
> ULEIIIU
> 070
> ILTUIILI
> I I17
> ITI
> IIIUITTh
> IIET
> UTAIIII
> 131
> 94
> leuzT
> hemulur
> LISUIEUIITTO
> UII2U2 L1
> ILIJUIU TI'
> 1292
> 11
> TnrTIC4
> R?Ular
> UIEIIIU
> 05120
> IITLII LI
> lI
> TVI
> IUILUITTh
> 04205 SST
> IIUIID UN
> 11
> VTh
> leIm2ujl
> hwulur
> UISUIEUITTTT0
> UII2U2u 41
> ILIUID TI'
> 12y
> 9.491
> TnrTIC4C
> R?UIaT
> WSUEUITE
> 141704 FT
> ULTLIITII
> 03.131
> 99
> CMI
> IIUIETIT
> 0U7s ST
> IAUIIUTIN
> 14
> 11h


共花费时间：


> [!NOTE] [图片 OCR 识别内容]
> [5]
> G4m 7.45
> <Response
> [201]>
> <Response
> [201]>
> <Response
> [201]>
> <Response
> [201]>
> <Response  [201]>
> <Response
> [201]>
> <Response
> [201]>
> <Response
> [201]>
> <Response
> [201]>
> <Response
> [201]>


步骤详细说明：

（1）单次API成功提交的实现

- 确定API接口参数：首先，需要了解API的具体要求，包括需要的参数、请求方式（GET、POST等）以及任何特定的请求头。
- 编写代码：基于API的要求，编写相应的代码以构建请求。这可能包括设置请求头、构建请求体、以及处理任何必要的身份验证步骤。
- 测试提交：在开发环境中测试API提交，确保所有参数都正确设置，并且能够成功获得预期的响应。
- 记录日志：为每次API提交创建日志记录，以便跟踪问题和性能。

（2）分析API提交的时间间隔和单线程提交的局限性

- 确定时间间隔：发现API有20秒的时间间隔限制，这意味着每次提交后至少需要等待20秒才能进行下一次提交。
- 计算单线程提交时间：考虑到这个限制，如果使用单线程提交1000次，每次等待20秒，加上提交本身的时间，总时间将非常长，至少需要5.5小时。

（3）引入多线程解决方案并处理相关问题

- 确定线程数量：为了加速提交过程，决定使用多线程。通过实验，发现开启10个线程可以达到较好的性能和稳定性。
- 解决多线程访问共享数据的问题：当多个线程需要访问或修改同一数据时，可能会出现死锁或数据不一致的问题。为了解决这个问题，引入了线程锁或其他同步机制，确保每次只有一个线程可以访问或修改数据。
- 调试与优化：在引入多线程后，可能会遇到各种预料之外的问题，如线程冲突、资源竞争等。通过不断地调试和代码优化，最终解决了这些问题。

（4）最终的提交效果

- 性能提升：通过使用多线程，显著提高了API的提交速度。从原来的5.5小时减少到了大约64分钟，大大提高了工作效率。
- 总结与反思：回顾整个优化过程，不仅解决了API提交的问题，还学到了很多关于多线程编程和性能优化的知识。同时，也意识到在引入多线程时，需要特别注意数据同步和线程冲突的问题。

第二部分：

我阅读的是：抢跑者的脚步声，基于价量互动的选股因子这篇研报

在投资领域，我们常常会遇到这样一个现象：当面临重要事件或消息时，投资者往往会加大筹码，试图通过买卖股票来获取更大的收益。这种现象在得到内幕消息时尤为明显，知情交易者（informed trader）通常会急于抛售或买入股票，以期在股价变动前获得利益。然而，作为普通投资者，我们往往无法获取这些内幕消息。那么，如何在不知道内幕消息的情况下，合理规避风险，抓住投资机会呢？

这篇研报为我们提供了一种解决方案：通过异常信号来识别知情交易者的行动。研报作者发现，成交量是泄露知情交易者行动的重要信息源。具体来说，换手率与第二天股价的波动呈现出正相关关系。这意味着，在股票大跌前，知情交易者会大量抛售股票，急于离场，导致换手率上升；而在大涨前，知情交易者会大量购买股票，急于进场，同样会导致换手率上升。这种换手率与股价波动的正相关关系，暗示了信息泄露程度的高低。当这种关系越强时，说明信息泄露程度越高，我们在该类股票上的博弈可能陷入劣势。

为了衡量股票未公开信息的泄露程度，研报提出了一个名为抢跑因子（Front Running, FR）的指标。这个指标通过计算T日换手率与T+1日涨跌幅的关系来评估信息泄露的程度。为了公平比较，研报在计算抢跑因子时剔除了常规因子如市值、动量、换手率、波动率和行业等因素的影响。

纯净的抢跑因子:FR=𝛽1𝑙𝑜𝑔(𝐹𝐴𝑀𝐶)+𝛽220𝐷𝑀𝑜𝑚+𝛽3𝑇𝑢𝑟𝑛+𝛽460𝐷𝑉𝑜𝑙+∑𝛽5𝑖∗𝐶𝑖𝑡𝑖𝑐𝐼𝑛𝑑𝑖+𝜀其中𝐹𝐴𝑀𝐶是股票自由流通市值，20DMom是20日动量，Turn是换手率，60DVol是60日波动率，𝐶𝑖𝑡𝑖𝑐𝐼𝑛𝑑是中信一级行业哑变量，ε是残差。

作者通过回测，得到以下结论：

首先，作者发现：当月因子值越小，次月收益越高。所以，投资者可以关注那些因子值较小的股票，因为它们可能在未来一个月内带来更高的收益。这种策略的实施，无疑增加了投资的灵活性和多样性，为投资者提供了更多的选择。

其次，研报还揭示了知情交易者在好消息和坏消息上的泄露程度存在差异。具体来说，坏消息的信息泄露现象更为显著。这意味着，在面临负面消息时，知情交易者可能更倾向于迅速采取行动，导致换手率上升。这一现象可能与投资者的心理反应有关。面对坏消息，投资者往往感到恐慌和不安，急于抛售股票以避免进一步的损失。因此，投资者在制定策略时，应充分考虑这一因素，避免在负面消息的影响下做出过激的反应。

此外，研报还探讨了上涨和下跌时𝐹𝑅0因子的预测能力差异。结果表明，下跌时的预测能力最强，整体强于上涨。这一发现为我们提供了关于市场行为的深刻洞察。在下跌时，由于投资者对损失的敏感性增加，他们可能更加关注股票的价格变动和相关信息。因此，在这种情况下，𝐹𝑅0因子能够更有效地预测股票的未来表现。

为了增强原始𝐹𝑅0因子的预测能力，研报提出了两种简单的方法。首先，可以使用𝐹𝑅𝑑因子替代𝐹𝑅0因子，即只使用下跌端的数据而不使用上涨端的数据。这种方法基于上述发现，即下跌时的预测能力最强。通过专注于下跌数据，我们可以更准确地捕捉市场行为的变化并做出更明智的投资决策。

其次，另一种方法是将上涨和下跌数据以一定比率结合起来。这种方法旨在平衡两者之间的预测能力差异，并充分利用两方面的信息。通过合理调整比率，我们可以找到最佳的平衡点，使因子在上涨和下跌时都能发挥出色的预测效果。

---

### 评论 #99 (作者: WL13229, 时间: 2年前)

[SW14484](/hc/en-us/profiles/20580045390871-SW14484)

非常完整的作业，完成速度令人赞叹。下节课我们的作业是要求将一篇论文/研报写成模板，看到你已经对该研报做了认真分析。可以着手开始尝试了。让我们下节课再见

---

### 评论 #100 (作者: BC25356, 时间: 2年前)

@ [HW97336](/hc/en-us/profiles/18134895192087-HW97336)

您好，看了您的代码，收益颇多。
可以分享下datafield_list这部分的代码吗？对于这部分，还是有疑惑的（具体怎么得到这个list的）。

---

### 评论 #101 (作者: IC51680, 时间: 2年前)

Screen Captures:

初始alpha:179


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> ShoW
> Out Of 179
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
> Searcn
> SeeL
> SeeL
> SeeL
> Searcn
> SeeL
> SeeL
> e.6> 1
> e.6> 1
> e.6> 1
> SeeL
> ERCTIJUs
> Reaular
> UNSUBMITTED
> 03/5/202- EST
> U-
> T0P300
> 0.27
> 631
> 643
> aCE 氓
> anonymous
> Raular
> UNSUBIITTED
> 03/05/202- ET
> US-
> TOP30T
> 0.79
> 9435
> 7.451
> aCE_aE
> anonymous
> Reaular
> UNSUBMITTED
> 03/5/202- EST
> U-
> T0P300
> 0.76
> 2.2711
> 2911
> aCE 氓
> anonymous
> Reeular
> UNSUBIITTED
> 03/05/202- ET
> US-
> T0P3000
> 1.5
> 51
> 51
> 泛
> anonymous
> Reaular
> UNSUBMITTED
> 03/5/202- EST
> U-
> T0P300
> -0.13
> 2321
> 7.741
> aCE 氓
> anonymous
> Raular
> UNSUBIITTED
> 03/05/202- ET
> US-
> T0P3000
> 1.63
> 9
> 801
> aCE_aE
> anonymous
> Reaular
> UNSUBMITTED
> 03/5/202- EST
> U-
> T0P300
> 0.30
> 7.251
> 3-1
> aCE 氓
> anonymous
> Reeular
> UNSUBIITTED
> 03/05/202- ET
> US-
> TOP30T
> -.01
> 111
> 5301
> 2o
> anonymous
> Reaular
> UNSUBMITTED
> 03/5/202- EST
> U-
> T0P300
> 0.12
> 2321
> 7.521
> aCE 氓
> anonymous
> Raular
> UNSUBIITTED
> 03/05/202- ET
> US-
> TOP30T
> 65
> 1.7811
> 7.653
> aCE_aE
> ShOw
> OUT Of 179
> Prv
> Next
> 殷用 Windows
> 移至 [彀定] 以敲用 Windows
> 17.03
> 2r
> W @
> ENG
> 8/3/2024
> Tag
> 3


ace library挺好用的

現有alpha 1224


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> STOW
> Dut Of 1,224
> Filter
> Select Columns
> Name
> Competition
> Type ^
> Status
> Date Created (EST)
> Region
> Unjverse
> Sharpe
> Returns
> Turnover
> Tag
> Searcn
> Selec
> Selec
> Selec
> Searcn
> Selec
> Selec
> e.6> 1
> e.6> 1
> e.6> 1
> Selec
> anonymous
> Raular
> UNSUBIITTED
> 03/9/202- ET
> US-
> TOP3UOJ
> 1.29
> 431
> 11.451
> ERCTIJU=
> Reaular
> UNSUBMITTED
> 03/09/202- EST
> U-
> T0P300
> 0.09
> 51
> 11.331
> aCE_T
> anonymous
> Raular
> UNSUBIITTED
> 03/9/202- ET
> US-
> T0P3000
> .57
> 851
> 11.331
> ERCTIJU=
> Reaular
> UNSUBMITTED
> 03/09/202- EST
> U-
> T0P300
> 0.09
> 0.57珩
> 11.321
> ae
> anonymous
> Reeular
> UNSUBIITTED
> 03/9/202- ET
> US-
> TOP3OO0
> .57
> 851
> 11.331
> aCE_7
> ERCTIJU=
> Reaular
> UNSUBMITTED
> 03/09/202- EST
> U-
> T0P300
> 0.43
> 571
> 11.701
> aE
> anonymous
> Raular
> UNSUBIITTED
> 03/9/202- ET
> US-
> TOP3OO0
> 1.43
> 571
> 11.701
> aCE
> ERCTIJU=
> Reaular
> UNSUBMITTED
> 03/09/2024 EST
> U-
> T0P300
> 0.29
> 131
> 11.463
> ae
> anonymous
> Reeular
> UNSUBIITTED
> 03/9/202- ET
> US-
> TOP3OO0
> 0.09
> 15711
> 11.331
> aCE
> ERCTIJU=
> Reaular
> UNSUBMITTED
> 03/09/202- EST
> U-
> T0P3000
> 0.57
> 351
> 11.943
> aCE_T
> Show
> OUT Of 1,224
> Po
> 123
> Next
> 敏用 Windows
> 移至 [彀定] 以殷用 Windows
> 13.57
> 15%C  多雾
> @ @ d
> ENG
> 9/3/2024


使用ace library multi simulation, 預設是 三綫程 344 x 3 = 1032

用時 ~2hr


> [!NOTE] [图片 OCR 识别内容]
> [53]:
> timz.sTrfzime
> %Y-S-%d
> %H;叫:%5" _
> Zime.Iocaltime())
> Out[53]:
> 2321-33-39 12:37:39
> [54]:
> r2SUI-
> aC2.SimUIaT=_aIoha_IisT_IU_ti(5 _
> aIpha_Iist)
> tins
> STrf-ime
> 3Y-R-20
> OH: 9:95
> Zime.Iocaltime())
> 188%
> 344/344
> [1:41:59〈83:83,17.795/i]
> Out[54]:
> 2321-33-39
> 13:51:42


用jupyter notebook 和 acelibrary 輔助, 使用三綫程 所有代碼(generaete alpha list, simulation, return result as dataframe) 不到60 多行

debug经历: 主要是拿result的是后 ace lib prettify result會把dataframe變成style , 之後slice不了dataframem,但改改就沒事了

我閲讀了【Alpha灵感】隔夜“拉锯战”和渔利因子

這文章解釋了如何利用隔夜交易者和盆中交易者的交易模式不同所導致的mispricing來獲利,一般來說，相對專業的機構投資者和職業投資者傾向於在盤中進行交易，而隔夜交易者中，短線交易的投資者比例較高.

在價格校正的過程中，機構投資者可能會出現過度校正的情況，錯誤地將部分隔夜有效交易歸因於由噪音引起的定價錯誤。過度校正可能導致股票定價存在偏差，並在未來呈現回歸的趨勢。

RET_OC = Intraday price change
RET_CO = Overnight price change
NR = Number of intraday reversals in the opposite direction in a month / Number of actual trading days in that month
PR = Number of intraday reversals in the same direction in a month / Number of actual trading days in that month

```
ret_oc = close/open-1; days = 66ret_co = open/ts_delay(close,1)-1;NR = ts_sum(ret_co>0&&ret_oc<0?1:0,66)/days ;PR = ts_sum(ret_co<0&&ret_oc>0?1:0,66)/days ;group = bucket(rank(cap),range='0,1,0.1');group_neutralize(rank(NR)+rank(-PR),group)
```

我在回測時使用了不同neutralization setting (Market sector subindustry...) 還更改了 days

模板的改进思路: 我覺得可以增加其他factor加進去(violatitly,volume,sentiment...)

---

### 评论 #102 (作者: YZ72310, 时间: 2年前)

一、任务前后alpha截图


> [!NOTE] [图片 OCR 识别内容]
> CPU
> 1 KBIs
> RAM
> 14%
> 4 KB/s
> 79%
> 10
> A
> Fri Mar 8
> 21:18
> 8
> 『 0
> SuperAlpha Competition
> Leaderboard
> 2024 Month
> 1
> Stats
> Rank:
> 1,066
> Score:
> Alphas:
> Level:
> No Level
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 132
> Total Active Alphas
> Total Decommissioned Alphas
> Total Alphas
> 138



> [!NOTE] [图片 OCR 识别内容]
> CPU
> 1 KBIs
> RAM
> 26%
> 2 KB/s
> 83%
> 0
> C
> LA
> Sat Mar 9
> 11:22
> SuperAlpha Competition
> Leaderboard
> 2024 Month
> 1
> Stats
> Rank:
> 1,066
> Score:
> Alphas:
> Level:
> No Level
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 1,142
> Total Active Alphas
> Total Decommissioned Alphas
> Total Alphas
> 1,148


二、连续运行能力和handle重连的能力


> [!NOTE] [图片 OCR 识别内容]
> [62]
> 707m 45.0s
> <Response
> [201]>
> siulation
> 0
> t0
> 10 prepared
> simulation
> Sent
> Simulation
> 0
> done
> Simulation
> 1
> done
> simulation
> 2
> done
> simulation
> 3 done
> Simulation
> 4
> done
> simulation
> 5
> done
> siulation
> 6
> done
> simulation
> 7
> done
> Ulation
> 8
> done
> LIUlation
> 9
> done
> Siulation  10
> t0
> 20 prepared
> Simulation
> Sent
> Siulation
> 10
> done
> Siulation
> 11
> done
> Siulation
> 12
> done
> siulation
> 13
> done
> Simulation
> 14
> done
> Simulation
> 15
> done
> Siulation
> 16
> done
> simulation
> 17
> done
> siulation
> 18
> done
> Siulation
> 19
> done
> Siulation
> Sent
> Siulation
> 998
> done
> Siulation
> 999
> done
> Siml1ation
> 1000
> done



> [!NOTE] [图片 OCR 识别内容]
> 190
> Simulation
> 156
> done
> 191
> Simulation
> 157
> done
> 192
> Simulation
> 158
> done
> 193
> Simulation
> 159
> done
> 194
> Simulation
> 160
> t0
> 170 prepared
> 195
> Simulation
> Sent
> 196
> error
> ('Connection aborted。
> RemoteDisconnected
> Remote
> end
> closed connection
> Without
> response') )
> 197
> Response
> [201]>
> 198
> Simulation
> 160
> t0
> 170 prepared
> 199
> Simulation
> Sent
> 200
> Simulation
> 160
> done
> 201
> Simulation
> 161 done
> 202
> Simulation
> 162
> done
> 203
> Simulation
> 163
> done
> 204
> simulation
> 164
> done
> 205
> Simulation
> 165
> done


三、总结反思以及需要改进的点

代码效率尚可，大约3分半钟可以完成10个alpha的提交以及结果获取。由于现在我采用的代码只是简单的调用了multisimulation的方法，并没有做进一步的优化，因此实际还是在串行，在之后需要采用多线程的方式不断检查是否有空余的simulation机会，并进行单个提交。debug经历其实不多，在看懂官方给出的文档后仅花费不多的时间就能调试成功，属于复杂但不困难。但现在的代码仅处于可以运行，还并不能算elegant，之后的想法是改为.py脚本文件从而方便后台运行和参数的添加，也能提高效率。

本次使用的模版是最基础的120天的ts_mean，适用性比较广泛，任何时序的数据类型都可以直接使用，本次操作中，是先获取一定数量的datafield，然后将数据都处理成为可以放入模版的类型再进行simulation，在此后也可以考虑边处理数据边进行simulation的方式。总体来说，这个模版由于过于简单，获得的alpha合格率不是特别高，主要都是sharpe比较低，当然也有return尚可的一些例子，但年际差异较大，无法实际使用。

对于这个模版改进的方向其实主要是增加他的复杂度，因为实际上大部分指标直接取时序平均并没有很直接的意思，可能在其中叠加横截面rank，以及标准差等运算符能够带来更多的信息。总体来说还是需要从一些基本的逻辑出发来进行改进。


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> TRAIN
> TEST
> 15
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.82
> 1.879
> 0.86
> 13.849
> 22.779
> 147.709o。
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
> 1.59
> 1.95%
> 1.71
> 14.46%
> 4.45%
> 148.50%oo
> 1054
> 1217
> 2013
> 0.03
> 1.71 %
> 0.00
> 0.199
> 4.6796
> 2.199oo
> 1076
> 1235
> 2014
> 0.70
> 3.599
> 0.96
> 23.639
> 22.779
> 131.84%o0
> 1109
> 1242
> 2015
> 2.04
> 1.879
> 4.06
> 49.499
> 20.41%
> 530.54%oo
> 1114
> 1255
> 2016
> 0.66
> 1.499
> 0.58
> 9.51%
> 11.61%
> 128.06%o。
> 1083
> 1258
> 2017
> 0.00
> 1.699
> 0.00
> 0.049
> 11.619
> 0.49%o0
> 1044
> 1247
> 2018
> 2.25
> 1.61%
> 2.68
> 17.809
> 6.02%
> 221.39%o0
> 1092
> 1312
> 2019
> 0.23
> 1.36%
> 0.11
> 2.839
> 9.649
> 41.4596o。
> 1096
> 1282
> 2020
> -0.23
> 1.33%
> -0.10
> -2.179
> 6.339
> -32.7
> %oo
> 1081
> 1218


四、论文阅读

我阅读的是 [https://support.worldquantbrain.com/hc/en-us/community/posts/15238260154007-Research-Paper-36-Quantitative-Fundamentals-Application-of-Piotroski-F-Score-on-Non-U-S-Markets](https://support.worldquantbrain.com/hc/en-us/community/posts/15238260154007-Research-Paper-36-Quantitative-Fundamentals-Application-of-Piotroski-F-Score-on-Non-U-S-Markets)

总结和体会：这篇文章主要通过应用Piotroski F-Score方法来分析非美国市场（BRIC、英国、德国），以确定该方法对产生Alpha的效果。结论是在非美国市场，具有高F-Score的公司在股票表现上较好，相较于对应市场指数表现，平均可实现8.2%的正收益（做多仓位）。相反，具有低F-Score的公司表现非常差，相较于对应市场指数表现，平均损失25.3%（做空仓位）。通过以上分析展示了Piotroski方法在非美国市场的适用性，能够通过买入持有交易策略产生Alpha。

构造alpha的idea：使用Piotroski F-Score来对非美国市场的股票进行筛选和投资，特别是在BRIC、英国和德国等市场。通过识别具有高F-Score的公司，并在长期持有的情况下，可以获得超额收益。因此，构建alpha的关键在于执行基于F-Score的投资策略，即长期持有高F-Score公司的股票，同时做空低F-Score公司的股票，以实现市场超额收益。

---

### 评论 #103 (作者: WL13229, 时间: 2年前)

[BC25356](/hc/en-us/profiles/13921805253911-BC25356)

这个帖子有一些关于获取datafield的代码，可以查看：

[[L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md]([L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md)

希望对你有帮助

---

### 评论 #104 (作者: WL13229, 时间: 2年前)

@ [IC51680](/hc/en-us/profiles/20023801895447-IC51680)

依然建议尽量从头搭建框架，即便模仿ACE library也会比直接使用得要好。因为在后续课程不断增加内容的过程中，你可能会发现debug的难度在增加。

---

### 评论 #105 (作者: DL92496, 时间: 2年前)

第一部分：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 5,509
> Total Active Alphas
> 64
> Total Decommissioned Alphas
> Total Alphas
> 5,573
> 23:10
> 星六
> 2024/3/9


Total Alphas如上图。

这次测试使用的模版是ts_skewness(vec_avg({x}), {y})作为测试基础，x为数据集变量，y为时间变量，生成Alpha List，最后调用ace lib里面的simulate_alpha_list_multi仿真。关键代码如下图。


> [!NOTE] [图片 OCR 识别内容]
> S[taodg
> Ots+
> Ot
> dlchyat-a(
> Mha
> cdn
> Iao
> uoowl
> oo [Uota
> Eonl(hs (ohao o
> NR Wutag [
> a
> Tom
> VCC
> Icy]hg
> T  |s| Le el((%|9;^
> cgNo U
> ue
> TRA
> VEC Ct
> N
> TocM L
> nT Wwo (
>  (
> ?
> UCo
> Bo]e(
> Tcmndommous Lotonm
> Noat [o
> U
> 0
> TLCC
> OU teO JO
> 0 [
> TN
> V
> o
> TeeoTsCgo
> SUaggoe
> Loo
>  _
> ! | .『
> Iel(6280
>  |+ !
> O』寻;
> 罩』
>  +U
>  |
> #& |
> 51159
> oU』
> 7
> k
> Toes
> To U
> 4768915
> 700
> RtA
> rttc
> I InuntT
> OT 
> 
> k
> .
> ee
> 
> (
> 2 .
> sUoIlo *0
> do
> Ua|
> UUN
>  4
> 7
> 9818


下图为仿真的状态，正在仿真，已经不间断运行超过1000次。


> [!NOTE] [图片 OCR 识别内容]
> u+LUlate uuhastSULtJ
> 
> 
> OULtJsLULatJon
> T TT
> Fh
> 4
> 6
>  |
> T6
> @;
> FT 110
> 1
> 4


第二部分：

阅读文献：

Healy, Brian and O'Sullivan, Conall, Dividend Capture Returns: Anomaly or Risk Premium? Evidence from the Equity Options Markets (February 8, 2019). Michael J. Brennan Irish Finance Working Paper Series Research Paper No. 19-2, Available at SSRN:  [https://ssrn.com/abstract=3337964](https://ssrn.com/abstract=3337964)  or  [http://dx.doi.org/10.2139/ssrn.3337964](http://dx.doi.org/10.2139/ssrn.3337964)

总结如下：

这篇文章研究如何利用期权市场的信息来预测除息日当天的预期回报。研究发现，对于交易难度较大、风险较高或股息较少的股票，除息日的回报可能会更高。论文使用Option Metrics 的数据库中的数据，该数据库包含期权价格及其相关股票的信息，但论文只研究了个股的期权，而不是股票组或其他类型的期权。

交易难度较大通常指的是缺少流动性的股票，缺少流动性意味着很难买入或卖出；风险的判断有两个指标，一个是观察个股有没有与市场无关的价格变化，另外一个是透过Beta系数，Beta系数越高意味着股票价格对市场变化更加敏感；股息较少的股票的衡量标准是观察股息是否低于市场水平。文章中主要使用个股数据不包括ETF和ADR。使用的指标包括每天开盘和收盘价格，文章只关注现金分红而忽略其他其他派息事件。文章也关注每天收盘的期权价格、隐含波动率、Delta、Vega和Gamma。

---

### 评论 #106 (作者: ZY25767, 时间: 2年前)

我有一个问题，就是如果setting不变，改变alpha的生成规则，会被算作同样的alpha嘛？

---

### 评论 #107 (作者: WL13229, 时间: 2年前)

[ZY25767](/hc/en-us/profiles/17488901499543-ZY25767)

本次作业不要求改变setting，仅改变Alpha表达式即可。不同表达式，就是不同的Alpha，不会算作同样的。

---

### 评论 #108 (作者: YJ78324, 时间: 2年前)

**必做1：**

1. 批量提交前的截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 18,832
> Total Active Alphas
> 10
> Total Decommissioned Alphas
> Total Alphas
> 18,842
> 16:29
> Cd
> 2024-03-10


1. 批量提交后的截图


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 21,172
> Total Active Alphas
> 10
> Total Decommissioned Alphas
> Total Alphas
> 21,182
> 19:32
> 英
> Cr d)
> 2024-03-10


1. Alpha提交输出截图


> [!NOTE] [图片 OCR 识别内容]
> Finish:
> 2317
> Alpha ID:
> OVGOA22
> Finish:
> 2318 Alpha ID
> 9JVObBX
> Finish:
> 2319 Alpha ID
> PASMEKO
> Finish:
> 2320 Alpha ID
> Vdkxxea
> Finish:
> 2321 Alpha ID:
> EKVPYGP
> Finish:
> 2322 Alpha ID
> PASMEAj
> Finish:
> 2323 Alpha ID:
> GkdsYe0
> Finish:
> 2324 Alpha ID:
> n3K5Y8d
> Finish:
> 2325 Alpha ID:
> pgPeokj
> Finish:
> 2326 Alpha ID
> NAQIqK7
> Finish:
> 2327
> Alpha ID:
> 2JOOQOY
> Finish:
> 2328 Alpha ID
> 9JVobjv
> Finish:
> 2329 Alpha ID: GkdsyxQ
> Finish:
> 2338 Alpha ID
> VdKXXAA
> Finish:
> 2331 Alpha ID:
> EkVPYmg
> Finish:
> 2332 Alpha ID:
> 1JXA11]
> Finish:
> 2333 Alpha ID:
> OorXqMy
> Finish:
> 2334 Alpha ID
> EKVPYML
> Finish:
> 2335 Alpha ID:
> Akg8YSe
> Finish:
> 2336 Alpha ID
> pgPeoe6
> Finish:
> 2337
> Alpha ID: ddorgrv
> Finish:
> 2338 Alpha ID
> QE3pjzg
> Finish:
> 2339 Alpha ID:
> OVGOVIV
> Finish:
> 2348 Alpha ID:
> ZrOVXYI


1. 总结

年前参加了第一次的英才候选人计划，当时因为时间原因没能完成最后一次的作业。此次重新参加这期活动，一方面是补上之前的课程，一方面也想进一步巩固一下之前学到的知识。模板自动化提交方面，我这周也进行了简单的优化，可以通过配置更加方便的对多个搜索字段进行填充，另外也在异常处理方面做了一些优化，现在可以稳定连续的进行Alpha提交了。

**必做2：**

本次我阅读的研报是来自太平洋证券的 **《基于交易异常的广义反转因子》**  ，这篇研报主要研究了基于交易异常的广义反转因子在A股市场的表现。研报中通过多种指标来刻画交易异常，包括收益分布的时间刻画（如隔夜-日内收益角力）、收益分布的离散度刻画（如强弱信息系数）、收益分布本身的刻画（如修正偏度）以及交易行为异常的刻画（如非流动性、异常成交量等）。

在多种因子中我选择了Attention因子进行了分析。Attention因子是用来衡量股票收益分布的异常性，特别是极端日度收益对投资者关注度的影响。这个因子基于行为金融学中的前景理论，该理论认为投资者在决策时会对小概率事件给予更高的权重，从而高估这些事件发生的概率。这种行为偏好可能导致投资者对某些股票的反应过度，从而产生预期收益率的反转效应。

具体来说，"Attention"因子的计算方法如下：


> [!NOTE] [图片 OCR 识别内容]
> Attentiomi;t
> (Riit
> 瓦)?


这个因子的核心思想是，极端的日度收益（无论是正的还是负的）容易吸引投资者的注意，从而影响他们的交易行为。在收益率分布上，这种关注度与收益率之间呈现出U形的曲线关系。通过这个因子，研究者试图捕捉这种关注度变化对股票未来表现的影响。

下图给出了搜索到最高夏普率的PnL


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 12M
> 11M
> 1OM
> 9,00OK
> 8,00OK
> 7,00OK
> OOOK
> 5,00OK
> 4,0OOK
> 3,00OK
> 2,00OK
> 12/26/2012
> 1,00OK
> Pnl: 1,204.41k


---

### 评论 #109 (作者: YZ31807, 时间: 2年前)

1.
 
> [!NOTE] [图片 OCR 识别内容]
> WORLDOUANT
> BRAN
> Simulate
> Alphas
> Data
> Competitions (3)
> Events
> Learn
> y
> Refer a friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 365
> Show
> 10
> Out
> Filter
> Unsubmitted。
> 355
> Active:
> 15
> Select Columns
> atus
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> Olec
> Search
> Selec
> Selec
> e 8>
> e.8>
> e.8>
> JTOTTJITIOUs
> ReBUIaT
> UNSUBMIT
> 03/08/2024 EST
> CHN
> TOP3000
> 0.89
> -5.629
> 2.0096
> anonymous
> Regular
> UNSUBMIT
> 03/08/2024 EST
> CHN
> TOP3000
> 0.25
> 1.84%
> 2.589
> anonymous
> Regular
> UNSUBMIT
> 03/08/2024 EST
> CHN
> TOP3000
> -0.38
> -1.629
> 1.93%
> anonymous
> Regular
> UNSUBMIT
> 03/08/2024 EST
> CHN
> T0P3000
> -1.16
> -4.999
> 2.519
> anonymous
> Regular
> UNSUBMIT
> 03/08/2024 EST
> CHN
> TOP3000
> 0.99
> 2.929
> 2.589
> anonymous
> Regular
> UNSUBMIT
> 03/08/2024 EST
> CHN
> TOP3000
> -1.75
> 7.1396
> 2.5996
> anonymOUs
> Resular
> UNSUBMIT.
> 03/08/2024 ESI
> CHN
> T0P3000
> 2.31
> -6.23%
> 2.4796
> 1OCC
> 10:24
> 晴朗
> 搜索
> 英 谷g) O
> 2024/3/9
  
> [!NOTE] [图片 OCR 识别内容]
> 0
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 1,460
> Show
> 10
> Filter
> Unsubmitted:
> 1,450
> Active:
> 15
> Select Columns
> atUs
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> Felect
> Search
> SOleC
> SeloC
> e.吕 >
> 58
> e.吕 >
> aTOTIYITOUS
> ReBUIaT
> UNSUBMIT
> 03/10/2024 EDT
> CHN
> T0P3000
> -0.53
> -5.3696
> 8.98%
> anonymous
> Regular
> UNSUBMIT
> 03/10/2024 EDT
> CHN
> TOP3000
> -0.17
> -1.26%
> 6.61%
> anonymoUs
> Regular
> UNSUBMIT
> 03/10/2024 EDT
> CHN
> TOP3000
> -0.05
> -0.41%
> 6.659
> anonymous
> Regular
> UNSUBMIT
> 03/10/2024 EDT
> CHN
> T0P3000
> -0.01
> -0.10%
> 6.5596
> anonymOUs
> Regular
> UNSUBMIT
> 03/10/2024 EDT
> CHN
> TOP3000
> -0.03
> -0.3196
> 6.639
> anonymous
> Regular
> UNSUBMIT.
> 03/10/2024 EDT
> CHN
> T0P3000
> -0.06
> -0.58%
> 6.68%
> 寺 apiworldquantbrain.com..
> Resular
> UNSUBMIT.
> 03/10/2024 EDI
> CHN
> T0P3000
> 004
> 0.33%
> 676%
> CNYIJPY
> 19.44
> -0.569
> 搜索
> 英  谷d匈
> 2024/3/10
> OUT
> Tag


本次1000次回测中我的alpha来源于【alpha灵感】单因子测试之财务质量因子。财务质量因子是一类比较重要的风格因子，可以反映企业过去的经营状况和未来的持续盈利能力，这些信息能够在一定程度上影响股票的价格。而由于财务信息具有一定的滞后性，财务因子也需要与其他因子进行结合。

rank(mdl175_roediluted*mdl175_cashrateofsales)。这个是文章中基本模型，考虑到大小盘的财务质量差异，利用group_neutralize进行处理，得到了group_neutralize(rank(mdl175_roediluted+mdl175_cashrateofsales), my_group)。在我的100次回测中，我利用get_datafields分别获取roe和cashrateofsale的数据，进行两两随机组合构建了不同的alpha进行回测。

总结与反思：

代码效率：一次性跑了1200次回测，共历时1h30min左右

Debug经历：在第一次的回测中出现了“强迫关闭现有连接”的问题，但过一会儿重新运行这段请求代码发现一切正常，目前没有太明白为什么出现这个情况，希望老师可以解答一下。 
> [!NOTE] [图片 OCR 识别内容]
> File
> lanaconda3 ILib Isite-packages Irequests ladapters. Oy: 513,
> in HTIPAdapter. send (self,
> request
> stream,
> timeout;
> Verify,
> Cert
> proxie
> 510
> raise RetryError (e,
> reqlest=reqlest )
> 512 if isinstance (e
> LeaSOI,
> _PrOxJEIrOI )
> 513
> raise ProxJError
> request=request)
> 515 jf isinstance (e.reason;
> SSLEIIOI )
> 516
> # Ihis branch is for UII1ib3 Vl.22 and Iater
> 517
> raise SSLEIrOr
> reqlest=reqlest)
> ProxyErrOr
> HIIPSConectionPool (host=' api
> VOIIdquantbrain. COm'
> DOrt=443)
> Max retries exceeded with
> lr1:
> /authentication
> (Caused by Proxy
> Error (' Canot
> COnnect
> to DrOXJ
> ConnectionResetError (10054,
> 远程主机强迫关闭了一个现有的连接。
> None,
> 10054,
> Vone)) )


Alpha改进思路：目前考虑除了将财务数据与cashrateofsale结合外，考虑将其与其他基本面数据结合或者添加其他的财务质量数据如现金流动比率等，提高alpha整体的稳定性。

2.

我阅读了 [Bid and Ask Prices of Index Put Options: Which Predicts the Underlying Stock Returns?](../顾问 CC40930 (Rank 95)/[L2] Research Paper Bid and Ask Prices of Index Put Options Which Predicts the Underlying Stock ReturnsPinned_15233936157847.md) ，这篇文章分析了期权在看跌时期买入价与卖出价的波动率对未来股票超额收益的关系以及预测能力的比较。考虑到经济衰退期间和中间资本风险不断增加，以及其关于未来市场方差风险溢价的信息更丰富，卖出价更可能具有较强的预测能力。通过对 S&P500 指数深度价外（OTM）看跌期权买入价和卖出价的隐含波动率的估算，得到了卖出价的隐含波动率比买入价的隐含波动率对股票收益的预测能力更强。本篇文章的研究方法如下：

1. 引入Intermediary Asset Pricing Model用于解释买入卖出价与未来回报的关系
2. 利用线性回归检验买入价与卖出价的波动率与预期收益的关系
3. 采用employ Newey and West t-statistics进行假设检验
4. 通过回归分析与假设检验，卖出价的变化了在对于未来收益的预测显著性水平为5%。这反映了该指标与Intermediary Asset Pricing Model模型的吻合，是一个优秀的预测手段

Alpha idea：根据论文的数据集构建方式，可以建立在看跌期期权卖出价格的波动率的计算模型，以此构建alpha。

---

### 评论 #110 (作者: ZY25767, 时间: 2年前)

这次作业整体收获还是很大的，主要是懂得了API的使用方法，但感觉很希望可以参考研究员后续比较完全健全的框架，来提升速度。

这是最开始的：


> [!NOTE] [图片 OCR 识别内容]
> marks
> Window
> Help
> ZOOm
> 回
> 囤
> l)s
> [5]
> C 0 ? AA Q @
> Sat Mar 9 8:30 PM
> platformworldquantbrain.com
> 89
> 十 @
> GT MFE
> CMU
> HackerRank
> Apple
> iCloud
> Bing
> Uchicago
> 乙 英才候选人计划实.
> API 可以实现的功能
> API 及日常回测时常
> Brain API 技巧:  如。
> (Alpha 灵感]  合集
> Research Paper 73:..
> WorldQuant BRAIN
> has
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 408
> Filter
> Unsubmitted:
> 401
> Active:
> Btus
> Date Created
> Region
> Universe
> Sharpe
> Returns
> Turnover ?Tag
> Decommissioned:
> 0
> (EST)
> Plect
> Search
> Select
> Select
> e.8>1
> @.8〉1
> e.8〉1
> Select
> anonymous
> Regular
> UNSUBMITTED
> 03/08/2024 EST
> USA
> TOP3000
> 0.12
> 1.00%
> 0.779
> anonymoUs
> Regular
> UNSUBMITTED
> 02/04/2024 EST
> USA
> TOP3000
> 0.60
> 5.859
> 79.159


这是现在最新的


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Data
> { Competitions (3)
> EVents
> Q
> Alphas
> Unsubmitted
> Submitted
> Total: 1,422
> Show
> 15
> out
> Unsubmitted:
> 1,415
> Active:
> 7
> Select Columns
> ItUS
> Decommissioned:
> 0
> Plect
> anonymoUs
> Reguar
> JNSUBMITTED
> anonymous
> Regular
> UNSUBMITTED
> 0
> LIAICIIRAAITTCT


1. 自动登出的问题：解决办法就是每一次回测前sign in一下

2. 建议有一个官方的API文档可以说明rate的个数。现在我发现还是很慢。我对多线程还是不够了解，只是将notebook多开几个来不断的去跑。的确发现速度不够。

3. 希望有一个online server可以使用。

第二部分：

我阅读的论文是

# Research Paper 73: Uncertainty Resolution Before Earnings Announcements


> [!NOTE] [图片 OCR 识别内容]
> U C
> {_上^C
> CLL <1 LCLLLLC)
> 11^ CLLJ CLL ^ C
> (1
> LLL81LL)
> <<1 ~ LCLCCL)
> (上
> CLL
> 上 < 0
> Cc C上〈上上1
> 9<上^L1<
> CL
> CC
> 979.
> 4
> Pre-announcement Returns and the Uncertainty Resolution Hypothesis
> 4.1
> The Average Pattern of Pre-announcement Returns
> Here We define the
> earnings announcement date as day 0, and the period from
> -10 to
> +10,
> OI the [-10,
> +10] window,
> as the
> 21-day window around earnings announcements。
> We first
> compute the abnormal daily returns (AR) by subtracting the CRSP value-weighted daily market returns
> from the stock daily returns, then obtain the cumulative abnormal returns (CAR) [-10,+10] between
> -10 and
> +10 by compounding the daily
> abnormal returns。
> The returns
> around earnings
> announcements, CAR [-10,+10], have a
> median of 0.0379 and a mean Of 0.3599/, suggesting
> positive skewness in the announcement premium。
> To illustrate the dynamics Of the returns around earnings announcements, we plot the average
> CAR across firms for the [-10,+10] window i Figure 1. The average CAR increases steadily from
> There are fewer stocks with the OptionMetrics data early i our sample period, but there are still 584 stocks per
> quarter on average before 2000.
> 12
> Electronic copy available at: https:/lssrn.comlabstract-3595953
> day
> day
> day
> day
> pooled
> day



> [!NOTE] [图片 OCR 识别内容]
> Here, the subscript d denotes
> d in the lagged three-quarter rolling window. Uncertaintyia is the
> uncertainty
> measure Of stock ifor
> d, and VIXa is the close Value Of VIX for
> d.
> We
> estimates
> With
> fewer
> tan
> 20
> observations
> 边
> the  lagged rolling window。
> With
> te
> estimated
> and
> 边 quarter 9,
> We
> decompose firm-level uncertainty
> at
> 11
> before
> the earnings
> announcement
> 0 i quarter 9,
> Uncertaintyi,-I1, into two
> market
> firm-specific
> Uncertaintyi,-Il
> -
> Uncertauntymqrl
> 十
> Uncertautyir
> (14)
> market
> with
> Uncertaltymall
> 二
> (15)
> firm-specific
> market
> and
> Uncertautyi,-ll
> T
> Uncertaintyi,-II
> Uncertaintyma
> (16)
> We then re-estimate the Fama-MacBeth regression specified by Equation (7), and replace the
> market
> firm-Specific 25
> uncertainty measure Uncertaintyi-11 with Uncertautymrk
> and
> Uncertawtyfirn
> The results are reported in Table 10. For brevity, we only report the results based on IVOW as
> the uncertainty
> Ieasure
> As Shown
> i the table; market-wide and idiosyncratic uncertainty have
> comparable impacts on the pre-announcement returns and change in implied volatilities before earnings
> releases. For an interquartile change in market-wide and idiosyncratic uncertainty, the impacts on the
> day
> day
> day
> drop
> lorq
> lirq
> day
> day
> Parts:
> luq
> VIX-11,


总结如下：

这篇论文讲的是根据Earnings Announcements构建的一个因子。我仔细阅读了前半部分，发现他的研究方式像是event study的感觉。

抛开理论的部分：我感觉这个文章提到了一个构建因子的方法；也就是收集 公告日 前10到后10天到[-10, +10] 收益并且用这个收益变化减去平时到收益变化绝对值，得到一个BETA表明这个股票对于 公告日来临这个时间点敏感程度。（这里可以用历史数据来进行分析）。然后根据论文的说法，这里有一个positive skewness in the announcement premium.意味着越敏感（因子值越大的股票），在这段时间的超额收益就越高。

然后我们根据这个因子值多空组合，看看表现如何。

存在的疑问：

如何将不好的研报结果的负收益情况隔离开来？我的想法是第一种可以区间放到【-10，-1】或者，通过对冲抵消这个影响。

---

### 评论 #111 (作者: WL13229, 时间: 2年前)

[ZY25767](/hc/en-us/profiles/17488901499543-ZY25767)

很好的思考，您提出的问题，我们将在后续课程中给出解答。也欢迎您在课程中与我们一同讨论。

---

### 评论 #112 (作者: WL13229, 时间: 2年前)

[YZ31807](/hc/en-us/profiles/18243220367511-YZ31807)

这是正常的报错，无论你是否在每次simulate前都sign_in，都逃脱不了这个4小时的强制断连。解决的办法是，使用try except方法，当报错时重新登录，直到成功即可。

我们会在下节课给出展示demo。欢迎你现在就进行尝试。

---

### 评论 #113 (作者: WL13229, 时间: 2年前)

[YJ78324](/hc/en-us/profiles/12940496308759-YJ78324)

欢迎回来，我对您有印象。似乎是在GA课程之前就没有看到您继续了。不知道上次GA的课您上了吗？相信这一次，你一定能找到更多的Alpha

---

### 评论 #114 (作者: WL13229, 时间: 2年前)

[ZY25767](/hc/en-us/profiles/17488901499543-ZY25767)

一个简单的思考是，如果您认为某个部分会亏钱，那么反着做，不就赚钱了吗？不过话说回来，如果想隔离，那么可以在最后赋值的时候，使用if_else，把它们变成nan即可。从文章的意思看，似乎您有一个performance的图片没有上传。

---

### 评论 #115 (作者: WM13885, 时间: 2年前)

**Task 1**


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 10
> OUt of 846
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
> SearCh
> Selec
> Selec
> Selec
> SearCh
> Selec
> Selec
> e.吕>1
> e.吕>1
> e8>1
> Se
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.04
> 0.21%
> 3.6796
> anonymoUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.11
> 0.63%
> 4.50%
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.13
> 0.72%
> 1.68%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.15
> -0.87%
> 1.82%
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.43
> 2.4996
> 1.66%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.13
> -0.71%
> 1.65%
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.13
> 0.72%
> 5.3496
> anonymoUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.00
> 0.02%
> 4.14%
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.00
> -0.00%
> 2.449
> 3:32
> 1 0  e
> @ W
> 2024/3/10
> Tag
  
> [!NOTE] [图片 OCR 识别内容]
> WORLDOUANT
> BRNN
> Simulate
> Alphas
> Data
> 召 Competitions (3)
> Events
> Learn
> Refer a friend
> 0 Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 10
> Out Of 1,852
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
> SearCh
> Selec
> Selec
> Selec
> SearCh
> Selec
> Selec
> e8>1
> e.g>1
> e8>1
> Se
> anonymOUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.17
> 0.6596
> 6.0596
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.32
> 1.18%
> 5.70%
> anonymOUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.27
> 1.25%
> 1.19%
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.14
> -0.62%
> 2.15%
> anonymOUs
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> 0.30
> 1.39%
> 1.77%
> anonymous
> Regular
> UNSUBMITTED
> 03/09/2024 EST
> USA
> TOP3000
> -0.22
> -0.849
> 1.27%6
> DnrrIr
> IINCIIRNIITTFn
> nDIO7n)^
> CCT
> Tpnnnn
> 031
> O0I
> 010
> 4:32
> 囟  @
> 2024/3/10
> Tag


一个小时左右跑完1000个，使用的template用于测试程序，并不复杂。用rank对analyst15跑了前1000个数据字段。因为担心漏跑几个alpha所以之后又补了个对simulation的追踪。 
> [!NOTE] [图片 OCR 识别内容]
> Datafiels
> anll5_bps_Br_ 12_mIm_ChB test
> SUCCZEO
> Datafiels
> anl15_bps_gr_12_M_3m_Che
> CEST
> SUCCSEC
> Datafiels
> anl15_bps_Br_12_#Gm_Chg test
> SUCCZEO
> Datafiels
> an115_bps_gr_12_m_COs
> TEST
> SUCCSEC
> Datafiels
> anl15_bps_gr_12_m_COS_
> TEST
> SUCCZEO
> Datafiels
> anlI5_bps_gr_12_m_COS_
> UP TEST SUCCZEC
> Datatiels
> 3n115_bp5_
> Er_12_n_ests
> test
> SUCCEE
> Datafiels
> anl15_bps_gr_12_M_Ssts_dn
> test
> SUCCEEO
> Datafiels
> an115_bps_gr_12_m_Sro
> TEST
> SUCCZEO
> Datafiels
> anlI5_bps_Br_12_mmean test SUcceed
> Datafiels
> anl15_bps_Br_12_m_st_dev test
> SUCCZEO
> Datafiels
> an115_bps_gr_12_m_Tr_
> Iean
> test
> SUCCEEO
> Datafiels
> anll5_bps_Br_18_mIm_ChB
> TEST
> SUCCZEO
> Datafiels
> anlI5_bps_Br_18_m3m_Chg test
> SUCCSEC
> Datatiels
> anl15_bps_gr_18_m_Gm_Chg
> TEST
> SUCCZEO
> Datafiels
> anlI5_bps_Br_18_mCOs test
> SUCCSEC
> Datafiels
> 31715_bps_gr_18_"_COS_
> TEST
> SUCCZEO
> Datafiels
> an115_bps_gr_18_m_COS_
> UP TEST
> SUCCSEC
> Datafiels
> 31715_bps_gr_18_m_Ssts_
> test
> SUCCEE
> Datafiels
> anl15_bps_gr_18_M_Ssts_
> test
> SUCCEEO
> Datafiels
> an15_bps_gr_13_M_JE
> TESt
> SUCCZZC
> Datafiels
> anl15_bps_gr_18_M_ST_JeV TEST SUCCEEd
> Datatiels
> anlls_bps_gr_18_m_Total
> tEST
> SUCCEZC
> Datafields anlls_bps_gr_CaI_Tyg_SrO
> CEST
> SUCCSEC
> Datafiels
> anllS_bps_gr
> Cal_TyG_JE
> tEST
> SUCCEZC
> Datafields
> 3n115_bp5_
> ind_Cal_Fy3_3m_Chg
> TeST SUCCeEJ
> Datafields anlls_bps_inc_CaT_Fy3_Gm_Chg TesT
> SUCCSEJ
> Datafiels
> 3n115_bp5_
> Inc_CaT_Ty3_
> C05
> test
> SUCCEE
> SImULateJ 193 Times SUCCESSTUIIy


对于代码效率这块，用的都是论坛上导师post的api使用方法和流程的代码稍微加工，也通过在跑代码的过程中在网站上尝试simulation得到simulate too many times error确认10个回测同时占用率。过程中的bug也通过自查+gpt比较顺利的解决。

下一阶段的目标就是用更复杂的template以及数据字段做更具economic sense的回测，筛选并提交有效alpha。

**Task 2**

选择的文章是【Alpha灵感】A股换手率类因子 Post by KJ42842。以下是12个换手率因子，自己也尝试用fast expression复现些：

 
> [!NOTE] [图片 OCR 识别内容]
> 困表1:
> 华泰单因子测试一换手率因子及共描述
> 大类因子
> 具体因子
> 因子描迷
> 1m
> 个股最近 N 个月内日均换手率
> turn_3m
> N=1,
> 3,
> 6
> turn_Gm
> bias_turn
> 1m
> 个股最近 N 个月内日均换手率除以最近2年内日均换手率,
> 再减去1
> bias_turn_3m
> N=l,
> 3,
> 6
> 换手率因子
> bias_turn_Gm
> (Turnover
> std_turn
> 1m
> 个股最近 N 个月内日换手率序列的标准差
> Factor)
> std_turn_3m
> N-l,
> 3,
> 6
> std_turn
> Gm
> bias_std_turn_Im
> 个股最近 N 个月内日换手率序列的标准差除以最近2年内日换手率序列的标
> bias_std_turn_3m
> 准差。再减去1
> bias_std_turn_Gm
> N=1,
> 3,
> 6
> turn_
 
 
> [!NOTE] [图片 OCR 识别内容]
> turnover
> Volume /sharesout;
> turnover_5
> ts_mean ( turnover
> 5);
> turnover
> ts_mean(turnover
> 22);
> turnover_long
> mean(turnover
> 256);
> 5td_
> turnover
> 5 = ts_std_dev(turnover, 5);
> 5td_
> turnover_22
> ts_std_dev (turnover
> 22);
> 5td_
> turnover_Ion
> ts_std_dev(turnover,
> 256);
> bias
> turnover_5
> turnover_S/turnover_Ion -1;
> bias_std
> turnover_5
> 5td
> turnover_S/std
> turnover
> -1;
> Iong
 

这篇帖子给了我很多启发，尤其是关于优化和提高Alpha模型鲁棒性的部分。虽然原始的换手率因子在Fast Expression中复现并不困难，但作者的重点在于如何结合研报内容对其进行优化。

在分析为何原Alpha未达到Robust Universe Return标准时，作者认为这可能与A股市场的特性有关。作者假设主要问题在于原Alpha过度做空了很多换手率较小的小市值股票以获取大部分收益，而这部分收益在真实交易中无法实现。为了验证这一假设，作者重新阅读了关于换手率的研究部分（及各行业换手率均值差异）

 
> [!NOTE] [图片 OCR 识别内容]
> 囝表3:
> 各一级行业 turn_Im bias_
> turn_Im std_turn_Im bias_std_turn_Im 中位数比较 (2016/12/30)
> 2.0%
> turn_Im
> std_turn_
> 1m
> -0.3
> bias_turn_Im(右轴)
> bias_std_turn_Im(右轴)
> -0.4
> 1.59
> -0.5
> 1.09
> -0.6
> -0.7
> 0.59
> -0.8
> 0.0%
> -0.9
> 鬓
> 绶荽
> 暴
> `
> 毖
> s
> 蒌o粪`蕊芟
> k4蓠
> 类
> "
> 薏
> u!
> -
> $
> 
> `


并进一步利用经济常识验证了小市值股票换手率通常较高的情况。为了证实观点，作者采用了power rank的方法，放大了个股换手率的差异，从而优化了原Alpha模型，使新Alpha能够更集中地做空换手率较高、市值较小的企业。随后，由于换手率因子在大盘股中效果较差而在中小盘股中效果较好，为进一步提高IS ladder sharpe的表现，作者采用了right_tail operator来剔除换手率较低的大盘股（噪音），最终使模型达标。

除了以上关于如何提高Robust Universe Return和剔除噪音的方法，作者对Alpha中性化处理以及选择短周期（如5天和22天）来增强Alpha信号的讨论也对我深入理解因子复现过程有很大帮助。可惜复刻后20-22年的表现达不到可以提交的标准，我也暂时没有想到提高IS ladder sharpe的方法，但还是强烈推荐这篇帖子给其他研究者阅读。

---

### 评论 #116 (作者: XH12546, 时间: 2年前)

**Task:1**


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant BRAIN
> https://platform worldquantbrain com/a.。
> A
> &
> 8 |
> 导入收藏夹
> 百度-下。你就知道
> WORLOOUANT
> BRAN
> Simulate
> Alphas
> Data
> 恩 Competitions (2)
> Alphas
> Total: 198
> Unsubmitted。
> 183
> Active:
> 15
> Decommissioned:
> Alpha Lists
> 22:28
> 中  瞬
> 2024/3/6
> 曷
  
> [!NOTE] [图片 OCR 识别内容]
> 骝
> IorldQuant BRAIN
> https://platform.worldqu...
> 导入收藏夹
> 舌庹-下。你就知道
> 骝
> ChatGPT
> 鬯哭
> Simulate
> Alphas
> Data
> 罟
> Alphas
> Unsubmitted
> Submitted
> Total: 1,282
> Show
> OUTI
> Unsubmitted:
> 1,267
> Active:
> 15
> Select Columns
> Decommissioned:
> 10:54
> @
> @
> 句)英  豳
> 2024/3/11


存在的问题：虽然使用了多线程进行数据获取，但模拟的发送仍然是按顺序进行的，未充分利用并行性能。

总结：1.通过随机洗牌DataFrame，增加了模拟发送的随机性;2.使用了函数封装和模块化设计，提高了可读性和可维护性;3.通过异常处理和延时机制，增加了代码的鲁棒性，使其能够更好地应对可能出现的问题。

**Task2:**

我阅读的论文题目是：Duration-Driven Returns久期驱动型回报

[Duration-Driven Returns by Niels Joachim Gormsen, Eben Lazarus :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3359027)

在这篇论文中，作者提出了一个基于久期的解释，旨在揭示主要股票因子（包括价值、盈利能力、投资、低风险和支付因子）溢价背后的谜题。文章通过投资于近期内获得大部分现金流的公司来解释这些因子的表现，并认为这或许是由于对近期现金流的溢价所致。

首先，作者明确了股票因子（价值、盈利能力、投资、低风险和支付因子）投资于在近期内获得大部分现金流的公司的特性。这种特性可能引发对近期现金流的溢价，从而影响这些因子的回报。通过对单一股票股利期货数据的分析，作者发现，在公司内部，个别现金流的预期CAPM阿尔法随着久期的缩短而减小。这一结果有力地支持了他们的基于久期的解释框架，表明投资于近期现金流的公司可能获得更高的回报。

在更为具体的分析中，作者通过估计CAPM betas，将月度回报对市场回报进行回归，并考虑市场滞后项，来验证他们的观点。为了简化模型，他们强制规定了最后三个滞后项具有相同的斜率参数。研究结果显示，阿尔法与公司的其他特征（如价值、盈利能力、投资、低风险和支付）无关，而与久期有关。这进一步强调了久期在解释股票因子溢价中的重要性，排除了其他特征的影响。

此外，作者详细介绍了他们对到期收益率beta的计算方法，使用了平均beta来衡量给定条带剩余寿命的期望阿尔法。这一方法使得他们能够更精确地理解股票因子溢价与久期之间的关系。

总结：这篇论文为投资者和金融从业者提供了一种新的视角，揭示了久期对主要股票因子溢价的影响。通过对股利期货数据的独特运用，成功解开了股票市场中一个重要而复杂的谜题，为未来的投资策略和市场理解提供了有价值的参考。

---

### 评论 #117 (作者: WH24469, 时间: 2年前)

**必做1：**

1.提交前：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Achievements
> m
> l
> 20
> 100
> GOOO
> Tool Unsuhmedu
> NPhas
> TOI DCOMISSTCA 42275
> Total Nphas
> 7,067
> G
> 50244N


2.提交后


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Status
> Total Unsubmitted 4lph3s
> 8,285
> Total Active Alphas
> TOalDecommlssloned Alphas
> TOtaIAIphas
> 8,295
> 10.18
> 中 ~d0
> 2024//11
> See


3.连续不断提交：


> [!NOTE] [图片 OCR 识别内容]
> 51841110
> TUCCNTTUY
> 409C
> S1_?__ehr
> SinlutaT
> Sebt SCCeSSWIL':
> ULII Ca1 12 Cb
> Siwluton !113 e succeytully:
> 4115L_V_Csl 4y2 Ccht
> 2LnT
> TaTn
> 4115_5_e_5]_ 173_5
> 470I+T
> TTCrrm
> ull5_Lps_V_C31_12_-t
> 51a111101
> 0!
> 21115_b_
> 「T
> 511110
> 1:1:
> 115 U
> elIy20
> 4701+NT
> 1118 so
> TCF
> 415_Eps_V_Col_13pe
> siwlsa
> 1
> 4115_6
> elIy
> 5111101
> e61 SCCerstlly; Jll5_Lp_ir_Cal_tyi_totil
> 3i1110
> SUCCesSuIly
> 2115 L
> Csl {g3_ICL
> 4701++AT
> tl: ills_bs_
> ty_i_chi
> SIIALLO
> Seb? SLCCeSSUIY: MLIgCTV_CSI_I
> 515111101
> TNh! TLCCNTUY
> 9115_5_i_Sl_Iy?_s
> Sinlator
> Sebt SCCeSSWIIY
> ULTICCT C31 +1-sts
> Siwlata !13 {1:
> 04115 h
> Iy3_pro
> 5141+10
> ~
> v115_b_p_e
> Uynr
> 5111501
> MCCNSTILLY
> J1TC
> Cal {IFe
> [IT]
> SU
> Tt :
> ? A0
> ZU2MJI


目前采用方法为使用for循环从始至终将全部数据都遍历并带入表达式中，如果提交失败就跳过，并显示fail；如果遍历程序中断，也可以从中断的index重新开始，但对于与表达式适配的数据类型的判断还需进一步完善，现在还无法直接提取适配的datasets。第二个问题就是遍历速度较慢，由于没有使用多线程，将全部数据遍历完所需时间较长，而网站在4hour后会自动断开，代码需要构建实时判断连接状态模块，并在断开时自动重连。

4.总结与反思：

（a）对于代码效率，由于采用for循环的方法，效率较低，采用多线程将节省更多的时间，对于数据的选取没有针对性，全部数据都遍历一遍虽然利于研究哪些数据更适合表达式，但花费的时间较多。

（b）Debug_1，当限制总的提交数量total_wanna_sim_num时，程序设定的是当sim_n 到达这个数字时，程序停止，但真正运行时，sim_n超过了total_wanna_sim_num程序仍然在运行。


> [!NOTE] [图片 OCR 识别内容]
> i si_n <二 total
> Vama_sinun
> for datasets_nw in range (len (datasets_id_list)):
> print(f" datasets
> {datasets_id_list [datasets_nw] } begin
> print {datafields_df_} {datasets_Juw})
> i len (datafields_df_1 [datasets_nu] )
> 0:
> print(" 战为空
> Continue
> for
> in list (datafields_df_1[datasets_num] ['i' ].ralues)
> i si_n
> <
> start_nw
> Dass
> else
> simulation_data


修改后代码结果如下图：


> [!NOTE] [图片 OCR 识别内容]
> alpha_ 旺
> pd.Datarrane (is_result)
> print (alpha_Af.colwus)
> Print (len(alpha d))
> Jlpha_l_liet.append(alpha  茈)
> Jou
> OTOCCSs
> TCSOUJSC
> fter
> Jeegeu
> 3tatus
> True
> ?1_
> Cc !
> print(f Jlready simwlate {total_
> TITTI7
> 3I IlI
> alpha
> brenk
> breyk
> Print
> Done
> Jataset
> aalyetl1 besin
> Silation
> CPTI
> successfully: 2l11_2le
> 5113t1o
> SPTI
> succe3stully: al11_2_1
> Siaulation
> eTit
> succeasfully; 3111
> LIpn
> Siulotion
> Sent
> succeesfull: 21112Itic
> Silation
> SCIIt
> Successfully: 2111
> Siulstion
> SeJit
> successtully: 2111_2_22
> Siulatior
> aent successfully: 3111
> Zpne
> Siulotion
> (
> succeastully: 5111
> 2tic
> Silotion
> CCT
> successfully: 2111_23
> SI4O
> 3P1
> successfully: al11_2_3
> Aleady ?iulse 10 slpha
> Dons


成功解决问题并能获取到程序停止时的datafields名字。

（c）Debug_2，原先的框架并没有获取出每个datafields的is_result的DataFrame，调整框架后，结果如下：


> [!NOTE] [图片 OCR 识别内容]
> 4111_2_1的i_rsult_#f:
> boolsize
> lonsCout
> ehortCotmt
> tznoyer
> Yetne
> nawlowm
> 1914105
> 2OOOOOO
> 1515
> 1357
> 0225
> 0192
> 1051
> 1914105
> 2OOOOOO0
> 1518
> 1367
> 0225
> 0192
> 1061
> 1914105
> 2OOOOOO0
> 1518
> 1367
> 0225
> 0192
> 0.1051
> 1914105
> 1518
> 0225
> 0192
> 1061
> 1914105
> 20oooo
> 1518
> 1367
> 0225
> 0192
> 1061
> 1914105
> ZOOOOOO
> 1515
> 1357
> 0225
> 0192
> 1061
> 1914105
> 2OOOOOO
> 1518
> 1367
> 0235
> 1061
> 1914105
> 2OOOOOO0
> 1513
> 1367
> 0225
> 0192
> 1061
> 1914105
> ZOOOOO0
> 1518
> 1367
> 0225
> 0192
> 1061
> 1914105
> 2ooOOOO0
> 1518
> 1367
> 0226
> 0192
> 1061
> 1914105
> ZOOUNMO
> 1515
> 1351
> 0225
> 0.0192
> 1051
> 1914105
> 2OOOOOO0
> 1515
> 1367
> 0235
> 0192
> 0.1061
> Mar%in
> fithess
> sharpe
> stzrt0it
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001693
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 2012-01-22
> 001698
> 0.24
> 2012-01-22
> 0.001698
> 0.24
> 0.52
> 2012-01-22
> Chechs
> I32
> LOt_SILRPE
> Le3ult'
> EgIL'
> 1i 1
> 13e
> LOt_FITIESS'
> result'
> FI
> 1in
> IaE
> Loy_TIIRNOTBR'
> result
> Pg35'
> 11.
> uasr
> HICH_TRNOER
> Hesult'
> Pgss'
> I3Te
> COICEITRSTED_IICHT'
> result'
> Pus3'
> I22
> Lot_SIB_INIIERSE_SILRPE
> Lesult
> 1ae
> SELF_CORRELITIOI
> restlt'
> PEWDIIC'
> IaE
> PROD_CORRELITIOI'
> result'
> PEIDIIB
> u2
> RECU 珉_SUIBI[ISSION'
> reeult'
> PEWT
> I3Te
> JTCIES_COIPETITIOI
> result'
> 4氓
> IaSe
> ITCIS_IIIES'
> re3ult'
> ISIING
> nase
> IS_LIDDER_SIIFPE'
> restlt'
> FyII
> Simulation 2
> PFTT
> successfully: 3l11_2_18
> 提取2111_2_13的i_result
> ZOOOOO0
> 135


可以看到anl11_2_2e这个datafields的is_result_df。

（d）模板适配的数据类型：

由于模型较简单，且原模型是用于衡量市盈率的，所以适配的数据多属于anl14及anl15类的数据，如下图：


> [!NOTE] [图片 OCR 识别内容]
> Flelds
> Datasets
> Search
> Coverase;
> Type
> Jmas
> Users
> anl4
> Clear
> Oatasol
> Feld
> Descnption
> Ty
> Covuage
> 00135
> StImUons Oir  Funimrnls
> O
> TNII
> upcoming?
> TUIAIN
>  CTOI
> 921
> Snl Cstluc T
> CIIUal<
> UPCONIT OCr:
> VeCOT
> anll! octaluc np f
> Ntproft
> Tczenlstouurter
> Iazm
> 91
> onll4 hoh Copextp4
> THI41n
> Expend IUTes
> Lm
> 50
> URSI.
> gUdne
> anll4_estvolueHpl
> Csma27 oly ?
> Upcomne CUgper
> CCtOT
> Snll4_Actrolue_etUJIp0
> Earnins
> 3rInr
> '
> Derreasgon
> Lr'
> SITINOA
> TNCATUISNRNT
> unllactalue ey TO
> Curni Per SJrt
> TeCentIy:cJgrer
> Iaur
> onlls_ocolue_np_NO
> Netprol
> TCenISLYCO
> Lr'
> anll4_actolUC_CbLpO
> CAIIIZ
> STCIncicn:
> Tcs
> TCCCn;IS
> UuT'
> TUgreT
> onlio_syoup
> TTIITM
> URCOIIIR
> 741A
> CTI
> Uor
> LSc
> oCep



> [!NOTE] [图片 OCR 识别内容]
> group_rank (ts_av_diff (anlls_bpsgics_ind_12
> ests_叩
> 480),subindustry )
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Tmmcation
> Neutraliation
> Pasteurization
> NaN Handling
> Unt Handling
> Equit
> US:
> T0P3000
> Fst Eresslan
> Market
> Venf
> Clone Alpha
> N Chart
> Pnl
> SOo
> OOOK
> Gog SUug
> SUUC Nb



> [!NOTE] [图片 OCR 识别内容]
> Sea「ch
> COMerage
> Tye
> Nphas
> sers
> anlts
> Clear
> 0at4so1
> Felu
> IIcIUI
> TyR
> Covuagt
> 1(
> Mphs
> Eamings forcc-r
> 01156p5_8_12_0_55_
> Th 12msrthfonordproradtoslnurberof
> Nur
> 100
> LSIN15 hhhJCCNJCedSCLIS
> MANIh MIh G C
> STCUD STOUPIR
> Jlt5bps 8 18 m_Im_chg
> The welshted
> Tone
> OCTen
> Chsngeo1g
> Nas
> 100。
> MTthonggtSo Voluc CT
> shgreEps]
> csmozn SRRTCRStcd whin CICS sroup
> TTOURITC
> 005_005_8_8N_S_OC
> The weBhed JVeTOBC Sondard Ceaton
> Naon
> 100』
> MAACh CIAdCDOk VolUe2e ShJrel75
> esmg2n
> wn GICSBroup
> Frzupir
> Jnlt5_aps_8_al_H3_
> The olnumorofolondmedhr sler
> NT
> 100
> EookVoluc PeshArCBPS]CsmnonwhIn GICS
> SSUP OrOURTR
> Jnlt5 bps BCal LOvel
> The WCIBhC
> JerdR
> UOOR VJlUC DC
> Ng
> 100。
> SdclSPS
> OTTnCr~nCl-nom
> GcalyCarJSrcSaed wthin GICSsroup groupins。
> 90I15_bps_Or_Clfyz_co
> Te CUmber
> COMONICTUCh
> CIenned ?
> 100*
> TSCOLYCATLDOK VAIUC CCTSIATC
> CSUNA[
> WhnGCSBrOUP BroUPITB
> CSJd
> Lm



> [!NOTE] [图片 OCR 识别内容]
> G Open alpha details in new tab
> Code
> Broup_rank (ts_av_diff(anll4_meanrating, 480),subindustry)
> simulation Settings
> Instrumont Typo
> Rowon
> UNors
> LnUago
> Ocoy
> Dolay
> Tncaton
> Noutrlizaton
> Pastwurtaton
> NaN Hndlnq
> Unt Hndlnq
> Equb
> U5
> T003009
> Fast Epresslcn
> Warker
> Venty
> Clone Alpha 
> N Chart
> Pnl
> 2OOOK
> SOOK
> PedSNLMSUJ
> SLU NON


（d）模板改进方向：


> [!NOTE] [图片 OCR 识别内容]
> 4PASS
> 3FAIL
> Sharpe Of1.16
> belowCUOToi 1.58
> Fmess Of0.5215 below CUtoff of1。
> SlddcrShoroe Of026
> belowCUOffof 1.58 for ladderyear 2: 1/24/2022
> 1125/2020
> 2 WARNING
> 3PENDING



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> ABBreBate
> Data
> Sarpe
> TUTnOer
> Hnes
> RPTUTn
> OTaWUIn
> Iarcp
> 1.16
> 2.7796
> 0.52
> 2.499
> 4.36%
> 17.93900
> Vear
> Sharpe
> Turmover
> Ftness
> Returs
> Orawdown
> Margi
> Long Count
> Short Count
> 2012
> 7SE
> 101%
> 1.71
> 5.195
> 30*
> 75.35
> 1433
> 121
> 2013
> 239
> 332
> 512
> 117
> 30.84
> 145
> 136
> 201-
> 2.17
> 32-5
> -7
> 1.721
> 77.64
> 1451
> 1373
> 2015
> 1.27
> 3.079
> 062
> 7.943
> 1.26*
> 19.16
> 1450
> 1400
> 2016
> 1.13
> 1050
> 07
> 36
> ~19.81
> 1459
> 1376
> 2017
> -7
> 783
> 4.745
> 1.79*
> 33.54
> 141
> 136-
> 7013
> 0.13
> 3.159
> 0.373
> 5
> 735
> 1553
> 1426
> 2019
> 1.77
> 2254
> 3.885
> 1-?
> 34515
> 1540
> 1405
> 2020
> 1.019
> 0.55
> 3.051
> 051
> 60.32
> 1+-5
> 1330
> 2021
> 0.73
> 1.829
> 00+
> 333
> 1?
> ,185
> 1302
> 1202
> 2022
> 3.37
> 0359
> ~273
> 6.449
> 53
> 365,03
> 1155
> 1242


目前的模板过于简单，只是求出现值与两年前的值的差值后进行平滑，Sharpe和Fitness都不符合要求，模板基本思想是偏向于基本面类的，那么是否可以考虑融合其他模型，例如CAPM模型等进行优化。

**必做2：**

我阅读的文章是： [【方正金工】显著效应、极端收益扭曲决策权重和“草木皆兵”因子——多因子选股系列研究之八 - 研报 - 一起量化 17quant.com](https://www.17quant.com/post/%E3%80%90%E6%96%B9%E6%AD%A3%E9%87%91%E5%B7%A5%E3%80%91%E6%98%BE%E8%91%97%E6%95%88%E5%BA%94%E3%80%81%E6%9E%81%E7%AB%AF%E6%94%B6%E7%9B%8A%E6%89%AD%E6%9B%B2%E5%86%B3%E7%AD%96%E6%9D%83%E9%87%8D%E5%92%8C%E2%80%9C%E8%8D%89%E6%9C%A8%E7%9A%86%E5%85%B5%E2%80%9D%E5%9B%A0%E5%AD%90%E2%80%94%E2%80%94%E5%A4%9A%E5%9B%A0%E5%AD%90%E9%80%89%E8%82%A1%E7%B3%BB%E5%88%97%E7%A0%94%E7%A9%B6%E4%B9%8B%E5%85%AB.html)

此篇文章首先考虑一个常见的月度反转策略，即常用的20日收益率alpha，该传统反转alpha的逻辑认为，过去20天里，收益率相对较高的股票，其未来表现会相对较弱，而收益率相对较低的股票，其未来表现相对较好。因此如果采用20日收益率的传统反转因子来进行选股，投资者会买入过去一个月收益较低的股票，类似于反转alpha，但是这一思想会使投资者将相邻两个交易日的alpha赋予相同的权重，这有悖于最初逻辑，所以“原始惊恐度”alpha作为对传统alpha的优化，同时也衡量市场对这个标的价格的过度反应程度，其放大了常用的20日收益率alpha的时间颗粒度，考虑每个交易日交易者的过度反应程度。

文章首先计算“惊恐度”alpha，基于“惊恐度”构建多样的加权决策分，利用决策分的移动均值和标准差的等权求和来衡量每个交易日过度反应程度：

- 将每日股票收益率（今收/昨收-1）直接作为当日股票的决策分。
- 将每日的“惊恐度”与每日的收益率相乘，得到加权调整后的决策分，简称“加权决策分”。
- 每月月底，分别计算过去20个交易日的“加权决策分”的均值和标准差，分别作为对“20日收益率因子”和“20日波动率因子”的改进，分别记为“惊恐收益”因子和“惊恐波动”因子，并将二者等权合成为“原始惊恐”因子。

Alpha Idea：文章中的原始惊恐度利用的是收益率数据，而决定收益率的一个重要因素包括成交额，且成交额中包含丰富的信息，这些信息收益率是无法单独体现的，所以考虑将收益率换成成交额，构建一个新的衡量市场情绪的alpha。文章周期统一采用20个交易日，属于中短期alpha，而对于反转，有大周期和小周期的反转，参数飘逸无法把握，是否能剔除该参数带来的不稳健性。

---

### 评论 #118 (作者: BL43673, 时间: 2年前)

TASK1


> [!NOTE] [图片 OCR 识别内容]
> 0
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 2,035
> Show
> 10
> Out
> Filter 
> Unsubmitted:
> 1,997
> Active:
> 38
> Select Columns
> atUs
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Decommissioned:
> 0
> Jelect
> Search
> Select
> Select
> e.8>1
> e.8>1
> e.8〉1
> Select
> anonymoUs
> RegwIar
> UNSUBMITTED
> 03/05/2024 EST
> USA
> TOP3000
> 0.12
> 1.009
> 0.779
> anonymous
> Regular
> UNSUBMITTED
> 11/14/2023 EST
> CHN
> TOP3000
> 2.80
> 29.909
> 11.849
> anonymous
> Regular
> UNSUBMITTED
> 11/14/2023 EST
> CHN
> TOP3000
> 2.84
> 30.819
> 11.959
> anonymous
> Regular
> UNSUBMITTED
> 11/14/2023 EST
> CHN
> TOP3000
> 1.73
> 13.61%
> 14.919
> anonymous
> Regular
> UNSUBMITTED
> 11/14/2023 EST
> CHN
> TOP3000
> 1.82
> 14.029
> 13.509
> anonymous
> Regular
> UNSUBMITTED
> 11/14/2023 EST
> CHN
> TOP3000
> 1.66
> 12.83%
> 13.919
> anonymoUs
> Regular
> UNSUBMITTED
> 11/13/2023 EST
> CHN
> TOP3000
> 2.75
> 28.909
> 11.749
> anonymous
> Regular
> UNSUBMITTED
> 11/10/2023 EST
> CHN
> TOP3000
> 2.20
> 17.719
> 11.609
> 80C
> 8:30
> Q
> 搜索
> 中  谷 dx 匈
> 多云
> PRE
> 2024/3/6
> Tag



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> 10
> out of 4,034
> Filter


主要是参考了【Alpha灵感】新闻动量文章启发的反转策略实现这篇文章的模板，尝试了sentiment相关的不同datafield，找到效果最好的几个然后调整了一下中性化的方法，最终得到了一个可以提交的alpha。 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 8,00OK
> 6,00OK
> 40OOK
> 2,0OOK
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
 一开始是用的每次回测十个alpha的方法，结果回测2000次花费了五个多小时，后面询问chatgpt+查看论坛之后学习使用了多线程，现在2h10min就能完成2000次测试。中间遇到过一些多线程中tqdm卡住无法继续以及缺少限制使代码进入死循环无法结束等问题，但都通过各种方法解决了。

之后希望能继续精进一下我的回测框架，争取把网页上能做的操作都用api实现一遍。

TASK2

我看的文章是开源金工组的《大小单重定标与资金流因子改进》 [大小单重定标与资金流因子改进 | 开源金工 (qq.com)](https://mp.weixin.qq.com/s/0FRlMiZkJXihzGi9LaTofw)

最基本的资金流因子构造方法如下：


> [!NOTE] [图片 OCR 识别内容]
> 表1:  大单资金流因子常见的几种定义方式
> 因子代码
> 因子筒称
> 计算公式
> Net Intlow
> C (B:-s;)
> 净流入
> (NI)
> 其中,
> 8;和5;分别表示大单资金在交易日[的买入金额和卖出金额。
> Net Inllow Ratio
> (NIR)
> 净流入率
> C" (Bi-SD/C" (B:-
> + Si)
> Net Inflow PCT
> C (Bi -
> SII
> Float
> 净流入占比
> (NIPCT)
> 其中,
> Float
> 为股票的流通市值。
> Net Intlow
> ACT
> 乙 Bacri
> SACT ,i
> 主动净流入
> (NI
> ACT)
> 其中
> BACT ;和SACT ;分别表示大单资金在交易日[主动买入金额和主动卖出金额。
> Net_Intlow_Ratio
> ACT
> 主动净流入率
> SACTi)
> |i
> Bacr i + SAcTi
> (NIR
> ACT)
> Net Inllow PCT
> ACT
> 主动净流入占比
> SAcTi) |MVpree Float
> (NIPCI
> ACI)
> 资料来源:  开源证券研究所,
> 回溯窗口 N 通常设为20个交易日
> MVpree
> MVrree
> (BACTi
> BACT1


我自己也在brain平台尝试了最基本的NIR，但我可能对英文的datafield理解存在一些偏差，我并不知道我使用的datafield是不是对的......


> [!NOTE] [图片 OCR 识别内容]
> CTaT
> Pnl
> 6,00OK
> 5,0OOK
> 4,00OK
> 3,000K
> 2,00OK
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


不过确实是有效果，但Sub_Universe_Sharpe无法满足要求。

研报中还介绍了如何用MOD方法去净化资金流，消除alpha中的反转效应，通过用当日ret对ln(B/S)回归得到的残差重新分配买卖的比例，来完成MOD方法。


> [!NOTE] [图片 OCR 识别内容]
> (1) 统计每个交易日的大单买入和大单卖出的成交金额,
> 记为和5;
> (2)逐个交易日计算下列回归方程,
> 并取残差项8作为修正系数;
> In(B /5) = a + R X Ret + 8
> 其中, Ret为当日涨跌幅。
> (3)基于修正系数反算大单买入和大单卖出的比例关系,并重新分配大单买入和卖出的成交
> 金额。
> e
> 合 =
> C X (B+5)
> 1 + ec
> 1
> $ =
> X (B+S)
> 1 + ee


目前因为时间原因还没有尝试使用该方法，如果有效的话可能就可以获得一个可以提交的alpha了。

但在这里我有疑问：这样子使用残差重新分配买卖单为什么就能排除掉alpha中的反转因素呢？文章中好像也没特别阐明。

另外，文章中还提出重新划分大小单，文章中认为以2万为界限划分大小单是最有效的。但是我目前在平台的数据中好像没有找到相关的数据，等有空再去翻找一下。

---

### 评论 #119 (作者: WL13229, 时间: 2年前)

[BL43673](/hc/en-us/profiles/18478216550679-BL43673)

我尝试将您的问题和原文输给GPT，得到了如下的答案

> 文章提到的使用残差重新分配买卖单以排除Alpha中的反转因素，实际上是基于一种统计方法来分离和剥离因子中的特定成分。这里的主要思想是利用截面回归模型来识别并分离出资金流向数据与股票未来涨跌幅之间的关系，尤其是去除那部分因为市场反转趋势而产生的Alpha效应。
> 简而言之，通过回归分析，文章尝试将资金流向的影响分解为两部分：
> 1. 与股票未来涨跌无直接关系的部分，即所谓的“纯净”Alpha部分，反映了主力资金流向本身对股票未来价格的预测能力；
> 2. 与股票未来涨跌有关的部分，主要是市场的反转因素，比如说因为股票价格短期内涨得过快而可能面临的回调压力。
> 通过回归分析，可以用来预测股票涨跌的独立变量（比如资金流向指标）与股票实际涨跌幅之间的关系被量化和识别。回归模型的残差部分（即实际观察值与模型预测值之间的差异）被认为是剥离了已知影响因素（比如反转趋势）之后的纯净效应。因此，将基于残差调整的买卖单数据用于进一步的分析和因子构建，理论上可以得到一个更为净化的、专注于捕捉主力资金流动性影响的Alpha因子。

---

### 评论 #120 (作者: YW65260, 时间: 2年前)

**必做1：**

截图1： 
> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> C
> Alphas
> Data
> upyter
> Casel
> Logout
> enU
> Trusted
> on 3
> Alphas
> Run
> Code
> Total: 2,874
> except Exception
> 85
> e
> print (f"alpha
> {counts}
> break。
> Unsubmitted:
> 2,819
> print (' connection dow'
> in0)
> Active:
> 35
> Decommissioned:
> 20
> IIICU
> (
> [
> ( (!
> UI工 工)
> Dha 169
> sent successfully.
> pha 170
> sent slccessfully.
> pha 171
> Sent
> slccessfully.
> Alpha Lists
> pha 172
> Sent
> successfully
> Dha
> 173
> sent successfully.
> pha
> 174
> sent slccessfully.
> Filter 
> pha
> 175
> Sent
> Successfully
> Dha 176
> sent slccessfully.
> Dha 177
> sent successfully.
> pha
> 178
> sent slccessfully.
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> pha 179
> Sent
> successfully
> Dha
> 180
> sent successfully.
> Search
> Select
> Select
> Select
> Search
> pha 181
> sent slccessfully.
> Dha
> 182
> Sent
> Slccessfully
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> Dha 183
> Sent
> successfully.
> Dha
> 184
> sent successfully.
> anonymoUs
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> pha 185
> sent slccessfully.
> pha 186
> Sent
> successfully。
> pha 187
> Sent
> slccessfully.
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> 0o
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> 14:33
> PRE
> PDF
> 英  谷 dx O
> 2024/3/11
> sign


截图2：


> [!NOTE] [图片 OCR 识别内容]
> InU
> Trusted
> Python 3
> Alphas
> &
> Run
> Code
> Total: 3,703
> print (' connection
> down )
> sign_in()
> Unsubmitted:
> 3,648
> Dha
> g8U
> Sent
> SUCCeSSfUIIJ
> Active:
> 35
> pha 981
> Sent
> slccessfully。
> Decommissioned:
> 20
> pha 982
> sent successfully
> pha 983
> Sent
> Successfully。
> pha 984
> Sent
> slccessfully。
> pha 985
> Sent
> slccessfully。
> Alpha Lists
> pha 986
> Sent
> Successfully。
> pha 987
> Sent
> slccessfully。
> pha 988
> Sent
> slccessfully
> Dha 989
> Sent
> slccessfully
> Filter 
> pha 990
> Sent
> slccessfully。
> Dha 991
> Sent
> slccessfully。
> pha 992
> Sent
> slccessfully。
> Dha 993
> Sent
> slccessfully。
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Dha 994
> Sent
> slccessfully。
> Dha 995
> Sent
> successfully。
> Search
> Select
> Select
> Select
> Search
> pha 996
> Sent
> slccessfully。
> Dha 997
> Sent
> slccessfully。
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> pha 998
> Sent
> Slccessfully.
> pha 999
> sent successfully。
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> [*]:
> anonymous
> Regular
> UNSUBMITTED
> 03/11/2024 EDT
> 19:11
> @  英 谷 dx 匈
> 2024/3/11


（由于截图1 忘记从一开始算的时候截了，所以这个差值少了些）

体会：在课程之前对于python还有点生疏很多语句都是现学现用，结合老师们上课的分享以及评论区很多的优秀作业和ChatGPT的帮助，完成了代码的学习、debug和提交。由于时间仓促，目前我做的只是完成了流程，包括评论区说的各种优化和多线程的处理方式我还要继续改进。这里我选取的alpha模板是“ts_mean(rank(x),20)”

**必做2：**

我阅读的论文是：量化研究推荐论文中的“ESG Preference, Institutional Trading, and Stock Return Patterns”

背景：ESG评价体系可以帮助投资者和企业更全面地评估企业的绩效和价值观。这里ESG分为3个模块分别是环境E、社会责任S、管理G。所以ESG报告并不仅仅是财报，同样也是评价企业对社会可持续发展的概览，可以形成了对公司更全面的评价。

主要内容：本文探讨了ESG偏好对机构交易和股票收益模式的影响，发现ESG偏好能显著提高机构交易者的收益，研究SR机构持股与股票对收益公告反应不足的关系，使用标准化意外收益(SUE)和复合定量信号(SYY)作为关键指标。结果显示，SR机构持股越高，股票越倾向于对收益公告反应不足。

方法：使用ESG、SR_IO和SYY评分进行股票分类和排序，首先，根据SR_IO（社会责任投资机构持股比例，反映某只股票被社会责任投资机构看好的程度）评分对股票进行排序，将股票分为三个ESG组：低ESG组、中ESG组和高ESG组。对于高SR_IO股票，低估股票的表现优于高估股票，且高ESG组的表现最为显著。而在低SR_IO股票中，未发现误定价信号与回报之间的显著关系。这些发现支持了SR_IO作为SR投资者评估股票吸引力的更有效指标的观点。

其中 stock’s weekly returns：


> [!NOTE] [图片 OCR 识别内容]
> Ti,t = dj + RjRmt +
> 十 Sj,t
> 12=1
> 8Cn)
> Rmt-n


---

### 评论 #121 (作者: BC25356, 时间: 2年前)

**必做1: 阅读 [【Alpha灵感】论文/研报合集 – WorldQuant BRAIN]([L2] 【Alpha灵感启示录】100 从论文到alpha的复现持续更新收录中Pinned论坛精选_19348865150743.md) 或者  [Research Papers for Consultants – WorldQuant BRAIN，](/hc/en-us/community/topics/12997688420247-Research-Papers-for-Consultants) 选择一个你感兴趣的Alpha作为模板,并实现对该模板的1000次以上回测。**

**模版：**

```
group_rank(datafield, industry)
```

**前：**

```

```

**后：**

```

```

**连续性（不中断）：**

```

```

**必做2:** 阅读👉 [量化研究推荐论文 – WorldQuant BRAIN]([L2] 量化研究推荐论文论坛精选_21004691882135.md) 中的任意一篇论文，或者自行寻找其他材料（如研报、论文），总结论文的核心思路和Alpha Idea **(注意不要和本帖子或论坛中已被发布的重复）**

```
Paper Title：The Rewards to Meeting or Beating Earnings ExpectationsRUL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=247435Abstract:这篇文章研究的是公司未来表现和营收预期的关系，且有两个核心结论。首先，如果公司在上季度实际营收达到或超越预计营收，这些公司会比没有做到的公司有3%的Returns（季度）提升。其次，这些公司也展现自己出色的营收管理和预期管理。Main Context：研报提出了一个概念Market Premium，它被定义成“真实市场表现”与“分析师预测表现或市场预期”之间的差值。如果这个值是正的，就叫做Earnning Surprise。其需要被捕捉，因为它可以帮助投资去找到那些未来可能高价的股票和获取回报。Data：研报使用的数据是在1983年至1997年，来自75000个公司150000个季度盈利数据。但是文中并没有提及，公司的所在国，市值，行业。所以我们在Brain上可以需要用Global Universe。Main Idea: 买入上个季度实际达到或超越预计营收的公司股票，但是我们发现如果按照研报的数据只有3%的提升，没有显著变化。所以我们进一步考虑公司的研发投入，进一步强化“未来好”的信号。思考：1. 对于没有公布Earning Performance的公司怎么办？2. 对于已经公布的是不是有做假行为？如果用多维度去衡量？3. 公布的频次如果是一年一次怎么办？4. 是不是有更多指标可以参与进来，去找到“未来好”的公司？
```

---

### 评论 #122 (作者: BC25356, 时间: 2年前)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)

您好

> Step4: 使用代码获取该类型的所有数据集和大部分数据字段（datafield)

> Step5:  **对数据进行初步处理（例如vector data需要先使用vector operator降维）** Step6 **:** 将数据字段插入模板，批量生成Alpha表达式。

对于这个vector data我有两个处理办法

法一：在datafield筛选里面只选matrix数据，直接avoid vecto数据，但是这样并不是降维处理。

法二：

- **在获得数据时处理** ：我可以在获取datafield result那一步，直接把所有vector数据进行降维处理，把其字段直接替换成统一的降维数据(vec_avg(vector data))。

- **在simulate这一步处理** ：在进行simulate之前，也就是把datafield放入regular前，对数据进行判断，如果是是vector数据，则进行降维 (Example: vec_avg(vector data))。 ****因为我是直接用API获取所有数据字段 (e.g. ern1_revenue)****  **，所以如何在simulate这一步的时候，对数据进行判断？然后通过if语句进行编写？**

我更想在simulate这一步进行判断，有代码案例吗？

---

### 评论 #123 (作者: XL87358, 时间: 2年前)

**必做1：**

1.最近的截图


> [!NOTE] [图片 OCR 识别内容]
> 8*鄙
> 曰
> 72%
> 吕+
> 3月118周
> 15;51
> tted
> C 囤  众
> 囿
> 9
> 舀 Competitions (3)
> Events
> Learn
> y
> Refer
> friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> ShOW
> Out Of 507
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Unjverse
> Sharpe
> Returns
> Turnover
> Tag
> Searcn
> Select
> Select
> Select
> Searcn
> Select
> Select
> e.5>1
> e.5>1
> Select
> anonymoUs
> Regular
> UNSUBMITTED
> 0311112024 EDT
> USA
> TOP3OOO
> -0.14
> -0.39%
> 13.87%
> anonymous
> Regular
> UNSUBMITTED
> 03/1112024 EDT
> USA
> TOP3000
> -0.51
> 82%
> 14.17%
> anohymoUs
> Regular
> UNSUBMITTED
> 0311112024 EDT
> USA
> TOP3000
> 0.02
> -0.08%
> 14.26-
> anonymoUs
> Regular
> UNSUBIITTED
> 03/1112024 EDT
> USA
> TOP3000
> 0.25
> 25%
> 21.65%
> anohymoUs
> Regular
> UNSUBMITTED
> 0311112024 EDT
> USA
> TOP3000
> 0.33
> 62%
> 21.56%
> anonymous
> Regular
> UNSUBIITTED
> 03/1112024 EDT
> USA
> TOP3000
> 0.27
> 05%
> 17.01%
> anonymoUs
> Regular
> UNSUBMITTED
> 0311112024 EDT
> USA
> TOP3000
> 0.33
> -1.11%
> 15.55%
> anonymoUs
> Regular
> UNSUBIITTED
> 03/1112024 EDT
> USA
> TOP3000
> 0.23
> -0.97%
> 22.29%
> anohymoUs
> Regular
> UNSUBMITTED
> 0311112024 EDT
> USA
> TOP3OOO
> 0.20
> 0.71%
> 15.34%
> anonymous
> Regular
> UNSUBIITTED
> 03/1112024 EDT
> USA
> TOP3000
> 0.26
> 08%
> 14.73%
> Show
> OUT of 507
> TR
> Next


2.simulation后的截图


> [!NOTE] [图片 OCR 识别内容]
> 8鄙
> 100%
> 3月118周
> 19;10
> ted
> C 囤  &
> 回
> 8
> 舀 Competitions (3)
> Events
> Learn
> 《
> Refer
> friend
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> ShOW
> 0f 1,744
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST]
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Searcn
> Select
> Select
> Select
> Searcn
> Select
> Select
> e.5>1
> e.5>1
> e.5>1
> Select
> anonymoUs
> Regular
> UNSUBMITTED
> 03/06/2024 EST
> USA
> TOP3000
> 3.67
> 30.68%
> 36.70%
> aRORYIOUS
> Regular
> UNSUBIITTED
> 03/06/2024 EST
> USA
> TOP3000
> 3.67
> 30.68%
> 36.70%
> anohymoUs
> Regular
> UNSUBMITTED
> 03/06/2024 EST
> USA
> TOP3000
> 3.67
> 30.68%
> 36.70%
> anonymoUs
> Regular
> UNSUBIITTED
> 03/06/2024 EST
> USA
> TOP3000
> 3.67
> 30.68%
> 36.70%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/04/2024 EST
> CHN
> TOP3000
> 3.61
> 24.24%
> 12.95%
> anonymoUs
> Regular
> UNSUBIITTED
> 03/04/2024 EST
> CHN
> TOP3000
> 2.87
> 20.80%
> 76.10%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/04/2024 EST
> CHN
> TOP3000
> 2.87
> 20.80%
> 76.10%
> anonymoUs
> Regular
> UNSUBIITTED
> 03/06/2024 EST
> USA
> TOP3000
> 2.23
> 13.18%
> 38.79%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/06/2024 EST
> USA
> TOP3000
> 2.23
> 13.18%
> 38.79%
> aRORYIOUS
> Regular
> UNSUBIITTED
> 03/06/2024 EST
> USA
> TOP30O0
> 2.23
> 13.18%
> 38.79%
> Show
> OUT of 1,744
> [PROo
> 175
> Next


3.代码连续运行情况：

使用了参考模板

```
 Ts_Rank(rank(x), 20)
```

，选择基本面类型数据共计1278条datafields，回测时以10个Alpha表达式为一组，连续运行2个小时未中断并完成回测。


> [!NOTE] [图片 OCR 识别内容]
> epochlz6:
> 993
> 126/127
> [2:05:20<01:07。67.645/it]
> Alpha_WLZnqPI
> done 5imulating;
> getting alpha details
> Alpha
> EkpgIMp
> done 5imulating
> getting
> alpha details
> Alpha
> RdbzMvg
> done
> simulating,
> getting alpha details
> Alpha_gJjayoq
> done
> simulating
> getting
> alpha details
> Alpha_QEbZMpH
> done
> simulating,
> getting alpha details
> Alpha_RdbzMPe
> done
> simulating, getting alpha details
> Alpha_3ZXaw2Z
> done
> simulating, getting alpha details
> Alpha_lrvOdIx
> done
> simulating
> getting
> alpha details
> Alpha_RdbzMGI
> done
> simulating,
> getting
> alpha details
> Alpha_ddbEDNX
> done 5imulating
> getting alpha details
> epochlz7:
> 1003
> 127/127
> [2:06:10<00:00。59.615/i]
> a11_sUmmary
> Values (by= ' sharpe
> ascending=False)
> 36]
> 0.05
> alpha_id
> sharpe
> ftne55
> tUINOVeI
> retUTI5
> Urawdown
> margin
> XR3mrn
> 1.59
> 0.47
> 0.4627
> 0.0407
> 0.0186
> 0.000176
> PV2XRGN
> 1.48
> 0.38
> 0.5088
> 0.0330
> 0.0210
> 0.000130
> EkPINIK
> 1.39
> 0.37
> 0.4887
> 0.0351
> 0.0250
> 0.000144
> LkNIzn
> 1.29
> 0.27
> 0.7169
> 0.0319
> 0.0230
> 0.000089
> 2Jwaraw
> 1.24
> 0.33
> 0.4557
> 0.0328
> 0.0340
> 0.000144
> Gkb62YO
> 1.24
> 0.48
> 0.4676
> 0.0693
> 0.7035
> 0.000296
> OoNkbWb
> 1.30
> 0.83
> 0.1375
> 0.0555
> 0.5999
> 0.000808
> YObm20q
> -1.30
> 0.83
> 0.1375
> 0.0555
> 0.5999
> 0.000808
> YObmz0q
> 1.30
> 0.83
> 0.1375
> -0.0555
> 0.5999
> 0.000808
> OoNkbWb
> 1.30
> 0.83
> 0.1375
> 0.0555
> 0.5999
> 0.000808
> 1270 rOWS
> COUInS
> SOTt


4. 总结反思：

代码效率上未使用多线程进行回测，运行效率可能还没有达到最佳，暂时还不满意，会在后续边实践边修改代码。

主要遇到了如下的bug，首先是使用alpha_id = simulation_progress.json()["alpha"]在尝试获得id的时候返回Keyerror，但单独检查alpha表达式后发现可以正常回测，经排查发现是因为账号异常登出。使用try except语句在发生错误，重新sign in()再运行回测函数，保证代码不中断。

此外，还遇到一个很有趣的bug，即使用get_datasets(s, settings)函数获取的datasets的id有重名的现象，如出现两个‘fundamental13’，我通过list做切片的方法得到需要的datasets，但因为重名创造了一些重复的Alpha表达式，因此实际系统显示的Alpha数目小于程序模拟的1200多次。（可以看到get_datasets得到的重名数据集实际上是不同的，这些数据集有什么区别呢？此外使用API get_datafields(s, dataset_id='fundamental13')无法选择重名数据集）


> [!NOTE] [图片 OCR 识别内容]
> nale
> description
> category
> subcategory
> reglon
> delay
> UniVerse
> coVerage
> turnoVer
> Valuescore
> UserCount
> alphaCount
> fieldCount
> researchPapers
> The dataset
> Management
> Contains
> fundamental-
> fundamentall
> and Executive
> information
> fundamental
> fundamental-
> USA
> TOP3000
> 0.3191
> None
> 3.0
> Data
> about
> models
> Company:
> The dataset
> Management
> contains
> fundamental-
> fundamentall
> and ExecutiVe
> information
> fundamental
> fundamental-
> USA
> TOP3000
> 0.2584
> None
> 5.0
> Data
> about
> Iodels
> Company。
> The dataset
> [{'title':
> Comprehensive
> holds
> fundamental-
> fundamentall3
> Fundamentals
> fundamental
> fundamental
> fundamental-
> USA
> TOP30O0
> 0.7575
> None
> 350
> 54832
> 'Research Paper
> 15: Investor
> Dataset
> items
> data
> Behavi。:
> icluded
> The dataset
> [{'title':
> Comprehensive
> holds
> fundamental-
> 'Research Paper
> fundamentall3
> Fundamentals
> fundamental
> fundamental
> fundamental-
> USA
> TOP3000
> 0.3776
> None
> 5.0
> 39: Compound
> Dataset
> iems
> data
> Return。
> included


调试代码的时候还参考了如下文章做了尝试：

1. [【Alpha灵感】新闻动量文章启发的反转策略实现]([L2] 【Alpha灵感】新闻动量文章启发的反转策略实现_19353819839639.md)

ehat=ts_regression(returns,ts_delay({datafield},1),120);alpha=group_neutralize(-ehat,bucket(rank(cap),range='0,1,0.1'));alpha

数据类型采用了'news',  'sentiment', 'socialmedia'三种类型的数据。得到了少量高夏普的alpha，但数据字段的coverage不够，无法通过 [IS ladder Shar](/hc/en-us/articles/6726865162903) pe测试。

**必做2：**

**我阅读的文章是发表在JFE上的论文：《Good and Bad Uncertainty: Macroeconomic and Financial Market Implications》**

该文章认为宏观经济的不确定性可以分解为“好”和“坏”两种波动性成分，并将其与总增长和资产价格相关联。好的不确定性预示着未来经济活动的增加，如消费、产出和投资，并与估值比率呈正相关，而坏的不确定性预示着经济增长的下降，并压低资产价格。文章以90年代美国科技股泡沫和08年金融危机中雷曼公司倒闭为例，在第一种情况下，一个普遍的观点是，互联网将提供许多积极的增长机会，从而促进经济发展，但究竟有多少是未知的。这种情况称为“好的”不确定性。另一方面，第二个案例标志着全球金融危机的开始，随着随后出现的许多破产案例，人们知道经济状况正在恶化——然而，还是不清楚恶化了多少?这种情况是“糟糕”不确定性的上升。论文基于美国宏观消费数据，采用Long Run Risks model of Bansal and Yaron (2004)将消费数据的冲击拆解为好与坏两部分。

论文主要涉及的数据：宏观数据部分包括消费和产出数据，R&D投入、存量数据，工业生产数据（supplement the annual data on these macroeconomic measures with the monthly data on industrial production from the Federal Reserve Bank of St. Louis.）

“好”与“坏”的计算方法：y代表宏观变量（e.g., industrial production, earnings, consumption）∆y 代表 demeaned growth rate in y（zero-mean之后的growth rate）


> [!NOTE] [图片 OCR 识别内容]
> RVp;ttl
> 2
> (3.1)
> RVnttl
> C I(Ay+&
> (3.2)
> where I( ) is the indicator function and N represents the number Of observations Of
> y available during the year。
> 0)a+f'
> I(Aytts
> 0)Ayi-8'


Alpha Idea：我查看了brain平台的宏观数据集，似乎并没有与上述相关的数据字段。但可以借用论文的思想，即不确定性可以以好与坏相区别，在“好”的情况下，波动性越大，股票的预期收益可能就会越高；相对的，在“坏”的情况下，波动性的上升可能意味着股票正在进入一个坏局面。

使用平台简单实践一下：假如把good = ts_mean(returns, 2) < ts_median(returns, 20); 定义为一个好事件（某种反转信号？）那么采用good? rank(ts_std_dev(returns, 20)): -rank(ts_std_dev(returns, 20))

可以看到结果并不理想，换手率相对过高，可能相对于论文的成果，在概念定义、条件设置上过于简单，还有很多可改进空间。后续会继续沿着对不确定性内部结构进行分解的思路继续改进。


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DuT4
> OOOK
> 7OOOK
> DOoK
> OOOK
> DOoK
> OOOK
> OOOK
> OOOK
> Jan '13
> Jan'14
> Jan '15
> Jan '16
> Jan 17
> Jan '18
> Jan '19
> Jan 20
> Jan 21
> Jan 22
> IS Summary
> Period
> Aggregate Data
> Shrpe
> TUrnOver
> FItness
> Ae[UTIIC
> Dradown
> Mareln
> 1.45
> 67.15%
> 0.53
> 8.95%
> 9.16%
> 2.679600


---

### 评论 #124 (作者: WL13229, 时间: 2年前)

[JK19915](/hc/en-us/profiles/9476915930519-JK19915)

您好，请将作业发布至本评论区，无需另开新帖。我已为您复制粘贴以下您内容。

“

**我阅读的文章是：**  **ESG Preference, Institutional Trading, and Stock Return Patterns**

这篇论文探讨了社会责任投资机构（Socially Responsible，简称SR）持股对股票价格效率及市场信息反应延迟的影响，尤其是当市场环境中的资金流动性较低时，由这些机构大量持有的股票在应对市场信息变化时表现出更大的价格延迟。

具体来看，研究首先构建了一个模型来衡量股票回报受滞后市场回报影响的程度，即Price Delay（价格延迟），并采用每周回报数据计算每家公司在历年内的这一指标。结果表明，社会负责任投资机构所持股份越多的公司，在后期样本期间（2004年至2016年）对市场信息的响应速度较慢，表现为Price Delay增大；而在早期的安慰剂期则没有观察到类似效应。

进一步分析发现，当将样本细分为高SR持股与低SR持股两类时，在资金流动性较低的时期，SR持股对Price Delay的影响更为显著。这意味着在资金流动性受限的情况下，SR机构持有股份较多的公司其股价对市场新信息的调整更迟缓。

此外，论文还基于不同的评分体系如SUE和SYY等对公司进行排序，并对比不同SR持股水平的股票组合的风险调整后收益（Alpha）。结果显示，对于高SR持股的股票，基于SUE或SYY评分形成的多空投资组合具有显著的Alpha值，这反映了这些股票存在可预测的定价偏差，而低SR持股股票的Alpha值则不显著。这种差异可能源自于SR机构持股比例较高的股票由于潜在的卖空限制而导致定价失衡未能及时纠正。

**A**  **lpha idea:** 根据SUE或SYY等量化指标对公司进行排序，构建一个多空投资组合，长仓持有那些SR机构持股比例高且评分良好的公司股票，同时短仓持有同等数量的SR持股低但评分较差的公司股票。由于高SR持股公司的定价偏差可能导致市场对其价值评估存在延后，这样的策略有可能在一段时间内获取Alpha收益，特别是在市场条件不利于快速价格发现的时候。”

---

### 评论 #125 (作者: WL13229, 时间: 2年前)

[BC25356](/hc/en-us/profiles/13921805253911-BC25356)

您好，您关于论文的描述过于简短，请提供更多的细节。量化慢工出细活，欲速则不达。

关于您对代码的问题。我们在API帖子中关于datafield的获取代码，返回的dataframe中，是涵盖了数据类型（如vector，matrix等）的，建议通过此进行判断。

---

### 评论 #126 (作者: WL13229, 时间: 2年前)

[XL87358](/hc/en-us/profiles/20580060743447-XL87358)

可否进一步阐述该论文涉及到的数据？

---

### 评论 #127 (作者: JZ65525, 时间: 2年前)

大家好，这是我Case1的内容：

在simulation 1000 次之前我的状态是这样的：


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 1,546
> Total Active Alphas
> 13
> Total Decommissioned Alphas
> 
> Total Alphas
> 1,566


Simulation1000次后: 
> [!NOTE] [图片 OCR 识别内容]
> SuperAlpha Competition
> SuperAlpha Competition
> Alphas
> See all
> Leaderboard
> Leaderboard
> 2024 Month 2
> 2024 Month 1
> Status
> Stats
> Stats
> Total Unsubmitted Alphas
> 1,546
> Rank:
> 2,409
> Rank:
> 2,560
> Total Active Alphas
> 13
> Score:
> Score:
> 555
> Total Decommissioned Alphas
> Alphas:
> Alphas:
> Total Alphas
> 1,566
> Level:
> No Level
> Level:
> No Level
> Achievements
> View Achievements
> 20
> 18
> GOOD
> BXCELLENT
> SPECTACULAR
> 120
> 1:08
> 晴朗
> Q 搜索
> bol
> 中  拼   Cgd O
> 2024/3/12


以下是连续不断simulation 1000次的状态：


> [!NOTE] [图片 OCR 识别内容]
> 2024-83-12
> 88
> 19:
> 868
> INFO
> 登录成功
> 2024-83-12
> 88:28:80,451
> INFO
> 模拟请求成功,
> 模拟I0:
> mZmmpwl
> 2824-83-12
> 80:28:88,454
> INFO
> 模拟请求成功,
> 模拟I0:
> 7JNNW7V
> 2824-83-12
> 80:28:88,454
> INFO
> 模拟请求成功.
> 模拟I0:
> Mkaaook
> 2024-03-12
> 88:28:88
> 530
> INFO
> 模拟请求成功,
> 模拟I:
> PVz2NNq
> 2824-83-12 88:28:88,755
> INFO
> 模拟 mZmmpwl
> 完成
> 2824-03-12
> 80:28:01,076
> INFO
> 模拟
> 7JNNW7V
> 完成
> 2824-83-12
> 80:28:01,413
> INFO
> 模拟
> Mkaaook 完成
> 2824-83-12
> 80:28:01,605
> INFO
> 模拟请求成功,
> 模拟I0: ddbbpkJ
> 2024-83-12
> 88:28:01,727
> INFO
> 模拟 Pvz2NNq
> 完成
> 2024-83-12
> 88:20:02,058
> INFO
> 模拟 ddbbpkJ 完成
> 2824-83-12
> 80:28:03,321
> INFO
> 模拟请求成功,
> 模拟I:
> 5MZZXOZ
> 2824-83-12
> 88:20:03,376
> INFO
> 模拟请求成功,
> 模拟I0:
> 7JNNWb8
> 2024-03-12
> 88:20:03,633
> INFO
> 模拟
> 5MZZXOZ
> 完成
> 2024-83-12
> 88:20:03,901
> INFO
> 模拟请求成功.
> 模拟I0:
> VoaaVj8
> 2824-83-12
> 80:28:03,955
> INFO
> 模拟
> 7JNNWb8 完成
> 2824-83-12
> 88:28:84
> 259
> INFO
> 模拟
> VOaaVj8 完成
> 2024-83-12
> 88:20:06,360
> INFO
> 模拟请求成功。
> 模拟ID: kooodld
> 2024-83-12
> 88:28:06,726
> INFO
> 模拟 kQoodld 完成
> 2824-83-12
> 80:28:20,573
> INFO
> 模拟请求成功.
> 模拟I0:
> 3ZXXWeX
> 2824-83-12
> 80:28:20,752
> INFO
> 模拟请求成功,
> 模拟I0:
> OoNNO7R
> 2024-83-12
> 88:28:20,839
> INFO
> 模拟请求成功,
> 模拟I:
> a0bb67V
> 2024-03-12
> 88:28:20,911
> INFO
> 模拟
> 3ZXXWeX
> 完成
> 2824-83-12
> 88:28:21,271
> INFO
> 模拟
> OONNOTR 完成
> 2824-83-12
> 80:28:21,680
> INFO
> 模拟 aobb67v 完成
> 2024-83-12
> 81:04:40,590
> INFO
> 模拟请求成功,
> 模拟I0:
> Irvvgd8
> 2024-83-12
> 81:04:40,717
> INFO
> 模拟请求成功,
> 模拟I0:
> mZmmIpW
> 2824-83-12
> 81:04:40,892
> INFO
> 模拟
> Irvvgd8 完成
> 2824-83-12
> 81:04:41,192
> INFO
> 模拟
> mZmmIpW 完成
> 34,


总结反思：

首先，关于 **代码效率** ，我们尝试通过并发执行的方式来提高模拟运行的速度。通过使用 `concurrent.futures` 模块中的 `ThreadPoolExecutor` ，能够在多个线程中并行发送HTTP请求，这大大提高了执行模拟的速度。然而，并发也引入了复杂性，特别是在管理HTTP会话和处理异常时。在这个过程中，理解每个任务如何独立运行以及如何有效地同步和管理这些任务的结果变得至关重要。

其次，我的 **debug经历** 强调了仔细检查错误消息的重要性。例如，当遇到 `SSLError` 时，初步可能只是简单地认为是网络问题。然而，通过细致地检查错误类型和消息，可以发现是SSL协议或证书方面的问题。这要求对底层网络协议有一定的理解，并知道如何调整请求以满足特定服务器的安全要求。

关于 **模板适合的数据类型** ，当前的模板设计主要针对的是处理网络请求和响应的场景，特别是与REST API交互时。这适用于数据类型为JSON的场景，因为这是Web API最常用的数据交换格式。对于需要处理大量网络请求和期望异步处理这些请求的任务，这个模板特别合适。

最后，考虑到 **模板的改进方向** ，虽然当前的实现提高了任务执行的效率，但仍有改进空间。例如，错误处理可以更加细化，以便更好地处理和重试失败的网络请求。此外，当前模板在处理TLS/SSL配置方面比较静态，引入更灵活的配置选项可以让模板更加通用。进一步地，引入更高级的并发控制机制，如异步IO（ `asyncio` ），可能会进一步提高效率，尤其是在IO密集型任务中。

通过这次经历，我深刻认识到在设计和实现并发网络请求处理时，既需要关注效率和速度，也不能忽视安全性和错误处理的重要性。未来，继续探索更高效的并发模式和更精细的错误处理机制将是提升代码质量和性能的关键方向。

---

### 评论 #128 (作者: JZ65525, 时间: 2年前)

大家好，这是我Case2的内容：

我阅读了文章《Online reviews can predict long-term returns of stocks》。本文通过分析机构投资者的决策型交易，探讨了机构投资者的信息优势对股票价格效率的影响。研究发现，具有未来收益相关信息的投资者会利用这些信息来策略性地调整过去的决策，进一步将机构交易分为决策型交易和隐含交易。决策型交易能够正向预测未来的股票收益和盈余惊喜，而隐含交易则负向预测收益。此外，机构投资者进行决策型交易的倾向以及决策型交易的表现在顶部20%的机构中具有很高的持续性。

通过使用1980至2017年间的季度13F申报数据，研究发现决策型交易在跨机构到股票层面均强烈预测未来的股票收益，顶层分位数的决策型交易股票在接下来的三个月内表现超越底层分位数股票2.59%（年化10.77%）。相比之下，隐含交易负向预测未来股票收益。进一步分析显示，决策型交易对未来盈余惊喜有强预测能力，表明股票基本面的价格发现是机构投资者信息优势的重要来源。

研究还考察了机构投资者信息优势的持续性，发现具有信息优势的机构能够持续利用这一优势。通过分析决策型交易在机构层面的持续性，以及决策型交易的表现在未来几个季度的持续性，结果表明一部分机构投资者能够持续获得信息优势，并专门从事有信息量的交易。

本文的发现不仅揭示了机构投资者在资本市场中的信息角色，还对理解信息如何被纳入股票价格提供了见解。尤其是在机构投资者之间竞争加剧的更近期时段，研究强调了在竞争环境中持续获得信息优势的重要性，为未来关于机构投资者决策型交易的更多研究提供了有价值的洞察。

Alpha Idea:

根据论文的发现和分析方法，可以构造几个量化因子来捕捉机构投资者的信息优势和交易行为对股票价格的影响： 1. 决策交易因子： 描述：这个因子通过计算每个股票在特定时期内所有机构投资者的决策型交易的累积值来衡量。正值表示积极的决策型交易，可能预示着未来股价上涨，而负值则可能预示着未来股价下跌。  计算方法：对于每只股票，将所有机构的决策型交易累加，然后根据其值进行排名或分组。  2. 信息优势持续性因子： 描述：这个因子旨在捕捉那些在决策型交易中表现出持续优势的机构投资者的行为。机构在过去几个季度内表现出强决策型交易能力的股票可能持续表现良好。  计算方法：基于机构过去的决策型交易表现（如过去四个季度的平均决策型交易表现）对股票进行排名或分组。  3. 未来收益预测因子： 描述：考虑到决策型交易对未来盈余惊喜具有预测能力，这个因子基于机构的决策型交易来预测股票的未来盈利能力。  计算方法：利用机构的决策型交易强度和方向来估计每只股票的未来盈利能力，然后根据预测的盈利能力对股票进行排名或分组。

---

### 评论 #129 (作者: BH42089, 时间: 2年前)

Task1:

1. 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Btatus
> Total Unsubmitted Alphas
> 27,326
> Total Active Alphas
> Total Decommissioned Alphas
> Total Alphas
> 27,336


2. 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Status
> Total Unsubmitted Alphas
> 29,151
> Total Active Alphas
> Total Decommissioned Alphas
> Total Alphas
> 29,161
> 7.11
> 幻
> @d)中
> 2024/3/12


3. 
> [!NOTE] [图片 OCR 识别内容]
> In
> 1
> impopt json
> 2
> peS
> S.simulate_and_response (simulation_ls )
> 3
> With open("assignmenti_simulate_results.json"
> "W" )
> 35
> f:
> json . dump(res
> f
> ensure_ascii=False,
> indent=2)
> 24%[
> 484/2000 [21:05<38:12,
> 1.515/i]
  
> [!NOTE] [图片 OCR 识别内容]
> In
> 14
> impopt json
> 2
> pes
> 5.
> simulate_and_response (simulation_ls )
> 3
> With open("assignmentl_simulate_results .json" ,
> IW" )
> 35
> f:
> json . dump(res,
> f,
> ensure_ascii=False ,
> indent=2)1
> 100%
> 2000/2000
> [1:26:40<00:00,
> 2.60s/i]


1. 以前在ACE比赛中搓过一个简单的world quant brain平台SessionManager，所以就在此基础上继续开发和debug了。

代码效率方面，经过我在本地的测试，从提交一个Alpha到可以收到测试结果大概需要15-30s时间。为了提高回测效率，代码中采用了线程池，从而并行测试Alpha，并且任务之间异步，不需要等待一个批次的Alpha测试完成后才测试下一批。为了尽可能提高回测效率，代码中直接将线程数设置为10（brain平台最大同时回测数量）。

为了程序可以长时间运行，用于发送测试数据并获取结果的函数采用重试机制并加入大量异常捕获代码。通过配置logger的handler可以将错误信息和运行情况信息写入log文件。

代码在小批量测试时可以正常运行，但是在连续测试2000个Alpha时，出现了一致没有办法定位和解决的bug。我首先采用” 【Alpha灵感】新闻动量文章启发的反转策略实现”的因子作为模板

通过替换`snt_buzz_ret`，`vhat`，`cap`以及时间窗口长度，构建出了2000个因子表达式。替换值可选参数的筛选方法为：1.`region=’USA’, universe=’TOP3000’, delay=1, search=f”{variable_name}”`，2.相同数据类型(`type=’Matrix’`)，3.因子数量（’alphaCount’）最多的前10个。通过筛选出的三组长度为10的可选字段，以及时间窗口d的可选值为[60, 120]，我们可以通过`itertools.product`构建出2000个不重复的因子。

接下来将因子表达式结合测试参数生成测试数据，并使用前面提到的代码回测
。然而在测试完这一批因子后，平台上显示我只测试了四百多个新因子。最终我发现问题出现在发送的因子表达式与获得的测试结果中的表达式不一样。

以下发送测试数据并获得测试结果的代码片段


> [!NOTE] [图片 OCR 识别内容]
> attempt In
> TOC
> (max_petries):
> 03』13
> try:
> Self,LOggeT.info(t starting tetch tor inde  {index}
> {simulation_data]
> 「eSIDOISI
> 50/55L01
> post(url; Json=simulation_data)
> 几850OISe
> 03158
> status()
> 0315e5
> ST0Re0
> HTTPEFOT
> 1 one
> 0CCURRe0
> simulatlon_progress_url
> TCSIUUISC
> Neate ps
> get( Locatron
> if not simulation_progress_url;
> 「aIse ValueError
> IIssIng SImulatlon progress URL
> Fetch simulation progpess
> NhIlC Tru:
> smulation_progress
> sesslon, get(simulation_progress_url)
> 1f Simulation_progress.headers , get( Retry-After
> Dreak
> sleep(float(simulation_progress
> headers [ Retry After"1]]
> SINULOtIon_progress
> raise_for_status()
> alpha_id
> 5imulation_progres5 , Json()
> get( alpha
> If not alpha_Id
> palse ValueError(Missing alpha I ]
> alpha_FeSpOnS@
> get(t"hTtOS; Llaplsorldquantorglm
> CowlalphasLfalpha_ro]
> alpha_response
> ralse_for_status()
> Self. logger.Info(f Fetch SUCCCSSTUI for Indet {Index}
> return alpha
> 「850005E
> Json(), index
> ercept ExCeption
> 5055100


在经过两天debug仍没有没有修复。我猜测问题可能出现在因子上，于是我随手写了个简单因子模板，采用相同的数据字段生成2000个因子表达式。这批因子的测试正常，可以正常地跑完2000个因子。由于接近ddl，所以就没有为第二批因子精心挑选模板和字段。


> [!NOTE] [图片 OCR 识别内容]
> 485
> 0007.
> Vhatzts_regresslon(VOUUCe
> delay(UTOJ
> ehat-ts_regresslon(retunns
> 4
> ORU
> ehattts_Cank(volune, 5],bueket(rank({2]),pange-0,10.1)
> CISOLULNCLSCOCUJOLN
> O(OLI5)0.2)
> hase_fOFRUUA
> TCNUeCoc
> 1
> {d


Task2：

**我阅读的文章是PV1：**  [Overnight Returns, Daytime Reversals, and Future Stock Returns](/hc/en-us/community/posts/14830168587287-Research-Paper-22-Overnight-Returns-Daytime-Reversals-and-Future-Stock-Returns)

这篇论文研究股票市场中的隔夜回报率日渐回报率反转现象，正向的夜间回报率紧随其后的是负向的日间回报率反转，论文将根据这一现象搭建因子预测股票回报率。当一个月内出现较高频率的正向夜间回报率后紧跟着负向日间回报率反转时，表明投资者之间存在比平时更激烈的对抗，其中夜间交易者可能是噪声交易者，而日间交易者则是套利者。研究结果表明，这种日常对抗的强度预测了跨部分的更高未来回报。论文构建了衡量这种日常对抗强度的因子，并且发现这些因子可以用于预测股票收益。

论文研究的数据集是美股1993/05到2017/12的价格数据和对应公司的财务数据。

论文的日内收益为(open-close)，日间收益为(close-close)收益。通过计算每个月内正向夜间回报后紧接的负向日间回报的频率，可以衡量投资者间日常对抗的强度，进而预测股票的未来回报。

---

### 评论 #130 (作者: SW49904, 时间: 2年前)

**Task 1**

*模拟前*


> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_ecfdbc3be4.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]


*模拟后*

*
> [!NOTE] [图片 OCR 识别内容]
> WORLOOU
> 鬯
> Simulate
> Nphas
> Data
> 恩 Competitions (10]
> Alphas
> Total: 4,248
> bmitted
> Unsubmitted:
> 4,224
> Active:
> tribution
> Decommissioned;
> Alpha Lists
> Fllter
> Select Columns
> Name
> Type
> Status
> Date Created (EST)
> Sharpe
> Returns
> Search
> Select
> Select
> Search
> 28
> 18
> 2.E>|
> aOnYIOUS
> Resular
> UNSUIBUITEU
> 03/11/2024 EDT
> 5.2150
> 5,205.19k
> aOIIMOUS
> REeSUIar
> UNSUBMITTED
> 03/11/2024 EDT
> 0.0555
> -51.47K
> aOIIIOUS
> ReSUIar
> UNSUBMITTED
> 03/11/2024 EDT
> 5035
> 43595k
> aOnYIOUS
> RESUlaT
> UNSUBMITTED
> 03/11/2024 EDT
> -9.3740
> 9,35343k
> aOnYIOUS
> Resular
> UNSUBMITTED
> 03/11/2024 EDT
> .305
> -5,790.38k
> aOIIMOUS
> REeSUIar
> UNSUBMITTED
> 03/11/2024 EDT
> 0.13
> 2.2355
> 22749Tk
> aOIIIOUS
> ReSUIar
> UNSUBMITTED
> 03/11/2024 EDT
> 0.43
> 4.3635
> 435534k
> aOnYIOUS
> RESUlaT
> UNSUBMITTED
> 03/11/2024 EDT
> 55
> -1,543.77
> VLSOOWS
> aOnYIOUS
> ReSUlaT
> UNSUIBUITEU
> 03/11/2024 EDT
> 0.20"设置1.315敫活 WiT307,96K
> aOIIMOUS
> REeSUIar
> UNSUBMITTED
> 03/11/2024 EDT
> 0.30
> 4.1755
> 4151.-1k
> 9:49
> S
>   9》 。 c  英
> MMI
> 2024/3/12
> Pnl
*

具体工作如下：

- Step 1-4，我按照平台提供的API进行了函数封装以便于后续的运行，构造了 *log_in ()，check_alpha (id, s)，get_datafields ()* 这样的函数，为后续simulation做准备。这里我直接用的Equity的例子，因为数据集和字段太多所有没有什么探索思路，希望得到一些启发。此外想问总共有哪些instrument_type，这个如何查看？
- Step 5，这里我的操作比较简单，只是按照type对数据集进行了切分(matrix, vector, group)这三类，后续针对这三种类型选择不同的operators。我这里分别对matrix和vector各跑了前1000个字段数据。
- Step 6-9，首先按照示例我构造了 *simulate_alpha(express,s)* 的函数，这里主要是对simulation模板的优化

*添加一个防止API连接中断的部分->*

```
while True:        simulation_response = s.post('https://api.worldquantbrain.com/simulations', json=simulation_data)        if simulation_response.status_code == 201:            #print("Sucessful")            break        elif simulation_response.status_code == 400:            print('Died')            return None        elif simulation_response.status_code == 401:            s = log_in ()            print("Re-log in")        else:            print(f"Sleeping for 20 seconds due to status code: {simulation_response.status_code}")            sleep(20)
```

*比如登陆超时，从运行记录上看是是这样的->*  
> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_46ef70d492.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]


*添加了一个防止由于计算错误引起模拟中断的熔断代码，大部分是由于数据字段和计算公式不匹配或冲突引起的，一般数据经过分类后出现的比较少，所以我选择对于计算错误的alpha直接跳过->*

```
try:    alpha_id = simulation_progress.json()["alpha"]    return alpha_id,sexcept KeyError as e:    print("Error:", e)    print("Skipping alpha simulation.")    return None,s
```

*从运行记录上看是是这样的->*  
> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_1eea77f678.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]


*最后模拟部分是一个简单的循环->*

```
for alpha in tqdm(vector_alpha_list):  alpha_id,s = simulate_alpha(alpha,s)
```

*从运行记录上看是是这样的->*  
> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_d452e81f02.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]


**额外部分**

我根据checks的信息构造了一个筛选潜力因子的函数，函数首先计算每个检查项的限制差异，并将结果存储在一个新的列中。然后，它计算失败检查的数量。接着，函数检查每个检查项的限制差异是否都小于容忍度因子的限制差异，并在满足条件时将 alpha 的 ID 和失败检查的数量添加到结果 DataFrame 中作为潜力因子。

```
def wether_potential (id, checks_df, CI, potential_df):  checks_df['limit_diff'] = CI * checks_df['limit']  checks_df['diff'] = abs(checks_df['limit'] - checks_df['value'])  num_fail = checks_df[checks_df['result'] == 'FAIL'].shape[0]  if (checks_df['diff'] < checks_df['limit_diff']).all():    print(f"{id} has the potential")    potential_df = potential_df.append({'id': id, 'FALL': num_fail}, ignore_index=True)  return potential_df
```

**反思部分**

我发现我跑的1000次模拟的字段表现都很差，也并没有表现能通过我潜力因子的函数。如果没有一个好的表达式模板，我认为暴力的测试太低效了，希望得到更多的建议，如何有一个好的挖掘因子的思路？此外，我想知道我挖掘潜力因子的思路是否正确，即使我把容错区间调整到CI=0.5，在这次任务的2000次模拟中我也没有筛选出来有潜力的因子。

**Task 2**

我选择的论文： [https://support.worldquantbrain.com/hc/en-us/community/posts/15238244743447-Research-Paper-35-Profitability-R-D-Investments-and-the-Cross-Section-of-Stock-Returns](/hc/en-us/community/posts/15238244743447-Research-Paper-35-Profitability-R-D-Investments-and-the-Cross-Section-of-Stock-Returns)

总结如下：

- 研发强度与股票收益关系探究：使用交叉截面回归分析，研究了研发支出（rd_expense）、毛利率（mdl175_grossprofit）、以及研发与市值比（R&D-to-market value，简称RDM）等因素对随后股票收益的影响。
- 毛利率对预测能力的影响：发现毛利率和研发支出水平（R&D-to-gross profits）会削弱RDM变量的预测能力。当以研发/资产比（R&D-to-assets）作为研发强度的代理时，毛利率仍然主导了研发支出水平的影响。
- 盈利动能的作用：引入盈利动能变量（SUE和CAR3），发现它们会降低研发强度的预测能力，但不影响毛利率的预测能力。盈利动能是未来盈利能力的早期信号，但并非驱动这一结果的因素。
- 市值的影响：报告季度盈利的公司和报告非零研发支出的公司在市值上存在差异，对于报告非零研发支出的大型公司，预测能力下降。
- 统计结果：在控制了R&D-to-assets和R&D-to-gross profits的情况下，大型公司的高毛利率会带来更高的平均收益，而R&D-to-market value变量似乎捕捉到了过去表现较差股票的影响。

---

### 评论 #131 (作者: RW67501, 时间: 2年前)

1. 刚开始simulation数目为559


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 559
> 5hOW
> Out
> U Filter
> Unsubmitted:
> 546
> Active:
> 13
> Select Columns
> atus
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> relect
> e
> eee
> Sele
> 巳.8> 1
> e.8> 1
> e >
> ATOIITIOUS
> ReBUaT
> UNSUBNITTED
> 03/05/2024 EST
> USA
> T0P3000
> 0,12
> 00G
> 0.7795
> anonymous
> Regular
> UNSUBLITTED
> 03/03/2024 EST
> US』
> T0P3000
> 0.85
> 2.5590
> 4.7095
> aonymoUs
> Regular
> UNSUBLITTED
> 03/03/2024 EST
> US4
> TOP3000
> 1.33
> 2.6796
> 2.5295
> 300nyI0U5
> Regular
> UNSUBMIITTED
> 03/03/2024 EST
> U5A
> T0P3000
> -0,04
> 0,149
> 22.439
> anonyIOUs
> Regular
> UNSUBIITTED
> 03/03/2024 CST
> USA
> T0P3000
> -0.68
> -3.939
> 35.1395
> 11:12 AM
> 英 5
> g) 匈
> 3/10/2024


2. 后来的simulation数目为770个

这里有bug未解决，我其实设置的代码里是跑了1290次，最后在网页端统计的Alpha数量只增加了约200个，并且有8个Decommissioned alpha。这种情况我在评论区也看到过别的用户出现过，我怀疑是有的Alpha虽然没有报错，但是这些Alpha丢失了。后续debug我会查看Alpha的具体状态


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Total: 770
> Show
> 10
> 0Ut
> Filter
> Unsubmitted。
> 757
> Active:
> Select Columns
> atus
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Decommissioned:
> Felec
> Search
> Selec
> Selec
> e.g〉1
> e.g〉1
> e.g〉1
> SC
> JTIOTTITIOUS
> UFI
> UNSUBMITTED
> 03/12/2024 EDT
> USA
> TOP3000
> 0.93
> 5.00%
> 21.67%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/12/2024 EDT
> USA
> TOP3000
> 00
> 0090
> 0.00%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/12/2024 EDT
> USA
> TOP3000
> 0.60
> 3.13%
> 13.08%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/12/2024 EDT
> USA
> TOP3000
> 1.23
> 9.03%
> 37.21%
> anonymoUs
> Regular
> UNSUBMITTED
> 03/12/2024 EDT
> USA
> TOP3000
> 1.16
> 7.69%
> 33.19%6
> 1:44 PN
> 中 5
> 谷 4)) 匈
> 3/12/2024
> ReB


3. 每个线程10次simulation，连续跑完129个线程


> [!NOTE] [图片 OCR 识别内容]
> simulation_pIOgIeSs
> 5.
> get(simulation_progress_UIl )
> if simulation_pIogress .headers . get( "RetIy-After "
> 0)
> 
> break
> print("Sleeping for
> +simulation_progress .headers [ "RetIy-After" ]
> Seconds"
> sleep(float(simulation_progress .headers[ "RetIy-After" ] ) )
> tIy
> child_alpha
> simulation_progress.json( ) ["children
> alpha_idList.append(child_alpha )
> print('The number of
> simulated Alphas:
> str(len(sum(alpha_idList , [])) ) )
> eXCept
> KeyEIIOI :
> S=sign_in()
> While True:
> simulation_pIogIess
> 5.
> Set(simulation_progress_uIl )
> if simulation_pIogress .headers . get( "RetIy-After"
> 0 )
> 
> 0:
> break
> ("Sleeping
> for
> +simulation_progress .headers [ "RetIy-After" ]
> Seconds"
> sleep(float(simulation_progress .headers [ "RetIy-After" ]) )
> child_alpha
> simulation_progress.json( ) ["children
> alpha_idlist.append(child_alpha )
> print( 'The number
> 0f
> simulated
> Alphas:
> str(len(sum(alpha_idlist ,[]))) )
> Sleeping for 2.5 seconds
> Sleeping for 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for
> 2.5 seconds
> Sleeping for 2.5 seconds
> The number of simulated Alphas:
> 1290
> CPU times:
> total: 906
> m5
> Wall time:
> 2h Smin 335
> print


4. 反思

本周我参考的模板来自  [[L2] 【Alpha灵感】新闻动量文章启发的反转策略实现_19353819839639.md]([L2] 【Alpha灵感】新闻动量文章启发的反转策略实现_19353819839639.md)  “【Alpha灵感】新闻动量文章启发的反转策略实现”，表达式为：

```
ehat=ts_regression(returns,ts_delay(snt_buzz_ret,1),120);alpha=group_neutralize(-ehat,bucket(rank(cap),range='0,1,0.1'));alpha
```

因此我选用的category为News data，根据Brain论坛上提供的代码模板，我先拿到New data下所有的dataset对应的id，然后通过id拿到所有datafield的数据。这样操作会得到一些完全重复的data id，通过去重复后共有1299个不同的data id，之后即可代入模板中替换snt_buzz_ret重复simulation。

开始没有对vector数据做操作，直接代入模板中报错。后来对数据类型为vector的数据先进行vec_avg()操作，就可以解决刚刚的bug。

另外运行中有时候存在账户登出的问题，需要try-except防止登出造成运行中断，实测1290次simulation的时候还没有登出。

使用multi-simulation的方法可以大大提高代码运行效率，可以同时跑10个simulation，大概跑完10个simulation需要50s，最终跑完1290个用了2个小时。

最终获得Alphalist，为multi-simulation中children的结果即为单个Alpha的Location。后续可以通过该list获取每个Alpha的id。


> [!NOTE] [图片 OCR 识别内容]
> In [305]
> sum(alpha_idlist , [] )
> [ '3nEs48gU64WRbqIWMvduvJi
> Zn3APIIaO4sOgCVJKBYAbDL
> 2U3mskeh34BtgsUGaUflooD
> Iykgl020r552aljLjnQ5BMh
> 'WpwDPfjD5znc2YXHOfZNHC
> ZKWBktgAU4pIbOQ4DlIqPAj
> 22SYFn7D44EPSNalOZVMTpPH
> 3s5V2fgFq4DsgcF85ZF1872
> 30Y50]35V4yqb8tisjDtaBj
> 'WUYJY3Hs4Ihc8St4VEIYqO
> lyxGjvhz4m4ajnjlCbgBlg
> 2IIPkS4PVSO3CWCgFYj2VDC
> 3bZPhtgZOSeXSRPI2pzdh7j1
> IOJMNIfmU4zbc5OI4AXpOSPM
> 15BXm41
> ii5hBcoylbqdzigim
> 3BYhNTGUgShRaDhlg4IOTIHk
> IAjiEYagQ4NXCy317gyOLOme
> 22XDqN8S4S9HCnxOCCWOIWk
> 3Ek3Tb7KY4KmaIu3OnbOIVl
> IkOZk77VZ4p28WqSMJePHDm
> bOnRISEs4Hwan4llYACQOVC
> 42c8b480641Da0606VEXIeR
> 4egn66dZJ4CVakalho04a]y7
> 43OTpnbGUSbRS8M7GkXhOYH '
> 49F3356u54yQ8QpCWa7yaH8
> 434jJa4Z4FagehldcqpBQlb


5. 改进

首先要解决消失的Alpha的问题，然后对于Alpha的后处理，performance比较进一步完善相关代码，增加代码可读性和运行速度。

6. 文献阅读

我阅读的因子日历中一个因子的索引研报，“高子剑，2020，高频价量相关性，意想不到的选股因子，东吴证券”。这里虽然是高频因子，但是我觉得在日频数据中应该也有效。

表达式为

```
pv_corr=corr(close,volume);alpha=std(pv_corr)
```

该因子考虑价量相关性波动性因子，从价格和成交量的相关性角度来提取有用的信号，而不是只考虑单一的价格和成交量。该因子也可以加入时序信息做平均和对市值做中性化处理。

---

### 评论 #132 (作者: WL13229, 时间: 2年前)

[RW67501](/hc/en-us/profiles/13836987458967-RW67501)

"我其实设置的代码里是跑了1290次，最后在网页端统计的Alpha数量只增加了约200个"

关于所谓"Alpha丢失了“的猜测是不准确的，您需要检查您Alpha的排队逻辑。如果有多个Alpha同时在跑，您需要等其他的跑完再提交。

---

### 评论 #133 (作者: MJ31525, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Show
> OUt Of 1,169
> Date Created (ESTJ; 03/11/2022-0311。
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
> Searcn
> See
> See
> See
> 03/11/2024
> 03112/1
> See
> See
> E.吕 >1
> e.g> 1
> e.g> 1
> See
> aTORIMOUs
> Resular
> UISUBMITTED
> 03/12/2024EDT
> USA
> TOPSOD
> 1.15
> 37.023
> 103.3395
> anOnyMOUS
> Resular
> UNSUBMITTED
> 03/11/2024EDT
> USA
> T0P30O0
> 0.95
> 28.5945
> 0.814
> aCE_taE
> aTORIMOUs
> Resular
> UISUBMITTED
> 03/11/2024EDT
> USA
> T0P30O0
> 0.95
> 28.5535
> 0.314
> aCS_taE
> anOnyMOUS
> Regular
> UNSUBMITTED
> 03/11/2024EDT
> USA
> T0P30O0
> 0.95
> 28.534
> 0.8235
> aCE_taE
> aTORIMOUs
> Resular
> UISUBMITTED
> 03/11/2024EDT
> USA
> T0P30O0
> 0.94
> 28.513
> 0.783
> tag
> ShOW
> Out Of 1,169
> [O
> 234
> Next
> Tag
  
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> See all
> Achievements
> View Achievements
> Status
> 20
> 旧0
> [
> GOOD
> Total Unsubmitted Alphas
> 54,104
> Total Actie Alphas
> 147
> BrzLLUII
> Total Decommissioned Alphas
> 28
> Total Alphas
> 54,279
> 17:05
> 搜索
> 3
> 中  拼  谷 d)
> 2024/3/12


python simulation流程：1、获取所有的data，以data减去data行业均值为模板后取行业中性，构造alpha快速表达式；2、提交simulation后，根据返回结果，筛选具有潜力的alpha；3、调整alpha表达式根据市值，成交量等调整输出最优alpha。缺点是：只有最后大批量输出使用并行sim，效率较低；模板适应性一般，挖掘效率低；最优结果的筛选机制还不成熟。

我阅读的文章是option4：Research Paper 26: Bid and Ask Prices of Index Put Options: Which Predicts the Underlying Stock Returns?

文章以标普500虚值认沽期权为样本，发现ask价格波动率和股票未来回报的相关性比bid更强，且资产下行风险加剧时更加显著，理解的是市场下行风险增加时，做市商会卖出downside侧认沽期权后，需要卖出股票来对冲，在快速下跌的过程中，做市商卖出股票的冲击成本更高，因此需要以更高的溢价来定价downside的虚值合约。因此ask的定价一定程度反应做市商对未来的预期，使用线性模型预测后根据预测值构建alpha。

---

### 评论 #134 (作者: WL13229, 时间: 2年前)

帮 [ZL70229](/hc/en-us/profiles/17108134190999-ZL70229) 发布作业

**必做（一）**

**
> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_6406d37a1b.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]
**

**
> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_28b44735aa.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]
**

**
> [!NOTE] [图片 OCR 识别内容]
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_177b21b0df.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]
**

**一、代码效率**

**（一）操作的优化**

**命令发送时间：比起单纯手工操作，命令的发送快了n倍，且此套模板可以复用。**

**调参速度：一键修改n次模拟的参数。**

**（二）理论层面的优化**

**因子挖掘指导：可短时间根据因子在不同数据或参数下的大样本结果比较，迭代指导性更强。**

- **模拟结果**

**受限于网站的服务器访问频次，依然需要等待一段时间才能看到模拟结果。但模拟只是中途停歇，并没有中途停止，所以访问频次的限制只是增加了模拟的时长，并没有提高操作的复杂度。**

- **debug经历**

**仅出现中途输错参数及账号密码没有加引号时出现了异常。但不知道是何原因，在进行了第一次的不间断模拟后，后续每次不间断模拟在WQ brain平台只能看到一个alpha记录。**

- **模板适合的类型**

**模板提高的事输入效率，更适用于包含更多datafield的dataset的模型以及表达式更简洁的策略。**

**四、模板改进的方向**

**可以优化代码，对每个参数的进行for循环进一步增加模拟次数。**

**必做（二）**

**我阅读的文章是**  [Research Paper 04: Strategic Rebalancing](/hc/en-us/community/posts/13304175062807-Research-Paper-04-Strategic-Rebalancing)

该文章通过对60-40（股票债券投资比）资产配置方法的“买入并持有”策略与“机械再平衡”策略进行对比，认为“机械再平衡”策略相较于买入存在负凸性，相当于卖出了straddle期权组合。卖出straddle会在资产存在较大上升或下降时遭受亏损，会在资产价格仅在微小区间内变动时由于收到对手方的期权费而盈利。并进一步比较“趋势再平衡”策略，认为该策略与“机械再平衡”相反，相对于“买入并持有”策略具有正的凸性。

该论文通过两阶段的资产配置模型与实证数据分析，得到了以上结论。该论文同样指出应当注意对“买入并持有”策略在市场价格存在持续性动量时会导致风险过度集中，以及简要说明了其他几个模型。

Alpha Idea：“趋势再平衡”策略可以达到做动量策略的效果，“机械再平衡”可以达到做反转策略的效果。

---

### 评论 #135 (作者: HY95587, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> platform worldquantbrain.com/alphas/unsubmitted
> Gu
> C @
> 8
> 0
> WORLDQUANT
> BRAN
> Simulate
> Alphas
> Learn
> Data
> 召 Competitions (4)
> 88 Team
> Community
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page size
> 10
> Out Of 1,768
> Filter 
> Select Columns
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
> Selec
> Selec
> SearCh
> Selec
> Selec
> e821
> e821
> 2.6
> Se
> anonymOUs
> Regular
> UNSUBMITTED
> 04/23/2024 EDT
> CHN
> TOP3000
> 3.44
> 14.89%
> 7.9696
> anonymoUs
> Regular
> UNSUBMITTED
> 04/20/2024 EDT
> CHN
> TOP3000
> 3.43
> 27.99%6
> 21.00%
> anonymOUs
> Regular
> UNSUBMITTED
> 04/20/2024 EDT
> CHN
> TOP3000
> 3.43
> 28.65%
> 20.73%
> anonymous
> Regular
> UNSUBMITTED
> 04/20/2024 EDT
> CHN
> TOP3000
> 3.42
> 28.33%
> 21.089
> anonymous
> Regular
> UNSUBMITTED
> 04/17/2024 EDT
> USA
> TOP3000
> 3.42
> 28.79%
> 70.50%
> anonymoUs
> Regular
> UNSUBMITTED
> 04/20/2024 EDT
> CHN
> TOP3000
> 3.41
> 28.85%
> 20.629
> anonymOUs
> Regular
> UNSUBMITTED
> 04/20/2024 EDT
> CHN
> TOP3000
> 3.41
> 46.58%
> 21.45%
> anonymoUs
> Regular
> UNSUBMITTED
> 04/17/2024 EDT
> USA
> TOP3000
> 3.41
> 29.90%
> 70.70%
> anonymOUs
> Regular
> UNSUBMITTED
> 04/20/2024 EDT
> CHN
> TOP3000
> 3.37
> 24.8796
> 14.87%
> anonymoUs
> Regular
> UNSUBMITTED
> 04/24/2024 EDT
> CHN
> TOP3000
> 3.36
> 21.3496
> 14.99%
> Page size
> 10
> Out Of 1,768
> Prev
> 177
> Next
> 15.06
> 2024/7/15
> Name
> Tag
 从代码效率来看，应该还可以，一小时能模拟完成。但是由于运行开始时间较晚，可能无法在 9 点之前完成模拟。先上传过程中的图片。 
> [!NOTE] [图片 OCR 识别内容]
> 〉 X
> https:/ /platform worldquantbrain.com/alphas/unsubmitted
> 8
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> 召 Competitions (4)
> 88 Team
> Community
> Consultant program
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page size
> 10
> Out Of 2,189
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
> Selec
> Selec
> Selec
> SearCh
> Selec
> Selec
> e821
> e821
> e821
> Selec
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 0.70
> -6.67%6
> 24.6496
> anonymoUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> -1.19
> 10.91%
> 50.87%
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 0.57
> 5.9796
> 25.139
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 0.57
> -5.29%
> 25.31%
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 1.21
> 12.2490
> 53.27%
> anonymoUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 0.94
> 8.43%
> 53.23%
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 0.78
> -7.43%
> 27.649
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 0.79
> -7.61%
> 25.249
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> 1.29
> -11.70%
> 56.39%
> anonymoUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOP3000
> -1.28
> -11.86%
> 52.88%
> Page size
> 10
> out Of 2,189
> Prev
> 219
> Next
> 正在等待 platform worldquantbrain.c...
> 〉》>
> quit()
> executable to run the lanquage serer?
> 20:44
> 2024/7/15
> Tag



> [!NOTE] [图片 OCR 识别内容]
> [55]
> 02
> 2gm 18.5s
> Python
> Multisimulation
> request
> sent successfully
> Already
> submitted
> 488
> alphas
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation request
> And retry
> after
> IOs
> Multisimulation
> request sent successfully
> Already
> submitted
> 410 alphas
> Multisimulation
> request sent successfully
> Already
> submitted
> 420 alphas
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation request。
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Multisimulation
> request sent successfully
> Already submitted
> 430 alphas
> Error
> in
> sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Multisimulation
> request
> sent successfully
> Already
> submitted
> 448
> alphas
> Multisimulation
> request
> sent successfully.
> Already
> submitted
> 458
> alphas
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in
> sending multisimulation request。
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in
> sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sendine multisimulation
> request .
> And
> retrv
> after
> 105


代码效率、debug经历、模板适合的数据类型、模板的改进方向：

代码效率大概 950 alphas/h。感觉不是很理想，因为按理来说可以 10 线程 * 10 multi-sim。

debug 发现 multi-sim 不允许传刚好一个 alpha 的模拟。以及一开始拼写错误中性化项目的单词，导致整个程序卡死。之后对 400 error 的报错报文，都进行了处理和输出，从而及时找到错误。

目前使用的是 ts_rank(rank(x), t) 的模板。我枚举了中性化、delay、decay、USA TOP ??? 这几种设置，x 目前使用了 close, open, vwap；此外调整了时间 t，以及 ts_rank 可能调整为 ts_zscore。

之前在 alpha example 见过类似的因子？好像是比较适合量价数据类型。ts_rank 对时间变化很敏感，不适合基本面的一些变化很慢的数据，以及新闻之类大部分时候为 0 但少部分时候很多的数据。

模版可以考虑稍微复杂一点。现在的模版只能用单一的数据集，可以考虑多个数据集的 ts_regression 或者投影之类的，这样可以删除掉数据的一些 beta 成分，生成更有效的 alpha。

**我阅读的是 option62: Testing for Asset Price Bubbles using Options Data"**

这篇文章提出了一种使用期权数据来评估资产价格泡沫的方法：

文章的目标是利用期权的前瞻性质来探测资产价格泡沫。通过分析看涨期权和看跌期权之间的价格差异，来作为是否存在资产价格泡沫的指标。

- **基本思路** ：期权作为一种衍生金融工具，其价格反映了市场对于未来资产价格走势的预期。理论上，如果资产存在价格泡沫，那么这种预期会在期权定价中表现出来，尤其是看涨期权和看跌期权价格的差异。
- **具体方法** ：
  1. **模型选择** ：选择一个灵活的参数模型（例如G-SVJD模型）来模拟资产价格的演变。
  2. **数据输入** ：使用看跌期权的数据来评估资产的基本价值。文章认为看跌期权的定价较为接近资产的真实基本价值，因为它们通常包含较少的投机性预期。
  3. **泡沫估计** ：将看涨期权的市场价格与从看跌期权得出的基本价值进行比较。价格差异较大时，可能表明存在资产价格泡沫。

- **Alpha Idea** ：根据文章提出的模型和方法，可以设计投资策略来应对资产价格泡沫。在泡沫初期，可以采取跟随市场动量的策略进行投资；当预测到泡沫即将破裂时，转而采取反向策略，以期获得收益。

---

### 评论 #136 (作者: HY95587, 时间: 2年前)


> [!NOTE] [图片 OCR 识别内容]
> [55]
> SGm 25.Os
> Error
> in sending
> multisimulation request。
> And retry
> after
> IOs
> Multisimulation request
> Sent
> successfully:
> Already submitted
> 940 alphas
> Error
> in
> sending
> multisimulation request.
> And retry
> after
> IOs
> Error
> in
> sending
> multisimulation request.
> And retry
> after
> IOs
> Error
> in
> sending
> multisimulation request.
> And retry
> after
> IOs
> Multisimulation request
> sent successfully
> Already
> submitted
> 950 alphas
> Error
> in sending
> multisimulation request
> And retry
> after
> IOs
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending multisimulation request。
> And retry
> after
> IOs
> Multisimulation request
> Sent
> successfully:
> Already submitted
> 960 alphas
> Error
> in sending
> multisimulation request.
> And retry
> after
> IOs
> Error
> in
> sending
> multisimulation
> request.
> And retry
> after
> IOs
> Multisimulation request
> Sent
> successfully:
> Already
> submitted
> 970 alphas
> Error
> in sending multisimulation request。
> And retry
> after
> IOs
> Error
> in sending multisimulation request。
> And retry
> after
> IOs
> Multisimulation request
> sent
> SUCCessfully
> Already
> submitted
> 980 alphas
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Error
> in sending
> multisimulation
> request。
> And retry
> after
> IOs
> Error
> in
> sending
> multisimulation request.
> And retry
> after
> IOs
> Error
> in sending
> multisimulation request.
> And retry
> after
> IOs
> Multisimulation request
> Sent
> successfully:
> Already
> submitted
> 990 alphas
> Error
> in sending multisimulation
> request.
> And retry
> after
> IOs
> Multisimulation request
> sent successfully
> Already
> submitted
> 1og8 alphas
  
> [!NOTE] [图片 OCR 识别内容]
> 〉
> X
> platform.worldquantbrain.com/alphas /unsubmitted
> @
> 8  ^凶
> WORLDQUANT
> BRANI
> Simulate
> Alphas
> Learn
> Data
> Competitions (4)
> Team
> Community
> 0
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page size
> 10
> Out Of 2,769
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
> Turnov
> Search
> Selec
> Selec
> Selec
> SearCh
> Selec
> Selec
> e821
> e.吕>1
> e.吕
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSO0
> 0.47
> 3.73%
> 34
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSOO
> 0.96
> -7.08%
> 55
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSO0
> 0.57
> -4.69%
> 34
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSOO
> -1.16
> -8.65%
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSO0
> 0.63
> -5.13%
> 36
> anonymous
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSOO
> 1.10
> 8.40%
> 70
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSO0
> 0.60
> 4.73%
> 37
> anonymoUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSOO
> 1.03
> -7.59%
> 73
> anonymOUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSO0
> 0.68
> -5.629
> 37
> anonymoUs
> Regular
> UNSUBMITTED
> 07/15/2024 EDT
> USA
> TOPSO0
> 1.17
> -8.93%
> 73
> Page size
> 10
> Out Of 2,769
> Prev
> 277
> Next
> 正在等待 platform.worldquantbrain.com 的响应
> 早盘开始.
> 由于今天会议开幕。郭嘉
> executable to run the lanquage serer?
> 21.15
> 2024/7/15


---

### 评论 #137 (作者: JC15033, 时间: 2年前)

您好，这段代码的报错一直是如下：

```
Failed to submit alpha: 405 Client Error: Method Not Allowed for url: https://api.worldquantbrain.com/alphas
```

请问要怎么修复？

import requests
import pandas as pd
import json
import time

username = "XXX"
password = "XXX“

# Function to handle authentication and maintain session
def sign_in():
    s = requests.Session()
    s.auth = (username, password)

while True:
        try:
            response = s.post(' [https://api.worldquantbrain.com/authentication](https://api.worldquantbrain.com/authentication) ')
            response.raise_for_status()
            print("Successfully signed in")
            break
        except requests.exceptions.RequestException as e:
            print(f"Failed to sign in: {e}")
            print("Retrying in 10 seconds...")
            time.sleep(10)

return s

# Function to generate an alpha
def generate_alpha(expression: str, universe: str = 'TOP3000', region: str = 'USA'):
    return {
        'expression': expression,
        'settings': {
            'universe': universe,
            'region': region
        }
    }

# Function to submit an alpha
def submit_alpha(session, alpha_data):
    url = ' [https://api.worldquantbrain.com/alphas](https://api.worldquantbrain.com/alphas) '
    try:
        response = session.post(url, json=alpha_data)
        response.raise_for_status()
        alpha_id = response.json()['id']
        print(f"Alpha submitted successfully. Alpha ID: {alpha_id}")
        return alpha_id
    except requests.exceptions.RequestException as e:
        print(f"Failed to submit alpha: {e}")
        return None

# Example alpha expression
alpha_expression = "1-rank(high/low)"

# Example usage:
session = sign_in()
if session:
    alpha_data = generate_alpha(alpha_expression)
    alpha_id = submit_alpha(session, alpha_data)
    if alpha_id:
        # Simulate alpha
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
        simulation_response = session.post(' [https://api.worldquantbrain.com/simulations](https://api.worldquantbrain.com/simulations) ', json=simulation_data)

if simulation_response.status_code == 202:
            simulation_progress_url = simulation_response.headers['Location']
            print("Simulation in progress...")
            while True:
                simulation_progress = session.get(simulation_progress_url)
                if simulation_progress.status_code == 200:
                    simulation_status = simulation_progress.json().get('status')
                    if simulation_status == 'SUCCESS':
                        print("Alpha simulation successful")
                        break
                    elif simulation_status == 'FAILED':
                        print("Alpha simulation failed")
                        break
                    else:
                        print(f"Simulation status: {simulation_status}")
                        retry_after = simulation_progress.headers.get("Retry-After")
                        if retry_after:
                            print(f"Sleeping for {retry_after} seconds...")
                            time.sleep(float(retry_after))
                        else:
                            print("Waiting for simulation to complete...")
                            time.sleep(10)
                else:
                    print(f"Error fetching simulation status: {simulation_progress.status_code}")
                    break
        else:
            print(f"Failed to start simulation: {simulation_response.status_code}")

---

### 评论 #138 (作者: WL13229, 时间: 2年前)

[JC15033](/hc/en-us/profiles/18243328791959-JC15033)

这个alpha还没有到submit的阶段所以使用

```
https://api.worldquantbrain.com/alphas
```

不正确。我有个建议是使用大语言模型帮助功能实现+参考ACE代码框架👉

1. ACE： [Alpha Creation Engine](/hc/en-us/articles/20786107171351-Alpha-Creation-Engine)

---

