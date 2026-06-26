# 使用Gemini CLI创建可能有效的模板经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 使用Gemini CLI创建可能有效的模板经验分享_33223735552407.md
- **作者**: OB53521
- **发布时间/热度**: 1年前, 得票: 69

## 帖子正文

最近Google推出了Claude Code的竞品Gemini CLI，相比于Cluade好处在于Gemini是免费的，缺点在于它是免费的。

大家只需要一行代码就可以在自己电脑上安装使用

```
npm install -g @google/gemini-cli
```

安装完成后选择自己喜欢的主题，然后进行账户的登陆即可开始使用。

> 如果出现无法登陆的情况，可以尝试打开TUN模式


> [!NOTE] [图片 OCR 识别内容]
> Gemini
> orange
> 1H1
> "U杠
> Tips
> for getting
> started:
> 1.
> Ask questions,
> edit files,
> O1
> run
> commands
> 2
> Be specific
> for the
> best
> results。
> 3.
> Create GEMINI .md
> files
> to
> customize your interactions with Gemini:
> 4.
> /help
> for
> more
> information.
> Type Your message
> O[
> @path/to/file
> n0
> sandbox (see /docs)
> gemini-2.5-pro
> (100% context
> left )


在命令行中使用AI的好处在于它可以从更系统的层面来调用一些工具完成你指定的任务，并且几乎可以阅读所有常见的文件格式（CSV、PDF、PNG）。

通过 `@` 你可以选择要发送给它的文件，在你发送文件之后，它会调用一系列工具来进行检查并且推测你的意图（默认使用英文回复，你可以指定使用中文）。

> 右下角显示了本次对话还剩余的文本长度，你可以再新开一个对话，又回变成100%。 
> [!NOTE] [图片 OCR 识别内容]
> Gemini
> orange
> 乙H1
> 『@IX
> Tips for getting started:
> 1.
> Ask questions
> edit files,
> Or
> run
> Commands
> 2
> Be specific
> for
> the best
> results。
> 3
> Create GEMINI.md files
> to customize
> your interactions
> With Gemini:
> 4
> /help for
> more
> information:
> @Codeproject /wqb-master /multi_sim.py
> ReadManyFiles Will attempt
> to
> read
> and
> Concatenate
> files
> US
> patterns:
> Codeproject /wqb-master/multi_sim.py
> (within target directory:
> /Users/orange `)
> Excluding.
> ###
> ReadManyFiles Result (Target Dir:
> /Users /orange
> Successfully
> read
> and concatenated
> content
> from **1
> file(s) **
> **Processed Files:**
> CodeProject /wqb-master /multi_sim.py
> This script
> automates
> financial backtesting。
> It contains hardcoded credentials
> for WQB and
> an
> email account,
> Which
> is
> 3
> security
> risk:
> 工
> Can
> replace them with
> environment
> variables
> to
> make
> the script
> more
> Secure。
> Shall I proceed?
> Type your
> message
> Or
> @path/to/file
> no sandbox (see
> /doCS )
> gemini-2.5-pro (99% context
> left)
> ing



> [!NOTE] [图片 OCR 识别内容]
> @CodeProject /wqb-master /datafields_EUR_I_TOP2500.csV @CodeProject /wqb-master/operators_2025.csV
> 结合代码以及这两个文件,理解模板是如何创建的;并且尝试创建更多具有经济学含义的模板,要求:  4~5个运算符,
> 仅使用1个数据字段。创建完成后使用中文回复并解释其含义
> ReadManyFiles Will attempt
> t0
> read and
> Concatenate
> files using patterns:
> Codeproject /wqb-master /datafields_EUR_I_TOP2500.csV
> CodeProject /wqb-master /operators_2Q.
> ### ReadManyFiles Result (Target Dir:
> /Users /orange
> Successfully
> read and concatenated content from **2 file(s)*。
> *xProcessed Files:**
> CodeProject /wqb-master /datafields_EUR_1 TOP2500.cSV
> CodeProject /wqb-master/operators_2025 .cSV
> 好的,我已经分析了您的代码
> 数据字段和操作符文件。
> 首先 ,
> 我们来理解一下模板是如何创建的。
> Alpha模板的创建本质上是将数据字段
> (Data Fields)
> 作为输入,通过一系列操作符 (Operators) 进行组合和计算,从而构建出一个具有特定经济学含义的投资因子 (Alpha)
> 这个过程就
> 像是用基础食材(数据字段) 和各种烹饪手法 (操作符)来制作一道莱
> (Alpha)



> [!NOTE] [图片 OCR 识别内容]
> Gemini
> orange
> 乙H1
> 1。基本面加速因子
> (Fundamental
> Acceleration )
> 这个因子旨在寻找那些核心基本面
> (如此处的"销售收入")
> 不仅在增长;
> 而且增长速度还在加快的公司
> *表达式:
> 1
> rank(zscore(subtract (ts_delta(sales ,
> 60) ,
> ts_delay (ts_delta(sales,
> 60)
> 60)) ) )
> * 使用字段: sales (销售收入 )
> * 使用操作符:
> rank,
> ZSCOre,
> subtract, ts_delta, ts_delay
> * 经济学含义:
> * ts_delta(sales,
> 60)  计算最近一个季度〈约60个交易日) 的销售额变化量,
> 可以理解为销售的"速度"。
> * ts_delay(ts_delta(sales, 60),
> 60)  获取上一个季度的销售额变化量
> *
> subtract(.'.) 计算两个季度销售"速度"的差值,即销售的"加速度"。
> * Zscore 和
> rank 对"加速度"进行标准化和排名。
> * 核心逻辑: -个公司的销售增长在加速,
> 通常是其业务进入快速扩张期的强烈信号,
> 可能预示着未来股价的强劲表现。这个模板会给销售增长最快的公司打高分。
> 2。低波动率因子
> (Low Volatility)
> 该因子基于"低波动率异象"理论,即从历史上看 ,价格波动性较低的股票往往能提供比高波动性股票更好的风险调整后收益。
> * 表达式:
> 1
> rank (reverse(ts_std_dev(ts_delta ( log (close) ,
> 1) ,
> 20) ) )
> *  使用字段: close (收盘价 )
> *  使用操作符:
> rank,
> reverse, ts_std_dev,
> ts_deltay
> *  经济学含义:
> * ts_delta(log(close), 1) 计算每日的对数收益率 ,
> 这是衡量股票价格变化的常用方法。
> * ts_std_dev(
> 20)  计算过去一个月(20个交易日)  对数收益率的标准差,
> 即历史波动率。
> * reverse 将波动率的值取反,因为我们想要寻找波动率低的股票
> * rank 对取反后的波动率进行排名。
> *  核心逻辑:  此模板会给近期价格最稳定的股票打高分。投资者通常认为这类股票防御性更好,在市场不确定性高时可能表现更佳 c
> 3。短期价格反转因子
> (Short-term
> Reversal )
> 该因子试图捕捉短期内超卖的股票,并押注其价格将回归均值
> *表达式:
> 1
> rank(reverse(ts_zscore(close,
> 20)) )
> log



> [!NOTE] [图片 OCR 识别内容]
> Gemini
> orange
> 乙H1
> 该因子试图捕捉短期内超卖的股票,并押注其价格将回归均值
> * 表达式:
> 1
> rank( reverse(ts_zscore(close,
> 20)) )
> *  使用字段: close
> (收盘价 )
> *  使用操作符:
> rank;
> reverse,
> ts_zscore (注:  这里用了3个核心算子,
> 但逻辑清晰,如需增加可组合其他算子)
> * 经济学含义:
> *
> ts_zscore(close, 20) 计算当前收盘价在过去一个月(20个交易日)  价格序列中的Z-score值。一个很大的负值意味着当前价格远低于近期均值。
> * reverse 将Z-score取反
> 这样 ,
> 一个偏离均值最远的负值(超卖最严重)会得到一个最大的正分。
> * rank 对最终结果进行排名
> *  核心逻辑:  寻找那些价格在近期内下跌幅度远超其自身历史波动的股票。这类股票被认为是"超卖"的,根据均值回归理论,
> 它们在短期内反弹的可能性更大。
> 4。波动率调整后动量因子
> (Volatility-Adjusted Momentum)
> 经典的动量因子认为近期上涨的股票会继续上涨,
> 但这种上涨可能是由高风险驱动的
> 本因子在动量的基础上加入了波动率的考量,寻找更"健康"的上涨。
> * 表达式:
> 1
> rank(zscore(divide(ts_delta(closey  20), ts_std_dev(ts_delta( log(close).
> 1),20))) )
> * 使用字段: close
> (收盘价 )
> *  使用操作符: rank,
> Zscore, divide, ts_delta, ts_std_dev
> *  经济学含义:
> * ts_delta(close,
> 20)  计算过去一个月(20个交易日) 的价格娈动 =
> 即动量。
> * ts_std_dev(ts_delta( log (close) ,
> 1,
> 20)  计算同期的价格波动率。
> *
> divide(..) 用动量除以波动率 ,
> 得到"风险调整后"的动量,也称为夏普比率的简化形式。
> * zscore 和
> rank 对结果进行标准化和排名。
> *核心逻辑:  此模板寻找的是那些上涨趋势强劲且过程相对平稳的股票
> 相比于剧烈波动的暴涨
> 这种"高质量"的动量可能更具持续性。
> 希望这些新的模板能为您的Alpha挖掘工作提供有价值的参考。
> Type your
> message
> Or
> @path/to/file
> n0
> Sandbox
> (see
> /doCS )
> gemini-2.5-pro
> (798 context
> left)
> 109


通过AI创建出来的模板具有 **不稳定性** ，并且也不一定能出货。

我的思路是：

- 将以前交过的alpha喂给他，因为现在大家基本上都把alpha以及各种settings保存在数据库或者csv文件中，让Gemini读取就可以让它更了解如果创建出一个更好的模板
- 将一些论文、研报喂给它，让他提炼出核心思路，并且按照这个思路，结合我们的数据字段表和运算符表进行alpha表达式的创建，这样应该会更具有经济学含义

如下图所示，我选择 [论坛中的一篇论文]([L2] Research Paper Firm Life Cycle Expectation Errors and Future Stock ReturnsPinned_14111788609047.md) 下载到本地之后将pdf文件发送给Gemini，让它创建模板 
> [!NOTE] [图片 OCR 识别内容]
> ReadManyFiles Will attempt
> t0
> read
> and
> Concatenate
> files using patterns:
> Downloads /ssrn-3332513.pdf
> (within target directory:
> /Users /orange`)
> Exclud
> pattern。
> ### ReadManyFiles Result (Target Dir:
> /Users /orange
> Successfully
> read
> and
> concatenated
> content
> from
> *1 file(s)*
> *Processed Files: *
> Downloads/ssrn-3332513.pdf
> 好的,我已经仔细阅读了您提供的这篇名为 《公司生命周期
> 预期误差与未来股票收益》的学术论文。
> 核心思路提炼
> 这篇论文的核心观点是 ,
> 公司的生命周期阶段可以显著预测未来的股票收益。这种可预测性主要源于市场对不同生命周期阶段公司的系统性错误定价
> 而这种错误定价由于套利限制而得以持
> 续存在。
> 具体来说 ,
> 核心思路可以分解为以下几点:
> 1。核心发现 (The Anomaly)
> 构建一个对冲投资组合。做多 (Long)
> 成熟期公司。做空
> (Short)
> 引入期公司 ,
> 可以获得显著的超额回报。这是因为市场倾向于高估引入期公司的价值,
> 同时低估成熟期公司的价值。
> 2。错误定价的根源
> (Expectation Errors)
> * 对引入期公司的过度乐观:  投资者和分析师系统性地高估了引入期公司 (通常是年轻
> 高增长
> 高不确定性的公司) 未来的盈利能力。这些公司未来的盈利增长分布具有很大的不确定
> 性和正偏度(即,有很小的可能性获得极高的增长)
> 这使得分析师更容易为他们的乐观预测找到理由
> * 对成熟期公司的过度悲观:  相应地
> 市场对成熟。增长缓慢的公司的未来盈利能力则显得过于悲观。
> 3。错误定价的证据:
> *盈余公告效应:
> 这种错误定价的修正常常发生在盈余公告日附近。论文发现 ,
> 在发布财报时,
> 引入期公司的股价倾向于下跌 (负的超额收益)
> 而成熟期公司的股价倾向于上涨 (正的超额收益)
> * 分析师预测误差:
> 分析师对引入期公司的盈利预测误差显著为负
> (即预测值远高于实际值) ,而对成熟期公司的预测则要准确得多。这个误差会随着时间的推移和信息的披露而逐渐被修正。
> 4。套利限制 (Limits
> to
> Arbitrage)
> 为什么理性的套利者不利用这种错误定价来获利呢?  论文指出了两个主要障碍:
> *卖空约束:  引入期公司通常机构持股比例较低,
> 导致可供借贷用于卖空的股票数量少 
> 成本高,这限制了对被高估股票的套利。
> *异质性风险 (Idiosyncratic Risk)
> 引入期公司通常具有非常高的公司特有风险
> (即与市场整体相关的风险 )
> 这种高风险会阻止套利者建立大的头寸,
> 因为他们难以完全对冲掉这些风险
> ing:



> [!NOTE] [图片 OCR 识别内容]
> Gemini
> orange
> 乙H1
> *  核心思想:  论文指出成熟期公司盈利能力强且稳定,
> 而引入期公司盈利能力弱或为负。我们可以使用 "营业利润率"作为公司成熟度的代理指标
> * 使用字段 :  Op_profit_margin (营业利润率)
> *表达式: rank(ts_decay_linear(zscore (op_profit_margin) ,
> 60) )
> *  使用操作符:
> rank;
> ts_decay_linear;
> ZSCOre
> *  经济学含义:  此模板寻找那些在过去一个季度〈约60天)内,经标准化处理后
> (zscore)
> 营业利润率表现出持续稳定
> decay_linear) 的公司
> 得分高的公司是那些盈利能力强且稳定
> 的"成熟"公司,应做多; 得分低的公司是盈利能力差的"引入期"公司 ,
> 应做空_
> 这直接模拟了论文的核心多空策略
> 模板二: 分析师预期误差反转因子
> * 核心思想:  论文的关键证据是分析师对引入期公司过度乐观
> 导致负的预测误差 ,
> 而这种误差会随着时间被修正 (即股价下跌)
> 此模板旨在捕捉这种预期的"向下修正"的动量。
> *  使用字段: act_q_eps_surprisemean (平均每股收益意外 )
> *表达式: rank(reverse(ts_delta(ts_mean (act_q_eps_surprisemean,
> 4),
> 20)) )
> *  使用操作符:
> rank
> reVerse,
> ts_delta,
> ts
> mean
> * 经济学含义:  此模板计算了过去一个月(20天)分析师"平均意外"的变化 (ts_delta)
> ts mean(
> 4)代表过去四个季度的平均意外值。一个大的负向ts_delta意味着分析师的乐观情绪
> 在近期急剧降温 (或悲观情绪加剧)
> 通过 reverse取反后 _
> 这些股票会获得高分,代表做空信号
> 这与论文中预期误差修正将导致股价下跌的逻辑一致。
> 模板三: 异质性风险套利限制因子
> * 核心思想:  论文发现
> 公司生命周期策略在异质性风险高的股票中表现更强
> 高风险吓退了套利者,使得错误定价更严重。此模板直接做空那些风险急剧增加的股票。
> * 使用字段: volatility_252d (年化波动率)
> *表达式: rank(reverse(zscore(ts_delta(volatility_252d, 20))) )
> * 使用操作符:
> rank;
> reverse
> ZSCore,
> ts_delta
> * 经济学含义:  此模板寻找在过去一个月
> (20天)
> 里,年化波动率增幅最大的公司
> 根据论文的逻辑,异质性风险的急剧增加会加剧错误定价并限制套利。
> 因此,
> 该模板做空这些风险骤增的
> 股票,押注其未来表现不佳。
> 模板四:  机构持股套利限制因子
> * 核心思想:  论文指出,在机构持股比例低(难以卖空) 的股票中,做空引入期公司的策略更有效。此模板旨在捕捉"聪明钱 "流出的信号。
> *  使用字段: inst_own_I3f_latest (最新机构持股比例 )
> *表达式: rank(zscore(ts_delta(inst_own_I3f_latest, 60)))
> *  使用操作符:
> rank;
> ZSCOre,
> ts_delta
> *  经济学含义:  此模板计算了过去一个季度〈60天)机构持股比例的娈化。一个大的负值(即低分)表示机构投资者正在抛售该股票。
> 这通常被视为一个负面信号,可能预示着未来股价下跌
> 这与论文中低机构持股加剧错误定价的发现相符 _
> 希望这些基于论文核心思想构建的模板能对您有所帮助。
> Type Your
> message
> Or
> @path/to/file
>  (ts_


可以看到Gemini还是给出了很多可以尝试的模板，后续通过微调是可以出货的。

Gemini CLI的用处也不至于此，除了创建模板，还能让它帮你批量重命名文件，对于有大量照片素材的人，可以说：

> 我有很多照片素材，请你帮我批量命名，取一个合适的名字

Gemini会在查看图片之后完成任务。总之还有很多用处，留给大家去探索。

---

## 讨论与评论 (1)

### 评论 #1 (作者: 顾问 JR23144 (Rank 6), 时间: 1年前)

感谢大佬分享  不过 本地用 Gemini 是不是要用魔法呀，有时候感觉GEmini 的幻觉很重，它思考过程 是 英文的，不像deepseek 思考过程是 中文的， 还是更喜欢用deepseek 一点， 不过能创建出有用的模板还是挺好的，喂它资料生成自己的知识库。
================================VF 1.0 ========================================

---

