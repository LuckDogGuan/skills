# 在Trae 中使用cnhkmcp中的Skills经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 在Trae 中使用cnhkmcp中的Skills经验分享_37609772940311.md
- **作者**: YL42885
- **发布时间/热度**: 5个月前, 得票: 24

## 帖子正文

今天更新了新版本的MCP（2.1.9）【如果有不知道更新命令的小伙伴，注意了：pip install --upgrade cnhkmcp】，无意间发现了大佬写好的skill，这这这 大佬们怎么只顾着闷头做事一点也不宣传啊，skill是啥我就不再过多赘述了，不了解的小伙伴可以问问AI。 
> [!NOTE] [图片 OCR 识别内容]
> 凸 cnhkmcp
> Pycache
> 凸 untracked
> Pycache
> OAII人
> 9A桌面插件
> APP
> back_叩
> mCp文件论坛版2_如果原版启动不了浏览器就试这个
> 6 skills
> 口 brain-calculate-alpha-selfcorrQuick
> brain-datafield-exploration-general
> brain-dataset-exploration-general
> brain-explain-alphas
> 口 brain-how-to-pass-AlphaTest
> brain-improve
> perfommance
> brain-nextMove-analysis
> expression_Verfer
> BRAINSKII
> Claude_Skill_Creation_Guidemd
> Linit_Py
> 配前运行我_安装必要依赖包;py
> 示例参考文档 BRAIN_Alpha_Test_Requirements_and_Tio
> 示例工怍流 Alpha_explaination_Workflow.md
> 示例工怍流 BRAIN_6_Tips_Datafeld_Exploration_Guide。
> 示例工怍流 BRAIN_Alpha_Improvement_Workflow md
> 示例工怍流 daily_report_workflow md
> 示例工怍流 Dataset_Exploration_Expert_Manualmd
> arXiV_API_Tool_Manualmd
> arXIV_aplpy
> brain-consultantmd
> forum_functions;py
> platform_functions:py
> sample_mcP_confgijson
> user_configjson
> alpha
> pull


由于本人一直在使用Trae，那么今天就给大家介绍一下如何用Trae来使用skill：

1. 环境要求
   Node.js >= 20.6.0   【node.js 下载地址： [https://nodejs.org/】](https://nodejs.org/%E3%80%91)
   npm
2. 全局安装OpenSkills
   ```
   npm install -g openskills
   ```
3. 在你的项目文件夹中新建文件夹【.claude】，并复制mcp中的skill文件夹到新建的文件夹【.claude】中
   
> [!NOTE] [图片 OCR 识别内容]
> claude
> skills
> braln-calculate-alpha-selfcorrQuick
> brain-datafield-exploration-general
> braln-dataset-exploration-general
> bran
> alphas
> braln-how-to-pass-AlphaTest
> brain-improve-alpha-performance
> brain-nextMove-analysis
> expression_venfer
> BRAINSkiII
> Claude_Skiill_Creation_Guidemd
> tr3e
> VenV
> IGE
> DrE
> Settingsjson
> ten
> summalj
> explain 
> Dull

4. 命令行中进入项目目录，执行命令
   ```
   openskills sync
   ```
   它便会显示出来刚才复制的所有skill，选择最后一个，则会将所有skill都导入
   
> [!NOTE] [图片 OCR 识别内容]
> C: IProjectlalpha>openskills
> SynC
> Select Skills
> to
> sync
> to AGENTS.md
> brain-calculate-alpha-selfcorrQuick (project)
> 曷
> brain-datafzeld-ptolafzoiogeqenalal Cojecest)
> brain-explain-alphas
> ProJect)
> (*)
> brain-how-to-pass-AlphaTest (project)
> (*]
> brain-improve-alpha-performance
> Cpro
> eCt)
> (}
> brain-nextMove
> analysis
> Cproject]
> expression_Verifier
> CproJect)
> [*] pull_BRAINSkill
> 〈proJect)
> Pulls
> Valid
> Claude Skills
> from
> ZIP
> URL Cpreferred)
> Git
> repository
 选中后回车，成功导入
   
> [!NOTE] [图片 OCR 识别内容]
> C: |Project lalpha>openskills
> SynC
> Select skills
> to sync
> to AGENTS.md
> brain-calculate-alpha-selfcorrQuick
> Cproject)
> brain-datafield-exploration-general
> Cproject)
> brain-dataset-exploration-general Cproject)
> brain-explain-alphas
> Cproject)
> brain-how-to
> pass-AlphaTest
> Cpro]
> lecti
> brain-improve-a
> ipha-performance
> Cproject』
> brain-nextMove-analysis
> Cproject)
> expression
> Verifier
> Droject]
> Pull_BRAINSkill
> Dno
> SCt
> Added Skills
> Section
> to AGENTS.md (9 skill(s)]
 再次查看项目文件夹，会发现跟目录有一个AGENTS.md文件，这就是我们的skill指导文件
   
> [!NOTE] [图片 OCR 识别内容]
> 文件
> 凸 4C #
> 6 .claude | skills
> brain-calculate-alpha-selfcorrQuick
> brain-datafield-exploration-general
> brain-dataset-exploration-general
> brain-explain-alphas
> brain-how-to-pass-AlphaTest
> brain-improve-alpha-performance
> brain-nextMove-analysis
> expression_Verfer
> pull_BRAINSkII
> Claude_Skill_Creation_Guidemd
> trae
> sVenV
> tes
> aCe
> AGENTSmd
> SINIU.
> 曰 ter

5. 了解Skill
   输入在聊天窗口输入：查看并描述你的技能库中的技能，输出为markdown格式，它便会输出所有skill的简介，可以根据这些信息来初步了解skill
   
> [!NOTE] [图片 OCR 识别内容]
> 查看并描逑你的技能库中的技能
> 输出为
> markdown格式
> SOLO Coder
> 思考过程
> 我需要读取AGENTS.md文件的内容。提取所有技能信息并整理
> 成详细bmarkdown格式介]。
> AGENTSmd
> n Thought
> 技能库介绍
> 技能库概述
> 技能库包含一系列专门用于Alpha因子研究和分析的技能。
> 提供
> 了从数据探索到因子验证。
> 性能优化等全方位的支持。所有技能
> 均己置完成
> 可以通过 openskills 命令直接调用。
> 可用技能列表
> 技骶名称
> 描述
> ]
> brain-calculate-alpha-
> 快速计算Alpha
> 项目
> selfcorrQuick
> 因子自相关性
> brain-datafield-
> 数据字段通用探
> 项目
> exploration-general
> 索分析
> brain-dataset
> 数捃集通用探索
> exploration-general
> 分析
> c
> Alpha囚子原理
> brain-explain-alphas
> 解释
> 购
> brain-how-to-pass
>  Alpha测试通过
> AlphaTest
> 指导
> c
> brain-improve-alpha-
> Alpha囚子性能
> performance
> 优化
> 购
> 下-步行动分析
> 项目
> brain-nextMove-analysis
> 建议
> Alpha表达式语
> 项目

6. 使用案例
   使用brain-datafield-exploration-general技能对USA地区中analyst11的anl11_1e字段进行全面分析。
   
> [!NOTE] [图片 OCR 识别内容]
> 使用brain-datafield-exploration-general技能
> 对USAA区中analyst11的anl11_1e字段进行全
> 面析
> SOLO Coder
> 思考过程
> 我需要使用brain-datafield-exploration-general技能提供的6
> 种方法
> 对USA地Banalyst11的anl11_1e字段进行全面分析
> apha
> r动运 
> 终端
> openskills
> pead brain datafield-exploration
> general
> Skill
> pead:
> brain-datafield-exploration-general
> Thought
> USA地区analyst11的an111_1e字段全面分
> 析
> 根据 brain-datafield-exploration-general 技能提供
> 的6种分析方法。我将为您生成
> 份针对USA地区analyst1 1的
> anl11_1e字段的全面分析方案。
> 分析前提条件
> 执行平台: WorldQuant BRAIN平台
> 配参数:
> Neutralization: None
> Decay: 0
> Test Period: POYOM
> 评估指标:  关注I5 Summaryt的Long CountgoShort
> Count
> 1.基础覆盖率分析
> 分析目的:  了解an111_16字段在U5A地区的覆盖范围
> 即有多
> 少股票包含该数据
> 表达式:
> PlainText
> anl11
> 1e
> 执行说明:
> 直接运行该表达式
> 计算覆盖率: (Long Count
> Short Count)
> Universe
> Size


以上就是Trae中使用cnhkmcp的skill的初步介绍，如有更好的方式，请大家多多指正~~

---

## 讨论与评论 (11)

### 评论 #1 (作者: YZ34957, 时间: 5个月前)

听trae工作人员说skills已经在内测了，不过说实话作为国内最强的IDE还没支持skills有点说不过去，codebuddy早已支持，除开这一点trae还是挺好用的
—————————————————**Happy Mining! 💎**—————————————————

---

### 评论 #2 (作者: HZ99685, 时间: 5个月前)

感谢楼主，小白想了解一下，skill和mcp调用到底有什么区别呢？什么时候用skill什么时候用mcp？是我和LLM交互的时告诉它还是它会自动选择？

---

### 评论 #3 (作者: JX39934, 时间: 5个月前)

大佬这都能注意到，我平时基本没有注意mcp的目录下有什么东西，也没有注意更新的内容，最近刚看过skills的文章，正准备玩一下skills,你的帖子就如及时雨一样出现了，谢谢

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 评论 #4 (作者: LY52969, 时间: 5个月前)

非常感谢，学会了在trae里用skill

---

### 评论 #5 (作者: ZH79186, 时间: 5个月前)

最后一个好像是全部取消

---

### 评论 #6 (作者: SX13432, 时间: 5个月前)

赞楼主，值得好好研究一下skills!~

---

### 评论 #7 (作者: FF56620, 时间: 5个月前)

skills会开创一个新时代，想象一下，就像大家一起为ai写了一本书，ai根据执行过程中的需要随时翻阅，然后follow流程处理alpha，可以做到的事情越来越多了

---

Pursue scalable, repeatable opportunities rooted in probability.

---

### 评论 #8 (作者: YZ29225, 时间: 5个月前)

太棒了

---

### 评论 #9 (作者: CL86067, 时间: 5个月前)

感谢大佬分享，正好最近在用trae，太及时了，为你点赞

---

### 评论 #10 (作者: 顾问 LZ63377 (Rank 33), 时间: 5个月前)

=====================================================================================

确实，写cnhkmcp的这位大佬埋头做了不少功能但很少讲解，大概这就是实干派吧。总之感谢感谢楼主和大佬的分享，这就去Trae里试试效果。

=====================================================================================

---

### 评论 #11 (作者: XW23690, 时间: 5个月前)

感谢分享，大佬们又总结出一些好用的文档，马上加入到我的文件夹里面。之前我是自己整理出了一些实用的md文档，放在同一个文件夹里面给ai使用，我用的是CLI，直接在输入框@对应文件让ai去参考，效果还是不错的，在优化alpha的时候不会出现像多个数据字段加权组合的过拟合情况。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

