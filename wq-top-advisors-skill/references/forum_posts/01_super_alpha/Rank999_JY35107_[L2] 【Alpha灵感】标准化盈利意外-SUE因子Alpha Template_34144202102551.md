# 【Alpha灵感】标准化盈利意外-SUE因子Alpha Template

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】标准化盈利意外-SUE因子Alpha Template_34144202102551.md
- **作者**: JY35107
- **发布时间/热度**: 10 months ago, 得票: 21

## 帖子正文

**标题：ESG Preference, Institutional Trading, and Stock Return Patterns**

**作者：Jie (Jay) Cao**

**概述：** 该篇论文探讨了社会责任型机构（SR institutions）因过度关注ESG表现，对传统错误定价信号（如SUE/SYY）反应不足。这导致高SR_IO股票的错误定价信号（SUE/SYY）产生显著超额收益，尤其当存在融资约束（如经纪商杠杆冲击）时。策略有效性在2004年后ESG投资兴起期显著，且主要存在于大盘股。故基于此概念，本文将SUE因子进行复现测试，最终取得有效的信号。

**Alpha Idea:**

关于SUE因子文章中提及一种计算方法，如下图：


> [!NOTE] [图片 OCR 识别内容]
> NC
> regard
> as mispricine stenals。
> LO Iuslrle thls
> We slart by examining the InK belween
> stock' 
> holdines by SRinstitutions and its tendency to underreact to eamings announcements. This
> analysis is similar t0 Hirshleifer; Lim, and Teoh (2009), who also examine how constraints
> atlenlion allecl slock
> rClums around
> earnings announcements。 Specifically;
> We follow Fosler。 
> Olsen。 and Shevlin (1984)
> and Bemard
> and Thomas (1989) and examine responses
> t0 Tmms'
> standardized unexpected eamings (SUE)。 computed
> as the diflerence
> belween
> their Currenl
> quarter's eamings
> and
> the
> earnings
> [OUI
> quarters ag0,
> scaled by
> the standard devialion
> unexpected earnings over the
> eight quarters。
> We also [ollow
> Stambaugh。 Yu。
> and
> Yuan (2015). and
> Consider
> monthly updated
> composite quantitative signal, constructed by combining each stock 's rankings On
> 11 anomaly
> variables。
> The
> anomalies
> Net Stock Issues, Composite Equih Issues。
> Jccruals。 Ner
> Operating Assets,
> Issel
> Growth。 Ivestment-to-Assels。 Distress。
> O-score。
> Lomenttm。
> Gross
> lasl
> UTC


以此按照该论述使用Fast Expression进行复现：

Setting：USA TOP3000，delay1 ， Subindustry

表达式：

```
current_eps = anl4_epsr_value;prev_eps = ts_delay(anl4_epsr_value, 120);eps_std = ts_std_dev(anl4_epsr_value, 220); (current_eps - prev_eps) / eps_std//表达式解释：current_eps = 最新季度盈利     # 当前成绩prev_eps   = 一年前同季度盈利   # 上次成绩eps_std    = 过去8季度盈利波动  # 历史波动标尺SUE = (current_eps - prev_eps) / eps_std1）SUE > 0 → 盈利超预期（利好，可能买入）2）SUE < 0 → 盈利不及预期（利空，可能卖出）
```

IS表现如图：


> [!NOTE] [图片 OCR 识别内容]
> TNTO
> IA
> T+
> c_c
> _JJOTa_
> 
> +Losdr Is]RaJ
> UTTP
> ECr
> Summan
> Ocr?Nt
> UMroxo0
> 087
> 5,5694
> 030
> ?71N
> 7,77
> 0744
> O


样本内数据：（sharpe: 0.82; margin:9.74）

**从pnl曲线看来，可见有一定的正向信号但是明显曲线波动异常，考虑到金融市场可能存在财报纠正、会计调整等干扰，故打算过滤掉异常值的股票以优化。**

**优化方法：**

这里用ts_std_dev操作符计算SUE指标的“21日滚动标准差“，判断波动率是否小于2.0阈值，同时因为过高的SUE可能是伴随财务数据质量问题、极端事件影响等，故用2.0阈值加以约束来提高策略鲁棒性。

**优化后的表达式为：**

```
current_eps = anl4_epsr_value;prev_eps = ts_delay(anl4_epsr_value, 120);eps_std = ts_std_dev(anl4_epsr_value, 220);SUE = (current_eps - prev_eps) / eps_std;ts_std_dev(SUE, 21) < 2.0
```

**
> [!NOTE] [图片 OCR 识别内容]
> Current
> eps
> anl4_epsr_value;
> Excellent
> Sinele Data Set Alpha
> preV_eps
> ts_delay (anl4
> epsr_value,
> 120)
> eps_std
> ts_std_dev (anl4
> epsr_Value, 220)
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> JSOCMIC
> Marsin
> SUE
> (current_eps
> preV
> eps )
> eps_std;
> 1.94
> 4.659
> 2.07
> 14.179
> 8.649
> 60.9
> 9600
> tS_std_
> dev(SUE,
> 21)
> 2.0;
> Year
> Sharpe
> Turover
> Fitess
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 1.0
> 4.60%
> 0.55
> 3.669
> 2.435
> 15.93533
> 1951
> 565
> Instrument Type
> Region
> Unlerse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> 2019
> 1.56
> 1.5936
> 1.15
> SGI
> 5.195
> 30.359330
> 1911
> 331
> Eouit
> US~
> T0P3000
> Fast Expression
> 001
> Subindustry
> Verfy
> 2020
> 0.37
> 5.4936
> 0.15
> 2.3336
> 7.489
> 8.48520
> 1922
> 392
> 2021
> 2.48
> 3.9036
> 3.57
> 27.4430
> 7.695
> 1-0.5-533
> 390
> 4
> 2022
> 3.42
> 1.3836
> 5.13
> 28.6330
> 4.0233
> 117.1933
> 2015
> 357
> Clone Alpha
> 2023
> 3.47
> 2.1836
> 440
> 20.1330
> 0,5535
> 18-.59533
> 1792
> 240
> N Chart
> Prl
> Correlation
> Self Correlation
> Maximum
> NinimUM
> Last RUn:
> 40OOK
> Performance Comparison
> ZOOOK
> Last RUn:
> Properties
> Last saved Wed; 08/13/2025,12-55 PN
> 13
> Jan"19
> JuI'19
> Jan '20
> Jul'20
> Jan '21
> Jan '22
> JU1 "22
> Jan'23
> 医
> JUI
> JUI
**


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 7 PASS
> Sharpe OT 1.9415 above CUtOff OT 1.25
> Fitness OT2.07is 3DOVe CUTOTfOT
> Turnoverof 4.6596 is above Cutof of 1%6
> Turnoverof
> 6596 Is below CUtOff OT 7096.
> Weight is 'Nell distributed owerinstruments
> SUb-universe Sharpe cf 0.8715 above Cutoff cf 0.84.
> Comoetition
> Challenge matches
> PENDING
> Performance Comparison
> Last RUn:
> Properties
> Last saved Wed;03/13/2025,12.55 PNI
> Name
> Category
> udd Npha t
> LSl
> Openalpha detalls In newtab
> Check Submission
> Submit Alpha
 表现得到了明显的提升，并且可以符合提交标准，从结果可以看到SUE信号因子在USA市场有效，而且在排除异常数据以后稳健性和趋势表现都不错。

**总结：** 通过本次复现测试，验证论文提及的SUE指标因子在USA D1市场具有明显的实际意义，或许可考虑在不同的市场进行测试验证。

同时，有一个猜想：SUE因子是否可以作为一个基础因子，同其他因子进行结合变化呢？这里，还需要后续做更多的测试研究。

**参考论文：** ESG Preference, Institutional Trading, and Stock Return Patterns  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3353623](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3353623)

---

## 讨论与评论 (7)

### 评论 #1 (作者: KJ42842, 时间: 10 months ago)

4个季度和8个季度分别是252和504个交易日。

---

### 评论 #2 (作者: MY21251, 时间: 10 months ago)

太牛逼了，是怎么想到最后一步的，用ts_std_dev操作符计算SUE指标的“21日滚动标准差“，判断波动率是否小于2.0阈值，这个简直是神来之笔，经常遇到这种有信号的，但是又无处下手的因子。

---

### 评论 #3 (作者: JB53978, 时间: 10 months ago)

看起来确实不错，可惜是user的alpha，到顾问后时间拉长就可以看出这个alpha完整的表现了

---

### 评论 #4 (作者: JY35107, 时间: 9 months ago)

JB53978

你好，因为刚成为顾问，所以才看到你的评论。

SUE因子是一个相对具有经济学含义的模型，成为顾问后我 **按照我在user阶段制作的模板** ，遍历替换新权限的eps字段后，制作出来许多可以提交的alpha，故请自重，希望您也可以多加尝试，谢谢！

---

### 评论 #5 (作者: LL40493, 时间: 1 month ago)

表达式的结果。是一或者说是零。有没有一种别的方法呢？更加准确的。

```
SUE = (current_eps - prev_eps) / eps_std           # 原始 SUE 值（连续值）
filter = ts_std_dev(SUE, 21) < 2.0                  # 二元过滤器（0 或 1）
result = SUE * filter                               # 不稳定股票的 SUE 被置为 0
```

---

### 评论 #6 (作者: FF65210, 时间: 1 month ago)

感谢佬的分享，这下又有新模板了，小白每天都进步一点，一起共勉。

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

### 评论 #7 (作者: AS53518, 时间: 21 days ago)

SUE   解释

x： 任意金融指标，例如eps

ts_delta(x,window)/ts_std_dev(x,window);

这里的window都是长时间例如250,500, 所以这里的ts_std_dev(x,window)可以理解为增速或速度，而不再是波动。

比值越大，有可能分子越大，也有可能分母越小。假设分母一样，也就是增速一样，差值越大，则做多。例如，腾讯和某个小市值公司，有一样的增速，你肯定会投资腾讯，类似于大象和老鼠一样灵活。同样假设分子不变，分母越小则做多，例如腾讯和网易今年涨的幅度一样，那说明网易的增速比腾讯大特别多，才能实现涨幅一样，因此增速越慢，越做多，这里似乎有点反直觉，相当于网易从1000亿涨到2000亿，腾讯从4万亿涨到4万1千亿。

---

