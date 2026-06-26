# 【Alpha灵感】The Momentum of News

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】The Momentum of News_18641983716503.md
- **作者**: ML13205
- **发布时间/热度**: 2 years ago, 得票: 17

## 帖子正文

**概述：** 基于全面的新闻发布数据集，构建每周公司水平的新闻情绪得分，并记录了过去有更积极消息的股票新闻势头现象，未来产生更积极的消息。我们提出了三个假设来解释这一现象， **并发现新闻势头是由公司基本面的持续性驱动的，而不是陈旧的新闻或公司战略披露。将好消息五分之一投资组合中的多头头寸与坏消息投资组合中的空头头寸相结合的交易策略** ，每年产生7.45%的风险调整回报率。这种返回异常现象同时出现在新闻日和非新闻日。总的来说，这些发现表明，投资者对新闻的横断面预测并没有完全纳入股价中。这种新闻驱动的回报可预测性只有在短期内和信息环境较差的股票中才很重要，比如那些公司规模较小、分析师覆盖率较低、机构持股量较少的股票。这一发现与对回报可预测性的错误定价观点相一致。

- **Alpha 思路: 初步的alpha 表达式
  （将月交易转为日交易）**

STEP1:每1日根据5日内的新闻情绪得分将所有股票分为10个投资组合。

STEP2:计算每个投资组合中所有公司从当前和未来几个月的平均加权平均新闻得分。

在t日发布最负面信息（低于10百分位）的十分之一被称为坏消息投资组合，

在t日发布最正面信息（高于90百分位）的十分之一被称为好消息投资组合。

SREP3:然后我们持有好消息投资组合，卖出坏消息投资组合

a=ts_mean(scl12_sentiment,5);

b=normalize(group_rank(a,densify(subindustry)));

c_1=group_percentage(a,densify(subindustry),percentage=0.9);

c_2=group_percentage(a,densify(subindustry),percentage=0.1);

c_0=if_else(or(a<c_1,a>c_2),b,0);

trade_when(and(vec_avg(nws18_relevance)>0.1,adv20>1),c_0,-1)

**2、Alpha 表现:**

**
> [!NOTE] [图片 OCR 识别内容]
> GOOK
> 40OK
> 2OOK
> -2OOK
> Jul '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> :
> Mhj
**

**3、相关数据集:**

1)relevance——nws18_relevance

2)News Sentiment score——scl12_sentiment——from Sentiment Data

3)News Score——rp_css_assets——form ravenpack

**4、反思与改进**  **:** 
月交易交易频率低，若类比为为日交易，则换手率turnover较高，难降低

---

## 讨论与评论 (4)

### 评论 #1 (作者: KJ42842, 时间: 2 years ago)

可以分享下论文标题和作者吗？想仔细读下，谢谢。

---

### 评论 #2 (作者: ML13205, 时间: 2 years ago)

在worldquant brain平台community的research papers for users的Research 1

Author: Ying Wang, Bohui Zhang, Xiaoneng Zhu

Year : 2018

Link:  [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3267337](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3267337)

---

### 评论 #3 (作者: JW52708, 时间: 2 years ago)

应该是这篇

[https://support.worldquantbrain.com/hc/en-us/community/posts/13954113156503-Research-paper-1-The-Momentum-of-News](https://support.worldquantbrain.com/hc/en-us/community/posts/13954113156503-Research-paper-1-The-Momentum-of-News)

---

### 评论 #4 (作者: KJ42842, 时间: 2 years ago)

好的，感谢分享  [ML13205](/hc/en-us/profiles/16858128944023-ML13205)   [JW52708](/hc/en-us/profiles/13722825555991-JW52708)

---

