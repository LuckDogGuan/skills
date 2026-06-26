# 顾问 BL59154 (Rank 74) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 BL59154 (Rank 74) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: Step 5: 计算中性化结果)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Operator大师-用基础的operator实现复杂功能_29085671898775.md
- **时间**: 10个月前

**提问/主帖背景 (WL13229)**:
集思广益，在目前自己已有的operator权限下，提出组合的尝试，延申目前已有operator的边界。评论请附上用例. [运算符和函数手册中文版 – WorldQuant BRAIN](/hc/en-us/community/posts/32340683206423-%E8%BF%90%E7%AE%97%E7%AC%A6%E5%92%8C%E5%87%BD%E6%95%B0%E6%89%8B%E5%86%8C%E4%B8%AD%E6%96%87%E7%89%88)

例如

group_zscore

```
group_zscore = (alpha - group_mean(alpha, market)) / group_std_dev(alpha, market)
```

有的人没有std,可以

```
group_zscore = (alpha - group_mean(alpha, market)) / power(power(alpha - group_mean(alpha, market), 2), 0.5)
```

**顾问 BL59154 (Rank 74) 的解答与建议**:
ts_min可以用以下表达式替代：（ts_max同理）

```
ts_min({datafield}, {days}) = ts_backfill(if_else(ts_arg_min({datafield}, {days})==0, {datafield}, nan), 120)
```


---
