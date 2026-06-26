# 【AI使用问题解决方案】如何正常登陆antigravity IDE （windows和mac通用），学生认证可以免费一年gemin3pro经验分享

- **链接**: https://support.worldquantbrain.com[L2] 【AI使用问题解决方案】如何正常登陆antigravity IDE windows和mac通用学生认证可以免费一年gemin3pro经验分享_36879336144023.md
- **作者**: EP71225
- **发布时间/热度**: 6 months ago, 得票: 7

## 帖子正文

默认的规则模式是为了给网页访问用的，给软件登录认证，要求设置一下TUN模式，得设置虚拟网卡之类，有些老版本cl软件的TUN模式不可以正常使用，折腾了半天才得出来的结果，成功登录了，尽量用新版本的cl，不要用老版本的。验证登录之前而且要在终端curl -I  [www.google.com](http://www.google.com)  是否显示，前提是出现HTTP 200状态才正常通网。


> [!NOTE] [图片 OCR 识别内容]
> (base)
> wanglang@192
> %
> CUII
> -I https:
> WWW .google
> COm
> HTTP /1.1
> 200 Connection
> established
> HTTP/2
> 200
> content-type:
> text /html;
> charset=Is0-8859-1
> content-security-policy-report-only:
> object-SIC
> none
> base-Uri
> self' ; script-SI
> nonce-9JMwq7kqaQxPWQHMcIvfgg'
> strict-dynamic '
> report-sample
> unsafe-eval '
> unsafe-inline
> https: http: ; report-uri https: / /csp .withgoogle . com/csp /gws /other
> -mp
> accept-ch:
> Sec-CH-Prefers-Color-Scheme
> pB3p:
> CP="This
> is
> not
> P3p policy !
> See
> 9.co/p3phelp
> for
> mOre
> info.
> date:
> Tue ,
> 09
> Dec
> 2025  07:19:02
> GMT
> SETVer:
> gWS
> X-XSS-protection:
> X-frame-options:
> SAMEORIGIN
> expires:
> Tue
> 09
> Dec
> 2025
> 07:19:02
> GMT
> cache-contzol:
> private
> set-Cookie:
> AEC=AaJma5u7HXfRLIGI-ANOW-UsGxYZKZDsHHauuliQ2WoW-h637TYU4IygjAg;
> eXP
> iressSun
> 07-Jun-2026
> 07:19:02 GMT;
> path/;
> domain=.google
> Com;
> Secure;
> Httponly
> Samesiteslax
> set-Cookie:
> NID=527=CZZOdZWwL2HXiPU7HJVnNINScapouS8qXNSO2RFQVY6I33SNYH6Z_MSJKIot
> IWhwVUyxcizfu4gIGf72OVVYXWCMUMZKZVsmSSXV-RUxaoCVeIOFOMtc4pYqlvbHEqAJIW-ONCRZykoQ
> y-xgtvfbZhtpHBghY3NdwdPx3ySoxIWP
> GBHSVqKieEBoKkG
> 5hMGbKZsaGSHaNZkCmXJRNIoKa6OCTo
> b0;
> expires=Wed ,
> 10-Jun-2026
> 07:19:02
> GMT;
> path=/;
> domain=.google. com;
> Httponly



> [!NOTE] [图片 OCR 识别内容]
> 已使用 /总量: 9.3168
> 16868
> 代理组
> 节点选择
> 到期时间:2026-10-24
> 节点
> 6%
> 自动选择
> 网络设置
> 圈 圈 要
> 代理模式
> 系统代理
> 虚拟网卡模式
> 规则
> 全局
> 直连
> TUN 模式已启用。应用将通过虚拟网卡访问网络
> 基于预设规则智能判断流量走向。提供灵活的代理策略
> 虚拟网卡模式
> 流量统计
> 10分钟
> 上传
> 1.2MB
> 下载


mac版本antigravity配合mcp比较好用，我用的学生认证的版本免费一年，学生认证请自行google搜索方法，或者ai搜索，嫌麻烦可以自行买个。


> [!NOTE] [图片 OCR 识别内容]
> 0CLIIIgS
> 7CCUUI LL
> GENERAL
> Enable Telemetry
> When toggled on, Antigravity collects interactions for use in evaluating, developing, and
> improving Antigravity and models that support Antigravity。
> ACCOUNT
> Your Plan: Google AI Pro
> You can upgrade to the Google AI Ultra plan to receive the highest rate
> Upgrade
> limits


不同电脑情况不一样，MAC电脑的mcp配置为：

```
{"mcpServers": {"worldquant-brain-platform": {"command": "/opt/anaconda3/bin/python","args": ["/opt/anaconda3/lib/python3.13/site-packages/cnhkmcp/untracked/platform_functions.py"],"description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features. Includes 25+ MCP tools for authentication, simulation creation, alpha management, dataset access, performance analysis, competition management, user profile operations, forum integration, and advanced analytics."}}}
```

 
> [!NOTE] [图片 OCR 识别内容]
> APP
> mcp_config.json
> Open
> 5
> Task
> Manage MCPs
> {}
> mcp_config.json
> X
> Users
> wanglang
> .gemini
> antigravity
> {}
> mcp_configjson
> 1
> 2
> "mcpServers"
> {
> 3
> worldquant-brain-platform"
> command" =
> /opt/anaconda3 /bin /python"
> 5
> Iargs"
> 6
> /opt/anaconda3/lib /python3.13/site-packages /cnhki
> 7
> 8
> 'description"
> "WorldQuant
> BRAIN Platform MCP Serve
> 9
> 10
> 11
> 12



> [!NOTE] [图片 OCR 识别内容]
> Task
> Manage MCPs
> Manage MCP servers
> 40 |100 tools
> View raw config
> Refresh
> WOF
> worldquant-brain-platform
> Configure
> Enabled
> brain-
> 40
> 40
> plat。
> 1.authenticate
> Authenticate with WorldQuant BRAIN platform. This is the
> first step in any BRAIN Workflow. You must authenticate before
> using any other tools. Args: email: Your BRAIN platform email
> address (optional if in config or .brain_credentials) password:
> Your BRAIN platform password (optional if in config or
> brain_credentials) Returns: Authentication result with user
> info and permissions
> 2. Value_factor_trendScore
> Compute and return the diversity score for REGULAR alphas in



> [!NOTE] [图片 OCR 识别内容]
> 11 |
> L4S
> CCT AgCIIC TaTagC
> U0
> 人 Z
> Explorer
> Task
> VS Code MCP Settings
> 十 &。 X
> APP
> Task
> DOW
> Review
> deltacts_rank(mdl30_smartestimate_fyl
> Cpycache_
> eps,
> 60),
> 10), subindustry) 的含义如
> blueprints
> Locate VS Code global MCP configuration file
> 下
> custom_templates
> Read and analyze MCP configuration
> 1
> 数据字段
> mdl30_smartestimate_fyl
> hkSimulator
> Search for 'platform_functions.py'
> O[
> 'cnhkmcp' package
> ):
> eps
> simulator
> Construct valid MCP configuration with actual paths
> 使用的是 Model 30 (Estimates
> static
> Write configuration to GEMINImd
> Model) 数据集
> templates
> Correctly write configuration to mcp_configjson
> 指的是 SmartEstimate FY1
> Tranformer
> Verify WorldQuant Brain Platform login
> EPS,
> 即对下-财年 (Fiscal Year
> .gitignore
> Explain alpha expression:
> 1) 每股收益 (EPS) 的智能预测
> apP.py
> group_neutralize(ts_delta(ts_rank(mdl3O_smartestimate_fyl_eps, 60), 10),
> 值。
> format_alpha_json.py
> subindustry)
> 2
> 核心逻辑:
> mirror_config.txt
> ts_rank(
> 60)
> 计算该 EPS
> M4
> MODULAR_STRUCTURE.md
> 预测值在过去 60天历史串口中的
> operaters.csV
> 排名 (百分位)
> 这把绝对数值
> M4
> README.md
> 转换为了通过自身历史标准化的
> requirements.txt
> 相对强弱指标 (0到1之间)
> run_app.bat
> ts_deltac.
> 10)
> 计算这个排
> run_app.sh
> 名在过去 10天 的变化量。这捕捉
> setup_tsinghua.bat
> 了 EPS 预测相对强度的动量或改
> Problems
> Output
> Terminal
> Zsh
> 十 v
> @
>  |句 X
> setup_tsinghua.sh
> 善趋势。
> 如果值为正,
> 说明该股
> 囚
> ssrn-3332513.pdf
> (base)
> wanglang@wanglangs
> APP
> %
> 票的 EPS 预测在自身历史看来正
> M4
> transformer_workflow_analysis.md
> 娈得越来越强。
> group_neutralizeC _
> subind
> ustry)
> 对上述计算结果在 子行
> 业 (Subindustry) 层面进行中性
> 0 Background Processes Running


---

## 讨论与评论 (1)

### 评论 #1 (作者: YQ84572, 时间: 5 months ago)

这个谷歌的ide确实比较难搞mcp配置也很奇怪老是不通过，配置了显示链接不上，这篇文章完美的解决了这个问题

--------------------------------------------------------------------------------------------------------------------

感谢分享，祝国区越来越好

--------------------------------------------------------------------------------------------------------------------

---

