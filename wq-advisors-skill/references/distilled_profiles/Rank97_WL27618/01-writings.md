# 顾问 WL27618 (Rank 97) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 WL27618 (Rank 97) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: agent时代对expression ast的一个大更新
- **主帖链接**: agent时代对expression ast的一个大更新.md
- **讨论数**: 6

虽然单用agent做长流程的任务非常不可靠, 但是的确为一次性的任务提供了很多便捷. 有了agent后, 我的工作流程也从 手动(一次性任务) | 写代码(重复任务) 的两个选项, 变成了 手动(一次性任务) | agent(一次性简单任务) | 写代码(重复任务) 的三个选项, 这日子是越过越好了.关于验证表达式合法性, 尤其是参数个数和参数类型匹配, 本来只有两种处理方法:1. 我自己手动写了一些规则, 比如vector, group的用法(难以周全难以维护)2. 从平台的文档中提取每个operator的参数用法(文档不完善不可靠)但是因为有了agent, 现在有了第三种方法3.通过平台feedback更新一份完善的包含所有operator参数规则的文档(容易维护, 完美的方案)首先, 我们规定一份文档的格式(几个position args, 几个keyword args, 返回类型, 参数类型, 是否强制输入, etc. )然后, 应用mcp在平台上自主对operator的用法进行 回测 -> feedback -> 修改文档 这套流程. (比如图示显示target_tvr是必要参数.sensitivity对jump decay是必要参数)最后得到包含所有合法性检验信息的本地文件.即使平台之后对某些operator的规则改变, 也只需通过这套流程修改一下规则文件即可.顺便宣传一下我的其他相关帖子:用ast生成super alpha中的combo表达式用python ast unparse修改表达式细节记录一下ast在代码中的用法super alpha combo中operator的使用心得

---

### 帖子 #2: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.comagent时代对expression ast的一个大更新_38291391911575.md
- **讨论数**: 6

虽然单用agent做长流程的任务非常不可靠, 但是的确为一次性的任务提供了很多便捷. 有了agent后, 我的工作流程也从 手动(一次性任务) | 写代码(重复任务) 的两个选项, 变成了 手动(一次性任务) | agent(一次性简单任务) | 写代码(重复任务) 的三个选项, 这日子是越过越好了.

关于验证表达式合法性, 尤其是参数个数和参数类型匹配, 本来只有两种处理方法:

1. 我自己手动写了一些规则, 比如vector, group的用法(难以周全难以维护)

2. 从平台的文档中提取每个operator的参数用法(文档不完善不可靠)

但是因为有了agent, 现在有了第三种方法

3.  **通过平台feedback更新一份完善的包含所有operator参数规则的文档(容易维护, 完美的方案)**

**
> [!NOTE] [图片 OCR 识别内容]
> # Generated
> struct With detailed argument
> info
> OPERATOR METADATA
> abs
> args
> [
> default'
> None,
> mandatory
> Truey
> name
> X'
> type
> MATRIX'}]
> category
> Arithmetic'
> is_variadic': Falsey
> max_args
> 1 
> min_args
> 1,
> return_type
> 'MATRIX
> add'
> args'
> default '
> None
> mandatory
> True,
> name
> X'
> type
> MATRIX'},
> default' :
> None
> mandatory
> True,
> name
> y'
> type
> MATRIX'},
> default'
> false
> mandatory'
> False
> name
> filter
> type
> SCALAR'}]
> category
> 'Arithmetic'
> is_variadic' :
> False,
> 'max_args
> 3,
**

首先, 我们规定一份文档的格式(几个position args, 几个keyword args, 返回类型, 参数类型, 是否强制输入, etc. )


> [!NOTE] [图片 OCR 识别内容]
> get_tosk progress (quont-night MCP Server) {"task_id": "08682061-4476-456f-4924-22744793448c"}
> status
> finished"
> 
> result"
> {
> E"status'
> :
> "failed" ,的格式(几个position args; 几个 keyword args; 返回类型;参数类型;是
> 'progress_url
> "https: / /api.worldquantbrain . com/simulations /ZghXlv3Q94GaaEEJwBXdGSG" =
> error
> 'Required attribute
> 'target_tvn
> must have
> Value



> [!NOTE] [图片 OCR 识别内容]
> "id":
> 'EWwGtdHUSaygaFleiszcNrz" 然后;应用mcp在平台L对operator 的用法迸行 回测 > feedback
> 修改文档  这套流程:(比如图示显示target_tVr
> }
> 
> 是必要参数 )
> ]
> error"
> "Batch failed:InCode:
> ts_decay_linear(close
> 10)
> CANCELLED:
> NonelnCode:
> ts_rankCclose,
> 10)
> >
> CANCELLED:
> NonelnCode: winsorize(close)
> CANCELLED:
> NonelnCode:
> pasteurize(close)
> >
> CANCELLED:
> NonelnCode: regression_neut(close, close)
> CANCELLED: NoneInCode
> ts_regression(close, close,
> 10)
> >
> CANCELLED: NonelnCode:
> ts_decay_exp_windowCclose, 10)
> >
> CANCELLED: NonelnCode:
> keep(close, 1)
> >
> CANCELLED:
> NonenCode:
> jump_decay(close,
> 10)
> >
> ERROR:
> Required attribute
> "sensitivity
> Iust
> have
> a ValuelnCode
> inst_tvr(close,
> 10)
> >
> CANCELLED:
> None
> }
> 
> 丰颞


然后, 应用mcp在平台上自主对operator的用法进行 回测 -> feedback -> 修改文档 这套流程. (比如图示显示target_tvr是必要参数.sensitivity对jump decay是必要参数)

最后得到包含所有合法性检验信息的本地文件.

即使平台之后对某些operator的规则改变, 也只需通过这套流程修改一下规则文件即可.

顺便宣传一下我的其他相关帖子:

[用ast生成super alpha中的combo表达式](用ast生成super alpha中的combo表达式代码优化_32726278113687.md)

[用python ast unparse修改表达式细节](用python ast unparse修改表达式细节代码优化_33892557730455.md)

[记录一下ast在代码中的用法](/hc/zh-cn/community/posts/35565539058967-%E8%AE%B0%E5%BD%95%E4%B8%80%E4%B8%8Bast%E5%9C%A8%E4%BB%A3%E7%A0%81%E4%B8%AD%E7%9A%84%E7%94%A8%E6%B3%95)

[super alpha combo中operator的使用心得](super alpha combo中operator的使用心得_32194005946775.md)

---

### 帖子 #3: DCC 第三名经验分享经验分享
- **主帖链接**: DCC 第三名经验分享经验分享.md
- **讨论数**: 11

## 
> [!NOTE] [图片 OCR 识别内容]
> 数据流
> 处理管线
> 优化方法
> 1。搜索效率
> Theme
> 时间上拆分成buckets
> 2。横截面拆分成batch
> 2。搜索质量(召回率)
> 主题的拆分和聚合
> 主题检索
> 2.
> Co-mention打 折回收机制
> 搜索质量(精确度)
> Api的重排序功能
> 2.
> 阈值截断
> Chuck
> Content' (段落内容)
> `Relevance
> (相关性评
> 分)
> Sentiment'
> (情绪评分)
> Entity_id
> (关联实体)
> 'Date' (发布日期)
> 直接映射 chuck > vector
> Relevance Vector
> 2
> sentiment Vector
> 数据映射
> 2
> 内容优化 content > Ilm >
> relevancelsentiment
> 3
> Vector内部优化
> doc(新闻)级整合和归因(再分配)
> Vector
> id
> (关联实体)
> Date` (发布日期)
> VeC
> countlvec_avglvec_
> maxl
> VeC
> norm
> relevance和sentiment结合:
> 矩阵合成
> weighted_sentiment
> Vec_sum(rel*sent)l
> Vec_sum(rel)
> Matrix
> Entity_id
> (关联实体)
> Date` (发布日期)
> 矩阵补强:  解决稀疏性
> 时间层面扩散: ts_
> meanl 7,
> ts_meanl, 30)
> 数据后处理与校验
> 2.
> 横截面扩散:用实体相关性矩阵做
> diffusion
> 2。数据质量
> Entity_


## 

我看dcc比赛大家很多都卡在没有完全理解整个工作流程, 所以想分享一下这方面, 至于如何提高os表现, 我也没有资格多说...

核心在于如何将碎片化的新闻  **Chunks（段落）**  转化为具有预测能力的“日期-实体”评分Matrix。

### 一、 标准处理管线 (Standard Pipeline)

1. **主题检索 (Retrieval)** ：根据预设的主题（Themes）进行数据拉取。
2. **数据映射与矩阵合成 (Mapping & Synthesis)** ：
   - **核心数据结构** ：API 返回的每一条原始数据均为一个  **Chunk** ，包含核心字段： `Content` （段落内容）,  `Relevance` （相关性评分）,  `Sentiment` （情绪评分）,  `Entity_id` （关联实体）,  `Date` （发布日期）。
   - **物理映射** ：将每个 Chunk 的评分根据其  `Date`  和  `Entity_id`  直接填充到对应的矩阵坐标中，形成特征矩阵。
3. **数据校验 (Validation)** ：在进入 Alpha 研究前，对矩阵的覆盖率（Coverage）、空值率（NaN Ratio）以及极端值分布进行工程化检查。

### 二、 关键优化策略 (Optimization Strategies)

#### 1. 搜索效率：Smart-batching

- **时间维优化** ：利用 Volume API 监控主题热度。对于新闻爆发的“热点日期”，自动缩减 Bucket 跨度（如从月缩短至天），防止数据截断。
- **实体维优化** ：利用 Co-mention API 预估实体热度。对于高覆盖率实体缩小 Batch 规模，实现资源的“错峰检索”。

#### 2. 深度召回：主题树拆解与剪枝 (Theme Decomposition)

- **分而治之** ：针对叶子节点（Sub-themes）分别进行精准检索，提升垂直领域的召回率（Recall）。
- **路径聚合** ：沿着树形路径将子主题信号向上归并，并对数据量不足的节点进行“剪枝”处理，确保信号具备统计显著性。

#### 3. 打折回收：Direct vs Co-mention

- **Direct (1.0x)** ：实体为检索目标。
- **Co-mention (0.5x)** ：实体在文中出现，文中不存在检索目标（陪跑实体）。

#### 4. doc(新闻)级整合和归因(再分配)

- 采用  **Relevance 加权算法** ：$doc_ws = \sum(Sentiment \times Relevance) / \sum(Relevance)$。该算法能让模型更关注高度相关的段落（核心事实），忽略低相关的噪声段落。

#### 5. LLM 根据 chunk 内容优化 Relevance 和 Sentiment Vector

- **相关性判别** ：输出 is_theme_related (0/1)，剔除伪阳性段落。
- **Impact 转换** ：将通用 Sentiment 转化为针对目标公司的 Business Impact（Positive → +1, Negative → -1, Neutral/Unclear → 0）。

#### 6. 矩阵补强：解决稀疏性

- **时序平滑** ：利用  `ts_mean(7/30)`  捕获新闻情绪的“滞后性吸收”与“持续性影响”。
- **截面扩散 (Cross-sectional Diffusion)** ：利用实体间的 Co-mention 数量制作关系矩阵，将信号沿关系链向关联实体扩散填补，利用“网络效应”缓解原始矩阵的稀疏性。

### 三、 其他优化策略

- **Novelty Weighting** : 对同一实体计算 Embedding 相似度，对高度重复的信号进行系数衰减。
- **Confidence-Weighted Synthesis** : 让 LLM 打分时额外输出置信度用于加权。
- **利用 source_rank** : 区分主流财经媒体与地方小报。
- **信号制作** : 采取不同的时间衰减策略，用 log(volume) 给 sentiment 加权。

### 四、 RAG 治理与幻觉控制

我们可以尝试用 RAG 治理的方法论优化流程：

*  **实体掩码 (De-biasing)** ：通过  `[TARGET_COMPANY]`  占位符技术，切断模型对特定公司的先验偏见，强迫其仅根据文中事实进行推理。

*  **归因溯源 (Citations)** ：强制 LLM 输出 Motivation。

*  **HyDE (Hypothetical Document Embeddings)** ：先由 LLM 生成“虚构理想片段”再进行检索。

*  **Small-to-Big 检索** : 提供 Chunk 所在的整段窗口或整篇文章。

*  **Collective Reasoning** : 同一天同一 entity 的 chunks 拼接喂给 LLM 重新打分。

### 五、 alpha经验的迁移

dcc的数据基本相当于我们sentiment的数据集, 所以我们平时的datafield, operator, idea都可以尝试在dcc给的文本数据上迁移.

---

### 帖子 #4: DCC 第三名经验分享经验分享
- **主帖链接**: https://support.worldquantbrain.comDCC 第三名经验分享经验分享_40957810418199.md
- **讨论数**: 11

## 
> [!NOTE] [图片 OCR 识别内容]
> 数据流
> 处理管线
> 优化方法
> 1。搜索效率
> Theme
> 时间上拆分成buckets
> 2。横截面拆分成batch
> 2。搜索质量(召回率)
> 主题的拆分和聚合
> 主题检索
> 2.
> Co-mention打 折回收机制
> 搜索质量(精确度)
> Api的重排序功能
> 2.
> 阈值截断
> Chuck
> Content' (段落内容)
> `Relevance
> (相关性评
> 分)
> Sentiment'
> (情绪评分)
> Entity_id
> (关联实体)
> 'Date' (发布日期)
> 直接映射 chuck > vector
> Relevance Vector
> 2
> sentiment Vector
> 数据映射
> 2
> 内容优化 content > Ilm >
> relevancelsentiment
> 3
> Vector内部优化
> doc(新闻)级整合和归因(再分配)
> Vector
> id
> (关联实体)
> Date` (发布日期)
> VeC
> countlvec_avglvec_
> maxl
> VeC
> norm
> relevance和sentiment结合:
> 矩阵合成
> weighted_sentiment
> Vec_sum(rel*sent)l
> Vec_sum(rel)
> Matrix
> Entity_id
> (关联实体)
> Date` (发布日期)
> 矩阵补强:  解决稀疏性
> 时间层面扩散: ts_
> meanl 7,
> ts_meanl, 30)
> 数据后处理与校验
> 2.
> 横截面扩散:用实体相关性矩阵做
> diffusion
> 2。数据质量
> Entity_


## 

我看dcc比赛大家很多都卡在没有完全理解整个工作流程, 所以想分享一下这方面, 至于如何提高os表现, 我也没有资格多说...

核心在于如何将碎片化的新闻  **Chunks（段落）**  转化为具有预测能力的“日期-实体”评分Matrix。

### 一、 标准处理管线 (Standard Pipeline)

1. **主题检索 (Retrieval)** ：根据预设的主题（Themes）进行数据拉取。
2. **数据映射与矩阵合成 (Mapping & Synthesis)** ：
   - **核心数据结构** ：API 返回的每一条原始数据均为一个  **Chunk** ，包含核心字段： `Content` （段落内容）,  `Relevance` （相关性评分）,  `Sentiment` （情绪评分）,  `Entity_id` （关联实体）,  `Date` （发布日期）。
   - **物理映射** ：将每个 Chunk 的评分根据其  `Date`  和  `Entity_id`  直接填充到对应的矩阵坐标中，形成特征矩阵。
3. **数据校验 (Validation)** ：在进入 Alpha 研究前，对矩阵的覆盖率（Coverage）、空值率（NaN Ratio）以及极端值分布进行工程化检查。

### 二、 关键优化策略 (Optimization Strategies)

#### 1. 搜索效率：Smart-batching

- **时间维优化** ：利用 Volume API 监控主题热度。对于新闻爆发的“热点日期”，自动缩减 Bucket 跨度（如从月缩短至天），防止数据截断。
- **实体维优化** ：利用 Co-mention API 预估实体热度。对于高覆盖率实体缩小 Batch 规模，实现资源的“错峰检索”。

#### 2. 深度召回：主题树拆解与剪枝 (Theme Decomposition)

- **分而治之** ：针对叶子节点（Sub-themes）分别进行精准检索，提升垂直领域的召回率（Recall）。
- **路径聚合** ：沿着树形路径将子主题信号向上归并，并对数据量不足的节点进行“剪枝”处理，确保信号具备统计显著性。

#### 3. 打折回收：Direct vs Co-mention

- **Direct (1.0x)** ：实体为检索目标。
- **Co-mention (0.5x)** ：实体在文中出现，文中不存在检索目标（陪跑实体）。

#### 4. doc(新闻)级整合和归因(再分配)

- 采用  **Relevance 加权算法** ：$doc_ws = \sum(Sentiment \times Relevance) / \sum(Relevance)$。该算法能让模型更关注高度相关的段落（核心事实），忽略低相关的噪声段落。

#### 5. LLM 根据 chunk 内容优化 Relevance 和 Sentiment Vector

- **相关性判别** ：输出 is_theme_related (0/1)，剔除伪阳性段落。
- **Impact 转换** ：将通用 Sentiment 转化为针对目标公司的 Business Impact（Positive → +1, Negative → -1, Neutral/Unclear → 0）。

#### 6. 矩阵补强：解决稀疏性

- **时序平滑** ：利用  `ts_mean(7/30)`  捕获新闻情绪的“滞后性吸收”与“持续性影响”。
- **截面扩散 (Cross-sectional Diffusion)** ：利用实体间的 Co-mention 数量制作关系矩阵，将信号沿关系链向关联实体扩散填补，利用“网络效应”缓解原始矩阵的稀疏性。

### 三、 其他优化策略

- **Novelty Weighting** : 对同一实体计算 Embedding 相似度，对高度重复的信号进行系数衰减。
- **Confidence-Weighted Synthesis** : 让 LLM 打分时额外输出置信度用于加权。
- **利用 source_rank** : 区分主流财经媒体与地方小报。
- **信号制作** : 采取不同的时间衰减策略，用 log(volume) 给 sentiment 加权。

### 四、 RAG 治理与幻觉控制

我们可以尝试用 RAG 治理的方法论优化流程：

*  **实体掩码 (De-biasing)** ：通过  `[TARGET_COMPANY]`  占位符技术，切断模型对特定公司的先验偏见，强迫其仅根据文中事实进行推理。

*  **归因溯源 (Citations)** ：强制 LLM 输出 Motivation。

*  **HyDE (Hypothetical Document Embeddings)** ：先由 LLM 生成“虚构理想片段”再进行检索。

*  **Small-to-Big 检索** : 提供 Chunk 所在的整段窗口或整篇文章。

*  **Collective Reasoning** : 同一天同一 entity 的 chunks 拼接喂给 LLM 重新打分。

### 五、 alpha经验的迁移

dcc的数据基本相当于我们sentiment的数据集, 所以我们平时的datafield, operator, idea都可以尝试在dcc给的文本数据上迁移.

---

### 帖子 #5: But for safety against 'universe' if they put it there:
- **主帖链接**: PYTHON alpha的ast解析和语法检查经验分享.md
- **讨论数**: 1

python alpha的语法解析比fastexpr简单太多了. 天生和python适配. 字段也只需要找@alpha的函数变量就可以.

import ast

def parse_python_alpha(code):

"""

Parses a Python alpha script and extracts operators and data fields.

Data fields are strictly extracted from the @alpha decorator's 'data' argument.

"""

try:

tree = ast.parse(code)

data_fields = set()

operators = set()

for node in ast.walk(tree):

# Extract data fields ONLY from @alpha decorator

ifisinstance(node, ast.FunctionDef):

for decorator in node.decorator_list:

# Handle @alpha(data=["..."], ...)

ifisinstance(decorator, ast.Call):

ifisinstance(decorator.func, ast.Name) and decorator.func.id =='alpha':

for kw in decorator.keywords:

if kw.arg =='data'andisinstance(kw.value, ast.List):

for elt in kw.value.elts:

# Support both string literals and constants (Python 3.8+)

ifisinstance(elt, (ast.Constant, ast.Str)):

val = elt.value if hasattr(elt, 'value') else elt.s

data_fields.add(val)

# Extract operators (function calls and attributes)

ifisinstance(node, ast.Call):

ifisinstance(node.func, ast.Name):

operators.add(node.func.id)

elifisinstance(node.func, ast.Attribute):

operators.add(node.func.attr)

# Filter out builtins and common script names

builtin_functions = set(dir(__builtins__))

ignore_names = {'alpha', 'np', 'npt', 'data', 'store', 'numpy', 'self', 'universe'}

operators = operators - builtin_functions - ignore_names

# We don't filter data_fields by ignore_names here because

# the user explicitly put them in the decorator list.

# But for safety against 'universe' if they put it there:

data_fields.discard('universe')

return {"operators": list(operators), "data_fields": list(data_fields)}

exceptExceptionas e:

print(f"Error parsing python alpha: {e}")

return {"operators": [], "data_fields": []}

另外其实PYTHON alpha也有一些语法要求的, 有时候会回测失败, 我只是还没测试过.

---

### 帖子 #6: But for safety against 'universe' if they put it there:
- **主帖链接**: https://support.worldquantbrain.comPYTHON alpha的ast解析和语法检查经验分享_40175357844503.md
- **讨论数**: 1

python alpha的语法解析比fastexpr简单太多了. 天生和python适配. 字段也只需要找@alpha的函数变量就可以.

import ast

def parse_python_alpha(code):

"""

Parses a Python alpha script and extracts operators and data fields.

Data fields are strictly extracted from the @alpha decorator's 'data' argument.

"""

try:

tree = ast.parse(code)

data_fields = set()

operators = set()

for node in ast.walk(tree):

# Extract data fields ONLY from @alpha decorator

ifisinstance(node, ast.FunctionDef):

for decorator in node.decorator_list:

# Handle @alpha(data=["..."], ...)

ifisinstance(decorator, ast.Call):

ifisinstance(decorator.func, ast.Name) and decorator.func.id =='alpha':

for kw in decorator.keywords:

if kw.arg =='data'andisinstance(kw.value, ast.List):

for elt in kw.value.elts:

# Support both string literals and constants (Python 3.8+)

ifisinstance(elt, (ast.Constant, ast.Str)):

val = elt.value if hasattr(elt, 'value') else elt.s

data_fields.add(val)

# Extract operators (function calls and attributes)

ifisinstance(node, ast.Call):

ifisinstance(node.func, ast.Name):

operators.add(node.func.id)

elifisinstance(node.func, ast.Attribute):

operators.add(node.func.attr)

# Filter out builtins and common script names

builtin_functions = set(dir(__builtins__))

ignore_names = {'alpha', 'np', 'npt', 'data', 'store', 'numpy', 'self', 'universe'}

operators = operators - builtin_functions - ignore_names

# We don't filter data_fields by ignore_names here because

# the user explicitly put them in the decorator list.

# But for safety against 'universe' if they put it there:

data_fields.discard('universe')

return {"operators": list(operators), "data_fields": list(data_fields)}

exceptExceptionas e:

print(f"Error parsing python alpha: {e}")

return {"operators": [], "data_fields": []}

另外其实PYTHON alpha也有一些语法要求的, 有时候会回测失败, 我只是还没测试过.

---

### 帖子 #7: super alpha combo中operator的使用心得
- **主帖链接**: super alpha combo中operator的使用心得.md
- **讨论数**: 3


> [!NOTE] [图片 OCR 识别内容]
> generate_stats
> 同时做了transpose
> SXDXN
> Choose 1 stat
> multiple States X dates Xalpha:40
> Selection
> NXDXI
> DXN
> Output
> Alphas:40 X dates Xinstruments
> dates Xalphas:40
> combo_a
> group_op: group 只能用 Market, country;
> ts_op
> industry 等
> cross_section_op
> ts_Op
> arithmetic_Op
> CrOSS
> section_Op
> logical_op
> arithmetic_op
> 讦_else
> logical_op: 但是只能判断,不实用
> self_corr -> reduce_Op
> Vec_OP
> 没有 vector data
> Self_Corr
> 理论上应该可以?但是会 take too
> trade_when
> 只能用在 instruments 上
> much resources
> group_op: 只能用在 instruments 上
> vec_op : 没有提示,会直接报错
> 单独的self_
> COTT:
> 维数对不上
> trade_when, if_else: 两个条件要匹配,但是实用
> 单独的 reduce_op: 虽然可以输入 DXN, 输
> 性基本没有
> 出D维;但是光一个 dates 没法和其他
> trade_when(l,alpha,-1) 可以
> operator 搭配
> trade_whenfalpha>Qalpha,o) 不可以;因为alpha
> 和0的dimension 不匹配
> trade_whenfalpha>O;alpha;-alpha) 会卡住
 如图, combo中有两种状态, 
1. alpha: dimension是selection的个数(40为例) x dates x 所有instruments, 是把普通alpha stack之后得到的
2. output: dimension是 dates x selection个数, 意义是某天某个alpha的weight

从第一种状态转换成第二种状态有generate_stats(_)._ 和combo_a(_) 两种方式

其中两种状态能使用的operator是不同的. 如图所示, 有些是因为dimension不匹配, 有些operator是只能使用在instruments上 > <. 操作instrument和state的weight我觉得都是正常的使用方式. 有些像reduce_operator, 我目前看下来只能和self_corr搭配, 感觉使用非常受限

当然这些都是我自己的实验结果和理解, 如果有错误, 希望大家在评论区指正

---

### 帖子 #8: super alpha combo中operator的使用心得
- **主帖链接**: https://support.worldquantbrain.comsuper alpha combo中operator的使用心得_32194005946775.md
- **讨论数**: 3


> [!NOTE] [图片 OCR 识别内容]
> generate_stats
> 同时做了transpose
> SXDXN
> Choose 1 stat
> multiple States X dates Xalpha:40
> Selection
> NXDXI
> DXN
> Output
> Alphas:40 X dates Xinstruments
> dates Xalphas:40
> combo_a
> group_op: group 只能用 Market, country;
> ts_op
> industry 等
> cross_section_op
> ts_Op
> arithmetic_Op
> CrOSS
> section_Op
> logical_op
> arithmetic_op
> 讦_else
> logical_op: 但是只能判断,不实用
> self_corr -> reduce_Op
> Vec_OP
> 没有 vector data
> Self_Corr
> 理论上应该可以?但是会 take too
> trade_when
> 只能用在 instruments 上
> much resources
> group_op: 只能用在 instruments 上
> vec_op : 没有提示,会直接报错
> 单独的self_
> COTT:
> 维数对不上
> trade_when, if_else: 两个条件要匹配,但是实用
> 单独的 reduce_op: 虽然可以输入 DXN, 输
> 性基本没有
> 出D维;但是光一个 dates 没法和其他
> trade_when(l,alpha,-1) 可以
> operator 搭配
> trade_whenfalpha>Qalpha,o) 不可以;因为alpha
> 和0的dimension 不匹配
> trade_whenfalpha>O;alpha;-alpha) 会卡住
 如图, combo中有两种状态, 
1. alpha: dimension是selection的个数(40为例) x dates x 所有instruments, 是把普通alpha stack之后得到的
2. output: dimension是 dates x selection个数, 意义是某天某个alpha的weight

从第一种状态转换成第二种状态有generate_stats(_)._ 和combo_a(_) 两种方式

其中两种状态能使用的operator是不同的. 如图所示, 有些是因为dimension不匹配, 有些operator是只能使用在instruments上 > <. 操作instrument和state的weight我觉得都是正常的使用方式. 有些像reduce_operator, 我目前看下来只能和self_corr搭配, 感觉使用非常受限

当然这些都是我自己的实验结果和理解, 如果有错误, 希望大家在评论区指正

---

### 帖子 #9: Vscode自动提示operator代码优化
- **主帖链接**: https://support.worldquantbrain.comVscode自动提示operator代码优化_33274404140439.md
- **讨论数**: 10

有时候一边写代码一边查opeartor网页会非常打断思路, 我们可以基于自己的 JSON 文档开发一个轻量级的 VSCode 插件，提供 **悬停文档** 和 **自动补全** 功能，用于自定义的 **数据字段** 和 **运算符** ，。

 
> [!NOTE] [图片 OCR 识别内容]
> field-operator-hints
> Welcome
> 1U
> test py
> t
> ts_arg
> Iax
> ts_arg_max(x,
> ts_arg_min
> ts_av_diff
> Time Series
> ts_backfill
> ts
> Returns the relative index of the max Value in the tme
> ts
> Count_nans
> series for the past d days
> If the current day has the max
> ts
> covariance
> Value for the past d days, i returns 0.If previous day
> ts_decay
> linear
> has the max Value for the past d days; j returns
> ts_delay
> ts_delta
> ts_ir
> ts
> kurtosis
> test py
> LCOFr
 

大家可以在vscode搜我编译好的插件试一下.

 
> [!NOTE] [图片 OCR 识别内容]
> EXTENSIONS: MARKETPLACE
> brain_s
> brain_snippet
> 2ms
> Worldquant brain platform datafiel..
> Roshameow
> Restart Extensions
> {
> 氐
 
加载自己的opeartors. 像这样, 在这里添加自己的json路径.

 
> [!NOTE] [图片 OCR 识别内容]
> field-operator-hints
> EXTENSIONS: MARKETPLACE
> Welcome
> package.json
> 田 Extension: brain_snippet
> test:py
> Settings
> 义
> brain_
> Jext:Roshameow field-operator-hints
> Setting Found
> brain_snippet
> 2ms
> User
> Workspace
> Backup and Sync Settings
> Worldquant brain platform datafiel..
> Roshameow
> Extensions (1)
> 品
> Field Operator Hints: Custom Operator JSON Path
> Path to a custom operator JSON file (absolute or workspace-relative path)
> 唱
> 囚


---

### 帖子 #10: What does the relevance mean?
- **主帖链接**: What does the relevance mean.md
- **讨论数**: 0

As I understand so far, the relevance is used to indicated how much chunk is related to theme.

In the workflow demo, no theme is given in searching payload. What does the returned relevance mean in that case 🤔?

---

### 帖子 #11: What does the relevance mean?
- **主帖链接**: https://support.worldquantbrain.comWhat does the relevance mean_39086727531159.md
- **讨论数**: 0

As I understand so far, the relevance is used to indicated how much chunk is related to theme.

In the workflow demo, no theme is given in searching payload. What does the returned relevance mean in that case 🤔?

---

### 帖子 #12: Getting started with Risk DatasetsResearch
- **主帖链接**: https://support.worldquantbrain.com[L2] Getting started with Risk DatasetsResearch_27157459347991.md
- **讨论数**: 15

**Tips for getting started with  [Risk]([链接已屏蔽])  Datasets:**

- Risk factors are variables that influence the returns of assets. Common examples include market returns, interest rates, inflation rates, or industry-specific influences. These factors can be:
  1. **Systematic** : Affecting the entire market (e.g., market returns, interest rates).
  2. **Idiosyncratic** : Specific to individual assets (e.g., company-specific news).
- **Factor Models** , such as the Capital Asset Pricing Model (CAPM) and the Fama-French Three-Factor Model, explain asset returns based on exposure to various risk factors. These models help in understanding the sources of risk and return.
- **Factor Loadings**  (also known as factor betas) measure how sensitive an asset's returns are to these risk factors. They provide valuable information for controlling risk exposure in your Alphas.

**Example Alpha ideas:**

1. Use  `vector_neut(Alpha, factor)`  to neutralize your Alpha's exposure to a chosen risk factor. Iterate over different factors to determine whether your Alpha's returns are influenced by any of them. This approach helps you maintain diversity in your Alpha pool and avoid over-reliance on a few specific factors.
2. To leverage factor loadings and enhance returns, consider the following strategy: During periods of healthy earnings growth, go long on stocks with high loadings on the earnings quality factor. This approach may potentially lead to higher returns by focusing on stocks that benefit from strong earnings quality.

**Recommended Datasets:**

- [Beta Risk Factors]([链接已屏蔽])
- [Multi-Factor Model]([链接已屏蔽])
- [Universal Multi-Factor Risk Models]([链接已屏蔽])
- [Other Multi-Factor Risk Models]([链接已屏蔽])

---

### 帖子 #13: Lab中处理Vector数据的一种方法代码优化
- **主帖链接**: [L2] Lab中处理Vector数据的一种方法代码优化.md
- **讨论数**: 0

这几天使用Lab时发现在可视化Vector数据时会报错，我的方法是定义一些函数，然后在读取原始数据后对Vector数据处理并进行可视化。

**1. 定义函数**

```
def vec_sum(x):    if isinstance(x, (list, np.array):        return np.sum(x)    return np.nandef vec_count(x):    if isinstance(x, (list, np.array):        return len(x)    return np.nandef vec_max(x):    if isinstance(x, (list, np.array):        return np.max(x)    return np.nan
```

**2. 可视化时调用**

```
model_field_df = brain.get_data_frame(brain.get_data_field("close"), universe="TOP3000", dates=[(">", "2021-01-01")]vec_processed_df = model_field_df.map(vec_max)visualizations.plot_values_distribution([vec_processed_df], names=["close values distribution"], nbins=100)
```

函数我只定义了几个常用的，各位可以根据自己的需求扩展。这个方法比较方便，输入一次后未来的代码修改量很小，某种程度也避免了Lab输入的效率低和复制粘贴不方便的问题。

以上就是我的方法，希望能帮助到大家。最后祝各位研究和投资顺利！

---

### 帖子 #14: Lab中处理Vector数据的一种方法代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] Lab中处理Vector数据的一种方法代码优化_33741724514455.md
- **讨论数**: 0

这几天使用Lab时发现在可视化Vector数据时会报错，我的方法是定义一些函数，然后在读取原始数据后对Vector数据处理并进行可视化。

**1. 定义函数**

```
def vec_sum(x):    if isinstance(x, (list, np.array):        return np.sum(x)    return np.nandef vec_count(x):    if isinstance(x, (list, np.array):        return len(x)    return np.nandef vec_max(x):    if isinstance(x, (list, np.array):        return np.max(x)    return np.nan
```

**2. 可视化时调用**

```
model_field_df = brain.get_data_frame(brain.get_data_field("close"), universe="TOP3000", dates=[(">", "2021-01-01")]vec_processed_df = model_field_df.map(vec_max)visualizations.plot_values_distribution([vec_processed_df], names=["close values distribution"], nbins=100)
```

函数我只定义了几个常用的，各位可以根据自己的需求扩展。这个方法比较方便，输入一次后未来的代码修改量很小，某种程度也避免了Lab输入的效率低和复制粘贴不方便的问题。

以上就是我的方法，希望能帮助到大家。最后祝各位研究和投资顺利！

---

### 帖子 #15: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: [L2] Machine Alpha 基础知识1什么是Alpha模板.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #16: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #17: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: [L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #18: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #19: replace 操作符的理解与运用
- **主帖链接**: https://support.worldquantbrain.com[L2] replace 操作符的理解与运用_35191104743447.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #20: [ BRAIN TIPS ] How does regression_neut work ?
- **主帖链接**: https://support.worldquantbrain.com[L2] [ BRAIN TIPS ] How does regression_neut work_9672576065943.md
- **讨论数**: 1

The regression_neut (Y,X) operator conducts a cross-sectional regression on all the stocks in a given universe for the variables Y and X, using the parameters ‘a’ and ‘b’ — creating the final neutralized output of Y-(a+b*X) for each of the stocks in the universe.

Say, you have a dataset with sales and assets for 3,000 USA-listed companies and you want to answer the question: On a particular day, if my company’s assets equal 10, what sales would it have? You look into all the other companies with assets equaling ‘any value’ and their sales happen to be ‘any other value.’ You want to find the dependency between sales and assets and come up with a line provided by regression.

This line is defined as: sales_estimation = a+b*assets, where a and b come from regression by 3,000 points (companies’ sales–assets pairs) on a particular day, and assets are the assets for your company on that day. The regression_neut is sales (actual sales for your company) - sales_estimation (cross-sectional).

Here are a couple of examples of how this idea can be used in your workflow:

- As cross-sectional mean reversion (or momentum) of some value (ratio, returns, etc.) by something related to this value (otherwise b would be 0).
- For orthogonalization to some factors defined by X (similar to vector_neut operator). One popular factor is long price momentum/reversion.

---

### 帖子 #21: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Lucky】为七十二变加上WQB回测配置--进行批量回测经验分享_36864734537879.md
- **讨论数**: 6

72 变是一个十分好用的工具，但是生成的 json 是没有回测配置的

> e.g.

> 
> [!NOTE] [图片 OCR 识别内容]
> 人9OOJIV
>  ]
> ATa_geVe4teU0133101131301
> "group_neutralize (rank(ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry)"'
> "group_neutralize( rank (ts_backfill (workforce_pillar_composite_score,
> 30) ) ,
> industry )
> "group_neutralize (rank(ts_backfill(anl8l_confidence_level_percent , 30)), industry)
> "group_neutralize ( rank (ts_std_dev (mdl177_liqcoeff,
> 21)
> /
> ts_mean (mdl177_liqcoeff
> 126) ),
> industry)",
> "group_neutralize ( rank
> ts_backfill(sustainability_sector_percentile,
> 30) ) ,
> industry)


为了提升回测效率，设计了一个脚本，将七十二变生成的 json转换成成 WQB 能直接回测的带回测配置的json

> e.g.
> 
> [!NOTE] [图片 OCR 识别内容]
> "type"
> 
> IREGULAR"
> settings":
> {
> "instrumentType":
> IEQUITYI
> 11
> "region":
> IND"
> Iuniverse":
> ITOP5OO"
> "delay":
> 1,
> "decay":
> 5 
> Ineutralization":
> IFASTI
> Itruncation": 0.08,
> 'pasteurization":
> ION"'
> ItestPeriod":
> IIPOYOMII
> "unitHandling":
> IVERIFYI
> "nanHandling
> IOFFI
> 11
> "language"
> 
> FASTEXPR"
> IVisualization":
> false
> }
> regular":
> "group_neutralize ( rank (ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry )
> Ivariant":
> "FASTI


设置好回测配置 & 文件输入输出的路径之后，即可生成可直接在 WQB 回测的 JSON。即可批量回测七十二变输出的变体了。

以下是实现代码

```
import jsondef convert_expressions(input_file, output_file, custom_settings):try:withopen(input_file, 'r') asf:expressions=json.load(f)output_data= []forexprinexpressions:alpha_object= {"type": "REGULAR","settings": custom_settings,"regular": expr}output_data.append(alpha_object)withopen(output_file, 'w') asf:json.dump(output_data, f, indent=2)print(f"Successfully converted {len(expressions)} expressions.")print(f"Output saved to '{output_file}'")exceptFileNotFoundError:print(f"Error: Input file not found at '{input_file}'")exceptjson.JSONDecodeError:print(f"Error: Could not decode JSON from '{input_file}'")exceptExceptionase:print(f"An unexpected error occurred: {e}")if __name__ == "__main__":# --- 请在这里自定义参数 ---# --- 以下为示例参数 ---default_settings= {"instrumentType": "EQUITY","region": "IND","universe": "TOP500","delay": 1,"decay": 5,"neutralization": "FAST","truncation": 0.08,"pasteurization": "ON","testPeriod": "P0Y0M","unitHandling": "VERIFY","nanHandling": "OFF","language": "FASTEXPR","visualization": False}INPUT_JSON_PATH='七十二变/输出/文件.json'OUTPUT_JSON_PATH='加上回测配置/文件/的输出路径.json'convert_expressions(INPUT_JSON_PATH, OUTPUT_JSON_PATH, default_settings)
```

---

### 帖子 #22: 【工具优化】华子哥插件的FireFox版本经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【工具优化】华子哥插件的FireFox版本经验分享_34502597199127.md
- **讨论数**: 3

最近因为论坛打开总是出问题，我把主力浏览器从Edge转换到了FireFox。但是FireFox有个缺点就是不支持华子哥的插件，在使用插件功能的时候还要再开一个Edge窗口就非常麻烦，于是我修改了华子哥插件的代码使其兼容了FireFox。

1. 文件下载：

[[链接已屏蔽])

2. 安装方法：

目前FireFox的插件如果要永久安装就要发布到他们的插件商店，为了尊重原作者也为了保护保护国区代码，我选择不发布到插件商店。所以目前还有两个选择，1) 安装FireFox开发者版 2) 每次使用都手动导入一下，我选择的是后者。安装方式如下：

1. 进入菜单 - 扩展 - 左侧选择扩展栏目
2. 点击右上角的齿轮 - 调试附加组件
3. 新页面的右上角点击临时加载附加组件 - 选择下载文件目录中的manifest.json

执行完以上步骤插件就安装成功了。经过测试各种功能均可以正常运行。

FireFox + 科学的方式打开论坛的成功率几乎是100%，这比Edge或者Chrome随缘打开随缘发贴好太多了，建议有论坛打不开困扰的顾问尝试一下这个方案。最后祝大家研究和投资顺利。

---

### 帖子 #23: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 959

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #24: 【日常生活贴】我的量化日记第五季
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第五季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../worldquant brain赛博游戏王/[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #25: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第六季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../worldquant brain赛博游戏王/[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #26: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #27: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: [L2] 【环境配置】在Nvim中配置MCP的方法经验分享.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #28: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【环境配置】在Nvim中配置MCP的方法经验分享_34239307743639.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #29: 选择最先出现的位置  if backfill_index != -1 and backfill_index != -1:            cut_index = min(backfill_index, backfill_index)
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何统计得到的字段数如何抓取多地区因子一起检验代码优化_28754183939351.md
- **讨论数**: 1

1、如何得到字段数分布

我们在二，三阶段之前都会拉一下待处理的因子，并对字段进行减枝操作。但是如果我们回测的是多个数据集，甚至是多个category，模版中给出的代码就不适用了。为了解决这个问题，我小修了一下代码，如下：

def extract_fields(next_alpha_recs):

field_counts = defaultdict(int)

for rec in next_alpha_recs:

# 提取完整字段名

full_field = rec[1]

# 找到 winsorize 或 ts_backfill 的位置

#winsorize_index = full_field.find('winsorize(')

backfill_index = full_field.find('ts_backfill(')

end_index=full_field.find(', 120')

# 选择最先出现的位置

if backfill_index != -1 and backfill_index != -1:

cut_index = min(backfill_index, backfill_index)

elif backfill_index != -1:

cut_index = backfill_index

elif backfill_index != -1:

cut_index = backfill_index

else:

# 如果没有找到这两个关键词，跳过此记录

continue

# 提取字段名（cut_index之前的部分）

field_name = full_field[cut_index+12:end_index].strip()

field_counts[field_name] += 1

这段代码需要再

fo_tracker = get_alphas("12-13", "12-24", 1.25, 0.7, "KOR", 1500, "track")（举个例子，可以换）后边直接使用，其输出是一个字典，key是字段名，value是次数/个数。（注意，对于向量类型，可能需要把向量的运算符，vex_avg这种放到筛选条件中）

最后会输出类似这样的图：


> [!NOTE] [图片 OCR 识别内容]
> {'rsk7o_mfmz_asetrd_earnyild'
> 365,
> 'volume
> 25,
> adv20
> 274,
> VWaP
> 171,
> 'high
> 37,
> IOW
> 76_
> open
> 36,
> oth466
> bs assets
> curr_q': 1
> fndl7_nprice
> 37,
> Cap
> 9,
> fndz7_volldavg
> 259,
> cash St
> dividend
> 3,
> fndl7_priceavglsoday '
> rsk7o_mfmz_asetrd_srisk
> cash
> 1
> oth466_cf_dps_secs_q': 1,
> fndl7_apricezbk'
> 1
> rsk7o_mfmz_asetrd_invsqlty'
> rsk7o_mfmz_asetrd_anlystsn
> fndl7_gihn
> assets
> CURr
> fndl7_qrecturn
> 45,
> oth46G_is_ebit_oper_q'
> 1
> oth466
> q_ngm_xtp_tr'
> 1
> Oth466_bs_cash_st q'
> 80,
> CIose
> 54}
> 53,


根据次数和个数，可以决定减枝的个数，如下：

def prune_second_order(inputdata,all_dict):

#inputdata是对象，dict是次数统计

th_tracker1=inputdata.copy()

#print(len(th_tracker1))

for i in all_dict.keys():

#print(all_dict[i])

if all_dict[i]>100:

a=prune(th_tracker1,i,1)

if all_dict[i]<=100 and all_dict[i]>50:

a=prune(th_tracker1,i,2)

if all_dict[i]>10 and all_dict[i]<=50:

a=prune(th_tracker1,i,2)

# if all_dict[i]<=10:

#     a=prune(th_tracker1,i,7)

#th_tracker1=a

return a

def prune(next_alpha_recs,prefix,keep_num):

output = []

num_dict = defaultdict(int)

for rec in next_alpha_recs:

exp = rec[1]

field = exp.split(prefix)[-1].split(",")[0]

sharpe = rec[2]

if sharpe < 0:

field = "-%s"%field

if num_dict[field] < keep_num:

num_dict[field] += 1

decay = rec[-2]

exp = rec[1]

output.append([exp,decay])

return output

这里面个数也是可选项，可以根据数据特性进行筛选。

2.如何同时抓取不同地区的因子进行回测？

def get_submitable_alphas(start_date, end_date, sharpe_th, fitness_th,turn_over, region, alpha_num, usage):

s = login()

output = []

# 3E large 3C less

sharpe_th1=sharpe_th

count = 0

for re in region:

if re=='CHN':

sharpe_th=max(sharpe_th,2.1)

else:

sharpe_th=sharpe_th1

for i in range(0, alpha_num, 100):

print(re,i)

url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2024-" + start_date  \

+ "T00:00:00-04:00&dateCreated%3C2024-" + end_date \

+ "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \

+ str(sharpe_th) + "&settings.region=" + re + "&order=-is.sharpe&hidden=false&type!=SUPER"

url_c = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2024-" + start_date  \

+ "T00:00:00-04:00&dateCreated%3C2024-" + end_date \

+ "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \

+ str(sharpe_th) + "&settings.region=" + re + "&order=is.sharpe&hidden=false&type!=SUPER"

urls = [url_e]

if usage != "submit":

urls.append(url_c)

for url in urls:

response = s.get(url)

#print(response.json())

try:

alpha_list = response.json()["results"]

#print(response.json())

for j in range(len(alpha_list)):

alpha_id = alpha_list[j]["id"]

name = alpha_list[j]["name"]

dateCreated = alpha_list[j]["dateCreated"]

sharpe = alpha_list[j]["is"]["sharpe"]

fitness = alpha_list[j]["is"]["fitness"]

turnover = alpha_list[j]["is"]["turnover"]

margin = alpha_list[j]["is"]["margin"]

longCount = alpha_list[j]["is"]["longCount"]

shortCount = alpha_list[j]["is"]["shortCount"]

decay = alpha_list[j]["settings"]["decay"]

exp = alpha_list[j]['regular']['code']

count += 1

if (longCount + shortCount) > 50 and turnover<turn_over and 'eeps_nxt_yr' not in exp:

if sharpe < -sharpe_th:

exp = "-%s"%exp

rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]

output.append(rec)

except:

print("%d finished re-login"%i)

s = login()

sleep(2)

print("count: %d"%count)

return output

这个是比较直白的一种方式，给出不同地区，写成循环，按照sharpe，fit，turnover进行筛选（筛选也可以按照个人状况调整，但是抓取的个数一个地区不能超过10000）。

使用示例：

supertracker=get_submitable_alphas('12-15', '12-24', 2, 1.1,  60,['CHN','KOR','ASI','JPG','HKG','GLB','AMR'],1500, 'submit')

---

### 帖子 #30: 这个因子到底能不能交？（下） 【传奇耐打王系列一】
- **主帖链接**: https://support.worldquantbrain.com[L2] 这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md
- **讨论数**: 24

上一篇在这： [[L2] 这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md-这个因子到底能不能交-上-传奇耐打王系列一]([L2] 这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md)

刚刚更新的combine证明我的思路大体应该是正确的：


> [!NOTE] [图片 OCR 识别内容]
> AIP
> Nmno tAl
> NIONI a(T
> C-IrTIITTSC
> T ATIHII
> UMTNTTIRNT21V
> Eligibility Criteria
> O
> CFen
> U
> Cn
> SIgnL
> 1Tn7IFrrort
> Fymmids Complsted
> IUs ULCIL
> ThITPI
> Wha FeTormaTCe
> 2.15
> CLemmm
> Combinod Soloced Aloh Prrtormancn
> mch Tocmo
> Combined Power PolMlpha Partormanco
> 2.22


那接下来我们就继续讨论啦！

说完了必须指标，我们该讨论优化指标了。优化指标就是在完成必须指标的基础上好中选优，位次越靠前优先度越高：

1.低相关（先pc后（sc或ppac））

2.sharpe和fitness的21年和22年优秀

3.sharpe和fitness逐年优秀

4.margin的21年和22年达标

5.margin的逐年达标

6.margin的21年和22年优秀

7.margin的逐年优秀

8.margin和return越高越好

9.turnover围绕在12%

10.drawdown越低越好

11.多空优秀

这里大家可以看到，我把低相关放到了第一位。首先，为什么追求pc低。很多时候我们都说，pc低可遇不可求，所以我们先拿准自己的池子，对sc做出要求。这里我们可以类比，每个人的池子是小池子，你提交上去的池子是世坤的池子，是大池子。你想把sc降低，那世坤也想把属于他的sc（pc）降低呀。

鑫佬名言：你做了别人没做过的（pc低），这对于世坤来说，就是杰出的贡献。

为什么说base主要看pc，这就是世坤衡量你贡献的主要指标。

在pc足够低的情况下，我认为可以相对忽略更优质的指标，优先选择pc低。

鑫佬名言：pc0.5以下就是极品，0.3以下已经是极品中的极品。

我当时交了一个0.2几的pc，是我成为有条件顾问后单日base首次破3。

以下举例一个我最近刚交的ra：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> N3ILT
> RrsNR
> CTTTILaU
> FTIIIFFTINT
> mII
> ARUNOMNUATI
> 2.29
> 5.419
> 3.813
> SE沾
> 11.8993
> IsT0
> TT
> OS
> T
> TCo
> 4A191
> hMre
> T
> 071T21 「T
> R7111
>  kg4
> UItot
> at
> N
> Chart
> I'Est HillT' Cnstrimer
> ATIMAI
> _匕
> 0.,76
> 904
> 7.18N
> 12,58m
> Correlation
> IoLC
> CALT219
> PI
> C-~TAIOI[
> Testing Status
> I1 FENCINL
> PdCrIalon
> ITu SuIinoII
> 0.3656
> 0.3925
> n]T


毫无疑问，赚的多而且对vf和combine有极大的帮助

再次强调，一定要满足基础要求！基础要求不满足不要看pc！

但我还在论坛里看到另外一个ppa大佬的经验分享（具体一下子找不到了，在这里对您表示感谢）：pc高说明什么？说明交的人多。交的人多从概率上说明这个因子值得信赖，否则为什么别人看到了高相关还交呢？我觉得这也是有道理的。

因此我觉得pc是一个很主观的东西，就是每个人心中要有符合自己个人的阈值。我一般不会在官方要求上再加一个自己的高要求（比如有的大佬pc0.6以上就不交），但对于一个小白来说，我还是更加重表现，比如下面这个ppa，也是我最近交的：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> N3ILT
> 41+7891757
> CTTTILaU
> TITH
> UAUTUUNUCOAL/
> SINVJaVIOC
> 3,33
> 5.354
> 6,115
> 1.253
> 24%
> 5T4
>  
> U4
> 11443
> OV
> 47
>  Hr
> TI7r
> TSITaln[
> Uge
> 2
> 7
> Ct
> Chart
> Ie? O
> CUIISISTIP
> AIreMLOu
> HD
> 二 FSI
> 15
> 4.975
> 1.719
> 1T
> Correlation
> Iron TT7
> 0.2975
> ~0.1253
> 05 Testing Slalus
> 1CTllsn
> PeOI
> UIIICI CI
> L u
> AMm。I IL
> 09065
> 0,4723
> 941451
> 247


虽然pc非常高，但是表现我很认可，再加上sc也不错，对于我的池子有不小的帮助，我会果断地提交它。

也有人问我sc的阈值，说实话，我也是按照官方的来的。甚至有时候，我会因为sharpe提高百分之十而提交不满足pc或者sc的因子，这都是需要根据表现来进行考虑的。

这里我详细解答为什么我会提交这样的因子。首先，提交这样的因子对combine的帮助很可能是负的。但是对于vf而言，如果你觉得这个因子你稳赚，那提交了就是正的收益。可能对于这个时期的我，我的目标是优先冲击vf高，所以为了收益我希望我有更多稳定赚的因子，所以我会提交。这是对于我个人现阶段的影响之下我的选择。

这里说一个我建议的阈值，我在组sa时发现，sc控制在0.55到0.6时往往可以实现因子的表现最大化。所以我觉得如果你要设置一个个人的sc阈值，0.6就已经很好了。对于像我一样的大部分小白，只跑一二三阶，我们能挖到低相关是存在很大一部分的运气成分。如果把阈值设置的太低，会导致我们无法提交足够数量的因子。数量同样也是一个重要的维度，因此我不建议自己设置太低的阈值。

在讨论接下来的指标之前，我先对这个顺序做解释。为什么sharpe和fitness在margin和return之前？因为稳定是一个因子非常非常重要的因素！！！划重点！！！

游戏王名言：因子一定是先稳而后赚。

我们的基础要求中有一个margin达标，margin达标说明已经能大概率赚钱了。接下来我们的目标就是要让因子稳定赚钱。稳定赚钱的因子我们称之为“印钞机”。我可以允许我一次赚的不多，但我一定要一直赚！！！稳定赚钱的因子对于vf和combine的帮助是超级大的。

接下来我们来说指标。我都是先写21年和22年表现好，而后才是逐年表现好。大家都希望逐年表现好。但除非顶尖高手我们都做不到逐年都好。因此关注最近两年是很重要的。为什么因子会不断地挖出来，不断地退役，就是因为因子具有时效性。这个因子现在在市场里如鱼得水，说不定半年后就变成错误信号了。最近两年的信号相对之前的几年肯定是最具有参考性的。如果有个因子前面表现很不错，然后最近两年开始下滑，我个人认为这是很需要警惕的。下面是我的例子：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> UT7-GS
> Nnu nul
> Cn R
> UTGI
> nNRA
> RrsNR
> CTTTILaU
> rT NTI,
> FFMIpm'
> U-mrsl
> C UIJL
> Code
> 15 Summary
> NTINTT 
> 4.80
> 34.91N
> ,46
> 39
> 1=
> SIIUOUI
> Uat
> T
> M
> 3
> Tmo
> T
> sa
> Cno Alah
> Chart
> Hls:naUtrallzed
> CVEU
> 3.519
> 10.829
> SO
> 6,20650
> Isbahilf' canstiner
> ATINCICTT
> F Lutuleer PnL
> In aImt CrsTJIIEIFT
> 26.299
> 8.425
> 3.399
> 6.4190
> Correlation
> 15 Testing Status
> eLCTrlotlc
> yr
> otm


这是我挖出来的一个ra，乍一看，基础要求都满足，sharpe和fitness还高的离谱。但是我们细看21年和22年，这两年的margin从合格走向不合格。用大家常说的一个词叫做：圆顶。这种就是圆顶因子我们看不到它往上增长的趋势了。对于usa地区而言，这几年行情好，很多因子都是翘头趋势。这个因子反而是圆顶。对此，只能说等到os更新的时候，对这个因子再次回测，看看这个因子到底跑的怎么样。现阶段肯定是不建议提交的，亏钱的几率非常的大。

所以，如果指标不是年年好，那就专注21年和22年。

游戏王名言：好的因子不应该受到任何特定事件的冲击，比如20年的疫情。

如果实在不能平滑向上，那就优先翘头而不是圆顶。

那什么才叫年年好呢？

从13年开始就有数据的，delay1的地区（我才刚开始尝试d0在此不做判断），对于sharpe而言，都大于1已经很不错了。有的人会问：是否允许有负的sharpe？我个人是允许的，只要不要发生在21年和22年。同时，负的幅度不要太大，一般就是-0.5以内。但凡比较大的负值，pnl看起来都会有些抽象，已经不满足我们的必须指标中的“pnl平滑”了。还有的人会说：这个因子有几年只有零点几的sharpe，能接受吗？这个时候最好的办法就是看这几年的margin。如果margin在这几年依旧达标，说明这个因子表现不是特别好、信号不是很强的时候依旧可以赚钱，那这个因子是值得肯定的。

可是有很多这样的问题：这个因子从18年开始才有数据，数据很漂亮，能不能交？

我的建议是，数据覆盖不超过8年的，都尽量不要交。意思就是，最多允许从15年开始有数据。

但这里提到一点，weijie老师在因子模版的帖子里的一个评论针对snt27的模版的有提到，观察数据更新频率，不失为一个好的因子。这里我只能说高手仁者见仁了。Snt27我至今都存着没敢交。

游戏王名言：如果你十年是逐年大于1，那5年是不是起码得逐年大于2？这甚至还只是一个下限，实际应该更加高。

我的建议就是，你把下面的滑动窗口视图拉大到有数据的那几年看看，是否符合我前面提到的必须要求？举例来说：


> [!NOTE] [图片 OCR 识别内容]
> UTTRA
> rJuno
> CTtR
> UTLIT-GU
> UTrt
>  TTTT
> 「
> TTIIFFI
> Coce
> Summar
> TJlI?N
> UII
> GRs
> ATIIIL
> 2.979
> 1.73
> 8.77%
> 3.41沆
> 59 C19
> T
> L
> UaS
> T
> N
> Rm
> 449
> ao
> U
> 5TIII
> |!$
> [
> Lsoaar
> 。
> Cna AI I
> Chart
> TII 51
> Ris eulnllied
> 295
> 4.4
> 265 
> 29.933e
> Inrestabllity
> CUIISITIIP
> 91 TTrPML
> IThIm CrrTIAHFm
> 2.843
> 909
> 3.809
> 55.56e
> Correlation
> IS Testing Status
> Tl Crrlalc



> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> O0OK
> UOOK
> Mayq
> Sep"19
> Nay 20
> Jan 
> lan 22
> Sop22
> Jan'23
> PnL
> RIsk Neutralized Pn
> Investability Constraned Pn
> Sep
> May
> Ser
> Na


拉大之后，我们能看到这个pnl并不是很平滑，而且也是圆顶的（其实指标也看的出来），这个因子就不值得信赖了。

接下来我们来解析turnover。Turnover为什么不是越低越好？反而是维持在12%？这里我们要强调一个点。股票、期货等等，我们追求的是一个对冲的思想。我们通过合理的做多做空，来实现对市场变化的应变。大家可以理解为，如果我的turnover非常低，只有百分之一点几，那这只股票基本上一年下来就不交易多少次，更多的就变成了极其稳定的持仓，这和对冲流动的思想是相违背的。

游戏王名言：turnover很低的因子，我都不知道它赚的是什么钱。

Weijie老师名言：turnover 5%以下的因子，都是“死鱼”因子。

你要问这个12%的标准怎么来的，说实话我也不知道，就像各个地区的margin最低标准一样，我也不清楚怎么算出来的。但我们把turnover控制在一个良好的范围，就是为了能让因子的表现更加稳定（这也是出自一位大佬的总结，名字我也给忘了，在这里表示道歉和感谢）。其他表现几乎一致的情况下，能积极对冲的因子一定会比死鱼因子更加值得信赖的。

于我个人的理解，就是一般情况下控制在5%以上20%以下都是ok的。每个人可以根据自己的需要进行调整。什么叫进行调整？以我自己为例，我一开始做usa的时候，交了非常多换手率只有百分之一点几的超级死鱼因子。当时我的想法就是为了尽可能拔高margin。后来我意识到这种想法是错误的时候，鑫佬建议我提交一些换手率较高的因子来使combine的表现获得提升，因此接下来我就交了不少margin只有万分之五到十，但是turnover有20%到30%的因子。大家可以理解为我用刚刚达标的因子着重的提高turnover了。但这只是权宜之计，并不是值得学习的行为。

那有的兄弟会问，对于高换手的主题呢？

这里我必须得和大家讲述一下turnover和return，margin的关系。

我们都说，这是一个跷跷板，return一定，turnover越高margin越低。对于超高换手率，比如40%到50%，如果你的return一样可以做到40%，那我觉得这个因子你提交完全ok的，这一定是一个不错的因子。但如果你的return只有15%，换手率还如上，那我觉得这就是一个亏钱因子了。为啥换手率高会亏钱？因为每一次换手都有手续费呀。换的越多手续费越多。你的因子赚的钱都不够交手续费，那只有亏钱的道理。

但是对于死鱼因子，我自己有一个不太一样的看法。在你对于一个因子的质量实在是拿不准的时候，死鱼因子就是一个很好的提交方式。你通过把turnover压得很低来大幅度提高margin，让因子的样本内表现看起来相对还可以。同时，由于是死鱼因子，搞笑一点来说，就算是亏钱因子，也亏不了多少钱，因为你的因子几乎不交易（令人哑然失笑）。因此，换手率极低并非完全不可取，还是那句话，你需要依你自己的情况而定。

对于drawdown这个指标，没有什么特殊的情况，肯定越低越好。但大家肯定遇到过下面这个样子的因子：


> [!NOTE] [图片 OCR 识别内容]
> U Cr RAI
> Irto  Iy
> Nnu nul
> Cn R
> UTGI
> nNRA
> RrsNR
> CTTTILaU
> FTIIFFI711
> CTmNSI
> Coce
> Summary
> CUIT
> JIJV
> 41I1TNIMaAINTaL .
> MIMTII
> GR
> Aret?uU
> 22
> 2.45
> 21,91%
> 11459
> 59,49mm
> 16
> T
> Las
> T
> N
> Ro
> 14
> 2
> 
> [
> Lnear
> !
> TI TM
> Oo 
> 41
> Chart
> Jg
> Ta
> 
> Hsk MeULTAUIZEU
> 0.54
> 833%
> 11.055
> 2263-0
> Iet F
> OITTTTTPI
> AIrotdteDu
> 3.29-0
> 16.409
> 15.213
> 99747
> Correlation
> Os Testing Status
> Corlalc
> 1


这个因子的drawdown很高，都有百分之十了，这时候我们到底如何考虑呢？

我个人的建议就是：return覆盖drawdown，margin覆盖turnover

只要return比drawdown高，margin比turnover高，我觉得可以尝试。比如我这个因子，return20%以上显著大于turnover，这个是没问题的。

当然，这个因子大家能看到，多空并不是特别平衡。明显做多大于做空。所以这个因子赚的是多头的钱，相较于其他的多空平衡的因子就不是那么稳定了。

那到底多空要怎么看呢？这里我们也分三个点，这三个点平行考虑，不分先后。对于多空都很重要：

1. 多加空能覆盖universe是比较好的
2. 多基本上等于空
3. 多空不要浮动变化。什么是不要浮动变化呢？举例来说，比如TOP3000的universe，一个因子，一开始多空都是九百到一千，过了两年变成一千五到一千六，过了两年变成九百到一千。这说明这个因子选股经常选到具备某些特征的股票，这些股票不是每次都可以挤到TOP3000，挤进去的时候多空就拉起来，挤不进去就下降。相对来说稳健性依旧比不上多空不浮动的因子

所以我刚刚举例的这个drawdown很高的因子，几乎三点都不满足。不过就像排序一样，多空只要不是赌博，就可以放在最后考虑。问题不大（自我安慰）。

看到这里肯定很多朋友有疑问了。传奇耐打王难道不看performance comparison吗？

肯定要看的，接下来我们就来详细解析这个该怎么看。

答案：同优化指标。

意思就是，并不是说真的是“四绿两红”才能交，也不是“四绿中的至少两绿”才能交。判断逻辑与之前是一致的。首先sharpe和fitness肯定越高越好，但如果一个加一个减怎么办，那就算净值，净值更优的排更靠前。我基本上只重点关注这两个值，对于return和margin，只要持续保持达标以上，我觉得加加减减并不关键。还是游戏王那句话，我们要的是——稳赚！！！同理，turnover保持12%浮动，drawdown尽可能降低（偶尔有的因子拉起来一点问题都不大）。所以，这个performance comparison我觉得并不是判断的关键。下面拿一个因为performance comparison阻止我提交的因子举例：


> [!NOTE] [图片 OCR 识别内容]
> INm
> 2,30
> 643
> 2]
> 357泗
> 66
> 11.10
> 7 e
> ol4e
> 
> Tag
> N
> TU
> NU TCtCn
> 0+
> gse
> 28
> Cen Nohe
> Chyrt
> IntlCnnrlrai-
> AAIIOIAI』
> 4,033
> 2.769
> 2,384
> 13.6954
> Te LLIIy CrIoTsUF
> Correlaton
> 944』!


这个因子看起来都挺漂亮的，是一个ra，但是我的performance comparison显示是全红（真的心碎）。因此这个因子我最终放弃了。

大家不要觉得我粘贴出来的因子看起来质量都不错。我自己也交了不少sharpe只有不到1.3，fitness0.5出头的ppa，这些都没有绝对的标准。还是那句话，看你自己的需要。对于提交因子这件事情，大家一定要管得住自己的手，在保持理性的前提下，再做提交的思考。毕竟我们为的不是那一天得多少base，而是为了未来的每天都有更多base。

以上是对于因子提交的优化指标的讨论。到此这个系列暂时就完结了。如果对您有帮助，请留下您宝贵的赞。

如有不正之处，恳请佬们批评指正。大家有什么问题，或者还有什么没有归纳到位的地方，都可以在评论区留言提出。或者你带着你的因子截个图放到评论区，问问传奇耐打王能不能交，我也是非常乐意解答的。

最后祝大家都能vf1.0，combine节节高。

---

### 帖子 #31: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [图一乐] osmosis rank对乘数的影响.md
- **讨论数**: 2

其实乐不出来...

新乘数的算法是: (原来的乘数) x (1+osmosis rank)

比如我的alpha theme乘数=2, pyramid乘数=1.1, osmosis rank=0.45 alpha的乘数就是(2.1)x1.45=3.04

如图所示


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Daily
> Factor
> Factor
> Osmosis
> 芒
> Rank
> 顾问 顾问 WL27618 (Rank 97) (Rank 97) (Me)
> 21.80
> 0.91
> 0.45



> [!NOTE] [图片 OCR 识别内容]
> Effective pyramid count for Geniusis 2。
> These themes match with the following multipliers: EUR TOPCS1600 Theme
> 2; EURIDIIFUNDAMENTAL Pyramid Theme
> 1.1. The final theme multiplier is
> 3.04


---

### 帖子 #32: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[图一乐] osmosis rank对乘数的影响_38423873285655.md
- **讨论数**: 2

其实乐不出来...

新乘数的算法是: (原来的乘数) x (1+osmosis rank)

比如我的alpha theme乘数=2, pyramid乘数=1.1, osmosis rank=0.45 alpha的乘数就是(2.1)x1.45=3.04

如图所示


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Daily
> Factor
> Factor
> Osmosis
> 芒
> Rank
> 顾问 顾问 WL27618 (Rank 97) (Rank 97) (Me)
> 21.80
> 0.91
> 0.45



> [!NOTE] [图片 OCR 识别内容]
> Effective pyramid count for Geniusis 2。
> These themes match with the following multipliers: EUR TOPCS1600 Theme
> 2; EURIDIIFUNDAMENTAL Pyramid Theme
> 1.1. The final theme multiplier is
> 3.04


---

### 帖子 #33: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【Community Leader -因子筛选与组合】本地数据库的使用筛选代码优化_36682316922135.md
- **讨论数**: 12

在成为新顾问的阶段, 一个很具体的问题就是: 究竟有没有必要建立一个本地的数据库存放和筛选回测过的alpha呢?

虽然平台的  [[链接已屏蔽])  功能已经提供了众多的筛选条件, 随着回测alpha变多, 还是有一些筛选功能是没覆盖到的, 每次都抓耳挠腮感觉自己的alpha失踪了.

下面我分享一些我自己经常使用的一些数据库筛选功能, 如果需要这些 **额外** 的功能, 结论就是 **需要建立一个本地的alpha数据库** .

 
> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> Search Regular
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 00
> Max Turnover (%^
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> eT
> Sharpe
> Created
> #
> priority_
> #Kq2WpqNP_sign_turnover_
> priority
> Xg533dJl
> ASI
> 1.32
> 1.21
> 10.45%
> 4.37%
> 47.86%oo
> 0.94
> 2025-11-30
> LOW_SHARPE UNITS,IS_LADDER_SHARPE,MATCHES
> #
> _priority_
> #Kq2WPqNP_sign_turnover
> priority
> npMjjLKM
> ASI
> 1.27
> 1.16
> 10.38%
> 4.56%
> 45.52%o。
> 0.92
> 2025-11-30
> LOW_SHARPE LOW_2Y_SHARPE,MATCHES_THEMES
 

这是我的筛选界面, 比较常用的有4个功能

1. **表达式的部分匹配**
2. **alpha id**
3. **距离今天多少天之内**
4. **is check具体条件**


> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计算 Co
> oth
> I0
> Region
> Delay
> Days Before
> Min Turnover (96
> Max Turnover
> 0?
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> Turnov
> Margi
> Sub-U
> Date
> Regular
> I0
> Message
> Pnl
> BI
> Sharpe
> Created
> ts_target_tvr_delta_limit(sign(filter(ts_max(sqrt(ts
> ZYeQ35ZX
> JPN
> 1.06
> 0.71
> 5.56%
> 3.11%
> 35.699oo 1.02
> 2025-11-28
> LOW_SHARPELOW_FITNESS UNITSIS_LADDER_SH'
> 查看
> ts_target_tvr_decay(ts_returns(ts
> max(-1/ts_back。。
> gJEgWaZe JPN
> 1.02
> 0.61
> 4.49%
> 9.14%
> 9.82%。
> 0.82
> 2025-11-27
> LOW_SHARPELOW_FITNESS CONCENTRATED_WEIC
> 查看
> #_priority_
> #POJpWggL_operator_transfer
> prior..NIvGkSkW
> GLB
> 1.49
> 0.76
> 4.59%
> 17.44%
> 5.26%oo
> 1.06
> 2025-11-25
> LOW_SHARPE LOW_FITNESS,LOW_GLB_EMEA_SHAI
> 查看



> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> oth515_is_open
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 91
> Max Turnover
> 0
> Min Margin (%oo)
> Min Return (%oo)
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> Sub-U
> Date
> Regular
> I0
> Message
> P
> eT
> Sharpe
> Created
> ts_target_tvr_delta_limit(sign(filter(ts_max(sqrt(ts。
> ZYeQ35ZXJPN
> 1.06
> 0.71
> 5.56%
> 3.11%
> 35.69%o。 1.02
> 2025-11-28
> LOW_SHARPELOW_FITNESS,UNITS,IS_LADDER_SHI



> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计算
> tS
> COTr
> I0
> Region
> Delay
> Days Before
> Min Turnover
> 00
> Max Turnover (%~
> Min Margin (%oo)
> Min Return (9ool
> Exclude Messages
> Include Messages
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> Pnl
> eT
> Sharpe
> Created
> signal = scale(ts_corr(adv2O,low; 5) +(hightlow)l2-
> LKZ3rpM EUR
> 90
> 3.39
> 1.29
> 10.95%
> 75.42%
> 2.90%oo
> 1.8
> 2025-05-05
> LOW_FITNESS,HIGH_TURNOVER UNITS,UNITS,MATC
> 查看
> signal = scale(ts_corr(adv2O,low; 5) +(hightlow)l2-.
> 5JjbZ5z
> EUR
> 90
> 3.39
> 1.29
> 10.95%
> 75.42%
> 2.90%oo
> 1.8
> 2025-05-05
> LOW_FITNESS,HIGH_TURNOVER UNITS UNITS MATC
> 查看
> CC
 
表达式可以直接查找任何前缀, 字段, operator


> [!NOTE] [图片 OCR 识别内容]
> alpha_results
> 计
> Search Regular
> I0
> Region
> Delay
> Days Before
> Min Turnover
> Max Turnover (%;
> LOW_ROBUST_UNIVERSE_SHARPEWITH_RATIO
> IS_LADDER_SHARPE
> Min Margin (%oo)
> Min Return (%oo)
> REVERSION_COMPONENT
> LOW_2Y_SHARPE X
> Regio Scor
> Sharp
> Fitnes
> Return
> TurnoV
> Margi
> SUb-U
> Date
> Regular
> I0
> Message
> Pnl
> eT
> Sharpe
> Created
> 3 =
> signed_power(ts_product(to_nan(ts_backfill(V
> XAKw3xpn GLB
> 3.76
> 2.3
> 4.67%
> 8.49%
> 11.0O%oo 2.1
> 2025-10-03
> REVERSION_COMPONENT MATCHES_THEMES
> 查看
> tail(-(ts_backfill(close, 252)
> last_diff_value(ts_ba.j2vaWP7e IND
> 3.29
> 1.9
> 20.24%
> 60.71 %
> 6.6790。
> 1.91
> 2025-11-02
> HIGH_TURNOVERREVERSION_COMPONENTMATCH
> 查看
> signal
> group_neutralize(ts_median(-vec_avg(rsk. Vkvwapbo GLB
> 2.87
> 3.29
> 16.43%
> 9.09%
> 36.15%o。 2.31
> 2025-10-03
> REVERSION_COMPONENT MATCHES_THEMES
> 查看
> signal-ts_backfill((vec_avg(anl6g_best_target_hi) ).
> gXRQoke
> EUR
> 87
> 2.63
> 1.84
> 8.75%
> 17.79%
> 9.84%o0
> 1.6
> 2025-05-30
> CONCENTRATED_WEIGHT REVERSION_COMPONEN
> 查看
> signal-ts_backfill((star_Val_pcf), 252);combined_si.
> 0R5pQ7g
> EUR
> 90
> 2.43
> 1.64
> 8.66%
> 19.04%
> 9.09%o。
> 1.33
> 2025-05-29
> REVERSION_COMPONENT
> 查看
> 十 C
> C3701C+3
> 0C
> CS+
> OC+'mS+o
> f1 IICo
> N1
> 1Cc
> C?
> 0101
> C00
> 4Col
> nC
> C


is_check也是经常需要的筛选条件.

如果有人需要我用的这个, 链接🔗是;  [[链接已屏蔽])

我的后端和mongodb是深度绑定的.

---

### 帖子 #34: 分享一下我的eltwise operator变换分类经验分享
- **主帖链接**: 分享一下我的eltwise operator变换分类经验分享.md
- **讨论数**: 9

eltwise operator顾名思义就是不管time-series, cross-section两个维度的相关性, 只依赖每天每instrument 的value进行变换的operator, 它们的作用有:
1. 调整分布, 控制我们信号的weight.
2. 降低相关性, 当我们进行非线性变换时就会自然的降低相关性
3. 在主信号不变的情况下, 把operator变为相似的平滑/离散版本, 从而控制信号的turnover. (这也是我在手调alpha的时候经常遇到的问题, 有时候信号因为不连续产生很多没必要的turnover, 那么换成连续的版本就能解决部分问题. )
4. 通过压缩或放大某段value, 找到alpha中起关键作用的部分.

下图我分享一些按我的习惯分类的operator, 在保证单调性的前提下, 对信号进行变换. 我是考虑尽量使用平台本来就有的operator, 以及尽量保持变换的多样性.

 
> [!NOTE] [图片 OCR 识别内容]
> Distribution Operator Groups Visualization
> Xin (0,inf) - yin (-inf, inf)
> -1/<
> Iog(x)
> Sqrt()
> X- 1/x
> Xin (-inf inf)
> in (0,inf)
> exp(x)
> Iog(l+exp())
> Tax(uo)
> Sigmoid(x)牛x
> Xin (-inf inf) - Yin [ 1, 1]
> arctan(x)
> tanh(x)
> clamp(y -11)
> Sign(x)
> Xin (inf inf)
> yin (infinf)
> signed
> Power( 0 2)
> log_Ip(x)
> Signed_DOWer(u0 5)
> tail(x-11)
> signed_power(xrz)
> Power(3)
> signed
> power(kr5)


---

### 帖子 #35: 分享一下我的eltwise operator变换分类经验分享
- **主帖链接**: https://support.worldquantbrain.com分享一下我的eltwise operator变换分类经验分享_35458200184471.md
- **讨论数**: 9

eltwise operator顾名思义就是不管time-series, cross-section两个维度的相关性, 只依赖每天每instrument 的value进行变换的operator, 它们的作用有:
1. 调整分布, 控制我们信号的weight.
2. 降低相关性, 当我们进行非线性变换时就会自然的降低相关性
3. 在主信号不变的情况下, 把operator变为相似的平滑/离散版本, 从而控制信号的turnover. (这也是我在手调alpha的时候经常遇到的问题, 有时候信号因为不连续产生很多没必要的turnover, 那么换成连续的版本就能解决部分问题. )
4. 通过压缩或放大某段value, 找到alpha中起关键作用的部分.

下图我分享一些按我的习惯分类的operator, 在保证单调性的前提下, 对信号进行变换. 我是考虑尽量使用平台本来就有的operator, 以及尽量保持变换的多样性.

 
> [!NOTE] [图片 OCR 识别内容]
> Distribution Operator Groups Visualization
> Xin (0,inf) - yin (-inf, inf)
> -1/<
> Iog(x)
> Sqrt()
> X- 1/x
> Xin (-inf inf)
> in (0,inf)
> exp(x)
> Iog(l+exp())
> Tax(uo)
> Sigmoid(x)牛x
> Xin (-inf inf) - Yin [ 1, 1]
> arctan(x)
> tanh(x)
> clamp(y -11)
> Sign(x)
> Xin (inf inf)
> yin (infinf)
> signed
> Power( 0 2)
> log_Ip(x)
> Signed_DOWer(u0 5)
> tail(x-11)
> signed_power(xrz)
> Power(3)
> signed
> power(kr5)


---

### 帖子 #36: 双子数据集统计
- **主帖链接**: 双子数据集统计.md
- **讨论数**: 1

如题, 前后数据集内容是一样的, 前面的是和category更匹配的名字. 可以用来减少重复回测.

我看大部分是从other变为其他类别, 或从其他类别变为model. 按各地区数量统计的, 可能会有错漏.

fundamental89 merged ['other395']
fundamental90 merged ['other401']
model261 merged ['other407']
analyst92 merged ['other411']
fundamental91 merged ['other416']
analyst94 merged ['other423']
fundamental92 merged ['other427']
sentiment33 merged ['other429']
model262 merged ['other432']
model263 merged ['other434']
risk88 merged ['other450']
fundamental93 merged ['other452']
model264 merged ['other460']
fundamental94 merged ['other466']
model266 merged ['other486']
model267 merged ['other510']
news104 merged ['other7']
model243 merged ['other72']
other732 merged ['model159']
other733 merged ['risk69']
other734 merged ['sentiment16']
model244 merged ['other83']
earnings14 merged ['other84']
sentiment31 merged ['other94']
news102 merged ['model210']
analyst82 merged ['model211']
model230 merged ['fundamental65']
model232 merged ['institutions8']
model237 merged ['risk82']
model238 merged ['shortinterest6']
model239 merged ['shortinterest7']
model240 merged ['other33']
model246 merged ['other131']
model248 merged ['other137']
model250 merged ['other176']
model252 merged ['other193']
model253 merged ['other238']
model257 merged ['other351']
model259 merged ['other378']
model260 merged ['other380']
model242 merged ['other54']
analyst81 merged ['model52']
fundamental86 merged ['model56']
socialmedia39 merged ['other100']
earnings11 merged ['news77']
analyst83 merged ['news87']
macro52 merged ['other15']
institutions25 merged ['other515']
fundamental85 merged ['model55']
fundamental87 merged ['news88']
macro55 merged ['other246']
analyst93 merged ['other419']
analyst84 merged ['sentiment12']
shortinterest55 merged ['other534']
analyst87 merged ['other1']
sentiment32 merged ['other111']
shortinterest54 merged ['other148']
macro56 merged ['other305']
model241 merged ['other41']
model265 merged ['other461']
macro53 merged ['other97']

---

### 帖子 #37: 双子数据集统计
- **主帖链接**: https://support.worldquantbrain.com双子数据集统计_34544228948887.md
- **讨论数**: 1

如题, 前后数据集内容是一样的, 前面的是和category更匹配的名字. 可以用来减少重复回测.

我看大部分是从other变为其他类别, 或从其他类别变为model. 按各地区数量统计的, 可能会有错漏.

fundamental89 merged ['other395']
fundamental90 merged ['other401']
model261 merged ['other407']
analyst92 merged ['other411']
fundamental91 merged ['other416']
analyst94 merged ['other423']
fundamental92 merged ['other427']
sentiment33 merged ['other429']
model262 merged ['other432']
model263 merged ['other434']
risk88 merged ['other450']
fundamental93 merged ['other452']
model264 merged ['other460']
fundamental94 merged ['other466']
model266 merged ['other486']
model267 merged ['other510']
news104 merged ['other7']
model243 merged ['other72']
other732 merged ['model159']
other733 merged ['risk69']
other734 merged ['sentiment16']
model244 merged ['other83']
earnings14 merged ['other84']
sentiment31 merged ['other94']
news102 merged ['model210']
analyst82 merged ['model211']
model230 merged ['fundamental65']
model232 merged ['institutions8']
model237 merged ['risk82']
model238 merged ['shortinterest6']
model239 merged ['shortinterest7']
model240 merged ['other33']
model246 merged ['other131']
model248 merged ['other137']
model250 merged ['other176']
model252 merged ['other193']
model253 merged ['other238']
model257 merged ['other351']
model259 merged ['other378']
model260 merged ['other380']
model242 merged ['other54']
analyst81 merged ['model52']
fundamental86 merged ['model56']
socialmedia39 merged ['other100']
earnings11 merged ['news77']
analyst83 merged ['news87']
macro52 merged ['other15']
institutions25 merged ['other515']
fundamental85 merged ['model55']
fundamental87 merged ['news88']
macro55 merged ['other246']
analyst93 merged ['other419']
analyst84 merged ['sentiment12']
shortinterest55 merged ['other534']
analyst87 merged ['other1']
sentiment32 merged ['other111']
shortinterest54 merged ['other148']
macro56 merged ['other305']
model241 merged ['other41']
model265 merged ['other461']
macro53 merged ['other97']

---

### 帖子 #38: 在wq平台, 我们应该通过mcp提供什么工具经验分享
- **主帖链接**: 在wq平台 我们应该通过mcp提供什么工具经验分享.md
- **讨论数**: 9

最近一直在强制自己很频繁的使用mcp. 我想结合例子讲一下什么时候用mcp

mcp的使用场景:

1. 原功能复杂or不通用: 反之可以直接让agent/skill调用命令(一个反面例子是搜索数据库, llm可以直接写mongosh的命令搜索, llm对数据库命令操作的比我还熟练.)
2. 使用频繁: 反之可以直接让agent读代码实现功能(比如给一些alpha打tags, 我不经常使用这个功能, 感觉让agent自己写个临时脚本更方便. )
3. 面向人类: 面向代码或llm的功能没有必要用mcp.(比如simulation功能, 对于全llm工作流来说, 应该是个用不上的功能吧. 但是对于突发奇想想测试什么idea/alpha的人类, 这个功能非常方便)

mcp的注意事项:

1. mcp调用是一次性的, 不应该用mcp来控制流程: 其实cli给mcp返回结果的窗口期很短, 当然有些邪修的方法可以绕过这个限制, 但是我个人也觉得让agent卡在mcp调用不是什么好事, 我自己是比较喜欢异步的
2. 调用简单: 必须让agent能够在工作中正确的调用, 我自己的一个例子是提交simulation时, 给llm的参数自由度太高了, 只规定str类型的话, 它经常出错.
3. 返回的内容不应该太多, 因为mcp的返回结果llm要读的: 我刚开始返回alpha结果的时候, 直接把数据库里所有内容返回了, pnl数据一下就污染了上下文. 还有operators, 如果不用query, 直接把所有有关无关的operator返回. 也挺污染上下文的.


> [!NOTE] [图片 OCR 识别内容]
> /mcp desc
> 
> 
> Configured NCP
> SeIVer5:
> quant-night
> Ready (9
> stzils
> Tools:
> find_related_datafields
> 8
> Search
> for similar data fields using natural language or keywords: 具头CI绐m60讴回纺呆刖窗u期很煜;当
> get_alpha_by_id
> 然有些邪修的方法可以绕过这个限制,但是我个人也觉得让agent卡在mcp调用不是什么
> Get alpha details by ID
> get_datafield_details
> 好事;我自是比较喜欢异步的
> Get
> full metadata for
>  specific datafield by its ID工作中正确的调用;我自己的一个例孑是提交simulation时
> get_operator_details
>  Cname, description, category, orusage) 它经常出错
> Get
> details
> for operators (name
> category
> Or
> usage)
> get_task_progress
> 3.返回的为容不应该太多
> 因Se的返回结某m要读的:我刚开始返回apha结果的时候;
> Check progress
> of
> On
> asynctask (simulation,  fetchsletc.) 数据一下就污染了上下文
> ping
> Health check (used
> for MCP discovery)
> simulate_alpha_batch
> Simulate
> batch of alphas
> with corresponding settings (I-to-1 mapping).
> Each batch must
> NOT exceed 10 alphas.
> For GLB region;
> resource
>  consumption
> simulation
> can take anywhere from
> minute
> to over 10 minutes
> submit_alpha
> Topie
> Submit alpha by
> ID
> validate_alpha
> 顾问专属中文论坛
> Validate alpha expression syntax and semantics


这个是我自己目前用的mcp列表. 有了mcp之后因为报错信息不光是我看, llm也要看, 所以算是强制提高了我代码质量? 这里面validate_alpha我加了之后好像就没用过, 可能应该把它删掉. 还有平时用的时候settings出错比较多, 所以加个available settings比较好吗?

希望有人跟我多多交流mcp的使用经验.

---

### 帖子 #39: 在wq平台, 我们应该通过mcp提供什么工具经验分享
- **主帖链接**: https://support.worldquantbrain.com在wq平台 我们应该通过mcp提供什么工具经验分享_38652207939735.md
- **讨论数**: 9

最近一直在强制自己很频繁的使用mcp. 我想结合例子讲一下什么时候用mcp

mcp的使用场景:

1. 原功能复杂or不通用: 反之可以直接让agent/skill调用命令(一个反面例子是搜索数据库, llm可以直接写mongosh的命令搜索, llm对数据库命令操作的比我还熟练.)
2. 使用频繁: 反之可以直接让agent读代码实现功能(比如给一些alpha打tags, 我不经常使用这个功能, 感觉让agent自己写个临时脚本更方便. )
3. 面向人类: 面向代码或llm的功能没有必要用mcp.(比如simulation功能, 对于全llm工作流来说, 应该是个用不上的功能吧. 但是对于突发奇想想测试什么idea/alpha的人类, 这个功能非常方便)

mcp的注意事项:

1. mcp调用是一次性的, 不应该用mcp来控制流程: 其实cli给mcp返回结果的窗口期很短, 当然有些邪修的方法可以绕过这个限制, 但是我个人也觉得让agent卡在mcp调用不是什么好事, 我自己是比较喜欢异步的
2. 调用简单: 必须让agent能够在工作中正确的调用, 我自己的一个例子是提交simulation时, 给llm的参数自由度太高了, 只规定str类型的话, 它经常出错.
3. 返回的内容不应该太多, 因为mcp的返回结果llm要读的: 我刚开始返回alpha结果的时候, 直接把数据库里所有内容返回了, pnl数据一下就污染了上下文. 还有operators, 如果不用query, 直接把所有有关无关的operator返回. 也挺污染上下文的.


> [!NOTE] [图片 OCR 识别内容]
> /mcp desc
> 
> 
> Configured NCP
> SeIVer5:
> quant-night
> Ready (9
> stzils
> Tools:
> find_related_datafields
> 8
> Search
> for similar data fields using natural language or keywords: 具头CI绐m60讴回纺呆刖窗u期很煜;当
> get_alpha_by_id
> 然有些邪修的方法可以绕过这个限制,但是我个人也觉得让agent卡在mcp调用不是什么
> Get alpha details by ID
> get_datafield_details
> 好事;我自是比较喜欢异步的
> Get
> full metadata for
>  specific datafield by its ID工作中正确的调用;我自己的一个例孑是提交simulation时
> get_operator_details
>  Cname, description, category, orusage) 它经常出错
> Get
> details
> for operators (name
> category
> Or
> usage)
> get_task_progress
> 3.返回的为容不应该太多
> 因Se的返回结某m要读的:我刚开始返回apha结果的时候;
> Check progress
> of
> On
> asynctask (simulation,  fetchsletc.) 数据一下就污染了上下文
> ping
> Health check (used
> for MCP discovery)
> simulate_alpha_batch
> Simulate
> batch of alphas
> with corresponding settings (I-to-1 mapping).
> Each batch must
> NOT exceed 10 alphas.
> For GLB region;
> resource
>  consumption
> simulation
> can take anywhere from
> minute
> to over 10 minutes
> submit_alpha
> Topie
> Submit alpha by
> ID
> validate_alpha
> 顾问专属中文论坛
> Validate alpha expression syntax and semantics


这个是我自己目前用的mcp列表. 有了mcp之后因为报错信息不光是我看, llm也要看, 所以算是强制提高了我代码质量? 这里面validate_alpha我加了之后好像就没用过, 可能应该把它删掉. 还有平时用的时候settings出错比较多, 所以加个available settings比较好吗?

希望有人跟我多多交流mcp的使用经验.

---

### 帖子 #40: 在用llm写descritpion的时候建议加上operator和datafields的描述经验分享
- **主帖链接**: 在用llm写descritpion的时候建议加上operator和datafields的描述经验分享.md
- **讨论数**: 4

如题.

不要只给llm提供表达式, 因为很多字段没法望文生义的. 加上描述之后效果好了很多, 已经算是(我觉得) 人类能阅读的范畴了.

```
signal = group_neutralize(ts_regression(ts_zscore(fnd31_milliq,252),ts_zscore(cap,252),252,rettype=0),industry);ts_target_tvr_decay(signal,target_tvr=0.1)Idea: Exploit mean reversion in illiquidity-adjusted returns after controlling for market capitalization and industry effects.Rationale for data used: Illiquidity captures price pressure, market capitalization reflects size effects, and industry accounts for sectoral biases.Rationale for operators used: ts_regression isolates the illiquidity effect net of market capitalization; group_neutralize removes industry biases.-ts_mean(ts_backfill(vec_sum(scl15_d1_conflict),22), 66)Idea: Identify stocks with recent increases in disagreement/conflict compared to their longer-term average.Rationale for data used: `scl15_d1_conflict` directly measures conflict levels.Rationale for operators used: `ts_mean` calculates the average conflict over different lookback periods. `ts_backfill` handles any missing values in the conflict data.signal= group_neutralize(ts_mean(-vec_avg(rsk60_offer), 22),sector);trade_when(vec_sum(rsk60_crowding)>-5,signal,-1)Idea: Fade the mean reversion of shorting offer rates when crowding is low.Rationale for data used: rsk60_offer reflects shorting costs; sector controls for industry bias; rsk60_crowding indicates market sentiment.Rationale for operators used: group_neutralize removes sector bias; trade_when conditions trading on crowding levels.
```

operator和datafields都可以从表达式ast解析出来. 然后平时存在本地的数据库(或者其他任何形式的文件), 从数据库把描述加进prompt. 我现在用的prompt是这样.

```
regular_alpha_fill:- role: usercontent: |You are a professional quantitative analyst. Given the following alpha expression and related information:Alpha Expression:<alpha>{alpha_regular}</alpha>Operators Used:{operator_info}Datafields Used:{datafields_info}Please complete the following analysis:- Refine the core idea of the alpha: summarize the main concept of the quantitative strategy.- Give concise reasons for using the datafields.- Give concise reasons for using the most important one or two operators.Then generate a structured output using this format (without blank lines):Idea: [fill in core idea]Rationale for data used: [concise explanation without unnecessary words]Rationale for operators used: [concise explanation of key operators]Do not include any extra commentary or formatting.
```

强调了很多次要concise .

接下来应该要让llm自动修改alpha name, 和选择提交alpha的category. 因为平时只会改tag, 这两项我都没有利用起来.

---

### 帖子 #41: 在用llm写descritpion的时候建议加上operator和datafields的描述经验分享
- **主帖链接**: https://support.worldquantbrain.com在用llm写descritpion的时候建议加上operator和datafields的描述经验分享_33620160071831.md
- **讨论数**: 4

如题.

不要只给llm提供表达式, 因为很多字段没法望文生义的. 加上描述之后效果好了很多, 已经算是(我觉得) 人类能阅读的范畴了.

```
signal = group_neutralize(ts_regression(ts_zscore(fnd31_milliq,252),ts_zscore(cap,252),252,rettype=0),industry);ts_target_tvr_decay(signal,target_tvr=0.1)Idea: Exploit mean reversion in illiquidity-adjusted returns after controlling for market capitalization and industry effects.Rationale for data used: Illiquidity captures price pressure, market capitalization reflects size effects, and industry accounts for sectoral biases.Rationale for operators used: ts_regression isolates the illiquidity effect net of market capitalization; group_neutralize removes industry biases.-ts_mean(ts_backfill(vec_sum(scl15_d1_conflict),22), 66)Idea: Identify stocks with recent increases in disagreement/conflict compared to their longer-term average.Rationale for data used: `scl15_d1_conflict` directly measures conflict levels.Rationale for operators used: `ts_mean` calculates the average conflict over different lookback periods. `ts_backfill` handles any missing values in the conflict data.signal= group_neutralize(ts_mean(-vec_avg(rsk60_offer), 22),sector);trade_when(vec_sum(rsk60_crowding)>-5,signal,-1)Idea: Fade the mean reversion of shorting offer rates when crowding is low.Rationale for data used: rsk60_offer reflects shorting costs; sector controls for industry bias; rsk60_crowding indicates market sentiment.Rationale for operators used: group_neutralize removes sector bias; trade_when conditions trading on crowding levels.
```

operator和datafields都可以从表达式ast解析出来. 然后平时存在本地的数据库(或者其他任何形式的文件), 从数据库把描述加进prompt. 我现在用的prompt是这样.

```
regular_alpha_fill:- role: usercontent: |You are a professional quantitative analyst. Given the following alpha expression and related information:Alpha Expression:<alpha>{alpha_regular}</alpha>Operators Used:{operator_info}Datafields Used:{datafields_info}Please complete the following analysis:- Refine the core idea of the alpha: summarize the main concept of the quantitative strategy.- Give concise reasons for using the datafields.- Give concise reasons for using the most important one or two operators.Then generate a structured output using this format (without blank lines):Idea: [fill in core idea]Rationale for data used: [concise explanation without unnecessary words]Rationale for operators used: [concise explanation of key operators]Do not include any extra commentary or formatting.
```

强调了很多次要concise .

接下来应该要让llm自动修改alpha name, 和选择提交alpha的category. 因为平时只会改tag, 这两项我都没有利用起来.

---

### 帖子 #42: 用ast生成super alpha中的combo表达式代码优化
- **主帖链接**: 用ast生成super alpha中的combo表达式代码优化.md
- **讨论数**: 1

出于以下两点:

1. 我发现写combo表达式的问题(输入有限, operator有限-> 表达式) 可以完整的表达成ast的格式

2. (这是我个人看法)虽然可以人工挑选有经济学意义的表达式, 但 除非明确知道selection得到的alpha pool中有某种经济学意义没得到充分表达, 这对于combo来说不过是bias, 我相信selection中的alpha全都有意义, 没理由认为某个意义要比其他高级. 在combo中, 我们应该放下偏见, 更无情的, 向着一个明确的指标优化(比如sharpe), 用机器的方法挖掘selection没有顾虑到的地方.

---

### 帖子 #43: 用ast生成super alpha中的combo表达式代码优化
- **主帖链接**: https://support.worldquantbrain.com用ast生成super alpha中的combo表达式代码优化_32726278113687.md
- **讨论数**: 1

出于以下两点:

1. 我发现写combo表达式的问题(输入有限, operator有限-> 表达式) 可以完整的表达成ast的格式

2. (这是我个人看法)虽然可以人工挑选有经济学意义的表达式, 但 除非明确知道selection得到的alpha pool中有某种经济学意义没得到充分表达, 这对于combo来说不过是bias, 我相信selection中的alpha全都有意义, 没理由认为某个意义要比其他高级. 在combo中, 我们应该放下偏见, 更无情的, 向着一个明确的指标优化(比如sharpe), 用机器的方法挖掘selection没有顾虑到的地方.

---

### 帖子 #44: 过滤掉 Python 内置函数和关键字
- **主帖链接**: https://support.worldquantbrain.com用python ast提取表达式中operator和datafield的方法代码优化_30870358077463.md
- **讨论数**: 7

python ast可以自动解析符合python规范的代码表达式. 因此把我们的alpha转换成python可以理解的方式就能解析了, 这样避免了每次字符串的解析(写正则表达式之类). 可以用来在跑模版的时候检测datafield是否符合规范, 也可以用来统计自己使用的各种datafield, operators频率.

代码如下:

import ast

import re

def parse_alpha(alpha_expression):

"""

Parses an alpha expression and extracts operators and data fields.

This function processes a given alpha expression by converting ternary expressions,

fixing indentation errors, and parsing it into an abstract syntax tree (AST). It then

traverses the AST to extract operators and data fields, while filtering out defined

variables, NaN values, and Python built-in functions and keywords.

Args:

alpha_expression (str): The alpha expression to be parsed.

Returns:

dict: A dictionary containing two lists:

- 'operators': A list of unique operators (function and method names) found in the expression.

- 'data_fields': A list of unique data fields (variable names) found in the expression, excluding defined variables and NaN values.

"""

# 处理三元表达式

alpha_expression = alpha_expression.replace('?',' if ').replace(':',' else ')

# 处理和python内置逻辑表达式冲突

alpha_expression = re.sub(r'\band\b', 'and_', alpha_expression) # 替换独立的 'and'

alpha_expression = re.sub(r'\band\(', 'and_(', alpha_expression) # 替换 'and('

alpha_expression = re.sub(r'\bor\b', 'or_', alpha_expression) # 替换独立的 'or'

alpha_expression = re.sub(r'\bor\(', 'or_(', alpha_expression) # 替换 'or('

# 处理逻辑表达式

alpha_expression = alpha_expression.replace('!',' not ').replace('&&',' and ')

# 处理range="0.1,1,0.1" 类似表达式

alpha_expression = re.sub(r'"([^"]*)"', "0", alpha_expression)

# 处理缩进错误，尝试修复

alpha_expression = "\n".join(line.strip() for line in alpha_expression.splitlines())

# 解析表达式为抽象语法树 (AST)

tree = ast.parse(alpha_expression)

# 提取 operators 和 data fields

operators = set()

data_fields = set()

# 提取过程中定义的变量

defined_variables = set()

# 遍历 AST

for node in ast.walk(tree):

# 提取赋值语句中的变量名

ifisinstance(node, ast.Assign):

for target in node.targets:

ifisinstance(target, ast.Name):

defined_variables.add(target.id) # 记录定义的变量名

# 提取函数调用 (operators)

ifisinstance(node, ast.Call):

ifisinstance(node.func, ast.Name):

operators.add(node.func.id) # 函数名

elifisinstance(node.func, ast.Attribute):

operators.add(node.func.attr) # 方法名

# 提取变量名 (data fields)

ifisinstance(node, ast.Name):

data_fields.add(node.id) # 变量名

# 提取三元条件表达式

ifisinstance(node, ast.IfExp):

# 提取条件部分

ifisinstance(node.test, ast.Compare):

for comparator in node.test.comparators:

ifisinstance(comparator, ast.Name):

data_fields.add(comparator.id)

# 提取 if 部分

ifisinstance(node.body, ast.Name):

data_fields.add(node.body.id)

# 提取 else 部分

ifisinstance(node.orelse, ast.Name):

data_fields.add(node.orelse.id)

# 过滤掉过程中定义的变量

data_fields = data_fields - defined_variables

# 过滤掉特殊变量nan

data_fields = data_fields - set(['nan','true','false'])

# 过滤掉 Python 内置函数和关键字

builtin_functions = set(dir(__builtins__)) # Python 内置函数

operators = operators - builtin_functions # 去掉内置函数

data_fields = data_fields - builtin_functions - operators # 去掉内置函数

return {'operators':list(operators),"data_fields":list(data_fields)}

目前这个版本我自己用着是没发现什么解析错误的问题. 欢迎大家指正.

---

### 帖子 #45: 3. Process and Save
- **主帖链接**: 脚本记录Osmosis point每日变化代码优化.md
- **讨论数**: 2

不知道Osmosis point的leaderboard的api之后会不会变化, 我想既然之后每周都要更新osmosis point, 用定时脚本记录历史变化应该比较有必要. 方便自己监测质量
 [图片 (图片已丢失)]

# monitor_osmosis.py

import asyncio

import aiohttp

import json

import logging

import os

import pandas as pd

from datetime import datetime

import sys

# Add project root to sys.path to allow imports

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from util.network_util import _request_with_retry

from api.login import async_login_to_brain

logger = logging.getLogger("OsmosisMonitor")

OSMOSIS_URL = " [[链接已屏蔽]) "

HISTORY_FILE = "osmosis_history.json"

# ======================================================

# ✅ 1. Fetch Osmosis Data

# ======================================================

async def fetch_osmosis_data(session) -> dict:

"""Fetch data from the Osmosis Competition API."""

logger.info(f"Fetching Osmosis data from {OSMOSIS_URL}...")

try:

data = await _request_with_retry(session=session, url=OSMOSIS_URL)

return data

exceptExceptionas e:

logger.error(f"Failed to fetch Osmosis data: {e}")

returndict()

# ======================================================

# ✅ 2. Compare and Update History

# ======================================================

def process_and_save(current_data: dict):

"""

Load history, compare current user stats with the last record,

print a summary of changes, and save the new record.

"""

ifnot current_data or"leaderboard"notin current_data:

logger.warning("⚠️ No user stats found in 'leaderboard' field.")

return

# Use actual date for daily tracking

now = datetime.now()

today_date = now.strftime("%Y-%m-%d")

today_full = now.strftime("%Y-%m-%d %H:%M:%S")

current_stats = current_data["leaderboard"]

# Load history

history = dict()

if os.path.exists(HISTORY_FILE):

try:

withopen(HISTORY_FILE, "r") as f:

history = json.load(f)

exceptExceptionas e:

logger.error(f"Failed to read history file: {e}")

# Find the latest previous record

sorted_dates = sorted([d for d in history.keys() if d < today_date], reverse=True)

last_date = sorted_dates[0] if sorted_dates else None

last_record = history.get(last_date, dict()) if last_date else dict()

last_stats = last_record.get("stats", dict())

if last_date:

logger.info(f"Comparing with last record from: {last_date}")

else:

logger.info("No previous records found for comparison.")

# --- 1. General Metrics ---

general_metrics = ['rank', 'totalScore']

general_summary = []

for key in general_metrics:

curr_val = current_stats.get(key)

prev_val = last_stats.get(key)

change_str = ""

if curr_val isnotNoneand prev_val isnotNone:

diff = curr_val - prev_val

if diff >0:

change_str = f" (🔺 +{diff})"

if key =="rank": change_str =f" (🔻 +{diff})"# Drop in rank

elif diff <0:

change_str = f" (🔻 {diff})"

if key =="rank": change_str =f" (🔺 {diff})"# Improve in rank

val_str = f"{curr_val}{change_str}" if curr_val is not None else "N/A"

general_summary.append(f"{key.capitalize()}: {val_str}")

print("\n🏆 My Osmosis Performance Update:")

print(f"📅 Today: {today_full}")

print(" | ".join(general_summary))

print("-"*60)

# --- 2. Regional Metrics Table ---

regions = ['ASI', 'EUR', 'GLB', 'IND', 'USA']

metric_map = {

'cumulativePNL': 'PnL',

'osmosisAlphas': 'Alphas',

'osmosisOSAfterCostIRRank': 'IR Rank',

'osmosisPointsAllocated': 'Points'

}

region_rows = []

for region in regions:

row = {'Region': region}

for prefix, col_name in metric_map.items():

full_key = f"{prefix}{region}"

curr_val = current_stats.get(full_key)

prev_val = last_stats.get(full_key)

val_str = str(curr_val) if curr_val is not None else "N/A"

if curr_val isnotNoneand prev_val isnotNoneandisinstance(curr_val, (int, float)):

diff = curr_val - prev_val

if diff !=0:

sign = "+" if diff > 0 else ""

# Logic: Rank -> lower is better (green), others -> higher is better (green)

# Use standard arrows for direction, user interprets meaning

icon ="🔺"if diff >0else"🔻"

# Context aware icon coloring (simulated)

if"Rank"in col_name:

# Rank increase (numeric) is bad

pass

val_str += f" ({icon} {sign}{diff})"

row[col_name] = val_str

region_rows.append(row)

df_regions = pd.DataFrame(region_rows)

ifnot df_regions.empty:

pd.set_option('display.max_rows', None)

pd.set_option('display.width', 1000)

# Reorder columns

cols = ['Region', 'PnL', 'Alphas', 'IR Rank', 'Points']

print(df_regions[cols].to_string(index=False))

else:

print("No regional metrics found.")

# Save today's record (overwrite if run multiple times today)

history[today_date] = {

"updated_at": today_full,

"stats": current_stats

}

try:

withopen(HISTORY_FILE, "w") as f:

json.dump(history, f, indent=2)

logger.info(f"\n✅ History updated in {HISTORY_FILE}")

exceptExceptionas e:

logger.error(f"Failed to save history: {e}")

# ======================================================

# ✅ 3. Main Workflow

# ======================================================

async def main():

asyncwith aiohttp.ClientSession() as session:

# 1. Login

await async_login_to_brain(session)

# 2. Fetch Data

data = await fetch_osmosis_data(session)

# 3. Process and Save

process_and_save(data)

if __name__ == "__main__":

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

asyncio.run(main())

log是这样, 会存一个history的json


> [!NOTE] [图片 OCR 识别内容]
> 2026-01-10 09:09:26,704
> WARNING
> Entering cookie validation check
> 2026-01-10 09:09:27,948
> INFO
> Cookie valid,
> login skipped
> 2026-01-10 09:09:27,948
> INF0
> Fetching Osmosis
> data
> from https: / /api.worldquantbrain.com/competitions/0C2025
> 2026-01-10 09:09:29,150
> INF0
> No previous
> records
> found
> for comparison.
> My Osmosis Performance Update:
> Today:
> 2026-01-10 09:09:29
> Rank:
> 422
> Totalscore:
> 41356.0
> Region
> Pnl Alphas
> IR Rank Points
> ASI
> 4811.0
> 43
> 4096.0 IOOOoa
> EUR
> 15398.0
> 44  29172.0 1OOOa0
> GLB
> -2367.0
> 33  64043.0  100000
> IND
> -13888.0
> 10  65644.0 IQOOoa
> USA
> -574.0
> 89  43825.0  100000
> 2026-01-10 09:09:29,154
> INF0
> History updated
> in osmosis_history.json


---

### 帖子 #46: 3. Process and Save
- **主帖链接**: https://support.worldquantbrain.com脚本记录Osmosis point每日变化代码优化_37576441185559.md
- **讨论数**: 2

不知道Osmosis point的leaderboard的api之后会不会变化, 我想既然之后每周都要更新osmosis point, 用定时脚本记录历史变化应该比较有必要. 方便自己监测质量
 [图片 (图片已丢失)]

# monitor_osmosis.py

import asyncio

import aiohttp

import json

import logging

import os

import pandas as pd

from datetime import datetime

import sys

# Add project root to sys.path to allow imports

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from util.network_util import _request_with_retry

from api.login import async_login_to_brain

logger = logging.getLogger("OsmosisMonitor")

OSMOSIS_URL = " [[链接已屏蔽]) "

HISTORY_FILE = "osmosis_history.json"

# ======================================================

# ✅ 1. Fetch Osmosis Data

# ======================================================

async def fetch_osmosis_data(session) -> dict:

"""Fetch data from the Osmosis Competition API."""

logger.info(f"Fetching Osmosis data from {OSMOSIS_URL}...")

try:

data = await _request_with_retry(session=session, url=OSMOSIS_URL)

return data

exceptExceptionas e:

logger.error(f"Failed to fetch Osmosis data: {e}")

returndict()

# ======================================================

# ✅ 2. Compare and Update History

# ======================================================

def process_and_save(current_data: dict):

"""

Load history, compare current user stats with the last record,

print a summary of changes, and save the new record.

"""

ifnot current_data or"leaderboard"notin current_data:

logger.warning("⚠️ No user stats found in 'leaderboard' field.")

return

# Use actual date for daily tracking

now = datetime.now()

today_date = now.strftime("%Y-%m-%d")

today_full = now.strftime("%Y-%m-%d %H:%M:%S")

current_stats = current_data["leaderboard"]

# Load history

history = dict()

if os.path.exists(HISTORY_FILE):

try:

withopen(HISTORY_FILE, "r") as f:

history = json.load(f)

exceptExceptionas e:

logger.error(f"Failed to read history file: {e}")

# Find the latest previous record

sorted_dates = sorted([d for d in history.keys() if d < today_date], reverse=True)

last_date = sorted_dates[0] if sorted_dates else None

last_record = history.get(last_date, dict()) if last_date else dict()

last_stats = last_record.get("stats", dict())

if last_date:

logger.info(f"Comparing with last record from: {last_date}")

else:

logger.info("No previous records found for comparison.")

# --- 1. General Metrics ---

general_metrics = ['rank', 'totalScore']

general_summary = []

for key in general_metrics:

curr_val = current_stats.get(key)

prev_val = last_stats.get(key)

change_str = ""

if curr_val isnotNoneand prev_val isnotNone:

diff = curr_val - prev_val

if diff >0:

change_str = f" (🔺 +{diff})"

if key =="rank": change_str =f" (🔻 +{diff})"# Drop in rank

elif diff <0:

change_str = f" (🔻 {diff})"

if key =="rank": change_str =f" (🔺 {diff})"# Improve in rank

val_str = f"{curr_val}{change_str}" if curr_val is not None else "N/A"

general_summary.append(f"{key.capitalize()}: {val_str}")

print("\n🏆 My Osmosis Performance Update:")

print(f"📅 Today: {today_full}")

print(" | ".join(general_summary))

print("-"*60)

# --- 2. Regional Metrics Table ---

regions = ['ASI', 'EUR', 'GLB', 'IND', 'USA']

metric_map = {

'cumulativePNL': 'PnL',

'osmosisAlphas': 'Alphas',

'osmosisOSAfterCostIRRank': 'IR Rank',

'osmosisPointsAllocated': 'Points'

}

region_rows = []

for region in regions:

row = {'Region': region}

for prefix, col_name in metric_map.items():

full_key = f"{prefix}{region}"

curr_val = current_stats.get(full_key)

prev_val = last_stats.get(full_key)

val_str = str(curr_val) if curr_val is not None else "N/A"

if curr_val isnotNoneand prev_val isnotNoneandisinstance(curr_val, (int, float)):

diff = curr_val - prev_val

if diff !=0:

sign = "+" if diff > 0 else ""

# Logic: Rank -> lower is better (green), others -> higher is better (green)

# Use standard arrows for direction, user interprets meaning

icon ="🔺"if diff >0else"🔻"

# Context aware icon coloring (simulated)

if"Rank"in col_name:

# Rank increase (numeric) is bad

pass

val_str += f" ({icon} {sign}{diff})"

row[col_name] = val_str

region_rows.append(row)

df_regions = pd.DataFrame(region_rows)

ifnot df_regions.empty:

pd.set_option('display.max_rows', None)

pd.set_option('display.width', 1000)

# Reorder columns

cols = ['Region', 'PnL', 'Alphas', 'IR Rank', 'Points']

print(df_regions[cols].to_string(index=False))

else:

print("No regional metrics found.")

# Save today's record (overwrite if run multiple times today)

history[today_date] = {

"updated_at": today_full,

"stats": current_stats

}

try:

withopen(HISTORY_FILE, "w") as f:

json.dump(history, f, indent=2)

logger.info(f"\n✅ History updated in {HISTORY_FILE}")

exceptExceptionas e:

logger.error(f"Failed to save history: {e}")

# ======================================================

# ✅ 3. Main Workflow

# ======================================================

async def main():

asyncwith aiohttp.ClientSession() as session:

# 1. Login

await async_login_to_brain(session)

# 2. Fetch Data

data = await fetch_osmosis_data(session)

# 3. Process and Save

process_and_save(data)

if __name__ == "__main__":

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

asyncio.run(main())

log是这样, 会存一个history的json


> [!NOTE] [图片 OCR 识别内容]
> 2026-01-10 09:09:26,704
> WARNING
> Entering cookie validation check
> 2026-01-10 09:09:27,948
> INFO
> Cookie valid,
> login skipped
> 2026-01-10 09:09:27,948
> INF0
> Fetching Osmosis
> data
> from https: / /api.worldquantbrain.com/competitions/0C2025
> 2026-01-10 09:09:29,150
> INF0
> No previous
> records
> found
> for comparison.
> My Osmosis Performance Update:
> Today:
> 2026-01-10 09:09:29
> Rank:
> 422
> Totalscore:
> 41356.0
> Region
> Pnl Alphas
> IR Rank Points
> ASI
> 4811.0
> 43
> 4096.0 IOOOoa
> EUR
> 15398.0
> 44  29172.0 1OOOa0
> GLB
> -2367.0
> 33  64043.0  100000
> IND
> -13888.0
> 10  65644.0 IQOOoa
> USA
> -574.0
> 89  43825.0  100000
> 2026-01-10 09:09:29,154
> INF0
> History updated
> in osmosis_history.json


---

### 帖子 #47: PnL = ∑(Robustness * Creativity)
- **主帖链接**: 适合邮箱自动推送的平台信息经验分享.md
- **讨论数**: 9

有些数据(尤其是排行榜数据), 刷新一次还是很浪费时间的. 这种情况我都觉得让邮箱每天自动推送比较好. 我选择推送的 **平台五项(income/consultant/genuis/message/simulation count).**

推送流程是: 1. 分开设置每个拉取不同数据的脚本 2. 设置总结推送脚本 3. 设置定时任务启动总结脚本

我用的是mac, 添加成功到~/Library/LaunchAgents/定时任务后系统会提示. 建议任务还是写在项目中, 系统目录下用软链接, 方便管理

**用到这些api:**


> [!NOTE] [图片 OCR 识别内容]
> USERS
> SELF
> URL:
> /users /self
> USERS
> SELF
> ALPHAS
> URL:
> /users/self/alphas
> USERS
> SELF_MESSAGES
> URL:
> /users /self /messages
> USERS
> SELF
> CONSULTANT_SUMMARY
> URL:
> /users /self /consultant
> summary
> USERS
> SELF_ACTIVITIES
> BASE
> PAYMENT_URL:
> /users/self/activities /base-payment
> CONSULTANT
> BOARDS
> GENIUS
> URL:
> /consultant /boards /genius
> CONSULTANT
> BOARDS
> LEADER_URL:
> /consultant
> boards /leader


我用的推送格式如图:


> [!NOTE] [图片 OCR 识别内容]
> Platform Data Report
> 2026-02-18 14:48
> Income & Submission Summary
> **Base Payment**
> Total:
>  $24.59
> Regular Alpha:
> $5.83
> Super Alpha
>  $18.76
> *XActivity Summary*x
> Submissions
> Simulations
> 935
> Leaderboard Ranks
> metric
> Value
> rank
> OWR
> country_
> rank
> change
> WeightFactor
> 21.8000
> 714
> 84
> ValueFactor
> 0.9100
> 386
> 127
> dailyOsmosisRank
> 0.4500
> 553
> 279
> dataFieldsUsed
> 539.0000
> 1476
> 186
> submissionsCount
> 424.0000
> 2015
> 242
> meanProdCorrelation
> 0.6731
> 4436
> 1840
> meanSelfCorrelation
> 0.3324
> 2592
> 1486
> Genius Ranking
> metric
> Value
> rank
> operatorCount
> 60.00
> 338.0
> operatorAvg
> 4.22
> 1419.0
> fieldCount
> 51.00
> 1945.0
> fieldAvg
> 1.59
> 1588.0
> communityActivity
> 44.90
> 89.0
> completedReferrals
> NaN
> NaN
> maxSimulationstreak
> 363.00
> 309.0
> Rank Score: 948
> Recent Research Papers
> Research Paper: Downside Beta and Equity Returns around the World
> Check out the research PapeC, its key ideas and the associated BRAIN data fields。
> Launching
> a neW "OTHERIDI Power Pool Feb 26 Theme"
> Exciting news! We have launched a new "OTHER/D1 Power Pool Feb` 26 Theme".
> Duration: 16 Feb'26
> 28th Feb'26 (2 weeks)
> Multiplier: 1X for regular power pool alphas
> Details: Power Pogl Alpha must be simulated with Delay
> in one of the following regions: AMR, HKG, TWN,JPN,or
> KOR. The pvl (Price Volume Data for Equity) dataset is not allowed for。
> Avg



> [!NOTE] [图片 OCR 识别内容]
> Unlock a 10% AIAC 2.0 Tiebreaker Boost for Your Genius Level
> 860 consultants completed Genius eligibility criteria last quarter and may have potentially been promoted to a higher
> Genius level f they had the 10% higher tiebreaker score. Earn this 10% Genius boost by fulfilling eompetition
> eligibility_criteria in AIAC 2.0. Submissions end on 15th February 23:59 EST
> Value Factor updated
> Value Factors have been refreshed on the consultant leaderboard. This Value Factor considers all the Alphas
> SuperAlphas submitted in the 3 month period ending 31 December 2025_
> Alpha Simulations (Past 24h)
> Past 24 Hours Alpha Simulations Counts
> 
> 
> TM TII
> T
> TEMI
> SHTIII
> 3T
> 4II
> UOII
> and


现在回测数不重要所以被我挪到最后了. 感谢 [顾问 SZ83096 (Rank 13)](/hc/en-us/profiles/29001331587351-顾问 SZ83096 (Rank 13))  橘子姐姐的画图代码. 抄了放在我代码库里很久了, 一直懒的运行, 终于找到它的用途了.

我自己来说主要在意的是自己的排名. 毕竟做了一年多了. 最近weight排名一直掉, 这个坎是过不去了.

---

### 帖子 #48: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com适合邮箱自动推送的平台信息经验分享_38472629440407.md
- **讨论数**: 9

有些数据(尤其是排行榜数据), 刷新一次还是很浪费时间的. 这种情况我都觉得让邮箱每天自动推送比较好. 我选择推送的 **平台五项(income/consultant/genuis/message/simulation count).**

推送流程是: 1. 分开设置每个拉取不同数据的脚本 2. 设置总结推送脚本 3. 设置定时任务启动总结脚本

我用的是mac, 添加成功到~/Library/LaunchAgents/定时任务后系统会提示. 建议任务还是写在项目中, 系统目录下用软链接, 方便管理

**用到这些api:**


> [!NOTE] [图片 OCR 识别内容]
> USERS
> SELF
> URL:
> /users /self
> USERS
> SELF
> ALPHAS
> URL:
> /users/self/alphas
> USERS
> SELF_MESSAGES
> URL:
> /users /self /messages
> USERS
> SELF
> CONSULTANT_SUMMARY
> URL:
> /users /self /consultant
> summary
> USERS
> SELF_ACTIVITIES
> BASE
> PAYMENT_URL:
> /users/self/activities /base-payment
> CONSULTANT
> BOARDS
> GENIUS
> URL:
> /consultant /boards /genius
> CONSULTANT
> BOARDS
> LEADER_URL:
> /consultant
> boards /leader


我用的推送格式如图:


> [!NOTE] [图片 OCR 识别内容]
> Platform Data Report
> 2026-02-18 14:48
> Income & Submission Summary
> **Base Payment**
> Total:
>  $24.59
> Regular Alpha:
> $5.83
> Super Alpha
>  $18.76
> *XActivity Summary*x
> Submissions
> Simulations
> 935
> Leaderboard Ranks
> metric
> Value
> rank
> OWR
> country_
> rank
> change
> WeightFactor
> 21.8000
> 714
> 84
> ValueFactor
> 0.9100
> 386
> 127
> dailyOsmosisRank
> 0.4500
> 553
> 279
> dataFieldsUsed
> 539.0000
> 1476
> 186
> submissionsCount
> 424.0000
> 2015
> 242
> meanProdCorrelation
> 0.6731
> 4436
> 1840
> meanSelfCorrelation
> 0.3324
> 2592
> 1486
> Genius Ranking
> metric
> Value
> rank
> operatorCount
> 60.00
> 338.0
> operatorAvg
> 4.22
> 1419.0
> fieldCount
> 51.00
> 1945.0
> fieldAvg
> 1.59
> 1588.0
> communityActivity
> 44.90
> 89.0
> completedReferrals
> NaN
> NaN
> maxSimulationstreak
> 363.00
> 309.0
> Rank Score: 948
> Recent Research Papers
> Research Paper: Downside Beta and Equity Returns around the World
> Check out the research PapeC, its key ideas and the associated BRAIN data fields。
> Launching
> a neW "OTHERIDI Power Pool Feb 26 Theme"
> Exciting news! We have launched a new "OTHER/D1 Power Pool Feb` 26 Theme".
> Duration: 16 Feb'26
> 28th Feb'26 (2 weeks)
> Multiplier: 1X for regular power pool alphas
> Details: Power Pogl Alpha must be simulated with Delay
> in one of the following regions: AMR, HKG, TWN,JPN,or
> KOR. The pvl (Price Volume Data for Equity) dataset is not allowed for。
> Avg



> [!NOTE] [图片 OCR 识别内容]
> Unlock a 10% AIAC 2.0 Tiebreaker Boost for Your Genius Level
> 860 consultants completed Genius eligibility criteria last quarter and may have potentially been promoted to a higher
> Genius level f they had the 10% higher tiebreaker score. Earn this 10% Genius boost by fulfilling eompetition
> eligibility_criteria in AIAC 2.0. Submissions end on 15th February 23:59 EST
> Value Factor updated
> Value Factors have been refreshed on the consultant leaderboard. This Value Factor considers all the Alphas
> SuperAlphas submitted in the 3 month period ending 31 December 2025_
> Alpha Simulations (Past 24h)
> Past 24 Hours Alpha Simulations Counts
> 
> 
> TM TII
> T
> TEMI
> SHTIII
> 3T
> 4II
> UOII
> and


现在回测数不重要所以被我挪到最后了. 感谢 [顾问 SZ83096 (Rank 13)](/hc/en-us/profiles/29001331587351-顾问 SZ83096 (Rank 13))  橘子姐姐的画图代码. 抄了放在我代码库里很久了, 一直懒的运行, 终于找到它的用途了.

我自己来说主要在意的是自己的排名. 毕竟做了一年多了. 最近weight排名一直掉, 这个坎是过不去了.

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《Step 5: 计算中性化结果》的评论回复
- **帖子链接**: [Commented] Operator大师-用基础的operator实现复杂功能.md
- **评论时间**: 1年前

```
{data}-ts_max_diff({data},{d}) #ts_max
```

```
(({data}-ts_max_diff({data},{d}))*ts_scale({data},{d})-{data})/(ts_scale({data},{d})-1)  #ts_min
```

---

### 探讨 #2: 关于《Step 5: 计算中性化结果》的评论回复
- **帖子链接**: [Commented] Operator大师-用基础的operator实现复杂功能.md
- **评论时间**: 1年前

```
weight = {d}+ts_step(0);ts_sum({data}*weight,{d})/ts_sum(weight,{d}) #ts_decay_linear
```

虽然linear decay大家都有, 其他filter都可以这么制作, 改weight就可以. 我等级低也没法验证是否完全一致

---

### 探讨 #3: 关于《Step 5: 计算中性化结果》的评论回复
- **帖子链接**: [Commented] Operator大师-用基础的operator实现复杂功能.md
- **评论时间**: 10个月前

```
group_normalize({data},{group}) = {data}/(group_sum(abs({data}),{group}))
```

===============================================================================

---

### 探讨 #4: 关于《Step 5: 计算中性化结果》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Operator大师-用基础的operator实现复杂功能_29085671898775.md
- **评论时间**: 1年前

```
{data}-ts_max_diff({data},{d}) #ts_max
```

```
(({data}-ts_max_diff({data},{d}))*ts_scale({data},{d})-{data})/(ts_scale({data},{d})-1)  #ts_min
```

---

### 探讨 #5: 关于《Step 5: 计算中性化结果》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Operator大师-用基础的operator实现复杂功能_29085671898775.md
- **评论时间**: 1年前

```
weight = {d}+ts_step(0);ts_sum({data}*weight,{d})/ts_sum(weight,{d}) #ts_decay_linear
```

虽然linear decay大家都有, 其他filter都可以这么制作, 改weight就可以. 我等级低也没法验证是否完全一致

---

### 探讨 #6: 关于《【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！》的评论回复
- **帖子链接**: [Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation.md
- **评论时间**: 11个月前

**模板**

```
<exceed op/>(<Arithmetic op/>(<option_call/>) , <Arithmetic op/>(<option_put/>))
```

- 模板中的变量使用 **< />** 进行了声明，总共4个变量。
- 具体变量1：<option_call/>: 可以包含所有和call有关的期权字段
- 具体变量2：<option_put/>: 可以包含所有和call有关的期权字段
- 具体变量3：< **Arithmetic op** />: 任何eltwise的变换operator(比如-1/x, log, signed_power, s_log_1p, tanh, arc_tan)等
- 具体变量4：< **exceed op** />: 任何表示前一个超出后一个的运算.(比如"({data1})/({data2})", "({data1}-({data2}))", "({data1}-({data2}))/({data2})",            # 相对变化率, data1, data2是正数的变量时使用 "({data1}-{data2})/({data1}/2+{data2}/2), ({data1}-{data2})/ts_std_dev({data2},252)”)等,

- 搜索空间的大小：option8, option4 , pair个数 x arithmetic op个数 x 外面套的1,2,3阶运算符的个数
- 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：  **Arithmetic op的目的** 就是想尽量扩大搜索范围, call,put分别套了arithmetic op 后correlation下降不少, 有些信号看着还挺好
- 产出效果： 可能option4数据集信号就是比较强, 随便跑都有很多产出
- 建议其他顾问未来尝试的探索方向: AI我尝试过不同希腊字母, 比如theta vega 配对, 但是效果一般, 感觉还是应该尝试不同的希腊字母组合.
  [图片 (图片已丢失)]

---

### 探讨 #7: 关于《【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **评论时间**: 11个月前

**模板**

```
<exceed op/>(<Arithmetic op/>(<option_call/>) , <Arithmetic op/>(<option_put/>))
```

- 模板中的变量使用 **< />** 进行了声明，总共4个变量。
- 具体变量1：<option_call/>: 可以包含所有和call有关的期权字段
- 具体变量2：<option_put/>: 可以包含所有和call有关的期权字段
- 具体变量3：< **Arithmetic op** />: 任何eltwise的变换operator(比如-1/x, log, signed_power, s_log_1p, tanh, arc_tan)等
- 具体变量4：< **exceed op** />: 任何表示前一个超出后一个的运算.(比如"({data1})/({data2})", "({data1}-({data2}))", "({data1}-({data2}))/({data2})",            # 相对变化率, data1, data2是正数的变量时使用 "({data1}-{data2})/({data1}/2+{data2}/2), ({data1}-{data2})/ts_std_dev({data2},252)”)等,

- 搜索空间的大小：option8, option4 , pair个数 x arithmetic op个数 x 外面套的1,2,3阶运算符的个数
- 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）：  **Arithmetic op的目的** 就是想尽量扩大搜索范围, call,put分别套了arithmetic op 后correlation下降不少, 有些信号看着还挺好
- 产出效果： 可能option4数据集信号就是比较强, 随便跑都有很多产出
- 建议其他顾问未来尝试的探索方向: AI我尝试过不同希腊字母, 比如theta vega 配对, 但是效果一般, 感觉还是应该尝试不同的希腊字母组合.
  
> [!NOTE] [图片 OCR 识别内容]
> opt
> All Status
> Region
> Delay
> Days Before
> Min Turnov:
> Max Turnov
> Min Margin
> 计算 Correl
> Min Return
> Regio
> Shar
> Fitne
> Retur
> Turnov
> Margi
> Sub-U
> Date
> Statu
> Regular
> I0
> Score
> Message
> Pnl
> pe
> SS
> ns
> er
> Sharpe
> Created
> ts_std_dev((opt4_ 182_put_pre_delta3O)/(opt4_ 18..JrMYXgI
> USA
> 26.719309203370738-1.04
> -0.8
> -7.42%
> 7.37%
> -20.12%00-0.54
> 2025-07-14
> FAIL LOW_SHARPE,LOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_547_call_vola_delta45-(opt4_547
> OgQqkOd USA
> 82.17038037547896
> 1.51
> 1.53
> 12.91 %
> 8.40%
> 30.74%o。 0.77
> 2025-07-14
> FAIL
> LOW_SHARPE MATCHES_THEMES
> 查看
> ts_av_diff((opt4_273_put_vola_delta25)/(opt4_27
> j0zlpz0
> USA
> 28.80059299117893
> -1.17
> -0.61
> -4.69%
> 17.08%
> -5.50%o。
> 1.01
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_ 122_put_vola_delta45)/(opt4_122_
> 05OkZbq
> USA
> 28.79967050699429
> -2.03
> -2.1
> -13.32%7.39%
> -36.07%。-1.13
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> (opt4_122_put_vola_delta5O-opt4_ 122_call_vola
> 8XSgXPV
> USA
> 28.85978993222753
> 1.65
> -1.27
> -11.47%19.27%
> -11.90%o0-0.84
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_30_put_vola_delta5O-opt4_30_cal.. 9Lk7329
> USA
> 22.16807467527147
> -1.2
> -1.03
> -9.20%
> 6.60%
> -27.88%00-0.78
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESS,LOW_SUB_UNIVERS
> 查看
> ts_delay((opt4_ 182_put_vola_delta45)/(opt4_182
> bAG7NqZ USA
> 28.861353313495975-2.03
> -1.68
> -12.13%17.69%
> -13.72%00-1.13
> 2025-07-14
> FAIL
> LOW_SHARPE LOW_FITNESSLOW_SUB_UNIVERS_
> 查看
> ts
> mean((opt23_super_OP_trans_iv_ra_iV_call-opt.. VelnnJy
> USA
> 84.37926278033673
> 1.39
> 0.98
> 6.23%
> 5.51%
> 22.61%o。 0.79
> 2025-07-14
> FAIL
> LOW_SHARPE,LOW_FITNESS,MATCHES_THEMES
> 查看
> ts_delta((opt4_30_put_vola_delta2O)/(opt4_30_
> Ca.WWKGmedUSA
> 28.407897015951416-1.2
> -0.53
> -3.83%
> 19.87%
> -3.869o。
> -1.23
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> ts_delta((opt4_730_put_vola_delta45)/(opt4_730
> XMmEVR1 USA
> 29.21246681753198
> -1.07
> -0.52
> -4.83%
> 20.35%
> -4.74%oo
> -0.73
> 2025-07-14
> FAIL LOW_SHARPE LOW_FITNESS,LOW_SUB_UNIVERS_
> 查看
> ts_delta((opt4_ 182_put_Vola_delta5o)l(opt4_ 182
> JrMLX7A
> USA
> 28.59394501691516
> -1.03
> -0.51
> -5.31%
> 21.81%
> -4.879o。
> -0.9
> 2025-07-14
> FAIL
> LOW_SHARPE,LOW_FITNESS,LOW_SUB_UNIVERS
> 查看
> ts_mean((opt4_GO_call_vola_delta45-opt4_GO_pU.. dvkwnxk
> USA
> 82.50928760533199
> 1.66
> 1.46
> 9.64%
> 6.28%
> 30.71%。
> 2025-07-14
> FAIL
> MATCHES_THEMES
> 查看
> ts_mean((opt4_1
> call_Vola_delta8o-(opt4_152
> qVgZvno
> USA
> 80.35573223118207
> 1.45
> 1.54
> 14.14%
> 9.00%
> 31.42%。0.77
> 2025-07-14
> FAIL
> LOW_SHARPEMATCHES_THEMES
> 查看
> ts_mean((opt4_GO_call_vola_delta5O-opt4_GO_pU.. qV9ZrSv
> USA
> 75.91622868322459
> 1.33
> 1.23
> 10.69%
> 7.02%
> 30.46%o。 0.79
> 2025-07-14
> FAIL
> LOW_SHARPEMATCHES_THEMES
> 查看
> ts_std_dev((opt4_call_vega_ 122d-opt4_put_vega... 691JY0o
> USA
> 27.945397048192213-1.13
> -0.82
> -6.52%
> 5.80%
> -22.49%o0-0.76
> 2025-07-14
> FAIL
> LOW_SHARPELOW_FITNESSLOW_SUB_UNIVERS
> 查看
> (opt23_photo_trans_iv_iv_call)/(opt23_photo_tran... |1pbpjn
> USA
> 83.31975278601249
> 1.44
> 0.51
> 6.84%
> 54.42%
> 2.52%。
> 0.87
> 2025-07-14
> FAIL
> LOW_SHARPE LOW_FITNESS,MATCHES_THEMES
> 查看
> 52_C


---

### 探讨 #8: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025/12/06

一直尝试探索institution category. 要说结果, 可以说是没有任何结果. 目前因为存货太少, 不停翻垃圾的话, 数据bias想必会越来越严重. 非常想扩充我的alpha存货.

大家都在用agent操作alpha了, 而我还没有用上function calling. 给自己的代码写了个skill接口和文档, 但是工作流还是没跑通. 手动操作的确太烦了, 如果能让llm接管一部分就好了. 而且好的agent实在太贵了, 不支持我用来做一天一刀的工作, 虽然可以到处薅羊毛, 但是根本没有精力去弄这些一次性的东西...

写了表达式的cse, 感觉非常有用.

==================================================================================

==================================================================================

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025/12/07

继续跑instittuions, 还是没有收获. 仅有的一些也并不是稳定信号. 可以试的配对也基本都试过了. 比较奇怪的是ts_returns倒有信号? 是因为原始数据分布在1附近吗? 因为lab里没法看数据也没法查证.

看到帖子里一个奇怪的alpha:
-rank(ts_corr(vwap,volume,5))*rank(price_limit_condition) 和 -rank(ts_corr(vwap,volume,5)) 的指标完全一样, 但rank(price_limit_condition)却又不是一个常数. 是为什么呢? 是不是price_limit_condition大量值是相同的, 所以分布在1附近呢

============================================================================

============================================================================

---

### 探讨 #10: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025/12/10

aiac拿到了第13名, 真是做wq以来为数不多的好消息了, 也是我参加比赛的最好名次了. 不过界面上os一直也没更新, 也看不出表现的怎么样.

因为想扩充存货, 最近一直在坚持交alpha, 浪费很多时间. 都来不及改代码了. 感觉真是对个人精力的一种巨大消耗.

============================================================================

============================================================================

---

### 探讨 #11: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

2025/07/14

整理了一天新添加的operator. 好多新的operator还完全没有理解.

sac终于结束了, 交了两天corr<0.5的sa, 可是base并不高, 看来os还是挺重要的. 本来sa已经交不上了, 幸好这次赶时间升到了master.

给插件增加了jupyter notebook的支持.

--------------------------------------------------------------

--------------------------------------------------------------

---

### 探讨 #12: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 0年前

2025/07/16

经过别人提醒, 我意识到有时候我完全找不到alpha是搜索范围太小的原因, 陷入了局部最优的陷阱. 增加了更多随机性之后, 确实有一些之前不怎么样的信号sharpe变高了, 给我非常真切的实感. 问题太明显了, 以至于疑惑为什么几个月前没有意识到

今天的培训课也收获非常大, 要做的事, 可以优化的地方太多了. 之前的培训虽然也讲过, 但是一直没有好好利用llm提高效率.

---

### 探讨 #13: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025/07/21

更新了value factor之后, 跌到了0.54. sa的prod correlation顿时没意义了. 反思自己5月做了什么事, 大概是提交变得更随意了. 刚开始做的时候, 提交之前都会积极的尝试化简一下表达式, 手动跑一下二阶三阶, 看一下对combined pnl的影响. 做着做着, 感觉实在太费时间, 就变成随便交了. 也没有去尝试新的idea, 可能也导致了提交的多样性不足. 看来之前的高value factor(虽然也不算太高) 是由于我花了巨多心思才勉强维持的, 并没法持续, 我整体的工作流还是问题非常大的.

==================================================================================

==================================================================================

---

### 探讨 #14: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025/08/02

今天终于下定决心写了任务中途插入回测的代码, 实际写起来比我想象中简单的多, 但是产生的新问题也不少. 比如我没有把所有任务统一管理, 而是完全放在不同的会话. 导致没法连续. 还有多次优化怎么进行, 现在还没有思路. 回测和收集结果现在完全分开, 如何把这个过程联系起来呢? 希望至少消融, 二阶, 三阶, 探索不同setting可以自动做. 不然实在太消耗人了.

_______________________________________________________________________________

_______________________________________________________________________________

---

### 探讨 #15: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025/08/07

能随时往数据库插入新的任务真是太好了, 把平时手动调参的流程固定化, 我都无脑的提交了两个alpha. 希望接下来能把二阶, 三阶加进工作流程. 看来目前主要的阻碍还是我没用元编程把插入流程配置成参数.

自从vf降到0.5左右, 也很久不挑sa了, 就用自己的alpha随便组一组.

====================================================================================

====================================================================================

---

### 探讨 #16: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025/08/08

昨天尝试了字段description的语义匹配, 还没有来得及回测实践. 为了能增加多样性, 我觉得应该再做数据集和region的区分. 还有字段类型的匹配也是必须做的. 目前glb交的alpha实在太少了, 而且全都是model类型, 希望语义匹配能从其他地区挖掘出一些在glb也能提交的alpha.

自从添加了自动消融表达式的插入流程, 反倒找了一些sharpe看着还行的alpha. 这两天都没有为提交alpha 发愁. 但是从这个季度就一直在跑USA, 一直在写代码. 有些新加的数据集看都没有看过. operator的整理工作也迟迟往后推...

==================================================================================

---

### 探讨 #17: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025/08/09

今天发现round这个operator我不理解, 好像会把nan变成一个奇怪的数, 但又不是-inf. 很迷惑... 平台上的operator经常会让我有这种无力感. 不知道在具体怎么运算的. 本来datafields也有, 拜lab所赐, 现在能看到数据所以没那么迷惑了. 感觉猜测operator用法浪费了太多时间...

把sa的category用llm标记后, 可以在组sa的时候用了, 还挺好用的. 今天没有交ra

==================================================================================

==================================================================================

---

### 探讨 #18: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025/08/24

把其他region的存货拿到glb跑, 很难跑出结果. 好几天只提交了sa. 手动改的话, 倒是可以改出一些, 但是实在太累, 不是个长久的方法. 至于为什么手动可以出的程序却跑不出, 应该是程序哪里出了问题. 但是我还没有发现. 除了model, 其他pyramid也很难跑出结果.

_______________________________________________________________________________

_______________________________________________________________________________

---

### 探讨 #19: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025/08/29

一直在修改priority任务的流程. 有些问题没有解决.

本地, 服务器, wq服务器的时间问题. 在本地数据库拉取result的时候可以和其他alpha的dateCreate对时间. 但是priority任务是随时插入的, 不在远程保存结果, 只能是我的代码服务器和wq筛选的时间对齐. 还没有解决.

operator替换问题. 之前的代码, 没有把expr -> ast 的流程拆干净. 消融和清理有部分代码没有复用.

流程问题. 当priority任务增加后, 前后顺序要怎么保证和管理. 消融也会产生大量result. 虽然也是alpha, 但是没有精力人工分析, 需要当成中间结果进行整合和删除.

一直把结果存在本地数据库, 但是最近数据库条目上了2w之后, 感觉加载变卡了. 接下来该怎么改善呢? 只加载最近一段时间的数据吗?

感觉我的alpha idea还是特别集中, 真正有意义能在各地区泛化的还是最开始做的时候和model数据. 随机跑出来的atom是不是真的信号, 感觉越来越分辨不出来.

==================================================================================

---

### 探讨 #20: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第九季.md
- **评论时间**: 5个月前

2026/01/21尝试添加了mcp和skills. 但是怎么说呢? 完全无法自动. mcp还稍好一些, 经过一些修正, 添加新功能不需要太多指令. skills是一个完全不可控的状态. 我想是因为skills自由度太高, 而且gemini说是适配了skills, 它模型不太理解skills究竟是什么. 尝试把项目的readme自动转成skills, 让人工和llm对齐, 结果是完全不可用. 如果自己写, 又要浪费许多工夫. 想必这些问题在大模型升级之后会自动解决吧...============================================================================================================================================================================

---

### 探讨 #21: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第九季.md
- **评论时间**: 5个月前

2026/01/21更新了os的结果, 发现大部分没有低头的alpha都是model数据. 说明wq的model还是比我自己用字段组合的效果好的多. 有些fundamental, analyst, is阶段表现真的很好, 很吸引人, 但是os阶段很糟糕.还有就是, 同一个数据集, 同一个字段, 我的alpha组合不同, 虽然is看起来接近, os却差距挺大的. 看表达式完全没觉得它们会差这么大, 特征尺度看起来真的接近============================================================================================================================================================================

---

### 探讨 #22: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第九季.md
- **评论时间**: 5个月前

2026/01/22尝试在lab直接找字段. 效果还可以, 但是有几个问题.1. lab的字段不全, 很多数据集是缺字段的. 新出的ind甚至全是4042. lab有时限, 大概一次只能看一个数据集. 今天看了一半掉线了, 上去之后之前的结果居然还在, 也很不容易了. 多了会卡掉线.3. 我复现的daily pnl不仅算的慢, 结果也差很多...============================================================================================================================================================================

---

### 探讨 #23: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第九季.md
- **评论时间**: 5个月前

2026/01/23发现我的daily pnl算的结果完全不对, 是因为我把其中一个矩阵转置导致计算错了... 其实速度是正常的. 但是算出来sharpe和pnl单位差很多?最近wq更新了os, 在更新数据库的时候, 总感觉特别麻烦. 虽然可以让skills和我自然语言交互. 可是skills没法全自动的写完, 总之就还是很麻烦.============================================================================================================================================================================

---

### 探讨 #24: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第九季.md
- **评论时间**: 4个月前

2026/01/19今天看了cnhk的skills, 用gemini cli跑了一下, 对比之下也发现了一些自己的流程没做好的部分.  虽然gemini cli对skills支持的并不好...感觉关键还是在于任务拆分的颗粒度. 从资料到idea/template到alpha真的把中间拆出来会比较好吗? 不拆的好处是可以确保operator的正确使用, 坏处是过于遵循给定的operator了. 拆的好处是idea更广泛, 坏处是最后用operator 合成alpha, 总会曲解idea的意思.============================================================================================================================================

---

### 探讨 #25: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026/01/21

尝试添加了mcp和skills. 但是怎么说呢? 完全无法自动. mcp还稍好一些, 经过一些修正, 添加新功能不需要太多指令. skills是一个完全不可控的状态. 我想是因为skills自由度太高, 而且gemini说是适配了skills, 它模型不太理解skills究竟是什么. 尝试把项目的readme自动转成skills, 让人工和llm对齐, 结果是完全不可用. 如果自己写, 又要浪费许多工夫. 想必这些问题在大模型升级之后会自动解决吧...

======================================================================================

======================================================================================

---

### 探讨 #26: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026/01/21

更新了os的结果, 发现大部分没有低头的alpha都是model数据. 说明wq的model还是比我自己用字段组合的效果好的多. 有些fundamental, analyst, is阶段表现真的很好, 很吸引人, 但是os阶段很糟糕.

还有就是, 同一个数据集, 同一个字段, 我的alpha组合不同, 虽然is看起来接近, os却差距挺大的. 看表达式完全没觉得它们会差这么大, 特征尺度看起来真的接近

======================================================================================

======================================================================================

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026/01/22

尝试在lab直接找字段. 效果还可以, 但是有几个问题.

1. lab的字段不全, 很多数据集是缺字段的. 新出的ind甚至全是404

2. lab有时限, 大概一次只能看一个数据集. 今天看了一半掉线了, 上去之后之前的结果居然还在, 也很不容易了. 多了会卡掉线.

3. 我复现的daily pnl不仅算的慢, 结果也差很多...

======================================================================================

======================================================================================

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026/01/23

发现我的daily pnl算的结果完全不对, 是因为我把其中一个矩阵转置导致计算错了... 其实速度是正常的. 但是算出来sharpe和pnl单位差很多?

最近wq更新了os, 在更新数据库的时候, 总感觉特别麻烦. 虽然可以让skills和我自然语言交互. 可是skills没法全自动的写完, 总之就还是很麻烦.

======================================================================================

======================================================================================

---

### 探讨 #29: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026/01/19

今天看了cnhk的skills, 用gemini cli跑了一下, 对比之下也发现了一些自己的流程没做好的部分.  虽然gemini cli对skills支持的并不好...

感觉关键还是在于任务拆分的颗粒度. 从资料到idea/template到alpha真的把中间拆出来会比较好吗? 不拆的好处是可以确保operator的正确使用, 坏处是过于遵循给定的operator了. 拆的好处是idea更广泛, 坏处是最后用operator 合成alpha, 总会曲解idea的意思.

======================================================================

======================================================================

---

### 探讨 #30: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/6/15

今天改一下后端代码, 把显式在代码里调用的环境配置移到配置文件里. 不过发现还是很难全部模块化.

没有提交alpha.

---

### 探讨 #31: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/6/18

今天把代码本地编译了一下, 发现还是有些地方没有解耦, 可读性有待提高. 提交了一个glb的ra, 凑够了20个pyr.

做ace的sa衰减明显, 但是有些select又不那么明显, 我在combo里复现不出来. 还是因为我select选的不够多么?

---

### 探讨 #32: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/19

今天用github actions进行macos和windows系统的release, 发现非常方便. 但是ubuntu系统中, 好多和桌面显示相关的库需要额外搭配就很麻烦, 尝试了一下最终放弃了. release出来的app用mac是可以正常打开, 不过windows的exe还是有些问题...

ace的sa感觉换了不同neutralize影响非常大, 如果可以同时使用多种neutralize就好了. 不同的selection影响也非常大, 感觉turnover高的alpha的returns和稳定性都差了相当多. 相反combo影响倒不大了, 看来还是因为我对combo的计算过程不是很理解.

---

### 探讨 #33: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/20

今天尝试复现RAM中性化, 试了各种momentum returns:
ts_returns(close,252)

ts_returns(close-group_mean(close,cap,market),252) 和各种变形

rsk70_mfm2_euetrd_momentum

ts_product(1 + mdl25_pcv421_71v / 100, 252) - 1

也试了各种operator,

beta_mom = group_sum(normalize(signal_o)*normalize(momentum),market)/group_sum(power(normalize(momentum),2),market);

还是无法达到RAM的效果. 具体说就是有的alpha用了RAM中性化后消除了2020年6月附近非常明显的spike, 效果很好. 但是我自己实现的就完全不行. 想不通关键问题出在哪里... 并且在我实现的一些momentum上也可以观测到这个spike, 但是做线性拟合却消除不掉?

---

### 探讨 #34: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/6/21

今天突然想试试自制厂, 看看能不能os, corr双赢. 发现还是比我想的麻烦的多, 这看起来只是条弯路不是捷径.

看来我们的提交系统比我想的坚挺, 虽然可能不是故意的, 我想是因为加速计算的各种噪声导致的.

---

### 探讨 #35: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/22

今天翻论坛发现, 有人说combo_a(algo1) 用的是Markowitz model. 按我的理解就是最大化250天的组合sharpe呗. 假设无风险的话, 应该是self_corr(returns)^{-1}*ts_mean(returns) 吧? 我们平台上combo应该不支持矩阵运算, 而且, 这跟我观察到的combo_a的表现不太一样... 实际上combo_a(alpha)=combo_a(-alpha) , 如果是Markowitz model应该是投资组合反过来吧

今天把RAM neutral在以前交过的alpha上跑了一遍, 交了一个d0 alpha.

---

### 探讨 #36: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/24

今天SAC 开了新的主题, atom, 在2022年之前和欧洲地区都表现很差, 只有2023年之后的USA看着还行... 欧洲怎么做都只有10几, 而欧洲的alpha数也很多. 看排行榜上的分数, atom应该是比ppac还要领先, 说明我和做的好的差距更大...

atom的特点是alpha数很多, limit不管开了多少, 怎么选都是满的. 限制turnover在0.1以内竟然都有几百alpha. selection突然变得重要很多.

---

### 探讨 #37: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/25

和老师约了1v1, 讨论了我一直以来的一个困惑, 原来是我没有理解好回测的交易过程导致的. sac不知道为什么断了一天, 好奇怪一点关于断的记忆也没有. atom 感觉真的特别难做... 前几周, 光做USA的时候, 改改表达式感觉prod corr根本不是限制. 做ASI, GLB的时候, 只要表达式不是1, 很容易就报corr过不去. 可能是用等权的原因, 就感觉经常跟别人撞车心态爆炸...

- ==============================================================================================================================================================================================================================================================================================================================================================================================================================================

---

### 探讨 #38: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/27

atom主题已经交了好几天0.7以上的sa了, glb的return和margin太低不敢交. 一直在交asi和eur. 我的combine到后段一个拐弯变得非常平, 感觉心里很慌

ra也断了好几天了.

=======================================================================

=======================================================================

=======================================================================

---

### 探讨 #39: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/29

做了一周感觉有点熟悉atom的selection了, 现在可以选到15-18return的super alpha了, 感觉有进步. usa的return甚至可以达到30多, drawdown 2点多. 每次改参数, 感觉都是return和drawback的trade off. combined pnl最后的走平感觉交多少个都没变化. 还有combined一些drawdown也不见能解决的希望. 怎么能选到和我combined大趋势更不同的alpha呢?

有一周多没提交ra, 感觉master已经没希望了, 想开点, 下个赛季从expert开始努力吧💪

=======================================================================

=======================================================================

---

### 探讨 #40: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

2025/06/30

看了论坛复现因子日历的帖子, 本来雄心勃勃觉得我上我也行, 但是这也太难了. 从一阶到2阶3阶对我有巨大的gap, 没明白怎么把一个看起来很差的alpha优化优化就变得非常好...

sa又继续交了asi, 因为总感觉最后combine的走平是我交了太多usa导致的, 想交别的地区中和一下. 但是turnover和margin都不怎么好.

=======================================================================

=======================================================================

---

### 探讨 #41: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025/10/13

在整理代码, 和写文档. 发现很多对api的调用应该统一处理. 其实平台的api是特别简单的, 有些地方是我写的复杂. 每次开一个python脚本需要100M多的内存, 最近感觉服务器的内存不够用了. 
又好几天没有交alpha了. 虽说平台鼓励交atom, 但是除了单数据字段, 在同一个数据集组合字段感觉难度更高. 单数据字段又还是那些看着眼熟的字段, 跑了很多eur的数据, 感觉在数据不多的category实在没法交单数据字段的alpha.

===================================================================================

===================================================================================

===================================================================================

---

### 探讨 #42: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025/10/15

从昨天开始完全没法提交alpha. 看别人似乎没有这个问题. 我的代码, 我的账号, 我做错了什么吗? 真是感到费解.

=======================================================================

=======================================================================

---

### 探讨 #43: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025/10/19

把vscode插件更新了一下, 加上了sa的提示. 既然功能多了, 代码也重构了一下, 拆了一些模块出来. 不过classification/competitions/theme 没找到对应的api没拿到. 深深的感觉sa selection写起来非常烦, 谁会有耐心去文档找那些东西呢...导致从这个赛季开始就没什么心情交sa了.

这几天提交变快了. 但是我还是没有提交很多, 时间非常紧迫. 我的simulation代码其实需要重构, 但是有点担心改出问题影响回测. 没想到100多行的代码让我有这种顾虑😂.

=======================================================================

=======================================================================

---

### 探讨 #44: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025/10/20

本来想这个月把代码整理好的. 感觉时间非常紧张. 想做eur地区的option数据, 但是总需要多个datafields, vector每个datafield都要增加一个operator, 很难达标ppa.
=======================================================================

=======================================================================

---

### 探讨 #45: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025/10/22

今天开始做jpn地区了. jpn竟然这么难做么. 不仅回测的速度比我想象中的慢很多, 可以提交的alpha也很少. 跑了一晚上一无所获, 还以为是程序bug了. 看来bug的不是程序而是我的思路.

最近在一阶把随机性调的非常大, 发现会漏掉一些数据集, 即, 虽然理论上在我的模版覆盖中, 但是因为搜索范围太广, 不是反复出现的idea就很容易搜索不到. 我的代码走向另一个极端了吗?

============================================================================

============================================================================

---

### 探讨 #46: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025/10/24

总算从<0.5 的vf出来了. 看来是我5月交的alpha出了大问题. 但是我一直没做alpha关于时间的统计, 已经记不得交了什么了. 感觉很急需做一个了.

=======================================================================

=======================================================================

---

### 探讨 #47: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

2024/11/02

IND开了, 交了两个alpha.

每次做比赛主题, 包括之前的ppac和现在的aiac, 就感觉自己的alpha idea太集中了. 可以说除了从做consultant开始一个月会积极探索新的idea以外, 一直交的都是重复的, 已经有的. 包括很多pyramid 区域, 更是现在都没什么好办法做. 完全没有正反馈.

=======================================================================

=======================================================================

---

### 探讨 #48: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

2024/11/03

发现aiac组出来的sa比我ra还差, 是因为我大部分都在同一字段搜索, 导致alpha太相似的原因吗? 我应该找大的数据集, 去数据集里搜索吗? 之前感觉时间有的是也没有在意, 能交就交了. 看来还是应该保证sa的多样性才行啊. 话又说回来, 有很多alpha在附近搜索过才发现, 本身的idea根本站不住脚. 比如anl数据经常是因为覆盖率不够, nan本身拉高了表现, 这种alpha信号本来就极度压缩了, 再换operator也不会有什么好结果.

=======================================================================

=======================================================================

---

### 探讨 #49: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 7个月前

2024/11/06

每天都在外面玩, 连打开网页, 或者发新回测的时间都没有. 代码虽然经常改, 能感觉到它在越变越好, 但是问题也总是出现.
我在想代码用传统的文件夹分级是否合理呢? 现在流行的笔记软件的用法是tag而不是层级, 一个笔记可以有多个tag, 那代码这么做的难点在哪呢? 最明显的是和python 的import机制不搭调. 依赖关系追踪复杂, 每次改变依赖关系预编译都会失效. python新的版本似乎和这个想法背道而驰, 不仅不会变的更动态, 还一直在加入新的预编译功能提速.

=======================================================================

=======================================================================

---

### 探讨 #50: 关于《【日常生活贴】我的量化日记第八季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第八季.md
- **评论时间**: 6个月前

2025/12/22又到了年底new year resolution的时间了. 今年真是在wq浪费了大量时间, 在那些一次性的, 用不上的事情上. 最近更是因为genius赛季末了, 因为要点塔, 浪费了更多时间. 总是倾向于做那些简单不用动脑子的事情, 而真正需要花费时间的却一拖再拖. 如果说工作给人一种“自己真的完成了什么”的错觉, wq也是一样. 指标和真正有趣的事往往背道而驰. 希望明年能更合理的利用时间.--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #51: 关于《【日常生活贴】我的量化日记第八季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第八季.md
- **评论时间**: 6个月前

2025/12/14终于点满了60个塔了. 辛苦的20天.发现我比赛的selection每天的EUR都负的好多, 想调查一下为什么, 但是事情越积越多. 最近wq的培训真的好多, 虽然内容比较雷同, 但是因为自己还没做, 每次都感觉焦虑.====================================================================================================================================================================================

---

### 探讨 #52: 关于《【日常生活贴】我的量化日记第八季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第八季.md
- **评论时间**: 6个月前

2025/12/25今天圣诞节了.在写筛选alpha的界面, 真是烦躁. 深感自己的效率太低了. 至于我效率为什么这么低, 想必是因为我对前端不熟悉, 有些东西即使让AI做, 我没法精准的描述. 如果能快速的让AI完成任务, 自己也需要是专家才行.还有就是llm没法直接查看我app的log, 虽然我tauri生成的应该也是用浏览器之类的内核...之前试了playwright mcp, 还是不行. 没法查看dom, 也没法查看界面.====================================================================================================================================================================================

---

### 探讨 #53: 关于《【日常生活贴】我的量化日记第八季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第八季.md
- **评论时间**: 6个月前

2025/12/25在听community leader的培训. 每次真的很疑惑. 看到大佬们总是又用AI, 又用了大量手动, 又花了钱.... AI在里面到底起了什么作用? 因为AI不听话, 我每次调用llm真是非常疲劳, 比不用AI还疲劳.... 完全不像代码, 只要实现了一个功能就可以放心了. 至少实现了多少就放心了多少, AI的调教又累人, 又无法复用. 如果AI是笨蛋, 真的值得花很多时间跟它交流吗?====================================================================================================================================================================================

---

### 探讨 #54: 关于《【日常生活贴】我的量化日记第八季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第八季.md
- **评论时间**: 6个月前

2025/12/25看到别人weight上的很快, 我的weight已经很久不动了. 虽然到了两位数, 但是rank已经很久不动了. 交的alpha也比较少, 还有希望吗?已经好几天没提交alpha了. base太少了, 连sa也不想做.====================================================================================================================================================================================

---

### 探讨 #55: 关于《【日常生活贴】我的量化日记第八季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第八季.md
- **评论时间**: 6个月前

2025/12/27今天一定要在周末刷新钱把submitted alpha筛选完. 互相关性测不了就下周吧. 买了google one的一年优惠, 希望能给我提升点效率.====================================================================================================================================================================================

---

### 探讨 #56: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/22

又到了年底new year resolution的时间了. 今年真是在wq浪费了大量时间, 在那些一次性的, 用不上的事情上. 最近更是因为genius赛季末了, 因为要点塔, 浪费了更多时间. 总是倾向于做那些简单不用动脑子的事情, 而真正需要花费时间的却一拖再拖. 如果说工作给人一种“自己真的完成了什么”的错觉, wq也是一样. 指标和真正有趣的事往往背道而驰. 希望明年能更合理的利用时间.

-------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------

---

### 探讨 #57: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/14

终于点满了60个塔了. 辛苦的20天.

发现我比赛的selection每天的EUR都负的好多, 想调查一下为什么, 但是事情越积越多. 最近wq的培训真的好多, 虽然内容比较雷同, 但是因为自己还没做, 每次都感觉焦虑.

============================================================

============================================================

============================================================

---

### 探讨 #58: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/25

今天圣诞节了.

在写筛选alpha的界面, 真是烦躁. 深感自己的效率太低了. 至于我效率为什么这么低, 想必是因为我对前端不熟悉, 有些东西即使让AI做, 我没法精准的描述. 如果能快速的让AI完成任务, 自己也需要是专家才行.
还有就是llm没法直接查看我app的log, 虽然我tauri生成的应该也是用浏览器之类的内核...之前试了playwright mcp, 还是不行. 没法查看dom, 也没法查看界面.

============================================================

============================================================

============================================================

---

### 探讨 #59: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/25

在听community leader的培训. 每次真的很疑惑. 看到大佬们总是又用AI, 又用了大量手动, 又花了钱.... AI在里面到底起了什么作用? 因为AI不听话, 我每次调用llm真是非常疲劳, 比不用AI还疲劳.... 完全不像代码, 只要实现了一个功能就可以放心了. 至少实现了多少就放心了多少, AI的调教又累人, 又无法复用. 如果AI是笨蛋, 真的值得花很多时间跟它交流吗?

============================================================

============================================================

============================================================

---

### 探讨 #60: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/25

看到别人weight上的很快, 我的weight已经很久不动了. 虽然到了两位数, 但是rank已经很久不动了. 交的alpha也比较少, 还有希望吗?

已经好几天没提交alpha了. base太少了, 连sa也不想做.

============================================================

============================================================

============================================================

---

### 探讨 #61: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025/12/27

今天一定要在周末刷新钱把submitted alpha筛选完. 互相关性测不了就下周吧. 买了google one的一年优惠, 希望能给我提升点效率.

============================================================

============================================================

============================================================

---

### 探讨 #62: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

2025/10/02

又到新赛季了. 每次想把代码整理好但是一直拖延. 代码越写越多, 有点产生认知负担. 希望在开始的一个月能整理好.

刚发现alpha id的生成规律, 没想到平台又变了. 我成小丑了.

今天交了3个glb的alpha, 没心情做sa了. 之前交的ra太少, 感觉sa有点到瓶颈了. glb的小category还没做, 一直在做model和pv.

=======================================================================

=======================================================================

---

### 探讨 #63: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

2025/10/03

今天没跑出可以正常交的glb alpha. 只能交几个eur的存货. 我的glb 的pool表现非常糟糕. 尤其是EMEA地区的表现, 很多alpha都是卡在这个地区. 之前在eur交的alpha转移到glb, 和EMEA地区的表现差距也非常大, 不理解为什么.

=======================================================================

=======================================================================

---

### 探讨 #64: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 8个月前

2025/10/08

更新了combined. 终于从1.多的combine出来了. 我觉得是8月份gac交了10多个glb的功劳. 我也非常意外, 一直以为是usa d0不稳定导致的, 以为在我d0做到稳定之前, combined没法提升了, 原来不是吗?!

=======================================================================

=======================================================================

---

### 探讨 #65: 关于《全局变量保存调度器实例_scheduler = Nonedef start_scheduler():    global _scheduler    避免在 reloader 进程中启动调度器，避免启动两次    if os.environ.get('RUN_MAIN') == 'true':        print("This is the reloader process. Scheduler not started.")        return    if _scheduler is not None:        print("Scheduler already running.")        return    _scheduler = BackgroundScheduler()    from app01.utils.util_funcs import count_perHour    每小时整点运行一次任务    _scheduler.add_job(        count_perHour,        'cron',        minute=0  整点执行    )    _scheduler.start()    print("Scheduler started and will run every hour at :00")》的评论回复
- **帖子链接**: [Commented] 打造自己的BrainAdmin用手机也能管理回测代码运行经验分享.md
- **评论时间**: 0年前

你简直是我知己! 我也是用前端传参管理模版, 除了我功能没这么多. 不支持这么多设备, 还有我不是用子进程, 是直接用tmux会话启停单个儿模版任务的

=================================================================================

---

### 探讨 #66: 关于《全局变量保存调度器实例_scheduler = Nonedef start_scheduler():    global _scheduler    避免在 reloader 进程中启动调度器，避免启动两次    if os.environ.get('RUN_MAIN') == 'true':        print("This is the reloader process. Scheduler not started.")        return    if _scheduler is not None:        print("Scheduler already running.")        return    _scheduler = BackgroundScheduler()    from app01.utils.util_funcs import count_perHour    每小时整点运行一次任务    _scheduler.add_job(        count_perHour,        'cron',        minute=0  整点执行    )    _scheduler.start()    print("Scheduler started and will run every hour at :00")》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 打造自己的BrainAdmin用手机也能管理回测代码运行经验分享_33454849256599.md
- **评论时间**: 1年前

你简直是我知己! 我也是用前端传参管理模版, 除了我功能没这么多. 不支持这么多设备, 还有我不是用子进程, 是直接用tmux会话启停单个儿模版任务的

=================================================================================

---

### 探讨 #67: 关于《本地表达式语法检测程序的初步尝试代码优化》的评论回复
- **帖子链接**: [Commented] 本地表达式语法检测程序的初步尝试代码优化.md
- **评论时间**: 7个月前

Vibe Coding能做到这个完成度太厉害了! 流程已经挺专业的了. 我之前也尝试过用AI写ast代码, 效果差多了, 有很明显的错误它就是不改.

您用的是哪个llm?

我看你的parser是用递归的方式解析的, 我觉得这种写法会导致后续扩展的时候比较难维护, 比如解析三元表达式(...?...:...)的时候. 我建议是用pratt parser, 我自己用的是这种方法, 代码很简洁, 可读性高...不过llm不像人那么在乎可读性.

---

### 探讨 #68: 关于《本地表达式语法检测程序的初步尝试代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 本地表达式语法检测程序的初步尝试代码优化_36310472781463.md
- **评论时间**: 7个月前

Vibe Coding能做到这个完成度太厉害了! 流程已经挺专业的了. 我之前也尝试过用AI写ast代码, 效果差多了, 有很明显的错误它就是不改.

您用的是哪个llm?

我看你的parser是用递归的方式解析的, 我觉得这种写法会导致后续扩展的时候比较难维护, 比如解析三元表达式(...?...:...)的时候. 我建议是用pratt parser, 我自己用的是这种方法, 代码很简洁, 可读性高...不过llm不像人那么在乎可读性.

---
