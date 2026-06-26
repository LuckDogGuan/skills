# 【Alpha灵感】Merton’s Model in Credit Risk Modelling

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Mertons Model in Credit Risk Modelling_20519180987927.md
- **作者**: Nguyen Dang Huynh(HN14753)
- **发布时间/热度**: 2 years ago, 得票: 15

## 帖子正文

标题：Merton’s Model in Credit Risk Modelling

作者: Junior BOULLEYS, Adonis TCHEUGUI, Hermann NGAMENI

Link:  [https://www.tnpconsultants.com/wp-content/uploads/2023/06/Merton-Model-in-Credit-Risk-Modelling-version-2023.pdf](https://www.tnpconsultants.com/wp-content/uploads/2023/06/Merton-Model-in-Credit-Risk-Modelling-version-2023.pdf)

概括: 在这篇简短的论文中，我们首先介绍默顿模型，这是信用的基本模型 风险建模。 默顿模型是一种违约结构模型，其中违约发生在 当公司资产的市值低于预定阈值时到期 由负债定义。 然后我们描述公司的违约概率并显示一些 比较静态分析。此外，我们还展示了一些众所周知的优点和缺点 模型。 最后，一些模型衍生了默顿模型，例如CreditMetrics、KMV模型 描述了信用风险加。

**什么是默顿模型？** 
默顿模型是股票分析和商业贷款官员等可以用来判断公司信用违约风险的数学公式。 默顿模型以 1974 年提出的经济学家罗伯特·C·默顿 (Robert C. Merton) 的名字命名，通过将公司股权建模为资产的看涨期权来评估公司的结构性信用风险。


> [!NOTE] [图片 OCR 识别内容]
> Assets
> At =
> Aoelfs-H)s+0a}
> E(AT) =
> Ao
> Probability of Default
> P(AT 三D)
> Time
> (todav)
> T (debt maturity)
> Aoe()
> AAMMNN


**默顿模型告诉您什么？** 
默顿模型可以更轻松地对公司进行估值，并通过分析其债务到期日和债务总额来帮助分析确定该公司是否能够保留偿付能力。

默顿模型计算欧式看跌期权和看涨期权的理论定价，不考虑期权有效期内支付的股息。 然而，该模型可以通过计算标的股票的除息日价值来考虑股息。

默顿模型做出以下基本假设：

所有期权均为欧式期权，仅在到期时行使。
不支付任何股息。
市场走势是不可预测的（有效市场）。
不包括佣金。
基础股票的波动性和无风险利率是恒定的。
标的股票的回报呈规律分布。
公式中考虑的变量包括期权的执行价格、当前标的价格、无风险利率以及到期前的时间。

**默顿模型的公式**

**
> [!NOTE] [图片 OCR 识别内容]
> 卫 = TN (di)
> Ke-rATN (d)
> Where:
> 皿装- (一
> 4T
> d1 =
> and
> d =d1
> OuVAt
> 卫 = Theoretical value Of a colpany's equity
> T = Vallle Of the company's assets i period t
> k = Value ofthe compaly's debt
> t =
> Current time period
> 工 = Future time period
> 工 = Risk-free interest rate
> T
> Cumulatire standard Iormal distribution
> Exponential term (i.e.2.7183.
> 「 =
> Standard deriation Of stock returls
> OuVAI
**

**
> [!NOTE] [图片 OCR 识别内容]
> Simulation
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3OOO
> N Chart
> Pnl
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 5.OOO
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OOO
> L,SOOK
> NEUTRALIZATION
> DECAY
> TRUNCATION
> LOOO
> Subindustry
> 008
> 3.5OOK
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> On
> Verify
> Off
> 3,0OOK
> 2.5OOK
> Apply
> SaVe as Default
> 2.0OOK
> Vt
> ts_delay
> assets, 252);
> K = debt_It;
> SOOK
> ts_backfill(fnd6_optrfr,24)
> t1 =24;
> t =252;
> OOOK
> sigma
> ts_std_dev(returns, 24);
> SOOK
> 41
> (IOg(Vt/K)
> ( + 51n^2/2)*t1) /(sima*sqrt(ti) );
> 42 =
> 5ina*sqrt(tI);
> Vt*rank_hy_side(dI)
> Kexp
> -pst) srank_by_side(d2);
> alpha
> =-ts_decay_exP_window(ts_decay_linear(E, 408 ),350);
> Broup_backfill(alpha, subindustry, 24)
> Jul'16
> Jan '17
> Jul'17
> Jan'18
> Jul'18
> Jan '19
> Jul'19
> Jan'20
> Jul '20
> Jan '21
> Qone this Nlphain
> Newtab
> Example
> Simulate
> udd Aphato
> List
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
**

**
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Sood
> Period
> Aggregate Data
> Sh3rO
> LUTISe
> Fitness
> R2tU「ns
> UraVgUVn
> Marein
> 1,60
> 1,959
> 1,51
> 11,1496
> 9,8296
> 114,029600
> Vear
> TUIOVeT
> Htness
> Returns
> Drawdow
> Margin
> Count
> Short Count
> 2115
> 1,51
> 2151:
> 9,0395
> 5,0295
> 5350
> 1-
> 92
> 217
> 1,73:
> 53
> 2313
> 375-
> 1925
> 97
> 2113
> 2231:
> 411
> 3:1
> 4352
> 593
> 933
> 119
> 019
> "731:
> 25
> 1:
> 1-1
> 931
> 220
> 2,27
> 313
> 2,733
> 4,359
> 217,5056s
> 32
> 21
> 553
> 2171:
> 2597
> 115,551
> 751
> 0737-
> 201
> 313
> Sharpe
> Uomo
**

Alpha效果很好，甚至可以送上top1000

**
> [!NOTE] [图片 OCR 识别内容]
> Simulation 13
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP1000
> Jul'16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul 19
> Jan '20
> Jul '20
> Jan'21
> Vt
> ts_delay(assets, 252);
> K = debt_It;
> [
> ts_backfill (fnd6_optrfr, 24 )
> IS Summary
> Ayerage
> Period
> t1 =24;
> t =252;
> 5iu
> ts_std_dev(returns, 24);
> Aggregate Data
> Sharpe
> TICNOE
> Fitns
> Retlrm
> UCaTTOT
> Marain
> 1,42
> 2,389
> 1,16
> 8,40%
> 5,7696
> 70,579000
> d1 = (Iog(Vt/K)
> ( + 51n^2/2)*t1) / (slna*sqrt(tl) );
> 11
> 42 =
> *sqrt(tI);
> Sharpe
> Turnover
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> E = Vt*rank_by_side(dl)
> Ksexp(-pet) *rank_by_side(d2);
> 715
> 0,35
> 351
> 一15:
> 4361
> 23,350:
> S-5
> 37
> alpha
> =-tS_decay
> eXP_window(ts_decay_Iinear(E, 488),350);
> Broup_backfill(alpha, subindustry, 24)
> 2017
> 203:
> 一
> 351:
> 1,4150
> 97,300:
> 713
> 0,15
> 7:
> 00-
> 1.3:
> 7530
> 330:
> SJ
> 33
> 719
> 1,11
> 2-5:
> 0,79
> 3
> 3-
> 51,30:
> 525
> 2020
> 1,55
> 35::
> 13:
> 4_-
> 1-11
> 535
> 37
> 7021
> 1,25
> 2,19*
> 1,1
> 0,7751
> 533,420
> 55
> 323
> Correlation
> Self Correlation
> Hishes: Correlation
> LaS LUI
> IS Testing Status
> Qone tis Nlphaina new tab
> Example
> Simulate
> udd Aphato
> Lst
> Oponalpha dotals
> new tab
> Check Submission
> Submit Alpha
> 5loa
> Vear
> Fitmess
> 〈51
**

我严格按照作者提到的公式实现了alpha表达式，结果相当不错。此外，作者还提到了该模型的一些变体，例如 Moody’s KMV model. 我意识到这个模型有很多变体，从中可以有很多想法来创建许多不同的阿尔法


> [!NOTE] [图片 OCR 识别内容]
> 2.1
> Noody's KNIV model
> The KMI model try tO overcome some Haws Of the Merton's model
> KMIV modelis developed
> by Moody s Analytics in 2002. In KMV model we model the Expected Default Frequency (EDE)
> Whichis the expected probability that
> eiven counlerparty default within one yeur。 Itis
> Slructurll
> model meaning that the default happens when the market value Of the ussets Of the company。 at
> malurily。 is smaller thdn the value Of liabilities。
> From equalion (1.12) We Can wrile down the
> followine equation。
> PD =$(d2)
> 1.1)
> With 0 二 1
> the survival function of the Gaussian distribution
> Dr is replaced by DT tal
> Tellect the Company
> liabilities payable with one year。 KMV model consider the distant to default
> defined ds
> A0
> Dr
> ODT
> In the Moody'
> KMV。the survival function 0 is remplaced by
> decreasing function estimaled
> using data. This function is denoted @Kv and the Expected Default Frequency becomes
> EDF = NMv(d)
> (2


结果表明生成的alpha有正信号


> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Simulation 14
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3OOO
> Jul'16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul 19
> Jan '20
> Jul '20
> Jan'21
> UANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> IS Summary
> Ayerage
> Period
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OOO
> Aggregate Data
> Sharpe
> TICNOE
> Fitns
> Retlrm
> Drawgowr
> Warain
> 1,43
> 3,51%
> 1,01
> 6,2596
> 7,819
> 35,66900
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Sharpe
> Turnover
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> Subindustry
> 008
> 715
> 1,39
> 337:
> 一23:
> 1151
> 21,550:
> 1413
> 502
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> 2017
> 3.521
> T-
> ::
> 14930
> 50:
> 14-3
> 1537
> Verify
> Off
> 713
> -1,70
> 3-:
> -1,19
> 11:
> 1.3151
> -35,340
> 1421
> 1535
> 719
> _30
> 3-3:
> 01
> 357:
> 0550
> 5430:
> 1433
> 1575
> Apply
> SaVe as Default
> 2020
> 1-
> 33:
> 4
> 21,17*
> 371
> 132,500:
> 14-
> 12
> 7021
> 577
> 34:
> 12,51
> 3544
> 503i
> 207,500:
> S-
> 1533
> debt;
> 5ln
> ts_std_dev(returns, 24);
> ts_delay(assets, 252);
> d = (Ao
> Dt) /(sigma Dt);
> 医 Correlation
> group_backfill(rank_by_side(d),sector, 350)
> Self Correlation
> Hishes: Correlation
> LaS LUI
> IS Testing Status
> Qone tis Nlphaina new tab
> Example
> Simulate
> udd Aphato
> List
> Oponalpha dotals
> newtab
> Check Submission
> Submit Alpha
> Vear
> Fitmess
> 0,15


另外，作者还提到了CreditMetrics模型和CR+


> [!NOTE] [图片 OCR 识别内容]
> 2.2
> Creditletrics model
> CreditMetrics is a model introduced by Jp Morgan in 1997. Despite the fact that the model relies
> OI the
> normality assumption
> it presents one interesting characteristics。
> The default threshold is defined
> credit ratings not liabilities as in the Merton s model。
> Thus; i takes into account both the default risk and the credit deterioration which is the
> second component Of the credit risk。
> The model allows for the computation of both the probability of default and the probability
> Of credit deterioration
> using



> [!NOTE] [图片 OCR 识别内容]
> 2.3
> Credit Risk Plus
> Credit Risk Plus is itroduced 皿 1997, CRt is a rather powerful model, which allows for the
> modeling of complex portfolios of instruments-
> In this model, default probability is conditionally
> poisson distributed. It is not a structural model but rather a mixture model. The model is actually
> used by banks because it introduces
> IIOIC
> realistic components such as
> Correlation and dependence among defaults。
> Variable default rates
> Some macroeconomic factors are introduced in order to take into account economic trends
> and cycles


我找到了更多提供 CR+ 公式的文档，但目前我无法在 Brain 上将公式应用到 alpha 中。 我想在这里发布文章链接，以便同学们学习和讨论


> [!NOTE] [图片 OCR 识别内容]
> This relation Is
> knowing that G(2) verify the following condition:
> 卫ak
> Ciroez
> @@) _
> G(
> =8
> 1-)
> Ci
> Generally; the CreditRiskt model is based on mathematical techniques "
> the modeling of the distribution of the losses 边 the field of the banking
> activities and of the
> isurance。 The behavior of common default of the
> borrowers is incorporated by treating the rate Of default as
> 9 COIlOn
> random variable for multiple borrowers。 So, the
> borrowers are assigned
> among the sectors among Which each has
> a rate Of average default and
> volatility Of rate Of default: The volatility Of rate of default is the standard
> deviation
> Which would be observed
> On
> portfolio of infinitely diversified
> homogeneous credit。
> applied
> being


[https://hal.science/hal-01696011/document](https://hal.science/hal-01696011/document)

[https://courses.edx.org/c4x/DelftX/TW3421x/asset/Week6_PD3_3.pdf](https://courses.edx.org/c4x/DelftX/TW3421x/asset/Week6_PD3_3.pdf)

---

## 讨论与评论 (0)

