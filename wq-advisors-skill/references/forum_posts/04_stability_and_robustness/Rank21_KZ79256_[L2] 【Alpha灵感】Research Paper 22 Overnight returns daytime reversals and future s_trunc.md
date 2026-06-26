# 【Alpha灵感】Research Paper 22 Overnight returns, daytime reversals, and future stock returns

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Research Paper 22 Overnight returns daytime reversals and future stock returns_20239918193303.md
- **作者**: SL57524
- **发布时间/热度**: 2 years ago, 得票: 13

## 帖子正文

两种不同的客户往往主导着隔夜和日间交易时段，这两种投资者群体的持续过剩需求可能会造成每天的“拉锯战”，导致两个时期的回报逆转模式反复出现。例如，隔夜客户的过度需求可能倾向于将价格拉向一个方向，最终导致开盘价格与相反客户的观点不一致。因此，这些持反对意见的客户可能会在日间交易中拉回价格，并在当天收盘时出现交易日逆转。


> [!NOTE] [图片 OCR 识别内容]
> Close
> ?
> RET_OCid
> Open
> 1
> Pid
  
> [!NOTE] [图片 OCR 识别内容]
> 1十
> RET_
> 1
> I+RET_OCid
> RETid
> COid


先通过日间间隔、日内开收盘价算出daytime returns 和overnight returns

将 一个a negative daytime reversal 定义为 a positive overnight return that is followed by a negative  daytime return.

计算负逆转negative daytime reversal 的天数与第t个月的总交易日数的比率，并将该变量表示为NR

而负反转的异常频率AB_NR =  NR除以过去12个月的NR

最终作者指出，由于在daytime 交易者的过度反应，AB_NR越高，未来回报越高


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAN
> Simulate
> Alphas
> Data
> " Competitions (2)
> Events
> Learn
> y
> Refer a friend
> Simulation 10
> Simulation 5
> Simulation 9
> Simulation 12
> Simulation 13
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation
> 1
> RET_OCplUSI
>  (close) / (open) ;
> Chart
> Pnl
> 2
> RET_OC
> RET_OCplusI
> 1;
> 3
> RETplUSI
> (close) / (ts_delay (close,1) ) ;
> 4
> RET_CO
> (RETplusI / RET_OCplus1 )
> 1;
> 5
> # We define
> negative daytime
> reversal
> as
> positive overnight
> return that
> is
> 9,00OK
> followed by
> negative daytime
> return.
> NUM
> if_else(and ( RET_CO
> 0, RET_OC
> <
> 0),
> 1, 0);
> 8 0OOK
> NR
> Sum(NUM,
> 20)/20;
> 8
> AB NR
> NR/ts_mean (NR,
> 240);
> #stocks
> involved
> in
> more
> intense tug of
> War,
> proxied by
> higher monthly
> 7,00OK
> frequency of
> these negative daytime reversals,
> have significantly higher future
> returns.
> 6,00OK
> 10
> 0.5xrank (-returns ) +0.5*rank
> AB NR)
> 5,00OK
> 4 0OOK
> 3,00OK
> Z,0OOK
> 1,00OK
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
> Clone this Alphain a new tab
> Example
> SMate
> Visualization
> $
> Add Alpha to
> List
> Check Submission
> Submit Alpha 
> MM
> tS_s


最后得出的alpha ，但这个alpha 需要和-returns（或者其他指标）拼在一起才能提交，但是他的corr很高，之前被别人提交过


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAN
> Simulate
> Alphas
> Data
> " Competitions (2)
> Events
> Learn
> y
> Refer a friend
> PROD CORRELATION:
> Maximum Pearson correlation coefficient from
> Simulation 10
> Simulation 5
> Simulation 9
> Simulation 12
> Simulation 13
> comparing a given alpha to all other alphas
> LEARN
> DATA
> ANOIYIOUS
> TOPSUUO
> submitted byall WorldQuant BRAIN users
> 2./9
> 539.8200
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation
> 1
> RET_OCplUSI
>  (close) / (open) ;
> Prod Correlation
> Highest Correlation
> Last Run: Sat; 12/30/2023,7:34 PM
> 2
> RET_OC
> RET_OCplusI
> 1;
> 3
> RETplUSI
> (close) / (ts_delay (close,1) ) ;
> 1
> 4
> RET_CO
> (RETplusI / RET_OCplus1 )
> 1;
> 5
> # We define
> negative daytime
> reversal
> as
> positive overnight
> return that
> is
> IOOM
> followed by
> negative daytime
> return.
> NUM
> if_else(and ( RET_CO
> 0, RET_OC
> <
> 0),
> 1, 0);
> NR
> Sum(NUM,
> 20)/20;
> IM
> 8
> AB NR
> NR/ts_mean (NR,
> 240);
> #stocks
> involved
> in
> more
> intense tug of
> War,
> proxied by
> higher monthly
> 鼍
> frequency of
> these negative daytime reversals,
> have significantly higher future
> IOk
> returns.
> 晷
> 10
> 0.5xrank (-returns ) +0.5*rank
> AB NR)
> }
> 100
> 02
> 0? &? 0? 0^
> 0 0?
> 09
> 9
> @
> 03
> 0@一
> 8:
> 0:
> IS Testing Status
> PASS
> Sharpe Of 2.38 is above cUtoff of 1.58_
> Fitness of 1.05 is above Cutoff of 1
> Turnover of 49.179 is above cUtoff of 19_
> Clone this Alphain a new tab
> Turnover of 49.179 is below CUtoff of 709
> Example
> SMate
> Visualization
> T
> Add Alpha to
> List
> Check Submission
> Submit Alpha 
> tS_s
> -0.9
> -0.8
> -0.7
> -0.6
> -0.5
> -0.4
> -0.3
> -0.1
> 0.0
> 0.5
> 0.8
> 1.0
> :
> -0.1.
> 0.2..
> 3
> 0.4.
> 0.7..
> 0.8.
> 0.9..
> 0.0.
> -1.0.
> %
> -0.4.
> -0.3.
> 3
> -0.9.
> -0.7.


单独的AB_NR表现如下：
 
> [!NOTE] [图片 OCR 识别内容]
> Settings
> USA/D1/T0P3000
> Convert to Multi-Simulation
> 1
> RET_OCplusI
> (close) / (open) ;
> Chart
> Pnl
> 2
> RET_OC
> RET_OCplUSI
> 1;
> 3
> RETplUSI
> (close) / (ts_delay ( close,1) ) ;
> 4
> C0
> (RETplusI / RET_OCplus1 )
> 1;
> 5
> # We define
> negative daytime
> reversal
> as
> positive overnight
> return
> that
> is
> followed by
> a
> negative daytime
> return。
> NUM
> if_else(and (RET_CO
> 0, RET_OC
> <01,
> 1,
> 0);
> 3,500K
> NR
> Sum(NUM,
> 20)/20;
> 8
> AB_NR
> NR/
> mean (NR,
> 240);
> 9
> #stocks
> involved
> in
> more intense tug
> 0f
> War, proxied by
> higher monthly
> 3,000K
> frequency of these negative daytime reversals,
> have significantly higher future
> returns.
> 10
> AB NR
> 2,50OK
> Z,0OOK
> 1,5OOK
> 1,00OK
> SOOK
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
> Clone this Alphain a new tab
> Example
> Simulate
> Visualization
> T
> Add Alpha to a List
> Check Submission
> SUbmtApha
> RET_C
> tS_5
> ts_r


采用其他指标替代- returns可以降低correlation, 但是我的疑惑在于，实际上这个idea本身包含的这个东西（AB- NR）其实是没有达到特别好的要求的。在Brain平台中，发现某个idea不能提交，然后再补充一个东西使得其可以提交，但在这个因子被实盘使用时，难道不是有效的只有原本的idea部分？

那么实际上有很多研报和论文中有效的因子都是通过不了全部检验的，那么这样不会导致在最后用一个复杂多因子模型的时候，缺失那些重要的，但是单独使用表现不佳的因子？

换句话说，有很多研报和论文构建的是多因子模型，如果想要复现这些观点，该如何在Brain中表达？

---

## 讨论与评论 (1)

### 评论 #1 (作者: KJ42842, 时间: 2 years ago)

1，大部分论文不会给你一个可以直接提交的Alpha，这是一个非常常见的现象，你可以在学术论文中已经有效的idea上进行完善，比如说这篇论文中说overnight和daytime之间对立拔河越强烈，之后的reveral越显著。那么是否可以思考如何将其之间的对立程度更细致的刻画？一个大的overnight的跳空高开+一个大的daytime的高开低走是否比一个小的overnight的开盘上涨+一个daytime小幅收跌要更intensive? 既然是多空之间的对立，在价格的基础上引入成交量是否能将对立刻画的更加深刻？这其实就是量化研究的要做的事情，在这个过程中研究水平得到提高。

2，多因子的Operator已经其他更多的Operator会在不久后加入，敬请期待！

---

