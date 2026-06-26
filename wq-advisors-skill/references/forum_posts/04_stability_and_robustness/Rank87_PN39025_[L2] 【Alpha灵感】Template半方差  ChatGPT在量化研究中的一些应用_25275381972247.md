# 【Alpha灵感】Template：半方差 && ChatGPT在量化研究中的一些应用

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Template半方差  ChatGPT在量化研究中的一些应用_25275381972247.md
- **作者**: XD81759
- **发布时间/热度**: 1 year ago, 得票: 23

## 帖子正文

ChatGPT可以帮我们快速读论文，提取关键信息。以下面这篇论文为例：

Link:  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2565660](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2565660)


> [!NOTE] [图片 OCR 识别内容]
> 读下面
> 段文字;
> 总结股票收益的驱动因素"Based on intraday data
> for a large cross-section of individual stocks and newly
> developed econometric procedures, We decompose the realized
> Variation for each of the stocks into separate so-called realized
> up and down semi-variance measures, or "good" and
> bad"
> volatilities, associated with positive and negative high-frequency
> increments, respectively: Sorting the individual stocks into
> portfolios based on their normalized
> minus bad Volatilities
> results in economically large and highly statistically significant
> differences in the subsequent portfolio returns. These
> differences remain significant after controlling for other firm
> characteristics and explanatory variables previously associated
> With the cross-section of expected stock returns"
> price
> good



> [!NOTE] [图片 OCR 识别内容]
> 这段文字总结了股票收益的驱动因素如下:
> 收益的驱动因素:
> 股票收益的主要驱动因素是 '好"波动性 (即价格上涨时的波动性)
> 与 "坏"波动性 (即价格
> 下跌时的波动性)  之间的差异。
> 通过将股票分成不同的组合
> 并基于其 "好"波动性减去''坏"波动性 进行排序
> 可以观察到
> 这些股票组合的收益存在经济上显著且统计上显著的差异。
> 具体方法:
> 使用高频数据和新开发的计虽经济学方法
> 将股票的实际娈动分解为 "好"半方差和 "坏"
> 半方差。
> 通过对股票迸行组合排序
> 根据其 "好"减去"坏"波动性的标准化值
> 能够发现组合收益的显
> 著差异。
> 控制其他因素:
> 这些收益差异在 控制其他公司特征和  之前与股票收益相关的解释变显 后仍然显著。
> 总结:  股票的收益差异主要由股票的"好"波动性和"坏"波动性之间的差异驱动,
> 这一差异在控制了其
> 他娈量后仍具有显著的解释力。


Alpha实现：


> [!NOTE] [图片 OCR 识别内容]
> r-returns;
> a=power(ts_std_dev(abs(r)+r, 30),2);
> b=power(ts
> dev((abs(r)-"),30),2);
> a-6
> Lstd



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> OOOK
> -1ON
> -151
> ZON
> 251
> 2013
> 2014
> 2015
> 2016
> 2017
> 2015
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> NeedsImproement
> Period
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margiln
> 2.11
> 12.96%
> 3,06
> 27.2596
> 282.949
> -42.059600


结果与论文相反，需要加一个负号才是一个盈利的alpha。这是一个反转信号，做多30天内向下波动大的股票，做空30天内向上波动大的股票。


> [!NOTE] [图片 OCR 识别内容]
> rreturns;
> a=power(ts_std_dev(abs(r)tr,30),2);
> b=power(ts_std_dev( (abs(r)-"),30),2);
> b-a



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> ZON
> 1SN
> SOOON
> 301
> 3014
> 3015
> 3016
> 301
> 2018
> 3019
> 3020
> 3021
> 302



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Period
> Aggregate Data
> Sharpe
> Turnover
> Ftness
> Returns
> Orawdown
> Margin
> 2.11
> 12.96%
> 3.06
> 27.259
> 20.279
> 42.05900


优化后，可以提升Returns/Drawdown Ratio


> [!NOTE] [图片 OCR 识别内容]
> IR
> abs(ts
> mean(returns, 252 ) /ts_std_dev(returns, 252) )
> rsreturns;
> a=power(ts_std_dev(abs(r)+r,30),2);
> b=power(ts_std_dev ( (abs(r)-r),30),2);
> c=regression
> neut (b-a, IR)
> group_neutralize(group_neutralize(c, bucket (rank
> CaP)
> range=
> 0.2,1,0.2' ) ) , country)



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> ZON
> 17.5M
> TSI
> 12.5M
> TON
> 7,50OK
> 0OOK
> SOOK
> 2013
> 2014
> 7015
> 2016
> 2017
> 7018
> 2019
> 3020
> 7021
> 3022



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Specacular
> Period
> Aggregate Data
> Sharpe
> TUrnover
> FItness
> Relurns
> Drawdown
> Margin
> 2.14
> 14.149
> 2.65
> 21.6696
> 11.2596
> 30.649600


同样可以抽象出Template，并跑出可以提交的alpha，大家可以试一试！

补充：

当有了alpha idea不会实现时，可以借助ChatGPT。


> [!NOTE] [图片 OCR 识别内容]
> 我只能计算0方差和@绝对值的方差
> 请问有什么办法可以替代正方差
> 减负方差吗



> [!NOTE] [图片 OCR 识别内容]
> 在理论上
> 正向和负向方差的差异可以通过如下公式估算:
> 正向半方差
> 负向半方差 =原始方差 _绝对值数据的方差
> 这是因为绝对值数据的方差包含了正向和负向波动的合成效应
> 而原始数据的方差则包含了正向
> 和负向波动的实际效应。通过计算两者的差异。可以近似地估算正向半方差和负向半方差之间的
> 差异。
> 理论解释
> 原始方差(6')  考虑了数据中的所有变异。包括正向和负向变异。
> 绝对值方差 (G_abs?) 则在计算时忽略了变异的方向。仅关注娈异的绝对大小。因此。它会高估
> 实际变异。因为正向和负向的波动被当作同等的波动来处理。
> 青青'
> "正方差减负方差" **可以被认为是:
> 原始方差 -绝对值方差
> 这是一种估算方法。用于量化正向和负向娈异的相对大小差异。


该alpha同样可以提交


> [!NOTE] [图片 OCR 识别内容]
> power(ts_std
> dev(abs(returns ), 20),2) -power(ts
> std_dev(returns, 20),2)



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> T51
> T0N
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



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Good
> Period
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.29
> 10.959
> 1.71
> 22.039
> 28.819
> 40.26900


---

## 讨论与评论 (1)

### 评论 #1 (作者: CC85858, 时间: 9 months ago)

------------                                                                                                                                                                                   很有价值的分享

---

