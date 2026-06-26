# 【Alpha灵感】Cox–Ingersoll–Ross model

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】CoxIngersollRoss model_21473777737623.md
- **作者**: TK53041
- **发布时间/热度**: 2 years ago, 得票: 32

## 帖子正文

**Paper:** CIR Modeling of Interest Rates

**Link:**  [https://lnu.diva-portal.org/smash/get/diva2:1270329/FULLTEXT01.pdf](https://lnu.diva-portal.org/smash/get/diva2:1270329/FULLTEXT01.pdf)

在数学金融中，考克斯-英格索尔-罗斯 (CIR) 模型描述了利率的演变。 它是一种“单因素模型”（短期利率模型），因为它将利率变动描述为仅由一个市场风险来源驱动。 该模型可用于利率衍生品的估值。 它由 John C. Cox、Jonathan E. Ingersoll 和 Stephen A. Ross 于 1985 年[1] 引入，作为 Vasicek 模型的扩展。

CIR 模型使用基本仿射跳跃扩散的特殊情况，它仍然允许债券价格的封闭式表达。 可以在模型中引入时变函数替换系数，以使其与预先指定的利率期限结构和可能的波动性保持一致。 最通用的方法来自 Maghsoodi (1996)。[2] Brigo 和 Mercurio (2001b)[3] 提出了一种更容易处理的方法，其中将外部时间相关转变添加到模型中，以与利率的输入期限结构保持一致。

CIR 模型将利率变动确定为当前波动率、平均利率和利差的乘积。 然后，引入了市场风险因素。 平方根元素不允许出现负利率，并且该模型假设均值回归到长期正常利率水平。

本质上，利率模型是对利率如何随时间变化的概率描述。 使用预期理论的分析师利用从短期利率模型获得的信息，以便更准确地预测长期利率。 投资者利用有关短期和长期利率变化的信息来保护自己免受风险和市场波动的影响。

Lin Chen (1996) 给出了 CIR 模型对随机均值和随机波动率情况的显着扩展，称为 Chen 模型。 Orlando、Mininni 和 Bufalo 提出的所谓“CIR #”是处理集群波动、负利率和不同分布的最新扩展（2018 年、[4] 2019 年、[5][6] 2020 年、[7] 2021 年） ，[8] 2023[9]），迪弗朗西斯科和卡姆（2021，[10] 2022[11]）提出了一个关注负利率的更简单的扩展，被称为 CIR- 和 CIR-- 模型。

CIR模型描述了瞬时利率 rt 具有 Feller 平方根过程，其随机微分方程为


> [!NOTE] [图片 OCR 识别内容]
> drt = a(6 -
> rt)dt + OVTtdTTf;


其中 Wt 是维纳过程（对随机市场风险因子建模），a、b、sigma 是参数。 参数a对应于均值b的调整速度，sigma对应于波动性。 漂移因子 a(b-rt) 与 Vasicek 模型中的完全相同。 它确保利率向长期值 b 均值回归，调整速度由严格的正参数 a 控制。标准差因子 sigma*sqrt(rt) 避免了所有正值出现负利率的可能性的 a和b。 零利率也被禁止，如果条件


> [!NOTE] [图片 OCR 识别内容]
> 2ab >0?


已满足。 更一般地，当速率 rt 接近于零时，标准差也变得非常小，这减弱了随机冲击对速率的影响。 因此，当速率接近于零时，其演变将由漂移因子主导，从而推动速率向上（接近平衡）。

在 2ab = sigma^2 的情况下，Feller 平方根过程可以从 Ornstein-Uhlenbeck 过程的平方获得。 它是遍历的并且具有平稳分布。 它在 Heston 模型中用于模拟随机波动性。


> [!NOTE] [图片 OCR 识别内容]
> Distribution
> edit ]
> Future distribution
> The distribution of future Values of a CIR process can be computed in closed form:
> 工
> Tt+T
> 2C
> 2a
> 4ab
> @
> Where C =
> and Yis a non-central chi-squared distribution with
> degrees of freedom and non-centrality parameter 2cre
> 0
> 02
> Formally the probability density function is:
> f(rt+T; rt, 0,b,0) = ce
> '(")
> (2V0)
> 2ab
> Where 9 二
> 一1.U = CTte
> 0
> U = CTt+r ;
> and I (2V4) is a modified Bessel function of the first kind of order 9:
> 02
> Asymptotic distribution
> Due to mean reversion, as time becomes large, the distribution of T。 will approach a gamma distribution with the probability density of:
> 34
> flra; a,b.0) =
> &
> T(a)
> Where 8 = 2a
> and Q
> 2ab
> J?
> Bro
> /o?
> /02 _



> [!NOTE] [图片 OCR 识别内容]
> Properties
> edit
> Mean reversion;
> Level dependent volatility (OVTt);
> For given positive To the process will never touch Zero, i 2ab
> otherwise i can occasionally touch the Zero point;
> E[rt
> T0」
> Toe
> 十6(1
> ) So long term mean is b,
> ba2
> Varlrt
> r0]
> 二 T0
> Znt
> (1- e-at)? _
> 20
> Calibration
> edit
> Ordinary least squares
> The continuous SDE can be discretized as folloWs
> TttAt
> N =
> a(6
> T) At + a
> TtAtet;
> Which is equivalent to
> Tt+』t
> abAt
> aVTtAt + CVAtet;
> Vrt
> provided Et is n.ii.d. (0,1). This equation can be used for a linear regression。


鞅估计
最大似然
模拟

CIR 过程的随机模拟可以使用两种变体来实现：

离散化
精确的

债券定价
在无套利假设下，债券可以使用这种利率过程定价。 债券价格与利率呈指数仿射关系：


> [!NOTE] [图片 OCR 识别内容]
> P(t,T) = A(t,Te-B(tT)it
> Where
> Dabio?
> 2hela +h)(T
> A(t,T) =
> 2h + (a + A)(eh(T-H -1) _
> 2(eh(r-t) _1)
> B(t,T) =
> 2h + (a + h)(ehtr-t) _1)
> h =
> 十 2O
> Vaz


对于维纳过程，我向同学学习使用：quantile(returns, driver = gaussian, sigma = 1)。 关于导数，我应用了Brain Tips，即使用ts_delta函数。 变量 rt、a、b、sigma 均按模型公式中的方式实现


> [!NOTE] [图片 OCR 识别内容]
> Simulation 8
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3OOO
> IS Summary
> Ayerage
> Period
> UANGUAGE
> INSTRUMENT TYPE
> Aggregate Data
> Sharpe
> TUITNUEI
> SinEs
> TetlTn
> UCSTOI
> Marain
> Fast Expression
> Equity
> 1,41
> 12,159
> 1,22
> 9,3196
> 6,7896
> 15,319000
> REGION
> UNIVERSE
> DELAY
> Sharpe
> TIOVeT
> Ftnoss
> Returns
> Drawdown
> Marqin
> LoNg Count
> Short Count
> USA
> TOP3OOO
> 717
> 01
> 12,113
> 005
> 1753
> 55291
> 3:
> 134-
> 532
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 2013
> 12,033
> _
> 5,31
> 3.2593
> 10,520:
> 1524
> 121
> Market
> 0,02
> 719
> 236
> 11,339
> 14115
> 2.359
> 2350:
> -
> 1532
> 7020
> 12,351
> 3-3
> 27,471
> 5,7393
> 33170:
> -25
> 1572
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> 2021
> 043
> 12,303
> 022
> 3154
> 6,089
> 17:
> 1-1
> GJS
> On
> Verify
> Off
> 7022
> 32
> 12,31
> 2572
> 253
> ,750:
> 330
> 2234
> Apply
> SaVe as Default
> 医 Correlation
> pt =
> fnd6_intc;
> Self Correlation
> HiEhes: Correlatior
> Last Run:
> ts_mean(nt,22);
> ts_std_dev(rt, 20);
> drt
> ~(ts_delta(b
> pt, 22)/22)
> O*ts_delta(sqrt(rt) , 8 ) /8*quantile(returns,
> driver
> Baussian
> 5诏千
> 1);
> Broup_backfill(group_rank(drt,industry) , subindustry, 350);
> IS Testing Status
> 7 PuSS
> Sharpe of 1,41 isabove CUtOff of
> Finess of 1,22is abOVE CUtOffof1.
> TurnoiisrOf 12,15%
> aboie CUtoff or 1%.
> Qone tis Nphain
> Newtab
> Turnoerof 12,15% i below CUToff of 709
> Example
> Simulate
> udd Aphato
> List
> 口
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
> Vear


结果显示出清晰的信号，但我必须将衰减调整为 20 才能获得最佳性能。 2017年和2021年这两年的PnL并不是很好。 还有很大的改进空间，但我发现自己非常严格地遵循推荐的公式。我尝试使用power for rt来增强鲁棒性和信号，结果表明alpha有所改善


> [!NOTE] [图片 OCR 识别内容]
> Jul 17
> Jn"18
> J0113
> Jan '19
> Jul 19
> Jan 20
> Jul 20
> Jan '21
> Jul'21
> Jan'22
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> IS Summary
> Good
> Period
> USA
> TOP3OO0
> Aggregate Data
> ShaTOE
> LUTMOTer
> FIMESs
> ETUTR
> UF3doIn
> Marein
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 1,9
> 13,75%
> 1,93
> 14,029
> 7,53%
> 20,39
> Market
> 0,02
> Vear
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Narqin
> Cownt
> Short Cownt
> PASTEURIZATION
> UNIT HANDLNG
> NAN HANDLING
> -1 
> 0,90
> 133
> 61:
> 53
> 870
> 1475
> 521
> On
> Verify
> Off
> 713
> 1,71
> 13.57:
> 1,51
> 10,57:
> 37751
> 520:
> 535
> 1435
> 2019
> 13.351
> 73
> 1-41
> 5
> 22270:
> E-5
> 1455
> Save as Default
> Apply
> 220
> 3,24
> 13.751
> 476
> 29,701:
> 3,1550
> -31:
> E
> 143
> 7021
> 0,57
> 13571:
> 0,43
> 5-:
> 135
> 100:
> 457
> 537
> power(fnd6_intc,2);
> 222
> 10,10
> 12311
> 2406
> 70,351
> 534
> 20:
> 1030
> 2122
> ts_mean(rt,22);
> ts_std_dev(rt,20);
> 26
> drt
> (ts_delta(b
> rt, 22)/22)
> O*ts_delta(sqrt(rt) ,8 ) /8*quantile(returns
> driver
> gaussian,
> 51n
> 1);
> Broup_backfill(group_rank(drt
> Sector
> market, 350);
> 医 Correlation
> Self Correlation
> TiEhes
> UCrelaTiur
> L+ RIn:
> IS Testing Status
> Qone this Alphaina neW tab
> Example
> Simulate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> 0ooo
> Sharpe
> Ung
> ~E


我很好奇当切换到D0时alpha是否仍然保持其良好的性能。 我尝试了一下，令我惊讶的是阿尔法能够发送


> [!NOTE] [图片 OCR 识别内容]
> Simulation 32
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DOTTOP3OOO
> Jul 17
> Jn13
> Ju1'18
> Jan '19
> Jul 19
> Jan 20
> Jul 20
> J3n'21
> Jul'21
> Ja7'22
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> IS Summary
> Good
> Period
> USA
> TOP3OOO
> Aggregate Data
> Sharpe
> TICR
> Frnes
> EIICns
> TCaOCIIT
> Warein
> NEUTRALIZATION
> DECAY
> TRUNCATION
> 2,00
> 14,2196
> 2,05
> 14,9906
> 9,7596
> 0000
> Market
> 0,02
> Sharpe
> Turnover
> Ftnoss
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> 717
> 0,90
> 1--33
> 05
> 5171
> 9.753
> 50:
> -53
> 1523
> On
> Verify
> Off
> 2013
> 25
> 1-,35:
> 一
> 13,9750
> 23391
> ,450
> 1553
> 14-1
> 719
> 927
> 135
> 925
> 13293
> 24320:
> 1555
> 1535
> Apply
> SaVe as Default
> 7020
> 121
> 1-,143
> 23,543
> 3.2393
> 一2200:
> 652
> 14-4
> 2021
> 0,53
> 1141
> -3
> 5,S
> 7.1293
> 000:
> 1-29
> 111
> 7022
> 11,17
> 15,-31
> 3-1
> 72,15
> 0.153
> 3,300:
> 1275
> 552
> power(fnd6_intc,2.5);
> b = ts_mean(nt,22);
> std_dev(rt,12);
> drt
> ~(ts_delta(b
> pt, 28)722)
> O*ts_delta(sqrt (rt),8) /8*quantile(returns,
> driver
> Baussian, 5诏咀
> 1);
> 医 Correlation
> alpha
> group_backfill
> Broup_rank(drt, sector
> market, 358);
> trade_
> (volume>8.3*adv20,
> alpha,
> -1)
> Self Correlation
> Hishes: Correlation
> LaS LUI
> IS Testing Status
> Qone tis Nlphaina new tab
> Example
> Simulate
> udd Aphato
> Lst
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
> 21,1
> Vear
> t5_
> when


Cox-Ingersoll-Ross 模型有几个对其功能至关重要的关键假设。 首先，它假设均值回归。 这意味着随着时间的推移，利率倾向于向长期均衡水平移动，并且这种均值回归的速度由参数控制（如上式所示）。

其次，该模型考虑了波动性。 它承认利率在均值附近表现出随机波动，这些波动的幅度由上面的 σ 参数决定。 CIR模型强制执行利率的非负性，反映了利率不可能变为负值的现实。

该模型还假设时间均匀性、连续性和平稳性。 这意味着利率的动态不依赖于绝对时间参考，利率是平滑且可微的，并且一旦达到均值回归水平，其统计特性就不会随时间变化。 该模型通常假设利率变化呈正态分布，并遵循无套利原则，这意味着它为理解利率变动提供了一个合理且一致的框架。

---

## 讨论与评论 (5)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

这个文章我认为非常精彩！！！！使用了很独特的数据集。在BRAIN中，consultant还有很多关于企业债券信息或者违约概率的数据，欢迎您继续探索。

---

### 评论 #2 (作者: TK53041, 时间: 2 years ago)

非常感谢老师的评论。 在alpha研究过程中，我学到了很多新知识。 【Alpha灵感】专题是一个非常有用的系列。 希望能向老师和同学们学习更多。 老师，谢谢。

---

### 评论 #3 (作者: JZ71360, 时间: 2 years ago)

2013~2017, 表现很一般，基本 没有信号

---

### 评论 #4 (作者: SW76467, 时间: 2 years ago)

老师好，请问是根据哪个公式推导到brain表达式中的导数呢？

[TK53041](/hc/en-us/profiles/21206894234647-TK53041)

---

### 评论 #5 (作者: RY92144, 时间: 1 year ago)

我昨晚验证了你的方法，发现了一些问题：数据集本身确实有效，但过程中的求导和给出的公式对不上，有些让人费解。可以的话，希望你能进一步说明，这样更有助于我理解和改进。

---

