# 手机远程连接claudecode，24小时随时指挥AI干活！经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 手机远程连接claudecode24小时随时指挥AI干活经验分享_37953156945687.md
- **作者**: ZL81441
- **发布时间/热度**: 5个月前, 得票: 9

## 帖子正文

最近Clawdbot太火了，我已经被Clawdbot刷屏两天了

他实现了WhatsApp, Telegram, Discord,直接和ai对话，并且可以远程指挥你的电脑干活
 
> [!NOTE] [图片 OCR 识别内容]
> 核心能力
> 具体表现
> 支持 WhatsApp` Telegram
> Discord。
> Slack。
> Signal
> 全平台融入
> iMessage:
> Microsoft Teams 等10+ 主流平台
> 收发邮件。管理日历。预定航班。控制智能家居。运行代砑
> 超越闲聊的执行力
> 操作文件系统
> 记住你的偏好。工作习惯和历史对话。 Al 会随着时间推移变得
> 持久记忆与个性化
> 越来越懂你
> 浏览器控制。命令行执行。文件读写
> 网络搜索。技能扩展系
> 强大的系统集成
> 统
> 本地优先与数据隐私
> 运行在你自己的设备上。数据完全在你的掌控之中
 

我也是第一时间部署到了自己的Mac mini上，老实说这个玩意权限确实有点大，想尝试的小伙伴还是整一台新的电脑或者是部署到vps上。我折腾了半天只跑通了千问的模型，使用下来觉得很兴奋，又有点小失望。兴奋是功能和潜力十分强大，交互方式十分的新颖。失望是配置起来简单，后续各种权限的设置等等，比想象的要复杂，感觉笨笨的（也不知道是不是千问的问题）

最让人失望的是他居然不能自动调用claudecode！也就是说我不能用它来帮助我做alpha工作。

于是我转念一想，用AI控制电脑，执行等 **这些功能，Claude Code 不是都有吗？**

区别在于Claude code只能在终端里交互，而 Clawdbot 让你能在聊天软件里用。 Clawdbot启发了我， **搭一座桥，把聊天软件连到 Claude Code。**

这两者原理如下：

```

```

Telegram │ ───▶ │ Bot 程序 │ ───▶ │ Claude Code

(你手机) │ ◀─── │ (你电脑) │ ◀─── │ (AI) │

```

```

1. 你在 Telegram 发消息
2. Bot 程序收到消息，转发给 Claude Code
3. Claude Code 执行任务（搜索、写文件、跑代码...）
4. Bot 程序把结果发回 Telegram

Bot 程序只是个"传话筒"，真正干活的是 Claude Code。

想法有了，于是我开始说干就干。啊不，我也不是程序员，于是我开始找开源社区有没有现成解决方案，在尝试了很多方案后失败，终于跑通了两个方案。

## **一 ：Telegram机器人**

仓库的地址如下 [https://github.com/hanxiao/claudecode-telegram](https://github.com/hanxiao/claudecode-telegram) 
 
> [!NOTE] [图片 OCR 识别内容]
> Error: CUDA out of memory. Tried to allocate 19.36 GiB. GPU 0 has a total capacity of 47.40 GiB of which 11.47 GiB is free. Including non-PyTorch memory, this process has 1.49 GiB memory in use. Process 58488 has 11.00 GiB memory in use. Process 58482 has 12.66 GiB memory in use. Process 58486 has 10.76 GiB memory in use. Of the allocated memory 1.02 GiB is allocated by PyTorch, and 164.03 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://docs.pytorch.org/docs/stable/notes/cuda.html#optimizing-memory-usage-with-pytorch-cuda-alloc-conf)
 

至于部署的方式，仓库readme文件写的比较详细，我这儿就不贴了。
如何创建telegram的机器人：

1. 打开Telegram，搜索
   [@Botfather](https://x.com/@Botfather)
2. 发送 /newbot
3. 按提示输入名称
4. 获得一个 Token （Use this token to access the HTTP API后面这一串英文和数字）

如果不会的话，可以直接把仓库地址和Token丢给Claudecode，让他来帮你安装。
最终成效
 
> [!NOTE] [图片 OCR 识别内容]
> 0.07
> 4G
> 5G
> 2.05
> 4G
> 5G
> 7:42
> KBIs
> VPN
> SIlsoll 100
> 7:42
> KBIs
> VPN
> Sl s511 100
> M
> Myclaude77_bot
> M
> Myclaude77_bot
> 机器人
> 机器人
> 可以了 ,
> 连接通了
> 07:05
> 使用改进alpha 技能
> 优化
> 07:10
> 好的
> 连接通了!有什么需要我帮忙的
> 吗?
> 输出每个变体的表现  07:28
> 07:05
> ##  所有变体表现对比
> 查看你有哪些技能
> 07:07
> 根据我的配置,
> 我有以下可用技能:
> ### Alpha IC。
> Tr7vJ (原始)
> ##规划与管理
> **表达式**:
> planning-with-files
> 复杂任务的文件式
> 规划 ,
> 创建 taskplenmd
> fingingsmg
> 2
> 和 progressmg
> H liz
> ## WorldQuant BRAIN 相关技能
> expression_verifier
> 验证 alpha 表达
> 式的语法
> **性能指标**:
> brain-improve-alpha-performance - 改
> 指标 |值 |
> 进 BRAIN alphas 的5步工作流
>  |
> brain-datafield-exploration-general
> Sharpe
> 2.28
> 评估 BRAIN 数据集的6种方法
> Fitness
> 1.93
> brain-feature-implementation
> 从
> Returns
> 13.81%
> markdown 文件实现 BRAIN features
> Drawdown
> 5.09%
> brain-explain-alphas
> 分析和解释
> Turnover
> 0.1925
> BRAIN alpha 表达式
> 2Y Sharpe
> 1.96
> brain-dataset-exploration-general
> 深
> Robust Sharpe
> **0.51**
> 入探索 BRAIN 数据集
> Sub Sharpe
> 0.67
> brain-calculate-alpha-selfcorrQuick
> 计算 alpha 自相关性
> *相关性**:
> brain-how-to-pass-AlphaTest
> Alpha
> 类型
> 值 |状态 |
> 提交测试的要求和改进建议
> 一-----
> 井'40丫 |7791
> 十 /71 |
> 二菜单
> 输入消息
> 二菜单
> 腧入消息


## **二：Happy coder app**

## （写稿的时候才发现，新手更加推荐！）
官方网站： [https://happy.engineering/](https://happy.engineering/)

电脑终端输入代码
npm i -g happy-coder && happy

 
> [!NOTE] [图片 OCR 识别内容]
> Happy Coder
> Bulka, LLC
> 』
> 应用内购商品
> 4.9太
> 1万+
> 838条评价
> 次下载
> 3岁以上 @
> 安装
> 分享
> 添加到心愿单
> 6
> 在您的设备上可以使用此应用
> Code everything, everywhere,allat once
> Realtime Voice with multiple sessions
> Review changes or
> 应用支持
> ~
> PA?
> 8:123
> ODEITUIICLUebeIUely Uuray: MacerI NoJe.ls Refiesh
> ODEITUIICLUebeIUely Uuray: MacerI NoJe.ls Refiesh
> 臼 {erglstoiciDrvelop;opentunnelisrc
>  Urcp
> 1
> OITrsm
> Migration; Comp eta
> TEWTR ICn
> IL=Col
> ASTCIRPTCF DTET
> Cmson{
> IaT4
> Lontend
> 7 M +
> 7 1373
> C TTTaTT
> CIidr1
> U111(1LO?n SN SU4aICHII
> IIITTT
> LITII
> U^
> CmrInder
> Tronzend ;Frontendsessionts
> AICTTt
> sttrllon
> TTon
> eoncttrTent
> 类似应用
> CTTU'
> R11
> ITCie;T
> Etrof Hindllire
> TmTanmN+o7 7 Lm
> IIDOIt
> startrzomen
>  zonzeno'startFTOIC2NO
> Dinn
> Updated Iosger contiguration
> IhTanSOCTf Snta
> SIC !utils WodeTTaCter
> IIDoIt
> + Tngm
> _e++1LS
> N Ftah  RLLel fttyitl
> TH i f h API
> I
> Would you prefer re to:
>  
> CorrSrlt:Li51L'lu
> TT
> Vsti:
> KeED the CUrrenL Complete Upqrade Tcomierge]
> SETLII
> IorIn|
> TFHIITT
> 'TUe551111
> TypeScrpt compilation: Allerrols resolyed
> Rewert
> original state and do on; NATS upsrade Trst
> 记账城市 -用每笔收支。
> 建造你的城市
> UTC Cet
> Norin orresl;
> Show you the specific NATS changes
> detail
> TmstTnsT
> T !TTnf
> CLI functionalty: Al ccmmands cperational with properhelp text
> lot hardled
> +1153
> T1ntu
> the Currentapprouch
> thalall dependencies Iork togetherard are tested 25 3 corr plele
> FOR UNE
> SPARKFUL
> Orn OISINiti
> Cxisting functicnality wile moderizins
> TTII
> atcwl'CU preter
> CIRTaT
> ICMm
> TUIIII?
> thc lalest,Irost
> NII
> T[TIsrr
> allldeperdencies, takirg
> CTpli'fTn-on'
> fulladyantage
> modlern Nadels features and improed TypeScript supnor!
> SI
> TtT
> 21T
> iTmin?
> C+
> 4.1大
> mntzn
> OTT
>  Listeninn http port]
> Type
> 35530
> Ttoni
> SOTOTC
> LISTs
> 53TOT Frdmmints
> TImSe
> KOIC
> frsl te NATS Uperade?
> aCLionI Iuntlon
> CNOOb
> maste
> 1 Fnr
> L79.12
>  +-
> CLIUIIs '
> LI
> TILO '
> MTCETtan
> Lant m5
> ACCIC
> UUShe NSTC
> Jprade hrst, but Iie aread; ccrpleted the fJll
> UIT个
> RnT
> goTnRI
> 922n.
> Jeperdeney upgrade inludin the NRIS risration frorm Is rals to nals j5
> TTO
> CMUNI
> +」cOTtTUNL
> 3095
> st+Fomo |
> httppor, CaObJ.51
> PRO
> Lel ie shoi you Vha Nas dore
> specifial' [or .he IATs Jpsrade:
> Let UULt
> OMtLuI'
> UdseTTLubtJuIs
> 9239
> Lel IttP'
> optyons-pl
> y」SLTItLuutiur
> SLarLF OTeIIoI 
> HLLPO', OITonss1
> PR
> FI|
> CNITN
> VII stI (o I h(CHG WT
> '' 
> Overload Apps
> MLIII'
> T
> NATS,
> Durl
 
appstore或者play商店搜索happy coder下载

APP扫码终端二维码即可绑定，流程更加简单快捷，UI交互也更全面友好！
 
> [!NOTE] [图片 OCR 识别内容]
> 0.75
> 46
> 56
> 0.00
> 46
> 56
> 8:27
> KB/s
> VPN
> S5
> 99
> 8:25
> KBIs
> VPN
> SIsl
> 99
> 终端
> BRAIN risk数据集研究
> 已连接
> ~/Downloads/Claudebot
> ~|Downloads/Claudebot
> 启动ind auto angent,
> 研究-Frisk数据集
> Claudebot
> Title changed to
> BRAIN risk 数据集研
> 在线
> 研究risk数据集
> 730.0s
> BRAIN risk数据集研究
> ideating: 
> MCP: Brain-mcp Authenticate
> 724.0s
> )
> 是
> 是
> 不再询问此工具
> 否;并告诉 Claude 该如何不同地操作
> MCP: Brain-mcp Get Platfor
> 712.0s
> 是
> 是
> 不再询问此工具
> 否;并告诉 Claude 该如何不同地操作
> MCP: Brain-mcp Get Datasets
> 706
> 0s
> 在线
> 绕过所有权限
> 输入消息
> 岛
> 收件箱
> 终端
> 设置


---

## 讨论与评论 (7)

### 评论 #1 (作者: ZL81441, 时间: 4个月前)

更正一下，今天又研究了一下Clawdbot，发现给Clawdbot安装一个coding-agent 的skills就手机可以调用Codex CLI, Claude Code, OpenCode等编程工具，支持GLM和minimax的codingplan，也不用担心token消耗感兴趣的小伙伴也可以尝试一下。
感觉Clawdbot这类的工具的想象空间比预想的要大不少，不仅是远程挖掘alpha

---

### 评论 #2 (作者: 顾问 RM49262 (Rank 30), 时间: 4个月前)

=====================================评论区=========================================

感谢大佬分享，这两天也被Clawdbot刷屏了

但我其实不明白的是，除了多了个聊天窗口控制的途径之外，这和我直接在Claude code中调用Skills有啥区别吗

===================================================================================

---

### 评论 #3 (作者: YQ84572, 时间: 4个月前)

Clawdbot确实很火，但是属于更多是边界，对于研究性的问题比较难以有进展，只能在远程检查或帮忙查看一些alpha感觉。
=================================感谢分享============================================

---

### 评论 #4 (作者: JX39934, 时间: 4个月前)

感谢大佬的分享，WQ国区论坛是真的牛，每次进来都能看到前沿科技，真的能让我学到很多东西，我这就回去捣鼓一下，看下能不能跑起来或者优化一下

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 评论 #5 (作者: HY20507, 时间: 4个月前)

好牛，又是前沿的技术，在wq最美好的体验莫过于此，喜欢这样探索的社区氛围，向大佬致敬

---

### 评论 #6 (作者: CY76111, 时间: 3个月前)

感谢大佬

---

### 评论 #7 (作者: XY20037, 时间: 3个月前)

太牛了大佬！把 Telegram/Happy coder 和 Claude Code 打通，实现手机远程 24 小时指挥 AI 干活，这思路直接拉满效率！还贴心纠正 Clawdbot 装 coding-agent 就能调用 Codex/Claude Code，甚至支持 GLM/minimax，这玩法的想象空间也太大了。对比直接在终端用 Claude Code，手机远程操控不用守在电脑前，挖 alpha、查数据随时随地都能搞，太贴合顾问的使用场景了。感谢分享这么前沿的玩法，国区论坛这种探索氛围真的绝了，马上去捣鼓部署！

---

