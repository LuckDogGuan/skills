# 【工具分享】Pkgdiff：在线免费给cnhkmcp做版本差异分析

- **链接**: https://support.worldquantbrain.com[Commented] 【工具分享】Pkgdiff在线免费给cnhkmcp做版本差异分析_40292420301591.md
- **作者**: ZH74761
- **发布时间/热度**: 1个月前, 得票: 7

## 帖子正文

上次做了一个小工具 [追踪每一次cnhkmcp的更新]( [[L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md]([L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md)  )，但还是有一些不人性化的地方，比如需要手动操作可能会破坏本地的代码，以及就算有版本diff也并看不懂的问题。于是诞生了这次新做的在线版本： [https://pkgdiff.app/](https://pkgdiff.app/)

**起因**

升级一个 Python 依赖之前，正常的流程是去 GitHub 翻 changelog或 release notes。但实际上经常会遇到几种情况：

- 包根本没有公开源码仓库
- 仓库存在但跟 PyPI 上发布的 wheel 已经不一致（构建脚本生成、私有 patch、被 fork 后改名上传等）
- 仓库的 release notes 写得极其敷衍，只有 "bugfixes and improvements"

这些场景下，唯一可信的事实来源就是 PyPI 上那个 wheel/sdist 本身。pkgdiff 就是奔着这个前提做的：不假设有 git 历史、不假设有 changelog，只看两个版本的发布产物。

**它做什么**

给定 (package, from_version, to_version)，输出一份结构化的 diff 报告：

1. **文件级 diff**  — 每个文件 added / removed / modified，文本文件给出 unified diff，二进制（.so / .pyd）只标记内容变化
2. **公共 API surface diff** — 加载两个版本的源码，对比模块、类、函数、属性的增删改，识别函数签名变化，标注哪些是 breaking
3. **元数据 diff** — Requires-Dist、Requires-Python、license、classifiers、entry points 的逐项变化
4. **LLM 摘要** — 把上面三段结构化 diff 喂给 LLM，生成一份人类可读的 Markdown 变更说明 + breaking-change brief

**第 4 点**  是关键的"最后一公里",也正是和前一篇内容的差别。前三个 analyzer 已经把"发生了什么"用机器可读的格式还原出来了，但人类升级依赖时真正想知道的是"这个变化会不会影响我"。LLM 在这里不负责发现事实，只负责把已经被严格挖出来的事实翻译成自然语言。

同时它还支持 Stepwise 模式。普通模式做 2.30.0 → 2.31.0 的 diff。但有时你跨了 5 个版本，把所有变化压成一个 diff 会丢失节奏感——你不知道 breaking change 是在哪个中间版本引入的。

Stepwise 模式给定一个版本序列，对每对相邻版本各跑一次完整 pipeline，最后再用一个汇总 LLM 调用把 N 份分步摘要合成一份统一的 changelog。

这个服务可以免费使用，且不需要注册！不仅针对cnhkmcp，也可以是任何python package. 大家有什么想法和建议欢迎评论~


> [!NOTE] [图片 OCR 识别内容]
> See What actually changed
> between two package versions。
> Don't trust hand-written changelogs. Pkgdiff reads the published artifacts directly and tells you
> exactly What's different
> public API, dependencies, files
> with an Al-written summary on
> ECOSYSTEM
> Python
> PACKAGE
> cnhkmcp
> FROM
> TO
> 2.3.18
> 3.1.11
> Add AI summary
> Step through every version
> 14 steps
> Analyze
> Currently supports Python
> tOP.



> [!NOTE] [图片 OCR 识别内容]
> CNHKMCP
> 2.3.18
> 3.1.11
> cnhkmcp
> 2.3.18
> 3.1.11
> breaking
> Overview
> 14steps
> 14 version steps
> 14 with breaking changes
> 2.3.18
> 2.3.19
> PUBLIC SYMBOLS
> API CHURN (SUM)
> BREAKING-API COUNT
> FILE OPS (SUM)
> 2.3.19
> 2.3.20
> 5
> 5
> +0
> -0
> ~0
> +10719
> -10183
> ~250
> 2.3.28
> 3.0.0
> 3.8.0
> 3.1.8
> 3.1.0
> 3.1.1
> Changelog
> 2.3.18
> 3.1.11
> 3.1.1
> 3.1.2
> Summary
> 3.1.2
> 3.1.3
> This upgrade is mostly about the app's embedded workflow tools rather than the importable Python APl. Across the range;
> cnhkmcp   grows from
> a small
> packaging refresh into
> a much broader BRAIN/orchestrator platform with pipeline lifecycle
> 3.1.3
> 3.1.4
> controls; prompt customization, simulation/status improvements;, credential/session persistence; and richer operator catalogs。
> 3.1.4
> 3.1.5
> The web UI also changes substantially: new dashboards and modal controls appear; some flows are reworked for better
> persistence and visibility, and the landing page is reorganized around the main BRAIN workflows. Operators using the pipeline
> 3.1.5
> 3.1.6
> Ul, simulator tooling, alpha submission paths, or generated formulas should review this upgrade carefully:
> 3.1.6
> 3.1.7
> New features
> 3.1.7
> 3.1.9
> Added and expanded the
> brain-orchestrator
> control plane under
> cnhkmcp /untracked /APP /brain-orchestrator /
> including
> 3.1.9
> 3.1.18
> pipeline runner/state management; stage modules
> stage_decide.py
> stage_enhance. Py
> stage_implement .py
> stage_inspect . Py
> stage
> simulate. py
> ) and dashboard docs/templates。
> 3.1.18
> 3.1.11
> Added pipeline lifecycle endpoints and UI actions for: delete, archive; restore, and list archived pipelines force-restart ofa
> pipeline via
> POST /api/pipeline/pipeline_id>
> force-restart
> updating stop conditions at runtime via
> POST
> /api/pipeline /<pipeline_id> /update-stop-conditions
> Added prompt-preview and prompt-editing support in the pipeline dashboard, including a phase-prompt preview endpoint
> and an advanced prompt/settings modal。
> Added structured stop-condition support for pipeline runs; including:  sharpe_target
> count
> pool_ideas
> max_alpha_
> submitted
> max_sim_completed
> max_iterations
> diminishing_returns
> optional
> use_abs
> for Sharpe
> thresholding
> Expanded
> trailSomeAlphas
> generation and enhancement workflows:
> implement
> idea.py
> DOW
> supports
> idea
> run_pipeline. Py
> HOW
> supports prompt overrides; adaptive retry on token-limit failures; and full-field prompting when
> max-fields
> is omitted
> enhance_template. py
> supports single-mode and cross-mode enhancement; with style instructions Via
> CROSS
> PROMPT_STYLES
> the cross-enhance UI now supports multiple uploaded idea files and selectable cross styles manual
> "Cross 手动输入
> Workflow documentation Was added
> Added environment propagation for universe-aware enhancement; including
> UNIVERSE
> being passed into subprocesses so
> manual and automated enhancement target the same stock pool。
> Added pipeline-level LLM request accounting:
> record_Ilm_request(
> summarize_IIm_requests
> Ilm_requests .jsonl
> artifacts per pipeline per-stage tagging for
> generate
> inspect
> enhance
> and
> decide
> max_



> [!NOTE] [图片 OCR 识别内容]
> cnhkmcp
> 3.1.10
> 3.1.11
> breaking changes
> pypi . generated 5/5/2026,4:37:53 PM
> API SYMBOLS
> API CHANGES
> DEPENDENCY ENTRIES CHANGED
> FILES (OLD
> NEW)
> 5
> 5
> +0
> -0
> ~0
> 949
> 949
> Export Markdown
> Export PDF
> Summary
> API
> Metadata
> Files
> 20
> Summary
> Summary
> cnhkmcp 3.1.11 is a UI- and operator-catalog-focused release. The package keeps the same public Python API surface; but several front-end workflows were refactored and
> the supported operator list changed. Engineers using the web UIor generating formulas from
> Vvalidop.json
> should review this upgrade carefully:
> New features
> Added a new simulator
> pointin
> cnhkmcp /untracked/APP _
> static /script.js
> runHKFacesimulator( )
> wired to a new
> 命令行页面 (人脸识别版)" option in the
> 'Run
> Simulator'
> modal
> Expanded the operator catalog in
> cnhkmcp
> untracked /APP /validop .json
> with new operators:
> pasteurize(x)
> ts
> returns (X,
> 4,
> mode
> 1 )
> group_count(x,
> group )
> group_std_dev(x,
> group )
> group_sum(x,
> group )
> Refactored the landing page in
> cnhkmcp /untracked/APP / templates
> index.html
> into staged sections for the main workflows, making the Alpha judge; Alpha submitter, and
> pipeline entry points more prominent:
> cnhkmcp_
> untracked
> APP
> static /inspiration.js
> now binds the inspiration modal to any
> inspiration-trigger
> element; allowing multiple UI entry points instead ofa
> single hard-coded button.
> fixes
> In
> cnhkmcp
> untracked/APP / 运行打开我 . Py
> credential caching now fails gracefully: writing ACE credentials to local disk is wrapped in
> try/except
> and Iogs a
> warning
> instead of raising.
> The pipeline credential sync
> in
> cnhkmcp /untracked/APP / 运行打开我 . Py
> is also guarded so local pipeline updates do not crash the process if an internal error occurs:
> Task lookup endpoints in
> cnhkmcp
> untracked/APP / 运行打开我. Py
> now return clearer JSON errors When a task is missing or when
> day_key
> is absent; replacing the previous
> garbled messages。
> The Alpha Inspector import pathlcomment in
> cnhkmcp /untracked/APP / 运行打开我 . Py
> Was corrected to Use
> 缘分
> 道桥
> Which should make the route setup easier to
> understand and maintain。
> Behavior & deprecations
> cnhkmcp /untracked/APP
> static /inspiration.js
> now enables/disables all
> inspiration-trigger
> buttons based on login state; rather than targeting a single
> entry
> Bug
> path



> [!NOTE] [图片 OCR 识别内容]
> Summary
> API
> Metadata
> Files
> 20
> 949
> 949 files
> +6 -6 ~8
> all
> added
> removed
> modified
> cnhkmcp/ _
> init_.Py
> cnhkmcp /untracked/APP
> ace
> cnhkmcp /untracked/APP _
> static /inspiration.js
> cnhkmcp /untracked/APP _
> static /script.js
> cnhkmcp /untracked/APP_
> static /styles _
> CSS
> cnhkmcp /untracked/APP / templates _
> index.html
> cnhkmcp /untracked/APP /validop .json
> cnhkmcp /untracked/APP _
> /运行打开我. py
> 285,7
> +285,18
> 285
> 285
> password
> str(password
> Or
> ).strip()
> 286
> 286
> i
> not
> Username
> Or
> not password:
> 287
> 287
> return
> 288
> WT
> ~ite_json_file(_ace_credentials_path(),
> {'email'
> username,
> password
> password} )
> 288
> try:
> 289
> Write_json_file(_ace_
> credentials_path(),
> {'email'
> username,
> password 
> password})
> 290
> except Exception
> as
> e:
> 291
> print (f"
> Warning:
> Could
> not
> cache
> credentials to
> local
> disk:
> {e}")
> 289
> 292
> 290
> 293
> 291
> 294
> def
> sync_pipeline_credentials (username
> password:
> str):
> 297,19 +380,22
> 297
> 300
> return
> 298
> 301
> 299
> 302
> updated
> 300
> for
> item
> in
> list pipelines()
> 1o8
> str,


---

## 讨论与评论 (5)

### 评论 #1 (作者: 顾问 RM49262 (Rank 30), 时间: 1个月前)

=====================================评论区====================================

感谢大佬分享！ 作为代码小白总是不知道CNHKMCP每次更新了啥

这下一眼就能看出来了

=============================================================================

---

### 评论 #2 (作者: XW23690, 时间: 1个月前)

感谢大佬分享。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #3 (作者: BW14163, 时间: 1个月前)

这简直是 Python 依赖管理的“救命稻草”！作为开发者，最头疼的就是遇到那种 Release Notes 写得敷衍、甚至没有公开源码仓库的依赖包，升级全靠“猜”和“赌”。

pkgdiff 直接回归“发布产物”这个唯一可信源，太务实了。特别是它引入 LLM 做“最后一公里”的翻译，把冰冷的代码 diff 变成可读的 Breaking Change 简报，完美解决了“知道变了什么，但不知道会不会搞挂我”的痛点。再加上 Stepwise 模式能还原版本演进的节奏感，简直是 CI/CD 流水线的必备神器。强烈建议作者开源，造福社区！

差不多快半年没更新了，该天抽空去看看有啥新的功能，扒下来引用一下

---

### 评论 #4 (作者: 顾问 FX25214 (传奇耐打王/耐打王) (Rank 22), 时间: 1个月前)

这种巧思每次看到都会让我眼前一亮。对于这么一个几乎每天大家都在使用的东西。变了什么，有时候尤为重要。因为我们要学习这个作者的思想，明白为什么这么变。或者根据个人使用习惯，决定自己是否要撤回这么变，或者再依据作者的灵感，想清楚自己可以怎么变。这个小工具的实用价值真的太有效了
--------------------------------来自传奇耐打王的点赞---------------------------------------------------------------------

---

### 评论 #5 (作者: RW22124, 时间: 20天前)

感谢分享，这个是真需要！

=============================================================================

爱来自中国

=============================================================================

---

