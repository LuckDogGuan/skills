---
name: wq-advisors-skill
description: |
  「WorldQuant Brain 顶级顾问团」的量化分析与因子挖掘智慧大脑。
  整合了 WQ 论坛前 100 名顶级顾问的发帖、回复、技术见解，并融合了大量回测图片、PnL、算子报错的 OCR 解析文本。
  触发词：「顾问排名」「因子挖掘」「ATLAS架构」「自相关性检测」「Decay扫频」「中性化配置」
---

# WorldQuant Brain 顶级顾问联合智能体 Skill

本 Skill 整合了 WorldQuant Brain 官方论坛前 100 名顶级顾问的发帖和回复数据，并对海量图片资源进行了 GPU 级别的 EasyOCR 文字提取，在脱敏和去噪的基础上，形成了供多模型/智能体直接调用的结构化量化策略知识库。

## 1. 核心顾问画像结构

在 `references/distilled_profiles/` 中拥有 57 位高活跃明星顾问的独立技术视角（文件夹名称带排名，例如 `Rank01_YW82626`、`Rank03_ZS59763_worldquant_brain赛博游戏王`），以及 30 位低活跃顾问的合并画像 `RankCombined_wq_advisors`。

你可以在回答时引用以下高活跃顾问在 `01-writings.md`、`02-conversations.md`、`03-expression-dna.md` 中留存的经典心智模型和最佳实践：
- **Rank 1**: YW82626 (Selection/Combo表达式专家)
- **Rank 3**: ZS59763_worldquant_brain赛博游戏王 (全自动爬山、自相关避坑、Decay与行业中性化压力测试导师)
- **Rank 6**: JR23144 (中国区核心顾问，庞大的因子产出与论坛答疑语料)
- **Rank 14**: AY17279 (拥有 220 万字超大体量技术发帖分享)
- **Rank 84**: QP72475 (拥有 380 万字巨量论坛技术讨论)

## 2. 知识库目录规范

* **[顾问核心画像 (distilled_profiles/)](file:///references/distilled_profiles/)**：各独立明星顾问和合并顾问的核心发帖论点、答疑对话录和表达DNA。
* **[论坛精选按主题归档 (forum_posts/)](file:///references/forum_posts/)**：包含 7,548 篇已融合图片 OCR 文字的论坛原始 Markdown 文章，并配有 [大纲索引(index.md)](file:///references/forum_posts/index.md)。分类包括：
  1. `01_super_alpha`: Super Alpha 竞赛与配置 (SAC)
  2. `02_value_factor`: Value Factor 价值因子挖掘
  3. `03_genius_and_pyramid`: Genius段位与Pyramid晋升机制
  4. `04_stability_and_robustness`: 稳健性与鲁棒性（Decay/中性化扫频）
  5. `05_datafields_and_operators`: 数据字段与算子表达式签名研究
  6. `06_engineering_and_code`: Python/API代码优化与回测内存优化
  7. `07_newbie_and_career`: 新手日常、职业避坑与收入经验
  8. `08_general_research`: 综合量化研究
