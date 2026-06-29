# Gemini cli如何使用cnhkmcp中的Skills经验分享

- **链接**: [Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享.md
- **作者**: PP26750
- **发布时间/热度**: 5个月前, 得票: 74

## 帖子正文

最近cnhkmcp更新了个好东西Skills，有了它我们就可以将自己摸索出来的或者大佬分享的 **"方法论"全部告诉ai，再配合Gemini 3 pro这个最强大脑真的是当之无愧的好东西**

**不过现在Gemini cli默认无法使用skills，需要进行一些配置**

**关于cnhkmcp的更新这里就不再讲解了，更新完成后会多一个skills文件夹，你需要在你的项目文件夹下新建.gemini文件夹然后将cnhkmcp中的skills文件夹复制到.gemini文件夹中。**

**第一步需要在终端运行更新，让你的Gemini cli到最新的预览版**

```
npm install -g @google/gemini-cli@preview
```

更新完成后再输入

```
gemini --version
```


> [!NOTE] [图片 OCR 识别内容]
> PS 0: |量化 IAIKnowledgeBase> gemini
> C-Version
> 0.24.0-preview . 2


如图所示如果显示0.24.0-preview.2就表示成功了，我们再用gemini进入

在对话框中输入/settings进入设置模式


> [!NOTE] [图片 OCR 识别内容]
> Settings
> Bearch
> to
> filter
> Preview Features Ce.9.
> models)
> truex
> Enable preview features
> preview models)
> Vim Mode
> false
> Enable
> Vim keybindings
> Disable Auto Update
> false
> Disable
> automatic updates
> Apply
> To
> User
> Settings
> Workspace Settings
> System Settings
> (Use
> Enter to select,
> Tab to change focus
> Esc
> to close)
> Ce.9.


第一个 Preview Features (e.g., models)推荐打开，也就是右边显示为true*

然后再在上方的搜索框中输入skills，按回车将Agent Skills设置为true*如图所示


> [!NOTE] [图片 OCR 识别内容]
> Settings
> skill
> Agent Skills
> tPuex
> Enable Agent
> Skills Cexperimental)
> Apply
> To
> User Settings
> Workspace Settings
> System Settings
> (Use
> Enter
> to
> select
> Tab
> to change focus
> Esc
> to
> Close)


这时候我们退出再重新进入，在对话框中输入/skills列出所有的技能，如图所示就表示成功了，有一点需要注意你启动Gemini的目录中需要有~/.gemini/skills/ 
> [!NOTE] [图片 OCR 识别内容]
> /skills
> Available Agent
> Skills
> brain-Calculate-alpha-selfcorrQuick
> Calculates
> self-correlation
> and
> PPAC (Power Pool Alpha
> correlations
> checks
> PPAC
> brain-datafield-exploration-general
> Provides
> 6 proVen
> methods
> to
> eValuate
> new datasets
> 00
> t
> Use
> When
> the
> USer Wants
> to
> understand
> specific datafie
> brain-dataset-exploration-general
> Provides
> comprehensive Workflow for deep-diving
> into
> research
> Use
> When
> the
> user Wants
> to
> audit
> dataset"
> brain-explain-alphas
> Provides
> step-by-step Workflow for analyzing
> and explz
> operators
> Work together
> Includes
> steps
> for data
> field
> brain-how-to-pass-AlphaTest
> Provides
> detailed requirements
> thresholds
> and improver
> When the
> User asks
> about alpha submission
> failures
> how


---

## 讨论与评论 (12)

### 评论 #1 (作者: CW62372, 时间: 5个月前)

====================================================================================

大佬执行力真是强，这么快研究好gemini-cli版本的了。有个问题需要请教下，复制过来的包含

~/.claude/skills/explaining-code/SKILL.md内容应该都得相应更改对吧。应该有许多地方原来写的是claude，现在需要改成gemini。

====================================================================================

---

### 评论 #2 (作者: 顾问 JG15244 (Rank 67), 时间: 5个月前)

TT大佬，学习了！

---

### 评论 #3 (作者: OY62064, 时间: 5个月前)

非常不错的教程，这样gemini cli 就可以用上技能了，在分析alpha的时候可以直接调用了！！！============================================================================                                          “路漫漫其修远兮，吾将上下而求索”
============================================================================

---

### 评论 #4 (作者: ZL64136, 时间: 5个月前)

感谢大佬分享，目前已经用上了，祝大佬更上一层楼!!! gemini cli每周更新，现在stable版本好像也可以用Agent Skills

---

### 评论 #5 (作者: LL46807, 时间: 5个月前)

T神！

---

### 评论 #6 (作者: YX50005, 时间: 5个月前)

哇，原来如此，各家AI工具纷纷支持skills，看来skills会继MCP之后成为A家主导的新标准了，看来skills开发必须学起来了！

---------------------If you come to the forum to study hard every day, you will get a GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------

---

### 评论 #7 (作者: QM70930, 时间: 5个月前)

感谢

---

### 评论 #8 (作者: MH27590, 时间: 5个月前)

感谢大佬分享，学习了！

---

### 评论 #9 (作者: MZ23121, 时间: 5个月前)

感谢大佬的分享，终于用上Gemini cli的里面的skills，用kimi的是真的不知道怎么计费的，一会时间30就没了。

---

### 评论 #10 (作者: 顾问 LW67640 (小虎) (Rank 24), 时间: 5个月前)

感谢分享，太赞啦！

在xhs上搜索了好几天，没有结果。

问iflow, gemini，没有结果。

但在咱们的顾问论坛里找到了解决方法，再次感谢！

============================================================================

长风破浪会有时，直挂云帆济沧海

============================================================================

---

### 评论 #11 (作者: XC66172, 时间: 5个月前)

感谢大佬分享！！还是免费的真香

让我试一下能否使用~~

================================

FIGHTING LABUBU!

================================

---

### 评论 #12 (作者: 顾问 MZ45384 (大角羊) (Rank 51), 时间: 5个月前)

学习了，不知道跟mcp使用起来体感有何不同

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

