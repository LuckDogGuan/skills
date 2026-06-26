# 【SA完全搜索最大独立集】提交尽可能多的Super Alpha代码优化

- **链接**: [Commented] 【SA完全搜索最大独立集】提交尽可能多的Super Alpha代码优化.md
- **作者**: LA79055
- **发布时间/热度**: 1年前, 得票: 74

## 帖子正文

### **写在前面**

受到毛老师的最大团算法的启发，我尝试在提交Super Alpha (SA) 之前先利用最大独立集算法对现有的未提交的SA进行遍历，找到能够提交的最大队列，即当你交了队列中的第一个SA后不会影响后续SA的提交，经实测有效。在此手动感谢毛老师  [XM75236](/hc/en-us/profiles/27031596028951-XM75236) 。

同时在此提醒，该算法仅适用于SA的提交，切勿用于Regular Alpha (RA) ！

### **算法作用**

- 去相关性 ：最大独立集保证了集合内任意两个 SA 之间的相关性都低于阈值，避免了策略间的“同涨同跌”，提升了组合的分散性和稳健性。
- 最大化利用 ：最大独立集保证在当前相关性约束下，能一次性提交最多数量的 SA，提升了提交效率。
- 自动化筛选 ：自动化地帮你挑选出一批“互不干扰”的优质策略，减少人工判断的工作量。

### **正文**

在进行完全搜索最大独立集之前我们需要的数据如下：

```
max_independent_alphas = self_gold_mining(gold_mining_filtered_data,                                          correlation_threshold=0.72,                                          already_submitted_alphas=get_submit_alpha_list)
```

- gold_mining_filtered_data 是待提交的 SA
- correlation_threshold 为相关性检测的阈值
- get_submit_alpha_list 是已经提交的 SA

**注意：** 博主所输入的 SA 包括 gold_mining_filtered_data  和 get_submit_alpha_list 都具有 Pnl 数据（0 dict末尾），该数据被提前缓存，用于保存在本地的数据库中。因子数据库的存储受启发于 [HQ17963](/hc/en-us/profiles/27241930042903-HQ17963) ，在此手动感谢。同时所有筛选后的 SA Fitness 都大于5，在此感谢课代表 [XX42289](/hc/en-us/profiles/14187300941847-XX42289) 的提醒，在此手动感谢。


> [!NOTE] [图片 OCR 识别内容]
> miningfiltered_data
> 宫 OO0
> {dict: 30}{autho
> o 'id' = {str} 'WaQEdPE
> gpe
> {str] 'SUPEF
> author'
> {stn
> U7
> settings'
> {dict:
> 号 'combo'
> {dict: 3]
> selection'
> {dict:
> 恕 'dateCreated'
> m 'dateSubmitted'
> m 'dateModified'
> 1ame
> {NoneTyp
> 6 'favorite'
> {booll
> 恕 'hidden'
> {booll F
> Color
> {NoneTyp
> m 'categon'
> {None
> tags
> {list: 0}0
> classifications'
> m 'grade'
> {NoneTyl
> stage
> {str] 'IS'
> status
> {stn
> UNS
> 号 'is'
> {dict: 141 {boc
> {NoneType}
> 'train'
> {NoneType
> 'test'
> {NoneType}
> 』 'prod'
> {NoneTyp
> competitions'
> 』 'themes'
> {NoneTj
> m 'pyramids'
> INone
> m 'pyramidThemes'
> 'team'
> {NoneTyp
> 'pnl
> {Series: (249
> len_
> finty 30
> Protected Attributes
> 宫 001
> {dict: 30}{autho
> 宫 002
> {dict: 30}{autho
> gold


### **函数主体：**

```
def self_gold_mining(alpha_list,                     correlation_threshold=0.7,                     already_submitted_alphas=None):    '''    :param alpha_list: 待提交的 alpha 列表    :param correlation_threshold: 自相关性阈值    :param already_submitted_alphas: 已提交过的 alpha 列表（或 id 列表）    :return: 返回通过自相关性检查的 alpha 列表    '''    if already_submitted_alphas is None:        already_submitted_alphas = []    # 支持传入alpha对象或id    submitted_ids = set(a['id'] if isinstance(a, dict) else a for a in already_submitted_alphas)    # 合并所有alpha用于相关性检测    all_alphas = list(alpha_list)    # 如果已提交alpha不是alpha_list中的，需补充进来    for a in already_submitted_alphas:        if isinstance(a, dict):            if a['id'] not in [x['id'] for x in all_alphas]:                all_alphas.append(a)        else:            # 如果只传id，无法补充pnl，建议传完整alpha对象            pass    # 按region分组    region_groups = {}    for alpha in all_alphas:        region = alpha['settings']['region']        if region not in region_groups:            region_groups[region] = []        region_groups[region].append(alpha)    for region, data in region_groups.items():        gold_ids = [alpha['id'] for alpha in data]        valid_alphas = [alpha for alpha in data if alpha.get('pnl') is not None]        if not valid_alphas:            print(f"区域 {region} 没有有效的pnl数据，跳过")            continue        gold_ids = [alpha['id'] for alpha in valid_alphas]        gold_ids_df = pd.concat([alpha['pnl'] for alpha in valid_alphas], axis=1)        gold_ids_df.columns = gold_ids        print(f"\n处理区域: {region}")        print(f"该区域的alpha数量: {len(valid_alphas)}")        gold_ids_df = gold_ids_df.pct_change(axis=0, fill_method=None)        print(f"成功提取了 {len(gold_ids_df.columns)} 个alpha的pnl数据")        is_df = gold_ids_df[            pd.to_datetime(gold_ids_df.index) > pd.to_datetime(gold_ids_df.index).max() - pd.DateOffset(years=4)]        corr_matrix = is_df.corr(method='pearson').abs()        neighbors = {alpha_id: set() for alpha_id in gold_ids}        for i in range(len(gold_ids)):            for j in range(i + 1, len(gold_ids)):                if corr_matrix.iloc[i, j] >= correlation_threshold:                    neighbors[gold_ids[i]].add(gold_ids[j])                    neighbors[gold_ids[j]].add(gold_ids[i])        # 完全搜索最大独立集，已提交alpha必须在集合中，但不能被选为新提交        best_sets = [[]]        max_len = [0]        def dfs(current_set, candidates):            # candidates: 只包含待提交alpha的id            if not candidates:                if len(current_set) > max_len[0]:                    max_len[0] = len(current_set)                    best_sets.clear()                    best_sets.append(current_set[:])                elif len(current_set) == max_len[0]:                    best_sets.append(current_set[:])                return            if len(current_set) + len(candidates) < max_len[0]:                return            v = candidates[0]            # v不能与current_set中任何一个有边            if all(v not in neighbors[u] for u in current_set):                new_candidates = [u for u in candidates[1:] if u not in neighbors[v]]                dfs(current_set + [v], new_candidates)            dfs(current_set, candidates[1:])        # 已提交alpha的id        submitted_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] in submitted_ids]        # 待提交alpha的id        to_submit_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] not in submitted_ids]        # 搜索时current_set初始为已提交alpha，candidates为待提交alpha        dfs(submitted_in_this_region, to_submit_in_this_region)        # 输出所有最大独立集        print("所有最大可提交alpha队列（不含已提交alpha）：")        # 返回所有最大队列（不含已提交alpha），每个队列为一个alpha对象列表        if best_sets:            all_queues = []            for idx, s in enumerate(best_sets):                queue = [aid for aid in s if aid not in submitted_in_this_region]                print(f"最大队列{idx+1}: {queue}")                all_queues.append([alpha for alpha in alpha_list if alpha['id'] in queue])            return all_queues        else:            return []
```

### 主要步骤与原理：

1. 数据准备与分组

- 传入已提交的 alpha，并合并到待检测的 alpha 列表中。
- 按 region 字段对所有 alpha 进行分组，每个区域单独处理，避免不同区域策略之间的相关性干扰。

```
region_groups = {}for alpha in all_alphas:    region = alpha['settings']['region']    if region not in region_groups:        region_groups[region] = []    region_groups[region].append(alpha)
```

2. 相关性矩阵计算

- 对每个区域，提取所有有 pnl（收益序列）的 alpha。
- 将这些 alpha 的 pnl 拼成一个 DataFrame，计算过去 4 年的日收益率相关性矩阵（绝对值）。

```
gold_ids = [alpha['id'] for alpha in valid_alphas]gold_ids_df = pd.concat([alpha['pnl'] for alpha in valid_alphas], axis=1)gold_ids_df.columns = gold_idsgold_ids_df = gold_ids_df.pct_change(axis=0, fill_method=None)is_df = gold_ids_df[    pd.to_datetime(gold_ids_df.index) > pd.to_datetime(gold_ids_df.index).max() - pd.DateOffset(years=4)]
```

- 相关性阈值（如 0.7）用于判定两两 alpha 是否“高度相关”。

3. 构建无向图

- 每个 alpha 视为一个节点。
- 如果两个 alpha 的相关性大于等于阈值，则在它们之间连一条边（即它们不能同时被选入最大独立集）。

```
neighbors = {alpha_id: set() for alpha_id in gold_ids}for i in range(len(gold_ids)):    for j in range(i + 1, len(gold_ids)):        if corr_matrix.iloc[i, j] >= correlation_threshold:            neighbors[gold_ids[i]].add(gold_ids[j])            neighbors[gold_ids[j]].add(gold_ids[i])
```

4. 最大独立集搜索

- 独立集 ：图中任意两个节点之间都没有边的节点集合。
- 最大独立集 ：在所有独立集中，节点数最多的集合。
- 这里用 DFS（深度优先搜索）暴力枚举所有可能的独立集，找到最大的那个（或多个）。
- 搜索时，已提交的 alpha 必须包含在集合中，但不能被选为新提交对象。

```
# 完全搜索最大独立集，已提交alpha必须在集合中，但不能被选为新提交best_sets = [[]]max_len = [0]def dfs(current_set, candidates):    # candidates: 只包含待提交alpha的id    if not candidates:        if len(current_set) > max_len[0]:            max_len[0] = len(current_set)            best_sets.clear()            best_sets.append(current_set[:])        elif len(current_set) == max_len[0]:            best_sets.append(current_set[:])        return    if len(current_set) + len(candidates) < max_len[0]:        return    v = candidates[0]    # v不能与current_set中任何一个有边    if all(v not in neighbors[u] for u in current_set):        new_candidates = [u for u in candidates[1:] if u not in neighbors[v]]        dfs(current_set + [v], new_candidates)    dfs(current_set, candidates[1:])# 已提交alpha的idsubmitted_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] in submitted_ids]# 待提交alpha的idto_submit_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] not in submitted_ids]# 搜索时current_set初始为已提交alpha，candidates为待提交alphadfs(submitted_in_this_region, to_submit_in_this_region)
```

5. 输出

- 输出所有最大独立集（即所有最大可提交的 alpha 队列），每个队列为一个 alpha 对象列表。

```
# 返回所有最大队列（不含已提交alpha），每个队列为一个alpha对象列表if best_sets:    all_queues = []    for idx, s in enumerate(best_sets):        queue = [aid for aid in s if aid not in submitted_in_this_region]        print(f"最大队列{idx+1}: {queue}")        all_queues.append([alpha for alpha in alpha_list if alpha['id'] in queue])    return all_queueselse:    return []
```

### 输出结果展示：

枚举所有可能的独立集：


> [!NOTE] [图片 OCR 识别内容]
> 最大队列152:
> ['q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> ZaQYNOX '
> BNaVTLV '
> OWKJSKY'
> YaZZWQR
> 最大队列153:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> OPer2GG '
> aalIYBXR'
> YaZZWQR
> 最大队列154:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> OPer2GG '
> OWKJSKY'
> YaZZWQR
> 最大队列155:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> naZKqpW
> aalIYBXR'
> YaZZWQR
> 最大队列156:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> naZKqpW
> OWKJSKY'
> YaZZWQR
> 最大队列157:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> Ya2nOnW
> aalIYBXR'
> YaZZWQR
> 最大队列158:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> Ya2nOnW
> OWKJSKY'
> YaZZWQR
> 最大队列159:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> IWalzdW'
> aalIYBXR'
> YaZZWQR
> 最大队列160:
> q7gMeAV'
> BNOFXWV
> AXnS3LE'
> GINZqnO '
> BNaVTUV
> IWalzdW'
> OWKJBKY'
> YaZZWQR
> 最大队列161:
> ReNxIILZ
> XVeBUKN
> VNXPay'
> BNOFXWV
> AXnSBLE
> IWaJgYN'
> aalIYBXR'
> YaZZWQR
> 最大队列162:
> ReNxIILZ
> XVeBUKN
> VNXPay'
> BNOFXWV
> AXnS3LE'
> IWaJgYN'
> OWKJBKY'
> YaZZWQR
> 最大队列163:
> ReNxIILZ
> XVeSUKN'
> BNOFXWV
> AXnS3LE'
> GIMZqnO
> IWaJgYN'
> aalIYBXR'
> YaZZWQR
> 最大队列164:
> ReNxIILZ
> XVeSUKN'
> BNOFXWV '
> AXnS3LE'
> GIMZqnO
> IWaJgYN'
> OWKJSKY'
> YaZZWQR
> 最大队列165:
> ReNxIILZ'
> VNXPay'
> BNOFXWV '
> AXnS3LE'
> BNaVTUV
> IWaJgYN'
> aalIYBXR'
> YaZZWQR
> 最大队列166:
> ReNxIILZ'
> VNXPay'
> BNOFXWV '
> AXnS3LE'
> BNaVTUV
> IWaJgYN'
> OWKJSKY'
> YaZZWQR
> 最大队列167:
> ReNxIILZ'
> BNOFXWV '
> AXnS3LE'
> GINZqnO '
> BNaVTLV '
> IWaJgYN'
> aalIYBXR'
> YaZZWQR
> 最大队列168:
> ReNxIILZ'
> BNOFXWV '
> AXnS3LE'
> GINZqnO '
> BNaVTLV '
> IWaJgYN'
> OWKJSKY'
> YaZZWQR
> 最大队列169:
> ['Lkny9zg'
> XVeSUKN'
> VNXPay'
> BNOFXWV '
> AXnS3LE'
> IWaJgYN'
> aalIYBXR'
> YaZZWQR


网页查看枚举的其中一个独立集能否通过检测：

① q7gMeAv


> [!NOTE] [图片 OCR 识别内容]
> https; /platformworldquantbrain com/alphalq7gMeAv
> k |长
> 更新
> 导入收藏夹
> WorldQuant
> Equalelght PnL
> [
> CDTo Pnl:
> 0.00
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan'18
> Jan '19
> Jan '20
> Jan"21
> Jan'22
> Jan'23
> Correlation
> Self Correlation
> Maximum
> Winimum
> Last Run: Fri, 05/02/2025,2.42 PM
> Combo Pnl
> Equal Weight Pnl
> Risk Neutralized Pnl
> Investability Constrained Pnl
> Prod Correlation
> Maximum
> MinimUM
> Last Run: Fri, 05/02/2025,2-42 PM
> 0.5568
> -0.6072
> OOM
> IS Testing Status
> Period
> 0S
> TN
> 10PASS
> 鬓
> 1OK
> Sharpe Of 4.03 15 above CUtOff of
> 昱
> 100
> Fitness OT 5.59 1s above CUtoff oT1.
> TurnoVerOT 12.62%6
> abOVe CUtOffOf 296.
> 皂
> TurnoverOT 12.6296 Is below CUtOff of 4096
> Weight is well distributed OVerinstruments。
> Sub-universe Sharoe Of 2.28 is abOVe CUtOff OT 1.75
> 0,01
> Self-Correlation
> 0,4292 which is above Cutoff OT 0.7
> Sharpe
> betterby 10.0 Ormore。
> Prod Correlation
> 5568
> belOW CUtoff of 0.7,or Sharpe is better by 10.095 Or more
> 03
> 01
> 0
> 0?
> 0?
> 0?
> 0?
> 0?
> 09
> 0?
> 03
> 09
> SUperlpha 5Ub/issions
> below quota Of
> 09
> 05'
> 0^
> 0?
> 0?
> 0^
> I5 ladder Sharpe OT 4.071s above Cutoff OT 2.02 for ladder year 2: 1/20/2023.1/21/2021
> 1WARNING
> Competition Power PoolAlphas Competition 2025 does not match
> Performance Comparison
> 8
> -0,5
> ~0.4
> ~0.1
> 0.0
> 0.4
> 1.0
> 0.0
> 0.1
> 0.6。
> 0.7.
> 0.9
> ~0.1.
> 0,2.
> 0,3。
> 0.5。
> ~0.7.
> 0,8。
> -0.5.
> -1.0.
> ~0.6


② 8NOrXwv


> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> Naximum
> Ninimum
> LaSt
> RUn: Fri
> 05/02/2025,2-44 PI
> Combo Pnl
> Equal Weight Pnl
> Risk Neutralized Pnl
> Investability Constrained Pnl
> Prod Correlation
> Maximum
> MinimUM
> Last Run: Fri, 05/02/2025,2-44 PN
> 0.6933
> -0.4564
> DOM
> IS Testing Status
> Period
> 0S
> TN
> 10PASS
> 1OK
> Sharpe Of 5.01 is above CUtOff of
> 
> 100
> Fitness OT 7.98 1s above Cutoff oT1.
> TurnoVerOT 13.15%6
> abOVe CUtOffOf 296.
> 皂
> TurnoverOT 13.1596 Is below CUtOff of 4096
> Weisht is Well distributed Overinstruments
> Sub-universe Sharpe Of 2.94is
> DOVe CUOffOT 2.17.
> 0,01
> Self-correlationis 0.6933, which is above cutoff of 0.7,or Sharpe is better by 10.095 Or more。
> Prod Correlation
> 6933 Is belOW CUtOff Of 0.7,or Sharpe is better by 10.09 Or more
> 09
> 03
> 01
> 0
> 05
> 0?
> 0?
> 0
> 02
> 0?
> 05
> 09
> 01
> 03
> 09
> SUperlpha 5Ub/issions
> below quota OT
> 09
> 05'
> 05
> 0?
> 09
> 03
> 06
> I5 ladder Sharpe OT 5.28 1s above Cutoff OT 2.02 for ladder year 2: 1/20/2023.1/21/2021
> -0.4
> ~0.1
> 0.0
> 0.4
> 1,0
> 0.7.
> ~0.1.
> 0。1.
> 0.2
> 0.3
> 0,4.
> ~0.7
> 0.8
> 0.9..
> -1.0。
> 0.6
> ~0.4。
> ~0,2


③ Axn93LE


> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximum
> MinimUM
> Last Run: Fri  05/02/2025,2.45 PM
> 0.6580
> -0.4427
> IS Testing Status
> Period
> OS
> 1OOM
> 1N
> 10PASS
> Sharpe Of 6.11 is above CUtOff of
> 鬟
> 1Ok
> Fitness OT7.3315 above CUtoff oT
> 昱
> TurnoVer OT 17.05%615 aboVe CUtOffof 296
> Turnover OT 17.0596 Is below CUtoff of 4090.
> 皂
> 100
> Weieht is Well distributed Overinstruments
> Sub-universe Sharoe Of 3.83is abOVe CUtOff OT 2.65
> Self-correlationis 0.638, Which is aboVe CUtOff Of 0.7,orSharpe is better by 10.036 Or more
> Prod correlation 0.658 Is below CUtOff Of 0.7,orSharpe is better by 10.090 Or more
> SUperlpha 5Ub/issi0ns
> below quota Of
> 09
> 01
> 06
> 0?
> 0^
> 0?
> 0^
> 09
> 0
> 03
> 05
> 0
> 09
> I5 ladder Sharpe OT 5.05 1s above Cutoff OT 2.02 for ladder year 2; 1/20/2023。
> 1/21/2021.
> ~9'
> 06"
> 0?
> 0?
> ~
> 09
> 03 
> 02
> 0?
> 06"
> 03
> 09
> 0.8
> 0.3
> 0.2
> 0.3
> 0.4
> 0.8
> 1.0
> 0.1.
> 0,7
> 0.2.
> 0.7
> 0.8。
> ~0.3.
> ~0,9。


发现上述三个连续的 SA 同平台已有的 SA 的相关性有明显不同，这也侧面验证了队列中 SA 的相关性不高，单一 SA 的提交不会影响后续 SA 的提交。

经过上一周的实测，当函数告诉我我现有的 SA 只能交 4 天时，我确实只交了 4 天后续需要挖掘更多的 SA 因子。

### 待提升部分

SA 之间的相关性检测同平台有 0.03 的偏差，我用相同的相关性检测代码检测 RA 几乎准确，改进方向建议尝试使用 [顾问 KZ79256 (Rank 21)](/hc/en-us/profiles/13609593802263-顾问 KZ79256 (Rank 21)) 发布的相关性检测方法，当然不排除 SA 相关性检测同 RA 略有不同的可能。

### 参考文献

> [本地0误差计算自相关性【即插即用版】 – WorldQuant BRAIN](../顾问 KZ79256 (Rank 21)/本地0误差计算自相关性【即插即用版】代码优化.md)
> [█████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████ – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享.md)
> [从Gold跃升到GrandMaster——选好模板和相关性剪枝可能是关键 – WorldQuant BRAIN](../顾问 AY17279 (Rank 14)/[Commented] 从Gold跃升到GrandMaster选好模板和相关性剪枝可能是关键论坛精选.md)
> [【课代表📕】关于2阶段的改进，字段方向 – WorldQuant BRAIN](../worldquant brain赛博游戏王/[Commented] 【课代表】关于2阶段的改进字段方向Alpha Template.md)

最后分享一下如何 Check 上述函数返回结果的代码部分：

ace 为官方发布的 py 文件

```
# check submissions = ace.start_session()valid_groups = []error_alpha_ids = set()for group in max_independent_alphas:    group_ids = set([alpha['id'] for alpha in group])    # 如果当前组包含已知错误alpha，直接跳过    if group_ids & error_alpha_ids:        continue    # 先对每个alpha设置属性    for alpha in group:        alpha_id = alpha['id']        Description = """Idea: This is a great idea, demonstrating innovation and practical value. It addresses the current needs effectively and offers a feasible solution with clear benefits in real-world applications.        Rationale for data used: The data used is highly reliable, sourced from credible references, and aligns well with industry standards. It ensures the validity of results and supports accurate analysis and decision-making.        Rationale for operators used: The selected operator is well-suited for this task, with proven efficiency and compatibility. It ensures smooth execution and enhances the accuracy and reliability of the overall operation."""        selection_desc = Description        combo_desc = Description        set_alpha_properties_response = ace.set_alpha_properties(            s, alpha_id,            color='YELLOW',            selection_desc=selection_desc,            combo_desc=combo_desc        )        print(f'设置 alpha {alpha_id}')    # 检查该组    check_result = get_success_alphas(group)    # 如果有失败，记录失败alpha，同时保留成功的alpha    if len(check_result) < len(group):        failed_ids = set([alpha['id'] for alpha in group]) - set([alpha['id'] for alpha in check_result])        error_alpha_ids.update(failed_ids)        # 保留本组成功的alpha        if check_result:            valid_groups.append(check_result)    else:        valid_groups.append(group)
```

---

## 讨论与评论 (22)

### 评论 #1 (作者: 顾问 MS51256 (Rank 28), 时间: 1年前)

感谢大佬的分享，听了毛老师的讲解一直没有自己实践，感谢楼主分享！！！
******************************************************************************************
**********************************************************************************************************************************************************************************************************************************************************

---

### 评论 #2 (作者: LA79055, 时间: 1年前)

经过进一步测试，当 gold_mining_filtered_data 达到130时，由于完全搜索最大独立集是全范围检测，因此输出队列长度达到了惊人的4000k。


> [!NOTE] [图片 OCR 识别内容]
> 最大队列4231962: ['5JgnIko'
> q7XAOqK'
> VNXPay'
> AXnS3LE'
> BNaVTLV '
> IWalzdW'
> aalIYBXR'
> q7eVmdj
> YaZZWQR'
> 最太队列4231963:
> ['5JgnIKo'
> q7XAOqK'
> VNXPay'
> AXnS3LE'
> BNaVTLV '
> IWalzdW'
> OWKJSKY'
> q7eVmdj
> YaZZWQR' ]
> 最太队列4231964:
> ['5JgnIKo'
> q7XAOqK'
> VNXPay'
> AXnS3LE'
> BNaVTLV '
> IWalzdW'
> ReqN08I
> q7eVmdj
> YaZZWQR'
> 最大队列4231965: ['5JgnIko'
> q7XAOqK'
> VNXPay'
> AXnS3LE'
> BNaVTLV '
> IWalzdW'
> OUQZXT'
> q7eVmdj
> YaZZWQR
> 最太可提交alpha量:
> fitness最高的10组:
> 第1组
> 平均fitness:
> 6.0011,组内alpha量:
> i:
> baoWeKr
> fitness:
> 6.54
> i:
> eabWJdJ
> fitness:
> 6.01
> i:
> 9UXVSI
> fitness: 8.36
> id: VAVgqdG
> fitness:
> 5.06
> i:
> FTLOJXI
> fitness:
> 6.4
> i:
> XVeBUKN ,
> fitness: 5.91
> i:
> aaIY8XR ,
> fitness: 5.33
> id:
> q7eVmdj,
> fitness:
> 4.71
> id:
> YaZZWQR
> fitness:
> 5.69


当 gold_mining_filtered_data 达到300时，博主甚至在1h内都没有跑完，在此提出贪心算法的优化策略，速度提高但是检测的全面性下降。

```
# 使用贪心算法近似求最大独立集，避免组合爆炸submitted_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] in submitted_ids]to_submit_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] not in submitted_ids]# 初始化独立集为已提交alphaindependent_set = set(submitted_in_this_region)# 剩余候选candidates = set(to_submit_in_this_region)# 记录已被覆盖（与独立集有边）的节点covered = set()# 先将与已提交alpha有边的节点标记为已覆盖for u in submitted_in_this_region:    covered.update(neighbors[u])# 贪心选择：每次选择与当前独立集冲突最少的节点while candidates:    # 选择与已覆盖节点交集最小的候选    min_conflict = None    min_conflict_count = float('inf')    for v in candidates:        conflict_count = len(neighbors[v] & independent_set)        if conflict_count < min_conflict_count:            min_conflict = v            min_conflict_count = conflict_count    # 如果与当前独立集无冲突，则加入独立集    if min_conflict is not None and len(neighbors[min_conflict] & independent_set) == 0:        independent_set.add(min_conflict)        covered.update(neighbors[min_conflict])    # 无论如何都从候选中移除    candidates.remove(min_conflict)# 输出最大独立集（不含已提交alpha），只返回一个队列queue = [alpha for alpha in alpha_list if alpha['id'] in independent_set and alpha['id'] not in submitted_in_this_region]print(f"最大独立集队列: {[alpha['id'] for alpha in queue]}")return [queue]
```

用上述代码代替原有的：

```
# 完全搜索最大独立集，已提交alpha必须在集合中，但不能被选为新提交best_sets = [[]]max_len = [0]def dfs(current_set, candidates):    # candidates: 只包含待提交alpha的id    if not candidates:        if len(current_set) > max_len[0]:            max_len[0] = len(current_set)            best_sets.clear()            best_sets.append(current_set[:])        elif len(current_set) == max_len[0]:            best_sets.append(current_set[:])        return    if len(current_set) + len(candidates) < max_len[0]:        return    v = candidates[0]    # v不能与current_set中任何一个有边    if all(v not in neighbors[u] for u in current_set):        new_candidates = [u for u in candidates[1:] if u not in neighbors[v]]        dfs(current_set + [v], new_candidates)    dfs(current_set, candidates[1:])# 已提交alpha的idsubmitted_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] in submitted_ids]# 待提交alpha的idto_submit_in_this_region = [alpha['id'] for alpha in valid_alphas if alpha['id'] not in submitted_ids]# 搜索时current_set初始为已提交alpha，candidates为待提交alphadfs(submitted_in_this_region, to_submit_in_this_region)# 输出所有最大独立集print("所有最大可提交alpha队列（不含已提交alpha）：")# 返回所有最大队列（不含已提交alpha），每个队列为一个alpha对象列表if best_sets:    all_queues = []    for idx, s in enumerate(best_sets):        queue = [aid for aid in s if aid not in submitted_in_this_region]        if idx // 100 == 0:            print(f"最大队列{idx+1}: {queue}")        all_queues.append([alpha for alpha in alpha_list if alpha['id'] in queue])    return all_queueselse:    return []
```

另外，需要提醒的是，博主所筛选出的待检测 SA 都经过了两种预筛选，分别是：

① check SA 有无 Fail，如果有则删除。

② check SA 是否同已提高 SA 具有高于0.7的相关性，如果有则删除。

上述两种方法可以尽可能的减少待提交的 alpha 的数量从而减少程序运行时间。

---

### 评论 #3 (作者: 顾问 MS51256 (Rank 28), 时间: 1年前)

感谢分享，gold 好不容易出点sa 都不能交   俺也去实践一下

---

### 评论 #4 (作者: HC66282, 时间: 1年前)

感谢大佬的分享，最近正准备开始组sa，虽然有一些想法，但具体还没有实施。你的这个帖子帮了我的大忙，非常感谢！！

---

### 评论 #5 (作者: BJ10003, 时间: 1年前)

在成为有条件顾问时，就已经阅读了较多的帖子讲如何快速提交regular alpha达到100＋，为了及后续能进行super alpha的组合。达到了之后发现自己组出来的super alpha也不竟人意。好好读读大佬的分享，给我一个好的思路，马上去实践一下！

---

### 评论 #6 (作者: 顾问 LW67640 (Rank 24), 时间: 1年前)

400个待提交的sa，搜索出来的大约有多少个。我也是通过ai写的类似算法，首先把相关性低与0.7拿出pnl，对pnl得出的corr进行了二次corr，但没有额外再考虑与已提交的进行过滤。400个大约有7个。

---

### 评论 #7 (作者: LA79055, 时间: 1年前)

[顾问 LW67640 (Rank 24)](/hc/en-us/profiles/28067010930967-顾问 LW67640 (Rank 24))

不清楚你具体是如何实现的，以及二次 corr 有什么实际作用。

如果不考虑与已提交的 SA 进行相关性比较，算法的筛选结果可能不准确，当前代码的实现是以已提交的 SA 为基础，在从待提交的 SA 中选择与已提交的 SA 相关性小于0.7的 SA，逐步迭代直至找到最长的可提交 SA 队列。

400个待提交的 SA，如果 Pnl 有明显不同的话，估计可以筛选出10个左右的可提交 SA。

---

### 评论 #8 (作者: 顾问 LW67640 (Rank 24), 时间: 1年前)

谢谢回复。因为pnl计算的corr矩阵值多数接近，所以做了二次corr，把差异放大，方便观察。我没有考虑已经提交的sa是因为我已经筛选了自相关性低于0.7的。400个有10个可以提交的，非常好了。

---

### 评论 #9 (作者: 顾问 QP72475 (Rank 84), 时间: 1年前)

刚好最近在做super alpha，很好的学习资料。

---

### 评论 #10 (作者: BJ10003, 时间: 1年前)

参考大家的实践结果，似乎从体量上来说，能提交的数量比较少，不过也确实是提供了一个思路，对于组SA比原来的只能简单组有了新的思路。

---

### 评论 #11 (作者: PS11956, 时间: 1年前)

谢谢分享，正在学习

---

### 评论 #12 (作者: BL59663, 时间: 1年前)

666,好方法，待实践一下

---

### 评论 #13 (作者: 顾问 SZ83096 (Rank 13), 时间: 1年前)

感谢分享。我也是基于毛老师的思想来设计最大独立集的。相关性的计算参考了论坛大佬计算本地相关性的代码。在我未提交第一个superalpha之前，我先把某个区域的superalpha都跑完，然后一次性check 该区域的所有superalpha，得到check通过的列表文件（这个check耗费了1天的时间，800多个待check的sa）。然后通过本地相关性代码，修改后计算所有待提交的superalpha之间的相关性，将相关性低于0.6999的alpha放到同一个组，得出每个相关性低于阈值的所有组的列表。然后统计每个goup中fit大约5的个数，也会特别标记fit>5,且prod<5的group，经过权衡后确定提交哪个group的sa

---

### 评论 #14 (作者: CM51884, 时间: 1年前)

太详细了！感谢毛老师分享sa相关知识

---

### 评论 #15 (作者: SW66069, 时间: 1年前)

感谢分享，大佬太牛了

---

### 评论 #16 (作者: 顾问 JR23144 (Rank 6), 时间: 1年前)

Fitness 大于 5  是指 IS 大于 还是 TRAIN  还是 TEST 大于，还是都要大于呢

---

### 评论 #17 (作者: JT77454, 时间: 1年前)

感谢分享，收获很多！

---

### 评论 #18 (作者: KM49592, 时间: 1年前)

感谢大佬分享，这就去实践！

---

### 评论 #19 (作者: 顾问 MS51256 (Rank 28), 时间: 1年前)

SA比赛又拜读了毛老师的帖子，sa比赛可以每天叫一个优质的高质量alpha，对于combine和vf都是一件非常好的事情，此外这个最大团算法对于提交确实又很大的帮助，感谢毛老师的分享，祝愿毛老师继续保持gm。
========================================================================================================================================================================

---

### 评论 #20 (作者: YQ84572, 时间: 6个月前)

这篇最大独立集算法太硬核了！我用贪心法优化后，每天能多筛出3-5个低相关SA，收益提升明显。但要注意，必须用本地缓存PNL数据，平台在线检测有0.03误差。建议新手先用Fitness>5和prod_correlation<0.5预筛，再跑算法。

---

### 评论 #21 (作者: JQ70858, 时间: 4个月前)

每天来学习，似乎我永远是新人。因为好多东西都看不懂，不知道是不是缺少某个领域的专业知识。。虽然已经学了sa的基础知识，但是不会自己组，都是在跑代码。而且也许是我的因子质量不行，从来没出过过5的。。不论是sharpe还是fitness。。。

---

### 评论 #22 (作者: LJ12230, 时间: 2个月前)

感谢大佬分享！

---

