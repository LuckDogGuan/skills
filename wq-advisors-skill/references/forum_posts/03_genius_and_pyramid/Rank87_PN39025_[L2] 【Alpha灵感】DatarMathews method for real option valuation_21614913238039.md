# 【Alpha灵感】Datar–Mathews method for real option valuation

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】DatarMathews method for real option valuation_21614913238039.md
- **作者**: TK53041
- **发布时间/热度**: 2 years ago, 得票: 21

## 帖子正文

**Paper:** Modeling Choices in the Valuation of Real Options: Reflections on Existing Models and Some New Ideas

**Author:**  Mikael Collan

**Link:**  [https://realoptions.org/openconf2011/data/papers/24.pdf](https://realoptions.org/openconf2011/data/papers/24.pdf)

Abstract: 本文讨论了期权的估值逻辑以及四种选定的实物估值方法。 根据他们的建模选择进行选择。 所选方法中的两种，DatarMathews 方法 [16, 24] 和模糊支付方法 [13] 代表了后来的发展 实物期权估值以及 Black & Scholes 公式和期权二项式模型 对实物期权估值中使用的更成熟的方法进行定价。 本文的目的是了解所使用的实物期权估值模型的总体情况 今天并讨论未来的建模观点。

Datar–Mathews 方法[1]（DM 方法）[2] 是一种实物期权估值方法。 该方法提供了一种简单的方法，只需使用项目积极结果的平均值即可确定项目的实际期权价值。 该方法可以理解为净现值（NPV）多情景蒙特卡罗模型的扩展，并针对风险规避和经济决策进行了调整。 该方法使用标准贴现现金流 (DCF) 或 NPV、项目财务评估中自然产生的信息。 它由西雅图大学教授 Vinay Datar 于 2000 年创建； 斯科特·H·马修斯 (Scott H. Mathews)，波音公司技术研究员。

**Method**

DM 方法的数学方程如下所示。 该方法通过在计算预期收益之前，以市场风险率 R 对营业利润的分布进行贴现，并以无风险利率 r 对全权投资的分布进行贴现，从而捕获实物期权价值。 那么选项值就是两个贴现分布之间的差值最大值或零的预期值。[3][4] 图。1。


> [!NOTE] [图片 OCR 识别内容]
> +M
> )0(
> $0
> 卫=0
> 
> Time, I
> Operating Profits, 3
> Launch Cost
> ($M)
> R&D Expenses
> 跖{)



> [!NOTE] [图片 OCR 识别内容]
> C
> 卫 |Inax
> (Sre
> Xe
> 0)]


C0 是单阶段项目的实物期权价值。 期权价值可以理解为两个现值分布之差的期望值，并在风险调整的基础上以经济合理的阈值限制损失。 该值也可以表示为随机分布。

Xt 是代表执行价格的随机变量。 在许多广义期权应用中，使用无风险贴现率。 然而，可以考虑其他折扣率，例如公司债券利率，特别是当应用程序是内部公司产品开发项目时。

St 是代表未来收益或 T 时刻营业利润的随机变量。R 是参与目标市场所需的回报率，有时称为最低回报率。

R 和 r 的不同贴现率隐含地允许 DM 方法解释潜在风险。 [5] 如果 R > r，则该期权将是风险规避的，这对于金融期权和实物期权来说都是典型的。 如果 R < r，则该选项将是风险偏好的。 如果 R = r，则这被称为风险中性选项，并且与 NPV 类型的决策分析（例如决策树）类似。 假设使用相同的输入和折扣方法，DM 方法给出与 Black-Scholes 和二项式格子期权模型相同的结果。 因此，这种非交易实物期权价值取决于评估者对市场资产相对于私人持有投资资产的风险感知。

DM 方法有利于在实物期权应用中使用，因为与其他一些期权模型不同，它不需要 sigma（不确定性度量）或 S0（当前项目的价值）值，而这两者都很难导出 用于新产品开发项目； 进一步参见实物期权估值。 最后，DM 方法使用任何分布类型的真实世界值，避免了转换为风险中性值的要求和对数正态分布的限制；[6] 进一步参见期权定价的蒙特卡罗方法。

其他实物期权估值方法的扩展已经开发出来，例如合同担保（看跌期权）、多阶段、早期启动（美式期权）等。

**Implementation**

DM 方法可以使用蒙特卡罗模拟 [7] 或以简化的代数或其他形式来实现（请参阅下面的范围选项）。

使用模拟，对于每个样本，引擎从 St 和 Xt 中抽取一个随机变量，计算它们的当前值，并取差值。[8][9] 图2A。 将差值与零进行比较，确定两者中的最大值，并由模拟引擎记录结果值。 这里，反映项目固有的选择性，净负值结果的预测对应于废弃的项目，并且具有零值。 图2B。 由此产生的值创建了一个收益分布，代表了在时间 T0 时项目的合理的、贴现的价值预测的经济合理集。


> [!NOTE] [图片 OCR 识别内容]
> ~Oiconns
> Owconins
> 
> 
> 
> ISBI
> +58
> (58)
> +58
> (SOI
> Fig. 2A Net profit present-value distribution
> Fig. 28 Rational decision distribution
> Fig. 2C Payoff distribution and
> option Value


当记录了足够的收益值（通常是几百）后，就可以计算收益分布的平均值或预期值。 图2C。 期权价值是预期值，即收益分布的所有正 NPV 和零的一阶矩。[10]

一个简单的解释是：


> [!NOTE] [图片 OCR 识别内容]
> Real option value
> arerage [Iax
> operating profit
> lalnch costs) , 0)]


其中营业利润和启动成本是到时间 T0 的现金流量的适当贴现范围。[11]

期权价值也可以理解为反映基础变量不确定性的分布C0。


> [!NOTE] [图片 OCR 识别内容]
> Simulation 32
> CODE
> RESULTS
> LEARN
> D4TA
> Settings
> USA/DITTOP3000
> Jul' 17
> Jn"18
> J0113
> Jan '19
> Jul' 19
> Jan 20
> Jul 20
> Jan '21
> Jul'21
> Jan'22
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> IS Summary
> Awerags
> Period
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OO0
> Aggregate Data
> ShaTC
> LUTTI
> LII2
> RetUTns
> UraVTgUVT
> Marain
> 1,46
> 8,01%
> 1,09
> 7,019
> 7,2996
> 17,500000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Vear
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Narqin
> Cownt
> Short Cownt
> Market
> 0,01
> -1 
> 0,22
> 333
> 3:
> 3,7550
> 2330:
> 123
> 1553
> PASTEURIZATION
> UNIT HANDLNG
> NAN HANDLING
> 713
> 12
> 351
> 0,51
> 552:
> 3
> 14740:
> 1232
> 15-7
> On
> Verify
> Off
> 2019
> 0,21
> 25
> V们
> :
> 47650
> 2,4190
> 1253
> 1-1
> 220
> T1
> 7,311
> 一3:
> 7
> 一7,560:
> 130
> 151+
> Save as Default
> Apply
> 7021
> 37:
> 1,7-
> 10,541:
> 47-51
> 25,330:
> 1153
> 1391
> 222
> 一5:
> 23,413
> 5
> 124,339.0:
> 1413
> 1733
> Vec_aVg(fnd6_newqeventvllo_optrfrq);
> mdf_gpr;
> 28;
> forward_price_20;
> 医 Correlation
> max(S*eXp(-rxt )
> Xxexp(-p t),0);
> rank(C)
> Self Correlation
> HiEhes: Correlation
> L+ RIn:
> IS Testing Status
> Clone tis Nphain a newtab
> Example
> Simulate
> Add Alpha
> CS
> Oponalohadotals
> newtab
> Check Submission
> Submit Alpha
> Sharpe
> Ung
> 5,05


我应用了该公式，结果显示出清晰的信号。 虽然2017年和2019年的夏普并不高，但近年来该指数表现非常好，屡创新高。 这表明 alpha 可能拥有良好的操作系统。我继续保持中立的市值排名，并取得了更好的成绩。


> [!NOTE] [图片 OCR 识别内容]
> 鬯臾
> Simulate
> Alphas
> Data
> 舀
> Competitions (1)
> @ Team
> Events
> Learn
> Consultant program
> Refer
> friend
> Simulation 32
> Simulation 35
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3000
> Jul' 17
> Jn"18
> J0113
> Jan '19
> Jul' 19
> Jan 20
> Jul 20
> Jan '21
> Jul'21
> Jan'22
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> IS Summary
> Awerage
> Period
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OO0
> Aggregate Data
> ShaTC
> LUTTI
> LII2
> RetUTns
> UraVTgUVT
> Marain
> 1,58
> 8,049
> 1,20
> 7,27%6
> 6,8096
> 18,08
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Year
> Sharpe
> TUIIOeT
> Htness
> Returns
> Drawdown
> Narqin
> Count
> Short Cownt
> Market
> 0,01
> 2017
> 070
> 3,35
> 1
> 2,3750
> 3,2393
> 5,570:
> 1-35
> 1551
> PASTEURIZATION
> HANDUNG
> NAN HANDLING
> 713
> 1,15
> 973
> 0,73
> 5,31
> 5.33
> 12,330:
> 1273
> 15-3
> Verify
> Off
> 2019
> 33
> 1
> 2,7550
> 4,7095
> 530:
> 1255
> 1-1
> 220
> 7
> 7,341
> 779
> 14,754
> 2-3
> 一0:
> 1
> 1575
> Save as Default
> Apply
> 7021
> 103
> 3-53
> 3
> 333
> 23,550:
> 1155
> 1395
> 222
> 723
> 一531
> 716
> 11,1
> 0.3491
> 5,35:0:
> 1-10
> 17-1
> Vec_avg(fnd6_newqeventvllo_optrfrq);
> mdf
> g
> 28;
> forward_price_2O;
> 医 Correlation
> max(S*exp(-p*t)
> Xxexp( -p t),0);
> Broup_neutralize(rank(C),bucket (rank(cap ),range=' 8.1,1,8.1'))
> Self Correlation
> HiEhes: Correlation
> L+ RIn:
> Qone this Alphaina neW tab
> IS Testing Status
> Incompatible unit for inputatindex
> expected "Unitp" found
> Unit[csprice:t]"
> Example
> SimMlate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> 0000
> Long
> UNIT


在论文中，作者提到了一些额外的变体：Algebraic_lognormal form 和 Triangle_form。您可以了解更多信息来构建新的 alpha. 希望这篇文章能够帮助大家获得更多构建 alpha 的灵感. 谢谢

---

## 讨论与评论 (3)

### 评论 #1 (作者: ZZ68826, 时间: 2 years ago)

请问这里使用的mdf_gpr字段是什么含义？是consultant才能使用的字段吗，谢谢

---

### 评论 #2 (作者: KJ42842, 时间: 2 years ago)

是model data的一个数据字段，目前该数据集已经下线。

---

### 评论 #3 (作者: MC63847, 时间: 1 year ago)

感觉贴现在这里没有起到作用，因为可以约掉然后直接等于max(S-X,0)

---

