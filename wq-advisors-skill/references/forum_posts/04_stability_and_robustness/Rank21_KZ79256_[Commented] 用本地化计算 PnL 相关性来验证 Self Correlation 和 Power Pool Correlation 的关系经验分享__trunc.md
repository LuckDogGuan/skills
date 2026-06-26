# 用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享_32272027850775.md
- **作者**: LL87164
- **发布时间/热度**: 1年前, 得票: 5

## 帖子正文

目的：搞清楚 Self Correlation 和 Power Pool Correlation 的关系

最近回测结果的相关性检测项中多出来一个 Power Pool Correlation，这个原来是在 Check Submission 中的一项，现在单独拿到相关性检测中了。问题是它和原来的 Self Correlation 是什么关系？Pow Pool 是 Self 的一个子集吗？如果是，为什么也二者的相关性检测结果会不同？最近注意到有些顾问在回测中也有同样的疑惑。所以做了一下下面的测试和验证。

结论：Self 不含 Power Pool。Self 指的是：所有获取的OS Alpha中， **非Power Pool** 的部分。

验证方法：通过用本地化计算 PnL 相关性的数据和页面检查的数据进行比对来验证。

代码逻辑如下（限于篇幅不附上具体代码）：

1. 首先，通过  `get_os_alphas_and_power_pool_ids`  获取了所有已提交OS Alpha 的详情（称之为  `all_os_alpha_ids_from_api` ），并从中识别出了Power Pool（  `power_pool_alpha_ids_from_api）` 。
2. 然后，为  `all_os_alpha_ids_from_api`  获取了PnL数据，形成了  `os_daily_pnl_df` 。这个  `os_daily_pnl_df`  包含了所有被选中的已提交OS Alpha（包括Power Pool成员和非Power Pool成员）的PnL。
3. 在进行“通用OS Alpha池”相关性检测时，代码明确地创建了一个  `general_os_pool_pnl_df` ，它是从  `os_daily_pnl_df`  中排除了  `power_pool_alpha_ids_from_api`  之后的部分。

所以  **“通用OS Alpha池”**  指的是：所有获取的OS Alpha中， **非Power Pool** 的部分。

以下是相关性的验证数据（以一个Alpha为例）


> [!NOTE] [图片 OCR 识别内容]
> NILN0
> 怕大性师迹
> 迪用03池
> OFFbUFV:
> 迪~
> (耶入怕大性
> '44 /
> ~
> ' / )
> 0
> WARNING
> 相关性筛选  通用05池
> GQmWGrP:
> 通过 (最大相关性
> 0.422
> <0.7)
> 4
> WARNING
> 相关性筛选  通用05池
> Lg8omAn:
> 通过 (最大相关性
> 0.347
> <0.7)
> 3
> WARNING
> 相关性筛选  通用05池
> aRRVOL2:
> 通过 &最大相关性  0.351
> <
> 0.列
> 1_T +5`4
> c
> 
> 
> [!_!



> [!NOTE] [图片 OCR 识别内容]
> WARNING
> 相关性筛选
> Power Pool池
> GQmWGrP:
> 通过 (最大相关性  0.494
> 0.5)
> WARNING
> 相关性筛选 Power Pool池
> L88omAn:
> 通过 (最大相关性  0.417
> 0.5)
> WARNING
> 相关性筛选
> Power
> P0ol池
> aRRV012:
> 通过
> (最大相关性 0.422
> 0.5)


页面打开同一个Alpha，做相关性检测，数据如下：


> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximum
> Minimum
> 0.3467
> -0.0076
> Power Pool
> Maximum
> Minimum
> Correlation
> 0.4169
> -0.1996


可以看出其数据和上面代码的数据是一样的。因此，从代码的逻辑和数据上可以验证出一开始的结论。

---

## 讨论与评论 (5)

### 评论 #1 (作者: 顾问 KZ79256 (Rank 21), 时间: 1年前)

虽然Self 不含 Power Pool，但是prod包含Power Pool。所以当一个因子用power pool交了之后，该因子没法通过正常的方式提交（因为prod 不过）

=============================================================

---

### 评论 #2 (作者: 顾问 SD17531 (Rank 15), 时间: 1年前)

虽然Self 不含 Power Pool，但是prod包含Power Pool。所以当一个因子用power pool交了之后，该因子没法通过正常的方式提交（因为prod 不过）

===================================================================================

===================================================================================
所以一个alpha想要交两次的话,需要先不加描述,不标记PPA提交一次,然后再用PPA的方式提交一次,一鱼两吃了.

---

### 评论 #3 (作者: LL87164, 时间: 1年前)

[顾问 SD17531 (Rank 15)](/hc/zh-cn/profiles/27215746752791-顾问 SD17531 (Rank 15))

个人认为这个应该是个bug，因为同一个alpha仅仅是因为描述的不同而产生了两个ID存在于OS池中。一鱼是两吃了，但是整个组合的相关性也加大了。

---

### 评论 #4 (作者: LL87164, 时间: 1年前)

另外，今天发现平台的算法应该是更新了。从本地计算的数据和网页端返回的数据进行比对后发现，现在的Self Correlation 是包含了 Power Pool Correlation的。

---

### 评论 #5 (作者: DZ31817, 时间: 9个月前)

20250928

------------------------------------------------------------------------------------------

目前有个新的变化，同时带有ra和ppa tag的alpha，会同时进入self corr和ppa corr的池子。目前可通过tag来判定该alpha进入哪个corr池子。

---

