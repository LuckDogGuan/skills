# 顾问 HP65370 (Rank 93) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 HP65370 (Rank 93) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: 【Alpha灵感】基于MCP提交的3个Short Interest 因子)
- **原帖链接**: [Commented] 【Alpha灵感】基于MCP提交的3个Short Interest 因子.md
- **时间**: 9个月前

**提问/主帖背景 (LR93609)**:
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

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的分享，我也用的deepseek，前段时间太忙没有花很多时间在mcp上，但是我觉得我也有点像楼主评论区所说的差不多，对数据字段还有模板的研究不是那么透彻，自然对mcp的训练和提问上有点生涩；楼主分享的内容给了我对mcp的一定的启发，待我去实践实践


---

### 技术对话片段 2 (原帖: 【Alpha灵感】基于MCP提交的3个Short Interest 因子)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】基于MCP提交的3个Short Interest 因子_34407581314583.md
- **时间**: 9个月前

**提问/主帖背景 (LR93609)**:
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

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的分享，我也用的deepseek，前段时间太忙没有花很多时间在mcp上，但是我觉得我也有点像楼主评论区所说的差不多，对数据字段还有模板的研究不是那么透彻，自然对mcp的训练和提问上有点生涩；楼主分享的内容给了我对mcp的一定的启发，待我去实践实践


---

### 技术对话片段 3 (原帖: 【ValueFactor涨分宝典】一个月从0.5→0.99的涨分之旅论坛精选)
- **原帖链接**: [Commented] 【ValueFactor涨分宝典】一个月从05099的涨分之旅论坛精选.md
- **时间**: 10个月前

**提问/主帖背景 (JL76306)**:
今天更新了截止六月份的ValueFactor（以下简称VF），非常惊喜地发现我的VF终于脱离了0.5（前阵子有一段时间断交断回测导致VF在0.5这档严重坐牢Orz），这次更新甚至达到了我不可思议的0.99！和191.02的“假专家级”Gold-Pay！！！


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Factor
> Factor
> Data
> Alphas
> Fields
> Submitted
> J76306 (Me)
> 0.00
> 0.99
> 299
> 274



> [!NOTE] [图片 OCR 识别内容]
> 卫02404 Payment
> 平平无奇老GOLD
> 0211472025
> 0S$117.531
> 12025 Q1Payment
> 05/2212025
> 05$115.82
> Super Alpha Competition 2025
> 波澜壮阔的02
> 07/25/2025
> US$300.00
> Super Alpha Competition 2025 Week 4 Group HCAC
> 07/25/2025
> US$300.00
> 202502 Pavment
> 0841712025
> 055191.021


> 前情提要：其实我的VF是经历了0.5以下（暗无天日的1.2刀Basepay）导致达到领季度低保要求后便开始了心灰意冷的“断交断回测”时期，这样的情况下理论上我的VF面临了严重的暴跌风险！
> 但是有幸的是低保alpha质量还不错，让我重新回到0.5，此时又恰遇有趣的Super Alpha Competition，回归的我重燃激情！（请让我再次感谢SAC!）
> 
> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 心灰意冷三个月V5激情的02
> <
> M
> p
> 2:
> ^9"
> ~' 3
> 2 AO:
> AO"
> 2
> 4
> 
> O
> AO
> 14.Jul
> 28.JUl
> Oct
> Nov
> Nov
> Dec
> Dec
> Dec
> Mar
> 13.Jan
> 24.Feb
> 21.ApF
> May
>  May
> !
> Jun
> 30.jun


首先我们来了解什么是ValueFactor，有助于我们更好的理解VF提升的原因，这里引用XZ23611大佬关于VF深入浅出的理解：

**Value Factor 衡量的是最近提交的Alpha对组合Alpha表现（近三个月）的影响，同时考虑三个特定因素：(a) Alpha的个体表现，(b) 最近Alpha提交的多样性，以及 (c) 提交的独特性，即与您过去的提交以及其他顾问提交的比较。**

故，我将从以下几个角度进行分析 “空池三个月的VF救赎之旅”案例。

（ **作者强烈不建议大家空池“断交断回测”，此举十分十分危险，本文仅希望从自身角度给予低VF的朋友一点信心和帮助** ）

希望我的分享能够给大家带来一点交流与启发，欢迎大家按赞、讨论！

### Part 1 ：最简单且重要的是“submit”

我认为持续账户的回测与提交维持账户有效活跃是VF的基石！

我们应该保持alpha池的积累，从理论上来说，更大的数据量才有更的大概率能撞击出好的产物。

所以无论如何多么灰心，如果只要有提交的能力请先保持住alpha的数量扩张。 **
> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 06/07/2025
> Submitted Alphas: 5
> s
> N
> Displayed Period
> 05/31/2025 -06/30/2025
> 126
> 3.jun
> Jun
> 7.jun
> .Jun
> 11.Jun
> 13.jun
> Jun
> 17.jun
> 19jun
> 21.Jun
> 23.Jun
> 25.lun
> 27.jun
> 29.Jun
**

### Part 2 ：注意alpha提交的质量

很显然大数量的提交也隐含着“恶魔果实“（低质量因子），所以在拥有提交能力的同时，也请一定注意提交的alpha质量!


> [!NOTE] [图片 OCR 识别内容]
> SOO
> CJ
> SJOM
> OOK
> SOK
> OJOr
> S0O
> TO
> TO5
> T016
> 70
> 7018
> 701
> 702
> 707
> 3
> 707
> IS Summary
> Period
> Sinele Data SetMphs
> PowerPogllchs
> Ojamdheme EURDTISHORTINTERESTy
> ABgregate Dara
> Shr
> TIN
> STI
> CAo
> 1.65
> 2.509
> 0.90
> 3.76%
> [2.44%
> 30.130000


我们知道一个alpha有如上图这样的六个参数，对这六个参数的使用可以有这样理解，即： **sharpe越高越好、turnover越低越好，fitness越高越好，return越高越好，drawdown越低越好，margin越高越好。**

但显然这并不是一个实用标准，那么结合学习经验，我一般会优先注意这四个维度：

- **margin要尽可能的高** （margin来源于你的return收益去掉turnover换手费率的实际效益，不同地区因不同难度有不同的建议值，总结研究小组的经验可以简单的一概而述为保持大于15+）
- **alpha尽可能的纯粹** （ATOM alpha/Signed alpha），也就是使用的data（Pyramid）尽量为1
- **alpha的曲线即可能的完整，丝滑** 。
- **有意识的管理自己的Self Correlation自相关性/ Prod Correlation同行相关性** ，正如你所知道的，越独特的越珍贵。

### Part 3：散布Pyramid

这里一定要提到的一点是，alpha提交的丰富性。

尽可能的交不同Region/不同Pyramid的alpha也有助于让账户的运营更趋于健康，请务必让你的alpha在整张genius图鉴散步起来，聚焦在一个数据集猛猛挖反而会错失许多其他地区的机会甚至在一个不可预见的坑里埋的更深（倒不如留着这个相同Pyramid的alpha到下个季度点塔，如果它确实不错）。

### Part 4：不要忽视Super Alpha

当到达提交满100个alpha可以解锁Super Alpha（以下简称SA）的时候，请花费一些时间去学习并提交SA，SA能够让你对挑选出的alpha进行策略组合，所以只要方法到位就可以很大程度挽救你的整体alpha质量（推荐大家可以去SA专家—游戏王worldquant brain赛博游戏王的SA分享系列贴子学习）。

特别的，这次仅通过一个月时间，我认为也能做到VF如此大的提升，参加SAC比赛制作SA功不可没，正是它让我能够使用所有人的alpha池，按照我对优质alpha的理解进行挑选重新组合强力修复我的alpha整体表现。

或许，通过比赛取得的Week4/HCAC组第一和总决赛31的时候，或许就已经提前预示我将大幅度提升我的VF。


> [!NOTE] [图片 OCR 识别内容]
> 325I
> 3ON
> 27SW
> 35
> 225N
> TOu
> 17S
> T5
> 125
> 10
> 7.SOoR
> DJD
> 2500
> 7_
> 7015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 222
> 202
> ComboPpL
> Equal NeiehrPnl
> IS Summary
> Period
> ARBTBate Data
> TUIOV
> C T
> CtUTII:
> SUC
> 8.95
> 12.88%
> 14.35
> 33.12%6
> 1.4596
> 51.439000
> N
> L1ain


（秀一张我在SAC比赛组的超绝SA，助力大家对制作Super Alpha更感兴趣）

“所有看不清的事情或许也有迹可循”

以上，是我对于六月VF提升的四个维度想法，如果能帮到你便是极好的啦。

有任何指正欢迎留言！

**顾问 HP65370 (Rank 93) 的解答与建议**:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------感谢大佬分享，我现在对于何为好的alpha有了清晰的认识，我最近一次更新vf从0.5跌到了0.25，看着每天超低的base心灰意冷，读了大佬的帖子我备受鼓舞，以后要坚持多交alpha，多交好的alpha,同时我阅读了游戏王worldquant brain赛博游戏王的sa帖子，收获颇丰，相信不久的将来我的vf一定会有质的提升！！！--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 4 (原帖: 【ValueFactor涨分宝典】一个月从0.5→0.99的涨分之旅论坛精选)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【ValueFactor涨分宝典】一个月从05099的涨分之旅论坛精选_34283569758999.md
- **时间**: 10个月前

**提问/主帖背景 (JL76306)**:
今天更新了截止六月份的ValueFactor（以下简称VF），非常惊喜地发现我的VF终于脱离了0.5（前阵子有一段时间断交断回测导致VF在0.5这档严重坐牢Orz），这次更新甚至达到了我不可思议的0.99！和191.02的“假专家级”Gold-Pay！！！


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Factor
> Factor
> Data
> Alphas
> Fields
> Submitted
> J76306 (Me)
> 0.00
> 0.99
> 299
> 274



> [!NOTE] [图片 OCR 识别内容]
> 卫02404 Payment
> 平平无奇老GOLD
> 0211472025
> 0S$117.531
> 12025 Q1Payment
> 05/2212025
> 05$115.82
> Super Alpha Competition 2025
> 波澜壮阔的02
> 07/25/2025
> US$300.00
> Super Alpha Competition 2025 Week 4 Group HCAC
> 07/25/2025
> US$300.00
> 202502 Pavment
> 0841712025
> 055191.021


> 前情提要：其实我的VF是经历了0.5以下（暗无天日的1.2刀Basepay）导致达到领季度低保要求后便开始了心灰意冷的“断交断回测”时期，这样的情况下理论上我的VF面临了严重的暴跌风险！
> 但是有幸的是低保alpha质量还不错，让我重新回到0.5，此时又恰遇有趣的Super Alpha Competition，回归的我重燃激情！（请让我再次感谢SAC!）
> 
> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 心灰意冷三个月V5激情的02
> <
> M
> p
> 2:
> ^9"
> ~' 3
> 2 AO:
> AO"
> 2
> 4
> 
> O
> AO
> 14.Jul
> 28.JUl
> Oct
> Nov
> Nov
> Dec
> Dec
> Dec
> Mar
> 13.Jan
> 24.Feb
> 21.ApF
> May
>  May
> !
> Jun
> 30.jun


首先我们来了解什么是ValueFactor，有助于我们更好的理解VF提升的原因，这里引用XZ23611大佬关于VF深入浅出的理解：

**Value Factor 衡量的是最近提交的Alpha对组合Alpha表现（近三个月）的影响，同时考虑三个特定因素：(a) Alpha的个体表现，(b) 最近Alpha提交的多样性，以及 (c) 提交的独特性，即与您过去的提交以及其他顾问提交的比较。**

故，我将从以下几个角度进行分析 “空池三个月的VF救赎之旅”案例。

（ **作者强烈不建议大家空池“断交断回测”，此举十分十分危险，本文仅希望从自身角度给予低VF的朋友一点信心和帮助** ）

希望我的分享能够给大家带来一点交流与启发，欢迎大家按赞、讨论！

### Part 1 ：最简单且重要的是“submit”

我认为持续账户的回测与提交维持账户有效活跃是VF的基石！

我们应该保持alpha池的积累，从理论上来说，更大的数据量才有更的大概率能撞击出好的产物。

所以无论如何多么灰心，如果只要有提交的能力请先保持住alpha的数量扩张。 **
> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 06/07/2025
> Submitted Alphas: 5
> s
> N
> Displayed Period
> 05/31/2025 -06/30/2025
> 126
> 3.jun
> Jun
> 7.jun
> .Jun
> 11.Jun
> 13.jun
> Jun
> 17.jun
> 19jun
> 21.Jun
> 23.Jun
> 25.lun
> 27.jun
> 29.Jun
**

### Part 2 ：注意alpha提交的质量

很显然大数量的提交也隐含着“恶魔果实“（低质量因子），所以在拥有提交能力的同时，也请一定注意提交的alpha质量!


> [!NOTE] [图片 OCR 识别内容]
> SOO
> CJ
> SJOM
> OOK
> SOK
> OJOr
> S0O
> TO
> TO5
> T016
> 70
> 7018
> 701
> 702
> 707
> 3
> 707
> IS Summary
> Period
> Sinele Data SetMphs
> PowerPogllchs
> Ojamdheme EURDTISHORTINTERESTy
> ABgregate Dara
> Shr
> TIN
> STI
> CAo
> 1.65
> 2.509
> 0.90
> 3.76%
> [2.44%
> 30.130000


我们知道一个alpha有如上图这样的六个参数，对这六个参数的使用可以有这样理解，即： **sharpe越高越好、turnover越低越好，fitness越高越好，return越高越好，drawdown越低越好，margin越高越好。**

但显然这并不是一个实用标准，那么结合学习经验，我一般会优先注意这四个维度：

- **margin要尽可能的高** （margin来源于你的return收益去掉turnover换手费率的实际效益，不同地区因不同难度有不同的建议值，总结研究小组的经验可以简单的一概而述为保持大于15+）
- **alpha尽可能的纯粹** （ATOM alpha/Signed alpha），也就是使用的data（Pyramid）尽量为1
- **alpha的曲线即可能的完整，丝滑** 。
- **有意识的管理自己的Self Correlation自相关性/ Prod Correlation同行相关性** ，正如你所知道的，越独特的越珍贵。

### Part 3：散布Pyramid

这里一定要提到的一点是，alpha提交的丰富性。

尽可能的交不同Region/不同Pyramid的alpha也有助于让账户的运营更趋于健康，请务必让你的alpha在整张genius图鉴散步起来，聚焦在一个数据集猛猛挖反而会错失许多其他地区的机会甚至在一个不可预见的坑里埋的更深（倒不如留着这个相同Pyramid的alpha到下个季度点塔，如果它确实不错）。

### Part 4：不要忽视Super Alpha

当到达提交满100个alpha可以解锁Super Alpha（以下简称SA）的时候，请花费一些时间去学习并提交SA，SA能够让你对挑选出的alpha进行策略组合，所以只要方法到位就可以很大程度挽救你的整体alpha质量（推荐大家可以去SA专家—游戏王worldquant brain赛博游戏王的SA分享系列贴子学习）。

特别的，这次仅通过一个月时间，我认为也能做到VF如此大的提升，参加SAC比赛制作SA功不可没，正是它让我能够使用所有人的alpha池，按照我对优质alpha的理解进行挑选重新组合强力修复我的alpha整体表现。

或许，通过比赛取得的Week4/HCAC组第一和总决赛31的时候，或许就已经提前预示我将大幅度提升我的VF。


> [!NOTE] [图片 OCR 识别内容]
> 325I
> 3ON
> 27SW
> 35
> 225N
> TOu
> 17S
> T5
> 125
> 10
> 7.SOoR
> DJD
> 2500
> 7_
> 7015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 222
> 202
> ComboPpL
> Equal NeiehrPnl
> IS Summary
> Period
> ARBTBate Data
> TUIOV
> C T
> CtUTII:
> SUC
> 8.95
> 12.88%
> 14.35
> 33.12%6
> 1.4596
> 51.439000
> N
> L1ain


（秀一张我在SAC比赛组的超绝SA，助力大家对制作Super Alpha更感兴趣）

“所有看不清的事情或许也有迹可循”

以上，是我对于六月VF提升的四个维度想法，如果能帮到你便是极好的啦。

有任何指正欢迎留言！

**顾问 HP65370 (Rank 93) 的解答与建议**:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------感谢大佬分享，我现在对于何为好的alpha有了清晰的认识，我最近一次更新vf从0.5跌到了0.25，看着每天超低的base心灰意冷，读了大佬的帖子我备受鼓舞，以后要坚持多交alpha，多交好的alpha,同时我阅读了游戏王worldquant brain赛博游戏王的sa帖子，收获颇丰，相信不久的将来我的vf一定会有质的提升！！！--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 5 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年11月27日

由于当时这几天去旅游了，遂将这几天的补上

今天交满了，交了4个jpn的ppa，涉及fundamental,analyst,model,instituitons，可谓是把分散化做到了极致，但是sharpe还是偏低了，在jpn好难做出那些sharpe高的alpha啊，可能是我实力还不够，交的是asi的sa

今日base指标：

sa：54.59dao  交的是asi notown 520，感觉base和我vf0,91差不了多少

ra:6.12dao 稍微比前几天高了1dao

================================坚持！=====================================


---

### 技术对话片段 6 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年11月28日

这个月快结束了，于是交了一个jpn 的own sa来稳一稳combinde，同时交了2个amr的ppa来提升一下我的六维，现在交的是之前的库存，而现在开始是为了下个月的d0做准备，已经跑出很多可以提交的alpha了

今日base指标:

sa:8.21dao  jpn own 不是35，单5，都能达到这个base，比三五只低一两刀

ra:2.98dao  这个月最低的base，现原形了，希望下次我的vf还能上0.9

===============================坚持！-===============================


---

### 技术对话片段 7 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年11月29日

今天不知不觉就交满了，交了4个amr的ppa，涉及fundamental,institutions,和两个analyst，发现我的存货还挺多的，交了这些还有三十多个可以立马提交的，看来下个赛季不用愁了，但是剩下的指标肯定没有这个月提交的好，还是要做一些取舍的，顺便交了1个amr的own sa

今日base指标：

sa:8.09dao  同样的单5，差不多8dao左右了，还是很有性价比

ra:6.51dao  看来交满了还是给的挺多的，但是我现在平均一天就交个3.5个吧，交满确实很吃力

===================================坚持！=================================


---

### 技术对话片段 8 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：22025年11月30日

今天是这个月的最后一天了，今天结束这个赛季的combine就定型了，今天交了一个asi的model ra和一个amr的analyst和model的ppa，隔了十多天又再次交了一个asi的，主要是这个ra是存货，等到下一次交这个alpha估计几个月之后了吧，担心prod涨上去就干脆交了，又交了一个asi的notown 520

今日base指标：

sa:57.62dao  asi notown 520 fitness也是有8了

ra:4.28dao

==============================坚持！=========================================


---

### 技术对话片段 9 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月01日

今天是这个月第一天，我也是打算开始做d0了，先把前几天回测出来的存货交一下，交的是两个usa d0 model和fundamental的，其中有一个alpha的sharpe甚至大于4，fitness大于3，可惜只是个ppa啊，也是第一次做出is这么好看的alpha，也是希望os不要太拉跨了，今天sa也交的是asi 520

今日base指标：

sa:53.77dao asi notown 520 略有下降

ra:4.51dao  交的alpha的prod都有点高了

====================================坚持!==================================


---

### 技术对话片段 10 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月02日

今天交满了，依然交的usa d0 的model pv other，都是ppa，sa还是asi notown 520,而且最近发现asi有了一个新的测试，发现以前屯的520都不能用了，还是很苦恼，又得重新开始做，d0一个月只能交30个，我还得合计合计该交些什么，金字塔是肯定不用担心的了，那就尽可能多的分散化一点吧，目前就准备点analyst fundamental other model  pv news这6个数据集的，d0的小数据集实在不敢碰，而且现在做也没什么意思

今日base指标：

sa:56.15dao asi notown 520  指标没有昨天的好

ra:4.6dao  乘数还是太低了

===========================坚持！====================================


---

### 技术对话片段 11 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月03日

今天还是坚持交满，交的是usa d0的两个model，一个ppa和一个ra，以及fundamental和pv的ppa，还是坚持在d0全部做成atom，不想去混信号，而且我发现我刚成为顾问的那三个月只做出来了一个ra，而现在做ra还是很简单的，一路走下来我还是一直在进步的，要继续保持一股学习的劲，今天的sa也是asi的520

今日base指标：

sa:52.27dao  asi notown 520，我发现最近的sa都是一天高一天低的很有规律，而且呈现的是下降趋势

ra:4.94dao

=============================坚持！=====================================


---

### 技术对话片段 12 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月04日

今天没有交满，其实这几天交的都是上个月跑的存货，这几天确实没有多少时间，太忙了，期末周也快到了，但是我的工作流已经很完备了，今天交的两个option的usa d0的ppa，用的是魔改论坛模板的，质量非常好，但是prod太高了，我甚至觉得我都快被踢出群了，因为usa的prod实在太高了，外加准备冲grandmaster又要保持多提交

今日base指标：

sa:54.54dao  交的asi notown 520，fitness甚至到了12，

ra:4.83dao  非常稳定，不多不少的

=============================坚持！====================================


---

### 技术对话片段 13 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月05日

今天交了usa d0 的option model news，现在把option的塔已经点掉了，最近都打算每天交三个alpha了，值得庆幸的是今天我的weight终于突破0了，来到了0.01，还是很惊喜的，从6月成为有条件顾问参加iqc以来过了这么久，终于来了，今天交了一个asi的520,fitness有8.53，我交的520的指标都很好，margin高，近两年来无衰减，希望不要对我的vf和combine造成较大的影响吧

今日base指标：

sa:52.10dao  越来越低了，不会后面会跌破50dao吧，其实拿这么多已经足够了

ra:4.52dao

==================================坚持!=================================


---

### 技术对话片段 14 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月06日

今天终于有时间写量化日记了，于是把之前的补上，一次性写了10条，今天交的是usa d0的三个ppa，涉及一个other一个fundamental一个model,从前天起就彻底结束对usa d0的回测了，算了一下，开始usa d0的回测也就8天吧，交满30个戳戳有余的，算上相关性问题，下赛季应该还有十多个的存货，出货率还是很不错的，而且后4天也是开了5个槽给eur d0跑，但是这一周的prod确实超标了，估计马上就收到警告了，准备下一周开始ind的回测和提交，来降低一下prod，但是还要在交10个usa d0，prod真是令人头大啊，在小地区一点也不用考虑prod的问题，怎么跑都是低相关性


---

### 技术对话片段 15 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月07日

今天交了3个alpha，包括usa d0的2个analyst的ppa，和一个asi的not own 520，以前总觉得analyst很好跑，觉得是仅次于model的第二好跑的数据集，可是这个赛季我发现analyst数据集不仅多，还比较难出货，对usa d0 analyst单槽回测了8天，只找到4个稍微好一点的ppa，然而other都找到了十个，同样体现于amr和jpn

今日base指标:

sa:54.63dao  asi not own 520，今天是连续上涨的第三天

ra:3.93dao rabase也是第一次跌到4dao以下了

===============================坚持！=====================================


---

### 技术对话片段 16 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月08日

今天开始限流了，平时我都会跑到2w个以上的，突然砍了一半要好好适应一下了，而且今天更新combine了，意料之中的涨了，因为我10月交了一百个alpha，涉及usa eur asi，都是大区，而且做的还算好，涨了大概0.6左右，但是下一次更新大概率是跌的，因为我交了amr和jpn，第一次做小地区，个人感觉jpn做的很不好，而且参加了aiac，交了很多差的sa，而且交了很多520,只希望不要暴跌就好了

今日base指标：

sa:54.67dao  连续四天上涨了，很好看的一个上涨曲线

ra:5.49dao 一个other一个analyst，把usa d0 analyst的塔点掉了，到目前为止点了56个塔了，现在倒不着急了，不过今天交两个竟然比平时交四个还要多

==================================坚持！====================================


---

### 技术对话片段 17 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月09日

最近在跑IND,analyst pv fundamental news model五个数据集各一个槽来跑，跑了接近两天了，只有model一个数据集有一阶跑完就有PASS的alpha，还不少，我随便找了几个去测相关性，不是0.95+就是0.85＋的，我寻思着我也没有全用传统一阶啊，pc都这么高，真的好难跑啊，不过现在只是初筛，还没有进行二阶变换，先跑一跑再说，最近几天就先交着usa d0的存货吧，还能交个3天左右，做完usa d0之后打算交ind或者eur d0了，但是做eur d0的化这个月只能交60个，上个月交了100个，感觉变化幅度有点大，对我之后的vf有负面效果

=================================坚持！======================================


---

### 技术对话片段 18 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月10日

今天交了3个alpha，一个asi的520的not own以及两个usa d0的other数据集的，最近没货了，故打算之后每天就交两个ra/ppa和一个ppa，毕竟现在已经点了56个塔了，点塔倒没有什么问题，六维和combine也看得过去，想囤一囤留给下一个赛季交，况且上个月交了100个，提交alpha的数量不能急剧下降，先缓降一下

今日base指标：

sa:54.68dao   依旧在54dao左右，还能吃几天的notown就要开始交own的sa了

ra:4.56dao

====================================坚持！================================


---

### 技术对话片段 19 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月11日

今天交了三个alpha，一个asi的520的not own和两个usa d0的other以及model，唯一的缺点就是sharpe太低了，不过上周我的pc超了，这周要保持低pc，我交完了才发现sa也算d0的额度，可是现在已经交了30个了，导致我不能交sa来稳combine了，天塌的，下次更新到12月岂不是我的combine和vf不保了，而且自我感觉我交的质量不好，而且还说去做eurd0的，没想到这个每月30个的额度还不分地区，明明已经跑了好几天的eur d0，挖到了几十个ra/ppa准备交的时候发现交不了，现在除了ind已经没货了，可是ind风险也太高了，于是转向usa d1，刚好还差4个塔顺手给点掉，问题是现在没有存货，只能翻翻垃圾交了

=====================================坚持!================================


---

### 技术对话片段 20 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月12日

今天只交了两个了，一个asi的520的not own sa和一个usa d1的analyst数据集的ppa，这个月剩下的日子打算在usa d1交上30个alpha就足够了，现在开始慢慢跑，现在交的都是存货里面的垃圾，剩下的own额度就交usa d1的sa吧，这几天还在拉数据库，要先跑一下裸字段，之后才能正式开始跑，这样能直接把缺数据的字段给排除掉，导致现在的进度一直为0。

今日base指标：

sa:53.87dao  差不多

ra:1,93dao  骤降，直接减半了，最低的一次

======================================坚持！=================================


---

### 技术对话片段 21 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月13日

今天也交了两个apha，一个usa的own双五，现在不追求三五了，两者的base对于我这个vf来说就是一两dao的差距，没必要废那么多功夫，我现在追求高margin，其次，我今天交了一个anayst+earnings的双字段alpha，其实不想交双字段的，确实是没办法就交了，指标还行的，还能接受吧，今天交了之后后面就没有存货了，虽然还有几个，但是质量实在太差，sharpe连1.2都没有，pc也高。

到这个赛季结束，我得交9个own和9个notown，usa的现在的alpha不算user和iqc交的一共有一百个了，足够我交很多ownsa了

=================================坚持！======================================


---

### 技术对话片段 22 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月14日

今天交了两个alpha，一个是asi的520 not own的，我发现我最近交的asi的sa真的太多了，不过这个月也就只做了usa d1 和d0，之后交了一个usa d1的model，昨天跑了5000次，出了十多个可以交的，还算不错，就是pc大多数都高于了0.7，应该是模板不具有独特性还有就是这些字段都被别人用的太多了，因为我昨天跑的是model和option的，还没有测option有多少可以交的，不过应该也能有几个吧，这样来说就算限制了5000个回测我应该也是有生存的余地了

昨日base指标：

sa:8.04dao 我倒是很惊讶，usa d1双五都能拿这么多，可是usa d1的sa我做不出三五

ra：1.91dao  习惯了，交一个而且没有乘数是这样的

=====================================坚持！=====================================


---

### 技术对话片段 23 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年12月15日

今天终于交了四个alpha了，交的是一个usa d1 的own sa 双5，不过都是几个月前的库存了，自从限流了之后再也没有跑过sa，先把库存交完了再说吧，另外交的三个ppa是usa d1的model和imbalance，今天把imbalance的塔点掉了，那截至目前为止点了57个塔了，还剩三个，估计一个星期之内能点完。今天vf更新了，不过我发现变化不大，应该微跌了，昨天交的一个usa d1 ppa只有1.81dao，而前天同样的usa d1 ppa确有1.91dao，现在vf是0.89dao，那我估计我是0.88 0.87 0.86的样子吧，不过我10月的combine大涨了，vf确降了，太难受了！

============================坚持！=====================================


---

### 技术对话片段 24 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月1日（回忆版）

今天交了3个eur的ra/ppa和一个eur的555

region universe sharpe fitness margin

EUR TOP2500 5.9200 5.9600 0.0020

EUR TOP2500 3.3200 2.6000 0.0018

EUR TOP2500 2.7600 2.1900 0.0021

EUR TOP2500 2.7600 1.9100 0.0012

今日base指标：

sa:33.1刀，0.89vf，赛季第一天三五就能达到这么高，有点不理解

ra:4.46刀

================================越努力，越幸运=============================


---

### 技术对话片段 25 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月2日（回忆版）

今天又交了3个eur的ppa/ra，和一个eur555,感觉最近交的alpha质量都很好啊

region universe sharpe fitness margin

EUR TOP2500 6.0600 5.9500 0.0019

EUR TOP2500 2.6800 2.0300 0.0012

EUR TOP2500 2.5800 1.7100 0.0016

EUR TOP2500 1.9700 1.2100 0.0011

今日base指标：

sa:9.72刀,同样的三五，都是own，昨天和今天就差了好几倍，因为昨天大家只能交own的，今天开始才能交not own的

ra:3.49刀,蚊子腿罢了

==============================越努力，越幸运=============================


---

### 技术对话片段 26 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月3日（回忆版）

今天和前两天一样，三个eur的ppa/ra，一个eur的own 555，做的很分散，基本上都涉及不同的数据集

region universe sharpe fitness margin

EUR TOP2500 6.6200 6.0600 0.0017

EUR TOP2500 2.1800 1.4600 0.0021

EUR TOP2500 1.7600 1.1000 0.0015

EUR TOP2500 1.6400 0.8900 0.0013

今日base指标：

sa:20.32刀,交的是own eur 555，同样的表现，比昨天高了一倍还要多

ra:3.70刀，没有做主题，就值这个价

==============================越努力，越幸运=============================


---

### 技术对话片段 27 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月4日（回忆版）

今天交了3个eur的ppa/ra，希望能稳住这个节奏，还交了一个asi的not own553，这几天对eur的margin不太满意

region universe sharpe fitness margin

ASI MINVOL1M 7.1600 8.0800 0.0025

EUR TOP2500 2.1400 1.4000 0.0021

EUR TOP2500 2.0900 1.3000 0.0012

EUR TOP2500 2.0300 1.1100 0.0012

今日base指标：

sa:54.02刀，爽啊，asi not own 553，要的就是这个感觉

ra:3.68刀，没记错这几都在交了些ra吧，还是这么低

===========================越努力，越幸运==============================


---

### 技术对话片段 28 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月5日（回忆版）

今天开始就交不动了，限制5000回测还是太吃力了，没有存货可交了，点塔可是个大问题，今天交了一个eur的own sa 555

region universe sharpe fitness margin

EUR TOP2500 6.2300 5.3300 0.0015

EUR TOP2500 2.0300 1.3200 0.0010

今日base指标：

sa:15.86刀，交的是eur own 555，奇数日交的sa的base越来越少了，看起来马上要回归正常水平了

ra:1.9刀，只交了一个就直接锐减啊

=============================越努力，越幸运===========================


---

### 技术对话片段 29 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月6日（回忆版）

开始限制只能交ind地区的ppa了，没办法，只能全力以赴点ind的塔了，但就是pc太高了，进攻ind的第一天还没有看到一个pc小于0.7的可以交的，顺便今天交了一个asi的not own  553

region universe sharpe fitness margin

ASI MINVOL1M 7.2200 7.5700 0.0022

IND TOP500 3.7500 5.0700 0.0054

今日base指标：

sa:55.5刀,交的是asi not own 553，交的还是存货，最近都不用回测sa

ra:3.68刀，相较于昨天交的eur，带了主题的比没有主题的还是多了个一倍

=============================越努力，越幸运==============================


---

### 技术对话片段 30 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月7日（回忆版）

又是缺粮的一天，今天交了一个eur的ra来过过渡，顺便降低一下平均prod，交了一个eur own 555

region universe sharpe fitness margin

EUR TOP2500 6.9300 6.5000 0.0018

EUR TOP2500 1.9400 1.1100 0.0012

今日base指标：

sa：9.94刀，eur的own的555，最近eur的三五存货交完了，要重新回测了，但是我发现现在比以前更难出三五，测了几十个都没出

ra:1.94刀,太少了太少了

==============================越努力，越幸运==============================


---

### 技术对话片段 31 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月8日(回忆版)

今天只交了两个alpha，一个asi的not own 553,还有一个ind的model ppa;

指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 8.4200 8.3400 0.0020

IND TOP500 1.9500 2.5800 0.0035

今日base指标：

sa:56.32刀,553的威力还是猛

ra:6.32刀，给的真多，就交一个就给这么多，太阳出西边出来了

===========================越努力，越幸运====================================


---

### 技术对话片段 32 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月9日（回忆版）

今天依旧交了两个alpha，库存已经没有了，相冲grandmaster还是有点难度啊，点塔是个大问题，交的是ind的ppa的model，指标非常爆炸，sa交的是eur的own的55吧，没有去追求555了，没啥意义

指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.9800 5.9200 0.0023

IND TOP500 3.5300 4.4900 0.0032

今日base指标：

sa:10.43刀，交的是eur own 557,拿那么多也算可以的了

ra:3.09刀，不错啊，之前交一个就1.9刀，进步了不少

=================================越努力，越幸运=============================


---

### 技术对话片段 33 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月10日（回忆版）

今天交了3个alpha,有进步了，交的是2个ind的ppa，之后还交了一个asi的not own 553，还是很不错的，ind的ppa还是特别好做，就是robust难搞

今日指标：

region universe sharpe fitness margin

ASI MINVOL1M 10.5100 10.6700 0.0021

IND TOP500 2.2000 2.0800 0.0071

IND TOP500 1.5300 1.3200 0.0033

今日base指标：

sa:9.71刀，原来交的时候交错了，交上去pc变成0.31了，错失好几十刀，太心痛了

ra:4.28刀，

===================================越努力，越幸运=============================


---

### 技术对话片段 34 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月11日（回忆版）

今天竟然交满了，为了点塔，把前几天回测的货拿出来跑一跑出来了一大堆，交了4个ind的ppa，和一个asi not own 553，

指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.3000 5.5000 0.0022

IND TOP500 2.3900 2.1600 0.0016

IND TOP500 1.9200 1.8200 0.0020

IND TOP500 1.7700 1.3400 0.0018

IND TOP500 1.3500 1.5900 0.0143

今日base指标：

sa:56.31刀，给力了，爽爽爽，asi not own 553

ra:4.58刀，四个才这么少一点，以前四个可是能有7 8 刀的啊

=================================越努力，越幸运================================


---

### 技术对话片段 35 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月12日（回忆版）

今天依旧交满了，很开心啊，快速点塔追上大部队，今天交的是4个ind的ppa，还有就是一个asi的not own 553，因为感觉快更新vf了，对vf没有什么把握，先把not own交完了再说，

今日指标：

region universe sharpe fitness margin

ASI MINVOL1M 7.1700 8.2800 0.0027

IND TOP500 3.1800 3.9100 0.0030

IND TOP500 1.9100 1.9100 0.0028

IND TOP500 1.8500 1.8200 0.0026

IND TOP500 1.6000 1.3700 0.0024

今日base指标：

sa:53.41刀,比昨天的asi not own 553少了3刀啊，不知道为什么

ra:4.77刀，比昨天略多一点点

===============================越努力，越幸运==================================


---

### 技术对话片段 36 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月13日（回忆版）

今天交满了，今天是交满的第三天了，依旧4个ind的ppa加一个eur的own 557，表现依旧很强啊今天

今日指标如下：

region universe sharpe fitness margin

EUR TOP2500 7.8900 9.5400 0.0038

IND TOP500 3.2400 2.9000 0.0016

IND TOP500 2.7800 3.1200 0.0037

IND TOP500 2.3300 3.5800 0.0168

IND TOP500 2.0100 1.7900 0.0016

今日base指标如下：

sa:8.55刀，交的eur own 557，base是显著下降啊，不过就算交的是555，也就估计10刀左右吧

ra:4.83刀，每天都在上升，但是没有什么用

==============================越努力，越幸运================================


---

### 技术对话片段 37 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月14日（回忆版）

今天没有交满了，今天交的是ind的3个ppa，和一个asi 的not own 的553,总计一共4个，前面交的太猛了，需要缓冲以下子了，

今日指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.7400 6.1800 0.0023

IND TOP500 2.8700 3.1600 0.0024

IND TOP500 1.7600 1.7600 0.0022

IND TOP500 1.5300 1.1300 0.0056

今日base指标如下：

sa:53.54刀，交的还是asi的not own 553，最近都在交asi,正好马上要出glb的theme了，准备not own转战glb试试

ra:4.03刀，下降了

==========================越努力，越幸运===============================


---

### 技术对话片段 38 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月15日（回忆版）

今天交了3个alpha，都是ind地区的，包括两个ind ppa和一个ind own sa，ind的sa指标看着特别舒服，margin和fitness看着都特别高，

alpha指标如下：

region universe sharpe fitness margin

IND TOP500 6.0900 10.3900 0.0080

IND TOP500 2.7500 2.9500 0.0024

IND TOP500 1.6400 1.9500 0.0097

今日base指标如下：

sa:8.55刀，上个月这个时候同样的双五要比这个低一点，交的是ind的own 557，

ra:3.37刀，两个alpha

================================越努力，越幸运==================================


---

### 技术对话片段 39 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月16日（回忆版）

今天同样交了3个alpha，包括两个ind的ppa点塔和一个asi的not own 553，此时ind地区的塔基本上1点的差不多了，没一个塔点了就撤，剩下的留给下一个赛季，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.0800 5.3200 0.0022

IND TOP500 2.4000 2.5000 0.0022

IND TOP500 1.9900 2.6200 0.0149

今日base指标如下：

sa:53.51dao,交的是asi的not own 553，相比前几天少了两三刀的样子

ra:3.88dao，比昨天高，估计是pc有点低

=============================也越努力，越幸运===============================


---

### 技术对话片段 40 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月17日（回忆版）

今天仍然交了3个alpha，交了两个ind的ppa和一个ind的own sa，ind到现在已经交了二十多个了，model还有十多个存货没有交，打算再交几个model的来稳一稳凑够30个，

今日alpha指标如下：

region universe sharpe fitness margin

IND TOP500 6.3600 9.9400 0.0064

IND TOP500 2.7600 2.7800 0.0043

IND TOP500 2.3500 2.3400 0.0033

今日base指标如下：

sa:8.76dao，可能是要多了一点，无关大雅，交的own sa ind 557，也就这样

ra:4.37dao，比前几天交的大概多了不到一刀的样子

==============================越努力，越幸运=============================


---

### 技术对话片段 41 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月18日（回忆版）

今天只交了两个alpha，交的是一个ind的ra，还有交的一个是glb的not own 553，之前一直没有在glb做过sa，今天去试了试，大概回测50个，找到了一个553，也是第一次在除了asi之外做出了一个553，但是指标并没有asi那样高，

今日alpha指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 6.3400 5.3400 0.0015

IND TOP500 1.2300 1.0600 0.0111

今日base指标如下：

sa:56.43dao，glb的not own 553确实要比asi的高个一两刀吧，但是效果也不是很明显

ra:1.97刀，果然，交的少就是给的少

==========================越努力，越幸运==========================


---

### 技术对话片段 42 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月19日（回忆版）

今天只交了两个alpha，同样是交的ind的一个ra，还有一个ind的sa，现在做ind的own sa有点困难了，做了一百多个才出了一个pc小于0.7的，这样有点难搞哦，ind的ra提交也快进入尾声了，已经在做glb了，glb回测真啊，很难回测完

今日alpha指标如下:

region universe sharpe fitness margin

IND TOP500 5.2100 7.2600 0.0039

IND TOP500 2.3400 2.1100 0.0016

今日base指标如下:

sa:8.69dao,交的是ind own 557，竟然比平时交的双五又要多一点了

ra:3.61dao，交一个竟然比前几天交两个甚至三个还要多，估计是pc比较低吧，搞不懂

=============================越努力，越幸运=============================


---

### 技术对话片段 43 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月20日（回忆版）

今天交了3个alpha，其中包括两个ind的ra，和一个asi的not own 553，到目前为止点了14个塔了，点塔好困难啊，而且glb只开放了四个塔的ppa，这不就是变相的只能做ra了吗，可是现在做ra好困难，很多存货都没有了，点到60个塔也太难了，时间和精力花在这上面的时间只能越来越多，但是一个gm也给的多啊，只要有机会，还是要继续冲gm的，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 6.5400 5.8800 0.0016

IND TOP500 1.9400 1.5800 0.0028

IND TOP500 1.8400 1.7900 0.0059

今日base指标如下;

sa:58.47dao，交的是asi 的not own 553，也是第一次553拿到这么高，有点高兴

ra:350dao，交了两个

============================越努力，越幸运===============================


---

### 技术对话片段 44 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月21日（回忆版）

今天交了两个alpha,也是过了十多天再次交eur啊，交的是一个eur的ra和一个eur的own sa，主要是glb出的货不多，而且质量是真的很差，所以交了一个eur的ra点了两个塔，现在我点到16个塔了，长路慢慢啊，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.5300 5.2500 0.0020

EUR TOP2500 1.9400 1.4200 0.0025

今日base指标如下:

sa:8.74dao,还行吧，就这个水平，就只有那么多

ra:1.93dao，一个，大多数情况就是这么多，没有主题

=================================越努力，越幸运=============================


---

### 技术对话片段 45 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月22日

今天交了四个alpha，其中有三个ind的ra，以及一个asi的not own 553，虽然现在ppa主题在glb，但是那些数据集出不了什么特别好的alpha，于是我就继续去做ind，做ra来点点塔，争取再多点一两个，glb暂时先不交，看情况，

今日alpha指标如下:

region universe sharpe fitness margin

ASI MINVOL1M 7.4100 7.1400 0.0019

IND TOP500 2.6600 2.3200 0.0015

IND TOP500 2.0400 1.7700 0.0017

IND TOP500 1.5800 1.5100 0.0061

今日base指标如下：

sa:56.25dao,交的是asi 的not own 553

ra:4.51dao,交了三个非主题ind 的ra

=================================越努力，越幸运==================================


---

### 技术对话片段 46 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月23日

今天就只交了两个alpha了，交的是一个glb的主题ppa和一个ind的own sa,ind的sa我是把那些os表现不好的打上标，之后选alpha的时候就不选这些，不然看着太难受了，这样做出来的sa看着还挺漂亮的，glb还是得交着走啊，这个月就开eur ind glb这三个地区吧，剩下这几天要多交glb的ra啊，不然交的太少了容易炸，

今日alpha指标如下：

region universe sharpe fitness margin

IND TOP500 5.4100 7.7200 0.0041

GLB MINVOL1M 2.1700 1.3400 0.0009

今日base指标如下：

sa:8.4dao,交的Ind own sa 557，目前不想去刻意做三五，就回测十多个交了就好了

ra:2.39dao，一个glb的主题ppa，没有主题差不多应该1.9刀的样子

=================================越努力，越幸运==============================


---

### 技术对话片段 47 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月24日

今天交了4个alpha，其中包括一个asi的not own 553和两个glb的ra以及一个glb的ppa，glb的点塔之路好漫长，回测太慢了一点也不想做，外加只能四个槽，ra也不好做，而且做出来的margin都好低，为了点塔只能适度交一些margin789之类的了，希望后面能够多产出一些margin高的，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.5500 6.1400 0.0027

GLB MINVOL1M 2.3000 1.3600 0.0008

GLB MINVOL1M 2.0300 1.1500 0.0008

GLB MINVOL1M 1.3800 0.9100 0.0046

今日base指标：

sa:54.67dao,交的是asi的not own 553,还是牺牲了一些表现，更新os之后23年的质量实在是太差了

ra:3.47dao，交了两个ra和一个ppa

=================================越努力，越幸运================================


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月25日

今天终于是交满了，今天交了4个glb的alpha，有三个glb的ra以及一个glb的ppa,还交了一个eur的own 557，目前已经点了19个塔，这个月的目标是希望能够点到23个，下个月春节没有多少时间去点塔了，这个月多点一点，后面就没有什么时间了，glb还能再点几个，ind也还能点，eur等主题ppa吧，没有的话就放在下个月吧，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.2200 5.6700 0.0028

GLB MINVOL1M 2.8800 1.9100 0.0009

GLB MINVOL1M 2.3000 1.2300 0.0013

GLB MINVOL1M 1.6700 0.8300 0.0012

GLB MINVOL1M 1.6500 1.0800 0.0010

今日base指标：

sa:8.22dao,交的是eur own 557,

ra:4.41dao交的是3个ra和一个主题ppa

=================================越努力，越幸运================================


---

### 技术对话片段 49 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月26日

今天又是交满了的一天，今天交了5个alpha，包括一个asi的not own 553，以及一个glb的ra和三个Ind的ra，终于又是交满了，这个月快结束了，开了三个地区，必须要快点点完，还要多交一点，ind就这样了，eur不想点了，就好好做一下glb吧，

今日alpha指标：

region universe sharpe fitness margin

ASI MINVOL1M 5.5500 5.1400 0.0017

IND TOP500 2.6400 3.2100 0.0035

GLB MINVOL1M 2.0700 1.2500 0.0010

IND TOP500 2.0100 1.7300 0.0017

IND TOP500 1.9300 1.7900 0.0039

今日base指标：

sa:52.4dao,今天太少了，越来越少了，交的asi的not own 553

ra:6.8dao，最多的一天，交14个ra

===================================越努力，越幸运=============================


---

### 技术对话片段 50 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月27日

今天只交了三个alpha,包括eur的own 557,以及两个glb的ra，glb交的alpha的margin都不行啊，但是为了点塔我还是交了吧，做eur不作glb是因为懒，eur的好做，glb的太难做了，随便测一下eur的pc小于0.7的就好了，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.3000 5.1000 0.0021

GLB MINVOL1M 2.1500 1.3800 0.0011

GLB MINVOL1M 1.9300 1.2300 0.0013

今日base指标如下：

sa:8.35dao,交的是eur的own 557,正常水平

ra:2.58dao,这也太少了，而且还是两个glb的ra，给这么少看都不想看

==========================越努力，越幸运=============================


---

### 技术对话片段 51 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月28日

今天我交了4个alpha，其中包括asi的not own 553，以及三个glb的ra,现在还在疯狂的点glb的塔，不想交ppa只好全部去做ra了，不做ppa主要是因为那些数据集太ex了，出来的质量太差了而且出货率太感人了，与其花费这个精力还不如直接去做ra来的舒坦一点，

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 5.7700 6.0000 0.0022

GLB MINVOL1M 2.2500 1.3000 0.0007

GLB MINVOL1M 1.8900 1.3200 0.0012

GLB MINVOL1M 1.4500 1.1300 0.0012

今日base指标如下：

sa:53.12dao,比上次稍微多了一点点而已，交的是asi的not own 553，趁着vf还不算低赶紧的去交一点，先甜后苦

ra:4.42dao，三个，这么多，还算可以的了

================================越努力，越幸运==========================


---

### 技术对话片段 52 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月29日

今天我只交了两个alpha,因为确实不想多做了，这个pc获取的太慢了，根本就没心情去等，就交了一个eur的own sa557和一个glb的ra来摆一摆吧，想等哪天prod获取不那么久了再开始多交一点，要快快修复啊，太难熬了，这个限流太让人头大了，什么也干不了，

今日alpha指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.9600 5.9000 0.0020

GLB MINVOL1M 2.8100 1.4000 0.0005

今日base指标如下：

sa:8.27dao,交的是eur的own sa557,已经过了很久很久没有交555了，我现在交own的话就每天回测一轮25个随便交一个比较好的就好了

ra:2.57dao，还不错，平时交一个只有1.9dao的样子

===============================越努力，越幸运===============================


---

### 技术对话片段 53 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年1月30日

今天我交了4个alpha,都是在早上1点，12点开始提交的，晚上忘记交了，主要是不想去等获取pc，今天早上起来开始搓alpha，搓出来了三个glb的ra，于是开始提交，一直没有交上去，本来打算交满的，因为这个月快结束了，glb的点塔任务还空余了一点，想抓紧点的，结果根本就交不上去，交的是3个glb的ra，和一个asi的not own 553,

今日alpha指标如下：

region universe sharpe fitness margin

ASI MINVOL1M 6.4300 6.9500 0.0023

GLB MINVOL1M 2.9500 2.0900 0.0010

GLB MINVOL1M 2.3600 1.4100 0.0007

GLB MINVOL1M 1.8700 1.0500 0.0006

今日base指标：

sa:53.4dao，基本上交的是asi的not own 553，也就是这个水平吧

ra:5.39dao，交了三个，这么多还不错哦

==================================越努力，越幸运=========================


---

### 技术对话片段 54 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月8日

在连续了7天交满alpha的情况下今天断了，只交了2个ppa和一个own sa，指标如下：

USA  Statistical  4.85  11.48%  15.83%  14.51‱  4.13

EUR  Subindustry  1.44  7.00%  10.01%   13.98‱  1.08

USA  Statistical  1.49  3.42%  6.85%  9.97‱  0.78

============================坚持！=========================


---

### 技术对话片段 55 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月9日

今天交了2个ppa和一个sa，指标如下：

EUR  Subindustry  5.43  18.02%  9.17%  39.29‱  6.52

EUR  Subindustry  1.65  3.41%  5.30%  12.87‱  0.86

USA  Crowding Factors  1.30  13.34%  17.25%  15.47‱  1.14

这段时间在编写自己的工作流，正好把数据库建立起来，没有多少时间调试alpha，导致alpha提交数量太少了

=======================================坚持！====================================


---

### 技术对话片段 56 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月10日

连续三天只交了2个ppa和sa了，ra越来越难出了目前主要集中火力做usa和eur的d1，有空也会做asi的d1，打算的是10月把usa eur asi的d1的塔点了，顺带做点glb

今日指标如下：

2.05  5.34%  8.49%  12.58‱  1.34

EUR  Fast Factors  7.10  15.27%  11.96%  25.54‱  7.85

USA Subindustry  1.51  4.52%  3.43%  26.31‱  0 .91

======================================坚持！===============================


---

### 技术对话片段 57 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月11日

今天终于是交满了，只可惜全是ppa，好久都没有出ra了，数据库也是建好了，方便了许多，工作流也是建好了，但是还不够稳定，后面还是要慢慢完善以下，今日alpha指标如下：

USA  Subindustry  1.24  4.53%  8.91%  10.17‱  0.75

USA  RAM  1.43  8.38%  8.36%  20.04‱  1.17

USA  Subindustry  1.35  4.92%  3.86%  25.49‱  0.85

USA  Subindustry  2.27  5.25%  3.24%  32.43‱  1.47

EUR  Statistical  5.69  11.62%  13.67%  16.99‱  5.25

======================================坚持！====================================


---

### 技术对话片段 58 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月12日

今天做的是usa的instituions，还是比较难做，还是做出来了3个atom，还有一个本该是option的ra的，结果交的时候不小心把描述写了交成ppa了，这个月一个not own都还没有交，才拿到not own权限还在研究，后面慢慢交一点not own的了，今日指标如下：

USA  RAM  1.93  3.60%  4.17%  17.26‱  1.04

EUR  Statistical  6.97  13.01%  13.18%  19.74‱  6.92

USA  Subindustry  1.74  3.39%  2.99%  22.68‱  0.91

USA  Statistical  1.78  8.82%  8.08%  21.83‱  1.50

USA  Industry  1.29  4.09%  2.39%  34.13‱  0.74

=================================坚持！======================================


---

### 技术对话片段 59 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月13日

今天在服务器特别卡的情况下还是交满了，交了四个ppa和一个ra，其中交了3个eur的imbalance数据集的alpha成功点亮imbalance的塔，虽然imbalance的数据集很少，但质量也是非常不错的，但是我也有点忧虑，ppa的sharpe能达到4＋，这种alpha真的没有问题吗？

==============================坚持！=======================================


---

### 技术对话片段 60 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月15日

今天交了2个ppa，一个ra，一个own sa，2个eur的fundamental数据集，和一个usa的analyst数据集的，指标如下:

EUR Market  1.98  6.61%  2.24%  59.12‱  1.44

EUR Subindustry  1.47   3.91%  4.15%  18.84‱  0.82

EUR Statistical  6.24  10.38%  14.99%  13.85‱  5.19

USA Subindustry  1.87  5.55%  8.25%  13.45‱  1.25

====================坚持！==================================


---

### 技术对话片段 61 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月14日

今天成功交满，交的是4个ppa和own的sa，4个ppa全是asi地区的，提交速度也是非常快，其中有2个imbalance数据集的，一个fundamental数据集的，还有一个broker数据集的，缺点就是turnover有点低了，margin也低了，指标如下：

ASI  Statistical  2.61  3.80%  7.51%  10.10‱  1.44

ASI  Statistical  1.65  2.79%  5.46%  10.24‱  0.78

ASI  Fast Factors  1.56  4.17%  9.78   %8.52‱   0.90

ASI  Industry  1.49  3.72%  9.25%   8.05‱   0.81

================================坚持！===================================


---

### 技术对话片段 62 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月16日

今天交了2个ppa和1个sa，今天是有not own以来第一次组出来了三五，但是还没打算交，想等vf更新了再交试试，现在vf0.41，很大一部分的影响是iqc期间，第一次更新vf是0.25，现在每天basepayment在3美元以上，但也是真不多啊，还是期待vf快点更新

===============================坚持！===================================


---

### 技术对话片段 63 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月17日

今天交了4个alpha,其中一个sa，一个ra,两个ppa，还是没交满，产率真的有点低了，也不想交存货，第一存货大多数是analyst,fundamental,model这种大数据集的，之前已经交了很多了，第二就是pc还是有点偏高，平台终于不卡顿了，可以从ASI转战到USA和EUR地区了，今天交的ra指标：

USA  Crowding Factors  1.76   4.01%  7.55%  10.62‱  1.00

====================================坚持！====================================


---

### 技术对话片段 64 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月18日

今天交了4个ppa和一个superalpha，最近开始点小数据的塔了，alpha是真的难出啊，就算出了也是高turnover低fitness低margin的，都引发提交焦虑了，又相交又不想交，但是我还是觉得diversity是比较重要的，还是交了，指标如下：

USAStatistical1.76  3.20%  15.29%  4.18‱  0.81

USAStatistical1.46  3.47%  7.48%   9.29‱  0.77

USASubindustry1.93  4.97%  9.53%  10.43‱  1.22

EURFast Factors1.45  2.29%   5.77%  7.91‱  0.62

================================坚持！=================================


---

### 技术对话片段 65 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月19日

今天是做小数据集的第二天，虽说小数据集难做，但是出的货也不少，就是质量实在是不好，今天仍然是交满了，并且一次性提交了两个ra,可以说还是有进步的，指标如下：

USA   Statistical  1.67  10.48%  11.82%  17.73‱   1.53

USA   Subindustry  1.72  5.02%  4.54%  22.14‱   1.09

ASI   Statistical   1.21  3.40%  6.54%   10.41‱   0.63

ASI   Slow + Fast Factors   1.38   2.78%  5.85%  9.49‱  0.65

================================坚持！============================


---

### 技术对话片段 66 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月20日

今天是做小数据集的第3天，今天仍然是交满了，交了4个ppa，很遗憾没有做出ra，质量总体来说算不错的了，就是returns和fitness偏低了，我最近的回测框架也差不多优化结束了，效率还是杠杠的，有空可以分享出来，指标如下：

USA  Statistical  1.55  2.40%  4.41%1  0.88‱  0.68

USA  Subindustry  1.17   4.31%  7.03%  12.25‱  0.69

USA  Subindustry   1.58  4.75%  4.55%  20.87‱  0.97

USA  Market   1.79   5.71%   20.67%   5.53‱   0.94

============================坚持！===============================


---

### 技术对话片段 67 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月21日

今天是做小数据集的第4天，今天交了3个ppa,质量大不如以前了，因为剩下的这些数据集太难出货了，至此，USA的小数据集完成了80%了，现在开始了对EUR的进攻，并且我找到了一个新的思路，待我尝试尝试看看效果怎么样，今日指标如下，margin普遍拉跨，后面要多交高margin来和这些alpha中和一下：

EUR  Subindustry  1.82  7.54%  20.47%  7.36‱  1.10

USA  RAM  3.61  9.88%  32.02%  6.17‱  2.01

USA  Statistical   1.25  2.98%  9.88%  6.03‱  0.61

===========================坚持！===================================


---

### 技术对话片段 68 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月22日

今日交了三个alpha,其中2个ppa,一个sa，依旧在做小数据集，做出来了一个social的，产量明显跟不上了，最近很吃力啊，指标如下：

USA  Sector  1.91   6.17%   9.27%   13.30‱   1.34

USA  Slow + Fast Factors   5.46   13.29%   11.72%   22.69‱   5.63

EUR  Subindustry   1.24  9.20%   18.89%   9.74‱   0.87

===============================坚持！==================================


---

### 技术对话片段 69 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月23日

今天交了四个alpha，其中3个ppa，一个sa，做的是eur的analyst和model，做小数据集实在做不下去了，做一做大数据集缓缓气。今天也是更新vf了！vf从0.5-0.25-0.41-0.91,终于出狱了，还是听weijie老师的多交atom管用，严格控制质量。

今日base记录：

ra:5.18   2个主题加一个非主题，fitness:1.39 1.82  1.93

sa:9.13  双5

下一日交一个三五试试水，ra base应该是被fitness抬高的

===============================坚持！========================


---

### 技术对话片段 70 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月24日

今天交了5个alpha，其中3个ppa，一个ra，一个sa，今天base还算客观，今天是小数据集混合大数据集一起提交，本来想全部交主题的，但是突然忘了。

今日base记录：

ra:7.15     2个主题加2个非主题，平均fitness:1.1,感觉是今天的pc要低一点给的多一点

sa:14.37  做的是eur not own 三五，fitness只有5，感觉比预期的要低

=============================坚持！======================================


---

### 技术对话片段 71 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月25日

今天也是交了5个alpha，4个ppa和1个sa，感觉更新了vf动力都增加了许多，愿意花更多时间在wq上了，今天交的也是大数据集和小数据集混合，只想快速结束usa和eur的小数据集，点着太痛苦了。

今日base记录：

ra:4.33     4个非主题，平均fitness有1.4，不知道为啥这么少啊

sa:20.16  eur own 三五,而且是665，比555要多5刀左右，下一天再交fitness高一点的三五试试水

============================坚持！=======================================


---

### 技术对话片段 72 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月26日

今天交了3个ppa和一个own的eur 三五，其中三个ppa点了一个eur的other的塔，指标都还好，pc稍微有点高。

今日bsae指标:

sa:11.55刀   775 eur own

ra:8.43  平均fitness 2.1

今天sa的fitness高了竟然还那么低，而ra的base是目前最高的，可见fitness对base的影响还是有的

=================================坚持！=================================


---

### 技术对话片段 73 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月27日

今天交了3个alpha，两个ra和一个sa,两个ra都是eur的model的，存货比较少了，不得不交一点model的，快到月末了，也快结束小数据集的点塔任务了。

今日base指标：

sa: 11.52刀 交的是eur own 565,比昨天交的差了一点居然拿到的钱差不多，基本一样

ra:4.15 平均fitness 1.5 pc也不高啊，而且两个都是ra，拿那么少也很惊讶

===========================坚持！========================================


---

### 技术对话片段 74 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月28日

今天交了5个alpha，有3个ppa，一个ra，一个sa，其中有两个eur 的institutions的ppa和一个usa analyst的ppa，sa交的是eur own 三五，ra 是usa的earnings的二阶，这个二阶是我自己构造的二阶模版跑出来的，最近产量慢慢跟上来了。

今日base指标：

sa:9.74刀  665三五都这么不值钱了吗，出奇的低，这和我第一天交997有什么区别啊，

ra:6.05刀  中规中距吧，没有做主题，这个base也差不多是我的平均水平了

下一步目标是做ASI了，但是我跑起来vector的一直报错，小数据集大多数都是vector，有点难受

=============================坚持！================================


---

### 技术对话片段 75 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月29日

今天交了6个alpha，多交了一个ra啊，太心疼了，今天交的很杂，包括insiders institutions short earnings analyst的都交了，主要是下个月开始ppa只能用风险中性化了，吓得我只好把数据库里面存的alpha拿出来交了，本来打算这些小地区留着下一个赛季点塔用的，我看着换风险中性化之后指标下降的比较多，就干脆这个赛季一并点掉，下一个赛季再想想办法吧，交着交着就忘记自己交了多少个了。

今日base指标：

sa：18.91刀,前几天三五的base一直在下降，今天也是扬眉吐气了一次了，今天搓出来了一个glb的765，还是glb的sa赚钱啊

ra:5.92刀 平均水平，知足了

=====================================坚持！===============================


---

### 技术对话片段 76 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年03月01日

今天交了1个因子，交了1个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.8300 5.3900 0.0031

今日base指标如下:

sa:1.49dao

ra:1.61dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 77 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年03月02日

今天交了2个因子，交了2个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.8300 4.8000 0.0027

GLB MINVOL1M 2.7400 2.0500 0.0015

今日base指标如下:

sa:1.78dao

ra:1.5dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 78 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年03月03日

今天交了5个因子，交了5个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.9000 4.6100 0.0026

GLB MINVOL1M 1.9300 1.4100 0.0020

GLB MINVOL1M 1.7200 1.7000 0.0021

GLB MINVOL1M 1.3100 0.9300 0.0023

GLB MINVOL1M 1.1800 1.0500 0.0017

今日base指标如下:

sa:1.76dao

ra:1.65dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 79 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年03月04日

今天交了3个因子，交了3个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 4.5600 4.1200 0.0023

GLB MINVOL1M 2.5000 1.6400 0.0014

GLB MINVOL1M 1.5500 1.0500 0.0011

今日base指标如下:

sa:1.54dao

ra:1.72dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 80 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2026年03月05日

今天交了3个因子，交了3个glb的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 5.8300 4.5100 0.0016

GLB MINVOL1M 1.3100 1.2300 0.0031

GLB MINVOL1M 1.2500 0.7300 0.0019

今日base指标如下:

sa:1.67dao

ra:1.47dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 81 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月15日

今天交了5个因子，交了2个glb的alpha，和3个EUR的alpha,指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 6.2900 5.1500 0.0017

EUR TOP2500 2.8900 2.0600 0.0010

EUR TOP2500 2.4300 1.6700 0.0009

EUR TOP2500 1.6600 1.1900 0.0010

GLB TOPDIV3000 1.6000 0.9300 0.0009

今日base指标如下:

sa:1.63dao

ra:1.64dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 82 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月16日

今天交了5个因子，交了1个glb的alpha，4个hkg的alpha指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 5.2000 4.1800 0.0017

HKG TOP800 2.0000 2.2600 0.0042

HKG TOP800 1.9400 1.7700 0.0033

HKG TOP800 1.6600 1.6100 0.0022

HKG TOP800 1.6600 1.5800 0.0080

今日base指标如下:

sa:1.65dao

ra:1.51dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 83 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月17日

今天交了5个因子，交了1个glb的alpha，以及4个hkg的alpha，指标如下：

region universe sharpe fitness margin

GLB MINVOL1M 5.4200 4.0500 0.0016

HKG TOP800 2.2100 2.3700 0.0025

HKG TOP800 1.5800 1.5200 0.0128

HKG TOP800 1.4400 1.1400 0.0059

HKG TOP800 1.4200 1.1300 0.0015

今日base指标如下:

sa:1.68dao

ra:1.6dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 84 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月18日

今天交了5个因子，交了1个eur的alpha，4个hkg的alpha,指标如下：

region universe sharpe fitness margin

EUR TOP2500 6.0600 5.9200 0.0019

HKG TOP800 1.9800 2.5900 0.0086

HKG TOP800 1.9400 1.6800 0.0037

HKG TOP800 1.8500 1.8700 0.0079

HKG TOP800 1.5300 1.4200 0.0042

今日base指标如下:

sa:1.69dao

ra:1.54dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 85 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月19日

今天交了5个因子，交了1个eur的alpha，4个hkg的alpha，指标如下：

region universe sharpe fitness margin

EUR TOP2500 5.0000 5.3000 0.0042

HKG TOP800 1.9700 2.1700 0.0024

HKG TOP800 1.6900 1.4000 0.0014

HKG TOP800 1.6100 1.4200 0.0058

HKG TOP800 1.4000 1.5200 0.0041

今日base指标如下:

sa:1.54dao

ra:1.47dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 86 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月20日

今天交了5个因子，交了1个eur的alpha，4个hkg的alpha，指标如下：

region universe sharpe fitness margin

EUR TOP2500 6.7400 6.2600 0.0017

HKG TOP800 2.0500 2.4700 0.0041

HKG TOP800 2.0500 2.0000 0.0039

HKG TOP800 1.3300 1.0100 0.0023

HKG TOP800 1.2100 0.8300 0.0021

今日base指标如下:

sa:1.51dao

ra:1.64dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 87 (原帖: 2026/03/06)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季](../顾问 NL80893 (Rank 16)/[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN](/hc/en-us/community/posts/37796479641111--%E6%97%A5%E5%B8%B8%E7%94%9F%E6%B4%BB%E8%B4%B4-%E6%88%91%E7%9A%84%E9%87%8F%E5%8C%96%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%B9%9D%E5%AD%A3) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记（回忆版）

日期：2026年02月21日

今天交了5个因子，交了5个hkg的alpha，指标如下：

region universe sharpe fitness margin

HKG TOP800 4.0300 5.6400 0.0068

HKG TOP800 1.9800 1.9900 0.0020

HKG TOP800 1.9500 2.3100 0.0031

HKG TOP800 1.7700 1.5100 0.0020

HKG TOP800 1.6200 1.3200 0.0022

今日base指标如下:

sa:1.67dao

ra:1.45dao

======================================================================

越努力，越幸运

The harder you work, the luckier you get. ======================================================================


---

### 技术对话片段 88 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
25/9/18

今天只交了一个USA的ppa，指标如下：

1.72   sharpe

4.69%  returns

3.87%  turnover

24.24‱    margin

1.05    fitness

turnover偏低了，生产相关性还是很高，自己开发的模板中有生产相关性低的alpha但操作符很多，而且产出率比较低，经常断交，并且为了保持住6维，很难做取舍，后面要多学习多做低相关性低操作符的alpha


---

### 技术对话片段 89 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
25/9/19

今天交了一个USA的ppa,指标如下：

1.78 sharpe

3.63% returns

17.37% turnover

4.17‱ margin

0.81 fitness

除了sharpe各指标都不好，因为想着看能不能冲下榜，还是没忍住交了，通过调ts_target_tvr_decay在提高margin的同时会损失大部分的sharpe，同时要想想办法去提高alpha的产率了，或许不应该着急，沉下心来用心去研究alpha


---

### 技术对话片段 90 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
2025年9月21日

今天也只交了一个ppa

USA

1.40    sharpe

5.03%   returns

10.77%  turnover

9.34‱    margin

0.89    fitness

断粮有点难受，外加vf0.41，即使比上次0.25的高，但base没有什么变化，但也不能只在意base，还是要只交好的，不能交差的，等把iqc期间交的差的因子都滚动掉我的vf会迎来晴天的。


---

### 技术对话片段 91 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
日期：2025年9月22日

今天是连续回测的第82天，因为iqc结束断了一周，导致我的连续回测天数很拉跨，在genius上面的竞争很难受，但好在接近3个月的坚持与努力，排名也是维持在了master的要求附近（不包括grandmaster 的情况下）

今天交了一个ppa：

USA

1.55     sharpe

4.87%   returns

4.64%   turnover

20.98‱    margin

0.97   fitness

质量不算好，但还过的去，另外最近在尝试新的模板，我发现这个模板出的货普遍生产相关性比较低，质量也说的过去，这给了我一定的自信心


---

### 技术对话片段 92 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
日期：2025年9月23日

连续十天每天只交一个alphal了，不知道这样的日子能维持到什么时候，交的少会影响vf，看来后面几天我要多交一点了，把前面囤的没有交的再拿来测一测相关性

今日alpha：

Sharpe：

1.44

Turnover：

17.63%

Fitness：

1.08

Returns：

10.00%

Drawdown:

10.05%

Margin:

11.34‱

仍然是个ppa，希望明天我能多交一点，每天都在进步！


---

### 技术对话片段 93 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月24日

今天是连续回测的84天，目前在回测usa地区的risk数据集，发现我所使用的模板回测出来的alpha其大多数sharpe是负的，并且正的sharpe竟然没有大于1的，而负的sharpe可以达到-1.91，我果断将所有的负sharpe的alpha全部反转，得到了许多比较优质的alpha，并且prod相关性还是比较低的


---

### 技术对话片段 94 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月25日

今天是我连续回测的第85天

最近遇到了瓶颈，很难找到prod比较低的alpha，也不愿意交比较高的prod的alpha了，而且经过一个早上和一个晚上，我的genius排名又降了6名，而目前而言前310才有希望进master，而我现在276，每天都这么降的话进master还是有点悬，还得继续努力啊


---

### 技术对话片段 95 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月26日

今天是我坚持连续回测的85天，再撑几天这个赛季就结束了，希望排名和combine能保住master，一直看着排名唰唰下降心里还是很难受，现在在master的universe内排282，还是特别危险，而且还要谨防有些人最后来偷塔

====================================================================


---

### 技术对话片段 96 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
25/9/18

今天只交了一个USA的ppa，指标如下：

1.72   sharpe

4.69%  returns

3.87%  turnover

24.24‱    margin

1.05    fitness

turnover偏低了，生产相关性还是很高，自己开发的模板中有生产相关性低的alpha但操作符很多，而且产出率比较低，经常断交，并且为了保持住6维，很难做取舍，后面要多学习多做低相关性低操作符的alpha


---

### 技术对话片段 97 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
25/9/19

今天交了一个USA的ppa,指标如下：

1.78 sharpe

3.63% returns

17.37% turnover

4.17‱ margin

0.81 fitness

除了sharpe各指标都不好，因为想着看能不能冲下榜，还是没忍住交了，通过调ts_target_tvr_decay在提高margin的同时会损失大部分的sharpe，同时要想想办法去提高alpha的产率了，或许不应该着急，沉下心来用心去研究alpha


---

### 技术对话片段 98 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
2025年9月21日

今天也只交了一个ppa

USA

1.40    sharpe

5.03%   returns

10.77%  turnover

9.34‱    margin

0.89    fitness

断粮有点难受，外加vf0.41，即使比上次0.25的高，但base没有什么变化，但也不能只在意base，还是要只交好的，不能交差的，等把iqc期间交的差的因子都滚动掉我的vf会迎来晴天的。


---

### 技术对话片段 99 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
日期：2025年9月22日

今天是连续回测的第82天，因为iqc结束断了一周，导致我的连续回测天数很拉跨，在genius上面的竞争很难受，但好在接近3个月的坚持与努力，排名也是维持在了master的要求附近（不包括grandmaster 的情况下）

今天交了一个ppa：

USA

1.55     sharpe

4.87%   returns

4.64%   turnover

20.98‱    margin

0.97   fitness

质量不算好，但还过的去，另外最近在尝试新的模板，我发现这个模板出的货普遍生产相关性比较低，质量也说的过去，这给了我一定的自信心


---

### 技术对话片段 100 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
日期：2025年9月23日

连续十天每天只交一个alphal了，不知道这样的日子能维持到什么时候，交的少会影响vf，看来后面几天我要多交一点了，把前面囤的没有交的再拿来测一测相关性

今日alpha：

Sharpe：

1.44

Turnover：

17.63%

Fitness：

1.08

Returns：

10.00%

Drawdown:

10.05%

Margin:

11.34‱

仍然是个ppa，希望明天我能多交一点，每天都在进步！


---

### 技术对话片段 101 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月24日

今天是连续回测的84天，目前在回测usa地区的risk数据集，发现我所使用的模板回测出来的alpha其大多数sharpe是负的，并且正的sharpe竟然没有大于1的，而负的sharpe可以达到-1.91，我果断将所有的负sharpe的alpha全部反转，得到了许多比较优质的alpha，并且prod相关性还是比较低的


---

### 技术对话片段 102 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月25日

今天是我连续回测的第85天

最近遇到了瓶颈，很难找到prod比较低的alpha，也不愿意交比较高的prod的alpha了，而且经过一个早上和一个晚上，我的genius排名又降了6名，而目前而言前310才有希望进master，而我现在276，每天都这么降的话进master还是有点悬，还得继续努力啊


---

### 技术对话片段 103 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月26日

今天是我坚持连续回测的85天，再撑几天这个赛季就结束了，希望排名和combine能保住master，一直看着排名唰唰下降心里还是很难受，现在在master的universe内排282，还是特别危险，而且还要谨防有些人最后来偷塔

====================================================================


---

### 技术对话片段 104 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月27日

今天是我连续回测的第86天了，目前genuis排在第296，在master的边缘徘徊，最后这几天不得不冲刺了，不然迟早会掉出master的，翻翻库存，多交一点alpha，能加几名算几名，大家也要一起努力啊！

=============================坚持！！！===============================================


---

### 技术对话片段 105 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年9月28日

今天是我坚持连续回测的第87天了，我想了一下，最后三天或者两天的时间内想要冲刺genuis的唯一方法就是多交低op的alpha来降低avg op了，这个赛季交的alpha还是有点少了，毕竟刚结束iqc初来乍到走了很多坑，能到达这个排名心里已经算很满足了，现在坚持每天交满四个alpha，最后是否能到master就看运气了


---

### 技术对话片段 106 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月1日

今天交了四个alpha，其中两个ra和两个ppa，其sahrpe,returns,turnover,margin,fitness如下：

USA

1.68

4.89%

6.93%

14.11‱

1.05

USA

2.48

114.24%

7.21%

316.86‱

7.50

USA

1.79

6.85%

14.54%

9.43‱

1.23

USA

1.67

7.45%

3.60%

41.41‱

1.29

====================10月平均prod:0.73,今日平均prod:0.73，较上一日进步：0========================


---

### 技术对话片段 107 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月2日

今天交了四个alpha，全是ppa，其sahrpe,returns,turnover,margin,fitness如下：

EUR

1.83

3.62%

4.53%

15.98‱

0.98

USA

1.75

8.45%

8.20%

20.63‱

1.44

1.93

5.74%

11.38%

10.08‱

1.31

ASI

2.09

3.93%

9.12%

8.63‱

1.17

======10月平均prod:0.7385,今日平均prod:0.7475，较上一日进步：-0.009==============


---

### 技术对话片段 108 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月3日

今天交了四个alpha，3个ppa一个ra，其sahrpe,returns,turnover,margin,fitness如下：

EUR：2.44  4.46%  10.86%  8.21‱  1.46

1.36  6.13%  10.74%  11.40‱  0.95

1.59  2.96%  6.03%  9.83‱  0.77

USA：1.24  27.53%  24.80%  22.20‱  1.31

======10月平均prod:0.7131,今日平均prod:0.6625，较上一日进步：0.085==============


---

### 技术对话片段 109 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月4日

今天交了四个alpha，2个ppa2个ra，其sahrpe,returns,turnover,margin,fitness如下：

EUR:1.37  3.68%  3.23%  22.77‱  0.74

1.65  4.60%  10.38%  8.86‱  1.00

1.50  2.81%  4.22%  13.31‱  0.71

ASI:  2.02  4.06%  9.09%  8.93‱  1.15

=========10月平均prod:0.6960,今日平均prod:0.645，较上一日进步：0.0175==============


---

### 技术对话片段 110 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月5日

今天交了四个alpha，全是ppa，其sahrpe,returns,turnover,margin,fitness如下：

1.36  12.30%  3.99%  61.62‱   1.35

1.44  2.88%  5.07%  11.34‱  0.69

1.46  3.02%  6.56%  9.21‱  0.72

2.26  5.45%  27.68%  3.94‱  1.00

=========10月平均prod:0.6693,今日平均prod:0.5625，较上一日进步：0.0825==============


---

### 技术对话片段 111 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月6日

今天交了四个alpha，其中有3个ppa，1个ra,其sharpe,returns,turnover,margin,fitness的指标如下：

1.58  8.09%  6.50%  24.90‱  1.27

1.36  30.17%  5.86%  102.93‱  2.11

1.21  20.97%  4.56%  91.99‱  1.57

1.48  6.13%  16.79%  7.30‱  0.89

===============10月平均prod:6636  ，今日平均prod:0.635,较上一日进步：-0.425===============


---

### 技术对话片段 112 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 HP65370 (Rank 93) 的解答与建议**:
我的量化日记

日期：2025年10月7日

今天交了三个alpha，其中有1个ppa，2个ra,其sharpe,returns,turnover,margin,fitness的指标如下：

1.95  3.50%   10.35%   6.76‱   1.03

1.63   5.65%   10.30%   10.97‱   1.10

1.68  5.65%   9.70%   11.66‱   1.13

===============10月平均prod:6639  ，今日平均prod:0.6666,较上一日进步：-0.031===============


---

### 技术对话片段 113 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: [Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 冲刺genius !
> 细节决定成败,你的六维还能提升 ! &模板
> 
> 
> 首先感谢游戏王 (2559763) ,
> 橘子姐
> (6383096) ,
> base payment 拉满的
> 大佬 (AH18340) 以及 上海 (MF59400)等等的帮助.也许你们自己都不知道 ,
> 但是潜移默化
> 的影响了我,
> 下面阐述的其中有-些内容是我在游戏王那里学习到的.


## **一、Genius定级与何相干？**

总体来说，一共与两方面有关，一是  **硬性指标** ，二是  **软指标** 。


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-03,July 1st, 2025
> September 3Oth; 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 266
> Reached Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 72
> Reached Grandmaster
> 10
> 30
> Combined Alpha Performance
> 2.39
> Reached Grandmaster
> 0.5


其中  **硬性指标** 包括由

1. 本季度 Signals (阿尔法)；

2. 本季度 Pyramids (金字塔)；

3. Combined Alpha Performance (提交的所有alpha表现)；

4. Combined Selected Alpha Performance (被选中的alpha费后表现)

5. Combined Power Pool Alpha Performance (power pool alpha表现)

五部分组成；

```
点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。
```

我们以Expert (专家)为例，硬性指标必须同时满足

1. 本季度alpha数量 Signals ≥ 20；

2. 本季度金字塔数量 Pyramids ≥ 10，

3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5

       这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).

[图片 (图片已丢失)]

**软指标** 又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。

**
> [!NOTE] [图片 OCR 识别内容]
> What happens 迂 more consultants qualify for a level than there are available
> If more consultants meet the base criteria for
> level than there are available Spots
> a tiebreaker criterion is used _
> This is based on a sum Of ranks across the following metrics
> 1.
> distinct Operators
> Alpha (Lower is better )
> 2.
> distinct Fields
> Alpha (Lower is better)
> 3. Total distinct Operators (Higher is better)
> 4
> Total distinct Fields (Higher is better)
> 5. Maximum Simulation Streak
> Best streak of
> consultant that ends i that quarter
> OI
> continues into the next quarter
> Streak does not reset to 0 every quarter。
> 6. Community leader
> Forum
> Number Of Likes on Posts Or comments that are
> published as Of the end Of quarter
> Ninimm length of post Or comment must be 100 characters。
> Referral
> Total number Of successful referrals i the quarter
> A referral is considered
> Slccessfil
> Khen the
> referring consultant h as become eligible to accrte the referral fee for someone
> have referred to BRAIN
> 讧 accordance with the guidelines Of the referral fee program
> Spots?
> Avg
> AVg
> they
**

**
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st, 2025
> September 3Oth, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.41
> 68
> 1.54
> Fields used
> Community activity
> Max simulation streak
> 260
> 33.2
> 88
**

其中  **软指标** (六维数据)包括由本季度

1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；

2. Operators used (操作符的去重使用个数)；

3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；

4. Fields used (字段使用(去重)数量)

5. Community activity (rank[社区活跃程度])

6. Max simulation streak (最大连续回测天数)

六部分组成；

```
·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。
```

[图片 (图片已丢失)]

## **二、冲刺 Genius !**

通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。

1. 关于六维数据  **细节**

这部分我们娓娓道来，关于六维数据我们能做的是什么?

i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；

ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；

iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；

iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；

v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .

首先，讲讲我的一些  **蠢行为! ,** 等等上面还有一点重要的忘记说了， **要保持区域、Delay以及数据集多样性！**

**
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st, 2025
> September 3Oth, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Fundamental
> Insiders
> Macro
> Mogel
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Social Media
> Earnin3s
**

使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多  **8~10**  个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Delayo
> NAN
> Delayl
> NAN
> Fundamental data
> Fundamental data
> Analyst data
> Analyst data
> Broker
> Broker
> News data
> News data
> Social media data
> Social media data
> Sentiment data
> Sentiment data
> Price VOluMe data
> Price Volume data
> Option data
> Option data
> Eamings
> Earnings
> Insiders
> Insiders
> Instiutional Ownership Data
> Instiutional Ownership Data
> Short interest data
> Short interest data
> Macro data
> Macro data
> Other
> Other
> Risk data
> Risk data
> Model data
> Model data
> USA
> ASI
> CHN
> EUR
> GL
> HKG
> KOR
> TVN
> AMR
> JPN
> USA
> ASI
> CHN
> EUR
> GLB
> HKG
> KOR
> TVN
> AMR
> JPN
> Click to drill down
> EUR
> ASI
> GLB
> USA
> CHN


保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.

[图片 (图片已丢失)]

接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/26/2025 EDT
> 顾问 ML47973 (Rank 100)
> Add Alphato
> LiSt
> Code
> IS Summary
> Period
> IS
> 05
> power(2,
> md177_astcomp
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> Simulation Settings
> 1.65
> 6.11%
> 2.64
> 31.939
> 16.609
> 104.449600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Subindustry
> On
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 1.69
> 5.46%
> 1.56
> 10.65%
> 4.76%
> 39.05920
> 1999
> 357
> 2019
> 4.949
> 1.71
> 18.5896
> 8.66%
> 75.279620
> 1988
> 375
> 2020
> -0.,04
> 029
> 0.01
> 0.5596
> 15.18%
> 82920
> 2010
> 375
> Clone Alpha 
> 2021
> 2.46
> 699
> 4.84
> 48.489
> 15.30%
> 122.899620
> 2142
> 380
> 2022
> 2.44
> 7.42%
> 6.08
> 77.70%
> 13.23%
> 209.41920
> 2136
> 390
> Chart
> Pnl
> 2023
> 3.61
> 6.13%
> 7.40
> 52.519
> 1.71%
> 171.19920
> 2114
> 397
> 匣
> Correlation
> 1ON
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,4;51
> PM
> 0.6840
> -0.0542
> OOOK
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,4;51
> Du
> 0.4204
> -0.1633
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 4;51
> 0
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul "22
> Jan '23
> Du
> 0.6874
> -0.6201
> Vear



> [!NOTE] [图片 OCR 识别内容]
> 这个 Q 当时让我 base payment 日 赚54.816 ,当时 iqc 结束 ,第一次0f更新0.86


直到我使用华子哥的插件才发现


> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 美东时间:2025/9/1200:38:06 北京时间: 2025/9/1212:38:06
> 在你可用的运算符中。共有67种运算符被使用。12种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统一为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x, Y, filter
> false); X + y
> 52
> COMBO,REGULARSELECTION
> base
> Arithmetic
> multiply(x ,y
> filterzfalse); X * y
> 76
> COMBO,REGULARSELECTION
> base
> Arithmetic
> sign(x)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> subtract(x, Y, filter-false) X -Y
> 157
> COMBO,REGULARSELECTION
> base
> Arithmetic
> pasteurize(x)
> COMBO,REGULAR
> genius
> Arithmetic
> log(x)
> COMBOREGULARSELECTION
> base
> Arithmetic
> maXfx;y
> COMBO,REGULARSELECTION
> base
> Arithmetic
> absfx)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> divide(x; y), XIy
> 158
> COMBO,REGULARSELECTION
> base


我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！

下面的操作有几率  **降低** 你的  ***Operators per Alpha*** ，和想要查看自己的alpha数据也可以认真看一下

在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)


> [!NOTE] [图片 OCR 识别内容]
> #  登录 (login)url
> CUrl
> --location
> --request
> POST
> https : / /api. worldquantbrain . com
> authentication
> header
> Authorization:
> Basic MZAZODUBMTAZOEBXcSSjbzeGQUYrQUYrQUYgMBFG
> ~-header
> Cookie:
> t=eyJeeXAiOiJKVIQiLCJhbGciOiJIUZIINiJg .eyJqdGkioi -



> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> login
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> POST
> https:Hapi.orldquantbrain comlauthentication
> Send
> Environments
> POST Simulation
> Params
> Authorization
> Headers (10)
> Body
> Scripts
> Settings
> Cookies
> PATCH alpha-adjust
> FIOws
> Auth Type
> GET data-fields
> Username
> 30-510
> COm
> Basic Auth
> GET alpha
> History
> GET Check
> Password
> The authorization header will be
> POST submit
> 0+
> automatically qenerated when yoU send the
> GET Self-COrr
> Body
> Cookies
> Headers (20)
> Test Results
> 201 Created
> 1.975
> 1.14 KB
> Save Response
> GET data-sets
> JSON
> Preview
> Visualize
> 三
> Q  @
> GET
> pyramid
> USET"
> id
> 顾问 ML47973 (Rank 100)
> Loken"
> EXDiTy
> 14400
> DeTmissions
> BEFORE
> ANID_
> AFTER
> PERFORMANCE_
> 10
> BRAIN_LA3S"
> 11
> BRAIN_LABS_JUPYTER
> L43
> 12
> CONSULTANTI
> 13
> "MULTI_SIMULATION "
> 14
> PROD_ALPHAS
> 15
> REFERRAL
> 16
> SUPER_ALPHA "
> 17
> IVISUALIZATION"
> 18
> WORKDAY"
> 19
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> 9@.


下面的是查询alpha信息的url


> [!NOTE] [图片 OCR 识别内容]
> #
> check_alpha_info 其中{alpha_id} 使用alpha_id替代即可
> Curl
> -location
> https : / /api .worldquantbrain . com/alphas / {alpha_id}
> -header
> Cookie:
> tseyJeexAioiJKVIQiLCJhbGciOiJIUZIINiJ9 .eyJqdGkioi


接下来我们就来看看几个alpha，查看它们的数据情况

1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/09/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> ib5
> SCOFe
> Single Data Set Alpha
> 俳
> Power Pool Alpha
> Pyramid theme: EURIDIIIMBALANCE X2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> Simulation Settings
> 3.37
> 22.089
> 2.26
> 9.9396
> 2.4596
> 9.009o0
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.02
> Statistical
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.19
> 23.9499
> 200
> 14.1990
> 1.08%
> 11.8590
> 1324
> 781
> 2014
> 4.55
> 23.2595
> 3.25
> 11.85%
> 0.78%
> 10.20950
> 1612
> 1005
> 2015
> 4.20
> 23.68%
> 3.26
> 13.02%
> 1.31%
> 11.00930
> 1101
> Clone Alpha
> 2016
> 4.52
> 22.9795
> 3.52
> 13.78%
> 1.65%
> 11.99930
> 627
> 1092
> 2017
> 4.22
> 22.0095
> 2.79
> 9.519
> 0.9190
> 8.72930
> 1749
> 1203
> Chart
> Pnl
> 2018
> 3.4
> 21.699
> 2.37
> 10.29%
> 20%
> 499
> 1714
> 1212
> 2019
> 3.26
> 21.4495
> 2.26
> 10.32%
> 1.23%
> 52930
> 1665
> 1162
> 2020
> 1.99
> 21.1495
> 1.12
> 6.6296
> 2.4596
> 2890
> 1616
> 1125
> 2021
> 2.52
> 20.1895
> 47
> 6.729
> 1.02%
> 58930
> 1703
> 1259
> 7,50OK
> 2022
> 1.37
> 20.139
> 0.67
> 4.839
> 2.29%
> 4.80930
> 652
> 1240
> 5,0OOK
> 2023
> -11.03
> 29.179
> 10.18
> -24.859
> 1.539
> -17.0293o
> 1505
> 1077
> 2,50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.99
> 8.649
> 1.44
> 6.5296
> 8.4096
> 15.089600
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 5;43
> PM
> 0.1456
> -0.0393
> 00
> IS Testing Status
> Period
> 05
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 5;43
> PM
> 0.6239
> -0.0916
> 6 PASS
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 5;43
> Sharpe Of 3.37 is above CUtOff of 1.58。
> PM
> Fitness Of 2.26 is above cutoff of 1
> 0.7043
> -0.3995
> Turnover of 22.089 is above cutoff of 1%
> Turnover of 22.08% is below cutoff of 70%


仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain.comlalphas BOPXEEZ
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 3.06
> 2.19 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> IaXTTaCE
> OFF
> operatorcount
> _
> 1Of1
> 个 b = X
> 17
> "language
> FASTEXPR'
> 18
> IVis0a1i2ation"
> false,
> 19
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE
> imb5_
> SCOIC!
> 24
> description
> Iaea:
> Take
> The
> negative
> Inverse
> O1 The
> inbalance
> SCOIE
> -0
> CIeaTe
> ConTLaLian Signal
> That
> elphasizes
> anC
> fLips
> The
> OIIgInal Ielatzonsh-p. InRatzonale
> for
> 0a-a
> USeC
> The
> inbalance
> SCOIE
> (imb5_
> SCOIE )
> Iikely
> IIea5ULe5
> OIOEI
> fIOW
> OI
> Iiquidity
> aSyIIeTTy;
> Its Inverse highlishts periods
> O1 balance,
> and
> The
> negative sign
> fuITher
> inverts
> The signal. InRationale
> fJI
> OperatoIs  used:
> The
> inVerBe
> (1/x)
> TTansfoIms high
> imbalance
> Into
> Ioy
> Values
> anC
> CHe
> negative sign
> (-〉 Iips
> The
> OUTpU
> PTLOIICIZe
> Conci-inns Where
> The OLiginal
> SCOIe
> Is negative (e.8
> sellIng pressuTe)
> bUT
> OWI
> appears
> positive signals
> 25
> ODeratozCount
> 25
> 27
> UateCzeated "
> 2025
> 09-09T01:43:59
> 04:00
> 28
> "dateSubmitted "
> 2025-09-09102:20:35-04:00
> "datelodified
> 2025-09-13109:42:37
> 04:00
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> alpha C


只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符

2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 08/14/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(2
> rsk72_atopzooO_dsrt
> rank
> mdl26
> FLtV
> rsSII
> 2000_30_
> Power Pool Alpha
> Pyramid theme: CHNIDIIRISK X1.4
> Simulation Settings
> Pyramid theme: CHNIDIIMODEL X1.6
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaNHar
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.59
> 48.989
> 0.96
> 17.739
> 14.389
> 7.249600
> Equity
> CHN
> TOPZOOOU
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,00
> 50.9796
> 2.14
> 25.8395
> 3.459
> 10.14930
> 376
> 311
> Clone Alpha
> 2014
> 3.19
> 50.37%6
> 2.39
> 28.3395
> 4.5996
> 11.259530
> 449
> 375
> 2015
> .99
> 43.99%
> 1.76
> 32.2995
> 14.38%
> 15.5935o
> 726
> 502
> 2016
> 2.15
> 46.26%
> 22.0595
> 5.0596
> 9.5390
> 675
> 556
> Chart
> Pnl
> 2017
> 0.46
> 46.93%
> 0.14
> 43895
> 8.6795
> 879530
> 595
> 501
> 2018
> 1.31
> 48.3796
> 0.64
> 11.6395
> 4.6796
> 83900
> 554
> 455
> 2019
> 2.07
> 50.56%
> 1.22
> 17.6995
> 4.11%
> 9850
> 524
> 420
> 2020
> 0.17
> 50.68%
> 0.03
> -1.9695
> 10.9096
> 0.77930
> 542
> 427
> 1ON
> 2021
> 51.20%
> 0.38
> 11.1295
> 9.73%
> 4.34900
> 543
> 425
> 2022
> 50.5696
> 1.12
> 20.1999
> 5.7390
> 7.979530
> 552
> 447
> 5,00OK
> 2023
> 10.25
> 50.3896
> 10.51
> 52.9395
> 2496
> 21.019500
> 562
> 484
> Risk neutralized
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> 1.17
> 48.989
> 0.39
> 5.4296
> 18.579
> 2.219600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.52
> 42.179
> 0.97
> 17.049
> 14.409
> 8.089600
> IS Testing Status
> Period
> IS
> 05
> [
> Correlation
> 8 PASS
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 6;01
> Turnover of 48.989 is above cutoff of 1%
> PM
> Turnover of 48.98% is below cutoff of 70%
> Weight is well distributed over instruments。
> Returns Of 17.73% is above cutoff of 8%.
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 6;01
> Sub-universe Sharpe of 1.55 is above Cutoff of 1.13.
> PM
> Robust universe Sharpe of 1.30 is above CUtoff of 0.64 (40% of Alphal
> 0.8918
> -0.2468
> Robust universe returns of 9.139 is above cutoff of 7.09% (40% of Alphal.
> These pyramid themes match with the following multipliers: CHN/DI/RISK-
> 1.4; CHNIDIIMODEL
> 1.6.The final
> pyramid theme multiplier is 1.4. Effective pyramid count for Genius is 2。
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 6;01
> PM
> 5WARNING
> 0.8234
> -0.6297
> Sharpe of 1.59is below CUtOff of 2.07.
> chng


我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi. worldquantbrain comlalphas/SdnGl4z
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 17.925
> 2.3 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三 Q6 &
> 15
> IaXTTaCE
> OFF
> operatorcount
> 酏*
> 1Of1
> 个 b = X
> 17
> "language
> IFASTEXPR"
> 18
> IVis0a1i2ation"
> false
> 19
> startDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> TegUIaT"
> 23
> COCE
> raIk (2
> ISk72_a20p2000_
> OSIT)
> raIk (3
> 10125_
> Chng_IICV_T_
> 工5511
> 2000_
> 30)
> 24
> "description"
> Iaea:
> Dual-Iank PIOCUCT
> Signal
> Combining
> SHOIT
> MnTerest
> anC
> RSS
> Iquidity
> Changes
> 1nRaTi3na12
> for 0a-a
> USeC:
> 1 -
> ISK72
> aTOp2OOO_OSIT:
> RUSSeII
> 2000
> SHOIT
> MnTerest
> percentile
> {几-
> Ic126_chng_
> IITV_T_ISSII
> 2000_
> 30:
> 30 -
> IelatIve Izquzdity
> Change
> SCOIC
> InlnRaionale
> fJI
> OpeIaTOIS
> USee
> 1-
> EXpOnenTiaI
> TransforIs
> CIeaTe
> COIVCX
> Ianking:
> 3a5e-2:
> SHOIT
> Interest
> aMplification
> 3a5e-3
> Htouidity
> change sensitivity
> 1 -
> MulTiplicaive
> Combinazion:
> High when
> boTh
> signals
> agTeE
> Near- ZeIn
> when
> eiTher
> neUTIaI
> {- Negative
> SIgn
> CargeTs:
> High
> SHOIT
> MnTerest
> CeTeriorating
> liquidity
> 1"5hoI
> 50UeeZe
> TIap
> ioentification
> OpezatozCount
> 25
> 27
> "datecreated "
> 2025
> 08-14T05:27:35-04:00
> 75
> rateSwhmitterl"
> 2025-08-15T01:04:25-04:Q0
> alpha C
> day


重复算 operatorCount 操作符了 .

没有  **字段使用数量信息** ，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .

[图片 (图片已丢失)]

**重点** ：巧妙的节省重复操作符 ！！！

从以上几个alpha操作符测试，让我们知道了

i ) +、-、*、/ 和 ^ 都是算入操作符计数的；

ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；

iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha

3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/12/2025 EDT
> anonymoUs
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> brk
> VeC
> Sum(brkl_start_stock_price);
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIBROKER X1.5
> alpha
> ts covariance
> bpk,
> 股票起始价格汇总
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> bpk
> 11同一序列的自相关讦算
> 1.05
> 13.439
> 0.86
> 9.059
> 10.689
> 13.479600
> 24
> 24周期(约1个月)滚动窗0
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0,80
> 14.3096
> 5.2995
> 5.0195
> 40930
> 1157
> 1571
> Instrument Tpe
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> 2014
> .85
> 12.39%
> .90
> 13.2495
> 3.239
> 21.369600
> 1424
> 1722
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> On
> OfT
> 2015
> +28
> 12.59%6
> 1.28
> 12.6295
> 7.6596
> 20.05930
> 1537
> 1751
> 2016
> 1.36
> 13.59%
> 1.57
> 18.2595
> 9.249
> 26.67930
> 1477
> 1690
> 2017
> 0.63
> 11.4796
> 0.32
> -3.20%
> 6.959
> -5.5893o
> 1746
> 1497
> Clone Alpha
> 2018
> 0.72
> 12.4696
> 0.52
> 5.469
> 8.5096
> 10.379530
> 1980
> 1765
> 2019
> 13.25%
> 1.71
> 13.5695
> 5.18%
> 20.47930
> 1757
> 1611
> 2020
> 0.47
> 15.54%
> 0.25
> 2.4495
> 7.5096
> 68930
> 1818
> 1731
> Chart
> Pnl
> 2021
> 14.52%
> 1.17
> 10.8195
> 4.0096
> 14.79930
> 2194
> 2300
> 2022
> 1.17
> 13.7096
> 0.94
> 8.759
> 6.35%
> 12.779530
> 1980
> 2197
> 2023
> 0.48
> 20.3796
> 0.17
> 26Ob
> 8296
> 2.5593o
> 1640
> 1992
> 7,50OK
> SOOOK
> Correlation
> 2,50OK
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,8;43
> Du
> 0.2112
> -0.0733
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 8;43
> PM
> 0.4247
> -0.0733
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 8;44
> PM
> 0.3960
> -0.3483


我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain comlalphaslobd5qOE
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 2.545
> 2.41 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> nanHandling"
> OFF
> operatorcount
> 劭
> ? Of1
> 个 b = X
> 16
> IaXTTaCE
> ON
> 17
> "language
> FASTEXPR
> 18
> IVis0ali2ation
> false,
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE"
> Ibrk
> VeC
> SUII ( bIkz_
> STAIT_
> sTOCk_priCe ) ; Irlnalpha
> C5_
> Covariance (IIin
> DIK,
> L 股票起始价格汇总 Irln
> bIk ,
> LL 同-序列的
> 自相关计算 {210
> 24
> J24周期〈约1个月)滚动窗OIrln) ; '
> 24
> "JesCZIptiOn"
> Iaea:
> COIpUTE
> the negatlve IoIIIng
> COVariance
> Of aggTegated
> starting stock prices with itself
> Iea5UIE
> 5e11-similarity
> anO
> invert
> The
> Ielationship
> InRationale
> fJI
> USeO:
> The aggIe
> starting
> STOCK priCe
> (VeC_
> SUII
> (brki_
> STaIT
> sTOCk_price)
> IeTIeCTS
> baseline
> Valuation
> levels
> 35
> boTh
> IpUTS
> COVariance
> CapTUIeS
> i5
> OIII
> Volatility
> and pattern
> consistency
> InRaTionale
> for OperatoIs
> USeC:
> The
> 24-period
> COVariance
> (TS
> COVariance)
> SeIies Iizh
> iself simplifies
> VaTZance
> measUring
> HOWI Uispersed
> The
> Values
> aIe
> aIOUnC
> Their
> IIean
> DVEI
> ShOIt
> term Window.
> The
> negative
> sign (-)
> TIVeITS
> 375,
> 50
> higher
> Variance (inszability)
> IeSUITs
> 11
> IOIeI
> 518na1 ,
> penalizing
> VoIatility
> 25
> OpezatozCount
> 25
> alpha C
> Jaza
> gazed
> Using


事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/01/2025 EDT
> jiao?
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> Vector
> neut
> VeC
> SUN(rSKGG
> offer),
> VeC
> SUm(rsk6o
> Offer)))
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> Simulation Settings
> 1.33
> 10.339
> 1.05
> 7.819
> 16.029
> 15.139600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Equity
> USA
> ILLIQUID_MINVOLIM
> Fast Expression
> 0.08
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.009
> 0.00
> 0.0096
> 00%
> 0093o
> 2014
> 1.30
> 7.1995
> 0.77
> 4.4296
> 1.6296
> 12.36950
> 936
> 1552
> 2015
> -0.29
> 7.5095
> -0.21
> 2.28%
> 8390
> 079330
> 716
> 1825
> Clone Alpha
> 2016
> 1.03
> 7.3295
> 5.4796
> 0996
> 14.93930
> 539
> 1878
> 2017
> 0.77
> 8.3595
> 3.36%
> 4.839
> 0593o
> 555
> 832
> Chart
> Pnl
> 2018
> 1.07
> 13.9099
> 5.29%
> 2.5795
> 7.62930
> 577
> 888
> 2019
> 0.95
> 13.0395
> 5.5596
> 4.98%
> 8.5390
> 512
> 1905
> 2020
> 1.25
> 11.1495
> 1.16
> 10.6596
> 5.11%
> 19.139500
> 464
> 1922
> 2021
> 0.91
> 10.1895
> 0.b
> 79%
> 12.53%
> 13.34930
> 2248
> 2022
> 5.02
> 14.389
> 7.52
> 32.31%
> 2.2796
> 44.9493o
> 1070
> 1821
> 40OOK
> 2023
> -1.55
> 10.6890
> -1.48
> -11.40%
> 2.35%
> -21.32930
> 752
> 1893
> 20OOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;55
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Du
> 0.3766
> -0.1774
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;55
> PM
> 0.3713
> -0.1928
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;55
> 00
> IS Testing Status
> Period
> OS
> PM
> 0.6809
> -0.5425


这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =

1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .

[图片 (图片已丢失)]

2. 点塔！

```
点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题
```

当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节： [交一个怎样的alpha能提升你的六维数据之定性定量分析 .](../顾问 WX64154 (Rank 32)/[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析.md)

我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！

关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：

i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)

[图片 (图片已丢失)]

比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 . 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(anl3g
> rOXLCXSpeq
> anl3g_xIcxspemtp)
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> RetUrns
> DrawOOwn
> Margin
> Simulation Settings
> 0.37
> 3.549
> 0.14
> 1.869
> 13.18%
> 10.539600
> Instrument Tpe
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.71
> 3.769
> 1.30
> -7.22%
> 11.439
> -38.389530
> 775
> 1332
> 2014
> 1.18
> 3.1795
> 0.75
> 5.0096
> 3.51%
> 31.53950
> 1058
> 1558
> 2015
> 0.37
> 3.4295
> 0.15
> 2.1796
> 7.36%
> -12.67900
> 1156
> 1557
> Clone Alpha
> 2016
> 1.83
> 3.8795
> 1.84
> 12.6796
> 3.21%
> 65.529530
> 1093
> 1627
> 2017
> 0.58
> 3.3295
> 0.32
> 2.6996
> 5.33%
> 16.2390
> 1172
> 1779
> Chart
> Pnl
> 2018
> 1.81
> 3.43995
> 1.42
> 7.42%
> 3.40%
> 43.25930
> 1135
> 1792
> 2019
> -U.61
> 3.3995
> 0.33
> 3.029
> 4.92%
> -17.9390
> 004
> 1825
> 2020
> 3.5395
> 0.10
> 5696
> 5.6796
> 8.84930
> 998
> 1752
> 2021
> 1.38
> 3.8595
> 5.5896
> 4.20%
> 28.97930
> 1855
> OOOK
> Mlwto
> 2022
> 0.32
> 3,6695
> 0.13
> 9996
> 859
> 10.8593o
> 1072
> 830
> 2023
> -3.70
> 3,0095
> 2.01
> -14.5890
> 0090
> 97.97930
> 970
> 1792
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Margin
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 0.27
> 2.2296
> 0.09
> 1.4096
> 14.639
> 12.579600
> Pnl
> Investability Constrained Pnl
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;36
> PM
> 0.2624
> -0.0448
> IS Testing Status
> Period
> OS
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;37
> PM
> 0.8554
> -0.6340
> 5PASS


通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 07/30/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank
> star
> Val
> industry_rank
> anl39
> rOXLCXSpeq
> anl39_xlcxspemtp
> Power Pool Alpha
> Pyramid theme: EURIDIIMODEL X1.4
> Simulation Settings
> Pyramid theme: EURIDIIANALYST X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.45
> 7.5596
> 1.91
> 7.629
> 4.2396
> 20.189600
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> On
> On
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.70
> 6.7096
> 1.04
> 46895
> 1.289
> 13.98900
> 778
> 1329
> Clone Alpha
> 2014
> 3.25
> 7.59%6
> 2.69
> 8.5495
> 1.149
> 22.5035o
> 1070
> 1525
> 2015
> 1.27
> 7.84%
> 0.72
> 2.0595
> 2.839
> 10.359500
> 1113
> 1611
> 2016
> 4,09
> 8.03%
> 2.34
> 12.0895
> .20%
> 35.07930
> 1025
> 695
> Chart
> Pnl
> 2017
> 2.61
> 7.3396
> 1.75
> 5.6295
> #1090
> 15.3390
> 1120
> 831
> 2018
> 3,05
> 7.7096
> 2.30
> 7.10%
> 2.0590
> 18.43900
> 1166
> 1750
> 2019
> 1.27
> 7.56%
> 62
> 3.0195
> 1.70%
> 7.95930
> 1183
> 1625
> 2020
> 2.34
> 8.01%
> 1.94
> 8.6095
> 1.72%
> 21.469530
> 1121
> 1621
> 5OOOK
> 2021
> 2.71
> 86%
> 2.35
> 9.4095
> 3.52%
> 27.40950
> 1122
> 1820
> 2022
> 2.45
> 7.81%6
> 2.27
> 10.75%
> 4.2390
> 27.51930
> 1163
> 1739
> 2,50OK
> 2023
> 3,80
> 7.5596
> 3.63
> 11.8095
> 0.489
> 31.269500
> 1093
> 1672
> Investability constrained
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.88
> 3.599
> 1.30
> 5.9796
> 3.9796
> 33.269600
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025,7.05
> PM
> 00
> IS Testing Status
> Period
> 05
> 0.5189
> -0.0937
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> 8 PASS
> PM
> 0.5189
> -0.1529
> Sharpe of 2.45 is above CUtOff of 1.58.
> Fitness Of 1.91 is above cutoffof1.
> Turnover of 7.5596 is above CUtoff of
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> PM
> Turnover of 7.55% is below cutoff of 70%.
> Weight is well distributed over instruments。
> 0.8288
> -0.4965
> Sub-universe Sharpe of 1.27 is above cutoff of 1.27.
> IS Iadder Sharpe Of 2.49 is above cutoff of 2.02 for Iadderyear 2: 1/20/2023.1/21/2021


ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> OS
> ts_target_
> tvr_decay (imbs_
> SCOre
> Iambda_min-o,
> Iambda
> maX=l, target
> tVr=0.1
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> Simulation Settings
> 2.86
> 7.7796
> 1.98
> 5.979
> 2.319
> 15.379600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.32
> 7.96%
> 2.54
> 7.3295
> 009
> 18.40950
> 1363
> 1355
> 2014
> 5.73
> 7.0796
> 5.12
> 9.999
> 0.739
> 28.259530
> 1569
> 1577
> 2015
> 4.83
> 7.5196
> 264
> 11.5495
> 1.289
> 30.7390
> 1645
> 653
> Clone Alpha 
> 2016
> 2.76
> 7.3796
> .82
> 5.42%
> .6890
> 14.71930
> 1574
> 593
> 2017
> 2.23
> 7.51%
> 3.00
> 5.2995
> 639
> 16.52930
> 1610
> 533
> Chart
> Pnl
> 2018
> 3.49
> 7.81%
> 2.54
> 6495
> .239
> 6.93930
> 1875
> 1871
> 2019
> 2.96
> 7.5596
> 2.04
> 5.9195
> 1.129
> 15.45930
> 645
> 1723
> 2020
> 8.30%6
> 22795
> 1.729
> 5.48930
> 1736
> 1813
> 2021
> .05
> 299
> 2.43%
> 2.31%
> 5.86930
> 2203
> 2291
> 40OOK
> 2022
> 7.97%6
> 0.22
> 1.5195
> .839
> 3.79950
> 2057
> 2121
> 2023
> 11.09%
> 5.57
> 8.2395
> 08%
> 14.85930
> 1783
> 1829
> ZOOOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;33
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> PM
> 0.3352
> -0.0929
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> Du
> 0.5597
> -0.1764
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> IS Testing Status
> Period
> 0S
> Du
> 0.9227
> -0.5410
> Year


比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .


> [!NOTE] [图片 OCR 识别内容]
> 说到这里,
> 我想说一下关于提交 alpha 关于 Prod Correlation ,
> Power Pool
> Correlation 和 Self Correlation,
> 也许在绿灯亮起提交 alpha 显示出的错误或许不
> 那么明确. (个人看法,如有问题还望大佬们不忘吝啬,
> 可评论区说明我好做出调
> 整)但大致是这样的 .
> 举个例子:有一个国王喜欢吃各种各样式的苹果
> 大家都会送苹果给国王
> 吃,
> 当然会获得相应的报酬,吃之前需要将苹果放进池子进行清洗,
> 有两个大小
> 的池子。如果你送来的苹果好,自然是放在大池子里。和大池子里的苹果比较 ,
> 如果大池子没有类似的苹果,
> 或者如果有类似的苹果,
> 但是你的苹果比这个类似
> 的苹果有更少的瑕疵,那你的苹果将会被收取从而获得报酬;  如果你的苹果不满^
> 足大池子,
> 那就继续按照以上这种方式放小池子,
> 当然这种小池子只是大家人手
> 一个,
> 大池子也是谁想用可以随时搬自己家测试,
> 小池子的作用是什么,如果大
> 池子的苹果被国王吃完了,那就会考虑小池子了,当然人家毕竟是国王,没有那
> 么容易吃完大池子的稀奇苹果.



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 09/11/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> ts_target_
> tvr_decay (imbs_
> SCOre
> mCr63_membership,  Iambda
> min=0
> Iambda
> Iax=l
> targe
> Power Pool Alpha
> Pyramid theme: ASIIDIIIMBALANCE X1.1
> Simulation Settings
> Pyramid theme: ASIIDIIMACRO X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 7.739
> 1.19
> 5.249
> 5.899
> 13.56900
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> 0n
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.03
> 8.02%
> 1.34
> 5.4795
> 2.0596
> 13.63330
> 1377
> 1351
> Clone Alpha 
> 2014
> 2.21
> 7.0596
> 407
> 11.659
> .76%
> 33.089500
> 1573
> 1573
> 2015
> 3.41
> 7.4796
> 293
> 9.20%
> 1.129
> 24.61930
> 670
> 628
> 2016
> +94
> 7.45%6
> 0.47
> 3.16%
> 5.8990
> 48930
> 590
> 1577
> Chart
> Pnl
> 2017
> 2.28
> 7.50%
> 2.8895
> 1.6596
> 12.84930
> 620
> 1623
> 2018
> 2.55
> 7.74%
> .84
> 5.5395
> 1.2996
> 16.879500
> 899
> 1827
> 2019
> .83
> 7.5496
> 1.14
> 4.8795
> .9890
> 12.91930
> 1705
> 653
> 2020
> 0.02
> 8.3296
> 0.00
> 0.059
> 2.259
> 0.1593o
> 800
> 1729
> 2021
> 8.18%6
> 1.21
> 5.159
> .6390
> 12.5893o
> 2305
> 2190
> 2022
> 7.82%
> 0.07
> 0.8795
> 2.5696
> 2.239500
> 2113
> 2055
> ZOOOK
> 2023
> 3.80
> 10.50%
> 3.02
> 7.9295
> 0.1996
> 15.08930
> 864
> 1757
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;43
> PM
> 0.3474
> -0.0437
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.3645
> -0.0892
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.6217
> -0.4420
> PASS
> Vear


事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .

[图片 (图片已丢失)]

3. 好而优的 alpha

何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .

一点：好，我理解在:

1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；

2) fitness ≥ 1  全方面稳定还是非常不错；

3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；

4) returns ≥ 10%  收益还是要好点能赚钱吧；

5) drawdown 回撤越小越好吧，大了心理抗压不行；

6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；

7) 十年数据中做多做空不能太少吧，权重太高危险危险！

8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .

满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/08/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> 1
> OS Summary
> Period
> I5
> 05
> peVerse(r
> ib5
> SCOre
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDOIIMBALANCE
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> Simulation Settings
> 0172112023 CT
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Close
> Close Ratio
> Self-Correlation
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone Alpha
> 2013
> 3.9
> 23.8899
> 4.13
> 26.189
> 2.5995
> 21.929600
> 986
> 405
> 2014
> 3.52
> 22.6895
> 3.36
> 20.65%
> 2.9096
> 18.22930
> 1070
> 431
> 2015
> 3.32
> 22.8295
> 3.46
> 24.43%
> 3.03%
> 21.41950
> 1130
> 459
> Chart
> Pnl
> 2016
> 2.53
> 21.1195
> 2.65
> 21.4796
> 3.4796
> 20.349530
> 1138
> 455
> 2017
> 2.77
> 20.7795
> 2.47
> 16.5496
> 3.40%
> 15.92930
> 1125
> 470
> 2018
> 1.88
> 19.5696
> 1.67
> 15.3796
> 7.27%6
> 15.71930
> 1010
> 418
> 2019
> 2.77
> 19.1395
> 3.03
> 22.829
> 3.18%
> 23.8890
> 998
> 423
> 1ON
> 2020
> 0.71
> 19.4395
> 0.39
> 5.9596
> 5.659
> 2930
> 908
> 392
> 2021
> 1.73
> 19.20%
> 10.789
> 5.089
> 11.22930
> 972
> 416
> 5OOOK
> 2022
> 18.4390
> 1.42
> 14.789
> 4.5795
> 16.0493o
> 050
> 439
> 2023
> 10.22
> 31.6599
> -14.39
> 62.7790
> 3.5796
> 39.67930
> 945
> 393
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pre
> Sharpe
> Pre


二点：优，我理解在:

1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；

2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；

3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；

使用


> [!NOTE] [图片 OCR 识别内容]
> 1
> 1.
> 事件距离基础信号:  距离越大。事件影响越小
> eVent
> signal
> VeC
> SUI
> nWs7g_event_detection_distance_358-
> 1
> 距离平方增骚:  放大极端距离信号的非线性影响
> brk
> VeC
> sum(brkl_start_stock_price);
> distance_squared
> event_signal
> 2;
> alpha
> ts covariance(
> brk,
> 股票起始价格汇总
> 1
> 词频倒数因子:  词数越少。信息浓度越高(1/词数)
> brk,
> 11  同一序列的自相关计算
> Word
> density
> 二 1
> VeC
> SUII
> nWS7g_word_count_391 )
> 24
> 24周期(约1个月)滚动窗口
> 10
> 1
> 复合事件驱动因子:  距离信号
> 非线性增骚
> 信息浓度
> 11
> alpha
> (event_signal
> distance_squared
> Word_density)



> [!NOTE] [图片 OCR 识别内容]
> 11 Core Logic:
> Reverse standardized composite factor
> reverse
> operation when large trader behavior diverges
> 1
> Synthetic
> Base
> Factor: Market
> pattern
> trader Value differential
> base factor
> mdl175 OGam
> power(Vec
> sum(pvz7_value_diff_large_trader), 2);
> /12. standardization: Convert to
> Z-score to eliminate scale effects
> Zscore_factor
> Zscore(base_factor) =
> 1
> Signal Reversal: Negative sign indicates
> Contrarian
> selection, seeking
> undervalued
> opportunities
> alpha
> ZSCOre
> factor;
> large



> [!NOTE] [图片 OCR 识别内容]
> Description
> 507
> 100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template_
> Idea: Identify the time index ofthe maximum imbalance score over a 2O-day Window, then invert the result:
> Rationale for data used: The imbalance score (imb5_score) likely measures order flow or liquidity asymmetry; its maximum pinpoints the
> most extreme positive imbalance event。
> Rationale for operators Used: The 20-dayarg max (ts_arg_max)returns the lookback period (0-19) where the series peaked_and the


不建议使用


> [!NOTE] [图片 OCR 识别内容]
> 1 |
> ts_covariance(vec
> SUm(brkl_start_stock_price) ,
> VeC
> sum(brkI_start_stock_price), 24)



> [!NOTE] [图片 OCR 识别内容]
> brk
> VeC
> sum(brkl_start_stock_price)
> alpha
> ts covariance
> brk,
> 股票起始价格汇总
> bk,
> 11同一序列的自相关计算
> 24
> 1124周期(约1个月)滚动窗口
> );
> alpha


[图片 (图片已丢失)]

**三、alpha模板 ！**

看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .


> [!NOTE] [图片 OCR 识别内容]
> N-1
> Ha
> 1,3N,8.七
> lim
> fa()-Cfa(a)
> 二
> Iim
> fa(a)
> n-〉+O
> n〉+O
> 2二1
> 2二1
> C=N
> 10-P


换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！

field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .

其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> 2,000
> UUJ
> OIlU
> 〈ee
> 3" A0。
> 02
> Displayed Period
> 02/14/2025
> 09/12/2025
> 149346
>  Mar
>  Mar
> Mar
> Mar
> Mar
> 30。
> 31。
> 24。


从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .

[图片 (图片已丢失)]

使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .

造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .

[图片 (图片已丢失)]

下节预告:  [Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析](../顾问 WX64154 (Rank 32)/[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析.md)

2025年9月14日

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的分享，我认真地看完了，文章的风格独特且美观，我也收获了很多，对于alpha的研究豁然开朗，有了不一样的见解，并且，此前一直没有想过用a=表达式1；表达式2（a)；这样也可以降操作符，突然感觉自己损失了很多；再者，对于在表达式中再加一个字段有时可以改良alpha的性能，以及我们可以自创数据字段，这些为我后面的研究带来了启迪性的作用


---

### 技术对话片段 114 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 冲刺genius !
> 细节决定成败,你的六维还能提升 ! &模板
> 
> 
> 首先感谢游戏王 (2559763) ,
> 橘子姐
> (6383096) ,
> base payment 拉满的
> 大佬 (AH18340) 以及 上海 (MF59400)等等的帮助.也许你们自己都不知道 ,
> 但是潜移默化
> 的影响了我,
> 下面阐述的其中有-些内容是我在游戏王那里学习到的.


## **一、Genius定级与何相干？**

总体来说，一共与两方面有关，一是  **硬性指标** ，二是  **软指标** 。


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-03,July 1st, 2025
> September 3Oth; 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 266
> Reached Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 72
> Reached Grandmaster
> 10
> 30
> Combined Alpha Performance
> 2.39
> Reached Grandmaster
> 0.5


其中  **硬性指标** 包括由

1. 本季度 Signals (阿尔法)；

2. 本季度 Pyramids (金字塔)；

3. Combined Alpha Performance (提交的所有alpha表现)；

4. Combined Selected Alpha Performance (被选中的alpha费后表现)

5. Combined Power Pool Alpha Performance (power pool alpha表现)

五部分组成；

```
点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。
```

我们以Expert (专家)为例，硬性指标必须同时满足

1. 本季度alpha数量 Signals ≥ 20；

2. 本季度金字塔数量 Pyramids ≥ 10，

3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5

       这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).

[图片 (图片已丢失)]

**软指标** 又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。

**
> [!NOTE] [图片 OCR 识别内容]
> What happens 迂 more consultants qualify for a level than there are available
> If more consultants meet the base criteria for
> level than there are available Spots
> a tiebreaker criterion is used _
> This is based on a sum Of ranks across the following metrics
> 1.
> distinct Operators
> Alpha (Lower is better )
> 2.
> distinct Fields
> Alpha (Lower is better)
> 3. Total distinct Operators (Higher is better)
> 4
> Total distinct Fields (Higher is better)
> 5. Maximum Simulation Streak
> Best streak of
> consultant that ends i that quarter
> OI
> continues into the next quarter
> Streak does not reset to 0 every quarter。
> 6. Community leader
> Forum
> Number Of Likes on Posts Or comments that are
> published as Of the end Of quarter
> Ninimm length of post Or comment must be 100 characters。
> Referral
> Total number Of successful referrals i the quarter
> A referral is considered
> Slccessfil
> Khen the
> referring consultant h as become eligible to accrte the referral fee for someone
> have referred to BRAIN
> 讧 accordance with the guidelines Of the referral fee program
> Spots?
> Avg
> AVg
> they
**

**
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st, 2025
> September 3Oth, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.41
> 68
> 1.54
> Fields used
> Community activity
> Max simulation streak
> 260
> 33.2
> 88
**

其中  **软指标** (六维数据)包括由本季度

1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；

2. Operators used (操作符的去重使用个数)；

3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；

4. Fields used (字段使用(去重)数量)

5. Community activity (rank[社区活跃程度])

6. Max simulation streak (最大连续回测天数)

六部分组成；

```
·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。
```

[图片 (图片已丢失)]

## **二、冲刺 Genius !**

通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。

1. 关于六维数据  **细节**

这部分我们娓娓道来，关于六维数据我们能做的是什么?

i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；

ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；

iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；

iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；

v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .

首先，讲讲我的一些  **蠢行为! ,** 等等上面还有一点重要的忘记说了， **要保持区域、Delay以及数据集多样性！**

**
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st, 2025
> September 3Oth, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Fundamental
> Insiders
> Macro
> Mogel
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Social Media
> Earnin3s
**

使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多  **8~10**  个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Delayo
> NAN
> Delayl
> NAN
> Fundamental data
> Fundamental data
> Analyst data
> Analyst data
> Broker
> Broker
> News data
> News data
> Social media data
> Social media data
> Sentiment data
> Sentiment data
> Price VOluMe data
> Price Volume data
> Option data
> Option data
> Eamings
> Earnings
> Insiders
> Insiders
> Instiutional Ownership Data
> Instiutional Ownership Data
> Short interest data
> Short interest data
> Macro data
> Macro data
> Other
> Other
> Risk data
> Risk data
> Model data
> Model data
> USA
> ASI
> CHN
> EUR
> GL
> HKG
> KOR
> TVN
> AMR
> JPN
> USA
> ASI
> CHN
> EUR
> GLB
> HKG
> KOR
> TVN
> AMR
> JPN
> Click to drill down
> EUR
> ASI
> GLB
> USA
> CHN


保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.

[图片 (图片已丢失)]

接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/26/2025 EDT
> 顾问 ML47973 (Rank 100)
> Add Alphato
> LiSt
> Code
> IS Summary
> Period
> IS
> 05
> power(2,
> md177_astcomp
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> Simulation Settings
> 1.65
> 6.11%
> 2.64
> 31.939
> 16.609
> 104.449600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Subindustry
> On
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 1.69
> 5.46%
> 1.56
> 10.65%
> 4.76%
> 39.05920
> 1999
> 357
> 2019
> 4.949
> 1.71
> 18.5896
> 8.66%
> 75.279620
> 1988
> 375
> 2020
> -0.,04
> 029
> 0.01
> 0.5596
> 15.18%
> 82920
> 2010
> 375
> Clone Alpha 
> 2021
> 2.46
> 699
> 4.84
> 48.489
> 15.30%
> 122.899620
> 2142
> 380
> 2022
> 2.44
> 7.42%
> 6.08
> 77.70%
> 13.23%
> 209.41920
> 2136
> 390
> Chart
> Pnl
> 2023
> 3.61
> 6.13%
> 7.40
> 52.519
> 1.71%
> 171.19920
> 2114
> 397
> 匣
> Correlation
> 1ON
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,4;51
> PM
> 0.6840
> -0.0542
> OOOK
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,4;51
> Du
> 0.4204
> -0.1633
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 4;51
> 0
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul "22
> Jan '23
> Du
> 0.6874
> -0.6201
> Vear



> [!NOTE] [图片 OCR 识别内容]
> 这个 Q 当时让我 base payment 日 赚54.816 ,当时 iqc 结束 ,第一次0f更新0.86


直到我使用华子哥的插件才发现


> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 美东时间:2025/9/1200:38:06 北京时间: 2025/9/1212:38:06
> 在你可用的运算符中。共有67种运算符被使用。12种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统一为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x, Y, filter
> false); X + y
> 52
> COMBO,REGULARSELECTION
> base
> Arithmetic
> multiply(x ,y
> filterzfalse); X * y
> 76
> COMBO,REGULARSELECTION
> base
> Arithmetic
> sign(x)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> subtract(x, Y, filter-false) X -Y
> 157
> COMBO,REGULARSELECTION
> base
> Arithmetic
> pasteurize(x)
> COMBO,REGULAR
> genius
> Arithmetic
> log(x)
> COMBOREGULARSELECTION
> base
> Arithmetic
> maXfx;y
> COMBO,REGULARSELECTION
> base
> Arithmetic
> absfx)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> divide(x; y), XIy
> 158
> COMBO,REGULARSELECTION
> base


我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！

下面的操作有几率  **降低** 你的  ***Operators per Alpha*** ，和想要查看自己的alpha数据也可以认真看一下

在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)


> [!NOTE] [图片 OCR 识别内容]
> #  登录 (login)url
> CUrl
> --location
> --request
> POST
> https : / /api. worldquantbrain . com
> authentication
> header
> Authorization:
> Basic MZAZODUBMTAZOEBXcSSjbzeGQUYrQUYrQUYgMBFG
> ~-header
> Cookie:
> t=eyJeeXAiOiJKVIQiLCJhbGciOiJIUZIINiJg .eyJqdGkioi -



> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> login
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> POST
> https:Hapi.orldquantbrain comlauthentication
> Send
> Environments
> POST Simulation
> Params
> Authorization
> Headers (10)
> Body
> Scripts
> Settings
> Cookies
> PATCH alpha-adjust
> FIOws
> Auth Type
> GET data-fields
> Username
> 30-510
> COm
> Basic Auth
> GET alpha
> History
> GET Check
> Password
> The authorization header will be
> POST submit
> 0+
> automatically qenerated when yoU send the
> GET Self-COrr
> Body
> Cookies
> Headers (20)
> Test Results
> 201 Created
> 1.975
> 1.14 KB
> Save Response
> GET data-sets
> JSON
> Preview
> Visualize
> 三
> Q  @
> GET
> pyramid
> USET"
> id
> 顾问 ML47973 (Rank 100)
> Loken"
> EXDiTy
> 14400
> DeTmissions
> BEFORE
> ANID_
> AFTER
> PERFORMANCE_
> 10
> BRAIN_LA3S"
> 11
> BRAIN_LABS_JUPYTER
> L43
> 12
> CONSULTANTI
> 13
> "MULTI_SIMULATION "
> 14
> PROD_ALPHAS
> 15
> REFERRAL
> 16
> SUPER_ALPHA "
> 17
> IVISUALIZATION"
> 18
> WORKDAY"
> 19
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> 9@.


下面的是查询alpha信息的url


> [!NOTE] [图片 OCR 识别内容]
> #
> check_alpha_info 其中{alpha_id} 使用alpha_id替代即可
> Curl
> -location
> https : / /api .worldquantbrain . com/alphas / {alpha_id}
> -header
> Cookie:
> tseyJeexAioiJKVIQiLCJhbGciOiJIUZIINiJ9 .eyJqdGkioi


接下来我们就来看看几个alpha，查看它们的数据情况

1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/09/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> ib5
> SCOFe
> Single Data Set Alpha
> 俳
> Power Pool Alpha
> Pyramid theme: EURIDIIIMBALANCE X2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> Simulation Settings
> 3.37
> 22.089
> 2.26
> 9.9396
> 2.4596
> 9.009o0
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.02
> Statistical
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.19
> 23.9499
> 200
> 14.1990
> 1.08%
> 11.8590
> 1324
> 781
> 2014
> 4.55
> 23.2595
> 3.25
> 11.85%
> 0.78%
> 10.20950
> 1612
> 1005
> 2015
> 4.20
> 23.68%
> 3.26
> 13.02%
> 1.31%
> 11.00930
> 1101
> Clone Alpha
> 2016
> 4.52
> 22.9795
> 3.52
> 13.78%
> 1.65%
> 11.99930
> 627
> 1092
> 2017
> 4.22
> 22.0095
> 2.79
> 9.519
> 0.9190
> 8.72930
> 1749
> 1203
> Chart
> Pnl
> 2018
> 3.4
> 21.699
> 2.37
> 10.29%
> 20%
> 499
> 1714
> 1212
> 2019
> 3.26
> 21.4495
> 2.26
> 10.32%
> 1.23%
> 52930
> 1665
> 1162
> 2020
> 1.99
> 21.1495
> 1.12
> 6.6296
> 2.4596
> 2890
> 1616
> 1125
> 2021
> 2.52
> 20.1895
> 47
> 6.729
> 1.02%
> 58930
> 1703
> 1259
> 7,50OK
> 2022
> 1.37
> 20.139
> 0.67
> 4.839
> 2.29%
> 4.80930
> 652
> 1240
> 5,0OOK
> 2023
> -11.03
> 29.179
> 10.18
> -24.859
> 1.539
> -17.0293o
> 1505
> 1077
> 2,50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.99
> 8.649
> 1.44
> 6.5296
> 8.4096
> 15.089600
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 5;43
> PM
> 0.1456
> -0.0393
> 00
> IS Testing Status
> Period
> 05
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 5;43
> PM
> 0.6239
> -0.0916
> 6 PASS
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 5;43
> Sharpe Of 3.37 is above CUtOff of 1.58。
> PM
> Fitness Of 2.26 is above cutoff of 1
> 0.7043
> -0.3995
> Turnover of 22.089 is above cutoff of 1%
> Turnover of 22.08% is below cutoff of 70%


仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain.comlalphas BOPXEEZ
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 3.06
> 2.19 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> IaXTTaCE
> OFF
> operatorcount
> _
> 1Of1
> 个 b = X
> 17
> "language
> FASTEXPR'
> 18
> IVis0a1i2ation"
> false,
> 19
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE
> imb5_
> SCOIC!
> 24
> description
> Iaea:
> Take
> The
> negative
> Inverse
> O1 The
> inbalance
> SCOIE
> -0
> CIeaTe
> ConTLaLian Signal
> That
> elphasizes
> anC
> fLips
> The
> OIIgInal Ielatzonsh-p. InRatzonale
> for
> 0a-a
> USeC
> The
> inbalance
> SCOIE
> (imb5_
> SCOIE )
> Iikely
> IIea5ULe5
> OIOEI
> fIOW
> OI
> Iiquidity
> aSyIIeTTy;
> Its Inverse highlishts periods
> O1 balance,
> and
> The
> negative sign
> fuITher
> inverts
> The signal. InRationale
> fJI
> OperatoIs  used:
> The
> inVerBe
> (1/x)
> TTansfoIms high
> imbalance
> Into
> Ioy
> Values
> anC
> CHe
> negative sign
> (-〉 Iips
> The
> OUTpU
> PTLOIICIZe
> Conci-inns Where
> The OLiginal
> SCOIe
> Is negative (e.8
> sellIng pressuTe)
> bUT
> OWI
> appears
> positive signals
> 25
> ODeratozCount
> 25
> 27
> UateCzeated "
> 2025
> 09-09T01:43:59
> 04:00
> 28
> "dateSubmitted "
> 2025-09-09102:20:35-04:00
> "datelodified
> 2025-09-13109:42:37
> 04:00
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> alpha C


只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符

2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 08/14/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(2
> rsk72_atopzooO_dsrt
> rank
> mdl26
> FLtV
> rsSII
> 2000_30_
> Power Pool Alpha
> Pyramid theme: CHNIDIIRISK X1.4
> Simulation Settings
> Pyramid theme: CHNIDIIMODEL X1.6
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaNHar
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.59
> 48.989
> 0.96
> 17.739
> 14.389
> 7.249600
> Equity
> CHN
> TOPZOOOU
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,00
> 50.9796
> 2.14
> 25.8395
> 3.459
> 10.14930
> 376
> 311
> Clone Alpha
> 2014
> 3.19
> 50.37%6
> 2.39
> 28.3395
> 4.5996
> 11.259530
> 449
> 375
> 2015
> .99
> 43.99%
> 1.76
> 32.2995
> 14.38%
> 15.5935o
> 726
> 502
> 2016
> 2.15
> 46.26%
> 22.0595
> 5.0596
> 9.5390
> 675
> 556
> Chart
> Pnl
> 2017
> 0.46
> 46.93%
> 0.14
> 43895
> 8.6795
> 879530
> 595
> 501
> 2018
> 1.31
> 48.3796
> 0.64
> 11.6395
> 4.6796
> 83900
> 554
> 455
> 2019
> 2.07
> 50.56%
> 1.22
> 17.6995
> 4.11%
> 9850
> 524
> 420
> 2020
> 0.17
> 50.68%
> 0.03
> -1.9695
> 10.9096
> 0.77930
> 542
> 427
> 1ON
> 2021
> 51.20%
> 0.38
> 11.1295
> 9.73%
> 4.34900
> 543
> 425
> 2022
> 50.5696
> 1.12
> 20.1999
> 5.7390
> 7.979530
> 552
> 447
> 5,00OK
> 2023
> 10.25
> 50.3896
> 10.51
> 52.9395
> 2496
> 21.019500
> 562
> 484
> Risk neutralized
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> 1.17
> 48.989
> 0.39
> 5.4296
> 18.579
> 2.219600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.52
> 42.179
> 0.97
> 17.049
> 14.409
> 8.089600
> IS Testing Status
> Period
> IS
> 05
> [
> Correlation
> 8 PASS
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 6;01
> Turnover of 48.989 is above cutoff of 1%
> PM
> Turnover of 48.98% is below cutoff of 70%
> Weight is well distributed over instruments。
> Returns Of 17.73% is above cutoff of 8%.
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 6;01
> Sub-universe Sharpe of 1.55 is above Cutoff of 1.13.
> PM
> Robust universe Sharpe of 1.30 is above CUtoff of 0.64 (40% of Alphal
> 0.8918
> -0.2468
> Robust universe returns of 9.139 is above cutoff of 7.09% (40% of Alphal.
> These pyramid themes match with the following multipliers: CHN/DI/RISK-
> 1.4; CHNIDIIMODEL
> 1.6.The final
> pyramid theme multiplier is 1.4. Effective pyramid count for Genius is 2。
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 6;01
> PM
> 5WARNING
> 0.8234
> -0.6297
> Sharpe of 1.59is below CUtOff of 2.07.
> chng


我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi. worldquantbrain comlalphas/SdnGl4z
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 17.925
> 2.3 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三 Q6 &
> 15
> IaXTTaCE
> OFF
> operatorcount
> 酏*
> 1Of1
> 个 b = X
> 17
> "language
> IFASTEXPR"
> 18
> IVis0a1i2ation"
> false
> 19
> startDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> TegUIaT"
> 23
> COCE
> raIk (2
> ISk72_a20p2000_
> OSIT)
> raIk (3
> 10125_
> Chng_IICV_T_
> 工5511
> 2000_
> 30)
> 24
> "description"
> Iaea:
> Dual-Iank PIOCUCT
> Signal
> Combining
> SHOIT
> MnTerest
> anC
> RSS
> Iquidity
> Changes
> 1nRaTi3na12
> for 0a-a
> USeC:
> 1 -
> ISK72
> aTOp2OOO_OSIT:
> RUSSeII
> 2000
> SHOIT
> MnTerest
> percentile
> {几-
> Ic126_chng_
> IITV_T_ISSII
> 2000_
> 30:
> 30 -
> IelatIve Izquzdity
> Change
> SCOIC
> InlnRaionale
> fJI
> OpeIaTOIS
> USee
> 1-
> EXpOnenTiaI
> TransforIs
> CIeaTe
> COIVCX
> Ianking:
> 3a5e-2:
> SHOIT
> Interest
> aMplification
> 3a5e-3
> Htouidity
> change sensitivity
> 1 -
> MulTiplicaive
> Combinazion:
> High when
> boTh
> signals
> agTeE
> Near- ZeIn
> when
> eiTher
> neUTIaI
> {- Negative
> SIgn
> CargeTs:
> High
> SHOIT
> MnTerest
> CeTeriorating
> liquidity
> 1"5hoI
> 50UeeZe
> TIap
> ioentification
> OpezatozCount
> 25
> 27
> "datecreated "
> 2025
> 08-14T05:27:35-04:00
> 75
> rateSwhmitterl"
> 2025-08-15T01:04:25-04:Q0
> alpha C
> day


重复算 operatorCount 操作符了 .

没有  **字段使用数量信息** ，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .

[图片 (图片已丢失)]

**重点** ：巧妙的节省重复操作符 ！！！

从以上几个alpha操作符测试，让我们知道了

i ) +、-、*、/ 和 ^ 都是算入操作符计数的；

ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；

iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha

3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/12/2025 EDT
> anonymoUs
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> brk
> VeC
> Sum(brkl_start_stock_price);
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIBROKER X1.5
> alpha
> ts covariance
> bpk,
> 股票起始价格汇总
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> bpk
> 11同一序列的自相关讦算
> 1.05
> 13.439
> 0.86
> 9.059
> 10.689
> 13.479600
> 24
> 24周期(约1个月)滚动窗0
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0,80
> 14.3096
> 5.2995
> 5.0195
> 40930
> 1157
> 1571
> Instrument Tpe
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> 2014
> .85
> 12.39%
> .90
> 13.2495
> 3.239
> 21.369600
> 1424
> 1722
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> On
> OfT
> 2015
> +28
> 12.59%6
> 1.28
> 12.6295
> 7.6596
> 20.05930
> 1537
> 1751
> 2016
> 1.36
> 13.59%
> 1.57
> 18.2595
> 9.249
> 26.67930
> 1477
> 1690
> 2017
> 0.63
> 11.4796
> 0.32
> -3.20%
> 6.959
> -5.5893o
> 1746
> 1497
> Clone Alpha
> 2018
> 0.72
> 12.4696
> 0.52
> 5.469
> 8.5096
> 10.379530
> 1980
> 1765
> 2019
> 13.25%
> 1.71
> 13.5695
> 5.18%
> 20.47930
> 1757
> 1611
> 2020
> 0.47
> 15.54%
> 0.25
> 2.4495
> 7.5096
> 68930
> 1818
> 1731
> Chart
> Pnl
> 2021
> 14.52%
> 1.17
> 10.8195
> 4.0096
> 14.79930
> 2194
> 2300
> 2022
> 1.17
> 13.7096
> 0.94
> 8.759
> 6.35%
> 12.779530
> 1980
> 2197
> 2023
> 0.48
> 20.3796
> 0.17
> 26Ob
> 8296
> 2.5593o
> 1640
> 1992
> 7,50OK
> SOOOK
> Correlation
> 2,50OK
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,8;43
> Du
> 0.2112
> -0.0733
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 8;43
> PM
> 0.4247
> -0.0733
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 8;44
> PM
> 0.3960
> -0.3483


我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain comlalphaslobd5qOE
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 2.545
> 2.41 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> nanHandling"
> OFF
> operatorcount
> 劭
> ? Of1
> 个 b = X
> 16
> IaXTTaCE
> ON
> 17
> "language
> FASTEXPR
> 18
> IVis0ali2ation
> false,
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE"
> Ibrk
> VeC
> SUII ( bIkz_
> STAIT_
> sTOCk_priCe ) ; Irlnalpha
> C5_
> Covariance (IIin
> DIK,
> L 股票起始价格汇总 Irln
> bIk ,
> LL 同-序列的
> 自相关计算 {210
> 24
> J24周期〈约1个月)滚动窗OIrln) ; '
> 24
> "JesCZIptiOn"
> Iaea:
> COIpUTE
> the negatlve IoIIIng
> COVariance
> Of aggTegated
> starting stock prices with itself
> Iea5UIE
> 5e11-similarity
> anO
> invert
> The
> Ielationship
> InRationale
> fJI
> USeO:
> The aggIe
> starting
> STOCK priCe
> (VeC_
> SUII
> (brki_
> STaIT
> sTOCk_price)
> IeTIeCTS
> baseline
> Valuation
> levels
> 35
> boTh
> IpUTS
> COVariance
> CapTUIeS
> i5
> OIII
> Volatility
> and pattern
> consistency
> InRaTionale
> for OperatoIs
> USeC:
> The
> 24-period
> COVariance
> (TS
> COVariance)
> SeIies Iizh
> iself simplifies
> VaTZance
> measUring
> HOWI Uispersed
> The
> Values
> aIe
> aIOUnC
> Their
> IIean
> DVEI
> ShOIt
> term Window.
> The
> negative
> sign (-)
> TIVeITS
> 375,
> 50
> higher
> Variance (inszability)
> IeSUITs
> 11
> IOIeI
> 518na1 ,
> penalizing
> VoIatility
> 25
> OpezatozCount
> 25
> alpha C
> Jaza
> gazed
> Using


事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/01/2025 EDT
> jiao?
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> Vector
> neut
> VeC
> SUN(rSKGG
> offer),
> VeC
> SUm(rsk6o
> Offer)))
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> Simulation Settings
> 1.33
> 10.339
> 1.05
> 7.819
> 16.029
> 15.139600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Equity
> USA
> ILLIQUID_MINVOLIM
> Fast Expression
> 0.08
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.009
> 0.00
> 0.0096
> 00%
> 0093o
> 2014
> 1.30
> 7.1995
> 0.77
> 4.4296
> 1.6296
> 12.36950
> 936
> 1552
> 2015
> -0.29
> 7.5095
> -0.21
> 2.28%
> 8390
> 079330
> 716
> 1825
> Clone Alpha
> 2016
> 1.03
> 7.3295
> 5.4796
> 0996
> 14.93930
> 539
> 1878
> 2017
> 0.77
> 8.3595
> 3.36%
> 4.839
> 0593o
> 555
> 832
> Chart
> Pnl
> 2018
> 1.07
> 13.9099
> 5.29%
> 2.5795
> 7.62930
> 577
> 888
> 2019
> 0.95
> 13.0395
> 5.5596
> 4.98%
> 8.5390
> 512
> 1905
> 2020
> 1.25
> 11.1495
> 1.16
> 10.6596
> 5.11%
> 19.139500
> 464
> 1922
> 2021
> 0.91
> 10.1895
> 0.b
> 79%
> 12.53%
> 13.34930
> 2248
> 2022
> 5.02
> 14.389
> 7.52
> 32.31%
> 2.2796
> 44.9493o
> 1070
> 1821
> 40OOK
> 2023
> -1.55
> 10.6890
> -1.48
> -11.40%
> 2.35%
> -21.32930
> 752
> 1893
> 20OOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;55
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Du
> 0.3766
> -0.1774
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;55
> PM
> 0.3713
> -0.1928
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;55
> 00
> IS Testing Status
> Period
> OS
> PM
> 0.6809
> -0.5425


这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =

1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .

[图片 (图片已丢失)]

2. 点塔！

```
点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题
```

当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节： [交一个怎样的alpha能提升你的六维数据之定性定量分析 .]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！

关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：

i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)

[图片 (图片已丢失)]

比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 . 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(anl3g
> rOXLCXSpeq
> anl3g_xIcxspemtp)
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> RetUrns
> DrawOOwn
> Margin
> Simulation Settings
> 0.37
> 3.549
> 0.14
> 1.869
> 13.18%
> 10.539600
> Instrument Tpe
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.71
> 3.769
> 1.30
> -7.22%
> 11.439
> -38.389530
> 775
> 1332
> 2014
> 1.18
> 3.1795
> 0.75
> 5.0096
> 3.51%
> 31.53950
> 1058
> 1558
> 2015
> 0.37
> 3.4295
> 0.15
> 2.1796
> 7.36%
> -12.67900
> 1156
> 1557
> Clone Alpha
> 2016
> 1.83
> 3.8795
> 1.84
> 12.6796
> 3.21%
> 65.529530
> 1093
> 1627
> 2017
> 0.58
> 3.3295
> 0.32
> 2.6996
> 5.33%
> 16.2390
> 1172
> 1779
> Chart
> Pnl
> 2018
> 1.81
> 3.43995
> 1.42
> 7.42%
> 3.40%
> 43.25930
> 1135
> 1792
> 2019
> -U.61
> 3.3995
> 0.33
> 3.029
> 4.92%
> -17.9390
> 004
> 1825
> 2020
> 3.5395
> 0.10
> 5696
> 5.6796
> 8.84930
> 998
> 1752
> 2021
> 1.38
> 3.8595
> 5.5896
> 4.20%
> 28.97930
> 1855
> OOOK
> Mlwto
> 2022
> 0.32
> 3,6695
> 0.13
> 9996
> 859
> 10.8593o
> 1072
> 830
> 2023
> -3.70
> 3,0095
> 2.01
> -14.5890
> 0090
> 97.97930
> 970
> 1792
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Margin
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 0.27
> 2.2296
> 0.09
> 1.4096
> 14.639
> 12.579600
> Pnl
> Investability Constrained Pnl
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;36
> PM
> 0.2624
> -0.0448
> IS Testing Status
> Period
> OS
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;37
> PM
> 0.8554
> -0.6340
> 5PASS


通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 07/30/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank
> star
> Val
> industry_rank
> anl39
> rOXLCXSpeq
> anl39_xlcxspemtp
> Power Pool Alpha
> Pyramid theme: EURIDIIMODEL X1.4
> Simulation Settings
> Pyramid theme: EURIDIIANALYST X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.45
> 7.5596
> 1.91
> 7.629
> 4.2396
> 20.189600
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> On
> On
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.70
> 6.7096
> 1.04
> 46895
> 1.289
> 13.98900
> 778
> 1329
> Clone Alpha
> 2014
> 3.25
> 7.59%6
> 2.69
> 8.5495
> 1.149
> 22.5035o
> 1070
> 1525
> 2015
> 1.27
> 7.84%
> 0.72
> 2.0595
> 2.839
> 10.359500
> 1113
> 1611
> 2016
> 4,09
> 8.03%
> 2.34
> 12.0895
> .20%
> 35.07930
> 1025
> 695
> Chart
> Pnl
> 2017
> 2.61
> 7.3396
> 1.75
> 5.6295
> #1090
> 15.3390
> 1120
> 831
> 2018
> 3,05
> 7.7096
> 2.30
> 7.10%
> 2.0590
> 18.43900
> 1166
> 1750
> 2019
> 1.27
> 7.56%
> 62
> 3.0195
> 1.70%
> 7.95930
> 1183
> 1625
> 2020
> 2.34
> 8.01%
> 1.94
> 8.6095
> 1.72%
> 21.469530
> 1121
> 1621
> 5OOOK
> 2021
> 2.71
> 86%
> 2.35
> 9.4095
> 3.52%
> 27.40950
> 1122
> 1820
> 2022
> 2.45
> 7.81%6
> 2.27
> 10.75%
> 4.2390
> 27.51930
> 1163
> 1739
> 2,50OK
> 2023
> 3,80
> 7.5596
> 3.63
> 11.8095
> 0.489
> 31.269500
> 1093
> 1672
> Investability constrained
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.88
> 3.599
> 1.30
> 5.9796
> 3.9796
> 33.269600
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025,7.05
> PM
> 00
> IS Testing Status
> Period
> 05
> 0.5189
> -0.0937
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> 8 PASS
> PM
> 0.5189
> -0.1529
> Sharpe of 2.45 is above CUtOff of 1.58.
> Fitness Of 1.91 is above cutoffof1.
> Turnover of 7.5596 is above CUtoff of
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> PM
> Turnover of 7.55% is below cutoff of 70%.
> Weight is well distributed over instruments。
> 0.8288
> -0.4965
> Sub-universe Sharpe of 1.27 is above cutoff of 1.27.
> IS Iadder Sharpe Of 2.49 is above cutoff of 2.02 for Iadderyear 2: 1/20/2023.1/21/2021


ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> OS
> ts_target_
> tvr_decay (imbs_
> SCOre
> Iambda_min-o,
> Iambda
> maX=l, target
> tVr=0.1
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> Simulation Settings
> 2.86
> 7.7796
> 1.98
> 5.979
> 2.319
> 15.379600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.32
> 7.96%
> 2.54
> 7.3295
> 009
> 18.40950
> 1363
> 1355
> 2014
> 5.73
> 7.0796
> 5.12
> 9.999
> 0.739
> 28.259530
> 1569
> 1577
> 2015
> 4.83
> 7.5196
> 264
> 11.5495
> 1.289
> 30.7390
> 1645
> 653
> Clone Alpha 
> 2016
> 2.76
> 7.3796
> .82
> 5.42%
> .6890
> 14.71930
> 1574
> 593
> 2017
> 2.23
> 7.51%
> 3.00
> 5.2995
> 639
> 16.52930
> 1610
> 533
> Chart
> Pnl
> 2018
> 3.49
> 7.81%
> 2.54
> 6495
> .239
> 6.93930
> 1875
> 1871
> 2019
> 2.96
> 7.5596
> 2.04
> 5.9195
> 1.129
> 15.45930
> 645
> 1723
> 2020
> 8.30%6
> 22795
> 1.729
> 5.48930
> 1736
> 1813
> 2021
> .05
> 299
> 2.43%
> 2.31%
> 5.86930
> 2203
> 2291
> 40OOK
> 2022
> 7.97%6
> 0.22
> 1.5195
> .839
> 3.79950
> 2057
> 2121
> 2023
> 11.09%
> 5.57
> 8.2395
> 08%
> 14.85930
> 1783
> 1829
> ZOOOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;33
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> PM
> 0.3352
> -0.0929
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> Du
> 0.5597
> -0.1764
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> IS Testing Status
> Period
> 0S
> Du
> 0.9227
> -0.5410
> Year


比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .


> [!NOTE] [图片 OCR 识别内容]
> 说到这里,
> 我想说一下关于提交 alpha 关于 Prod Correlation ,
> Power Pool
> Correlation 和 Self Correlation,
> 也许在绿灯亮起提交 alpha 显示出的错误或许不
> 那么明确. (个人看法,如有问题还望大佬们不忘吝啬,
> 可评论区说明我好做出调
> 整)但大致是这样的 .
> 举个例子:有一个国王喜欢吃各种各样式的苹果
> 大家都会送苹果给国王
> 吃,
> 当然会获得相应的报酬,吃之前需要将苹果放进池子进行清洗,
> 有两个大小
> 的池子。如果你送来的苹果好,自然是放在大池子里。和大池子里的苹果比较 ,
> 如果大池子没有类似的苹果,
> 或者如果有类似的苹果,
> 但是你的苹果比这个类似
> 的苹果有更少的瑕疵,那你的苹果将会被收取从而获得报酬;  如果你的苹果不满^
> 足大池子,
> 那就继续按照以上这种方式放小池子,
> 当然这种小池子只是大家人手
> 一个,
> 大池子也是谁想用可以随时搬自己家测试,
> 小池子的作用是什么,如果大
> 池子的苹果被国王吃完了,那就会考虑小池子了,当然人家毕竟是国王,没有那
> 么容易吃完大池子的稀奇苹果.



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 09/11/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> ts_target_
> tvr_decay (imbs_
> SCOre
> mCr63_membership,  Iambda
> min=0
> Iambda
> Iax=l
> targe
> Power Pool Alpha
> Pyramid theme: ASIIDIIIMBALANCE X1.1
> Simulation Settings
> Pyramid theme: ASIIDIIMACRO X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 7.739
> 1.19
> 5.249
> 5.899
> 13.56900
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> 0n
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.03
> 8.02%
> 1.34
> 5.4795
> 2.0596
> 13.63330
> 1377
> 1351
> Clone Alpha 
> 2014
> 2.21
> 7.0596
> 407
> 11.659
> .76%
> 33.089500
> 1573
> 1573
> 2015
> 3.41
> 7.4796
> 293
> 9.20%
> 1.129
> 24.61930
> 670
> 628
> 2016
> +94
> 7.45%6
> 0.47
> 3.16%
> 5.8990
> 48930
> 590
> 1577
> Chart
> Pnl
> 2017
> 2.28
> 7.50%
> 2.8895
> 1.6596
> 12.84930
> 620
> 1623
> 2018
> 2.55
> 7.74%
> .84
> 5.5395
> 1.2996
> 16.879500
> 899
> 1827
> 2019
> .83
> 7.5496
> 1.14
> 4.8795
> .9890
> 12.91930
> 1705
> 653
> 2020
> 0.02
> 8.3296
> 0.00
> 0.059
> 2.259
> 0.1593o
> 800
> 1729
> 2021
> 8.18%6
> 1.21
> 5.159
> .6390
> 12.5893o
> 2305
> 2190
> 2022
> 7.82%
> 0.07
> 0.8795
> 2.5696
> 2.239500
> 2113
> 2055
> ZOOOK
> 2023
> 3.80
> 10.50%
> 3.02
> 7.9295
> 0.1996
> 15.08930
> 864
> 1757
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;43
> PM
> 0.3474
> -0.0437
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.3645
> -0.0892
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.6217
> -0.4420
> PASS
> Vear


事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .

[图片 (图片已丢失)]

3. 好而优的 alpha

何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .

一点：好，我理解在:

1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；

2) fitness ≥ 1  全方面稳定还是非常不错；

3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；

4) returns ≥ 10%  收益还是要好点能赚钱吧；

5) drawdown 回撤越小越好吧，大了心理抗压不行；

6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；

7) 十年数据中做多做空不能太少吧，权重太高危险危险！

8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .

满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/08/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> 1
> OS Summary
> Period
> I5
> 05
> peVerse(r
> ib5
> SCOre
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDOIIMBALANCE
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> Simulation Settings
> 0172112023 CT
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Close
> Close Ratio
> Self-Correlation
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone Alpha
> 2013
> 3.9
> 23.8899
> 4.13
> 26.189
> 2.5995
> 21.929600
> 986
> 405
> 2014
> 3.52
> 22.6895
> 3.36
> 20.65%
> 2.9096
> 18.22930
> 1070
> 431
> 2015
> 3.32
> 22.8295
> 3.46
> 24.43%
> 3.03%
> 21.41950
> 1130
> 459
> Chart
> Pnl
> 2016
> 2.53
> 21.1195
> 2.65
> 21.4796
> 3.4796
> 20.349530
> 1138
> 455
> 2017
> 2.77
> 20.7795
> 2.47
> 16.5496
> 3.40%
> 15.92930
> 1125
> 470
> 2018
> 1.88
> 19.5696
> 1.67
> 15.3796
> 7.27%6
> 15.71930
> 1010
> 418
> 2019
> 2.77
> 19.1395
> 3.03
> 22.829
> 3.18%
> 23.8890
> 998
> 423
> 1ON
> 2020
> 0.71
> 19.4395
> 0.39
> 5.9596
> 5.659
> 2930
> 908
> 392
> 2021
> 1.73
> 19.20%
> 10.789
> 5.089
> 11.22930
> 972
> 416
> 5OOOK
> 2022
> 18.4390
> 1.42
> 14.789
> 4.5795
> 16.0493o
> 050
> 439
> 2023
> 10.22
> 31.6599
> -14.39
> 62.7790
> 3.5796
> 39.67930
> 945
> 393
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pre
> Sharpe
> Pre


二点：优，我理解在:

1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；

2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；

3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；

使用


> [!NOTE] [图片 OCR 识别内容]
> 1
> 1.
> 事件距离基础信号:  距离越大。事件影响越小
> eVent
> signal
> VeC
> SUI
> nWs7g_event_detection_distance_358-
> 1
> 距离平方增骚:  放大极端距离信号的非线性影响
> brk
> VeC
> sum(brkl_start_stock_price);
> distance_squared
> event_signal
> 2;
> alpha
> ts covariance(
> brk,
> 股票起始价格汇总
> 1
> 词频倒数因子:  词数越少。信息浓度越高(1/词数)
> brk,
> 11  同一序列的自相关计算
> Word
> density
> 二 1
> VeC
> SUII
> nWS7g_word_count_391 )
> 24
> 24周期(约1个月)滚动窗口
> 10
> 1
> 复合事件驱动因子:  距离信号
> 非线性增骚
> 信息浓度
> 11
> alpha
> (event_signal
> distance_squared
> Word_density)



> [!NOTE] [图片 OCR 识别内容]
> 11 Core Logic:
> Reverse standardized composite factor
> reverse
> operation when large trader behavior diverges
> 1
> Synthetic
> Base
> Factor: Market
> pattern
> trader Value differential
> base factor
> mdl175 OGam
> power(Vec
> sum(pvz7_value_diff_large_trader), 2);
> /12. standardization: Convert to
> Z-score to eliminate scale effects
> Zscore_factor
> Zscore(base_factor) =
> 1
> Signal Reversal: Negative sign indicates
> Contrarian
> selection, seeking
> undervalued
> opportunities
> alpha
> ZSCOre
> factor;
> large



> [!NOTE] [图片 OCR 识别内容]
> Description
> 507
> 100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template_
> Idea: Identify the time index ofthe maximum imbalance score over a 2O-day Window, then invert the result:
> Rationale for data used: The imbalance score (imb5_score) likely measures order flow or liquidity asymmetry; its maximum pinpoints the
> most extreme positive imbalance event。
> Rationale for operators Used: The 20-dayarg max (ts_arg_max)returns the lookback period (0-19) where the series peaked_and the


不建议使用


> [!NOTE] [图片 OCR 识别内容]
> 1 |
> ts_covariance(vec
> SUm(brkl_start_stock_price) ,
> VeC
> sum(brkI_start_stock_price), 24)



> [!NOTE] [图片 OCR 识别内容]
> brk
> VeC
> sum(brkl_start_stock_price)
> alpha
> ts covariance
> brk,
> 股票起始价格汇总
> bk,
> 11同一序列的自相关计算
> 24
> 1124周期(约1个月)滚动窗口
> );
> alpha


[图片 (图片已丢失)]

**三、alpha模板 ！**

看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .


> [!NOTE] [图片 OCR 识别内容]
> N-1
> Ha
> 1,3N,8.七
> lim
> fa()-Cfa(a)
> 二
> Iim
> fa(a)
> n-〉+O
> n〉+O
> 2二1
> 2二1
> C=N
> 10-P


换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！

field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .

其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> 2,000
> UUJ
> OIlU
> 〈ee
> 3" A0。
> 02
> Displayed Period
> 02/14/2025
> 09/12/2025
> 149346
>  Mar
>  Mar
> Mar
> Mar
> Mar
> 30。
> 31。
> 24。


从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .

[图片 (图片已丢失)]

使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .

造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .

[图片 (图片已丢失)]

下节预告:  [Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

2025年9月14日

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的分享，我认真地看完了，文章的风格独特且美观，我也收获了很多，对于alpha的研究豁然开朗，有了不一样的见解，并且，此前一直没有想过用a=表达式1；表达式2（a)；这样也可以降操作符，突然感觉自己损失了很多；再者，对于在表达式中再加一个字段有时可以改良alpha的性能，以及我们可以自创数据字段，这些为我后面的研究带来了启迪性的作用


---

### 技术对话片段 115 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 如何利用tvr操作符与alpha起舞论坛精选.md
- **时间**: 9个月前

**提问/主帖背景 (QX52484)**:
##### ts_target_tvr_decay(x, lambda_min=0, lambda_max=1, target_tvr=0.1)

需要输入的参数为以上4个。

通过lambda_min值（不衰减），和lamdba_max值（衰减）的搜索空间中，去搜索lambda（λ)值，来得到target_tvr值。

也就是说，足够大的搜索空间，通过能得到一个λ，使得alpha的tvr为target_tvr值。

而目前多数顾问采用的是

##### lambda_min=0, lambda_max=1, target_tvr=[0.1,0.15,0.2,0.25] 这样的用法。

但按照我个人理解，设置成

##### lambda_min=0, lambda_max=5, target_tvr=[0.01，0.15，1]   （其中1是tvr参数的是上限值）

在扩大搜索空间后，使得alpha tvr的变化呈现缩小值、理想值、强化值。 这样的用法会更有意义。

**因为与其在固定的搜索空间去趋近target_tvr ，不如扩大搜索空间，跳出局部求解更为实际。如果将**

##### **lambda_min=0, lambda_max=5, target_tvr=0.15作为模板，那么搜索对于tvr弱的alpha，λ值会趋向于5，旧信号衰减更快，增强tvr,趋近0.15。对于tvr强的alpha，λ值会趋向于0，旧信号衰减更慢，降低tvr趋近0.15。是一个自适应的模板。类似decay的用法。**

若如果不存在相应的λ值，0.01和1也使得tvr的变化朝减弱和增强进行了延伸。综上所述，tvr 操作符总是能将tvr值按照自己理想的方向进行变化，是一个很实用的操作符。

比如这个alpha，看到tvr为2.58%， 通常是认为是一个beta而放弃提交。

[图片 (图片已丢失)]

但通过增强，可能会使得tvr落到理想的区间内，可以不用担心因为tvr<5%or<10% 降低可用性。

[图片 (图片已丢失)]

降低tvr的方式参考游戏王的降tvr帖子即可。

其他微调tvr的方式如调整decay trucation ts_op的day 亦可尝试。

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的分享，要不是大佬分享我还不会注意到有这个操作符，以前都专注于交低turnover的alpha，以至于交了很多3%甚至2%的alpha，自从听了weijie老师的讲解，才开始反思其为什么turnover会这么低，于是我会对每个低turnover并且margin足够高的alpha根据大佬的讲解套ts_target_tvr_decay以提高turnover并尽可能使margin保持在合理范围内


---

### 技术对话片段 116 (原帖: 如何利用tvr操作符与alpha起舞论坛精选)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 如何利用tvr操作符与alpha起舞论坛精选_34562640928023.md
- **时间**: 9个月前

**提问/主帖背景 (QX52484)**:
##### ts_target_tvr_decay(x, lambda_min=0, lambda_max=1, target_tvr=0.1)

需要输入的参数为以上4个。

通过lambda_min值（不衰减），和lamdba_max值（衰减）的搜索空间中，去搜索lambda（λ)值，来得到target_tvr值。

也就是说，足够大的搜索空间，通过能得到一个λ，使得alpha的tvr为target_tvr值。

而目前多数顾问采用的是

##### lambda_min=0, lambda_max=1, target_tvr=[0.1,0.15,0.2,0.25] 这样的用法。

但按照我个人理解，设置成

##### lambda_min=0, lambda_max=5, target_tvr=[0.01，0.15，1]   （其中1是tvr参数的是上限值）

在扩大搜索空间后，使得alpha tvr的变化呈现缩小值、理想值、强化值。 这样的用法会更有意义。

**因为与其在固定的搜索空间去趋近target_tvr ，不如扩大搜索空间，跳出局部求解更为实际。如果将**

##### **lambda_min=0, lambda_max=5, target_tvr=0.15作为模板，那么搜索对于tvr弱的alpha，λ值会趋向于5，旧信号衰减更快，增强tvr,趋近0.15。对于tvr强的alpha，λ值会趋向于0，旧信号衰减更慢，降低tvr趋近0.15。是一个自适应的模板。类似decay的用法。**

若如果不存在相应的λ值，0.01和1也使得tvr的变化朝减弱和增强进行了延伸。综上所述，tvr 操作符总是能将tvr值按照自己理想的方向进行变化，是一个很实用的操作符。

比如这个alpha，看到tvr为2.58%， 通常是认为是一个beta而放弃提交。


> [!NOTE] [图片 OCR 识别内容]
> Settings
> GLB/D1/MINVOLTM
> IS Summary
> Period
> Streak: 107 day
> A single Data Set Alpha
> quantile(signed_power(Broup_neutralize( -
> Count_nans
> Winsorize
> ts_backfill(ern3_
> next_reptime,5),std=4),22)),
> Country)1.8)
> Aggregate Data
> Sharoe
> TUTNIUE
> FNss
> REUTR
> LTaOCI
> Narai
> 1.35
> 2.5896
> 0.86
> 5.02%
> 4.3096
> 38.959600
> Year
> Sharpe
> Turover
> Ftess
> Returns
> Drawdown
> Margln
> Long Count
> Short Count
> 2013
> 0.73
> 4.25
> 533
> 2.32
> 11.338:
> 367
> 355
> 2014
> 1.2-
> 3.25
> 3.2E3
> 2.159
> 20.03:
> 41|
> 3370
> 2015
>  5
> 3.33
> E73
> 2.77
> 038:
> 4316
> 1050
> TIC
> 1.46
> 03:
> TJ
> .39
> 4.6:
> 4133
> 33T1
> 2017
> 0.86
> 2.35
> ES%
> 1.759
> 11.575
> 4279
> -120
> 711?
> 1.73
> 2-
> 一273
> 1.379
> 3.32:
> 4621
> -52
> 2015
> 0.25
> _一=
> U6;
> 3.55
> 77304
> 4513
> 3335
> 2020
> 1.13
> 1.73
> 3
> 71 :
> 4333
> 333
> 2021
> 1.
> 88%
> 2.179
> 42.139
> 575-
> -332
> 2022
> 2.76
> 1_ 
> 13.253
> +3
> 201.329
> 573-
> 一37
> 2023
> 0
> 7.7%
> SS
> 155.84903
> 573
> 3375
> AMER
> Aggregate Data
> Snaroe
> TITIT
> Cc
> ReTylrns
> Drawdow
> Marsn
> 0.79
> 1.01%
> 0.28
> 1.59%
> 6.99%
> 31.469600
> APAC
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> CTOI
> MarEn
> 0.60
> 0.9196
> 0.23
> 1.7996
> 7.36%
> 39.479600
> EMEA
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> Cratda'
> MarEn
> 96
> 0.659
> 0.35
> 1.629
> 3.149
> 49.709600
> Clone this Alphain
> newtab
> Risk neutralized


但通过增强，可能会使得tvr落到理想的区间内，可以不用担心因为tvr<5%or<10% 降低可用性。


> [!NOTE] [图片 OCR 识别内容]
> Simulation 14A
> Simulation 148
> Settings
> GLB/D1/MINVOLTM
> IS Summary
> Period
> Streak: 107 day
> Single Data Sez AIpha
> A Power Pool Alpha
> Pyramid theme: GLB/DTIEARNINGS %1
> ts_target
> tvr_decay(quantile(signed_power(growp_neutralize((
> count_nans
> winsorize(
> backfill
> (ern3
> next_reptime,5),std-4),22)),
> country ),1.8) ) 
> Iambda_min=o,
> lambda_max=3,
> target_tVrzl)
> Aggregate Data
> 33TO
> LJTC=
> TITE
> RCUTTS
> UTWIOOYT
> Harein
> 1.57
> 10.759
> 1.21
> 7.46%
> 4.9296
> 13.879600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margln
> Long Count
> Short Count
> 2013
> 12.31
> 7.73
> 一7
> 263沾
> 119
> 3715
> 351
> 2014
> 10.335
> 0.75
> 3.319
> SE
> 一SO
> 412E
> 3355
> 215
> 0.53
> 1.21
> 7.27
> 0
> 2.30沾
> 9
> 4343
> 4134
> TIC
> 2.37
> 181
> 5
> Ss
> 13.3_5:
> 4193
> 3331
> 2017
> 0.74
> 0.7
> 529:
> 2.17沾
> 339
> Jy
> J1IE
> 711?
> 0.67
> 5.13
> 4E
> 匕
> JFU
> 一
> 2015
> 5;
> 0.42
> 3.75
> 3.51沾
> 1.229
> 432
> 3555
> 1
> 10.76:
> 13.159
> 一 C
> 1 65:
> 21
> 3355
> 2021
> 10.75
> 15.329
> 2.50沾
> 29.46*o:
> 527
> -373
> 2022
> 3.35
> 0.35
> 27.37
> 355
> 3.554:
> 557
> -235
> 2023
> 0.5
> 6:
> 7.23
> 3310
> CI:;
> 4
> 5717
> 3570
> AMER
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> Cryda
> Marsn
> 1.24
> 3.73%
> 0.63
> 3.22%
> 5.92%
> 17.279600
> APAC
> Aggregate Data
> Snaroe
> TITTT=
> Cc
> ReTylrns
> Cratda'
> MarEn
> 0.69
> 2.65%
> 0.25
> 1.70%
> 5.559
> 12.869600
> EMEA
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> Drawdowir
> Marsn
> 0.97
> 2.12%
> 0.40
> 2.17%
> 4.60%
> 20.509600
> Clone this Alphaina newtab
> Risk neutralized
> 41013
> OpnLOA


降低tvr的方式参考游戏王的降tvr帖子即可。

其他微调tvr的方式如调整decay trucation ts_op的day 亦可尝试。

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的分享，要不是大佬分享我还不会注意到有这个操作符，以前都专注于交低turnover的alpha，以至于交了很多3%甚至2%的alpha，自从听了weijie老师的讲解，才开始反思其为什么turnover会这么低，于是我会对每个低turnover并且margin足够高的alpha根据大佬的讲解套ts_target_tvr_decay以提高turnover并尽可能使margin保持在合理范围内


---

### 技术对话片段 117 (原帖: 连续三个季度蝉联Master，我的佛系Genius之旅经验分享)
- **原帖链接**: [Commented] 连续三个季度蝉联Master我的佛系Genius之旅经验分享.md
- **时间**: 10个月前

**提问/主帖背景 (XD81759)**:
一、历程（无干货，建议跳过）

2024Q4，世坤推出了Genius评级计划。由于前期躺平，压力给到12月，虽然12月交了121个alpha，但总数距离220还是差了三四个，自然无缘Grand Master（当然，就算交够了也不一定能成），只能成为中国大陆8位Master中的一员。

2025Q1，由于Combine改版，12月又交了太多高换手的因子，导致combine直接砍半（从3+变成了1.5左右）。雪上加霜的是VF降到了0.13，开始坐牢。心灰意冷之下，又进入了躺平状态。该赛季共提交RA 58个，SA 62个，刚好达到Master的标准，成为了中国大陆16位Master中的一员。

2025Q2，或许是躺平躺习惯了，又或许是5000美元的季度奖已经差强人意（0.97的VF使得日均BASE超过40美元进一步加强了这种情绪），这个赛季依然得过且过，共提交RA 62个，SA 60个，勉强达到Master的标准，成为了中国大陆70位Master中的一员.

二、经验

Q2的Master对我来说其实殊为不易，最大回测天数断了很多次，加分会议只参加了一次，能够保住Master，归根到底得益于：压per。我Q2基本上只使用了一阶的模板，虽然未能调到对performance最好的状态，但近三个月0.97、0.99、1.00的VF说明这种兼顾Genius和VF的方式是可行的。

三、展望

相信每个顾问都有一个成为Grand Master的梦想，我自然也不例外。摆在我面前的第一座大山便是Combine，我的三个Combine一直稳定在1.5左右，距离Grand Master要求的2还差一些。对此，我已找到解决的办法，等成功后便分享给大家，敬请期待！

（如果以上内容对您有帮助，请点点赞，谢谢~）

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的经验分享，我现在开始注重六维开始压per了，不过现在达到master要点30个塔，有必要为了点塔交那种比较差的alpha吗，就比如数据缺失或者turnover高amrgin低的这种影响vluefactor，交了这种alpha总觉得污染了我的池子，但是不交又觉得难以点到30个塔


---

### 技术对话片段 118 (原帖: 连续三个季度蝉联Master，我的佛系Genius之旅经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 连续三个季度蝉联Master我的佛系Genius之旅经验分享_33628502441751.md
- **时间**: 11个月前

**提问/主帖背景 (XD81759)**:
一、历程（无干货，建议跳过）

2024Q4，世坤推出了Genius评级计划。由于前期躺平，压力给到12月，虽然12月交了121个alpha，但总数距离220还是差了三四个，自然无缘Grand Master（当然，就算交够了也不一定能成），只能成为中国大陆8位Master中的一员。

2025Q1，由于Combine改版，12月又交了太多高换手的因子，导致combine直接砍半（从3+变成了1.5左右）。雪上加霜的是VF降到了0.13，开始坐牢。心灰意冷之下，又进入了躺平状态。该赛季共提交RA 58个，SA 62个，刚好达到Master的标准，成为了中国大陆16位Master中的一员。

2025Q2，或许是躺平躺习惯了，又或许是5000美元的季度奖已经差强人意（0.97的VF使得日均BASE超过40美元进一步加强了这种情绪），这个赛季依然得过且过，共提交RA 62个，SA 60个，勉强达到Master的标准，成为了中国大陆70位Master中的一员.

二、经验

Q2的Master对我来说其实殊为不易，最大回测天数断了很多次，加分会议只参加了一次，能够保住Master，归根到底得益于：压per。我Q2基本上只使用了一阶的模板，虽然未能调到对performance最好的状态，但近三个月0.97、0.99、1.00的VF说明这种兼顾Genius和VF的方式是可行的。

三、展望

相信每个顾问都有一个成为Grand Master的梦想，我自然也不例外。摆在我面前的第一座大山便是Combine，我的三个Combine一直稳定在1.5左右，距离Grand Master要求的2还差一些。对此，我已找到解决的办法，等成功后便分享给大家，敬请期待！

（如果以上内容对您有帮助，请点点赞，谢谢~）

**顾问 HP65370 (Rank 93) 的解答与建议**:
感谢大佬的经验分享，我现在开始注重六维开始压per了，不过现在达到master要点30个塔，有必要为了点塔交那种比较差的alpha吗，就比如数据缺失或者turnover高amrgin低的这种影响vluefactor，交了这种alpha总觉得污染了我的池子，但是不交又觉得难以点到30个塔


---
