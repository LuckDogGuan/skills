# 【Alpha灵感】Individual Option Volatility Smirk

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Individual Option Volatility Smirk_25824706455703.md
- **作者**: JY72168
- **发布时间/热度**: 1 year ago, 得票: 21

## 帖子正文

论文题目：What Does Individual Option Volatility Smirk Tell Us about Future Equity Returns?

**Alpha 核心思路**

这篇论文研究了波动率微笑（volatility smirk）的预测能力,即远价看跌期权和平价看涨期权的隐含波动率之差,对未来股票收益的影响。作者发现,在其交易期权中具有最陡峭波动率微笑的股票,相比具有最不明显波动率微笑的股票,风险调整后的年化收益率低约10.9%。这种可预测性至少持续6个月,且具有最陡峭波动率微笑的公司在下一季度经历最严重的盈利冲击。结果表明,波动率微笑中包含的信息与公司基本面有关,而股票市场在吸收这些信息方面反应缓慢。

原文中公式为：


> [!NOTE] [图片 OCR 识别内容]
> SREI,
> TOL 
> VOLAIK'


**Alpha setting**

文中样本数据来自1996年至2005年的CRSP和Compustat的股票数据,以及OptionMetrics的期权数据，且文中提及股票市场流动性较低,SKEW的可预测性更强,故选择USA TOP3000,Neut文中并未明确提及，尝试后选择Fast

**
> [!NOTE] [图片 OCR 识别内容]
> UNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Fast Factors
> 0.1
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDUING
> TEST PERIOD
> On
> Verify
> On
> YEARS
> MONTHS
> Save as Default
> Apply
**

最初直接尝试

```
implied_volatility_call_10-implied_volatility_put_10
```


> [!NOTE] [图片 OCR 识别内容]
> 60OOK
> SOOOK
> 40OOK
> 30OOK
> 2,0OOK
> OOOK
> 02/13/2012
> Pnl。 305.02k
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
> IS Summary
> Needs Improvement
> Period
> 1S
> O5
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawoown
> MarEin
> 1.14
> 120.669
> 0.28
> 7.1696
> 20.28%
> 1.199600


考虑到该字段的覆盖率问题，对数据进行处理


> [!NOTE] [图片 OCR 识别内容]
> 3,50OK
> 30OOK
> 25OOK
> ZOOOK
> 1,50OK
> 0OOK
> SOOK
> 06/27/2012
> DnL  157.0S
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
> IS Summary
> Needs Improvement
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrhs
> Drawdown
> Margin
> 1.85
> 103.019
> 0.37
> 4.069
> 2.7496
> 0.799600


已经可以看到明显信号但是turnover仍然过高，最后看到文章末尾的图表想到使用ts_kurtosis计算skew的峰度值


> [!NOTE] [图片 OCR 识别内容]
> 0.18
> 0.14
> 0.12
> [OG
> [L0
> 0.02
> 0.02
> 12
> lowcst skcw
> highcst skCw


使用ts_kurtosis计算skew的峰度值


> [!NOTE] [图片 OCR 识别内容]
> 1ON
> 80OOK
> OOOK
> 09/29/2015
> Pnl: 5,064.39k
> 40OOK
> OOOK
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
> o IS Summary
> Average
> Period
> 15
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> 1.73
> 17.519
> 1.44
> 12.159
> 11.049
> 13.889600


alpha表现有明显提升

**增强Alpha的信号**

文章还提到成交量加权的波动率偏度，故采用volume分组中性化


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> MarEin
> 1.92
> 25.679
> 1.37
> 13.019
> 10.389
> 10.149600


Sharpe和returns均有少量提升

**可提交的版本**

```
skew  = (rank(winsorize(ts_backfill(implied_volatility_call_10,5)-ts_backfill(implied_volatility_put_10,5),std = 4)));alpha = -ts_kurtosis(skew,120);group_neutralize(alpha,bucket(rank(volume),range = "0,1,0.1"))
```

**
> [!NOTE] [图片 OCR 识别内容]
> 1ON
> 7,SOOK
> SOOOK
> 2SOOK
> 01/26/2012
> Dn: 112.04k
> Jan '13
> Jan'14
> Jan '15
> Jan '16
> Jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> o IS Summary
> Average
> Period
> 15
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> RetUrns
> Drawgown
> Margin
> 1.92
> 25.679
> 1.37
> 13.019
> 10.389
> 10.149600
**

**
> [!NOTE] [图片 OCR 识别内容]
> MaXIMUM
> Minimun
> 0.5583
> -0.3846
**

**Alpha模板**

```
skew  = (rank(winsorize(ts_backfill(implied_volatility_call_10,5)-ts_backfill(implied_volatility_put_10,5),std = 4)));alpha = -ts_kurtosis(skew,120);{group_operator}(alpha,{group})
```

模板生成的alpha基本都达到提交标准，但相关性都过高

**探索该Alpha遇到的困难与踩过的坑**

一直不太会处理由数据覆盖率引起的weight concentrate问题，ts_backfill的参数很难调整，经常让alpha的表现变差

---

## 讨论与评论 (4)

### 评论 #1 (作者: WL13229, 时间: 1 year ago)

1. ts_kurtosis计算skew的峰度值 这个步骤很精彩！

2. 这个模板如果只是换group operator还有group的话，确实是很难找到新的Alpha的，建议把数据也进行替换。

3. 为了表达“即远价看跌期权和平价看涨期权的隐含波动率之差,对未来股票收益的影响。”，使用

```
implied_volatility_call_10-implied_volatility_put_10
```

似乎并不好，并不能合理表达原文含义。

4. weight concentrate 的问题，可以尝试使用ts_decay_linear在最后的信号去尝试填充和平滑。

---

### 评论 #2 (作者: AA53991, 时间: 1 year ago)

weight concentrate 是什么意思

---

### 评论 #3 (作者: MY82844, 时间: 9 months ago)

公式里面是OTM put - ATM call，使用的字段不准确吧

---

### 评论 #4 (作者: DL74068, 时间: 8 months ago)

user阶段目前没有找到OTM put数据，可能consultant阶段才会解锁OTM数据？

---

