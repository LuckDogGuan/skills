# 【Alpha灵感】使用nip族数据点亮news塔Alpha Template

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】使用nip族数据点亮news塔Alpha Template_40847481080087.md
- **作者**: MY82844
- **发布时间/热度**: 25天前, 得票: 78

## 帖子正文

根据之前 [点亮sentiment塔]([Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md) 的经验，我们发现：相关性算子+FAST neutralization的组合比较适合处理sentiment的数据。考虑到news数据和sentiment数据经常有很强的关联性，所以自然地，我们想到在EUR的news塔也使用一下这个组合，看是不是可以跑出一些不错的alpha。

考虑几个基础的相关性模版：

```
ts_corr(fld, returns, ndays)ts_covariance(fld, returns, ndays)ts_regression(returns, fld, ndays, lag = 0, rettype = 2)
```

在EUR地区D0/D1回测下来，我们发现：

```
nip(news impact projection)-字段在相关性模版下面经常有不错的表现
```

在news18(Ravenpack News Data)，我们可以找到不少此类字段。通过搜索，后来我们发现其实可以在更多数据集找到类似包含nip字符串的字段。比如，在EUR D0，容易找到一些来自news和pv87的字段：


> [!NOTE] [图片 OCR 识别内容]
> 山ta_fie1ui
> dataset
> i Tegion
> delay
> Cout
> USEI
> out
> I31
> CoJh
> Iih
> IeH31
> EJ
> II31
> ColP_AO_nip
> IeI3
> ETJ
> I31
> Jlltiple
> ColP_AO_nip
> IeH31
> IIN3
> Jllltiple_
> ColP_AO_nip
> IeI3
> IIN3
> Jultiple_
> COJP_Iip
> IeH31
> II31
> Jlltiple
> COJP_Iip
> IeI3
> II31
> Iih
> IeH31
> IIN3
> IeI3
> IIN3
> tiple_
> COJP_Iip
> IeI3
> II3
> Jlltiple
> COJP_Iip
> IeI3
> IHS20
> tiple_
> ColP_AO_nip
> IeHS20
> IIN3
> Jultiple_
> CoJh
> dO_Iip
> IeHS20
> Jultiple_
> COJP_Iip
> IeHS20
> IHf320_Jlltiple_
> COJP_Iip
> IeHS20
> IHS20
> Iih
> IeHS20
> IeHS20
> IeH3 坊
> J3
> IeH3 坊
> TI 5
> IeH3 G
> IeH3 G
> IeH3 50
> JI350
> Iih
> IeI3 50
> pt8?_PI2_
> elparg20
> SIOUP_Ilip_accuigitiors _
> JerSEr3
> TTS1
> PI2_ezlat忌20_
> SIOUP_Ilip_accuigitiors _
> JerSEr3
> H8
> prY2_expav820_
> SIOUP_Iip_
> prY2_expav820_
> SIOLP_Iip_a1
> D8?
> HIT2
> elparg20
> SIOUP_Iip_
> &38et3
> H&
> DIT2_
> elparg20
> SIOUP_Iip_a83eta
> DIT2_
> elparg20
> SIOUP_Ilip_dividerds
> Pr 8? _PI72_eypa3忌20_
> SIOUP_Ilip_dividerds
> P 8? _PIT2_
> elparg20
> SIOUP_Iip_earrirss
> ETJ
> D8?
> pIv2_expa3g20
> SIOUP_Iip_
> earllirg3
> alpha
> Dra7


不同的nip字段跑下来还有一些区分度，替换着用，可以降低相关性：


> [!NOTE] [图片 OCR 识别内容]
> ts_covariance(Vec_aVg (msSO
> peturns,
> 186
> Simulation Settings
> Instrument Type
> Region
> UnNerse
> LangUage
> Decay
> Delay
> Truncation
> Neutralizatijon
> Pasteuriation
> Lookback
> MaxTrade
> Max Position
> Equiz
> EUR
> TOPZSOD
> Fast Expression
> 0.005
> Fast FECOFs
> Clone Alpha
> N Chart
> Pnl
> OOOK
> OOOK
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> nip);



> [!NOTE] [图片 OCR 识别内容]
> Val
> Vec_aVg(nws28_j);
> nds
> 180;
> ts_covariance(Val, returns, nds )
> Simulation Settings
> Instrument Type
> Region
> Unmerse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pastauriation
> Lookback
> MaxTrade
> Max Position
> Equi?
> EUR
> TOPZSO
> Fast Expression
> 0.00-
> Fast TECOFs
> Clone Alpha
> Chart
> Pnl
> 5OOOK
> 25OOK
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


总结：相关性算子+FAST neutralization+nip字段，在EUR地区的D0/D1出PPA还是非常容易的，后续结合一些ts算子和group算子控制下PC仍然可以出一些不错的RA。抛砖引玉，有待小伙伴们继续挖掘。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 眙 Regular Alpha
> Dyramid theme: EURIDOIPV %1.5
> Dyramid theme: EURIDOINEWS %1
> Aggregate Data
> Sharpe
> TICRIS
> Iitmess
> TTNICn 
> Drawdown
> Marain
> 3.3
> 10.689
> 2.6
> 8.149
> 2.049
> 15.259
> 000


---

## 讨论与评论 (14)

### 评论 #1 (作者: HX55085, 时间: 24天前)

感谢大佬模板，尝鲜啦！

---

### 评论 #2 (作者: HZ99685, 时间: 24天前)

感谢佬，我一直有个疑问，这样会不会过度使用pv1数据，造成pv数据集受限，大佬是怎么考虑的呢？

---

### 评论 #3 (作者: JX84394, 时间: 24天前)

牛逼 USA d1 出信号了 交了一个ppa,感谢！非常好的模板，文章简洁有力，赞！！！

---

### 评论 #4 (作者: JL52079, 时间: 24天前)

感谢大佬分享，确实是不错的思路，这让快断粮的我又燃起了斗志！

=========================Just do it！=========================

---

### 评论 #5 (作者: WL58980, 时间: 23天前)

非常不错的模板，马上去试试，感谢分享！！！！

============================================================================

Study hard — quality over quantity, no room for mediocrity. Cherish every learning opportunity, stay focused, and learn from the experts. Keep pushing!

============================================================================

---

### 评论 #6 (作者: WL20457, 时间: 23天前)

感谢博主分享的知识，news数据和sentiment数据经常有很强的关联性， 另外我自己很少用ts_covariance， ts_corr， ts_regression，看到博主分享的回测结果，我觉得有必要尝试一下这些组合
============================================================================================

---

### 评论 #7 (作者: FF65210, 时间: 23天前)

感谢大佬分享，这个模板我一直也在用，非常好用，每次都能出一些，祝大佬早日vf1.0.

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

### 评论 #8 (作者: 顾问 RM49262 (Rank 30), 时间: 23天前)

=====================================评论区====================================

感谢大佬分享如此优质的模板

这么强的帖子值得一个赞

=============================================================================

---

### 评论 #9 (作者: KD86036, 时间: 23天前)

很不错的idea,跟我之前的模板ts_corr(news18_martrix,price_field,d)经济学意义有点类似，我一直反复思考如何拓展该模板，MY82844大佬你给了我指明了方向，可以使用带_nip后缀的数据集进行拓展，形成更丰富的新闻量价数据相关性模板，十分感谢。

---

### 评论 #10 (作者: SL35215, 时间: 22天前)

感谢分享：sentiment 上验证过的「相关性算子 + FAST neutralization」搬到 news，再利用 nip 字段，研究思路很有参考价值。期待大佬更多分享。

=============================================================================

The only thing we have to fear is fear itself — nameless, unreasoning, unjustified terror which paralyzes needed efforts to convert retreat into advance.

=============================================================================

---

### 评论 #11 (作者: YQ84572, 时间: 22天前)

学到了，又是一个点塔的小妙招，不过这种因子会不会太依赖与return这个信号了，retrun这个因子加入噪音的话确实是能处理出很多ra的。对于这点还是很疑惑的。
==================================================================================

感谢大佬的分享，祝大佬vf0.99，base多多

==================================================================================

---

### 评论 #12 (作者: SY90356, 时间: 20天前)

请问是用FAST中性化进行回测吗?目前正值USA PPA可提交阶段，我发现theme数据集中有很多news数据，不知道您的这个方法在USA地区是否依旧表现出色。

------------------------------------------------------------------------------------------

回测是历史的答案，实盘是未来的考题。

------------------------------------------------------------------------------------------

---

### 评论 #13 (作者: MY82844, 时间: 19天前)

[HZ99685](/hc/en-us/profiles/32603557750935-HZ99685)  确实，不过一般在news和sentiment不会逗留很久，每个季度点塔做个2-3个差不多，应该对pv影响不会很大

---

### 评论 #14 (作者: MY82844, 时间: 16天前)

[SY90356](/hc/en-us/profiles/27705939991959-SY90356)  是的，适用FAST，USA也有不少类似的字段，不过出货率感觉没有EUR高，还需要后期再加工下看看

---

