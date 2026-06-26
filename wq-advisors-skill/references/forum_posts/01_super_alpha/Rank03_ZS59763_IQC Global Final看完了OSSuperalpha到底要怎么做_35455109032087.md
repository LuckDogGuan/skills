# IQC Global Final：看完了OS，Superalpha到底要怎么做？

- **链接**: https://support.worldquantbrain.comIQC Global Final看完了OSSuperalpha到底要怎么做_35455109032087.md
- **作者**: worldquant brain赛博游戏王
- **发布时间/热度**: 8个月前, 得票: 62

## 帖子正文

IQC Global Final系列：

[IQC Global Final：Superalpha的OS都长什么样？ – WorldQuant BRAIN](IQC Global FinalSuperalpha的OS都长什么样论坛精选_35377525887255.md)

Superalpha的OS比预期中的还要差，OS/IS达到0.3的都很少。在这种情况下，到底要怎么做Superalpha？

## 对于sa的建议：

### 一位来自韩国的研究员建议如下：

- 多选因子：靠着大数定理进行内部对冲
- diversity，diversity，diversity
- combo要有实质逻辑，不超过三个operator
- turnover小于18%（时间不够，没有追问为什么是18而不是其他）
- combo_a三个算法中，他认为算法1是 最好的，三个算法究竟是什么，不能说
- is很高，sharpe10+，20+，只要做好diversity，不刻意过拟合，完全ok

### 跟kunqi老师讨论的一些小思路：

- 有一些高production correlation的因子，可能在因子池内，与其最高correlation的因子只有几个，十几个，在选择时也未必能选到。所以针对高correlation的因子，可以将其选出后，根据select到因子池的内部相关性进行加权（这个可以通过selfcor进行筛选控制，learn文档里面有一个combo讲了这个事情，但我用下来跟等权没有差异，可能是方法不对）
- 因子是容许亏钱的，亏钱因子就下掉
- quantity is quality，wq用的因子组合包含上万个因子，足够的diversity，足够的quantity，可以保证足够的quality·

### 跟weijie老师的讨论：

- asi的sa，j既要关注kor，如果kor和jpn表现近似，有performance就可以接受，哪怕只用jp的部分，也是可以的
- robust test，只要拉decay就能解决
- 因子的表现随着operator呈现双峰分布，op多，可能是手作的因子，质量也是有保证的，但这个阈值的确定要额外考虑

### 跟英区顾问的讨论：

- model数据实在是不敢用，选择时都会剃掉（个人感觉，model数据有一些还是很“讲道理”的，不是十足的黑箱，例如mdl77这种，还是可以放心用）
- sa的author字段，他是通过英区排行榜，看一些combine好的人，他们的平均correlation是多少，针对性地用这些人的因子（设置不同的区间，但他是master，叠加上英区人少，所以还算ok）
- 接前两点，他表示，如果按照author平均sharpe高于2.25来筛选，可能很多因子都是mdl数据，靠着mdl数据将平均sharpe拉到2+，这就是为什么他推荐用第一个点的原因

### 跟其他顾问的讨论：

- 用turnover分层，用count分层，他们也有在做
- diversity，diversity，diversity

### 官方培训：


> [!NOTE] [图片 OCR 识别内容]
> Super
> Su 5
> Sper SMUUUOG
> SUr
> Sollngs
> USAIDTITOPAOOO
> SotonE'Rreeon
> else(n(atacoegonles
> optton
> Turoer
> 10.1
> Clse(n(aatacateRorles
> Tunonntal
> tunover
> 6s, datafield_count
> 5
> C9oo鼍oo


根据数据类型的特性针对性来选择，fnd数据的turn普遍低，option数据turn普遍高，设置ifelse条件

## 
> [!NOTE] [图片 OCR 识别内容]
> no(avorlre)
> 
> TCOJor
> GREEN
> Otfiold Cont
> TUNNONCI
> aSs
> ComboEpsso
> Stoks
> Bencmte Stt(olpw);
> U
> CeducoNowersl
> Lolt c0r(stats roturn,252),
> CONSht
> 1(111)


按照ic，ir等经典指标进行加权


> [!NOTE] [图片 OCR 识别内容]
> K
> USAIDITOPAOOO
> Selocton Exprnlon
> not(hvorl)
> (color
> ~GREEN
> Otliold cont
> 2
> TTOUCF
> 9.
> Co Soo
> Combo epros on
> Stocs
> Bonomte_Stats(alpn)
> 1/5_std cov(stots,roturns,7521
 低波组合

### 选手的组合思路（不全，有些人没有放）


> [!NOTE] [图片 OCR 识别内容]
> Allselection
> Equal Weight
> unoxmonlalITe
> ACVoI
> 1.Corr
> Alrondy considor
> Dlverslfled pool
> GIorslcaton
> Conslder Market
> 2.IR
> N Dhovo (oethewo
> A
> Strlctsubmlssion
> Robust
> Interesr Rate
> NohIntorosr
> LowIntoro
> 551
> 45
> Prevent unprdictable Risk
> Buslness Cycle
> Estimatlon error
> Expnson
> Rroosson
> Overtitung
> O
> A0
> Nolse Effoct
> @g



> [!NOTE] [图片 OCR 识别内容]
> Super Alpha Selection And Combo
> 74
> Wan4altot
> 80
> Socorrolaton
> Super AlphaScore
> 100
> TUroVr
> Performance (sharpe Ratio) / Hidden Risk
> 94
> HowIt Work:
> Hawqwaley
> Performance: Reward hleh, rlsk adjustedreturns
> (Sharpe Ratio)
> 137
> Sgtes
> Hidden Risk: Penallze "streaklnessi (heh
> correlaton), WhichisViewedasaslenOTfragllity
> andhgh modelrsk
> 165
> ronkt5



> [!NOTE] [图片 OCR 识别内容]
> Problemin Whole alpha pool:
> Highly correlated
> Selectionidea:
> Highturnover
> Prioritize Iower self-corr
> Filter fortoo highllow
> High drawdown
> turnover
> Diferent universe
> Only focuson TOP SOOOalpha
> Generate stats
> Hnaloutput
> Combologic:
> Extract returns
> Oawdown
> Signal Smoothing
> Ani
> Correlation
> Momentumbooster
> 500re



> [!NOTE] [图片 OCR 识别内容]
> Selection Logic:
> Combo Logic:
> Fundumenul;
> Analysl
> Option
> Prce
> Volumo
> Sentiment
> I-yenr correlntion motrix
> Tumover
> Sums squared correlions Io nl others
> mnge < 7%
> Dlfeld
> Allocale more wcipht (0 unique alphas and down
> COUIL
> 10
> wvciehl crowded ones
> Count + short_counu)
> 1000
> Simultion universe nnd neutrnlizntion;
> Potentinl improvement:
> TOP3000
> Addnn RR Ierm
> Subindustry
> Widen brendth Ihreshold (0 150-250
> Iong


## 
> [!NOTE] [图片 OCR 识别内容]
> SoloclonLozk
> Combladontodk
> Boundingtheturnover
> 10 %
> TUIOVCTL3OU
> Dovlalonolroturn
> Corrclatlon Mthlnthe pool
> Corrcluon
> 44
> Furtherrocurch
> Ccorlo
> Lonandshortcouns
> Comlatedwlhdrawdown
> Slmolo
> Inonoon


## 
> [!NOTE] [图片 OCR 识别内容]
> SuperAlpha Selection Expression Logic
> OUCome:
> Goal: Maxme 
> RemoVed02
> KeptONV
> SelectedNOT
> Dlscardedx
> UIersICaton
> Corelatod
> Improved
> Fovorltetoavold
> Ophas
> Nhas
> VCIIOns
> OVertUNR
> Ceaner dwerse
> Dool
> SuperAlpha Combo Expression Logic
> Down Wolehtod
> Up wolhod
> Goal: Dlerslly
> Calculated 250.
> hgh IC
> UNOUC ONs
> SIarpo 483 >
> Turhern
> daylcloreach
> (redundant)
> Ou
> 
> 5.48(+13.5% )
> Combo staRe
> alpha
> Slenals
> (


## 
> [!NOTE] [图片 OCR 识别内容]
> Selecton Logie
> Synonymous WUh RobwIoss Checls (ommed in Research Process:
> SIwlton Ulvere; TOP30O0
> Correlaton
> <0.0
> Nculallznlon: Industry
> Turnover < 1096
> Stock Counl
> Universe
> Additional Crilerin:
> Curate Wrnover Glens for datasets morc pronc to mispricing (Pricc Volumc, Volatlit)
> Filter out Alphas thnt ulilize modlolllsels
> Reduceoverntling by limiting maximwmdansels to 4 and muximmopemlors to 9
> Qombo LoBie
> to Alphas wth a Lower Correlntion, and apply less to those with a higher correlation
> Apply more woighl
> Compare correlation over a longerlookbnck (3 years)
> Increnses accurcy of weights being
> to Nphas with lower correlation
> Lnstemcompnnson Improves porfolio diyefifcition
> Rowentinllmproyemcnts
> Personally handpck Alphas based on custom categones
> Redomaymmgafcritena to icrense qwnofseleciom
> in Comlo Kpcesson
> Rsvecomreed plcing moreweinhls t leh-peffomming Alphzs
> (OUIO
> applied


## 
> [!NOTE] [图片 OCR 识别内容]
> Verormanoe
> Stpersac strateey
> Selection Expression
> Combo expression
> 1 e guspicious about 2022overtitting
> 1.Lowtmover
> 2LLow Self-corelation
> CausingOxtromely hch sharpe
> 2Stblltyover retwm
> 3igh coverage
> 3.Avolid uncortalntyofrlsk
> 4Low Cowplexiby
> Combo Expresslon
> I38Gturnoverz0.025) )
> &&(selzcorrelationco.SGG
> turnoverco。
> count
> 8)8&(truncation=0.1N
> self_correlation
> 0
> 0)GG(operator
> IOwnGG


## 

## 但是！但是！但是！

sa的bias会比想象中的要严重。

bias主要来自于ra的bias，单个ra可能只有一点点bias，但在sa中可能会造成巨大的偏差。

即使ra是在正常拟合，组合起来的偏差也会收到影响

select要严格把控，杜绝过拟合因子，garbage in，garbage out

（所以没有sa拿weight的机会比ra多的说法，因为无法探明sa中究竟包含了多少bias，从os/is对比也能看出，品控不严，系统性的过拟合是很严重的）

---

## 讨论与评论 (3)

### 评论 #1 (作者: MY82844, 时间: 7个月前)

精华收藏

OS/IS达到0.3的都很少--这个很意外

---

### 评论 #2 (作者: QM70930, 时间: 5个月前)

收藏一下，有空研究

---

### 评论 #3 (作者: MW39826, 时间: 5个月前)

MARK

---

