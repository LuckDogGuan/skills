# 【工具推荐】zcf + Claude Code + GLM-4.6：低价也能实现优质效果！经验分享

- **链接**: [Commented] 【工具推荐】zcf  Claude Code  GLM-46低价也能实现优质效果经验分享.md
- **作者**: TD65874
- **发布时间/热度**: 6个月前, 得票: 7

## 帖子正文

GLM-4.6是我目前使用过的所有AI中唯一提供‘真正’包月套餐的模型，和按token或者是‘假’包月的那些大模型相比，性价比可以说是相当高，但如果是直接使用GLM-4.6，据我使用感受而言，是比较一般的，所以，我们得搭配Claude Code来使用，这样才能达到很不错的效果。

然后在使用Claude Code的途中我又发现了一个好用的工具——zcf [GitHub - UfoMiao/zcf: Zero-Config Code Flow for Claude code & Codex]( [https://github.com/UfoMiao/zcf)（零配置,一键搞定](https://github.com/UfoMiao/zcf)%EF%BC%88%E9%9B%B6%E9%85%8D%E7%BD%AE,%E4%B8%80%E9%94%AE%E6%90%9E%E5%AE%9A)  Claude Code & Codex 环境设置 - 支持中英文双语配置、智能代理系统和个性化 AI 助手），非常适合搞不定Claude Code相关配置的朋友，具体操作非常简单：
### Step 1：安装 Node.js
zcf需要 Node 来跑，所以电脑没安装node的朋友请先安装一下node，官网：  [https://nodejs.cn/en/download](https://nodejs.cn/en/download)  ，官网下载自己系统的版本，安装之后在终端里输入：
```
node -v
npm -v
npx -v
```
能看到版本号，就说明成功了。
 
> [!NOTE] [图片 OCR 识别内容]
> PS C: |Users |10597> node
> CV
> V22.18.0
> Ps
> C: | Users |10597>
> npm
> CV
> 11
> 5.2
> PS C: |Users |10597>
> npX
> CV
> 11
> 5.2
> PS C: |Users |10597>


### Step 2：zcf 初始化
命令行中输入：`npx zcf` 打开交互式菜单，按需选择即可。
 
> [!NOTE] [图片 OCR 识别内容]
> C: | Users | 10597>npx
> ZCf
> Need
> to
> install
> the
> following packages
> ZCf@3
> 4.3
> Ok
> to proceed?
> Cy)
> E巳巨
> for
> Claude
> Code
> Zero-Config Code FLow
> Version:
> 3.4.3
> https : / /github . com /UfoMiao/zcf
> 请选择功能
> Claude Code
> 1
> 完整初始化
> 安装
> Claude Code
> 导入工作流
> 配置
> API 或
> CCR 代理
> 配置 MCP 服务
> 2
> 导入工作流
> 仅导入 /更新工作流相关文件
> 3
> 配置
> API 或
> CCR 代理
> 配置
> API
> URL
> 认证信息或
> CCR 代理
> 4.
> 配置
> MCP
> 配置
> MCP 服务 (含
> Windows 修复 )
> 5.
> 配置默认模型
> 设置默认模型 (opus/sonnet/sonnet Im/自定义)
> 6。
> 配置
> Claude 全局记忆
> 配置
> AI 输出语言和输出风格
> 7
> 导入推荐环境娈量和权限配置
> 导入隐私保护环境娈量和系统权限配置
> 其他工具
> R。
> CCR
> 配置
> Claude
> Code
> Router 以使用多个
> AI 模型
> U.
> CCusage
> Claude
> Code 用量分析
> 匕
> CCometixLine
> 基于
> Rust 的高性能
> Claude Code 状态栏工具, 集成 Git 信息和实时使用量跟踪
> ZCF
> 更改显示语言
> Select display language
> 更改
> ZCF 界面语言
> 5
> 切换代码工具
> 在支持的代码工具之间切换
> (Claude Code,
> Codex)
> 卸载和删除配置
> 从系统中删除
> Claude
> Code 配置和工具
> 检查更新
> 检查并更新
> Claude
> Code
> CCR 和
> CCometixLine 的版本
> @.
> 退出
> 请输入选项,回车确认 (不区分大小写)


### Step3：指定模型为GLM-4.6


> [!NOTE] [图片 OCR 识别内容]
> 「请输入选项 ,
> 回车确认 (不区分大小写)
> 3
> 请选择
> API 配置模式
> 2.
> 自定义
> API 配置
> Claude
> Code 配置管理
> 当前配置数量:
> 1
> 当前默认配置:  glm-test
> 请选择操作
> 1.
> 添加配置
> 2.
> 编辑配置
> 3.
> 复制配置
> 4.
> 删除配置
> 5.
> 跳过
> N navigate
> select
  
> [!NOTE] [图片 OCR 识别内容]
> [
> 请选择操作
> 1.
> 添加配置
> 添加新配置
> 「请选择
> API 供应商
> 4.
> GLN
> 己选择供应商:
> GLN
> 「配置名称 (仅限字母
> 数字
> 空格.
> '一)
> 9lm-4.6
> 请输入
> GLM 的
> API
> Key
 
选择供应商GLM，然后输入自己的GLM-4.6的api key即可。

这一步如果没有api key的朋友，可以通过我的**邀请链接**注册：
 [https://www.bigmodel.cn/claude-code?ic=F0ICABFQRK](https://www.bigmodel.cn/claude-code?ic=F0ICABFQRK) 
或者直接进官网注册也可以：
 [https://bigmodel.cn/](https://bigmodel.cn/)

注册完之后，进入特惠专区：
 
> [!NOTE] [图片 OCR 识别内容]
> BigModel
> 特惠专区
> 大模型
> 应用空间
> 体验中心
> 价格
> 开发者 ~
> 企业
> 关于智谱
> 开发文档
> 控制台
> GLM Coding 跨年限时特惠
> 1/7价格.
> 3倍用量
> 适用Claude Code
> Cline
> 等主流编程工具
> GLM Coding
> 跨年特惠Coding套餐
> 邀好友赚赠金



> [!NOTE] [图片 OCR 识别内容]
> BigModel
> 我的编程套餐
> 接入编程工具 `
> 调AMCP
> 社区
> 常见问题
> API
> GLM Ioclimg pam:跨年特惠
> 12.08-01.15:
> 50% 首购立减 +额外节日限定优惠! 详细说明
> 全球顶尖编程模型 GLM-4.6 驱动
> GLM-4.6 发布时。在推理。代码和智能体能力等方面达到开
> 源模型 SOTA 水平
> Claude Sonnet 4.5
> 1387
> 无缝适配多种主流 Al 编程工具
> GLM 4.6
> 1372
> 超大容量
> 更低价格
> GPT 5.1
> 1364
> 免费享专属 MCP 
> 解锁高级能力
> 位列 Code Arena 榜单第一梯队
> 取自榜单更新时间 2025-11-22
> 首月享5折,
> 最高立省200元
> 琏续包月
> 连续包季
> -559
> 连续包年
> -609
 
订阅适合自己的套餐即可，订阅后点击右上角的API Key，然后创建api key并复制即可。

### Step4：开始使用
在按照zcf上面的步骤配置完成之后，我们先在控制台中cd到自己项目的地址，比如：`cd C:\Code\wqb` ，然后输入：`claude`，然后回车即可，如果出现如图所示的页面代表配置成功：
 
> [!NOTE] [图片 OCR 识别内容]
> Ps
> C: | Users |10597>
> cd
> C: | Code Iwqb
> Ps
> C: | Code'
> claude
> Claude
> Code
> V2.0.26
> Tips
> for getting started
> Welcome
> back !
> Run
> /init
> to
> Create
> CLAUDE .md
> file with
> instructions
> for Claude
> Recent
> activity
> No
> recent
> activity
> Sonnet
> 4.5
> API Usage Billing
> C: | Code|wqb
> Iy
> Iedit
> <filepath>
> to
> Sonnet
> 4.5
> main
> 0.6%
> 1.Ik tokens
> Thinking
> On
> Ctab
> to
> toggle)
> Wqb>
> Wqb
 
然后就可以正式使用了。

更多关于zcf的用法、参数与工作流说明可以查看文档： [ [https://zcf.ufomiao.com/zh-CN/](https://zcf.ufomiao.com/zh-CN/)](https://zcf.ufomiao.com/zh-CN/](https://zcf.ufomiao.com/zh-CN/))

==然后补充一点，如果用不习惯Claude Code cli命令行工具的，可以去vscode中下载Claude Code插件：
 
> [!NOTE] [图片 OCR 识别内容]
> File
> Edit
> Selection
> View
> Go
> Run
> Terminal
> Help
> WQ-code [Administrator]
> 侣
> EXTENSIONS
> 田 Extension: Claude Code for VS Code X
> 米 凹
> Claude Code
> Search Extensions in Marketplace
> Past Conversations
> Claude Code for VS Code
> V2
> INSTALLED
> Cline
> Update
> Anthropic
> anthropiccom
> 2,335,422
> Claude Code
> CodellDB
> 13ms
> Claude Code for VS Code: Harness the power of Cla.
> Debugger for native code; powered by LLDB。
> Restart Extensions
> Disable
> Uninstall
> Auto Up
> Vadim Chugunov
> Update
> CICt +
> DETAILS
> FEATURES
> CICt +
> CICt + Intellisense; debugging, and code bro.
> Microsoft
> Restart Extensions
> Categories
> C# Dev Kit
> Claude Code for VS
> 0#
> Official C# extension
> Microsoft
> Chat
> Microsoft
> Restart Extensions
> Code
> Claude Code for VS Code
> ggms
> Resources
> Claude Code for VS Code: Harness the power
> Unleash Claude's raw power directly in your
> It's a beautiful
> to use the computer, don't
> Anthropic
> Restart Extensions
> terminal Search million-line codebases instantly。
> Marketplace
> you think?
> Turn hours-long workflows into a single
> Issues
> ESLint
> 31ms
> command. Your tools。 Your workflow. Your
> Anthropic
> ES
> Integrates ESLint JavaScript into VS Code。
> Uint
> codebase; evolving at thought speed。
> Microsoft
> Restart Extensions
> More Info
> Powerful intelligence: Use the latest
> Lua
> Lua Language Server coded by Lua
> Claude models using your Pro, Max; Team;
> Published 2025-06-19,
> Ua
> sumneko
> Restart Extensions
> OI
> Enterprise subscription; or pay-as
> 00:32:16
> go pricing
> Last
> 2025-12-18,
> Prefer the Terminal experience? Switch back in Settings。
> Lua Debug
> Works alongside you: Claude
> released
> 06:13:33
> Ua
> VSCode
> debugger extension for Lua
> autonomously explores
> codebase;
> Last
> 2025-12-18,
> ctrl esc to focus or unfocus Claude
> YOUT
> actboyl68
> Restart Extensions
> updated
> 15.01.48
> readsand writes code; and runs Term
> Identifier
> anthropic. claude
> Ask before edits
> alpha_searcher_use:ipynb
> Prettier
> Code formatter
> G1ms
> commands with your permission。
> Code
> Code formatter
> prettier
> Now ferhor mtorface that makes 汁
> from
> day
> JOU
> using


---

## 讨论与评论 (7)

### 评论 #1 (作者: PZ64174, 时间: 6个月前)

```
“群友们真是人才众多！”
```

感谢大佬分享！五花八门各式各样的ai使用方式都在论坛见到了，最近也在不断尝试新的方式进行使用，对比使用体验。看看哪个体验更好性价比更高！

====================================================================

一年一个台阶，一步一个脚印

====================================================================

---

### 评论 #2 (作者: 顾问 LW67640 (Rank 24), 时间: 6个月前)

我之前发给一个帖子关于iflow的，iflow有个人用户免费的api接口，也有glm-4.6模型，推荐给有需要的顾问。

---------------------------------------------------------------------------------

时间要花在有效率的地方

---------------------------------------------------------------------------------

---

### 评论 #3 (作者: YQ84572, 时间: 6个月前)

您发现的“GLM-4.6 + Claude Code + ZCF”确实是当前AI工具的“黄金组合”，GLM-4.6真正的包月制让高频使用毫无压力，成本仅为国际大模型的零头；Claude Code提供了顶级的代码生成与交互体验；而ZCF工具则实现了一键配置，将复杂的API对接和环境搭建化为无形。感谢分享

---

### 评论 #4 (作者: YZ64617, 时间: 6个月前)

ZCF的CCR，支持iflow，配置起来更容易和方便。

但是，几个ZCF版本之前，这种CCR配置iflow，会报错。个人感觉可能是因为iflow只提供单线程调用。

**如果用不习惯Claude Code cli命令行工具的，可以去vscode中下载Claude Code插件**

vscode中的Claude Code，需要单独配置。大家搜搜

---

### 评论 #5 (作者: MY49971, 时间: 6个月前)

AI 工具越来越多了，不知道选哪个好了...

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #6 (作者: ZH12413, 时间: 5个月前)

从Node.js安装到API配置，步骤清晰易懂，连邀请链接和截图手把手教学。
感谢细致的分享，祝大佬玩转Alpha，vf0.99+，受益多多。
==================================================================================
Hard work pays off.
==================================================================================

---

### 评论 #7 (作者: XW23690, 时间: 5个月前)

感谢分享，iflow也有GLM4.6模型可以使用，而且是免费的。CLI的调用可是事先准备好相关的prompt以及operators等md文件，我自己亲测发现也可以得到不错的信号，特别是针对优化因子，有一两个test需要优化的时候，AI能提供很好的帮助。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

