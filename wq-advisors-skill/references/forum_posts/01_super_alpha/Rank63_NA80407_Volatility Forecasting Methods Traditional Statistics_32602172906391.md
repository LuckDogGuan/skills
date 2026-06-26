# Volatility Forecasting Methods: Traditional Statistics

- **链接**: https://support.worldquantbrain.comVolatility Forecasting Methods Traditional Statistics_32602172906391.md
- **作者**: 顾问 NA80407 (Rank 63)
- **发布时间/热度**: 1年前, 得票: 2

## 帖子正文

Traditional statistical models are the first models for volatility forecasting, based on the characteristics of volatility in the past that can predict the future. These methods often use historical data in combination with mathematical formulas to estimate and forecast. Their strengths lie in simplicity, strict theoretical foundation and fast deployment. However, for unusual market fluctuations or complex nonlinear relationships, these models often have difficulty forecasting.

### **1.1. Rolling Variance**

Rolling Variance is one of the simplest methods to estimate the volatility. This method uses the sliding average of the variance (or standard deviation) from the property yield chain in a fixed time window to forecast the current volatility or the near future. With intuitive and easy to implement, the Rolling Variance is often used as a preliminary tool to assess the level of market fluctuations.


> [!NOTE] [图片 OCR 识别内容]
> Formula:
> 02
> (ri - p?
> N 1
> tlN+1
> Where:
> 02
> Estimated variance at time t
> N: Length Of the time window (e.e, 20
> 60
> trading days)一
> Return at time i
> I: Mean return over the window A
> often
> assumed to be zero for
> daily returns
> calculated as the sample
> Mean


Advantage:

- Simple and intuitive: This method is easy to calculate, understand and does not require intensive knowledge about statistics.

- Quick: Provide instant estimates of the level of fluctuations based on the nearest historical data.

- Suitable for limited data: Do not require large amounts of data, suitable for small markets or new assets.

Limit:

- Slow reaction: This method assigns uniform weight to all observations in the window, leading to slow response to market shocks or sudden changes.

- Simplifying assumption: Volatility assumption is the constant in the time window that does not reflect the Time-Varying nature of the volatility.

- Sensitive to time windows: The result depends on the length of the N window, and the selection of N is often subjective, lacking a clear theoretical basis.

- Do not grasp the fluctuating cluster: Sliding variance cannot describe the phenomenon of "volatility clustering" - an important feature of the financial chain, where high fluctuations are often followed by similar stages.

### **1.2. ARCH model (Auto Regressive Conditional Heteroskedasticity)**

The ARCH model, introduced by Robert Engle in 1982, marked a turning point in modeling of financial volatility. As a pioneering model in the officialization of the concept of conditional variance, the ARCH assumes that the volatility at the present time depends on the square of the square of the shocks (errors) in the past. This work has brought the Economic Nobel Prize, affirming the importance of the model in finance.


> [!NOTE] [图片 OCR 识别内容]
> ARCH(p ) Formula:
> p = M + Cl
> Gl 二 Oizl,
> 3~ IID(O.I)
> 0 =w + Xaie_i
> 11
> Where:
> 儿: Return at time +
> L: Conditional mean of returns (may be a constant
> Or an ARMA
> model).
> CL: Error (shock) at time , with Ct-i representing lagged errors
> 02: Conditional variance at time .z: Independent and identically
> distributed random variable with
> mean
> 0 and variance I (typically
> standard normal or Student'st).
> W: Positive constant (w > 0).
> Qi: Parameters measuring the impact of the squared lagged error ion
> Current
> volatility:
> 卫: Order of the ARCH model, indicating the number of lagged errors
> considered.


Advantage:

- Fluctuing cluster model: ARCH is the first model to capture the phenomenon of "Volatility Cluster" - high fluctuations often go together.

- Contact the shock: Volatility depends on the magnitude of the past shocks, increasing practicality. Certain theoretical basis: is the foundation for many modern fluctuations.

Limit:

- High level requirements: usually need large levels, leading to many parameters and risks of violating model conditions.

- Symmetrical effects: Not reflecting "leverage effects", when bad news often increases the volatility stronger than good news.

- Limitations: Lack of flexibility when faced with sudden structural changes.

### **1.3. Garch model (Generalized Arch)**

Developed by Bollerslev's heart in 1986, the Garch model expanded from ARCH by adding late volatility components (variance for late conditions) to the variance equation. This helps Garch to grasp the Persistence and the phenomenon of cluster fluctuations more effectively with less parameters. Garch (p, q) is a general form, of which p is the Arch term (late square error) and q is the Garch term (variance with late conditions). In fact, Garch (1,1) is the most common variant thanks to the balance between accuracy and simplicity.


> [!NOTE] [图片 OCR 识别内容]
> GARCH(I,I ) Formula:
> T = Ml + El,
> EL = Olzl;
> Z ~
> IID(0,1)
> 02
> 二
> w + Oc2_1 + Bozl
> Where:
> Oi_1: Lagged conditional variance:
> B: Parameter measuring the impact of past volatility on current
> Volatility。
> W
> (,
> C1: As defined in the ARCH model
> Conditions for positive variance and weak stationarity: w > 0,
> (
> 20,
> B 20,and a +8 < 1.
> A
> sum Ofa + B close to 1 indicates high
> volatility persistence。


Advantage:

- Effective with few parameters: Garch (1.1) only needs three parameters but well described volatility.

- Reflecting durability: grasping the inertia of fluctuations over time.

- Wide application: Popular in risk management, valuation and transactions. There are many variations: Egarch, Gjr-pass, Aparch, Figarch to overcome the limitations of the original model.

Limit:

- Rigid structure: Difficult to describe complex motivation or change the market structure.

- The assumption of distributing limited errors: Not always suitable for actual data. - Difficult estimate: complex variants are easy to cause joints and difficulty estimating

---

## 讨论与评论 (2)

### 评论 #1 (作者: SK90981, 时间: 1年前)

Traditional models like Rolling Variance, ARCH, and GARCH offer solid foundations for volatility forecasting but often struggle with sudden shocks, structural shifts, and complex market dynamics.

---

### 评论 #2 (作者: PY38056, 时间: 1年前)

Great summary of traditional volatility models!  Rolling Variance is a solid starting point, but it's great to see how ARCH and GARCH advanced the field by modeling volatility clustering and persistence. GARCH(1,1)’s efficiency with just three parameters is especially powerful. However, as highlighted, these models do struggle with structural shifts and non-linear complexities — a space where machine learning may offer complementary strength. Excellent post.

---

