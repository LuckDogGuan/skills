# 【IDEA BY TIGER】关于在ASI，如何提升JPN表现不佳的一个思路经验分享

- **链接**: [Commented] 【IDEA BY TIGER】关于在ASI如何提升JPN表现不佳的一个思路经验分享.md
- **作者**: ZZ13271
- **发布时间/热度**: 10个月前, 得票: 86

## 帖子正文

一、首先我们来看一下初始的signal及其在country维度下的pnl表现（应大群要求，这里隐去了df，因为这个不重要），我们可以看到这个初始的signal的sharp为1.35，且在JPN其表现是负的


> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Simulation 5
> Multi-Simulation 5
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> ASIIDIIMINVOLIM
> Convert to Multi-Simulation
> SOOK
> Streak: 73
> Iog_Ip(winsorize
> ts_backfill(vec
> choose(anlGg
> nth=0),22), std-4) )
> SOOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Pnl - 2
> Australia
> Hong Kong
> Indonesia
> Japan
> Korea, Republic of
> Malaysia
> NeN
> Zealand
> Singapore
> Thailand
> Taiwan
> IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> Single Data Set Alpha
> Aggregate
> Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marsin
> 1.35
> 10.819
> 0.75
> 3.889
> 4.50%
> 7.189600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone this Alphaina newtab
> IOOW。
> 2013
> 0.00
> 0.00N
> 0.00
> 0.0035
> 0.0Oqo
> 10.00930
> day
> Year


二、思路：既然只有JPN表现为负，那我们是不是可以去掉它，我想到的办法是将所有公司的市值先在country里分组，也就是group_mean(cap,1,country)；再对其进行排名，也就是rank(group_mean(cap,1,country))；这个时候我们需要知道JPN在所有国家排名的中的位置，通过提问大模型，我们知道日本排在第四，如图：


> [!NOTE] [图片 OCR 识别内容]
> 亚洲
> (含澳大利亚
> 中国台湾
> 中国香港)  并剔除中国大陆 A 股后
> "平均市值"最高的前10  个经济体
> -以 「总市值 :上市公司家数」计算。取最新可得数据 (202403-2025
> Q2)
> 表格
> G复制
> 排名
> 经济体
> 总市值
> 上市公司家数
> 平均市值
> 新加坡
> $0.65T
> 约 650家
> $1.0 B
> 中国香港
> $4.55T
> 约2600 家
> $1.75 B
> 中国台湾
> $1.92T
> 约 960家
> $2.0B
> 日本
> $7.0T
> 3933家
> $1.8 B
> 澳大利亚
> $1.72T
> 2200+家
> $0.78 B


三、既然JPN排名第四，那么其在rank(group_mean(cap,1,country))的位置可能是在0.6-0.8之间；那么我们通过如下表达式，可以达到去除jpn的效果：

signal=s_log_1p(winsorize(ts_backfill(vec_choose(df,nth=0),22),std=4));

gr = rank(group_mean(cap,1,country));

if_else(or(gr>0.8,gr<0.6),signal,nan)

优化后的表现如下，就差一点点了：


> [!NOTE] [图片 OCR 识别内容]
> Ua
> signal=s
> Ip(winsorize(ts_backfill(vec_
> choose(df,nth-o),22), std-4) );
> 即
> rank
> BroUP
> mean
> cap,1, country
> ZSOOK
> if_else(or(gr>0 . 8,Er<0 .
> signal,nan)
> Z0OOK
> 1,5OOK
> 1,OOOK
> 5OOK
> 10/09/2015
> Train pnL. 211.59K
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawown
> Warsin
> 1.54
> 9.389
> 0.99
> 5.189
> 3.129
> 11.05960o
> ICg
> 6),


四、再对其二阶，done


> [!NOTE] [图片 OCR 识别内容]
> Streak: 73 day
> signal=s
> Ip(winsorize(ts_backfill(vec_choose
> nth=o),22), std-4) );
> 1,5OOK
> 8
> rank(Broup_
> mean(cap,1, country) );
> alpha
> if_else(or(gr>0 . 8,Br<0.6),signal,nan);
> OOOK
> group_
> Zscore(alpha, bucket(rank(cap ),range= '0.1,1,0.1'))
> SOOK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> IS Summary
> Period
> IS
> 05
> Theme: ASI Scalability Theme X2
> Regular Alpha
> Pyramid theme: ASIIDTIPV X1
> Pyramid theme: ASIIDTIANALYST X1.3
> Aggregate
> Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.76
> 10.549
> 1.19
> 5.679
> 3.229
> 10.779600
> (df
> Iog



> [!NOTE] [图片 OCR 识别内容]
> 戌
> Correlation
> Self Correlation
> WaxmUM
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Ninimum
> Last Run: Fri, 03/29/2025
> 11:53 4M
> 0.3056
> -0.4304
> TOON
> 1N
> 4
> 1OK
> 昱
> 100
> 8


---

## 讨论与评论 (17)

### 评论 #1 (作者: TX98685, 时间: 9个月前)

好思路，又学会一招

---

### 评论 #2 (作者: BW14163, 时间: 9个月前)

厉害啊，通过向AI咨询国别之间在ASI中的市值rank，进一步剔除目前国家，从而提升alpha，这个思路很有启发性

---

### 评论 #3 (作者: XW99584, 时间: 9个月前)

学习了，谢谢虎哥

---

### 评论 #4 (作者: YQ51506, 时间: 9个月前)

很好的魔修思路，虽然不推荐常用，但是思路清晰，值得学习

---

### 评论 #5 (作者: XC66172, 时间: 9个月前)

很好的思路，谢谢虎哥~  感觉以后回测完都可以分国家看看表现，对于不好的国家可以进一步剔除。（虽然有点担心是否过拟合）

====================================

FIGHTING LABUBU!

====================================

---

### 评论 #6 (作者: JB53978, 时间: 9个月前)

可以，学了一个小技巧，确实厉害，这个小技巧只有在jpn有效吗，其他的比如usa和chn呢，有尝试其他region吗

---

### 评论 #7 (作者: TL53163, 时间: 9个月前)

signal=s_log_1p(winsorize(ts_backfill(vec_choose(df,nth=0),22),std=4));

gr = rank(group_mean(signal,1,country));

if_else(gr>=0.1,signal,nan)

可否通过这样，直接把signal表现最不佳的一个国家排除掉呢

---

### 评论 #8 (作者: ZZ13271, 时间: 9个月前)


> [!NOTE] [图片 OCR 识别内容]
> TL53163
> 390
> signal=s_log_lp(winsorize(ts_backfill(Vec_choose(dfnth=o),22),std=4));
> gr
> rank(group_mean(signal,lcountry));
> if_elselgrs=Olsignalnan)
> 可否通过这样,直接把signal表现最不佳的一个国家排除掉呢
> Jays


这应该是不行的，pnl是simulate之后的结果，你这个是simulate之前


> [!NOTE] [图片 OCR 识别内容]
> YO51506
> 7 days ago
> 很好的魔修思路。虽然不推荐常用=
> 但是思路清晰。值得学习
> <
> XC66172
> 4daysago
> 很好的思路。谢谢虎哥~  感觉以后回测完都可以分国家看看表现。对于不好的国家可以进一步剔除。 (虽然有点
> 担心是否过拟合


风险是有的哦，的确不建议常用


> [!NOTE] [图片 OCR 识别内容]
> 3853978
> 4days ago
> 可以,
> 学了一个小技巧。确实厉害,这个小技巧只有茌jpn有效吗。其他的比如usa和chn呢。有尝试其他
> region吗


只有在ASI、GLB、EUR这种包含多个国家的才适用。先visual一下看看在country维度下的pnl，在这个前提下只要知道表现不好的某个国家或地区的平均市值排名，就可以试试去掉它。当然也可以只做表现最好的国家，不过我怀疑这样的话就严重过拟合了

---

### 评论 #9 (作者: YW58613, 时间: 9个月前)

又学习了一个知识点，感谢分享。

---

### 评论 #10 (作者: AM12075, 时间: 9个月前)

======================================================================

能否直接写成 gr=group_rank(cap,country))？这个和gr = rank(group_mean(cap,1,country))有什么区别吗？

======================================================================

---

### 评论 #11 (作者: ZZ13271, 时间: 9个月前)


> [!NOTE] [图片 OCR 识别内容]
> 能否直接写成 gr=group_rank(cap;country))? 这个和gr
> ranklgroup_meanlcap;l,country)) 有什么区别
> 吗?


区别还是有的，一个是一个国家的平均市值排名，一个是每过国家内各个股票的排名

---

### 评论 #12 (作者: XW99584, 时间: 8个月前)

那是否可以用group_sum，然后求总市值排名呢

---

### 评论 #13 (作者: DS48533, 时间: 8个月前)

在论坛总是能刷到耳目一新的玩法，if_else是被玩坏了

---

### 评论 #14 (作者: JZ94116, 时间: 6个月前)

牛逼

---

### 评论 #15 (作者: MY82844, 时间: 6个月前)

[ZZ13271](/hc/en-us/profiles/27032633829527-ZZ13271)  这么操作之后，从average size分布上看效果怎么样，剔除干净吗？


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Average SIZe By Country
> Region
> Talwan
> AUstralla
> Thalland
> Kong
> Singapore
> Indonesla
> New Zealand
> Malaysia
> Korea, Republic of
> Japan
> Hong


---

### 评论 #16 (作者: 顾问 MZ45384 (Rank 51), 时间: 5个月前)

但是这个JPN排名不是第二吗，平均市值1.8仅次于台湾。但rank下来应该是0.6-0.8, 应该是打错了吧。优化方案加一, 利用市值排名去除表现不佳的区域：

gr = rank(group_mean(cap,1,country));

if_else(or(gr>up_rank,gr<down_rank),a,nan)

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #17 (作者: JC31003, 时间: 2个月前)

真的是救命了，太感谢了

---

