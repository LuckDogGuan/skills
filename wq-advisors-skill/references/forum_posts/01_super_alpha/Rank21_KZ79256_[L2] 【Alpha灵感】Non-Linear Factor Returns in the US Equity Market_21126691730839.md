# 【Alpha灵感】Non-Linear Factor Returns in the U.S. Equity Market

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Non-Linear Factor Returns in the US Equity Market_21126691730839.md
- **作者**: YZ64617
- **发布时间/热度**: 2 years ago, 得票: 9

## 帖子正文

论文标题：Non-Linear Factor Returns in the U.S. Equity Market

论文链接： [https://ssrn.com/abstract=4709397](https://ssrn.com/abstract=4709397)

从论文的研读和实现，花了不少时间。中间又借助于ChatGPT去理解一些金融概念。所以，都分享在这里。

## 摘要：

We examine non-linear return-to-characteristic relationships for five equity market factors: Value, Momentum, Small Size, Low Beta, and Profitability. Our research employs monthly returns and characteristics for the largest one thousand U.S. stocks from 1964 to 2023 with a focus on average active returns over the last twenty years. Beyond simplicity in modeling the return generating process we find no reason to assume a linear relationship between characteristics and security returns. Allowance for non-linearity leads to increases in Information Ratios for factor portfolios neutralized with respect to non-linear as well as linear exposure to the other factors. The return to the pure Profitability characteristic across stocks is highly non-linear, as is the alpha return within the Low Beta portfolio. Non-linearity of the Small Size return across the largest one thousand stocks is complex and changed around the turn of the century. Over the last twenty years, the return to earnings yield has been flat across the entire Value spectrum.

这篇论文研究了 **五个股票市场因子（价值、动量、小盘股、低贝塔和盈利能力）** 与回报之间的非线性关系。研究使用了1964年至2023年 **美国最大一千家股票** 的月度回报和特征数据，重点关注过去二十年的平均主动回报。在对回报生成过程进行简化建模的基础上，研究发现没有理由假设特征与证券回报之间存在线性关系。对非线性的允许导致了在与其他因素的非线性以及线性敞口中中性化的因子投资组合的信息比率增加。在股票中，纯盈利特征的回报非常非线性，低贝塔投资组合内的阿尔法回报也是如此。在最大的一千支股票中，小盘股回报的非线性复杂，并在世纪之交左右发生了变化。过去二十年中，整个价值范围内的盈利收益率保持不变。

我对于Beta不是理解接，所以，搜了一下，如下。

### 贝塔Beta的概念 - 来自ChatGPT

在金融领域，贝塔（Beta）通常用来衡量一个资产或投资组合相对于市场整体的价格波动情况。贝塔值大于1表示资产或投资组合的价格波动幅度较市场更大，而贝塔值小于1则表示波动幅度较市场小。

低贝塔（Low Beta）指的是那些相对于市场整体波动较小的资产或投资组合。这类资产可能受市场波动的影响较小，通常被认为具有相对较低的风险。投资者可能会将低贝塔资产纳入他们的投资组合，以寻求更加稳定和相对低风险的回报。

举例来说，假设有一支股票的贝塔为0.8，而市场整体的波动为1.0。这表示该股票相对于市场整体的波动较小，它的价格相对稳定。如果市场上涨1%，那么该股票可能只会上涨0.8%，而如果市场下跌1%，该股票可能只会下跌0.8%。这种相对较小的波动特征使得该股票被认为是低贝塔资产。

- 低贝塔股票：
- - 优势： 低贝塔股票通常相对较稳定，波动性较小，适合那些追求相对低风险、稳定回报的投资者。
  - 劣势： 在市场上涨时，低贝塔股票可能表现相对较弱，因为它们的涨幅通常小于市场平均水平。
- 高贝塔股票：
- - 优势： 高贝塔股票在市场上涨时可能表现更为出色，其回报通常高于市场平均水平。
  - 劣势： 高贝塔股票在市场下跌时可能波动较大，风险相对较高，不适合所有投资者，尤其是那些追求资产保值和相对低风险的投资者。

## 公式

文字提到了线形公式，最后证明很多东西线形公式是无法解释的。这个公式和Fama French factor model类似。通过对其中2个factor的复现，信号是有的，但是远远无法满足需求。


> [!NOTE] [图片 OCR 识别内容]
> Linear Fector PortfolioReturns
> This section introduces econometric methodologies used throughout the paper icluding
> multivariate linear regressions, and then presents the results for non-linear cubic regressions。
> The
> five-factor Fama and Macbeth (1973) linear regression specification is
> ri = GSi,i+C2Sz,i +C3S3,i +C4
> +Cs Ss,i + 8i
> SAi


这个公式的解读：

这五组分数分别对 **应于盈利收益率（即倒数的滚动市盈率）、对数价格动量、负对数市值、负的滚动36个月市场贝塔以及前一年度的毛利率** 。 The five sets of scores in Equation 1, are standardized characteristics to earnings yield (i.e.,  **inverse trailing P/E** ),  **log price momentum** ,  **negative log market capitalization, negative trailing 36-month market beta, and prior-year gross-margin** .

这些特征每个月都进行横截面标准化，使其成为加权均值为零、单位方差的变量。标准化的目的是使得这些特征在横截面上具有可比性，即它们的尺度相同，便于进行比较和分析。

之后，作者又给出了非线性公式


> [!NOTE] [图片 OCR 识别内容]
> NgnLinearFactor PortfolgRetrng
> Non-linear returns within factor portfolios Use an expansion Of Equation
> 1 tat includes
> orthogonalized squared and cubed characteristic scores for each factor. The non-pure single-factor
> portfolio regression specification is
> ri =
> 18+2.32+2383 +81
> where $; is the scored characteristic, and $2 is based on the squared characteristic。
> As described
> j the Technical Appendix, the squared characteristic is analytically orthogonalized to the linear
> SCOre。
> making
> 让
> cross-sectionally
> uncorrelated.
> The
> cubed
> characteristic。
> 83
> is jointly
> orthogonalized to both the linear score and squared characteristics。
> The squared and cubed terms
> 讥 Equation
> 3
> are rescored after orthogonalization to
> 8
> weighted
> mean Of zero and
> weighted
> Variance Of one。
> Ihe orthogonalization process adds precision to the examination Of non-linear
> return
> patterns using cubic regressions because the right-hand side variables would otherwise be
> highly correlated leading to larger correlations in realized portfolio returns. Specifically, the slope
> coefficients,
> 4
> 22
> and
> 33 边 Equation
> 3
> are
> equivalently estimated by three individual
> univariate regressions。
> As with Equation 1 , an intercept term i included is exactly zero, Or equal


重点是，非线性公式不再是5个factor的组合，而是一个factor构成的非线性公式。所以，理论上，可以使用5个factor，构成5个非线形公式 - 5个alpha 策略。

需要注意的是，作者在Appendix中，给出了非线形公式的详细推导，如下


> [!NOTE] [图片 OCR 识别内容]
> The cubed score transformation that is orthogonal to just te linear Score is
> 8
> bit more
> complicated to solve algebraically but can be shown to be
> 8;
> Kurt Si
> Skew
> 83i
> 1/2
> (Tail
> 
> Skew?
> (A15)
> The cubed score transformation that is jointly orthogonal to both the linear score and the squared
> transformation s2i in involves substantial algebra, but can be solved as
> 8
> 一
> Kurt Si
> Skew-Y (52
> 
> Skew -1)
> 831
> 1/2
> (A16)
> Tail
> 
> -Y (Kurt - 2 Skew + Skew-l))
> Hyper
> Skew (Kurt -1)
> Where
> 7
> 一
> (A17)
> Kurt
> 
> Skew? -1
> For example, for a normal distribution with Skew
> 二
> 0, Kurt = 3,
> Hyper
> 二
> 0, and Tail
> 二
> 15,both
> Equations A15 and 416 both simplify to
> Kurtz
> Kurtz
> Skew?
  
> [!NOTE] [图片 OCR 识别内容]
> We first derive a transformation of squared score thatis orthogonal to linear score and has weighted
> ZerO mean and unit Variance。
> With some algebra it can be shown that
> 8
> Skew $;-1
> 82i
> 1/2
> (A13)
> Kurt
> 
> Skew -1)
> has these properties. For example, for a normal distribution with Skew = 0 and Kurt = 3, Equation
> A13 simplifies to
> 82i =
> 疙(?-》
> (A14)


## alpha相关

USA TOP3000 （虽然abstract说作者是用的1000家美国最大股票，实际TOP3000表现更好）NEUTRALIZATION：Slow Factors

数据集可以是5类，如论文所述（已黑体）。我选用了P/E类的数据和Price Momentum，分别构建了2个非线形公式，信号都非常强烈，几乎是可以直接提交的程度。

- P/E: anl69_best_pe_ratio

可能由于P/E数据太过于热门，correlation是一个很大的问题。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> egate Data
> TUTTOTPI
> FTness
> Returns
> ROIO
> Warain
> 3.55
> 50.14%
> 1.50
> 9.00%
> 4.15%
> 3.599oo
> Year
> Turnover
> Fitness
> Returns
> Orawdown
> Margin
> Long Count
> Count
> 2012
> 50.8130
> 2.92
> 12.22%
> 0.509
> 4.812
> 1525
> 1533
> 2013
> 50.853
> 2.85
> 10.75%
> 0.559
> 4.23wee
> 1535
> 1553
> 2014
> 50.1330
> 54%
> 2.219
> 61%a
> 1533
> 1553
> 2015
> 50.23%0
> 67%
> 5795
> 3.45pe
> 1570
> 1557
> 2016
> 4.33
> 50.183
> 3.48%
> 059
> r
> 1562
> 1555
> 2017
> 4.42
> 51.6030
> 1.70
> 63%
> 059
> 96 
> 1543
> 1557
> 2018
> 1.74
> 50.3330
> 0.48
> 89%
> 1.759
> 54ee
> 1549
> 1570
> 2019
> 49.405
> 7.049
> .499
> 8Soe
> 1553
> 1554
> 2020
> 2.75
> 49.11%0
> 1.31
> 11.09%
> 4.159
> 5Zew
> 1555
> 1545
> 2021
> 3.24
> 48.755
> 12.47%
> 349
> 1Ze
> 1547
> 1601
> 2022
> 49.713
> 2.53
> 07骀
> 559
> OGev
> 1520
> 1623
> ABSr
> SIPC
> Sharpe
> Shoft



> [!NOTE] [图片 OCR 识别内容]
> 心耻
> 鬯A
> Simulate
> Alphas
> Data
> 舀 Competitions (4)
> Events
> Learn
> 呆 Refer
> friend
> Simulation
> Simulation 2
> CODE
> RESULTS
> LEARN
> DuT4
> Settings
> USA/D1/TOP3000
> Conyert to Multi-Simulation
> Correlatlon
> Self Correlation
> Tlahesc
> LaSt RUn
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> Prod Correlation
> Hlghest Correlatlon
> LaSt RUn
> REGION
> UNIVERSE
> DELY
> USA
> TOP3OO0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> IS Testing Status
> SIow Factors
> 0.1
> PASS
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> FAIL
> YEARS
> MONTHS
> Verity
> Off
> Prod Correlation
> 868715 above Cutoff ot 0.7and Sharoe not better by 10.055 Ormore。
> WARMNC
> Saye as
> Default
> Apply
> Performance Comparison
> LaSt RUn
> Properties
> Last SaVeJ SUn, 02104'2024
> 11.00 PN
> Name
> Category
> Currently 'anonymOlls'
> NOne
> Clonethis Alphain
> newtab
> Cannot submit Nlpha: 
> test failed


改进：之后，我通过grouping，成功提交了基于P/E的alpha。

感慨一下写出那些数学公式的人，竟然真的可以创建出一个还可以的alpha。

---

## 讨论与评论 (1)

### 评论 #1 (作者: TN63138, 时间: 2 years ago)

您好，您能分享一下 alpha 表达式吗？ 非常感谢。

---

