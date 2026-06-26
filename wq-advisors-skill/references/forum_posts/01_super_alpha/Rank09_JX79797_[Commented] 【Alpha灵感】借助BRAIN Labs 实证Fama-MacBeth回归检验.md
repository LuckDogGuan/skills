# 【Alpha灵感】借助BRAIN Labs 实证Fama-MacBeth回归检验

- **链接**: [Commented] 【Alpha灵感】借助BRAIN Labs 实证Fama-MacBeth回归检验.md
- **作者**: LR93609
- **发布时间/热度**: 9个月前, 得票: 93

## 帖子正文

**一、概述**

1.  **什么是Fama-MacBeth 两步回归？** 部分借助Kimi大模型（节省查文献的时间）

****一句话理解：**** 先每天与returns进行横截面回归，再对系数做 t 检验——看因子对未来收益的预测能力是否显著。

**类比一句话：** 就像你每天做一次  **“考试”** （与returns进行横截面回归），然后看  **平均分** （mean_beta）和  **标准差** （std_error），最后算  **p 值** （t_value）——判断这个因子是不是  **“真学霸”**  还是  **“蒙的”** 。

**总结一句话：** 回归检验框架 = 用“统计铁锤”砸因子，看它是真金还是泡沫。

**2. 输出指标怎么看？借助Kimi大模型**


> [!NOTE] [图片 OCR 识别内容]
> 捐标
> 含义
> 判断标准
> mean_beta
> 因子每涨1  单位。未来收益平均变化多少
> 绝对值越大越好
> t_Value
> 显著性检验
> 川
> 2.0才算显著
> 95% CI
> beta 的置信区间
> 不包含0才算有效
> mean_rz
> 横截面解释力
> >0.01  就有信息量
> Valid_days
> 有效回归天数
> >250才稳健


**3. 检验可用数据有哪些？个人理解**

- 可以是单因子；

- 也可以是多因子合成的时间序列因子值；

- 理论上只要是固定格式时间序列值，都可以。

简单起见，此处使用USA D1中PV数据集中的pv13_custretsig_retsig（Sign of customer return）举例

**二、实证过程**

**1. 是否能够生成有效因子，使用者多少？来自Data中的数据描述**

**
> [!NOTE] [图片 OCR 识别内容]
> Resion
> Dzay
> Uniwerse
> Data
> Datas2zs > Relationship Data forEqUiTI>
> custretsIgretsig
> U-
> TOF0
> Simulate Field
> Visualize Field
> Field description
> Category: Price VoluME
> Rela-onshp
> Type: Matrix
> SIan
> CUstomerreturn
> Reglon
> Delay
> Unlerse
> Pramld Theme
> LOerage
> Na5
> MUUUOUe
> TIPTI
> 4
> pvTy
> TREI
> Uen
**

**2. 数据分布情况如何？分布是否均匀？借助Brain Labs分析value分布，接近正态分布**


> [!NOTE] [图片 OCR 识别内容]
> TCJn
> TnC
> 071T
> TN/CFIn o
> Flal
> CUTCTCC519
> 「519
> UITCTSR
> 773000'
> O个5
> 7
> 0.0111
> NIT-+FT
> Nisri ;OIITadel
> Tilnt
> Distnuon of pv13 custretslq
> 「a/SI alles
> SNIIIIT
> UIIIO
> 
> 300000
> TOI
> JOUOUU
> 191



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> CO Cl
> custrets 诅B_rets JB;
> 昵 SeIe Data Ses Moh3
> eate Data
> ShE P=
> TMPTC
> TT S
> [SHo
> 0.,87
> 15.9290
> -0.,52
> 5,6700
> 5S,5
> 859
> 39300
> 5411UUJLUOI
> SeltII =
> Itnw-lu TI 
> Reglom
>  UNer
> URU
> Day
> Uo
> Trneatn
> Nubollolon
>  Pasteurtaton
> NoN Hancng
> Unt Hanong
> Ue Trede
> SN
> Tumo
> Reurs
> Io
> Uong Cun
> Shot Cont
> U5
> TO?C
> SFres:
> 0.23
> Subindustr;
> 2013
> .+
> 151
> 1
> .1*
> 243
> 0+53
> 15
> 71_
> J.s
> 15::
> .45
> ?:
> 51
> 115
> 2=
> _
> :
> J?
> 43::
> 12
> Clone Alpha
> ZE
> 1.34
> 1 _
> 04
> 1''
> 13_7 
> 17
> 172
> 3017
> E
> ECs
> 55
> TT
> 11
> Chart
> Pnl
> 71
> 0.10
> 1C;
> D
> CI
> 35.
> 7.512.
> 仨?
> 1
> -715
> 1.55
> 87
> El
> 5-
> 113
> 1-
> 17
> 220
> 53
> 4
> 322:
> 一
> 1
> OOJK
> .2
> 177::
> 72:
> :
> #:
> 1SJe
> 222
> 52
> 3
> 0.23
> 5
> 5-
>  :
> 1
> 0721202D
> OOJK
> RIL NeIrra
> 8778
> 72
> 3*
> u;
> -3871SE:
> ~OOJ
> Risk neutralized
> ln
> 1 C
> Jn9
> Jr'-
> J '21
> In 22
> 1n-
> Assregale Data
> 5131
> [12!
> 011@
> UTIN
> 0.31
> 15.92%
> 0.28
> 1.959
> 21.02%
> 2.479630
> P1
>  N
> Ma
> SU5


**3. 分组是否清晰、均匀？分组中性化结果是否有畸变？**

**- 分组：清晰、均匀**


> [!NOTE] [图片 OCR 识别内容]
> UIETOe
> Dvl} custretsIg
> retslg
> SUILITOISLR;
> CUCLUL
> CJeL+
> CVCLL
> CeLLN
> CVCC-L_
> CNeCU
> CCCU 
> CVCC-LU
> CVCYU1
> UJllt
> 71031(
> V=tenals AT
> CTTMMTI=TITTC
> ~911431e
> 71031/
> 23[NCCS
> NIaCITanGznere
> TTAJC
> LTCOIUIC
> 13-1
> Retal-KEJn
> UEpt Store
> UVeTtSITO AOENCIEs
> Computsr Nded Uesiqn
> nanoal GIaantee I
> MaCITRMaLenE
> LanJl
> CTTbII CSINITCI|
> TtallLESTaUTTt
> auyertising
> Cl
> CmII=
> SCITIt
> [33Tc
> mmInitTr
> NIacISNIILTd
> LTT
> CUTTPITTUIT
> Retal-sportng
> 69
> UVeTtSITIC
> SEMCZS
> CUIUULZ
> STIZE
> 7sh2112
> NchlnaRHUIDs
> LTate
> TIUIt'
> HetallIJ
> StOTE
> 三TI-031
> UETans =
> CTmII=
> 5nfta
> NlacInThemI PTC -ess
> PTfelTna
> STIITT
> RfalTSh Sr(rtr
> UTOSDAC
> UETZns =
> ZCUIDIent
> CDILULTS
> OUJCaNIEC
> Nann
> SEMICS
> LCDTt
> CasValt Ins
> HetallMtIIns
> VUT SUp
> ayricultural BIotecn
> CTmIMtrcnanrtedShams
> cd-catering
> NCr =
> ITTSUITMS52/7
> CIHECTIn Sfah
> U-hTrTCT
> aget Cars
> LCTICUITUTa
> CTeMICAIs
> CUILULTSMeMOIY UeICZ
> OUJ CONecIOnET;
> NEOICa
> at107 S/5
> Fblic Thorcughtares
> HUbUE
> HaSHIC TOUUCs
> LTTICUITUITaI
> Ope
> 73NT/5
> CTIIMtrs MthE
> 1 LnITTICC
> NCr =
> ITIN2
> MIAIITITT-10
> ThHFCIT
> UIF MIUIDn CorTS
> EOUITIIZT
> CTTTULZTs HnnTZra
> COUIONER
> UalT
> NECICa
> Labs
> ZSHIT ?
> LUOIITITO-Mewspaqars
> IrIts Centr
> LTIIT Sc
> CTTTMtc
> TE-nTnrtI
> TNI-EA Lr TTIT
> Neris
> Lstars
> MIhIITITT-CImprals
> TTIS Tatem U
> Mrmort Uevelcn
> Ialtnance
> CTTSUITIT Serilcas
> LOOO-TIsC
> UTerItlen
> NECICa
> HTOTUCT
> SaTyIh
> ITTIs SOUHEITU
> Uem
> CTSTI
> CTNCIm
> PCTIs-LIC 
> NJ-sl
> NCr =
> TTST =
> GGene
> AFILAnTmert
> TTISMm (
> UEMaIIVE
> Wasie IECT
> CTntaInErs VEa
> G1a55
> LOOO-VHUeSaI
> Uistnt
> NCCalUNUI
> REITS Drersihed
> Satallne
> ZCCII
> appare
> MaTIFTIIT
> CtanFr Man-r
> Plastic
> TN'ea
> Jelatet 'rparel
> NerliralGarFTIC Mmn
> AIT-Haalh CaT
> Thools
> RIInce
> TTSMT-NCc
> TIFTTIa=
> SVT =
> HLC[个s
> Sa ng
> LTTOTI


**- 模拟：均匀、无畸变**


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Cregted 09.082025 EDT
> JnonymOs
> * pha
> 3Lst
> Code
> IS Summary
> Prodl
> custretsig_rets 琚;
> 眺 See Dats Ser Mloh3
> Broup_Fank(u, subindustry);
> Hat
> Dar
> TITTI
> TITE
> CT
> Warar
> 12.2690
> 1,25
> ,95%6
> 4489
> 12.969000
> SIIIIITIOI
> Setrlnzs
> Srpo
> Tunou
> T
> Reume
> OIoo
> Mrgln
> Uong Cnt
> Sht Cwnt
> UtwtclTD
> Rdl
> Uoherse
> Lenguay
> 0cay
> Oay
> Twncaton
> Nuualhabon
> Pasturtad
> NaNHalo
> UtHnUlno
> Ua Trede
> 2013
> 3.53
> .31.
> 1.9.
> 3 .
> 53:
> 15-
> U 
> TC?3O]
> 王 =C
> 0.03
> SJU
> 201-
> 7
>  
> 0.73
> 一?:
> 3.2:
> C:
> 1_-
> 2=
> 29
> :
> 2-5
> 12 :
> 污:
> 1 :
> 14
> Clone Alpha
> ZE
> 3
> 11.318
> 274
> 5
> 3:
> 1汜
> 143
> 3017
> 15#
> 05
> 1
> 51
> 116
> 71
> 15
> 002
> C4
> 41
> TST
> 1713
> 1-7
> Chart
> -715
> 1.75
> 2.35*
> 2.
> 15C
> 1T2
> 1-33
> 220
> 4:
> 11 :
> 3-7
> 1
> 11 _
> 537
> 二 :
> :
> 37.5:
> 17=
> 15
> 25'0712021
> TJDK
> Pn
> 37.-5k
> 222
> _:
> 8
> 汀
> 2:
> 1_73
> Rlk NeuralkedPnL-.
> 72
> U
> 03*
> :
> 1
> 20
> Risk neutralized
> Assresale Data
> |
> UTI@
> 0
> Ia11
> Jn 4
> Jon15
> 4Jn'16
> J `18
> Jung
> J3
> Jn 73
> 1.10
> 12.26%
> 0.58
> 3.51%
> 3.78%
> 390
> Rsk NEUTaIZEDPnl
> Pv
> _


4.  **Fama-MacBeth 回归检验结果如何？**

**- 代码：来自Brain Labs案例**


> [!NOTE] [图片 OCR 识别内容]
> 127T1
> TTnnr
> Tnyrl
> IINOTT
> 1 :n6rReorrssion
> TnTt
> SCTT';
> 517+-
> 5TT
> T Tegressionuf
> GaS:1 :
> Lhaci
> SIgnals With Fana
> I UetnNegresSrUI
> retyrns
> TUtrat170 UT
> df.sU(Jf.neanlaxis=
> 3115二 |
> Jetaye0
> 0+Tl
> 21116221
> NIMTCaITa
> 3h(
> SIL15=11
> ShTt'
> Olu5
> IqUJreo
> 「turns
> 6rnin
> 16rin
> Filgl"return '
> ITarr
> T-7-F
> inle
> RarrT
> STatisTIC2 simni-icae
> [131
> 01-+3
> LlVas
> 「-hnc1
> TCUFNS
> Ltves
> VEnenUent
> Whl
> VJLLU Isk
> LSMIN I
> 1LutLC' !
> 1SJMLY1
> T]
> YL]'6
> 711
> VLI11457k
> C-055-SC-tionl
> TTTC5TOI
> 1ET1
> 11+1
> [02l
> LIn=aTRTTEsSIOTI|
> [Tel
> 717
> U1
> NlU |
> Ltus_tLst
> OLL JIOLl
> SVare
> T
> predic: (x_validl
> CTTCIC
> C
> SCCCon
> TRnRT
> TnT3 |
> SIIy
> Tpeanly
> 6111902 1
> o111
> SITI
> 471+
> SOUaTE0
> 「1043
> TotalI
> total
> else np.nan
> SNI
> JTEN IT
> SIUaTECI
> elye
> [499
> JHL OOLT .Ih
> SNUHTCI
> UTTCTTTC
> NSa个
> TSTIEFT
> [+
> 1is1
> S141T
> i
> Std_rror
> M.Nasdlberas_lIst)
> {
> l
> TT{
> 1)
> U
> T+T
> 'tve
> ?Fro「
> 5tT
> CONTIOENC? Irtenal
> Cy
> TOTP
> UUII0T
> 953021
> 3TTUT
> SOFTIA/I
> JL[
> UULIIO
> ULJI CCl
> .90
> ISCU Crror
> SOTINI
> VU-Ia
> 1
> Ah
> TNITTTO
> Lrd listi
> prinz |
> H HEITeSSITI
> SUIT3T
> 5 |
> |CUS107
> 31
> LaT'
> SCCNI
> 9371
> 5LUCTror:
> LSLTTOUnUlsed CrTr
> mm
> IT+
> 1s?TTTOUNJIUCNC [
> JOI
> |
> [str(roud (upper_bound。 2)11 ]
> Th
> TUTTd
> 5TTTTomdlnn
> SAUTCI
> 711
> U1 
> 015 ;
> 4541559
> 0;|
> 71+
> OFOI ^


**- 计算结果**


> [!NOTE] [图片 OCR 识别内容]
> U
> Bralnlregions UsA 
> PLJ-
> UVerse=' TopJe30]
> daulleld_dl
> UToLIsy UJ
> 1JnICTJ-I
> Uulu
> 1UUJIU
> CUStieLg_Tets-y
> TCgTc55?oplo7tt1ocd 01
> KCICUl
> UII
> ]+ *
> 'TI
> PTFII '
> 95 ConTicens
> Tneryal :
> 177
> SOULCeC
> Vuld_duy: 251
> 「S


**- 结论分析（借助Kimi大模型）**

**
> [!NOTE] [图片 OCR 识别内容]
> 指标
> 数值
> 含义
> mean_beta
> -1.85
> 每增加1个标准差
> 未来收益平均下跌1.85%
> t_Value
> -9.99
> 极度显著 (p ~ 0)
> 95% CI
> [-2.21,-1.48]
> 不包含 0,方向稳定
> Valid_days
> 2517
> 10 年+的样本,极度稳健
> mean
> squared
> 0.0
> 横截面 解释力极低
> 但这不是问题
> (FM 回归 Rz 通常都很低)
**

**- 结论：这是一个极度显著、方向稳定、样本充足的反向因子**

**三、 验证二步回归结果**

**1. 用rank≥0.7和sign≥0.4实证二步回归检验**

**- rank验证：sharpe标准0.87×0.7=0.61＜0.67，合格**


> [!NOTE] [图片 OCR 识别内容]
> U
> Created 09/082025 EDT
> anonymOUs
> Add Nphato
> Ust
> Code
> IS Summary
> Perod
> 0VI3_custretsig retslg;
> 吣 Snele Data Setsloha
> rank (a)
> ASBregate Data
> SharDs
> TUrno=
> Flnes:
> C
> Orawgowr
> Wrain
> 0.67
> 15.5096
> 0.34
> 3.9996
> 12.59%
> 5.1596o0
> Simulation Settines
> IstrUMI Typa
> Reolon
> Uherse
> LnOage
> Co
> Oy
> Truneton
> Neutllnwon
> Pastewrtato
> NaNHang
> Unlt HanO
> Nax Tmd
> Shalp
> Tutwer
> Fgs
> Returns
> Dewdown
> Uagln
> Log Cont
> Shot Count
> Sauny
> C-
> TO-J
> Fast S Cressn
> T
> 0.03
> SubnJ-sr
> =r
> 7013
> 0,7
> 1537:
> 03
> 77
> C3-
> 33:
> 15
> 1
> -1
> 7
> 1_7-:
> CEJ
> 459沁
>  .
> 5--
> 1533
> 15-
> 301=
> 0.3
> 15
> 0?
> 303
> 251汨
> '130
> 157
> 153
> Clone Alpha
> -015
> 0.34
> 1-37-
> 037
> 二75:
> ~55.
> 33-
> 三
> 127
> 2017
> 111
> 12
> 5855
> 2376
> 3319
> 521
> 1527
> Chart
> nl
> 2013
>  E
> 1_5:
> 0=
> Cs:
> 225
> 77:
> =
> 1525
> 2019
> .34
> 151
> 0.10
> 1.21沿
> 85汩
> 52
> 115
> 152
> 01
> 153:
> 140
> 3
> 1E
> 5;
> T=
> 1513
> 一-
> 5
> 17.3
> 0-J
> 1.07
> 9.33
> 3
> 154
> 1SE_
> 0JJ
> 11/232018
> 3022
> 0.1E
> 1535
> 005
> 4沿
> C12
> 157:
> 11
> 1573
> Du
> 333.17
> Risk Neutralized Pnl
> 582.36<
> -
> 15_
> 131
> 11.75.
> T1
> -:
> 1-3
> 1537
> Risk neutralized
> Jn '14
> JaT 15
> 0715
> Ja
> 13713
> 119
> J2
> 157.71
> J7 -
> J2
> Aeereeate Data
> Sharce
> IUTTO
> Finess
> FetUCN
> 903OU
> Warein
> 0.71
> 15.509
> 0.23
> 1.5996
> 6.5490
> 2.0596oo
> Pn
> Risk Neutralzeo Pnl


**- sign验证：sharpe标准0.87×0.4=0.35＜0.54，合格**

**
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09;08/2025 EDT
> anonymous
> uodphato
> Ust
> Code
> IS Summary
> Perod
> Custretsig retsig;
> 0 Snele Data Set slpha
> sign (a)
> Aeeregate Data
> Sharp=
> UTMC Ir
> Fisness
> T=upns
> OTaUT
> Nsrain
> 0.52
> 12.1296
> 0.24
> 2.4596
> 12.78%
> 4.049600
> Simulation Settines
> IstrumltType
> Reolo
> Uhers
> Lnoage
> Cy
> Oely
> TNNCton
> Newtllawon
> Rastertzatm
> NaN Handlg
> Unlt Handwng
> Ia Tmd
> Sherpe
> 
> Fes
> Rts
> Dowdowm
> Noym
> Lo Co
> Shot Count
> Sury
> U-
> TO-J
> Fast SpressIen
> TZE
> 0.03
> Subindusoy
> Ur
> T0
> Cs
> 14
> Ds
> 3
> 222:
> 302:
> 151
> 131
> 2011
> 11.459
> 0.82
> 4419
> 4.15
> 7.7C.
> 53
> 15_
> 2015
> 025
> 113
> DDE
> 7.
> 3
> 2
> 5
> 1565
> Alpha
> ZOIE
> 031
> |_
> 0.03
> 0.35:
> 1
> SL:
> 110
> 1SES
> 2017
> TCE
> 11635
> 0.3
> 41
> 3
> J5
> 435
> 1545
> N Chart
> Pnl
> TO
> 0E3
> 41 =
> 0
> 1.359:
> 3:
> 37:
> =13
> 1=3
> 201
> +0.20
> 121
> 4
> 5
> 243
> 0.9
> 4
> 1545
> 3030
> 731
> =
> 73
> 17-
> 11
> 72:
> 13
> 19
> -1
> DS
> 1.759
> 031
> 4+9
> 1559
> 551.
> 45
> 15-3
> 7OD
> 702
> 011
> 1705
> D0
> 32.
> E S2.
> 5.711:
> 1513
> 1E01
> DJO
> 一
> .-5
> 125
> |
> 7.519
> 0.5:
> S:
> 110
> 1-
> Risk neutralized
> Jny
> Ja 15
> 17 16
> Ja
> Jan8
> Jan9
> Jan '20
> 1371
> J7 -
> Jn
> AEEregate Data
> SNarce
> Turnove
> Fihe_=
> Reury_
> DrawJowi
> Warsin
> 0.51
> 12.12%
> 0.15
> 1.06%
> 4.84%
> 1.759600
> Pn_
> Risk NeJralzzo Pn_
> 0v13
> Clone
**

**2. 分组、验证、增强并提交：** 用ts_rank进行增强并提交

**- 分组：sharpe=1.57**


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Cregted 09.082025 EDT
> JnonymOs
> * pha
> 3Lst
> Code
> IS Summary
> Prodl
> custretsig_rets 琚;
> 眺 See Dats Ser Mloh3
> Broup_Fank(u, subindustry);
> Hat
> Dar
> TITTI
> TITE
> CT
> Warar
> 12.2690
> 1,25
> ,95%6
> 4489
> 12.969000
> SIIIIITIOI
> Setrlnzs
> Srpo
> Tunou
> T
> Reume
> OIoo
> Mrgln
> Uong Cnt
> Sht Cwnt
> UtwtclTD
> Rdl
> Uoherse
> Lenguay
> 0cay
> Oay
> Twncaton
> Nuualhabon
> Pasturtad
> NaNHalo
> UtHnUlno
> Ua Trede
> 2013
> 3.53
> .31.
> 1.9.
> 3 .
> 53:
> 15-
> U 
> TC?3O]
> 王 =C
> 0.03
> SJU
> 201-
> 7
>  
> 0.73
> 一?:
> 3.2:
> C:
> 1_-
> 2=
> 29
> :
> 2-5
> 12 :
> 污:
> 1 :
> 14
> Clone Alpha
> ZE
> 3
> 11.318
> 274
> 5
> 3:
> 1汜
> 143
> 3017
> 15#
> 05
> 1
> 51
> 116
> 71
> 15
> 002
> C4
> 41
> TST
> 1713
> 1-7
> Chart
> -715
> 1.75
> 2.35*
> 2.
> 15C
> 1T2
> 1-33
> 220
> 4:
> 11 :
> 3-7
> 1
> 11 _
> 537
> 二 :
> :
> 37.5:
> 17=
> 15
> 25'0712021
> TJDK
> Pn
> 37.-5k
> 222
> _:
> 8
> 汀
> 2:
> 1_73
> Rlk NeuralkedPnL-.
> 72
> U
> 03*
> :
> 1
> 20
> Risk neutralized
> Assresale Data
> |
> UTI@
> 0
> Ia11
> Jn 4
> Jon15
> 4Jn'16
> J `18
> Jung
> J3
> Jn 73
> 1.10
> 12.26%
> 0.58
> 3.51%
> 3.78%
> 390
> Rsk NEUTaIZEDPnl
> Pv
> _


**- rank验证：sharpe标准=1.57×0.7=1.1＜1.57，合格**


> [!NOTE] [图片 OCR 识别内容]
> UNS
> Creglsd 09082025 EDT
> anonymOus
> NJDataJS
> Code
> IS Summary
> PuTrod
> pVI3_custretsJB_Fets g;
> [ See Dats Ser Moha
> PTUIV
> Tank(a, subindustry);
> eank {)
> AEBreeate
> 0C3
> TUTTO
> TICN
> TTJTI
> LTyC
> 1.57
> 12.2690
> 1,25
> 7.9790
> 4.509
> 3,019000
> SIIUIaton Settllzs
> WotwelTYD
> Reglon
>  UoNerse
> UB
> Way
> Tmncaton
> Nuballallon
> [-T
> NaNHandlg
> UntHanolng
> Ua Trede
> Ver
> Cro
> Tmg
> Ft
> Reum
> [r
> Wrgln
> Long Cont
> Shot Cont
> TS?
> Fast XPres:?
> 7.13
> Subindustr
> Vn
> 21
> 3.D
> .5.
> C
> 1.5
> 3.5.
> 275:
> 15
> 201-
> 1
> 一_ :
> 一?
> 3
> =:
> 1__
> 3
> ;
> 10.2 :
> 污:
> 5:
> Clone Alpha
> ZE
> 38
> 277*
> 3
> 1u
> 3017
> 0.31
> 0
> AE
> 45
> 二!
> 113
> 2018
> 52.
> C
> [J
> 4.17
> TSE
> 1715
> 147
> N Chart
> 2115
> |
> 20
> 1-SC
> 20120
> 2
> 1015
> 3.
> 1 -
> 1-11
> 2.55
> C_:
> Js :
> :
> _:
> 1
> -3
> 222
> 222
> 210:
> 3污-
> =:
> 17
> 1212'2213
> 51
> 2
> 3
> SDK
> 2315r
> RLsk Neutrallzed PnL 1ASE 6S
> Risk neutralized
> DUu
> Orauro
> Jr'20
> In 
> Jn 77
> 1.09
> 12.269
> 0.58
> 3.529
> 3.84%
> 5.74960
> ZSKNEE
> ZEU Pnl
> 0a
> 三」
> ?5
> Fesi
> SLut


**- sign验证：sharpe标准1.57×0.4=0.63＜1.42，合格**


> [!NOTE] [图片 OCR 识别内容]
> UNS
> Creglsd 09082025 EDT
> anonymOus
> NJDataJS
> Code
> IS Summary
> PuTrod
> DVIL
> custretsiB_rets 氓;
> 昵 Sele Dats Ser Nlph3
> PTUIV
> Tank(a, subindustry);
> SLBn ()
> AEBreeate Data
> 3C=
> LUIFnC
> TTS
> TZUTT
> a
> 42
> 5,7
> 1,14
> 8,009
> 5,5791
> 28,029000
> SIIUIaUOn SetUnas
> WotwelTYD
> Reglom
>  UoNerse
> UB
> Tmncaton
> Nuballallon
> [-T
> NaNHandlg
> UntHanolng
> 2
> Ver
> Chc
> Tuler
> 「t
> Rhr
> 0r
> Marglm
> Cnt
> Shot Cont
> TS?
> Fast XPres:?
> 7.13
> Sidustr
> 711
> 3
> 3
> 537.
> 4.529
> |.
> 一_
> S.E
> E:
> 3.1:
> 3+:
> 1E
> 3
> -5:
> 12-3:
> :
> Clone Alpha
> ZIE
> 143:
> 4.21.
> 3017
> 055
> Cr
> 5
> 31
>  T.
> 2018
> 055
> 1.57 .
> 4,139.
> 5ZS
> 153
> 113
> N Chart
> 2115
> 7-
> 5.03
> 3 .
> .239
> 3.
> 15
> 220
> ~5
> 5715
> 03
> 一-
> :
> 53
> 2:
> 一:
> :
> 2017
> 137
> DDK
> C1272
> 222
> -5
> 312:
> 污:
> 1218
> 355.52k
> Risk Nautralzed PnL:
> 3153
> 22
> :
> 0.738
> 15;
> 1
> 2S3cK
> Risk neutralized
> Aesregate
> DUu
> TurnO
> Rlurr
> SISJ
> Warel
> Jun 14
> en '1
> In 
> Jn 77
> 0.91
> 5.70%
> 0.46
> 3.23%
> 4.8795
> 11.3496
> Pnl
> Risk NEUTaIZED Pnl
> Uen
> 0a
> Ct
> 20
> 5:
> DT
> 2;
> gL


**- ts_rank增强并提交**

**
> [!NOTE] [图片 OCR 识别内容]
> ACV
> Cralsd OSOS 2025 EDT
> anonymoUs
> AU Aphgt 3 UIst
> Code
> IS Summary
> Period
> a 「CVerse(ts
> Fank (EFCUP
> TMI
> CustretsJB_retsJ'
> subindustry)
> 752));
> ICme
> VarasetUtilaton Iheme
> 昵 Sirale Daza Ser Alpha
> Power Pol Alpha
> Pramio there: USNDIIPV &1
> NEBreEate
> 0ara
> TITTI
> CIT
> Crano
> 13.8590
> 1.25
> 7,789
> 6.349
> 11.,249000
> SIIUIatIor
> Settinss
> ImuTR 
> Reglon
>  Uner
> URU
> De
> Tmncgtn
> N-uuallaton
> Pasturbouo
> NoN Helclg
> Unt Hanoung
> Ue Trede
> S[ 
> Tum
> T
> UI
> Io
> OM
> on Cun
> Sht Cont
> TC-
> Fsst SFrsss ?
> 1.23
> Sbindustr
> 2513
> 17
> 12-3
> 1_ .
> 53:
> 1s+E
>  _
> _
> E.S
> 207:
> 3:
> 1ss
> 2015
> 1_-
> 一1::;
> 17-
> 洪:
> 125
> Clone Alpha
> ZTE
> 14
> 1
> 70_
> 377-
> -
> 1_汇
> 3017
> 1-
> 5
> 15
> E
> 1
> N Chart
> 211
> 1
> 5.25玷
> 1
> 3.25
> 715
> 1235
> E.23沿
> -3.
> 10.51:
> 1
> 一
> 5:
> 一5
> E
> 5:
> 1-3
> :
> 23.75沿
> 43:
> 3:
> U
> 13
> SDDK
> 2122
> _
> 473-
> C:
> 1
> 1_5
> OIJE -13
> 
> E
> J
> ~抵;
> 118
> 15Pnl  3353.E2
>  =JO
> Risk neutralized
> HSICSJL
> 1
> T
> U
> Marein
> 24
> 13.859
> 0.59
> 3.0995
> 4.31%
> 4.46950
> 1
> 1n
> 3__
> In _
> Pv13
> Ce
> 』
> TL
> ShaTF
**

**3. 总结：** 金融与资产定价研究中，Fama-MacBeth 回归（1973）至今仍是国际学术界最主流、最通用、最被认可的因子显著性检验框架之一 ——  **解释来自借助Kimi大模型**

- 能够通过二步回归检验，说明因子的预测性是显著的，能够在很大程度上确保OS的稳定。

- 建议在后续因子分析中，有条件的情况下，应首先进行二步回归，避免走弯路，提高分析效率。

- 在一定程度上说明，rank≥0.7和sign≥0.4的验证是有效的（相对宽松），在simulator中可以使用。

---

## 讨论与评论 (21)

### 评论 #1 (作者: WL13229, 时间: 9个月前)

这个文章其实发掘了一个使用BRAIN LAB变成一个回测器的思路，建议大家使用。虽然alpha很简单，但是可以帮助你拓展自己的回测槽。别忘了，除了brain的网页请求，你还可以在lab里面遍历。

---

### 评论 #2 (作者: LL87164, 时间: 9个月前)

很好的分享。点赞 👍！

RE: "rank≥0.7和sign≥0.4"，两个问题：1、这两个值的出处来自哪里？经验还是论文？2、文中这两个验证与Fama-MacBeth 回归验证的关系，是以谁为主，即用谁来验证谁，还是说可以起到互相“替代”验证的作用，一阶后的信号，用 rank 和 sign 来验证即可？

---

### 评论 #3 (作者: JL76306, 时间: 9个月前)

很感谢贴主的复现和分享，这样的验证思路对alpha呈现了不同维度的表现效果。

这里想请教一下，对于这个主信号贴主有什么样的筛选技巧呢？因为显然现在LAB的反应速度较慢，无法快速的找到这样数据正态/均匀的数据字段。

或许该思路是否也可以对应为符合上述类型数据字段的高效模板呢？

---

### 评论 #4 (作者: SL19872, 时间: 9个月前)

单个因子是如何筛选的？先裸跑吗？

---

### 评论 #5 (作者: YX50005, 时间: 9个月前)

之前有尝试在lab中大规模的跑一些数据，但是好像跑一段时间就自动停了，不知道主包有没有遇到？

---

### 评论 #6 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

大佬，真是太棒了！🙇‍♂️ 您这篇帖子对我来说有些晦涩难懂，但看完大受震撼！作为一个小白，好多术语都不懂，但您这个 step by step 的实证过程，还有和Kimi的联动，让我这种菜鸟也能模模糊糊感觉到这个因子“很强”！

尤其是最后您说的  **“能够通过二步回归检验，说明因子的预测性是显著的，能够在很大程度上确保OS的稳定”** ，这句话我拿小本本记下来了！以后我自己做因子，也知道了不能光看模拟收益，得先拿这个“统计铁锤”砸一下，看看是不是真金，不然全是白费功夫。

---

### 评论 #7 (作者: MY49971, 时间: 9个月前)

很好的分享，这样是不是可以在lab里面遍历单字段和returns的回归，筛选出其中具有统计显著性的字段来跑？

===================================================================================
===================Talk is cheap,show me the alpha=======================================

---

### 评论 #8 (作者: JB53978, 时间: 9个月前)

很好的思路啊，我还没去搞mcp，你这个思路挺不错的，后面我要搞mcp了就使用你这个思路去试一试看看效果，你mcp是使用什么模型的api呢，是国内的模型吗。

===================================================================================

---

### 评论 #9 (作者: LR93609, 时间: 9个月前)

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)

master你好！关于你的问题：

RE: "rank≥0.7和sign≥0.4"，两个问题：1、这两个值的出处来自哪里？经验还是论文？2、文中这两个验证与Fama-MacBeth 回归验证的关系，是以谁为主，即用谁来验证谁，还是说可以起到互相“替代”验证的作用，一阶后的信号，用 rank 和 sign 来验证即可？

回复：

1. 论坛中热心网友的经验值，我觉得有意义，就用起来，现在看来是没错的。

2. Fama-MacBeth检验是国际通用检验标准。

3. 我是在最终提交时使用rank和sign，因为不同neut下，结果是截然不同的。

感谢回帖，有问题，随时问。

---

### 评论 #10 (作者: LR93609, 时间: 9个月前)

[JL76306](/hc/en-us/profiles/27129028295447-JL76306)

感谢回帖

其实，裸跑字段是最好的办法，速度也很快，比Labs效率要高很多；

我觉得如果sharpe>0.7 and fitness>0.4，说明是不错的字段。

当然，不是说sharpe<0.7就不好，可以先标准化，再跑，速度也很快。

我有很多模版，不同数据集匹配不同的模版，大多数时候：

我先shuffle看看信号密度，然后再深入搜索；

如果信号很少，pass；如果信号很多，就深入，做市场推广的套路。

感兴趣可以看看我的另一篇帖子，专门介绍信号密度的：

[../顾问 MZ45384 (Rank 51)/[Commented] 【Alpha灵感】虎哥模版实证及其改进效果评价Alpha Template.md](../顾问 MZ45384 (Rank 51)/[Commented] 【Alpha灵感】虎哥模版实证及其改进效果评价Alpha Template.md)

---

### 评论 #11 (作者: LR93609, 时间: 9个月前)

[YX50005](/hc/en-us/profiles/29899344989847-YX50005)

感谢回帖

我没有大规模跑过，只是偶尔看看数据结构，毕竟操作符有限，

我觉得打开速度慢，就说明资源有限，可能不支持大规模的回测。

有机会，我深入研究下，发帖分享。

---

### 评论 #12 (作者: HM24686, 时间: 9个月前)

感谢大佬的分享、解惑，学到了很多。

---

### 评论 #13 (作者: BT92131, 时间: 9个月前)

**#========= WORLDQUAN =====**

**这个分享值得试试，    这个是一个开始，确实看到自己缺的东西，然后进去努力就行，expect希望上**

**#================ ole ole =======================#**

---

### 评论 #14 (作者: 顾问 JX79797 (Rank 9), 时间: 9个月前)

[LR93609](/hc/en-us/profiles/30244554462231-LR93609)     冷兄的一系列 灵感贴 看了很有启发， 目前集中在框架、mcp，下季度一定好好研究研究！！！

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**

---

### 评论 #15 (作者: LR93609, 时间: 9个月前)

HM24686

抱歉没理解里的意思，如果只是调decay的话，个人建议：

1. 大部分情况下decay与turnover是负相关，pv和sentiment等数据集除外；

2. 我一般用5/10/22/44/66/126/256/512，不会像11/12/13/14这么细致的去调，避免过度调参；

3. turnover也不要降到5%以下，5-10%为宜，再降就失真了。

不知道有没有回答你的问题，感谢回帖。

---

### 评论 #16 (作者: ZW33065, 时间: 9个月前)

感谢各位大佬的分享和讨论，学习到了。

---

### 评论 #17 (作者: AM12075, 时间: 9个月前)

请问看到lab的图之后是怎么确定该用哪些操作符的呢？全是问AI吗？

===================================================================================
===================================================================================

---

### 评论 #18 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

谢谢分享。 看来以后要通过Lab做一下数据筛查，观察数据分布，再去做回测。特别是GLB这种回测速度慢的region，这样可以避免大量无效回测。

---

### 评论 #19 (作者: LR93609, 时间: 8个月前)

[AM12075](/hc/zh-cn/profiles/30421958512663-AM12075)  感谢回帖

我觉得AI也不太懂数学，毕竟它没有过系统的认识或者是学习，缺乏研究思路。

我主要是三件套：

**1. 标准化、归一化：** 用zscore、rank或scale，先让它随机分布；如果本身就是正态分布的，就直接用；如果不是正态分布，就再调整。

**2. 检验波动性：** 服从正态分布的字段，波动性也是随机分布的，也是有信号的；

**3. 周期轮动性：** 如果服从正态分布、波动性也是随机的，那么周期轮动性也会有信号，大概率也是随机分布的。

这是三件套，我还没有偏度、峰度等Operator，我相信后面还会拓展为四件套、五件套，届时我再来分享。

-----------------------------------------------------------------------
  凡是发生，皆利于我；愿我所愿，尽是美好
-----------------------------------------------------------------------

---

### 评论 #20 (作者: LR93609, 时间: 8个月前)

[顾问 YH25030 (Rank 31)](/hc/zh-cn/profiles/28941108652823-顾问 YH25030 (Rank 31))

感谢回帖，您的方向是对的，给了我新的思路，后面我也验证下，争取开发更多的因子。

-----------------------------------------------------------------------
  凡是发生，皆利于我；愿我所愿，尽是美好
-----------------------------------------------------------------------

---

### 评论 #21 (作者: DX67257, 时间: 8个月前)

冷兄，请教下

vector类型字段如何验证

---

