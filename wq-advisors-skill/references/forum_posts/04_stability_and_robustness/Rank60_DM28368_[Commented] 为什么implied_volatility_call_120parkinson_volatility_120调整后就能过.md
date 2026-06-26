# 为什么implied_volatility_call_120/parkinson_volatility_120调整后就能过？

- **链接**: [Commented] 为什么implied_volatility_call_120parkinson_volatility_120调整后就能过.md
- **作者**: YZ84314
- **发布时间/热度**: 1年前, 得票: 13

## 帖子正文

作为初学者，我按照document里面的19-alpha-examples第一个例子进行实验：

```
implied_volatility_call_120/parkinson_volatility_120
```

但是并未成功，看例子的提升思路：“transformational operators on the expression improve performance”，于是查operator页面，看到transformational operators有trade_when函数，于是写成如下：

```
trade_when(volume < adv20,  implied_volatility_call_120/parkinson_volatility_120, -1)
```

trade_when的条件我是在论坛里面随便抄的，但是为什么我能成功，我一点头绪也没有。有没有人能帮忙分析下呢？

---

## 讨论与评论 (15)

### 评论 #1 (作者: KJ42842, 时间: 1年前)

trade_when 让你的alpha在 volume < adv20 的交易日才开仓，因此提高了alpha的表现。

---

### 评论 #2 (作者: AK76468, 时间: 1年前)

同问

---

### 评论 #3 (作者: KX44437, 时间: 1年前)

settings有改吗，我想复现的看一下

---

### 评论 #4 (作者: YZ84314, 时间: 1年前)

[KX44437](/hc/en-us/profiles/29027336152983-KX44437) ，不知道对你有没有用，我还没签约，这个应该只会在签约前的这个阶段才能跑通吧。


> [!NOTE] [图片 OCR 识别内容]
> Code
> trade
> Wihen
> IOlume
> ad420,
> implied
> IOlatility
> Call
> 128  parkinson_
> 401
> atility_128,
> Simulation Settin m
> Instrument TyPe
> Region
> Uniyerse
> LaNwage
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handlin
> Unit Handlin
> Equit
> 05k
> TOPIIo
> Fast E:pression
> Subindustry
> Herify


---

### 评论 #5 (作者: DX46889, 时间: 1年前)

我的理解是这样的，通过trade_when设置开平仓的条件控制了alpha的交易频率，从而能达到优化策略的目的。在这个例子中，volume < adv20表示市场的成交量低于过去20天的平均成交量，implied_volatility_call_120 / parkinson_volatility_120表示隐含波动率与历史波动率的比值。

从您的表述中，我认为可能是由于volume < adv20交易条件的引入，减少了市场处于高波动、高成交时的交易频率。在高成交量的情况下，市场活跃，价格波动可能会更加剧烈，波动率相应的也可能较大，此时隐含波动率可能过高从而增加了implied_volatility_call_120 / parkinson_volatility_120的噪音。因此只在低成交量时触发交易，减少了过度交易的可能性，提高了信号的稳定性。

但是实际上我按照您的setting设置并进行了回测，并没有达到上述的效果，只是降低了换手率，以下是我的回测结果。

implied_volatility_call_120 / parkinson_volatility_120


> [!NOTE] [图片 OCR 识别内容]
> Streak: 53 day
> Pnl
> Risk Neuralized Pnl
> implied_volatility_call
> 120
> parkinson_volatility_Iz8
> IS Summary
> Period
> K Single Data Set Alpha
> Aggregate Data
> SI3TO
>  UTMCVET
> CIIES
> RetUTnis
> UF3MOOWn
> Marein
> 1.44
> 30.5596
> 0.77
> 8.71%
> 11.82%
> 5.709600
> Year
> TUIIOVeT
> Ftness
> Returs
> Drawdown
> Margin
> Count
> Short Cownt
> 2012
> 257
> 30.67光
> 10.13光
> 1.19*
> 6.51922
> 335
> 2013
> 0.72
> 25-3
> 9
> 241
> 39*
> 329323
> 413
> 153
> 2011
> 143
> 31.81兆
> .10
> 62光
> 40光
> 029
> -29
> -73
> 2015
> 209
> 36.41光
> 0.35
> 69光
> 259*
> 239
> 2015
> 0.5
> 31.531
> 17
> 2.71
> 3.335
> 719323
> 449
> 132
> 2017
> 27.77北
> 494*
> 237*
> 559
> 145
> 135
> 2013
> 28.21兆
> 95光
> 56光
> 309
> -56
> 135
> 2019
> 2501
> 56*
> 231沁
> 909323
> 135
> 2020
> 34.15光
> 3.17
> 25.13d
> 2.23*
> 15.339
> 145
> 131
> 2021
> 27.50沁
> 1.43
> 21.705
> 11.32
> 15.7392
> +50
> 475
> 2022
> 0.5-
> 36.37光
> 0.25
> 541*
> S.5
> 939323
> -4
> -72
> Sharpe
> Long


trade_when(volume < adv20,  implied_volatility_call_120/parkinson_volatility_120, -1)


> [!NOTE] [图片 OCR 识别内容]
> Streak: 53 day
> IJ VUIIITOI )
> trade_when(lvolume
> advz8,
> implied
> volatility_call_Izo/parkinson_volatility_120,
> Aggregate Data
> Sharpe
> TUITNUE
> Fitnec
> 3STICn
> Ca
> Marein
> 1.30
> 25.31%
> 0.73
> 8.0896
> 11.4896
> 6.389600
> Year
> Sharpe
> TurnOVeT
> Ftness
> Returs
> Orawdown
> Marqin
> LoNg Count
> Short Count
> 2012
> 53
> 25.546
> 1.73
> 10.66沁
> 1.23*
> 3592
> 33
> -32
> 2013
> -0.25
> 22.23*
> 0.87*
> 90兆
> 739
> 110
> 201-
> 0.5J
> 25.135
> 0.19
> 2.51沁
> 3.05
> 07932
> 427
> 2015
> 29.91
> 1
> 5.14*
> 3.16*
> 0933
> 452
> 2015
> 032
> 26.03*
> 0.36
> 497*
> 3.30光
> 3.31923
> 145
> -33
> 2017
> 22.12沁
> 5.5-
> 2.10*
> 279323
> 14+
> +35
> 2013
> 0.3-
> 23.67光
> 0.3
> 333*
> 304*
> 32932
> 456
> -35
> 2019
> 2433沁
> 7.51*
> 2.81*
> -9
> -33
> 2020
> 2903*
> 3.43
> 25411
> 2.52*
> 993
> -45
> -33
> 2021
> 1.53
> 22.59*
> 21.12*
> 11-3*
> 15.629522
> 159
> 2022
> 0.20
> 30.39*
> -1.75兆
> 23北
> 59
> -55
> -75


---

### 评论 #6 (作者: KX44437, 时间: 1年前)

这样子呀，谢谢哦

---

### 评论 #7 (作者: SC38173, 时间: 1年前)

为什么我按照你说的调整了也过不了呢
 
> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1/TOP1000
> trade_whenlvolumecadvz0 , implied_volatility_call_120/
> N
> parkinson_volatility_120,-巩
> 5 PASS
> 2 FAIL
> Sharpe Of 1.60 is below cutOff Of 2。
> Fitness of 1.03 is below cutoff of 1.30
> PENDING


---

### 评论 #8 (作者: CT98586, 时间: 1年前)

SC38173

你的delay设置为0，delay为0和delay为1的时候对于最终alpha的sharpe和fitness要求会更高，我对此的理解是使用delay为1的情况下进行测算是基于历史信息的，而使用delay为0的情况则是使用了当天信息的，会有一点拿结果找过程的意味在其中，但并不是完全否定这种思路，只是这样会有更多的信息所有对于你找到的alpha有更高的要求才算过关才可能在实际中更有用,我还没有签约，以上内容仅个人思考，供你参考

---

### 评论 #9 (作者: 顾问 SZ83096 (Rank 13), 时间: 1年前)

SC38173

这个应该是用户阶段才能通过的吧，我试了下，用户阶段是可以的


> [!NOTE] [图片 OCR 识别内容]
> C|731
> (
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 7 PASS
> REGION
> UNIVERSE
> DELAY
> Sharpe of 1.54is above cutoff of 1.25.
> Fitness of 1.06 is above cutoff of1.
> USA
> TOP1000
> Turnoverof 25.079 is above cUtoff of 1% _
> Turnover of 25.0796 is below cutoff of 70%.
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Weight is well distributed over instruments。
> Sub-universe Sharpe Of 1.42 is above cUtoff Of 0.82.
> Subindustry
> 0.08
> Competition Challenge matches。
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> FAIL
> On
> Verify
> On
> YEARS
> MONTHS
> Self-correlation 0.8604 is above cUtoff of 0.7
> Sharpe not better by 10
> Saveas Default
> Apply
> Performance Comparison
> trade_When (Volume
> advzo,
> implied_Volatility_call_128/
> parkinson_volatility_120=
> -1)
> 3
> Chart
> Pnl
> Clone this Alphain a newtab
> and


---

### 评论 #10 (作者: 顾问 DM28368 (Rank 60), 时间: 1年前)

wow this is exactly the post I was looking for. Operator trade_when used to change Alpha value only in a specified condition and keep Alpha value in other cases. It also allows closing Alpha positions (assigning NaN value) in a specified condition. I was using trade_when($data, $data, $data) way which didn't work, good to see this post.

---

### 评论 #11 (作者: AB60254, 时间: 1年前)

有人可以发送一下  **19-alpha-examples**  文档的链接吗？

---

### 评论 #12 (作者: SG46247, 时间: 10个月前)

=================================================================================

=================================================================================

trade_when(volume < adv20,  implied_volatility_call_120/parkinson_volatility_120, -1)中 退出条件是一直持有，进场条件是当天交易量小于过去20天的平均交易量，挑选出交易量比较过去小的股票进行投资，获得更高收益

=================================================================================

=================================================================================

---

### 评论 #13 (作者: CC85858, 时间: 9个月前)

AB60254                                                                                                                                                                文档好像是在微信公众号里找到的

---

### 评论 #14 (作者: EO24865, 时间: 8个月前)

Great

---

### 评论 #15 (作者: MM27120, 时间: 5个月前)

本人现在跑ind区域，出现好多这个robus<1的问题，指标都很好，sharpe>2 fitness>1的，就是找不到解决方法

---------------------------------天无绝人之路----------------------------------------------------

今天刷帖子终于找到该问题的解决方法，虽然还没有尝试，但是总算是有一种解决思路了

-----------------------------------感谢老铁的分享----------------------------

---

