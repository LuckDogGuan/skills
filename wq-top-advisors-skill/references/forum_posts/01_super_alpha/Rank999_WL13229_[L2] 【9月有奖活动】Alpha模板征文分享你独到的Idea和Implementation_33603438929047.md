# 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！

- **链接**: https://support.worldquantbrain.com[L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
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

## 讨论与评论 (30)

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
> Error: Could not find a backend to open `/home/guanjianxiong/code/ocr/images/img_708c39cfa6.png`` with iomode `r`.
> Based on the extension, the following plugins might add capable backends:
>   pyav:  pip install imageio[pyav]


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

- Reference:  [../顾问 CC40930 (Rank 95)/[Commented] Getting started with Risk DatasetsResearch_27157459347991.md?_gl=1*1orlfhc*_gcl_au*ODM4Njg5MjI5LjE3NDg1MjY5NDQ.*_ga*MTc0ODUyNjk0MTk2OTRmNjhiNDBjMGVlZTk.*_ga_9RN6WVT1K1*czE3NTMxOTg1NTgkbzI4OSRnMSR0MTc1MzE5OTYyNyRqNTYkbDAkaDA](../顾问 CC40930 (Rank 95)/[Commented] Getting started with Risk DatasetsResearch_27157459347991.md?_gl=1*1orlfhc*_gcl_au*ODM4Njg5MjI5LjE3NDg1MjY5NDQ.*_ga*MTc0ODUyNjk0MTk2OTRmNjhiNDBjMGVlZTk.*_ga_9RN6WVT1K1*czE3NTMxOTg1NTgkbzI4OSRnMSR0MTc1MzE5OTYyNyRqNTYkbDAkaDA) .
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

