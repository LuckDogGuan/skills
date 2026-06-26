# iqc高效高分高收入实践

- **链接**: iqc高效高分高收入实践.md
- **作者**: 顾问 JX79797 (Rank 9)
- **发布时间/热度**: 1年前, 得票: 54

## 帖子正文

一、自相关校验

[../顾问 AY17279 (Rank 14)/[Commented] 从Gold跃升到GrandMaster选好模板和相关性剪枝可能是关键论坛精选.md](../顾问 AY17279 (Rank 14)/[Commented] 从Gold跃升到GrandMaster选好模板和相关性剪枝可能是关键论坛精选.md)

[../顾问 KZ79256 (Rank 21)/本地0误差计算自相关性【即插即用版】代码优化.md](../顾问 KZ79256 (Rank 21)/本地0误差计算自相关性【即插即用版】代码优化.md)

自相关性校验实现基于以上两篇帖子，本地因子自相关性校验去除相关度高的信号因子，提升10倍以上回测速度。 GM大佬是一个阶段运行完毕之后，统一去做因子自相关性校验，由于用户阶段算力有限，往往跑完一阶段需要半个月甚至更久，所以实现上更改为先到先入，增量检查更新的方式。

过程中存储已对比过的id，要跑下一阶段的id和pnls


> [!NOTE] [图片 OCR 识别内容]
> fundamentalG_usa_Istep_alpha_ids .pickle
> fundamentalG_usa_Istep_next_alpha_ids.pickle
> fundamentalG_usa_Istep_next_alpha_pnls. pickle


```
主要用于对新的 alpha 因子进行筛选和更新操作，具体步骤如下：1. 加载已有的 alpha 因子 ID 和对应的 PnL 数据。2. 从 fo_tracker 中提取新的 alpha 因子 ID。3. 遍历新的 alpha 因子 ID，计算每个因子与已有因子的自相关性。4. 根据自相关性和因子质量（通过 check_quality_better 函数判断）决定是将新因子添加到结果列表中，还是替换已有因子。5. 保存更新后的因子 ID 和 PnL 数据，并返回筛选后的因子列表。
```

二、因子结果获取

对执行完毕的tag因子，通过API获取因子数据、计算关键指标（如IQC分数、自相关性等），并根据设定的阈值筛选高价值因子，最终输出结果供后续分析使用。

```
主要逻辑如下：1. 因子数据获取与IQC分数计算2. 多线程并发处理与筛选3. 自相关性分析与结果输出4. 异常处理与状态管理,对分数低或自相关高的因子后续不在拉取 
```


> [!NOTE] [图片 OCR 识别内容]
> alpha_id, iqcscore, self_corr , sharpe , fitness, result , fieldKey , grade
> WY6Ix1d , 661,0.11,1.39,1.43 , Pass , "group_neutralize(trade_when(ts_arg_max(c
> 7GEE692,110,0.11,1.6,1.15 , Pass, "group_neutralize(trade_when (ts_corr (close
> OP8XjRV, 148,0.12,1.71,1.16 , Pass, "group_neutralize (trade_when (ts_corr(clos
> 19b0711,127,0.15,1.64,1.37 , Pass, "group_neutralize (trade_when (ts_mean(volu
> 2G8YeKY, 68,0.15,1.93,1.14, Pass,
> group_neutralize(trade_when (ts_corr (close
> p0v9q1a,-29,0.16,1.69,1.33 , Pass, "group_neutralize (trade_when (pcr_oi_ 270
> p0Yeb29,211,0.17,1.63,1.17 , Pass, "group_neutralize (trade_when (ts_corr(clos
> PPdN85q,175,0.18,1.54,1.18, Pass, "group_zscore (trade_when(ts_arg_min (volum
> ZAKnQbX, 127,0.18,1.89,1.12,Pass , "gpoup_scale (trade_when(ts_regression(ret
> lgbpdrn, 70,0.18,1.36,1.32, Pass, "group_neutralize (trade_when (pcr_oi 270
> VYwbe8a, 130,0.19,1.26,1.22, Pass, "group_neutralize (trade_when(pcr_oi_ 270
> 7GEW3X8,0,0.19,1.42,1.37,Pass, "group_neutralize (trade_when(ts_mean (volume
> NKVwbqg, 177,0.20,1.47,1.52, Pass, "group_neutralize (trade_when (pcr_oi_ 270
> KVL2Z02,109,0.21,1.44,1.68, Fail, "group_neutralize (trade_when(ts_regressio
> elJWrOM,151,0.23,1.79,1.52, Pass, "winsorize (ts_backfill(mdl77_earningsqual
> OP7L1el, 104,0.23,1.87,1.26 , Pass, "group_neutralize (trade_when(ts_arg_max(c
> 767.215,355,0.25,1.63,1.25 , Pass,
> group_zscore (trade_when(ts_std_dev(retur
> 86db922,375,0.27,1.67,2.01,Fail, "group_neutralize (trade_when (ts_corr (clos


三、高base因子筛选和手动调整

```
iqc score必须为正fitness和sharpe越高越好自相关低于0.2， 低于0.3等越低越好单日提交最好凑满4个跑出来的因子往往需要手动调整进一步获得更好的表现，weight和sub sharpe出错的因子也可以调整通过设置: decay, 截断因子表达式调整： ts_decay_linear， ts_mean, ts_sum, signed_power等综合使用
```

两个0.2以下excellent和两个0.3以下good，大概50刀水平

大家多点赞评论，过十在群里分享代码

---

## 讨论与评论 (14)

### 评论 #1 (作者: RW81345, 时间: 1年前)

学习到了

---

### 评论 #2 (作者: ZS91324, 时间: 1年前)

求代码分享

---

### 评论 #3 (作者: QZ28759, 时间: 1年前)

太强了，学习了！

---

### 评论 #4 (作者: SL52857, 时间: 1年前)

感谢大佬分享

---

### 评论 #5 (作者: PY58917, 时间: 1年前)

谢谢老板

---

### 评论 #6 (作者: LY63868, 时间: 1年前)

0.2以下的excellent，太强了。大佬可以再分享一下怎么找模板吗？

---

### 评论 #7 (作者: WT73952, 时间: 1年前)

这几天已经没有这样的收入了，40可能都够呛

---

### 评论 #8 (作者: JL37541, 时间: 1年前)

求代码分享

---

### 评论 #9 (作者: JS71074, 时间: 1年前)

求大佬代码分享

---

### 评论 #10 (作者: LX57490, 时间: 1年前)

本地自相关加速检测，检测iqc因子质量，还为我们这些新手告知iqc计算规则，感谢前辈分享

---

### 评论 #11 (作者: FF56620, 时间: 1年前)

感谢分享，但是最近iqc的收入真的感人

---

### 评论 #12 (作者: ZZ75629, 时间: 1年前)

太强啦！求代码分享

---

### 评论 #13 (作者: HW66800, 时间: 1年前)

赞了兄弟，求分享代码

---

### 评论 #14 (作者: AS92842, 时间: 2个月前)

感谢分享，新人急需，请问在哪个群分享代码？

---

