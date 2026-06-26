# 【Community Leader -因子构造 】ai推荐比率按照实际含义推荐operator经验分享

- **链接**: [Commented] 【Community Leader -因子构造 】ai推荐比率按照实际含义推荐operator经验分享.md
- **作者**: XG43628
- **发布时间/热度**: 6个月前, 得票: 70

## 帖子正文

其实这是之前的思路，不过那会还可以通过大规模回测来找到alpha，现在限制回测之后才对改工作流进行了一定的修改，通过昨天kuiqi老师说的，我的想法其实就是来自最早开始kunqi老师讲的比率，只是这是通过ai去做数据集分析，数据字段分析以及数据类型介绍和对于的paper来做比率，完成比率生成之后，让ai按照比率的实际意义去做operator推荐。

下面是工作流内容：

```
# Alpha 生成工作流本工作流旨在通过探索 WorldQuant BRAIN 平台上的数据集，系统地生成具有经济意义的 Alpha 表达式。## 步骤 1: 认证在开始任何操作之前，必须先通过 BRAIN 平台认证。```<use_mcp_tool>  <server_name>worldquant-brain-platform</server_name>  <tool_name>authenticate</tool_name>  <arguments>    {}  </arguments></use_mcp_tool>```## 步骤 2: 获取数据字段确定目标市场和数据集，然后获取所有可用的数据字段。**参数:***   `region`: 目标区域 (例如, `ASI`, `USA`, `EUR`, `GLB`)*   `universe`: 目标股票池 (例如, `TOP3000`, `MINVOL1M`)*   `dataset_id`: 目标数据集 (例如, `other466`, `fundamental31`, `analyst15`)**示例:**```<use_mcp_tool>  <server_name>worldquant-brain-platform</server_name>  <tool_name>get_datafields</tool_name>  <arguments>    {      "region": "ASI",      "universe": "MINVOL1M",      "dataset_id": "other466"    }  </arguments></use_mcp_tool>```## 步骤 3: 分析与生成 Alpha 表达式仔细阅读获取到的数据字段描述，理解其经济含义，并遵循以下策略生成 Alpha 表达式：*   **避开常规组合**: 专注于发现非传统的、但具有强大经济逻辑的组合。*   **字段数量**: 严格使用两个字段或三个字段进行组合。*   **数据类型处理**: 如果字段是 `VECTOR` 类型，在进行算术运算前使用 vec_类型 等聚合函数，并在生成组合时请考虑用vec_类型操作符的实际经济学含义；例如：计算当天事件数量： vec_sum(datafiled)/vec_avg(datafield). 感觉蛮有用的，如果是新闻数据可以用来看当天热度。*   **算术运算**: 仅使用 `+`, `-`, `*`, `/`。*   **排除项**: 不使用 `group` 类型 `operator`、`if_else` 和 `trade_when`。**生成策略示例并按照策略生成20个组合 (基于数据集描述以及数据字段描述并且尽量多样化):**## 步骤 4: 根据生成组合的实际含义套用operator，从operator.json中获取有关operator的详细信息*   **使用operator有实际含义**: 要有实际经济学含义或者数学含义。*   **使用规范**: 严格按照operator.json中的operator语法使用operator，注意：请勿对ts_套用超过3层，group_套用超过两层**按照生成的20个组合套用operator演变出100个表达式**## 步骤 5: 保存并检查将生成的 Alpha 表达式保存到 JSON 文件中，并仔细检查以确保所有使用的字段都来自指定的数据集。## 知识库目录Resources里面按照region_decay_universe_dataset的文件名，每个文件包含对应数据集的介绍，和Research Paper。**示例:**```<write_to_file>  <path>eur_anl4__alphas_combinations.json</path>  <content>  ["group_neutralize(zscore(ts_zscore(anl4_afv4_eps_mean + anl4_afv4_cfps_mean, 22)),(market))"]
```

以下是通过该工作流生成的一些alpha表现：


> [!NOTE] [图片 OCR 识别内容]
> 毗 Rszular Alpha
> Pyramid theme: USAIDIIRISK :1.2
> Fyramig
> T=
> USAIDIIOTHER *.3
> AEgregate Data
> SIaUe
> TUINI
> TUIe
> Cu
> LUTir
> Simulation Settings
> 1.58
> 10.12%
> 1.84
> 16.899
> 17.2995
> 33.399200
> IntrumenT
> Reglon
> Unierse
> Uarguag
> Gecy
> Ulay
> Trumcabo
> Mempliaton
> Rselriaboq
> NaN Handling
> Uat Handling
> NaxTrer
> CUu
> TUIJCJI
> Fasl Culeysiul
> UuUr FaLluls
> Ver i '
> Tunwer
> C
> Relr
> Uad
> Lor Cunt
> 1O
> U1
> 1114
> 0
> ZOI
> 954
> TOC
> 5.93乩
> 5771
> Clone Alpha
> 95
> 6.714
> 17.29;
> 3[
> 1
> 19
> 754
> 11274
> 1O.
> T59
> T5
> Chart
> 2013
> 1d
> 3,164
> 3314
> UTT
> 2790
> 154
> J5.9
> T3S
> 571
> LU
> 1TC
> 1
> TTU
> 4344
> 1956
> J35
> 759
> 2391
> N
> 1u
> 4,94
> 4Jt
> 9
> 1.524
> 1.-0
>  |555
> 5TIIL
> Investability constrained
> AEgregate Data
> CAIc
> TUIC
> Fuies
> ReluIrI
> CreUL
> 55
> 6.6
> 1.35
> 9.4095
> 7.53%
> 28.46900
> Jul 1
> Jul'1-
> Jn 15
> Jul (5
> Jul 16
> Jul"17
> Jan(
> Jul'13
> Ju"1g
> J '20
> Ju'20
> JUl 21
> Jan 2
> Jul72
> J 2
> 医 Correlation
> Self Correlation
> Mariruir
> LITiIJrT
> LuRu
> OS Testing Status
> Period
> 0121
> JOOILOrrelatlon
> Mariruir
> LIimrr
> Run Fr 1219/2025
> 3.27F
> .4202
> 0.0944
> I1PENDING
> Lorrelatlon
> Mariruir
> LIimrr
> LslRun Fr 1219/2025
> 3.26 F
> 0.5955
> 0.5501
> 10ON
> Sro
> Myn
> Ja
> Jns
> J T
> Jar
> 15121
  
> [!NOTE] [图片 OCR 识别内容]
> 酡 Sirele Data Set Apna
> 酡 Resu arApkz
> FyramiyeM=: USNDIINACRO*1
> AEgregate Data
> SMulre
> TUIe
> OIgUUIT
> Maleir
> SimMatiOn
> Settings
> 1.58
> 5.5696
> 2.01
> 20.3396
> 17.8196
> 73.
> 19623
> IntumenT
> Reoo
> Untere
> Uanguag
> Decay
> Uely
> Truncabo
> Memliaton
> Pastedrtabon
> NaN Handling
> Ut Handling
> Iax Tra
> CUun
> TUJLTI
> FJsl Culeysiull
> TrUUI FJLLUI
> Ver f
> Sme
> Tunover
> Fnees
> Rehrr
> Odon
> Log Colit
> 5354
> 1TO
> 7324
> 5.26〉
> 5 IU
> 5[
> 106
> 3.103〉
> Clone Alpha
> 00
> 5204
> UzGy
> 95GCU
> O[?
> 2015
> 5
> 955
> 10359
> 945
> TJU
> 2.329
> TSC
> O
> Chart
> 2013
> 3旧
> 17.549
> 4.10s
> GSC?
> 5.5S
> J6.249
> GP
> 1E?
> L3u
> |
> 145C
> 7.64
> 5.26弘
> 34.029
> 13.754
> 10-
> 27
> 5154
> 594
> TIC
> 221.725
> TON
> TJ
> 19.5
> 1.194
> 116GC
> SOOOR
> Investability constrained
> 4831283TE
> 0at3
> TAI
> TUIIU
> Fitriey
> ReluTiy
> UIrJlJUIT
> 1.34
> 4.61%
> 1.49
> 15.5496
> 15.52%
> 67.51900
> Jul1
> Jar "
> Jul'14
> Jn 1s
> Jul
> Jan 16
> Jul 16
> Jn 17
> Ju"17
> Jan 13
> Jul'13
> Ju'19
> J '20
> Ju20
> J37"21
> Jul 21
> Jan 2
> Jul 22
> Jn 2
> Correlation
> SeITLOTTEIaTIOO
> Matirruiri
> LIiIrT
> LFu
> OS Testing Status
> Period
> VOe
> LOOILOrrelatlon
> Mlatiruir
> LIiIJrT
> Lust Run
> I1PENDING
> Prod Correlation
> Mariruiri
> LrimJrri
> Lusl Rur: Fri; 12/192025
> 0.6714
> 0.6374
> 10ON
> AIphas
> 1S0
> Mangn
> Ja=
  
> [!NOTE] [图片 OCR 识别内容]
> #Per Pool Aphs
> # Resusr Lphs
> FyrmiJtems USADIINACRO .11
> Fyramidem= USADIIOTHER  .
> ABBregatE
> Uata
> SApr
> TUITIII
> Cm
> UTr
> SIIIUIatIOI
> Settings
> 1.65
> 22.13%
> 1.57
> 22.68%
> 14.019
> 20.5093o0
> InslrumerTe
> Reoo
> Untete
> UIa
> Decay
> T
> Neualtalon
> Paselriobon
> NaN Handling
> Uut Handling
> Max Trade
> LUU
> 70?3030
> Crpressiun
> Cruwdrg Fatlors
> Sharpe
> Tunoer
> Fuess
> Tr
> Uro
> Manga
> Long Count
> 20IJ
> 7.324
> 0.67
> 14.114
> 11.3北
> 7154
> 75.174
> 21.7E9
> 1.51北
> 7
> 74564
> 19GCN
> _n
> 161U
> Clone Alpha 
> 16g
> 21.714
> G2T
> -57
> 71.7014
> 1
> 5594
> 165k
> Chart
> 22.94
> 1,T0
> T
> 53
> 7139
> 7170
> TO
> 30
> 224:
> 19.964
> 0.65
> 1.SC
> 1.094
> 151
> 2041
> 74.33
> 46.179
> 5514
> 373
> 7102
> 19114
> 2.26
> 9.9
> T41
> TON
> 1554
> 7.64
> 25.554
> 1
> 2173
> OOOr
> Investability constrained
> AEgregate Data
> 31+1
> OO A TO
> N'y
> 0.55
> 12.02%6
> 0.34
> 4.88%
> 16.66%
> 290
> Jult
> lan
> Jn 1s
> Juli
> Jan ts
> Jul 16
> JEn 1
> Jan
> JUI /
> Jan
> Ju'1g
> 139 UI
> J0
> J'21
> Jul 21
> Jn  
> Jul-
> Jn 卫
> Correlation
> Self Correlation
> TIATTTITT
> T
> OS Testing Status
> Period
> Dne
> Correlation
> TIAITTITT
> T
> 11PENDING
> Prod Correlation
> TIAITTITT
> T
> 174+920T
> SJ0P
> 0.6332
> 0.6739
> 10ON
> 兽
> 101
> Ca
> Vrs
> 0
> Ju_
> JU
  
> [!NOTE] [图片 OCR 识别内容]
> Code
> I IS
> Summary
> =TOI
> 酡 Reguldr Nplz
> KaIIULII
> INDN
> TATTCLLTTTIL
> CUOMTST
> LLUTULJtU LJt
> ShaR
> [-51
> Mrlr
> 1.97
> 8.2993
> 1.14
> 4.205
> 4,0435
> 4930
> Shm
> TT
> T
> Kt
> Umo
> M
> IoCmrt
> Shot Count
> Simulation Settings
> OC
> 0
> U00
>  :
> I-hmt
> FemO
> U
> Ut
> Dco
> C
>  
> mh
> --
> IHm
> Ul
> N 
> 1
> 1.70
>  :
> ECUIR
> WI'SLIII
> TuErCTslOT
> L
> 一 |
> :
> 二75
> T9
> T =:
> 6455
> Ug0
> 15:
> Clone Nlpha
> U
> -447
> :
> !
> :
> Chart
> 32
> +34=
> :
> Su
> 1.0
> 25
> 1T:
> 53
> 24 45:
> 20JU
> AMER
> LLUTULJtU LJt
> [sU
> 1,0JOk
> 1.17
> 4.0591
> 923
> 3,3435
> 279630
> APAC
> I
> Hri '1
> Jun '15
> Il'
> JuI I
> JUI IE
> 1'
> 1TI '13
> Jul'1
> A
> Jn 20
> Jl'I
> 1'1
> Jul'z1
> Jul'
> TI '
> LLUTULJtU LJt
> CCJri
> LIrIr
> +39
> 2.7093
> +3435
> 363
> 9.929t30
> EMEL
> LLUTULJtU LJt
> ShTCC
> UITTTNIn
> 47
> 1,5545
> 0,41
> 0.959
> 1.2493
> 12.289630
> OS Testing Status
> Perin 
> Investabillity Constrained
> LLUTULJtU LJt
> ShTCO
> OTIn
> Wnlr
> 1.53
> 6,7145
> 0,94
> 4.153
> 5.2093
> 12.209630
> I1PENDINC
> 座 Correlation
> SUIT CorrelJion
> NmUm
> UTITTUI
> oOTon
> TMNT
> CmmN
> SIT - F
> 17119217
> 
> 0.5978
> -0.3238
> 44111
> Ju 1
> 川 I
> Nl I
> Jn 2


然后通过这些alpha再去缘分一道桥，在同一个region self corr跟prod corr会比较高但是其他region能出基本上都是可以交的regular alpha，差一些的也可以通过ai优化流程去优化一下，基本上也可以交成regular alpha，实在是不行的就尽量交成1个waring的ppa也不错。

如果贴子给大家带来一些帮助，请大家给我点点赞！

---

## 讨论与评论 (17)

### 评论 #1 (作者: WF69827, 时间: 6个月前)

这个有点意思，感谢分享

---

### 评论 #2 (作者: 顾问 LW67640 (Rank 24), 时间: 6个月前)

感谢分享，最早课代表发过一个帖子，让豆包做比率，一年后又进化了，比率这个方向挺好的，使用范围广。而且有时候可以点两个塔，pnl曲线也不错。

----------------------------------------------------------------------------------

回归本质，做简单的事，比如：让AI做比率

----------------------------------------------------------------------------------

---

### 评论 #3 (作者: LG87838, 时间: 6个月前)

比率， if_else,  这是目前我的mcp给出的最靠谱的表达式模板。

感谢分享。

-----------------------------------------------------------------------------------

慢慢来，相信时间的力量。

-----------------------------------------------------------------------------------

---

### 评论 #4 (作者: MY82844, 时间: 6个月前)

赞，产生的一般直接就能过那些提交的check吗，还是需要手动进一步调整下？

---

### 评论 #5 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

是不是可以先用代码穷举生成所有的比例，然后再用AI去判断是否有经济学含义呢

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #6 (作者: 顾问 NL80893 (Rank 16), 时间: 6个月前)

明白了，看来我的工程还得调，是不是不同的数据集特性也不一样，我感觉我做的比率成功率不是特别高。

====================================================================================
祝大佬base多多，vf高高，分享更多小妙招～～
====================================================================================

---

### 评论 #7 (作者: MY49971, 时间: 6个月前)

和不错的分享，比例数据确实好出信号

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #8 (作者: YQ84572, 时间: 6个月前)

有点东西的，比率的做法确实需要更多的协调我在做比率的时候感觉效果都不是很好，看来还得优化
====================================================================================
祝大佬base多多，vf0.9+
====================================================================================

---

### 评论 #9 (作者: YZ54944, 时间: 6个月前)

第三步第四步是这个思路的精华，谢谢大佬的分享

==================================================================================

学习一小步，收益一大步

==================================================================================

---

### 评论 #10 (作者: XC66172, 时间: 6个月前)

谢谢楼主分享，看到楼主提交的因子质量和PC都很不错。看来比率是一个可以进一步研究的课题！！

===================================

FIGHTING LABUBU!~

===================================

---

### 评论 #11 (作者: 顾问 WX84677 (Rank 69), 时间: 6个月前)

我也在尝试往这个方向努力，由 AI 先对数据集进行分析并输出有经济学意义的 “两两字段组合”，并推荐与之匹配的因子策略。然后再基于此去构造 alpha 表达式。

还在摸索中，感谢分享给予灵感！

============================ 积跬步，至千里 =============================

---

### 评论 #12 (作者: WW15616, 时间: 6个月前)

学习到了，比我人脑做的效果好多了，感谢分享。

---

### 评论 #13 (作者: 顾问 MZ45384 (Rank 51), 时间: 6个月前)

厉害了，全都是RA，几个月看到一个大佬的帖子也是使用的加减乘除，不过感觉你这个更广泛，收藏了。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #14 (作者: XG98059, 时间: 5个月前)

这种不会有混信号的可能吗？

---

### 评论 #15 (作者: AK76468, 时间: 5个月前)

====================================================================================

我最近也是这样做比率的，或者构建一个独特的字段组合，确实有一些没被人发现的信号。但是往往这类因子需要依赖比较结构化的数据集、数据字段间要存在关联，这样的数据AI就能很好的发挥作用，然后把生成的字段组合放入123阶去探索就行，由于生成的组合一般不会很多，所有限流的情况下确实也够挖掘一次的了。

====================================================================================

---

### 评论 #16 (作者: XW23690, 时间: 5个月前)

我也是采用类似的想法。比率组合生成有经济意义的0阶模板，或者采用if_else、trade_when，AI对于这种情况的处理还是很可以的，至少有逻辑，经济意义上也解释得通。唯一缺点就是平均的OP以及field会上升，不利于六维比拼。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #17 (作者: HW93328, 时间: 5个月前)

============================HW93328============================

比率数据从单个字段的含义提示到了双字段组合的经济含义，相当于1维空间提示到了2维空间，是搜索空间维度的提示，这其中可能探索的顾问数量比较少，是一个值得探索的蓝海，借助ai会变得更加容易，继续学习！

============================HW93328============================

---

