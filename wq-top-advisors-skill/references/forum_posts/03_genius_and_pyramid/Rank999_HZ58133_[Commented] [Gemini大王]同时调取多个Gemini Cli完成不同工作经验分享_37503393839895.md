# [Gemini大王]同时调取多个Gemini Cli完成不同工作经验分享

- **链接**: https://support.worldquantbrain.com[Commented] [Gemini大王]同时调取多个Gemini Cli完成不同工作经验分享_37503393839895.md
- **作者**: HZ58133
- **发布时间/热度**: 5个月前, 得票: 7

## 帖子正文

在使用AI改进Alpha时，我每次都需要打开terminal，然后输入提示词开始任务，颇为繁琐。于是想到是否可以有更高效的办法，比如用代码同时唤起多个Gemini Cli大模型然后完成不同的任务。

经过学习发现有多种方法可以实现，比如可以多任务调度”Python 脚本(需要api)如果有需要我之后也可都介绍一下，我们现在主要介绍使用  **PowerShell 并行脚本(免费)。**

### **第一步:安装Gemini Cli**

Terminal中输入

```
npm install -g @google/gemini-cli
```

### **第二部:VS Code里安装Powershell**

点开VS code左侧的小方块(Extensions)，搜索PowerShell并下载，


> [!NOTE] [图片 OCR 识别内容]
> Powershell
> Microsoft
> microsoft.com
> C 17,382,414
> &(171]
> Develop Powershell modules; commands and scripts in Visual Studio Code!
> Set Color Theme
> Uninstall
> Switchto Pre-Release Version
> Auto Update


### **第三步:编写 ps1. 文档调用Gemini Cli执行任务**

```
$OutputEncoding = [System.Text.Encoding]::UTF8[Console]::OutputEncoding = [System.Text.Encoding]::UTF8chcp 65001 | Out-Null  # 强制切换当前终端代码页为 UTF-8$tasks = @(    @{ File = "C:\Users\dujid\Desktop\WORLDQUANT\Learn\Gemini\总结.txt"; Hint = "总结一下这段话" };    @{ File = "C:\Users\dujid\Desktop\WORLDQUANT\Learn\Gemini\math.txt"; Hint = "输出结果" };    @{ File = "C:\Users\dujid\Desktop\WORLDQUANT\Learn\Gemini\翻译.txt"; Hint = "翻译成中文" })Write-Host "--- 正在启动并行任务 ---" -ForegroundColor Yellowforeach ($task in $tasks) {    if (Test-Path $task.File) {        Start-Job -ScriptBlock {            param($f, $h)            # 在子任务中也要确保编码环境            [Console]::OutputEncoding = [System.Text.Encoding]::UTF8            Get-Content -Path $f -Raw | gemini $h        } -ArgumentList $task.File, $task.Hint        Write-Host "已启动任务: $($task.File | Split-Path -Leaf)" -ForegroundColor Green    } else {        Write-Warning "找不到文件: $($task.File)"    }    # 稍微停顿，防止 API 触发频率限制（Rate Limit）    Start-Sleep -Milliseconds 600}Write-Host "`n所有任务已在后台运行，正在回收结果...`n" -ForegroundColor Cyan# 2. 等待并回收结果Write-Host "`n所有任务已在后台运行，正在回收结果...`n" -ForegroundColor Cyan$allJobs = Get-Jobforeach ($job in $allJobs) {    Wait-Job $job | Out-Null       # 打印一个简单的分割线    Write-Host ">> 任务 [ID: $($job.Id)] 的处理结果:" -ForegroundColor Cyan -BackgroundColor DarkBlue       # 接收结果    Receive-Job -Job $job -ErrorAction SilentlyContinue       Write-Host "------------------------------------`n"}# 清理任务缓存Remove-Job *
```

### **使用说明:**

```
@{ File = "C:\xx\xx\xx\这里写你需要Gemini阅读的提示词.txt"; Hint = "这里写执行任务的命令" }
```

**现在先简单演示一下效果**

一共设置了三个不同任务

**
> [!NOTE] [图片 OCR 识别内容]
> 翻泛 tt
> 07/01/202608;53
> Tet SOUrCE File
> 总筅 b
> 07/01/202608;52
> Tet SOUrCE File
> mathut
> 07/01/202608;51
> Text Source File
**

输入文件路径和指令


> [!NOTE] [图片 OCR 识别内容]
> $tasks
> File
> "C: lUsers Idujid DesktopIWORLDQUANT ILearn  Gemini  总结
> txt
> Hint
> "总结一下这段话" };
> File
> "C: IUsers dujid Desktop IWORLDQUANT
> Learn  Gemini Imath.txt"
> Hint
> "输出结果" };
> File
> "C: IUsers {dujid Desktop IWORLDQUANT
> Learn  Gemini | 翻译.txt'
> Hint
> '翻译成中文"


成功运行，返回结果 
> [!NOTE] [图片 OCR 识别内容]
> Name
> PSJobTypeName
> State
> HaslloreData
> Location
> Command
> 10637
> BackgroundJob
> Running
> True
> localhost
> 已启动任务:  总结
> txt
> 10639
> BackgroundJob
> Running
> True
> localhost
> 已启动任务: math.txt
> 10641
> BackgroundJob
> Running
> True
> Iocalhost
> 巳启动任务:  翻译.txt
> 所有任务已在后台运行。正在回收结果.
> 所有任务已在后台运行。正在回收结果.
> 任务
> [I:
> 的处理结果:
> 这段文字主要概括
> 唐纳德.特朗普 (Donald John Trump) 的生平。商业背慕及政治生涯。要点如下:
> 囊+1
> 身份与成就*皋
> 纂双任总统瘛:  他足美国第45任总统。井于2024年再次胜选成为第47任候任总统。他足美囝历史上第二位两度当选但任期不连续的总统。也足当选时最年长的总统。
> 袤商业与媒体背录*:  出身房地产世家。接手家族企业井更名为特朗普集团。涉足摩天大楼。酒店。赌场等领域。曾主办"环球小姐"比赛井主持真人秀《飞黄腾达)
> (The Apprentice)
> 积累了巨额财富和知名度。
> 2。政治生涯*
> 謇2016年大选*
> 以共和党人身份参选井击败希拉里:克林顿。咸为首位无军政背景的总统。推行保护主义。民族主义和民粹主义政策。
> ]2020年大选~
> 败绐乔.拜登。但拒绝承认败选。其言论被指煽动了2021年1月68的国会山骚乱。
> 謇2024年大选謇
> 击败卡玛拉.哈里斯。赢得普选票和选举人票。重返白宫。
> 3。法律纠纷与争议*
> 皋弹劾*:  他是美国历史上首位被众议院两次弹劾
> (2019年。2021年)  的总统。但均被参议院宣告无罪。
> **刑事与民事诉讼*:  他是首位面临刑事指控及被判重罪成立 (34项伪造商业记录罪)  的前总统。此外。他在性虐待。诽谤和财务欺诈等民事诉讼中被判负有责任。需赔偿数亿美元。
> 皋历史评价〈:  学者和历史学家对其总统任期的评价普遍偏低。认为他是
> 位极具争议的政治人物。
> 任务 [I:  39] 的处理结果:
> Will
> Use Python
> to calculate the 5Um Of 1,
> and 3。
> 任务
> [I:
> 411  的处理结果
> 如果您懂得如何生活,生命是美好的。


## **现在进入实战环节:**

为了方便观察，我们使用Gemini Cli对三个不同地区(EUR, USA, IND)不合格Alpha进行改进。

**由于调用Gemini Cli进行回测时需要调用工具，因此我们要对代码做出相应修改。**

```
# 1. 环境编码设置$OutputEncoding = [System.Text.Encoding]::UTF8[Console]::OutputEncoding = [System.Text.Encoding]::UTF8chcp 65001 | Out-Null# 明确你的工作目录路径$workDir = "C:\Users\dujid\Desktop\WORLDQUANT\Learn\Gemini"$tasks = @(    @{ File = "$workDir\ImproveEUR.md"; Hint = "获取ID为`xxx`的Alpha的数据,在其原有表达式的基础上对其进行改进提升。阅读ImproveEUR.md" };    @{ File = "$workDir\ImproveUSA.md"; Hint = "获取ID为`xxx`的Alpha的数据,在其原有表达式的基础上对其进行改进提升。阅读ImproveUSA.md" };    @{ File = "$workDir\ImproveIND.md"; Hint = "获取ID为`xxx`的Alpha的数据,在其原有表达式的基础上对其进行改进提升。阅读ImproveIND.md" })Write-Host "--- 正在启动并行任务 (全授权模式) ---" -ForegroundColor Yellowforeach ($task in $tasks) {    if (Test-Path $task.File) {        Start-Job -ScriptBlock {            param($f, $h, $d)            # A. 必须在子任务内部切换到文件所在目录，否则 Gemini 找不到 .md 文档            cd $d            [Console]::OutputEncoding = [System.Text.Encoding]::UTF8                       # B. 使用 --yolo 标志直接授权所有工具调用（回测、平台连接等）            Get-Content -Path $f -Raw | gemini $h --yolo        } -ArgumentList $task.File, $task.Hint, $workDir        Write-Host "已启动任务: $($task.File | Split-Path -Leaf)" -ForegroundColor Green    } else {        Write-Warning "找不到文件: $($task.File)"    }    Start-Sleep -Milliseconds 800 # 稍微延长停顿，给工具初始化留时间}Write-Host "`n任务已全部提交，正在回收结果 (由于涉及 BRAIN 回测，可能需要较长时间)...`n" -ForegroundColor Cyan# 2. 等待并回收结果$allJobs = Get-Jobforeach ($job in $allJobs) {    Wait-Job $job | Out-Null    Write-Host ">> 任务 [ID: $($job.Id)] 处理结果:" -ForegroundColor Cyan -BackgroundColor DarkBlue       # 使用 -ErrorAction SilentlyContinue 过滤登录等杂音    Receive-Job -Job $job -ErrorAction SilentlyContinue       Write-Host "------------------------------------`n"}# 清理任务Remove-Job *
```

任务成功启动


> [!NOTE] [图片 OCR 识别内容]
> 正在启动井行任务 (全授权模式)
> Nlame
> PSJobTypeName
> State
> HaslloreData
> Location
> Command
> J0b49
> BackgroundJob
> Running
> True
> Iocalhost
> 已启动任务: ImproveEUR.md
> J0b51
> BackgroundJob
> Running
> True
> Iocalhost
> 已启动任务: ImprovelSA.md
> J0b53
> BackgroundJob
> Running
> True
> Iocalhost
> 已启动任务
> ImproveIND.md
> 任务已全部提交。正在回收结果 (由于涉及
> BRAINI
> 回测。可能需要较长时间)


查看Alpha界面，成果回测并取得了结果，以下是EUR地区的示例

改进前: 
> [!NOTE] [图片 OCR 识别内容]
> Iulation Settings
> Istut Type
> Regl
> Uelse
> 7034101
> Dcay
> Olay
> UIUNaON
> NUTIaTaUON
> Pastewrtato
> NaN Hanl
> Unlt Handling
> Max Trate
> EaJi?
> EUR
> TOF2
> TC SOTESSITI
> 7.03
> SUCIOUSO
> VErfy
> Clone Alpha
> Chart
> SJOK
> Jn "1
> Jan 16
> Jan13
> J3n*19
> Jn
> Jen '21
> JaT 
> Jan '2
> Pl
> Risk NEUtrallzed Pnl
> Inestability Constralned Pnl
> IS Testing Status
> Lerrg
> 7PASS
> Sharpso229
> 3C
> CUtofor 1.58
> Fin S
> 1.25
> ECD CUTCff1
> UPTON
> 22.163
> aCT
> CuCffof 1%
> Turnoror22.163
> TEI IIT
> T0i
> Weeht
> JITIOLIEJ Ciep IRTUTENt
> 23ear Sharps cf2
> 3-n
> CUCff
> 1.58
> Pyrsmid theme EURIDIISENTIMENT maches with multiplier of 1.4 Effective Pyramio coun:for Cenius
> FAIL
> Sh-InIrre
> Of1.157 below Cutoffof 1.19.
> Sneroe


成功改进:


> [!NOTE] [图片 OCR 识别内容]
> SIIUIatIOT
> SettIIes
> Tnstuwt Type
> Reglo
> Werse
> Unwae
> 9a
> Oelay
> Truncatlon
> Neutallalon
> Pastewrtat
> NaNHanl
> UltHanOUO
> Max Trade
> CTJI
> SUR
> TOF2J
> FastSPressian
> SU TUS
> 「T
> Clone Alpha
> N Chart
> Pnl
> OJOK
> 0112512715
> ZOJOK
> Pnl
> 1,753.33
> Risk Neutraliized PnL
> 587.95K
> Imestabilt ConstralnedpnL 1,12223
> J37"14
> Jans
> Jan 16
> J"T7
> Ja3
> J3n19
> Jen '20
> J "21
> Ja7 2
> J3723
> Pl
> Risk Neutraized Pnl
> Inyestabilit Constraned Pnl
> IS Testing Status
> Period
> 8PASS
> Sharpe or2.15 is above CUtefor 1.58.
> Fi-ress 2+1.35
> 
> TUTOT 1
> TUTCNEI
> 15.519
> 37
> CutCffof 1%
> TITC
> 15.513
> beloy CUs?f
> 70*
> Weehtis Wel
> JI-TICLIJ CsrI-ruTTt
> Sub-universe Sharps
> 1.147 sboe ~UtSfor 1.12
> 2e2
> Shars cf 279
> 3CE
> CUtOfor 1.58。
> Pyramid theme EURIDIISENTIMENT maches wwith multiplier of 1.4 Effective Pramid coun:for
> Teriwc


三个任务也都在同时进行: 
> [!NOTE] [图片 OCR 识别内容]
> SROIMOUS
> ReSUIaT
> 01/0712026 EST
> US4
> TOP3OOO
> Subindustny
> aOHYIOUs
> RESUlar
> 01/0712026 EST
> US4
> TOP3OOO
> Subindustny
> aORJIOUS
> ResUlar
> 01/0712026 EST
> IND
> TOPSDO
> Mlarket
> aOHYIOUs
> RESUlar
> 01/0712026 EST
> IND
> TOPSJO
> Market
> aOHYITOUs
> RESUlar
> 01/0712026 EST
> IND
> TOPSJO
> Market
> aORJIOUS
> ReSUlar
> 01/0712026 EST
> IND
> TOPSDO
> Mlarket
> aOHYITOUs
> RESUlar
> 01/0712026 EST
> IND
> TOPSJO
> Market
> anORYITOUs
> ReSUlar
> 01/0712026 EST
> IND
> TOPSDO
> Mlarket
> an3nyIOUs
> Resular
> 01/0712026 EST
> IND
> TOPSOO
> Market
> aonyMOUS
> ReSUlaT
> 01/0712026 EST
> IND
> TOPSJO
> Market


---

## 讨论与评论 (3)

### 评论 #1 (作者: JX39934, 时间: 5个月前)

感谢大佬的分享，这招并发任务直接解决了AI回测效率的问题，顺便想问下，gemini cli的并发数量最大是3个吗，还有就是开了3个对电脑硬件性能的占比如何呢，望大佬解答一下

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 评论 #2 (作者: HZ58133, 时间: 5个月前)

您好，Gemini cli并发数量理论上来讲是可以无限多的，开五个十个都可以。单个cli大概占200-500MB的内存，电脑内存16GB+的话完全可以胜任5个cli同时开。

---

### 评论 #3 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 5个月前)

看起来比直接多开更便捷，但是要是遇到socket hung up, keep try或者potential loop detected怎么处理。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

