# 浅探对robust test结果的观测方法经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 浅探对robust test结果的观测方法经验分享_31920180343703.md
- **作者**: DZ31817
- **发布时间/热度**: 1年前, 得票: 63

## 帖子正文

所谓robust test（稳健性测试），是指为因子设置不同的工作环境，并观测其在不同环境下的表现，如果表现没有出现大幅波动，说明这个因子是比较稳健的。这里设置的不同环境在某种意义上来说也算是一种OS，因此表现稳健的因子更有可能获得更稳定的OS表现。

我们在平台做robust test，主要通过遍历修改因子回测的各种参数，观测因子在不同设置组下的表现来实现。遍历的参数方面，有离散型的region、universe、neut和3个开关参数，以及decay、trun这两个连续型参数。

在遍历跑完后，如何对结果进行观测，这里分享一下我的一些方法，希望可以抛砖引玉。

1.首先观测因子主要指标总体的表现分布，这里通过画分布直方图、KDE图、箱型图并结合定量指标来观测。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 25
> 20
> 詈
> 詈
> Sharpe
> Fitness
> Margin
> Turnover
> 25
> 詈
> `
> 0.0000
> 0.0025
> 0.0050
> 0.0075
> 0.0100
> 0.0125
> 0.0150
> 0.0175
> 0.0200
> 0.00
> 0.25
> 0.50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Margin
> Turnover
  
> [!NOTE] [图片 OCR 识别内容]
> KDE
> Sharpe KDE
> Fitness KDE
> 1.0
> 1.25
> 1.00
> 0.6
> 鲁
> 鲁
> 0.75
> 0.50
> 0.25
> 0.00
> Value
> Value
> Margin KDE
> Turnover KDE
> BO0
> 500
> 400
> 鲁
> 300
> 
> 200
> 100
> 0.0000
> 0.0025
> 0.0050
> 0.0075
> 0.0100
> 0.0125
> 0.0150
> 0.0175
> 0.0200
> 0.00
> 0.25
> 0.50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Valle
> ValUe
  
> [!NOTE] [图片 OCR 识别内容]
> Boxplot
> Sharpe Boxplot
> Fitness Boxplot
> 詈
> 詈
> Margin Boxplot
> Turnover Boxplot
> 0200
> 2.00
> 0.0175
> 1.75
> 0.0150
> 1.50
> 0.0125
> 1.25
> 詈00100
> 詈
> 1.00
> 0075
> 0.75
> 0050
> 0.50
> 0025
> 0.25
> 0000
> 0.00


肉眼看表现不是很稳定，但也没有出现特别差的极端值。

2.接下来进行更细粒度的观测，画出因子指标在不同设置下的具体表现。这种观测除了进行robust test的目的外，还可以帮助你思考现在这个模板、数据集更适合什么设置。

不同universe下的表现：

看出这个因子在更大的universe下表现更好。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Universe
> Fitness by Universe
> 1.4
> 1.0
> 1.2
> 1.0
> 0.8
> Universe
> Universe
> Margin by Universe
> Turnover by Universe
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 0.003
> 0.150
> 0.125
> 0.002
> 0.100
> 0.075
> 0.001
> 0.050
> 0000
> 0.025
> Universe
> Universe
> MINVOLTM
> TOP1200
> TOP4O0
> TOP8O0
> _MINVOLTM
> TOP1200
> TOP4O0
> TOP8OO
> ILLIQUID_
> ILLIQUID
> TOP1200
> TOP1200
> TOP4O0
> TOP8O0
> _MINVOLTM
> TOP4OO
> TOPgOO
> MINVOLTM
> ILLIQUID_
> ILLIQUID_


说到不同universe该如何选择，之前也在研究小组中讨论过，这里把gpt的总结也顺带放这个帖子里。仅供参考，不一定完全适用。


> [!NOTE] [图片 OCR 识别内容]
> Universe 分类与推荐适配关系 (按 Datafield 类型分)
> Datafield 类型
> 推荐 universe 示例
> 说明
> Analyst
> TOP5OO
> TOPZOODU
> 尤其是
> TOPSP5OO
> 覆盖面广的 sell-side 研究。适用于大中
> TOPIOGO
> 盘股。数据密度高
> Earrngs
> TOP1OO0
> TOPSPS吣0
> EPS surprise。 guidance 变化等容易在
> 大票中反应明确
> Fundamental
> TOPIOGO
> 以下。如
> TOP16O0
> TOP3OOO
> 甚至
> 小票和低流动性股信息滞后。误定价多
> LLIQUID_MINVOLIN
> 基本面因子容易出 alpha
> Imbaance
> TOP4OO 以内。如
> TOP5O
> TOPIOO
> TOPSP5B0
> tklevel
> 数据需要高流动性。高频交易
> 特征在大盘蓝筹中更稳定
> Insiders
> TOPBOO
> TOP3OOO
> 小中盘股 insider 交易更有预测力。尤其
> 在信息不对称强的股票上
> Institutions
> TOP5OO
> TOPIGg0
> 机构重仓通常集中在中大盘。低流动性股
> 票机构参与少
> Macro
> 全市场通用。如
> T0P30O0
> TOPZOOgU
> 与个股无强关联性。可作为横截面
> beta。 风格回归项
> Model
> 跟随原始模型设计池子
> 模型因子取决于训练数据设计。不做统
> 分类
> News
> TOPIOGO
> 以内。如
> TOP2O0
> TOPSP5OO
> 上新闻的股票以热点大票为主。小票新闻
> 稀疏无效
> Option
> TOPSO
> TOP5OO
> 尤其 TOPSP5OO
> 有期权交易的股票以大盘蓝筹为主。其余
> 票期权数据缺失
> Other
> 具体字段具体判断
> 例如
> othg4
> Oth95
> 常见于舆情[事件
> 类。适用于中大票
> Price Volume
> TOP3OOO 全部。需做分层测试
> 价格。波动宰。成交量因子广谱适用。尤
> 其 momentum 在大票更稳定
> Risk
> T0P30O0  通用
> Volatility
> beta。
> size 等因子构建风格模
> 型基础组件
> Sentiment
> TOPIOO
> TOPIGg0
> 舆情活跃股通常足热点股票。小票讨论稀
> 疏。舆情滞后
> Short Interest
> TOP4OO
> TOPI6OO
> 做空机制活跃的股票更可能出现在中大
> 票。低流动性票难以借券
> Social Media
> TOPIOO
> TOPIGg0
> 社交媒体热度集中于热门票。小票信息噪
> 声大或缺失


继续观测robust test结果，不同中性化下的表现：

看出这个因子在country中性化下表现更好。这个示例因子我用的是EUR的因子，这个结论也与官方的推荐设置一致，逻辑闭环了。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Neut
> Fitness by Neut
> 1.4
> 1.0
> 1.2
> 1.0
> 0.8
> p9
> G
> Neut
> Neut
> Margin by Neut
> Turnover by Neut
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 0.003
> 0.150
> 0.125
> 0.100
> 0.075
> 0.001
> 0.050
> 0.000
> 0.025
> Neut
> Neut
> 惫
> FAST
> COUNTRY
> CROWDING
> MARKET
> SECTOR
> FAST
> INDUSTRY
> SLOW
> SUBINDUSTRY
> COUNTRY
> CROWDING
> MARKET
> SECTOR
> FAST
> INDUSTRY
> SLOW
> SUBINDUSTRY
> STATISTICAL
> STATISTICAL
> AND_
> OW_
> SLOW
> COUNTRY
> MARKET
> |
> FAST
> s
> SUBINDUSTRY
> COUNTRY
> SECTOR
> INDUSTRY
> FAST
> SLOW
> SUBINDUSTRY
> CROWDING
> STATISTICAL
> SECTOR
> WNDUSTRY
> CROWDING
> MARKET
> FAST
> STATISTICAL
> AND
> AND_
> SLOW
> SLOW


不同universe+中性化组合下的表现：

帮助找到当前最适合的搭配。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Group
> Fitness by Group
> 1.4
> 1.0
> 1.2
> 0.8
> 1.0
> 0.8
> Neut
> Neut
> Margin by Group
> Turnover by Group
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 003
> 0.150
> 0.125
> UUU2
> 0.100
> 0.075
> 0.00
> 0.050
> DOO
> 0.025
> Neut
> Neut


不同decay下的表现：

这里decay离散取了几个值，看出对于这个因子，decay越高似乎表现更好。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Decay
> Fitness by Decay
> 1.4
> 1.0
> 1.2
> 0.8
> 1.0
> 0.4
> 120
> 240
> 120
> 240
> Decay
> Decay
> Margin by Decay
> Turnover by Decay
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 0.003
> 0.150
> 0.125
> 0.002
> 0.100
> 0.075
> 0.001
> 0.050
> DOO
> 0.025
> 120
> 240
> 22
> 120
> 240
> Decay
> Decay
> DTOUH


由于decay是连续型参数，我干脆固定了其它参数后把decay从0-240都取值跑了一下，结果如下：

看出对于这个因子，decay对性能增强的峰值在70附近。同时，也可以观测到turnover随decay的增大而被削弱，与理论吻合。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> VS Decay
> 1.60
> 1.55
> 1.50
> 詈
> 1.45
> 1.40
> Fitness Vs Decay
> 1.30
> 1.25
> 1.20
> 岛
> 1.15
> 1.10
> 1.05
> Margin Vs Decay
> 0.0050
> 0.0045
> 0.0040
> 
> 0.0035
> 0.0030
> 0.0025
> 0020
> Turnover Vs Decay
> 0.06
> 
> 0.05
> 0.04
> 100
> 150
> 200
> 250
> Decay


既然说到了turnover，虽然它不是一个参数，但大家都对它比较敏感，对高turnover的因子避之不及，因此我也顺便观测了一下turnover对性能的影响：

看出turnover在15以上后性能确实迅速退化。此外，这里margin随turnover的变化图像也验证了return ~ turnover*margin的理论，理论与实践再次闭环。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe Vs Turnover
> 1.25
> 1.00
> 詈
> 0.75
> NIRI
> 0.50
> 0.25
> Fitness Vs Turnover
> 1.0
> 0.8
> 0.6
> 
> 0.4
> 0.2
> "WWlkwt
> 0.0
> Margin Vs Turnover
> 0.005
> 0.004
> 0.003
> 
> 0.002
> 0.001
> 0.000
> TurnoVer VS Turnover
> 0.20
> 0.15
> 
> 0.10
> 0.05
> 0.025
> 0.050
> 0.075
> 0.100
> 0.125
> 0.150
> 0.175
> 0.200
> 0.22
> WM
> IMMAN


以上观测方法仅仅是抛砖引玉，对于robust test的结果还是要人工判断，没有一个能一概而论的判断标准，希望大家能够分享交流是否有更好的观测方法。另外，从这次观测之旅我们也体会到，这种详细的数据分析和深入研究的收获，往往能大大超出你原本的目的。

---

## 讨论与评论 (14)

### 评论 #1 (作者: YX50005, 时间: 1年前)

"看出这个因子在country中性化下表现更好。这个示例因子我用的是EUR的因子，这个结论也与官方的推荐设置一致，逻辑闭环了"

请问官方推荐设置在哪里看呢？

---

### 评论 #2 (作者: worldquant brain赛博游戏王, 时间: 1年前)

WQ科学家！！！很好的帖子，点赞。如果对于不同地区的因子都做一次测试，就可以找出最适合每个地区的中性化方式了。

---

### 评论 #3 (作者: DZ31817, 时间: 1年前)

[YX50005](/hc/en-us/profiles/29899344989847-YX50005)

请看这篇官方文档，对于有多个国家的region，官方推荐使用country中性化。 [https://platform.worldquantbrain.com/learn/documentation/advanced-topics/neut-cons](https://platform.worldquantbrain.com/learn/documentation/advanced-topics/neut-cons)

---

### 评论 #4 (作者: LL87164, 时间: 1年前)

如果能用更多样本的分析以下两点，则更有参考价值：

1. 不同region下turnover在多大时，性能明显退化

2. decay的峰值与因子的哪些特征有关联

---

### 评论 #5 (作者: SH97251, 时间: 1年前)

我要加入Kitty神教

---

### 评论 #6 (作者: BL59663, 时间: 1年前)

这就叫专业！膜拜大佬

---

### 评论 #7 (作者: XC66172, 时间: 1年前)

由于decay是连续型参数，我干脆固定了其它参数后把decay从0-240都取值跑了一下...

这个太厉害了，图中也很直观的表现了decay对性能增强的峰值70。我一般采用decay的值是20，60，120，240来跑一遍看哪个综合指标更高

gpt的总结也很实用。我现在一般都按照官方的推荐从dataset来推导相应的neutralization. 不过想EUR的小数据集总是跑不出好的，可以再结合一下这个试着换一下别的neut来跑。

---

### 评论 #8 (作者: 顾问 FD69320 (Rank 34), 时间: 11个月前)

感谢楼主，各种指标对应decay的变化趋势很受启发，会在本地尝试加入自己的框架。

===================================================================

===================================================================

===================================================================

---

### 评论 #9 (作者: BW14163, 时间: 11个月前)

模板多为大佬的发言，准备把帖子打印出来，作为日常指导性材料

---

### 评论 #10 (作者: LR93609, 时间: 9个月前)

感谢分享，大佬出手，完全不同，学到了，个人感受：

1. earning、short、snt、scl、insider、imbalance、Option、news、institution等小数据集，我总是找不到办法，原来问题出在流动性上面，确实前期所学是有欠缺的；

2. 后续将通过适配不同的universe，组建不同的因子；

3. 解释了coverage，有效抨击了各类妖魔鬼怪。流动性低的票，ts_backfill解决不了问题，那完全是谬论。

---------------------------------------------------------------------------------------

凡是发生，皆利于我；愿我所愿，尽是美好

---------------------------------------------------------------------------------------

---

### 评论 #11 (作者: 顾问 SJ65808 (Rank 20), 时间: 9个月前)

大佬牛逼，分析的有理有据，不亏是科学家~~

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #12 (作者: SZ20589, 时间: 8个月前)

感谢大佬分享，有几个问题，望解答下。

[DZ31817](/hc/en-us/profiles/25751669201943-DZ31817)  对于有多个国家的region，官方推荐使用country中性化。那是不是对于ASI, EUR，GLB官方都推荐Country吗？

[LR93609](/hc/en-us/profiles/30244554462231-LR93609)  earning、short、snt、scl、insider、imbalance、Option、news、institution等小数据集，我总是找不到办法，原来问题出在流动性上面，确实前期所学是有欠缺的 这究竟是什么意思？找到什么方法了，能否告知？

====================================================================================

一分耕耘，一分收获

====================================================================================

---

### 评论 #13 (作者: SQ98290, 时间: 7个月前)

=====================================感谢分享=======================================

楼主的这份分析报告做得非常的详细

其中关于universe 和 decay的ai推荐及测试更是让我耳目一新

一直以来我都只跑一个univer 和 一个decay，对这些设置不得其解，凑合用也就没有专门的去看

现在看完了楼主的帖子，感觉思路开阔了不少

现在我在跑回测的时候也有在尝试不同的decay和universe了

非常感谢楼主的分享

祝你继续gm，vf月月1.0

---

### 评论 #14 (作者: XW23690, 时间: 5个月前)

感谢分享。最近被IND区域的robust问题困扰，特来论坛学习。在实践中也深有体会，不同的数据集不同的中性化在robust层面有很大不同。之前跑USA的时候也是，很多alpha在流动性更低的MINVOL区域表现会更佳。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

