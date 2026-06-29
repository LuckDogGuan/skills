# 【SuperAlpha灵感】ChatGPT Portfolio Selection

- **链接**: https://support.worldquantbrain.com[L2] 【SuperAlpha灵感】ChatGPT Portfolio Selection_21479160264727.md
- **作者**: Nguyen Dang Huynh(HN14753)
- **发布时间/热度**: 2 years ago, 得票: 33

## 帖子正文

大家好，我注意到【Alpha灵感】计划很活跃，但是还没有关于super_alpha的文章，所以今天我想分享一篇我觉得很有趣的论文，可以应用于super alpha的选择和组合。

**Paper:** ChatGPT-based Investment Portfolio Selection

**Authors:**  Oleksandr Romanko, Akhilesh Narayan, Roy H. Kwon

**Link:**  [https://arxiv.org/ftp/arxiv/papers/2308/2308.06260.pdf](https://arxiv.org/ftp/arxiv/papers/2308/2308.06260.pdf)

Abstract: 在本文中，我们探讨了生成式 AI 模型（例如 ChatGPT）的潜在用途 投资组合选择。 值得信赖的来自 Generative Pre-Trained Transformer (GPT) 的投资建议 由于模型“幻觉”，模型是一个挑战，需要仔细验证和验证 输出.输出. 因此，我们采取替代方法。 我们使用 ChatGPT 获取大量股票 对投资具有潜在吸引力的 S&P500 市场指数。 随后，我们比较了各种 利用人工智能生成的交易宇宙的投资组合优化策略，根据这些策略进行评估 定量投资组合优化模型以及与一些流行投资基金的比较。 我们的研究结果表明，ChatGPT 在选股方面有效，但在分配方面可能表现不佳 投资组合中股票的最佳权重。 但当ChatGPT选股与 建立了投资组合优化模型，我们取得了更好的结果。 通过将人工智能生成的选股优势与先进的定量优化技术相结合，我们观察到了 更稳健和有利的投资结果，建议采用混合方法来更有效和可靠 未来的投资决策。 关键词 投资组合优化 · 投资管理 · 生成人工智能 · ChatGPT

在文章中，作者提到了以下模型：我们进一步计算了每个宇宙的均值方差有效前沿，并选择了三个额外的投资组合：
• 最小方差投资组合（“min Var”）；
• 投资组合的最大预期回报（“max Ret”）；
• 最大夏普比率投资组合（“最大夏普”）。

同样，我将为池中的 alpha 标记“max_returns”、“max_sharpe”和“min_var”。我将把相同的选择限制限制为 20 alpha. 对于组合，我保留相同的组合，该组合为具有较低相关性的 alpha 分配较高的权重。 我发现这是一个非常有效的组合

以下是带有“max_sharpe”标签的 Super_alpha 的结果


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Prl
> ION
> 7.5OOK
> OOO
> SOOK
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
> C01b0 Pn_
> Equal Weieht Pnl



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> Sh3rO
> TUFTOE
> FItnEss
> TECUTI
> UTaMOUn
> Marsin
> 5,60
> 12,0906
> 5,39
> 11,6096
> 1,749
> 19,200000
> Sharpe
> Turnover
> Ftnoss
> Returns
> Drawdown
> Margin
> LONg Count
> Short Count
> 2712
> -1-
> 1-13:
> 5,31
> 12,333
> 7,743
> 13,15
> 1515
> 15-2
> 713
> 1537:
> 455
> 10,0095
> 0,429
> 1302
> 533
> 15
> 271-
> 47
> 11:
> 3,7
> 7,7193
> 7,753
> 1351
> 543
> 15-3
> 2715
> 41
> 11,52:
> 327
> 7,53
> 57
> 1311
> 570
> 1557
> 2315
> 543
> 117
> 4,99
> 10,551
> ,73
> 17,932
> 555
> 1572
> 2717
> 5,41
> 15:
> 5
> 10,351
> 5S:
> 17,22
> 5
> 15-3
> 2713
> 4 4-
> 117:
> 3,71
> 3,7393
> 7,513
> 1-3;
> 5
> 1552
> 2119
> 541
> 11,73
> 11,3:1
> 351
> 19,5
> 143
> 15
> 2720
> 103::
> 1435
> 77,333
> 553
> 5-05
> 551
> 15-3
> 2721
> 10,5
> 3,+5
> 10,073
> 1,74:1
> 1901
> S52
> 1565
> 272
> 10-3
> 33
> 13153
> ,:
> 25032
> 1553
> 1533
> Vear


以下是带有“max_returns”标签的 Super_alpha 的结果


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 12/0-12017
> Equal Weight Pnl: 7.293,351
> COIboPnL
> 7.092,31
> OOO
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
> C01b0 Pn_
> Equal Weieht Pnl



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> ShaTOE
> LUrnOE
> TInES
> ECUTI
> UTaMOUT
> 1aTaIn
> 6,49
> 11,4996
> 6,82
> 13,8296
> 1,3706
> 24,049000
> Year
> Sharpe
> TurOVer
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2712
> 54-
> 13-7:
> 11,133
> 0,459
> 155
> 145-
> 5O4
> 2113
>  
> 11,9
> 13
> 1,15
> 429
> -
> 1455
> 1532
> 271-
> 5_-
> 191:
> 753
> 353
> 1-53
> +57
> 503
> 2715
> 5,11
> 1-3-
> 1-,553
> 0,4395
> 19,53
> 1535
> 2115
> 7,25
> 135
> 1,70
> 1,33
> 5
> 5
> 1555
> 2717
> 5,5
> 975:
> 52
> 533
> 7,503
> 193
> 1553
> 2713
> 5,59
> 11.,17::
> 12,313
> 1,7291
> 2313:0
> 1519
> 5O
> 2119
> 7,79
> 9.33:
> 1
> 1,141
> ,511
> 7
> 5-
> 1574
> 2720
> 901:
> 13,53
> 75,351
> 0,4395
> 5955
> SS0
> 1557
> 2321
> 351
> 93::
> 3,51
> 11,241
> 1,371
> 02
> 515
> 1533
> 2022
> 0,51
> 3,3
> -7,25
> 31
> 0,199
> 93
> 5
> 1523
> Ftres


以下是带有“min_var”标签的 Super_alpha 的结果


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Prl
> 7.5OOK
> OOOK
> SOOK
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
> C01b0 Pn_
> Equal Weieht Pnl



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Aggregate Data
> ShaTOE
> LUrnOE
> TInES
> ECUTI
> UTaMOUT
> 1aTaIn
> 5,51
> 10,81%
> 4,93
> 10,0196
> 69
> 18,5
> 0000
> Year
> Sharpe
> TurOVer
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2712
> 5,73
> 11,1:
> 542
> 11,273
> 7,4593
> 203
> 53
> 57
> 2313
> 51_
> 10,21:
> 5,30
> 3,3
> 35:
> 13,252
> 54-
> 15-4
> 271-
> 5,55
> 10-5:
> 517
> 3,331
> 7,373
> 1,3
> 542
> 154
> 2715
> 45
> 03:
> 413
> 3,75:1
> 9395
> 808s
> 55-
> 1573
> 271
> 513
> 12,19沁
> 445
> -:1
> ,7295
> 15-3
> 1537
> 2717
> 4,59
> 10,7:
> 3,75
> 333
> 1,473
> 535
> 513
> 1532
> 2713
> 3
> 43沁
> 3
> 5,133
> 323
> 1031
> 523
> 1535
> 2319
> 531
> 10,29沁
> 55
> 153
> 30
> 2320
> 525
> 153
> 2720
> 5,15
> 1005:
> 1,35
> 13,123
> 7,4493
> 303
> 5
> 1553
> 2321
> 10-31
> 6321
> 3
> 1205
> 1537
> 2022
> ~1,16
> 1r
> 4
> 631
> 453
> 3%
> 564
> 1534
> ?13


可以看出，high_return 标签具有最高的锐度和回报，而 min_var 具有最小的回撤。 作者还通过图表提供了不同选择方法的比较


> [!NOTE] [图片 OCR 识别内容]
> 80%
> 50%
> 
> 4096
> 
> 
> efcient fronter wth bound constraints
> 20%
> eftclent fronter wth no-short-sale Constralnts
> TINIINII ATIIC
> portfolio Imin Varl
> 07ITIM
> expected
> TNIT
> porttolo Imax Retl
> marmum Sharpe ratlo
> portfolio
> Imax Shampel
> GPT-weighted portfolio
> 3qual
> Ily-weighied pontfolio
> individu-lstocks
> Volatility (standard deviationl
> 6 Risk-reward profiles of portfolios from the universe Of 30 stocks (in-sample)
> Fig:


对于GPT加权，作者建议使用Chat-GPT4来选股，但选股在Brain上不适用，所以我不知道在本文中如何提及。此外，“Max Ret”和“Max Sharpe”策略具有最高的夏普比率，表明这些投资组合每单位风险（波动性）具有最佳的样本外表现。 另一方面，“最小方差”策略通常显示出最低的每周波动性，使其成为风险最小的选择，尽管通常会产生较低的回报。本质上，虽然“Max Ret”和“Max Sharpe”策略提供了高回报的潜力，并且具有 尽管夏普比率较高，但它们也带来了巨大的风险。 追求稳定而非高回报的投资者 “Min Var”策略可能会更好。 那些寻求风险和回报之间平衡的人可能会 考虑“GPT 加权”或“等权重”投资组合。

“GPT加权”和“等权重”投资组合提供了稳健的表现，通常介于高回报-高风险“Max Ret”和“Max Sharpe”策略以及低风险低回报“Min Var”策略之间。 从本质上讲，虽然“Max Ret”和“Max Sharpe”策略提供了高回报的潜力并具有优越的夏普比率，但这些策略也带来了巨大的风险。 “Min Var”策略可能会更好地满足寻求稳定而非高回报的投资者的需求。 那些寻求风险和回报之间平衡的人可能会考虑“GPT 加权”或“等权重”投资组合。


> [!NOTE] [图片 OCR 识别内容]
> GPT-welghted
> Equally weighted
> IIn Var
> Max Ret
> 14
> Max
> IIax
> Sharpe
> Card
> MIn Var
> card
> Max Ret
> card
> SSP 500
> Popular Investment Funds
> 13
> 
> 12
> 
> 11
> 10
> 70270115
> 70770101
> 70770.15
> 707705.01
> 7077.075.15
> 70270FO1
> 70270F 15
> 2177-07.01
> 2177-07.1
> 7077.0301
> Date
> Fig: 10 Cumulative returns of portfolios with 15 assets and benchmarks out-of
> sample (14 March 2023
> 31 July 2023)
> Sharpe


值得注意的是，大多数实施的策略都优于传统策略 S&P500 等基准，强调了将 ChatGPT 等 AI 功能集成到 投资策略设计。 此外，增强 ChatGPT 所选性能的策略 通过应用优化技术，投资组合的风险回报显着提高 配置文件。 这展示了用既定的金融理论和技术来补充人工智能能力的价值 技术。

总之，我认为 ChatGPT 可以用作支持人们选择和组合的工具。 尽管 Brain 上的结果并不总是像 ChatGPT 所建议的那么准确，但仍然值得一试。由于许多限制，使用 ChatGPT 作为“独立”投资顾问可能不一定是个好主意。 首先，生成模型会产生“幻觉”，因此生成模型产生的输出需要严格的验证。 它使对其建议进行可靠的验证检查成为实际使用的要求。 至少，获得可靠的投资组合需要向 ChatGPT 提出多个请求，评估结果，并使用多数投票系统最终确定股票组合。 其次，必须确保推荐的资产确实是我们要求的指数的一部分，例如 S&P500。 此外，可能需要对 ChatGPT 输出执行其他不太明显的检查和验证。 另一方面，值得注意的是，ChatGPT 基本上利用了训练期间的综合情绪，这可能并不总是与最新的市场数据一致，至少目前是这样。 然而，当 ChatGPT 的输出与传统定量模型相结合时，改善投资组合风险回报状况的潜力巨大。 通过利用 ChatGPT 生成的投资宇宙并在此基础上执行投资组合优化，我们可以获得比仅使用 ChatGPT 或不使用 ChatGPT 的投资组合优化算法获得的投资组合更好的投资组合。 总之，我们的研究结果得出两个关键结论。 首先，与基数受限的投资组合相比，ChatGPT 投资组合的优异表现强化了 ChatGPT 擅长“选股”的观点。 其次，当与严格的验证和传统的定量金融模型（例如投资组合优化）相结合时，ChatGPT 被证明是一个有价值的投资工具。 这些混合解决方案为实际投资提供了更高效、更有效的方法的潜力，成为当前机器人咨询策略的卓越替代方案。

---

## 讨论与评论 (4)

### 评论 #1 (作者: TN48752, 时间: 2 years ago)

一篇带有非常新主题的帖子。 希望会有更多关于 super_alpha 的鼓舞人心的帖子。 谢谢。

---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

给我一个启发，可以尝试下载自己已经提交的Alpha的PnL,使用GPT推荐做一个组合。看看效果如何。

---

### 评论 #3 (作者: Nguyen Dang Huynh(HN14753), 时间: 2 years ago)

老师您好，我将 super alpha 的结果捕获到 bingAI 中（我还没有 chatGPT 4，所以无法上传 PnL csv 文件）并询问我可以做些什么来改进我的作品集。
虽然仍然很简单，但 Bing 建议通过选择 low_corr alpha 和管理风险来实现多元化。 我看到这两种方法都可以应用在Brain上。 我认为通过更详细的问题，Bing 可以给出更明确的答案。


> [!NOTE] [图片 OCR 识别内容]
> Capilot
> Based on the results Of your super alpha; there are several ways to optimize yOUr
> portfolio beyond selecting alphas with the highest returns;
> 1. Dersification: Include
> variety of uncorrelated alphas to reduce nisk
> 2.Risk Management: Implement strict risk management protocols to minimize
> potential Iosses。
> 3. Dynamic Rebalancing: Regularly adjust the portfolio to maintain the desired risk and
> return levels
> Machine Learning Algorithms: Utilize machine learning to identify patterns and
> optimize alpha selection
> 5. Stress Testing: Test the portfolio under different economic scenarios to ensure robust
> performance。
> Remember that this is
> lighthearted estimation and not
> scientifically precise
> measurement
> 凸 P0 S
> Of 10


---

### 评论 #4 (作者: WL13229, 时间: 2 years ago)

BRAIN平台可以直接通过corr的条件来筛选alpha.您可以尝试一下，看看效果。

---

