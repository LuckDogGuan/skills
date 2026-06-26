# 【Alpha灵感】股票推荐系统-随机贴现现金流Alpha Template

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】股票推荐系统-随机贴现现金流Alpha Template_34912030967319.md
- **作者**: RZ39578
- **发布时间/热度**: 9个月前, 得票: 10

## 帖子正文

## **【Alpha灵感】股票推荐系统-随机贴现现金流**

### **Idea想法**

通过随机折现现金流构建企业公允价值分布，计算当前企业价值处于企业公允价值分布中的位置，判断当前企业价值是否被低估，高估，决定买入，卖出。

论文链接： [[L2] Research Paper 12 Stock Recommendations from Stochastic Discounted Cash FlowsPinned_15770966939671.md]([L2] Research Paper 12 Stock Recommendations from Stochastic Discounted Cash FlowsPinned_15770966939671.md)

### **原文逻辑**

1. 通过企业未来现金流 作为自变量，企业收入的对数作为因变量构建模型
2. 将所得模型放入蒙特卡洛模拟得到随机现金流分布
3. 通过代入企业随机现金流分布到DCF赋值模型，得到企业价值分布
4. 再计算企业价值分布-各项成本得到股票价值分布

带入当今股票价值，计算其在分布中的位置，决定是否买入，卖出


> [!NOTE] [图片 OCR 识别内容]
> Ch:=
> WOPII
> Du.1
> CIPL{
> JIC
> 末现金
> MII
> TOPIdenole  (le Iwetopernle
> Afer
> UI deprentonnn
> IIIIII
> tization  CIPE{
> Capital ependitre and JIrC
> the change
> the Workln capital
> Iu tu; VOPIT Ca be obtind fotu the earwiug before iterest,
> LC
> deprocjatiou
> ar nmortimntion EBTTD A Ising the relfion NOPAT
> (LRITD !
> Du,1I-11
> To
> TIcle
> IpIosonts the
> narginal tax rate。
> T drri the Rm prCCnt Value fom esti
> Ulater tutI Calsh tu.
> TILT
> twuptlouegy First.
> IoIWUaCUCUUS CUst OcNpitl
> 11SI
> disrot ftre Cnsh Hnw,
> The csl
> Capitgl
> Compmterl
> welghtel
> ULCTUIC
> tlo Ccst
> equity。 afterta
> 11131
> ofdcbt
> Cost rf
> prcfeio stocks。
> Sccond
> TT Ie Ith other stirre
> Iteratire Keg
> DamoTan
> [UUU
> WIU
> Cowsidlor
> [U-SLIUC
> uodol
> USIUI
> thnt
> UI3t
> datc 工 >
> ud
> Dopomla』
> growth raler
> Will
> k such (hal
> [oral
> 2T i
> CFti
> C
> (+9
> Thls auming that a the random quantite are defined m
> tltered probabilit
> (F(FJP. for
> poesible ttur rcalization
> Csh Hows CFlu) vith
> ! th
> HSSLUIHIUI
> Irw pren
> VJwe TnL
> DCF估l企业忻_楔
> Tla)
> CElI
> CFJty
> 
> 1 +N
> (1 + KITI
> ptil
> 18,
> AI
> N
> TIICL
> S


**模拟结果**

**
> [!NOTE] [图片 OCR 识别内容]
> LC Pl09-07-91
> Loil 201709-71
> Lo P2010029
> TC
> 401919
> 9
> Pigwre
> Distribution o[ tle logaritl of the Jair ualue listrihlion [or Booking Holdings
> Inc; (ridker BKXG) computerl at diferent dates; The rd Jottol lines indicate the markot
> price AI the enltion dnl
> shurw to obtain tle Jir volic ilrihlion
> Uwder tle Ipothesis of tle wodel B[WI
> roprcents the traditional point-wisc prSCII waluC estimate o[ corp
> slares, Figwre凹
> shos (he logarth O[ the fr
> Vluo Jitibution [or
> Holdings Iuc。
> (tickor
> BKTG) cowputed a Jilfereut dates.
> Tbe rel dottel liues udicate the Iaket loe-price
> tle evalualiou dale。
> A the cud ol the hrst quarter i ?009。
> the compau Tesults
> heivik wderalued。 while i results owly mildly uderwulued i 2013 Ql ad 2018 Q1
> Bookg
**

可以看到论文中的推荐系统可以准确判断当前 股票价值在公允股票价值分布中的位置

### **概念解释**

**1 企业价值**

> 完全收购一家企业，市场愿意付出的钱

这里企业的价值并非看资产值多少钱，而是看企业制造利润的能力。

**2 折现现金流（DCF)**

> 把未来的现金流 按照资本成本 折算为当前价值。

假设银行每年利率3.5%,那么1年后的103.5跟现在的100是等值的，dcf就是把未来的现金流折算为当前价值，

用于评估企业值多少钱。

**3 加权平均资本成本(Weight Average Capital Cost)**

> 表示每年向资金来源付出的回报占总资本的比率

一家公司如果单向银行借钱，利率3.5%，那么3.5%就是企业的加权平均资本成本。

但企业的融资来源一般会有多个,通过计算各来源资本占比以及其预期回报可以得到 企业的加权平均资本成本（wacc)。


> [!NOTE] [图片 OCR 识别内容]
> D
> WACC =
> Re | +
> Rd * (1-0)
> 区 +D
> (区+D
> WACC is the rate that a business is expected to pay to
> finance its assets
> 剡泞 @Tc Firrics


- Equity:股权资金
- Debt:债务资金

**4 蒙特卡洛模拟**

> 通过不断地随机，逼近事物原先的值

[https://www.bilibili.com/video/BV1fo4y1977h](https://www.bilibili.com/video/BV1fo4y1977h)

**5 DCF估值模型**

**
> [!NOTE] [图片 OCR 识别内容]
> W(w)
> CHilw)
> CFIlw)(1 +9)
> =5
> (1+k)
> (1 +k) ( -9)
**

在这个模型中，企业价值由未来能产生的现金流决定，第一部分的累加表示 企业在n年内的现金流折算为当前的企业估值-part1，第二部分表示n年之后的现金流折算为当前的企业估值-part2。

### **Alpha构建**

**1 用回归模型拟合[未来现金流&企业收入]的关系**

```
cf_margin = (ebitda-capex-(working_capital-last_diff_value(working_capital,504)))/log(revenue);a = ts_regression(log(revenue),cf_margin,1080,lag=0,rettype=2);b = ts_regression(log(revenue),cf_margin,1080,lag=0,rettype=1);
```

**2 用市场均值作为随机值模拟蒙特卡洛**

```
x= group_mean(cf_margin,1,market);# simulate_log(revenue)y=a*x+b;cf_random = y*cf_margin;
```

**3 计算 加权平均资本支出（WACC)**

```
# wacc# risk_market:市场风险risk_market = ts_delta(pv13_revere_index_value,1)/ts_delay(pv13_revere_index_value,1);# re:股权风险re = fnd6_optrfr+fnd6_beta*(risk_market-fnd6_optrfr);e = fnd6_mkvalt;d = debt_lt+debt_st;# 债务风险rd = fnd6_intpn/d;# 税收比率tc = income_tax / pretax_income;v = e + d;k= (e/v)*re + (d/v)*rd *(1-tc);
```

**4 通过DCF估值模型计算 公允企业价值分布**

```
day=60;g= k/5;enterprise_value_random = ts_mean(cf_random/signed_power(1+k,ts_step(day)),day)*day + cf_random*(1+g)/(signed_power(1+k,day)*(k-g));
```

5 计算当前企业价值位置并根据位置确定 分配权重。

```
ev_random_mean = ts_mean(enterprise_value_random,1080);ev_random_dev = ts_std_dev(enterprise_value_random,1080);alpha = (enterprise_value-ev_random_mean)/ev_random_dev;#此处0.67，以及1.15为论文中0.25与0.125的换算trade_when(abs(alpha)>0.67,if_else(abs(alpha)>1.15,-2*alpha,-alpha),-1)
```

### **Alpha初步结果**

**
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 7SLUK
> SCCCK
> ~ SCC
> T12018
> Pnl .1 57.85k
> 45
> Jul'旧
> J5 +9
> Jultg
> V 20
> J
> l 21
> Jul 21
> 14'22
> J22
> 77
**

**
> [!NOTE] [图片 OCR 识别内容]
> I5 Summary
> PTlC O
> TUrsUt
> 0.87
> 3.593
> 39.6235
> 50.2896
> 220.49960
> Sho
> Uurw
> Fw
> RhT
> Orwwn
> Nnon
> U Cot
> StlCo
> 1471
> 175
> S-
> 75
> 1575
> 41553
> 09
> 1155
> 195
> 41
> T0
> JCT
> 350S
> 4157
> m
> 1.597
**

可以看到总体结果还是不错的，作为基本面alpha turnover也很低，说明企业公允价值分布的计算是有效的。

但sharpe太低了，推测是交易频率门槛过高导致的，考虑降低交易门槛以及增加对于偏离公允价值企业的反应

#### **降低交易门槛+提升alpha对于信号反应**

**
> [!NOTE] [图片 OCR 识别内容]
> Summary
> PeTiC
> SCTJR
> ATTCTOVC Uta
> 0.74
> 3.94%
> 1.22
> 33.9196
> 50.283
> 171.S99o
> K
> T
> S
> N
>   [
> S
> U Cmnt
> Kno
> 13
> SUo
> 5245
> T.3
> 45N
> 5613
> C
> 4139
> IU
> 35
> 7
> SUS1。
> 19S5
> 95
**

在拉低门槛，以及拉高反应后，表现还不如之前，推测是更改了原论文的推荐比例问题，所以这里打算单独提升alpha对于极值的反应.

#### **单独提升alpha对于信号反应**

**
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> PoTiod
> ICe
> TZRTeRre Urn
> 0.74
> 3.949
> 1.22
> 33.919
> 50.2895
> 171,99900
> Shc
> Te
> Filn
> Nl
> DrHw
> LM
> Uo (m
> Sh (
> 11477
> 5T
> 5-5
> 33.
> 15+4
> N
> 1211
> 71
> TEN
> -5541
> JO5
> TTE
> 4902n
> 355
> T51
> 7975
> 35998
**

结果还是一样，所以没有办法通过简单的降低交易门槛，拉高alpha反应的方式 提升alpha表现，所以接下来打算引入论文中的 横截面推荐系统，将其与当前的单股推荐系统结合得到更强的信号。

#### **检查 ev_random信号是否有效-排除结果来自trade_when()**

不过在此之前，需要再检查算出的ev_random分布是否有效，于是将其换成data中的enterprise_value,结果如下


> [!NOTE] [图片 OCR 识别内容]
> 415 SUI


说明 计算出来的ev_random为有效值。

### **改进Alpha**

**引入论文中横截面推荐系统**

```
log_revenue = log(revenue);cf_margin = (ebitda-capex-(working_capital-last_diff_value(working_capital,504)))/log(revenue);a = ts_regression(log_revenue,cf_margin,1080,lag=0,rettype=2);b = ts_regression(log_revenue,cf_margin,1080,lag=0,rettype=1);# random_value 用市场均值作为随机值x= group_mean(cf_margin,1,market);# simulate_log(revenue) y=a*x+b;cf_random = y*cf_margin;# wacc 加权平均资本支出risk_market = ts_delta(pv13_revere_index_value,1)/ts_delay(pv13_revere_index_value,1);re = fnd6_optrfr+fnd6_beta*(risk_market-fnd6_optrfr);e = fnd6_mkvalt;d = debt;rd = fnd6_intpn/d;tc = income_tax / pretax_income;v = e + d;k= (e/v)*re + (d/v)*rd *(1-tc);# DCF估算企业价值day=60;g= k/5;enterprise_value_random = ts_mean(cf_random/signed_power(1+k,ts_step(day)),day)*day + cf_random*(1+g)/(signed_power(1+k,day)*(k-g));# 计算当前企业价值所处位置ev_random_mean = ts_mean(enterprise_value_random,1080);ev_random_dev = ts_std_dev(enterprise_value_random,1080);alpha = (enterprise_value-ev_random_mean)/ev_random_dev;# 单股票推荐系统ssq = trade_when(abs(alpha)>0.67,if_else(abs(alpha)>1.15,-2*alpha,-alpha),-1);# 横截面股票推荐系统neu_rank_alpha = group_neutralize(rank(alpha),densify(industry));csq = trade_when(abs(neu_rank_alpha)>0.1,neu_rank_alpha,-1);csq+ssq
```


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Perlod
> 4TeGate Onta
> 0.92
> 3.524
> 40.939
> 50.2895
> 232.8590
> Shorme
> Tl
> Frey
> Rt
> CrU
> Nyn
> L Cwl
> CtCol
> 131
> C
> 
> 2S
> 15SS
> 53
> 5
> 575
> -0
> 71
> -57
> 35.355
> 70512
> -51
> ~3755
> 189957


可以看到，sharpe增加了，但总体增加不多，可能是横截面推荐系统并没有引入更多的有效信号。

**问题**

1. 如果我后续还要继续改进该alpha应该从哪些方面入手？
2. wacc（加权平均资本支出）的计算实在是很繁琐，有没有什么数据字段可以替代的？
3. 这种跟着论文复现的alpha，应该不具有抽象为模板的能力，那么我们如何从这些论文中获得我们的alpha模板呢？

---

## 讨论与评论 (5)

### 评论 #1 (作者: AH18340, 时间: 9个月前)

感谢大佬分享，太专业了，没大看懂- -！

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #2 (作者: LR93609, 时间: 9个月前)

感谢分享，非常详细的财务成本分析，我有几个疑问，请帮忙解答：

**1. margin计算方法：** 如果用了log就变形了，建议去掉。

比如，1/20=0.05，相当于5%，对于margin来讲是合理的；

1/log(20)=33%，完全是两个结果，而且也不成比例。

```
cf_margin = (ebitda-capex-(working_capital-last_diff_value(working_capital,504)))/log(revenue);
```

**2. 市场风险计算：** pv13_revere_index_value：Value of specified index for the date？与市场风险是两码事。

建议使用：systematic_risk_last_360_days，Systematic Risk Last 360 Days

```
# risk_market:市场风险risk_market = ts_delta(pv13_revere_index_value,1)/ts_delay(pv13_revere_index_value,1);
```

**3. 估值计算：** 按照基础公式，后半部分是比值，你算成了均值，可能是笔误，建议调整

```
enterprise_value_random = ts_mean(cf_random/signed_power(1+k,ts_step(day)),day)*day + cf_random*(1+g)/(signed_power(1+k,day)*(k-g));
```

总之，估值模型是相对科学的，analyst和model里面都有静态或动态估值模型，确实有不错的表现。

建议，如有时间，再完善一下，说不定会是一个不错的Alpha，加深对财务成本的认识。

再次感谢分享，随白璧微瑕，但可圈可点，做了很多不错的尝试。

--------------------------------------------------------------------------------------------------

凡事发生，皆利于我；愿我所愿，尽是美好

--------------------------------------------------------------------------------------------------

---

### 评论 #3 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

谢谢分享。想问一下这个模板回测时间正常吗？

我发现如果数据字段里面数据很多，即使是USA，EUR的ts_regression回测时间会很长，GLB则是报利用资源太多的错误。不知道大佬有没有遇到同样问题。

---

### 评论 #4 (作者: RZ39578, 时间: 7个月前)

[顾问 YH25030 (Rank 31),](/hc/en-us/profiles/28941108652823-顾问 YH25030 (Rank 31))

这个模板是之前用户阶段写的，回测时间只有5年。当时在写alpha的时候，也遇到了operator使用过多的问题，特意压了几个operator。

---

### 评论 #5 (作者: RZ39578, 时间: 7个月前)

[LR93609](/hc/en-us/profiles/30244554462231-LR93609)

好的，谢谢建议。 现在各类知识还比较薄弱，等最近补足后，再尝试完善这个模板。

---

