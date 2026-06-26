# 【Alpha灵感】Zeta Analysis

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Zeta Analysis_21392182344215.md
- **作者**: TN48752
- **发布时间/热度**: 2 years ago, 得票: 32

## 帖子正文

Paper: Zeta Analysis

Link:  [https://pages.stern.nyu.edu/~ealtman/ZETA-Analysis.pdf](https://pages.stern.nyu.edu/~ealtman/ZETA-Analysis.pdf)

**什么是 Zeta 模型？** 
Zeta 模型是一种数学模型，用于估计上市公司在两年内破产的可能性。 该模型产生的数字称为公司的 Z 分数（或 zeta 分数），被认为是未来破产的合理准确预测指标。

该模型由纽约大学金融学教授爱德华·奥尔特曼 (Edward I. Altman) 于 1968 年发表。 由此产生的 Z 分数使用多个公司收入和资产负债表值来衡量公司的财务健康状况。


> [!NOTE] [图片 OCR 识别内容]
> The Formula for the Zeta Model Is
> 5=1.24+1.48 -3.30' -0.6D -卫
> There:
> 5= Score
> 1 =
> Vorking capital divided by total assets
> retained earnings divided by total assets
> earnilgs before interest and tax divided br total assets
> D = market value of equity dirided by total liabilities
> 卫 = sales divided by total assets


**Zeta 模型告诉您什么？** 
Zeta 模型返回一个数字，即 z 分数（或 zeta 分数），代表公司在未来两年内破产的可能性。 z 分数越低，公司破产的可能性就越大。 Zeta 模型的破产预测准确度范围从破产前一个时期的 95% 以上到之前五个年度报告期间的 70%。
第一的

Z 分数存在于所谓的歧视区，这表明公司破产的可能性。 z分数低于1.8表明有可能破产，而分数大于3.0则表明未来两年不太可能发生破产。 z 分数在 1.8 到 3.0 之间的公司处于灰色地带，破产的可能性很小。

- Z > 2.99 -“Safe” Zones
- 1.81 < Z < 2.99 -“Grey” Zones
- Z < 1.81 -“Distress” Zones

对于私营企业、新兴市场风险和非制造工业等特殊情况，存在不同的 z 分数公式和 zeta 模型。

Zeta模型由纽约大学教授Edward Altman于1968年开发。该模型最初是为上市制造公司设计的。 该模型的后续版本是为控股私营公司、小型企业和非制造业公司以及新兴市场开发的。

我注意到创建因素 A、B、C、D、E 的数据字段都在基本数据集中。然而，在 Brain 上进行测试后，我意识到要使这个模型有效，Zeta 模型必须成为公共 alpha 的触发条件：-ts_delta(close,days)

A = working_capital/assets;

B = retained_earnings/assets;

C = ebitda/assets;

D = equity/liabilities;

E = sales/assets;

S = 1.2*A+1.8*B + 3.0*C + 0.6*D + E;

除此之外，我还需要更改得分函数中的系数以实现可发送的 alpha


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> ?I
> OOO
> OOOK
> 7.0OOK
> OOOK
> OOO
> OOOK
> 3,00OK
> OOO
> OOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022



> [!NOTE] [图片 OCR 识别内容]
> Simulation 308
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USAIDIIILLIQUID_MINVOLIM
> Convert to Multi-Simulation
> LANGUAGE
> INSTRUMENT TYPE
> 2013
> 2014
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILUIQUID_MINVOLIM
> IS Summary
> Period
> TRAIN
> TEST
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Aggregate Data
> Sharps
> TUCNOE
> Frnes
> ReTlrns
> Drawdown
> Marain
> Subindustry
> 008
> 1,55
> 35,5496
> 0,65
> 6,229
> 4,5496
> 3,50900
> Sharpe
> Turnover
> Htnoss
> Returns
> Drawdown
> Marqin
> LoNg Count
> Short Count
> PASTEURIZATION
> UNIT HANDUNG
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> On
> Verify
> Off
> 712
> 33
> 39313
> 123
> 327:
> -3
> 27
> 1
> 2013
> 15
> 3_7:
> 005
> ::
> 334::
> 65
> 454
> 450
> SaVe as Default
> Apply
> 71-
> 233
> 34,57*
> 1.23
> 10 _7:
> 227:
> 05
> 54
> 5-5
> 715
> 3-3:
> 03
> 151:
> -54:
> 3:
> 532
> 577
> Working_capitallassets;
> 2015
> 313:
> 3
> :
> 3,.73
> 23
> 577
> 557
> retained_earnings
> assets;
> ebitdalassets;
> 7017
> 35:
> 031
> 57:
> 37:
> 037
> 571
> equity /liabilities;
> 713
> 33
> 052
> 515:
> 531
> 04
> Sales /assets;
> 5 = 1.214+1.8C
> 2.8C +
> 8.6*0 + E;
> 2019
> 715
> 三04:
> 371:
> 2.731:
> 513
> alpha
> trade_when(5<1.88,
> ts_delta(close,6)-1);
> Broup
> (alpha
> exchange)
> 7020
> 779
> 34,44*
> ~7,13
> 23.33:
> 5
> -16,755
> 220
> 3365
> 3753:
> 354
> 31.55:
> 303
> 16,751:
> 675
> 2021
> 一-5
> 三15:
> 12
> 15,31
> 307
> 335
> 31
> 793
> 7022
> 23,54*
> 23
> 21,73:
> 277:
> -15,235
> 903
> 357
> Qone tis Nphain
> Newtab
> Example
> Simwlate
> Visualization
> udd Aphato
> List
> Oponalpha dotals
> Ret0
> Check Submission
> Submit Alpha
> Voar
> Fank
  
> [!NOTE] [图片 OCR 识别内容]
> Simulation 308
> CODE
> RESULTS
> LEARN
> DATA
> Sattings
> USA/DIIILLIQUID_MINVOLIN
> Conyertto Multi Simulation
> LANGUAGE
> INSTRUMENT TYPE
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Fast Expression
> REGION
> UNIVERSE
> DELAY
> USA
> ILUIQUID_MINVOLIM
> IS Summary
> Period
> TRAIN
> TEST
> NEUTRALIZATION
> DECAY
> AUUICAU
> Aggregate Data
> Sharpe
> LUTMOTeT
> FMESS
> ETUTI
> UF3dCIn
> Narein
> Subindustry
> 008
> 3,05
> 35,53%
> 2,46
> 23,0506
> 3,0996
> 12,972
> Vear
> Sharpe
> TUIIOVeT
> Ftnoss
> Returs
> Dawdown
> Margin
> Count
> Short Cownt
> PASTEURIZATION
> UI
> HANDUNG
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> Verify
> Off
> 2012
> 331
> 39,314
> 12371
> 327:
> -3:
> 一
> 一
> 713
> 13
> 367:
> 005
> 27:
> 3341
> 555
> -54
> -557
> Apply
> 201-
> 3
> -57:
> 1 -
> 2271:
> 05
> 54
> 5-5
> Save as Default
> 2015
> 3-3:
> 055
> 一1:
> 1544
> 35:
> 5
> 577
> working_capitallassets;
> 715
> 053
> 577:
> 373:
> 287
> 57
> retained_earnings
> a5sets;
> ebitda
> assets;
> 2017
> 352:
> 31
> 3.657
> 3,731:
> 037
> 577
> equity/liabilities;
> 2013
> 33
> 0.522
> 515:
> 355
> 314:
> 635
> Sales /assets;
> 5 =1.214+1.8* +2.8+C +0.6*0 + E;
> 11
> 041:
> 3.74:
> 273:
> 3
> 555
> alpha
> trade_when(5<1.88,
> ts_delta(close, 6),-1);
> Broup_
> rank(alpha,exchange)
> 2020
> 7,79
> 34,449
> 713
> 3.33
> 5
> ~16,75
> 7020
> 335
> 37,59*
> 34
> 31.5:
> 33:
> 15,787
> 573
> 7021
> 1-5
> 34,18*
> 12
> 3
> :
> 335
> 307
> 73
> 222
> 2354
> 23
> 21,73:
> 2771:
> -15,2382
> 903
> 351
> Qone this Alphaina neW tab
> Example
> Simwlate
> Visualization
> Add Alphato
> CS
> Open alpha details in new t3b
> Check Submission
> Submit Alpha
> Equlty
> 0o00
> LonO
  
> [!NOTE] [图片 OCR 识别内容]
> Simulation 308
> CODE
> RESULTS
> LEARN
> DATA
> Settings
> USA/DI/ILLIQUID
> MINVOLIN
> Conyertto Multi Simulation
> LANGUAGE
> INSTRUMENT TYPE
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> ILUIQUID_MINVOLIM
> IS Summary
> Period
> TRAIN
> TEST
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Aggregate Data
> Sharpe
> |UrNOE
> FITESs
> KETUFNS
> UF3UCIT
> Warsin
> Subindustry
> 0,03
> 1,93
> 35,5496
> 1,00
> 9,499
> 4,549
> 5,349000
> Vear
> Sharpe
> TUINOVeT
> Ftnoss
> Returs
> Dawdown
> Margin
> Count
> Short Cownt
> PASTEURIZATION
> UNIT HANDLNG
> NAN HANDLING
> TEST PERIOD
> YEARS
> MONTHS
> Verify
> Off
> 2012
> 331
> 3931
> 13:
> 321:
> -3:
> 一
> 一
> 713
> 13
> 367:
> 005
> 27:
> 3341
> 555
> -54
> -557
> Apply
> 201-
> 3
> 34,574
> :
> 227::
> JE
> 54
> 5-5
> SaVe 35 Default
> 3-3:
> 一1:
> 1544
> 35
> working_capitallassets;
> 31:
> 577:
> 373:
> 23
> 557
> retained_earnings
> assets;
> ebitda
> assets;
> 2017
> 352:
> 31
> 6::
> 3.7:
> 03
> 577
> equity/liabilities;
> 2013
> 33
> ::
> 355
> 04o
> Sales
> assets;
> 5 =1.214+1.8*8
> 2.8+C +0.6*0 + E;
> 719
> 11
> 041:
> 3.74:
> 273:
> 513
> 555
> alpha
> trade_when(5<1.88
> ts_delta
> Close,6),-1);
> Broup_rank(alpha,exchange)
> 2020
> -7,79
> 34,449
> 1
> 3.33
> 5
> 15,755
> 54
> 51
> 7020
> 37,59*
> 34
> 31.5:
> 03*
> 3
> 573
> 7021
> 245
> 34,18*
> 12
> 15,34
> :
> 335
> 307
> 73
> 222
> 3,14:
> 723
> ,73:
> 277::
> 15,235
> 903
> 351
> Conetis Nphain a newtab
> Example
> Simwlate
> Visualization
> Add Alphato
> CS
> Oponalohadotals
> new tab
> Check Submission
> Submit Alpha
> LonO


我尝试在前 8 年的训练中只适合 alpha，以获得可以发送的 alpha 版本，然后查看剩余 2 年的 self os 结果。 实现10年都可以提交的alpha要困难得多。 虽然终于可以发送了，但是alpha的prod corr非常高。 我正在考虑如何添加合理的条件或更改 alpha 来减少 corr。

8年来，我一直找不到一个让健身值>1的最佳方法。 不过，剩余2年的自主操作系统成绩非常好，这使得整体alpha可以提交。

我们希望收到老师和朋友关于如何更有效地使用train_test_period功能以及如何优化这个alpha想法的反馈。 另外，我还没有能够有效的使用可视化功能（按行业、行业、覆盖范围进行锐化……），希望得到老师和朋友更多关于这个功能的指导。 非常感谢各位老师、朋友们。

---

## 讨论与评论 (12)

### 评论 #1 (作者: JZ71360, 时间: 2 years ago)

我觉得这个主要还是-ts_delta(close,days) 的作用， 收益inverse的原理，不过这个可能会筛选出投机股，更贴近投机

---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

有个数据直接就是这个的计算 [fnd65_allcap_sedol_altmanz](https://platform.worldquantbrain.com/data/data-sets/fundamental65/data-fields/fnd65_allcap_sedol_altmanz)

---

### 评论 #3 (作者: TN48752, 时间: 2 years ago)


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 02/16/2024 EST
> anonymoUs
> Add Alpha t0
> UISt
> Code
> IS Summary
> Period
> Aggregate Data
> SharOe
> LUTTS2
> TItnES
> RetUTns
> U「3UoIn
> Iarsin
> trade_When
> fnd65_allcap_sedol_altmanz<1.8,ts_delta(close, 6),
> 1,53
> 30,239
> 1,03
> 13,65%
> 5,25%
> 9,03900
> Simulation Settings
> Sharpe
> TuINOVeF
> Ftnoss
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Instrument Type
> Region
> Unmerse
> Language
> Decay
> Delay
> Trwncation
> Neutralization
> Pasteuriation
> NaN Handling
> Unit Handling
> 2712
> DOD
> 000#
> 7,30
> 0,0793
> 7,303
> 000soso
> EqUII
> [5
> TOF3O
> Fast Expression
> 103
> Subndusty
> Vry
> 2313
> 0,00
> OX:
> 0,0301
> ,7
> 0;
> 271-
> DOD
> :
> 0,0793
> 7,303
> 0i
> 2715
> DOD
> 00*
> 7,30
> 0,073
> 7,303
> 000soso
> Clone Alpha
> 2315
> DO0
> 0#
> 0,031
> 0,009
> p
> 2717
> DOD
> 00*
> 0,073
> 7,303
> OOsoso
> Chart
> 2713
> JOD
> :
> 0,0793
> 7,303
> 0i
> Prl
> 2319
> 0,00
> 00#
> ,00N
> ,7
> 0;
> 2720
> DOD
> :
> 0,0793
> 7,303
> 0i
> 2721
> 0,99
> -3
> 3,55
> 7,3703
> 5251
> 一
> 243
> 222
> OOOK
> 272
> 23-
> 1,35
> 73,153
> 3,2593
> 5-3
> 345
> 293
> 7SOK
> SOJK
> Correlation
> Self Correlation
> Hiehest Correlation
> Last Run: .
> 25OK
> Prod Correlation
> Hizhest Correla-ion
> T
> TI:
> 2013
> 2014
> 2015
> 2015
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> Vear


我尝试使用您提供的 data_field，但 alpha 结果存在丢失数据的问题

---

### 评论 #4 (作者: WL13229, 时间: 2 years ago)

不应该直接这样进行使用。使用datafield前，需要了解您的数据。请参考下列方式了解数据后，再进行使用：

[[BRAIN TIPS] 6 ways to quickly evaluate a new dataset – WorldQuant BRAIN]([L2] [BRAIN TIPS] 6 ways to quickly evaluate a new datasetFeatured_11807866133911.md)

---

### 评论 #5 (作者: WL13229, 时间: 2 years ago)

[TN48752](/hc/en-us/profiles/13714359745431-TN48752)

如果方便，可否展示一下，您对 [fnd65_allcap_sedol_altmanz](https://platform.worldquantbrain.com/data/data-sets/fundamental65/data-fields/fnd65_allcap_sedol_altmanz) 此数据的分析结果。根据我之前分享的帖子，您应该可以获得其coverage，frequency，等相关信息。

---

### 评论 #6 (作者: TN48752, 时间: 2 years ago)

亲爱的老师。 我已经计算了数据字段的覆盖率和覆盖率%。 不过对于频率，我不太清楚频率的计算公式，希望大家教教我这个公式。 老师，谢谢


> [!NOTE] [图片 OCR 识别内容]
> Coverage:
> 2157
> Coverage%:
> 0.719



> [!NOTE] [图片 OCR 识别内容]
> Bounds (X-O.5):
> [O,
> 1636。 2857]
> Bounds (X=0.8):
> 1563
> 1984]
> Bounds (Xl):
> 1507
> 1897]
> Bounds
> (X-1.2):
> 1457
> 1831]
> Bounds (X-l.5):
> 1385
> 1738]
> Bounds (X=2):
> [,
> 1256,1567]



> [!NOTE] [图片 OCR 识别内容]
> Median (X=O.1):
> [,
> 1611
> 2855]
> Median (Xl):
> [0,
> 1440,
> 1845]
> Median (X=18):
> 363,
> 438]
> Median (X-l8o):
> 27,31]
> Median (X=1800):
> Median (X-18gg8)
> [0,
> 0,0]



> [!NOTE] [图片 OCR 识别内容]
> Distribution (X=0,8.2):
> [,
> 462,
> 1386]
> Distribution (X-o.2,0.4):
> [O,
> 1250,769]
> Distribution (X=0.4,0.6):
> 3,2]
> Distribution
> (X0.6,0.8):
> Distribution (X=O.8,1):
> [,



> [!NOTE] [图片 OCR 识别内容]
> LkgWKGV
> KkXPgGX
> Rdzoeez
> byogaaq
> DVOgaIR
> 850
> 罡
> 
> 20
> 0,0.2
> 0.2.0.4
> 0.4,0.6
> 0.6,0.8
> 0.8,1
> Ranges



> [!NOTE] [图片 OCR 识别内容]
> i Iist
> [ 'QEZojX'
> bVoALSK
> 7a2090
> IroNzgl
> data_dict
> for
> 1 in range(I,
> 5):
> id_list[i-I]
> df2
> hf.get_alpha_yearly_stats(s,
> alpha
> id-alpha_id )
> Iongcount_list
> df2.IongCount.values.tolist()
> shortCount
> Iist
> df2
> shortCount.Values
> tolist()
> data_dict[alpha_id]
> { 'Longcount
> IongCount_Iist,
> ShortCount
> shortCount_Iist}
> N_values
> [5,
> 22,
> 66,252]
> for
> N_values:
> total_frequency
> for alpha_id,
> data
> in data_dict.items( )
> expression
> f'ts_std_dev(fnd6s_allcap_sedol_altmanz,{N}) !=8 ?1 :0'
> frequency
> 5um(data[ ' LongCount
> data[
> ShortCount' ])
> total_frequency
> frequency
> final_frequency
> total_frequency
> len(data_dict )
> print(f"Final Frequency (N={N}):
> {final_frequency }'
> [47]
> 3.0s
> Final
> Frequency
> (N-5):
> 387.775
> Final Frequency (川-22)
> 88.13068181818183
> Final
> Frequency (N=66):
> 29.37689393939394
> Final Frequency (川=252):
> 693948412698413
> alpha


其实对于频率计算公式，我还是不太明白怎么计算。 我希望你能回答我的问题。

---

### 评论 #7 (作者: WL13229, 时间: 2 years ago)

谢谢你的分享。

- 首先关于频率的计算公式，核心假设在于：一串数列，如果在一段时间内没有变动，那么在这段时间内的标准差，也就是ts_std_dev将为0.因此在这个的计算中，您应该考虑，是哪个N，能使得coverage尽可能地接近该数据的真实coverage，即2157.越接近的N，就是最接近的Frequency。当然，有时候，也不要过于在意在这个计算中coverage小的变动，以某真实coverage为1000的数据字段为例。N=5时，ts_std_dev coverage为500，N=22时，ts_std_dev coverage为502，那么我建议你依然认为，该数据字段的更新频率为weekly而非monthly。仅有当N=22，ts_std_dev coverage为1000左右时，我才觉得你可以采信该数据更新的频率为monthly。
- 接着，回到问题本身，“如何使用这些数据的insight帮助我们进行研究呢”？根据观察，我们可以发现，这个数据字段仅有最后两年有更新，那么前八年，我们可能需要一些别的数据去替代，或者暂时先不使用这个数据参与到我们的Alpha研究。
- 另外，可以看到数值一般都小于10，但是也存在极值。在这些极值中，我们可以有两个方向，a)出现极值的时候，可能是rare case,可以考虑把这个做成一个event alpha.即出现极值的时候再做交易。b)这个极端值可能是一种扰动的信息，我们可以直接先使用winsorize(x, std=4)消除极值。

以上是一些常见的data preprocessing的操作，希望能帮助到你。

---

### 评论 #8 (作者: TN48752, 时间: 2 years ago)

非常感谢老师。 我学到了很多东西。

---

### 评论 #9 (作者: TN48752, 时间: 2 years ago)

老师，再次执行频率函数后，得到这个结果，这个数据就会按日期更新了吧？ 我发现当 X = 5, 22, 66, 252 时，长计数接近 2157 并且变化不大。 希望您能解答我的问题，谢谢老师。


> [!NOTE] [图片 OCR 识别内容]
> Frenquency (X=5):
> [0,
> O, 0
> O,0
> O。1710,
> 2159]
> Frenquency (X=22):
> [0,
> 8。1711。2166]
> Frenquency (X=66):
> [0,
> 1713。2166]
> Frenquency (X=252):
> [0,
> O1715,2171]


---

### 评论 #10 (作者: BC25356, 时间: 2 years ago)

老师，在winsorize(x, std=4)表达式中，为什么std=4？为什么离散程度选择4？可否是3？ 可否是5？还是根据数据的分布来的？

> 
> [!NOTE] [图片 OCR 识别内容]
> Distribution (X=0,8.2):
> [8,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0
> 462,
> 1386]
> Distribution (X-o.2,0.4):
> [0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0
> 0
> 0,
> 1250,
> 769]
> Distribution (X-o.4,0.6):
> [0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 3,
> 2]
> Distribution
> (X-0.6,0.8):
> [0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 8,
> 8,
> 0]
> Distribution (X-o.8,1):
> [0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> 0,
> O,0]
> 0,
> 0,


---

### 评论 #11 (作者: WL13229, 时间: 2 years ago)

[TN48752](/hc/en-us/profiles/13714359745431-TN48752)

是的，可以认为weekly

---

### 评论 #12 (作者: WL13229, 时间: 2 years ago)

[BC25356](/hc/en-us/profiles/13921805253911-BC25356)

这个operator默认的值是4，当然，可以根据您自身需求修改。

---

