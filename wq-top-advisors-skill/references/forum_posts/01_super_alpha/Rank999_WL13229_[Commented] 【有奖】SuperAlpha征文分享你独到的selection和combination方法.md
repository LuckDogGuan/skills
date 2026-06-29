# 【有奖】SuperAlpha征文：分享你独到的selection和combination方法！

- **链接**: [Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法.md
- **作者**: WL13229
- **发布时间/热度**: 1 year ago, 得票: 67

## 帖子正文

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

## 讨论与评论 (49)

### 评论 #1 (作者: WL13229, 时间: 1 year ago)

**获得纪念品的名单： [LA79055](/hc/en-us/profiles/28845324426135-LA79055) ， [JB71859](/hc/en-us/profiles/26720563911063-JB71859) ， [PW58059](/hc/en-us/profiles/25878520088087-PW58059) ， [PZ64174](/hc/en-us/profiles/28846373031959-PZ64174) ， [WP88606](/hc/en-us/profiles/27032592505751-WP88606) ， [MY27687](/hc/en-us/profiles/28843046087063-MY27687) ， [ZL35633](/hc/en-us/profiles/28828582941975-ZL35633) ， [WH24469](/hc/en-us/profiles/13991511763607-WH24469) ， [JL40454](/hc/en-us/profiles/28831795834263-JL40454) ， [LW49759](/hc/en-us/profiles/26717472313751-LW49759) ， [CH62432](/hc/en-us/profiles/28879407938455-CH62432) ，LZ14530， [LX31898](/hc/en-us/profiles/30215090251159-LX31898) ，KL64183， [顾问 YX23928 (Rank 8)](/hc/en-us/profiles/27479819504663-顾问 YX23928 (Rank 8)) ， [顾问 KZ79256 (Rank 21)](/hc/en-us/profiles/13609593802263-顾问 KZ79256 (Rank 21)) ， [LH44620](/hc/en-us/profiles/26717918976919-LH44620) ，MZ54236， [顾问 JR23144 (贺六浑) (Rank 6)](/hc/en-us/profiles/28844048981143-顾问 JR23144 (贺六浑) (Rank 6)) ， [HW93328](/hc/en-us/profiles/28771941793815-HW93328) ，XY91783， [XC66172](/hc/en-us/profiles/28880767093655-XC66172) ， [CL88457](/hc/en-us/profiles/25846674784919-CL88457)**

**获得优胜奖名单： [ZL29184](/hc/en-us/profiles/22955594228503-ZL29184) ， [worldquant brain赛博游戏王，](/hc/en-us/profiles/26858512793111-worldquant brain赛博游戏王)  [YB49779，](/hc/en-us/profiles/26716038151319-YB49779)  [KD86036，](/hc/en-us/profiles/27031622119831-KD86036)  [AK76468](/hc/en-us/profiles/28846915371031-AK76468) ， [YW93864](/hc/en-us/profiles/14096946892439-YW93864)**

**相关链接地址将发送至您邮箱。**

**SuperAlpha是一个很好地弥补自身组合缺点的方式，请一定要识别本身组合需提升的方面。**

**示例Idea:将自己高流动性的Alpha与池中进行组合**

**类别：selection**


> [!NOTE] [图片 OCR 识别内容]
> Super Simulation
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> USA
> Positive


> 注意：selection数量为30仅为展示，不建议将该数量设置过低。

```
# 选择一部分自己池中流动性较好的,并给较大权重，保证自己的都先被选上self_set = (own&&universe_size(universe)<=1000)*2; # 选择池中低换手,高流动性股票池的新顾问的Alpha,他们可能会带入一些新想法# 且如果该Alpha的作者相关性越低，就越容易选到这个alphapool_set = (!own && author_turnover<0.1 && author_tenure <100 && universe_size(universe)<=500) *author_self_correlation ; # 将两个分数相加，请注意，我们使得只要满足self_set的Alpha一定可以获得高分，保证了自己的都先被选上self_set+pool_set
```

---

### 评论 #2 (作者: ZL29184, 时间: 1 year ago)

**Idea:选取一个较大集合中不相交的子集**

**类别：selection**

**
> [!NOTE] [图片 OCR 识别内容]
> Super Simulation 1
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> USA
> Positive
> 100
**

我个人倾向选取40个以上的。

```
not(own) && #选择别人的alpha保证有足够的alpha(universe =='TOP3000')&& #选择同一个universe的，这个可以后续调整(neutralization =='SECTOR')&&#选择同一个neutralization的，这个可以后续调整(dataset_count ==1 )&&#选择dataset_count ==1的，也就是atom alpha，1这个参数可以后续调整in(datasets, "fundamental6")#选择某一个数据集的alpha，可以选单个，也可以选多个数据集
```

本质上是做出可以组合的拼图，选出一些互相不相交的alpha集合，并且保证它们有相对一致的特征。关于这个不相交，你可以设置不同的参数阈值，使得在固定的维度，你的alpha集合被分为若干个不相交的子集。上面只是一个例子，最后在USA TOP3000选出来了6个alpha，你也可以适当放宽条件以选取更多。

你也可以自由删减这些特征，也可以把若干个加起来。
根据我的实践，这个selection思想足够帮你做出很多相关性很低，能提高组合表现的sa。

祝各位在sa的比赛中有好成绩！

2025/05/30

于广州

---

### 评论 #3 (作者: worldquant brain赛博游戏王, 时间: 1 year ago)

类别：SELECTIONN

表达式：

(

not(own)&&

#选择不是自己的因子

((turnover<0.07&&turnover>0.05)||

(turnover<0.15&&turnover>0.13)||

(turnover<0.12&&turnover>0.09))

#按照turnover进行分层，每次选取不同的范围以保证每次选到的因子不同，提升多样性

&&(operator_count<8)  &&(dataset_count<=2)

#限制op和pyramid个数，降低过拟合的概率

&&(prod_correlation<0.5&&prod_correlation>0.1)

#按照prodcor筛选，0.5可以保证充分的分散化，0.1则是保证不选到奇奇怪怪的东西（一些厂或者极端的pnl）

#以上为组合部分，以下为权重分配

)

/(turnover*s_log_1p(turnover)

#按照turnover进行加权

*sigmoid(self_correlation)

*sigmoid(prod_correlation)

#按照prodcor进行加权，为了防止权重变化过大，比如0.5和0.1权重差五倍，容易集中到一个因子上去

*abs(long_count-short_count))

#按照多空进行加权，对于多空平衡的因子赋予更高权重，可以避免选到偏多或者偏空因子

其他参数： 
> [!NOTE] [图片 OCR 识别内容]
> Combo Expression
> Simulation Settings
> Instrument Type:
> Equity
> Decay:
> Pasteurization:
> 0n
> Reglon:
> A51
> Delajl:
> NaN
> Handling:
> 0n
> Universe:
> MINVOLIM
> Truncation:
> 0.08
> Unit Handling:
> Verify
> Language:
> Fast Expression
> Neutralization:
> Sector
> Max Trade:
> Off


最终结果：


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> TurnoVer
> Fithess
> Returns
> Drawgown
> Margin
> 7.66
> 13.049
> 9.20
> 18.839
> 1.539
> 28.899600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 8.04
> 13.7695
> 10.34
> 22.759
> 0.76%
> 33.07330
> 1385
> 1331
> 2014
> 6,63
> 13.299
> 14.799
> 829
> 22.26930
> 1598
> 1547
> 2015
> 8,64
> 12.8995
> 11.54
> 23.4196
> 0.519
> 36.33950
> 659
> 538
> 2016
> 4.65
> 12.6995
> 4.56
> 12.739
> 1.5796
> 20.059630
> 590
> 1577
> 2017
> 8.92
> 12.9995
> 10.93
> 19.52%
> 88%
> 30.0530
> 605
> 1638
> 2018
> 8.89
> 13.4095
> 10.75
> 19.589
> .68%
> 29.21930
> 883
> 1851
> 2019
> 6,08
> 13.3796
> 6.14
> 13.649
> 1.139
> 20.41930
> 1675
> 2020
> 8,05
> 12.959
> 10.15
> 20.6096
> 0.939
> 31.80750
> 1811
> 1736
> 2021
> 9.21
> 12.629
> 11.83
> 20.8196
> 0.529
> 33.00750
> 2243
> 2250
> 2022
> 8.60
> 12.5595
> 10.91
> 20.18%
> 639
> 630
> 2104
> 2072
> 2023
> 5.90
> 9.8195
> 8.18
> 24.029
> 0.7196
> 28.3530
> 1760
> 1872
> Risk neutralized
> Aggregate Data
> Sharpe
> TurnoVer
> Fithess
> Returns
> Drawcown
> MarEin
> 7.55
> 13.049
> 7.87
> 14.18%
> 0.7796
> 21.759600
> VYear


---

### 评论 #4 (作者: LA79055, 时间: 1 year ago)

分段条件判断和乘法组合

默认设置：


> [!NOTE] [图片 OCR 识别内容]
> Super Simulation 1
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION UIMIT
> USA
> Positive
> 30


类别1：Selection

```
"multiplier = if_else(category == 'FUNDAMENTAL', 1.3, 1.1);\n""adjustment = if_else(decay < 2.0, 1.5, 1);\n""base = sqrt(universe_size(universe));\n""score = multiplier * adjustment * base;\n""if_else(turnover > 0.33, nan, score)",
```

- **类别权重（multiplier）**  – 使用  `if_else`  检查  `category`  是否为  `"FUNDAMENTAL"` 。如果是，则赋值 1.3，否则为 1.1。这说明在该策略体系中，与基本面（FUNDAMENTAL）相关的 α 被认为更有价值，所以获得更高的加权因子。
- **衰减调整（adjustment）**  – 根据  `decay` （衰减）参数是否小于 2.0，赋予 1.5 或 1。通常，较低的衰减可能表明信号稳定性更高，从而给予一个额外加成。
- **基础规模（base）**  – 计算  `universe_size(universe)`  的平方根。这里的 universe_size 可能返回样本（比如股票池）的大小，取平方根起到平滑放大规模效应的作用，使得评分不会随着股票数目线性放大，而是适度调整。
- **综合得分（score）**  – 将上面三个因子相乘，以获得一个初步评分。
- **换手率过滤**  – 最后利用  `if_else(turnover > 0.33, nan, score)`  筛选：如果换手率超过 33%（可能代表交易过于频繁或信号风险较大），则不返回评分，而是返回 NaN，将该 α 排除在候选外。

类别2：Selection

```
"vol_factor = 1 / (abs(prod_correlation) + 0.001);\n""activity_bonus = if_else(author_activity >= 0.85, 1.3, 1);\n""score = vol_factor * activity_bonus * operator_count;\n""if_else(turnover >= 0.34, nan, score)",
```

- **波动性因子（vol_factor）**  – 这里利用反比关系：1 除以（绝对值的  `prod_correlation`  加上一个小常数 0.001）。当 α 与其他信号的相关性较低（绝对值较小）时，vol_factor 较大。这种设计鼓励低相关性、分散化的策略，同时加上一个极小的偏移值避免除零错误。
- **活跃度奖励（activity_bonus）**  – 根据作者的活跃度  `author_activity`  是否达到或超过 0.85，加一个 1.3 的系数，否则为 1。较高的提交频率或活跃度可能被视为对策略构造的持续优化与稳定性保证，因此给予额外奖励。
- **评分计算**  – 得分等于上述两个因子乘以  `operator_count` 。这里的  `operator_count`  反映了策略表达式中操作符的数量，通常用来衡量方法“复杂度”或包含的经济逻辑的丰富性。
- **换手率约束**  – 如果换手率大于或等于 34%，则返回 NaN，排除高换手率的策略，以控制交易成本和策略不稳定风险。

类别3：Selection

```
"bonus = if_else(author_sharpe >= 2.5 && author_sharpe <= 3.5, 1.2, 1);\n""score = operator_count * bonus;\n""if_else(turnover >= 0.35, nan, score)",
```

- **夏普比率奖励（bonus）**  – 利用  `if_else`  判断作者的夏普比率  `author_sharpe`  是否处于 2.5 到 3.5 的理想区间。如果在这个区间，则奖励系数为 1.2，否则系数为 1。通过这样的设计，平台鼓励构造在风险调整后收益表现最佳的策略。
- **评分计算**  – 得分直接是  `operator_count`  与 bonus 的乘积。这意味着策略在符合理想风险收益范围时，其复杂度（操作符数量）得以提升，从而在筛选时可能更受青睐。
- **换手率过滤**  – 设置换手率门槛 35%，超过这一门槛的策略将被视为风险或成本过高而被过滤掉。

类别4：Selection

```
"news_factor    = if_else(in(datacategories, 'news'), 1.4, 1);\n""neutral_factor = if_else(neutralization == 'SUBINDUSTRY', 1.2, 1);\n""bonus = if_else(author_sharpe >= 2.5 && author_sharpe <= 3.5, 1.2, 1);\n""score = news_factor * neutral_factor * bonus * operator_count;\n""if_else(turnover > 0.30, nan, score)",
```

- **新闻因子（news_factor）**  – 如果数据类别  `datacategories`  中包含  `'news'` ，则赋值 1.4，否则为 1。这暗示平台认为融入新闻信息的 α 可能抓住突发事件或市场情绪，从而赋予更高权重。
- **中性化因子（neutral_factor）**  – 判断是否采用了子行业（SUBINDUSTRY）水平的中性化。如果是，则给予 1.2 的加权，否则为 1。这样的处理有助于降低行业、板块效应，表明该策略风险管理更精细。
- **夏普奖励（bonus）**  – 同前面的表达式，如果作者的夏普比率处在 2.5 到 3.5 之间，则奖励 1.2，否则为 1。
- **综合评分计算**  – 将上述三个因子与  `operator_count` （表达式复杂度）相乘，得到最终得分。
- **换手率过滤**  – 当换手率大于 30%时，输出 NaN，从而排除换手过高、可能存在过多交易成本风险的策略。

类别5：Selection

```
"simplicity  = 1 / (operator_count + 1);\n""decay_bonus = if_else(decay < 1.5, 1.3, 1);\n""bonus = if_else(author_sharpe >= 2.5 && author_sharpe <= 3.5, 1.2, 1);\n""score = simplicity * decay_bonus * bonus;\n""if_else(turnover >= 0.30, nan, score)",
```

- **简洁度因子（simplicity）**  – 采用 1/(operator_count+1) 的方式，直接将表达式所用操作符数量转化为“简洁度分数”。操作符越少，即表达式越简洁，分数越高；这里的“+1”用于防止除零。简单往往意味着更容易解释和更低的过拟合风险。
- **衰减奖励（decay_bonus）**  – 根据  `decay`  值，如果小于 1.5则给予 1.3 的加乘，否则为 1。衰减较低可能代表信号持续性更好或噪音较少，这是积极的一面。
- **夏普比率奖励（bonus）**  – 同样地，如果作者的夏普比率位于最佳区间（2.5～3.5），则额外奖励 1.2，否则保持 1。
- **综合评分计算**  – 得分为上述三个因素的乘积，强调了“简洁性”与“信号稳定性”（衰减）以及风险调整后收益水平（夏普）的联合作用。
- **换手率过滤**  – 同样，如果换手率达到或超过 30%，则认为该 α 可能交易过于频繁，从而返回 NaN筛除之。

---

### 评论 #5 (作者: WL13229, 时间: 1 year ago)

楼上虽然AI味比较浓重，但还是有一定启发性，遂通过

---

### 评论 #6 (作者: JB71859, 时间: 1 year ago)

**Idea : 高质量低相关策略**

**Selection Expression:**

(self_correlation <= 0.5) * (prod_correlation < 0.4) * (turnover >= 0.1) * (turnover <= 0.3) * (long_count + short_count)

setting：


> [!NOTE] [图片 OCR 识别内容]
> U12
> UNGUNGE
> IIATOIICNT TOC
> Fast Expression
> Equiy
> REGION
> DOI
> SELECTION HANDUNG
> SELECTION UNIT
> USA
> DZT
> 100
> (0110
> settings
> S4par
 
最终结果： 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Agaregate
> Uata
> UAMUC
> TTe+
> 4.68
> 10.30%
> 25.04%6
> 4.9990
> 48.619600
> Vear
> Sharpe
> Turower
> CN
> Returns
> UawJown
> Margl
> UOI
> Short Comt
> 2013
> 170
> 11.5
> 4.4
> 11275
> 39:
> 1
> 143
> 201-
> 3
> 1_-
> 3:
> 3虎:
> 15
> 2015
> 9.7
> 4
> 256:
> +72:
> 1573
> 2015
> ?
> 193
> 10
> _3::
> 37:
> 2017
> 13.51
> 1.69
> 21E45s
> 2013
> 10.75
> 27.28
> 3:
> 4?:
> 2019
> 
> 21
> 1.17:
> 1;
> 1516
> 2020
> 2
> 257
> _3:
> +77:
> 2021
> 5.68
> 10.13
> 1.19
> -35
> 499:
> 5 
> 2022
> 5.23
> 10.458
> 3.52
> 297:
> -:
> 1621
> 2023
> 7.65
> 102
> 1292
> 35
> JGS::
> 533:
> 11
> Ce


**解释** : 选择自相关性和生产相关性都较低，换手率适中，覆盖度高的Alpha。

---

### 评论 #7 (作者: PW58059, 时间: 1 year ago)

**Idea:观察自己表现好的regular alphas特性，选取对应特性的regular alphas并叠加生产相关性低的alphas获得多样性增益**

**类别：selection**

注意：selection数量仅为展示，具体数值应该视你所选特性alphas的数量而定，但不建议将该数量设置过低。


> [!NOTE] [图片 OCR 识别内容]
> Super Simulation 6
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> GLB
> Positive
> 200


```
# 比如我自己的GLB regular alphas中，risk70这个数据集在TOP3000这个universe中表现都比较好：(in(datasets, "risk70") && universe=="TOP3000") # 如果想只选取自己的alphas做增益的化，也可以提前将alphas标好颜色，然后直接选取对应颜色，比如：color=="YELLOW" # 之后添加一些生产相关性低的alphas获取多样性增益，整体selection expression如下：(in(datasets, "risk70") && universe=="TOP3000") || (prod_correlation<0.4 && universe=="TOP3000" && turnover<0.15)  && not(own)
```

---

### 评论 #8 (作者: YB49779, 时间: 1 year ago)

**这是我SAC比赛提交的第一个因子**

**Idea:选择尽可能稳定的换手率区间内的优质因子**

**类别：selection**

**Setting： 
> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
> Instrument Type
> Region
> Unmerse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteuriatjon
> NaN Handling
> Unt Handling
> MaxTrade
> Equiz
> EUR
> TOPZSOO
> Fast ExPression
> 0.03
> Crowding FaCOrs
> Verify
**

**由于我是第一次在GM的池子中组SA，数量很多，所以我希望尽可能缩小搜索空间，示例中的区间仅为示例，我认为这个区间内的换手率较为稳定。**

# 我是G2组的只能选择simple alphas
# 操作符数小的，且被作者favorite相对更加稳定
# 低decay只是为了刨除那些为了过相关性测试盲目提高decay的劣质因子
# 最后由于我在TOP2500中做sa所以希望来自大的universe的因子占到更高权重
select:(!own&&in(classifications,'SIMPLE')&&turnover>0.08&&turnover<0.15&&operator_count<7&&favorite&&decay<6)*universe_size(universe)
combo:combo_a(alpha)

 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> ION
> OOOK
> 2012
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
  
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharoe
> UTNC
> Fitness
> REUTMS
> LTaVOCT
> IaTeIn
> 8.31
> 19.949
> 7.72
> 17.229
> 1.4796
> 17.289600
> Year
> Sharpe
> TurOVer
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> 0.00
> 00*
> 0.00
> 0.0395
> 0.0091
> 0O
> 2011
> 12.49
> 19.25*
> 13.39
> 23.3095
> 3395
> 733:
> 1317
> 12-0
> 2015
> 1112
> 20.13*
> 11.35
> 1.1091
> 329
> 20.362
> 1395
> 1327
> 2015
> 11.10
> 19.24*
> 12.45
> 1.2191
> 0.5791
> 82
> 1381
> 1340
> 2017
> 1.42
> 19.37北
> 10.05
> 13.5093
> 5495
> 13.52
> 1485
> 1455
> 2013
> 19.51沁
> 3.15
> 17.5593
> 0.4591
> 17.397
> 1485
> 14-1
> 2019
> 20.03光
> 15.7093
> 0.3795
> 15.542
> 129
> 1400
> 2020
> 5.96
> 21.57*
> 1.36
> 14.3393
> 0095
> 13.293
> 399
> 13653
> 2021
> |1
> 18.45*
> 1.75
> 20.1593
> 0.1091
> 21.8352
> 1539
> 1413
> 2021
> 5.53
> 20.03*
> 1.38
> 12.1593
> 0.7295
> 12.103
> 1440
> 1522
> 2022
> 3.19
> 19.3北
> 2.01
> 7.7095
> .4795
> 341:
> 1-71
> 1431
> 2023
> 0.13
> 21.2-5
> 0.01
> +2591
> 4593
> 257
> 1452
> 1312
> Investability constrained
> Aggregate Data
> Sharpe
> TCTO
> Fitne
> ReICns
> Cram
> Marain
> 5.59
> 9.02%
> 5.39
> 11.61%
> 1.91%
> 25.759600
> Ftres
> LonO
 
 
> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximur
> Winimup
> Last Run; Tue。06/03/2025,2.42 PN
> 0.4483
> -0.3787
> OOM
> 
> 1Ok
> 8
> 100
> ~0
> 0 A
> 0?
> 06 
> 0?
> 03
> 0.8
> ~0.9
> 0.7
> 0.0
> 令
 解释：在提交时prod为0.43，最终base有55，帖子是在一天后写的，此时prod提升到了0.44

---

### 评论 #9 (作者: WL13229, 时间: 1 year ago)

[YB49779](/hc/en-us/profiles/26716038151319-YB49779)  能想到favorite这个idea是真的妙啊

---

### 评论 #10 (作者: PZ64174, 时间: 1 year ago)

**类别：selection**

*in(classifications, "SIMPLE") && not(own)&&(datafield_count<2)&&(operator_count<5)&&(datacategory_count<2)&&(neutralization=='COUNTRY')&&(long_count>500)&&(short_count>500)&&turnover<0.15*

**in(classifications, "SIMPLE")**  *#G2第一周selection池子*

**not(own)**  *#选择非自己的*

**datafield_count<2**  *#限制数据字段个数*

***operator_count<5***  *#限制ops个数，防止出现混信号以及复杂因子*

***datacategory_count<2***  *#限制data类型个数*  *，防止出现混信号以及复杂因子*

**neutralization=='COUNTRY'**  *#因为做的是ASI的，所以选的这个中性化（此中性化在多国家region有比较好的表现，eur也可以选用）*

**(long_count>500)&&(short_count>500)**  *#防止缺少数据的不稳定alpha*

***turnover<0.15***  *#限制换手率*

*注意：selection数量仅为展示，具体数值应该视你所选特性alphas的数量而定，但不建议将该数量设置过低。*

*******（不知道为啥我评论的时候没法放图片，只好口述下selection settings，region：ASI,***  *Selection Handling:Non-Nan,***  *Selection Limit:300***  ***）***

Sharpe 5.33 Turnover 7.97% Fitness 5.53  Returns 13.48% Drawdown 1.50% Margin 33.82‱

**Combo Expression**

**combo_a(alpha)**

---

### 评论 #11 (作者: WP88606, 时间: 1 year ago)

一种随机生成SuperAlpha，进行机器回测的方式，之前发的，可以混个笔记本吗？

[../顾问 FZ60707 (Rank 78)/[Commented] 一种随机生成 SuperAlpha进行机器回测的方式代码优化.md](../顾问 FZ60707 (Rank 78)/[Commented] 一种随机生成 SuperAlpha进行机器回测的方式代码优化.md)

---

### 评论 #12 (作者: MY27687, 时间: 1 year ago)

**类别：selection**

**Selection Expression：**

```
in(classifications, "SIMPLE")&& not(own)&&(in(datasets,'analyst4')+in(datasets,'analyst69')+in(datasets,'model110'))&&turnover<0.02
```

**setting： 
> [!NOTE] [图片 OCR 识别内容]
> Simulation 2
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> GLB
> NonNan
> 100
> Combo settings
> UNIVERSE
> NEUTRALIZATION
> MINVOLIM
> Subindustry
> DECAY
> TRUNCATION
> PASTEURIZATION
> UNIT HANDLING
> 008
> On
> Verity
> NAN HANDLING
> TEST PERIOD
> MAX TRADE
> On
> YEARS
> MONTHS
> 0ff
> Save as Default 
> Apply
> Super
**

**Idea:**

成为顾问后一直在做EUR，后来转战ASI 发现有些数据集信号在不同 Universe下 依然信号很好，所以用来super alpha的 **Selection Expression** 选取换手率turnover<0.02 ，analyst4 analyst69 以及model110的alpha进行组合，由于分配到了G2所以选取的alpha质量并不高。

结论：


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Snarpe
> Turnover
> Fitness
> Rezurns
> Drawdown
> Marsin
> 5.46
> 14.409
> 6.25
> 18.899
> 2.849
> 26.249600
> Year
> Sharpe
> Tumover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 8.33
> 14.679
> 11.78
> 25.10%
> 1.023
> 35.585330
> 3580
> 3592
> 2014
> 3.34
> 14.359
> 11.01
> 22.263
> 0.5935
> 31.03523
> 4010
> 1036
> 2015
> 7.06
> 14.3830
> 9,06
> 23,593
> 1.239
> 32.9_533
> 4153
> 1132
> 2016
> 5,31
> 14.519
> 5.5.
> 15,319
> .09%
> 21,79530
> 4010
> 4032
> 2017
> 5.26
> 14.12%
> 5,32
> 12.219
> 0.603
> 17.295330
> 4154
> 4207
> 2018
> 14.-79
> 15,279
> 3635
> 21.109330
> 4452
> 1537
> 2019
> 5.7
> 14.-59
> 5,78
> 14.59%
> 1.203
> 20.20530
> 4201
> 4178
> 2020
> 111
> 14.509
> 4,56
> 18,56%
> 2.8-3
> 25.739230
> 4350
> 4350
> 2021
> 5.73
> 14.2330
> 6,99
> 21,159
> 1.-795
> 29.72533
> 5241
> 5353
> 2022
> 4.01
> 14.329
> 49
> 21,729
> 2.389
> 30.329330
> 5078
> 5157
> 2023
> -1.45
> 13.8-9
> -5,36
> 20,059
> 2.00F
> 23,979330
> 4550
> 4593



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/03/2025 EDT
> anonymoUs
> Mdd Mpha to
> Ust
> 囚 Openalpha details in newtab
> N Chart
> Pnl
> N
> 134
> 161
> Q
> 1411
> 12u
> 10N
> OOOK
> OOOK
> OOOK
> ZOOOK
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


信号还可以，但是PC有点高


> [!NOTE] [图片 OCR 识别内容]
> ~
> Correlation
> Self Correlation
> Maximum
> Minimup
> Last Run:
> Prod Correlation
> Maximum
> Minimup
> Last Run: Tue  06/03/2025,10.31 PI
> 0.7410
> -0.4102
> 1N
> 1Ok
> 0.0.
> Alphas: 40 369
> 矍
> 100
> 昱
> 皂


---

### 评论 #13 (作者: KD86036, 时间: 1 year ago)

**类别：combo**

**idea:将市净率、市盈率等有经济学意义的概念迁移至SUPERALPHA 。**

**setting:和楼上大佬一样评论区加载不了图片，只好口述参数设置** EUR,TOP2500,DECAY:12,Neutralization:RAM,Selection Limit:100

**Combo Expression:**

**step1：基于alpha statistic生成有经济学意义的特征**

stats = generate_stats(alpha);  # 生成a各类lpha statistic

book_value=stats.pnl/stats.returns; #账面规模

cap=stats.trade_value+stats.hold_value; #市值

eps=stats.pnl/(stats.trade_shares+stats.hold_shares);#每股收益

price=cap/(stats.trade_shares+stats.hold_shares); #价格

book_value_per_share=book_value/(stats.trade_shares+stats.hold_shares);#每股账面价值

**step2：基于以上特征进一步构建PB、PE等有经济学意义的表达式**

PE(市盈率)=price/eps

PB(市净率)=price/book_value_per_share

**step3：将上述特征结合时间序列操作符进行回测会产生很不错的效果。**

注意：不要局限于常规时间序列操作符，可以与协方差，偏度，回归等时序操作符结合使用

Example：ts_co_skewness(eps,ts_delay(eps,20) , 252)>0

Result：Sharpe 5.51 Turnover 8.62% Fitness 6.56  Returns 17.74% Drawdown 3.69% Margin 41.16‱

self corr:0.5637,prod corr:0.5637

此处selection仅为参考，欢迎大家拓展：not(own)*(1-self_correlation)*(1-turnover)

---

### 评论 #14 (作者: ZL35633, 时间: 1 year ago)

分享一个selection表达式的格式：

每行写一个表达式，调试的时候可以注释整行不影响执行。

```
# 做bool判断的表达式写在这里，用来筛选需要的alphabool = (    not (own) &&    in(classifications, "POWER_POOL") &&    ( turnover>0.04 && turnover<0.30 ) &&    datacategory_count<=3 &&    short_count+long_count > 1000 &&    1);# 计算权重的表达式写在这里weight = (    1    *(prod_correlation)    *abs(self_correlation-0.5)    *(1-turnover));bool * weight
```

在PPAC中，pc值大的可能是顾问挑选的历史表现好的alpha


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
>  Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> EUR
> TOP2500
> Fast Expression
> 20
> 0.01
> Subindustry
> On
> Off
> Verify
> Off



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 9.50
> 6.099
> 12.37
> 21.189
> 1.389
> 69.51%600


---

### 评论 #15 (作者: WL13229, 时间: 1 year ago)

[【SuperAlpha灵感】因子择时模型 – WorldQuant BRAIN](../顾问 JL16510 (Rank 18)/[Commented] 【SuperAlpha灵感】因子择时模型Alpha Template.md)   [YW93864](/hc/en-us/profiles/14096946892439-YW93864)

---

### 评论 #16 (作者: WH24469, 时间: 1 year ago)

类别：SELECTION

（无法上传图片）

settings：GLB，1， positive， 50

Idea:

1.有color或者有category的alpha，说明alpha有其特殊之处，要不很好要不很差，从中选出好的。

2.添加一个prod corr范围来限制过拟合的alpha。

3.os_start_date比较新的说明alpha没有面临失效风险的（这一part也考虑过最近几年performance的，有兴趣的朋友可以自行探索）。

```
in(classifications, "POWER_POOL") &&prod_correlation < 0.5 && prod_correlation > 0.1 &&color != "NONE" &&category != "NONE" &&os_start_date >= "2022-01-01"
```

IS performance:

sharpe : 8.01

turnover : 10.32%

fitness7.28

returns : 10.32%

drawdown : 0.80%

margin : 20.01

已经提交了一个SA了，所以PC会比较高。

补充说明：pc > 0.1是因为power pool中有些author会提交很差的alpha，这些alpha呈现厂或者只有近几年的数据，但凡整体走势是向上的都会导致指标非常好看，pc也比较低，所以我想剔除掉这些“要不很差”的alpha。

另外就是本来有color和有category且2022年后开始os的alpha个人认为已经比较“稀有”了，且现在consultant越来越多，造出来pc低于0.1的且优秀的alpha难度比较大，所以我选择规避掉这部分风险。

最主要还是剔除尾部风险

---

### 评论 #17 (作者: WL13229, 时间: 1 year ago)

[WH24469](/hc/en-us/profiles/13991511763607-WH24469)  请补充阐述 以下选择的原因

```
prod_correlation > 0.1
```

---

### 评论 #18 (作者: WH24469, 时间: 1 year ago)

pc > 0.1是因为power pool中有些author会提交很差的alpha，这些alpha呈现厂或者只有近几年的数据，但凡整体走势是向上的都会导致指标非常好看，pc也比较低，所以我想剔除掉这些“要不很差”的alpha。

另外就是本来有color和有category且2022年后开始os的alpha个人认为已经比较“稀有”了，且现在consultant越来越多，造出来pc低于0.1的且优秀的alpha难度比较大，所以我选择规避掉这部分风险。

最主要还是剔除尾部风险

---

### 评论 #19 (作者: JL40454, 时间: 1 year ago)

User-selected-ntr思路:

Selection的结构简而言之为条件+评分, 在此只阐述条件思路.

选取提交者心中特殊的alpha, 比如颜色, 星标, tag等, 通过对规定域中的人工标签选出被特殊关照的alpha:

- color ==/!= <COLOR>: 颜色筛选;
- favorite/not(favorite): 是否星标;
- tag ==/!= <TAG>: 不太好选, 建议使用AI创建tag池进行选取测试;
- neutralization ==/!= <NEUTRALIZATION>: 剔除不经思考的machine alpha，如果他的neutralization不是machine alpha的默认设置，默认他经过了鲁棒性检测，也属于被用户特殊关照的一类，但是有可能默认设置的值不一定是NONE，或许常用的一些其他neutralization选项也可以加入不等于的条件;
- category ==/!= <CATEGORY>: 是否选择类别;

示例如下, score可随意修改:

> is_special = favorite || color!= "NONE" || neutralization != "NONE" || category != "NONE";
> other_condition = os_start_date > "2024-01-01" && operator_count<7 && dataset_count ==1;
> condition = is_special && other_condition;
> score =(1-prod_correlation)*(1-self_correlation)/turnover;
> if_else(condition, score, nan)

设置:

> "settings":{
> "nanHandling":"OFF",
> "instrumentType":"EQUITY",
> "delay": 1,
> "universe": "TOP3000",
> "truncation": 0.01,
> "unitHandling":"VERIFY",
> "selectionLimit": 250,
> "selectionHandling": "POSITIVE",
> "pasteurization":"ON",
> "region": "USA",
> "language":"FASTEXPR",
> "decay": 5,
> "neutralization": "NONE",
> "visualization": False,
> "testPeriod":"P0Y",
> 'maxTrade': "ON"
> }

---

### 评论 #20 (作者: WL13229, 时间: 1 year ago)

[JL40454](/hc/en-us/profiles/28831795834263-JL40454)

neutralization != "NONE"

这个估计不太好，可以考虑删除，您觉得呢

---

### 评论 #21 (作者: LW49759, 时间: 1 year ago)

### 类别：selection

### 表达式：

```
(not(own)&&(in(classifications,'POWER_POOL'))&&((turnover<0.29&&turnover>0.27)||(turnover<0.25&&turnover>0.23)||(turnover<0.20&&turnover>0.17)||(turnover<0.14&&turnover>0.11)||(turnover<0.09&&turnover>0.05)||(turnover<0.04&&turnover>0.02))&&(operator_count<8)&&(prod_correlation<0.6&&prod_correlation>0.2)&&(dataset_count<=2)&&(long_count>300)&&((neutralization=='SLOW')||(neutralization=='FAST')||(neutralization=='SLOW_AND_FAST')))/(turnover*tanh(turnover)*sigmoid(self_correlation)*sigmoid(prod_correlation))
```

### idea：

选取SLOW，FAST和SLOW_AND_FAST的Neutralization，settings选择SLOW_AND_FAST，记得之前老师说过风险中性化的表现会更加稳健，在此基础上再使用风险中性化，可能会提高稳健性，除了上面三个还可以选择CROWDING，STATISTICAL等分别尝试

selection其他说明：

- turnover分片选择使得每次选到的alpha尽可能不一样
- operator_count和dataset_count使得信号尽量纯粹
- prod_correlation>0.2可以规避一些pnl很奇怪的因子
- 除法后面的权重计算是参考的游戏王的帖子，按照turnover进行加权，按照correlation进行加权，sigmoid是为了防止权重变化过大

### settings：


> [!NOTE] [图片 OCR 识别内容]
> Super Simulation 2
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> EUR
> Positive
> 100
> Combo settings
> UNIVERSE
> NEUTRALIZATION
> TOP2500
> SIOW + Fast Factors
> DECAY
> TRUNCATION
> PASTEURIZATION
> UNIT HANDLING
> 0.08
> On
> Verify
> NAN HANDLING
> TEST PERIOD
> MAX TRADE
> On
> YEARS
> MONTHS
> On


（实际选到了97个）

### 表现：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 10M
> 5,0OOK
> 2015
> 2017
> 2019
> 2021
> 2023



> [!NOTE] [图片 OCR 识别内容]
> w IS Summary
> Period
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 7.63
> 7.829
> 8.04
> 13.899
> 0.879
> 35.55%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 9.20
> 9.099
> 10.89
> 17.53%
> 0.449
> 38.589o。
> 1021
> 1080
> 2014
> 9.13
> 7.639
> 10.08
> 15.25%
> 0.31%
> 39.97960。
> 1315
> 1304
> 2015
> 8.36
> 7.93%
> 9.14
> 14.939
> 0.559
> 37.68%o0
> 1335
> 1391
> 2016
> 8.04
> 7.649
> 8.36
> 13.51%
> 0.61%
> 35.36900
> 1336
> 1388
> 2017
> 6.61
> 7.979
> 5.65
> 9.13%
> 0.439
> 22.929o。
> 1455
> 1498
> 2018
> 5.22
> 8.029
> 4.41
> 8.93%
> 0.8796
> 22.289o。
> 1457
> 1474
> 2019
> 7.56
> 7.859
> 7.44
> 12.129
> 0.539
> 30.899o。
> 1393
> 1440
> 2020
> 6.37
> 7.879
> 7.09
> 15.48%
> 0.729
> 39.34900
> 1354
> 1412
> 2021
> 10.28
> 7.199
> 12.78
> 19.339
> 0.429
> 53.789o。
> 1462
> 1504
> 2022
> 9.91
> 7.259
> 11.27
> 16.18%
> 0.089
> 44.63900
> 1466
> 1552
> 2022
> 6.24
> 7.139
> 6.19
> 12.329
> 0.689
> 34.579600
> 1395
> 1507
> 2023
> 13.59
> 6.02%
> 17.99
> 21.909
> 0.109
> 72.75900
> 1339
> 1430



> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last
> Run:
> Prod
> Maximum
> Minimum
> Last Run: Thu,
> Correlation
> 06/05/2025,10:08
> AM
> 0.6647
> 0.4128
> IOOM
> IM
> 訾
> IOk
> 昱
> 100
> }
> 0.01
> 89
> 0~0?03
> 0901
> 9:
> 0?"
> 8:
> -0.8
> -0.7
> -0.6
> -0.5
> 0.0
> 0.5
> 0.8
> 0.9
> 1.0
> -0.4
> -0.3
> -0.2
> -0.1
> 0.4
> 0.9..
> 0.2...
> 0.6..
> 0.7 ..
> -0.1.
> 0.0.
> 0.1. _
> 0.4..
> 0.5.
> 0.8..
> %
> -0.5..
> -0.3..
> -0.2..
> -1.0.
> -0.9.
> $
> -0.4.


---

### 评论 #22 (作者: CH62432, 时间: 1 year ago)

**类别:Selection;**

**Idea:**

> **中心思想是优先挑选 **信号方向性强且表达式简洁的alpha;****
> ****其余的操作 :数据类型、换手率的限制等等...,通过这些操作来强化中心思想选中alpha****

**Selection Expresson:**

```
abs_score = if_else(abs(long_count - short_count) > 1000, 1.5, 0.5);op_score = if_else(operator_count <= 5, 1.5, 0.5);final_score = (abs_score * op_score) * (in(classifications, 'POWER_POOL') && !own) * (in(datacategories, "analyst") + in(datacategories, "socialmedia") + in(datacategories, "sentiment")) *(turnover < 0.2);final_score;
```

Settings:


> [!NOTE] [图片 OCR 识别内容]
> Super Simulation 3
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> USA
> Positive
> 100
> Combo settings
> UNIVERSE
> NEUTRALIZATION
> T0P3000
> Subindustry
> DECAY
> TRUNCATION
> PASTEURIZATION
> UNIT HANDLING
> 0.08
> On
> Verify
> NAN HANDLING
> TEST PERIOD
> MAX TRADE
> On
> YEARS
> MONTHS
> Off
> Save as Default
> Apply


**表现**


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawcown
> Margin
> 5.72
> 7.849
> 6.64
> 16.849
> 1.9596
> 42.989600
> Year
> Sharpe
> Turover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.0096
> 0.00
> 0.009
> 0.009
> 0OYoo
> 2014
> 7.05
> 9.4990
> 7.68
> 14.859
> 1.01%
> 31.2930
> 1386
> 483
> 2015
> 7.05
> 7.2590
> 8.13
> 16.529
> 0.8595
> 45.833500
> 1555
> 1517
> 2016
> 7.13
> 6.5990
> 7.83
> 15,079
> 8795
> 45.02963o
> 1522
> 1541
> 2017
> 7.88
> 7.1796
> 8.75
> 15.4196
> 0.549b
> 42.92963o
> 1493
> 1540
> 2018
> 4.27
> 7.1396
> 4.00
> 10.989
> 8890
> 30.81900
> 1527
> 1521
> 2019
> 4.78
> 7.8596
> 4.64
> 11.7790
> 6996
> 29.98350
> 1572
> 1455
> 2020
> 3.79
> 9.129
> 4.24
> 15.6490
> 9596
> 34.319500
> 1514
> 1520
> 2021
> 6.52
> 7.6396
> 9.49
> 26.4896
> 1.359
> 69.39350
> 1502
> 1587
> 2022
> 6.87
> 7.5890
> 24.849
> 1.359
> 64.68%00
> 1512
> 1577
> 2023
> 2.17
> 10.9990
> 1.42
> -5.389
> 0.5890
> 79350
> 1562
> 1548
> Risk neutralized
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawgown
> Margin
> 5.80
> 7.849
> 5.63
> 11.789
> 1.3596
> 30.079600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawJOwn
> Margin
> 5.39
> 7.219
> 6.00
> 15.489
> 1.879
> 42.979600



> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximum
> UinimUn
> Last Run; ThU。 06/05/2025,
> 1.43 PN
> 0
> 0.6106
> -0.6088
> 10ON
> TN
> 簟
> TOk
> 昱
> 100
> 0.6.
> 0.7
> 8
> Alphas: 2
> 0.01
> 89
> 01
> 0^
> 02
> 0~
> 09
> 02
> 0?
> 02
> 01
> 09
> ~9
> 01
> 02
> 0 
> 09
> 0^ 
> 02
> 0?
> 0^
> 05"
> 06"
> 03
> 09
> ~0.6
> -0.5
> 0.5
> 0,6
> 0.8
> 0.8
> ~0.3
> 0.7.
> -1.0。
> 0.9
> ~0.8。
> ~0.6。
> ~0.5。


---

### 评论 #23 (作者: LZ14530, 时间: 1 year ago)

Idea: 在G4组power pool，对上面的SELECTION Idea做了许多尝试，发现选择的alpha中，returns的高低跟alpha质量高低有一定的正相关，期望基于年波动率，给returns高的alpha做高权重

类别：Combo

（无法上传图片）

Setting:

> Region: USA, Delay: 1, Positive: 40;
> Universe: TOP3000,  Neutralization: Subindustry,  Decay: 6,  Truncation: 0.08,  Pasteurization: ON,  Unit Handling: Verify,  Nan Handling: ON,  MaxTrade: OFF

Combo Expression:

```
stats=generate_stats(alpha);ts_std_dev(stats.returns,252)/1
```

测试了多个selection，此combo在margin上优于equal weight

---

### 评论 #24 (作者: WL13229, 时间: 1 year ago)

[LW49759](/hc/en-us/profiles/26717472313751-LW49759)

可否阐释一下tanh和sigmoid的作用，以及它们对Alpha筛选分的影响

---

### 评论 #25 (作者: 顾问 WX84677 (Rank 69), 时间: 1 year ago)

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

### 评论 #26 (作者: AK76468, 时间: 1 year ago)


> [!NOTE] [图片 OCR 识别内容]
> Super Simulation 9
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> DELAY
> SELECTION HANDLING
> SELECTION LIMIT
> USA
> Positive
> 1000
> Combo settings
> UNIVERSE
> NEUTRALIZATION
> T0P3000
> RAM
> DECAY
> TRUNCATION
> PASTEURIZATION
> UNIT HANDLING
> 5
> 0.08
> On
> Verify
> NAN HANDLING
> TEST PERIOD
> MAX TRADE
> Off
> 2
> YEARS
> MONTHS
> Off


## 假设：

- SIMPLE POOL中的alpha是去除噪音的alpha，每个alpha只保留其有价值的部分。
- 在SIMPLE池中，如果一个alpha的运算符和字段数量超出常规，那么认为这个alpha是作者带有目的实现的Human alpha，具有经济学含义。
- 在SIMPLE池中，如果一个alpha仅有一个运算符和字段，那么认为这个字段本身就具有极强的经济学含义。

## 发现：

> 池内绝大部分的alpha的op数量在 [ 1, 8 ]，绝大部分的alpha的datafield数量在[ 1, 3 ]

## **idea：将极简alpha和复杂alpha组合**

### 类别：Selection

```
(in(classifications,'SIMPLE')&&operator_count<30&&operator_count>10&&//选取运算符介于[10,30]的alphadatafield_count>4&&//选取使用字段大于4的alpha(universe_size(universe)*0.3<long_count&&universe_size(universe)*0.3<short_count)&&//选取多空平衡的alpha，增强可信度os_start_date<"2023-07-01")//选取一定的OS范围，增强可信度+(in(classifications,'SIMPLE')&&operator_count==1&&dataset_count==1&&//选取极简alpha(universe_size(universe)*0.3<long_count&&universe_size(universe)*0.3<short_count)&&os_start_date<"2023-07-01")
```

> *alpha数量=78*

#### combo

> 减弱极简alpha中的相似性，按照相关性分配权重

```
stats =generate_stats(alpha);innerCorr =self_corr(stats.returns,500);ic =if_else(innerCorr >0.8, nan, innerCorr);maxCorr =reduce_max(ic);1 - maxCorr
```


> [!NOTE] [图片 OCR 识别内容]
> 叫 IS
> Summary
> Period
> TRAIN
> TEST
> IS 
> 09
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 6.13
> 14.48%
> 7.62
> 22.379
> 2.659
> 30.90%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 7.35
> 14.969
> 7.56
> 15.83%
> 0.749
> 21.169oo
> 1519
> 1556
> 2014
> 8.55
> 14.549
> 10.31
> 21.149
> 0.629
> 29.089o。
> 1550
> 1546
> 2015
> 8.01
> 14.649
> 9.35
> 19.95%
> 0.679
> 27.269o。
> 1559
> 1578
> 2016
> 8.20
> 14.759
> 9.97
> 21.790
> 0.769
> 29.559oo
> 1567
> 1560
> 2017
> 8.03
> 14.319
> 9.28
> 19.11%
> 0.609
> 26.71%o。
> 1541
> 1559
> 2018
> 5.58
> 14.20%
> 6.11
> 17.01%
> 1.11 %
> 23.959o。
> 1574
> 1545
> 2019
> 5.79
> 14.339
> 6.52
> 18.199
> 0.959
> 25.399o。
> 1566
> 1542
> 2020
> 5.61
> 14.379
> 7.07
> 22.839
> 1.53%
> 31.78%o。
> 1553
> 1547
> 2021
> 18.36
> 13.749
> 44.33
> 80.11%
> 0.00%
> 116.599oo
> 1580
> 1567
> 2021
> 7.13
> 13.91%
> 12.15
> 40.409
> 2.489
> 58.089o。
> 1577
> 1571
> 2022
> 4.79
> 14.759
> 6.57
> 27.77%
> 2.659
> 37.66%o。
> 1598
> 1555
> 2023
> 6.70
> 14.33%
> -8.93
> 25.489
> 1.46%
> -35.559oo
> 1608
> 1564


---

### 评论 #27 (作者: WL13229, 时间: 1 year ago)

[AK76468](/hc/en-us/profiles/28846915371031-AK76468)

请阐述一下设置os start date的原因及具体参数由来

---

### 评论 #28 (作者: AK76468, 时间: 1 year ago)

设置os start date可以选取特定时间范围的alpha，我了解到在2023年第三季度时有ACE的比赛，这时顾问们开始广泛使用接口machine alpha。那么假设在此之前，human alpha的占比会比现在多，手工混信号要比机器混信号成本更高，所以op数量多的alpha更可能是有经验顾问手搓出来的，而不是machine混信号出来的，就增大了selection的可信度

> 如果一个alpha的运算符和字段数量超出常规，那么认为这个alpha是作者带有目的实现的Human alpha，具有经济学含义。

---

### 评论 #29 (作者: LX31898, 时间: 1 year ago)

KD86036

有关公式ts_co_skewness(eps , ts_delay(eps , 20) , 252)>0：

我是刚解锁superalpha的有条件顾问，然而在复现大佬的idea过程中发现我并没有ts_co_skewness这个操作符。问了一下deepseek有什么替代的表达式，它给了如下两种替换方法，数学功底好的大佬帮我看看这么替换有没有道理：

方法1：用协方差和矩操作符组合实现
协偏度本质是联合三阶矩，可通过以下操作符组合实现：
X = (eps - ts_mean(eps, 252)) ** 2;  # X的平方偏差
Y = ts_delay(eps, 20) - ts_mean(ts_delay(eps, 20), 252);  # Y的中心化
co_skew = ts_covariance(X, Y, 252);  # 协方差代替联合矩
co_skew > 0

方法2：用回归残差实现（更稳定）
通过线性回归分离非线性依赖，捕捉偏度特征：
# 步骤1: 对Y = ts_delay(eps, 20) 做线性回归
residual = ts_residual(Y, X_linear, 252);  # 残差包含非线性信息
# 步骤2: 计算残差与X平方的协方差
co_skew = ts_covariance(X ** 2, residual, 252);
co_skew > 0
其中 X_linear 可包含线性因子如：
X_linear = ts_mean(eps, 252) || ts_delta(eps, 1) || ... ;  # 拼接线性特征

(ts_residual可用ts_regression替代)

---

### 评论 #30 (作者: KL64183, 时间: 1 year ago)

```
d1 = if_else(color != "NONE", 1, 0);d2 = if_else(category != "NONE", 1, 0);d3 = if_else(!in(datacategories, "model"), if_else(!in(datacategories, "fundamental"), 1, 0.5),0);d4  = if_else(turnover >= 0.5, 0.5, if_else(turnover >= 0.3, 1, if_else(turnover >= 0.1, 0.5, 1)));f1 = sigmoid(turnover/datafield_count);f2 = sigmoid(turnover/operator_count+1);f3 = sigmoid(1/log(abs(long_count-short_count)/universe_size(universe)));in(classifications, "SIMPLE")*(3*(f1+f2)+6*f3+(d1+d2+d3+d4))/16
```

1. **離散指標 (d1 ~ d4)**
   - **d1** ：檢查  `color`  是否為 “NONE”，若不是則 d1=1，否則為 0。
   > 目的：篩選出使用者標註的顏色特徵(alpha)，代表作者在該 alpha 構建上投入較多心力。
   - **d2** ：檢查  `category`  是否為 “NONE”，若不是則 d2=1，否則為 0。
   > 目的：同上述，確保納入使用者手動標籤的分類標籤(alpha)。
   - **d3** ：根據  `datacategories`  給予權重：
   - 若不屬於 “model” 也不屬於 “fundamental”，d3=1（最高權重）；
   - 若屬於 “fundamental” 且不屬於 “model”，d3=0.5（中等權重）；
   - 若屬於 “model”，d3=0（最低權重）。
   > 目的：減少純模型資料的比重、避免基本面資料過度集中，提升資料類別多樣性。
   - **d4** ：根據  `turnover` （換手率）的區間進行分段賦值：
   - ≥ 0.5 → 0.5（高換手率降低利潤率）；
   - [0.3, 0.5) → 1（中度穩定區間）；
   - [0.1, 0.3) → 0.5；
   - [0, 0.1) → 1（低換手率也納入多樣性考量）。
   > 目的：在不同換手率區間中平衡選取高、中、低換手率的 alpha 池。
2. **連續函數 (f1 ~ f3)**
   - **f1 = sigmoid(turnover / datafield_count)**
   > 衡量每個資料欄位平均帶來的換手率大小，高值代表該欄位資訊量較豐富。
   - **f2 = sigmoid(turnover / (operator_count + 1))**
   > 衡量所用運算子效率，運算子越多則分母越大，相對降低效果。
   - **f3 = sigmoid( 1 / log( |long_count − short_count| / universe_size ) )**
   > 評估多空部位分佈的均衡程度；以對數降低敏感度，再取倒數並映射至 (0,1)。
3. **最終分數組合**
   ```
   score =
   in(classifications, "SIMPLE")
   * ( 3*(f1 + f2) + 6*f3 + (d1 + d2 + d3 + d4) ) / 16
   ```
   - 只有當  `classifications`  包含  `"SIMPLE"`  時才計算分數。
   - 將 f1、f2 的合計乘以 3，f3 乘以 6，離散指標之和與之相加後，以 16 為總權重正規化。
   - 選擇 f3 加權 6（優於 3）顯示多空均衡的 alpha 效果更佳；整體採用等權正規化以保持簡潔。

透過上述設計，該邏輯旨在：

- 優先篩選出經作者精心標註的 alpha；
- 平衡不同資料類別與換手率特性；
- 強調多空部位均衡性；
- 並在「SIMPLE」分類下統合所有指標，生成最終分數。


> [!NOTE] [图片 OCR 识别内容]
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
>  Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> EUR
> TOP2500
> Fast Expression
> 0.08
> Statistical
> On
> Off
> Verify
> Off
> Delay



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> I5S
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 10.04
> 10.299
> 12.17
> 18.36%
> 1.31%
> 35.709600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 14.17
> 11.0096
> 19.25
> 23.07%
> 0.37%
> 41.949000
> 1059
> 1042
> 2014
> 15.33
> 10.0996
> 22.79
> 27.63%
> 0.22%
> 54.790000
> 1301
> 1319
> 2015
> 12.28
> 9.7296
> 15.95
> 21.09%
> 9
> 43.400000
> 1368
> 1360
> 2016
> 13.35
> 10.0696
> 18.36
> 23.63%
> 0.2796
> 46.970000
> 1357
> 1368
> 2017
> 12.93
> 10.1596
> 15.19
> 17.26%
> 0.319
> 34.000000
> 1465
> 1490
> 2018
> 9.45
> 10.6196
> 10.53
> 15.51%
> 0.469
> 29.249000
> 1441
> 1492
> 2019
> 12.53
> 10.5996
> 15.58
> 19.32%
> 9
> 36.490000
> 1388
> 1447
> 2020
> 6.94
> 10.5396
> 7.98
> 16.52%
> 0.8896
> 31.389000
> 1369
> 1398
> 2021
> 8.09
> 10.0896
> 8.63
> 14.21%
> 0.549
> 28.200000
> 1478
> 1490
> 2022
> 2.65
> 10.1096
> 1.81
> 5.82%
> 1.31%
> 11.539000
> 1433
> 1476
> 2023
> 6.21
> 9.43%6
> 5.83
> 11.01%6
> 0.20%
> 23.359000
> 1354
> 1417



> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximum
> Minimum
> Last Run: Sat。 06/07/2025,3:39 PM
> 0.6603
> -0.4784
> 10OM
> 1M
> 簟
> 1Ok
> 晷
> 8
> 100
> 09
> 0?
> 02
> 03
> 06
> 01
> 03
> 02
> 1.0
> 0.0.
> 0.7.
> ~0.5。


---

### 评论 #31 (作者: WL13229, 时间: 1 year ago)

[LW49759](/hc/en-us/profiles/26717472313751-LW49759)

```
((turnover<0.29&&turnover>0.27)||(turnover<0.25&&turnover>0.23)||(turnover<0.20&&turnover>0.17)||(turnover<0.14&&turnover>0.11)||(turnover<0.09&&turnover>0.05)||(turnover<0.04&&turnover>0.02))
```

请思考一下这个条件，如果你分得再细一些，基本可能所有turnover的Alpha都会被选中，是不是跟删掉它差不多呢

---

### 评论 #32 (作者: 顾问 YX23928 (Rank 8), 时间: 1 year ago)

由于无法上传图片的原因，setting/selection/combo均以文字形式展示：

SETTING：

Region:EUR,Universe:TOP2500,Decay:0,Neutralization:RAM,Max Trade:Off

Selected Alphas：300

#选择新的Neutralization，避免高相关性问题

Selection Expression:

(!own&&in(classifications,'SIMPLE')&&turnover>0.05&&turnover<0.10&&operator_count<8&&decay<10)*universe_size(universe)*(long_count + short_count)

#选择低turnover，低operator_count且(long_count + short_count)较多的alpha

Combo :

stats = generate_stats(alpha);std = ts_std_dev(stats.returns,60);std_crowd = std /ts_delay(std,60);ts_rank(-std_crowd ,500)

#选用YW93864大佬因子择时模型，可减缓因等权选取因子衰减问题

Sharpe:6.48;Turnover:14.89%;Fitness:6.78;Returns:16.29%;Drawdown:1.94%;Margin:21.87‱;

prod correlation:0.64

---

### 评论 #33 (作者: 顾问 KZ79256 (Rank 21), 时间: 1 year ago)

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

### 评论 #34 (作者: LH44620, 时间: 1 year ago)

分享几个combination，经过我回测了各种各样的池子，表现较好的。

1.

```
combo_a(alpha, nlength = 255, mode = 'algo1')+Neutralization选择Statistical
```

虽然combo_a操作符是大家常用的组合superAlpha的选择。可是经过一些回测，我发现combo_a配合上Statistical会有更好的表现。我的池子是g2的simple，所以指标可能没有那么高。这个选择我测试了多个地区，感觉都是成立的。并且corr也较低。


> [!NOTE] [图片 OCR 识别内容]
> Combo Expression
> COIbO
> (alpha,
> nlength =250,
> mode
> alg01
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
> Max Trade
> Equity
> EUR
> TP2500
> Fast Epression
> 0.03
> Stztistizzl
> Verfy
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> SaroE
> UTRCEI
> FITESS
> TCUTR
> UT3OOWI
> Marein
> 9.93
> 11.369
> 11.55
> 16.9196
> 1.2596
> 29.789600


2.

```
combo_a(normalize(alpha), nlength =250, mode = 'algo1')
```

在combo_A的基础上加上normalize(x)操作符。这种用法是在看到wq的sa英文课程时，看到了类似的用法。于是我就想能不能先标准化一下再进行combo_A呢？结果还不错。corr也比较低。池子依然是g2的simple。这个选择我测试了多个地区，感觉也都是成立的。
 
> [!NOTE] [图片 OCR 识别内容]
> Combo Expression
> COIbO
> (normalize(alpha
> nlength
> =250
> mode
> a1801
> Simulation Settings
> Instrument Type
> Region
> Unjverse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurizatjon
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> EUR
> TP1200
> Fast Epression
> 0.03
> Stztistizzl
> Welf



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 13N
> 12A
> 1IMI
> ION
> OOOK
> OOOK
> 70OOK
> OOOK
> 5OOOK
> LOOOK
> OOOK
> 02/25/2015
> Equal Weight Pnl:
> 4,195,03k
> ComboPnl:
> 2,471.55k
> OOOK
> Investability Constrained Pnl:
> 882.17k
> OOOK
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



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> SharO E
> TUTMCVET
> Ftness
> ECUTI
> UF3UOWn
> UaTaIn
> 7.13
> 12.2796
> 7.64
> 14.36%
> 1.7296
> 23.409600
 可以看到后期pnl表现超过等权了。

3.

```
x = generate_stats(alpha);ts_co_kurtosis(x.drawdown, x.returns, 215)
```

目的是看极端回撤和极端收益是否共振，判断收益波动性风险。 若cokurtosis很高，说明策略在回撤时也容易出现极端收益波动（高风险区域）。池子是g2的simple。选了200个的GLB，corr较低。这个选择我测试了多个地区，感觉也都是成立的。


> [!NOTE] [图片 OCR 识别内容]
> Combo Expression
> Benerate_stats
> alpha
> kurtosis (x.drawdoun,
> returns,
> 215)
> Simulation Settings
> Instrument Type
> Region
> Universe
> LangUage
> Decay
> Delay
> Truncation
> Neutralization
> Pasteuriatjon
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> SLS
> NINVOLINI
> Fast Eipresson
> 003
> Stztistizz
> Verfy



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> OOOK
> BOOOK
> TOOOK
> 08/04'2017
> Equal Weight Pnl:
> 6,552.5OK
> ComboPn
> 6,217,44k
> OOOK
> InyestabilityConstrainedPnl 5,899.07
> 5OOOK
> OOOK
> 30OOK
> 2OOOK
> OOOK
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



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> SharO E
> TUTMCVET
> Ftness
> RETUTS
> UF3UOWn
> Marsin
> 5.55
> 15.8796
> 4.53
> 10.569
> 2.900
> 13.319600


---

### 评论 #35 (作者: YW93864, 时间: 1 year ago)

本周的SAC暂告一小节，share一下我这周在比赛中做的一些工作，可能有启发意义。后文中，我们假设我们筛选和组成的SA是最大化margin的。需要注意的是，本文用到了一些统计手段，所得出来的结论是模型依赖的，意味着有过拟合的风险，我们在最大化margin和过拟合中做权衡，tradeoff。

**1. 首先是selection，要设定一个基础的筛选标准**

```
cond = (in(classifications,"SIMPLE")&&operator_count<=8&&turnover<=0.5&&datacategory_count<=2&&abs(long_count-short_count)<=500&&not(own));
```

**以下是每一行的逻辑：**

1. 第一行代表我在G2
2. 第二行代表我希望operator_count<=8，不希望太长的operator。太长的很容易没逻辑，选到overfitting的alpha概率就提升了
3. 第三行是对turnover的限制，高turnover低turnover都需要有，所以不能限制太低的turnover，不然大部分alpha可能都是fundamental/analyst或者其他更新频率很低的类型；同时我不希望turnover太高，虽然平时的提交标准是70%，但我们可以适当把阈值拉紧一些。
4. datacategory<=2是希望不要混信号
5. abs(long_count-short_count)<=500，是希望alpha的两头在合理的范围内平衡，允许有一点差异
6. not(own)加不加都可以

**2. 通过统计的方法筛选出哪些datacategory的alpha可能本身就很有用。**

具体来说，我对四个region，将每一个datacategory下的alpha提取出来，为了简单起见，我们就先使用1/ turnover在每一类alpha中选出得分最高的1000个（换手率最小的1000个alpha）。具体的代码可以中群里面或者自己F12调试网页找到。

接着，我们做一些统计。一方面观测各个类型的数据集之间，哪一类数据集的margin更高；一方面观测特定类型的数据集中，哪些变量对margin最有影响，比如turnover，operatorCount，universe_size等等。实际上从select这一步能提取出来的alpha也有限，获取到的信息也很少，仅限turnover，operatorCount，long，short四个信息（我在G2，有一些信息比如neutralization，就无法有效使用）。

**首先展示某个region我能拉到的alpha的绩效（很奇怪，api拉出来的和网页端数量不一致，部分差的蛮多，可能是我的程序有bug，但不影响思路）**

**
> [!NOTE] [图片 OCR 识别内容]
> margin
> sharpe
> fitness
> turnover
> operatorCount
> count
> cumCount
> datacategory
> shortinterest
> 1.584
> 0.960
> 0.590
> 5.57
> 4.0
> earnings
> 1.141
> 0.745
> 0.415
> 7.59
> 3.0
> other
> 0.935
> 1.140
> 0.560
> 10.43
> 5.0
> 13
> 22
> risk
> 0.804
> 1.170
> 0.565
> 11.15
> 4.0
> 144
> 166
> neWs
> 0.646
> 1.560
> 0.840
> 11.44
> 3.0
> 15
> 181
> fundamental
> 0.391
> 2.380
> 1.120
> 55.15
> 40
> 230
> 411
> institutions
> 0.340
> 1.020
> 0.420
> 14.72
> 3.0
> 412
> analyst
> 0.311
> 2.090
> 0.850
> 54.29
> 3.0
> 279
> 691
**

假设我们这里拉出来的alpha数量都是正确的。我们想要maximize margin，最简单那我们可以选某个margin以上的类别用来组SA，我们这里假设就选用初analyst以外的alpha。

**接着，我们优中选优，假设我们希望在400个alpha中选200个。一个方法是对这400个alpha用一个大一统的指标去筛选，另一个方法是每一类中，单独选出效果最好的n个alpha组合。**

那我们很容易想到对每一类的alpha做一些统计，寻找什么变量对margin影响最高，对每一类alpha设计一个独特的指标进行筛选。


> [!NOTE] [图片 OCR 识别内容]
> OperatorCount Vs Margin
> Turnover Vs Margin
> AbsCountDiff Vs Margin
> 0.0008
> 0.0008
> 0.0008
> 0.0007
> 0.0007
> 0.0007
> 0.0006
> 0.0006
> 0.0006
> 0.0005
> 0.0005
> 0.0005
> 
> 0.0004
> 
> 0.0004
> 
> 0.0004
> 0.0003
> 0.0003
> 0.0003
> 0.0002
> 0.0002
> 0.0002
> 0.0001
> 0.0001
> 0.0001
> 10
> 20
> 30
> 40
> 0.66
> 0.68
> 0.70
> 0.72
> 0.74
> 0.76
> 0.78
> 0.80
> 0.82
> 500
> 1000
> 1500
> 2000
> 2500
> operatorCount
> turnoVer
> absCountDiff
> OperatorCount Distribution
> TurnoVer Distribution
> AbsCountDiff Distribution
> 700
> 250
> 120
> 600
> 200
> 100
> 500
> 80
> 150
> 400
> 蒿
> 蒿
> 60
> 薏
> 300
> 100
> 40
> 200
> 50
> 20
> 100
> 10
> 20
> 30
> 40
> 0.66
> 0.68
> 0.70
> 0.72
> 0.74
> 0.76
> 0.78
> 0.80
> 0.82
> 500
> 1000
> 1500
> 2000
> 2500
> operatorCount
> trnover
> absCountDif


比如这里就是某个region某个datacategory的分析图。可以发现这里三类指标都和margin有一定线性关系，那我们可以从这三个角度上设计一些独特指标，在每一类alpha中单独打分。 **需要注意的是该分数要能拉开区分度，不同指标之间需要保持量纲差异较小，这样才能做到可比性和筛选性。**

**3. 指标设计**

我们这里就先设计一个大一统的指标。这里给出一个demo，参考群里面老师的思路：怎样选出不是拉大decay降低turnover的alpha，我的思路是1. 高turnover高decay这样的双高alpha肯定要惩罚的；2. 双低的alpha，说明这样的alpha天然就很低turnover；3. 适中的turnover with 适中的decay，这些可以适中的获取。以下是我设计的v1.0函数


> [!NOTE] [图片 OCR 识别内容]
> ATE 30 Surface: T = 0.1,Dcrit = 10,5 =3
> ATE Contour
> 20.0
> 0.90
> 17.5
> 1.0
> 15.0
> 0.75
> 0.8
> 0.8
> 0.6
> 曷
> 12.5
> 0.60
> 0.4
> 1
> 0.6
> @
> 系
> 10.0
> 0.2
> 0.4
> 鲁
> 0.45
> 嵩
> 0.0
> 7.5
> 0.2
> 20.0
> 0.30
> 17.5
> 5.0
> 15.0
> 12.5
> 00
> 10.0,0
> 0.1
> 7.5
> 0.15
> 2.5
> 0.2
> 50
> 0.3
> 2.5
> 0.4
> 0.0
> 0.5
> 00
> 0.00
> 0.0
> 0.1
> 0.2
> 0.3
> 0.4
> 0.5
> Turnover (T)
> Decay
> Tumnover


具体公式是：(1-sigmoid(T/tau))*(1+tanh(D-decay)/s),tau=0.1,D=10,s=3，tau是默认换手率，认为多少的换手率可以作为一个基准值，高了就惩罚，低了就奖励；D是默认decay，逻辑和前面基本一致；s是敏感性系数，是一个可以调的超参数，这个可以控制decay给多少惩罚。最后这个函数值在0-1之间

**后续优化思路：1. 还可以加入operatorCount作为第三个参数去model；2. 这个函数如果是decay和turnover都适中得分最高，应该更优，因为过双低alpha也可能是字段本身带来的，单独的字段更容易导致alpha表现衰减，所以后续加入更多参数应该会得到更好的alpha**

**4. combo**

这里参考 [顾问 KZ79256 (Rank 21)](/hc/en-us/profiles/13609593802263-顾问 KZ79256 (Rank 21)) 大佬的combo，其实是随机森林的思想，把弱学习器集成起来，得到更稳健的效果。


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 06/08/2025 EDT
> anonymous
> Add Alpha to a List
> Code
> o IS Summary
> Period
> IS 
> 05
> Selection Expression
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 6.97
> 4.039
> 7.94
> 16.249
> 2.299
> 80.5796。。
> 10
> ate
> (I-sigmoid
> turnover/0.1) )*(I+tanh ( 10-decay ) /3) ;
> 11
> 12
> data_cond
> in (datacategories, 'option' ) 
> i
> datacategories ,
> insiders' ) |
> i (datacateg
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 12
> 2013
> 8.13
> 4.209
> 8.74
> 14.46%
> 0.449
> 68.86%o。
> 863
> 742
> Combo Expression
> 2014
> 11.99
> 3.83%
> 17.16
> 25.59%
> 0.35%
> 133.739。
> 1336
> 1283
> short
> combo_a(alpha,nlength=6o, mode= 'algo1');
> 2015
> 8.47
> 3.86%
> 10.44
> 18.989
> 0.3896
> 98.459o。
> 1392
> 1334
> 2
> medium
> combo_a(alpha,nlength=120 , mode= ' a1g01');
> 2016
> 9.75
> 3.96%
> 13.41
> 23.639
> 0.599
> 119.37900
> 1340
> 1384
> 3
> COmbo_
> a(alpha,nlength=250 , mode= 'a1g01');
> 2017
> 8.37
> 4.079
> 8.93
> 14.24%
> 0.459
> 70.03%。
> 1494
> 1460
> 5
> signed_power(scale
> short
> +SCale
> medium
> +scale (long) ,0.5)
> 2018
> 8.06
> 3.94%
> 9.69
> 18.059
> 0.88%
> 91.709o。
> 1501
> 1430
> Simulation Settings
> 2019
> 8.61
> 3.799
> 9.99
> 16.839
> 0.41%
> 88.859oo
> 1425
> 1409
> Instrument Type:
> Equity
> Decay:
> 20
> Pasteurization:
> On
> 2020
> 3.15
> 3.899
> 2.51
> 7.94%
> 1.469
> 40.81%o。
> 1358
> 1408
> Region:
> EUR
> NaN Handling:
> On
> Universe:
> TOP2500
> Truncation:
> 0
> Unit Handling:
> Verify
> 2021
> 5.13
> 3.849
> 5.41
> 13.92%
> 0.990
> 72.549oo
> 1431
> 1535
> Language:
> Fast Expression
> Neutralization:
> RAM
> Max Trade:
> On
> 2022
> 1.50
> 4.029
> 87
> 4.19%
> 2.29%
> 20.86%o。
> 1441
> 1467
> 2023
> 6.36
> 3.139
> 6.67
> 13.73%
> 0.40%
> 87.629。
> 1327
> 1443
> Clone Alpha
> Long
> long
> Delay:


---

### 评论 #36 (作者: MZ54236, 时间: 1 year ago)

对于G2，这种抵抗性挑选，算不算过拟合呢。

我的想法是既然别人的alpha看不到，那就参考自己的alpha，找sharpe衰减不严重的alpha，整体pnl没有大drawdown的alpha。

挑选范围可以稍微大一点，包括不同universe，不同中性化。找到这些自己的alpha以后，再用其数据集和相关指标做select筛选条件。

select筛选的时候适当的放大条件，避免反反复复就挑到那么几个。

```
md125 = (not(own) && in(classifications, "SIMPLE") && decay <= 10&& (turnover > 0.03 && turnover < 0.07) && in(datasets,'model25'));risk70 =(not(own)&&in(classifications,"SIMPLE")&& decay <= 15 && (turnover > 0.09 && turnover < 0.21) && in(datasets,'risk70'));analyst4 = (not(own) && in(classifications, "SIMPLE") && decay <= 15&& (turnover > 0.07 && turnover < 0.18) && in(datasets,'analyst4')) ;analyst7 = (not(own) && in(classifications, "SIMPLE") && decay <= 6&& (turnover > 0.08 && turnover < 0.11) && in(datasets,'analyst7'));pv13 =(not(own)&&in(classifications,"SIMPLE")&& decay <= 10 && ( turnover < 0.2) && in(datasets,'pv13'));(md125 + risk70 + analyst4 + analyst7 + pv13)*universe_size(universe)
```

以上就是我挑选的几个数据集例子。

Setting，region我选的是USA，因为EUR只能选到Top1200，表现一般，

唯一需要注意的是 Selection Limit，你需要测试每个data set能获得的alpha数量，然后设置一个大于所选总量alpha的limit，避免一个data就把选择池占满。

其余按照操作RA的方式适当调整即可。

---

### 评论 #37 (作者: 顾问 JR23144 (贺六浑) (Rank 6), 时间: 1 year ago)

这是我提交的第一个可以参加 SA 比赛的alpha
Idea核心思想： **“精粹非基本面 & 极致内部异质性”加权策略** 
本策略首先通过Selection明确排除基本面（Fundamental）类别的Alpha，专注于挖掘其他类型的信号源，并初步筛选出自身相关性较低的Alpha。随后，在Combo阶段，并非采用简单的等权重或基于生产相关性（prod_correlation）的加权，而是通过计算已选Alpha池内部两两收益率的相关性，动态地为那些与池内其他Alpha“最不相似”（即与最相似那个Alpha的相关性也依然较低）的Alpha赋予更高权重，以追求极致的内部异质性和分散效果。

Selection Expression

```
not(in(datacategories, "fundamental")) * (1-self_correlation)
```

明确剔除所有数据类别包含 "fundamental" 的Alpha。这可能是为了避免某些拥挤的基本面因子，或者专注于挖掘市场微观结构、量价、另类数据等其他来源的Alpha。对剩余Alpha进行打分，self_correlation 越低的Alpha得分越高，意味着优先选择那些自身历史表现不那么“内部一致”（可能代表信号更稳定或适应性更强，而非依赖单一短期模式）的Alpha

Combo Expression

```
stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr
```

1. stats = generate_stats(alpha): 获取Selection阶段选出的所有Alpha的详细统计数据。
2. innerCorr = self_corr(stats.returns, 500): 计算这些已选Alpha的日收益率（stats.returns）之间，过去500个交易日的两两相关系数矩阵。
3. ic = if_else(innerCorr == 1.0, nan, innerCorr): 在相关系数矩阵中，每个Alpha自身与自身的相关性为1.0。为了在下一步正确找到与其他Alpha的最大相关性，将这些对角线上的1.0替换为nan (Not a Number)，使其在reduce_max中被忽略。
4. maxCorr = reduce_max(ic): 对于每一个Alpha，在处理过的相关性矩阵（ic）的对应行/列中，找到它与其他所有Alpha收益率相关性的最大值。这个maxCorr代表了该Alpha与它在当前已选池中“最相似的那个伙伴”的相似程度。
5. 1 - maxCorr: 这是最终的权重分配逻辑。一个Alpha的maxCorr值越低（意味着它即便与池中最相似的Alpha相比，其相似度依然不高），那么1 - maxCorr的值就越大，该Alpha获得的权重也就越高。本质上是 **奖励那些在当前组合中最具独特性的Alpha** 。
   
> [!NOTE] [图片 OCR 识别内容]
> Super Simulation
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGIION
> DELAY
> SELECTION HANDUING
> SELECTION LIMIT
> GLB
> Positive
> Combo settings
> UNIVERSE
> NEUTRALIZATION
> MINVOLIM
> Industry
> DECAY
> TRUNCATION
> PASTEURIZATION
> UNIT HANDUING
> 0.01
> On
> Verity
> NAN HANDLING
> TEST PERIOD
> MAXTRADE
> Off
> YEARS
> MONTHS
> Off
> Save as Default
> Apply
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> Turnovel
> Fizness
> Reurns
> AITFLIOIOLI
> Margin
> 5.78
> 15.939
> 6.83
> 22.279
> 3.4796
> 27.969600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 6.01
> 18.3435
> 5,40
> 20.80
> 1.2195
> 22.685220
> 3512
> 3699
> 2014
> 7.66
> 16.2995
> 8,59
> 20,93
> 0.5545
> 25.77520
> 4103
> 3978
> 2015
> 6.29
> 15.8535
> 7.55
> 23,44*
> 493
> 29.57520
> 4269
> 4108
> 2016
> 1.74
> 15.7095
> 5,10
> 13.143
> 3.4795
> 0o
> 4147
> 3937
> 2017
> 5.51
> 15.8595
> 5,53
> 15,5335
> 5545
> 20.855620
> 4309
> 4090
> 2018
> 6.23
> 15.4195
> 7.70
> 23,5545
> 0.933
> 30.58530
> 471
> 4357
> 2019
> 15.4295
> 5,13
> 15,6335
> 0.314
> 21.5752
> 4396
> 4021
> 2020
> 1.64
> 15.7295
> 5.75
> 24.13
> 2.7335
> 30.70520
> 445
> 4202
> 2021
> 1.05
> 16.1795
> 1.12
> 15,7745
> 0.633
> 20.75522
> 4961
> 4536
> 2021
> 7.81
> 15.3295
> 11.05
> 30.7035
> 1.123
> 40.0950
> 5491
> 5208
> 2022
> 612
> 15.4995
> 8.53
> 30,074
> 2014
> 38.8153
> 535
> 4917
> 2023
> -1.35
> 14.8095
> 0.78
> 4,935
> 0.6935
> 655630
> 495_
> 4333



> [!NOTE] [图片 OCR 识别内容]
> Risk neutralized
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdowin
> Margin
> 6.54
> 15.939
> 5.80
> 12.529
> 1.4696
> 15.71%600
> Investability constrained
> Aggregate Data
> Sharpe
> TUrnOVE 
> Fitness
> Returns
> Drawaowin
> Margin
> 5.21
> 14.749
> 6.13
> 20.389
> 4.01%
> 27.669600
> 医 Correlation
> Correlation
> MaimUT
> Mnimum
> Lasz Run: Mon
> 06/09/2025,10.13 AN
> 0.3273
> 0.0384
> Prod Correlation
> MaimUT
> Mnimum
> Lasz Run: Mon
> 06/09/2025,10.13 AN
> 0.6622
> -0.4108
> Self


这种策略旨在构建一个不仅整体表现优异，而且内部各个组成部分之间也高度分散的SuperAlpha。理论上，这能带来更强的鲁棒性，尤其是在市场发生结构性变化或某些共性因子失效时，组合的整体回撤有望得到更好的控制，从而可能实现更高的风险调整后收益.

---

### 评论 #38 (作者: HW93328, 时间: 1 year ago)

在社区投稿了一篇用代码自动回测super alpha的帖子，功能包括随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。希望对各位有帮助。

[Super alpha全自动回测代码--开箱即用！ – WorldQuant BRAIN](../顾问 JX79797 (华子哥/华子) (Rank 9)/[Commented] Super alpha全自动回测代码--开箱即用代码优化.md)

---

### 评论 #39 (作者: XY91783, 时间: 1 year ago)

## **idea：使用datacategories来选取分散的alpha，同时依据dataset的质量进行select分数的加权**

### 类别：Selection

在选取alpha时，我主要考虑的是alpha的分散性，即alpha之间的corr尽可能低。

为了实现这个目的，通过选择不同数据集的alpha来保证alpha的分散性，同时由于不同数据集产生的alpha质量参差不齐，所以在分散性原则的基础上，尽量选择质量好的alpha。

在我的理解中基本面的数据质量最高，所以在分配权重时，按照了下面的原则：

```
Fundamental  > Analyst > News > PV > Model
```

在权重考量时，参考了之前有同学分享的具有 favorite 属性的alpha质量更高，所以加入了这个部分

```
bool = (    in(competitions, "HCAC2025") &&            prod_correlation > 0.1  &&    os_start_date >= "2022-01-01");category_fund = in(datacategories, "fundamental") * 0.5;category_anal = in(datacategories, "analyst") * 0.4;category_news = in(datacategories, "news") * 0.3;category_pv = in(datacategories, "pv") * 0.2;category_model = in(datacategories, "model") * 0.1;weight = (    1        * if_else(favorite, 2, 1));first = bool * weight;first*category_anal + first*category_fund + first*category_news + first*category_model + first*category_pv
```

参数设置

 
> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
> Instrument Tpe
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
> Equi?i
> USA
> TOP3JOO
> Fast Expression
> 3.11
> S-a-5-CaI
> Verify
> Off


参数设置时，要注意Selection Limit的设置，数值太大会导致选取的alpha和selection的代码关联太小（全都选了，就没有select的意义了），数值太小的话可能会导致performance低，我一般选择是在100~200之间，根据能选择的alpha数量上限来调整

performance的表现


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> 31a「0E
> UTICNEI
> IIeS
> T2tUTII
> F3wCINT
> Marein
> 6.84
> 12.5296
> 7.14
> 13.6396
> 1.3696
> 21.799600
> Sharpe
> Turnover
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> 2013
> 0.00
> 0.0090
> 0OD
> 0.0090
> 0.0090
> 0.009
> 231-
> 7.-9
> 12.4755
> 72-
> 11.5935
> 0.4555
> 18.759522
> -35
> 1455
> 2015
> 11.98
> 12.4790
> 1545
> 20.535
> 0.245
> 33-192
> 5
> 1553
> 2315
> 11.-0
> 11.135
> 1445
> 20.095
> 28吃
> 0933
> 530
> 1551
> 2317
> 3.-3
> 11.5255
> 13.2035
> 563
> 22.729522
> 542
> 1551
> 2013
> 6.37
> 13.235
> 57
> 1.7750
> 0.5555
> 15.22932
> 1519
> 603
> 2319
> 3.74
> 14.0755
> 2.70
> 7.335
> 1.2155
> 10.-29
> 543
> 1557
> 2020
> 12.5935
> 12.2355
> 0450
> 19.239
> 552
> 552
> 221
> 7.55
> 11.735
> 15.8990
> 0.52s5
> 25.30922
> 552
> 1535
> 2022
> 1.25
> 12.4535
> 3.57
> 3.3155
> 365
> 14.9-922
> 542
> 1515
> 2023
> 0.54
> 11.4455
> 1.235
> 3530
> 2.15923
> 539
> 1533
> Yoar
> Frass



> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximun
> CTTNIC
> T
> TII:
> Prod Correlation
> Maximur
> Winimup
> Last Run: Wed。06/11/2025。1.53 PM
> 0.4620
> -0.4418
> 10OM
> 
> TOk
> 8
> -0.4.。
> -0.3
> Alphas: 27
> 09
> 09
> 05
> 0^
> 00
> 02
> 09
> ~0
> 0
> 09
> 0?
> 02
> 0?
> 05'
> 03
> ~0.8
> 0.2
> 07
> 0.9
> 0.7
> 0.6.
> ~0.7.
> 0.6 .
> ~0.9.
> 0.8。
> ~0.5


---

### 评论 #40 (作者: WL13229, 时间: 1 year ago)

[XY91783](/hc/en-us/profiles/30270229238807-XY91783)

请注意计算，有时候这样打分只是一厢情愿。如果fundamental的alpha很多，那么就会有很多alpha都有高分，例如有100个fundamental alpha都有高分，那么你的limit低于100，就无法选到其他的categories

---

### 评论 #41 (作者: 顾问 MG88592 (Rank 38), 时间: 1 year ago)

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

### 评论 #42 (作者: XC66172, 时间: 1 year ago)

**Idea:** 我是用代码跑super alpha，首先先通过run selection确认哪些字段会选出不一样的alpha(有些字段例如说author_sharpe在simple alpha就不起作用）,在代码方面写出多种组合。例如对所有SA, **(in(datacategories, "xxx")** 都是有效的，写出不同数量的多种组合 **(in(datacategories, "xxx")||in(datacategories, "xxx").** 同理，其他字段也可以设置不同的阈值，((long_count+short_count)>(universe_size(universe)*xx))

**注意事项：** 因为最终的combination太多，必须要用random来随机跑，按顺序跑就会出来结果都高度雷同的。

**类别：Selection:**

```
not(own) && ((neutralization == "SLOW") || (neutralization == "SLOW_AND_FAST") || (neutralization == "CROWDING") || (neutralization == "STATISTICAL") || (neutralization == "REVERSION_AND_MOMENTUM")) && (1-prod_correlation) && (in(datacategories, "macro")||in(datacategories, "news")||in(datacategories, "sentiment")||in(datacategories, "socialmedia")) && ((long_count+short_count)>(universe_size(universe)*0.8))
```


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Sharpe
>  UTMCVET
> JIMess
> TEUTR
> F3wCINT
> Warain
> 7.33
> 8.359
> 9.26
> 19.9496
> 2.6196
> 47.769600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 10.57
> 5.530
> 13.31
> 21.5-
> 0.51
> 5.725
> 535
> 231-
> 10.11
> 7.9-55
> 13.41
> 21.93*
> 52北
> 5.355
> 563
> 653
> 2015
> 7.536
> 12.79
> 22.81*
> 0.751
> 57.88*0
> 559
> 673
> 2315
> 9.21
> 3.1160
> 12.30
> 2223*
> 0-11
> 5-.375
> 559
> 532
> 2317
> 3.27
> 7.7455
> 9.43
> 1624*
> 0.444
> 41.9750
> 703
> 2013
> 469
> 5.566
> 1.45
> 1127北
> 45*
> 25.454
> 2019
> 7.10
> 3.5755
> 1542*
> 0.574
> 35.5850
> 5GS
> 2020
> 6.33
> 9050
> 26.44*
> 954
> 5.445
> 673
> 201
> 9-5
> 31760
> 13.75
> 25.43*
> 0.751
> 5-.335
> 553
> Gs
> 2022
> 193
> 3.7355
> 5.38
> 17.81*
> 2324
> 40.8250
> 567
> 673
> 2023
> 3.4955
> 5.74
> -22.17*
> 33*
> 52.204
> 556
> 552



> [!NOTE] [图片 OCR 识别内容]
> GLB:
> Universes
> neutralizations
> Selection
> limits
> 657696 pools
> 9207744
> ASI:
> Universes
> neutralizations
> 2 Selection
> limits
> 657696 pools
> 9207744
> USA:
> Universes
> neutralizations
> Selection limits
> 657696 pools
> 0576960
> EUR:
> Universes
> neutralizations
> Selection
> limits
> 657696 pools
> 10523136
> Completed: 10
> Remaining: 35515574


我是四个区混在一起随机跑的，一共需要跑3500万次回测，所以必须要随机跑。如果放在云主机上跑，因为只有两核有时候还会有memory issue,这时候只能降低变体数量从而降低总体回测数。

---

### 评论 #43 (作者: WL13229, 时间: 1 year ago)

[XC66172](/hc/en-us/profiles/28880767093655-XC66172)  这个搜索空间太大了，不太合理

---

### 评论 #44 (作者: XC66172, 时间: 1 year ago)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)

1. 搜索空间确实太大了。原因是这个是初始设置，各个参数累乘，地区再相加的结果；在后面迭代中可以减小搜索空间。例如category combo里我现在是9个类别选四个组合，这样就会有126种组合，再加上其他参数也有多种组合，最终搜索空间会很大。

2.可以通过以下两种方式减小搜索空间：

（a) 回测了一定数量后（例如说500次），可以看一下质量好alphas(sharpe >5 fitness >5)和质量不好alphas的各参数。例如说如果category news没有出现在里面但出现在质量不好的alphas里，那我就把news剔除不再拿来作为参数组合。其他参数同理，可以剔除掉表现不好的neutralizaiton等等。

（b) 质量好的alphas可以使用遗传算法的思维来进行再组合。例如优质alphas A是turnover <0.2 neutralization:SLOW; alphas B是author_sharpe >1.5, neutralization:RAM, 则可以再组合成C:turnover<0.2,neutralization:RAM,D:author_sharpe >1.5,neutralization:SLOW. 看一下表现如何。

---

### 评论 #45 (作者: 顾问 JR23144 (贺六浑) (Rank 6), 时间: 1 year ago)

**在社区投稿了一篇用代码的帖子，功能包括随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。使用 了 MySQL 数据库实现的自动生成super alpha ,并多线程回测super alpha的方案，并且这个方案具备“断点续传”的能力，无惧程序中途宕机** 。

[Super-Alpha-自动生成-多线程自动回测-mysql-版本-无惧程序宕机-断点续传](Super Alpha 自动生成多线程自动回测 mysql 版本 无惧程序宕机断点续传代码优化.md)

---

### 评论 #46 (作者: LH44620, 时间: 1 year ago)

在量化小组沟通，发现sa确实大部分的combo 表现都差于等权。那么在sa比赛中，如果交其他combo的话，表现肯定不如全交等权的，不论是is还是os。那么是不是在比赛中交sa的策略可以调整为：尽量只交prod corr合格的等权sa呢？除非有表现好于等权的combo。那么努力的方向就变成在如何selection上了。

---

### 评论 #47 (作者: CL88457, 时间: 1 year ago)

数据区域ASI

```
selection:
```

not(own)&&

((turnover<0.12&&turnover>0.09)||(turnover<0.15&&turnover>0.13)||(turnover<0.19&&turnover>0.16))

&&(operator_count<8)&&(prod_correlation<0.5&&prod_correlation>0.0)

```
combo:
```

```
stats = generate_stats(alpha);ic = self_corr(stats.returns,20);
```

inneric = if_else(ic==1,nan,ic);

```
ts_rank(-reduce_min(inneric),120)表现图片无法上传：sharp7.01 turnover8.00% fitness9.86 returns24.75% drawdown2.02% margin61.91
```

---

### 评论 #48 (作者: 顾问 QX52484 (Rank 35), 时间: 1 year ago)

```
weight = (    1    *(prod_correlation)    *abs(self_correlation-0.5)    *(1-turnover));bool * weight 各位老师，我想请教一下像这样改变权重是如何影响到选取alpha的？ 是得到一个具体数值，而后在Selection Handling为nan的规则下，数值越高则从因子池中优先选取吗？
```

---

### 评论 #49 (作者: MM27120, 时间: 20 days ago)

以前还不懂selection和comb什么意思，如何选择，读了这篇文章感觉有那么一点明白了

还得继续看看帖子中的大神的经验

------------------------------------------------

---

