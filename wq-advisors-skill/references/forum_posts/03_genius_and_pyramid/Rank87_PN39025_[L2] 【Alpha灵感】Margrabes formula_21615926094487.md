# 【Alpha灵感】Margrabe's formula

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Margrabes formula_21615926094487.md
- **作者**: Nguyen Dang Huynh(HN14753)
- **发布时间/热度**: 2 years ago, 得票: 23

## 帖子正文

**Paper:** Pricing and hedging Margrabe options with stochastic volatilities

**Link:**   [https://econ-papers.upf.edu/papers/1475.pdf](https://econ-papers.upf.edu/papers/1475.pdf)

**Abstract:**  Margrabe 或交换期权是一种将一种资产交换为另一种资产的期权。 在 一般随机波动率框架，以第二项资产作为计价单位， 我们推导了 Margrabe 期权的定价以及近似定价公式。 这 作为具体例子，研究了相关的 Stein & Stein 模型和 3=2 模型。 此外，我们推导了一般均值-方差最优对冲策略，并表明它是 仅在资产价格与波动性之间零相关性的情况下进行德尔塔对冲。

在数学金融中，Margrabe 公式[1] 是一种期权定价公式，适用于到期时将一种风险资产交换为另一种风险资产的期权。 它由 William Margrabe（芝加哥博士）于 1978 年推导出来。Margrabe 的论文已被 2000 多篇后续文章引用。[2]

假设 S1(t) 和 S2(t) 是两种风险资产在时间 t 的价格，并且每种风险资产都有恒定的连续股息收益率 qi。 我们希望定价的期权 C 赋予买方在到期 T 时将第二种资产交换为第一种资产的权利，但没有义务。换句话说，其收益 C(T) 为 max (0，S1(T) - S2(T))。

Margrabe 公式指出，期权在时间 0 的公平价格为：


> [!NOTE] [图片 OCR 识别内容]
> 9iT
> Si(O)N(di)
> e q2T
> S(O)N(d)
> Where:
> 41, q2 are the expected dividend rates Ofthe prices S1, Sz underthe appropriate risk-neutral measure;
> N denotes the cumulative distribution function Tor
> Standard normal,
> (皿(51(0)/5,(0)) - (@2
> /2)卫)JoI;
> 4 =di 一 OVI
> 十@


**Derivation**

马格拉布的市场模型仅假设两种风险资产的存在，其价格像往常一样被假设遵循几何布朗运动。 这些布朗运动的波动性不需要恒定，但重要的是 S1/S2 的波动性 σ 是恒定的。 特别是，该模型不假设存在无风险资产（例如零息债券）或任何类型的利率。 该模型不需要等效的风险中性概率测度，但需要 S2 下的等效测度。

通过将情况简化为我们可以应用布莱克-斯科尔斯公式的情况，该公式很快得到了证明。

首先，将两种资产视为以 S2 为单位定价（这称为“使用 S2 作为计价单位”）； 这意味着第一个资产的一个单位现在价值第二个资产的 S1/S2 个单位，而第二个资产的一个单位价值 1。
在计价定价的变化下，第二项资产现在是无风险资产，其股息率 q2 是利率。 根据计价单位的变更重新定价的期权收益为 max(0, S1(T)/S2(T) - 1)。
因此，原始期权已成为第一个资产（及其计价定价）的看涨期权，行使价为 1 个单位的无风险资产。 请注意，即使定价发生变化，第一项资产的股息率 q1 仍保持不变。
应用 Black-Scholes 公式，将这些值作为适当的输入，例如 初始资产价值S1(0)/S2(0)、利率q2、波动率σ等，给出了计价定价下期权的价格。
由于生成的期权价格以 S2 为单位，因此乘以 S2(0) 将撤消计价单位的更改，并给出以原始货币表示的价格，这就是上面的公式。 或者，可以通过吉尔萨诺夫定理来证明这一点。


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OO0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 001
> PASTEURIZATION
> UNIT HANDLNG
> NAN HANDLING
> On
> Verify
> Off
> Save as Default
> Apply
> 9 = dividend;
> 51 = CIose;
> 52 =
> ts_delay(open,1);
> 5IBIa
> ts_std_dev(close, 22);
> T =
> 22;
> 01 =
> (108(51/52) + (9 + sigma^2/2)*22) /sigma*sqrt(22);
> d2 = dI - slna*sqrt(T);
> Margrabe
> eXP (
> q*T)sSI rank(dI)
> eXP(-9*T)*52*rank(d2) ;
> Broup_backfill
> quantile(Margrabe
> market, 20);



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Needs Improwement
> Period
> Aggregate Data
> Sh3TOE
> UPICEI
> FIMESs
> RetUTns
> STaVOCT
> IaVeIn
> 1,60
> 48,5296
> 0,78
> 11,5696
> 5,4796
> 4,769000
> Vear
> TUINOVeT
> Htnoss
> Returs
> Drawdown
> Margin
> Count
> Short Count
> 2117
> 705
> 43331
> 4
> 27:
> 2211:
> 25
> 1-1
> 1435
> 213
> 095
> 47,32:
> 1.23
> -71:
> 25:
> 631
> 533
> 1515
> 2119
> 705
> 1.35
> 37:
> 3,151:
> 3,655030
> 135
> 1475
> 21
> S0,14:
> 一1
> 3,701:
> 12,315030
> 147
> 721
> 0,93
> 43,74:
> 1-3
> 10.331
> 5-7:
> 4,259
> 554
> 1524
> 2022
> 4-5:
> -3,75:
> 54:
> _
> 1523
> 1557
> Sharp
> Long
> 47,974
> -
> 5711


按照方程实施alpha后，发现有明显的信号，但换手率很高，适应度没有通过回测。 所以我添加了一些关于数量和市值的条件。 添加条件后的结果现在可以发送


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> PI_
> SOOK
> OOOK
> 3,5OOK
> OOOK
> SOOK
> Z.OOOK
> SOOK
> OOOK
> SOOK
> Jul
> Jan'18
> Ju1'18
> Jan '19
> Jul 19
> Jan 20
> Jul 20
> Jan'21
> Jul'21
> Jan'22
> 4



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Ayerage
> Perioq
> Aggregate Data
> Sharpe
> TUITNCE
> SinEs
> TetlTn
> Urayon
> Marein
> 2,02
> 33,679
> 1,10
> 10,0596
> 3,219
> 5,979000
> Sharpe
> Turnover
> Htnoss
> Returns
> Drawdown
> Marqin
> LoNg Count
> Short Count
> 717
> 3513
> 33
> 35*
> 32
> 1237
> 1224
> 2013
> 34,703
> 070
> 08*
> 3:
> 5
> 12
> 1255
> 719
> 3913
> 0.33
> 5-4
> 23:
> 302
> 1273
> 1257
> 7020
> 355:
> -57:
> 2-1:
> 05:
> 1237
> 1233
> 2021
> 392:
> 1225
> 321
> 7,93503
> 1327
> 13332
> 7022
> 73.92
> -34,71*
> 251:
> -24,015
> 131
> 1353
> Vear


我尝试在 D0 上构建 alpha，它也给出了清晰的信号，但目前无法发送


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> NEEOs ImprOVEMER
> Period
> Aggregate Data
> Sh3rO
> LUPMO'Er
> FIMess
> RetUTn=
> UFaMUoVT
> Marain
> 1,79
> 40,6496
> 0,77
> 7,5706
> 4,21%
> 3,739000
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> 2717
> 9:
> 55
> 1721
> 34
> 1195
> 1231
> 2313
> -5-5:
> 7,393
> 5
> 一:
> 1
> 153
> 2719
> 7,31
> 31:
> 303
> 55
> 117
> 1255
> 177
> 2720
> 331:
> 2+3
> 17,773
> 32
> 545
> 1270
> 1303
> 2721
> 314:
> 3
> 421
> 一71
> 1315
> 1323
> 2
> 331
> 3-
> -37,3391
> 2+51
> -2233
> 13-
> 1327
> Yoar


---

## 讨论与评论 (1)

### 评论 #1 (作者: ML45463, 时间: 2 years ago)

d1的formula应该是

```
(log(S1/S2) + (q + sigma^2/2)*T) / (sigma*sqrt(T))
```

但这样便没有了信号，所以这结果应该是误打误撞出来的：）

---

