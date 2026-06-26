# QuantGo Kit：基于Grafana的WorldQuant量化可视化篇代码优化

- **链接**: https://support.worldquantbrain.com[L2] QuantGo Kit基于Grafana的WorldQuant量化可视化篇代码优化_37495033591447.md
- **作者**: 顾问 ML47973 (Rank 100)
- **发布时间/热度**: 5 months ago, 得票: 14

## 帖子正文


> [!NOTE] [图片 OCR 识别内容]
> Value-at-Risk
> (Vaz)
> 
> Mean
> Probability
> 一8
> CVaRB
> LOss
> VaRp


## **一、2026 开端**

本篇是基于上篇  **[QuantGo Kit：基于Go开发的WorldQuant量化工具箱篇]([Commented] QuantGo Kit基于Go开发的WorldQuant量化工具箱篇代码优化_37163832225943.md)**  存入数据库数据做 Grafana可视化，多维度查看和分析自己做过的 Alpha，以及 操作符Op 和 Combine & vf & wf 等数据 .


> [!NOTE] [图片 OCR 识别内容]
> Quantco Kit: 基于Co开发的WorldQuant量化工具箱篇
> 代码优化
> 顾问 ML47973 (Rank 100)
> QuantGo Kit 为何诞生?
> 去年十月,说错了。今年十月, WorldQuant 围区的
> Drod
> COII
> 比赛启动后。我创建了第一个文件夹;
> 写了个计箅平均
> Drod_
> COII
> 的小工具
> 随着需求增多;一个个独立的小程序相继诞生
> 每个都待在各自的文
> 件夹里
> 很快问题浮现:  文件夹海洋让我迷失方向。相似的命名让查找娈得困难;  想要对比多个程序效果时,不得不
> 开启数个VSCode窗口。管理成本陡增
> 于是,
> 一个想法诞生:  为什么不让它们和谐共处?  将所有工具集成到统一框架下,
> 一键运行
> 即时对比 .当
> 这个工具箱逐渐成型时,我想
> 也许其他人也会需要这样的便利 
> 就这样, Quant * Go Kit 诞生了


Grafana 官方下载中心： `https://grafana.com/grafana/download`  ，我选择下载Grafana到本地，可以不使用Docker启动 . 默认访问地址  `https://localhost:3000` ，首次登录账号/密码  `admin/admin`  .


> [!NOTE] [图片 OCR 识别内容]
> GrafanaLabs
> Products
> Open Source
> Solutions
> Leam
> Docs
> Downloads
> Contact Us
> Signin
> Grafana
> Overview
> Grafana project
> Grafana Alerting
> Download
> Download Grafana
> Nightly Builds
> Grafana Cloud
> You
> can USe
> Grafana Cloud to avoid installing; maintaining; and scaling Your own instance of Grafana. Create a free account to get started, which includes free forever access to
> 10k series Prometheus metrics; 5068 logs, 50GB traces; & more。
> Version:
> 12.3.
> Edition:
> Enterprise
> The Enterprise Edition is the default and recommended edition.
> It includes all the features of the OSS Edition; can be used for free and can be upgraded to the full
> Enterprise feature set, including support for Enterprise plugins.
> License:
> Grafana Labs License
> Release Date:
> December 17, 2025
> Release Info:
> Linux
> Windows
> Mac
> Docker
> Linux on ARNIG4
> Pricing


## 

## **二、Visual Layout**

从大布局来看，Grafana - WorldQuant 项目下包括

1. Alpha Quant (Alpha信息数据)

2. Combin & vf & wf (Alpha表现 / Value_Factor / Weight_Factor)

3. Op Informatization (季度性操作符Op信息)

4. Pyramid alpha distribution (季度 | 非季度性 金字塔数据)

四大板块信息 .


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dashboards
> Ai &
> 8|众
> 首页 〉仪表板
> 搜索
> CtrItk
> 十 ~
> 仪表板
> 新建
> 创建并管理仪表板,以将您的数据可视化
> 搜索仪表板
> 按标签筛选
> 已加星标
> 排序
> 名称
> 标签
> WorldQuant
> Alpha Quant
> 器 Combine & Vf & Wf
> 器 Op Informatization
> 品 Pyramid alpha distribution
> CloudVendor Classified Files
> Riemann's Ideas & Analysis


其中，Alpha Quant 共包括 6个 Row, 分别是 理论与可投资术语、已提交的全部alpha(包括隐藏和sa)、GroupBy 分组、Ts_Mean 时序均值、Value Factor 潜在可能影响情况 与 Osmosis Competition 2025 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dladrrggglalpha-quant?orgld=
> &from= 2025-02-13T16:00:00.000Z8to=nowatimezone=browsergvar-alphalD=&var-type=s
> all8var-geniusquarter=S_all8var-region= $_
> Ai
> 8 |众
> 首页
> 仪表板
> WorldQuant
> Alpha Quant
> 搜索。
> CtrI-k
> 十 ~
> 0
> 添加
> 设置
> 退出编辑
> 保存仪表板
> AlphalD
> 输入数值
> TYPE
> AIl
> GENIUS季度
> AlI
> REGION
> AlI X
> UNIVERSE
> AlI X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> All X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> (1panel)
> 已提交的全部alpha(包括隐藏和sa)
> Danels)
> GroupBy 分组
> (6 panels)
> Ts_Mean 时序均值
> (5 panels)
> Value Factor 潜在可能影响情况
> Danels)
> Osmosis Competition 2025
> (5 panels)


[图片 (图片已丢失)]

Combin & vf & wf 有3个数据表，数据来源于 weight_value_factor 和 combined_alpha_performance 表，可以分析Combine、wf何时开始有数据，以及变化情况 .


> [!NOTE] [图片 OCR 识别内容]
> 首页
> 仪表板
> WorldQuant
> Combine & Vf & Wf
> Q 搜索
> CtrItk
> 十 ~
> 19
> 编辑
> 导出
> 分享
> Combine & Vf & wf
> Vf & Combine update
> Combine
> Time
> 10
> 12
> 13
> Value_factor
> 0.86
> 0.71
> 0.75
> 0.48
> 0.72
> 0.44
> 0.57
> combined_alpha_performance
> 2.14
> 2.39
> 2.03
> 1.71
> 1.78
> 1.84
> combined_selected_alpha_performance
> 1.47
> 1.32
> combined_power_pool_alpha_performance
> 1.79
> 1.45
> 1.53
> 1.63
> 1.72
> genius_level
> Grand Master
> Calculation_date
> 2025-06-28
> 2025-07-20 2025-08-07
> 2025-08-19
> 2025-09-11
> 2025-09-20
> 2025-10-06
> 2025-10-25  2025-11-20
> 2025-11-21 2025-12-08  2025-12-162026-01-06
> Vf & Combine '折'线图
> 2.6
> 0,86
> 2,39
> 24
> 0,8
> 2.14
> 22
> 0.75
> 2.03
> 0.72
> 0.71
> 0
> 1,84
> 1.79
> 1.,78
> 1.71
> 1.721.8
> 1.63
> 06
> 53
> 0.57
> 1.6
> 1.45
> 1.321.4
> 0.5
> 48
> 0.44
> 1.18
> 1.2
> 04
> 06/28
> 07/05
> 07/12
> 07/19
> 07/26
> 08/02
> 08/09
> 08/16
> 08/23
> 08/30
> 09/06
> 09/13
> 09/20
> 09/27
> 10/04
> 10/11
> 10/18
> 10/25
> 11/01
> 11/08
> 11/15
> 11/22
> 11/29
> 12/06
> 12/13
> 12/20
> 12/27
> 01/03
> Value_factor
> combined_alpha_performance
> combined_selected_alpha_performance
> combined_power_pool_alpha_
> performance
> 1.18


[图片 (图片已丢失)]

Op Informatization 板块目前只包括 operators 表数据，只存了一个图表，支持操作符 / 操作符类别 / Scope 类别 / Genius等级 / Genius季度 等过滤，这个板块我想要做的是 等季度更新之后，再做一个比较的图表，比如: 2025-Q4 与 2026-Q1 操作符比较，掉级导致操作符少了哪些 信息 .


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dladgzmgm/op-informatization?orgld = 18from=now-Gh8to=nowgtimezone=browsergvar-OpName=&var-Category=$
> all8var-Scope=$_
> all8var-Geniuslevel= $_
> alI8Var。。
> A》 &
> 8 |众
> 首页
> 仪表板
> WorldQuant
> Op Informatization
> 搜索。
> CtrI-k
> 十~
> 编辑
> 导出
> 分享
> 操作符名
> 输入数值
> 操作符类别
> AII
> Scope类别
> AlI
> Genius等级
> AlI X
> Genius季度 0
> AlI X
> Op操作符表
> name
> category
> SCODe
> definition
> en_description
> Cn
> add
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> addlxi
> Y, filter
> falsel X + Y
> Add all inputs (at least 2 inputs required). If filter
> true  filterall
> eXP
> Arithmetic
> ["COMBO
> "REGULAR" "SELECTION"]
> eXP(X)
> Natural exponential function: e^x
> multiply
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> multiply(x ,y
> filter-false), X
> Multiply all inputs. At least 2 inputs are required. Filter sets the
> sign
> Arithmetic
> ["COMBO
> "REGULAR" "SELECTION"]
> sign(x)
> 讦 input
> 0, return 1; if input
> 0, return -1; if input
> 0, return 0;
> sUbtract
> Arithmetic
> ["COMBO"
> REGULAR" "SELECTION"]
> subtractlx, Y, filter-false), X -Yy
> X-Y.If filter
> true, filter all input NaN to 0 before
> subtracting
> pasteurize
> Arithmetic
> ["COMBO" "REGULAR"]
> pasteurizelx)
> Set to NaN 讦f Xis INF or if the underlying instrument is notin the
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> Iog(x)
> Natural logarithm. For example: Log(high llow) uses natural logal
> purify
> Arithmetic
> ["COMBO
> "REGULAR", "SELECTION"]
> purify(x)
> Clear infinities (+inf, -inf) by replacing with NaN
> arc_tan
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> arc_tan(x)
> This operator does inverse tangent of input
> log


## **三、详细说明 Alpha Quant 板块**

Alpha Quant 板块 数据来源于 active_alpha_list 数据大表，其中包括了几乎alpha接口的所有数据，不包括 alpha Pnl 数据，然后


> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> AlI
> REGION
> AIl
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> All X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值


**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> OYmgll2
> TYPE 0
> AII X
> GENIUS季度
> AII
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE @
> AII X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
**

**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> AII
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AII X
> STATUS
> AlI X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 样本内-单位收益;非使用例: !二 5%0
> 理论与可投资术语
> panel)
**

**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> OYmgll2
> TYPE 0
> AII
> GENIUS季度
> AlI
> REGION
> AII X
> UNIVERSE
> AIl
> DELAY
> AIl
> NEUTRALIZATION
> AII
> MAX TRADE 0
> AII X
> STATUS
> DECOMMISSIONED X
> xQ
> SHARPE 0
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> Selected (1)
> 理论与可投资术语
> panel)
> AII
> 已提交的全部alpha(包括隐藏和sa)
> ACTIVE
> Submitted Alphas (同网页端)
> DECOMMISSIONED
> 100
> UNSUBMITTED
**

过滤字段 包括 AlphaID 可以查询某一个alpha的信息，TYPE分类 ra 与 sa，alpha 属于哪个大区、股票池、延迟处理 和 中性化等等，以及 Alpha的状态，还有 alpha满足 sharpe、fitness、returns 和 margin 等等，所有过滤条件对 Alpha Quant 板块所有数据图表支持查询过滤 .


> [!NOTE] [图片 OCR 识别内容]
> 首页
> 仪表板
> WorldQuant
> Alpha Quant
> Q 搜索
> CtrItk
> 十 `
> |
> 编辑
> 导出
> 分享
> AlphalD
> 输入数值
> TYPE @
> AIl
> GENIUS季度 @
> AlI
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY @
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AI
> STATUS @
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 25-02-15
> 2025-03-11
> 2025-04-04
> 2025-04-28
> 2025-05-22
> 2025-06-15
> 2025-07-09
> 2025-08-02
> 2025-08-26
> 2025-09-19
> 2025-10-13
> 2025-11-06
> 2025-11-30
> 2025-12-24
> Submitted Alphas (每日提交和累计总和)
> 800
> 700
> 600
> 500
> 400
> 300
> 200
> 100
> 02/14
> 03/01
> 03/16
> 03/31
> 04/15
> 04/30
> 05/15
> 05/30
> 06/14
> 06/29
> 07/14
> 07/29
> 08/13
> 08/28
> 09/12
> 09/27
> 10/12
> 10/27
> 11/11
> 11/26
> 12/11
> 12/26
> 每曰提交数
> 暴计总和
> 已提交全部alpha(包括sa)
> id 5
> type ?
> author
> instrument_type ?
> region ?
> universe 5
> delay ?
> decay
> neutralization
> truncat
> OmWI2gQk
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
> TOP5O0
> 18
> MARKET
> OmWlJNmG
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> ILLIQUID_MINVOLIM
> STATISTICAL
> ONK3wVq
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> INDUSTRY
> OVaRQV8
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> STATISTICAL
> OXNXEI2
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> SUBINDUSTRY
> OY32dmq
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> 100
> SUBINDUSTRY
> 0Ymgll2
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> SUBINDUSTRY
> 13eKO8R
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR
> T0P2500
> 10
> SUBINDUSTRY
> 1837Vr0
> PFFIII 40
> AAI ^7072
> FOIIITV
> FUNI
> TODnnnl
> FOOIININIC
> active regular alpha
> active superalpha
> id
> region
> universe
> delay
> decay ?
> neutralizatior
> type
> author
> instrument_type
> region
> O1ZJp7r
> ASI
> MINVOLIM
> INDUSTRY
> OmWI2gQk
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
>  OJO3AgP
> GLB
> TOP3O00 
> 10
> REVERSION_AND_MC
> 2rkLkpVW
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
> OJYZYOV
> USA
> TOP3000
> SECTOR
> 3v1gVle
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR
> OL53m3p 
> EUR
> TOP2500
> SUBINDUSTR
> 58XG3NJo
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> JPN
> 0LgKQ7q
> GLB
> TOP3000
> SUBINDUSTA
> GQSZrRE
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> OUzrgk 
> USA
> TOP3O00 
> STATISTICA
> GXmeKNYp
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> Om352Irr
> USA
> ILLIQUID_MINVOLIM
> STATISTICA
> GXOKW3k5
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR


已提交的全部alpha(包括隐藏和sa)  包括（日期已经匹配了美国夏冬令时）5个图标，总体来说就是描述随着日期 Alpha 的提交量，以及已经提交的所有 Alpha 列表，还有就是分成 ra 与 sa 的两个小图表 .

其中 Submitted Alphas (同网页端) 图表就是模仿 WorldQuantBrain  [performance](https://platform.worldquantbrain.com/profile/performance)  做的，不过比平台多了一些查询功能 (图表太多，下面就不展示过滤功能了)，平台只显示了整体每一天总的提交量，无法区分ra 与 sa分别交了多少， 交的是哪个Region的，Grafana支持 Type 与 Region 等过滤查询 .


> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE
> SUDer
> GENIUS季度
> All
> REGION 0
> AII
> UNIVERSE
> AII
> DELAY
> AlI X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AII X
> STATUS
> AII
> SHARPE 0
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN 0
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 0.4
> 0.2
> '025-07-02
> 2025-07-15
> 2025-07-28
> 2025-08-10
> 2025-08-23
> 2025-09-05
> 2025-09-18
> 2025-10-01
> 2025-10-14
> 2025-10-27
> 2025-11-09
> 2025-11-22
> 2025-12-05
> 2025-12-18



> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> All
> REGION
> HKG
> UNIVERSE
> AlI X
> DELAY 0
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE
> AII X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 2.5
> 0.5
> 2025-10-13
> 2025-10-17
> 2025-10-21
> 2025-10-25
> 2025-10-29
> 2025-11-02
> 2025-11-06
> 2025-11-10
> 2025-11-14
> 2025-11-18
> 2025-11-22
> 2025-11-26
> 2025-11-30
> 2025-12


[图片 (图片已丢失)]

GroupBy 分组 Row 就是将 Alpha 按照 Region / Neutralization / Universe / Delay / Decay 分组，可以查看 Alpha 大体主要是交在了哪些 Region / Neutralization 等 .


> [!NOTE] [图片 OCR 识别内容]
> GroupBy 分组
> Region
> Decay (count > 5)
> 350
> 250
> 300
> 200
> 250
> 200
> 150
> 150
> 100
> 100
> 50
> 50
> USA
> EUR
> ASI
> GLB
> KOR
> JPN
> CHN
> AMR
> HKG
> TNN
> IND
> 10
> 16
> 20
> 30
> 40
> 60
> 100
> 200
> 512
> Universe
> Neutralization
> 300
> 300
> 250
> 200
> 200
> 150
> 100
> 100
> 50
> Type
> Delay
> regularalpha
> ra
> atom
> Ppa
> 无延迟
> superalpha
> 有延迟
> 128
> 256
> 512
> 1.02
> 512
> MINVOLIM
> TOP1OOO
> TOP1200
> TOP16OO
> TOP2OOOU
> TOP2500
> TOP3000
> 400
> TOPSOO
> TOP8OO
> MINVOLIM
> TOPGOO
> RAM
> Statistical
> Factors
> Factors
> Factors
> Market
> Sector
> Industry
>  Subindustry
> Factors
> None
> TOPC
> Fast
> Fast 
> Crowding
> Slow
> ILLIQUID_
> SIOW


从上面图表中，我能够很清楚的知道，主要交的 Alpaha 在 USA / TOP3000 / Subindustry / decay = 4，这个也正是符合最开始做 WorldQuant 时，国区老师们交我们 setting 的参数 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Ts_Mean 时序均值
> 日度因子指标均值
> 140%
> 400 %oo
> 120%
> 100%
> 300 %00
> 80%
> 200 %oo
> 60%
> 40%
> 100 %oo
> 20%
> 0%
> 9o00
> 02/14
> 03/13
> 04/07
> 05/02
> 05/27
> 06/21
> 07117
> 08/12
> 9/06
> 10/01
> 10/26
> 11/20
> 12/15
> sharpe
> fitness
> turnoVer
> drawdown
> 「eturns
> margin
> 月度因子指标均值
> Name
> Max
> Mean
> 25%
> 50 %00
> sharpe
> 2.15
> 1.72
> fitness
> 1.82
> 1.50
> 20%
> 50 %oo
> turnoVer
> 0.223
> 0.157
> 1.5
> 40 %ooo
> drawdown
> 24.7%
> 12.5%
> 159
> returns
> 20.1%
> 13.8%
> 30 %oo
> margin
> (右侧Y轴)
> 61.9 %00
> 41.4 %00
> 109
> 20 %oo
> 0.5
> 5%
> 10 %oo
> 9o00
> 2025-02
> 2025-03
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
> 2026-01
> 月度因子指标均值
> 2.2
> 25%
> GO %ooo
> 20%
> 50 %ooo
> 1.8
> 40 Vooo
> 16
> 15 %
> 30 %oo
> 10%
> 20 %oo
> 02/14
> 03/01
> 03/16
> 03/31
> 04/15
> 04/30
> 05/15
> 05/30
> 06/14
> 06/29
> 07/14
> 07/29
> 08/13
> 08/28
> 09/12
> 09/27
> 10/12
> 10/27
> 11/11
> 11/26
> 12111
> 12/26
> sharpe
> fitness
> turnoVer
> drawdown
> 「eturns
> margin
> 季度因子指标均值
> 50 %00
> Name
> Max
> Mean
> 20%
> 1.75
> sharpe
> 1.86
> 1.68
> 50 %oo
> 1.5
> ftness
> 1.70
> 1.48
> 159
> tUrnOVeT
> 20.6%
> 15.9%
> 1.25
> 40 %oo
> drawdown
> 16.4%
> 12.9%
> 30 %oo
> 「etUrns
> 16.1%
> 14.0%
> 109
> 0.75
> margin
> (右侧Y轴)
> 57.9 %oo
> 40.6 %00
> 20 %0o
> 0.5
> 59
> 10 %0o
> 0.25
> 9000
> 2025-01
> 2025-02
> 2025-03
> 2025-04
> 2026-01
> 年度因子指标均值
> 1.75
> Name
> Max
> Mean
> 15%
> 35 %oo
> Sharpe
> 1.71
> 1.55
> 1.5
> 30 %oo
> fitness
> 1.47
> 1.37
> 12.5%
> 1.25
> tUTIOVeT
> 15.7%
> 14.4%
> 25 %00
> 10%
> drawdown
> 16.4%
> 14.8%
> 20 %oo
> 「EtUrns
> 13.5%
> 13.4%
> 7.5%
> 0.75
> IIIUIIIL
> 15 %00
> margin
> (右侧Y轴)
> 38.0 %oo
> 33.5 %00
> 5%
> 0.5
> 10 %0
> 2.5%
> 0.25
> 5 %ooa
> 0%
> Vooo
> 2025年
> 2026年


Ts_Mean 时序均值 Row 记录了 Alpha 主要指标的均值，包括 sharpe、fitness、turnover 和 margin， 以此来分析 vf 可能和哪些数据有关，或者与哪些数据的组合有关 (这块是我想要做的)，你想要单独比较某列数据，你就
 
> [!NOTE] [图片 OCR 识别内容]
> 月度因子指标均值
> 51.9 93
> Name
> Max
> Mean
> 50 %0o
> sharpe
> 2.15
> 1.72
> 55.2 %
> 52.1
> fitness
> 1.82
> 1.50
> 48.2 %ooo
> 50 %000
> 45.7 %oco
> tUrnoVer
> 0.223
> 0.157
> 40 %ooo
> grawdown
> 24.7%
> 12.5%
> 35.9 %
> 35.8 %
> returns
> 20.1%
> 13.8%
> 29.1 %ooo
> 30 %oo
> 26.7 Socs
> margin
> (右侧Y轴)
> 61.9 %oo
> 41.4 %0
> 22.0 %co
> 22.2 %ooo
> 20 %0o
> 10 %ooo
> 9o00
> 2025-02
> 2025-03
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
> 2026-01


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 潜在可能影响情况
> 季度型滑动窗口因子指标均值
> 5O %ooo
> Name
> Max
> Mean
> 17.5%
> 1.75
> sharpe
> 1.86
> 1.72
> 50 %oo
> 15%
> 1.5
> fitness
> 1.74
> 1.52
> turnoVer
> 18.1%
> 16.0%
> 12.5%
> 1.25
> 40 %ooo
> drawdown
> 16.5%
> 12.7%
> 10%
> 30 %oo
> returns
> 16.8%
> 14.4%
> 7.5%
> 0.75
> margln
> (右侧〈轴〉
> 57.3 %00
> 44.2 %0
> 20 %oo
> 5%
> 0.5
> 10 %oo
> 2.5%
> 0.25
> 0oo
> %oo
> 2025-020304
> 2025-030405
> 2025-040506
> 2025-050607
> 2025-060708
> 2025-070809
> 2025-080910
> 2025-091011
> 2025-101112
> 普通
> 有条件
> 正式顾问指标均值
> 209
> 000
> Name
> Max
> Mean
> G00
> 1.75
> 17.59
> alpha因子数量
> 588
> 263
> 50 %oo
> 500
> sharpe
> 1.82
> 1.76
> 1.5
> 15%
> fitness
> 1.67
> 1.58
> 40 %oo
> 1.25 400
> 12.590
> turnOVeT
> (右侧Y轴)
> 18.6%
> 16.5%
> 10%
> 30 %oo
> drawdown
> 13.8%
> 11.9%
> 300
> returns
> 15.9%
> 14.8%
> 0.75
> 7.5%
> 20
> 200
> margin
> (右侧Y轴)
> 57.1 %oo
> 47.7 %00
> 0.5
> 5%
> sharpe_std
> 0.944
> 0.585
> 100
> 10 %00
> 0.25
> 2.59
> returns_std
> 11.1%
> 9.61%
> 0%
> 9000
> 通顾问
> 有条件顾问
> 正式顾问
> 正式研究顾问前后指标均值
> Name
> Max
> Mean
> 1.75
> G00
> 15%
> 50 %0
> alpha因子数量
> 588
> 395
> 1.5
> 500
> sharpe
> 1.78
> 1.73
> 12.5%
> 7.25
> 40 %ooo
> ftness
> 1.66
> 1.53
> 400
> 109
> tUrnOVeT
> (右则Y轴)
> 16.5%
> 15.9%
> 30 %0
> drawdown
> 13.8%
> 12.5%
> 300
> 7.5%
> 0.75
> returns
> 15.8%
> 14.3%
> 20 %oo
> 200
> 59
> margin
> (右侧Y轴)
> 54.9 %0o
> 43.5 %00
> 05
> 0.25
> 100
> 2.5%
> 10 %0
> 00o
> Vooo
> 成为顾问前
> 成为顾问后


Value Factor 潜在可能影响情况 Row 记录了 vf 可能会被什么数据影响，以及 vf 是按照 季度型滑动，所以我记录了 2025-040506， 2025-070809 这样的均值数据 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Osmosis Competition 2025 All Alpha
> id 9
> regular_code ?
> osmosis_points ?
> region ?
> universe ?
> neutralization
> OXNXEI2
> if_else(pvl3_reve
> al >=0,1,21
> if_e
> 2000
> USA
> TOP3000
> SUBINDUSTRY
> QNRTLqQ
> std_dev(mdl77
> tOr_as
> 2000
> USA
> TOP3000
> SUBINDUSTRY
> 1YQIAjvz
> jump_decay(pv87_ivy_opr
> Ivcallmputs3, 60, sensiti
> 0.1)
> 2000
> USA
> TOP3O00
> REVERSION_AND_MC
> 2AmOQYZ
> ts_sum(lanl4_
> gric_low)
> 31l4_[OLa
> 951
> group
> lensify(close 2000
> USA
> TOP3000
> SUBINDUSTRY
> REORbA1
> Win
> backfill(implied_volatility_call 180
> 10,2), std
> 9),C2000
> USA
> TOP3O00
> SUBINDUSTRY
> SEGaPpk
> grOUP
> rallze
> tincome_
> T,densify 2000
> USA
> TOP3000
> SUBINDUSTRY
> SGZrgIN
> sentiment
> delay
> 21,20); Vhat
> ression(volume sentimE 2000
> USA
> TOP3O00
> SUBINDUSTRY
> GGKISVE
> ts_sumlpowerlpower(zsco
> delay(powe
> DS「
> 0000
> USA
> TOP3000
> SECTOR
> 7LVLKKZ
> ts_sum((anl4_gric_hi
> 9014
> anl4_tot
> Iow  78)
> 000
> USA
> TOP3000
> SUBINDUSTRY
> group by Region
> group_by Universe
> alpha_count
> 175K
> alpha_count
> 100K
> total_points
> total_
> points
> 150K
> avg_points
> avg_points
> 80K
> 125K
> 60 K
> 1O0K
> 75 K
> 40K
> 50K
> 20K
> 25K
> USA
> GLB
> EUR
> ASI
> MINVOLIM
> TOP3000
> TOP2500
> ILLIQUID_MINVOLIN
> group_by Neutralization
> group_by Decay
> 150k
> alpha
> CoUnt
> 120K
> gecay
> total_points
> alpha_count
> 125K
> 100K
> avg_points
> total_points
> 100K
> avg_points
> 80K
> 75 K
> 60 k
> 50K
> 40k
> 25k
> 20k
> 2K 2K 2K 2K 2K 2K 2K 2K 2K
> 2K10K10K 2K 2K 2K 2K 2K 2K 2K 2K
> gric
> FAST
> INDUSTRY
> FAST
> SUBINDUSTRY
> MARKET
> SECTOR
> MOMENTUM
> CROWDING
> STATISTICAL
> SLOW_AND
> REVERSION_AND


Osmosis Competition 2025 Row 记录了  Osmosis 比赛 被选中的 Alpha，以及 Alpha 被分配了多少分，以及按照某些字段分组图标.
 
> [!NOTE] [图片 OCR 识别内容]
> https:/Iplatform worldquantbrain.com/competition/0C2025
> 出 AI 众
> { |众
> WORL
> 鬯"
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> { Competitions (5)
> Community
> @ $ & 三
> This competition starts on December 15th, 2025 at 1:00:00 PM CST and ends on January Sth, 2026 at 12:59:59 PM CST。 
> Osmosis Competition
> Score
> Leaderboard
> Guidelines
> FAQ
> OSMOSIs
> 2025
> 2025-26
> Aggregate by:
> University
> Country
> Region
> Filter
> Rank
> User
> Total
> Combo IR
> Alphas
> Points
> Daily
> Combo IR
> Alphas
> Points
> Daily
> Combo IR
> Alphas
> Scoreas
> Rank
> USA
> Allocated
> PNL USA
> Rank
> GLB
> Allocated
> PNL GLB
> Rank
> EUR
> on Dec
> USA
> USA
> GLB
> GLB
> EUR
> 29th
> 顾问 ML47973 (Rank 100) (Me)
> 63,183
> 98,529
> 50
> 100,000
> 68,392
> 99,529
> 10
> 100,000
> 61,655
> 51,805
> DA98440
> 78,562
> 82,353
> 100,000
> 19,767
> 37,562
> 100,000
> 34,785
> 85,740
> 儿71699
> 77,823
> 97,059
> 100,000
> -14,867
> 93,321
> 100,000
> -31,197
> 76,895
> X42289
> 76,265
> 64,706
> 100,000
> 29,421
> 97,959
> 100,000
> 10,707
> 78,339
> AM112075
> 75,547
> 93,934
> 26
> 100,000
> 48,545
> 89,425
> 100,000
> -38,506
> 74,368
> Y815978
> 74,474
> 99,265
> 25
> 100,000
> -15,368
> 53,432
> 100,000
> -4,331
> 99,278
> 0X52484
> 73,278
> 88,971
> 20
> 100,000
> 17,561
> 82,746
> 20
> 100,000
> 8,101
> 72,744
> User


USA 分配了50个 Alpha, GLB分配了10个 Alpha，都是均分 .  从结果上来看，USA 和 GLB 的 Combo IR Rank 都还不错 .

## **四、**  **智源勘探 (Intellisource Prospecting)**

Grafana - WorldQuant 项目我还想要补全，但是还未完成的 :

1. 为了方便同时查看所有 Alpha 的 PnL 数据，可以使用 Grafana 的 JSON API 插件，通过登录 WorldQuant Brain 账号直接接入数据 . 只要在插件中配置好 PnL 接口（例如： `https://api.worldquantbrain.com/alphas/{alpha_id}/recordsets/pnl` ），并利用  `alpha_id`  变量，理论上就能在同一个面板中动态展示不同 Alpha 的 PnL . 但我对 API 返回的数据格式不太熟悉，不确定在 Grafana 中具体应该如何配置查询和字段映射 . 如果有类似的经验或成功配置过，欢迎在评论区分享，非常感谢！

2. Value_Factor (vf) 这个数据，大家都比较关心，在排除他人影响的情况下，想要通过自己的 sharpe、fitness、 returns 和 margin 等数据构建某种线性 | 非线性函数，拟合自己的 vf，得到一个大致接近有预测自己下一次的 函数 .

3. 补全 Alpha Quant 板块的 理论与可投资术语 Row，使用 轻量级标记语言 Markdown 丰富，可以写记录 一些公式 比如：sharpeRatio = (Rp - Rf) / σp ，Equal Weight PnL、Combo PnL、Investability Constrained PnL 和 Risk Neutralized PnL曲线图表，记录它们之间的关系，比如，当 Max Trade = OFF 时，Combo PnL 与 Investability Constrained PnL 走势背驰意味着什么 等等，方便大家记录和学习 .

## **五、**  **Grafana Visualization JSON 共享**

当下载好 Grafana 后， 接上篇下载数据进数据库并导入评论区 Grafana JSON 数据，便可以多维度查看和分析自己的 Alpha 啦 .

---

## 讨论与评论 (5)

### 评论 #1 (作者: 顾问 ML47973 (Rank 100), 时间: 5 months ago)

1. worldquant_program_collection 项目 + 2. grafana json

github :  [https://github.com/Epsilon-Riemannian/worldquant_program_collection](https://github.com/Epsilon-Riemannian/worldquant_program_collection)

gitee :  [https://gitee.com/riemannian/worldquant_program_collection](https://gitee.com/riemannian/worldquant_program_collection)

baiduwangpan :  [https://pan.baidu.com/s/1oAZOD1oLFbFI4qJyishzHA?pwd=9jvc](https://pan.baidu.com/s/1oAZOD1oLFbFI4qJyishzHA?pwd=9jvc#list/path=%2F)  (初始版，不再更新)

---

### 评论 #2 (作者: WF69827, 时间: 5 months ago)

高手！看着就很专业，这才是我们国区当之无愧的顾问

---

### 评论 #3 (作者: 顾问 LW67640 (Rank 24), 时间: 5 months ago)

这个可视化厉害了，感谢分享。

早就听说了Grafana做可视化大屏厉害，一直没有动手，现在跟着大佬都教程可以做起来了。

------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------------------

---

### 评论 #4 (作者: JR57542, 时间: 5 months ago)

学到了，真的很好看！

---

### 评论 #5 (作者: MY49971, 时间: 3 months ago)

看着就很厉害，感谢大佬开源

===================================================================================
===================Talk is cheap,show me the alpha=================================

---

