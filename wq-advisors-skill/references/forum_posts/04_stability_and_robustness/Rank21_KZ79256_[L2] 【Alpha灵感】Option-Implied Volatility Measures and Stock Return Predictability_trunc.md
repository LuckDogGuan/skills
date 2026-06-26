# 【Alpha灵感】Option-Implied Volatility Measures and Stock Return Predictability

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Option-Implied Volatility Measures and Stock Return Predictability_21110734836887.md
- **作者**: YW27566
- **发布时间/热度**: 2 years ago, 得票: 5

## 帖子正文

论文题目：Option-Implied Volatility Measures and Stock Return Predictability
by X Fu, YE Arisoy, MB Shackleton, M Umutlu - academia.edu

论文概述：文中作者通过构建三大类衡量波动率价差构建的思路来构建交易策略,这三大类包括了call和put波动率价差, OTM call/put和ATM call/put隐含波动率价差以及隐波和实波价差。作者后续基于这三大类价差，又构建了六种不同的价差计算方式：
（1）IVatm,call-IVatm,put

（2）IVotm,put-IVatm,call

（3）[(IVitm,put+IVotm,call)-(IVitm,call+IVotm,put)]/2

（4）IVotm,call-IVatm,call

（5）IVotm,put-IVatm,put

（6）RV-IVatm

最后作者根据价差高低进行排序构建多空交易策略

数据集：Volatility Data，Implied Volatility and Pricing for Equity Options

其中包含了很多不同的volatility和implied volatility的类型可供选择，如opt4_273_put_vola_delta30，表示虚值0.3期限为273的put

根据论文中作者提供的spread构建思路对这些符合条件的数据遍历，并对alpha进行cap，volume中性化处理，可以得到符合提交要求的alpha


> [!NOTE] [图片 OCR 识别内容]
> 15M
> 12.5M
> 1OM
> 7,50OK
> 5,0OOK
> 05/14/2014
> IS Pnl: 4,605.85K
> 2,5OOK
> 2014
> 2016
> 2018
> 2020
> 2022



> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.3636.72%1.6317.589610.4899.579600



> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Highest Correlation
> Last Run: Sun, 02/04/2024,11:33 PM
> 0.6
> 1OOM
> TM
> -0.2.-0.1
> 鬓
> Alphas: 19 895
> 1Ok
> 昱
> 皂
> 100
> 01
> 0@0?
> 09
> 0?
> ~
> 0.
> O'
> 0
> ~0.8
> 0.6
> 0.5
> ~0.4
> 0.2.
> -0.7.


---

## 讨论与评论 (2)

### 评论 #1 (作者: YW93864, 时间: 2 years ago)

hello，该alpha我尝试做过类似的，也尝试过做一些变换，但是后续发现很多时候prod_corr较高，请问您是否做了一些特殊的处理降低corr，是否可以分享或指导，感谢！

我尝试了将volume中性化换成其他model data的中性化，发现有可提交的alpha，很好奇您是怎么做的

[YW27566](/hc/en-us/profiles/18162425397783-YW27566)

---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

[YW93864](/hc/en-us/profiles/14096946892439-YW93864)

实现的方法可以参考该朋友在 [[Commented] 英才候选人计划实训考核Case2_总第三期_19992945218711.md?page=2#comments]([Commented] 英才候选人计划实训考核Case2_总第三期_19992945218711.md?page=2#comments)

的评论。

---

