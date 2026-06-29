# 基于mcp提出的建议改进Super Alpha指标

- **链接**: https://support.worldquantbrain.com[Commented] 基于mcp提出的建议改进Super Alpha指标_36671358997143.md
- **作者**: KY99488
- **发布时间/热度**: 6个月前, 得票: 11

## 帖子正文

通过大佬分享，最近也是有了一些指标能合格的Super Alpha。
今天浏览SA因子时，发现数据质量表现较为一般
 
> [!NOTE] [图片 OCR 识别内容]
> Period
> TRAIN
> TEST
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 5.10
> 13.199
> 4.95
> 12.439
> 1.109
> 18.849600
> Period
> TRAIN
> TEST
> IS
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.27
> 10.339
> 2.45
> 7.019
> 1.659
> 13.569600
 
发给mcp，让其给点建议
 
> [!NOTE] [图片 OCR 识别内容]
> 现在我的选择表达式是: notfin (datacategories, "fundamental"))
> (1-
> self_correlation)
> 我的combo表达式是combo_alalpha, nlength=500, mode= "a1go1")既然
> 黑色的曲线都己经比橙色的更优。能不能调整一下比例什么的。提高橙色曲
 据mcp所给建议：调整组合权重、优化选择表达式、增加正则化项、使用不同组合方法
那最开始还是选择最直接的调整combo表达式中的参数（nlength = 500，mode = “algo1”）

暂时不太懂，就使用最笨的单一变量轮次比较
修改了nlength = 400，mode=algo1
 
> [!NOTE] [图片 OCR 识别内容]
> 组合策略优化:
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 5.10
> 13.199
> 4.95
> 12.439
> 1.109
> 18.849600
> 在组合策略中加^正则化项;
> 如11或12正则化
> Combo Expression
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> CONbO
> (alpha 5.16
> 13.099
> 5.05
> 12.539
> 1.319
> 19.149600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> 3.27
> 10.339
> 2.45
> 7.019
> 1.659
> 13.569600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.43
> 10.299
> 2.60
> 7.19%
> 1.45%
> 13.979600
  （段截图指标是修改后的表现）
可以看到，修改了nlength后，会有较小的提升，那接下来继续降低nlength

nlength = 300，mode=“algo1”
 
> [!NOTE] [图片 OCR 识别内容]
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 5.02
> 13.159
> 4.89
> 12.469
> 0.99%
> 18.949600
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 3.32
> 10.379
> 2.48
> 6.979
> 1.399
> 13.439600
 可以看到，nlength=300，表现反而降低，继续降低也是徒劳无功。

暂时将nlength=400敲定为最佳表现（肯定是不严谨的，因为nlength不是点，而是连续的，大步长选择nlength的值，会错过最优解）

nlength =400， mode = “algo2”
 
> [!NOTE] [图片 OCR 识别内容]
> Combo Expression
> Combo
> Blpha, nlength=4oo,
> mode="a1802
> Immary
> Period
> TRAIN
> TEST
> I5
> lata
> Sharpe
> Turnover
> FTnESS
> Rezurns
> Drawdown
> Margin
> 5.98
> 11.679
> 7.08
> 17.5096
> 1.699
> 30.009600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.79
> 9.369
> 3.15
> 8.6296
> 2.629
> 18.419600
 可以看到，相对于之前的表现，这次的指标有了较为明显的提升，尤其是Fitness和Margin

接下来乘胜追击，nlength =400， mode = “algo3”
 
> [!NOTE] [图片 OCR 识别内容]
> LI」 |
> '5'
> Combo Expression
> 5S
> COmbo
> a(alpha
> nlength-40o
> mode
> 'a1803
> TEST
> 15
> Data
> Sharpe
> TurnoVe
> Fitness
> Returns
> DrawcOwn
> Margin
> 5.84
> 11.249
> 7.43
> 20.259
> 1.749
> 36.029600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> IS
> 3.70
> 9.279
> 3.25
> 9.639
> 2.709
> 20.789600
> ggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 3.70
> 9.279
> 3.25
> 9.639
> 2.709
> 20.789600
> egate
 修改成algo3后，Margin得以进一步增长。表现最优（当然，这些指标针对于我现在的数据能带来的提升）

nlength = 600 mode = “algo3”
 
> [!NOTE] [图片 OCR 识别内容]
> Period
> TRAIN
> TEST
> 1S
> 2022
> 202
> Sharpe
> TUIOVOT
> Ftnoss
> Returns
> Drawcown
> MarBin
> 5.93
> 11.409
> 7.56
> 20.349
> 1.679
> 35.679600
> a
> IS Summary
> Period
> TRAIN
> TEST
> 15
> 05
> Aggregate Data
> Sharpe
> Turnover
> Finess
> RetUrns
> Drawdown
> Marein
> 3.60
> 9.169
> 3.11
> 9.359
> 2.719
> 20.429600
> 2ry
 nlength设600，性能有仍然在提升，不过提升幅度过小。
综合来看应当是400，algo3表现最佳。

但是仍有其余的一些因素值得考虑，查看400，algo3的prod correlation为0.70+，而600，algo3的PC为0.65，且数据不弱于前者，损失一些资源换取PC的差距也是值得考虑的关键点。
（后面我尝试了一些不同的组合方法：加权平均，指数加权等等以及添加其他参数，但显示mcp提供操作符不正确，我这方面的知识仍旧欠缺，还没有学习到位就不展示出来了）

接下来可以来针对选择表达式来改进

初始表达式：not(in(datacategories, "fundamental")) * (1-self_correlation)
这个表达式的因子为：筛选出所有非基本面类别的因子（datacategories是因子的数据类别，"fundamental"表示基本面数据），并通过（1-self_correlation)来对相关性高的因子做出惩罚。
在我的理解看来，相关性高的因子是得以加入惩罚机制，但是是否会丢失一些较好的数据？

修改后的表达式：not(in(datacategories, "fundamental")) * (1-self_correlation*0.8)
通过对SC的衰减处理，可以尽可能保持因子的多样性的同时，保留降低高SC权重的初衷，避免过度筛选。通过衰减来平滑自相关性的影响，实现稳健筛选。
好的，那么到这里，理论部分没有什么太大的问题，但是很遗憾的是，实践部分是大跌眼镜的。如下：

未修改


> [!NOTE] [图片 OCR 识别内容]
> 01/04/2023
> Equal Weight Pnl:
> 10.79M
> Test Combo Pnl: 7,385.42K
 修改后：
 
> [!NOTE] [图片 OCR 识别内容]
> 01/13/2023
> Equal Weight Pnl:
> 11.24N
> Test Combo Pnl:
> 7,081.83K
 （因子本身也不够好，combo<weight）虽然指标并无太大变化，但是PnL的数值以及稳定性不够好。最重要的一点是PC提高了很多。
那么尝试比较一下衰减影响与加重惩罚的PC对比。

1-self_correlation*0.8 PnL曲线
 
> [!NOTE] [图片 OCR 识别内容]
> 01/09/2023
> Equal Weight Pnl:
> 11.18M
> Test Combo Pnl: 7,040.4GK
 可以看到，几乎与*0.8无异。因此保持一个稳定适中的“惩罚”是值得肯定的，大多情况下过度或衰减应当都不可取。

这个SA的PnL曲线并不理想，combo<weight，但是如何改良却也是值得学习的点。改进方法进一步优化，会得以产生良好的效果。
希望大家多多出三五SA，一起加油

---

## 讨论与评论 (7)

### 评论 #1 (作者: 顾问 YH25030 (Rank 31), 时间: 6个月前)

最近回到了手搓SA，感觉mcp有时候的确可以给出好建议，希望这不是AI幻觉。😄

---

### 评论 #2 (作者: XM75236, 时间: 6个月前)

良好的探索,逻辑性非常好,值得学习

=================================================================================

Achievements are reached by hard work, but ruined by idleness; Actions are accomplished through thorough consideration, but destroyed by casual decision.​​  =================================================================================

---

### 评论 #3 (作者: AH18340, 时间: 6个月前)

看到ai优化ra的，终于看到ai优化sa的了，给大佬点赞

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #4 (作者: CC21336, 时间: 6个月前)

用MCP去优化探索SA，的确是个好的思路。不过作者这篇文章感觉更多的是自己基于对SA的理解自己探索优化出来的。似乎MCP的作用没那么显著。

---

### 评论 #5 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 6个月前)

虽然实践起来一波三折，但是我还真没尝试过使用ai+mcp去优化Super alpha，看了你的帖子后感觉却有可取之处。可惜使用的还得太浅了，要是进一步探索就能看到真章了。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #6 (作者: SY36032, 时间: 5个月前)

非常受用，感谢分享

---

### 评论 #7 (作者: HY20507, 时间: 4个月前)

感谢分享，发现自己对SA的知识有许多欠缺，仍待学习

---

