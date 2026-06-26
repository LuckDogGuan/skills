# 顾问 WX64154 (Rank 32) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 WX64154 (Rank 32) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: [L2] Machine Alpha 基础知识1什么是Alpha模板.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #2: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #3: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: [L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #4: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #5: replace 操作符的理解与运用
- **主帖链接**: https://support.worldquantbrain.com[L2] replace 操作符的理解与运用_35191104743447.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #6: SAC 2025 从IS第171名逆袭到最终成绩第46名——跑赢等权组合的心得体会经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] SAC 2025 从IS第171名逆袭到最终成绩第46名跑赢等权组合的心得体会经验分享_33841348895767.md
- **讨论数**: 2

第一次在论坛进行分享，本人于2025年1月成为顾问。至今一共参加过两次比赛，上一次是PPAC 2025，成绩不好，从IS前10名大幅滑落到最终成绩400多名，当时的OS表现让自己至此之后“步步战战兢兢，步步如履薄冰”。因此，本次参加SAC不敢再奢望拿到什么名次，纯粹是从本着学习做SA的目的，尝试使用not(own)的alpha去组SA。

我被分配在G4组。带着上述的目的，全程六周的主题，我都全部参加，并且尽可能都做出能够提交且自己认为值得提交的alpha，尽管有些主题感觉容易些，有些主题感觉困难些，最终都顺利完赛，共提交37个SA，包括：

按主题分，PPA 7个﹑HCAC 7个﹑ACE 6个﹑ATOM 7个﹑SIMPLE 4个﹑Risk-Neut 6个。

按地区分，USA 13个﹑GLB 9个﹑EUR 9个﹑ASI 6个。

最终获得IS 78022分，OS 105929分，OS/IS≈1.358。

对本人而言，

主题难度：

ACE>SIMPLE>HCAC>Risk-Neut>ATOM>PPA。

其中，ACE可能是有一段时间了，性能有较大的衰减，近年来有走平的趋势。对于通过selection和combo来调整pnl走势，难度比较大。SIMPLE是组出来的SA对自己的组合没有加持了，都是扣分的，但当时为了多多利用not(own)的好处去diversify自己的pool，还是把扣分的SA交上去了。

地区难度：

GLB>ASI>EUR>USA

其中，自己感到GLB难道大的原因是，自己在比赛期间Selection Limit只能是100个，超过100个，就回测出错了，有时甚至100个也回测不了，只能选50个。所以GLB SA没办法采用“大力出奇迹”的技巧，需要花更多时间去思考selection并选择合适的combo。

**在selection方面**

Selection表达式，我通常包括两个部分，选出目标alpha，以及确定目标权重。

**选出目标alpha** ，我从4个方面着手：

**一是从RA的settings着手，例如什么universe﹑neut﹑decay等；**

**二是从RA的表达式着手，例如用了什么dataset﹑多少个datafield﹑多少个operator等；**

**三是从RA的性能着手，例如turnover﹑self-cor﹑prod-cor等；**

**四是从RA的创建者着手，例如author_returns_to_drawdown﹑author_fitness等。**

**以上四组特性，进行有限的排列组合，组出基础的表达式。** 这种方法在比赛结束后也帮助我更容易找到SA。

值得注意的是，上述的四组性能对于有些主题可能会失效，例如ATOM已经限定了dataset_count==1，就无需再强调这一条件了；又例如HCAC已经限定了其RA的turnover<=10%，所以就无需再考虑turnover>10%的分层选择了。

**然后在此表达式的基础上乘以一个目标权重，这个就根据自己更看中RA哪个方面的特性，例如常见的*(1-prod_correlation)﹑*(1-turnover)等。**

**在combo方面**

比赛期间，自己主要 **选择“1”，以及单独使用或者组合使用combo_a** 。此外，自己也尝试根据在全球会议上所介绍的一些combo的方式，但发现在大多数情况下，至少在比赛期间，效果没有等权和combo_a的效果好，包括在SA的表现性能以及IS的分数方面。

除了以上一些比赛期间组SA的心得外，还有一些特别的收获，就是比赛期间一共提交了近十个跑赢了等权的SA；尤其是ACE主题，尽管其RA都比较难组出性能很好的SA，但竟然是最容易组出跑赢等权的，提交的6个ACE SA中，有4个跑赢等权的，靠这么平平无奇的combo带来巨大惊喜（这可能是得益于前辈大神们的实力，尽管性能衰减，但还是如此强大）。因为自己在大多数情况下，都极少能组出跑赢等权的。这也进一步让我感受到自己的RA与前辈们的RA的差距。

其中，提交了跑嬴等权的SA的主题有HCAC﹑ACE﹑SIMPLE ﹑Risk-Neu。而我认为最好做SA的PPA和ATOM却一直都没做出跑赢等权的SA。

另外，从地区来看在USA TOP3000﹑GLB MINVOL1M﹑EUR TOP2500都有做出跑赢等权的，但ASI就没有。

由此可见，值得探索的空间还是非常大。

以下各个主题部分跑赢的等权的SA。

**示例1：**

HCAC主题，USA TOP3000，使用了408个RA

因为HCAC无需担心高turnover，所以可能RA会在settings的decay里调整对turnover的限制。

selection是从RA的性能着手，关注decay，并强调多空平衡。

```
combo_a(alpha, nlength=250, mode="algo1")
```


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 12.5N
> 10N
> 7.5OOK
> OOOK
> 25OOK
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
> Combo Dnl
> Equal Weight Pnl



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Sharpe
> TUrnOVEI
> Fitness
> Retyrns
> DrawdoVn
> Wargin
> 8.40
> 6.789
> 9.71
> 16.709
> 0.709
> 49.279600


**示例2：**

ACE主题，USA TOP3000，使用了1000个RA

因为ACE的RA衰减较大，可能对于RA的创建者要求更高。

selection是从RA的创建者特性着手，关注其过往行为模式和产出。

```
combo_a(alpha, nlength=250, mode="algo1")
```


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 12.5M
> 1ON
> 7.5OOK
> OOOK
> Z5OOK
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
> Combo Pnl
> EqUal
> Weight Pnl



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Snarpe
> Turnove
> Fitness
> Rezurns
> Drawdown
> Margin
> 6.26
> 15.609
> 6.42
> 16.429
> 2.749
> 21.049600


**示例3：**

Risk-Neu主题，EUR TOP2500，使用了300个RA

Risk-Neu下选择范围更加丰富，强调不同dataset的多元化组合，从底层含义进行多样化。

selection是从RA的表达式着手，强调不同dataset的结合。

```
stats = generate_stats(alpha); w1 = ts_median(stats.pnl, 250);w2 = combo_a(alpha, nlength=60, mode="algo1");W3 = combo_a(alpha, nlength=120, mode="algo1");W4 = combo_a(alpha, nlength=250, mode="algo1");scale(rank(w1)) + scale(w2) + scale(w3) + scale(w4)
```


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 10N
> 7.5OOK
> SOOOK
> Z5OOK
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
> Combo Pnl
> Equal Weight Pnl



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 05
> Aggregate Data
> Snarpe
> Turnover
> Fitness
> Rezurns
> Drawdown
> Marsn
> 7.35
> 11.099
> 7.59
> 13.349
> 0.609
> 24.069600


也许得益于个别几个比较稳健的SA，才使得最终成绩有所提升。

此外，就是一直没有掌握IS该如何才能加分，到比赛的中后期，都是扣分的，或者加分/扣分交替反复，最终IS都没能过80000分，一直在78000分上下浮动。只能在以后的比赛中再进行探索了。

---

### 帖子 #7: [MCP]找灵感功能上手详解经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]找灵感功能上手详解经验分享_37113649831831.md
- **讨论数**: 20

最近mcp又出新功能了，马上尝试了一下。如下图选好你想要研究的地区和数据集就可以开始了，配置好key点击生成模板就能一键生成好用的模板
 
> [!NOTE] [图片 OCR 识别内容]
> NSA
> 细问比轱
> IOTTIII
> TOHIIILI
> 顾+5
> Alpha Inspiration Master (找灵感)
> model138
> ACcountlng-based
> MoCel
> LLM Settings
> Results
> 生成 Alpha 模板
> Factors
> 8a52 URL
> Sensitivity to the
> hps Ilapi moonshotcn1
> model140
> Model
> 正在生成模板这可能需要几分钟。
> Inflation Change
> Model
> Name
> Stock Selection DL
> model144
> Model
> kimi-kz-turbo-preview
> model
> APIKey
> model16
> Fundamental Scores
> Model
> 测试连接
> Return prediction
> model1 62
> Model
> from conference call
> ML/AI-Estimates for
> Simulation Settings
> model163
> Analysts' Factor
> Model
> Region
> Model
> USA
> Time-series
> model165
> prediction ofalpha
> Model
> Universe
> models
> TOP3000
> Research Analyst
> model17
> Model
> Delay
> Estimate Factors
> Fundamental &
> modelzo
> Model
> Technical Rank Model
> 开始新任务
> Alpha expression cannot be assigned to
> Template configured as operator with 20 variables
> Variable
> No classes, objects
> pointers
> OTfunctions
> 使用说明
> allowed
 生成之后我们直接下载到本地
 
> [!NOTE] [图片 OCR 识别内容]
> Resuits
> 生成 Alpha 模板
> 下载椟板到本地 d
> 以下给出 6 组可直接在平台"填空"的 a-Template。
> 每个模板均保留"插槽"一一用 <>括起
> -方便日后系统扫描。替换或贝叶斯调参。
> 所有模板已用现有 operator 拼装。可直接粘贴到研究环境缩译。
> 模板1:
> ML 模型残差动量 (分析师来源)
> 经济逻辑:  剥离行业共性后。取模型打分短期娈化。赌"模型新信息"尚末被价格充分反映。
> alpha
> [S_ZSCOre(
> group_neutralizel
> deltal
> backfill(<mdl165_analyst_layerl_or_layerz>;
> 63)
> industry
> 20
 
然后就可以结合mcp去使用了我的用法是直接让ai帮我去找合适的字段去填充模板 
> [!NOTE] [图片 OCR 识别内容]
> TCUC
> TU
> @1md 根据椟板内容的描述去获取合适的数据字段。你觉得合适的字段就放进
> ModellGs 数据字段列表
> 适用于模板AIpha生成
> 来;多一点没关系
> Thought for 2s
> [
> Analyst (分析师)  类特征
> 基于 IBES 数据]
> Read 1md
> Thought for Zs
> Layer 1 特征 (快速信号):
> mdl165_dlgibesnuggetschiwumodell_OIv
> 根据模板内容。需要获取以下几类数据字段:
> mdl165_dlgibesnuggetschiwumodelI_OzV
> modell65 ML/AI特征
> analystlquantlfundamental 三类;
> layer-I/layer-
> mdl165_dlgibesnuggetschiwumodell_IIv
> mdl165_dlgibesnuggetschiwumodelI_ZIV
> 2。基本面宇段
> leverage; market_cap; ROE 等
> mdl165_dlgibesnuggetschiwumodell_3Iv
> 3。成交量宇段
> dollar_Volume; advz0 等
> mdl165_dlgibesnuggetschiwumodell
> 4IV
> 让我先认证BRAIN平台。然后搜索这些字段:
> mdl165_dlgibesnuggetschiwumodelz_SIV
> mdl165_dlgibesnuggetschiwumodell
> GIV
> MCP Tool: worldquant-brain-platfomm
> authenticate
> mdl165_dlgibesnuggetschiwumodell
> 71V
> Thought for Zs
> mdl165_dlgibesnuggetschiwumodell
> BIV
> mdl165_dlgibesnuggetschiwumodell_gIv
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell_zV
> mdl165_
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> dlgibesnuggetschiwumodell
> mdl165_dlgibesnuggetschiwumodell
> MCP Tool: worldquant-brain-platform
> get_datafields
> mdl165_dlgibesnuggetschiwumodelz
> OIV
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodelz_12v
> Thought for 35
> mdl165_dlgibesnuggetschiwumodelz
> mdl165_dlgibesnuggetschiwumodelz_ZIV
> 让我继续搜索更多模板需要的字段:
> mdl165_dlgibesnuggetschiwumodel2_32V
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> ## Layer
> 特征 (愎速信号):
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell_O3v
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 13V
> Thought for 35
> mdl165_dlgibesnuggetschiwumodell_I4v
> mdl165_dlgibesnuggetschiwumodell_Z3V
> 让我再搜索fundamental类的model165字段:
> mdl165_dlgibesnuggetschiwumodell_33V
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 43V
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 44V
> 07]C
> 4105 CITOT +suT7 !
> ThOINht fom
 
然后根据选出来的字段往wqb里面的模板里面去选，选好之后就像下面这样
 
> [!NOTE] [图片 OCR 识别内容]
> 示例
> 双重中性化:以Analyst15为例
> 组间比较_GLB_topdiv
> 组间比较_9lb_topdiv_anl15
> 顾问分析示例
> Expression Editor
> Decode 
> Templates
> Expression Editor 
> Clear
> Configure Template: <modelA_layerl/>
> Detected Templates
> Operator
> 〈modelA_layerIl> (20)
> ZSCore(ts
> delta
> grOUP_
> ZsCOre
> 〈modeln
> Enter
> COIIa
> -separated list Of operators forthe modelA_layerl
> DalaField
> Other
> template:
> mdl165_dlgibesnuggetschiwumodelz_OlV
> 〈dayIl〉 
> mdl16s_dlgibesnuggetschiwumodelz_
> 121
> mdl165_dlgibesnuggetschiwumodelz
> DalaField
> Other
> mdl165_dlgibesnuggetschiwumodel2
> 2IV
> mdl165_dlgibesnuggetschiwumodelz_32 
> 〈day2/〉 
> Choose Operators Trom BRAIN
> DataField
> OtheT
> 11
> Grammar Rules
> 12
> CanCel
> Apply
> 13
> Block comments for multiple lines
> 14
> 15
> Statement separator (not needed for
> last line)
> 17
> Last statement is the Alpha expression for
> 18
> BRAIN simulator 
> Alpha expression cannot be assigned to
> Template configured as operator with 20 variables
> Variable 
> No classes; objects; pointers
> functions
> 使用说明
> allowed
 
然后一键开始回测就好啦

---

### 帖子 #8: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Lucky】为七十二变加上WQB回测配置--进行批量回测经验分享_36864734537879.md
- **讨论数**: 6

72 变是一个十分好用的工具，但是生成的 json 是没有回测配置的

> e.g.

> 
> [!NOTE] [图片 OCR 识别内容]
> 人9OOJIV
>  ]
> ATa_geVe4teU0133101131301
> "group_neutralize (rank(ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry)"'
> "group_neutralize( rank (ts_backfill (workforce_pillar_composite_score,
> 30) ) ,
> industry )
> "group_neutralize (rank(ts_backfill(anl8l_confidence_level_percent , 30)), industry)
> "group_neutralize ( rank (ts_std_dev (mdl177_liqcoeff,
> 21)
> /
> ts_mean (mdl177_liqcoeff
> 126) ),
> industry)",
> "group_neutralize ( rank
> ts_backfill(sustainability_sector_percentile,
> 30) ) ,
> industry)


为了提升回测效率，设计了一个脚本，将七十二变生成的 json转换成成 WQB 能直接回测的带回测配置的json

> e.g.
> 
> [!NOTE] [图片 OCR 识别内容]
> "type"
> 
> IREGULAR"
> settings":
> {
> "instrumentType":
> IEQUITYI
> 11
> "region":
> IND"
> Iuniverse":
> ITOP5OO"
> "delay":
> 1,
> "decay":
> 5 
> Ineutralization":
> IFASTI
> Itruncation": 0.08,
> 'pasteurization":
> ION"'
> ItestPeriod":
> IIPOYOMII
> "unitHandling":
> IVERIFYI
> "nanHandling
> IOFFI
> 11
> "language"
> 
> FASTEXPR"
> IVisualization":
> false
> }
> regular":
> "group_neutralize ( rank (ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry )
> Ivariant":
> "FASTI


设置好回测配置 & 文件输入输出的路径之后，即可生成可直接在 WQB 回测的 JSON。即可批量回测七十二变输出的变体了。

以下是实现代码

```
import jsondef convert_expressions(input_file, output_file, custom_settings):try:withopen(input_file, 'r') asf:expressions=json.load(f)output_data= []forexprinexpressions:alpha_object= {"type": "REGULAR","settings": custom_settings,"regular": expr}output_data.append(alpha_object)withopen(output_file, 'w') asf:json.dump(output_data, f, indent=2)print(f"Successfully converted {len(expressions)} expressions.")print(f"Output saved to '{output_file}'")exceptFileNotFoundError:print(f"Error: Input file not found at '{input_file}'")exceptjson.JSONDecodeError:print(f"Error: Could not decode JSON from '{input_file}'")exceptExceptionase:print(f"An unexpected error occurred: {e}")if __name__ == "__main__":# --- 请在这里自定义参数 ---# --- 以下为示例参数 ---default_settings= {"instrumentType": "EQUITY","region": "IND","universe": "TOP500","delay": 1,"decay": 5,"neutralization": "FAST","truncation": 0.08,"pasteurization": "ON","testPeriod": "P0Y0M","unitHandling": "VERIFY","nanHandling": "OFF","language": "FASTEXPR","visualization": False}INPUT_JSON_PATH='七十二变/输出/文件.json'OUTPUT_JSON_PATH='加上回测配置/文件/的输出路径.json'convert_expressions(INPUT_JSON_PATH, OUTPUT_JSON_PATH, default_settings)
```

---

### 帖子 #9: 【分析】Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析
- **主帖链接**: [L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析.md
- **讨论数**: 4


> [!NOTE] [图片 OCR 识别内容]
> Wotloquant 启动 !
> 分析1
> 交一个怎样的 & 能提升六维数据之定性定量分析
> IL47973
> 罗超林


[图片 (图片已丢失)]

在定性定量分析六维数据之前，如果你还不知道啥是genius等级和六维数据，建议去看以一下
 [【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板 – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享.md)  这一篇帖子，有解释了genius定级优胜制和六维数据字面意思，为此帖子做铺垫，和有几率增强六维某些数据的小tips；
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

### 帖子 #10: 【分析】Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析
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

### 帖子 #11: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 959

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #12: 【日常生活贴】我的量化日记第三季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **讨论数**: 742

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #13: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #14: 【日常生活贴】我的量化日记第二季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **讨论数**: 930

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #15: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #16: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #17: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **讨论数**: 37


> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN]([Commented] 【插件】Genius Rank分析代码优化_29496672188951.md) 
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

### 帖子 #18: 【Alpha 模板】分析师预期的动态估值因子
- **主帖链接**: 【Alpha 模板】分析师预期的动态估值因子.md
- **讨论数**: 7

半个月以来成功提交的Regular alpha公式拆解rtk_ptf_lowThe Lowest of Price Target分析师目标价最低值比率含义 该比率衡量“最低预期价格 / 市值”，可能反映：估值安全边际：比率越高，说明当前市值相对于最低预期价越低，可能被低估。反转信号：若该比率极低，可能预示价格超卖，未来有反弹可能。时间序列变化：ts_delta(x, 66)计算变量x在过去 66个交易日 的变化量分位数分组：quantile(x)将变量x的值按分位数分组策略逻辑：计算财务比率：用最低预期价格除以市值，得到估值安全边际。时间序列变化：观察该比率在66天内的变化方向（上升/下降），可能是为了捕捉市场对估值的重新定价。分位数分组：在全市场股票中，根据上述变化值分组，选择变化最大的（如上升最多）做多，变化最小的（如下降最多）做空。泛化模板<cross_sectional/>(<ts_op/>(<analyst/>/<pv1/>,<days/>))其他应用举例usa地区：

---

### 帖子 #19: 【Alpha 模板】分析师预期的动态估值因子
- **主帖链接**: https://support.worldquantbrain.com【Alpha 模板】分析师预期的动态估值因子_35026706128279.md
- **讨论数**: 7

半个月以来成功提交的Regular alpha


> [!NOTE] [图片 OCR 识别内容]
> ATV
> Created 09/14/2025 EDT
> anonymoUs
> Add Alphato
> Uist
> Code
> IS Summary
> Period
> quantile(ts_delta(rtk_ptg_low / cap,
> A Power Pool Alpha
> 郑 Resular Alpha
> Pyramid -heme: EURIDTIPV *1
> Pyramid -heme: EURIDTIANALYST X1 -
> Aggregate Data
> Sharpe
> TCnOE
> Timas
> Retrm
> UCaOT
> Marein
> Simulation Settings
> 1.97
> 8.609
> 1.42
> 6.50%
> 2.63%
> 15.129600
> Instrument Type
> Region
> Unierse
> LangUaqe
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> EqU
> EUE
> TOFZSNJ
> Fast Expression
> 3.03
> Sbinlusry
> Verif
> Year
> TUINOVeT
> Ftness
> Returns
> Drawdown
> Margin
> Count
> Short Cownt
> 2713
> 1.55
> 53
> 3.393
> 313
> 321:
> 717
> 704
> 271-
> ._
> 53:
> -4:1
> 2.141
> 35:
> 755
> Clone Alpha
> 2715
> 1.23
> 59*
> 5593
> 537
> 3.35:
> 775
> 755
> 2715
> 2.5
> 5.7:
> .5393
> 1.4193
> 二:
> 776
> 752
> 2317
> 1.77
> 13
> 1093
> 1.3703
> 10.71:
> 313
> 3
> N Chart
> Prl
> 2713
> -3:
> 1.13
> 1.3193
> 2.4593
> 1.51:
> 345
> 557
> 2319
> 3.00
> 76
> 2.1
> 10.553
> 31
> -.31:
> 793
> 2320
> 2.72
> 93
> .3
> 13.-31
> 2.53
> 5:
> 779
> 750
> 2721
> 5.13
> 2.4593
> 1.23:
> 7-
> 792
> OOOK
> 2022
> 1.70
> 3:
> 7.1293
> 2.251
> 1.17:
> 717
> 725
> 2323
> 1.91
> 75
> .53
> -51
> .31
> 5:
> 713
> 55
> OOOK
> Risk neutralized
> 拖 至
> Aggregate Data
> Sharpe
> TUITMTTIE
> Fitness
> ReTUITn
> TaOCII
> Warain
> 2.24
> 8.609
> 1.39
> 4.80%
> 2.579
> 11.169600
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
> Sharpe
> Lono


#### **公式拆解**

**rtk_ptf_low** The Lowest of Price Target

分析师目标价最低值

比率含义 该比率衡量  **“最低预期价格 / 市值”** ，可能反映：

- **估值安全边际** ：比率越高，说明当前市值相对于最低预期价越低，可能被低估。
- **反转信号** ：若该比率极低，可能预示价格超卖，未来有反弹可能。

#### **时间序列变化：**

#### **`ts_delta(x, 66)`**  **计算变量  `x`  在过去 66个交易日 的变化量**

#### **分位数分组： `quantile(x)`**

**`将变量x的值按分位数分组`**

**策略逻辑：**

计算财务比率：用最低预期价格除以市值，得到估值安全边际。

时间序列变化：观察该比率在66天内的变化方向（上升/下降），可能是为了捕捉市场对估值的重新定价。

分位数分组：在全市场股票中，根据上述变化值分组，选择变化最大的（如上升最多）做多，变化最小的（如下降最多）做空。

#### 泛化模板

```
<cross_sectional/>(<ts_op/>(<analyst/>/<pv1/>,<days/>))
```

**其他应用举例**

**
> [!NOTE] [图片 OCR 识别内容]
> BRAfN
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> 凸 Competitions (5)
> Community
> Refer
> friend
> UNSUB
> Created 09/14/2025 EDT
> anonymous
> Add Alpha t0
> UISt
> Code
> IS Summary
> Period
> quantile(ts_
> diff (rtk_ptg_median /close,
> Aggregate Data
> Sharoe
> LUTTS2
> FTnEss
> REUTn
> LTaVOC
> IareIn
> 2.20
> 13.539
> 1.94
> 10.4796
> 4.2396
> 15.489600
> Simulation Settings
> Instrument Type
> Region
> Unmerse
> Language
> DeCay
> Delay
> Truncation
> Neutraliation
> Pasteurization
> NaN Handling
> Unit Handling
> MaTrade
> Year
> Turnover
> Ttness
> Returs
> Drawdown
> Marqin
> LONO Count
> Short Count
> EqUi?I
> EJ
> TOFZSJD
> Fast Expression
> 7.03
> Subinclusry
> Verify
> 2313
> 14.20
> 2.27
> 5.7
> 35
> 12.3
> 725
> 271-
> -3
> 13.535
> 3.0651
> -:
> 35
> 730
> 735
> 2315
> 201
> 13.570
> 7.5055
> 一 
> 10.355
> 790
> Clone Alpha
> 2115
> 335
> 13.591
> 3.3
> 15.3
> :
> 25.365
> 731
> 2317
> 13.03
> 1.41
> 5.031
> 94*
> .22*6
> 332
> 323
> 2313
> _33
> 13.35
> +
> 1.2050
> 73
> 15.27
> 35-
> 370
> N Chart
> Prl
> 2719
> 250
> 13.05
> 2.25
> 1.50
> 2313
> 16.25
> 319
> 2320
> 13.5-1
> 3.55
> 23.153
> 3334
> 33
> 730
> 754
> 1
> 1
> 13.3
> 1.75
> +091
> 31
> 13.5
> 733
> 795
> 2
> 73
> 13471
> 0.45
> 4.3751
> -23:
> 3-
> 72
> OOOK
> 2323
> 12.05
> -1.35
> 55
> 55:
> 1-。 4
> 706
> Risk neutralized
> Aggregate Data
> SrOe
> UIPCNeI
> TIIES
> R2tUFns
> UTawOUWT
> IareIn
> 拖抻至
> 09
> 13530
> 19
> 4 ?50n
> 050h
> 400
> Sharpw
**

usa地区：


> [!NOTE] [图片 OCR 识别内容]
> AT
> Created 09/16/2025 EDT
> anonymous
> udd Alphato
> List
> Code
> 0S Summary
> Period
> 05
> pank(ts
> product (anl14_Iow_ebitda_fy4/close
> 68)
> A Power Pool Aloha
> Pyramid theme: USAIDIIPV *1.1
> Dyramid thEME: USAIDIIANALYST *1,2
> Start Date
> Sharpe
> TUITNUE
> ima
> FSTIC =
> TCMOTI
> Marsir
> simulation Settings
> 0142172023CST
> Instrument Type
> Region
> UnNerse
> LangUage
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> EqU
> US-
> TOP3OOO
> Fast Expression
> 7.03
> RAN
> Verify
> Sharpe 60
> 125
> Sharpe 250
> 500
> 05/5 Ratio
> Pre Close Sharpe
> Pre Close Rabo
> Self Corelation
> Year
> TIOVeT
> Ftness
> Returs
> Dawdow
> Margin
> Count
> Short Cownt
> Clone Alpha
> 2713
> 1.54
> 342
> 0.97
> 4.31
> 2311
> 1.31
> 542
> 24-5
> 231-
> 0.97
> 531
> 0.45
> 3.0950
> 765
> 3.04
> 530
> 2415
> N Chart
> 2315
> 0.50
> ]
> 0.25
> 2.0950
> 395
> -5.27
> 2420
> Prl
> 2315
> 5351
> 0.50
> 593
> 574
> 3.3
> 537
> 24-7
> 291
> 21
> 1
> 5.31
> 11:
> 13.37
> 739
> 2331
> 2113
> 114
> 75
> 1.54
> 3.1
> 13:
> 10.15-
> 789
> 233
> 2719
> 1.75
> 1471
> 0.3
> 2.5751
> 705:
> 4
> 755
> 2351
> 2320
> 5]
> 1.33
> 56
> 一-:
> 233
> OOOK
> 2321
> 7.511
> 3.5751
> 3.241
> 7
> 749
> 23
> 2
> 713
> 7.75
> 2.33
> 15.0153
> 54:
> 3.75
> 333
> 拖 至此上
> 3
> 25
> 5.5
> 1
> 3
> 0.3:
> 30.320
> 937
> 2235
> 201
> 2015
> 2015
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> 2023
> Sharpe
> Sharpe
> Sharpe
> Lono
> -0


---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 26年Q1 Genius定级已更新Q2赛季加油_39728814444695.md
- **评论时间**: 2个月前


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2026-21,January 1st, 2026
> Mar-h 315t, 2026
> SJIJ
> EpErt
> Iaster
> GranTas-er
> Signals
> 276
> Reached Grandmaster
> Pyramids Completed
> 60
> Reached Grandmaster
> Combined Alpha Performance
> 2.04
> Reached Grandmaster
> Combined Selected Alpha Performance
> 0.99
> 0.01 more t0 Master
> Combined Power Pool Alpha Performance
> 2.03
> Reached Grandmaster
> Combined Osmosis Performance
> -1.06
> 1.56 more to Expert
 努力了一个季度 又一次成为了GM

================================================================================

=============================越努力，越幸运======================================

==============================================================================

---

### 探讨 #2: 关于《【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘》的评论回复
- **帖子链接**: [Commented] 【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘.md
- **评论时间**: 6个月前

非计算机专业，实在是不会用AI，不大知道能走多远

=================================================================================================================good good study==========================================

===============================day day up=============================================

---

### 探讨 #3: 关于《【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha Mining】基于 AI Agent 的全自动 Alpha 挖掘_35951496406551.md
- **评论时间**: 6个月前

非计算机专业，实在是不会用AI，不大知道能走多远

=================================================================================================================good good study==========================================

===============================day day up=============================================

---

### 探讨 #4: 关于《【Alpha模板】基于labs分析macro做出可泛化的模板经验分享》的评论回复
- **帖子链接**: [Commented] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享.md
- **评论时间**: 9个月前

to_nan的操作符权限Gold好像没有

---

### 探讨 #5: 关于《【Alpha模板】基于labs分析macro做出可泛化的模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享_34584423754263.md
- **评论时间**: 9个月前

to_nan的操作符权限Gold好像没有

---

### 探讨 #6: 关于《【Alpha灵感】借助BRAIN Labs在CHN中点亮risk72（1个字段3个atom）Alpha Template》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk721个字段3个atomAlpha Template.md
- **评论时间**: 9个月前

这曲线有点不大平滑 我有点不大敢交1 这种

---

### 探讨 #7: 关于《【Alpha灵感】借助BRAIN Labs在CHN中点亮risk72（1个字段3个atom）Alpha Template》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】借助BRAIN Labs在CHN中点亮risk721个字段3个atomAlpha Template_34715794180247.md
- **评论时间**: 9个月前

这曲线有点不大平滑 我有点不大敢交1 这种

---

### 探讨 #8: 关于《【⚡️VF0.77，单alpha60刀分享⚡️】活动主题+高fitness+低PC或是base payment的版本答案经验分享》的评论回复
- **帖子链接**: [Commented] 【VF077单alpha60刀分享】活动主题高fitness低PC或是base payment的版本答案经验分享.md
- **评论时间**: 8个月前

牛逼 我见到这种只有5年数据都是直接放弃的

---

### 探讨 #9: 关于《【⚡️VF0.77，单alpha60刀分享⚡️】活动主题+高fitness+低PC或是base payment的版本答案经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【VF077单alpha60刀分享】活动主题高fitness低PC或是base payment的版本答案经验分享_35332601368215.md
- **评论时间**: 8个月前

牛逼 我见到这种只有5年数据都是直接放弃的

---

### 探讨 #10: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: [Commented] 【插件】Genius Rank分析代码优化.md
- **评论时间**: 9个月前

6维的具体排名机制是怎么排的，每个维度的权重是相同的吗

---

### 探讨 #11: 关于《【插件】Genius Rank分析代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md
- **评论时间**: 9 months ago

6维的具体排名机制是怎么排的，每个维度的权重是相同的吗

---

### 探讨 #12: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【效率王】你说你没有模板这里你多得用不完.md
- **评论时间**: 6个月前

准备升级了

反复升级还有点累

========================================================================================================Pursue scalable, repeatable opportunities rooted in probability.================

====================================================================================

---

### 探讨 #13: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **评论时间**: 6个月前

准备升级了

反复升级还有点累

========================================================================================================Pursue scalable, repeatable opportunities rooted in probability.================

====================================================================================

---

### 探讨 #14: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

12月份来了，开始我的混塔日常

又又通过group_backfill混了2塔

==================================================================================================================点塔中！！！=======================================

==================================================================================

---

### 探讨 #15: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

20251206

为了点塔 又交了一个只有5年的垃圾

=================================================================================

================================继续点塔！！！=====================================

==================================================================================

---

### 探讨 #16: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

===============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===================================

20251208

combine更新了

PPA的combine有点让人够不懂，三条线表现并不一致

===============================================================================================================HOPE HIGH COMBINE===================================

==================================================================================

---

### 探讨 #17: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

回测限10000了！！！

确实限制产出

太卷了

===================================================================================================================VF1.0=============================================

==================================================================================

---

### 探讨 #18: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

20251209

限速后的base似乎高了一点

3RA的base20刀只有1个主题

==============================================================================================================HOPE HIGH BASE=======================================

==================================================================================

---

### 探讨 #19: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记================================

20251210

又是SA < 0.3 base拿满的一天

====================================================================================================================天天拿满！！！====================================

==================================================================================

---

### 探讨 #20: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记================================

20251214

Sentiment的真难点！！！

====================================================================================================================努力点塔=========================================

=================================================================================

---

### 探讨 #21: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

==============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记====================================

20260120

昨天OS更新

今天的sa怎么组，都感觉怪怪的

还是交个三五吧

==================================================================================

================================第九季开始=========================================

==================================================================================

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

====================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==============================

5000用完了

3 + 1个GLB

==================================================================================

=================================VF1.0============================================

=================================================================================

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记================================

OS出来 GLB的OS表现不太满意

GLB的THEME 要注意质量了

==================================================================================

===================================VF1.0=========================================

=================================================================================

---

### 探讨 #24: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

OS 更新后组不出 PC < 0.3 的SA了

Base少了好多

==================================================================================

==============================VF1.0================================================

=================================================================================

---

### 探讨 #25: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

=============================20251012==============================================

4+1个alpha

Q4的第10塔点亮，继续！！！

====================================================================================================================加油============================================

---

### 探讨 #26: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

量化日记 251015

到底是没能在12点前交上，提交太慢了~~

2 + 1 alpha

=============================================================================

========Genius is one percent inspiration and ninety-nine percent perspiration.================

==============================================================================

---

### 探讨 #27: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

================2025-10-18==顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记======================================

4+1个alpha base8+刀

vf 0.74

=========坚决不要混信号、坚决不要过拟合、确保多样性、确保稳健性、要有经济学意义=========

---

### 探讨 #28: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

===============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===================================

第一次三五的SA  也首次超过5刀 vf 0.73

=======================================================================

Achievements are reached by hard work, but ruined by idleness; Actions are accomplished through thorough consideration, but destroyed by casual decision.​​  =======================================================================

---

### 探讨 #29: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记========================================

vf 更新了 0.76 base较0.74基本没什么变化

================================加油！！！=================================

---

### 探讨 #30: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)========================================

VF 0.76 的三五SA  base在6+刀左右

==========================Talk is cheap,show me the alpha================================

---

### 探讨 #31: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

===================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===============================

20251221

第八季开始！！！

今天回测7200，提交3alpha

====================================================================================================================Hope high combine==================================

==================================================================================

---

### 探讨 #32: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

SA的PC有找到一个小于0.3的

又有60刀了

=====================================================================================================================Hope high VF=====================================

==================================================================================

---

### 探讨 #33: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

回测开始5000了

极度影响产量

只有2RA

====================================================================================================================加油！！！=======================================

==================================================================================

---

### 探讨 #34: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251222

今天又是SA 60刀打卡

==================================================================================

=================================加油！！！========================================

==================================================================================

---

### 探讨 #35: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251223

AI工具还是不好用，总要有一定的回测量才行，太影响产出了

===================================================================================================================HOPE HIGH COMBINE==============================

=================================================================================

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251224

做出了个EUR的own三五！！！

===================================================================================================================加油！！！=========================================

==================================================================================

---

### 探讨 #37: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

===============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===========================-=========

没跑出好的 交了一个垃圾

====================================================================================

===================================Q4优化6维中=======================================

====================================================================================

---

### 探讨 #38: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

=================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20251226

交了一个 RA一个SA

=====================================================================================================================优化6维中=======================================

==================================================================================

---

### 探讨 #39: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

==================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

今天27刀，没有三五

======================================================================================================================加油！！！=========================================

====================================================================================

---

### 探讨 #40: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260319

4RA 9+

SA 60

OS 0.7+

===================================================================================================================点塔中！==========================================

==================================================================================

---

### 探讨 #41: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260318

4RA 6+

SA 9+

total 16

OS 0.7+

===================================================================================================================点塔中！==========================================

==================================================================================

---

### 探讨 #42: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260320

4RA 7+

SA 59

OS 0.6+

===================================================================================================================点塔！==========================================

==================================================================================

---

### 探讨 #43: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260316（回忆）

4RA 7+

SA 58+

OS 0.7+

===================================================================================================================点塔！==========================================

==================================================================================

---

### 探讨 #44: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=================================

20260321

52塔了

USA点塔中

===================================================================================================================点塔！==========================================

==================================================================================

---

### 探讨 #45: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

=============================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记=====================================

20260303

os 0.7+

ra 1个 48$

sa 59$

total 107$

=================================================================================

=================================HIGH VF AND OS==============================

===============================================================================

---

### 探讨 #46: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记==================================

20260301

ra  0个  没想到是GLB的Theme

SA 11$

=================================================================================

=================================HIGH VF AND OS==============================

===============================================================================

---

### 探讨 #47: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

===================================顾问 顾问 WX64154 (Rank 32) (Rank 32)的量化日记===============================

20260228

高os  三五 SA 57$

=================================================================================

=================================HIGH VF AND OS==============================

===============================================================================

---

### 探讨 #48: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年09月19日

今天一共提交了1个Super Alpha(s)，表现如下：

第1个：type=SUPER, region=EUR, sharp=6.13, turnover=9.26%, fitness=5.22, returns=11.89%, drawdown=1.95%, margin=26.19%%

以下是昨日SA表现与BASE：

date

vf

fitness

prod

base

0919

0.74

5.22

0.68

4.9

---

### 探讨 #49: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

20250921 5个alpha交满的第三天

===========================================

RA：GLB 1个，  ASI 2个， USA1个

SA: GLB

=======================不混信号、不过拟合、多样性、稳健性============================

---

### 探讨 #50: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025923

4个RA 没组出 super alpha

base  3.98  vf 0.74

=======================不混信号、不过拟合、多样性、稳健性============================

---

### 探讨 #51: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

我的量化流水账：2025年09月24日

4个RA， 依然组不出Super alpha

Base 4.24 vf 0.74

=======================================================================
那些凌晨三点还亮着的屏幕光，终会化作晋级榜单上闪耀...
=======================================================================

---

### 探讨 #52: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

9.25 我的量化日记第四季

4个RA ，0Super alpha

Base 5 vf 0.74

===================================================================================
===================Talk is cheap,show me the alpha=======================================

---

### 探讨 #53: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX44j9wB86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAjcBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzM0OTEzNzQ3Nzg4Njk1LS0lRTclQkIlOEYlRTklQUElOEMlRTUlODglODYlRTQlQkElQUItJUU1JTg2JUIyJUU1JTg4JUJBLWdlbml1cy0lRTclQkIlODYlRTglOEElODIlRTUlODYlQjMlRTUlQUUlOUElRTYlODglOTAtJUU4JUI0JUE1LSVFNCVCRCVBMCVFNyU5QSU4NCVFNSU4NSVBRCVFNyVCQiVCNCVFOCVCRiU5OCVFOCU4MyVCRCVFNiU4RiU5MCVFNSU4RCU4Ny0lRTclODIlQjklRTUlQTElOTQtYWxwaGElRTYlQTglQTElRTYlOUQlQkYGOwhUOg5zZWFyY2hfaWRJIik3MWJmMjVmNS1lYTY3LTRjOGEtYjIyNi0zN2E1Zjc2YWE1NmIGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDY0MTU0BjsIVDoScmVzdWx0c19jb3VudGkf--dc515f535bff21c3d15516c213be8bc24369be03
- **评论时间**: 9个月前

感谢大佬分享。给我深深上了一课，期待下节。想知道大佬怎么把combine刷的那么高

---

### 探讨 #54: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX44j9wB86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAjcBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzM0OTEzNzQ3Nzg4Njk1LS0lRTclQkIlOEYlRTklQUElOEMlRTUlODglODYlRTQlQkElQUItJUU1JTg2JUIyJUU1JTg4JUJBLWdlbml1cy0lRTclQkIlODYlRTglOEElODIlRTUlODYlQjMlRTUlQUUlOUElRTYlODglOTAtJUU4JUI0JUE1LSVFNCVCRCVBMCVFNyU5QSU4NCVFNSU4NSVBRCVFNyVCQiVCNCVFOCVCRiU5OCVFOCU4MyVCRCVFNiU4RiU5MCVFNSU4RCU4Ny0lRTclODIlQjklRTUlQTElOTQtYWxwaGElRTYlQTglQTElRTYlOUQlQkYGOwhUOg5zZWFyY2hfaWRJIik3MWJmMjVmNS1lYTY3LTRjOGEtYjIyNi0zN2E1Zjc2YWE1NmIGOwhGOglyYW5raQs6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDY0MTU0BjsIVDoScmVzdWx0c19jb3VudGkf--dc515f535bff21c3d15516c213be8bc24369be03
- **评论时间**: 9个月前

感谢大佬分享。给我深深上了一课，期待下节。

想知道大佬怎么把combine刷的那么高

---

### 探讨 #55: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **评论时间**: 9个月前

感谢大佬分享。给我深深上了一课，期待下节。

想知道大佬怎么把combine刷的那么高

---

### 探讨 #56: 关于《看到好多同期已经拿到顾问协议了，想问问有多少人没有，又是什么原因？》的评论回复
- **帖子链接**: [Commented] 看到好多同期已经拿到顾问协议了想问问有多少人没有又是什么原因.md
- **评论时间**: 1年前

可我都交到67个了 还没收到顾问协议

---

### 探讨 #57: 关于《看到好多同期已经拿到顾问协议了，想问问有多少人没有，又是什么原因？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 看到好多同期已经拿到顾问协议了想问问有多少人没有又是什么原因_31041301082007.md
- **评论时间**: 1年前

可我都交到67个了 还没收到顾问协议

---

### 探讨 #58: 关于《高VF的经验和VF崩盘的反思（0.99>0.93>0.99>0.98>0.97>0.7）经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 高VF的经验和VF崩盘的反思09909309909809707经验分享_41021984423063.md
- **评论时间**: 16天前

同交553 目前vf坐牢中

0.99-0.99-0.98-0.88-0.6

还是交三五吧

============================553还是少交==============================================

====================================================================================

---
