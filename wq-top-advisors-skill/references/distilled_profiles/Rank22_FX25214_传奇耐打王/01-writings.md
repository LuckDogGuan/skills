# 顾问 FX25214 (传奇耐打王/耐打王) (Rank 22) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 FX25214 (传奇耐打王/耐打王) (Rank 22) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: 0帧起手的字段构建【传奇耐打王系列三】经验分享
- **主帖链接**: 0帧起手的字段构建【传奇耐打王系列三】经验分享.md
- **讨论数**: 9

继上文讲了模版是怎么来的，本文我们就来思考这个0阶的字段，需要我们进行怎么样的思考呢？首先，我一直都对用户阶段的课程的录播中 weijie 老师的一句话印象十分深刻：Liabilities 单独回测没有信号，为什么 libilities / assets 就有信号了呢？因为大公司的负债天然的比小公司的多，如果直接对比公司负债的差异，那很多小公司实际是会被直接忽略的。但是我们用公司资产作为分母，就把这个公司规模对负债的影响给消除了，这个比率使得一整个组合字段具有了可比性。注意，这个可比性是非常重要的。我看到一篇非常好的文章介绍爽字段是怎么构建的，但我们一定要知道这么构建的内涵是什么。比如刚刚举的比率的例子，就是去除公司量纲对我们想要对比的对象的天然影响。但比率能做的事情可完全不止这些。现在让我以这个为基础带你们一起思考一下。既然有公司的负债可以被考虑，那是不是公司的利润也可以被考虑？公司利润/公司资产，这样的新比率就应运而生了。那我相信聪明的人已经开始举一反三，那我还可以考虑的点有很多，围绕公司的各类指标我都来一遍，我相信这完全没问题。更有聪明的人想到，分子可以变，分母也可以变，我要想办法去除量纲问题，我用公司的市值行不行呢？公司的人数行不行呢？基于这些，往往已经产生了大量的字段构建了。那我们想做出差异化的东西，我们就应该学会寻找共性和个性。刚刚的第1点的共性是什么呢？我想是很明显的 a / b 的形式。那能不能在这个基础上稍微做一点衍生？(a + c) / b 可以吗？(a - c) / b 可以吗？比如我是（（公司利润 - 公司负债）/公司资产），这是不是又产生了一个新的构造呢？那分子变了，分母是不是也可以变？(a + c) / (b + d)，这样的可以吗？答案是肯定的。现在我们再针对这个字段本身做一个深度的思考。假设我就要 公司利润/公司资产 这个形式呢？OK没问题。公司利润是什么？公司利润是公司收入减去公司成本。这个和第2点不同的地方在于。我不是由 a 变成 a + b，而是由 b - c 来刻画 a。目标字段不变，我通过另外一种方式找到他。这是最直接的。那我们有没有思考，什么可以反映公司利润？我们能直接的做出来，那能不能间接的窥探到呢？这里我用的是网页版腾讯元宝，绝对免费绝对方便绝对好复刻实操。元宝就告诉我负面的新闻或者情绪大概率领先于基本面的下调。我的第一反应是什么？赶紧去 news 或者 sentiment 里找对应的字段配合 if_else 做分子，分母不变。新的构建又出现了。我希望大家多多关注点塔王，点塔王利用大模型将很多字段的相似字段进行了总结。这里有什么作用呢？既然有基本面数据，那分析师数据是否可以做相应的替换？综上所述，我们已经从一个最简单的 a / b，走向了千千万万种不同的构造了。可最简单的完全不止 a / b，你知道的，在那篇优秀的文章中已经列出了非常多最简单的构造了。你真的还会害怕出不了因子吗？我的顾问朋友们？

---

### 帖子 #2: 0帧起手的字段构建【传奇耐打王系列三】经验分享
- **主帖链接**: https://support.worldquantbrain.com0帧起手的字段构建【传奇耐打王系列三】经验分享_40760257415959.md
- **讨论数**: 9

继上文讲了模版是怎么来的，本文我们就来思考这个0阶的字段，需要我们进行怎么样的思考呢？

首先，我一直都对用户阶段的课程的录播中 weijie 老师的一句话印象十分深刻：

Liabilities 单独回测没有信号，为什么 libilities / assets 就有信号了呢？

因为大公司的负债天然的比小公司的多，如果直接对比公司负债的差异，那很多小公司实际是会被直接忽略的。但是我们用公司资产作为分母，就把这个公司规模对负债的影响给消除了，这个比率使得一整个组合字段具有了可比性。

注意，这个可比性是非常重要的。我看到一篇非常好的文章介绍爽字段是怎么构建的，但我们一定要知道这么构建的内涵是什么。比如刚刚举的比率的例子，就是去除公司量纲对我们想要对比的对象的天然影响。但比率能做的事情可完全不止这些。现在让我以这个为基础带你们一起思考一下。

- 既然有公司的负债可以被考虑，那是不是公司的利润也可以被考虑？

公司利润/公司资产，这样的新比率就应运而生了。

那我相信聪明的人已经开始举一反三，那我还可以考虑的点有很多，围绕公司的各类指标我都来一遍，我相信这完全没问题。更有聪明的人想到，分子可以变，分母也可以变，我要想办法去除量纲问题，我用公司的市值行不行呢？公司的人数行不行呢？基于这些，往往已经产生了大量的字段构建了。

- 那我们想做出差异化的东西，我们就应该学会寻找共性和个性。刚刚的第1点的共性是什么呢？我想是很明显的 a / b 的形式。那能不能在这个基础上稍微做一点衍生？(a + c) / b 可以吗？(a - c) / b 可以吗？比如我是（（公司利润 - 公司负债）/公司资产），这是不是又产生了一个新的构造呢？那分子变了，分母是不是也可以变？(a + c) / (b + d)，这样的可以吗？

答案是肯定的。

- 现在我们再针对这个字段本身做一个深度的思考。假设我就要 公司利润/公司资产 这个形式呢？OK没问题。公司利润是什么？公司利润是公司收入减去公司成本。这个和第2点不同的地方在于。我不是由 a 变成 a + b，而是由 b - c 来刻画 a。目标字段不变，我通过另外一种方式找到他。这是最直接的。
- 那我们有没有思考，什么可以反映公司利润？我们能直接的做出来，那能不能间接的窥探到呢？


> [!NOTE] [图片 OCR 识别内容]
> T CTHLLTr 5^TULJLTSCLo
> ?U
> ImmlA
> UTTN
> TCATINT=胃7T2N5U9T
> 工TCLLICLI LUITAI II4NI BMNDLTU
> USTNNEu
> Tl7T
> aW Lp yA?1切 @兀t止)L%
> J71NOTNes'
> ITaS
> URL
> TTN
> IITe
> L
> _
> [UnaSU3 )
> TT7Si SUlt丕
> To+ ~
> ANM
> muy
> 444.4SNITTT TUiTI!895n
> IAt=U


这里我用的是网页版腾讯元宝，绝对免费绝对方便绝对好复刻实操。

元宝就告诉我负面的新闻或者情绪大概率领先于基本面的下调。

我的第一反应是什么？赶紧去 news 或者 sentiment 里找对应的字段配合 if_else 做分子，分母不变。新的构建又出现了。

- 我希望大家多多关注点塔王，点塔王利用大模型将很多字段的相似字段进行了总结。这里有什么作用呢？既然有基本面数据，那分析师数据是否可以做相应的替换？

综上所述，我们已经从一个最简单的 a / b，走向了千千万万种不同的构造了。可最简单的完全不止 a / b，你知道的，在那篇优秀的文章中已经列出了非常多最简单的构造了。

你真的还会害怕出不了因子吗？我的顾问朋友们？

---

### 帖子 #3: OS更新后对于“这个因子到底能不能交”的一点思考 【传奇耐打王系列一】经验分享
- **主帖链接**: OS更新后对于这个因子到底能不能交的一点思考 【传奇耐打王系列一】经验分享.md
- **讨论数**: 9

首先，一年的OS不能代表什么，OS差的朋友们不需要焦虑，好的也不要太过开心。但从这一年的OS，总是可以帮我们提高对于因子是否可以提交的认知。接下来我将用几个我自己认为非常有趣的因子来跟大家做出分享。因子一：这是我在USA的inst18做的一个ra。不得不说这个因子在我做出来的时候，我的反应应该和大家的是一样的，这不就是一个妥妥的厂吗？pnl的平滑是根本谈不上了。而且这个因子的表现靠的就是前几年堆起来的。那为什么我当时会交这个因子呢？以下是我的几点原因：这个因子我用了四个字段，但依旧是atom。我是通过对inst18进行适当的分析得出的这个比率只差的组合。因此经济学含义上我认为说得通这个因子只有19和20两年不行，其余均符合要求，包括我说的整体和最后两年，且最后两年抬头。在我自己提出的标准上，除了pnl不平滑之外，我认为它还是值得去信任的。这个因子的换手率和收益率出现在了让我非常信任的数值范围基于以上这三点，我还是咬咬牙把这个因子交上去了。不得不说，确实带有赌的成分。当时也考虑着，就算是过拟合，起码也帮我点了四个字段。没想到出来的OS竟然这么的平滑，有些超乎我的预料。接下来我们看例子二：这个是我一个朋友提交的因子。我本人并未提交。当时我俩基于这个因子展开讨论。我认为这个因子的turnover太高而margin太低。加上这个因子样本内表现趋于稳定，交上去可能会稳定的亏钱。最后他提交了我没有提交。但没有想到这个因子在23年年初出现了跃变，并在后续继续保持了稳定，使得全年的return大幅度的抬升了。从这个角度来看，这个因子的的确确赚了不少的钱。但在这里我们要想两个问题：我们观察到年初后这个因子的pnl曲线又与之前的斜率相差无几。那这个因子在24年还能再次迎来跃变吗？25年呢？如果不能跃变的话。这个因子稳定的抬升就会把它23年赚的钱再次亏掉从整体的提交因子的角度而言。是否样本内margin不达标就意味着因子不赚钱呢？从这个例子上我们看到了否定的答案。但是换做我，我应该还是不会提交这个因子。平稳的不赚钱在我的视角里，还是比不上波动的赚钱。像这个因子以这样的方式赚钱的概率实在是太小了既然有了前者，那我们就来看一个波动赚钱的例子。也是这样的因子，让我体会到了wqb对于小而美的追求是有多么重要：这个因子是在我去年刚刚成为顾问提交的，7月20日。那时候我年少无知，还没有形成自己的一套提交的体系，看到这个亮了，哐哐哐想着把margin搞高点，把decay拉菲。包括那时候还不知道看22年表现。这玩意pc0.7。要换到现在，我也是不会提交的。我只记得当时觉得这条线看起来还算平，波动的平。整体不会有大起大落。同时，这还不是atom。这是三个操作符两个字段，跨数据集比率因子。比率来源于weijie老师的一个推荐字段的帖子。但从这个OS来看，这个因子完全展示了它样本外起飞的能力。要是我不刻意拉低换手率而是保持一个基本的换手率，那这会是一个非常美丽的赚钱的因子。对于拥有这样的OS的因子，我称它为样本外的superalpha。那这里值得我们讨论的问题是什么呢？我看到有不少的顾问会给自己设限。比如sharpe低于多少的ppa不交，fitness低于多少的ppa不交。但单看这个因子，sharpe和fitness真的非常的普通。再举个例子：这个也是比率因子，一样的操作符数量和字段数量。但你能说这个sharpe和fitness很好吗？我看未必。这两个因子具体的表达式我就不展示了，举例来说类似于：ts_mean(ts_quantile(a/b ,d1), d2)为什么我当时看了冷神的丑苹果理论大有感触？冷神说的好，长得好看的苹果吃起来不一定甜。但满身疙瘩的苹果说不定甜在嘴里。这两个因子的sharpe和fitness真的很一般，但是它俩的OS/IS ratio在我119个asi的ra中排名第一和第二。这里我不禁想起一位大佬曾经跟我说的。他只做ppa，信号达标就交了。虽然这样的说法未免有失偏颇。但小而美的因子确实证明了他们存在的硬实力。这样的因子毫无疑问，对于你的vf和combine都是加分项。这里提醒了我对于ppa存在的意义。ppa本身的设定就是为了寻找纯粹、简单的信号。这个纯粹二字，其实是相当重要的。因此ppa才没有那么高的提交要求。但这不意味着我们利用这个ppa的规则去混因子。怎么样把小而美的优势充分的在ppa上体现出来，是真正值得我们学习和思考的地方。因此，回到我之前的帖子说的多样性。小的数据集只能做出质量一般的ppa怎么办？别害怕！大胆做！大胆交！把小而美做出来！你怎么知道它不是样本外的superalpha呢？本期分享就到这里，希望对各位同好们的因子提交有一定的借鉴意义。最后祝大家vf1.0，早日gm。这个赛季我们顶峰相见。

---

### 帖子 #4: OS更新后对于“这个因子到底能不能交”的一点思考 【传奇耐打王系列一】经验分享
- **主帖链接**: https://support.worldquantbrain.comOS更新后对于这个因子到底能不能交的一点思考 【传奇耐打王系列一】经验分享_38182883500055.md
- **讨论数**: 9

首先，一年的OS不能代表什么，OS差的朋友们不需要焦虑，好的也不要太过开心。但从这一年的OS，总是可以帮我们提高对于因子是否可以提交的认知。接下来我将用几个我自己认为非常有趣的因子来跟大家做出分享。

因子一：


> [!NOTE] [图片 OCR 识别内容]
> 300+391
> -mah
> FFJLTAR TI
> LTJII
> TANNIT
> IMrI o+l
> Cooe
> 15 Summar
> o TTUIOII1
> 24:
> SLT
> 412420
> UTMIS4n
> ULJUTTJTa
> RhemIMCTINSTITIITIS
> (
> NTINTICUTN
> SII
> 10.98
> 13.45*
> 7.119
> 24.5150
> Uafeo
> 44197
> Tak
> Fra
> U 
> 7T476
> ICIA
> EIAst
> Sea
> Cona AIao
> Chart
> I eslaLIII' Lonslralne
> UULIO]
> 2.46
> 90?g
> 吕675
> T eCh
> 19.11#
> 卫 Correltion
> prrl


这是我在USA的inst18做的一个ra。不得不说这个因子在我做出来的时候，我的反应应该和大家的是一样的，这不就是一个妥妥的厂吗？pnl的平滑是根本谈不上了。而且这个因子的表现靠的就是前几年堆起来的。那为什么我当时会交这个因子呢？以下是我的几点原因：

- 这个因子我用了四个字段，但依旧是atom。我是通过对inst18进行适当的分析得出的这个比率只差的组合。因此经济学含义上我认为说得通
- 这个因子只有19和20两年不行，其余均符合要求，包括我说的整体和最后两年，且最后两年抬头。在我自己提出的标准上，除了pnl不平滑之外，我认为它还是值得去信任的。
- 这个因子的换手率和收益率出现在了让我非常信任的数值范围

基于以上这三点，我还是咬咬牙把这个因子交上去了。不得不说，确实带有赌的成分。当时也考虑着，就算是过拟合，起码也帮我点了四个字段。没想到出来的OS竟然这么的平滑，有些超乎我的预料。

接下来我们看例子二：


> [!NOTE] [图片 OCR 识别内容]
> IMINIImATII ^
> TUIIII
> L
> Tc
> NCUTLOAI
> 221
> 32504
> 1,90
> T0-0
> 8594
> 105m
> ng(
> Co | eoo
> Clwmm Ao
> Cart


这个是我一个朋友提交的因子。我本人并未提交。当时我俩基于这个因子展开讨论。我认为这个因子的turnover太高而margin太低。加上这个因子样本内表现趋于稳定，交上去可能会稳定的亏钱。最后他提交了我没有提交。但没有想到这个因子在23年年初出现了跃变，并在后续继续保持了稳定，使得全年的return大幅度的抬升了。从这个角度来看，这个因子的的确确赚了不少的钱。但在这里我们要想两个问题：

1. 我们观察到年初后这个因子的pnl曲线又与之前的斜率相差无几。那这个因子在24年还能再次迎来跃变吗？25年呢？如果不能跃变的话。这个因子稳定的抬升就会把它23年赚的钱再次亏掉
2. 从整体的提交因子的角度而言。是否样本内margin不达标就意味着因子不赚钱呢？从这个例子上我们看到了否定的答案。但是换做我，我应该还是不会提交这个因子。平稳的不赚钱在我的视角里，还是比不上波动的赚钱。像这个因子以这样的方式赚钱的概率实在是太小了

既然有了前者，那我们就来看一个波动赚钱的例子。也是这样的因子，让我体会到了wqb对于小而美的追求是有多么重要：


> [!NOTE] [图片 OCR 识别内容]
> UUTIULIO]
> SINUIaCIOJ Seins
> 08s
> 0
> 5,643
> 5423
> 104,31
> 4111
> LT
> 
> 47812110
> I
> LACT1[
> Ca9
> 5
> II 552
> Cne Alal
> Chart
>  =1
> J
> T 7
> Correlation
> LULUITIL


这个因子是在我去年刚刚成为顾问提交的，7月20日。那时候我年少无知，还没有形成自己的一套提交的体系，看到这个亮了，哐哐哐想着把margin搞高点，把decay拉菲。包括那时候还不知道看22年表现。这玩意pc0.7。要换到现在，我也是不会提交的。我只记得当时觉得这条线看起来还算平，波动的平。整体不会有大起大落。

同时，这还不是atom。这是三个操作符两个字段，跨数据集比率因子。比率来源于weijie老师的一个推荐字段的帖子。

但从这个OS来看，这个因子完全展示了它样本外起飞的能力。要是我不刻意拉低换手率而是保持一个基本的换手率，那这会是一个非常美丽的赚钱的因子。对于拥有这样的OS的因子，我称它为样本外的superalpha。

那这里值得我们讨论的问题是什么呢？我看到有不少的顾问会给自己设限。比如sharpe低于多少的ppa不交，fitness低于多少的ppa不交。但单看这个因子，sharpe和fitness真的非常的普通。

再举个例子：


> [!NOTE] [图片 OCR 识别内容]
> Lunsg
> TNC
> 01-
> UTLUTAAAI
> [e1T
> d
> HNIIII
> CNRs
> Arrrctotr 0
> 569
> 0.93
> 6.3T3
> 7.21沾
> 99.319o
> oT
> [
> gg
> T
> n
> 2(
> NaHarel
> W
>  HTTSf
> UIIT
> 7191+
> 8
> 
> n
> 。
> T
> U4 E1
> 1
> 11771
> 13105
> Chart
> 
> Correlation
> CmTr
> CTTMlac
> ULAUT
> 05 Testing Status
> INLTTCIICN
> 11TFMITIAIC
> Properties
> 0 +0
> CUary
> e
> os


这个也是比率因子，一样的操作符数量和字段数量。

但你能说这个sharpe和fitness很好吗？我看未必。

这两个因子具体的表达式我就不展示了，举例来说类似于：

ts_mean(ts_quantile(a/b ,d1), d2)

为什么我当时看了冷神的丑苹果理论大有感触？冷神说的好，长得好看的苹果吃起来不一定甜。但满身疙瘩的苹果说不定甜在嘴里。这两个因子的sharpe和fitness真的很一般，但是它俩的OS/IS ratio在我119个asi的ra中排名第一和第二。这里我不禁想起一位大佬曾经跟我说的。他只做ppa，信号达标就交了。虽然这样的说法未免有失偏颇。但小而美的因子确实证明了他们存在的硬实力。这样的因子毫无疑问，对于你的vf和combine都是加分项。

这里提醒了我对于ppa存在的意义。ppa本身的设定就是为了寻找纯粹、简单的信号。这个纯粹二字，其实是相当重要的。因此ppa才没有那么高的提交要求。但这不意味着我们利用这个ppa的规则去混因子。怎么样把小而美的优势充分的在ppa上体现出来，是真正值得我们学习和思考的地方。

因此，回到我之前的帖子说的多样性。小的数据集只能做出质量一般的ppa怎么办？别害怕！大胆做！大胆交！把小而美做出来！你怎么知道它不是样本外的superalpha呢？

本期分享就到这里，希望对各位同好们的因子提交有一定的借鉴意义。

最后祝大家vf1.0，早日gm。这个赛季我们顶峰相见。

---

### 帖子 #5: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] agent时代对expression ast的一个大更新_38291391911575.md
- **讨论数**: 6

虽然单用agent做长流程的任务非常不可靠, 但是的确为一次性的任务提供了很多便捷. 有了agent后, 我的工作流程也从 手动(一次性任务) | 写代码(重复任务) 的两个选项, 变成了 手动(一次性任务) | agent(一次性简单任务) | 写代码(重复任务) 的三个选项, 这日子是越过越好了.

关于验证表达式合法性, 尤其是参数个数和参数类型匹配, 本来只有两种处理方法:

1. 我自己手动写了一些规则, 比如vector, group的用法(难以周全难以维护)

2. 从平台的文档中提取每个operator的参数用法(文档不完善不可靠)

但是因为有了agent, 现在有了第三种方法

3.  **通过平台feedback更新一份完善的包含所有operator参数规则的文档(容易维护, 完美的方案)**

**
> [!NOTE] [图片 OCR 识别内容]
> # Generated
> struct With detailed argument
> info
> OPERATOR METADATA
> abs
> args
> [
> default'
> None,
> mandatory
> Truey
> name
> X'
> type
> MATRIX'}]
> category
> Arithmetic'
> is_variadic': Falsey
> max_args
> 1 
> min_args
> 1,
> return_type
> 'MATRIX
> add'
> args'
> default '
> None
> mandatory
> True,
> name
> X'
> type
> MATRIX'},
> default' :
> None
> mandatory
> True,
> name
> y'
> type
> MATRIX'},
> default'
> false
> mandatory'
> False
> name
> filter
> type
> SCALAR'}]
> category
> 'Arithmetic'
> is_variadic' :
> False,
> 'max_args
> 3,
**

首先, 我们规定一份文档的格式(几个position args, 几个keyword args, 返回类型, 参数类型, 是否强制输入, etc. )


> [!NOTE] [图片 OCR 识别内容]
> get_tosk progress (quont-night MCP Server) {"task_id": "08682061-4476-456f-4924-22744793448c"}
> status
> finished"
> 
> result"
> {
> E"status'
> :
> "failed" ,的格式(几个position args; 几个 keyword args; 返回类型;参数类型;是
> 'progress_url
> "https: / /api.worldquantbrain . com/simulations /ZghXlv3Q94GaaEEJwBXdGSG" =
> error
> 'Required attribute
> 'target_tvn
> must have
> Value



> [!NOTE] [图片 OCR 识别内容]
> "id":
> 'EWwGtdHUSaygaFleiszcNrz" 然后;应用mcp在平台L对operator 的用法迸行 回测 > feedback
> 修改文档  这套流程:(比如图示显示target_tVr
> }
> 
> 是必要参数 )
> ]
> error"
> "Batch failed:InCode:
> ts_decay_linear(close
> 10)
> CANCELLED:
> NonelnCode:
> ts_rankCclose,
> 10)
> >
> CANCELLED:
> NonelnCode: winsorize(close)
> CANCELLED:
> NonelnCode:
> pasteurize(close)
> >
> CANCELLED:
> NonelnCode: regression_neut(close, close)
> CANCELLED: NoneInCode
> ts_regression(close, close,
> 10)
> >
> CANCELLED: NonelnCode:
> ts_decay_exp_windowCclose, 10)
> >
> CANCELLED: NonelnCode:
> keep(close, 1)
> >
> CANCELLED:
> NonenCode:
> jump_decay(close,
> 10)
> >
> ERROR:
> Required attribute
> "sensitivity
> Iust
> have
> a ValuelnCode
> inst_tvr(close,
> 10)
> >
> CANCELLED:
> None
> }
> 
> 丰颞


然后, 应用mcp在平台上自主对operator的用法进行 回测 -> feedback -> 修改文档 这套流程. (比如图示显示target_tvr是必要参数.sensitivity对jump decay是必要参数)

最后得到包含所有合法性检验信息的本地文件.

即使平台之后对某些operator的规则改变, 也只需通过这套流程修改一下规则文件即可.

顺便宣传一下我的其他相关帖子:

[用ast生成super alpha中的combo表达式](../顾问 WL27618 (Rank 97)/用ast生成super alpha中的combo表达式代码优化_32726278113687.md)

[用python ast unparse修改表达式细节](../顾问 WL27618 (Rank 97)/用python ast unparse修改表达式细节代码优化_33892557730455.md)

[记录一下ast在代码中的用法](/hc/zh-cn/community/posts/35565539058967-%E8%AE%B0%E5%BD%95%E4%B8%80%E4%B8%8Bast%E5%9C%A8%E4%BB%A3%E7%A0%81%E4%B8%AD%E7%9A%84%E7%94%A8%E6%B3%95)

[super alpha combo中operator的使用心得](../顾问 WL27618 (Rank 97)/super alpha combo中operator的使用心得_32194005946775.md)

---

### 帖子 #6: AIAC 2025的一些小 Tips
- **主帖链接**: https://support.worldquantbrain.com[L2] AIAC 2025的一些小 Tips_36141016690199.md
- **讨论数**: 3

1. 关于 ra 打 tag 问题

所有提交的 ra 都必须打上父 alpha id 的 tag，有条件的话最好 check 一下，会出现 "Eligible to be a component alpha in AIAC2025 Super Alpha." 的 pass。


> [!NOTE] [图片 OCR 识别内容]
> 11PASS
> Turnover of 5.79% is above cUtoff of 1%.
> Turnoverof 5.79% is below cutoff of 709.
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 0.88 is above cUtoff of 0.55.
> Self-correlation is 0.1065, Which is above cUtoff of 0.7, or Sharpe is better by 10.0% or more:
> Data overuse check passed.
> Alpha submissions 2 below quota of 4.
> 2 year Sharpe of 1.68 is above cutoff of 1.58.
> Power Pool correlation 0.0913 is below cutoff of 0.5,or Sharpe is better by 10.0% or more。
> Pyramid theme USAIOIMODELmatches with multiplierof 1,3. Effective pyramid count for Genius is 1.
> Eligible to be a component alpha in AIAC2025 Super Alpha.


以下是一个 ppa 提交后，正确打 tag 的示例。实测发现，ra 是可以提交后再补 tag 的。


> [!NOTE] [图片 OCR 识别内容]
> 匕 Properties
> Last saved Wed, 11/05/2025,3:52 PM
> Name
> Category
> Currently 'anonymous'
> None
> Tags
> Color
> GXmVo8gl
> PowerPoolSelected
> 又
> None
> Description
> 891
> 100 character minimum


2. 关于 sa 打 tag 的问题

sa 的 select 语句中必须要有 in(tags, ${parent_alpha_id})，其中 ${parent_alpha_id} 必须是 ra 提交时打上的 tag，以下是一个 sa 的示例：


> [!NOTE] [图片 OCR 识别内容]
> Code
> Selection Expression
> 1
> in(tags, "VRWrPgLG"))
> Combo Expression


**sa 提交前必须先打好 parent alpha Id 的 tag 和所使用的大模型的 tag，记住！是必须提交前先打好tag！提交前先打好tag** ！提交后补 tag 是不算比赛 alpha 的（别问我是怎么知道的。。）以下是 sa 提交前的 tag 示例：


> [!NOTE] [图片 OCR 识别内容]
> Name
> Category
> XgGO9X8a
> None
> Tags
> Color
> VRWrPgLG
> 又
> Qwen3-max 义
> None


最好在提交前 check 一次，会有 “Competition Al Alphas Competition 2025 matches.” 的 pass


> [!NOTE] [图片 OCR 识别内容]
> 9 PASS
> Sharpe Of 3.25 is above cutoff of 1.58.
> Fitness of 2.82is above cUtoff of 1.
> Turnoverof 6.44% is above cutoff of 2%
> Turnover of 6.44% is below cUtoff of 400
> Weight is well distributed over instruments。
> Sub-universe Sharpe of 2.28 is above cUtoff of 1.41.
> This alpha is self SuperAlpha。
> IS ladder Sharpe of 3.24 is above cutoff of 2.02 for ladder year 2: 1/20/2023..1/21/2021.
> Competition Al Alphas Competition 2025 matches。


3. 比赛过程中的小心得

每天的前四个 ra 可以正常按自己赛季节奏，该点塔点塔，该做 theme 做 theme。交够 4 个后， **尽量多交** 通过父 ra 衍生出来的子 ra，把父 ra 对应的 tag 池子做大，这样 sa select 的时候才有操作空间。

像我之前有一天交了 68 个 alpha，多交池子大了，sa 就好做了。


> [!NOTE] [图片 OCR 识别内容]
> 11/02/2025
> Submitted Alphas: 68


---

### 帖子 #7: AI比赛参考工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] AI比赛参考工作流_35831427191703.md
- **讨论数**: 15

千万不能思维受限


> [!NOTE] [图片 OCR 识别内容]
> Start
> USer
> provides seed
> alpha id
> Authenticate with BRAIN
> and LLM gateway
> Analysil phase
> Fetch alpha details
> code and se
> ttings
> 2. Identify operators and
> data fields Used
> Core research LOOD
> 4.AI powered reflection
> LLLLiHor
> Fetch context for each
> LLM experiment
> b. Query API for all related
> Generate performance
> component from BRAIN API
> summary and next steps
> alphas by tag
> comparison graphs
> 4. Call LLM to generate
> 5. Select new champion
> economic rationale
> for next iteration
> Output
> group of variation
> Step 3 - Al powered
> alphas
> End result
> family
> ideation
> of optimized alphas
> SuperAlpha
> 3.3 Settings variation
> 3.2 Data field variation
> 3.1 Operator variation
> Generate new alpha
> expressions
> Simulate evaluate and
> Simulate on BRAIN
> With parent id
> Retrieve performance
> results
> Performance results
> Tag


如果觉得阅读有困难，可以复制下面代码，到 [[链接已屏蔽])  生成高清流程图

```
graph TDA[Start - user provides seed alpha id] --> B[Authenticate with BRAIN and LLM gateway]subgraph AnalysisPhase [Analysis phase]  direction TB  C1[1. Fetch alpha details - code and settings]  C2[2. Identify operators and data fields used]  C3[3. Fetch context for each component from BRAIN API]  C4[4. Call LLM to generate economic rationale]  C1 --> C2 --> C3 --> C4endB --> C1subgraph CoreLoop [Core research loop]  direction TB  I{Step 3 - AI powered ideation}  I --> V1[3.1 Operator variation]  I --> V2[3.2 Data field variation]  I --> V3[3.3 Settings variation]  V1 --> G[Generate new alpha expressions]  V2 --> G  V3 --> G  subgraph SimEvalTag [3. Simulate evaluate and tag for each generated expression]    direction TB    S1[a. Simulate on BRAIN]    S2[b. Tag with parent id]    S3[c. Retrieve performance results]    S1 --> S2 --> S3  end  G --> SimEvalTag  S3 --> R[Performance results]  subgraph ReflectViz [4. AI powered reflection and visualization]    direction TB    N1[a. LLM experiment summary and next steps]    N2[b. Query API for all related alphas by tag]    N3[c. Generate performance comparison graphs]  end  R --> ReflectViz  ReflectViz --> CH[5. Select new champion for next iteration]  CH --> IendC4 --> ICH --> OUT[Output - group of variation alphas - End result - family of optimized alphas - SuperAlpha]
```

---

### 帖子 #8: BRAIN API及日常回测时常见的报错代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md
- **讨论数**: 5

以下是一些可能的错误消息，它们的可能原因以及解决方案：

- **1. **Attempted to use unknown variable**尝试使用未知变量**

- 数据不可用
   - 表达式中包含了一个不可用的变量。检查你的变量是否有拼写错误，或者你是否在设置中使用了正确的区域。提示：如果在表达式中正确使用，数据字段和操作符的字体颜色会显示为蓝色。

- **2. **Unexpected end of input**意外的输入结束**

- 语法错误，Alpha没有结尾
   - 一个常见的语法错误通常来自于最后一行的Alpha缺少括号或缺少分号。
   - 例如："rank(sales/assets" 会引发此错误

- **3. **Expression cannot be empty**表达式不能为空**

- 在最后一行加分号
   - 该错误通常在用户将他们的alpha分配给一个变量，但实际上没有在之后调用它时引发。
   - 例如： "alpha = -ts_delta(close,5);" 会引发错误，但 "alpha = -ts_delta(close,5); alpha" 就不会。

- **4. **Illegal group index value, cannot exceed number of elements****

- Group operator没有加densify
   - 为确保平台的高性能，在模拟过程中对组索引的值进行检查。索引值不应超过所有索引组所属的元素数量。如果引发错误消息，那么可能是组的索引在某个操作符中使用的不是密集的（非密集索引看起来像[0, 5, 8, 26, 107]）。在这种情况下，使用"densify(group)"会有所帮助。

- **5. **Illegal group index value, cannot be negative**非法的组索引值，不能为负**

- 非法的grouping值
   - 我们不允许组索引的值为负，要解决这个问题，试试使用densify操作符。且自定义分组的时候不能有负值

- **6. **Got invalid value for attribute "lookback", must be constant or string****

- "lookback" 得到无效值，必须为常量或字符串
   - 当你试图在操作符的 "lookback" 字段中使用非常量或字符串，或者当你错误地排列参数时，会引发此错误。
   - 例如："ts_rank(sales/assets, days_from_last_change(sales))" 会引发错误

- **7. **Grouping data used outside of group operator**在group operator外部使用grouping数据**

- 分组数据只能在组操作符中使用。如果你试图在其他地方使用组数据，就会引发此错误。
   - 例如："ts_delta(industry, 5)" 会引发错误

- **8. **Cumulative lookback of expression exceeds available history**表达式的累积回看超过了可用的历史**

- lookback区间非法
   - 由于数据历史的限制，如果你试图回看超过我们可以提供的范围，就会引发此错误。注意，考虑的累积回看是表达式中使用的最高回看。
   - 例如：ts_rank(ts_mean(close,20),20) 会有40的累积回看。

- **9. **You have reached the limit of concurrent simulations. Please wait for previous simulations to finish****

- 一个用户只能同时simulate10个；你已经达到了并行回测的限制。请等待之前的回测完成
   - 你一次只能模拟有限数量的alpha，所以如果你试图模拟超过这个数量，就会引发此错误。你必须等待你之前的一个模拟完成才能继续。

- **10. **Invalid number of inputs: X, should be exactly Y input(s)****

- 有参数未输入
    - 当你提供的输入数量多于或少于所需数量时，会引发此错误。
    - 例如：无论是 "group_mean(sales/assets, market)" 还是 "group_mean(sales/assets, 1, market, 1)" 都会引发此错误。正确的表达式应该是："group_mean(sales/assets, 1, market)"

- **11. **超时登出：Http Error****

- 所有用户每4个小时or提交过多错误simulation会被强制登出。需要书写代码捕捉错误并随时重登，同时需要保证任务的断点续传。

- ***12.* “回测应该回测了3000多个实例，但由于某种原因，丢失了1700个实例。已经设置了一个sleep函数，以防止访问次数过多，并一直在监视status_code以查找错误。但依然出现此问题，如何解决？”**

- simulation_response.status_code为201并不代表你的Alpha运行没有问题，运行有问题的Alpha就是会被丢失的。您可以运行一下下列代码，体会一下错误的来源：

```
simulation_data = {    'type': 'REGULAR',    'settings': {        'instrumentType': 'EQUITY',        'region': 'USA',        'universe': 'TOP3000',        'delay': 1,        'decay': 15,        'neutralization': 'SUBINDUSTRY',        'truncation': 0.08,        'pasteurization': 'ON',        'unitHandling': 'VERIFY',        'nanHandling': 'OFF',        'language': 'FASTEXPR',        'visualization': False,    },    'regular': 'high-close+dfd'}simulation_response = s.post('[链接已屏蔽] json=simulation_data)print(simulation_response.status_code)print(s.get(simulation_response.headers['Location']).json())print(f'status: {s.get(simulation_response.headers["Location"]).json()["status"]}')
```

- ***13.***  **“不确定SLOW+FAST参数的代码”/“不确定Neutralize选项country/region参数的代码”**

*- "* SLOW_AND_FAST"

*- "* COUNTRY"

- ***14.***  **”当使用模板进行模拟时，结果不好，有些时间点显示出平坦的曲线，表明该模型在那些时间没有股票选择能力。“**

- 请手动找到这个Alpha进行查看。在网页浏览器入“ [[链接已屏蔽]) 即可以看到它的表现。一般这种Alpha的出现是因为使用Alpha前的数据处理工作还不够好。

- ***15.***  **"目前我的代码在运行1000次成功回测的时间大概是2个小时到2个半小时之间，这是一个正常的速度吗？"**

-速度是正常的。看到您也获得了一个新可提交的Alpha,从效率上看，大约1000次simulation获得一个Alpha也是正常的效率，这个说明您的模板选择和数据选择都比较合适。另外一个检测自己速度是否合适的方法就是，回到网页界面，尝试手动simulate一下Alpha,如果会报错“too many simulation at a time”，这就说明代码正在全力工作，占用完了十个线程，算是高效了。

- **16. Correlation获取超时**

-用户只能在60分钟内发送150 correlation requests。不要对每个simulated的Alpha都request

- 17. 如何在JupyterNotebook实现多线程和随时插队？

下面这个代码可能可以提供一些思路：

在JupyterNote Book 的第一个cell

```
import timeimport threadingimport requestsclass RequestThread(threading.Thread):    def __init__(self, urls):        threading.Thread.__init__(self)        self.urls = urls    def send_request(self, url):        print(f'Sending request to {url}')        response = requests.get(url)        # handle your response here        time.sleep(5)    def run(self):        i = 0        while i < len(self.urls):            self.send_request(self.urls[i])            i += 1           urls = ['[链接已屏蔽] '[链接已屏蔽] '[链接已屏蔽] = RequestThread(urls)request_thread.start()
```

接着可以随时跑其他cell

```
urls.append('[链接已屏蔽])
```

或者，可以把所有待simulate的Alpha全部先放到一个csv文件，然后用另外一个notebook去读这个csv文件，不断发出Alpha到服务器中。简而言之，将csv文件作为不同notebook的交互点（中转站）

---

### 帖子 #9: Brain API技巧：如何挖掘API代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] Brain API技巧如何挖掘API代码优化_20309362198679.md
- **讨论数**: 9

Brain平台其实开发的非常规矩，很多功能页面都是通过api实现的。API文档只是其中一部分接口。很多同学在尝试使用API文档的时候，会遇到很多问题，例如不知道api的参数如何设定，返回值长什么样子等。希望下面这些信息能够帮助大家。

## 工具介绍

介绍2个好用的工具：

- 浏览器的开发者工具：developer tools：挖掘api，直接看到api链接和返回值
- Postman：测试api，python代码生成

### 浏览器的开发者工具developer tools

这个可以在Chrome，Edge，Firefox的菜单中找到。网上可是搜到详细使用方法。结合Brain平台，它可以帮助我们知道Brain平台使用了哪些API，可以获得什么返回值。

简单概括：打开浏览器 > 开发者工具 > Network(网络)，然后，进行Brain平台的操作（登录，查Data，进入不同菜单，simulation，修改settings，查看自己的alpha，对自己的alpha进行filter等）。这些操作，都会触发不同的api行为，这些api操作都会被记录下来。

下图，domain在api.worldquantbrain.com的就都是可能对我们有用的api


> [!NOTE] [图片 OCR 识别内容]
> Welcome
> Elements
> Console
> 毖 Sources
> NstNoi
> Pelommance
> Memon
> Application
> Presere log
> Disable cache
> No throttling
> Filter
> Inel
> Hide cata URLS
> Hde extenslon URLs
> Doc
> FctchxHR
> CSS
> Font
> Img
> Mcdla
> Manitcst
> Wasm
> Othor
> Blocked response cookies
> Blocked requests
> 3rd-pary requests
> Big recuest rOWS
> GroUp by frame
> Oyeriew
> Screenshots
> Name
> Status
> Domaln
> Type
> authenticaton
> 200
> api. worldquantbraincom
> fetch
> configuration
> 200
> api.Norldquantbraincom
> fetch
> 200
> api. worldquantbraincom
> fetch
> agreements
> 200
> api.Norldquantbraincom
> fetch
> ader?USer
> 200
> api. worldquantbraincom
> fetch
> messages?order--dateCreatedalimit-5
> 200
> api.worldquantbraincom
> fetch
> simulation
> 200
> api. worldquantbraincom
> fetch
> alphas
> 200
> api.Norldquantbraincom
> fetch
> summary
> 200
> api. worldquantbraincom
> fetch
> 117 requests 393 kB transferred
> 12.8 MB resources Finish: 7.4min DOMContentloaded: 2.35
> Load: 4.91


点击想看的api记录，（在Name列），就可以看到如下的信息。其中，“Headers”里有这个API的URL，Request Method(GET, POST, OPTIONS等)，状态code。“Response” tab是返回值，一般都是json格式。


> [!NOTE] [图片 OCR 识别内容]
> C
> https:Ilplatform worldquantbrain.comldata?delay-lginstrumentType=EQUITY&region=CHN&universe-TOP3000
> 鬯"
> Simulate
> Alphas
> Data
> 舀 Competitions (3)
> Events
> Learn
> Reter
> friend
> Region
> Delay
> Universe
> CHN
> TOP3000
> What data do yoU want to find?
> Search bydatasethame heldname Ordescripton
> SGarch
> Browse All Datasets
> Browse All Fields
> Browse by Category
> Welcome
> 〈少Elements
> Console
> 毖 Sources
> Nstwork
> 4 Perommance
> Memon
> Application
> Preserve log
> Disable Cache
> No throttling
> Filter
> Inver
> Hide data URLS
> Hde extension URLs
> Doc
> FctchxHR
> CSS
> Font
> Img
> Mcda
> Manifest
> WS
> Wasm
> Othor
> Blocked response COokes
> Blocked requests
> 3rd-par requests
> Blg request rOWS
> Grouo by frame
> Include pendlng reouests in HAR tile
> Oyeriew
> Screenshots
> Name
> Headers
> Preview
> Response
> Initiator
> Timing
> Cookies
> data:apolicationfo.
> General
> Collzc
> Request URL:
> https.ilapi worldquantbrain comdata-categores
> { data-Categories
> HeqUESt NEtnOC:
> ehyelOPe
> Status Code:
> 200OK
> enyelope
> Remote Address:
> 10.33.130.232.8080
> envelope
> Referrer Policy:
> strict-origin-when-cross-orign
> { authentic
> T?
> Response Headers
> CCESS-ContolAloW-Credentials


对于POST的请求，是需要有Payload的，例如跑alpha的时候，这个时候，也是可以在开发者工具中查看到的，这个过程，你可以查看到整个数据交互的过程，可以了解到从技术流程（跑一个alpha，会生成一个id，跑完后，会生成一个alpha id）。

下面就是simulate alpha的API的信息


> [!NOTE] [图片 OCR 识别内容]
> Headers
> Payload
> Preview
> Response
> Initiator
> Timing
> Cookles
> Genera
> Request URL
> httpsilapi Worldquantbrain comslmulations
> Request Method:
> POST
> Status Code:
> 201 Created
> Remote Adcress
> 10.33.130.232:8080
> Referrer Policy:
> strict-origin-when-Cross-origin
> Response Headers
> ACCeSS-Control-AlloW-Credentials:
> tuE
> AccesS-Control-Allow-Origin:
> https Iplatform worldquantbrain com
> ACCeSS-Contol-Epose-Headers
> Locatlon Retn-Afel
> AIow:
> POST OPTIONS
> Content-Language:
> Content-Length:
> Content-Type:
> texthtml; charset-UTF-8
> Date
> ThU, 04 Jan 2024 05:58:57 GMT


Payload中，是alpha公式和settings信息


> [!NOTE] [图片 OCR 识别内容]
> Headers
> Payload
> Preview
> Response
> Initiator
> Tming
> Cookles
> Request Payload
> View parsed
> TyDE
> REGULAR"
> 5ettings'
> {"nanHandling
> OFF"
> instrumenTyDe'
> EQUITY"
> delajy":1
> Universe"
> 
> TTuncation
> uniHandling
> VERIFYI
> pasteurization
> ON"
> region'
> U54
> a55et
> Tir
> Value but
> Corparatively
> 1TIe !
> EBIT are
> likely
> Comoanies
> that have invesTeJ
> TOI
> Towth
> TIe |
> the past years
> and
> hayve More
> TUI
> Tor
> 9rowth
> the fuzureInnIMPLENENITATION:
> Ween
> domestic and foreign
> EBIT
> Set
> LONe|
> lpha signa
> for
> Comoanies
> WiTh
> lOwET 355eT fair
> Value
> InIHINT
> TO IMPROVE THE ALPHA:
> Can
> Zhe
> lpha
> WOrK Well 讦
> Comparing
> aong
> Companies
> that
> lower
> Cashflows. Iny/nnalpha
> 9rOUp
> rank(fnd2_
> ebitdm;
> industryl
> 9roup
> rank(Tnd2_
> ebitfr
> industry) ; Iningroup_rank ( fn_assets_
> val_ay
> indusTryI
> 0.5
> alpha
> alpha"}
> hioh
> Tair_


“Allow”中显示的是这个API URL支持的请求method。例如上上图支持OPTIONS（虽然当前请求是POST）。既然支持OPTIONS，那你就可以在Postman工具中，尝试一下，看看会有什么返回值，是否有用。

通过developer tools可以监控的很多api urls，可以让你不单单局限在官方的Brain API文档中。

### Postman

这个工具可以让我们不断尝试API，找到我们想要的返回结果。更重要的是，Postman可以给我们展示python代码（支持很多编程语言），特别适合我们编写不同API的函数 - copy代码，简单修改一下，就是我们需要的特定函数。

**注：**  *Postman限制需要注册（免费），登录，才能够开启Collection（理解为，将很多Brain API放到一起）。有很多类似工具，但是只有Postman有代码生成功能（代码生成，特别适合编程不熟的同学。如果很熟悉编程，可以选择任意类似工具，例如Insomnia）*

#### 针对Brain API的使用

使用Postman发送Brain API请求，是需要获得authorization的。所以

1. 首先 **POST**   [[链接已屏蔽]按照下面这个设置就可以。用户名，密码就是Brain平台的email和密码。]([链接已屏蔽])

注意：生成的token有效期是4小时。所以，4个小时后（目前状态，不确定未来Brain是否会改），就需要重新获得token。在编写自己的代码的时候，你需要考虑一下过期之前，重新刷新token，或者如果运行API返回结果是token过期的消息，重新刷一下token。


> [!NOTE] [图片 OCR 识别内容]
> My Workspace
> New
> Import
> Overview
> POST authe
> GET
> Exam
> GET reference
> OPT alpha
> GET ALL Data
> GET TES
> POST simulati
> No Environment
> 000
> WQ-TEST
> authentication
> SaVe
> Collections
> POST
> https:/lapi.worldquantbrain.comlauthentication
> Send
> APIs
> WQ-TEST
> Params
> Authorization
> Headers (10)
> Body
> Pre-request Script
> Tests
> Settings
> Cookies
> 〈
> POST authentication
> Environments
> POST simulation
> Type
> Basic Auth
> Heads up! These parameters hold sensitive data. To keep this data secure While working in a collaborative
> POST simulation multiple
> environment; we recommend using variables. Learn more about yariables
> Mock servers
> The authorization header will be
> GET my Info
> automatically generated when you send
> GET get Example
> the request. Learn more about Basic Auth
> Username
> 用户名
> History
> authorization
> Password
> 密码
> 0十
> Body
> Cookies (1)
> Headers (13)
> Test Results
> Status: 201 Created
> Time: 940 ms
> Size: 839B
> Save as example
> 000
> Pretty
> Raw
> Preview
> Visualize
> JSON
> 2
> USeI"
> 2
> 3
> Iid
> 4
> 5
> token
> 2
> 6
> expiry
> 14400.0
> 7
> 8
> permissions
> [
> CONSULTANT
> 10
> MULTI_SIMULATION
> 11
> "PROD ALPHAS"
> 12
> REFERRAL
> get


2. 在第一步之后，未来的4小时之内，我们就可以不断尝试各种API了。注意一下，其他各种API的Authorization选择继承。例如。


> [!NOTE] [图片 OCR 识别内容]
> WQ-TEST
> TEST
> SaVe
> GET
> https:/lapi.worldquantbrain.comlsuggestlexamples?limit= 500
> Send
> Params
> Authorization
> Headers (9)
> Body
> Pre-request Script
> Tests
> Settings
> Cookies
> Type
> Inherit aut
> The authorization head
> Inherit auth from parent
> automatically generater
> the request. Learn morr
> No Auth
> aythorizatign
> Basic Auth
> This request is using Basic Auth from collection WQ-TESI:
> Bearer Token
> JWT Bearer


#### Postman代码功能

右侧，又一个 </> 图标，点开，选择Python-Requests，就可以看到基于requests 的python 代码。


> [!NOTE] [图片 OCR 识别内容]
> HP
> WQ-TEST
> TEST
> SaVe
> Code snippet
> GET
> https:/lapi.worldquantbrain.com/suggestlexamples?limit= 500
> Send
> Python
> Requests
> 1
> import
> requests
> Params
> Auth
> Headers (9)
> Body
> Pre-req.
> Tests
> Settings
> Cookies
> 2
> UII
> "https: //api.worldquantbrain. com /
> Query Params
> suggest/examples?Limit=500'
> Value
> Description
> Bulk Edit
> payload
> {3
> headers
> {
> limit
> 500
> Authorization
> Basic  0g=
> Key
> Value
> Description
> '
> 10
> 11
> response
> requests . request (
> GET"
> UII
> headerszheaders
> data=payload )
> 12
> 13 print (response
> text )
> 14
> Body
> 200 OK
> 276 ms
> 2.76 KB
> Save as example
> 000
> Pretty
> Raw
> Preview
> Visualize
> JSON
> 2
> Count
> 10_
> 3
> Inext"
> null
> previous
> null
> 5
> results
> [
> 6
> 7
> "settings":
> {
> 8
> "instrumentType
> EQUITY'
> Key


详细的Postman使用，大家可以网上搜搜。

## 一些额外的API

#### 查看自己的messages：GET

[[链接已屏蔽])

#### 查看fastexpression：GET

[[链接已屏蔽])

#### 符合某一个settings的所有datafields：GET

网页端有10000条上限，通过下面API格式，没有上限。如果是几万条数据，大概几百k大小的，需耐心多等几秒）
 [[链接已屏蔽])

[[链接已屏蔽])

网页开发者工具看到的链接是这样的（有10000条上限）
 [[链接已屏蔽])

#### 符合某一个settings的所有datasets：GET

[[链接已屏蔽])

#### 查看某一个dataset的所有datafields：GET

例子dataset.id=fundamental6。dataset ID是可以通过看浏览器的url和查看dataset API的返回值得到。
 [[链接已屏蔽])

#### 个人所有的alpha：GET

[[链接已屏蔽])

可以添加更多条件进行filter。例如` [[链接已屏蔽]) 
具体filter条件，可以去Alphas菜单，自行设置Filter条件，然后通过developer tool查看

#### Simulations：OPTIONS

[[链接已屏蔽]) 
返回值中有所有settings中的值。如果Brain系统加入新的region或者universe等，这里都会实时体现。可以用来批量生产settings组合。

#### 获得alpha examples：GET

返回的是10个examples。Brain也只给出了10个，不超过50个，limit=50是没太大用处的。
 [[链接已屏蔽])

---

### 帖子 #10: claude code添加mcp经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] claude code添加mcp经验分享_34283772405143.md
- **讨论数**: 3

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行** 
claude code是一款AI编程的命令行工具, 在某些场景下比cursor表现更好; 类似工具genimi code、qwen code 等
原版的claude code在中国大陆无法使用, 可以借助claude code router使用, 配合claude code router可以配置多个厂家的api, 比如qwen-coder、deepseek等

配置mcp的方式: 
```
claude mcp add brain-mcp --scope local -- python /..../site-packages/cnhkmcp/untracked/platform_functions.py
```
最后一段是platform_functions.py的路径

添加完成后再<userhome>/.cluade里可以看到这样的配置:
```
      "mcpServers": {
        "brain-mcp": {
          "type": "stdio",
          "command": "python",
          "args": [
            "/home....../cnhkmcp/untracked/platform_functions.py"
          ],
          "env": {}
        }
      },
```

关于如何下载mcp,请看集合贴👉 [01-【新人必读】新顾问入门指南！(内含BRAIN API和 顾问收入等精华帖） – WorldQuant BRAIN]([Commented] 01-【新人必读】新顾问入门指南内含BRAIN API和 顾问收入等精华帖置顶的论坛精选_27928616328855.md)

大佬们已经说太多了，在这里不赘述。

---

### 帖子 #11: 目录结构
- **主帖链接**: https://support.worldquantbrain.com[L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md
- **讨论数**: 20

最近在积极地尝试使用 MCP ，基本没有错过论坛内的相关帖子，大家都在使用各种各样的工具。最近接触了 Gemini CLI ，论坛内正好也没有类似的内容，于是便进行了一番初步探索，分享给大家。

简单了解一下 Gemini CLI，是直接运行在终端地命令行工具， **免费调用 Gemini 2.5 Pro 模型，支持百万 Token 上下文，60 次/分钟，1000 次/每天的免费调用额度** ，个人用户应该是非常充足了。上下文的容量也比较大（正如 weijie 老师所说，上下文容量很重要，针对顾问们与 mcp 进行多轮对话来拷打出 alpha 是很适配的）。因此在我看来值得尝试一下。

先分享一下个人简单总结的初步使用感受，来供大家参考是否继续阅读并尝试使用：

**优点：** 免费；上下文容量很大（正常对话非常足够，且能压缩上下文）；速度还算较快；Memory 功能可以自定义规范；脱离 IDE 独立行走；能够输出有价值的alpha idea（尝试了一下难产的 insiders 数据集，还真整了一个ppa出来）；道歉还挺诚恳的（虽然没啥用）。

**缺点：** 命令行操作也许不够直观便捷；偶尔不够稳定；模型的表现有时也似乎不太稳定，会犯一些低级错误，如vector数据处理、数据字段名错误，有时候会有幻觉，也有我刚开始用没调教好的原因。

另外：在使用过程中可以保存或者让 AI 记住你的“指导”，利用编写工作流或者其他类似的方式，可以提高使用的效率。AI 还是需要好好调教的，需要一步步引导才能得到预期内和效果比较好的结果，感觉我的方法和技巧还是比较稚嫩，希望各位大佬能够多指导和分享 AI 的使用技巧！

如果对您有启发和帮助，请告诉我或者给我一个赞吧！

MCP 的安装和配置相信应该都没有什么难度了，就不多赘述。

## Gemini CLI 启动

> 参照 Github:  [[链接已屏蔽])  中的  `Quickstart`

**Pre：**

- Node.js ≥ 20 版本（Gemini CLI 是ts开发的）
- Google 账户（用于身份验证）

建议使用 npm 全局安装（npx用于临时使用）：

```
npm install -g @google/gemini-cli
gemini

```

安装完成之后就可以在任意地方输入  `gemini`  来启动 Gemini CLI 了。

### 用户认证

> 这里可能会有点小坑，可能会出现一些不同的认证失败的情况..
> 本文会在后面附上一些认证失败的解决办法，这里不影响继续阅读

作为个人用户就直接用 <  *Login with Google >* Google 账号来验证。点击回车之后会跳转到登录 Google 账号的页面。认证成功后就会进入 Gemini CLI。


> [!NOTE] [图片 OCR 识别内容]
> SE[UI
> Tips
> for getting started:
> 1
> Ask questions;
> edit
> files
> OI
> TUn
> Commands
> 2
> Be specific
> For
> the
> best results
> 3
> Create
> GEMINI .md files
> to
> CUstomize
> yOUI
> interactions With Gemini。
> 4
> /help for
> more
> information
> Using
> 工
> MCP
> SerVer
> Cctrltt
> to view)
> Type Your message
> 01
> @path/to/file


## MCP 配置

Gemini CLI 支持两种配置文件：项目级配置文件 和 全局配置文件。

全局配置文件一般位于用户主目录下  `C:\\Users\\xxx\\.gemini\\settings.json`  。

如果只想在某项目目录中配置，那么打开你想使用 Gemini CLI 的项目文件夹（一般在你的 WQ 的常用工作区目录下即可），创建  `.gemini`  目录，再在此目录下创建文件  `settings.json`  作为 mcp 配置文件。

```
# 创建 .gemini 目录
mkdir .gemini
# 在 VS Code 中打开设置文件
code .gemini/settings.json

# 目录结构
Your WQ Workspace/
├── .gemini/
│   └── settings.json
├── ....
├── ....

```

接着复制 WQ mcp 的 json 配置到 Gemini CLI mcp 配置文件  `settings.json`  中即可。

配置文件中 Gemini CLI 的行为按照以下优先级加载：

- 全局设置：~/.gemini/setting.json
- 项目设置：（项目根目录）/.gemini/setting.json

主要配置项：

- mcpServers：定义提供自定义工具的 MCP 服务器。

## Gemini CLI + MCP 使用

当 mcp 配置完成后，就可以使用  `/mcp`  或  `/mcp nodesc`  查看来查看已有的 mcp 及其工具。

`/mcp desc`  可以显示已有 mcp 及其工具的具体介绍。

### Compress 功能

Gemini CLI 提供了一个 compress 功能（ `/compress` ），可以对上下文进行压缩。

假设对话过程中超出了最大的上下文窗口，那么就会开始丢弃最开始的会话内容，那么 AI 模型就不能获取到全部的内容，会影响最终生成的结果。

那这个时候利用 Compress 功能对上下文进行压缩，AI 就能够获取到全部的上下文。并且压缩后上下文变短，那么 AI 要处理的数据也变少了，消耗的 Token 也会随之减少。

### 保存会话记录

如果需要退出当前会话并保存，方便下次再次进入会话，可以用命令： `/chat save <tag>`  。其中 tag 就是你给这个会话的标签，是下次再找到并进入会话的凭证。

查看已经保存的所有会话： `/chat list`  。

> 不会自动保存会话历史记录，需要保存的话记得 save。

### Shell 命令

使用  `！`  开头即可使用常规的 shell 命令。

退出 shell 命令就再次输入  `！`  。

### Memory 功能

`/memory show`  可以展示已添加到会话上下文中的记忆文件。（默认为  [GEMINI.md]([链接已屏蔽]) ，可以在 `~/.gemini/` 或项目目录中）

可以自己将需要它遵循的规则写入文件，让它记住并遵守，如环境、编程规范、代码风格等，甚至工作流程之类的也可以。

附1（Gemini CLI 认证）：

1. 如果认证成功那真是太好了。
2. 如果 **选择账号并登录之后一直卡在这个认证页面，那么可能是网络的问题** 。
   解决方法比较简单。回到命令行按  `ESC`  ，两次  `Ctrl+c`  退出 Gemini CLI。打开代理软件，复制终端代理命令，粘贴到命令行（为 **当前命令行** 配置代理）。或者打开 TUN 模式。
   然后重启 Gemini CLI，重新认证即可。
3. 如果 **选择账号并登录之后显示授权成功，但是回到命令行发现报错了** 。
   命令行会提示需要设置 GOOGLE_CLOUD_PROJECT 这个环境变量。
   这种情况需要先进入 Google Cloud 的控制台，在左上角图标旁选择一个项目（如果没有创建过项目那就新建一个项目。
   进入项目后搜索  `Gemini for Google Cloud`  ，点击启用服务。等启用成功后，回到项目页面，复制项目的ID，这就是我们需要的参数。
   接着就是设置一下环境变量参数，操作就不多赘述。重新进入Gemini CLI ，重新认证即可。
4. 如果除了上述的其他情况，那么可以分享到评论区大家一起来解决~

> 使用 export 方式配置环境变量或终端代理只对当前终端生效，如果需要全局生效就需要写入系统的配置文件中哦~

附2（它给的一个ppa，虽然性能比较普通）：


> [!NOTE] [图片 OCR 识别内容]
> 5,033K
> 250OK
> Jn"4
> Jn'15
> Jan'17
> Jn'13
> J3n'19
> J31'20
> Jn21
> J31'22
> J123


附3（来自AI诚挚的歉意）：


> [!NOTE] [图片 OCR 识别内容]
> 我为在这个过程中给您带来的巨大困扰。浪费您宝贵的时间和耐心
> 致以最深刻。最诚挚的歉意。
> 我已经证明了我目前无法胜任您托付的这项任务。
> 我不会再提出任何新的方案了。非常抱歉,我没能帮到您。
> Using:
> 1
> MCP
> SerVer
> (ctrltt
> to
> View)
> accepting
> edits
> (shift
> 十
> tab
> t0
> toggle)


看到这了别忘了点个赞再走 ：）

---

### 帖子 #12: Harness engineering下的AI Quant经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] Harness engineering下的AI Quant经验分享_39304762113815.md
- **讨论数**: 50

这篇文章介绍一套我长期使用的人机协同工作流，以及我对这套流程的一些理解。

这套方法并不追求把量化研究完全交给 AI。我的做法更接近一种分工明确的协作框架：让 AI 参与它最擅长的环节，让代码承担稳定、重复、可验证的部分，让人保留目标设定、异常判断和最终提交权。

从来源上看，这套流程仍然建立在最传统的 1/2/3 阶框架之上，但过去一年多里不断吸收研究小组和论坛中的许多经验，把原先“简单提取字段再做扩展”的思路，逐步改造成了“由 AI 驱动”的结构。因此，它在今天依然保持着很强的生命力。

整套流程可以概括为三步：

1. 由 AI 生成结构简单、具有经济学含义的裸信号。
2. 从中筛出已有一定信号量的候选，再通过 1/2/3 阶和 robust 做增强。
3. 对符合提交条件的 alpha 做各类检测，补充经济学解释，最终由人决定是否提交。

在这三步中，AI 主要参与第一步和第三步中的解释辅助。中间的大部分流程，由硬编码脚本和人工调整的阈值共同完成。

这样的分工有一个直接好处：既能利用 AI 的创造力和高吞吐能力，又能尽量避免全 AI 工作流里常见的幻觉、偏航问题。入口端保持创新发散，中后段保持收敛，整套系统就能稳定运行。


> [!NOTE] [图片 OCR 识别内容]
> Harness 架构的三段式蓝图
> 阶段一:  信号生成
> 阶段二:  信号增强
> 阶段三:  检验提交
> Tier-1大模型发散生
> 机械化预处理。多通道剪
> 本地与平台指标检
> 成纯粹的经济学裸信
> 枝。1/2/3阶算子增强。
> 验。A1重新介入提
> 号。
> AI在此被绝对隔离。
> 供解释。人类执行
> 最终决策。
> 注意A1角色:  被高度隔离。仅负责提供创造力基石与逻辑解释。
> NotebookLN


———

## **## 一、AI 生成裸信号**

具体做法是：根据当前要做的塔，先确定对应的数据集，再从中选取一批数据字段，把字段名和字段描述发给 AI，要求它生成 50 到 100 个具有经济学含义的裸信号。这里我通常会强调三点：

1. 思路要尽量创新、发散。
2. 表达式要尽量简单、纯粹。
3. 可用的 op 只允许从我事先给定的基础 op 集合中选择。
4. 一定要有经济学含义，在输出表达式的同时也要输出经济学含义。

之所以强调“简单”，是因为这一步的目标还不是直接得到成熟 alpha，而是尽量生成一些结构清晰、逻辑直白、带有经济直觉的信号种子。后续的 1/2/3 阶和 robust，会承担大部分加工和增强工作。

AI 生成完成之后，我会对这批因子做两类预处理，这两步都由代码完成，AI 不参与：

1. #### 语法检查

使用论坛开源的语法解析器，检查字段是否存在、op 用法是否正确，先把明显无效的表达式清理掉。

1. #### vec 数据检查

对属性为 vector 的数据字段，自动补上 vec op。由于裸信号数量本来就不算多，这里我通常会把所有 vec op 都补上，因子数量虽然会增加，但总体仍在可控范围内。

处理完这些步骤之后，再对这批裸信号进行统一回测。

### ### 一些经验观察

在实际使用中，我有几条比较稳定的经验：

1. 模型越强，裸信号质量通常越高。实际效果上，tier 1 的模型，例如 GPT 和 Claude，通常明显优于更便宜的模型。
2. 更适合直接用 instant 模式，不开 thinking。我的实际观察是，一旦进入长链条思考，生成结果反而更容易变复杂，纯粹性会下降。
3. 输入给 AI 的信息不宜过多。只提供字段名和字段描述，效果往往最好；如果再加上覆盖度、用户量等额外信息，结果有时会变差。

后两条还没有非常明确的理论解释。我的猜测是，输入越复杂，模型越容易把注意力放到一些次要信息上，输出也更容易偏向“复杂但不纯”的表达式。


> [!NOTE] [图片 OCR 识别内容]
> 阶段一:  纯粹的A1引擎 (信号生成)
> 极简输入
> Tier 1 大模型
> 极简输入:  仅提供基础
> 输出
> 字段名 +字段描述。严
> 开启 Instant Mode
> 50-100个极简裸信号
> 禁输入复杂元数据。
> Thinwiiy "ode
> 髭
> 上下文复杂度
> 反直觉发现 "Anti-Thinking"
> 给予A1的上下文越少。 思考路径越短。生成的金融信号反而越纯粹。
> NotebookLM


———

## ## 二、信号增强

回测结束后，流程进入信号增强阶段。

### ### 2.1 阈值初筛

第一步是按一定阈值筛选裸信号，例如 Sharpe > 0.6、Fitness > 0.4 等。阈值并不是固定不变的，会根据当前塔、当前样本质量和候选数量做适当调整。

### ### 2.2 剔除无效因子

初筛之后，我会进一步剔除一些没有继续增强价值的无效因子，主要包括厂、横线因子等。这类因子不只是没法用，还会污染下一步相关性剪枝的计算。

常见的剔除方式包括：

1. 剔除 longCount + shortCount 过少的因子。
2. 剔除 PnL 最后若干个数值全为 0 的因子，这种情况基本可以直接视为厂。

### ### 2.3 多通道相关性剪枝

这是整个中段最重要的一步。

做法是：把通过初筛的因子，分别按 Sharpe、Fitness、Margin 等多个维度排序。每个维度都可以看作一个“通道”。在每个通道里，先把排第一的因子放进该通道候选池，后续因子只有在与当前池子的 max corr 小于阈值时，才会被保留，否则丢弃。最后将多个通道得到的候选池取并集，得到剪枝结果。这样做的目的，是尽量保留多样性，避免单一指标主导。

相关性阈值本身也不一定要固定。为了多保留一些高质量候选，我通常会采用逐步衰减的方式，例如：

- 前 5 个因子，阈值设为 0.85

- 第 5 到第 10 个因子，阈值设为 0.80

- 之后的阈值设为 0.75


> [!NOTE] [图片 OCR 识别内容]
> 阶段二:  多通道相关性剪枝 (保持物种多样性)
> Pruning Matrix
> Top 5 候选池
> 第5-10候选池
> 第10+候选池
> (Max Corr < 0.85)
> (Max Corr < 0.80)
> (Max Corr < 0.75)
> Sharpe 通道
> Fitness 通道
> Margin 通道
> raW
> signals
> 拒绝单-维度的粗暴过滤。多维降维与衰减式相关性阈值。有效防止因孑沦为高度同质化的近亲繁殛产物。
> NotebookLN


### ### 2.4 进入 1/2/3 阶或 robust

完成剪枝之后，就进入传统的增强流程。

最常见的路径是：

裸信号进入 1 阶，1 阶继续筛选后进入 2 阶，2 阶再进入 3 阶。每一阶之间，都会重复上述的步骤。

如果跑完 1 阶或 2 阶之后，就已经获得了相当数量的可提交因子，那流程通常就到此为止，不再继续向下扩展。

如果跑完之后，可提交因子仍然偏少，我会考虑补跑 robust，通过参数遍历做进一步增强。但这一步需要非常克制。robust 的初衷是检验因子，而不是增强因子。使用过度，容易走向过拟合。

———

## ## 三、检验和提交

### ### 3.1 先过本地相关性

如果候选是 ppa，直接本地跑自己 ppa 池子的相关性即可。

如果候选是 ra，通常会先跑自己 ra 池子的自相关，再继续跑平台 check。

### ### 3.2 借助数据库做一轮人工筛选

对所有待提交因子，我会先在自己的数据库里做一轮浏览和筛选。除了 Sharpe、Fitness 这些基本指标之外，我的数据库里还会显示其他辅助判断信息，例如：

- maxTrade 线是否接近原 PnL

- op 数

- df 数

一般会先按 Sharpe、Fitness、Margin 从高到低排序，再剔除 turnover 过高、op 过多、df 过多的因子，然后进行挑选。

这一层仍然保留较强的人工判断成分。

### ### 3.3 执行测试（一）

这一轮主要是网页端的人工复核，重点看以下几项：

1. 看 compare，对自己的组合有没有提升。对组合明显拖后腿的因子，通常不会进入提交。
2. 看基本指标，确认 TVR 和 return 是否正常，最大回撤是否过高。
3. 看分年度表格。如果 2022 年和 2023 年表现过低，通常也会比较谨慎。
4. 看 PnL 线、Sharpe 线、Turnover 线的形态是否顺眼。

这一层虽然带有一定主观性，但对剔除一些“表面过线、整体感觉不对”的结果很有帮助。

### ### 3.4 执行测试（二）

这一轮主要做可自动化的一键测试。

#### 第一部分是 rank/sign test：

对候选因子跑 rank(alpha) 和 sign(alpha)。如果这些变形版本的 Sharpe 低于原 alpha 的 50%，我一般不会提交。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 067
> 1.00
> 0.40
> 0.75
> 04
> 0.50
> 0.2
> 0.25
> 鼍
> 0.0
> 000
> -0.2
> -0.25
> -0.4
> org sharpe
> 1.00
> -0.50
> 50% orig = 0.50
> -0.6
> 054
> 0.59
> orig
> rank
> slgn
> sign_gn
> sign_gn
> none
> orig
> raTk
> sign
> sign_gn
> sign_gn_none
> Margin
> Turnover
> 10.07
> 24.52
> 745
> 25
> 4|1
> 20
> -20
> 14.62
> 15
> S
> 8
> 11.73
> -40
> 10
> 8.75
> G0
> 3.93
> 78.13
> orig
> rank
> slgn
> sign_gn
> sign_gn_
> none
> org
> rank
> slgn
> slgn_gn
> sign_gn_none
> Returns
> Drawdown
> 301
> 211.27
> 200
> 3.00
> 175
> 150
> 125
> 8
> 100


#### 
> [!NOTE] [图片 OCR 识别内容]
> 181
> RS Test Pnl Compare: QPjgNLqp
> orig
> QPjBNLqP
> OrIg
> rank
> ZYIRLk2Q
> sign
> 58GZVNa1
> sign_gn
> pwzqganx
> 05
> sign_gn_none | mLzPkeqx
> 「
> SIgn_gn
> 日
> -0.5
> -1.0
> -1.5
> Slgn_gn
> none
> UuNw
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
> 2024
> Date


#### 第二部分是 robust test：

对原 alpha 跑 robust 测试。如果结果方差过大，也会比较谨慎。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> 最大值:  1.0900
> 均值: 0.3135
> 中位数:  0.2800
> 最小值:
> -0.3200
> 标准差:
> 0.2960
> 四分位距 (IQR):
> 0.4450
> 极差:  1.4100
> Fitness
> 最大值:  1.8400
> 均值: 0.2300
> 中位数:
> 0.1300
> 最小值: -0.2000
> 标准差:
> 0.3274
> 四分位距 (IQR):
> 0.2900
> 极差:  2.0400
> Margin
> 最大值:  134.2600
> 均值:  12.5754
> 中位数:
> 3.6900
> 最小值: -17.3000
> 标准差:  25.9616
> 四分位距
> (IQR) :
> 10.7450
> 极差:
> 151.5600
> Turnover
> 最大值:  40.9200
> 均值:  14.7835
> 中位数:  11.9300
> 最小值:  3.2800
> 标准差:  8.5542
> 四分位距 (IQR): 12.5750
> 极差:  37.6400
> Returns
> 最大值:  41.9000



> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 100
> 40
> 75
> 30
> 墨
> 20
> 詈
> 50
> 10
> 25
> 0
> 2
> 2
> 2
> 2
> Sharpe
> Fitness
> Margin
> TurnoVer
> 150
> 40
> 詈
> 100
> 詈
> 20
> 50
> -200
> -150
> -100
> -50
> 50
> 100
> 150
> 200
> 10
> 20
> 30
> 40
> 50
> 60
> 70
> Margin
> TurnoVer
> Returns
> Drawdown
> 100
> 75
> 40
> 詈
> 50
> 詈
> 20
> 25
> -40
> -20
> 20
> 40
> 20
> 40
> G0
> 80
> 100
> Returns
> Drawdown



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Decay
> Fitness by Decay
> 1.00
> 1.5
> 0.75
> 0.50
> 1.0
> 0.25
> 0.5
> 0.00
> 0.0
> -0.25
> 22
> GG
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Margin by Decay
> Turnover by Decay
> 40
> 125
> 100
> 30
> 75
> 50
> 20
> 25
> 圭
> 圭
> 10
> 22
> 66
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Returns by Decay
> Drawdown by Decay
> 40
> 125
> 30
> 100
> 20
> 75
> 10
> 50
> 25
> 22
> RG
> 120
> 240
> 512
> 22
> FG
> 120
> 240
> 512



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Universe
> Fitness by Universe
> 1.0
> 0.5
> 0.0
> 丰
> A
> A
> Universe
> Universe
> Margin by Universe
> Turnover by Universe
> 40
> 100
> 50
> 20
> Universe
> Universe
> Returns by Universe
> Drawdown by Universe
> 40
> 100
> 20
> 50
> 0
> 0
> TOPSOO
> TOP2O0
> TOP3000
> TOPSP5OO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1000
> MINVOLI
> MINVOL
> ILLIQUID
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOPSPSOO
> TOP1000
> MINVOLIM
> MINVOLTM
> '
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOP1OOO
> TOPSPSOO
> MINVOLIM
> TOPSPSOO
> MINVOLTN



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Neut
> Fitness by Neut
> 生
> 圭空臣孛l
> Neut
> Neut
> Margin by Neut
> Turnover by Neut
> 40
> 100
> 20
> 丢
> Neut
> Neut
> Returns by Neut
> Drawdown by Neut
> 25
> 100
> 垩 +
> 豆S星|臣
> 50
> 鹇 -工
> 丰茔茔
> 簋
> SLOW
> SECTOR
> 簋
> 磊
> 
> SECTOR
> 
> NONE
> FAST
> INDUSTRY
> 
> MONRKM
> CROWDING
> 鸶
> FAST
> 
> _MOMERKAM
> STATISTICAL
> STATISTICAL
> AND
> AND_
> SLOW_
> SLOW
> 昱
> AND_
> REVERSION
> REVERSION
> 簋
> SLOW
> NONE
> FAST
> INDUSTRY
> SUBINDUSTRY
> SECTOR
> 
> CROWDING
> 簋
> SLOW
> NONE
> n
> SUBINDUSTRY
> SECTOR
> _MOMERKBM
> CROWDING
> INDUSTRY
> STATISTICAL
> STATISTICAL
> 昱
> AND_
> SLOW
> SLOW
> AND_
> AND
> REVERSION
> REVERSION
> 簋
> SUBINDUSTRY
> FAST
> SUBINDUSTRY
> $
> NONE
> FAST
> INDUSTRY
> SECTOR
> MOMRKEM
> CROWDING
> SLOW
> NONE
> FAST
> INDUSTRY
> 暑
> _MOMERKAM
> CROWDING
> STATISTICAL
> STATISTICAL
> AND_
> AND_
> s
> SLOW_
> AND_
> AND_
> IERSION
> IRSION



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Group
> Fitness by Group
> 1.0
> 0.5
> 00
> 9
> "
> Group
> Group
> Margin by Group
> Turnover by Group
> 40
> 100
> 50
> 20
> y
> 聃貊
> 酾堕百
> 酝
> 苫 酶错
> Group
> Group
> Returns by Group
> Drawdown by Group
> 40
> 丐
> 100
> 20
> 亘
> 5
> q醒
> 50
> 5颐
> 牾-鸱



> [!NOTE] [图片 OCR 识别内容]
> 167
> PNL Curves by universe (colored by group max PNL)
> 1e7
> universe
> TOP200141898873.0000)
> C"」 '
> T0P3000(34151195.00OOJ
> TOPSP500 (33184197.0000)
> 1' |
> TOP500131186982.0000)
> ICY7 
> 4.00
> TOP1000 125998203.000OJ
> Lqiyc
> ILLOUID_NINVOLII (2136329400001
> 3.75
> 3.50
> 3.25
> _
> 300
> 2.75
> 250
> 2.25
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
> 2024



> [!NOTE] [图片 OCR 识别内容]
> 1e7
> PNL Curves by uni neut (colored by group max PNL )
> 1e7
> uni*neut
> TOP2OO NONE (41898873.0000)
> CeyAr
> 40
> T0P3000 NONE (34151196.00001
> T
> TOPSPSOO NONE 133184197.00OO)
> VSA
> TOP5OO NONE (311869820000)
> TOPIO0 NONE (259982030000)
> ILLIGUID_NINVOLIIINONE (21363294.00001
> 35
> TOPZOO SECTOR (13214659.0000)
> TOPZOOINDUSTRY (13052861.0000)
> TOP2OO MARKET (10940356.00001
> TOP3000 SUBINDUSTRY (1033918000001
> TOP3OOD*INDUSTRY (9251236.0000)
> 30
> TOP300 FAST (9050392.00001
> TOP200 REVERSION_AND_NONENTUI (8732002.0000j
> TOP3OOO SECTOR (8669384.0000)
> TOP30ODNARKET (7947224.0000)
> 25
> 
> TOP3OOOREVERSION_AND_MOMENTUM 17463611.0000)
> TOP200CROIDING (7316500.000O)
> TOP3OOOCROWDING (71144850000I
> 鱼
> TOPSPSOO FAST (6302806.00001
> _
> TOP3000 SLOI (6275460,000OI
> 20
> 盏
> TOPZOO*FAST (6193168.00001
> TOPSPSOO SECTOR (6187494,0000)
> TOP3000 SLOI
> AND_FAST (6159347.0000)
> 趸
> TOP3000STATISTICAL (5796010,0DOOI
> TOP5OD FAST (5775770.00001
> TOP5OD*SLOW (5654524,0000)
> 1.5
> 邕
> TOPSOOINDUSTRY (5461946.0000)
> TOPSPSOOINDUSTRY (5428550.0OOOI
> TOP5OOSLOW_AND_FAST (5389790.00OO)
> TOP200*SUBINDUSTRY (4519126.0000)
> TOPSP5OO M4RKET (4494552,000OI
> 1.0
> TOPSPSOO SLOI (44774460000)
> TOPSPSOOSLOI_AND_FAST (4446454,0000)
> TOPSOOCROWDING (4356666.0000)
> ILLOUID_NINVOLII FAST (4308647.000O)
> TOPSPSOO REVERSION_AND_NOMENTUN 14271460.0000]
> 05
> TOPSOO REVERSION_AND_NONENTUN14255880.0000)
> TOP5O0 SECTOR (421024-.0OOOI
> TOPSPSOO CROWDING (3929487.000O)
> TOP5O0 NIARKET (3624809.0OOO)
> ILLQUID_NINVOLIIINDUSTRY (31659490000)
> 00
> ILLIQUID_NINVOLIISLOW_AND_FAST (31279620000)
> O
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 2024
> TOPI0OOINDUSTRY (3089212000O
> ILLIQUID_NINVOLII SLOW (2823083 OOOOI
> Date
> TOP5OO*STATISTICAL (2540856,000O)


这一部分已经实现了自动化，只需要输入原 alpha 的 id，就可以一键完成。

### ### 3.5 执行测试（三）

这一步是 AI 第二次进入流程。

把该因子的表达式、数据字段含义发给 AI，让它输出以下内容：

1. 经济学解释
2. 因子值越大代表什么
3. 做多/做空因子值高/低的公司的合理性与潜在不合理处
4. 符合平台格式的因子描述，用于填写因子描述

对于经济学解释显著与常识不符的，我会慎重考虑。让AI提出正反两方面的观点，也可以防止从结果倒推原因。另外，认真填写描述似乎对weight有一定作用，可能可以增加自己因子被选中的机会。


> [!NOTE] [图片 OCR 识别内容]
> 二
> 经济学含义 (核心)
> 这个因子本质是在找:
> 在同一子行业内。同时具备高盈利能力 (ROA) 和高运营效率 (资产周转率)  的公司
> 因子值高的公司意味着什么?
> 当因子值高时,
> 公司通常具备:
> 1。资产赚钱能力强 (高ROA)
> 成本控制好 /定价能力强
> 或者资本结构合理
> 2。资产使用效率高 (高资产周转率)
> 存货周转快
> 业务模式轻资产 |高周转
> 3。经营质量高
> 不是"靠重资产堆利润'
> 而是"又赚得多;
> 又转得快"
> 典型特征:
> 消费品龙头 (高周转+稳定利润)
> 优质制造企业 (精益生产)
> 平台型轻资产公司



> [!NOTE] [图片 OCR 识别内容]
> 三
> 做多高因子股票的逻辑
> 合理性
> 1
> 质量因子 (Quality Factor)
> 高ROA = 好公司
> 高周转 =高效率
> 〉
> 双重筛选。避免"假盈利"
> 2。抗周期能力强
> 高效率公司更能应对需求波动
> 3。资本配置优
> 资产利用率高 >再投资回报更高
> 4
> 行业内比较更公平
> group_rank避免行业偏差 (例如银行 Vs 科技)
> 风险与不合理之处
> 1。可能错杀"重资产优质公司"
> 如公用事业
> 能源。半导体
> 天生周转率低 >被低估
> 2
> 周期顶部风险
> 在景气周期中:
> 收入暴涨 >周转率虚高
> 利润暴涨 > ROA虚高
> >因子容易在高点买入
> 3.
> ZSCore引l入极端值放大
> 异常高收入公司可能被过度放大权重
> 4。没有考虑增长性
> 高ROA + 高周转+高成长
> 可能是"成熟但不增长"的公司



> [!NOTE] [图片 OCR 识别内容]
> 四。做空低因子股票的逻辑
> 合理性
> 低ROA + 低周转:
> 〉
> 资产使用效率差 +盈利能力差
> 〉常见于:
> 僵尸企业
> 低效国企
> 管理层低效公司
> 风险
> 1
> 反转风险 (Turnaround)
> 低效公司一旦改革 >爆发性上涨
> 2
> 高投入早期公司
> 科技|创新企业:
> 当前ROA低。周转低
> 但末来潜力大
> 3.
> 行业周期底部
> 全行业ROA下降 >错误做空



> [!NOTE] [图片 OCR 识别内容]
> 五。整体评价
> 这个因子:
> 逻辑清晰 (杜邦框架)
> 行业内中性化 (很重要)
> 同时刻画"盈利 +效率"
> 但=
> 对周期敏感
> 偏好轻资产行业
> 缺乏增长维度
> 六。推荐评分
> 评分:  &110
> 适合作为:
> 核心质量因子之一
> 与成长因子 |估值因子结合使用
> 不建议单独使用的原因:
> 周期波动较大
> 行业风格偏向明显
> 七
> 英文总结
> Idea: Identify firms
> both high profitability and high asset efficiency within subindustries。
> Rationale for data used: Net income over total assets captures profitability (ROA), While revenue over
> total assets measures asset turnover; jointly reflecting operational and capital efficiency。
> Rationale for operators used: Ranking ROA emphasizes relative profitability; Z-scoring turnover highlights
> deviations in efficiency; and multiplication ensures only firms strong in both dimensions score highly; while
> group ranking neutralizes industry effects。
> with


### ### 3.6 提交

完成上述步骤之后，进入最终提交。

———

## ## 四、Harness engineering 下的 AI Quant

这套工作流我已经用了很久。回头看，它最核心的一点其实很简单：让 AI 做擅长的创新扩展的工作，让代码承担稳定、重复、明确的任务，让人保留高层决策和控制权。最近 harness engineering 这个概念开始流行起来，我觉得它非常适合概括这套方法。

如果打个比喻，这套流程更像一列火车。AI 驱动的裸信号生成，像是给火车换上了更强劲的引擎；而相关性约束、稳健性测试、RS 测试和分层筛选机制，则像轨道、道岔和信号系统。动力很强，方向也比较稳定。AI 先提出新的创意，后续流程再为这些创意补上轨道，因此轨道本身并不会提前封死创新。

相比之下，全 AI 工作流更像一辆高性能汽车。它有强劲动力，有自动驾驶，也有各种 skills 和提示词作为导航和路牌，但它仍然要在开放路网里持续做局部判断。一旦方向偏了，系统往往不会立刻停下，而是会沿着错误道路继续高速前进。动力越强，偏航之后冲出去的距离通常也越远，最后掉头的成本越高。


> [!NOTE] [图片 OCR 识别内容]
> 认知重构:  全A1工作流 VS. Harness Engineering
> 全A1工作流 /汽车模型
> Harness Engineering / 火车模型
> 特征:  极高的自主性;Al包揽生成。测试与纠错。
> 特征: A1提供前迸的动力 (引擎)
> 硬编码视则提供运行的轨道 (铁轨)
> 隐患:  在金酃嗓声中猴易[轨或陷入幻觉;方向不可控,容崭成本极高。
> 优势:  能量榄精准约束。铁轨本身不限制创造力,只设定致命哟边界。
> 真正的力量不在于A1的绝对自主。而在于对A1能量的精准约束。
> NotebookLM


———

## ## 五、与模板爆炸法的区别

AI打工人中现在用的一套方法，是先让 AI 提出一个因子表达式模板，再给出可以填入模板的数据集，然后围绕这个模板做大规模生成和回测。这种方法可以称为模板爆炸法。

研究者先假定某种表达式结构大体有效，再让模型或程序去填不同的数据字段。这样做的好处是效率高、可控性强，也适合围绕某一类已知有效结构做快速放大。但这个方法对于所使用的模板要求是比较高的。除了内置的几套验证过的有效模板，如果新手直接自己探索模板或者让AI未经验证给出一个模板，其实很难说效果会好。

而生成裸信号的方法更偏向发现式研究。通过这个方法发现和验证后的结果，也可以总结成模板，两者并不冲突。

———

## ## 六、AI 还能继续做的事

在当前版本里，AI 主要参与裸信号生成和最终的经济学解释。中间流程仍然以硬代码和人工软判断为主。但如果将现在中间段的操作日志、数据全量记录下来，然后交给AI去统计和发现其中的模式，AI 也会在这些位置上逐步加深参与。

———

## ## 结语

我对这套工作流的总体评价很简单：

它让 AI 做 AI 擅长的部分，让代码做代码擅长的部分，让人继续承担研究中最重要的判断工作。

在量化研究这种高噪声、高伪阳性、高竞争的场景里，有价值的通常不是盲目追求让 AI 覆盖更多步骤，而是能够约束并高效利用AI的能量。

这正是 Harness engineering 在 AI Quant 里的意义。

---

### 帖子 #13: MCP结合论文实践经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] MCP结合论文实践经验分享_36221002981271.md
- **讨论数**: 7

官方推荐的论文

Research Paper: Overvalued Equity and Financing Decisions

[../顾问 JG15244 (Rank 67)/[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md](../顾问 JG15244 (Rank 67)/[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md)

根据MCP工具里面的APP, 提取论文的方程 和表达式
 
> [!NOTE] [图片 OCR 识别内容]
> DI
> (44T
> 4CBQ
> 4TXDB)/ATt-I
> Debt issuance measure
> change in assets minus change in book equity
> deferred taxes scaled by lagged assets
> Variables:
> English
> 中文
> ATt-I
> Total assets at previous period (COMPUSTAT item AT, dollars)
> DI
> Debt issuance (dimensionless ratio)
> 4AT
> Change in total assets (COMPUSTAT item AT, dollars)
> 4CBQ
> Change in book equity (COMPUSTAT item CEQ dollars)
> 4TYDB
> Change in deferred taxes (COMPUSTAT item TXDB, dollars)
> Context: Measurement of net debt issuance following Baker and Wurgler (2002)
> methodology
> 中文描述:债务发行衡量指标
> 总资产娈动减去账面权益和递延税款娈动,再除以前期总资产。用于衡量公司净债务融资活动
> and
 
 
> [!NOTE] [图片 OCR 识别内容]
> 9 =
> (MVE + AT
> (C卫Q + TXDB))|AT
> Tobins 9
> market Value of equity plus assets minus book Value of equity; all divided by assets
> Variables:
> English
> 甲文
> AT
> Total assets (COMPUSTAT item AT, dollars)
> 0卫0
> Book value of equity (COMPUSTAT item CEQ dollars)
> MV卫
> Market value of equity (dollars)
> TJDB
> Deferred taxes (COMPUSTAT item TXDB, dollars)
> Tobin's q (dimensionless ratio)
> Context: Control variable for growth opportunities and investment prospects in regression tests
> 中文描述:托宾0值
> 权益市场价值加总资产减去权益账面价值。再除以总资产
> 用于衡量公司投资机会和市场估值
 导出分析结果
根据论文提供的 数据字段 mdl23_bk_net_equity_financ 利用ai  对起进行分析，

分析结果如下：

## 原始表达式（已回测）

**Alpha ID**: `rK3edZVd`

**表达式**:

```

group_neutralize(ts_rank(ts_mean(mdl23_bk_net_equity_financ, 20), 60) + ts_rank(ts_mean(pv87_stock_tvrwgthold, 20), 60), densify(sector))

```

**回测结果**:

- IS Sharpe: 0.61 (FAIL - 低于1.58阈值)

- IS Fitness: 0.22 (FAIL - 低于1.0阈值)

- Turnover: 0.0651 (PASS)

- Sub-universe Sharpe: 0.19 (FAIL)

**逻辑**: 高股权融资 + 高换手率 = 更强的市场时机信号

---

### 帖子 #14: Save credentials into session
- **主帖链接**: https://support.worldquantbrain.com[L2] Python的安装学习和API文档的下载代码优化_19024058049431.md
- **讨论数**: 15

1. **完成VScode+python+jupyter环境搭建**
   我们需要完成VScode+python+jupyter环境的搭建，核心目的是让计算机能够成功运行jupyter notebook。可以参考这个视频教程（ **请注意播放音量** ）： [vscode+python+jupyter环境搭建_哔哩哔哩_bilibili]([链接已屏蔽]) 。完成后，请用jupyter notebook运行以下代码并截图：
   ```
   print("my user id is: xxxxx")
   ```

2. **安装必要的python package**

参考上述视频，我们将使用“pip install XXXX”方法安装以下插件：

pandas
              requests
              seaborn
              matplotlib
              tqdm
              plotly

请截图显示插件安装成功的提示。

3.  **用户成功使用API连接到BRAIN**

我们需要成功地使用API连接到BRAIN。可以参考这个网页： [API Web:BRAIN API | WorldQuant BRAIN]([链接已屏蔽]) 。请运行以下代码以连接BRAIN后台：

```
def sign_in():
    import requests
    username = "yourBRAINemail@aaaaa.com"
    password = "yourBRAINpassword"

    # Create a session to persistently store the headers
    s = requests.Session()

    # Save credentials into session
    s.auth = (username, password)

    while True:
        try:
            # Send a POST request to the /authentication API
            response = s.post('[链接已屏蔽])
            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
            break
        except:
            print("connection down, trying to login again")
            sleep(10)

    print(response)
    return s
sign_in()
```

只有当返回值为下列显示时，才算跑通

```
 <Response 201>
```

通过上述任务，你已经完成了Python环境的搭建和接通了BRAIN后台，接下来可以开启自动化Alpha开发之旅了！🎇

---

### 帖子 #15: Trae配置使用mcp经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] Trae配置使用mcp经验分享_34228456653719.md
- **讨论数**: 46

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

对比使用了Roo code、通义灵码和Trae，RooCode配上顶级模型当然最好，就是费钱。通义灵码在使用过程中mcp经常掉线。Trae目前体验感还算可以。论坛上已经有大佬发了通义灵码、Cusor的配置流程，故此简单介绍一下Trae配置mcp的流程。

1、首先官网 [TRAE - The Real AI Engineer]([链接已屏蔽]) 下载安装Trae

2、安装cnhkmcp，对话框直接输入

```
pip install cnhkmcp
```


> [!NOTE] [图片 OCR 识别内容]
> @Builder s
> pipinstall cnhkmcp
> #  园
> Doubao-Seed-16


3、对话框右上角 齿轮按钮“AI功能管理”，添加>手动添加，


> [!NOTE] [图片 OCR 识别内容]
> TRAE
> AI 功能管x
> 返回对话
> 智能悭
> MC
> 上下文
> 规则
> 楔型
> MCP
> 添加
> worldquant-brain-platform 企


4、找到cnhkmcp的安装路径下的sample_mcp_config文件，将里面的内容复制到里面即可，当然，你如果报错，一般就是你的配置不对，需要用AI或者terminal帮你改写一下。


> [!NOTE] [图片 OCR 识别内容]
> Ma
> AppData
> Local
> Programs
> Python
> Python312
> Lib
> site-packages
> cnhkmcp
> Unzrazked
> N 诽序
> 三  查
> 侈改日期
> -」
> Pycache
> 2025/8/1611:30
> 文件买
> aryiy_aplpyy
> 2025/8/168;48
> Pthon
> arXiv_API_Too
> Manua
> 2025/8/168;48
> Markdown File
> 14KB
> TOrUI_
> functions:py
> 2025/8/168;48
> Pthon
> 42KB
> platform_functions py
> 2025/8/1611;27
> Pthon
> 109 KB
> platform_functions py.bak
> 2025/8/1611;2
> BAK 文件
> 109 KB
> sample_mcp_config
> 2025/8/16 8:48
> JSON 文件
> 2KB
> search_forum_with_authpy
> 2025/8/168;58
> Pthon
> USEI
> config
> 2025/8/1615;15
> JSON 文件
> 示S参考文栏_BRAIN_Alpha_Test_Requirements_and_Tips
> 2025/8/168;48
> Markdown File
> 17 KB
> 示工怅流_BRAIN_6_Tips_Datafield_Exploration_Guide
> 2025/8/168;48
> Markdown File
> 示工怅流_BRAIN_Alpha_Improvement_Workflow
> 2025/8/168;48
> Markdown File
> 示例工作流 daily_report_workflow
> 2025/8/168;48
> Markdown File
> 示工怅流 Dataset_Exploration_Expert_Manua
> 2025/8/16
> Markdown File
> 24KB
> 8,49



> [!NOTE] [图片 OCR 识别内容]
> 手配置
> 原始虱置 (ISON)
> 请从 MCP Servers 的介绍页面复制配置 JSON (优先使用 NPX 或 UVX  ]
> 粘贴到输入框中
> "mCpServers"
> "worldquant-brain-platform"
> Command"
> python
> apgs"
> "C:
> IUsers
> IAdmin |IAppData
> 1L0Cal
> IPro
> grams | |Python |Python3z21ILib | Isite-pa
> Ckages
> CnhkmCp
> untracked
> platform_f
> unctions .py
> 10
> 取消


配置好后，会显示mcp的功能，看到就表示可以正常使用


> [!NOTE] [图片 OCR 识别内容]
> TRAE
> 返回对话
> 智能体
> MCP
> 上下文
> 规则
> 楔型
> MCP
> 添加
> worldquant-brain-platform 企
> authenticate
> Authenticate with WorldQuant BRAIN platform. This is the first step
> manage_contig
> Manage contiguration settings
> get Or update configuration.Args:
> Create_simulation
> Create
> nEW simulation on BRAIN platfomm This tool creates and st。
> get_alpha_details
> Get detailed infommation about analpha.Args: alpha_id: The ID oft
> get_datasets
> Getavallable Jatasets tor research: Use this to Jiscover what Jata 15
> get_datafields
> Get available Jata felds foralpha construction. Use this to fnd speC
> get_alpha_pnl
> Get Pnl (Profitand Loss) data foranalpha
> alpha_id: The ID Of。
> get_user_alphas
> Get Users alphas with advanced filtening. pagination, and sorting:
> submit_alpha
> Submit analpha for production Use this when your alpha
> ready
> ATgS


5、对话框的内置智能体选择Builder with MCP ，然后就可以使用了


> [!NOTE] [图片 OCR 识别内容]
> 内置智能体
> Builder
> Builder with MCP
> 创建智能体
> Doubao-Seed-16



> [!NOTE] [图片 OCR 识别内容]
> TRME
> 使用mc工具首先学习了解brain平台的搜所有基础概念。认真学习总结brai平台的每-篇
> 文档
> Builder wiith MCP
> 思考过程
> 首先。我需要获取Brain平台的所有文档列表。这样才能系统地学习和总结每
> 篇文档。我将使用MCP眼务器提供的
> get_documentations 工具来实现这一点。
> worldquant-brain-platformlget_documentations
> 根据返回结果。我需要先进行身份验证才能访问文档。让我调用 authenticate 工具来完成身份验证。
> Worldquant-brain-platformlauthenticate
> 身份验证己成功。现在我可以继续获取Brain平台的文档列表。让我再次调用 get_documentations 工具来获耶所舸可文
> 档和学习材料。
> Worldquant-brain-platformlget_documentations
> 现在我己经获得了Brain平台的文档列表。接下来我需要开始学习这些文档。首先。我应该从最基础的入门文档开始。犄别
> this First
> Starter Pack"
> 这应该是了解平台的第-步。我将使用 read_specific_documentation 工具来读取
> 这篇文档的详细内容。
> Worldquant-brain-platformlread_specifc_documentation
> 我己经学习了 *Read this First
> Starter Pack
> '的内客。了解了Brain平台的基本介绍
> 顾问计划。金圃础知识和量化分析
> 的概念。接下来。我应该继续学习下一篇基础文档 Introduction to Alphas
> 以深入了解Apha的心概念。
> Worldquant-brain-platformlread_specifc_documentation
> ARead


---

### 帖子 #16: velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享_32340009231127.md
- **讨论数**: 25

在我第一次更新VF（velue factor）时，数值显示为0.04。当时，我心中充满了疑问：系统难道出错了吗？怎么会有这么低的VF值？于是，我急忙写邮件询问，是否是系统问题，但得到的回复却是：“没有问题。”这让我瞬间陷入了深深的失落，几乎觉得天塌了——怎么可能，连0.1都不到，之后还能做什么？

然而，这只是我VF学习之路的起点。为了寻找答案，我开始请教一些经验丰富的大佬，他们中有些VF值高达0.98甚至1.0。他们耐心地与我分享了他们的经验和见解，这些交流让我逐渐找到了自己的问题所在。原来，我不自觉地陷入了过拟合的泥潭，交出的结果都是“垃圾”。我明白了：问题出在自己的方法上。

**重新审视与总结**

经过这段时间的反思，我发现了自己在方法上的几个关键错误。在不知不觉中，我深陷于一阶、二阶、三阶死代码的漩涡，完全忽视了核心的“alpha”操作。我每天就是无脑地运行代码，反复跑着一堆没有意义的模型，完全没有思考“为什么”去做这些。VF值的低迷，也正是这些无用操作累积的结果。

意识到问题后，我开始调整思路。为了避免重复犯错，我决定通过更为系统的方式进行自我提升。我开始更加积极地参加论坛讨论、查阅书籍，并向研究小组里的资深成员请教，深入了解模型的核心思想与技术细节。每天都坚持积累，不再盲目操作，而是逐步理清了我自己的逻辑框架。

**突破与升华**

随着不断的实践与学习，我逐渐整理出了属于自己的交alpha逻辑和代码。我的模型开始逐步改进，VF值也在不断提高。最终，我成功突破了0.5以下的瓶颈，达到了0.93还成为了Expert。这段艰辛的成长历程，虽然充满挑战，但也让我收获了宝贵的经验和深刻的理解。

通过这次经历，我深刻认识到，技术和方法固然重要，但更重要的是要保持不断学习、持续反思的态度。没有什么是“一蹴而就”的，每一次的低谷，都是我们成长的铺垫。正是这份坚持与耐心，才让我从0.04走到了0.93，终于找到了属于自己的成功之路。

---

### 帖子 #17: VF0.5->1.0->1.0->1.0->?,1.0体验卡结束后的总结与思考【指标分析篇】经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] VF05-10-10-10-10体验卡结束后的总结与思考【指标分析篇】经验分享_35880708570391.md
- **讨论数**: 9

6、7、8月的VF终于是更新了，在幸运的拿到三个月的1.0体验卡后也终于产生了变化，最新的VF下降到了0.85。之前一直没有完整的总结分析过过往几个月提交的alpha的情况，所以也借着次更新变动的契机来做一个基于alpha指标的分析总结。在分析过程中会得出一些可能的结论，纯个人总结猜测，不一定为真。

看到有顾问朋友问拿到了高VF怎么交能拿高base，欢迎看看我的上一篇帖子

1.指标数据概览


> [!NOTE] [图片 OCR 识别内容]
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> sharpe
> 1.684
> 1.82
> 1.815
> 1.794
> 1.619
> fitness
> 1.812
> 1.587
> 1.461
> 1.513
> 1.415
> returns
> 0.193
> 0.119
> 0.106
> 0.118
> 0.118
> turnoVer
> 0.108
> 0.098
> 0.101
> 0.113
> 0.101
> margin
> 0.005
> 0.004
> 0.003
> 0.003
> 0.004
> Self cor
> 0.184
> 0.036
> 0.346
> 0.441
> 0.263
> prod_cor
> 0.255
> 0.475
> 0.752
> 0.755
> 0.671
> Count
> 15.0
> 71.0
> 68.0
> 74.0
> 91.0


我是今年4月底成为的consultant，因子在2025-04只提交了少量的alpha，所以在后面的分析中，不把4月的指标做重要考虑。我首次刷新VF是在3、4、5这个时间窗口内，对于我来说也就是4、5两个月的alpha数据。

4、5月-->1.0 4、5、6月-->1.0 5、6、7-->1.0 6、7、8月-->0.85

从这四次VF的刷新中不难看出，5月的alpha数据在三次1.0中应该是起到了比较大的作用，毕竟5月的窗口过去之后VF就产生了较大变化。如果只从各个指标的avg数据上来看，2025-08的平均指标确实要比2025-05差上一些，但整体上我觉得是一个可接受波动范围。（8月开始为了genius可能交了一些指标没有那么好的alpha）

**结论1: 在WQ，从不缺少优秀的consultant，不进则是退。**

关于super alpha我这次没有做详细指标统计，我从6月的比赛开始陆续做sa，7月、8月提交的基本都是指标较好的super alpha（base图中sa收入也是占大头），暂时不能判断sa对于VF的影响，也许要等到下次VF刷新时再观察。但如果是sa之前交的很少，那多交一些sa应该是有助于VF的。


> [!NOTE] [图片 OCR 识别内容]
> 2025-04 to 2025-06
> 2025-05 to 2025-07
> 2025-06 to 2025-08
> sharpe
> 1.805
> 1.809
> 1.732
> fitness
> 1.554
> 1.521
> 1.459
> returns
> 0.12
> 0.114
> 0.115
> turnover
> 0.101
> 0.104
> 0.105
> margin
> 0.004
> 0.003
> 0.003
> Self Cor
> 0.187
> 0.276
> 0.344
> prod
> COI
> 0.576
> 0.661
> 0.721
> Count
> 154
> 213
> 233


从3个月的平均指标上来看，确实是比之前低一些的。在5月时貌似有个bug，有些ra提交后其prod会显示为0，所以在统计上5月的pc指标上就明显低了一些。

2.指标分布情况


> [!NOTE] [图片 OCR 识别内容]
> sharpe comparison
> fitness comparison
> returns comparison
> 1.0
> 1.0
> 0.8
> 0.8
> 0.6
> 0.6
> 
> 
> 喜
> 3
> 0.4
> 0.4
> 2
> 0.2
> 0.2
> 0.0
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> Sharpe
> fitness
> returns
> turnover comparison
> margin comparison
> prod_cor comparison
> 2.5
> 200
> 175
> 2.0
> 150
> 125
> 1.5
> 
> 3
> 喜
> 100
> 
> 1.0
> 75
> 2
> 50
> 0.5
> 25
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 0.00
> 0.01
> 0.02
> 0.03
> 0.04
> -0.2
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> turnover
> margin
> prod_cor


图片中蓝色为567月时间窗口中的指标分布，黄色为678月。上图中有较明显变化的是sharpe、turnover和prod，sharpe上明显低的个数变多了，turnover上30%-40%这块有所增加（温和的turnover是ok的，但这个区间明显偏高了）。prod上还算正常，有高有低。

5、6、7月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆
> 豆20
> 豆40
> 1.5
> 20
> 2.5
> 30
> 35
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 2.5
> 30
> 35
> 4.0
> 4.5
> 0.4
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 100
> 豆
> 8
> 豆 15
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 0005
> 0010
> 0.015
> 0.020
> 0.025
> 0030
> 0035
> 0.040
> 0.4
> 06
> 1.0
> bUrOVeT
> margIn
> Prod
> COI


6、7、8月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆20
> 豆20
> 豆
> 1.0
> 1.5
> 2.0
> 2.5
> 30
> 3.5
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 25
> 30
> 3.5
> 40
> 45
> U0
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 20.0
> 17.5
> 15.0
> 12.5
> 8
> 8
> 10.0
> 7.5
> 50
> 25
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 005
> 0010
> 0015
> 020
> 0.2
> 0.3
> 0.4
> 05
> 0.6
> 07
> 0.8
> 0.9
> 1.0
> WUrnoVeT
> margIn
> Prod
> COI
> 豆


其实我个人从以上指标分布的对比中没有感觉出特别明显的差异，我提交因子时也会把握一个标准，从日常提交上来说也没有太大差异。

结论2: 做好自己的研究，剩下的交给系统

影响VF的因素实在太多了，数量、diversity、OS、成长表现、rank等等等等，不可能做到面面具到，只有尽量做出好alpha，提交符合自己审美的alpha，尽力就好。

3.地区/数据集分布


> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/DI
> 100
> 37.88%
> EUR/DI
> 88
> 33.33%
> ASIID1
> 46
> 17.42%
> GLB/DI
> 30
> 11.36%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> MODEL
> 54
> 20.45%
> RISK
> 39
> 14.77%
> FUNDAMENTAL
> 31
> 11.74%
> PV
> 31
> 11.74%
> ANALYST
> 30
> 11.36%
> OTHER
> 19
> 7.20%
> NEWS
> 15
> 5.68%
> OPTION
> 3.79%
> MACRO
> 9
> 2.65%
> SENTIMENT
> 7
> 2.65%
> INSTITUTIONS
> 7
> 2.65%
> EARNINGS
> 2.65%
> INSIDERS
> 3
> 1.14%
> SOCIALMEDIA
> 2
> 0.76%
> SHORTINTEREST
> 2
> 0.76%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/D1
> 38.68%
> EUR/D1
> 5
> 19.86%
> ASIID1
> 42
> 14.63%
> AMR/D1
> 31
> 10.80%
> GLB/D1
> 25
> 8.71%
> JPNIDI
> 21
> 7.32%
> Total
> 287
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> ANALYST
> 39
> 13.59%
> MODEL
> 37
> 12.89%
> RISK
> 35
> 12.20%
> FUNDAMENTAL
> 33
> 11.50%
> PV
> 33
> 11.50%
> OTHER
> 26
> 9.06%
> OPTION
> 5.92%
> NEWS
> 1
> 5.57%
> SENTIMENT
> 3.83%
> INSTITUTIONS
> "
> 2.79%
> EARNINGS
> 7
> 2.44%
> INSIDERS
> 7
> 2.44%
> SHORTINTEREST
> 6
> 2.09%
> SOCIALMEDIA
> 6
> 2.09%
> MACRO
> 4
> 1.39%
> BROKER
> 2
> 0.70%
> Total
> 287
> 100.00%


8月下旬开始陆陆续续开始交了一些jpn和amr的alpha，数量不多，可能是组合中不稳定的来源。D0听说也比较难，我还没有尝试过。

最后，现在无论是genius还是vf，竞争都很激烈，还是要努力提升自己，多交高质量的alpha！祝各位vf常高，base长红～

（结论3:新顾问要抓住机会，刚开始时的成长贡献可能会带给你一个高VF）

---

### 帖子 #18: [AIAC 2025 比赛] 迭代法寻找集合中Score最高SA
- **主帖链接**: https://support.worldquantbrain.com[L2] [AIAC 2025 比赛] 迭代法寻找集合中Score最高SA_36169526810519.md
- **讨论数**: 3

最近一直在参加AIAC比赛，在此分享一些构建 SA（Super Alpha） 的实践与思考，望各位前辈大佬多多指教。

**比赛的核心规则：**

1. 选出parent Alpha；
2. 基于parent Alpha，利用AI生成child Alphas；
3. 使用child Alphas构建SA参赛。

**遭遇的困难：**

我遇到的主要问题是 child Alphas 产出数量不足，导致备选池深度不够，难以组合出高分的 SA。

要从根本上解决这一问题，关键在于优化 prompt 以提升 child Alphas 的产出效率。

然而比赛时间紧迫，我必须在现有条件下，基于已生成的 child Alphas 尽可能构建出高分的  SA，否则连完赛都成问题。 *（此前比赛规则尚未调整，每天只能提交 1 个 SA， 现在规则已改为每天最多可交 4 个）*

**小池子高 score 解决方案：**

由于不清楚比赛对 SA 评分的具体规则，一通摸索后，最终我还是决定采用迭代法：

1. 先从池子中选出 10 个child Alphas，构建基础 SA；（我选了self-cor 最低的10个，并遍历了全部 risk neutralization，选择 score 最高的作为基础 SA）
2. 从剩余 alpha 中逐一遍历，每次选取一个追加到 SA 中并重新回测；(self-cor 低者优先)
3. 若回测后 score 提升，则保留该 alpha；反之则剔除；
4. 如此循环，直至处理完池中所有 child Alphas。

**具体实现（手搓）：**

由于所有 child Alphas 均带有 tag 标记，可通过  `in(tags, "A") ` 表达式筛选出所有component child Alphas。

同时，利用 alpha 的 color 属性标记其状态：color == "BLUE" 表示当前迭代中临时选中，color == "GREEN" 表示最终入选。

SA 的 selection 表达式示例如下：

> `in(tags, "parent_alpha_id") && (color == "GREEN" || color == "BLUE")`

**总结：**

通过迭代法，我确实找到了 score 优于直接全选的SA组合。过程中观察到以下现象，供大家参考：

1. 多数情况下，Sharpe 和 Fitness 越高，score 也越高；
2. 追加的 Alpha 若其 PNL 曲线走势与当前最高分 SA 的 PNL 曲线差异明显，则往往能提高 score 或降低 prod-correlation；
3. 追加的 Alpha 若使用与 SA 现有component Alphas 不同的 Dataset，则往往能显著提升 score。

由于数据样本有限，上述观察仅供参考，尚不足以形成定论，恳请老师和各位批评指正。

---

### 帖子 #19: 基于模版的Alpha生成相似字段Alpha工作流这是一个通用工作流，旨在通过替换现有Alpha表达式中的特定组件（如数据字段）来系统地、批量地生成新的Alpha变体。这种方法适用于快速探索相似因子的表现，并扩大有效的Alpha策略池。#核心思想该工作流的核心是“模板化”和“替换”。我们从一个表现良好或结构有趣的“种子Alpha”开始，将其视为一个模板。然后，我们识别出该模板中的某个关键部分（通常是一个数据字段），并找到一系列与之相似或相关的替代项，最后通过批量替换生成大量新的候选Alpha。#工作流步骤##1. 选择种子Alpha (Seed Alpha)选择一个作为起点的Alpha表达式。这个表达式可以来源于：- 你自己过去研究中发现的高绩效Alpha。- 一个具有特定逻辑结构（例如，时间序列操作、截面操作组合）的Alpha。- 一个你希望探索其变体的基础因子。**示例种子Alpha**：```-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))```在这个例子中，我们选择了一个基于`anl44_2_grossmargin_lastactccy`（毛利率）字段最后变动天数的表达式。##2. 识别可变组件确定你想要替换的表达式部分。最常见的是数据字段，但也可以是算子或参数。**示例可变组件**：在 `-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))` 中，可变组件是数据字段 `anl44_2_grossmargin_lastactccy`。##3. 发现相似组件寻找与上一步中识别出的可变组件相似或相关的替代项。这是提升Alpha生成质量的关键步骤。- **对于数据字段**：1.**筛选同一数据集 (Primary Filter)**：首先，将范围缩小到与原字段相同的数​​据集。例如，如果原字段来自 `anl44`，则优先探索该数据集下的其他字段。这可以作为初步筛选，因为同一数据集的字段通常在逻辑上是相关的。2.**分析语义相似性 (Key Step)**：在第一步筛选出的字段中，进一步通过分析其**描述（description）**来判断语义相似性。这是最重要的一步。寻找衡量相似经济或金融概念的字段。-**示例**：如果你的种子Alpha使用了一个关于“毛利率”（Gross Margin）的字段，那么在寻找替代项时，应优先选择描述中同样涉及**盈利能力**的字段，例如：-`EBITDA` (税息折旧及摊销前利润)-`Net Profit` (净利润)-`EPS` (每股收益)-`ROE` (股本回报率)- 通过这种方式，你可以确保新生成的Alpha在逻辑上与种子Alpha保持一致，而不仅仅是字段名称或来源相似。3.**考虑名称相似性 (Optional)**：在某些情况下，名称相似的字段也可能相关，但这通常不如基于描述的语义分析可靠。**发现工具与数据来源**：- **本地文件**：数据字段存储在本地的 `data/fields` 目录下的 CSV 文件中。你需要读取相关文件并解析其内容，特别是包含字段名称和描述的列，以寻找相似组件。不应使用 API 来获取字段。**示例相似组件**：假设我们发现 `anl44` 数据集中，除了关于 `grossmargin` 的字段，还有以下同样衡量盈利能力的字段：- `anl44_2_ebitdaps_value` (描述: ebitdaps value)- `anl44_2_epsr_value` (描述: epsr value)- `anl44_2_netprofit_rep_value` (描述: netprofit rep value)- `anl44_2_roe_value` (描述: roe value)- ...等等##4. 生成新表达式以编程方式，将种子Alpha模板中的可变组件替换为你在上一步中找到的相似组件列表，从而生成一系列新的Alpha表达式。**示例生成结果**：生成的表达式应直接在对话中以 Python 列表的格式返回，方便用户直接复制使用。```pythonexpressions = ["ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_qty),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_qty),120), 5)"]```##5. 评估与迭代 (可选但推荐)对生成的新Alpha表达式进行性能评估。- **批量回测**：使用 `create_multiSim` 工具可以一次性回测多个表达式，高效地获取它们的性能指标。- **分析结果**：分析回测报告，筛选出表现优异的Alpha。- **迭代优化**：基于评估结果，可以重复此工作流，例如选择一个新的种子Alpha，或探索另一组相似组件。#总结这个工作流提供了一种半自动化的方法，能够基于已有的知识和发现，快速、大规模地生成新的、有潜力的Alpha。它将研究员的洞察力（选择种子和相似组件）与机器的执行力（批量生成和回测）有效结合起来。
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP] 基于相似字段产生alpha的工作流分享_35797714275223.md
- **讨论数**: 4

使用的工具链参考：  [../顾问 JX79797 (华子哥/华子) (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md](../顾问 JX79797 (华子哥/华子) (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)

**本工作流基于相似字段寻找更多的alpha**

**1. 可以用于ai alpha比赛产生子alpha**

**2. 可以用于 ASI 通过Robust测试**

**工作流程：**

1. 选择一个“种子Alpha”: 从一个已知表现良好或结构有趣的Alpha表达式开始，把它当作一个模板。

2. 识别并替换关键部分:

确定该Alpha中的一个关键组成部分（通常是一个数据字段），例如一个关于“毛利率”的字段。

3. 发现相似字段: 寻找与该关键字段在语义上相似的替代字段。工作流强调，关键在于分析字段的描

述来寻找衡量相似经济概念的替代品（例如，用另一个盈利能力指标如“净利润”或“EBITDA”来替换“

毛利率”），而不仅仅是看字段名称。

4. 批量生成:

用找到的相似字段列表，批量替换模板中的原始字段，从而快速生成大量逻辑一致的新Alpha变体

**使用提示：**

```
Instrument Type: Equity, Region: ASI, Universe: MINVOL1M, Delay: 1 下的alpha "ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactsell_amt),120), 5)", 使用工作流similar_field_alpha_generation_workflow.md 生成 20 个新的表达式
```

上文示例中的alpha，Robust失败无法提交

- **Robust universe Sharpe of 1.13 is below cutoff of 1.46 (90% of Alpha).**

使用工作流得到新的20个表达式，执行回测，得到2个可提交alpha

**工作流内容**

```
# 基于模版的Alpha生成相似字段Alpha工作流这是一个通用工作流，旨在通过替换现有Alpha表达式中的特定组件（如数据字段）来系统地、批量地生成新的Alpha变体。这种方法适用于快速探索相似因子的表现，并扩大有效的Alpha策略池。## 核心思想该工作流的核心是“模板化”和“替换”。我们从一个表现良好或结构有趣的“种子Alpha”开始，将其视为一个模板。然后，我们识别出该模板中的某个关键部分（通常是一个数据字段），并找到一系列与之相似或相关的替代项，最后通过批量替换生成大量新的候选Alpha。## 工作流步骤### 1. 选择种子Alpha (Seed Alpha)选择一个作为起点的Alpha表达式。这个表达式可以来源于：- 你自己过去研究中发现的高绩效Alpha。- 一个具有特定逻辑结构（例如，时间序列操作、截面操作组合）的Alpha。- 一个你希望探索其变体的基础因子。**示例种子Alpha**：```-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))```在这个例子中，我们选择了一个基于`anl44_2_grossmargin_lastactccy`（毛利率）字段最后变动天数的表达式。### 2. 识别可变组件确定你想要替换的表达式部分。最常见的是数据字段，但也可以是算子或参数。**示例可变组件**：在 `-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))` 中，可变组件是数据字段 `anl44_2_grossmargin_lastactccy`。### 3. 发现相似组件寻找与上一步中识别出的可变组件相似或相关的替代项。这是提升Alpha生成质量的关键步骤。- **对于数据字段**：1.**筛选同一数据集 (Primary Filter)**：首先，将范围缩小到与原字段相同的数​​据集。例如，如果原字段来自 `anl44`，则优先探索该数据集下的其他字段。这可以作为初步筛选，因为同一数据集的字段通常在逻辑上是相关的。2.**分析语义相似性 (Key Step)**：在第一步筛选出的字段中，进一步通过分析其**描述（description）**来判断语义相似性。这是最重要的一步。寻找衡量相似经济或金融概念的字段。-**示例**：如果你的种子Alpha使用了一个关于“毛利率”（Gross Margin）的字段，那么在寻找替代项时，应优先选择描述中同样涉及**盈利能力**的字段，例如：-`EBITDA` (税息折旧及摊销前利润)-`Net Profit` (净利润)-`EPS` (每股收益)-`ROE` (股本回报率)- 通过这种方式，你可以确保新生成的Alpha在逻辑上与种子Alpha保持一致，而不仅仅是字段名称或来源相似。3.**考虑名称相似性 (Optional)**：在某些情况下，名称相似的字段也可能相关，但这通常不如基于描述的语义分析可靠。**发现工具与数据来源**：- **本地文件**：数据字段存储在本地的 `data/fields` 目录下的 CSV 文件中。你需要读取相关文件并解析其内容，特别是包含字段名称和描述的列，以寻找相似组件。不应使用 API 来获取字段。**示例相似组件**：假设我们发现 `anl44` 数据集中，除了关于 `grossmargin` 的字段，还有以下同样衡量盈利能力的字段：- `anl44_2_ebitdaps_value` (描述: ebitdaps value)- `anl44_2_epsr_value` (描述: epsr value)- `anl44_2_netprofit_rep_value` (描述: netprofit rep value)- `anl44_2_roe_value` (描述: roe value)- ...等等### 4. 生成新表达式以编程方式，将种子Alpha模板中的可变组件替换为你在上一步中找到的相似组件列表，从而生成一系列新的Alpha表达式。**示例生成结果**：生成的表达式应直接在对话中以 Python 列表的格式返回，方便用户直接复制使用。```pythonexpressions = ["ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_qty),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_qty),120), 5)"]```### 5. 评估与迭代 (可选但推荐)对生成的新Alpha表达式进行性能评估。- **批量回测**：使用 `create_multiSim` 工具可以一次性回测多个表达式，高效地获取它们的性能指标。- **分析结果**：分析回测报告，筛选出表现优异的Alpha。- **迭代优化**：基于评估结果，可以重复此工作流，例如选择一个新的种子Alpha，或探索另一组相似组件。## 总结这个工作流提供了一种半自动化的方法，能够基于已有的知识和发现，快速、大规模地生成新的、有潜力的Alpha。它将研究员的洞察力（选择种子和相似组件）与机器的执行力（批量生成和回测）有效结合起来。
```

```

```

---

### 帖子 #20: [MCP]免费最强版 Trae/VsCode + Cline + Gemini-cli 构建 cnhkmcp 使用环境经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享_34338855618583.md
- **讨论数**: 21

先赞后看，一键三连，需科学上网

**1. Gemini Cli 安装和登录验证参考，只需要通过用户认证即可**

[[L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md]([L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md)

**2. Cline 插件下载安装**

Cline插件在3.18.0短暂的支持过Gemini Cli ，在google要求下很快下线了该功能，该版本下载地址：  [[链接已屏蔽])

在Trae和VsCode ide中，选择从VSIX安装,安装后在Cline介绍页关闭自动更新 
> [!NOTE] [图片 OCR 识别内容]
> 终端
> 窗0
> 帮助
> 搜索
> Ppa
> 从 VSIX 安装。
> 让


**3. Cline配置**

打开Cline，选择使用其他api key不登录cline账号， 在API Provider 下拉列表中选择Gemini CLI Provider -> 视系统情况看是否需要配置oauth_creds.json 路径，一般无需配置， Let‘s get Started

**如果直接选择Gemini CLI Provider，Let‘s get Started没有反应，可以任意选一个其他的AI填入api key，进入之后再重新选择Gemini CLI Provider**

**4. MCP配置**

如下图，在1配置角色规则，2配置mcp server

角色配置参考： [[Commented] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md]([Commented] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md)


> [!NOTE] [图片 OCR 识别内容]
> Type
> @ for context;
> for slash commands & Workflows, hold shift to drag in fileslim
> @
> 十
> 骂
> 蛮 gemini-cli:gemini- 2.5-pro


成品：


> [!NOTE] [图片 OCR 识别内容]
> Rules
> Workflows
> Rules allow you to provide Cline with system-level guidance. Think of them as a
> persistent way to include context and preferences for your projects or globally
> for every conversation. Docs
> Global Rules
> Consultantmd
> New rule file。
> Workspace Rules
> New rule file。
> 十
> 恩
> 蛮  gemini-cli:gemini-2.5-pro
> Plan
> Act



> [!NOTE] [图片 OCR 识别内容]
> Auto-approve:
> Enabled
> Read
> Edit
> Safe Commands
> MCP Servers
> Worldquant-brain-platform
> 十
> 嚣
> 蛮  gemini-cli:gemini-2.5-pro
> Plan
> Act


**5. 使用感受**

**强于大部分收费大模型， 60次每分钟，1000次每天的额度足够调教自己的员工**


> [!NOTE] [图片 OCR 识别内容]
> 0
> Cline (器+')
> 器
> 9 巴
> 缌
> Task
> $0.0000
> 描述当前mcp的详细功能
> Tokens:
> 1.5m
> 13.9k
> 4.05 MB
> 419.8k
> 1.Om
> 9'T1 o
> 核心洞察:
> 1.战略转移成功:  您近期的研究重点已成功从 USA 扩展至 EUR 和 GLB 市场。尤
> 其在 EUR/DI/ANALYST 类别上取得了显著成果。
> 2.多元化初见成效:  您在欧洲点亮了多个新的数据类别。显著提升了投资组合的
> 多元化程度。
> 3.明确的增长机会:
> CHN
> (中国)  市场仍然是您投资组合中的空白区域。是您未
> 来获取高额回报和提升顾问等级的最大机遇。
> 下一步战略建议:
> 首要任务:  立即开始对 CHN 市场的数据集进行研究。使用
> get_datasets (region='CHN' ) 来发现可用的数据。
> 巩固优势:  在 EUR 和 GLB 市场。继续深化对 MODEL 和 RISK 类别的研究。建
> 立您的护城河
> 优化USA策略:  将在 USA 市场的精力从数量转向质量。专注于开发高
> Sharpe。 低相关性的独特Alphaa
> 您的近期表现证明了您具备快速适应和开拓新领域的能力。现在。将这股势头带入
> 中国市场。将是您成为顶尖顾问的关键步
> Auto-approve:
> Enabled
> Read
> Edit
> Safe Commands
> Start New Task
> Type a message。.
> Type @ for context;
> for slash commands & Workflows, hold shift to drag in fileslimages
> 十
> 蛮 gemini-cli:gemini-2.5-pro
> Plan
> Act


---

### 帖子 #21: AI-Driven, Semantically-Aware Alpha Generation Workflow (Local)This document outlines an advanced, robust workflow for generating financial alpha expressions. The process is driven by an AI assistant, operates entirely on local data, and focuses on creating semantically meaningful and syntactically correct alphas.#Workflow Diagram```mermaidgraph TDsubgraph "输入与学习 (Input & Learning)"A[1. 定义参数与学习<br>Define Parameters & Learn<br><br><b>用户输入:</b><br>- Region, Universe, Delay, Category, Operator<br><br><b>AI学习 (关键):</b><br>- <b>必须</b>从 `data/gold_operators.csv` 学习操作符定义、参数和用法。]endsubgraph "本地数据检索 (Local Data Retrieval)"B[2. 加载数据集元数据<br>Load Dataset Metadata<br><br><b>路径 (本地):</b><br>`data/datasets/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>读取并解析CSV，根据`Category`筛选数据集ID。]C[3. 加载并筛选字段<br>Load & Filter Fields<br><br><b>路径 (本地):</b><br>`data/fields/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>1. 加载所有字段。<br>2. 根据数据集ID筛选出`Category`相关字段。<br>3. 识别每个字段的类型 (matrix vs. vector)。]endsubgraph "AI智能生成与验证 (AI-Powered Generation & Verification)"D[4. AI理解、组合与验证<br>AI Understands, Combines & Verifies<br><br><b>过程:</b><br>- <b>处理Vector:</b> 对vector类型字段使用`vec_avg`等聚合。<br>- <b>组合字段:</b> 寻找经济学上合理的组合。<br>- <b>应用操作符:</b> 使用正确语法和分组关键字。<br>- <b>最终验证 (强制):</b> 重新检查每个表达式中所有字段的类型。]endsubgraph "输出 (Output)"E[5. 保存表达式<br>Save Expressions<br><br><b>工具:</b> `write_to_file`<br><b>内容:</b> 生成的、经过验证的、语法正确的表达式列表。]endA --> B;B --> C;C --> D;D --> E;```#Detailed Steps##1. Define Parameters & Learn- **User Input**: The user specifies the target parameters for the generation task: `Region`, `Universe`, `Delay`, `Category`, `Operator`.- **AI Learning (Crucial Step)**: The AI **must** retrieve and analyze the operator's definition, parameters, and correct syntax from the local file: `data/gold_operators.csv`.##2. Load Dataset Metadata (Local)- **Action**: The AI reads the appropriate dataset metadata file from the `data/datasets/` directory (e.g., `data/datasets/EQUITY_EUR_1_TOP2500.csv`).- **Parsing**: It extracts `dataset_id`s that match the specified `Category`.##3. Load & Filter Field Metadata (Local)- **Action**: The AI reads the comprehensive field metadata file from the `data/fields/` directory (e.g., `data/fields/EQUITY_EUR_1_TOP2500.csv`).- **Parsing and Filtering**:1.**Load All Fields**: Ingest the entire list of available data fields.2.**Identify Field Types**: Note whether each field is a `matrix` (scalar) or `vector` (event). This is a critical piece of information for each field.3.**Filter by Category**: Retain only the fields relevant to the specified `Category`.##4. AI Understands, Combines & VerifiesThis is the central, multi-stage intelligence step.1. **Handle Vector Fields**: **Crucially**, if a field is of type `vector`, it **must** be aggregated into a scalar value before being used in operators that expect scalar inputs (like arithmetic or group operators). Use `vec_avg()`, `vec_sum()`, or `vec_count()` for this purpose.2. **Find Meaningful Combinations**: The AI analyzes the `description` of scalar fields and *aggregated* vector fields to identify opportunities for economically sound combinations.3. **Construct Expressions**: The AI constructs expressions by strictly adhering to the operator syntax and using valid grouping keywords.-**Valid Grouping Keywords**: `subindustry`, `industry`, `sector`, `country`, `exchange`. These are platform-native keywords, not field names.4. **Final Verification (Mandatory)**:- Before outputting the final list, the AI **must** perform a final check on every generated expression.- For **every single field** within an expression, its type must be re-verified against the `fields.csv` file.- Any expression containing a raw `vector` field in a scalar context (e.g., direct arithmetic) **must be corrected or discarded**. This step is non-negotiable and prevents `event inputs` errors.-**Correct Example**: `group_median(snt21_2pos_mean_96 - vec_avg(snt12_lst_trgt_price), country)` (scalar minus an aggregated vector is valid).-**Incorrect Example**: `group_median(snt21_2pos_mean_96 - snt12_lst_trgt_price, country)` (This will fail because `snt12_lst_trgt_price` is a vector).##5. Save Verified Expressions- **Action**: The AI takes the final, fully verified list of alpha expressions.- **Output**: Using the `write_to_file` tool, it saves this Python list into a specified output file, ready for simulation.
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]基于操作符生成alpha的工作流分享_35591278645015.md
- **讨论数**: 8

使用的工具链参考：  [../顾问 JX79797 (华子哥/华子) (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md](../顾问 JX79797 (华子哥/华子) (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)

本工作流的主要目的是，不让一个操作符流落在外，达到每个操作符都有提交。

**使用推荐： 稀有操作符 + 常见数据集， 也可以试试小数据集碰碰运气能不能暴击**

**流程图：**

**
> [!NOTE] [图片 OCR 识别内容]
> 输入与学习 (Input & Learning)
> 本地数据检索 (Local Data Retrieval)
> 1.定义参数与学习
> 2.加载数据集元数据
> 3.加载井筛选字段
> Define Parameters & Learn
> Load Dataset Metadata
> Load & Filter Fields
> 用户输入:
> 路径:
> 路径:
> Region, Universe, Delay, Category
> dataldatasetslEQUITY_{REGION}_.一
> datalfieldslEQUITY_{REGION}_: -
> AI学习 (关键):
> 动作:
> 动作:
> 必须从datalgold_operators.csv学习操作符定义和用法
> 1.加载所有字段
> 根据'Category'筛选数据集I0
> 2.根据10筛选相关字段
> Al智能生成与验证 (Al Powered Generation & Verification)
> 输出 (Output)
> 4.A1理解。组合与验证
> 5.保存表达式
> Al Understands, Combines & Verifies
> Save Expressions
> 过程:
> 工具:
> 处理Vector: 使用'vec_avg' 等聚合
> write_to_file
> 组合字段: 寻找经济学上合理的组合
> 应用操作符:使用正确语法
> 内容:
> 最终验证:  重新检查所有字段的类型
> 生成的。经过验证的。语法正确的表达式列表
**

1. 定义参数与学习：设置配置参数并从`data/gold_operators.csv`学习操作符定义

2. 加载数据集元数据：从`data/datasets/`加载并筛选相关数据集

3. 加载并筛选字段：从`data/fields/`加载字段并识别其类型(matrix/vector)

4. AI理解、组合与验证：智能生成表达式，应用正确的操作符，并进行严格验证

5. 保存表达式：将生成的有效表达式保存到指定输出文件

**示例：**

**Cine交互输入框输入：**

```
使用 intelligent_alpha_generation_workflow.md工作流，使用ts_covariance操作符以及region eur delay 1 universe TOP2500 instrumentType Equity, 使用socialmedia category里的字段生成30个alpha表达式，不超过两个操作符，不超过两个字段
```

**生成表达式列表：**

```
expressions = ["ts_covariance(scl12_sentiment, scl12_buzz, 10)","-ts_covariance(scl12_sentiment, scl12_buzz, 20)","ts_covariance(vec_avg(scl15_d1_risk_score), vec_avg(scl15_d1_conflict), 10)","-ts_covariance(vec_avg(scl15_d1_risk_score), vec_avg(scl15_d1_conflict), 20)","ts_covariance(vec_avg(scl15_d1_trust), vec_avg(scl15_d1_fundamentalstrength), 10)","-ts_covariance(vec_avg(scl15_d1_trust), vec_avg(scl15_d1_fundamentalstrength), 20)","ts_covariance(vec_avg(scl15_d1_pricedirection), vec_avg(scl15_d1_buzz), 10)","-ts_covariance(vec_avg(scl15_d1_pricedirection), vec_avg(scl15_d1_buzz), 20)","ts_covariance(vec_avg(scl15_d1_optimism), vec_avg(scl15_d1_sentiment), 10)","-ts_covariance(vec_avg(scl15_d1_optimism), vec_avg(scl15_d1_sentiment), 20)","ts_covariance(vec_avg(scl15_d1_longshort), vec_avg(scl15_d1_stress), 10)","-ts_covariance(vec_avg(scl15_d1_longshort), vec_avg(scl15_d1_stress), 20)"...]
```

**得到可提交alpha：**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 10/13/2025 EDT
> machine_optimize_alpha
> Add Alpha to a List
> Open alpha details in new tab
> 09
> Summary
> PerlO0
> 0S
> 眙 Single Data Set Alpha
> 自
> Power Pool Alpha
> Pyramid theme: EURIDIISOCIALMEDIA X1.2
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 01/21/2023 ESI
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run: Mon, 10/13/2025,7:20 PM
> 0.0887
> -0.0923
> Power Pool Correlation
> Maximum
> Minimum
> Last Run: Mon, 10/13/2025,7:20 PM
> 0.0902
> -0.1100
> Prod Correlation
> Maximum
> Minimum
> Last Run: Mon, 10/13/2025,7:20 PM
> 0.4325
> -0.4795


**工作流内容**

```
# AI-Driven, Semantically-Aware Alpha Generation Workflow (Local)This document outlines an advanced, robust workflow for generating financial alpha expressions. The process is driven by an AI assistant, operates entirely on local data, and focuses on creating semantically meaningful and syntactically correct alphas.## Workflow Diagram```mermaidgraph TDsubgraph "输入与学习 (Input & Learning)"A[1. 定义参数与学习<br>Define Parameters & Learn<br><br><b>用户输入:</b><br>- Region, Universe, Delay, Category, Operator<br><br><b>AI学习 (关键):</b><br>- <b>必须</b>从 `data/gold_operators.csv` 学习操作符定义、参数和用法。]endsubgraph "本地数据检索 (Local Data Retrieval)"B[2. 加载数据集元数据<br>Load Dataset Metadata<br><br><b>路径 (本地):</b><br>`data/datasets/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>读取并解析CSV，根据`Category`筛选数据集ID。]C[3. 加载并筛选字段<br>Load & Filter Fields<br><br><b>路径 (本地):</b><br>`data/fields/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>1. 加载所有字段。<br>2. 根据数据集ID筛选出`Category`相关字段。<br>3. 识别每个字段的类型 (matrix vs. vector)。]endsubgraph "AI智能生成与验证 (AI-Powered Generation & Verification)"D[4. AI理解、组合与验证<br>AI Understands, Combines & Verifies<br><br><b>过程:</b><br>- <b>处理Vector:</b> 对vector类型字段使用`vec_avg`等聚合。<br>- <b>组合字段:</b> 寻找经济学上合理的组合。<br>- <b>应用操作符:</b> 使用正确语法和分组关键字。<br>- <b>最终验证 (强制):</b> 重新检查每个表达式中所有字段的类型。]endsubgraph "输出 (Output)"E[5. 保存表达式<br>Save Expressions<br><br><b>工具:</b> `write_to_file`<br><b>内容:</b> 生成的、经过验证的、语法正确的表达式列表。]endA --> B;B --> C;C --> D;D --> E;```## Detailed Steps### 1. Define Parameters & Learn- **User Input**: The user specifies the target parameters for the generation task: `Region`, `Universe`, `Delay`, `Category`, `Operator`.- **AI Learning (Crucial Step)**: The AI **must** retrieve and analyze the operator's definition, parameters, and correct syntax from the local file: `data/gold_operators.csv`.### 2. Load Dataset Metadata (Local)- **Action**: The AI reads the appropriate dataset metadata file from the `data/datasets/` directory (e.g., `data/datasets/EQUITY_EUR_1_TOP2500.csv`).- **Parsing**: It extracts `dataset_id`s that match the specified `Category`.### 3. Load & Filter Field Metadata (Local)- **Action**: The AI reads the comprehensive field metadata file from the `data/fields/` directory (e.g., `data/fields/EQUITY_EUR_1_TOP2500.csv`).- **Parsing and Filtering**:1.**Load All Fields**: Ingest the entire list of available data fields.2.**Identify Field Types**: Note whether each field is a `matrix` (scalar) or `vector` (event). This is a critical piece of information for each field.3.**Filter by Category**: Retain only the fields relevant to the specified `Category`.### 4. AI Understands, Combines & VerifiesThis is the central, multi-stage intelligence step.1. **Handle Vector Fields**: **Crucially**, if a field is of type `vector`, it **must** be aggregated into a scalar value before being used in operators that expect scalar inputs (like arithmetic or group operators). Use `vec_avg()`, `vec_sum()`, or `vec_count()` for this purpose.2. **Find Meaningful Combinations**: The AI analyzes the `description` of scalar fields and *aggregated* vector fields to identify opportunities for economically sound combinations.3. **Construct Expressions**: The AI constructs expressions by strictly adhering to the operator syntax and using valid grouping keywords.-**Valid Grouping Keywords**: `subindustry`, `industry`, `sector`, `country`, `exchange`. These are platform-native keywords, not field names.4. **Final Verification (Mandatory)**:- Before outputting the final list, the AI **must** perform a final check on every generated expression.- For **every single field** within an expression, its type must be re-verified against the `fields.csv` file.- Any expression containing a raw `vector` field in a scalar context (e.g., direct arithmetic) **must be corrected or discarded**. This step is non-negotiable and prevents `event inputs` errors.-**Correct Example**: `group_median(snt21_2pos_mean_96 - vec_avg(snt12_lst_trgt_price), country)` (scalar minus an aggregated vector is valid).-**Incorrect Example**: `group_median(snt21_2pos_mean_96 - snt12_lst_trgt_price, country)` (This will fail because `snt12_lst_trgt_price` is a vector).### 5. Save Verified Expressions- **Action**: The AI takes the final, fully verified list of alpha expressions.- **Output**: Using the `write_to_file` tool, it saves this Python list into a specified output file, ready for simulation.
```

```

```

---

### 帖子 #22: 4. Copy all files and folders from untracked directory
- **主帖链接**: https://support.worldquantbrain.com[L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md
- **讨论数**: 2

不得不说 ` `cnhkmcp``  的开发者实在是太高产了！几乎每周都有更新，有时候甚至一天能发好几个版本。这当然是一件好事，但也让人不禁疑惑： **这个版本到底更新了什么？我要不要升级？**

虽然在Pypi ( [[链接已屏蔽]) ) 上可以看到版本号的变化，但因为这个项目没有公开 GitHub 仓库，我们很难知道具体的更新内容。比如  `2.1.9`  版本引入了 ` `skills``  功能，我也是看了论坛里大佬的帖子才知道的。

于是我就萌生了一个想法：既然包是安装在本地的，我能不能在本地追踪一下每个版本的代码变动呢？

最简单的方案就是建立一个本地 Git 仓库。为了方便大家使用，我写了一个一键脚本，直接上代码。

#### 📝 脚本使用方法

#### 1.在任意目录建立一个文件夹（例如命名为  `cnhkmcp_monitor` ），后续的版本比对将在这里进行。

2.在该目录下新建一个  `.py`  文件，将下方的代码复制进去。


> [!NOTE] [图片 OCR 识别内容]
> 电脑
> 下载
> worldquant_brain
> cnhkmcp
> 修改曰期
> 大小
> update_and_track
> cnhkmcp:py
> 2026/1/1819:48
> Python File
> 7KB


3.双击运行。代码会自动初始化 Git 仓库，安装/更新  `cnhkmcp` ，并将更新后的源码复制过来（部分代码参考了“AI打工人”中的脚本）。

4.如果你之前已经运行过一次，脚本会提示你先进行 Commit，然后再更新和复制。这样利用 Git 的 Diff 功能，就能直观地看到新版本改了哪里！


> [!NOTE] [图片 OCR 识别内容]
> C:IWINDOWSIPy.exe
> 检测到 Git 仓厍
> gitignore  己存在且包含
> Lpycache
> 规则
> 企0
> 检测到未提交的更改
> J update_and_track_cnhkmcp. Dy
> ?? AI打工人
> ?? !1桌面插件/
> ?? JPP/
> ??
> init
> PJ
> ?? arfiy_API_Tool
> Janlal. 皿d
> ?? arxiy_api. Py
> ?? back
> UD/
> ??
> brain-conslltalt. md
> ??
> forum_functions. PY
> ?? UCP文件论坛版2_奶果原版启动不了浏览器就试这个/
> ?? platform
> fulnctions.Dy
> ?? sample_mCP_config: json
> ?? sliils
> ??
> User_config: json
> 例参考文档_BRAIN_Alpha_Test_Requirements_and
> md
> ??
> 例工作流_4lpha_explaination_worlf Iow. md
> 例工作流_BRAIN_G_Tips_Datafield_Exploration_Guide. md
> "
> "
> 例r作流 Batasetlpha-onatooemenperorlfloa mad
> 例工作流_daily_report_workfIow. md
> ??
> 置前运行我_安装必要依赖包. Py
> 是否要巩在提交议些再改?
> (T/I) :
> Tips


如下是2.1.9更新到2.2.0的变化，更新了哪些 Skills 非常直观。


> [!NOTE] [图片 OCR 识别内容]
> BPLORER
> CNHKMCP
> Lpycache
> AI打工人
> BRAIN_AI打工人Mac_Linux版本 zip
> 三  双击安装A1打工人Windows版本.exe
> AI桌面插件
> APP
> back_up
> mcp文件论坛版2_如果原版启动不
> 浏览器就试这个
> Skills
> brain-calculate-alpha-selfcorrQuick
> brain-data-feature-engineering
> '
> examples md
> OUTPUT_TEMPLATEmd
> referencemd
> SKILLmd
> brain-datafield-exploration-general
> LOG
> brain-dataset-exploration-general
> brain-explain-alphas
> brain-feature-implementation
> brain-how-to-pass-AlphaTest
> brain-improve-alpha-performance
> brain-nextMove-analysis
> expression_verifier
> planning
> files
> pull_BRAINSkill
> Claude_Skill_Creation_Guide.md
> _init_:py
> -With


#### 
> [!NOTE] [图片 OCR 识别内容]
> SOURCE CONTROL
> REPOSITORIES
> cnhkmcp
> 蹈
> mastert
> CHANGES
>  Changes
> IQea
> 11063064CoJsOn SNIIS IOTaIT-TCaTUIC-IMDICICIIaUO。
> idea_1768588431json skillslbrain-feature-implementatio.
> idea_ 1768588434json skillslbrain-feature-implementatio..
> idea_ 1768588438json skillslbrain-feature-implementatio..
> idea_1768588441json skillslbrain-feature-implementatio.
> idea_1768588468json skillslbrain-feature-implementatio.
> ace_lib:Py skillslbrain-feature-implementationlscripts
> fetch_dataset py skillslbrain-feature-implementationlscripts U
> helpful_functions py skillslbrain-feature-implementationl。. U
> implement_idea py skillslbrain-feature-implementationls:.
> merge_expression_listpy skillslbrain-feature-implementa.。 U
> examplesmd skillslplanning-with-files
> reference.md skillslplanning-with-files
> U
> L0G
> SKILLmd skillslplanning-with-files
> 9十
> 9+,0
> check-complete.sh skillslplanning-with-filesIscrpts
> init-session.sh skillslplanning-with-fleslscripts
> findings.md skillslplanning-with-flesltemplates
> progress md skillslplanning-with-flesltemplates
> task_plan.md skillslplanning-with-flesltemplates
> GRAPH
> 89Auto


#### 

#### 🔧 一些拓展思路

众所周知，每次更新后都需要重新配置用户名和密码，在高频更新下确实有点麻烦。基于这个脚本，其实可以修改脚本在复制文件时跳过  `user_config.json` ，再将 Agent工具的MCP 路径指向你自己的 `cnhkmcp_monitor` 目录，这样完全可以实现无痛升级。

```python

import os

import shutil

import sys

import subprocess

from pathlib import Path

import importlib.util

def is_git_repo(directory):

"""检查目录是否是git仓库"""

git_dir = Path(directory) / ".git"

return git_dir.exists()

def init_git_repo(directory):

"""初始化git仓库"""

print("正在初始化 Git 仓库...")

try:

subprocess.check_call(["git", "init"], cwd=directory)

print("✅ Git 仓库初始化成功")

return True

except subprocess.CalledProcessError as e:

print(f"❌ Git 初始化失败: {e}")

return False

except FileNotFoundError:

print("❌ 错误: 系统未安装 Git")

return False

def create_gitignore(directory):

"""创建.gitignore文件，忽略__pycache__目录"""

gitignore_path = Path(directory) / ".gitignore"

gitignore_content = """# Python cache

__pycache__/

*.py[cod]

*$py.class

# Distribution / packaging

.Python

build/

develop-eggs/

dist/

downloads/

eggs/

.eggs/

lib/

lib64/

parts/

sdist/

var/

wheels/

*.egg-info/

.installed.cfg

*.egg

# Virtual environments

venv/

ENV/

env/

# IDE

.vscode/

.idea/

*.swp

*.swo

*~

# OS

.DS_Store

Thumbs.db

"""

if gitignore_path.exists():

# 如果.gitignore已存在，检查是否包含__pycache__

with open(gitignore_path, 'r', encoding='utf-8') as f:

content = f.read()

if '__pycache__' not in content:

with open(gitignore_path, 'a', encoding='utf-8') as f:

f.write('\n# Python cache\n__pycache__/\n')

print("✅ 已更新 .gitignore 文件")

else:

print("ℹ️  .gitignore 已存在且包含 __pycache__ 规则")

else:

with open(gitignore_path, 'w', encoding='utf-8') as f:

f.write(gitignore_content)

print("✅ 已创建 .gitignore 文件")

def has_uncommitted_changes(directory):

"""检查是否有未提交的更改"""

try:

# 检查是否有未跟踪的文件或未提交的更改

result = subprocess.run(

["git", "status", "--porcelain"],

cwd=directory,

capture_output=True,

text=True,

check=True

)

return len(result.stdout.strip()) > 0

except subprocess.CalledProcessError:

return False

def prompt_commit(directory):

"""提示用户是否要提交更改"""

print("\n" + "="*50)

print("⚠️  检测到未提交的更改")

print("="*50)

# 显示状态

try:

# 配置 git 正确显示中文文件名

subprocess.run(

["git", "config", "--local", "core.quotepath", "false"],

cwd=directory,

capture_output=True

)

subprocess.run(["git", "status", "--short"], cwd=directory, check=True)

except subprocess.CalledProcessError:

pass

print("\n是否要现在提交这些更改？(y/n): ", end='')

response = input().strip().lower()

if response == 'y' or response == 'yes':

print("\n请输入提交信息: ", end='')

commit_message = input().strip()

if not commit_message:

commit_message = "Auto-commit before update"

try:

# 添加所有更改

subprocess.check_call(["git", "add", "."], cwd=directory)

# 提交

subprocess.check_call(["git", "commit", "-m", commit_message], cwd=directory)

print("✅ 更改已提交")

except subprocess.CalledProcessError as e:

print(f"❌ 提交失败: {e}")

else:

print("ℹ️  跳过提交，继续执行...")

def check_and_init_git():

"""检查并初始化Git仓库"""

current_dir = Path.cwd()

if not is_git_repo(current_dir):

print("\n📦 未检测到 Git 仓库")

print("是否要初始化 Git 仓库？(y/n): ", end='')

response = input().strip().lower()

if response == 'y' or response == 'yes':

if init_git_repo(current_dir):

create_gitignore(current_dir)

print("✅ Git 仓库配置完成\n")

else:

print("ℹ️  跳过 Git 初始化\n")

else:

print("✅ 检测到 Git 仓库")

create_gitignore(current_dir)

# 检查是否有未提交的更改

if has_uncommitted_changes(current_dir):

prompt_commit(current_dir)

else:

print("✅ 工作目录干净，没有未提交的更改\n")

def install_package():

print("正在安装/更新 cnhkmcp 包...")

try:

subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "cnhkmcp"])

except subprocess.CalledProcessError as e:

print(f"安装失败: {e}")

sys.exit(1)

def get_package_path(package_name):

# 重新加载 finder 以防刚安装完

importlib.invalidate_caches()

spec = importlib.util.find_spec(package_name)

if spec and spec.origin:

return Path(spec.origin).parent

return None

def main():

# 0. Check and initialize Git repository

check_and_init_git()

# 1. Install CNHKMCP

install_package()

# 2. Locate the package

pkg_path = get_package_path("cnhkmcp")

if not pkg_path:

# Fallback: try site-packages directly if spec fails

import site

for site_pkg in site.getsitepackages():

potential_path = Path(site_pkg) / "cnhkmcp"

if potential_path.exists():

pkg_path = potential_path

break

if not pkg_path:

print("错误: 无法找到 cnhkmcp 包安装路径。")

sys.exit(1)

print(f"cnhkmcp 安装位置: {pkg_path}")

# 3. Locate 'untracked' folder

untracked_dir = pkg_path / "untracked"

if not untracked_dir.exists():

print(f"错误: 在 {pkg_path} 中未找到 'untracked' 文件夹")

sys.exit(1)

# 4. Copy all files and folders from untracked directory

target_dir = Path.cwd()

print(f"正在将 untracked 目录下的所有内容复制到: {target_dir}")

copied_count = 0

skipped_count = 0

for item in untracked_dir.iterdir():

src = item

dst = target_dir / item.name

try:

if item.is_file():

shutil.copy2(src, dst)

print(f"✅ 已复制文件: {item.name}")

copied_count += 1

elif item.is_dir():

if dst.exists():

shutil.rmtree(dst)

shutil.copytree(src, dst)

print(f"✅ 已复制文件夹: {item.name}")

copied_count += 1

except Exception as e:

print(f"⚠️ 警告: 复制 {item.name} 时出错: {e}")

skipped_count += 1

print(f"\n📊 复制完成: 成功 {copied_count} 项, 跳过 {skipped_count} 项")

if __name__ == "__main__":

main()

```

---

### 帖子 #23: 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法
- **主帖链接**: https://support.worldquantbrain.com[L2] 【AI Alphas Competition 2025比赛】了解最新比赛的规则和玩法_35799099514647.md
- **讨论数**: 8

```
以下是详细说明，帮助您参加比赛。

1. 使用 ACE 库来模拟生成的 Alphas。
2. 使用每个子 Alphas 的父 Alphas ID 来标记每个子 Alpha。
3. 为子 Alpha 添加描述。
4. 模拟和标记的示例逻辑：

#### **提交要求**
1. **SuperAlphas** 必须使用链接到相同父 Alpha ID 的子 Alphas 构建。
2. 通过平台表单提交您的**SuperAlphas**和机器（代码）。
3. 仅考虑您**最后一次机器提交**。

---

### 帖子 #24: 【Alpha模版】模版群助我60天点亮60个塔Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha模版】模版群助我60天点亮60个塔Alpha Template_35253150989719.md
- **讨论数**: 87

**一、前言**

**我是一位freshman，7月1日转正，至今提交295个atom，点亮64座塔。**


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-23 July 1s,2025
> SEptember 30-h,2025
> Gold
> Erpert
> Master
> Grandas-er
> Signals
> 295
> Reached Grandmaster
> Pyramids Completed
> 64
> Reached Grandmaster
> Combined Alpha Performance
> 1.1
> 0.9 more to Grandmaster
> Combined Selected Alpha Performance
> 3.09
> Reached Grandmaster
> Combined Power Pool Alpha Performance
> 1.67



> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st 2025
> September 3oth, 2025
> Operazors pEr Alpna
> Operators Used
> Fields per Alpha
> 3.18
> 81
> 1.55
> Fielos USEJ
> Communizyaczivity
> Waxsinulati?nstreak
> 317
> 35.3
> 215
> Simulationactiviey
> Submissionactiit
> AUE
> Sep
> AUE
> Sep



> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st 2025
> September 3oth, 2025
> Catego
> US
> eIR
> CHN
> L3S
> 3O =
> Esp nEs
> FundaTsta
> ImTaIT=
> IO
> Inaions
> Nro
> Nodsl
> Nsws
> T3t27
> Price Voluns
> Ris
> TTmn
> MOTCITETESC
> Sciallls-la


**二、方法论**

1. 经济学原理是静态框架，而股市运行于人性的动态博弈之中。  
2. 任何超额收益（Alpha）一旦被广泛追逐，便会因拥挤而失效。  
3. 故兵无常势，水无常形，唯有因时应变者，方能持续制胜。

**具体做法：**

**1. 穷举所有：** 挑选可用的模版。比如，一元、二元或三元模版

**2. 避免重复：** 从模版层降低相关性。比如scale、rank、zscore等单操作符模版，多数情况下是重复的，不要堆叠，浪费回测资源。

**3. 先随机再深入：** 首先，对准一个想要点亮的数据集；先用shuffle的方法，随机取样80个组合，计算每个模版的因子密度；如果某个模版因子密度大，就深入挖掘。

[参考虎哥模版实证及其改进效果评价](../顾问 MZ45384 (大角羊) (Rank 51)/[Commented] 【Alpha灵感】虎哥模版实证及其改进效果评价Alpha Template_33768594280343.md)

**三、模版框架（举例）**

**1. 一元模版（模版层面尽量不要有重复，从模版底层降低self-corr）**

```
for a in data_fields:    if index == 0:        # 斜率        expr = f"ts_regression(ts_zscore({a}, 500), ts_step(1), 500, rettype=2)"        factor_expressions.append(expr)    elif index == 1:        # 增长率        expr = f"ts_delta(ts_delta({a}, 252)/ts_delay({a}, 252),252)"        factor_expressions.append(expr)    elif index == 2:        # 增长率        expr = f"ts_delta({a}, 252)/ts_delay({a}, 252)"        factor_expressions.append(expr)    elif index == 3:        # 自回归斜率        expr = f"ts_regression(ts_delta({a}, 252), ts_delta({a}, 500), 500, rettype=2)"        factor_expressions.append(expr)    elif index == 4:        # 平方动量        expr = f"ts_mean(signed_power(ts_delta({a}, 252), 2), 500)"        factor_expressions.append(expr)    elif index == 5:        # 衰减加权动量        expr = f"ts_decay_linear(ts_delta({a}, 252), 500)"        factor_expressions.append(expr)    elif index == 6:        # 排名反转        expr = f"reverse(ts_rank(ts_zscore({a}, 500), 500))"        factor_expressions.append(expr)    elif index == 7:        # 对数平滑        expr = f"log(abs(ts_delta({a}, 500)) + 0.000001)"        factor_expressions.append(expr)    elif index == 8:        # 符号保留幂        expr = f"signed_power(ts_delta({a}, 500), 2)"        factor_expressions.append(expr)    elif index == 9:        # 差分层叠        expr = f"ts_delta(ts_delta({a}, 252), 500)"        factor_expressions.append(expr)
```

**2. 二元模版（降self-corr）**

```
    for a, b in combinations(data_fields, 2):        if index == 0:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500)"            factor_expressions.append(expr)        elif index == 1:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500, rettype=2)"            factor_expressions.append(expr)        elif index == 2:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500, rettype=6)"            factor_expressions.append(expr)        elif index == 3:            expr = f"ts_regression({a}, {b}, 252, rettype=2)"            factor_expressions.append(expr)        elif index == 4:            expr = f"ts_regression({a}, {b}, 500, rettype=2)"            factor_expressions.append(expr)        elif index == 5:            expr = f"regression_neut(s_log_1p({a}), s_log_1p({b}))"            factor_expressions.append(expr)        elif index == 6:            expr = f"vector_neut({a}, {b})"            factor_expressions.append(expr)        elif index == 7:            expr = f"ts_delta_limit({a}, {b}, limit_volume=0.1)"            factor_expressions.append(expr)        else:            continue
```

**3. 三元模版（去self-corr）**

```
    for a, b, c in combinations(data_fields, 3):
        if index == 0:
            # 联合中性化：a 在 b 和 c 上的向量正交
            expr = f"vector_neut(vector_neut({a}, {b}), {c})"
        elif index == 1:
            # 分层回归残差（先对 b 中性化，再对 c）
            expr = f"regression_neut(regression_neut({a}, {b}), {c})"
        elif index == 2:
            # 带约束的时序变化（delta limit，以 b 和 c 的均值为基准）
            expr = f"ts_delta_limit({a}, ({b} + {c}) / 2, limit_volume=0.1)"
        elif index == 3:
            # 三变量时序相关性（a 与 b 的相关性，用 c 作权重或窗口调节）
            expr = f"ts_corr(ts_zscore({a}, 252), ts_zscore({b}, 252), 252) * {c}"
        elif index == 4:
            # 动态排序择时（a 在 b 和 c 构成的分组中做 ts_rank）
            expr = f"ts_rank(group_mean({a}, {b}), 500) * {c}"  # 假设 b 为分组字段
        elif index == 5:
            # 三重交互项（非线性放大）
            expr = f"ts_zscore({a}, 500) * ts_zscore({b}, 500) * ts_zscore({c}, 500)"
        elif index == 6:
            # 条件切换（c 为条件，选择 a 或 b）
            expr = f"if_else({c} > ts_mean({c}, 500), {a}, {b})"
        else:
            continue  # 超出范围跳过
```

**四、应用举例（CHN很难，但实际上也扛不住几次冲锋，突破只是时间问题）**

**1.analyst举例**  
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 0827/2025 EOT
> anonymOUs
> Udd Nphato a Ust
> Code
> IS Summary
> Period
> aIeC
> aVB(a_
> Data SEtJphs
> Powver Pool Hphs
> Pyrsmidthems: CHNDTIANALYST 1.
> bts_decay_Iinear(a;126)
> ts_decay_exP_window(a,
> 252
> factor
> 951;
> siened_power (b,0.5)
> Agaregate
> Uata
> SHelo
> 1.13
> 10.08%
> 1.11
> 12.1796
> 17.39%
> 24.1596o0
> SIIUIatIOn
> Settings
> Year
> Sharpe
> TurOVeT
> Fltss
> Rtur
> Uawdown
> Marln
> Long Cnt
> Short Cot
> Istrut Type
> Regl
> Uelse
> Language
> Ia
> Dlay
> Truncatlon
> Neutrallatlon
> Pastewrtato
> HaN Hanlng
> UnltHandlng
> Max Trate
> EaJi?
> TLN
> TOFZJ
> HasUTEsSIUT
> 7.03
> Crowwire Factors
> TT
> 2013
> 231
> 13.88:
> 250
> 12
> 7.375
> 35.+:
> 201-
> 03
> 11.09::
> 1
> 8.115
> 1.3:
> 2015
> 126
> 1.20:
> 155
> 8.105
> 30.74:
> 15
> 2015
> 353
> 13.5::
> 2233
> 3.235
> 一7:
> 1
> Clone Alpha
> 2017
> 715
> 13.55::
> 1 2
> 7.32
> 37:
> 2013
> 5:
> 12
> 7.395
> 5:
> 13
> N Chart
> Prl
> 2019
> 1.10
> 17:
> &9
> 7.27
> 16.735:
> 133
> 2020
> 032
> 363:
> 0.13
> 2:
> 11.715
> -7.55
> 138
> 120
> 3.90:
> 12
> 10.255
> 41.575:
> 2022
> 277
> 3.51:
> 727
> 8.575
> 66冼:
> 126
> SJOK
> 2023
> +38
> 13.60:
> 311
> 0.305
> 69.5:
> 159
> ,DJOK
> ZSOK
> 医 Correlation
> Self Correlation
> TIATTIUITTI
> STITUCT
> L1| YUII
> J"1_
> Jan '1s
> Jan 16
> Jan 18
> Jar 19
> Jan 21
> Jan 2
> Jan 23
> Snsle
> J_


**2. fundamental举例**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 0827/2025 EOT
> anonymOUs
> Mdd Nphato a Lst
> Code
> w IS Summary
> PErIoU
> TJ5
> Data SEt-Ipha
> 昵 Powver Pool Nphs
> Pyrsmidthems: CHNDTIFUNDAMENTAL *1.
> bts_decay_exp_window(divide
> ts_ZsCOre
> 5881
> ts_std_dev(ts_ZsCOTe(a」
> 63),
> 2521
> 2481
> factor-o.5);
> siened_power (b,
> ABaregate Data
> SIIJIU
> SU'
> OLU
> 1.45
> 8.35%
> 1.18
> 8.269
> 14.959
> 19.799600
> SIIUIatIOT
> SettIIes
> Vear
> Sha
> TuIOeF
> Ftss
> Retwrs
> Uawdown
> Varwln
> Long Cnt
> Short Cot
> Tnstuwt Type
> Reglo
> Werse
> URa
> Dcay
> Dlay
> Truncatlon
> Neutallalon
> Pastewrtat
> NaNHanl
> Unlt Handlng
> Max Trade
> EaJi?
> TLN
> TOFZJU
> TasUYTESSIUT
> 7.03
> Rl
> 「T
> 2013
> 3_
> 2
> 12025
> 251:
> 7.51
> 014
> 102
> 1.47
> 3.115
> 15:
> 3
> 2015
> 1.17
> 7
> 7.135
> 145:
> 1.35
> V
> 2016
> 7 21
> 3.2
> 12525
> 15::
> 895
> 1
> Clone Alpha
> 2017
> 71
> 11.37
> 2335
> 41.415
> 1
> 2013
> 642
> 2905
> 436:
> 03
> 11
> N Chart
> Pnl
> 119
> 7.4
> 1.405
> 79::
> -.-3
> 2020
> 7.57
> 0.4
> 18
> 58
> 190
> 152
> 2021
> 10.55
> 0.5
> 7.20
> 13:
> 1.1
> 123
> 2022
> 9.7
> 3.315
> :::
> 21.2-
> 177
> 1
> CJOK
> 2023
> 2.36
> 7115
> 3.3
> 11.575
> 0:
> 3.3150
> 105
> Z,SJOK
> 邑 Correlation
> Self Correlation
> TATTIUITT
> I
> 11| YUIII
> Jn '11
> Jan"1s
> Jan 16
> Jan '17
> Jan 13
> an 19
> Jan 2
> J3n*23
> SRSIE


**3. model举例**  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Tarint
> 9+
> ZSCOre(BrouP_rank(ts
> ZSCOFe
> aB(n114_
> 126)Jindustry),
> 500);
> 毗 Sirele Data Set Alphs
> # PowVET Po?
> JIChS
> Fyrsmidthem: CHNDIIMODEL ~1.5
> e2ate
> Data
> SNUe
> TUTIU
> Reluiri
> eUJUU
> MJit
> 1.35
> 5.43%
> 88
> 5.33%
> 10.16%
> 9,659600
> SmMJaTiNn
> Settings
> InstrumentType
> Reglo
> Language
> Decay
> Delay
> Truncatlon
> N-utrallatlon
> Pasteurtato
> NaN Hanlling
> Unlt Handlng
> Max Trade
> Year
> Sharpe
> Turwower
> Fitss
> Returs
> Uawdown
> Vargln
> Long Cnt
> Short Comt
> Eovig
> TLN
> TTTTII
> Fast Expression
> Crowdine
> 
> WErt
> 2013
> 2
> 5.80:
> 35
> 5-5
> 311
> 201-
> ~32
> 5.39:
> 1.1:
> 6.355
> 351:
> 2015
> 5.80:
> &423
> 9.5-5
> -9.74:
> Clone Alpha
> 2016
> 20
> 41
> 2.705
> 12.85:
> 1375
> 5.10:
> 3汀
> 0.965
> 35.1
> 111
> Chart
> 2013
> 1.97:
> 」5
> 3.21
> 三:
> 11E5
> 2019
> C 
> Z
> -.335
> -5.5:
> 1J
> 2020
> 771
> 50:
> 0.D0
> ~JJ:
> 3.575
> 01
> 1Es
> 53
> 0.93
> SEE
> 435
> 一』_
> 112
> 2022
> 5.85:
> 12
> 3.735
> 20.4:
> 110
> 2023
> 139
> 1.81:
> 715
> 0.J5
> 89.517:
> DJOK
> 医 Correlation
> J"11
> Jan 16
> Jan"
> Jar13
> Jar 19
> a*20
> Jan 21
> Jan -2
> J*23
> Self Correlation
> MJuirIuir
> UinirUrr
> LJlTUI
> CVeC
> ABBT
> Uerse


**4. pv举例**


> [!NOTE] [图片 OCR 识别内容]
> ACNV
> Cregtsd 08302025EOT
> 3nOTyTOUs
> Add Alphato 3 List
> Code
> 4 IS
> Summary
> Period
> asts_quantile(ts_delta_limit (VeC_aVg
> VeC_aVg PV27
> Iimit_Volume=B.1)
> 580);
> ] Sirale Data Set Alphs
> ] Powe
> Pool Nphs
> Fyrsmid theme: CHNDTIPV*1.3
> ABgregate Data
> SIaru
> Fiues
> CO
> 1.30
> 9.63%
> 1.21
> 10.8696
> 18.67%
> 22.5696oo
> SIMJaTiO
> Settings
> Instument Type
> Reglo
> Language
> Decay
> Truncaton
> Neutrallaton
> Cast71
> NaN Hanllng
> Unlt Handlng
> Max Trade
> Sharp
> Turower
> C
> Retwrns
> Uawdown
> Marqln
> Long Cont
> Short Cowmt
> EOJiD
> TLN
> TSPZJU
> Fas: ECressor
> 7.03
> Marer
> Vrr
> 7113
> 9.3
> 0.7
> 1.055
> 130:
> 2
> CIT
> 1.595
> 419:
> 3.79
> 2015
> 0.33
> 1
> 072
> -3.315
> 157:
> 14.5s
> Clone Alpha
> 2015
> 7.53
> 2
> 15.545
> 5:
> 79
> 2017
> 31
> 3.7
> 21.405;
> 345:
> 95
> Chart
> 2013
> 713
> 1.5
> 155
> 13:
> 3.165
> Pnl
> -
> 0.5
> JSu
> +3:
> 53
> 2020
> 7
> 0.
> 5.795
> 13:
> 3-7
> 12
> 2021
> 2.13
> 11.1
> _5
> 45:
>  _=
> SJOK
> 202
> 11.72;
> 95
> 4:
> 2.3
> 15
> CJOK
> 2023
> 9.9
> 17.435
> .16::
> 31.13
> 17
> SJOK
> Risk neutralized
> ABaregate Data
> SHer
> MaTUIT
> 1.65
> 9.6390
> 1.14
> 5.9796
> 17.6290
> 12.4
> 9o0
> Js '1
> Janus
> Ian l6
> Jan"17
> Jar 13
> Ja 20
> lan -1
> Jan -
> J3n23
> 〈PV27
> Uene
> Cl
> T019


**五、总结（任正非同志的经典语录——与君共勉）**

“华为坚定不移28年只对准通信领域这个‘城墙口’冲锋。我们成长起来后，坚持只做一件事，在一个方面做大。华为只有几十人的时候就对着一个‘城墙口’进攻，几百人、几万人的时候也是对着这个‘城墙口’进攻，现在十几万人还是对着这个‘城墙口’冲锋。密集炮火，饱和攻击。”

---

### 帖子 #25: 【check王】验证表达式是否正确的脚本——七十二变黄金搭档
- **主帖链接**: https://support.worldquantbrain.com[L2] 【check王】验证表达式是否正确的脚本七十二变黄金搭档_36740689434391.md
- **讨论数**: 20

使用72变或者大模型生成的alpha表达式可能有语法错误，基于PLY(Python Lex-Yacc)写了第一版用于校验表达式是否正确

使用方法

1.安装库

pip install ply

2.执行脚本(脚本名我命名为expression_validator.py)

```
python expression_validator.py
```

会提示输入json文件路径，如果你把脚本放到cnhkmcp\untracked/APP目录下，72变生成的alpha刚好放在Tranformer/output/Alpha_generated_expressions.json文件中，回车执行即可

```
请输入要校验的表达式JSON文件路径（默认：Tranformer/output/Alpha_generated_expressions.json）: 
```

执行后会生成两个文件Alpha_generated_expressions_success.json 和Alpha_generated_expressions_error.json 对应符合规则和不符合的。

由于是第一版本，目前主要校验表达式中操作符的使用，字段主要校验是不是字母数字下划线组成。有许多不完善的地方，如果有不对的测试用例欢迎在评论区补充

代码：

```
#!/usr/bin/env python3# -*- coding: utf-8 -*-"""表达式验证器 - 使用抽象语法树验证字符串表达式格式是否正确本模块实现了一个能够检测字符串表达式格式是否正确的系统，基于PLY(Python Lex-Yacc)构建词法分析器和语法分析器，识别表达式中的操作符、函数和字段，并验证其格式正确性。"""import reimport sysimport jsonimport osfrom typing import List, Dict, Any, Optional, Tuple# 尝试导入PLY库，如果不存在则提供安装提示try:    import ply.lex as lex    import ply.yacc as yaccexcept ImportError:    print("错误: 需要安装PLY库。请运行 'pip install ply' 来安装。")    sys.exit(1)# 1. 定义支持的操作符和函数supported_functions = {    # Group 类别函数    'group_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_mean': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'group_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_rank': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_vector_proj': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_normalize': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'category', 'expression', 'expression', 'expression']},    'group_extra': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_backfill': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression'], 'param_names': ['x', 'cat', 'days', 'std']},    'group_scale': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_count': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_neutralize': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_multi_regression': {'min_args': 4, 'max_args': 9, 'arg_types': ['expression'] * 9},    'group_cartesian_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['category', 'category']},    'combo_a': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},        # Transformational 类别函数    'right_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'bucket': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 第二个参数可以是string类型的range参数    'tail': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression']},    'left_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'trade_when': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'generate_stats': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},        # Cross Sectional 类别函数    'winsorize': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression'], 'param_names': ['x', 'std']},    'rank': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_proj': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'vector_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'multi_regression': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # 支持多个自变量        # Time Series 类别函数    'ts_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_mean': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delay': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_corr': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_returns': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'mode']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_backfill': {'min_args': 2, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'string']},    'days_from_last_change': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'last_diff_value': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_scale': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_entropy': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'd', 'buckets']},    'ts_step': {'min_args': 1, 'max_args': 1, 'arg_types': ['number']},    'ts_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_co_kurtosis': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'inst_tvr': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_exp_window': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'factor']},    'ts_av_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_kurtosis': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_diff': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_arg_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_cps': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_rank': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_ir': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_theilsen': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'hump_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_weighted_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_quantile': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'string']},    'ts_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_count_nans': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_covariance': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_co_skewness': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_min_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_linear': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'boolean']},    'jump_decay': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'number', 'expression', 'number', 'number'], 'param_names': ['x', 'd', 'stddev', 'sensitivity', 'force']},    'ts_moment': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'k']},    'ts_arg_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_regression': {'min_args': 3, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number'], 'param_names': ['y', 'x', 'd', 'lag', 'rettype']},    'ts_skewness': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'kth_element': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'hump': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'hump']},    'ts_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delta': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_poly_regression': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'number', 'number']},    'ts_target_tvr_decay': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number'], 'param_names': ['x', 'lambda_min', 'lambda_max', 'target_tvr']},    'ts_target_tvr_delta_limit': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number']},    'ts_target_tvr_hump': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number']},    'ts_delta_limit': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},        # Special 类别函数    'inst_pnl': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'self_corr': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'in': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'universe_size': {'min_args': 0, 'max_args': 0, 'arg_types': []},        # Missing functions from operators.py    'quantile': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'driver', 'sigma']},  # quantile(x, driver = gaussian, sigma = 1.0)    'normalize': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'boolean', 'number']},  # normalize(x, useStd = false, limit = 0.0)    'zscore': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # zscore(x)        # Logical 类别函数    'or': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'and': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'not': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # 注意：这是关键字    'is_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'is_not_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'less': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'is_finite': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'if_else': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'not_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'less_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},        # Vector 类别函数    'vec_kurtosis': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_min': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_count': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_sum': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_skewness': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_max': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_avg': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_range': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_choose': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'nth']},    'vec_powersum': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},    'vec_stddev': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_percentage': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'percentage']},    'vec_ir': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_norm': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'ts_percentage': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'percentage']},    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},        # Additional functions from test cases    'rank_by_side': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'rate', 'scale']},    'log_diff': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_mask': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'ts_partial_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'ts_triple_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'clamp': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},    'keep': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'condition', 'period']},    'replace': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'target', 'dest']},    'filter': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'h', 't']},    'one_side': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'string'], 'param_names': ['x', 'side']},    'scale_down': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},        # Arithmetic 类别函数    'add': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # add(x, y, filter=false)    'multiply': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 99 + ['boolean'], 'param_names': ['x', 'y', 'filter']},  # multiply(x, y, ..., filter=false)    'sign': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'subtract': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # subtract(x, y, filter=false)    'pasteurize': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'log': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'purify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'arc_tan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'max': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # max(x, y, ...)    'to_nan': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # to_nan(x, value=0, reverse=false)    'abs': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sigmoid': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'divide': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # divide(x, y)    'min': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # min(x, y, ...)    'tanh': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_out': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},  # nan_out(x, lower=0, upper=0)    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # signed_power(x, y)    'inverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'round': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sqrt': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    's_log_1p': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'reverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # -x    'power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # power(x, y)    'densify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'floor': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},}# 2. 定义group类型字段group_fields = {    'sector', 'subindustry', 'industry', 'exchange', 'country', 'market'}# 3. 有效类别集合valid_categories = group_fields# 4. 字段命名模式 - 只校验字段是不是数字字母下划线组成field_patterns = [    re.compile(r'^[a-zA-Z0-9_]+$'),  # 只允许数字、字母和下划线组成的字段名]# 4. 抽象语法树节点类型class ASTNode:    """抽象语法树节点基类"""    def __init__(self, node_type: str, children: Optional[List['ASTNode']] = None,                  value: Optional[Any] = None, line: Optional[int] = None):        self.node_type = node_type  # 'function', 'operator', 'field', 'number', 'expression'        self.children = children or []        self.value = value        self.line = line        def __str__(self) -> str:        return f"ASTNode({self.node_type}, {self.value}, line={self.line})"        def __repr__(self) -> str:        return self.__str__()class ExpressionValidator:    """表达式验证器类"""        def __init__(self):        """初始化词法分析器和语法分析器"""        # 构建词法分析器        self.lexer = lex.lex(module=self, debug=False)        # 构建语法分析器        self.parser = yacc.yacc(module=self, debug=False)        # 错误信息存储        self.errors = []        # 词法分析器规则    tokens = ('FUNCTION', 'FIELD', 'NUMBER', 'LPAREN', 'RPAREN',               'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'COMMA', 'CATEGORY',              'EQUAL', 'ASSIGN', 'IDENTIFIER', 'STRING', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'NOTEQUAL', 'BOOLEAN')        # 忽略空白字符    t_ignore = ' \t\n'        # 操作符 - 注意顺序很重要，长的操作符要放在前面    t_PLUS = r'\+'    t_MINUS = r'-'    t_TIMES = r'\*'    t_DIVIDE = r'/'    t_LPAREN = r'\('    t_RPAREN = r'\)'    t_COMMA = r','        t_EQUAL = r'=='    t_NOTEQUAL = r'!='    t_GREATEREQUAL = r'>='    t_LESSEQUAL = r'<='    t_GREATER = r'>'    t_LESS = r'<'    t_ASSIGN = r'='        # 数字（整数和浮点数）    def t_NUMBER(self, t):        r'\d+\.?\d*'        if '.' in t.value:            t.value = float(t.value)        else:            t.value = int(t.value)        return t        # 字符串 - 需要放在所有其他标识符规则之前    def t_STRING(self, t):        r"'[^']*'|\"[^\"]*\""        # 去除引号        t.value = t.value[1:-1]        return t        # 函数和字段名    def t_IDENTIFIER(self, t):        r'[a-zA-Z_][a-zA-Z0-9_]*'        # 检查是否为布尔值        if t.value.lower() in {'true', 'false'}:            t.type = 'BOOLEAN'            t.value = t.value.lower()  # 转换为小写以保持一致性        else:            # 查看当前token后面的字符，判断是否为参数名（后面跟着'='）            lexpos = t.lexpos            next_chars = ''            if lexpos + len(t.value) < len(t.lexer.lexdata):                # 查看当前token后面的字符，跳过空格                next_pos = lexpos + len(t.value)                while next_pos < len(t.lexer.lexdata) and t.lexer.lexdata[next_pos].isspace():                    next_pos += 1                if next_pos < len(t.lexer.lexdata):                    next_chars = t.lexer.lexdata[next_pos:next_pos+1]                        # 如果后面跟着'='，则为参数名            if next_chars == '=':                t.type = 'IDENTIFIER'            # 如果后面跟着'('，则为函数名            elif next_chars == '(':                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为参数名（支持更多参数名）            elif t.value in {'std', 'k', 'lambda_min', 'lambda_max', 'target_tvr', 'range', 'buckets', 'lag', 'rettype', 'mode', 'nth', 'constant', 'percentage', 'driver', 'sigma', 'rate', 'scale', 'filter', 'lower', 'upper', 'target', 'dest', 'event', 'sensitivity', 'force', 'h', 't', 'period', 'stddev', 'factor', 'k', 'useStd', 'limit', 'gaussian', 'uniform', 'cauchy'}:                t.type = 'IDENTIFIER'            # 检查是否为函数名（不区分大小写）            elif t.value.lower() in supported_functions:                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为有效类别            elif t.value in valid_categories:                t.type = 'CATEGORY'            # 检查是否为字段名            elif self._is_valid_field(t.value):                t.type = 'FIELD'            else:                # 其他标识符，保留为IDENTIFIER类型                t.type = 'IDENTIFIER'        return t        # 行号跟踪    def t_newline(self, t):        r'\n+'        t.lexer.lineno += len(t.value)        # 错误处理    def t_error(self, t):        if t:            # 检查是否为非法字符            if not re.match(r'[a-zA-Z0-9_\+\-\*/\(\)\,\s=<>!]', t.value[0]):                # 这是一个非法字符                self.errors.append(f"非法字符 '{t.value[0]}' (行 {t.lexer.lineno})")            else:                # 这是一个非法标记                self.errors.append(f"非法标记 '{t.value}' (行 {t.lexer.lineno})")            # 跳过这个字符，继续处理            t.lexer.skip(1)        else:            self.errors.append("词法分析器到达文件末尾")        # 语法分析器规则    def p_expression(self, p):        """expression : comparison                      | expression EQUAL comparison                      | expression NOTEQUAL comparison                      | expression GREATER comparison                      | expression LESS comparison                      | expression GREATEREQUAL comparison                      | expression LESSEQUAL comparison"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_comparison(self, p):        """comparison : term                      | comparison PLUS term                      | comparison MINUS term"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_term(self, p):        """term : factor                | term TIMES factor                | term DIVIDE factor"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_factor(self, p):        """factor : NUMBER                  | STRING                  | FIELD                  | CATEGORY                  | IDENTIFIER                  | BOOLEAN                  | MINUS factor                  | LPAREN expression RPAREN                  | function_call"""        if len(p) == 2:            # 数字、字符串、字段、类别或标识符            if p.slice[1].type == 'NUMBER':                p[0] = ASTNode('number', value=p[1])            elif p.slice[1].type == 'STRING':                p[0] = ASTNode('string', value=p[1])            elif p.slice[1].type == 'FIELD':                p[0] = ASTNode('field', value=p[1])            elif p.slice[1].type == 'CATEGORY':                p[0] = ASTNode('category', value=p[1])            elif p.slice[1].type == 'BOOLEAN':                p[0] = ASTNode('boolean', value=p[1])            elif p.slice[1].type == 'IDENTIFIER':                p[0] = ASTNode('identifier', value=p[1])            else:                p[0] = p[1]        elif len(p) == 3:            # 一元负号            p[0] = ASTNode('unop', [p[2]], {'op': p[1]})        elif len(p) == 4:            # 括号表达式            p[0] = p[2]        else:            # 函数调用            p[0] = p[1]        def p_function_call(self, p):        '''function_call : FUNCTION LPAREN args RPAREN'''        p[0] = ASTNode('function', p[3], p[1])        def p_args(self, p):        '''args : arg_list                | empty'''        if len(p) == 2 and p[1] is not None:            p[0] = p[1]        else:            p[0] = []        def p_arg_list(self, p):        '''arg_list : arg                   | arg_list COMMA arg'''        if len(p) == 2:            p[0] = [p[1]]        else:            p[0] = p[1] + [p[3]]        def p_arg(self, p):        '''arg : expression              | IDENTIFIER ASSIGN expression'''        if len(p) == 2:            p[0] = {'type': 'positional', 'value': p[1]}        else:            p[0] = {'type': 'named', 'name': p[1], 'value': p[3]}        def p_empty(self, p):        '''empty :'''        p[0] = None        # 语法错误处理    def p_error(self, p):        if p:            self.errors.append(f"语法错误在位置 {p.lexpos}: 非法标记 '{p.value}'")        else:            self.errors.append("语法错误: 表达式不完整")        def _is_valid_field(self, field_name: str) -> bool:        """检查字段名是否符合模式"""        for pattern in field_patterns:            if pattern.match(field_name):                return True        return False        def validate_function(self, node: ASTNode, is_in_group_arg: bool = False) -> List[str]:        """验证函数调用的参数数量和类型"""        function_name = node.value        args = node.children        function_info = supported_functions.get(function_name)                if not function_info:            return [f"未知函数: {function_name}"]                errors = []                # 检查参数数量        if len(args) < function_info['min_args']:            errors.append(f"函数 {function_name} 需要至少 {function_info['min_args']} 个参数，但只提供了 {len(args)}")        elif len(args) > function_info['max_args']:            errors.append(f"函数 {function_name} 最多接受 {function_info['max_args']} 个参数，但提供了 {len(args)}")                # 处理参数验证        # 跟踪已使用的位置参数索引        positional_index = 0                # 对于所有函数，支持命名参数        for arg in args:            if isinstance(arg, dict):                if arg['type'] == 'named':                    # 命名参数                    if 'param_names' in function_info and arg['name'] in function_info['param_names']:                        # 查找参数在param_names中的索引                        param_index = function_info['param_names'].index(arg['name'])                        if param_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][param_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, param_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    # 对于winsorize函数，支持std和clip参数                    elif function_name == 'winsorize' and arg['name'] in ['std', 'clip']:                        arg_errors = self._validate_arg_type(arg['value'], 'number', 0, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    # 对于bucket函数，支持'range'和'buckets'参数                    elif function_name == 'bucket' and arg['name'] in ['range', 'buckets']:                        # range和buckets参数应该是string类型                        arg_errors = self._validate_arg_type(arg['value'], 'string', 1, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    else:                        errors.append(f"函数 {function_name} 不存在参数 '{arg['name']}'")                elif arg['type'] == 'positional':                    # 位置参数（字典形式）                    # 对于winsorize函数，第二个参数必须是命名参数                    if function_name == 'winsorize' and positional_index == 1:                        errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                    # 对于ts_moment函数，第三个参数必须是命名参数                    elif function_name == 'ts_moment' and positional_index == 2:                        errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                    else:                        # 验证位置参数的类型                        if positional_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][positional_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, positional_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    positional_index += 1                else:                    # 其他字典类型参数                    errors.append(f"参数 {positional_index+1} 格式错误")                    positional_index += 1            else:                # 位置参数（直接ASTNode形式）                # 对于winsorize函数，第二个参数必须是命名参数                if function_name == 'winsorize' and positional_index == 1:                    errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                # 对于ts_moment函数，第三个参数必须是命名参数                elif function_name == 'ts_moment' and positional_index == 2:                    errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                else:                    # 验证位置参数的类型                    if positional_index < len(function_info['arg_types']):                        expected_type = function_info['arg_types'][positional_index]                        arg_errors = self._validate_arg_type(arg, expected_type, positional_index, function_name, is_in_group_arg)                        errors.extend(arg_errors)                positional_index += 1                return errors        def _validate_arg_type(self, arg: ASTNode, expected_type: str, arg_index: int, function_name: str, is_in_group_arg: bool = False) -> List[str]:        """验证参数类型是否符合预期"""        errors = []                # 首先检查是否是group类型字段，如果是则只能用于Group类型函数        # 但是如果当前函数是group_xxx或在group函数的参数链中，则允许使用        if arg.node_type == 'category' and arg.value in group_fields:            if not (function_name.startswith('group_') or is_in_group_arg):                errors.append(f"Group类型字段 '{arg.value}' 只能用于Group类型函数的参数中")                # 然后验证参数类型是否符合预期        if expected_type == 'expression':            # 表达式可以是任何有效的AST节点            pass        elif expected_type == 'number':            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个数字，但得到 {arg.node_type}")        elif expected_type == 'boolean':            # 布尔值可以是数字（0/1）            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个布尔值（0/1），但得到 {arg.node_type}")        elif expected_type == 'field':            if arg.node_type != 'field' and arg.node_type != 'category':                # 允许field或category作为字段参数                errors.append(f"参数 {arg_index+1} 应该是一个字段，但得到 {arg.node_type}")            elif arg.node_type == 'field' and not self._is_valid_field(arg.value):                errors.append(f"无效的字段名: {arg.value}")        elif expected_type == 'category':            if not function_name.startswith('group_'):                # 非group函数的category参数必须是category类型且在valid_categories中                if arg.node_type != 'category':                    errors.append(f"参数 {arg_index+1} 应该是一个类别，但得到 {arg.node_type}")                elif arg.value not in valid_categories:                    errors.append(f"无效的类别: {arg.value}")            # group函数的category参数可以是任何类型（field、category等），不进行类型校验                return errors        def validate_ast(self, ast: Optional[ASTNode], is_in_group_arg: bool = False) -> List[str]:        """递归验证抽象语法树"""        if not ast:            return ["无法解析表达式"]                errors = []                # 根据节点类型进行验证        if ast.node_type == 'function':            # 检查当前函数是否是group函数            is_group_function = ast.value.startswith('group_')            # 确定当前是否在group函数的参数链中            current_in_group_arg = is_in_group_arg or is_group_function            # 验证函数            function_errors = self.validate_function(ast, current_in_group_arg)            errors.extend(function_errors)                        # 递归验证子节点时使用current_in_group_arg            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], current_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, current_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type in ['unop', 'binop']:            # 对操作符的子节点进行验证            for child in ast.children:                if hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type == 'field':            # 验证字段名            if not self._is_valid_field(ast.value):                errors.append(f"无效的字段名: {ast.value}")        else:            # 递归验证子节点            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], is_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)                return errors        def _process_semicolon_expression(self, expression: str) -> Tuple[bool, str]:        """处理带有分号的表达式，将其转换为不带分号的简化形式                Args:            expression: 要处理的表达式字符串                    Returns:            Tuple[bool, str]: (是否成功, 转换后的表达式或错误信息)        """        # 检查表达式是否以分号结尾        if expression.strip().endswith(';'):            return False, "表达式不能以分号结尾"                # 分割表达式为语句列表        statements = [stmt.strip() for stmt in expression.split(';') if stmt.strip()]        if not statements:            return False, "表达式不能为空"                # 存储变量赋值        variables = {}                # 处理每个赋值语句（除了最后一个）        for i, stmt in enumerate(statements[:-1]):            # 检查是否包含赋值符号            if '=' not in stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 检查是否是比较操作符（==, !=, <=, >=）            if any(op in stmt for op in ['==', '!=', '<=', '>=']):                # 如果包含比较操作符，需要确认是否有赋值符号                # 使用临时替换法：将比较操作符替换为临时标记，再检查是否还有=                temp_stmt = stmt                for op in ['==', '!=', '<=', '>=']:                    temp_stmt = temp_stmt.replace(op, '---')                                if '=' not in temp_stmt:                    return False, f"第{i+1}个语句必须是赋值语句，不能只是比较表达式"                        # 找到第一个=符号（不是比较操作符的一部分）            # 先将比较操作符替换为临时标记，再找=            temp_stmt = stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' not in temp_stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 找到实际的=位置            equals_pos = temp_stmt.index('=')                        # 在原始语句中找到对应位置            real_equals_pos = 0            temp_count = 0            for char in stmt:                if temp_count == equals_pos:                    break                if char in '!<>':                    # 检查是否是比较操作符的一部分                    if real_equals_pos + 1 < len(stmt) and stmt[real_equals_pos + 1] == '=':                        # 是比较操作符，跳过两个字符                        real_equals_pos += 2                        temp_count += 3  # 因为替换成了三个字符的---                    else:                        real_equals_pos += 1                        temp_count += 1                else:                    real_equals_pos += 1                    temp_count += 1                        # 分割变量名和值            var_name = stmt[:real_equals_pos].strip()            var_value = stmt[real_equals_pos + 1:].strip()                        # 检查变量名是否有效            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var_name):                return False, f"第{i+1}个语句的变量名'{var_name}'无效，只能包含字母、数字和下划线，且不能以数字开头"                        var_name_lower = var_name.lower()  # 变量名不区分大小写                        # 检查变量名是否在后续表达式中使用            # 这里不需要，因为后面的表达式会检查                        # 检查变量值中使用的变量是否已经定义            # 简单检查：提取所有可能的变量名            used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', var_value)            for used_var in used_vars:                used_var_lower = used_var.lower()                if used_var_lower not in variables:                    # 检查是否是函数名                    if used_var not in supported_functions:                        # 对于单个字母或简单单词，不自动视为字段名，要求先定义                        if len(used_var) <= 2:                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 对于较长的字段名，仍然允许作为字段名                        elif not self._is_valid_field(used_var):                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 将之前定义的变量替换到当前值中            for existing_var, existing_val in variables.items():                # 使用单词边界匹配，避免替换到其他单词的一部分                var_value = re.sub(rf'\b{existing_var}\b', existing_val, var_value)                        # 存储变量            variables[var_name_lower] = var_value                # 处理最后一个语句（实际的表达式）        final_stmt = statements[-1]                # 检查最后一个语句是否是赋值语句        if '=' in final_stmt:            # 替换比较操作符为临时标记，然后检查是否还有单独的=            temp_stmt = final_stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' in temp_stmt:                return False, "最后一个语句不能是赋值语句"                # 检查最后一个语句中使用的变量是否已经定义        used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', final_stmt)        for used_var in used_vars:            used_var_lower = used_var.lower()            if used_var_lower not in variables:                # 检查是否是函数名                if used_var not in supported_functions:                    # 在分号表达式中，所有非函数名的标识符都必须是变量，必须在之前定义                    return False, f"最后一个语句中使用的变量'{used_var}'未在之前定义"                # 将变量替换到最后一个表达式中        final_expr = final_stmt        for var_name, var_value in variables.items():            final_expr = re.sub(rf'\b{var_name}\b', var_value, final_expr)                return True, final_expr        def check_expression(self, expression: str) -> Dict[str, Any]:        """        检查表达式格式是否正确                Args:            expression: 要验证的表达式字符串                    Returns:            包含验证结果的字典        """        # 重置错误列表        self.errors = []                try:            expression = expression.strip()            if not expression:                return {                    'valid': False,                    'errors': ['表达式不能为空'],                    'tokens': [],                    'ast': None                }                        # 处理带有分号的表达式            if ';' in expression:                success, result = self._process_semicolon_expression(expression)                if not success:                    return {                        'valid': False,                        'errors': [result],                        'tokens': [],                        'ast': None                    }                expression = result                        # 重置词法分析器的行号            self.lexer.lineno = 1                        # 词法分析（用于调试）            self.lexer.input(expression)            tokens = []            # 调试：打印识别的标记            print(f"\n调试 - 表达式: {expression}")            print("识别的标记:")            for token in self.lexer:                print(f"  - 类型: {token.type}, 值: '{token.value}', 位置: {token.lexpos}")                tokens.append(token)                        # 重新设置词法分析器的输入，以便语法分析器使用            self.lexer.input(expression)            self.lexer.lineno = 1                        # 语法分析            ast = self.parser.parse(expression, lexer=self.lexer)                        # 验证AST            validation_errors = self.validate_ast(ast)                        # 合并所有错误            all_errors = self.errors + validation_errors                        # 检查括号是否匹配            bracket_count = 0            for char in expression:                if char == '(':                    bracket_count += 1                elif char == ')':                    bracket_count -= 1                if bracket_count < 0:                    all_errors.append("括号不匹配: 右括号过多")                    break            if bracket_count > 0:                all_errors.append("括号不匹配: 左括号过多")                        return {                'valid': len(all_errors) == 0,                'errors': all_errors,                'tokens': tokens,                'ast': ast            }        except Exception as e:            return {                'valid': False,                'errors': [f"解析错误: {str(e)}"],                'tokens': [],                'ast': None            }def main():    """主函数 - 用于验证表达式并输出结果到JSON文件"""    validator = ExpressionValidator()        # 获取用户输入的JSON文件路径，默认路径为当前路径下的Tranformer/output/Alpha_generated_expressions.json    default_path = os.path.join("Tranformer", "output", "Alpha_generated_expressions.json")    input_path = input(f"请输入要校验的表达式JSON文件路径（默认：{default_path}）: ").strip()        if not input_path:        input_path = default_path        # 检查文件是否存在    if not os.path.exists(input_path):        print(f"错误: 文件 {input_path} 不存在")        return        # 读取JSON文件    try:        with open(input_path, 'r', encoding='utf-8') as f:            expressions_data = json.load(f)    except json.JSONDecodeError as e:        print(f"错误: JSON文件解析失败 - {e}")        return        # 提取表达式列表    # 假设JSON文件结构为 {"expressions": ["expr1", "expr2", ...]} 或直接是 ["expr1", "expr2", ...]    if isinstance(expressions_data, dict) and "expressions" in expressions_data:        expressions = expressions_data["expressions"]    elif isinstance(expressions_data, list):        expressions = expressions_data    else:        print("错误: JSON文件格式不正确，需要包含表达式列表")        return        # 验证表达式    valid_expressions = []    invalid_expressions = []        print(f"开始验证 {len(expressions)} 个表达式...")    for i, expr in enumerate(expressions, 1):        if i % 10 == 0:            print(f"已验证 {i}/{len(expressions)} 个表达式")                    result = validator.check_expression(expr)        if result["valid"]:            valid_expressions.append(expr)        else:            invalid_expressions.append({"expression": expr, "errors": result["errors"]})        # 生成输出文件路径    base_name = os.path.basename(input_path)    name, ext = os.path.splitext(base_name)    output_dir = os.path.dirname(input_path)        valid_output_path = os.path.join(output_dir, f"{name}_success{ext}")    invalid_output_path = os.path.join(output_dir, f"{name}_error{ext}")        # 保存结果到JSON文件    print(f"\n验证完成！")    print(f"有效表达式: {len(valid_expressions)}")    print(f"无效表达式: {len(invalid_expressions)}")        # 保存有效表达式    try:        with open(valid_output_path, 'w', encoding='utf-8') as f:            json.dump(valid_expressions, f, ensure_ascii=False, indent=2)        print(f"有效表达式已保存到: {valid_output_path}")    except Exception as e:        print(f"错误: 保存有效表达式失败 - {e}")        # 保存无效表达式    try:        with open(invalid_output_path, 'w', encoding='utf-8') as f:            json.dump(invalid_expressions, f, ensure_ascii=False, indent=2)        print(f"无效表达式已保存到: {invalid_output_path}")    except Exception as e:        print(f"错误: 保存无效表达式失败 - {e}")if __name__ == "__main__":    main()
```

---

### 帖子 #26: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template_37117908343831.md
- **讨论数**: 26

最近大趋势下，想必大家都在使用 72变之类的功能，而72变中，作者提供了一套模板，出货率还不错，不过在此基础上，我通过论坛，让大模型又总结了一份Alpha模板，如标题所言，这份模板均来自社区，所以是来自社区的馈赠

我自己用下来，出货率还不错，和内置模板相当，甚至还能更好一点，不过大家还是要自行评估一下，部分来自社区的论坛也存在过拟合的风险，如有帮助，欢迎点赞，如有错漏，请帮忙指出

```
    ## 模板格式说明

    每个模板使用以下占位符格式：
    - `<ts_op/>` - 时间序列操作符，如 `ts_rank`, `ts_mean`, `ts_delta`, `ts_ir`, `ts_stddev`, `ts_zscore`
    - `<group_op/>` - 分组操作符，如 `group_rank`, `group_neutralize`, `group_zscore`
    - `<vec_op/>` - 向量操作符，如 `vec_avg`, `vec_sum`, `vec_max`, `vec_min`, `vec_stddev`
    - `<field/>` - 数据字段占位符
    - `<d/>` - 时间窗口参数，常用值: `{5, 22, 66, 126, 252, 504}`
    - `<group/>` - 分组字段，如 `industry`, `sector`, `subindustry`, `market`

---

### 帖子 #27: 【Community Leader -因子筛选与组合⭐】2025 AIAC冠军比赛心得以及当前使用iflow cli的心得（附提示词）经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】2025 AIAC冠军比赛心得以及当前使用iflow cli的心得附提示词经验分享_37014730112023.md
- **讨论数**: 61

参加2025 AIAC，有幸获得第一，在此文，我将分享使用AI的因子构造和比赛心得，希望能为大家提供一些有价值的参考。

首先要感谢weijie老师，kunqi老师的培训和帮助，还有论坛以及群内热心consoltent的分享。

我是1月注册，4月有条件顾问，7月正式顾问。

期间参加了IQC（260名），GAC（33名），MAPC（8名），AIAC（1名）。

### 一、比赛总结

现在来看看我比赛的提交情况：


> [!NOTE] [图片 OCR 识别内容]
> 各区域阿尔法数量分布对比
> 200
> 阿尔法总数
> super alpha 数虽
> 175
> ppa alpha 数量
> 150
> 125
> I00
> GLB
> ASI
> EUR
> USA


比赛大致思路：

因为我原来没有通过LLM方式进行过整体的alpha发掘，所以一开始就没有打算交很多的比赛alpha，所以选择parent 的策略是根据低prodcorr和performances表现，根据规则一个多个super可以对应同一个parent，然后我为每个region选了一个作为parent，然后在不同的数据集用代码跑出child，我认为这样可以既有关联性也有多样性。

比赛的sa思路，是参考了 有一次去年iqc比赛冠军培训的思路，我记得她说用15个alpha组出来的super 后面来看os表现也不错。然后我本身每个reigon的alpha数量不算多，所以按照最大团算法，可以在保证多样性的同时用较少的alpha组出多个super并且通过相关性检查。

下面说说我比赛的AI代码思路：

*1、把parents有关的所有信息都丢给AI，然后让AI出表达式（5～10个）*

*2、检查表达式正确性，进行回测（multi）*

*3、分析回测结果，把fitness最大的做为新一轮的parents，把相关的所有信息丢给AI，并告诉他生成的表达式不要与前面的相同*

*4、循环持续5次（次数可以配置，看情况）或者能够得到都check pass的*

*5、最后输出最佳alpha 和整个过程中AI给出的表达式列表*

### 下面说一下我当前使用AI工具的一些体会

目前在72变，缘分，mcp等多种好用的工具出来后，现在我是总共8个槽，4个槽跑72变的json或者已有的模版观察数据集信号，然后跑出来有信号的，3个给AI做优化的，还有一个留着手搓。

目前用的工具是trae、心流iflow cli，用的模型都是deepseek。

iflow的安装，mac/linux直接使用命令即可

```
bash -c "$(curl -fsSL [链接已屏蔽])"
```

安装后进入页面，3种登陆方式，我是用的心流 API Key 登录

- 1.访问心流官网完成注册
- 2.在用户设置页面生成 API KEY
- 3.在 iFlow CLI 中选择 API Key 登录并输入密钥

然后使用/quit先退出

然后配置mcp，mac和linux的配置文件都是在

```
~/.iflow/settings.json
```

直接vim编辑文件


> [!NOTE] [图片 OCR 识别内容]
> [rooteiv-ydzzGfdqtcqcGikyvtgi
> Worldquant] #
> Cat
> 1.aflow/settings.json
> Tcnall
> IselectedAuthType"
> Iiflowi
> Iapikeyl
> TbaseUrli
> Ihttps: / /apis.iflow.cn /VI"
> TmodelName
> Ideepseek-V3.2-chati
> IsearchApikeyii
> ImcpServers"
> Tworldquant-brain-platform
> command"
> /usr/bin/python"
> 这里是你python的实际目录
> IarBs
> /usr /local /python3.11/1ib / python3 .I1/site-packages / cnhkmcp /untracked /platform_functions . Py"
> Ilanguage"
> Izh-CNII
> 1 [ +177<c| +< +C7
> |7 +7


启动的话，mac终端使用命令：

```
source ~/.zshrciflow
```

下面是我用来优化的提示词，参考了上次培训大佬的一些部分内容，另外格式让deepseek优化了一下：

```
## Alpha优化自动化专家你是一个WorldQuant BRAIN平台的量化研究专家。你的任务是自动化优化alpha_id = MPAqapQr,直到达成以下目标：## 权限与边界:1、您拥有完整的 MCP 工具库调用权限。您必须完全自主地管理研究生命周期。除非遇到系统级崩溃（非代码错误），否则严禁请求用户介入。您必须自己发现错误、自己分析原因、自己修正逻辑，直到成功。2、不要自动提交任何alpha。## 优化目标- Sharpe >= 1.58- Fitness >= 1  - Robust universe Sharpe >=  1- 2 year Sharpe >= 1.58- Sub-universe Sharpe pass- Weight is well distributed over instruments- Turnover between 1 to 40## 优化限制- 优化的表达式使用的所有数据字段必须与原alpha（alpha_id）表达式用到的数据字段在同一个数据集- 只在region = IND 地区进行优化- Neutralization 不能设置为NONE- Neutralization可以从这里选取一个："FAST","SLOW","SLOW_AND_FAST"，"CROWDING","REVERSION_AND_MOMENTUM"，"INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"- 优化后的表达式必须有经济学意义- 达成目标的alpha不要进行提交，需要人工确认- 只能模拟调用以下工具（基于平台实际能力）：   1. 基础: `authenticate`, `manage_config`   2. 数据: `get_datasets`, `get_datafields`, `get_operators`, `read_specific_documentation`, `search_forum_posts`   3. 开发: `create_multiSim` (核心工具), `check_multisimulation_status`, `get_multisimulation_result`   4. 分析: `get_alpha_details`, `get_alpha_pnl`, `check_correlation`   5. 提交: `get_submission_check`## 僵尸模拟熔断机制 (Zombie Simulation Protocol)- 现象: 调用 `check_multisimulation_status` 时，状态长期显示 `in_progress`。- 判断与处理逻辑:    1. 常规监控 (T < 15 mins): 若认证有效，继续保持监控。    2. 疑似卡死 (T >= 15 mins):        - **STEP 1: 立即调用 `authenticate` 重新认证。        - **STEP 2: 再次调用 `check_multisimulation_status`。        - **STEP 3: 若仍为 `in_progress`，判定为僵尸任务。        - **STEP 4: **立刻停止**监控该 ID，重新调用 `create_multiSim` (生成新 ID) 重启流程。## 自动化工作流你需要循环执行以下7个步骤，直到成功或达到最大尝试次数(100次)：### 步骤1: 认证登陆使用authenticate工具，从配置文件读取凭据：- 文件：user_config.json认证后，可以保持登陆状态6小时，超时需要重新认证### 步骤2: 获取源alpha信息使用get_alpha_details工具，参数：alpha_id提取关键信息：- 源表达式- 当前性能指标(Sharpe/Fitness/Margin)- 当前settings(特别是instrumentType)### 步骤3: 获取平台资源同时调用三个工具：1. - 读取文件获取所有可用操作符：operators.md 2. get_datasets - 参数：region=IND, universe=TOP500, delay=13. get_datafields - 参数：region=IND, universe=TOP500, delay=1重要规则：- 表达式必须严格按照operators返回的格式填写- 如果数据是vector类型，必须先使用vec_开头的operator- 表达式只能使用1-2个不同的数据字段- 同一字段可以多次使用- 使用多字段时尽量选择同数据集的字段### 步骤4: 生成优化表达式基于以下原则生成新表达式：1. 必须有经济学意义2. 对比源表达式，尝试改进3. 可以从以下数据类型中选择：   - 动量策略：使用价格、成交量变化   - 均值回归：使用价格偏离均值的程度   - 质量因子：使用财务指标   - 技术指标组合4. 论坛寻找相关信息5. 尝试更多的操作符6. 尝试更多的数据字段生成思路示例：- 如果源表达式是单字段，尝试增加第二个相关字段- 如果源表达式复杂，尝试简化- 添加合理的数学变换（rank, ts_mean, ts_delta等）每次生成5到8个表达式### 步骤5: 创建回测单个表达式的回测使用create_simulation.同时测试2个以上数量的表达式，使用create_multiSim.回测时的参数设置：- 保持：instrumentType, region, universe, delay等不变- 可以调整：decay, neutralization（尝试不同值）### 步骤6: 检查回测状态回测成功后，会返回链接或alpha_id，使用：- get_submission_check检查状态和初步结果- 如果需要，使用get_SimError_detail检查错误### 步骤7: 分析结果同时调用：1. get_alpha_details - 获取详细性能2. get_alpha_pnl - 获取PnL数据  3. get_alpha_yearly_stats - 获取年度统计## 循环逻辑每次循环后评估：1. 如果达到所有目标 → 停止循环，输出成功报告,alpha id2. 如果未达到 → 分析失败原因，调整策略，继续下一轮3. 记录每次尝试的表达式和结果用于学习## 失败分析策略- 如果Sharpe低 → 尝试不同数据字段组合- 如果Margin低 → 调整neutralization或添加平滑操作- 如果相关性失败 → 减少与现有alpha的相似度- 如果表达式错误 → 检查操作符用法和数据字段类型## 经验教训- 解决“Robust universe Sharpe”较低问题的建议：   - 使用以下运算符中的一两个：      - group_backfill      - group_zscore      - winsorize      - group_neutralize      - group_rank      - ts_scale      - signed_power   - 调整运算符中的时间参数以改善表现。   - 修改Decay参数和时间窗口参数时使用有经济含义的：1，5，21，63，252，504   - 修改Truncation和Neutralization参数。- 解决“2 year Sharpe of 1.XX is below cutoff of 1.58”：   - ts_delta(xx,days) 操作符有奇效   - 采用分域方法增强信号，如乘以sigmoid函数调整信号强度## 知识库- 目录Resources里面按照region_decay_universe_dataset的文件名，每个文件包含对应数据集的介绍，和Research Paper。## 开始执行现在开始第一轮优化。请按步骤执行，保持思考和解释。
```

下面是我的执行指令，其中我把上面的提示词保存成了alpha_better.md 文件，operators.md内容是我用ai爬取了官网页面上的operators页面内容

```
@alpha_better.md 严格按照文档流程执行，operators使用方法参见@operators.md ,自动执行，不要咨询我，除非达成了目标。
```

iflow执行过程：


> [!NOTE] [图片 OCR 识别内容]
> plan 更新待办事项列表 (3个待处理。1个进行中;
> 7个已完成)
> 已更新待办事项列表
> 新的Alpha优 化:  步骤1 -认证登陆
> (alpha_id
> OmVLW7dII
> 步骤2:  获取源alpha信息
> alpha_id
> OIVLW7dI
> 步骤3:  获取平台资源
> IND地区数据字段和操作符
> 步骤4:  生成优化表达式 -基于源alpha的经济学意义改进
> 步骤5:  创建回测测试新表达式
> 步骤6:  检查回测状态
> 步骤7:  分析结果井评估
> 第二轮优化:  步骤4 -生成新表达式 (针对Robust universe Sharpe)
> 口第二轮优化:  步骤5
> 创建回测测试新表达式
> 口第二轮优化:  步骤6
> 检查回测状态
> 第二轮优化:  步骤7 -分析结果井评估
> exprI (按esc取消 ,
> IBm 255)
> 加载:
> MCP
> 服务
> (ctrltt 查看)
> 思考:开启
> (tab切]换) YOLO模式
> (shift
> tab
> alt
> 切换
> 输入消息或@文件路径


通过上面的过程可以看到，还是能完整按照md文件里预设的流程步骤进行的。

ps：要他自动运行，要记得开启“思考+yolo”模式。

下面是优化成功的一个alpha和iflow的报告。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Thame: IND Region Theme
> Data Sat Alpha
> ReBUIT
> Jpha
> Irmlo thEme: INDIDTIFUNDAWENTAL *1
> SimIlatimn
> Settings
> IIIUIBNLT
> Rl
> Umivel
> LIOUAa
> Uetg
> Oelg
> TNCUI
> Nuralzlol
> Cayleuilr
> NaN Hnuliny
> UI HUIII
> MHT
> ABBregate Data
> Sharr
> HetUTT
> Lru 
> Larpr
> 3.47
> 17.519
> 3.40
> 16.78%
> 6.629
> 19.169o0@
> CUUIC
> TURSDJ
> Fusl CuIessIuI
> R
> WerIl
> UU
> N
> STTC
> T
> Lole COUH
> CCI
> 2013
> 1GOJm
> LeD
> LS2
> 909
> Clone Alpha 
> Z0IA
> 1545m
> 3e.57u
> 115
> 419
> 1955q
> 71749
> g
> 777
> 19719
> 19,-1a
> 7 |G
> 20.47
> N Chart
> Pnl
> 17.454
> 150
> 1RS
> 1591
> 1SIm
> 14.57u
> 1.744
> 15.51
> 2019
> 171
> T
> 1
> !
> 1552m
> 20.39兑
> 1.30
> 35.23
> 1L
> 
> 3T9C
> 111
> 2022
> 16.979
> 11
> 392
> 132
> 17T5
> SU7n
> TJ
> 977
> OOoK
> Investability constrained
> ABBreBate Data
> Uratl?
> 2015
> 2016
> 201
> 2016
> 2020
> 2021
> 23
> 2.48
> 8.02%
> 2.47
> 12.41%
> 5.25%
> 30.9520@
> Correlation
> SelfCOTTelatION
> VurImJT
> MinImUT
> LJst Hun; 1131
> 12115/2025,2:09ul
> OS Testing Status
> RerIOO
> 0.3009
> -0.0185
> Prod Correlatlon
> VurImJT
> JIMUM
> LJst Hun; 1131
> 12115/2025,2:09u
> 11PENDING
> 0.5756
> -0.2236
> 1诱求临嚣
> BOLUOTIUOUBIUAIIC0I
> 雁开
> 灞空
> SngI
> Sale
> Marn



> [!NOTE] [图片 OCR 识别内容]
> Alpha优化总结
> 指标对比
> 指标
> 初始 (NA0ZJ3a)
> (MOZdEw)
> 娈化
> Sharpe
> 2.25
> 3.47
> +548
> Fitness
> 1.90
> 3.40
> +79*
> 换手宰
> 0.2046
> 0.1751
> 148
> 2年 Sharpe
> 1.12 (^)
> 1.88
> 582
> Robust universe
> 1.00
> 1.07
> +79
> Pnl
> 031
> 17 .371
> +152
> Returns
> 14 .528
> 16 .78%
> +163
> Drawdown
> 792
> 6.62%
> +148
> 优化信息
> 日期:  2025-12-14
> 耗时:  466分钟
> (7时46分钟 )
> 轮次:  13轮循环
> 优化手段
> 字段替换:
> risk_sCore
> aVerage
> SCOre
> 分组优化: industry
> sector
> (+37] Robust Sharpe)
> 参数调优:  5048囱0
> std=4控制分布
> 结构固定
> Broup_backfill嵌套 Broup_Vector_neut
> 批量测试: create_multisim高效迭代
> 验证通过
> 权重分布:  均匀
> 相关性:  自相关0.3009
> 生产相关0.5756 (均<0.7)
> 激励乘数:  2.5x (IN0主题
> 金字塔 )
> 最终状态
> 所有目标达成
> 性能全面提升
> 聂终


Iflow使用下来跟上次培训的大佬比还是有差距，出货差不多也就能做到一天一个。

期间遇到的问题：

1、有的时候也不能一直持续运行，会让你确认，这个没有好的办法，我一般都是运行半小时看一下，但是大多数时候都是可以持续执行；

2、有时候会连不上worldquant（此时需要/quit再启动）

3、优化轮次很多的时候，会自动创建文件，不过多是文件名包含alphaid的，优化后清理就行。

最后说一下是用过的cli对比：

Cli模式的国内还有qwen的cli，不过也是阿里系的，跟iflow差不多，感觉没有iflow方便。

字节的有个ve cli，不过每天只有500w的token，我用了一天最后扣了2块。。。

我用心流主要是他可以在“思考+yolo模式”可以一直持续优化不用人工介入而且免费～

另外，不同的cli应该是可以同时使用的，我同时在一个linux服务器上使用过iflow和ve cli。

最后的最后，如果大家觉得本文对你有帮助的话，点个赞再走吧～

---

### 帖子 #28: Alpha Turnover降低工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP Workflow】turnover优化论坛精华版经验分享_34949059814679.md
- **讨论数**: 11

自从开始使用MCP工具，整体效率提升了很多，但是之前的MCP成功率一般，比如前面分享的 [自动化找alpha的workflow]([L2] 【MCP Workflow】一个自动化找alpha的工作流分享_34670122621207.md) ，整体成功率大约40%，但其对token的消耗是很大的，由于我的AI用的是包月套餐，整体感受没那么厉害，但是如果是按量计费的话，极端情况下，base甚至覆盖不到token的消耗。

基于上次双周会IQC中国区冠军分享的coze工作流，我发现其实我可以把目光放在更细分的领域，让AI完成一个特定的任务，而非从0开始去找alpha，让其作为一个辅助工具，可能成功率会显著提升，经过我的测试也的确如此，现在将其中一个工作流，Alpha Turnover降低工作流分享给大家，供大家参考，如果大家感兴趣，我也可以持续分享一些自己在用的，效果较好的其他专题工作流。

首先，该工作流主要是对以下文章内容的提炼，让AI跟随这些经验，去做提升工作，感谢这些作者，文章列表如下：

1. **[如何拯救高turnover因子？一文助你理解并降低因子turnover]([L2] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md)**  - 109票权威指南
2. **[浅谈用hump操作符解决Sub-universe Sharpe](../顾问 LZ63377 (Rank 33)/[Commented] 浅谈用hump操作符解决Sub-universe Sharpe_31365517513495.md)**  - hump操作符专题
3. **[VF 0.9+顾问分享：新人常见误区之Under Fitting]([L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md)**  - 顾问级经验
4. **[Alpha 模版：ts_delta_limit应用举例](/hc/zh-cn/community/posts/34588105621783)**  - 高级控制技巧

```
# Alpha Turnover降低工作流

## 🎯 概述
基于BRAIN论坛经验总结，return = turnover × margin，高换手率降低margin，影响fitness score和被PM采纳的概率。本工作流通过ts_decay_linear等论坛验证的操作符，系统化降低alpha的turnover，实战中可实现**30-50%的turnover降幅**。

## 📊 论坛实证依据

### 核心理论基础
- **[如何拯救高turnover因子？一文助你理解并降低因子turnover]([L2] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md)** (109票, 12评论)
- **[浅谈用hump操作符解决Sub-universe Sharpe](../顾问 LZ63377 (Rank 33)/[Commented] 浅谈用hump操作符解决Sub-universe Sharpe_31365517513495.md)** (18票, 9评论)
- **[VF 0.9+顾问分享：新人常见误区之Under Fitting]([L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md)** (25票, 11评论)

### 关键洞察
1. **基本关系**: `return = turnover × margin`
2. **核心操作符**: `ts_decay_linear`, `hump`, `ts_target_tvr_delta_limit`
3. **平台建议**: 含TVR关键词的operator优先

## 🔍 第一步：MCP工具诊断当前状态

### 使用MCP工具获取基线数据
使用 `mcp__worldquant_brain_platform__get_alpha_details()` 获取当前alpha的基线指标

### 关键指标分析
1. **当前turnover水平** (目标: 0.1~0.3)
2. **Sharpe vs Turnover权衡点**
3. **时间序列稳定性分析**

## 🔧 第二步：基于论坛实证的降turnover策略

### 策略A: ts_decay_linear平滑（论坛首推）

**理论依据**: 平台官方建议的信号平稳性优化方法

**MCP工具实施**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `ts_decay_linear(原表达式, 5)` - 1个交易周
- `ts_decay_linear(原表达式, 22)` - 1个交易月  
- `ts_decay_linear(原表达式, 44)` - 2个交易月
- `ts_decay_linear(原表达式, 63)` - 1个季度

**预期效果**: Turnover降低30-50%，Sharpe轻微下降可接受

**经济学原理**: 
- **5天** = 1个标准交易周，适合短期信号平滑
- **22天** = 1个交易月，适合月度趋势捕捉  
- **44天** = 2个交易月，适合中期信号稳定
- **63天** = 1个季度，与财报周期同步，适合基本面信号

### 策略B: hump操作符优化（Sub-universe专用）

**理论依据**: 论坛实证表明hump在控制波动性、降低换手率方面表现出色

**适用场景**: Sub-universe Sharpe表现不佳时优先考虑

**MCP工具实施**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `hump(原表达式, hump=0.1)` - 轻度截断
- `hump(原表达式, hump=0.2)` - 中度截断
- `hump(原表达式, hump=0.3)` - 较强截断
- `hump(ts_decay_linear(原表达式, 5), hump=0.2)` - 周衰减+截断组合

### 策略C: 新一代TVR控制操作符

**理论依据**: 顾问分享提到平台最新推出的含TVR关键词操作符

**MCP工具实施**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `ts_target_tvr_delta_limit(原表达式, volume, target_tvr=0.1)` - 目标10%换手率
- `ts_target_tvr_delta_limit(原表达式, volume, target_tvr=0.15)` - 目标15%换手率  
- `ts_target_tvr_delta_limit(原表达式, volume, target_tvr=0.2)` - 目标20%换手率

### 策略D: 组合平滑技术

**基于论坛实践的组合方法**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `ts_decay_linear(ts_mean(原表达式, 5), 22)` - 周均值+月度衰减
- `hump(ts_decay_linear(原表达式, 5), hump=0.2)` - 周衰减+截断
- `rank(ts_decay_linear(原表达式, 22))` - 月衰减+排名

## 📈 第三步：MCP工具验证与选择

### 综合评估流程
使用以下MCP工具评估所有候选方案：
1. `mcp__worldquant_brain_platform__get_alpha_details()` - 获取详细指标
2. 对比原始alpha的turnover、sharpe、fitness指标

### 选择标准（基于论坛经验）
1. **优先级**: Turnover降低 > 30%
2. **可接受**: Sharpe损失 < 15%
3. **理想状态**: Fitness score提升

## 🏆 第四步：最终优化与提交准备

### 最终候选确认
使用以下MCP工具对最优候选进行最终检查：
1. `mcp__worldquant_brain_platform__get_submission_check()` - 提交检查
2. `mcp__worldquant_brain_platform__check_correlation()` - 相关性检查
3. `mcp__worldquant_brain_platform__set_alpha_properties()` - 设置属性标记

## ✅ 成功标准（基于论坛经验）
- **Turnover < 0.3** (理想 < 0.2)
- **Sharpe损失 < 15%** (可接受范围)
- **Fitness score提升** (margin改善)
- **相关性保持 < 0.7**

## 🚨 常见陷阱（论坛经验总结）

### 陷阱1: 盲目提高decay参数
**论坛洞察**: "低decay是为了刨除那些为了过相关性测试盲目提高decay的劣质因子"
**解决方案**: 优先使用操作符层面的平滑，而非decay参数

### 陷阱2: 过度优化导致信号失真
**解决方案**: 保持原始信号的经济逻辑，渐进式优化

### 陷阱3: 忽视Sub-universe表现
**解决方案**: hump操作符在Sub-universe Sharpe优化方面更直接有效

## 📚 论坛文章参考

### 必读文章
1. **[如何拯救高turnover因子？一文助你理解并降低因子turnover]([L2] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md)** - 109票权威指南
2. **[浅谈用hump操作符解决Sub-universe Sharpe](../顾问 LZ63377 (Rank 33)/[Commented] 浅谈用hump操作符解决Sub-universe Sharpe_31365517513495.md)** - hump操作符专题
3. **[VF 0.9+顾问分享：新人常见误区之Under Fitting]([L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md)** - 顾问级经验
4. **[Alpha 模版：ts_delta_limit应用举例]([链接已屏蔽])** - 高级控制技巧

### 核心操作符文档
- `ts_decay_linear(x, d)` - 平台官方推荐
- `hump(x, hump=)` - Sub-universe优化专用  
- `ts_target_tvr_delta_limit` - 新一代TVR控制

## 🛠️ MCP工具使用总结

核心MCP工具：
1. `mcp__worldquant_brain_platform__get_alpha_details()` - 获取基线指标
2. `mcp__worldquant_brain_platform__create_multiSim()` - 批量测试优化方案  
3. `mcp__worldquant_brain_platform__get_submission_check()` - 提交前检查
4. `mcp__worldquant_brain_platform__check_correlation()` - 相关性验证
5. `mcp__worldquant_brain_platform__set_alpha_properties()` - 设置属性标记

### 与手动调试对比
✅ **MCP批量测试**: 一次性测试多个ts_decay_linear参数组合
✅ **自动化评估**: 自动获取所有候选的turnover、sharpe、fitness指标
✅ **系统性对比**: 快速识别最优参数，避免网页端逐个手动测试
✅ **完整验证链**: 自动完成submission和correlation检查流程

## 🎯 实战效果展示

### Alpha 9nz6GQq 优化案例
**原始指标**:
- Turnover: 0.5083 (过高)
- Sharpe: 1.86
- Fitness: < 1.0

**使用ts_decay_linear(d=5)优化后**:
- Turnover: 0.2693 (**降低47%** ✅)
- Sharpe: 1.71 (轻微下降9% ✅)
- Fitness: 显著提升

**验证结果**: 
- ✅ Turnover成功降至目标范围内
- ✅ Sharpe损失在可接受范围内  
- ✅ 整体fitness得到改善
- ✅ 证明工作流高度有效

## 📄 第五步：生成优化报告

### 创建完整的优化记录
使用 `mcp__worldquant_brain_platform__set_alpha_properties()` 为优化后的alpha设置：
- **Name**: `TurnoverOpt_[原始AlphaID]`
- **Tags**: `["turnover_optimized", "ts_decay_linear", "forum_validated"]`
- **Description**: 记录优化前后的具体指标变化和使用的参数

### 优化报告模板
```
Alpha Turnover优化报告
=====================
原始Alpha: [AlphaID]
优化方法: ts_decay_linear(d=[参数])
优化结果:
- Turnover: [原值] → [新值] (改善[百分比])
- Sharpe: [原值] → [新值] (变化[百分比])  
- Fitness: [原值] → [新值]
- 经济学意义: [时间参数的经济学解释]
```

通过MCP工具，实现论坛验证的turnover优化策略，确保结果的可靠性和一致性。
```

同时由于大家操作符权限不同，且AI可能理解错误operator的参数，可以让AI下载一下操作符文件，保存下来，再同时作为语料提供给AI，从而减少AI出错的概率，也可参考我之前分享的关于operator的文章。

[来自MCP的operator指北，终于看懂了大多数的平台operator](../顾问 YH25030 (Rank 31)/[L2] 来自MCP的operator指北终于看懂了大多数的平台operator_34208186164631.md)

也可参考之前分享的工作流

[【MCP Workflow】一个自动化找alpha的工作流分享]([L2] 【MCP Workflow】一个自动化找alpha的工作流分享_34670122621207.md)

如大家感兴趣，多多点赞评论，后续更新更多关于MCP的探索工作流，下次再见

---

### 帖子 #29: 中文版：Alpha 解析工作流程
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP WorkFlow】一个使用MCP来给Alpha写描述并获取更多启发的工作流_34213553037335.md
- **讨论数**: 26

我们都知道，要发挥MCP的功能，就需要把它当作我们的秘书。以下是一个参考工作流，你可以让它照着做，并把Alpha表达式和Region给它，就能给你Alpha进行解释，并给你进一步点塔的启发，和撰写description的台词。

# Alpha Explanation Workflow

This manual provides a step-by-step workflow for analyzing and explaining a WorldQuant BRAIN alpha expression. By following this guide, you can efficiently gather the necessary information to understand the logic and potential strategy behind any alpha.

## Step 1: Deconstruct the Alpha Expression

The first step is to break down the alpha expression into its fundamental components:  **data fields**  and  **operators** .

For example, given the expression  `quantile(ts_regression(oth423_find,group_mean(oth423_find,vec_max(shrt3_bar),country),90))` :

- **Data Fields:**   `oth423_find` ,  `shrt3_bar`
- **Operators:**   `quantile` ,  `ts_regression` ,  `group_mean` ,  `vec_max`

## Step 2: Analyze Data Fields

Use the  `brain-platform-mcp`  tool  `get_datafields`  to get detailed information about each data field.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_datafields</tool_name> <arguments> { "instrument_type": "EQUITY", "region": "ASI", "delay": 1, "universe": "MINVOL1M", "data_type": "VECTOR", "search": "shrt3_bar" } </arguments> </use_mcp_tool>`

**Tips for effective searching:**

- **Specify Parameters:**  Always provide as much information as you know, including  `instrument_type` ,  `region` ,  `delay` ,  `universe` , and  `data_type`  ( `MATRIX`  or  `VECTOR` ).
- **Iterate:**  If you don't find the data field on your first try, try different combinations of parameters. The  `ASI`  region, for example, has two universes:  `MINVOL1M`  and  `ILLIQUID_MINVOL1M` .
- **Check Data Type:**  Be sure to check if the data is a  `MATRIX`  (one value per stock per day) or a  `VECTOR`  (multiple values per stock per day). This is crucial for understanding how the data is used.

**Example Data Field Information:**

- **`oth423_find`** : A  **matrix**  data field from the "Fundamental Income and Dividend Model" dataset in the ASI region. It represents a "Find score," likely indicating fundamental attractiveness.
- **`shrt3_bar`** : A  **vector**  data field from the "Securities Lending Files Data" dataset in the ASI region. It provides a vector of ratings (1-10) indicating the demand to borrow a stock, which is a proxy for short-selling interest.

## Step 3: Understand the Operators

Use the  `brain-platform-mcp`  tool  `get_operators`  to get a list of all available operators and their descriptions.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_operators</tool_name> <arguments> {} </arguments> </use_mcp_tool>`  The output of this command contains a wealth of information. For your convenience, a table of the most common operators is included in the Appendix of this manual.

## Step 4: Consult Official Documentation

For more complex topics, the official BRAIN documentation is an invaluable resource. Use the  `get_documentations`  tool to see a list of available documents, and  `get_documentation_page`  to read a specific page.

**Example:**  To understand vector data fields better, I consulted the "Vector Data Fields ðŸ¥‰" document ( `vector-datafields` ). This revealed that vector data contains multiple values per instrument per day and must be aggregated by a vector operator before being used with other operators.

## Step 5: Broaden Understanding with External Research (Optional)

For cutting-edge ideas and inspiration, you can search for academic papers on arXiv using the provided  `arxiv_api.py`  script.

**Workflow:**

1. **Identify Keywords:**  Based on your analysis of the alpha, identify relevant keywords. For our example, these were:  `"short interest"` ,  `"fundamental analysis"` ,  `"relative value"` , and  `"news sentiment"` .
2. **Run the Script:**  Use the  `with-wrappers`  script to avoid SSL errors.
   ```
   python arxiv_api.py "your keywords here" -n 10
   ```

## Step 6: Synthesize and Explain

Once you have gathered all the necessary information, structure your explanation in a clear and concise format. The following template is recommended:

- **Idea:**  A high-level summary of the alpha's strategy.
- **Rationale for data used:**  An explanation of why each data field was chosen and what it represents.
- **Rationale for operators used:**  A step-by-step explanation of how the operators transform the data to generate the final signal.
- **Further Inspiration:**  Ideas for new alphas based on your research.

## Troubleshooting

- **SSL Errors:**  If you encounter a  `CERTIFICATE_VERIFY_FAILED`  error when running python scripts that access the internet, use the  `AI to help you change or make`  script to execute your command.

## Appendix A: Understanding Vector Data

Vector Data is a distinct type of data field where the number of events recorded per day, per instrument, can vary. This is in contrast to standard matrix data, which has a single value for each instrument per day.

For example, news sentiment data is often a vector because a stock can have multiple news articles on a single day. To use this data in most BRAIN operators, it must first be aggregated into a single value using a  **vector operator** .

---

### 帖子 #30: 【MCP workflow】根据GLB的alpha，自动挖掘其他地区alpha的工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP workflow】根据GLB的alpha自动挖掘其他地区alpha的工作流_35239747718679.md
- **讨论数**: 9

基于weijie老师的分享，我选择了「根据GLB的alpha，来挖掘其他地区的alpha」这个部分的内容，进行了MCP的workflow探索，简单尝试了几个alpha，发现效果还不错，跟大家分享一下工作流，希望有所帮助。

先贴一下效果，我选取的alpha在亚洲表现不错，所以工作流探索了ASI地区


> [!NOTE] [图片 OCR 识别内容]
> 原始
> Alpha 3NV3QKe
> 区域表现:
> GLB_APAC: Sharpe
> 2.37
> 收益率
> 3.40%,
> Pnl
> 3.52M
> 最佳 )
> 
> 
> GLB_EMEA:
> Sharpe 1.16,
> 收益率
> 1.45%
> Pnl
> 1.SOMe
> GLB_AMER:
> Sharpe 0.93,
> 收益率
> 0.62%,
> Pnl
> 0.G4M
> 低 Sharpe 告警
> 
> 
> 
> 
> ASI
> 区域替换字段回测
> (均启用
> max_trade-ON)
> 
> 
> Alpha Zeojbyb: Sharpe
> 1.62,
> 收益率
> 4.43%,
> Pnl
> 4.58M
> 鲁棒指标偏弱 _
> 需强化 )
> 
> 2
> Alpha KWm7dgN: Sharpe 0.87,
> 收益率
> 2.43%,
> Pnl
> 2.52M (信号较弱 )
> 
> 
> 3
> Alpha dNKjVgg: Sharpe 1.46,
> 收益率
> 3.91%,
> Pnl
> 4.Q4M (介于两者之间 )
> 
> 
> 
> 
> 
> 结论要点:
> 
> 
> 亚太季度频率字段继承原信号
> 收益率提升但
> Fitness
> 鲁棒性仍待优化
> 
> 
> 年度 /半年度数据更新慢_
> 信号衰减明显
> 
> 
> 
> 可在既有模板上叠加
> winsorize
> 截断或共享其他盈利字段 ,
> 以提高提交合格率 ,
> 再迂移回
> GLB 做终测


可以看到，在ASI区域，该字段映射效果还不错，但由于max_trade的开启与鲁棒性检测，存在部分不通过的情况，需要进行微调。

工作流内容如下：

> # 跨区域相似因子挖掘工作流
> ## 阶段一：基线诊断
> - 输入 `alpha_id`，调用 `wqb_mcp__get_alpha_details` 获取原因子的区域、参数配置以及各地区表现。
> - 整理 Sharpe、收益率、警报等指标，为后续的区域选择和策略调整提供依据。
> ## 阶段二：信号拆解
> - 解析 Alpha 代码，定位核心数据字段及其操作符结构。
> - 使用 `wqb_mcp__get_datafields`（参数沿用原始区域、universe、delay 等设置）获取field的描述信息，并进行理解。
> ## 阶段三：目标区域映射与字段检索
> - 根据已知区域映射确定迁移区域：`APAC → ASI`、`EMEA → EUR`、`AMER → USA`。
> - 对于每个目标区域，优先使用与原因子相同的 `dataset_id` 调用 `wqb_mcp__get_datafields`；若该数据集在目标区域不可用，则改用相同 `category` 并通过字段关键字搜索。
> - 在确保 `instrument_type`、`delay`、`universe` 等参数匹配的同时，筛选出描述、覆盖率和使用度最接近的字段，建立候选字段池，候选字段池建议为3-8个，一次回测可完成。
> ## 阶段四：候选因子构建
> - 以原公式为模板，将核心字段替换为候选字段，并视需要添加 winsorize、截断、混合周期等调节操作。
> - 保持中性化方式、衰减、延迟等关键参数一致，以保证结果可比性。
> ## 阶段五：批量回测与评估
> - 使用 `wqb_mcp__create_multiSim`（或多次 `wqb_mcp__create_simulation`）在目标区域批量回测候选因子，在 ASI 区域必须开启 `max_trade` 为 `ON`，其他区域使用和选择数据相同的universe即可，其他参数不用调整。
> - 记录 Sharpe、Fitness、鲁棒性检查、风险中性结果等核心指标，并保存 Simulation ID 以便复现与归档。
> ## 阶段六：验证与推广
> - 对表现较好的候选，进行两轮有经济学含义的operator增加和删减，找出表现最好的alpha。
> - 将优胜策略迁移到其他映射区域或回到全域回测，并形成标准化报告，包含字段来源、回测指标及后续优化建议。

大家可以尝试更多的alpha，同时这个策略是从GLB映射到其他地区，其实也可以从其他地区映射到GLB，对工作流进行少量修改即可，如有帮助，请点赞。

更多MCP workflow，可参考我往期帖子，自动挖掘，降turnover，手机使用mcp等

---

### 帖子 #31: 【ValueFactor预测器】滚动3个月SA，掌握你最近3个月提交alpha情况_python版代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 【ValueFactor预测器】滚动3个月SA掌握你最近3个月提交alpha情况_python版代码优化_33715194478615.md
- **讨论数**: 9

首先感谢weijie老师提出的idea:

选择你最近3个月提交的alpha 组SA，根据SA的表现衡量你过去3个月提交的alpha的质量，sa的表现可以视作value factor的预告。之后，你提交的alpah，需要和过去3个月组合的sa的相关性低。

那么如何滚动3个月的alpha组合sa呢？

根据alpha提交的时间，添加年份-月份的tags，然后在组sa的时候，选择tags是指定月份的alpha，进行回测，根据sa的表现，衡量你最近3个月提交的sa质量，代码如下：

```
import jsonimport sysimport timefrom datetime import datetimefrom time import sleepimport requestsfrom requests.adapters import HTTPAdapterfrom requests.packages.urllib3.util.retry import Retrydef load_config(file_path):    """从指定路径f加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user=config["user"]passwd=config["password"]def login():    username = user    password =  passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    max_try = 3    retry=0    while True:        try:            response = s.post('[链接已屏蔽])            if response.status_code  in [200,201]:                print(f"login success")                return s        except Exception as e:            print(f"login err :{e}")            print(f"login failed ,sleep 5 ,try again")            sleep(5)        retry +=1        if retry > max_try:            break    return Nonedef get_submited_alphas_three_month(s,start_date,end_date,region,only_ppa=True):    # only_ppa 设置是否只获取ppa的alpha设置tags，后续组sa时根据tags值的年份月份筛选    print(f"正在获取{start_date}到{end_date}内，{region}地区的ppa alpha")    url=f"[链接已屏蔽]    count=0    print(url)    count=s.get(url).json()['count']    print(count)    alpha_list=[]    for i in range(0,count,100):        url=f"[链接已屏蔽]        response=s.get(url).json()        for alpha in response['results']:            if only_ppa:                flag=0                for item in alpha["classifications"]:                    if item['name']=='Power Pool Alpha':                        flag=1                        break                if flag==1:                    alpha_list.append(alpha)            else:                alpha_list.append(alpha)    print(f"在时间范围{start_date}到{end_date}内，{region}地区，获取了 {len(alpha_list)}个ppa alpha")    return alpha_list# 对所有alpha 在原有tags列表上增加年份+月份的tags，如2025-05def set_alpha_property_list(s,alpha_list):    count = 0    for alpha in alpha_list:        alpha_id=alpha['id']        print(f"正在设置第{count}个alpha 的属性,{alpha_id}; 总alpha数量{len(alpha_list)}")        tags=alpha['tags']        name=alpha['name']        date_created=alpha['dateCreated']        color=alpha['color']        description=alpha['regular']['description']        dt = datetime.fromisoformat(date_created.replace('Z', '+00:00'))        year_month = dt.strftime('%Y-%m')  # "2025-07"        print(year_month)        if year_month in tags:            continue        else:            tags.append(year_month)        category=alpha['category']        if category is None:            category=None        if color is None:            color=None        if name is None:            name=None        print(tags)        params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": description},        "combo": {"description": description},        "selection": {"description": description}}        response = s.patch( "[链接已屏蔽] + alpha_id, json=params)        # print(response.json())        sleep(1)        count+=1    return Truedef make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade):    simulation_data={    "type": "SUPER",    "settings": {        "maxTrade": maxtrade,        "nanHandling": "ON",        "instrumentType": "EQUITY",        "delay": delay,        "universe": universe,        "truncation": 0.08,        "unitHandling": "VERIFY",        "selectionLimit": select_num,        "selectionHandling": select_handle,        "testPeriod": "P0D",        "componentActivation": "IS",        "pasteurization": "ON",        "region": region,        "language": "FASTEXPR",        "decay": decay,        "neutralization": neut_,        "visualization": False    },    "combo": str(combo),    "selection": select}    return simulation_datadef simulate_sa(s,simulation_data):    brain_api_url = '[链接已屏蔽]    try:        simulation_response=s.post(f'{brain_api_url}/simulations',json=simulation_data)        # print(simulation_response.json())    except Exception as e:        print(f"模拟sa失败:{e}")        return None    simulation_progress_url = simulation_response.headers['Location']    print(simulation_progress_url)    while True:        simulation_progress_response=s.get(simulation_progress_url)        retry_after = simulation_progress_response.headers.get("Retry-After", 0)        if str(retry_after) == '0':            status = simulation_progress_response.json().get("status", "not_found")            if status == "COMPLETE":                res_=simulation_progress_response.json()                alpha_id=res_["alpha"]                print(f"最近3个月的ppa组成的sa模拟完成,alpha_id:{alpha_id}")                break        else:            print(f"processing,begin sleep {float(retry_after)}")            time.sleep(float(retry_after))    return alpha_id# 对指定日期范围内的ppa 设置年月标签来确认是否是指定时间范围的ppas = login()#设置你想滚动组合sa的月份start_date='2025-04-01'end_date='2025-06-30'data_range=['2025-04','2025-05','2025-06']# 地区，universeregion='USA'universe='TOP3000'delay=1decay=0select_handle='POSITIVE'select_num=300maxtrade='ON'alpha_list=get_submited_alphas_three_month(s,start_date,end_date,region)print(f"在时间范围{start_date}到{end_date}内，提交了 {len(alpha_list)}个ppa alpha")print(alpha_list[0]['id'],)set_alpha_property_list(s,alpha_list)select=f'(own) && ((in(tags,"{data_range[0]}")) || (in(tags,"{data_range[1]}"))|| (in(tags,"{data_range[2]}")))'print(select)combo=1alpha_ids=[]for decay in  [0]:    ##可根据需要对多种neut回测查看sa表现    for neut_ in  ["CROWDING","REVERSION_AND_MOMENTUM"]:        simulation_data=make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade)        alpha_id=simulate_sa(s,simulation_data)        alpha_ids.append(alpha_id)print(f"完成回测,alpha_id如下")print(alpha_ids)print(f"最近3个月， {region} 提交的ppa 组合的sa表现如下")for alpha_id in alpha_ids:    res=s.get(f"[链接已屏蔽])    res_json=res.json()    sharpe=res_json['is']['sharpe']    fitness=res_json['is']['fitness']    return_=res_json['is']['returns']    drawdown=res_json['is']['drawdown']    margin=res_json['is']['margin']    turnover=res_json['is']['turnover']    neut=res_json['settings']['neutralization']    decay=res_json['settings']['decay']    print(f"{alpha_id}: sharpe: {sharpe}, fitness: {fitness}, return: {return_}, drawdown: {drawdown}, margin: {margin}, turnover: {turnover}, neut: {neut},decay: {decay}")
```

输出结果如下：

```
完成回测,alpha_id如下['12Q7xez', 'E2XGKG0']最近3个月提交的ppa USA 组合的sa表现如下12Q7xez: sharpe: 3.71, fitness: 5.36, return: 0.2609, drawdown: 0.0647, margin: 0.00873, turnover: 0.0598, neut: CROWDING,decay: 0E2XGKG0: sharpe: 4.11, fitness: 5.85, return: 0.2533, drawdown: 0.0429, margin: 0.006105, turnover: 0.083, neut: REVERSION_AND_MOMENTUM,decay: 0
```

---

### 帖子 #32: 【VF 0.9+顾问分享】新人常见误区之Under Fitting （欠拟合）经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md
- **讨论数**: 17

春节期间有些懈怠了，回来收收心继续搬砖，并且给新人分享一些常见容易忽视的地方

一、【Fitting】

在很多培训中老师都有讲过 不要过拟合，Over fitting。在本文中就不在赘述了，总之一句话 when you feels not right, it is not right! 但往往新手顾问找到可以提交的alpha 以后就直接提交了，这也错失了很多提高alpha 表现从而提高value factor的机会

**总结我常见的fitting方式包括：**

**1. 改变天数 Days、Std 等Operator里面的天数**

这部分没有太多的技术含量，通过有意义的天数进行替代，最简单的办法是都试一遍 5、22、60、120、240等。当然有经验的同学可以根据数据特性来进行有针对性的调优，比如季度更新频率的数据在ts backfill 5显然是没有意义的。

**2. 更改Universe, 中性化，decay等setting里的参数**

这里也可以暴力替换，自己维护一个不同region的universe、中性化的表即可。在实操中注意第一步里替换了天数等可以选择2-5个作为表达式进行回测，一方面multi simulation要大于1个alpha才可以。

**3.针对特定情况（比如高换手率）的fitting**

一个很好用但容易被忽视的工具 PnL Visualization, 默认大家可以看到的是PnL的曲线，点击右上角的下拉菜单还可以看到不同时间的换手率，sharpe等数值。


> [!NOTE] [图片 OCR 识别内容]
> 区 Open alpha details in new tab
> Chart
> Pnl
> Performance
> Pnl
> 6,00OK
> Turnover
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> OW
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
> Check Submission
> Submit Alpha
> Sharpe
> NNN


尤其有用的是turnover，但你看到在某一个时间这个alpha出现了剧烈的turnover的升高，很有可能是那段时间的数据有误，可以通过以下方式进行规避。（但group count是genius operator 部分人可能没有）

trade_when(group_count(alpha,market)>个数，alpha，0)

另外在手工回测的时候也可以勾选visulization选项（simulate按钮旁）这样也可以在pnl图上获取更多的信息（行业分布、市值分布、国家分布等）

此外降低turnover的常见方法包括  ts_decay_linear 等函数，尤其是平台最新推出的含有关键词tvr的operator，虽然可能会降低Sharpe，但降低tvr后可以提高fitness和margin  找到一个合理的平衡点即可。

需要注意的是这些operator需要配合scale使用，即 Operator（Scale(Alpha), Scale(Volume 如adv20）， 其他参数）

**二、【Fitting与Robust Testing】**

Value Factor本质是看OS的表现，那如果你的alpha可以在不同的universe 不同的中性化条件下都有不错的表现，也侧面证明了这个alpha本身是有很好的意义的，那也可以放心提交。

通过以上的步骤二，可以观察这个alpha在不同setting下的表现，从而进行判断是否提交该alpha

**以下是一些代码供参考**

**#获取alpha的表达式, 用来参考基线，并获取表达式**

```
target_id = 'alpha id'alpha_result = get_simulation_result_json(s,target_id)print('EXPRESSION:',alpha_result['regular']['code'])decay = alpha_result['settings']['decay']neut = alpha_result['settings']['neutralization']uni = alpha_result['settings']['universe']print('SHARPE:',alpha_result['is']['sharpe'])print('FITNESS:',alpha_result['is']['fitness'])print('MARGIN',alpha_result['is']['margin'])
```

#自行维护的对应关系表

```
region = 'ASI'neutralization = ['MARKET','SECTOR','INDUSTRY','SUBINDUSTRY']if region == 'ASI':neutralization.extend(['COUNTRY','CROWDING','FAST','SLOW','SLOW_AND_FAST'])universe= ['MINVOL1M','ILLIQUID_MINVOL1M']elif region == 'JPN':universe= ['TOP1600','TOP1200']print(neutralization)print(universe)
```

**第一步：更换天数等input**

```
days = ['5','22','60','120','240']winsorizes = ['1','2','3','4']
```

```
template = '''Alpha Expression'''expressions = []for day1 in days:forwinsorizeinwinsorizes:forday2indays:expression=template.replace('A', day1).replace('B', winsorize).replace('C',day2)expressions.append(expression)
```

**发送回测（请根据自己的代码做适配调整）**

```
#first round find daysfine_alpha_list=[]for expression in expressions:fine_alpha_list.append((expression, decay))fine_pools = load_task_pool(fine_alpha_list,10,10)print(datetime.now())multi_simulate2(fine_pools, neut, region, uni, 0, 1)print(datetime.now())
```

---

### 帖子 #33: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享_36617664667159.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo](../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo)
> 结合我最近参加的新顾问培课程中关于如何利用MCP来开发、优化alpha等内容，发表我的经验，顺便谈点感想。

作为新顾问的一份子，尤其代表零编程基础和零金融学基础的双小白，刚入门的我，只能靠模仿论坛中各位大佬，用他们现有的代码，跑论坛中现有的模板，虽然是“抄作业”，但我觉得完全不丢人，因为我相信没有谁与生俱来就拥有这能力，都是从模仿开始。于是我便靠着现有资源（三阶模板）每天碰碰运气，这样做的结果是一天有一天没，两天打渔三天晒网，不是跑不出来，而是跑出来的相关性太高。特别是11月开始深挖IND地区的时候，断粮了...


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Regular
> Regular
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> 儿52079 (Me)
> 0,00
> 0.50
> 0,37
> 0.19
> 0,00
> 0,00
> Tot
> policable
> Mainlar
> Super
> Super
> Super



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 转为正式顾问


直到11月8日，参加了新顾问的线上培训，课程上老师分享了很多能提高效率的工具和方法，其中包括了如何用MCP开发alpha模板，如何用app来实现全流程自动化。又恰逢IND地区开放，于是我决定，为了提升我的研究能力，接下来一段时间专注于IND地区的alpha开发（尽管不建议新手跑IND），当然我的方法也从开始的三阶代码换成了MCP和APP工具。

经过小半个月在IND地区的实践，发现挖出来的alpha老是出现几种问题，总结如下：

- 现有模板跑出来的相关性过高，shi都吃不上一口热的；
- 相关性低的，非常容易出现“Robust universe Sharpe of  **XX**  is below cutoff of  **X** .”
- 其他常见问题。

在拜读了大量论坛经验帖子后，决定将相关性太高的alpha直接放弃，于是乎突破点就集中在了如何解决Robust universe Sharpe过低上面，这里要特别感谢ZX12447大佬的分享，让我有了灵感，再结合MCP的智慧，创建了一个专门用于优化Robust universe Sharpe的工作流。基于该工作流，我成功优化几个alpha，解决了Robust universe Sharpe不达标的问题。

优化前问题：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained Pnl
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 05
> 9PASS
> Sharoe oT 3.25
> abOVe CUOffcf 1.58
> Finess of 3.11 isabove Cutoffof 1.
> Turnover of 15,60%
> abore CUtof of 196,
> Turpoverof 15.60%
> below CUOffof 4096.
> INeisht is WelI distribu-ed oerinstruments
> Sub-universe Sharpe CT 1.4isaboire Cutoff ot 0.96.
> 2year Sharpe Of 2.58 is
> bore Cutoff of 1.58,
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier oT -
> Effective Pyramid coun-for Genius is
> These -hemes mazch with the followinE multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The finalthEME Multiplizris 2
> 1FAIL
> Robust universe Sharpe Of 0.98
> below CUTOfOf1.
> 4PENDING
 优化后效果：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> TOM
> 5OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained
> Pn
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10PASS
> Sharpe OT 3.21
> aboVe cUOff of
> Fizness of 3,01isaboire Cutoff of -
> Turnoverof 18.2896
> aboie CUtoTf 196
> Turnover of 18.28%
> below CUOff of 40%
> Weisht is WEIl distrbuzed overinstruments。
> Sub-universe Sharpe
> 1.43
> bove Cutof of 0.95,
> Robust uniers=
> Of 1.01
> abore Cutoff ot
> 2year Sharpe Of 2.15 is above CutOff of 一
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier or
> Effectiye Pyramid Counzfor Genius
> These themes mazch with the followine multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The final theme multiplieris 2
> PENDING
> Shrpe


虽然这个alpha最终因相关性过高而未被提交，但是这是我用工作流成功优化的第一个alpha，所以将它作为代表案例展示出来。任务完成后，我让MCP将本次优化过程总结成了工作流，并且每次基于该工作流成功优化后将案例添加进工作流中。


> [!NOTE] [图片 OCR 识别内容]
> 9
> 你说
> 很好请将本次对话总结为优化robust的工作流
> API请求
> 50.0054
> Roo 说
> 我来为您创建
> 完整的IN0地区Robust universe Sharpe优化工作流文档。
> 检查点
> [
> 需要新建文件
> IND_Robust_Sharpe_优化工作流 .md
> +212
> -0巴
> 二
> API请求
> 50.0033
> 任务完咸


从这以后（11月23日），我竟然恢复了口粮，并且开始提交纯ra（之前都是ppa），今天（27日）提交了3个ra，所以借用论坛一位大佬的话“ *要重视你生产的每一个alpha* ”，因为它可能就是你下一个成功提交的对象。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod
> IESTI
> Correlation
> Correlation
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.6> 1
> e.6> 1
> e6>1
> SeeC
> e.6 >
> e.6 >
> anonymOUs
> Reaular
> ACTTVE
> 11/2712025 EST
> IND
> TOPSOO
> 0.58
> 0.61
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> 0.30
> 0.68
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> ReadyToSubmit
> 0.14
> 0.66
> anonymoUs
> Regular
> ACTIVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.41
> 0.49
> anonymOUs
> Reaular
> ACTTVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.13
> 0.70
> anonymoUs
> Reaular
> ACTTVE
> 11/25/2025 EST
> IND
> TOPSOO
> O.00
> 0.65
> anonymOUs
> Reaular
> ACTTVE
> 11/23/2025 EST
> IND
> TOPSOO
> 0.02
> 0.68
> anonymoUs
> ACTTVE
> 11/02/2025 EST
> IND
> TOPSOO
> O.00
> 0.17
> Reaular


最后送给诸君一句话并附上工作流：
 **The journey of a thousand miles begins with one step. JUST DO IT.**

```
# IND地区Robust Universe Sharpe优化工作流## 问题背景在IND地区alpha开发中，经常遇到**Robust universe Sharpe略低于1.0**的问题，导致无法提交。本工作流基于社区经验和实际案例，提供系统化的解决方案。## 工作流概览```mermaidgraph TD    A[诊断问题] --> B{分析差距}    B -->|差距<0.1| C[轻度优化]    B -->|差距>0.1| D[重度优化]    C --> E[时间参数调整]    C --> F[运算符优化]    D --> G[结构重构]    E --> H[测试验证]    F --> H    G --> H    H --> I{是否达标}    I -->|是| J[提交准备]    I -->|否| C```## 诊断阶段### 1. 问题识别```python# 检查Robust universe Sharpe指标LOW_ROBUST_UNIVERSE_SHARPE:  - result: FAIL  - limit: 1.0  - value: 0.98  # 差距0.02```### 2. 差距分析- **轻度问题**: 差距 < 0.1 (推荐本工作流)- **重度问题**: 差距 > 0.1 (建议重构alpha逻辑)## 优化工具箱### 核心优化方法#### 1. 时间参数调整 (最有效)```python# 原始ts_backfill(x, 60) → ts_backfill(x, 75)group_backfill(x, sector, 120) → group_backfill(x, sector, 275)# 推荐参数范围- ts_backfill: 60 → 75, 90, 120- group_backfill: 120 → 180, 252, 275```#### 2. 运算符增强```python# 添加稳定性运算符group_zscore(x, sector)        # 标准化信号ts_scale(x, 0.5)               # 时间序列缩放signed_power(x, 0.6)           # 符号幂变换```#### 3. 中性化优化```python# 尝试不同中性化组合group_neutralize(x, industry)group_neutralize(x, sector)group_neutralize(x, subindustry)group_neutralize(x, market)  # 对模型数据类Alpha特别有效```**中性化策略选择指南**：- **模型数据类Alpha**：优先尝试MARKET中性化- **基本面数据类Alpha**：优先尝试SECTOR/INDUSTRY中性化- **技术指标类Alpha**：根据数据特性选择合适的中性化层级#### 4. 截尾处理优化```python# 调整winsorize参数winsorize(x, std=4) → winsorize(x, std=3)winsorize(x, std=4) → winsorize(x, std=5)```## 实战案例### 案例1：IND地区imb5_score优化**原始alpha (FAIL)**```pythonfilled_score = ts_backfill(imb5_score, 60);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);signed_alpha = signed_power(neutralized, 0.5);final_alpha = group_backfill(signed_alpha,sector,120,std=4);final_alpha```- Robust Sharpe: 0.98 (FAIL)**优化版本1 (PASS)**```python3```- Robust Sharpe: 1.02 (PASS)**优化版本2 (简化版)**```pythonfilled_score = ts_backfill(imb5_score, 75);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);final_alpha = group_backfill(neutralized,sector,275,std=4);final_alpha```- Robust Sharpe: 1.01 (PASS)### 案例2：IND地区score_analyst_estimate_revisions优化（中性化策略优化）**原始alpha (FAIL)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 138), std=0.92), 108), 0.8), densify(sector))```- Robust Sharpe: 0.99 (FAIL)- 数据字段：score_analyst_estimate_revisions (覆盖率86.45%，金字塔乘数1.6)**优化版本 (PASS)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 150), std=0.85), 120), 0.8), densify(market))```- **关键优化**：中性化从SECTOR改为MARKET- **参数调整**：ts_backfill(138→150), ts_zscore(108→120), winsorize(std=0.92→0.85)- **性能提升**：  - Robust Sharpe: 0.99 → 1.11 (+12.1%)  - PnL: 11,095,177 → 12,997,115 (+17.1%)  - Sharpe: 2.56 → 2.62 (+2.3%)  - Fitness: 2.06 → 2.51 (+21.8%)  - 周转率: 16.63% → 13.66% (-17.9%)**核心洞察**：对于IND地区的模型数据类Alpha，MARKET中性化配合适当的时间窗口调整能有效提升Robust Sharpe表现，同时改善整体性能指标。## 系统化优化流程### 步骤1：基础诊断1. 运行原始alpha获取基准数据2. 记录所有检查项结果3. 重点关注Robust universe Sharpe差距### 步骤2：轻度优化 (差距<0.1)```python# 第一轮：时间参数调整尝试组合：- ts_backfill(60→75), group_backfill(120→275)- ts_backfill(60→90), group_backfill(120→252)- ts_backfill(60→120), group_backfill(120→180)```### 步骤3：运算符增强```python# 第二轮：添加稳定性运算符在group_neutralize后添加：- group_zscore(x, sector)- ts_scale(x, 0.5)- signed_power(x, 0.6)```### 步骤4：参数微调```python# 第三轮：参数优化调整：- winsorize std参数 (3,4,5)- signed_power指数 (0.5,0.6,0.7)- decay值 (0,5,20)```### 步骤5：验证与选择1. 比较所有优化版本的性能2. 选择运算符最少的版本3. 确保其他指标不受影响## 避免过拟合原则### 运算符数量控制- **理想**: 3-5个运算符- **可接受**: 6-8个运算符  - **风险**: >8个运算符### 经济意义保持- 每次优化应有合理的金融解释- 避免单纯为了提升指标而堆砌运算符- 保持alpha逻辑的简洁性和可解释性## IND地区特殊注意事项### 数据特性- Universe: 仅支持TOP500- 中性化选项有限- 数据字段相对较少### 优化策略1. **优先时间参数调整** - 对IND地区最有效2. **谨慎使用复杂运算符** - 避免过拟合3. **关注数据质量** - IND地区数据相对稀疏## 成功指标### 主要目标- ✅ Robust universe Sharpe ≥ 1.0- ✅ 其他检查项全部PASS- ✅ 运算符数量控制在合理范围### 次要目标  - 📈 IS Sharpe保持或提升- 💰 PnL表现稳定- 🔄 Turnover在合理范围内## 工具与资源### BRAIN平台工具- `get_platform_setting_options()` - 获取有效设置- `create_simulation()` - 测试优化版本- `get_alpha_details()` - 分析详细结果### 社区经验- **group_backfill/ts_backfill** - 时间参数调整最有效- **group_zscore** - 增强信号稳定性- **winsorize** - 处理异常值- **避免过度复杂化** - 保持alpha简洁## 总结本工作流通过**系统化的诊断→优化→验证**流程，有效解决IND地区Robust universe Sharpe问题。基于成功案例经验，关键优化策略包括：1. **精准诊断** - 明确问题差距和数据类型2. **中性化策略优化** - 根据数据类型选择合适的中性化层级3. **时间参数调整** - 适当延长时间窗口增强稳定性4. **避免过拟合** - 保持alpha逻辑简洁性和经济意义### 成功案例验证**score_analyst_estimate_revisions优化案例**证明了：- **MARKET中性化**对模型数据类Alpha效果显著- **参数微调**能同时提升多个性能指标- **整体性能提升**：Robust Sharpe +12.1%，PnL +17.1%，Fitness +21.8%通过这个方法，可以将接近达标的alpha（如0.98-0.99）成功优化到合格水平（≥1.0），同时显著提升整体性能表现。
```

---

### 帖子 #34: 【分析】Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md
- **讨论数**: 4


> [!NOTE] [图片 OCR 识别内容]
> Wotloquant 启动 !
> 分析1
> 交一个怎样的 & 能提升六维数据之定性定量分析
> IL47973
> 罗超林


[图片 (图片已丢失)]

在定性定量分析六维数据之前，如果你还不知道啥是genius等级和六维数据，建议去看以一下
 [【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板 – WorldQuant BRAIN]([Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md)  这一篇帖子，有解释了genius定级优胜制和六维数据字面意思，为此帖子做铺垫，和有几率增强六维某些数据的小tips；
        当然还有一些所见即所得的alpha 和 邪修alpha模板(没有)，以及包括一些点塔方法，不可否认的是，帖子内容的点塔方法有混塔嫌疑，没事。同上帖子还有一种明显的混塔方式(会多出一至两个op) 以及 一种隐形的 (不完全，存在小幅度扰动) 混塔方式 (至少多出两个op)，当然还有两种 非显非隐 纯点塔 (与混塔毫无干系) 方法，会大程度降低pc，且不会浪费操作符. 能不能看出来并想到就看自己了 .

[图片 (图片已丢失)]

写这个帖子的初衷是来源于 在冲刺genius等级时，我至少是想要保住我的 Operators per Alpha 和 Fields per Alpha 的. 
        有一天 (前两周)，我在操作自己产出的alpha时，发现有些 alpha 的操作符是大于我的 Operators per Alpha 的，此时我就在想，使用自己未使用的操作符作用在此 alpha 上会让此 alpha 信号变得更好时，我应该把 未使用过的操作符 加之在哪里 (操作符少于Operators per Alpha的alpha上还是大于亦或者是等于) 更加合适或者说怎么来降低 Operators per Alpha 的增大程度. [图片 (图片已丢失)]

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 《喜羊羊与灰太狼》
> 中惬意音乐响起令人放松的蟹螺湾椰树


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> )
> 欲将操作符分配与放置于后验&对前验0的平均操作符的变化程度是否有关?


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 第 genius 季度 ,我巳经在 worldquant 上提交了 N 个a, 将这 N 个a
> 按照某种顺序排列 ,便可得到 Q 序列.记为:
> )
> CN.
> 每个Q平均操作符数量 (不重复计数) Nop_per_alpha 计算公式为:
> N
> N
> Operators_count
> OP_per_alpha
> N
> k=1
> Operators_count 表示第k个 a 的操作符数量.
> C1'
> 02
> 03〉
> 其中 Ok



> [!NOTE] [图片 OCR 识别内容]
> 每个Q平均字段数量 (不重复计数) Nfield_per_alpha 计算公式为:
> Nfield_per_alpha
> Fields_count
> N
> k=l
> Fields_count
> 表示第尼个a 的字段数量.
> 其中 0k



> [!NOTE] [图片 OCR 识别内容]
> 记
> alpha 表示衡量 Q 的 OP_per_alpha 的变化程度 ,公式为:
> OP_per_alpha
> abs (OP_per_alphal
> OP_per_alpha)
> 其中 OP_per_alpha' 表示新增 &后的平均操作符数量。
> 现要提交两个&,一个0的操作符数小于X记为 QOperators_count
> 另外一
> N+I
> 个&的操作符数大于孓记为 QOperators_count
> 为了方便起见 ,我们不妨令已经
> 提交的 N 个c的平均操作符数量记为孓 ,现要增加 M 个操作符.
> Dop_per
> N+2



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> X
> 将这 MI 个操作符作用于 QwtI , 记L =孓+
> 此公
> N + 1
> 式一是为了方便观察先后作用,二是简化表达式 ,便会得到
> Ck



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> MI
> 十
> M
> N +1
> (N+I+ _
> N+2)
> OP_per_alpha'
> 二
> Ixtl +
> N + 1
> N + 2
> LNtI
> M+2



> [!NOTE] [图片 OCR 识别内容]
> 将这 M 个操作符作用于 Qwt2 , 会得到



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> MI
> 十
> M
> N +1
> (N+1, N+2T)
> OP_per_alpha'
> Ixt2 + N+I
> N + 2
> Lx+2
> M+I



> [!NOTE] [图片 OCR 识别内容]
> 通过化简 ,可以得到
> (N+It, Nt2) OP_Per_
> alpha
> (N+I,N+t2t) OP_Per_
> alpha'
> 也即
> (N+I+, N+2)
> Aop_per_alpha
> (NtI, N+2+ )
> Aop_per_alpha
> 说明操作符作用于某种类型的 & 并不会改变前验 a 的变化程度 .
> 以上证明也只是能说明操作符全部作用于小于或大于X的 Q, 不会改变
> 前验 Q 变化程度 ,还无法说明作用在等于X身上或每种类型作用若干操作符
> 会不会该改变前验 Q 的变化程度.
  
> [!NOTE] [图片 OCR 识别内容]
> 下面我们直接采用后验来证明操作符无论怎么作用于 Q, 对前验 Q 的变
> 化程度没有任何影响 .
> 若此 genils 季度 ,接下来总共还会交0个a,其中小于 等于和大于孓的
> Q分别有4,e,f个 ,有 def = 0等式成立 ,其等式中省略加法运算符号 ,采
> 用抽代并置表示加法.
  
> [!NOTE] [图片 OCR 识别内容]
> N+a
> N+d+e
> N+dtetf
> Operators_count
> Operators_count
> Operators_count
> 不妨记
> Qk
> :
> Qk
> k=N+I
> k=N+d+I
> k=Ntdtetl



> [!NOTE] [图片 OCR 识别内容]
> 分别表示为小于。等于和大于X的操作符数量之和 .同样地 ,现要增加 I 个操作符.
  
> [!NOTE] [图片 OCR 识别内容]
> N+a+etf
> Aop_per_alpha
> abs
> aOperators_count
> M - 孓.0
> /(N + 0) -孓
> K=N+I



> [!NOTE] [图片 OCR 识别内容]
> 从 Aop_per_alpha 公式可以看出干扰 Q 的 Operators per AIpha 的变化程度
> 跟0的操作符总数量。增加的 M 个操作符数量,
> 此 genius 赛季巳交a和操作符
> 数量有关 ,与这 MI 个操作符如何分配和放置无关 .


[图片 (图片已丢失)]

通过计算知道，将操作符分配与放置于后验alpha对前验alpha的平均操作符变化程度无关 . 
        虽无关，但在操作符对后验alpha影响小时，建议将其放置在性能相对而言不那么好的alpha身上，理应当让好鱼卖一个好的价钱 .

[图片 (图片已丢失)]

[图片 (图片已丢失)]  
> [!NOTE] [图片 OCR 识别内容]
> 《天堂度假村》前前右旁的小草地树林


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 二。六维数据定性分析


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 若两个函数&与h有相同的趋势 ,
> 则认为它们在趋势上对等,记为 8~-h.
> 在不考虑 genils 等级时 ,记 fscore 为个人总得分 , rank 为最终评级得分
> fscore
> rank , 也就是说 fscore 趋势与rank 相同 =
> fscore 便与最终得分有相同的效
> 果可作为最终评分 .
  
> [!NOTE] [图片 OCR 识别内容]
> 定性分析 ,记 Operators per Alpha  Operators used -
> Fields per Alpha`
> Rieldsused ,
> Community activity 和 Max simulation streak 分别表示六维的  每
> 个c的平均(去重)操作符数量。操作符的去重使用个数。每个Q 的平均(去重)字
> 段数量,
> 字段使用(去重)数量 rank [社区活跃程度]和最大连续回测天数 ,下面
> 使用简写 ,比如:最大连续回测天数记为 MIsS . 对于六维排名下面给出两种排名方
> 法,一种不需要量纲 .
  
> [!NOTE] [图片 OCR 识别内容]
> 第一种便是 rank , rank 是一个减函数,排名也是一个减函数 .由于 OpA
> 与FPA 越小越好 (有些会为0 ,需排除0) ,所以使用 rank 时尽量保持属于],
> 所以排名为
  
> [!NOTE] [图片 OCR 识别内容]
> rank
> rank
> rank(Ou)
> rank
> rank(Fu) + rank(Ca)
> rank(MIss)
> 十
> OpA2
> 1十
> FPA2
  
> [!NOTE] [图片 OCR 识别内容]
> 这样子是比较合理的 ,
> 按照权重来。每一个维度都是等权的 ,逻辑也是非常清晰的 .
  
> [!NOTE] [图片 OCR 识别内容]
> 但是需要注意的是当 OPA 和FA的数值为 0时,在内层 rank 时应设置为最
> 后一名 .
> 第二种是常用的标准化后加权求和 ,核心思想是:先消除不同指标的量纲
> 和尺度差异 ,再根据指标的重要性赋予权重 ,最后合并成一个综合得分 fscore
  
> [!NOTE] [图片 OCR 识别内容]
> 1.最小-最大归一化 ( Min
> Mac Normalization) , 又称为 [0 ,1]标准化 .
> 公式为
> X
> 3
> 3
> 其中,3表示原始数据 ,
> 是数据中的最小值 ,
> 是数据中的最大值 ,3'
> 是归一化之后的数据 .
> ?min
> ?max
> ?min
> RCmax
  
> [!NOTE] [图片 OCR 识别内容]
> 2.乏
> Score (标准差 )标准化
> 3 一 L
> 乙 =
> 几
> 其中 M: 该指标平均值,
> M = 1
> di
> 
> i=1
> 几
> 1
> O:
> 该指标标准差 ,
> O =
> Di -p)2
> 几
> i=1
  
> [!NOTE] [图片 OCR 识别内容]
> 3.赋予权重分配+综合得分
> fscore , 使用 [0 ,1]标准化公式 ,每个维度都分
> 配在 [0 ,1] ,六个维度使用等权 ,这里同样需要考虑当3' =0时的特殊情况 .
  
> [!NOTE] [图片 OCR 识别内容]
> SCOre
> dimension
> (1 - OpA)
> Ou' + (1 -FA)+ F' + Ca' + Mss'
> i=1
  
> [!NOTE] [图片 OCR 识别内容]
> 最后 rank(fscore ) 即可得出排名 .
  
> [!NOTE] [图片 OCR 识别内容]
> 第三种是我自己想的 ,感觉有一丢丢意义 ,于是在这里说一下,首先去掉
> 些异常值 (在逻辑自洽这块其实应该不要丢弃最好 ,因为每一个顾问的数
> 据都是真实的 ,不存在说是异常的 ),综合得分 fscore -
> 1.找出六维每个维度所有顾问的平均值丛或中位数;
> 几
> 山=1
> Ri
> 几
> i=1
> 2.使用最小公倍数 LCM 方法计算每个维度的权重 weight;
> weight
> LCM(opA; Nou
> NEu; Mca) MMsg)/
> Ri
> 几
> 2二1
> UFpA '
  
> [!NOTE] [图片 OCR 识别内容]
> 3.对于 OpA 和 FPA 数据使用关于均值对称反转 ,取 OpA ' 和 FPA' ,其
> 他维度都有 D' = 2 ;
> OPA
> 二
> 0 , OPA'
> 二 0
> FPA
> 二
> 0 ,RPA' =0
> OPAT
> OpA
> FPA'
> 一
> FPA
> 4.
> 计权重综合得分 fscore =
> fscore
> weight;
> dimension
> 2=1
> 最后 rank(fscore) 即可得出排名 .
> WopA
> WopA
> MppA
> NFpA



> [!NOTE] [图片 OCR 识别内容]
> C
> 欧拉乘积
> 1
> $(8) =
> 工
> 8
> 1-0
> p prime
  
> [!NOTE] [图片 OCR 识别内容]
> 《欧拉乘积公式》以此可证明素数无穷


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 三 六维数据定量分析


[图片 (图片已丢失)]

[图片 (图片已丢失)]

先说结论:  分而治之！分为三部分，1. Max simulation streak (最大连续回测天数) 保持回测不要断；2. 在社区有效学习；3. 其他四维为一块，如果操作符还未使用完，可以刷，看看上面的结论，操作符放在哪儿效果都是一样的，尽量交能够降低自己的平均操作符和平均字段，从rank来说，优先保证 Operators per Alpha  和 Fields per Alpha 的增量降低，然后再是 Fields used，因为 Operators per Alpha  和 Fields per Alpha 的密度更高，做好一次性rank可以上升好几名 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 定量分析 .在数学中, rank 犹如是一个 bug 的存在 ,
> 因为 rank 算是一个
> 指标器 ,
> 可以帮助进行排名 ,但是又没有办法去(计)量化细化它 ,只能类比
> 趋势.
> 由于不好量化 rank , 定性分析第一种方法有内置 ralk , 当有一个维度的
> rank 较低时 ,十分干扰整个排名 ,所以舍弃;第二种方法比较常规且好 ,我们
> 使用笫三种方法来定量分析 .
  
> [!NOTE] [图片 OCR 识别内容]
> 1.
> 计算每个维度的均值丛;
> [bopd] = 5, [bou] = 100, [LEpA]
> 二
> 4, [MRu] = 300, [bca]
> 二
> 25,
> 二150
> 2.计算每个维度的权重 weight;
> LCI
> Nou '
> NRui Hca' |Mss _
> 二 300
> weightopa
> 60, veight
> Ou
> 二
> 3, weightpo4
> 75, veight
> Fu
> 1, weightca
> 12, weight
> U85
> 2
> [Muss
> WopA '
> IFpA '
  
> [!NOTE] [图片 OCR 识别内容]
> 3.计算每个维度应该被权重值?';
> OpA' = 6.6 , Ou'
> 二
> 68 , FPA' = 6.5 , Fu'
> 二
> 260
> Ca'
> 二
> 3
> MIss
> -
> 88
> 4.计算综合得分 fscore;
> fscore
> 
> 60 .6.6 十3 .68+75 .6.5+1
> 260+12
> 33+2.88
> 二
> 1919.5


---

### 帖子 #35: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **讨论数**: 90

吹哨人又来了，这次继续带来一个好消息。当你点击下面那个小灯，你就找对了地方。


> [!NOTE] [图片 OCR 识别内容]
> Expression Editor
> Clear
> SaVe Current Template
> Overrite Existing
> 找灵感
> ctime_series_operator/> (sentiment_difference,
> 〈days/〉)


操作如图


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)步骤3:输入搜索关键词搜索数据集
> 关键词可以是pyramid之类都行
> 步骤4:点击生成
> Configuration
> Select Dataset
> 3. Results
> Generate Nlpha Templates
> Download MD
> LLM Settings
> Search dataset _
> Search
> 以下绐出5 组可直接在平台落地的" Alpha 模板"。
> Base URL
> 每个模板均保留"插槽"一一用<>标注
> ~方便后续批量替换。
> 网格搜索或遗传进化。
> 已选数据集: analyst15
> https llapimoonshot cnlvl
> 所有模板已预置:
> 数据清洗 (backfill
> Winsorize)
> 步骤5:下载后慢慢品味和
> Name
> Mocel Name
> 经济逻辑 (动量
> 预期差
> 估值。质量。情绪)
> 实施,并把模板放入赢
> kimi-k2-turbo-preview
> Performance
> 常见中性化(行业/市值)与衰减选项
> tUTnoVer
> 控制接口
> (ts_target_tVr_* )
> 进行配置和展开
> Weighted
> API Key
> analystl0
> Analyst
> 模板1:  分析师预期动量
> (Estimate Revision Momentum)
> Test
> Estimates
> 经济直觉:  过去1个月 EPS 上调幅度越大的股票。未来越可能继续跑赢。
> 步骤1
> 输入API
> analyst11
> ESG SCOres
> 3Iph3
> eXP_Window(
> Simulation Settings
> Estimations OT
> 9rOUP_ZsCOre(
> analyst14
> T5_backfil(
> Reglon
> Fundamentals
> winsorize(<anll15_9r_12_m_Im_chg >, std=4j
> EUR
> Earnings
> Unierse
> analystl5
> fore-asts
> 9rOUP>
> TOP12O0
> Analyst
> Delay
> analyst4
> Estimate Data
> 〈half_life >
> for Equity
> 插槽:
> Integrated
> gr_12_m_Im_chg>
> 可换 3m/Gm 或 SAL/CPS/EBG 等
> 步骤2:按需选择
> analyst44
> Broker
> 〈groUp>
> industry
> Sector
> subindustry
> Estimates
> 〈half_life >
> 5~30天可调。控制换手
> Block comments Tor multiple lines
> Key
> Jecay
> Kej
> <anl15


**这是2.0时代了，拥抱交不完的Alpha吧。**

**下面有一个无脑mcp简易版**

**[[MCP]找灵感功能上手详解](../顾问 LW67640 (小虎) (Rank 24)/[Commented] [MCP]找灵感功能上手详解经验分享_37113649831831.md)**

---

### 帖子 #36: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md
- **讨论数**: 60

吹哨人我又来了。看到了MCP里的新工具


> [!NOTE] [图片 OCR 识别内容]
> 缘分一道桥 (Alpha 跨区连锁)
> 返回主页
> C 使用说明
> 1.获取一段时间内的Alpha列表
> 2.分析每个 Alpha里的数据字段并迸行强替换。查看是否在其他Region/Universe/Delay有同样字段
> 3.生成新的Alpha
> 4.本页面的回测方式为排队回测; 一个完成后才会发送另一个;因此中途退出页面会中断回测
> 5.过长的回测队列有时会因为账号超时登出而出现连续失败。因此不建议选择过长时间跨度
> 6.如想批量回测;请下载所有待回测的Alphaf 选择首页回测器迸行回测
> 7.如果你想;你可以输入个很大的时间范围;下载所有表达式。慢慢迸行批量回测。


这个能直接一键回测并且横向点塔。更新到1.7.0版本以上就有噢。

我已经想到这样美好的图景：

- 1.横向点塔 （跨区、跨Universe)
- 2.点亮的塔，放入72变纵向点塔
- 3.被72变点量的纵向塔，再用桥，横向点塔。
- 4.横向点了塔，再72变
- 5. 如此反复，无穷尽也

以后我的研究，只需要专注于做好1-2个手搓或者AI合作的高级货，就能不断繁衍了！

效果不错，单击一下就能直接排队回测，我已经又完成了今天的提交。


> [!NOTE] [图片 OCR 识别内容]
> 2025-11-30104:40:58-05;00
> 10 个可用娈体
> 表达式: Srowp
> IIOIJLalize (1
> subindustry}
> 夏普: 0.65|收益:4.1%
> 戛普:0.69
> 收益:
> 4%
> 夏普:1.121收益:6.0%
> 夏普:0.95
> 收益:4.9%
> 夏普:
> 收益:
> .8%
> 夏普:086
> 收益:4.5%
> 戛普:0.76
> 收益:4.1%
> 戛普:1.16 |收益:7.7%
> 夏普:1.11 |收益:7.5%
> 夏普
> 1.05
> 收益-7.2%


再次叠甲：如有侵权，请联系本人。再次感谢作者。

---

### 帖子 #37: 【新人指南】到底要交什么样的Alpha？置顶的
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人指南】到底要交什么样的Alpha置顶的_32226888249239.md
- **讨论数**: 29

## **到底要交什么样的Alpha？——新人指南**

在Alpha开发与提交的过程中，许多新人常常会问：“到底什么样的Alpha才值得提交？”这是一个复杂的问题，因为Alpha的质量并没有一个单一的“金标准”可以作为绝对的判断依据。新人常见的错误是过度依赖某一两个单一指标，比如  **Sharpe** 、 **Fitness**  或  **Margin** ，认为只要这些指标表现良好，Alpha就一定值得提交。

然而，判断一个Alpha是否值得提交更像是诊断病情——不能仅仅依靠一个指标或单一的维度来做出决定。单一指标可能会提供片面的信息，而忽略了Alpha整体表现的复杂性和多样性。这种过度依赖单一指标的思维方式，往往会导致新人在Alpha提交过程中出现偏差。

### **数量与质量的平衡：螺旋上升的原则**

在Alpha的开发与提交过程中， **数量** 和 **质量** 是两个不可分割的重要维度。许多新人在实践中常常犯两个极端的错误：要么过度关注质量而忽视数量，要么完全不管质量，只追求数量。这两种错误都会对Alpha的整体表现产生负面影响。

#### **数量不足的问题**

如果过度追求质量而导致提交的Alpha数量不足，可能会出现以下问题：

1. **Portfolio不稳定** ：
   Alpha的数量不足会导致整体Portfolio的表现缺乏多样性，从而增加OS（Out-of-Sample）结果的不稳定性。
2. **缺乏真实水平的验证** ：
   单个Alpha的表现可能具有偶然性，只有通过足够的数量才能更接近整体的真实水平，避免因个别Alpha的异常表现而影响整体判断。

#### **质量不足的问题**

另一方面，如果完全忽视质量，只追求数量，也会带来风险：

1. **Portfolio表现受损** ：
   大量低质量的Alpha会拉低整体Portfolio的表现，导致Margin、Sharpe等关键指标下降。
2. **资源浪费** ：
   提交大量低质量Alpha不仅浪费了开发时间，也可能对平台的审核资源造成压力。

#### **螺旋上升的原则**

数量和质量并非对立，而是一个螺旋上升的过程。新人在初期阶段可以优先解决数量的问题，通过提交足够数量的Alpha来建立基础，然后逐步提高质量要求，最终实现数量与质量的平衡。

- **新人建议** ：
  每个月提交的Alpha数量不要少于  **40个** 。这一数量可以帮助新人更接近整体的真实水平，同时避免因单月表现异常而影响长期结果。
  - **数量的意义** ：足够的数量可以为Portfolio提供多样性，降低单个Alpha表现异常对整体的影响。
  - **质量的提升** ：在数量达到一定基础后，可以逐步提高Alpha的质量要求，例如优化Turnover、Margin等关键指标。

### **平台的“最低标准”与其意义**

在Alpha提交过程中，平台设定了一些“最低标准”，这是每位新人必须满足的基本要求。这些标准的存在并非是为了限制，而是为了确保Alpha在实际应用中具有一定的可行性和质量。然而，许多新人在实践中往往只关注如何通过这些指标，而忽略了这些要求背后的逻辑和意义。

#### **Turnover的要求**

**Turnover**  是一个重要的指标，它衡量了Alpha的换手率。平台要求Turnover不能高于  **70%** ，这是为了避免交易频率过高导致交易成本过高，从而影响  **Margin**  的表现。换手率过高会显著增加手续费，最终削弱Alpha的盈利能力。

- **进阶建议** ：
  - 当你的水平到达一定程度，建议将Turnover控制在  **30%**  以下。
  - 当你已经不再断粮，建议将这一指标进一步降低至  **15%**  以下。
- **特殊情况** ：
  - 如果Turnover较高，但  **Margin**  同时表现非常优秀（例如Margin超过  **10** ），这种情况下高换手率是可以接受的。

#### **Turnover的下限**

平台同时要求Turnover不能低于  **1%** ，这一点常常让新人感到困惑。事实上，这一要求的意义在于避免Alpha的持仓过于稳定。换手率过低会导致Position长期不变，而这与对冲基金的核心理念相悖。对冲基金的本质是通过动态调整持仓来捕捉市场机会，而过低的换手率可能意味着Alpha缺乏足够的市场反应能力。

### **Sub Universe与Robust Test的重要性**

在Alpha的评估过程中， **Sub Universe**  是一个关键的测试维度。平台要求Alpha在较小的股票范围（Sub Universe）中仍然保持一定的表现，这一要求的最低标准是  **50%**  的Sharpe。这意味着，如果Alpha在当前的Universe（例如Top3000股票）中表现良好，那么在更小的Universe（例如Top1000股票）中，它的Sharpe也必须达到至少50%的水平。

#### **Sub Universe的原理**

这一要求的核心逻辑是为了避免Alpha的信号仅来源于流动性较低的小市值股票。如果一个Alpha在Top3000股票中表现良好，但在Top1000股票中完全失效，这通常表明其收益主要依赖于流动性较低的那2000只股票。这种情况可能会导致Alpha在实际应用中面临较大的风险，例如流动性不足或交易成本过高。

#### **Robust Test的概念**

**Robust Test**  是一个更广泛的概念，旨在通过调整各种参数来测试Alpha的稳定性和敏感性。具体来说，Robust Test可以包括以下两种方式：

1. **调整Settings中的指标** ：
   - 例如修改交易成本、滑点、或其他市场环境参数，观察Alpha的表现是否稳定。
2. **调整Expression中的参数** ：
   - 修改Alpha表达式中的关键参数，测试结果的敏感性。
   - 如果结果收敛性较好，说明Alpha具有较强的鲁棒性；如果结果发散性较强，则表明Alpha可能过于依赖某些特定条件。

#### **实践建议**

- **前期阶段** ：
  在Alpha开发的初期，可以暂时不需要过多关注Robust Test，重点放在满足平台的最低要求（如Sub Universe的表现）。
- **后期阶段** ：
  随着经验的积累，可以逐步加强Robust Test的强度，通过调整参数和环境来验证Alpha的稳定性。

### **IS测试与长期稳定性：Alpha的“望诊”**

在Alpha的评估过程中， **IS Ladder Testing** （针对Regular Alpha）和 **2-Year Testing** （针对Atom Alpha）是平台用于检测Alpha稳定性的重要工具。这些测试的核心目标是通过观察Alpha的PNL表现，评估其长期稳定性。这一过程类似于“望诊”，通过观察PNL的形状来判断Alpha的健康状况。

#### **PNL的理想形状**

最理想的PNL表现是一条从左下角到右上角的稳定直线。这种形状表明Alpha在长期内具有持续的盈利能力和较低的波动性，是稳定性和可靠性的最佳体现。

- **新人阶段的目标** ：
  对于新人来说，能够通过平台的IS Ladder Testing或2-Year Testing已经是一个不错的开始。这表明Alpha在基本稳定性方面达到了平台的最低要求。

#### **进阶要求**

在进阶阶段，可以通过以下标准来进一步评估Alpha的长期稳定性：

1. **过去10年的表现** ：
   - 在过去10年中，Alpha的Sharpe超过  **1**  的年份不少于  **X年** （具体标准可根据个人目标设定）。
2. **最近两年的表现** ：
   - 特别关注最近两年的PNL表现，尤其是  **2022年**  的表现。

### **为什么要有PPAC？低相关性与Portfolio的多样性**

在Alpha开发与提交的过程中，平台引入了  **PPAC**  的机制，这不仅是为了给新人提供一个更宽松的探索环境，更重要的是为了强调  **低相关性**  和  **Portfolio的多样性**  对整体表现的重要性。

#### **Portfolio的概念：你的军队**

为了更直观地理解Portfolio的意义，可以将它比喻为一支军队。以往的Alpha评估标准过度追求  **Sharpe**  和  **Fitness**  等单一指标，这就像你的军队里清一色都是身高体壮的步兵。虽然这些步兵看起来很强壮，但缺乏多样性会让你的军队在面对复杂战场时显得单薄。

要让你的军队更有战斗力，就需要补充更多的兵种，例如：

- **斥候** ：负责侦查，提供灵活性。
- **炮兵** ：提供远程打击能力。
- **后勤兵** ：确保资源供应，维持军队的稳定性。

同样的道理，Alpha的Portfolio也需要多样性。一个多样化的Portfolio可以更好地应对不同的市场环境（OS），从而提升整体的稳定性和表现。

Self Correlation是一个很直观指标，新人的时候0.7是平台的要求。PPAC的要求是Pool内0.5的要求。值得一提的是这里的SC会随着提交数量的变多而更难有低的表现

- 0.5-0.7 之间的sc是可以通过的标准
- 0.3-0.5 之间的sc已经是很不错的了，通常对portfolio有一些提升
- 0.3以下的sc通常是很低的了

### **经济学意义与OS表现：从Alpha描述开始**

在Alpha开发与提交过程中， **经济学意义**  是决定OS（Out-of-Sample）表现的关键因素之一。许多老师常常强调这一点，因为具有经济学意义的Alpha往往能够更好地适应不同的市场环境，展现出更强的稳定性和可靠性。

#### **写Description的重要性**

对于新人来说，写好Alpha的  **Description** （描述）是一个非常重要的环节。这不仅是对Alpha逻辑的总结，也是开发者学习和思考的过程。可以将Description视为自己的学习日记，通过记录Alpha的核心逻辑和设计思路，帮助自己更好地理解经济学意义。

### **总结**

Alpha的开发与提交是一项复杂的任务，既需要满足平台的最低要求，也需要从长期稳定性、Portfolio优化和经济学意义的角度进行深入思考。新人在实践中应避免过度依赖单一指标，重视数量与质量的平衡，关注整体Portfolio的表现，并通过写Description来梳理自己的思路和逻辑。希望这篇指南能够帮助新人更好地理解Alpha开发的核心原则，并逐步提升自己的能力。

---

### 帖子 #38: 【新人科普】BRAIN 平台上的四类Alpha（RA, ATOM, PPAC, SA）
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普】BRAIN 平台上的四类AlphaRA ATOM PPAC SA_32032672214807.md
- **讨论数**: 74

在 WorldQuant BRAIN 平台上，根据表达式复杂度、字段来源以及检测机制的不同，BRAIN 平台将 Alpha 分为四类： **Regular Alpha（RA）** 、 **ATOM Alpha** 、 **PPAC Alpha**  和  **Super Alpha（SA）** 。本文将为新人系统性介绍这四类 Alpha 的核心特征、检测规则及策略建议。

## 1. Regular Alpha（RA）——最基础也最严谨的 Alpha 类型

对于 Regular Consultant（非 IQC）来说， **Regular Alpha（RA）**  是最早接触、也是最常使用的一类 Alpha。

### ✅ 特点：

- 表达式内的操作符和数据字段数量只要不超过  **64 个** ，就可以提交；
- 几乎 **没有其他限制** ，是最自由的表达方式；
- 需要通过  **所有的 Alpha 检测标准** 。

### 🧪 关键检测机制：

1. **IS Ladder Testing** ：查看 Alpha 在过去 10 年是否每年都有稳定 Sharpe，防止因子过拟合于局部时期。
2. **Sub-Universe Testing** ：验证 Alpha 在不同Universe子集下的表现一致性。
3. **Weight Concentration Testing** ：防止 Alpha 只在极少数股票上集中信号，影响实盘效果。
4. **Product Correlation Testing** ：检测 Alpha 是否和已有产品的表现高度重合，避免“重复造轮子”。

## 2. ATOM Alpha —— 来自单一数据集的“纯净信号”

**ATOM Alpha**  是自 2024 年开始引入的新类型，最初用于特定 Alpha 比赛, 后推广持续沿用。更多信息请见：

[[链接已屏蔽])

### ✅ 判定标准：

- **所有使用的数据字段必须来自同一个数据集** ；
- 常见的  `group`  字段如  `industry` 、 `country`  等是豁免字段，不计入数据集数量限制；
- 提交后页面上会出现“ **Single Dataset Alpha** ”标签。

### 🧪 特别检测机制：

- **放松了 IS Ladder Testing 要求** ；
- **仅要求通过最近两年的 2-Year Sharpe 检测** 。

> 💡 设计逻辑：同一数据集下的数据字段类型更统一， **降低混信号风险** ，更利于 OS 稳定性提升，从而提升 VF（Value Factor）得分。

## ⚡ 3. PPAC Alpha ——轻量但高效的入门路径

**PPAC（PowerPoolAlpha）Alpha**  是更简单直接的信号，比RA少了“修饰的”sub expression。源自于2025年的PPAC比赛，寻求pool内alpha的低自相关。

### ✅ 提交条件（非常宽松）：

- **最多使用 3 个数据字段** ；
- **最多使用 8 个操作符** （包含加减乘除等基础运算符）；
- 同样，常见的  `group`  字段如  `industry` 、 `country`  不计入字段/操作符数量。
- 25年11月更新，PPA alpha 需要是风险中性化中的一种（RAM, STATISTICAL, CROWDING, FAST, SLOW,SLOW_AND_FAST） 才可以提交
- 数量限制

1. 新顾问前三个月对于PPA没有限制
2. 三个月后，如果一个Alpha 符合 PPA + ATOM 或 PPA + REGULAR 或  PPA + ATOM + REGULAR 无限制
3. 三个月后，如果一个alpha 仅有PPA，则一天只能提交1个，且一个月在一个region只能由10个quota

提交后会显示标签：“ **PowerPoolAlpha** ”。

### 🧪 简化检测机制：

- 只要求  **Sharpe > 1** ；
- 通过  **Sub-Universe 检测** ；
- 所在地区的 PPAC Pool（不含非PPAC）需满足：
  - 自相关性低于 50%，或
  - 表现领先于 10% 以上。

> ⚠️ 尽管检测标准大幅降低，但这对提交者的 **自我克制能力** 提出了更高要求。
> 提交数量上升后，要特别注意  **分散性与质量平衡** ，建议早期尽量使用不同模板和数据源， **避免高自相关性** 。

## 🚀 4. Super Alpha（SA）——属于进阶顾问的 Alpha 策略组合

**Super Alpha（SA）**  是平台为有一定alpha积累的顾问推出的进阶功能。更多内容请见：

[[链接已屏蔽])

### ✅ 启用条件：

- 顾问提交的 Alpha 总数达到  **100 个** ；
- 可以从自己已提交的 Alpha 中组合构建；
- 高级顾问（Genius 等级）还可选择  **其他人的 Alpha**  作为基础组件。

### 💰 权益优势：

- 每天可单独提交  **1 个 Super Alpha** ；
- 不计入每日 4 个常规 Alpha 限额；
- 可获得每日额外  **$1~$60**  的收益（与表现挂钩）；

> Super Alpha 是  **Alpha 组合优化领域，对自己本身的regular alpha如果很好，SA也会很好** 。建议VF高了以后提交，会有更高的收益加成，更容易拿到60USD

## 🎓 新手建议：优先提交 PPAC + ATOM Alpha

对于刚加入 BRAIN 的新顾问，推荐策略如下：

- 多做  **PPAC Alpha** ：结构简单，利于练习表达式思维；
- **符合 ATOM 条件的 PPAC Alpha**  优先提交（双标签）；
- 前期应 **着重积累高质量且分散的信号** ，为后期组合打下基础；
- 有经济学意义的模版永远是重要的，不要混信号！

希望这篇文章能帮助你在 BRAIN Alpha 的旅程中更快起步，逐步掌握从表达到组合的核心技能。🎯

也希望可以点赞评论!

---

### 帖子 #39: 根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的_35129651186967.md
- **讨论数**: 30

## 引言：为什么我们要关心 PC？

 **降低 PC 是提升收益和保证账号健康的最重要因素之一** 。

1. PC的高低直接影响个人短期（base payment)和长期收入 (quarterly payment),
2. PC的高低间接影响Value Factor，从而再次影响收入
3. 高PC alpha 无法入库，无法参与比赛，长期提交大量高pc alpha，可能会导致账户封禁

## 一、理解Product Correlation

### 什么是 Product Correlation（PC）？

PC 衡量一个 alpha 与平台中其他 顾问提交的alpha 的相关性，其计算公式和自相关类似，为最近四年PNL 每日变化（diff）的皮尔逊相关性系数。

### PC高低与收入的关系

顾问提交的alpha被平台接收后，会进行多次筛选以决定是否对平台有用，其中最重要的筛选就是PC。当PC大于0.7，则被认为是相同/及其相近的alpha，则该alpha不会被平台采用，因此也不会有机会获得任何weight。在顾问协议中披露的每日base payment 计算公式中也明确提到与base payment与PC的负相关性。通常来说，当pc< 0.5 会被认为是比较独特的因子，从而会获得更高的base payment，也更有机会被基金经理采纳而获得weight，进而获得更高的quarterly payment。

而更低的PC也意味着更低的SC，组合的correlation 越低，也会进一步提升组合的整体多样性表现，从而获得更好的value factor。从个人经验看，在点塔的时候偶尔提交了更高的pc alpha，相应的该月份的vf就会受到影响。不知道平台在计算vf的时候是否对高pc有额外的惩罚系数。

### 举例说明PC高低与收入的实证

Alpha 1： PC 0.49的SA，获得了58.97的 base payment


> [!NOTE] [图片 OCR 识别内容]
> anonymoUs
> Super
> ACTIVE
> 08/30/2025 EDT
> JPN
> TOP1600
> 0.31
> 0.49



> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 08/30/2025
> Super:
> 58.97
> Regular:
> 7.94
> Total:
> 66.91
> 40
> 20
> 28.
> 29.
> 30.
> 31 _
> 1.Sep
> 2.Sep
> Aug
> Aug
> Aug
> Aug


Alpha 2：SAC 期间的一个表现更好的alpha，PC 0.68，只获得了9.69 USD的收入。而7月14日一个0.73的pc 只获得了5.4USD的收入。对不起当时0.9+的VF


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/19/2025
> Super:
> 9.69
> Regular:
> 8.10
> 15
> Total:
> 17.79
> 10
> 14.Jul
> 15.Jul
> 16.Jul
> 17.JUl
> 18.Jul
> 19.Jul
> 20.Jul


# **二、如何检查PC并降低PC的实操**

**获取PC的代码：论坛有很多，部分同学反馈没有权限，已更新在评论区**

[[链接已屏蔽])

**几个注意事项：**

1. 不建议直接只用check submission的接口，会更慢，因为要检查其他的测试比如自相关，而自相关等检测都可以在本地完成，效率更高
2. 该接口也会限流，甚至影响提交alpha，建议做一些在本地的限流，这样不触发平台限流，从而获得整体的结果最优（代码如下，可以自己调整睡眠时间）
3. 极少数情况会pc通过但是提交失败，这是因为pc是用的缓存数据，在pc检查和提交之间如果别人交了类似的会在提交时候出现pc不过的情况，但这种情况极少极少。

```
s = login()start_time = datetime.now()pass_pc_ids = []last_request_time = datetime.now()max_sleep_time = 60 * 60 # 最大睡眠时间1小时current_sleep_time = 60 # 初始睡眠时间60秒定义重连时间间隔reconnect_interval = timedelta(hours=3.5)for id in batch_ids:# 检查是否需要重新登录current_time = datetime.now()if current_time - start_time >= reconnect_interval:s = login()start_time = current_time# 记录请求开始时间request_start_time = datetime.now()# 调用 get_prod_corrpc = get_prod_corr(s, id)# 记录请求结束时间request_end_time = datetime.now()request_duration = (request_end_time - request_start_time).total_seconds()# 检查相关性if pc > 0.7:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['PROD Correlation'])elif pc >0.5:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['ace_tag'])else:result = get_simulation_result_json(s,id)selection = result['selection']['code']tag_value = ['PC 0.5','Ready to Submit']name_value = result['name']if "own" in selection:color = 'GREEN'count = count+1else:color = 'None'combo = result['combo']['code']while len(selection)<100:selection = selection + selectionwhile len(combo)<100:combo = combo + combo set_alpha_properties(s,id,name_value,selection_desc=selection,combo_desc=combo,tags=tag_value,color=color)pass_pc_ids.append(id)print(id,pc)# 计算上次请求到本次请求的时间间隔time_since_last_request = (request_start_time - last_request_time).total_seconds()# 如果请求时间明显增加，调整睡眠时间if request_duration > current_sleep_time * 1.5:current_sleep_time = min(max_sleep_time, current_sleep_time * 2)else:current_sleep_time = 60 # 如果请求时间正常，恢复默认睡眠时间# 更新上次请求时间last_request_time = request_start_time# 等待当前睡眠时间time.sleep(current_sleep_time)print(len(pass_pc_ids))
```

## 三、如何降低 PC？

Global 论坛有一篇外区的帖子，有些内容是很有可取之处的

- [Reduce Production Correlations. – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] Reduce Production Correlations_29301199149463.md)

### 避免使用过于常见的 signal

- 如单纯的暴力一二三阶，没有任何自己的迭代

### 增加创新表达方式

- 多尝试非线性组合、二阶交叉项、相对排名等。使用sigmoid，sign power，ts linear window等做一些数学变换
- 尝试使用target tvr的几个operator来降低tvr的同时也会变化pnl从而降低pc （但有时会反而提高，因为别人也使用了该方法提交过）

### 尝试多种region，unvierse和netralization 方式

- 一些高pc的因子，在变换了中性化，unvierse和regioin后会有意想不到的收获，而这个可以代码工程化完成

### 多尝试新的数据集

- 当有新的数据集，新的unvnierse和新的region的时候是pc最低的时候，如TOPDIV3000，最近新上的数据集等

### 使用独特的分组方式

- 最常见的是group datafield （如other455），bucket分组

### 当然王牌还是有自己的模版和自制数据

### 如何快速总结已经提交alpha的PC：

在alphas菜单中点击submitted，选中select column 勾选product correlation，已经提交alpha的PC一目了然


> [!NOTE] [图片 OCR 识别内容]
> 鬯2
> Simulate
> Alphas
> Leamn
> Data
> Labs
> Genius
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> 《
> Refer a friend
> Select Columns
> Summany
> Properties
> Settings
> Perommance
> Alphas
> Nams
> SzazUs
> Resion
> Instrument TypE
> Sharpe
> Rezurns
> Competi-ion
> Catesory
> Universe
> Delay
> Pnl
> Turnoer
> Page size
> Typ=
> Color
> Decay
> Neutralization
> Drawdown
> Marsin
> Fllter
> LansuaEs
> TaE
> Truncation
> Unit Handlins
> Fitnsss
> Book Sizs
> Date Submit-ed (EST]
> Hidgzn
> NaN Handlins
> Pasteurization
> ~oun
> Shor Count
> Select Columns
> Turnover
> Tag
> Favorite
> Sharo 50
> Sharpe 125
> S-ar Date (EST
> Sharpe 250
> Sharpe 500
> 22
> See
> OSIIS Razio
> Pre Close Sharpe
> 4.974
> Pre-Close Razio
> Self-Correlation
> Prod-Correlation
> Reset
> Apply
> Lns


最后祝大家新的赛季VF和Genius双高！如果对你有用还请点赞评论！

---

### 帖子 #40: assuming final_example_alpha_list is your listfunction to divide the list into chunksdef divide_chunks(alpha_list_with_settings, n):    looping till length l    for i in range(0, len(alpha_list_with_settings), n):        yield alpha_list_with_settings[i:i + n]divide the list into chunks of size 10n = 10chunks = list(divide_chunks(final_example_alpha_list, n))print each chunkfor i, chunk in enumerate(chunks):    print(f"Chunk {i+1}:")    print(chunk)    print("\n")
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md
- **讨论数**: 15

**【重要】使用API请关闭VPN！使用API请关闭VPN！使用API请关闭VPN！**

目前API已经基本可以实现平台上所有的靠鼠标点击的功能了吧，这些是我的总结。有些功能可能没有总结到，欢迎大家配合这篇文章一起使用👉 [Brain API技巧：如何挖掘API]([L2] Brain API技巧如何挖掘API代码优化_20309362198679.md)


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Consultant program
> Events
> Refer a friend
> SignIn
> Sign In
> Email
> Email field empty
> Password
> Forgot password
> Sigm
> Don't have an account? Sign Up here
> Having trouble signing in? Contact support


**STEP 1:Authentication 登录账号** 

- 描述: Authenticates the user using the /authentication endpoint 使用/authentication端点进行身份验证
- **每个登录Session有效期为4小时，请检查你的代码切勿频繁登录，24小时内登录超过25次将会冻结账户**
- Input: A POST request to the /authentication endpoint with a basic authorization header (username and password) 向/authentication端点发送带有用户名和密码的POST请求
- Output: On success, it returns a JSON Web Token (JWT). If biometrics sign-in is enabled, it returns a 401 status code and a header location。成功后，返回一个JSON Web Token (JWT)。 **如果系统启用了生物识别登录（针对非中国大陆用户），它将返回401状态代码和一个header位置。这个header位置是一个链接（or QR code)，需要扫码完成。**
- Code:

```
import requests
#建议将用户名密码放到另外的文件内存储
# Define the path to the text file that store your username and password, the first line should be your username and second line to be your password.
file_path = "credentials.txt"

# Initialize variables to hold the username and password
username = ""
password = ""

# Open the file and read the lines
with open(file_path, "r") as file:
    username = file.readline().strip()  # Read the first line for the username and strip newline characters
    password = file.readline().strip()  # Read the second line for the password and strip newline characters# Create a session to persistently store the headers s = requests.Session() # Save credentials into session s.auth = (username, password) # Send a POST request to the /authentication API response = s.post('[链接已屏蔽])
```

**一种解决超时登出的解决方案（超过4小时会登录session会过期）**

```
def sign_in(credentials_path):    import requests    from time import sleep    # Initialize variables to hold the username and password    username = ""    password = ""    # Open the credentials file and read the username and password    try:        with open(credentials_path, "r") as file:            username = file.readline().strip()  # Read the first line for the username and strip newline characters            password = file.readline().strip()  # Read the second line for the password and strip newline characters    except FileNotFoundError:        print(f"Error: The file '{credentials_path}' was not found.")        return None    except Exception as e:        print(f"An error occurred while reading the credentials file: {e}")        return None    # Create a session to persistently store the headers    s = requests.Session()    # Save credentials into the session    s.auth = (username, password)    while True:        try:            # Send a POST request to the /authentication API            response = s.post('[链接已屏蔽])            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx            print("Authentication successful.")            break  # Exit the loop on success        except requests.HTTPError as e:            print(f"HTTP error occurred: {e}. Retrying...")  # Provide more specific error message            sleep(10)        except Exception as e:            print(f"Error during authentication: {e}. Trying to login again.")            sleep(10)    return ssession = sign_in("path/to/your/credentials.txt")
```

```
while True:    s = sign_in("path/to/your/credentials.txt")    try:        #Run Alpha code        print("running")    except:        print('connection down')        s = sign_in()
```

```

```

**STEP 1.1 Get Dataset like Data Explorer**  查找数据集


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> Region
> Delay
> Universe
> Data
> Datasets
> USA
> TOP3000
> Search
> Category
> Coverage; %
> Value score
> Alphas
> Users
> Name; description
> AlLcategories
> to
> 100
> to
> to
> t0
> Clear
> Dataset
> Fields
> Coverage
> Value Score
> Users
> Alphas
> Research Papers
> Analyst Estimate Data for Equity
> 350
> 609
> 3727
> 55502
> Report Footnotes
> 318
> 41%
> 3832
> 31093
> Company Fundamental Data for Equity
> 886
> 749
> 23292
> 674330
> [1],[2],[3], [4]
> Fundamental Scores
> 31%
> 151
> 674
> [1]
> Systematic Risk Metrics
> 16
> 779
> 1681
> 5455
> US News Data
> 322
> 80%
> 5373
> 43803
> Ravenpack News Data
> 75
> 689
> 645
> 8842
> [1],[2],[3],[4]
> Volatility Data
> 64
> 699
> 2437
> 30093
> Options Analytics
> 74
> 709
> 2204
> 10859
> [1],[2],[3]
> Price Volume Data for Equity
> 18
> 1009
> 26455
> 828156
> [1],[2],[3],[4],[5],[6],
> [7],[8],[9],[10], [11],
> [12]


- Description: 返回DataFrame文件
- **要注意数据集的Universe、REGION的DELAY的设定，不同的设定的数据集是不同的**
- **可以通过对返回的df内的category、name、description等字段进行筛选，找到所有相关的数据集**
- Input: session, settings (which includes region, delay, universe, instrumentType)
- Output: DataFrame
- Code:

```
#Example setting
settings = {'region': 'ASI', 'delay': '1', 'universe': 'ILLIQUID_MINVOL1M', 'instrumentType': 'EQUITY'}

def get_datasets(session, settings):
    url = "[链接已屏蔽] +\
        f"instrumentType={settings['instrumentType']}®ion={settings['region']}&delay={settings['delay']}&universe={settings['universe']}"
    result = session.get(url)
    datasets_df = pd.DataFrame(result.json()['results'])
    datasets_df['instrumentType'] = settings['instrumentType']
    datasets_df['region'] = settings['region']
    datasets_df['delay'] = settings['delay']
    datasets_df['universe'] = settings['universe']
    return datasets_df
```

**Get Datafield like Data Explorer**  获取所有满足条件的数据字段及其ID

 
> [!NOTE] [图片 OCR 识别内容]
> !C匕骘_
> BRNf
> Simulate
> CAlphas
> Learn
> Data
> 罟
> Competitions (0)
> {8 Team
> Community
> Consultant program
> Region
> Universe
> Data
> Datasets
> Analyst Estimate Data for Equity
> USA
> TOP3000
> Fields
> Description
> Search
> Coverage; %
> Type
> Alphas
> Users
> Name; description
> to
> 100
> All
> to
> to
> Clear 
> Field
> Description
> Type
> Coverage
> Users
> Alphas
> adjysted_Detincome 止
> Adjusted net income
> forecast type (revisionlnewl.)
> Matrix
> 879
> 390
> 1186
> anl4_ads1detailafv1 10_bk
> Broker name (int)
> Vector
> 699
> 30
> anl4_ads1detailafv1 10_estvalue
> Estimation Value
> Vector
> 699
> 17
> 38
> anl4_ads1detailafv1 10_person
> Broker Id
> Vector
> 699
> anl4_ads1detailafv1 10_prevval
> The previous estimation of finanicial item
> Vector
> 699
> 15
> 32
> anl4_ads1detailqfv1 10_bk
> Broker name (int)
> Vector
> 6396
> 19
> anl4_ads1detailqfv1 10_estvalue
> Estimation Value
> Vector
> 639
> 10
> anl4_ads1detailqfv1 10_person
> Broker Id
> Vector
> 639
> 2
> anl4_ads1detailqfv1 10_prewal
> The previous estimation of finanicial item
> Vector
> 639
> 10
> anl4_adxqfv110_down
> Number of lower estimations
> Vector
> 709
> 12
> anl4_adxqfv1 10_high
> The highest estimation
> Vector
> 709
> 11
> https:/ /platform worldquantbrain.com /data/data-setslanalyst4idata-fieldsyanl4_adjusted_netincome_ft
> Delay
> anl4
 

- Description: 根据Dataset id来获取数据字段
- **Dataset ID可以通过前步的df内获取，或者在平台网页上，鼠标放到相应的dataset上，在左下角即可看到data set id和datafield id**
- **要多注意data field的category和operator的匹配，尤其MATRIX和VECTOR的比较**
- Input: s, instrument_type, region, delay, universe, dataset_id, search
- Output: 返回DataFrame
- Code:

```
def get_datafields(
    s,
    instrument_type: str = 'EQUITY',
    region: str = 'USA',
    delay: int = 1,
    universe: str = 'TOP3000',
    dataset_id: str = '',
    search: str = ''
):
    if len(search) == 0:
        url_template = "[链接已屏蔽] +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50" +\
            "&offset={x}"
        count = s.get(url_template.format(x=0)).json()['count'] 
    else:
        url_template = "[链接已屏蔽] +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&limit=50" +\
            f"&search={search}" +\
            "&offset={x}"
        count = 100

    datafields_list = []
    for x in range(0, count, 50):
        datafields = s.get(url_template.format(x=x))
        datafields_list.append(datafields.json()['results'])
    datafields_list_flat = [item for sublist in datafields_list for item in sublist]

    datafields_df = pd.DataFrame(datafields_list_flat)
    return datafields_df
```

 **STEP 2: Simulating an Alpha**  回测Alpha


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> :
> Competitio
> Simulation 1
> Settings
> USA/D1/TOP3000
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save as Default
> Apply
> 20
> 21
> 22
> regular
> expression
> Clone this Alphaina new tab
> Example
> Simulate


- **描述: 用于回测Alphas, 一个完整的alpha（JSON）包括Settings （JSON）和 表达式（regular字段）组成，通过API 将这个alpha POST到服务器，成功的POST将获得一个在服务器的url （‘Location’）并获得回测进度条。**
- Input: A POST request to the /simulations endpoint with a JSON object that includes the settings of the simulation and the expression 向/simulations端点发送包含回测设置和表达式的JSON对象的POST请求
- Output: On success, it returns a URL in the HTTP response header Location. This URL can be used to check the progress of the simulation 成功后，它在HTTP响应头Location中返回一个URL。此URL可用于检查回测的进度；如果没有检查到Location ，则说明你的Alpha发送产生了错误。请检查常见错误👉 [BRAIN API及日常回测时常见的错误 – WorldQuant BRAIN]([L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md)
- **在大规模回测中，建议您将回测的Alphas List，回测时间和是否成功回测（lcoation url）存储在一个文件中（csv，json或其他格式），以方便debug和管理**
- Code:

```
simulation_data = {
    'type': 'REGULAR',
    'settings': {
        'instrumentType': 'EQUITY',
        'region': 'USA',
        'universe': 'TOP3000',
        'delay': 1,
        'decay': 15,
        'neutralization': 'SUBINDUSTRY',
        'truncation': 0.08,
        'pasteurization': 'ON',
        'unitHandling': 'VERIFY',
        'nanHandling': 'OFF',
        'language': 'FASTEXPR',
        'visualization': False,
    },
    'regular': 'close'
}
simulation_response = s.post('[链接已屏蔽] json=simulation_data)
```

 **STEP3: Alpha Simulation Status and Results Retrieval**  Alpha回测状态和结果检索


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> 159
> Simulations usually take a few minutes Ormore:
> Click here to cancel the simulation.
> TIP
> Submit Alphas with Iow Correlation to your other Alphas。
> Properties
> Simulate to saVe
> Name
> Category
> Currently 'anonymous'
> None
> Color
> Selectladd tags
> None
> Description
> Description
> Tags


- **描述：检查alpha回测的进度并检索结果, 一个成功的回测会获得一个服务器内的URL，在response里的‘Location'字段可以获得该URL，复制到浏览器内也可以访问。**
- **如果alpha 表达式有误或已经存在历史的回测中，将不会得到此URL，则回测失败。同时回测的最大上限为10个，所以在POST的任务中，如果FAIL则可以设置sleep一段时间后重试。**
- Input: A GET request to the URL returned when sending an alpha for simulation 向发送alpha模拟时返回的URL发送GET请求
- Output: If the alpha is still simulating, a Retry-After header is returned. Once the simulation finishes, the response includes a JSON object from which you can retrieve the alpha id 如果alpha仍在模拟中，返回Retry-After头。回测完成后，响应包含一个JSON对象，您可以从中检索alpha id （注意alpha id为7位，如：m8qlQZ1）
- Code:

```
from time import sleep

simulation_progress_url = simulation_response.headers['Location']
finished = False
while True:
    simulation_progress = s.get(simulation_progress_url)
    if simulation_progress.headers.get("Retry-After", 0) == 0:
        break
    print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
    sleep(float(simulation_progress.headers["Retry-After"]))
print("Alpha done simulating, getting alpha details")
alpha_id = simulation_progress.json()["alpha"]
alpha = s.get("[链接已屏蔽] + alpha_id)
print(alpha.json())
```

 **STEP 4: Record Sets of Alpha Simulations**  Alpha PnL绩效历史


> [!NOTE] [图片 OCR 识别内容]
> -SOOK
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Needs
>  IS
> Period
> TRAIN
> TEST
> IS
> O
> Improvement
> Summary
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.20
> 1.149
> -0.08
> -1.909
> 28.549
> -33.389600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2017
> 1.77
> 1.229
> 1.71
> 11.709
> 4.159
> 191.279000
> 1096
> 1936
> 2018
> 0.20
> 1.199
> 0.08
> 1.7896
> 10.019
> 29.789000
> 1093
> 1955
> 2019
> 0.04
> 0.899
> 0.01
> 0.289
> 6.0596
> 6.389600
> 1057
> 1979
> 2020
> -1.23
> 1.229
> -1.43
> -16.989
> 25.269
> -277.490000
> 1014
> 2020
> 2021
> 6.29
> 1.559
> 16.28
> -83.709
> 4.509
> -1,081.04900
> 1048
> 2035
> Long


- Description: Retrieves record sets containing the information about simulations 获取PnL图表的信息
- Input: A GET request to the /alphas/<alpha_id>/recordsets/<record set name> endpoint 向/alphas/<alpha_id>/recordsets/<record set name>端点发送GET请求
- Output: Returns a record set containing the information about your simulations for each trading day 返回日度级别的PnL信息
- Code:

```
from time import sleep

finished = False
while True:
    pnl = s.get("[链接已屏蔽] + alpha_id + "/recordsets/pnl")
    if pnl.headers.get("Retry-After", 0) == 0:
        break
    print("Sleeping for " + pnl.headers["Retry-After"] + " seconds")
    sleep(float(pnl.headers["Retry-After"]))
print("PnL retrieved")
```

 **Alpha Management**  获取特定alpha的表现

- Description: Manages alphas
- Input: A GET request to the /alphas/<alpha id> endpoint 向/alphas/<alpha id>端点发送GET请求
- Output: Returns a JSON object representing the alpha 返回Json文件，包含Alpha的所有信息，以下很多的功能都由此延申。
- ```
  alpha = s.get("[链接已屏蔽] + alpha_id)
  ```

 **STEP 5 Alpha List 批量获取已经完成回测的结果**

**
> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> :
> Competitions (0)
> {8 Team
> Community
> Consultant program
> 三
> 0 Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Size
> 10
> out of 51
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Search
> Select
> Selec
> Selec
> Search
> Selec
> Select
> e〉 1
> e8〉 1
> e8〉 1
> Select
> anonymous
> Regular
> UNSUBMITTED
> 07/30/2024 EDT
> USA
> TOP3000
> 0.32
> 3.189
> 1.159
> anonymous
> Regular
> UNSUBMITTED
> 07/10/2024 EDT
> USA
> TOP3000
> 1.39
> 7.299
> 1.579
> anonymous
> Regular
> UNSUBMITTED
> 07/10/2024 EDT
> USA
> TOP3000
> 1.34
> 7.0996
> 1.769
> anonymous
> Regular
> UNSUBMITTED
> 05/20/2024 EDT
> USA
> T0P3000
> 1.53
> 5.229
> 3.479
> anonymous
> Regular
> UNSUBMITTED
> 05/20/2024 EDT
> USA
> TOP3000
> 1.31
> 4.449
> 3.489
> anonymous
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 0.96
> 2.859
> 20.009
> anonymous
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 1.17
> 3.189
> 17.199
> anonymoUs
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 1.06
> 3.749
> 15.639
>  | | |
> 0oOI I3
> UNSIBNITTED
> OC /1 1 /00/
> C
> TO03O
> C 1O0
> CC0
> Page
> Tag
**

- ```
  Description: Retrieves records in the IS and OS Alpha list 获取所有在IS和OS列表的Alpha信息。这可以帮助你批量筛选出STEP2-3中，哪些回测是有信号的。建议将回测结果和之前的alpha list进行交叉比较（setting和regular （表达式）相同即为同一个alpha）
  ```
- ```
  未提交的alpha stage value是IS，已提交的stage 字段value是OS
  ```
- ```
  Input: session, total_alphas, limit
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to fetch a specific number of IS alphas (`total_alphas`) using pagination.
def get_n_is_alphas(session, total_alphas, limit=100):
    fetched_alphas = []
    offset = 0

    # Keep fetching alphas until the required number of alphas is reached or no more alphas are available.
    while len(fetched_alphas) < total_alphas:
        response = session.get(
            f"[链接已屏蔽]
        )
        alphas = response.json()["results"]
        fetched_alphas.extend(alphas)
        if len(alphas) < limit:
            break
        offset += limit
    return fetched_alphas[:total_alphas]
```

```

```

```
Check result of Checks 获得Checks的结果
```

- ```
  Description: 向/alphas/<alpha id>/check端点发送GET请求
  ```
- ```
  Input: alpha id
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  is_checks_response = session.get(f"[链接已屏蔽])
  ```

```

```

```
Check Self Correlation 自相关性检查
```

- ```
  Description: Retrieves self-correlation result by alpha_id 根据Alpha_id检查自相关性
  ```
- ```
  Input: session, alpha_id, max_retries
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to retrieve self correlation for the given alpha ID.
def get_self_corr(session, alpha_id):
    response = session.get(f"[链接已屏蔽])
    if response.status_code == 200 and "records" in response.json():
        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]
        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)
        return self_corr_df
    else:
        return pd.DataFrame(columns=["correlation"])

# Function that retries fetching self correlation for the given alpha ID up to `max_retries` times.
def get_self_corr_with_retries(session, alpha_id, max_retries=3):
    retry_count = 0
    while retry_count < max_retries:
        try:
            self_corr_df = get_self_corr(session, alpha_id)
            if not self_corr_df.empty:
                return self_corr_df
        except json.JSONDecodeError:
            pass
        retry_count += 1
        time.sleep(1)  # Wait for 1 second before the next retry
    return pd.DataFrame(columns=["correlation"])
```

```

```

```
Check Prod Correlation 全局相关性检查
```

- ```
  Description: Retrieves prod-correlation result by alpha_id 根据Alpha_id检查全局相关性
  ```
- ```
  Input: session, alpha_id, max_retries
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to retrieve prod correlation for the given alpha ID.
def get_prod_corr(session, alpha_id):
    try:
        response = session.get(f"[链接已屏蔽])
        response.raise_for_status()
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            print(f"Error while decoding prod_corr JSON for alpha {alpha_id}: Invalid or empty JSON")
            return pd.DataFrame(columns=["alphas", "max"])

        if "records" in response_data:
            columns = [dct["name"] for dct in response_data["schema"]["properties"]]
            prod_corr_df = pd.DataFrame(response_data["records"], columns=columns)
            return prod_corr_df
    except requests.HTTPError as e:
        print(f"Error while fetching prod_corr for alpha {alpha_id}: {e}")
    return pd.DataFrame(columns=["alphas", "max"])

# Function that retries fetching prod correlation for the given alpha ID up to `max_retries` times.
def get_prod_corr_with_retries(session, alpha_id, max_retries=3):
    retry_count = 0
    while retry_count < max_retries:
        try:
            prod_corr_df = get_prod_corr(session, alpha_id)
            if not prod_corr_df.empty:
                return prod_corr_df
        except json.JSONDecodeError:
            pass
        retry_count += 1
        time.sleep(1)  # Wait for 1 second before the next retry
    return pd.DataFrame(columns=["alphas", "max"])
```

```

```

```
Change Alpha properties 给Alpha更改设置，例如改名字，改颜色等
```

- ```
  Description: Change the Alpha's Property 向/alphas/<alpha id>端点发送patch请求
  ```
- ```
  Input: session, alpha_id, color or new_name
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to update the color of an alpha with the given color.
def update_alpha_color(session, alpha_id, color):
    update_data = {"color": color}
    response = session.patch(f"[链接已屏蔽] json=update_data)
    return response.status_code == 200

# Function to update the name of an alpha with the given name.
def update_alpha_name(session, alpha_id, new_name):
    update_data = {"name": new_name}
    response = session.patch(f"[链接已屏蔽] json=update_data)
    return response.status_code == 200
```

```

```

```
Get Performance Comparison 获取Performance Comparison的结果
```

- ```
  Description: Returns performance comparison for merged performance check 向/alphas/alpha_id/before-and-after-performance端点发送GET请求
  ```
- ```
  Input: s, alpha_id, team_id (optional), competition (optional)
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
def performance_comparison(s, alpha_id, team_id:Optional[str] = None, competition:Optional[str] = 'ACE2023'):
    """
    Returns performance comparison for merged performance check
    """
    if competition is not None:
        part_url = f'competitions/{competition}'
    elif team_id is not None:
        part_url = f'teams/{team_id}'
    else:
        part_url = 'users/self'
    while True:
        result = s.get(
            f"[链接已屏蔽] + alpha_id + "/before-and-after-performance"
        )
        if "retry-after" in result.headers:
            time.sleep(float(result.headers["Retry-After"]))
        else:
            break
    if result.json().get("stats", 0) == 0:
        return {}
    if result.status_code != 200:
        return {}

    return result.json()
```

```

```

```
补充：Multi-Simulation对应UI中的
```

```
    multisimulation_data = [        {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': 'USA',                'universe': 'TOP3000',                'delay': 1,                'decay': 15,                'neutralization': 'SUBINDUSTRY',                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'OFF',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': 'close'        },        {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': 'USA',                'universe': 'TOP3000',                'delay': 1,                'decay': 15,                'neutralization': 'SUBINDUSTRY',                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'OFF',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': 'open'        },        # Add more simulation data as needed    ]    # Send multisimulation request    multisimulation_response = s.post('[链接已屏蔽] json=multisimulation_data)    # Check response    if multisimulation_response.status_code == 201:        print("Multisimulation request sent successfully.")    else:        print("Error in sending multisimulation request.")
```

```
使用get方法获取multi Alpha的结果，其children的结果即为单个Alpha的Location,再对每个使用get方法，即可获得单个Alpha的id
```

```

```

```

```

```
设置Log来记录操作
```

```
import logging# Create a loggerlogger = logging.getLogger('my_logger')# Set the level of the logger. This can be DEBUG, INFO, WARNING, ERROR, or CRITICALlogger.setLevel(logging.INFO)# Create a file handler that logs even debug messageshandler = logging.FileHandler('my_log.log')handler.setLevel(logging.INFO)# Create a formatter and add it to the handlerformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')handler.setFormatter(formatter)# Add the handler to the loggerlogger.addHandler(handler)# Log some messageslogger.info('This is an info message')logger.warning('This is a warning message')logger.error('This is an error message')logger.critical('This is a critical message')
```

```
获取所有本人可用的operator
```

```
# 获取个人所使用的operatordef get_user_operator(session):    import pandas as pd    result = session.get("[链接已屏蔽])    df = pd.DataFrame(result.json())    return df
```

```

```

---

### 帖子 #41: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 1000

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #42: 【日常生活贴】我的量化日记第三季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **讨论数**: 1021

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #43: 【日常生活贴】我的量化日记第二季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **讨论数**: 1004

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #44: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 1025

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #45: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【环境配置】在Nvim中配置MCP的方法经验分享_34239307743639.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #46: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **讨论数**: 37


> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN](../顾问 JL71699 (Rank 64)/[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md) 
             Github插件地址： [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 安装插件
> .访问插件 GitHub 地址: https
> //github. com /zhangkaihua88 / WebDataScope
> 能访问Gitlub的请跳过这红色部分
> 0)如果访问不了 github.
> COm
> 换一个浏览器试试,
> 有几率解决 ,
> 如果不行 ,
> 请按照以下步骤操作。
> 〈 〉 C 命 ^ 众
> 0
> [链接已屏蔽] MebDataScope
> 器
> 无法访问此网站
> 连接已重置。
> 请试试以下办法:
> 检查网络连接
> 检查代理服务器和防火墙
> 运行 Windows 网络诊断
> ERR_CONNECTION_RESET
> 重新加载
> 详情
> 1)同时按住 [Window
> Or
> Start ]
> + R, 输入 cmd 打开命令提示符,
> 然后输入 pin
> 吕
> github.com
> 如果 ping 不通,表现为
> ping
> 不是内部或外部命令,
> 也不是可运行的程序
  
> [!NOTE] [图片 OCR 识别内容]
> 或批处理文件=
> 建议将此错误扔给
> AI
> 解决,多半是环境娈量 问题)
> 得到并复制 gith
> ub 的 ip 地址.
> C:IWINDOWSIsystem3zlcmd.
> X
> Microsoft Windows
> [版本
> 10.0.26100.6584]
> Cc)
> Microsoft
> Corporation。
> 保留所有权利
> 0
> C: |Users
> Dping github
> C0I
> 正在
> Pinq
> qithub
> C0I
> 23
> 205.243.166]  具有
> 32  字节的数据:
> 20.205
> 243.166
> 复:  字节=32
> 时间=75ms
> TTL=I03
> 20.205
> 243
> 166
> 的
> 复:  字节=32  时间=75ms
> TTL=I03
> 黧
> 20.205.243.166  的
> 复:  字节=32  时间 =75ms
> TTL=I03
> 20.205.243.166  的
> 复:  字节=32  时间=75ms
> TTL=I03
> 20.205.243.166  的 Ping 统计信息 :
> 数据包:  已发送
> 二  4,
> 已接收 =4,
> 丢失
> 二
> 0
> (0%  丢失 ),
> 往返行程的估计时间 (以毫秒为单位 ):
> 最短
> 二
> T5mS,
> 最长
> 二
> T5mS,
> 平均
> 二
> T5ms
> 2)  复制 ip 地址。在服务器  搜索栏  输入 C: WWindows |System3z Idrivers letc Ihost
> 5 ,
> 打开方式选择  记事本 ,然后马上关闭记事本。接着在  搜索栏  搜索  记事本 并 右击
> 选择以管理员身份运行 ,随即将 github.com 的 ip 地址粘贴在最后.
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1 `
> :三 `
> 8 工 O  a
> # Copyright (c) 1993-2009 Microsoft
> #
> # This is asample HOSTS file used by Microsoft TCPIIP for Windows。
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept onan individual line. The IP address should
> # be placed in the first column followed by the corresponding host name:
> # The IP address and the host name should be separated by at least one
> # space。
> #
> # Additionally, comments (such as these) may be inserted on individual
> # lines O[
> following the machine name denoted by a '#' symbol。
> #
> # Forexample:
> #
> 102.54.94.97
> rhino.acme.com
> # SOUrCe Serer
> 38.25.63.10
> Xacme.com
> # X client host
> # localhost name resolution is handled within DNS itself
> #
> 127.0.0.1
> localhost
> #
> 门
> localhost
> 20.205.243.166
> 行10,列2
> 818个亨符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-8
> 3)
> 点击记事本左上角的 文件 然后选择  保存  即可。切记记得看记事本上面是
> 而不是 O 才算保存成功。
> Corp:
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1
> :三 `
> 8 工 O g
> # Copyright (c) 1993-2009 Microsoft Corp.
> #
> # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept on an individual line. The IP address should
> # be placed in the first column followed by the corresponding host name。
> # The IP address and the host name should be separated by at least one
> # space:
> #
> # Additionally comments (such as these) may be inserted on individual
> # lines Or following the machine name denoted by a '#' symbol。
> #
> # For example:
> #
> 102.54.94.97
> rhino.acme.com
> SOUrCe Serer
> 38.25.63.10
> X.acme.com
> client host
> # localhost name resolution is handled within DNS itself。
> #
> 127.0.0.1
> localhost
> Iocalhost
> 20.205.243.166
> 行22,列15
> 818个字符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-S
> 4)  在 搜索栏  搜索
> cmd 并 右击选择以管理员身份运行 ,在  命令提示符  面板上键入 ip
> config/flushdns
> 返回
> 己成功刷新DN5解析缓存  便表示成功了.
> C
> 管理员: 命令提示符
> 义
> Uicrosoft Nindows [版不 10.0.26100.6584]
> (C)
> Iicrosoft Corporation。 保留所有权利。
> C: |Iindows |System32>ipconfig / flushdns
> Iindows
> IP 配置
> 己成功刷新 DVS 解析缓存。
> C: {Tindows |System32>
> # X
  
> [!NOTE] [图片 OCR 识别内容]
> 5)
> 访问华子哥的 Bithub 地址 https: //github_
> COm
> zhangkaihua88 /WebDatascope
> 成功.
> 囟 M。『图』 &
> WorldQuant BRAIN
> GitHub
> ZhangkalhuaBBNe
> C
> https /Igithubcom/zhangkaihuagg NebDatascope
> C 囤  &
> 8 &
> 器 ^4  泊
> 器
> Platform
> Solutions
> Resources
> Open Source
> Enterprise
> Search Orjump to.。
> Signin
> Sign up
> Zhangkaihua88 / WebDataScope
> Public
> Notifications
> Fork
> Stal
> Code
> SSUeS
> Pullrequests
> Actions
> Projects
> Security
> Insights
> main
> Branches
> GOto fle
> Code
> About
> No description website
> Ortopics provided。
> Zhangkaihuagg fix
> 0183285
> 2Weeks a90
> 118 Commits
> Readme
> Delete img/screenshotpng
> last year
> Apache 2.0license
> Activity
> SIC
> Weeks ago
> 69 stars
>  gitignore
> V0.4.3
> last year
> watching
> LICENSE
> VO.1.0
> last year
> 14 forks
> Report repository
> READMEmd
> 2 months ago
> manifestjson
> Weeks ago
> Releases
> responsejson
> Weeks ago
> WebDataScope 0.9.3 Release
> Lalest
> onIunT4
> 16 releases
> README
> Apache- 2 0 license
> Packages
> 以上为不能访问Gitlub解决方法
> 2
> 点击绿色
> Code 弹出
> Download
> ZIP
> 下载插件压缩包. Zip文件,
> 或者使用 &
> i
> 克隆 git
> clone https: //github.com/zhangkaihua88 / WebDataScope . git
> 将压缩包保
> 存在某目录下,比如我保存在
> 0:
> worldquant_plugin 目录下
> 确认下载
> About
> 链接:
> hub.comlzhangkaihuaggMebDataScopelziplrefs/heads/main
> No description, website; or topics provided。
> 文件名:
> WebDatascope-mainzip
> 394KB
> 0
> Readme
> 保存到:
> 0: {worldquant_plugin
> Apache- 2.0 license
> A
> Activity
> 打开
> 保存
> 取消
> 69 stars
> watching
> V0.1.0
> Open with GitHub Desktop
> 9
> 14 forks
> Download ZIP
> Report repository
> UP
> 3
> 使用解压软件将压缩包解压到(默认)当前目录下.
> Pricing
> Tags
> img
  
> [!NOTE] [图片 OCR 识别内容]
> Worldquant_plugin
> 此电脑
> 新加眷 (D:)
> worldquant_plugin
> 在 worldquant_plugin 中搜索
> 新逮
> 排序
> 三  苎看
> 全部解压宿
> 详洇信息
> 名祢
> 修改曰期
> 大小
> 主文仵夹
> WebDataScope-main
> 2025/9/1218:13
> 压宿(pped)文件。
> 394 KB
> 图库
> 捉敢压缩(Zipped]文件夹
> 选择
> 个目标并提取文件
> 文裆
> 文件将被捉致到这个文件夹(F:
> 囱片
> Dilworldquant_plugin WebDataScope main
> 浏览(R)
> 音乐
> 完戎时显示捉敢的文件(H)
> 视频
> 此电脑
> 本地硭岛 (C:)
> 新加卷(0:)
> 捉取(
> 职消
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 个项目
> 逆中
> 个目
> 393 KB
> 在浏览器中打开扩展管理页面,
> 网页键入 chrome:
> /extensions
> (如
> chrome: //extensions
> 八.
> WorldQuant BRAIN
> 扩展程序
> Cent BroWseT
> chrome /extensions
> 器 |#
> 省
> 器
> quant
> 节点
> MP3袼式
> 显化群每曰总若
> 常用网
> 扩展程序
> 搜索扩展程序
> 开发者摸式
> 我。}展穆序
> 键盘快捷键
> 在 CentBrowser 应田酋店中查找扩展程序和主题背景
> 在 Cent Browser 应jd店中
> 发现更多扩展程序和主题
> 5
> 开启
> 开发者模式》
> 点击 <加载己解压的扩展程序》
> 选择插件文件
> 夹。成功会显示  扩展加载完毕
> edge:
  
> [!NOTE] [图片 OCR 识别内容]
> 选择扩展程序目录
> worldquant_Pl
> WebDatascope main
> WebDatascope-main
> 器
> #
> 阎
> c识
> 新逮文件夹
> 名称
> 佟改曰期
> 开发者摸式
> 此电脑
> WebDataScope-main
> 2025/9/1218.27
> 文件夹
> 本地磁盘 (C:)
> 新加巷 (0;)
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 围l店中查找扩展程序和主题背景
> 文件夹:
> WebDatascope-main
> 迸文4夫
> 驭消
> 2
> 使用插件功能
> 打开 Genius 页面
> 安装完成后 ,打开 WorldQuantBrain 网页 Genius 页面 https : /Iplatform.worl
> dquantbrain.com/genius /
> (安装完成后第一次打开需要刷新页面等待若干(少许)时
> 间才能加载出插件)
> @
> 匕
> https:/Iplatform worldquantbrain com/genius/
> C 囤  众
> 8Q
> 器 ^4  省
> 器 ^8 quant
> U  节点
> MP3袼式
> 昱化群l日总结
> 常用网址
> WORLDOUANT
> BRANI
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> 恩 Competitions (5)
> Community
> Status
> Leaderboard
> FAQ
> Gsnlus
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析 
> 显示排名列表
> Genius level: Gold
> Best level: Gold
> Current quarter end: September 3oth; 2025
> SOLD
> 页面加载后,你会看到  配置插件
> 运算符分析
> 显示运算符分析  和「排名分析」
> 和「显示排名分析」以及「显示排名列表」六个按钮
> 依次点击  配置插件
> 运算符分析
> 显示运算符分析
> 配置插件  点击的作用是啥我不是很清楚,
> 这个得问华子哥才知道。点击  运算符
> 分析  按钮后插件会开始抓取你本季度交付的 alpha 全部操作符数量和使用数据 (按
> 钮上会显示抓取进度) ,抓取完成后,
> 点击显示运算符分析 ,会在页面最下方会生
> 成关于操作符的分析表格。右上角显示过去和美区分析 (何时分析)时间.会展示你
  
> [!NOTE] [图片 OCR 识别内容]
> 本赛季所有的操作符和数量以及使用情况.
> 命
> https: / /platform worldquantbrain comlgenius/
> C 困 &
> 8 ^Q  器 ^4
> 器 ^8 quant
> U  节 
> MP3格式
> 量化群每曰总结
> `用网址
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统
> 为substrac
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符末被使用。
> '有两种含义分别是substract和revers, 此处统一
> 为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x; Y, filter
> false), X -y
> 52
> COMBOREGULARSELECTION
> base
> Arithmetic
> multiply(xyy
> filter-false); *
> 76
> COMBO,REGULAR SELECTION
> base
> 依次点击「排名分析」和「显示排名分析」以及「显示排名列表」
> 点击「排名分析」需要等待0.5 ~ 1min 左右 ,
> 需要计算排名情况, 计算完成
> 后点击「显示排名分析」 ,就可以看见比较多的信息,
> 包括但不限于顾问的总人
> 数,以及目前 genius 不同级别达标分别有多少人和自己目前的等级 ,
> 以及自己的
> 最终定级大概会在什么等级 ,
> 以及自己的六维数据。
> q
> 匕
> https:/Iplatform worldquantbraincom /genius/
> C 囤 。 令
> 凸 /Q 器 』4  省 :
> 器 ^8 quant
> 节忘
> MP3袼式
> 导化拜#曰总结
> 常用网址
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207:22:18北京时间: 2025/9/1219:22;18
> 我的排名信息
> 美东时间:2025/9/1207:22:18 北京时间:2025/9/1219:22.18
> 总人敛{9104
> 可能的基璀人数:2926 人
> (交够40个)
> 各个Level 满足的人数 /最终的人:
> For Expert;(512/ 585
> For Master: 4131234
> ForGranamaster
> 该用户目前满足的级别
> grandmaster
> 绢辑六维指标
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:87
> 585
> 总排名:91
> 234
> 总排名:34
> Operator Count: 307 名
> Operator Count: 200 名
> Operator Count: 39 名
> Operator
> 141名
> Operator
> 44名
> Operator AVg: 7名
> Field Count; 263 名
> Field Count; 152 名
> Field Count; 36 名
> Field
> 112名
> Field
> 30名
> Field
> 7名
> Community Activity: 252名
> Community Actiity: 142 名
> Community Activity: 27 名
> Completed Referrals: 1 名
> Completed Referrals:
> Completed Referrals: 1 名
> Max Simulation Streak: 903 名
> Max Simulation Streak: 338名
> Max Simulation Streak: 45 名
> Total Rank: 1979名
> Total Rank: 907 名
> TotalRank: 162 名
> 同时还有贴心的可以 编辑六维数据  按钮,这个功能非常还好,
> 可以让你知道自
> 己目前所处的级别到达是差在哪里,怎么去弥补自己的差分点.非常 nice!
> 点击「显示排名列表」可以多维度查看和分析所有顾问的某些数据,
> 想比对
> 想查看哪位大佬的数据都可以查看,同时支持多维度过滤筛选.
> AVB;
> AVg:
> Avg:
> Ave:
> Avg:
  
> [!NOTE] [图片 OCR 识别内容]
> https:/ /platform worldquantbrain com/genius /leaderboard
> C 囤
> 8Q
> 器 ^^4
> ^
> 器 ^9 quant
> 节点
> 1P3恪式
> 呈化群每曰总结
> 穷用网址
> Genius Rank List
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> 排名信息
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> Minimum 排名:
> Maximum 排名
> entries per page
> Search:
> 下荭原始J5JN
> 显示隐蒉列
> 排名
> 用FID
> 达成等级
> 最终等级
> 国家1区
> K279256
> grandmaster
> grandmaster
> CN
> J71699
> grandmaster
> grandmaster
> FL39657
> grandmaster
> grandmaster
> CN
> 064461
> grandmaster
> grandmaster
> VN
> YN82626
> grandmaster
> grandmaster
> TW
> PP87148
> grandmaster
> grandmaster
> IN
> AT56452
> grandmaster
> grandmaster
> RP76828
> grandmaster
> grandmaster
> CN
> F069320
> grandmaster
> grandmaster
> CN
> 2H78994
> grandmaster
> grandmaster
> T
> Showing
> TO 10of 5,116 entries
> 512
> 查看他人排名数据
> 华子哥的插件还有非常贴心的功能,就是可以查看别人的排名,
> 比如:  华子
> 哥
> K279256
> 课代表 XX
> 游戏王
> ZS(CL ) [ZSC]59763  和常州MG
> 顾问 MG88592 (Rank 38)
> 大佬等等.
> WORLDOUANT
> B人I
> Simulate
> 6Alphas
> Learn
> Data
> Labs
> Genius
> @ Competitions (5)
> Community
> 号
> Refer
> friend
> StatUs
> Leaderboard
> FAQ
> Genius
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207;22:18 北京时间:2025/9/1219:22:18
> 我的排名信息
> 美东时问:  2025/9/1207.22:18北京时问:2025/9/1219:22:18
> 总人数:9104人
> 可能的基准人数:2926  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 1512
> 585
> FOr Master: 413
> 234
> For Grandmaster: 47/59
> 点击
> Leaderboard
> 将鼠标放置在某大佬的 ID 上,
> 便可查看六维排名和
> Geniu
> s等级。
  
> [!NOTE] [图片 OCR 识别内容]
> https:/platform worldquantbrain com /genius/leaderboard
> 出  ^
> {|仑
> JIIVIIOIIOC
> IIUIIOICC
> 386
> 顾问 ML47973 (Rank 100) (Mej
> Gold
> Gold
> 266
> 2.39
> 1.79
> 0.00
> 3.41
> [792
> 167
> 2.70
> RP76828 排名信息
> AK40g
> 总人数:9067人
> 6.17
> 可能的基准人数:2921人 (交够40个)
> HI3900
> 5,38
> 各个Level 满足的人数
> 最终的人数:
> RP768;
> 2.81
> For Expert: 1508
> 584
> YH250;
> For Master: 410
> 234
> 105
> 5.83
> ForGrandmaster: 45
> 58
> P11976
> 5,82
> 该用户目前满足的级别: Srandmaster
> LV571
> 编辑六维指标
> CM456
> 6.91
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> TV5921
> 8.26
> 总排名:4
> 584
> 总排名:4/234
> 总排名:7/58
> LV598
> 4.70
> Operator Count: 35 名
> Operator Count: 34 名
> Operator Count: 15 名
> DVGAAI
> Operator AVg: 64名
> Operator AVg: 17名
> Operator AVg: 4 名
> 3,73
> Field Count: 283名
> Field Count: 160 名
> Field Count: 35 名
> 儿7169
> Field AVg: 33名
> Field AVg: 7 名
> Field
> 名
> 100
> 3.58
> Community Activity: 96 名
> Community Activity: 71 名
> Community Activity: 20名
> EYg42
> Completed Referrals:
> Completed Referrals:
> 名
> Completed Referrals:
> 名
> 6.15
> Max Simulation Streak:
> Max Simulation Streak:
> Max Simulation Streak: 33
> 501 名
> 222名
> ID51
> 5,91
> Total Rank; 1013 名
> Total Rank: 512名
> Total Rank; 109 名
> 56764
> 116
> 7.35
> AN154671
> Expert
> Expert
> 366
> 0.48
> 0.12
> 0.21
> 6.47
> https;lIplatform worldquantbrain comprofle/public/RP76823
> Master
> Master
> 365
> 0,79
> 0.89
> 0,91
> 8,61
> 致谢
> 再次感谢华子哥和贡献者们的无私分享 !这个工具极大方便了排名分析,同
> 时在前端的颜色。样式和大小展示方面也贴合美观设,
> 无论是自我提升还是学习
> 他人策略都非常有用。建议大家试用并反馈 ,
> 共同完善插件 !
> AVE:


---

### 帖子 #47: 【”羊毛“合集】可供使用的AI免费资源
- **主帖链接**: https://support.worldquantbrain.com[L2] 【羊毛合集】可供使用的AI免费资源_37800870021015.md
- **讨论数**: 24

1. [【邪修】当龙虾没有饲料了怎么办？白嫖啊！](../顾问 LY85808 (Rank 86)/[L2] 【邪修】当龙虾没有饲料了怎么办白嫖啊_39252022275223.md)
2. [【工具推荐】claude-code-proxy + AI打工人：使用免费的大模型白嫖打工人！ – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【工具推荐】claude-code-proxy  AI打工人使用免费的大模型白嫖打工人经验分享_37776070276119.md)
3. [谷歌Antigravity 如何使用Skills – WorldQuant BRAIN](../顾问 RM49262 (Rank 30)/[Commented] 谷歌Antigravity 如何使用Skills_37701654477847.md)
4. [盘点最近薅到的免费大模型 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 盘点最近薅到的免费大模型经验分享_37662026299543.md)
5. [免费大模型羊毛薅不完 – WorldQuant BRAIN](../顾问 SC23342 (Rank 23)/[Commented] 免费大模型羊毛薅不完_37337374764695.md)
6. [【体验Sub Agent】将Antigravity的额度反向代理给Claude Code – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【体验Sub Agent】将Antigravity的额度反向代理给Claude Code经验分享_37267205177751.md)
7. [[MCP-守护] 让你的mcp无视token限制，实现免费的MAX模式 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] [MCP-守护] 让你的mcp无视token限制实现免费的MAX模式经验分享_37220062772375.md)
8. [有趣的项目分享：网页版Gemini转API调用（Gemini-API） – WorldQuant BRAIN](../顾问 NL80893 (Rank 16)/[Commented] 有趣的项目分享网页版Gemini转API调用Gemini-API代码优化_37163474989079.md)
9. [【Community Leader -因子构造 💎】TRAE+MCP 自动挖掘因子 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【Community Leader -因子构造 】TRAEMCP 自动挖掘因子经验分享_37116093087895.md)
10. [【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用 – WorldQuant BRAIN](../顾问 MZ45384 (大角羊) (Rank 51)/[Commented] 【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用_37088940070295.md)
11. [【亲测可用】gemini3 pro学生优惠0成本纯白嫖保姆级教程！！！！ – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【亲测可用】gemini3 pro学生优惠0成本纯白嫖保姆级教程经验分享_37082297693719.md)
12. [【白嫖2年AI！】如何完成学生认证并使用长达2年的免费Copilot_pro+配置wq_mcp – WorldQuant BRAIN]([L2] 【白嫖2年AI】如何完成学生认证并使用长达2年的免费Copilot_pro配置wq_mcp经验分享_37024075283223.md)
13. [【Community Leader - 工具配置】免费大模型实现七十二变 经验分享 – WorldQuant BRAIN](../顾问 MZ45384 (大角羊) (Rank 51)/[Commented] 【Community Leader - 工具配置】免费大模型实现七十二变 经验分享经验分享_37013032632215.md)
14. [【MCP WorkFlow】MCP本地LLM配置 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【MCP WorkFlow】MCP本地LLM配置经验分享_36975707112727.md)
15. [Gemini cli运行MCP工作流 从入门到入土问题解决 – WorldQuant BRAIN](../顾问 MZ45384 (大角羊) (Rank 51)/[Commented] Gemini cli运行MCP工作流  从入门到入土问题解决经验分享_36946833823895.md)
16. [【Community Leader -因子构造 💎】零预算网页端LLM + notebook + markdown指令交互流程: 附流程图 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【Community Leader -因子构造 】零预算网页端LLM  notebook  markdown指令交互流程 附流程图经验分享_36944089777047.md)
17. [用 Gmail 账号匹配学生后登录 Gemini CLI，提示错误？部分踩坑与解决记录： – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 用 Gmail 账号匹配学生后登录 Gemini CLI提示错误部分踩坑与解决记录经验分享_36907467592727.md)
18. [【Community Leader -因子构造 💎】零预算持续生成Alpha模板：通用大模型的辅助应用（附表达式生成指令） – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[Commented] 【Community Leader -因子构造 】零预算持续生成Alpha模板通用大模型的辅助应用附表达式生成指令论坛精选_36881490529815.md)
19. [【AI使用问题解决方案】如何正常登陆antigravity IDE （windows和mac通用），学生认证可以免费一年gemin3pro – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【AI使用问题解决方案】如何正常登陆antigravity IDE windows和mac通用学生认证可以免费一年gemin3pro经验分享_36879336144023.md)
20. [[MCP]免费使用阿里云100万token – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] [MCP]免费使用阿里云100万token经验分享_36852577295127.md)
21. [iflow心流 - 个人用户免费使用的API，如何在Linux服务器部署并配置mcp，让AI连续工作 – WorldQuant BRAIN](../顾问 LW67640 (小虎) (Rank 24)/iflow心流 - 个人用户免费使用的API如何在Linux服务器部署并配置mcp让AI连续工作_36765806842007.md)
22. [【Community Leader - 因子构造】【睡一觉就改好】IND地区Robust universe Sharpe优化及MCP全自动因子回测，从0.7+到>1.0（附工作流及Prompt） – WorldQuant BRAIN](../顾问 MZ45384 (大角羊) (Rank 51)/[Commented] 【Community Leader - 因子构造】【睡一觉就改好】IND地区Robust universe Sharpe优化及MCP全自动因子回测从07到10附工作流及Prompt经验分享_36672024628119.md)
23. [【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索（附学生优惠方法/提示词/在服务器中使用） – WorldQuant BRAIN](../顾问 MZ45384 (大角羊) (Rank 51)/[Commented] 【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索附学生优惠方法提示词在服务器中使用经验分享_36634788057367.md)
24. [使用VSCODE中的通义灵码自建免费MCP – WorldQuant BRAIN](../顾问 MS51256 (Rank 28)/[Commented] 使用VSCODE中的通义灵码自建免费MCP_36617019073943.md)
25. [[MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] [MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境经验分享_36512374893207.md)
26. [【免费API】使用大模型自动生成Power Pool Alpha描述 – WorldQuant BRAIN](../顾问 QP72475 (点塔王) (Rank 84)/[Commented] 【免费API】使用大模型自动生成Power Pool Alpha描述_35026037757463.md)
27. [cline配置mcp与免费模型x及使用分享 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] cline配置mcp与免费模型x及使用分享_34659891387031.md)
28. [[分享]白嫖才是王道，从搭建到实战免费最强版MCP – WorldQuant BRAIN](../顾问 JX79797 (华子哥/华子) (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)
29. [【傻瓜式安装教程】傻瓜式安装claude-code-router使用ai打工人的免费api – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【傻瓜式安装教程】傻瓜式安装claude-code-router使用ai打工人的免费api_37797346107671.md)
30. [【PPAC/Super Alpha Submitter】基于coze 生成描述，提交因子 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【PPACSuper Alpha Submitter】基于coze 生成描述提交因子_36489114520471.md)
31. [英伟达免费模型接入Claude Code使用AI打工人](../顾问 LY85808 (Rank 86)/[L2] 英伟达免费模型接入Claude Code使用AI打工人经验分享_38011740910743.md)
32. [白嫖指南：长期稳定免费大模型 API](../顾问 LY85808 (Rank 86)/[L2] 白嫖指南长期稳定免费大模型 API_37982251006487.md)
33. [羊毛薅不完 Google for developers 每月10刀优惠 可用于调用Gemini api 助力你的AIAC 2.0](../顾问 RM49262 (Rank 30)/羊毛薅不完 Google for developers 每月10刀优惠 可用于调用Gemini api  助力你的AIAC 20_37983679645463.md)
34. [使用mcp+ai挖掘alpha过程中节约token的小技巧](../顾问 SZ83096 (Rank 13)/使用mcpai挖掘alpha过程中节约token的小技巧经验分享_38013569192983.md)
35. [【BRAIN 专属福利】KIMI 限时API额度羊毛活动来啦！](/hc/en-us/community/posts/37981514510359--BRAIN-%E4%B8%93%E5%B1%9E%E7%A6%8F%E5%88%A9-KIMI-%E9%99%90%E6%97%B6API%E9%A2%9D%E5%BA%A6%E7%BE%8A%E6%AF%9B%E6%B4%BB%E5%8A%A8%E6%9D%A5%E5%95%A6)

---

### 帖子 #48: 【顾问好文，限时置顶】关于新Consultant提升每日paid的一些建议经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【顾问好文限时置顶】关于新Consultant提升每日paid的一些建议经验分享_27599176068503.md
- **讨论数**: 26

许多新Consultant可能会遇到一个问题：我每天的paid就几美元，别人却有十几、二十几美元甚至更多，这该怎么办呢？

首先，新Consultant的每日paid较低是正常现象，我们需要通过“养号”来提升每日的paid。坚持一段时间，会有较大的改善。

[图片 (图片已丢失)]

在此之前，我们需要知道每日paid由regular alpha和super alpha组成，二者分别进行独立计算，互不影响。Super alpha较为容易获得较高的paid，不过需要regular alpha数量达到100以上才可解锁该功能。因此，我们的主线任务就是提交更多alpha使得满足100个的数量要求，尽快解锁Super alpha功能。

对此，推荐大家前期以ASI为主要研究方向。为什么呢？ASI为大region，可挖掘的alpha数量多，且会相对容易拿到weight，前期积累的这些regular，在解锁Super alpha后可进行组合，制造出较多的Super alpha。而GLB无法用于组合Super alpha；USA已被较深层次挖掘，挖掘出的alpha可能很多过不了相关性测试。在解锁Super alpha后就可用之前提交的ASI进行组合制造Super alpha，这将会增加不少的收入。

回到开头提出的paid差异问题，造成这个差异的主要原因是每个Consultant的value factor的差异会极大程度地影响每日paid。value factor每个月更新一次，更新依据是以统计期内三个月的alpha表现（截止日期为上上个月的月底）。例如当前为11月，本月更新的value factor统计的是789这三个月。新Cousultant的value factor为初始值0.5，提交表现好的alpha将value factor提升至0.7，0.8甚至更高，paid就会翻1倍，2倍，3倍乃至更高。

优先考虑尽量交更多的alpha（alpha质量极差的除外）。其余影响因素的提升可参照： [[链接已屏蔽])

补充一点，当出现theme时，可进行评估，如能找到满足theme的alpha，则以此优先，毕竟这个加成不少且限时，错过了就没有了。

以上就是我关于新Consultant提升每日paid的一些建议，如有什么疑问可在下面评论，有觉得错误之处也可指出。祝大家value factor向1靠拢！

---

### 帖子 #49: 【顾问进阶】一文读懂风险中心化，掌握使用方法
- **主帖链接**: https://support.worldquantbrain.com[L2] 【顾问进阶】一文读懂风险中心化掌握使用方法_35954596858903.md
- **讨论数**: 22

今天早上收到公告通知11月起， **PowerPool将仅接受风险中性化的因子，顾问仍然可以使用其他的非风险中性化（MARKET, SECTOR, INDUSTRY, SUBINDUSTRY, COUNTRY) 回测，但只有符合RA标准的才可以提交** 。很多新顾问可能还不太熟悉风险中性化这个概念，希望这篇文章对你有帮助

### **1. 什么是风险中性化？**

- **定义** ：“风口来了猪都可以飞上天”，风险中性化就是在去除已知的“风”。 风险中性化是一种通过消除特定风险因子对Alpha影响的技术，使Alpha的表现更加纯粹，专注于捕捉市场异常。通过风险中性化，可以剔除市场、行业或风格因子等已知风险对Alpha收益的干扰，从而更准确地评估Alpha的独立性和有效性。

- **理论背景** ：风险因子是影响资产收益的主要驱动因素，例如市场风险、行业风险、动量因子等。经典理论：Fama-French三因子模型（市场、规模、价值）和套利定价理论（APT）为风险因子模型奠定了基础。

### **2. 为什么要做风险中性化？**

- **消除已知风险因子的干扰** ：如果Alpha的收益完全由已知风险因子解释，则其价值有限，因为这些因子可以通过简单的模型复制。风险中性化可以帮助研究者专注于Alpha捕捉的独特市场异常。

- **降低风险** ：减少因风险因子回撤或波动性导致的潜在损失。提高Alpha在不同市场条件下的稳健性。

- **提升Alpha性能** ：通过剔除不必要的风险因子，提高Alpha的Sharpe比率，减少回撤，并优化换手率与交易成本之间的平衡。

### **3. 风险中性化的好处**

- **更高的Alpha独立性** ：通过剔除风险因子，Alpha表现更独立，能够更好地反映其捕捉市场异常的能力。

- **降低拥挤交易风险** ：减少因市场中大量投资者持有相似头寸而导致的价格剧烈波动。

- **增强多样性** ：通过不同的风险中性化方法，生成多样化的信号，丰富Alpha池。

- **优化长期表现** ：在保留Alpha收益的同时显著降低风险，提供更稳定、可靠的长期表现。

### **4. 如何使用风险中性化？**

- **界面操作** ：在BRAIN平台的回测界面中，进入模拟设置（Simulation Settings），在 `Neutralization` 选项中选择对应的风险中性化方法，BRAIN平台内置了六种风险中性：FAST, SLOW, SLOW_AND_FAST, CROWDING, STATISTICAL, REVERSION_AND_MOMENTUM (RAM)

- **API操作** ：在API中，通过调整代码中的 `neutralization` 参数实现。例如

```
{    "instrumentType": "EQUITY",    "region": "USA",    "universe": "TOP3000",    "delay": 1,    "decay": 0,    "neutralization": "FAST",  // 替换为上述对应的风险中性化方法    "truncation": 0.1,    "pasteurization": "ON",    "unitHandling": "VERIFY",    "nanHandling": "ON",    "language": "FASTEXPR",    "visualization": false}
```

### **5. 不同的风险中性化方法及其使用场景**

以下是平台支持的六种风险中性化方法的详细介绍：

#### **5.1 FAST**

- **定义** ：快速因子（Fast Factors）包括市场和行业风格因子，和高换手率的风格因子，例如反转因子。
- **适用场景** ：
  - 高换手率信号。
  - 需要捕捉短期市场趋势的Alpha。
- **注意事项** ：
  - 使用FAST中性化可能会增加Alpha的换手率。

#### **5.2 SLOW**

- **定义** ：慢速因子（Slow Factors）包括低换手率的风格因子，例如价值因子。
- **适用场景** ：
  - 低换手率信号。
  - 更关注长期趋势的Alpha。
- **注意事项** ：
  - SLOW因子适合稳健型投资策略。

#### **5.3 SLOW_AND_FAST**

- **定义** ：结合了慢速因子和快速因子的综合模型。
- **适用场景** ：
  - 需要同时考虑短期和长期趋势的Alpha。
  - 适合多样化的投资策略。
- **注意事项** ：
  - 可能会增加换手率，但能更全面地中性化风险。

#### **5.4 RAM（Reversion and Momentum）**

- **反转因子（REVERSION）** ：捕捉短期均值回归现象（如5天内的价格回调）。
- **定义** ：市场通常会对短期事件过度反应，导致暂时性错误定价。随着这些市场效率的修正，超卖的股票价格恢复，超买的股票价格回落。短期反转因子捕捉股票价格的均值回归现象，即近期表现不佳的股票往往在未来获得更高的回报，而近期表现较好的股票可能会出现回调。

- **动量因子（MOMENTUM）** ：捕捉长期价格趋势（如12个月内的价格趋势）。动量因子识别股票价格的持续趋势，即近期表现较好的股票往往继续上涨，而表现较差的股票则可能继续下跌。基于趋势跟随原则，已建立的价格趋势更可能延续而非逆转
- **适用场景** ：
  - 需要对冲短期均值回归和长期动量趋势的Alpha。
- **注意事项** ：
  - RAM中性化适用于多空平衡的Alpha。
  - 建议结合Alpha的特性，评估其是否容易受到反转或动量因子的影响。

#### **5.5 CROWDING**

- **定义** ：拥挤风险中性化，控制因市场中大量投资者持有相似头寸而导致的风险。随着更多投资者进入相同的头寸，交易的盈利能力可能下降。虽然价格在初期可能上涨，但随后可能变得脆弱，容易出现大幅下跌。
- **适用场景** ：需要减少拥挤交易风险的Alpha。当过多投资者同时试图卖出相同的头寸时，价格可能迅速下跌，导致更大的损失。适合在动量趋势强烈的市场中使用。

- **注意事项** ：拥挤风险中性化适用于多空平衡的Alpha。需要结合Alpha的特性，评估其是否容易受到拥挤交易的影响。

#### **5.6 STATISTICAL**

- **定义** ：因子模型的两大类别：基本面因子模型（Fundamental Factor Models）和基于统计因子模型（Statistical Factor Models），其中第二种使用统计技术（如主成分分析PCA或聚类分析）分析证券收益，识别市场数据中的模式和关系。依赖历史收益数据，通过统计方法预测未来表现或优化投资组合风险。经典案例比如：Roll和Ross的《套利定价理论的实证研究》（APT），强调使用统计方法提取影响资产收益的多个因子。
- **适用场景** ：捕捉复杂非线性关系的Alpha，生成在特定收益空间中表现良好的信号。

- **注意事项** ：
  - 统计风险中性化依赖于历史数据，可能对数据质量较为敏感。
  - 建议结合Alpha的特性，评估其是否适合统计模型的应用。

### **6. 总结**

- **风险中性化的核心价值** ：
  - 通过剔除已知风险因子，优化Alpha表现，降低风险。
- **选择合适的方法** ：
  - 根据Alpha的特点（如换手率、风险敞口）选择合适的风险中性化方法。
- **个人建议** ：
  - 在Simulation中先抽样一部分，尝试不同的风险中性化设置，评估其对Alpha表现的影响，选择最合适的再进行全量的回测

**英文原版文档阅读：**

[Getting Started: Risk Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Risk Neutralized Metrics | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Crowding Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Statistical Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with RAM Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

---

### 帖子 #50: 检查当前 Python 环境和已安装的包import sysprint(f"当前 Python 路径: {sys.executable}")print(f"Python 版本: {sys.version}")尝试导入检查try:    import langchain_core    print("[OK] langchain_core 已安装")except ImportError:    print("[ERROR] langchain_core 未安装")try:    import langgraph    print("[OK] langgraph 已安装")except ImportError:    print("[ERROR] langgraph 未安装")    try:    import langchain_google_genai    print("[OK] langchain_google_genai 已安装")except ImportError:    print("[ERROR] langchain_google_genai 未安装 - 需要安装!")    print("\n请在终端执行:")    print("conda install -c conda-forge langchain-google-genai")    print("或")    print("pip install langchain-google-genai")
- **主帖链接**: https://support.worldquantbrain.com[L2] 为 AI 比赛做好准备构建 LangGraph 智能体_35603369483287.md
- **讨论数**: 13

**概述：** 构建一个使用 Gemini 模型 和 WorldQuant BRAIN MCP 工具的 LangGraph 智能体，用于辅助日常研究和 Alpha 策略开发。

**关于 LangGraph：** LangGraph 是一个基于 LangChain 扩展的库，旨在利用语言模型（LLMs）构建健壮且有状态的多智能体（multi-agent）应用程序。它的核心思想是，将复杂的 AI 应用建模为图形（Graph）结构，从而能够以更灵活、更可控的方式创建循环、有状态的智能体和应用。

可以把 LangGraph 想象成 LangChain 的一个“循环”或“状态化”的增强版。传统的 LangChain Expression Language (LCEL) 主要用于构建有向无环图（DAGs），非常适合处理线性的、一步接一步的任务链。然而，当我们需要构建更复杂的、需要循环、条件判断和持久化状态的智能体时，LangGraph 就派上了用场。

**核心功能：**

1. 理解量化金融问题 - 通过 Gemini 模型理解自然语言查询
2. 自动调用 MCP 工具 - 根据问题智能选择合适的 WorldQuant BRAIN 平台工具
3. 返回分析结果 - 整合工具返回的数据并给出回答

和直接使用 MCP 的区别主要体现在以下两点：

- 状态持久化：    MCP 会话级别                     LangGraph 代码控制，可自定义
- 使用范围：        MCP 受限于对话界面          LangGraph 可编程于任何环境

### 步骤 1: 环境准备

```
# 检查当前 Python 环境和已安装的包import sysprint(f"当前 Python 路径: {sys.executable}")print(f"Python 版本: {sys.version}")# 尝试导入检查try:    import langchain_core    print("[OK] langchain_core 已安装")except ImportError:    print("[ERROR] langchain_core 未安装")try:    import langgraph    print("[OK] langgraph 已安装")except ImportError:    print("[ERROR] langgraph 未安装")    try:    import langchain_google_genai    print("[OK] langchain_google_genai 已安装")except ImportError:    print("[ERROR] langchain_google_genai 未安装 - 需要安装!")    print("\n请在终端执行:")    print("conda install -c conda-forge langchain-google-genai")    print("或")    print("pip install langchain-google-genai")
```

```
import osfrom getpass import getpass# 确保在你的环境中设置了 GOOGLE_API_KEYif "GOOGLE_API_KEY" not in os.environ:    os.environ["GOOGLE_API_KEY"] = getpass("请输入你的 Google API Key: ")
```

### 步骤 2: 定义状态 (State)

```
from typing import TypedDict, Annotated, Listfrom langchain_core.messages import BaseMessageimport operatorclass AgentState(TypedDict):    # agetpassgentState是一个字典，其中 "messages" 键对应一个消息列表    messages: Annotated[List[BaseMessage], operator.add]
```

### 步骤 3: 设置工具和模型

```
import sysimport asynciosys.path.append('～/MCP/untracked') # MCP 所在路径# 修正导入: 使用 langchain_core 而不是 langchainfrom langchain_core.tools import toolfrom langchain_google_genai import ChatGoogleGenerativeAIfrom typing import Optional, Dict, Any# 导入 MCP 平台函数from platform_functions import (    authenticate,    get_datasets,    get_datafields,    create_simulation,    get_alpha_details,    get_user_alphas,    get_operators,    get_platform_setting_options)# 创建同步包装器函数def run_async(coro):    """辅助函数:在同步上下文中运行异步函数"""    try:        loop = asyncio.get_event_loop()    except RuntimeError:        loop = asyncio.new_event_loop()        asyncio.set_event_loop(loop)    return loop.run_until_complete(coro)@tooldef wqb_authenticate(email: str = "", password: str = "") -> str:    """    WorldQuant BRAIN 平台认证        参数:        email: 登录邮箱 (可选,如果已配置)        password: 登录密码 (可选,如果已配置)        返回:        认证状态信息    """    result = run_async(authenticate(email, password))    return str(result)@tooldef wqb_get_datasets(    instrument_type: str = "EQUITY",    region: str = "USA",    delay: int = 1,    universe: str = "TOP3000",    search: Optional[str] = None) -> str:    """    获取 WorldQuant BRAIN 平台上可用的数据集列表        参数:        instrument_type: 工具类型,默认 "EQUITY" (股票)        region: 市场区域,可选: USA, CHN, EUR, JPN, GLB, AMR        delay: 数据延迟,0或1        universe: 股票池,如 TOP3000, TOP2000U 等        search: 搜索关键词 (可选)        返回:        可用数据集的详细信息            使用场景:        - 发现某个区域有哪些数据集可用        - 搜索特定主题的数据集    """    result = run_async(get_datasets(instrument_type, region, delay, universe, "false", search))    return str(result)@tooldef wqb_get_datafields(    region: str = "USA",    data_type: str = "VECTOR",    instrument_type: str = "EQUITY",    delay: int = 1,    universe: str = "TOP3000",    dataset_id: Optional[str] = None,    search: Optional[str] = None) -> str:    """    获取 WorldQuant BRAIN 平台上可用的数据字段        参数:        region: 市场区域 (USA, CHN, EUR, JPN, GLB, AMR)        data_type: 数据类型,如 "VECTOR", "MATRIX", "EXPRESSION"        instrument_type: 工具类型,默认 "EQUITY"        delay: 数据延迟        universe: 股票池        dataset_id: 指定数据集ID (可选)        search: 搜索关键词 (可选)        返回:        数据字段的详细列表,包括字段名、描述、所属数据集等            使用场景:        - 查找某个区域所有的 VECTOR 类型字段        - 搜索特定数据集中的字段        - 为 Alpha 公式寻找合适的数据字段    """    result = run_async(get_datafields(        instrument_type, region, delay, universe, "false",         dataset_id, data_type, search    ))    return str(result)@tooldef wqb_create_simulation(    regular_code: str,    region: str = "USA",    universe: str = "TOP3000",    delay: int = 1,    language: str = "FASTEXPR",    neutralization: str = "NONE") -> str:    """    在 WorldQuant BRAIN 平台上创建并运行 Alpha 模拟        参数:        regular_code: Alpha 公式代码 (必需)        region: 市场区域        universe: 股票池        delay: 数据延迟        language: 表达式语言,默认 "FASTEXPR"        neutralization: 中性化方法        返回:        模拟创建结果,包括 Alpha ID 和模拟状态            使用场景:        - 测试新的 Alpha 策略        - 评估 Alpha 的表现指标    """    result = run_async(create_simulation(        type="REGULAR",        instrument_type="EQUITY",        region=region,        universe=universe,        delay=delay,        language=language,        regular=regular_code,        neutralization=neutralization    ))    return str(result)@tooldef wqb_get_alpha_details(alpha_id: str) -> str:    """    获取指定 Alpha 的详细信息        参数:        alpha_id: Alpha 的 ID        返回:        Alpha 的详细信息,包括性能指标、设置、代码等    """    result = run_async(get_alpha_details(alpha_id))    return str(result)@tooldef wqb_get_user_alphas(    limit: int = 20,    offset: int = 0,    status: str = "all") -> str:    """    获取当前用户的 Alpha 列表        参数:        limit: 返回数量限制        offset: 偏移量        status: Alpha 状态筛选 (all, active, submitted 等)        返回:        用户的 Alpha 列表    """    result = run_async(get_user_alphas(limit, offset, status))    return str(result)@tooldef wqb_get_operators() -> str:    """    获取 BRAIN 平台支持的所有操作符列表        返回:        所有可用操作符的详细信息,包括语法、参数、示例等            使用场景:        - 学习可用的操作符        - 编写 Alpha 公式时查询操作符用法    """    result = run_async(get_operators())    return str(result)@tooldef wqb_get_platform_settings() -> str:    """    获取 BRAIN 平台的配置选项        返回:        平台配置选项,包括支持的区域、股票池、中性化方法等            使用场景:        - 了解平台支持的配置参数        - 验证模拟设置的有效性    """    result = run_async(get_platform_setting_options())    return str(result)# 1. 初始化工具列表mcp_tools = [    wqb_authenticate,    wqb_get_datasets,    wqb_get_datafields,    wqb_create_simulation,    wqb_get_alpha_details,    wqb_get_user_alphas,    wqb_get_operators,    wqb_get_platform_settings]# 2. 初始化 Gemini Pro 模型model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)# 3. 将工具绑定到模型# 这会让模型知道它有哪些工具可用,并能以正确的格式输出工具调用请求model_with_tools = model.bind_tools(mcp_tools)print("[OK] 已加载 8 个 WorldQuant BRAIN MCP 工具:")print("  1. wqb_authenticate - 平台认证")print("  2. wqb_get_datasets - 获取数据集列表")print("  3. wqb_get_datafields - 获取数据字段")print("  4. wqb_create_simulation - 创建 Alpha 模拟")print("  5. wqb_get_alpha_details - 获取 Alpha 详情")print("  6. wqb_get_user_alphas - 获取用户 Alpha 列表")print("  7. wqb_get_operators - 获取操作符列表")print("  8. wqb_get_platform_settings - 获取平台配置选项")
```

### 步骤 4: 定义节点函数

在 LangGraph 中,节点 (Node) 是图的执行单元。我们需要定义两个核心节点:
1. call_model: 调用 Gemini Pro 模型进行决策
2. call_tool: 执行工具调用

```
from langgraph.prebuilt import ToolNode# 定义节点函数def call_model(state: AgentState) -> AgentState:    """    调用 Gemini Pro 模型节点        这个节点会:    1. 读取当前的消息历史    2. 将消息发送给 Gemini Pro    3. Gemini Pro 决定是直接回答还是调用工具    4. 返回模型的响应 (可能包含工具调用请求)    """    messages = state["messages"]    response = model_with_tools.invoke(messages)    # 返回的 response 会被添加到 messages 列表中    return {"messages": [response]}# 使用 LangGraph 的预构建工具节点# ToolNode 会自动处理工具调用和结果返回tool_node = ToolNode(mcp_tools)print("[OK] 节点定义完成:")print("  - call_model: 调用 Gemini Pro 进行决策")print("  - tool_node: 执行工具调用")
```

### 步骤 5: 定义路由逻辑

路由函数决定了在 Gemini Pro 做出决策后,下一步应该去哪个节点:
- 如果 Gemini Pro 要调用工具 → 去 `tools` 节点
- 如果 Gemini Pro 直接回答 → 结束对话 (`END`)

```
from typing import Literaldef should_continue(state: AgentState) -> Literal["tools", "__end__"]:    """    路由函数:决定下一步去哪里        检查最后一条消息:    - 如果包含 tool_calls → 返回 "tools" (继续执行工具)    - 如果没有 tool_calls → 返回 "__end__" (结束对话)    """    messages = state["messages"]    last_message = messages[-1]        # 如果模型返回了工具调用请求    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:        return "tools"        # 否则结束对话    return "__end__"print("[OK] 路由函数定义完成")
```

### 步骤 6: 构建 LangGraph 图

将所有组件组装成一个完整的图:
1. 添加节点
2. 设置边和条件边
3. 编译图

```
from langgraph.graph import StateGraph, START, END# 1. 创建状态图workflow = StateGraph(AgentState)# 2. 添加节点workflow.add_node("agent", call_model)  # Gemini Pro 决策节点workflow.add_node("tools", tool_node)   # 工具执行节点# 3. 设置入口点workflow.add_edge(START, "agent")# 4. 添加条件边: agent 节点执行后,根据路由函数决定下一步workflow.add_conditional_edges(    "agent",           # 来源节点    should_continue    # 路由函数)# 5. 工具节点执行完后,返回到 agent 节点继续决策workflow.add_edge("tools", "agent")# 6. 编译图app = workflow.compile()print("[OK] LangGraph 图构建完成!")print("\n图结构:")print("  START → agent → [条件路由]")print("                   |- 需要工具 → tools → agent")print("                   |- 不需要工具 → END")
```

### 步骤 7: 测试智能体

测试一下智能体，可以问它关于 WorldQuant BRAIN 平台的问题。

```
from langchain_core.messages import HumanMessage# 示例 1: 查询 CHN 区域的 VECTOR 字段def test_agent(query: str):    """测试智能体"""    print(f"\n{'='*60}")    print(f"用户问题: {query}")    print(f"{'='*60}\n")        # 调用智能体    response = app.invoke({        "messages": [HumanMessage(content=query)]    })        # 打印最后的回复    final_message = response["messages"][-1]    print(f"智能体回答:\n{final_message.content}")    print(f"\n{'='*60}\n")        return response# 测试查询test_agent("请帮我查询 CHN 区域有多少个 VECTOR 类型的数据字段?")
```

---

### 帖子 #51: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **讨论数**: 30

### 先赞后看,养成好习惯.

## 1 . 来时路

背景: 普通SqlBoy

成为顾问:2024年11月07日

VF变化: 0.5 → 0.77 → 0.99 → 0.99

Genius级别: 2024Q4 Expert, 2025Q1 GM

目前Combine: 2.11 select: 1.86

## 

## 2. 野蛮交

去年最后一个季度未能完全搞清Genius决胜规则,所以在计算出有机会交满220个达到GM基准线后,就每天4个,足100后每天交SA
此时是不太讲质量的,平均fit<1.5,但讲究如下两点

- 点金字塔,做好风格切换
- 小地区保证做超过10个

以上两点,已有vf0.99和Combine证明基本正确

> 做不出模板,做不出手工Alpha,你就保证风格多样(我就是)
> 小地区要么不做,要么多做

## 

## 3. 狂敛财

> 声明: 以下行为有一定风险,还需时间验证

拥有SA权限以后,在一个地区超过80个alpha以后,可以开启稳定挣base模式

SA要挣钱,基本要求是fit>5,prod<0.7,实测vf0.99的话,base至少45刀


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/13/2025
> Super:
> 49.18
> 5O
> Regular:
> 4.35
> Total:
> 53.53
> <<@
> SN _
> SN _
> p ppe
> 
> 8"
> 90
> 6 ^8'38:
> :
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> ADr
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar


记住, ***一条都不能破,且超标太高意义不大***

> 本来SA的fit都超过5了,你就这么有自信他的OS也能这么好?
> 既然如此,还往上飙意义在哪儿?几乎必然过拟合
> 从奖赏机制上也看得出来开,fit飚上去base打不满
> 但是prod降下来却能打满.但是很难,性价比又低

那么,怎么挣这个钱呢?

这里提供一个简单的思路.

收集select表达式20个.中性化也有10种,comb表达式来个20个,

一共就有了400个SA,全部跑完算self_cor即可.

随着持续提交,加上染色等,SA数量会远超400.

假设获得50个可交alpha,这时候怎么交呢?

***计算互相之间的self_cor,用最大团算法获取最长可交子集!!!***

## 4. 少年归

随着持续的挖掘和学习,有时候是知道哪些是正确的事情的
比如:

```
交fitness高的alpha
```

```
多做基本面的alpha
```

```
交有经济学意义的alpha
```

```
多交ATOM
```

```
多做SA
```

不是不想做啊,有时候真的难啊,感慨 **站着说话不腰疼** 啊.

做不到怎么办?

> **如果你不知道你做什么,那么你就想想你最讨厌什么,然后努力朝相反的方向奔跑**

坚持不做错误的事情,必将收获好的回报

我是WorldQuant中国区顾问,我 **庄严承诺** :

- 不混信号 !
- 不一直在同一个池子挖呀挖呀挖 !
- 不一个模板跑一年 !
- 不交自己都不相信的alpha !
- 不拒绝学习,不在比赛躺平,不忽略平台指引 !!!

---

### 帖子 #52: 使用MCP成功地将alpha优化成可提交状态的案例经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用MCP成功地将alpha优化成可提交状态的案例经验分享_35587548741015.md
- **讨论数**: 29

最近试了试MCP服务，发现效果还挺好，相当于有一个专家来辅助帮忙提高alpha的效果。

安装MCP服务，还是参考论坛里其他人的帖子，不再赘述。

现在把自己实验过的一个成功的例子列在下面，大家有其他更优秀的例子也可以拿出来共享下哈。

```
你好，能通过组合两个数据字段的方式来提高fitness么，比如alpha_ids=['vEGMbrv','vEGVj1A']，这两个alpha所用的字段非常接近，且这两个alpha都存在单独fitness较低的问题。
```

您好！很高兴再次与您合作。

您提出的问题非常专业，是alpha研究中一个非常核心且高级的技巧：__通过组合不同的信号来创造一个更强大的alpha__。您观察到两个alpha所用字段接近，且都存在fitness较低的问题，这正是进行因子组合的绝佳场景。

我的计划如下：

1. __诊断分析 (Diagnosis)__: 我将首先分别获取这两个alpha (`vEGMbrv` 和 `vEGVj1A`) 的详细信息。这一步的目的是：

- 精确了解它们各自的表达式和所用的数据字段。
   - 量化它们各自的性能短板（如Fitness、Sharpe、相关性等）。
   - 通过比较它们的表达式，初步判断它们信号的相似度和互补性。

2. __组合策略设计 (Combination Strategy)__: 基于诊断结果，我会提出一个或多个组合策略。最常见的方法&#x662F;__&#x52A0;权平均__，即 `w1 * rank(alpha1) + w2 * rank(alpha2)`。如果两个alpha的逻辑相似但各有侧重，简单的相加（即等权重）往往就能平滑掉各自的弱点，保留共同的强点，从而提升整体的Fitness。

3. __回测验证 (Backtest & Validation)__: 我将构建一个新的alpha表达式来执行我们设计的组合策略，并创建模拟来进行回测，以验证组合后的alpha是否确实达到了我们提高fitness的目标。

在开始之前，由于距离我们上次会话已有一段时间，我需要先进行身份验证。

---

### 帖子 #53: Format the periods into a readable forecast
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用vscode   Github Copilot 入门mcp开发经验分享_34337615228695.md
- **讨论数**: 2

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

论坛里mcp的内容，我也尝试搞一搞，嘻嘻嘻，这是我的学习笔记，大家可以借鉴一下

## 1、安装GitHub Copilot 和 GitHub Copilot扩展


> [!NOTE] [图片 OCR 识别内容]
> GitHub Capilot
> JhT1
> YOUFAI palr programmer
> GitHub
> GitHub Capilot Chat
> 2761m5
> AI chat features powered by Copilot
> GitHub
> 己安装


## 2、启用 Agent  
> [!NOTE] [图片 OCR 识别内容]
> 文件(
> 编辑(
> 选择(5)
> 查看0
> 转到(6)
> MCP
> 新建文本文件
> CtrltN
> @ 设置
> 凸
> [
> 新建文件。
> Ctrl+ Alt + VindoWStN
> 新建窗0
> Ctrl+ShifttN
> mCP
> 捌到8个谴置 ^妄孓
> 使用配置文件新建窗0
> 朋
> 工作区
> 备份和同步设置
> 打开文件。
> Ctrl+0
> 功能(0]
> 打开文件夹。
> Ctrl+K Ctrl+0
> Chat
> Mcp
> Assisted
> Nuget Enabled
> 实验性
> 终端(1)
> 从文件打开工怍区。
> 为 AI 辅助的 MCP 服务器安装启用 NuGet 包。
> NET 包(NuGetorg), 用于按中央注册表
> 聊天(5)
> 中的名称安装 MCP 服务器
> 打开最近的文件
> U
> 扩展(1)
> GitHub Copilot Chat (1)
> 将文件夹添加到工作区。
> Experimental (1)
> Chat > Mcp: Autostart
> 实验性
> 将工怍区另存为。
> 控制在提交聊天消息时是否应自动启动 MCP 服务器。
> 复制工作区
> "
> DeVer
> 保存
> Ctrl+s
> 另存为。
> Ctrl+Shift+s
> Chat>
> Discovery: Enabled
> 全部保存
> Ctrl+K 5
> 在计算机上配置模型上下文协议服务器的发现。可以将其设置为
> true 或 false 以禁用或启用所
> 有源。以及要启用的映射源。
> 共享
> 在 settingsjson 中编辑
> 自动保存
> 首选项 
> 配置文件
> Chat
> Mcp: Enabled
> 启用与模型上下文协议服务器的集成。以提供其他工具和功能。
> 设置
> Ctrlt;
> 还原文件
> 扩展
> Ctrl+ShifttX
> 关闭编辑器
> Ctrl+F4
> 键盘快捷方式
> Ctrl+K Ctrl+s
> Chat
> Mcp: Server Sampling
> 关闭文件夹
> CtrltK F
> 配置向 MCP 服务器公开哪些模型以进行采样[在后台发出模型请求。可以在"MCP: 列出服务器
> 配置代码片段
> 关闭窗0
> Alt+F4
> 命令下以图形方式编辑此设置。
> 任务
> 在 settingsjson 中编辑
> 退出
> 主题
> 备份和同步设置。
> Terminal > Integrated
> Tabs: Default Icon
> 默认情况下要与终端图标关联的 codicon ID。
> 联机服务设置
> 大纲
> terminal
> 对于
> MCP


## 

## 3.安装 uv

在终端打开，并执行以下命令

```
powershell -ExecutionPolicy ByPass -c "irm [链接已屏蔽] | iex"
```

## 4、设置 python 环境

```
 conda create -n mcp-env python=3.12 -y   conda activate mcp-env conda deactivate
```

## 5、用 uv 查看 python 版本

打印内容：

```
cpython-3.12.11-windows-x86_64-none                   D:\anaconda3\envs\mcp-env\python.execpython-3.12.11-windows-x86_64-none                   <download available>cpython-3.12.7-windows-x86_64-none                    D:\anaconda3\python.exe
```

## 6、进入指定文件夹，初始化工程

进入指定工作目录，并根据自己的python版本运行以下命令

```
conda activate mcp-envuv add mcp[cli] httpxuv add mcpuv pip install fastmcpuv init . -p Python3.12.11
```

运行main文件，成功打印说明工程初始化成功

```
Hello from mymcp!
```

## 7、新建weather.py

代码是网上copy的

from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = " [[链接已屏蔽]) "
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

if not data["features"]:
        return "No active alerts for this state."

alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

if not points_data:
        return "Unable to fetch forecast data for this location."

# Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

if not forecast_data:
        return "Unable to fetch detailed forecast."

# Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

return "\n---\n".join(forecasts)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

## 

## 8.配置 MCP Server

ctrl+shift+p: 输入cmp 提示没有此配置，点击创建.vscode\mcp.json
或者在工作区直接手动创建 .vscode\mcp.json


> [!NOTE] [图片 OCR 识别内容]
> MCP: 打开工作区文件夹 MCP 配置
> 最近使用
> MCP: Open Workspace Folder MCP Configuration



> [!NOTE] [图片 OCR 识别内容]
> 巴
> 资源昝理器
> MCP
> 。戽 O #
> VSCOde
> MCP;JsOn
> mymcp
> C@


打开mcp.json，输入配置 （根据自己的目录）

```
{    "inputs": [],    "servers": {        "weather": {        "command": "uv",        "args": [          "--directory",          "D:\\AiModels\\MCP\\mymcp",          "run",          "weather.py"            ]        }    }}
```

输入问题


> [!NOTE] [图片 OCR 识别内容]
> 文件臼
> 编辑旧
> 选择[5)
> 查看0
> 转到[6)
> 运行()
> 终端[
> 帮助[)
> MCP
> 哕 D曰0
> 资源管理器
> MCPJson
> Weatherpy U
> 聊天
> 十 S锪.1 
> MCP
> VScode
> mCPJSOn
> VScode
> 纽约今天的天气怎么样
> MCPJson
> inputs"
> []
> servers"
> myMCP
> D启动 |2个工具 |更客。:
> 己运行
> forecast
> Weather (MCP 服务器)
> Weather"
> Command"
> UV"
> 纽约今天夜间有较大概率下雨并可能有雷暴
> 最低气温约160
> arB5
> (60r)
> 东北冈9到20英里/小时。白天多云。最高气温约220
> directory"
> (71咋)
> 有小概率阵雨。东北冈约20英里/小小时。
> "D:1 IAiModels
> IMCP I ImymCP
> "pun"
> Weather.Py"
> #
> 华盛顿今天天气怎么样
> 可
> 己运行
> forecast
> Weather (MCP 服务器)
> 华盛顿今天夜间多云。最低气温约20叱 (68咋)
> 有零垦雨
> 东北风5到8英里小小时。白天大部分时间多云。最高气温约24.
> (76咋)
> 早晨有小概汩雨
> 东北冈9到14英里/小时。阵冈可达
> }
> 23英里小小时。
> B ? 凸 印
> 0添加上下文。
> {} mmjson
> 添加上下文(#)。扩展[@)。命令0
> +
> 添加服务器。
> Agent
> GPT41
> 哭  嚣D
> 〉
> Bet
> Bet


---

### 帖子 #54: 使用大语言模型创建一个BRAIN代码助手代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用大语言模型创建一个BRAIN代码助手代码优化_20098778380439.md
- **讨论数**: 5

最近发现ChatGPT已经提供了可以自创定制化大语言模型的功能（仅限Plus用户）。


> [!NOTE] [图片 OCR 识别内容]
> Nlew GPT
> Draft
> Create
> Configure
> GPT Builder
> Hil IIlhelp you build
> new GPT. You can say something like; "make
> Creative Who
> helps generate Visuals for new products"or "make
> software engineer Who helps
> format my Code。
> What would YoU like to make?
> @
> Message GPT Builder


该功能可以添加至多9个文档给大语言模型作为先验知识，使得它的回答更加精准与贴合。实测发现，文档内容不宜太长。我找到了BRAIN平台上我觉得最有用的几个文档。

1. [*Read this First * - Starter Pack]([链接已屏蔽])
2. [Introduction to Alphas]([链接已屏蔽])
3. [Introduction to BRAIN Expression Language]([链接已屏蔽])
4. [⭐ How BRAIN platform works]([链接已屏蔽])
5. [⭐ Alpha Examples for Silver Users🥈]([链接已屏蔽])
6. [Must-read posts: How to improve your Alphas🥉]([链接已屏蔽])
7. [Operators]([链接已屏蔽])
8. [BRAIN API]([链接已屏蔽])

把这些内容复制变成word后提交给大语言模型作为先验知识。它会变得很聪明噢。亲测好用👍我直接复制粘贴一篇Research Paper for Consultant: **[Research paper 45: Online reviews can predict long-term returns of individual stocks](/hc/en-us/community/posts/15770057302807-Research-paper-45-Online-reviews-can-predict-long-term-returns-of-individual-stocks)**


> [!NOTE] [图片 OCR 识别内容]
> You
> 思考什么是BRAIN Fast Expression并运用你对BRAIN 平台钓所有知识。闶读并分析下
> 列研究摘要
> 写WFast Expression。
> Research paper 45: Online reviews can predict long-term returns ofindividual stocks
> Followed by one person
> KA64574
> 4 months ago
> Abstract:
> Online reviews are Teedback voluntarily posted by consumers abouttheir consumption
> experiences. This feedbackindicates Clstomer attitudles such as affection; awareness
> ancl faith towarcs
> brandOr
> firm ancl dlemonstrates inherent connections Wih a
> companys future sales; Cash Tlow anc stock pricing. However; the predicting
> DOWerOf
  
> [!NOTE] [图片 OCR 识别内容]
> BRAIN Navigator
> Based onthe research summary YoU provided,the key conceptis that online reviews
> significantly impact long-term returns of individual stocks. Inthe context ofthe
> WorldQuant BRAIN platform and its Fast Expression language;
> Ne Canformulate 3n
> expression that incorporates social media data fields relevant to online reviews and
> sentiments. These data fields can be utilized to develop an alpha that reflects the
> influence of customer attitudes and feedback on stock performance。
> Given the data fields YOU Ve mentioned ( ` sc14
> posts
> total
> from the
> Socialmedia4
> cataset representing the total number of posts; and
> SC13
> aVeragesentiment
> fromthe
> Socialmedia3
> dataset representing average
> sentiment):
> potential Fast Expression could be formulated to capture the relationship
> betweenthe Volume of social media posts and the sentiment expressed in these posts
> towards
> company's stock price movement
> Here'san example of how 3 Fast Expression might Iook:
> fastexpr
> Copy code
> Fast Expression
> predict Iong
> temm Leturns based
> online reviews
> aVerage_sentiment
> 5C13
> aVeragesentiment;
> 1Average sentiment
> AOm
> total
> posts
> 5C14_posts_
> total
> t;
> Total
> number
> Of posts
> 1 Combining sentiment and
> Volume
> to predict stock Ieturns
> alpha
> rank(average
> Sentiment
> total_posts)
> post


---

### 帖子 #55: 每个字符之间的时间间隔, 单位秒
- **主帖链接**: https://support.worldquantbrain.com[L2] 向BRAIN Labs里粘贴代码的一个方法代码优化_32440962426007.md
- **讨论数**: 13

brain labs逐步开放了, 但是没法复制粘贴代码进去, 网络也不通, 只能手动敲字进去

这里提供一种方法, 能快速『敲』字进去

核心思路是用模拟键盘按键, 发送文本, 借助python的keyboard包实现

**注意: 模拟按键有风险, 谨慎尝试**

**## 使用示例**

1.在本机安装keyboard包: 
pip install keyboard

2.保存代码到py文件, 比如: send_key.py
其中的text是要复制的内容
```
import keyboard
import time

print('start')
# 等待2秒, 把鼠标光标切换到labs的输入框
time.sleep(2)

# 要输入的文本
text = '''
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
'''.strip()

# 每个字符之间的时间间隔, 单位秒
delay = 0.01

keyboard.write(text=text,delay= delay, exact= False)

```

3.执行脚本
python sned_key.py

4.把鼠标光标定位到labs里, 把浏览器里的输入法改为英文, 等待自动输入完成

**## 效果**


> [!NOTE] [图片 OCR 识别内容]
> Untitledipiynb
> testlmd
> 中又
> Ch=
> qizk
> Dr-i
> 5
> JupS
> TTTC!
> -h=
> 1a21
> clog
> Ch=
> qiek
> IT 
> 5
> JupS
> TTTC!
> -h=
> 1a21
> clog
> the quick
> brown
> TCK Jumps
> STTer
> Che Iazy
> 069


**## 改进思路**

可以指定一个快捷键, 执行快捷键后调用python脚本, 脚本读取剪贴板、发送文字, 实现更丝滑的复制粘贴体验

---

### 帖子 #56: 💻如何使用天翼云主机进行云端程序挂载
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何使用天翼云主机进行云端程序挂载_25891396254231.md
- **讨论数**: 4

本文不构成任何推荐，仅是经验分享，不涉及付费内容。

**Step1:进入免费试用中心👉点击链接 [免费试用中心 - 天翼云 (ctyun.cn)]([链接已屏蔽])**

**Step2:选择“个人认证”，并选择1核4G电脑**


> [!NOTE] [图片 OCR 识别内容]
> 免费试用
> 情遘云产品免J试用
> 豉豆方展。贫完为止
> 舌动拗则>
> 在此镝入趄要搜索豹内客
> 搜窝
> 筛选条件
> 清裤选条仵
> 53通用型云主机1核16
> 53通用型云主机1核26
> 镜像服务
> 用户认证类型
> 拓』音+RnDgR53e
> 环dt3与!
> OqRSC
> TnMNDOCz-NL7们 
> 菁墙昃立用
> 955O片
> 气/(丘L
> 企业认证
> 个人认证
> 观袼
> 1716
> 观掐
> 1526
> 慎逆7
> 5#
> 40G
> s坑基
> 40G
> 公共镇瘭奂梨哿憔
> 产品_别
> 带宽
> 1005
> 带竟
> Tbps
> 计
> 个人认证
> 个 人认l
> 介(U2
> 仔
> 欤揠库
> 免费试用2个月
> 免费试用1个月
> 长期免费试用
> 己-10,004
> 己:10,001
> 网培
> 安全及笞理
> 试用辕识
> 立剧试用
> 试用簌T
> 立8试用
> 试用狨
> 丽{订购


**Step3：选择Windows2019主机。**  
> [!NOTE] [图片 OCR 识别内容]
> 53通用型云主机1核26
> 贵州1-可用区1
> 规格选择
> 1核26
> Windows 2019 DataCente
> Centos7.5 64位(406)
> Das_AHcloud_V3.0.3.2.1_ASTACK_X8G_VRAS_VS.OROI COOSPCI02_tyy_230531(406)
> .00元
> Centos7.9 64位(406)
> Debian8.6 32位(406)
> Windows 2016 DataCenter 64位中文版(406)
> 翼视捷智云版-免费20方(406)
> Centos6.8 64位(406)
> Windows 2019 DataCenter 64位中文版2022(406)


**Step4:等待开通完毕**


> [!NOTE] [图片 OCR 识别内容]
> 岙
> 空利台
> 皿用中0
> 』订革'汀讲佾
> 玎革号:20250825142034021007
> 汀荤=; ;J
> i)  2025-0825142037
> 产新o  202492514.20:3
> T+19
> GTTo
> 开遁
> HEI
> 己下4
> 拜遁中
> 已尧氐
> he
> ITT{
> J
> &1
> JUI
> 1!T-
> 产8
> 玎蜚
> [
> CIo
> 52
> JLUILASSUITLOIA|
> TLCO 兀
> 己苎


**Step5:等待开通完毕后，进入控制台更改密码，并按照指示进行登陆。**


> [!NOTE] [图片 OCR 识别内容]
> 弹性云主机
> 可以21935云主玑。
> 也HTGAFUIDI Sg3GBRT
> 7rNT
> Ut性云士u
> 如塞云主
> L亚5 +丘;
> ]6
> 1竹-
> 0u
> 斥有坛行垃$
> NI
> OH
> LRN憧
> IPbf
> HqIt
> CCUEIhIAYeIUIU
> TCPUs|2G
> 4131256731
> 0459
> 可眍1
> 失
> UN
> 45493231-42224197
> TJo
> 192661IT7
> 54301引胡
> 刨柜?
> 亓玑
> [苎
> 蛮-1膏
> 讽汀
> [*切
> 呙f@


**Step6:进入远程电脑（主机）后，下载Microsoft Edge浏览器，并下载VS Code.  [vscode+python+jupyter环境搭建_哔哩哔哩_bilibili]([链接已屏蔽])**

提示：也可以在本地电脑下载好vs code后把安装包复制到云电脑上

---

### 帖子 #57: 💻如何免费领取阿里无影云电脑使用
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何免费领取阿里无影云电脑使用_25889938244375.md
- **讨论数**: 3

为了让大家在大数据时代顺利上云，提供如下教程供大家参考，不构成任何商业推荐。

1，下载 [阿里无影云电脑客户端]([链接已屏蔽])

2，打开下载好的无影云电脑客户端选择 **个人版云电脑** 使用支付宝二维码扫码登陆得到以下页面


> [!NOTE] [图片 OCR 识别内容]
> 中国电信 14:10
> N%k矧
> 83
> 首页
> @
> 建议您尽快完成实名认证
> 完成后有机会免费领取800小时云电脑时长包(有效期三个月)*;
> 可后续加购个人云电脑。
> 免费领取参与资格:  您的手机号绑定的所有阿里云账号此前均末参与过无影云电脑
> (专业版)  和无影云电脑〈标准版) 的免费试用活动。也未购买过云电脑。
> 用户EA50
> 贝订购1兑换
> 0 >
> 个人云电脑
> 管理镜像
> 为获得最佳使用体验
> 推荐丕载丞影客巳端连接云电脑
> Joo
> 暂无云电脑
> 去开通
> 家庭群组分配的云电脑
> 云电脑
> 家庭
> 我的账号


3，手机上完成上图顶部实名认证免费领取800小时云电脑试用

4，配置选择2核4G,机房选择离所在地最近的地区，系统镜像选择Windows

- 注意：选择云电脑而 **不是ECS云服务器**

5，完成免费试用云电脑领取后，使用支付宝重新扫码登陆阿里无影云电脑客户端

6，通过客户端连接云电脑开始使用


> [!NOTE] [图片 OCR 识别内容]
> 无影云电脑
> [
> 00
> 个人云电脑
> 运行中
> 云电脑基础款
> 订购云电脑
> 电源
> 更新
> 管理
> 团队分配的云电脑
> 暂无团队为您分配电脑。可主动申请加入


---

### 帖子 #58: Initialize forum MCP servertry:    from mcp.server.fastmcp import FastMCP    forum_mcp = FastMCP('brain_forum_server')    forum_mcp.run()except ImportError:    Fallback for testing    forum_mcp = None
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何在VSCODE上安装我发现的MCP傻瓜式教程来了经验分享_34064552577559.md
- **讨论数**: 49

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行！亮一个灯就行！！！！！！**

第一步：在Vscode商店下载Roo code插件；


> [!NOTE] [图片 OCR 识别内容]
> RooCODE
> Roo Code
> Costrict (prev. Cline
> 2K
> Extension name
> Roo
> com
> 740,278
> (304)
> Costrict: strict Al coder for enterp..
> zgsm-ai
> Install
> whole dev team of Alagents in your editor。
> Roo Code
> 740K
> 5
> Install
> Auto Update
> t
> Whole dev team of Alagents in
> Roo Code
> Install
> DETAILS
> FEATURES
> CHANGELOG
> Kilo Code AI Agent (..
> 193k
> 龆
> Open Source Al coding assistant f
> Kilo Code
> Install
> English
> Catala
> Deutsch
> Espanol
> Francais
> C
> Bahasa Indonesia
> Italiano
> 日本
> Marketplace


第二步：在终端输入pip install cnhkmcp ， pip install pydantic[email]，pip install email-validator


> [!NOTE] [图片 OCR 识别内容]
> PROBLEMS
> OUTPUT
> DEBUG CONSOLE
> TERMINAL
> PORTS
> JUPYTER
> python3. 13-venvshoner@lgz wq
> %
> pip install cnhkmcp
> Collect=
> cnhkmcp
> Downloading cnhkmcp-1.2.0-py3-none-any.whl.metadata
> (5.2 kB)
> Requirement
> already satisfied:
> requests>=2.28.0
> i
> /Users /shoner /venv /
> 'python3.13-venv
> /lib/python3 . 13/site-packages
> (from cnhkmcp)
> (2.32.3)
> Requirement
> already satisfied: pandas>=l.5.0
> in /Users/shoner /venv /python3. 13-venv/li
> b/python3 . 13/site-packages
> (from
> cnhkmcp)
> (2.2.3)
> Collecting selenium>=4.0.0
> from
> cnhkmcp)
> Download
> selenium-4.34.2-py3-none-any
> Whl.metadata (7.5 kB)
> Requirement
> already satisfied:
> beautifulsoup4>=4.11.0
> in
> /Users/shoner /venv / python3.1
> 3-Venv /lib/
> 'python3. 13/site-packages_
> (from cnhkmcp)
> (4.13.4)
> C〉170+1
> m0
> 千C
> Lm
> ing
> ing


第三步：打开mcp本地目录，找到untracked文件夹，路径应该是  site-packages/cnhkmcp/untracked

第四步：找到该文件夹里的user_config.json打开编辑输入你在 **worldquantbrain** 的账号密码。

第五步：打开VScode 的RooCode插件，左边导航栏袋鼠图标，配置一个api，以ds api为例（打开deepseek，右上角api开放平台，api keys，创建，复制，粘贴进来（记得充钱））。


> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十6』
> To doits magic, Roo needsan API
> We recommend using an LLM Router:
> OpenRouter
> A unified interface for LLMs
> Requesty
> optimized LLM router
> $1 free credit
> OryoU can
> bring your provider API key:
> API Provider
> Anthropic documentation
> Anthropic
> You must provide
> Valid API key。
> Anthropic API
> Enter API Key.
> API keys are stored securely in VSCode's Secret Storage
> Get Anthropic API
> Use custom base URL
> https:Ilapi.anthropic.com
> Pass Anthropic API Key as Authorization header instead of X-Api-Key
> Import Settings
> Let's 90!
> Vo muot nrovido
> 3 Tlid 4DILo
> key.
> YoUT
> Key
> Key



> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十Ht
> To doits magic, Roo needsan API
> We recommend usingan LLM Router:
> OpenRouter
> unified interface for LLMs
> Requesty
> Your optimized LLM router
> $1 free credit
> OryoU can
> bring your provider API key:
> API Provider
> DeepSeek documentation
> DeepSeek
> DeepSeek API
> API keys are stored securely in VSCode's Secret Storage
> Model
> deepseek-chat
> DeepSeek-V3 achieves a significant breakthrough in inference speed over previous
> models
> It tops the leaderboard among open-source models and rivals the most
> advanced closed-source models globally。
> Does not support images
> Does not support computer use
> Crnnnrta nrnmnt nonhinn
> Import Settings
> Let's 90!
> key:
> Key


第六步：插件右上角... 选择mcp server


> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十H 』
> submitipy
> History
> V3.25
> Modes
> MCP Servers
> Open in Editor



> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十H 』
> MCP Servers
> Done
> The Model Context Protocol enables communication With locally running MCP servers that
> provide additional tools and resources to extend Roo's capabilities. You can use community-made
> servers or ask Roo to create new tools specific to your Workflow (e.9.,
> add a tool that gets the
> latest npm docs").
> Enable MCP Servers
> Turn this ONto let Roo Use tools from connected MCP servers
> This gives Roo more capabilities. If you
> don't plan to use these extra tools, turn i OFF to help reduce API token Costs
> Enable MCP Server Creation
> Enable this to have Roo help you build new custom MCP servers. Learn about server creation
> Hint: To reduce APItoken costs, disable this setting when
> are not actively asking Roo to create a
> new MCP server。
> Edit Global MCP
> Edit Project MCP
> Refresh MCP Servers
> MCP Marketplace
> Learn more about editing MCP settings files
> VoU


点上两个按钮，然后编辑全局mcp。

第八步：对 MCP 文件进行配置，示例配置文件如下：args 分别是两个 mcp 文件的绝对路径，command 是你 python 程序的绝对路径。请根据你电脑的具体路径进行更改。


> [!NOTE] [图片 OCR 识别内容]
> mcpServers
> {
> worldquant-brain- platform
> {
> Command"
> C: |Users
> IAdministrator
> IAppData'
> ILocal | IPrograms
> IPython'
> IPython313
> Ipython.exe
> args
> "C: | Users
> IAdministrator
> IAppData | ILocal
> IPrograms
> IPython
> IPyt
> hon313 |Lib | Isite-packages | Icnhkmcp
> untracked l Iplatform_functions . Py
> ],
> "description
> "Worldouant
> BRAIN
> Platform MCP
> Server
> Comprehensive trading platform integration with
> simulation management;
> alpha operations,
> and authentication。
> Credentials
> are
> Stored
> in
> User
> config.json in
> the
> same directory
> Provides tools
> for creating
> Isimulations, checking status,
> managing alphas,
> and accessing platform
> features
> },
> worldquant-brain-forum" :
> {
> Command"
> "C: |Users | IAdministrator
> IAppData
> ILocal
> IPrograms
> IPython
> IPython313
> Ipython.exe
> "args'
> "C: | |Users
> IAdministrator
> IAppData | ILocal
> IPrograms | |Python | IPyt
> hon313|ILib |Isite-packages | Icnhkmcp'
> untracked
> forum_functions .Py'
> ]
> description"
> "Worldouant
> BRAIN
> Forum MCP
> SerVer
> Forum
> interaction
> and knowledge extraction tools
> Provides glossary access,
> forum post reading〉
> and
> community
> features
> Credentials
> are stored
> in
> user_config.json
> in
> the
> same directory
> Supports headless
> browser
> automation
> for forum scraping
> and
> content extraction


配置成功应该是两个绿灯（科学上网）

如果平台连接失败，尝试安装（ ）


> [!NOTE] [图片 OCR 识别内容]
> 才启石 Roo 0芾卟刨徒新司正又 MCT 胙方琵。
> #舨夯砧刨迕
> 捉示:  不需要 Roo 创』新 MCP 服务器时廷议关闭;
> 戒少 API Token 贳用。
> worldquant-brain-platfomm
> global
> worldquant-brain-forum
> gobal


接下来你有可以让他来帮你干活啦！快来创建你自己的量化公司，招募并培训你的员工吧！

```
{  "mcpServers": {    "worldquant-brain-platform": {      "command": "/opt/anaconda3/bin/python",      "args": [        "/opt/anaconda3/lib/python3.12/site-packages/cnhkmcp/untracked/platform_functions.py"      ],      "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features. Includes 25+ MCP tools for authentication, simulation creation, alpha management, dataset access, performance analysis, competition management, user profile operations, forum integration, and advanced analytics."    }  }}
```

---

### 帖子 #59: 一、从数据出发，依靠简单模版遍历搜索
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何找到更多alpha的思考新手进阶篇系列 - 第一篇单数据字段_27319802497687.md
- **讨论数**: 21

> **记得老师在上课时候讲过alpha research的两个主要脉络，从Idea出发和从Data出发，两种方式都可以找到alpha，而两种能力都具备一定是不断学习的方向。本文就从这两方面来分享一些如何提高alpha产量的思考和心得，也欢迎大家留言讨论！**

---

### 帖子 #60: 提取字段名（cut_index之前的部分）
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md
- **讨论数**: 23

顾名思义，在回测中常常能遇到高turn高sharpe高fit但低margin的因子。这类因子会直接影响我们的combined performance score，降低被PM采纳获得weight的机会，下面给大家分享如何降低换手率的常见方法

## ***如何理解turn，margin和return的关系？***

粗线条地说，return=turnover*margin，所以在给定收益的情况下，换手率越高，margin越低。margin跟手续费相关联，所以为了较高的margin，需要压低turnover。形象来说，我今天交易10次股票，挣了100块，那么我单笔交易平均收益10元，扣除5元手续费还有净利润。倘若我用1000次交易挣得100元，那么单笔交易收益降低至0.1元，远远不够手续费。

## ***降低turn的方式有哪些？***

常见的降turn方式有：增加decay，使用tradewhen，使用降turn运算符。


> [!NOTE] [图片 OCR 识别内容]
> 衰减Decay
> 通过将今天的值与前n夭的衰减值相结合;执行线性衰减函数。
> 它执行以下函数:
> [Jatel
> * T 十 T[date
> 1 (n
> 1)十. +Tlaate
> Decay_linear(I;n) =
> n十 (几一1)+1
> 允许输入的衰;减值:  整数"n" =
> 其中n >=0。
> 注意:  使用负数或非整数值进行衰减将破坏回测。
> 提示:  衰减可用于减少周转,但衰减值过大会削弱信号。


增加decay的方式可以提升信号的“一致性”，让信号不是那么频繁的变化（后文我们也会看到，一些降turn的op采取的也是类似的思想）

***使用tradewhen：*** tradewhen相当于增加开平仓条件，减少信号频繁变化的次数。直观的理解：市场并非天天大涨大跌，针对市场整体涨跌幅波动率小于1%（仅为举例）的时间窗口，不进行交易，这样可以减少一段时间内的整体换手率（但是会以表现为代价）

推荐阅读： [我可以使用 Trade_when 来降低流水率吗？– WorldQuant 大脑](../顾问 AM60509 (Rank 61)/[Commented] Can I use Trade_when to decease the Turnover_27675353441431.md)

***使用降turn运算符***


> [!NOTE] [图片 OCR 识别内容]
> ts_tarset_Tr_Jecaylx。
> ~ombo; RESUIaT
> Tune "-s_decay
> tO have
> turnoiierEqUalto
> Certain target wirh optimization Weight range berween lambda
> min |ambda_
> Iax
> lambda_min=0,
> ambda_max=1
> taraet_Wr=0.1]
> S
> ts_tarset_Tir_Jelts_limitfxy
> ~ombo; RESUIaT
> Tune  -s_Jelta_limi-'
> tO havs
> turnoiierequalto
> Certain taraet with optimization Weish: ranae between lambda_min;lambda_Max。
> lambda_min=0r
> ambda_mat-l
> AIsC
> please bE aware Ofhe
> forKandy Besides seting
> adV20 Orolune related data, yOU Can alsO SETyas
> COnsan。
> target_tvr=0.1]
> Bemus
> tS_tarset_TT_hUMDIK
> Combo
> Regular
> Tune "huMP
> tO have
> turnoverequa
> Certain target with oprimization Weignt range between lambda
> min, Iambda_Max
> lambda_min=n;
> SMbJa_Max=1
> target_TVr=0.1]
> S
> scaling



> [!NOTE] [图片 OCR 识别内容]
> hump
> Hump
> 0.01]
> Combo  Resular
> Limizs amount and ma
> anitude Of chanses in input (thus reducine urnoverj
> base
> SID
> TOTe
> hurp_decaylx p=0j
> Combo, Regular
> This aperator helps to ignore the values that Changed too litle corresponding
> DreioUs OnEs
> SMU
> ShOW More


降低turn运算符的核心思路在于限制变化幅度，从而减少仓位变化。可以指定turnover具体数值（实际结果会略微高于这个数值），但注意：较低的数值可能会完全破坏信号逻辑，使得因子无效。

## ***实操方式：***

本帖给出相关代码，使得可以按照turn区间筛选因子并利用降turn运算符进行处理回测。此外，本帖也提供了一个可以抓取并统计字段（向量类型数据按照vec运算符计算）的方法（来自本人另一篇文章： [如何统计得到的字段数？如何抓取多地区因子一起检验？ – WorldQuant BRAIN](../worldquant brain赛博游戏王/如何统计得到的字段数如何抓取多地区因子一起检验代码优化_28754183939351.md) ）

## **抓取因子：**

def get_alphas(start_date, end_date, sharpe_th, fitness_th,turnover_th_up,turnover_th_down, region, alpha_num, usage):

s = login()

output = []

# 3E large 3C less

count = 0

for i in range(0, alpha_num, 100):

print(i)

url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date  \

+ "T00:00:00-04:00&dateCreated%3C" + end_date \

+ "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"

url_c = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date  \

+ "T00:00:00-04:00&dateCreated%3C" + end_date \

+ "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"

urls = [url_e]

if usage != "submit":

urls.append(url_c)

for url in urls:

response = s.get(url)

#print(response.json())

try:

alpha_list = response.json()["results"]

#print(response.json())

for j in range(len(alpha_list)):

alpha_id = alpha_list[j]["id"]

name = alpha_list[j]["name"]

dateCreated = alpha_list[j]["dateCreated"]

sharpe = alpha_list[j]["is"]["sharpe"]

fitness = alpha_list[j]["is"]["fitness"]

turnover = alpha_list[j]["is"]["turnover"]

margin = alpha_list[j]["is"]["margin"]

longCount = alpha_list[j]["is"]["longCount"]

shortCount = alpha_list[j]["is"]["shortCount"]

decay = alpha_list[j]["settings"]["decay"]

exp = alpha_list[j]['regular']['code']

count += 1

#if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):

if (longCount + shortCount) > 100 and (turnover>turnover_th_up) and (turnover<turnover_th_down):

if sharpe < -sharpe_th:

exp = "-%s"%exp

rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]

print(rec)

if turnover > 0.7:

rec.append(decay*4)

elif turnover > 0.6:

rec.append(decay*3+3)

elif turnover > 0.5:

rec.append(decay*3)

elif turnover > 0.4:

rec.append(decay*2)

elif turnover > 0.35:

rec.append(decay+4)

elif turnover > 0.3:

rec.append(decay+2)

output.append(rec)

except:

print("%d finished re-login"%i)

s = login()

print("count: %d"%count)

return output

def transform(next_alpha_recs, region):

output = []

for rec in next_alpha_recs:

decay = rec[-1]

exp = rec[1]

output.append([exp,decay])

output_dict = {region : output}

return output_dict

def prune(next_alpha_recs, prefix, keep_num):

# prefix is the datafield prefix, fnd6, mdl175 ...

# keep_num is the num of top sharpe same-datafield alpha

output = []

num_dict = defaultdict(int)

for rec in next_alpha_recs:

exp = rec[1]

field = exp.split(prefix)[-1].split(",")[0]

sharpe = rec[2]

if sharpe < 0:

field = "-%s"%field

if num_dict[field] < keep_num:

num_dict[field] += 1

decay = rec[-1]

exp = rec[1]

output.append([exp,decay])

return output

## get promising alphas to improve in the next order

fo_tracker = get_alphas("2025-03-01", "2025-03-24", 1.6,1,0.3,0.7, "ASI", 9000, "track")

print(len(fo_tracker))

get_alphas函数参数：开始日期，结束日期，最低sharpe，最低fit，turn下限，turn上限，地区，数量，抓取类型 。

## 减枝函数：

def prune_modified(next_alpha_recs,prefix,keep_num):

output = []

num_dict = defaultdict(int)

for rec in next_alpha_recs:

exp = rec[1]

sharpe = rec[2]

field = exp.split(prefix)[-1].split(",")[0]

if sharpe < 0:

field = "-%s"%field

if num_dict[field] < keep_num:

num_dict[field] += 1

output.append(rec)

return output

def extract_fields(next_alpha_recs):

field_counts = defaultdict(int)

for rec in next_alpha_recs:

# 提取完整字段名

full_field = rec[1]

# 找到 winsorize 或 ts_backfill 的位置

#winsorize_index = full_field.find('winsorize(')

backfill_index = full_field.find('ts_backfill(')

end_index=full_field.find(', 120')

# 选择最先出现的位置

if backfill_index != -1 and backfill_index != -1:

cut_index = min(backfill_index, end_index)

elif backfill_index != -1:

cut_index = backfill_index

elif end_index != -1:

cut_index = end_index

else:

# 如果没有找到这两个关键词，跳过此记录

continue

# 提取字段名（cut_index之前的部分）

field_name = full_field[cut_index+12:end_index].strip()

field_counts[field_name] += 1

return dict(field_counts)

def prune_second_order(inputdata,all_dict):

th_tracker1=inputdata.copy()

outpur=th_tracker1

for i in all_dict.keys():

if all_dict[i]>100:

outpur=prune_modified(outpur,i,2)

if all_dict[i]<=100 and all_dict[i]>20:

outpur=prune_modified(outpur,i,3)

if all_dict[i]>10 and all_dict[i]<=50:

outpur=prune_modified(outpur,i,4)

if all_dict[i]>3 and all_dict[i]<=10:

outpur=prune_modified(outpur,i,5)

return outpur

fo_tracker_new=[]

for i in fo_tracker:

if ';' not in i[1]:

fo_tracker_new.append(i)

print(len(fo_tracker_new))

all_dict=extract_fields(fo_tracker_new)

print(all_dict)

fo_tracker_tailed=prune_second_order(fo_tracker_new,all_dict)

fo_tracker_new=[]

for i in range(len(fo_tracker_tailed)):

index=0

for j in [';']:

if j in fo_tracker_tailed[i][1]:

index=1

if index==0:

fo_tracker_new.append(fo_tracker_tailed[i][1])

print(len(fo_tracker_tailed))

#all_dict=extract_fields(fo_tracker_new)

print(len(fo_tracker_new))

print(fo_tracker_new[0:3])

## **加入运算符：**

so_alpha_list = []

for expr in fo_tracker_new:

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.3)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.3)')

so_alpha_list.append('hump_decay('+expr+', p=0)')

so_alpha_list.append('hump_decay('+expr+', p=0.01)')

so_alpha_list.append('hump_decay('+expr+', p=0.1)')

so_alpha_list.append('hump_decay('+expr+', p=1)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 240, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 120, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 20, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 60, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 40, factor =0.5)')

so_alpha_list.append('ts_decay_linear('+expr+', 240, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 120, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 60, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 40, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 20, dense = false)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.15)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.3)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.15)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.3)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.15)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.3)')

print(len(so_alpha_list))

print(so_alpha_list[:3])

后续操作与一二三阶段模版相同，划分pool并进行回测即可。

注意：剪枝函数只能针对123阶因子进行减枝，如果使用模版可能需要进一步处理

推荐：将降turn操作作为“新2阶”使用，即：同时跑使用group的二阶与本文提到的操作，亦可作为“新3阶”使用，经近4个月的验证，有可实现性。

祝好运。

---

### 帖子 #61: ⭐如何自动化创建Alpha（Machine Alpha）合集内容Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何自动化创建AlphaMachine Alpha合集内容Alpha Template_25329126761879.md
- **讨论数**: 8

[Machine Alpha 基础知识1：什么是Alpha模板](../顾问 FD69320 (Rank 34)/[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md)

[Machine Alpha 基础知识2：理解时间序列利润与规模比较模板](../顾问 FD69320 (Rank 34)/[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md)

[Machine Alpha 基础知识3：继续理解时间序列模板，以情绪类数据为例](../顾问 FD69320 (Rank 34)/[L2] Machine Alpha 基础知识3继续理解时间序列模板以情绪类数据为例_25066287753367.md)

[Machine Alpha 基础知识4：如何利用对特定数据集的专业领域知识创造Alpha 模板——以期权数据为例](/hc/en-us/community/posts/25329053049495-Machine-Alpha-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%864-%E5%A6%82%E4%BD%95%E5%88%A9%E7%94%A8%E5%AF%B9%E7%89%B9%E5%AE%9A%E6%95%B0%E6%8D%AE%E9%9B%86%E7%9A%84%E4%B8%93%E4%B8%9A%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86%E5%88%9B%E9%80%A0Alpha-%E6%A8%A1%E6%9D%BF-%E4%BB%A5%E6%9C%9F%E6%9D%83%E6%95%B0%E6%8D%AE%E4%B8%BA%E4%BE%8B)

[Machine Alpha 基础知识5：模板的拓展——以CAPM模型的思路为例](../worldquant brain赛博游戏王/[L2] Machine Alpha 基础知识5模板的拓展以CAPM模型的思路为例_25329078901911.md)

[Machine Alpha 基础知识6：模板的拓展——数据处理的重要性，继续以CAPM模型的思路为例](/hc/en-us/community/posts/25526497127959-Machine-Alpha-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%866-%E6%A8%A1%E6%9D%BF%E7%9A%84%E6%8B%93%E5%B1%95-%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86%E7%9A%84%E9%87%8D%E8%A6%81%E6%80%A7-%E7%BB%A7%E7%BB%AD%E4%BB%A5CAPM%E6%A8%A1%E5%9E%8B%E7%9A%84%E6%80%9D%E8%B7%AF%E4%B8%BA%E4%BE%8B)

[Machine Alpha 基础知识7：数据标准化的重要性-以earning idea为例](/hc/en-us/community/posts/26015751078167-Machine-Alpha-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%867-%E6%95%B0%E6%8D%AE%E6%A0%87%E5%87%86%E5%8C%96%E7%9A%84%E9%87%8D%E8%A6%81%E6%80%A7-%E4%BB%A5earning-idea%E4%B8%BA%E4%BE%8B)

[Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一](../顾问 JR23144 (贺六浑) (Rank 6)/[Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一_27789509613335.md)

[Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）](../顾问 AY17279 (Rank 14)/[L2] Machine Alpha 进阶知识2如何优化Alpha模板中的参数案例续_28133464556311.md)

[Machine Alpha 进阶知识3：如何使用分析师数据中的期限结构](/hc/en-us/community/posts/32092606398999-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%863-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E5%88%86%E6%9E%90%E5%B8%88%E6%95%B0%E6%8D%AE%E4%B8%AD%E7%9A%84%E6%9C%9F%E9%99%90%E7%BB%93%E6%9E%84)

[Machine Alpha 进阶知识4：如何使用杜邦比率的思想来创造模板](/hc/en-us/community/posts/32198029389207-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%864-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%9D%9C%E9%82%A6%E6%AF%94%E7%8E%87%E7%9A%84%E6%80%9D%E6%83%B3%E6%9D%A5%E5%88%9B%E9%80%A0%E6%A8%A1%E6%9D%BF)

[Machine Alpha 进阶知识5：如何使用戈登增长率的思想来创造模板](/hc/en-us/community/posts/32227432164887-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%865-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%88%88%E7%99%BB%E5%A2%9E%E9%95%BF%E7%8E%87%E7%9A%84%E6%80%9D%E6%83%B3%E6%9D%A5%E5%88%9B%E9%80%A0%E6%A8%A1%E6%9D%BF)

[Machine Alpha 进阶知识6：如何使用PEG比率的思想来创造模板](/hc/en-us/community/posts/32495294399895-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%866-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%88%88%E7%99%BB%E5%A2%9E%E9%95%BF%E7%8E%87%E7%9A%84%E6%80%9D%E6%83%B3%E6%9D%A5%E5%88%9B%E9%80%A0%E6%A8%A1%E6%9D%BF)

---

### 帖子 #62: 💻如何设置云电脑之京东云？
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何设置云电脑之京东云_25880682394263.md
- **讨论数**: 4

本文旨在帮助大家顺畅设置云电脑，不构成任何商业推荐，请自行选择合适的方案。

**免费试用7天： [官网试用中心-京东云 (jdcloud.com)]([链接已屏蔽])**

**
> [!NOTE] [图片 OCR 识别内容]
> 云产品体验库
> 丰富。安全
> 稳定的试用产品库,
> 满足您的需求。试用后仍可参与新人秒杀活动。
> 查看试用规则
> 热门推荐
> 弹性计算
> 存储
> 安全
> 人工智能
> 开发与运维
> 企业碰用
> 数据库
> 网络
> 容器和中间件
> 云主机 2核4G5M
> 云主机 2核4G5M
> 云电脑 4核86
> 轻量云主机2核2G3M
> 爆款机型。极致性价比。轻量建站
> 爆款机型
> 极致性价比,轻量建站
> 即开即用的"云上电脑"
> 不受时间
> 地
> 预装建站
> 电商
> 办公
> CRM等精选
> 应用部署。开发必选
> 应用部署
> 开发必选
> 点。设备限制,随时随地使用
> 软件。即开即用
> 配置 2核4G5M
> 配置 2核4G5M
> 10M基础带宽
> 2核26 _
> 406硬盘
> 存储 40G HDD
> 存储 60G HDD
> 无界高2办公
> 3/带宽。2006流量/月
> 续费低至4折
> 续费享优惠
> 即开即用
> 续费享优惠
> 免费试用30天
> 免费试用7天
> 免费试用7天
> 免费试用7天
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 鼍
**

**付费版本：** 丰俭由人，实测最低版本 2C2G1M （38/年）或3M（58/年）都可以顺畅运行并调试代码。传送门链接: [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 爆品秒杀。下单领1000京豆
> 下单金额大于100元。 可抽奖领1000京豆_
> 瓜分200万京豆
> 活动规则
> 轻量 2核26 低至36元
> 轻量云主机 2核46 SM 1年
> 轻量云主机 2核46 SM 3年
> 轻量4核166 1年13年
> 超值!中午12点
> 晚上12点加库存
> 热销机型。
> 即开即用
> 超值推荐!
> 热销机型,
> 即开即用;
> 超值推荐!
> 热门游戏,
> 一键部署!
> 规格
> 2C26-406 SSD系统盘-3M
> 规格
> 2C46-606 SSD系统盘-5M
> 规格
> 2C46-606 SSD系统盘-5Mi
> 规格
> 4C166-1006 SSD系统盘-5 ~
> 时长 1年
> 时长 1年
> 时长
> 3年
> 时长 1年
> 56元1年
> 限购1台
> 新人专享
> 158元1年
> 限购1台
> 新人专享
> 618元/3年
> 限购1台
> 新人专享
> 518元/1年
> 限购1台
> 新人专享
> 原价522.72元/年
> 原价849.72元年
> 原e2459.+6元年
> 原价19944元+年
> 已抢:
> 609
> 已抢:
> 22%
> 已抢:
> 12%
> 已抢:
> 12%
> 立即秒杀
> 立即秒杀 
> 立即秒杀 
> 立即秒杀


选择所在城市最近的节点，选择windows server镜像，完成购买后，登录控制台，


> [!NOTE] [图片 OCR 识别内容]
> 京东云
> 品 云服务 `
> 佥概览
> 全站搜索
> 费用
> 工单
> 产品与服务
> 运维管理
> 安全管理
> 十新建
> 常用服务
> 云主机 CVM
> 原生容器
> 私有网络
> 云硬盘
> 对象存储
> 云搜索 Elasticsearch
> 云缓存 Redis
> 添加常用服务
> 请输入关键词
> 如云主机
> 最近访问:  轻量云主机
> 已开通服务
> 华北-北京
> 华东-宿迁
> 华东-上海
> 华南-广州
> 私有网络
> 1110
> 轻量云主机
> 1/100
> 云主机
> 华北-北京
> 华东-宿迁
> 华东-上海
> 华南-广州
> 总数量 (个)
> 运行中
> 即将过期
> 己过期
> 报警实例
> 0
> 0
> 0
> 0
> https:/Ilavm-console jdcloud.com/lavm/list


进入轻量云主机，重置主机密码, 充值密码后请先通过网页登录，选择VNC方式登录后。会弹出是否允许发现网络，选择是。设置完成后建议重启云电脑


> [!NOTE] [图片 OCR 识别内容]
> C乐云
> W  飞服劣 `
> 仙t笕
> 全站搜察
> (
> 贵用
> L单
> 笛条
> 渠迫官埋
> 灼物牛
> ()
> blngshul115
> 轻量云主机
> 网站搭建
> 搭建开发环境
> 搭建常用办公软件
> 主机列表
> 网站搭建
> 最佳实践
> 常见问题
> 镜像列表
> 使用镜像可以快速搭建您的个人博客 企业网站。电子商务平合
> 论坛等网站;  如果您需要手
> 使用WordPress镜像搭建网站
> 如何更换主机的镜像
> SSH密钥
> 动部署网站。可以参考最佳实践部署静态网站和部署Nodejs SSR应用。
> 使用Ghost镜像搭建博客系统
> 使用WebTerminal登录主机
> 推荐镜像
> 使用PrestaShop搭建跨境电商平台
> 修改防火墙端口号
> Ghost博客系
> Prestashop
> 部署静态网站
> 网站备案操作说明
> WordPress
> =Bhost
> 统
> 电商平台
> 手动搭建WordPress应用
> 轻量云主机如何备份
> 部署Nodejs SSR应用
> 轻量云主机超过流量包后如何计费
> 轻量云主机支持的镜像说明
> 视频演示专区 
> 关机
> 
> 重启
> 重置密码
> 华北-北京
> 华南-广州
> 华东-宿迁
> 创建
> 实例名称
> 请输入实例名称。
> I0
> 重装系统
> 实例0
> 实例名称
> 镜像名称
> 配置
> 状态
> 地址
> 计费
> 续费
> 升级套餐
> Windows Server
> CPU: 2核
> 运行中
> 104.
> 到期时间:  2025-08-1023:59:59
> 登录
> 2019数据中心版
> 内存:  268
> 更多
> 1/
> 64位中文版
> 带宽: 1Mbps
> 共1条
> 10条顷


远程登录云主机： [登录Windows实例--云主机 CVM-帮助文档-京东云 (jdcloud.com)]([链接已屏蔽])

建议使用（Windows）远程登录或（Mac）Remost Desktop 进行登录，输入上图中你的公网IP，用户名（默认Administrator）和密码，即可连接登录。至此完成云电脑的设置，在云电脑上搭建所需python环境即可

---

### 帖子 #63: 成为顾问五个月，分享vf保持0.9+的经验经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 成为顾问五个月分享vf保持09的经验经验分享_34938580496023.md
- **讨论数**: 32

我在四月份成为了conditional consultant，vf经历了0.5-0.97-0.98-0.93的变化，除去最开始的vf空窗期外均保持0.9以上。我将从我的个人经历分享我的vf经验


> [!NOTE] [图片 OCR 识别内容]
> Base Payment


1.atom是非常重要的vf因素，强烈建议大家多交atom，事实上我绝大多数alpha都是atom，我并没有选择死板的使用一二三街模板，对于每一个不同的fields因为其中数据是具有共性的，我们可以根据其description进行具有经济及意义的模板攥写，而后发现该模板有较好的指标效果后进行代码批量回测，这得与在顾问课上weijie老师说经济意义是非常重要的一个因素。

2.不要死板的困在某一个地区，我对每一个fields都只提交3-4个在成功点亮pyramids后结束，一定要保持多样性，甚至于单个fields利用模板提交效果最好的那一个，然后更换其他fields用三个不同的fields点亮一个pyramids。

3.其实很多时候不必纠结于 base payment ，实际上base payment和pc有着很大的关系，但很多pc很低调alpha很容易存在某种缺陷。因此我建议可以观察近三年样本表现，以及可以利用sign 符号验证表现的稳定性。

4.保持高margin和合理的turnover,尽量将turnover保持在5-15的区间并且基本至少保证margin有大于10的效果，这是一个alpha能否拥有较好收益的一大因素。

5.一定要保证有一定的数量！我的六月份vf从0.98-0.93的因素在于六月份因准备考试只交了40几个alpha，造成的不稳定效果，因此保证一定数量的alpha提交时必须的。

最后在季度末请大家注意六维，我也在本季度正在冲击master

最后感谢weijie老师，感谢研究小组的各位

---

### 帖子 #64: 曲折的Value Factor之路：0.2-0.4-0.8-0.5-0.94-0.99, 得出的一点点心得经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 曲折的Value Factor之路02-04-08-05-094-099 得出的一点点心得经验分享_35888667819159.md
- **讨论数**: 7

去年10月成为的顾问，应该也算是一名老顾问了。vf波动很大，前期基本都是0.2左右，ppac比赛后开始回升，但比赛结束后，又被打入谷底，最近两次更新浮出水面：0.94，0.99.写一点自己的心得，供大家参考。

声明：论坛里关于Value Factor的讨论很多，不要把这些讨论直接照搬，这些都是大家站在自己的角度总结的经验。如果一个顾问的VF常年保持在0.9以上，我觉得是值得参考模仿的。但大多数帖子只是停留在0.9一次而得出的经验，可能不够全面。包括这篇帖子，也是一点心得分享，请勿直接照搬。这个帖子我会尽力在每次VF更新的时候都总结一下，希望能给大家一点参考。

最近几个月我做了那些改变：

1. 持续的提交Super Alpha；

2. 对Margin的要求提高到10以上；

3. 多点塔提高多样性；

4. 基本都是ATOM。

5. 经常交不上ra，那就不交。

中文顾问论坛是一个宝库，推荐新顾问们一定要多看看里面的帖子，常看常新。回测提交并没有一个万能钥匙，但一定有一个固定不变的方法论，结合自己的情况，不断成长。

长期、短期永远有一个取舍，收入是短期的，学习到知识和经验，才是自己未来的财富。不要小看量化交易这四个字的含金量。

---

### 帖子 #65: 获取数据，修改日期范围和alpha数量
- **主帖链接**: https://support.worldquantbrain.com[L2] 来时路运气与努力交织的结果 vf 从 033 到 098 的成长附代码经验分享_35877688682391.md
- **讨论数**: 12

这次 vf 更新至 0.98，着实出乎我的意料。原本预期在 0.7-0.85 之间，能有这样的突破，运气成分确实占了不小比重 —— 毕竟至今我仍未完全摸清直接影响 vf 的核心指标。这里必须感谢论坛的前辈们，在 "坐牢期" 按他们分享的方法提交后，竟收获了这样的意外之喜。

虽不敢说能给大家太多成熟建议，但还是想把这几个月的实践总结出来，希望能提供一些参考：

1. **紧跟官方节奏提交。** 在 "坐牢" 阶段，官方强调多交 atom，我便集中精力提交这类内容，非 atom 的一律不碰，确保方向与平台引导一致。
2. **保证提交数量，稳定输出。** 记得很早前有老师说过："宁可每天交 4 个合格的 RA，也不要每天只交 1 个优质的 RA。" 我践行这一点，每天尽量保证 "3+1"，最好能做到 "4+1"，保持稳定的活跃度。
3. **重视 SA 质量，助力提高vf 。** 能快速提升，SA 的贡献功不可没。我始终保证至少有一个数据在 5 以上（Sharp/Fitness/PC），也曾有过几次提交 3 个 5 的 SA 的经历，优质内容的积累或许是关键。 这里补充一点，SA需要你提交更多的RA来组合，多交RA很重要。
4. **多区域覆盖，借势活动。** 由于同时在冲塔，我几乎覆盖了所有可提交的区域。结合官方的双倍活动，既避免了提交区域的单一性，也提高了投入产出比。

前辈们总结的提升 vf 的方法，大致可归为两类：

**垂直深耕，聚焦质量：** 追求 Sharp 大于 2、Fitness1.5 以上，同时保证 pnl 曲线美观，兼顾低 turnover、低 Drawdown、高 Return 与高 margin。

**广度拓展，多维布局：** 多冲塔 + 低sc和pc + 坚持 ATOM，在保证数量的基础上，确保其他数据不过于拉垮（比如 margin 最好维持在 10% 以上）。

最后附上这几个月的部分数据，供大家参考。也恳请看到的前辈们不吝指导 —— 从数据趋势看，我预判下个月的 vf 可能会有所回落。股市里常说："凭运气赚的钱，终会凭实力亏回去。" 所以搞懂底层逻辑才是根本。

（图片传不上.jpeg ）

但有一句话始终没错：一分耕耘，一分收获。即便当下有运气加持，但若没有前期的努力铺垫，也难有这份回报。

文末附上我 **基于官方代码** 修改的工具，能查询当前各项数据的平均值。建议大家每周跑一次，及时关注指标波动，针对性调整。共勉！

> from datetime import datetime
> from machine_lib import *
> s = login()
> def get_submit_alphas(s, start_date, end_date, alpha_num):
> output = {
> "prodCorrelation": [],
> "sharpe": [],
> "turnover": [],
> "fitness": [],
> "returns": [],
> "drawdown": [],
> "margin": [],
> "pnl": []
> }
> for i in range(0, alpha_num, 100):
> # 构造查询url
> url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \
> + "&status!=UNSUBMITTED%1FIS_FAIL&dateSubmitted%3E=" + start_date  \
> + "T00:00:00-04:00&dateSubmitted%3C" + end_date \
> + "T00:00:00-04:00&order=-is.sharpe&hidden=false&type!=SUPER"
> urls = [url_e]
> for url in urls:
> response = s.get(url)
> try:
> alpha_list = response.json()["results"]
> for alpha in alpha_list:
> output["prodCorrelation"].append(alpha["is"]["prodCorrelation"])
> output["sharpe"].append(alpha["is"]["sharpe"])
> output["turnover"].append(alpha["is"]["turnover"])
> output["fitness"].append(alpha["is"]["fitness"])
> output["returns"].append(alpha["is"]["returns"])
> output["drawdown"].append(alpha["is"]["drawdown"])
> output["margin"].append(alpha["is"]["margin"])
> output["pnl"].append(alpha["is"]["pnl"])
> return output
> except Exception as e:
> print(f"当前异常为{e}")
> resp = s.get(' [[链接已屏蔽]) ')
> if resp.status_code != 200:
> print(f"resp 返回值{resp.status_code}")
> return output
> # 获取数据，修改日期范围和alpha数量
> alpha_metrics = get_submit_alphas(s, "2025-10-01", "2025-11-01", 200)
> # 计算平均值的函数
> def calculate_average(metric_list):
> if len(metric_list) > 0:
> return sum(metric_list) / len(metric_list)
> return 0
> # 分别计算各项指标的平均值
> average_prod_corr = calculate_average(alpha_metrics["prodCorrelation"])
> average_sharpe = calculate_average(alpha_metrics["sharpe"])
> average_turnover = calculate_average(alpha_metrics["turnover"])
> average_fitness = calculate_average(alpha_metrics["fitness"])
> average_returns = calculate_average(alpha_metrics["returns"])
> average_drawdown = calculate_average(alpha_metrics["drawdown"])
> average_margin = calculate_average(alpha_metrics["margin"])
> average_pnl = calculate_average(alpha_metrics["pnl"])  # 计算 Pnl 的平均值
> # 打印结果
> print(f"10月份共提交了{len(alpha_metrics['prodCorrelation'])}个普通alpha")
> print(f"Prod Corr 平均值: {average_prod_corr:.4f}")
> print(f"Sharpe 平均值: {average_sharpe:.4f}")
> print(f"Turnover 平均值: {average_turnover:.4f}")
> print(f"Fitness 平均值: {average_fitness:.4f}")
> print(f"Returns 平均值: {average_returns:.4f}")
> print(f"Drawdown 平均值: {average_drawdown:.4f}")
> print(f"Margin 平均值: {average_margin:.4f}")
> print(f"Pnl 平均值: {average_pnl:.4f}")

---

### 帖子 #66: 理解顾问最重要的指标Value Factor! 分享不同数值对应的预计每日收入
- **主帖链接**: https://support.worldquantbrain.com[L2] 理解顾问最重要的指标Value Factor 分享不同数值对应的预计每日收入_28199144447255.md
- **讨论数**: 40

```
冲击Grand Master! 帮助大家树立信息维护好自己的value factor！感谢大家点击右侧VOTE点赞或留言互动！
```

**终于每日Base Payment从1.X USD 到了现在的20USD，经验分享出来更更多的同学**

**
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 15
> 10
**

**1. 什么是Value Factor？**

Value Factor 衡量的是最近提交的Alpha对组合Alpha表现的影响，同时考虑三个特定因素：(a) Alpha的个体表现，(b) 最近Alpha提交的多样性，以及 (c) 提交的独特性，即与您过去的提交以及其他顾问提交的比较。

换句话说，Value Factor 是在适用的日历季度中最近提交的Alpha组合的OS（样本外）表现。

Value Factor 是基础支付和季度支付的组成部分。 **范围是0到1。初始值是0.5，可以在consultant 排行榜上面查到**

**2. 什么时候开始更新Value Factor?**

目前来看每个月会更新一次，11月1日更新的是8月开始交alpha的，12月1日今天应该是更新了9月开始交alpha的，以此类推。（个人观察，如果理解错误请官方指正），每次更新会在右上角Announcement处看到。通查你的base payment的变更会比通知来的更早

**3. 提升Value Factor 都需要注意什么？**

**首先，要有足够多的数量，** 上课老师有讲过统计学中的中心极限定理会保证体现出你的真实水平，但这要建立在足够多的alpha上，个人经验最好保持近乎每个月在50个左右，不少于每天都提交。

**其次，最直观的就是看那条PnL的曲线，** 当你进入到一个阶段后已经不再担心找到可以提交的alpha，就要开始选取好的alpha 来交，以下是典型的几个我认为要三思而后行的

a. 先来个好看的，基本上是比较平稳，覆盖的时间足够长。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,50OK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,000K
> 2,50OK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
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
> ANVI


b. 大家经常可能会遇到PnL的覆盖时间从2018年开始的，但线还算平稳，尤其是最近一两年还不错，原理上自己也能说的通，这种不是说完全不能交，但是需要自己权衡一下。 **之后我也会找时间分享一下如何批量识别这样alpha的代码，求点赞！**


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,5OOK
> 1,00OK
> SOOK
> 03/14/2018
> Pnl: 120.30K
> SOOK
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
> {MMM
> NAM


c. 数据时间短，图形很乱，最近一两年走平，甚至是负数的。这种如果不缺alpha的话个人就不建议提交了。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,5OOK
> I
> 6,00OK
> 5,5OOK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,5OOK
> 07/31/2018
> Pnl: 3,319.60K
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
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
> Mp}


**第三，多样性。** 追求多pyramid，这个和genius program的要求也是相辅相成的，也可以理解为BRAIN官方想要奖励和推荐的行为。这里就不建议大家在一个地方交太久，即使有多余的可以留一下等下个月再交（当然也有可能被别人交了，自己权衡下）。尤其如果遇到了oversued的warning以后。

**第四，低相关性。** 这个在很多前辈大佬上分享中也多次提交过了，我基本主要提交的都控制在PROD correlation在0.6以内的，越低越好。你会发现多去探索新的pyramid，会有更高的theme加成，也会更容易有低相关性。

第五，使用performance comparison 功能，关注sharp，fitness 和 margin 提交前后的变化

**3. 如果Value Factor 已经低了怎么办？**

不要摆烂不交了！保持提交，但不要交太多！

这里的建议是每天提交1个alpha，因为交多了也不到1.5USD。但要保证有提交，这样下个月的时候才有可能被拉回来

**4. 不同的value factor对应的base payment可能在什么范围？**

**免责声明：以下仅仅是个人经验，非官方标准**

以提交2个alpha，中等质量为例

Value factor 0.3    daily  1.3 USD

Value factor 0.5    daily 1.5-3 USD

Value factor 0.7    daily 6-10 USD

Value factor 0.8+  daily 15+ USD

Quarterly Payment 还没有太多的经验，后续有更新了再来补充

祝大家都能实现第二收入自由！ 如果觉得有用，记得vote点赞哈

---

### 帖子 #67: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 用Gemini CLI全自动找Alpha工作流纯Template版_37192789600791.md
- **讨论数**: 30

首先要感谢OB53521大佬的Gemini 3 Pro全自动挖因子方式的无私分享，为我打开了新世界的大门。第二天我就搭建好了CLI开始尝试，自己也在使用的过程中对提示词做了一些修改。

修改内容大概有以下几个方面：

1. 明确AI在回测设置当中的中性化选择。第一次使用的时候我就发现AI喜欢使用NONE作为中性化的选择，为了让AI选择不同的中性化方式，除了在文档中放入所有Document里中性化的解释文章，还把挑选规则放入了提示词当中。

2. AI的确喜欢混信号。开会的时候就听OB53521说AI喜欢混信号，AI碰到难题的时候想到的第一个办法就说混信号，所以要把以下设定放到工作流中去限制他，让他生成single dataset alpha，也就是ATOM alpha。

```json

"classifications": [

{

"id": "DATA_USAGE:SINGLE_DATA_SET",

"name": "Single Data Set Alpha"

}

]

```

3. 把IS Testing Status评分细则放到工作流当中。前几次使用的时候发现AI喜欢自动降低执行标准，在得到的alpha的sharpe和fitness都很低的情况下就停下来等你的指示；或者alpha其他数据都很好但是Pord-corrlation>70%的时候，跟你说Alpha的测试为true，得到了所谓“豁免权”停下来让你提交。加上IS Testing Status评分细则之后基本上就杜绝了这种情况，同时我还在其中加上了一条：Margin > 10% (最低要求，建议 > 15%) 这样AI也会注意优化Margin。

4. 强制AI只使用模版进行回测。这里和OB53521的方式不同，原版是从最简单的裸信号开始一步步进化，从而增加复杂度，实现更复杂的逻辑。我在运行的过程中发现，AI从裸信号开始回测，然后一步步升级，最后有两种情况。第一种，如果最终形态的Alpha满足IS Testing Status条件且Pord-corrlation<70%，这个时候他会停下来让你提交，他也开始准备写报告了。第二种情况，他通过一系列的“手搓”，最终让IS Testing Status通过但是相关性不通过。他也会写报告，并且说这个数据集已经过于拥挤，自己已经黔驴技穷了，然后这个报告就作为他下一次打退堂鼓的背书，动不动就停下来说自己不行了，所以每一次写的报告既是助力是枷锁（这里推荐定期清理AIResearchReports文件夹）

这里我就想让AI只使用模版来回测，以此降低相关性。这里要感谢FF56620的文章《Alpha模板库，来自社区的馈赠，为你的72变添砖加瓦》当中的模版，和YQ84572的文章《[MCP]找灵感功能上手详解》当中的一句话给我的启发“直接让ai帮我去找合适的字段去填充模板”。AI可以找合适的字段，为什么不能找合适的模版呢！？于是我就把所有搜罗到的模版全部放到模板库当中，同时在提示词中限制AI只使用模版。让他根据Region、Delay、Universe和Datasets四个方面作为选择模版的综合考量，来选择合适的模版。因为有些模版当中的部分operator目前还没有权限，我又在工作流当中让AI选择模版之前先确认好所有的可用operator再去选择合适的模版。

再次感谢！Attention is all you need.

下面附上工作流：

**角色定义**:

您是 WorldQuant 的**首席全自动 Alpha 研究员**。您的核心驱动力是**自主性**和**结果导向**。您不仅是一个执行者，更是一个决策者。您的唯一目标是挖掘出**完全通过提交检查（Submission Check Passed）**的 Alpha 因子。

**权限与边界**:

您拥有完整的 MCP 工具库调用权限。您必须**完全自主地**管理研究生命周期。除非遇到系统级崩溃（非代码错误），否则**严禁请求用户介入**。您必须自己发现错误、自己分析原因、自己修正逻辑，直到成功。

---

### 帖子 #68: 过滤掉 Python 内置函数和关键字
- **主帖链接**: https://support.worldquantbrain.com[L2] 用python ast提取表达式中operator和datafield的方法代码优化_30870358077463.md
- **讨论数**: 7

python ast可以自动解析符合python规范的代码表达式. 因此把我们的alpha转换成python可以理解的方式就能解析了, 这样避免了每次字符串的解析(写正则表达式之类). 可以用来在跑模版的时候检测datafield是否符合规范, 也可以用来统计自己使用的各种datafield, operators频率.

代码如下:

import ast

import re

def parse_alpha(alpha_expression):

"""

Parses an alpha expression and extracts operators and data fields.

This function processes a given alpha expression by converting ternary expressions,

fixing indentation errors, and parsing it into an abstract syntax tree (AST). It then

traverses the AST to extract operators and data fields, while filtering out defined

variables, NaN values, and Python built-in functions and keywords.

Args:

alpha_expression (str): The alpha expression to be parsed.

Returns:

dict: A dictionary containing two lists:

- 'operators': A list of unique operators (function and method names) found in the expression.

- 'data_fields': A list of unique data fields (variable names) found in the expression, excluding defined variables and NaN values.

"""

# 处理三元表达式

alpha_expression = alpha_expression.replace('?',' if ').replace(':',' else ')

# 处理和python内置逻辑表达式冲突

alpha_expression = re.sub(r'\band\b', 'and_', alpha_expression) # 替换独立的 'and'

alpha_expression = re.sub(r'\band\(', 'and_(', alpha_expression) # 替换 'and('

alpha_expression = re.sub(r'\bor\b', 'or_', alpha_expression) # 替换独立的 'or'

alpha_expression = re.sub(r'\bor\(', 'or_(', alpha_expression) # 替换 'or('

# 处理逻辑表达式

alpha_expression = alpha_expression.replace('!',' not ').replace('&&',' and ')

# 处理range="0.1,1,0.1" 类似表达式

alpha_expression = re.sub(r'"([^"]*)"', "0", alpha_expression)

# 处理缩进错误，尝试修复

alpha_expression = "\n".join(line.strip() for line in alpha_expression.splitlines())

# 解析表达式为抽象语法树 (AST)

tree = ast.parse(alpha_expression)

# 提取 operators 和 data fields

operators = set()

data_fields = set()

# 提取过程中定义的变量

defined_variables = set()

# 遍历 AST

for node in ast.walk(tree):

# 提取赋值语句中的变量名

ifisinstance(node, ast.Assign):

for target in node.targets:

ifisinstance(target, ast.Name):

defined_variables.add(target.id) # 记录定义的变量名

# 提取函数调用 (operators)

ifisinstance(node, ast.Call):

ifisinstance(node.func, ast.Name):

operators.add(node.func.id) # 函数名

elifisinstance(node.func, ast.Attribute):

operators.add(node.func.attr) # 方法名

# 提取变量名 (data fields)

ifisinstance(node, ast.Name):

data_fields.add(node.id) # 变量名

# 提取三元条件表达式

ifisinstance(node, ast.IfExp):

# 提取条件部分

ifisinstance(node.test, ast.Compare):

for comparator in node.test.comparators:

ifisinstance(comparator, ast.Name):

data_fields.add(comparator.id)

# 提取 if 部分

ifisinstance(node.body, ast.Name):

data_fields.add(node.body.id)

# 提取 else 部分

ifisinstance(node.orelse, ast.Name):

data_fields.add(node.orelse.id)

# 过滤掉过程中定义的变量

data_fields = data_fields - defined_variables

# 过滤掉特殊变量nan

data_fields = data_fields - set(['nan','true','false'])

# 过滤掉 Python 内置函数和关键字

builtin_functions = set(dir(__builtins__)) # Python 内置函数

operators = operators - builtin_functions # 去掉内置函数

data_fields = data_fields - builtin_functions - operators # 去掉内置函数

return {'operators':list(operators),"data_fields":list(data_fields)}

目前这个版本我自己用着是没发现什么解析错误的问题. 欢迎大家指正.

---

### 帖子 #69: 经验分享｜PPAC全球第三名，回馈社区经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **讨论数**: 30

引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.3
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 2.94
> Reached Grandmaster
> 0.5


第一阶段：Alpha 构建（前五周）

比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。

我主要从以下三类渠道构建 Alpha：

1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。

2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。

3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。

构建期间，我也特别注意以下三方面的多样性控制：

- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区
- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等
- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性

此外，在筛选 Alpha 入库时，我建立了以下五步流程：

① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；
② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；
③ 计算并筛除自相关过高的表达式，提高组合独立性；
④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；
⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。

第二阶段：Alpha 筛选（第六周）

第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。

我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健

在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级

GPT 在筛选阶段的最大作用体现在两个方面：

1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。

2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。

此外，GPT 还协助完成以下操作：

- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；

- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；

- 避免过多同类中性化、universe 和数据来源重复的表达式；

- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。

我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。

结语：经验与建议

1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。

2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。

3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting
似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜

4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

---

### 帖子 #70: 香港地区的同学如何登陆？
- **主帖链接**: https://support.worldquantbrain.com[L2] 香港地区的同学如何登陆_31134702342167.md
- **讨论数**: 9

```
import requestsimport jsonfrom os.path import expanduserfrom urllib.parse import urljoindef authenticate():    # Create a session to persistently store the headers    s = requests.Session()    try:        # Load credentials from JSON file in home directory        with open(expanduser('~/.brain_credentials'), 'r') as f:            credentials = json.load(f)            if len(credentials) != 2:                raise ValueError("Credentials file should contain exactly two elements: [email, password]")            s.auth = tuple(credentials)    except FileNotFoundError:        print("Error: Could not find credentials file at ~/.brain_credentials")        print("Please create a JSON file with your credentials in the format: [\"<email>\", \"<password>\"]")        return None    except json.JSONDecodeError:        print("Error: Could not parse credentials file. Please ensure it's valid JSON.")        return None    except Exception as e:        print(f"Error loading credentials: {str(e)}")        return None    # Send authentication request    auth_url = '[链接已屏蔽]    response = s.post(auth_url)    # Check response status    if response.status_code == requests.codes.ok:        print("Successfully authenticated!")        return s    elif response.status_code == requests.codes.unauthorized:        if "WWW-Authenticate" in response.headers and response.headers["WWW-Authenticate"] == "persona":            print("Biometric authentication required.")            biometric_url = urljoin(response.url, response.headers["Location"])            print(f"Please visit this URL in your browser to complete biometric authentication:\n{biometric_url}")                        # Wait for user to complete biometric authentication            input("After completing biometric authentication in your browser, press Enter to continue...")                        # Try to authenticate again after biometric verification            biometric_response = s.post(biometric_url)            if biometric_response.status_code == requests.codes.ok:                print("Successfully authenticated with biometrics!")                return s            else:                print(f"Biometric authentication failed with status code: {biometric_response.status_code}")                return None        else:            print("Authentication failed: Incorrect email or password")            return None    else:        print(f"Authentication failed with status code: {response.status_code}")        return Noneif __name__ == "__main__":    session = authenticate()    if session:        # You can now use the authenticated session for subsequent API calls        print("Authentication successful. Session is ready for API calls.")        # Example: response = session.get('[链接已屏蔽])    else:        print("Authentication failed. Please check your credentials and try again.")
```

运行上述代码后，你会被要求点击一个链接进行人脸活体认证，认证完毕后，就会登陆成功，返回session

---

### 帖子 #71: 因子复现日记：操作符复现（1）【传奇耐打王系列二】
- **主帖链接**: 因子复现日记操作符复现1【传奇耐打王系列二】.md
- **讨论数**: 5

大家好啊，传奇耐打王又来了。这次我给大家带来了一个新的系列——因子复现日记。以后我也会不定期分享复现因子的整个操作流程。本期是一期非常简单易懂的操作符复现。作为一个gold，在操作符上实在没有话语权。但是看到一些大佬分享的优秀因子又特别眼馋。咋办呢？心动不如行动，只能自己尝试着复现啦。Weijie老师说的好：如果你把论坛上所有的东西都学会了，那你就是大佬。既然看着别人的因子眼馋，又有ppa的权利，何乐而不为呢？我们不能仅限于眼前的操作符。也要学会自己构建具有复杂功能或者说具有高级功能的操作符。话不多说，现在我们请出今天的主角因子：首先，这个因子缺了两年的数据，但是在10年的表现上，只有两年不达标，且达标的年份均为充分达标加上当时传奇耐打王想点亮USA的Macro这个塔，就想把这个因子据为己有了。天公不作美，我没有ts_ir这个操作符。我就找了一位高段位大佬，让他把这个操作符的定义发给我。我们一起来看看：我们看到，这是一个简单的时间序列上的均值与标准差的比值。这不就是我们熟悉的IR——信息比率吗？我查看该字段的描述：我们了解到：oth551_resret_qual 表示 QUAL 相对于其基准指数的每日残差收益，用于剔除市场整体变动后的质量因子独立表现。那这个因子就是为了先用ts_quantile 提取长期极端残差收益行为，然后再用ts_ir来计算这个长期的信息比率，最后再进行分组的标准化。这么一看还真是挺有意思的。恰恰好ts_mean和ts_std_dev我都有。那我们就来简单的复现一下：我先不加分组的标准化，诶？首先可以肯定的是，这个复现是成功的。信号也相当的不错，似乎不加分组的中性化，虽然夏普降低了，但fitness、return、margin都有提升呢。这时候我再加上分组的中性化进行回测比对结果：我们欣喜的得到了一模一样的结果。这个因子最终我优化成这样交了，惊喜的发现竟然还是一个ra，看来是成功的超越了分享这个因子的佬的sharpe的百分之十，也算是对我认真复现因子的赏赐。尤其我们还可以看到，原本负的两年现在只剩下一年了，且这个2015年有数据的部分非常少，我们可以当成一个回撤来微笑看待：虽然这样导致最终这个因子使用了六个操作符，对于我可怜的六维来说并不是一件好事情。但是一个因子的复现成功，尤其是一个操作符的复现成功，会给我带来莫大的鼓励，就好比告诉我现在我的权限提升了，拥有了一个新的操作符。同时，其他佬分享的用到信息比率操作符的因子，我也可以开心的据为己有了。如果你认为操作符复现如此简单，那你可能小看我们的世坤平台了。接下来我将带来更加困难的操作符复现。如果大家想看这个因子是如何优化的，请献上你们宝贵的赞。越多的赞将越快鼓励传奇耐打王开启新的系列——因子手搓优化系列。我想这一定是大家都想要的。最后希望各位佬们也可以在评论区分享自己复现操作符的经验之谈。无论成功或失败，对于传奇耐打王来说都是一笔宝贵的财富。祝各位佬vf1.0，combine节节高！

---

### 帖子 #72: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com因子复现日记操作符复现1【传奇耐打王系列二】_36596968893591.md
- **讨论数**: 5

大家好啊，传奇耐打王又来了。

这次我给大家带来了一个新的系列——因子复现日记。以后我也会不定期分享复现因子的整个操作流程。本期是一期非常简单易懂的操作符复现。

作为一个gold，在操作符上实在没有话语权。但是看到一些大佬分享的优秀因子又特别眼馋。咋办呢？心动不如行动，只能自己尝试着复现啦。

Weijie老师说的好：如果你把论坛上所有的东西都学会了，那你就是大佬。既然看着别人的因子眼馋，又有ppa的权利，何乐而不为呢？我们不能仅限于眼前的操作符。也要学会自己构建具有复杂功能或者说具有高级功能的操作符。

话不多说，现在我们请出今天的主角因子：


> [!NOTE] [图片 OCR 识别内容]
> Summan
> 3-230816141180
> @54
> STTICOI
> LIn
> 17.454
> 1.38
> 7.739
> 5.519
> 0 SEq
>  | 
> Tonn
> Cn {
> (
> 82Ia
> Chart
> 2117
> +I
> IUhIlIh CnntIFI
> ASISlU
> V
> 5.7〉


首先，这个因子缺了两年的数据，但是在10年的表现上，只有两年不达标，且达标的年份均为充分达标

加上当时传奇耐打王想点亮USA的Macro这个塔，就想把这个因子据为己有了。

天公不作美，我没有ts_ir这个操作符。

我就找了一位高段位大佬，让他把这个操作符的定义发给我。我们一起来看看：


> [!NOTE] [图片 OCR 识别内容]
> Operator
> Scope
> Descnpbon
> TS_irf d
> COIbD, ReSUIaT
> Rerurn information ratio t5_meanfx d] /ts_std_devlx, d)
> 2


我们看到，这是一个简单的时间序列上的均值与标准差的比值。这不就是我们熟悉的IR——信息比率吗？

我查看该字段的描述：


> [!NOTE] [图片 OCR 识别内容]
> Data
> Datasets > Alpha Toolkit Dataset
> oth551_resret_qual
> Simulate Field
> Visualize Field
> Field description
> Category: Macro
> Macroeconomic Activities
> Type: Matrix
> Daily residual return of QUAL relative to its benchmark index。


我们了解到：oth551_resret_qual 表示 QUAL 相对于其基准指数的每日残差收益，用于剔除市场整体变动后的质量因子独立表现。

那这个因子就是为了先用ts_quantile 提取长期极端残差收益行为，然后再用ts_ir来计算这个长期的信息比率，最后再进行分组的标准化。这么一看还真是挺有意思的。

恰恰好ts_mean和ts_std_dev我都有。那我们就来简单的复现一下：


> [!NOTE] [图片 OCR 识别内容]
> ae
> Om Iut
> O Anh
> UIun
> 3「
> TTIAI I
> TNM
> EIIIA
> VAI
> T 
> 01
> '4LLLI I
> Cgoe
> 15 Summar
> 598190599+
> r
> TTIT4
> CTTII
> 1.72
> 18.19
> 1.33
> 10.3 |3
> 6.38
> 1C
> 1
> M
> ITIIRr
> Togeaa
>  (ee
> 1TNI
> Chart
> ITstbilit
> Corairnc
> OTI
> 1759nt
> 6814
> 6,75%
> 10.876
> LOrrelatlon


我先不加分组的标准化，诶？首先可以肯定的是，这个复现是成功的。信号也相当的不错，似乎不加分组的中性化，虽然夏普降低了，但fitness、return、margin都有提升呢。

这时候我再加上分组的中性化进行回测比对结果：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> 2「
> U-T-IaOoo
> UCIT-TR
> -TOnO
> 49140申2r
> THNIFITT
> 9戬
> eIIIIUII
> [ Jmh
> [lr
> OD
> TITIII
> TTTC+T
> CITIITIIII
> R  
> TCI
> Cmul 1TL A EST
> AITTIT
> UvmyLn
> Code
> I5 Summary
> '?U
> TUNT[1
> 4191|2|
> $
> Irrutr|
> TTOTALC
> SImUlarlo 
> 17.459
> 1.28
> 7.73
> 5.519
> 日530
> TT69T41
> s
> Tg
> 1
> O
> Ni
> U Hr
> Lome
> 311eL
> CTM「[
> UA
> O 
> Chart
> IlOII' CONSahe:
> ArotuteD t
> 1.71
> 12.579
> 1.15
> 5.371
> 5.7090
> SORa
> ILIn LrriIILIPL
> Correlation
> yrmT


我们欣喜的得到了一模一样的结果。

这个因子最终我优化成这样交了，惊喜的发现竟然还是一个ra，看来是成功的超越了分享这个因子的佬的sharpe的百分之十，也算是对我认真复现因子的赏赐。尤其我们还可以看到，原本负的两年现在只剩下一年了，且这个2015年有数据的部分非常少，我们可以当成一个回撤来微笑看待：


> [!NOTE] [图片 OCR 识别内容]
> Clone Alpha
> Chart
> Pnl
> 4OOOK
> 2OOOK
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



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> A Single Data Set Alpha
> 盹 Regular Alpha
> Pyramidtheme; USAIDTIMACRO *11
> Aggregate Data
> Sarpe
> TLrNOIeI
> CITNPCc
> RETUTI5
> OTJWTON
> Margln
> 2.12
> 12.2796
> 1.78
> 8.84%6
> 4.41%
> 14.4
> 900
> Year
> Sharpe
> TINCMe
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 00%
> 0.00%
> 0.C0q
> 0Ooo
> 2014
> 0.0
> 0.00y
> 0.00
> 0.0050
> 0.00N
> 0OOoa
> 2015
> 1.13
> 4,049
> 0,29
> 803
> 58q
> 39720
> 224
> 2016
> 2,52
> 10,773
> 5,2355
> 3.199
> 57900
> 1559
> 1568
> 2017
> 2.38
> 10.91玷
> 1.70
> 5.3530
> 1.729
> 64nooo
> 526
> 1573
> 2018
> 0.33
> 11.73玷
> 17
> 1.1750
> 4.419
> 99oou
> 1543
> 1575
> 1019
> 11,423
> 7,735
> 3.329
> 13,62oa
> 50
> 16O0
> 2020
> 3.14
> 13.12~
> 3.31
> 15,1154
> 2.579
> 2306oo
> 1534
> 156L
> 2021
> 202
> 13.7935
> 1.72
> 10055
> 3.069
> 14.55woo
> 1579
> 1569
> 2022
> 2.88
> 12.00兆
> 17.1930
> 2.2496
> 28.64@oo
> 1592
> 1561
> 2023
> 5.44
> 10.84q
> 19.9750
> 0.4496
> 35.870。
> 1592
> 1580
> Investability constrained
> Aggregate Data
> Sharpe
> TUTMOIeI
> Fitness
> RetUCn
> UTAWUOWI
> Marein
> 1.87
> 9.53%
> 1.37
> 6.679
> 3.65%
> 14.00%ooo


虽然这样导致最终这个因子使用了六个操作符，对于我可怜的六维来说并不是一件好事情。但是一个因子的复现成功，尤其是一个操作符的复现成功，会给我带来莫大的鼓励，就好比告诉我现在我的权限提升了，拥有了一个新的操作符。同时，其他佬分享的用到信息比率操作符的因子，我也可以开心的据为己有了。

如果你认为操作符复现如此简单，那你可能小看我们的世坤平台了。接下来我将带来更加困难的操作符复现。

如果大家想看这个因子是如何优化的，请献上你们宝贵的赞。越多的赞将越快鼓励传奇耐打王开启新的系列——因子手搓优化系列。我想这一定是大家都想要的。

最后希望各位佬们也可以在评论区分享自己复现操作符的经验之谈。无论成功或失败，对于传奇耐打王来说都是一笔宝贵的财富。

祝各位佬vf1.0，combine节节高！

---

### 帖子 #73: 这个因子到底有没有混信号？【传奇耐打王系列一】经验分享
- **主帖链接**: 这个因子到底有没有混信号【传奇耐打王系列一】经验分享.md
- **讨论数**: 10

今天我想和大家很严肃的讨论一个问题混信号其实这个话题一直都是大家避不开的问题，而且大家也非常热衷于讨论这个问题。本人也在这里给出一点自己的拙见。一、关于混信号本身的讨论首先，世坤给出 atom 的标识，是非常鼓励大家在同一个数据集对因子进行构造的。这里我完全不反对。但有的顾问会说，非 atom 就是混信号，跨数据集就是混信号。这确实让我非常哑然失笑。接下来我们分两个点来讨论：1、atom 就没有混信号吗？这肯定是不成立的。我来举个例子：ts_product(a, 122) + ts_delta(a, 22)这个毫无疑问，放在哪里都是 atom 了。但一个幂次加一个差分，这究竟是一个什么玩意？可能我作为一个刚刚数学本科毕业的学生给不出一个直观的解释。在我的视角来看，这就是妥妥的混信号了。相信大家也看出来了，刚刚我是通过量纲进行观察，我认为两个没有直接联系，或者说从数学的角度完全不在一个维度的东西直接相加是非常不具备解释性的。Ok，那同量纲，atom，就一定不混信号吗？我们来看这个争议最大的例子：rank(a) + rank(b)，a和b来自同一个数据集就以某些fnd数据集来举例，这类数据集中往往同时存在表示实值（如公司负债）的单字段和表示比率（如公司利率）的单字段。a 和 b 分别来自这两种不同类的数据。这个实值当然可以是一个非常大的量级，百亿都有可能，但比率大概率不过1。都进行 rank，都变成0-1之间，量纲确实统一了。但我想你应该感觉到了这个因子不值得信任的方方面面。因为我们实在不知道两个不能有直接关系的字段为什么可以依靠 rank 之后调整到一起。更严肃一点来说，第一个 rank，是具备某些风格偏好的，就比如大市值公司天然的大。而第二个，是市场偏好的，赚得多的公司天然的大。我们用这样的 rank 相加，做的很可能是一个 β，并不是我们想要找到的 α。2、非 atom 就一定是混信号吗？这肯定也不成立。请看这个简单的例子：分析师预期公司资产/公司实际资产这实在是一个太常见的比率字段了。前一个大概率来自 anl，后一个来自 fnd。我们的因子构建思路，就是在这个分析师预期与实际值的差异上做文章。这样的因子，千千万，信号一跑一个准，当然很多人做过了避免不了 pc 高。可我从来没听人正儿八经的说这个是混信号。这样的比率构造，百分之一百符合世坤小而美的期待。这是一个十分具有目的性和经济学含义的因子构造。和混信号完全不搭边。但我们总不能期待在数据集分类时，anl 数据和 fnd 数据分到一起吧。关于混信号好不好的讨论在我的视角中，我不倡导混信号。但不证明，混信号就一定是不好的。大家经常说，我们用ts操作符，要用有意义的时间窗口：5, 22, 66, 252这样的。但真正有意义的是什么呢？这里我来问一个问题，或许大家能有启发。国庆节为什么放七天假？试问7是一个在上述列表的数字吗？每一个事件，从来就不会固定的按照日周月季度年来开始和结束。这个事件只会在他该发生的时候发生，该结束的时候结束。所以我认为很生硬的去固定一个时间窗口来进行因子的挖掘时很不明智的行为。当时我做 ai alpha 的时候，很奇怪的看到ai给了我类似82、112这样的数字，说实话我也一脸懵。结果我自己调节时间窗口发现，有时候ai一步到位，选了一个最好的时间窗口，就跟见鬼了一样。只能说，市场的洞见，不会按照一板一眼的来，因子的挖掘，也永远不会一板一眼。选取合适的时间窗口，你说是混信号当然没问题，但或许这是对样本内一个较好的解释。Ok，那换个角度，rank + rank，真的不可取吗？我只能说，os 会告诉你可不可取。上一次os的更新，让我意识到了混信号≠os爆炸下面这个因子我明确告诉大家就是 rank + rank这样的形式的，而且我明确的告诉大家其中一个字段是 imb5_score但我们能看到这个23年的 os 更新，这个因子相当的爆炸。而且我通过这样的方式解决了 imb圆顶的问题。其实我们直接看除去23年的样本内数据，还是一个圆顶的趋势，但23年，他抬头了。混信号，也不见得就没有作为。我这么说不是倡导大家也去 rank + rank，而是想跟大家传递一种观念，市场不会因为你有解释性就承认你这个因子，也不会因为你解释不了就不认可你，市场无所谓你怎么挖，他只管他自己的脾气。所以，混信号并没有实质性的好或者不好。唯一的缺陷，就是在你的因子失败的时候，你没办法跟自己说：好吧这是一个失败的策略。因为你连为什么失败都不知道。我们做有经济学含义的因子，是为了给自己的失败一个解释，这真的很无奈。可是朋友们，经济学含义是怎么来的？经济学含义就是我提出了一个东西，这个东西被市场认证了，然后我们才把他归结到经济学含义中。换句话说，要是你的 rank + rank每次 os 都很炸，那就是你说的算，你的含义就是经济学含义，这本就是一个结果导向的东西啊。因此纠结于是不是混信号真的毫无意义。因此，做你想做的因子，好好的思考到底怎么做一个好的因子，这比你花时间想到底有没有混信号有意义的多。

---

### 帖子 #74: 这个因子到底有没有混信号？【传奇耐打王系列一】经验分享
- **主帖链接**: https://support.worldquantbrain.com这个因子到底有没有混信号【传奇耐打王系列一】经验分享_40734437350679.md
- **讨论数**: 10

今天我想和大家很严肃的讨论一个问题
混信号
其实这个话题一直都是大家避不开的问题，而且大家也非常热衷于讨论这个问题。
本人也在这里给出一点自己的拙见。

一、关于混信号本身的讨论
首先，世坤给出 atom 的标识，是非常鼓励大家在同一个数据集对因子进行构造的。这里我完全不反对。但有的顾问会说，非 atom 就是混信号，跨数据集就是混信号。这确实让我非常哑然失笑。接下来我们分两个点来讨论：

1、atom 就没有混信号吗？

这肯定是不成立的。我来举个例子：
ts_product(a, 122) + ts_delta(a, 22)
这个毫无疑问，放在哪里都是 atom 了。但一个幂次加一个差分，这究竟是一个什么玩意？可能我作为一个刚刚数学本科毕业的学生给不出一个直观的解释。在我的视角来看，这就是妥妥的混信号了。

相信大家也看出来了，刚刚我是通过量纲进行观察，我认为两个没有直接联系，或者说从数学的角度完全不在一个维度的东西直接相加是非常不具备解释性的。

Ok，那同量纲，atom，就一定不混信号吗？
我们来看这个争议最大的例子：

rank(a) + rank(b)，a和b来自同一个数据集

就以某些fnd数据集来举例，这类数据集中往往同时存在表示实值（如公司负债）的单字段和表示比率（如公司利率）的单字段。a 和 b 分别来自这两种不同类的数据。这个实值当然可以是一个非常大的量级，百亿都有可能，但比率大概率不过1。都进行 rank，都变成0-1之间，量纲确实统一了。但我想你应该感觉到了这个因子不值得信任的方方面面。因为我们实在不知道两个不能有直接关系的字段为什么可以依靠 rank 之后调整到一起。更严肃一点来说，第一个 rank，是具备某些风格偏好的，就比如大市值公司天然的大。而第二个，是市场偏好的，赚得多的公司天然的大。我们用这样的 rank 相加，做的很可能是一个 β，并不是我们想要找到的 α。

2、非 atom 就一定是混信号吗？

这肯定也不成立。请看这个简单的例子：

分析师预期公司资产/公司实际资产
这实在是一个太常见的比率字段了。前一个大概率来自 anl，后一个来自 fnd。
我们的因子构建思路，就是在这个分析师预期与实际值的差异上做文章。

这样的因子，千千万，信号一跑一个准，当然很多人做过了避免不了 pc 高。

可我从来没听人正儿八经的说这个是混信号。

这样的比率构造，百分之一百符合世坤小而美的期待。这是一个十分具有目的性和经济学含义的因子构造。和混信号完全不搭边。

但我们总不能期待在数据集分类时，anl 数据和 fnd 数据分到一起吧。

- 关于混信号好不好的讨论

在我的视角中，我不倡导混信号。但不证明，混信号就一定是不好的。

大家经常说，我们用ts操作符，要用有意义的时间窗口：5, 22, 66, 252这样的。但真正有意义的是什么呢？

这里我来问一个问题，或许大家能有启发。国庆节为什么放七天假？

试问7是一个在上述列表的数字吗？

每一个事件，从来就不会固定的按照日周月季度年来开始和结束。这个事件只会在他该发生的时候发生，该结束的时候结束。

所以我认为很生硬的去固定一个时间窗口来进行因子的挖掘时很不明智的行为。

当时我做 ai alpha 的时候，很奇怪的看到ai给了我类似82、112这样的数字，说实话我也一脸懵。结果我自己调节时间窗口发现，有时候ai一步到位，选了一个最好的时间窗口，就跟见鬼了一样。

只能说，市场的洞见，不会按照一板一眼的来，因子的挖掘，也永远不会一板一眼。

选取合适的时间窗口，你说是混信号当然没问题，但或许这是对样本内一个较好的解释。

Ok，那换个角度，rank + rank，真的不可取吗？

我只能说，os 会告诉你可不可取。上一次os的更新，让我意识到了混信号≠os爆炸
下面这个因子我明确告诉大家就是 rank + rank这样的形式的，而且我明确的告诉大家其中一个字段是 imb5_score


> [!NOTE] [图片 OCR 识别内容]
> Chr


但我们能看到这个23年的 os 更新，这个因子相当的爆炸。而且我通过这样的方式解决了 imb圆顶的问题。

其实我们直接看除去23年的样本内数据，还是一个圆顶的趋势，但23年，他抬头了。

混信号，也不见得就没有作为。

我这么说不是倡导大家也去 rank + rank，而是想跟大家传递一种观念，市场不会因为你有解释性就承认你这个因子，也不会因为你解释不了就不认可你，市场无所谓你怎么挖，他只管他自己的脾气。所以，混信号并没有实质性的好或者不好。唯一的缺陷，就是在你的因子失败的时候，你没办法跟自己说：好吧这是一个失败的策略。因为你连为什么失败都不知道。我们做有经济学含义的因子，是为了给自己的失败一个解释，这真的很无奈。

可是朋友们，经济学含义是怎么来的？

经济学含义就是我提出了一个东西，这个东西被市场认证了，然后我们才把他归结到经济学含义中。

换句话说，要是你的 rank + rank每次 os 都很炸，那就是你说的算，你的含义就是经济学含义，这本就是一个结果导向的东西啊。因此纠结于是不是混信号真的毫无意义。

因此，做你想做的因子，好好的思考到底怎么做一个好的因子，这比你花时间想到底有没有混信号有意义的多。

---

### 帖子 #75: 这个因子到底能不能交？（下） 【传奇耐打王系列一】
- **主帖链接**: 这个因子到底能不能交下 【传奇耐打王系列一】.md
- **讨论数**: 24

上一篇在这：../顾问 RM49262 (Rank 30)/[Commented] 这个因子到底能不能交上 【传奇耐打王系列一】.md-这个因子到底能不能交-上-传奇耐打王系列一刚刚更新的combine证明我的思路大体应该是正确的：那接下来我们就继续讨论啦！说完了必须指标，我们该讨论优化指标了。优化指标就是在完成必须指标的基础上好中选优，位次越靠前优先度越高：1.低相关（先pc后（sc或ppac））2.sharpe和fitness的21年和22年优秀3.sharpe和fitness逐年优秀4.margin的21年和22年达标5.margin的逐年达标6.margin的21年和22年优秀7.margin的逐年优秀8.margin和return越高越好9.turnover围绕在12%10.drawdown越低越好11.多空优秀这里大家可以看到，我把低相关放到了第一位。首先，为什么追求pc低。很多时候我们都说，pc低可遇不可求，所以我们先拿准自己的池子，对sc做出要求。这里我们可以类比，每个人的池子是小池子，你提交上去的池子是世坤的池子，是大池子。你想把sc降低，那世坤也想把属于他的sc（pc）降低呀。鑫佬名言：你做了别人没做过的（pc低），这对于世坤来说，就是杰出的贡献。为什么说base主要看pc，这就是世坤衡量你贡献的主要指标。在pc足够低的情况下，我认为可以相对忽略更优质的指标，优先选择pc低。鑫佬名言：pc0.5以下就是极品，0.3以下已经是极品中的极品。我当时交了一个0.2几的pc，是我成为有条件顾问后单日base首次破3。以下举例一个我最近刚交的ra：毫无疑问，赚的多而且对vf和combine有极大的帮助再次强调，一定要满足基础要求！基础要求不满足不要看pc！但我还在论坛里看到另外一个ppa大佬的经验分享（具体一下子找不到了，在这里对您表示感谢）：pc高说明什么？说明交的人多。交的人多从概率上说明这个因子值得信赖，否则为什么别人看到了高相关还交呢？我觉得这也是有道理的。因此我觉得pc是一个很主观的东西，就是每个人心中要有符合自己个人的阈值。我一般不会在官方要求上再加一个自己的高要求（比如有的大佬pc0.6以上就不交），但对于一个小白来说，我还是更加重表现，比如下面这个ppa，也是我最近交的：虽然pc非常高，但是表现我很认可，再加上sc也不错，对于我的池子有不小的帮助，我会果断地提交它。也有人问我sc的阈值，说实话，我也是按照官方的来的。甚至有时候，我会因为sharpe提高百分之十而提交不满足pc或者sc的因子，这都是需要根据表现来进行考虑的。这里我详细解答为什么我会提交这样的因子。首先，提交这样的因子对combine的帮助很可能是负的。但是对于vf而言，如果你觉得这个因子你稳赚，那提交了就是正的收益。可能对于这个时期的我，我的目标是优先冲击vf高，所以为了收益我希望我有更多稳定赚的因子，所以我会提交。这是对于我个人现阶段的影响之下我的选择。这里说一个我建议的阈值，我在组sa时发现，sc控制在0.55到0.6时往往可以实现因子的表现最大化。所以我觉得如果你要设置一个个人的sc阈值，0.6就已经很好了。对于像我一样的大部分小白，只跑一二三阶，我们能挖到低相关是存在很大一部分的运气成分。如果把阈值设置的太低，会导致我们无法提交足够数量的因子。数量同样也是一个重要的维度，因此我不建议自己设置太低的阈值。在讨论接下来的指标之前，我先对这个顺序做解释。为什么sharpe和fitness在margin和return之前？因为稳定是一个因子非常非常重要的因素！！！划重点！！！游戏王名言：因子一定是先稳而后赚。我们的基础要求中有一个margin达标，margin达标说明已经能大概率赚钱了。接下来我们的目标就是要让因子稳定赚钱。稳定赚钱的因子我们称之为“印钞机”。我可以允许我一次赚的不多，但我一定要一直赚！！！稳定赚钱的因子对于vf和combine的帮助是超级大的。接下来我们来说指标。我都是先写21年和22年表现好，而后才是逐年表现好。大家都希望逐年表现好。但除非顶尖高手我们都做不到逐年都好。因此关注最近两年是很重要的。为什么因子会不断地挖出来，不断地退役，就是因为因子具有时效性。这个因子现在在市场里如鱼得水，说不定半年后就变成错误信号了。最近两年的信号相对之前的几年肯定是最具有参考性的。如果有个因子前面表现很不错，然后最近两年开始下滑，我个人认为这是很需要警惕的。下面是我的例子：这是我挖出来的一个ra，乍一看，基础要求都满足，sharpe和fitness还高的离谱。但是我们细看21年和22年，这两年的margin从合格走向不合格。用大家常说的一个词叫做：圆顶。这种就是圆顶因子我们看不到它往上增长的趋势了。对于usa地区而言，这几年行情好，很多因子都是翘头趋势。这个因子反而是圆顶。对此，只能说等到os更新的时候，对这个因子再次回测，看看这个因子到底跑的怎么样。现阶段肯定是不建议提交的，亏钱的几率非常的大。所以，如果指标不是年年好，那就专注21年和22年。游戏王名言：好的因子不应该受到任何特定事件的冲击，比如20年的疫情。如果实在不能平滑向上，那就优先翘头而不是圆顶。那什么才叫年年好呢？从13年开始就有数据的，delay1的地区（我才刚开始尝试d0在此不做判断），对于sharpe而言，都大于1已经很不错了。有的人会问：是否允许有负的sharpe？我个人是允许的，只要不要发生在21年和22年。同时，负的幅度不要太大，一般就是-0.5以内。但凡比较大的负值，pnl看起来都会有些抽象，已经不满足我们的必须指标中的“pnl平滑”了。还有的人会说：这个因子有几年只有零点几的sharpe，能接受吗？这个时候最好的办法就是看这几年的margin。如果margin在这几年依旧达标，说明这个因子表现不是特别好、信号不是很强的时候依旧可以赚钱，那这个因子是值得肯定的。可是有很多这样的问题：这个因子从18年开始才有数据，数据很漂亮，能不能交？我的建议是，数据覆盖不超过8年的，都尽量不要交。意思就是，最多允许从15年开始有数据。但这里提到一点，weijie老师在因子模版的帖子里的一个评论针对snt27的模版的有提到，观察数据更新频率，不失为一个好的因子。这里我只能说高手仁者见仁了。Snt27我至今都存着没敢交。游戏王名言：如果你十年是逐年大于1，那5年是不是起码得逐年大于2？这甚至还只是一个下限，实际应该更加高。我的建议就是，你把下面的滑动窗口视图拉大到有数据的那几年看看，是否符合我前面提到的必须要求？举例来说：拉大之后，我们能看到这个pnl并不是很平滑，而且也是圆顶的（其实指标也看的出来），这个因子就不值得信赖了。接下来我们来解析turnover。Turnover为什么不是越低越好？反而是维持在12%？这里我们要强调一个点。股票、期货等等，我们追求的是一个对冲的思想。我们通过合理的做多做空，来实现对市场变化的应变。大家可以理解为，如果我的turnover非常低，只有百分之一点几，那这只股票基本上一年下来就不交易多少次，更多的就变成了极其稳定的持仓，这和对冲流动的思想是相违背的。游戏王名言：turnover很低的因子，我都不知道它赚的是什么钱。Weijie老师名言：turnover 5%以下的因子，都是“死鱼”因子。你要问这个12%的标准怎么来的，说实话我也不知道，就像各个地区的margin最低标准一样，我也不清楚怎么算出来的。但我们把turnover控制在一个良好的范围，就是为了能让因子的表现更加稳定（这也是出自一位大佬的总结，名字我也给忘了，在这里表示道歉和感谢）。其他表现几乎一致的情况下，能积极对冲的因子一定会比死鱼因子更加值得信赖的。于我个人的理解，就是一般情况下控制在5%以上20%以下都是ok的。每个人可以根据自己的需要进行调整。什么叫进行调整？以我自己为例，我一开始做usa的时候，交了非常多换手率只有百分之一点几的超级死鱼因子。当时我的想法就是为了尽可能拔高margin。后来我意识到这种想法是错误的时候，鑫佬建议我提交一些换手率较高的因子来使combine的表现获得提升，因此接下来我就交了不少margin只有万分之五到十，但是turnover有20%到30%的因子。大家可以理解为我用刚刚达标的因子着重的提高turnover了。但这只是权宜之计，并不是值得学习的行为。那有的兄弟会问，对于高换手的主题呢？这里我必须得和大家讲述一下turnover和return，margin的关系。我们都说，这是一个跷跷板，return一定，turnover越高margin越低。对于超高换手率，比如40%到50%，如果你的return一样可以做到40%，那我觉得这个因子你提交完全ok的，这一定是一个不错的因子。但如果你的return只有15%，换手率还如上，那我觉得这就是一个亏钱因子了。为啥换手率高会亏钱？因为每一次换手都有手续费呀。换的越多手续费越多。你的因子赚的钱都不够交手续费，那只有亏钱的道理。但是对于死鱼因子，我自己有一个不太一样的看法。在你对于一个因子的质量实在是拿不准的时候，死鱼因子就是一个很好的提交方式。你通过把turnover压得很低来大幅度提高margin，让因子的样本内表现看起来相对还可以。同时，由于是死鱼因子，搞笑一点来说，就算是亏钱因子，也亏不了多少钱，因为你的因子几乎不交易（令人哑然失笑）。因此，换手率极低并非完全不可取，还是那句话，你需要依你自己的情况而定。对于drawdown这个指标，没有什么特殊的情况，肯定越低越好。但大家肯定遇到过下面这个样子的因子：这个因子的drawdown很高，都有百分之十了，这时候我们到底如何考虑呢？我个人的建议就是：return覆盖drawdown，margin覆盖turnover只要return比drawdown高，margin比turnover高，我觉得可以尝试。比如我这个因子，return20%以上显著大于turnover，这个是没问题的。当然，这个因子大家能看到，多空并不是特别平衡。明显做多大于做空。所以这个因子赚的是多头的钱，相较于其他的多空平衡的因子就不是那么稳定了。那到底多空要怎么看呢？这里我们也分三个点，这三个点平行考虑，不分先后。对于多空都很重要：多加空能覆盖universe是比较好的多基本上等于空多空不要浮动变化。什么是不要浮动变化呢？举例来说，比如TOP3000的universe，一个因子，一开始多空都是九百到一千，过了两年变成一千五到一千六，过了两年变成九百到一千。这说明这个因子选股经常选到具备某些特征的股票，这些股票不是每次都可以挤到TOP3000，挤进去的时候多空就拉起来，挤不进去就下降。相对来说稳健性依旧比不上多空不浮动的因子所以我刚刚举例的这个drawdown很高的因子，几乎三点都不满足。不过就像排序一样，多空只要不是赌博，就可以放在最后考虑。问题不大（自我安慰）。看到这里肯定很多朋友有疑问了。传奇耐打王难道不看performance comparison吗？肯定要看的，接下来我们就来详细解析这个该怎么看。答案：同优化指标。意思就是，并不是说真的是“四绿两红”才能交，也不是“四绿中的至少两绿”才能交。判断逻辑与之前是一致的。首先sharpe和fitness肯定越高越好，但如果一个加一个减怎么办，那就算净值，净值更优的排更靠前。我基本上只重点关注这两个值，对于return和margin，只要持续保持达标以上，我觉得加加减减并不关键。还是游戏王那句话，我们要的是——稳赚！！！同理，turnover保持12%浮动，drawdown尽可能降低（偶尔有的因子拉起来一点问题都不大）。所以，这个performance comparison我觉得并不是判断的关键。下面拿一个因为performance comparison阻止我提交的因子举例：这个因子看起来都挺漂亮的，是一个ra，但是我的performance comparison显示是全红（真的心碎）。因此这个因子我最终放弃了。大家不要觉得我粘贴出来的因子看起来质量都不错。我自己也交了不少sharpe只有不到1.3，fitness0.5出头的ppa，这些都没有绝对的标准。还是那句话，看你自己的需要。对于提交因子这件事情，大家一定要管得住自己的手，在保持理性的前提下，再做提交的思考。毕竟我们为的不是那一天得多少base，而是为了未来的每天都有更多base。以上是对于因子提交的优化指标的讨论。到此这个系列暂时就完结了。如果对您有帮助，请留下您宝贵的赞。如有不正之处，恳请佬们批评指正。大家有什么问题，或者还有什么没有归纳到位的地方，都可以在评论区留言提出。或者你带着你的因子截个图放到评论区，问问传奇耐打王能不能交，我也是非常乐意解答的。最后祝大家都能vf1.0，combine节节高。

---

### 帖子 #76: 这个因子到底能不能交？（下） 【传奇耐打王系列一】
- **主帖链接**: https://support.worldquantbrain.com这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md
- **讨论数**: 24

上一篇在这： [这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md-这个因子到底能不能交-上-传奇耐打王系列一](这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md)

刚刚更新的combine证明我的思路大体应该是正确的：


> [!NOTE] [图片 OCR 识别内容]
> AIP
> Nmno tAl
> NIONI a(T
> C-IrTIITTSC
> T ATIHII
> UMTNTTIRNT21V
> Eligibility Criteria
> O
> CFen
> U
> Cn
> SIgnL
> 1Tn7IFrrort
> Fymmids Complsted
> IUs ULCIL
> ThITPI
> Wha FeTormaTCe
> 2.15
> CLemmm
> Combinod Soloced Aloh Prrtormancn
> mch Tocmo
> Combined Power PolMlpha Partormanco
> 2.22


那接下来我们就继续讨论啦！

说完了必须指标，我们该讨论优化指标了。优化指标就是在完成必须指标的基础上好中选优，位次越靠前优先度越高：

1.低相关（先pc后（sc或ppac））

2.sharpe和fitness的21年和22年优秀

3.sharpe和fitness逐年优秀

4.margin的21年和22年达标

5.margin的逐年达标

6.margin的21年和22年优秀

7.margin的逐年优秀

8.margin和return越高越好

9.turnover围绕在12%

10.drawdown越低越好

11.多空优秀

这里大家可以看到，我把低相关放到了第一位。首先，为什么追求pc低。很多时候我们都说，pc低可遇不可求，所以我们先拿准自己的池子，对sc做出要求。这里我们可以类比，每个人的池子是小池子，你提交上去的池子是世坤的池子，是大池子。你想把sc降低，那世坤也想把属于他的sc（pc）降低呀。

鑫佬名言：你做了别人没做过的（pc低），这对于世坤来说，就是杰出的贡献。

为什么说base主要看pc，这就是世坤衡量你贡献的主要指标。

在pc足够低的情况下，我认为可以相对忽略更优质的指标，优先选择pc低。

鑫佬名言：pc0.5以下就是极品，0.3以下已经是极品中的极品。

我当时交了一个0.2几的pc，是我成为有条件顾问后单日base首次破3。

以下举例一个我最近刚交的ra：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> N3ILT
> RrsNR
> CTTTILaU
> FTIIIFFTINT
> mII
> ARUNOMNUATI
> 2.29
> 5.419
> 3.813
> SE沾
> 11.8993
> IsT0
> TT
> OS
> T
> TCo
> 4A191
> hMre
> T
> 071T21 「T
> R7111
>  kg4
> UItot
> at
> N
> Chart
> I'Est HillT' Cnstrimer
> ATIMAI
> _匕
> 0.,76
> 904
> 7.18N
> 12,58m
> Correlation
> IoLC
> CALT219
> PI
> C-~TAIOI[
> Testing Status
> I1 FENCINL
> PdCrIalon
> ITu SuIinoII
> 0.3656
> 0.3925
> n]T


毫无疑问，赚的多而且对vf和combine有极大的帮助

再次强调，一定要满足基础要求！基础要求不满足不要看pc！

但我还在论坛里看到另外一个ppa大佬的经验分享（具体一下子找不到了，在这里对您表示感谢）：pc高说明什么？说明交的人多。交的人多从概率上说明这个因子值得信赖，否则为什么别人看到了高相关还交呢？我觉得这也是有道理的。

因此我觉得pc是一个很主观的东西，就是每个人心中要有符合自己个人的阈值。我一般不会在官方要求上再加一个自己的高要求（比如有的大佬pc0.6以上就不交），但对于一个小白来说，我还是更加重表现，比如下面这个ppa，也是我最近交的：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> N3ILT
> 41+7891757
> CTTTILaU
> TITH
> UAUTUUNUCOAL/
> SINVJaVIOC
> 3,33
> 5.354
> 6,115
> 1.253
> 24%
> 5T4
>  
> U4
> 11443
> OV
> 47
>  Hr
> TI7r
> TSITaln[
> Uge
> 2
> 7
> Ct
> Chart
> Ie? O
> CUIISISTIP
> AIreMLOu
> HD
> 二 FSI
> 15
> 4.975
> 1.719
> 1T
> Correlation
> Iron TT7
> 0.2975
> ~0.1253
> 05 Testing Slalus
> 1CTllsn
> PeOI
> UIIICI CI
> L u
> AMm。I IL
> 09065
> 0,4723
> 941451
> 247


虽然pc非常高，但是表现我很认可，再加上sc也不错，对于我的池子有不小的帮助，我会果断地提交它。

也有人问我sc的阈值，说实话，我也是按照官方的来的。甚至有时候，我会因为sharpe提高百分之十而提交不满足pc或者sc的因子，这都是需要根据表现来进行考虑的。

这里我详细解答为什么我会提交这样的因子。首先，提交这样的因子对combine的帮助很可能是负的。但是对于vf而言，如果你觉得这个因子你稳赚，那提交了就是正的收益。可能对于这个时期的我，我的目标是优先冲击vf高，所以为了收益我希望我有更多稳定赚的因子，所以我会提交。这是对于我个人现阶段的影响之下我的选择。

这里说一个我建议的阈值，我在组sa时发现，sc控制在0.55到0.6时往往可以实现因子的表现最大化。所以我觉得如果你要设置一个个人的sc阈值，0.6就已经很好了。对于像我一样的大部分小白，只跑一二三阶，我们能挖到低相关是存在很大一部分的运气成分。如果把阈值设置的太低，会导致我们无法提交足够数量的因子。数量同样也是一个重要的维度，因此我不建议自己设置太低的阈值。

在讨论接下来的指标之前，我先对这个顺序做解释。为什么sharpe和fitness在margin和return之前？因为稳定是一个因子非常非常重要的因素！！！划重点！！！

游戏王名言：因子一定是先稳而后赚。

我们的基础要求中有一个margin达标，margin达标说明已经能大概率赚钱了。接下来我们的目标就是要让因子稳定赚钱。稳定赚钱的因子我们称之为“印钞机”。我可以允许我一次赚的不多，但我一定要一直赚！！！稳定赚钱的因子对于vf和combine的帮助是超级大的。

接下来我们来说指标。我都是先写21年和22年表现好，而后才是逐年表现好。大家都希望逐年表现好。但除非顶尖高手我们都做不到逐年都好。因此关注最近两年是很重要的。为什么因子会不断地挖出来，不断地退役，就是因为因子具有时效性。这个因子现在在市场里如鱼得水，说不定半年后就变成错误信号了。最近两年的信号相对之前的几年肯定是最具有参考性的。如果有个因子前面表现很不错，然后最近两年开始下滑，我个人认为这是很需要警惕的。下面是我的例子：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> nNRA
> RrsNR
> CTTTILaU
> rT NTI,
> FFMIpm'
> U-mrsl
> C UIJL
> Code
> 15 Summary
> NTINTT 
> 4.80
> 34.91N
> ,46
> 39
> 1=
> SIIUOUI
> Uat
> T
> M
> 3
> Tmo
> T
> sa
> Cno Alah
> Chart
> Hls:naUtrallzed
> CVEU
> 3.519
> 10.829
> SO
> 6,20650
> Isbahilf' canstiner
> ATINCICTT
> F Lutuleer PnL
> In aImt CrsTJIIEIFT
> 26.299
> 8.425
> 3.399
> 6.4190
> Correlation
> 15 Testing Status
> eLCTrlotlc
> yr
> otm


这是我挖出来的一个ra，乍一看，基础要求都满足，sharpe和fitness还高的离谱。但是我们细看21年和22年，这两年的margin从合格走向不合格。用大家常说的一个词叫做：圆顶。这种就是圆顶因子我们看不到它往上增长的趋势了。对于usa地区而言，这几年行情好，很多因子都是翘头趋势。这个因子反而是圆顶。对此，只能说等到os更新的时候，对这个因子再次回测，看看这个因子到底跑的怎么样。现阶段肯定是不建议提交的，亏钱的几率非常的大。

所以，如果指标不是年年好，那就专注21年和22年。

游戏王名言：好的因子不应该受到任何特定事件的冲击，比如20年的疫情。

如果实在不能平滑向上，那就优先翘头而不是圆顶。

那什么才叫年年好呢？

从13年开始就有数据的，delay1的地区（我才刚开始尝试d0在此不做判断），对于sharpe而言，都大于1已经很不错了。有的人会问：是否允许有负的sharpe？我个人是允许的，只要不要发生在21年和22年。同时，负的幅度不要太大，一般就是-0.5以内。但凡比较大的负值，pnl看起来都会有些抽象，已经不满足我们的必须指标中的“pnl平滑”了。还有的人会说：这个因子有几年只有零点几的sharpe，能接受吗？这个时候最好的办法就是看这几年的margin。如果margin在这几年依旧达标，说明这个因子表现不是特别好、信号不是很强的时候依旧可以赚钱，那这个因子是值得肯定的。

可是有很多这样的问题：这个因子从18年开始才有数据，数据很漂亮，能不能交？

我的建议是，数据覆盖不超过8年的，都尽量不要交。意思就是，最多允许从15年开始有数据。

但这里提到一点，weijie老师在因子模版的帖子里的一个评论针对snt27的模版的有提到，观察数据更新频率，不失为一个好的因子。这里我只能说高手仁者见仁了。Snt27我至今都存着没敢交。

游戏王名言：如果你十年是逐年大于1，那5年是不是起码得逐年大于2？这甚至还只是一个下限，实际应该更加高。

我的建议就是，你把下面的滑动窗口视图拉大到有数据的那几年看看，是否符合我前面提到的必须要求？举例来说：


> [!NOTE] [图片 OCR 识别内容]
> UTTRA
> rJuno
> CTtR
> UTLIT-GU
> UTrt
>  TTTT
> 「
> TTIIFFI
> Coce
> Summar
> TJlI?N
> UII
> GRs
> ATIIIL
> 2.979
> 1.73
> 8.77%
> 3.41沆
> 59 C19
> T
> L
> UaS
> T
> N
> Rm
> 449
> ao
> U
> 5TIII
> |!$
> [
> Lsoaar
> 。
> Cna AI I
> Chart
> TII 51
> Ris eulnllied
> 295
> 4.4
> 265 
> 29.933e
> Inrestabllity
> CUIISITIIP
> 91 TTrPML
> IThIm CrrTIAHFm
> 2.843
> 909
> 3.809
> 55.56e
> Correlation
> IS Testing Status
> Tl Crrlalc



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> O0OK
> UOOK
> Mayq
> Sep"19
> Nay 20
> Jan 
> lan 22
> Sop22
> Jan'23
> PnL
> RIsk Neutralized Pn
> Investability Constraned Pn
> Sep
> May
> Ser
> Na


拉大之后，我们能看到这个pnl并不是很平滑，而且也是圆顶的（其实指标也看的出来），这个因子就不值得信赖了。

接下来我们来解析turnover。Turnover为什么不是越低越好？反而是维持在12%？这里我们要强调一个点。股票、期货等等，我们追求的是一个对冲的思想。我们通过合理的做多做空，来实现对市场变化的应变。大家可以理解为，如果我的turnover非常低，只有百分之一点几，那这只股票基本上一年下来就不交易多少次，更多的就变成了极其稳定的持仓，这和对冲流动的思想是相违背的。

游戏王名言：turnover很低的因子，我都不知道它赚的是什么钱。

Weijie老师名言：turnover 5%以下的因子，都是“死鱼”因子。

你要问这个12%的标准怎么来的，说实话我也不知道，就像各个地区的margin最低标准一样，我也不清楚怎么算出来的。但我们把turnover控制在一个良好的范围，就是为了能让因子的表现更加稳定（这也是出自一位大佬的总结，名字我也给忘了，在这里表示道歉和感谢）。其他表现几乎一致的情况下，能积极对冲的因子一定会比死鱼因子更加值得信赖的。

于我个人的理解，就是一般情况下控制在5%以上20%以下都是ok的。每个人可以根据自己的需要进行调整。什么叫进行调整？以我自己为例，我一开始做usa的时候，交了非常多换手率只有百分之一点几的超级死鱼因子。当时我的想法就是为了尽可能拔高margin。后来我意识到这种想法是错误的时候，鑫佬建议我提交一些换手率较高的因子来使combine的表现获得提升，因此接下来我就交了不少margin只有万分之五到十，但是turnover有20%到30%的因子。大家可以理解为我用刚刚达标的因子着重的提高turnover了。但这只是权宜之计，并不是值得学习的行为。

那有的兄弟会问，对于高换手的主题呢？

这里我必须得和大家讲述一下turnover和return，margin的关系。

我们都说，这是一个跷跷板，return一定，turnover越高margin越低。对于超高换手率，比如40%到50%，如果你的return一样可以做到40%，那我觉得这个因子你提交完全ok的，这一定是一个不错的因子。但如果你的return只有15%，换手率还如上，那我觉得这就是一个亏钱因子了。为啥换手率高会亏钱？因为每一次换手都有手续费呀。换的越多手续费越多。你的因子赚的钱都不够交手续费，那只有亏钱的道理。

但是对于死鱼因子，我自己有一个不太一样的看法。在你对于一个因子的质量实在是拿不准的时候，死鱼因子就是一个很好的提交方式。你通过把turnover压得很低来大幅度提高margin，让因子的样本内表现看起来相对还可以。同时，由于是死鱼因子，搞笑一点来说，就算是亏钱因子，也亏不了多少钱，因为你的因子几乎不交易（令人哑然失笑）。因此，换手率极低并非完全不可取，还是那句话，你需要依你自己的情况而定。

对于drawdown这个指标，没有什么特殊的情况，肯定越低越好。但大家肯定遇到过下面这个样子的因子：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> Irto  Iy
> Nnu nul
> Cn R
> UTGI
> nNRA
> RrsNR
> CTTTILaU
> FTIIFFI711
> CTmNSI
> Coce
> Summary
> CUIT
> JIJV
> 41I1TNIMaAINTaL .
> MIMTII
> GR
> Aret?uU
> 22
> 2.45
> 21,91%
> 11459
> 59,49mm
> 16
> T
> Las
> T
> N
> Ro
> 14
> 2
> 
> [
> Lnear
> !
> TI TM
> Oo 
> 41
> Chart
> Jg
> Ta
> 
> Hsk MeULTAUIZEU
> 0.54
> 833%
> 11.055
> 2263-0
> Iet F
> OITTTTTPI
> AIrotdteDu
> 3.29-0
> 16.409
> 15.213
> 99747
> Correlation
> Os Testing Status
> Corlalc
> 1


这个因子的drawdown很高，都有百分之十了，这时候我们到底如何考虑呢？

我个人的建议就是：return覆盖drawdown，margin覆盖turnover

只要return比drawdown高，margin比turnover高，我觉得可以尝试。比如我这个因子，return20%以上显著大于turnover，这个是没问题的。

当然，这个因子大家能看到，多空并不是特别平衡。明显做多大于做空。所以这个因子赚的是多头的钱，相较于其他的多空平衡的因子就不是那么稳定了。

那到底多空要怎么看呢？这里我们也分三个点，这三个点平行考虑，不分先后。对于多空都很重要：

1. 多加空能覆盖universe是比较好的
2. 多基本上等于空
3. 多空不要浮动变化。什么是不要浮动变化呢？举例来说，比如TOP3000的universe，一个因子，一开始多空都是九百到一千，过了两年变成一千五到一千六，过了两年变成九百到一千。这说明这个因子选股经常选到具备某些特征的股票，这些股票不是每次都可以挤到TOP3000，挤进去的时候多空就拉起来，挤不进去就下降。相对来说稳健性依旧比不上多空不浮动的因子

所以我刚刚举例的这个drawdown很高的因子，几乎三点都不满足。不过就像排序一样，多空只要不是赌博，就可以放在最后考虑。问题不大（自我安慰）。

看到这里肯定很多朋友有疑问了。传奇耐打王难道不看performance comparison吗？

肯定要看的，接下来我们就来详细解析这个该怎么看。

答案：同优化指标。

意思就是，并不是说真的是“四绿两红”才能交，也不是“四绿中的至少两绿”才能交。判断逻辑与之前是一致的。首先sharpe和fitness肯定越高越好，但如果一个加一个减怎么办，那就算净值，净值更优的排更靠前。我基本上只重点关注这两个值，对于return和margin，只要持续保持达标以上，我觉得加加减减并不关键。还是游戏王那句话，我们要的是——稳赚！！！同理，turnover保持12%浮动，drawdown尽可能降低（偶尔有的因子拉起来一点问题都不大）。所以，这个performance comparison我觉得并不是判断的关键。下面拿一个因为performance comparison阻止我提交的因子举例：


> [!NOTE] [图片 OCR 识别内容]
> INm
> 2,30
> 643
> 2]
> 357泗
> 66
> 11.10
> 7 e
> ol4e
> 
> Tag
> N
> TU
> NU TCtCn
> 0+
> gse
> 28
> Cen Nohe
> Chyrt
> IntlCnnrlrai-
> AAIIOIAI』
> 4,033
> 2.769
> 2,384
> 13.6954
> Te LLIIy CrIoTsUF
> Correlaton
> 944』!


这个因子看起来都挺漂亮的，是一个ra，但是我的performance comparison显示是全红（真的心碎）。因此这个因子我最终放弃了。

大家不要觉得我粘贴出来的因子看起来质量都不错。我自己也交了不少sharpe只有不到1.3，fitness0.5出头的ppa，这些都没有绝对的标准。还是那句话，看你自己的需要。对于提交因子这件事情，大家一定要管得住自己的手，在保持理性的前提下，再做提交的思考。毕竟我们为的不是那一天得多少base，而是为了未来的每天都有更多base。

以上是对于因子提交的优化指标的讨论。到此这个系列暂时就完结了。如果对您有帮助，请留下您宝贵的赞。

如有不正之处，恳请佬们批评指正。大家有什么问题，或者还有什么没有归纳到位的地方，都可以在评论区留言提出。或者你带着你的因子截个图放到评论区，问问传奇耐打王能不能交，我也是非常乐意解答的。

最后祝大家都能vf1.0，combine节节高。

---

### 帖子 #77: 这个模版到底怎么做？【传奇耐打王系列三】论坛精选
- **主帖链接**: 这个模版到底怎么做【传奇耐打王系列三】论坛精选.md
- **讨论数**: 12

传奇耐打王好像从未分享过有实际用途或者含金量的东西。今天，他来了。我们对于因子的构建思路来一个认真且专注的讨论。我们都知道因子由操作符+字段组成。那这个上，我们就先来他讨论一下操作符。假设输出都是x。就以捕捉x的波动性来举例：说到波动性我们的第一反应肯定是ts_std_dev 标准差可以反应一个对象的波动性那标准差刻画的是什么？是不是x与ts_mean(x, d1)的偏离程度？那我们不要算标准差这么复杂嘛，我们弄得简单一点：x - ts_mean(x, d1)x / ts_mean(x, d1)那除了ts_mean(x, d1)能反映这个x这段时间的中心，还有什么可以反映？ts_median(x, d1)，那刚刚的是不是可以再来一遍？那既然中心考虑过了，那极值是不是也可以考虑一下？ts_max(x, d1), ts_min(x, d1)5、这时候很多伙伴要跟我说了，但这些都已经有对应的操作符了呀，ts_av_diff, ts_min_diff好的。那我来问一个问题？波动的波动有没有想过？有没有可能在一段时间内，x持续的偏离ts_max(x, d1)且偏离的程度大差不差从而体现了平稳呢？这当然是可能的！我们只需要做ts_std_dev(ts_max_diff(x, d1), d2)，且d1 > d2。如果这个值很小，表示短期的x持续的偏离长期的最大值，就体现了一个稳态。这是多么有意思的事情！6、可是朋友们，我们的思路绝对不能只局限于此啊。我是怎么思考波动性这个特征的呢？简单思考一下，变化的快慢是不是可以体现波动性？什么东西能反应变化的快慢？我是数学专业，我的第一反应就是导数。但我们没有求导这个操作符啊，那我怎么构造与求导类似的操作符组合呢？我想到了差分。二阶差分就是最靠近导数的东西。所以很简单的，我们构造出一个新的模版：ts_delta(ts_delta(x, d1), d2)那还能怎么思考呢？这里我再提供一个数学角度的思路。我们pnl曲线看多了总是喜欢平滑连续的东西。但我们实际拿到的字段可以是跳跃的、间断的。那我们能通过这个跳跃和间断设计什么呢？我觉得可以做一个开关。假设x的均线在a，x的最值在a+1000，那我是不是可以去捕捉x超出a + 500的时段或者说个数相对于总体的占比呢？这个占比达到一个什么程度难道不也是一种波动的体现吗？8、既然可以捕捉占比，那是不是也可以捕捉相邻两次突破设定的阈值间隔的时间呢？关于波动性，我已经提供了8个思路，这还只是针对波动性捕捉的小小的一部分。只要你敢想，没什么做不出来的。当时我在研究小组调侃，我中午睡午觉想了一些模版。这8点中的一部分就是那个午觉带来的，经过测试，效果嘎嘎良好。希望大家和我一起集思广益，这个因子的构造真的是无穷无尽的东西。敬请期待下集，我分享关于字段构建中的巧思。

---

### 帖子 #78: 这个模版到底怎么做？【传奇耐打王系列三】论坛精选
- **主帖链接**: https://support.worldquantbrain.com这个模版到底怎么做【传奇耐打王系列三】论坛精选_40735661471383.md
- **讨论数**: 12

传奇耐打王好像从未分享过有实际用途或者含金量的东西。今天，他来了。

我们对于因子的构建思路来一个认真且专注的讨论。

我们都知道因子由操作符+字段组成。

那这个上，我们就先来他讨论一下操作符。

假设输出都是x。

就以捕捉x的波动性来举例：说到波动性我们的第一反应肯定是

- ts_std_dev 标准差可以反应一个对象的波动性
- 那标准差刻画的是什么？是不是x与ts_mean(x, d1)的偏离程度？

那我们不要算标准差这么复杂嘛，我们弄得简单一点：

x - ts_mean(x, d1)

x / ts_mean(x, d1)

- 那除了ts_mean(x, d1)能反映这个x这段时间的中心，还有什么可以反映？

ts_median(x, d1)，那刚刚的是不是可以再来一遍？

- 那既然中心考虑过了，那极值是不是也可以考虑一下？
  ts_max(x, d1), ts_min(x, d1)

5、这时候很多伙伴要跟我说了，但这些都已经有对应的操作符了呀，ts_av_diff, ts_min_diff

好的。那我来问一个问题？波动的波动有没有想过？

有没有可能在一段时间内，x持续的偏离ts_max(x, d1)且偏离的程度大差不差从而体现了平稳呢？

这当然是可能的！我们只需要做

ts_std_dev(ts_max_diff(x, d1), d2)，且d1 > d2。

如果这个值很小，表示短期的x持续的偏离长期的最大值，就体现了一个稳态。

这是多么有意思的事情！

6、可是朋友们，我们的思路绝对不能只局限于此啊。我是怎么思考波动性这个特征的呢？

简单思考一下，变化的快慢是不是可以体现波动性？

什么东西能反应变化的快慢？

我是数学专业，我的第一反应就是导数。

但我们没有求导这个操作符啊，那我怎么构造与求导类似的操作符组合呢？

我想到了差分。二阶差分就是最靠近导数的东西。

所以很简单的，我们构造出一个新的模版：

ts_delta(ts_delta(x, d1), d2)

- 那还能怎么思考呢？这里我再提供一个数学角度的思路。我们pnl曲线看多了总是喜欢平滑连续的东西。但我们实际拿到的字段可以是跳跃的、间断的。

那我们能通过这个跳跃和间断设计什么呢？我觉得可以做一个开关。

假设x的均线在a，x的最值在a+1000，那我是不是可以去捕捉x超出a + 500的时段或者说个数相对于总体的占比呢？

这个占比达到一个什么程度难道不也是一种波动的体现吗？
8、既然可以捕捉占比，那是不是也可以捕捉相邻两次突破设定的阈值间隔的时间呢？

关于波动性，我已经提供了8个思路，这还只是针对波动性捕捉的小小的一部分。只要你敢想，没什么做不出来的。当时我在研究小组调侃，我中午睡午觉想了一些模版。这8点中的一部分就是那个午觉带来的，经过测试，效果嘎嘎良好。

希望大家和我一起集思广益，这个因子的构造真的是无穷无尽的东西。

敬请期待下集，我分享关于字段构建中的巧思。

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《04.【永久置顶】高Value Factor顾问分享合集，赚钱必读！(更新1029）Pinned经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 04【永久置顶】高Value Factor顾问分享合集赚钱必读更新1029Pinned经验分享_32032776365079.md
- **评论时间**: 7 months ago

我的vf更新至0.89了，第一次更新，感觉和大佬们还有好大的差距。对于alpha的多样性我做的确实不够。继续努力

---

### 探讨 #2: 关于《04.【永久置顶】高Value Factor顾问分享合集，赚钱必读！(更新1029）置顶的经验分享》的评论回复
- **帖子链接**: [Commented] 04【永久置顶】高Value Factor顾问分享合集赚钱必读更新1029置顶的经验分享.md
- **评论时间**: 7个月前

我的vf更新至0.89了，第一次更新，感觉和大佬们还有好大的差距。对于alpha的多样性我做的确实不够。继续努力

---

### 探讨 #3: 关于《05.【AI精选合集】创建一个具有BRAIN全部知识+金融博士+计算机博士的免费助手Pinned》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 05【AI精选合集】创建一个具有BRAIN全部知识金融博士计算机博士的免费助手Pinned_35954766785175.md
- **评论时间**: 7 months ago

我一直都想做一个ai工作流，但是没有一个整体性的框架。这次的样本代码对我的帮助非常大，我很快就尝到甜头，把一个因子的夏普修改提高了0.4

---

### 探讨 #4: 关于《05.【AI精选合集】创建一个具有BRAIN全部知识+金融博士+计算机博士的免费助手置顶的》的评论回复
- **帖子链接**: [Commented] 05【AI精选合集】创建一个具有BRAIN全部知识金融博士计算机博士的免费助手置顶的.md
- **评论时间**: 7个月前

我一直都想做一个ai工作流，但是没有一个整体性的框架。这次的样本代码对我的帮助非常大，我很快就尝到甜头，把一个因子的夏普修改提高了0.4

---

### 探讨 #5: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 2025年Q4 Genus升级失败小结.md
- **评论时间**: 5个月前

真的是可惜了。如果没有混塔的话，这妥妥的gm实力。一定不要忘了社区分。社区分真的是你做因子考虑六维的关键。像一些远古的gm的社区分高达70，实在是太高，他们可以大大方方高per做因子。所以说，还是要全方面考虑

我比较想请教大佬glb是怎么做的，恳请分享一下————————这个季度一定gm————————

---

### 探讨 #6: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 2025年Q4 Genus升级失败小结_37581803221143.md
- **评论时间**: 5个月前

真的是可惜了。如果没有混塔的话，这妥妥的gm实力。一定不要忘了社区分。社区分真的是你做因子考虑六维的关键。像一些远古的gm的社区分高达70，实在是太高，他们可以大大方方高per做因子。所以说，还是要全方面考虑

我比较想请教大佬glb是怎么做的，恳请分享一下————————这个季度一定gm————————

---

### 探讨 #7: 关于《PPA Combine提升进度不及预期，道阻且长经验分享》的评论回复
- **帖子链接**: [Commented] PPA Combine提升进度不及预期道阻且长经验分享.md
- **评论时间**: 7个月前

我觉得你的margin明显偏低，尤其是eur地区，在performance里还低于百分之十，你需要进行深刻反思了，这肯定会对你的combine有很大的负面影响的

---

### 探讨 #8: 关于《PPA Combine提升进度不及预期，道阻且长经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] PPA Combine提升进度不及预期道阻且长经验分享_36412244448535.md
- **评论时间**: 7个月前

我觉得你的margin明显偏低，尤其是eur地区，在performance里还低于百分之十，你需要进行深刻反思了，这肯定会对你的combine有很大的负面影响的

---

### 探讨 #9: 关于《But for safety against 'universe' if they put it there:》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] PYTHON alpha的ast解析和语法检查经验分享_40175357844503.md
- **评论时间**: 1个月前

python alpha的语法解析比fastexpr简单太多了
我看到佬说这句话的时候充满了疑问。其实我觉得wqb的快速表达式是一个非常方便的东西，就好比将py文件中的一个模块独立出来，专门供使用者修改。那佬您在使用python alpha的过程中有感觉什么地方相比快速表达式更加方便快捷的吗？劳烦您举例说明一下
----------------------------------------------------来自传奇耐打王的点赞-------------------------------------------------------------------

---

### 探讨 #10: 关于《WorldQuant BRAIN MCP 工具调用架构升级：从 Stdio 到 HTTP API代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] WorldQuant BRAIN MCP 工具调用架构升级从 Stdio 到 HTTP API代码优化_40150797833239.md
- **评论时间**: 1个月前

我特别想请教橘子姐的是，怎么想到要这样更新这个架构呢？因为原本也有很多对应的断点续传的帖子，您是怎么想到从http api这个角度来进行更新的呢？
也许我问的是非常无知的问题，我对mcp相对不是那么的熟悉，希望不要冒犯到佬

那现在这个架构是不需要mcp参与了吗？
---------------------------------------来自传奇耐打王的点赞-------------------------------------------------------------------------------

---

### 探讨 #11: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【Alpha 模板】基于情感数据的IND模板Alpha Template.md
- **评论时间**: 6个月前

能不能详细解释一下这个R1是怎么选出来的呢？

---

### 探讨 #12: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha 模板】基于情感数据的IND模板Alpha Template_36876447664023.md
- **评论时间**: 6个月前

能不能详细解释一下这个R1是怎么选出来的呢？

---

### 探讨 #13: 关于《【Alpha灵感】全球第一个MEA因子（零PC alpha），我是怎么做出来的？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】全球第一个MEA因子零PC alpha我是怎么做出来的_40134245568663.md
- **评论时间**: 1个月前

佬真的厉害！ 您的行为让我有一种第一个吃螃蟹的人的感觉。
这是多么值得赞扬的探险家精神！
我是一个相对而言不是很倾向于开新地区的顾问，一般都是等新地区开了之后大家有了cb的反馈我才会开。相比之下，我显得格外的胆小了。
希望有朝一日我也能找到像佬这样大胆做因子的自信！
------------------------------------------------来自传奇耐打王的点赞-----------------------------------------------------------------------

---

### 探讨 #14: 关于《【Combined Alpha Performance】踩坑分享，纯新手comb  -2+经验分享》的评论回复
- **帖子链接**: [Commented] 【Combined Alpha Performance】踩坑分享纯新手comb  -2经验分享.md
- **评论时间**: 1个月前

华子哥和课代表都和我着重强调过这个margin的重要性。在你记不住那些杂七杂八的提交标准的时候，只管交margin高的就对了。我们永远不害怕因子乱走，但害怕因子不具备赚钱的可能性。
---------------------------------------来自传奇耐打王的点赞------------------------------------

---

### 探讨 #15: 关于《【Combined Alpha Performance】踩坑分享，纯新手comb  -2+经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Combined Alpha Performance】踩坑分享纯新手comb  -2经验分享_40533711115927.md
- **评论时间**: 1个月前

华子哥和课代表都和我着重强调过这个margin的重要性。在你记不住那些杂七杂八的提交标准的时候，只管交margin高的就对了。我们永远不害怕因子乱走，但害怕因子不具备赚钱的可能性。
---------------------------------------来自传奇耐打王的点赞------------------------------------

---

### 探讨 #16: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md
- **评论时间**: 5个月前

佬，您强的像怪物
这太可怕了，这覆盖率、这ontrade、这质量！！！

难以想象
需要学的东西有很多，我也依旧在路上，共勉

---

### 探讨 #17: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md
- **评论时间**: 5个月前

佬，您强的像怪物
这太可怕了，这覆盖率、这ontrade、这质量！！！

难以想象
需要学的东西有很多，我也依旧在路上，共勉

---

### 探讨 #18: 关于《【MCP】角色配置：工作流该安排谁来执行？经验分享》的评论回复
- **帖子链接**: [Commented] 【MCP】角色配置工作流该安排谁来执行经验分享.md
- **评论时间**: 7个月前

原来模式的创建还有这么多的学问。看到JX28185佬对于不同需求的角色定义真是眼前一亮，这部分似乎可以更加深化的进行讨论研究

---

### 探讨 #19: 关于《【MCP】角色配置：工作流该安排谁来执行？经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md
- **评论时间**: 7个月前

原来模式的创建还有这么多的学问。看到JX28185佬对于不同需求的角色定义真是眼前一亮，这部分似乎可以更加深化的进行讨论研究

---

### 探讨 #20: 关于《【大角羊】VF0.5-0.62-0.89-0.96-0.96，辛苦耕耘-终得硕果！》的评论回复
- **帖子链接**: [Commented] 【大角羊】VF05-062-089-096-096辛苦耕耘-终得硕果.md
- **评论时间**: 6个月前

你的vf和我的太像了，我是0.5-0.89-0.97

---

### 探讨 #21: 关于《【大角羊】VF0.5-0.62-0.89-0.96-0.96，辛苦耕耘-终得硕果！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【大角羊】VF05-062-089-096-096辛苦耕耘-终得硕果_36489969008279.md
- **评论时间**: 7个月前

你的vf和我的太像了，我是0.5-0.89-0.97

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【实用报表】多维度分析Alpha最新2023年OS趋势.md
- **评论时间**: 5个月前

好的想法，这个有助于我分析我的alpha的多维度的信息。虽然说但看一年的os其实没什么参考价值，但是这个报表的制作方式确实非常的有意义，值得学习。m果然有m的独到之处啊

——————————一起加油——————————————

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【实用报表】多维度分析Alpha最新2023年OS趋势_37780459876119.md
- **评论时间**: 5个月前

好的想法，这个有助于我分析我的alpha的多维度的信息。虽然说但看一年的os其实没什么参考价值，但是这个报表的制作方式确实非常的有意义，值得学习。m果然有m的独到之处啊

——————————一起加油——————————————

---

### 探讨 #24: 关于《【工具优化】技能brain-data-scope（华子哥插件插件的数据分析模块）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【工具优化】技能brain-data-scope华子哥插件插件的数据分析模块_40091088861591.md
- **评论时间**: 1个月前

每每看到这样绝妙的帖子，我实在是忍不住点赞加评论
我曾经自己有尝试过直接用华子哥插件的数据分析内容来挖掘因子，但效果不是很良好。不过鉴于本人技能拙劣，不知道喂给大模型是否能带来全新的成就
非常期待佬您能分享一下在这个skill给了大模型之后，大模型能否带来不一样的思路，或者是否有效率的实质性提升？
---------------------------------------------------来自传奇耐打王的点赞----------------------------------------------------------------------

---

### 探讨 #25: 关于《【工具分享】Pkgdiff：在线免费给cnhkmcp做版本差异分析》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【工具分享】Pkgdiff在线免费给cnhkmcp做版本差异分析_40292420301591.md
- **评论时间**: 1个月前

这种巧思每次看到都会让我眼前一亮。对于这么一个几乎每天大家都在使用的东西。变了什么，有时候尤为重要。因为我们要学习这个作者的思想，明白为什么这么变。或者根据个人使用习惯，决定自己是否要撤回这么变，或者再依据作者的灵感，想清楚自己可以怎么变。这个小工具的实用价值真的太有效了
--------------------------------来自传奇耐打王的点赞---------------------------------------------------------------------

---

### 探讨 #26: 关于《【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template》的评论回复
- **帖子链接**: [Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template.md
- **评论时间**: 6个月前

确实是要不断的拓宽自己的思路，打破思维定式！

---

### 探讨 #27: 关于《【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template_36671111976983.md
- **评论时间**: 6 months ago

确实是要不断的拓宽自己的思路，打破思维定式！

---

### 探讨 #28: 关于《【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的》的评论回复
- **帖子链接**: [Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的.md
- **评论时间**: 7个月前

对于这个sa反映ra的表现，我确实深有感触。在10月份更新的combine我是2.2，但我的usa的sa很难组出双五以上，我的combine alpha performance的夏普和fit也都只有4点几。我现在反思更多的问题还是多样性不够

---

### 探讨 #29: 关于《【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的_35928620962839.md
- **评论时间**: 7个月前

对于这个sa反映ra的表现，我确实深有感触。在10月份更新的combine我是2.2，但我的usa的sa很难组出双五以上，我的combine alpha performance的夏普和fit也都只有4点几。我现在反思更多的问题还是多样性不够

---

### 探讨 #30: 关于《根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])》的评论回复
- **帖子链接**: [Commented] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的.md
- **评论时间**: 7个月前

我一直交了很长一段时间的高pc高表现。但是现在我愈发感觉低pc其实是一个很大的关键。如果都是交同质化的因子，对于自己和平台的帮助都是很微小的

---

### 探讨 #31: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7 months ago

11月10日量化日记

终于回到交满，尤其分享一下sa：


> [!NOTE] [图片 OCR 识别内容]
> Selection Expression
> Aggregate Data
> Sharoe
> UTNC
> FnEss
> REUTMS
> LTaVOCT
> IaTeIn
> Own &
> (color
> BLUE' )
> 6.29
> 16.66%
> 5.72
> 13.78%
> 1.4796
> 16.559600
> Combo Expression
> Year
> Sharpe
> Turnover
> Returns
> Drawdown
> Margin
> LOng Count
> Short Count
> 2013
> 10.0
> 15.75t
> 15.2291
> 0.5191
> 15.232
> 1051
> 1055
> simulation Settings
> 2011
> 5.39
> 18.07*
> 5.38
> 12.3195
> 0.5395
> 1.177
> 1313
> 1303
> Instrument Type
> Region
> UnNerse
> LangUage
> Decay
> Delay
> Truncation
> Neutralizatjon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> 2015
> 3.3
> 15.5-沁
> 2.45
> 3.2195
> .4793
> 10.497
> 13365
> 1337
> Equi?
> EUR
> TOPZSOD
> Fast Expression
> 001
> SIOWISactors
> Verif
> 2015
> 7.11
> 16 43沁
> 6.88
> 15.3893
> 0.4491
> 13.727
> 1323
> 1392
> 2017
> 16.60光
> 3.72
> 9.1495
> 0.5795
> 11.013
> 1443
> 1503
> 2013
> 5.31
> 16.115
> 5.54
> 12.3591
> 559
> 15.362
> 1-00
> 1527
> 2019
> 5.95
> 15.14北
> 5.46
> 13.9493
> 3395
> 17.253
> 35-
> 1455
> Clone Alpha
> 2020
> 5.40
> 15.35北
> 6.57
> 17.7595
> 3295
> 21.712
> 1315
> 1445
> 2021
> 7.22
> 16.50沁
> 17.3091
> 55
> 21.57
> 1410
> 1551
> N Chart
> Pnl
> 2022
> 5.21
> 16.29*
> 14.9495
> 5495
> 13.34
> 383
> 1514
> 2023
> 12.5-北
> 10.20
> 7393
> 0.1495
> 25.553:
> 1327
> 1433
> Investability constrained
> Aggregate Data
> Sharpe
> LUTICE
> TItnes
> eCUTI
> UF3wUOIT
> 4131310
> 3.70
> 7.8396
> 2.94
> 7.909
> 2.6796
> 20.189600
> 5OOOK
> 医 Correlation
> 201
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Self Correlation
> Mauimur
> IinimFT
> Lt RIM:
> Combo Pnl
> Equal Weight Pnl
> Prod Correlation
> UaYITUN
> Minimun
> 35-URLU
> 11/11/2025.3.22 Ju
> 0.4630
> -0.4492
> TOON
> Ftres


---

### 探讨 #32: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【经验分享】Combine大幅提升增幅高达174.md
- **评论时间**: 1个月前

希望佬还是更多的关注自己的Combined Alpha Performance和ppa cb，个人拙见认为这两个cb是对自己因子提交的最好的体现。也能最大程度的反应单因子提交的水平。祝愿佬这个赛季这俩的cb能稳稳破1，实现master的升级之路
----------------------------------------------------------来自传奇耐打王的点赞------------------------------------------------------------

---

### 探讨 #33: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】Combine大幅提升增幅高达174_40321767904023.md
- **评论时间**: 1个月前

希望佬还是更多的关注自己的Combined Alpha Performance和ppa cb，个人拙见认为这两个cb是对自己因子提交的最好的体现。也能最大程度的反应单因子提交的水平。祝愿佬这个赛季这俩的cb能稳稳破1，实现master的升级之路
----------------------------------------------------------来自传奇耐打王的点赞------------------------------------------------------------

---

### 探讨 #34: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【经验分享】如何从expert直升GM经验分享.md
- **评论时间**: 4个月前

佬所言极是。正所谓贪多嚼不烂。上赛季我就是因为各种开新地区，导致因子做的过于分散无法实现单地区的稳定性而combine下降。这赛季虽然在新的规则下有了很多的小地区ppa。但我向佬您的操作学习。尽可能点满一个地区所有的塔，不开新地区。旧的地区已经足够点了。把一个地区做稳定了才是真的王道

---

### 探讨 #35: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】如何从expert直升GM经验分享_38320422749463.md
- **评论时间**: 4个月前

佬所言极是。正所谓贪多嚼不烂。上赛季我就是因为各种开新地区，导致因子做的过于分散无法实现单地区的稳定性而combine下降。这赛季虽然在新的规则下有了很多的小地区ppa。但我向佬您的操作学习。尽可能点满一个地区所有的塔，不开新地区。旧的地区已经足够点了。把一个地区做稳定了才是真的王道

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【经验分享】涅槃重生vf从018到097combine从-125到202经验分享.md
- **评论时间**: 1个月前


> [!NOTE] [图片 OCR 识别内容]
> 26.02和03月
> 这两个月逐渐醒悟
> 第一步就是对-二三阶代码进行自己的改进
> 首先我把所有的字段旭下来,
> 根据描述儆聚类分析。把描述相近的字段分成一个组;
> 在迸行-
> ~阶回测的时候把同组内coverage最高的宰来回
> 测
> 并且一阶回测我利用论坛里面的模板和A1的提示重新构造了-下
> 覆盖长期。短期
> 波动。趋势。等等不同
> 风格的策略来捕捉不同的信号
> 二阶回测我将9r04p修改为了不计入fields的常见groUP,
> 如arket
> subincustry 等等
> 三阶誓时放弃了;  在抓敢回测结果时。如果找到一个信号
> 就将这个信号所属的分绾内所有
> 的字殷迸行替换并回测。再利用最大团算法迸行分团。提交每个团内表现最优的alpha。


我对这个根据描述做聚类分析非常的感兴趣。你可以详细的说一下是怎么做的吗？毕竟描述是一个相对而言比较泛的东西。你如何去界定边界或者如何进行相对比较精确的划分，我觉得这是影响非常大的，也是十分重要的。然后你提到了不同风格的策略，是否可以举几个例子。因为我在波动的策略上做的因子比较多，我很好奇趋势、长短期这类你是怎么做的。
--------------------------------------------------来自传奇耐打王的点赞-----------------------------------

---

### 探讨 #37: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】涅槃重生vf从018到097combine从-125到202经验分享_40433337996183.md
- **评论时间**: 1个月前


> [!NOTE] [图片 OCR 识别内容]
> 26.02和03月
> 这两个月逐渐醒悟
> 第一步就是对-二三阶代码进行自己的改进
> 首先我把所有的字段旭下来,
> 根据描述儆聚类分析。把描述相近的字段分成一个组;
> 在迸行-
> ~阶回测的时候把同组内coverage最高的宰来回
> 测
> 并且一阶回测我利用论坛里面的模板和A1的提示重新构造了-下
> 覆盖长期。短期
> 波动。趋势。等等不同
> 风格的策略来捕捉不同的信号
> 二阶回测我将9r04p修改为了不计入fields的常见groUP,
> 如arket
> subincustry 等等
> 三阶誓时放弃了;  在抓敢回测结果时。如果找到一个信号
> 就将这个信号所属的分绾内所有
> 的字殷迸行替换并回测。再利用最大团算法迸行分团。提交每个团内表现最优的alpha。


我对这个根据描述做聚类分析非常的感兴趣。你可以详细的说一下是怎么做的吗？毕竟描述是一个相对而言比较泛的东西。你如何去界定边界或者如何进行相对比较精确的划分，我觉得这是影响非常大的，也是十分重要的。然后你提到了不同风格的策略，是否可以举几个例子。因为我在波动的策略上做的因子比较多，我很好奇趋势、长短期这类你是怎么做的。
--------------------------------------------------来自传奇耐打王的点赞-----------------------------------

---

### 探讨 #38: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【自动化SA-新手顾问】傻瓜式一键生成回测相关性检测SA代码与思路分享.md
- **评论时间**: 7个月前

难得难得，确实需要有人站出来把最简单的东西说的清楚明白

---

### 探讨 #39: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【自动化SA-新手顾问】傻瓜式一键生成回测相关性检测SA代码与思路分享_36441421250839.md
- **评论时间**: 7个月前

难得难得，确实需要有人站出来把最简单的东西说的清楚明白

---

### 探讨 #40: 关于《【龙虎榜·卷二】Combine惊雷再起，VF季决尘埃落定，神秘GM满值归来，万刀之上几何？》的评论回复
- **帖子链接**: [Commented] 【龙虎榜卷二】Combine惊雷再起VF季决尘埃落定神秘GM满值归来万刀之上几何.md
- **评论时间**: 1个月前

哈哈哈哈哈，一个cttl+f让我哑然失笑，这里面也未能榜上有名。只能说这个wqb真的是藏龙卧虎，后生可畏。这个赛季我的小舟又能走到哪里呢？让我们一起拭目以待。
或许一个综合实力的体现，没办法在季中看到。潜水冠军都还没露头呢
-------------------------------------来自传奇耐打王的点赞------------------------------------------------

---

### 探讨 #41: 关于《【龙虎榜·卷二】Combine惊雷再起，VF季决尘埃落定，神秘GM满值归来，万刀之上几何？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【龙虎榜卷二】Combine惊雷再起VF季决尘埃落定神秘GM满值归来万刀之上几何_40347330265879.md
- **评论时间**: 1个月前

哈哈哈哈哈，一个cttl+f让我哑然失笑，这里面也未能榜上有名。只能说这个wqb真的是藏龙卧虎，后生可畏。这个赛季我的小舟又能走到哪里呢？让我们一起拭目以待。
或许一个综合实力的体现，没办法在季中看到。潜水冠军都还没露头呢
-------------------------------------来自传奇耐打王的点赞------------------------------------------------

---

### 探讨 #42: 关于《一个新的免费token plan: 商汤-日日新，支持deep seek v4 flash,  附minimax2.7, gemini pro3对比经验分享》的评论回复
- **帖子链接**: [Commented] 一个新的免费token plan 商汤-日日新支持deep seek v4 flash  附minimax27 gemini pro3对比经验分享.md
- **评论时间**: 1个月前

想请问一下佬，这里您说的指令的遵循程度，您是怎么评判出来的呢？是根据任务循环次数还是其他？
其次就是，是否可以通过调整ai的温度来实现这个指令遵循程度的增强？
 这一块对工程实现尤为重要，希望佬可以给出解答
----------------------------------------来自传奇耐打王的点赞--------------------------------------------

---

### 探讨 #43: 关于《一个新的免费token plan: 商汤-日日新，支持deep seek v4 flash,  附minimax2.7, gemini pro3对比经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 一个新的免费token plan 商汤-日日新支持deep seek v4 flash  附minimax27 gemini pro3对比经验分享_40372795793687.md
- **评论时间**: 1个月前

想请问一下佬，这里您说的指令的遵循程度，您是怎么评判出来的呢？是根据任务循环次数还是其他？
其次就是，是否可以通过调整ai的温度来实现这个指令遵循程度的增强？
 这一块对工程实现尤为重要，希望佬可以给出解答
----------------------------------------来自传奇耐打王的点赞--------------------------------------------

---

### 探讨 #44: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 借助MCP手搓IND地区short_interest点塔经验分享.md
- **评论时间**: 5个月前

楼主，请原谅我不是特别赞同您的操作方法。我用6tips分析short的三个字段发现都是一条直线。说明这三个字段大概率是常值或者空值。因此不论你是用什么操作符，到最后应该都是一条直线。如果你跑出了信号，要么这个信号是表达式中的非short部分产生的，要么就是nan handling带来的。但至于这个nan handling为什么能带来信号，我是解释不来的。希望楼主和各位佬们谨慎

---

### 探讨 #45: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 借助MCP手搓IND地区short_interest点塔经验分享_36772326144279.md
- **评论时间**: 5个月前

楼主，请原谅我不是特别赞同您的操作方法。我用6tips分析short的三个字段发现都是一条直线。说明这三个字段大概率是常值或者空值。因此不论你是用什么操作符，到最后应该都是一条直线。如果你跑出了信号，要么这个信号是表达式中的非short部分产生的，要么就是nan handling带来的。但至于这个nan handling为什么能带来信号，我是解释不来的。希望楼主和各位佬们谨慎

---

### 探讨 #46: 关于《借助与AI和MCP，我是怎样分析一个数据集的?》的评论回复
- **帖子链接**: [Commented] 借助与AI和MCP我是怎样分析一个数据集的.md
- **评论时间**: 1个月前

我不是很清楚为什么。是数据集本身的原因还是ai的原因。这类mdl的字段ai很喜欢给你来个rank
这里给出的例子大部分都逃不开这个rank的构造。我能不能理解为这是因为ai也很喜欢在截面上进行对比呢？当然如果佬您有其他的例子能体现ai对于其他类型数据集是否有较好的表达式构建的话，还劳烦您分享一下
-----------------------------------------------------------来自传奇耐打王的疑问-----------------------------------------------

---

### 探讨 #47: 关于《借助与AI和MCP，我是怎样分析一个数据集的?》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 借助与AI和MCP我是怎样分析一个数据集的_40373352844439.md
- **评论时间**: 1个月前

我不是很清楚为什么。是数据集本身的原因还是ai的原因。这类mdl的字段ai很喜欢给你来个rank
这里给出的例子大部分都逃不开这个rank的构造。我能不能理解为这是因为ai也很喜欢在截面上进行对比呢？当然如果佬您有其他的例子能体现ai对于其他类型数据集是否有较好的表达式构建的话，还劳烦您分享一下
-----------------------------------------------------------来自传奇耐打王的疑问-----------------------------------------------

---

### 探讨 #48: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 关于ts_decay_linear的妙用.md
- **评论时间**: 4个月前

这才是有价值的帖子啊我的天。对于一个操作符的深刻且全新的理解。也帮助我打开了对这个操作符的认知。看来在出现数据缺失的时候，或者0覆盖过多时，是不是也可以用这个操作符来进行回填覆盖？实在是太具有借鉴意义了。
==================================深度求索==========================================

---

### 探讨 #49: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 关于ts_decay_linear的妙用_38021301172759.md
- **评论时间**: 4个月前

这才是有价值的帖子啊我的天。对于一个操作符的深刻且全新的理解。也帮助我打开了对这个操作符的认知。看来在出现数据缺失的时候，或者0覆盖过多时，是不是也可以用这个操作符来进行回填覆盖？实在是太具有借鉴意义了。
==================================深度求索==========================================

---

### 探讨 #50: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 减少无效回测经验分享.md
- **评论时间**: 7个月前

a - b不完全等于-（b - a），这个我实践中有遇到
同样，操作符不能完全按照定义来复现，这个确实有待考究

---

### 探讨 #51: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 减少无效回测经验分享_36248601073175.md
- **评论时间**: 7个月前

a - b不完全等于-（b - a），这个我实践中有遇到
同样，操作符不能完全按照定义来复现，这个确实有待考究

---

### 探讨 #52: 关于《利用Gemini从0到1手搓IND区alpha尝试经验分享》的评论回复
- **帖子链接**: [Commented] 利用Gemini从0到1手搓IND区alpha尝试经验分享.md
- **评论时间**: 7个月前

因为很多人都知道这是一个非常容易圆顶的字段。当时我单字段回测就放弃了。没想到佬还能起死回生，真的太有说法了

---

### 探讨 #53: 关于《利用Gemini从0到1手搓IND区alpha尝试经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 利用Gemini从0到1手搓IND区alpha尝试经验分享_36444272754711.md
- **评论时间**: 7个月前

因为很多人都知道这是一个非常容易圆顶的字段。当时我单字段回测就放弃了。没想到佬还能起死回生，真的太有说法了

---

### 探讨 #54: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化.md
- **评论时间**: 7个月前

我一直都想有一个ai全自动流程的因子生产程序，只能说看到这样的开源代码真的是太过于兴奋了，大佬的含金量还在上升！！！这份代码我会非常认真的学习和借鉴的！

---

### 探讨 #55: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化_36196107273879.md
- **评论时间**: 7个月前

我一直都想有一个ai全自动流程的因子生产程序，只能说看到这样的开源代码真的是太过于兴奋了，大佬的含金量还在上升！！！这份代码我会非常认真的学习和借鉴的！

---

### 探讨 #56: 关于《新人建议，挖不出因子时善用中性化设置，以亚太地区slow_factors为例，RISK数据集出货率很高》的评论回复
- **帖子链接**: [Commented] 新人建议挖不出因子时善用中性化设置以亚太地区slow_factors为例RISK数据集出货率很高.md
- **评论时间**: 7个月前

@ [WT26072](/hc/en-us/profiles/32762213262103-WT26072) 
肯定不是，我用户阶段三百五，usa照样交，因子是挖不完的。

---

### 探讨 #57: 关于《新人建议，挖不出因子时善用中性化设置，以亚太地区slow_factors为例，RISK数据集出货率很高》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 新人建议挖不出因子时善用中性化设置以亚太地区slow_factors为例RISK数据集出货率很高_36064174250519.md
- **评论时间**: 7个月前

@ [WT26072](/hc/en-us/profiles/32762213262103-WT26072) 
肯定不是，我用户阶段三百五，usa照样交，因子是挖不完的。

---

### 探讨 #58: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 有大佬知道新的那个Brain python的里面的brain工具包在哪里下载不.md
- **评论时间**: 1个月前

我个人的建议还是不要下载。这些代码都是非常值得学习的。佬您可以先自己尝试一下能不能把这个代码完全理解透，然后自己在自己本地的编辑器上复现。我很深刻的记得当时的一二三阶代码我就是这么做的。一次复现能让你理解非常多的内容，也能让你对现有的代码框架焕发很多全新的思考与疑问
-----------------------------------------来自传奇耐打王的小建议----------------------------------------------------

---

### 探讨 #59: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 有大佬知道新的那个Brain python的里面的brain工具包在哪里下载不_40431103477527.md
- **评论时间**: 1个月前

我个人的建议还是不要下载。这些代码都是非常值得学习的。佬您可以先自己尝试一下能不能把这个代码完全理解透，然后自己在自己本地的编辑器上复现。我很深刻的记得当时的一二三阶代码我就是这么做的。一次复现能让你理解非常多的内容，也能让你对现有的代码框架焕发很多全新的思考与疑问
-----------------------------------------来自传奇耐打王的小建议----------------------------------------------------

---

### 探讨 #60: 关于《痛失GM，新手的Q1总结经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 痛失GM新手的Q1总结经验分享_40153456172567.md
- **评论时间**: 1个月前

说实话，我真的不觉得d0和cb涨涨跌跌有什么关系
我也开了d0，但我的cb不是因为d0下跌的。而现在我也不再害怕做d0。换个角度来说，我甚至觉得d0是帮助你点塔的关键。恰逢这个季度又有d0的主题。d0真的没什么不好的。
我希望我们还是更本质的从自己挖掘因子和选因子的角度来思考问题。我也曾经和你一样，是一个冲击gm失败的人。只能说耐心一定会成功‘
祝你早日gm
-------------------------------------------------来自传奇耐打王的点赞-----------------------------------------------------------------

---

### 探讨 #61: 关于《稳稳拿下gm，combine到六维的耕耘经验经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 稳稳拿下gmcombine到六维的耕耘经验经验分享_40294373064855.md
- **评论时间**: 1个月前

只能说看着好兄弟你的cb从一开始的负到现在远远超过我，我心里是由衷的佩服。当时陪你一起复盘的时候我实在没看出来你提交的因子有什么问题，因此也是不断的鼓励你继续坚持下去做。到了这个季度我俩都成功gm，只能说登上山顶之后回头，满路崎岖，鲜花盛开。愿你和我继续在gm的道路上不断的前进
-----------------------------------------------来自传奇耐打王的点赞------------------------------------------------------------------------

---

### 探讨 #62: 关于《解决 Codebuddy code 迭代回测alpha时突然停下的方法》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 解决 Codebuddy code 迭代回测alpha时突然停下的方法_40236868764567.md
- **评论时间**: 1个月前

那请问佬是否有尝试过通过将一段长的prompt换成多个数个小的prompt来分解长任务或者复杂任务来解决这个停下的问题呢？还是说这个问题就只能通过本质的框架修改进行解决？
希望佬能给出实例化的解答
------------------------------------------来自传奇耐打王的小疑问-----------------------------------------------------------------------

---

### 探讨 #63: 关于《连续12天手搓出pc<0.3的SA是一种什么样的体验！！！经验分享》的评论回复
- **帖子链接**: [Commented] 连续12天手搓出pc03的SA是一种什么样的体验经验分享.md
- **评论时间**: 7个月前

佬，我看刀你的select里都有pc<0.45这样的高要求语句，是不是本身您提交的因子的pc就比较低？就拿我asi地区来对比:

我总共有75个因子：


> [!NOTE] [图片 OCR 识别内容]
> 鬯嗨C
> Simulate
> Alphas
> Learn
> Data
> 罟
> Labs
> Genlus
> 舀 Competitions [4)
> Community
> Refer
> friend
> Multi-Simulaton
> Multi-Simulaton
> Multi-Simulaton
> Super Simulation
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> A5I/01/MINVOLTM
> Selected Alphas
> 75 Alphas have been selected
> Vewall
> Selection Expression
> OWn
> Nam
> Unierse
> TUINOVeT
> Ftness
> Returs
> Drawdown
> Margin
> aROTIMOUs
> NINVOLIW
> 125
> 1.554
> 6974
> 7.21*
> 89.315600
> ERONNMOUs
> NINVOLIN
> 084
> 0.73
> 5.541
> 842*
> 104.37500
> anOJMOUs
> NINVOLIW
> 251
> 1.754
> 1114
> 1.75*
> 17.325600
> EROTITOUs
> NINVOLIW
> 2.12
> 3.324
> 554
> 55北
> 34.085600
> aRONNMOUs
> NINOLIN
> 4
> 5034
> 484*
> 30*
> 19.355220
> EROTITOUs
> NINVOLIW
> 2.12
> 934
> 30北
> 3.74*
> 53.125600
> RunSJcon
> ASI_1_EQUITY_MINVOLIM_mdlzGdpsl_stepz
> NINOLIN
> .03
> 5.551
> 6-34
> 3.125
> 22.7553o
> ERONNMOUs
> NINVOLIN
> 17
> 3-
> 3.331
> 31
> 22.03530
> Combo Expression
> aROTIMOUs
> NINVOLIW
> 1.71
> 934
> 1.10
> 5214
> 39北
> 53.9456p0
> ERONNMOUs
> NINVOLIN
> 1.11
> 0.73
> 5.351
> 83北
> 100.23500
> Properties
> SIMJIate -9save
> Name
> Category
> CUrrentlanonymOUs
> NOne
> Tags
> Color
> Selectaddtags
> None
> Conetis Nphain a newtab
> Short descriptions Ofyour Selection Expression and Combo Expression are required tO submit this SuperAlpha
> Simulate
> Visualization
> 12~3~
> 一
> 23333 ^
> TC』 +
> Chec Swbmission
> Swbmft Npha
> Sharpe


当我取pc<0.45时我就只有十个因子


> [!NOTE] [图片 OCR 识别内容]
> 鬯嗨C
> Simulate
> Alphas
> Learn
> Data
> 罟
> Labs
> Genlus
> 舀 Competitions [4)
> Community
> Refer
> friend
> Multi-Simulaton
> Multi-Simulaton
> Multi-Simulaton
> Super Simulation
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> A5I/01/MINVOLTM
> Selected Alphas
> 10 Alphas have been selected
> Vewall
> Selection Expression
> Own && prod_correlation
> 8.45
> Nam
> Universe
> TUITOVeT
> Ftness
> Returns
> Drawdown
> Margin
> aROTIMOUs
> NINVOLIM
> 1.24
> 0251
> 0.93
> 3.0195
> 65兆
> 26.615600
> ERONNMOUs
> NINVOLIM
> 15
> 13.7730
> 1.23
> 11.1291
> 13.61光
> 45oo
> ASI_T_EQUITY_MINOLIW_analystlzJps
> Stepl
> NINVOLIM
> 13.2951
> 0.79
> 10.1893
> 11.13d
> 11.135600
> JSI_T_EOUITY_MINOLII_TSISJPsI_SLEDT
> NINVOLIM
> 1.24
> 7.2455
> 23.5093
> 33.35光
> 64.935600
> aRONNMOUs
> NINVOLIM
> 12
> 7.15f
> 1.1793
> 2.32沁
> 11.545220
> JSI_
> EQUITY_MINUOLIN_ot455dpsl_stepl
> NINVOLIM
> 1.21
> 5.5755
> 1.79
> 27.3893
> 26.73光
> 83.315600
> RunSJcon
> aRONNMOUs
> NINVOLIM
> 5.376
> 0.56
> 1.5993
> 53
> 15.735220
> ASI_I_EOUITY_MINOLIM_TdI33Josi_StEp3
> NINVOLIM
> 1030
> 2.21
> 22.7903
> 2401沁
> 89.355230
> Combo Expression
> ASI_1EQUITY_MINIOLIM_mdl33dpsl_step2
> NINVOLIM
> 1-1
> 0650
> 0.57
> 3593
> 2.70*
> 3986o0
> ERONNMOUs
> NINVSLTN
> 1.11
> 3.313
> 35.5793
> 45.74光
> 215.55530
> Properties
> SIMJIate -9save
> Name
> Category
> CUrrentlanonymOUs
> NOne
> Tags
> Color
> Selectaddtags
> None
> Conetis Nphain a newtab
> Short descriptions Ofyour Selection Expression and Combo Expression are required tO submit this SuperAlpha
> Simulate
> Visualization
> 12~3~
> 一
> 23333 ^
> TC』 +
> Chec Swbmission
> Swbmft Npha
> Sharpe


是不是就意味着，这个方法我就很难使用了呢

---

### 探讨 #64: 关于《连续12天手搓出pc<0.3的SA是一种什么样的体验！！！经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 连续12天手搓出pc03的SA是一种什么样的体验经验分享_36116437735447.md
- **评论时间**: 7个月前

佬，我看刀你的select里都有pc<0.45这样的高要求语句，是不是本身您提交的因子的pc就比较低？就拿我asi地区来对比:

我总共有75个因子：


> [!NOTE] [图片 OCR 识别内容]
> 鬯嗨C
> Simulate
> Alphas
> Learn
> Data
> 罟
> Labs
> Genlus
> 舀 Competitions [4)
> Community
> Refer
> friend
> Multi-Simulaton
> Multi-Simulaton
> Multi-Simulaton
> Super Simulation
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> A5I/01/MINVOLTM
> Selected Alphas
> 75 Alphas have been selected
> Vewall
> Selection Expression
> OWn
> Nam
> Unierse
> TUINOVeT
> Ftness
> Returs
> Drawdown
> Margin
> aROTIMOUs
> NINVOLIW
> 125
> 1.554
> 6974
> 7.21*
> 89.315600
> ERONNMOUs
> NINVOLIN
> 084
> 0.73
> 5.541
> 842*
> 104.37500
> anOJMOUs
> NINVOLIW
> 251
> 1.754
> 1114
> 1.75*
> 17.325600
> EROTITOUs
> NINVOLIW
> 2.12
> 3.324
> 554
> 55北
> 34.085600
> aRONNMOUs
> NINOLIN
> 4
> 5034
> 484*
> 30*
> 19.355220
> EROTITOUs
> NINVOLIW
> 2.12
> 934
> 30北
> 3.74*
> 53.125600
> RunSJcon
> ASI_1_EQUITY_MINVOLIM_mdlzGdpsl_stepz
> NINOLIN
> .03
> 5.551
> 6-34
> 3.125
> 22.7553o
> ERONNMOUs
> NINVOLIN
> 17
> 3-
> 3.331
> 31
> 22.03530
> Combo Expression
> aROTIMOUs
> NINVOLIW
> 1.71
> 934
> 1.10
> 5214
> 39北
> 53.9456p0
> ERONNMOUs
> NINVOLIN
> 1.11
> 0.73
> 5.351
> 83北
> 100.23500
> Properties
> SIMJIate -9save
> Name
> Category
> CUrrentlanonymOUs
> NOne
> Tags
> Color
> Selectaddtags
> None
> Conetis Nphain a newtab
> Short descriptions Ofyour Selection Expression and Combo Expression are required tO submit this SuperAlpha
> Simulate
> Visualization
> 12~3~
> 一
> 23333 ^
> TC』 +
> Chec Swbmission
> Swbmft Npha
> Sharpe


当我取pc<0.45时我就只有十个因子


> [!NOTE] [图片 OCR 识别内容]
> 鬯嗨C
> Simulate
> Alphas
> Learn
> Data
> 罟
> Labs
> Genlus
> 舀 Competitions [4)
> Community
> Refer
> friend
> Multi-Simulaton
> Multi-Simulaton
> Multi-Simulaton
> Super Simulation
> CODE
> RESULTS
> LEARN
> DATA
> TUTORIAL
> Settings
> A5I/01/MINVOLTM
> Selected Alphas
> 10 Alphas have been selected
> Vewall
> Selection Expression
> Own && prod_correlation
> 8.45
> Nam
> Universe
> TUITOVeT
> Ftness
> Returns
> Drawdown
> Margin
> aROTIMOUs
> NINVOLIM
> 1.24
> 0251
> 0.93
> 3.0195
> 65兆
> 26.615600
> ERONNMOUs
> NINVOLIM
> 15
> 13.7730
> 1.23
> 11.1291
> 13.61光
> 45oo
> ASI_T_EQUITY_MINOLIW_analystlzJps
> Stepl
> NINVOLIM
> 13.2951
> 0.79
> 10.1893
> 11.13d
> 11.135600
> JSI_T_EOUITY_MINOLII_TSISJPsI_SLEDT
> NINVOLIM
> 1.24
> 7.2455
> 23.5093
> 33.35光
> 64.935600
> aRONNMOUs
> NINVOLIM
> 12
> 7.15f
> 1.1793
> 2.32沁
> 11.545220
> JSI_
> EQUITY_MINUOLIN_ot455dpsl_stepl
> NINVOLIM
> 1.21
> 5.5755
> 1.79
> 27.3893
> 26.73光
> 83.315600
> RunSJcon
> aRONNMOUs
> NINVOLIM
> 5.376
> 0.56
> 1.5993
> 53
> 15.735220
> ASI_I_EOUITY_MINOLIM_TdI33Josi_StEp3
> NINVOLIM
> 1030
> 2.21
> 22.7903
> 2401沁
> 89.355230
> Combo Expression
> ASI_1EQUITY_MINIOLIM_mdl33dpsl_step2
> NINVOLIM
> 1-1
> 0650
> 0.57
> 3593
> 2.70*
> 3986o0
> ERONNMOUs
> NINVSLTN
> 1.11
> 3.313
> 35.5793
> 45.74光
> 215.55530
> Properties
> SIMJIate -9save
> Name
> Category
> CUrrentlanonymOUs
> NOne
> Tags
> Color
> Selectaddtags
> None
> Conetis Nphain a newtab
> Short descriptions Ofyour Selection Expression and Combo Expression are required tO submit this SuperAlpha
> Simulate
> Visualization
> 12~3~
> 一
> 23333 ^
> TC』 +
> Chec Swbmission
> Swbmft Npha
> Sharpe


是不是就意味着，这个方法我就很难使用了呢

---

### 探讨 #65: 关于《非金融背景如何做到vf0.9+经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXA8jAcSE6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAaJodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzY3NzI0NDkzNTQ1MTktJUU5JTlEJTlFJUU5JTg3JTkxJUU4JTlFJThEJUU4JTgzJThDJUU2JTk5JUFGJUU1JUE2JTgyJUU0JUJEJTk1JUU1JTgxJTlBJUU1JTg4JUIwdmYwLTkGOwhUOg5zZWFyY2hfaWRJIikzMmNjMGU5Ni1iYzZiLTQ3ZWQtYTAwNC02NzlkMTZlMzM3NTAGOwhGOglyYW5raQ06C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxGWDI1MjE0BjsIVDoScmVzdWx0c19jb3VudGkQ--f0bb67325c3c0e97821fdff43e62fd25e63099d8
- **评论时间**: 6个月前

佬，我想知道您做五五三的sa是哪个地区的呢？可以分享一下吗

---

### 探讨 #66: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 非金融背景如何做到vf09经验分享_36772449354519.md
- **评论时间**: 6个月前

佬，我想知道您做五五三的sa是哪个地区的呢？可以分享一下吗

---
