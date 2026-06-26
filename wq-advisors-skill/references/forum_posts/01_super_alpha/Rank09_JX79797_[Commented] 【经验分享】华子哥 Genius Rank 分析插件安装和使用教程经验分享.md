# 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享

- **链接**: [Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享.md
- **作者**: 顾问 ML47973 (Rank 100)
- **发布时间/热度**: 9个月前, 得票: 35

## 帖子正文


> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN](../顾问 JL71699 (Rank 64)/[Commented] 【插件】Genius Rank分析代码优化.md) 
             Github插件地址： [https://github.com/zhangkaihua88/WebDataScope](https://github.com/zhangkaihua88/WebDataScope)


> [!NOTE] [图片 OCR 识别内容]
> 安装插件
> .访问插件 GitHub 地址: https
> //github. com /zhangkaihua88 / WebDataScope
> 能访问Gitlub的请跳过这红色部分
> 0)如果访问不了 github.
> COm
> 换一个浏览器试试,
> 有几率解决 ,
> 如果不行 ,
> 请按照以下步骤操作。
> 〈 〉 C 命 ^ 众
> 0
> https://github.comlzhangkaihuagg MebDataScope
> 器
> 无法访问此网站
> 连接已重置。
> 请试试以下办法:
> 检查网络连接
> 检查代理服务器和防火墙
> 运行 Windows 网络诊断
> ERR_CONNECTION_RESET
> 重新加载
> 详情
> 1)同时按住 [Window
> Or
> Start ]
> + R, 输入 cmd 打开命令提示符,
> 然后输入 pin
> 吕
> github.com
> 如果 ping 不通,表现为
> ping
> 不是内部或外部命令,
> 也不是可运行的程序
  
> [!NOTE] [图片 OCR 识别内容]
> 或批处理文件=
> 建议将此错误扔给
> AI
> 解决,多半是环境娈量 问题)
> 得到并复制 gith
> ub 的 ip 地址.
> C:IWINDOWSIsystem3zlcmd.
> X
> Microsoft Windows
> [版本
> 10.0.26100.6584]
> Cc)
> Microsoft
> Corporation。
> 保留所有权利
> 0
> C: |Users
> Dping github
> C0I
> 正在
> Pinq
> qithub
> C0I
> 23
> 205.243.166]  具有
> 32  字节的数据:
> 20.205
> 243.166
> 复:  字节=32
> 时间=75ms
> TTL=I03
> 20.205
> 243
> 166
> 的
> 复:  字节=32  时间=75ms
> TTL=I03
> 黧
> 20.205.243.166  的
> 复:  字节=32  时间 =75ms
> TTL=I03
> 20.205.243.166  的
> 复:  字节=32  时间=75ms
> TTL=I03
> 20.205.243.166  的 Ping 统计信息 :
> 数据包:  已发送
> 二  4,
> 已接收 =4,
> 丢失
> 二
> 0
> (0%  丢失 ),
> 往返行程的估计时间 (以毫秒为单位 ):
> 最短
> 二
> T5mS,
> 最长
> 二
> T5mS,
> 平均
> 二
> T5ms
> 2)  复制 ip 地址。在服务器  搜索栏  输入 C: WWindows |System3z Idrivers letc Ihost
> 5 ,
> 打开方式选择  记事本 ,然后马上关闭记事本。接着在  搜索栏  搜索  记事本 并 右击
> 选择以管理员身份运行 ,随即将 github.com 的 ip 地址粘贴在最后.
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1 `
> :三 `
> 8 工 O  a
> # Copyright (c) 1993-2009 Microsoft
> #
> # This is asample HOSTS file used by Microsoft TCPIIP for Windows。
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept onan individual line. The IP address should
> # be placed in the first column followed by the corresponding host name:
> # The IP address and the host name should be separated by at least one
> # space。
> #
> # Additionally, comments (such as these) may be inserted on individual
> # lines O[
> following the machine name denoted by a '#' symbol。
> #
> # Forexample:
> #
> 102.54.94.97
> rhino.acme.com
> # SOUrCe Serer
> 38.25.63.10
> Xacme.com
> # X client host
> # localhost name resolution is handled within DNS itself
> #
> 127.0.0.1
> localhost
> #
> 门
> localhost
> 20.205.243.166
> 行10,列2
> 818个亨符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-8
> 3)
> 点击记事本左上角的 文件 然后选择  保存  即可。切记记得看记事本上面是
> 而不是 O 才算保存成功。
> Corp:
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1
> :三 `
> 8 工 O g
> # Copyright (c) 1993-2009 Microsoft Corp.
> #
> # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept on an individual line. The IP address should
> # be placed in the first column followed by the corresponding host name。
> # The IP address and the host name should be separated by at least one
> # space:
> #
> # Additionally comments (such as these) may be inserted on individual
> # lines Or following the machine name denoted by a '#' symbol。
> #
> # For example:
> #
> 102.54.94.97
> rhino.acme.com
> SOUrCe Serer
> 38.25.63.10
> X.acme.com
> client host
> # localhost name resolution is handled within DNS itself。
> #
> 127.0.0.1
> localhost
> Iocalhost
> 20.205.243.166
> 行22,列15
> 818个字符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-S
> 4)  在 搜索栏  搜索
> cmd 并 右击选择以管理员身份运行 ,在  命令提示符  面板上键入 ip
> config/flushdns
> 返回
> 己成功刷新DN5解析缓存  便表示成功了.
> C
> 管理员: 命令提示符
> 义
> Uicrosoft Nindows [版不 10.0.26100.6584]
> (C)
> Iicrosoft Corporation。 保留所有权利。
> C: |Iindows |System32>ipconfig / flushdns
> Iindows
> IP 配置
> 己成功刷新 DVS 解析缓存。
> C: {Tindows |System32>
> # X
  
> [!NOTE] [图片 OCR 识别内容]
> 5)
> 访问华子哥的 Bithub 地址 https: //github_
> COm
> zhangkaihua88 /WebDatascope
> 成功.
> 囟 M。『图』 &
> WorldQuant BRAIN
> GitHub
> ZhangkalhuaBBNe
> C
> https /Igithubcom/zhangkaihuagg NebDatascope
> C 囤  &
> 8 &
> 器 ^4  泊
> 器
> Platform
> Solutions
> Resources
> Open Source
> Enterprise
> Search Orjump to.。
> Signin
> Sign up
> Zhangkaihua88 / WebDataScope
> Public
> Notifications
> Fork
> Stal
> Code
> SSUeS
> Pullrequests
> Actions
> Projects
> Security
> Insights
> main
> Branches
> GOto fle
> Code
> About
> No description website
> Ortopics provided。
> Zhangkaihuagg fix
> 0183285
> 2Weeks a90
> 118 Commits
> Readme
> Delete img/screenshotpng
> last year
> Apache 2.0license
> Activity
> SIC
> Weeks ago
> 69 stars
>  gitignore
> V0.4.3
> last year
> watching
> LICENSE
> VO.1.0
> last year
> 14 forks
> Report repository
> READMEmd
> 2 months ago
> manifestjson
> Weeks ago
> Releases
> responsejson
> Weeks ago
> WebDataScope 0.9.3 Release
> Lalest
> onIunT4
> 16 releases
> README
> Apache- 2 0 license
> Packages
> 以上为不能访问Gitlub解决方法
> 2
> 点击绿色
> Code 弹出
> Download
> ZIP
> 下载插件压缩包. Zip文件,
> 或者使用 &
> i
> 克隆 git
> clone https: //github.com/zhangkaihua88 / WebDataScope . git
> 将压缩包保
> 存在某目录下,比如我保存在
> 0:
> worldquant_plugin 目录下
> 确认下载
> About
> 链接:
> hub.comlzhangkaihuaggMebDataScopelziplrefs/heads/main
> No description, website; or topics provided。
> 文件名:
> WebDatascope-mainzip
> 394KB
> 0
> Readme
> 保存到:
> 0: {worldquant_plugin
> Apache- 2.0 license
> A
> Activity
> 打开
> 保存
> 取消
> 69 stars
> watching
> V0.1.0
> Open with GitHub Desktop
> 9
> 14 forks
> Download ZIP
> Report repository
> UP
> 3
> 使用解压软件将压缩包解压到(默认)当前目录下.
> Pricing
> Tags
> img
  
> [!NOTE] [图片 OCR 识别内容]
> Worldquant_plugin
> 此电脑
> 新加眷 (D:)
> worldquant_plugin
> 在 worldquant_plugin 中搜索
> 新逮
> 排序
> 三  苎看
> 全部解压宿
> 详洇信息
> 名祢
> 修改曰期
> 大小
> 主文仵夹
> WebDataScope-main
> 2025/9/1218:13
> 压宿(pped)文件。
> 394 KB
> 图库
> 捉敢压缩(Zipped]文件夹
> 选择
> 个目标并提取文件
> 文裆
> 文件将被捉致到这个文件夹(F:
> 囱片
> Dilworldquant_plugin WebDataScope main
> 浏览(R)
> 音乐
> 完戎时显示捉敢的文件(H)
> 视频
> 此电脑
> 本地硭岛 (C:)
> 新加卷(0:)
> 捉取(
> 职消
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 个项目
> 逆中
> 个目
> 393 KB
> 在浏览器中打开扩展管理页面,
> 网页键入 chrome:
> /extensions
> (如
> chrome: //extensions
> 八.
> WorldQuant BRAIN
> 扩展程序
> Cent BroWseT
> chrome /extensions
> 器 |#
> 省
> 器
> quant
> 节点
> MP3袼式
> 显化群每曰总若
> 常用网
> 扩展程序
> 搜索扩展程序
> 开发者摸式
> 我。}展穆序
> 键盘快捷键
> 在 CentBrowser 应田酋店中查找扩展程序和主题背景
> 在 Cent Browser 应jd店中
> 发现更多扩展程序和主题
> 5
> 开启
> 开发者模式》
> 点击 <加载己解压的扩展程序》
> 选择插件文件
> 夹。成功会显示  扩展加载完毕
> edge:
  
> [!NOTE] [图片 OCR 识别内容]
> 选择扩展程序目录
> worldquant_Pl
> WebDatascope main
> WebDatascope-main
> 器
> #
> 阎
> c识
> 新逮文件夹
> 名称
> 佟改曰期
> 开发者摸式
> 此电脑
> WebDataScope-main
> 2025/9/1218.27
> 文件夹
> 本地磁盘 (C:)
> 新加巷 (0;)
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 围l店中查找扩展程序和主题背景
> 文件夹:
> WebDatascope-main
> 迸文4夫
> 驭消
> 2
> 使用插件功能
> 打开 Genius 页面
> 安装完成后 ,打开 WorldQuantBrain 网页 Genius 页面 https : /Iplatform.worl
> dquantbrain.com/genius /
> (安装完成后第一次打开需要刷新页面等待若干(少许)时
> 间才能加载出插件)
> @
> 匕
> https:/Iplatform worldquantbrain com/genius/
> C 囤  众
> 8Q
> 器 ^4  省
> 器 ^8 quant
> U  节点
> MP3袼式
> 昱化群l日总结
> 常用网址
> WORLDOUANT
> BRANI
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> 恩 Competitions (5)
> Community
> Status
> Leaderboard
> FAQ
> Gsnlus
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析 
> 显示排名列表
> Genius level: Gold
> Best level: Gold
> Current quarter end: September 3oth; 2025
> SOLD
> 页面加载后,你会看到  配置插件
> 运算符分析
> 显示运算符分析  和「排名分析」
> 和「显示排名分析」以及「显示排名列表」六个按钮
> 依次点击  配置插件
> 运算符分析
> 显示运算符分析
> 配置插件  点击的作用是啥我不是很清楚,
> 这个得问华子哥才知道。点击  运算符
> 分析  按钮后插件会开始抓取你本季度交付的 alpha 全部操作符数量和使用数据 (按
> 钮上会显示抓取进度) ,抓取完成后,
> 点击显示运算符分析 ,会在页面最下方会生
> 成关于操作符的分析表格。右上角显示过去和美区分析 (何时分析)时间.会展示你
  
> [!NOTE] [图片 OCR 识别内容]
> 本赛季所有的操作符和数量以及使用情况.
> 命
> https: / /platform worldquantbrain comlgenius/
> C 困 &
> 8 ^Q  器 ^4
> 器 ^8 quant
> U  节 
> MP3格式
> 量化群每曰总结
> `用网址
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统
> 为substrac
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符末被使用。
> '有两种含义分别是substract和revers, 此处统一
> 为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x; Y, filter
> false), X -y
> 52
> COMBOREGULARSELECTION
> base
> Arithmetic
> multiply(xyy
> filter-false); *
> 76
> COMBO,REGULAR SELECTION
> base
> 依次点击「排名分析」和「显示排名分析」以及「显示排名列表」
> 点击「排名分析」需要等待0.5 ~ 1min 左右 ,
> 需要计算排名情况, 计算完成
> 后点击「显示排名分析」 ,就可以看见比较多的信息,
> 包括但不限于顾问的总人
> 数,以及目前 genius 不同级别达标分别有多少人和自己目前的等级 ,
> 以及自己的
> 最终定级大概会在什么等级 ,
> 以及自己的六维数据。
> q
> 匕
> https:/Iplatform worldquantbraincom /genius/
> C 囤 。 令
> 凸 /Q 器 』4  省 :
> 器 ^8 quant
> 节忘
> MP3袼式
> 导化拜#曰总结
> 常用网址
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207:22:18北京时间: 2025/9/1219:22;18
> 我的排名信息
> 美东时间:2025/9/1207:22:18 北京时间:2025/9/1219:22.18
> 总人敛{9104
> 可能的基璀人数:2926 人
> (交够40个)
> 各个Level 满足的人数 /最终的人:
> For Expert;(512/ 585
> For Master: 4131234
> ForGranamaster
> 该用户目前满足的级别
> grandmaster
> 绢辑六维指标
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:87
> 585
> 总排名:91
> 234
> 总排名:34
> Operator Count: 307 名
> Operator Count: 200 名
> Operator Count: 39 名
> Operator
> 141名
> Operator
> 44名
> Operator AVg: 7名
> Field Count; 263 名
> Field Count; 152 名
> Field Count; 36 名
> Field
> 112名
> Field
> 30名
> Field
> 7名
> Community Activity: 252名
> Community Actiity: 142 名
> Community Activity: 27 名
> Completed Referrals: 1 名
> Completed Referrals:
> Completed Referrals: 1 名
> Max Simulation Streak: 903 名
> Max Simulation Streak: 338名
> Max Simulation Streak: 45 名
> Total Rank: 1979名
> Total Rank: 907 名
> TotalRank: 162 名
> 同时还有贴心的可以 编辑六维数据  按钮,这个功能非常还好,
> 可以让你知道自
> 己目前所处的级别到达是差在哪里,怎么去弥补自己的差分点.非常 nice!
> 点击「显示排名列表」可以多维度查看和分析所有顾问的某些数据,
> 想比对
> 想查看哪位大佬的数据都可以查看,同时支持多维度过滤筛选.
> AVB;
> AVg:
> Avg:
> Ave:
> Avg:
  
> [!NOTE] [图片 OCR 识别内容]
> https:/ /platform worldquantbrain com/genius /leaderboard
> C 囤
> 8Q
> 器 ^^4
> ^
> 器 ^9 quant
> 节点
> 1P3恪式
> 呈化群每曰总结
> 穷用网址
> Genius Rank List
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> 排名信息
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> Minimum 排名:
> Maximum 排名
> entries per page
> Search:
> 下荭原始J5JN
> 显示隐蒉列
> 排名
> 用FID
> 达成等级
> 最终等级
> 国家1区
> K279256
> grandmaster
> grandmaster
> CN
> J71699
> grandmaster
> grandmaster
> FL39657
> grandmaster
> grandmaster
> CN
> 064461
> grandmaster
> grandmaster
> VN
> YN82626
> grandmaster
> grandmaster
> TW
> PP87148
> grandmaster
> grandmaster
> IN
> AT56452
> grandmaster
> grandmaster
> RP76828
> grandmaster
> grandmaster
> CN
> F069320
> grandmaster
> grandmaster
> CN
> 2H78994
> grandmaster
> grandmaster
> T
> Showing
> TO 10of 5,116 entries
> 512
> 查看他人排名数据
> 华子哥的插件还有非常贴心的功能,就是可以查看别人的排名,
> 比如:  华子
> 哥
> K279256
> 课代表 XX
> 游戏王
> ZS(CL ) [ZSC]59763  和常州MG
> 顾问 MG88592 (Rank 38)
> 大佬等等.
> WORLDOUANT
> B人I
> Simulate
> 6Alphas
> Learn
> Data
> Labs
> Genius
> @ Competitions (5)
> Community
> 号
> Refer
> friend
> StatUs
> Leaderboard
> FAQ
> Genius
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207;22:18 北京时间:2025/9/1219:22:18
> 我的排名信息
> 美东时问:  2025/9/1207.22:18北京时问:2025/9/1219:22:18
> 总人数:9104人
> 可能的基准人数:2926  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 1512
> 585
> FOr Master: 413
> 234
> For Grandmaster: 47/59
> 点击
> Leaderboard
> 将鼠标放置在某大佬的 ID 上,
> 便可查看六维排名和
> Geniu
> s等级。
  
> [!NOTE] [图片 OCR 识别内容]
> https:/platform worldquantbrain com /genius/leaderboard
> 出  ^
> {|仑
> JIIVIIOIIOC
> IIUIIOICC
> 386
> 顾问 ML47973 (Rank 100) (Mej
> Gold
> Gold
> 266
> 2.39
> 1.79
> 0.00
> 3.41
> [792
> 167
> 2.70
> RP76828 排名信息
> AK40g
> 总人数:9067人
> 6.17
> 可能的基准人数:2921人 (交够40个)
> HI3900
> 5,38
> 各个Level 满足的人数
> 最终的人数:
> RP768;
> 2.81
> For Expert: 1508
> 584
> YH250;
> For Master: 410
> 234
> 105
> 5.83
> ForGrandmaster: 45
> 58
> P11976
> 5,82
> 该用户目前满足的级别: Srandmaster
> LV571
> 编辑六维指标
> CM456
> 6.91
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> TV5921
> 8.26
> 总排名:4
> 584
> 总排名:4/234
> 总排名:7/58
> LV598
> 4.70
> Operator Count: 35 名
> Operator Count: 34 名
> Operator Count: 15 名
> DVGAAI
> Operator AVg: 64名
> Operator AVg: 17名
> Operator AVg: 4 名
> 3,73
> Field Count: 283名
> Field Count: 160 名
> Field Count: 35 名
> 儿7169
> Field AVg: 33名
> Field AVg: 7 名
> Field
> 名
> 100
> 3.58
> Community Activity: 96 名
> Community Activity: 71 名
> Community Activity: 20名
> EYg42
> Completed Referrals:
> Completed Referrals:
> 名
> Completed Referrals:
> 名
> 6.15
> Max Simulation Streak:
> Max Simulation Streak:
> Max Simulation Streak: 33
> 501 名
> 222名
> ID51
> 5,91
> Total Rank; 1013 名
> Total Rank: 512名
> Total Rank; 109 名
> 56764
> 116
> 7.35
> AN154671
> Expert
> Expert
> 366
> 0.48
> 0.12
> 0.21
> 6.47
> https;lIplatform worldquantbrain comprofle/public/RP76823
> Master
> Master
> 365
> 0,79
> 0.89
> 0,91
> 8,61
> 致谢
> 再次感谢华子哥和贡献者们的无私分享 !这个工具极大方便了排名分析,同
> 时在前端的颜色。样式和大小展示方面也贴合美观设,
> 无论是自我提升还是学习
> 他人策略都非常有用。建议大家试用并反馈 ,
> 共同完善插件 !
> AVE:


---

## 讨论与评论 (37)

### 评论 #1 (作者: LK12887, 时间: 9个月前)

运算符分析没反应是啥情况

---

### 评论 #2 (作者: YH47265, 时间: 9个月前)

感谢分享。

有两个问题，麻烦问下哈：

一是默认的参与排名的提交数量设置为40，这个依据是什么呀？改这个感觉排名变化很大。

二是关于排名规则的，比如有4000人达标参与排名，按照2%的GM人数，有80个名额，但很可能没有这么多达标的GM，比如只有60人达标。剩下20人去参加M的竞争了。但是M本身按8%算是320个名额，空出的20个GM名额会匀给M吗？变成340？

---

### 评论 #3 (作者: XC34297, 时间: 9个月前)

good

---

### 评论 #4 (作者: BW14163, 时间: 9个月前)

感谢华子哥的插件，也感谢大佬的分享，终于学会学这个插件了，使用以后感觉非常好用，期待有更多的大佬分享更多的插件。

---

### 评论 #5 (作者: 顾问 YH25030 (Rank 31), 时间: 9个月前)

谢谢您的分享。看您的帖子，才发现华子哥的插件又更新了。其中排名分析分两步，第一步是抓取数据基本分析，第二步是深度抓取。我理解第一步是六维排名。对于第二步，我没有弄明白具体是什么含义，感觉是剔除一些不活跃的顾问。

---

### 评论 #6 (作者: 顾问 RM49262 (Rank 30), 时间: 9个月前)

想请问一下，插件中以Expert/Master/Grandmaster为universe的最下面那个total rank是什么意思呢？是指1.signal 2.pyramid 3.performance三选一  这三个条件均满足某个universe标准的人中我六维的综合排名吗？还是其他什么意思呢。谢谢！
-----------------------------------------------------------------------------------------------

---

### 评论 #7 (作者: 顾问 JX79797 (Rank 9), 时间: 9个月前)

@ [YH47265](/hc/zh-cn/profiles/31706852029335-YH47265)     不可能发生这种情况的，很多人习惯性赛季末发力。 假如这不够就是m增多  m+gm 10%

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**

---

### 评论 #8 (作者: HS55260, 时间: 9个月前)

插件已使用上，感谢分享，感谢华子哥。麻烦问一下例如Exper的总排名，包含M和GM的大佬吗？

---

### 评论 #9 (作者: WH74165, 时间: 9个月前)

太好用了

---

### 评论 #10 (作者: HL42518, 时间: 9个月前)

感謝大佬无私的分享~~!很实用

---------------------------------------------------------------------------------------------------

---

### 评论 #11 (作者: JW39100, 时间: 9个月前)

感谢大佬分享

---

### 评论 #12 (作者: QZ62699, 时间: 9个月前)

**#========= WORLDQUAN =====kuanggong**

**这个插件对我们帮助很大，确实看到自己缺的东西，然后进去努力就行，expect希望上**

**#=================挣扎 奋进=======================#**

---

### 评论 #13 (作者: SZ24058, 时间: 9个月前)

============================================================================

非常详细的教程了！插件对于冲等级很有指导性，可以看看排名比自己高的高在具体哪些地方，从而优化自己的提交策略。

@ [LK12887](/hc/en-us/profiles/32199366315159-LK12887) ，运算符分析显示显示在genius最下面，可能需要拉到底才能看见QAQ

============================================================================

---

### 评论 #14 (作者: CW63908, 时间: 9个月前)

插件已经用上了，个功能都非常不错，感谢分享。

---

### 评论 #15 (作者: HZ45023, 时间: 9个月前)

很实用，感谢分享

---

### 评论 #16 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[LK12887](/hc/en-us/profiles/32199366315159-LK12887)  请截图，直接问，我也不知道是啥原因

---------------------------------------------------------------------------------------------------

---

### 评论 #17 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[YH47265](/hc/en-us/profiles/31706852029335-YH47265)

> 一是默认的参与排名的提交数量设置为40，这个依据是什么呀？改这个感觉排名变化很大。

这个40是初始为了保险由课代表设置的，随后就沿用了。现在你可以参考 HQ17963大佬的 [25Q3顾问提交情况播报（每日更新）](../顾问 JR23144 (Rank 6)/[Commented] 25Q3顾问提交情况播报每日更新.md) 文章获取Q3满足的人数，从而调整提交个数

> 二是关于排名规则的，比如有4000人达标参与排名，按照2%的GM人数，有80个名额，但很可能没有这么多达标的GM，比如只有60人达标。剩下20人去参加M的竞争了。但是M本身按8%算是320个名额，空出的20个GM名额会匀给M吗？变成340？

剩下的20人和满足M的人一起竞争M的8%的名额，不存在M名额的变动，以此类推。

因此，不关注六维极有可能满足GM或M的标准，但是最终定级为Gold

---

### 评论 #18 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[顾问 YH25030 (Rank 31)](/hc/en-us/profiles/28941108652823-顾问 YH25030 (Rank 31))

> 其中排名分析分两步，第一步是抓取数据基本分析，第二步是深度抓取。我理解第一步是六维排名。对于第二步，我没有弄明白具体是什么含义，感觉是剔除一些不活跃的顾问。

第一步抓取的Genius的排行榜，第二步深度抓取的是Consultant排行榜，把二者合并起来，方便查看不同人的WF，VF等信息

---

### 评论 #19 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[顾问 RM49262 (Rank 30)](/hc/en-us/profiles/32668684211991-顾问 RM49262 (Rank 30))

> 想请问一下，插件中以Expert/Master/Grandmaster为universe的最下面那个total rank是什么意思呢？是指1.signal 2.pyramid 3.performance三选一  这三个条件均满足某个universe标准的人中我六维的综合排名吗？还是其他什么意思呢。谢谢！

total rank是你所有六维的rank的数值加和，用于在Universe里排名

可以通过插件设置页面选择考不考虑performance

---

### 评论 #20 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[HS55260](/hc/en-us/profiles/29795741334551-HS55260)

> 麻烦问一下例如Exper的总排名，包含M和GM的大佬吗？

Exper的总排名为满足Exper条件所有人的排名，因此包含M和GM。但有可能会出现部分M或GM在Exper的排名可能比你低的情况。

---

### 评论 #21 (作者: JX14975, 时间: 9个月前)

可以强调一下：一定要从code-downloadzip下载。我一般习惯性地去看右边栏的last updated，一直以为上次更新还在6月

---------------------------------------------------------------------------------------------------

---

### 评论 #22 (作者: 顾问 QP72475 (Rank 84), 时间: 9个月前)

这个插件确实帮助不少。

---

### 评论 #23 (作者: AH18340, 时间: 9个月前)

感谢华子哥的分享，很有帮助。

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

---

### 评论 #24 (作者: AM12075, 时间: 9个月前)

-------------------------------------------------------------------------------------------------------------------------------

为什么排名列表和下面具体的不按照combine排名的名次会有差异呢？具体应该按照哪个为准呢？

-------------------------------------------------------------------------------------------------------------------------------

---

### 评论 #25 (作者: LR93609, 时间: 9个月前)

感谢分享，无敌华子哥，无敌GM，确实帮助不少

1. 可以时刻关注自身排名，直到自己在竞争中的位置；

2. 可以找到个人operators使用情况，查缺补漏；

3. 可以编制指标，找到影响最大的指标项，重点突破；

4. 可以查看竞争对手的指标，找到自身之不足。

总之，晋级利器、GM伴侣.......

--------------------------------------------------------------------------------------------------

凡事发生，皆利于我；愿我所愿，尽是美好

--------------------------------------------------------------------------------------------------

---

### 评论 #26 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

> 为什么排名列表和下面具体的不按照combine排名的名次会有差异呢？

没看懂

---

### 评论 #27 (作者: AM12075, 时间: 8个月前)


> [!NOTE] [图片 OCR 识别内容]
> 排名信息
> 美东时间;2025/9/2817.1506 北京时间:2025/9/2905.15.06
> Minimum 排名:
> Maximum 排名
> entries per page
> Search:
> 下载原始JSON
> 晁示:隐荻列
> 排名
> 用户0
> 达成等级
> 最终等级
> 国家地区
> 101
> PT55616
> Iaster
> Iaster
> 102
> XX42289
> Iaster
> master
> CN
> 103
> 顾问 YH25030 (Rank 31)
> grandmaster
> Iaster
> CN
> 104
> FMS9649
> Iaster
> Iaster
> KE
> 105
> HTI G465
> grandmaster
> master
> 105
> 4N95618
> master
> master
> "
> 107
> CC85858
> master
> master
> 108
> SK14400
> master
> master
> IN
> 109
> NH16784
> master
> master
> VN
> 110
> PII58059
> Iaster
> Iaster
> CN
> Showing 101 to 110of 5,389 entries
> 53
 -------------------------------------------------------------------------------------------------------------------------

就是这个表和下面这个排序不一样

------------------------------------------------------------------------------------------------------------------------- 
> [!NOTE] [图片 OCR 识别内容]
> 不按 combine 过滤
> 编辄六维指标
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe


---

### 评论 #28 (作者: 顾问 KZ79256 (Rank 21), 时间: 8个月前)

[AM12075](/hc/en-us/profiles/30421958512663-AM12075)

因为计算逻辑不同, 下面的是以每个满足等级需求的为Universe, 进行排序的, 低等级的Universe里包含高等级的人一起排序

上面的是先计算能定级到GM的人, 之后把这部分排除, 再找能定级到M的人, 以此类推

---

### 评论 #29 (作者: CS14313, 时间: 8个月前)

终于用上了插件，大佬讲的很详细，小白一步一步照着来居然就流畅的运行起来。虽然运行起来发现想升级还有很大的差距，但是至少有工具了，感谢大佬。

---

### 评论 #30 (作者: JX14975, 时间: 8个月前)

注意，旧版本的华子哥插件在进行第4季度的运算符分析时会出错，从github下载10月的新版本以解决此问题：

--------------------------------------------------------------------------------------------------

[https://github.com/zhangkaihua88/WebDataScope](https://github.com/zhangkaihua88/WebDataScope)

---

### 评论 #31 (作者: XW23690, 时间: 8个月前)

感谢分享！对于我这个新手很有用，可以看一下自己哪些运算符没用过以及和别人的差距，对于冲击genius和提高vf很有帮助

---

### 评论 #32 (作者: DL32665, 时间: 8个月前)

感谢华子哥的插件，也感谢大佬的分享，终于学会学这个插件了，使用以后感觉非常好用，期待有更多的大佬分享更多的插件。

---

### 评论 #33 (作者: 顾问 LZ63377 (Rank 33), 时间: 7个月前)

这个插件可以检查sc吗？怎样用呢？没找到

---

### 评论 #34 (作者: SH51727, 时间: 6个月前)

感谢感谢，非常详细的教程，太赞了

---

### 评论 #35 (作者: ZW14723, 时间: 4个月前)

太强了这个插件

---

### 评论 #36 (作者: WL27319, 时间: 4个月前)

这个插件对于新手朋友来说太友好了！！

---

### 评论 #37 (作者: JX14975, 时间: 4个月前)

吹哨：
插件已更新V0.10.9
更新了直到24年1月的os数据

为datafield也添加了is/os数据，如需使用要在插件设置处关闭数据分析功能，以避免与dataset的重叠
网盘里有上述原始数据

转载自华子哥的发言

---

