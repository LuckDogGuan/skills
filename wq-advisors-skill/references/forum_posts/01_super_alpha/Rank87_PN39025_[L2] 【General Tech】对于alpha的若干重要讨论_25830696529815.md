# 【General Tech】对于alpha的若干重要讨论

- **链接**: https://support.worldquantbrain.com[L2] 【General Tech】对于alpha的若干重要讨论_25830696529815.md
- **作者**: YW93864
- **发布时间/热度**: 1 year ago, 得票: 20

## 帖子正文

**参考** ：

1. 兴业证券——高频系列研究报告之一，高频漫谈
2. Python量化交易员公众号若干文章
3. 亦往量化公众号若干文章

**概述** ：本篇是general tech的第二篇，第一篇中我们探讨了alpha合成的相关内容，从向量的角度理解了为什么相同datafield的alpha合成合理、如何再利用没用预测能力的alpha。本文聚焦于single alpha的绩效考核问题。

1. 在你是否知道为什么Brain回测出来的曲线是流动性最好的若干支股票的信号值加权组合？
2. 换手率低的因子透露了什么？
3. 为什么时序求均值可以提升alpha效果？
4. 为什么有时候我们需要做中性化neutralization？
5. “减法”、“除法”以及“回归去残差”三种从A中消除B的方法有和异同？

本文结合笔者最近的阅读总结出以下内容，其中大量内容为上述文章的浓缩和精选。


> [!NOTE] [图片 OCR 识别内容]
> Factor Investing Related Proo[
> Yimin TTI
> July 2024


1. 结论先行

先说明本文的结论，看看和大家的直觉是否相符：

1. 因子值多空加权组合可以近似为纯因子收益率，前提是在截面上（同一时点）的因子值异常值较少、分布均匀，最好近似均匀分布或正态分布；
2. 换手率低的因子通常截面分布较为稳定，但也有和收益之间的trade-off；
3. 时序求均值本质上是因子合成，其重要因素是每个截面上因子的预测能力较为稳定、方向相同；
4. 中性化本质上消除风险因子导致alpha收益受额外波动带来的影响
5. 减法和除法本质上也是回归，减法是系数等于1时的回归去残差，而除法是双对数后系数等于1的回归去残差

- 因子绩效篇

1. 首先，我们来讨论一下因子值的多空加权组合。

我们先定义一些向量以及其性质，如股票收益、股票仓位、收益在截面上的均值和方差等，出于方便，我们假设因子值在截面上服从正态分布，


> [!NOTE] [图片 OCR 识别内容]
> Proj Snppose the price of
> stock
> C time
> Xit then the retwrn, R,of i
> 9tt |
> Bosides,
> h
> Cross sectional) properties thnt
> E[R]
> 0, Var[R
> OI
> Further, suppose the position is denoted by
> and the IactorValte i denoted
> by Ft which is assimed followine normal distribution for simplicity; ie。
> R
> N(IR, &
> Xirl
> Ri
> Xi
> Rt+1
> P


我们进一步假设f是zscore后的因子值，进一步可以得到投资组合Rp的收益


> [!NOTE] [图片 OCR 识别内容]
> Lhe
> demoted hy ft the
> HILIT_T |TI
> After 4sorerl
> Mldl the
> TIITITI
> tIe
> portolin 
> |1, [t+1, 元
> Rttl = PT
> IFwe let 卫rl
> 声; then
> Rp
> Rtl
> R


由于，f是经过zscore的，那么它的L2范数退化为标准差，此时为1，因此可以化简为


> [!NOTE] [图片 OCR 识别内容]
> Since
> tle Hctor-value 1
> Z-scored。 this idlicates
> that fit follows
> standard
> Iortal distribltion, ie。
> f . Rttl
> R


通过pearson系数、协方差等统计量的定义，并结合sigma=1我们可以得到如下结果，即因子IC和下期收益有正相关关系


> [!NOTE] [图片 OCR 识别内容]
> From the definition; IC; (Information cocfficient) i dcoted by
> IC(fu, Ritr) = p(fi, Riti)
> By the dlefinition of tle Covariance。
> COV
> 凹(
> BIHI)(Y
> P[Y|
> E[{]
> E[HIE[]
> Ne have
> E[Rp;ttl] = 卫 [罕
> Rtyi]
> CO
> (f,Ru+])
> 0 * OJ
> CR
> = IC * GR+1
> L COICllsion
> based On the previols proof。 we kow that
> Both Ofthe Cross-scctional returns Of the stock nnd the IC Ive
> Dositivc
> relationslip vith the expectcd rcturn Of the portfolio


上述只是热身，我们进一步证明它和因子收益率的关系，由于f是zscore后的因子值，我们可以将其再展回去，具体如下


> [!NOTE] [图片 OCR 识别内容]
> Proaf Using the wotatiou mentioned before; tbe retru of the portfolio d
> te
> I Rprl]
> Rryt. Since
> '
> L
> f
> Ihe portfolio s retirn
> DC TCTntten
> Rtti
> OR
> (}:
> I
> Rr])
> (i* (:
> RitI) - IR;
> Rrr )
> CoV(C Rifi)
> Cr
> 章 0 $OR
> ORtl =TtTC
> OR
> CRti
> `8.
> +RxORry」
> OR
> OR
> Rtl
> R
> U
> TJe


至此，我们证明了因子收益率beta，近似为因子值加权组合，此外我们也可以知道因子投资和截面宽度是正相关的，即n, n为股票个数；与资产收益率的截面标准差正相关，因子投资本质是捕捉收益在截面上的差异；因子截面标准差虽然在分母上，但它不代表负相关，而是作为beta的比例系数，和beta之间动态平衡；如果到做模型的层面，X的标准差越大，反而更容易预测，因为beta的标准误会被缩小。但也要注意，本文的假设很严格，实际上，因子在截面上的分布很难是均匀或者正态，这种加权方式会导致幸存者偏差，比如由于因子的极端值对某一只股票上了很大的仓位。对于这种情况，解决方式为进行一个log(rank())处理，rank可以有效的减小偏度，使得分布更加均匀，log是lambda等于0的box-cox变换，数据更容易趋向正态。

- 因子稳定篇

1. 根据上述内容，我们继续深挖因子的稳定性，我们考虑一个换仓问题。由于，股票权重是因子值，那么我们可以得到t和t-1之间的股票权重差异，即为因子值差异。根据前文，我们假设因子值是服从正态分布的，那么其差值应该服从二元正态分布，差值的绝对值服从对称正态分布，根据对称正态分布求解出来的期望，我们可以发现，因子自相关越高，换手率低
2. 
> [!NOTE] [图片 OCR 识别内容]
> Prnnf
> Sof,
> Ive disclssed the topies ihont factors before fee. Let's disclss
> something after fee。 Suppose the rate Of the fee is C, then the actlil fee we
> T7(
> t0 py i
> CTO<
> SCCtion i
> CIIi
> I-I,il = C.Ifi - fiil
> where Ti A the weight Of the stock
> u time
> The
> ad f1 follow bivariate
> TIOTTI
> distribntion,
> f-f1~ (0,2(1 - p))
> Elf
> 尤川 =
> Tlor
> Know thnt 讦 the atocorrelation 』 small;
> tc TrIOVCP 咨
> CUTY
> 斥Vp
> Inrge


但是换手率低的因子，会损失收益，就好比你不能赚到短期的波段收益，就好比基本面因子和量价因子，基本面因子换手率低但收益也常常比量价因子小。

1. 上述我们说到，换手率低的因子，截面稳定性好，这说明尽管delay一天还是两天，甚至20天，因此都应当具备对未来的预测能力；我们通常会对不同的因子进行合成，这是截面的视角，而既然我们已知delay不同期的因子对未来某期有预测能力，那么我们也可以从时序上进行合成，最简单的就是等权平均。从数学上讲，假设G向量是我们已经处理好的因子加权值，那么它们可以乘以我们之前的股票截面向量，得到新的因子收益，这也能够解释为什么高频指标的 n 日平均因子表现往往会好于 单独使用 1 天的指标：因为多因子组合的效果往往好于单因子


> [!NOTE] [图片 OCR 识别内容]
> mean(GT)Rt+I
> (91+92+93 + + gn)TRtti/n
> (@lRtti + 9ZRt+i + 9Rtti + .  + ggRtti)/n
> RGnti


但我们也会看到随着n的增加，因子的预测能力也会衰减，这是因为，假设因子向量、收益向量在截面上均服从标准正态分布，


> [!NOTE] [图片 OCR 识别内容]
> 对于竽权组合 _
> 组合1Cn等于
> COD(gi Rrti) + cov(gz, Rrtl) +  +
> cov(gnRt])
> ICn
> std(Rtti)std(gi + 92 ++ gn)


最差的情况，随着n的增加，因子对未来的预测会逐渐变弱甚至相反（如长期动量和短期反转现象），因此分子的边际增长会变缓甚至递减，而因子标准差一般是稳定的，因此分母增长速度几乎不变，当分子分母边际错配时，IC就会衰减，如果会最优化的同学可以进一步解出IC和n的显示解，最暴力的方法即为n的遍历。

1. 另外，研报还提到为什么标准差因子有效。具体来说，假设动量因子被定义为某日日内分钟收益率的均值mu，假设j到t天动量因子是独立同分布的情况下，标准差就是mu的标准误，标准误衡量统计量与总体分布的参数值是否接近，标准误越小，样本对整体分布的代表性越好。事实上，动量因子的标准差就是波动率因子，波动率因子衡量了动量因子在时序上的差异，这种差异来自于动量因子在时序上分布的差异。波动率越大，股票含有的风险可能越大，因此需要更高的预期收益来补偿，所以波动率因子对股票截面收益率有预测能力。当然，笔者的个人理解为，对这种没有符号的因子（相似的例子为熵因子），如果有信号，那很可能是发现了市场上的异象，当这种异象消除时，该因子会有失效的可能。

- 因子消除篇

1. 首先，我们需要知道风险因子是长期回报很低甚至没有回报的因子，其最常见的表征是具有明显的风格变换能力，k.a均值回归能力，那么长期上该因子的期望为0；而真正有信号的alpha因子，长期上的期望（纯因子收益的期望）应该为非零常数。因子收益序列可以表示为如下，因为我们很难得到真正纯的因子，所以收益来源中会有其他因子的暴露


> [!NOTE] [图片 OCR 识别内容]
> 入 =Ap +刀


根据上述推论，我们可以知道lambda的期望即为纯因子收益的期望，


> [!NOTE] [图片 OCR 识别内容]
> B[入] =
> E[A]


我们发现风险因子收益消失了！！但如果考虑波动率，


> [!NOTE] [图片 OCR 识别内容]
> D[2]
> D[Ap] + D[A] + 2cov(pAr _


我们可以发现风险因子还在，这说明风险因子在长期上徒增了波动率，使得因子的风险回报较低，因此，我们需要进行中性化，将风险因子剔除，提高sharpe ratio

1. 最后，我们来探讨一下，减法、除法和回归取残差

Y=aX+b+ε是最常见的回归式

设a=1，我们可以发现Y-X=b+ε=C，C为常数，减法等价于回归系数为1的回归；

如果我们对Y和X取对数，log(Y)=alog(X)+b+ε，在计量经济学中，我们认为它是考虑X变动n%，Y会变动多少%，同样设置a=1，我们发现log(Y/X)=b+ε，取自然常数后，发现Y/X=exp(b+ε)=C，除法等价于a=1的回归

综上，我们需要思考在做减法时或除法时，因子表现好是否落入了关于回归系数的参数陷阱，因此可以考虑在做因子后加一步回归；其次，Y/X常用于财务指标，比如EP，净利润除以市值，如果净利润为负，此时EP就不是好的估值指标，log不支持负号，在统计和经济意义上都不支持负EP因子的存在；最后，Y/X在截面上也容易带来分布的问题，X极小，或者估值陷阱、红利陷阱（以红利陷阱而言，有的可能是相同分红的情况下，市值大幅缩水）

---

## 讨论与评论 (7)

### 评论 #1 (作者: CZ10093, 时间: 1 year ago)

是否能够分享一下《Factor investing related proof》这篇论文，google不到，谢谢。

---

### 评论 #2 (作者: YW93864, 时间: 1 year ago)

[CZ10093](/hc/en-us/profiles/26965592415639-CZ10093)

您好，《Factor investing related proof》是我自己的笔记，所有内容已经呈现在论坛中

---

### 评论 #3 (作者: LL87164, 时间: 1 year ago)

您好！您文中提到的第一篇（第一篇中我们探讨了alpha合成的相关内容）是指下面的这篇吗？

### [【Alpha灵感】特质盈利因子]([L2] 【Alpha灵感】特质盈利因子_24728011984151.md)

---

### 评论 #4 (作者: YW93864, 时间: 1 year ago)

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)

Hi, 抱歉回复晚了。

alpha合成的相关内容请看《【SuperAlpha灵感】从面试题到RegularAlpha和SuperAlpha的思考》

```
[L2] 【SuperAlpha灵感】从面试题到RegularAlpha和SuperAlpha的思考_23521891229207.md
```

---

### 评论 #5 (作者: WX16829, 时间: 1 year ago)

文章提到因子值多空加权组合的有效性依赖于因子值在截面上的分布均匀性。可以考虑对因子值进行 `rank()` 或 `log(rank())` 处理，以减少偏度并使分布更接近正态分布。

另外，文章提到波动率因子的有效性可能源于市场异象。可以通过分析市场行为（如投资者情绪、交易量异常）挖掘潜在的Alpha因子。

---

### 评论 #6 (作者: AA53991, 时间: 1 year ago)

感谢总结

---

### 评论 #7 (作者: LY67324, 时间: 3 months ago)

感恩分享，很值得学习的一篇文章！

---

