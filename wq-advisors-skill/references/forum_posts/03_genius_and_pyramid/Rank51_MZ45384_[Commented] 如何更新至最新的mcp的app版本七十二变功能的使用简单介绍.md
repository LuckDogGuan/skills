# 如何更新至最新的mcp的app版本+七十二变功能的使用简单介绍

- **链接**: [Commented] 如何更新至最新的mcp的app版本七十二变功能的使用简单介绍.md
- **作者**: YD80858
- **发布时间/热度**: 6个月前, 得票: 15

## 帖子正文

当前的app版本是1.5.3,具有七十二变的功能，可以在命令行运行和终端运行。


> [!NOTE] [图片 OCR 识别内容]
> (base)
> >ip show cnhkmcp
> lame
> cnhkmcp
> Tersion:
> 1 53


如果你的页面不是如下图这样，可以考虑更新至最新版本。


> [!NOTE] [图片 OCR 识别内容]
> Open Submitter
> Connected to BRAIN
> Goto Simulator
> BRAIN Expression Template Decoder
> Open Simulator_hk
> Inspiration House
>  Paper Analysis
> Specialized template decoderwith arammar checkina forexpression-like lanquage
> 七十-娈
> DataField Guide
> Run Transformer (72娈)
> 选择您想要运行 Transformer 的方式:
> Expression Templates
> Import User Templates
> Load Transformer File
> Vector Data Processing
> Nested Feature Dic
> ssidual_Vector Data
> TVR Delta Limit
> TVR Hump
> 命令行界面
> Web 界面
> samplel
> Double Neutral in Analyst15
> compare_glb_topdivmodel26 
> 传统的交互式命令行界面。
> 用户友好的 Web 表单。
> Researcher_only_analyst10_
> eUT
> Reseal
> 交互式参数输入
> 所有参数在一个表单中
> 适合熟悉命令行的高级用户
> 实时日志监控
> 结果下载
> Expressic
> rode Templates


更新也简单，请先确保你在正确的python环境中操作，在终端输入以下命令： **pip install --upgrade cnhkmcp**

你可以通过在终端输入：pip show cnhkmcp

查看当前的版本号

**七十二变功能的使用简单介绍**

**
> [!NOTE] [图片 OCR 识别内容]
> Open Submitter
> Connected to BRAIN
> Goto Simulator
> BRAIN Expression Template Decoder
> Open Simulator_hk
> Inspiration House
> Paper Analysis
> Specialized template decoder with grammar checking for expression-like language
> 七十娈
> DataField Guide
**

该功能可以对您输入ID对应的Alpha（尽量是表现好的）为基础进行衍变，产生多个不同的Alpha模板，会以JSON文件的形式保存。

如何获取Alpha的ID呢？

在Alpha列表随便点开一个，然后点击下图中的位置。


> [!NOTE] [图片 OCR 识别内容]
> ER]]
> SIUaCE
> 0卢/35
> LeaII
> Uata
> LaU5
> OeIIUS
> LOIIPEUUOIS (
> CUIIIUIIU
> N2l
> TeIU
> UNSUB
> Created 12/09/2025 EST
> Add Alpha to
> Lst
> Alphas
> Unsubmitted
> Submitted
> alpha details in newtab
> Code
> P3ge 51ze
> Out 0f
> 0,000+
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (ESTI
> Simulation
> Selecr
> Selecr
> Selecr
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
> Search
> Search
> Equity
> EUR
> TCP250
> Fast Erpression
> 003
> Fast Factors
> Verfy
> EUR_
> EQUITY_.
> Resular
> UNSUBMITTED
> 12109'2025 EST
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/0912025 EST
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/0912025 EST
> Clone Alpha
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/09/2025 EST
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/0912025 EST
> Chart
> PIL
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/09/2025 EST
> EUR_IEQUITY_.
> Regular
> UNSUBMITTED
> 12/0912025 EST
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/0912025 EST
> ZOOK
> EUR_
> EQUITY_.
> Regular
> UNSUBMITTED
> 12/0912025 EST
> 10O
> EUR_IEQUITY_.
> Resular
> UNSUBMITTED
> 12/09/2025 EST
> Size
> OUT Of 10,000
> Open
> Settings
> PJge


你就可以在新页面的最上面找到该Alpha对应的ID


> [!NOTE] [图片 OCR 识别内容]
> https://platform worldquantbrain.com/alphayOmvzznQq
> 咕 &
> 8
> WORLOOUANT
> BRAN
> Smulate
> O Alphas
> Learn
> Data
> Labs
> Genius
> Competitions (1)
> Community
> Refer
> friend


打开七十二变页面

自己 **先搞定API** ，论坛有很多帖子可以参考。之后填写自己的账号密码，在下面填上Alpha的ID，最下面的“Datafield Top N”是指你想让它产生几个模板。


> [!NOTE] [图片 OCR 识别内容]
> BRAIN Transformer (72娈)
> Backto Home
> Configuration
> Output Log
> LLI Model Name
> Hitin
> S
> bmi-kz-turbo-preview'
> LLM API Key
> LLI Base URL
> hpslapimoonshotcn
> TestLUMCoecbon
> BRAIN Username
> Fmail
> Usemame
> BRAIN Password
> Template Summary
> Load fom F =
> EII Sp2E莰J些三=
> 醯'。?璧箫黧褰黧鼹
> 士#:
> [:#-~交刁荭=兰辽L二C;
> 季工-
> 4三
> 井$ =-S-L2J;
> -; .三方:芒兰=C二
> NTr S
> 霪二-^荻 (3?豸=
> 汩芒纂产
> Alpha ID
> Datatield TOpN
> Run TTanSIOIeT
> #掣


点击run之后，等待一会便可以得到一个JSON文件，这个文件里面保存了产生的Alpha模板。

你可以点击主页的load transformer file将该模板文件加载进来，你可以点击任意一个模版进行自主化的修改。


> [!NOTE] [图片 OCR 识别内容]
> Submitter
> Connect to BRAIN
> Goto Simulator
> BRAIN Expression Template
> Open Simulator_hk
> Inspiration House
> Analysis
> Decoder
> 七十二娈
> DataField Guide 
> Specialized template decoder with grammar checking for expression-like
> language
> Expression Templates
> Show Users Only
> Export User Templates
> Import User Templates
> Load Transformer File
> Vector Data Processing
> Nested Feature Digger
> Double Neutralization
> Group Mean Residual_Matrix Data
> Group Mean Residual_Vector Data
> TVR Delta Limit
> TVR Hump
> Open
> Paper



> [!NOTE] [图片 OCR 识别内容]
> Transformer Candidates
> Transformer Candidate
> Transformer Candidate
> Transformer Candidate
> Contrarian to shorter-horizon analyst enthusiasm:
> Counts the streak of monthly EPS FY2 estimate incr.
> Penalizes rising, standardized analyst dispersion
> Transformer Candidate
> Transformer Candidate
> Short the herding nexus of revisions and price: Wh..
> Weighted regression mean-reversion: industry-neutr.
> Expression Editor
> Decode Templates


该平台的其他功能的使用，比如模板如何修改、导出、运行，请参考顾问群中的视频：“第三课：Brain Lab数据探索与Alpha策略开发”

作为新人，希望自己微薄之力能帮助大家！

---

## 讨论与评论 (13)

### 评论 #1 (作者: YB15978, 时间: 6个月前)

感谢大佬分享，能否介绍下软件的来源和大致的历史，能否介绍下软件的原理呢，

---

### 评论 #2 (作者: YD80858, 时间: 6个月前)

当前app已经版本更新到：1.7.0，添加“缘分一道桥”功能


> [!NOTE] [图片 OCR 识别内容]
> Alpha_Submitter提交器
> Open Simulator_hk
> 七十二娈
> 缘分-道桥


---

### 评论 #3 (作者: CZ16695, 时间: 6个月前)


> [!NOTE] [图片 OCR 识别内容]
> (.VenV)
> shine@home
> ~/project /quant-wqb/
> Venv/lib /python3. 12/site-packages /cnhkmcp /untracked/APP$ pip
> shoW cnhkmcp
> Name
> cnhkmcp
> Version:
> 1.7
> Summary:
> comprehensive Model
> Context
> Protocol
> (MCP )
> SerVer
> for quantitative trading platform integration
> Home-page
> https : //github . com/ cnhk / cnhkmcp
> Author
> CNHK
> Author-email:
> cnhk@example . com
> License
> Location:
> /home
> shine /project /quant-Wqb /
> Venv/lib /python3 . 12/site-packages
> Requires
> beautifulsoup4, Ixml,
> mCP,
> pandas , pydantic,
> requests,
> selenium
> Required-by:
 博主请问为什么我点击这个功能404呢 
> [!NOTE] [图片 OCR 识别内容]
> INFO : Werkzeug: 127.0.0
> [11/Dec/2025
> 14:54:02]
> "GET
> /alpha_inspector
> HTTP/I.1"
> 404
> INFO: Werkzeug: 127.0.0.1
> [11/Dec /2825
> 14:54:86一
> "GET
> /alpha
> inspector
> HTTP/I .1"
> 404


---

### 评论 #4 (作者: JY16044, 时间: 6个月前)

你好，我把cnhkmcp升级到了1.7.0之后，再打开app，也没有这个左侧的七十二变 是怎么回事

---

### 评论 #5 (作者: YB16410, 时间: 6个月前)

你好，请问七十二变这个APP怎么获取，你发出来的图片是哪里的页面呢？麻烦你了！！！谢谢你！！！

---

### 评论 #6 (作者: ZZ37826, 时间: 6个月前)

这个不是python的库吗，方便问一下这个网页是咋打开的吗？

---

### 评论 #7 (作者: YD80858, 时间: 6个月前)

*关于mcp这个app的安装：*

*1、在python环境下的终端，输入：终端输入pip install cnhkmcp*

*2、打开mcp本地目录，找到untracked文件夹，路径应该是  site-packages/cnhkmcp/untracked，应该在你python安装路径下面*

*3、找到该文件夹里的user_config.json打开编辑输入你在 **worldquantbrain** 的账号密码。*

*4、对 untracked文件中的“sample_mcp_config.json”进行配置，示例配置文件如下：args 分别是两个 mcp 文件的绝对路径，以“platform_functions.py”结尾；command 是你 python 程序的绝对路径。请根据你电脑的具体路径进行更改。*

*
> [!NOTE] [图片 OCR 识别内容]
> 氏
> 'mcpServers
> worldawant
> hrain-platform"
> Command"
> "E:
> lanaconda
> Ipython.exe
> apes
> E:
> anaconda | lLibl Isite-packages
> cnhkmcp | luntracked
> Iplatform_functions .Py'
> 」
> description"
> "WorldQuant BRAIN Platform MCP Server
> Comprehensive trading platfc
> }
*

*5、运行这个python文件安装依赖包*

*
> [!NOTE] [图片 OCR 识别内容]
> arxiv_api py
> arXiv API Tool Manual md
> forum_functions: Py
> platform_functions Py
> sample_mcP_configjson
> UISeI
> confiaison
> 配置前运行我_安装必要依赖包 Py
> 示例参考又档_BKAIN_Alpha_lest_Requirements_and_Tips.md
> 示例工作流_Alpha_explaination_workflow md
> K例丁 (乍济
> DDIAI ` Tim.
> [3+3f1o1|
> CnIorz+ion
> C」o m
*

*6、在 untracked文件夹下找到“APP”文件夹打开，找到“运行打开我.py”进行运行。*

*
> [!NOTE] [图片 OCR 识别内容]
> blueprints
> 2025/12/1113:41
> 文件夹
> custom_templates
> 2025/12/1113:41
> 文件夹
> hkSimulator
> 2025/12/1113:41
> 文件夹
> simulator
> 2025/12/128:09
> 文件夹
> static
> 2025/12/1113:41
> 文件夹
> templates
> 2025/12/1113:41
> 文件夹
> Tranformer
> 2025/12/1122:50
> 文件夹
> 缘分
> 道桥
> 2025/12/1113:41
> 文件夹
> gitignore
> 2025/12/1113:41
> Git Ignore 源文件
> 1 KB
> aCe。
> 2025/12/1113:41
> LOG 文件
> 4 KB
> mirror_config.txt
> 2025/12/1113:41
> TXT 文件
> 1 KB
> MODULAR STRUCTUREmd
> 2025/12/1113:41
> QQBrowser HTML
> 5KB
> operaters.csV
> 2025/12/1113:41
> Microsoft Excel 逗
> 14KB
> READMEmd
> 2025/12/1113:41
> QQBrowser HTML
> 12KB
> requirements.txt
> 2025/12/1113:41
> TXT 文件
> 1 KB
> rUn
> app.bat
> 2025/12/1113:41
> Windows 批处理文件
> 1 KB
> rUn
> app.sh
> 2025/12/1113:41
> SH 源文件
> 1 KB
> setup_tsinghua.bat
> 2025/12/1113:41
> Windows 批处理文件
> 2 KB
> setup_tsinghua.sh
> 2025/12/1113:41
> SH 源文件
> 2 KB
> SSrn-3332513.pdf
> 2025/12/1113:41
> Microsoft Edge PD..
> 2,034KB
> 运行打开我 Py
> 2025/12/1113:41
> JetBrains PyCharm
> 73 KB
> .log
*

*7、运行后会产生一个链接，图中的几个链接好像都可以。*

*
> [!NOTE] [图片 OCR 识别内容]
> BRALN
> Expresslon
> eIp Late
> UeCOUer
> TU LLY
> L01t1a L12e0 !
> Ready
> t0
> process
> templates
> and integrate
> With
> BRAIN
> API !
> 亏
> 十~5 +
> DDA TNI
> 3552
> TS7?+?
> 033392
> Is
> Application _
> Application
> Will
> pun
> 0[
> BRAIN
> API Integratzon
> InclUded
> n0
> separate
> proxy
> needed !
> Serving
> Flask app
> '运行打开我
> Debug
> mode
> Off
> INFO : werkzeug
> WARNING:
> This
> is
> development
> SepVer.
> 0o
> not
> USe
> i
> in
> production deployment。
> Use
> product
> Runnina
> 0n
> 311
> addresses
> (0 ,0 ,0
> 0 )
> Running
> 0[
> Running
> 0n
> INFO : werkzeug=
> Press
> CTRL+C
> to quit
*

*8、复制链接去网页打开。点击“Connect to BRAIN”输入账号密码就可以使用了。*

*
> [!NOTE] [图片 OCR 识别内容]
> Alpha_Submitter提交器
> Connect to BRAIN
> 打开回测器
> BRAIN Expression Template
> Open Simulator_hk
> Al创意工坊
> 论文分析
> Decoder
> 七十-娈
> 数据字段指南^
> Specialized template decoder with grammar checking for expression-like
> 缘分道桥
> language
> 模板空间
> 只展示用户自建模板
> 导出用户自建模板
> 导入用户自建模板
> 加载72娈生成的模板
> 载入72娈生成的表达式
*

---

### 评论 #8 (作者: WW37372, 时间: 6个月前)

查看D:\Python314\Lib\site-packages\cnhkmcp\untracked\APP  这里的app导入运行就可以了

---

### 评论 #9 (作者: LG87838, 时间: 6个月前)

大佬，最近mcp的版本更新很快，有没有办法在更新后，保留我之前的配置文件的方法，不需要手工的复制粘贴。

----------------------------------------------------------------------------------------------------

慢就是快，相信时间的力量！

----------------------------------------------------------------------------------------------------

---

### 评论 #10 (作者: 顾问 MZ45384 (Rank 51), 时间: 6个月前)

感谢大佬的分享，要是模板能一键聚合到一起再一起添加settings就更完美了。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值
======================================================================================

---

### 评论 #11 (作者: JW65774, 时间: 6个月前)

发现已经1.8.3了

---

### 评论 #12 (作者: XZ47401, 时间: 6个月前)

按照博主的步骤，可以打开七十二变了，感谢

---

### 评论 #13 (作者: YQ84572, 时间: 5个月前)

mcp工具更新迭代非常的快啊，没几天论坛就出现一批新版本的使用操作，很好的分享，关注论坛就能及时意识到工具更新和使用方法

--------------------------------------------------------------------------------------------------------------------

感谢分享，祝国区越来越好

--------------------------------------------------------------------------------------------------------------------

---

