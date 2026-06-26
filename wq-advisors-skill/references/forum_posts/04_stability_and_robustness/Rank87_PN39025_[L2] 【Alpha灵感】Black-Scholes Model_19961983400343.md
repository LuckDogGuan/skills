# 【Alpha灵感】Black-Scholes Model

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Black-Scholes Model_19961983400343.md
- **作者**: DP11917
- **发布时间/热度**: 2 years ago, 得票: 25

## 帖子正文

文章：定价选择和企业责任
作者：费舍尔·布莱克和迈伦·斯科尔斯

关联: [https://www.cs.princeton.edu/courses/archive/fall09/cos323/papers/black_scholes73.pdf](https://www.cs.princeton.edu/courses/archive/fall09/cos323/papers/black_scholes73.pdf)

**什么是布莱克-斯科尔斯模型？** 
Black-Scholes模型，也称为Black-Scholes-Merton模型（BSM），是现代金融理论中最重要的概念之一。 该数学方程估计了基于其他投资工具的衍生品的理论价值，并考虑了时间和其他风险因素的影响。 它于 1973 年开发，至今仍被认为是期权合约估值的最佳方式之一。
Black-Scholes模型，也称为Black-Scholes-Merton模型（BSM），是现代金融理论中最重要的概念之一。 该数学方程估计了基于其他投资工具的衍生品的理论价值，并考虑了时间和其他风险因素的影响。 它于 1973 年开发，至今仍被认为是期权合约估值的最佳方式之一。

**布莱克-斯科尔斯假设** 
Black-Scholes 模型做出了某些假设：

- 不支付任何股息。
- 市场本质上是随机的（意味着市场趋势无法预测）。
- 购买期权没有交易成本。
- 标的资产的无风险利率和波动性是已知且恒定的。
- 标的资产的回报呈正态分布。
- 该期权是欧式期权，只能在到期时行使。

尽管最初的 Black-Scholes 模型没有考虑期权有效期内支付的股息的影响，但该模型经常被修改为通过确定除息日价值来计算股息。 标的证券。 许多出售期权的做市商也会修改他们的模型，以考虑到期前可能行权的期权的影响。

**Black-Scholes 模型公式** 
这个公式涉及的数学很复杂并且可能令人生畏。 幸运的是，您不需要了解甚至理解数学即可在自己的策略中使用 Black-Scholes 模型。 期权交易者可以使用许多在线期权计算器，并且当今许多交易平台都拥有强大的期权分析工具，包括执行计算的指标和电子表格，计算并给出期权价值的估计。
Black-Scholes 看涨期权公式是通过将股票价格乘以累积标准正态概率分布函数来计算的。 然后从先前计算的结果值中减去执行价格的净现值 (NPV) 乘以累积标准正态分布。


> [!NOTE] [图片 OCR 识别内容]
> Sckoles
> Formula
> %
> Slock
> [
> Hna I
> erpraho
> X= eercise
> G =
> Slaudard
> doiaho
> C4
> 「= nsl
> Cea
> IIerest
> Cle
> reUurns
> /
> 9。
> I
> C
> 
> C
> SoN(d) - Xe-rT(d〉
> 0
> In(&) +(ctr
> 02
> In(:)_<c
> S VT
> S U
> Black
> Price
> Price
> Log
> CvolaflH
> BsF
> eS



> [!NOTE] [图片 OCR 识别内容]
> C = SV(di) - Ke-rtV(da)
> There:
> ls - ( -
> "
> di =
> and
> d =41 - OsVt
> and where:
> C = Call option Price
> 5 = Current stock
> Or other underlying) price
> 丘 = Strike Price
> Risk-free iterest rate
> t = Time to maturity
> N
> 二4 Iormal distribution
> OsVt



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3OOO
> OOOK
> 5 = cIose;
> K = Call
> bpeakeven_Io;
> SOOK
> Vec_avg(fnd6_newqeventvllo_optrfrq);
> ts_std_dev( (returns
> 252);
> 厂 = 18;
> 2.7182;
> 41
> (exp(S/K)
> (+0^2/2)*T)/(o*sqrt(T));
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
> 42
> (exp(S/K)
> (-0^2/2)*T)/(o*sqrt(T));
> C = S*quantile(dI)
> Kve^(-peT)*quantile(d2);
> alpha
> -ts
> backfill(quantile(c),18);
> alphal
> trade
> (Volume<l. 2eadv28
> breakeven_Io,alpha,
> sqrt(advzo )
> hump(alphal, h叩p
> BOOOI
> IS Summary
> Awerage
> Period
> 05
> Aggregate Data
> Sharpe
> JUTICE
> Fitness
> REUTI
> UT3MOUWT
> Marsin
> 1,41
> 3,619
> 1,30
> 10,5896
> 7,459
> 58,589000
> Year
> TUINOeT
> Ftness
> Returns
> Drawdown
> Marqin
> Count
> Short Cownt
> 2015
> 3
> 3.35
> 7
> 173
> 5,979
> 40,0690
> 5
> 9
> 7017
> 1.37
> 3.75:
> 0,12
> 405
> 4373
> ~1,450.
> 357
> 1233
> 2013
> 1.30
> 35:
> 11
> 50
> 433
> 79.
> 1373
> 2019
> 0-5
> 3.35
> 0,20
> 1294
> 5,5101
> 13,569
> 11
> 1395
> 7020
> 231
> 297:
> +2
> 23,395
> 5
> 5719
> 113
> 1477
> 221
> 7,35
> 3::
> 27,+3
> 52120
> 4
> 11579933
> 1139
> 1433
> 医 Correlation
> Qone this Nlphain
> Newtab
> Self Correlation
> TiEhes
> UCrelaTiur
> L+ RIn:
> Example
> SImMlate
> udd Aphato
> List
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
> When
> Dut
> Sharpe
> Lonq



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3O00
> N Chart
> Pnl
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> L,SOOK
> USA
> TOP3OOO
> OOO
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industy
> 008
> 3.5OOK
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> 3,0OOK
> On
> Verify
> Off
> 2.5OOK
> Apply
> SaVe as Default
> Z.OOOK
> SOOK
> OOOK
> SOOK
> Jul '16
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
> SImMlate
> udd Aphato
> List
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha


在 alpha 中，我发现用 return 替换 log(return) 可以得到更好的结果。

需要考虑的事项：布莱克-斯科尔斯模型仅用于对欧式期权进行估值，并未考虑到美式期权可以在到期前行权。 所以我认为这个 alpha 版本需要更多改进才能在美国市场真正有效地发挥作用

现金流不灵活：该模型假设股息不变和无风险利率，但现实情况可能并非如此。 因此，由于模型的刚性，布莱克-斯科尔斯模型可能无法准确反映投资的未来现金流量。
假设波动率恒定：该模型还假设波动率在期权的整个生命周期内保持恒定。 事实上，这种情况通常不会发生，因为波动性会根据供需水平而波动。
误导性的其他假设：Black-Scholes 模型还使用其他假设。 这些假设包括没有交易成本或税收，无风险利率在所有期限内保持不变，收益可以用于卖空证券，并且不存在套利机会。无风险价格偏差。 这些假设中的每一个都可能导致价格偏离实际结果。

---

## 讨论与评论 (1)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

这个按理说应该是个量价的Alpha,但turnover显示它基本是一个基本面Alpha.所以我感觉这个Alpha基本已经被r这个指标dominant。我也在很多fundamental Alpha中见过类似的pnl。

造成这种现象的原因可能是数据的问题，建议分步检查一下。可能这个Alpha并没有完全实现作者想要实现的东西。

---

