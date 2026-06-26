# Fetch datafield for level GOLD

- **链接**: https://support.worldquantbrain.comFetch datafield for level GOLD_35063006259607.md
- **作者**: 顾问 CT48231 (Rank 2)
- **发布时间/热度**: 9个月前, 得票: 5

## 帖子正文

May I ask for some clarification? When I use the API to pull datafields, I can only retrieve up to 10,000 fields. However, these datafields do not fully match the datasets I pulled. Does this mean that I am missing some of them? Thank you in advance, and I look forward to your guidance!

---

## 讨论与评论 (1)

### 评论 #1 (作者: LB76673, 时间: 9个月前)

The ACE API has a hard cap of 10,000 fields per call, so if a dataset contains more than that, you’ll only retrieve a subset. You’re not actually missing fields—they’re just paginated. To get the full set, you’ll need to use the  `offset`  parameter and pull data in multiple requests until you’ve covered all fields. That way, you can stitch them back together to match the dataset fully.

---

