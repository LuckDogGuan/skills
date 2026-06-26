# 【Community Leader -因子构造 💎 】AI模板+mcp实现模板跨数据集提交alpha经验分享

- **链接**: https://support.worldquantbrain.com【Community Leader -因子构造  】AI模板mcp实现模板跨数据集提交alpha经验分享_37176161580823.md
- **作者**: 顾问 QX52484 (Rank 35)
- **发布时间/热度**: 6个月前, 得票: 64

## 帖子正文

```
ts_mean((vec_count(oth515) - ts_mean(vec_count(oth515), 15)) / ts_mean(vec_count(oth515), 75), 10)
```


> [!NOTE] [图片 OCR 识别内容]
> SIMJaTiO
> Settings
> 1.01
> 7.98%6
> 6b
> 5.33%6
> 7.8390
> 13.359600
> Instrumnt Type
> Reglo
> Lanwage
> Dlay
> Truncaton
> Neutrallatlon
> Pastewrtzato
> NaN Hanllng
> Unlt Handlng
> Max Trade
> EOJib
> TOPI
> Epression
> Crowgine Factors
> Vrr
> Sharpe
> TurNOVe
> T5
> CT
> Oawdown
> Margln
> Long Cont
> Short Cowmt
> 2013
> JJD
> JO:
> DDD
> 077
> 0.005
> 0.-:
> 2014
> J0
> JO;:
> 0.D0
> 000*
> 0.005
> 0.0s
> Clone Alpha
> 2015
> JJD
> JO:
> DDD
> 077
> 0.005
> 0.-:
> 016
> ?
> 1?5
> 7.335
> 一7:
> 2017
> 93:
> -.125
> 1.72:
> N Chart
> Pnl
> 2013
> 733
> SD::
> 0.59
> 1175
> 3.905
> 15-
> 2019
> _
> 3.73
> 0.25
> EE
> 一U
> 6:
> 120
> 2020
> 738
> ?7
> 0.15
> 21
> 5.975
> 5.12:
> CJOK
> 1.75:
> 9汩
> 3.535
> =
> 06/0112021
> ZOJOK
> PIL:
> 2,194.02k
> 202
> 3.63:
> 52
> L005
> 22.41恣
> 2023
> 1158:
> 211
> 0.295
> 5
> OJOK
> Correlation
> Jan_
> Ja715
> Ja716
> Jan 18
> Jan 19
> Jan 20
> Jan 21
> Jen 22
> J3723
> Self Correlation
> MJuirIuir
> Uinirurr
> LlTUI
> Uene
> Cco
> .


模板是通过gemini CLI让alpha探索oth515得出的.

后续改用了iflow.

让iflow理解alpha模板的经济学含义


> [!NOTE] [图片 OCR 识别内容]
> OWork
> OOa2XMWg
> 个alpha表达式有经济学含义吗?
> Ng


结合七十二变的拓展思想 让mcp也进行这样的尝试.寻找类似经济学含义的字段或者同数据集字段.


> [!NOTE] [图片 OCR 识别内容]
> 经济学含义分析:
> 数据字段含义 =
> oth515
> 这是机构交易数据
> 表示过去2年内的证券交易次数
> Vec_countC): 计算向量中非空值的数量。用于处理数据缺失
> 核心逻辑=
> 分子:
> VeC
> CountCoth5le
> ts_mean(vec_countCoth5l5
> 15)
> 当前交易次数与过去15天半巩父殇以4叫左佴
> 衡量交易活跃度的短期异常娈化
> 分母:
> ts_mean(vec_count(oth5l5
> 75)
> 过去75天的平均交易次数
> 作为基准,用于标准化短期娈化
> 完整逻辑 =
> (短期异常变化) /(长期基准水平]:  计算交易活跃度的相对娈化率
> ts_mean(
> 10):  对相对娈化率取10天移动平均,
> 平滑信号
> 经济学解释=
> 这是-
> 个机构交易动量 /反转策略
> 逻辑:  当机构交易活跃度短期显著高于长期平均水平时
> 可能预示着:
> 动量效应:  机构持续买入 /卖出
> 推动价格趋势
> 信息优势=
> 机构可能掌握私有信息。交易活跃度娈化反映信息流
> 流动性需求:  机构大额交易可能影响价格
> 在JPN市场,机构交易数据可能反映:
> 外资流入 /流出
> 国内机构调仓
> 公司治理事件 (如并购
> 重组)
> 策略类型
> 属于行为金融学范畴
> 利用机构投资者的交易行为模式
> 可能捕捉机构资金流动蒂来的价格压力
> plan Updating
> todo list (0 pending
> 0 in
> progress.
> completed)
> Updated
> todo list
> ~获取 alpha OOazXMWg 的详细信息
> V分析 alpha 表达式的经济学含义
> 总结
> 这个
> alpha 表达式有明确的经济学含义
> 它是一个基于机构交易活跃度相对娈化的策略
> 属于行为金融学中的机
> 构交易行为分析。通过比较短期交易活跃度与长期基准水平的相对变化
> 捕捉机构资金流动带来的价格动量或反
> 转效应。在JPN市场中.
> 这种策略可能反映外资流动。
> 国内机构调仓等市场微观结构娈化。
> 按照这个alpha模板
> 替换其中的oth5l!
> 为字段来寻找甚他的alpha


获取的结果


> [!NOTE] [图片 OCR 识别内容]
> plan Updating
> todo list (1 pending;
> 1 in
> progress.
> completed)
> Updated
> todo list
> 获取
> JPN 地区可用的数据字段
> 筛选适合替换的字段
> 生成新的 alpha 表达式
> 口批量测试新 alpha
> 基于分析
> 我筛选出以下适合替换的字段。原模板是机构交易次数相对娈化策略。我将用类似逻辑的字段替换
> 筛选出的字段
> 1.
> 交易活跃度类 (与原字段最相似)
> inst25
> Security_trade
> Count_Iyr
> 过去1年交易次数
> inst25_security_trade
> Count
> 3mo
> 过去3个月交易次数
> inst25
> Security_trade
> count
> IWR
> 过去1周交易次数
> 价格成交量类 (类似经济学含义 )
> Volume
> 日成交量 (交易活跃度代理)
> adV20
> 208平均成交量
> returns
> 日收益率 (价格动量)
> 机构持仓类
> instl4_longnego
> 可协商保证金交易多头持仓
> instl4_shortnego
> 可协商保证金交易空头持仓
> 现在生成新的 alpha 表达式:
> plan Updating
> todo
> list (0 pending;
> 1 In
> Progress
> completed)
> Updated
> todo list
> 获取 JPN 地区可用的数据字段
> 筛选适合替换的字段
> 生成新的 alpha 表达式
> 批量测试新 alpha



> [!NOTE] [图片 OCR 识别内容]
> 成功 !
> 己经成功创建了8个新的alpha模拟。
> 以下是测试结果总结
> 测试结果分析:
> 1。机构交易频率类 (Alpha ID: JjL36Zgm,
> ZrkG3baw
> mLkKEMIK)
> 表现
> Sharpe=0. 98,
> Fitness=0.63, Margin=g. 57bps
> 特点
> 与原alpha表现相似 (原:
> Sharpe=l. 01,
> Fitness=0. 66)
> 金字塔:  匹配JPN/DI/INSTITUTIONS
> (1.4x]
> 问题
> Sharpe未达标
> (<1.58)
> Fitness末达标 (<1.0)
> 价格成交量类 (Alpha
> ID:  OOVGLEbd
> ESAmgXql, QPdwwlnr)
> 表现较差
> Volume
> Sharpe=0. 29
> Margin=z. 97bps
> Advzo:
> Sharpe=-0.10 ,
> Margin=-I.Gbps
> Returns:
> Sharpe=-0. 38 ,
> Margin=-9.07bps
> 问题:  表现负向,不适用该模板
> 3。机构持仓类 (Alpha
> ID: KPRVjnk 最后-个)
> 等待完整结果:  数据还在处理中
> 关键发现:
> 模板有效性:  机构交易频率字段
> (instz5_ *) 表现相对稳定。与原模板相似
> 2。字段适用性
> 价格成交量字段不适用此相对变化率模板
> 金字塔匹配=
> 所有alpha都匹配了相应的金字塔主题
> (INSTITUTIONS或PV)
> 建议下一步:
> 优化方向 =
> 对表现较好的机构交易频率alpha迸行参数优化
> 2。字段扩展
> 尝试其他机构相关字段 (如instz5_activity, instz5_sentiment等)
> 3。模板调整
> 对价格成交量类字段需要不同的处理逻辑
> 最佳候选=
> 前3个机构交易频率alpha (JL36Zg, ZrkG3baw ,
> MLkKEMIK) 有优化潜力, Sharpe接近1.0,
> Marginsgbps。
> 添加操作符忧化这些表现较好的alpha
> 我来为表现较好的机构交易频率alpha添加操作符进行优化。基于原模板和测试结果_
> 我将添加标准化
> 中性
> 化等操作符来提升表现。
> plan Updating
> todo list (2 pending;
> 1 In
> progress,
> 0 completed)
> Updated
> todo list
> 设计优化操作符方案
> 生成优化后的alpha表达式
> 测试优化后的alpha


这样就实现了从oth515到inst25的拓展.  由于本身alpha模板也比较简单,导致了ppc比较高.

那怎么受得了,进行下一轮优化.


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_mean( (Vec_Count instzr
> tS_Nean VeC
> count(instz
> 15) )
> ts_mean(VeC_Count instzs
> Data SEtJphs
> ABaregate Data
> SIATLI
> SIIUIatIOn
> Settings
> 1.02
> 9.0596
> 65
> 5.109
> 8.7890
> 11.279600
> Istrut Type
> Regl
> Uelse
> 7034101
> IIa
> Olay
> Truncatlon
> Neutrallatlon
> Pastewrtato
> HaN Hanlng
> UnltHandlng
> Max Trate
> EaJi?
> TOPIE
> Fast Spressizn
> Crowwire Factors
> TT
> Year
> Sharpe
> TurOVeT
> Fltss
> Rtur
> Uawdown
> Marln
> Long Cnt
> Short Cot
> 2013
> JJ0
> J00:
> 7
> 0.005
> 0.0s
> 201-
> DJD
> J0:
> 7775
> 0.005
> 0.7-7:
> Clone Alpha
> 2015
> J00:
> 7
> 0.005
> 0.7:
> 2015
> 775
> 35::
> 427
> 5.515
> 85
> 2017
> 1.75
> 58:
> -
> -.9-5
> 47:
> T
> N Chart
> Pnl
> 2013
> 0
> 1.36:
> 374
> 3.505
> 10.1:
> 2019
> 753
> 3.76:
> 2
> 3.75
> 5:
> 119
> 2020
> 008
> 36:
> 4:
> 8.735
> -0.5:
> 2021
> 31:
> &3泸
> -.335
> 1
> ZOJOK
> 3E 15,2520
> 2022
> -9::
> 371
> -055
> 4:
> Pnl: 1.817.70K
> 2023
> 010
> 08:
> 0.02
> 74
> 0.525
> 0.52:
> DJOK
> 医 Correlation
> Jan 16
> Jan 13
> Jan 19
> Jan 20
> Jar 21
> Jn 2
> Jan 23
> Self Correlation
> TIATTIUITTI
> STITUCT
> L1| YUII
> PoVel
> COrrelatlon
> TIATTIUITT
> STITUCT
> Losl Ru; Sun122112025.11.09
> 0.8221
> -0.1147
> o IS Testing Status
> Ferrg
> Prod Correlation
> TIATTIUITTI
> STITUCT
> Losl Ru; Sun122112025.11.09
> 0.4427
> -0.2508
> 7PASS
> 3WARNING
> Snsle



> [!NOTE] [图片 OCR 识别内容]
> MPAgJVer 且前这个alpha和我的自相关性太高了  使用group 调整中性化尝试  加强alpha的表现
> 降低它的相关性



> [!NOTE] [图片 OCR 识别内容]
> 基于 RRLSRQOo的发现继续优化
> 总结一下优化结果:
> 最佳alpha:
> RRLSRQoo
> Sharpe:
> 1.28 (从1.19提升]
> Fitness
> 0.88
> Margin:
> 10.G4bps
> Turnover
> 0.1113
> 表达式
> ts_Zscore(ts
> mean( (vec_count(ins
> ts_mean(vec
> count(ins
> 15))
> ts_mean(vec
> count(ins
> 75),10), 132)
> 关键优化发现:
> ts_Zscore窗口调整:  从66天改为132天
> Sharpe从 1.19提升到1.28
> 2。配置优化:  使用CROWDING中性化
> nan
> handling=ON
> Nax
> trade-ON
> 3。时间窗廿组合:  0OVROrQY通过组合不同时间窗廿(15/75和30/150)达到Sharpe=l. 26
> 经济学含义=
> 这是一个机构交易活跃度相对娈化策略
> 通过比较短期(15天)  和长期(75天) 的机构交易频率娈化。识别机
> 构交易行为的异常娈化,然后进行132天的时间序列标准化。
> 虽然SharpeK 0.98提升到了1.28,但仍未达到提交标准 (Sharpe>l. 58)
> 需要进一步优化才能达到可提交水
> 平
> 继续忧化_直到sharpel.58
> fitness
> 也可尝试调整day的窗


因为操作符总数＞8,无法再按PPA提交了.这里看AI有些陷入局部最优解了,人工介入调整了下参数做到RA.


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 12202025 EST
> anonymOUs
> Mdd Nphato a Lst
> Code
> IS Summary
> PErIoU
> ts_ZSCOrE(ts_mean
> (VeC_count(ins
> ts_Oean(VeC_Count(in
> tS_mean VeC_CoUn
> IIEI: SCalable
> ATOMTheme
> Data SEtJIpha
> 酡 Resular Alpha
> Pramio heme JPNIDTIINSTITUTIONS ^ _
> ABaregate Data
> IITTL
> [4
> Simulation Settings
> 1.60
> 9.739
> 1.18
> 89
> 6.6990
> 13.93900
> Tnstuwt Type
> Reglo
> Werse
> Unwae
> Ia
> Olay
> Truncatlon
> Neutallatlon
> Pastewrtat
> NaNHanl
> Unlt Handlng
> Max Trade
> EaJi?
> TOPIEJ
> FastSPressian
> 7.01
> CTo'NUIne TtoTs
> 「T
> Year
> Sharpe
> TurNOVeT
> Foess
> Rus
> Cawdow
> Maryln
> Long Cnt
> Short Cot
> 2013
> J0
> J.00:
> 0.O0
> 037
> 0.005
> 0.0s
> 014
> JJ0
> JO:
> D.D0
> 077
> 0.005
> 0.01:
> Clone Alpha
> 2015
> J0
> JO;:
> 0.O0
> 037
> 0.005
> 0.0s
> 2016
> 759
> 11.3:
> 0.29
> 3053
> 5.935
> 3:
> 2017
> 223
> 08:
> ?;
> _.59
> 1
> N Chart
> Pnl
> 2013
> JS0
> 1.61:
> 5
> 6.695
> 6.715:
> 17
> 119
> 1
> 3.18:
> 三7
> 2.20
> 5:
> 2020
> 1.13
> 36:
> 45拓
> 2.075
> 10.2:
> 2021
> 3
> 1.-5:
> 3.93
> 147
> 1.175
> & :
> 2022
> 99::
> 1.03
> 5123
> 3.205
> 1.2:
> CJOK
> 2023
> 152
> 09:
> 1-.73
> 2435
> 0.105
> 52.57:
> 13
> 匿 Correlation
> Jan15
> Jan 16
> Jan i
> Jar 18
> Jan 19
> Jan 20
> Jan 21
> J2
> J3*23
> Self Correlation
> TATTIUITT
> TA
> 11| YUIII
> Prod Correlation
> TATTIUITT
> T
> PIII:CUI
> 12/21/202,1213PN
> 0.4539
> 0.1779
> 10OK
> 小 OS Testing Status
> Period
> TOK
> 11PENDING
> 
> 100
> SITele


再进行下一轮


> [!NOTE] [图片 OCR 识别内容]
> plan Updating
> todo list (2 pending
> m
> Progress.
> completed)
> Updated
> todo list
> ~获取 alpha ESANIAnR 的详细信息
> 查找 instzs 数据集的其他字段
> 口查找经济学含义类似的字段
> 0生成替换字段的
> alpha 娈体
> 测试优化结果
> :I've
> Seen
> things you people
> Wouldn 't believe
> like
> USEI
> Who
> reads
> Cesc
> Canceli
> I
> loading messages
> 515)
> Loaded:
> MCP
> server Cctrltt
> to
> Thinking:Off (tab
> to
> YOLO mode (shift
> tab
> alt
> 皿 to
> View)
> toggle)
> toggle)
> ESANIAnR
> 根据这个alpha
> 调整其中的inst2
> 字段为经济学含义类似的字段或者同为inst25
> 数据集的字段  来寻找atpna


---

## 讨论与评论 (5)

### 评论 #1 (作者: LG87838, 时间: 6个月前)

就喜欢看这样的实操，手把手的教啊，感谢大佬的分享。

先围绕字段做，再配合operators，省得AI胡编乱造。

------------------------------------------------------------------------------------------------------------------------------------

慢慢来，相信时间的力量

------------------------------------------------------------------------------------------------------------------------------------

---

### 评论 #2 (作者: YQ84572, 时间: 6个月前)

很不错的模板分享，感觉可以试试，相关性应该很低
====================================================================================
祝大佬base多多，vf0.9+
====================================================================================

---

### 评论 #3 (作者: FF65210, 时间: 6个月前)

感谢大佬的思路分享，我感觉能找到更多的alpha了，不用担心断粮了。

---

### 评论 #4 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

很不错的分享，vec_count 这个操作符用的比较少

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #5 (作者: AK76468, 时间: 5个月前)

====================================================================================

Ai还真是能想到一下独特的东西，虽然很多时候不好用，但还是能拓宽视野、丰富idea呀

====================================================================================

---

