# [MCP]免费最强版 Trae/VsCode + Cline + Gemini-cli 构建 cnhkmcp 使用环境经验分享

- **链接**: [Commented] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享.md
- **作者**: 顾问 JX79797 (Rank 9)
- **发布时间/热度**: 10个月前, 得票: 89

## 帖子正文

先赞后看，一键三连，需科学上网

**1. Gemini Cli 安装和登录验证参考，只需要通过用户认证即可**

[../顾问 JG15244 (Rank 67)/[Commented] Gemini CLI 结合 MCP 工具的探索经验分享.md](../顾问 JG15244 (Rank 67)/[Commented] Gemini CLI 结合 MCP 工具的探索经验分享.md)

**2. Cline 插件下载安装**

Cline插件在3.18.0短暂的支持过Gemini Cli ，在google要求下很快下线了该功能，该版本下载地址：  [https://github.com/cline/cline/releases/download/v3.18.0/cline-3.18.0.vsix](https://github.com/cline/cline/releases/download/v3.18.0/cline-3.18.0.vsix)

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

角色配置参考： [../顾问 FX25214 (Rank 22)/[Commented] 【MCP】角色配置工作流该安排谁来执行经验分享.md](../顾问 FX25214 (Rank 22)/[Commented] 【MCP】角色配置工作流该安排谁来执行经验分享.md)


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

## 讨论与评论 (21)

### 评论 #1 (作者: SG46247, 时间: 10个月前)

========================================================================

感谢老哥的分享，现在要不是模型免费，但模型不强，要不就是模型可以但是烧钱，老哥给我们找到折中的法子，爆赞

====================================

---

### 评论 #2 (作者: JL97920, 时间: 10个月前)

```
求助作者  到了Let's go! 目前不知道怎么继续了  点let's go!没有反应
```

---

### 评论 #3 (作者: 顾问 JX79797 (Rank 9), 时间: 10个月前)

**如果直接选择Gemini CLI Provider，Let‘s get Started没有反应，可以任意选一个其他的AI填入api key，进入之后再重新选择Gemini CLI Provider**

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**

---

### 评论 #4 (作者: XZ35933, 时间: 10个月前)

按照你的操作步骤，终于配置成功，很好用，非常感谢！

---

### 评论 #5 (作者: QL33236, 时间: 10个月前)

有没有遇到Request failed with status code 403报错的情况

---

### 评论 #6 (作者: SC77987, 时间: 10个月前)

========================================================================
感谢大佬的分享，前几天在用通义灵码, 但是完全回答不上问题, 没有任何生产力, gemini就聪明多了,虽然有额度限制,但是 60次每分钟，1000次每天的额度也完全够用了,再次感谢大佬的分享,谢谢
========================================================================

---

### 评论 #7 (作者: 顾问 JX79797 (Rank 9), 时间: 10个月前)

@ [SC77987](/hc/en-us/profiles/33743095949079-SC77987)

额度限制 切换到 gemini-2.5-flash上，感觉也不差，用一会再切回去

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐==========================#**

---

### 评论 #8 (作者: JT28152, 时间: 10个月前)

大佬，为什么我的会连接报错（已科学上网）？ 
> [!NOTE] [图片 OCR 识别内容]
> CLINE [品+)
> 十 罾 9囚
> ] Extension: Cline
> 50.0000
> Cline
> 描述当前mcp的详细功能
> Cline
> Token: 个0 !0
> 16.9LB
> Autonomous coding agent rghtin your IDE capable of creatinglediting fles; running commands; using the br..
> 10m
> Disable
> Uninstall
> Auto Update
> API Streaming Failed
> DETAILS
> FEATUREs
> CHANGELOG
> Cline instance aborted
> ONECLOJInT
> Compa
> Rsso
> API Streaming Failed
> Changelog
> request to https; | |cloudcode-pa:googleapis comfvlinternal:streamGenerateContent?
> alt=SSe failed reason: Client network socket disconnected before Secure TLS connection
> [3.18.0]
> Was established
> Optimized Cline to work with the Claude
> family af models; resulting in improved performance; reliability and new capabilities
> Added
> new Gemini CU provider that allows you to Use your local Gemini CU authentication to access Gemini models for free (Thanks
> @google geminiy]
> Optimized Cline to work
> the Gemini 2.5 family af models
> Updated the default and recommended model to Claude
> Sonnet for the best performance
> Fix race condition in Plan/Act mode switching
> Improve robustness af search and replace parsing
> Task
> uth


---

### 评论 #9 (作者: JL67084, 时间: 10个月前)

大佬，Request failed with status code 403报错怎么解决

---

### 评论 #10 (作者: ZY95930, 时间: 10个月前)

我是VsCode + Cline遇到Request failed with status code 403报错，还没有定位到问题原因。

---

### 评论 #11 (作者: YL20168, 时间: 10个月前)

JT28152 JL67084 ZY95930

好像是gemini CLI把这个版本的调用也给禁了，换个扩展吧，亲测kilo code还可以调用gemini CLI，直接扩展搜索安装就可以

---

### 评论 #12 (作者: CH62432, 时间: 10个月前)

昨天听了您的分享很受启发，今天结合您发布的文章在vscode上成功配置了，并且顺利运行起来了。非常感谢您的无私分享，特别期待后续能有更多实用的示例可以参考！

**--------------------- WORLDQUANT  BRAIN -------------------**

---

### 评论 #13 (作者: JW85895, 时间: 9个月前)

感谢分享，成功运行了

---

### 评论 #14 (作者: LL49894, 时间: 9个月前)

报403应该就是没有配置projectid导致的，cmd窗口运行gemini如果projectid配置错了，也是报403，环境变量配对以后，cmd窗口能正常调用。但是cline没有输projectid的地方，感觉这问题无解。

---

### 评论 #15 (作者: YC28464, 时间: 9个月前)

我错过了什么吗，worldquant-brain-platform这个mcp在哪里安装呢？

---

### 评论 #16 (作者: 顾问 MZ45384 (Rank 51), 时间: 9个月前)


> [!NOTE] [图片 OCR 识别内容]
> API Configuration
> Plan Mode
> Act Mode
> API Provider
> Gemini CLI Provider
> OAuth Credentials Path (aptional)
> Default: ~ / geminiloauth_credsjson
> Path to the OAuth credentials file. Leave empty to use the default location (~ / geminiloauth_credsjson)。
> This provider uses OAuth authentication from the Gemini CLI tool and does not require API keys.If you haven't
> authenticated
> please run gemini in your terminal first。
> Gemini CLI Setup Instructions
> Model
> gemini-2.5-pro
> Google's Gemini 2.5 Pro model via OAuth (free tier)
> Supports images
> Supports browser use
> Max output: 65,536 tokens
> Free up to 2 requests per minute: After that;
> depends on prompt size: For more info, see pricing details:
> Important Requirements
> you need to install the Gemini CLI tool
> Then; run
> in yourterminal and make sure you Log in with Google
> Works with personal Google accounts (not Google Workspace accounts)
> Does not use API keys
> authentication is handled via OAuth
> Requires the Gemini CL tool to be installed and authenticated first
> Free tieraccess Via OAuth authentication
> Use different models for Plan and Act modes
> Switching between Plan and Act mode will persist the APIand model used in the previous mode: This may be helpful
> 8.9. when
> strong reasoning model to architect a plan for a cheaper coding model to act on。
> yet
> billing
> First
> gemini
> Only
> using
 感谢分享，已经按照步骤成功build。

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================================================#**

---

### 评论 #17 (作者: LQ97658, 时间: 9个月前)

按照大佬的步骤来的，可惜一直Request failed with status code 403报错，然后把cline换成kilo code，同样的配置MCP serve，终于成功了，给其他遇到同样问题的朋友们参考。

**=================================================**

---

### 评论 #18 (作者: SZ83119, 时间: 9个月前)

请问大佬这和直接安装Gemini CLI Companion扩展的优势在哪里呢

---

### 评论 #19 (作者: YM14905, 时间: 7个月前)

用Cline怎么配都配不好，换了kilo，kilo code里甚至没有Gemini Cli的选项，有大佬成功的吗

---

### 评论 #20 (作者: XG98059, 时间: 6个月前)

大佬无敌

---

### 评论 #21 (作者: RW49172, 时间: 1个月前)

感谢大佬分享

---

