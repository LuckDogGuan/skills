# 【Community Leader -因子筛选与组合⭐】本地数据库的使用(筛选)代码优化

- **链接**: [L2] 【Community Leader -因子筛选与组合】本地数据库的使用筛选代码优化.md
- **作者**: 顾问 WL27618 (Rank 97)
- **发布时间/热度**: 6 months ago, 得票: 74

## 帖子正文

在成为新顾问的阶段, 一个很具体的问题就是: 究竟有没有必要建立一个本地的数据库存放和筛选回测过的alpha呢?

虽然平台的  [https://platform.worldquantbrain.com/alphas/](https://platform.worldquantbrain.com/alphas/)  功能已经提供了众多的筛选条件, 随着回测alpha变多, 还是有一些筛选功能是没覆盖到的, 每次都抓耳挠腮感觉自己的alpha失踪了.

下面我分享一些我自己经常使用的一些数据库筛选功能, 如果需要这些 **额外** 的功能, 结论就是 **需要建立一个本地的alpha数据库** .

 
> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> Search Regular
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 00
> Max Turnover (%^
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> eT
> Sharpe
> Created
> #
> priority_
> #Kq2WpqNP_sign_turnover_
> priority
> Xg533dJl
> ASI
> 1.32
> 1.21
> 10.45%
> 4.37%
> 47.86%oo
> 0.94
> 2025-11-30
> LOW_SHARPE UNITS,IS_LADDER_SHARPE,MATCHES
> #
> _priority_
> #Kq2WPqNP_sign_turnover
> priority
> npMjjLKM
> ASI
> 1.27
> 1.16
> 10.38%
> 4.56%
> 45.52%o。
> 0.92
> 2025-11-30
> LOW_SHARPE LOW_2Y_SHARPE,MATCHES_THEMES
 

这是我的筛选界面, 比较常用的有4个功能

1. **表达式的部分匹配**
2. **alpha id**
3. **距离今天多少天之内**
4. **is check具体条件**


> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计算 Co
> oth
> I0
> Region
> Delay
> Days Before
> Min Turnover (96
> Max Turnover
> 0?
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> Turnov
> Margi
> Sub-U
> Date
> Regular
> I0
> Message
> Pnl
> BI
> Sharpe
> Created
> ts_target_tvr_delta_limit(sign(filter(ts_max(sqrt(ts
> ZYeQ35ZX
> JPN
> 1.06
> 0.71
> 5.56%
> 3.11%
> 35.699oo 1.02
> 2025-11-28
> LOW_SHARPELOW_FITNESS UNITSIS_LADDER_SH'
> 查看
> ts_target_tvr_decay(ts_returns(ts
> max(-1/ts_back。。
> gJEgWaZe JPN
> 1.02
> 0.61
> 4.49%
> 9.14%
> 9.82%。
> 0.82
> 2025-11-27
> LOW_SHARPELOW_FITNESS CONCENTRATED_WEIC
> 查看
> #_priority_
> #POJpWggL_operator_transfer
> prior..NIvGkSkW
> GLB
> 1.49
> 0.76
> 4.59%
> 17.44%
> 5.26%oo
> 1.06
> 2025-11-25
> LOW_SHARPE LOW_FITNESS,LOW_GLB_EMEA_SHAI
> 查看



> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> oth515_is_open
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 91
> Max Turnover
> 0
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> Sub-U
> Date
> Regular
> I0
> Message
> P
> eT
> Sharpe
> Created
> ts_target_tvr_delta_limit(sign(filter(ts_max(sqrt(ts。
> ZYeQ35ZXJPN
> 1.06
> 0.71
> 5.56%
> 3.11%
> 35.69%o。 1.02
> 2025-11-28
> LOW_SHARPELOW_FITNESS,UNITS,IS_LADDER_SHI



> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计算
> tS
> COTr
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 00
> Max Turnover (%~
> Min Margin (%oo)
> Min Return (9ool
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> Pnl
> eT
> Sharpe
> Created
> signal = scale(ts_corr(adv2O,low; 5) +(hightlow)l2-
> LKZ3rpM EUR
> 90
> 3.39
> 1.29
> 10.95%
> 75.42%
> 2.90%oo
> 1.8
> 2025-05-05
> LOW_FITNESS,HIGH_TURNOVER UNITS,UNITS,MATC
> 查看
> signal = scale(ts_corr(adv2O,low; 5) +(hightlow)l2-.
> 5JjbZ5z
> EUR
> 90
> 3.39
> 1.29
> 10.95%
> 75.42%
> 2.90%oo
> 1.8
> 2025-05-05
> LOW_FITNESS,HIGH_TURNOVER UNITS UNITS MATC
> 查看
> CC
 
表达式可以直接查找任何前缀, 字段, operator


> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计
> Search Regular
> I0
> Region
> Delay
> Days Before
> Min Turnover
> Max Turnover (%;
> LOW_ROBUST_UNIVERSE_SHARPEWITH_RATIO
> IS_LADDER_SHARPE
> Min Margin (%oo)
> Min Return (%oo)
> REVERSION_COMPONENT
> LOW_2Y_SHARPE X
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> Pnl
> eT
> Sharpe
> Created
> 3 =
> signed_power(ts_product(to_nan(ts_backfill(V
> XAKw3xpn GLB
> 3.76
> 2.3
> 4.67%
> 8.49%
> 11.0O%oo 2.1
> 2025-10-03
> REVERSION_COMPONENT MATCHES_THEMES
> 查看
> tail(-(ts_backfill(close, 252)
> last_diff_value(ts_ba.j2vaWP7e IND
> 3.29
> 1.9
> 20.24%
> 60.71 %
> 6.6790。
> 1.91
> 2025-11-02
> HIGH_TURNOVERREVERSION_COMPONENTMATCH
> 查看
> signal
> group_neutralize(ts_median(-vec_avg(rsk. Vkvwapbo GLB
> 2.87
> 3.29
> 16.43%
> 9.09%
> 36.15%o。 2.31
> 2025-10-03
> REVERSION_COMPONENT MATCHES_THEMES
> 查看
> signal-ts_backfill((vec_avg(anl6g_best_target_hi) ).
> gXRQoke
> EUR
> 87
> 2.63
> 1.84
> 8.75%
> 17.79%
> 9.84%o0
> 1.6
> 2025-05-30
> CONCENTRATED_WEIGHT REVERSION_COMPONEN
> 查看
> signal-ts_backfill((star_Val_pcf), 252);combined_si.
> 0R5pQ7g
> EUR
> 90
> 2.43
> 1.64
> 8.66%
> 19.04%
> 9.09%o。
> 1.33
> 2025-05-29
> REVERSION_COMPONENT
> 查看
> 十 C
> C3701C+3
> 0C
> CS+
> OC+'mS+o
> f1 IICo
> N1
> 1Cc
> C?
> 0101
> C00
> 4Col
> nC
> C


is_check也是经常需要的筛选条件.

如果有人需要我用的这个, 链接🔗是;  [https://github.com/roshameow/quantnight-frontend](https://github.com/roshameow/quantnight-frontend)

我的后端和mongodb是深度绑定的.

---

## 讨论与评论 (12)

### 评论 #1 (作者: YL96878, 时间: 6 months ago)

感谢，深有益处

---

### 评论 #2 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 6 months ago)

[顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97))

大佬，这个database可以统计目前提交的alpha属于哪个category和具体的dataset吗，真的急需这样的功能。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值
======================================================================================

---

### 评论 #3 (作者: XG43628, 时间: 6 months ago)

感谢大佬分享！最近确实越来越感觉继续已回测alpha的重要性，因为快要限制回测数以及最近有点断粮，想去找一找之前回测的alpha，结果找起来很困难，getalpha总会有缺失遗漏的情况，让ai去修改代码也是不能避免掉这种情况并且还会带着api limit的情况。

==================================================================================

知难上，戒骄狂，常自省，穷途明 ==================================================================================

---

### 评论 #4 (作者: JX14975, 时间: 6 months ago)

大佬这个筛选界面对我非常有用。我之前都只能通过json文件管理回测结果，非常麻烦，而且没有储存过去的回测记录意味着难以应对未来的变化。给大佬赞一个。

---

### 评论 #5 (作者: FZ24842, 时间: 6 months ago)

大佬我没安装成功，quantnight-frontend打不开，我估计是这里有问题
您只需确保后端的  `src-tauri/config.toml`  文件存在且包含基本的数据库连接信息。这个需要怎么弄？

---

### 评论 #6 (作者: AH18340, 时间: 6 months ago)

确实有数据之后本地筛选比较能自己加新的东西，感谢大佬分享

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #7 (作者: 顾问 WL27618 (Rank 97), 时间: 6 months ago)

> 这个database可以统计目前提交的alpha属于哪个category和具体的dataset吗

这个我后续会加, 但是也像pnl, 和计算correlation一样. 不能依赖原始字段. 需要自己在数据库加上相关字段

> 我没安装成功，quantnight-frontend打不开，我估计是这里有问题
> 您只需确保后端的  `src-tauri/config.toml`  文件存在且包含基本的数据库连接信息。

我现在添加了从设置界面修改的功能, 下载1.2.0版本. 我自己试过授权后是可以直接启动了.


> [!NOTE] [图片 OCR 识别内容]
> 重1凹刈十百
> ]测任务管理
> Linux: 与可执行文件同目录的 resourcesl
> 策略构建
> Frontend Configuration (configjs)
> 支持热修复
> 数据面板
> Template Paths
> 测试巡游
> Super Template Path:
> Itemplateslsuperl
> 设置
> Template Path:
> Itemplates
> Priority Template
> Itemplateslpriority
> Path:
> Data Filter Options
> alpha_results
> alpha_results
> Remove
> alpha_submitted
> alpha_submitted
> Remove
> Add Option
> Backend Configuration (config.toml)
> 修改后需要手动重启应用
> MongoDB
> Database
> Settings
> MongoDB Connection
> Local URI:
> mongodb:Illocalhost:27017
> Remote URl:
> mongodb:Illocalhost:27017
> [+13a^
> C


数据库是从这里配置地址

---

### 评论 #8 (作者: 顾问 LW67640 (小虎) (Rank 24), 时间: 6 months ago)

mongodb安装在本地，定期从服务器拉取，如果在服务器上运行，低配的服务器可能性能跟不上。

另外，可以分批查询，第一次全量查询24G内存的电脑直接崩了。让gemini改成了分批，效果就好了，最简单的指定一个日期范围。

------------------------------------------------------------------------------------------

路虽远，行则将至。

-------------------------------------------------------------------------------------------

---

### 评论 #9 (作者: CC21336, 时间: 6 months ago)

※※※※※※※※※※※※※※※CC21336的评论※※※※※※※※※※※※※※

刚成为顾问的时候，也考虑过想用Mysql 或 Mongodb 在本地建一个数据库

进行维护存储。后面还是觉得麻烦，直接用WQ平台进行存储。把alpha的名字

当作大Key，Tags 当作小Key，其它想存储的内容可写在Description中，这样你就

有了一个自己的文件存储系统。理论上可以存储自己想要的所有内容。当然

自己在本地进行Key的维护，方便自己进行查询。

※※※※※※※※※※※※※※※CC21336的评论※※※※※※※※※※※※※※

---

### 评论 #10 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 6 months ago)

文洁大佬的AIAC感悟颇多，因为迟迟没能成功使用AI产出过alpha，我就没有太关注这个比赛，看了大佬的经历，至少已经迈出一大大步了。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #11 (作者: YY31580, 时间: 6 months ago)

好想法！

---

### 评论 #12 (作者: HZ99685, 时间: 5 months ago)

大佬，具体使用有没有相关教程啊？下载安装后第一步需要做什么？点添加任务按钮没有任何反应。。。

---

