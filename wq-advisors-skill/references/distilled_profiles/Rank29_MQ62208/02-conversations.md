# 顾问 MQ62208 (Rank 29) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 MQ62208 (Rank 29) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: [经验分享踩过的坑] 优化筛选alpha的方法)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [经验分享踩过的坑] 优化筛选alpha的方法_28230705623575.md
- **时间**: 1年前

**提问/主帖背景 (XP21100)**:
优化筛选alpha的方法：

```
def verfiy_result(res):    checks = res['is']['checks']    result = []    for check in checks:        if check['result'] == 'PASS':            continue        if check['result'] in ['FAIL','ERROR']:            name = check['name']            limit = check.get('limit', '')            value = check.get('value', '')            opeator = ""            if 'LOW_' in name:#IS_LADDER_SHARPE                opeator = "<"                IS_indicators = name.replace("LOW_", "")            elif 'HIGH_' in name:                opeator = ">"                IS_indicators = name.replace('HIGH_', '')            elif 'SELF_CORRELATION' in name or 'PROD_CORRELATION' in name:                opeator = ">"                IS_indicators = name            elif 'CONCENTRATED_WEIGHT' == name:                IS_indicators = name + '权重过于集中'            elif 'IS_LADDER_SHARPE' == name and 'SHARPE' in str(result):                continue            elif "REGULAR_SUBMISSION" == name:                IS_indicators = name                opeator = "提交次数到上限"            else:                IS_indicators = name        elif check['result'] == 'PENDING':            name = check['name']            limit = check.get('limit', '')            value = check.get('value', '')            opeator = ""            IS_indicators = name + '待定'        else:            continue        text = f"{IS_indicators}{value}{opeator}{limit}"        result.append(text)    return result
```

文中的res是请求的响应对象response.json();

```
error = verfiy_result(res)
```

只要error 返回不是空，就是有不通过的内容

```
check_url = f'[链接已屏蔽]
```

注意返回对象的状态码

```
response.status_code
```

```
if response.status_code == 429:  您已达到并发提交Alpha的限制。请等待前一个完成
```

```
if response.status_code == 403:  提交失败，需要改进
```

```
if response.status_code == 404:  提交超时，请重新提交
```

**顾问 MQ62208 (Rank 29) 的解答与建议**:
这是check alphas接口还是提交 alphas 的接口？


---

### 技术对话片段 2 (原帖: 【插件】Genius Rank分析代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【插件】Genius Rank分析代码优化_29496672188951.md
- **时间**: 1 year ago

**提问/主帖背景 (KZ79256)**:
插件地址： [[链接已屏蔽])

在插件中增加了对于genius rank的分析，这里非常感谢  [XX42289](/hc/en-us/profiles/14187300941847-XX42289)  提供的 [python分析代码]([L2] 【课代表】最新genius排名模拟代码_29383292162199.md)

使用说明

- 安装完插件后，打开genius页面（如果没有可以刷新一下，这可能和WQ的加载逻辑相关，后续会进行fix），可以看到会增加了两个按钮，其中`排名分析`是抓取排行榜的数据进行分析.`显示排名分析`是调用之前抓取的分析结果（自己的排名数据）. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> Gnius
> Displaying quarter:
> 2025-01 (Curren)
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析

- 无论点击以上哪一个按钮都会在该页面的按钮的下面显示一个自己的分析表格, 表格右上角是分析的时间.PS:排名分析按钮需要等待片刻（抓取时按钮上显示抓取的进度） 
> [!NOTE] [图片 OCR 识别内容]
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> Genius Rank Analysis
> 2025-01-25112:48:02.2082
> 我的排名信息
> 2025-01-2571243.022082
> 总人数:5691 人
> 可能的基准人数:936人
> (交够40个)
> 名个Level 满足的人数 _
> 最终的人数:
> For Expert: 721 /187
> For Master: 22194
> For Grandmaster: 0119
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171/187
> 总排名:15/94
> 总排名:0119
> Operator Count: 533名
> Operator Count: 21 名
> Operator Count:
> Operator AVE: 3名
> Operator AVE: 1 名
> Operator AVg:
> Field Count: 705 名
> Field Count: 23 多
> Field Count:
> Field AVB: 2名
> Field AVg:
> Field AVg:
> Community Activity: 81 名
> Community Activiny: 15 名
> Community Activity:
> Completed Referrals: 58 名
> Completed Referrals: 2 多
> Completed Referrals; 1 名
> Max Simulation Streak: 310名
> Max Simulation Streak: 18 名
> Max Simulation Streak:
> TotalRank; 1692 多
> Tota
> Rank: 81 名
> Tota
> Rank:
> Current level;: Gold
> Best leyel: Gold
> Current quarterend: March 31st. 2025
> COUO

- 此外，还可将鼠标移动到排行榜上的UserId处展示他人的分析数据 
> [!NOTE] [图片 OCR 识别内容]
> X42289 排名信息
> 总人数:5691 人
> Aggregate by:
> 可能的基准人数:936  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 721/187
> For Master: 22194
> For Grandmaster: 0/19
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171187
> 总排名:4194
> 总排名:0/19
> Operator Count: 199名
> Operator Count: 13名
> Operator Count: 1 名
> Operator
> 17名
> Operator
> 2名
> Operator
> 1名
> Rank
> User
> Field Count: 423名
> Field Count: 23名
> Field Count:
> 名
> Field
> 18名
> Field
> 名
> Field
> Community Activity: 20名
> Community Activity: 3名
> Community Activity:
> Completed Referrals: 12名
> Completed Referrals: 1 名
> Completed Referrals:
> 名
> 1,090
> 1279256
> Max Simulation Streak:
> Max Simulation Streak: 16
> Max Simulation Streak:
> 273名
> Total Rank: 962名
> Total Rank: 59名
> Total Rank: 7名
> XP21
> 042289
> Maser
> Maser
> 117
> 0.00
> AVB:
> AVE: 
> AVg:
> AVB: -
> AVg:
> AVB: -


**顾问 MQ62208 (Rank 29) 的解答与建议**:
华子哥写的这个插件确实牛逼，响应那句科技造福于人类。使用真的很方便，直接能看到自己目前的等级。希望华哥后续还能整出其他方便快捷的小插件。这是位前端大佬，膜拜大佬，感谢大佬。


---

### 技术对话片段 3 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MQ62208 (Rank 29) 的解答与建议**:
量化学习日记

由于value factor 太低导致每天只有一美元，痛定思痛总结了下，

提高value factor 实用技巧：

1. Focus on Low Correlation 专注于低相关性
2. Create Single-Dataset Alphas 创建单数据集 Alpha
3. Turnover and Sharpe Improvements 降低换手率和夏普改进
4. Explore New Datasets 探索新数据集
5. Avoid Overfitting 避免过拟合


---

### 技术对话片段 4 (原帖: 完成当前池后，保存进度)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 基于三阶模板的一些优化_28293182637463.md
- **时间**: 1年前

**提问/主帖背景 (SH97251)**:
## 原始运行框架

原始的三阶运行模板大致逻辑顺序为：选定datafield -> 填充datafield -> 用基础运算符构建第一轮次模拟 -> 筛选第一轮次模拟结果，用进阶运算符构建第二轮次模拟 -> 筛选第二轮次+第一轮次模拟结果，用trade_when运算符构建第三轮次模拟 -> 最终筛选

## 问题讨论

### 运算符选择问题

所有模板中的运算符有：

```
basic_ops = ["log", "sqrt", "reverse", "inverse", "rank", "zscore", "log_diff", "s_log_1p",'fraction', 'quantile', "normalize", "scale_down"]ts_ops = ["ts_rank", "ts_zscore", "ts_delta", "ts_sum", "ts_product", "ts_ir", "ts_std_dev", "ts_mean", "ts_arg_min", "ts_arg_max", "ts_min_diff", "ts_max_diff", "ts_returns", "ts_scale", "ts_skewness", "ts_kurtosis", "ts_quantile"]arsenal = ["ts_moment", "ts_entropy", "ts_min_max_cps", "ts_min_max_diff", "inst_tvr", 'sigmoid', "ts_decay_exp_window", "ts_percentage", "vector_neut", "vector_proj", "signed_power"]group_ops = ["group_neutralize", "group_rank", "group_normalize", "group_scale", "group_zscore"]
```

在第一轮结束，第二轮模拟的时候，如果使用的运算符有重复，有时候会出现很drama的zscore(zscore)这种相同运算符套在一起的情况，因此我增加了模拟之前运算符的查重逻辑，限定同一个运算符不能出现三次及以上。

由于运算符的级别不同，我认为在模拟中，它们应该具有不同的复杂度，因此我人为定义了运算符的复杂度，为了防止最终的alpha过拟合，我限定了复杂度的最大值，大于最大值的表达式我认为过拟合风险高，不予进行模拟。

建立在这两条逻辑之上，我增加了运算符的处理逻辑，运算符处理单独作为一个py文件存在，全部内容如下：
```

from typing import Dict, Set, List, Tuple

class OperationAnalyzer:

def__init__(self):

# 基于已有操作符定义权重

self.operation_weights= {

# 基础运算 - 计算复杂度O(n)

'basic': {

'log': 1.0,

'sqrt': 1.0,

'reverse': 1.0,

'inverse': 1.0,

'rank': 1.5,

'zscore': 1.5,

'log_diff': 1.0,

's_log_1p': 1.0,

'fraction': 1.0,

'quantile': 1.5,

'normalize': 1.5,

'scale_down': 1.0

},

# 时序操作 - 需要历史数据

'ts': {

'ts_rank': 2.0,

'ts_zscore': 2.0,

'ts_delta': 1.5,

'ts_sum': 1.5,

'ts_product': 1.5,

'ts_ir': 2.0,

'ts_std_dev': 2.0,

'ts_mean': 1.5,

'ts_arg_min': 1.5,

'ts_arg_max': 1.5,

'ts_min_diff': 1.5,

'ts_max_diff': 1.5,

'ts_returns': 1.5,

'ts_scale': 1.5,

'ts_skewness': 2.0,

'ts_kurtosis': 2.0,

'ts_quantile': 1.5

},

# 高级操作 - 复杂计算或特殊处理

'arsenal': {

# 复杂的统计指标

'ts_moment': 3.0, # 更高阶的统计矩

'ts_entropy': 3.0, # 信息熵计算复杂

# 中等复杂度

'ts_min_max_cps': 2.5,

'ts_min_max_diff': 2.5,

'vector_neut': 2.5,

'vector_proj': 2.5,

# 相对简单的转换

'inst_tvr': 2.0,

'ts_decay_exp_window': 2.0,

'sigmoid': 1.5,

'ts_percentage': 1.5,

'signed_power': 1.5

},

# 分组操作 - 需要截面数据

'group': {

'group_neutralize': 2.5,

'group_rank': 2.5,

'group_normalize': 2.5,

'group_scale': 2.5,

'group_zscore': 2.5

}

}

# 定义有效的操作组合及其复杂度调整

self.effective_combinations= {

('rank', 'log'): -0.5, # rank(log(x))

('zscore', 'log'): -0.5, # zscore(log(x))

('rank', 'ts_returns'): -0.5, # rank(ts_returns(x))

('ts_rank', 'log'): -0.5 # ts_rank(log(x))

}

# 定义无效的操作序列

self.invalid_sequences= [

('rank', 'rank'),

('zscore', 'zscore'),

('normalize', 'normalize'),

('log', 'log'),

('ts_rank', 'rank'),

('rank', 'ts_rank'),

('zscore', 'normalize'),

('normalize', 'zscore')

]

defanalyze_expression(self, expr: str) -> Dict:

"""分析alpha表达式的复杂度和特征"""

stats= {

'total_ops': 0,

'complexity_score': 0,

'op_counts': {},

'nesting_level': 0,

'category_usage': {cat: 0forcatinself.operation_weights.keys()},

'operation_sequence': []

}

# 统计嵌套层数

stats['nesting_level'] =expr.count('(')

# 统计各类操作符使用情况

forcategory, opsinself.operation_weights.items():

foropinops:

ifopinexpr:

count=expr.count(op)

stats['op_counts'][op] =count

stats['category_usage'][category] +=count

stats['complexity_score'] +=count*self.operation_weights[category][op]

stats['total_ops'] +=count

stats['operation_sequence'].append(op)

# 应用有效组合的复杂度调整

for (op1, op2), adjustmentinself.effective_combinations.items():

iff"{op1}({op2}("inexpr:

stats['complexity_score'] +=adjustment

returnstats

defcheck_operation_sequence(self, expr: str) -> Tuple[bool, str]:

"""检查操作序列是否合理"""

forop1, op2inself.invalid_sequences:

iff"{op1}({op2}("inexpr:

returnFalse, f"发现无效的操作序列: {op1}({op2})"

returnTrue, ""

defis_valid_expression(self, expr: str, max_complexity: float=15.0) -> Tuple[bool, str]:

"""检查表达式是否合理"""

# 首先检查操作序列

seq_valid, seq_reason=self.check_operation_sequence(expr)

ifnotseq_valid:

returnFalse, seq_reason

stats=self.analyze_expression(expr)

# 复杂度检查

ifstats['complexity_score'] >max_complexity:

returnFalse, f"表达式复杂度过高: {stats['complexity_score']:.2f} > {max_complexity}"

# 嵌套层数检查

ifstats['nesting_level'] >10:

returnFalse, f"嵌套层数过多: {stats['nesting_level']} > 8"

# 重复操作检查

forop, countinstats['op_counts'].items():

ifcount>2:

returnFalse, f"操作符 {op} 重复使用过多: {count} > 2"

# 分类使用检查

category_count=sum(1forusageinstats['category_usage'].values() ifusage>0)

ifcategory_count>3:

returnFalse, f"使用了过多不同类型的操作符: {category_count} > 3"

returnTrue, ""

defget_expression_complexity(self, expr: str) -> float:

"""获取表达式的复杂度分数"""

returnself.analyze_expression(expr)['complexity_score']

deffilter_expressions(self, expressions: List[str], max_complexity: float=13.0) -> List[str]:

"""过滤表达式列表，返回复杂度合理的表达式"""

return [exprforexprinexpressionsifself.is_valid_expression(expr, max_complexity)[0]]

defget_expression_details(self, expr: str) -> Dict:

"""获取表达式的详细分析信息"""

stats=self.analyze_expression(expr)

is_valid, reason=self.is_valid_expression(expr)

return {

'valid': is_valid,

'reason': reason,

'complexity': stats['complexity_score'],

'nesting_level': stats['nesting_level'],

'operation_counts': stats['op_counts'],

'category_usage': stats['category_usage']

}

```然后是一些模拟前表达式生成的工作：
```

def get_enhanced_expressions(base_expr: str, region: str) -> List[str]:

"""

生成增强版的表达式

Args:

base_expr: 基础表达式

region: 地区

Returns:

增强后的表达式列表

"""

enhanced_exprs= []

# 统计增强

statistical_ops= [

# 高阶矩

f"ts_moment({base_expr}, 3)", # 三阶矩

f"ts_moment({base_expr}, 4)", # 四阶矩

# 不同时间窗口的熵

f"ts_entropy({base_expr}, 5)", # 周度熵

f"ts_entropy({base_expr}, 22)", # 月度熵

f"ts_entropy({base_expr}, 66)", # 季度熵

f"ts_entropy({base_expr}, 120)"# 半年熵

]

enhanced_exprs.extend(statistical_ops)

# 动态权重和衰减

decay_ops= [

f"ts_decay_exp_window({base_expr}, 5)", # 周度

f"ts_decay_exp_window({base_expr}, 22)", # 月度

f"ts_decay_exp_window({base_expr}, 66)", # 季度

f"ts_decay_exp_window({base_expr}, 120)"# 半年

]

enhanced_exprs.extend(decay_ops)

# 非线性变换

transform_ops= [

f"sigmoid({base_expr})",

f"signed_power({base_expr}, 0.5)", # 类平方根

f"signed_power({base_expr}, 2)"# 平方

]

enhanced_exprs.extend(transform_ops)

# 复合条件交易

combined_ops= [

f"trade_when(ts_entropy(close, 22) < 0.5, {base_expr})", # 市场低不确定性时段

f"trade_when(abs(ts_moment(close, 3)) < 2, {base_expr})", # 分布相对对称时段

f"trade_when(ts_std_dev(volume, 22) > ts_std_dev(volume, 66), sigmoid({base_expr}))"# 波动放大时段

]

enhanced_exprs.extend(combined_ops)

returnenhanced_exprs

def process_third_round(so_layer: Dict, region: str, dataset_id: str) -> List[Tuple[str, int]]:

"""

处理第三轮模拟的表达式生成和筛选

Args:

so_layer: 第二轮筛选后的结果

region: 地区

dataset_id: 数据集ID

Returns:

筛选后的(alpha表达式, decay)列表

"""

th_alpha_list= []

skipped_count= {'trade_when': 0, 'enhanced': 0}

forregion, couplesinso_layer.items():

forexpr, decayincouples:

# 1. 处理原始trade_when表达式

trade_when_candidates=trade_when_factory("trade_when", expr, region)

foralphaintrade_when_candidates:

is_valid, reason=analyzer.is_valid_expression(alpha)

ifis_valid:

th_alpha_list.append((alpha, decay))

else:

skipped_count['trade_when'] +=1

ifskipped_count['trade_when'] <=5: # 限制打印次数

print(f"Skipped trade_when: {alpha}\nReason: {reason}")

# 2. 处理增强版表达式

enhanced_candidates=get_enhanced_expressions(expr, region)

foralphainenhanced_candidates:

is_valid, reason=analyzer.is_valid_expression(alpha)

ifis_valid:

th_alpha_list.append((alpha, decay))

else:

skipped_count['enhanced'] +=1

ifskipped_count['enhanced'] <=5: # 限制打印次数

print(f"Skipped enhanced: {alpha}\nReason: {reason}")

# 打印统计信息

print(f"\nThird round filtering statistics:")

print(f"Total expressions generated: {len(th_alpha_list)}")

print(f"Skipped trade_when expressions: {skipped_count['trade_when']}")

print(f"Skipped enhanced expressions: {skipped_count['enhanced']}")

returnth_alpha_list

```

### 关于进度保存的问题

在运行过程中，如果被打断，再开始的时候会从0开始运行，因此针对multi_simulate函数，我增加了进度保存功能，增加了一个入参if_new,用于确认这次运行是新的运行还是继承之前没运行完的结果，选择True就清空之前的记录文件从头跑，选择False就继承之前的运行结果，跳过已经模拟过的alpha。修改后的simulate函数如下：
```

def multi_simulate_Sia(alpha_pools, neut, region, universe, start, progress_file, if_new_progress=False):

s=login() # 登录获取会话

brain_api_url=' [[链接已屏蔽]) '

# 初始化 completed_pools 和 completed_alpha_ids

completed_pools= []

completed_alpha_ids= []

ifif_new_progress==False:

# 加载已有的进度

progress=load_progress(progress_file)

completed_pools=progress["completed_pools"]

completed_alpha_ids=progress["completed_alpha_ids"]

else:

withopen(progress_file, 'w') asf:

json.dump({"completed_pools": [], "completed_alpha_ids": []}, f)

# 开始模拟任务

forx, poolinenumerate(alpha_pools):

ifx<start:

continue

# 跳过已经完成的池

ifxincompleted_pools:

print(f"Pool {x} already completed, skipping...")

continue

progress_urls= []

fory, taskinenumerate(pool):

# 给每个任务生成唯一的 alpha_id

task_id=f"pool_{x}_task_{y}"

iftask_idincompleted_alpha_ids:

print(f"Task {task_id} already completed, skipping...")

continue

# 生成模拟数据

sim_data_list=generate_sim_data(task, region, universe, neut)

try:

# 发送请求进行模拟

simulation_response=s.post(' [[链接已屏蔽]) ', json=sim_data_list)

simulation_progress_url=simulation_response.headers['Location']

progress_urls.append(simulation_progress_url)

except:

print(" loc key error")

sleep(10)

s=login()

print(f"Pool {x} post done")

# 监控每个进度 URL

forj, progress_urlinenumerate(progress_urls):

try:

whileTrue:

simulation_progress=s.get(progress_url)

ifsimulation_progress.headers.get("Retry-After", 0) ==0:

break

sleep(float(simulation_progress.headers["Retry-After"]))

# 获取模拟进度

status=simulation_progress.json().get("status", 0)

task_id=f"pool_{x}_task_{j}"# 任务ID

ifstatus=="COMPLETE":

completed_alpha_ids.append(task_id) # 记录已完成的任务

print(f"Task {task_id} completed")

else:

print(f"Task {task_id} not complete: {progress_url}")

exceptKeyError:

print(f"Look into: {progress_url}")

exceptExceptionase:

print(f"Error: {e}")

# 完成当前池后，保存进度

completed_pools.append(x) # 标记当前池已经完成

save_progress({

"completed_pools": completed_pools,

"completed_alpha_ids": completed_alpha_ids

}, progress_file)

print(f"Pool {x} simulate done")

print("Simulation done")

```

## 优化后的运行框架

在进行完运算符筛选组合，和设置完simulate函数后，不同阶段的运行过程如何衔接，自由度很高。我尝试过把它们组合成一个函数，也尝试过分轮次运行分别保存结果，发现这个过程最好还是不要固定，根据自己需要处理的数据集大小、电脑能够连续不断运行的时间自行决定，因此大家可以自己发挥衔接这两部分。

```
补充关于process_file的两个函数：def load_progress(progress_file):ifos.path.exists(progress_file):withopen(progress_file, 'r') asf:returnjson.load(f)else:withopen(progress_file, 'w') asf:progress= {"completed_pools": [], "completed_alpha_ids": []}json.dump(progress, f)returnprogressdef save_progress(completed_tasks, progress_file):try:withopen(progress_file, 'w') asf:json.dump(completed_tasks, f)exceptExceptionase:print(f"Failed to save progress to {progress_file}: {e}")
```

另外，如果要保存每个阶段最终的alpha_id的话，可以在process_file里新增一个键，下次运行的时候直接从本地文件读取上一次的alpha_id，而不是重新进行处理。因为重新处理会有问题，下面是例子：
假设round1已经跑完，进入round2。第一次运行round2的时候，按照筛选条件，筛选的一定是所有符合条件的round1结果，但如果中途断掉，重新运行round2，即使有进度记录，但是此时的输入会变成：round1符合条件的结果+round2跑完那部分符合条件的结果，那么本次的pool和上次运行round2的pool就不相同，进度记录也会失效。如果有把握在一段时间内三个阶段都能跑完，就不用额外增加这一步。

**顾问 MQ62208 (Rank 29) 的解答与建议**:
感谢博主分享


---
