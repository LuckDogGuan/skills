# 【工作流分享】基于openclaw的自动化agent工作流经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【工作流分享】基于openclaw的自动化agent工作流经验分享_39354616684439.md
- **作者**: ZQ21774
- **发布时间/热度**: 3个月前, 得票: 8

## 帖子正文

利用996中难得的周末，通过codex等vibe coding工具，设计一套基于openclaw的自动化工作流

## 关键组件

### 1. OpenClaw Agent 层

当前 MVP 里有 3 个 agent：

- `alpha_pm`
- `researcher_hkg`
- `researcher_eur`

其中：

- `alpha_pm` 是总控，负责看 pyramid、配额、submission funnel，然后下发 assignment
- `researcher_*` 是区域锁定研究员，只处理自己 region 的 assignment
- 后续扩 region 时，不需要改 simulator 和数据库主结构，只要加新的 `researcher_<region>` 即可

### 2. Skill 层

因为 OpenClaw 不支持原生 MCP，我把 WQB 平台的能力全部桥接成了本地 skills。

一类是业务技能：

- `pm_get_pyramid_status`
- `pm_check_daily_limits`
- `pm_submit_alphas`
- `pm_daily_report`
- `research_get_regional_data`
- `research_review_local_context`
- `research_save_templates`
- `research_compile_templates`
- `research_verify_expressions`
- `research_peer_review`

另一类是平台桥接技能：

- `wqb_get_platform_setting_options`
- `wqb_get_datasets`
- `wqb_get_datafields`
- `wqb_create_simulation`
- `wqb_create_multi_simulation`
- `wqb_get_alpha_details`
- `wqb_get_alpha_pnl`
- `wqb_get_alpha_yearly_stats`
- `wqb_get_submission_check`
- `wqb_check_correlation`
- `wqb_submit_alpha`
- `wqb_set_alpha_properties`
- `wqb_get_pyramid_multipliers`
- `wqb_get_pyramid_alphas`
- 以及其余一整套 BRAIN 平台工具

本质上就是把原来 `platform_functions.py` 里的工具面，全部封装成 OpenClaw 可直接调用的本地 `wqb_*` skills。

### 3. Simulator Daemon

simulator 被设计成纯执行器，不承担 PM 决策逻辑。

它只做几件事：

- 从数据库里领取 `READY` 的回测任务
- 按完整 settings 分桶，确保 multi-sim 不跨 `region / delay / universe / language / instrumentType`
- 向 WQB 发 simulation
- 轮询 simulation 结果
- 抽取 `alpha_id`
- 回写 IS 指标、PnL、yearly stats、submission check、corr 信息
- 按美东日期给 alpha 打 tag

### 4. PostgreSQL 状态面

数据库不再只是存表达式，而是承担整套 pipeline 的状态机，包括：

- reference data
- pyramid snapshot
- PM assignment
- researcher output
- backtest queue
- WQB alpha artifacts
- submission funnel
- daily report

## 流程图


> [!NOTE] [图片 OCR 识别内容]
> OpenClaw Cron
> alpha_pm
> superisor
> fallback
> operator
> sync pyramid
> quota
> reference
> build assisnments
> researcher_hkg
> researcher
> eUI
> researcher
> PostgresQl
> WW_ready_
> backtest_bucket
> VW_submission_candidates
> simulator-dispatch
> WorldQuant BRAIN
> simulator-
> Doll


## PostgreSQL 表结构

表结构大致分成 5 层。

### 1. 参考数据层

- ref_setting_combo
- ref_dataset
- ref_datafield

用途：

- 缓存合法 simulation settings
- 缓存 dataset / datafield 元信息
- 给 researcher 做 grounding，避免胡编 field

### 2. 策略与运营层

- pyramid_snapshot_batch
- pyramid_status_snapshot
- daily_quota_usage

用途：

- 保存每次抓取的 pyramid 状态
- 同时记录 multiplier 和 alpha_count
- 显式记录每日 simulation / submission 配额，而不是靠统计推断

### 3. PM / Research 层

- researcher_registry
- pm_cycle
- pm_assignment
- research_run
- peer_review
- alpha_template
- alpha_candidate
- alpha_candidate_validation

用途：

- PM 生成 assignment
- researcher 基于 assignment 产出模板和 candidate
- 保存 peer review 和静态验证结果
- lineage_date_et 贯穿整个链路

### 4. 回测执行层

- backtest_batch
- backtest_job
- wqb_alpha
- alpha_snapshot_raw
- alpha_metric_is
- alpha_pnl_raw
- alpha_yearly_stats_raw
- alpha_pnl_quality
- alpha_check

用途：

- backtest_job 是唯一合法的回测队列表
- backtest_batch 用来承接 multi-sim parent request
- 所有 WQB 回测产物统一挂到 wqb_alpha_id

### 5. 提交与报告层

- submission_policy
- submission_attempt
- alpha_submit_funnel_day
- daily_report

用途：

- 保存提交门槛
- 记录每日 submission funnel
- 输出日报

## Appendix

系统中的很多部分都是基于社区里大佬的源码和提示词开发的，感谢大佬。
因为是刚落地，还没有跑出什么值得分享的结果。欢迎大家分享，也欢迎架构大佬指点。环境的话我是使用的2c4g的linux，不推荐2c2g的，在安装openclaw时容易卡死。

---

## 讨论与评论 (8)

### 评论 #1 (作者: TS80399, 时间: 2个月前)

坐个沙发，可以搞个docker

---

### 评论 #2 (作者: 顾问 LW67640 (小虎) (Rank 24), 时间: 2个月前)

感谢大佬的分享，虽然有了ai辅助，把这套流程搞下来也是需要不少精力的。

从论文出发这个点学习到了，看来token plan的钱省不了。

上下文的问题，大佬是怎么解决的？

==============================================================

长风破浪会有时，直挂云帆济沧海。

==============================================================

---

### 评论 #3 (作者: LG87838, 时间: 2个月前)

我的openclaw干了一个礼拜，想卸载了，突然提交两个atom的regular alpha。

估计很多顾问和我一样，尝试了新武器，但忽略如何把新武器用起来？修改架构/设约束。。。

-------------------------------------------------------------------------------------------

慢慢来，相信时间的力量。

-------------------------------------------------------------------------------------------

---

### 评论 #4 (作者: ZC26080, 时间: 2个月前)

工作流不错，请问大佬用这套工作流的产出如何？（个人感觉AI在优化已有alpha上比较给力，但是在全自动挖掘方面依然有所不足）

=================================================================================

Study hard — quality over quantity, no room for mediocrity. Cherish every learning opportunity, stay focused, and learn from the experts. Keep pushing!

=============================================================================

---

### 评论 #5 (作者: CH62432, 时间: 2个月前)

考虑到安全性问题一直没有没敢尝试openclaw去做alpha , 看过大佬的分享后很有启发效果,期待后续的继续分享!

==================================================================================

“牛市在悲观中诞生，在怀疑中成长，在乐观中成熟，在狂热中死亡。”
 *(Bull markets are born on pessimism, grow on skepticism, mature on optimism, and die on euphoria.)*

*==================================================================================*

---

### 评论 #6 (作者: 顾问 MG88592 (Rank 38), 时间: 2个月前)

感谢分享，正好买了一个服务器还没排上用场，空闲了可以琢磨琢磨。

-------------------------------------------------------------------------------------------

慢慢来，相信时间的力量。

-------------------------------------------------------------------------------------------

---

### 评论 #7 (作者: YX50005, 时间: 2个月前)

我也试了openclaw，目前还在一个比较鸡肋的状态，似乎比用一个固定的脚本好一点，但是也好不了多少。。。

来学习一下大佬的用法，得到了不少启发！

---------------------If you come to the forum to study hard every day, you will get a GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------

---

### 评论 #8 (作者: SZ20589, 时间: 2个月前)

感谢大佬分享，准备买个服务器来用openclaw来挖因子，但是还不知道token使用量能不能扛得住啊

=============================================================================

========Genius is one percent inspiration and ninety-nine percent perspiration.=============

==============================================================================

---

