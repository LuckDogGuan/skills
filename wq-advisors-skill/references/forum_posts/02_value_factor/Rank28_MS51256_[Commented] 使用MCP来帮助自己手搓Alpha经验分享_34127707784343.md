# 使用MCP来帮助自己手搓Alpha经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 使用MCP来帮助自己手搓Alpha经验分享_34127707784343.md
- **作者**: JB71859
- **发布时间/热度**: 10 months ago, 得票: 75

## 帖子正文

最近在会议上听老师讲了MCP工具，会后立马搭了个"实习生"玩玩。虽然换成Claude4.1烧钱烧得心疼，但想着贵有贵的道理，就咬牙上了。最近在搞ASI的alpha，感觉自己用的数据集都快被榨干了，就让"实习生"帮我梳理一下还有哪些数据没碰过。它提到了EARNINGS里的ern3_pre_interval字段，我之前确实没怎么关注过这个。

拿到这个字段后，凭直觉先做了个ts_mean操作，发现效果还行，有搞头。然后开始各种折腾，最后按我的想法组合出来：

**ts_delta(quantile(ts_mean(ern3_pre_interval, 252)), 50)**

**
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> iot
> Data SE: Nphs
> AEaregate Data
> Shar
> TNCRC
> insc
> eTIITT
> TCan
> Warain
> 0.45
> 8.839
> 0.13
> 1.0496
> 6.41%
> 2.359600
> Year
> Shalp
> Turover
> Foess
> ReWIIs
> Drawow
> Nagl
> Long Cunt
> Short Cot
> 01
> 7.16
> 4:
> 0.03
> -1.33:
> 77
> 3
> 1
> 11
> 204
> 4:
> .S8
> 2.73:
> -3:
> O
> 117
> 2OS
> 3.11:
> Z.5:
> -
> JSIN;
> 1E35
> ZE
> 1.53
> ::
> 3:
> 3
> 12
> TE2
> 20
> 3.
> 2.51:
> 114
> 33
> 157_
> 1SES
> 20
> 0.23
> 3:
> 7.43::
> 222沾
> 0
> 1375
> 171
> 2019
> 3:
> 3:
> 115
> ECRO?
> 1715
> ES4
> 2020
> 0.57
> 3.J5:
> 23:
> 250治
> 22o
> 1773
> 1771
> 2021
> ~7.15
> 3.5:
> 1.12
> 0.329
> 3.315
> T;:
> 225
> 225
> 2
> 0.23
> 3.55
> 0.s:
> 2715
> 3
> 2152
> 2085
> 023
> 1.-1:
> 33:
> 32
> T
> 13
> SRSIE
**

结果一跑尴尬了，表现有点拉跨，而且margin有点低。

把这个悲惨的结果告诉"实习生"，等了老半天（Claude4.1虽然聪明但真的慢啊），它给了我一个用 **ts_av_diff** 的表达式。整体效果没有得到提升，虽然差了一些但Prod_corr是0.3624，我觉得很不错了。
改进后的表达式：
 **ts_av_diff(quantile(ts_mean(ern3_pre_interval, 5)), 60)** 
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> YEVICCI
> 昵 Sirele Data Se: Nlphs
> ABaregate
> Lata
> TUPN?
> TII2
> YeTUTn
> TaJoVT
> Warain
> 1.1
> 7.7290
> 0.62
> 3.51%
> 96%
> 9.109000
> Sharpe
> TuMOeT
> C
> Retuns
> Orawdown
> Varqln
> Long
> Short Cowmt
> 201
> 17
> 7.759
> 1.15
> 5.43:
> 1.E5
> 14.1E5:
> 103
> 1015
> 3014
> ~JE
> :
> -0.05
> -1.73:
> 三55
> -2.088:
> 111
> 1135
> ZOs
> 7.5:
> 7
> 123
> .1:
> 1OE
> OE
> 1.7
> 5.33:
> 2.473
> 4.055
> 1021
> 20
> 2.5:
> 4.36:
> 1.43
> 10.82?
> 1071
> 11u
> 01
> 3:
> :
> 3.73
> 5〉:
> C
> 1037
> 2019
> 7.26:
> 3.14
> 57
> EEf:
> 15
> 1
> 20
> 17
> .75:
> 5.329:
> 12
> 3.73:;
> 141
> 21
> 7
> J.EE:
> Z.ZE:
> 243
> 5.918?
> TTE
> TE7
> 2
> 51
> DS
> .27:
> 2.43
> _
> 173
> JE?
> 2022
> 7
> &.70%
> 223
> 2:
> 0.35%
> 1.55:
> 135
> 1025
> Risk neutralized
> Jar
> Cowt



> [!NOTE] [图片 OCR 识别内容]
> Settlngs
> A5I/DTTMINVOLTN
> Convertto Multl-SIulatlon
> 2
> 7.51:
> 5.2:
> 2.43
> 1:
> 173
> 023
> 7
> &.7:
> 223
> .2
> 3
> 18.57d
> 135
> 12
> Streak: 42
> ts_ay_diff(quantile(ts_mean(ern3_next_intervaly 252))
> 6)
> Risk neutralized
> AEaregate Data
> Sharpe
> Turno
> SiTn
> Re-urns
> CaTIIC
> Marein
> 92
> 7.72%
> 0.37
> 2.0790
> 5.35%
> 5.379600
> 医 Correlation
> Self Correlation
> Wawmur
> Ninimum
> L VF
> Pn'e
> Corrlatial
> TTTTC
> NlinimUT
> Run: Tue。 03/12/202511.3DM
> ].6851
> 0.0675
> 名宇
> Unherse
> Corelation
> Sharpe
> Petm
> T
> Fitwess
> Mareln
> anonymous (current]
> MINVOLTNI
> 10000
> 1.17
> 3510
> 7.72%
> 0.62
> 9.109
> SOpyTVS
> MINNOLIN
> g'
> 11
> 1
> 三
> 0.43
> E.119
> SOnmUUS
> NNVO_TN
> 0.2125
> 1.31
> J`
> E.17
> 0.73
> 241C0?
> SOpyTVS
> MNNO_TN
> 0.1325
> 1.2
> 一2
> E.E3
> DE
> 1.379
> SONITTOVS
> NNNO_TN
> 0.15-
> 11
> 7 8 沿
> Z51
> 0.53
> SEI
> aOnTUS
> NNVO_TN
> 0.1511
> 1-2
> 2.705
> C.SS
> CEs
> 匕_
> Prod Correlation
> WaIUN
> TIITUNI
> L35t Run: Tue。 03/122025,11.35 DM
> 0.3624
> 0.3582
> 1OON
> day


虽然prod很低，但我觉得margin还是有点低了，最后又询问了一下“实习生”让我使用 **ts_count_nans，** 加入到表达式后整体表现果然得到了提升。

最终的表达式：
 **-ts_count_nans(quantile(ts_mean(ern3_pre_interval, 5)), 5)** 
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> YEVICCI
> Data SE: Alphs
> ABaregate
> Lata
> SIaTCE
> LUTNO
> 12n255
> REUPT
> Uray'gUI
> Marain
> 1.41
> 5.1196
> 0.75
> 3.5696
> 2.5596
> 13.969600
> Sharpe
> TuMOeT
> Ftess
> Retus
> Orawdown
> Varqln
> Long Cont
> Short Cowmt
> 201
> ~3.15
> OO
> 1.3
> 1E_
> +1.518:。
> TE
> 1031
> 2014
> 33
> 4.9
> 3.25
> 2.55:
> 1,43
> 3.265:
> _ =
> ZOs
> 35
> J三:
> 0.13
> 1.51:
> 2.473
> 7.13:
> 1SE2
> 3336
> ZOE
> 25
> 4.1:
> 1.75
> 5.33:
> 1
> 27.848:?
> 131
> 1235
> 2
> 32
> 17
> E.13:
> 1.23
> 26.378?
> 1297
> 1
> 3.32
> 1.43:
> 0.35
> 2.029:
> 5
> 2::
> 7
> 433
> 2019
> 5:
> 0.1-
> 1.1
> ES
> 3.71*;
> 22
> 11
> 20
> 17
> S:
> 5.17:
> ES
> .44:;
> 2145
> 431
> 21
> 5.45:
> 0.13
> .369:
> 1.22
> 0;;:
> ZE1
> TTE
> 2
> 1.2
> Ce
> 5:
> 1.
> 16115:
> 2427
> 1753
> 2022
> 13
> 二
> 11.31
> 0.15
> E::
> 212
> 1510
> SnS
> Jar
 
还算可以，但总觉得差点意思。后来试着把NEUTRALIZATION改成Statistical，效果立马上了一个台阶。

整个过程下来，感觉AI助手确实能帮助发现一些盲点，但最终的调优还是得靠自己的经验和直觉。整个过程中模型的能力我觉得是重中之重，如果我没有选择使用Claude4.1我觉得也不会整出这个alpha。

---

## 讨论与评论 (4)

### 评论 #1 (作者: TL53163, 时间: 10 months ago)

大佬动手能力真强，预感未来MCP会给我们带来巨大的帮助

---

### 评论 #2 (作者: BW14163, 时间: 10 months ago)

感谢大佬分享，用的api是deepseek，目前是问一条，需要点一个接受，感觉还需要继续学习大佬的经验

---

### 评论 #3 (作者: WL13229, 时间: 10 months ago)

**ts_count_nans 确实没想到**

---

### 评论 #4 (作者: 顾问 MS51256 (Rank 28), 时间: 9 months ago)

贵有贵的道理 claude 4.1还是蛮牛的

感谢JB哥的分享，好久没使用mcp了，感觉像是乌克兰放弃了核武器一样是个愚蠢的决定，我打算重新启用了，不然下个季度难搞了

====================================================================================================================================================================

---

