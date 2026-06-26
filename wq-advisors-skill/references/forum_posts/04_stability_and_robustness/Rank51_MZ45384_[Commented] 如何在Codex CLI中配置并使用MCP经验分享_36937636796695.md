# 如何在Codex CLI中配置并使用MCP经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 如何在Codex CLI中配置并使用MCP经验分享_36937636796695.md
- **作者**: WL27319
- **发布时间/热度**: 6个月前, 得票: 4

## 帖子正文

因为Gemini帐号没有学生认证资格，遂决定用Codex来进行MCP研究，现将流程分享如下：

前提：拥有ChatGPT Plus/Pro 账号

### **1. 安装Node.js** :

- 如果你的本地电脑已安装 Node.js，请使用 node -v 确认版本是否在 18 或更高版本。 
> [!NOTE] [图片 OCR 识别内容]
> Cbase) PS
> C:  Users Administrator AppData |Local>
> node
> V22.19


### **2. 安装 Codex CLI** :

- 在终端中运行以下命令进行全局安装：npm install -g @openai/codex 
> [!NOTE] [图片 OCR 识别内容]
> (base) PS C: |Users |Administrator |AppData |Local> npm install
> -9 @apenai/codexl


- 安装好之后输入：codex –version验证 
> [!NOTE] [图片 OCR 识别内容]
> (base)
> PS C: |Users |AdministratorlAppData lLocals codex
> -Version
> codex-cli
> 0.69.0


### **3.配置MCP服务器**

- 在如下目录中找到全局配置文件config.toml 
> [!NOTE] [图片 OCR 识别内容]
> 此电脑
> Win 11 Pro *64 (C:)
> 胪
> Administrator
> COGex
> 刊  排序
> 三  查看
> 修改日期
> 奖
> IO9
> 2025/12/1018;25
> 文件夹
> Sessions
> 2025/11/2014:40
> 文件夹
> authjson
> 2025/12/1016:45
> JSON 文仵
> configtoml
> 2025/11/2014:57
> TOML 文仵
> historyjsonl
> 2025/12/1018:41
> JSONL 文件
> 1 KB
> versionjson
> 2025/12/1018;25
> JSON 文件


- 然后把下面的配置复制进去(相关路径需要自行修改)
  ```
  model = "gpt-5.1-codex-max"model_reasoning_effort = "medium"sandbox_mode = "danger-full-access"[mcp_servers.worldquant-brain-platform]command="D:\\Miniconda3\\python.exe"args=["D:\\Miniconda3\\Lib\\site-packages\\cnhkmcp\\untracked\\platform_functions.py"]description="WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features."alwaysAllow=["get_alpha_details","get_submission_check","check_correlation","read_forum_post","search_forum_posts","get_platform_setting_options","authenticate","get_datafields","get_operators","create_multiSim","get_forum_posts"]enabled = true
  ```
- 验证MCP是否安装成功，命令行中输入：codex mcp list 
> [!NOTE] [图片 OCR 识别内容]
> (base) PS C: Users Administrator lAppData ILocals
> Codex ICP
> list
> Name
> Cammand
> Args
> Env
> Cwd
> Status
> Auth
> worldquant-brain-platforn
> IMiniconda3 python.exe
> 0: IMiniconda3lLiblsite-packages Icnhkmcp luntracked platform_function
> enabled
> Unsupported


### 4.  **命令行中输入：codex 启动** ，此时会提示登录账号，点击链接跳转到浏览器中登录完成即可。 
> [!NOTE] [图片 OCR 识别内容]
> Wetcome
> to Codex
> OpenAI
> command-line coding agent
> Finish signing
> Via
> JOUI
> DrOWser
> If the link doesn
> t open automatically,
> open the
> following link to
> authenticate:
> https: Llauth Openai
> comloauthlauthorize?response_typescodesclient_jdsapp_EMoamEEZT3fockxaxpThrannsredirect_urishttpg3A2
> F2Elocalhost%3Al455%2FauthgzEcallbackescopesopenidgzOprofile%zOemailgzOoffline_accessgcode
> ChallengeUdslhAQVRIZSWVSqU
> eZsUSEWI3HDOLODbLiShGAtBYGcode_Challenge_methodssz56cid
> Loken
> add_@rganizationsstruescodex clisimplified
> flowtruegstat
> eZqifGeWOsgSeNZtEptrB3VEfIBPC
> YyUGaintgRoqNQgoriginatorcodex
> SliIs
 5.  **登录完成后启动codex如下** ： 
> [!NOTE] [图片 OCR 识别内容]
> (base) Ps C: |Users |Administrator |AppData |Local>
> Codex
> OpenAI Codex (vo. 69.0)
> model:
> 1-codex-max medium
> /model to change
> directory:
> IAppData lLocal
> Tip: Start
> fresh idea With /new; the previous
> session stays available in history
> Find
> fix
> in @filename
> 1008
> context left
> ? for shortcuts
> gpt-5
> bug
> and


### 6.  **现在可以愉快地使用MCP进行因子研究了**  
> [!NOTE] [图片 OCR 识别内容]
> tenaeRe
> 
>  Jocr
> 
> Cll =
> UR7Omn[
> 2t
> ON
> C7
> 
> 
> C
> 
> 
> 
> 
> B。 (ed
> 
> 
> C
> 
> 
> 
> 
> 
> 
> 
> 
> 
> R
> 
> 
> 
> Culle
> unNnoOmmeo(
> 
> Sy(antz』_stustor_COssect_fswsJo_satloj
> 
> 
> Caovganlglsststor_eclatwsaatssyajj。 Ptsurysceyagtrlgusls_eogal
> 
> gCnTTtomeotonhrtnmneeo
> 
> 
> 
> TO
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> TCR
> 0
> 
> 
> 
> 
> g
> |!
> 
> 
> 
> 
> NttoFtad
> 
> aTTezlnpus DsOTatrr |Tpastetylzel
> 
> 
> 
> 
> 
> o
> 
> 20mgeC
> 
> ttemoted
> 
> Cutled
> l|OMmm
> 
> teucCUgTIRLLU_
> 
> Cnoeb Pmepnotbn
> 
> 
> 
> 
> 
> 
> 
> 
> oIlRtRCmeoS
> 
> 
> Oo
> 
> OoCg
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> no
> 
> 
> 
> m]
> 
> 
> 
> 
> 
> ]
> 
> 
> 
> o0
> 
> 
> Ch too
> uthun t Cue 1mlr
> Calle
> Nnoemo(
> CJagantzl_erofiesululeyfas_suyst_Rsolltbtrt
> ee_aog(a_usoflubrtts_aalyse_erftgluley_Cgaj
> Calls
> U35AUarAJomnCCasyUor(
> 
> R
> 
> 
> 
> 
> r
> 
> 
> 
> 
> 
> 
> 
> SIe
> 
> 
> 
> 
> Nratheecc
> 
> 
> SCLCTTCR]
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> R
> 
> goC
> @c
> aatupn


---

## 讨论与评论 (2)

### 评论 #1 (作者: YQ84572, 时间: 6个月前)

很详细的codex 配置mcp 的分享，对新人使用codexcli 进行mcp使用很有帮助

====================================================================

一年一个台阶，一步一个脚印

====================================================================

---

### 评论 #2 (作者: 顾问 MZ45384 (Rank 51), 时间: 17天前)

学到了，最近Gemini挂彩了，一直显示current location not available。得转战codex了。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

