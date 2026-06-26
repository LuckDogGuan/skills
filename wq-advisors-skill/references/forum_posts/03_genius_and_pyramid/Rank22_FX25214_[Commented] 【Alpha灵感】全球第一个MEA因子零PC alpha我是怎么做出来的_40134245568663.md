# 【Alpha灵感】全球第一个MEA因子（零PC alpha），我是怎么做出来的？

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】全球第一个MEA因子零PC alpha我是怎么做出来的_40134245568663.md
- **作者**: JL76306
- **发布时间/热度**: 1个月前, 得票: 11

## 帖子正文

半夜做因子的时候发现新开了一个MEA地区，考虑到低PC高奖赏原则于是开始了因子设计。


> [!NOTE] [图片 OCR 识别内容]
> Prod
> Correlation
> ee >
> 0.00
 
（先上镇楼 PC0.00 图）

### PART1：了解现有情况计划对策

MEA开始的时候，我发现在data集合里面搜索为空，应该是接口也未开没办法直接用程序批量回测。

那下一个，就是得测试一下这个地区是不是可以开始制作？
于是，我用了最简单的adv20，发现不存在，但是！data输入时下拉展示列表存在可用data展示。进行回测，进度条可以到35%说明该地区真实打开！


> [!NOTE] [图片 OCR 识别内容]
> Settings
> MEA/DI/TOP300
> Comy
> Streak: 340day
> adv
> aVB_daily_dollar_volume_Zod
> avg_daily_dollar_volume_2Od
> 0 avg_daily_dollar_volume_God
> daily_dollar_volume_ten_day
> Type: Matrx Price Volume
> aVB_daily_Volume_I2Od
> aVB_daily_volume_2Od
> The average dailytrading Value in USD over the
> aVg_daily_volume_25Od
> past 20 days for securities inthe 'MEA_Uber
> daily_Volume_4Od
> universe.It is calculated as the Z0-day average
> aVB_daily_Volume_Sd
> Volume multiplied by
> reference price。
> aVB_daily_Volume_GOd
> 3 aVB_daily_volume_fifty_day
> average_daily_volume_GOd
> average_daily_Volume_63_days
> a+
> a+


OK，总结现有情况：MEA地区可做、MEA data仅可通过熟悉字段输入在下拉中选择。

结合现有情况，那么或许应该去做模板因子，特别是， **有特定data选择** 、 **有经济学含义的因子模板** ！
（ps：还有另一个好处，开点新地区确实冒险所以有经济学含义的话会稳一点）

### PART2:站在前人的肩膀上前进！

由于我不是经济学出身也想不起来啥关键字，于是，我去问ai有哪些经济学关键字眼合适做底层data来做因子。拿到一批关键词后，我开始去论坛进行搜索相关文章（因子模板）。

发现了，金矿！

【Alpha模板】标准化盈利意外-SUE因子2：升级篇--全市场！！横向无痛点塔 Anl、Fnd（附模板） [[L2] 【Alpha模板】标准化盈利意外-SUE因子2升级篇--全市场横向无痛点塔 AnlFnd附模板Alpha Template_35837735141015.md]([L2] 【Alpha模板】标准化盈利意外-SUE因子2升级篇--全市场横向无痛点塔 AnlFnd附模板Alpha Template_35837735141015.md)

JY35107大佬曾提供一个构建的基于eps data的SUE因子，看起来非常有具体含义，，且大家点赞颇高，大佬研究真的很精深，再次感谢大佬，大家也请多为他点赞！！！

于是我开始了测试，按照模板填写，选了一个综合性最强的eps data填入，，，
成功就这样出现了，，，，


> [!NOTE] [图片 OCR 识别内容]
> 屉 Correlation
> Self Correlation
> Haximum
> IITMUM
> Last Run: Fr, 05/91/2026,12-50 J
> Power Pool Correlation
> Haximum
> IITMUM
> Last Run: Fr, 05/91/2026,12-49 J
> Prod Correlation
> IT
> NIimUM
> Last Run: Fr; 05/01/2026,12.20-
> ThE  3re nC
> proo-Correlated alphzs。
> IS Testing Status
> 8P4SS
> Sharpe of 2.17is above CUtoff of
> FitnEss Of 2.33
> EbVE CUOff 3
> TurnoVerof 2.709
> 3bOVe Cutoffcf 1%
> TurOEFOf 27036
> beow CUtOffof 7096_
> Ieightis WeI
> listribued C ins-rmEnts
> SUb-Uie SE Sharpe Of 2.1415 EbJVE ~UTOff J 1.33
> 2jearSharpe cf 1.89
> aDOVE ~UOff Of 1.58
> Pyramid theme MENDIIPV marches With multiplier af 2.Effective Pyramid count for Genius
> NARNING
> PENDING


传说中的前无古人因子，，，


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_decay_linear(ts
> av_diff
> 120)/ts_std_dei
> 25211252)
> 酡 Single Data Ser Alpha
> m Power Pool Alpna
> 酡 Regular Alpha
> Pyramid teme- MENDTIPV X
> ABgregate Data
> Thz
> TICCC
> Fitne
> ReTrlTn
> Ur
> Marein
> Simulation Settings
> 2.17
> 2.70%
> 2.33
> 14.36%
> 9.26%
> 106.3
> 9000
> Instrument Type
> Region
> Unwerse
> Langwage
> Decay
> Delay
> Truncation
> N-utralization
> Pasteurizalion
> Loohback
> MaxTrade
> Max Positon
> EquIt
> WEA
> TCF3JO
> Fast Excression
> 0.35
> Wrkst
> Vear
> Shampe
> Tumower
> Ftness
> Returs
> Drawdown
> Margin
> Long Cownt
> Short Count
> 2014
> Z.15
> 一239
> 2.73
> Ss
> 3.2535
> 93.225:
> 2015
> 59:
> 0.57
> 4.53汩
> 一33
> 33.31t:
> 143
> ?06
> 1.32
> 2.619
> 8.21汩
> 1.33
> 67.525
> Clone Alpha
> 2017
> 2.34
> 539
> 15.345
> 7.3235
> 149.725:
> 140
> 201
> 一-
> 15.3E
> 一0235
> 130.555:
> N Chart
> PIL
> 2015
> 2.52
> 2379
> 2.5
> 13.15汩
> 2.913
> 111.485:
> 143
> 2020
> 539
> S.FE污
> 一73
> 75.375:
> 13
> 202
> 4.31
> 2439
> Ee
> 25.73汩
> 3.66%
> 233.355.
> 2022
> T
> 539
> 2.3
> 13.5汩
> 2.193
> 104.735:
> 142
> TON
> 2023
> 559:
> 8.12汩
> 3.613
> 63.31汩:
> 143
> 07122'2019
> PnL 7,327.42k
> OOJK
> Investability constrained
> Aggregate Data
> Sharp
> TUFnO
> iTe
> RaITns
> T
> Wsrain
> 1.83
> 2.53%
> 1.83
> 12.46%
> 9.1
> 98.729000
> Jul"14
> Jul"15
> J1"16
> J1"17
> J41'13
> Jul'19
> J41'20
> JUI'21
> J1'22
> JUl'23
> 医 Correlation
> Self Correlatlon
> TsmUT
> Mpimum
> ICTFI
> PoWeF Pool Correlation
> TsmUT
> Mpimum
> ICTFI
> IS Testing Status
> Period
> Prod Correlation
> IHMUIT
> TNIMUM
> Last Run; Fr, 05/01/2026,12-53 A
> 8 PASS


点击，提交。

看到PC 0的那一刻，我知道，我成了。

以上思路，希望可以帮助到大家！

也再次感谢JY大佬！感谢社区的开源精神！期待大家也能挖到低相关性的好因子！

---

## 讨论与评论 (9)

### 评论 #1 (作者: 顾问 RM49262 (Rank 30), 时间: 1个月前)

=====================================评论区====================================

恭喜大佬  这下真成第一个吃螃蟹的人了

好奇prod corr 0的话base pay能给多少

=============================================================================

---

### 评论 #2 (作者: SL19872, 时间: 1个月前)

我交了几个PC0.2左右的

---

### 评论 #3 (作者: MY82844, 时间: 1个月前)

太强了！

看了下，turnover非常低margin非常高，ts_decaly_linear(*,252)是什么考量，为了压低turnover吗？

=======================================================================

Pain + Reflection + Observation = Progress

=======================================================================

---

### 评论 #4 (作者: YX86102, 时间: 1个月前)

果然是第一个提交的，PC为0，坐等PC0的因子base是多少哈哈哈哈哈

---

### 评论 #5 (作者: XX27743, 时间: 1个月前)

试了下profit/size的模板，sharpe始终差一点，weight distribution经常》50%。。。。

---

### 评论 #6 (作者: XW23690, 时间: 1个月前)

早起的鸟儿有虫吃，pc为0估计能吃满base了吧！

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #7 (作者: 顾问 SC23342 (Rank 23), 时间: 1个月前)

数据字段下拉列表实际上需要等一段时间，等到字段闪烁一下，这个时候列表显示的才是真正的可用字段，你可能只是刚好选中了这个region也有的字段。这个似乎不是网络原因，有时候突然还会再闪一下，字段就变成一直是白色的，然后列表完全用不了……网页的这个问题还是有点恼人的

================================泰山哥布林 DJ泰哥儿====================================

---

### 评论 #8 (作者: 顾问 FX25214 (Rank 22), 时间: 1个月前)

佬真的厉害！ 您的行为让我有一种第一个吃螃蟹的人的感觉。
这是多么值得赞扬的探险家精神！
我是一个相对而言不是很倾向于开新地区的顾问，一般都是等新地区开了之后大家有了cb的反馈我才会开。相比之下，我显得格外的胆小了。
希望有朝一日我也能找到像佬这样大胆做因子的自信！
------------------------------------------------来自传奇耐打王的点赞-----------------------------------------------------------------------

---

### 评论 #9 (作者: FF65210, 时间: 1个月前)

感谢大佬分享，好奇佬能吃多少base。

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

