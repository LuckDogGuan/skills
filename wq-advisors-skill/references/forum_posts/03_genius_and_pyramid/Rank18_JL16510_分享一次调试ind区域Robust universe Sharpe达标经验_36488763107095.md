# 分享一次调试ind区域Robust universe Sharpe达标经验

- **链接**: https://support.worldquantbrain.com分享一次调试ind区域Robust universe Sharpe达标经验_36488763107095.md
- **作者**: 顾问 JL16510 (Rank 18)
- **发布时间/热度**: 7个月前, 得票: 33

## 帖子正文

最初该alpha通过一阶跑出，回测设置和结果如下：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> +s_ZSCore
> Tndl7_ttmepsincx,
> 258
> A single Data Set Npha
> ABBregate Data
> Sharpe
> TUTTOLE 
> Fnes
> Rerupns
> Orawoown
> Nargin
> Simulation Settings
> 2.51
> 6.58% 2.68 14.269 9.76% 43.349600
> Irstrumen: Type
> Equi
> Truncation
> 0.08
> Rezion;
> I0
> Neuralzaron:
> Irausny
> Unlers=
> TCPSUO
> Tastsurizaton
> Year
> Sharpe
> Turoer
> Ftress
> Returs
> Drawdown
> Marqin
> Long Coun
> Short Count
> Larauogc;
> Fos  Eprc -lon
> NaN Handlins:
> Decay:
> Unit Hardlins:
> Verify
> -01
> 371
> 5.88%
> ;16
> 21.039
> 498N
> 71.53
> 133
> 11
> Delay
> Ma  Trade
> 201-
> 1.83
> 614-0
> 1,83
> 11,67
> 9.7690
> 38O-oc
> 2015
> 430
> 5.374
> 5.90
> 235+0
> 1.95q
> 80152oe
> 165
> 143
> 2016
> 1.37
> 7.214
> 1,03
> 7.005。
> 2-29
> 19.42oc
> Clone Alpha
> 2017
> 1.30
> 6974
> 0.99
> 5.3
> 3 19q
> 168832。
> 146
> 2013
> 3.21
> 6.539
> 3,94
> 17.919
> 3+9
> 5363
> 136
> N Chart
> Pnl
> 2010
> 307
> 5O
> 4,04
> 21,645
> 3849
> 50.340
> 2020
> 143
> 6.309
> 1.21
> 8-2
> 3.309
> 74742
> 733
> 223
> 2021
> 343
> 6.214
> 47165
> 2.41q
> 3531
> 239
> 200
> 2022
> 1.64
> 5,579
> 137
> 3.69
> 3589
> 30.657
> 750
> 192
> TON
> 2023
> 3,065
> 1,23
> 5,824
> 0384
> 3805
> 265
> 190
> UOOK
> Investability constrained
> ABgregate Data
> Sharue
> TUMION
> Fncss
> Rerurs
> Drawgowm
> Narg
> 1.94
> 4.199
> 1.84
> 11.21%  11.76% 53.559600
> 2015
> 2017
> 2019
> 2021
> 2023
> Pnl
> Inyestability Constralned Pnl
> Correlation
> SeltCorrelation
> Maxmum
> Mnmum
> Lo
> RUR
> Prod Correlation
> Mamm
> WNMUm
> Last
> Rup
> IS Testing Status
> Perlod
> 9PASS
> 1FAIL
> Performance Comparison
> RObUSLUnIVerse
> Sharpe Or0.90Is below cutotiof
> ColRum
> WNRNNC
> 4PENDING
> Properties
> Lunsaed Thu  11/20/2025。12,25 AN
 
可以看到Robust universe Sharpe为0.9，距离达标还有一些差距。

首先注意到该alpha的Investability constrained指标符合rg的要求，因此打开Max Trade重新回测，回测结果不仅Robust universe Sharpe没达标，Weight concentration也超标，如下： 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_ZSCore(tnd17_ttmepsincx,
> 250
> Single Data Set Npha
> ABBregate Data
> Sharp
> TUrnOVEI
> FInES
> RETUI
> Drawdowr
> MargI
> Simulation Settings
> 1.94 4.19%1.8411.21%11.7696 53.55900
> Irstrumen: Tpe
> Truncaion
> 008
> Region;
> IND
> Neuralzaton:
> Indusn
> Unlers=
> TCPSOO
> pastzurizaon;
> Year
> Sharpe
> Turnover
> Fress
> Returns
> Drawdown
> Margln
> Count
> Short Count
> Lanauoge。
> Fas  Exprc--lon
> NaN Handlins
> Deco ;
> Unit Hardling:
> Verfy
> 7013
> -50
> 05%
> 3.20
> 705%
> 3129
> 105.6。
> 12
> 1
> Delay
> LaxTrade
> 201-
> 1.49
> 3,194
> 1,34
> T012
> T0 07No
> 63_0o0
> 7015
> 3.31
> 3.570
> 3.93
> 47299
> 234
> 96.94。
> 7016
> 071
> 3,999
> 0,39
> 3.769
> 3999
> 13,3520
> 145
> Clone Alpha
> 7017
> 123
> 4,470
> 091
> 5.3600
> 37800
> 23396o
> 193
> 15
> 2013
> 267
> 7,349
> 290
> 14.739
> 2979
> 67.919。
> 140
> N Chart
> Pnl
> 2019
> 205
> 4,919
> 2,08
> 1290S
> 3.344
> 52,569
> 193
> 133
> 7020
> 076
> 4,239
> 041
> 4.179
> 4.759
> 19.70ca
> 233
> 229
> 2021
> 319
> 4,970
> 3,41
> 142850
> 1629
> 57.52360
> 25
> 206
> TON
> 70
> 4,419
> 1,57
> 495
> 479
> 42,BC
> 765
> 190
> 7,50OK
> 2023
> 021
> 2,664
> 005
> 06gqu
> 0.58%
> 51Uesa
> 189
> QOOK
> 'SOOK
> Correlation
> Corrclation
> Mrmum
> Mmmum
> L
> 2015
> 7017
> 2019
> 2021
> 207
> Prod Correlatlon
> Maumum
> MNIUI
> Lat
> Run
> Performance Comparison
> IS Testing Status
> Perlod
> Lst Run;
> PASS
> 2FAIL
> Properties
> Last Saed Wed, 11/19/2025, 721PN
> Wolohconcentaton 12.903
> abowo cutoftof 109b on 1/21/2013
> RobUstUniverse
> 010.74
> beo Cutotof
> Name
> Category
> WNRNINC
> Currenfly 'anonymous'
> None
> PENDING
> Cquin
> Lom
> Soll
> RUn。
> SharbC


如果Investability constrained指标不符合rg的要求，一般情况下首先想到探索decay对其影响，结果发现decay变化对Robust universe Sharpe的影响不敏感。再探索更换neutralization的影响，所有的类型都回测一遍。结果发现还是原本neutralization设置下的Robust universe Sharpe最高。各类neutralization设置的回测结果如下： 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Crealed 11/19/2025EST
> anonymous
> Add Alphat03 List
> Code
> IS Summary
> Period
> ts_Zscore(tndl7_ttmepsincx,
> 250
> A single Data Set Alpha
> ABBregate Data
> 5hams
> TUrnowe
> Frn2ss
> Rerurns
> Orawoown
> Narei
> Simulation Settings
> 2.14
> 6.85%2.1312.3997.749 36.189600
> ITSIIPT 
> Tpe
> quiy
> Trunca-ion:
> 0.38
> Rezion;
> IND
> Neuralzanon:
> Subindustry
> Unwersz
> TCP3UO
> Pastsurizalon
> Year
> TUMOeT
> Ftress
> Returs
> Drawoown
> Marqin
> Coun
> Short Count
> Languoge:
> Fos  Epres-lon
> NaN Handlins:
> Unit Hrdlinz:
> Verf
> 2013
> 41
> 6.043
> 277
> 16.4595
> 6.0896
> 54512
> 103
> Delay
> Ia Trade
> 201-
> 147
> 640
> 1,21
> 9,274
> 7.74q0
> 2880c
> 2015
> 3.06
> 6.019
> 3.51
> 16.719
> 2.159
> 5563
> 2016
> 1.37
> 7.305
> 107
> 7.5944
> 2589
> 20812c
> 138
> Clone Alpha
> 7017
> ~064
> 7.26%
> 0.31
> 28990
> 4749
> -7.952o9
> 2013
> 220
> 6.994
> 2.22
> 12.699
> 3.239
> 36292
> 133
> Chart
> Pnl
> 201o
> 353
> 882
> 4O1
> 2420
> 34q
> 5489os
> 2020
> 1.97
> 7.15
> 1,35
> 11.139
> 7539
> 31142
> 212
> 199
> 2021
> 397
> 6.594
> 4,04
> 19.3740
> 213Nr
> 3875
> 225
> 182
> 7022
> 1.63
> 6.03%
> 140
> 9.209
> 47790
> 30262.
> 220
> 2023
> 二52
> 3,415
> 5,10
> 43,920
> 0364
> 93-73
> 22
> QOOK
> Investability constrained
> ABgregate Data
> Sharpc
> TICNO
> FIICSs
> Return
> Oroyoo
> Wargin
> 1.51
> 4.30%
> 1.28
> 8.959
> 13.949
> 41.649600
> 2015
> 2017
> 2019
> 2021
> 2023
> Pnl
> Investability Constralned Pnl
> Correlation
> Sell Correlation
> Maxmum
> Mnmum
> Lo
> RUp
> Prod Correlation
> MaMUM
> MNMUm
> Last
> Run
> IS Testing Status
> Perlod
> 9PASS
> IFAIL
> Performance Comparison
> Robustunlverse Sharpe Or0.81
> belo Cutotvof 1
> LostRun
> WARNING
> Shrp
> Long
> Oec



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> +5_ZSCore
> fndl7_ttmepsincx,
> 250
> A single Data Set Npha
> ABBregate Data
> Sarqe
> Turnoyer
> FItnsss
> ReTURn
> Dramdown
> Marin
> Simulation Settings
> 2.31 4.88%2.4814.39%18.72958.999600
> Irstrumen: Tpe
> Equig
> Truncation
> 0.08
> Rezion;
> IN0
> Neutalzaron:
> Mrker
> Unlerse
> TCPSUO
> Dastsurizaon
> Year
> Sharpe
> Turoyer
> Ftress
> Returs
> Drawoown
> Margln
> Cont
> Short Count
> Larauoge;
> Fos  Eprc -lon
> NaN Handlins:
> Decy;
> Urit
> Handlins:
> Verify
> -013
> 5
> 4379
> 290
> 1653%
> 7.87q
> 75,32。
> T
> 113
> Delay
> Wa  Trade
> 201-
> 090
> -5
> 0,63
> 7.3-
> 18,7240
> 32.17930
> 132
> 2015
> 4.75
> 4.394
> 7.05
> 77.619
> 205q
> 125.74260
> 140
> 2016
> 0.63
> 5,199
> 0,37
> 3,799.
> 一189
> 14,6C6s0
> 18
> 13
> Clone Alpha
> 2017
> 4,934
> 394
> 3.18q
> 37.23129
> 18
> 12
> 2013
> 323
> -.914
> 3.93
> 17.959
> 一039
> 74.704
> N Chart
> Pnl
> 2010
> 2O0
> 6,624
> 3.70
> 21.3940
> 41Oq
> 54,519
> 2020
> 5.019
> 1.25
> 9.7995
> 5.369
> 39.064
> 2021
> 360
> 4,714
> 4,43
> 189J
> 29140
> 80-220
> 196
> 7022
> 703
> 4,29%
> 7.01
> 12059
> 3.319
> 55.191.。
> 133
> TON
> 2023
> ~1.52
> 2,02
> ~0,83
> 19m
> 0.69q
> 5620
> 130
> UOOK
> Investability constrained
> ABgregate Data
> Sharpe
> Turnove
> Fmes
> Rerurn
> Drawgown
> Narg
> 1.68
> 3.429
> 1.56
> 10.71%  26.5596  62.569600
> 2015
> 2017
> 2019
> 2021
> 2023
> Pnl
> Investability Constralned Pnl
> Correlation
> Sell Correlaton
> Maxmum
> WNmum
> Lo
> RUI
> Prod Correlation
> MaMUm
> WNMUm
> Last
> Run
> S Testing Status
> Perlod
> 9PASS
> 1FAIL
> Performance Comparison
> RObUSLUNIVerse
> Sharpe Or 0.68
> below CutotOt
> CotRum
> WNRNNC
> 4PENDING
> Properties
> Lt SJled Wed, 11/19/2025,721PM
> Lom9



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_Zscore(tndl7_ttmepsincx,
> 258
> A single Data Sct Alpha
> ABBregate Data
> Sharpe
> Turnoye
> Fn2 s
> Rarun
> Orawoop
> Waret
> Simulation
> Settings
> 2.43 5.78%2.58 14.049 9.45%
> 48.599600
> ISTIIPT
> Tpe
> Equiy
> TICTir
> 0.38
> Rezion;
> IND
> Neuralzaron:
> SCTOT
> Unlerse
> TOPSUO
> Dasturizatlon:
> Year
> Sharpe
> Turoyer
> Ftrss
> Returs
> Drawdown
> Margin
> Count
> Short Count
> Lanauogc;
> Fos  Epres-lon
> NaN Handlins
> Urit
> Hardlins:
> Verfy
> 2013
> 273
> 5.29%
> 3.19
> 47.119
> 5379
> 6.5974
> 145
> Delay
> Wa Trade
> 201-
> 220
> 5,63-0
> 2,29
> 13,5550
> 9-340
> 77,99730
> 133
> 2015
> 61
> 5.154
> 6.73
> 26.665
> 23690
> 103.5160
> 2016
> 1.13
> 6.20
> 0,85
> 6二9
> 3.309
> 20,75230
> 135
> Clone Alpha
> 7017
> 1.73
> 6.069
> 1,37
> 7.8790
> 346q
> 25,98364
> 150
> 2013
> 276
> 5.774
> 3,02
> 14.959
> 1709.
> 51.369
> 176
> Chart
> Pnl
> 2010
> 207
> 7,59u
> 3,87
> 21,2690
> OSq
> 53,33429
> 19
> 14
> 2020
> 1.35
> 5.909
> 1.11
> 8.459
> 13-9
> 23.5524
> 2021
> 293
> 5,37
> 3.,18
> 14,570
> 24740
> 5.2120
> 27
> 19
> TOM
> 2022
> 229
> 1.70
> 40249
> 2949
> 41.94。
> 276
> 137
> 2023
> 2,4b-0
> ~O
> 165h
> 0.6340
> 33,8020
> 273
> 193
> OOOK
> Investability constrained
> ABgregate Data
> SNaroe
> TUTMOII
> FIm25
> C
> Draol0
> 1.70
> 3.86%
> 1.53
> 10.149 15.9296  52.469600
> 2015
> 2017
> 2019
> 2021
> 2023
> Pnl
> Investability Constralned Pnl
> Correlation
> Self Correlation
> Maxmum
> Mnmum
> Los
> RUR
> Prod Correlation
> MaMMUM
> Mnmum
> Las
> Run
> 1S
> Testing Status
> Perlod
> 9PASS
> IFAIL
> Performance Comparison
> RobUSCUnIerse
> Sharpe Or 0.76 Is belo cutotiof
> Last Run
> WARMING
> 4PENDING
> Long
> Deco
> Nr8I


接着尝试探索分组操作符对Robust universe Sharpe的影响，分别利用分组字段market, sector, industry等和pv里面的group类型进行回测，结果发现所有的回测结果Robust universe Sharpe依旧小于1。
注意到该alpha使用时序运算符，决定探索days的增减对alpha的Robust universe Sharpe的影响，把原本的250天变成240,270。结果发现随着days的增加，Robust universe Sharpe逐渐增大，一直到350天，Robust universe Sharpe刚好达标。 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> 75Core
> fndl7_ttmepsincx,
> 240
> Single Data Set Npha
> Simulation Settings
> ISTIIPC
> TPe
> Equig
> Trunca-ion:
> 038
> Rezion;
> IND
> Neuralzanon:
> Irousry
> UnNers=
> TOPSUO
> Dastsurizaon
> Larauogc:
> Fos  Epre -lon
> NaN Handlins:
> Unit Hrdlins:
> Verf
> Dely
> Iax Trade
> Clone Alpha
> N Chart
> PFL
> Correlation
> Self Correlation
> Maxmum
> WNTUM
> LaSI
> Rup
> Prod Correlation
> TaN
> WmUM
> Run
> Performance Comparison
> LastRUT -
> Properties
> Last Saed Wed; 11/19/2025,7-2,PN
> IS Testing Status
> Perlod
> Name
> Category
> Currenlly anonymoUs'
> None
> 9PASS
> Tags
> Color
> IFAIL
> Selectladd TaBs
> None
> RObUSTUnIErs=
> OT0.87I5 below Cutoffof 1.
> WNRNINC
> Description
> 4PENDING
> Descriplion
> Dccaj
> Las
> Sharpe



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_ZSCore(tnd17_ttmepsincx,380
> E Single Data Set Apha
> ABBregate Data
> SharDe
> Turnove
> FIES
> RETUIT
> Oramdow
> Margi
> Simulation Settings
> 2.46  6.00%2.6013.96%10.4296 46.50900
> Irstrumen: Tpe:
> Truncaion:
> 0.08
> Resion;
> IND
> Neutalzanon:
> IngusTy
> UnWErs=
> TOPSOO
> Pastcurizatlon;
> Sharpe
> Turover
> Fitress
> Returs
> Drawdown
> Margln
> Count
> Short Count
> Larauagc:
> Fas  Expres-lon
> Nl Handlns
> Decy:
> Unit Hordlins:
> Verify
> 7013
> 330
> 5.34%
> 4.31
> 71.309
> 44795
> 79.712
> 136
> Dely
> Ia
> Trade:
> 201-
> 5,64
> 1,94
> 12370
> T0 -24
> -3.85
> 1+
> 7015
> 449
> 5.51%
> 6.31
> 7779
> 20
> 39.633
> 145
> 2016
> 6509
> 0,75
> 5.775.
> 6390
> 17 -33
> 142
> Clone Alpha
> 7017
> 13
> 6184
> 0.91
> 6159
> 2 BOI
> 19 90oe
> 148
> 7013
> 320
> GOTI
> 3.73
> 17+2.
> 3.259
> 5735
> 159
> 142
> Chart
> Pnl
> 2019
> 8.114
> 3,35
> 19,119
> 39740
> 4715-
> 150
> 7020
> 6239
> 1+15
> 311
> 3.599
> 26022
> 233
> 219
> 2021
> 343
> 5,43-
> L01
> T600
> 23300
> 5U8Jc
> 202
> TOM
> 702
> 1.60
> 5.06q
> 1.37
> 37
> 3.71q
> 334Tac
> 251
> 2023
> 2.76-0
> 074
> 3,984
> 05340
> 288-0c
> 266
> 189
> DOO
> Investability constrained
> Aggregate Data
> SNaroC
> Turnove
> FNess
> ReLUInS'
> Drawdown
> Margin
> 1.95
> 3.929
> 1.84
> 11.15%  10.7096 56.849600
> 2015
> 2017
> 2019
> 2021
> 2023
> Investabiliy Constralned Pnl
> Correlation
> Sell Correlation
> NMM
> Mmmum
> Last
> Run .
> Prod Correlation
> WaMUM
> Mnmum
> Las
> IS Testing Status
> Perlod
> Run
> 9PASS
> I FAIL
> Performance Comparison
> Robust unlverse Sharpe 01 0.97Is below Cutotfof
> Lost Run:
> WNRNNC
> 4PENDING
> Properties
> Lusr saed Weq 11/19/2025,7.29 PN
> Equiny
> Year
> Long
> Pnl



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> +5_ZSCore
> fndl7_ttmepsincx, 350
> A single Data Set Npha
> ABBregate Data
> Sarqe
> Turnover
> FInsss
> RETUrn
> UaTTI
> Mari
> Simulation Settings
> 2.405.73%2.51 13.71%10.789 47.889600
> Irstrumen: Tpe
> Equig
> Truncation
> 0.08
> Rezion;
> IN0
> Neutalzaron:
> Irausry
> Unlerse
> TCPSUO
> Dastsurizaon
> Year
> Sharpe
> Turoyer
> Ftress
> Returs
> Drawoown
> Margin
> Long Count
> Short Count
> Larauoge;
> Fos  Eprc -lon
> NaN Handlins:
> Decy;
> Urit
> Handlins:
> Verify
> -013
> 3.36
> 5.054
> 4,43
> 21.639
> 46gI
> 357J2a
> 137
> Delay
> Wa  Trade
> 201-
> 1.19
> 5,330
> 1,73
> 11,665
> 107840
> -36_c
> 2015
> 432
> 5.234
> 6.07
> 74.69
> 219N5
> 933333
> 155
> 2016
> 1 41
> 6.324
> 1,03
> 7.309
> 2+990
> 2311oc
> 14
> Clone Alpha
> 2017
> 1.16
> 5954
> 077
> 450
> 2.77
> 19333。
> 149
> 2013
> 3.13
> 5,.674
> 3.65
> 16.975
> 2539
> 59.352
> N Chart
> Pnl
> 2010
> 261
> 7,87
> 317
> 1840
> 405q
> 4579o
> 2020
> 5.939
> 114
> 8.059
> 3.239
> 76957
> 2-0
> 217
> 2021
> 303
> 5115
> 3,35
> 14,799
> 2.3740
> 3795
> 204
> TOA
> 7022
> 1.63
> 4,059
> 1.35
> 3.690
> 3379
> 35312
> 251
> 2023
> 02
> 2,56-
> 0,30
> 219m
> 0.619
> 16-1c
> 257
> OOOK
> Investability constrained
> ABgregate Data
> SNaroe
> TUMION
> Fmes
> RLLII
> Drawdown
> Narg [
> 1.95
> 3.7796
> 1.84
> 11.18%  10.4096 59.379600
> 2015
> 2017
> 2019
> 2021
> 2023
> Pnl
> Investability Constralned Pnl
> Correlation
> Sell Correlaton
> Maxmum
> WNmum
> Lo
> RUI
> Prod Correlation
> MaMUm
> WNMUm
> Last
> Run
> S Testing Status
> Perlod
> 10PASS
> O12.40
> above CULOfTOI 1.58
> Performance Comparison
> FIless Of2.51
> aboye CUtofIOT
> CotRum
> TUrnOVCL 015.7336
> above Cutoffof 19。
> TUrnOVLOT
> 739
> below cutoff of 4096
> lehtis well distribured overinstruments,
> SUb-Unlyerse Sharpe of
> above cutortof0,71。
> RobUstunlerse Sharpe Or
> I5above Cutottol
> year Sharpe O[
> 26 Isabove CUOIfoI 1.58
> Properties
> Luusaved Thu  11/20/2025,1247 AN
> Pyramld theme INDIDTIFUNDAMENTAL matches wlth multpllerof 1.7.Effecve Pyramid
> CountTorGonlusI5
> These themes match with the Tollowlng multpllers; IND Reglon Theme
> Name
> Category
> INDIDTIFUNDAMENTAL Pyramid Theme
> 1.7. The Inal theme multlpller
> 2.7.
> 0.84_1119
> None
> WARNNC
> 4PENDING
> Color
> Selectladd (ags
> None
> Shape
> Tags


最后为了使days更有经济学意义，选取370(一年半)，结果如下：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> +5_ZSCore
> tnd17_ttmepsincx, 370 )
> A single Data Set Npha
> ABBregate Data
> Sarqe
> Turnver
> FItnsss
> RETUrns
> Drawown
> Marin
> Simulation Settings
> 2.385.6492.4913.70910.659 48.639600
> Irstrumen: Tpe
> Equig
> Tryncaior
> 0.08
> Rezion;
> IN0
> Neutalzaron:
> Irausny
> Unlerse
> TCPSUO
> Tastsurizatlon
> Year
> Turoer
> Ftress
> Returs
> Drawdown
> Marqin
> Long Count
> Short Count
> Lorauoge
> Fos  Epres-lon
> NaN Handlins:
> Deca;
> Urit
> Handlins:
> Verf
> -013
> 341
> 4.959
> 4.51
> 21.879
> 471
> 33 1-2a
> 119
> Delay
> Max Trade:
> 201-
> 1.8-
> 5,220
> 1,81
> 12,0850
> 100340
> -62-c
> 2015
> 423
> 5.204
> 5.93
> 74.59
> 2230
> 94312oe
> 155
> 142
> 2016
> 6194
> 1.15
> 7.659.
> 2+99
> 247520c
> 14
> Clone Alpha
> 7017
> 1.15
> 5974
> 076
> 54700
> 2670
> 19633。
> 149
> 2013
> 3.03
> 5,.534
> 3-7
> 16.379
> 2319
> 59.272
> 150
> N Chart
> Pnl
> 2010
> 263
> 7,804
> 321
> 18,650
> 411q
> 4781J
> 2020
> 1.36
> 5.999
> 1,07
> 7.769
> 3.379
> 76357
> 2-0
> 217
> 2021
> 304
> 034
> 3,30
> 14,709
> 2.41q
> 38L
> 24
> 204
> TOA
> 7022
> 1.57
> 4,01%
> 1,29
> 3459
> 4OOq
> 35152-
> 251
> 2023
> 087
> 2.74
> 050
> 2.595
> 0394
> 18 gOoc
> 238
> OOOK
> Investability constrained
> ABgregate Data
> Sharpe
> Turnove
> Fess
> RZIUIII
> Drawdown
> Narg
> 1.95
> 3.729
> 1.85
> 11.23%  10.4996  60.389600
> 2015
> 2017
> 2019
> 202
> 2023
> Pnl
> Investabiliy Constralned Pnl
> Correlation
> Sell Correlation
> Maxmum
> Mnmum
> Lo
> RUR
> Prod Correlation
> Mamum
> Mnimum
> Lagt
> Run
> IS Testing Status
> Perlod
> 10PASS
> O12.38
> above CUOffOf 1.58
> Performance Comparison
> Fless Of2,49
> aboye CUtofIOT
> ColRuu
> TUrnOVCLO
> .0496
> above Cutoffof 19。
> TUrOVLOT
> 6136
> Delow cutoftof40g6
> Ieht
> Well distributed over instruments;
> SUb-unlyerse Sharpe of
> apove cutortof0 ,7
> RobUSCUNIverse Sharpe Or 1,04
> above CUtoItof1。
> year Sharpe Of2.2
> aboye CUtoIIOf
> Properties
> LJn 5vedTnu; 11/20/2025,1.28 AN
> Pyramld theme INDIDTIFUNDAMENTAL matches wlth multpllerof 1.7.Effecve Pyramid
> CountTorGonlusI5
> These themes match with the Tollowlng multpllers; IND Reglon Theme
> Name
> Category
> INDIDTIFUNDAMENTAL Pyramid Theme
> 1.7. The Inaltheme multlolerls 2.7.
> 0.83
> None
> WARNNC
> 4PENDING
> Color
> Selectladd (ag5
> None
> Description
> Descrplion
> Check Submission
> Subilt Alpha
> Sharpe
> Shape
> Tags


---

## 讨论与评论 (2)

### 评论 #1 (作者: JL55804, 时间: 5个月前)

学到了，亲测有用

---

### 评论 #2 (作者: ZC81788, 时间: 11天前)

---
  感谢分享，最近在 IND TOP500 / analyst44（ebitda_latest_actual_date）上一阶模板也撞到 RUS
  不达标的问题，可以补充一组对照数据供大家参考：

我的 baseline（与楼主场景高度类似）：
  - 区域/池：IND / TOP500，delay=1，neutralization=SUBINDUSTRY，truncation=0.08，decay=7
  - 核心算子：group_rank(-ts_arg_max(zscore(winsorize(ts_backfill(vec_max(ebitda_latest_actual_date), 120), std=4)),
  122), densify(sector/market/country/subindustry/industry))
  - Sharpe 1.68–1.74 / Fitness 1.41–1.49 / Sub-Universe Sharpe 0.79–0.90（PASS）
  - LOW_ROBUST_UNIVERSE_SHARPE FAIL：0.51–0.54（阈值 1.0） ← 楼主场景是 0.9，我是更糟的 0.5x 区间

关于楼主的"加大 days"方法：在 ebitda 模板上我也尝试过把 120 扩到 200+，RUS 改善幅度有限（仍在 0.6 附近），可能因为
  fundamental 字段的"信号生命周期"和 ts_arg_max 的回看窗口不在同一量级，单纯拉长时序窗口并不一定能复现楼主的迁移效果。计
  划下一步用"分位数扫描"（110/120/140/170/200）系统跑一次再回帖。

提醒看 ZR19003 佬拼接法的同学：他那篇已明确说拼接对 RUS < 0.7 的 alpha 效果有限，我现在的 0.5x
  区间大概率不适合直接套。需要先把单因子拉过 0.7 再谈拼接。准备先尝试 trade_when 剔除 top 20% cap + 微调 days
  两条路，看能不能先把 0.5x 抬到 0.7+ 再走 ZR19003 的方法。

附：这次逛论坛最直接的收获是发现 ZR19003 那篇——以前一直把 RUS < 0.7
  的直接扔了，现在多了两条候选路径。等我跑出来会在本帖同步结果。

---

---

