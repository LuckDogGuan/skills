# 【⭐Uncommon Operators⭐】 操作符研究之generalized_rank

- **链接**: https://support.worldquantbrain.com[Commented] 【Uncommon Operators】 操作符研究之generalized_rank_37245403025431.md
- **作者**: 顾问 SJ65808 (Rank 20)
- **发布时间/热度**: 6个月前, 得票: 63

## 帖子正文

赛季末了，最近在一直在维护自己的六维，发现一些不常见的操作符还没有使用到，所以一直在探索这些操作符的使用方法。正好坤奇老师今晚分享课提到了generalized_rank(广义排序)这个操作符，我也用这个操作符做出一个alpha,因此分享一下我对这个操作符的研究。

函数说明如下:


> [!NOTE] [图片 OCR 识别内容]
> Cross Sectional
> Oerator
> Scope
> Oescripton
> EeREralized
> rankopen mzl)
> T -
> Resular
> The iJsa
> T-Ur-ren
> 0YESnINRTITEN1
> =
> TTE Ci=
> UE -
> nosinswNEnTIh
> biaeer Value
> -
> SNLCC=
> FonTh=
> ISTIMEnTih
> 三三
> TII
> Wore Jssils
> ThE Tos =h
> Pe
> SO
> SUT
> 迂工 =0
> TRT
> ThoTp
> 1
> SgII
> [-1
> 近工 >
> In Case When m=0 since any number raised to the Zero pOWeris
> the result is the numberoT
> instruments with lesser Value minus the number of instruments with bigger Value divided by total
> count ofinstruments
> In Case ofm=l the result is simply
> Note: Ittakes Very longtime when M != 0 OrM != 1
> Ctm


首先这是一个截面的操作符，可以类似rank来看，但是平台并没有对应的ts和group操作。

在函数定义中有|x_i - x_j|^m,对数学比较敏感的同学应该能发现这实际上就是计算两个数的距离，当m=1的时候是绝对值距离，m=2的时候就是常见的平方距离。此外定义中使用sign(x_i  - x_j)来判定两个点的符号，从数学的角度来说这个操作符就是计算一个点对一个集合中所有点的带符号的距离均值。

函数说明中提到当m!={0,1}的时候计算会比较耗时，那就暂时考虑这两种特殊情况，当m=0时，公式如下:


> [!NOTE] [图片 OCR 识别内容]
> SMi sign(zi
> generalized_rankl-i, M 一 0)


实际就是计算集合中小于x_i个数以及大于x_i个数的差值，然后再除以总数N

当m=1时,公式如下:


> [!NOTE] [图片 OCR 识别内容]
> Xsigng
> 卫j)
> Iz;
> Djll
> generalized_rank(Ii, m 二 1) =
> C_
> 一1
> (?j
> ~)
> Cxi 1 * ("; -~ )
> N
> A
> CN (:
> ?j
> 二 Di -正 Ni = {3 < Ti}, N
> {疋 >-}
> N


从这个推导可以看出当m=1的时候实际上计算的是点x_i与集合所有点的均值之差，相信到这里有的同学应该能联想到之前的模板

```
{data} - group_mean({data},1,market)
```

两者居然在数学意义上是等价的，而且还能省略一个操作符！！！

下面在平台上使用两个表达式做一下验证，结果也和数学推导对应的上


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Beneralized_rank(close,圈-1)
> Data SEtphs
> #CIose
> Braup_mean(open,1,market )
> ABaregate Data
> CIA
> MTyII
> 0.13
> 9%
> 0.05
> 1.93%
> 60.099
> 48.849600
> SIIUIatIOn
> Settings
> Vear
> Shape
> TurOVer
> Ftress
> Returts
> Drawdow
> Nalgl
> Long Cwnt
> Short Cot
> Istrut Type
> Regl
> Uelse
> 7034101
> a
> Olay
> UIUNaON
> Neutallalon
> Pastewrtato
> HaN Hanlng
> Unlt Handling
> Max Trate
> EaJi?
> US-
> TOF
> Fast Spressizn
> ITI=
> TT
> 2013
> 7.85
> 2373
> 0.43
> 3.93:
> 2.615
> 3:
> 201-
> 172
> 3.99::
> 17
> 1577:
> 24
> 2015
> 07
> 7.93:
> 9.3755
> 3_~:
> 258
> 2015
> 3.02
> 0.633
> 7.31:
> 18.775
> 571%:
> 773
> Clone Alpha
> 2017
> D-E
> 1.18:
> 8.773
> 1372:
> 28S
> 2013
> 3515
> 15.00:
> 18.335
> 62414:
> 27
> N Chart
> Pnl
> 2019
> 7.85
> 047
> 0.79
> ~1.75::
> 15.77
> 40:
> 3
> 2020
> 201
> 07
> 3.50
> 3.8
> -9.5,
> TE:
> 7
> 136::
> 13.74
> 3755:
> 2022
> 0583
> 10
> 71.47
> 851_1:
> 2汲
> SJOK
> 2023
> 145
> 46.03
> -15004
> 8.273
> -6,71111:
> S
> Risk neutralized
> SOOK
> Aggregate
> Data
> DJwUul
> 0.6
> 0.79%
> 0.47
> 6.2496
> 16.63%
> 157.579600
> Jan"14
> Jari5
> J37'15
> Jan "13
> J"13
> Jan 20
> Jan -1
> J 22
> J3733
> Snsle
> 113
> Ja



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Beneralized_rank (close,M=1)
> Data SEtphs
> Close
> Broup_mean(open,1,market )
> Agaregate
> Uata
> CIAT [
> 0.13
> 0.81%
> 05
> 1.92%
> 60.1096
> 47.699600
> SIIUIatIOn
> Settings
> Shape
> TIT
> Ftress
> Retuts
> IIao
> Nalgl
> Long Cwnt
> Short Cot
> Istrut Type
> Regl
> Uelse
> Uawwag
> Dcay
> Olay
> Truncatlon
> Neutrallalon
> Pastewrtato
> NaN Hanl
> Unlt Handlng
> Max Trate
> EaJi?
> US-
> TOF
> Fast Spressian
> ITI=
> Vrty
> 2013
> 7.85
> 23
> 39
> 2.615
> 3E:
> 251
> 201-
> 10
> 1.
> 3.99::
> 17
> 1525
> 24
> 2015
> 1.09
> 31
> 0.02
> 7.90:
> 9.375
> _=
> 253
> 2015
> JEJ
> 3.25::
> 18.77
> 7:
> 2
> Clone Alpha
> 2017
> 7.3
> 047
> 1.19:
> 8.773
> 135.515
> 28S
> 2013
> 5
> EOO:
> 18.325
> 6015:
> 27
> N Chart
> Pnl
> 2019
> 7.86
> 0483
> 0.30
> ~1.75::
> 15.725
> 44535
> 3
> 2020
> -201
> 7
> 3.50
> 3.85:
> -9.E06
> -1,0132:
> 289
> 0.66
> 7
> 1.-5::
> 13.735
> 321:
> 2022
> 5
> 2.08:
> 21.435
> 35255:
> 2汲
> SJOK
> 2023
> ~1.31
> 145
> 51 _
> 506:
> 8.2750
> -6.6577
> S
> Risk neutralized
> SOOK
> Aggregate
> Data
> WUUI
> 0.67
> 0.81%
> 0.47
> 6.2496
> 16.63%
> 154.869600
> Jan"14
> Jari5
> Jan "13
> J"13
> Jan 20
> Jan 21
> J 22
> J*23
> Pn
> Risk NEralzzg Pn
> 匮 Correlation
> Snsle


之前系列，欢迎大家评论点赞    [[L2] 操作符研究之tail家族_36915505477271.md]([L2] 操作符研究之tail家族_36915505477271.md)

---

## 讨论与评论 (15)

### 评论 #1 (作者: ZW16380, 时间: 6个月前)

太快了，会刚开完不久就有帖子了哈哈哈！赛季末卷六维时挖到这种冷门操作符的解析，简直是及时雨！从广义排序的截面属性，到 m 取 0/1 时的数学推导，尤其是点破 m=1 时和 `group_mean({data},1,market)` 等价这一点，直接打通操作符复用的任督二脉，还能省操作符数，太绝了！跟着坤奇老师的课落地实践，再附上平台验证结果，逻辑链超扎实。这种把数学原理和平台实操结合的分享，对因子开发者来说，比单纯的模板分享印象更深刻！期待后续也能有更多冷门操作符的拆解，赛季末冲六维全靠这种硬核干货续命！

---

### 评论 #2 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

补充说明： 只是一下等价关系成立

```
{data} - group_mean({data},1,market)  = generalized_rank({DATA},m=1)
```

group_mean中加权参数是其他的情况下不成立，且分组参数不是market也不成立，使用generalized_rank最大好处就是节省一个操作符

---

### 评论 #3 (作者: BW14163, 时间: 6个月前)

为大佬点赞，一点一点的吃头操作符，时间积累后，总会出现不一样的风景

---

### 评论 #4 (作者: DD76063, 时间: 6个月前)

为啥是以market来分组呢？

---

### 评论 #5 (作者: MY49971, 时间: 6个月前)

哇哦，大佬厉害，可惜没有这个操作符~~

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #6 (作者: YQ84572, 时间: 6个月前)

很详细的操作符研究的深入分享，对探索操作符很有帮助,感谢大佬的分享。

-----------------------------------------------------------------------------

祝大佬base多多，vf0.9+

-----------------------------------------------------------------------------

---

### 评论 #7 (作者: MY82844, 时间: 6个月前)

感谢分享，不知道，这种高级算子一般用在什么数据集上会有特效？

---

### 评论 #8 (作者: XC66172, 时间: 6个月前)

谢谢佬分享，感觉generalized_rank这个操作符是GM才有的吧。。 我就没有

group_mean/group_median kunqi倒是分享了个不错的模板，有空试试~~

===========================

FIGHITNG LABUBU!`

===========================

---

### 评论 #9 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

@MY82844 和数据集没啥关系，都可以用，我自己用下来analyst出货率更高一些

---

### 评论 #10 (作者: ML10446, 时间: 6个月前)

==================================================

哇！感谢大佬分享，希望自己早日可以使用更多运算符

==================================================

---

### 评论 #11 (作者: LG87838, 时间: 6个月前)

好陌生的操作符，点进去一看发帖大佬是GM。。。

学习思路和方法，希望下一个季度可以有这样的操作符。

--------------------------------------------------------------------------------------------------------------------

慢慢来，相信时间的力量。

--------------------------------------------------------------------------------------------------------------------

---

### 评论 #12 (作者: JX14975, 时间: 6个月前)

[XC66172](/hc/zh-cn/profiles/28880767093655-XC66172)  大佬，kunqi老师何时讲过这个 group_mean/group_median 模板？是私人会议还是公开场合呢？ 我感觉自己错过了好多东西。谢谢大佬，祝大佬base多多。

---

### 评论 #13 (作者: ZF97721, 时间: 5个月前)

感谢分享，还没有见过这个operator，小小gold的权限差距好大。不过看大佬的推理，这个{data} - group_mean({data},1,market)倒是用过，用来做一些alpha的增强，会出一些因子的，不过还没直接用在datafield上直接套用测试，不知道效果怎么样。

---

### 评论 #14 (作者: LJ85703, 时间: 5个月前)

学到了，大佬就是大佬

---

### 评论 #15 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 5个月前)

记录了：generalized_rank(x, m=1)  <=>  x - group(x, 1, market)。可以省下一个op，但可惜小小expert没有这个操作符的使用权限。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

