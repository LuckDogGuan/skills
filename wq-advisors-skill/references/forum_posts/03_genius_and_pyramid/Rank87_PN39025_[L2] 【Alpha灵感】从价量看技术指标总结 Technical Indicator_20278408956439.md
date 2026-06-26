# 【Alpha灵感】从价量看技术指标总结 (Technical Indicator)

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】从价量看技术指标总结 Technical Indicator_20278408956439.md
- **作者**: TN48752
- **发布时间/热度**: 2 years ago, 得票: 41

## 帖子正文

老师们、同学们大家好。 经过一段时间的研究如何使用价量数据集创建技术指标，今天我想分享一些我已经实现的指标。本文将不断更新新指标。 如果我没有正确实施 alpha，如果您能提供额外的指标或建议，我将感到荣幸和荣幸。

**什么是技术指标？** 
技术指标是由遵循技术分析的交易者使用的证券或合约的价格、交易量和/或未平仓合约产生的启发式或基于模式的信号。

通过分析历史数据，技术分析使用指标来预测未来的价格走势。 常见技术指标的示例包括相对强弱指数 (RSI)、资金流量指数 (MFI)、随机指标、移动平均收敛散度 (MACD) 和布林线 (Bollinger Bands®)。

技术指标有两种基本类型：

叠加：使用与价格相同比例的技术指标，绘制在股票图表上价格的顶部。 示例包括移动平均线和布林带®。
振荡指标：在局部最低值和最高值之间振荡的技术指标绘制在价格图表的上方或下方。 示例包括随机震荡指标、MACD 或 RSI。

**技术指标示例** 
下图显示了一些最常见的技术指标，包括移动平均线、RSI 和 MACD。


> [!NOTE] [图片 OCR 识别内容]
> 0907
> 285.0
> 282,5
> 280.0
> 277.5
> 2750
> 27338
> 271
> 41U,U
> 267,5
> 265,0
> 262.5
> 260.0
> 40OI
> 257,5
> 300N
> 25491
> 20ON
> 252,5
> I0ON
> 250,0
> 689992
> 0319
> 16 23
> 6 132027Dec 11
> 18 26
> 1622
> 122026
> Oct
> Nov
> 2018
> Feb
> Mar
> Investopedia


在此示例中，50 天和 200 天移动平均线绘制在价格上方，以显示当前价格相对于历史平均线的位置。 在这种情况下，50 日移动平均线高于 200 日移动平均线，这表明总体趋势是积极的。 图表上方的 RSI 显示了当前趋势的强度，在本例中为中性 49.07。 图表下方的 MACD 显示两条移动平均线如何收敛或背离——在本例中略显看跌。

**1. RSI - Relative Strength Index**

**Link:  [https://www.investopedia.com/terms/r/rsi.asp](https://www.investopedia.com/terms/r/rsi.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Relative Strength
> Index (RSI)
> [re-la-tiv 'stren(k)th in-,deks]
> Atechnical indicator, used
> in momentum
> trading; that
> measures the
> and
> magnitude ofa securityis
> recent price changes。
> Investopedia
> speed



> [!NOTE] [图片 OCR 识别内容]
> RS Istep
> 100
> I00
> Ole
> 1 NTes 2卫
> Arrerage LOs


window = 20;

offset = 0.02; delta = ts_delta(vwap, 1);

RS = ts_sum((delta>0 ? delta : 0), window) /ts_sum((delta<0 ?delta : 0), window) + offset; RSI = 100 - 100/RS ;

-hump_decay(-RSI, p = 4, relative = False)

**2. Bollinger Bands**

**Link:  [https://www.investopedia.com/terms/b/bollingerbands.asp](https://www.investopedia.com/terms/b/bollingerbands.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Bollinger Band
> [bal-in-ar- 'band]
> Atechnicalanalysis tool defined
> bya setof trendlines plotted
> two standard deviations
> (positively and negatively)
> away froma simple moving
> average (SMA) of a security's
> but which can be adjusted
> to User
> preferences。
> Investopedia
> price;



> [!NOTE] [图片 OCR 识别内容]
> BOLU
> 二
> NIA(TP,n) - m * O[TP, n]
> BOLD
> JIA(TP,n)
> m * O[TP, n]
> Where:
> BOLUJ
> Upper Bollinger Band
> BOLD
> Lower Bollinger Band
> TIA
> MIoving average
> TP (typical price)
> High + Low - Close) = 3
> 1
> Mumber of days in smoothing period (typically 20)
> 112
> Number ofstandard deviations (typically 2)
> O[TP,n]
> 二
> Standard Deviation OTer last n
> periods Of TP


window = 20;

tp =(high+low+close)/3;

MA= ts_mean(tp,window);

BOLU = MA + ts_std_dev(tp,window);

BOLD = Ma - ts_std_dev(tp,window);

signal = ts_sum(close<BOLD,window)-ts_sum(close>BOLU,window); ts_zscore(signal,240)

**3. Moving average**

**Link:  [https://en.wikipedia.org/wiki/Moving_average](https://en.wikipedia.org/wiki/Moving_average)**


> [!NOTE] [图片 OCR 识别内容]
> Moving Average (MA)
> 'mli-vin a-vla-Jij]
> A stock indicator commonly
> used in technicalanalysis。
> Investopedia


**a. SMA (Simple moving average)**


> [!NOTE] [图片 OCR 识别内容]
> 41一_42 +
> 一 _4n
> SU4 =
> There:
> 1 = Arerage i Period n
> 几 =
> Number oftime periods


SMA = ts_sum(close,n)/n

Example:
signal = abs(ts_mean(close,20)/ts_mean(close,60)-1);
signal*sign(returns)

**b. EMA (Exponential Moving Average)**


> [!NOTE] [图片 OCR 识别内容]
> EM4t
> T
> ()]-
> + EMAy
> [-()]
> Vhere:
> EM4t
> EMIA today
> T = Valle today
> EMIAy
> ENIA yesterday
> Smoothing
> Number Of days


EMA = ts_decay_exp_window(close,window)

**c. WMA (Weighted Moving Average)**


> [!NOTE] [图片 OCR 识别内容]
> Pricer
> X n 十
> Pricez
> 几
> 1) 一
> Pricen
> TTIIA
> n < (TT11
> Where:
> 几 =
> Time period


WMA = ts_decay_linear(close,window)

**d. TRIX (Triple Exponential Average)**


> [!NOTE] [图片 OCR 识别内容]
> EMAI(i)
> 二
> EMA(Price; N,1 )
> Where:
> Price(i) =
> Current Price
> EMAI(i)
> 二
> Tlle currelt Value of the Exponential
> MIoving Average
> Next, the second smoothing ofthe obtained average is executed-double
> exponential smoothing:
> EMA2(i)
> EMIA(EMIAI,N,i)
> The double exponential movingaverage is smoothed exponentially one more
> time-hence, the triple exponentialaverage:
> EM 43(i)
> EMA(EM42,N,i)
> Now the indicator itself is found with:
> EU43(i)
> EUA3(i 1)
> TRIY(i)
> E4(讧n


EMA1 = ts_decay_exp_window(close,15);

EMA2 = ts_decay_exp_window(EMA1,15);

EMA3 = ts_decay_exp_window(EMA2,15);

TRIX = (EMA3 - ts_decay_exp_window(EMA3,14))/ts_decay_exp_window(EMA3,14);

**e. Double Exponential Moving Average (Dema)**


> [!NOTE] [图片 OCR 识别内容]
> DEU1 = 2
> EMA
> EMIAof EM_A
> Vhere:
> N
> Look-back period


EMA1 = ts_decay_exp_window(close,15);

EMA2 = ts_decay_exp_window(EMA1,15);

DEMA = 2*EMA1 - EMA2

**f. MACD (Moving Average Convergence/Divergence)**


> [!NOTE] [图片 OCR 识别内容]
> IIACD
> I2-Period ENIA
> 26-Period ENIA


EMA12 = ts_decay_exp_window(close,12);

EMA26 = ts_decay_exp_window(close,26);

MACD = EMA12 - EMA26

**g. STC (Schaff Trend Cycle)**

EMA23 = ts_decay_exp_window(close,23);

EMA50 = ts_decay_exp_window(close,50);

STC = ts_decay_linear(EMA23 - EMA50,10)

h. QStick Indicator


> [!NOTE] [图片 OCR 识别内容]
> QSI = EIIA or SNIA of ( Close
> Open)
> Where:
> ENIA
> Exponeltial moring arerage
> SNII
> Simple Iorilg arerage
> Close
> Closing price for period
> Open
> Opening Price for period


QSI = ts_decay_exp_window(HIGH-CLOSE,window)

**4. ATR (Average True range)**

**Link:  [https://en.wikipedia.org/wiki/Average_true_range](https://en.wikipedia.org/wiki/Average_true_range)**


> [!NOTE] [图片 OCR 识别内容]
> Average True
> Range (ATR)
> ['a-vla-)rijj 'trii 'ranj]
> technicalanalysis
> indicator that measures
> market volatility by
> decomposing the entire
> range ofanasset
> for that period。
> Investopedia
> price



> [!NOTE] [图片 OCR 识别内容]
> Previous ATR(n
> 1) + TR
> Where:
> 1
> Number Of periods
> TR
> Trle range
> Ifthere is not a previous ATR calculated, you must use:
> TRi
> There:
> TRi
> Particular trle range; such as first day's
> then secold, tlen third
> 1
> Number ofperiods
> T;



> [!NOTE] [图片 OCR 识别内容]
> TR
> MIax [(珏
> 工), |
> Cpl; I工
> Cpl]
> There:
> 珏
> Today's high
> 工
> 二
> Today's IoT
> Cp = Yesterday's closing price
> Nax
> Highest value of the three terms
> 50 that:
> (珏
> 工)
> Today's high minls the Iow
> |珏
> Cpl
> Absolute Value Of today's high minlls
> yesterday's closing price
> [
> Cpl
> Absolute value Of today's Iow Iinlls
> Jesterday's closing Price


window = n;

TR = max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1)));

ATR = ts_sum(TR,window)/window;

**5. Rate of change (ROC)**

**Link:  [https://www.investopedia.com/terms/r/rateofchange.asp#:~:text=Rate%20of%20change%20(ROC)%20refers,and%20identify%20momentum%20in%20trends](https://www.investopedia.com/terms/r/rateofchange.asp#:~:text=Rate%20of%20change%20(ROC)%20refers,and%20identify%20momentum%20in%20trends) .**

**
> [!NOTE] [图片 OCR 识别内容]
> Rate of
> Change
> [ratav 'chanj]
> The
> at Which
> variable changes
> OVera
> specific
> period of time。 
> Investopedia
> speed
**


> [!NOTE] [图片 OCR 识别内容]
> Closing
> ROC
> 100
> Closing
> Where:
> Closing 
> Closing price of most recent period
> Closing
> Closing price n periods before
> IlOst Iecelt
> period
> Pricep
> Pricep
> Pricep
> Pricep


ROC = ts_delay(close,p)/ts_delay(close,p-n)*100;

**6. Stochastic Oscillator**

**Link:  [https://www.investopedia.com/terms/s/stochasticoscillator.asp](https://www.investopedia.com/terms/s/stochasticoscillator.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Stochastic
> Oscillator
> [sta- 'ka-stik 'a-sa- la-tar]
> Amomentum indicator
> comparing a particular
> closing
> ofa security to
> 0
> range ofits prices overa
> certain period oftime。
> Investopedia
> price



> [!NOTE] [图片 OCR 识别内容]
> 工14
> %k =
> 100
> H14
> 工14
> Where:
> C = The most recent closing price
> LI4
> The Iowest Price traded of the 14 previols
> trading sessions
> 珏14
> The highest price traded during the same
> I4-day period
> %
> The currelt Talue of the stochastic indicator


C = close;

L14 = ts_min(low,14);

H14 = ts_max(high,14);

%K = (C-L14)/(H14-L14)*100;

**7. On Balance Volume**

**Link:  [https://www.investopedia.com/terms/o/onbalancevolume.asp](https://www.investopedia.com/terms/o/onbalancevolume.asp)**


> [!NOTE] [图片 OCR 识别内容]
> On-Balance
> Ill
> Volume (OBV)
> [on 'ba-lanft)s 'val-(Jyiim]
> Atechnical
> momentum indicator
> that uses volume flow
> to
> predict changes in
> stock
> Investopedia
> MIM
> trading
> price。



> [!NOTE] [图片 OCR 识别内容]
> Tolume;
> 让 close
> OBV
> OBVprev
> 0;
> 让 close
> Volume;
> 让 close
> Where:
> OBV
> Current on-balalce Tolulne lerel
> OBVprev
> Previols on-balalce Tolule level
> Tolulhe
> Latest trading Volume amolnt
> Closeprev
> closepreu
> Closeprev


OBV = vec_avg(mdl109_vbo);

close>ts_delay(close,1)? ts_delay(OBV,1) + volume : ts_delay(OBV,1) - volume

**8. Aroon Oscillator**

**Link:  [https://www.investopedia.com/terms/a/aroonoscillator.asp](https://www.investopedia.com/terms/a/aroonoscillator.asp)**


> [!NOTE] [图片 OCR 识别内容]
> The formula forthe Aroon oscillatoris:
> Aroon Oscillator
> Aroon UP
> Aroon DowII
> (25
> Periods Since 25-Period High )
> Aroon UP
> 100 *
> 25
> (25
> Periods Since 25-Period LoT
> Aroon DoTII
> 100
> 25


arr_up = (25 - ts_arg_max(high, 25))/25*100;

arr_down = (25 - ts_arg_min(low, 25))/25*100;

arr_os = arr_up - arr_down

**9. Average Directional Index (ADX)**

**Link:  [https://www.investopedia.com/terms/a/adx.asp](https://www.investopedia.com/terms/a/adx.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Smoothed -DM
> TDI
> 100
> 4TR
> Smoothed -DM
> DI
> 100
> 4TR
> TDI
> ~DI
> DX
> 100
> LDI + -DI
> Prior ADX
> X13
> 十 Current ADX
> ADX
> 14
> Where:
> ~DM (Directional Uovement
> Current High
> P珏
> P珏
> Previous High
> ~DMI
> Previous
> Current LoN
> 14
> SDN
> Smoothed -/-DMI
> t=1
> DM
> ~ CDNI
> CDM
> Current DN
> 4TR
> Average Tre Range
> Low


DH = high - ts_delay(high,1);

DL = low - ts_delay(low,1);

TR = max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1)));

DH_smooth = ts_sum(DH,14)/14;

DL_smooth = ts_sum(DL,14)/14;

TR_smooth = ts_sum(TR,14)/14;

DIH = DH_smooth/TR_smooth*100;

DIL = DL_smooth/TR_smooth*100;

DX = abs(DIH-DIL)/abs(DIH+DIL)*100;

fADX = ts_sum(DX,14)/14;

ADX = (ts_delay(fADX,1)*13+fADX)/14

**10. Supertrend Indicator**

**Link:  [https://www.investopedia.com/supertrend-indicator-7976167](https://www.investopedia.com/supertrend-indicator-7976167)**


> [!NOTE] [图片 OCR 识别内容]
> Supertrend
> Indicator
> ['sii-par-'trend 'in-da-ka-tar]
> (
> A
> technical
> analysis tool designed to
> assist tradersin
> identifying
> market trends。
> Investopedia
> ~6
> popular


Multiplier = const;

window = n;

TR = max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1)));

ATR = ts_sum(TR,window)/window;

Supertrend=(High+Low)/2+(Multiplier)*(ATR)

**11. Fractal Indicator**

**Link:  [https://www.investopedia.com/terms/f/fractal.asp](https://www.investopedia.com/terms/f/fractal.asp)**


> [!NOTE] [图片 OCR 识别内容]
> The Formulas for Fractals Are:
> Bearish Fractal
> High(M) > High(T - 2) and
> High(V)
> High( _ 1) and
> High(N) > High(V + 1) and
> High(M) > High(T + 2)
> Bullish Fractal
> Low(N) < Low(N
> 2) and
> LOV(N)
> Low(N
> 1) and
> LoV(N)
> Low(N _ 1) and
> LoV(N)
> Low(N _ 2)


n = window

Bearish_Fractal = ts_delay(high,n) > ts_delay(high,n-2) && ts_delay(high,n) > ts_delay(high,n-1)&& ts_delay(high,n) > ts_delay(high,n+1)&& ts_delay(high,n) > ts_delay(high,n+2);

Bullish_Fractal = ts_delay(low,n) < ts_delay(low,n-2) && ts_delay(low,n) < ts_delay(low,n-1)&& ts_delay(low,n) < ts_delay(low,n+1)&& ts_delay(low,n) < ts_delay(low,n+2);

**12. Fisher Transform Indicator**

**Link:  [https://www.investopedia.com/terms/f/fisher-transform.asp](https://www.investopedia.com/terms/f/fisher-transform.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Fisher Transform
> 2
> 1
> ()
> Khere:
> In is tle natural logarithm
> 王
> transformatiol Of price to a lerel betmeen -1 and 1


X = s_log_1p(close)

Fisher = 0.5*log((1+X)/(1-X))

**13. Accumulation/Distribution Indicator**

**Link: [https://www.investopedia.com/terms/a/accumulationdistribution.asp#:~:text=The%20accumulation%2Fdistribution%20indicator%20(A%2FD)%20is%20a,how%20strong%20a%20trend%20is](https://www.investopedia.com/terms/a/accumulationdistribution.asp#:~:text=The%20accumulation%2Fdistribution%20indicator%20(A%2FD)%20is%20a,how%20strong%20a%20trend%20is) .**


> [!NOTE] [图片 OCR 识别内容]
> Accumulation/
> Distribution
> Indicator (A/D)
> [a-kyii-m(y)a- 'la-shan
> di-stra-'byij-shan in-da  ka-tar]
> A
> cumulative indicator
> that uses volume and
> price to confirm
> trends。
> Investopedia
> price



> [!NOTE] [图片 OCR 识别内容]
> Close
> LoT
> (High
> Close)
> VIFNI
> High
> LoT
> Where:
> VIFNI
> Noney Flov Nultiplier
> Close
> Closing price
> LOT
> Low price for the period
> High
> High price for the period
> NIoney Flow Volume
> NIFNI X Period Volulne
> 4/D = Previous A /D - CNFV
> Where:
> CNIFV
> Current Period money tlow Volume


MFM = ((close-low)-(high-close))/(high-low);

MFV = MFM*volume; #money flow volume

A_D = ts_delay(A_D,1)+MFV #For the first calculation, use money flow volume as the first value.

**14. Adaptive Price Zone**

**Link:  [https://www.investopedia.com/articles/trading/10/adaptive-price-zone-indicator-explained.asp](https://www.investopedia.com/articles/trading/10/adaptive-price-zone-indicator-explained.asp)**


> [!NOTE] [图片 OCR 识别内容]
> 657.03
> Decrcased Volatlity
> 63960
> 620,00
> 600.00
> 586.68
> 580,00
> 560.00
> Increased Volatility
> 540.00
> 21 28 ^5
> 21 28'10
> Sep
> Oct
> Nov
> Dec
> Investopedia



> [!NOTE] [图片 OCR 识别内容]
> Upper APZ Band = (Volatility Value
> Deviation Factor) + Volatility
> Value
> Lower APZ Band = (Volatility Value
> Deviation Factor) -
> Volatility
> Value


Vol_value = ts_decay_exp_window(close,5) - ts_decay_exp_window(high-low,5);

UAPZ = Vol_value*fnd65_us5000_cusip_60dsigma + Vol_value;

LAPZ = Vol_value*fnd65_us5000_cusip_60dsigma - Vol_value;

**15. Ease of Movement Indicator**


> [!NOTE] [图片 OCR 识别内容]
> High
> LOT
> PH
> 豇
> Distance Lored
> Iolume
> Box Ratio
> Scale
> '
> LOT
> 丑E
> Lor
> PH - P工
> I-Period ENIV
> Tolum
> SAle
> Igh
> LoT


​Distance_Moved = (high+low)/2 + (ts_delay(high,1)+ts_delay(low,1))/2;

box_ratio = volume/(high-low);

EMV = ​Distance_Moved/box_ratio

**16. Ichimoku Cloud**

**Link:  [https://www.investopedia.com/terms/i/ichimoku-cloud.asp](https://www.investopedia.com/terms/i/ichimoku-cloud.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Ichimoku Cloud
> ['ich-y mo- 'kii 'klaud]
> Acollection of technical
> indicators that show support
> and resistance levels, as well
> as momentum and trend
> direction。
> Investopedia



> [!NOTE] [图片 OCR 识别内容]
> 9-卫珏 - 9-卫r
> Conversion Line (tenkan sen)
> 26-卫珏 + 26-卫
> Base Line (kijlll Sen)
> CL
> Base Line
> Leading Span
> 4
> (senkou spall 4 ) =
> 52-卫珏-52-卫
> Leading Span B (senkou span B)
> Lagging Span
> chikoll sPan)
> 二 Close
> plotted 26 periods
> i the Past
> Where:
> PH
> Period high
> PL
> Period loT
> CL
> ConTersion
> lne


CL = (ts_max(high,9) + ts_min(low,9))/2;

BL = (ts_max(high,26) + ts_min(low,26))/2

SPA = (CL+BL)/2;

SPB = (ts_max(high,52) + ts_min(low,52))/2

我相信从成交量来理解和应用技术指标将有助于我们更好地理解阿尔法. 文章将持续更新。 希望老师朋友们能够提出更多的指标。 谢谢

---

## 讨论与评论 (4)

### 评论 #1 (作者: Nguyen Dang Huynh(HN14753), 时间: 2 years ago)

感谢您分享这些有用的知识

---

### 评论 #2 (作者: TN48752, 时间: 2 years ago)

非常感谢您的支持,  [HN14753](/hc/en-us/profiles/13678373208599-HN14753)

---

### 评论 #3 (作者: deleted user, 时间: 2 years ago)

这篇文章确实质量很高而且很详细。 非常感谢您与全班同学的分享

**17. 我想提供唐奇安通道指标 (Donchian Channels)**

**Link:  [https://www.investopedia.com/terms/d/donchianchannels.asp](https://www.investopedia.com/terms/d/donchianchannels.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Donchian Channels
> JTOO
> 2
> J00
> J40 0
> J0 O
> J20 C
> JIO0
> JOO
> 2@
> 260OO
> TTO OO
> ZEO O
> AIO
> ZI0O
> DUI O
> TradingView



> [!NOTE] [图片 OCR 识别内容]
> The Formula for Donchian Channels
> UC = Highest High in Last N Periods
> Niddle Channel
> ((UC +IC)/2)
> LC
> Lowest Low i Last N periods
> There:
> TC
> Challlel
> N
> Number ofminutes; Iours;
> Teeks; months
> Period =Linutes; holrs;
> Veeks;
> Ionths
> LC
> Lomer channel
> Upper
> days;
> days;


UC = ts_max(high,window);

LC = ts_min(low,window);

MC = (UC + LC) /2

**18. Commodity Channel Index (CCI)**

**Link:  [https://www.investopedia.com/terms/c/commoditychannelindex.asp](https://www.investopedia.com/terms/c/commoditychannelindex.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Typical Price
> JIA
> COI
> 015 X Nean Deviation
> There:
> Typical Price
> Sisi((High + Low + Close) = 3)
> 卫 = Number Of periods
> MIA
> Moving Average
> Moving Average
> (Sisl Typical Price) 士 卫
> Nean Deviation
> Cizl
> Typical Price
> MIA |) =卫


window = 20;

TP = (high+low+close)/3;

MA = ts_sum(TP,window)/window;

MD = ts_sum(abs(TP-MA))/window;

CCI = (TP-MA)/(0.15*MD)

**19. Candle sticks**

**Link:  [https://www.investopedia.com/terms/c/candlestick.asp](https://www.investopedia.com/terms/c/candlestick.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Candlestick
> ['kan-dal- stk]
> A
> type of price chart used
> in technical analysis that
> displays the high, low,
> open,and
> ofa security fora
> specific period。 
> Investopedia
> closing
> prices


group_zscore(( close - open )/(high - low), subindustry)

**20. Keltner Channel**

**Link:  [https://www.investopedia.com/terms/k/keltnerchannel.asp](https://www.investopedia.com/terms/k/keltnerchannel.asp)**


> [!NOTE] [图片 OCR 识别内容]
> Upper Band = EMA
> (ATR X multiplier)
> Middle Band = EMA
> Lower Band = EMA
> (ATR X
>  multiplier)


EMA = ts_decay_exp_window(close,14);

window = 14;

TR = max(high-low,abs(high-ts_delay(close,1)),abs(low-ts_delay(close,1)));

ATR = ts_sum(TR,window)/window;

Multiplier = 2;

Upper_Band = EMA + (ATR x multiplier);

Middle Band = EMA;

Lower Band = EMA - (ATR x multiplier);

请继续更新

---

### 评论 #4 (作者: TN48752, 时间: 2 years ago)

非常感谢您对知识的贡献,  [TK95999](/hc/en-us/profiles/18243496991767-TK95999)

---

