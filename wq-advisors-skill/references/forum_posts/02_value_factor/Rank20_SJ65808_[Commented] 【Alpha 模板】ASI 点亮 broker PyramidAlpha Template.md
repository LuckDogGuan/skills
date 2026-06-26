# 【Alpha 模板】ASI 点亮 broker PyramidAlpha Template

- **链接**: [Commented] 【Alpha 模板】ASI 点亮 broker PyramidAlpha Template.md
- **作者**: LH94963
- **发布时间/热度**: 9个月前, 得票: 94

## 帖子正文

## Alpha Template

Alpha模版之信念熵值幂放大（行为金融预测质量）：用信息熵量化预测不确定性，幂函数放大强信号

```
signed_power(ts_entropy({field}, 144), 0.618)

```

## 一、构造逻辑（公式拆解）

**分子：ts_entropy({field}, 144)**  → 过去 144 天的信念强度信息熵  **外层：signed_power(x, 0.618)**  → 黄金比例幂次变换

**分子** ：这只股票过去 144 天里，Minkabu用户预测的信念强度有多"随机"。  **外层** ：对信息熵进行非线性幂变换，放大强信号、压制弱信号。

**因子** ："信念不确定性 ^ 0.618" = 保持符号的非线性强化，即经过黄金比例调优的预测质量信号。

## 二、金融直觉（经济学含义）

**低值** ：信念强度变化规律性强，预测行为稳定 ⇒ 群体意见相对一致，信号较弱。  **高值** ：信念强度高度随机波动，预测行为不稳定 ⇒ 市场分歧巨大，蕴含强烈信号。

**本质** ：基于信息论的思想，把"预测行为的随机性"当成不确定性度量，把"非线性幂变换"当成信号增强器，追求行为金融学中的预测质量评估。

## 三、使用场景（交易层面）

**行为分歧策略** ：因子极端高 → 做多；极端低 → 做空，配合 行业/规模中性化 降低系统性风险。

**预测质量过滤** ：在对其他broker因子打分前，先剔除信念熵值过低的股票，避免"低分歧陷阱"。

**组合加权** ：把该因子作为 预测质量调节系数，与其他 alpha 因子相乘，提升信息比率。

## 四、应用举例

二阶组合 ts 操作符

ts_mean(-signed_power(ts_entropy(vec_sum(brk1_conviction_flag), 144), 0.618), 120)


> [!NOTE] [图片 OCR 识别内容]
> ts_mean (-signed
> power(ts
> entropy
> VeC
> SUN
> brkl
> COnV
> Iiction_flag)
> 144)
> 0.618)
> 120
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 1.45
> 4.879
> 0.82
> 3.959
> 3.339
> 16.20%o。
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handlin
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Statistical
> On
> On
> Verify
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 88
> 5.78%
> 0.45
> 3.31%
> 3.339
> 11.4790。
> 1570
> 1152
> 2014
> 1.61
> 4.859
> 93
> 4.21%
> 0.999
> 17.3490。
> 1844
> 1302
> 2015
> 2.55
> 4.990
> 2.06
> 8.129
> 1.439
> 32.52%。
> 1953
> 1346
> Clone Alpha
> 2016
> .80
> 4.939
> 1.24
> 5.989
> 2.609
> 24.28%o。
> 1937
> 1230
> 2017
> 2.20
> 4.719
> 1.46
> 5.509
> 1.459
> 23.36%o。
> 1947
> 1296
> 2018
> 1.73
> 4.26%
> .01
> 4.29%
> 1.5096
> 20.
> 296oo
> 2171
> 1575
> Chart
> Pnl
> 2019
> 1.91
> 4.339
> 1.14
> 4.459
> 1.01%
> 20.5996oo
> 1995
> 1373
> 2020
> -0.25
> 5.229
> 0.06
> 0.629
> 2.689
> 2.38900
> 1969
> 1580
> 2021
> 0.60
> 4.759
> 0.19
> 1.269
> 1.1796
> 5.31%。
> 2415
> 2079
> 3,00OK
> 2022
> .02
> 4.4396
> 0.41
> 2.049
> 1.2796
> 9.21%。
> 2217
> 1960
> 2023
> 5.16
> 14.189
> 4.96
> 13.0896
> 0.339
> 18.45%o。
> 1898
> 1733
> 2,00OK
> 1,OOOK
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
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
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run: Wed, 09/17/2025,10:18 AM
> o
> IS Testing Status
> Period
> IS
> 0S
> 0.2752
> -0.3570


虽然 returns 不是很高，但是 ASI broker category 目前交的人很少，所以 prod correlation 都很低。

---

## 讨论与评论 (23)

### 评论 #1 (作者: QW20325, 时间: 9个月前)

谢谢分享

---

### 评论 #2 (作者: CW49566, 时间: 9个月前)

这个模板解析说明很清晰，小白也能理解。再用代码封装替换字段就可以批量跑了。赞👍🏻

---

### 评论 #3 (作者: DS48533, 时间: 9个月前)

学到了黄金比例 **signed_power(x, 0.618)**  ，你这个PC真的太低了，希望我之后也能挖到这么低的高质量alpha

---

### 评论 #4 (作者: DA98440, 时间: 9个月前)

很有意思的一个策略，学习到了

---

### 评论 #5 (作者: SX13432, 时间: 9个月前)

正在ASI区劳动，非常及时，给大佬点赞！

---

### 评论 #6 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

谢谢您的分享。我才发现竟然没有ts_entropy这个运算符。虽然不太明白0.618黄金比例幂次变化的效果怎么样，但是思路很新颖。决定下次用0.618与1，2幂次变换比较以下，看看哪个效果更好。

---

### 评论 #7 (作者: QZ28759, 时间: 9个月前)

这个0.618用得妙啊，基于此还可以试试一些数学上有意义的数字，如：2.7828

---

### 评论 #8 (作者: GY56717, 时间: 9个月前)

不知道是不是等级不够， 没有ts_entropy，哈哈哈，先mark，以后有机会试试

---

### 评论 #9 (作者: SQ89646, 时间: 9个月前)

谢谢大佬，ASI区我挖了三天没有产出，可能是国家间差异信号较大，今天尝试一下这个思路处理

---

### 评论 #10 (作者: LR93609, 时间: 9个月前)

感谢分享，不错的策略

我有几个疑问：

1. 信念熵值是否应该是信号熵值？

```
Alpha模版之信念熵值幂放大（行为金融预测质量）：用信息熵量化预测不确定性，幂函数放大强信号
```

这里反复提及的 **信念熵值**  是不是笔误？比如说  **信号熵值**

2. 黄金比例幂变换是否有出处？我头一次听说有这个东东，请帮忙补充解释

```
signed_power(x, 0.618) → 黄金比例幂次变换
```

我理解，这里只是保留符号并进行幂次压缩，且0.618是经验值并非理论值或者理论支撑

3. 为何是放大强信号、压制弱信号呢？明明是压缩极端值、增强小信号敏感性，提升因子质量

```
外层：对信息熵进行非线性幂变换，放大强信号、压制弱信号。
```

结论与实际刚好相反

再次感谢分享，请帮忙回复。

-------------------------------------------------------------------------------------------------------------------------

凡事发生，皆利于我；愿我所愿，尽是美好

-------------------------------------------------------------------------------------------------------------------------

---

### 评论 #11 (作者: MY82844, 时间: 9个月前)

0.618回测结果比0.5和1显著好么？

---

### 评论 #12 (作者: AH18340, 时间: 9个月前)

感觉这个二阶这个有点厂了

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #13 (作者: AM12075, 时间: 9个月前)

运用黄金比例的具体想法是什么呢，是为了降低pc吗？ 0.618 虽然能放大极端信号，但对异常值敏感，可能放大噪声而非有效信号，有没有尝试2以上的数值呢？二阶组合如 ts_mean 进一步平滑，可能会弱化原因子的波动特性，导致信号衰减。信息熵计算依赖过去144天的数据，可能对短期市场突发事件反应迟缓，滞后性较强，可以尝试不同的窗口期，也许会有更好的表现。

---

### 评论 #14 (作者: DT40395, 时间: 9个月前)

黄金比例幂次变换是什么东西呢？可有什么渊源吗？大佬太厉害了！

---

### 评论 #15 (作者: 顾问 SJ65808 (Rank 20), 时间: 9个月前)

哇，表达式里面的参数真是不常见，对比一般的参数不知道效果是否有明显改善~~

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #16 (作者: MY49971, 时间: 8个月前)

看pnl曲线多少有点厂的感觉，而且0.618和144这些参数多少有点膈应，不知道是不是有点过拟合

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #17 (作者: TB73554, 时间: 8个月前)

大佬的观点很新颖，昨天第一次尝试手搓，有点头疼，根据大佬的模版手搓出来的二阶段因子有厂，请问这个应该怎么解决？

---

### 评论 #18 (作者: MY82844, 时间: 8个月前)

赞， 很有启发，另外看了下，这个data description是不是对映混乱了...


> [!NOTE] [图片 OCR 识别内容]
> Field
> Description
> Type
> brkl
> active
> Prediction/Stock Price Statls
> Vector
> brkl
> SelI
> flag
> for
> Orsell prediction (BUY Or SELL)
> Vector
> brkl
> Conviction
> Rationale
> underlying prediction
> Vector
> brkl
> end_stock_price
> Stock price at the time of prediction started
> Vector
> brkl_number_of_comments
> Stock price at the time of prediction closed
> Vector
> brkl_prediction_horizon
> price
> Vector
> brkl_prediction
> 「e3501
> Prediction status flag [true (active prediction), False
> Vector
> (terminated prediction)]
> brkl_prediction_status
> Investment Horizon associated with prediction
> Vector
> brkl
> Dredictionswqreceivetime
> This field represents the User's conviction in their forecast. For
> Vector
> example; 讦
> user sets the conviction flag in their forecastand
> they also specify that -
> are
> seller via the
> Sell-flag;'
> they are indicating that they are strongly convicted to their se。
> brkl
> start_stock_price
> Time
> prediction started (in UTC time zone)
> Vector
> DrkT_start_time
> Itis WQ receive time
> Vector
> brkl_target_price
> Number of comments for this prediction
> Vector
> Flag
> bUy
> buy
> fln
> Target
> they
> 'buy-


---

### 评论 #19 (作者: SZ20589, 时间: 8个月前)

感谢大佬分享，这里的黄金分割点0.618是怎么来的呢？可以随便设置一个小数吗？

大佬的实践和创新精神真是惊为天人，有这种创新和实践精神，不管大佬干什么行业，大佬都会是业界翘楚，行业标杆。祝愿大佬早日GM， VF经久1.0。

再次感谢大佬

=============================================================================

========Genius is one percent inspiration and ninety-nine percent perspiration.=============

==============================================================================

---

### 评论 #20 (作者: JL52079, 时间: 8个月前)

谢谢大佬分享，很有用

---

### 评论 #21 (作者: YY31580, 时间: 6个月前)

试了一下，感觉还不错。感谢分享

---

### 评论 #22 (作者: LJ12230, 时间: 3个月前)

感谢大佬分享！

---

### 评论 #23 (作者: CY76111, 时间: 3个月前)

谢谢分享

---

