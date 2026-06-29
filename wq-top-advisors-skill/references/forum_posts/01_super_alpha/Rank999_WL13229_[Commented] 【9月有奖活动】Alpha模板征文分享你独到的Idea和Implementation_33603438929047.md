# 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！

- **链接**: https://support.worldquantbrain.com[Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **作者**: WL13229
- **发布时间/热度**: 10个月前, 得票: 108

## 帖子正文

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

## 讨论与评论 (73)

### 评论 #1 (作者: WL13229, 时间: 9个月前)

通过质量检查的背包获奖者：

[JB71859](/hc/en-us/profiles/26720563911063-JB71859) ,  [顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97)) ,  [YK49234](/hc/en-us/profiles/29236832485911-YK49234) ,  [CC85858](/hc/en-us/profiles/29142660537879-CC85858) , worldquant brain赛博游戏王,  [GZ81958](/hc/en-us/profiles/28845596009751-GZ81958) , XX25820,  [AL13375](/hc/en-us/profiles/27647035974807-AL13375) ,  [XC66172](/hc/en-us/profiles/28880767093655-XC66172) ,  [KD86036](/hc/en-us/profiles/27031622119831-KD86036) ,  [LM81527](/hc/en-us/profiles/27707767300503-LM81527) ,  [SQ15289](/hc/en-us/profiles/28969190745367-SQ15289) ,  [YH82809](/hc/en-us/profiles/30611282193687-YH82809) ,  [顾问 QX52484 (Rank 35)](/hc/en-us/profiles/28901412334615-顾问 QX52484 (Rank 35)) ,  [JB53978](/hc/en-us/profiles/30875128290711-JB53978) ,  [AK76468](/hc/en-us/profiles/28846915371031-AK76468) ,  [AM12075](/hc/en-us/profiles/30421958512663-AM12075) ,  [SG46247](/hc/en-us/profiles/29144016357527-SG46247) ,  [PX70901](/hc/en-us/profiles/30498915469847-PX70901) ,  [JG21054](/hc/en-us/profiles/29027000582551-JG21054) ,  [TJ14150](/hc/en-us/profiles/28969921835159-TJ14150) ,  [顾问 SC23342 (Rank 23)](/hc/en-us/profiles/29679605251735-顾问 SC23342 (Rank 23)) ,  [BA51127](/hc/en-us/profiles/8958551180311-BA51127) ,  [ML42552](/hc/en-us/profiles/27182530443671-ML42552)

优胜奖获得者：

顾问 JR23144 (贺六浑) (Rank 6), LH44620,  [YZ70114](/hc/en-us/profiles/26918538763927-YZ70114) ,  [LL49894](/hc/en-us/profiles/30413446999703-LL49894) ,  [JL98779](/hc/en-us/profiles/31205672631319-JL98779) ,  [LR93609](/hc/en-us/profiles/30244554462231-LR93609)

示例：

模板

```
iv_difference = <option_call/> - <option_put/>;std_group = bucket(rank(historical_volatility_120), range="0.1,1,0.1");decorrelator = 1 / (1 + abs(ts_delta(iv_difference, 5)));<group_compareOP/>(iv_difference, std_group)  * decorrelator
```

- 模板中的变量使用 **< />** 进行了声明，总共三个变量。
- 具体变量1：<option_call/>: 可以包含所有和call有关的期权字段
- 具体变量2：<option_put/>: 可以包含所有和call有关的期权字段
- 具体变量3：<group_compareOP/>: 可以对组间进行计算的分组运算符，例如group_rank, group_zscore, group_neutralize等

- 搜索空间的大小：以数据集option4为例的话，大约是230*230*9
- 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：<group_compareOP/>(iv_difference, std_group) * decorrelator：对iv_difference在std_group内做分组运算（如group_rank），再乘以decorrelator，得到最终信号。其中，std_group = bucket(rank(historical_volatility_120), range="0.1,1,0.1")：对历史波动率分rank后分桶，形成分组标签。decorrelator = 1 / (1 + abs(ts_delta(iv_difference, 5)))：用5期的iv_difference变化幅度做装饰，降低信号自相关性。
- 产出效果：我尝试了X次回测，有20个可以提交的Alpha.
- 建议其他顾问未来尝试的探索方向: 在不同市场、不同品种（如ETF期权、商品期权）上做迁移和泛化测试。

如您无意参赛，也欢迎留言参与讨论：

随手分享一个来自热心顾问的小小数据探索模板，他说这个称不上完整，但是很适合探索新数据。且不参与征文，故对格式就不严格要求了。👇代发内容如下

> zscore(ts_delta(rank(ts_zscore(datafield,60)),5))

上文中的模板op可以进行替换，时间参数也应该针对不同数据集进行合理替换.

---

### 评论 #2 (作者: JB71859, 时间: 11个月前)

**Alpha模板Name：《多重平滑排名信号》**

模板

ranked_signal = ts_rank( **<Earnings_data_field/>** ,  **<decay_1/>** );

**<ts_statistical/>** (ranked_signal,  **<decay_2/>** )

具体变量1：<Earnings_data_field/>: 可以包含所有EARNINGS的数据字段进行遍历
具体变量2：<decay_1/>: 第一层平滑ts_rank的decay可以是5，10，20，60，120
具体变量3：<decay_2/>: 第二层平滑ts_mean的decay可以是5，10，20，60，120

具体变量4：<ts_statistical/>: 尝试了ts_mean, 但是觉得还有很多可以尝试，例如median，sum, max, last change

搜索空间的大小：以数据集earnings2为例的话，大约是12 * 5 * 5

模板的idea，implement细节：ts_mean(ts_rank(<Earnings_data_field/>, <decay_1/>), <decay_2/>)：首先ts_rank(<Earnings_data_field/>,<decay_1/>) 对原始EARNINGS数据进行时间序列排名（第一重平滑），将绝对数值转换为相对排名，消除量纲影响；然后ts_mean(ranked_signal, <decay_2/>) 对排名序列进行时间窗口均值平滑（第二重平滑），进一步降低信号噪声，确保输出稳定的Alpha信号。

产出效果：我在尝试了2个数据集大概2000次的回测后，点亮了USA中earnings的塔，通过该模板提交了3个Atom的Alpha。
该模板还未在EUR、ASI和GLB中运行，存在一定的潜力.第一步的ts_rank其实也可以抽象成其他的ts相关的运算符。感觉这个模板适合一些已经处理好的数据，因为如果数据不处理的话，第一步得到的东西会很抽象且不好用。建议大家在放入第一步前处理一下数据。

也可以跟其他处理数据的模板结合在一起使用。

---

### 评论 #3 (作者: 顾问 WL27618 (Rank 97), 时间: 11个月前)

**模板**

```
<exceed op/>(<Arithmetic op/>(<option_call/>) , <Arithmetic op/>(<option_put/>))
```

- 模板中的变量使用 **< />** 进行了声明，总共4个变量。
- 具体变量1：<option_call/>: 可以包含所有和call有关的期权字段
- 具体变量2：<option_put/>: 可以包含所有和call有关的期权字段
- 具体变量3：< **Arithmetic op** />: 任何eltwise的变换operator(比如-1/x, log, signed_power, s_log_1p, tanh, arc_tan)等
- 具体变量4：< **exceed op** />: 任何表示前一个超出后一个的运算.(比如"({data1})/({data2})", "({data1}-({data2}))", "({data1}-({data2}))/({data2})",            # 相对变化率, data1, data2是正数的变量时使用 "({data1}-{data2})/({data1}/2+{data2}/2), ({data1}-{data2})/ts_std_dev({data2},252)”)等,

- 搜索空间的大小：option8, option4 , pair个数 x arithmetic op个数 x 外面套的1,2,3阶运算符的个数
- 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：  **Arithmetic op的目的** 就是想尽量扩大搜索范围, call,put分别套了arithmetic op 后correlation下降不少, 有些信号看着还挺好
- 产出效果： 可能option4数据集信号就是比较强, 随便跑都有很多产出
- 建议其他顾问未来尝试的探索方向: AI我尝试过不同希腊字母, 比如theta vega 配对, 但是效果一般, 感觉还是应该尝试不同的希腊字母组合.
  
> [!NOTE] [图片 OCR 识别内容]
> opt
> All Status
> Region
> Delay
> Days Before
> Min Turnov:
> Max Turnov
> Min Margin
> 计算 Correl
> Min Return
> Regio
> Shar
> Fitne
> Retur
> Turnov
> Margi
> Sub-U
> Date
> Statu
> Regular
> I0
> Score
> Message
> Pnl
> pe
> SS
> ns
> er
> Sharpe
> Created
> ts_std_dev((opt4_ 182_put_pre_delta3O)/(opt4_ 18..JrMYXgI
> USA
> 26.719309203370738-1.04
> -0.8
> -7.42%
> 7.37%
> -20.12%00-0.54
> 2025-07-14
> FAIL LOW_SHARPE,LOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_547_call_vola_delta45-(opt4_547
> OgQqkOd USA
> 82.17038037547896
> 1.51
> 1.53
> 12.91 %
> 8.40%
> 30.74%o。 0.77
> 2025-07-14
> FAIL
> LOW_SHARPE MATCHES_THEMES
> 查看
> ts_av_diff((opt4_273_put_vola_delta25)/(opt4_27
> j0zlpz0
> USA
> 28.80059299117893
> -1.17
> -0.61
> -4.69%
> 17.08%
> -5.50%o。
> 1.01
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_ 122_put_vola_delta45)/(opt4_122_
> 05OkZbq
> USA
> 28.79967050699429
> -2.03
> -2.1
> -13.32%7.39%
> -36.07%。-1.13
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> (opt4_122_put_vola_delta5O-opt4_ 122_call_vola
> 8XSgXPV
> USA
> 28.85978993222753
> 1.65
> -1.27
> -11.47%19.27%
> -11.90%o0-0.84
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_30_put_vola_delta5O-opt4_30_cal.. 9Lk7329
> USA
> 22.16807467527147
> -1.2
> -1.03
> -9.20%
> 6.60%
> -27.88%00-0.78
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESS,LOW_SUB_UNIVERS
> 查看
> ts_delay((opt4_ 182_put_vola_delta45)/(opt4_182
> bAG7NqZ USA
> 28.861353313495975-2.03
> -1.68
> -12.13%17.69%
> -13.72%00-1.13
> 2025-07-14
> FAIL
> LOW_SHARPE LOW_FITNESSLOW_SUB_UNIVERS_
> 查看
> ts
> mean((opt23_super_OP_trans_iv_ra_iV_call-opt.. VelnnJy
> USA
> 84.37926278033673
> 1.39
> 0.98
> 6.23%
> 5.51%
> 22.61%o。 0.79
> 2025-07-14
> FAIL
> LOW_SHARPE,LOW_FITNESS,MATCHES_THEMES
> 查看
> ts_delta((opt4_30_put_vola_delta2O)/(opt4_30_
> Ca.WWKGmedUSA
> 28.407897015951416-1.2
> -0.53
> -3.83%
> 19.87%
> -3.869o。
> -1.23
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_delta((opt4_730_put_vola_delta45)/(opt4_730
> XMmEVR1 USA
> 29.21246681753198
> -1.07
> -0.52
> -4.83%
> 20.35%
> -4.74%oo
> -0.73
> 2025-07-14
> FAIL LOW_SHARPE LOW_FITNESS,LOW_SUB_UNIVERS_
> 查看
> ts_delta((opt4_ 182_put_Vola_delta5o)l(opt4_ 182
> JrMLX7A
> USA
> 28.59394501691516
> -1.03
> -0.51
> -5.31%
> 21.81%
> -4.879o。
> -0.9
> 2025-07-14
> FAIL
> LOW_SHARPE,LOW_FITNESS,LOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_GO_call_vola_delta45-opt4_GO_pU.. dvkwnxk
> USA
> 82.50928760533199
> 1.66
> 1.46
> 9.64%
> 6.28%
> 30.71%。
> 2025-07-14
> FAIL
> MATCHES_THEMES
> 查看
> ts_mean((opt4_1
> call_Vola_delta8o-(opt4_152
> qVgZvno
> USA
> 80.35573223118207
> 1.45
> 1.54
> 14.14%
> 9.00%
> 31.42%。0.77
> 2025-07-14
> FAIL
> LOW_SHARPEMATCHES_THEMES
> 查看
> ts_mean((opt4_GO_call_vola_delta5O-opt4_GO_pU.. qV9ZrSv
> USA
> 75.91622868322459
> 1.33
> 1.23
> 10.69%
> 7.02%
> 30.46%o。 0.79
> 2025-07-14
> FAIL
> LOW_SHARPEMATCHES_THEMES
> 查看
> ts_std_dev((opt4_call_vega_ 122d-opt4_put_vega... 691JY0o
> USA
> 27.945397048192213-1.13
> -0.82
> -6.52%
> 5.80%
> -22.49%o0-0.76
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> (opt23_photo_trans_iv_iv_call)/(opt23_photo_tran... |1pbpjn
> USA
> 83.31975278601249
> 1.44
> 0.51
> 6.84%
> 54.42%
> 2.52%。
> 0.87
> 2025-07-14
> FAIL
> LOW_SHARPE LOW_FITNESS,MATCHES_THEMES
> 查看
> 52_C


---

### 评论 #4 (作者: YK49234, 时间: 11个月前)

**动量分歧因子**

模版：

```
<ts_delta/ts_mean>(ts_zscore(<feild/>,<window day1/>),<window day1/>)-<ts_delta/ts_mean>(ts_zscore(<feild/>,<window day2/>),<window day2/>)
```

**具体变量1** : **<ts_delta/ts_mean>** 表示俩个操作符二选一

**具体变量2** : **<feild/>** 表示数据字段，前后俩个 **<feild/>** 相同，表示同一个数据字段，模版对 **<feild/>** 数据字段类型适配度比较广泛，没有太大限制

**具体变量3** : **<window day1/>** &  **<window day2/>** 俩个不同的时间窗口 俩个窗口的比例要尽量大 例如 **<window day1>** = 100 ; **<window day2/>**  = 400

**搜素空间大小** ：以 **pv13**  matrix ，短期+长期窗口 【5，10，20】、【200，300，400】 为例 28*2*3*3

**模版的idea** ：捕捉同一个数据字段 短期与长期动量的分歧  并保证模版普适性

产出效果：以1sharp、0.6fitness为“有信号“阈值：   **fundamental** （asi minvol1m）出信号率约4%

**pv** （asi minvol1m）出信号率约6%   20000次回测我最后选择并提交了4个alpha

建议其他顾问未来尝试的探索方向: 此模版适配性较强，还可以尝试用组合数据字段进行回测

---

### 评论 #5 (作者: WL13229, 时间: 11个月前)

[YK49234](/hc/en-us/profiles/29236832485911-YK49234)  对field的描述请详细些，补充一下，这两个field有没有什么约束条件

---

### 评论 #6 (作者: 顾问 JR23144 (贺六浑) (Rank 6), 时间: 11个月前)

### 基于oth455 网络因子差值动量模板

**模板**

<ts_operator_op/> ( <oth455_xxxx_fact1_value/> <math_op/> <oth455_xxxx_fact2_value/>,<days_op/>)

**1. 模板中的变量使用< />进行了声明，总共五个变量。**

**具体变量1：<ts_operator_op/> 可以是** ts_rank, ts_zscore, ts_delta, ts_sum, ts_delay, ts_std_dev, ts_mean, ts_arg_min, ts_arg_max, ts_scale, ts_quantile  等

**具体变量2：<oth455_xxxx_fact1_value/> 可以是** oth455_relation_roam_w3_pca_fact1_value, oth455_relation_roam_w4_pca_fact1_value, oth455_relation_roam_w5_pca_fact1_value, oth455_partner_roam_w5_pca_fact1_value 等

**具体变量3：<math_op/> 可以是** + ，-，* , / 等

**具体变量4：<oth455_xxxx_fact2_value/> 可以是** oth455_relation_roam_w3_pca_fact2_value, oth455_relation_roam_w4_pca_fact2_value, oth455_relation_roam_w5_pca_fact2_value, oth455_partner_roam_w5_pca_fact2_value 等

**具体变量5：<days_op/> 可以是** 20,60,120,240 等

**2. 搜索空间的大小**

以oth455数据集为例，因子配对（如fact1-fact2, fact1- fact3, fact2-fact3,fact1* fact2）有3种核心组合。数据集本身有约11 **(时间序列算子）**  * 4 **(数学运算)**  * 300 ****(基础设定)****  = 13,200 种不同的“关系-算法-窗口”基础设定 。 数据量非常大，有巨大的挖掘潜力 。

**3. 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）**

- **Idea** : oth455的PCA因子（fact1, fact2, fact3）捕捉了公司在关系网络中不同层面的特征。fact1通常代表“主流/规模”特征，而fact2、fact3代表更“小众/特色”的特征。本模板的核心思想是，通过计算不同因子间的 **差值或比率** ，来寻找网络地位**“失衡” **的公司，例如那些“主流地位”不强但“特色地位”突出的“隐形冠军”。然后，通过时间序列算子捕捉这种“失衡”特征的** 持续性或变化动量**。
- **Implement细节** :
  - **<oth455_xxxx_fact1_value/> <math_op/> <oth455_xxxx_fact2_value/>;**   这是 **数据处理** 步骤。它将两个独立的网络因子合成为一个具有更清晰经济学意义的“差值”信号。
  - **<ts_operator_op/>(factor_difference, <days_op/>)**  这是 **主信号生成** 步骤。它作用于处理后的“差值”信号，将其转化为一个捕捉长期累积效应（如ts_sum）或短期变化趋势（如ts_delta）的最终Alpha。

**4. 产出效果**

EUR 市场中 Other模块 **乘数** 是 **最高** 的，不过也是能找到很多alpha的。给大家展示一个提交了的alpha，使用 ts_sum(oth455_xxxx_fact2_value - oth455_xxxx_fact1_value, 240) 这个具体表达式，从附图的回测结果看，虽然Fitness为0.6，还有提升空间，但其有0.07 的margin 并且operator 少，还有Risk neutralized 也是紧贴着的所以我交了。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_SUm(oth455
> factz_Value
> oth455
> factI
> Value
> 240)
> 眈 Single Data Ser Mlpha
> M Power Pool Alpha
> Pyramid theme: EURIDIIOTHER Y.7
> Aggregate Data
> SArCe
> LUTCIe
> TIIe
> ReUTI
> LTaIOO
> NIreIr
> Simulation Settings
> 1.01
> 1.15%
> 0.60
> 4.42%
> 4.49%
> 76.7
> 900
> Instrument Type
> Region
> Unlerse
> Langwage
> Decay
> Delay
> Trncation
> Neutraliation
> Pastewriation
> NaN Handling
> Unt Handling
> TaTrade
> Equity
> EUR
> TCF2507
> ExprEssion
> D.JE
> Subindustry
> Werf
> Vear
> Sharpe
> Tumower
> Ftness
> Rehrs
> Dowdown
> Long Count
> Shrt Count
> 2013
> .353
> 357
> 201沾
> 5E.39
> 30
> 13JE
> 2014
> D.Js
> 1.173
> 0.02
> .41
> 2.84沾
> 7.549
> T1
> Clone Alpha
> 2015
> 0.35
> 633
> 0.4
> 153
> 4.00
> 131.3
> ZOIE
> 0.21
> 0.7096
> OOE
> D.S5
> 4.4s汩
> 2.1293
> 1732
> 2017
> 1.72
> 0.7595
> 1.13
> 508
> 1.734
> So
> 1316
> 1135
> N Chart
> PIL
> 2018
> .973
> 0.07
> 3.57
> 4.05沾
> 12.704
> 1306
> 112E
> 2015
> 187
> DZE
> {3:
> 2.08沾
> -.-32
> 1715
> 1115
> 2020
> 0.3
> 059
> O.EE
> SED
> 3.34沾
> T
> 15_
> 1033
> 2021
> 333
> DE
> 53:
> 2.5汩
> 0193
> 13E
> 1571
> 03JK
> 2022
> 35
> 2.7
> 10.39
> e汩
> 151.37
> 112
> 1777
> 2,00OK
> 2023
> .773
> 15.52
> 0.60治
> 413.59
> 1172
> 1535
> 03JK
> Risk neutralized
> Aggregate Data
> SrDe
> LUTOET
> CTS
> RUUTS
> CaOC
> Ir3IT
> 1.05
> 1.159
> 0.50
> 2.88%
> 3.209
> 49.909600
> J37"14
> Jan'15
> Jan'16
> Jan '17
> Jan'18
> Jan '19
> Jan '20
> Jan '21
> J30'22
> J3n'23
> Wrgin


**5. 建议其他顾问未来尝试的探索方向**

1. **系统性挖掘** : 全面遍历我上面提到的 <ts_operator_op/> ， <oth455_xxxx_fact1_value/> ，<math_op/> ，<oth455_xxxx_fact2_value/>，<days_op/>的组合，大概率能发现比我这个ts_sum版本表现更优的Alpha。
2. **构建二阶Alpha 三阶Alpha** : 这个模板产出的信号还是有的，非常适合作为**“基石”或“风控”因子**。可以该模板去套培训用的二阶三阶模版，相信也是会有更好表现的。
3. **跨关系比较** : 我模板中比较的是同一关系内的fact1和fact2。一个更有趣的方向是进行 **跨关系比较** ，例如 customer_fact1 - competitor_fact1，这可以构建一个衡量公司“网络护城河”的强大信号。

---

### 评论 #7 (作者: CC85858, 时间: 11个月前)

模板：

```
signed_power(normalize(ts_backfill(trade_when(pcr_oi_<days1/>>1, implied_volatility_call_<days2/>-implied_volatility_put_<days3/>, -1),5)), 2)
```

模板中的变量使用< />进行了声明，总共三个变量。
• 具体变量1：<days1/>: 10、20、30、60、90、120、150、180、270、360、720、1080
• 具体变量2：<days2/>: 10、20、30、60、90、120、150、180、270、360、720、1080
• 具体变量3：<days3/>: 10、20、30、60、90、120、150、180、270、360、720、1080
• 搜索空间的大小：使用option8，option9大约是12*12*12
• 模板的idea，implement细节：捕捉短期看跌情绪pcr_oi_<days1/>>1的极端变化，通过数据平滑和信号增强，生成衡量市场恐慌/贪婪强度的方向性指标。
比如说当20天期权出现看跌情绪主导时，对比6个月看涨期权与1年看跌期权的隐含波动率差异，他的极端值反映了投资者对中期风险与长期保护的定价分歧，再通过标准化normalize和非线性放大signed_power后提取显著的交易信号。

signed_power(normalize(ts_backfill(trade_when(pcr_oi_<days1/>>1, implied_volatility_call_<days2/>-implied_volatility_put_<days3/>, -1),5)), 2)：首先通过条件触发（当PCR_OI大于1时）计算隐含波动率差，然后对无效值回填，再标准化，最后取符号保留的平方得到最终信号。其中，trade_when(pcr_oi_180>1, iv_diff, -1)：当days天期权成交量的看跌看涨比大于1时，取隐含波动率差（call IV - put IV），否则置为-1；ts_backfill(series,5)：用最近5期内的有效值向前填充无效值；normalize(series)：将序列标准化；signed_power(x,2)：计算sign(x)*x^2，以保留方向并增强信号强度。
• 产出效果：我尝试了一万次回测，有15个可以提交的优质Alpha（sharp超过2，fitness超过3，return超过40%的alpha也不在少数）.
• 建议其他顾问未来尝试的探索方向: 在不同的universal（比如top3000、ILLIQUID_MINVOL1M）以及不同的操作符（比如去除ts_backfill，改为

group_neutralize（x，industry），或者将sign_power改为

ts_decay_linear（x,5))。trade_when中的条件也可尝试

volume >ts_mean(volume, 60)*2，

ts_regression(returns, ts_step(5), 20, lag = 0, rettype = 2) > 0，

rank(rp_css_business) > 0.8，option9中其他比率型的数据字段以及

使用三阶模板中的一些条件也都有不错的表现。

**而且特别重要的一点，这个模板跑出的alpha符合ppac，这意味着如果不看重生产相关性的话每个人都可以交**

） 
> [!NOTE] [图片 OCR 识别内容]
> Code
> signed_power (normalize (ts_
> backfill
> trade_When
> Pcr_
> 1,implied_volatility_ca:
> implied_volatility_Pl
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
> USA
> TOP3000
> Fast Expression
> 22
> 0.04
> Sector
> On
> On
> Verify
> Off
> Clone Alpha
> N
> Chart
> Pnl
> 2SM
> ZOM
  
> [!NOTE] [图片 OCR 识别内容]
> 0
> IS Summary
> Period
> IS
> 05
> Power Pool Alpha
> Pyramid theme: USAIDIIOPTION X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.03
> 9.21 %
> 3.25
> 32.129
> 16.63%
> 69.749600
> Year
> Sharpe
> TUrnOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.29
> 12.23%
> 1.34
> 13.44%
> 9.09%6
> 21.989600
> 1507
> 730
> 2014
> 4.95
> 9.52%
> 9.01
> 41.39%
> 3.4496
> 87.009600
> 1813
> 783
> 2015
> 3.75
> 10.2796
> 6.86
> 41.87%
> 4.26%6
> 81.569600
> 1843
> 779
> 2016
> 0.09
> 9.5290
> -0.03
> -1.039
> 16.63%
> 59600
> 1862
> 783
> 2017
> 0.61
> 9.1396
> 0.45
> 6.949
> 7.9196
> 15.219600
> 1896
> 775
> 2018
> 1.91
> 8.81%
> 3.45
> 40.72%
> 11.50%
> 92.469600
> 1797
> 880
> 2019
> 0.76
> 8.90%
> 0.71
> 10.90%
> 10.8396
> 24.489600
> 1716
> 969
> 2020
> 2.16
> 8.7996
> 3.99
> 42.72%
> 5.91%
> 97.189600
> 1578
> 1091
> 2021
> 2.95
> 5.8096
> 6.11
> 53,66%
> 11.3096
> 157.809600
> 1932
> 872
> 2022
> 3.36
> 8.2596
> 8.39
> 77.86%
> 11.5496
> 188.659600
> 2475
> 453
> 2023
> 8.94
> 9.4896
> 26.26
> 107.85%
> 7.02%6
> 227.529600
> 2316
> 36
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 9.21 %
> 2.54
> 23.84%
> 13.78%
> 51.759600


---

### 评论 #8 (作者: worldquant brain赛博游戏王, 时间: 11个月前)

波动率分歧因子（适用于rsk数据 类型）

模版：

```
<group_op>(power(<ts_op>(abs(<data>),<day1>),2)-power(<ts_op>(<data>,<day1>),2),<group>)
```

**具体变量：**

<group_op>：'group_neutralize','group_zscore','group_rank','group_normalize'

<ts_op>：'ts_std_dev','ts_rank','ts_sum','ts_zscore'

<data>：与风险有关的数据集 字段 ，例如rsk70

<day1>：常见的时间窗口 ，5,20,120,252均可，模版中默认是5

<group>：中性化组，模版中默认使用四个基础的中性化组

**搜索空间大小：** 按照默认参数，单个字段搜索空间为4*4*4*1=64个因子=7个槽

**产出效果：** 实验在usa地区按照使用人数倒序选取前100个rsk类型数据，目前跑了2234个因子，按照sharpe1和fit0.6进行筛选，得到114个因子，产出率为5%

**模版的idea：** 衡量过去 `<day1>` 天内数据的波动幅度与趋势的偏离程度，可以用来衡量风险的稳定性或者风险的突变。

**探索方向：**

- 在其他类型数据中实验模版
- abs(data)=data的问题，weijie老师给出的建议是把abs的处理方式换成在数轴上的分布，从而按照分布进行处理，初步的想法是按照ts_mean作为分布中心点，以if_else的方式代替abs处理，可以基于此进一步优化模版

---

### 评论 #9 (作者: WL13229, 时间: 11个月前)

[顾问 JR23144 (贺六浑) (Rank 6)](/hc/en-us/profiles/28844048981143-顾问 JR23144 (贺六浑) (Rank 6))

很漂亮

---

### 评论 #10 (作者: WL13229, 时间: 11个月前)

[YL41226](/hc/en-us/profiles/32915413080983-YL41226)

请不要拿AI生成的东西不经思索就上传，对参数、字段约束、模板效果的描述没有提供有效细节（如截图），请参考前人优秀作品进行彻底修改，您的旧评论将在今日被删除。

同时，您历史发布的所有帖子与评论将会在本日进行人工审核，疑似AI的帖子或评论都将被删除，社区分数亦会被相应降低。

---

### 评论 #11 (作者: WL13229, 时间: 11个月前)

[CC85858](/hc/en-us/profiles/29142660537879-CC85858)

感谢分享。建议继续补充一些关于模板拓展性的内容或者关于trade_when条件的讨论，使其可以拓展到更多类似数据集。

---

### 评论 #12 (作者: XX25820, 时间: 11个月前)

模板

```
(<field1/> - ts_mean(<field1/>, <day/>)) / ts_mean(<field1/>, <day/>)
```

- 模板中的变量使用 **< />** 进行了声明，总共2个变量。
- 具体变量1：<field1/>: 是任何连贯的数据字段，要求是一定要数据丰富，数据连贯，每天都有数据的是最好的。
- 具体变量2：<day/>: 看你要考察当前因子Field值与多长时间范围的平均值的偏离程度。可以是20一个月，也可以是252一年，all OK。

- 搜索空间的大小：以数据集analyst69为例的话，大约是226 * 4 = 904
- 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：

#### **1. 数据处理阶段**

- **输入字段准备** ：
  - 确保  `<field1/>`  是一个连贯且数据丰富的字段，且每天都有数据。
  - 确保  `<day/>`  是一个合理的时间窗口（如20天、252天等），根据分析需求选择适当的时间跨度。
- **时间序列均值计算** ：
  - 对  `<field1/>`  进行滚动窗口计算，计算过去  `<day/>`  天的均值  `ts_mean(<field1/>, <day/>)` 。
  - 滚动均值的计算是数据处理的核心步骤，确保均值计算的窗口长度与  `<day/>`  一致。

#### **2. 主信号生成阶段**

- **偏离程度计算** ：
  - 计算  `<field1/>`  当前值与其滚动均值的偏离程度
  - 该公式的分子部分捕捉了当前值与历史均值的差异，分母部分通过标准化消除量纲影响，使得信号具有可比性。
- **信号输出** ：
  - 生成的信号是一个标准化的偏离值，范围通常在正负区间内（例如，正值表示当前值高于均值，负值表示当前值低于均值）。
  - 一般而言，这个是一个反转因子，所以在最后要加上一个 **负号！！！**

- 产出效果：我尝试了900次回测，有28个可以提交的Alpha.
- 建议其他顾问未来尝试的探索方向: 任何数据集全都可以产出，这是一个通用模板。


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> SIZC
> Of 60
> Sharpe:
> Fitness:
> 0.5
> Turnover:
> Name: Bias
> Filter
> Select Columns
> Name
> Type
> Status
> Date Created (EST)
> Region
> Unjverse
> Delay
> Sharpe
> Returns
> Turnover
> Drawdown
> Margin
> Fitness
> Tag
> Long Count
> Short Count
> Bizs
> Selec
> Selec
> Searcn
> Selec
> Selec
> Selec
> e.6> 1
> 470
> e.6> 1
> e.6> 1
> ~0.5
> Selec
> Cg
> Cg
> plus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 2.20
> 7.2435
> 12.5535
> 3.6735
> 11.555
> 1.67
> Dias;
> 763
> 776
> Bias_plus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 2.18
> 7.2735
> 12.833
> 3.703
> 11.336
> bias;
> 772
> Bias_plus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 2.17
> 6.923
> 11.3735
> 3.703
> 12.186
> 843
> Bias_plus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 2.14
> 7.133
> 11.483
> 3.723
> 12.42
> bias;
> 765
> 774
> Bias_plus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 2.13
> 5.863
> 10.7035
> 3.8535
> 10.96:
> Dias;
> 792
> 746
> Bias_plus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 6.9735
> 10.4435
> 3.81
> 13.36
> Dias;
> 762
> 776
> Bias
> Regular
> UNSUBMITTED
> 07/17/2025 EDT 
> EUR
> T0P2500
> 2.06
> 6.8635
> 10.303
> 3.863
> 13.33
> bias;
> 763
> 776
> Bias_Dlus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT
> EUR
> TOP2SOD
> 2.05
> .6593
> 13.5535
> 4.9235
> 9.81
> Dizs;
> 765
> 774
> Bias_Dlus
> Regular
> UNSUBMITTED
> 07/17/2025 EDT
> EUR
> TOP2500
> 2.01
> 4.81
> 12.383
> 2.9435
> 7.47:
> Dizs;
> 788
> 751
> Page
> Bias
> blas。


---

### 评论 #13 (作者: LH44620, 时间: 11个月前)

```
signal = <dataprocess_op/>(-group_backfill(vec_max(<nws77/>),country,60, std = 4.0));ts_decay_linear(<ts_Statistical_op/>(signal, 90),5, dense = false)
```

- 模板中的变量使用 **< />** 进行了声明，总共三个变量。
- 具体变量1：<nws77/>: EUR region TOP2500 universe, DataSet ID： **nws77** . DataFields Type: Vector.
- 具体变量2：<dataprocess_op/>: quantile(x)、winsorize(x)等，对 **数据进行整理** 的函数。
- 具体变量3：<ts_Statistical_op/>: ts_ir(x,days) 、ts_zscore(x,days)、ts_entropy(x,days)等，计算信号 **复合统计指标** 的函数。
- 注：ts_decay_linear也可以替换成jump_decay和ts_decay_exp_window(x, d, factor = f)这些 **Time Series: Decay, Smoothing, and Turnover Control (时间序列：衰减、平滑和周转控制)** 的函数 **。** 因为这些函数的参数数量不一致，为了简洁，该模板就写死了ts_decay_linear。

- 搜索空间的大小：以数据集 **nws77** 为例的话，大约是29*2*3=179个。 **nws77** 有29个数据字段。
- nws77数据特征分析： 
> [!NOTE] [图片 OCR 识别内容]
> 11:
> SeI
> model field dfi"E00000000000075547"
> Ser.index
> pd
> to datetime (ser.Index)
> Valid
> eVent
> SC1
> notna( )
> chg
> eVent
> SCI
> ne (ser.shift() )&
> S2「.notna
> eVent
> Chg
> event
> cnt_year
> event
> groupby (event . index. year)
> SUII( )
> label
> pd
> CUt (cnt
> year
> bins
> 1,4,53/2,53,365/2,365*2]
> labels
> annual"
> quarterly"
> PWeekly
> "daily" ,"intra-day"] )
> print (pd
> DataFrane ([
> Count
> Cnt
> Vear
> freq
> label]) )
> Count
> freq
> 2013
> annual
> 2014
> annual
> 2015
> annual
> 2016
> annual
> 2017
> ahnUal
> 2018
> quarterly
> 2019
> 11
> quarterly
> 2020
> quarterly
> 2021
> annual
> 2022
> annual
> 2023
> annual
  
> [!NOTE] [图片 OCR 识别内容]
> Visualizations . plot
> non
> 几3
> Counts (model field df)
> Non-NaN and Non-Zero Count
> Counts
> Non NaN Count
> Non-NaN and Non-Zero Count
> 800
> 600
> 
> 400
> 200
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
> 2023
> Date
  
> [!NOTE] [图片 OCR 识别内容]
> e
> 0
> UVaLI.yec
> Uog
> TTae(0TaLI.ye
> Uocu
> TLeC01
> ALJS_SPVU4 /
> UILVe1Se
> 11001U
> TTC L
> OaceS (
> C7
> ind df
> brain .
> data
> frame (brain.get_data_field ("country" )
> universe-"T0P2500"
> dates= [
> "2013-01-01")] )
> Visualizations . plot
> 9roups
> aVerage
> Values (model field df
> ind df)
> Group-wise Average Datafields Over Time
> 0.4
> 0,2
> GrOUPs
> AUT
> 0,0
> BEL
> CHE
> 
> DEU
> DNK
> 一0.2
> ESP
> 
> FIN
> FRA
> GBR
> 0.4
> IL
> TTA
> NLD
> NOR
> 0.6
> PRT
> SWE
> ZAF
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
> 2023
> Dste
> get
  
> [!NOTE] [图片 OCR 识别内容]
> 「5]
> dist dict
> model_field_df.stack()
> ValUe
> counts (dropna=False)
> to_dict()
> dist_dict
> 「5」
> {-0.18000000715255737:  384378,
> -0.11999999731779099;
> 52146
> 0.23999999463558197
> 41042
> 0:  38472.
> 0.10000000149011612;34293
> 0.14000000059604645:  32634,
> -0.14000000059604645:
> 31627
> -0.05999999865889549:
> 29950
> ~0
> 07999999821186066:
> 22658
> 0.30000001192092896;
> 17290
> -0.2199999988079071:
> 14208
> -0.30000001192092896:
> 13197
> -0,019999999552965164:  11072,
> -0,25999999046325684: 10920
> 0.3199999928474426:
> 9585
> 05999999865889549
> 9574
> 0.3799999952316284:  7806
> 30000000208023224
> 7716
  
> [!NOTE] [图片 OCR 识别内容]
> 6]
> Vals
> model_field_df.Iloc [:, 0].dropna( )
> high
> np.percentile(vals, [1,99] )
> Vals ClIp
> Vals.clip(Zow,high)
> Visualizations. plot
> Values_distribution ( [vals_CIip],
> names= ["values Justribution"]
> nbins=l00)
> Visualizations . plot
> Values distribution(
> model field df]
> Dames
>  ["0riginal
> VaLU2s
> dustribution"]
> 001n5-501
> Original values dustribution
> 400000
> 350000
> 300000
> 250000
> 
> 200000
> 150000
> 100000
> 50000
> 0.6
> 一0.4
> -0.2
> 00
> 0.2
> 0.4
> 0.6
> Values
> ZOW
 总结一下 ***nws77*** 数据集中代表字段 ***nws77_sentiment_impact_projection*** 的数据分布，并用ai加以整理后就是：分布特征，数据分布高度集中且呈负偏态（左偏），众数显著地出现在-0.18附近。数值以负值为主，这表明整体的情绪预测偏向谨慎或看跌。稀疏性与覆盖率，该数据集极其稀疏，存在大量NaN（缺失）值。然而，数据覆盖率（即非缺失值的数量）自2013年以来呈现强劲的上升趋势，并表现出明显的季度性规律，这与企业财报的发布周期相符。时间序列性质，该数据为事件驱动型，而非连续的时间序列。针对特定实体的数据更新频率较低，且对应于财报电话会议等离散事件。非缺失值（Non-NaN）与非缺失且非零值（Non-NaN and Non-Zero）的数量几乎完全相同，说明有效的数值极少为零。群组行为，群组层面（如按国家分组）的均值表现出强烈的协同变动性，这表明存在一个共同的宏观或整体市场因素在影响着市场情绪。（ *Distribution: The data has a highly concentrated and negatively skewed distribution, with a prominent mode around -0.18. The predominantly negative values suggest an overall cautious or bearish sentiment projection.Sparsity & Coverage: The dataset is extremely sparse with a high prevalence of NaN values. However, data coverage (the count of non-NaN entries) shows a strong upward trend since 2013 and exhibits clear quarterly seasonality, consistent with corporate earnings reporting cycles.Time Series Nature: The data is event-driven, not a continuous time series. Updates for a given entity are infrequent and correspond to discrete events like earnings calls. The Non-NaN and Non-NaN and Non-Zero counts are nearly identical, indicating that valid data points are rarely zero.Group Behavior: Group-level averages (e.g., by country) show strong co-movement, suggesting a common macro or market-wide influence on sentiment.* ）可以直接复制用在最新的APP AI数据集探索的提示词当中。
- 模板的idea，implement细节：signal = <dataprocess_op/>(-group_backfill(vec_max(<nws77/>),country,60, std = 4.0))部分是对信号进行处理。vec_max选出vector中值最大元素。group_backfill则负责填充缺失值，减少意外平仓的情况。<dataprocess_op/>则主要用来调整数据分布，减少极值，起到增强信号的作用。ts_decay_linear(<ts_Statistical_op/>(signal, 90),5, dense = false)则是主信号部分，用来提取经过初步处理后的数据中的时序信息。ts_decay_linear则用来进一步平滑和增强信号。
- 产出效果：我尝试了174次回测，有1个可以提交的单数据字段Alpha。但是剩下的alpha几乎都有明显的信号，可以证明模版在nws77数据集的泛用性。需要进一步针对每个数据字段不同的特征进行进一步的信息提取，来得到可以提交的alpha。
- 以下是探索模版的分阶段表现（消融实验）：
- 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 07/21/2025 EDT
> anonymous
> udd AIpha
> USt
> Code
> IS Summary
> Period
> Vec_max(nws77_sentiment
> ipact_projection )
> A single Data Set Alpha
> Aggregate Data
> Sharoe
> JUTNTIET
> TICIeS
> RsCUTTS
> Drawdown
> arer
> -0.50
> 100.42%
> 0.06
> 1.43%
> 15.59%6
> -0.289600
> Simulation Settings
> Instrument Type
> Reglon
> Unlverse
> Language
> Decay
> Delay
> Tmncatlon
> Netrallzation
> Rastewrtatlon
> NaN Handlng
> Unt Handling
> VaxTrade
> Vear
> Sharpe
> Turover
> Ftness
> Returt
> Urawdown
> Margln
> Long Count
> Short Count
> Eguity
> EUR
> T032500
> 35:rESIn
> 0.3
> Satistizal
> VerI
> 2313
> 11.759:
> 7.23汩
> 7.16:
> 26903
> 1097
> 1012
> 231_
> 0.31
> 103.59
> I_
> -2.53汩
> 4.6E
> _4
> 1343
> 1271
> 2015
> 105.-29
> -0.10
> +1.96治
> 3.3
> 1 270
> 1393
> 1323
> Clone Alpha 
> 2315
> 0.13
> 103.259
> 0.31
> 55沾
> 4.37
> 11140
> 1112
> 1314
> 20
> 103.539
> -0.33
> 0.80治
> 3.31
> 1567
> 1333
> 2313
> 107.-39:
> 0.12
> -2.23汩
> 4.16::
> 431
> 1523
> 1-74
> N Chart
> Pnl
> 2313
> 102.739:
> 2.76汩
> 33
> 4
> 1463
> 1355
> 2020
> 53.219
> -0.36
> 50沾
> 3.705
> 2
> 1435
> 1332
> 5OOK
> 2321
> 0.55
> 57.079:
> 0.33
> 1.77汩
> 1.67
> 35
> 1543
> 119
> 202
> 2-.339
> 2.99沾
> 4
> TO
> 1533
> 1-90
> OOOK
> 2323
> 86.219
> -5.31汩
> 0.31
> 4E93
> 1123
> 132
> ~1,50OK
> OOOK
> Investability constrained
> Aggregate Data
> Shar0e
> LUPTO
> Fitness
> Retyrns
> UTaMOTn
> Uarain
> Jan'14
> Jul14
> Jan '15
> Jul'15
> J3n'15
> Jul"16
> Jan'17
> Jul'17
> Jan'18
> JUl'13
> Jan '19
> Jan'20
> Jul'20
> Jan'21
> Jul'21
> Jan'22
> Jul'22
> Jan'23
> 0.63
> 27.05%6
> -0.17
> -1.91%
> 20.45%
> -1.419600
> Pnl
> Investability Constrained Pnl
> 医 Correlation
> Jul3
> Ju1'19
  
> [!NOTE] [图片 OCR 识别内容]
> UNISP
> Created 07212025 EDT
> anonymous
> HUd AIphato
> Usl
> Code
> IS Summary
> Period
> Eroup_backfill(vec_max (nws77_sentiment
> impact_projection ) , country, 60,
> std
> A Single Data Set Alpha
> Aggregate Data
> ShaTOe
> JUTTUIe「
> TITE
> REUTns
> UTMOTIT
> Narain
> -0.60
> 57.42%
> -0.10
> 1.59%
> 17.43%
> -0.559600
> Simulation Settings
> Instrument Type
> Reglon
> Unlverse
> Language
> Decay
> Dlay
> Trncation
> Netrallzation
> Rastewrtatlon
> NaN Handlng
> Unt Handling
> Max Trade
> Shampe
> Turnover
> Fltmess
> Returis
> Orawdown
> Nargln
> Long Count
> Short Count
> EUIt
> EUR
> T032500
> Fast Expression
> 0.03
> Satistica
> Veris
> 7
> 1.95
> E3.129
> 7.55
> 4.99汩
> 10
> 5393
> 13
> 1JIE
> 231
> 12
> E3.359
> 7.23
> 36
> 4.35
> 0193
> 1335
> 1235
> 2315
> -0.57
> 59.139
> 0.07
> 1。13
> 2.40
> 439
> 1375
> 1352
> Clone Alpha
> 2315
> 05
> 53.279
> 7.33
> -0.72汩
> 5::
> 2593
> 135
> 131
> 2317
> 379
> 汩
> 55
> ~239
> 1523
> 1-25
> 2313
> 56.39
> 7.31
> 40治
> 41
> 1
> 143
> 1511
> Chart
> Pnl
> 3113
> 57.339
> 0.23
> 2.364
> 33
> SS
> 1-25
> 1C
> 2027
> 55.3-9
> -6_
> 675
> 039
> 133
> 1373
> 2321
> 5.139
> 0.11
> 83汩
> 35:
> EBRO
> 533
> 1-55
> OOOK
> 2022
> 52.579
> _:
> 4.36
> E39
> 1433
> 1-21
> 2323
> |
> 57.359
> 0.24
> -2.575
> 0.75
> 5393
> 17
> 331
> OOOK
> Investability constrained
> Aggregate Data
> ShaTOe
> JUTTOUE
> FITE
> ReTyrns
> OTaMOTUT
> Warzin
> Jul'13
> Jan'14
> Jul1-
> Jan'15
> J3n'15
> J3n'17
> Jul'17
> Jan'18
> Jul "13
> Jan '19
> Jan'20
> Jul'20
> Jan '21
> Jan'22
> 14122
> Jan'23
> 0.69
> 21.19%
> -0.21
> -1.95%
> 24.68%
> 1.849600
> Pnl
> Investability Constrained Pnl
> Correlation
> Year
> Juls
> Jul5
> Jul9
> JUI 21
  
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 07/21/2025 EDT
> anonymoUs
> Add Alphato
> US
> Code
> IS Summary
> Period
> quantile
> group
> backfill ( VeC
> Max ( nls77
> sentiment_impact_projection ) , country, 60,
> std
> 4.0) )
> A Single Data Set Alpha
> Aggregate Data
> Sharp=
> TTnC
> Tin sss
> TeTICT 
> TpaO
> Warein
> 0.69
> 59.16%
> 0.11
> 1.5796
> 4.3496
> 0.539600
> Simulation Settings
> Instrument Type
> Reglon
> Unlverse
> Language
> Dlay
> Tmncatlon
> Neutrallatlon
> Pastewrtalon
> NaN Handlng
> Unit Handlng
> MaxTrade
> Year
> Sharpe
> TurOVer
> Fitness
> Returs
> Drawdown
> Margln
> Count
> Short Count
> EVR
> T01775UII
> Expression
> [73
> TTT
> Verisy
> 2013
> 2.-3
> E5.259
> 0.71
> 5.39治
> 0.9
> C
> 9337
> 12
> 201
> E3.59:
> 0.27
> 2.33汩
> 1_=
> IC
> 1232
> 1113
> 2315
> E.539
> 1J
> -0.375
> 1.73
> 140
> 125_
> 174
> Clone Alpha 
> 2315
> E3.379:
> 0.36
> 03汩
> 915
> 7J
> 1223
> 1-35
> 231
> 53.739
> 0.35
> 0.76汩
> 57
> 0.2ERo?
> 1293
> 1552
> 2013
> 53.39:
> 0.15
> 1.78汩
> 63-
> ICIC
> 1293
> 1334
> Chart
> Pnl
> 2013
> 53.559
> .13
> 2.104
> SE
> [7
> 126_
> 1570
> 2320
> 55.719
> 0.26
> 60沾
> 87:
> 257
> 1232
> 1535
> 05/03/2019
> 2021
> 5.739:
> 33汩
> 90沾
> 仃 |JC
> 1 _
> 1572
> ODOK
> Pnl:
> 0-0S3k
> nvestability Constralned Pnl:
> 007.2
> 2322
> 5.029
> 3.97汩
> 1.31
> 寸
> 1267
> 1557
> 2023
> 55.339
> 0.56
> 4375
> 0.5
> CEI
> 1233
> 1532
> SOOK
> Investability constrained
> harr =
> TTnIC
> Titnsss
> TeTC 
> TraO
> Aggregate Data
> ]113
> 」1'14
> Jul 1-
> J3n"15
> J1"15
> J31'15
> J41"15
> J3n 17
> Jul"17
> Jan '18
> JUl"13
> J3n"19
> J1"13
> J1'20
> JUI'20
> J3n'21
> J'21
> Jn'22
> J122
> Jn'23
> 0.61
> 21.94%
> 0.16
> 1.5196
> 4.6596
> 1.389600
> Ce
> Lom
> Cau
> GOK
> Irs'
  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_ir(quantile ( -group_backfill
> Vec
> 0F
> (nws77_sentiment
> Ipact
> projection)
> 60,
> std
> 4.01)
> 90)
> ASingle Data Set Alpha
> Aggregate Data
> Sharc =
> TUFNOU
> Fnss
> ReCUTT
> UrauTOT
> Harair
> Simulation Settings
> 0.95
> 28.99%
> 0.30
> 2.92%
> 5.64%
> 2.029600
> Instrument Type
> Reglon
> Unlverse
> Language
> Decay
> Delay
> Tmncatlon
> Netrallzation
> Rastewrtatlon
> NaN Handlng
> Unt Handling
> VaxTrade
> EVR
> T01775UII
> FSst ECrEssion
> 0.03
> TTT
> Verisy
> Vear
> Sharpe
> Turover
> Ftness
> Retur
> Drawdown
> Hargln
> Long Count
> Short Count
> 2313
> 3.15
> 33.703
> 门[7
> -0.51
> 2.339
> ~3.318
> 11TE
> 1033
> 231_
> 28.8E%
> OJ
> 0.71
> 3.539
> 0.-3沾
> 1375
> 12-5
> Clone Alpha 
> 2015
> 27.25%5
> 14
> -1.75
> 3.19
> .25*
> 1431
> 1237
> 2315
> 27.5S
> 57
> 2.079:
> 4.1380
> 135
> 133
> 2
> 28.71%
> 0.07
> 05
> 2.219
> 0751
> 11
> 12
> Chart
> Pnl
> 2313
> 25.713
> 3
> 2.119
> 1.15
> 1355
> 2313
> 1.21
> 25.243
> 0.5i
> 2.229
> 0沁:
> 517
> 1313
> 2020
> 32.5E%
> 一|_
> 12.9
> 1.-79
> ,31
> 457
> 1331
> OOO
> 2321
> 33.733
> 10.32
> 1.739:
> 匕沁:
> EO4
> 1354
> 202
> 0.75
> 25.3135
> .21
> 2.7
> 1.759
> 5351
> 593
> 13
> OOOK
> 11/23/2013
> 2323
> 30.9E%
> -15.55
> 1.239
> =10.7551
> 1JT
> 13-
> PnL
> 455.5TK
> Investabilit Constrained Pnl: 250.25K
> Investability constrained
> ]113
> 」1'14
> Jul 1-
> J1"15
> J31'15
> J41"15
> J3n"17
> Jul"17
> Jan '18
> JUl"13
> J3n"19
> J1"13
> J1'20
> JUI'20
> J3n'21
> J'21
> Jn'22
> J122
> Jn'23
> Aggregate Data
> Sharp=
> TUFNCUET
> FITSs
> Returns
> Urau'TOT
> Narai
> 0.42
> 10.83%
> 0.13
> 1.179
> 7.14%
> 2.1
> Yooo
> country;
> Cau

- 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_decay_Iinear (ts_ir (quantile
> Broup
> backfill(Vec_max (nw577
> sentiment_impact_projection
> country, 60,
> std
> 4.0)),90),5
> dense
> False )
> Asingle Data Set Alpha
> Aggregate Data
> Sharps
> TITnI=
> Cac
> ReMI =
> TCaO
> Warzir
> Simulation Settings
> 1.11
> 18.76%
> 0.46
> 3.27%
> 3.9496
> 3.499600
> Instrument Type
> Reglon
> Unlverse
> Language
> Decay
> Ulay
> Truncatlon
> Neitrallatlon
> Pastewrtaton
> NaNHandlng
> Unt Handlng
> HaxTrde
> EUIt
> EUR
> T032500
> ~5  rESIn
> 0.03
> Satistica
> Veris
> Year
> TuroVer
> Ftness
> Returs
> Drawdown
> Margln
> Cownt
> Short Count
> 2313
> .28
> 21.433
> JOE
> 0.855
> 2.70
> 0.3151
> 1102
> 1971
> 2011
> 13.323
> 0.20
> 85
> 2.559
> 3
> 13T
> _一
> Clone Alpha
> 3115
> 17.725
> -7.14
> 一
> 539
> 5:
> 1432
> 123
> 2315
> 2.12
> 17.433
> 1.18
> 5.37
> 1一
> 5。
> 1325
> 1337
> 2317
> J.JS
> 13.425
> 0.00
> 0.13
> 339
> 0.1-5
> 1345
> 175
> Chart
> Pnl
> 2313
> .22
> 17.E8%
> 0.28
> 2133
> 1 3_
> 2.3551
> 171
> 135
> 2313
> 17.053
> 3.11
> 075
> 379
> 1.2551
> 1515
> 1315
> 2327
> 21.253
> 2.30
> 12.-7
> -2
> 11.57d
> 145E
> 1239
> 2021
> 3.17
> 21.52%
> 235
> 1.759
> 1.31
> 507
> 135
> OOOK
> 232
> .34
> 15.575
> D.OE
> 0.31
> 1.779
> 1.沁:
> 195
> 1314
> OOOK
> 09/10/2013
> PnL
> 321.75k
> 2023
> -5.78
> 13.203
> 5.24
> -15.735
> 1.239
> -16
> 1411
> 1329
> Investabilit Constrained Pnl: 104.27K
> Investability constrained
> Jan'14
> Jul'1
> Jan'15
> J3n'15
> Jan'17
> Jan'18
> Jan '19
> Jan'20
> Jul'20
> Jan '21
> Jan'22
> Jan'23
> Data
> TITIT
> TT=ss
> TTUCT
> TpaO
> Aggregate
> 0.37
> 8.6396
> 0.10
> 0.99%
> 9.8596
> 2.299600
> Pnl
> Investability Constrained Pnl
> Shan
> Loro
> Ju1'13
> Juls
> Jul5
> JUl'17
> Jul'13
> Jul9
> JUI 21
> Jul22
> STr
> 1!3rEI

- 建议其他顾问未来尝试的探索方向: 这个数据集中turnover普遍较高（不是某些时间的极端值，而是从时间上看都很高），margin较低。

---

### 评论 #14 (作者: WL13229, 时间: 11个月前)

[LH44620](/hc/en-us/profiles/26717918976919-LH44620)

漂亮，漂亮到我觉得50USD都少了

---

### 评论 #15 (作者: AH18340, 时间: 11个月前)

```
<group_compareOP/>(<risk_field/>, <std_group/>) 
```

- 模板中的变量使用 **< />** 进行了声明，总共三个变量。
- 具体变量1： **<group_compareOP/>** : 可以对组间进行计算的分组运算符，例如group_rank, group_zscore, group_neutralize等
- 具体变量2： **<risk_field/>** : 可以包含所有和 GLB risk 的数据集，vec数据需要套上vec_op
- 具体变量3： **<std_group/>** : 可以包含pv,other 数据集中 group类型的数据

- 搜索空间的大小：<group_compareOP/>使用group_zscore ， **<std_group/>** 选5个，所有GLB三个region , 6 种中性化，risk 下的数据集为例的话，一共是6750个
- 
> [!NOTE] [图片 OCR 识别内容]
> groUp VARCHAR
> region VARCHAR
> universe VARCHAR
> oth455_customer_n2v_p10_q50_WS_pca_fact2_cluster_10
> GLB
> TOPDIV3O00
> pv13_2_sector
> GLB
> TOPDIV3O00
> stal_allc2
> GLB
> TOPDIV3OOO
> stal_allc10
> GLB
> TOPDIV3OOO
> exchange
> GLB
> TOPDIV3OOO
> oth455_relation_n2v_p10_q50_WS_pca_factl_cluster_20
> GLB
> TOP3000
> oth455_competitor_n2v_p10_q50_W3_pca_factl_cluster_20
> GLB
> TOP3000
> stal_allc5
> GLB
> TOP3000
> country
> GLB
> TOP3000
> stal_allc50
> GLB
> TOP3000
> oth455_partner_n2v_p10_q200_WS_pca_factl_cluster_5
> GLB
> MINVOLIM
> pv13_2_sector
> GLB
> MINVOLIM
> stal_allc2
> GLB
> MINVOLIM
> stal_allcl0
> GLB
> MINVOLIM
> exchange
> GLB
> MINVOLIM

- 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：
- 使用labs 查看这个这个数据集，在回测后发现该字段本身就是有信号的，使用不同组间运算符增强组间信号
- 
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 07/20/2025 EDT
> anonymous
> Add Alpha to
> List
> Code
> IS Summary
> Period
> IS
> 05
> FSK70
> mfmz_gemtrd
> anlystsn
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: GLB/DI/RISK XI
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 1.24
> 6.339
> 0.80
> 5.19%
> 5.699
> 16.39%0。
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
> GLB
> TOPDIV3OO0
> Fast Expression
> 0.08
> Market
> On
> On
> Verify
> Off
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
> 3.55
> 7.42%
> 3.34
> 11.04%6
> 1.56%
> 29.7590
> 673
> 745
> 2014
> 2.60
> 6.39%
> 89
> 6.5996
> .42%6
> 20.619600
> 722
> 823
> 2015
> 1.01
> 6.30%
> 0.50
> 3.10%
> 2.41 %
> 9.83900
> 801
> 842
> Clone Alpha
> 2016
> -0.75
> 6.32%
> -0.34
> 2.52%
> 3.91%
> .98%600
> 753
> 840
> 2017
> 66
> 5.95%
> 0.97
> 4.28%
> 1.93%
> 14.39900
> 750
> 836
> N Chart
> Pnl
> 2018
> 0.71
> 5.88%
> 0.32
> 2.48%
> 3.88%
> 8.44900
> 833
> 907
> 2019
> 29
> 6.09%
> 0.08
> 86%
> 3.23%
> 2.82900
> 816
> 884
> 2020
> 0.92
> 5.46%
> 0.64
> 06%
> 5.69%
> 22
> 8900
> 847
> 1023
> 2021
> 2.41
> 6.56%
> 2.63
> 14.9196
> 3.23%
> 45.4700
> 1020
> 1204
> 4,00OK
> 2022
> 1.55
> 6.96%
> 1.26
> 8.259
> 4.32%
> 23.73900
> 979
> 1129
> 2023
> 10.95
> 6.14%
> 20.20
> 42.5496
> 2.67%6
> -138.64000
> 966
> 995
> 2,00OK
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.32
> 6.339
> 0.06
> 0.449
> 3.799
> 1.409oo
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
> Q
> Investability constrained

- 发现sharpe增加，fitness增加不多
- 
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 07/20/2025 EDT
> anonymous
> Add Alpha to
> List
> Code
> IS Summary
> Period
> Is
> OS
> groUP
> ZsCOre
> rsk70_mfmz
> gemtrd
> anlystsn, densify ( pv13_2
> SeCtor
> U
> Power Pool Alpha
> Pyramid theme: GLBIDI/PV X1
> Pyramid theme: GLBIDIIRISK X1
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation
> Settings
> 1.64
> 7.859
> 0.86
> 3.46%
> 2.06%
> 8.81%。
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
> Max Trad
> Equity
> GLB
> TOPDIV3OO0
> Fast Expression
> 0.08
> Crowding Factors
> On
> On
> Verify
> Off
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
> 2.66
> 8.9696
> 1.70
> 5.10%
> 0.89%
> 11.38200
> 712
> 703
> 2014
> 80
> 7.809
> 0.91
> 3.19%
> 1.01%
> 8900
> 761
> 781
> 2015
> 0.84
> 7.7096
> 0.29
> 1.54%
> 40%
> 3.999600
> 766
> 874
> Clone Alpha 
> 2016
> 0.20
> 7.8996
> 0.04
> -0.40%
> 64%
> 02900
> 781
> 809
> 2017
> 1.59
> 7.2796
> 68
> 2.27%
> 0.80%
> 6.252600
> 790
> 793
> 2018
> 2.10
> 7.219
> 24
> 4.39%
> 81%
> 12.179600
> 852
> 884
> N
> Chart
> Pnl
> 2019
> 1.38
> 7.3796
> 0.62
> 2.55%
> 1.24%
> 6.929600
> 840
> 857
> 2020
> 2.10
> 6.8096
> 44
> 5.91%
> 1.26%
> 17.38900
> 889
> 976
> 2021
> 1.92
> 8.6496
> 1.15
> 4.51%
> 1.78%
> 10.43900
> 1083
> 1135
> 2022
> 2.84
> 8.8596
> 2.17
> 7.30%
> 1.41%
> 16.49900
> 1008
> 1097
> 2023
> 8.46
> .50%6
> -11.31
> -22.34%
> 46%
> 59.589oo
> 985
> 973
> 2,00OK
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.66
> 7.949
> 0.88
> 3.51 %
> 2.259
> 8.839。
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

- 尝试再外面套ts_op效果不理想
- 产出效果：我尝试了6750次回测，有的sharpe是<0的，需要表达式前加负号，最终回测比这数值高，有339个sharpe>1的alpha,目前已选中几个提交点亮的py
- 建议其他顾问未来尝试的探索方向: 其他region

---

### 评论 #16 (作者: WL13229, 时间: 11个月前)

[AH18340](/hc/en-us/profiles/28845157706135-AH18340)

模板似乎与课堂示例没有太多不同，没有原创性，没有针对数据集进行深入探索，深度不足。请重新思考并修改。

---

### 评论 #17 (作者: AL13375, 时间: 11个月前)

## 模板

```
<ts_op1/>(<ts_op2/>(<oth_datafields/>,<days1/>),<days2/>)
```

- 模板中的变量使用 **< />** 进行了声明，总共三个变量。
- 具体变量1：<ts_op1/>: 可以包含时间序列中所有字段，如ts_returns、ts_rank、ts_zscore等
- 具体变量2：<ts_op2/>: 可以包含时间序列中所有字段，但两个字段不可以重复，建议这里选择ts_mean、ts_max、ts_delta等字段
- 具体变量3：<days1/>: 时间窗口，可选为20，60，120，252，504等
- 具体变量4：<days2/>: 时间窗口，可选为5，20，60，120，252等，并且days2要大于days1

- 搜索空间的大小：以数据集other143为例的话，大约是84*3*3*15=11340
- 模板的idea，implement细节：该双重时间序列模板是利用不同时间窗口的数据差异，分析数据的周期性内在联系，其中ts_op2的作用是为了对数据做预处理，对于oth_datafields的选择为覆盖率大于等于80%以保证处理效果，再用ts_op1获得主信号，灵感来自于lab上对于数据字段周期性的研究，认为PNL的变化在一定尺度上的变化幅度是符合周期性的，未来也可以根据周期做相应预测。
- 产出效果：我尝试了3000次回测，有24个可以提交的Alpha，并且近三年表现都较好且有递增趋势，其中一个数据如下（无法上传图片，在这里简单说明一下产出alpha的特点：pnl后期无下滑且一直向上，sharpe也是如此）。
- YearSharpeTurnoverFitnessReturnsDrawdownMarginLong CountShort Count
- 2021 1.37 13.05% 1.08 8.08% 4.13% 12.39‱ 1520 1482
  2022 2.34 11.37% 2.38 12.88% 3.14% 22.65‱ 1539 1523
  2023 8.86 10.52% 13.63 29.57% 0.22% 56.21‱ 1553 1525
- 建议其他顾问未来尝试的探索方向: 该模板为基础模板，可以嵌入到其他模板中代替单字段使用，后续建议在anl、mdl、fnd等覆盖率较高的数据集中使用（或者手动选择覆盖率高的字段）。

---

### 评论 #18 (作者: XC66172, 时间: 11个月前)

```
alpha = alpha; #有信号的一阶表达式vector_neut(alpha,ts_backfill(<risk70/>,120)) #是否要ts_backfill可自行决定
```

- 模板中的变量使用 **< />** 进行了声明，总共一个变量。
- 具体变量1： **<risk70/>** : dataset risk70;
- 搜索空间的大小：以ASI - D1 - MINVOL1M为例，一共30个字段
- 模板的idea，implement细节：alpha是一阶表达式作为主信号，vector_neut(alpha,ts_backfill(<risk70/>,120))对于主信号做风险因子的中性化处理（类似于neutralization里的RAM,statistical等)，相当于对一阶因子做二阶处理
- 产出效果：我回测了几个有信号的一阶表达式套上模板，回测结果都和原来的表达式信号大致相同，同时也是鲁棒性测试的一个补充检验（和neutralization类似，一般而言returns可能比原信号稍微低一点，但同时drawdown也会降低）
- 注意事项：alpha推荐是有信号的一阶表达式，假设是二阶表达式（这时可能已经用了两个数据集包含pv),则再套用以上模板则此表达式最终有3个数据集，虽然可以提交但无法点亮任何金字塔。所以注意alpha应该只包含一个数据集的字段。
- 应用场景：

（1）假设一阶表达式刚好卡在pc（0.72）或者sc边缘（0.52），套用该模板后有可能降低相关性得以提交

（2）假设RISK pyramid还没有点亮，提交此类因子有助于点亮RISK pyramid

（3）vector_neut算是一个比较少用的operator, 可增加六维里的operator count

- Reference:  [[L2] Getting started with Risk DatasetsResearch_27157459347991.md?_gl=1*1orlfhc*_gcl_au*ODM4Njg5MjI5LjE3NDg1MjY5NDQ.*_ga*MTc0ODUyNjk0MTk2OTRmNjhiNDBjMGVlZTk.*_ga_9RN6WVT1K1*czE3NTMxOTg1NTgkbzI4OSRnMSR0MTc1MzE5OTYyNyRqNTYkbDAkaDA]([L2] Getting started with Risk DatasetsResearch_27157459347991.md?_gl=1*1orlfhc*_gcl_au*ODM4Njg5MjI5LjE3NDg1MjY5NDQ.*_ga*MTc0ODUyNjk0MTk2OTRmNjhiNDBjMGVlZTk.*_ga_9RN6WVT1K1*czE3NTMxOTg1NTgkbzI4OSRnMSR0MTc1MzE5OTYyNyRqNTYkbDAkaDA) .
- 以上模板来自于官方推荐，亲测有效。

**Example Alpha ideas:**

Use  `vector_neut(Alpha, factor)`  to neutralize your Alpha's exposure to a chosen risk factor. Iterate over different factors to determine whether your Alpha's returns are influenced by any of them. This approach helps you maintain diversity in your Alpha pool and avoid over-reliance on a few specific factors.

例子：

原来因子（alpha)

```
 ts_backfill(oth176_maltahc_eq_score, 120)
```


> [!NOTE] [图片 OCR 识别内容]
> Simulation 14
> Simulaton 7B
> Settings
> ASIIDIIMINVOLTM
> IS Summary
> Period
> TRAIN
> TEST
> Streak: 145 day
> ts_backfill(othI76_maltahc_eq_score, 120);
> . Single Data Set Alpha
> Aggregate Data
> SrOE
> UTTCI
> SReS
> RCUTnS
> UrauoUAT
> Narsr
> 1.59
> 4.89%
> 1.46
> 10.58%
> 15.06%
> 43.309600
> Year
> Sharpe
> Tumower
> Fitness
> Returs
> Orawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.439
> 1.34汩
> 3.119:
> 5.719
> 1_1
> 1132
> 201-
> !
> -3
> 17.34汩
> 3.339:
> 7373:
> 13
> 2015
> 1.55
> E3:
> _ 
> 5339:
> 3353:
> 1435
> 2016
> 1.43
> 5.259
> 117
> 7.TE
> 30
> ZS.SE
> 1
> 1371
> 2017
> 2.53
> 一
> .3
> 12.12
> 2529
> 51.018:
> 115
> 1331
> 2018
> E2%
> 252
> 1.38泸
> 5559
> EE S980:
> 1555
> 1-34
> 2013
> 0.07
> 0.40沾
> 5219
> 5
> 1425
> 13
> 2027
> 3.85
> 5.229
> GE
> 5.514
> 12-79:
> -21.13:
> 1572
> 1-30
> 2021
> 11.2
> 239
> 22.3
> 51.574
> 0.139:
> E4SEX:
> EIE
> 1623
> 2021
> 1.51
> 279
> 12.8E治
> 5__9
> 53.5:
> L
> 1754
> 2022
> 1.31
> 239
> 15.3
> 17_59
> TJE
> 1750
> 2023
> 一4
> 5.179
> -5.75
> -21.124
> .319:
> -21.754:
> 672
> 153r
> Risk neutralized
> Aggregate Data
> Sharpe
> TITnOIE
> Fitmc
> TeICT 
> UTMJTI
> Iarain
> 2.26
> 4.8996
> 1.21
> 3.619
> 3.23%
> 14.789600


套用模板后因子

```
alpha =ts_backfill(oth176_maltahc_eq_score, 120);vector_neut(alpha,ts_backfill(rsk70_mfm2_asetrd_cntadj,120))
```


> [!NOTE] [图片 OCR 识别内容]
> Simulation 1A
> Simulation 18
> Settings
> ASIIDIIMINVOLIM
> IS Summary
> Period
> TRAIN
> TEST
> Streak: 145
> alpha
> =ts_backfill(othl76_maltahc
> eq_sCore, 120);
> Vector_neut(alpha
> ts_backfill(rsk7o_mfmz_asetrd_cntadj,120) )
> Aggregate Data
> 5narne
> TUTTLIE
> Fines
> RsTIICn 
> JraTr
> Marsn
> 1.72
> 4.11%6
> 1.57
> 10.47%
> 13.23%
> 50.929600
> Year
> Sharpe
> Tumower
> Ttness
> Returs
> Orawdown
> Maryin
> Long Count
> Short Count
> 2013
> 3.36
> 一739
> 14.33汩
> 2259
> E0.01X0:
> 121
> 1132
> 201-
> 3
> 3
> -3
> 17.13治
> 3.359
> SE.ZEt::
> 1355
> 1335
> 2015
> 2.03
> SJ:
> 22
> 12-15
> 5339
> 6519:
> 1430
> 135
> T 
> 一4
> 2
> 7.50汩
> 5.329
> 31-:
> 15
> 1352
> 2017
> 2.53
> 559:
> 2.96
> 12.34;
> 579:
> E:
> 145
> 1372
> 2013
> 2.36
> 3.27:
> 2.5
> 14.珑:
> 659:
> 74.3540
> 1557
> 113
> 2013
> 4
> 1339
> 7.15
> 2.29沿
> 5279
> 1:
> 143
> 1331
> 2027
> ~3.5D
> 一
> J.ED
> -5.525
> 11.539
> -25.46:
> 1471
> 2021
> 11.73
> 039:
> 32
> 5.205
> 0.15%
> 211.515:
> 635
> 1EJS
> 2021
> 559:
> 12.15:
> 5.529
> E1 34
> 133
> 17-
> 2022
> E39:
> .7
> 16.10沾
> 339
> 5:
> 1734
> 173
> 2023
> -239:
> 1.51汩
> 659
> 723:
> 1535
> 1534
> Risk neutralized
> Aggregate Data
> SArce
> UTIONEI
> SITS
> ReUrns
> UTaWTJT
> WaTaIT
> 2.15
> 4.1196
> 1.14
> 3.549
> 3.37%6
> 17.219600
> day


可以看到数据基本有所提升（除returns外），

sharpe: 1.59 -> 1.72; fitness:1.46->1.57; Returns:10.58%->10.47%;Margin:43.3 ->50.92

---

### 评论 #19 (作者: LH44620, 时间: 11个月前)

WL13229 谢谢老师的认可

---

### 评论 #20 (作者: WL13229, 时间: 11个月前)

[XC66172](/hc/en-us/profiles/28880767093655-XC66172)

内容OK，但请补充一些具体应用，例如你使用过的因子，放进去的效果。

---

### 评论 #21 (作者: WL13229, 时间: 11个月前)

[AL13375](/hc/en-us/profiles/27647035974807-AL13375)

> "产出效果：我尝试了3000次回测，有24个可以提交的Alpha，并且近期表现都较为优异。"

请补充说明、细节

---

### 评论 #22 (作者: AL13375, 时间: 11个月前)

WL13229 无法上传图片，已补充文字说明，请老师点评指正！

---

### 评论 #23 (作者: XC66172, 时间: 11个月前)

@WL13229  谢谢WEIJIE老师点评，我已经在原来的帖子基础上补充了例子。

---

### 评论 #24 (作者: YZ70114, 时间: 11个月前)

```
模板:去除组内平均效应的相对排名信号s = <vec_op/>(<risk_data/>) - group_mean(<vec_op/>(<risk_data/>), <weight/>, <group/>);<group_op/>(<cross_op/>(s)，<group2/>)
```

模板中的变量使用< />进行了声明，总共7个变量。

- 具体变量1：<vec_op/>: vector 数据处理 例如：vec_avg 等
- 具体变量2：<risk_data/>: risk 数据集推荐USA-D1 的risk60 的  rsk60_crowding, rsk60_offer
- 具体变量3：<weight/>: group_mean 的weight 定义，可以放 1 或者adv20 等pv1 的字段
- 具体变量4：<group/>: 中性化组，pv1例如:sector, market, industry, subindustry
- 具体变量5：<group_op/>:使用 group_rank group_zscore 等做排名
- 具体变量6：<cross_op/>横截面 运算符 例如：zscore, rank, quantile 等
- 具体变量7：<group2/>: 中性化组，pv1例如:sector, market, industry, subindustry

搜索空间的大小：以数据集risk60为例的话，大约是(SearchSpace: 1 × 2 × 1 × 4 × 3 × 3 × 4 = 288)
模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：
  核心思想是构建一个去除组内平均效应的相对排名信号。
  sign = <vec_op/>(<risk_data/>) - group_mean(...) - 核心主信号，通过减去组内均值来获得相对强度
  <group_op/>(<cross_op/>(sign), <group2/>) - 对信号进行截面处理和二次分组排名

该模板是之前kunqi 老师分享的组平均差去做的实操，我直接用于risk60做的尝试，直接是先用组分差看是否有信号，再一步步套其他操作符号产生的，在这里做了一个web app 的template 版本，希望能给大家有所启发。
跑了之后我去分析其中的原理:

```
rsk60_crowding 的字段说明：Crowding is a daily score for shorting and covering activity on the security. Scores of 7 and greater represent significant shorting activity for a given day. Scores of 5 to 0 show notable shorting activity for a given day. Negative scores represent covering on a security. Scores of -7 and less represent significant covering activity for a given day. Scores of 0 to -5 show notable covering activity for a given day. 可得rsk60_crowding 是衡量个股每天卖空拥挤度的打分指标≥ 7 显著做空压力1 ~ 6 可观察到做空行为 0 中性，无明显变化  -1 ~ -6 可观察到回补行为 ≤ -7 强烈的空头回补 因子则是衡量一只股票的空头交易活跃度相对于市场平均的偏离程度排名靠前（空头很集中）:可能市场过度看空，反弹潜力大 排名靠后（大家都在回补）: 市场开始转向就顺势做多，情绪刚转暖行业内部比较剔除行业因素，看相对强弱，精选同类股里“风向变”的那只
```

建议其他顾问未来尝试的探索方向:
  1.权重的控制可以探索其他值
  2.其他地区的数据是否也能好的效果？


> [!NOTE] [图片 OCR 识别内容]
> Code
> 1
> group_rank (quantile
> Vec_avg ( rsk6o_crowding
> group
> mean
> Vec_avg
> FSKGO
> crowding _
> 1,
> market ) ) , densify ( subindustry )
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
> Unit Handling
> Max Trade
> Equity
> USA
> TOP3000
> Fast Expression
> 20
> 0.07
> RAM
> On
> On
> Verify
> Off
> Delay



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,0OOK
> 4,00OK
> 2,00OK
> 04/28/2016
> TrainPnl。 122.24K
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


---

### 评论 #25 (作者: WL13229, 时间: 11个月前)

[YZ70114](/hc/en-us/profiles/26918538763927-YZ70114)

变量描述的地方似乎缺少了 下列变量的描述

```
cross_op
```

---

### 评论 #26 (作者: YZ70114, 时间: 11个月前)

[WL13229](/hc/en-us/profiles/12285040305687-WL13229)  不好意思，写漏了一个操作符，已补上

---

### 评论 #27 (作者: WL13229, 时间: 11个月前)

[SL95036](/hc/en-us/profiles/30784934275991-SL95036)

您的发言偏离主题，在本贴无贡献。请不要将AI的内容不假思索进行粘贴，您的历史论坛活动将被人工审核，疑似AI的帖子或评论都将被删除，社区分数亦会被相应降低。

---

### 评论 #28 (作者: LL49894, 时间: 11个月前)

```
模板：ts_corr(ts_zscore(<vec_op/>(<snt27_data/>),20), ts_zscore(<vec_op/>(<snt27_data/>),20), 90)
```

模板中的变量使用< />进行了声明，总共两个变量
具体变量1：<snt27_data/>: USA TOP3000 的sentiment27数据中的两两组合字段。这个数据集只有429个 user使用，Pyramid 1.4。
具体变量2：<vec_op/>:vec_sum 或者 vec_avg，处理vector类型的数据
搜索空间的大小：272 × 4 = 1088
模板的idea：这个数据集是针对热门网站的排名指标，通过计算两个经过标准化处理的网站相关指标在过去 90 天内的时间序列相关系数，衡量这两个指标同步变化趋势，更好的反映网站的市场表现、用户偏好或竞争格局的内在关联。最后得到做多或者做空的信号。
implement细节：
首先用vec操作符号对处理vector类数据，
然后用ts_zscore对数据进行标准化处理，统一量纲
最后用ts_corr计算两者的关联程度，这里选择的90天，计算中长期的关联程度，如 “网站排名” 与 “相对受欢迎度” 是否在 90 天内同步上升 / 下降）。作为最终的主信号
产出效果：我尝试了1088次回测，有6个可以提交的Alpha。提交标准为PPAC。该模板为单数集字段。
建议其他顾问未来尝试的探索方向：可以扩展到多数据集计算两两的相关程度，在时间的选择上面也可以修改，比如252天，60天和20天，捕捉长期，短期交易信号。

以下是其中一个alpha：使用的字段为

```
snt27_relpopularity08_11：Relative popularity calculated with alpha=0.8 snt27_avgranking_19：Average of rankings
```

snt27_relpopularity08_11反应了市场短期情绪或消费者即时偏好

snt27_avgranking_19 简单平均排名则代表长期稳定表现，不受短期波动影响

当两者相关性较高时，说明短期热度与长期质量表现一致；若相关性低，则可能表示 “昙花一现” 的炒作或未被市场及时发现的优质产品。计算两者的ts_corr相关程度，可以生成做空以及做多的信号。该alpha表现如下。


> [!NOTE] [图片 OCR 识别内容]
> Simulation 1
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> 1S SUmmary
> Period
> IS
> 05
> Settings
> USA/D1/T0P3000
> Convertto Multi-Simulation
> Streak: 17 day
> Single Data Set Alpha
> ts
> corr(ts
> ZsCOre
> Vec_aVg(sntz7_avgranking_19),20)
> ts
> ZSCore(Vec
> SUI
> Snt27
> peL
> popularityog_11),20)
> 90
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.78
> 2.6296
> 1.40
> 7.6996
> 5.049
> 58.649600
> Vear
> Sharpe
> TrOVer
> Ftness
> Retums
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.0090
> 0.00
> 0.0090
> 0.00%
> 0033oo
> 2014
> 0,00
> 0.0090
> 0.00
> 0.00%
> 0.0ON
> 0.0033oo
> 2015
> 0,00
> 0.0090
> .00
> 0.009b
> 0.009
> 0033oo
> 2016
> 0,00
> 0.0090
> 0.00
> 0.0090
> 0.0ON
> 0.0033oo
> 2017
> 0,00
> 0.009b
> 0.009b
> 0.009
> 0033oo
> 2018
> 0,00
> 0.0090
> 0.00
> 0.0090
> 0.0ON
> 0033oo
> 2019
> 1,82
> 3.0996
> 22
> 5.59%6
> 3.2390
> 36。
> 89300
> 1756
> 911
> 2020
> 2.35
> 1.9990
> 1.97
> 8.75%
> 2.6790
> 87.683o0
> 2136
> 961
> 2021
> 2.53
> 2.4190
> 2.36
> 10.8990
> 2.5290
> 90.4433oo
> 2255
> 891
> 2022
> 0.92
> 2.5890
> 0.58
> 4.9990
> 5.0490
> 38.663o0
> 2309
> 841
> Clone this Alphain a newtab
> 2023
> 0.03
> 2.8890
> 0.00
> 0.1690
> 1.2990
> 49300
> 2207
> 949
> Example
> Simulate
> Visualization
> Add Alpha
> Openalpha detalls
> Check Submission
> Submit Alpha
> LISt
> in newtab


在五月份成为条件顾问以后，第一VF更新为0.95。因为snt27这个数据集做的人较少，所以自己单独尝试了一下，鉴于该数据集只有2019年以后的数据，我并不太确定这个alpha的稳定性。所以没有交，也想请weijie老师指点一下。谢谢老师！

如下图所示，已补充数据分布以及更新频率，基本上每天或者3-4天就会更新，这个更新频率应该比较符合sentiment的。


> [!NOTE] [图片 OCR 识别内容]
> snt27 Values dustribution
> 40000
> 35000
> 30000
> 25000
> 
> 20000
> 15000
> 10000
> 5000
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> Values
> Ie6



> [!NOTE] [图片 OCR 识别内容]
> Update rrequancy
> 40
> 35
> 3,0
> Metncs
> 「25
> Ieralldays
> '0
> 15
> 10
> 202101
> 202104
> 3021-01
> 202110
> 202201
> 2022-04
> 2022-01
> 2022-10
> 2023-01


该alpha换手率极低，我感觉可能是和90天长窗口有关系，我先测试了ts_zscore的窗口，换手率没有变化，估计只要两个序列的相对波动节奏一致，它们的 z-score 变化方向可能同步，相关性未必剧烈变化。

我继续测试，调整ts_corr的窗口为5天，10天，20天如图所示：


> [!NOTE] [图片 OCR 识别内容]
> -ts_corr(ts
> ISCOTEIVE
> aVB(sntzT_aygranking
> +181,
> T5Core er
> Rdc-
> LsTC2
> Felpopularityay_II,
> HSregat Data
> hurr
> Turno'
> Dradoyr
> 1.45
> 23,769
> 0,71
> 5,659
> 4.799
> 4,769600
> Cs



> [!NOTE] [图片 OCR 识别内容]
> LOII5
> 3SLIIP
> UB(snt7 avrankin
> 17,161
> 35OeLIe
> Hsnge Data Set Alpha
> (50127 Telppularityi 11,10
> ABgTCBatC Oata
> ThJ
> 1.58
> 12.189
> 1,27
> 7.16%
> 3,6595
> 11.7690



> [!NOTE] [图片 OCR 识别内容]
> Streak:
> NSSretate Uuta
> ShuTp
> OTTCT'
> TIUoIT
> CUTT C
> ISCOTE IVEC
> aVB(sntz7_avranking
> 1,16
> T =IIIP|T三
> 57
> 6,7495
> 1.17
> 6,9495
> 4,5595
> 20.5990
> 1St 77
> TeLTODUJanlt
> 111,11,
> SNTC
> J
> t
> Rtu
> UmwOI
> MMIT
> Uo Cot
> L T
> NT
> 107
> IU
> IT
> III
> D
> DDL
> TOT
> T
> 10
> NU
> U
> 2016
> 1
> .0751
> IT
> T
> NTO
> 0.039
> NIU
> T T[
> TII
> III
> IUIL
> T
> L M
> O
> JI
> J'午
> 3
> 5.775
> 37-1
> 15
> TITE
> 0
> T
> `4
> 19 SI:
> ?Z
> 5.195
> 4551
> 」
> 1165
> 77
> 7
> U11[
> CrAAhINSTOTk
> - |
> Alph
> Upnn nha Npralls
> Example
> OIN
> VNIH
> I Ts It
> Check Submlsslon
> Submlt Alpha


短期关系易反转，换手率突然上升，长窗口的话，更能看出两者之间的稳定关系，所以 **ts_corr 是 “信号变化频率” 的核心开关** ，而 ts_zscore 更多影响信号的 “波动幅度”，这也是为什么调整 ts_corr 窗口后换手率变化更显著。虽然这几个窗口都能提交，估计是需要找到一个临界点。我个人感觉10天的窗口比较合适。请weijie老师再看一下。

---

### 评论 #29 (作者: WL13229, 时间: 11个月前)

[LL49894](/hc/en-us/profiles/30413446999703-LL49894)

抽空可以看看数据字段本身的更新频率。目前这个Alpha的更新频率很低，感觉上来说，一个sentiment的数据不应该这么低的更新频率。如果更新频率匹配且相关性低的话，不失为一个好的Alpha

---

### 评论 #30 (作者: GZ81958, 时间: 11个月前)

## 消除市值干扰后的分析师数据横截面比较

### 模版:

```

financial_data = ts_backfill(<analyst_field/>, 66);
signal = <group_operator/>(financial_data, <group/>);
signal - regression_proj(signal, rank(cap))

```

### 变量:

- <analyst_field/> 分析师数据，如果是向量的话用 vec_sum / vec_mean 处理

- <group_operator/>: group_zscore, group_scale, group_neutralize

- <group/>: 分组我是直接使用 mechine_lib 里面 USA 定义的分组，加上 industry, sector 这些

### 搜索空间大小：

以 analyst4 为例：
matrix数据 202 + vector数据 148 * 2 = 498; 分组操作符3个; 分组数据没有太细究，直接从 machine lib 上复制了大概20个。

因此：一共大概 500 * 3 * 20 = 30000 搜索空间。

### Idea & Implement

开始尝试直接对分析师数据数据做时间序列处理后，发现 turnover 特别高，而且信号感觉不强。因此，开始直接进行组件横截面比较，信号不错。而后想到一般而言，市值越高的公司会越受到分析师关注，所以高市值公司分析师数据会有更多偏见，正好可以用使用 `regression_proj` 把原来信号和市值进行回归，然后再减去结果，从而得到更佳纯粹的信号。

以 `anl4_rd_exp_low` 数据为例：一般来讲市值越高的公司 R&D 数据会越高，且分析师更愿意去分析考虑高市值的公司。通过回归可以很好消除这个影响，这个信号我测试如果不回归的话，sharpe 值会下降到1.03。除了这个例子，我发现分析师横截面比较的信号，剔除市值影响后，都会有一定程度的提升。 
> [!NOTE] [图片 OCR 识别内容]
> Simulation 3A
> Simulation 38
> Settings
> USA/D1/TOP3000
> Streak: 11
> 叫 IS
> Summary
> Period
> IS
> 0s
> 1
> financial_data
> ts_backfill(anl4_rd_exp_low
> 256) ;
> 2
> signal
> group_scale(financial_data,
> Aggregate
> Sharpe Turnover
> Fitness
> Returns
> Drawdown Margin
> pv13_h_minz_focused_pureplay_3000_sector) ;
> Data
> 1.561.9191.075.9093.33961.90%o。
> 3
> signal
> regression_proj (signal,
> rank(cap) )
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Coun
> 2013
> 1.50
> 2.24%
> 0.93
> 4.76%
> 2.46%
> 42.429。
> 132C
> 2014
> 2.20
> 1.899
> 1.72
> 7.619
> 1.43%
> 80.51%oo
> 1462
> 2015
> 1.49
> 1.879
> 0.89
> 4.51%
> 1.81%
> 48.159oo
> 157
> 2016
> 0.45
> 2.14%
> 0.16
> 1.509
> 3.129
> 14.049oo
> 1576
> 2017
> 2.39
> 1.799
> 1.90
> 7.939
> 1.459
> 88.66%o。
> 1516
> 2018
> 0.11
> 1.939
> 0.02
> 0.389
> 2.56%
> 3.909oo
> 1586
> 2019
> 0.69
> 1.849
> 0.28
> 1.999
> 1.499
> 21.639o。
> 1471
> 2020
> 0.34
> 1.989
> 0.11
> 1.349
> 2.899
> 13.5390。
> 130
> 2021
> 2.77
> 1.749
> 2.81
> 12.86%
> 3.33%
> 147.5796o。
> 1265
> 2022
> 2.79
> 1.699
> 3.13
> 15.71%
> 3.16%
> 185.899o。
> 134
> 2023
> 1.14
> 1.36%
> 0.80
> 6.21%
> 1.039
> 91.30%o。
> 124C
> Clone this Alphaina new tab
> day


### 产出效果

在 anl4 遍历了一万多，能交 ppa 的有不少。

### 后续

1. 有可能会有比【市值】更好衡量这种偏见的字段，也就是替代 rank(cap)；2. 或者再去套 trade when。我也想知道有没有办法能再去提升这个信号，如果大家有什么想法也可以一起交流谢谢🙏

---

### 评论 #31 (作者: WL13229, 时间: 11个月前)

[顾问 MQ62208 (Rank 29)](/hc/en-us/profiles/27263578312727-顾问 MQ62208 (Rank 29))   [LM81527](/hc/en-us/profiles/27707767300503-LM81527)

深度不足 请更换更有数据集特征或效果更强的模板。

---

### 评论 #32 (作者: WL13229, 时间: 11个月前)

[LL49894](/hc/en-us/profiles/30413446999703-LL49894)

日频更新的数据，经过你的处理，它变成了一个turnover很低的alpha，可以仔细探索一下，是哪一步使得它turnover降低这么多。

---

### 评论 #33 (作者: KD86036, 时间: 11个月前)

**1.idea** :探索新闻数据集与量价数据集之间的相关性。

**2.模板** ：<group_operator/>(ts_corr(<news18_field/>,<pv1_field/>,<days/>),densify(<group/>))

**3. 模板总共包含五个变量**

<group_operator/>:"group_neutralize","group_rank", "group_scale", "group_zscore"；

<news18_field/>：此处只针对news18martrix数据集,共有59个数据字段；

<pv1_field/>："returns";

<days/>：120，252

<group/>:"industry","country"等常规分组数据字段共36个；

**4.搜索空间大小**

共形成16992个表达式，其中sharpe1.58以上大概1%左右，我最终提交alpha共有3个。

**5.模板的idea，implement细节**

<group_operator/>(ts_corr(<news18_field/>,<pv1_field/>,<days/>),densify(<group/>))，该模板核心主信号：ts_corr(<news18_field/>,<pv1_field/>,<days/>)，探索新闻数据字段对回报率或者收盘价的潜在预测影响，然后通过二阶分组操作符进一步增强确实有相关性的alpha的信号

**6.产出效果展示**

此处不好展示图片，我口述相关参数设置和指标，

参数设置：EUR,TOP2500,COUNTRY,DECAY(5),DELAY(1);

相关指标：sharpe1.92,turnover4.28%,fitness1.18,returns4.73%,drawdown3.62%, margin:千分之22.11;

相关性：当时提交自相关性很低，并且pro相关性至今都有0.54，看来这个模板还没被大佬们挖掘。

**7.后续拓展计划**

ts_corr是否可以换成ts_co_skewness;

group操作符不要局限以上四种，根据自已的级别全部拉满；

除了回报率，收盘价等其它量价数据代入是否有信号；

目前我只在欧洲区域尝试，USA,GLB和ASI尚未挖掘，欢迎各位大佬一起共同探索。

---

### 评论 #34 (作者: LM81527, 时间: 11个月前)

模板
tg=ts_regression(<ts_operator1/>(<analyst_metric/>, <window_days1/>), <ts_operator1/>;(<pv_metric/>, <window_days1/>), <window_days2/>);
gp = group_cartesian_product(country, industry);
-<ts_operator2/>(<group_operator/>(tg, gp), <window_days2/>)

模板中的变量使用< />进行了声明，总共三个变量。
具体变量1：<ts_operator1/>、 <ts_operator2/>: 即时间序列操作符，如ts_mean、ts_returns、ts_rank、ts_zscore等
具体变量2：<analyst_metric/>: 分析师数据，可选择覆盖率较高且已组alpha较多的字段
具体变量3：<window_days1/>、<window_days2/>: 时间窗口，可选为5，20，60，120，252等，且要求<window_days2/>   >   <window_days1/>
具体变量4：<group_operator/>: 分组操作符，如group_mean、group_rank、group_zscore等

搜索空间的大小：以数据集analyst69为例，选择region为EUR且universe为TOP2500，覆盖率大于90%且已组alpha数量大于100个的字段有192个，搜索空间大约是192*3*3*3*10=51840

模板的idea，implement细节：该模板借鉴了weijie老师推荐使用的工具中的适用于GLB地区的双重中性化模板，在认真研究并且实际跑过这个模板之后，我发现这个模板产出率和产出的alpha质量还不错，便有意在此模板基础上进行拓展。原模板中使用的是anl69的vec数据，这次我便针对anl69的matrix数据进行了研究，在lab上查看了一些字段的更新频率、分布和区间等等，并根据工具推荐使用了ts时间序列操作符进行处理。加上在论坛查看帖子时，留意到了ts_regression这个操作符，便通过回归分析来寻找分析师数据和市场价格、市值等daily更新的价格因子的关系，以期在股票市值高于分析师预期时卖出，低于预期时买入，获得收益。
产出效果：我尝试了1840次回测，有16个可以提交的Alpha，下面是其中一个的表现（ 历年表现表格数据和pnl，sharpe和turnover ）


> [!NOTE] [图片 OCR 识别内容]
> tts_regression(ts_mean (anl69_aeps_expected_report_dt,
> 252),
> mean(CIose, 252),
> 252);
> Broup_cartesian_product (country, industry
> ZSCore(Broup_ZSCore 圯,即)
> 252 )
> Simulation Settings
> Instrumant TyPa
> Reqion
> Unmgrsg
> Languaga
> Dcay
> Dalay
> Trmcation
> Nautralizaton
> Pastaurizalon
> NaN Handling
> Unt
> Handling
> Ma Trada
> Equity
> EUR
> T0P2530
> Fas-
> Expression
> 0.05
> Indusiny
> Verify



> [!NOTE] [图片 OCR 识别内容]
> OOOK
> S0oK
> OOoK
> SOOK
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
> IS Summary
> Period
> 05
> 眙 Power Pool Alpha
> Pyramid theme: EURIDIIPVxI
> Pyramid -heme; EURIDTIANALYST x1.5
> Aggregate Data
> Sharpe
> TMTnOE
> CITMS
> RaTCm 
> UCa'TUI
> Warsir
> 1.28
> 3.20%
> 0.61
> 2.84%
> 2.329
> 17.739600


建议其他顾问未来尝试的探索方向: 该模板在EUR地区时使用的是country和industry，可以考虑使用market、subindustry等中性化选项；目前在anl69上表现良好，可以考虑在其他分析师数据集甚至mdl、fnd等数据集。

---

### 评论 #35 (作者: WL13229, 时间: 11个月前)

最近看到一些跟量价有关的regression。一般来说，总能出Alpha，但还是谨慎使用，不要交太多这种，因为它本质还是一个量价的alpha.

---

### 评论 #36 (作者: WL13229, 时间: 11个月前)

[LM81527](/hc/en-us/profiles/27707767300503-LM81527)

拓展得很好。但是analyst69是个很好的数据集，太好出了。不要一个季度在这里交太多。分散

---

### 评论 #37 (作者: WL13229, 时间: 11个月前)

随手分享一个来自热心顾问的小小数据探索模板，他说这个称不上完整，但是很适合探索新数据。且不参与征文，故对格式就不严格要求了。👇代发内容如下

> zscore(ts_delta(rank(ts_zscore(datafield,60)),5))

上文中的模板op可以进行替换，时间参数也应该针对不同数据集进行合理替换.

---

### 评论 #38 (作者: SQ15289, 时间: 11个月前)

模板

```
<group_operator/>(<cross_sectional/>(<fundamental/>/cap),<group/>)
```

- 具体变量<fundamental/>建议是与公司的财务挂钩的因子，这里的思路是，如果在市值相同的情况下，如果公司财务越高，那么就代表这个公司有增长潜力，由此反推；对于cap这个因子我还有一些别的想法比如使用close，high，low，open，sharesout这些能代表市场的因子作为分母替换掉cap，不过在这个模板中我只使用了cap作为主要使用的实验对象，<fundamental/>使用了fundamental17数据集

- <cross_sectional/>使用了rank和quantile，两个操作符都可以让信号都会根据一组数值的大小关系来处理每个数据，而在lab中查看fundamental17和cap的因子数据会发现他们大多数集中在0的附近，但还有一些极端值在很远的地方，因此使用这种可以让数值排序后消除原始数值的绝对大小差异，保留了相对顺序，以确保不会丢失信号，也不会因为极端值受到大的影响
  
> [!NOTE] [图片 OCR 识别内容]
> le6
> fd17 rhsfcq
> 12
> 1.0
> 0.8
> 
> 0.4
> 一2.5
> 一2.0
> 一1.5
> 一1.0
> 一0.5
> 0.0
> 0.5
> Values
> le6

  
> [!NOTE] [图片 OCR 识别内容]
> Ie6
> 2.5
> 2.0
> 1.5
> 
> 1.0
> 0.5
> 1.0
> 1.5
> 2.0
> 2.5
> 3.0
> Values
> Ie7

- <group_operator/>使用了group_scale和group_neutralize两个操作符，使用group_scale是因为前面已经让数值消除了原始数据的绝对大小，那么在这里可以统一公司的标准，从而更好的了解那个公司更有潜力；group_neutralize就是为了消除一些market，industry之类的影响；当然这里也建议使用别的group类型的操作符

- <group/>使用了常用的market，sector，country，market分组还有一些为close，returns和split的桶分组，这里也建议试试别的分组方式

以EUR,TOP3000的fundamental17数据集为例：
数据集因子有367，<cross_sectional/>使用2个，<group_operator/>使用2个，分组弄了7个，因此搜索空间为10276，我运行完按照ra的标准进行筛选ppac并且没有任何的warning情况下有30多个为合格

下面是我拿出的一个alpha的数据给大家展示


> [!NOTE] [图片 OCR 识别内容]
> Code
> group_scale(quantile(fndl7_rhsfcqlcap
> densify (bucket
> rank(adv2o) _
> range='0.1,1,0.1')))
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
> Handling
> Unit Handling
> Max Trade
> Equitj
> EUR
> TOP2500
> Fast Expression
> 0.08
> Country
> Region
> 0n
> On
> Verify
> On
> NaN



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
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
> 1.86
> 3.9396
> 1.49
> 7.9896
> 6.4296
> 40.629600
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
> 3.73
> 5.4095
> 3.76
> 12.73%
> 1.2190
> 47.19960
> 570
> 2014
> 448995
> 1.40
> 6.5596
> 2.4996
> 29.279600
> 887
> 650
> 2015
> 2.89
> 3.9795
> 2.89
> 12.51%
> 1.8796
> 63.079000
> 900
> G2
> 2016
> 3.7195
> 1.52
> 8.50%
> 3.48%
> 46.349300
> 381
> 629
> 2017
> 3.75
> 3.6395
> 3.47
> 10.7096
> 0.9795
> 59.0096oo
> 79
> 659
> 2018
> 0.35
> 3.5295
> 0.11
> 1.2796
> 3.10%
> 7.259600
> 002
> 707
> 2019
> 3.4095
> 5.18%6
> 1.959
> 30.259600
> 930
> 680
> 2020
> 0.36
> 0995
> 0.15
> -2.04%6
> 5.939
> 9.993600
> 366
> 698
> 2021
> 0.05
> 3.2395
> .01
> 0.20%
> 0.5590
> 229000
> 318
> 765
> 2021
> 4.02
> 3.6795
> 4.50
> 16.39%
> 8796
> 89.329600
> 953
> 744
> 2022
> 3.569b
> 1.20
> 8.7996
> 4.7990
> 49.329600
> 716
> 2023
> 0.90
> 3.2595
> 0.59
> -5.3496
> 3396
> 32.839600
> 851
> 671
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.25
> 3.9396
> 0.57
> 2.63%
> 3.979
> 13.419600



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 70OOK
> OOOK
> SOOOK
> 40OOK
> 300Ok
> ZOOOK
> 0OOK
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
> Pnl
> Risk Neutralized Pnl
> MNMUA


---

### 评论 #39 (作者: JL98779, 时间: 11个月前)

**模板（在EUR, TOP2500進行測試）**

```
min(<group_op/>(<fnd28_matrix/>, <oth455_group/>), <ts_op/>(<fnd28_matrix/>, <window/>))
```

**具體變量賦值：**

- group_op：group_rank, group_zscore, group_quantile, ...
- fnd28_matrix：基本面數據集fundamental28（Global Fundamental Data）的matrix, 如fnd28_value_05191q（用來計算季度EPS的普通股數量）
- oth455_group：其他數據集other455（Relationship enhanced with AI/ML）的group, 如oth455_partner_roam_w1_kmeans_cluster_20（合作夥伴的分類）
- ts_op：可以是ts_rank, ts_zscore,  甚至是ts_quantile, ts_std_dev, ...
- window：用來比較時間數據的窗口，推薦使用252, 504

**注意：** 最好在使用group_rank時也使用ts_rank，group_zscore時也使用ts_zscore，如此類推。

**搜索空間的大小：** 1655（fnd28） * 1200（oth455）* 3（ops）* 2 （window）~ 11,916,000，當中不少fields的users只有一至兩個，發掘潛力無限

**模板的idea，implement細節：** 我們要求該公司的fnd28數據在競爭對手中或合作夥伴中有較高排名， **同時** 亦較以往的表現有進步。因此，使用min(signal1, signal2)來達到上述效果。alpha中主信號來源於fnd28，通過group_op進行group内比較，通過ts_op與該datafield的過往表現進行比較，再運用min取兩者最小值，決定該股票的權重。

**產出效果：** 測試了400多個alpha，有5個可提交PPAC的，他們的PnL也很高


> [!NOTE] [图片 OCR 识别内容]
> VI0  WorldQuant
> Version control
> maln
> 》
> Project
> apLPy
> maln py
> 三 alpha_2025_07_27_231223.CSV
> alpha_zUzb_UI_T8_2CSV
> 一@
> 』 D 邑
> CSV
> 山  心  ` |
> 品
> 三 alpha_2025_07_18_3
> CSV
> 三 alpha_2025_07_19_1.CsV
> alpha_id 孓
> Sharpe
> Fitness
> Turnover
> Returns
> Pnl
> 三 alpha_2025_07_20_
> CSV
> I2njgAm
> 1.31
> 1.68
> 3.99
> 20.48
> 21139345
> 三 alpha_2025_07_20_2.CsV
> L21ZV16
> 1.13
> 1.06
> 3.06
> 10.97
> 11323568
> 三 alpha_2025_07_20_3.CsV
> E2rRUXG
> 1.11
> 1.22
> 7.5
> 15.16
> 15655915
> 三 alpha_2025_07_21_1.CsV
> A203jxq
> 1.07
> 0.98
> 3.25
> 10.44
> 10774725
> 三 alpha_2025_07_21_213338.CsV
> jdgVN5
> 1.03
> 1.63
> 7.48
> 31.47
> 32485945
> 三 alpha_2025_07_22_155329.CsV
> QO5VA9K
> 0.99
> 1.17
> 5.68
> 17.42
> 17979334
> 三 alpha_2025_07_22_181754.CsV
> IXIIGKqd
> 95
> 0.8
> 8.94
> 9225474
> 三 alpha_2025_07_22_184023.CsV
> 三 alpha_2025_07_23_000459.CsV
> 0257NJd
> 0.92
> 0.65
> 6356862
> 三 alpha_2025_07_23_121456.CsV
> ZLJKHIKV
> 0.87
> 0.76
> 3.89
> 9960448
> 三 alpha_2025_07_23_142213.CsV
> I2NJpN6
> 0.86
> 1.16
> 22.78
> 23514678
> 三 alpha_2025_07_23_214005.Csv
> OaKpKe8
> 0.42
> 5.33
> 3096666
> 三 alpha_2025_07_24_123431.CsV
> 12
> E2zrlpnJ
> 0.81
> 0.42
> 3.43
> 3539306
> 三 alpha_2025_07_24_195935.CsV
> 13
> VOJ2IIOA
> 0.8
> 0.55
> 3.05
> 5.96
> 0151883
> 三 alpha_2025_07_25_130100.CsV
> 14
> 92AXZMK
> 0.76
> 0.34
> 2.51
> 2.54
> 2625366
> 三 alpha_2025_07_25_144728.CsV
> 15
> eWIqOAPE
> 0.75
> 0.39
> 2.25
> 3.32
> 3422673
> 三 alpha_2025_07_25_234410.CsV
> 三 alpha_2025_07_26_192941.CsV
> UNROV55
> 74
> 0.77
> 13.51
> 12922273
> alpha_2025_07_27_231223.CsV
> 72KWHIZb
> 0.74
> 0.82
> 6.66
> 15.44
> 15938367
> configjson
> VRYPnEO
> 0.74
> 0.62
> 4.0
> 8.72
> 8999784
> aplpy
> J25GnYx
> 0.73
> 0.55
> 3.48
> 7.09
> 7314893
> bot py
> dPLdLdY
> 72
> 11751229
> Client py
> L2lNXr2
> 0.72
> 0.52
> 6.6
> 0.59
> 6805372
> maln py
> 0k9Y006
> 0.71
> 0.28
> 8.3
> 1.99
> 2057457
> requirementstxt
> Okgoj3
> 0.71
> 0.52
> 4.04
> 0.58
> 6795536
> External Libraries
> Scratches and Consoles
> ZNRVZOA
> 0.71
> 0.55
> 5.11
> 7.53
> 3472497
> Text
> Data
> WorldQuant
> alpha_records
> 三 alpha_2025_07_27_231223.CsV
> SUM: 1.13
> 2:2
> Python 3.12 (WorldQuant)



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> 们Power Pool Alpha
> Pyramid theme: EURIDTIFUNDAMENTAL %1.1
> Pyramid hemE: EURIDIIOTHER X1.7
> Aggregate Data
> ShSTO=
> TUTTTU「
> Fitness
> RECUFns
> UTaTTITT
> Tren
> Simulation Settings
> 1.53
> 2.749
> 2.32
> 28.7996
> 31.649
> 210.239600
> Instrument Type
> Region
> Unierse
> LangVage
> Decay
> Dlay
> Truncatjon
> Newtraliation
> Pastewrialion
> NaN Handling
> Unit Handlng
> Equity
> TCP2500
> FastExCTESsIT
> 3.03
> Noe
> Verif
> Vear
> Sharpe
> Tumover
> Ftness
> Rewvrs
> Dawdown
> Margin
> Long Count
> Short Count
> 201
> 2.32
> 07
> 5.3
> ?Ru
> 12.52:
> SZESE
> 81
> 37
> 2014
> 2.5
> 3.5
> 27E
> E.50
> 257.57950
> 352
> Z05
> 1.55
> 寸
> 1.5
> 11.119
> 24.3汩
> 31.3E0
> Clone Alpha
> Z015
> 429
> 37.E39:
> SE:
> 311.30
> 20
> 0.3
> 1|TO
> DZE
> 6.539
> 23.50沿
> ES 230
> 2013
> Z35
> 23.03:
> 13.505
> 9190
> 1152
> Chart
> PIL
> 2019
> 339:
> 029:
> 1._
> 255.530
> 1123
> 2027
> 2.54
> 3.239
> 5.5
> 5.239
> 1.154
> 3030
> 107
>  _|
> 1.77
> 399
> SG:
> 1.;
> 50.5490
> 11
> ZON
> 2022
> ES%
> 2.52
> 33.539
> 1278治
> 143.200
> 1179
> 202
> 139:
> 146.01
> 03沾
> 33211
> 11
> 1
> Risk neutralized
> Data
> 3T
> TUCTII'P
> Firnssc
> TeTUCTS
> Cracn
> Msrein
> Aggr
> 0.66
> 2.74%
> 0.50
> 10.46%
> 37.63%
> 76.4
> 9ooo
> 2014
> 2015
> 2015
> 2017
> 2015
> 2019
> 2020
> 2021
> 2022
> 2023
> Investability constrained
> Aggregate Data
> SArCe
> TUTNIEF
> Fitness
> Returns
> UTOO
> Wrein
> 33
> 32300
> 5S
> 93900
> 090h
> 995opnn
> EBate


**建議其他顧問未來探索的其他方向：** 此模板產出的alpha sharpe並不算很理想。可以考慮在other455裏選出合適的group，或者對整個模板進行平截面處理，例如：

```
rank(min(<group_op/>(<fnd28_matrix/>, <oth455_group/>), <ts_op/>(<fnd28_matrix/>, <window/>)))
```

---

### 评论 #40 (作者: WL13229, 时间: 11个月前)

[SQ15289](/hc/en-us/profiles/28969190745367-SQ15289)

可以再想想办法 怎么拓展到cap以外的分母

---

### 评论 #41 (作者: WL13229, 时间: 11个月前)

[JL98779](/hc/en-us/profiles/31205672631319-JL98779)

可以继续想想办法 ；怎么拓展到其他数据集

---

### 评论 #42 (作者: YS42224, 时间: 11个月前)

```
自由现金流/市值模版:<group_operator/>(-<ts_operator/>(winsorize(ts_backfill(fndl_fcf/<market_capital>, 120), std=4), 60),densify(<group/>))
```

- - 模板中的变量使用 **< />** 进行了声明，总共五个变量。
  - 具体变量1：< **fndl_fcf** />: 可以包含所有自由现金流(fcf)有关的字段
  - 具体变量2：< **market_capital** />: 可以所有和市值有关的字段
  - 具体变量3：< **group_operator** />: 可以对组间进行计算的分组运算符，例如group_rank, group_zscore, group_neutralize等
  - 具体变量4：< **ts_operator** >：时序字段,ts_zscore等
  - 具体变量5：< **group/** >:group 分组;
  - 搜索空间的大小：以数据集Eur Fnd17为例的话，大约是30个
  - 模板的idea，implement细节：单因子回测，发现fnd17_fcfmtt因子质量比较好，看了下解释，是最近A股比较火的自由现金流类因子，在海外市场确实也比较靠谱。通过deepseek搜索了一下，给出了和其他因子的组合，这里选择自由现金流/市值（FCF/Market Cap）​，​逻辑​是衡量公司自由现金流相对于市值的“含金量”，识别高现金流低估值的企业。​应用场景​：价值投资策略，筛选被市场低估的高现金流公司。
  - 之后对主信号做风险因子的中性化处理（类似于neutralization里的RAM,statistical等);
  - 产出效果：我尝试了180次回测，有15个可以提交的Alpha。
  - 建议探索方向: 自由现金流因子与其他因子组合，符合基本面逻辑的方向。

---

### 评论 #43 (作者: WL13229, 时间: 11个月前)

[YS42224](/hc/en-us/profiles/29028830626711-YS42224)

缺乏深度，与课程材料无大差别

---

### 评论 #44 (作者: YH82809, 时间: 11个月前)

低波动高成交组合策略模板

process_price = winsorize(ts_backfill(<price_datafield/>,<backfill_windows/>),std=4) ;  
process_volume = winsorize(ts_backfill(<volume_datafield/>,<backfill_windows/>),std=4) ; 
process_datafield = winsorize(ts_backfill(<datafield/>,<backfill_windows/>),std=4) ;

gp = group_cartesian_product(country, sector) ;

input1 = and( ts_std_dev(process_price, <short_day/>) < ts_std_dev(process_price, <long_day/>), ts_mean(process_volume, <short_day/>) > ts_mean(process_volume,<long_day/> )) ;

input2 = and( ts_std_dev(process_price, <short_day/>) > ts_std_dev(process_price, <long_day/>), ts_mean(process_volume, <short_day/>) < ts_mean(process_volume,<long_day/> )) ;

alpha = <ts_operator/>(<group_operator/>(process_datafield, gp), <window/>) ; 

if_else(input1,alpha,if_else(input2,-alpha,-1))

1. 模板中的变量使用< />进行了声明，总共9个变量，3个数据集变量，2个操作符变量，4个时间窗口变量；
变量<price_datafield/>     4  
变量<volume_datafield/>    3
变量<datafield/>           12
变量<backfill_windows/>    2
变量<short_day/>           1
变量<long_day/>            2
变量<ts_operator/>         11
变量<group_operator/>      4
变量<window/>              2

2. 搜索空间的大小

以asi pv1 数据集为例，按照上述的每个变量的数量，产生的组合为4*3*12*2*1*2*11*4*2 = 50688个，随机抽取5000个进行回测，目前回测了323个。

3. 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）

3.1 Idea: 通过股价的波动和成交量的变化来捕捉alpha信号。

核心逻辑
本模板结合“低波动高成交”（风险-流动性因子）与“分组因子增强（动量因子），构建Alpha信号。具体逻辑如下：

低波动：短期波动率（<short_day/>天）低于长期波动率（<long_day/>天），表示价格波动趋稳，风险较低。
高成交：短期成交量（<short_day/>天）高于长期成交量（<long_day/>天），表示市场关注度提升，流动性改善，推动价格上涨。
分组因子增强：对“低波动高成交”的股票，按行业×市值交叉分组，计算组内动量因子（<datafield/>）的均值，再通过时间序列排名（<ts_operator/>）生成Alpha信号（排名越高，信号越强）。
经济含义
低波动高成交：筛选出“风险低、易交易”的股票，符合投资者的“安全边际+流动性”需求。
分组因子增强：通过行业×市值分组，消除因子的“风格偏差”，提升信号的纯度。

4. Implement细节:
4.1 数据处理（预处理步骤）
填补缺失值：用ts_backfill(<price_datafield/>,<backfill_windows/>)填补价格数据集的缺失值（如前5天均值）；同理处理成交量和动量因子。
处理极端值：用winsorize(..., std=4)将有关价格数据、有关成交量及有关动量因子的极端值缩尾到4倍标准差范围内（去除异常值，如跳空缺口）。
4.2 主信号条件（input1）
input1是低波动高成交的条件组合，用and连接两个子条件：
子条件1（低波动）：短期价格标准差（<short_day/>=5天）低于长期收盘价标准差（<long_day/>=20天，60天等），表示波动趋稳。
子条件2（高成交）：短期成交量均值（<short_day/>=5天）高于长期成交量均值（<long_day/>=20，60天等），表示流动性提升。

4.3 Alpha信号生成
分组计算：用group_cartesian_product(country, sector)生成地区×行业交叉分组,构建“地区+行业”双维度的同质群体，解决因子投资中的偏差问题（地理地区偏差、行业偏差），提升因子信号的纯度与稳定性。
因子增强：用group_operator(<datafield/>, gp)计算每个分组内的动量因子，消除风格偏差。
时间序列排名：用ts_operator(<group_operator_result>, <window/>)对分组动量均值做不同时间的滚动排名（ts_rank），生成Alpha信号（排名越高，信号越强）。

4.4 多空判断
用if_else(input1,alpha,if_else(input2,-alpha,-1))区分多空：

做多：input1成立（低波动高成交），用Alpha信号（alpha）表示做多强度（排名越高，仓位越重）。
做空：input1不成立,input2成立（高波动低成交），用-alpha 表示做空（固定仓位）。
-1 : 空仓，或平仓出局。

5. 产出效果（回测结果）
回测设置
数据集：用asi pv1 数据集。
时间范围：2013年1月1日-2023年12月31日（10年，覆盖牛熊周期）。

回测结果

Alpha数量：回测了323个参数组合，目前只发现一个可以提交的。信号有点弱。具体表现如下：

说明一下：一张图片只有22.4K左右，一直上传不上来，如果需要我再上传。

6. 未来探索方向
因子扩展：将<datafield/>从“动量因子”扩展到“价值因子”（如PE ratio）或“盈利因子”（如ROE），验证不同因子的分组增强效果。
分组优化：用group1/group2,优化group_cartesian_product（交叉分组），更灵活地划分股票组（如按行业+子行业等）。
信号过滤：在input1中加入“动量条件”（如过去1个月收益率>0），筛选“低波动高成交+高动量”的股票，提升收益。
地区扩展：将<region/>从USA扩展到EUR或Asia或GLB等，验证策略的跨地区有效性。

由于以前都是用平台，老师，以及大佬们的模板，不知道如何把想法结合经济含义，来表达alpha， 这个也是模仿着粗糙成型，请大家多多指教。

---

### 评论 #45 (作者: WL13229, 时间: 11个月前)

[LL49894](/hc/en-us/profiles/30413446999703-LL49894)

ts_corr计算的是相关性，如果数据点太少，计算出来的数值可能不稳定或者缺乏统计学意义。虽然这个alpha是做出来了，但是从数学上的稳健性还有提升空间

---

### 评论 #46 (作者: WL13229, 时间: 11个月前)

[YH82809](/hc/en-us/profiles/30611282193687-YH82809)

有心了，是个好作品。希望能看到图片

---

### 评论 #47 (作者: WY38139, 时间: 10个月前)

<scale_down/scale/rank/>(quantile(<risk_option_datafield/>, driver="cauchy") * ts_std_dev(<risk_option_datafield/>, <days/>),  constant=0 )

- 模板中的变量使用 **< />** 进行了声明，总共三个变量。
- 具体变量1：<scale_down/scale/rank/>: 包含scale_down,scale或rank
- 具体变量2：<risk_option_datafield/>: 可以包含所有风险字段或期权字段
- 具体变量3：<days/>: 用于计算波动率的天数，可设为[5, 22, 60, 120, 250]

- 搜索空间的大小：以数据集risk70为例的话，大约是32*3*5
- 模板的idea：
- 1.通过分位数映射增强极端值区分度，乘以波动率放大高波动区间的信号；
- 2.截面缩放至[0,1]避免过拟合。

该模板是之前kunqi 老师分享的模板，喂给ai后联想生成的新模板。实践证明risk字段和option字段使用此模板搜索可以直接得到ppac标准的alpha，且相关性与使用同字段生成的组平均差模板alpha相比较低，且turnover和return会更高。

根据描述，容易出现极端值的且波动率差异较高的数据应该都适用于此模板。

---

### 评论 #48 (作者: 顾问 QX52484 (Rank 35), 时间: 10个月前)

```
多NAN值处理模板:-ts_count_nans(<cross_op/>(ts_backfill(<data_field/>, 5)), 5)
```

具体变量1：<data_field/>: 缺失值较多（>5%?）的数据集

具体变量2：<cross_op/>: 处理横截面的quantile,winsorize等。

以USA TOP3000的mdl211_delta_netq_q1_mae为例，通过lab查看数据存在大量的nan数据。 
> [!NOTE] [图片 OCR 识别内容]
> What % of mdl2ll_delta_netq_qI_mae Values are NaN or zero?
> 100
> perceni_nan
> NM
> percen_ZrO
> 
> 201
> 2016
> 2018
> 2020
> 2022
> Dale
> ITyOU see that percentage Of NaN Values Is high
> Use backtll operators


如果简单进行回填处理，不能出现信号。 
> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1TTOP3000
> BOOK
> Streak: 92 day
> Winsorize(ts_backfill (ndl211_delta_netq
> mae
> 120),
> std-4 )
> TOOK
> GOOK
> SOOK
> LOOK
> 3OO
> ZOOK
> 1OOK
> 1OOI
> 2012
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> PnL
> Risk Neltralized PIL
> IS Summary
> Period
> 眙 Sirgle Data Set Alpha
> Aggregate Data
> SaTC
> TUFNOET
> IIeS
> TECUTI
> UF3wdoIn
> Marsin
> 0.35
> 6.229
> 0.10
> 0.979
> 8.479
> 3.139600
> 7023


使用ts_count_nans符号后，得到明显优化


> [!NOTE] [图片 OCR 识别内容]
> Simulaton 5D
> Simulation SF
> Simulation 5G
> Settings
> USA/D1TTOP3O00
> Streak: 92 day
> 7OOOK
> Count
> nans (ts_arg_max(winsorize(ts
> backfill (mdl211_delta_netq_ql
> maey 120), std-4)
> 120),5)
> OOOK
> 5OOOK
> LOOOK
> 30OOK
> 20OOK
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
> Pnl
> Risk Neutralized Pnl
> IS Summary
> Period
> _ Single Data Set Alpha
> Aggregate Data
> Sh3rO
> LUFMOIEr
> HIMeSs
> Returns
> UraWJUMIT
> MMarsin
> 1.59
> 1.4296
> 1.41
> 9.81%
> 9.91%
> 138.519600
> 7023


如果只进行ts_count_nans 效果不明显。猜测可能是先进行ts_back回填，数据整体会更加平滑。


> [!NOTE] [图片 OCR 识别内容]
> Simulation 4F
> Simulation 48
> Simulaton 4C
> Simulation 40
> Simulation 4
> Simulation 46
> Simulation 4H
> Settings
> USA/D1TTOP3000
> LOOOK
> Streak: 93 day
> ts
> Count_nans (mdl211_delta_ebtq_ql
> mae,120)
> 3,50OK
> 30OOK
> 25OOK
> 20OOK
> SOOK
> OOOK
> SOOK
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
> PnL
> Risk Neutralized Pnl
> IS Summary
> Period
> Single Data Set Alpha
> egate Data
> Sharpe
> TICNT
> Sitms
> RaTlrn=
> Drawdown
> Marein
> 0.86
> 2.4796
> 0.52
> 4.589
> 8.959
> 37.149600
> ABBr


## 产出效果

对含nan值较多的数据集都能取得明显提升，对于实例的mdl211数据集，mdl211_delta_netq_q[1-4]_mae，能作为PPA进行提交，这几个数据字段几乎完全一样，会卡自相关性。

##建议其他顾问未来尝试的探索方向:

尝试to_nan等nan相关的操作符（我这gold菜鸡没有），信号增强。我尝试了sign_power，group的方式，但相交ts_count_nan处理后都没有明显变化。可能主体的变化已经通过ts_count_nan转化实现。另外，对于这样数据集已大幅nan的数据集进行这样数据处理后是否有值得探索的价值也需要探讨。

---

### 评论 #49 (作者: 顾问 SJ65808 (Rank 20), 时间: 10个月前)

### 模板

```
<data_field/> / group_sum(<data_field/>,<gp/>)
```

- 变量说明：< **data_field/** >结合大模型的说明最好是具有 **可加性数值指标，即指标加和之后具有一定经济学含义；**   **<gp/>** 常见分组即可
- **搜索空间** :为了点塔，data_field这边选择了EUR地区所有字段大类(除了fnd,mdl外)产出alpha数量最多的前20个字段，gp选择了market,group_cartesian_product(country, industry)两个，最终进行了2338次回测
- **Idea** ：这是一个atom类通用型模板，主要计算指标在一组内占比，可作为0阶使用，出了信号之后结合ts、group操作做进一步增强
- **产出效果:**  以shape>1.2且fitness>0.7(shape<-1.2且fitness<-0.7)为界最终产出71个有信号的alpha，其中存在不少重复的，去重之后发现pv、anl、shortinterset类均有产出。其中有些甚至直接可以提交： 
> [!NOTE] [图片 OCR 识别内容]
> Settings
> EURIDITTOPZSOO
> Convet to Mulli Simulaton
> Steak 265
> IS Summary
> Paria0
> -ts_backfill(vec_min
> Broup_sUm(ts_backfilI(VeC_min
> 20),Rarket )
> ASinsle Data Sst JIpna
> ABEregatE
> Tat
> Shalpe
> OTTU
> 1TUIT
> Mryr
> 1.85
> 5.099
> 1.43
> 7.5296
> 9.46%
> 29.579600
> Ter
> Shape
> Tumoer
> Fmes
> Relum
> IVo
> Margin
> Long Cont
> Shor Count
> 2013
> 564
> 1
> C
> 1143
> 132
> 4714
> 10.914
> 2239
> U
> 1773
> 2015
> J
> 934
> TO
> 33
> 4.652
> 3.924
> .6y
> 159
> 2017
> 434
> 7.35乩
> 1
> 353
> 2J07
> 2013
> 45比
> 119
> 2.SB
> 77
> 135
> 2019
> 464
> 一
> 3.114
> TJL
> 13
> 2020
> T!
> 534
> 牛
> 2232:
> 2021
> T
> 5.04
> JCC
> 14 5
> 1027
> 2022
> 594
> 1 -
> 3414
> L 
> 1959
> JJ6
> 16
> TIOu
> 匡 Correlation
> Self Correlation
> 415TTTUI
> UTTITTIITT
> Pne|
> TOrFLTiI
> 415TTTUI
> UTTITTIITT
> Prnd Crreltinn
> 415TTTUI
> UTTITTIITT
> IS Testing Status
> P-55
> O-OhT
> o

- **后续**

1. 字段方面:fnd里面应该不少这种具有可加性的字段，本人由于fnd要被禁用了，所以没有进一步搜索，期待其余大佬的发现，再一个news,snt一些得分字段可能也有用，我目前没有跑出来，可能是搜索字段不足，准备进一步搜索试试
2. 操作符方面:group_sum 可以替换成 group_mean、group_median等分组统计类操作符，也可以考虑时间序列ts_sum等
3. region方面:该模板比较通用，经济学含义也比较简单，应该都可以尝试

---

### 评论 #50 (作者: WH74165, 时间: 10个月前)

WL13229

在您的模板中，您使用了下列式子来衡量波动变化。

> decorrelator = 1 / (1 + abs(ts_delta(iv_difference, 5)));

请问为什么不使用decorrelator = 1 / (1 +ts_std_dev(iv_difference, 5));呢？求教

---

### 评论 #51 (作者: LR23136, 时间: 10个月前)

尝试对 shortinterest2 进行探索

```
gp = group_cartesian_product(<g1/>, country);<g_op/>(<t_op/>(<shortinterest2/>, 5), gp)
```

具体变量1：<g1/>: 就是所有能用的group字段，包括Price Volume与shortinterest2
具体变量2：<g_op>: 可用的group操作符
具体变量3：<t_op/>: 可用的time操作符 天数为5
具体变量4：<shortinterest2/>: shortinterest2里非group字段
搜索空间的大小：大约是51 × 6 × 16 × 6 = 29,376
模板的idea，implement细节：作为Short Interest 里唯一个数据集，shortinterest2本身就是个模型（描述翻译：这是一个模型数据集，提供股票的卖空兴趣数据。它主要涵盖美国股票，但在其他地区也有一定程度的覆盖。投资假设表明，被卖空股份数量较多 / 较少的股票，其表现将逊于 / 优于同类股票。该数据对不同国家、市值和行业类别的卖空兴趣水平进行了标准化处理，还提供了股票的机构持股比例、波动率水平和空头挤压水平。）既然这样，那直接试试ts_rank再来个group_rank排一下序，再扩散至能用的time操作符与group操作符看看有没有惊喜

产出效果：目前已经跑了200+，有5个可行的


> [!NOTE] [图片 OCR 识别内容]
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> SeeC
> SeeC
> 08/13/2025
> 08/13/
> SeeC
> SCeC
> 28
> 28
> SeeC
> Regular 
> UNSUBMITTED
> 08/13/2025 EDT
> GLB
> T0PDIV3000
> 1.02
> 3.77%6
> 1.51%6 
> Regular 
> UNSUBMITTED
> 08/13/2025 EDT
> GLB
> T0PDIV3000
> 1.20
> 4.31%
> 2.2796
> Regular
> UNSUBMITTED
> 08/13/2025 EDT
> GLB
> TOPDIV3000
> 1.34
> 4.809
> 3.58% 
> Regular
> UNSUBMITTED
> 08/13/2025 EDT
> GLB
> TOPDIV3000
> 54
> 5.5396
> ,8296
> Regular
> UNSUBMITTED
> 08/13/2025 EDT
> GLB
> TOPDIV3000
> .64
> 5.89%
> 10.809
> Tag
  
> [!NOTE] [图片 OCR 识别内容]
> 即
> Broup_
> cartesian_product(currency , country ) ;group_neutralize(rsk7o_mfmz_Bemtrd_
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> MarEin
> Simulation Settings
> 1.64
> 10.809
> 1.13
> 5.899
> 4.499
> 10.929600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> GL3
> T0PDIV30O0
> Fast Expression
> 0.08
> None
> Off
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
> 3.40
> 11.98%
> 3.02
> 9.88%
> 1.3796
> 16.5096oo
> 595
> 720
> 2014
> 2.91
> 10.56%6
> 2.17
> 6.9290
> 1.3996
> 13.129600
> 749
> 793
> 2015
> 1.65
> 10.5996
> 03
> 4.859
> .5296
> 9.1
> 780
> 850
> Clone Alpha 
> 2016
> 0.29
> 10.5796
> 08
> 0.8990
> 2.7596
> 699603
> 759
> 831
> 2017
> .89
> 10.049
> 1.13
> 4.5096
> 50%6
> 8.97960
> 778
> 805
> Chart
> Pnl
> 2018
> 1.39
> 9.83%
> 0.80
> 4.1796
> 2.5696
> 8.49960
> 358
> 878
> 2019
> 0.46
> 10.119
> 0.15
> 1.2795
> 3.1196
> 2.519600
> 330
> 857
> 2020
> 1.00
> 10.26%
> 0.58
> 5.859
> 4.4996
> 11.41960
> 384
> 981
> 2021
> 3.58
> 11.679
> 4.12
> 16.569
> 2.5596
> 28.36960
> 1161
> 057
> 2022
> 1.90
> 12.40%
> 1.57
> 8.4996
> 93%
> 13.699603
> 030
> 1072
> 2,50OK
> 2023
> -11.24
> 10.79%
> 19.28
> 36.79%
> 2.31%
> 69o
> 990
> 957
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawoown
> Margin
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
> 0.65
> 5.399
> 0.26
> 1.939
> 4.999
> 7.159600
> 79o


先继续跑看看效果

---

### 评论 #52 (作者: LR93609, 时间: 10个月前)

**高产模版（轮动策略）**

```
<group_op/>(<ts_op/>(<datafield/>, <days1>), <group/>) - <group_op/>(<ts_op/>(<datafield/>, <days2>), <group/>)
```

- **变量1：** group_op 可以使用group_scale/rank/zscore
- **变量2：** ts_op可以使用ts_mean/rank/delta
- **变量3：** days1可以使用[63, 126, 252]
- **变量4：** days2可以使用[126,252,500]
- **变量5：** group可以使用[ 'subindustry', 'industry', 'market', 'country', 'exchange', 'currency', 'sector' ]

- **搜索空间：** 以数据集risk70为例的话，大约是32 * 3 * 3 * 3 * 7 = 6048
- **模板idea：**

1. **比较强弱：** 先对同一 group 内横截面标准化，再比较短、长两个周期的相对强弱。
2. **轮动信号：** 正值代表短期相对长期“过热”，负值代表“过冷”，可用于行业/风格/地域轮动策略。

**举例一：GLB nws23_acquiror_akw1rpa** 

 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Penod
> a=Vec_aVg(nws23_acquiror_akwlrpa);
> A Sinsle Dats Set Apha
> POWE  Po314pha
> FyraTdETe GLBIDTINEWS3
> bindustry;
> C-normalize (group_scale (ts_mean
> a,63),6)
> Broup_scale (ts_mean(a,252,6;
> ABBrEBate Data
> Sharpe
> Turnover
> FITnESS
> Rerurns
> Drawdown
> Marein
> Signed_power(CyI. 5)
> 1.14
> 7.22%
> 0.81
> 6,2590
> 5.90%
> 17.319600
> Sinulation
> Settings
> Vear
> Tuover
> Flmss
> Returs
> Uawdown
> Nrwn
> Coun
> Sho Cownt
> Instruient TyDe
> Regon
> Universe
> Language
> Decay
> Delay
> Trncaton
> Neutaliation
> Pastelriralion
> NaN Handling
> Uit Handling
> MaxTrade
> 2013
> 1.13
> 3795
> 0.97
> 8301
> 590
> 13.3542
> 197_
> 1590
> E-iy
> C
> NNO_IN
> Fas Eoression
> 0.08
> Indusry
> Verf
> 701-
> 1.53
> 5.7120
>  -
> 6
> 0390
> 13.21923
> 935
> 2+92
> 7015
> 1.83
> 5020
> 13-21
> 93-0
> -3.35
> 1351
> 2112
> 2016
> 031
> ?-30
> O
> -5
> S-1
> 3.3293
> 135s
> 1913
> Clone Alpha
> 2017
> 1.5
> 7.03-0
> 9
> 6- 
> 1.970
> 13.J-93
> 010
> 1335
> 7013
> 019
> 7-25-0
> 00s
> 934
> 4110
> 7.7292
> 632
> 1953
> N Chart
> Pnl
> 2019
> 130
> 703-0
> Ds
> 529*
> 53-7
> 15.179
> 121
> 1503
> 2020
> 1.19
> 7.250
> 0.92
> 3-51
> 3275
> 73.305
> 1
> 13-
> 202
> 15_
> 7.39-0
> 799北
> 323珩
> 20.253
> 11
> 1573
> 20
> 5.3340
> 0.70
> 560北
> 3 _40
> 15.23923-
> 535
> 173-
> 0JOK
> 703
> 10
> 59_-0
> 1086-
> 1+3-0
> -35.524
> 197
> 1755
> 200OK
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Ftness
> Rerurns
> Drowdown
> Marsin
> 1.34
> 3.23%
> 0.83
> 4.78%
> 5.14%
> 29.549600
> Jan'14
> Jan'15
> Ja116
> [717
> Jan3
> Jan19
> 13720
> 0071
> 1022
> Jan 23
> APAC
> ABBrEBate Data
> Sharpe
> Turnoer
> FITRESS
> RezUrns
> Drawdown
> Margin
> 0.14
> 2.4096
> 0.03
> 0.5096
> 10.169
> 4.169600
> Shc
> Lomg


**举例二：EUR mdl25_vrv421_41v**


> [!NOTE] [图片 OCR 识别内容]
> 4d125_Vrv421
> 7 single Data Set Alpha
> POWE  PoaL4pha
> Fyramidtene EURIDTIMODEL3
> bcountry;
> group_rank (ts
> rank(a,252)〉b
> group_rank(ts_rank(a, 63),
> b;
> ABgregate Data
> 57arne
> TUTOVE
> FITESS
> RETUTTS
> Drawdown
> Marfin
> 1.27
> 5.45%
> 0.66
> 3.389
> 4.74%
> 12.409600
> Simulation Settings
> Year
> Sharpe
> Turnover
> Fless
> Reluri
> Orawdown
> Margi
> Coun
> Short Count
> Instument Type
> Remon
> Unyerst
> Language
> Dcy
> Dly
> Trcaton
> Newtaliaton
> Rastomrization
> NaNHondling
> Uit Handlng
> NTroe
> 7013
> 25s
> 5.37
> 57
> 1.373
> 16.400
> 1153
> 3-3
> E-iy
> EUF
> TOPZSOD
> Fas: E pre-sion
> 0.03
> InJusr
> Verf
> 201-
> 72
> 5.03
> 3.32
> 2173
> 15.743
> 1--
> 1195
> 2015
> 0.91
> 5.33
> 037
> 203
> 951
> 7.753
> 1--
> 1295
> 7015
> 0.+5
> 5.331
> 0.17
> 53
> 3.133
> ?533
> -00
> 1325
> Clone Alpha
> 70
> 1.20
> 5.254
> 0-3
> 1.3
> 1.073
> 7.5080
> 1533
> 1355
> 2013
> 0.51
> 5-3
> 1_
> 0.97
> 1-
> 3.553
> 1-7
> 1451
> N Chart
> PIL
> 2019
> 1.3
> 52
> 0.93
> +1:
> 1.313
> 5.25.7
> 1-
> 1+
> 00
> 0.52
> 5.701
> 023
> 253
> 一7
> 55
> 131-
> 1453
> 70
> 291
> 521
> 713
> 7.07
> 3
> 27.140
> 553
> 1299
> 202
> 5.51
> 0.35
> 4.75
> 3103
> 1.33
> 1335
> 157_
> 20JJK
> 03
> 一-5
> --
> ~225
> 0-33
> 10.1223
> 1333
> 1+33
> 09K
> Risk neutralized
> Agsregate Data
> Sharoe
> Turnover
> Fitness
> ReUrns
> Drawdown
> Margin
> 0.54
> 5.459
> 0.14
> 0.9096
> 4.2296
> 3.309600
> Jan14
> Jans
> 13716
> 13717
> J30'3
> 13121
> J30'22
> J3023
> OTrolato
> AIV;
> Lom9
> Jano
> Ja7 20


**举例三：EUR fnd6_fincfy**


> [!NOTE] [图片 OCR 识别内容]
> fnd6_fincfy;
> R Single Data Set Alpha
> A Power Pool Apha
> FyramidteTe EURIDTIFUNDANENTAL *.1
> bcountry;
> Broup_rank (ts_rank(a;
> 63)' b-group_rank (ts
> rank(a〉 252b;
> ABBrEBate Data
> Snarpe
> TUFTONET
> FiTTE-S
> Returns
> Drawdown
> Margin
> sined
> power(C;2)
> 1.36
> 4.629
> 0.74
> 3.7096
> 3.549
> 16.029600
> Simulation Settings
> Year
> Sharpe
> Tumover
> Fus
> Relur
> Uawdown
> Margi
> Long Coun
> Short Count
> Instument Tyoe
> Regon
> Uyerst
> Language
> Dcgy
> Dlay
> Trcaton
> Nemtaliaton
> Rasteization
> NaNHondling
> Uit Handlng
> Nax Trade
> 7013
> 0.97
> SJS
> 0-
> 730
> SE
> 7.53-
> 07
> 11OD
> E-i
> EUF
> TOPZSOJ
> Fas  E presson
> 0.03
> Sub
> nJusny
> arf
> 201-
> 1.29
> 139
> 0.55
> 313
> 23
> 1447:
> 1290
> 1330
> 05
> 773
> 452:
> 05
> 7.05
> 5
> 31.20-
> 1352
> 1376
> 2016
> 1 1
> 456
> DED
> 797
> 201
> 13.05-
> 13-1
> 1335
> Clone Alpha
> 70
> 075
> 446
> 027
> 52:
> 30
> 7 7
> -
> 1413
> 01
> 1.51
> 15
> 0.33
> 一一
> 2.091
> 19SOs:
> 一0
> 1+3-
> N Chart
> PnL
> 2019
> 15
> 1.17
> 一7
> 121
> 71.19 -:
> 141
> 1+-3
> 70_0
> 0.30
> 171
> 0.33
> 2
> 3.-5
> 12.34-
> 1-13
> 1350
> 20_
> 1.0
> 121
> 0-3
> 133
> SS
> 134 :
> 503
> 1+38
> 30371
> 2022
> 1.73
> 4S0y:
> 1.15
> 5.55.
> 2.201
> 24.70
> 1-0
> 1507
> 023
> -3.30
> 5:
> ~.13
> 1-25
> 0
> 13494
> 7-31
> 1-1
> 20K
> Risk neutralized
> ODOK
> Aggregate Data
> Sharpe
> Turnover
> Ctness
> Reurns
> Drawoown
> Marn
> 1.10
> 4.629
> 0.51
> 2.73%
> 2.68%
> 11.829600
> Jan'14
> Janis
> 13016
> 13717
> J30'3
> Jan'9
> J3020
> Ja121
> J30'22
> Jn 23
> 医 Correlation


---

### 评论 #53 (作者: JB53978, 时间: 10个月前)

《社交媒体突破信号》的模板
模板：
 **<Cross_Sectional_op/>** ( **<ts_arg_max/>** (ts_rank( **<Socialmedia_field/>** ,  **<decay_1/>** ),  **<decay_2/>** ),  **<decay_3/>** )

**1.**  变量说明：

**<Cross_Sectional_op/>：** 可以用 normalize、quantile、rank、zscore、regression_proj、vector_neut、vector_proj、winsorize、ts_decay_linear 等。

**<Socialmedia_field/>：** 来自 socialmedia12 和 socialmedia8 数据集的 matrix 字段。

**<ts_arg_max/>：** 固定用 ts_arg_max 去找历史最大值的位置。

**<decay_1/>：** 范围 [60, 120]

**<decay_2/>：** 范围 [252, 120, 60, 20]

**<decay_3/>：** 范围 [20, 10, 5, 1]

**2** . 搜索空间大小：
以 socialmedia12 为例，6 个 matrix 字段 * 9 个 Cross_Sectional Operator * 不同 decay 组合 ==  540 个。

**3** . 模板的 **idea** ， **implement** 细节
 **Idea:** 我感觉社交媒体数据挺特殊的，它经常会突然爆一下，然后又慢慢降下来，挺有节奏感的。所以这个模板的核心想法是：
先用 **ts_rank** 对社交媒体数据做个 X 天滚动排名，去掉绝对值的影响，让不同股票在同一水平上比较。再用  **ts_arg_max** 找出过去 X 天里排名最高的那天，等于是在找“最近的高光时刻”。最后用 **Cross_Sectional**   **Operator** 做标准化。
 **Implement细节:** 
 **ts_rank(<Socialmedia_field/>, <decay_1/>)：** 第一步，把原始数据转成相对排名。
 **ts_arg_max(..., <decay_2/>)：** 第二步，找出过去 <decay_2/> 天的最高点位置。
 **<Cross_Sectional_op/>(..., <decay_3/>)：** 最后一步，对跨股票的信号做标准化。
 **4.**  产出效果
这种方法我觉得在预测上比较有用，因为社交媒体上的热点和资金关注度往往是同步的。我跑过几组参数，发现近期有过社交媒体热度突破，表现还不错，通过这个模板我也成功点亮了Socialmedia的塔，没有去混信号，以Atom_ppa的方式来完成点亮。
 **5.**  建议其他顾问未来尝试的探索方向
 **二阶信号：** 可以把这个模板的输出再丢进 **ts_delta、ts_correlation** 等Operator里，做多层信号。
 **6.** 跑出Alpha实际效果图 **
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> A Sirzle Data Set Nlphs
> # Powver Pool Nphs
> Fjrsmidthems: USNDUISOCIALMEDIA X
> ABEregate
> 03+3
> Sharpe
> TUFnOET
> TmEC
> ReTTITT
> UCSIII
> Warain
> 1.11
> 1.G490
> 0.61
> 3.7290
> 5.0390
> 6.039300
> Shalpe
> TOVeT
> Foess
> Rehms
> Uawdow
> Marln
> Long Count
> Short Coat
> 2713
> 7.71
> 一-
> -7.23
> 3:
> .3:
> I
> 113
> 1471
> 2711
> 一3::
> 1.1E
> STE
> 3
> 3三:
> 177
> T3
> 2015
> EE:
> 0.18
> 5;
> 匕15:1
> 11-
> 324
> ZOIE
> 一
> 3:
> _5::
> 3抚:?
> 1755
> 1TE
> 2017
> 汇:
> 331
> _3
> 5.7180
> 2018
> 一315
> 13
> 2.12治
> 5.708:0
> 325
> 11
> 2019
> JsE
> 5:
> 7
> 2.264
> 12.17?
> 1773
> 130
> 220
> JSE
> 一7::
> .-3
> _3:
> 一3:
> 110
> 175
> 12
> 2021
> 一5
> 12
> 2.503
> 5.575:
> 1
> T3
> 2022
> 一3:
> 7.31
> 152::
> 2.745
> 5127:
> 172-
> 12
> 223
> 55
> 一5
> 21.344
> 一
> 3.03
> 131
> 191
> Risk neuiralized
> ABEregate
> 03+3
> Sh3
> TITMOE
> Tnas
> PSTII
> TCSTIOIC
> Warsin
> 0.97
> 4.6490
> 0.41
> 2.26%
> 2.9796
> 9.749300
**

**
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> A Sirzle Data Set Nlphs
> Power Pool Aphs
> Fjrsmidthems: USNDUISOCIALMEDIA ^1
> Eaate Data
> Shar
> TUFT
> TNEC
> ReTrl
> CCaTIO
> 1.15
> 4.55%
> 0.67
> 4.28%
> 6.3090
> 8.839300
> Shalpe
> IT
> Foess
> Rehms
> VTaOO
> Marln
> Long Count
> Short Coat
> 2713
> 55
> 一5:
> S:
> E三
> 153
> 1822
> TJ
> 一7:
> 7.71
> S::
> 3::
> J 
> 1315
> 1731
> 2015
> 一〉
> 375
> 5
> 06
> 1_
> ZOIE
> 1-5
> 一1
> -7.13
> 5::
> 1.345
> 382:?
> 2017
> 一_
> 4
> 1.91;
> 2.3E
> 5::
> 12
> 2018
> 115
> 3.315
> .13
>  
> :
> ::
> 31
> 12
> 15
> 一
> 1.TE
> 一;
> S:
> 22.51兄0
> 13
> 173
> 220
> 一3::
> 1.7
> 32
> 一1
> 3.05:
> 137
> 171
> 2021
> 25
> 53:
> 15:
> 3
> JE.ES
> 1233
> S
> 2022
> 一5
> O.7s
> 一52:
> 71
> 7
> 1E7
> 223
> 5:
> 1
> 1.57
> 7.5
> 17
> 23
> FEZ
> Naar
**

---

### 评论 #54 (作者: AK76468, 时间: 10个月前)

## 针对 model264 的 ATOM 模版

```
<sum_op/>(<mdl264_predict1/>,<mdl264_predict_2/>,<mdl264_predict_3/>)
```

- 变量1: <sum_op/>：可以是add和multiply等计算累计得分的运算符，multiply会放大股票之间得分差异，可能会有更好的表现。
- 变量2: <mdl264_predict(x)/>：可以是mdl264中预测趋势方向的字段，如： **mdl264_emp_class** ，描述为：Predicted trend of "Number of employees" (1: fall, 2: neutral, 3: move up)，即：“员工数量” 的预测趋势，数据离散，只有1，2，3三种取值。可以通过带有‘class’的后缀选到，即：mdl264_xxx_class
- 搜索空间大小：以model264为例，筛选userCount最大的前20个字段，为2*20*19*18=13680，考虑add和multipy作用类似，回测任务可以只使用其中一个，在提交时遍历运算符选择表现好的提交即可，所以搜索空间可进一步压缩为20*19*18=6840
- 模版idea：model264是时序上的预测数据，通过访问lab得知，该类数据离散且没有缺失值和0值，故不需要回填、截断、变换等预处理。mdl264_xxx_class这类字段是 **针对多维度经济、财务、市场及技术指标等的未来趋势预测结果** ，可将该字段理解为得分，上涨得分越高，下跌得分越低，所以通过将股票的多维度预测数据的得分累计。比如正向指标得分高意味着企业进步，做多。但是得分高低不意味着股票表现的好坏，比如负向指标肯定是下跌好，所以得分低才做多。
- 产出效果：回测了5812次，按照abs(sharpe)>1.2筛选，得出590个alpha
- 建议其他顾问未来尝试的探索方向：mdl264该类数据有400+个，搜索空间巨大，有些是正向指标，有些是负向指标，有些字段指标类似，直接相加可能没意义。所以可以通过让 MCP 区分指标的正向与负向属性，再筛选出关联度低的预测字段，再将方向一致且相关性低的字段进行组合，可以大大降低搜索空间，还能得到更全面的预测并提升预测的准确性。后续可以继续将该alpha当作数据字段使用到一二三阶的流程中。


> [!NOTE] [图片 OCR 识别内容]
> 7,0OOK
>  Settings
> USA/D1/TOP3000
> Convert to Multi-Simulation
> LANGUAGE
> INSTRUMENT TYPE
> 6,00OK
> Fast Expression
> Equity
> 5,00OK
> REGION
> UNIVERSE
> DELAY
> USA
> T0P3000
> 4,00OK
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 0.08
> 3,00OK
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> 2,00OK
> On
> Verify
> Off
> YEARS
> MONTHS
> MAX TRADE
> 1,00OK
> On
> Save as Default
> Apply
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
> Pnl
> Risk Neutralized Pnl
> IS Summary
> Period
> IS 
> 05
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Clone this Alpha in a new tab
> 1.77
> 2.659
> 1.41
> 7.890
> 5.239
> 59.45%o。
> Mtr


---

### 评论 #55 (作者: WL13229, 时间: 10个月前)

[JB53978](/hc/en-us/profiles/30875128290711-JB53978)

请展示实际效果图

---

### 评论 #56 (作者: WL13229, 时间: 10个月前)

[AK76468](/hc/en-us/profiles/28846915371031-AK76468)

你这个idea有点意思。挺好。

尝试做一些turnover 10%以上的Alpha

---

### 评论 #57 (作者: JL98779, 时间: 10个月前)

**【更新：如何避免過度擬合】
模板（在GLB, MINVOL1M進行測試）**

```
<ts_op/>(<op/>(ts_backfill(vec_avg(<mdl138_vector/>), 5) + <rsk70_matrix/>), <window/>)
```

**具體變量賦值：**

- ts_op: ts_rank, ts_zscore, ts_quantile, ts_scale, ... 輸出值介乎0至1的運算符
- op: rank, zscore, quantile, tanh, sigmoid, ... 輸出值介乎-1至1的運算符
- mdl138_vector: 任何model138（Stock Selection From Accounting-based Factors）内的vector，例如mdl138_longsimeq_qpdi4_cfo_curr_liab（現金流比短期債務的 [Four-Factor Model](https://tiomarkets.com/article/carhart-four-factor-model-guide) ）
- rsk70_matrix: 任何risk70的matrix（Multi-Factor Model），例如rsk70_mfm2_gemtrd_anlystsn（分析師的情緒指標）
- window: 時間窗口，建議使用252，504

**搜索空間的大小：** 120（mdl138） * 31（rsk70）* 4（ts_op）* 5（op）* 2（window）~ 148,800

**模板的idea，implement細節：** model138的字段 **從基本面** 中選出具升值潛力的股票，risk70結合 **短期數據，例如分析師情緒、回報率等製成因子模型** ，再從模型選出股票。我們 **從Brain Lab中可得知model138中的NaN數值很多** ，可以推斷是 **數據不連續更新** 所造成的。因此，可以使用ts_backfill， **把不完整的數據以一星期（5天）的數據回填** ，有效的降低turnover。把兩者的數值相加，再 **進行橫截面比較，穩定數值在-1至1之間** ，最後再 **選出在最近一至兩年内此數值較高的股票** ，給於較高的權重。此模板 **結合基本面、短期數據，組成長短期信號** ，所產出的 **PnL較爲穩定** 。

**產出效果：** 測試了187個alpha，定義sharpe > 1為有信號，有信號的alpha有51個， **出信號率為27%** 。設定中性化為STATISTICAL或COUNTRY的話，decay=0， **sharpe > 2的不在少數，更有一部分的sharpe可突破3** 。此外此模板的總運算符為5，總datafield數量為2， **符合PPAC的提交標準，更有一部分可提交GAC。** Prod corr多數接近0.6。

範例1 **
> [!NOTE] [图片 OCR 识别内容]
> AOO ulpna tO a
> Code
> IS Summary
> Period
> 们Power Pool Alpha
> Pyramid theme: GLBIDI/RISK +1
> Pyramid thene: GLBIDIIMODEL X1 _
> Aggregate Data
> ShSTO=
> TUTTTU1
> TIeS
> Returns
> UTaTTITT
> Narer
> Simulation Settings
> 3.50
> 15.04%
> 1.72
> 3.6496
> 0.919
> 4.84900
> Instrument Type
> Region
> Unierse
> Langwaye
> Decay
> Delay
> Trncation
> Neutraliation
> Pasteurtalion
> NaN Handlng
> Unit Handling
> Equity
> GL
> NIO_I
> Fsst ECresson
> 0.35
> Sristis
> Veris
> Vear
> Sharpe
> Turover
> Fbness
> Retuis
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> TE::
> .174
> 0.53
> 亡3
> 3557
> 322
> 2014
> 15.25
> 3.17治
> L
> 4.165:
> -157
> 43
> Z05
> 3.35
> 15.12
> 3.315
> 0.513
> 5.335.
> 4210
> Clone Alpha
> Z015
> .3
> 1457
> 4.24
> 0.53
> 75:
> -37
> 4351
> 20
> E.J
> 14SE:
> 3.32
> .574
> 0.265
> 585:
> 111
> 4
> 2013
> 1.70
> 14.555
> J.55
> 1
> 0.62%
> 2.-15t:
> -
> 45JE
> Chart
> PIL
> 2019
> _7
> 13.5
> 125
> 2.3汩
> I-1
> 41沁:
> 一C5
> 420S
> 2027
> 1.55
> 14.71
> 7.64
> 2.05沿
> IaJ
> ?J
> -03
> 433
> 2021
> 2.73
> 15.52
> 2.354
> 0.45%
> 3.675:
> 5258
> OODK
> 202
> 4.31
> 1S.ES:
> 247
> 二 E
> 0.65%
> 555:
> 5J25
> 5133
> OJK
> 202
> 1_
> 13.15
> S
> -2.334
> 0.35
> 3.375:
> 1581
> 4671
> DOJK
> AMER
> Aggregate Data
> Shar
> TUCTLTIE
> Frnssc
> TeTIICT
> UCa
> Warein
> 0.46
> 5.55%
> 0.07
> 0.33%
> 2.409
> .209o00
> 2014
> 2015
> 2016
> 2017
> 2015
> 2019
> 2020
> 2021
> 2022
> 2023
> APAC
> Aggregate Data
> Sharoe
> |UTNIYET
> Ftness
> Returns
> UTaWJOLT
> 4aTIn
> 4.01
> 6.28%
> 1.79
> 2.50%
> 0.429
> %oo
> EMEA
> 7.9
**

範例2
 
> [!NOTE] [图片 OCR 识别内容]
> Aggr
> Data
> 5narne
> TITTTI=
> STes
> R-UCns
> DrawJown
> 2.28
> 8.49%
> 1.03
> 2.549
> 2.5996
> 0UOooo
> Simulation Settings
> Instrument Type
> Region
> Unierse
> Langwaye
> Decay
> Delay
> Trncation
> Neutraliation
> Pasteurtalion
> NaN Handlng
> Unit Handling
> Vear
> Sharpe
> Turnoer
> Ftness
> Retums
> Dawdown
> Nargin
> Long Count
> Short Count
> Equity
> GL
> NIO_I
> Excression
> 0.35
> Ss-istical
> Veris
> 201
> 5S
> ~333
> 0.10沿
> 112
> 372
> 35
> 2014
> 一3
> 」
> Z.S
> 一353
> 0.12沿
> 3.3:
> 135
> 333
> Z05
> 8.5
> 22335
> 0.5汩
> _:
> 一_
> 13
> ZOIE
> 3.06
> 8.25治
> 32795
> 0.35
> 945
> 113
> 358
> Clone Alpha
> 20
> 2.15
>  T;
> 333
> 0.30汩
> 559:
> -225
> 41SE
> 201
> DET
> {.4
> T.E
> .713
> 1.05沿
> 635:
> TEI
> 451
> Chart
> 2019
> 抡沾
> 12
> 63%
> 0.575
> 9+5
> -337
> PIL
> 2020
>  S
> 0.J0
> 1.353
> 2.55汩
> 17
> 一_
> 41
> 2021
> 34
> =
> 3919
> 0.59沿
> 3359
> 545
> 5171
> 2022
> 3.0
> -
> 1.73
> 一353
> 0.30汩
> 535:
> 52EE
> 71
> 10/11/2015
> Dn
> 1,131.13K
> 2023
>  =
> 64%6
> 0.305
> 15.339:
> 一764
> nyestabllihrConstalnedPnl  1,01593
> OOJK
> AMER Pnl:
> 215.3
> APACPnL
> 5150J
> AMER
> EWEAPnL:
> 293.75
> Aggregate Data
> Sharoe
> |UTNIYET
> HMEss
> TCJTT
> UTaWJO'
> Marsin
> 1.22
> 3.61%
> 0.35
> 1.03%
> 1.92%
> 5.7
> 9ooo
> 2014
> 2015
> 2016
> 2017
> 2015
> 2019
> 2020
> 2021
> 2022
> 2023
> APAC
> Aggregate Data
> Sharpe
> TUCTLTIE
> Frnsssy
> TeTIICT
> Drawrdo
> Warein
> Pnl
> Investability Constrained Pnl
> ~LIER Dnl
> ~PJC Pnl
> EWILPnl
> 1.67
> 3.08%
> 0.45
> 0.919
> 0.88%
> 5.92000
> EMEA
> Data
> Sharpe
> TUCTLTIE
> Frnssc
> TeTIICT
> UCa
> Aggregate
> 1.69
> 1.80%
> 0.37
> 0.60%
> 0.37%
> 5.709000
> IS Testing Status
> Period
> Investability constrained
> 3
> Sate
> MIarsip
  
> [!NOTE] [图片 OCR 识别内容]
> LMEA
> Data
> Sharpe
> TUCTLTIE
> Frnssc
> TeTIICTS
> UCa
> Aggregate
> 1.69
> 1.80%
> 0.37
> 0.60%
> 0.37%
> 5.709000
> IS Testing Status
> Period
> Investability constrained
> Aggregate Data
> Sharoe
> |UTNIYE「
> Ftness
> TCJTT
> UTaWJOLT
> Narsin
> 12PASS
> 2.08
> 7.639
> 0.91
> 2.3796
> 2.29%
> 229000
> STErDE Of 2.28
> 3b32 CUOf 311.58
> Sitness Cf 1.03
> aDOVE CUtoff of
> AVER STEIDE Of 1.22
> Sb CUOf 311.
> EE Sharpe CT1.69
> aDOVE CUTCff of 1 _
> APACShBTPE 3T 1.67 is 3bove CUtof cf1。
> 医 Correlation
> Tmovercf
> 49%
> abOVE CUOfT 3F 1%
> Trowercf
> 49%
> below cutoff
> 704。
> Self Correlation
> Matimum
> Nnimum
> L35t Rur -
> Weisht
> dsnbured OVerinsruments。
> Sb-Universe Sharpe Of 1.38
> abOVE CUtCffof0.8
> adder ShaTDE Of 3.20
> SbOJE COFT 2.02Tcr IsdleryEsr 2 1/20/2023.1/21/2021.
> Competition Global Alpha Compettion 2025 matches。
> Tnese Pyramid thees Tazcnwith the Tollowins mul-ipliers: GLBIDTIRISK
> 1; GLBIDIIMODEL
> 1.4. Tne fnal yramidthene Tultplier
> PoWe『 Pool Correlation
> IHMUMT
> Nnimum
> L35t Rur -
> Efetive Pyralid CoUn: for Geniusi
> ARMNG
> 5PENDING
> Prod Correlation
> TsmUM
> TMNC
> Run: Sun。 08/1712025。1.06 &
> 0.5584
> -0.2155
> 
> 10O
> 0.01
> 03
> 05"
> MIarsip
> ~05
> 0.4
> O.T
> 0.0。
> 01
> 0.6
> 0.7
> 0,8.
> 0,9。
> 0.4.
> -1.0_
> 0,.8


**建議其他顧問未來探索的其他方向：** 此模板產出的PnL並不高。可以研究如何提升整體的PnL或者進一步降低turnover以提升margin。

**【更新：如何避免過度擬合】** 應Weijie老師要求，解釋如何避免過度擬合。首先在提交alpha前，可以先 **查看alpha裏面各字段的意思** 。由於此 **alpha的核心思想是結合長短期信號以產出穩定的回報** ，所以我們要 **確保mdl138_vector變量和rsk70_matrix變量分別含有一個長期和一個短期信號** 。例如，如果machine alpha選出的字段分別是mdl138_longsimeq_dtl_3idp（3 Factor model based on Return on Assets）和rsk70_mfm2_gemtrd_ltrevrsl（Long-Term Reversal Style Factor Loading）， **兩個都是長期信號，那麽就會增加過度擬合的風險** 。
此外，我們也可以 **從alpha表面數據判斷其穩定性** ，例如其returns / drawdown比例，sharpe的標準差等。詳情可以參考我 [這個post]([L2] 【代碼分享】一鍵測試alpha穩健性即插即用Python代碼代码优化_34092588057111.md) 。

---

### 评论 #58 (作者: WL13229, 时间: 10个月前)

[JL98779](/hc/en-us/profiles/31205672631319-JL98779)

请阐述在两个数据字段相加时如何避免过拟合

---

### 评论 #59 (作者: AM12075, 时间: 10个月前)

```
模板：group_neutralize(round_down(ts_kurtosis(<ern3_data/>, 66)),densify(bucket(rank(<fnd28_data/>), range='0.2, 1, 0.2')))
```

模板中的变量使用 < /> 进行声明，总共两个变量。

具体变量1：<ern3_data/>：与财务报告发布时间相关的日期变量，可以包含所有和ern3有关的字段。

具体变量2：<fnd28_data/>：各项基础财务指标，可以包含所有和fnd28有关的字段。

```
字段示例：ern3_pre_interval：trading days before last report date (so it's always a non-positive number)fnd28_value_08606：Book Value per Share Growth (year ago)
```

搜索空间的大小： 4 × 156。

模板的idea，implement细节：

- round_down(ts_kurtosis(<ern3_data/>, 66))：对<ern3_data/>进行66期滚动kurtosis计算，并向下取整，作为主信号。
- bucket(rank<fnd28_data/>), range='0.2, 1, 0.2')：对<fnd28_data/> 做rank后分桶形成分组标签，densify() 对缺失组进行填充，保证每个组都有数据。
- group_neutralize(..., ...)：在分组标签 densify(bucket(...)) 内对主信号做组内中性化，去除因分组带来的偏差，得到最终Alpha信号。

**因子构造逻辑：**

不同股票在“财报前多少天”市场关注度不同，有的提前很久就有交易量和异动，有的集中在最后几天才异动，通过 ts_kurtosis 就能抓到这种“分布形态的差异”。

- ts_kurtosis 在这里的意义是利用财报周期性信息，度量不同股票在财报前的“市场关注集中度差异”。如果一只股票的“财报前 N 日”的分布集中在少数几个点 → 峰度高，说明这只股票的交易行为/市场反应主要集中在特定的财报临近日；如果分布更均匀 →峰度低，说明市场在财报前的关注相对分散。
- 例如：对于股票A，市场习惯在财报前3天才大幅波动 → ern3_pre_interval 分布集中，kurtosis 高。对于股票 B：市场在财报前20天就逐步有交易反应 → 分布更均匀，kurtosis 低。

产出效果：我尝试了600次回测，有三四个可以提交的Alpha，每个因子的各项指标也非常相似。提交符合PPAC，同时该模板为双数据集字段，有助于点亮金字塔。

建议其他顾问未来尝试的探索方向：

- 尝试不同长度窗口的日期（如22、120）对信号稳定性的影响。
- 替换其他ts操作符，进而使得PNL曲线更加平滑。
- 将 <fnd28_data/>替换为比率指标测试分组效果。

下面是其中一个回测示例，GLB地区的earnings较难出货，对于点塔还是有很大帮助。

```

```

---

### 评论 #60 (作者: WL13229, 时间: 10个月前)

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

请阐释为什么使用如下运算符及其作用

```
ts_kurtosis
```

---

### 评论 #61 (作者: FG12730, 时间: 10个月前)

很有帮助

---

### 评论 #62 (作者: SG46247, 时间: 10个月前)

## 模板

region：ASI

-ts_corr({other455}, {vec}({news20}), {day})

变量说明

#### {other455}：机构关系网络引力场，基于深度学习的公司关系聚类（供应链/资本关联/技术协同）

#### **({news20})：新闻注意力密度，** 实时新闻情感数据的事件冲击强度

具体变量：{vec}使用'vec_count'，'vec_avg'

具体变量：{other455}用matrix类型的数据

具体变量：<day/>: 时间窗口，可选为20，60，120等

搜索空间的大小：大约是284*3*23*2=39,192

模板的idea：该新闻数量反映市场关注度，突发新闻导致机构紧急调仓，高相关性 → 信息在关系网中快速扩散，低相关性 → 存在套利窗口，

产出效果：我尝试了1000多次回测，产出了了11个可以提交的alpha，发现这是一个反转因子，有8个可以提交的Alpha，每年的表现都比较均衡

以下是其中一个产出效果


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 08/21/2025 EDT
> anonymOUs
> UdO uphat0
> Usl
> Code
> IS Summary
> Period
> 05
> t5
> corr(oth45s
> competitor
> I2V
> P5
> 9200_WI
> Pca
> fact3_value
> VeC
> Count
> nWs2O_event
> text )
> 120
> Aggregate Data
> Sharpe
> TurTOVE
> Fitness
> Returns
> Drawdown
> Marsin
> 1.30
> 3.1896
> 1.06
> 8.2796
> 9.709
> 51.95900
> Simulation Settings
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
> Unit Handling
> Max Trade
> Year
> Sharpe
> Turnover
> Ftness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> Equizy
> 451
> WINVOLIII
> Fast Expression
> 0,05
> Industry
> Verify
> 2013
> 1.73
> 311
> 2.00
> 15.719
> 5.179
> 107.33533
> 343
> 550
> 2014
> 0.22
> 2.343
> 0.07
> 38%
> 7.943
> 11.739230
> 700
> 736
> 2015
> 1.27
> 2.434
> 1.13
> 9,879
> 6.6435
> 79,53523
> 333
> 799
> Clone Alpha
> 2016
> 2.6745
> 2.0_
> 13,129
> 2.7095
> 93.29533
> 945
> 763
> 2017
> 1.73
> 3.079
> 1.36
> 7.779
> 2.654
> 50,51930
> 1075
> 748
> 2018
> 1.26
> 2.339
> 1.25
> 9.209
> 3.189
> 63,33523
> 1300
> 301
> N Chart
> Pnl
> 2019
> 0.70
> 3.643
> 0.37
> 3.-936
> 2.944
> 19,17533
> 1225
> 716
> 2020
> 0.-3
> 4.233
> 0.20
> 2.679
> 919
> 12.559330
> 1255
> 787
> 2021
> 3.65
> 8.509
> 2.-54
> 45.505330
> 1570
> 941
> 2022
> 3.704
> 11.323
> 3.169
> 61,12533
> 1574
> 333
> OOOK
> 2023
> GGF
> 14.25
> 1.5195
> 50.33523
> 1334
> 331
> 25OOk
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Returns
> Drawdown
> Marsin
> 1.50
> 3.189
> 0.76
> 3.199
> 3.249
> 20.039600
> Jan'12
> Jan '15
> Jan'16
> J3n 17
> Jn 13
> 」31 19
> Jan '20
> Jan '21
> J3n'22
> Jan '23
> Pnl
> Risk Neutralized Pnl
> Correlation
> Self Correlation
> Maximum
> Winimun
> Last Ron


建议其他顾问未来尝试的探索方向: 该模板为基础模板，可以将新闻情绪类数据与anl、mdl、fnd，option等覆盖率较高的数据集结合使用。该模板在USA地区中信号也是不错的

---

### 评论 #63 (作者: PX70901, 时间: 10个月前)

- ## 模板
  region：ASI,USA,EUR,GLB
  <op/>(ts_delta(<mdl110data1/>,<day/>))+ <op/>(ts_delta(<mdl110data2/>,<day/>))
  变量说明
  #### {mdl110data}：这个是取自model110的数据,Big data and machine learning based model，这个数据集应该是基于大模型对公司的不同能力的打分。
  具体变量：{op}使用 quantile,zscore,rank。
  具体变量：{mdl110data1}model110的所有数据
- 具体变量：{mdl110data2}model110的所有数据
- 具体变量：<day/>: 时间窗口，可选为22,66,120,240等
  搜索空间的大小：大约是3*8*8*4=768
  模板的idea：对mdl110的数据与过去day天比较（用ts_delta实现），如果分数增加做多，分数减少做空，例如50分升到70分做多。
- 想法是源自于Consultant Tutorial 里面的[Task] Power Pool Alpha的answer **:** rank(ts_delta(mdl110_growth,120))+rank(ts_delta(mdl110_analyst_sentiment,120))
  产出效果：我尝试了10000多次回测，产出了了9个左右可以提交的alpha，我是MARKET,SUBINDUSTRY,CROWDING三个中性化进行回测，并且ASI,USA,EUR,GLB这4个国家进行回测，发现除了USA效果一般其余几个国家的效果都不错
- 以下是其中一些的效果

我把每个国家sharpe和fitness都大于1的筛选出来。

USA没有sharpe和fitness都大于1

EUR

记录太多暂显示部分出来。应为我是3个中性化跑了一次，并且只要rank有信号zscore和quantile都会有，我看sharpe和fitness都大于1应该有40条左右。大概有3个是不重复的。


> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 511
> 5.251
> 50
> 1.11
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 103
> 5.6415
> 5.3255
> 1.15
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 1.72
> 4.4035
> 5.793
> 3.793
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOP2500
> 1.61
> 55驴
> 353
> 7.553
> 1.17
> anonymous
> Rsaular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 6.311
> 6.7511
> 733
> 1.09
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 6.313
> 6.753
> 6.733
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 4.343
> 533
> 183
> 1.03
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 6.033
> 803
> 53i
> 1.06
> anonymoUs
> Regular
> UNSUBMITTED
> 08/24/2025 EDT
> EUR
> TOP2500
> 333
> 6.743
> 833
> 1.07
> anonyMUS
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 363
> 323
> 7.4335
> 1.13
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 5.375
> 59珩
> 5.133
> 112
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 033
> 803
> 53i
> 1.06
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 5.001
> 5.303
> 3.521
> 1.16
> anonymoUs
> Regular
> UNSUBMITTED
> 08/24/2025 EDT
> EUR
> T0P2500
> 1.81
> 4.8135
> 5.7735
> 5935
> 1.12
> Purple
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 5.413
> 56珩
> 4.3631
> 1.03
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOP2500
> 4.721
> 6.513
> 08
> 1.01
> anonymous
> Regular
> UNSUBMITTED
> 08/24/2025 EDT
> EUR
> T0P2500
> 1.52
> 6.3535
> 5.1935
> 9.2135
> 1.08
> Purple
> anohyMUs
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOPZSOD
> 1.76
> 5.1235
> 5.3455
> 68
> 1.13
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 4.81
> 5.775
> 3.59珩
> 112
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> TOP2500
> 6.103
> 5.643
> 5.323
> 1.15
> anonymous
> Regular
> UNSUBMITTED
> 08/2-/2025 EDT
> EUR
> T0P2500
> 5.371
> 5.591
> 5.133
> 112
> anonymous
> Rsaular
> UNSUBMITTED
> 03/2-/2025 EDT
> EUR
> T0P2500
> 1.51
> 6.333
> 6.743
> 833
> 1.07
  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> 05
> quantile(ts_delta
> mdl110_analyst_sentiment, 248)
> quantile(ts
> delta (mdlIlO_growth, 24)
> ASirale Data Set Alpha
> Aggregate Data
> SharpE
> LUTU
> Ftnes
> ETUTA
> UTaWJOT
> Iarain
> Simulation Settings
> 1.81
> 5.779
> 1.12
> 4.819
> 3.599
> 16.679600
> Instrument Type
> Region
> UnNerse
> Lanquage
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> EqU?
> EUR
> TOPZSOO
> Fast ExPression
> Suoindusy
> Verify
> Year
> Sharpe
> TurOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> 37
> 5.731
> 2.43
> 62沁
> 1.085
> 22.50922
> 715
> 710
> 201-
> 335
> 0.93
> 64兆
> 0030
> 13.54932
> 72-
> 722
> 2015
> 5.7250
> 117
> 4.70沁
> 12932
> Clone Alpha
> 2015
> 1.75
> 5.3450
> 0.99
> 3.975
> 50W6
> 14.359333
> 757
> 2017
> 1.75
> 50
> 0.9
> 54兆
> 1.4350
> 12.379532
> 371
> Chart
> Pnl
> 2013
> 2.55
> 003
> 43*
> 1.7930
> 21.60932
> 740
> 2019
> 412*
> 1.2155
> 13.51922
> 7O0
> 635
> 2020
> 005
> 5.1655
> 0.01
> 0.16*
> 4930
> 529
> 533
> 530
> 2021
> 254
> 5.5190
> 1.9
> 6.76沁
> 0.919
> 0933
> 553
> 2022
> 1.71
> 5.2355
> 1.25
> 5.73*
> 2.9455
> 25.49922
> ZOOOK
> 2023
> 2.57
> 4.4155
> 2.03
> 725*
> 0.3755
> 32.379522
> 533
> Risk neutralized
> Aggregate Data
> Sharpe
> LUpnoe
> FiznEss
> TeCUII
> LraVgC
> Iarl
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
> 1.23
> 5.779
> 0.55
> 2.529
> 3.679
> 8.739600
> PIL
> Risk Neutralized Pnl
> Correlatinn
> Long
> 15
 挑选2个出来看看


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 08/24/2025 EDT
> anonymoUs
> udd AIphato
> Lisr
> Code
> IS Summary
> Period
> quantile(ts_delta(mdl110_growth, 240
> quantile(ts_delta (mdl118
> SCOre
> 240
> 眙sirgle Data Set Alpha
> Aggregate Data
> Sharpe
> TUCnI
> Fitne
> REIICn
> Cpa
> Marair
> Simulation Settings
> 1.52
> 5.1996
> 1.08
> 6.359
> 9.21%
> 24.499600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteuriation
> NaN Handlling
> Unit Handling
> MaxTrade
> EqU?
> EUR
> TOPZSOJ
> Fast Sxpression
> Marke-
> Verif
> Year
> Sharpe
> TUITOVeT
> Ftnoss
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> ~-5
> 5.2295
> 1.71
> 1-.0393
> 40沁
> 45.075600
> 715
> 710
> 2014
> 39
> 4
> 5695
> 23沁
> 93530
> 728
> 2015
> 1393
> 5895
> 32北
> EFDD
> 754
> 753
> Clone Alpha
> 201
> 7593
> 0.55
> 5595
> 39兆
> 036oo
> 769
> 795
> 201
> 3991
> 0.30
> 09
> 93
> 70F6oo
> S5
> Chart
> Pnl
> 2013
> 5.2793
> 1.22
> 5695
> 30北
> 21.4566p3
> 743
> 745
> 2319
> 5.3393
> 989
> 46沁
> 22.44553o
> 592
> 595
> 2020
> 0.32
> 5.7893
> 14
> 3593
> 9.215
> 35830
> 2321
> 2.15
> 5.2795
> 1.79
> 3.7195
> 90沁
> 3.0230
> 675
> 20
> 559
> 0.59
> 555
> 931
> 24.795600
> 575
> 533
> 25OOK
> 2023
> 101
> 5693
> 一.35
> 0293
> 5
> 103.345200
> 551
> 535
> Risk neutralized
> Aggregate Data
> Sharme
> TUCnI
> Fitness
> TeTIICn
> [ran
> Mareir
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
> 1.06
> 5.199
> 0.45
> 2.22%
> 5.529
> 8.579600
> LonO


接下来可以看看ASI的，应该有3个左右可交的因子


> [!NOTE] [图片 OCR 识别内容]
> 鬯%
> Simulate
> Alphas
> Learn
> Data
> %
> Labs
> Genius
> 留 Competitions (4)
> Community
> !
> Refer
> friend
> UNSUB
> Created 08/24/2025 EDT
> anonymoUs
> udd AIphato
> Lisr
> Code
> IS Summary
> Period
> quantile(ts_delta(mdll10_price_momentum_reversal,128
> quantile(ts_delta (mdlllg_growth,120 )
> u Sinale Data Set Alpha
> Aggregate Data
> Sharpe
> TUCnII
> Fitness
> REIICn
> Cpa
> Marai
> Simulation Settings
> 1.76
> 7.6596
> 1.10
> 4.849
> 3.78%
> 12.669600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralizatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTa
> EqU?
> MNOLIII
> Fast SPressIOn
> Suoindusny
> Verify
> Year
> Sharpe
> TuITOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> 3.32
> 55G5
> 3.51
> 105-
> 1.3-51
> 21.929522
> 1154
> 2014
> 3-3
> 5.74
> 2.79
> 829沁
> 1.123
> 24.51933
> 1250
> 1272
> 2015
> 355
> 1.13
> 83沁
> 56G5
> 35932
> 134-
> 1355
> Clone Alpha
> 2015
> 7.1755
> 0.7-
> 82北
> 2.5-35
> 659
> 349
> 13-1
> 201
> -1
> 7.615
> 53
> 1750
> 29333
> 35-
> 1370
> Chart
> Pnl
> 2013
> 335
> 1.33
> 43北
> 2.2550
> 93932
> 502
> 503
> 2319
> 0.75
> 8.10]
> 0.30
> 90沁
> 2.03
> 6996
> 1325
> 1324
> 2020
> 0.72
> 0250
> 0.33
> 255光
> .7355
> 0393
> 1-29
> 1452
> 2321
> 1.15
> 7.715
> 0.59
> 22北
> 2.9635
> 35922
> 1571
> 592
> 20
> 0.31
> 8.38]
> .42
> 2.70*
> 2.435
> 193
> 1649
> 1653
> ZOOOK
> 2023
> 0.55
> 0.910
> 0.29
> 51
> 0.5950
> 9593
> 555
> 1432
> Risk neutralized
> Aggregate Data
> Sharpe
> TUCnU
> Fitness
> TeTIICn
> Drawdowr
> Marzir
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
> 1.61
> 7.659
> 0.79
> 2.990
> 4.4496
> 7.829600
> PnL
> Risk Neutralized Pnl
> LONO



> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 08/24/2025 EDT
> anonymous
> AJd Aphato
> LIst
> Code
> IS Summary
> Period
> quantile(ts_delta (mdlllo_price
> momentum_reversal, 248
> quantile(ts_delta (mdlllo_tree, 240
> Asinale Data Set Alpha
> Aggregate Data
> Sharp
> Turnove
> Fitness
> EICn
> UCaIIO
> Marsin
> Simulation Settings
> 1.82
> 8.129
> 1.17
> 5.219
> 3.299
> 12.819600
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
> MaxTa
> Equ
> MINOLIN
> Fast Expression
> 0.03
> Subindusny
> Verify
> Year
> Sharpe
> TUIOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2313
> 3.70
> 3.2695
> 3.29
> 3893
> .4195
> 23.939
> 1126
> 1123
> 2014
> 2.52
> 5.739
> 5.3593
> 1.7293
> 13.8793
> 1205
> 1200
> 2315
> 9993
> 2.21
> 4693
> .4095
> 21.359
> 1251
> 1305
> Clone Alpha
> 2016
> 1893
> 0.76
> 3.3195
> 2.4195
> 10459
> 1274
> 1297
> 2017
> 3.0993
> 0.5-
> 5991
> 1.2993
> 559323
> 1321
> 1337
> Chart
> Pnl
> 2013
> 0.83
> 7.9593
> 0.41
> 5593
> 3895
> 679533
> 1-76
> 14-5
> 2019
> 3.3993
> 一499
> 1.2493
> 10.709323
> 131-
> 1333
> 2020
> 2.3-
> 10.3003
> 5893
> 2.5293
> 669333
> 1372
> 13-7
> 2321
> 0.25
> 9593
> 0.07
> 0.3493
> 2995
> 579
> 520
> 607
> 2022
> 2.17
> 3.1593
> 7.0493
> 1.5195
> 172992
> 1551
> 1553
> OOOK
> 2023
> 10.7795
> 5.91
> -17.57i
> 2093
> -32.539
> 1539
> 1433
> Risk neutralized
> Aggregate Data
> Turnove
> TitnEs
> ReTMTn=
> Craor
> Marain
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
> 0.63
> 8.1296
> 0.19
> 1.1796
> 4.4596
> 2.889600
> LONO
> 5h3


GLB  应该有3个左右的可交的因子


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Zscore(ts_delta (mdlllo_Browth, 240
> ZSCOre
> ts_delta (mdl118_analyst_sentiment, 240
> A Sinale Data Set Alpha
> Aggregate Data
> Sharpe
> TICU
> Cte
> REIICn
> Cramm
> Marain
> Simulation Settings
> 1.68
> 9.62%
> 1.12
> 5.52%
> 4.71%
> 11.489600
> Instrument Type
> Region
> UnNerse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handlling
> Unit Handling
> Max Trade
> Equz
> GLB
> TOP3OO0
> Fast
> Expression
> 0.03
> Marke-
> Verify
> Year
> Sharpe
> TuITOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> 3-3
> 4250
> 2.8-
> 828沁
> 1.1435
> 17.579522
> 1243
> 1255
> 2014
> 3.19
> 5.936
> 2.31
> 553沁
> 1.0190
> 14.5-932
> 1252
> 1270
> 2015
> 3.0150
> 5.19*
> 5930
> 529
> 30-
> 1293
> Clone Alpha
> 2016
> 1.-5
> 0250
> 0.83
> 408光
> 2.3555
> 059532
> 1310
> 1300
> 201
> -5
> 54S5
> 5*
> 1.0130
> 12.27922
> 232
> 1310
> Chart
> Pnl
> 2013
> 2.33
> 3.815
> 2.29
> 16兆
> 1.5155
> 639523
> 306
> 1303
> 2019
> 0.25
> 835
> 3.05
> 0.711
> 2.9455
> 43903
> 305
> 1292
> 2020
> |]
> 8650
> 0.02
> 45沁
> 4.7190
> 3593
> 1255
> 1257
> DOO
> 2321
> 2.20
> 30-
> 00沁
> 2.4-55
> 17.-79
> 239
> 1233
> 20
> 9.4455
> 111
> 7.24沁
> 4.4030
> 15.329
> 1253
> 1235
> ZOOOK
> 2023
> 1.25
> 895
> .
> 42*
> 0.7390
> 5093
> 1279
> 1344
> AMER
> Aggregate Data
> Sharpe
> TVCnUE
> Firnes
> ReTUITn
> Crawdowr
> Mareir
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
> 0.81
> 3.359
> 0.28
> 1.47%
> 3.8796
> 8.789600
> Pnl
> Risk Neutralized Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> APAC
> Aggregate Data
> Sharoe
> UTICVEI
> Fitness
> REUFns
> S3USIR
> Narein
> 1.07
> 3.649
> 0.48
> 2.5596
> 3.499
> 14.009600
> Long


- 建议其他顾问未来尝试的探索方向
- 因为我看Prod Correlation都比较高
- 建议大家可以试下其他相关的数据集
- 可以试下<op/>改成groupOp（group_zscore）加入自己的分组(我后面试下如果有成功我回来更新)，例如
  bucket(rank(debt/enterprise_value),range="0,1,0.2"),
  bucket(rank(cap),range="0,1,0.2")
  bucket(rank(capex/sales),range="0,1,0.1")
  这样就可以降低一定的相关性。可能可以做出自己的RA。
  下面这个相关性是0.71，但是我并没有下降相关性成功。
  还有一个缺点就是（return）回报有点低...
  
> [!NOTE] [图片 OCR 识别内容]
> 2022
> 1.77
> 531*
> 1.34
> 7.1593
> 3.4595
> 556
> 637
> 20OOK
> 2023
> 3.20
> 4-7*
> 2.57
> 3.7195
> 0.3795
> 3.3:
> 589
> Risk neutralized
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
> Sharps
> Turnos
> Fitnes
> RetUFn
> DrawJowr
> Marair
> 1.23
> 5.809
> 0.56
> 2.639
> 3.51%
> 9.059600
> Pnl
> Risk Neutralized Pnl
> 医 Correlation
> Self Correlation
> Mauimur
> Tinimr
> -1
> TIn:
> IS Testing Status
> Period
> Power Pool
> Correlation
> 443 TTUT
> TTINITUN
> Last Run:
> 8PASS
> 2WARNING
> Prod Correlation
> LIaemIF
> UCTNIC
> 08125/202511.37Pu
> 5PENDING
> 0.7153
> -0.4978
> 91
> OR

  
> [!NOTE] [图片 OCR 识别内容]
> Zscore(ts_delta (mdlllo_Browth,240)
> ZSCOre
> ts_delta (mdl11g_analyst_sentiment, 240
> 眙 Single Data Set Alpha
> Aggregate Data
> 5h3rC
> TMCnOe
> iTns
> 3eTI
> U「3TOn
> Simulation Settings
> 1.84
> 5.809
> 1.16
> 5.00%
> 3.52%
> 17.249600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralizatjon
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Equ?
> EUR
> TOPZSOO
> Fast Sxpression
> 0.03
> Subinlsry
> Year
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2013
> 32
> 6.33*
> 2.55
> 3.0395
> 0395
> 23.44:
> 710
> 715
> 2014
> 5.41沁
> 3.3893
> 1293
> 1-.332
> 719
> 725
> Clone Alpha
> 2015
> 5.73*
> 1.15
> 5393
> 5195
> 16.37:
> 749
> 754
> 201
> 35北
> 0.39
> 5393
> 5395
> 13.78:
> 755
> 793
> 2017
> 211
> 5.-1
> 3397
> 349
> 367
> 305
> N Chart
> Pnl
> 2013
> 2.57
> 604*
> 5.5195
> 3495
> 21.353
> 740
> 752
> 2019
> 11沁
> 一149
> 2393
> 55-:
> 701
> 535
> 2020
> 0.13
> 62-5
> 0.02
> 1591
> 3.2743
> 497
> 634
> 2021
> 564*
> 5393
> 339
> 23.33:
> 572
> 2022
> 1.77
> 5315
> 1.34
> 7.1595
> 4593
> 25.342
> 656
> 537
> ZOOOK
> 2023
> 447冼
> 2.57
> 3.7195
> 0.3791
> 33.37:
> Risk neutralized
> 2012
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> 2023
> Aggregate Data
> 5h3rC
> TCnOE
> Fitnes
> FSt
> [ralTO
> 1.23
> 5.8096
> 0.56
> 2.639
> 3.51%
> 9.059600
> Pnl
> Risk Neutralized Pnl
> Correlation
> Self Correlation
> UaTIMUN
> WinimJp
> Last Run:
> Marein
> Sharpe
> Long
> Verif
> Marz


---

### 评论 #64 (作者: JG21054, 时间: 10个月前)

模板:

```
<time_series_operator>(rank(<backfill_op>(<positive_sentiment,days))-rank (<backfill_op>(<negative_sentiment, days)), days)
```

模板中的变量使用 </> 进行了声明，总共四个变量。
具体变量 1：<time_series_operator/>: 可用于时间序列处理的运算符，用于对 sentiment 差值进行时间序列上的操作。我推荐使用ts_product、ts_max、ts_sum 这三个时间序列运算符。

- 通过ai分析知道ts_product 能放大指定窗口内sentiment_difference 的持续正向 / 负向趋势，强化强趋势性情绪变化；ts_max 可提取窗口内情绪差值的最大值，精准锚定情绪爆发点；ts_sum 能计算窗口内情绪差值的总和，平滑单日波动以反映中长期情绪累积的整体偏向，三者从趋势、峰值、累积三个核心维度，全面捕捉情绪变化特征。

具体变量 2：<backfill_op/>: 用于对 sentiment 数据进行回填处理的运算符，如 ts_backfill、to_nan 等，以提高数据覆盖率
具体变量 3：<compare_op/>: 用于比较 positive_sentiment 和 negative_sentiment 的运算符，除了模板的减法运算符外还可以尝试一下其他的运算符比如除法可以放大极端差异。
具体变量 4：days: 时间参数，可选用如周 (5 天)、月 (20 天)、季度 (60 天)、年 (250 天) 等合理值

模板的 idea，implement 细节（即哪步是数据处理，哪步是主信号）：
主信号：<time_series_operator>(<positive_sentiment> - <negative_sentiment>, days)，通过时间序列运算符处理 sentiment 差值得到最终信号。
数据处理：

- <backfill_op>：对 sentiment 数据进行回填，通过Lab去找了几个这两个数据集里的数据字段，查了一下发现缺失值比较多所以推荐用ts_backfill回填一下数据。
- rank：对回填后的 sentiment 进行排名，使数据分布在熟悉范围内，同时去除部分原始数据噪声，属于数据清洗和标准化处理
- sentiment_difference = <compare_op>(positive_sentiment, negative_sentiment)：通过比较运算符得到 sentiment 差值，为后续时间序列操作做准备

产出效果：在USA地区使用news18数据集与socialmedia12数据集情绪做差，大概61×5有305个组合，只套用我推荐的三个时间序列操作符，使用ts_backfill回填数据，时间天数五个都用的的话大概有305×3×5=4575个。由于这个模板跑的时间比较早具体的产出没有统计，不过有很多is指标很好，单独达到ra标准的sharpe和fitness的也有不少。除此之外还可以当作一阶信号去套二阶。下面放一个alpha的is表现。


> [!NOTE] [图片 OCR 识别内容]
> 15 SUmmary
> Period
> IS 
> 0S
> Regular Alpha
> Pyramid theme: USADIISOCIALMEDIA X1.1
> Pyramid theme: USALDIINEWS X1.2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.60
> 1.979
> 1.21
> 7.20%
> 5.68%
> 72.949600
> Year
> Sharpe
> TUrnOVeT
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.68
> 2.439
> -0.26
> -1.89%
> 3.69%
> -15.629600
> 1348
> 851
> 2014
> 1.19
> 1.4596
> 0.69
> 4.1796
> 3.22%
> 57.429600
> 1603
> 871
> 2015
> 1.71
> 1.6496
> 1.23
> 6.42%
> 3.26%
> 78.269600
> 1624
> 896
> 2016
> 0.40
> 1.8296
> 0.14
> 1.4896
> 5.19%
> 16.249600
> 1456
> 937
> 2017
> 2.48
> 2.0496
> 1.94
> 7.62%
> 1.42%
> 74.769600
> 1375
> 984
> 2018
> 1.05
> 2.1296
> 0.54
> 3.26%
> 1.5796
> 30
> 89600
> 1410
> 1029
> 2019
> 1.12
> 2.0396
> 3.82%
> 3.04%6
> 37.649600
> 1416
> 982
> 2020
> 1.03
> 2.1896
> 0.73
> 6.26%
> 3.58%
> 57.459600
> 1358
> 1002
> 2021
> 2.89
> 2.2596
> 3.44
> 17.71%
> 3.10%
> 157.709600
> 1654
> 1140
> 2022
> 3.52
> 1.8496
> 4.90
> 24.2796
> 3.4796
> 264.489600
> 1625
> 1102
> 2023
> 3.54
> 1.86%
> -4.94
> 24.3996
> 2.25%
> -263.019600
> 1495
> 1072


这个模板的原文链接放到下面，大家有兴趣可以去看看。我只探索了news18数据集与socialmedia12数据集，希望可以帮助大家有需要的点亮社交媒体和新闻的金字塔。

- > [[L2] [Alpha Template] Time-Series Sentiment Comparison TemplateAlpha Template_24756474790551.md]([L2] [Alpha Template] Time-Series Sentiment Comparison TemplateAlpha Template_24756474790551.md)

大家如果跑的话建议在ILLIQUID_MINVOL1M 宇宙中开启max_trade。后面让ai总结了一下原因：该策略之所以适用于 ILLIQUID_MINVOL1M 宇宙，核心在于其特性与宇宙特征高度契合：一方面，宇宙内标的流动性低（日成交额≥100 万美元）导致信息传播慢、股价易存在偏差，策略通过捕捉情绪趋势、峰值及累积效应，能提前挖掘情绪与股价的信息差，精准把握价格修复机会；另一方面，宇宙高滑点、做空难的高交易成本问题，与策略采用周 / 月 / 季度级时间窗口、信号更新慢且换手率低的设计相匹配，可减少交易成本对收益的侵蚀。而开启基于 adv20（20 日平均成交量）比例设定的 max_trade，对该宇宙而言更具关键价值 —— 既能避免因交易规模远超标的流动性引发的大幅滑点（如买入推高股价、卖出压低股价，导致实际成交价偏离预期），又能确保订单可执行（低流动性标的难以消化大额订单，按 adv20 比例限制规模可避免订单无法及时成交或拆分多日成交导致的策略滞后），进一步适配宇宙低流动性特性，保障策略实操效果。

建议其他顾问未来尝试的探索方向：尝试结合更多样化的时间序列运算符和比较运算符；在不同数据集上进行测试，观察该模板的适用性；

---

### 评论 #65 (作者: TJ14150, 时间: 10个月前)

- 模版

"financial_data = ts_corr(<ts_operator/>(<data_metric/>,<window/>), <data_metric/>, 20);
gp = group_cartesian_product(country, industry);
-<group_operator/>(financial_data , gp)"

- 模版中变量

<ts_operator/>：可以是所有的ts操作符ts_zscore, ts_std_dev, ts_scale, ts_sum, ts_av_diff, ts_arg_max, ts_max, ts_rank, ts_delay, ts_quantile, ts_min, ts_arg_min, ts_delta等，经测试ts_zscore,ts_rank, ts_arg_max效果最好，但是最好一开始全选上， ts_sum和ts_product可以不选

<group_operator/>：可以是所有<group_operator/>(financial_data , gp)结构的，group_min, group_max, group_rank, group_scale, group_zscore, group_neutralize，其中group_min, group_max最好别用没什么产出

<window/>：5，20，60

- 模版idea

ts_corr(<ts_operator/>(<data_metric/>,<window/>), <data_metric/>, 20)度量指标的自相关/稳定性，或捕捉指标变动与自身的动态关系，根据不同的ts操作符可以度量自身指标在短期与自身动态变化关系，举例ts_corr(ts_arg_min(data, 5), data, 20) 计算5日内某数据的最小值的位置序列，计算20天内其与本身的相关性，相关性高，越早出现在5日窗口（最近创了新低），二者走势高度一致，data如果是机构资金比例则表示其不断下降，近期不断刷新短期低点。如果很低甚至负相关，说明虽然有时候创低点，但整体持股比例没有明显趋势关系，可能在震荡或反弹

- 数据处理

如果有缺失数据可用ts_backfill()填充可能效果更好，数据也尽量使用数据全的，更新快的数据。后面gp = group_cartesian_product(country, industry);-<group_operator/>(financial_data , gp)是根据教材灵感进行强化，<group_operator/> 常见有：group_neutralize 去掉分组层面的系统性偏差，group_zscore / group_scale 在组内标准化，group_rank 在组内排序。此因子往往要取负，负号表示相关性高说明趋势稳定，预示趋势稳定拥挤要反向信号

- 产出效果：usa地区ILLIQUID_MINVOL1M 和TOP3000都可尝试，fund数据集fundamental7，140*15*3*4=25200，有产出ra；other数据集取前30个30*15*3*4=5400；news，analyst数据集也有产出


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 1S
> 05
> Single Data Set Alpha
> Power Pool Alpha
> 鹛 Regular Alpha
> Pyramid theme: USAIDIIFUNDAMENTAL X1.2
> Aggregate
> Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Marein
> 1.76
> 15.209
> 1.17
> 6.7496
> 3.989
> 8.879600
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
> 2.34
> 14.5296
> 3.95
> 12.0996
> 1.1996
> 16,6596o
> 6534
> 516
> 2014
> 4.98
> 14.139
> 5.13
> 15.01%
> 2896
> 21.239600
> 1813
> 585
> 2015
> 0.50
> 14.1596
> 017
> 1.5790
> 2.3696
> 2.36900
> 876
> 555
> 2016
> 13.4796
> 2.8990
> 3.0296
> 4.29900
> 1791
> 525
> 2017
> 13.12%
> 0.13
> 790
> 2.11%6
> -1.78900
> 1773
> 612
> 2018
> 0.02
> 16.86%
> .0590
> 2.1396
> 0.07960
> 1914
> 551
> 2019
> 1.16
> 16.589
> 0.55
> 3.8390
> .8696
> 4.62900
> 842
> 576
> 2020
> 2.91
> 17.249
> 2.53
> 13.069
> .9996
> 15.15960
> 762
> 527
> 2021
> 0.62
> 15.36%
> 0.27
> 2.859
> 3.8696
> 3.71900
> 2087
> 788
> 2022
> 3.12
> 16.26%
> 3.38
> 19.0396
> 3.98%
> 23.409603
> 2105
> 805
> 2023
> 3.06
> 24.35%
> 2.37
> -14.5890
> 5896
> -11.98900
> 998
> 528
> 11
> 0.00
  
> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> 05
> Single Data Set Alpha
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: USADIIOPTION X1.3
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawcown
> Marein
> 1.74
> 11.259
> 1.17
> 5.629
> 5.619
> 9.999600
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
> 1.75
> 12.46%
> 0.99
> 3.9796
> 1.36%
> 5.37960
> 1194
> 057
> 2014
> 2.70
> 10.909
> 2.03
> 7.0495
> 1.5996
> 12.92960
> 1344
> 1155
> 2015
> 1.39
> 10.439
> 0.80
> 41190
> 2.2096
> 7.88900
> 1212
> 1131
> 2016
> 1.71
> 10.729
> 08
> 5.0196
> 2.4096
> 9.35900
> 1344
> 1076
> 2017
> 0.46
> 10.949
> 0.13
> 1.0796
> 3.02%6
> 69o
> 1295
> 1093
> 2018
> 0.14
> 11.649
> 0.02
> 0.349
> 2.5896
> 0.5996oa
> 1314
> 1152
> 2019
> 2.93
> 11.389
> 2.33
> .8390
> 44%
> 13.87900
> 1314
> 105
> 2020
> 0.18
> 11.329
> 0.05
> 8096
> 5.6196
> 42960
> 1297
> 093
> 2021
> 2.81
> 11.469
> 2.5
> 11.039
> 2.0296
> 19.26900
> 1528
> 1329
> 2022
> 3.56
> 11.259
> 3.98
> 15.5996
> 9596
> 27.73900
> 1586
> 1329
> 2023
> 2.54
> 12.82%
> 2.92
> -17.18%
> 1.5196
> 26.799603
> 1265
> 1182
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: USAIDIINEWS X1.2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawoown
> Margin
> 1.93
> 13.309
> 1.40
> 6.999
> 3.219
> 10.519600
> Vear
> Sharpe
> Turover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.72
> 15.5996
> 1.93
> 7.81%
> 3.019
> 0.03900
> 1539
> 711
> 2014
> 1.71
> 15,08%
> 0.95
> 4.769
> 1.18%
> 6.3
> 90
> 1734
> 762
> 2015
> 0.45
> 14.859
> 0.13
> 1.28%
> 2.2596
> 1.7290
> 1796
> 725
> 2016
> 2.07
> 13.92%
> 1.36
> 6.0596
> .9696
> 09o
> 1701
> 715
> 2017
> 1.57
> 11.2790
> 0.85
> 3.7890
> 1.7296
> 70900
> G09
> 778
> 2018
> 1.74
> 12.809
> 1.15
> 5.639
> 2.0296
> 8.79900
> 593
> 872
> 2019
> 0.82
> 11.48%
> 0.37
> 2.5190
> 3.21%6
> 4.37960
> 530
> 387
> 2020
> 2.00
> 13.259
> 8.839
> 2.2296
> 13.339603
> 6599
> 583
> 2021
> 3.63
> 12.29%
> 4.41
> 18.419
> 2.2096
> 29.9590
> 946
> 929
> 2022
> 2.51
> 12.589
> 2.52
> 12.5590
> 3.2096
> 20.11900
> 2082
> 830
> 2023
> -3.43
> 13.989
> -4.51
> 24.1790
> 2.1196
> 34.59960
> 899
> 745
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: USAIDIIANALYST X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawOOwn
> Margin
> 1.55
> 12.449
> 2.68
> 37.349
> 27.40%
> 60.039600
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
> 0.22
> 13.239
> 0.10
> -2.60q
> 9.819
> -3.92930
> 165
> 220
> 2014
> -0.37
> 14.29%
> 0.19
> 3.92%
> 16.6595
> -5.4350
> 290
> 322
> 2015
> 0.50
> 13.69%
> 0.32
> 5.5496
> 7.8195
> 030
> 432
> 421
> 2016
> ,00
> 17.2496
> 0.95
> 15.5496
> 10.4395
> 18
> 5330
> 217
> 211
> 2017
> 1.20
> 12.9196
> 1.33
> 15.7796
> 8.6895
> 24.43950
> 345
> 236
> 2018
> 2.66
> 12.7596
> 4.40
> 34.959
> 5.8095
> 54.81930
> 319
> 271
> 2019
> 0.37
> 12.39%
> 0.21
> 3.98%
> 9.2095
> 6.4330
> 291
> 315
> 2020
> 2.02
> 11.039
> 4.54
> 63.1796
> 15.8595
> 114.553o
> 295
> 285
> 2021
> 2.05
> 8.819
> 4.40
> 57.59%
> 15.3095
> 130.3630
> 555
> 252
> 2022
> 3,60
> 7.869
> 14.13
> 192.5396
> 27.409
> L30
> 693o
> 611
> 167
> 2023
> 1.39
> 14.6096
> 1.52
> 19.8596
> 1.1495
> Soo
> 835
> 597


asi地区MINVOL1M的analyst数据集先取前30个测试30*15*3*4=5400，other数据集也有但少


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 1S
> 05
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIANALYST X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.68
> 7.869
> 1.40
> 8.739
> 5.879
> 22.219600
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
> 1.50
> 8.2296
> 1.28
> 8.039
> 2.28%
> 19.04900
> 704
> 517
> 2014
> 7.4096
> 1.56
> 8.5796
> 2.5796
> 23.
> 596o
> 805
> 532
> 2015
> 0.28
> 7.7296
> 012
> 2.139
> 5.8790
> 5.52960
> 705
> 544
> 2016
> 0.21
> 7.5996
> 0.05
> .019
> 4.5996
> 2.67900
> 532
> 2017
> 2.10
> 7.7296
> 1.77
> 8.939
> 2.719
> 23.08900
> 774
> 552
> 2018
> 2.35
> 7.5896
> 2.35
> 12.40%
> 2.62%
> 32.28900
> 343
> 618
> 2019
> 1.93
> 80096
> .55
> 9.119
> 4.31%
> 22.79900
> 539
> 2020
> 3.77
> 8.5096
> 4.56
> 18.3196
> 2.1496
> 43.11900
> 750
> 564
> 2021
> 2.51
> 7.5796
> 2.59
> 12.309
> 2.1796
> 32.09900
> 375
> 716
> 2022
> 1.41
> 7.79%6
> 1.10
> 7.62%
> 3.21%
> 19.54960
> 556
> 2023
> 0.79
> 11.0996
> 0.36
> 2.5796
> 1.149
> 4.64960
> 538
> 417
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIOTHER X1.
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawOOwn
> Margin
> 1.41
> 13.929
> 1.48
> 15.26%
> 16.839
> 21.929600
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.0
> 14.1796
> 2.5
> 23.809
> 7.3890
> 33.58900
> 1281
> 1427
> 2014
> 0.31
> 17.5296
> 0.16
> 4.46%
> 10.329
> 5.099603
> 1964
> 1181
> 2015
> 2.58
> 16.12%6
> 4.31
> 45.059
> 13.089
> 09o
> 1396
> 902
> 2016
> 1.25
> 13.22%6
> 1.25
> 13.06%
> 5.5696
> 19.7690
> 1199
> 958
> 2017
> 0.42
> 12.8396
> 0.21
> 3.239
> 6.0390
> 5.03900
> 1538
> 1705
> 2018
> 1.31
> 11.5096
> 1.17
> 9,939
> 4.759
> 17.27900
> 1584
> 2162
> 2019
> 2.65
> 12.2996
> 3.18
> 17.9796
> 4.819
> 28.7690
> 1354
> 2012
> 2020
> 0.35
> 13.9296
> 0.17
> 3.219
> 9.219
> 4.6090
> 1583
> 1955
> 2021
> 2.15
> 12.31%6
> 2.39
> 15.5196
> 4.0096
> 09o
> 1904
> 2590
> 2022
> 1.25
> 13.5896
> 1.19
> 12.269
> 9.1090
> 17.92900
> 1926
> 2251
> 2023
> 3.32
> 38.0296
> 4.70
> 76.3196
> 1.3796
> 2960
> 1243
> 2187


glb的MINVOL1M池：pv1数据集12*3*4*15=2160


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 1S
> 05
> Single Data Set Alpha
> Power Poo14Ipha
> Pyramid theme: GLBIDIIPV X1
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Marein
> 1.58
> 14.51%
> 2.10
> 25.649
> 30.339
> 35.349600
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
> 0.19
> 165.2195
> 0.08
> 3.10%
> 22.7895
> 3,83960
> 6012
> 2014
> 1.92
> 13.88991
> 2.32
> 20.1896
> 4.859
> 29.09960
> 7215
> 2015
> .82
> 13.959
> 0.83
> 14.4396
> 17.439
> 20.69960
> 7365
> 2016
> 1.20
> 15.4695
> 1.2
> 21.5196
> 8.799
> 27.829600
> 6533
> 2017
> 3.80
> 12.3595
> 6.20
> 40.71%
> 8.6895
> 55.75900
> 7322
> 2018
> 2.67
> 12.1595
> 4.25
> 35.92%
> 7.9495
> 50.78900
> 8017
> 2019
> .92
> 15.299
> 2.20
> 23.9496
> 8.3195
> 31.32900
> 7372
> 2020
> 14.339
> 1.02
> 20.5296
> 30.339
> 28.65960
> 7299
> 2021
> 3.00
> 13.8790
> 5.11
> 40.2396
> 5.3095
> 58.02960
> 9858
> 2022
> 12.0495
> 3.39
> 41.0596
> 23.5495
> 58.48960
> 8900
> 2023
> 3.84
> 8.8295
> -10.38
> 91.35%
> 8.1595
> 207.17900
> 8929
> 28


其实一开始是想做单数据集，并且练习ts_corr的使用，本来是想前后数据都进行ts处理，且不同时间窗口，发现数据量过于大，而且表现还不如单个处理，然后还想结合不好点塔的数据集增强信号，但是那些数据往往可能缺失过多，根本无法相关性计算，完全不适合当主信号，但是在作为辅助信号的方面的开发，我认为是很有潜力的，其他顾问可以尝试其他地区和不同中性化，可能会有好的表现，也可在其作为辅助信号方面探索可能性

---

### 评论 #66 (作者: 顾问 SC23342 (Rank 23), 时间: 10个月前)

1. Idea: 探索企业盈利指标间的相对强度关系与PCA特征值的正交化处理，挖掘基本面因子与技术因子的组合效应。
2. 模板：
   `vector_neut(ts_std_dev(vec_max(<anl69_field1/>) / vec_max(<anl69_field2/>), <days/>), <oth455_field/>)`
3. 变量声明：

- `<anl69_field1/>` ：指标上涨相关字段（共18个_up结尾的字段）
- `<anl69_field2/>` ：盈利预测相关字段（共18个_numest结尾的字段）
- `<days/>` ：时间窗口参数（120/180/240）
- `<oth455_field/>` ：oth455数据集中的PCA特征值字段（共300个字段，但根据字段命名规律，只需要遍历20种不同的*_w1_pca_fact1_value）

1. 搜索空间大小：
   18× 18× 3× 20 = 19440种组合
2. 实现细节：

- 主信号： `vec_max(anl69_field1) / vec_max(anl69_field2)`  反映每股收益与盈利预测数量的强度比。
- 数据处理：
  a) 通过ts_std_dev计算180日波动率捕捉稳定性
  b) 使用vector_neut与PCA特征值正交化消除系统风险
- 增强逻辑：正交化处理保留个股特异性的同时抑制行业共性波动

1. 回测效果：
   setting：EUR,TOP2500,FAST,Decay 0
   在以上遍历组合中，Sharpe＞1.5的表达式占比不到3%，最终提交了3个Regular Alpha


> [!NOTE] [图片 OCR 识别内容]
> 盹 Regular Alpha
> Pyramid theme: EURIDIIANALYST *1.5
> Pyramid theme: EURIDIIOTHER *1.6
> Aggregate Data
> Sha「o
> TUFMOYer
> TMeSs
> RetUFII
> LraVgC
> Marein
> 1.9
> 5.549
> 1.19
> 4.8996
> 3.2296
> 17.639600
> Sharpe
> Turnover
> Ftness
> Returs
> Orawdown
> Marqin
> LoNg Count
> Short Count
> 2013
> 0.00
> 0.00沁
> 0.00
> 0.031
> 0.031
> 0.00Ko
> 201-
> 0.00
> 00沁
> 034
> 0034
> 0.035
> 2015
> 1.12
> 95光
> 0.71
> 1.714
> 133
> 3.545
> 554
> 2015
> 1.75
> 43兆
> 0.37
> 3.754
> 1.154
> 13.735
> 1255
> 1454
> 2017
> 3.07
> 5.1-*
> 30*
> 0.334
> 22.545
> 1415
> 1537
> 2013
> 1.45
> 40北
> 0.71
> 2974
> 2.254
> 11.015
> 42
> 1524
> 2019
> 49
> 0.75
> 334
> 1.154
> 11.535
> 1354
> 1455
> 2020
> 2.51
> 62兆
> 2.25
> 10034
> 3.224
> 3.535
> 353
> 1404
> 2021
> 3.10
> 5.21光
> -3
> 034
> 53*
> 31.054
> 141
> 1521
> 202
> 0.35
> 6-;
> -
> 2.934
> 2011
> 10.335
> 1-14
> 1433
> 2023
> 5.12
> 45兆
> 16.274
> 1.144
> 59.5540
> 1291
> 1473
> Yoar



> [!NOTE] [图片 OCR 识别内容]
> 酏 Reaular Alpha
> Dyramid theme: EURIDIIANALYST *1.5
> Dyramid theme: EURIDIIOTHER *1.6
> Aggregate Data
> TUCIIIIP
> IiMess
> RatUCn
> Orayar
> Marein
> 1.65
> 7.3696
> 1.02
> 4.74%6
> 3.369
> 12.8
> 900
> Year
> Sharpe
> TINOeT
> Ftnoss
> Retwrns
> Drawdown
> Margin
> Count
> Short Cownt
> 2013
> 0O0
> 0.0095
> 000
> 0035
> 0.0095
> 0.00*0
> 2014
> 000
> 0.0093
> 0.03
> 0.0030
> 0.0093
> 0.00C
> 2015
> 1.52
> 1.5493
> 0.7
> 83
> 2591
> 2.205
> 734
> 201
> 3595
> 2.1255
> 5393
> 5.774
> 1137
> 1533
> 201
> 53
> 6.7093
> 1.73
> 5.53f
> 0.8795
> 5SKeo
> 1233
> 1713
> 2013
> 003
> 7.5395
> 0.01
> 0.1935
> 2.4095
> 0.515
> 223
> 697
> 2019
> 0.36
> 5.-995
> 0.33
> 8350
> 3793
> 5.315
> 1213
> 1515
> 2020
> .33
> 7.1893
> 302
> 13.7930
> 3.3693
> 33.-15
> 1195
> 1565
> 2021
> 3.0095
> 2.-5
> 0635
> 0.3395
> 20.155o
> 1245
> 1715
> 2022
> 0.55
> .9595
> 0.25
> 9250
> 2.4995
> 5.545
> 331
> 1572
> 2023
> 0.03
> 3.1191
> -0.01
> 205
> 0.4491
> 0.47*0
> 1337
> 1423
> Shrue
> LonO



> [!NOTE] [图片 OCR 识别内容]
> Rezular Alpha
> Pyramid theme: EURIDIIANALYST *1.5
> Pyramid theme: EURIDIIOTHER *1,6
> Aggregate Data
> Sharoe
> LUTIIe
> IIeSs
> RetUFns
> Uraydown
> Marein
> 1.91
> 7.399
> 1.23
> 5.2296
> 5.8996
> 14.129600
> Year
> Sharpe
> Turnover
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> 2013
> 0OO
> 0.0093
> 0.0
> 0.00f
> 0.0091
> 0.00C
> 2011
> 0OO
> 0.0095
> 000
> 0.0055
> 0.0095
> 0.00*
> 2015
> 213
> 5995
> 4.835
> 1.1495
> 21.0156
> 490
> 761
> 201
> 1.17
> 3.1093
> 0.53
> 3.1250
> 1591
> 7.715
> 1124
> 1595
> 2017
> 3.75
> 6.3795
> 4950
> 0893
> 23.50*0
> 233
> 1713
> 2013
> 7.7593
> 114
> 4.26轱
> 0991
> 10.99*e0
> 1243
> 1573
> 2019
> 二2
> 6.7591
> 1.14
> 57
> 339
> 15.515
> 1175
> 154
> 2020
> 5.9795
> 0.15
> 6750
> 5.3995
> 4.78*6
> 1134
> 1573
> 2021
> 4+3
> 7.2393
> ~.35
> 11.7330
> 5493
> 32.565
> 1212
> 1750
> 2022
> 7.3193
> 0.70
> 3.7530
> 2.073
> 0.275
> 1331
> 1571
> 2023
> 7.3395
> -0.57
> ~3.0430
> 5995
> ZSo
> 1245
> 1513
> Fitnws


1. 拓展建议：

- 尝试替换vec_max为其他vec运算符
- 尝试代入其他类型的比率。主信号可抽象为其他有经济学含义的比率,  例如在fnd类型中的profit字段 / size字段，pv类型的high / low，snt类型的follower / following等，具有时序和统计性特征的比率组合
- 用其他基础统计类的ts运算符替代ts_std_dev，如ts_mean和ts_sum

- 在GLB，USA，ASI等市场测试跨市场有效性

---

### 评论 #67 (作者: BA51127, 时间: 9个月前)

### **行业情绪偏斜：捕捉高管发言中的集体信号**

**1. 模板**

```
<group_operator/>(<data_processing_op/>(kth_element(vec_skewness(<news87_vector_field/>), <d/>, k=1)), <group/>)
```

**下面是我基于这个模板跑出来的一个具体Alpha表达式：**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> 1
> Broup_median (floor (kth_element
> VeC
> skewness (mWs87_cfo_neu_Iogit_pres ),6,k-l) ),industry )
**

**2. 变量说明**

- **<news87_vector_field/>** : 特指news87这类会议纪要数据中的向量（vector）字段。这些字段涵盖了发言的情绪、可读性、词汇统计等多个维度。本例中使用的 mws87_cfo_neu_logit_pres 就是一个典型字段，代表CFO（首席财务官）发言中的中性情绪得分。
- **<group_operator/>** : 分组运算符。我主要用了 group_median 来捕捉行业的中位数情绪，避免极端值干扰。也可以尝试 group_mean, group_rank 等。
- **<data_processing_op/>** : 数据处理运算符。我用了 floor 来对信号进行取整，目的是让信号对微小的、可能是噪音的波动不那么敏感，只在情绪偏斜度发生显著变化时才作出反应。
- **<d/>** : kth_element 的时间窗口。这里我用了较短的6天，是为了捕捉近期最显著的一次集体情绪偏斜。
- **<group/>** : 分组字段。这里用 industry 来定义同类股票群体，当然也可以扩展到 sector, country 等。

**3. 搜索空间的大小 (Search Space Size)**

- news87 包含数百个字段，而且搜索空间是多维度的。除了在模板内部排列组合不同的操作符（operator）、数据字段（datafield）和时间窗口（window），我们还可以将整个策略框架应用到不同的Region和Universe中去。

**4. 模板的Idea和Implement细节 (Idea and Implementation)**

- **核心Idea：**
  单个高管在一次发言中的情绪可能会有很大的偶然性，但如果一个行业内，多数公司高管的发言情绪呈现出一种非对称的、集体性的偏斜时，这往往预示着行业基本面或预期的共同变化。例如，如果一个行业内，多数公司的CFO都只是“轻描淡写”地提到正面信息，但有少数几位CFO“极度乐观”，这会形成一个正偏态分布。反之亦然。我们捕捉的正是这种行业共识的“情绪偏态”。
- **Implement细节：**
  - **数据处理（捕捉单次会议的情绪形态）：**
  1. vec_skewness(<news87_vector_field/>): 这是第一步，也是最关键的一步。它将一次会议中所有发言的情绪得分向量，提炼成一个单一的“偏度”数值。它衡量的不是情绪的平均值，而是情绪分布的对称性。
  2. kth_element(..., 6, k=1): 捕捉最近6天内的最小偏度值（即最左偏的信号）。我发现关注近期最悲观或最不乐观的集体情绪信号，往往更具预测力。
  3. floor(...): 对信号取整，使其更加稳健，过滤掉那些微不足道的偏度变化。
  - **主信号生成（提炼行业集体信号）：**
  - group_median(..., industry): 这是生成最终Alpha的核心。它计算的是同一行业内所有公司信号的中位数。这意味着，最终我们赋予每只股票的Alpha值，是它所在行业的集体情绪信号，而非它自身的信号。这样做极大地过滤了个股的噪音，让我们交易的是一个更纯粹的、行业层面的预期变化。

**5. 参数设置：**

- GLB,MINVOL1M,STATISTICAL,DECAY(0),DELAY(1)

**6. 产出效果**

- 我对这个模板在特定市场进行了回测，结果显示它能够稳定地产生信号。

**
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> LSOOK
> OOOK
> 3.50Ok
> 30OOK
> 25OOK
> ZOOOK
> 15OOK
> OOOK
> 5OOK
> Jan '19
> May '19
> SEp '19
> Nay '20
> Se0'20
> Jan '21
> Way 21
> Jan'22
> May 22
> SEP '22
> jan '23
> SEp 21
**

 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Sinale Data Set Alpha
> Power Pool Alpha
> Pyramid theme: GLBIDIIANALYST *1.5
> Aggregate Data
> SaroE
>   UFNUE「
> Ftness
> RetU「ns
> Uray'uoINT
> Marsin
> 1.64
> 45.239
> 1.05
> 18.449
> 7.9796
> 8.159600
 

**7. 建议其他顾问未来尝试的探索方向**

- **挖掘不同统计量：**  将 vec_skewness 替换为 vec_kurtosis (峰度)，可以用来捕捉情绪的“极端事件”风险，即行业内是否存在“极端一致”的乐观或悲观情绪。
- **双重中性化：**  除了 industry，可以尝试 group_cartesian_product(country, industry) 等更精细的分组，观察信号是否更强。
- **作为“情绪滤镜”：**  这个模板产生的信号代表了行业的“景气度”。可以把它作为一个条件，用 if_else 或 trade_when 来过滤其他Alpha。例如：if_else(本模板信号 > 0, 另一个动量Alpha, 0)，即只在行业情绪偏乐观时，才执行动量策略。

---

### 评论 #68 (作者: ML42552, 时间: 9个月前)

**Alpha模板Name：《可泛化mcr模板》**

模板

```
fill_data = ts_backfill(to_nan(<macro_data_field/>), 60);handle_data = ts_quantile(fill_data, 5, driver=gaussian);<ts_statistical/>(handle_data , <day/>)
```

具体变量1：<macro_data_field/>: 可以包含所有macro的数据字段进行遍历
具体变量2：<day/>: 可以是5，10，20，60，120

具体变量3：<ts_statistical/>: ts_mean, ts_max,ts_ir,ts_product 都有不错的效果

搜索空间的大小：以数据集mcr7为例的话，大约是22 * 5 * 5

模板的idea，implement细节：通过labs对mcr数据进行研究分析，处理0值和缺失值，对异常值进行正态分布处理平滑，最后进行时序处理，可泛化性较强。

产出效果：我回测了USA,GLB,EUR，一个数据集就能点亮塔。

具体分析思路可以参考我下面的帖子：

[[L2] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享_34584423754263.md]([L2] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享_34584423754263.md)

---

### 评论 #69 (作者: ZJ47021, 时间: 9个月前)

我就是来参考模版的！

---

### 评论 #70 (作者: CH92851, 时间: 9个月前)

很有用啊

---

### 评论 #71 (作者: MM27120, 时间: 7个月前)

新人报道：对我们目前来说很有意义，有了一个初步的指标概念，模板可以作为借鉴，自己慢慢去发现 去理解

---

### 评论 #72 (作者: WS48176, 时间: 5个月前)

snt27我生成的Alpha都是不完整的，缺乏几年数据。

---

### 评论 #73 (作者: MM27120, 时间: 5个月前)

感谢分享，多少还是学会了点东西

---------------------------------------------------

---

