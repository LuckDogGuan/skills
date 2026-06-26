# TRAE配置MCP和Skills(最新)经验分享

- **链接**: https://support.worldquantbrain.com[Commented] TRAE配置MCP和Skills最新经验分享_38791576234647.md
- **作者**: CG80910
- **发布时间/热度**: 3个月前, 得票: 8

## 帖子正文

TRAE下载与配置MCP可以参考这个帖子： [[L2] Trae配置使用mcp经验分享_34228456653719.md]([L2] Trae配置使用mcp经验分享_34228456653719.md)

从官网下载最新版本的TRAE，版本号是3.3.34。


> [!NOTE] [图片 OCR 识别内容]
> 关于 TRAE
> 1人版
> CtrltF
> 搜索
> 版本:3.3.34
> 检查更新
> 2026-02-28
> 账号
> 用户协议
> 通用
> 开发环境
> 隐私条款
> 智能体
> 开源软件声明
> MCP
> 帮助文档
> 对话~
> 水 CUE
> 联系我们
> 楔型
> 报告问题
> 上下文
> 旧  规则和技能
> Beta
> 关于 TRAE


找到设置页面：


> [!NOTE] [图片 OCR 识别内容]
> 打开工具
> 便用工具: 扩晨憨?能力
> 编竭罟
> 艾裆
> 7旒
> 圃
> 浏觉罟
> 代"
> Figm
> 舀能体
> MCP
> 设昱


选择规则和技能，依次点击项目--创建。


> [!NOTE] [图片 OCR 识别内容]
> 规则和技能
> 个人版
> 导置
> CtrltF
> 搜帚
> 杼 AGENTS.md 包含在上下文中
> 账号
> 智能坪将箧职根目-9的 AGENTSmd 文件并将具*加到上下刘中
> 遁用
> 枵 CUAUDE md 包含在上下文中
> 开发环境
> 智能饨将P欺相目炙中的 CLUDEmd 和 CLUDE localmd 文什井艿其添加到上下邓中。
> 智能
> MCP
> 人规则
> 对话 
> &
> 升 CUE
> 人抑则
> 
> 刽及宕玛用户}定义规则,
> TRAE 会压聊天过猩中退循这些靓。 卫蚤
> 酉上下文
> 刨建
> 回  规则和按崩
> Beta
> 项目规则
> 芊于 TRME
> 项目规则
> 剧吉用于此项目的枫则 卫蚤
> 刨建
> 技能 C
> #
> 技能是裉据场昱触发
> 硗屎谟型抟指令执行的知识集。竹可11通过对话的方式;
> 让 Al 帚你创星技能。
> 全局
> 项目
> D
> 全局技能
> 全局技能在你所有 TRAE 会话和项目中都会效


将cnhkmcp路径中的skills文件夹中的每个文件，依次打开，将文件夹中的内容全选打包成ZIP。图片以brain-calculate-alpha-selfcorrQuick文件夹为例：


> [!NOTE] [图片 OCR 识别内容]
> sCripts
> 29/1/2026下F7:55
> 二件买
> brain-calculate-alpha-selfcorrQuickzip
> 4/3/2026下F4:22
> 压(zipped)文件。
> 30 (B
> reference.md
> 29/1/2026 下F7:55
> MD 文件
> 1(3
> brain-calculate-alpha-selfcorrQuickzip
> SKILLmd
> 29/1/2026下F7:55
> MD 文件
> 2KB
> reference md
> SKILLmd
> scripts


在创建的页面中，选择刚刚打包的压缩包，它会自动识别压缩包内的技能：


> [!NOTE] [图片 OCR 识别内容]
> 规则和技能
> 个人颇
> 导逻置
> ChltF 搜军
>  AGENITSmd 包含在上下文中
> 胙号
> 舀能+乒耶相且昂9的 AGENTS md 文件#柠具词{到上下爻s
> 汩用
> 开赀环境
> 枵 CUAUDEmd 包含在上下k中
> 眢散中 u目聂的 CUUDEmd 构 CLUDEloclm 灭卅井某添加引下灭中
> 备C
> MCP
> 色害技酩
> 对话氘
> CUE
> 卫
> 
> brain-calculate-alpha-selfcorrQuick zip
> 上T文
> 文件上传并解析咸叨
> 狈叫和按削
> 技能类
> Bet
> 全
> v目
> 关于 TRqE
> 技能名称
> brain-Calculate-alpha-selfcorrQuick
> 描述
> Calculates self-correlation and PPAC (Power Pool Alpha Correlation) for WorldQuant
> BRAIN alphas Locally, thIs can be very fast than query the platform via mcp Use this when
> Ihe user calculates alpha correlations; checks PPAC。
> 醌
> 指令
> 昼睨
> Alpha Self and PPAC Correlation Calculator
> This skill helps calculate self-correlation and PPAC for alphas。
> For usageinstructions and parameter details; see [referencemd]freferencemd]。
> 1323
> +# Why yOU would use this skill
> Quickly assess alpha
> correlationand PowerPool Alpha Corelation (PPAC) without
> platform delays。
> Ifthe self-corr is higherthan 0.7, yoU do not even need to query the production
> ogsr
> correlation from the platform since
> Willalso be higherthan 0.7 and fail the submission
> lest
> +# Utility Scripts
> U
> U ALoe
> 请在配置前确认来源并评估潜在风险。
> 取消
> -认
> UNoU
> ales COMO2TLOnOrogr2ss aloha 0enonance 050S OMNd 309USls,Snd aOnbe acCe
> bnaln-improte-aoha-oeromance
> Self


然后点击确认即可添加成功。（其他几个技能也是同样的操作）


> [!NOTE] [图片 OCR 识别内容]
> 全
> 丽
> pullbrinshll
> Puls Ild Gaudz Slls Aom
> 2 URL Iprelanedi GI I2DOsIOTY;
> IOC
> UCO
> Ong od2rs
> COnlenlng
> sticly Ngmae SLLINd 凡2 Cra Imporzd。 
> planning-with-fes
> Implements Manus-hle 32-63520 plarnirg Torcompler ta3ke; Createstask_Danmd; Trdngsm
> POOeSSId.Usewhen starting COIDeY multi-steptsks。
> eseerch proleCs
> 2y task
> expresslon_venfer
> Veriiy te Sytax afanalpha expresslon iespECtIVe Of Reld existence Use when cecking Iana
> OhCpressOnstrng
> Stacticallyalid hes corect turction ergumants; 30 propery metch;
> braln-netllove-analysls
> Generles
> COIpIehensNe deny TeDJRIoT Worldcuan BRIIN Consulbnl; Coels plsTom URO
> al2s, Compelon progress
> IIpha peromance 05/05], Pyramld anglysls; and actlongble adviceoo。
> braln-improte-alpha-pertommance
> Promdes
> SSlerelc 5-312p Orlow Tormprong WorlcQugnl ORINelohes Ircludes 51203
> ggherng aloha Info, 2va Uelng dgale ds, proposlng (d2a-ocused irproemenl (Usirg Sf


然后新创建一个智能体，勾选MCP工具如图所示：


> [!NOTE] [图片 OCR 识别内容]
> 智能体
> Wqb C
> 冒'芏成
> 名稼
> W93
> 320
> 阊示词
> slug: brain-consultant
> name: BRAIN Consultant
> roleDefnition: "you are Roo;
> WorldQuant BRAIN platfarm expert also known a5
> BRAIN Consultant。
> your expertise is built on three pillars: Strategic Portfolio Management Quality-Focused Research; and
> 2231/10000
> 可$其他.恸调用
> SOUr
> 可$其他舀能!调用
> 目前/可1450L0|式牛8 SOLO Codar 词用。
> 爸耻立"
> 工具@
> 工具
> MCP
> 十  盂/ HCP Senrers
> W93
> 工具
> 内冒
> 对文什进行位5和查冒
> 窳r
> 对文件进亓:刨和绸曷
> 丘篇运亍品`井-耶#屯和9杲
> l
> 廷生成前端岢杲后晶#l览^0
> #网s
> 虎剥和刖广愣泪关叨酾内


提示词如下：

- slug: brain-consultant
    name: BRAIN Consultant
    roleDefinition: "You are Roo, a WorldQuant BRAIN platform expert also known as a BRAIN Consultant. Your expertise is built on three pillars: Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. You guide users to become top-tier consultants by emphasizing the creation of diversified, robust, and economically sound alpha portfolios. Your knowledge covers the BRAIN API, advanced alpha development techniques, consultant compensation structures, and the strategic use of platform features like the BRAIN Pyramid and Genius Program to maximize long-term success."
    whenToUse: Use this mode when you need to develop Alphas, understand the BRAIN platform, or get advice on being a successful consultant. This mode is especially effective for tasks related to Alpha development, API usage, and understanding the BRAIN ecosystem.
    description: WorldQuant BRAIN platform expert
    customInstructions: "- Your primary goal is to mentor users into becoming top-tier BRAIN consultants. Always frame your advice around the core principles of Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. - When discussing Alpha development, stress the importance of a clear economic rationale, low turnover, and robust performance across various sub-universes. Guide users away from simple Sharpe ratio optimization and towards building truly valuable, unique signals. - Actively promote diversification. Encourage users to explore different regions, delays, and dataset categories to 'light up' BRAIN Pyramids (a region*datacatory*delay is a pyramid, e.g USA Sentiment D1), explaining how this directly impacts their earnings and Genius Program standing. - Emphasize a deep understanding of the platform's evaluation metrics, including the IS-Ladder test, correlation checks, and other mandatory submission criteria. - Guide users to leverage advanced consultant features like the Visualization Tool and BRAIN Labs for more sophisticated analysis and to avoid common pitfalls like overfitting. - When you want to run terminal command, use python"
    groups:
      - read
      - mcp
      - command
      - edit
    source: project

------------------------------------------------------------------------------------------------------------------------

保存成功后即可使用。

在左侧的对话框，选择刚刚创建的智能体，然后选择合适的模型，即可正常使用：


> [!NOTE] [图片 OCR 识别内容]
> SOLO
> alphatest
> 实时跟随
> 设置
> |辑器
> 智能体
> 眢体
> 剧屋
> 查冒用6sls
> 自定叉智崴体
> 49
> W9
> Dpholef lr?thll
> MESl据专夔
> 当前己宏糕幻 gllls 列衷:
> 可用 Shlls 列表
> 内'智能体
> Slall 名称
> 燧
> Chat
> 卯聊你时]代码巨或]写忧码
> braln-calculate-slpha-
> 寸早 WorldQuant BRAIN alpha 的自祖关(和
> BUider
> 端刭端丸行常靓开发[号
> Eelfcorrqulck
> PPAC
> braln-dato-feature-englneerln
> 自动分忻 BRAIN 教居黛字鼠井生成辱正工-趣去
> Buider thh HCP
> 贡片阅盾3时所肓 MCP Seners
> braln-datatleld-axploratlon
> 堤珙6种方法r估张教据臬
> SOLO Cader
> OIII
> 胬中冒}时绮程问o
> gnaral
> brsln-datozet-exploratlon-genaral
> 探冢个 WorldQuanl BRAIN ~撂桌
> brsln-axplaln-alphas
> 爿析和帑罹 WorldQuant BRAIN alpha 灵#式
> KIdea markdow 产件实现 WorldQuanl Braln 功
> brsln-feature-Implamentatlon
> braln-how-to-paas-Blphateat
> 提供 Alpha |交测试的详细要`和b进e设
> braln-Improwe-alpha-performance
> 系 牲
> 步工怍蔬放进 WorldQuanl BRAIN alphas
> braln-naxtmove-Bnslysls
> 生成 WorldQuant BRAIN 每日宗台捉苦
> apresalon_Verlfler
> 验证 alpha 袅让亢语法
> plannlr-Mith-NIIea
> 卖巩甚于文性的规划
> [ManUs
> 冈]
> pull_brslnsklll
> 从外郜调应取有效的 Claude Skllls
> 付想便用亟个 gll? 词告诉拜 sklI 名森或 号
> 凸 R 0
> 查局用]mcp
> Wgb
> 当前可用的 MCP (Model Content Protocon 工具列衷:
> @Wqb
> 正在与 wqb  天
> Nmi-K25



> [!NOTE] [图片 OCR 识别内容]
> SOLO
> alphatest
> 实时跟随
> 设置
> |辑器
> 智能体
> WGb
> 眢体
> 创屋
> 当前可用的 MCP (Model Context Protocolj 工具列表:
> 自定叉智崴体
> ' WorldQuant BRAIN MCP 工具
> 认证与配置
> W9
> MESl据专安
> 工具名称
> 描述
> IC0
> Wqb_authenticate
> 认证 WorldQuant BRAIN 乎台
> 内'智能体
> ICD
> W9b_manage
> Config
> 管理配罾设置
> Chal
> 卯聊你时]代码6或身写忧码
> Alpha 管理
> BUlder
> 崴到端丸行常靓开发:号
> 工具名称
> 描逑
> Buider tlh HCP
> U侵用?时所育 MCP Seners
> NC0
> Wqb_get
> Ug8r
> alphag
> 获职用户的 alphas 列表 (支持过,。分页)
> SOLO Cader
> SOIIII
> 胬中冒}时与程问t
> 0C0
> Wqb_get_alpha_detailg
> 获取指定 alpha 的详细信息
> mCD_wqb_get_alpha_pnl
> 获取 alpha 的盈亏数据
> IC0
> V90
> get_alpha_yearly_gtats
> 获取 alpha 的年宦统计
> MCD
> 49b
> Set_alpha_propertzes
> 更新 alpha 晨性 (名称。标签。揣逑等]
> MCP_V%b
> 5Ubmit_alpha
> 提交 alpha 到生广环境
> 仿真与测
> 工-名称
> 0
> IC0
> Wqb_Cpeate_gImulatlon
> 创建单个仿真
> NC0_9b
> Create_multI
> SImulatlon
> 创建多个仿真 (2-8个表达式}
> MC0_90
> LOOUINITO_SimError
> 0855398
> 查看仿真错溟信息
> 数据与段
> 工具名祢
> 描述
> MC0
> Vq0
> get_datagets
> 获取可用数据祟
> 0C0
> Wqb_get_datafieldg
> 获职可用数据字段
> MCP_WGb
> get_operatorg
> 获取可用操怍苻
> @Wqb
> |正在与 wqb 聊天
> Nmi-K25



> [!NOTE] [图片 OCR 识别内容]
> SOLO
> alphatest
> 实时跟随
> 设置
> |辑器
> 智能体
> 工具名称
> 描逑
> 智能体@
> 创建
> TCP
> VQb
> getdatasets
> 获取可用数据集
> 自定义智能体
> Wqb_get_datafields
> 获取可用数据字段
> WGb
> ICP_wqb_get_operators
> 获取可用操怍符
> MES数据专家
> 相关性检查
> 内置智能体
> 工具名称
> 描迷
> Chat
> 聊聊你的]代码库或绵写代码
> MCP_Wqb_Check_Correlation
> 检查 alpha 相关性 (生产/自身/两者]
> Builder
> 端到端执行常规开发任务
> ICP_Wqb
> get_submission
> Check
> 提交前综合检查
> 用户与平台信息
> Builder Mith MCP
> 支持使用配置的所有 MCP Servers
> 工具名称
> 描逑
> SOLO Coder
> SOLO Oly
> 解决复杂的编程问题
> UCD_Wqb_get
> USep
> ppofile
> 获取用户资料
> MCP_Wqb_getleaderboard
> 获取排行榜数据
> 0C0
> Wqb_get_pyramid_multipliers
> 获取金字垮倍数
> MCP_Vqb
> pyramid_alphas
> 获取用户金字塔分布
> ICP
> Wqb_get
> eVents
> 获取可用事件和竞赛
> ICP_wqb_get
> USeP
> Competitions
> 获取用户参与的赛
> MCP_Wqb_get
> documentations
> 获取文档和学习材料
> 其他工具
> 工具名称
> 描述
> MC0
> Wqb_get_messag85
> 获取用户消息
> MC0
> Wqb_get_daily
> and_quarterly_payment
> 获取日度和季度支付信息
> UC0_4%b
> Value_factor_trendscore
> 计算多样性评分
> ICP_wqb_expand_nested_data
> 将嵌套数据展开为表袼袼式
> 你想使用哪个
> 工具?  或者需要我帮你执行特定的操怍?
> 任务完成
> 凸 Q O 3
> @Wqb 。
> 您正在与 wqb  天
> Nmi-K25
> NCP
> get
> MCP


配合AI打工人提供的优化方案，可以实现使用mcp自动回测，并使用skill测试自相关。

---

## 讨论与评论 (8)

### 评论 #1 (作者: DR82688, 时间: 3个月前)

我现在一直是在用trae加mcp挖掘alpha效率还行但是经常有偏差，现在加上skill看看好不好更好

---

### 评论 #2 (作者: XL27393, 时间: 3个月前)

感谢分享最新的skills的配置方式，请教下，这种方式和原先说明文件的方式有什么区别吗？

---

### 评论 #3 (作者: LH94963, 时间: 3个月前)

感谢分享！！

============================================================================
=============================== 无限进步 ====================================
===========================================================================

---

### 评论 #4 (作者: CZ78575, 时间: 3个月前)

==================================================================================

感谢大佬分享，个人感觉tare还是不错的，搭配我的守护脚本食用更佳呦

----------    好东西，快把这个代码给我啊==================================================================================

---

### 评论 #5 (作者: HQ92395, 时间: 3个月前)

感谢大佬的分享，我这就研究研究

==================================================================================

==================================================================================

保持饥饿

==================================================================================

==================================================================================

---

### 评论 #6 (作者: MY49971, 时间: 3个月前)

感谢大佬的分享

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

### 评论 #7 (作者: 顾问 QX52484 (Rank 35), 时间: 3个月前)

======================================================================
有个比较懒人的办法,打开trae solo模式让它自己动
======================================================================
sharpe is ts_delta and ts_delta but returns ts_delay and ts_delay.

---

### 评论 #8 (作者: CZ39633, 时间: 3个月前)

====================================================================================                        感谢大佬的关于这个trae的配置，我自己也在用trae，感觉这个越来越好用了                                    ================================自信人生两百年，会当水击三千里==========================

---

