# [工具分享] WQ Brain 网页增强工具：网页会话复用+相关性缓存

- **链接**: https://support.worldquantbrain.com[Commented] [工具分享] WQ Brain 网页增强工具网页会话复用相关性缓存_37822652857367.md
- **作者**: GC13416
- **发布时间/热度**: 5个月前, 得票: 62

## 帖子正文

兄弟们，此时此刻，《此处省略300字小作文》，恰如彼时彼刻......

"Session Expired" (会话过期)

登录页面朝你微微一笑，刚才的 Alpha 就像前任一样，回不来了，找不到了。

为了拯救被 WorldQuant Brain "光速踢下线" 折磨的道友们，我把之前的 Session Keeper 再次进化了！

发布 v4.1 自适应增强版 —— 这次它比你还能熬！

项目开源：

Gitee: < [https://gitee.com/boludapao/wq-session-guardian](https://gitee.com/boludapao/wq-session-guardian) >

Github: < [https://github.com/chenguangjun8-jpg/WQ-Session-Keeper](https://github.com/chenguangjun8-jpg/WQ-Session-Keeper) >

核心功能 (说人话版)

一、 会话续命 (Session Keeper v4.1)

1. 后台隐身登录 (自适应版)

旧版是“每隔几秒点一下”，一旦网卡就歇菜。

v4.1 新版 学聪明了：它会像猎豹一样盯着进度条，网速慢就多等会儿，网速快就秒登。

全程在后台隐身操作，你在前台刷剧/写代码完全无感。哪怕你断网睡了一觉，醒来它还在尝试重连，简直是全自动电子看门狗。

2. ⚡ 主动 API 探针

以前是等网页跳转了才发现“挂了”。

现在插件会主动发包探测服务器：“喂，还活着吗？” —— 一旦发现苗头不对（401错误），反手就是一个自动登录，把掉线扼杀在摇篮里。

3. 🛡️ 智商在线 (异常感知)

遇到验证码 (Captcha) 或者 2FA 怎么办？

旧版：像个铁头娃一样一直撞墙重试。

新版：立刻“装死”并报警。绝不跟验证码硬刚，保护你的账号不被封。

二、 记忆面包 (ProdMemo v4.0)

1. 🧠 你的第二大脑

跑出来的 Alpha，Prod Correlation 只有 0.6？还是 0.9？

别猜了，插件自动把 Prod/Pool/Self 相关性数据记在小本本上（本地缓存）。

2. 🎴 详情页“照妖镜”

点开 Alpha 详情页，右下角直接弹出一个炫酷的毛玻璃卡片。

🟥 红色：高度相关（在那抄作业呢？）

🟩 绿色：低相关（又是大肉！）

再也不用把鼠标移上去一个个猜了。

3. 📋 列表页“改头换面”

把那个没啥用的 "Book Size" 列，一键替换成 "Max Prod Corr"。

扫一眼列表，谁是真·独家策略，谁是大众脸，一目了然。

4. 📦 搬家小能手 (导入导出)

换电脑了？清缓存了？数据丢了怎么办？

放心，支持一键导出数据备份 (JSON格式)，随时随地恢复你的“记忆”。

卖家秀：


> [!NOTE] [图片 OCR 识别内容]
> ProdMemo 数据管理 (点击展开)
> 己缓存:22条
> 号出
> 导
> 嵩
> OOKpKjed
> Ia 0.3952
> 0112112:22
> WjkpKAAP
> Ma 07244
> 01211155
> KAXNNOKT
> Ia 07341
> 01211154
> bITS6CNG
> 休息
> '41
> Ooowemo
> SESSIOI
  
> [!NOTE] [图片 OCR 识别内容]
> 最近心跳 (Last Pulse)
> 13:07:47
> 刷新间隔(分钟)
> 设置自动登录 (点击展开)
> 保存账号信息
> 启用定时重登
> 重登间隔 (小时):
> 最近登录:
> 登录成功
> 下穴E]新:
> 2h 44m
> Prodlemo 数据管理 (点击展三



> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> 区 Open alpha details in newtab 
> 2019
> 1.29
> 2.153
> 0.71
> 3.7935
> 2.-917
> 35.09520
> 292
> Page size
> OUt 0f3,851
> 2020
> 3.52
> 2.404
> 3.74
> 14.1335
> 2.2235
> 117.549520
> 268
> 202
> 2021
> 3.09
> 2.554
> 3.31
> 14.3545
> 1.753
> 103.47520
> 266
> 210
> 2022
> 2.18
> 2.454
> 8.543
> 2.33{
> 59.155220
> 284
> 139
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> 2023
> 5.25
> 2.5535
> 6.93
> 21.7545
> 28{
> 53.41530
> 291
> 176
> Search
> See
> See
> See
> Search
> TWN
> analyst3g_divi。
> ReEUIaT
> UNSUBMITTED
> 0112012025 EST
> TINN
> Investability constrained
> Aggregate Data
> Sharpe
> TUTTOVET
> Finess
> Returns
> Drawgown
> Marsin
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TN
> 1.79
> 2.359
> 1.31
> 6.719
> 7.599
> 57.0096oo
> analyst39_divid。。
> ReEular
> UNSUBMITTED
> 0112012025 EST
> analyst39_divid
> ReEular
> UNSUBNITTED
> 0112012025 EST
> TWN
> Correlation
> analyst3g_divid.
> ReEUIaT
> UNSUBNITTED
> 01120/2025 EST
> TN
> Self Correlation
> Maimun
> NnimUM
> Last RUn: Wed, 01/21/2026,
> 12.22 PN
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TN
> 0.8952
> 0.4276
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TN
> Power Pool Correlation
> MaimUT
> Mnimum
> Last RUn: Wed; 01/21/2026, 12.22 PN
> analyst39_divid
> ReEular
> UNSUBMITTED
> 0112012025 EST
> TWIN
> 0.5825
> 0.5825
> 踣
> analyst39_divid
> ReEular
> UNSUBNITTED
> 0112012025 EST
> TWIN
> Prod Correlation
> MaimUT
> Mnimum
> Last RUT: Wed; 01/21/2026
> 12.22 PN
> analyst39_divid。。
> RegUlaT
> UNSUBNITTED
> 0112012025 EST
> TWN
> 0.8952
> -0.1725
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TN
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TN
> IS Testing Status
> analyst39_divid。。
> ReEular
> UNSUBMITTED
> 0112012025 EST
> TWIN
> analyst39_divid
> ReEular
> UNSUBNITTED
> 0112012025 EST
> TWN
> 10PASS
> analyst39_divid。。
> Regular
> UNSUBNITTED
> 0112012025 EST
> TWIN
> 2WARNING
> analyst3g_divid.
> ReEUIaT
> UNSUBNITTED
> 01120/2025 EST
> TIN
> 5PENDING
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TIN
> PRODMEMO
> OOKpNjBd
> 01/21 12:22
> analyst3g_divid.
> ReEUIaT
> UNSUBMITTED
> 01120/2025 EST
> TN
> Performance Comparison
> PPC
> 0.8952
> 0.5825
> 0.8952
> analyst39_divid。。
> ReEular
> UNSUBMITTED
> 0112012025 EST
> TWN
> Check Submission
> Submit AIp
> ReeUlar
> UNSUBNITTED
> 011012075
  
> [!NOTE] [图片 OCR 识别内容]
> CUUNE AUUIa
> 2017
> 3.30
> 3.133
> 3,43
> 13.-83
> 2.0595
> 85,033
> 209
> 259
> 品
> 2018
> 3.2936
> 8.023
> 3.2395
> 43,313
> 213
> 268
> Chart
> Pnl
> 2019
> 3.12%
> 1.11
> 5.79{
> 2.379
> 37.113
> 232
> 248
> 2020
> 1.19
> 3.303
> 0911
> 2.045
> 24,323
> 247
> 241
> 2021
> 2.75
> 3.333
> 3,38
> 18.863
> 3.059
> 113,32323
> 261
> 232
> OOOK
> 2022
> 1.45
> 3.20%
> 1.11
> 7.283
> 5.2535
> 42.373
> 223
> 259
> 2023
> 1.07
> 3.30%
> 0.70
> 5.363
> 2.9795
> 32.433
> 223
> 260
> Z50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> FitTESs
> Returns
> Drawdown
> Marsin
> 1.50
> 3.239
> 1.
> 6.729
> 6.779
> 41.579600
> JUI'14
> Jul'15
> JuI'16
> JuI'17
> Ju1'18
> Jul'19
> JuI'20
> Jul '21
> Jul'22
> JUl'23
> Prl
> Investability Constrained Pnl
> Correlation
> Self Correlation
> Maximum
> NinimUM
> Last RUn: Wed, 01/21/2026,1-01 PN
> 0.0941
> 0.0433
> Power Pool Correlation
> Maximum
> NinimUM
> Last RUn: Wed, 01/21/2026,1-01 PN
> IS Testing Status
> Period
> 0S
> 0.0433
> 0.0433
> Prod Correlation
> Maximum
> WinimuI
> Last RUT; Wed
> 01/21/2026,1.01 PN
> 9PASS
> 3WARNING
> 0.7561
> -0.3525
> 5PENDING
> Performance Comparison
> Last RUn:
> Properties
> Last -aVed
> 01/21/2026,12.15Pl
> Name
> Category
> analyst3g_divide_stage_0_1_2_4
> None
> PRODMEMO
> 419967e
> 01/2171.32
> Tags
> Color
> PC
> PC
> SC
> analyst3g
> divide ^
> PNL_CHECKED *
> None
> 0.7561
> 0.0433
> 0.0941
> Description
> 01100 character minimum
> 10
> WEdr


食用方法

1. 下载：拿走压缩包解压。

2. 安装：Chrome/Edge -> 扩展程序 -> 开启开发者模式 -> “加载已解压的扩展程序”。

3. 配置：点开那个绿色的小盾牌，填上账号密码（放心，密码加密存在你自己电脑里，我偷不到）。

4. 躺平：此时你可以去睡觉/吃饭/打球了，只要电脑不关，这网页能挂到天荒地老。

5.遇到问题可以在评论发出，我会尽量解决

P.S.：觉得好用请 点个免费的赞 👍 (疯狂暗示)，祝各位大佬 IS 大涨，OS 不回撤，Combined 直接拉满！🚀

---

## 讨论与评论 (14)

### 评论 #1 (作者: 顾问 RM49262 (Rank 30), 时间: 5个月前)

=====================================评论区=========================================

感谢大佬分享!每次session expire真的很痛苦

这就下载下来试试看

===================================================================================

---

### 评论 #2 (作者: CM48632, 时间: 5个月前)

=====================================评论区=========================================

感谢大佬分享!每次session expire真的很痛苦

这就下载下来试试看

===================================================================================

---

### 评论 #3 (作者: FF45555, 时间: 5个月前)

感谢大佬，确实有时候网页回测的时候挂着等回测结果，结果过一段时间没注意一切换回来直接提示要登陆，回测结果和微调的标签页全都没了，很奔溃，之前看过一个能维持登录的帖子，但是找不到了，试试这个。

======================================================================================
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
=====================================================================================

---

### 评论 #4 (作者: DZ31817, 时间: 5个月前)

20260124

------------------------------------------------------------------------------------------

感谢分享，在网页上回测、手搓alpha和研究的时候，遇到登录过期的情况真的很苦恼，因为重新登录会跳到新的页面，导致原本打开的页面和alpha丢失，这下可以解决了。

---

### 评论 #5 (作者: ML10013, 时间: 5个月前)

感谢大佬分享!试了一下很好用！！！

---

### 评论 #6 (作者: LL15439, 时间: 5个月前)

你好，初始设定的3.8h自动登录一次，我有看到它准时弹出了一个新标签页然后自动关闭了，我估计这是它的自动重新登陆？但是它登录以后过一会还是session expire了，并没有成功守护。

---

### 评论 #7 (作者: GC13416, 时间: 4个月前)

=====================================评论区=========================================

插件更新，请下载4.3版本压缩包使用，名称： [Q_Brain_Enhancer_v4.3.zip](https://gitee.com/boludapao/wq-session-guardian/blob/master/WQ_Brain_Enhancer_v4.3.zip) 
注意先导出已缓存的PC数据，更新后导入
 Gitee: < [https://gitee.com/boludapao/wq-session-guardian](https://gitee.com/boludapao/wq-session-guardian) >

建议各位关注帖子以获取更新情况

=====================================插件更新======================================

---

### 评论 #8 (作者: HY20507, 时间: 4个月前)

牛的，缓存alpha数据并打标签的功能，好用，感谢大佬

---

### 评论 #9 (作者: HL64570, 时间: 4个月前)

挺好的，感谢分享。提个建议：请让那个显示PC、PPAC、SC的框是可拖动的，因为它有时候会遮挡视线。

---

### 评论 #10 (作者: YH37288, 时间: 4个月前)

大佬，哪个定时勾选框勾选后，下次打开后处于没有勾选状态

---

### 评论 #11 (作者: YL42885, 时间: 4个月前)

感谢大佬，非常好用 特意回来点赞

---

### 评论 #12 (作者: GC13416, 时间: 4个月前)

@ [LL15439](/hc/zh-cn/profiles/30163423929367-LL15439) 插件有更新，官方最开始的版本官方改了接口，所以那个版本失效了

---

### 评论 #13 (作者: GC13416, 时间: 4个月前)

@ [YH37288](/hc/zh-cn/profiles/30843143685271-YH37288) 顺手点一下保存账户配置，我把两个保存放在一起的

---

### 评论 #14 (作者: KH21822, 时间: 3个月前)

------------------------------------------------------------------------------------------

感谢分享，好用，感谢大佬
===================================================================================

---

