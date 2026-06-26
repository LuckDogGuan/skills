# VSCode copilot配置MCP经验分享

- **链接**: https://support.worldquantbrain.comVSCode copilot配置MCP经验分享_34252479802007.md
- **作者**: 顾问 KZ79256 (Rank 21)
- **发布时间/热度**: 10个月前, 得票: 67

## 帖子正文

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

VSCode copilot对于大学生可以免费使用, 所以在这里就把cnhkmcp的服务配置到里面

1. 首先到github copilot申请学生认证, 这样就可以免费使用copilot了

2. 下载并安装cnhkmcp

安装cnhkmcp，cmd里直接输入

```
pip install cnhkmcp
```

3. 在左侧选择扩展, 浏览mcp,

在此处安装一个官方的mcp服务, 之后找到配置的json, 或者直接新建一个C:\Users\XXX\AppData\Roaming\Code\User\mcp.json 文件(此处的XXX)是你的用户名,

内部这样设置

```
{    "servers": {        "worldquant-brain-platform": {            "command": "python.exe",            "args": [                "platform_functions.py"            ],            "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features.",        }    },    "inputs": []}
```

command和args分别输入python和函数的地址

4. 之后点击启动


> [!NOTE] [图片 OCR 识别内容]
> SeNeCs
> D启动
> 39个工具 |更客。
> worldquant
> brain-platform"
> Command"
> Ipython
> exe
> args
> platform_functions
> description
> "WorldQuant
> BRAIN Platform
> MICP Server
> Comprehensive trading
> platform integration with simulation management,
> alpha operations,
> and
> authentication
> Credentials
> are
> stored
> user_config json in
> the
> Same directory
> Provides tools for creating simulations, checking
> status, managing alphas,
> and
> accessing platform features
> inputs"
> Py


5.之后在对话框的右下角点击工具, 查看是否启动了mcp服务, 之后直接在对话框询问即可


> [!NOTE] [图片 OCR 识别内容]
> 文件旧
> 编辑旧
> 选择[5]
> 查看0
> 转到[G]
> 运行[R)  终端[
> 帮助[]
> 配工具
> 凸锪
> 拖抻至此上传
> 扩展
> check_USA cOF
> 选择可用于聊天的工具。
> 已选81项
> 确定
> MCP
> settingsjson
> 聊天
> OUTLINE MAP
> 十9
> } X
> 凸
> Users
> Kaihu
> WCP
> 眼务器 Dlance WCp Serer
> descnption
> 在应用商店中搜索扩展
> MCP_Worldquant-br_Bet_glossary_terms
> 术语表
> MCP 眼务器: worldquant-brain-platform
> 膏E5
> 本地-己安装
> 内苴
> 需要我用这些工具跑一次登录并拉你的 Alpha 列表或开
> 个示例模拟
> SSH: SUPERMY
> 己安紫
> 阳 changes 获取己更改文件的差异
> 吗?
> 推荐
> codebase 在代码库中查找相关文件区块符鄂其他L息
> MCF 最务器
> 己瓮
> editFiles 编辑工忪区中的文件
> extensions 在 Visual Studio Code 扩展商域中嫂萦扩展
> worldquant-brain-platform
> @
> fetch 从顾页中提取主要内客。应包括要提 页面的 URL。
> 获取一下我最近的收入情允
> 凸
> fndTestFiles
> 对于源代码文件。请查找包含测试的文件。对于讽试文件。请查找包含正在测武.
> githubRepo 在 GitHub 存储库中搜索相关的原代码片段。可以使用 `所有者[存储牵 来指定存。
> in
> {} mCpjson6
> c
> 戽 new 在 VS Code 中措建新工作区的基架
> rectory
> 哭 opensimpleBrowser 在简易浏览器中预览本地托笞的网站
> 我先尝试直接从 BRAIN 平台拉取你的日赓与季赓支付数据。并汇总"最
> and
> 近"收入。
> 召
> problems 检查持定文件的错误
> readNotebookCelloutput 读取以前执行的单元楷的 出
> 己运行 get_daily_and_quarterly_payment
> runCommands 在终端中运行命令
> "
> runNotebooks 运行笔记本单元格
> worldquant-brain-platform (MCP 眼务器)
> runTasks
> 运行{务#为工<区6耿其#出
> 我己从 BRAIN 平台拉取支付数据并汇总"最近收入"
> 先给出结论
> 再附
> % runTests 运行单元测试
> 明细与可选导出方式。
> 1TL[tmtTLRTCTI
> 待办清单
> 获取日度与度支付数据:  己完成
> 汇总最近7天。8月累计。本季度。今年以来。历虫累计:  己完
> 标注最近"其他支付": 己完成
> 核心结论
> 昨8
> (2025-08-16)
> 59.26
> (Base」
> 近7天 (2025-08-10 ~ 2025-08-16)
> $65.26 (Base)
> 8月累计 (2025-08-01
> 2025-08-16]
> $135.56
> (Base)
> 本季度累计 (2025-07-01
> 2025-08-31。当前进度)
> $426.47
> (Base)
> 今年以来
> (YTD
> Base)
> $1,581.19
> 今年以来 (Other)
> 约$561.26 (合计: $2,142.45]
> 历虫累计: Base $1,816,88
> Other $2,315.11
> $4,131,.99 (USD)
> 数据时间戳:  2025-08-18109:39:262
> 问题
> 辙出
> 筛选器
> MCP: Worldquant-brain
> 亏 &#1:? X
> C023-00-10
> 09.33;3.310
> LwafflLfIB」 Lserver
> CUC[
> IUOOOLTSEO WUTLUUUaIIL
> NNU
> MLr SerVer
> LLIIB:
> 详细明细
> 2825-88-18  89:35:52.327
> [warning]
> [server stderr]
> 2825-88-18  89:35:52,325
> INFO
> Processing request Of type
> ListToolsRequest
> 昨日: $9.26 (Base)
> 2025-88-18  09:35:52.328
> [warning]
> [server stderr]
> 2025-88-18 89:35:52,327
> INFO
> Processing
> request Of type
> 近7天 (8/10-8/16, Base)
> ListpromptsRequest
> 7.74 +897
> 9.56
> 9.10
> 9.89
> 10.74
> 9.26
> $65.26
> 2025-88-18 89:35:52.329 [info] Discovered
> 39 tools
> 其他支付: $0
> 2025
> 88-18 89:39:24.397
> [warning]
> [server stderr]
> 2825
> 88-18 89:39:24,376
> INF0
> Processing request Of type
> CallTooIRequest
> 添加匕下文:
> TOJSOI
> 2025
> 88-18  09:39:24.397
> [warning]
> [server stderr]
> [INFO]
> 1U8081f510 Starting Authentication process
> 提供指令。
> 2025-88-18  09:39:25.362
> [warning]
> [server stderr]
> [SUCCESS]
> Authentication SUCCeSsfuI
> 2025
> 88-18
> 89:39:25.362
> [warning]
> [server stderr]
> [SUCCESS]
> JUT
> token automatically stored by
> 5e55ion
> Agent
> GPT-S (Prevewyj)
> 哭
> >
> 2025-88-18  09:44:48.417
> [info] 正在停止服务器 worldquant-brain-platform
> 3Cor


最后需要注意的是, 如果你是通过ssh连接到远端服务器时, 你的上述mcp配置应该仍在本机完成

最后的最后感谢weijie老师说copilot也可以使用mcp, 之前一直没咋探索🤣

---

## 讨论与评论 (3)

### 评论 #1 (作者: ZZ31673, 时间: 7个月前)

您好请问一下，我这配置完右下角的工具没有出现，有什么方法解决吗

---

### 评论 #2 (作者: YQ84572, 时间: 6个月前)

好用好用，直接用上copilot配合mcp了
====================================================================================================================

---

### 评论 #3 (作者: JF12271, 时间: 4个月前)

你好，没有找到启动按钮是为什么呢

---

