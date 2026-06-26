# 顾问 WX84677 (Rank 69) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 WX84677 (Rank 69) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: 附录：所有函数速查表)
- **原帖链接**: https://support.worldquantbrain.com[Commented] DCC比赛Tutorial和代码详解代码优化_38631459115543.md
- **时间**: 3个月前

**提问/主帖背景 (YZ64617)**:
## 写在前面的废话

DCC比赛之后，官方发布了3个版本的代码。第一版是Bigdata在github上的tutorial修改而来。之后的2个版本分别增加了 **Workflow_multi_theme_sentiment** 和 **Competition_Full_Workflow_Demo** 。新增的这2个文件夹是一个相对完整的针对这次比赛的例子。

比赛代码会用到bigdata-research-tools 和bigdata-client包。bigdata有详细的文档和代码例子。

- [Bigdata官方文档]([链接已屏蔽])
- [Bigdata Cookbook]([链接已屏蔽]) ：它们的github中，还有不少资源可以借鉴。

**个人的一些理解和可能的坑** ：

- LLM不是必须的，但我感觉使用LLM会增加数据量化的准确性
- Brain给出的2个完整的例子并没有使用LLM
- 包含LLM使用的例子在Workflow_example中，源头来自Bigdata的cookbook
- Bigdata依赖包是支持自定义openai兼容接口的模型的
- 在这里定义  *`from bigdata_research_tools.llm.base import LLMConfig* ` （可以让AI帮你写）
- LLM调用在代码中，默认10线程并行，大家注意。根据自用的模型进行设定。token消耗量，会是比较大的，且运行时间会长。
- 有可能，在notebook中运行LLM相关功能时，代码会报错。大概是涉及到异步的问题。经过CC的多次尝试，不修改依赖包 *bigdata_research_tools.llm* 下的文件似乎是无法解决的。所以，CC最后把项目文件夹内的venv内的依赖包给改了。如果大家遇到这个情况，请根据自身情况来决定。猜测，可能和notebook中运行代码有关。

下面的正文是我多次与CC对话和修改代码的过程中生成的。希望对大家有帮助。里面有一些小瑕疵。

## 目录

- 第一章：背景知识——你需要先理解这些
  - 1.1 这是什么比赛
  - 1.2 什么是量化信号
  - 1.3 NLP与新闻数据在金融中的应用
  - 1.4 关键术语表
- 第二章：环境搭建
  - 2.1 安装 Python 和 uv
  - 2.2 创建虚拟环境并安装依赖
  - 2.3 配置凭据
  - 2.4 启动 Jupyter Notebook
- 第三章：项目整体架构
  - 3.1 文件夹结构总览
  - 3.2 核心管线流程图
  - 3.3 外部依赖库说明
- 第四章：四大API详解
  - 4.1 认证机制——BrainSession
  - 4.2 Search API——语义搜索
  - 4.3 Volume API——聚合计数
  - 4.4 CoMentions API——共现发现
  - 4.5 Knowledge Graph API——知识图谱
- 第五章：Smart Batching——大规模高效搜索
  - 5.1 为什么需要批量搜索
  - 5.2 SmartBatchingPlanner 工作原理
  - 5.3 搜索执行与限速
  - 5.4 关键函数一览
- 第六章：Workflow_example——LLM辅助端到端工作流
  - 6.1 Step 1：主题思维导图生成
  - 6.2 Step 2：搜索规划与执行
  - 6.3 Step 3：实体提取与过滤
  - 6.4 Step 4：公司名称掩码
  - 6.5 Step 5：LLM标注与验证
  - 6.6 Step 6：滚动信号构建
  - 6.7 最终输出解读
- 第六点五章：Workflow_multi_theme_sentiment——多主题情感+BRAIN上传
  - 6.5.1 这个模块有什么不同？
  - 6.5.2 工作流六步走
  - 6.5.3 主题定义——正交主题设计
  - 6.5.4 实体归因机制
  - 6.5.5 复合信号构建
  - 6.5.6 数据质量验证
  - 6.5.7 上传到BRAIN
- 第六点七五章：Competition_Full_Workflow_Demo——比赛完整工作流演示
  - 6.75.1 这个模块的定位
  - 6.75.2 工作流五步走
  - 6.75.3 评分机制
  - 6.75.4 MATRIX vs VECTOR 上传
  - 6.75.5 三套工作流对比
- 第七章：经济学与金融逻辑
  - 7.1 新闻情感与股价的关系
  - 7.2 主题选择的策略思考
  - 7.3 信号质量评估
- 第八章：比赛实战指南
  - 8.1 比赛流程
  - 8.2 学习路径建议
  - 8.3 进阶优化方向
- 附录：所有函数速查表

# 第一章：背景知识——你需要先理解这些

## 1.1 这是什么比赛

**Bigdata.com & WorldQuant Data Creation Challenge 2026**  (简称 DCC2026) 是一个量化研究比赛。

**比赛要求你做的事** ：

1. 利用 Bigdata.com 提供的新闻数据API，挖掘新闻中的信息
2. 构建"量化信号"——一组数字，代表每家公司每天受某个主题影响的程度
3. 将信号上传到 WorldQuant Brain 平台，进行模拟回测（simulation）
4. 系统根据信号的预测能力给你打分

**通俗理解** ：想象你是一个基金经理的助手。每天有海量新闻，你需要从中提炼出"哪些公司因为某个主题（比如AI芯片短缺）受到了正面或负面影响"，然后把这个判断量化为一个数字信号。

## 1.2 什么是量化信号

量化信号（Quantitative Signal）是一个时间序列数据，格式如下：

公司名称
日期
信号值

Apple Inc.
2021-01-15
0.75

Apple Inc.
2021-01-16
0.62

Tesla Inc.
2021-01-15
-0.30

- **正值** ：表示该公司在这个主题下收到了正面影响（好消息多）
- **负值** ：表示负面影响（坏消息多）
- **接近零** ：表示中性或无明显影响

在本项目中，最终输出的信号是  `signal_7d` （7天滚动均值）和  `signal_30d` （30天滚动均值）。

## 1.3 NLP与新闻数据在金融中的应用

**为什么新闻数据有价值？**

传统量化投资依赖价格、成交量等数字数据。但新闻包含了市场参与者的预期、事件发展、政策变化等"软信息"。通过自然语言处理（NLP）技术，可以从海量文本中提取情感、主题、影响力等信息。

**核心思路** ：

```
新闻报道 → NLP分析 → 情感/影响判断 → 量化信号 → 交易决策

```

**例子** ：

- 新闻："芯片短缺导致汽车制造商减产" → 对汽车公司是 **负面** 消息
- 新闻："苹果公司发布创新AR眼镜，市场反响热烈" → 对Apple是 **正面** 消息

## 1.4 关键术语表

术语
英文
含义

chunk
Chunk
文档中的一个文本片段，是搜索API返回的基本单位

实体
Entity
新闻中提到的公司、人物、地点等，每个有唯一ID

实体宇宙
Entity Universe
你关注的公司集合（本项目用美国前3000家公司）

语义搜索
Semantic Search
基于含义（而非关键词匹配）的搜索

共现
Co-mention
两个实体在同一段文本中被同时提到

思维导图
MindMap
将一个大主题拆分成若干子主题的树形结构

滚动窗口
Rolling Window
用过去N天的数据计算的统计值（如7天平均值）

前瞻偏差
Look-ahead Bias
在回测中使用了未来才能知道的信息——必须避免

时间点一致
Point-in-time
只使用当时已知的信息，不偷看未来

LLM
Large Language Model
大语言模型，如GPT-4o-mini，用于理解和标注文本

basket
Basket
一组公司的集合，打包在一起发送搜索请求

# 第二章：环境搭建

## 2.1 安装 Python 和 uv

**Python** ：需要 Python 3.10 或更高版本。到  [python.org]([链接已屏蔽])  下载安装。

**uv** ：一个极快的 Python 包管理器（替代 pip），安装方式：

```
# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm [链接已屏蔽] | iex"

# 或者用 pip 安装
pip install uv

```

## 2.2 创建虚拟环境并安装依赖

```
# 进入项目根目录
cd DCC2026_v1

# 创建虚拟环境
uv venv .venv

# 激活虚拟环境
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 安装所有依赖（使用根目录下的整合版 requirements.txt）
uv pip install -r requirements.txt

```

安装完成后，你应该能看到类似 "Installed 137 packages" 的信息。

## 2.3 配置凭据

每个模块文件夹下都有一个  `.env.example`  文件。你需要：

```
# 复制模板文件
cp .env.example .env

# 编辑 .env 文件，填入你的凭据
BRAIN_EMAIL=你的注册邮箱
BRAIN_PASSWORD=你的密码

```

**如何获取凭据** ：到  [WorldQuant Brain]([链接已屏蔽])  注册账号。比赛参与者会获得API访问权限。

**Workflow_example 额外需要** （可选）：

```
OPENAI_API_KEY=你的OpenAI密钥

```

这是用于LLM标注步骤的。如果没有，可以跳过LLM验证步骤。

> **重要** ：每个模块文件夹（Search_API、Volume_API 等）都需要各自配置  `.env` ，因为它们是独立运行的。

## 2.4 启动 Jupyter Notebook

```
# 确保虚拟环境已激活
jupyter notebook

```

浏览器会自动打开，你可以导航到任何模块文件夹打开对应的  `.ipynb`  文件。

# 第三章：项目整体架构

## 3.1 文件夹结构总览

```
DCC2026_v1/
│
├── Search_API/                   # 模块1：语义搜索教程
│   ├── Search_API_Tutorial.ipynb # Jupyter教程notebook
│   ├── session.py                # 认证会话类
│   ├── api_helpers.py            # API调用辅助函数
│   ├── print_helpers.py          # 结果打印辅助函数
│   ├── .env.example              # 环境变量模板
│   └── requirements.txt          # 本模块依赖
│
├── Volume_API/                   # 模块2：聚合计数教程
│   ├── Volume_API_Tutorial.ipynb
│   ├── session.py
│   ├── api_helpers.py
│   ├── print_helpers.py
│   └── ...
│
├── CoMentions_API/               # 模块3：共现发现教程
│   ├── CoMentions_API_Tutorial.ipynb
│   └── ...
│
├── Knowledge_Graph_API/          # 模块4：知识图谱教程
│   ├── Knowledge_Graph_API_Tutorial.ipynb
│   └── ...
│
├── Smart_Batching/               # 模块5：大规模批量搜索
│   ├── test_smart_batching.ipynb
│   ├── session.py
│   ├── src/
│   │   ├── smart_batching.py     # 分批规划器（1366行核心代码）
│   │   ├── search_function.py    # 搜索执行器（1032行核心代码）
│   │   ├── smart_batching_config.py  # 配置常量
│   │   └── output_converter.py   # 输出格式转换
│   └── id_name_mapping_us_top_3000.csv  # 实体宇宙数据
│
├── Workflow_example/             # 模块6：LLM辅助端到端工作流
│   ├── Workflow_example.ipynb    # 完整工作流教程
│   ├── session.py
│   ├── df_rolling_signal.csv     # 示例信号输出
│   ├── id_name_mapping_us_top_3000.csv
│   └── src/
│       ├── helper.py             # 通用辅助函数（实体处理、信号构建、可视化）
│       ├── search_function.py    # 搜索执行（带限速和并发控制）
│       ├── smart_batching.py     # 分批规划
│       ├── smart_batching_config.py
│       ├── output_converter.py
│       ├── processing_results.py # 搜索结果处理
│       ├── mindmap/
│       │   ├── mindmap.py        # MindMap数据结构
│       │   ├── mindmap_generator.py  # 思维导图生成器
│       │   └── mindmap_utils.py  # 提示词模板和工具
│       ├── labeler/
│       │   └── screener_labeler.py  # LLM标注器
│       └── prompts/
│           └── labeler.py        # 所有提示词模板
│
├── Workflow_multi_theme_sentiment/  # 模块7：多主题情感 + BRAIN上传
│   ├── Workflow_multi_theme_sentiment.ipynb  # 完整多主题工作流
│   ├── session.py               # 增强版认证（支持2FA）
│   ├── universe.json            # 3435个实体ID
│   └── .env.example             # 环境变量模板
│
├── Competition_Full_Workflow_Demo/  # 模块8：比赛完整工作流演示（★新增）
│   ├── DataCreationCompetition_workflow.ipynb  # 精简比赛工作流
│   ├── session.py               # 增强版认证（支持2FA）
│   ├── universe.json            # ~3000个实体ID
│   ├── requirements.txt         # 模块依赖
│   ├── .env.example             # 环境变量模板
│   └── README.md                # 模块说明
│
└── tutorial/                     # 本教程文件夹
    └── step_by_step_guide.md     # 你正在读的这个文件

```

## 3.2 核心管线流程图

整个项目要做的事情，用一张图概括：

```
┌─────────────────────────────────────────────────────────────┐
│                    第一阶段：数据获取                         │
│                                                             │
│  选择主题 ──→ 生成思维导图 ──→ 拆分为子主题                    │
│  (你的创意)   (LLM生成)        (如"AI芯片 → 供应链、研发...")  │
│                                                             │
│       ↓                                                     │
│  智能分批规划 ──→ 语义搜索执行 ──→ 获取新闻chunk               │
│  (优化API调用)   (并行+限速)      (文本片段+情感分数)          │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│                    第二阶段：数据处理                         │
│                                                             │
│  实体提取 ──→ 公司过滤 ──→ 名称掩码 ──→ LLM标注              │
│  (从chunk中)  (只留宇宙内)  (防偏见)    (判断正面/负面)        │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│                    第三阶段：信号构建                         │
│                                                             │
│  影响评分 ──→ 日度聚合 ──→ 滚动均值 ──→ 信号表               │
│  (+1/-1/0)   (每公司每天)  (7天/30天)    (最终输出)           │
└─────────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────────┐
│                    第四阶段：比赛提交                         │
│                                                             │
│  路径A (Workflow_example):                                   │
│  信号表 ──→ 格式转换 ──→ 上传Brain平台 ──→ Simulation评分     │
│  (代码产出)  (你需自己写)   (平台操作)      (系统自动)         │
│                                                             │
│  路径B (Workflow_multi_theme_sentiment): ★推荐★              │
│  MATRIX数据 ──→ Parquet打包 ──→ 自动上传BRAIN ──→ Simulation │
│  (代码自动)     (代码自动)       (代码自动)        (系统自动)  │
│                                                             │
│  路径C (Competition_Full_Workflow_Demo): ★最简单★            │
│  日度抓取 ──→ 评分 ──→ MATRIX+VECTOR上传 ──→ Simulation      │
│  (代码自动)  (代码自动)  (代码自动)            (系统自动)      │
└─────────────────────────────────────────────────────────────┘

```

> **注意** ：
> - **路径A** （Workflow_example）：代码覆盖前三个阶段，第四阶段的格式转换和上传需要你自行实现。
> - **路径B** （Workflow_multi_theme_sentiment）：代码覆盖 **全部四个阶段** ，包括自动上传到BRAIN！适合想要深度定制主题和信号的参赛者。
> - **路径C** （Competition_Full_Workflow_Demo）： **最精简的端到端路径** ，不需要定义主题、不需要滚动信号，直接日度抓取评分上传。 **新手推荐先用这条路径跑通完整流程！**

## 3.3 外部依赖库说明

库名
用途
你需要了解的

 `requests` 
HTTP请求库
所有API调用的底层实现

 `pandas` 
数据处理框架
DataFrame是贯穿全项目的核心数据结构

 `numpy` 
数值计算
数组操作、数学运算

 `scipy` 
科学计算
统计分析（信号处理中可能用到）

 `plotly` 
交互式可视化
生成漂亮的图表（网络图、仪表盘等）

 `matplotlib` 
静态可视化
折线图、柱状图等

 `python-dotenv` 
环境变量管理
从  `.env`  文件读取凭据

 `bigdata-research-tools` 
BigData高层封装
LLM引擎、标注器基类、搜索函数

 `bigdata-client` 
BigData底层API
查询组件（Entity、Keyword等）

 `openai` 
OpenAI API客户端
调用GPT模型进行标注

 `graphviz` 
图形可视化
思维导图的图形渲染

 `json-repair` 
JSON修复
修复LLM返回的不规范JSON

 `pyarrow` 
Parquet格式
用于MATRIX数据打包和上传到BRAIN（Workflow_multi_theme_sentiment）

# 第四章：四大API详解

所有API都通过同一个认证机制访问。理解这四个API是使用项目的基础。

## 4.1 认证机制——BrainSession

**文件** ：每个模块的  `session.py`

**它是什么** ： `BrainSession`  是一个自定义的 HTTP 会话类，继承自 Python 的  `requests.Session` 。它帮你处理登录认证。

**工作原理** ：

```
from session import BrainSession

session = BrainSession(
    email="你的邮箱",
    password="你的密码",
    api_base_url="[链接已屏蔽]
)
# 之后所有API调用都通过 session 发送
# session 会自动处理登录token

```

**底层流程** ：

1. 发送用户名+密码到  `/authentication`  端点
2. 获取 JWT token
3. 之后每次请求自动在Header中附带token
4. Token过期会自动重新认证

> **注意** ：项目中有两种 BrainSession：
> - **标准版** （大部分模块）：简单 HTTP Basic Auth
> - **增强版** （Workflow_multi_theme_sentiment）：支持  **Persona 2FA** （生物识别认证），有token过期追踪机制

## 4.2 Search API——语义搜索

**对应文件夹** ： `Search_API/` 
 **教程Notebook** ： `Search_API_Tutorial.ipynb`

### 做什么的？

语义搜索是整个项目的 **数据来源核心** 。它不是简单的关键词匹配，而是理解你查询的 **含义** ，返回语义相关的新闻文档片段（chunk）。

### 请求结构

```
payload = {
    "query": {
        "text": "artificial intelligence chip shortage",  # 搜索语义
        "filters": {
            "timestamp": {
                "start": "2021-01-01T00:00:00Z",
                "end": "2022-12-31T23:59:59Z"
            },
            "entity": {
                "any_of": ["00067A", "003W2R"],  # 实体ID过滤
                "search_in": "BODY"
            }
        },
        "max_chunks": 100,          # 最大返回chunk数
        "reranker": True,           # 是否使用重排序器
        "relevance_threshold": 0.5, # 相关性阈值
        "freshness_boost": 0,       # 新鲜度加权（比赛要求设为0）
    }
}
response = session.post("/bigdata/v1/search", json=payload)

```

### 返回数据结构

```
{
    "results": {
        "documents": [
            {
                "id": "doc_123",
                "headline": "Intel Reports Chip Shortage...",
                "timestamp": "2021-06-15T10:30:00Z",
                "source": {"id": "src_1", "name": "Reuters", "rank": 1},
                "url": "[链接已屏蔽]
                "chunks": [
                    {
                        "cnum": 0,          # chunk编号
                        "text": "Intel reported severe chip shortages...",
                        "relevance": 0.85,  # 语义相关性分数（0-1）
                        "sentiment": -0.6,  # 情感分数（-1到0之间）
                        "detections": [     # 检测到的实体
                            {"id": "001A3F", "type": "entity", "start": 0, "end": 5}
                        ]
                    }
                ]
            }
        ]
    }
}

```

### 关键参数说明

参数
说明
建议值

 `max_chunks` 
单次请求返回的最大chunk数
100-1000

 `reranker` 
二次排序，提高相关性但增加延迟
True（质量优先）或 False（速度优先）

 `relevance_threshold` 
过滤掉低于此阈值的结果
0.3-0.7

 `freshness_boost` 
偏向新文档的程度
 **比赛要求设为 0** 

 `source_boost` 
偏向高排名来源
根据需要调整

### 关键辅助函数

**文件** ： `Search_API/api_helpers.py`

函数
用途

 `semantic_search(session, query, filters, ...)` 
执行单次语义搜索

 `search_with_reranker(session, query, ...)` 
带重排序器的搜索

 `plot_relevance_distribution(results)` 
绘制相关性分布图

 `compare_with_without_reranker(...)` 
对比开关reranker的效果

## 4.3 Volume API——聚合计数

**对应文件夹** ： `Volume_API/` 
 **教程Notebook** ： `Volume_API_Tutorial.ipynb`

### 做什么的？

Volume API 返回的是 **计数** 而不是实际文档。它告诉你"对于这个查询，每天有多少条相关新闻"。

### 为什么有用？

- **评估覆盖范围** ：在做正式搜索前，先看看某个主题有多少数据
- **情感趋势** ：按天统计正面/负面新闻数量
- **决策依据** ：数据太少的主题或时间段，信号不可靠

### 请求示例

```
payload = {
    "query": {
        "text": "AI chip shortage",
        "filters": {
            "timestamp": {"start": "2021-01-01T00:00:00Z", "end": "2022-12-31T23:59:59Z"}
        },
        "granularity": "day"  # 按天统计
    }
}
response = session.post("/bigdata/v1/search/volume", json=payload)

```

### 返回数据

```
{
    "results": [
        {"date": "2021-01-15", "document_count": 42, "chunk_count": 156},
        {"date": "2021-01-16", "document_count": 38, "chunk_count": 132},
        ...
    ]
}

```

## 4.4 CoMentions API——共现发现

**对应文件夹** ： `CoMentions_API/` 
 **教程Notebook** ： `CoMentions_API_Tutorial.ipynb`

### 做什么的？

发现哪些实体（公司、人物、地点等）经常和你的搜索主题 **一起被提到** 。

### 为什么有用？

- **发现相关公司** ：搜"芯片短缺"，发现 Intel、TSMC、NVIDIA 被频繁提及
- **构建主题篮子** ：找出一组受同一主题影响的公司
- **网络分析** ：理解实体之间的关联关系

### 请求示例

```
payload = {
    "query": {
        "text": "semiconductor shortage",
        "filters": {
            "timestamp": {"start": "...", "end": "..."},
            "entity": {
                "any_of": ["公司ID列表"],  # 在这些公司中查找
                "search_in": "BODY"
            }
        },
        "limit": 1000
    }
}
response = session.post("/bigdata/v1/search/co-mentions/entities", json=payload)

```

### 在项目中的实际用途

Smart Batching 系统用 CoMentions API 来 **预估每个公司的新闻量** （chunk数），从而优化搜索策略。这是整个分批系统的第一步。

## 4.5 Knowledge Graph API——知识图谱

**对应文件夹** ： `Knowledge_Graph_API/` 
 **教程Notebook** ： `Knowledge_Graph_API_Tutorial.ipynb`

### 做什么的？

实体名称和ID之间的 **双向解析** 。

### 核心操作

操作
说明
例子

名称 → ID
根据公司名找到唯一ID
"Apple" → "00F26A"

ID → 名称
根据ID查公司名和元数据
"00F26A" → "Apple Inc."

来源查询
查找新闻来源信息
查看某来源的排名和类别

### 为什么重要？

所有API的实体过滤都用 **ID** 而非名称。你必须先通过知识图谱把公司名转成ID，才能精确搜索。

```
# 查找Apple公司的ID
response = session.get("/bigdata/v1/knowledge-graph/entities", params={"name": "Apple"})
# 返回: [{"id": "00F26A", "name": "Apple Inc.", "type": "company", ...}]

```

# 第五章：Smart Batching——大规模高效搜索

## 5.1 为什么需要批量搜索

**问题** ：你要搜索的实体宇宙有3000+家公司，如果逐一搜索：

- 3000家 × 每家1次请求 = 3000次API调用
- API限速100次/分钟 → 需要30分钟
- 如果时间跨度大，每家公司需要多次请求 → 更久

**Smart Batching 的解决方案** ：

- 把公司按新闻量分组，打包成"basket"
- 每个basket一次请求搜索多家公司
- 自动切分时间窗口，确保每次请求不超过1000 chunks
- 结果： **减少 67-99% 的API调用**

## 5.2 SmartBatchingPlanner 工作原理

**文件** ： `Workflow_example/src/smart_batching.py`  中的  `SmartBatchingPlanner`  类

### 两阶段流程

**阶段1：量发现** （Phase 1）

```
输入：公司列表 + 搜索主题 + 时间范围
   ↓
调用 CoMentions API 获取每家公司的chunk数量
   ↓
输出：{公司ID: chunk数量} 的字典

```

**阶段2：分批规划** （Phase 2）

```
输入：每家公司的chunk数量
   ↓
按量分桶：high(500+), medium(100-500), low(1-100), very_low(0)
   ↓
创建basket：确保每个basket总chunk ≤ 1000，实体数 ≤ 500
   ↓
自适应时间切分：高量公司用更细粒度（月/周）
   ↓
输出：搜索计划（哪些公司在什么时间段搜索）

```

### 关键配置（smart_batching_config.py）

```
MAX_ENTITIES_IN_ANY_OF = 500   # 每次请求最多500个实体
MAX_CHUNKS_PER_BASKET = 1000   # 每个basket最多1000个chunk
START_DATE = "2021-01-01"       # 默认起始日期
END_DATE = "2022-12-31"         # 默认结束日期

```

## 5.3 搜索执行与限速

**文件** ： `Workflow_example/src/search_function.py`

### SlidingWindowRateLimiter

搜索执行器内置了一个滑动窗口限速器，确保不超过API速率限制：

```
限速规则：
- 每分钟最多 100 个请求
- 连续请求间至少间隔 5 秒（防突发）
- 线程安全（支持并行搜索）

```

### 两种搜索模式

模式
函数
说明

Smart搜索
 `execute_search(plan, chunk_percentage)` 
按计划执行，按比例采样chunk

全网格搜索
 `execute_full_grid_search(...)` 
简单遍历所有basket，不做比例采样

**chunk_percentage**  参数：控制每个basket实际请求的chunk比例。设为0.5表示只取50%的chunk（加快速度，牺牲覆盖度）。

## 5.4 关键函数一览

函数
文件
用途

 `SmartBatchingPlanner.plan_all_periods()` 
smart_batching.py
生成完整搜索计划

 `SmartBatchingPlanner.load_universe()` 
smart_batching.py
从CSV加载实体列表

 `SmartBatchingPlanner.get_comention_volumes()` 
smart_batching.py
三遍模式查询公司chunk量

 `SmartBatchingPlanner.get_comention_volumes_iterative()` 
smart_batching.py
迭代模式查询（更高效）

 `SmartBatchingPlanner.create_baskets()` 
smart_batching.py
创建公司分组basket

 `SmartBatchingPlanner.export_to_csvs()` 
smart_batching.py
导出计划到CSV

 `execute_search()` 
search_function.py
执行Smart搜索

 `execute_full_grid_search()` 
search_function.py
执行全网格搜索

 `deduplicate_documents()` 
search_function.py
合并重复文档

 `convert_to_dataframe()` 
output_converter.py
原始结果转DataFrame

# 第六章：Workflow_example——LLM辅助端到端工作流

这是LLM辅助的端到端工作流模块，展示了从主题到信号的完整流程。对应  `Workflow_example/Workflow_example.ipynb` 。

## 6.1 Step 1：主题思维导图生成

**文件** ： `src/mindmap/mindmap.py` ,  `src/mindmap/mindmap_generator.py`

### 做什么？

把一个大主题（如"AI芯片短缺"）用LLM自动拆分成若干子主题，形成树形结构。

### 为什么要拆分？

一个大主题直接搜索，可能覆盖不全。拆成子主题后，可以：

- 提高搜索的 **召回率** （recall）：每个子主题捕获不同角度的新闻
- 更精确的 **标注** ：子主题更具体，LLM判断更准确

### 示例

```
AI芯片短缺                          ← 根节点（主题）
├── 供应链中断风险                    ← 子主题
│   ├── 晶圆制造瓶颈                 ← 叶子节点（最终搜索目标）
│   ├── 物流运输延迟
│   └── 原材料供应紧张
├── 企业成本风险
│   ├── 芯片采购成本上升
│   ├── 产品延迟发布
│   └── 研发替代方案投入
└── 市场竞争风险
    ├── 客户转向竞争对手
    └── 市场份额变化

```

### 核心代码

```
from src.mindmap.mindmap import generate_theme_tree

# 一次性生成
tree = generate_theme_tree(
    main_theme="AI chip shortage",
    focus="impact on semiconductor companies",
    llm_model_config="openai::gpt-4o-mini"
)

# 查看结果
tree.print()  # 打印树形结构
tree.get_terminal_labels()  # 获取所有叶子节点标签
tree.get_terminal_label_summaries()  # 获取叶子节点的标签+摘要
tree.save_json("my_mindmap.json")  # 保存为JSON

```

### MindMap 类核心方法

方法
用途

 `MindMap.from_dict(dict)` 
从字典创建MindMap

 `.print()` 
打印树形结构

 `.visualize(engine="graphviz")` 
生成可视化图（支持graphviz/plotly/matplotlib）

 `.get_terminal_labels()` 
获取所有叶子节点的标签列表

 `.get_terminal_label_summaries()` 
获取叶子节点{标签: 摘要}字典

 `.get_label_to_parent_mapping()` 
获取叶子→父节点的映射

 `.to_dataframe()` 
转为DataFrame

 `.to_json()` 
转为JSON字符串

 `.save_json(filepath)` 
保存为JSON文件

### MindMapGenerator 高级模式

`MindMapGenerator`  类提供了三种生成模式：

模式
方法
说明

一次性
 `generate_oneshot()` 
LLM直接生成，最快

精炼
 `generate_refined()` 
LLM生成 → 搜索验证 → 调整优化，质量更高

动态
 `generate_dynamic()` 
按月/季度分段生成，适应随时间变化的主题

## 6.2 Step 2：搜索规划与执行

### 规划

```
from src.smart_batching import SmartBatchingPlanner

planner = SmartBatchingPlanner(session=session)

# 生成搜索计划
plan = planner.plan_all_periods(
    topic="AI chip shortage",
    start_date="2021-01-01",
    end_date="2022-12-31",
    volume_query_mode="iterative",  # 推荐迭代模式
)

# 查看计划报告
print(planner.generate_report(plan))

```

### 执行

```
from src.search_function import execute_search

# 执行搜索（chunk_percentage控制采样比例）
results = execute_search(
    session=session,
    plan=plan,
    topic="AI chip shortage",
    chunk_percentage=1.0,  # 1.0 = 100%完整搜索
)

```

### 结果转DataFrame

```
from src.output_converter import convert_to_dataframe

df_chunks = convert_to_dataframe(results)
# 每行是一个chunk，包含：
# date, doc_id, headline, chunk_text, chunk_relevance,
# chunk_sentiment, entity_ids, detections, ...

```

## 6.3 Step 3：实体提取与过滤

**文件** ： `src/helper.py`

### 为什么要过滤？

搜索返回的chunk中可能包含各种实体（公司、人物、地点等）。我们只关心"实体宇宙"中的公司。

### 流程

```
from src.helper import load_universe_entities, explode_to_dataframe

# 加载实体宇宙
entity_ids, id_to_name = load_universe_entities("id_name_mapping_us_top_3000.csv")
# entity_ids: {"00067A", "003W2R", ...}（4732个ID的集合）
# id_to_name: {"00067A": "Humana Inc.", ...}

# 按实体展开（一个chunk可能包含多个公司 → 拆成多行）
df_exploded = explode_to_dataframe(
    df_chunks,
    universe_csv="id_name_mapping_us_top_3000.csv"
)
# 现在每行是一个 (chunk, 实体) 组合
# 新增列：entity_id, entity_name

```

### 关键概念：展开（Explode）

一条新闻中可能提到3家公司。展开操作会把这条新闻变成3行，每行对应一家公司：

```
原始chunk：
  "Apple and Microsoft are competing for AI chip supply from NVIDIA"
  detections: [Apple, Microsoft, NVIDIA]

展开后：
  行1: entity=Apple,     chunk_text="Apple and Microsoft..."
  行2: entity=Microsoft, chunk_text="Apple and Microsoft..."
  行3: entity=NVIDIA,    chunk_text="Apple and Microsoft..."

```

## 6.4 Step 4：公司名称掩码

**文件** ： `src/helper.py`  中的  `mask_companies_in_df()`

### 为什么要掩码？

发送文本给LLM标注时，如果文本中出现"Apple"，LLM可能因为自己对Apple的"印象"而产生偏见。掩码就是把公司名替换成中性占位符：

```
原文：
  "Apple reported strong earnings while Microsoft faced regulatory challenges"

掩码后（假设目标公司是Apple）：
  "Target_Company reported strong earnings while Other_Company_1 faced regulatory challenges"

```

### 代码

```
from src.helper import mask_companies_in_df

df_masked = mask_companies_in_df(
    df_exploded,
    text_column="chunk_text",
    detection_column="companies_detection",
    target_entity_id_column="entity_id"
)
# 新增列：masked_text, other_entities_map

```

## 6.5 Step 5：LLM标注与验证

**文件** ： `src/labeler/screener_labeler.py`

### 做什么？

用LLM（如GPT-4o-mini）阅读每段掩码后的文本，判断：

1. **是否与主题相关** （is_theme_related: True/False）
2. **影响方向** （impact: Positive/Negative/Neutral/Unclear）

### 两种标注模式

模式
方法
说明

基础标注
 `get_labels()` 
一步判断影响方向

验证标注
 `get_validation_labels()` 
两步：先判相关性，再判影响

### 代码示例

```
from src.labeler.screener_labeler import ScreenerLabeler

labeler = ScreenerLabeler(
    llm_config="openai::gpt-4o-mini",
    theme="AI chip shortage",
    sub_themes=tree.get_terminal_label_summaries()
)

# 两步验证标注
df_labeled = labeler.get_validation_labels(df_masked)
# 新增列：is_theme_related, impact, motivation

```

### ThemeValidationResult 模型

```
class ThemeValidationResult(BaseModel):
    is_theme_related: bool    # 是否与主题相关
    impact: ImpactType        # "Positive" | "Negative" | "Neutral" | "Unclear"
    motivation: str           # LLM的判断理由

```

### 提示词模板

所有发送给LLM的提示词模板在  `src/prompts/labeler.py`  中定义。主要模板：

模板
用途

 `screener_system_prompt_template` 
基础主题标注

 `theme_validation_prompt_template` 
两步验证：相关性+影响

 `risk_system_prompt_template` 
风险场景评估

## 6.6 Step 6：滚动信号构建

**文件** ： `src/helper.py`  中的  `build_rolling_impact_signal()`

### 核心逻辑

```
影响评分映射：
  Positive  → +1
  Negative  → -1
  Neutral   → 0
  Unclear   → 0

日度聚合：
  每家公司每天的 daily_score = 当天所有chunk评分的平均值

滚动均值：
  signal_7d  = daily_score 的过去7天滚动平均
  signal_30d = daily_score 的过去30天滚动平均

```

### 代码

```
from src.helper import build_rolling_impact_signal

df_signal = build_rolling_impact_signal(
    df_labeled,
    entity_col="entity_name",
    date_col="date",
    impact_col="impact",
    is_theme_related_col="is_theme_related",
    window_7d=7,
    window_30d=30,
    rolling_agg="mean"  # 使用均值（还可以用 "sum"）
)

```

### 可视化

```
from src.helper import plot_top_entities_rolling_signal

# 画出新闻量最多的5家公司的信号趋势
plot_top_entities_rolling_signal(
    df_signal,
    signal_col="signal_30d",  # 或 "signal_7d"
    top_n=5
)

```

## 6.7 最终输出解读

`df_rolling_signal.csv`  的每一行代表 **一家公司在一天的信号** ：

列名
含义
取值范围

 `entity_name` 
公司名称
如 "Apple Inc."

 `date` 
日期
2021-01-01 ~ 2022-12-31

 `daily_score` 
当天影响均值
-1 到 +1

 `n_positive` 
当天正面新闻数
0, 1, 2, ...

 `n_negative` 
当天负面新闻数
0, 1, 2, ...

 `n_neutral` 
当天中性新闻数
0, 1, 2, ...

 `n_unclear` 
当天不明确新闻数
0, 1, 2, ...

 `volume` 
当天总新闻数
0, 1, 2, ...

 `signal_7d` 
7天滚动信号
-1 到 +1

 `signal_30d` 
30天滚动信号
-1 到 +1

 `volume_7d` 
7天滚动新闻量
0, 1, 2, ...

 `volume_30d` 
30天滚动新闻量
0, 1, 2, ...

**如何解读** ：

- `signal_30d = 0.8` ：过去30天该公司在此主题下以正面新闻为主（做多信号）
- `signal_30d = -0.6` ：过去30天以负面新闻为主（做空信号或风险预警）
- `signal_30d ≈ 0` ：中性或数据不足

# 第六点五章：Workflow_multi_theme_sentiment——多主题情感+BRAIN上传

这是项目新增的 **最完整模块** ，展示了从主题定义到BRAIN平台上传的全流程。对应  `Workflow_multi_theme_sentiment/Workflow_multi_theme_sentiment.ipynb` 。

> **★ 新手推荐先看这个模块！**  因为它不需要LLM（省掉OpenAI费用），而且包含了完整的BRAIN上传代码。

## 6.5.1 这个模块有什么不同？

特性
Workflow_example
Workflow_multi_theme_sentiment

需要LLM？
是（OpenAI）
 **否** 

如何判断情感？
LLM标注
 **API内置sentiment过滤器** 

主题数量
单一主题拆分
 **多个正交主题** 

是否上传BRAIN？
❌ 需自行实现
 **✅ 代码自动完成** 

信号格式
CSV（长格式）
 **MATRIX Parquet（宽格式）** 

实体列表
CSV（含名称）
JSON（纯ID）

核心优势
LLM精度高
无需LLM、完整提交流程

**核心思路** ：用多个 **正交主题** （互相独立的角度），每个主题有明确的 **正/负方向** ，利用API的sentiment过滤器直接获取正面或负面新闻，然后加权合成复合信号。

## 6.5.2 工作流六步走

```
步骤1: 实体宇宙 + 主题定义
  ↓ 加载3435个实体ID，定义正面/负面主题
步骤2: 批量搜索执行
  ↓ 500实体/批 × 月份 × 主题，带API层面sentiment过滤
步骤3: 实体归因 + 情感评分
  ↓ 把搜索结果归因到具体公司，计算加权情感分
步骤4: 滚动信号构建
  ↓ 7天/30天滚动均值 → 方向加权合成 → 截面去均值
步骤5: 数据质量QA验证
  ↓ 6项自动检查确保数据没问题
步骤6: 上传到BRAIN
  ↓ 打包成Parquet格式，自动上传MATRIX数据字段

```

## 6.5.3 主题定义——正交主题设计

**什么是正交主题？**  就是从不同的、互相独立的角度来捕捉新闻情感。比如：

- "财报正面新闻"（方向：+1）——捕捉盈利增长
- "供应链负面新闻"（方向：-1）——捕捉供应链风险

```
THEMES = {
    "earnings_positive": {
        "text": "the company reports strong earnings growth revenue beat expectations",
        "description": "Clearly positive earnings news only",
        "sentiment_filter": {"min": 0.3, "max": 1.0},  # 只要正面情感的新闻
        "direction": 1.0,  # 正面方向
    },
    "supply_chain_negative": {
        "text": "supply chain disruption shortage delays logistics bottleneck",
        "description": "Clearly negative supply chain news only",
        "sentiment_filter": {"min": -1.0, "max": -0.3},  # 只要负面情感的新闻
        "direction": -1.0,  # 负面方向
    },
}

```

**关键参数** ：

- `text` : 搜索查询文本（语义搜索用）
- `sentiment_filter` : API层面的情感过滤（ `min` / `max`  范围是 -1 到 1）
- `direction` : 合成复合信号时的方向权重

> **进阶提示** ：示例展示了5个金融主题。你可以进一步扩展到8-10个正交维度，覆盖更多角度（如"并购活动"、"产品创新"等）。主题越多、越正交，复合信号越稳健。

## 6.5.4 实体归因机制

搜索返回的新闻中可能提到多家公司。系统用以下逻辑将新闻归因到具体实体：

归因类型
条件
权重

 **直接归因** 
实体在chunk中被检测到  **且**  在查询的batch中
100%

 **共提及归因** 
实体在chunk中被检测到，在实体宇宙中，但 **不在** 查询batch中
50%

 **丢弃** 
chunk中没有检测到任何实体宇宙中的实体
0%

**评分公式** ：

```
文档加权情感 = Σ(相关性 × 情感) / Σ(相关性)
平均相关性 = mean(各chunk相关性)

```

## 6.5.5 复合信号构建

### 步骤1：每主题滚动均值

把每个主题的日度评分做 7天 和 30天 的 **回溯滚动均值** （只看过去，不看未来，确保时间点一致）。

### 步骤2：方向加权合成

```
composite = Σ(主题矩阵 × 方向权重 × 0.5)

```

比如：earnings_positive 的矩阵 × (+1) × 0.5 + supply_chain_negative 的矩阵 × (-1) × 0.5

### 步骤3：截面去均值

每天对所有有信号的公司做 **去均值** 处理（减去当日均值）。这确保信号是 **相对的** ——相对于同日其他公司的表现。

```
# 每天的截面去均值
for date in all_dates:
    nonzero = composite.loc[date] != 0
    if nonzero.sum() > 1:
        composite.loc[date, nonzero] -= composite.loc[date, nonzero].mean()

```

## 6.5.6 数据质量验证

Notebook内置了6项自动QA检查：

检查项
内容
通过条件

QA-1 日期范围
矩阵覆盖完整日期
起止日期正确

QA-2 实体覆盖
有信号的实体占比
>5% 通过, >1% 警告

QA-3 NaN/Inf
数据中无异常值
无NaN且无Inf

QA-4 值域范围
信号值合理
[-1.5, +1.5] 范围内

QA-5 复合平衡
正负信号比例
20%-80% 且均值接近0

QA-6 平滑度
30天滚动比原始更平滑
30d标准差 ≤ raw标准差

## 6.5.7 上传到BRAIN

这是整个比赛最关键的一步——将信号上传到WorldQuant BRAIN进行alpha模拟！

### 上传数据格式

属性
值

类型
 `MATRIX` 

格式
Parquet + GZIP 压缩

矩阵形状
日期行 × 实体ID列

值
信号值 × 100（放大100倍）

字段ID
 `{USER_ID}_{主题缩写}_{窗口}`

### 上传代码核心

```
# 准备上传
field_meta = json.dumps({
    'id': field_id,          # 如 "12345_earnings_pos_7d"
    'type': 'MATRIX',
    'source': 'BigData',
    'data': [{'region': 'USA', 'delay': 1}]
})

# 发送到BRAIN
response = session.post(
    "/users/self/data-fields",      # 上传端点
    data={'field': field_meta},     # 元数据
    files={'data': parquet_buffer}, # Parquet文件
    timeout=120
)

```

### 上传字段示例

字段ID
说明

 `{USER_ID}_earnings_pos_7d` 
7天滚动正面财报情感

 `{USER_ID}_earnings_pos_30d` 
30天滚动正面财报情感

 `{USER_ID}_supply_neg_7d` 
7天滚动负面供应链情感

 `{USER_ID}_supply_neg_30d` 
30天滚动负面供应链情感

> **成功上传后** ，你就可以在BRAIN平台上使用这些数据字段来构建alpha表达式并运行Simulation了！

# 第六点七五章：Competition_Full_Workflow_Demo——比赛完整工作流演示

这是项目新增的 **最精简模块** ，展示了从实体ID到BRAIN平台上传的最短路径。对应  `Competition_Full_Workflow_Demo/DataCreationCompetition_workflow.ipynb` 。

> **★ 绝对新手推荐先看这个模块！**  不需要LLM，不需要BRT库，不需要定义主题，代码最少，流程最直接。

## 6.75.1 这个模块的定位

特性
Workflow_example
Workflow_multi_theme_sentiment
Competition_Full_Workflow_Demo

需要LLM？
是
否
 **否** 

需要BRT库？
是
否
 **否** 

需要定义主题？
是
是
 **否** 

上传类型
需自行实现
MATRIX
 **MATRIX + VECTOR** 

代码复杂度
高
中
 **低（最简单）** 

API端点
生产环境
生产环境
 **开发环境** 

核心优势
LLM精度
多主题复合信号
 **最短路径跑通全流程**

**核心思路** ：每天批量获取新闻文档 → 用每个chunk的  `相关性 × 情感`  计算评分 → 汇总为每个实体每天的分数 → 同时上传MATRIX（均值）和VECTOR（列表）到BRAIN。

## 6.75.2 工作流五步走

```
步骤1: 实体宇宙加载
  ↓ 从 universe.json 加载 ~3000 个实体ID
步骤2: 日度文档获取
  ↓ 每天 → 分批500个ID → 调Search API → 带指数退避重试
步骤3: 情感评分计算
  ↓ 每篇文章: avg(相关性 × 情感) × 100 → 归因到文章中提到的实体
步骤4: DataFrame构建
  ↓ 行=日期, 列=实体ID, 值=评分列表 → 保存Parquet
步骤5: 上传到BRAIN
  ↓ MATRIX（均值float）+ VECTOR（评分列表）同时上传

```

### 关键代码结构

```
# 主执行函数
all_entity_data = run_workflow(
    start_date_input="2021-01-01",
    end_date_input="2021-01-07",
    universe_ids=top3000      # ~3000个实体ID
)
# 返回: {entity_id: {date_str: [scores]}}

# 构建DataFrame
df = create_dataframe(all_entity_data, "2021-01-01", "2021-01-07", top3000)
# shape: (7天, ~3000列)

# 上传MATRIX（每个单元格一个float）
df_matrix = df.applymap(lambda x: mean(x) if x else 0.0)
create_data_field(f"{USER_ID}_sentiment_matrix", df_matrix, 'USA', 1, 'MATRIX', 'BigData')

# 上传VECTOR（每个单元格一个float列表）
df_vector = df.applymap(lambda x: list(x) if x else [])
create_data_field(f"{USER_ID}_sentiment_vector", df_vector, 'USA', 1, 'VECTOR', 'BigData')

```

## 6.75.3 评分机制

这个模块的评分逻辑非常直接：

### 文档级评分

```
对每篇文章：
  1. 遍历所有chunk
  2. chunk_score = relevance × sentiment
     - relevance: 语义相关性 (0~1)
     - sentiment: 情感分数 (-1~+1)
  3. article_score = mean(所有chunk_score) × 100

最终：
  - 正分 = 相关且正面的文章（如：高相关性的利好新闻）
  - 负分 = 相关且负面的文章
  - 接近零 = 不太相关或情感中性

```

### 实体归因

每篇文章的分数会被分配给文章中提到的 **所有在实体宇宙中的实体** ：

```
for chunk in article['chunks']:
    for detection in chunk['detections']:
        if detection['type'] == 'entity' and detection['id'] in universe_set:
            # 这个实体获得这篇文章的分数
            entity_scores[detection['id']].append(article_score)

```

> **注意** ：与 Workflow_multi_theme_sentiment 的区别——这里没有"直接归因 vs 共提及归因"的区分，所有在文章中检测到的实体都获得相同权重的分数。

## 6.75.4 MATRIX vs VECTOR 上传

这个模块同时演示了两种BRAIN数据字段类型：

类型
每个单元格的值
用途

 **MATRIX** 
单个float（多篇文章取均值）
简单的日度情感均值

 **VECTOR** 
float列表（保留所有文章分数）
保留完整信息，可在BRAIN端做更复杂处理

```
# MATRIX示例（某实体某天）：
# 3篇文章评分: [25.5, -10.2, 8.0]
# MATRIX值 = mean([25.5, -10.2, 8.0]) = 7.77

# VECTOR示例（同样的实体同天）：
# VECTOR值 = [25.5, -10.2, 8.0]  ← 保留原始列表

```

### 上传格式

属性
MATRIX
VECTOR

类型名
 `MATRIX` 
 `VECTOR` 

格式
Parquet + GZIP
Parquet + GZIP

矩阵形状
日期行 × 实体ID列
日期行 × 实体ID列

单元格值
float
list[float]

字段ID
 `{USER_ID}_sentiment_scores_matrix` 
 `{USER_ID}_sentiment_scores_vector`

## 6.75.5 三套工作流对比

维度
Workflow_example
Workflow_multi_theme_sentiment
Competition_Full_Workflow_Demo

 **复杂度** 
★★★★★
★★★☆☆
★☆☆☆☆

 **信号质量** 
最高（LLM精度）
高（多主题正交）
基础（原始评分）

 **成本** 
需要LLM API费用
免费
免费

 **完整度** 
缺BRAIN上传
完整
完整

 **适用场景** 
深度研究
正式比赛
快速入门/原型验证

> **建议路径** ：先用 Competition_Full_Workflow_Demo 跑通全流程 → 再用 Workflow_multi_theme_sentiment 提升信号质量 → 最后用 Workflow_example 追求极致精度。

# 第七章：经济学与金融逻辑

## 7.1 新闻情感与股价的关系

**学术基础** ：行为金融学研究表明，新闻情感可以预测短期股价走势。原因包括：

1. **信息传播延迟** ：并非所有投资者同时看到并消化新闻
2. **注意力有限** ：投资者不可能关注所有公司的所有新闻
3. **情感反应** ：负面新闻往往引发过度反应，正面新闻可能反应不足

**本项目的逻辑链** ：

```
新闻发布 → NLP提取情感 → 构建信号 → 假设信号能预测未来价格变动

```

**注意** ：这只是一个假设。信号好不好用，要靠 **回测验证** 。

## 7.2 主题选择的策略思考

主题选择是整个管线中 **最重要的创意环节** 。好的主题应该：

特征
好的主题
差的主题

影响范围
影响多家公司，但不是所有公司
要么只影响1-2家，要么影响所有公司

可量化
有明确的正面/负面影响
模糊不清，难以判断正负

时效性
在目标时间段有持续新闻
只是一两天的新闻

差异化
不同公司受影响程度不同
所有公司影响一样（无alpha）

独特性
别人不太可能想到
太通用（如"经济衰退"）

**主题示例** ：

- ✅ "芯片短缺对汽车行业的影响"——具体、可量化、差异化
- ✅ "新冠疫苗研发进展对医药公司的影响"——时效性强
- ❌ "全球经济增长"——太宽泛
- ❌ "某CEO言论"——太窄、一次性

## 7.3 信号质量评估

在把信号提交到Brain平台之前，你可以自己初步评估：

### 覆盖度

```
有信号的公司数 / 实体宇宙总数

```

太低说明主题覆盖不够，太高说明可能不够精确。

### 信号分布

好的信号应该有合理的正负分布，不应该全是正面或全是负面。

### 时间稳定性

`signal_30d`  不应该剧烈跳动（除非有重大事件）。如果信号噪声太大，考虑加大滚动窗口或增加过滤条件。

### 新闻量支撑

`volume_30d`  很低的公司信号不可靠。可以设阈值过滤掉低量公司。

# 第八章：比赛实战指南

## 8.1 比赛流程

### 路径A：Workflow_example（LLM辅助，需自行上传）

```
1. 注册 WorldQuant Brain 账号
2. 获取 API 凭据（BRAIN_EMAIL, BRAIN_PASSWORD）+ OpenAI API Key
3. 选择研究主题
4. 运行 Workflow_example 管线生成信号CSV
5. 将信号CSV转换为 Brain 平台的 MATRIX 格式（需自行实现）
6. 上传到 Brain 平台
7. 运行 Simulation
8. 查看评分和排名

```

### 路径B：Workflow_multi_theme_sentiment（完整流程，多主题复合信号）

```
1. 注册 WorldQuant Brain 账号
2. 获取 API 凭据（BRAIN_EMAIL, BRAIN_PASSWORD）
3. 定义多个正交金融主题
4. 运行 Workflow_multi_theme_sentiment notebook
5. 代码自动搜索、评分、构建MATRIX、上传到BRAIN ← 全自动！
6. 在BRAIN平台构建alpha表达式
7. 运行 Simulation
8. 查看评分和排名

```

### 路径C：Competition_Full_Workflow_Demo（★新手首选，最简单★）

```
1. 注册 WorldQuant Brain 账号
2. 获取 API 凭据（BRAIN_EMAIL, BRAIN_PASSWORD）
3. 运行 DataCreationCompetition_workflow.ipynb
4. 代码自动日度抓取、评分、上传MATRIX+VECTOR到BRAIN ← 全自动！
5. 在BRAIN平台构建alpha表达式
6. 运行 Simulation
7. 查看评分和排名

```

> **绝对新手推荐路径C** ：最少的代码、最少的配置、最短的路径跑通全流程。跑通之后再切换到路径B提升信号质量。

## 8.2 学习路径建议

### 第1周：基础

1. 配好环境，跑通所有  `.env`  配置
2. 按顺序运行4个API Tutorial Notebook：
   - `Search_API_Tutorial.ipynb` （最重要，理解chunk概念）
   - `Volume_API_Tutorial.ipynb`
   - `Knowledge_Graph_API_Tutorial.ipynb`
   - `CoMentions_API_Tutorial.ipynb`
3. 每个Notebook的每个cell都运行一遍，理解输入输出

### 第2周：进阶

1. **★ 运行  `Competition_Full_Workflow_Demo/DataCreationCompetition_workflow.ipynb`**
2. 理解最简单的"抓取→评分→上传"全流程（新手必须先跑通这个！）
3. 运行  `Smart_Batching/test_smart_batching.ipynb`
4. 理解分批原理，尝试修改参数
5. 运行  `Workflow_multi_theme_sentiment/Workflow_multi_theme_sentiment.ipynb`
6. 理解多主题 + BRAIN上传的完整流程
7. 运行  `Workflow_example/Workflow_example.ipynb` （需要OpenAI API Key）
8. 对比三种工作流的不同

### 第3周：实战

1. 设计自己的正交主题组合（参考 THEMES 字典格式）
2. 修改 Workflow_multi_theme_sentiment 的主题、时间范围、批次大小
3. 运行完整管线并上传到BRAIN
4. 在BRAIN平台构建alpha表达式，运行Simulation
5. 分析QA检查结果和Simulation评分

### 第4周：迭代优化

1. 增加更多正交主题（扩展到5-10个）
2. 调整sentiment_filter的阈值范围
3. 尝试 Workflow_example 的LLM标注方案，对比效果
4. 优化滚动窗口参数、归因权重
5. 提交最佳信号，冲刺排名

## 8.3 进阶优化方向

当你跑通基础流程后，以下方向可以帮你在比赛中脱颖而出：

### 信号构建优化

方向
说明

衰减加权
越近的新闻权重越高（指数衰减）

z-score标准化
跨公司横截面标准化，消除量级差异

行业中性化
减去行业平均信号，提取公司特有信号

多主题合成
综合多个主题的信号（等权或优化权重）— Workflow_multi_theme_sentiment 已实现基础版

异常量检测
新闻量突增时加大信号权重（事件驱动）

归因权重优化
调整共提及归因的0.5×折扣系数，可按距离或频率动态调整

截面去均值改进
可尝试按行业分组去均值，而非全市场去均值

### 搜索质量优化

方向
说明

调整 relevance_threshold
提高阈值减少噪声，降低阈值增加覆盖

reranker开关
开=质量高但慢，关=速度快但噪声多

来源过滤
只用高排名来源（source_rank）减少噪声

精炼MindMap
用refined模式生成更好的子主题

### LLM标注优化

方向
说明

改进prompt
让LLM判断更准确（最具性价比的优化）

换模型
试试更强大的模型（如 gpt-4o）

验证模式
使用两步验证（先判相关性再判影响）

置信度过滤
只保留LLM高置信度的判断

# 附录：所有函数速查表

## 认证（session.py）

函数/类
说明

 `BrainSession(email, password, api_base_url)` 
创建标准认证会话（大部分模块）

 `BrainSession(base_url, email, password, refresh_margin)` 
创建增强版认证会话（Workflow_multi_theme_sentiment，支持2FA）

## 思维导图（mindmap/mindmap.py）

函数/方法
说明

 `generate_theme_tree(main_theme, focus, llm_model_config)` 
生成主题思维导图

 `generate_risk_tree(main_theme, focus, llm_model_config)` 
生成风险思维导图

 `MindMap.from_dict(dict)` 
从字典创建

 `MindMap.print()` 
打印树结构

 `MindMap.visualize(engine)` 
可视化（graphviz/plotly/matplotlib）

 `MindMap.get_terminal_labels()` 
获取叶子节点标签

 `MindMap.get_terminal_label_summaries()` 
获取叶子节点{标签:摘要}

 `MindMap.get_label_summaries()` 
获取所有节点{标签:摘要}

 `MindMap.get_label_to_parent_mapping()` 
叶子→父节点映射

 `MindMap.to_dataframe(leaves_only)` 
转DataFrame

 `MindMap.to_json()` 
转JSON字符串

 `MindMap.save_json(filepath)` 
保存JSON文件

## 思维导图生成器（mindmap/mindmap_generator.py）

方法
说明

 `MindMapGenerator.generate_oneshot()` 
一次性生成

 `MindMapGenerator.generate_refined()` 
精炼生成

 `MindMapGenerator.generate_dynamic(intervals)` 
动态时间段生成

 `MindMapGenerator.bootstrap_refined(n)` 
并行生成n棵精炼树

## 分批规划（smart_batching.py）

方法
说明

 `SmartBatchingPlanner.plan_all_periods(topic, ...)` 
生成完整搜索计划

 `SmartBatchingPlanner.load_universe(csv_path)` 
加载实体宇宙

 `SmartBatchingPlanner.get_comention_volumes(companies, topic, ...)` 
三遍模式查询chunk量

 `SmartBatchingPlanner.get_comention_volumes_iterative(...)` 
迭代模式查询

 `SmartBatchingPlanner.create_baskets(company_volumes, max_chunks)` 
创建分组basket

 `SmartBatchingPlanner.split_period(start, end, period_type)` 
按粒度切分时间

 `SmartBatchingPlanner.generate_report(report)` 
生成人类可读报告

 `SmartBatchingPlanner.export_to_csvs(report, ...)` 
导出CSV

## 搜索执行（search_function.py）

函数
说明

 `execute_search(session, plan, topic, chunk_percentage)` 
Smart搜索执行

 `execute_full_grid_search(session, companies, topic, ...)` 
全网格搜索

 `deduplicate_documents(results)` 
文档去重

## 数据处理（helper.py）

函数
说明

 `load_universe_entities(csv_path)` 
加载实体宇宙（返回set和dict）

 `explode_by_entity(results, valid_ids, id_to_name)` 
按实体展开原始结果

 `explode_to_dataframe(data, universe_csv)` 
展开为DataFrame

 `mask_companies_in_df(df, ...)` 
公司名称掩码

 `entity_statistics(df)` 
实体统计（文档数、情感均值等）

 `prepare_sentiment_dataframe(df)` 
准备情感分析DataFrame

 `get_top_entities_by_volume(df, n)` 
获取新闻量Top N实体

 `build_rolling_impact_signal(df, ...)` 
构建滚动影响信号

 `plot_top_entities_rolling_signal(df, ...)` 
绘制Top实体信号趋势图

 `display_sentiment_volume(df, entity)` 
显示单个实体情感+新闻量图

 `display_top_entities_dashboard(df, daily_sentiment, n)` 
显示Top实体仪表盘

## 结果处理（output_converter.py）

函数
说明

 `convert_to_dataframe(raw_results)` 
原始API结果 → 按chunk展开的DataFrame

## 实体处理（processing_results.py）

函数
说明

 `aggregate_results_by_chunk(results)` 
按chunk聚合搜索结果

 `get_unknown_entities_from_df_column(df, known_entities)` 
找出未知实体

 `extract_companies_from_entity_list(entity_ids, session)` 
从KG API提取公司信息

 `process_entities_and_filter_companies(df, session, universe_csv)` 
处理实体并过滤公司

## 标注器（labeler/screener_labeler.py）

方法
说明

 `ScreenerLabeler.get_labels(df)` 
基础主题标注

 `ScreenerLabeler.get_validation_labels(df)` 
两步验证标注

 `ScreenerLabeler.post_process_dataframe(df)` 
后处理格式化

## 思维导图工具（mindmap/mindmap_utils.py）

函数/变量
说明

 `prompts_dict` 
主题/风险树的提示词模板字典

 `format_mindmap_to_dataframe(text)` 
文本格式思维导图转DataFrame

 `save_results_to_file(results, dir, filename)` 
保存结果到JSON

 `load_results_from_file(dir, filename)` 
从JSON加载结果

## 多主题情感管线（Workflow_multi_theme_sentiment notebook内函数）

函数/类
说明

 `RateLimiter(max_requests_per_minute)` 
线程安全限速器（默认30 req/min）

 `api_request(endpoint, payload, max_retries)` 
带重试和限速的API请求

 `monthly_buckets(start, end)` 
生成月度时间桶列表

 `build_rolling_matrices(long_df, windows)` 
构建滚动矩阵（raw/7d/30d）

 `upload_matrix(field_id, matrix_df, scale, ...)` 
上传MATRIX数据字段到BRAIN

## 比赛演示管线（Competition_Full_Workflow_Demo notebook内函数）

函数/类
说明

 `get_daily_documents(target_date_str, company_ids)` 
按日期获取新闻文档，500/批，带指数退避重试

 `calculate_scores_for_day(documents, valid_ids_set)` 
计算当日所有文档的实体评分，返回  `{entity_id: [scores]}` 

 `run_workflow(start_date, end_date, universe_ids)` 
主执行入口：按日迭代→获取→评分→聚合

 `create_dataframe(entity_data, start, end, universe_ids)` 
将嵌套字典转为DataFrame，保存Parquet

 `create_data_field(data_field_id, data_frame, region, delay, type_name, source)` 
上传MATRIX或VECTOR数据字段到BRAIN

 `calc_average(scores)` 
将评分列表取均值（用于MATRIX）

 `parse_keep_as_list(scores)` 
保持评分列表格式（用于VECTOR）

> **最后的话** ：这个项目看起来复杂，但核心逻辑其实很清晰——就是"搜新闻 → 判好坏 → 算分数 → 上传BRAIN"。建议新手先跑通  `Competition_Full_Workflow_Demo` （最简单，5步搞定），再进阶到  `Workflow_multi_theme_sentiment` （多主题正交信号），最后研究  `Workflow_example`  的LLM高精度方案。三条路径递进互补，选最适合你当前阶段的！祝你比赛顺利

**顾问 WX84677 (Rank 69) 的解答与建议**:
这教程太硬核了！从环境搭建到三套工作流对比，从API详解到Smart Batching原理，把DCC比赛全流程扒得明明白白。特别是"新手路径C→进阶B→高精A"的递进设计，还有LLM异步坑、token消耗这些细节提醒，都是踩过坑才能写出来的干货。附录函数速查表更是贴心，直接当文档查。感谢整理，省了我至少一周摸索时间！


---

### 技术对话片段 2 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (LZ63377)**:
大家新年好呀，给大家拜个晚年了🧨🧨

首先声明我不是大佬，很多东西我都是一知半解的，还在逐渐摸索，combine和vf得分也有很大的运气成分。

我是去年11月下旬转为有条件顾问的，至今经历了两次combine刷新和一次vf刷新，变动如下图所示：


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combieq4lpha
> DOwET Dool
> 0 Seleced Alpha
> 0.97
> Combin」
> 3.71
> 090
> 300
> 0.80
> 200
> 0,70
> 100
> 050
> 0.00
> 1.00
> 0.50
> 0.45
> ~1.73
> 202503
> 202509
> 202510
> 202508
> 202509
> 202510
> 302500
> 302510
> 202571
> 202500
> 202510
> 202571
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512


可以看到前后仅一个月，我的combine就从-1.2拉升到了3.18，vf也涨到了0.92，对比过于强烈，完全可以说是从全错到全对的过程。因此我认为自己这个样本还是很具有研究价值的，对目前combine仍处于谷底的顾问应该也会有所启发，那么我11月和12月的提交情况是怎样的呢？又能得出什么结论呢？（省流直接跳到后面粗体看结论，右上角给点个赞吧，多谢了！）

因为平台在今年1月20更新了os期，所有此前提交的因子默认显示的都是os期数据，而我提交时自然不可能预见os表现，所以下面展示的仍然是is时期的数据。此外我提交的大部分都是atom，只有少量混pv。

先看11月份，这个月底我刚成为顾问，共提交了13个因子，数据如下（图有点宽，建议ctrl+放大看）：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 10
> 2.13
> 1.625
> 1.656
> 4.03
> 3.075
> 2.984
> 0.001243
> 0.000637
> 0.000747
> 0.1494
> 0.0736
> 0.0739
> EUR
> 01
> 1.92
> 1.9
> 1.9
> 3.01
> 2.855
> 2.855
> 0.001011
> 0.001002
> 0.001002
> 0.0765
> 0.0626
> 0.0626
> USA
> 01
> 1.58
> 1.58
> 1.58
> 2.71
> 2.71
> 2.71
> 0.000681
> 0.000681
> 0.000681
> 0.0561
> 0.0561
> 0.0561


再看12月份，这个月份共提交了61个因子，数据如下：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 对象数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 3
> 1.35
> 1.17
> 1.18
> 1.66
> 1.46
> 1.4267
> 0.007593
> 0.001492
> 0.003362
> 0.127
> 0.0825
> 0.0901
> EUR
> 18
> 3.08
> 1.26
> 1.4278
> 3.82
> 2.125
> 2.2739
> 0.002114
> 0.001282
> 0.001308
> 0.0834
> 0.0471
> 0.0515
> IND
> 器
> 21
> 3.32
> 1.77
> 1.8457
> 3.08
> 2.26
> 2.3048
> 0.002643
> 0.001136
> 0.001325
> 0.1931
> 0.1373
> 0.1359
> USA
> 19
> 3.07
> 1.59
> 1.7595
> 3.78
> 1.76
> 1.9811
> 0.007382
> 0.001876
> 0.002561
> 0.3445
> 0.11
> 0.1277


因为我最高的combine是总池，所以再补一张11、12月份汇总数据：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 13
> 2.13
> 1.61
> 1.5462
> 4.03
> 295
> 2.6246
> 0.007593
> 0.000731
> 0.00135
> 0.1494
> 0.0799
> 0.0776
> EUR
> 20
> 3.08
> 1.275
> 1.475
> 3.82
> 2.21
> 2.332
> 0.002114
> 0.001257
> 0.001278
> 0.0834
> 00484
> 0.0526
> IND
> 器
> 3.32
> 1.77
> 1.8457
> 3.08
> 2.26
> 2.3048
> 0.002643
> 0.001136
> 0.001325
> 0.1931
> 0.1373
> 0.1359
> USA
> 20
> 3.07
> 1.585
> 1.7505
> 3.78
> 1.805
> 2.0175
> 0.007382
> 0.001698
> 0.002467
> 0.3445
> 0.1068
> 0.1241


这样一来答案是不是显而易见了？接下来开始盘点全错和全对行为。

**全错：**

1. **月底入坑，提交量少，但却刚好够出combine分（这个也确实没啥好办法，总有我这种月底转正的倒霉蛋，好在提交量少很快就能冲回来）**
2. **一上来就做d0（数据少难度高）**
3. **只看fitness和sharpe,忽略了margin（就算os维持is期的表现都是亏的，更别提os可能还要俯冲一波了）**
4. **乱开地区又没点上塔（地区表现直接崩盘）**

**全对：**

1. **稳定提交，平均每日2个因子，不多不少（对于冲gm的顾问可能少了，但都准备冲gm了也不用我多说什么了）**
2. **尽量少做甚至不做d0了**
3. **开始注意各地区最低margin，保证不低于底线**
4. **每个地区都提交了20个以上的因子，稳定了地区表现**

一个反直觉的结论，12月提交的fitness和sharpe相比于11月是有下降的（也可能是因为11月样本量少），但因为margin够高，所以对combine是积极影响。另一方面，我发现margin对每日的渗透分的影响也很大，我之前简单粗暴地按margin打分竟然也意外地吃到了几天高base，但之后也开始俯冲。。附一张渗透分趋势图：


> [!NOTE] [图片 OCR 识别内容]
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-27
> 切换到周维度
> Ranl
> 0.30
> 0,73
> 0.50
> 1期2026-02-25
> Dal05105I5 Rank0g2
> 0,40
> 0,20
> 0.00
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026
> 7026
> 7026
> 7026
> 2026
> 7026
> 2026


除了以上结论外，有几位大佬的帖子也启发了我，非常感谢：

[[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md]([Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md)

[../顾问 FX25214 (Rank 22)/[Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md](../顾问 FX25214 (Rank 22)/[Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md)

最后祝大家马年combine，vf齐飞跃,拿钱拿到手软！都看到这了，给点个赞吧！

**顾问 WX84677 (Rank 69) 的解答与建议**:
这反转太戏剧性了！一个月从-1.2干到3.18，简直地狱到天堂。核心教训就几条：

1. 别月底入坑新 region 当冤种；
2. 新人远离D0高难度矿区；
3. margin比sharpe/fitness更保命、地区要广撒网但也别乱开。

最反直觉的是12月fitness和sharpe反而降了，但margin够硬combine照样起飞——说明手续费意识才是真金白银。

每日2个因子节奏稳，20+地区深度铺，这路子确实扎实。

感谢分享这活生生的"全错到全对"样本。


---

### 技术对话片段 3 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md
- **时间**: 3个月前

**提问/主帖背景 (LZ63377)**:
大家新年好呀，给大家拜个晚年了🧨🧨

首先声明我不是大佬，很多东西我都是一知半解的，还在逐渐摸索，combine和vf得分也有很大的运气成分。

我是去年11月下旬转为有条件顾问的，至今经历了两次combine刷新和一次vf刷新，变动如下图所示：


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combieq4lpha
> DOwET Dool
> 0 Seleced Alpha
> 0.97
> Combin」
> 3.71
> 090
> 300
> 0.80
> 200
> 0,70
> 100
> 050
> 0.00
> 1.00
> 0.50
> 0.45
> ~1.73
> 202503
> 202509
> 202510
> 202508
> 202509
> 202510
> 302500
> 302510
> 202571
> 202500
> 202510
> 202571
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512


可以看到前后仅一个月，我的combine就从-1.2拉升到了3.18，vf也涨到了0.92，对比过于强烈，完全可以说是从全错到全对的过程。因此我认为自己这个样本还是很具有研究价值的，对目前combine仍处于谷底的顾问应该也会有所启发，那么我11月和12月的提交情况是怎样的呢？又能得出什么结论呢？（省流直接跳到后面粗体看结论，右上角给点个赞吧，多谢了！）

因为平台在今年1月20更新了os期，所有此前提交的因子默认显示的都是os期数据，而我提交时自然不可能预见os表现，所以下面展示的仍然是is时期的数据。此外我提交的大部分都是atom，只有少量混pv。

先看11月份，这个月底我刚成为顾问，共提交了13个因子，数据如下（图有点宽，建议ctrl+放大看）：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 10
> 2.13
> 1.625
> 1.656
> 4.03
> 3.075
> 2.984
> 0.001243
> 0.000637
> 0.000747
> 0.1494
> 0.0736
> 0.0739
> EUR
> 01
> 1.92
> 1.9
> 1.9
> 3.01
> 2.855
> 2.855
> 0.001011
> 0.001002
> 0.001002
> 0.0765
> 0.0626
> 0.0626
> USA
> 01
> 1.58
> 1.58
> 1.58
> 2.71
> 2.71
> 2.71
> 0.000681
> 0.000681
> 0.000681
> 0.0561
> 0.0561
> 0.0561


再看12月份，这个月份共提交了61个因子，数据如下：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 对象数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 3
> 1.35
> 1.17
> 1.18
> 1.66
> 1.46
> 1.4267
> 0.007593
> 0.001492
> 0.003362
> 0.127
> 0.0825
> 0.0901
> EUR
> 18
> 3.08
> 1.26
> 1.4278
> 3.82
> 2.125
> 2.2739
> 0.002114
> 0.001282
> 0.001308
> 0.0834
> 0.0471
> 0.0515
> IND
> 器
> 21
> 3.32
> 1.77
> 1.8457
> 3.08
> 2.26
> 2.3048
> 0.002643
> 0.001136
> 0.001325
> 0.1931
> 0.1373
> 0.1359
> USA
> 19
> 3.07
> 1.59
> 1.7595
> 3.78
> 1.76
> 1.9811
> 0.007382
> 0.001876
> 0.002561
> 0.3445
> 0.11
> 0.1277


因为我最高的combine是总池，所以再补一张11、12月份汇总数据：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 13
> 2.13
> 1.61
> 1.5462
> 4.03
> 295
> 2.6246
> 0.007593
> 0.000731
> 0.00135
> 0.1494
> 0.0799
> 0.0776
> EUR
> 20
> 3.08
> 1.275
> 1.475
> 3.82
> 2.21
> 2.332
> 0.002114
> 0.001257
> 0.001278
> 0.0834
> 00484
> 0.0526
> IND
> 器
> 3.32
> 1.77
> 1.8457
> 3.08
> 2.26
> 2.3048
> 0.002643
> 0.001136
> 0.001325
> 0.1931
> 0.1373
> 0.1359
> USA
> 20
> 3.07
> 1.585
> 1.7505
> 3.78
> 1.805
> 2.0175
> 0.007382
> 0.001698
> 0.002467
> 0.3445
> 0.1068
> 0.1241


这样一来答案是不是显而易见了？接下来开始盘点全错和全对行为。

**全错：**

1. **月底入坑，提交量少，但却刚好够出combine分（这个也确实没啥好办法，总有我这种月底转正的倒霉蛋，好在提交量少很快就能冲回来）**
2. **一上来就做d0（数据少难度高）**
3. **只看fitness和sharpe,忽略了margin（就算os维持is期的表现都是亏的，更别提os可能还要俯冲一波了）**
4. **乱开地区又没点上塔（地区表现直接崩盘）**

**全对：**

1. **稳定提交，平均每日2个因子，不多不少（对于冲gm的顾问可能少了，但都准备冲gm了也不用我多说什么了）**
2. **尽量少做甚至不做d0了**
3. **开始注意各地区最低margin，保证不低于底线**
4. **每个地区都提交了20个以上的因子，稳定了地区表现**

一个反直觉的结论，12月提交的fitness和sharpe相比于11月是有下降的（也可能是因为11月样本量少），但因为margin够高，所以对combine是积极影响。另一方面，我发现margin对每日的渗透分的影响也很大，我之前简单粗暴地按margin打分竟然也意外地吃到了几天高base，但之后也开始俯冲。。附一张渗透分趋势图：


> [!NOTE] [图片 OCR 识别内容]
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-27
> 切换到周维度
> Ranl
> 0.30
> 0,73
> 0.50
> 1期2026-02-25
> Dal05105I5 Rank0g2
> 0,40
> 0,20
> 0.00
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026
> 7026
> 7026
> 7026
> 2026
> 7026
> 2026


除了以上结论外，有几位大佬的帖子也启发了我，非常感谢：

[[L2] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md]([L2] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md)

[[L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md]([L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md)

最后祝大家马年combine，vf齐飞跃,拿钱拿到手软！都看到这了，给点个赞吧！

**顾问 WX84677 (Rank 69) 的解答与建议**:
这反转太戏剧性了！一个月从-1.2干到3.18，简直地狱到天堂。核心教训就几条：

1. 别月底入坑新 region 当冤种；
2. 新人远离D0高难度矿区；
3. margin比sharpe/fitness更保命、地区要广撒网但也别乱开。

最反直觉的是12月fitness和sharpe反而降了，但margin够硬combine照样起飞——说明手续费意识才是真金白银。

每日2个因子节奏稳，20+地区深度铺，这路子确实扎实。

感谢分享这活生生的"全错到全对"样本。


---

### 技术对话片段 4 (原帖: 【Alpha灵感】A股换手率类因子)
- **原帖链接**: [Commented] 【Alpha灵感】A股换手率类因子.md
- **时间**: 1年前

**提问/主帖背景 (KJ42842)**:
标题：华泰单因子测试之换手率类因子

作者：林晓明

概述：该篇论文作者构建了近N个月每日换手率均值，标准差，及衍生的换手率乖离率等12个基于换手率的因子，首先分析了这些因子行业间的差异以及与市值因子的相关性，然后使用回归法和分层回测等因子测试流程中的因子收益率,t值,IC值等系统地验证了换手率因子在A股市场中的有效性。

Alpha Idea:

直接将论文中构建的因子原封不动的用Fast Expression实现。


> [!NOTE] [图片 OCR 识别内容]
> 图表1:
> 华泰单因子测试一换手率因子及其描述
> 大类因子
> 具体因子
> 因子描述
> turn_Im
> 个股最近 N 个月内日均换手率
> turn_3m
> N=l,
> turn_Gm
> bias_turn_Im
> 个股最近 N 个月内日均换手率除以最近2年内日均换手率
> 再减去1
> bias_turn_3m
> N=l,
> 换手率因子
> bias_turn Gm
> (Turnover
> std_turn_Im
> 个股最近 N 个月内日换手率序列的标准差
> Factor)
> std_turn_3m
> N=l, 3,
> std_turn_Gm
> bias_std turn Im
> 个股最近 N 个月内日换手率序列的标准差除以最近2年内日换手率序列的标
> bias_std_turn_3m
> 准差,
> 再减去1
> bias_std_turn Gm
> N=1, 3,


由于论文中论证了换手率因子的行业差异，所以我们选用Industry中性化，可以看出该alpha表现出明显的信号。


> [!NOTE] [图片 OCR 识别内容]
> 5|?
> S2
> 11
> .
> AESULTs
> LC
> Sotts
> CHIIOTITOPJD00
> 04014 MVU Sonwlatoa
> Chart
> UNcUCT
> 4T1
> Kl L
> Tl
> oCI
> [o
> 1o
> NUIuAUUATI
> 6C8
> AuttArIC
> Int
> UIN
> Utawlt
> APOy
> Urmr
> UTIhrMt +144290
> CAUTTUTTN
> OSU
> 50
> N


*Note: Sharesout is counted in millions on Brain*

*
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> stage
> IS
> 05
> Aggregate Data
> Sharpe
> TUrnover
> Ciness
> Returns
> Orawdown
> Margin
> 2.18
> 5.269
> 3.28
> 28.329
> 22.31%
> 107.64900
> Year
> Sharpe
> Tumover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.95
> 5.5930
> 二91
> 34.62-
> 1.70
> 123.81
> 118
> 73
> 2012
> 2.95
> 5.093
> 一56
> 29.91
> 5.73
> 117.5
> 1519
> 777
> 7013
> 22-
> 5.043
> 3.25
> 26.36-
> 112
> 10_.55
> 1511
> 371
> 2014
> 1.95
> 5.453
> 2-7
> 20.10--
> 7.00
> 73.30:
> 1-91
> 397
> 2015
> 0.03
> 5.753
> 0.02
> 1.09-7
> 22.31
> 3.30:
> 1373
> 10ED
> 2016
> 212
> 5.043
> 3.08
> 26-2-
> 7.30
> 10-.90:
> 1560
> 1009
> 2017
> 3.0-
> 5.313
> 5.36
> -5.517
> 7.15
> 175.17::
> 2016
> 96_
> 2013
> 192
> 一981
> 3.02
> 23.87
> 7.95
> 115,33:
> 2031
> 973
> 2012
> 2.5
> 5.113
> 一49
> 357
> 13.3-
> 141.32:
> 1976
> 1027
> 2020
> 1.43
> 5.373
> 1.33
> 2239
> 10.153
> 33:
> 1952
> 1059
> 7021
> 9-0
> 5.037
> 31.37
> 43372
> 2.301
> 527.62:
> 1971
> 1053
*

因为文中论证了换手率因子与市值的负相关性，所以我对市值进行分组再通过group_neutralize降低市值对换手率因子的影响，可以看出alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> SITUUO !
> SLIZ
> 5T73
> Sukma
> RESULTS
> LSRI
> ed
> OSOOOC
> Chart
> 1881
> Tot
> Ee]
> CO
> 3-
> A
> JOT
> TIII
> MUUTRUIUATWNI@
> TUAATONI@
> &1+1151118
> s
> AaT
> Dlawl
> Noply
> TUTTO 
> Volutsharoscut 1i2
> Rup utrallzt
> SanltUrTOp
> bCetlran (Cap , CanR O.1
> 7TNe
> SCUO
> 7 +
> o( a&
> ssnely



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marain
> 2.67
> 6.069
> 4.29
> 32.219
> 13.469
> 106.25900
> Year
> Sharpe
> Tumover
> Fitness
> Retums
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.21
> 6.319
> 5,45
> 36,133
> 4,6053
> 114,455
> 1394
> 756
> 2012
> 3.23
> 5.761
> 5,65
> 32,999
> 4,499
> 114.565
> 1505
> 791
> 2013
> 2.64
> 5.731
> 一11
> 30.234
> 4.625
> 105.514
> 1503
> 379
> 2014
> 2.92
> 6.2197
> 一-3
> 28,756
> 5.7895
> 92.67.9
> 177
> 910
> 2015
> 1,38
> 6.471
> 2'
> 20,97
> 13,46
> 64.77
> 1330
> 1048
> 2016
> 3.29
> 5.011
> 5,64
> 36,639
> 5.105
> 122.005
> 1634
> 935
> 2017
> 7.31
> 5.041
> 502
> 39,359
> 5,3795
> 131.92
> 1934
> 935
> 2018
> 2.50
> 5.329
> 一.10
> 33,599
> 7.1545
> 115.3
> 1997
> 1007
> 2019
> 3.05
> 5.0317
> 5,-0
> 38,876
> 11,0655
> 128.84
> 1959
> 10-
> 2020
> 1,11
> 6.357
> 1,27
> 16,31
> 9,811
> 51.385
> 1918
> 1093
> 2021
> 6.11
> 5.791
> 17,03
> 97.133
> 2.1455
> 335.72:
> 1952
> 1062


文章还对换手率因子进行了样本期长度的敏感性测试，发现用5天左右的长度能使回归因子收益率以及IC,IR达到最佳。所以，我将alpha的样本期长度从一个月（22个交易日）改为5天，可以看到alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> o
> CATCIN
> Chart
>  Uwcuo
> to
> Fg Ce
> CU
> ] [If
> Cggo
> SUIUAOe
> 62C
> TRUNCATION
> Isty
> UO1
> MA Mo
> Uul
> NOy
> Irmw
> Taloshriyt +111:
> RTO FutrT-LCnurmer,5
> LUCtTane (CAPI,
> TNRC
> N
> SCUO
> *0



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> TurnoVer
> Finess
> Relurns
> Drawdown
> Margin
> 2.90
> 13.989
> 4.81
> 38.449
> 10.049
> 55.01%00
> Year
> Sharpe
> Tumover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.27
> 13.743
> 5.57
> 39,84
> 4,73
> 57,99
> 117
> 733
> 2012
> 3.78
> 13.635
> 6.38
> 38,845
> 4.101
> 55.995
> 1525
> 771
> 2013
> 3.15
> 12.539
> 5.11
> 33.-0
> 5.10*
> 52.66*
> 1525
> 356
> 2014
> 2.32
> 14,321
> 3.39
> 23.14
> 5.369
> 37.975
> 143
> 90
> 2015
> 2,13
> 15.233
> 31
> 31,095
> 7,081
> 10,8
> 1373
> 1065
> 2016
> 3.33
> 13.883
> 5.71
> 39.365
> 5.055
> 55.71
> 1695
> 97_
> 2017
> 2.79
> 13.239
> 一91
> 41.16
> 10.0_95
> 62.01
> 1992
> 935
> 2018
> 3.30
> 13.161
> 6.15
> 45.72
> 6.5193
> 69.505
> 2010
> 99
> 2019
> 3.79
> 13.691
> 7.50
> 53.545
> 9,89
> 78.22*
> 1989
> 101
> 2020
> 114
> 13.91
> 1-1
> 21.3355
> 9.3555
> 30.67
> 195-
> 1057
> 2021
> 5.62
> 12.439
> 15.11
> 90.33
> 1.2235
> 125.334
> 1973
> 1046


最后，文中描述如果从收益率的角度来说换手率和换手率序列标准差较好，如果从稳定性的角度来说换手率的乖离率和换手率序列标准差的乖离率较好。


> [!NOTE] [图片 OCR 识别内容]
> Sattos
> CUTITTIISOINO
> Kogat
> Chart
> T-
> TTMT T
> Tn504
> LUT
> UCI
> TI
> SITAIATO
> TUtCATIC
> UJU
> LTTTIo
> TeTa
> 
> II
> Ug
> TITT
> To4rMJ
> Il
> (_*d_de(tu noer 51/1_Jtd_do(tumer 500)1;
> OTTuT AIIIsIIa
> UUCLAICaN(Ca !
> 0]; ,0.19;
> T
> 50
> 750
> IUTCI1
> 5Pnl 1TOI
> Urto
> +a



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> 05
> Aggregate Data
> Sharpe
> Turnover
> Finess
> Returns
> Drawdown
> Margin
> 2.96
> 26.899
> 2.98
> 27.339
> 12.389
> 20.329000
> Year
> Sharpe
> Turnover
> Fitness
> Returs
> Drawuown
> Margin
> Long Count
> Short Count
> 2011
> 2.30
> 26,479
> 2.53
> 24.209
> 3.749
> 13.285
> 1413
> 737
> 2012
> 3.97
> 26,019
> 1,24
> 29.613
> 3.6330
> 22.775
> 1519
> 776
> 2013
> 3.35
> 27,554
> 3.35
> 27.584
> 3.333
> 19.95,。
> 1530
> 852
> 2014
> 2,11
> 27,459
> 1,43
> 13.5130
> 4,303
> 9.345
> 1521
> 366
> 2015
> 2.83
> 29.985
> 3,05
> 33.33
> 12381
> 222-5
> 148-
> 95
> 2016
> 4.15
> 26.599
> 4.89
> 35.94
> 一459
> 27.79
> 1719
> 950
> 2017
> 2.65
> 25,39北
> 2.72
> 26.753
> 5.2030
> 21.075
> 1953
> 1022
> 2018
> 一7
> 25.269
> 一95
> 3577
> 2.903
> 2332
> 1992
> 1012
> 2019
> 1,23
> 26,549
> 5.13
> 39.07
> 3.3635
> 29.344
> 1962
> 1040
> 2020
> 0.27
> 27,459
> 0,03
> 3.2035
> 9.1930
> 2.335
> 1935
> 1075
> 2021
> 2.37
> 27.179
> 2.93
> 29.533
> 1.729
> 21.72
> 1969
> 1055


从结果可以看出，虽然换手率乖离率因子的收益率不如换手率因子，但是该因子在更多的年份有更小的Drawdown, 因而有更平滑的PnL曲线和更高的Sharpe，与论文中的结论一致。

相关数据集：Price Volume Data for Equity

疑问与讨论：

1. 换手率因子如果在A股市场验证有效，是否在其他市场也是有效的？
2. 有什么方法可以进一步改进换手率因子Alpha使其可以达到Robust Universe Return?


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> 05
> PASS
> FulL
> Robust universe rerurns Of 10.7896Is below CutOff of 15.3896 (~095 OfAlohaj。
> WARNING
> 3 PENDING


**顾问 WX84677 (Rank 69) 的解答与建议**:
[KJ42842](/hc/en-us/profiles/12429216262167-KJ42842)  精彩，感谢分享！


---

### 技术对话片段 5 (原帖: 【Alpha灵感】A股换手率类因子)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】A股换手率类因子_18600255773719.md
- **时间**: 1 year ago

**提问/主帖背景 (KJ42842)**:
标题：华泰单因子测试之换手率类因子

作者：林晓明

概述：该篇论文作者构建了近N个月每日换手率均值，标准差，及衍生的换手率乖离率等12个基于换手率的因子，首先分析了这些因子行业间的差异以及与市值因子的相关性，然后使用回归法和分层回测等因子测试流程中的因子收益率,t值,IC值等系统地验证了换手率因子在A股市场中的有效性。

Alpha Idea:

直接将论文中构建的因子原封不动的用Fast Expression实现。


> [!NOTE] [图片 OCR 识别内容]
> 图表1:
> 华泰单因子测试一换手率因子及其描述
> 大类因子
> 具体因子
> 因子描述
> turn_Im
> 个股最近 N 个月内日均换手率
> turn_3m
> N=l,
> turn_Gm
> bias_turn_Im
> 个股最近 N 个月内日均换手率除以最近2年内日均换手率
> 再减去1
> bias_turn_3m
> N=l,
> 换手率因子
> bias_turn Gm
> (Turnover
> std_turn_Im
> 个股最近 N 个月内日换手率序列的标准差
> Factor)
> std_turn_3m
> N=l, 3,
> std_turn_Gm
> bias_std turn Im
> 个股最近 N 个月内日换手率序列的标准差除以最近2年内日换手率序列的标
> bias_std_turn_3m
> 准差,
> 再减去1
> bias_std_turn Gm
> N=1, 3,


由于论文中论证了换手率因子的行业差异，所以我们选用Industry中性化，可以看出该alpha表现出明显的信号。


> [!NOTE] [图片 OCR 识别内容]
> 5|?
> S2
> 11
> .
> AESULTs
> LC
> Sotts
> CHIIOTITOPJD00
> 04014 MVU Sonwlatoa
> Chart
> UNcUCT
> 4T1
> Kl L
> Tl
> oCI
> [o
> 1o
> NUIuAUUATI
> 6C8
> AuttArIC
> Int
> UIN
> Utawlt
> APOy
> Urmr
> UTIhrMt +144290
> CAUTTUTTN
> OSU
> 50
> N


*Note: Sharesout is counted in millions on Brain*

*
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> stage
> IS
> 05
> Aggregate Data
> Sharpe
> TUrnover
> Ciness
> Returns
> Orawdown
> Margin
> 2.18
> 5.269
> 3.28
> 28.329
> 22.31%
> 107.64900
> Year
> Sharpe
> Tumover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2011
> 2.95
> 5.5930
> 二91
> 34.62-
> 1.70
> 123.81
> 118
> 73
> 2012
> 2.95
> 5.093
> 一56
> 29.91
> 5.73
> 117.5
> 1519
> 777
> 7013
> 22-
> 5.043
> 3.25
> 26.36-
> 112
> 10_.55
> 1511
> 371
> 2014
> 1.95
> 5.453
> 2-7
> 20.10--
> 7.00
> 73.30:
> 1-91
> 397
> 2015
> 0.03
> 5.753
> 0.02
> 1.09-7
> 22.31
> 3.30:
> 1373
> 10ED
> 2016
> 212
> 5.043
> 3.08
> 26-2-
> 7.30
> 10-.90:
> 1560
> 1009
> 2017
> 3.0-
> 5.313
> 5.36
> -5.517
> 7.15
> 175.17::
> 2016
> 96_
> 2013
> 192
> 一981
> 3.02
> 23.87
> 7.95
> 115,33:
> 2031
> 973
> 2012
> 2.5
> 5.113
> 一49
> 357
> 13.3-
> 141.32:
> 1976
> 1027
> 2020
> 1.43
> 5.373
> 1.33
> 2239
> 10.153
> 33:
> 1952
> 1059
> 7021
> 9-0
> 5.037
> 31.37
> 43372
> 2.301
> 527.62:
> 1971
> 1053
*

因为文中论证了换手率因子与市值的负相关性，所以我对市值进行分组再通过group_neutralize降低市值对换手率因子的影响，可以看出alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> SITUUO !
> SLIZ
> 5T73
> Sukma
> RESULTS
> LSRI
> ed
> OSOOOC
> Chart
> 1881
> Tot
> Ee]
> CO
> 3-
> A
> JOT
> TIII
> MUUTRUIUATWNI@
> TUAATONI@
> &1+1151118
> s
> AaT
> Dlawl
> Noply
> TUTTO 
> Volutsharoscut 1i2
> Rup utrallzt
> SanltUrTOp
> bCetlran (Cap , CanR O.1
> 7TNe
> SCUO
> 7 +
> o( a&
> ssnely



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Marain
> 2.67
> 6.069
> 4.29
> 32.219
> 13.469
> 106.25900
> Year
> Sharpe
> Tumover
> Fitness
> Retums
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.21
> 6.319
> 5,45
> 36,133
> 4,6053
> 114,455
> 1394
> 756
> 2012
> 3.23
> 5.761
> 5,65
> 32,999
> 4,499
> 114.565
> 1505
> 791
> 2013
> 2.64
> 5.731
> 一11
> 30.234
> 4.625
> 105.514
> 1503
> 379
> 2014
> 2.92
> 6.2197
> 一-3
> 28,756
> 5.7895
> 92.67.9
> 177
> 910
> 2015
> 1,38
> 6.471
> 2'
> 20,97
> 13,46
> 64.77
> 1330
> 1048
> 2016
> 3.29
> 5.011
> 5,64
> 36,639
> 5.105
> 122.005
> 1634
> 935
> 2017
> 7.31
> 5.041
> 502
> 39,359
> 5,3795
> 131.92
> 1934
> 935
> 2018
> 2.50
> 5.329
> 一.10
> 33,599
> 7.1545
> 115.3
> 1997
> 1007
> 2019
> 3.05
> 5.0317
> 5,-0
> 38,876
> 11,0655
> 128.84
> 1959
> 10-
> 2020
> 1,11
> 6.357
> 1,27
> 16,31
> 9,811
> 51.385
> 1918
> 1093
> 2021
> 6.11
> 5.791
> 17,03
> 97.133
> 2.1455
> 335.72:
> 1952
> 1062


文章还对换手率因子进行了样本期长度的敏感性测试，发现用5天左右的长度能使回归因子收益率以及IC,IR达到最佳。所以，我将alpha的样本期长度从一个月（22个交易日）改为5天，可以看到alpha表现进一步提升。


> [!NOTE] [图片 OCR 识别内容]
> o
> CATCIN
> Chart
>  Uwcuo
> to
> Fg Ce
> CU
> ] [If
> Cggo
> SUIUAOe
> 62C
> TRUNCATION
> Isty
> UO1
> MA Mo
> Uul
> NOy
> Irmw
> Taloshriyt +111:
> RTO FutrT-LCnurmer,5
> LUCtTane (CAPI,
> TNRC
> N
> SCUO
> *0



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> IS
> 05
> Aggregate Data
> Sharpe
> TurnoVer
> Finess
> Relurns
> Drawdown
> Margin
> 2.90
> 13.989
> 4.81
> 38.449
> 10.049
> 55.01%00
> Year
> Sharpe
> Tumover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 201
> 3.27
> 13.743
> 5.57
> 39,84
> 4,73
> 57,99
> 117
> 733
> 2012
> 3.78
> 13.635
> 6.38
> 38,845
> 4.101
> 55.995
> 1525
> 771
> 2013
> 3.15
> 12.539
> 5.11
> 33.-0
> 5.10*
> 52.66*
> 1525
> 356
> 2014
> 2.32
> 14,321
> 3.39
> 23.14
> 5.369
> 37.975
> 143
> 90
> 2015
> 2,13
> 15.233
> 31
> 31,095
> 7,081
> 10,8
> 1373
> 1065
> 2016
> 3.33
> 13.883
> 5.71
> 39.365
> 5.055
> 55.71
> 1695
> 97_
> 2017
> 2.79
> 13.239
> 一91
> 41.16
> 10.0_95
> 62.01
> 1992
> 935
> 2018
> 3.30
> 13.161
> 6.15
> 45.72
> 6.5193
> 69.505
> 2010
> 99
> 2019
> 3.79
> 13.691
> 7.50
> 53.545
> 9,89
> 78.22*
> 1989
> 101
> 2020
> 114
> 13.91
> 1-1
> 21.3355
> 9.3555
> 30.67
> 195-
> 1057
> 2021
> 5.62
> 12.439
> 15.11
> 90.33
> 1.2235
> 125.334
> 1973
> 1046


最后，文中描述如果从收益率的角度来说换手率和换手率序列标准差较好，如果从稳定性的角度来说换手率的乖离率和换手率序列标准差的乖离率较好。


> [!NOTE] [图片 OCR 识别内容]
> Sattos
> CUTITTIISOINO
> Kogat
> Chart
> T-
> TTMT T
> Tn504
> LUT
> UCI
> TI
> SITAIATO
> TUtCATIC
> UJU
> LTTTIo
> TeTa
> 
> II
> Ug
> TITT
> To4rMJ
> Il
> (_*d_de(tu noer 51/1_Jtd_do(tumer 500)1;
> OTTuT AIIIsIIa
> UUCLAICaN(Ca !
> 0]; ,0.19;
> T
> 50
> 750
> IUTCI1
> 5Pnl 1TOI
> Urto
> +a



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Spectacular
> Stage
> 05
> Aggregate Data
> Sharpe
> Turnover
> Finess
> Returns
> Drawdown
> Margin
> 2.96
> 26.899
> 2.98
> 27.339
> 12.389
> 20.329000
> Year
> Sharpe
> Turnover
> Fitness
> Returs
> Drawuown
> Margin
> Long Count
> Short Count
> 2011
> 2.30
> 26,479
> 2.53
> 24.209
> 3.749
> 13.285
> 1413
> 737
> 2012
> 3.97
> 26,019
> 1,24
> 29.613
> 3.6330
> 22.775
> 1519
> 776
> 2013
> 3.35
> 27,554
> 3.35
> 27.584
> 3.333
> 19.95,。
> 1530
> 852
> 2014
> 2,11
> 27,459
> 1,43
> 13.5130
> 4,303
> 9.345
> 1521
> 366
> 2015
> 2.83
> 29.985
> 3,05
> 33.33
> 12381
> 222-5
> 148-
> 95
> 2016
> 4.15
> 26.599
> 4.89
> 35.94
> 一459
> 27.79
> 1719
> 950
> 2017
> 2.65
> 25,39北
> 2.72
> 26.753
> 5.2030
> 21.075
> 1953
> 1022
> 2018
> 一7
> 25.269
> 一95
> 3577
> 2.903
> 2332
> 1992
> 1012
> 2019
> 1,23
> 26,549
> 5.13
> 39.07
> 3.3635
> 29.344
> 1962
> 1040
> 2020
> 0.27
> 27,459
> 0,03
> 3.2035
> 9.1930
> 2.335
> 1935
> 1075
> 2021
> 2.37
> 27.179
> 2.93
> 29.533
> 1.729
> 21.72
> 1969
> 1055


从结果可以看出，虽然换手率乖离率因子的收益率不如换手率因子，但是该因子在更多的年份有更小的Drawdown, 因而有更平滑的PnL曲线和更高的Sharpe，与论文中的结论一致。

相关数据集：Price Volume Data for Equity

疑问与讨论：

1. 换手率因子如果在A股市场验证有效，是否在其他市场也是有效的？
2. 有什么方法可以进一步改进换手率因子Alpha使其可以达到Robust Universe Return?


> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Stage
> 05
> PASS
> FulL
> Robust universe rerurns Of 10.7896Is below CutOff of 15.3896 (~095 OfAlohaj。
> WARNING
> 3 PENDING


**顾问 WX84677 (Rank 69) 的解答与建议**:
[KJ42842](/hc/en-us/profiles/12429216262167-KJ42842)  精彩，感谢分享！


---

### 技术对话片段 6 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】ai推荐比率按照实际含义推荐operator经验分享_37141295460375.md
- **时间**: 6个月前

**提问/主帖背景 (XG43628)**:
其实这是之前的思路，不过那会还可以通过大规模回测来找到alpha，现在限制回测之后才对改工作流进行了一定的修改，通过昨天kuiqi老师说的，我的想法其实就是来自最早开始kunqi老师讲的比率，只是这是通过ai去做数据集分析，数据字段分析以及数据类型介绍和对于的paper来做比率，完成比率生成之后，让ai按照比率的实际意义去做operator推荐。

下面是工作流内容：

```
# Alpha 生成工作流本工作流旨在通过探索 WorldQuant BRAIN 平台上的数据集，系统地生成具有经济意义的 Alpha 表达式。## 步骤 1: 认证在开始任何操作之前，必须先通过 BRAIN 平台认证。```<use_mcp_tool>  <server_name>worldquant-brain-platform</server_name>  <tool_name>authenticate</tool_name>  <arguments>    {}  </arguments></use_mcp_tool>```## 步骤 2: 获取数据字段确定目标市场和数据集，然后获取所有可用的数据字段。**参数:***   `region`: 目标区域 (例如, `ASI`, `USA`, `EUR`, `GLB`)*   `universe`: 目标股票池 (例如, `TOP3000`, `MINVOL1M`)*   `dataset_id`: 目标数据集 (例如, `other466`, `fundamental31`, `analyst15`)**示例:**```<use_mcp_tool>  <server_name>worldquant-brain-platform</server_name>  <tool_name>get_datafields</tool_name>  <arguments>    {      "region": "ASI",      "universe": "MINVOL1M",      "dataset_id": "other466"    }  </arguments></use_mcp_tool>```## 步骤 3: 分析与生成 Alpha 表达式仔细阅读获取到的数据字段描述，理解其经济含义，并遵循以下策略生成 Alpha 表达式：*   **避开常规组合**: 专注于发现非传统的、但具有强大经济逻辑的组合。*   **字段数量**: 严格使用两个字段或三个字段进行组合。*   **数据类型处理**: 如果字段是 `VECTOR` 类型，在进行算术运算前使用 vec_类型 等聚合函数，并在生成组合时请考虑用vec_类型操作符的实际经济学含义；例如：计算当天事件数量： vec_sum(datafiled)/vec_avg(datafield). 感觉蛮有用的，如果是新闻数据可以用来看当天热度。*   **算术运算**: 仅使用 `+`, `-`, `*`, `/`。*   **排除项**: 不使用 `group` 类型 `operator`、`if_else` 和 `trade_when`。**生成策略示例并按照策略生成20个组合 (基于数据集描述以及数据字段描述并且尽量多样化):**## 步骤 4: 根据生成组合的实际含义套用operator，从operator.json中获取有关operator的详细信息*   **使用operator有实际含义**: 要有实际经济学含义或者数学含义。*   **使用规范**: 严格按照operator.json中的operator语法使用operator，注意：请勿对ts_套用超过3层，group_套用超过两层**按照生成的20个组合套用operator演变出100个表达式**## 步骤 5: 保存并检查将生成的 Alpha 表达式保存到 JSON 文件中，并仔细检查以确保所有使用的字段都来自指定的数据集。## 知识库目录Resources里面按照region_decay_universe_dataset的文件名，每个文件包含对应数据集的介绍，和Research Paper。**示例:**```<write_to_file>  <path>eur_anl4__alphas_combinations.json</path>  <content>  ["group_neutralize(zscore(ts_zscore(anl4_afv4_eps_mean + anl4_afv4_cfps_mean, 22)),(market))"]
```

以下是通过该工作流生成的一些alpha表现：


> [!NOTE] [图片 OCR 识别内容]
> 毗 Rszular Alpha
> Pyramid theme: USAIDIIRISK :1.2
> Fyramig
> T=
> USAIDIIOTHER *.3
> AEgregate Data
> SIaUe
> TUINI
> TUIe
> Cu
> LUTir
> Simulation Settings
> 1.58
> 10.12%
> 1.84
> 16.899
> 17.2995
> 33.399200
> IntrumenT
> Reglon
> Unierse
> Uarguag
> Gecy
> Ulay
> Trumcabo
> Mempliaton
> Rselriaboq
> NaN Handling
> Uat Handling
> NaxTrer
> CUu
> TUIJCJI
> Fasl Culeysiul
> UuUr FaLluls
> Ver i '
> Tunwer
> C
> Relr
> Uad
> Lor Cunt
> 1O
> U1
> 1114
> 0
> ZOI
> 954
> TOC
> 5.93乩
> 5771
> Clone Alpha
> 95
> 6.714
> 17.29;
> 3[
> 1
> 19
> 754
> 11274
> 1O.
> T59
> T5
> Chart
> 2013
> 1d
> 3,164
> 3314
> UTT
> 2790
> 154
> J5.9
> T3S
> 571
> LU
> 1TC
> 1
> TTU
> 4344
> 1956
> J35
> 759
> 2391
> N
> 1u
> 4,94
> 4Jt
> 9
> 1.524
> 1.-0
>  |555
> 5TIIL
> Investability constrained
> AEgregate Data
> CAIc
> TUIC
> Fuies
> ReluIrI
> CreUL
> 55
> 6.6
> 1.35
> 9.4095
> 7.53%
> 28.46900
> Jul 1
> Jul'1-
> Jn 15
> Jul (5
> Jul 16
> Jul"17
> Jan(
> Jul'13
> Ju"1g
> J '20
> Ju'20
> JUl 21
> Jan 2
> Jul72
> J 2
> 医 Correlation
> Self Correlation
> Mariruir
> LITiIJrT
> LuRu
> OS Testing Status
> Period
> 0121
> JOOILOrrelatlon
> Mariruir
> LIimrr
> Run Fr 1219/2025
> 3.27F
> .4202
> 0.0944
> I1PENDING
> Lorrelatlon
> Mariruir
> LIimrr
> LslRun Fr 1219/2025
> 3.26 F
> 0.5955
> 0.5501
> 10ON
> Sro
> Myn
> Ja
> Jns
> J T
> Jar
> 15121
  
> [!NOTE] [图片 OCR 识别内容]
> 酡 Sirele Data Set Apna
> 酡 Resu arApkz
> FyramiyeM=: USNDIINACRO*1
> AEgregate Data
> SMulre
> TUIe
> OIgUUIT
> Maleir
> SimMatiOn
> Settings
> 1.58
> 5.5696
> 2.01
> 20.3396
> 17.8196
> 73.
> 19623
> IntumenT
> Reoo
> Untere
> Uanguag
> Decay
> Uely
> Truncabo
> Memliaton
> Pastedrtabon
> NaN Handling
> Ut Handling
> Iax Tra
> CUun
> TUJLTI
> FJsl Culeysiull
> TrUUI FJLLUI
> Ver f
> Sme
> Tunover
> Fnees
> Rehrr
> Odon
> Log Colit
> 5354
> 1TO
> 7324
> 5.26〉
> 5 IU
> 5[
> 106
> 3.103〉
> Clone Alpha
> 00
> 5204
> UzGy
> 95GCU
> O[?
> 2015
> 5
> 955
> 10359
> 945
> TJU
> 2.329
> TSC
> O
> Chart
> 2013
> 3旧
> 17.549
> 4.10s
> GSC?
> 5.5S
> J6.249
> GP
> 1E?
> L3u
> |
> 145C
> 7.64
> 5.26弘
> 34.029
> 13.754
> 10-
> 27
> 5154
> 594
> TIC
> 221.725
> TON
> TJ
> 19.5
> 1.194
> 116GC
> SOOOR
> Investability constrained
> 4831283TE
> 0at3
> TAI
> TUIIU
> Fitriey
> ReluTiy
> UIrJlJUIT
> 1.34
> 4.61%
> 1.49
> 15.5496
> 15.52%
> 67.51900
> Jul1
> Jar "
> Jul'14
> Jn 1s
> Jul
> Jan 16
> Jul 16
> Jn 17
> Ju"17
> Jan 13
> Jul'13
> Ju'19
> J '20
> Ju20
> J37"21
> Jul 21
> Jan 2
> Jul 22
> Jn 2
> Correlation
> SeITLOTTEIaTIOO
> Matirruiri
> LIiIrT
> LFu
> OS Testing Status
> Period
> VOe
> LOOILOrrelatlon
> Mlatiruir
> LIiIJrT
> Lust Run
> I1PENDING
> Prod Correlation
> Mariruiri
> LrimJrri
> Lusl Rur: Fri; 12/192025
> 0.6714
> 0.6374
> 10ON
> AIphas
> 1S0
> Mangn
> Ja=
  
> [!NOTE] [图片 OCR 识别内容]
> #Per Pool Aphs
> # Resusr Lphs
> FyrmiJtems USADIINACRO .11
> Fyramidem= USADIIOTHER  .
> ABBregatE
> Uata
> SApr
> TUITIII
> Cm
> UTr
> SIIIUIatIOI
> Settings
> 1.65
> 22.13%
> 1.57
> 22.68%
> 14.019
> 20.5093o0
> InslrumerTe
> Reoo
> Untete
> UIa
> Decay
> T
> Neualtalon
> Paselriobon
> NaN Handling
> Uut Handling
> Max Trade
> LUU
> 70?3030
> Crpressiun
> Cruwdrg Fatlors
> Sharpe
> Tunoer
> Fuess
> Tr
> Uro
> Manga
> Long Count
> 20IJ
> 7.324
> 0.67
> 14.114
> 11.3北
> 7154
> 75.174
> 21.7E9
> 1.51北
> 7
> 74564
> 19GCN
> _n
> 161U
> Clone Alpha 
> 16g
> 21.714
> G2T
> -57
> 71.7014
> 1
> 5594
> 165k
> Chart
> 22.94
> 1,T0
> T
> 53
> 7139
> 7170
> TO
> 30
> 224:
> 19.964
> 0.65
> 1.SC
> 1.094
> 151
> 2041
> 74.33
> 46.179
> 5514
> 373
> 7102
> 19114
> 2.26
> 9.9
> T41
> TON
> 1554
> 7.64
> 25.554
> 1
> 2173
> OOOr
> Investability constrained
> AEgregate Data
> 31+1
> OO A TO
> N'y
> 0.55
> 12.02%6
> 0.34
> 4.88%
> 16.66%
> 290
> Jult
> lan
> Jn 1s
> Juli
> Jan ts
> Jul 16
> JEn 1
> Jan
> JUI /
> Jan
> Ju'1g
> 139 UI
> J0
> J'21
> Jul 21
> Jn  
> Jul-
> Jn 卫
> Correlation
> Self Correlation
> TIATTTITT
> T
> OS Testing Status
> Period
> Dne
> Correlation
> TIAITTITT
> T
> 11PENDING
> Prod Correlation
> TIAITTITT
> T
> 174+920T
> SJ0P
> 0.6332
> 0.6739
> 10ON
> 兽
> 101
> Ca
> Vrs
> 0
> Ju_
> JU
  
> [!NOTE] [图片 OCR 识别内容]
> Code
> I IS
> Summary
> =TOI
> 酡 Reguldr Nplz
> KaIIULII
> INDN
> TATTCLLTTTIL
> CUOMTST
> LLUTULJtU LJt
> ShaR
> [-51
> Mrlr
> 1.97
> 8.2993
> 1.14
> 4.205
> 4,0435
> 4930
> Shm
> TT
> T
> Kt
> Umo
> M
> IoCmrt
> Shot Count
> Simulation Settings
> OC
> 0
> U00
>  :
> I-hmt
> FemO
> U
> Ut
> Dco
> C
>  
> mh
> --
> IHm
> Ul
> N 
> 1
> 1.70
>  :
> ECUIR
> WI'SLIII
> TuErCTslOT
> L
> 一 |
> :
> 二75
> T9
> T =:
> 6455
> Ug0
> 15:
> Clone Nlpha
> U
> -447
> :
> !
> :
> Chart
> 32
> +34=
> :
> Su
> 1.0
> 25
> 1T:
> 53
> 24 45:
> 20JU
> AMER
> LLUTULJtU LJt
> [sU
> 1,0JOk
> 1.17
> 4.0591
> 923
> 3,3435
> 279630
> APAC
> I
> Hri '1
> Jun '15
> Il'
> JuI I
> JUI IE
> 1'
> 1TI '13
> Jul'1
> A
> Jn 20
> Jl'I
> 1'1
> Jul'z1
> Jul'
> TI '
> LLUTULJtU LJt
> CCJri
> LIrIr
> +39
> 2.7093
> +3435
> 363
> 9.929t30
> EMEL
> LLUTULJtU LJt
> ShTCC
> UITTTNIn
> 47
> 1,5545
> 0,41
> 0.959
> 1.2493
> 12.289630
> OS Testing Status
> Perin 
> Investabillity Constrained
> LLUTULJtU LJt
> ShTCO
> OTIn
> Wnlr
> 1.53
> 6,7145
> 0,94
> 4.153
> 5.2093
> 12.209630
> I1PENDINC
> 座 Correlation
> SUIT CorrelJion
> NmUm
> UTITTUI
> oOTon
> TMNT
> CmmN
> SIT - F
> 17119217
> 
> 0.5978
> -0.3238
> 44111
> Ju 1
> 川 I
> Nl I
> Jn 2


然后通过这些alpha再去缘分一道桥，在同一个region self corr跟prod corr会比较高但是其他region能出基本上都是可以交的regular alpha，差一些的也可以通过ai优化流程去优化一下，基本上也可以交成regular alpha，实在是不行的就尽量交成1个waring的ppa也不错。

如果贴子给大家带来一些帮助，请大家给我点点赞！

**顾问 WX84677 (Rank 69) 的解答与建议**:
我也在尝试往这个方向努力，由 AI 先对数据集进行分析并输出有经济学意义的 “两两字段组合”，并推荐与之匹配的因子策略。然后再基于此去构造 alpha 表达式。

还在摸索中，感谢分享给予灵感！

============================ 积跬步，至千里 =============================


---

### 技术对话片段 7 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template_37117908343831.md
- **时间**: 6个月前

**提问/主帖背景 (FF56620)**:
最近大趋势下，想必大家都在使用 72变之类的功能，而72变中，作者提供了一套模板，出货率还不错，不过在此基础上，我通过论坛，让大模型又总结了一份Alpha模板，如标题所言，这份模板均来自社区，所以是来自社区的馈赠

我自己用下来，出货率还不错，和内置模板相当，甚至还能更好一点，不过大家还是要自行评估一下，部分来自社区的论坛也存在过拟合的风险，如有帮助，欢迎点赞，如有错漏，请帮忙指出

```
    ## 模板格式说明

    每个模板使用以下占位符格式：
    - `<ts_op/>` - 时间序列操作符，如 `ts_rank`, `ts_mean`, `ts_delta`, `ts_ir`, `ts_stddev`, `ts_zscore`
    - `<group_op/>` - 分组操作符，如 `group_rank`, `group_neutralize`, `group_zscore`
    - `<vec_op/>` - 向量操作符，如 `vec_avg`, `vec_sum`, `vec_max`, `vec_min`, `vec_stddev`
    - `<field/>` - 数据字段占位符
    - `<d/>` - 时间窗口参数，常用值: `{5, 22, 66, 126, 252, 504}`
    - `<group/>` - 分组字段，如 `industry`, `sector`, `subindustry`, `market`

**顾问 WX84677 (Rank 69) 的解答与建议**:
点赞评论加关注了，看着无比丰富多样，感谢分享。这就去尝试整合进自己的工作流。

============================== 积跬步，至千里 =============================


---

### 技术对话片段 8 (原帖: 【Community Leader -因子筛选与组合⭐】判断因子是否可以提交，稳住你的combine经验分享)
- **原帖链接**: [Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (SZ83096)**:
分享下我判断因子是否值得提交的一些经验，希望小伙伴们能有所收获。一个因子值不值得提交，一个是看因子本身的指标，一个是对组合的增益情况。对我个人而言，后者的重要性一般会大于因子本身的指标（这是在因子指标合格的情况下的）；一般很难找到所有指标对performance都是正面明显的。所以你需要在各个指标之间权衡。根据is performance 的正负面影响判断：可提交的情况fitness 是排首位的，一般fitness有明显增益，margin和sharpe的增益不明显，或者稍微一点负面影响，我会选择提交；95%的情况下，fitness 对最近3-5年 的performance 有明显的负面影响（比如-0.1），不提交;sharpe 和fitness,margin有增益，但是returns稍微有些负面影响，提交；什么情况下不会提交：1、margin不符合地区的最低要求，不提交3、fitness 最近几年明显负面影响，不提交( 超过1个年份<-0.1)4、sharpe  最近几年明显负面影响 ，不提交( 超过1个年份 <-0.1)3、多个指标对组合负面明显过大，即使自相关性低，也不提交很难一一列举对performance 影响的所有情况，是否提交这个因子，根据组合影响，个人情况判断。从因子本身的指标来看：1、sharpe>=1 ,fitness>=0.6 的前提下margin 必须达到各地区margin要求的最低标准，我一般要求比最低标准高万分之五（USA，eur）,glb和ASI 地区的margin有时候比较难找到超过15的，在没有选择的情况下，一般ASI 最低14，15；GLB 14，15（少部分情况下会只要求>10【点塔】）2、pnl线的波动比较小，向上，sharpe线不往下走；3、ASI 地区 还会观察下jpn的表现，如果jpn明显表现不佳或者或者kor表现明显大于其他地区的表现，不会提交以上是我个人的一些经验，可能考虑还欠缺一些其他的点，如果小伙伴有其他好的 判断方法，期待你评论区的分享如果想要保证combine 的稳定，我个人的经验是 绝对不要提交margin不合格、fitness 负面影响过大、最近3年sharpe 线明显下降，pnl趋于厂 的因子（个人经验）最后，给大家看看我现在的combine 情况，希望国区顾问的combine 都能保持稳定增长。

**顾问 WX84677 (Rank 69) 的解答与建议**:
这标准清晰得能当教科书了！fitness排首位、margin卡死地区底线+0.05%、sharpe≥1且fitness≥0.6才进门，最近3年任何指标明显掉链子直接pass——把"组合增益>单因子指标"的思路量化得明明白白。看完直接抄作业，感谢大佬分享！


---

### 技术对话片段 9 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】提高效率之过滤出ROBUST_UNIVERSE_SHARPE高的IND alpha经验分享_37112731513879.md
- **时间**: 6个月前

**提问/主帖背景 (MZ45384)**:
这个月开启了IND区域alpha探索之旅，由于IND只能交Regular Alpha，且大多时候会因为ROBUST_UNIVERSE_SHARPE不达标而卡住，因此不得不优化，如果我们选择该指标高于一定阈值的alpha，就能大大提高优化难度和出货效率。于是我写了一个函数，可以帮助筛选过滤符合一定要求的alpha。

```
def wait_get(sess, url: str, max_retries: int = 10) -> "Response":    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef ind_probe(s, alpha_list, cutoff):   # s即session   # alpha_list是上一步过滤出来的alpha_id列表   # cutoff是选择过滤的阈值，建议初始选择0.8，可以上下调整  may_list = []  for alpha_id in tqdm(alpha_list, total=len(alpha_list), desc='Checking ROBUST_UNIVERSE_SHARPE', colour='#00ff00'):      metrics = wait_get(s, f'[链接已屏蔽]).json()        for i in metrics['is']['checks']:            if i['name'] == 'LOW_ROBUST_UNIVERSE_SHARPE':                if i['value'] > cutoff:                    may_list.append([alpha_id, i['value']])                    break    df = pd.DataFrame(may_list, columns=['alpha_id', 'ROBUST_UNIVERSE_SHARPE']).set_index('alpha_id')    may_df = df.sort_values('ROBUST_UNIVERSE_SHARPE', ascending=False)    return may_df
```

最后返回的是一个按ROBUST_UNIVERSE_SHARPE倒序的dataframe:


> [!NOTE] [图片 OCR 识别内容]
> Checking
> ROBUST UNIVERSE SHARPE: 100%
> 7/7
> [00:06<00:00,
> 2.14it/s]
> [2]:
> ROBUST UNIVERSE SHARPE
> alpha_id
> ak3oveNo
> 1.06
> kqsalvnk
> 1.04
> AIdKYNVW
> 0.95
> LLxknVI6
> 0.94
> SBVMWrLn
> 0.93
> JjLbYNPn
> 0.85


一轮搜索过滤下来选择第一个最高的，通常只有weight concentration的问题，优化难度肉眼可见地减小。在经过几天的空档期后，终于有alpha交了。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,00OK
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023


**顾问 WX84677 (Rank 69) 的解答与建议**:
很棒的方法，感谢分享。最近也是在跟 IND 地区死磕，结合大佬给出的工具，找待优化种子 alpha 的效率大大提升了~

=========================== 积跬步，至千里 ============================


---

### 技术对话片段 10 (原帖: 【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享)
- **原帖链接**: [Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (SZ83096)**:
今天是第4天了吧，对于为啥连续几天SA 都拿满60刀，我自己也挺困惑的。说说我的SA 怎么做的吧，小伙伴们应该感兴趣吧，我也不确定是不是正确的道路。

这个思路是我ACE主题（上周）最后几天手搓SA的时候，灵光一闪想到的。得益于游戏王的turnover分层思想，我一开始想着turnover分层的，但是ACE主题，turnover分层选择的结果不是很理想。看了learn的文档，尝试了下datacategories 分层，从我最熟悉datacategories开始尝试，试了下，效果挺好的。后面我尝试了不同datacategories的组合，可能是我选的datacategories 表现比较好，组合起来都挺不错的。

昨天 7月7号的SA 选择的思路

```
1、我先看看主题和🔝的这个datacategories 有多少alpha，然后我给datacategories 限制条件，比如op，turnover，prod，设置个大概的范围，看这个datacategories有多少，然后决定要不要再更细致的分层。这样完成了一个datacategories2、然后继续另一个独立的datacategories 设置，和第一个一样。3、最后2个或者2个以上的datacategories 加起来（|| 连接，）这样就相当于你保证选择了不同的datacategories 。
```

最后给大家看看最近4天的SA base吧

[图片 (图片已丢失)]

如果我的分享对你有帮助，记得点赞哦～～

**顾问 WX84677 (Rank 69) 的解答与建议**:
一次 SA 打满 60 刀也许是运气，连续几天每天都打满 60 刀，那就肯定是实力了！

感谢大佬无私分享自己的方法，非常受用。

我现在也是按照 datacategories 结合其他限制条件分层构建一个小池子，再组合多个小池子的方法去做 selection。真的挺容易出高表现，低相关 SA 的。

============================ 积跬步，至千里 ===========================


---

### 技术对话片段 11 (原帖: 【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享_33316845356439.md
- **时间**: 6个月前

**提问/主帖背景 (SZ83096)**:
今天是第4天了吧，对于为啥连续几天SA 都拿满60刀，我自己也挺困惑的。说说我的SA 怎么做的吧，小伙伴们应该感兴趣吧，我也不确定是不是正确的道路。

这个思路是我ACE主题（上周）最后几天手搓SA的时候，灵光一闪想到的。得益于游戏王的turnover分层思想，我一开始想着turnover分层的，但是ACE主题，turnover分层选择的结果不是很理想。看了learn的文档，尝试了下datacategories 分层，从我最熟悉datacategories开始尝试，试了下，效果挺好的。后面我尝试了不同datacategories的组合，可能是我选的datacategories 表现比较好，组合起来都挺不错的。

昨天 7月7号的SA 选择的思路

```
1、我先看看主题和🔝的这个datacategories 有多少alpha，然后我给datacategories 限制条件，比如op，turnover，prod，设置个大概的范围，看这个datacategories有多少，然后决定要不要再更细致的分层。这样完成了一个datacategories2、然后继续另一个独立的datacategories 设置，和第一个一样。3、最后2个或者2个以上的datacategories 加起来（|| 连接，）这样就相当于你保证选择了不同的datacategories 。
```

最后给大家看看最近4天的SA base吧


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/04/2025
> Super:
> 60.00
> Regular:
> 9.59
> Total:
> 69.59
> 40
> 20
> 2.Jul
> 3.Jul
> 4.Jul
> 5.Jul
> 6.Jul
> 7.Jul
> Period
> Regular
> Super
> Total


如果我的分享对你有帮助，记得点赞哦～～

**顾问 WX84677 (Rank 69) 的解答与建议**:
一次 SA 打满 60 刀也许是运气，连续几天每天都打满 60 刀，那就肯定是实力了！

感谢大佬无私分享自己的方法，非常受用。

我现在也是按照 datacategories 结合其他限制条件分层构建一个小池子，再组合多个小池子的方法去做 selection。真的挺容易出高表现，低相关 SA 的。

============================ 积跬步，至千里 ===========================


---

### 技术对话片段 12 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】你说你没有模板这里你多得用不完.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
吹哨人又来了，这次继续带来一个好消息。当你点击下面那个小灯，你就找对了地方。


> [!NOTE] [图片 OCR 识别内容]
> Expression Editor
> Clear
> SaVe Current Template
> Overrite Existing
> 找灵感
> ctime_series_operator/> (sentiment_difference,
> 〈days/〉)


操作如图


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)步骤3:输入搜索关键词搜索数据集
> 关键词可以是pyramid之类都行
> 步骤4:点击生成
> Configuration
> Select Dataset
> 3. Results
> Generate Nlpha Templates
> Download MD
> LLM Settings
> Search dataset _
> Search
> 以下绐出5 组可直接在平台落地的" Alpha 模板"。
> Base URL
> 每个模板均保留"插槽"一一用<>标注
> ~方便后续批量替换。
> 网格搜索或遗传进化。
> 已选数据集: analyst15
> https llapimoonshot cnlvl
> 所有模板已预置:
> 数据清洗 (backfill
> Winsorize)
> 步骤5:下载后慢慢品味和
> Name
> Mocel Name
> 经济逻辑 (动量
> 预期差
> 估值。质量。情绪)
> 实施,并把模板放入赢
> kimi-k2-turbo-preview
> Performance
> 常见中性化(行业/市值)与衰减选项
> tUTnoVer
> 控制接口
> (ts_target_tVr_* )
> 进行配置和展开
> Weighted
> API Key
> analystl0
> Analyst
> 模板1:  分析师预期动量
> (Estimate Revision Momentum)
> Test
> Estimates
> 经济直觉:  过去1个月 EPS 上调幅度越大的股票。未来越可能继续跑赢。
> 步骤1
> 输入API
> analyst11
> ESG SCOres
> 3Iph3
> eXP_Window(
> Simulation Settings
> Estimations OT
> 9rOUP_ZsCOre(
> analyst14
> T5_backfil(
> Reglon
> Fundamentals
> winsorize(<anll15_9r_12_m_Im_chg >, std=4j
> EUR
> Earnings
> Unierse
> analystl5
> fore-asts
> 9rOUP>
> TOP12O0
> Analyst
> Delay
> analyst4
> Estimate Data
> 〈half_life >
> for Equity
> 插槽:
> Integrated
> gr_12_m_Im_chg>
> 可换 3m/Gm 或 SAL/CPS/EBG 等
> 步骤2:按需选择
> analyst44
> Broker
> 〈groUp>
> industry
> Sector
> subindustry
> Estimates
> 〈half_life >
> 5~30天可调。控制换手
> Block comments Tor multiple lines
> Key
> Jecay
> Kej
> <anl15


**这是2.0时代了，拥抱交不完的Alpha吧。**

**下面有一个无脑mcp简易版**

**[[MCP]找灵感功能上手详解](../顾问 LW67640 (Rank 24)/[Commented] [MCP]找灵感功能上手详解经验分享.md)**

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢大佬分享，第一时间实践，期待好的结果！！

---------------------------------------------------------------------------------------------------

----------------------------------- 积跬步，至千里 -------------------------------------------

---------------------------------------------------------------------------------------------------


---

### 技术对话片段 13 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
吹哨人又来了，这次继续带来一个好消息。当你点击下面那个小灯，你就找对了地方。


> [!NOTE] [图片 OCR 识别内容]
> Expression Editor
> Clear
> SaVe Current Template
> Overrite Existing
> 找灵感
> ctime_series_operator/> (sentiment_difference,
> 〈days/〉)


操作如图


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)步骤3:输入搜索关键词搜索数据集
> 关键词可以是pyramid之类都行
> 步骤4:点击生成
> Configuration
> Select Dataset
> 3. Results
> Generate Nlpha Templates
> Download MD
> LLM Settings
> Search dataset _
> Search
> 以下绐出5 组可直接在平台落地的" Alpha 模板"。
> Base URL
> 每个模板均保留"插槽"一一用<>标注
> ~方便后续批量替换。
> 网格搜索或遗传进化。
> 已选数据集: analyst15
> https llapimoonshot cnlvl
> 所有模板已预置:
> 数据清洗 (backfill
> Winsorize)
> 步骤5:下载后慢慢品味和
> Name
> Mocel Name
> 经济逻辑 (动量
> 预期差
> 估值。质量。情绪)
> 实施,并把模板放入赢
> kimi-k2-turbo-preview
> Performance
> 常见中性化(行业/市值)与衰减选项
> tUTnoVer
> 控制接口
> (ts_target_tVr_* )
> 进行配置和展开
> Weighted
> API Key
> analystl0
> Analyst
> 模板1:  分析师预期动量
> (Estimate Revision Momentum)
> Test
> Estimates
> 经济直觉:  过去1个月 EPS 上调幅度越大的股票。未来越可能继续跑赢。
> 步骤1
> 输入API
> analyst11
> ESG SCOres
> 3Iph3
> eXP_Window(
> Simulation Settings
> Estimations OT
> 9rOUP_ZsCOre(
> analyst14
> T5_backfil(
> Reglon
> Fundamentals
> winsorize(<anll15_9r_12_m_Im_chg >, std=4j
> EUR
> Earnings
> Unierse
> analystl5
> fore-asts
> 9rOUP>
> TOP12O0
> Analyst
> Delay
> analyst4
> Estimate Data
> 〈half_life >
> for Equity
> 插槽:
> Integrated
> gr_12_m_Im_chg>
> 可换 3m/Gm 或 SAL/CPS/EBG 等
> 步骤2:按需选择
> analyst44
> Broker
> 〈groUp>
> industry
> Sector
> subindustry
> Estimates
> 〈half_life >
> 5~30天可调。控制换手
> Block comments Tor multiple lines
> Key
> Jecay
> Kej
> <anl15


**这是2.0时代了，拥抱交不完的Alpha吧。**

**下面有一个无脑mcp简易版**

**[[MCP]找灵感功能上手详解]([L2] [MCP]找灵感功能上手详解经验分享_37113649831831.md)**

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢大佬分享，第一时间实践，期待好的结果！！

---------------------------------------------------------------------------------------------------

----------------------------------- 积跬步，至千里 -------------------------------------------

---------------------------------------------------------------------------------------------------


---

### 技术对话片段 14 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
【量化日记 DAY1】：

新规后，因 model31 数据集权限被收走，之前的存货归零了。

外部环境总是会变化的，困难总是存在，大家都一样，不抱怨，想办法解决。

修改代码，重新选定了新的数据集，继续跑三阶模板。

皇天不负有心人，终于又出货了。

计划接下来一周，实现三阶模板自动化。解放人力后，将精力放在研究论坛中的模板大师。

各位战友，2025国服要崛起，一起加油吧！


---

### 技术对话片段 15 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
【量化日记 DAY2】：

今天继续用三阶模板跑 anl4 数据集，实测有坑的字段：

anl4_fcfps_flag、anl4_ffo_flag...

PNL表现：

[图片 (图片已丢失)]

进一步推断  **_flag**  后缀的字段要小心，可以考虑过滤掉先不跑，或者手动探索下数据情况。

以上分享，望能帮助战友避坑，节省时间。


---

### 技术对话片段 16 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
今天用量化研究小组虎哥提供的“双字段回归”模板，成功挖出不少 alpha。

相较于新手村赠送的三阶模板，此模板的优势明显：

1. 出货率高。

2. 提交后一次点亮两个金字塔，效率高。

模板如下：

group_rank(
     ts_regression (
          ts_zscore( ***matrix_data*** , 252), 
          ts_zscore(vec_sum( ***vector_data*** ), 252),
          252),
     densify(sector)
)

感谢虎哥—— **ZZ13271  [ZZ13271](/hc/en-us/profiles/27032633829527-ZZ13271)**

**祝各位伙伴，得所愿。**


---

### 技术对话片段 17 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第一季经验分享.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
昨天跑了一堆alpha，因为不符合比赛要求，打算囤一囤。

今天 13:00 后想筛着交几个，结果一 check，全部 self-cor 不合格。

问题是，我昨天到今天 13:00，这期间也没有提交过其他 alpha 啊！？

严重怀疑，是不是调(an)整(gai)了 check 规则啊？？？


---

### 技术对话片段 18 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
【量化日记 DAY1】：

新规后，因 model31 数据集权限被收走，之前的存货归零了。

外部环境总是会变化的，困难总是存在，大家都一样，不抱怨，想办法解决。

修改代码，重新选定了新的数据集，继续跑三阶模板。

皇天不负有心人，终于又出货了。

计划接下来一周，实现三阶模板自动化。解放人力后，将精力放在研究论坛中的模板大师。

各位战友，2025国服要崛起，一起加油吧！


---

### 技术对话片段 19 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
【量化日记 DAY2】：

今天继续用三阶模板跑 anl4 数据集，实测有坑的字段：

anl4_fcfps_flag、anl4_ffo_flag...

PNL表现：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 20O
> OOK
> OO
> DO
> 2013
> 201
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022


进一步推断  **_flag**  后缀的字段要小心，可以考虑过滤掉先不跑，或者手动探索下数据情况。

以上分享，望能帮助战友避坑，节省时间。


---

### 技术对话片段 20 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
今天用量化研究小组虎哥提供的“双字段回归”模板，成功挖出不少 alpha。

相较于新手村赠送的三阶模板，此模板的优势明显：

1. 出货率高。

2. 提交后一次点亮两个金字塔，效率高。

模板如下：

group_rank(
     ts_regression (
          ts_zscore( ***matrix_data*** , 252), 
          ts_zscore(vec_sum( ***vector_data*** ), 252),
          252),
     densify(sector)
)

感谢虎哥—— **ZZ13271  [ZZ13271](/hc/en-us/profiles/27032633829527-ZZ13271)**

**祝各位伙伴，得所愿。**


---

### 技术对话片段 21 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
昨天跑了一堆alpha，因为不符合比赛要求，打算囤一囤。

今天 13:00 后想筛着交几个，结果一 check，全部 self-cor 不合格。

问题是，我昨天到今天 13:00，这期间也没有提交过其他 alpha 啊！？

严重怀疑，是不是调(an)整(gai)了 check 规则啊？？？


---

### 技术对话片段 22 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-12-09

天气：晴

限流第一天，放平心态，拥抱变化。用 AI 折腾了一上午从0到1构建 alpha，结果非常让人沮丧。各种指标底下，checks 不通过，或者 PC > 0.7 ...

还是对 AI 提示词的使用经验太少，继续看论坛大佬的贴子学习吧，希望早日能搭建好自己的 AI 工作流，在新规下稳定产出 alpha。


---

### 技术对话片段 23 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-12-11

天气：小雨

AI 对 alpha 表现的优化日志：

**Date**: 2025-12-10

**Original Alpha ID**: O0aXMLkp

**Focus**: Improve 2-Year Sharpe (Target > 1.58) and Robust Universe Sharpe (Target > 1.0) using Hybrid Strategies.

## 🧪 Iteration Log (Round 4)

| Expression Description | Sharpe | 2Y Sharpe | Robust Sharpe | Result |

|------------------------|--------|-----------|---------------|--------|

| `rank(corr(75)) + rank(corr(20))` | 1.69 | 1.46 | 1.04 | **Best Combo** |

| `ts_decay_linear(rank(corr(75)), 2)` | N/A | N/A | N/A | Failed/Timeout |

| `group_rank(corr(75))` | 1.72 | 0.84 | 0.67 | High Sharpe, Low 2Y |

| `ts_zscore(decay(rank(corr(75))), 252)` | 1.23 | 0.39 | 0.64 | Failed |

| `ts_rank(corr(75), 252)` | 1.29 | 0.96 | 0.74 | Failed |

| `rank(corr(75)) - 0.5*rank(corr(252))` | 1.22 | 1.02 | 0.71 | Failed |

好奇，这样的优化方式，算不算过拟合？？


---

### 技术对话片段 24 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-09-03

天气晴

Q3冲刺月了，我的策略就是点塔和尝试用不同的操作符去构建 ATOM。

今早看到回测报告，发现每小时回测量大幅下降，赶紧打开研究小组群一探究竟。

果然，大家都在吐槽。是什么比赛结算么？或是说 combine 在计算？还是测试数据该偏移了？也可能几样一起来吧。真心希望平台赚多点，然后基础设施多投入点。

对于下一次 combine 更新，内心很矛盾，既期待又焦虑。因为7月份，我开始做 AMR 地区，base 收入可观但内心忐忑，不知 combine 和 vf 能否保住，祈祷。


---

### 技术对话片段 25 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-09-05

天气晴

PPA、RA 都断粮，用经典模板已经跑不出 pc < 0.5 的 alpha 了。靠着 SA 每天勉力支撑。

准备转战 JPN region D1 TOP1600，计划先跑一遍全量一阶，筛选出有信号且 pc 较低的 fields，构建 JPN “有信号子数据集”。随后，再根据 dataset 收益加成系数从高到低，在“有信号子数据集”中挑选字段，逐塔击破！

PS，怎么 OS 还不更新呢！？！


---

### 技术对话片段 26 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-06-25

上周工作太忙了，连着加班。每天投入到 wqb 的时间只有可怜的1小时，还是每天 6：00 起床挤出来的。为了备战下个赛季，现在跑的alpha全是 macro、news、sentiment 这种字段数量较少的 dataset。希望能把 model、fundamental、analyst 等已经深红的 dataset 稀释下。

=================================== 积跬步，至千里 ===================================


---

### 技术对话片段 27 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-06-26

昨天参加了国际会议，老师分享了 SAC 优化提升的方法。示例中 select expression 使用了 not(not(in(xxx)||in(xxx))) 这种写法，细想了一下。
not (in(A) & in(B))  与 not(not(in(A) || in(B))) 逻辑上是不等价的。
如果用前者构建 sa 表现不理想，试试换成后者的写法，会调整部分 select 的 alpha，表现也会有变化。
可以作为多样性的降低 pc 的方案。

================================= 积跬步，至千里 =================================


---

### 技术对话片段 28 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-06-27

月底啦，ppa 6月的时间窗口马上要截止。提醒各位顾问，注意调整 POWERPOOL tag，优中选优，争取能在月度评奖中获胜~~
另外，Q2最后冲刺倒计时！还有5天！！

================================= 积跬步，至千里 =================================


---

### 技术对话片段 29 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025年12日23日

天气：晴

今天凌晨起来手搓 520 SA，从 0.35 搓到 0.2986，满心欢喜准备提交，结果出现 1 FAIL： 'Your SuperAlpha contains unauthorized component alphas, please clone this alpha and re-simulate' 。

研究小组翻聊天记录发现似乎很多人都遇到了这个问题，无解。

提了 support，等待官方答复。

============================ 积跬步，至千里 ===========================


---

### 技术对话片段 30 (原帖: 【日常生活贴】我的量化日记第四季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXdY1z1B86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzQ5OTczMzIxNzgxOTktLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOUIlOUIlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyODg1NDg4Yy1jMDE5LTRjMTMtOWEyMi01MGRkYjgxOTkxYzcGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDg0Njc3BjsIVDoScmVzdWx0c19jb3VudGkg--23bdc5ecf43ba43f1d15c9625a99c4c23b9f8ebd
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。第一季和第二季（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第四季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-09-25天气晴Q3一直以 GM 为目标努力，金字塔还差 3 个，六维排在 75 左右，三项 combine 数据离 GM 均有差距。只剩定级前最后一次 combine 更新，需要有某项 combine 达到 GM，且六维进入前60。有希望，但不大。还有一周，把能做的做了即可。争其必然，顺其自然。


---

### 技术对话片段 31 (原帖: 【日常生活贴】我的量化日记第四季)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXdY1z1B86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzQ5OTczMzIxNzgxOTktLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOUIlOUIlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIikyODg1NDg4Yy1jMDE5LTRjMTMtOWEyMi01MGRkYjgxOTkxYzcGOwhGOglyYW5raQ46C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxXWDg0Njc3BjsIVDoScmVzdWx0c19jb3VudGkg--23bdc5ecf43ba43f1d15c9625a99c4c23b9f8ebd
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。第一季和第二季（【日常生活贴】我的量化日记第一季+【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN+【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN）因评论到达上限，已无法评论，特此展开第四季注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即无论您是否订阅，您都不会收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-10-08天气晴今天阅读了“传奇耐打王”关于alpha该不该交的帖子，受益匪浅。感恩他的无私分享，感叹咱们中文社区的分享精神。真希望什么时候我也能产出有价值的经验分享与大家。总结下 alpha 该不该交的判断标准：【必要条件】：1. PNL 平滑；2. Margin 达标（usa>5, eur>10, asi>15, glb>15），越高越好；3. sharp、fitness 达标，越高越好；4. 多空不赌博（我理解就是 (long count + short count) / universe 越高越好）【优化条件】：1. 低相关性（低 pc，低 sc）2. sharpe、fitness21年22年表现优秀（sharpe > 1）3. sharpe、fitness逐年表现优秀（sharpe > 1）4. margin21年22年表现优秀（参考必要条件的值）5. margin逐年表现优秀（参考必要条件的值）6. margin、returns 越高越好7. turnover 围绕在 12%，（低于5%的称为“死鱼因子”，看情况交）8. drawdown 越低越好9. 多空优秀（多空相加覆盖universe、多空接近、多空每年情况稳定）10. performance 不一定非要四绿两红，具体根据自己池子情况选择原贴解释详细，案例丰富，非常推荐大家阅读：《这个因子到底能不能交？（上） 【传奇耐打王系列一】》《这个因子到底能不能交？（下） 【传奇耐打王系列一】》


---

### 技术对话片段 32 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-09-25

天气晴

Q3一直以 GM 为目标努力，金字塔还差 3 个，六维排在 75 左右，三项 combine 数据离 GM 均有差距。

只剩定级前最后一次 combine 更新，需要有某项 combine 达到 GM，且六维进入前60。

有希望，但不大。

还有一周，把能做的做了即可。

争其必然，顺其自然。


---

### 技术对话片段 33 (原帖: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 WX84677 (Rank 69) 的解答与建议**:
2025-10-08

天气晴

今天阅读了“传奇耐打王”关于alpha该不该交的帖子，受益匪浅。感恩他的无私分享，感叹咱们中文社区的分享精神。真希望什么时候我也能产出有价值的经验分享与大家。

总结下 alpha 该不该交的判断标准：

【必要条件】：
1. PNL 平滑；
2. Margin 达标（usa>5, eur>10, asi>15, glb>15），越高越好；
3. sharp、fitness 达标，越高越好；
4. 多空不赌博（我理解就是 (long count + short count) / universe 越高越好）

【优化条件】：
1. 低相关性（低 pc，低 sc）
2. sharpe、fitness21年22年表现优秀（sharpe > 1）
3. sharpe、fitness逐年表现优秀（sharpe > 1）
4. margin21年22年表现优秀（参考必要条件的值）
5. margin逐年表现优秀（参考必要条件的值）
6. margin、returns 越高越好
7. turnover 围绕在 12%，（低于5%的称为“死鱼因子”，看情况交）
8. drawdown 越低越好
9. 多空优秀（多空相加覆盖universe、多空接近、多空每年情况稳定）
10. performance 不一定非要四绿两红，具体根据自己池子情况选择

原贴解释详细，案例丰富，非常推荐大家阅读：
 [《这个因子到底能不能交？（上） 【传奇耐打王系列一】》]([L2] 这个因子到底能不能交上 【传奇耐打王系列一】_35347883248919.md) 
 [《这个因子到底能不能交？（下） 【传奇耐打王系列一】》]([Commented] 这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md)


---

### 技术对话片段 34 (原帖: 步骤2: 计算残差与X平方的协方差)
- **原帖链接**: [Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法.md
- **时间**: 1 year ago

**提问/主帖背景 (WL13229)**:
一句话总结该活动：直接在评论区评论，分享高质量selection或者combo。

> ```
> 被审核通过者将获得BRAIN纪念品一份优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至6.14日23：59（以服务器时间为准）

活动要求：参赛同学可发布多个idea参赛，可以是selection idea或者combo idea；必须展示setting。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。


> [!NOTE] [图片 OCR 识别内容]
> S~A吣I
> BRAINI


> 纪念品图

再次强调🎇

**被审核通过者将获得BRAIN纪念品一份
优秀分享更有机会将获得50USD的一次性津贴。**

**顾问 WX84677 (Rank 69) 的解答与建议**:
【思路】：基于os 表现好 regular alpha (以下简称 ra) 的特征，构建 select 表达式。

已知满足以下条件的 ra , os 表现大概率较好：

1. returns > turnover;
2. returns > drawndown;
3. PNL 数据完整
4. long_count 与 short_count 接近（多空平衡）
5. long_count、short_count 较大（覆盖面广）
6. 表达式简单，字段较少（避免过拟合，例如 PPA、ATOM）
7. turnover 低于 10% （防止计算交易手续费后亏钱）
8. alpha 在不同 neutralization

第3~7点基本可以通过 select 语句表达，第8点通过同表达式回测所有 neutralizition 来判断（不同 neutralizition PNL 走势及 sa 的六维参数相近）

select 表达式如下：

```
#  sac 主题池，属于主题的得分 1，否则得分 0.theme_score = in(classifications, "POWER_POOL");# dataset_count 挑出 dataset_count 小于等于 2 的，dataset_count 越小得分约高dataset_score = (dataset_count <= 2)*-dataset_count;# turnover 挑选 [2%~10%] 的tvr_score = (turnover >= 0.02 && turnover <= 0.1);# pnlpnl_score = (long_count >= 1000 && short_count >= 1000) * -abs(long_count-short_count) * (long_count+short_count);select_score = theme_score*dataset_score*tvr_score*pc_score*pnl_score;select_score
```

希望对各位有帮助，祝大家在 sac 中取得好成绩。


---

### 技术对话片段 35 (原帖: 步骤2: 计算残差与X平方的协方差)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
一句话总结该活动：直接在评论区评论，分享高质量selection或者combo。

> ```
> 被审核通过者将获得BRAIN纪念品一份优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至6.14日23：59（以服务器时间为准）

活动要求：参赛同学可发布多个idea参赛，可以是selection idea或者combo idea；必须展示setting。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。


> [!NOTE] [图片 OCR 识别内容]
> S~A吣I
> BRAINI


> 纪念品图

再次强调🎇

**被审核通过者将获得BRAIN纪念品一份
优秀分享更有机会将获得50USD的一次性津贴。**

**顾问 WX84677 (Rank 69) 的解答与建议**:
【思路】：基于os 表现好 regular alpha (以下简称 ra) 的特征，构建 select 表达式。

已知满足以下条件的 ra , os 表现大概率较好：

1. returns > turnover;
2. returns > drawndown;
3. PNL 数据完整
4. long_count 与 short_count 接近（多空平衡）
5. long_count、short_count 较大（覆盖面广）
6. 表达式简单，字段较少（避免过拟合，例如 PPA、ATOM）
7. turnover 低于 10% （防止计算交易手续费后亏钱）
8. alpha 在不同 neutralization

第3~7点基本可以通过 select 语句表达，第8点通过同表达式回测所有 neutralizition 来判断（不同 neutralizition PNL 走势及 sa 的六维参数相近）

select 表达式如下：

```
#  sac 主题池，属于主题的得分 1，否则得分 0.theme_score = in(classifications, "POWER_POOL");# dataset_count 挑出 dataset_count 小于等于 2 的，dataset_count 越小得分约高dataset_score = (dataset_count <= 2)*-dataset_count;# turnover 挑选 [2%~10%] 的tvr_score = (turnover >= 0.02 && turnover <= 0.1);# pnlpnl_score = (long_count >= 1000 && short_count >= 1000) * -abs(long_count-short_count) * (long_count+short_count);select_score = theme_score*dataset_score*tvr_score*pc_score*pnl_score;select_score
```

希望对各位有帮助，祝大家在 sac 中取得好成绩。


---

### 技术对话片段 36 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】菜鸟日记代码小白如何稳住6个月VF09经验分享_38767793594775.md
- **时间**: 3个月前

**提问/主帖背景 (ZH41150)**:
各位新年好，这帖子一直想写很久了~先自我介绍一下，本人是代码小白，一点基础都没有，目前仍然使用一二三阶代码，去年3月末注册，5月底成为有条件顾问，8月底成为正式顾问，我的VF更新分数为0.5-0.89-0.91-0.91-0.92-0.95-0.96-0.92，也是比较幸运，在上个季度成为了第74名GM，极限卡位了，comb分数也是在第二次更新后稳定在2以上。


> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-04, October
> 2025
> December 31st, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> KOR
> TN
> HKG
> JPN
> AMR
> IND
> Analyst
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> News
> Option
> Other
> Price Volume
> 16
> 13
> 19
> Risk
> Sentiment
> Short Interest
> Social Media
> 1st


说实在，我个人也不知道自己为什么能一直保持0.9+的VF，我只能说一下我的思路和提交策略，基本每个月交1-2个区域的，每个字段点亮后就直接更换新的字段，基本一个月是20个塔左右，大概150个因子。（应该是符合weijie老师说的多样化提交）

至于提交因子的质量如何，有好有差，最低标准要求是sharpe>1,fit>0.5。margin分地区：USA5%+；EUR10%+；GLB10%+;ASI10%+;剩下基本都是10左右，但margin是否满足在我这里不是必要条件，一般我会考虑这个alpha是哪个数据集，如果是比较小众的数据集，会考虑塔的难易程度，简单来讲就是，能拉高尽量拉高，不能拉高就看近年趋势，如果是为了点塔，综合考虑差点的还是会提交，毕竟多样化，有好有差才是正常的，而且尽量多点塔，少集中在好出货的数据集中疯狂提交；以上仅个人观点。

下面是我一些提交的过的因子，基本都是比较垃圾，margin都偏低，很少有特别高的，而且因为我不太会混塔，基本都是atom的，所以数据都比较差。 
> [!NOTE] [图片 OCR 识别内容]
> o
> IS Summary
> Period
> IS 
> 05
> Theme: EUR TOPCS16O0 Theme X2
> K Single Data Set Alpha
> Regular Alpha
> Pyramid theme: EURIDIIIMBALANCE X1
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.67
> 11.299
> 1.06
> 5.079
> 3.409
> 8.999600
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 0S
> Theme: EUR TOPCS16O0 Theme x2
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: EURIDTISENTIMENT X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.71
> 9.479
> 1.02
> 4.489
> 3.159
> 9.479600
  
> [!NOTE] [图片 OCR 识别内容]
> o
> IS Summary
> Period
> IS 
> 0S
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: USADIIINSIDERS X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.80
> 12.88%
> 1.16
> 5.359
> 3.449
> 8.309600
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS 
> 05
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: USAIDIIEARNINGS X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.60
> 18.279
> 1.22
> 10.57%
> 7.959
> 11.579600


在这里非常感谢nike大佬，没认识他之前，check因子，我都是在页面上一个个点开查看是否绿了能提交，谢谢大佬给的代码，让我简直就是原始人迈入了现代社会。

还有感谢cnhkmcp的作者，自从用了mcp，效率是大大提升了，虽然我在mcp上使用，无法像其他大佬一样能全自动产出ra，但是用了1个多月的curs，还是能在日常上帮助我更好的完成优化alpha。 
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 05
> Single Data Set Alpha
> Regular Alpha
> Pyramid theme: USAIDIIINSIDERS X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.87
> 9.089
> 1.67
> 10.01%
> 4.8896
> 22.059600
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> Os
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.68
> 3.389
> 1.05
> 4.92%
> 4.659
> 29.129600


总结就是多交atom，多点塔，因为个人能力问题，所以D0不考虑。

**顾问 WX84677 (Rank 69) 的解答与建议**:
惊了，代码小白也能极限卡位GM74！零基础靠一二三阶代码，每月硬怼20塔150因子，sharpe>1、fit>0.5的底线标准卡死，小众数据集灵活取舍不纠结margin，用atom堆出组合稳健性。从手动check到MCP提效，原始人变现代人太真实。这路子野但管用，学到了！


---

### 技术对话片段 37 (原帖: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享)
- **原帖链接**: [Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享.md
- **时间**: 1年前

**提问/主帖背景 (XM75236)**:
### 先赞后看,养成好习惯.

## 1 . 来时路

背景: 普通SqlBoy

成为顾问:2024年11月07日

VF变化: 0.5 → 0.77 → 0.99 → 0.99

Genius级别: 2024Q4 Expert, 2025Q1 GM

目前Combine: 2.11 select: 1.86

## 

## 2. 野蛮交

去年最后一个季度未能完全搞清Genius决胜规则,所以在计算出有机会交满220个达到GM基准线后,就每天4个,足100后每天交SA
此时是不太讲质量的,平均fit<1.5,但讲究如下两点

- 点金字塔,做好风格切换
- 小地区保证做超过10个

以上两点,已有vf0.99和Combine证明基本正确

> 做不出模板,做不出手工Alpha,你就保证风格多样(我就是)
> 小地区要么不做,要么多做

## 

## 3. 狂敛财

> 声明: 以下行为有一定风险,还需时间验证

拥有SA权限以后,在一个地区超过80个alpha以后,可以开启稳定挣base模式

SA要挣钱,基本要求是fit>5,prod<0.7,实测vf0.99的话,base至少45刀


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/13/2025
> Super:
> 49.18
> 5O
> Regular:
> 4.35
> Total:
> 53.53
> <<@
> SN _
> SN _
> p ppe
> 
> 8"
> 90
> 6 ^8'38:
> :
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> ADr
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar


记住, ***一条都不能破,且超标太高意义不大***

> 本来SA的fit都超过5了,你就这么有自信他的OS也能这么好?
> 既然如此,还往上飙意义在哪儿?几乎必然过拟合
> 从奖赏机制上也看得出来开,fit飚上去base打不满
> 但是prod降下来却能打满.但是很难,性价比又低

那么,怎么挣这个钱呢?

这里提供一个简单的思路.

收集select表达式20个.中性化也有10种,comb表达式来个20个,

一共就有了400个SA,全部跑完算self_cor即可.

随着持续提交,加上染色等,SA数量会远超400.

假设获得50个可交alpha,这时候怎么交呢?

***计算互相之间的self_cor,用最大团算法获取最长可交子集!!!***

## 4. 少年归

随着持续的挖掘和学习,有时候是知道哪些是正确的事情的
比如:

```
交fitness高的alpha
```

```
多做基本面的alpha
```

```
交有经济学意义的alpha
```

```
多交ATOM
```

```
多做SA
```

不是不想做啊,有时候真的难啊,感慨 **站着说话不腰疼** 啊.

做不到怎么办?

> **如果你不知道你做什么,那么你就想想你最讨厌什么,然后努力朝相反的方向奔跑**

坚持不做错误的事情,必将收获好的回报

我是WorldQuant中国区顾问,我 **庄严承诺** :

- 不混信号 !
- 不一直在同一个池子挖呀挖呀挖 !
- 不一个模板跑一年 !
- 不交自己都不相信的alpha !
- 不拒绝学习,不在比赛躺平,不忽略平台指引 !!!

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢毛老师无私分享！收获很大！


---

### 技术对话片段 38 (原帖: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **时间**: 1 year ago

**提问/主帖背景 (XM75236)**:
### 先赞后看,养成好习惯.

## 1 . 来时路

背景: 普通SqlBoy

成为顾问:2024年11月07日

VF变化: 0.5 → 0.77 → 0.99 → 0.99

Genius级别: 2024Q4 Expert, 2025Q1 GM

目前Combine: 2.11 select: 1.86

## 

## 2. 野蛮交

去年最后一个季度未能完全搞清Genius决胜规则,所以在计算出有机会交满220个达到GM基准线后,就每天4个,足100后每天交SA
此时是不太讲质量的,平均fit<1.5,但讲究如下两点

- 点金字塔,做好风格切换
- 小地区保证做超过10个

以上两点,已有vf0.99和Combine证明基本正确

> 做不出模板,做不出手工Alpha,你就保证风格多样(我就是)
> 小地区要么不做,要么多做

## 

## 3. 狂敛财

> 声明: 以下行为有一定风险,还需时间验证

拥有SA权限以后,在一个地区超过80个alpha以后,可以开启稳定挣base模式

SA要挣钱,基本要求是fit>5,prod<0.7,实测vf0.99的话,base至少45刀


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/13/2025
> Super:
> 49.18
> 5O
> Regular:
> 4.35
> Total:
> 53.53
> <<@
> SN _
> SN _
> p ppe
> 
> 8"
> 90
> 6 ^8'38:
> :
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> ADr
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar


记住, ***一条都不能破,且超标太高意义不大***

> 本来SA的fit都超过5了,你就这么有自信他的OS也能这么好?
> 既然如此,还往上飙意义在哪儿?几乎必然过拟合
> 从奖赏机制上也看得出来开,fit飚上去base打不满
> 但是prod降下来却能打满.但是很难,性价比又低

那么,怎么挣这个钱呢?

这里提供一个简单的思路.

收集select表达式20个.中性化也有10种,comb表达式来个20个,

一共就有了400个SA,全部跑完算self_cor即可.

随着持续提交,加上染色等,SA数量会远超400.

假设获得50个可交alpha,这时候怎么交呢?

***计算互相之间的self_cor,用最大团算法获取最长可交子集!!!***

## 4. 少年归

随着持续的挖掘和学习,有时候是知道哪些是正确的事情的
比如:

```
交fitness高的alpha
```

```
多做基本面的alpha
```

```
交有经济学意义的alpha
```

```
多交ATOM
```

```
多做SA
```

不是不想做啊,有时候真的难啊,感慨 **站着说话不腰疼** 啊.

做不到怎么办?

> **如果你不知道你做什么,那么你就想想你最讨厌什么,然后努力朝相反的方向奔跑**

坚持不做错误的事情,必将收获好的回报

我是WorldQuant中国区顾问,我 **庄严承诺** :

- 不混信号 !
- 不一直在同一个池子挖呀挖呀挖 !
- 不一个模板跑一年 !
- 不交自己都不相信的alpha !
- 不拒绝学习,不在比赛躺平,不忽略平台指引 !!!

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢毛老师无私分享！收获很大！


---

### 技术对话片段 39 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 组sa时如何选取高质量因子经验分享.md
- **时间**: 1年前

**提问/主帖背景 (ZS59763)**:
如题，在顾问群中发现很多刚开始组sa的顾问，不清楚select的具体选择方式。本帖给出对应规则以及一些例子。

对于expert及以上顾问来说，筛选因子的第一步是用自己的因子，还是组别人的。这个可以通过own和not(own）进行筛选。

第二步，降低选到的因子是过拟合的，或者混信号的概率，可以通过operator_count限制op数量，dataset_count限制数据集数量。

（第二点五步，如果想要选取特定category，特定color或者特定tag的因子，也可以进行筛选。研究小组中有大佬提出过利用color和tag对于因子进行分组，从而按组select的方式）

第三步，选低相关因子：从分散化角度来说,我们自然希望选出的因子相关性较低,这个可以从prod_correlation参数进行控制（selfcor也可以，但是这个是小于等于prod的，不够准确）

第四步，选老顾问/组合表现较好顾问的因子：平台提供了许多因子owner的相关数据参数，可以根据参数进行筛选，主要包括成为顾问的时长，顾问地区，该顾问的sharpe，fit等等

第五步，按照表现选因子。出于防止过拟合和刻意筛选的角度，我们不能够直接选高sharpe，高fit的好（not for sure）因子，平台提供了几个字段帮助我们筛选因子，包括turnover，truncation，long和short count等等，按照每个字段的范围进行分组选因子可以大幅降低重复筛选的概率，从而降低相关性。

前边几步是筛选的过程，对于筛选的权重我们也可以进行调整。

例如：我们可以按照turnover的大小进行赋权，对于turnover较高的因子赋予更小的 权重（在select表达式后加上/turnover即可），此步需要根据个人需求进行修改。

总结：

以上几步是我在筛选中的思考流程，更为详细具体的可以参考 [Selection Expression | WorldQuant BRAIN]([链接已屏蔽]) ，针对因子选择的流程需要发挥主观能动性，多想多试，才能选出最适合的因子。以下几个案例是我在研究小组发过的select表达式总结，可以基于这三类，对于参数与权重进行调整，从而实现更好的组合。在自动化跑sa的时候，也可以按照不同的“模块”进行组装（但要注意条件不能太苛刻，至少得选出10个因子才能开始跑。）

(own&& ( (turnover>0.03&&turnover<0.05)||(turnover<0.13&&turnover>0.1)||(turnover<0.17&&turnover>0.15) || ((turnover>0.17&&turnover<0.20)))&&(operator_count<18)&&prod_correlation<0.7)/(sigmoid(turnover)*sigmoid(prod_correlation)*log(long_count))

(
not(own)&& 
((turnover<0.12&&turnover>0.09)||(turnover<0.15&&turnover>0.13)||(turnover<0.19&&turnover>0.16))
&&(operator_count<8)
&&(prod_correlation<0.4&&prod_correlation>0.0)
&&(dataset_count<=2)
) 
/(turnover*tanh(turnover)*sigmoid(self_correlation)*sigmoid(prod_correlation)*abs(long_count-short_count))

(own&&(turnover<0.07||(turnover<0.25&&turnover>0.2)))/(sigmoid(turnover)*sigmoid(prod_correlation))

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢游戏王哥的分享，期待下一篇~


---

### 技术对话片段 40 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 组sa时如何选取高质量因子经验分享_32034293019671.md
- **时间**: 1年前

**提问/主帖背景 (ZS59763)**:
如题，在顾问群中发现很多刚开始组sa的顾问，不清楚select的具体选择方式。本帖给出对应规则以及一些例子。

对于expert及以上顾问来说，筛选因子的第一步是用自己的因子，还是组别人的。这个可以通过own和not(own）进行筛选。

第二步，降低选到的因子是过拟合的，或者混信号的概率，可以通过operator_count限制op数量，dataset_count限制数据集数量。

（第二点五步，如果想要选取特定category，特定color或者特定tag的因子，也可以进行筛选。研究小组中有大佬提出过利用color和tag对于因子进行分组，从而按组select的方式）

第三步，选低相关因子：从分散化角度来说,我们自然希望选出的因子相关性较低,这个可以从prod_correlation参数进行控制（selfcor也可以，但是这个是小于等于prod的，不够准确）

第四步，选老顾问/组合表现较好顾问的因子：平台提供了许多因子owner的相关数据参数，可以根据参数进行筛选，主要包括成为顾问的时长，顾问地区，该顾问的sharpe，fit等等

第五步，按照表现选因子。出于防止过拟合和刻意筛选的角度，我们不能够直接选高sharpe，高fit的好（not for sure）因子，平台提供了几个字段帮助我们筛选因子，包括turnover，truncation，long和short count等等，按照每个字段的范围进行分组选因子可以大幅降低重复筛选的概率，从而降低相关性。

前边几步是筛选的过程，对于筛选的权重我们也可以进行调整。

例如：我们可以按照turnover的大小进行赋权，对于turnover较高的因子赋予更小的 权重（在select表达式后加上/turnover即可），此步需要根据个人需求进行修改。

总结：

以上几步是我在筛选中的思考流程，更为详细具体的可以参考 [Selection Expression | WorldQuant BRAIN]([链接已屏蔽]) ，针对因子选择的流程需要发挥主观能动性，多想多试，才能选出最适合的因子。以下几个案例是我在研究小组发过的select表达式总结，可以基于这三类，对于参数与权重进行调整，从而实现更好的组合。在自动化跑sa的时候，也可以按照不同的“模块”进行组装（但要注意条件不能太苛刻，至少得选出10个因子才能开始跑。）

(own&& ( (turnover>0.03&&turnover<0.05)||(turnover<0.13&&turnover>0.1)||(turnover<0.17&&turnover>0.15) || ((turnover>0.17&&turnover<0.20)))&&(operator_count<18)&&prod_correlation<0.7)/(sigmoid(turnover)*sigmoid(prod_correlation)*log(long_count))

(
not(own)&& 
((turnover<0.12&&turnover>0.09)||(turnover<0.15&&turnover>0.13)||(turnover<0.19&&turnover>0.16))
&&(operator_count<8)
&&(prod_correlation<0.4&&prod_correlation>0.0)
&&(dataset_count<=2)
) 
/(turnover*tanh(turnover)*sigmoid(self_correlation)*sigmoid(prod_correlation)*abs(long_count-short_count))

(own&&(turnover<0.07||(turnover<0.25&&turnover>0.2)))/(sigmoid(turnover)*sigmoid(prod_correlation))

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢游戏王哥的分享，期待下一篇~


---

### 技术对话片段 41 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
- **原帖链接**: [Commented] 经验分享PPAC全球第三名回馈社区经验分享.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。

[图片 (图片已丢失)]

第一阶段：Alpha 构建（前五周）

比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。

我主要从以下三类渠道构建 Alpha：

1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。

2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。

3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。

构建期间，我也特别注意以下三方面的多样性控制：

- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区
- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等
- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性

此外，在筛选 Alpha 入库时，我建立了以下五步流程：

① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；
② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；
③ 计算并筛除自相关过高的表达式，提高组合独立性；
④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；
⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。

第二阶段：Alpha 筛选（第六周）

第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。

我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健

在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级

GPT 在筛选阶段的最大作用体现在两个方面：

1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。

2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。

此外，GPT 还协助完成以下操作：

- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；

- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；

- 避免过多同类中性化、universe 和数据来源重复的表达式；

- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。

我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。

结语：经验与建议

1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。

2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。

3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting
似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜

4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢大佬分享，祝后续 PPAC 常规赛，继续优胜！


---

### 技术对话片段 42 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.3
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 2.94
> Reached Grandmaster
> 0.5


第一阶段：Alpha 构建（前五周）

比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。

我主要从以下三类渠道构建 Alpha：

1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。

2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。

3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。

构建期间，我也特别注意以下三方面的多样性控制：

- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区
- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等
- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性

此外，在筛选 Alpha 入库时，我建立了以下五步流程：

① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；
② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；
③ 计算并筛除自相关过高的表达式，提高组合独立性；
④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；
⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。

第二阶段：Alpha 筛选（第六周）

第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。

我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健

在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级

GPT 在筛选阶段的最大作用体现在两个方面：

1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。

2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。

此外，GPT 还协助完成以下操作：

- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；

- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；

- 避免过多同类中性化、universe 和数据来源重复的表达式；

- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。

我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。

结语：经验与建议

1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。

2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。

3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting
似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜

4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

**顾问 WX84677 (Rank 69) 的解答与建议**:
感谢大佬分享，祝后续 PPAC 常规赛，继续优胜！


---

### 技术对话片段 43 (原帖: 这个因子到底能不能交？（下） 【传奇耐打王系列一】)
- **原帖链接**: [Commented] 这个因子到底能不能交下 【传奇耐打王系列一】.md
- **时间**: 8个月前

**提问/主帖背景 (FX25214)**:
上一篇在这： [../顾问 RM49262 (Rank 30)/[Commented] 这个因子到底能不能交上 【传奇耐打王系列一】.md-这个因子到底能不能交-上-传奇耐打王系列一](../顾问 RM49262 (Rank 30)/[Commented] 这个因子到底能不能交上 【传奇耐打王系列一】.md)

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

**顾问 WX84677 (Rank 69) 的解答与建议**:
总结整理的非常棒，还有这么多案例，太优秀啦！感恩无私分享！


---

### 技术对话片段 44 (原帖: 这个因子到底能不能交？（下） 【传奇耐打王系列一】)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 这个因子到底能不能交下 【传奇耐打王系列一】_35459650154519.md
- **时间**: 8 months ago

**提问/主帖背景 (FX25214)**:
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

**顾问 WX84677 (Rank 69) 的解答与建议**:
总结整理的非常棒，还有这么多案例，太优秀啦！感恩无私分享！


---
