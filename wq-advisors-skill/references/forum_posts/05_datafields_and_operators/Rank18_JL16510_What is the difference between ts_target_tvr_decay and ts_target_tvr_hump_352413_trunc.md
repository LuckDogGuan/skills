# What is the difference between ts_target_tvr_decay and ts_target_tvr_hump?

- **链接**: https://support.worldquantbrain.comWhat is the difference between ts_target_tvr_decay and ts_target_tvr_hump_35241353069591.md
- **作者**: 顾问 JL16510 (Rank 18)
- **发布时间/热度**: 9个月前, 得票: 44

## 帖子正文

Hi,everyone.
I notice that everything is same in the description of ts_target_tvr_decay and ts_target_tvr_hump, except for the names after tune being different. It indicates that the usage of the two operators is quite similar, but there should still have some differences. I want to know what the subtle differences are.
Thank you.

---

## 讨论与评论 (1)

### 评论 #1 (作者: RK65765, 时间: 9个月前)

I think the main difference is in how they shape the turnover path. With  `ts_target_tvr_decay` , turnover tapers off smoothly over time, while  `ts_target_tvr_hump`  follows more of a bell-shaped curve where turnover builds up, peaks, and then falls. Both help control trading costs, but decay is more gradual, and hump is more concentrated in the middle.

---

