# 【Alpha灵感】Brain Tips 新闻数据的 Alpha 优化

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Brain Tips 新闻数据的 Alpha 优化_21781672860567.md
- **作者**: ZM32460
- **发布时间/热度**: 2 years ago, 得票: 22

## 帖子正文

Post: Working on news datasets

Link:  [https://support.worldquantbrain.com/hc/en-us/community/posts/8918440691223--BRAIN-TIPS-Working-on-news-datasets](https://support.worldquantbrain.com/hc/en-us/community/posts/8918440691223--BRAIN-TIPS-Working-on-news-datasets)

处理新闻数据集时的一个简单想法可能如下：

事件检测：对于特定股票，确定与该股票相关的新闻发生的日期（您可以通过检查 NaN 和非 NaN 值来做到这一点）。

作业：一旦识别出新闻信息中的相关事件，该股票的仓位就可以视为该新闻对股票价格百分比变化的影响。

持仓：在剩余的时间内，您可以简单地持有您分配的仓位。

按照上述步骤，alpha 可能是： trade_when(news_tot_ticks, news_pct_5_min,-1)

改进范围：在这种情况下，可以在所有三个级别上进行改进。

事件检测也可以通过各种其他方式完成，不同的检测方法可以显着改变您的 alpha 表达。 您可以通过查看“学习”部分中的新闻数据字段来想到其他一些分配方式。 此外，您可以通过设置阈值或衰减 Alpha 来提高 Alpha 性能，而不是仅仅保留 Alpha。 欢迎所有见解或改进！

**优化流程**

我开始使用Brain Tips给出的alpha模拟，但结果并不好. 可以看出，尽管是建立在top3000之上，但换手率和回撤率都很高，覆盖率也很低


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Needs Improwement
> Period
> Aggregate Data
> Sharoe
> TUrNOEr
> HIness
> TSTUIT
> UraWJUIIT
> Marein
> -0,08
> 62,2906
> -0,01
> -0,56%
> 28,049
> -0,189000
> Vear
> TUIIOeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> -1
> 53:
> 1
> S
> 05:
> 625
> 549
> 213
> 1.25
> 5-51:
> 0.04
> 1,441
> 44::
> -5
> 5
> -119
> 623:
> 3:
> 2,96沁
> 2,7156o
> S55
> 21
> T-5
> 63-3:
> 3,7491
> 15,010
> 13?
> 559
> 35
> 721
> 1
> 3,714
> 11
> ~15,433
> 25005
> 52:
> 510
> 2022
> 9
> 61::
> 1511
> 56::
> 670
> 723
> Sharpe
> Lono


阅读文档后，我意识到有一个非常好的新闻 alpha 想法可以应用：
假设 ：
我们研究了上个季度大幅重新定价的股票。 如果近期股价下跌超过10%，下跌趋势可能会持续，因此可以做空。 另一方面，如果自重新定价以来该季度已过去相当长的时间，则应持有多头头寸，因为在过去持续的抛售压力之后，该股可能会开始上涨。
执行 ：
我们使用 ts_arg_min 运算符找到收益下降 10% 的最低持续时间的最近一天。

我发现数据新闻集通常适用于 ts_arg_min 或 ts_arg_max 等运算符。 我还继续暗示通过使用 arc_tan 来提高 alpha 以使值更接近。 另外，我会延长alpha申请时间，5分钟对于投资者在消息出现时决定建仓的时间太短了。


> [!NOTE] [图片 OCR 识别内容]
> Simulation
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOP3OOO
> Jul 17
> Jan'18
> Ju1'18
> Jan '19
> Jul 19
> Jan 20
> Jul 20
> Jan '21
> Jul'21
> Jan'22
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> IS Summary
> Average
> Period
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OO0
> egate Data
> Sharpe
> TICNOE
> Frnes
> ReTlrns
> TCaOCIIT
> Marain
> 1,76
> 21,749
> 1,08
> 8,2396
> 5,31%
> 7,579000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Sharpe
> TurIOVer
> Htness
> Returns
> Drawdown
> Marqin
> LoNg Count
> Short Count
> Market
> 001
> 217
> 159
> 71,153
> 8,9255
> 2-41
> 3,470:
> 573
> 375
> PASTEURIZATION
> UNIT HANDUNG
> NANI HANDLING
> 113
> 1
> 22,521
> 3
> +3
> 3.731
> 123:
> 710
> 402
> Verify
> 0ff
> 219
> 71,533
> 1.13
> 41
> 0595
> 30:
> 713
> 335
> 220
> 71,733
> 11,315
> 5313
> ,350:
> 21
> 355
> Apply
> SaVe 35 Default
> 21
> 1,43
> 21,5593
> 192
> 531
> 3-3
> 7,720
> 2745
> 33
> 2022
> 230
> -323
> 5050
> 51
> 0:
> 7313
> 335
> trade_when(news
> tot_ticks,
> arc_tan(ts_arg_min(news_pct_Izomin, 120) ),-1)
> Correlation
> Self Correlation
> Hiahes: Corre
> aCIUp
> Last Run: .
> IS Testing Status
> Cone tis Nlphaina new tab
> Example
> Simulate
> Add Alpha to
> Ust
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
> ABBr
> Year


信号已经大大增强，可以发送alpha了。 然而，存在一个问题：多空不平衡。 我尝试使用 alpha 等级，但信号丢失了。 请问各位老师、朋友有什么办法可以改善这种情况吗？ 谢谢。

---

## 讨论与评论 (1)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

麻烦展示一下这个Alpha的更多维度信息。另外我个人认为，你首先尝试一下，risk neutral是否可以改变这个情况。

---

