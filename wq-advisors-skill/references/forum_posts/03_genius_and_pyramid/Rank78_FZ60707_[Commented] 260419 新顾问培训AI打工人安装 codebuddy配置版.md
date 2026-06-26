# 26.04.19 新顾问培训AI打工人安装 codebuddy配置版.

- **链接**: [Commented] 260419 新顾问培训AI打工人安装 codebuddy配置版.md
- **作者**: 顾问 QX52484 (Rank 35)
- **发布时间/热度**: 2个月前, 得票: 12

## 帖子正文

由于周六突发疑似claude官方导致的问题. 在安装AI打工人后遇到该报错的同学建议尝试codebuddy CLI


> [!NOTE] [图片 OCR 识别内容]
> 不持的 16 位应用裎序
> 由于与64位版本的 Windows 不蒹容。此程序或功能
> I?AC:(UserslAdminlAppDatalRoaminglnpmlnode_modulesl@anthropic-aiclau
> de-codelbinlclaude.exe 无法启动或运行。请联系软件供应商询问足否有与64位
> Windows 莱容的版本。
> 磔定


请务必完整搜索codebuddy CLI 避免误安装IDE


> [!NOTE] [图片 OCR 识别内容]
> codebuddy cli
> 0
> 网页
> u
> 视频
> 词典
> 地囝
> 币多
> 约91,600 个结果
> Workbuddy
> WWcodebuddycn
> CodeBuddy Code- 专业工程师的A1 CLI工具
> CodeBuddy Code 通过自然语言命令自动完成炱杂的编程任务,实现极致自动化效率捉升;终端原生,无缝集


打开网页找到npm install -g @tencent-ai/codebuddy-code 输入cmd进行安装 为避免安装时权限不足 建议按管理员权限打开.


> [!NOTE] [图片 OCR 识别内容]
> 终端原生
> cmd
> 自动化构建部署
> 全部
> 应用
> 文档
> Hy
> 文件夹
> 照片
> 22160 *
> 最佳匹配
> 在熟悉的终端环境,直接获得 Al 辅助,无需切换开发工具。全仓目
> 命令捉示符
> 知。内置完整工具链。用自然语言驱动开发运维全流程自动化
> 系坑
> 应用
> 命令提示符
> Nodejs command prompt
> $ npm install
> 9 @tencent-ai/codebuddy-code
> Install Additional Tools for Nodejs
> 打开
> Git CMD
> 以臂理员y#运行
> 打开爻件血五
> 搜索网页 11+
> 固定到~开蛄~氐'
> 查看更多溲泰结果
> 囹定到任务栏
> Cmd管理员身份运行 命令
> cmd 命令大全
> cmd怎么打开
> cmd
> 文档
> Cmd py
> Cmd


由于我已安装过 下载内容较少.


> [!NOTE] [图片 OCR 识别内容]
> 6 选绎 npm view @tencent-ailcodebuddy-code@latest version
> Ticrosoft Vindos [舨本
> 10.026200.80371
> C〉 Icrosoft Corporatior。
> 保留斯有权利
> Iindows   Systen32>IpU install
> 『telcent-ai ! codebuddy-code
> changed
> packages in Ils
> Iindows  System32>codebuday
> CodeBuddy Code 42.91
> for getting started
> Press
> USe
> Commuldz
> to nelitioli files。
> Ruu
> fterminal-setup
> configure newline
> binding for
> Yollr terminal
> Press Ctrl
> to paste URLs;
> file paths。
> imaaes
> Recent actirity
> Lecelit  actiyity
> http; 11127.0.0.1:58503
> ?sessionld=c9217.71-66+5-433-8af0-642958acaac0
> Ilinilfax-I[2, 7-highspeed
> internal [Jsage Billina
> Windows   System32
> Hodls SessionStart
> 前下支持 『indois 系统
> 靖使髑emcbs"荻
> IcDS 或 Lin
> Iips
> Ley


切换到安装AI打工人的untracked目录 构建一个.mcp.json文件


> [!NOTE] [图片 OCR 识别内容]
> 此电脑
> Data [D:)
> code
> Python
> Lib
> site-packages
> cnhkmcp
> Unzrazked
> N 排序 
> 三  查
> 修改日期
> 类型
> reter
> 2026/4/17 15:20
> 文件夹
> SECrets
> 2026/3/3116;00
> 文件买
> skills
> 2026/3/2916;47
> 文件买
> sUpEr_alpha
> 2026/4/19 9;48
> 文件买
> brain_credentials
> 2026/4/517:35
> BRAIN_CREDEN
> 'mcpijson
> 2026/4/19 9;51
> JSON 源文件


.mcp.json配置内容 安装个人情况自行修改 如果改不来,可以启动codebuddy 让AI自己改. 启动方式见下文

```
{  "mcpServers": {    "worldquant-brain-platform": {      "type": "stdio",      "command": "D:/code/python/python.exe",      "args": [        "D:/code/python/Lib/site-packages/cnhkmcp/untracked/platform_functions.py"      ],      "env": {        "PYTHONUNBUFFERED": "1"      },      "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication.",      "excludeTools": ["submit_alpha", "check_correlation", "create_simulation"],      "autoApprove": true    }  }}
```

在untracked目录 空白处右键 点击在终端中打开. 实现在当前目录下启动cmd 输入codebuddy


> [!NOTE] [图片 OCR 识别内容]
> npm list
> Ps
> 0: Icode Ipython ILiblsite-packages Icnhkmcpluntracked> codebuddy
> CodeBuddy Code
> V2.91.0
> P5
> for getting
> started
> Run /init
> Create
> CODEBUDDY .md
> Or
> AGENTS
> md file
> With
> instruction。
> Press
> to
> use Commands
> @ to mention files
> Open
> Web UI
> browser for
> richer interactive experience
> Recent
> activity
> 凹
> lgent
> browser:install
> /model
> um://12?.@:@:!:6@454/?点ssnIdsegfsfhze-@?@-4@f-点燃-!@58?J
> GLI-5.1
> internal Usage Billing
> d: Icode lpython lLiblsite-packages |cnhkmcp luntracked
> Hook Sessionstart
> agent-browser 目前不支持
> Windows 系统
> 请使用
> macOs 或
> Linux
> bypass permissions
> Calttm
> to
>  cycle)


左下角的alt+m 模式为yolo模式 不想被多次询问则进行开启.

在配置完mcp.json后 在codebuddy中输入/mcp 检查是否正常运行


> [!NOTE] [图片 OCR 识别内容]
> !1点点!』点』点』.
> #点烹点烹
> !
> 
> !
> GLN- 5.1
> internal Usage Billing
> 4: Icode
> IpythonlLiblsite
> packages Icnhkmcp luntracked
> ~ Hook
> Sessionstart
> agent-browser 目前不支持
> Windows 系统
> 请使用
> macOs 或
> Linux
> /mcp
> Manage MCP
> SerVers
> SerVer
> Project MCPs Cd: Icode lpythonlLiblsite-packages Icnhkmcp luntracked l.mcp.json)
> Worldquant
> brain-platform
> Connected
> For help configuring MCP
> SerVers
> see: https: /
> ' /copilot .tencent
> Com/docs /cli/mcp
> to navigate
> Enter to
> Confirm
> Esc
> to cancel


输入/model 修改模型 本次课程建议使用GLM5.1或GLM 5.0 (5.1效果较好但请求高峰问题严重)


> [!NOTE] [图片 OCR 识别内容]
> /model
> Select Model
> Select
> model
> for this
> conVersation
> and future
> Sessions
> GLN- 5.1
> [9lm-5.1]
> Cxl.06 credits)
> GLM-5
> 9lm-5.01
> Cx0 . 80 credits)
> GLI-5.0-Turbo
> [9lm-5.0-turbo]
> CxO.95 credits)
> GLMI-SV-Turbo
> [9lm-Sv-turbo]
> Cx0 . 95
> credits)
> GLI-4 .7
> [9lm-4.7]
> Cx0.21
> credits)
> MiniMax-M2.7
> [minimax "2.7]
> Cx0.26 credits]
> Minilax M2.5
> [minimax-m2.5]
> Cx0.18 credits)
> Kimi K2. 5
> kimi-kz. 5]
> Cx0.45 credits)
> DeepSeek-V3.2
> deepseek-V3-2-Volc]
> Cx0.29
> credits)
> Hunyuan-2. 0-Thinking
> [hunyuan-2.O-thinking]
> Cxo
> 04 credits)
> Enter
> confirm
> t for this session
> Esc
> to
> exit
> only


模型消耗codybuddy端额度,在官网个人页面中进行查询额度 [https://www.codebuddy.cn/profile/usage](https://www.codebuddy.cn/profile/usage)

目前注册有赠送.(到此疑似超图片上传额度详见评论区)

---

## 讨论与评论 (13)

### 评论 #1 (作者: 顾问 QX52484 (Rank 35), 时间: 2个月前)


> [!NOTE] [图片 OCR 识别内容]
> 加人 WorkBuddy, 合伙养虾计划, 一起赚虾米
> 立即加2〉
> 诱于4/30前;
> 登录异常补偿1000 Credits 已到账。感谢您的理解与支持
> 已领取
> 限时加赠4/1-4
> 欢迎体验 WorkBudgy 3000 Credits 见面礼。助您快速启动
> 巳领取
> 基础体验包
> 下次刷新时间:2026年 05月01800:00:00
> 500
> 500
> 0剩余
> 活动赠送包
> 生效中
> 活动包额度:  6000 积分
> 活动赠送积分到期后自动失效。请在有效期内使用。
> 3230.03
> 6000
> 2769.97剩余
> 详情


有月度额度和额外赠送额度,建议自行体验后考虑其他套餐

---

### 评论 #2 (作者: 顾问 QX52484 (Rank 35), 时间: 2个月前)

调整为API调用时到用户目录 建立models.json文件


> [!NOTE] [图片 OCR 识别内容]
> 此电脑
> Windows (C:]
> 用
> SIyUan454
> codebuddy
> N  诽序
> 三  查
> 名祢
> 修改日期
> 粪
> -小
> Connectors
> 2026/4/820;10
> 文件买
> Connectors-marketplace
> 2026/4/820;16
> 文件买
> file-histony
> 2026/4/199:46
> 文件买
> inspiration
> 2026/4/820;10
> 文件买
> ocal_storage
> 2026/4/221:11
> 文件买
> 095
> 2026/4/19 9;20
> 文件买
> plugins
> 2026/4/820;16
> 文件买
> projects
> 2026/4/19 9;20
> 文件买
> SessIons
> 2026/4/1910:19
> 文件买
> shell-snapshots
> 2026/4/19
> 文件买
> skills-marketplace
> 2026/4/820;17
> 文件买
> tasks
> 2026/4/199;4
> 文件买
> traces
> 2026/4/199:59
> 文件买
> expert-histonjjson
> 2026/4/112;27
> JSON 源文件
> histonyjsonl
> 2026/4/1910;23
> JSONL fle
> 32KB
> instancesijson
> 2026/4/818;09
> JSON 源文件
> mcpijson
> 2026/4/112;27
> JSON 源文件
> modelsjson
> 2026/4/1910;24
> JSON 源文件
> USEI
> statejson
> 2026/4/1910:19
> JSON 源文件
> settingsijson
> 2026/4/1910;06
> JSON 源文件
> 2KB
> 10.19


参考该样式进行建立


> [!NOTE] [图片 OCR 识别内容]
> 配置结构
> "models":
> Iid"
> 9lm-5.1"
> name
> "Mylodel"
> Vendop"
> "Zhipu"
> apiKey"
> "Your-API-Key"
> IUpl"
> https : / /open. bigmodel. cn/api
> Coding /paas /V4
> SUppoptsToolCall"
> tpUe ,
> sUpportsReasoning
> trUe


---

### 评论 #3 (作者: 顾问 QX52484 (Rank 35), 时间: 2个月前)

目前疑似只支持open ai协议


> [!NOTE] [图片 OCR 识别内容]
> 1.2接口地址
> 协议
> Base URL
> OpenAl 协议
> https : / Imaas-coding-api
> Cn-huabei
> -1.Xf-yun. Com/vz
> Anthropic 协议
> https : / Imaas-coding-api
> Cn-huabei
> -1.Xf-yun. com /anthropic



> [!NOTE] [图片 OCR 识别内容]
> Ld"
> a5tpOn
> Code
> latest"
> 0ame
> Astron
> Code
> Latest
> Vendor
> ZhipU"
> apikey
> dedf3cd08db4ee02738485bae92d8868;MjhMZDZhMDRZNT
> "UPT"
> ht5:/maas
> coding-aie-hyabei.x_yyComLvz"


设置成功后对应模型不再显示额度


> [!NOTE] [图片 OCR 识别内容]
> /model
> Select Model
> Select
> a model
> for this conversation
> future sessions
> GLN- 5.0
> [glm-5.0]
> CxO.80 credits)
> KimiK2. 5
> [ kimi-kz. 5]
> Cx0.45
> credits)
> GLM-4.GV
> [glm-4.Gv]
> Cx0.11 credits)
> GLM-4.5 Air
> [glm-4.5-air]
> GLM-5.1
> [GLNI5.1]
> Astron Code
> Latest
> [astroncodelatest ]
> Enter to
> confirm
> for this
> session only
> Esc
> to exit
> and


---

### 评论 #4 (作者: 顾问 QX52484 (Rank 35), 时间: 2个月前)

补充: skills则找到skills文件放在该路径下 即可/skills查看


> [!NOTE] [图片 OCR 识别内容]
> 此电脑
> Data {0;)
> COOe
> Python
> Lib
> slte-packages
> CnhkmCP
> Untracked
> codebuddy
> skills
> N #序
> 三  查
> 侈改日期
> "
> 天小
> Claude_Skill_Creation_Guideimd
> 2026/1/17 9:41
> Markdown 源文件
> 5 K3
> brain-calculate-alpha-selfcorrQuick
> 2026/4/112:30
> 文件买
> brain-data-feature-engineering
> 2026/4/112:30
> 文件买
> brain-datafield-exploration-
> enera
> 2026/4/112:30
> 文件买
> brain-dataset-exploration-
> enera
> 2026/4/112:30
> 文件奕
> brain-explain-alphas
> 2026/4/112:30
> 文件买
> brain-Teature-
> ementation
> 2026/4/112:30
> 文件买
> brain-how-to-pass-AlphaTest
> 2026/4/112:30
> 文件奕
> brain-improve-alpha-performance
> 2026/4/112:30
> 文件买
> brain-nextMove-analysis
> 2026/4/112:30
> 文件买
> expression_verifier
> 2026/4/112:30
> 文件买
> planning-with-files
> 2026/4/112:30
> 文件买
> pull_BRAINSkiII
> 2026/4/112:30
> 文件买
> mpl


---

### 评论 #5 (作者: 顾问 QX52484 (Rank 35), 时间: 2个月前)

后附:一个可参考的科大讯飞的套餐  [https://maas.xfyun.cn/packageSubscription](https://maas.xfyun.cn/packageSubscription)  39/月/1W8次请求 可以支撑一个中度使用AI顾问的月度用量.

可以在 [https://maas.xfyun.cn/packageSubscription](https://maas.xfyun.cn/packageSubscription)  点击邀请用户填写邀请码后再点击旁边的订阅套餐进行购买.

可以找其他顾问互填并购买,这样可以一起拿到39月月卡套餐+39X2的API额度.

如果朋友是最难达成的配置,可以填我的邀请码【MAAS-439467FF】

---

### 评论 #6 (作者: FF65210, 时间: 2个月前)

感谢大佬分享，狠狠学习了。

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

### 评论 #7 (作者: XC66172, 时间: 2个月前)

谢谢思源佬的分享，又多了一个CODEBUDDY CLI可以拿来学习使用~~

=========================================

FIGHTING LABUBU!~

========================================

---

### 评论 #8 (作者: 顾问 FZ60707 (Rank 78), 时间: 2个月前)

大佬太强了，这波codebuddy配置教程非常实用，尤其对刚入门的新顾问来说简直是及时雨！已收藏，回头就照着折腾起来，感谢无私分享

========================================================================================================================================================================

---

### 评论 #9 (作者: WW74101, 时间: 2个月前)

它不是干巴巴的理论，而是带着自己的踩坑经验，把每个环节的操作、截图、命令都写得明明白白。
它给出的方案（CodeBuddy CLI），完美解决了原 Claude 客户端的兼容性问题，同时保留了 AI 打工人的核心功能。

---

### 评论 #10 (作者: ES80736, 时间: 2个月前)


> [!NOTE] [图片 OCR 识别内容]
> Press
> to
> USe
> Commands
> @ to mention
> files
> Open
> Web UI
> in
> browser for
> richer
> interactive experience
> Press
> Ctrl
> V to paste URLs
> file
> paths
> OI
> images
> Recent activity
> 回
> 匆么连不上worldquant ,该如何修改配置
> !m:/412? .@.@.1:5@55@
> GLM-5.1
> internal Usage Billing
> d: |worldquant |dagongren
> untracked
> MCP
> Manage
> MCP
> SerVers
> SerVer
> Project
> MICPs
> Cd: Iworldquant |dagongren luntrackedl .mcp . json)
> Worldquant-brain-platform
> X
> Disconnected
> For help configuring
> MCP
> SerVers
> See:
> https : / /copilot .tencent . com /docs /cli
> mCP
> 八
> t0
> navigate
> Enter to confirm
> Esc to cancel
 mcp显示连接不上，请问此类配置要如何修改

---

### 评论 #11 (作者: YP74336, 时间: 2个月前)

使用过workbuddy优化alpha，运行一会就卡住不动了。准备按楼主的方法尝试codebuddy cli，感谢分享

---

### 评论 #12 (作者: XL98962, 时间: 1个月前)

学会了，感谢大佬分享

==================================================================、

==================================================================

---

### 评论 #13 (作者: 顾问 MZ45384 (Rank 51), 时间: 1个月前)

大佬太强了。新工具源源不断，希望alpha也能源源不断。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

