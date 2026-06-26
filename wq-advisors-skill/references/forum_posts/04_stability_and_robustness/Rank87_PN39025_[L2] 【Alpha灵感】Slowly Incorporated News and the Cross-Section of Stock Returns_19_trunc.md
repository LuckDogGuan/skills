# 【Alpha灵感】Slowly Incorporated News and the Cross-Section of Stock Returns

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Slowly Incorporated News and the Cross-Section of Stock Returns_19514322953495.md
- **作者**: FP65798
- **发布时间/热度**: 2 years ago, 得票: 6

## 帖子正文

文章标题和作者

**Tomorrow's Fish and Chip Paper? Slowly Incorporated News and the Cross-Section of Stock Returns**

Ran Tao, Chris Brooks, Adrian Bell

论文链接： [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3363648](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3363648)

概述：论文作者使用双重分类方法将股票分为9类。第一次分类基于调整后的回报，将股票分为高回报（HR）、中回报（MR）和低回报（LR）三类。在每类股票中，再根据新闻情绪进行第二次分类，将股票分为高（HS）、中（MS）和低（LS）三类。这样就得到了3 * 3 = 9 类股票组合。其中，高回报低新闻情绪（HRLS）和低回报高新闻情绪（LRHS）的股票组合称为慢性吸收新闻（SI），而高回报高新闻情绪（HRHS）和低回报高新闻情绪（LRLS）的股票组合称为急性吸收新闻（QI）。 后续的研究重点关注了 SI 和 QI 这两类股票组合。研究发现，SI 对回报具有较高的预测能力。

Alpha构建思路：分类后直接取SI组的sentiment作为因子，只对SI组的进行操作。

• 相关的数据集

Term
Datafield
Dataset

news sentiment score
scl12_sentiment
 [https://platform.worldquantbrain.com/data/data-sets/socialmedia12](https://platform.worldquantbrain.com/data/data-sets/socialmedia12) 

return
returns

[https://platform.worldquantbrain.com/data/data-sets/pv1](https://platform.worldquantbrain.com/data/data-sets/pv1)

Setting 
> [!NOTE] [图片 OCR 识别内容]
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
> Unit Handling
> Equity
> USA
> TOP3000
> Fast Expression
> 0.03
> None
> On
> Off
> Verify


```
monthly_stock_returns = ts_mean(returns, 21);
news_sentiment_scores = (scl12_sentiment - ts_mean(scl12_sentiment, 21))/ts_std_dev(scl12_sentiment, 21);
return_sort = bucket(rank(monthly_stock_returns), range="0.0, 1.0, 0.3333");
LRHS = if_else(
    rank(monthly_stock_returns)<0.333333, 
    if_else(
        group_rank(news_sentiment_scores,return_sort)>0.666667, 
        1, 0
    ),
    0
);
HRLS = if_else(
    rank(monthly_stock_returns)>0.666667, 
    if_else(
        group_rank(news_sentiment_scores, return_sort)<0.333333, 
        2, 0
    ),
    0
);
# LRHS?-group_neutralize(news_sentiment_scores, LRHS):NaN
or(LRHS,HRLS)?news_sentiment_scores:NaN
```

参考论文测试使用的一个月窗口，所以使用ts_mean({data}, 21);

LRHS组记为1，HRLS组记为2。

回测结果如下：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,00OK
> 4,00OK
> 2,00OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.58
> 158.559
> 0.13
> 8.239 19.41%
> 1.04%oo
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 1.80
> 157.839
> 0.82
> 32.779
> 7.06%
> 4.159oo
> 110
> 112
> 2012
> 1.29
> 158.459
> 0.39
> 14.80%
> 13.15%
> 1.87900
> 150
> 156
> 2013
> 0.10
> 158.499
> 0.01
> 0.90%
> 6.58%
> 0.11%o。
> 205
> 228
> 2014
> 0.04
> 157.16%
> 0.00
> 0.63%
> 14.20%
> 0.089。
> 241
> 272
> 2015
> 0.48
> 161.979
> 0.10
> 6.679
> 19.41%
> 0.829。
> 236
> 241
> 2016
> 1.05
> 160.76%
> 0.33
> 16.229
> 13.509
> 2.029o0
> 251
> 254
> 2017
> -0.00
> 157.76%
> -0.00
> -0.049
> 10.219
> -0.009oo
> 287
> 306
> 2018
> 0.23
> 157.609
> 0.03
> 2.649
> 9.45%
> 0.339。
> 293
> 302
> 2019
> 0.96
> 158.539
> 0.27
> 12.18%
> 18.63%
> 1.549oo
> 260
> 271
> 2020
> 0.24
> 156.96%
> 0.04
> 5.179
> 12.8796
> 0.6690。
> 260
> 284
> 2021
> -0.28
> 156.06%
> -0.05
> -5.889
> 4.30%
> -0.7590。
> 290
> 312


可以看到信号，各项指标都不好。但long short count数额接近预期3000*2/9～=666。

根据论文操作，对ruturn数据进行一点调整，用原始数据减去五分位市值组平均

```
cap_sort = bucket(rank(cap), range="0.0, 1.0, 0.2"); #monthly_stock_returns = ts_mean(returns, 21) monthly_stock_returns = returns-group_mean(returns, 1, cap_sort)
```


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1OM
> 7,500K
> 5,0OOK
> 2,50OK
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> NMN
> AN



> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> IS
> 0s
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.10
> 184.689 0.30
> 13.41%17.639
> 1.459o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2011
> 1.01
> 185.389
> 0.30
> 16.43%
> 17.63%
> 1.779。
> 108
> 113
> 2012
> 1.61
> 184.949
> 0.50
> 17.89%
> 6.55%
> 1.93900
> 148
> 156
> 2013
> 1.49
> 184.21%
> 0.40
> 13.099
> 4.1796
> 1.42900
> 202
> 231
> 2014
> 0.65
> 184.009
> 0.13
> 7.099
> 10.54%
> 0.779。
> 228
> 283
> 2015
> 1.79
> 185.859
> 0.58
> 19.45%
> 7.15%
> 2.09%oo
> 232
> 244
> 2016
> 1.34
> 185.589
> 0.41
> 17.329
> 11.869
> 1.8一
> %oo
> 248
> 257
> 2017
> -0.27
> 184.579
> -0.03
> -2.209
> 16.409
> 0.2490。
> 279
> 313
> 2018
> 1.59
> 183.96%
> 0.47
> 16.11%
> 8.71%
> 1.759。
> 288
> 305
> 2019
> 1.38
> 184.629
> 0.38
> 14.20%
> 6.76%
> 1.549oo
> 259
> 271
> 2020
> 0.76
> 183.999
> 0.21
> 14.1796
> 12.1796
> 1.549oo
> 266
> 280
> 2021
> 1.44
> 183.32%
> 0.64
> 35.759
> 9.13%
> 3.909oo
> 293
> 309
> Long
 可以发现各项指标都有明显提高，Sharpe从0.58提高到了1.10， 但Margin还是比较小。

改进思路：

- return数据可继续调整；
- 考虑对非SI组的处理，不然Turnover会一直过高；
- 结合可视化工具做进一步分析改进。


> [!NOTE] [图片 OCR 识别内容]
> 12/09/2019
> Pnl ; 2:
> 1,734.70k
> 2,00OK
> 0-20%:
> -2,195.52K
> 20-4006。
> 1,594.32K
> 40-6096:
> 514.33k
> 60-80%:
> 1,384.87K
> 1,00OK
> 80-1009:
> 2,171.41k
> -1,000K
> -2,00OK
> 2012
> 2014
> 2016
> 2018
> 2020
> Pnl : 2
> 0-20%
> 20-40%
> 40-60%
> 60-809
> 80-1009


---

## 讨论与评论 (0)

