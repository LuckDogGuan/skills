# 【Alpha灵感】Constant elasticity of variance model

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Constant elasticity of variance model_21066239770903.md
- **作者**: deleted user
- **发布时间/热度**: 2 years ago, 得票: 26

## 帖子正文

Paper: Estimation in the Constant Elasticity of Variance Model

Link:  [http://www.actuaries.org/AFIR/colloquia/Tokyo/Chu_Yang_Yuen.pdf](http://www.actuaries.org/AFIR/colloquia/Tokyo/Chu_Yang_Yuen.pdf)

恒定方差弹性 (CEV) 扩散过程可用于对普通股回报的异方差性进行建模。 在这个扩散过程中，波动性是股票价格的函数，涉及两个参数。 与 Black-Scholes 分析类似，CEV 模型可以获得看涨期权的均衡价格。 本文的目的是为 CEV 模型提出一种新的估计程序。 我们的方法的一个优点是对模型的弹性参数没有施加任何限制。 此外，不需要频繁调整参数估计。 仿真研究表明该方法适合实际应用。 以香港股票期权市场为例进行说明。 还讨论了该方法的各个方面。

在数学金融中，CEV 或恒定方差弹性模型是一种随机波动率模型，试图捕捉随机波动率和杠杆效应。 该模型被金融行业从业者广泛使用，特别是在股票和商品建模方面。 它由 John Cox 于 1975 年开发。[1]

CEV 模型描述了一个根据以下随机微分方程演化的过程：


> [!NOTE] [图片 OCR 识别内容]
> dSt
> NStdt + OSZdVt


其中S是现货价格，t是时间，μ是表征漂移的参数，σ和γ是其他参数，W是布朗运动。[2] 所以我们有[


> [!NOTE] [图片 OCR 识别内容]
> O(St,t) = OSt



> [!NOTE] [图片 OCR 识别内容]
> The constant parameters 0,
> 2 satisfy the conditions G
> 0,
> V
> >0.
> The parameter ? controls the relationship between volatility and price, and is the central feature of the model. When ?Y
> 1
> We see an effect; commonly observed in equity markets, where the Volatility of a stock increases as its price falls and the
> leverage ratio increases [3] Conversely; in commodity markets; We often observe ? > 1,[4][5] whereby the volatility of the
> Ofa
> commodity tends to increase as its
> increases and leverage ratio decreases. If we observe
> 二
> 0 this model is
> considered the model which was proposed by Louis Bachelier in his PhD Thesis "The Theory of Speculation"
> price
> price


```
我意识到这个阿尔法的最初想法是一个非常简单的价格反转想法：-ts_delta(close,n)
```

我将公式应用到 alpha 上。 我使用 ts_delta 函数作为导数，并且条件是常数 sigma 和 gamma 必须为正。 我面临的困难是我不知道如何将 W is a Brownian_motion 应用于 alpha。 希望得到老师和朋友们的解答


> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1/TOP3000
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> 5,OOOK
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3OO0
> OOOK
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0,03
> 3,00OK
> PASTEURIZATION
> UNIT HANDLNG
> O
> HANDLING
> Verify
> Off
> OOO
> Save as Default
> Apply
> CIose;
> OOO
> 0.4;
> 0.6;
> 0.3;
> dSt
> uts_delta(S,t) /
> Osts_delta(S^V,t)7t;
> a=-pank(dst);
> Jan'18
> Ju1'18
> Jan '19
> Jul 19
> Jan 20
> Jul 20
> Jan '21
> Jul'21
> Jan '22
> IS Summary
> Needs Improvement
> Period
> Aggregate Data
> Sharpe
> TUITNCE
> SinEs
> TetlTn
> Urayon
> Warein
> Qone this Alphaina neW tab
> 1,84
> 69,079
> 0,78
> 12,329
> 8,839
> 3,579000
> Example
> Simulate
> Add Alphato
> CS
> Open alpha details in new t3b
> Chec Swbmissiom
> SUbMit Alpha
> MAAN 
> JUI 17


至于结果，我看到了一个明确的信号，但是收益太高，导致适应度低，使得alpha无法发送，并且prod_corr太高。 我在 trade_when 函数中添加了一些条件，以最大限度地减少营业额并获得更好的结果/


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> 2.5OOK
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> OOOK
> USA
> TOP3OO0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> SOOK
> Subindustry
> 0,03
> PASTEURIZATION
> UNIT HANDLNG
> O
> HANDLING
> OOOK
> Verify
> Off
> SOOK
> Save as Default
> Apply
> OOK
> Jul 17
> Jn"18
> Jul'18
> Jan '19
> Jul' 19
> Jan 20
> Jul 20
> Jan '21
> Jul '21
> Jan'22
> IS Summary
> Awerags
> Period
> Qone tis Nlphaina new tab
> Aggregate Data
> Sharpe
> |UrNOE
> FITESs
> KETUFRS
> P3UCC
> Warsin
> 1,89
> 22,3496
> 1,05
> 889
> 3,769
> 6,165
> Incompatible unit for inputatindex 0, expected "Unitp" found "Unit[csPrice:1]": Incompatible unit for inputat
> Toek
> expected "Unit[TsPrice:tj". found "Unitpm
> Year
> TUIIOVeT
> Ftnoss
> Returs
> Dawdown
> Margin
> Count
> Short Cownt
> Example
> SimMlate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> 9o0
> Sharpe
> LoNO


下一个问题是我是否可以找到更多 CEV 模型的变体，因为 prod corr 仍然很高，并且还无法提交 alpha。 希望得到老师和朋友们的解答。 谢谢

---

## 讨论与评论 (2)

### 评论 #1 (作者: YW93864, 时间: 2 years ago)

[deleted user](/hc/en-us/profiles/18243496991767-deleted-user)  hello，因为dW=(dt)^(0.5)，您这里设置的t是4，那么W应该等于2。

额外的问题：我看到您的表达式最后和微分方程似乎不太一样，因为似乎表达式中有两个导数，而微分方程中是dt和dW两个随机变量；以及对于mu,sigma等参数，我猜应该不是手动设定的，可以尝试用ts_mean,ts_std_dev重构，看看能否降低corr

额外的想法：仅针对您的表达式而言，我对该alpha的理解是，它在价格反转策略的基础上，考虑了价格非线性变化。一方面可以再引入偏度和峰度，似乎可以按照JB-test的方法；除了使用close以外，可以看看其他价量数据有没有信号

---

### 评论 #2 (作者: deleted user, 时间: 2 years ago)

你好。 谢谢您的意见。 我将研究并优化阿尔法。

---

