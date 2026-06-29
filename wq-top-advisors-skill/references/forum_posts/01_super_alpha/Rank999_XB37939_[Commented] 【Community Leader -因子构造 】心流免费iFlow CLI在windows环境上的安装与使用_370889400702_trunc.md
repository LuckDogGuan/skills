# 【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用

- **链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用_37088940070295.md
- **作者**: XB37939
- **发布时间/热度**: 6 months ago, 得票: 58

## 帖子正文

## 前言

最近回测数量下降，需要提高回测的时候。最近拜读了很多大佬的文章，受益匪浅。看到有人使用心流 **iFlow CLI，出货率很高。** 可惜看帖子的教程是使用的mac的。现在找到了windows如何安装和配置的方法，特此和大家分享一下。

## 安装 **iFlow CLI**

**[https://platform.iflow.cn/cli/quickstart#%E5%BF%AB%E9%80%9F%E5%AE%89%E8%A3%85](https://platform.iflow.cn/cli/quickstart#%E5%BF%AB%E9%80%9F%E5%AE%89%E8%A3%85)**

**Windows**

**有可能需要管理员权限启动cmd才能安装~**

```
1. 访问 https://nodejs.org/zh-cn/download 下载最新的 Node.js 安装程序2. 运行安装程序来安装 Node.js3. 重启终端：CMD(Windows + r 输入cmd) 或 PowerShell4. 运行 `npm install -g @iflow-ai/iflow-cli@latest` 来安装 iFlow CLI5. 运行 `iflow` 来启动 iFlow CLI
```

**此处npm安装如果较慢，则可以修改npm地址为淘宝**

```
npm config set registry https://registry.npmmirror.com/
```

**安装过程可能确实一些包，也可以直接安装即可。**

## **配置**

[https://platform.iflow.cn/cli/examples/mcp](https://platform.iflow.cn/cli/examples/mcp)

推荐使用配置文件配置

windows环境下 打开C:\Users\用户名\.iflow

找到settings.json文件

编辑文件添加 mcp配置，python和 ***cnhkmcp路径要配置你自己的***

{
  "cna": "CqLJIVqQ93sCAXjr6FG9+9iN",
  "hasIdeOnboardingBeenShown": {
    "JetBrains": true
  },
  ***"mcpServers": {*** 
 ***"worldquant-brain-platform": {*** 
 ***"command": "D:\Python\Python313\python.exe",*** 
 ***"args": [*** 
 ***"D:\Python\Python313\Lib\site-packages\cnhkmcp\untracked\platform_functions.py"*** 
 ***]*** 
 ***}*** 
 ***}*** 
}

## 启动flow

打开cmd控制面板，输入iflow命令启动。

推荐使用apikey登录

输入apikey即可进入下面页面


> [!NOTE] [图片 OCR 识别内容]
> TIow
> bai
> Tips
> for getting
> started:
> Ask questions
> edit files
> OI
> PUn
> Commands
> 2
> Be specific
> for
> the
> best results
> 3
> Create
> IFLOW.md
> files by
> /init
> Command
> and then customize your interactions with
> ilow
> 4
> /hezp
> for
> IoPe
> information
> Yolo mode
> is enabled by
> default
> Use
> ctrlty
> to
> disable
> if you need confirmation
> for each operation
> Type
> /docs
> for
> document
> and
> /demo
> for
> quick
> demo
> 9
> Paste
> images using alttv
> Click [hemel
> to join the
> iFlow Developer
> Forum
> become
> an
> iLoW
> Builder
> and share experiences
> and
> feedback !
> 恣 Tip:
> Use
> to
> execute
> shell commands
> directly
> You
> are
> running iFLow CLI
> in your
> home directory
> It
> is recommended
> to
> PUn
> in
> project-specific
> directory
> Loaded
> MCP
> SeIVeI
> Cctrltt
> to
> Thinking :Off
> Ctab
> to
> SMant
> mode
> Cshift
> tab
> alt
> to
> View
> toggle)
> toggle )
> Type your
> message
> 0I
> @path/to /file
> deepseek-v3 . 2-chat
> 100%
> Context
> left
> 0 IDE: Disconnected
> VO.4.7


在Type your message 这里输入你的ai提示语，即可使用心流cli的功能。

推荐大家参考这个大佬文章的关键词

[[Commented] 【Community Leader -因子构造 】零预算持续生成Alpha模板通用大模型的辅助应用附表达式生成指令论坛精选_36881490529815.md]([Commented] 【Community Leader -因子构造 】零预算持续生成Alpha模板通用大模型的辅助应用附表达式生成指令论坛精选_36881490529815.md)

***角色核心定位：***

***你是全球顶尖对冲基金的资深量化研究员，你的核心任务是基于给定的数据类型、运算符规则及约束条件，为发达资本市场（美国、欧洲等）生成具备强泛化性、高经济学逻辑的通用 Alpha 表达式，确保在样本内能通过10年滚动回测的严苛验证，在实践中满足实盘级风险收益特征要求。***

***任务核心约束***

***1.数据类型及适配性约束***

***必须完整覆盖pv（量价）、fundamental（基本面）、analyst（分析师）、option（期权）、news（新闻）、sentiment（情绪）、model（模型输出）7类数据，分别生成符合该类型数据的通用Alpha表达式。***

***其中，「通用型」定义：Alpha表达式需兼容不同头部数据供应商的同类字段映射逻辑，即使字段命名存在差异，也可通过基础字段属性（如 “成交量”“市盈率”“分析师评级”）完成适配，无需修改运算符逻辑。***

***2.表达式复杂度约束***

***2.1每个因子仅可调用1 个数据字段，字段统一用 {id} 表示。***

***2.2表达式中算术 / 时序 / 分组运算符的总数量≤4（运算符可从给定列表中选择，必要时可自定义运算符），最大化降低过拟合风险，；***

***2.3若使用ts_op（时序运算符），可从 [1，5，10，20，60，120，250，500] 中选择时间窗口，且窗口需与数据类型的时效性匹配（如 news/sentiment 类数据优先选≤20 的短期窗口，fundamental 类优先选≥60 的中长窗口）；***

***2.4若使用group_op（分组运算符），可从 [market，sector，industry，subindustry] 中选择组别，且组别需与Alpha逻辑匹配（如行业基本面因子优先选 industry/subindustry 中性化，全市场量价因子优先选 market 中性化）。***

***3.内在逻辑与有效性约束***

***3.1 逻辑坚实度：每个Alpha必须具备可验证的经济学底层逻辑，并且存在实证支撑需明确该类逻辑在发达市场（特别是发达国家市场，如美、欧）的历史有效性结论，如具备持续的盈利能力和普适性，能穿越不同市场周期（牛 / 熊 / 震荡市）。***

***3.2 预期表现：每个Alpha的样本内验证标准按长达10年的滚动回测中，应有望表现出高夏普比率、合理换手率、高年化收益率与低回撤的特征。***

***3.3 实施稳健性：每个Aloga能偶在实际操作中可靠，对噪音和参数具备鲁棒性。***

***3.3.1 参数敏感性低：所选时间窗口（如60日与65日）或分组方式（如industry与subindustry）的微小变动不应导致因子排名和绩效发生颠覆性变化。***

***3.3.2 数据源容错性：对数据源的细小错误（如单日数据缺失、小幅度的定义差异）有较强的抵抗能力，核心信号不会因此失效。***

***3.4 idea独特性***

***3.4.1可提供增量信息，可以提供独立于常见风险因子的增量预测能力。***

***3.4.2具备低冗余性：其信号逻辑应与Barra等主流风险模型中的风格因子保持较低相关性。***

***3.4.3 逻辑新颖性：在遵循经典理论的基础上，鼓励通过独特的运算符组合或数据视角，对已知异象进行更精细或更稳健的捕捉。***

***4.给定基础运算符清单***

***4.1 算术 / 截面运算符（arithmetic/cross_op）***

***abs、add、divide、inverse、log、multiply、sign、signed_power、sqrt、subtract、normalize、quantile、rank、scale、zscore***

***4.2 时序运算符（ts_op）***

***ts_arg_max、ts_arg_min、ts_av_diff、ts_delay、ts_delta、ts_ir、ts_kurtosis、ts_max_diff、ts_mean、ts_quantile、ts_rank、ts_scale、ts_std_dev、ts_zscore***

***4.3 分组运算符（group_op）***

***group_neutralize、group_rank、group_scale、group_zscore、group_mean、group_std_dev、group_sum、group_max、group_min***

***输出要求***

***严格按照上述任务约束和要求，每类数据至少提供10个Alpha表达式，按你对其综合优先级的降序进行排序，并说明该表达式的经济学含义及摆在逻辑，必要时可提供理论或实证支撑。***

*也可以自己研究下其他关键词。*

*运行效果：*

*
> [!NOTE] [图片 OCR 识别内容]
> TIow
> ba
> group_neutralize
> group_rank
> group_scale.
> 9LOUp_ZsCOre
> group
> Iean
> gPoup
> Std
> dev
> 严格按照上述任务约束和要求.
> 每类数据至少提供10个Alpha表达式
> 按你对其综合优先级的降序进行排序
> 并说明该表达式的经济学含叉及摆在逻辑'
> 必要时可提供理论或实证支撑。
> 我将作为全球顶尖对冲基金的资深量化研究员
> 为您生成?类数据 (pv
> fundamental
> analyst。
> option
> news
> sentime
> nt
> model ) 的通用Alpha表达式。
> 首先让我创建一个任务列表来系统性地完成这项工作
> plan Updating
> todo
> List
> (9 pending,
> in
> progress
> completed)
> Updated todo
> list
> 分析任务要求
> 理解1类数据特性和约束条件
> 生成 pv (量价)类Alpha表达式 (210个
> 生成 fundamental (基本面)  类Aipha表达式 (210个)
> 生成analyst (分析师)  类Alpha表达式 (210个)
> 生成option (期权)类Alpha表达式 (210个)
> 生成 news (新闻)类Alpha表达式 (210个
> 生成 sentiment ( 情绪)
> 类Alpha表达式 (210个
> 生成 model (模型输出)类Alpha表达式 (210个
> 验证所有表达式符合复杂度约束 (运算符s4个 )
> 整理最终输出,按优先级排序并说明经济学逻辑
> 基于任务分析,我将开始生成7数据的Alpha表达式。首先完成 pv (量价)类:
> plan Updating
> todo
> list
> (8 pending,
> 1 in
> progress ,
> completed]
> Updated todo
> list
> 分析任务要求:
> 理解?数据特性和约束条件
> 生成 pv (量价)类Alpha表达式 (210个
> 生成 fundamental (基本面)  类Aipha表达式
> (210个)
> 生成analyst (分析师)  类Alpha表达式 (210个)
> 生成option (期权〉类Alpha表达式 (210个)
> 生成news (新闻)类Alpha表达式
> (210个)
> 生成sentiment ( 情绪)
> 类Alpha表达式
> (210个
> 生成 model (模型输出) 类Alpha表达式
> (210个
> 验证所有表达式符合复杂度约束 (运算符54个)
*

*
> [!NOTE] [图片 OCR 识别内容]
> TIow
> ba
> 风险控制
> industry /sector中 性化,
> 波动率调整仓位
> 3
> 回测验证
> 10年滚动回测
> 关注样本外稳定性
> 实盘监控 :
> 跟踪因子衰减
> 定期再优化
> plan Updating
> todo
> list
> (0 pending;
> in
> progress,
> 10 completed)
> Updated todo
> list
> 分析任务要求
> 理解7数据特性和约束条件
> 生成pv (量价) 类Alpha表达式 (210个
> 生成 fundamental (基本面)类Aipha表达式
> (210个)
> 生成analyst (分析师)  类Alpha表达式 (210个)
> 生成option (期权)类Alpha表达式 (210个)
> 生成news (新闻)类Alpha表达式 (210个)
> 生成sentiment ( 情绪
> 类Alpha表达式
> (210个
> 生成 model (模型输出)类Alpha表达式
> (210个
> 验证所有表达式符合复杂度约束 (运算符<4个
> 整理最终输出,按优先级排序并说明经济学逻辑
> 总结
> 巳成功生成?类数据共70个通用Alpha表达式,每个表达式:
> 1
> 严格遵循复杂度约束 (运算符<4个 )
> 2.
> 具备坚实经济学逻辑与实证支撑
> 针对发达资本市场 (美
> 欧)  优化
> 4 .
> 预期在10年滚动回测中表现稳健
> 5 .
> 具备实盘实施可行性
> 所有表达式使用{i}占位符 ,
> 可适配不同数据供应商字段 ,
> 确保泛化性。建议优先实施顶级推荐组合, 进行严格回测验证
> 后逐步实盘部署。
> You
> are
> running
> iFLoW CLI
> in your
> home directory
> It
> is recommended
> to
> PUn
> in
> project-specific
> directory
*

*然后将模板复制下来进行回测即可。*

也可以直接让心流根据推荐的模板，生成alpha表达式


> [!NOTE] [图片 OCR 识别内容]
> 根据 brain平台EUR的字段参考上面的模板生成700个alpha
> 生成
> CSV文 件
> 我将为 BRAIN平 台 EUR市 场生成700个 Alpha表达式
> 并输出为CSVX 件
> 首先更新任务列表:
> plan Updating
> todo
> list
> (8 pending;
> in
> progress,
> 2 completed)
> Updated
> todo
> list
> 获取 BRAIN平 台EUR市 场可用数据字段
> 分析 EUR市 场'特性与数据类别
> 生成 pv (量价) 类Alpha表达式 (100个
> 生成 fundamental (基本面)  类Aipha表达式 (100个)
> 生成analyst (分析师)  类Alpha表达式 (100个)
> 生成option (期权)类Alpha表达式 (100个)
> 生成 news (新闻)类Alpha表达式 (100个)
> 生成 sentiment ( 情绪)
> 类Alpha表达式
> 生成 model (模型输出) 类Alpha表达式
> {100}
> 验证所有表达式符合复杂度约束
> 整理输出为CSV格式
> 每个区域生成100


---

## 讨论与评论 (13)

### 评论 #1 (作者: ML28213, 时间: 6 months ago)

这篇太实用了，最难是把“Windows 环境怎么从 0 跑通 写得非常清晰：等于把“装工具 + 产表达式 + 回测闭环”直接打通了，照着抄就能复现，真的是提高出货率的硬干货。

---

### 评论 #2 (作者: JL67084, 时间: 6 months ago)

感谢分享

---

### 评论 #3 (作者: JX28185, 时间: 6 months ago)

写的不错，手把手教我用上免费好用的大模型。

---

### 评论 #4 (作者: FF65210, 时间: 6 months ago)

很有帮助，已经安装好了，开始用起来了，感谢！

---

### 评论 #5 (作者: YQ84572, 时间: 6 months ago)

很详细的讲解了心流的安装使用，解决了在大会上的分享无法做到详细的问题，感谢分享
==============================================================================================

---

### 评论 #6 (作者: YZ29225, 时间: 6 months ago)

太棒了

---

### 评论 #7 (作者: CY96125, 时间: 6 months ago)

感谢作者的分享，但是其实这个面临着一个问题，到底什么样的大模型才能够真正用的得心应手，能够深度挖掘字段和操作符的含义，其实这个也是个探索的过程。

---

### 评论 #8 (作者: KG24072, 时间: 6 months ago)

win下心流的MCP的位置参数好像不对吧，你这样可以成功么？

***"mcpServers": {*** 
 ***"worldquant-brain-platform": {*** 
 ***"command": "D:\Python\Python313\python.exe",*** 
 ***"args": [*** 
 ***"D:\Python\Python313\Lib\site-packages\cnhkmcp\untracked\platform_functions.py"***

***我这里是需要"\"来区分的，用"\"会报错***

---

### 评论 #9 (作者: LQ14941, 时间: 6 months ago)

纠正一下MCP的配置：

在settings.json文件中，

需要采用两个\来作为文件目录的分隔符，不能只用单个\


> [!NOTE] [图片 OCR 识别内容]
> 'mCRSRNVerS'
> 'Worldqyant-brain-platform":
> "command": "E:IFythonerojeetllRythom?:I3IRythg:exe'
> "args": [
> 'E:IlRythonRrojeetllRythen3:I3ILibllsite packagesllcnhkmcplluntraekedllplatform_tnctigns:Ry"


感谢楼主的分享！！！！

---

### 评论 #10 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 6 months ago)

感谢大佬的iflow-cli搭建教程，我已经成功build。得力干将加一，希望能与gemini-cli一起框框出货，加油。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #11 (作者: XB37939, 时间: 6 months ago)

[KG24072](/hc/en-us/profiles/35386080156183-KG24072)   需要双斜杠，我用的双斜杠\ 但是打到论坛就变成了单斜杠，感谢指正

{

"mcpServers": {

"worldquant-brain-platform": {

"command": "D:\Users\xb\AppData\Local\Programs\Python\Python313\python.exe",

"args": [

"D:\Users\xb\AppData\Local\Programs\Python\Python313\Lib\site-packages\cnhkmcp\untracked\platform_functions.py"

]

}

}

}

---

### 评论 #12 (作者: JQ70858, 时间: 5 months ago)

配置时出了点小问题，像楼上说的是“双斜杠”，已经尝试使用了一个简单的工作流作为试验。在vscode里也用了tongyi，但是效果不行，几乎没有跑通过，也许是因为免费的功能会有所阉割？希望iflow能确实提升工作效率。

再次感谢楼主。

---

### 评论 #13 (作者: WX39795, 时间: 5 months ago)

感谢大佬的文章，拜读一下决定动手试一下，现在是倒逼自己学习进步，不然就要被时代的洪流淘汰了

---

