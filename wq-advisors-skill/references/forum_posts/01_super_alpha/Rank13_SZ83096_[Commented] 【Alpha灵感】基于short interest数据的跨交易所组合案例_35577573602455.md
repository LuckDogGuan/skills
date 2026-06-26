# 【Alpha灵感】基于short interest数据的跨交易所组合案例

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】基于short interest数据的跨交易所组合案例_35577573602455.md
- **作者**: MY82844
- **发布时间/热度**: 8个月前, 得票: 14

## 帖子正文

**适用数据：shortinterest43 以及 institutions20**

**数据分析：**


> [!NOTE] [图片 OCR 识别内容]
> Feld
> Description
> Type
> shr43_EdBxshVol_SVOI
> SnorVlUME
> Wari
> shr43_bashvol_sVoI
> Snor Valume
> Mazp
> Shr43_baSsHVO
> SUOI
> SorVlUME
> Matrx
> Shr43_EdBxshVOI_otalvolume
> Toral VOluME raded 37the Marke- Center
> Tatr
> shrt43_batsshvo
> TOtEWOIUME
> Total volume traded onthe Markez Cener
> Matrix
> shr43_byochvol_otalVolume
> Total volume traded onthe market center
> Macrik
> Shr43_edgashol_totalvolume
> Total Volume traded onthe marker Center
> Mazrix


观察shortinterest43数据，发现介绍不是很清楚，于是把一些重复的单词bats, byxx, edga和edgx提给AI，让它分析一下，结果发现是CBOE四个子交易所的数据：


> [!NOTE] [图片 OCR 识别内容]
> Alphabetical summary of Cboe's four U.S.equity exchanges (10 Oct 2025 share):
> BZX- 5.81 %
> Cboe's flagship
> BATS" book; high-speed
> I3
> ker-taker; top-tier volume。
> BYX- 0.929
> Inverted-fee (taker-maker) book that pays for liquidity removal。
> EDGA
> 1.01 %
> Neutral-fee, midpoint-friendly venue for directional & routing flow.
> EDGX
> 6.24 %
> Cboe's highest-volume pool; maker-taker; retail-heavy, deep liquidity.
> Cboe-family total
> 13.97 % Of U.S. equity volume


从介绍可以看到，数据集包含了每个子交易所的volume和short volume等数据。

**Alpha构建：** AI提示可以根据short volume to volume ratio构建因子，简单测试之后发现ts_rank()下面表现比较明显，但是turnover比较高，可以考虑例如decay=250进行控制：


> [!NOTE] [图片 OCR 识别内容]
> 5诏
> shrt43_batsshvol_SVOI
> shrt43_batsshvol
> totalvolume;
> ts_rank(s诅, 250)
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteuriatjon
> NaN Handling
> Unit Handling
> Max Tade
> Equity
> 054
> TCP3000
> Fast Erpression
> 250
> 0.005
> Indusy
> Verfy



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> 酏 Sinale Data Set Alpha
> Aggregate Data
> Sharpe
> Turnove
> FrnEss
> ETITnS
> JCaTITO
> Warain
> 1.66
> 3.86%
> 1.08
> 5.3
> 3.359
> 27.479000


**Alpha改进：** 注意到数据集其实包含多个子交易所的信息，所以自然地想到可以通过组合多个子交易所的数据，提升鲁棒性，比如可以组合bats和byxx，或者根据交易量占比组合bats和edgx。

以bats和byxx的组合为例：


> [!NOTE] [图片 OCR 识别内容]
> shnt43_batsshvol_sVOI
> 5hrt43
> byxxshvol_SVOI;
> shrt43_batsshvol
> totalVolume
> shrt43_byxxshvol_totalvolume
> ts_rank (a/b,
> 250)
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> Single Data Set Alpha
> Aggregate Data
> Sharoe
> LUTICNe
> FIMESs
> ECUTI
> OTaWOUn
> Marzin
> 1.72
> 4.299
> 1.16
> 5.6496
> 3.2796
> 26.329000
 确实对表现有所提升，同时可以比对另一种组合方式：


> [!NOTE] [图片 OCR 识别内容]
> shrt43_batsshvol
> 5VOI
> shrt43
> batsshvol_totalvolume;
> shrt43_byxxshvol
> SVOI
> shrt43_byxxshvol_totalvolume;
> pank(a,
> 250)
> ts_rank(b, 250)



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> K Sinale Data Set Alpha
> Aggregate Data
> Sharoe
> LUTMCNe|
> FIMESs
> ECUTI
> OTaWOUn
> Marzin
> 1.76
> 4.149
> 1.20
> 5.8596
> 3.2696
> 28.249000


从表现上来看，第二种组合方式提升更明显。

**其它：**

1. 观察institutions20数据，结构是类似的，上面的方法同样有效。


> [!NOTE] [图片 OCR 识别内容]
> Fel
> Oescription
> TyDe
> instzg_sq_t
> ASSrESEtE reported sha
> VOlume Ofall executed trades during
> Nsr
> tradne hours
> InstzO_I_
> AgSrEgate reported sha
> VolUME OTall executed trades
> Jurins
> Mlap
> tradng hours
> InstzO_y_SeV
> ASSrESECE
> epOIeJshare VOlUME
> EKEcuted shortsalE
> Nsr
> exeTp:trades curins
> tradine hours
> In5220_5q_SeV
> AgSregate reported share volume
> eecured shortSalE
> Mlap
> ExeTP:trades Jurins
> tradine ToUrs
> inst20_59_S
> ASSrESECE
> eported sh
> VOlUME
> EKEcuted shoitSl
> and
> Nsr
> SHOF SE
> ExempraEs
> Jurins
> EBUlartrading RoUrs
> InstZO_I_SV
> AgSregate reported share volume
> execured shortSal
> an
> Mlap
> STOF SEI
> ExeMPraJEs
> Jurins
> ESUlartrading hOUrs
> TeSJIar
> rERUIar
> FEUIC
> rEJJaT


2. AI提示short interst策略有被short squeeze的风险，搜索了一下发现risk60数据似乎可以提供一些度量，但是简单测试发risk60的历史数据比较短，有待进一步比较研究，比如使用trade_when进行仓位控制来规避squeeze的风险。


> [!NOTE] [图片 OCR 识别内容]
> Feld
> Descriptijon
> Type
> rskGO_crowding
> Crowdinsis
> Jaily SCOrE TOr
> shorringand covering activity On
> VEtOT
> The security. Scores Of 7and greater represent significant
> shorineactivity Tor
> Siven dayy. SCOrEs OfS-0
> show norable
> shorting activiqy for
> Siven day. Negative SCOrES rePrESER。
> TSKGO_Jatatime
> Tme JEE
> Vector
> rSKGO_last
> TnE I3s  rate
> the Tnancins rate at Which WE haVe S2enhE
> VETF
> mOSC recent borrowtransaction OCCUF. ThE rate
> qUoteyin
> TSKGO_Ofer
> The Offer rate
> the fnancing
> ErE aC Which
> shor pasi-ion
> Vector
> holder can borrOW
> SE-Urity ThE rate
> qUOedinfee. TnE
> fees are qUOTEJ peranRUM。


3. 在这个数据集上发现tanh(ratio)也有作用，大家有兴趣可以试一下

---

## 讨论与评论 (3)

### 评论 #1 (作者: 顾问 SZ83096 (Rank 13), 时间: 8个月前)

写得很有启发意义，感谢分享

----------------------------------------------------------- 学习，进步 ------------------------------------------------------

---

### 评论 #2 (作者: SZ20589, 时间: 8个月前)

感谢大佬分享，文章内容是通过AI提前筛选对比的数据字段，然后根据这几个模板来比较性能。很不错的手段，比我盲目使用数据字段进行二元回测好太多。给了我很多启示，我唯一担心的是这里的重复的操作符在六维里算不算重复计算了？

祝愿大佬季季GM, VF持久1.0。

=============================================================================

========Genius is one percent inspiration and ninety-nine percent perspiration.=============

==============================================================================

---

### 评论 #3 (作者: MY82844, 时间: 8个月前)

[SZ20589](/hc/en-us/profiles/33432836706711-SZ20589)  这个操作确实字段数和运算符数比较大，看怎么取舍了...

---

