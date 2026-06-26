# 【Alpha灵感】AI搜索字段极性配对，构建低PC因子(附提示词)经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】AI搜索字段极性配对构建低PC因子附提示词经验分享_39845230299927.md
- **作者**: MY82844
- **发布时间/热度**: 2个月前, 得票: 64

## 帖子正文

延续之前在 [Sentiment塔]([Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md) 里通过字段极性配对(polarity pairs)构造差异化RA的思路，在AI帮助下，我们发现类似的想法可以推广到更到数据集，构造一些低PC的因子，缓解SLOW_AND_FAST theme时期的断粮危机。

第一步，使用提示词，调用大模型的看家本领，让大模型寻找给定数据集里面的极性配对：

SYSTEM_POLARITY = """You are a quantitative data curator for WorldQuant BRAIN-style datafields.

Task: find **semantic polarity pairs** within the SAME dataset chunk — two fields that describe the **same underlying concept** but **opposite valence** (e.g. positive vs negative sentiment, bullish vs bearish, increase vs decrease counts, upgrade vs downgrade, up vs down in the same metric family).

Rules:

- Use BOTH **field id** and **description**.

- **field_id_more_positive**: the field whose values represent the more **positive / favorable / bullish / upward** direction for that paired concept.

- **field_id_more_negative**: the more **negative / unfavorable / bearish / downward** direction.

- If you are not sure, do NOT invent pairs.

- **Every id MUST be copied exactly** from the provided table (same spelling).

- Output **ONLY** a JSON array (no markdown, no commentary). Schema:

[{"field_id_more_positive":"...","field_id_more_negative":"...","pair_label":"short EN label","confidence":0.0,"reason_zh":"一句中文理由"}]

If no pairs: [].

"""

大模型在这种任务上准确率普遍较高，比如在IND，可以得到如下的结果：


> [!NOTE] [图片 OCR 识别内容]
> dataset_id
> Dair_
> inde
> field_id_Jore_Dositive
> field_id_Jore_
> negatixe
> Dair_Iabel
> confiderce
> Lea3oll_ZhI
> JIa133t4
> hiahest
> eetiate
> 1owe3t
> 331e3_eetijate
> SaLe3
> 〈allllal〉
> eetiate
> bolarity
> 销售额年度最高与最低估计
> 表示相反销售预期
> JIa133t4
> OB 331e3
> estijate_JazinlJ_
> Cllarterl3
> estinate_JiriJlJ_
> clarterl3
> 3a1e3
> 〈quarterl
> estijate Dolarity
> 销售额季度最
> 与最低估计
> 体现相反营恢趋势
> JIa133t4
> 0? shareholder3 _
> estijate_JaxinU_Gf
> shareholder3_
> ecllity_
> estijate_JiriJll_rf
> Shareholder?
> eetiate
> bolarity
> 股东极益的
> 低估计
> 伐表相反资本结构预期
> JIa133t44
> pretaxprofi
> eetiates
> Hre
> taxprofi
> estijates_
> dowrri_
> Pretay profi
> eetiate
> LeTi31o11
> Colllzt
> 和向
> 修订数量
> 问上修订积极 =
> 向下修订消报
> JIa133t44
> 116 Ioe
> I11II
> estijates_
> 1I
> Loe
> IlJL_ estijates_
> dowrri_
> R讵
> eetiate
> LeT1310I1
> Colllzt
> 估计4周
> 和向
> '修订数量,问上修订积极
> 向下修订消极。
> JIa133t44
> 11? &ales_upwlrard_revisiors _
> 341e3
> dowrrzwrard
> LeTi310113_
> 3a1e3
> estijate rerisiorl
> Colllzt
> 销售额估计4周内向上和向下修订数量
> 问上修订积极 _
> 向下修订消报
> JIa133t-
> 118 all G
> bdzd
> opt_iplied
> 工aI8e
> aIL $
> bdrd_opt_implied_rarge
> Optioris
> Implied Rarge
> 期杈隐
> 范围的高值和低值
> 高值表示乐观预期,低值表示悲观预期
> 531
> egUI
> egUI
> Hieh


第二步，我们可以通过简单的运算导出一些新的变量：

```
diff = fld_pos - fld_neglog_diff = log(fld_pos) - log(fld_neg)ratio = fld_pos / (fld_pos + fld_neg)
```

然后，从这些新的变量出发，通过一二阶的单变量算子，可以构造一些差异化的ATOM类型的alpha。因为相对的使用配对的顾问还比较少，在各大region还是可以出一些PC比较低的因子。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> A Sirgle Data Set Alpha
> Regular Alpha
> Pyramid -heme; INDIDIIANALYST <1.5
> Aggregate Data
> SharCe
> LUrnOer
> FIMESs
> TCUTR
> UF3UoIn
> MarEin
> 2.70
> 9.55%
> 2.80
> 13.4596
> 5.549
> 28.189000


---

## 讨论与评论 (15)

### 评论 #1 (作者: MW39826, 时间: 2个月前)

GOOD

---

### 评论 #2 (作者: 顾问 RM49262 (Rank 30), 时间: 2个月前)

=====================================评论区====================================

感谢大佬分享模板思路！学到了很多

这就去试试看！

=============================================================================

---

### 评论 #3 (作者: XW25488, 时间: 2个月前)

感谢分享，请问“使用提示词，调用大模型的看家本领”这一步，老师你会开启thinking模式吗？

---

### 评论 #4 (作者: JZ76850, 时间: 2个月前)

感谢大佬的经验，字段极性配对这个思路之前从没有想过，现在S&F下我的USA点塔之路走的极为艰难。现在又多了个思路可以试一试。

====================================================================================

===============================加油加油加油=====================================

====================================================================================

---

### 评论 #5 (作者: YX50005, 时间: 2个月前)

谢谢主包分享！之前都是让大模型直接输出表达式，效果一直一般，原来还可以有这样的路径！给了我好大的启发呀！

---------------------If you come to the forum to study hard every day, you will get a GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------

---

### 评论 #6 (作者: XC66172, 时间: 2个月前)

感谢佬的分享~~ 大地区挖PC低的因子越来越难了 组合出新的字段来跑一阶确实可以实行一下

=======================================

fighting labubu

=======================================

---

### 评论 #7 (作者: 顾问 YH25030 (Rank 31), 时间: 2个月前)

差分的log比列没有想到过。谢谢大佬分享模板。不过SLOW_AND_FAST实在太慢了，有点熬人。

==================================================================================
Life is about waiting for the right moment to act. So, RELAX. You’re not LATE. You’re not EARLY.
You are very much ON TIME, and in your, TIME ZONE Destiny set up for you.
==================================================================================

---

### 评论 #8 (作者: 顾问 MZ45384 (Rank 51), 时间: 2个月前)

学到了，我这就去让我的Gemini试试这个prompt。大佬真的太有发掘力了。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

### 评论 #9 (作者: ST61360, 时间: 2个月前)

这个思路挺好，之前也偶尔想过，只是没有想到合适的提示词，感谢分享。

---

### 评论 #10 (作者: MY82844, 时间: 2个月前)

[XW25488](/hc/en-us/profiles/37083385366295-XW25488)  一般会开的，然后把 **temperature** 调低些，这样结果比较容易复现

===========================================================================

Pain + Reflection = Progress

===========================================================================

---

### 评论 #11 (作者: CZ39633, 时间: 2个月前)

====================================================================================  感谢大佬教我们怎么使用极性配对去构建出pc低的alpha                                                                                          ================================自信人生两百年，会当水击三千里==========================

---

### 评论 #12 (作者: MY82844, 时间: 2个月前)

[JZ76850](/hc/en-us/profiles/36590032309655-JZ76850)  同感，S&F跑起来确实慢，所以得想方设法跑些快的neutralization，出些RA来交

===========================================================================

Reflection + Pain + AI = Progress

===========================================================================

---

### 评论 #13 (作者: WL58980, 时间: 1个月前)

有了新的灵感，受益匪浅呀！！！感谢！！！

============================================================================

Study hard — quality over quantity, no room for mediocrity. Cherish every learning opportunity, stay focused, and learn from the experts. Keep pushing!

============================================================================

---

### 评论 #14 (作者: KB18445, 时间: 1个月前)

受益匪浅，感谢分享

---

### 评论 #15 (作者: LT33293, 时间: 1个月前)

学习了，感谢分享

---

