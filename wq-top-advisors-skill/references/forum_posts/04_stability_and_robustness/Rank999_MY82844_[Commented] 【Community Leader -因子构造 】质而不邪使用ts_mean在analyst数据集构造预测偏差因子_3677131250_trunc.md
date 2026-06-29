# 【Community Leader -因子构造 💎】质而不邪，使用ts_mean在analyst数据集构造预测偏差因子

- **链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】质而不邪使用ts_mean在analyst数据集构造预测偏差因子_36771312509463.md
- **作者**: MY82844
- **发布时间/热度**: 6个月前, 得票: 11

## 帖子正文

**适用数据：** analyst10等

**数据分析：**

**
> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Performance-Weighted Analyst Estimates
> EUR
> T0P2570
> Fields
> Description
> Search
> ThEME
> Cowerage;
> Alphas
> UsErs
> sUrprisg
> 100
> Claar
> Ryranid
> Hl
> Dsornon
> Typ
> 172
> Coverege
> Users
> Alhas
> LC
> 3nl10_5a/f02
> SUros_V
> Prsdictsd SUFis
> EinT0Trlas Tr
> 12(3
> 711131
> ar
> -
> TCESICITCENEIS
> anll0_netyl_pred_Suros_vl
> TT=TICTI SUCs 三I -
> WrnECCONE for Fyl [ TU 2
> Ulati
> 1015
> [mars
> TTRLU
> TRSTSU
> 3n110
> TETJpTE
> SJros_V
> Prsdictsd SUFis
> I 
> TTIC TeTI=
> for FY2 C Use
> ar
> 1
> T=TI
> 7005TSI
> anl10coxtyl
> _SUIPS_V2_235
> Prsdictsd SUPis
> 三C -
> Capita
> exendUrestor TT
> a
> 17
> 13171131431
> LMaREts
> TC =三T
> TOAEESIL
> anll0_oorfyl_pred_suros_VO
> T=TICTI SUCs I -
> TTC TOFSIT TTTI TTT
> Ilati
> S
> LOIUIas0
> (smar_Sts
> CONEENSILIOREENSIL
> 3n/10
> COxTJZ_OrEJ_SUIPS_MI_280
> Prsdictsd SUPis
> I 
> exoendtures for FV2
> a
> 17
> TlMlasn
> OAESSIIONEESIL
> TjOE
> Fre
> DrsJ
> CEJi
**

发现EUR的D0和D1该数据集下有大量关于各种基本面指标的predicted surprise的数据，使用量不是很大，于是想尝试下仿照earnings surprise，构造一些低相关性的因子。

**Alpha构建：** 先通过AI了解一下大概的信息，确定构造的方向，大致方向和earnings surprise是一样的，predicted surprise和未来收率正相关。


> [!NOTE] [图片 OCR 识别内容]
> 这个指标叫 "预测意外" (Predicted Surprise) , 也叫 "预测差异率"  或 "预测偏差率"=
> 公式:
> Predicted Surprise
> (Smart Estimates
> ConsensUs]
> ConsensUs
> 其中
> Smart Estimates 是 Refinitiv
> StarMine 用算法加权最近。最准的分析师预测后得到的"更聪明"的一
> 致预期;
> Consensus 就是传统意义上所有覆盖分析师的简单平均预期。
> 所以 Predicted Surprise Version 0 for Sales Q1 读成白话就是:
> 用 Smart Estimates 算出的Q1营收;比市场一致预期高/低多少个百分点。
> 正值
> Smart 预测高于市场,暗示"正向惊喜"可能;
> 负值
> Smart 预测低于市场;暗示"负向惊幸"风险。
> 它本身不是己经发生的"惊喜" (Surprise) , 而是一个领先指标。用来预测公司公布业绩时实际数字相对
> 于市场一致预期可能出现的偏差。


尝试了常用的一些算子的处理，发现效果不是非常好，没有通过提交检验。最后，想起来使用最朴素的 **ts_mean() + sign()** 的方式处理下看看，没想到，有些字段的绿按钮亮了起来，至少可以作为一个ppa+atom。


> [!NOTE] [图片 OCR 识别内容]
> ts_mean(sign(anlIe_dpsfyl_pred_SUFPS_YI_528),
> 252)
> Simulation Settinas
> Instrment Type
> Reolon
> UaNOUaOe
> Delay
> Tnwncatlon
> Neutralzatlo
>  Pasteurtatlon
> NaN Handung
> Umt Handllng
> Vax Trade
> Equity
> EJR
> TOP_SOO
> Fast Erssslon
> Tas -aC
> TerI
> Uwyrse
> Dc



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Pariot
> . Single Data Set Nlphs
> ABaregate
> Uata
> SNdlr
> 叭AMO
> MTyI
> 1.68
> 2.57%
> 0.83
> 3.08%
> 2.47%
> 23.959000


**Alpha改进：** 后面可以使用group算子，或者signed_power算子进一步提升一下表现，让fitness达到1的水平。

**其它：**

1. EUR的D0和D1都有类似的数据字段，只是命名方式略有不同，测试了下，表现比较相似，相关性比较高

2. 因为数据离散的缘故，不同region可能对数据需要进行不同的backfill处理，以保证因子有效

3. 后续发现在其它一些数据集，比如options，ts_mean也可以得到一些可以过线的因子

[【Community Leader -因子构造 💎】AI严选条件动量模版，点塔Sentiment – WorldQuant BRAIN]([Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md)

[【Alpha灵感】基于short interest数据的跨交易所组合案例 – WorldQuant BRAIN]([L2] 【Alpha灵感】基于short interest数据的跨交易所组合案例_35577573602455.md)

---

## 讨论与评论 (9)

### 评论 #1 (作者: AH18340, 时间: 6个月前)

d0的数据这个指标虽然能交但是指标感觉差了点

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #2 (作者: LL61351, 时间: 6个月前)

有时很难想象，ts_sum(sign(field),day)会比直接ts_sum(field,day)信号强，可实际的回测就是这样？可能通过sign分配权重更有效

---

### 评论 #3 (作者: MY82844, 时间: 6个月前)

[AH18340](/hc/en-us/profiles/28845157706135-AH18340)  确实，和D1数据的表现没有拉开差距，离D0的RA标准有点远，抛砖引玉

---

### 评论 #4 (作者: MY82844, 时间: 6个月前)

[LL61351](/hc/en-us/profiles/32148227400983-LL61351)  在这角度的算法下强一些，估计是极度降噪了...

---

### 评论 #5 (作者: XZ52921, 时间: 6个月前)

对于差异率来说，差异的数值可能没有差异的方向有预测性，所以加sign以后反而有信号，是个很好的思路，感谢分享。

---

### 评论 #6 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

sign(x)的结果是-1,0,1, ts_mean(sigx(x),252) 相当于计算一年内这个数值的正负比例，这样居然也能出信号

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #7 (作者: MY82844, 时间: 6个月前)

[顾问 SJ65808 (Rank 20)](/hc/en-us/profiles/25875982235543-顾问 SJ65808 (Rank 20))  这个出来一般performance不是非常sharp

---

### 评论 #8 (作者: AK76468, 时间: 5个月前)

====================================================================================

这个还是挺有意思的，忽略强度只看方向的表现竟然会更好，“谁超预期的次数越多，我越做多”，一定程度上也消除了极端值的风险，已经加入优化小妙招+

==================================================================================

---

### 评论 #9 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 5个月前)

模板捕捉——预测意外：

<ts_ops/>(sign(<predict_surprise/>), <d/>)

不知不觉看过大佬好几种模板思路了，已关注学习。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

