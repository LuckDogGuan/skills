---
name: wq-top-advisors-skill
description: |
  「WorldQuant Brain 黄金顾问团」精选量化分析与因子挖掘智慧大脑。
  整合了 WQ 论坛官方前 10 位顶级核心顾问（王哥、台湾第一、贺六浑、小虎、大角羊、点塔王等）的高价值发帖、回复及技术分享。
  触发词：「黄金顾问」「因子挖掘」「ATLAS架构」「自相关性检测」「Decay扫频」「中性化配置」
---

# WorldQuant Brain 黄金顾问团（精选）Skill

本 Skill 精选了 WorldQuant Brain 官方论坛前 10 位最核心、贡献最突出的黄金顾问发帖与回复数据（去除其他 89 位低活跃与纯回帖噪音），并进行了完整的脱敏、除噪、OCR图片文本融合。形成了供大模型直接检索调用的量化策略知识底座。

## 1. 黄金顾问画像结构

在 `references/distilled_profiles/` 中拥有 10 位核心明星顾问的独立技术画像：
- **Rank 1**: YW82626 (台湾第一 / Selection-Combo专家)
- **Rank 3**: ZS59763_worldquant_brain赛博游戏王 (王哥 / 自相关与行业中性化压力测试导师)
- **Rank 6**: JR23144_贺六浑 (量化工程优化、own三五SA架构大师)
- **Rank 9**: JX79797_华子哥 (Genius Rank 分析与插件开发专家)
- **Rank 11**: ZH78994 (机器学习与量化基础大满贯博主)
- **Rank 14**: AY17279 (《我的量化日记》实战成长经验博主)
- **Rank 22**: FX25214_传奇耐打王 (传奇耐打王系列思考，因子反思导师)
- **Rank 24**: LW67640_小虎 (小虎 / 16815美刀季度奖经验分享与wqb库开发者)
- **Rank 51**: MZ45384_大角羊 (大角羊团队 / pyramid金字塔管理工具专家)
- **Rank 84**: QP72475_点塔王 (点塔王 / 相似因子大语言模型搜索技术开拓者)

## 2. 知识库目录规范

* **[顾问核心画像 (distilled_profiles/)](file:///references/distilled_profiles/)**：各黄金顾问的核心发帖论点、答疑对话录和表达DNA。
* **[论坛精选按主题归档 (forum_posts/)](file:///references/forum_posts/)**：包含约 800 篇已融合图片 OCR 文字的黄金顾问团精选 Markdown 帖子，并配有 [精选大纲索引(index.md)](file:///references/forum_posts/index.md)。分类包括：
  1. `01_super_alpha`: Super Alpha 竞赛与配置 (SAC)
  2. `02_value_factor`: Value Factor 价值因子挖掘
  3. `03_genius_and_pyramid`: Genius段位与Pyramid晋升机制
  4. `04_stability_and_robustness`: 稳健性与鲁棒性（Decay/中性化扫频）
  5. `05_datafields_and_operators`: 数据字段与算子表达式签名研究
  6. `06_engineering_and_code`: Python/API代码优化与回测内存优化
  7. `07_newbie_and_career`: 新手日常、职业避坑与收入经验
  8. `08_general_research`: 综合量化研究
