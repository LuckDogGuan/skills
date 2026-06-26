# 【Brain Labs】探索Coverage和Date Coverage的计算方法经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【Brain Labs】探索Coverage和Date Coverage的计算方法经验分享_37313013232023.md
- **作者**: HL64570
- **发布时间/热度**: 5个月前, 得票: 13

## 帖子正文

## 一、疑问

### 当你浏览“fundamental6”的时候，肯定会有疑问：为什么Coverage都是50%？有这么巧吗？如果这个数字是正确的，为什么基于基本面的alpha（《零基础学量化》的第二课）的换手率并不高？

### 数据集链接：

[https://platform.worldquantbrain.com/data/data-sets/fundamental6?delay=1&instrumentType=EQUITY&limit=20&offset=0&order=id&region=USA&universe=TOP200](https://platform.worldquantbrain.com/data/data-sets/fundamental6?delay=1&instrumentType=EQUITY&limit=20&offset=0&order=id&region=USA&universe=TOP200)


> [!NOTE] [图片 OCR 识别内容]
> Pyramid
> Date
> Field
> Description
> Type
> Theme
> Coverage
> Alphas
> Coverage
> Multiplier
> assets
> Assets
> Total
> Matrix
> 1.2
> 509
> 1009
> 2262
> assets_CUrr
> Current Assets
> Total
> Matrix
> 1.2
> 509
> 1009
> 491
> bookvalue_ps
> Book Value Per Share
> Matrix
> 1.2
> 509
> 100%
> 574
> Capex
> Capital Expenditures
> Matrix
> 1.2
> 509
> 1009
> 1329
> cash
> Cash
> Matrix
> 1.2
> 509
> 1009
> 447
> cash_st
> Cashand Short-Term Investments
> Matrix
> 1.2
> 509
> 100%
> 372
> Cashflow
> Cashflow (Annual)
> Matrix
> 1.2
> 509
> 1009
> 208
> cashflow_dividends
> Cash Dividends (Cash
> Matrix
> 1.2
> 509
> 100%
> 112
> cashflow_fin
> Financing Activities
> Net Cash
> Matrix
> 1.2
> 509
> 100%
> 107
> cashflow_invst
> Investing Activities
> Net Cash FloW
> Matrix
> 1.2
> 509
> 1009
> 85
> cashflow_Op
> Operating Activities
> Net Cash Flow
> Matrix
> 1.2
> 509
> 100%
> 254
> COgS
> Cost of Goods Sold
> Matrix
> 1.2
> 509
> 100%
> 222
> current_ratio
> Current Ratio
> Matrix
> 1.2
> 509
> 1009
> 375
> FIow)
> FIOW


## 二、借助Brain Labs验证

### 按照我对每日覆盖率的理解，写了以下代码：


> [!NOTE] [图片 OCR 识别内容]
> [1]:
> from brain import Brain,
> Visualizations
> 个 V  古
> iport pandas
> 35
> pd
> import
> nUmPY
> 35
> np
> iport Seaborn
> 35
> SnS
> import matplotlib. pyplot
> 35
> Plt
> [2]:
> brain
> Brain (region="USA "
> delay=l;
> universe="T0P200" )
> field
> brain。
> data
> field ("assets" )
> USA-D1-TOP2OOhgassets
> universe
> brain.
> data
> field ("TOP2O0")
> field_af
> brain.
> data
> frame (field )
> 转为DataFrame格式
> universe_df
> brain.get_data
> frame (universe)
> coverage_daily
> field
> df.notna
> Where (universe
> df)
> SUM(axis=1)
> universe
> af
> SUM(axis=l )
> coverage_daily. plot()
> plt.show()
> 分子:  每天universe中有数字的股票数量
> (100
> (1
> coverage_daily) ) .plot ()
> 分母:  每天universe的股票娄量
> plt. show( )
> 1.000
> 0.975
> 0.950
> 0.925
> 0.900
> 0.875
> 0.850
> 0.825
> 0.800
> get
> get
> get
> N 
> 2015
> 2016
> 2013
> 2014
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


### 
> [!NOTE] [图片 OCR 识别内容]
> 20.0
> 17.5
> 15.0
> 12.5
> 10.0
> 7.5
> 5.0
> 2.5
> y
> 0.0
> IM
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2023
> 2021
> 2022


### 以上画了两张图，其中，第一张是每日覆盖率，第二张是每天的NaN占比，两张图本质是一样的，之所以画第二张，是为了和官方的绘图函数做对照，用于检验我的计算方法是否有问题。


> [!NOTE] [图片 OCR 识别内容]
> [3]。
> Visualizations . plot_coverage (field_df,
> universe
> df)
> Coverage O[assets or topzco
> 20.0
> 作为对照。调用了Brain Labs的覆盖率绘图函数
> 1 5
> 蓝线代表每天的NaN占比
> 15 0
> 发现蓝线和我的计算结果是一模样的;
> Nice!
> 125
> 
> 10 0
> 75
> 50
> 25
> T0
> 7011
> 3014
> 7315
> 7015
> 7017
> 7010
> 2319
> 7020
> 3021
> 7322
> 7073
> Ute
> Rrsr;_nn
> TICFnII0


### 发现结果是一模一样的，说明我的每日覆盖率计算方法是对的。

### 计算Date Coverage和Coverage：


> [!NOTE] [图片 OCR 识别内容]
> [4]:
> Dp
> round(100
> (1
> (coverage_daily
> 
> 0)
> mean()) )
> [4]:
> 100
> Date Coverage: 每日覆盖率中
> 不等于0的天数占比
> [5].
> m
> round
> 100
> CoVerage
> daily. loc [ coverage_daily
> 01
> mean() )
> [5]:
> 96
> 0
> Coverage: 每日覆盖率的均值 (剔除了每日覆盖率等于0的数据)


### 发现Date Coverage与网页中的结果是一模一样的，而Coverage与网页中的结果相差比较大（96% vs 50%），我认为我的结果（96%）更可信：

### 1 我对照了官方的覆盖率绘图函数，证明我的计算方法是对的。

### 2 观察了assets里面的具体数值，发现NaN占比很小，绝对不可能是50%。

### 3 基于基本面的alpha（《零基础学量化》的第二课）的换手率并不高，可以侧面表明Coverage是比较高的。

## 三、结论

### 随机挑选了几个字段实验，发现官方网页上的Date Coverage是准确的，而Coverage是不准确的（有可能是定义不同，目前没找到一个官方的精确定义），准确的Coverage最好自己通过Brain Labs计算获得。

---

## 讨论与评论 (14)

### 评论 #1 (作者: YQ84572, 时间: 5个月前)

对coverage的分析计算进行很详细的讲解，很有助于初入lab研究的新人

--------------------------------------------------------------------------------------------------------------------

感谢分享，祝大佬保持vf0.9+

--------------------------------------------------------------------------------------------------------------------

---

### 评论 #2 (作者: LL87164, 时间: 5个月前)

有用！点赞！👍

看来用 coverage 来做过滤，是不准确的。

另外，可以用华子哥插件看，虽然和上面用 lab 计算的有点误差（96% vs 93%），但是不影响判断。

---

### 评论 #3 (作者: HZ99685, 时间: 5个月前)

我觉得楼主说的是对的，希望官方解释一下。。

---

### 评论 #4 (作者: 顾问 NL80893 (Rank 16), 时间: 5个月前)

太赞了！终于有人深究这个问题了！我之前浏览 fundamental6 的时候也纳闷为啥所有字段 Coverage 都是 50%，总觉得不对劲但又不知道怎么验证，大佬用 Brain Labs 代码实测验证，还理清了 Date Coverage 准确、Coverage 不准确的结论，直接解决了我的疑惑，还提供了自行计算的思路，干货满满，必须收藏！

====================================================================================祝大佬base多多，vf高高，分享更多知识呀～～====================================================================

---

### 评论 #5 (作者: MY82844, 时间: 5个月前)

赞，分析地非常细致，原来那个50%覆盖率怎么算出来的，有什么猜想吗？和回测出来的Long/Short数量有关系吗？

---

### 评论 #6 (作者: LL46807, 时间: 5个月前)

大佬的钻研精神佩服！
=================================================================================
Hard work builds and idleness ruins; thorough planning succeeds and haste fails. Aim high to achieve middling results; aim middling and you will fall short.
=================================================================================

---

### 评论 #7 (作者: YX50005, 时间: 5个月前)

谢谢大佬分享这个有趣又实用的洞察，也慷慨的分享了计算覆盖率的代码，让我Labs的知识又增加了！希望大佬以后可以分享更多labs的有趣用法！

---------------------If you come to the forum to study hard every day, you will get a GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------

---

### 评论 #8 (作者: HZ99685, 时间: 5个月前)

感谢大佬的细心分享！希望官方能解释一下，我也一直很困扰这个问题，既然有50%这个值，就一定有它的计算方法，为什么不给个明确说明是怎么的出来的呢，如果是错误的数据，平台为什么还要提供呢。太纠结了，好多数据集都是这个问题，这样怎能不让人在混沌中撞大运，只能暴力穷举，最终出的一批都是自己都不知道所以然的因子。

---

### 评论 #9 (作者: 顾问 YH25030 (Rank 31), 时间: 5个月前)

谢谢分享。以前对Data Coverage和Coverage是一知半解，拜读了您的帖子，茅塞顿开。这个概念的辨析对在回测前的数据清理大有帮助！

---

### 评论 #10 (作者: AK76468, 时间: 5个月前)

以下是我的想法哈

Coverage是横截面的覆盖度，也就是这个数据集/字段覆盖到了该region的多少股票，也就是在10年窗口中，只要一天有值就算被覆盖到了。

Data coverage是时间序列的覆盖度，也就是这个字段在10年窗口中有多少天是有值的，可以判断这个数据是否仅有几年数据或者是否停更。

---

### 评论 #11 (作者: PS55811, 时间: 5个月前)

给大佬点赞，平台需要更多像您这样具备探究精神的人

---

### 评论 #12 (作者: JX14975, 时间: 5个月前)

感谢大佬分享，但我个人感觉这是个特例：一些常见的字段的coverage都被标为50%了。如果要说明平台的coverage显示完全不准确，还需要其他例子。另外，我也不认同datecoverage都是准确的这一点，待我开贴细说。

---

### 评论 #13 (作者: GZ60647, 时间: 5个月前)

如果我没搞错的话，这个coverage是覆盖了universe的数量，比如如果universe=top3000，50%就代表只有1500的证券有这个值。

而datecoverage也不是覆盖了多少天，而是指覆盖的年份比率，也就是整个数据一共包含10年的信息，而这个字段包含了多少年。大家都知道我们的is现在是10年，如果datecoverage=50%，代表了只有5年的数据，如果是100%，那就代表10年的数据都有。
比如去看ind，top500的earnings6。会发觉coverage是36%，也就是只覆盖了500*36%=180，也就是只有180个证券有这个数据，而datecoverage是44%，所以也就只有4.4年的数据。所以，你去模拟这里的字段，前面5年都是直线。

---

### 评论 #14 (作者: 顾问 MZ45384 (Rank 51), 时间: 5个月前)

大佬的钻研精神令人敬佩，但我认为你计算的只是后者datecoverage，前者是其他含义。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

