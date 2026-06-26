# 【SKILLS everywhere】自动同步skills，从claude到gemini，codex，iflow

- **链接**: https://support.worldquantbrain.com[Commented] 【SKILLS everywhere】自动同步skills从claude到geminicodexiflow_37745706080407.md
- **作者**: FF56620
- **发布时间/热度**: 5个月前, 得票: 71

## 帖子正文

随着claude将skills进行标准化，各家也对skills进行了支持，本文简单介绍一下在各种工具中对于skills的使用，供大家参考。

现在大家对skills的规范支持都是一样的，内部结构都保持一致，结构如下：

```
skills/
└── skillsA/
    ├── SKILL.md
    └── ...
└── skillsB/
    ├── SKILL.md
    └── ...
└── skillsC/
    ├── SKILL.md
    └── ...
```

但是对于顶层目录的要求是不同的，如果你已经安装了AI打工人，你会发现其默认在.claude文件夹下，而对于其他工具，这个目录的要求是不同的， gemini在.gemini文件夹下，codex在.codex文件夹下，而iflow在.iflow文件夹下，这会让文件维护变得很困难，无法做到一个地方修改，其他地方徒步，当前，如果你不知道怎么用下面的工具，也可以使用复制的方式

# Step 1

准备好fswatch，监听  `~/.claude/skills`  的变化，具体目录可根据实际需求进行调整

```
brew install fswatch

```

# https://linux.do/t/topic/1468794#p-12652197-step-2-2 Step 2

准备一个  `sync_skills.sh` :

```
#!/bin/bash
fswatch -o ~/.claude/skills | while read f; do
    rsync -a --delete --exclude-from=～/.codex/skills/.exclude-list ~/.claude/skills/ ~/.codex/skills/
    rsync -a --delete --exclude-from=～/.gemini/skills/.exclude-list ~/.claude/skills/ ~/.gemini/skills/
    rsync -a --delete --exclude-from=～/.iflow/skills/.exclude-list ~/.claude/skills/ ~/.iflow/skills/
done

```

其中  `--exclude-from`  是为了在某些工具中想要排除一些skills的同步，比如有一些skills只能用于某个工具里，就可以创建一个 `.exclude-list` 文件，把要排除的skills文件夹名丢进去，一行一个。

最后，还有一个tips，在codex中，需要通过.codex/config.toml开启skills才能使用

```
[features]skills = true
```

---

## 讨论与评论 (6)

### 评论 #1 (作者: JY56809, 时间: 5个月前)

简单粗暴的把 skill文件夹复制粘贴过去了。

---

### 评论 #2 (作者: JT59922, 时间: 5个月前)

iflow我是直接复制skill文件夹到对应配置文件夹，按配置规范创建就行，命令行检查下能识别到

---

### 评论 #3 (作者: EP71225, 时间: 5个月前)

这是mac的，windows怎么弄呢

---

### 评论 #4 (作者: TZ69297, 时间: 5个月前)

用cc switch一键管理skills和MCP，支持claude，gemini，codex，还能一键代理API大模型 
> [!NOTE] [图片 OCR 识别内容]
> CC Switch
> Skills 管理
> 导入已有
> 发现技能
> 已安装
> Claude: 12 . Codex: 0 . Gemini: 0
> brain-Calculate-alpha-selfcorrQuick
> Claude
> Calculates self-correlation and PPAC (Power Pool Alpha Correlation) for WorldQuant BRAIN alphas
> Codex
> Locally, this can be very fast than query the platform via mcp. Use this when the user calculates alph...
> 本地
> Gemini
> brain-data-feature-engineering
> Claude
> Automatically analyzes BRAIN dataset fields and generates feature engineering ideas for alpha
> Codex
> creation. Input: data category, delay, region parameters; Output: markdown document with deep。..
> 本地
> Gemini
> brain-datafield-exploration-general
> Claude
> Provides 6 proven methods to evaluate new datasets on the WorldQuant BRAIN platform. Includes
> Codex
> methods for checking coverage; non-zero values, update frequency; bounds, central tendency,and ..
> 本地
> Gemini


---

### 评论 #5 (作者: MG77993, 时间: 4个月前)

可以用软链接,维护一份skills文件就可以.

---

### 评论 #6 (作者: 顾问 MZ45384 (Rank 51), 时间: 16天前)

太方便了，看得出来现在大佬们都在同时使用多份AI大模型和对应cli工具。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

