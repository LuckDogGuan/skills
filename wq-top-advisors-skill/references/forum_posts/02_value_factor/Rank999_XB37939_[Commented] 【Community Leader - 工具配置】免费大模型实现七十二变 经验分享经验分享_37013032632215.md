# 【Community Leader - 工具配置】免费大模型实现七十二变 经验分享经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【Community Leader - 工具配置】免费大模型实现七十二变 经验分享经验分享_37013032632215.md
- **作者**: XB37939
- **发布时间/热度**: 6 months ago, 得票: 62

## 帖子正文

## 前言

最近mcp出现的72变和缘分一道桥功能很火，也很容易出货，毕竟是道生一，一生二，二生三，三生万物的功能。缘分一道桥不需要大模型的api就可以使用毕竟方便，但是72变需要使用大模型的api，大部分大模型都需要收费，在投入和产出之间不好把握。刚好有一个免费的大模型api平台可以使用，方便入门学习72变的使用，使用熟练后可以考虑购买相应大模型的api进行进一步的调试。

## 免费api平台

这里使用的是心流平台，有多个免费的大模型可以调用。百度搜心流即可。

[https://platform.iflow.cn/docs](https://platform.iflow.cn/docs)


> [!NOTE] [图片 OCR 识别内容]
> 免费调用超多前沿模型。让先进技术触手可及
> TStars-2.0
> Qwen3-Coder-Plus
> 淘宝星辰大模型是由淘天集团和爱橙科技共问研发的通用大语言模型。淘宝星辰大谟型的
> Owen3-Coder-Plus; 这是
> 个总参数量 4808。敬活 358的 MoE 葆型。原生支持 256K
> 设计原则是:  海呈数据。平台易用。聚焦业务;
> 曰壬可控。
> 显新版本淘宝星辰大模型使一
> Oken 的上下文井可通过 YaRN 扩展刭 IM token; 拥有卓越的代码和 Agent 能力。
> 上下文窗口:128k
> 最大输出: 64K
> 上下文窗口: IM
> 最大输出: 64K
> 复制檬型 I0
> 复制横型 I0
> Qwen3-Max
> Qwen3-VL-Plus
> 通义干问3系列Ma*模型。相较preview版本在智能体缤程与工具调用方向进行了专项升
> Owen3-VL 系列
> 这是迄今为止 Qwen 系列中最强大的视觉语言模型。
> 这一代椟型在多
> 级。本次发布的正式版模型达到领域SOTA水平。适配场景更加妄杂的眢崴体需求。
> 个维度实现了全面跃升:  无论是纠文本理解与生成。还是视觉内4的惑知与推理;  无论 .
> 上下文窗口:256K
> 最大输出:32k
> 上下文窗口:256K
> 最大输出:32k
> 复制模型 I0
> 复制樟型 I0
> Qwen3-Max-Preview
> Kimi-K2-Instruct- 0905
> 通义干问3系列Ma*模型Preview版本,相较2.5系列整体通用能力有大幅度捉升,中英文通
> Kimi K2-Instruct- 0905, 由月之暗面研发的开源万亿参敖M0E模型。+活参数达320亿;
> 用文本理解能力。复杂抬令遵循崴力。主观开放任务崴力 多语言-力 工具调用能力 .
> 采用混合专家架构。支持256K超长上下文。具备卓趑的编码智能与工具调用崴力,
> 尤甘
> 上下文窗口:256K
> 最大输出:32k
> 上下文窗口:256K
> 最大输出: 64K
> nU1W I1
> nUltA


在右上角头像处可以生成apikey


> [!NOTE] [图片 OCR 识别内容]
> 重要通知:  为了更安全的使用体验。我们将于2025-10-10起。统一启用API Key有效期机制。届时您需要手动垂置API Key以继
> 续使用。若您在使用iFlow CLI, 建议使用 /auth 切换至"通过iF|ow登录"的方式。享受AP| Key自动续期服务。
> API
> Key管理
> 重置AP1密钥
> 创建新的 API 密钥以访问所有模型
> API Key
> 于2025-12-21失效 |
> 复制


然后在模型库里面选择需要的模板，我这里选择的是DeepSeek-V3.2-Exp点击复制模板id，复制后的模板id为deepseek-v3.2

## 使用过程

然后打开mcp的py文件，我这里的路径为D:\Python\Python313\Lib\site-packages\cnhkmcp\untracked\APP。点击里面的运行打开我.py。启动这个py文件，启动成功后访问网址 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  即可看到七十二变和缘分一道桥


> [!NOTE] [图片 OCR 识别内容]
> Npha_Submitter提交器
> Connectto BRAIN
> 打开回测器
> BRAIN Expression Template Decoder
> Open Simulator_hk
> Al创意工坊
> 论文分析
> Specialized template decoder with grammar checking for expression-like language
> 七十二娈
> 数据字段指南 
> 缘分-道桥
> 模板空间
> 只展示用户自建模板
> 导出用户自建模板
> 导入用户自建模板
> 加载72娈生成的模板
> 载入72娈生成的表达式
> Vector数据处理模板
> 单字段深度处理
> 双重中性化
> 组内均值超额信号_
> Matrix Data
> 组内均值超额信号_
> Vector Data
> 换手率娈动Delta模板
> 换手率Hump模板
> 示例
> 双重中性化:以Analyst15为例
> 组间比较_GLB_topdiv
> 组间比较_glb_topdiv_anl15
> 顾问分析示例
> Expression Editor
> Decode Templates
> Expression Editor
> Clear
> Save Current Template
> Overwrite Existing
> Detected Templates
> Ctime
> series_operator/〉
> 〈time_series_operator /> (sentiment_difference, 〈days/〉)
> Op
> DataField
> Other
> 〈days/〉
> Op
> DataField
> Other
> Grammar Rules
> Block comments for multiple lines
> 18
> 11
> Statement separator (not needed for
> 12
> 13ct I1


打开72变，推荐使用web界面，交互友好


> [!NOTE] [图片 OCR 识别内容]
> Open Slmulator_bK
> Specialized template decoder with grammar checking for expression-like language
> 七十二娈
> 缘分
> ~道桥
> Run Transformer (72娈)
> 选择您想要运行 Transformer 的方式:
> 模板空间 
> 加载72
> Vector数据处理模板
> 单字段深度处理
> 双重
> e娈动Delta模板
> 示例
> 双重中性化:以Analyst15为例
> 命令行界面
> Web 界面
> 传统的交互式命令行界面。
> 用户友好的 Web 表单。
> Expression
> Jecode Template
> 交互式参数输入
> 所有参数在一个表单中
> 适合熟悉命令行的高级用户
> V 实时日志监控
> 结果下载
> Expression Editor
> Detec
> 〈time_series_operator /> (sentiment_difference, 
> 〈days/〉)


输入模板id和apikey（我这里使用的deepseek-v3.2，LLM Base URL为 [https://apis.iflow.cn/v1）](https://apis.iflow.cn/v1%EF%BC%89)

输入后点击Test LLM Connection 测试链接，显示Connection Successful!即链接成功。


> [!NOTE] [图片 OCR 识别内容]
> Configuration
> LLM Model Name
> deepseek-v3.2
> LLM API
> LLM Base URL
> https:llapis .iflow.cnlv1
> Test LLM Connection
> Connection Successful!
> Key


然后输入你的BRAIN账号密码，登录后即可使用72变功能。

输入alpha_id

选择dataset啊区域啊什么的 然后点击RUN Transformer

生成效果：


> [!NOTE] [图片 OCR 识别内容]
> BRAIN Transformer (72娈)
> Back to Home
> Configuration
> Output Log
> LLM Model Name
> 已验证  100/174 个表达式
> deepseek-V3 2
> 已验证  110/174 个表达式
> 已验证  120/174
> 表达式
> 己验证  130/174
> 表达式
> LLM API Key
> 己验证  140/174
> 表达式
> 已验证  150/174 个表达式
> 己验证  160/174  个表达式
> 已验证  170/174
> 表达式
> LLM Base URL
> 验证完成!
> https Ilapis fow Cnil
> 有效表达式:
> 161
> 无效表达式:
> Test LLM Connection
> 有效表达式己保存到:
> a: Ugerg
> TpData  IoCal
> Prograng
> BythonlPython313ILiblgite-
> Dackageg  CnhlmcP
> Untracked
> HPIranformer
> Output
> apha_generated_
> EXDTeS310nS
> SUCCeSS.j300
> Connection SUCCeSsfUI!
> 无效表达式己保存到:
> a: Uger:
> WppData lLocallProgramg PythonlPython313ILiblgite-
> BRAIN Username
> Packageg
> CnhlmcplutrackedlgelIranformer loutput lalpha_
> generated
> EXDTeSS10nS
> eTTOI.j80I;
> 交件包含错误详情
> 查看该文件, 你将获得修改模扳的灵感, 你可以定位到错误的模扳并茌哩修改
> 请注意:  该文件仅用于验证表达式的格式正确性;
> 不保证表达式在实际Y用中的逻辑正确性或可执行性
> BRAIN Password
> 不在内罡函数列表中的operator将无法捡查
> 如有需要
> 请使用豇按需修改validator 源代码添加
> 不同模型效果不同; 默让的kmi模型可能会产生4pha语法错误,请检查生成的摸板文件进行甄别
> 下一步。请下载己完成的模板;放》41首页进行解析和语法捡查
> 强烈建议生成表达式后手动尝试回则
> Logm & Fetch Optons
> PrOCe3S
> Completed SucceggfulIy!
> Login Successful! Options fetched
> Template Summary
> Generation Complete!
> Load from File
> Download Alpha_candidatesjson
> 瓯缸}坛623模板精华总结
> Alpha 模钣文件,可放入苴页载入并精细化调整
> 本文档旨在系统性地整理和总结忧
> 。翰』釉
> ?鞲赚嫘l
> Download Nlpha_generated_expressions_successjson
> 的筛
> 核心思想
> 4lph3表达式列表。可放
> 苴页或machine_lib载入后添加setting迸行回测
> 夷用时请思考如何将下列摸板与有
> Download Alpha_generated_expressions_errorjson


下载成功的json文件：


> [!NOTE] [图片 OCR 识别内容]
> add (ts
> Zscore (ts_backfill(cfundamental_composite/>, 252)
> 252)
> ZSCOFe (ts_backfill(ctechnical_Composite/>;
> 252),
> 252))":
> template_explanation"
> "Extends
> the
> Seed
> alpha by adding ts_backfill
> to handle sparse fundamental
> and
> technical
> data;
> enSU
> seed_alpha_settings
> instrumentType"
> EQUITYI
> "pegion" 
> ASI"
> Universe
> "HINVOLIN"
> delay"
> decay"
> neutralization"
> REVERSION_AND_HOMENTUI"
> Itruncation
> 0.08
> pasteurization"
> ON"
> "unitHandling"
> VERIFY"
> nanHandling
> ON"
> maxTrade"
> "ON"
> Vlanguage"
> "FASTEXPR"
> VVisualization"
> fal5e
> startDate"
> 2013-01-20"
> endDate
> "2023-01-20"
> placeholder
> Candidates":
> <fundamental_Composite/>":
> "type
> "data_fieldn
> candidates"
> vid":
> nfnd72
> pit
> b5_9_1_fundamental_entry_dt"
> description"
> Date
> when the
> fundamental
> pecord for
> this period
> is Created"
> vid":
> nfnd72
> pit
> 9_2_fundamental_entry_dt"
> description"
> Date
> when
> the fundamental
> pecord for
> this period
> is Created"
> vid":
> nfnd72
> pit
> q_fundamental_entry_dt'
> description"
> Date
> when
> the fundamental
> pecord for
> this period
> is Created"
> vid":
> nfnd72
> pit
> Op_Cf_q_fundamental_entry_dt"
> "description":
> "Date
> when the fundamental
> pecord for
> this
> period is Created"


这就是72变生成的模板和字段文件了，可以基于此进行模板构建和回测，然后进行裂变，不断提交合适的alpha

祝大家使用这个功能多多出货，早日GM

---

## 讨论与评论 (22)

### 评论 #1 (作者: ML28213, 时间: 6 months ago)

膜拜大佬，这都能被找到。马上用起来。感谢大佬

---

### 评论 #2 (作者: LW98064, 时间: 6 months ago)

优秀，感谢分享

---

### 评论 #3 (作者: JC25837, 时间: 6 months ago)

这个太棒了！有了免费的api就可以不断尝试七十二变与缘分一道桥的功能了！

---

### 评论 #4 (作者: JY56809, 时间: 6 months ago)

大佬还是 厉害，api已使用。

---

### 评论 #5 (作者: SX13432, 时间: 6 months ago)

很详细，给大佬点赞。心流apikey有效期一周。每周更新一次就可以了~

---

### 评论 #6 (作者: HL81191, 时间: 6 months ago)

太棒了，真正的免费，可以节省我在kimi和deepseek的token费用

---

### 评论 #7 (作者: WF69827, 时间: 6 months ago)

早就听过心流，终于看到完整的教学了。感谢分享

---

### 评论 #8 (作者: XG43628, 时间: 6 months ago)

心流还能这么用！感谢分享！我现在用的是默认的kimi，准备换心流的ai模型试一试，看看效果有什么区别，准备多换几款ai模型都试试，七十二变最新版还区分了vector跟matrix的区分输出，更好用了！

==================================================================================

知难上，戒骄狂，常自省，穷途明 ==================================================================================

---

### 评论 #9 (作者: JL67084, 时间: 6 months ago)

请问心流api可以用多久

---

### 评论 #10 (作者: DW35234, 时间: 6 months ago)

太赞了

---

### 评论 #11 (作者: HJ31437, 时间: 6 months ago)

如果提示openai的异常   例如Connection Failed: module 'openai' has no attribute 'OpenAI'

建议升级或者下载一下openai
1、python -m pip install -U openai
2、pip install -U openai

---

### 评论 #12 (作者: JX28185, 时间: 6 months ago)

感谢分享

---

### 评论 #13 (作者: XB37939, 时间: 6 months ago)

@ [JL67084](/hc/en-us/profiles/28860513004567-JL67084)  心流目前可以一直用~

---

### 评论 #14 (作者: ZZ26913, 时间: 6 months ago)

试用过了，很实用，能正常调用API，尝试不同模型下的内容生成效果，通过对比来选择最适合的大模型。

---

### 评论 #15 (作者: CC21336, 时间: 6 months ago)

当我用这个免费的 DeepSeek-V3.2-Exp创建新ALpha的时候，表现虽还可以，但相比付钱的DeepSeek还是有些差距。当然一分钱一分货，有免费的使用自然不能嫌弃。

---

### 评论 #16 (作者: YQ84572, 时间: 6 months ago)

可以可以的，免费的大模型还有这么多可以选，感谢佬的分享
====================================================================================
祝大佬base多多，vf高高，分享更多小妙招～～
====================================================================================

---

### 评论 #17 (作者: BW14163, 时间: 6 months ago)

感谢分享，一直是充钱搞得deepseek和kimi，今天回看帖子，突然发现免费的也不错，赞

---

### 评论 #18 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 6 months ago)

不愧是大佬，代码能力太强了，开发出了这么多结合AI的强大工具，还有iflow这个免费大模型平台。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #19 (作者: OY62064, 时间: 5 months ago)

MCP 最近的 72 变和缘分一道桥是真的火，感谢大佬分享！干货满满~~
============================================================================
                                          “路漫漫其修远兮，吾将上下而求索”
============================================================================

---

### 评论 #20 (作者: MT31982, 时间: 5 months ago)

为什么我的cmp打开没看到缘分一道桥和72变啊，我一直找不到缘分一道桥在哪里，求大佬分享

---

### 评论 #21 (作者: JC31003, 时间: 5 months ago)

这个真是捡到宝了,每一次用kimi差不多2元,性价比不高,而且感觉还没有deep seek好用

---

### 评论 #22 (作者: ZY27848, 时间: 4 months ago)

感谢大佬分享，冬天送火炭，夏天送电扇，及时雨

---

