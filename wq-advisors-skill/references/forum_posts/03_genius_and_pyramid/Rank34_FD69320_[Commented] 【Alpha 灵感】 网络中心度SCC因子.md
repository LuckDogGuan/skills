# 【Alpha 灵感】 网络中心度SCC因子

- **链接**: [Commented] 【Alpha 灵感】 网络中心度SCC因子.md
- **作者**: TL87739
- **发布时间/热度**: 1年前, 得票: 48

## 帖子正文

这篇Alpha灵感内容包括：

1. 研报复现

2. brain的pnl算法与研报常用的五分组pnl算法的差异研究

3. 降低prodcution correlation的一些小技巧

参考文献：

> 【华西证券】股票网络与网络中心度因子研究
> 【长江证券】关系图谱分析与网络中心度选股策略

1. 研报复现：

在股票市场之中，一个股票的波动除了自身，往往与其他的股票密切相关。股票价格波动的互相影响就形成了关联网络。而处于网络中心的股票则期待更高的风险补偿，基于这个假设，做多处于网络中心的股票，会有更高的预期收益。

研报使用20日的收益率序列截面计算皮尔逊相关系数矩阵，构建关联网络：


> [!NOTE] [图片 OCR 识别内容]
> 2.1 基于网络视角的股票风险刻画:  空间网络中心度因子
> 华西证笄
> HUAXI SECURITIES
> 网络分析方法在金融领域中广泛用于分析系统性风险和描述金融体系稳定性 ,
> 张自力
> 等 (2020)基于网络分析视角,利用股票回报的相关系数构建股票网络,描述股票市场
> 的拓扑结构和系统性风险的传播路径。
> 本文中我们参考上述方法,
> 基于股票平均相关系数来构建股票网络。计算股票1和股票
> 市场组合中其他股票的平均Pearson相关系数:
> N-1
> Dit
> 二
> N - 1
> j=ljti
> 由此,
> 根据前述股票距离的定义,  我们定义股票1和其他股票的平均距离为
> ait = J2 *(I5
> ait反映了该股票与其他股票的平均距离 ,
> 该值越小 ,
> 说明t时刻股票与其他股票的距
> 离越近,与其他股票互相影响程度越高,
> 处在网络的相对中心位置
> 我们定义空间网络相对中心度
> (SCC)
> 1
> SCCit
> 一
> adit
> Cov(ri,t'
> Tiit)


笔者无法找到在Brain计算股票两两之间的相关系数矩阵的operator，因此参考了第二篇研报的公式推导：


> [!NOTE] [图片 OCR 识别内容]
> 模型随想
> 股票关系图谱的数据基础为相关系数矩阵;
> 中心度 =个股与其他股票的相关系数的加权平均
> P1,2
> p1,3
> PiN
> 02,1
> 02,2
> Pz,N
> Pi
> 二
> Oj
> Pij
> Cj
> COT
> (RiB)
> 4j=1
> PN,1
> PN,2
> PNN_
> cor(Ri'
> Oj
> R )
> 二
> cor (Ri,RM)
> Pij
> cor(Ri,R)
> Ljzl
> Lj=l
 由此，相关系数矩阵再求均值，等价于：

```
mkt_ret = group_mean(returns,1,market);ts_corr(returns,mkt_ret,20);
```

结果如下：


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/DI/TOPZOOOU
> Convert to Multi-Simulation
> Chart
> Pnl
> Streak: 44 day
> mkt ret
> Broup
> mean(returns,1,market ) ;
> pt
> ts_corr(returns, mkt
> ret,28);
> 11(2*(1-pt )
> 1GM
> 14M
> 1.1Ks
> 75%
> 0TNIs
> 12M
> 1OM
> 8,00OK
> OOOK
> 4,0OOK
> 2,0OOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> IN



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> Os
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.70
> 37.83%
> 1.18
> 18.299
> 26.81 %
> 9.679600
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count


可以看到，虽然有信号，但是距离可提交还相差甚远。

我们再看研报给出的performance：


> [!NOTE] [图片 OCR 识别内容]
> 2.3
> 全部A股中860因子表现出色;
> 多空组合年化收益达26.80%
> 华西证笄
> HUAXI SECURITIES
> 我们选择最近一个月交易数据来计算股票空间网络中心度因子
> 时间网络中心度因子
> 以及合成的股票网络中心度因子,
> 并测试其在截面上的选股能力
> 空间网络中心度因子5C0表现出色,
> 单调性较好,多空组合年化收益率达26.80%,
> 信息
> 比高达4.64,
> 最大回撤1.79%,
> 因子加权组合年化收益8.88%,
> 信息比3.89 =
> 全部A股空间中,
> SCC因子历史16均值8.30%,
> 年化16_1R为3.97 _
> 图4:  空间网络中心度因子分组单调性较好
> 表1:  全部A股中空间网络中心度因子分组及多空表现
> Demeamettieutratf Cumutattve Retwm
> 年化
> 年化
> 累积
> 最大
> 组别
> 信息比
> 收益率
> 波动率
> 收益率
> 回撤
> 笫一组
> -6.00%
> 26.98%
> -48。60%
> -0.22
> -73.93%
> 
> 笫二组
> 0.58%
> 25.84%
> 6.40%
> 0.02
> -63.34%
> 2.0
> 笫三组
> 5.32%
> 25.59%
> 74.66%
> 0.21
> -57.27%
> 笫四组
> 7.69%
> 25。68%
> 121.73%
> 0.30
> -52。62%
> 笫五组
> 10.04%
> 25.66%
> 179
> 87%
> 0.39
> -49.41 %
> 量
> 笫六组
> 11.55%
> 25.83%
> 224.01%
> 0.45
> -43.55%
> 笫七组
> 13.29%
> 25.95%
> 282
> 71%
> 0.51
> -40.08%
> 1,0
> 笫八组
> 15.23%
> 26。13%
> 359
> 32%
> 0.58
> -36.86%
> 笫九组
> 17.50%
> 26.14%
> 466.53%
> 0.67
> -36.11 %
> 筻土组
> 19。64%
> 26.36%
> 587.59%
> 0.75
> -36.44%
> 因子加权组合
> 8.88%
> 2.28%
> 149.53%
> 3.89
> -0.86%
> 多空组合
> 26.80%
> 5。78%
> 1184.66%
> 4.64
> 一1。79%
> 202
> 资料来源: Wind,
> 华西证券研究所
> 资料来源: Wind,
> 华西证券研究所
> 慧博资讯'
> 专业的投资研究大数据分享平台
> 2018
> 2020
> 2010
> 2012
> 2016


研报20日rankIC高达8%，这个表现不会只有1.7的sharpe。

**因此涉及本文第二个主题：brain的pnl算法与研报常用的五分组pnl算法的差异研究**

A股券商投研报告的因子喜欢使用5分组或者10分组的算法。该算法将股票根据因子值进行排名然后分成5组或者10组，分组内部等权计算多头收益，然后使用多头第十组-多头第一组作为多空的pnl。

brain的计算方法可以参考：

[⭐ How BRAIN platform works | WorldQuant BRAIN](https://platform.worldquantbrain.com/learn/documentation/create-alphas/how-brain-platform-works)

简单来说就是每个因子值归一化之后的权重都会成为最后的头寸。

因此两种算法下：

1. coverage不同。分组计算pnl的算法最后的coverage相当于只有截面的20%或者40%。

2. 股票的权重不同。分组算法下分组内等权，也就是说分组内部的股票的因子值失去了意义，第一组内不管因子值再高，和其他成员都是等权。而brain平台的回测下，每一个股票的因子值都会成为头寸的一部分。

因此很多五分组/十分组研报直接用其表达式做出来的alpha往往不尽人意，这个是正常的。笔者之前探讨过如何完全复刻五分组/十分组的算法，但没想到最优解，尽管如此，仍然可以使用rank这个operator，将因子值变为均匀分布，去靠近分组算法。

这个alpha加上rank之后，即可提交。


> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Simulation 2
> Simulation 3
> Simulation 4
> CODE
> RESULTS
> LEARN
> DATe
> Settings
> CHNIDIITOPZOOOU
> Convert to Multi-Simulation
> Chart
> Pnl
> Streak: 44
> mkt
> ret
> group_mean
> returns
> 1,market);
> pt
> corr(returns, mkt_ret, 20);
> rank(1/ (2*(1-pt)) )
> 17.5M
> 50.7s
> 76%
> 36.7Ws
> 15M
> 12.5M
> 1OM
> 7,50OK
> 5,0OOK
> 2,50OK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Clone this Alphain a new tab
> Add Alphatoa
> Openalpha details innew
> Fxamnle
> SiMate 
> SMaato
> Check Submission
> Submit Alpha
> day
> tS_



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.04
> 19.559
> 3.23
> 22.01 %
> 9.64%
> 22.51900


此外，从研报可以看出，这个alpha是一个多头选股能力非常强的alpha，我们可以通过robust universe test管中窥豹：


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 11 PASS
> Sharpe of 3.04is above CUtOff Of 2.07.
> Fitness Of 3.23is above cUtOff of 1.
> Turnover of 19.559 is above cutoff of 1 %_
> Turnover of 19.559 is below cutoff of 709.
> Weight is well distributed over instruments
> Returns of 22.01% is above cutoff of 8%.
> Sub-universe Sharpe of 2.68 is above cUtoff of 2.16.
> Robust universe Sharpe of 1.50 is above cUtoff of 1.22 (4096 of Alpha).
> Robust universe returns Of 10.739 is above cutoff of 8.809 (40% of Alpha):
> 2 year Sharpe of 2.93 is above CUtOff of 2.07.
> Pyramid theme CHN/DI/Price Volume matches with multiplier of 1.1.
> WARNING


即使考虑A股的涨跌停限制与做空限制，这个alpha仍有不错的表现，并且高于cutoff不少。

很可惜，A股的alpha尤其是pv类型风格太类似了，这个alpha的prod corr有0.85


> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximum
> Minimum
> Last Run: Tue; 11/19/2024,6.50 PN
> &
> 0.8517
> -0.4252
> 10Ok
> 0
> 1Ok
> 鬓
> 1
> 昱
> 100
> 8
> 10
> 01
> 0
> 0?
> ~9
> 09
> 3.
> 01
> 02
> 0:
> 0.5
> 0.2.
> 令


接下来是本文第三个话题，推荐一些降低production correlation的小技巧：

```
signed_power(x,n)
```

通过对alpha进行指数运算，调整分布，可以降低correlation,优化performance

```
hump
```

hump算子可以将t日与t-1日变动过小的alpha值保留原值，一般用来降低turnover，有时也可起到降低correlation的效果。

```
vector_neut
```

通过正交一些风格因子，往往可以降低correlation

```
trade_when(group_count(alpha,{group})>{threshold},alpha,0)
```

这个表达式相当于去除一些截面上股票过少的交易日，在优化performance、降低correlation的方面往往有奇效。

本人时间有限，在这里可以抛砖引玉，大家可尝试这些方法，看看能否将这个alpha提交~

---

## 讨论与评论 (16)

### 评论 #1 (作者: WL13229, 时间: 1年前)

请找到办法修改并提交的同学务必在此留言，尊重原创IP

---

### 评论 #2 (作者: MC63847, 时间: 1年前)

这个pnl图形我好像之前看到过类似的，可能与之前某个idea产生的效果有异曲同工的地方

---

### 评论 #3 (作者: QS13316, 时间: 1年前)

参考本文之后修改参数

mkt_ret = group_mean(returns,1,market);

pt=ts_corr(returns,mkt_ret,10);

rank(1/(2*(1-pt)))

---

### 评论 #4 (作者: JZ71360, 时间: 1年前)

这个可以作为一个基础信号，合并其他的信号，可以产生很好的提交

---

### 评论 #5 (作者: WL13229, 时间: 1年前)

[JZ71360](/hc/en-us/profiles/20064207247639-JZ71360)

这种行为有over fitting风险

---

### 评论 #6 (作者: AA53991, 时间: 1年前)

赞同

---

### 评论 #7 (作者: AA53991, 时间: 1年前)

手动点赞

---

### 评论 #8 (作者: AB30207, 时间: 1年前)

很好的帖子

---

### 评论 #9 (作者: JB71859, 时间: 1年前)

这篇文章对于Alpha策略的深入分析非常有价值，尤其是在研报复现和与Brain的PNL算法对比部分，提供了很多实用的见解。你对研报中的关联网络和中心度因子的理解很到位，并通过具体的实践验证了其可行性。同时，关于五分组PNL算法和Brain计算方法的差异探讨，能够帮助大家更清晰地理解为何传统的五分组策略有时不尽人意，并且如何通过Brain的回测方法来优化因子权重和头寸。

关于降低生产相关性的小技巧部分，像 `signed_power(x, n)` 、 `hump` 算子和 `vector_neut` 这些方法提供了很好的思路，能够有效改善Alpha的表现，尤其是在降低相关性和提升多样性方面的效果，确实值得在实际操作中深入尝试。

总的来说，这篇文章结合了理论和实践，逻辑严谨，思路清晰，对于那些从事Alpha开发和量化交易的同学来说，有很高的参考价值。期待更多的分析和细节，帮助我们更好地理解如何提升Alpha的效果！

---

### 评论 #10 (作者: JC70166, 时间: 1年前)

点赞

---

### 评论 #11 (作者: MJ66615, 时间: 9个月前)

大佬这篇文章给了我很强的启发性，特别是研报中相关系数加权平均的等效，让我学到了很多

---

### 评论 #12 (作者: CC85858, 时间: 9个月前)

很优秀的文章，里面的降低相关性的方法很有用，只不过太多人用了，快失效了😄

---

### 评论 #13 (作者: 顾问 FD69320 (Rank 34), 时间: 6个月前)

时隔一年重新阅读，依然倍感收获，谢谢大佬的分享。

==================================================================================

WorldQuant is anyone‘s legend

---

### 评论 #14 (作者: JC78366, 时间: 5个月前)

非常好的文章，让我了解了研报研究的内容和平台回测的不同，降prod correlation的方法很好用

---

### 评论 #15 (作者: LY67324, 时间: 4个月前)

感谢分享，作为新手，学习到很多

---

### 评论 #16 (作者: RH86116, 时间: 1个月前)

谢谢大佬的分享,让我学到了制作alpha的方法：通过阅读学习论文，利用的论文知识，产生好的idea，在通过平台里对应的数据集和操作符去实现验证的想法，很有趣！

==================================================================================

WorldQuant is anyone‘s legend
WorldQuant 是任何人的传奇

---

