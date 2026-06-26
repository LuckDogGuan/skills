# 【Alpha灵感】vasicek interest model

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】vasicek interest model_20238317296791.md
- **作者**: TN48752
- **发布时间/热度**: 2 years ago, 得票: 8

## 帖子正文

Paper: An Overview of the Vasicek Short Rate Model

Author: Nicholas Burgess

Link:  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2479671](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2479671)

Vasicek 利率模型一词是指对利率变动和演变进行建模的数学方法。 它是基于市场风险的单因素短期利率模型。 Vasicek 利率模型在经济学中常用来确定未来利率的走势。 简而言之，它估计利率在给定时间内的变动情况，可用于帮助分析师和投资者了解未来经济和投资的走势。

Vasicek 利率模型如何运作
预测利率如何演变可能很困难。 投资者和分析师有许多可用的工具来帮助他们了解随着时间的推移他们将如何变化，以便就他们的投资和经济做出明智的决策。 Vasicek 利率模型是可用于帮助估计利率走向的模型之一。

如上所述，Vasicek利率模型，通常称为Vasicek模型，是金融经济学中用于估计未来利率变化的潜在路径的数学模型。 因此，它被认为是随机模型，这是一种有助于做出投资决策的建模形式。

它将利率的变动概括为由市场风险、时间和均衡价值组成的因素。 随着时间的推移，该比率往往会恢复到这些因素的平均值。 该模型通过考虑当前市场波动性、长期平均利率值和给定的市场风险因素，显示给定时间段结束时利率的最终结果。

Vasicek 利率模型使用以下等式对瞬时利率进行估值：


> [!NOTE] [图片 OCR 识别内容]
> drt
> a(6 - r)dt - GdTTt
> Where:
> TT
> Random Iarket risk (represented by
> TTiener Process)
> t =
> Time period
> a(6
> r) = Expected change 边 the iterest rate
> at tile t (the drift factor )
> Speed oftle reversion to the Iean
> 6 =
> term lerel of the Ieall
> Tolatility at time t
> Long-t


该模型指定瞬时利率遵循随机微分方程，其中 d 指其后面变量的导数。 在没有市场冲击的情况下（即，当 dWt = 0 时），利率保持不变 (rt = b)。 当 rt < b 时，漂移因子变为正值，这表明利率将朝着均衡方向增加。

如前所述，Vasicek 模型是一种单因素短期利率模型。 单因素模型是一种仅通过考虑利率来识别影响市场回报的一个因素的模型。 在这种情况下，市场风险就是影响利率变化的因素。

该模型还考虑了负利率。 在经济不确定时期，利率降至零以下可以为央行当局提供帮助。 尽管负利率并不常见，但事实证明负利率有助于央行管理经济。 例如，丹麦央行在 2012 年将利率降至零以下。两年后，欧洲银行也紧随其后，日本央行 (BOJ) 也紧随其后，于 2016 年将利率降至负值。
1
世界经济论坛。 “负利率：绝对是你需要知道的一切。” 访问日期：2021 年 12 月 28 日。


> [!NOTE] [图片 OCR 识别内容]
> Simulation
> CODE
> RESULTS
> LEARN
> D4TA
> Settings
> USA/DITTOP3000
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
> #dnt
> k* (O-rt)dt
> Gdllt
> #pt
> 日 + (r
> O)*e^-k
> OjO->t e^k* (5-t)dls
> ts_delta(fam_roe
> rank, 22);
> ts_std_dev(IOB(returns ),22);
> IS Summary
> Awerags
> Period
> G
> ts_delta(systematic_risk_last_3O_days,30)
> drt
> dl;
> Aggregate Data
> ShaTC
> LUTTI
> FITESs
> KETUFRS
> P3UCC
> Warsin
> alpha
> Broup_neutralize(rank(dnt )
> bucket (rank(cap),
> range
> '0.1,1,8.1'));
> 1,52
> 13,569
> 1,06
> 6,579
> 3,439
> 9,65
> alphal
> trade_when(days_from_last_change(rel_ret_comp) ==0,alpha,
> 1;
> kth_element (alphal, 252,k="1
> inore
> NAN O"
> Vear
> TUIIOeT
> Htness
> Returns
> Drawdown
> Narqin
> Count
> Short Cownt
> 2015
> 7
> 13141
> 23
> 701
> 17101
> 140:
> 1
> 1
> 7017
> 0,31
> 13,133
> 305
> 333
> 20:
> 1275
> 1253
> 2013
> 0,01
> 13,51
> 0,335
> 27393
> 140:
> 1251
> 1255
> 2019
> 2,37
> 13,3703
> 175
> ,254
> 23393
> 1,370:
> 1241
> 1233
> 7020
> 115
> 1-,351
> 123
> 5711
> 3-39
> 22,230:
> 1215
> 12914
> 221
> 3
> 1-,3703
> 432
> 541
> 0.9703
> 25,550:
> 1155
> 1212
> 医 Correlation
> Self Correlation
> HiEhes: Correlation
> L+ RIn:
> IS Testing Status
> Qone this Alphaina neW tab
> Example
> SimMlate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> siema
> siBma
> 9ooo
> 18
> Sharpe
> Long



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> CODE
> RESULTS
> LEARN
> D4TA
> Settings
> USA/DITTOP3000
> N Chart
> PI_
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OO0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> SOOK
> Sector
> 008
> PASTEURIZATION
> UI
> HANDUNG
> NAN HANDLING
> OOO
> Verify
> Off
> SOOK
> Save as Default
> Apply
> OOO
> SOO
> Jul'16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> J7'19
> Jul 19
> Jan '20
> Jul '20
> Jan'21
> Qone this Alphaina neW tab
> Example
> SimMlate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> Equity



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Turhover
> 22N5
> 203
> 183
> 16
> Jul"16
> Jn 17
> Jul17
> 30'13
> Jul '13
> 30'13
> Jul '19
> Jan '20
> Jul'20
> Jan'21


结果显示 alpha 具有良好的换手率（约 10%）和较低的回撤。 我正在考虑如何提高锐度。

感谢中国大脑社区与用户分享了很多有用的知识。 希望今年Brain社区越来越壮大，老师和同学们能够更多地互相帮助。

---

## 讨论与评论 (2)

### 评论 #1 (作者: YW93864, 时间: 2 years ago)

您好，我猜是该步表达式使覆盖率下降了，因为这将returns为负的股票剔除了。

```
log（returns）
```

该步可能是在表达对数收益率，可能下方的代码会更好

```
log(close/ts_delay(close,1))
```

---

### 评论 #2 (作者: TN48752, 时间: 2 years ago)

谢谢您的评论。 我将采纳您的建议来优化 alpha。

---

