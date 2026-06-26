# 【Alpha灵感】Liquidity Shocks and Stock Market Reactions

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Liquidity Shocks and Stock Market Reactions_25740783868439.md
- **作者**: ZL29184
- **发布时间/热度**: 1 year ago, 得票: 17

## 帖子正文

论文题目：Liquidity Shocks and Stock Market Reactions

**Alpha 核心思路**

研究发现股票市场对流动性冲击的反应不足： **流动性冲击不仅与同期回报正相关** ，而且还能预测未来长达六个月的回报持续性。通过构建基于流动性冲击的多空投资组合，可以产生每月0.70%到1.20%的显著回报，这些回报在不同的流动性冲击度量标准下以及控制风险因素和股票特征后依然稳健。

流动性冲击的度量方法：Amihud的流动性度量指标与其过去12个月平均值之间的负差值。

Amihud的流动性度量指标：Amihud指标通过资产的日收益率与日成交额的比值来反映资产的流动性，即资产在单位收益率下的成交量。

**主信号：流动性冲击与同期回报正相关，不过实际在brain平台的回测显示这是个反转因子。**

**Alpha setting**

这项研究关注的是美国股票市场。研究样本包括了从1963年7月至2010年12月期间在纽约证券交易所(NYSE)、美国证券交易所(Amex)和纳斯达克(Nasdaq)上市的所有普通股。

故初步设为USA region。

Top 3000 universe

Neut初步为market，但是表现并不好。根据高的turnover，换成fast + slow factors，效果也不佳，换为slow factors后，达到提交标准（不考虑product corr的情况下）但由于corr过高无法提交。


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> T0P3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Slow Factors
> 10
> 008
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDUING
> TEST PERIOD
> On
> Verify
> Off
> VEARS
> MONTHS
> Save as Default
> Apply


故考虑转移到其他region，转移到GLB region后，达到了提交标准，且corr小于0.65。


> [!NOTE] [图片 OCR 识别内容]
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> GLB
> MINVOLIM
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 10
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save a5 Default
> Apply


**Alpha performance**

USA region:


> [!NOTE] [图片 OCR 识别内容]
> o
> IS Summary
> Average
> Period
> IS
> O
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.49
> 59.849
> 1.16
> 12.989
> 6.099
> 4.349600



> [!NOTE] [图片 OCR 识别内容]
> Prod
> Maximum
> Minimum
> Last RUn; MOn
> Correlation
> 03/19/2024.2:35 PM
> 0.9202
> -0.7715
> TN
> 1Ok
> 訾
> 晷
> 2
> 100


GLB region：


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Average
> Period
> IS
> O
> Aggregate Data
> Sharpe
> TUrnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 2.81
> 42.129
> 1.38
> 10.209
> 3.81%
> 4.849600



> [!NOTE] [图片 OCR 识别内容]
> Prod
> Maximum
> Minimum
> Last Run; Mon
> Correlation
> 08/19/2024.2;05 DN
> 0.6120
> -0.4848
> 1OOk
> 1Ok
> Ik
> 訾
> 100
> 晷
> 2
> 10
> 01


**增强Alpha的信号，以及其他不同的探索与尝试**

增强Alpha的信号

研究还发现，这种正相关关系在非危机期间、经济衰退期和扩张期同样显著，这表明市场对流动性冲击的反应不足并不是由特定的宏观经济环境造成的。此外，研究排除了流动性冲击自身具有正向自相关性作为解释这一现象的原因，因为在有效市场中，如果市场能够理性且即时地对流动性冲击作出反应，则未来的回报不应该具有可预测性。即市场反应不足是alpha信号的主要来源，并且有多个成因导致了市场反应不足。这是我们做增强信号的起点。

研究中提到的两个可能解释市场反应不足的原因是有限的投资者注意力和流动性问题本身。

投资者注意力不集中可以通过多种方式来衡量。

1. **股票规模**  (LNME): 股票的市值大小往往与投资者的关注度相关。一般而言，大规模股票比小规模股票更能吸引投资者的注意力。
2. **分析师覆盖度**  (CVRG): 分析师覆盖度是指跟踪一只股票的分析师数量，通常用分析师人数的自然对数表示。更多的分析师覆盖意味着更高的关注度。
3. **机构持股比例**  (INST): 机构投资者通常会对他们持有的股票给予更多关注，因此机构持股比例可以作为衡量注意力的一个指标。

利用市值作为增强。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Average
> Period
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marein
> 3.04
> 42.889
> 1.49
> 10.249
> 4.0296
> 4.789600



> [!NOTE] [图片 OCR 识别内容]
> l
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Prod
> MaximUm
> Minimum
> LaStRUn; MOn
> Correlation
> 08/19/2024,2:47 PM
> 0.5828
> -0.4810


可以看到Sharpe值和fitness都增强了不少，returns稍微增大，drawdown增加较大。

其他两个暂未找到好的数据字段。

其他不同的探索与尝试

换group

利用pv13的group进行替换，有八个达到提交标准的（未考虑corr）。


> [!NOTE] [图片 OCR 识别内容]
> Regular
> USUUITTLC
> 03/19/2024 EDT
> GLB
> NINVOLII
> 1024
> 42.369
> 1.49
> Regular
> USUBLIITTEC
> 08119/2024 EDT
> GLB
> IIOLTI
> 2.81
> 10.20
> 92.12
> Regular
> USUBLIITTEC
> 03/19/202 EDT
> GLB
> IINVOLII
> 259
> 12.374
> 63.565
> 1.10
> ReRular
> VISIOITTF
> 08/19/2024 EDT
> GLB
> MINVOLIII
> 291
> 13.67.
> 63,37
> RegUlr
> UCILPNITTFI
> 08/19/202EDT
> GLG
> MINVOLII
> 258
> 13,65
> 6,73
> Repulai
> USURIIITTCC
> 08/19/2024 EDT
> GLB
> WINVOLT
> 2.80
> 13.22
> 63,32
> 1,23
> RegUlT
> USUULITTLC
> 08/19/2024 EDT
> GLG
> WINOLT'
> 2.60
> 12,64*
> 63,550
> 1,12
> Regular
> USURLIITTTI
> 09/19/2025 EDT
> GL
> IINOLII
> 254
> 12.91*
> 68.505
> 1.10


Operator

Quantile rank zscore normalize 都能达到提交标准（未考虑corr）。

**可提交的版本**


> [!NOTE] [图片 OCR 识别内容]
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> GLB
> MINVOLIM
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 10
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save a5 Default
> Apply



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Average
> Period
> IS
> O
> Aggregate Data
> Sharpe
> TUrnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 2.81
> 42.129
> 1.38
> 10.209
> 3.81%
> 4.849600



> [!NOTE] [图片 OCR 识别内容]
> Prod
> Maximum
> Minimum
> Last Run; Mon
> Correlation
> 08/19/2024.2;05 DN
> 0.6120
> -0.4848
> 1OOk
> 1Ok
> Ik
> 訾
> 100
> 晷
> 2
> 10
> 01


```
Amihud_liquid_index = returns/volume;liquid_index = -(Amihud_liquid_index-ts_mean(Amihud_liquid_index,252));a = group_neutralize(quantile(-regression_neut(returns,liquid_index)),densify(subindustry)*1000+densify(country)+pv13_6l_scibr);trade_when(volume>adv20*0.618,a,-1)
```

**Alpha的模板**

```
initial_index = {data}/volume;time_period = time; #e.g. 120,252index = -(initial_index-ts_mean(initial_index,time_period));group1 = group; #e.g. densify(subindustry)alpha = group_neutralize(quantile(-regression_neut(returns,index)),group1);event1 = event;#e.g. volume>adv20trade_when(event1,alpha,-1)
```

暂未试过可行性。

**探索该Alpha遇到的困难与踩过的坑**

主要困难在于降低turnover，拉decay会让alpha的表现变差，故极少调整。使用trade_when能减少到40%左右，但依然是很高。这导致margin不高。

在USA region还没想到很好降低corr的办法。

---

## 讨论与评论 (5)

### 评论 #1 (作者: WL13229, 时间: 1 year ago)

有一个叫filter的operator非常值得尝试，它的中文翻译叫滤波。

---

### 评论 #2 (作者: WL13229, 时间: 1 year ago)

**分析师覆盖度这个数据应该可以使用analyst dataset里面的数据字段算出**

---

### 评论 #3 (作者: WL13229, 时间: 1 year ago)

另外就是，既然这是一个还可以预测未来半年的回报持续性，在处理主信号的数据时，可以考虑ts_decay_linear等operator，对数据进行科学的平滑，也可以降低turnover

---

### 评论 #4 (作者: ZL29184, 时间: 1 year ago)

用ts_decay_linear后确实turnover降下来了，不过其他的指标没那么好了。


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> Pnl
> 40OOK
> ZOOOK
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



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Average
> Period
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 23.369
> 1.01
> 7.049
> 4.549
> 6.039600


然后试了试filter，在这个alpha效果不是很好。分析师覆盖度我后面再试试。

谢谢老师指导。

---

### 评论 #5 (作者: WL13229, 时间: 1 year ago)

```
Amihud_liquid_index = returns/volume;👆这个地方也可以用ts_decay_linear的
```

---

