# 【Alpha灵感】The Fama and French Six-Factor Model

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】The Fama and French Six-Factor Model_19347527464343.md
- **作者**: TN48752
- **发布时间/热度**: 2 years ago, 得票: 20

## 帖子正文

**Title:** The Fama and French Six-Factor Model –Evidence for the German Market

**Author:**  Daniel Georg Novak

**Link:**   [https://repositorio.ucp.pt/bitstream/10400.14/36816/1/202946215.pdf](https://repositorio.ucp.pt/bitstream/10400.14/36816/1/202946215.pdf)

**Alpha inspiration:**

First we need to understand Multi-Factor Model:  [https://www.investopedia.com/terms/m/multifactor-model.asp](https://www.investopedia.com/terms/m/multifactor-model.asp)

You can also learn about Factor Investing:  [https://www.investopedia.com/terms/f/factor-investing.asp](https://www.investopedia.com/terms/f/factor-investing.asp)


> [!NOTE] [图片 OCR 识别内容]
> Multi-Factor
> Model 
> [ mal-te-fak-tar 'ma-dal]
> financial
> modeling
> strategy in Which multiple
> factors are used to
> analyze
> and
> asset
> Investopedia
> explain
> prices。


A multi-factor model is a  [financial model](https://www.investopedia.com/terms/f/financialmodeling.asp)  that employs multiple factors in its calculations to explain market phenomena and/or  [equilibrium](https://www.investopedia.com/terms/e/equilibrium.asp)  asset prices. A multi-factor model can be used to explain either an individual security or a  [portfolio](https://www.investopedia.com/terms/p/portfolio.asp)  of securities. It does so by comparing two or more factors to analyze relationships between variables and the resulting performance.

## Understanding a Multi-Factor Model

Multi-factor models are used to construct portfolios with certain characteristics, such as risk, or to track  [indexes](https://www.investopedia.com/terms/i/index.asp) . When constructing a multi-factor model, it is difficult to decide how many and which factors to include. Also, models are judged on historical numbers, which might not accurately predict future values.

Multi-factor models also help explain the weight of the different factors used in the models, indicating which factor has more of an impact on the price of an asset.

## Multi-Factor Model Formula

Factors are compared using the following formula:

**Ri = ai + _i(m) * Rm + _i(1) * F1 + _i(2) * F2 +...+_i(N) * FN + ei**

Where:

**Ri**  is the return of security

**Rm**  is the market return

**F** (1, 2, 3 ... N) is each of the factors used

**_**  is the  [beta](https://www.investopedia.com/terms/b/beta.asp)  with respect to each factor including the market (m)

**e**  is the error term

**a**  is the intercept

Multi-factor models can be divided into three categories: macroeconomic models, fundamental models, and statistical models.

**Macroeconomic models:**  Macroeconomic models compare a security's return to such factors as employment,  [inflation](https://www.investopedia.com/terms/i/inflation.asp) , and interest.

**Fundamental models:**  Fundamental models analyze the relationship between a security's return and its underlying financials, such as  [earnings](https://www.investopedia.com/terms/e/earnings.asp) ,  [market capitalization](https://www.investopedia.com/terms/m/marketcapitalization.asp) , and debt levels.

**Statistical models:**  Statistical models are used to compare the returns of different securities based on the statistical performance of each security in and of itself. Many times, historical data is used in this type of modeling.

## Construction of Multi-Factor Models

The three most commonly used models to construct a multi-factor model are a combination model, a sequential model, and an intersectional model.

**Combination model:**  In a combination model, multiple single-factor models, which utilize a single factor to distinguish stocks, are combined to create a multi-factor model. For example, stocks may be sorted based on momentum alone in the first pass. Subsequent passes will use other factors, such as  [volatility](https://www.investopedia.com/terms/v/volatility.asp) , to classify them.

**Sequential model:**  A sequential model sorts stocks based on a single factor in a sequential manner to create a multi-factor model. For example, stocks for a specific market capitalization may be sequentially analyzed for various factors, such as value and momentum, sequentially.

**Intersectional model:**  In the intersectional model, stocks are sorted based on their intersections for factors. For example, stocks may be sorted and classified based on intersections in value and  [momentum](https://www.investopedia.com/terms/m/momentum.asp) .

## Measurement of Beta

The beta of a security measures the  [systematic risk](https://www.investopedia.com/terms/s/systemic-risk.asp)  of a security in relation to the overall market. A beta of 1 indicates that the security theoretically experiences the same degree of volatility as the market and moves in tandem with the market.

A beta greater than 1 indicates the security is theoretically more volatile than the market. Conversely, a beta less than 1 indicates the security is theoretically less volatile than the market.

When multi-factor models are used by investment managers to assess the risk of investments, beta is an important factor that they can use.

In this paper, the author develops from CAPM -> Fama and French Three-Factor Model  -> Carhart Four-Factor Model -> Fama and French Five-Factor Model -> Fama and French Six-Factor Model

**Term**

**Data field**

**Dataset**

risk-free rate

fnd6_newqv1300_optrfrq

**[Company Fundamental Data for Equity](https://platform.worldquantbrain.com/data/data-sets/fundamental6)**

market

market

[**Price Volume Data for Equity**](https://platform.worldquantbrain.com/data/data-sets/pv1)

returns

returns

[**Price Volume Data for Equity**](https://platform.worldquantbrain.com/data/data-sets/pv1)

beta                beta_last_360_days_spy     **[Systematic Risk Metrics](https://platform.worldquantbrain.com/data/data-sets/model51)**

**Size (SMB):** Market capitalization = Market Price x Total number of shares outstanding
 **Value (HML)** : Book-to-Market ratio = Book Value (t−1)
Market Value (t−1)
 **Profitability (RMW):**  Operating Profitability = Operating Profit (t−1)− Interest Expense(t−1)
Book Value (t−1)
 **Investment (CMA):**  Annual Asset Growth = Total assets (t−1) − Total assets (t−2)
Total assets (t−2)
 **Momentum (WML)** : Monthly returns for t-12 until t-2

**CAPM**

The Capital Asset Pricing Model (CAPM) describes the relationship between  [systematic risk](https://www.investopedia.com/terms/s/systematicrisk.asp) , or the general perils of investing, and  [expected return](https://www.investopedia.com/terms/e/expectedreturn.asp)  for assets, particularly stocks.1

U.S. Department of Commerce, Commercial Law Development Program. “ [Financial Modeling: CAPM & WACC](https://cldp.doc.gov/sites/default/files/PPP%20Authority%20Financial%20Modeling%20CAPM,%20WACC,%20and%20Iteration.pdf#:~:text=Formula%20for%20Expected%20Return%20of%20an%20Asset%20%E2%80%A2,%E2%80%A2%20%28ERm%20%E2%88%92%20Rf%29%20%3D%20market%20risk%20premium) .”

 It is a finance model that establishes a linear relationship between the required return on investment and risk. The model is based on the relationship between an asset's  [beta](https://www.investopedia.com/terms/b/beta.asp) , the  [risk-free rate](https://www.investopedia.com/terms/r/risk-freerate.asp)  (typically the  [Treasury bill](https://www.investopedia.com/terms/t/treasurybill.asp)  rate), and the equity risk premium, or the expected return on the market minus the risk-free rate.

CAPM evolved as a way to measure this systematic risk. It is widely used throughout finance for pricing risky  [securities](https://www.investopedia.com/terms/s/security.asp)  and generating expected returns for assets, given the risk of those assets and  [cost of capital](https://www.investopedia.com/terms/c/costofcapital.asp) .

**
> [!NOTE] [图片 OCR 识别内容]
> Capital Asset
> Pricing Model
> (CAPM)
> ['ka-pa-tal 'a-,set 'prisin 'ma-dal]
> A mathematical model
> that estimates the
> expected return ofan
> investment based onits
> riskiness relative to the rest
> ofthe market。
> Investopedia
**

E(Ri) = Rf + βi (Rm – Rf) (4)
where
E(Ri) = Expected return of investment
Rf = Risk-free rate
Rm = Return of market portfolio
βi = Beta coefficient of investment
Rm – Rf = Market risk premium

Understand Expected Returns:  [https://www.investopedia.com/terms/e/expectedreturn.asp](https://www.investopedia.com/terms/e/expectedreturn.asp)

Understand Beta:  [https://www.investopedia.com/investing/beta-know-risk/](https://www.investopedia.com/investing/beta-know-risk/)

Understand Risk-free rate:  [https://www.investopedia.com/terms/r/risk-freereturn.asp](https://www.investopedia.com/terms/r/risk-freereturn.asp)


> [!NOTE] [图片 OCR 识别内容]
> Simulation 13
> CODE
> RESULTS
> LEARN
> DATA
> Sattings
> USA/DITTOPSOO
> narket
> pet
> ts_delta(Itgroup_rank(fam
> rank*returns, subindustry ),320)-3;
> pft
> (fnd6_optrfr);
> expected_
> return
> rft+o.5*beta_last_368_days_spy* (market_ret-8.5*rft);
> IS Summary
> Awerags
> Period
> 05
> actual_
> petupn
> ts_backfill(returns+1,320)-1;
> alpha
> trade_when(ts_rank(ts_std_dev(returns,
> 245)
> 8.76
> actual_
> peturn
> expected_
> return, -1);
> Aggregate Data
> SharOe
> TUTnTTe
> CIIES
> TeCUTI
> LTaVOC
> 4aTaIn
> ts_backfill (alpha, 20 )
> 1,41
> 4,879
> 1,43
> 12,9396
> 11,349
> 53,129000
> Vear
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Narqin
> Cownt
> Short Cownt
> 2015
> 0,33
> 一23
> 31
> 54
> +0:
> 13
> 7017
> 1,73
> 92
> 55:
> 2035
> -3170:
> 102
> 2013
> 0,52
> :
> _
> 一
> 11_
> 12,560:
> 2019
> 1,70
> 一5:
> 17
> 12,33#:
> S5
> 55,5590:
> 12
> 7020
> 34-
> 5
> 5,5
> -5,251:
> 44051
> 201,+30:
> 221
> 1,33
> 35::
> 1131
> 4740
> 105,330:
> 医 Correlation
> Self Correlation
> TiEhes
> UCrelaTiur
> L+ RIn:
> IS Testing Status
> PuSs
> Qone this Alphaina neW tab
> FFNDING
> Example
> SimMlate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> alpha
> 24)'
> Sharpe
> Ung



> [!NOTE] [图片 OCR 识别内容]
> Chart
> PIL
> OOO
> OOOK
> OOO
> OOO
> OOO
> ~10DOK
> Way '165
> Sep '16
> Jan '17
> Way'17
> Jan'13
> SEp"18
> Jan '19
> Way '19
> SEP '19
> Way '20
> SEp 20
> Jan '21
> S-0
> Iy


**Fama and French Three-Factor Model**

The Fama and French Three-Factor Model (or the Fama French Model for short) is an asset pricing model developed in 1992 that expands on the capital asset pricing model (CAPM) by adding size risk and value risk factors to the market risk factor in CAPM. This model considers the fact that value and small-cap stocks outperform markets on a regular basis. By including these two additional factors, the model adjusts for this outperforming tendency, which is thought to make it a better tool for evaluating manager performance.

**
> [!NOTE] [图片 OCR 识别内容]
> Fama and French
> Three Factor Model
> ['f 'ma an(d) 'french 'thre
> fak-tar 'ma da]
> An asset pricing model
> that describes portfolio
> performance by adding size
> and Value Variables to the
> capital asset pricing
> model (CAPM)。
> Investopedia
**

Ri – Rf = ai + βi (Rm – Rf) + si SMB + hi HML + εi (5)
where
Ri = Return of the asset i
Rf = Risk-free rate
Ri - Rf = Expected excess return of the asset i
Rm = Return of the market portfolio
Rm – Rf = Market risk premium
SMB = Size premium, Small minus Big
HML = Value premium, High minus Low
αi = Intercept, Return that cannot be explained by factors
βi, si, hi = Factor coefficients of investment i

Understand HML:  [https://www.investopedia.com/terms/h/high_minus_low.asp](https://www.investopedia.com/terms/h/high_minus_low.asp)

Understand SMB:  [https://www.investopedia.com/terms/s/small_minus_big.asp](https://www.investopedia.com/terms/s/small_minus_big.asp)

Since the model consists of various factors in order to explain the average returns of stocks and
portfolios, the FF3 is considered a key element for the area of “multifactor asset-pricing
models”. But besides the evidence for the size and value
premia, Fama and French (1993) suggest further research, especially regarding the relationship between profitability and average returns, in order to check for other factors that might
possess explanatory power for the performance of assets.


> [!NOTE] [图片 OCR 识别内容]
> Simulation 36
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOPSOO
> Jul'16
> Jan
> Jul'17
> Jan'18
> Jul'18
> Jan '19
> Jul'19
> Jan'20
> Jul '20
> Jan '21
> market_
> pet
> ts_delta(Itgroup_rank(fam
> rank*returns,market ),328)-1;
> pft
> (fnd6_optrfr);
> MMIL
> ts_backfill(ts_delay (mdf_pbk,1),350 ) /ts_backfill(ts_delay (fnd6_mkvalt,1 ),350)
> SMB
> rank(Cap);
> expected_
> return
> rfttbeta_last_36O_days_Spy
> (market
> ret-O.5erft ) +0.5*systematic_risk_Iast_360_days
> IS Summary
> Good
> Period
> HMLbeta
> last_
> 6O_days
> SPy
> SMB*beta_Iast_368_days_Spy;
> actual_
> petupn
> ts_backfill(returns+1,320)-1;
> alpha
> trade_when(ts_rank(ts_std_dev(returns,
> 245)
> 8.76
> actual_
> peturn-expected_
> return, -1);
> Aggregate Data
> SharOe
> JUPICNe|
> CIIES
> TeCUTI
> LTaVOC
> 4aTaIn
> ts_backfill (alpha, 20 )
> 1,54
> 86%
> 1,56
> 12,8496
> 10,3
> 37,439000
> Vear
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Narqin
> Cownt
> Short Cownt
> 2015
> 052
> 551:
> 6::
> 34
> 3,51
> 7017
> 34:
> 034:
> 37151
> 300:
> 2013
> 012
> 1051
> 0,03
> 31
> O
> E0:
> 2019
> 0,31
> 715:
> -5::
> 10,3750
> 250
> 7020
> 425
> 573:
> 5,15
> -5,324
> 30751
> 310:
> 221
> 721
> 252:
> ::
> 5550
> 174,450:
> 医 Correlation
> Self Correlation
> TiEhes
> UCrelaTiur
> L+ RIn:
> IS Testing Status
> Qone this Alphaina neW tab
> Example
> SimMlate
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> alpha
> 24)'
> Sharpe
> Ung



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pn_
> OOOK
> OOOK
> OOOK
> OOOK
> OOOK
> Jul"16
> 30'17
> Jul17
> Jan '18
> Jul '13
> Jan '19
> Jul19
> a1'20
> Jul '20


**Carhart Four-Factor Model**

In addition to the factors that finally led to the FF3, one specific phenomenon also receives considerable attention: the evidence of the past performance of stocks to explain their
future returns. The idea behind it is to analyze the price evolution of past periods and then
make decisions for the portfolio construction based on it in order to generate excess returns.

Ri = ai + βi (Rm – Rf) + si SMB + hi HML + wi WML + εi (6)
where
Ri = Return of the asset i
Rf = Risk-free rate
Rm = Return of the market portfolio
Rm – Rf = Market risk premium
SMB = Size premium, Small minus Big
HML = Value premium, High minus Low
WML = Momentum premium, Winners minus Losers
αi = Intercept, Return that cannot be explained by factors
βi, si, hi, wi = Factor coefficients of investment i


> [!NOTE] [图片 OCR 识别内容]
> Simulation 30
> CODE
> RESULTS
> LEARN
> D4TA
> LOOOK
> Settings
> USA/DITTOPSOO
> Jul'16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul 19
> Jan '20
> Jul '20
> Jan'21
> market_
> pet
> delta(ltgroup_rank(fam_alpha
> rankpeturns
> subindustry ),320)-1;
> pft
> (fnd6_optrfr);
> HMIL
> ts_backfill(ts_delay (mdf_pbk,1),350 ) /ts_backfill(ts_delay (fnd6_mkvalt,1 ),350)
> SMB
> rank(Cap);
> NON
> delay(returns
> 252);
> expected_return
> rfttbeta_last_360_
> days_spy  (market
> pet-O
> 5*rft) +0.5*systematic_risk_last_360_days
> IS Summary
> Good
> Period
> HMLbeta
> last_360
> SPy
> SMB*beta_last_368_days_spy
> MOM*beta_last_368_days_spy;
> actual_
> petupn
> ts_backfill(returns+1,320)-1;
> Aggregate Data
> Sharpe
> TUITNUEI
> Titn
> REIICn
> UCSTOI
> Marain
> alpha
> trade_when(ts_rank(ts_std_dev(returns,
> 245)
> 8.76
> actual_
> peturn
> expected_return,-1);
> 1,57
> 8,6596
> 1,58
> 12,60%6
> 8,1296
> 29,149000
> ts_backfill (alpha, 20 )
> Sharpe
> TurOVer
> Ftnoss
> Returns
> Drawdown
> Maroin
> Long Count
> Short Count
> 715
> 05_
> 532:
> 03
> 57:
> 51251
> 30:
> 2017
> 1,3_
> 515:
> 7,731:
> 2,7956
> 25,330:
> 713
> 0-
> 13133:
> -0,01
> 1.21:
> 1151
> 30:
> 719
> 1,31
> 031
> 314:
> 593
> 330:
> 2020
> 404
> 35:
> 145
> -2,614:
> 0550
> 35,3
> 7021
> 1,31
> 252:
> 1-524
> 503
> 115,770:
> 医 Correlation
> Self Correlation
> HiEhes: Correlatior
> Last Run:
> IS Testing Status
> Conetis Nphain a newtab
> Example
> SimMlate
> Add Alpha
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> days
> 24),
> Vear



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> PIL
> 5.OOOK
> LOOOK
> 3,00OK
> Z.OOOK
> OOOK
> ~1OOOK
> Jul'16
> Jan '17
> Jur17
> Jan '18
> Jul '13
> Jan '19
> Jul 19
> Jan'20
> Jul '20
> Jan '21


**Fama and French Five-Factor Model**

Based on their established FF3, Fama and French (2015) add the well-studied profitability
and investment factors and present the Fama and French Five-Factor Model:
Ri - Rf = ai + βi (Rm – Rf) + si SMB + hi HML + ri RMW + ci CMA + εi (8)
where
Ri = Return of the asset i
Rf = Risk-free rate
Rm = Return of the market portfolio
Rm – Rf = Market risk premium
SMB = Size premium, Small minus Big
12
HML = Value premium, High minus Low
RMW = Profitability premium, Robust minus Weak
CMA = Investment premium, Conservative minus Aggressive
αi = Intercept, Return that cannot be explained by factors
βi, si, hi, ri, ci = Factor coefficients of investment i

In this context, robust companies indicate those with higher operating profitability, while
weak are counterparts with low operating profitability. Correspondently, those companies
with low asset growth in past periods are referred to as conservative, while those with high
investments were called aggressive.


> [!NOTE] [图片 OCR 识别内容]
> Simulation 16
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1/TOP5OO
> Jul'16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul 19
> Jan '20
> Jul '20
> Jan'21
> market
> pet
> ts_delta(Itgroup_rank(fam_alpha
> peturns, subindustry ),320)-3;
> pft
> (fnd6_optrfr);
> HNIL
> ts_backfill(ts
> delay(mdf_pbk,1),350 ) /ts_backfill(ts_delay ( fnd6_mkvalt,1 ),358 )
> SMB
> (cap);
> RJW
> quantile(mdf_oey);
> IS Summary
> SpECtaCUlar
> Period
> CMN
> (ts_delay
> assets,1)-t5_delay(assets,2) ) /ts_delay (assets,2);
> expected_return
> rft+8.5*beta_last_368_days_spy* (market_ret-O.5*rft ) +0.5esystematic_risk_last_368_days
> HMLbeta
> last_360_days_Spy
> SMB*beta_Iast_368_day5_SPy
> RM*beta_Iast_368_day5_SPy
> Aggregate Data
> Sharpe
> TUITNUEI
> Titn
> REIICns
> Drawoown
> Marain
> CMA-beta
> last_368_days_Spy;
> 2,18
> 3,489
> 2,56
> 17,219
> 5,920
> 98,88900
> actual
> peturn
> backfill(returns+1,320)-1;
> alpha
> trade_when(ts_rank(ts_std_dev(returns,
> 24) ,
> 245)
> 8.76
> actual
> return-expected_return, -1);
> Sharpe
> TurOVer
> Ftnoss
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> ts_backfill(alpha,28)
> 715
> 0,3
> 332:
> 07
> 773:
> 5350
> -5,530:
> 2017
> 1,2-
> 231:
> 0,91
> 7.121:
> 43
> 5,560:
> 11
> 713
> -74:
> 12551:
> 8255
> 5330:
> 102
> 719
> 2,14
> 051:
> 17524
> 9255
> 114,550
> 2020
> 459
> 3.53
> +
> -2
> 72
> 731,750:
> 7021
> 1,33
> 051:
> 3.333
> 34151
> 35720:
> 医 Correlation
> Self Correlation
> HiEhes: Correlatior
> LaS LUI
> Qone tis Nphain
> Newtab
> IS Testing Status
> Incompatible Uit fornputatindek
> expected
> UNIUO
> found"UnitISPrice:1]
> Example
> Simulate
> udd Aphato
> Lst
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
> Fank  
> Fank
> Vear



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pn_
> 7.0OOK
> OOOK
> OOO
> OOOK
> OOOK
> OOO
> OOO
> 04'23,201
> Pn: 43438k
> Jul'16
> an'17
> Ju17
> Jan '18
> Jul"13
> a1'19
> Jul'19
> Jan '20
> Jul '20
> a0'21


**Fama and French Six-Factor Model**

Finally, Fama and French completed their FF5 with the momentum factor, introduced
by Carhart, turning into the Fama and French Six-Factor Model:
Ri - Rf = ai + βi (Rm – Rf) + si SMB + hi HML + ri RMW + ci CMA + wi WML + εi (9)
where
Ri = Return of the asset i
Rf = Risk-free rate
Rm = Return of the market portfolio
Rm – Rf = Market risk premium
SMB = Size premium, Small minus Big
HML = Value premium, High minus Low
RMW = Profitability premium, Robust minus Weak
CMA = Investment premium, Conservative minus Aggressive
WML = Momentum premium, Winner minus Loser
αi = Intercept, Return that cannot be explained by factors
βi, si, hi, ri, ci, wi = Factor coefficients of investment i

Even though there exist many more factors with the same purpose, the FF6 represents today a benchmark for multi-factor asset pricing models and is continuously explored.


> [!NOTE] [图片 OCR 识别内容]
> Simulation 16
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOPSOO
> market
> pet
> delta(ItBroup_rank (fam_alpha
> rank*peturns, subindustry ),320)-3;
> pft
> (fnd6_optrfr);
> HMIL
> ts_backfill(ts_delay (mdf_pbk,1),350 ) /ts_backfill(ts_delay (fnd6_mkvalt,1 ),350)
> IS Summary
> SpECtaCUlar
> Period
> SMB
> rank(Cap);
> RJW
> quantile(mdf_oey );
> CMA
> (ts_delay(assets,1)-ts_delay (assets, 2) ) /ts_delay (assets,2);
> Aggregate Data
> Sharpe
> Turnove
> Titn
> REIICn
> Drawoown
> Warain
> MON
> ts_delay(returns
> 252);
> 2,17
> 3,489
> 2,54
> 17,1596
> 5,939
> 98,4
> 0000
> expected_return
> rft+o.5*beta_last_368_days_spy* (market_ret-8.5*rft) +0.5*systematic_
> risk_last_36B_days
> HMLbeta
> last_368_days
> SPy
> SMB*beta_last_368_days_spy
> RM"beta_last_36O_days_Spy
> Sharpe
> TurOVer
> Returns
> Drawdown
> Marqin
> Long Count
> Short Count
> CMA〈beta
> last_
> 6O_days
> Spy+ MOM*beta_last_36O_days_spy;
> actual_
> petupn
> ts_backfill(returns+1,320)-1;
> 715
> 7,3
> 332:
> 0,73
> 177:
> 45751
> -5,320:
> alpha
> trade_when(ts_rank(ts_std_dev(returns,
> 245)
> 8.76
> actual_
> peturn
> expected_return,-1);
> ts_backfill (alpha, 20 )
> 2017
> 1,23
> 231:
> 1
> 7044
> 43
> 5,040:
> 11
> 713
> -7:
> 12714
> 845
> 53,530
> 102
> 719
> 二12
> 317:
> 173334
> 933
> 112,340
> 2020
> 453
> 3.53
> 一,33
> 17250
> 731,3190:
> 7021
> 17
> 05:
> 751:
> 350
> 30:
> 医 Correlation
> Self Correlation
> Hishes: Correlation
> LaS LUI
> IS Testing Status
> Conetis Nphain a newtab
> Incompatible unit forinput at index 1,expected "Unit0". found "Unit[TsPrice:1j"
> 5PuSS
> 1/ 「L I|
> Example
> SimMlate
> Add Alphato
> CS
> Oponalohadotals
> newtab
> Check Submission
> Submit Alpha
> Vear
> Fitmess
> 24),



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> PIL
> 7.OOOK
> GOOOK
> 5,OOOK
> LOOOK
> 3,00OK
> Z.OOOK
> OOOK
> Jul"16
> Jan '17
> Jur17
> Jan '18
> Jul '13
> Jan '19
> Jul19
> Jan'20
> Jul '20
> Jan'21


FF5 and FF6 show good performance at both delay 0.


> [!NOTE] [图片 OCR 识别内容]
> Simulation 84
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DOTTOP5OO
> Jul'16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul 19
> J7'20
> Jul '20
> Jan'21
> market_pet
> delta(ltgroup_rank(returns, subindustry ) , 288)-3;
> Fft
> (fnd6_optrfr);
> HNL
> ts_backfill(ts_delay (mdf_pbk,1),350 )/ts_backfill(ts_delay (mdf
> Cap,1),350)
> SMB
> rank(cap);
> RJW
> quantile(mdf_oey);
> IS Summary
> Scellent
> Period
> CMA
> (ts_delay(assets,1)-ts_delay (assets,2) ) /ts_delay (assets,2);
> NOM
> ts_delay (returns
> 252);
> expected
> return
> rfttmdf
> bet * (mapket_ret
> 8.5*rft )
> HML*mdf_bet
> SMBemdf_bet
> RMemdf_bet
> CMA"mdf_bet;
> egate Data
> TUTIITP
> Fitness
> FSTIC =
> UraoT
> Marain
> #+ MOM*beta_last_368_days
> SPy
> 2,13
> 4,359
> 2,90
> 23,1
> 9
> 9,1796
> 106,459000
> actual peturn
> backfill(returns+1, 280)-1;
> alpha
> trade_when(ts_rank(ts_std_dev(returns, 24),
> 248)
> 8.76
> actual_return-expected_return, -1);
> Sharpe
> TuNOVeF
> Ftnoss
> Returs
> Drawdown
> Marqin
> Long Count
> Short Count
> ts_backfill (alpha,20)
> 2115
> 0,75
> 35*
> 0,52
> 337:
> 55J
> -3,520:
> 12
> 2117
> 113
> 35:
> 3:
> 0910
> 51,30:
> 120
> 213
> 0,3
> 533
> 0,91
> 10,74:
> 9171
> 33340:
> 219
> 13
> 04:
> 325
> 73-3:
> 531
> 115,
> 50:
> -21
> 449
> 一24
> 976
> 504
> 431
> 273,520:
> 103
> 7021
> 351
> 1,77:
> 1.79
> 51,51:
> 5,7151
> 725,350:
> 104
> Correlation
> Self Correlation
> Hiahes: Corre
> aCIUp
> Last Run: .
> IS Testing Status
> Qone tis Nlphaina new tab
> Example
> SImMlate
> udd Aphato
> List
> Oponalpha dotalsinnotab
> Check Submission
> Submit Alpha
> ABBr
> 53r
> Yoar



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> PI_
> OOO
> OOOK
> OOO
> OOO
> Jul'16
> Jan17
> Jan '18
> Jul'18
> Jan '19
> Jul 19
> Jan '20
> Jul '20
> Jan'21
> Jul7


**
> [!NOTE] [图片 OCR 识别内容]
> Table 2: Faclor cottelations _
> Factors
> Nlarket
> SMB
> IIIL
> RAIII
> CMI
> TAIL
> Aarket
> 0O0
> 0.203
> 0.111
> 0.292
> #0.294
> 0.217
> SNB
> 0.208
> 1.OO0
> 0.015
> 0.163
> 0.044
> 0.141
> IIL
> 0.111
> 0015
> 0O0
> 0.514
> 0.355
> 0.167
> RITI
> 0.292
> 0.163
> 0.514
> 1.0O0
> =0.140
> 0.198
> CMI
> 0.294
> 0.044
> 0.355
> 0.140
> 0O0
> 0.109
> TTAIL
> 0.217
> 0.141
> 0.167
> 0.198
> 0.109
> 1000
**

The value factor and the profitability factor have the highest negative correlation at -0.514. The value and investment factors have the highest positive factor correlation at 0.355. This is expected as high B/M stocks tend to have lower profitability and higher investment. The market factor has a negative correlation with all factors except the value factor (0.111), between -0.2 and -0.3. The size and value factor show a minimal correlation of 0.015. Foye found a strong correlation between the size factor and the investment factor. In this sample, the size factor and the investment factor instead show a weak correlation of 0.044. Fama and French, found a positive correlation between the size and market factor (0.28). In this sample, the correlation is negative (-0.208), which indicates that small stocks may have lower betas. The value and momentum factors negative correlation (-0.167) is not surprising as similar, but often stronger, negative correlations are presented by Cakici in the emerging markets and Asness et al (2013) in both the developed and emerging markets. Though there is no consensus regarding the explanation for this negative correlation, Asness et al (2013) have shown that value and momentum have the opposite relationship to liquidity risk. In general, momentum increases while liquidity is available. Value or high B/M firms, on the other hand, tend to increase their returns during liquidity shocks. This pattern is especially visible during periods of financial crisis, for example, the Great Recession between 2007-2009.


> [!NOTE] [图片 OCR 识别内容]
> Table 3: Factor spanning regressions
> A sixth factor is sequentially Teeressed on [ive [aclors _
> The table presents the intercept, coeffcients and adjusted R~ [or each regression。
> non-sienificant intercept indicates that the dependent factor is redundant
> 卡卡|
> 019
> sienificance level *
> % sienificance level,
> S9a
> sienifcance level。
> LHS
> RHS
> Narket
> SNB
> UIL
> RNI
> CMA
> IAIL
> Intercept
> Adj R
> Aarket
> 0.691
> 0.130
> 1.29
> -1.074
> -0.147
> 1.282***
> 0.259
> SNB
> 0.099
> 0.062
> -0.418
> -0.083
> 0.099
> 0.226
> 0.114
> HNIL
> 0.016
> 0.054
> -0.637
> 0.377
> 0.075
> 0.687*米米
> 0.353
> RNI
> -0.076
> 0.174
> -0.306
> -0.059
> 0.056
> 0.404*平
> 0.367
> CNA
> 0.110
> 0.060
> 0.313
> -0.102
> 0.079
> 0.087
> 0.245
> IAIL
> 0.040
> 0.200
> 0.175
> 0.269
> 0.223
> 837**%
> 0.094


The results from the factor-spanning regressions show that the intercepts for the excess market return (Market), value (HML), profitability (RMW) and momentum factor (WML) are all highly significant. It can consequently be concluded that the value factor, in contrast to Fama and French but similar to Cakici, Lin and Foye, is not redundant. Lin and Foye found the investment factor and the size factor to be redundant in Asia. We can likewise conclude that the investment factor is redundant as its intercept is insignificant. The size factor is also insignificant and redundant. In the developed markets, Fama and French found the size and investment factor to be redundant in Europe and Japan. Cakici and Leite do not present any factor-spanning regressions.

**Questions and ideas for improvement:** 
Coverage of alpha (Long + Short)/ Universe_size is quite low, how can we improve it while still maintaining performance?
Is it possible to integrate other factors into the model?

---

## 讨论与评论 (8)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

感动，上了这么多课，第一次有同学把Fama and French因子写出来了.而且还谈到了coverage的问题。进步很快！

---

### 评论 #2 (作者: TN48752, 时间: 2 years ago)

Thank you so much, Mr. WL13229. I hope I can learn more from Brain and the community.

I tried using some backfill functions like kth_element, ts_backfill and group_backfill, but the coverage still hasn't improved.

Besides, I also implemeted a number of tests to check robustness for an alpha, for example, nesting rank, zscore, rank power operators into the final alpha to check sharpe as well as checking sharpe at super and sub-universe (I learned these tests in the Os test video on Brain) and found that alpha ensures robustness. This alpha can work both on Top 3000, 1000 and 200 and delay 0  Top 500 as well.

---

### 评论 #3 (作者: WL13229, 时间: 2 years ago)

对于coverage问题。我建议你对所有使用到的数据，在使用前都进行一次backfill。你可以考虑ts_backfill或者group_backfill.对于偏模型或者比例类的数据，我个人常用group_backfill。这样会比较好地增加覆盖率。

---

### 评论 #4 (作者: TN48752, 时间: 2 years ago)

I just tried using group_backfill by sector and noticed a significant increase in coverage delay 1 and delay 0. Thank you very much for your helpful advice.


> [!NOTE] [图片 OCR 识别内容]
> Simulation 13
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DITTOPSOO
> Jul'16
> Jan
> Jul'17
> Jan'18
> Jul'18
> Jan '19
> Jul'19
> Jan'20
> Jul '20
> Jan '21
> market_
> pet
> ts_delta(Itgroup_rank(fam
> rank"peturns, subindustry ),320)-3;
> pft
> (fnd6_optrfr);
> MMIL
> ts_backfill(ts_delay (mdf_pbk,1),350 ) /ts_backfill(ts_delay (fnd6_mkvalt,1 ),350)
> SMB
> rank(Cap);
> RJW
> quantile(mdf_oey );
> IS Summary
> SCellent
> Period
> CMA
> (ts_delay
> assets,1)-t5_delay e
> assets,2) ) /ts_delay (assets,2);
> MOM
> ts_delay (returns, 252);
> expected_
> return
> rft+o.5*beta_last_368_days_spy* (market_ret-8.5*rft) +0.5*systematic_risk_last_368_days
> Aggregate Data
> SharOe
> JUTICE
> Fitness
> REUTI
> UT3MOUWT
> Warsin
> HMLbeta
> last_368_days_spy
> SMB*beta_Iast_368_days_Spy
> RM"beta_last_36O_days_Spy
> 2,11
> 3,189
> 2,22
> 13,869
> 5,
> 8%
> 87,3
> 0000
> CMA-beta_last_
> 6O_days_spy;
> #+ MOM*beta_last_368_days_spy
> Vear
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Narqin
> Cownt
> Short Cownt
> actual_
> petupn
> ts_backfill(returns+1,320)-1;
> alpha
> trade_when(ts_rank(ts_std_dev(returns,
> 245)
> 8.76
> actual_
> peturn-expected_
> return -1)
> 2015
> 052
> 31:
> 3-1:
> 5135
> 2
> 719
> 51
> Broup_backfill(ts_backfill(alpha, 20) ,industry,350 )
> 7017
> 934
> T」
> 一1:
> 7530
> 2,530:
> 3-
> 2013
> 3.35
> 15:
> 31750
> 5,560:
> -93
> 135
> 2019
> 277:
> _
> 1331
> 4
> 115,100:
> 315
> 7020
> 44
> 335:
> 13
> 3440*
> 0930
> 205,270:
> 55
> 207
> 221
> 64::
> 11,53*
> 5790
> 1-1,44
> 175
> 医 Correlation
> Self Correlation
> TiEhes
> UCrelaTiur
> L+ RIn:
> Qone this Alphaina neW tab
> IS Testing Status
> Incompatible unit forinputat index 1, expected "Unitpm  found "Unit[TsPrice:1]m
> Example
> SimMlate
> Add Alphato
> CS
> 区
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> alpha
> Sharpe
> Ung
> 24),
> 75



> [!NOTE] [图片 OCR 识别内容]
> Simulation 9
> CODE
> RESULTS
> LEARN
> D4TA
> 1,OOOK
> Settings
> USAIDOTTOPSOO
> Jul'16
> Jan '17
> Jul'17
> Jan'18
> Jul'18
> Jan '19
> Jul'19
> Jan'20
> Jul '20
> Jan '21
> market
> pet
> delta(Itgroup_rank(returns, subindustry
> 280)
> pft
> (fnd6_optrfr);
> HMIL
> ts_backfill(ts_delay (mdf_pbk,1),350 ) /ts_backfill(ts_delay (mdf_Cap,1),350)
> SMB
> rank(Cap);
> RJW
> quantile(mdf_oey );
> IS Summary
> Good
> Period
> CMA
> (ts_delay
> as5Sets
> delay e
> assets,2) ) /ts_delay (assets,2);
> MON
> delay(returns, 252);
> expected_return
> rfttmdf_bet * (market_ret-8.5*rft)
> HML*mdf_bet
> SMBemdf_bet
> RMmdf_bet
> CMA*mdf_bet+
> Aggregate Data
> SharOe
> JUTICE
> TItn2s
> Re-Jrns
> UT3MOUWT
> Marsin
> MOM-mdf_bet;
> 2,01
> 3,999
> 2,51
> 19,439
> 8,319
> 97,329000
> actual_
> petupn
> ts_backfill(returns+1, 280)-1;
> alpha
> trade_when(ts_rank(ts_std_dev(returns
> 248)
> 8.76
> actual_
> peturn
> expected_return,-1);
> Vear
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Narqin
> Cownt
> Short Cownt
> Broup_backfill(ts_backfill(alpha, 20), sector
> 350)
> 2015
> 35:
> 043
> 35:
> 6,955
> 3370:
> 24
> 273
> 7017
> 1,15
> 332:
> 02
> 313:
> 5,4351
> -3,700:
> 254
> 2013
> 0,3
> 6::
> 0173
> 3
> 531
> 31,50
> 303
> 23
> 2019
> 372:
> 2:
> S1_
> 113,550:
> 232
> 234
> 7020
> 43
> -04:
> 57
> 5314
> 342
> -3,330:
> 733
> 724
> 221
> 721
> 55:
> 35.331:
> 5
> 457,50:
> 34
> 医 Correlation
> Self Correlation
> HiEhes: Correlation
> L+ RIn:
> IS Testing Status
> Conetis Nphain a newtab
> Example
> SimMlate
> Add Alpha
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> 24),
> Sharpe
> Ung
> ~35


---

### 评论 #5 (作者: deleted user, 时间: 2 years ago)

Wow! I was really impressed when reading your article. Thank you for sharing so detailed about the multi factor model. Regarding factor selection, you can refer to paper "Choosing factors"on SSRN:

[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2668236](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2668236)

Hope this paper can help you

---

### 评论 #6 (作者: BX78946, 时间: 2 years ago)

Hi, thank you for your wonderful sharing. I have learned a lot from it.

I have a question about your definition of market return: 
> [!NOTE] [图片 OCR 识别内容]
> market_ret
> ts_delta(1+Broup_rank (fam_alpha
> 「etURIC
> suhindustry )
> Rank


Your definition of 'market_ret' incorporates information on 'rank', which is measured in terms of ranking. However, your 'rft' below represents information on the rate of return. Can they be directly subtracted from each other given their different dimensions?


> [!NOTE] [图片 OCR 识别内容]
> pft
> (fndo_optrfr);
> expected_return
> rft+g.5*beta_last_368_days_spy * (market_ret-8.5*rft);


Moreover, I am not quite sure about the comparison you are intending to make. Are you looking to compare the current rate of return with that of 320 days ago？

[https://platform.worldquantbrain.com/learn/documentation/create-alphas/example-expression-alphas](https://platform.worldquantbrain.com/learn/documentation/create-alphas/example-expression-alphas)

In the above link, there is an example of CAPM. Hope this could help you!

---

### 评论 #7 (作者: TN48752, 时间: 2 years ago)

Hi Mr.BX78946,

Thank you for your question,

I tried using group_mean and rank for alpha and found that performance is still good, maybe alpha is not sensitive to small changes in data and operators.

I read the example and saw that the lookback used is 250 days (1 year), but here I set 320 to simply fit alpha for the best performance. Perhaps comparing with a lookback longer than 1 year will lead to better results.

Thank you for your comments. I'll delve deeper into this alpha implementation.

---

### 评论 #8 (作者: CZ10093, 时间: 1 year ago)

感谢分享。但是我觉得这个实现不是真正的、理论上的Fama French模型。

比如为什么对于market excess return, SMB和HML，都使用了相同的beta，而WQ提供的beta其实针对的只是market excess return的，不是针对SMB和HML的


> [!NOTE] [图片 OCR 识别内容]
> market
> pet
> ts_delta(ItBroup_rank
> fam_alpha
> peturns,market ),328)-1;
> pft
> (fnd6_optrfr);
> HMIL
> ts_backfill(ts
> delay (mdf_pbk,1),350 ) /ts_backfill(ts_delay (fnd6_mkvalt,1),358 )
> SMB
> (cap);
> expected_return
> rfttbeta_Iast_368_days_Spy
> (market
> pet-O.5 rft )+0.5  systematic_risk_Iast_360_days
> HMLTbeta_Iast_368_days_SPy
> SMB *beta_Iast_368_day5_spy;
> aCtual peturn
> ts_backfill(returns+1,320)-1;
> alpha
> trade_When(ts_rank(ts_std_dev(returns, 24),
> 245)
> .76
> actual
> peturn-expected_return -1);
> ts_backfill(alpha,28)
> Pank 
> Tank


而且理论上的SMB和HML，是类似于大盘的变量，是所有个股所共享的，不是针对每支股票的。每支股票所不同的是针对SMB和HML的“因子暴露”。而代码中的HML和SMB，都是针对个股的。

当然，如果说是因为WQ提供的数据有限，所以权宜之计，我也只能这样了解

---

