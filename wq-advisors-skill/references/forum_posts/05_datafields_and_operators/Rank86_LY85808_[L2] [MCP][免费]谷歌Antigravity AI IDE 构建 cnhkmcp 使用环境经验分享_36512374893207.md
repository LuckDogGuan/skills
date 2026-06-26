# [MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境经验分享

- **链接**: https://support.worldquantbrain.com[L2] [MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境经验分享_36512374893207.md
- **作者**: ZY65847
- **发布时间/热度**: 7 months ago, 得票: 22

## 帖子正文

先赞后看，一键三连，需科学上网

谷歌最近正式发布新一代旗舰大模型 Gemini3，同时重磅推出全新 AI 原生集成开发环境（IDE）——Google Antigravity。免费支持Gemini 3 Pro、Claude Sonnet 4.5，以及GPT-OSS等模型。

1. Antigravity下载安装

[https://antigravity.google/](https://antigravity.google/)   根据自己的电脑选择下载的版本


> [!NOTE] [图片 OCR 识别内容]
> Google Antigravity
> Product
> Use Cases
> Pricing
> Resources
> Download
> Google Antigravity
> Experience liftoff
> with the next-generation IDE
> Download for MacOs
> Explore use cases
> Blog


2. 在Antigravity中点Log in with Google登录自己的Google账号(✈️需要使用TUN模式，系统代理是登录不上的)


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> Open Agent Manager 哕
> Login with
> Googlu
> Agent
> Authentication Required
> Please sign in。
> Antigravity
> Switch to Agent Manager
> Code with Agent
> Edit code inline


3. python环境和cnhkmcp等依赖

我使用的是在项目中创建的虚拟环境，虚拟环境的创建跟vscode一样，可以先用IDE打开或创建一个文件夹，然后再随便新建一个.py的文件夹，然后就可以在右下角看到本地的环境


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> testpy
> Open Agent Manager 侣
> testpy
> Agent
> test py
> WorldQuant
> Ask anything (lL @ to mention
> fOT WOTKTIOWS
> Planning
> GPT-OSS 1208 (Medium)
> Template Alpha Formula Generation
> 12h
> Fixing Trailing Comma
> 18h
> Understand MCP Config Usage
> 19h
> AImay make mistakos. Double-chock all generatod Codo
> 行1。列1
> 空格:4
> UTF-B
> Pytho
> 3.14.064-bit
> ntigravity
> Settings


点击这个，然后选择创建虚拟环境


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> testpy
> Oper
> testpy
> Agent
> test py
> Select Interpreter
> Selected Interpreter: Jusrllocallbinlpython3
> Create Virtual Environment。。
> It
> Enter interpreter path。
> Python 3.14.0 (venv: Venv)
> Ivenvlbinlpython
> Recommended
> 19 (fL
> Python 3.14.0 64-bit /usrllocallbinlpython3
> Global
> Ining
> Python 3.9.6 64-b Jusrlbinjpython3


根据提示创建完虚拟环境后会在当前的文件夹下看到.venv这个python环境的文件夹


> [!NOTE] [图片 OCR 识别内容]
> 资源罾理器
> WorldQuant
> [戽 己 印
> agent
> wenv
> 槟版


然后就可以在IDE的终端使用命令安装cnhkmcp

```
pip install cnhkmcp
```


> [!NOTE] [图片 OCR 识别内容]
> 问题
> 辎出
> 调试控剐台
> 终端
> 端0
> 十 ~
> ZSh
> @0  血
>  |岛 *
> SOUrCe /Users/ZyP /Documents /WorldQuant /.venv /bin/activate
> ZypoyupengdeMacBook-Air
> NorldQuant
> Source /Users/zyp /Documents /WorldQuant /.venv /bin/a
> ctivate
> Venv) ZypoyupengdeMacBook-Air
> Norldquant
> pp install cnhkc


在虚拟环境的文件夹中找到cnhkmcp


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> VenV
> l | python3.14 / site-packages
> cnhkmcp
> untracked
> APP
> c
> mCp文件论坛版2_如果原版启动
> 配置前运行我_安装必要依赖包 py
> 出
> 下例丐亏又臼BKAIN_AIpna
> 1
> 示例工作流_Alpha_explaination。。
> 示例工作流_BRAIN_G_Tips
> Dat。
> 示例工作流_BRAIN_Alpha_Impr。。
> 示例工作流_daily_report_Workfl。
> 示例工作流_Dataset_Exploratio
> arXiV_API_Tool_Manualmd
> arxiv_apipy
> forum_functions py
> platform_functions py
> sample_mcp_configjson
> User_configjson
> init_py


可以先运行一下 依赖包.py的文件安装一下

然后最好再单独安装一下email-validator这个包

```
pip install email-validator
```

因为我后面出现报错，正好问一下ai是什么原因，😂


> [!NOTE] [图片 OCR 识别内容]
> Undorstand MCP Contig 0sa98
> Error: calling "initialize": EOF 这个报错是什么意思
> Thought for 75
> Debug MCP Connection Error
> Verified that the Server now starts correctly and keeps stdout
> clean。 The "EOFI error Was caused by
> missing
> emoil-volida
> tor dependency which
> have installed
> Progress Updates
> Expandall
> Running MCP server manually
> Installing missing dependency
> Verifying MCP server startup
> Checking stdout Vs stderr
> Reporting fix to User
> 报错
> Error: calling
> initialize"
> EOF 意味著 MCP 服务器
> 进程在初始化完成前就意外退出了
> 经过排查。原因是你的 Python 环境缺少
> email-validator 体赖
> 导致脚本启动时崩溃。
> 我已经为你安装了缺失的依赖:
> pip
> install
> emqil-volidator
> 现在 MCP 服务器应该可以正常启动了
> 请重试连接 (例如重启
> Claude Desktop)


4. 配置mcp文件

在user_config.json这个文件中填写你的email和password


> [!NOTE] [图片 OCR 识别内容]
> 资源管理器 ({ E)
> User_config.json
> WorldQuant
> [戽 己 #
> Venv
> python3
> VenV
> Credentia
> [ / python3.14
> site-packages
> Pmail"
> cnhkmcp
> pasSWOT
> untracked
> apisettii
> APP
> "base
> mcp文件论坛版2_如果原版启动。。
> Vtimeout
> 配置前运行我_安装必要依赖包 py
> "retry
> 凸
> 示例参考文档_BRAIN_Alpha_
> forum
> 示例工作流_Alpha_explaination。。
> 示例工作流_BRAIN_G_Tips
> Dat。
> "headles
> 示例工作流_BRAIN_Alpha_Impr。。
> Vtimeout
> 示例工作流_daily_report_Workfl。
> 5inulatior
> 示例工作流_Dataset_Exploratio
> Ttype
> arXiv_API_Tool_Manualmd
> "instrumc
> arxiv_apipy
> "region"
> forum_functions py
> Vunivers
> platform_functions.Py
> "delay"
> "decay'
> sample_mcp_configjson
> rneutra
> User_configjson
> Itruncat
> u
> 问题
> 辅出
> 调试控蠼
> TC。
> Set
> vbase


然后打开sample_mcp_config.json,根据这个示例填写你自己环境的路径

command就是你的pyhon执行文件的路径

args就是你的platform_functions.py这个文件的路径

然后复制这些内容，按图示找到mcp_config.json这个文件


> [!NOTE] [图片 OCR 识别内容]
> Open Agent Manager 侣
> Agent
> Customizations
> MCP Servers
> Download Diagnostics
> WorldQuant
> Ask anything (lL @ to mention
> fOr WOTKfIOWS
> Planning
> Gemini
> Pro (High)



> [!NOTE] [图片 OCR 识别内容]
> Open Agent Manager 侣
> Back to Agont
> MCP Store
> Manage MCP Servers
> Search MCP serers
> Dart
> The Dart and Flutter MCP Server exposes Dart
> Flutter)
> development toolactions to compatible Al-assistant clients。
> Firebase
> The Firebase Model Context Protocol (MCPI Server gives AI-powered
> development tools the ability to Work with your Firebase projects an。
> BigQuery
> Interact with VOUF
> BigQuery data using natural language. This MCP
> SereralloWs VOU to Securely connect to YoUr datasets to search the。。
> AlloyDB for Postgresal
> Interact with yOUT AloyDB for PostgresQL data Using naturar
> anguage。
> This MCP SerVer allows yOU to Securely connect to YOUF database fo
> Spanner
> Interact with your Google Cloud Spanner data using natural language
> This MCP Server allows yoU to Securely connect to yoUr instances fO
> Cloud SQL for Postgresal
> Vand



> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> Manage MCPs
> Manage MCPs
> Manage MCP servers
> View raw contig
> Refresh
> No MCP servers installed. Clickhere to view the MCP server store


然后把之前复制的mcp配置文件粘贴到这个文件中保存


> [!NOTE] [图片 OCR 识别内容]
> ToTUUUant
> ICP_COnTIgJSOn
> Manage MCPs
> mCP_configjson
> Users
> ZVP
> gemini
> antigravity
> mcP_contigjson
> mcpServers"
> "worldquant-brain-platform"
> command"
> /Users / ZYP /Documents /WorldQuant /.venv/bin /python'
> args"
> /Users / ZYp /Documents /WorldQuant /.venv /lib /python3. 14/site-pac
> descript"
> "NorldQuant
> BRAIN Platfomm MCP Server
> Comprehen


返回Manage MCPs,点Refresh刷新一下就可以看到我们配置好的MCP了


> [!NOTE] [图片 OCR 识别内容]
> Manage MCPs
> ICP
> configjson
> Manage MCP servers
> 100 tools
> View raw config
> Refresh
> WOF。
> Worldquant brain
> Configure
> Enabled
> brain-  40140
> platform
> plat
> 1.authenticate
> Authenticate with WorldQuant BRAIN platform. This is
> the first step inany BRAIN Workflow。 You must authenticate
> before Using any other tools. Args: emajl: Your BRAIN
> platform email address (optiona
> in config Or
> .brain_credentials) password: Your BRAIN platform
> password (optional i in config Or .brain_credentials)
> Returns: Authentication result with User info and
> permissions
> 2. Value_factor_trendScore
> Compute and return the diversity score for REGULAR alphas
> 问题
> 输出
> 调试控剐台
> 终端
> 端0
> ZSh
> 0  血
> n


5. 开始使用

这样我们就配置好了自己的mcp，让我们来测试一下吧

```
最近论坛有啥新的Alpha挖掘思路吗，帮我看看这个月热门的讨论。
```


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> Forum Hot Topics
> Open Agent Manager 侣
> Manage MCPs
> 凸 Forum Hot Topics
> Template Alpha Formula Generation
> MCP [0OI: WOTIOqUaNT Draln-DIaTTOTm
> SearCn_TOTUM_DOSIS
> Forum Hot Topics
> 13小时前
> Review
> ShOW Details
> MCP Tool: wyorldquant-brain-platform
> search_forum_posts
> WorldQuant BRAIN 论坛热门讨论总结
> ShOW Details
> 更新时间:2025年11月
> 太好了!我找到了一些最近的论坛讨论。让我再搜索
> 些更具体的
> Alpha 策略和技术讨论:
> 本月热门话题
> 搜索论坛热门讨论
> 已搜索论坛,找到多个热门讨论主题;包括 Alpha ideas。 因子挖
> 1.基于研究论文的 Alpha 开发方法
> 掘。策略优化等。正在整理总结报告。
> 热度:太女^4
> (25票)
> Files Edited
> 发布时间: 2025年3月
> Forum Hot Topics
> 核心内":
> Progress Updates
> Expand all
> 如何将学术研究论文转化为实际可用的 Alpha 策略
> 关键步骤:
> 搜索最新的 Alpha 挖掘思路和技术讨论
> 整理论坛热门讨论总结
> 1.选择合适的研究论文(关注因子。异常收益。市场微观结构)
> 2.理解论文核心观点和数据需求
> 3.在 BRAIN 平台上找到对应的数据集
> 已为您整理好论坛最新的热门讨论!包括7个主要话题:研究论文转
> 使用合适的运算符构建 Alpha 公式
> Alpha
> 遗传规划因子挖掘。全球市场因子分析
> RA组合优化
> 天候策略
> 分析师建议价值。社交媒体数据应用等。还附带了实用
> 问题
> 输出
> 调试控制台
> 终端
> 端0
> 十 ~
> ZSh
> @" 『 `|中 *
> 技巧和学习建议
> Sortedcontainers
> 2.4.0
> Soupsieve
> 2.8
> Forum Hot Topics
> Open
> SSe-starlette
> 3.0.3
> starlette
> WorldQuant BRAIN 论坛最新热门讨论总结;包括 Alpha 挖掘思路
> trio
> 因子研究。策略优化等多个方向的精选内容。
> trio Websocket
> typing_extensions
> typing-inspection
> 4.2
> Review Changes
> tZdata
> 2025.2
> Url1ib3
> Wicorn
> Ask anything (HL),@ to mention
> fOT WOTKTIOWS
> Websocket-client
> 1.9.0
> Wsproto
> 1.3.2
> Planning
> Gemini
> Pro (High)
> 1011/
> 71NLIOINNONH 
> UaCTMNIIan+


---

## 讨论与评论 (13)

### 评论 #1 (作者: JX84394, 时间: 6 months ago)

感谢分享，救了我一条老命，原来linux上可以用，windows死活连不上mcp

---

### 评论 #2 (作者: MZ23121, 时间: 6 months ago)

大佬，请问Error: calling "initialize": invalid trailing data at the end of stream.这个怎么解决啊

---

### 评论 #3 (作者: XM75236, 时间: 6 months ago)

感谢分享,用心了,非常实用

=================================================================================

Achievements are reached by hard work, but ruined by idleness; Actions are accomplished through thorough consideration, but destroyed by casual decision.​​  =================================================================================

---

### 评论 #4 (作者: ZX59167, 时间: 6 months ago)

你好 这个官方的文件可以给下吗

---

### 评论 #5 (作者: YL96878, 时间: 6 months ago)

先赞后看，养成习惯

---

### 评论 #6 (作者: XC66172, 时间: 6 months ago)

感谢佬的分享！！ 免费支持Gemini 3 Pro看到很难不心动~~

看到大家都用起MCP了自己也得加快进程加入

=======================================

FIGHITING LABUBU!

=======================================

---

### 评论 #7 (作者: AH18340, 时间: 6 months ago)

已经点赞了，又有免费mcp可以用了，用起来

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #8 (作者: XC66172, 时间: 6 months ago)

@ZY65847 大佬 我在配置的时候也遇到了这个问题，Error: calling "initialize": invalid trailing data at the end of stream.这个怎么解决啊？

---

### 评论 #9 (作者: QM70930, 时间: 5 months ago)

nice

---

### 评论 #10 (作者: JC21292, 时间: 5 months ago)

Gemini3比其他al都好用，但是有墙导致不稳定，要不停的换梯子，不然总是莫名其妙的断了，感觉很不方便。想租一台性能好的国外的云服务器，直接在国外的云服务器上跑，这样即稳定也省事，就是价格有点贵，有没有大佬这么干的。

---

### 评论 #11 (作者: HY20507, 时间: 4 months ago)

很详细的过程，点赞

---

### 评论 #12 (作者: JJ47083, 时间: 4 months ago)

感谢大佬，已实现安装，期待更多干货

---

### 评论 #13 (作者: MM27120, 时间: 3 months ago)

感谢分享 还没按照教程实操

---

