# 【Alpha灵感】基于MCP提交的3个Short Interest 因子

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】基于MCP提交的3个Short Interest 因子_34407581314583.md
- **作者**: LR93609
- **发布时间/热度**: 10个月前, 得票: 87

## 帖子正文

**一、概述**

**Eur的short interest中共2个字段**

**shrt3_bar：** A rating on a scale of 1 to 10 that provides a simple indication of the level of demand to borrow a given stock, with 1 indicating a relatively low demand and 10 indicating a relatively high demand.

**shrt3_utilizationpercent_units：** The ratio between the number of shares on loan to the number of shares available for lending.

**二、MCP过程**

**1. 提交需求：提示词相对比较初级，只是简单的MCP命令**


> [!NOTE] [图片 OCR 识别内容]
> 任务 帮我分析 Fworlaquantbrain平台
> shrt3_utilizationpercent_units 字段的结构;生成椟版
> 39.1k/128.O1
> 50.11
> AIItasks completed!
> -5/5
> API请求
> 30,0067
> 用户要求我分析WorldQuant BRAIN 平台 shrt3_utilizationpercent
> units
> 字段结构并生成模板。这是 个关于金鼬数据字段
> 分析的任务。
> 我 要:
> 首先连接到NorldQuant BRAIN平台获取相关信总
> 2.分析 shrt3_utilizationpercent_
> units 字段的结构
> 生成相应的模板
> 让我先查看
> 下当前的工作环境。看看是否有相关的置文件或代码可以参考。从文件结构看。这是
> 个虽化因子分析的代码库;有
> 很多Python 文件和CSV数据文件。
> 我应该先使|MCF工具连接到WorldQuant BRAIN乎台来获取数据字段信息。
> 我笨要帮您分析WorldQuant BRAIN平台的 shrt3_utilizationpercent_
> units 字段结构井生成椟板。让我先连接到平台获取相关
> 信总。


**2. 执行过程：基于DeepSeek的MCP执行过程，全过程花费$0.11**


> [!NOTE] [图片 OCR 识别内容]
> AIItasks completed!
> 荭 5/5
> 我己经成功完成了对WorldQuant BRAIN 平台 shrt3_utilizationpercent_units 字段的全面分析,井生成了完整的模板和示例。
> 完成的工作:
> 1.字段结构分析
> 字段I0: shrt3_utilizationpercent_units
> 描逑:借出股票数虽与可供借出股票数虽之间的比孪
> 数据集
> Securities Lending Files Data (shortinterest3]
> 数据类型: VECTOR, 覆益孪10096
> 使用统计:136个用户
> 293个 Alpha因子
> 2.生成的模板文件:
> 点:!燕:g!点!:!趟烹:点t:Ry
> 完整的Python椟板类。包含基础表达式。高级策略和组合因孑
> 烹
> 燃:}烹点!R烹点烹!!?烹烹点烈8 :R
> 使用示例和BR4IN平台集成代码
> 点煦@#点!熊:熊熊煦 煦
> 详细的分析报告文档
> 3.关键特性:
> 做空情绪指标:高值表示做空兴趣强烈
> 多种策略适用:均值回归。动虽。相对强度等
> 高质虽数据:100%覆益孪
> 广泛伎用
> 组合性强:易于与其他因子结合
> 4.包含的Alpha表达式:
> 基础表达式:  直接伎用
> 排名。对数娈换等
> 高级策咯:  均值回归。动星。波动调整等
> 组合因孑: 与流动性。波动孪。市值等指标结合
> 5。使用建议:
> 适合做空恃绪分析和风险管理
> 推荐测试不同的时词窗口和中性化方法
> 注意数据延迟和极端值处理
> 这些模板可以直接在WorldQuant BRAIN平台上伎用。为您提供了基于借贷利用孪字段的完整alpha因子开发解决方案。


**3. 生成模版：MCP自动生成10多个高阶模版，都有信号，且自相关和生产相关性都不高**


> [!NOTE] [图片 OCR 识别内容]
> shrt3_utilizationpercent_units_example py
> shrt3_utilizationpercent_
> analysis.md
> WorldQuant BRAIN平台
> shrt3_utilizationpercent_units字段分祈报告
> 凹#
> Alpha因子模板
> WorldQuant BRAIN平台
> Shrt3
> utilizationpercent_units字段分析报告
> 字段解释
> ###
> 金融含义
> Alpha因子棋板
> ###
> 基础表达式
> Vac
> aVg(shrt3_utilizationpercent_units) `
> 直接使用
> rank(vec_avg(shrt3_utilizationpercent_units) )
> 排名处理
> Iog(vec_avg(shrt3_utilizationpercent_units )
> 对数娈换
> mean (vec_avg(shrt3_utilizationpercent_units),
> 5) `
> 移动平均
> ###
> 高级策略
> Python
> 均值回归策略
> ~Cs
> Zscore (Vec_aVg(shrt3_utilizationpercent_units),
> 20)
> 动量策略
> ts_delta(vec_aVg (shrt3_utilizationpercent_units ) =
> 相对强度策略
> rank (Vec_avg(shrt3_utilizationpercent_units )
> rank (Vec_avg(shnt3_utilizationpe
> 波动调整策略
> (Vec_aVg(shrt3_utilizationpercent_units 
> mean (Vec_aVg(shrt3_utilizationperc
> 拥挤度择时策略
> sign(ts
> I?ah
> Vec_avg(shrt3_utilizationpercent_units ),
> 580 )
> Mean (Vec_
> aVg(shr
> ###  组合町子
> Python
> 与流动性结合
> pank (Vec_avg
> shrt3_uilizationpercent
> Units
> rank(adv20)
> 与值结合
> VeC
> aVg(shrt3_utilizationpercent_units )
> CAP
> 回归组合
> regression_
> neut (s_Iog_IP
> Vec_aVg(shrt3_utilizationpercent
> units) )
> Iog_IP(Vec_
> 幅度限制
> ts_delta_limit (vec_avg(shrt3_utilizationpercent_units)
> Vec_avg
> shrt3_
> limi
> 推荐使用场景
> ###
> (空情绪指标
> Uhits
> bar),


**三、结果输出：根据MCP提供的模版，2个字段跑出来三个一起提交的因子**

**1. 拥挤度择时策略（模版原封不动）**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> o IS Summary
> TTOI
> 昵 sirele Datd Sel Rlra
> Pmer PlAI 
> I
> TURDTISHORTINTTRFCT
> 日VeC
> aVB(shrtJ_utilizatlonper Cent
> UI
> SUIOICC5
> Meal8
> ICBr
> 352
> ULUTULJt
> STJTC 
> T
> UTN
> 1.29
> 3.1096
> 0.52
> 2.,0095
> 2.4496
> 12.9096c0
> SIIUIaTIOI
> Settings
> Sm
> TI
> Ftn
> Feht
> Umwdown
> Vrn
> Im (mt
> St Cmk
> MhII
> FemO
> U
> Kl
> 0
> NIIChc
> Nmmh
> Tl
> Olhm
> U l
> N l
> 135
> 二
> ECUIR
> TCPZETD
> TSvorczslor
> U
> 159
> 1
> Sy:
> 125
> 1582:
> Clone Nlpha
> 7811
> 052
> 15.5S
> 1573
> N Chart
> 132
> 13.04:
> 10:
> 457
> 二10
>  =
> 1CUI
> 13
> Ts
> 258:
> 1,0JO
> SOJK
> 巨 Correlation
> SUIT CorrelJtion
> ILMIMTUT
> UTITUI
> L5t RLT:
> Jul'3
> II'4
> T们
> JUI IC
> II's
> 1'
> I
> I'E
> JuI'?
> TTI '19
> JuI'19
> L
> JulIII
> I
> Jl'1
> 1'
> Il
> 1TI '3
**

**2. 截面回归策略（略微调试）**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> ~IOO
> IONeDretsslol
> NeUt
> 1 ec
> AVUshrt
> ULLIIzatLonpercent
> UICS)
> Io IuLVeC
> aNCSIrt
> Uar ]
> Dsingle Oaw SeiAa
> 昵 Powc PzolNplo
> STaTIIULCMe; CURUDTSIORTINTCRCST
> UyJtt
> TJT
> UTEO
> SIIUIaTIOI
> 1.23
> 9.2196
> 0.31
> 5,4635
> 7.58q
> 11.359300
> Settings
> Ihmt
> Cm
> Unoere
> Um
> 0
> Delay
> ICh
> Nubmton
> O
> NaNIrdlim
> Unt Harong
> N
> C
> UT
> Ts
> TmT
> ICmo
> CM
>  Um mt
> ot C
> ECyI
> T
> T SmrCTIOT
> ICUTT
> g
> S0C
> 二13
> 21.9二
> 599
> 17.535:
> Nlpha
> 47.15
> 5-
> Sl
> 41112
> 1 |.55:
> 二8
> 1312二
> N Chart
> 3
> 1.91
> T
> 11.55
> 34
> :
> S
> 二
> UCJO
> 07/312120
> .5
> 三_=
> 20.3二
> ISpn 3775351
> 419.79
> 1.5
> 45|
> 20JU
> Risk neutralized
> Aeyregdtt Djta
> UTJLAJCIT
> 0.45
> 9.2196
> 0.14
> 1,1336
> 4.109
> 2.459600
> JUII
> AIC
> IUIC
> JUIC
> Je '2]
> Jul 'ZU
> Jri '21
> lUI
> JaII 'D
> V'
> NN
> CIo
> OT '5
> UD 'TA
> OOT
**

**3. 幅度限制策略（信号加强后）**

**
> [!NOTE] [图片 OCR 识别内容]
> Code
> o IS Summary
> TTOI
> SFr
> S
> U4UI
> 昵 sirele Datd Sel Rlra
> PT
> Paol Npha
> I
> TURDTISHORTINTTRFCT
> Uets
> UeIt
> LILLVCCa
> ULZatoLerCeUIUS |
> IeCaVt
> bar]
> SIohedLOMer「a2
> NLUTULJt
> ShaO
> TUTTII5
> UCUI
> SiMILaTTII
> Settings
> 1.55
> 3.439
> 1.33
> 9,1595
> 11.394
> 53.399630
> IhINI
> Reglom
> U
> Kl
> 0
> NIIChc
> Nmmh
> Tl
> Olhm
> U l
> N l
> Shpe
> T
> Ftwes
> Rerume
> Umwdow
> m
> Lang Count
> Sht Count
> ECUIR
> TCPZETD
> TC
> STJUSCT 
> 49弋
> 399
> 5qe
> 994
> 31
> 5 T
> 
> U;T:
> Clone Nlpha
> 411
> U:
> U士
> 315
> 77.73
> 1]
> 35
> B04e
> N Chart
>  TC+
> ICc
> 353
> C二-:
> J+3士
> 7.044
> OI
> 3U.:
> 3.29+
> II2e
> 359
> 796
> TCJO
>  TTC
> 199Ec
> 35
> 5CJO
> FT
> 4q4Es
> 4113
> 二:
> TCNA
> Risk neutralized
> NLUTULJtt UJte
> TIIO
> TC
> 1.10
> 3.439
> 4.6995
> 4.4235
> 27.399600
> Jul'3
> II'4
> TI'C
> JUI IC
> II's
> 1'
> TI 'C
> JuI'?
> JuI'19
> JulIII
> I
> I
> 1'
> JuI'
> 1TI '3
**

**四、结论**

**1. MCP效率很高，随时改动；**

**2. 低相关性，且相对高质量；**

**3. 需完善提示词，不断调试。**

---

## 讨论与评论 (20)

### 评论 #1 (作者: HX40615, 时间: 10个月前)

感谢分享，学习了

=============================================

keep moving

=============================================

---

### 评论 #2 (作者: FL39657, 时间: 10个月前)

感谢博主分享，对我来说有很大帮助，希望博主日后可以多多分享一些使用mcp做alpha的例子，我最近也一直在尝试用mcp做alpha，不过似乎效果一般，可能是我的提示词说的有问题，并且调试过程没有引导到位。

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

### 评论 #3 (作者: LR93609, 时间: 10个月前)

[FL39657](/hc/en-us/profiles/28857979560727-FL39657)

我也不是太熟悉提示词工程，传说可以更加精确一些，

我理解，重要的是经验的积累，通过测试不断沉淀：

首先，可以给它一些过往的经验总结或者是喜好，

比如，一元、二元或多元操作符的特征（txt文档），

抑或是操作符组合结构，它能够更深刻的理解并使用。

其次，给他一些成功案例，

比如，我的优势是模版多样性（前期成功案例），

它就能创造更多类似的模版，传递更多的创新。

---

### 评论 #4 (作者: QW96917, 时间: 10个月前)

这次展示了全面的提示词过程，学习了！

还想请问您，这个是最后用mcp直接提交的吗？

---

### 评论 #5 (作者: JB53978, 时间: 10个月前)

很厉害的一个博主，直接分享了alpha的表达式，前段时间我也在为Short Interest 这个塔的点亮而犯愁，花了我两天的时间来设计模板，后面也是成功点亮。但看到你用的这个工具看起来很轻松就点亮的Short Interest 的塔，很不错的工具，你用的是什么API？

------------------------------------

---

### 评论 #6 (作者: LR93609, 时间: 10个月前)

[QW96917](/hc/en-us/profiles/28830966804247-QW96917)

感谢跟帖，我还不会用mcp直接提交，也是刚刚调试通过，目前还处于模版探索阶段。

讲真，基于当前对Alpha的理解和mcp的运用，我暂时还没有信心让他帮我提交，其实我自己提交也还有不小的压力，担心vf爆雷。

我看有些热心的朋友，已经实现了全流程，大为震撼，希望能有更多的学习进步。

我会保持学习，持续分享，再次感谢。

---

### 评论 #7 (作者: LR93609, 时间: 10个月前)

[JB53978](/hc/en-us/profiles/30875128290711-JB53978)

感谢跟帖，你所说的API具体指的是什么呢？mcp的应用？大模型？

mcp应用：我用的是platform，让他读取字段描述，然后根据本人以往常用的模版或论坛信息，推荐的模版。

大模型：deepseek v3，前期充值10块钱，还没花完；国外的模型还不会充值。

我是否回答了你的问题？期待后续反馈。

---

### 评论 #8 (作者: ZZ37826, 时间: 10个月前)

deepseek V3这么强吗？

---

### 评论 #9 (作者: SH67409, 时间: 9个月前)

为什么我模拟出来的结果和楼主的差异很大呢？比如第一个
 
> [!NOTE] [图片 OCR 识别内容]
> Streak:
> day
> a=Vec_aVg(shrt3_utilizationpercent
> units);
> bsign(ts_mean(a,
> 580 )
> ts_mean(a
> 252));
> ZOOV
> Jan '14
> Jan '15
> Jan '16
> Jan'17
> Jn13
> Jan 19
> Jan 20
> Jan '21
> Jan'22
> Jan '23
> Pnl
> Risk Neutralized Pnl
> IS Summary
> Period
> K Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTMCVET
> TIMess
> ECUTI
> UraVdoIT
> Warain
> 0.82
> 2.04%
> 0.29
> 1.529
> 3.519
> 14.939600
  
> [!NOTE] [图片 OCR 识别内容]
> Sattings
> EUR/DITTOPZ500
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DEUAY
> EUR
> TOP25O0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.03
> PASTEURIZATION
> UNIT HANDLNG
> NAN HANDLING
> TEST PERIOD
> Verify
> Off
> YEARS
> MONTHS
> MAX TRADE
> Save as Default
> Apply


---

### 评论 #10 (作者: LR93609, 时间: 9个月前)

[ZZ37826](/hc/en-us/profiles/33841678941207-ZZ37826)

我个人理解，仅仅就模版推演来讲，deepseek已经够用了，

如果说是mcp更为高端的功能，deepseek可能还做不到，

是否有必要呢？他帮我们找到因子、提交因子吗？

如果要做到这一点，恐怕要内置一个金融模型，

开放所有的数据给他才行，我理解短时间内很难做到。

因子挖掘 **重点可能还是我们对字段和模版的理解和认识** ，

平台可能想到，大家多数是搞计算机的，不懂金融，推荐使用mcp，

但不全是对工具的使用吧，我看有些朋友重点放到工具上，

压根儿不去研究字段，也不研究模版，空对空，死磕mcp，

是不是有点舍本逐末，或者是本末倒置了呢？

很多字段， **我都是手动simulate，然后提交的，反而更加高效，**

比如 **我在后面的帖子中讲到的，CHN Risk72数据集，一个字段，**

**我用了一天时间，手动提交了三个alpha，手动点亮了pyramid。**

---

### 评论 #11 (作者: DS48533, 时间: 9个月前)

感觉像是已经有了很多模版，然后LLM根据对于字段的理解，去选择了一些模版，然后也有根据op描述txt，加的一些创新。挺好的，然后可以加入一些循环，让AI一直做这样的事情。最后生成很多alpha后，用程序检测表达式的合法性，或者挨个跑，报错的不要了。

---

### 评论 #12 (作者: JB71859, 时间: 9个月前)

看起来蛮不错的，你对mcp的使用确实蛮好的，你目前跑这个是有使用什么工作流吗，我使用了Claude4.1的效果确实不错，但一下午跑了23刀，但看你使用deepseek v3也可以达到这个效果，我想问一下，你是通过工作流来解决模型差距的还是说deepseek v3本身就很强，非常期待你的回复。
====================================================================================

---

### 评论 #13 (作者: LR93609, 时间: 9个月前)

[DS48533](/hc/en-us/profiles/29332844557207-DS48533)

可以这么理解，我是先对模版有了认识，然后才用上了MCP；

MCP推荐一批模版以后，我再修修剪剪。

MCP的方向是对的，需要手动完善，等习惯了我的风格，可能会有所改变吧。

---

### 评论 #14 (作者: 顾问 NL80893 (Rank 16), 时间: 9个月前)

感谢楼主教学！通过您这个生成的模板也有了一些新思路，EUR的short interest总是做不出来，要么就是信号不强~想请问一下您是用的哪个MCP的底层呀，我感觉我的TRAE免费版并不是很好用，总是找不到网页，重复N次才成功一次，还是说免费的确实就不好呀~期待楼主的回复~

===========柯楠要你努力GM呀=============

---

### 评论 #15 (作者: 顾问 HP65370 (Rank 93), 时间: 9个月前)

感谢大佬的分享，我也用的deepseek，前段时间太忙没有花很多时间在mcp上，但是我觉得我也有点像楼主评论区所说的差不多，对数据字段还有模板的研究不是那么透彻，自然对mcp的训练和提问上有点生涩；楼主分享的内容给了我对mcp的一定的启发，待我去实践实践

---

### 评论 #16 (作者: LR93609, 时间: 9个月前)

[SH67409](/hc/zh-cn/profiles/29030826126359-SH67409)

我开了NAN HANDLING，你没开，很多时候会差别很大。

推荐常开，类似于ts_backfill

我的设置就是敞开状态

感谢回帖，有问题随时沟通

---

### 评论 #17 (作者: LR93609, 时间: 9个月前)

[顾问 NL80893 (Rank 16)](/hc/zh-cn/profiles/29953598557975-顾问 NL80893 (Rank 16))

感谢回帖，我用的是deepseek v3

我觉得大模型在MCP中的使用类似于提示词工程，不需要太复杂的模型，只要提示词到位，简单的模型就够了。如果Kimi或者是豆包可以用，我会用免费的。

你如果用过扣子就明白，设定好了以后，在当前技术水平下，大厂发布的简单模型就可以完成我们所需的大部分需求。

当然，可能贵有贵的道理，我也没有用过更好的，v3已经可以满足我的日常需要了。

我觉得大模型能做到这个程度已经足够了，难不成让他完全替代我们去分析数据和提交因子吗？

我觉得多样性上面，在可以预见的未来，大模型可能真做不到，大可不必纠结工具的聪明程度，够用就行

不知道有没有回答你的问题，一家之言，欢迎置评

---

### 评论 #18 (作者: 顾问 SJ65808 (Rank 20), 时间: 9个月前)

感谢大佬分享，EUR shrt只有一个数据集，没想到还能有这种用法，拓展使用自己的方法~~

===================================================================================
===================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #19 (作者: AM12075, 时间: 9个月前)

跑这几个大概花了多少token？这种方法感觉出来质量也不是很高，和123阶相比是不是只是花的时间少了一些呢？

===================================================================================
===================================================================================

---

### 评论 #20 (作者: LR93609, 时间: 9个月前)

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

感谢回帖，如下是我的回答：

1. 让他推荐模板库里现存模版，花费很少，文中提到$0.11，但是在我安装调试时花了10块钱人民币。

2. 质量高于不高，主要看数据字段，其次看组合方式，最后看调试过程，并非看工具，否则要人干嘛；

3. 到了consultant，我就不再跑123阶了，效率低不说，还容易过拟合，毕竟没有任何经济学逻辑瞎跑。

-----------------------------------------------------------------------
凡是发生，皆利于我；愿我所愿，尽是美好
-----------------------------------------------------------------------

---

