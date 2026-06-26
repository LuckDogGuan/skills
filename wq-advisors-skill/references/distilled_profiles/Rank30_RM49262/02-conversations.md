# 顾问 RM49262 (Rank 30) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 RM49262 (Rank 30) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: 0帧起手的字段构建【传奇耐打王系列三】经验分享)
- **原帖链接**: [Commented] 0帧起手的字段构建【传奇耐打王系列三】经验分享.md
- **时间**: 24天前

**提问/主帖背景 (FX25214)**:
继上文讲了模版是怎么来的，本文我们就来思考这个0阶的字段，需要我们进行怎么样的思考呢？

首先，我一直都对用户阶段的课程的录播中 weijie 老师的一句话印象十分深刻：

Liabilities 单独回测没有信号，为什么 libilities / assets 就有信号了呢？

因为大公司的负债天然的比小公司的多，如果直接对比公司负债的差异，那很多小公司实际是会被直接忽略的。但是我们用公司资产作为分母，就把这个公司规模对负债的影响给消除了，这个比率使得一整个组合字段具有了可比性。

注意，这个可比性是非常重要的。我看到一篇非常好的文章介绍爽字段是怎么构建的，但我们一定要知道这么构建的内涵是什么。比如刚刚举的比率的例子，就是去除公司量纲对我们想要对比的对象的天然影响。但比率能做的事情可完全不止这些。现在让我以这个为基础带你们一起思考一下。

- 既然有公司的负债可以被考虑，那是不是公司的利润也可以被考虑？

公司利润/公司资产，这样的新比率就应运而生了。

那我相信聪明的人已经开始举一反三，那我还可以考虑的点有很多，围绕公司的各类指标我都来一遍，我相信这完全没问题。更有聪明的人想到，分子可以变，分母也可以变，我要想办法去除量纲问题，我用公司的市值行不行呢？公司的人数行不行呢？基于这些，往往已经产生了大量的字段构建了。

- 那我们想做出差异化的东西，我们就应该学会寻找共性和个性。刚刚的第1点的共性是什么呢？我想是很明显的 a / b 的形式。那能不能在这个基础上稍微做一点衍生？(a + c) / b 可以吗？(a - c) / b 可以吗？比如我是（（公司利润 - 公司负债）/公司资产），这是不是又产生了一个新的构造呢？那分子变了，分母是不是也可以变？(a + c) / (b + d)，这样的可以吗？

答案是肯定的。

- 现在我们再针对这个字段本身做一个深度的思考。假设我就要 公司利润/公司资产 这个形式呢？OK没问题。公司利润是什么？公司利润是公司收入减去公司成本。这个和第2点不同的地方在于。我不是由 a 变成 a + b，而是由 b - c 来刻画 a。目标字段不变，我通过另外一种方式找到他。这是最直接的。
- 那我们有没有思考，什么可以反映公司利润？我们能直接的做出来，那能不能间接的窥探到呢？


> [!NOTE] [图片 OCR 识别内容]
> T CTHLLTr 5^TULJLTSCLo
> ?U
> ImmlA
> UTTN
> TCATINT=胃7T2N5U9T
> 工TCLLICLI LUITAI II4NI BMNDLTU
> USTNNEu
> Tl7T
> aW Lp yA?1切 @兀t止)L%
> J71NOTNes'
> ITaS
> URL
> TTN
> IITe
> L
> _
> [UnaSU3 )
> TT7Si SUlt丕
> To+ ~
> ANM
> muy
> 444.4SNITTT TUiTI!895n
> IAt=U


这里我用的是网页版腾讯元宝，绝对免费绝对方便绝对好复刻实操。

元宝就告诉我负面的新闻或者情绪大概率领先于基本面的下调。

我的第一反应是什么？赶紧去 news 或者 sentiment 里找对应的字段配合 if_else 做分子，分母不变。新的构建又出现了。

- 我希望大家多多关注点塔王，点塔王利用大模型将很多字段的相似字段进行了总结。这里有什么作用呢？既然有基本面数据，那分析师数据是否可以做相应的替换？

综上所述，我们已经从一个最简单的 a / b，走向了千千万万种不同的构造了。可最简单的完全不止 a / b，你知道的，在那篇优秀的文章中已经列出了非常多最简单的构造了。

你真的还会害怕出不了因子吗？我的顾问朋友们？

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢牛牛的分享  这波字段构建的小技巧学到了！

这个月刚好要跑IND了 准备测试一下

=============================================================================


---

### 技术对话片段 2 (原帖: 0帧起手的字段构建【传奇耐打王系列三】经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 0帧起手的字段构建【传奇耐打王系列三】经验分享_40760257415959.md
- **时间**: 25天前

**提问/主帖背景 (FX25214)**:
继上文讲了模版是怎么来的，本文我们就来思考这个0阶的字段，需要我们进行怎么样的思考呢？

首先，我一直都对用户阶段的课程的录播中 weijie 老师的一句话印象十分深刻：

Liabilities 单独回测没有信号，为什么 libilities / assets 就有信号了呢？

因为大公司的负债天然的比小公司的多，如果直接对比公司负债的差异，那很多小公司实际是会被直接忽略的。但是我们用公司资产作为分母，就把这个公司规模对负债的影响给消除了，这个比率使得一整个组合字段具有了可比性。

注意，这个可比性是非常重要的。我看到一篇非常好的文章介绍爽字段是怎么构建的，但我们一定要知道这么构建的内涵是什么。比如刚刚举的比率的例子，就是去除公司量纲对我们想要对比的对象的天然影响。但比率能做的事情可完全不止这些。现在让我以这个为基础带你们一起思考一下。

- 既然有公司的负债可以被考虑，那是不是公司的利润也可以被考虑？

公司利润/公司资产，这样的新比率就应运而生了。

那我相信聪明的人已经开始举一反三，那我还可以考虑的点有很多，围绕公司的各类指标我都来一遍，我相信这完全没问题。更有聪明的人想到，分子可以变，分母也可以变，我要想办法去除量纲问题，我用公司的市值行不行呢？公司的人数行不行呢？基于这些，往往已经产生了大量的字段构建了。

- 那我们想做出差异化的东西，我们就应该学会寻找共性和个性。刚刚的第1点的共性是什么呢？我想是很明显的 a / b 的形式。那能不能在这个基础上稍微做一点衍生？(a + c) / b 可以吗？(a - c) / b 可以吗？比如我是（（公司利润 - 公司负债）/公司资产），这是不是又产生了一个新的构造呢？那分子变了，分母是不是也可以变？(a + c) / (b + d)，这样的可以吗？

答案是肯定的。

- 现在我们再针对这个字段本身做一个深度的思考。假设我就要 公司利润/公司资产 这个形式呢？OK没问题。公司利润是什么？公司利润是公司收入减去公司成本。这个和第2点不同的地方在于。我不是由 a 变成 a + b，而是由 b - c 来刻画 a。目标字段不变，我通过另外一种方式找到他。这是最直接的。
- 那我们有没有思考，什么可以反映公司利润？我们能直接的做出来，那能不能间接的窥探到呢？


> [!NOTE] [图片 OCR 识别内容]
> T CTHLLTr 5^TULJLTSCLo
> ?U
> ImmlA
> UTTN
> TCATINT=胃7T2N5U9T
> 工TCLLICLI LUITAI II4NI BMNDLTU
> USTNNEu
> Tl7T
> aW Lp yA?1切 @兀t止)L%
> J71NOTNes'
> ITaS
> URL
> TTN
> IITe
> L
> _
> [UnaSU3 )
> TT7Si SUlt丕
> To+ ~
> ANM
> muy
> 444.4SNITTT TUiTI!895n
> IAt=U


这里我用的是网页版腾讯元宝，绝对免费绝对方便绝对好复刻实操。

元宝就告诉我负面的新闻或者情绪大概率领先于基本面的下调。

我的第一反应是什么？赶紧去 news 或者 sentiment 里找对应的字段配合 if_else 做分子，分母不变。新的构建又出现了。

- 我希望大家多多关注点塔王，点塔王利用大模型将很多字段的相似字段进行了总结。这里有什么作用呢？既然有基本面数据，那分析师数据是否可以做相应的替换？

综上所述，我们已经从一个最简单的 a / b，走向了千千万万种不同的构造了。可最简单的完全不止 a / b，你知道的，在那篇优秀的文章中已经列出了非常多最简单的构造了。

你真的还会害怕出不了因子吗？我的顾问朋友们？

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢牛牛的分享  这波字段构建的小技巧学到了！

这个月刚好要跑IND了 准备测试一下

=============================================================================


---

### 技术对话片段 3 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 16815刀季度奖经验分享-小虎经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (SD17531)**:
大家好，我是SD7531，顾问朋友们都很nice，一般喊我小虎哥。

我从 2024 年 12 月 13 日开始提交顾问 Alpha，近三次定级都很幸运地保住了 GM。我本科专业是公共管理，代码一般是现学现用。 我的背景在顾问里也算和量化最不相关的之一，不过反过来说，我这样的背景都能做到 GM，相信绝大多数顾问朋友，只要愿意付出时间和精力，都能冲刺 GM。
下面附上我的季度奖和一路熬过来的每日 base，希望能给大家一些鼓励：只要不放弃，收益终究会一柱擎天。
 
> [!NOTE] [图片 OCR 识别内容]
> Other Payment
> For attending the offline meetup at BJISHIGZin Dec 2024
> 02/07/2025
> US$137.00
> 202501 Payment
> 05/22/2025
> 05$112.73
> Value Factor Improvement Program Rewards
> 06/25/2025
> 0S$200.00
> Referral
> 07/13/2025
> 0S$200.00
> 2025 Q2 Payment
> 08/17/2025
> 0S$322.73
> Research Award August
> 09/01/2025
> 05$28.00
> Research Award
> 09/11/2025
> US$14.00
> Research Award
> 09/25/2025
> 0S$28.00
> 2025 Q3 Payment
> 11/24/2025
> US$8,065.01
> Referral
> 12/26/2025
> US$200.00
> Power Pool Alphas Monthly Competition December 2025
> ASI D1
> 01/01/2026
> US$500.00
> 2025Q4 Payment
> 02/21/2026
> US$16,815.45
> 11/18/2024
> Total
> 05$26,622.92
> 03/10/2026
  
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/20/2026
> Regular:
> 57.93
> Super:
> 55.58
> Total:
> 113.50999999999999
> 75
> 50
> 25
> Mar
> May
> May
> Mar
 
关于季度奖，顾问 YX23928 (Rank 8)和
顾问 SJ65808 (Rank 20)两位大佬都有分享。帖子分别如下： [../顾问 MS51256 (Rank 28)/[Commented] 一个非科班选手的量化打怪升级路季度奖突破万刀必读.md](../顾问 MS51256 (Rank 28)/[Commented] 一个非科班选手的量化打怪升级路季度奖突破万刀必读.md)  

 [../顾问 MG88592 (Rank 38)/[Commented] 2025年度收入回顾经验分享.md](../顾问 MG88592 (Rank 38)/[Commented] 2025年度收入回顾经验分享.md)  

两位大佬讲的很详细了，我听了也获益良多。

先分享一下我自己的数据：
第一次季度奖，VF分别是0.70-0.85-0.82，weight增加值大概是9，对应的季度奖是8065刀。
第二次季度奖，VF分别是0.87-0.90-0.98，weight增加值大概是15，对应的季度奖是16815刀。

从这两次季度奖的情况来看，我个人认为季度奖的核心影响因素是该季度第三个月的 VF 值 —— 这个 VF 值恰好核算的是当季所有提交 Alpha 的质量。和其他顾问交流后也能明显感受到，最后一个月 VF 低于 0.9，大多只能拿到保底季度奖。

那么如何获取更高的季度奖， 其实也可以转化为如何获得更高的VF。我来分享一下我自己的提交数据，希望对大家有所启发。我将所有历史提交的RA和SA的数据下载下来，让AI帮忙绘制了月度Alpha平均指标和三月滚动的alpha平均指标（correlation）的图片。
 
> [!NOTE] [图片 OCR 识别内容]
> Monthly Combo Bars
> Lines (Baseline-Relative) (2025-03 to 2025-12)
> 文
> 111
> 65
> 114
> 85
> 30
> 20
> 10
> {}:$
> 吕@员:岛芒思
> @3&8@3
> 恩
> 总@@寰@
> &38838@
> 38号
> 李e38
> }a:黑
> 88g8品&
> 8军$8}&
> 38 $@ $寺
> 8
> O 寸
> C C
> R
> O I R
> i
> @
>  「
> &
> M 
> Se
> 寸卉
> O M
> S83
> CC
> 385
> U m
> m m
> SSaw
> mni
> SRo
> 10
> 20
> Metrics (bars & lines)
> sharpe
> margin
> prodcorrelation
> 30
> fitness
> turnover
> selfCorrelation
> returns
> 8
> 2025-03
> 2025-04
> 2025-05
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
> 2025-C
 
 
> [!NOTE] [图片 OCR 识别内容]
> Rolling 3M Combo Bars + Lines (Baseline-Relative) (2025-06 to 2025-12)
> 30
> 20
> 10
> & 守835苎%
> 总v8怠畏莴舄
> `:
> 8@@S$
> 莴营s~
> 总&盒窝@密忿
> 8品 @@%@品
> @$ &
> 品
> @R &
> @
> 88Rg孚8 &
> @%38w& @
> SO
> 8
> R~ &
> R
>  e只~
> M M
> S9a m
> qm
> 9896
> SR Sw
> mm
> 58
> OUm
> 10
> -20
> Metrics (bars
> lines)
> Sharpe
> margin
> prodCorrelation
> fitness
> turnoVer
> selfCorrelation
> 30
> returns
> @%5
> 9e6
> 1品
> 2025-03
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
 我个人的 VF 近几个月呈缓慢增长趋势，波动幅度并不大。VF 的计算公式在论坛中就能找到。从我的数据来看，VF受影响确实是多个维度综合产生的，提交数量、prod_correlation、其他顾问的提交质量等都会对VF产生影响。可以从图片中看到我每个月的数据情况，大家有需要的话可以根据我的VF波动去评估该月份涨跌的主要原因。值得一提的是，我 10-12 月每月提交的因子数量相差不大，且呈 85-91-92 的递增趋势，prodCorrelation 表现也比 7-9 月好不少；而 7-9 月的提交量则是 114-111-71 的骤降趋势，这或许是我第四季度 VF 优于第三季度的原因之一。

然后打铁还需自身硬，老生常谈的diversity也是必须安排上的。我的策略，主要是在同一个region多做不同类型的因子，但是不做太多不同的region。
 
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-04, October 1st, 2025
> December 31st, 2025
> Category
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
> 16
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> MaCro
> Model
> 15
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media
 因子方面，我优先做多操作符少的 Atom，同时尽量使用不同的操作符来保证多样性。
 
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st, 2025
> December 31st, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 4.19
> 167
> 1.39
> Fields used
> Community activity
> Max simulation streak
> 223
> 44.7
> 387
 
非常建议大家用代码分析自己每月的提交数据，我把 AI 写的代码附在文末，抛砖引玉。大家可以结合 Region、Delay、月度、三月周期做更深度的分析，再和自己的历史 VF 数据对比，相信会有不少收获。

最后，一路走来，我感觉我的运气还是非常不错的，运气最好的地方就是认识了这么多优秀的顾问朋友。感谢课代表，游戏王，橘子姐，毛老师，MG哥，老虎哥，大角羊，文姐，孙哥，强哥（排名不分先后），太多需要感谢的，就不一一列举了。希望后面能跟大家继续一起进步。

大佬们，请继续教我本领！！！

代码：

import os

import json

import math

import logging

from pathlib import Path

from datetime import datetime, timezone

from typing import Any, Dict, List, Optional, Tuple

import requests

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

LOG_NAME = Path(__file__).stem

BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR / "logs"

OUTPUT_DIR = BASE_DIR / "outputs"

CHART_DIR = OUTPUT_DIR / "charts"

def _ensure_dirs() -> None:

LOG_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CHART_DIR.mkdir(parents=True, exist_ok=True)

def _setup_logger() -> logging.Logger:

_ensure_dirs()

logger = logging.getLogger(LOG_NAME)

if not logger.handlers:

logger.setLevel(logging.INFO)

fh = logging.FileHandler(LOG_DIR / f"{LOG_NAME}.log", encoding="utf-8")

fmt = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s")

fh.setFormatter(fmt)

logger.addHandler(fh)

return logger

logger = _setup_logger()

def print_exec_timestamp() -> None:

ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[EXECUTION START] {ts}")

logger.info(f"Execution started at {ts}")

def get_session() -> requests.Session:

try:

# 优先使用现成的已登录会话

from machine_lib import s as session  # type: ignore

if isinstance(session, requests.Session):

logger.info("Using session 's' from machine_lib")

return session

except Exception:

pass

try:

from machine_lib import login  # type: ignore

logger.info("Creating session via machine_lib.login()")

session = login()

if isinstance(session, requests.Session):

return session

except Exception as e:

logger.info(f"machine_lib.login() not available or failed: {e}")

logger.info("Fallback to anonymous requests.Session (may not work without auth)")

return requests.Session()

def _iso_with_tz(dt: datetime) -> str:

if dt.tzinfo is None:

dt = dt.replace(tzinfo=timezone.utc)

return dt.astimezone().isoformat(timespec="seconds")

def fetch_alphas_since(

session: requests.Session,

start_submitted_dt: datetime,

limit: int = 100,

) -> List[Dict[str, Any]]:

logger.info(f"Fetching alphas since submission time: {start_submitted_dt.isoformat()}")

results: List[Dict[str, Any]] = []

base = " [[链接已屏蔽]) "

start_str = _iso_with_tz(start_submitted_dt)

offset = 0

while True:

url = (

f"{base}?limit={limit}&offset={offset}"

f"&dateSubmitted%3E={requests.utils.quote(start_str, safe='')}"

f"&hidden=false"

f"&status!=UNSUBMITTED%1FIS-FAIL"

f"&order=-dateSubmitted"

)

try:

resp = session.get(url)

if resp.status_code != 200:

logger.info(f"Fetch error: status={resp.status_code}, text={resp.text[:300]}")

break

data = resp.json()

page = data.get("results", [])

results.extend(page)

count = int(data.get("count", 0))

logger.info(f"Fetched {len(page)} items at offset {offset}, total so far {len(results)}/{count}")

if offset + len(page) >= count or len(page) < limit:

break

offset += limit

except Exception as e:

logger.info(f"Exception during fetch: {e}")

break

logger.info(f"Total fetched records: {len(results)}")

return results

def _safe_get(d: Dict[str, Any], *keys: str, default: Any = None) -> Any:

cur: Any = d

for k in keys:

if not isinstance(cur, dict) or k not in cur:

return default

cur = cur[k]

return cur

def normalize_alpha_record(rec: Dict[str, Any]) -> Dict[str, Any]:

is_data = rec.get("is", {}) or {}

risk_neu = is_data.get("riskNeutralized", {}) or rec.get("riskNeutralized", {}) or {}

settings = rec.get("settings", {}) or {}

norm = {

"id": rec.get("id"),

"type": rec.get("type"),

"name": rec.get("name"),

"dateCreated": rec.get("dateCreated"),

"dateSubmitted": rec.get("dateSubmitted"),

"settings": {

"region": settings.get("region"),

"universe": settings.get("universe"),

"delay": settings.get("delay"),

"decay": settings.get("decay"),

"neutralization": settings.get("neutralization"),

"truncation": settings.get("truncation"),

"pasteurization": settings.get("pasteurization"),

"unitHandling": settings.get("unitHandling"),

"visualization": settings.get("visualization"),

},

"is": {

"fitness": is_data.get("fitness"),

"longCount": is_data.get("longCount"),

"shortCount": is_data.get("shortCount"),

"turnover": is_data.get("turnover"),

"returns": is_data.get("returns"),

"drawdown": is_data.get("drawdown"),

"margin": is_data.get("margin"),

"sharpe": is_data.get("sharpe"),

"prodCorrelation": is_data.get("prodCorrelation"),

"selfCorrelation": is_data.get("selfCorrelation"),

},

"riskNeutralized": {

"pnl": risk_neu.get("pnl"),

"bookSize": risk_neu.get("bookSize"),

"longCount": risk_neu.get("longCount"),

"shortCount": risk_neu.get("shortCount"),

"turnover": risk_neu.get("turnover"),

"returns": risk_neu.get("returns"),

"drawdown": risk_neu.get("drawdown"),

"margin": risk_neu.get("margin"),

"fitness": risk_neu.get("fitness"),

"sharpe": risk_neu.get("sharpe"),

},

"checks": rec.get("is", {}).get("checks", []) or rec.get("checks", []),

}

if "regular" in rec and isinstance(rec["regular"], dict):

norm["regular"] = {"code": rec["regular"].get("code")}

if "combo" in rec:

norm["combo"] = rec.get("combo")

if "selection" in rec:

norm["selection"] = rec.get("selection")

return norm

def save_json(data: List[Dict[str, Any]], path: Path) -> None:

_ensure_dirs()

with path.open("w", encoding="utf-8") as f:

json.dump(data, f, ensure_ascii=False, indent=2)

logger.info(f"Saved JSON data to {path}")

def load_json(path: Path) -> List[Dict[str, Any]]:

with path.open("r", encoding="utf-8") as f:

data = json.load(f)

logger.info(f"Loaded JSON data from {path}")

return data

def _parse_month(s: Optional[str]) -> Optional[str]:

if not s:

return None

try:

dt = datetime.fromisoformat(s.replace("Z", "+00:00"))

return dt.strftime("%Y-%m")

except Exception:

return None

def _to_frame(records: List[Dict[str, Any]]) -> pd.DataFrame:

rows = []

for r in records:

isd = r.get("is", {}) or {}

st = r.get("settings", {}) or {}

rows.append(

{

"id": r.get("id"),

"type": r.get("type"),

"name": r.get("name"),

"dateSubmitted": r.get("dateSubmitted"),

"submitMonth": _parse_month(r.get("dateSubmitted")),

"region": st.get("region"),

"delay": st.get("delay"),

"turnover": isd.get("turnover"),

"fitness": isd.get("fitness"),

"returns": isd.get("returns"),

"drawdown": isd.get("drawdown"),

"margin": isd.get("margin"),

"sharpe": isd.get("sharpe"),

"prodCorrelation": isd.get("prodCorrelation"),

"selfCorrelation": isd.get("selfCorrelation"),

}

)

df = pd.DataFrame(rows)

return df

def compute_monthly_stats(records: List[Dict[str, Any]]) -> pd.DataFrame:

df = _to_frame(records)

df = df.dropna(subset=["submitMonth", "region", "delay"])

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

agg_map = {m: "mean" for m in metrics}

grp = df.groupby(["submitMonth", "region", "delay"], dropna=False)

stats = grp.agg(agg_map).reset_index()

cnt_total = grp.size().reset_index(name="count")

cnt_regular = grp.apply(lambda g: (g["type"] == "REGULAR").sum()).reset_index(name="count_regular")

cnt_super = grp.apply(lambda g: (g["type"] == "SUPER").sum()).reset_index(name="count_super")

out = stats.merge(cnt_total, on=["submitMonth", "region", "delay"], how="left")

out = out.merge(cnt_regular, on=["submitMonth", "region", "delay"], how="left")

out = out.merge(cnt_super, on=["submitMonth", "region", "delay"], how="left")

return out

def export_table(df: pd.DataFrame, name: str) -> Tuple[Path, Path]:

_ensure_dirs()

csv_path = OUTPUT_DIR / f"{name}.csv"

xlsx_path = OUTPUT_DIR / f"{name}.xlsx"

try:

df.to_csv(csv_path, index=False, encoding="utf-8-sig")

with pd.ExcelWriter(xlsx_path, engine="xlsxwriter") as writer:

df.to_excel(writer, index=False, sheet_name="data")

logger.info(f"Exported tables: {csv_path.name}, {xlsx_path.name}")

return csv_path, xlsx_path

except PermissionError:

ts = datetime.now().strftime("%Y%m%d_%H%M%S")

csv_alt = OUTPUT_DIR / f"{name}_{ts}.csv"

xlsx_alt = OUTPUT_DIR / f"{name}_{ts}.xlsx"

df.to_csv(csv_alt, index=False, encoding="utf-8-sig")

with pd.ExcelWriter(xlsx_alt, engine="xlsxwriter") as writer:

df.to_excel(writer, index=False, sheet_name="data")

logger.info(f"Target locked, exported tables to: {csv_alt.name}, {xlsx_alt.name}")

return csv_alt, xlsx_alt

def _line_trend(df: pd.DataFrame, metric: str, title: str, fname: str) -> None:

tmp = df.groupby("submitMonth")[metric].mean().reset_index()

tmp = tmp.sort_values("submitMonth")

plt.figure(figsize=(10, 4))

sns.lineplot(data=tmp, x="submitMonth", y=metric, marker="o")

plt.title(title)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

out_path = CHART_DIR / fname

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def _heatmap_region_delay(df: pd.DataFrame, metric: str, title: str, fname: str) -> None:

tmp = df.groupby(["region", "delay"])[metric].mean().reset_index()

pivot = tmp.pivot(index="region", columns="delay", values=metric)

plt.figure(figsize=(10, 6))

sns.heatmap(pivot, annot=True, fmt=".3f", cmap="Blues")

plt.title(title)

plt.tight_layout()

out_path = CHART_DIR / fname

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def _bar_latest_month(df: pd.DataFrame, metric: str, title: str, fname: str) -> None:

if "submitMonth" not in df.columns or df["submitMonth"].dropna().empty:

return

latest = sorted(m for m in df["submitMonth"].dropna().unique())[-1]

tmp = df[df["submitMonth"] == latest].groupby(["region", "delay"])[metric].mean().reset_index()

plt.figure(figsize=(12, 5))

sns.barplot(data=tmp, x="region", y=metric, hue="delay")

plt.title(f"{title} (Latest: {latest})")

plt.tight_layout()

out_path = CHART_DIR / fname

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_monthly_charts(df: pd.DataFrame) -> None:

metrics = [

("sharpe", "Average Sharpe Ratio"),

("fitness", "Average Fitness"),

("returns", "Average Return"),

("drawdown", "Average Drawdown"),

("margin", "Average Margin"),

("turnover", "Average Turnover"),

("prodCorrelation", "Average Prod Correlation"),

("selfCorrelation", "Average Self Correlation"),

]

for col, title in metrics:

_line_trend(df, col, f"{title} - Monthly Trend", f"monthly_trend_{col}.png")

_heatmap_region_delay(df, col, f"{title} by Region x Delay", f"heatmap_region_delay_{col}.png")

_bar_latest_month(df, col, f"{title} Region/Delay", f"bar_latest_{col}.png")

def compute_custom_periods(

records: List[Dict[str, Any]],

periods: List[Tuple[str, datetime, datetime]],

) -> pd.DataFrame:

df = _to_frame(records)

df = df.dropna(subset=["dateSubmitted", "region", "delay"])

def within(dts: str, start: datetime, end: datetime) -> bool:

try:

dt = datetime.fromisoformat(dts.replace("Z", "+00:00"))

return start <= dt <= end

except Exception:

return False

rows = []

for label, start, end in periods:

mask = df["dateSubmitted"].apply(lambda s: within(s, start, end))

sub = df[mask].copy()

if sub.empty:

continue

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

grp = sub.groupby(["region", "delay"], dropna=False)

stats = grp[metrics].mean().reset_index()

stats.insert(0, "period", label)

cnt_total = grp.size().reset_index(name="count")

cnt_regular = grp.apply(lambda g: (g["type"] == "REGULAR").sum()).reset_index(name="count_regular")

cnt_super = grp.apply(lambda g: (g["type"] == "SUPER").sum()).reset_index(name="count_super")

st = stats.merge(cnt_total, on=["region", "delay"], how="left")

st = st.merge(cnt_regular, on=["region", "delay"], how="left")

st = st.merge(cnt_super, on=["region", "delay"], how="left")

rows.append(st)

if not rows:

return pd.DataFrame(

columns=[

"period", "region", "delay",

"sharpe", "fitness", "returns", "drawdown", "margin", "prodCorrelation", "selfCorrelation",

"count", "count_regular", "count_super",

]

)

return pd.concat(rows, ignore_index=True)

def generate_custom_period_charts(df: pd.DataFrame, period_label: str) -> None:

metrics = [

("sharpe", "Average Sharpe Ratio"),

("fitness", "Average Fitness"),

("returns", "Average Return"),

("drawdown", "Average Drawdown"),

("margin", "Average Margin"),

("turnover", "Average Turnover"),

("prodCorrelation", "Average Prod Correlation"),

("selfCorrelation", "Average Self Correlation"),

]

for col, title in metrics:

tmp = df.groupby("region")[col].mean().reset_index()

plt.figure(figsize=(10, 4))

sns.barplot(data=tmp, x="region", y=col)

plt.title(f"{title} by Region - {period_label}")

plt.tight_layout()

out_path = CHART_DIR / f"{period_label}_region_{col}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

plt.figure(figsize=(10, 5))

sns.boxplot(data=df, x="delay", y=col)

plt.title(f"{title} Distribution by Delay - {period_label}")

plt.tight_layout()

out_path = CHART_DIR / f"{period_label}_delay_box_{col}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def _scale_for_display(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:

scaled = df.copy()

if "returns" in cols and "returns" in scaled.columns:

scaled["returns"] = scaled["returns"] * 100.0

if "turnover" in cols and "turnover" in scaled.columns:

scaled["turnover"] = scaled["turnover"] * 100.0

if "margin" in cols and "margin" in scaled.columns:

scaled["margin"] = scaled["margin"] * 10000.0

if "prodCorrelation" in cols and "prodCorrelation" in scaled.columns:

scaled["prodCorrelation"] = scaled["prodCorrelation"] * 10.0

if "selfCorrelation" in cols and "selfCorrelation" in scaled.columns:

scaled["selfCorrelation"] = scaled["selfCorrelation"] * 10.0

return scaled

def _barline_unified(months: List[str], values: List[float], title: str, y_label: str, out_name: str, y_lim: Tuple[float, float], counts: Optional[List[float]] = None) -> None:

x = np.arange(len(months))

plt.figure(figsize=(12, 5))

bars = plt.bar(x, values, color="#4c72b0", alpha=0.6)

plt.plot(x, values, color="#c44e52", marker="o", linewidth=2)

plt.xticks(ticks=x, labels=months, rotation=45, ha="right")

plt.ylabel(y_label)

plt.title(title)

plt.ylim(y_lim)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.03

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for rect, v in zip(bars, values):

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{v:.2f}", ha="center", va="center", fontsize=8, rotation=90)

if counts is not None and len(counts) == len(x):

y_top = y_lim[1] - (y_lim[1] - y_lim[0]) * 0.02

for xi, c in zip(x, counts):

plt.text(xi, y_top, f"n={int(c)}", ha="center", va="top", fontsize=8, color="#333333")

plt.tight_layout()

out_path = CHART_DIR / out_name

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_monthly_barline_unified(monthly_df: pd.DataFrame, year: int = 2025, start_month: int = 6, end_month: int = 12) -> None:

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy()

tmp = tmp.sort_values("submitMonth")

tmp_scaled = _scale_for_display(tmp, metrics)

y_max = 0.0

for c in metrics:

if c in tmp_scaled.columns:

vals = tmp_scaled[c].dropna().values

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

title_map = {

"sharpe": "Average Sharpe (Monthly)",

"fitness": "Average Fitness (Monthly)",

"returns": "Average Return % (Monthly)",

"drawdown": "Average Drawdown (Monthly)",

"margin": "Average Margin ×1e4 (Monthly)",

"turnover": "Average Turnover % (Monthly)",

"prodCorrelation": "Average Prod Correlation (Monthly)",

"selfCorrelation": "Average Self Correlation (Monthly)",

}

y_label_map = {

"returns": "%",

"turnover": "%",

"margin": "×1e4",

}

# 月度 alpha 数量（按 submitMonth 聚合求和），用于叠加显示

cnt_series = monthly_df.groupby("submitMonth")["count"].sum().reindex(tmp_scaled["submitMonth"]).fillna(0)

cnt_list = cnt_series.tolist()

for c in metrics:

if c not in tmp_scaled.columns:

continue

vals = tmp_scaled[c].tolist()

_barline_unified(

months=[m for m in tmp_scaled["submitMonth"]],

values=vals,

title=title_map.get(c, c),

y_label=y_label_map.get(c, ""),

out_name=f"barline_monthly_{c}_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=y_lim,

counts=cnt_list,

)

# 额外输出 alpha 数量（月度总数，求和）

cnt = monthly_df.groupby("submitMonth")["count"].sum().reindex(months).fillna(0)

if not cnt.empty:

cnt_vals = cnt.tolist()

cnt_ymax = max(abs(v) for v in cnt_vals) if cnt_vals else 1.0

if cnt_ymax == 0:

cnt_ymax = 1.0

cnt_ylim = (0, cnt_ymax * 1.15)

_barline_unified(

months=months,

values=cnt_vals,

title="Alpha Count (Monthly)",

y_label="count",

out_name=f"barline_monthly_count_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=cnt_ylim,

)

def generate_rolling3_barline_unified(monthly_df: pd.DataFrame, year: int = 2025, start_month: int = 6, end_month: int = 12) -> None:

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp_scaled = _scale_for_display(tmp, metrics)

seq = months

tmp_scaled = tmp_scaled.set_index("submitMonth").reindex(seq)

roll = tmp_scaled[metrics].rolling(window=3, min_periods=1).mean().reset_index()

y_max = 0.0

for c in metrics:

vals = roll[c].dropna().values

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

title_map = {

"sharpe": "Average Sharpe (Rolling 3M)",

"fitness": "Average Fitness (Rolling 3M)",

"returns": "Average Return % (Rolling 3M)",

"drawdown": "Average Drawdown (Rolling 3M)",

"margin": "Average Margin ×1e4 (Rolling 3M)",

"turnover": "Average Turnover % (Rolling 3M)",

"prodCorrelation": "Average Prod Correlation (Rolling 3M)",

"selfCorrelation": "Average Self Correlation (Rolling 3M)",

}

y_label_map = {

"returns": "%",

"turnover": "%",

"margin": "×1e4",

}

for c in metrics:

vals = roll[c].tolist()

_barline_unified(

months=roll["submitMonth"].tolist(),

values=vals,

title=title_map.get(c, c),

y_label=y_label_map.get(c, ""),

out_name=f"barline_rolling3_{c}_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=y_lim,

counts=cnt_vals,

)

# 额外输出 alpha 数量（3M滚动总数，按月度 count 求和后再滚动求和）

cnt_month = monthly_df.groupby("submitMonth")["count"].sum().reindex(seq).fillna(0).astype(float)

cnt_roll = cnt_month.rolling(window=3, min_periods=1).sum()

cnt_vals = cnt_roll.tolist()

cnt_ymax = max(abs(v) for v in cnt_vals) if cnt_vals else 1.0

if cnt_ymax == 0:

cnt_ymax = 1.0

cnt_ylim = (0, cnt_ymax * 1.15)

_barline_unified(

months=cnt_roll.index.tolist(),

values=cnt_vals,

title="Alpha Count (Rolling 3M)",

y_label="count",

out_name=f"barline_rolling3_count_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=cnt_ylim,

)

def _combo_positions(n_months: int, n_bars: int) -> Tuple[List[np.ndarray], float]:

x = np.arange(n_months)

total = 0.8

w = total / max(n_bars, 1)

w = min(max(w, 0.05), 0.15)  # 瘦长柱：限制在 [0.05, 0.15]

gap = (total - w * n_bars) / 2.0

offs = []

for i in range(n_bars):

offs.append(x - total / 2 + gap + (i + 0.5) * w + i * (0))

return offs, w

def generate_monthly_combo_barline(monthly_df: pd.DataFrame, year: int = 2025, metrics: Optional[List[str]] = None, baseline_map: Optional[Dict[str, float]] = None, start_month: int = 6, end_month: int = 12) -> None:

if metrics is None:

metrics = ["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

if baseline_map is None:

baseline_map = {

"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0,

"turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0

}

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp = _scale_for_display(tmp, metrics)

# 计算以基线为参考的增量，用于放大差异

deltas = {}

y_max = 0.0

for c in metrics:

if c not in tmp.columns:

continue

base = baseline_map.get(c, 0.0)

vals = (tmp[c] - base).astype(float)

deltas[c] = vals

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

x = np.arange(len(tmp))

pos, bar_w = _combo_positions(len(tmp), len(metrics))

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974", "#64b5cd", "#e17c05", "#76b7b2"]

plt.figure(figsize=(14, 6))

for i, m in enumerate(metrics):

if m not in tmp.columns:

continue

p = pos[i] if i < len(pos) else x

bars = plt.bar(p, deltas[m].tolist(), width=bar_w, color=colors[i % len(colors)], alpha=0.85, label=m, linewidth=0)

plt.plot(x, deltas[m].tolist(), color=colors[i % len(colors)], marker="o", linewidth=1.6)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.03

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for j, rect in enumerate(bars):

val = float(deltas[m].iloc[j] + baseline_map.get(m, 0.0))

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{val:.2f}", ha="center", va="center", fontsize=7, color=colors[i % len(colors)], rotation=90)

plt.xticks(ticks=x, labels=tmp["submitMonth"].tolist(), rotation=45, ha="right")

plt.ylim(y_lim)

plt.axhline(0, color="#999999", linewidth=1, linestyle="--")

plt.title(f"Rolling 3M Combo Bars + Lines (Baseline-Relative) ({year}-{start_month:02d} to {year}-{end_month:02d})")

plt.legend(ncol=3, fontsize=9, title="Metrics (bars & lines)")

# 顶部标注 3M 滚动 alpha 数量（按月滚动求和）

cnt_month = monthly_df.groupby("submitMonth")["count"].sum().reindex(months).fillna(0).astype(float)

cnt_roll = cnt_month.rolling(window=3, min_periods=1).sum().tolist()

for idx, month in enumerate(months):

plt.text(idx, y_lim[1] * 0.95, f"{int(cnt_roll[idx])}", ha="center", va="top", fontsize=7, color="#333333")

# 在顶部右侧标注每月 alpha 数量

for idx, month in enumerate(months):

total_cnt = int(tmp.loc[tmp["submitMonth"] == month, "count"].sum())

plt.text(idx, y_lim[1] * 0.95, f"{total_cnt}", ha="center", va="top", fontsize=7, color="#333333")

plt.tight_layout()

out_path = CHART_DIR / f"combo_monthly_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_rolling3_combo_barline(monthly_df: pd.DataFrame, year: int = 2025, metrics: Optional[List[str]] = None, baseline_map: Optional[Dict[str, float]] = None, start_month: int = 6, end_month: int = 12) -> None:

if metrics is None:

metrics = ["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

if baseline_map is None:

baseline_map = {

"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0,

"turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0

}

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp = _scale_for_display(tmp, metrics)

seq = months

tmp = tmp.set_index("submitMonth").reindex(seq)

roll = tmp[metrics].rolling(window=3, min_periods=1).mean().reset_index()

# 基于基线的增量

deltas = {}

y_max = 0.0

for c in metrics:

if c not in roll.columns:

continue

base = baseline_map.get(c, 0.0)

vals = (roll[c] - base).astype(float)

deltas[c] = vals

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

x = np.arange(len(roll))

pos, bar_w = _combo_positions(len(roll), len(metrics))

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974", "#64b5cd", "#e17c05", "#76b7b2"]

plt.figure(figsize=(14, 6))

for i, m in enumerate(metrics):

if m not in deltas:

continue

p = pos[i] if i < len(pos) else x

bars = plt.bar(p, deltas[m].tolist(), width=bar_w, color=colors[i % len(colors)], alpha=0.85, label=m, linewidth=0)

plt.plot(x, deltas[m].tolist(), color=colors[i % len(colors)], marker="o", linewidth=1.6)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.03

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for j, rect in enumerate(bars):

val = float(deltas[m].iloc[j] + baseline_map.get(m, 0.0))

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{val:.2f}", ha="center", va="center", fontsize=7, color=colors[i % len(colors)], rotation=90)

plt.xticks(ticks=x, labels=roll["submitMonth"].tolist(), rotation=45, ha="right")

plt.ylim(y_lim)

plt.axhline(0, color="#999999", linewidth=1, linestyle="--")

plt.title(f"Rolling 3M Combo Bars + Lines (Baseline-Relative) ({year}-06 to {year}-12)")

plt.legend(ncol=3, fontsize=9, title="Metrics (bars & lines)")

plt.tight_layout()

out_path = CHART_DIR / f"combo_rolling3_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_rolling3_combo_windows(monthly_df: pd.DataFrame, year: int = 2025, metrics: Optional[List[str]] = None, baseline_map: Optional[Dict[str, float]] = None, start_month: int = 6, end_month: int = 12) -> None:

if metrics is None:

metrics = ["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

if baseline_map is None:

baseline_map = {"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0}

tmp = monthly_df.groupby("submitMonth")[metrics].mean().reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp = _scale_for_display(tmp, metrics)

seq = months

tmp = tmp.set_index("submitMonth").reindex(seq)

roll = tmp[metrics].rolling(window=3, min_periods=1).mean().reset_index()

for i in range(2, len(seq)):

start = seq[i - 2]

end = seq[i]

vals = []

deltas = []

labels = []

for m in metrics:

v = roll.loc[i, m]

if pd.isna(v):

continue

vals.append(float(v))

deltas.append(float(v - baseline_map.get(m, 0.0)))

labels.append(m)

if not vals:

continue

y_max = max(abs(x) for x in deltas) if deltas else 1.0

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.2, y_max * 1.2)

x = np.arange(len(labels))

plt.figure(figsize=(10, 5))

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974", "#64b5cd", "#e17c05", "#76b7b2"]

bar_colors = [colors[j % len(colors)] for j in range(len(labels))]

bars = plt.bar(x, deltas, width=0.35, color=bar_colors, alpha=0.9)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.04

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for j, rect in enumerate(bars):

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{vals[j]:.2f}", ha="center", va="center", fontsize=9, rotation=90)

plt.axhline(0, color="#999999", linewidth=1, linestyle="--")

plt.xticks(ticks=x, labels=labels, rotation=30, ha="right")

plt.ylim(y_lim)

plt.title(f"Rolling 3M Window {start} to {end} (Baseline-Relative)")

plt.tight_layout()

out_path = CHART_DIR / f"combo_rolling3_window_{start}_to_{end}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def run_pipeline_default() -> None:

print_exec_timestamp()

force_download = False

start_dt = datetime(2024, 12, 1, tzinfo=timezone.utc)

json_path = OUTPUT_DIR / "alphas_since_2024-12.json"

if force_download:

session = get_session()

raw = fetch_alphas_since(session, start_dt, limit=100)

data = [normalize_alpha_record(r) for r in raw]

save_json(data, json_path)

else:

if json_path.exists():

data = load_json(json_path)

else:

session = get_session()

raw = fetch_alphas_since(session, start_dt, limit=100)

data = [normalize_alpha_record(r) for r in raw]

save_json(data, json_path)

monthly_df = compute_monthly_stats(data)

export_table(monthly_df, "monthly_stats")

generate_monthly_charts(monthly_df)

generate_monthly_barline_unified(monthly_df, year=2025, start_month=3, end_month=12)

generate_rolling3_barline_unified(monthly_df, year=2025, start_month=3, end_month=12)

generate_monthly_combo_barline(

monthly_df,

year=2025,

metrics=["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"],

baseline_map={"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0},

start_month=3,

end_month=12,

)

generate_rolling3_combo_barline(

monthly_df,

year=2025,

metrics=["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"],

baseline_map={"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0},

start_month=3,

end_month=12,

)

generate_rolling3_combo_windows(

monthly_df,

year=2025,

metrics=["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"],

baseline_map={"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0},

start_month=3,

end_month=12,

)

p_start = datetime(2025, 3, 1, tzinfo=timezone.utc)

p_end = datetime(2025, 5, 31, 23, 59, 59, tzinfo=timezone.utc)

custom_df = compute_custom_periods(

data,

periods=[("2025-03_to_2025-05", p_start, p_end)],

)

export_table(custom_df, "custom_period_stats_2025-03_to_2025-05")

if not custom_df.empty:

generate_custom_period_charts(custom_df, "2025-03_to_2025-05")

logger.info("Pipeline finished")

if __name__ == "__main__":

run_pipeline_default()

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

这标题实在太震撼了

羡慕的泪水从我的嘴角流出

希望有一天能追上大佬的步伐！

==================================================================================


---

### 技术对话片段 4 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 16815刀季度奖经验分享-小虎经验分享_38980270292631.md
- **时间**: 3个月前

**提问/主帖背景 (SD17531)**:
大家好，我是SD7531，顾问朋友们都很nice，一般喊我小虎哥。

我从 2024 年 12 月 13 日开始提交顾问 Alpha，近三次定级都很幸运地保住了 GM。我本科专业是公共管理，代码一般是现学现用。 我的背景在顾问里也算和量化最不相关的之一，不过反过来说，我这样的背景都能做到 GM，相信绝大多数顾问朋友，只要愿意付出时间和精力，都能冲刺 GM。
下面附上我的季度奖和一路熬过来的每日 base，希望能给大家一些鼓励：只要不放弃，收益终究会一柱擎天。
 
> [!NOTE] [图片 OCR 识别内容]
> Other Payment
> For attending the offline meetup at BJISHIGZin Dec 2024
> 02/07/2025
> US$137.00
> 202501 Payment
> 05/22/2025
> 05$112.73
> Value Factor Improvement Program Rewards
> 06/25/2025
> 0S$200.00
> Referral
> 07/13/2025
> 0S$200.00
> 2025 Q2 Payment
> 08/17/2025
> 0S$322.73
> Research Award August
> 09/01/2025
> 05$28.00
> Research Award
> 09/11/2025
> US$14.00
> Research Award
> 09/25/2025
> 0S$28.00
> 2025 Q3 Payment
> 11/24/2025
> US$8,065.01
> Referral
> 12/26/2025
> US$200.00
> Power Pool Alphas Monthly Competition December 2025
> ASI D1
> 01/01/2026
> US$500.00
> 2025Q4 Payment
> 02/21/2026
> US$16,815.45
> 11/18/2024
> Total
> 05$26,622.92
> 03/10/2026
  
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/20/2026
> Regular:
> 57.93
> Super:
> 55.58
> Total:
> 113.50999999999999
> 75
> 50
> 25
> Mar
> May
> May
> Mar
 
关于季度奖，顾问 YX23928 (Rank 8)和
顾问 SJ65808 (Rank 20)两位大佬都有分享。帖子分别如下： [[L2] 一个非科班选手的量化打怪升级路季度奖突破万刀必读_38628691756695.md]([L2] 一个非科班选手的量化打怪升级路季度奖突破万刀必读_38628691756695.md)  

 [[L2] 2025年度收入回顾经验分享_38623022786839.md]([L2] 2025年度收入回顾经验分享_38623022786839.md)  

两位大佬讲的很详细了，我听了也获益良多。

先分享一下我自己的数据：
第一次季度奖，VF分别是0.70-0.85-0.82，weight增加值大概是9，对应的季度奖是8065刀。
第二次季度奖，VF分别是0.87-0.90-0.98，weight增加值大概是15，对应的季度奖是16815刀。

从这两次季度奖的情况来看，我个人认为季度奖的核心影响因素是该季度第三个月的 VF 值 —— 这个 VF 值恰好核算的是当季所有提交 Alpha 的质量。和其他顾问交流后也能明显感受到，最后一个月 VF 低于 0.9，大多只能拿到保底季度奖。

那么如何获取更高的季度奖， 其实也可以转化为如何获得更高的VF。我来分享一下我自己的提交数据，希望对大家有所启发。我将所有历史提交的RA和SA的数据下载下来，让AI帮忙绘制了月度Alpha平均指标和三月滚动的alpha平均指标（correlation）的图片。
 
> [!NOTE] [图片 OCR 识别内容]
> Monthly Combo Bars
> Lines (Baseline-Relative) (2025-03 to 2025-12)
> 文
> 111
> 65
> 114
> 85
> 30
> 20
> 10
> {}:$
> 吕@员:岛芒思
> @3&8@3
> 恩
> 总@@寰@
> &38838@
> 38号
> 李e38
> }a:黑
> 88g8品&
> 8军$8}&
> 38 $@ $寺
> 8
> O 寸
> C C
> R
> O I R
> i
> @
>  「
> &
> M 
> Se
> 寸卉
> O M
> S83
> CC
> 385
> U m
> m m
> SSaw
> mni
> SRo
> 10
> 20
> Metrics (bars & lines)
> sharpe
> margin
> prodcorrelation
> 30
> fitness
> turnover
> selfCorrelation
> returns
> 8
> 2025-03
> 2025-04
> 2025-05
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
> 2025-C
 
 
> [!NOTE] [图片 OCR 识别内容]
> Rolling 3M Combo Bars + Lines (Baseline-Relative) (2025-06 to 2025-12)
> 30
> 20
> 10
> & 守835苎%
> 总v8怠畏莴舄
> `:
> 8@@S$
> 莴营s~
> 总&盒窝@密忿
> 8品 @@%@品
> @$ &
> 品
> @R &
> @
> 88Rg孚8 &
> @%38w& @
> SO
> 8
> R~ &
> R
>  e只~
> M M
> S9a m
> qm
> 9896
> SR Sw
> mm
> 58
> OUm
> 10
> -20
> Metrics (bars
> lines)
> Sharpe
> margin
> prodCorrelation
> fitness
> turnoVer
> selfCorrelation
> 30
> returns
> @%5
> 9e6
> 1品
> 2025-03
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> 2025-09
> 2025-10
> 2025-11
> 2025-12
 我个人的 VF 近几个月呈缓慢增长趋势，波动幅度并不大。VF 的计算公式在论坛中就能找到。从我的数据来看，VF受影响确实是多个维度综合产生的，提交数量、prod_correlation、其他顾问的提交质量等都会对VF产生影响。可以从图片中看到我每个月的数据情况，大家有需要的话可以根据我的VF波动去评估该月份涨跌的主要原因。值得一提的是，我 10-12 月每月提交的因子数量相差不大，且呈 85-91-92 的递增趋势，prodCorrelation 表现也比 7-9 月好不少；而 7-9 月的提交量则是 114-111-71 的骤降趋势，这或许是我第四季度 VF 优于第三季度的原因之一。

然后打铁还需自身硬，老生常谈的diversity也是必须安排上的。我的策略，主要是在同一个region多做不同类型的因子，但是不做太多不同的region。
 
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-04, October 1st, 2025
> December 31st, 2025
> Category
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
> 16
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> MaCro
> Model
> 15
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media
 因子方面，我优先做多操作符少的 Atom，同时尽量使用不同的操作符来保证多样性。
 
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st, 2025
> December 31st, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 4.19
> 167
> 1.39
> Fields used
> Community activity
> Max simulation streak
> 223
> 44.7
> 387
 
非常建议大家用代码分析自己每月的提交数据，我把 AI 写的代码附在文末，抛砖引玉。大家可以结合 Region、Delay、月度、三月周期做更深度的分析，再和自己的历史 VF 数据对比，相信会有不少收获。

最后，一路走来，我感觉我的运气还是非常不错的，运气最好的地方就是认识了这么多优秀的顾问朋友。感谢课代表，游戏王，橘子姐，毛老师，MG哥，老虎哥，大角羊，文姐，孙哥，强哥（排名不分先后），太多需要感谢的，就不一一列举了。希望后面能跟大家继续一起进步。

大佬们，请继续教我本领！！！

代码：

import os

import json

import math

import logging

from pathlib import Path

from datetime import datetime, timezone

from typing import Any, Dict, List, Optional, Tuple

import requests

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

LOG_NAME = Path(__file__).stem

BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR / "logs"

OUTPUT_DIR = BASE_DIR / "outputs"

CHART_DIR = OUTPUT_DIR / "charts"

def _ensure_dirs() -> None:

LOG_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CHART_DIR.mkdir(parents=True, exist_ok=True)

def _setup_logger() -> logging.Logger:

_ensure_dirs()

logger = logging.getLogger(LOG_NAME)

if not logger.handlers:

logger.setLevel(logging.INFO)

fh = logging.FileHandler(LOG_DIR / f"{LOG_NAME}.log", encoding="utf-8")

fmt = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s")

fh.setFormatter(fmt)

logger.addHandler(fh)

return logger

logger = _setup_logger()

def print_exec_timestamp() -> None:

ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[EXECUTION START] {ts}")

logger.info(f"Execution started at {ts}")

def get_session() -> requests.Session:

try:

# 优先使用现成的已登录会话

from machine_lib import s as session  # type: ignore

if isinstance(session, requests.Session):

logger.info("Using session 's' from machine_lib")

return session

except Exception:

pass

try:

from machine_lib import login  # type: ignore

logger.info("Creating session via machine_lib.login()")

session = login()

if isinstance(session, requests.Session):

return session

except Exception as e:

logger.info(f"machine_lib.login() not available or failed: {e}")

logger.info("Fallback to anonymous requests.Session (may not work without auth)")

return requests.Session()

def _iso_with_tz(dt: datetime) -> str:

if dt.tzinfo is None:

dt = dt.replace(tzinfo=timezone.utc)

return dt.astimezone().isoformat(timespec="seconds")

def fetch_alphas_since(

session: requests.Session,

start_submitted_dt: datetime,

limit: int = 100,

) -> List[Dict[str, Any]]:

logger.info(f"Fetching alphas since submission time: {start_submitted_dt.isoformat()}")

results: List[Dict[str, Any]] = []

base = " [[链接已屏蔽]) "

start_str = _iso_with_tz(start_submitted_dt)

offset = 0

while True:

url = (

f"{base}?limit={limit}&offset={offset}"

f"&dateSubmitted%3E={requests.utils.quote(start_str, safe='')}"

f"&hidden=false"

f"&status!=UNSUBMITTED%1FIS-FAIL"

f"&order=-dateSubmitted"

)

try:

resp = session.get(url)

if resp.status_code != 200:

logger.info(f"Fetch error: status={resp.status_code}, text={resp.text[:300]}")

break

data = resp.json()

page = data.get("results", [])

results.extend(page)

count = int(data.get("count", 0))

logger.info(f"Fetched {len(page)} items at offset {offset}, total so far {len(results)}/{count}")

if offset + len(page) >= count or len(page) < limit:

break

offset += limit

except Exception as e:

logger.info(f"Exception during fetch: {e}")

break

logger.info(f"Total fetched records: {len(results)}")

return results

def _safe_get(d: Dict[str, Any], *keys: str, default: Any = None) -> Any:

cur: Any = d

for k in keys:

if not isinstance(cur, dict) or k not in cur:

return default

cur = cur[k]

return cur

def normalize_alpha_record(rec: Dict[str, Any]) -> Dict[str, Any]:

is_data = rec.get("is", {}) or {}

risk_neu = is_data.get("riskNeutralized", {}) or rec.get("riskNeutralized", {}) or {}

settings = rec.get("settings", {}) or {}

norm = {

"id": rec.get("id"),

"type": rec.get("type"),

"name": rec.get("name"),

"dateCreated": rec.get("dateCreated"),

"dateSubmitted": rec.get("dateSubmitted"),

"settings": {

"region": settings.get("region"),

"universe": settings.get("universe"),

"delay": settings.get("delay"),

"decay": settings.get("decay"),

"neutralization": settings.get("neutralization"),

"truncation": settings.get("truncation"),

"pasteurization": settings.get("pasteurization"),

"unitHandling": settings.get("unitHandling"),

"visualization": settings.get("visualization"),

},

"is": {

"fitness": is_data.get("fitness"),

"longCount": is_data.get("longCount"),

"shortCount": is_data.get("shortCount"),

"turnover": is_data.get("turnover"),

"returns": is_data.get("returns"),

"drawdown": is_data.get("drawdown"),

"margin": is_data.get("margin"),

"sharpe": is_data.get("sharpe"),

"prodCorrelation": is_data.get("prodCorrelation"),

"selfCorrelation": is_data.get("selfCorrelation"),

},

"riskNeutralized": {

"pnl": risk_neu.get("pnl"),

"bookSize": risk_neu.get("bookSize"),

"longCount": risk_neu.get("longCount"),

"shortCount": risk_neu.get("shortCount"),

"turnover": risk_neu.get("turnover"),

"returns": risk_neu.get("returns"),

"drawdown": risk_neu.get("drawdown"),

"margin": risk_neu.get("margin"),

"fitness": risk_neu.get("fitness"),

"sharpe": risk_neu.get("sharpe"),

},

"checks": rec.get("is", {}).get("checks", []) or rec.get("checks", []),

}

if "regular" in rec and isinstance(rec["regular"], dict):

norm["regular"] = {"code": rec["regular"].get("code")}

if "combo" in rec:

norm["combo"] = rec.get("combo")

if "selection" in rec:

norm["selection"] = rec.get("selection")

return norm

def save_json(data: List[Dict[str, Any]], path: Path) -> None:

_ensure_dirs()

with path.open("w", encoding="utf-8") as f:

json.dump(data, f, ensure_ascii=False, indent=2)

logger.info(f"Saved JSON data to {path}")

def load_json(path: Path) -> List[Dict[str, Any]]:

with path.open("r", encoding="utf-8") as f:

data = json.load(f)

logger.info(f"Loaded JSON data from {path}")

return data

def _parse_month(s: Optional[str]) -> Optional[str]:

if not s:

return None

try:

dt = datetime.fromisoformat(s.replace("Z", "+00:00"))

return dt.strftime("%Y-%m")

except Exception:

return None

def _to_frame(records: List[Dict[str, Any]]) -> pd.DataFrame:

rows = []

for r in records:

isd = r.get("is", {}) or {}

st = r.get("settings", {}) or {}

rows.append(

{

"id": r.get("id"),

"type": r.get("type"),

"name": r.get("name"),

"dateSubmitted": r.get("dateSubmitted"),

"submitMonth": _parse_month(r.get("dateSubmitted")),

"region": st.get("region"),

"delay": st.get("delay"),

"turnover": isd.get("turnover"),

"fitness": isd.get("fitness"),

"returns": isd.get("returns"),

"drawdown": isd.get("drawdown"),

"margin": isd.get("margin"),

"sharpe": isd.get("sharpe"),

"prodCorrelation": isd.get("prodCorrelation"),

"selfCorrelation": isd.get("selfCorrelation"),

}

)

df = pd.DataFrame(rows)

return df

def compute_monthly_stats(records: List[Dict[str, Any]]) -> pd.DataFrame:

df = _to_frame(records)

df = df.dropna(subset=["submitMonth", "region", "delay"])

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

agg_map = {m: "mean" for m in metrics}

grp = df.groupby(["submitMonth", "region", "delay"], dropna=False)

stats = grp.agg(agg_map).reset_index()

cnt_total = grp.size().reset_index(name="count")

cnt_regular = grp.apply(lambda g: (g["type"] == "REGULAR").sum()).reset_index(name="count_regular")

cnt_super = grp.apply(lambda g: (g["type"] == "SUPER").sum()).reset_index(name="count_super")

out = stats.merge(cnt_total, on=["submitMonth", "region", "delay"], how="left")

out = out.merge(cnt_regular, on=["submitMonth", "region", "delay"], how="left")

out = out.merge(cnt_super, on=["submitMonth", "region", "delay"], how="left")

return out

def export_table(df: pd.DataFrame, name: str) -> Tuple[Path, Path]:

_ensure_dirs()

csv_path = OUTPUT_DIR / f"{name}.csv"

xlsx_path = OUTPUT_DIR / f"{name}.xlsx"

try:

df.to_csv(csv_path, index=False, encoding="utf-8-sig")

with pd.ExcelWriter(xlsx_path, engine="xlsxwriter") as writer:

df.to_excel(writer, index=False, sheet_name="data")

logger.info(f"Exported tables: {csv_path.name}, {xlsx_path.name}")

return csv_path, xlsx_path

except PermissionError:

ts = datetime.now().strftime("%Y%m%d_%H%M%S")

csv_alt = OUTPUT_DIR / f"{name}_{ts}.csv"

xlsx_alt = OUTPUT_DIR / f"{name}_{ts}.xlsx"

df.to_csv(csv_alt, index=False, encoding="utf-8-sig")

with pd.ExcelWriter(xlsx_alt, engine="xlsxwriter") as writer:

df.to_excel(writer, index=False, sheet_name="data")

logger.info(f"Target locked, exported tables to: {csv_alt.name}, {xlsx_alt.name}")

return csv_alt, xlsx_alt

def _line_trend(df: pd.DataFrame, metric: str, title: str, fname: str) -> None:

tmp = df.groupby("submitMonth")[metric].mean().reset_index()

tmp = tmp.sort_values("submitMonth")

plt.figure(figsize=(10, 4))

sns.lineplot(data=tmp, x="submitMonth", y=metric, marker="o")

plt.title(title)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

out_path = CHART_DIR / fname

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def _heatmap_region_delay(df: pd.DataFrame, metric: str, title: str, fname: str) -> None:

tmp = df.groupby(["region", "delay"])[metric].mean().reset_index()

pivot = tmp.pivot(index="region", columns="delay", values=metric)

plt.figure(figsize=(10, 6))

sns.heatmap(pivot, annot=True, fmt=".3f", cmap="Blues")

plt.title(title)

plt.tight_layout()

out_path = CHART_DIR / fname

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def _bar_latest_month(df: pd.DataFrame, metric: str, title: str, fname: str) -> None:

if "submitMonth" not in df.columns or df["submitMonth"].dropna().empty:

return

latest = sorted(m for m in df["submitMonth"].dropna().unique())[-1]

tmp = df[df["submitMonth"] == latest].groupby(["region", "delay"])[metric].mean().reset_index()

plt.figure(figsize=(12, 5))

sns.barplot(data=tmp, x="region", y=metric, hue="delay")

plt.title(f"{title} (Latest: {latest})")

plt.tight_layout()

out_path = CHART_DIR / fname

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_monthly_charts(df: pd.DataFrame) -> None:

metrics = [

("sharpe", "Average Sharpe Ratio"),

("fitness", "Average Fitness"),

("returns", "Average Return"),

("drawdown", "Average Drawdown"),

("margin", "Average Margin"),

("turnover", "Average Turnover"),

("prodCorrelation", "Average Prod Correlation"),

("selfCorrelation", "Average Self Correlation"),

]

for col, title in metrics:

_line_trend(df, col, f"{title} - Monthly Trend", f"monthly_trend_{col}.png")

_heatmap_region_delay(df, col, f"{title} by Region x Delay", f"heatmap_region_delay_{col}.png")

_bar_latest_month(df, col, f"{title} Region/Delay", f"bar_latest_{col}.png")

def compute_custom_periods(

records: List[Dict[str, Any]],

periods: List[Tuple[str, datetime, datetime]],

) -> pd.DataFrame:

df = _to_frame(records)

df = df.dropna(subset=["dateSubmitted", "region", "delay"])

def within(dts: str, start: datetime, end: datetime) -> bool:

try:

dt = datetime.fromisoformat(dts.replace("Z", "+00:00"))

return start <= dt <= end

except Exception:

return False

rows = []

for label, start, end in periods:

mask = df["dateSubmitted"].apply(lambda s: within(s, start, end))

sub = df[mask].copy()

if sub.empty:

continue

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

grp = sub.groupby(["region", "delay"], dropna=False)

stats = grp[metrics].mean().reset_index()

stats.insert(0, "period", label)

cnt_total = grp.size().reset_index(name="count")

cnt_regular = grp.apply(lambda g: (g["type"] == "REGULAR").sum()).reset_index(name="count_regular")

cnt_super = grp.apply(lambda g: (g["type"] == "SUPER").sum()).reset_index(name="count_super")

st = stats.merge(cnt_total, on=["region", "delay"], how="left")

st = st.merge(cnt_regular, on=["region", "delay"], how="left")

st = st.merge(cnt_super, on=["region", "delay"], how="left")

rows.append(st)

if not rows:

return pd.DataFrame(

columns=[

"period", "region", "delay",

"sharpe", "fitness", "returns", "drawdown", "margin", "prodCorrelation", "selfCorrelation",

"count", "count_regular", "count_super",

]

)

return pd.concat(rows, ignore_index=True)

def generate_custom_period_charts(df: pd.DataFrame, period_label: str) -> None:

metrics = [

("sharpe", "Average Sharpe Ratio"),

("fitness", "Average Fitness"),

("returns", "Average Return"),

("drawdown", "Average Drawdown"),

("margin", "Average Margin"),

("turnover", "Average Turnover"),

("prodCorrelation", "Average Prod Correlation"),

("selfCorrelation", "Average Self Correlation"),

]

for col, title in metrics:

tmp = df.groupby("region")[col].mean().reset_index()

plt.figure(figsize=(10, 4))

sns.barplot(data=tmp, x="region", y=col)

plt.title(f"{title} by Region - {period_label}")

plt.tight_layout()

out_path = CHART_DIR / f"{period_label}_region_{col}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

plt.figure(figsize=(10, 5))

sns.boxplot(data=df, x="delay", y=col)

plt.title(f"{title} Distribution by Delay - {period_label}")

plt.tight_layout()

out_path = CHART_DIR / f"{period_label}_delay_box_{col}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def _scale_for_display(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:

scaled = df.copy()

if "returns" in cols and "returns" in scaled.columns:

scaled["returns"] = scaled["returns"] * 100.0

if "turnover" in cols and "turnover" in scaled.columns:

scaled["turnover"] = scaled["turnover"] * 100.0

if "margin" in cols and "margin" in scaled.columns:

scaled["margin"] = scaled["margin"] * 10000.0

if "prodCorrelation" in cols and "prodCorrelation" in scaled.columns:

scaled["prodCorrelation"] = scaled["prodCorrelation"] * 10.0

if "selfCorrelation" in cols and "selfCorrelation" in scaled.columns:

scaled["selfCorrelation"] = scaled["selfCorrelation"] * 10.0

return scaled

def _barline_unified(months: List[str], values: List[float], title: str, y_label: str, out_name: str, y_lim: Tuple[float, float], counts: Optional[List[float]] = None) -> None:

x = np.arange(len(months))

plt.figure(figsize=(12, 5))

bars = plt.bar(x, values, color="#4c72b0", alpha=0.6)

plt.plot(x, values, color="#c44e52", marker="o", linewidth=2)

plt.xticks(ticks=x, labels=months, rotation=45, ha="right")

plt.ylabel(y_label)

plt.title(title)

plt.ylim(y_lim)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.03

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for rect, v in zip(bars, values):

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{v:.2f}", ha="center", va="center", fontsize=8, rotation=90)

if counts is not None and len(counts) == len(x):

y_top = y_lim[1] - (y_lim[1] - y_lim[0]) * 0.02

for xi, c in zip(x, counts):

plt.text(xi, y_top, f"n={int(c)}", ha="center", va="top", fontsize=8, color="#333333")

plt.tight_layout()

out_path = CHART_DIR / out_name

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_monthly_barline_unified(monthly_df: pd.DataFrame, year: int = 2025, start_month: int = 6, end_month: int = 12) -> None:

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy()

tmp = tmp.sort_values("submitMonth")

tmp_scaled = _scale_for_display(tmp, metrics)

y_max = 0.0

for c in metrics:

if c in tmp_scaled.columns:

vals = tmp_scaled[c].dropna().values

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

title_map = {

"sharpe": "Average Sharpe (Monthly)",

"fitness": "Average Fitness (Monthly)",

"returns": "Average Return % (Monthly)",

"drawdown": "Average Drawdown (Monthly)",

"margin": "Average Margin ×1e4 (Monthly)",

"turnover": "Average Turnover % (Monthly)",

"prodCorrelation": "Average Prod Correlation (Monthly)",

"selfCorrelation": "Average Self Correlation (Monthly)",

}

y_label_map = {

"returns": "%",

"turnover": "%",

"margin": "×1e4",

}

# 月度 alpha 数量（按 submitMonth 聚合求和），用于叠加显示

cnt_series = monthly_df.groupby("submitMonth")["count"].sum().reindex(tmp_scaled["submitMonth"]).fillna(0)

cnt_list = cnt_series.tolist()

for c in metrics:

if c not in tmp_scaled.columns:

continue

vals = tmp_scaled[c].tolist()

_barline_unified(

months=[m for m in tmp_scaled["submitMonth"]],

values=vals,

title=title_map.get(c, c),

y_label=y_label_map.get(c, ""),

out_name=f"barline_monthly_{c}_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=y_lim,

counts=cnt_list,

)

# 额外输出 alpha 数量（月度总数，求和）

cnt = monthly_df.groupby("submitMonth")["count"].sum().reindex(months).fillna(0)

if not cnt.empty:

cnt_vals = cnt.tolist()

cnt_ymax = max(abs(v) for v in cnt_vals) if cnt_vals else 1.0

if cnt_ymax == 0:

cnt_ymax = 1.0

cnt_ylim = (0, cnt_ymax * 1.15)

_barline_unified(

months=months,

values=cnt_vals,

title="Alpha Count (Monthly)",

y_label="count",

out_name=f"barline_monthly_count_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=cnt_ylim,

)

def generate_rolling3_barline_unified(monthly_df: pd.DataFrame, year: int = 2025, start_month: int = 6, end_month: int = 12) -> None:

metrics = ["sharpe", "fitness", "returns", "drawdown", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp_scaled = _scale_for_display(tmp, metrics)

seq = months

tmp_scaled = tmp_scaled.set_index("submitMonth").reindex(seq)

roll = tmp_scaled[metrics].rolling(window=3, min_periods=1).mean().reset_index()

y_max = 0.0

for c in metrics:

vals = roll[c].dropna().values

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

title_map = {

"sharpe": "Average Sharpe (Rolling 3M)",

"fitness": "Average Fitness (Rolling 3M)",

"returns": "Average Return % (Rolling 3M)",

"drawdown": "Average Drawdown (Rolling 3M)",

"margin": "Average Margin ×1e4 (Rolling 3M)",

"turnover": "Average Turnover % (Rolling 3M)",

"prodCorrelation": "Average Prod Correlation (Rolling 3M)",

"selfCorrelation": "Average Self Correlation (Rolling 3M)",

}

y_label_map = {

"returns": "%",

"turnover": "%",

"margin": "×1e4",

}

for c in metrics:

vals = roll[c].tolist()

_barline_unified(

months=roll["submitMonth"].tolist(),

values=vals,

title=title_map.get(c, c),

y_label=y_label_map.get(c, ""),

out_name=f"barline_rolling3_{c}_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=y_lim,

counts=cnt_vals,

)

# 额外输出 alpha 数量（3M滚动总数，按月度 count 求和后再滚动求和）

cnt_month = monthly_df.groupby("submitMonth")["count"].sum().reindex(seq).fillna(0).astype(float)

cnt_roll = cnt_month.rolling(window=3, min_periods=1).sum()

cnt_vals = cnt_roll.tolist()

cnt_ymax = max(abs(v) for v in cnt_vals) if cnt_vals else 1.0

if cnt_ymax == 0:

cnt_ymax = 1.0

cnt_ylim = (0, cnt_ymax * 1.15)

_barline_unified(

months=cnt_roll.index.tolist(),

values=cnt_vals,

title="Alpha Count (Rolling 3M)",

y_label="count",

out_name=f"barline_rolling3_count_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png",

y_lim=cnt_ylim,

)

def _combo_positions(n_months: int, n_bars: int) -> Tuple[List[np.ndarray], float]:

x = np.arange(n_months)

total = 0.8

w = total / max(n_bars, 1)

w = min(max(w, 0.05), 0.15)  # 瘦长柱：限制在 [0.05, 0.15]

gap = (total - w * n_bars) / 2.0

offs = []

for i in range(n_bars):

offs.append(x - total / 2 + gap + (i + 0.5) * w + i * (0))

return offs, w

def generate_monthly_combo_barline(monthly_df: pd.DataFrame, year: int = 2025, metrics: Optional[List[str]] = None, baseline_map: Optional[Dict[str, float]] = None, start_month: int = 6, end_month: int = 12) -> None:

if metrics is None:

metrics = ["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

if baseline_map is None:

baseline_map = {

"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0,

"turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0

}

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp = _scale_for_display(tmp, metrics)

# 计算以基线为参考的增量，用于放大差异

deltas = {}

y_max = 0.0

for c in metrics:

if c not in tmp.columns:

continue

base = baseline_map.get(c, 0.0)

vals = (tmp[c] - base).astype(float)

deltas[c] = vals

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

x = np.arange(len(tmp))

pos, bar_w = _combo_positions(len(tmp), len(metrics))

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974", "#64b5cd", "#e17c05", "#76b7b2"]

plt.figure(figsize=(14, 6))

for i, m in enumerate(metrics):

if m not in tmp.columns:

continue

p = pos[i] if i < len(pos) else x

bars = plt.bar(p, deltas[m].tolist(), width=bar_w, color=colors[i % len(colors)], alpha=0.85, label=m, linewidth=0)

plt.plot(x, deltas[m].tolist(), color=colors[i % len(colors)], marker="o", linewidth=1.6)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.03

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for j, rect in enumerate(bars):

val = float(deltas[m].iloc[j] + baseline_map.get(m, 0.0))

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{val:.2f}", ha="center", va="center", fontsize=7, color=colors[i % len(colors)], rotation=90)

plt.xticks(ticks=x, labels=tmp["submitMonth"].tolist(), rotation=45, ha="right")

plt.ylim(y_lim)

plt.axhline(0, color="#999999", linewidth=1, linestyle="--")

plt.title(f"Rolling 3M Combo Bars + Lines (Baseline-Relative) ({year}-{start_month:02d} to {year}-{end_month:02d})")

plt.legend(ncol=3, fontsize=9, title="Metrics (bars & lines)")

# 顶部标注 3M 滚动 alpha 数量（按月滚动求和）

cnt_month = monthly_df.groupby("submitMonth")["count"].sum().reindex(months).fillna(0).astype(float)

cnt_roll = cnt_month.rolling(window=3, min_periods=1).sum().tolist()

for idx, month in enumerate(months):

plt.text(idx, y_lim[1] * 0.95, f"{int(cnt_roll[idx])}", ha="center", va="top", fontsize=7, color="#333333")

# 在顶部右侧标注每月 alpha 数量

for idx, month in enumerate(months):

total_cnt = int(tmp.loc[tmp["submitMonth"] == month, "count"].sum())

plt.text(idx, y_lim[1] * 0.95, f"{total_cnt}", ha="center", va="top", fontsize=7, color="#333333")

plt.tight_layout()

out_path = CHART_DIR / f"combo_monthly_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_rolling3_combo_barline(monthly_df: pd.DataFrame, year: int = 2025, metrics: Optional[List[str]] = None, baseline_map: Optional[Dict[str, float]] = None, start_month: int = 6, end_month: int = 12) -> None:

if metrics is None:

metrics = ["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

if baseline_map is None:

baseline_map = {

"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0,

"turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0

}

tmp = monthly_df.groupby("submitMonth")[metrics + ["count"]].agg({**{m: "mean" for m in metrics}, "count": "sum"}).reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp = _scale_for_display(tmp, metrics)

seq = months

tmp = tmp.set_index("submitMonth").reindex(seq)

roll = tmp[metrics].rolling(window=3, min_periods=1).mean().reset_index()

# 基于基线的增量

deltas = {}

y_max = 0.0

for c in metrics:

if c not in roll.columns:

continue

base = baseline_map.get(c, 0.0)

vals = (roll[c] - base).astype(float)

deltas[c] = vals

if len(vals):

y_max = max(y_max, float(np.nanpercentile(np.abs(vals), 95)))

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.1, y_max * 1.1)

x = np.arange(len(roll))

pos, bar_w = _combo_positions(len(roll), len(metrics))

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974", "#64b5cd", "#e17c05", "#76b7b2"]

plt.figure(figsize=(14, 6))

for i, m in enumerate(metrics):

if m not in deltas:

continue

p = pos[i] if i < len(pos) else x

bars = plt.bar(p, deltas[m].tolist(), width=bar_w, color=colors[i % len(colors)], alpha=0.85, label=m, linewidth=0)

plt.plot(x, deltas[m].tolist(), color=colors[i % len(colors)], marker="o", linewidth=1.6)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.03

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for j, rect in enumerate(bars):

val = float(deltas[m].iloc[j] + baseline_map.get(m, 0.0))

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{val:.2f}", ha="center", va="center", fontsize=7, color=colors[i % len(colors)], rotation=90)

plt.xticks(ticks=x, labels=roll["submitMonth"].tolist(), rotation=45, ha="right")

plt.ylim(y_lim)

plt.axhline(0, color="#999999", linewidth=1, linestyle="--")

plt.title(f"Rolling 3M Combo Bars + Lines (Baseline-Relative) ({year}-06 to {year}-12)")

plt.legend(ncol=3, fontsize=9, title="Metrics (bars & lines)")

plt.tight_layout()

out_path = CHART_DIR / f"combo_rolling3_{year}-{start_month:02d}_to_{year}-{end_month:02d}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def generate_rolling3_combo_windows(monthly_df: pd.DataFrame, year: int = 2025, metrics: Optional[List[str]] = None, baseline_map: Optional[Dict[str, float]] = None, start_month: int = 6, end_month: int = 12) -> None:

if metrics is None:

metrics = ["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"]

if baseline_map is None:

baseline_map = {"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0}

tmp = monthly_df.groupby("submitMonth")[metrics].mean().reset_index()

months = [f"{year}-{m:02d}" for m in range(start_month, end_month + 1)]

tmp = tmp[tmp["submitMonth"].isin(months)].copy().sort_values("submitMonth")

tmp = _scale_for_display(tmp, metrics)

seq = months

tmp = tmp.set_index("submitMonth").reindex(seq)

roll = tmp[metrics].rolling(window=3, min_periods=1).mean().reset_index()

for i in range(2, len(seq)):

start = seq[i - 2]

end = seq[i]

vals = []

deltas = []

labels = []

for m in metrics:

v = roll.loc[i, m]

if pd.isna(v):

continue

vals.append(float(v))

deltas.append(float(v - baseline_map.get(m, 0.0)))

labels.append(m)

if not vals:

continue

y_max = max(abs(x) for x in deltas) if deltas else 1.0

if y_max == 0.0:

y_max = 1.0

y_lim = (-y_max * 1.2, y_max * 1.2)

x = np.arange(len(labels))

plt.figure(figsize=(10, 5))

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974", "#64b5cd", "#e17c05", "#76b7b2"]

bar_colors = [colors[j % len(colors)] for j in range(len(labels))]

bars = plt.bar(x, deltas, width=0.35, color=bar_colors, alpha=0.9)

y_base = 0.0

y_off = (y_lim[1] - y_lim[0]) * 0.04

y_text = max(y_lim[0] + y_off * 0.2, y_base - y_off)

for j, rect in enumerate(bars):

plt.text(rect.get_x() + rect.get_width() / 2, y_text, f"{vals[j]:.2f}", ha="center", va="center", fontsize=9, rotation=90)

plt.axhline(0, color="#999999", linewidth=1, linestyle="--")

plt.xticks(ticks=x, labels=labels, rotation=30, ha="right")

plt.ylim(y_lim)

plt.title(f"Rolling 3M Window {start} to {end} (Baseline-Relative)")

plt.tight_layout()

out_path = CHART_DIR / f"combo_rolling3_window_{start}_to_{end}.png"

plt.savefig(out_path, dpi=150)

plt.close()

logger.info(f"Saved chart: {out_path.name}")

def run_pipeline_default() -> None:

print_exec_timestamp()

force_download = False

start_dt = datetime(2024, 12, 1, tzinfo=timezone.utc)

json_path = OUTPUT_DIR / "alphas_since_2024-12.json"

if force_download:

session = get_session()

raw = fetch_alphas_since(session, start_dt, limit=100)

data = [normalize_alpha_record(r) for r in raw]

save_json(data, json_path)

else:

if json_path.exists():

data = load_json(json_path)

else:

session = get_session()

raw = fetch_alphas_since(session, start_dt, limit=100)

data = [normalize_alpha_record(r) for r in raw]

save_json(data, json_path)

monthly_df = compute_monthly_stats(data)

export_table(monthly_df, "monthly_stats")

generate_monthly_charts(monthly_df)

generate_monthly_barline_unified(monthly_df, year=2025, start_month=3, end_month=12)

generate_rolling3_barline_unified(monthly_df, year=2025, start_month=3, end_month=12)

generate_monthly_combo_barline(

monthly_df,

year=2025,

metrics=["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"],

baseline_map={"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0},

start_month=3,

end_month=12,

)

generate_rolling3_combo_barline(

monthly_df,

year=2025,

metrics=["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"],

baseline_map={"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0},

start_month=3,

end_month=12,

)

generate_rolling3_combo_windows(

monthly_df,

year=2025,

metrics=["sharpe", "fitness", "returns", "margin", "turnover", "prodCorrelation", "selfCorrelation"],

baseline_map={"sharpe": 1.0, "fitness": 0.0, "returns": 0.0, "margin": 0.0, "turnover": 0.0, "prodCorrelation": 0.0, "selfCorrelation": 0.0},

start_month=3,

end_month=12,

)

p_start = datetime(2025, 3, 1, tzinfo=timezone.utc)

p_end = datetime(2025, 5, 31, 23, 59, 59, tzinfo=timezone.utc)

custom_df = compute_custom_periods(

data,

periods=[("2025-03_to_2025-05", p_start, p_end)],

)

export_table(custom_df, "custom_period_stats_2025-03_to_2025-05")

if not custom_df.empty:

generate_custom_period_charts(custom_df, "2025-03_to_2025-05")

logger.info("Pipeline finished")

if __name__ == "__main__":

run_pipeline_default()

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

这标题实在太震撼了

羡慕的泪水从我的嘴角流出

希望有一天能追上大佬的步伐！

==================================================================================


---

### 技术对话片段 5 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 2025年Q4 Genus升级失败小结_37581803221143.md
- **时间**: 5个月前

**提问/主帖背景 (LL61351)**:
今天收到“Genius Levels Refreshed!”的通知，点到genus页面查看一下，怎么还是三个五角星？


> [!NOTE] [图片 OCR 识别内容]
> Genius level: Gold
> Best level: Gold
> Current quarter end: March 31st, 2026
> GOLD


我有点不敢相信自己的眼睛，因为上赛季我可是点了58个塔，提交了219个因子，我本以为可以拿下Master可以自由组Super Alpha的！！！

我赶紧在培训群中问了一下，得到小伙伴的确认后，我再也不能克服自己的情绪！为什么这样？为什么连Expert都不是，我止不住的问自己。

这是我的combine alpha performance:


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-04, October 1st, 2025
> December 31st, 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 219
> more to Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 58
> 2 more to Grandmaster
> 10
> 30
> 60
> Combined Alpha Performance
> 2.53
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas; refreshed monthly
> Combined Power Pool Alpha Performance
> -2.78


这是我的点塔情况：


> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-04, October
> 2025
> December31st 2025
>  Category
> USA
> GL
> EUR
> ASI
> CHN
> IND
> Analyst
> 10
> Droker
> Earnings
> Fundamental
> 12
> Imbalance
> Inslders
> Insttutons
> Macro
> Moael
> 14
> News
> Opton
> Other
> Price Volume
> 14
> 19
> 12
> 33
> Risk
> Senrmenr
> ShortInterest
> Social Media
> 1st


...............................................此处省略N字.............................................................................

好吧，事已至此，也只能好好总结一下问题，亡羊补牢。

首先，我推测在每一个级别的定级算法上，应该是先圈中所有达到这个级别的顾问（点塔是基本的入围标准，包括上一级别未被选中的），再根据提交的因子performance及六维累计排名得分计入最终获奖名单。我12月combine alpha performance为2.08，1月份更新后是不是2.53，这个没问题。

根本的问题出在六维上，看一下排名：


> [!NOTE] [图片 OCR 识别内容]
> Minimum 排名:
> Maximum 排名:
> 10
> entries per page
> Search:
> 下载原始JSON
> 显示/隐藏列
> 排名
> 用户ID
> 仨
> 当前等级
> 仨 三
> 达成等级
> 仨
> 三
> 最终等级
> 仨
> 三
> 国家/地区
> 1L61351
> X []
> [
> [
> [
> [
> 1077
> 1L61351
> GOLD
> master
> expert
> CN
> Consultant 基本信息
> RA Count: 274
> RA Prod Corr: 0.6043
> RA Self Corr: 0.3082
> SA Count: 1
> SA Prod Corr: 0.6031
> SA Self Corr: 0.4839
> University: Jiangxi University Of Finance And Economic
> Value Factor: 0.94
> Weight Factor: 0
> 基础信息
> Signals: 219
> Pyramids: 58
> Combined Alpha Performance: 2.53
> Combined Selected Alpha Performance: 0
> Combined Power Pool Alpha Performance: -2.78
> 六维
> Operators used: 74
> Operator AVg: 6.82
> Fields used: 282
> Field
> 2.58
> Community Activity: 0.4
> Max Simulation Streak: 133
> Gold 排名总和: 14585
> Gold Operator Count Rank: 484
> Gold Operator AVg Rank: 4485
> Gold Field Count Rank: 408
> Gold Field AVg Rank: 4105
> Gold Community Activity Rank: 3444
> Gold Max Simulation Streak Rank: 1658
> Expert 排名总和:5771
> Expert Operator Count Rank: 439
> Expert Operator
> Rank: 1454
> Expert Field Count Rank: 215
> Expert Field
> Rank:
> 290
> Expert Community Activity Rank: 1377
> Expert Max Simulation Streak Rank: 995
> Master 排名总和:2707
> Master Operator Count Rank: 350
> Master Operator
> Rank: 592
> Master Field Count Rank: 132
> Master Field Avg Rank: 540
> Master Community Activity Rank: 585
> Master Max Simulation Streak Rank: 507
> Showing
> to 1of1
> entry (filtered from 5,845 total entries)
> AVg:
> AVg
> AVS
> AVg


相比较第1个Master的排名：


> [!NOTE] [图片 OCR 识别内容]
> Consultant 基本信息
> RA Count: 1196
> RA Prod Corr: 0.5571
> RA Self Corr: 0.3382
> SA Count: 345
> SA Prod Corr: 0.5856
> SA Self Corr: 0.5402
> University: null
> Value Factor: 0.8
> Weight Factor: 22.89
> 基础信息
> Signals: 460
> Pyramids: 64
> Combined Alpha Performance: 1.83
> Combined Selected Alpha Performance: 1.56
> Combined Power Pool Alpha Performance: 1.61
> 六维
> Operators used: 155
> Operator AVg: 2.85
> Fields used: 294
> Field
> 1.11
> Community Activity: 34.1
> Max Simulation Streak: 281
> Gold 排名总和:2370
> Gold Operator Count Rank: 37
> Gold Operator
> Rank: 497
> Gold Field Count Rank: 377
> Gold Field AVg Rank: 702
> Gold Community Activity Rank: 278
> Gold Max Simulation Streak Rank: 478
> Expert 排名总和: 1096
> Expert Operator Count Rank: 37
> Expert Operator AVg Rank: 113
> Expert Field Count Rank: 195
> Expert Field
> Rank: 138
> Expert Community Activity Rank: 240
> Expert Max Simulation Streak Rank: 372
> Master 排名总和:700
> Master Operator Count Rank: 37
> Master Operator AVg Rank: 51
> Master Field Count Rank: 119
> Master Field AVg Rank: 64
> Master Community Activity Rank: 190
> Master Max Simulation Streak Rank: 238
> 76
> 5C87308
> GRANDMASTER
> master
> master
> IN
> 77
> 0P72475
> GRANDMASTER
> master
> master
> CN
> 78
> J71699
> GRANDMASTER
> master
> master
> CN
> 79
> DN41247
> MASTER
> master
> master
> VN
> 80
> AK44462
> MASTER
> master
> master
> IN
> Showing 71 to 80 of 5,845 entries
> 8
> 585
> AVg:
> AVg
> AVg


最后一个Master的排名：


> [!NOTE] [图片 OCR 识别内容]
> Consultant 基本信息
> RA Count: 1024
> RA Prod Corr: 0.6279
> RA Self Corr: 0.3863
> SA Count: 319
> SA Prod Corr: 0.6347
> SA Self Corr: 0.5524
> University: CHUKA university
> Value Factor: 0.5
> Weight Factor: 18.13
> 基础信息
> Signals: 408
> Pyramids: 80
> Combined Alpha Performance: 1.53
> Combined Selected Alpha Performance: 2.22
> Combined Power Pool Alpha Performance: 1.13
> 六维
> Operators used: 57
> Operator
> 5.3
> Fields used: 222
> Field
> 1.47
> Community Activity: 19.7
> Max Simulation Streak: 395
> Gold 排名总和:7401
> Gold Operator Count Rank: 987
> Gold Operator
> Rank: 3066
> Gold Field Count Rank: 706
> Gold Field
> Rank: 1596
> Gold Community Activity Rank: 850
> Gold Max Simulation Streak Rank: 195
> Expert 排名总和:3415
> Expert Operator Count Rank: 650
> Expert Operator Avg Rank: 1029
> Expert Field Count Rank: 423
> Expert Field
> Rank: 520
> Expert Community Activity Rank: 636
> Expert Max Simulation Streak Rank: 156
> Master 排名总和: 1969
> Master Operator Count Rank: 450
> Master Operator
> Rank: 497
> Master Field Count Rank: 261
> Master Field AVg Rank: 244
> Master Community Activity Rank: 414
> Master Max Simulation Streak Rank: 102
> Grandmaster 排名总和: 402
> Grandmaster Operator Count Rank: 89
> Grandmaster Operator
> Rank: 83
> Grandmaster Field Count Rank: 62
> Grandmaster Field
> Rank: 51
> Grandmaster Community Activity Rank: 87
> Grandmaster Max Simulation Streak Rank: 29
> AVg:
> AVg:
> AVg
> AVg
> AVg
> AVg
> AVg
> AVg


看到这些数字，我大概明白了，分指标细化总结一下：

1.Operator Count，我授予了79个operator，用了74个，下一次应该全用上。不过个Gold是比较吃亏的，因为授予operator比较少。

2.Operator Avg、Field Avg这两个指标可以合在一起，我在9月过了新人期后，PPA因子被限制了，只能一天提交一个Risk neutralization下的因子，因此，后面提交的大部份是RA，而组RA由于2 year sharpe、相关性等限制原因必然会跑二阶、三阶，导致单Alpha的Operator Avg、Field Avg增加，从而导致Rank排名较大。跑二阶、三阶引发的另一个问题是使用了太多PV数据集字段，相关数据集亮起了红灯，针对这各情况，后继的改进方案:

- 能用PPA点塔就用PPA，特别较小字段的数据集，尽量用较少的操作符和字段点塔，
- 三阶中需要增加非PV数据集字段的条件，减少PV数据集字段条件的使用。
- 为了补足Alpha数量，自有Super Alpha需要组起来。

3.Community Activity，这是个可以较快改进的问题，多参加培训，多写贴子，多跟贴！

4.Field Count Rank，没问题，注意少用重复字段点塔。

5.Max Simulation Streak，保持每天回测。

另外一个小问题，我一开始也百思不得其解，我最新的Combined Power Pool Alpha Performance: -2.78，这个同Combine Alpha Performance 2.58相差好大。


> [!NOTE] [图片 OCR 识别内容]
> Properties
> Last saved Sat, 01/10/2026,12:03 AM
> Name
> Category
> anl4_afv4_eps_high
> Analyst
> Tags
> Color
> RA &
> PowerPoolSelected %
> None
> Osmosis Points
> 1-100000
> Description
> 636/100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template。
> Idea: Exploits earnings expectations by ranking EPS forecasts Within sector groups, adjusting for market cap exposure through
> regression residual。
> Rationale for data used: Uses anl4_afv4_eps_high (highest EPS estimation) to capture analyst expectations; sector grouping for industry


直到昨天，无意中培训群中小伙伴指出了我的问题，原来我自己在提交Alpha时，按RA、ATOM、PPA打标，将PowerPoolSelected标签去除了，导致没有一个PPA被选中导致的。我重新将需要放入池中计算产出的PPA打标，相信下个月会更新为正数（所以说，没知识，多可怕！！）。

将这些小结写出来，内心也逐渐恢复平静，Gold又怎么样，收入是少了一块，想想这几个月收获的知识和方法，值得！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，大佬这个combine如此优秀，没评上GM真的是可惜了

只能说还是得重视六维

===================================================================================


---

### 技术对话片段 6 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 26年Q1 Genius定级已更新Q2赛季加油.md
- **时间**: 2个月前

**提问/主帖背景 (KH94146)**:

> [!NOTE] [图片 OCR 识别内容]
> Ganius
> 3喜报
> 2026年01季度 Genius项目定级
> 困
> 区荣誉榜
> Grand Master 级别
> Master 级别
> Expert 级别
> GRAND
> MASTER
> MASTER
> EXPERT
> 49人
> 131人
> 326人
> 获得
> 获得
> 获得
> 季度奖金:
> 季度奖金:
> 季度奖金:
> 8000
> 2000
> 200
> 25000
> 8000
> 2000
> USD
> USD
> USD
> Gonius
> Genius 定级,荣耀共享


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

向各位GM大佬看齐！争取下次也能评上GM哈哈

=============================================================================


---

### 技术对话片段 7 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 26年Q1 Genius定级已更新Q2赛季加油_39728814444695.md
- **时间**: 2个月前

**提问/主帖背景 (KH94146)**:

> [!NOTE] [图片 OCR 识别内容]
> Ganius
> 3喜报
> 2026年01季度 Genius项目定级
> 困
> 区荣誉榜
> Grand Master 级别
> Master 级别
> Expert 级别
> GRAND
> MASTER
> MASTER
> EXPERT
> 49人
> 131人
> 326人
> 获得
> 获得
> 获得
> 季度奖金:
> 季度奖金:
> 季度奖金:
> 8000
> 2000
> 200
> 25000
> 8000
> 2000
> USD
> USD
> USD
> Gonius
> Genius 定级,荣耀共享


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

向各位GM大佬看齐！争取下次也能评上GM哈哈

=============================================================================


---

### 技术对话片段 8 (原帖: 📢 AI Alpha 竞赛：提交前最终自查清单 (Final Self-Check List))
- **原帖链接**: [Commented] AI Alpha 竞赛提交前最终自查清单 Final Self-Check List.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
各位参赛选手请注意：
本次比赛评审采用  **严格标准** 。为确保您的作品能被正确受理，提交前请务必完成以下  **四项强制性自查** 。❌  **任何不符项都可能导致作品无效。**

#### ✅ 1. 环境依赖 (Dependency Management)

比赛基准环境见 requirements.txt。

- **强制要求** ：如果您的代码中使用了任何  **非标准库** （不在 requirements.txt 中）， **必须**  在 Notebook 靠前的单元格中显式包含安装命令。
- ```
  pandas
  ```
- **示例** ： `!pip install <your_package_name>`
- **自查标准** ：假设在一台全新的机器上运行您的 Notebook，它必须能自动安装依赖并跑通全流程。请特别注意，标准库中没有

#### ✅ 2. 输出文件格式 (Strict Output Schema)

程序运行结束后，必须在当前目录下生成名为 alphas.json 的文件。该文件必须是一个  **JSON 对象列表** ，且每个对象  **严格包含**  以下 5 个字段（拼写区分大小写）：

1. `"alpha_expression"`
2. `"economic_rationale"`
3. `"data_fields_used"`
4. `"operators_used"`
5. `"alpha_settings"`

- **自查标准** ：请用文本编辑器打开生成的 alphas.json，确保 Keys 与上述 5 项完全匹配，无多余字段，无拼写错误。

#### ✅ 3. LLM 使用与运行记录 (Execution Trace)

- **核心逻辑** ：Notebook 中必须明显包含调用 LLM（大语言模型）生成或优化策略的代码/提示词。
- **保留输出** ：提交的  `.ipynb`  文件  **必须保留所有单元格的运行输出 (Cell Outputs)** 。
- **自查标准** ：提交前  **切勿**  点击 "Clear All Outputs"。确保评审能看到代码执行日志和中间结果。

#### ✅ 4. 提交物与语言要求 (Submission & Language)

- **提交内容** ：必须同时提交  **演示文稿 (PPT)**  和  **Jupyter Notebook (.ipynb)** 。
- **语言要求** ：所有提交材料（包括 PPT 内容、Notebook 中的注释及 Markdown 说明） **必须使用英语** 。
- **自查标准** ：检查您的 PPT 和 Notebook，确保所有文本均为英文且表达清晰。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢weijie老师的贴心提醒

自己看了是符合要求的  AI也说全PASS了  那就交上去把

===================================================================================


---

### 技术对话片段 9 (原帖: 📢 AI Alpha 竞赛：提交前最终自查清单 (Final Self-Check List))
- **原帖链接**: https://support.worldquantbrain.com[Commented] AI Alpha 竞赛提交前最终自查清单 Final Self-Check List_38375309010327.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
各位参赛选手请注意：
本次比赛评审采用  **严格标准** 。为确保您的作品能被正确受理，提交前请务必完成以下  **四项强制性自查** 。❌  **任何不符项都可能导致作品无效。**

#### ✅ 1. 环境依赖 (Dependency Management)

比赛基准环境见 requirements.txt。

- **强制要求** ：如果您的代码中使用了任何  **非标准库** （不在 requirements.txt 中）， **必须**  在 Notebook 靠前的单元格中显式包含安装命令。
- ```
  pandas
  ```
- **示例** ： `!pip install <your_package_name>`
- **自查标准** ：假设在一台全新的机器上运行您的 Notebook，它必须能自动安装依赖并跑通全流程。请特别注意，标准库中没有

#### ✅ 2. 输出文件格式 (Strict Output Schema)

程序运行结束后，必须在当前目录下生成名为 alphas.json 的文件。该文件必须是一个  **JSON 对象列表** ，且每个对象  **严格包含**  以下 5 个字段（拼写区分大小写）：

1. `"alpha_expression"`
2. `"economic_rationale"`
3. `"data_fields_used"`
4. `"operators_used"`
5. `"alpha_settings"`

- **自查标准** ：请用文本编辑器打开生成的 alphas.json，确保 Keys 与上述 5 项完全匹配，无多余字段，无拼写错误。

#### ✅ 3. LLM 使用与运行记录 (Execution Trace)

- **核心逻辑** ：Notebook 中必须明显包含调用 LLM（大语言模型）生成或优化策略的代码/提示词。
- **保留输出** ：提交的  `.ipynb`  文件  **必须保留所有单元格的运行输出 (Cell Outputs)** 。
- **自查标准** ：提交前  **切勿**  点击 "Clear All Outputs"。确保评审能看到代码执行日志和中间结果。

#### ✅ 4. 提交物与语言要求 (Submission & Language)

- **提交内容** ：必须同时提交  **演示文稿 (PPT)**  和  **Jupyter Notebook (.ipynb)** 。
- **语言要求** ：所有提交材料（包括 PPT 内容、Notebook 中的注释及 Markdown 说明） **必须使用英语** 。
- **自查标准** ：检查您的 PPT 和 Notebook，确保所有文本均为英文且表达清晰。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢weijie老师的贴心提醒

自己看了是符合要求的  AI也说全PASS了  那就交上去把

===================================================================================


---

### 技术对话片段 10 (原帖: Antigravity插件分享--模型剩余额度实时监测经验分享)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXqQsM0iE6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAdZodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzcxODYwMjg5Mzk1NDMtQW50aWdyYXZpdHklRTYlOEYlOTIlRTQlQkIlQjYlRTUlODglODYlRTQlQkElQUItJUU2JUE4JUExJUU1JTlFJThCJUU1JTg5JUE5JUU0JUJEJTk5JUU5JUEyJTlEJUU1JUJBJUE2JUU1JUFFJTlFJUU2JTk3JUI2JUU3JTlCJTkxJUU2JUI1JThCBjsIVDoOc2VhcmNoX2lkSSIpOGE4MTkyYTItM2RmOC00NjIwLThmNWItZDI4NTg0MThjMjkyBjsIRjoJcmFua2kOOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMUk00OTI2MgY7CFQ6EnJlc3VsdHNfY291bnRpFA%3D%3D--d53a2db6bb32a90b68793a16e839081e4576e3a1
- **时间**: 5个月前

**提问/主帖背景 (GC13416)**:
此方法仅限于使用Antigravity，其他IDE理论也能用；今天冲浪发现个好东西：如图可以监测Antigravity各个模型的剩余量及模型重置时间，我觉得非常实用，分享给各位项目地址：[链接已屏蔽]插件地址：[链接已屏蔽]祝各位VF一路高涨，嘿嘿

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================感谢大佬分享，这个插件确实很好用哈哈哈只是我个人使用antigravity的时候，总是会遇到prompt执行到一半就出错的问题，大佬有类似的情况吗？===================================================================================


---

### 技术对话片段 11 (原帖: Antigravity插件分享--模型剩余额度实时监测经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Antigravity插件分享--模型剩余额度实时监测经验分享_37186028939543.md
- **时间**: 5个月前

**提问/主帖背景 (GC13416)**:
此方法仅限于使用Antigravity，其他IDE理论也能用；
今天冲浪发现个好东西： 
> [!NOTE] [图片 OCR 识别内容]
> 配置页面
> Antigravity Quota Watcher: Emabled
> Enable auto monitoring
> 配额详情
> Antgravity Quota Watcher: Polling Interal
> Polling interval (seconds)
> Antigravity 橛型颧
> 檑翠
> 剩余
> 重置[问
> Antigravity Quota Watcher: Display Style
> 状态栏显示
> Claude Opus 45 (hinking)
> 89.6% 4h 27m from now
> Status bar display style
> Claude Sonnet 45
> 89.6% 4h 27m from nOW
> percentage
> percentage
> Claude: 90%
> 6Pro: 99%
> 6 Flashi 96%
> Claude Sonnet 45 (Thinking) 89.6% 4h Z7m from now
> Antigravity Quota Watcher: Api Method
> Gemini 3 Flash
> 96.0% 4h zgm from nOw
> API Method; GET_USER_STATUS (Fu]) orCOMMAND_MODELCONFIG (Lite)
> GET_USER_STATUS
> Gemini 3
> (High)
> 99.1% 4h 32m from nOw
> Gemini 3
> (Low)
> 99.1% 4h32m from nOw
> Antigravity Quota Watcher:
> Threshold
> Warning threshold (购)
> GPT-OSS 1208 (Medium)
> 89.6% 4h 27m from nOw
> Antgraviyy Quota Watcher: Critiaal Threshold
> Critical threshold (购)
> Pro
> Pro
> Warning


如图可以监测Antigravity各个模型的剩余量及模型重置时间，我觉得非常实用，分享给各位
项目地址： [[链接已屏蔽]) 
插件地址： [[链接已屏蔽]) 

祝各位VF一路高涨，嘿嘿

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

感谢大佬分享，这个插件确实很好用哈哈哈

只是我个人使用antigravity的时候，总是会遇到prompt执行到一半就出错的问题，大佬有类似的情况吗？

===================================================================================


---

### 技术对话片段 12 (原帖: DCC 第三名经验分享经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] DCC 第三名经验分享经验分享_40957810418199.md
- **时间**: 19天前

**提问/主帖背景 (WL27618)**:
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

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享这么详细的经验贴！ 我DCC做了几个之后找不到啥信号就放弃了

祝大佬后续比赛取得好成绩

=============================================================================


---

### 技术对话片段 13 (原帖: IQC Global Final：Superalpha的OS都长什么样？论坛精选)
- **原帖链接**: [Commented] IQC Global FinalSuperalpha的OS都长什么样论坛精选.md
- **时间**: 8个月前

**提问/主帖背景 (ZS59763)**:
如题，本文记录了一些is，os，以及我的一些分析，主要是记录os，欢迎讨论

（我手机像素差，看不清的可以问顾问 JY88060 (Rank 85)要，或许有好一点的画质，更详细的讨论与总结后续会写）


> [!NOTE] [图片 OCR 识别内容]
> Solottoy Neho
> 234
> ]
> Uy
> _U



> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpo 
> Roturns
> ;
> 207
> 817
> 1;071
> II5
> 501
> MS
> 5121



> [!NOTE] [图片 OCR 识别内容]
> Chan
> IS Summan
> 539
> 1025
> 932
> 3737
> 3021
> 729.



> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpe
> Returns
> {
> 2.56
> 11.69
> 且
> 7011
> In 7021
> 7011
> 707
> 102



> [!NOTE] [图片 OCR 识别内容]
> Pnl
> 20
> !
> 10
> 50O0r
> lul  1e
> I 'I
> J T
> Jn 20
> l 20
> M 21
> Ju
> In 2
> Jul 22
> In 2
> Sharpe
> Turnovor
> Fno55
> Returns
> Orawdown
> MarBin
> 8.87
> 13.91%
> 15.12
> 40.449
> 1.349
> 58.139600
> Chart



> [!NOTE] [图片 OCR 识别内容]
> MWM
> TOam
> Sharpe
> Ro
> 0.37
> 1.78
> 50'
> 4450
> 5
> '
> NNH



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Char
> 11
> MIIIIG
> 149
> 99
> 4,46
> 20,649
> 5
> 10759
> 1



> [!NOTE] [图片 OCR 识别内容]
> 盏
> Tenm
> Sharpe
> Returns
> 0.49
> 2.63
> 021
> 0
> J 3021
> I 2025
> 00
> 宦



> [!NOTE] [图片 OCR 识别内容]
> ana
> Paamotor
> MoMVAIUo
> 415
> FIInorr
> TUTNO
> 16351
> Rowurnrtodrrro
> TU
> SIPa



> [!NOTE] [图片 OCR 识别内容]
> 8
> 
> 麈
> J202)
> Jn 2021
> J2021
> Jn 2025
> J20〉
> Team
> Sharpe
> Roturns
> Q
> 2.09
> 10007
> MANM



> [!NOTE] [图片 OCR 识别内容]
> Chan
> 15 Summan
> Kw
> 5g
> 682
> 1026
> 4379
> 305
> 128



> [!NOTE] [图片 OCR 识别内容]
> Tom
> Shurpe
> Qourus
> 
> 205
> 118
> 
> J1 .0 |
> 221
> N2
> T9 37
> 00


（没有展示is）


> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpe
> Retums
> 223
> 9.38
> 昱
> 0
> Nn 7021
> O
> Iun 7075
> 7021



> [!NOTE] [图片 OCR 识别内容]
> Chan
> ' |
> UI
> 
> IT
> U
> !
> UL
> L
> (
> CNTc
> Cce
> IS Summary
> uoo
> 465
> 772+
> 0
> 2374
> 299
> 61,47
> Cn



> [!NOTE] [图片 OCR 识别内容]
> 12
> INNIN
> 0
> 
> Kotrs
> 1.83
> 6.04
> 012021
> Jn 2021
> 0
> J0
> 0
> O
> Shrp


（没有放统计指标，大致估计，sharpe6-8，fit6-8）


> [!NOTE] [图片 OCR 识别内容]
> (
> 咖



> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpe
> Relurns
> 124
> 3,24
> 量
> M021
> M 7021
> 1702
> J09
> 0
> NNN



> [!NOTE] [图片 OCR 识别内容]
> In Sample Metrics
> R
> 6.56
> 8.48%
> 10.50
> Rturn
> Ordonn
> Wupn
> 32.0396
> 2.3296
> 75.569oo
> N Chart
> Pnl
> Comparison with Equal Weightage
> 639
> 1499
> 10.06
> 37.134
> 2579
> 49550
> TONI
> SOJOK
> hng
> Jn '20
> Jn 21
> JJn
> In 2
> Combo Pnl
> Equol Welgh( Pnl
>  Donchmork Pnl
> ShICe
> TurnOs



> [!NOTE] [图片 OCR 识别内容]
> Tenm
> Sharpe
> Roturns
> 
> 2.17
> 6.71
> 1
> 」
> J1 2071
> Jn 2021
> O
> 0n7023
> 14 2025



> [!NOTE] [图片 OCR 识别内容]
> Chn
> Ol
> 849
> 1587
> 4208
> 89 ^
> 9903
> 855



> [!NOTE] [图片 OCR 识别内容]
> Toam
> Shorpo
> 541440028
> 00〉


os无疑是让人十分震撼的，针对展示的os总结，有如下两点：

①garbage in, garbage out，最后一位选手的ra多数使用tradewhen运算符，拉到十年的数据往往对半，乃至为负。如果底层逻辑本质上是过拟合与数据窥探的产物，其os不得不令人担忧

②diversity, diversity, diversity，几乎每个sa都包含这个topic，不论是从production的diversity，还是从思路，运算符，category的diversity，高度的分散是极其重要的，quantity makes quality。

③如果把os和美国股市的涨跌幅结合来看，在2024年1月末，2025年年初均跟市场走势有一定相关性。虽说alpha是做过中性化，但据选手反馈，只能使用四个基础的中性化。因此，在sa中使用风险中性化显得更为必要。

最后，提出一个讨论，能看到的，os乱走的sa，其sharpe和fit往往差距甚大，甚至到翻倍的地步，这种差距是否暗示着某种过拟合？日常做sa是否要尽可能控制这两个指标相对一致？sharpe和fit差异巨大的ra往往会包含某方面的极端情况，sa是否也是这样？

针对sa的进一步详细讨论会在后续发出。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

感谢大佬分享，虽然没资格参加IQC，但看到这些NB的SA还是惊叹自己和大佬之间的差距还是好大哈哈

===================================================================================


---

### 技术对话片段 14 (原帖: IQC Global Final：Superalpha的OS都长什么样？论坛精选)
- **原帖链接**: https://support.worldquantbrain.com[Commented] IQC Global FinalSuperalpha的OS都长什么样论坛精选_35377525887255.md
- **时间**: 8个月前

**提问/主帖背景 (ZS59763)**:
如题，本文记录了一些is，os，以及我的一些分析，主要是记录os，欢迎讨论

（我手机像素差，看不清的可以问顾问 JY88060 (Rank 85)要，或许有好一点的画质，更详细的讨论与总结后续会写）


> [!NOTE] [图片 OCR 识别内容]
> Solottoy Neho
> 234
> ]
> Uy
> _U



> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpo 
> Roturns
> ;
> 207
> 817
> 1;071
> II5
> 501
> MS
> 5121



> [!NOTE] [图片 OCR 识别内容]
> Chan
> IS Summan
> 539
> 1025
> 932
> 3737
> 3021
> 729.



> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpe
> Returns
> {
> 2.56
> 11.69
> 且
> 7011
> In 7021
> 7011
> 707
> 102



> [!NOTE] [图片 OCR 识别内容]
> Pnl
> 20
> !
> 10
> 50O0r
> lul  1e
> I 'I
> J T
> Jn 20
> l 20
> M 21
> Ju
> In 2
> Jul 22
> In 2
> Sharpe
> Turnovor
> Fno55
> Returns
> Orawdown
> MarBin
> 8.87
> 13.91%
> 15.12
> 40.449
> 1.349
> 58.139600
> Chart



> [!NOTE] [图片 OCR 识别内容]
> MWM
> TOam
> Sharpe
> Ro
> 0.37
> 1.78
> 50'
> 4450
> 5
> '
> NNH



> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Char
> 11
> MIIIIG
> 149
> 99
> 4,46
> 20,649
> 5
> 10759
> 1



> [!NOTE] [图片 OCR 识别内容]
> 盏
> Tenm
> Sharpe
> Returns
> 0.49
> 2.63
> 021
> 0
> J 3021
> I 2025
> 00
> 宦



> [!NOTE] [图片 OCR 识别内容]
> ana
> Paamotor
> MoMVAIUo
> 415
> FIInorr
> TUTNO
> 16351
> Rowurnrtodrrro
> TU
> SIPa



> [!NOTE] [图片 OCR 识别内容]
> 8
> 
> 麈
> J202)
> Jn 2021
> J2021
> Jn 2025
> J20〉
> Team
> Sharpe
> Roturns
> Q
> 2.09
> 10007
> MANM



> [!NOTE] [图片 OCR 识别内容]
> Chan
> 15 Summan
> Kw
> 5g
> 682
> 1026
> 4379
> 305
> 128



> [!NOTE] [图片 OCR 识别内容]
> Tom
> Shurpe
> Qourus
> 
> 205
> 118
> 
> J1 .0 |
> 221
> N2
> T9 37
> 00


（没有展示is）


> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpe
> Retums
> 223
> 9.38
> 昱
> 0
> Nn 7021
> O
> Iun 7075
> 7021



> [!NOTE] [图片 OCR 识别内容]
> Chan
> ' |
> UI
> 
> IT
> U
> !
> UL
> L
> (
> CNTc
> Cce
> IS Summary
> uoo
> 465
> 772+
> 0
> 2374
> 299
> 61,47
> Cn



> [!NOTE] [图片 OCR 识别内容]
> 12
> INNIN
> 0
> 
> Kotrs
> 1.83
> 6.04
> 012021
> Jn 2021
> 0
> J0
> 0
> O
> Shrp


（没有放统计指标，大致估计，sharpe6-8，fit6-8）


> [!NOTE] [图片 OCR 识别内容]
> (
> 咖



> [!NOTE] [图片 OCR 识别内容]
> Team
> Sharpe
> Relurns
> 124
> 3,24
> 量
> M021
> M 7021
> 1702
> J09
> 0
> NNN



> [!NOTE] [图片 OCR 识别内容]
> In Sample Metrics
> R
> 6.56
> 8.48%
> 10.50
> Rturn
> Ordonn
> Wupn
> 32.0396
> 2.3296
> 75.569oo
> N Chart
> Pnl
> Comparison with Equal Weightage
> 639
> 1499
> 10.06
> 37.134
> 2579
> 49550
> TONI
> SOJOK
> hng
> Jn '20
> Jn 21
> JJn
> In 2
> Combo Pnl
> Equol Welgh( Pnl
>  Donchmork Pnl
> ShICe
> TurnOs



> [!NOTE] [图片 OCR 识别内容]
> Tenm
> Sharpe
> Roturns
> 
> 2.17
> 6.71
> 1
> 」
> J1 2071
> Jn 2021
> O
> 0n7023
> 14 2025



> [!NOTE] [图片 OCR 识别内容]
> Chn
> Ol
> 849
> 1587
> 4208
> 89 ^
> 9903
> 855



> [!NOTE] [图片 OCR 识别内容]
> Toam
> Shorpo
> 541440028
> 00〉


os无疑是让人十分震撼的，针对展示的os总结，有如下两点：

①garbage in, garbage out，最后一位选手的ra多数使用tradewhen运算符，拉到十年的数据往往对半，乃至为负。如果底层逻辑本质上是过拟合与数据窥探的产物，其os不得不令人担忧

②diversity, diversity, diversity，几乎每个sa都包含这个topic，不论是从production的diversity，还是从思路，运算符，category的diversity，高度的分散是极其重要的，quantity makes quality。

③如果把os和美国股市的涨跌幅结合来看，在2024年1月末，2025年年初均跟市场走势有一定相关性。虽说alpha是做过中性化，但据选手反馈，只能使用四个基础的中性化。因此，在sa中使用风险中性化显得更为必要。

最后，提出一个讨论，能看到的，os乱走的sa，其sharpe和fit往往差距甚大，甚至到翻倍的地步，这种差距是否暗示着某种过拟合？日常做sa是否要尽可能控制这两个指标相对一致？sharpe和fit差异巨大的ra往往会包含某方面的极端情况，sa是否也是这样？

针对sa的进一步详细讨论会在后续发出。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

感谢大佬分享，虽然没资格参加IQC，但看到这些NB的SA还是惊叹自己和大佬之间的差距还是好大哈哈

===================================================================================


---

### 技术对话片段 15 (原帖: MCP回测超时的一种解决办法代码优化)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX%2FGlOeR86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAbJodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzQ2MDU4NjcwNzI2NjMtTUNQJUU1JTlCJTlFJUU2JUI1JThCJUU4JUI2JTg1JUU2JTk3JUI2JUU3JTlBJTg0JUU0JUI4JTgwJUU3JUE3JThEJUU4JUE3JUEzJUU1JTg2JUIzJUU1JThBJTlFJUU2JUIzJTk1BjsIVDoOc2VhcmNoX2lkSSIpNTkzNzk1NDYtNjI0NS00ZGQzLTlmZmMtY2NiODJlMWQ3YzkyBjsIRjoJcmFua2kKOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMUk00OTI2MgY7CFQ6EnJlc3VsdHNfY291bnRpFA%3D%3D--74923ddb8520fc856ab19729774b1102cd156b11
- **时间**: 9个月前

**提问/主帖背景 (WF37935)**:
我使用gemini cli回测alpha会出现超时的情况，研究后发现可能是因为gemini cli调用mcp的时候有内置的超时时间，大概30秒左右，而回测至少也得几分钟时间。看了官方文档问了AI也没找到能改变超时时间的办法，后来想了个方法，把回测的代码改一下就可以了。官方自带的回测方法create_multiSim包含了三个部分：发送回测请求，获取回测进度，回测完成后获取回测结果，根据这个把create_multiSim拆分成三个方法。发送回测请求和回测完成后获取回测结果一般都很快，关键就是获取回测进度，这个方法中，我并不会等到回测完成，而是设置了重试次数，目前是８次，而每次回测worldquant都会给我们返回Retry-After,是2.5秒，这样每次执行时间严格控制在30秒之内，基本上就不会有回测超时的问题了。代码如下：@mcp.tool()async def create_multiSim(alpha_expressions: List[str],instrument_type: str = "EQUITY",region: str = "USA",universe: str = "TOP3000",delay: int = 1,decay: int = 0,neutralization: str = "NONE",truncation: float = 0.0,test_period: str = "P0Y0M",unit_handling: str = "VERIFY",nan_handling: str = "OFF",language: str = "FASTEXPR",visualization: bool = False,pasteurization: str = "ON",max_trade: str = "OFF") -> Dict[str, Any]:"""🚀 Create multiple regular alpha simulations on BRAIN platform in a single request.This tool creates a multisimulation with multiple regular alpha expressions,waits for all simulations to complete, and returns detailed results for each alpha.⏰ NOTE: Multisimulations can take 8+ minutes to complete. This tool will waitfor the entire process and return comprehensive results.Call get_platform_setting_options to get the valid options for the simulation.Args:alpha_expressions: List of alpha expressions (2-8 expressions required)instrument_type: Type of instruments (default: "EQUITY")region: Market region (default: "USA")universe: Universe of stocks (default: "TOP3000")delay: Data delay (default: 1)decay: Decay value (default: 0)neutralization: Neutralization method (default: "NONE")truncation: Truncation value (default: 0.0)test_period: Test period (default: "P0Y0M")unit_handling: Unit handling method (default: "VERIFY")nan_handling: NaN handling method (default: "OFF")language: Expression language (default: "FASTEXPR")visualization: Enable visualization (default: True)pasteurization: Pasteurization setting (default: "ON")max_trade: Max trade setting (default: "OFF")Returns:Dictionary containing multisimulation status.If multisimulation is compelted, call get_multisimulation_result to get individual alpha details"""try:logger.info('create_multiSim start')# Validate inputif len(alpha_expressions) < 2:return {"error": "At least 2 alpha expressions are required"}if len(alpha_expressions) > 8:return {"error": "Maximum 8 alpha expressions allowed per request"}# Create multisimulation datamultisimulation_data = []for alpha_expr in alpha_expressions:simulation_item = {'type': 'REGULAR','settings': {'instrumentType': instrument_type,'region': region,'universe': universe,'delay': delay,'decay': decay,'neutralization': neutralization,'truncation': truncation,'pasteurization': pasteurization,'unitHandling': unit_handling,'nanHandling': nan_handling,'language': language,'visualization': visualization,# 'testPeriod': test_period,'testPeriod': 'P0Y','maxTrade': max_trade},'regular': alpha_expr}multisimulation_data.append(simulation_item)logger.info(multisimulation_data)# Send multisimulation requestresponse = brain_client.session.post(f"{brain_client.base_url}/simulations", json=multisimulation_data)start_time = time.time()start_time_formatted = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')logger.info(f"multisimulate start at {start_time_formatted}")logger.info(response.content)if response.status_code != 201:if response.status_code == 429:logger.warning("Rate limit exceeded")return {"error": f"Too Many Requests! You should stop and ask the user to try again later."}else:return {"error": f"Failed to create multisimulation. Status: {response.status_code},, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}# Get multisimulation locationlocation = response.headers.get('Location', '')if not location:return {"error": "No location header in multisimulation response"}logger.info(f'location: {location}')# Wait for children to appear and get resultsreturn await check_multisimulation_status(start_time, location, len(alpha_expressions))except Exception as e:return {"error": f"Error creating multisimulation: {str(e)}, , you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def check_multisimulation_status(start_time: float, location: str, expected_children: int) -> Dict[str, Any]:"""check multisimulation status: in progess, completed or error"""try:# Simple progress indicator for userslogger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")logger.info(f"Expected {expected_children} alpha simulations")print()# Wait for children to appear - much more tolerant for 8+ minute multisimulationschildren = []max_wait_attempts = 8  # Increased significantly for 8+ minute multisimulationswait_attempt = 0while wait_attempt < max_wait_attempts and len(children) == 0:wait_attempt += 1try:multisim_response = brain_client.session.get(location)if multisim_response.status_code == 200:multisim_data = multisim_response.json()children = multisim_data.get('children', [])if children:breakelse:# Wait before next attempt - use longer intervals for multisimulationsretry_after = multisim_response.headers.get("Retry-After", 5)logger.info(f'waiting for multiSim completion, sleeping {retry_after}s')wait_time = float(retry_after)await asyncio.sleep(wait_time)else:await asyncio.sleep(5)except Exception as e:await asyncio.sleep(5)if not children:current_time = time.time()elapsed = (current_time - start_time) / 60return {"status": "in_progress","message": "wait for one minute and call check_multisimulation_status","start_time": start_time,"location": location,"expected_children": expected_children,"note": f"multisimulation last for {elapsed} minutes, if longer than 15 minutes, stop and ask the user"}else:status = multisim_response.json().get("status", 0)if status == 'ERROR':return {"status": "error","message": "call get_SimError_detail for the error detail","location": location}elif status == 'COMPLETE':return {"status": "completed","message": "multisimulation finished, you should call get_multisimulation_result to get result","location": location,"expected_children": expected_children}else:return {"status": "undefined status", "message": "you should stop and ask the user about this situation"}except Exception as e:return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def get_multisimulation_result(location: str, expected_children: int) -> Dict[str, Any]:"""After multisimulation completed, return results"""try:# Simple progress indicator for userslogger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")logger.info(f"Expected {expected_children} alpha simulations")print()# Wait for children to appear - much more tolerant for 8+ minute multisimulationschildren = []try:multisim_response = brain_client.session.get(location)if multisim_response.status_code == 200:multisim_data = multisim_response.json()children = multisim_data.get('children', [])if not children:return {"error": f"Children did not appear (multisimulation may still be processing)"}except Exception as e:logger.info(f'waiting for completion error: {e}')await asyncio.sleep(5)logger.info('multiSimulate complete, getting children information...')# Process each child to get alpha resultsalpha_results = []for i, child_id in enumerate(children):try:# The children are full URLs, not just IDschild_url = child_id if child_id.startswith('http') else f"{brain_client.base_url}/simulations/{child_id}"# Wait for this alpha to complete - more tolerant timingfinished = Falsemax_alpha_attempts = 100  # Increased for longer alpha processingalpha_attempt = 0while not finished and alpha_attempt < max_alpha_attempts:alpha_attempt += 1try:alpha_progress = brain_client.session.get(child_url)if alpha_progress.status_code == 200:alpha_data = alpha_progress.json()retry_after = alpha_progress.headers.get("Retry-After", 0)if retry_after == 0:finished = Truebreakelse:wait_time = float(retry_after)await asyncio.sleep(wait_time)else:await asyncio.sleep(5)except Exception as e:await asyncio.sleep(5)if finished:# Get alpha details from the completed simulationalpha_id = alpha_data.get("alpha")if alpha_id:# Now get the actual alpha details from the alpha endpointalpha_details = brain_client.session.get(f"{brain_client.base_url}/alphas/{alpha_id}")if alpha_details.status_code == 200:alpha_detail_data = alpha_details.json()alpha_results.append({'alpha_id': alpha_id,'location': child_url,'details': alpha_detail_data})else:alpha_results.append({'alpha_id': alpha_id,'location': child_url,'error': f'Failed to get alpha details: {alpha_details.status_code}'})else:alpha_results.append({'location': child_url,'error': 'No alpha ID found in completed simulation'})else:alpha_results.append({'location': child_url,'error': f'Alpha simulation did not complete within {max_alpha_attempts} attempts'})except Exception as e:alpha_results.append({'location': f"child_{i+1}",'error': str(e)})# Return comprehensive resultslogger.info(f"Multisimulation completed! Retrieved {len(alpha_results)} alpha results")return {'success': True,'message': f'Successfully created {expected_children} regular alpha simulations','total_requested': expected_children,'total_created': len(alpha_results),'multisimulation_id': location.split('/')[-1],'multisimulation_location': location,'alpha_results': alpha_results,'note': "if you got a negative alpha sharpe, you can just add a minus sign in front of the last line of the Alpha to flip then think the next step."}except Exception as e:return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}

**顾问 RM49262 (Rank 30) 的解答与建议**:
巧了我今天下午也在研究为啥Gemini Cli调用MCP超时，我看他们Github页面已经有不少人提了Issue，貌似现在这个版本的Gemini Cli有bug会无视MCP设置里的Timeout，希望下个版本能修复吧！ 也感谢大佬给出新的解决方案


---

### 技术对话片段 16 (原帖: MCP回测超时的一种解决办法代码优化)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX%2FGlOeR86D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAbJodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzQ2MDU4NjcwNzI2NjMtTUNQJUU1JTlCJTlFJUU2JUI1JThCJUU4JUI2JTg1JUU2JTk3JUI2JUU3JTlBJTg0JUU0JUI4JTgwJUU3JUE3JThEJUU4JUE3JUEzJUU1JTg2JUIzJUU1JThBJTlFJUU2JUIzJTk1BjsIVDoOc2VhcmNoX2lkSSIpNTkzNzk1NDYtNjI0NS00ZGQzLTlmZmMtY2NiODJlMWQ3YzkyBjsIRjoJcmFua2kKOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMUk00OTI2MgY7CFQ6EnJlc3VsdHNfY291bnRpFA%3D%3D--74923ddb8520fc856ab19729774b1102cd156b11
- **时间**: 9个月前

**提问/主帖背景 (WF37935)**:
我使用gemini cli回测alpha会出现超时的情况，研究后发现可能是因为gemini cli调用mcp的时候有内置的超时时间，大概30秒左右，而回测至少也得几分钟时间。看了官方文档问了AI也没找到能改变超时时间的办法，后来想了个方法，把回测的代码改一下就可以了。官方自带的回测方法create_multiSim包含了三个部分：发送回测请求，获取回测进度，回测完成后获取回测结果，根据这个把create_multiSim拆分成三个方法。发送回测请求和回测完成后获取回测结果一般都很快，关键就是获取回测进度，这个方法中，我并不会等到回测完成，而是设置了重试次数，目前是８次，而每次回测worldquant都会给我们返回Retry-After,是2.5秒，这样每次执行时间严格控制在30秒之内，基本上就不会有回测超时的问题了。代码如下：@mcp.tool()async def create_multiSim(alpha_expressions: List[str],instrument_type: str = "EQUITY",region: str = "USA",universe: str = "TOP3000",delay: int = 1,decay: int = 0,neutralization: str = "NONE",truncation: float = 0.0,test_period: str = "P0Y0M",unit_handling: str = "VERIFY",nan_handling: str = "OFF",language: str = "FASTEXPR",visualization: bool = False,pasteurization: str = "ON",max_trade: str = "OFF") -> Dict[str, Any]:"""🚀 Create multiple regular alpha simulations on BRAIN platform in a single request.This tool creates a multisimulation with multiple regular alpha expressions,waits for all simulations to complete, and returns detailed results for each alpha.⏰ NOTE: Multisimulations can take 8+ minutes to complete. This tool will waitfor the entire process and return comprehensive results.Call get_platform_setting_options to get the valid options for the simulation.Args:alpha_expressions: List of alpha expressions (2-8 expressions required)instrument_type: Type of instruments (default: "EQUITY")region: Market region (default: "USA")universe: Universe of stocks (default: "TOP3000")delay: Data delay (default: 1)decay: Decay value (default: 0)neutralization: Neutralization method (default: "NONE")truncation: Truncation value (default: 0.0)test_period: Test period (default: "P0Y0M")unit_handling: Unit handling method (default: "VERIFY")nan_handling: NaN handling method (default: "OFF")language: Expression language (default: "FASTEXPR")visualization: Enable visualization (default: True)pasteurization: Pasteurization setting (default: "ON")max_trade: Max trade setting (default: "OFF")Returns:Dictionary containing multisimulation status.If multisimulation is compelted, call get_multisimulation_result to get individual alpha details"""try:logger.info('create_multiSim start')# Validate inputif len(alpha_expressions) < 2:return {"error": "At least 2 alpha expressions are required"}if len(alpha_expressions) > 8:return {"error": "Maximum 8 alpha expressions allowed per request"}# Create multisimulation datamultisimulation_data = []for alpha_expr in alpha_expressions:simulation_item = {'type': 'REGULAR','settings': {'instrumentType': instrument_type,'region': region,'universe': universe,'delay': delay,'decay': decay,'neutralization': neutralization,'truncation': truncation,'pasteurization': pasteurization,'unitHandling': unit_handling,'nanHandling': nan_handling,'language': language,'visualization': visualization,# 'testPeriod': test_period,'testPeriod': 'P0Y','maxTrade': max_trade},'regular': alpha_expr}multisimulation_data.append(simulation_item)logger.info(multisimulation_data)# Send multisimulation requestresponse = brain_client.session.post(f"{brain_client.base_url}/simulations", json=multisimulation_data)start_time = time.time()start_time_formatted = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')logger.info(f"multisimulate start at {start_time_formatted}")logger.info(response.content)if response.status_code != 201:if response.status_code == 429:logger.warning("Rate limit exceeded")return {"error": f"Too Many Requests! You should stop and ask the user to try again later."}else:return {"error": f"Failed to create multisimulation. Status: {response.status_code},, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}# Get multisimulation locationlocation = response.headers.get('Location', '')if not location:return {"error": "No location header in multisimulation response"}logger.info(f'location: {location}')# Wait for children to appear and get resultsreturn await check_multisimulation_status(start_time, location, len(alpha_expressions))except Exception as e:return {"error": f"Error creating multisimulation: {str(e)}, , you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def check_multisimulation_status(start_time: float, location: str, expected_children: int) -> Dict[str, Any]:"""check multisimulation status: in progess, completed or error"""try:# Simple progress indicator for userslogger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")logger.info(f"Expected {expected_children} alpha simulations")print()# Wait for children to appear - much more tolerant for 8+ minute multisimulationschildren = []max_wait_attempts = 8  # Increased significantly for 8+ minute multisimulationswait_attempt = 0while wait_attempt < max_wait_attempts and len(children) == 0:wait_attempt += 1try:multisim_response = brain_client.session.get(location)if multisim_response.status_code == 200:multisim_data = multisim_response.json()children = multisim_data.get('children', [])if children:breakelse:# Wait before next attempt - use longer intervals for multisimulationsretry_after = multisim_response.headers.get("Retry-After", 5)logger.info(f'waiting for multiSim completion, sleeping {retry_after}s')wait_time = float(retry_after)await asyncio.sleep(wait_time)else:await asyncio.sleep(5)except Exception as e:await asyncio.sleep(5)if not children:current_time = time.time()elapsed = (current_time - start_time) / 60return {"status": "in_progress","message": "wait for one minute and call check_multisimulation_status","start_time": start_time,"location": location,"expected_children": expected_children,"note": f"multisimulation last for {elapsed} minutes, if longer than 15 minutes, stop and ask the user"}else:status = multisim_response.json().get("status", 0)if status == 'ERROR':return {"status": "error","message": "call get_SimError_detail for the error detail","location": location}elif status == 'COMPLETE':return {"status": "completed","message": "multisimulation finished, you should call get_multisimulation_result to get result","location": location,"expected_children": expected_children}else:return {"status": "undefined status", "message": "you should stop and ask the user about this situation"}except Exception as e:return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def get_multisimulation_result(location: str, expected_children: int) -> Dict[str, Any]:"""After multisimulation completed, return results"""try:# Simple progress indicator for userslogger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")logger.info(f"Expected {expected_children} alpha simulations")print()# Wait for children to appear - much more tolerant for 8+ minute multisimulationschildren = []try:multisim_response = brain_client.session.get(location)if multisim_response.status_code == 200:multisim_data = multisim_response.json()children = multisim_data.get('children', [])if not children:return {"error": f"Children did not appear (multisimulation may still be processing)"}except Exception as e:logger.info(f'waiting for completion error: {e}')await asyncio.sleep(5)logger.info('multiSimulate complete, getting children information...')# Process each child to get alpha resultsalpha_results = []for i, child_id in enumerate(children):try:# The children are full URLs, not just IDschild_url = child_id if child_id.startswith('http') else f"{brain_client.base_url}/simulations/{child_id}"# Wait for this alpha to complete - more tolerant timingfinished = Falsemax_alpha_attempts = 100  # Increased for longer alpha processingalpha_attempt = 0while not finished and alpha_attempt < max_alpha_attempts:alpha_attempt += 1try:alpha_progress = brain_client.session.get(child_url)if alpha_progress.status_code == 200:alpha_data = alpha_progress.json()retry_after = alpha_progress.headers.get("Retry-After", 0)if retry_after == 0:finished = Truebreakelse:wait_time = float(retry_after)await asyncio.sleep(wait_time)else:await asyncio.sleep(5)except Exception as e:await asyncio.sleep(5)if finished:# Get alpha details from the completed simulationalpha_id = alpha_data.get("alpha")if alpha_id:# Now get the actual alpha details from the alpha endpointalpha_details = brain_client.session.get(f"{brain_client.base_url}/alphas/{alpha_id}")if alpha_details.status_code == 200:alpha_detail_data = alpha_details.json()alpha_results.append({'alpha_id': alpha_id,'location': child_url,'details': alpha_detail_data})else:alpha_results.append({'alpha_id': alpha_id,'location': child_url,'error': f'Failed to get alpha details: {alpha_details.status_code}'})else:alpha_results.append({'location': child_url,'error': 'No alpha ID found in completed simulation'})else:alpha_results.append({'location': child_url,'error': f'Alpha simulation did not complete within {max_alpha_attempts} attempts'})except Exception as e:alpha_results.append({'location': f"child_{i+1}",'error': str(e)})# Return comprehensive resultslogger.info(f"Multisimulation completed! Retrieved {len(alpha_results)} alpha results")return {'success': True,'message': f'Successfully created {expected_children} regular alpha simulations','total_requested': expected_children,'total_created': len(alpha_results),'multisimulation_id': location.split('/')[-1],'multisimulation_location': location,'alpha_results': alpha_results,'note': "if you got a negative alpha sharpe, you can just add a minus sign in front of the last line of the Alpha to flip then think the next step."}except Exception as e:return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}

**顾问 RM49262 (Rank 30) 的解答与建议**:
今天测试了一下，新版本Gemini Cli已经修复这个问题了，目前可以正常调用回测工具了。感谢楼主的代码让我学到了新思路！---------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 17 (原帖: MCP回测超时的一种解决办法代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] MCP回测超时的一种解决办法代码优化_34605867072663.md
- **时间**: 9个月前

**提问/主帖背景 (WF37935)**:
我使用gemini cli回测alpha会出现超时的情况，研究后发现可能是因为gemini cli调用mcp的时候有内置的超时时间，大概30秒左右，而回测至少也得几分钟时间。看了官方文档问了AI也没找到能改变超时时间的办法，后来想了个方法，把回测的代码改一下就可以了。

官方自带的回测方法create_multiSim包含了三个部分：发送回测请求，获取回测进度，回测完成后获取回测结果，根据这个把create_multiSim拆分成三个方法。发送回测请求和回测完成后获取回测结果一般都很快，关键就是获取回测进度，这个方法中，我并不会等到回测完成，而是设置了重试次数，目前是８次，而每次回测worldquant都会给我们返回Retry-After,是2.5秒，这样每次执行时间严格控制在30秒之内，基本上就不会有回测超时的问题了。

代码如下：

```
@mcp.tool()async def create_multiSim(    alpha_expressions: List[str],    instrument_type: str = "EQUITY",    region: str = "USA",    universe: str = "TOP3000",    delay: int = 1,    decay: int = 0,    neutralization: str = "NONE",    truncation: float = 0.0,    test_period: str = "P0Y0M",    unit_handling: str = "VERIFY",    nan_handling: str = "OFF",    language: str = "FASTEXPR",    visualization: bool = False,    pasteurization: str = "ON",    max_trade: str = "OFF") -> Dict[str, Any]:    """    🚀 Create multiple regular alpha simulations on BRAIN platform in a single request.        This tool creates a multisimulation with multiple regular alpha expressions,    waits for all simulations to complete, and returns detailed results for each alpha.        ⏰ NOTE: Multisimulations can take 8+ minutes to complete. This tool will wait    for the entire process and return comprehensive results.    Call get_platform_setting_options to get the valid options for the simulation.    Args:        alpha_expressions: List of alpha expressions (2-8 expressions required)        instrument_type: Type of instruments (default: "EQUITY")        region: Market region (default: "USA")        universe: Universe of stocks (default: "TOP3000")        delay: Data delay (default: 1)        decay: Decay value (default: 0)        neutralization: Neutralization method (default: "NONE")        truncation: Truncation value (default: 0.0)        test_period: Test period (default: "P0Y0M")        unit_handling: Unit handling method (default: "VERIFY")        nan_handling: NaN handling method (default: "OFF")        language: Expression language (default: "FASTEXPR")        visualization: Enable visualization (default: True)        pasteurization: Pasteurization setting (default: "ON")        max_trade: Max trade setting (default: "OFF")        Returns:        Dictionary containing multisimulation status.         If multisimulation is compelted, call get_multisimulation_result to get individual alpha details    """    try:        logger.info('create_multiSim start')        # Validate input        if len(alpha_expressions) < 2:            return {"error": "At least 2 alpha expressions are required"}        if len(alpha_expressions) > 8:            return {"error": "Maximum 8 alpha expressions allowed per request"}                # Create multisimulation data        multisimulation_data = []        for alpha_expr in alpha_expressions:            simulation_item = {                'type': 'REGULAR',                'settings': {                    'instrumentType': instrument_type,                    'region': region,                    'universe': universe,                    'delay': delay,                    'decay': decay,                    'neutralization': neutralization,                    'truncation': truncation,                    'pasteurization': pasteurization,                    'unitHandling': unit_handling,                    'nanHandling': nan_handling,                    'language': language,                    'visualization': visualization,                    # 'testPeriod': test_period,                    'testPeriod': 'P0Y',                    'maxTrade': max_trade                },                'regular': alpha_expr            }            multisimulation_data.append(simulation_item)                logger.info(multisimulation_data)        # Send multisimulation request        response = brain_client.session.post(f"{brain_client.base_url}/simulations", json=multisimulation_data)        start_time = time.time()        start_time_formatted = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')        logger.info(f"multisimulate start at {start_time_formatted}")        logger.info(response.content)                if response.status_code != 201:            if response.status_code == 429:                logger.warning("Rate limit exceeded")                return {"error": f"Too Many Requests! You should stop and ask the user to try again later."}            else:                return {                    "error": f"Failed to create multisimulation. Status: {response.status_code},, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}                # Get multisimulation location        location = response.headers.get('Location', '')        if not location:            return {"error": "No location header in multisimulation response"}        logger.info(f'location: {location}')                # Wait for children to appear and get results        return await check_multisimulation_status(start_time, location, len(alpha_expressions))             except Exception as e:        return {"error": f"Error creating multisimulation: {str(e)}, , you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def check_multisimulation_status(start_time: float, location: str, expected_children: int) -> Dict[str, Any]:    """check multisimulation status: in progess, completed or error"""    try:        # Simple progress indicator for users        logger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")        logger.info(f"Expected {expected_children} alpha simulations")        print()        # Wait for children to appear - much more tolerant for 8+ minute multisimulations        children = []        max_wait_attempts = 8  # Increased significantly for 8+ minute multisimulations        wait_attempt = 0                while wait_attempt < max_wait_attempts and len(children) == 0:            wait_attempt += 1                        try:                multisim_response = brain_client.session.get(location)                if multisim_response.status_code == 200:                    multisim_data = multisim_response.json()                    children = multisim_data.get('children', [])                                        if children:                        break                    else:                        # Wait before next attempt - use longer intervals for multisimulations                        retry_after = multisim_response.headers.get("Retry-After", 5)                        logger.info(f'waiting for multiSim completion, sleeping {retry_after}s')                        wait_time = float(retry_after)                        await asyncio.sleep(wait_time)                else:                    await asyncio.sleep(5)            except Exception as e:                await asyncio.sleep(5)                if not children:            current_time = time.time()            elapsed = (current_time - start_time) / 60            return {                "status": "in_progress",                 "message": "wait for one minute and call check_multisimulation_status",                "start_time": start_time,                "location": location,                "expected_children": expected_children,                "note": f"multisimulation last for {elapsed} minutes, if longer than 15 minutes, stop and ask the user"             }        else:            status = multisim_response.json().get("status", 0)            if status == 'ERROR':                return {                    "status": "error",                     "message": "call get_SimError_detail for the error detail",                    "location": location                    }            elif status == 'COMPLETE':                return {                    "status": "completed",                     "message": "multisimulation finished, you should call get_multisimulation_result to get result",                    "location": location,                    "expected_children": expected_children                 }            else:                return {"status": "undefined status", "message": "you should stop and ask the user about this situation"}    except Exception as e:        return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def get_multisimulation_result(location: str, expected_children: int) -> Dict[str, Any]:    """After multisimulation completed, return results"""    try:        # Simple progress indicator for users        logger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")        logger.info(f"Expected {expected_children} alpha simulations")        print()        # Wait for children to appear - much more tolerant for 8+ minute multisimulations        children = []                    try:            multisim_response = brain_client.session.get(location)            if multisim_response.status_code == 200:                multisim_data = multisim_response.json()                children = multisim_data.get('children', [])                if not children:                    return {"error": f"Children did not appear (multisimulation may still be processing)"}        except Exception as e:            logger.info(f'waiting for completion error: {e}')            await asyncio.sleep(5)        logger.info('multiSimulate complete, getting children information...')                # Process each child to get alpha results        alpha_results = []        for i, child_id in enumerate(children):            try:                # The children are full URLs, not just IDs                child_url = child_id if child_id.startswith('http') else f"{brain_client.base_url}/simulations/{child_id}"                                # Wait for this alpha to complete - more tolerant timing                finished = False                max_alpha_attempts = 100  # Increased for longer alpha processing                alpha_attempt = 0                                while not finished and alpha_attempt < max_alpha_attempts:                    alpha_attempt += 1                                        try:                        alpha_progress = brain_client.session.get(child_url)                        if alpha_progress.status_code == 200:                            alpha_data = alpha_progress.json()                            retry_after = alpha_progress.headers.get("Retry-After", 0)                                                        if retry_after == 0:                                finished = True                                break                            else:                                wait_time = float(retry_after)                                await asyncio.sleep(wait_time)                        else:                            await asyncio.sleep(5)                    except Exception as e:                        await asyncio.sleep(5)                                if finished:                    # Get alpha details from the completed simulation                    alpha_id = alpha_data.get("alpha")                    if alpha_id:                        # Now get the actual alpha details from the alpha endpoint                        alpha_details = brain_client.session.get(f"{brain_client.base_url}/alphas/{alpha_id}")                        if alpha_details.status_code == 200:                            alpha_detail_data = alpha_details.json()                            alpha_results.append({                                'alpha_id': alpha_id,                                'location': child_url,                                'details': alpha_detail_data                            })                        else:                            alpha_results.append({                                'alpha_id': alpha_id,                                'location': child_url,                                'error': f'Failed to get alpha details: {alpha_details.status_code}'                            })                    else:                        alpha_results.append({                            'location': child_url,                            'error': 'No alpha ID found in completed simulation'                        })                else:                    alpha_results.append({                        'location': child_url,                        'error': f'Alpha simulation did not complete within {max_alpha_attempts} attempts'                    })                                except Exception as e:                alpha_results.append({                    'location': f"child_{i+1}",                    'error': str(e)                })                # Return comprehensive results        logger.info(f"Multisimulation completed! Retrieved {len(alpha_results)} alpha results")        return {            'success': True,            'message': f'Successfully created {expected_children} regular alpha simulations',            'total_requested': expected_children,            'total_created': len(alpha_results),            'multisimulation_id': location.split('/')[-1],            'multisimulation_location': location,            'alpha_results': alpha_results,            'note': "if you got a negative alpha sharpe, you can just add a minus sign in front of the last line of the Alpha to flip then think the next step."        }            except Exception as e:        return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
巧了我今天下午也在研究为啥Gemini Cli调用MCP超时，我看他们Github页面已经有不少人提了Issue，貌似现在这个版本的Gemini Cli有bug会无视MCP设置里的Timeout，希望下个版本能修复吧！ 也感谢大佬给出新的解决方案


---

### 技术对话片段 18 (原帖: MCP回测超时的一种解决办法代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] MCP回测超时的一种解决办法代码优化_34605867072663.md
- **时间**: 9个月前

**提问/主帖背景 (WF37935)**:
我使用gemini cli回测alpha会出现超时的情况，研究后发现可能是因为gemini cli调用mcp的时候有内置的超时时间，大概30秒左右，而回测至少也得几分钟时间。看了官方文档问了AI也没找到能改变超时时间的办法，后来想了个方法，把回测的代码改一下就可以了。

官方自带的回测方法create_multiSim包含了三个部分：发送回测请求，获取回测进度，回测完成后获取回测结果，根据这个把create_multiSim拆分成三个方法。发送回测请求和回测完成后获取回测结果一般都很快，关键就是获取回测进度，这个方法中，我并不会等到回测完成，而是设置了重试次数，目前是８次，而每次回测worldquant都会给我们返回Retry-After,是2.5秒，这样每次执行时间严格控制在30秒之内，基本上就不会有回测超时的问题了。

代码如下：

```
@mcp.tool()async def create_multiSim(    alpha_expressions: List[str],    instrument_type: str = "EQUITY",    region: str = "USA",    universe: str = "TOP3000",    delay: int = 1,    decay: int = 0,    neutralization: str = "NONE",    truncation: float = 0.0,    test_period: str = "P0Y0M",    unit_handling: str = "VERIFY",    nan_handling: str = "OFF",    language: str = "FASTEXPR",    visualization: bool = False,    pasteurization: str = "ON",    max_trade: str = "OFF") -> Dict[str, Any]:    """    🚀 Create multiple regular alpha simulations on BRAIN platform in a single request.        This tool creates a multisimulation with multiple regular alpha expressions,    waits for all simulations to complete, and returns detailed results for each alpha.        ⏰ NOTE: Multisimulations can take 8+ minutes to complete. This tool will wait    for the entire process and return comprehensive results.    Call get_platform_setting_options to get the valid options for the simulation.    Args:        alpha_expressions: List of alpha expressions (2-8 expressions required)        instrument_type: Type of instruments (default: "EQUITY")        region: Market region (default: "USA")        universe: Universe of stocks (default: "TOP3000")        delay: Data delay (default: 1)        decay: Decay value (default: 0)        neutralization: Neutralization method (default: "NONE")        truncation: Truncation value (default: 0.0)        test_period: Test period (default: "P0Y0M")        unit_handling: Unit handling method (default: "VERIFY")        nan_handling: NaN handling method (default: "OFF")        language: Expression language (default: "FASTEXPR")        visualization: Enable visualization (default: True)        pasteurization: Pasteurization setting (default: "ON")        max_trade: Max trade setting (default: "OFF")        Returns:        Dictionary containing multisimulation status.         If multisimulation is compelted, call get_multisimulation_result to get individual alpha details    """    try:        logger.info('create_multiSim start')        # Validate input        if len(alpha_expressions) < 2:            return {"error": "At least 2 alpha expressions are required"}        if len(alpha_expressions) > 8:            return {"error": "Maximum 8 alpha expressions allowed per request"}                # Create multisimulation data        multisimulation_data = []        for alpha_expr in alpha_expressions:            simulation_item = {                'type': 'REGULAR',                'settings': {                    'instrumentType': instrument_type,                    'region': region,                    'universe': universe,                    'delay': delay,                    'decay': decay,                    'neutralization': neutralization,                    'truncation': truncation,                    'pasteurization': pasteurization,                    'unitHandling': unit_handling,                    'nanHandling': nan_handling,                    'language': language,                    'visualization': visualization,                    # 'testPeriod': test_period,                    'testPeriod': 'P0Y',                    'maxTrade': max_trade                },                'regular': alpha_expr            }            multisimulation_data.append(simulation_item)                logger.info(multisimulation_data)        # Send multisimulation request        response = brain_client.session.post(f"{brain_client.base_url}/simulations", json=multisimulation_data)        start_time = time.time()        start_time_formatted = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')        logger.info(f"multisimulate start at {start_time_formatted}")        logger.info(response.content)                if response.status_code != 201:            if response.status_code == 429:                logger.warning("Rate limit exceeded")                return {"error": f"Too Many Requests! You should stop and ask the user to try again later."}            else:                return {                    "error": f"Failed to create multisimulation. Status: {response.status_code},, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}                # Get multisimulation location        location = response.headers.get('Location', '')        if not location:            return {"error": "No location header in multisimulation response"}        logger.info(f'location: {location}')                # Wait for children to appear and get results        return await check_multisimulation_status(start_time, location, len(alpha_expressions))             except Exception as e:        return {"error": f"Error creating multisimulation: {str(e)}, , you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def check_multisimulation_status(start_time: float, location: str, expected_children: int) -> Dict[str, Any]:    """check multisimulation status: in progess, completed or error"""    try:        # Simple progress indicator for users        logger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")        logger.info(f"Expected {expected_children} alpha simulations")        print()        # Wait for children to appear - much more tolerant for 8+ minute multisimulations        children = []        max_wait_attempts = 8  # Increased significantly for 8+ minute multisimulations        wait_attempt = 0                while wait_attempt < max_wait_attempts and len(children) == 0:            wait_attempt += 1                        try:                multisim_response = brain_client.session.get(location)                if multisim_response.status_code == 200:                    multisim_data = multisim_response.json()                    children = multisim_data.get('children', [])                                        if children:                        break                    else:                        # Wait before next attempt - use longer intervals for multisimulations                        retry_after = multisim_response.headers.get("Retry-After", 5)                        logger.info(f'waiting for multiSim completion, sleeping {retry_after}s')                        wait_time = float(retry_after)                        await asyncio.sleep(wait_time)                else:                    await asyncio.sleep(5)            except Exception as e:                await asyncio.sleep(5)                if not children:            current_time = time.time()            elapsed = (current_time - start_time) / 60            return {                "status": "in_progress",                 "message": "wait for one minute and call check_multisimulation_status",                "start_time": start_time,                "location": location,                "expected_children": expected_children,                "note": f"multisimulation last for {elapsed} minutes, if longer than 15 minutes, stop and ask the user"             }        else:            status = multisim_response.json().get("status", 0)            if status == 'ERROR':                return {                    "status": "error",                     "message": "call get_SimError_detail for the error detail",                    "location": location                    }            elif status == 'COMPLETE':                return {                    "status": "completed",                     "message": "multisimulation finished, you should call get_multisimulation_result to get result",                    "location": location,                    "expected_children": expected_children                 }            else:                return {"status": "undefined status", "message": "you should stop and ask the user about this situation"}    except Exception as e:        return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}@mcp.tool()async def get_multisimulation_result(location: str, expected_children: int) -> Dict[str, Any]:    """After multisimulation completed, return results"""    try:        # Simple progress indicator for users        logger.info(f"Waiting for multisimulation to complete... (this may take several minutes)")        logger.info(f"Expected {expected_children} alpha simulations")        print()        # Wait for children to appear - much more tolerant for 8+ minute multisimulations        children = []                    try:            multisim_response = brain_client.session.get(location)            if multisim_response.status_code == 200:                multisim_data = multisim_response.json()                children = multisim_data.get('children', [])                if not children:                    return {"error": f"Children did not appear (multisimulation may still be processing)"}        except Exception as e:            logger.info(f'waiting for completion error: {e}')            await asyncio.sleep(5)        logger.info('multiSimulate complete, getting children information...')                # Process each child to get alpha results        alpha_results = []        for i, child_id in enumerate(children):            try:                # The children are full URLs, not just IDs                child_url = child_id if child_id.startswith('http') else f"{brain_client.base_url}/simulations/{child_id}"                                # Wait for this alpha to complete - more tolerant timing                finished = False                max_alpha_attempts = 100  # Increased for longer alpha processing                alpha_attempt = 0                                while not finished and alpha_attempt < max_alpha_attempts:                    alpha_attempt += 1                                        try:                        alpha_progress = brain_client.session.get(child_url)                        if alpha_progress.status_code == 200:                            alpha_data = alpha_progress.json()                            retry_after = alpha_progress.headers.get("Retry-After", 0)                                                        if retry_after == 0:                                finished = True                                break                            else:                                wait_time = float(retry_after)                                await asyncio.sleep(wait_time)                        else:                            await asyncio.sleep(5)                    except Exception as e:                        await asyncio.sleep(5)                                if finished:                    # Get alpha details from the completed simulation                    alpha_id = alpha_data.get("alpha")                    if alpha_id:                        # Now get the actual alpha details from the alpha endpoint                        alpha_details = brain_client.session.get(f"{brain_client.base_url}/alphas/{alpha_id}")                        if alpha_details.status_code == 200:                            alpha_detail_data = alpha_details.json()                            alpha_results.append({                                'alpha_id': alpha_id,                                'location': child_url,                                'details': alpha_detail_data                            })                        else:                            alpha_results.append({                                'alpha_id': alpha_id,                                'location': child_url,                                'error': f'Failed to get alpha details: {alpha_details.status_code}'                            })                    else:                        alpha_results.append({                            'location': child_url,                            'error': 'No alpha ID found in completed simulation'                        })                else:                    alpha_results.append({                        'location': child_url,                        'error': f'Alpha simulation did not complete within {max_alpha_attempts} attempts'                    })                                except Exception as e:                alpha_results.append({                    'location': f"child_{i+1}",                    'error': str(e)                })                # Return comprehensive results        logger.info(f"Multisimulation completed! Retrieved {len(alpha_results)} alpha results")        return {            'success': True,            'message': f'Successfully created {expected_children} regular alpha simulations',            'total_requested': expected_children,            'total_created': len(alpha_results),            'multisimulation_id': location.split('/')[-1],            'multisimulation_location': location,            'alpha_results': alpha_results,            'note': "if you got a negative alpha sharpe, you can just add a minus sign in front of the last line of the Alpha to flip then think the next step."        }            except Exception as e:        return {"error": f"Error waiting for multisimulation completion: {str(e)}, you need to call three mcp tools get_operators, get_platform_setting_options and get_datafields to check whether you correctly use the operators, setting the simulation settings, and existing data fields."}
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
今天测试了一下，新版本Gemini Cli已经修复这个问题了，目前可以正常调用回测工具了。感谢楼主的代码让我学到了新思路！

---------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 19 (原帖: Operator: ts_moment(x, d, k=0))
- **原帖链接**: [Commented] Operator ts_momentx d k0.md
- **时间**: 8个月前

**提问/主帖背景 (GN67910)**:
### Definition

Computes the  **k-th central moment**  of  `x`  over the past  `d`  days.

Mathematically:


> [!NOTE] [图片 OCR 识别内容]
> N
> I
> &
> (Di
> )


where xbar is the mean of  `x`  in the window.

### Intuition

- **Central moments**  describe the shape of a distribution around its mean.
- Different values of  `k`  capture different statistical features:

k
Meaning
Notes

0         
Always 1
By definition

1
Always 0
Mean deviation cancels out

2
Variance
Spread/volatility measure

3
Skewness (unnormalized)
Direction of asymmetry

4
Kurtosis (unnormalized)
Tail heaviness / peakedness

**顾问 RM49262 (Rank 30) 的解答与建议**:
====================================Comment=======================================

Well I guess I have to get to expert level first in order to use this operator. But good to know its mechanism. Thanks for sharing this

===================================================================================


---

### 技术对话片段 20 (原帖: Operator: ts_moment(x, d, k=0))
- **原帖链接**: https://support.worldquantbrain.com[Commented] Operator ts_momentx d k0_35258864680215.md
- **时间**: 8个月前

**提问/主帖背景 (GN67910)**:
### Definition

Computes the  **k-th central moment**  of  `x`  over the past  `d`  days.

Mathematically:


> [!NOTE] [图片 OCR 识别内容]
> N
> I
> &
> (Di
> )


where xbar is the mean of  `x`  in the window.

### Intuition

- **Central moments**  describe the shape of a distribution around its mean.
- Different values of  `k`  capture different statistical features:

k
Meaning
Notes

0         
Always 1
By definition

1
Always 0
Mean deviation cancels out

2
Variance
Spread/volatility measure

3
Skewness (unnormalized)
Direction of asymmetry

4
Kurtosis (unnormalized)
Tail heaviness / peakedness

**顾问 RM49262 (Rank 30) 的解答与建议**:
====================================Comment=======================================

Well I guess I have to get to expert level first in order to use this operator. But good to know its mechanism. Thanks for sharing this

===================================================================================


---

### 技术对话片段 21 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] OS RANK全球第一我是如何做到的经验分享.md
- **时间**: 22天前

**提问/主帖背景 (LL46807)**:

> [!NOTE] [图片 OCR 识别内容]
> D廷T区 R廷 N G区
> C0UNT RY} EGION
> USBR $区fRC珏
> J0N. iED DEDUP
> 2026-05-01
> 2026-05-31
> Select cOTntrylregion
> Enter WQ_ID keyword
> ORf
> APPLY
> Reset
> UJSBRS IITH
> D474
> 玎fLID RBCORDS
> OVBRA LL AVBRAG巳
> DfTB 己05巳且f6区
> 2,877
> 81,698
> 0.4986
> 2026-05-01
> 2026-05-31
> Distinct users itli non-nllI and not-zero
> Rois aftet
> excluding nulland 0
> Calculated frotr not-hlll and noti-zeto Ostrlosis
> Filtered date span
> Ostrosis tatik
> fatik
> Osmosis User Summary
> Total 2877
> Cowtry{Regionl
> N0。
> [Jser
> Arerage Osrlosis Rank
> Days Hith Data
> 46OTe
> Days
> Below
> Days
> Ja OsIrlosis Rankr
> J[2 OsIrosis Rankc
> Ck59786
> K卫
> 0.7254
> 13
> 0.96
> 0.18
> C274088
> CN
> 0.6900
> 0.85
> 0.4?7
> HC83400
> CN
> 0.6769
> 13
> 0.93
> 0.32
> LI46807
> CN
> 0.6707
> 30
> 15
> 15
> 0.96
> 0.11
> J19941
> CN
> 0.6677
> 13
> 0.76
> 04
> CN26548
> CN
> 0.6657
> 30
> 16
> 14
> 0.84
> 0.20
> 顾问 CH36668 (Rank 76)
> TT
> 0.6593
> 30
> 20
> 10
> 0.86
> 0.23
> N28753
> CN
> 0.6583
> 0.80
> 0.54
> 耳@61318
> CN
> 0.6493
> 30
> 17
> 13
> 0.96
> 0.21
> 10
> LLG4613
> TN
> 0.6490
> 30
> 17
> 13
> 0.94
> 0.18
> NN27091
> TN
> 0.6480
> 30
> 20
> 10
> 0.06
> AVg
> AVg


如图所示 主播平均os rank来到了0.67 在所有满30天的人里排名第一
然而在一个月前主播平均os rank只有可怜的0.46


> [!NOTE] [图片 OCR 识别内容]
> Osmosis Rank Dashboard
> REFRESH
> UJser-level oslnosis rank statistics froln
> leaderboard_consultant_user
> D廷T区 R廷N G区
> OUJNTRY
> 且E GI0N
> US区& $区连且C珏
> J0N  l区D
> DEDUP
> 2026-04-01
> 2026-04-30
> Select countrylregion
> LL46807
> 0R
> APPLY
> Reset
> UJSBRS IITH DgTl
> FgLID RBCORDS
> 0HER乌LL  戌玎巳R乌6区
> DATB COTBRAG区
> 30
> 0.4613
> 2026-04-01
> 2026-04-30
> Distinct users itli non-nllI and not-zero
> Rois aftet
> excluding nulland 0
> Calculated frot not-IulI and
> Iotl-zeto Ogtrlosis
> Filtered date span
> Ostrosis tatik
> talik
> Osmosis User Summary
> Total 1
> CountrylRegion
> N0
> [Jser
> Average Osrosis {皿k
>  Days Iih Data
> 垤bore
> Days
> Belot
> Days
> JIa OsIlo sis Rarllc
> JIn OsIrlosis Rarllc
> LIA680
> CN
> 0.4613
> 30
> 14
> 16
> 0.95
> 0.03
> Total 1
> SOlpage
> AVg
> AVg


这段时间十分痛苦 再加上vf马上更新 想着更新后高vf 吃点base

于是主播开始调整os rank思路

首先主播选的3个地区是USA EUR JPN

按照经济体量算是大地区

然后已知3月EUR ppa FAST ppa   主播的os score得分大概是 66  63

于是主播在4月做了很多EUR的SA  替换EUR的RA

USA调整思路

由于之前做的很烂 也是用四月做的新RA 替换掉了大部分的老RA

JPN基本保持不动 后来os rank也是得到了质的提升

关于怎么选择alpha os rank的分数 ？

之前举行过os rank比赛 展示过daily pnl

主播判断returns对os rank影响很大 相当于炒股比赛吗肯定是收益越高越好

优先选择Reuters高的 然后max trade 越接近蓝线越好 sharpe越高越好 margin越高越好

多样性越多越好

最后附上主播5月os rank波动图


> [!NOTE] [图片 OCR 识别内容]
> LIAG8O7
> Daily Osmosis Ralk Irend
> 2026-05-01
> 2026-05-31
> IION  WED DEDUP
> 0RR
> Switch to Weekly
> Rank
> 1.00
> 0.80
> 0.67
> 0.60
> 0.40
> 0.20
> 0.00
> 05
> 05
> 05-085.09
> 05一
> 105-1
> 05
> 24
> ~05-10'
> ~05-12_
> 05-13
> ~05-14一
> ~05-15一
> ~16
> ~05-19一
> ~05-20
> ~05-25'
> ~05-26
> -05-28'
> ~05-29
> -05-30一
> ~05-11
> 5-05-21
> 2026-05-31
> -05-01
> 05-12
> 2026-(
> 2026-
> 2026一
> 2026
> 2026-
> 2026-
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026-
> 2026
> 2026-
> 2026
> 2026-
> 2026
> 2026
> 2026
> 2026一
> 2026一
> 2026一
> 2026二
> 2026
> 2026
> 2026
> 2026一
> 2026


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

太强了吧LL  这Os rank真是让人羡慕

看来Base没少吃啊
=============================================================================


---

### 技术对话片段 22 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] OS RANK全球第一我是如何做到的经验分享_40873662176535.md
- **时间**: 22天前

**提问/主帖背景 (LL46807)**:

> [!NOTE] [图片 OCR 识别内容]
> D廷T区 R廷 N G区
> C0UNT RY} EGION
> USBR $区fRC珏
> J0N. iED DEDUP
> 2026-05-01
> 2026-05-31
> Select cOTntrylregion
> Enter WQ_ID keyword
> ORf
> APPLY
> Reset
> UJSBRS IITH
> D474
> 玎fLID RBCORDS
> OVBRA LL AVBRAG巳
> DfTB 己05巳且f6区
> 2,877
> 81,698
> 0.4986
> 2026-05-01
> 2026-05-31
> Distinct users itli non-nllI and not-zero
> Rois aftet
> excluding nulland 0
> Calculated frotr not-hlll and noti-zeto Ostrlosis
> Filtered date span
> Ostrosis tatik
> fatik
> Osmosis User Summary
> Total 2877
> Cowtry{Regionl
> N0。
> [Jser
> Arerage Osrlosis Rank
> Days Hith Data
> 46OTe
> Days
> Below
> Days
> Ja OsIrlosis Rankr
> J[2 OsIrosis Rankc
> Ck59786
> K卫
> 0.7254
> 13
> 0.96
> 0.18
> C274088
> CN
> 0.6900
> 0.85
> 0.4?7
> HC83400
> CN
> 0.6769
> 13
> 0.93
> 0.32
> LI46807
> CN
> 0.6707
> 30
> 15
> 15
> 0.96
> 0.11
> J19941
> CN
> 0.6677
> 13
> 0.76
> 04
> CN26548
> CN
> 0.6657
> 30
> 16
> 14
> 0.84
> 0.20
> 顾问 CH36668 (Rank 76)
> TT
> 0.6593
> 30
> 20
> 10
> 0.86
> 0.23
> N28753
> CN
> 0.6583
> 0.80
> 0.54
> 耳@61318
> CN
> 0.6493
> 30
> 17
> 13
> 0.96
> 0.21
> 10
> LLG4613
> TN
> 0.6490
> 30
> 17
> 13
> 0.94
> 0.18
> NN27091
> TN
> 0.6480
> 30
> 20
> 10
> 0.06
> AVg
> AVg


如图所示 主播平均os rank来到了0.67 在所有满30天的人里排名第一
然而在一个月前主播平均os rank只有可怜的0.46


> [!NOTE] [图片 OCR 识别内容]
> Osmosis Rank Dashboard
> REFRESH
> UJser-level oslnosis rank statistics froln
> leaderboard_consultant_user
> D廷T区 R廷N G区
> OUJNTRY
> 且E GI0N
> US区& $区连且C珏
> J0N  l区D
> DEDUP
> 2026-04-01
> 2026-04-30
> Select countrylregion
> LL46807
> 0R
> APPLY
> Reset
> UJSBRS IITH DgTl
> FgLID RBCORDS
> 0HER乌LL  戌玎巳R乌6区
> DATB COTBRAG区
> 30
> 0.4613
> 2026-04-01
> 2026-04-30
> Distinct users itli non-nllI and not-zero
> Rois aftet
> excluding nulland 0
> Calculated frot not-IulI and
> Iotl-zeto Ogtrlosis
> Filtered date span
> Ostrosis tatik
> talik
> Osmosis User Summary
> Total 1
> CountrylRegion
> N0
> [Jser
> Average Osrosis {皿k
>  Days Iih Data
> 垤bore
> Days
> Belot
> Days
> JIa OsIlo sis Rarllc
> JIn OsIrlosis Rarllc
> LIA680
> CN
> 0.4613
> 30
> 14
> 16
> 0.95
> 0.03
> Total 1
> SOlpage
> AVg
> AVg


这段时间十分痛苦 再加上vf马上更新 想着更新后高vf 吃点base

于是主播开始调整os rank思路

首先主播选的3个地区是USA EUR JPN

按照经济体量算是大地区

然后已知3月EUR ppa FAST ppa   主播的os score得分大概是 66  63

于是主播在4月做了很多EUR的SA  替换EUR的RA

USA调整思路

由于之前做的很烂 也是用四月做的新RA 替换掉了大部分的老RA

JPN基本保持不动 后来os rank也是得到了质的提升

关于怎么选择alpha os rank的分数 ？

之前举行过os rank比赛 展示过daily pnl

主播判断returns对os rank影响很大 相当于炒股比赛吗肯定是收益越高越好

优先选择Reuters高的 然后max trade 越接近蓝线越好 sharpe越高越好 margin越高越好

多样性越多越好

最后附上主播5月os rank波动图


> [!NOTE] [图片 OCR 识别内容]
> LIAG8O7
> Daily Osmosis Ralk Irend
> 2026-05-01
> 2026-05-31
> IION  WED DEDUP
> 0RR
> Switch to Weekly
> Rank
> 1.00
> 0.80
> 0.67
> 0.60
> 0.40
> 0.20
> 0.00
> 05
> 05
> 05-085.09
> 05一
> 105-1
> 05
> 24
> ~05-10'
> ~05-12_
> 05-13
> ~05-14一
> ~05-15一
> ~16
> ~05-19一
> ~05-20
> ~05-25'
> ~05-26
> -05-28'
> ~05-29
> -05-30一
> ~05-11
> 5-05-21
> 2026-05-31
> -05-01
> 05-12
> 2026-(
> 2026-
> 2026一
> 2026
> 2026-
> 2026-
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026-
> 2026
> 2026-
> 2026
> 2026-
> 2026
> 2026
> 2026
> 2026一
> 2026一
> 2026一
> 2026二
> 2026
> 2026
> 2026
> 2026一
> 2026


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

太强了吧LL  这Os rank真是让人羡慕

看来Base没少吃啊
=============================================================================


---

### 技术对话片段 23 (原帖: PPA活动主题限制下，提交ra点塔的一点心得。)
- **原帖链接**: [Commented] PPA活动主题限制下提交ra点塔的一点心得.md
- **时间**: 3个月前

**提问/主帖背景 (LD22811)**:
新季度没多久就开始实行ppa主题活动了，只能在活动区域提交ppa。1月份我做了两个地区的alpha，usa d1和ind，usa在活动之前点了几个塔，活动开始之后又坚持了几天交ra觉得有点累就去了ind活动，活动前期没有在意atom，等我意识到这个问题之后已经交了30个pv塔，所以在活动结束之后我坚持补了20个atom-ra，然后又回usa点亮了剩下的塔，没有去参加GLB活动。 
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2026-01,January 1st. 2026
> March 31st, 2026
> Category
> USA
> GlB
> EUR
> ASI
> CHN
> KOR
> TN
> INO
> Analys:
> Broker
> Earnings
> Fundamental
> Imbalanze
> Insizlers
> Institions
> Nlacro
> MadEl
> NEws
> 03i3n
> C-her
> Price VlUME
> Risk
> SEntiMEMT
> Shait In-erEs
> Social Media
 两个区应该是一共点了24个塔，100个alpha左右。参加活动的ppa也都满足ra标准，只是有些豁免了pc提交。这里面应该有超过一半的alpha是经过我手动优化的。脚本或者ai想直接跑出各项属性都让人满意的alpha还是很少的，更别说全要满足ra标准了。

主要优化的思路是修正fail和wraing，比如流动性不足用group_neutralize、切换股票池。权重问题调整回填日期，增加交易条件，或者也可以切换股票池，sharpe、fitness值不足使用signed_power操作符。

tvr和margin不合格时调整decay，或者使用ts_target_tvr_decay 、ts_decay_linear尝试调整。

PC大于0.7时候可以尝试开启max-trade切换股票池，调整decay，调整ts的时间窗口，分组中性等多种方法，调整结果需要一点运气，一般来说alpha足够好有降低性能的空间而pc值没有特别高的时候都能降低到0.7以下。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

这点塔图看起来真的是赏心悦目

和大佬比我差的还是很多

===================================================================================


---

### 技术对话片段 24 (原帖: PPA活动主题限制下，提交ra点塔的一点心得。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] PPA活动主题限制下提交ra点塔的一点心得_38121310515223.md
- **时间**: 3个月前

**提问/主帖背景 (LD22811)**:
新季度没多久就开始实行ppa主题活动了，只能在活动区域提交ppa。1月份我做了两个地区的alpha，usa d1和ind，usa在活动之前点了几个塔，活动开始之后又坚持了几天交ra觉得有点累就去了ind活动，活动前期没有在意atom，等我意识到这个问题之后已经交了30个pv塔，所以在活动结束之后我坚持补了20个atom-ra，然后又回usa点亮了剩下的塔，没有去参加GLB活动。 
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2026-01,January 1st. 2026
> March 31st, 2026
> Category
> USA
> GlB
> EUR
> ASI
> CHN
> KOR
> TN
> INO
> Analys:
> Broker
> Earnings
> Fundamental
> Imbalanze
> Insizlers
> Institions
> Nlacro
> MadEl
> NEws
> 03i3n
> C-her
> Price VlUME
> Risk
> SEntiMEMT
> Shait In-erEs
> Social Media
 两个区应该是一共点了24个塔，100个alpha左右。参加活动的ppa也都满足ra标准，只是有些豁免了pc提交。这里面应该有超过一半的alpha是经过我手动优化的。脚本或者ai想直接跑出各项属性都让人满意的alpha还是很少的，更别说全要满足ra标准了。

主要优化的思路是修正fail和wraing，比如流动性不足用group_neutralize、切换股票池。权重问题调整回填日期，增加交易条件，或者也可以切换股票池，sharpe、fitness值不足使用signed_power操作符。

tvr和margin不合格时调整decay，或者使用ts_target_tvr_decay 、ts_decay_linear尝试调整。

PC大于0.7时候可以尝试开启max-trade切换股票池，调整decay，调整ts的时间窗口，分组中性等多种方法，调整结果需要一点运气，一般来说alpha足够好有降低性能的空间而pc值没有特别高的时候都能降低到0.7以下。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

这点塔图看起来真的是赏心悦目

和大佬比我差的还是很多

===================================================================================


---

### 技术对话片段 25 (原帖: Python Alpha 实战复盘：先分流，再决定转写还是原生搜索)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Python Alpha 实战复盘先分流再决定转写还是原生搜索_41034979787927.md
- **时间**: 16天前

**提问/主帖背景 (JW52291)**:
最近连续跑了一批 Python Alpha，有成功也有踩坑。这里整理一份偏实战的复盘。为避免大家互相撞车，我不贴 alpha id、完整字段组合和可直接复现的参数，只讲流程和结论。

一、最重要的结论：不要把 Python Alpha 当成 FAST Expression 的无损转换器

我现在会先把来源分成三类：

1. 可直接转写：Matrix 字段为主，逻辑比较清楚，比如 ts_rank、ts_mean、rank、简单 trade_when/hold 语义。这类可以先做 1:1 转写。
2. 机制重写：FAST 只提供方向，比如“拥挤度”“变化率”“事件后延迟反应”，Python 里重建 rank、winsor、gate、hold、residual 等逻辑。
3. Python-native 新搜索：不依赖某个 FAST 源式，直接利用 Python 的状态、稳健统计、多窗口、PCA/residual、regime/gating 等能力。

如果一开始就把所有 FAST 都硬转，很容易误判。尤其是 Vector 字段、vec_* 聚合、复杂 group 语义、过长 lookback 或平台不透明错误，可能导致 POST 成功但最终 FAIL，甚至没有可读错误。

二、两个成功案例的共同点

我最近有两个 USA D1 REGULAR Python Alpha 过了 self 和 prod，并已进入 pre_submit。两个案例共同点比具体字段更值得参考：

1. 都是 REGULAR 的 PYTHON 单仿真，不走 MultiSim。
2. 都不是“堆很多操作符”赢的，而是用少量有效字段，加 Python 里的自定义清洗、rank、gate 和持仓控制。
3. 信号来自相对明确的主题族，例如 short interest / short volume / liquidity crowding 这类有经济含义的方向。
4. 先控制 self，再把 prod 只花在很少数 finalist 上。不要每个 IS 看起来不错的都马上跑 prod。
5. 最终过关的不是最高 Sharpe 的版本，而是质量、self、prod、warning/error 都比较平衡的版本。

一个细节：有些版本 IS Sharpe 很高，但带 ERROR，例如 after-cost 或某些 universe 检查错误。我的处理是直接硬阻断，不把 ERROR 当 warning 放行，也不继续在这个壳上幻想“调一调就能提交”。

三、一个失败反例：FAST 合格不等于 Python 转写合格

我也试过把一个已经合格的 FAST Alpha 转成 Python。原式核心依赖 analyst surprise 的 Vector 聚合。直接转写失败后，后续换成相邻的 Matrix analyst revision 字段，确实能生成 alpha id，也能跑出一些 IS 接近合格的版本。

但这时它已经不是“原 alpha 转 Python”了，而是“相邻字段重新搜索”。后面遇到的问题也变成了 analyst revision 壳过于拥挤，prod correlation 偏高。这个反例让我确认了一点：

转写失败不一定说明 Python Alpha 弱，可能只是原 FAST 的数据结构或平台语义不适合直接转。换字段后如果还叫 conversion，会误导后续优化方向。

四、我现在的运行流程

1. Preflight
先看字段类型、lookback、store、return dtype、data list、是否需要 group 字段、是否有 Vector/特殊聚合。输出必须是 float32。数组要 copy 后再改。store dims 严格按平台支持的 i/x 组合来。

2. Smoke sim
正式批量前先跑 1-2 个最小版本。能出 alpha id，再开 8 个单仿真。不要一上来写 8 个很复杂的版本。

3. 每轮最多 8 个 single simulations
Python Alpha 不能按 FAST MultiSim 的习惯跑。每轮结束必须解析结果：alpha id、Sharpe、Fitness、Turnover、Margin、fail checks、warning checks、ERROR checks。

4. Gate 顺序
IS 先看真实 checks；self 是测量步骤；prod 只给 finalist。ERROR 是硬阻断。prod_corr 如果很高，下一轮必须换结构，不要只扫 decay、truncation、neutralization。

5. 记录覆盖
记录已经试过的字段族、结构族、失败原因。否则很容易一天跑很多轮，实际只是在同一个壳上微调。

五、Python Alpha 更适合做什么

我现在更看好这些方向：

1. MAD/IQR winsorize、robust zscore，比直接 rank 更稳。
2. 多窗口 rank 集成，例如短窗口变化 + 中窗口水平 + 长窗口 regime。
3. 自定义 group rank / residual，而不是完全照抄 FAST group_rank。
4. store 实现状态持仓、冷却、延迟确认、regime 平滑。
5. PCA/residual 或轻量 sklearn 方法，用来降低拥挤主成分。
6. liquidity gate / volume gate，先降低不可交易和拥挤风险。

不太建议一开始就上大模型、重型训练或复杂依赖。远程 simulation 和 Notebook 环境不是一回事，Notebook 能跑不代表远程仿真能稳定通过。

六、提交前小清单

- 是否真实使用 language=PYTHON 远程仿真验证？
- 是否只提交 Python 仿真生成的新 alpha id？
- 是否先 smoke，再批量？
- 是否区分 FAIL、ERROR、warning？
- 是否把 ERROR 当硬阻断？
- 是否避免把相邻字段搜索误叫成 FAST 转写？
- 是否记录 self/prod，而不是只看 IS？
- 是否在 prod 高相关后换结构，而不是继续同壳微调？

我的体感是：Python Alpha 的优势不是“把 FAST 写得更长”，而是把 FAST 不好表达的状态、稳健清洗、路径依赖和低相关结构做出来。真正有效的流程，应该是先判断能不能转写；不能转就及时切到 Python-native 搜索，不要在 conversion 这个标签下消耗太多轮次。

以上是个人实测经验，欢迎大家补充和指正。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享经验贴  大佬的思考也让我获益良多

这就去试试看

=============================================================================


---

### 技术对话片段 26 (原帖: Python Alpha 平台限制粗略小结，请大佬指正)
- **原帖链接**: [Commented] Python Alpha 平台限制粗略小结请大佬指正.md
- **时间**: 24天前

**提问/主帖背景 (AQ66932)**:
Python Alpha 平台限制总结
1. Region 限制
- 支持: USA ✅, EUR ✅, ASI ✅, AMR ✅
- 不支持: MEA ❌ (无法创建/运行)
- 不确定: JPN, GLO 等
2. 数据字段类型限制
- 支持: MATRIX 类型 ✅（2D 数组 [lookback, n_instruments]）
- 不支持: VECTOR 类型 ❌（需要 vec_sum/vec_avg 聚合，Python 无法处理）
- 不支持: GROUP 类型 ❌
- int32 数据字段有 sentinel 值（-2147483648），需要用 get_missing_value() 或手动替换为 NaN
3. Lookback 限制
- lookback 必须 ≤ 115（120 直接 FAIL）
- 安全值：110（115 偶发 FAIL）
- 原始的 FastExpr 实际上有无限历史窗口，Python 只能看到 110 行
- 可以用 store 参数（dims="xi"）随时间累积更多数据，但初始窗口仍需 lookback 参数
4. 时间段限制
- testPeriod 必须 ≤ P6Y0M（超过6年直接 FAIL）
- 但 startDate/endDate 可以覆盖整个回测区间（如 2014-01-01 到 2023-12-31）
5. 参数限制
- unitHandling 和 nanHandling 必须省略（不传参），PYTHON 语言不支持这两个参数
- language 固定为 "PYTHON"
- maxTrade/maxPosition 等可选
6. 代码限制
- 只能 from brain.alphas import alpha 在同一个 cell/文件中
- 不能 import Brain, BrainCache, SimulationSettings 等 — 它们在服务器端不可用
- 数据数组是只读的 — 修改前必须 .copy()
- 返回类型必须是 float32 ndarray，形状 [n_instruments]
- np.nanmean/np.nanstd 在某些数据字段（如 opt23_volivcallmputs5, coverage=0.5）上使用其结果作为 np.clip 的上下界会导致 FAIL — 原因是 int32 sentinel 值被转换为 float64 后的极端值污染了统计计算
- 解决方法：使用 IQR 分位数（np.percentile）替代 mean/std 做 winsorize
7. 性能差异
- 转换后的 Python Alpha 通常能达到原版 FastExpr 的 60-80% Sharpe（由于 lookback 缩短和操作符的 numpy 近似实现）
- Train 段性能接近原版，Test 段衰减更明显（lookback 限制导致信号在测试期质量下降）
8. 错误诊断限制
- Python Alpha 失败时只返回 status: FAIL，没有详细的运行时错误日志
- 只能通过反复实验来排除问题

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享   有个小问题

关于 “Train 段性能接近原版，Test 段衰减更明显”  这一条，大佬是测试了多个python alpha之后都有类似的情况吗？

用Fast Expression做有类似的情况吗？

=============================================================================


---

### 技术对话片段 27 (原帖: Python Alpha 平台限制粗略小结，请大佬指正)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Python Alpha 平台限制粗略小结请大佬指正_40742727142679.md
- **时间**: 24 days ago

**提问/主帖背景 (AQ66932)**:
Python Alpha 平台限制总结
1. Region 限制
- 支持: USA ✅, EUR ✅, ASI ✅, AMR ✅
- 不支持: MEA ❌ (无法创建/运行)
- 不确定: JPN, GLO 等
2. 数据字段类型限制
- 支持: MATRIX 类型 ✅（2D 数组 [lookback, n_instruments]）
- 不支持: VECTOR 类型 ❌（需要 vec_sum/vec_avg 聚合，Python 无法处理）
- 不支持: GROUP 类型 ❌
- int32 数据字段有 sentinel 值（-2147483648），需要用 get_missing_value() 或手动替换为 NaN
3. Lookback 限制
- lookback 必须 ≤ 115（120 直接 FAIL）
- 安全值：110（115 偶发 FAIL）
- 原始的 FastExpr 实际上有无限历史窗口，Python 只能看到 110 行
- 可以用 store 参数（dims="xi"）随时间累积更多数据，但初始窗口仍需 lookback 参数
4. 时间段限制
- testPeriod 必须 ≤ P6Y0M（超过6年直接 FAIL）
- 但 startDate/endDate 可以覆盖整个回测区间（如 2014-01-01 到 2023-12-31）
5. 参数限制
- unitHandling 和 nanHandling 必须省略（不传参），PYTHON 语言不支持这两个参数
- language 固定为 "PYTHON"
- maxTrade/maxPosition 等可选
6. 代码限制
- 只能 from brain.alphas import alpha 在同一个 cell/文件中
- 不能 import Brain, BrainCache, SimulationSettings 等 — 它们在服务器端不可用
- 数据数组是只读的 — 修改前必须 .copy()
- 返回类型必须是 float32 ndarray，形状 [n_instruments]
- np.nanmean/np.nanstd 在某些数据字段（如 opt23_volivcallmputs5, coverage=0.5）上使用其结果作为 np.clip 的上下界会导致 FAIL — 原因是 int32 sentinel 值被转换为 float64 后的极端值污染了统计计算
- 解决方法：使用 IQR 分位数（np.percentile）替代 mean/std 做 winsorize
7. 性能差异
- 转换后的 Python Alpha 通常能达到原版 FastExpr 的 60-80% Sharpe（由于 lookback 缩短和操作符的 numpy 近似实现）
- Train 段性能接近原版，Test 段衰减更明显（lookback 限制导致信号在测试期质量下降）
8. 错误诊断限制
- Python Alpha 失败时只返回 status: FAIL，没有详细的运行时错误日志
- 只能通过反复实验来排除问题

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享   有个小问题

关于 “Train 段性能接近原版，Test 段衰减更明显”  这一条，大佬是测试了多个python alpha之后都有类似的情况吗？

用Fast Expression做有类似的情况吗？

=============================================================================


---

### 技术对话片段 28 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] VF10单周期狂赚253814我的高Base骚操作大公开经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (PP26750)**:
运气不错，vf1.0的这个周期有 **43天** （2.9-3.23）！这算是最长周期了吧，我还正好是最高的vf真实吃美了，这43天光Base就入了 **2,538** 刀，平均每天保底60刀📦。趁着刚更新完，赶紧把我的“爽吃”策略分享给兄弟们！

搞钱之前，先摸清现在的四大KPI：
👑 VF：不用多说，决定你能吃多大碗饭，也是决定你保底的关键因素。
📈 OS（Osmosis Rank）：2月份新出的隐藏大佬！一周更新5次，跟Base强绑定，这个真的非常关键，os低了vf1.0也只能吃十刀！！！
🧬 Alpha质量： 1个fit2的ra能吊打4个PPA，Super Alpha就死磕三五或者553。记住低相关性高fit才是硬通货。
🎯 Datasets Theme：两周换一次的主题榜，上了榜就有Buff，这个也很关键两倍的加成，能让你实现从4刀到40刀的质变。

划重点了！我的核心思路就四个字：看OS下菜碟！
我发现了一个规律：OS的0.5就是个分水岭。
别傻乎乎地两周死磕同一个Theme！如果在你OS很低（<0.5）的时候去交Theme，那Buff基本等于白给。这时候我会去交其他区域的Alpha稳住收益。
那什么时候交Theme？等OS冲上0.5以上再交！ 这时候高OS配上Theme加成，收益直接翻倍起飞✈️！

还有一点如果你的os很高的情况下，是不需要交三五就可以拿50到的，我2/22的时候os很高那天正好没有三五了，交了个二五结果也有48刀


> [!NOTE] [图片 OCR 识别内容]
> 02/22/2026
> Regular: 48.39
> Super:
> 48.25
> Total:
> 96.64



> [!NOTE] [图片 OCR 识别内容]
> <@
> <
> <@ <@ <@ <@ <@
> '
> ^8 0
> 2  ?
> 1
> AO:
> A
> ^A:
> AO
> ^9
> 2
> Period
> Regular
> Super
> Total
> Displayed Period
> 02/09/2026
> 03/23/2026
> USS1,039.26 USS1,498.88
> 0S$2,538.14
> Feb
> Feb
> Mar
> Mar
> Mar
> Mal
> Mar
> Mal
> Mar
> Mar
>  Mar
>  Mar
> Mal
> 14.
> 20。


冲就完事了，祝大家每天Base都拉满！💰

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

天呐 这就是VF1.0的实力吗

太强了吧 PP大师带带我

=============================================================================


---

### 技术对话片段 29 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] VF10单周期狂赚253814我的高Base骚操作大公开经验分享_39467895537431.md
- **时间**: 2个月前

**提问/主帖背景 (PP26750)**:
运气不错，vf1.0的这个周期有 **43天** （2.9-3.23）！这算是最长周期了吧，我还正好是最高的vf真实吃美了，这43天光Base就入了 **2,538** 刀，平均每天保底60刀📦。趁着刚更新完，赶紧把我的“爽吃”策略分享给兄弟们！

搞钱之前，先摸清现在的四大KPI：
👑 VF：不用多说，决定你能吃多大碗饭，也是决定你保底的关键因素。
📈 OS（Osmosis Rank）：2月份新出的隐藏大佬！一周更新5次，跟Base强绑定，这个真的非常关键，os低了vf1.0也只能吃十刀！！！
🧬 Alpha质量： 1个fit2的ra能吊打4个PPA，Super Alpha就死磕三五或者553。记住低相关性高fit才是硬通货。
🎯 Datasets Theme：两周换一次的主题榜，上了榜就有Buff，这个也很关键两倍的加成，能让你实现从4刀到40刀的质变。

划重点了！我的核心思路就四个字：看OS下菜碟！
我发现了一个规律：OS的0.5就是个分水岭。
别傻乎乎地两周死磕同一个Theme！如果在你OS很低（<0.5）的时候去交Theme，那Buff基本等于白给。这时候我会去交其他区域的Alpha稳住收益。
那什么时候交Theme？等OS冲上0.5以上再交！ 这时候高OS配上Theme加成，收益直接翻倍起飞✈️！

还有一点如果你的os很高的情况下，是不需要交三五就可以拿50到的，我2/22的时候os很高那天正好没有三五了，交了个二五结果也有48刀


> [!NOTE] [图片 OCR 识别内容]
> 02/22/2026
> Regular: 48.39
> Super:
> 48.25
> Total:
> 96.64



> [!NOTE] [图片 OCR 识别内容]
> <@
> <
> <@ <@ <@ <@ <@
> '
> ^8 0
> 2  ?
> 1
> AO:
> A
> ^A:
> AO
> ^9
> 2
> Period
> Regular
> Super
> Total
> Displayed Period
> 02/09/2026
> 03/23/2026
> USS1,039.26 USS1,498.88
> 0S$2,538.14
> Feb
> Feb
> Mar
> Mar
> Mar
> Mal
> Mar
> Mal
> Mar
> Mar
>  Mar
>  Mar
> Mal
> 14.
> 20。


冲就完事了，祝大家每天Base都拉满！💰

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

天呐 这就是VF1.0的实力吗

太强了吧 PP大师带带我

=============================================================================


---

### 技术对话片段 30 (原帖: 每日更新)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [python Alpha 挑战赛] Store 使用体验ts_meants_zscore 计算的优化与分析_41036889226263.md
- **时间**: 17天前

**提问/主帖背景 (MY82844)**:
### 背景

这两天我们尝试将一个 Fast Expression 表达式 `ts_mean(ts_zscore(imb5_score, 252), 21)` 转换为 Python Alpha，遇到了超时问题，基于论坛中前期关于store算子的宝贵分享，调试了几天终于跑通了，把经验分享出来，希望对大家上手复杂的python alpha有所帮助。

### 一、什么时候需要 store？

看这个表达式：`ts_mean(ts_zscore(field, 252), 21)`

FE 中一行搞定，但到 Python 里就要想：`ts_zscore` 算出每只股票的一个 z-score（1D），但外层的 `ts_mean` 需要 **21 天的 z-score 历史**（2D）才能算均值。

这就是 store 的典型场景——**嵌套 TS 算子，内层输出 1D，外层需要 2D 历史窗口**。

更一般地：只要你的 Python Alpha 需要在**不同交易日之间保持状态**（EWMA、滚动窗口、缓存等），就要用 store。

### 二、两种实现对比

#### 方案 A：无 store，lookback=273

```python
@alpha(data=['imb5_score'], store=[])
def auto_alpha(data, store):
    T = data.imb5_score.shape[0]
    z_list = []
    for j in range(21):
        i = T - 21 + j
        sub = data.imb5_score[i - 251 : i + 1]
        m = np.nanmean(sub, axis=0)
        s = np.nanstd(sub, axis=0, ddof=0)
        ok = (s > 0) & ~np.isnan(m)
        z = np.full_like(data.imb5_score[i], np.nan)
        z[ok] = (data.imb5_score[i, ok] - m[ok]) / s[ok]
        z_list.append(z)
    signal = np.nanmean(z_list, axis=0)
    return signal.astype(np.float32)
```

**问题**：
- 每天算 21 次 z-score，计算量大
- lookback=273（252+21），数据量更大
- 实际提交时轮询超时（600s 不够），导致失败

#### 方案 B：store 环形缓冲区，lookback=252

```python
@alpha(
    data=['imb5_score'],
    store=[{"name": "z_buf", "dims": "xi", "extend": np.float32(np.nan)}],
)
def auto_alpha(data, store):
    # ts_zscore(imb5_score, 252) — 每天只算 1 次
    m = np.nanmean(data.imb5_score, axis=0)
    s = np.nanstd(data.imb5_score, axis=0, ddof=0)
    ok = (s > 0) & ~np.isnan(m)
    z = np.full_like(data.imb5_score[-1], np.nan)
    z[ok] = (data.imb5_score[-1, ok] - m[ok]) / s[ok]

# Store 环形缓冲区：FIFO shift + append
    if store.z_buf is None:
        store.z_buf = np.full((21, z.shape[0]), np.nan, dtype=np.float32)
    store.z_buf[:-1] = store.z_buf[1:]  # 丢弃最旧一行
    store.z_buf[-1] = z                 # 追加今天 z-score

# ts_mean(z_buf, 21)
    signal = np.nanmean(store.z_buf, axis=0)
    return signal.astype(np.float32)
```

**优势**：
- 每天只算 1 次 z-score，不是 21 次
- lookback=252（少了 21 天数据量）
- 提交成功，耗时 ~470s

### 三、Store 的核心规则（踩坑总结）

| 规则 | 说明 |
|------|------|
| `dims` 合法值 | SDK 源码 `_DIMENSIONS = ["i", "x"]`，组合为 `"i"` `"x"` `"xi"` `"ii"` |
| `"i"` = 股票轴 | universe 扩张时自动 padding |
| `"x"` = 自由轴 | 自己管理长度，不会自动扩展 |
| `"ii"` = 工具×工具矩阵 | 如相关矩阵，universe 扩张时自动扩展行列，需手动修复对角线（见下文） |
| `extend` 必须是 numpy 标量 | ✅ `np.float32(0)` `np.float64(np.nan)` ❌ `0` `0.0` `np.nan` |
| 首次调用 store 是 None | 必须手动建数组初始化 |
| 注意类型提升 | `np.nanmean` / `np.nanstd` 会将 float32 提升到 float64，返回前记得 `.astype(np.float32)` |
| 数据只读 | 不能修改 data.xxx，必须先 `.copy()` |
| 返回类型 | 必须 `astype(np.float32)` |

### 四、进阶 Store 技巧

#### 4.1 dims="ii"：工具×工具矩阵

```python
store=[{"name": "corr", "dims": "ii", "extend": np.float64(0)}]
```

用于相关矩阵等 `[n_instruments, n_instruments]` 场景。universe 扩张时行列自动扩展，但**新增工具的对角线需手动修复**（平台会填 0）：

```python
n = data.returns.shape[1]
if store.corr is None:
    store.corr = np.eye(n, dtype=np.float64)
    store.prev_n = n
else:
    if n > store.prev_n:
        store.corr[n-1, n-1] = 1.0  # 修复对角线
        store.prev_n = n
```

#### 4.2 无类型 store 的手动 padding

如果用了普通字符串声明 store，universe 增长时需要手动 pad：

```python
@alpha(data=["returns"], store=["my_cache"])
def alpha(data, store):
    n = data.returns.shape[1]
    if store.my_cache is None:
        store.my_cache = np.zeros(n, dtype=np.float32)
    elif store.my_cache.shape[-1] < n:
        # 手动 padding
        store.my_cache = np.pad(store.my_cache, (0, n - store.my_cache.shape[-1]),
                                mode='constant', constant_values=np.nan)
```

#### 4.3 Warm-start：预填缓冲区消除冷启动

直接使用方案 B 时，store 缓冲区初始全是 NaN，前 21 天 ts_mean 算出来是 NaN。顾问 JX79797 (Rank 9) 的帖子提出了 **warm-start** 方案：首次调用时用 lookback 数据回填缓冲区，消除冷启动期：

```python
def _warmup_z_buf(data, n_inst):
    """Pre-fill z_buf from lookback data so buffer isn't cold."""
    buf = np.full((21, n_inst), np.nan, dtype=np.float32)
    for k in range(21):
        sub = data.imb5_score[-252 - k : -k if k > 0 else None]
        m = np.nanmean(sub, axis=0)
        s = np.nanstd(sub, axis=0, ddof=0)
        ok = (s > 0) & ~np.isnan(m)
        z = np.full(n_inst, np.nan)
        z[ok] = (sub[-1, ok] - m[ok]) / s[ok]
        buf[21 - 1 - k] = z
    return buf

@alpha(
    data=['imb5_score'],
    store=[{"name": "z_buf", "dims": "xi", "extend": np.float32(np.nan)}],
)
def auto_alpha(data, store):
    m = np.nanmean(data.imb5_score, axis=0)
    s = np.nanstd(data.imb5_score, axis=0, ddof=0)
    ok = (s > 0) & ~np.isnan(m)
    z = np.full_like(data.imb5_score[-1], np.nan)
    z[ok] = (data.imb5_score[-1, ok] - m[ok]) / s[ok]

if store.z_buf is None:
        store.z_buf = _warmup_z_buf(data, z.shape[0])
    store.z_buf[:-1] = store.z_buf[1:]
    store.z_buf[-1] = z

signal = np.nanmean(store.z_buf, axis=0)
    return signal.astype(np.float32)
```

#### 4.4 vstack 截断模式（替代环形缓冲区）

HZ32281 的帖子用了另一种方式——每次 vstack 追加新行，然后只保留后 N 行：

```python
new_cache = np.vstack([store.rank_cache, today_rank[np.newaxis, :]])
store.rank_cache = new_cache[-RANK_DAYS:]
```

每次分配新内存，适合小窗口（N < 100）；大窗口建议用 FIFO shift。

#### 4.5 EWMA 状态持久化（dims="i"）

```python
store=[{"name": "ewma", "dims": "i", "extend": np.float32(0)}]
# 每日更新
if store.ewma is None:
    store.ewma = np.zeros(data.returns.shape[1], dtype=np.float32)
store.ewma = 0.9 * store.ewma + 0.1 * today_value
```

### 五、Lookback 选取建议

| lookback | 窗口大小 | 适用场景 | 模拟耗时 |
|----------|---------|---------|---------|
| 30 | 31天 | 快速迭代测试 | ~2-3 分钟 |
| 63 | 64天 | 季度数据 | ~3-5 分钟 |
| 120 | 121天 | 半年数据 | ~5-8 分钟 |
| 252 | 253天 | 年度数据 | ~10-15 分钟 |

顾问 JX79797 (Rank 9) 的转换器使用 **max_window × 2** 的经验公式自动推断 lookback。对于我们的例子，最大窗口是 252（ts_zscore 的窗口），所以 lookback=504。但实测 lookback=252 也够用，因为 store 环形缓冲区自己保存中间结果。

### 六、时序分析

#### 轮询耗时数据（来自实际提交）

我们的 alpha 提交轮询日志（lookback=252, 单字段, store 方案）：

```
Status: 201
Waiting 5.0s... × 96 次 = ~480 秒（约 8 分钟）
```

#### 超时经验

第一次用方案 A（lookback=273，每天 21 次 z-score），工具 600s 超时被 kill。改用方案 B（store，lookback=252，每天 1 次 z-score），~480s 成功。

建议：
- API 轮询设 5s 间隔
- 超时至少设 600s（10 分钟）
- 用后台任务提交，避免前端超时中断
- 复杂 alpha 预估 5-10 分钟

### 总结

Store 是 Python Alpha 实现跨周期状态持久化的核心工具。它的本质是将全量重算（O(n) 全历史）转为增量更新（O(1) 当日），在减少 lookback、降低计算量、避免超时方面非常有价值。

关键就是记住几点：
1. dims 用 i/x/xi/ii 组合
2. extend 必须 numpy scalar
3. 首次调用记得初始化
4. np.nanmean 会提升类型，返回前 astype(np.float32)
5. 大窗口用 FIFO shift，小窗口可以 vstack 截断
6. 考虑 warm-start 预填缓冲区避免冷启动

### 参考帖子

- [HZ32281] [Python Alpha 挑战赛] 基于 skill: brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化 —  [[L2] [Python Alpha 挑战赛] 基于skill brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化_40796757798807.md]([L2] [Python Alpha 挑战赛] 基于skill brain-simAlphasinBatch-and-track 的 Python Alpha 迭代工作流代码优化_40796757798807.md) 
- [顾问 JX79797 (Rank 9)] [Python Alpha 挑战赛] AI Agent 自动将 Fast Expression 转为 Python Alpha 并回测经验分享 —  [[L2] [Python Alpha 挑战赛] AI Agent 自动将 Fast Expression 转为 Python Alpha 并回测经验分享_40740029001239.md]([L2] [Python Alpha 挑战赛] AI Agent 自动将 Fast Expression 转为 Python Alpha 并回测经验分享_40740029001239.md)

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 每次都干货满满啊

这就去试试看

=============================================================================


---

### 技术对话片段 31 (原帖: [Python Alpha 挑战赛]半自动化的python alpha挖掘思路经验分享)
- **原帖链接**: [Commented] [Python Alpha 挑战赛]半自动化的python alpha挖掘思路经验分享.md
- **时间**: 21天前

**提问/主帖背景 (WX87649)**:
**1. Idea**

该 Alpha 假设短周期机器学习预测信号在高流动性股票中更可靠。首先对 predicted_first_quantile_five_day_return_14 取 3 日均值以降低噪声，再进行横截面排序和子行业内排序，提取行业中性化后的个股相对强弱。

同时，使用 20 日平均成交量的横截面分位数作为流动性门控。仅当股票流动性排名高于 22% 时更新信号；低流动性股票退出持仓。该设计减少了低流动性标的中的预测误差和交易成本风险。

**2. 实现**

Python Alpha 使用 NumPy 实现了可复用的排序算子与状态机：

```
liquidity_rank = rank01(volume_mean, universe)prediction_rank = rank01(prediction_mean, universe)candidate = group_rank01(prediction_rank, subindustry, universe)result[liquidity_rank > 0.22] = candidate[liquidity_rank > 0.22]result[liquidity_rank <= 0.22] = np.nanstore.previous_alpha = result
```

**3.提交的页面展示：**

**
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 05/31/2026 EDT
> anonymous
> Add Alpha to a List
> Code
> o OS Summary
> Period
> IS
> 05
> 1
> from brain.alphas import alpha
> . Regular Alpha
> Pyramid theme: EURIDIIPV X1.1
> Pyramid theme: EURIDI/OTHER X1.6
> 2
> iport numpy
> a5
> mp
> 3
> import numpy.typing
> as
> npt
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 01/01/2024 EST
> 5
> Simulation
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Pre-Close Sharpe
> Pre-Close Ratio
> Self-Correlation
> Settings
> Instrument Type:
> Equity
> Delay:
> Lookback:
> 256
> Region:
> EUR
> Truncation:
> 0.08
> Max Trade:
> Off
> Universe:
> TOP2500
> Neutralization:Slow
> Fast
> Max Position:
> Off
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Language:
> Python
> Factors
> Decay:
> Pasteurization:
> On
> 2014
> 6.83
> 30.68%
> 3.88
> 9.91%
> 0.349
> 6.46%o。
> 1288
> 1322
> 2015
> 4.97
> 30.38%
> 2.57
> 8.10%
> 0.579
> 5.33%0。
> 1351
> 1367
> 2016
> 7.05
> 31.31 %
> 4.07
> 10.439
> 0.259
> 6.6796。
> 1335
> 1380
> Clone Alpha 
> 2017
> 4.21
> 30.499
> 1.88
> 6.119
> 1.099
> 4.01%o。
> 1461
> 1487
> 2018
> 5.23
> 31.249
> 2.69
> 8.279
> 0.6796
> 5.30%o。
> 1449
> 1475
**

**2.1 造轮子：自定义 Operator**

rank01() 是自定义横截面分位数算子。它使用稳定排序处理有效股票，并对相同数值分配平均排名。该实现显式过滤NaN 和无限值，输出归一化到 [0, 1]。

group_rank01()在每个 subindustry内调用 rank01()，并过滤无效行业编码。相比直接依赖内置算子，Python 版本可以精确控制缺失值、并列值和行业分组边界的处理方式。

此外，store.previous_alpha 实现了状态持有逻辑：仅在流动性条件满足时更新信号，否则清空持仓。该复合逻辑可以视为一个可扩展的 stateful liquidity-gated group-rank operator。

2.2 降相关 / 提表现

Python 版本由 Fast Expression Alpha 改造而来，但不再完全依赖内置算子的执行语义。自定义排序、缺失值过滤、行业编码校验和状态更新会改变边界股票的入选结果，使每日持仓路径与原版本不完全一致。

平台详情显示，Python 版本的换手率由 `32.98%` 降至 `31.38%`，下降 `1.60` 个百分点。原因是更严格的有效值过滤和流动性门控减少了边界股票的频繁切换。

python alpha由于不依靠官方提供的operator，相关性是直接降低到0.6以下

对比图如下:
 
> [!NOTE] [图片 OCR 识别内容]
> 5,0OOK
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> 2,5OOK
> Prod Correlation
> Maximum
> Minimum
> Last Run: Mon, 06/01/2026
> 12:34 PM
> 0.6000
> -0.4191
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> IOOM
> Pnl
> Investability Constrained Pnl
> IM
> 訾
> IOk
> o IS Testing Status
> Period
> TRAIN
> TEST
> IS
> 05
> 罡
> 100
> 皂
> 8 PASS
> 1 WARNING
> 0,01
> 4 PENDING
> 89
> 8?
> 89
> 09
> 0^ 0?
> 0
> 01
> 9
> 9'
> 01
> O
> 0?
> 0?一
> 0一
> 01一
> 0*
> 0:
> 0
> -0.7
> ?
> -0.3
> 0.8
> 1.0
> -0.4
> -0.2
> -0.1
> 0.1
> 0.2
> 0.3
> 0.9
> 0.0...
> 0.4...
> -0.1.
> 0.1.
> 0.3.
> 0.8.
> 0.9.
> 1.0.
> 0.5.
> 0.4.
> 0.3.
> 0.2.
  
> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run: Mon, 06/01/2026,12:40 PM
> 0.5427
> -0.3402
> IOOM
> IM
> 訾
> IOk
> 罡
> }
> 100
> C
> 8
> 8:
> 9
> 9:
> C"
> ( :
> 8
> 0*
> 0*
> 0.
> 0
> 0:
> -0.8
> -0.7
> -0.5
> 0.5
> 0.6
> 0.7
> 0.8
> 1.0
> -0.4
> -0.3
> -0.2
> -0.1
> 0.0
> 0.1
> 0.2
> 0.3
> 0.4
> 0.9
> 0.0..
> 0.2...
> 0.4..
> -0.1.
> 0.1._
> 0.3..
> 0.5..
> 0.7 .
> -0.7.
> -0.2..
> -1.0.
> -0.5..
> -0.4.
> -0.3.
 
 **关于半自动化构建python alpha的挖掘思路**


> [!NOTE] [图片 OCR 识别内容]
> operators信息
> 官方python 文档
> 数据分析
> 数据分析结果
> 系统提示词
> alpha 产出
> skills 总结
> 合法的示例
> 量化论文实现要点
> python
 

1.首先可以依据AI打工人中提供的两个skills:brain-dataset-exploration-general与brain-datafield-exploration-general
将这两个skill进行整合,成为一个专职与数据分析的skills。用途:快速发现信号强的数据字段,由大到小，缩小挖掘复杂度与时间
2.通过mcp服务获取的operator作为创建新的operator的参照,为了增加理论支撑,你可以采用arxiv-mcp服务让llm去直接搜索相关的论文，将其论文中设计的操作办法通过python语言进行实现，增强其独特性

3.官方的资料-llm搞懂python alpha的核心支撑

首先将官方文档进行复制(关于平台中的回测的示例)，形成md文档，在结合官方的示例python alpha形成理论支撑,通过一份系统提示词(已经有顾问给出，这里不再赘述)让llm进行python alpha的操作--这是kunqi老师教的方法

4.依据返回结果，你可以在brain lab上进行数据分析的操作并重复迭代，最终产出python alpha 结果

关于这里的半自动化的python alpha挖掘，只是做思路呈现.后续的实际操作，我会在下一篇帖子呈现

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 这波半自动化的alpha挖掘思路超级赞

这就准备在我的工作流中试试看

=============================================================================


---

### 技术对话片段 32 (原帖: [Python Alpha 挑战赛]半自动化的python alpha挖掘思路经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [Python Alpha 挑战赛]半自动化的python alpha挖掘思路经验分享_40870826319511.md
- **时间**: 21天前

**提问/主帖背景 (WX87649)**:
**1. Idea**

该 Alpha 假设短周期机器学习预测信号在高流动性股票中更可靠。首先对 predicted_first_quantile_five_day_return_14 取 3 日均值以降低噪声，再进行横截面排序和子行业内排序，提取行业中性化后的个股相对强弱。

同时，使用 20 日平均成交量的横截面分位数作为流动性门控。仅当股票流动性排名高于 22% 时更新信号；低流动性股票退出持仓。该设计减少了低流动性标的中的预测误差和交易成本风险。

**2. 实现**

Python Alpha 使用 NumPy 实现了可复用的排序算子与状态机：

```
liquidity_rank = rank01(volume_mean, universe)prediction_rank = rank01(prediction_mean, universe)candidate = group_rank01(prediction_rank, subindustry, universe)result[liquidity_rank > 0.22] = candidate[liquidity_rank > 0.22]result[liquidity_rank <= 0.22] = np.nanstore.previous_alpha = result
```

**3.提交的页面展示：**

**
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 05/31/2026 EDT
> anonymous
> Add Alpha to a List
> Code
> o OS Summary
> Period
> IS
> 05
> 1
> from brain.alphas import alpha
> . Regular Alpha
> Pyramid theme: EURIDIIPV X1.1
> Pyramid theme: EURIDI/OTHER X1.6
> 2
> iport numpy
> a5
> mp
> 3
> import numpy.typing
> as
> npt
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 01/01/2024 EST
> 5
> Simulation
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Pre-Close Sharpe
> Pre-Close Ratio
> Self-Correlation
> Settings
> Instrument Type:
> Equity
> Delay:
> Lookback:
> 256
> Region:
> EUR
> Truncation:
> 0.08
> Max Trade:
> Off
> Universe:
> TOP2500
> Neutralization:Slow
> Fast
> Max Position:
> Off
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Language:
> Python
> Factors
> Decay:
> Pasteurization:
> On
> 2014
> 6.83
> 30.68%
> 3.88
> 9.91%
> 0.349
> 6.46%o。
> 1288
> 1322
> 2015
> 4.97
> 30.38%
> 2.57
> 8.10%
> 0.579
> 5.33%0。
> 1351
> 1367
> 2016
> 7.05
> 31.31 %
> 4.07
> 10.439
> 0.259
> 6.6796。
> 1335
> 1380
> Clone Alpha 
> 2017
> 4.21
> 30.499
> 1.88
> 6.119
> 1.099
> 4.01%o。
> 1461
> 1487
> 2018
> 5.23
> 31.249
> 2.69
> 8.279
> 0.6796
> 5.30%o。
> 1449
> 1475
**

**2.1 造轮子：自定义 Operator**

rank01() 是自定义横截面分位数算子。它使用稳定排序处理有效股票，并对相同数值分配平均排名。该实现显式过滤NaN 和无限值，输出归一化到 [0, 1]。

group_rank01()在每个 subindustry内调用 rank01()，并过滤无效行业编码。相比直接依赖内置算子，Python 版本可以精确控制缺失值、并列值和行业分组边界的处理方式。

此外，store.previous_alpha 实现了状态持有逻辑：仅在流动性条件满足时更新信号，否则清空持仓。该复合逻辑可以视为一个可扩展的 stateful liquidity-gated group-rank operator。

2.2 降相关 / 提表现

Python 版本由 Fast Expression Alpha 改造而来，但不再完全依赖内置算子的执行语义。自定义排序、缺失值过滤、行业编码校验和状态更新会改变边界股票的入选结果，使每日持仓路径与原版本不完全一致。

平台详情显示，Python 版本的换手率由 `32.98%` 降至 `31.38%`，下降 `1.60` 个百分点。原因是更严格的有效值过滤和流动性门控减少了边界股票的频繁切换。

python alpha由于不依靠官方提供的operator，相关性是直接降低到0.6以下

对比图如下:
 
> [!NOTE] [图片 OCR 识别内容]
> 5,0OOK
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> 2,5OOK
> Prod Correlation
> Maximum
> Minimum
> Last Run: Mon, 06/01/2026
> 12:34 PM
> 0.6000
> -0.4191
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> IOOM
> Pnl
> Investability Constrained Pnl
> IM
> 訾
> IOk
> o IS Testing Status
> Period
> TRAIN
> TEST
> IS
> 05
> 罡
> 100
> 皂
> 8 PASS
> 1 WARNING
> 0,01
> 4 PENDING
> 89
> 8?
> 89
> 09
> 0^ 0?
> 0
> 01
> 9
> 9'
> 01
> O
> 0?
> 0?一
> 0一
> 01一
> 0*
> 0:
> 0
> -0.7
> ?
> -0.3
> 0.8
> 1.0
> -0.4
> -0.2
> -0.1
> 0.1
> 0.2
> 0.3
> 0.9
> 0.0...
> 0.4...
> -0.1.
> 0.1.
> 0.3.
> 0.8.
> 0.9.
> 1.0.
> 0.5.
> 0.4.
> 0.3.
> 0.2.
  
> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run: Mon, 06/01/2026,12:40 PM
> 0.5427
> -0.3402
> IOOM
> IM
> 訾
> IOk
> 罡
> }
> 100
> C
> 8
> 8:
> 9
> 9:
> C"
> ( :
> 8
> 0*
> 0*
> 0.
> 0
> 0:
> -0.8
> -0.7
> -0.5
> 0.5
> 0.6
> 0.7
> 0.8
> 1.0
> -0.4
> -0.3
> -0.2
> -0.1
> 0.0
> 0.1
> 0.2
> 0.3
> 0.4
> 0.9
> 0.0..
> 0.2...
> 0.4..
> -0.1.
> 0.1._
> 0.3..
> 0.5..
> 0.7 .
> -0.7.
> -0.2..
> -1.0.
> -0.5..
> -0.4.
> -0.3.
 
 **关于半自动化构建python alpha的挖掘思路**


> [!NOTE] [图片 OCR 识别内容]
> operators信息
> 官方python 文档
> 数据分析
> 数据分析结果
> 系统提示词
> alpha 产出
> skills 总结
> 合法的示例
> 量化论文实现要点
> python
 

1.首先可以依据AI打工人中提供的两个skills:brain-dataset-exploration-general与brain-datafield-exploration-general
将这两个skill进行整合,成为一个专职与数据分析的skills。用途:快速发现信号强的数据字段,由大到小，缩小挖掘复杂度与时间
2.通过mcp服务获取的operator作为创建新的operator的参照,为了增加理论支撑,你可以采用arxiv-mcp服务让llm去直接搜索相关的论文，将其论文中设计的操作办法通过python语言进行实现，增强其独特性

3.官方的资料-llm搞懂python alpha的核心支撑

首先将官方文档进行复制(关于平台中的回测的示例)，形成md文档，在结合官方的示例python alpha形成理论支撑,通过一份系统提示词(已经有顾问给出，这里不再赘述)让llm进行python alpha的操作--这是kunqi老师教的方法

4.依据返回结果，你可以在brain lab上进行数据分析的操作并重复迭代，最终产出python alpha 结果

关于这里的半自动化的python alpha挖掘，只是做思路呈现.后续的实际操作，我会在下一篇帖子呈现

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 这波半自动化的alpha挖掘思路超级赞

这就准备在我的工作流中试试看

=============================================================================


---

### 技术对话片段 33 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] [经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (LZ63377)**:

> [!NOTE] [图片 OCR 识别内容]
> Genluy
> Synals
> Pramt
> Cobined
> Combinu
> Combttd
> CoIUIU
> 10l
> 01
> CmTPte[
> Alpha
> OwCTPnol
> Solacten
> ISIT TSI5
> Perlomance
> UOh
> Mpha
> Felormnce
> JertormarCe
> P2TIOTIaITCC
> 1 1Aq
> 1763377I
> Gold
> old
> 400
> LZEAATT
> 353
> 4
> THTA70
> Uer
> O
> Emcn
> T
> 298


大家好，标题整蛊一下O(∩_∩)O，我是练习量化4个月的新人顾问Ricardo。2月上旬平台更新了combine和vf，当时我的combine从-1.2一举跃升至3.18，提升超4，前后只隔一个月悬殊却如此之大，属实是个值得研究的典型样本。因此我发布了自己去年11，12月的提交数据，希望能够带给大家一些启发，感兴趣的可以看看，能够更好地衔接本文👉：  [../顾问 MS51256 (Rank 28)/[Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享.md](../顾问 MS51256 (Rank 28)/[Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享.md)

再到后来，1月os期更新导致所有存货全部失效，加上那段时间比较忙，所以提交量相比12月是减少的。我本以为这次更新combine下滑在所难免，结果没想到总池combine再创新高，飙升至3.58，位居全球第一！同时ppa池combine也升至1.85，属实是意外之喜。这样看来，我的提交策略确实是有可取之处的，那就书接上回，继续展开讲讲吧！


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combinea Apha
> POwerPool
> SEIECEOAphs
> Combinea Osmosis
> 0.97
> Combin」
> 400
> 090
> 3,00
> 0.30
> 00
> 0,70
> 1.00
> 050
> 0,00
> 0.50
> 1.00
> 015
> 1.77
> 202503
> 202509
> 202510
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202501


先看下1月的提交数据（建议ctrl+放大观看）：


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
> IND
> 01
> 18
> 3.59
> 2.145
> 2.2039
> 4.21
> 2.25
> 2.3839
> 0.003831
> 0.001766
> 0.001897
> 0.2149
> 0.1455
> 0.1455
> USA
> 12
> 3.03
> 1.56
> 1.7492
> 2.56
> 1.885
> 1.9217
> 0.007154
> 0.001891
> 002321
> 0.2848
> 0.0953
> 0.1094


1月我只做了USA和IND两个区,数量不多，不过sharpe、fitness、margin，等关键指标都还不错，无论是中位数还是平均值都远高于提交底线。

再看上次combine出分时的总池数据与本次的对照：


> [!NOTE] [图片 OCR 识别内容]
> Ln]
> Cm』
> m
> Cm
> Cd
> SN
> C
> |
> ST 辜
> U $ [
> Us
> Tdo
> a
> e
> O4


可以发现变化不大，说明之前的策略确实是可行的，1月时我我又对策略进行了更多细化，得出了以下的结论和猜想：

1. **重视近几年表现。** 因子的预测能力都是有时限的，有些因子指标很漂亮但2year sharpe不达标，这很可能说明此因子的快要丧失预测能力了，os表现搞不好会一泻千里。即使2year sharpe合格，也要看是否是其中一年的优秀表现掩盖了另一年乏力的情况。这条规则也可以反过来利用，如果一个因子近几年表现很好但前中期略有起伏，那也是可以容忍的。
2. **注意开启maxtrade后的表现。** 有些因子在开启maxtrade之前表现一路长虹，开启之后却基本是一条水平线，这种最好不要提交。我的理解是开启maxtrade可能更接近实盘表现，如果开启后仍能保持sharpe>1,fitness>0.5的话，就算不错了。
3. **注意return的隐藏底线。** 如果说margin的高低决定了策略赚钱的效率，而return的高低则决定了这个策略究竟有没有投产价值，说白了，你的return如果连这个地区的银行年化利率都比不过，那在风险更高的市场里还有什么意义呢？
4. **关于最大回撤的一点看法。** 我之前一直是秉持着最大回撤不能超过return这个观点的，但架不住有些策略就是高风险高收益的。于是我把条件放宽为最大回撤不能出现在近3年，并且除最大回撤以外，每年的小回撤也不能太高，否则仍然说明此策略的稳健性不够。
5. **精选PPA池。** PPA池combine是可以通过手动增删标签来控制的，比总池combine相对容易掌控，那自然要优中选优。首先，按RA的标准来筛自然不必多说，一月更新的os期表现也是重要依据，再就是把前4条综合起来应用，核心要义是保留有上升趋势的因子。
6. **换手率对Osmosis影响的猜想。** 每日os和os combine还是有很大区别的，我了解到有很多顾问的每日os不算差，但os combine却相差甚远，反之亦然。这一方面跟每日os是rank的有关，有时可能单纯的是在比谁亏的少；另一方面，我觉得这跟换手率多少有些关系，低换手率的因子可能会因为单日没有触发交易条件而只守着老本，而os combine的时间窗口相对较长，更能体现出因子真实的表现来。所以，如果想要每日和combine两开花，还是尽量避免给换手过低的因子赋高分吧。

最后是我做了4个月顾问之后的一点感想，做量化不能陷入“科学迷信”。所谓“科学迷信”最开始是指19世纪物理学家们认为只要知道所有粒子的初始状态，并用牛顿力学算一遍，就能精确算出未来的一切，但后来大家也都知道了，一个名为蝴蝶效应的现象打破了这个幻想。做量化时，我们也要清楚，能长期准确预测市场走向的策略是不存在的，或者说以现在的算力是做不到的，但我们至少可以避免提交即将失效的因子，让自己策略的当打之年延长一些。

祝大家在即将结算的这赛季猛猛上分，季度奖和base拿到手软！点个赞吧，感谢！！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享

这combine真是让人羡慕啊

=============================================================================


---

### 技术对话片段 34 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] [经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享_39224484288663.md
- **时间**: 3个月前

**提问/主帖背景 (LZ63377)**:

> [!NOTE] [图片 OCR 识别内容]
> Genluy
> Synals
> Pramt
> Cobined
> Combinu
> Combttd
> CoIUIU
> 10l
> 01
> CmTPte[
> Alpha
> OwCTPnol
> Solacten
> ISIT TSI5
> Perlomance
> UOh
> Mpha
> Felormnce
> JertormarCe
> P2TIOTIaITCC
> 1 1Aq
> 1763377I
> Gold
> old
> 400
> LZEAATT
> 353
> 4
> THTA70
> Uer
> O
> Emcn
> T
> 298


大家好，标题整蛊一下O(∩_∩)O，我是练习量化4个月的新人顾问Ricardo。2月上旬平台更新了combine和vf，当时我的combine从-1.2一举跃升至3.18，提升超4，前后只隔一个月悬殊却如此之大，属实是个值得研究的典型样本。因此我发布了自己去年11，12月的提交数据，希望能够带给大家一些启发，感兴趣的可以看看，能够更好地衔接本文👉：  [[L2] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md]([L2] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md)

再到后来，1月os期更新导致所有存货全部失效，加上那段时间比较忙，所以提交量相比12月是减少的。我本以为这次更新combine下滑在所难免，结果没想到总池combine再创新高，飙升至3.58，位居全球第一！同时ppa池combine也升至1.85，属实是意外之喜。这样看来，我的提交策略确实是有可取之处的，那就书接上回，继续展开讲讲吧！


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combinea Apha
> POwerPool
> SEIECEOAphs
> Combinea Osmosis
> 0.97
> Combin」
> 400
> 090
> 3,00
> 0.30
> 00
> 0,70
> 1.00
> 050
> 0,00
> 0.50
> 1.00
> 015
> 1.77
> 202503
> 202509
> 202510
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202501


先看下1月的提交数据（建议ctrl+放大观看）：


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
> IND
> 01
> 18
> 3.59
> 2.145
> 2.2039
> 4.21
> 2.25
> 2.3839
> 0.003831
> 0.001766
> 0.001897
> 0.2149
> 0.1455
> 0.1455
> USA
> 12
> 3.03
> 1.56
> 1.7492
> 2.56
> 1.885
> 1.9217
> 0.007154
> 0.001891
> 002321
> 0.2848
> 0.0953
> 0.1094


1月我只做了USA和IND两个区,数量不多，不过sharpe、fitness、margin，等关键指标都还不错，无论是中位数还是平均值都远高于提交底线。

再看上次combine出分时的总池数据与本次的对照：


> [!NOTE] [图片 OCR 识别内容]
> Ln]
> Cm』
> m
> Cm
> Cd
> SN
> C
> |
> ST 辜
> U $ [
> Us
> Tdo
> a
> e
> O4


可以发现变化不大，说明之前的策略确实是可行的，1月时我我又对策略进行了更多细化，得出了以下的结论和猜想：

1. **重视近几年表现。** 因子的预测能力都是有时限的，有些因子指标很漂亮但2year sharpe不达标，这很可能说明此因子的快要丧失预测能力了，os表现搞不好会一泻千里。即使2year sharpe合格，也要看是否是其中一年的优秀表现掩盖了另一年乏力的情况。这条规则也可以反过来利用，如果一个因子近几年表现很好但前中期略有起伏，那也是可以容忍的。
2. **注意开启maxtrade后的表现。** 有些因子在开启maxtrade之前表现一路长虹，开启之后却基本是一条水平线，这种最好不要提交。我的理解是开启maxtrade可能更接近实盘表现，如果开启后仍能保持sharpe>1,fitness>0.5的话，就算不错了。
3. **注意return的隐藏底线。** 如果说margin的高低决定了策略赚钱的效率，而return的高低则决定了这个策略究竟有没有投产价值，说白了，你的return如果连这个地区的银行年化利率都比不过，那在风险更高的市场里还有什么意义呢？
4. **关于最大回撤的一点看法。** 我之前一直是秉持着最大回撤不能超过return这个观点的，但架不住有些策略就是高风险高收益的。于是我把条件放宽为最大回撤不能出现在近3年，并且除最大回撤以外，每年的小回撤也不能太高，否则仍然说明此策略的稳健性不够。
5. **精选PPA池。** PPA池combine是可以通过手动增删标签来控制的，比总池combine相对容易掌控，那自然要优中选优。首先，按RA的标准来筛自然不必多说，一月更新的os期表现也是重要依据，再就是把前4条综合起来应用，核心要义是保留有上升趋势的因子。
6. **换手率对Osmosis影响的猜想。** 每日os和os combine还是有很大区别的，我了解到有很多顾问的每日os不算差，但os combine却相差甚远，反之亦然。这一方面跟每日os是rank的有关，有时可能单纯的是在比谁亏的少；另一方面，我觉得这跟换手率多少有些关系，低换手率的因子可能会因为单日没有触发交易条件而只守着老本，而os combine的时间窗口相对较长，更能体现出因子真实的表现来。所以，如果想要每日和combine两开花，还是尽量避免给换手过低的因子赋高分吧。

最后是我做了4个月顾问之后的一点感想，做量化不能陷入“科学迷信”。所谓“科学迷信”最开始是指19世纪物理学家们认为只要知道所有粒子的初始状态，并用牛顿力学算一遍，就能精确算出未来的一切，但后来大家也都知道了，一个名为蝴蝶效应的现象打破了这个幻想。做量化时，我们也要清楚，能长期准确预测市场走向的策略是不存在的，或者说以现在的算力是做不到的，但我们至少可以避免提交即将失效的因子，让自己策略的当打之年延长一些。

祝大家在即将结算的这赛季猛猛上分，季度奖和base拿到手软！点个赞吧，感谢！！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享

这combine真是让人羡慕啊

=============================================================================


---

### 技术对话片段 35 (原帖: 三、 **比赛经验总结**)
- **原帖链接**: [Commented] 【AIAC20 冠军】关于比赛过程中一些经验的交流经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (LH44620)**:
自2024年10月加入WorldQuant BRAIN成为顾问，过去达到了Grand Master级别。并且在Super Alpha 组合竞赛SAC2025（Super Alpha Competition 2025）中荣获G2 组全球第一名。在AIAC 2.0 (AI Alphas Competition 2.0)中获得了全球第一的成绩。

虽然取得的名次还不错，可是就技术而言，我没有用多么先进与独特的技术，还是大家常用的LLMs ＋ MCP tools + Skills的形式。所以说关于技术的分享，就大概只能朝着 ***“为什么这个技术路线可行？”*** 的方向进行。再结合一点制作alpha方向选择的经验。

# 一、 **为什么这个技术路线可行？**

*下面是这个架构的抽象图示：*

*
> [!NOTE] [图片 OCR 识别内容]
> MASTER SIGNIFIER
> The Spark . Master Signifier
> tasks prompt
> BRAIN 8 NERVOUS SYSTEM
> (LLMs 88 human experience 88 contexl)
> NCrOCNps
> Inpu
> Valdge
> SKELETON
> (MCP toolsgghard-coding function)
> Hisloncal Dala Reposion
> CCCUIe
> Erccuie
> Anolze
> CLOSED LOOP EXECUTION MUSCLE
> CLOSED LOOP EXECUTION LUSCLE
> SUBIITALPHA
> SUBMITALPHA
> READ ERRORS
> READ ERRORS
> AUTO CORRECT
> AUTO CORRECT
*

将  **Alpha 模板、AI Agent 操作经验、个人直觉以及量化相关知识上下文** 注入到 LLMs 中，便构成了系统类似于人体中的  **‘大脑与神经系统’** （软性智能） **；** 而基于 **确定的函数、** 硬编码规则构建的 **MCP Tools** 与 **Skills，** 则代表了人体中的 **‘骨骼与肌肉’** （硬性结构） **。** 正是这些‘硬’的物理边界与执行框架，才确保了大脑这种‘软’的智能能够切实、有效地落地 **；** 针对每个具体任务输入 **的简短 Prompt** 则是 **‘主人能指’** (Master Signifier)——它是赋予目标、唤醒并驱动这具完整躯体开始运转的初始意志。

而在这个框架中，针对alpha制作中全流程的完整权限（制作alpha表达式→平台回测→分析回测结果→改进alpha表达式的逻辑→平台回测）我都是赋予AI agent的， **我认为这是很重要的一点** 。让AI agent完整的接触真实的物理世界。虽然目前的大语言模型（LLM）并不具备真正意义上的‘创造力’。它的核心能力是从海量训练数据中进行信息的整合与涌现，本质上依然是一个极其高级的工具。而人类在真正的探索发现和创造性直觉方面，具有不可替代的优势。 因此，AI 最完美的系统定位是‘高级执行者’： **由人类负责提供创意的火花和底层思路（从0到1），而让 AI 去承担那些繁重的代码落地与执行工作（从1到100）。** 所以，我把 AI 看作一个非常高级的工具，由人类提供创意想法，产生 **‘主人能指’** (Master Signifier)，而 AI 作为一个能和真实物理世界交互的完整个体负责执行。

这涉及到 **世界模型** 的概念。图灵奖得主、Meta 首席 AI 科学家杨立昆是当前“世界模型”最坚定、最有影响力的布道者。简单来说，当前的LLMs本质上还是根据前面的词去预测下一个词的 **相关性** 。而世界模型得到的是真实世界的 **因果关系** 。相关性回答的是“什么通常会一起出现？”，而因果性回答的是“为什么它会发生？”

回到AI Agent系统中：

**1.MCP Tools 与回测系统，就是这个世界的“物理引擎”**

在 OpenAI 的 Sora 中，“物理法则”是重力、光影和三维几何； 在AI Alpha 系统中， **“物理法则”就是金融市场的交易规则、因子的计算逻辑、以及严苛的回测机制（MCP Tools）。**  当你赋予 AI 调用回测引擎的权力时，你实际上是给了它一个 “真实世界的沙盒模拟器”。AI 不再只是凭空想象“这个因子可能会赚钱”（相关性幻觉），而是必须把因子放进沙盒里跑一遍，看看真实的市场数据会给出什么反馈（因果验证）。

**2.注入节点（Injection Nodes），就是这个世界的“先验法则”**

即便是人类和职业背景差距较大的人类之间进行交流，如果没有提前的知识对齐，那么交流起来也是十分的费劲的；对于LLMs来说同理。同样，你把 Alpha 模板、个人的量化经验和上下文注入给 LLM，就等同于 **硬编码了这个量化世界的“常识”与“先验法则”** 。这让 AI 在模拟推演时，起步就在一个极高的认知基线上，而不是像盲头苍蝇一样在无穷大的数学空间里随机试错。

**3.“给 AI 真实模拟全过程的权力”，就是完成了“反事实推演”**

真正的世界模型最核心的特征就是“基于动作的预测（Action-Conditional Prediction）”。 在本系统中，AI 提出一个 Alpha 公式（Action），系统通过代码执行和回测反馈真实结果（Future State）。在这个闭环中，LLM 不再是一个只懂文字接龙的复读机，它变成了一个 **具备“试错-反馈-自我修正”能力的自主智能体（Agentic System）** 。它在你的沙盒里推演因果，最终输出了经过物理世界（金融数据）检验的、真正有效的 Alpha。

这些结构其实都帮助LLMs构建出了一个针对于制作alpha的“小世界”（世界模型）。而正是这个世界模型，在促使AI Agent可以自主的按照我们的命令（主人能指）高效的制作出表现良好的Alpha 信号。

# 二、 **Alpha方向选择经验**

之前大家都是在用一二三阶及其各种变体去遍历单数据字段来得到operator较少的alpha信号。不瞒大家说，之前我也是这个路子，并且用这个方法，也拿到了Grand Master。可是，好景不长，在2025年最后一个季度，我的各种 **Combined Alpha Performance** 都急转直下。这是只有2025年8月后的表现。之前不论是 **Combined Alpha Performance** 还是 **Combined Selected Alpha Performance** 都大于2的。


> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化趋势
> Combined Alpha
> 0 Power Pool
> 0
> Selected Alpha
> 0 Combined Osmosis
> Combined
> 1.59
> 1.50
> 1.20
> 0.90
> G0
> 0.30
> 0.04
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202601


正好碰到了OS更新，我重新审视了一下自己之前提交的那么多alpha（1000+alpha）。也用了Super alpha去选择各个地区各种类型的alpha，查看其组合的性能。才发现自己之前提交的alpha的质量有多么的差。到了后来挑选优质alpha去参加 **Osmosis** 比赛，我发现甚至选不出几个真正优质的alpha去参加比赛。

在以上各种背景下，我做出了一个决定，放弃了对于之前制作alpha的标准。正所谓 **“重疾要用狠药”** 。我制作提交alpha的标准只有一个，就是一定要是一个优质的alpha。而不是使用了多少operator，使用了多少数据字段等。

而此次AIAIC 2.0取得的还不错的名次，算是对我更换决策的一个安慰。我的VF也产生了一个大V。当然 **Combined Alpha Performance** 还没有一转它的颓势。 **😂** 希望能有好的改变。


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Value Factor
> 0.84
> 0,80
> 0.70
> 0.60
> 0.50
> 0.40
> 0.33
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202601


在之前的大衰退时刻，唯一还有点希望的就是Weight Factor。只有它还在一点一点的向上蠕动，而没有往下掉。


> [!NOTE] [图片 OCR 识别内容]
> Weight 娈化趋势
> 4!!
> N
> 000
> 2qJ


而借助AI，我算是实现了一点点扶大厦之将倾的意味，将自己的 **Performance** 实现了一些起色。我相信借助AI，大家也一定能制作出许多高质量的alpha，从而实现高高的 **VF** ，高高的 **Combined Alpha Performance** ，稳定的 **Osmosis rank** ，以及 **Grand Master** ！

# 三、 **比赛经验总结**

其实这次比赛取得还不错的名次，也是正如在“研究小组”中所说，有不少运气好的成分。比如，甚至我没有看到需要回复才能参加AIAC2.0决赛的邮件，多亏在最后的之前Weijie老师被临时通知主持比赛，有了Weijie老师的提醒，我才没有错过最终的决赛，才有了后面的一切😂。

也是有了国区老师们以及顾问们的热心技术分享，正是站在了各位巨人的肩膀上，加上了一点点运气的加持，才有了取得这次比赛名次的机会！大家只要加油，相信肯定会再创辉煌！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

听了大佬的分享，收获了不少新的知识

希望我的AI agent也能变得这么强

=============================================================================


---

### 技术对话片段 36 (原帖: 三、 **比赛经验总结**)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【AIAC20 冠军】关于比赛过程中一些经验的交流经验分享_39621432305175.md
- **时间**: 2个月前

**提问/主帖背景 (LH44620)**:
自2024年10月加入WorldQuant BRAIN成为顾问，过去达到了Grand Master级别。并且在Super Alpha 组合竞赛SAC2025（Super Alpha Competition 2025）中荣获G2 组全球第一名。在AIAC 2.0 (AI Alphas Competition 2.0)中获得了全球第一的成绩。

虽然取得的名次还不错，可是就技术而言，我没有用多么先进与独特的技术，还是大家常用的LLMs ＋ MCP tools + Skills的形式。所以说关于技术的分享，就大概只能朝着 ***“为什么这个技术路线可行？”*** 的方向进行。再结合一点制作alpha方向选择的经验。

# 一、 **为什么这个技术路线可行？**

*下面是这个架构的抽象图示：*

*
> [!NOTE] [图片 OCR 识别内容]
> MASTER SIGNIFIER
> The Spark . Master Signifier
> tasks prompt
> BRAIN 8 NERVOUS SYSTEM
> (LLMs 88 human experience 88 contexl)
> NCrOCNps
> Inpu
> Valdge
> SKELETON
> (MCP toolsgghard-coding function)
> Hisloncal Dala Reposion
> CCCUIe
> Erccuie
> Anolze
> CLOSED LOOP EXECUTION MUSCLE
> CLOSED LOOP EXECUTION LUSCLE
> SUBIITALPHA
> SUBMITALPHA
> READ ERRORS
> READ ERRORS
> AUTO CORRECT
> AUTO CORRECT
*

将  **Alpha 模板、AI Agent 操作经验、个人直觉以及量化相关知识上下文** 注入到 LLMs 中，便构成了系统类似于人体中的  **‘大脑与神经系统’** （软性智能） **；** 而基于 **确定的函数、** 硬编码规则构建的 **MCP Tools** 与 **Skills，** 则代表了人体中的 **‘骨骼与肌肉’** （硬性结构） **。** 正是这些‘硬’的物理边界与执行框架，才确保了大脑这种‘软’的智能能够切实、有效地落地 **；** 针对每个具体任务输入 **的简短 Prompt** 则是 **‘主人能指’** (Master Signifier)——它是赋予目标、唤醒并驱动这具完整躯体开始运转的初始意志。

而在这个框架中，针对alpha制作中全流程的完整权限（制作alpha表达式→平台回测→分析回测结果→改进alpha表达式的逻辑→平台回测）我都是赋予AI agent的， **我认为这是很重要的一点** 。让AI agent完整的接触真实的物理世界。虽然目前的大语言模型（LLM）并不具备真正意义上的‘创造力’。它的核心能力是从海量训练数据中进行信息的整合与涌现，本质上依然是一个极其高级的工具。而人类在真正的探索发现和创造性直觉方面，具有不可替代的优势。 因此，AI 最完美的系统定位是‘高级执行者’： **由人类负责提供创意的火花和底层思路（从0到1），而让 AI 去承担那些繁重的代码落地与执行工作（从1到100）。** 所以，我把 AI 看作一个非常高级的工具，由人类提供创意想法，产生 **‘主人能指’** (Master Signifier)，而 AI 作为一个能和真实物理世界交互的完整个体负责执行。

这涉及到 **世界模型** 的概念。图灵奖得主、Meta 首席 AI 科学家杨立昆是当前“世界模型”最坚定、最有影响力的布道者。简单来说，当前的LLMs本质上还是根据前面的词去预测下一个词的 **相关性** 。而世界模型得到的是真实世界的 **因果关系** 。相关性回答的是“什么通常会一起出现？”，而因果性回答的是“为什么它会发生？”

回到AI Agent系统中：

**1.MCP Tools 与回测系统，就是这个世界的“物理引擎”**

在 OpenAI 的 Sora 中，“物理法则”是重力、光影和三维几何； 在AI Alpha 系统中， **“物理法则”就是金融市场的交易规则、因子的计算逻辑、以及严苛的回测机制（MCP Tools）。**  当你赋予 AI 调用回测引擎的权力时，你实际上是给了它一个 “真实世界的沙盒模拟器”。AI 不再只是凭空想象“这个因子可能会赚钱”（相关性幻觉），而是必须把因子放进沙盒里跑一遍，看看真实的市场数据会给出什么反馈（因果验证）。

**2.注入节点（Injection Nodes），就是这个世界的“先验法则”**

即便是人类和职业背景差距较大的人类之间进行交流，如果没有提前的知识对齐，那么交流起来也是十分的费劲的；对于LLMs来说同理。同样，你把 Alpha 模板、个人的量化经验和上下文注入给 LLM，就等同于 **硬编码了这个量化世界的“常识”与“先验法则”** 。这让 AI 在模拟推演时，起步就在一个极高的认知基线上，而不是像盲头苍蝇一样在无穷大的数学空间里随机试错。

**3.“给 AI 真实模拟全过程的权力”，就是完成了“反事实推演”**

真正的世界模型最核心的特征就是“基于动作的预测（Action-Conditional Prediction）”。 在本系统中，AI 提出一个 Alpha 公式（Action），系统通过代码执行和回测反馈真实结果（Future State）。在这个闭环中，LLM 不再是一个只懂文字接龙的复读机，它变成了一个 **具备“试错-反馈-自我修正”能力的自主智能体（Agentic System）** 。它在你的沙盒里推演因果，最终输出了经过物理世界（金融数据）检验的、真正有效的 Alpha。

这些结构其实都帮助LLMs构建出了一个针对于制作alpha的“小世界”（世界模型）。而正是这个世界模型，在促使AI Agent可以自主的按照我们的命令（主人能指）高效的制作出表现良好的Alpha 信号。

# 二、 **Alpha方向选择经验**

之前大家都是在用一二三阶及其各种变体去遍历单数据字段来得到operator较少的alpha信号。不瞒大家说，之前我也是这个路子，并且用这个方法，也拿到了Grand Master。可是，好景不长，在2025年最后一个季度，我的各种 **Combined Alpha Performance** 都急转直下。这是只有2025年8月后的表现。之前不论是 **Combined Alpha Performance** 还是 **Combined Selected Alpha Performance** 都大于2的。


> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化趋势
> Combined Alpha
> 0 Power Pool
> 0
> Selected Alpha
> 0 Combined Osmosis
> Combined
> 1.59
> 1.50
> 1.20
> 0.90
> G0
> 0.30
> 0.04
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202601


正好碰到了OS更新，我重新审视了一下自己之前提交的那么多alpha（1000+alpha）。也用了Super alpha去选择各个地区各种类型的alpha，查看其组合的性能。才发现自己之前提交的alpha的质量有多么的差。到了后来挑选优质alpha去参加 **Osmosis** 比赛，我发现甚至选不出几个真正优质的alpha去参加比赛。

在以上各种背景下，我做出了一个决定，放弃了对于之前制作alpha的标准。正所谓 **“重疾要用狠药”** 。我制作提交alpha的标准只有一个，就是一定要是一个优质的alpha。而不是使用了多少operator，使用了多少数据字段等。

而此次AIAIC 2.0取得的还不错的名次，算是对我更换决策的一个安慰。我的VF也产生了一个大V。当然 **Combined Alpha Performance** 还没有一转它的颓势。 **😂** 希望能有好的改变。


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Value Factor
> 0.84
> 0,80
> 0.70
> 0.60
> 0.50
> 0.40
> 0.33
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202601


在之前的大衰退时刻，唯一还有点希望的就是Weight Factor。只有它还在一点一点的向上蠕动，而没有往下掉。


> [!NOTE] [图片 OCR 识别内容]
> Weight 娈化趋势
> 4!!
> N
> 000
> 2qJ


而借助AI，我算是实现了一点点扶大厦之将倾的意味，将自己的 **Performance** 实现了一些起色。我相信借助AI，大家也一定能制作出许多高质量的alpha，从而实现高高的 **VF** ，高高的 **Combined Alpha Performance** ，稳定的 **Osmosis rank** ，以及 **Grand Master** ！

# 三、 **比赛经验总结**

其实这次比赛取得还不错的名次，也是正如在“研究小组”中所说，有不少运气好的成分。比如，甚至我没有看到需要回复才能参加AIAC2.0决赛的邮件，多亏在最后的之前Weijie老师被临时通知主持比赛，有了Weijie老师的提醒，我才没有错过最终的决赛，才有了后面的一切😂。

也是有了国区老师们以及顾问们的热心技术分享，正是站在了各位巨人的肩膀上，加上了一点点运气的加持，才有了取得这次比赛名次的机会！大家只要加油，相信肯定会再创辉煌！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

听了大佬的分享，收获了不少新的知识

希望我的AI agent也能变得这么强

=============================================================================


---

### 技术对话片段 37 (原帖: 【Alpha模板】模板群管理——动态优化淘汰低效模板)
- **原帖链接**: [Commented] 【Alpha模板】模板群管理动态优化淘汰低效模板.md
- **时间**: 5个月前

**提问/主帖背景 (SY43349)**:
## 引言

大家好我是sy。最近社区一直在缩减回测量想必大家可能会遇到很多困难。我是11月中旬成为条件顾问，到目前刚好一个半月了，这期间我总共提交了122个alpha，点了27个塔，平均每日回测大概2500左右，目前大概每天能稳定提交2-4个alpha（中间断交主要是临时有事。。）  我想跟大家分享一下目前我在实现低回测高产出方面的核心经验——动态管理模板群。  不过需要注意⚠️的是，由于代码和我自身的框架非常绑定无法单独抽离，以下内容主要以思路为主，希望能对大家有所帮助。


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> Z0O
> Oou
> so
> Oe
> 2 ^.
> @ ^8 ?D (
> S 3
> NO
> Nov
> NOV
> Noy
> Nov
> NOV
> NOv
> Noy
> NOV
> Nov
> NO
> ND
> Oec
> Dec
> Dec
> Dec
> Dec
> Oec
> Oec
> Dec
> Dec
> Dec
> 28。



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> so'so'soosososo'
> Oec
> Oec
> 2 ^
> ' 3
> Dec
> Dec
> Qec


## 模板群管理

想必大家手里都有很多模板，但是实际上不知道大家有没有进行过统计，不同模板的产出效率完全不同，甚至相差数百倍，长期在低效模板上的回测是没有意义的。因此，我想到了能不能多各个模板的产出结果进行统计，实现对低效模板的发现和剔除，从而提升这个模板群的效率。

### 抽象模板生成方法

#### alpha funcs 库

要实现动态的模板库管理需要对模板库进行一层抽象，它接受给定的模板库

```
ALPHA_FUNCS = [   "func1", "func2"]
```

#### 动态alpha 生成

随后generator根据给定的alpha funs生成所有的对应的alpha

```
    def generate_random_alphas(self, count):        """        🎲 使用多种策略生成指定数量的随机 Alpha。        使用多种生成器（fundamental, technical, sentiment 等），并按权重抽样。        """        print(f"\n🎲 正在生成 {count} 个随机 Alpha...")        # 所有可用的 Alpha 生成函数列表（涵盖基本面、技术面、情绪面、随机结构等）        all_alphas = []        alpha_funcs = []        generators = get_func_call_info().keys()        # 从每个生成器中随机抽取部分结果        for gen in tqdm(generators):            try:                gen = eval(f'{gen}')                result = gen()                result = list(set(result))                if result and len(result) > 0:                    # 每个生成器抽取 1 ~ min(建议数量, 实际数量) 个                    sample_size = min(count // len(generators) + 5, len(result))                    sample_size = max(1, sample_size)                    selected = ALPHA_SELECTOR.rng.sample(result, sample_size)                    tmp_selected = []                    # 去重                    for s in selected:                        if s not in all_alphas:                            tmp_selected.append(s)                                        all_alphas.append(tmp_selected)                    alpha_funcs.append([gen.__name__] * len(tmp_selected))            except Exception as e:                print(f"⚠️ 生成器 {gen.__name__} 出错: {e}")                continue        all_alphas = [alpha for sublist in all_alphas for alpha in sublist]        alpha_funcs = [func for sublist in alpha_funcs for func in sublist]        print(f"✅ 成功生成 {len(final_alphas)} 个随机 Alpha！")        return final_alphas, final_funcs
```

#### 模板标记

要做到跟踪统计首先是，做到准确的来源标记。这里我采用dataclass的方式在生成时就标记了alpha的来源。

```
@dataclassclass AlphaRecord:    """Data class for storing alpha information, extends evaluation result"""    expression: str    alpha_func: str    alpha_link: str = None    sharpe: float = None    subsharpe: float = None    fitness: float = None    turnover: float = None
```

#### 统计分析

通过上述步骤我们就可以追踪每个alpha 模板的表现，随后可以自己制定规则动态淘汰一些模板。我自己采用的是通过率淘汰的方式。以下是效果展示：


> [!NOTE] [图片 OCR 识别内容]
> ntig
> alpha_lunc_Call_intolson
> Jha"
> passed
> Count"
> 215,
> total_Count"
> 10566
> passed_ratio"
> 02034828695816771}
> late
> passed_count"
> 91,
> total_Count
> 5699
> passed_ratio"
> 015967713633970874}
> 033400
> Count
> 工70,
> LULOL
> Count"
> 15477,
> passed_ratio"
> 0.011371712864250177}
> alpha"
> passed_count"
> 31
> total_count
> 2790,
> passed_ratio"
> 011111111111111112};
> OnC
> JVU COCC
> UGLTCU
> COUIC
> g2;
> total_count"
> 10147
> passed_ratio"
> 00906671922735784},
> passed_count"
> 115,
> total_count"
> 18963
> passed_ratio"
> 0060644412803881245}
> Dassed_count"
> total_count"
> 9813,
> passed_ratio"
> 0007133394476714562}
> Dassed_Count"
> total
> Count"
> Dassed_ratio"
> 0邝


目前经过我对模板群的不断优化，现在每日平均可提交alpha已经可以做到1%的水平（最好2%，最差0.07%），每天只需要挑选其中最好的进行进一步优化和提交即可。


> [!NOTE] [图片 OCR 识别内容]
> Overall Sumary:
> Total alphas processed:
> 994
> Passed alphas
> Count:
> Pass rate:
> 1.073


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，之前有积累一些模板，确实没想到还可以动态淘汰模板

学到了！

===================================================================================


---

### 技术对话片段 38 (原帖: 【Alpha模板】模板群管理——动态优化淘汰低效模板)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha模板】模板群管理动态优化淘汰低效模板_37285699644823.md
- **时间**: 5个月前

**提问/主帖背景 (SY43349)**:
## 引言

大家好我是sy。最近社区一直在缩减回测量想必大家可能会遇到很多困难。我是11月中旬成为条件顾问，到目前刚好一个半月了，这期间我总共提交了122个alpha，点了27个塔，平均每日回测大概2500左右，目前大概每天能稳定提交2-4个alpha（中间断交主要是临时有事。。）  我想跟大家分享一下目前我在实现低回测高产出方面的核心经验——动态管理模板群。  不过需要注意⚠️的是，由于代码和我自身的框架非常绑定无法单独抽离，以下内容主要以思路为主，希望能对大家有所帮助。


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> Z0O
> Oou
> so
> Oe
> 2 ^.
> @ ^8 ?D (
> S 3
> NO
> Nov
> NOV
> Noy
> Nov
> NOV
> NOv
> Noy
> NOV
> Nov
> NO
> ND
> Oec
> Dec
> Dec
> Dec
> Dec
> Oec
> Oec
> Dec
> Dec
> Dec
> 28。



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> so'so'soosososo'
> Oec
> Oec
> 2 ^
> ' 3
> Dec
> Dec
> Qec


## 模板群管理

想必大家手里都有很多模板，但是实际上不知道大家有没有进行过统计，不同模板的产出效率完全不同，甚至相差数百倍，长期在低效模板上的回测是没有意义的。因此，我想到了能不能多各个模板的产出结果进行统计，实现对低效模板的发现和剔除，从而提升这个模板群的效率。

### 抽象模板生成方法

#### alpha funcs 库

要实现动态的模板库管理需要对模板库进行一层抽象，它接受给定的模板库

```
ALPHA_FUNCS = [   "func1", "func2"]
```

#### 动态alpha 生成

随后generator根据给定的alpha funs生成所有的对应的alpha

```
    def generate_random_alphas(self, count):        """        🎲 使用多种策略生成指定数量的随机 Alpha。        使用多种生成器（fundamental, technical, sentiment 等），并按权重抽样。        """        print(f"\n🎲 正在生成 {count} 个随机 Alpha...")        # 所有可用的 Alpha 生成函数列表（涵盖基本面、技术面、情绪面、随机结构等）        all_alphas = []        alpha_funcs = []        generators = get_func_call_info().keys()        # 从每个生成器中随机抽取部分结果        for gen in tqdm(generators):            try:                gen = eval(f'{gen}')                result = gen()                result = list(set(result))                if result and len(result) > 0:                    # 每个生成器抽取 1 ~ min(建议数量, 实际数量) 个                    sample_size = min(count // len(generators) + 5, len(result))                    sample_size = max(1, sample_size)                    selected = ALPHA_SELECTOR.rng.sample(result, sample_size)                    tmp_selected = []                    # 去重                    for s in selected:                        if s not in all_alphas:                            tmp_selected.append(s)                                        all_alphas.append(tmp_selected)                    alpha_funcs.append([gen.__name__] * len(tmp_selected))            except Exception as e:                print(f"⚠️ 生成器 {gen.__name__} 出错: {e}")                continue        all_alphas = [alpha for sublist in all_alphas for alpha in sublist]        alpha_funcs = [func for sublist in alpha_funcs for func in sublist]        print(f"✅ 成功生成 {len(final_alphas)} 个随机 Alpha！")        return final_alphas, final_funcs
```

#### 模板标记

要做到跟踪统计首先是，做到准确的来源标记。这里我采用dataclass的方式在生成时就标记了alpha的来源。

```
@dataclassclass AlphaRecord:    """Data class for storing alpha information, extends evaluation result"""    expression: str    alpha_func: str    alpha_link: str = None    sharpe: float = None    subsharpe: float = None    fitness: float = None    turnover: float = None
```

#### 统计分析

通过上述步骤我们就可以追踪每个alpha 模板的表现，随后可以自己制定规则动态淘汰一些模板。我自己采用的是通过率淘汰的方式。以下是效果展示：


> [!NOTE] [图片 OCR 识别内容]
> ntig
> alpha_lunc_Call_intolson
> Jha"
> passed
> Count"
> 215,
> total_Count"
> 10566
> passed_ratio"
> 02034828695816771}
> late
> passed_count"
> 91,
> total_Count
> 5699
> passed_ratio"
> 015967713633970874}
> 033400
> Count
> 工70,
> LULOL
> Count"
> 15477,
> passed_ratio"
> 0.011371712864250177}
> alpha"
> passed_count"
> 31
> total_count
> 2790,
> passed_ratio"
> 011111111111111112};
> OnC
> JVU COCC
> UGLTCU
> COUIC
> g2;
> total_count"
> 10147
> passed_ratio"
> 00906671922735784},
> passed_count"
> 115,
> total_count"
> 18963
> passed_ratio"
> 0060644412803881245}
> Dassed_count"
> total_count"
> 9813,
> passed_ratio"
> 0007133394476714562}
> Dassed_Count"
> total
> Count"
> Dassed_ratio"
> 0邝


目前经过我对模板群的不断优化，现在每日平均可提交alpha已经可以做到1%的水平（最好2%，最差0.07%），每天只需要挑选其中最好的进行进一步优化和提交即可。


> [!NOTE] [图片 OCR 识别内容]
> Overall Sumary:
> Total alphas processed:
> 994
> Passed alphas
> Count:
> Pass rate:
> 1.073


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，之前有积累一些模板，确实没想到还可以动态淘汰模板

学到了！

===================================================================================


---

### 技术对话片段 39 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】AI搜索字段极性配对构建低PC因子附提示词经验分享_39845230299927.md
- **时间**: 2个月前

**提问/主帖背景 (MY82844)**:
延续之前在 [Sentiment塔]([Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md) 里通过字段极性配对(polarity pairs)构造差异化RA的思路，在AI帮助下，我们发现类似的想法可以推广到更到数据集，构造一些低PC的因子，缓解SLOW_AND_FAST theme时期的断粮危机。

第一步，使用提示词，调用大模型的看家本领，让大模型寻找给定数据集里面的极性配对：

SYSTEM_POLARITY = """You are a quantitative data curator for WorldQuant BRAIN-style datafields.

Task: find **semantic polarity pairs** within the SAME dataset chunk — two fields that describe the **same underlying concept** but **opposite valence** (e.g. positive vs negative sentiment, bullish vs bearish, increase vs decrease counts, upgrade vs downgrade, up vs down in the same metric family).

Rules:

- Use BOTH **field id** and **description**.

- **field_id_more_positive**: the field whose values represent the more **positive / favorable / bullish / upward** direction for that paired concept.

- **field_id_more_negative**: the more **negative / unfavorable / bearish / downward** direction.

- If you are not sure, do NOT invent pairs.

- **Every id MUST be copied exactly** from the provided table (same spelling).

- Output **ONLY** a JSON array (no markdown, no commentary). Schema:

[{"field_id_more_positive":"...","field_id_more_negative":"...","pair_label":"short EN label","confidence":0.0,"reason_zh":"一句中文理由"}]

If no pairs: [].

"""

大模型在这种任务上准确率普遍较高，比如在IND，可以得到如下的结果：


> [!NOTE] [图片 OCR 识别内容]
> dataset_id
> Dair_
> inde
> field_id_Jore_Dositive
> field_id_Jore_
> negatixe
> Dair_Iabel
> confiderce
> Lea3oll_ZhI
> JIa133t4
> hiahest
> eetiate
> 1owe3t
> 331e3_eetijate
> SaLe3
> 〈allllal〉
> eetiate
> bolarity
> 销售额年度最高与最低估计
> 表示相反销售预期
> JIa133t4
> OB 331e3
> estijate_JazinlJ_
> Cllarterl3
> estinate_JiriJlJ_
> clarterl3
> 3a1e3
> 〈quarterl
> estijate Dolarity
> 销售额季度最
> 与最低估计
> 体现相反营恢趋势
> JIa133t4
> 0? shareholder3 _
> estijate_JaxinU_Gf
> shareholder3_
> ecllity_
> estijate_JiriJll_rf
> Shareholder?
> eetiate
> bolarity
> 股东极益的
> 低估计
> 伐表相反资本结构预期
> JIa133t44
> pretaxprofi
> eetiates
> Hre
> taxprofi
> estijates_
> dowrri_
> Pretay profi
> eetiate
> LeTi31o11
> Colllzt
> 和向
> 修订数量
> 问上修订积极 =
> 向下修订消报
> JIa133t44
> 116 Ioe
> I11II
> estijates_
> 1I
> Loe
> IlJL_ estijates_
> dowrri_
> R讵
> eetiate
> LeT1310I1
> Colllzt
> 估计4周
> 和向
> '修订数量,问上修订积极
> 向下修订消极。
> JIa133t44
> 11? &ales_upwlrard_revisiors _
> 341e3
> dowrrzwrard
> LeTi310113_
> 3a1e3
> estijate rerisiorl
> Colllzt
> 销售额估计4周内向上和向下修订数量
> 问上修订积极 _
> 向下修订消报
> JIa133t-
> 118 all G
> bdzd
> opt_iplied
> 工aI8e
> aIL $
> bdrd_opt_implied_rarge
> Optioris
> Implied Rarge
> 期杈隐
> 范围的高值和低值
> 高值表示乐观预期,低值表示悲观预期
> 531
> egUI
> egUI
> Hieh


第二步，我们可以通过简单的运算导出一些新的变量：

```
diff = fld_pos - fld_neglog_diff = log(fld_pos) - log(fld_neg)ratio = fld_pos / (fld_pos + fld_neg)
```

然后，从这些新的变量出发，通过一二阶的单变量算子，可以构造一些差异化的ATOM类型的alpha。因为相对的使用配对的顾问还比较少，在各大region还是可以出一些PC比较低的因子。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> A Sirgle Data Set Alpha
> Regular Alpha
> Pyramid -heme; INDIDIIANALYST <1.5
> Aggregate Data
> SharCe
> LUrnOer
> FIMESs
> TCUTR
> UF3UoIn
> MarEin
> 2.70
> 9.55%
> 2.80
> 13.4596
> 5.549
> 28.189000


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享模板思路！学到了很多

这就去试试看！

=============================================================================


---

### 技术对话片段 40 (原帖: 【Alpha灵感】全球第一个MEA因子（零PC alpha），我是怎么做出来的？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】全球第一个MEA因子零PC alpha我是怎么做出来的_40134245568663.md
- **时间**: 1个月前

**提问/主帖背景 (JL76306)**:
半夜做因子的时候发现新开了一个MEA地区，考虑到低PC高奖赏原则于是开始了因子设计。


> [!NOTE] [图片 OCR 识别内容]
> Prod
> Correlation
> ee >
> 0.00
 
（先上镇楼 PC0.00 图）

### PART1：了解现有情况计划对策

MEA开始的时候，我发现在data集合里面搜索为空，应该是接口也未开没办法直接用程序批量回测。

那下一个，就是得测试一下这个地区是不是可以开始制作？
于是，我用了最简单的adv20，发现不存在，但是！data输入时下拉展示列表存在可用data展示。进行回测，进度条可以到35%说明该地区真实打开！


> [!NOTE] [图片 OCR 识别内容]
> Settings
> MEA/DI/TOP300
> Comy
> Streak: 340day
> adv
> aVB_daily_dollar_volume_Zod
> avg_daily_dollar_volume_2Od
> 0 avg_daily_dollar_volume_God
> daily_dollar_volume_ten_day
> Type: Matrx Price Volume
> aVB_daily_Volume_I2Od
> aVB_daily_volume_2Od
> The average dailytrading Value in USD over the
> aVg_daily_volume_25Od
> past 20 days for securities inthe 'MEA_Uber
> daily_Volume_4Od
> universe.It is calculated as the Z0-day average
> aVB_daily_Volume_Sd
> Volume multiplied by
> reference price。
> aVB_daily_Volume_GOd
> 3 aVB_daily_volume_fifty_day
> average_daily_volume_GOd
> average_daily_Volume_63_days
> a+
> a+


OK，总结现有情况：MEA地区可做、MEA data仅可通过熟悉字段输入在下拉中选择。

结合现有情况，那么或许应该去做模板因子，特别是， **有特定data选择** 、 **有经济学含义的因子模板** ！
（ps：还有另一个好处，开点新地区确实冒险所以有经济学含义的话会稳一点）

### PART2:站在前人的肩膀上前进！

由于我不是经济学出身也想不起来啥关键字，于是，我去问ai有哪些经济学关键字眼合适做底层data来做因子。拿到一批关键词后，我开始去论坛进行搜索相关文章（因子模板）。

发现了，金矿！

【Alpha模板】标准化盈利意外-SUE因子2：升级篇--全市场！！横向无痛点塔 Anl、Fnd（附模板） [[Commented] 【Alpha模板】标准化盈利意外-SUE因子2升级篇--全市场横向无痛点塔 AnlFnd附模板Alpha Template_35837735141015.md]([Commented] 【Alpha模板】标准化盈利意外-SUE因子2升级篇--全市场横向无痛点塔 AnlFnd附模板Alpha Template_35837735141015.md)

JY35107大佬曾提供一个构建的基于eps data的SUE因子，看起来非常有具体含义，，且大家点赞颇高，大佬研究真的很精深，再次感谢大佬，大家也请多为他点赞！！！

于是我开始了测试，按照模板填写，选了一个综合性最强的eps data填入，，，
成功就这样出现了，，，，


> [!NOTE] [图片 OCR 识别内容]
> 屉 Correlation
> Self Correlation
> Haximum
> IITMUM
> Last Run: Fr, 05/91/2026,12-50 J
> Power Pool Correlation
> Haximum
> IITMUM
> Last Run: Fr, 05/91/2026,12-49 J
> Prod Correlation
> IT
> NIimUM
> Last Run: Fr; 05/01/2026,12.20-
> ThE  3re nC
> proo-Correlated alphzs。
> IS Testing Status
> 8P4SS
> Sharpe of 2.17is above CUtoff of
> FitnEss Of 2.33
> EbVE CUOff 3
> TurnoVerof 2.709
> 3bOVe Cutoffcf 1%
> TurOEFOf 27036
> beow CUtOffof 7096_
> Ieightis WeI
> listribued C ins-rmEnts
> SUb-Uie SE Sharpe Of 2.1415 EbJVE ~UTOff J 1.33
> 2jearSharpe cf 1.89
> aDOVE ~UOff Of 1.58
> Pyramid theme MENDIIPV marches With multiplier af 2.Effective Pyramid count for Genius
> NARNING
> PENDING


传说中的前无古人因子，，，


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_decay_linear(ts
> av_diff
> 120)/ts_std_dei
> 25211252)
> 酡 Single Data Ser Alpha
> m Power Pool Alpna
> 酡 Regular Alpha
> Pyramid teme- MENDTIPV X
> ABgregate Data
> Thz
> TICCC
> Fitne
> ReTrlTn
> Ur
> Marein
> Simulation Settings
> 2.17
> 2.70%
> 2.33
> 14.36%
> 9.26%
> 106.3
> 9000
> Instrument Type
> Region
> Unwerse
> Langwage
> Decay
> Delay
> Truncation
> N-utralization
> Pasteurizalion
> Loohback
> MaxTrade
> Max Positon
> EquIt
> WEA
> TCF3JO
> Fast Excression
> 0.35
> Wrkst
> Vear
> Shampe
> Tumower
> Ftness
> Returs
> Drawdown
> Margin
> Long Cownt
> Short Count
> 2014
> Z.15
> 一239
> 2.73
> Ss
> 3.2535
> 93.225:
> 2015
> 59:
> 0.57
> 4.53汩
> 一33
> 33.31t:
> 143
> ?06
> 1.32
> 2.619
> 8.21汩
> 1.33
> 67.525
> Clone Alpha
> 2017
> 2.34
> 539
> 15.345
> 7.3235
> 149.725:
> 140
> 201
> 一-
> 15.3E
> 一0235
> 130.555:
> N Chart
> PIL
> 2015
> 2.52
> 2379
> 2.5
> 13.15汩
> 2.913
> 111.485:
> 143
> 2020
> 539
> S.FE污
> 一73
> 75.375:
> 13
> 202
> 4.31
> 2439
> Ee
> 25.73汩
> 3.66%
> 233.355.
> 2022
> T
> 539
> 2.3
> 13.5汩
> 2.193
> 104.735:
> 142
> TON
> 2023
> 559:
> 8.12汩
> 3.613
> 63.31汩:
> 143
> 07122'2019
> PnL 7,327.42k
> OOJK
> Investability constrained
> Aggregate Data
> Sharp
> TUFnO
> iTe
> RaITns
> T
> Wsrain
> 1.83
> 2.53%
> 1.83
> 12.46%
> 9.1
> 98.729000
> Jul"14
> Jul"15
> J1"16
> J1"17
> J41'13
> Jul'19
> J41'20
> JUI'21
> J1'22
> JUl'23
> 医 Correlation
> Self Correlatlon
> TsmUT
> Mpimum
> ICTFI
> PoWeF Pool Correlation
> TsmUT
> Mpimum
> ICTFI
> IS Testing Status
> Period
> Prod Correlation
> IHMUIT
> TNIMUM
> Last Run; Fr, 05/01/2026,12-53 A
> 8 PASS


点击，提交。

看到PC 0的那一刻，我知道，我成了。

以上思路，希望可以帮助到大家！

也再次感谢JY大佬！感谢社区的开源精神！期待大家也能挖到低相关性的好因子！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

恭喜大佬  这下真成第一个吃螃蟹的人了

好奇prod corr 0的话base pay能给多少

=============================================================================


---

### 技术对话片段 41 (原帖: 【Combined Alpha Performance】踩坑分享，纯新手comb  -2+经验分享)
- **原帖链接**: [Commented] 【Combined Alpha Performance】踩坑分享纯新手comb  -2经验分享.md
- **时间**: 24天前

**提问/主帖背景 (XW83124)**:
1月9号开始成为顾问，4月份第一次更新comb,所有alpha的comb是-2+,因为当时提交数量少

且不知道很多隐性的提交标准,所以想着等下一次再更新的时候,应该不至于负这么多了,可是

等5月9号更新的时候还是-2+,这个时候就开始重视找问题了.可以看到我从1月份到3月份总

共提交了66个。那么问题出现在哪呢，接下来继续看。 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page sIZe
> SUbIISSIOI Date:
> 01/11/2026-03/31』 ..
> HIlter
> belect Columns
> Name
> Competition
> Type
> Status
> Language
> Date Submitted
> Failed
> Failed
> Osmosis
> Region
> Universe
> Sharpe
> Retums
> Tumover
> Tag
> (ESTI
> PPA
> Points
> Search
> Selec
> See
> 01/11/2025
> 03/31
> 32 >
> 32 
> 32 
> Select
> Selec
> 32 
> 32 
> 巳 吕>
> Selec
> SCICt
> SEICCt


现在看一下我找出问题的部分alpha


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> ThEME: IND/DI Power PoolJan ` 26*1
> 昵
> Dazs Set JIpha
> X Power Pool Alpha
> 7 Regular Alpha
> Fyramid thene: INDIDTIPV X1.2
> Aggregate Data
> SrCe
> LUFnOVE
> FIIeS
> ReTUTns
> UTUTTMn
> Warsin
> 2.26
> 23.92%
> 1.53
> 10.91%
> 6.84%
> 9.129600
> Vear
> Sharpe
> Turover
> Ftness
> Returs
> Drawdown
> Lon Cownt
> Shrt Count
> 2013
> 2.13
> 23359
> 10.705
> 3.0595
> 8.539
> 2014
> 23.379
> _
> -2.324
> 9一4
> 4S9
> 2015
> 0.3
> 33.939
> 35;
> 5.333
> 1ERO
> 20E
> Z.5E
> 2.379
> 12.155
> 2.333
> 1.1;
> 213
> 2017
> 2.09
> 23.759
> 1.2
> &.54沾
> 9155
> .15
> 216
> 2018
> 2.679
> 4.33
> 20.51汩
> 3.1-5
>  710
> 2015
> 3.3
> 2579
> Z.75
> 15.575
> 4119
> 1254;
> 216
> 2020
> 4.7
> 33.339
> 4.3
> 26.05沿
> 633
> 21.3
> 213
> 2021
> 2.379
> 9治
> 3.4295
> 1_
> 210
> 202
> 1.7
> 2.619
> 3汩
> 0.333
> 48EIo
> 217
> 2022
> 4
> 33.929
> 2.30
> 15.37汩
> 1919
> T41C9
> 217
> 品^
> 2023
> -3.3
> 13.139
> -2.-5
> 10.3汩
> .633
> 1+1
> 202
> 2023
> 07
> 23239
> 0.14
> 94沾
> 2.8595
> 1.
> 214
> Single
> Margin
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> U ReBuIar Alpha
> Pyramid heme: INDIDIIPV<1.2
> Pyramid theme: INDIDIISENTIMENT 〈1.
> Aggregate Data
> SrCe
> UTIONET
> Fitness
> ReTUTns
> UTUTTMn
> IaTaIn
> 2.26
> 35.49%
> 1.25
> 10.80%
> 4.99%
> 5.0
> 900
> Vear
> Sharpe
> Tumover
> Ftness
> Relrs
> Drawdown
> Long Count
> Shrt Count
> 2013
> 2.37
> 34235
> 11.E79
> 1539
> 5.319
> 014
> 3455::
> 0.32
> 3.339
> -439
> 4.79
> 2015
> 3431
> 13.339
> .039:
> S
> 2-0
> ZOIE
> 306
> 8.279
> 539:
> 二
> 20i
> 35515
> 379
> 3
> 2.119
> 4
> ?0?
> 34
> 3
> 7.35
> 529
> 2.139:
> TTT
> 2015
> 331
> JE:
> 1539
> 5
> 23
> 2020
> S 42
> D.TE
> 30
> 1.239:
> S
> 2021
> DE?
> SE115
> 313
> 3.59
> 7
> 2022
> 4=
> 21.359:
> DEJN:
> 3ER
> 2022
> SE
> S三 
> 5.30
> 23E79
> E
> 1.74
> 23
> 2023
> 37.333
> 0.53
> 1439
> 3.239:
> 3
> 品
> 2023
> 0.03
> .415
> 0.31
> 0.229
> 2.539
> L_
> Wrgin
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> e Power Poo Alpha
> 7 Regular Alpha
> Pyramid -hEME: IND/DIIRISK 
> Fyramid theme: INDIDIIOTHER KI
> Aggregate Data
> Sharpe
> TUFnOIP
> Trnssc
> TPTUCT
> Cra'dn
> 2.48
> 18.34%
> 2.17
> 4.03%
> 8.1796
> 15.309600
> Vear
> Shrpe
> Tumover
> Ftness
> Retrs
> Drawdown
> Nargin
> Long Cownt
> Short Count
> 2014
> 1443
> 5.50
> 2.739
> Sg:
> 31.SCR02
> 222
> 234
> 2015
> 1732
> 31
> 539
> S
> 25
> ZOIs
> 1.12
> 539
> 039
> 11.12
> 203
> 2017
> 17.E
> 1.J5
> 721
> 339
> 379
> 332
> 201
> 15.27
> 4.Js
> 21.579:
> 2529
> 22.8CRO?
> 213
> 2019
> 20.45:
> 0.5S
> 7.239
> 5.339
> 7.1492
> 2020
> 1.33
> 18.09
> 5.32
> 3E39
> 3.479
> 3.12
> 235
> 2021
> 0.52
> 17.14
> 0.52
> 439
> 8.179
> TA
> 314
> 2022
> 20.11
> 12.739
> 2.519
> 12.579
> 219
> 234
> 2023
> 71
> 20.71
> 2.13
> 12819:
> 579
> 12.3793
> 21-
> 232
> aralc


**这些alpha都有共同的特点,ind地区,高换手,低margin,像这样的alpha,我一共交了8个,后期**

**在组sa的时候也没有意识到这个问题,组了有6个有问题的sa,也就是我在基数66个的情况下,**

**有14个是有问题的,按照论坛里面的计算方法,一个坏的alpha需要3-4个alpha才能补正,那么**

**我这comb不为负才奇怪呢。**

**总结来说：第一、提交的时候一定要注意margin值。第二、在已知有问题的alpha的时候为**

**了避免组sa的时候选到问题alpha,可以把有问题的alpha标注颜色,并且进行隐藏,这样组sa**

**的时候,就会筛选不到了。**

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享  提交Alpha的过程中 Margin确实是一个不可忽视的指标

否则就会被Combine教做人了

=============================================================================


---

### 技术对话片段 42 (原帖: 【Combined Alpha Performance】踩坑分享，纯新手comb  -2+经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Combined Alpha Performance】踩坑分享纯新手comb  -2经验分享_40533711115927.md
- **时间**: 24天前

**提问/主帖背景 (XW83124)**:
1月9号开始成为顾问，4月份第一次更新comb,所有alpha的comb是-2+,因为当时提交数量少

且不知道很多隐性的提交标准,所以想着等下一次再更新的时候,应该不至于负这么多了,可是

等5月9号更新的时候还是-2+,这个时候就开始重视找问题了.可以看到我从1月份到3月份总

共提交了66个。那么问题出现在哪呢，接下来继续看。 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page sIZe
> SUbIISSIOI Date:
> 01/11/2026-03/31』 ..
> HIlter
> belect Columns
> Name
> Competition
> Type
> Status
> Language
> Date Submitted
> Failed
> Failed
> Osmosis
> Region
> Universe
> Sharpe
> Retums
> Tumover
> Tag
> (ESTI
> PPA
> Points
> Search
> Selec
> See
> 01/11/2025
> 03/31
> 32 >
> 32 
> 32 
> Select
> Selec
> 32 
> 32 
> 巳 吕>
> Selec
> SCICt
> SEICCt


现在看一下我找出问题的部分alpha


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> ThEME: IND/DI Power PoolJan ` 26*1
> 昵
> Dazs Set JIpha
> X Power Pool Alpha
> 7 Regular Alpha
> Fyramid thene: INDIDTIPV X1.2
> Aggregate Data
> SrCe
> LUFnOVE
> FIIeS
> ReTUTns
> UTUTTMn
> Warsin
> 2.26
> 23.92%
> 1.53
> 10.91%
> 6.84%
> 9.129600
> Vear
> Sharpe
> Turover
> Ftness
> Returs
> Drawdown
> Lon Cownt
> Shrt Count
> 2013
> 2.13
> 23359
> 10.705
> 3.0595
> 8.539
> 2014
> 23.379
> _
> -2.324
> 9一4
> 4S9
> 2015
> 0.3
> 33.939
> 35;
> 5.333
> 1ERO
> 20E
> Z.5E
> 2.379
> 12.155
> 2.333
> 1.1;
> 213
> 2017
> 2.09
> 23.759
> 1.2
> &.54沾
> 9155
> .15
> 216
> 2018
> 2.679
> 4.33
> 20.51汩
> 3.1-5
>  710
> 2015
> 3.3
> 2579
> Z.75
> 15.575
> 4119
> 1254;
> 216
> 2020
> 4.7
> 33.339
> 4.3
> 26.05沿
> 633
> 21.3
> 213
> 2021
> 2.379
> 9治
> 3.4295
> 1_
> 210
> 202
> 1.7
> 2.619
> 3汩
> 0.333
> 48EIo
> 217
> 2022
> 4
> 33.929
> 2.30
> 15.37汩
> 1919
> T41C9
> 217
> 品^
> 2023
> -3.3
> 13.139
> -2.-5
> 10.3汩
> .633
> 1+1
> 202
> 2023
> 07
> 23239
> 0.14
> 94沾
> 2.8595
> 1.
> 214
> Single
> Margin
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> U ReBuIar Alpha
> Pyramid heme: INDIDIIPV<1.2
> Pyramid theme: INDIDIISENTIMENT 〈1.
> Aggregate Data
> SrCe
> UTIONET
> Fitness
> ReTUTns
> UTUTTMn
> IaTaIn
> 2.26
> 35.49%
> 1.25
> 10.80%
> 4.99%
> 5.0
> 900
> Vear
> Sharpe
> Tumover
> Ftness
> Relrs
> Drawdown
> Long Count
> Shrt Count
> 2013
> 2.37
> 34235
> 11.E79
> 1539
> 5.319
> 014
> 3455::
> 0.32
> 3.339
> -439
> 4.79
> 2015
> 3431
> 13.339
> .039:
> S
> 2-0
> ZOIE
> 306
> 8.279
> 539:
> 二
> 20i
> 35515
> 379
> 3
> 2.119
> 4
> ?0?
> 34
> 3
> 7.35
> 529
> 2.139:
> TTT
> 2015
> 331
> JE:
> 1539
> 5
> 23
> 2020
> S 42
> D.TE
> 30
> 1.239:
> S
> 2021
> DE?
> SE115
> 313
> 3.59
> 7
> 2022
> 4=
> 21.359:
> DEJN:
> 3ER
> 2022
> SE
> S三 
> 5.30
> 23E79
> E
> 1.74
> 23
> 2023
> 37.333
> 0.53
> 1439
> 3.239:
> 3
> 品
> 2023
> 0.03
> .415
> 0.31
> 0.229
> 2.539
> L_
> Wrgin
  
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> e Power Poo Alpha
> 7 Regular Alpha
> Pyramid -hEME: IND/DIIRISK 
> Fyramid theme: INDIDIIOTHER KI
> Aggregate Data
> Sharpe
> TUFnOIP
> Trnssc
> TPTUCT
> Cra'dn
> 2.48
> 18.34%
> 2.17
> 4.03%
> 8.1796
> 15.309600
> Vear
> Shrpe
> Tumover
> Ftness
> Retrs
> Drawdown
> Nargin
> Long Cownt
> Short Count
> 2014
> 1443
> 5.50
> 2.739
> Sg:
> 31.SCR02
> 222
> 234
> 2015
> 1732
> 31
> 539
> S
> 25
> ZOIs
> 1.12
> 539
> 039
> 11.12
> 203
> 2017
> 17.E
> 1.J5
> 721
> 339
> 379
> 332
> 201
> 15.27
> 4.Js
> 21.579:
> 2529
> 22.8CRO?
> 213
> 2019
> 20.45:
> 0.5S
> 7.239
> 5.339
> 7.1492
> 2020
> 1.33
> 18.09
> 5.32
> 3E39
> 3.479
> 3.12
> 235
> 2021
> 0.52
> 17.14
> 0.52
> 439
> 8.179
> TA
> 314
> 2022
> 20.11
> 12.739
> 2.519
> 12.579
> 219
> 234
> 2023
> 71
> 20.71
> 2.13
> 12819:
> 579
> 12.3793
> 21-
> 232
> aralc


**这些alpha都有共同的特点,ind地区,高换手,低margin,像这样的alpha,我一共交了8个,后期**

**在组sa的时候也没有意识到这个问题,组了有6个有问题的sa,也就是我在基数66个的情况下,**

**有14个是有问题的,按照论坛里面的计算方法,一个坏的alpha需要3-4个alpha才能补正,那么**

**我这comb不为负才奇怪呢。**

**总结来说：第一、提交的时候一定要注意margin值。第二、在已知有问题的alpha的时候为**

**了避免组sa的时候选到问题alpha,可以把有问题的alpha标注颜色,并且进行隐藏,这样组sa**

**的时候,就会筛选不到了。**

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享  提交Alpha的过程中 Margin确实是一个不可忽视的指标

否则就会被Combine教做人了

=============================================================================


---

### 技术对话片段 43 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md
- **时间**: 6个月前

**提问/主帖背景 (MY82844)**:
在EUR点塔Sentiment的时候，我们尝试把 [顾问 顾问 RM49262 (Rank 30) (Rank 30)](/hc/en-us/profiles/32668684211991-顾问 顾问 RM49262 (Rank 30) (Rank 30)) 的 [强大模版](【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template_35294898626711.md) 交给AI学习，最后AI推荐了一个新的条件动量模版，使用下来发现可以提炼一个通用模版，适用多种情形。

**因子模版：**

```
ts_mean(if_else(<condition>, returns, 0), <days>)
```

这边condition可以是某种事件，或者正负数/正负力的对比关系。当然，如果condition取1，days取252，我们就回到最简单的动量情形。

**因子逻辑：**

截取某种“有效“时间区间内的股票回报做度量，未来的表现会惯性持续一段时间。

在EUR的Sentiment的情形，我们尝试了下面的组合方式，得到一些低pc的结果：


> [!NOTE] [图片 OCR 识别内容]
> ts_mean (if_else
> Snt21_ZPO5
> mean
> snt2l
> 2neg_mean,
> peturns
> 0)
> Simulation Settings
> Instrument Type
> Region
> Unierse
> LangUaqe
> Decay
> Delay
> Tmuncation
> Neutraliatijon
> Pasteurization
> NaN Handling
> Unit Handling
> MaxTrade
> Equi
> EUR
> TOPZSOO
> Fast ExPression
> 0.01
> FES- FaC-Ors
> Verify
> Clone Alpha
> Chart
> Pnl
> OOOK
> OOOK
> Jul'13
> Jul1
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
> Jul17
> Jan '18
> Jul'18
> Jan '19
> Jul19
> Jan 20
> Jul'20
> Jan 21
> Jul 21
> Jan'22
> Jul'22
> Jan '23
> Jan _


**后续：**

1. 可以再配合一些group_op()的操作，进一步提升alpha的表现

2. ts_mean和ts_sum可以比较进行，表现有时候会有些差异（包括NaN的不同处理）

3. condition可以多种多样，比如analyst的up/down的力对比，call/put的力对比，有待进一步挖掘

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，又学到了新模板

===================================================================================


---

### 技术对话片段 44 (原帖: 【Eligibility Criteria篇】一文告诉你如何GOLD直通Grandmaster！（上篇）置顶的论坛精选)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXvZk%2FTyQ6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAd5odHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzk5MjI3ODgwNTYzNDMtLUVsaWdpYmlsaXR5LUNyaXRlcmlhJUU3JUFGJTg3LSVFNCVCOCU4MCVFNiU5NiU4NyVFNSU5MSU4QSVFOCVBRiU4OSVFNCVCRCVBMCVFNSVBNiU4MiVFNCVCRCU5NUdPTEQlRTclOUIlQjQlRTklODAlOUFHcmFuZG1hc3Rlci0lRTQlQjglOEElRTclQUYlODcGOwhUOg5zZWFyY2hfaWRJIik4YTgxOTJhMi0zZGY4LTQ2MjAtOGY1Yi1kMjg1ODQxOGMyOTIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxSTTQ5MjYyBjsIVDoScmVzdWx0c19jb3VudGkU--887a5072b8c56b14f6662b0e6c5f35360d569886
- **时间**: 1个月前

**提问/主帖背景 (LX57490)**:
一、引言大家好，我是来自兰州的一位大学生顾问，在AI发展迅速的现在，我没有学会我专业应该熟悉的算法，而是全权使用AI从0到1进行各种新事物的学习。从国际经济与贸易专业转到计算机科学与技术，赶上AI大爆发，从刚转过去就开始用AI，导致我虽然对代码一无所知，也能和AI对话制作出我想要的代码，当时还是半人工的方法，询问完，复制过来，我最开始的回测系统和AI模版以及自相关代码也是这样改出来的。而如今，AI已经可以自动化回测，自动写代码，真的只需要敲敲键盘，写下你的想法，就能实现你想要的结果，算是赶上了一波时代的红利，让我借此通过AI拿到了GrandMaster！Gold直通GrandMaster的难度看似变高，实则变低了，为什么呢？听我细细说来：1.  PPA虽然大削，但是大家使用的操作符数量都会上升，正常做RA被操作符影响的概率更低了，还能督促大家提高PPA质量到RA，从而保证combine！2.  回测大削，大家不能无脑代码堆量低opPPA，此时奔着RA制作将是一个不错的选择，RA毕竟0.7以下就行，PPA还得保证0.5以下，或者用sharpe压过去，还是比较麻烦的。3.  人数少，相较于M，GM的竞争力不高，虽然限制了75人，不过上赛季最终达标也就83/75人，只要能稳住combine，达到标准，基本上没什么太大问题！高筑墙！广积粮！缓称王！二、Eligibility Criteria（一）Signals我们这里使用LH44620大佬开源的代码进行分析！本季度共计317个alpha，其中Regular Alpha:252个，Super Alpha：65个 。1.  主要制作USA，IND，EUR的SA，IND拉一下我的margin，USA,EUR正常稳固地区且好做。2.  IND的model和analyst比较多，是因为听到IND手续费比较高，选择提升质量，拉高margin，降低turnover，稳固一点。3.  EUR的model是当时为了吃2倍的加成，猛猛多高了点高质量，美美吃base。4.  其余地区数据集，亮就跑。（二）Pyramids Completed一月下旬觉得有机会冲级GM，开始猛攻点塔，刚刚好凑够60塔，被迫五地区QAQ。IND RA开路，为我奠定了冲塔的基础，给足了做RA的信心，我以RA为基础，PPA为辅助进行冲级之路。1.  IND USA EUR几乎百分之95的RA，几个PPA，绝大部分ATOM+RA。2.  GLB 绝大部分PPA，因为三地区sharpe，我只能尽力接近，不能什么数据集都RA，且margin达标。赶上GLB TOPDIV3000 PPA 直接用COUNTRY起手，高质量快速PPA点完GLB。3.  USA EUR GLB IND四地区GOLD点满也没有60塔，索性直接ASI RA，大地区总比小地区稳定，就是太难做了，下次我还是选小地区QWQ！4. 基于（2026-4-22）目前版本对于我开的五地区进行难度排序：ASI >>>> GLB > USA ≈ IND >  EUR（三）Combine这里我们使用顾问 JG15244 (Rank 67)为国区无私开源的网址[链接已屏蔽]进行分析！（一） Combined Alpha Performance1.  高质量RA，高质量PPA，高质量SA，死守各地区magin底线，其次越高越好。2.  补救差地区提交高质量SA，拉高fitness，sharpe，magrin，returns，降低drawdown！3.  margin建议：USA:  margin > 10 ( ILLIQUID_MINVOL1M > 15 )EUR:  margin > 10GLB:  margin > 15   (10+也可以)ASI:  margin > 15 (10 12 13也能忍受)IND:  margin > 15 (同时turnover低于15，我偏向于这个地区更降低一点，手续费偏高，需要更高margin，例如turnover 15  margin 15  我可能会把turnover降低到 12 10 9 8这样提交)其余小地区均 > 15（二） Combined Power Pool Alpha Performance当我通过删改PPA tag，将0.14变成2.49后，我便没有轻易动，然后OS出来了，我删了os差的，然后combine明显变差，所以已知的os在未来两年依然是未知数，改变更好的IS反而会过拟合，影响表现。其次，达标以后，我交一个PPA，删一个ppa tag，以保我的combine还能维持住！三、碎碎念回顾三赛季历程，感叹时间飞速，在这期间我学到了很多知识，认识到了很多人，来自五湖四海，各行各业，各个年龄段，宛如线上旅游，了解各地工作就业情况，体验各个地区的人文交流，颇感良多，感谢各位一路陪伴，终于实现了Gold直通GrandMaster的奇迹！（一） IQC赛季（2025-Q2）从零开始的量化之路，我从一个回测界面Simulate都需要单词查询意思的人，通过翻译以及挨个按钮点击学习，了解到了WQ平台的运作原理，开始使用machine_lib.py代码为基础的回测流程，同一开始的无脑一二三阶，二三阶叠加，变成了有精准选择的使用一二阶。1. 通过一阶代码，将ts_ops(ts_backfill(winsorize(单字段)))，选择改进零阶单字段，把单字段变成多字段组合形式，我提供给AI一个数据集里面的字段和描述，通过简单的四则运算给我一键制作零阶字段，省回测且有经济学意义的方法，例如新手教程的option8, call - put 双字段以后进行其他操作符叠加，得到alpha。2. 通过给二阶代码加入相关性剪枝，进行对一阶alpha的剪枝，减去大部分重复alpha，并且关于bukcet进行更多的想象力，详细内容可以从课代表（XX42289）的帖子进行学习，制作有经济学意义的特别bucket，这里面不只是bucket(rank)，不只是range ="0.1,1,0.1"，还可以更多的操作符，更多的字段，更多的参数范围，这使得我在IQC期间交了很多alpha。（二）初步了解赛季（2025-Q3）IQC顾问转正式顾问，跨度很大，IQC的长周期让人陷入在用户权限的温柔乡，在这里学习了很多知识，才进入顾问的状态。1. 了解RA,ATOM,PPA,SA四大类的区别和提交区别，以及IS指标的作用，sc，ppac，pc三者的区别与联系。2. 修改回测代码，将用户三并发改为8*10并发，解决4xx，5xx报错问题，使得代码更加稳健，除了亚马逊服务器崩了，一般不会再有问题了 : (3. 读论坛所有经验贴，避雷贴，结合回测出来的alpha进行IS数据的初步了解，知道什么alpha可以提交，什么alpha肯定不能提交，学习什么会影响VF和combine稳定，地区这么多可不可以多开，新手应该交什么样的alpha，以至于我这个赛季就交了31个alpha，实际VF combine也还行，没什么大事，combine稳定提升，VF最低0.64，起码大于0.5。（三）稳扎稳打赛季（2025-Q4）终于学的差不多了，开始尝试冲级，此时的我combine从0.79变成了1.52上下徘徊，说明质量没什么问题，开始往上走，这个时候我不交PPA，对PPA还不是很明白，顶多是RA+PPA+ATOM这种情况，顺带提交PPA，这也是日后的一个伏笔。1. PPA combine一直不咋好，0.14，删除了第一个不知道怎么提交的顾问PPA，更新一跃2.49，从此稳定2+，奠定了冲级的资格。2. 此时我并不知道六维带来的影响很大，还是用着用户的方法，bucket使用的操作符很多，densify我也没删，操作符平均数量飙升，加上刚转顾问断了一天回测，六维太可怜了，赛季末使用华子哥插件expert排行985，遗憾被刷，依然GOLD。3. 但是当时做出来的alpha，在日后的OS更新后，明显可以看出来，质量很好，不过操作符比较多，bucket的二阶是一个提升质量不可多得好方法！（四）奇迹出现赛季（2025-Q1）三赛季铺垫，终于厚积薄发！开头的我也是几天偶尔交一个，到了赛季更新后，各种新规则出来，我下定决心，直冲GM，二月初的时候我也不到7个塔，直接二月底到达35塔，四月冲级60塔，人不逼自己一把，不知道自己的上限有多高！1.  PPA大削，趁机通过RA进行点塔，我采用5op，2fileds方式进行RA制作，保证我的六维维持在这附近，下篇我会详细讲六维这方面。2.  返璞归真，AI+machine_lib，制作模版，遍历模版，保证4+1点塔，按照数据集进行分析，不同数据集制作不同模版，同数据集同预处理模版，二次切换不同一阶二阶，可得到无穷无尽的RA，只不过还需要看IS和近四年趋势，有些RA我并不会选择提交。3.  华子哥RAW数据横空出世！得到了全部数据，我开始精准选择我有的数据集，通过筛选我的要求，进行选择中性化和字段，精准打击alpha！既然他们能做出来，那我也能做出来的思想，做出来一个又一个小数据集的ATOM+RA！最后的最后，再次感谢各位朋友陪伴，使得我能够创造奇迹：感谢WQ平台，感谢国区各位老师，感谢研究小组二群的各位，感谢IQC的朋友们（以下排名，不分先后）：感谢weijie老师，kunqi老师，huangkai老师，顾问 KZ79256 (Rank 21) (华子哥)，XX42289 (课代表) ，worldquant brain赛博游戏王 (游戏王)，顾问 QX52484 (Rank 35) (司源老师)，顾问 FX25214 (Rank 22)，DA98440，JX39934，ZH41150，顾问 顾问 RM49262 (Rank 30) (Rank 30)，PP26750， LD27384，顾问 JG15244 (Rank 67)，LS17092，WT73952，XJ80376，QW94165，ZY20347，JZ45765，ll46807，JW52291等研究小组二群的各位朋友们！！！！最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！高筑墙！广积粮！缓称王！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================太强了尼克 Gold直升GM这篇经验贴也是干活满满，学到了很多！祝尼克一直GM下去！=============================================================================


---

### 技术对话片段 45 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Eligibility Criteria篇】一文告诉你如何GOLD直通Grandmaster上篇置顶的论坛精选_39922788056343.md
- **时间**: 2个月前

**提问/主帖背景 (LX57490)**:
### 一、引言

大家好，我是来自兰州的一位大学生顾问，在AI发展迅速的现在，我没有学会我专业应该熟悉的算法，而是全权使用AI从0到1进行各种新事物的学习。从国际经济与贸易专业转到计算机科学与技术，赶上AI大爆发，从刚转过去就开始用AI，导致我虽然对代码一无所知，也能和AI对话制作出我想要的代码，当时还是半人工的方法，询问完，复制过来，我最开始的回测系统和AI模版以及自相关代码也是这样改出来的。而如今，AI已经可以自动化回测，自动写代码，真的只需要敲敲键盘，写下你的想法，就能实现你想要的结果，算是赶上了一波时代的红利，让我借此通过AI拿到了GrandMaster！

Gold直通GrandMaster的难度看似变高，实则变低了，为什么呢？听我细细说来：

1.  PPA虽然大削，但是大家使用的操作符数量都会上升，正常做RA被操作符影响的概率更低了，还能督促大家提高PPA质量到RA，从而保证combine！

2.  回测大削，大家不能无脑代码堆量低opPPA，此时奔着RA制作将是一个不错的选择，RA毕竟0.7以下就行，PPA还得保证0.5以下，或者用sharpe压过去，还是比较麻烦的。

3.  人数少，相较于M，GM的竞争力不高，虽然限制了75人，不过上赛季最终达标也就83/75人，只要能稳住combine，达到标准，基本上没什么太大问题！

**高筑墙！广积粮！缓称王！**

### **二、Eligibility Criteria**

#### **（一）Signals**  
> [!NOTE] [图片 OCR 识别内容]
> Signals
> 252
> Reached Grandmaster
> 020


我们这里使用 [LH44620](/hc/zh-cn/profiles/26717918976919-LH44620)  大佬开源的代码进行分析！

本季度共计317个alpha，其中Regular Alpha:252个，Super Alpha：65个 。

1.  主要制作USA，IND，EUR的SA，IND拉一下我的margin，USA,EUR正常稳固地区且好做。

2.  IND的model和analyst比较多，是因为听到IND手续费比较高，选择提升质量，拉高margin，降低turnover，稳固一点。

3.  EUR的model是当时为了吃2倍的加成，猛猛多高了点高质量，美美吃base。

4.  其余地区数据集，亮就跑。


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> IND
> ANALYST
> EARNINGS
> FUNDAMENTAL
> IMBALANCE
> INSIDERS
> INSTITUTIONS
> MACRO
> MODEL
> NEWS
> OPTION
> OTHER
> PV
> RISK
> SENTIMENT
> SHORTINTERES
> SOCIALMEDIA
  
> [!NOTE] [图片 OCR 识别内容]
> SA
> 26


#### **（二）Pyramids Completed**  
> [!NOTE] [图片 OCR 识别内容]
> Pyramids Completed
> 60
> Reached Grandmaster
> 10


一月下旬觉得有机会冲级GM，开始猛攻点塔，刚刚好凑够60塔，被迫五地区QAQ。IND RA开路，为我奠定了冲塔的基础，给足了做RA的信心，我以RA为基础，PPA为辅助进行冲级之路。

1.  IND USA EUR几乎百分之95的RA，几个PPA，绝大部分ATOM+RA。

2.  GLB 绝大部分PPA，因为三地区sharpe，我只能尽力接近，不能什么数据集都RA，且margin达标。赶上GLB TOPDIV3000 PPA 直接用COUNTRY起手，高质量快速PPA点完GLB。

3.  USA EUR GLB IND四地区GOLD点满也没有60塔，索性直接ASI RA，大地区总比小地区稳定，就是太难做了，下次我还是选小地区QWQ！

4. 基于（2026-4-22）目前版本对于我开的五地区进行难度排序：

ASI >>>> GLB > USA ≈ IND >  EUR


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GlB
> EUR
> ASI
> CHN
> KOR
> TN
> HKG
> JPN
> AR
> I0
> Analys:
> Broker
> Earnines
> Fundamentar
> Imbalanze
> Insizlers
> Instittions
> MIaro
> Madel
> NEWs
> 03tion
> C-hEI
> Frice VlUME
> Risk
> SEntiMERT
> Shai In-eres-
> Social Media


#### **（三）Combine**  
> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 1.98
> 0.02 more to Grandmaster
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.28
> Reached Grandmaster
> 0C


这里我们使用 [顾问 JG15244 (Rank 67)](/hc/zh-cn/profiles/26966744854807-顾问 JG15244 (Rank 67))  为国区无私开源的网址 [[链接已屏蔽])  进行分析！

#### **（一） Combined Alpha Performance**

1.  高质量RA，高质量PPA，高质量SA，死守各地区magin底线，其次越高越好。

2.  补救差地区提交高质量SA，拉高fitness，sharpe，magrin，returns，降低drawdown！

3.  margin建议：

- USA:  margin > 10 ( ILLIQUID_MINVOL1M > 15 )
- EUR:  margin > 10
- GLB:  margin > 15   (10+也可以)
- ASI:  margin > 15 (10 12 13也能忍受)
- IND:  margin > 15 (同时turnover低于15，我偏向于这个地区更降低一点，手续费偏高，需要更高margin，例如turnover 15  margin 15  我可能会把turnover降低到 12 10 9 8这样提交)
- 其余小地区均 > 15

#### **（二） Combined Power Pool Alpha Performance**

当我通过删改PPA tag，将0.14变成2.49后，我便没有轻易动，然后OS出来了，我删了os差的，然后combine明显变差，所以已知的os在未来两年依然是未知数，改变更好的IS反而会过拟合，影响表现。其次，达标以后，我交一个PPA，删一个ppa tag，以保我的combine还能维持住！


> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化趋势
> Combined Alpha
> POWer Pool
> 0
> Selected Alpha
> 0 Combined Osmosis
> Combined
> 3.00
> 2.00
> 1.00
> 0.00
> 1.00
> 2.00
> 202510
> 20251
> 202512
> 202601
> 202602


### 三、碎碎念

回顾三赛季历程，感叹时间飞速，在这期间我学到了很多知识，认识到了很多人，来自五湖四海，各行各业，各个年龄段，宛如线上旅游，了解各地工作就业情况，体验各个地区的人文交流，颇感良多，感谢各位一路陪伴，终于实现了Gold直通GrandMaster的奇迹！

#### **（一） IQC赛季（2025-Q2）**

从零开始的量化之路，我从一个回测界面Simulate都需要单词查询意思的人，通过翻译以及挨个按钮点击学习，了解到了WQ平台的运作原理，开始使用machine_lib.py代码为基础的回测流程，同一开始的无脑一二三阶，二三阶叠加，变成了有精准选择的使用一二阶。

1. 通过一阶代码，将ts_ops(ts_backfill(winsorize(单字段)))，选择改进零阶单字段，把单字段变成多字段组合形式，我提供给AI一个数据集里面的字段和描述，通过简单的四则运算给我一键制作零阶字段，省回测且有经济学意义的方法，例如新手教程的option8, call - put 双字段以后进行其他操作符叠加，得到alpha。

2. 通过给二阶代码加入相关性剪枝，进行对一阶alpha的剪枝，减去大部分重复alpha，并且关于bukcet进行更多的想象力，详细内容可以从课代表（ [XX42289](/hc/zh-cn/profiles/14187300941847-XX42289) ）的帖子进行学习，制作有经济学意义的特别bucket，这里面不只是bucket(rank)，不只是range ="0.1,1,0.1"，还可以更多的操作符，更多的字段，更多的参数范围，这使得我在IQC期间交了很多alpha。

#### **（二）初步了解赛季（2025-Q3）**

IQC顾问转正式顾问，跨度很大，IQC的长周期让人陷入在用户权限的温柔乡，在这里学习了很多知识，才进入顾问的状态。

1. 了解RA,ATOM,PPA,SA四大类的区别和提交区别，以及IS指标的作用，sc，ppac，pc三者的区别与联系。

2. 修改回测代码，将用户三并发改为8*10并发，解决4xx，5xx报错问题，使得代码更加稳健，除了亚马逊服务器崩了，一般不会再有问题了 : (

3. 读论坛所有经验贴，避雷贴，结合回测出来的alpha进行IS数据的初步了解，知道什么alpha可以提交，什么alpha肯定不能提交，学习什么会影响VF和combine稳定，地区这么多可不可以多开，新手应该交什么样的alpha，以至于我这个赛季就交了31个alpha，实际VF combine也还行，没什么大事，combine稳定提升，VF最低0.64，起码大于0.5。

#### **（三）稳扎稳打赛季（2025-Q4）**

终于学的差不多了，开始尝试冲级，此时的我combine从0.79变成了1.52上下徘徊，说明质量没什么问题，开始往上走，这个时候我不交PPA，对PPA还不是很明白，顶多是RA+PPA+ATOM这种情况，顺带提交PPA，这也是日后的一个伏笔。

1. PPA combine一直不咋好，0.14，删除了第一个不知道怎么提交的顾问PPA，更新一跃2.49，从此稳定2+，奠定了冲级的资格。

2. 此时我并不知道六维带来的影响很大，还是用着用户的方法，bucket使用的操作符很多，densify我也没删，操作符平均数量飙升，加上刚转顾问断了一天回测，六维太可怜了，赛季末使用华子哥插件expert排行985，遗憾被刷，依然GOLD。

3. 但是当时做出来的alpha，在日后的OS更新后，明显可以看出来，质量很好，不过操作符比较多，bucket的二阶是一个提升质量不可多得好方法！

#### **（四）奇迹出现赛季（2025-Q1）**

三赛季铺垫，终于厚积薄发！开头的我也是几天偶尔交一个，到了赛季更新后，各种新规则出来，我下定决心，直冲GM，二月初的时候我也不到7个塔，直接二月底到达35塔，四月冲级60塔，人不逼自己一把，不知道自己的上限有多高！

1.  PPA大削，趁机通过RA进行点塔，我采用5op，2fileds方式进行RA制作，保证我的六维维持在这附近，下篇我会详细讲六维这方面。

2.  返璞归真，AI+machine_lib，制作模版，遍历模版，保证4+1点塔，按照数据集进行分析，不同数据集制作不同模版，同数据集同预处理模版，二次切换不同一阶二阶，可得到无穷无尽的RA，只不过还需要看IS和近四年趋势，有些RA我并不会选择提交。

3.  华子哥RAW数据横空出世！得到了全部数据，我开始精准选择我有的数据集，通过筛选我的要求，进行选择中性化和字段，精准打击alpha！既然他们能做出来，那我也能做出来的思想，做出来一个又一个小数据集的ATOM+RA！

最后的最后，再次感谢各位朋友陪伴，使得我能够创造奇迹：

感谢WQ平台，感谢国区各位老师，感谢研究小组二群的各位，感谢IQC的朋友们（以下排名，不分先后）：

感谢weijie老师，kunqi老师，huangkai老师，顾问 KZ79256 (Rank 21) (华子哥)，XX42289 (课代表) ，worldquant brain赛博游戏王 (游戏王)，顾问 QX52484 (Rank 35) (司源老师)，顾问 FX25214 (Rank 22)，DA98440，JX39934，ZH41150，顾问 顾问 RM49262 (Rank 30) (Rank 30)，PP26750， LD27384，顾问 JG15244 (Rank 67)，LS17092，WT73952，XJ80376，QW94165，ZY20347，JZ45765，ll46807，JW52291等研究小组二群的各位朋友们！！！！

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

太强了尼克 Gold直升GM

这篇经验贴也是干活满满，学到了很多！祝尼克一直GM下去！

=============================================================================


---

### 技术对话片段 46 (原帖: Roo 顾问提示: 这是您个人评估标准的核心，调整这些阈值以符合您的投资组合策略。)
- **原帖链接**: [Commented] 【MCP 工作流】论坛模板评估经验分享.md
- **时间**: 10个月前

**提问/主帖背景 (FD69320)**:
以下是我用的上下文，还在调教中，虽然有点笨，但很乖很听话。

```
# WorldQuant论坛模板质量评估工作流程## 概述本文档详细描述了分析WorldQuant BRAIN论坛中Alpha模板并评估其质量的工作流程。新同事将负责从论坛中识别有价值的Alpha模板，评估其质量，并为团队提供高质量的模板推荐。工作流程强调模板的经济学含义、可实施性、回测效果和优化程度，确保推荐的模板符合PPA提交标准，特别是ATOM类型Alpha。## 总体工作流程1. **认证与准备**：通过BRAIN MCP工具认证，访问平台和论坛数据2. **模板发现与收集**：搜索论坛中的Alpha模板和相关讨论3. **初步筛选**：基于基本标准进行第一轮筛选4. **深度分析**：对筛选出的模板进行详细分析，包括经济学含义、可实施性等5. **回测验证**：将模板转换为Alpha表达式并进行回测6. **质量评估**：基于多维度指标进行综合评分7. **报告撰写**：生成详细的评估报告和推荐建议8. **持续监控**：跟踪已推荐模板的后续表现## 具体步骤与MCP工具使用### 步骤1：认证与准备（5分钟）**目标**：确保能够访问BRAIN平台和论坛数据**具体操作**：1. 使用BRAIN MCP工具进行认证   - 工具：`mcp_worldquant-brain-platform_authenticate`   - 参数：提供用户邮箱和密码2. 验证认证状态   - 工具：`mcp_worldquant-brain-platform_manage_config`   - 参数：action="get"**输出**：认证成功确认，获取用户权限信息### 步骤2：模板发现与收集（15-20分钟）**目标**：从论坛中搜索和收集Alpha模板**具体操作**：1. **搜索论坛帖子**：使用关键词搜索相关模板讨论   - 工具：`mcp_worldquant-brain-platform_search_forum_posts`   - 参数：     - search_query: "alpha template" OR "alpha formula" OR "alpha strategy"     - max_results: 100     - headless: true2. **获取热门讨论**：搜索特定主题的模板   - 工具：`mcp_worldquant-brain-platform_search_forum_posts`   - 参数：     - search_query: "ATOM alpha" OR "momentum" OR "value factor" OR "quality factor"     - max_results: 50     - headless: true3. **获取术语表**：了解论坛中的专业术语   - 工具：`mcp_worldquant-brain-platform_get_glossary_terms`   - 参数：headless=true**输出**：论坛帖子列表，包含模板讨论和代码示例### 步骤3：初步筛选（10-15分钟）**目标**：基于基本标准进行第一轮筛选**筛选标准**：1. 帖子包含完整的Alpha表达式或伪代码2. 有明确的策略描述或经济学逻辑3. 讨论热度较高（回复数量、点赞数等）4. 发布时间较新（优先考虑最近6个月）**具体操作**：1. 分析搜索结果，识别包含完整模板的帖子2. 记录帖子ID、标题、作者、发布时间、热度指标3. 初步分类：按策略类型（动量、价值、质量、技术等）**输出**：初步筛选后的模板列表，包含基本信息### 步骤4：深度分析（20-30分钟）**目标**：对筛选出的模板进行详细分析**分析维度**：#### 4.1 经济学含义分析- **评估标准**：  - 是否有明确的经济学理论支撑  - 策略逻辑是否清晰易懂  - 是否符合市场微观结构理论  - 是否有学术研究支持#### 4.2 可实施性分析- **评估标准**：  - 表达式语法是否正确  - 使用的数据字段是否在BRAIN平台可用  - 操作符使用是否合理  - 是否需要特殊的数据处理**具体操作**：1. **获取可用数据字段**：验证模板中使用的数据字段   - 工具：`mcp_brain-api_get_datafields`   - 参数：     - instrument_type: "EQUITY"     - region: "USA"     - search: [具体字段名]2. **获取可用操作符**：验证模板中使用的操作符   - 工具：`mcp_brain-api_get_operators`3. **获取平台设置选项**：了解可用的回测参数   - 工具：`mcp_brain-api_get_platform_setting_options`**输出**：每个模板的详细分析报告，包含经济学含义评分和可实施性评分### 步骤5：回测验证（30-60分钟）**目标**：将模板转换为Alpha表达式并进行回测**具体操作**：1. **创建回测表达式**：将论坛模板转换为可执行的Alpha表达式，如果模板带有Operator的占位符，选取合适的占位符替换，如果模板带有数据字段的占位符选取合适的数据字段替换，表达式不需要有注释，保证简单直接，每一行用分号;隔开。   - 工具：`mcp_brain-api_get_operators`   - 工具：`mcp_brain-api_get_datafields`   - 参数：     - instrument_type: "EQUITY"     - region: "USA"     - search: [关键词]2. **运行回测**：使用BRAIN平台进行回测，如果回测失败，可能是语法错误，调整语法，**重试最多三次**，如果还是不行，进行下一个模板的回测   - 工具：`mcp_brain-api_create_simulation`   - 参数：     - type: "REGULAR"     - instrument_type: "EQUITY"     - region: "USA"     - universe: "TOP3000"     - delay: 1     - decay: 0     - test_period: "P0D"     - truncation: 0.08     - neutralization: "NONE"     - visualization: false     - max_trade: "ON"     - regular: [转换后的Alpha表达式]3. **获取回测结果**：分析回测性能   - 工具：`mcp_brain-api_get_alpha_details`   - 参数：alpha_id: [回测ID]   - 工具：`mcp_brain-api_get_alpha_pnl`   - 参数：alpha_id: [回测ID]   - 工具：`mcp_brain-api_get_alpha_yearly_stats`   - 参数：alpha_id: [回测ID]**输出**：回测结果，包含关键性能指标### 步骤6：质量评估（15-20分钟）**目标**：基于多维度指标进行综合评分，如果第5步没有成功的回测结果，跳过这一步。**评估指标体系**：#### 6.1 核心指标评分（权重：50%）- **Sharpe Ratio**：  - 优秀：≥1.5（5分）  - 良好：1.25-1.5（4分）  - 一般：1.0-1.25（3分）  - 较差：<1.0（2分）- **Fitness**：  - 优秀：≥1.2（5分）  - 良好：1.0-1.2（4分）  - 一般：0.8-1.0（3分）  - 较差：<0.8（2分）- **Margin**：  - 优秀：≥0.8（5分）  - 良好：0.6-0.8（4分）  - 一般：0.4-0.6（3分）  - 较差：<0.4（2分）#### 6.2 风险控制评分（权重：25%）- **Turnover**：  - 优秀：≤0.3（5分）  - 良好：0.3-0.5（4分）  - 一般：0.5-0.7（3分）  - 较差：>0.7（2分）- **Drawdown**：  - 优秀：≤0.1（5分）  - 良好：0.1-0.2（4分）  - 一般：0.2-0.3（3分）  - 较差：>0.3（2分）#### 6.3 复杂度评分（权重：15%）- **操作符数量**：  - 优秀：≤5个（5分）  - 良好：6-10个（4分）  - 一般：11-15个（3分）  - 较差：>15个（2分）- **数据字段数量**：  - 优秀：≤3个（5分）  - 良好：4-6个（4分）  - 一般：7-10个（3分）  - 较差：>10个（2分）#### 6.4 PnL曲线质量评分（权重：10%）- **曲线平滑度**：  - 优秀：平滑向上，无明显回撤（5分）  - 良好：整体向上，偶有小幅回撤（4分）  - 一般：波动较大但趋势向上（3分）  - 较差：波动剧烈，趋势不明确（2分）**综合评分计算**：```综合评分 = 核心指标评分 × 0.5 + 风险控制评分 × 0.25 + 复杂度评分 × 0.15 + PnL曲线质量评分 × 0.1```**评分等级**：- A级：4.5-5.0分（强烈推荐）- B级：3.5-4.4分（推荐）- C级：2.5-3.4分（一般）- D级：<2.5分（不推荐）**具体操作**：1. 计算各项指标得分2. 计算综合评分3. 确定评分等级4. 记录评分依据和详细分析**输出**：每个模板的综合评分和等级### 步骤7：报告撰写（20-30分钟）**目标**：生成详细的评估报告和推荐建议**报告结构**：#### 7.1 执行摘要- 评估的模板总数- 推荐模板数量（A级和B级）- 主要发现和建议#### 7.2 模板详细评估- **模板1**：[模板名称]  - 来源：论坛帖子链接  - 策略描述：经济学含义和逻辑  - 回测结果：关键指标数据  - 质量评分：各项得分和综合评分  - 推荐等级：A/B/C/D  - 改进建议：具体优化方向#### 7.3 推荐模板汇总- A级模板列表（强烈推荐）- B级模板列表（推荐）- 按策略类型分类#### 7.4 实施建议- 优先实施的模板顺序- 需要的资源和支持- 风险提示和注意事项**具体操作**：1. 整理所有评估数据2. 撰写详细报告3. 生成推荐模板清单4. 提供实施路线图**输出**：完整的评估报告（Markdown格式）### 步骤8：持续监控（每周）**目标**：跟踪已推荐模板的后续表现**具体操作**：1. **监控已实施模板**：定期检查推荐模板的回测表现   - 工具：`mcp_brain-api_get_alpha_pnl`   - 工具：`mcp_brain-api_get_alpha_yearly_stats`2. **更新评估结果**：根据新数据调整评分3. **收集用户反馈**：了解团队使用模板的体验4. **优化评估标准**：根据实践结果改进评估体系**输出**：定期更新报告和评分调整## 工作流程模板### 每日工作模板```markdown# 模板评估日报 - [日期]## 今日工作内容- 搜索论坛模板：__个- 初步筛选：__个- 深度分析：__个- 回测验证：__个- 质量评估：__个## 发现的高质量模板1. [模板名称] - 评分：__/5.0 - 等级：__2. [模板名称] - 评分：__/5.0 - 等级：__## 明日工作计划- [具体任务1]- [具体任务2]## 遇到的问题- [问题描述及解决方案]```### 评估记录模板```markdown# 模板评估记录 - [模板名称]## 基本信息- 来源：论坛帖子ID- 发布时间：[日期]- 作者：[用户名]- 热度：[回复数/点赞数]## 策略分析- 经济学含义：[描述]- 策略逻辑：[描述]- 理论支撑：[描述]## 可实施性分析- 数据字段可用性：[检查结果]- 操作符可用性：[检查结果]- 语法正确性：[检查结果]## 回测结果- Alpha ID：[ID]- Sharpe Ratio：[数值]- Fitness：[数值]- Margin：[数值]- Turnover：[数值]- Drawdown：[数值]## 质量评分- 核心指标评分：__/5.0- 风险控制评分：__/5.0- 复杂度评分：__/5.0- PnL曲线质量评分：__/5.0- 综合评分：__/5.0- 推荐等级：[A/B/C/D]## 改进建议- [具体建议1]- [具体建议2]## 备注[其他重要信息]```## 质量控制与错误防范### 常见错误及防范措施1. **回测参数设置错误**：   - **错误示例**：使用了不兼容的region和universe组合   - **防范措施**：使用`mcp_brain-api_get_platform_setting_options`验证参数组合   - **验证步骤**：在回测前确认所有参数的有效性2. **数据字段验证不足**：   - **错误示例**：模板使用了平台不存在的数据字段   - **防范措施**：使用`mcp_brain-api_get_datafields`验证每个字段   - **验证步骤**：建立常用字段清单，定期更新3. **评分标准不一致**：   - **防范措施**：建立标准化的评分表格和计算工具   - **质量检查**：定期回顾评分结果，确保一致性### 持续改进机制- 记录每次评估的详细过程- 收集团队反馈，优化评估标准- 建立模板质量数据库，追踪长期表现- 定期更新评估体系，适应平台变化## 工具使用最佳实践### 并行化操作- 同时运行多个回测以提高效率- 使用多线程处理数据收集和分析### 数据缓存- 缓存常用的数据字段和操作符信息- 避免重复查询相同信息### 错误处理- 建立完善的错误处理机制- 记录所有工具调用错误，便于调试## 总结本工作流程为WorldQuant论坛模板质量评估提供了系统化的方法，确保推荐的模板具有高质量、可实施性和良好的回测表现。通过使用BRAIN MCP工具，新同事可以高效地完成模板发现、分析、验证和评估的完整流程，为团队提供有价值的Alpha策略模板。工作流程强调质量优先，通过多维度评估确保推荐的模板符合PPA提交标准，特别是ATOM类型Alpha。同时，持续监控和改进机制确保评估体系的准确性和实用性。如有任何问题或需要进一步指导，请随时与团队其他成员或平台支持团队联系。
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
感谢大佬！ MCP搜到了这篇文章，我直接喊他follow instruction就好哈哈


---

### 技术对话片段 47 (原帖: Roo 顾问提示: 这是您个人评估标准的核心，调整这些阈值以符合您的投资组合策略。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【MCP 工作流】论坛模板评估经验分享_34310411227799.md
- **时间**: 10个月前

**提问/主帖背景 (FD69320)**:
以下是我用的上下文，还在调教中，虽然有点笨，但很乖很听话。

```
# WorldQuant论坛模板质量评估工作流程## 概述本文档详细描述了分析WorldQuant BRAIN论坛中Alpha模板并评估其质量的工作流程。新同事将负责从论坛中识别有价值的Alpha模板，评估其质量，并为团队提供高质量的模板推荐。工作流程强调模板的经济学含义、可实施性、回测效果和优化程度，确保推荐的模板符合PPA提交标准，特别是ATOM类型Alpha。## 总体工作流程1. **认证与准备**：通过BRAIN MCP工具认证，访问平台和论坛数据2. **模板发现与收集**：搜索论坛中的Alpha模板和相关讨论3. **初步筛选**：基于基本标准进行第一轮筛选4. **深度分析**：对筛选出的模板进行详细分析，包括经济学含义、可实施性等5. **回测验证**：将模板转换为Alpha表达式并进行回测6. **质量评估**：基于多维度指标进行综合评分7. **报告撰写**：生成详细的评估报告和推荐建议8. **持续监控**：跟踪已推荐模板的后续表现## 具体步骤与MCP工具使用### 步骤1：认证与准备（5分钟）**目标**：确保能够访问BRAIN平台和论坛数据**具体操作**：1. 使用BRAIN MCP工具进行认证   - 工具：`mcp_worldquant-brain-platform_authenticate`   - 参数：提供用户邮箱和密码2. 验证认证状态   - 工具：`mcp_worldquant-brain-platform_manage_config`   - 参数：action="get"**输出**：认证成功确认，获取用户权限信息### 步骤2：模板发现与收集（15-20分钟）**目标**：从论坛中搜索和收集Alpha模板**具体操作**：1. **搜索论坛帖子**：使用关键词搜索相关模板讨论   - 工具：`mcp_worldquant-brain-platform_search_forum_posts`   - 参数：     - search_query: "alpha template" OR "alpha formula" OR "alpha strategy"     - max_results: 100     - headless: true2. **获取热门讨论**：搜索特定主题的模板   - 工具：`mcp_worldquant-brain-platform_search_forum_posts`   - 参数：     - search_query: "ATOM alpha" OR "momentum" OR "value factor" OR "quality factor"     - max_results: 50     - headless: true3. **获取术语表**：了解论坛中的专业术语   - 工具：`mcp_worldquant-brain-platform_get_glossary_terms`   - 参数：headless=true**输出**：论坛帖子列表，包含模板讨论和代码示例### 步骤3：初步筛选（10-15分钟）**目标**：基于基本标准进行第一轮筛选**筛选标准**：1. 帖子包含完整的Alpha表达式或伪代码2. 有明确的策略描述或经济学逻辑3. 讨论热度较高（回复数量、点赞数等）4. 发布时间较新（优先考虑最近6个月）**具体操作**：1. 分析搜索结果，识别包含完整模板的帖子2. 记录帖子ID、标题、作者、发布时间、热度指标3. 初步分类：按策略类型（动量、价值、质量、技术等）**输出**：初步筛选后的模板列表，包含基本信息### 步骤4：深度分析（20-30分钟）**目标**：对筛选出的模板进行详细分析**分析维度**：#### 4.1 经济学含义分析- **评估标准**：  - 是否有明确的经济学理论支撑  - 策略逻辑是否清晰易懂  - 是否符合市场微观结构理论  - 是否有学术研究支持#### 4.2 可实施性分析- **评估标准**：  - 表达式语法是否正确  - 使用的数据字段是否在BRAIN平台可用  - 操作符使用是否合理  - 是否需要特殊的数据处理**具体操作**：1. **获取可用数据字段**：验证模板中使用的数据字段   - 工具：`mcp_brain-api_get_datafields`   - 参数：     - instrument_type: "EQUITY"     - region: "USA"     - search: [具体字段名]2. **获取可用操作符**：验证模板中使用的操作符   - 工具：`mcp_brain-api_get_operators`3. **获取平台设置选项**：了解可用的回测参数   - 工具：`mcp_brain-api_get_platform_setting_options`**输出**：每个模板的详细分析报告，包含经济学含义评分和可实施性评分### 步骤5：回测验证（30-60分钟）**目标**：将模板转换为Alpha表达式并进行回测**具体操作**：1. **创建回测表达式**：将论坛模板转换为可执行的Alpha表达式，如果模板带有Operator的占位符，选取合适的占位符替换，如果模板带有数据字段的占位符选取合适的数据字段替换，表达式不需要有注释，保证简单直接，每一行用分号;隔开。   - 工具：`mcp_brain-api_get_operators`   - 工具：`mcp_brain-api_get_datafields`   - 参数：     - instrument_type: "EQUITY"     - region: "USA"     - search: [关键词]2. **运行回测**：使用BRAIN平台进行回测，如果回测失败，可能是语法错误，调整语法，**重试最多三次**，如果还是不行，进行下一个模板的回测   - 工具：`mcp_brain-api_create_simulation`   - 参数：     - type: "REGULAR"     - instrument_type: "EQUITY"     - region: "USA"     - universe: "TOP3000"     - delay: 1     - decay: 0     - test_period: "P0D"     - truncation: 0.08     - neutralization: "NONE"     - visualization: false     - max_trade: "ON"     - regular: [转换后的Alpha表达式]3. **获取回测结果**：分析回测性能   - 工具：`mcp_brain-api_get_alpha_details`   - 参数：alpha_id: [回测ID]   - 工具：`mcp_brain-api_get_alpha_pnl`   - 参数：alpha_id: [回测ID]   - 工具：`mcp_brain-api_get_alpha_yearly_stats`   - 参数：alpha_id: [回测ID]**输出**：回测结果，包含关键性能指标### 步骤6：质量评估（15-20分钟）**目标**：基于多维度指标进行综合评分，如果第5步没有成功的回测结果，跳过这一步。**评估指标体系**：#### 6.1 核心指标评分（权重：50%）- **Sharpe Ratio**：  - 优秀：≥1.5（5分）  - 良好：1.25-1.5（4分）  - 一般：1.0-1.25（3分）  - 较差：<1.0（2分）- **Fitness**：  - 优秀：≥1.2（5分）  - 良好：1.0-1.2（4分）  - 一般：0.8-1.0（3分）  - 较差：<0.8（2分）- **Margin**：  - 优秀：≥0.8（5分）  - 良好：0.6-0.8（4分）  - 一般：0.4-0.6（3分）  - 较差：<0.4（2分）#### 6.2 风险控制评分（权重：25%）- **Turnover**：  - 优秀：≤0.3（5分）  - 良好：0.3-0.5（4分）  - 一般：0.5-0.7（3分）  - 较差：>0.7（2分）- **Drawdown**：  - 优秀：≤0.1（5分）  - 良好：0.1-0.2（4分）  - 一般：0.2-0.3（3分）  - 较差：>0.3（2分）#### 6.3 复杂度评分（权重：15%）- **操作符数量**：  - 优秀：≤5个（5分）  - 良好：6-10个（4分）  - 一般：11-15个（3分）  - 较差：>15个（2分）- **数据字段数量**：  - 优秀：≤3个（5分）  - 良好：4-6个（4分）  - 一般：7-10个（3分）  - 较差：>10个（2分）#### 6.4 PnL曲线质量评分（权重：10%）- **曲线平滑度**：  - 优秀：平滑向上，无明显回撤（5分）  - 良好：整体向上，偶有小幅回撤（4分）  - 一般：波动较大但趋势向上（3分）  - 较差：波动剧烈，趋势不明确（2分）**综合评分计算**：```综合评分 = 核心指标评分 × 0.5 + 风险控制评分 × 0.25 + 复杂度评分 × 0.15 + PnL曲线质量评分 × 0.1```**评分等级**：- A级：4.5-5.0分（强烈推荐）- B级：3.5-4.4分（推荐）- C级：2.5-3.4分（一般）- D级：<2.5分（不推荐）**具体操作**：1. 计算各项指标得分2. 计算综合评分3. 确定评分等级4. 记录评分依据和详细分析**输出**：每个模板的综合评分和等级### 步骤7：报告撰写（20-30分钟）**目标**：生成详细的评估报告和推荐建议**报告结构**：#### 7.1 执行摘要- 评估的模板总数- 推荐模板数量（A级和B级）- 主要发现和建议#### 7.2 模板详细评估- **模板1**：[模板名称]  - 来源：论坛帖子链接  - 策略描述：经济学含义和逻辑  - 回测结果：关键指标数据  - 质量评分：各项得分和综合评分  - 推荐等级：A/B/C/D  - 改进建议：具体优化方向#### 7.3 推荐模板汇总- A级模板列表（强烈推荐）- B级模板列表（推荐）- 按策略类型分类#### 7.4 实施建议- 优先实施的模板顺序- 需要的资源和支持- 风险提示和注意事项**具体操作**：1. 整理所有评估数据2. 撰写详细报告3. 生成推荐模板清单4. 提供实施路线图**输出**：完整的评估报告（Markdown格式）### 步骤8：持续监控（每周）**目标**：跟踪已推荐模板的后续表现**具体操作**：1. **监控已实施模板**：定期检查推荐模板的回测表现   - 工具：`mcp_brain-api_get_alpha_pnl`   - 工具：`mcp_brain-api_get_alpha_yearly_stats`2. **更新评估结果**：根据新数据调整评分3. **收集用户反馈**：了解团队使用模板的体验4. **优化评估标准**：根据实践结果改进评估体系**输出**：定期更新报告和评分调整## 工作流程模板### 每日工作模板```markdown# 模板评估日报 - [日期]## 今日工作内容- 搜索论坛模板：__个- 初步筛选：__个- 深度分析：__个- 回测验证：__个- 质量评估：__个## 发现的高质量模板1. [模板名称] - 评分：__/5.0 - 等级：__2. [模板名称] - 评分：__/5.0 - 等级：__## 明日工作计划- [具体任务1]- [具体任务2]## 遇到的问题- [问题描述及解决方案]```### 评估记录模板```markdown# 模板评估记录 - [模板名称]## 基本信息- 来源：论坛帖子ID- 发布时间：[日期]- 作者：[用户名]- 热度：[回复数/点赞数]## 策略分析- 经济学含义：[描述]- 策略逻辑：[描述]- 理论支撑：[描述]## 可实施性分析- 数据字段可用性：[检查结果]- 操作符可用性：[检查结果]- 语法正确性：[检查结果]## 回测结果- Alpha ID：[ID]- Sharpe Ratio：[数值]- Fitness：[数值]- Margin：[数值]- Turnover：[数值]- Drawdown：[数值]## 质量评分- 核心指标评分：__/5.0- 风险控制评分：__/5.0- 复杂度评分：__/5.0- PnL曲线质量评分：__/5.0- 综合评分：__/5.0- 推荐等级：[A/B/C/D]## 改进建议- [具体建议1]- [具体建议2]## 备注[其他重要信息]```## 质量控制与错误防范### 常见错误及防范措施1. **回测参数设置错误**：   - **错误示例**：使用了不兼容的region和universe组合   - **防范措施**：使用`mcp_brain-api_get_platform_setting_options`验证参数组合   - **验证步骤**：在回测前确认所有参数的有效性2. **数据字段验证不足**：   - **错误示例**：模板使用了平台不存在的数据字段   - **防范措施**：使用`mcp_brain-api_get_datafields`验证每个字段   - **验证步骤**：建立常用字段清单，定期更新3. **评分标准不一致**：   - **防范措施**：建立标准化的评分表格和计算工具   - **质量检查**：定期回顾评分结果，确保一致性### 持续改进机制- 记录每次评估的详细过程- 收集团队反馈，优化评估标准- 建立模板质量数据库，追踪长期表现- 定期更新评估体系，适应平台变化## 工具使用最佳实践### 并行化操作- 同时运行多个回测以提高效率- 使用多线程处理数据收集和分析### 数据缓存- 缓存常用的数据字段和操作符信息- 避免重复查询相同信息### 错误处理- 建立完善的错误处理机制- 记录所有工具调用错误，便于调试## 总结本工作流程为WorldQuant论坛模板质量评估提供了系统化的方法，确保推荐的模板具有高质量、可实施性和良好的回测表现。通过使用BRAIN MCP工具，新同事可以高效地完成模板发现、分析、验证和评估的完整流程，为团队提供有价值的Alpha策略模板。工作流程强调质量优先，通过多维度评估确保推荐的模板符合PPA提交标准，特别是ATOM类型Alpha。同时，持续监控和改进机制确保评估体系的准确性和实用性。如有任何问题或需要进一步指导，请随时与团队其他成员或平台支持团队联系。
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
感谢大佬！ MCP搜到了这篇文章，我直接喊他follow instruction就好哈哈


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【OSMOSIS新人友好版】真正的一键打分指定区域清空补齐10类标签过滤_39408397746199.md
- **时间**: 2个月前

**提问/主帖背景 (BQ64903)**:
前几天看到  **[XX42289](/hc/en-us/profiles/14187300941847-XX42289)**   [【课代表】【轻松点击即可完成参赛】CA 降维 + 多指标聚类数评判 + KMeans / 层次 / DBSCAN 聚类的 Osmosis 点数分配工具 – WorldQuant BRAIN]([Commented] 【课代表】【轻松点击即可完成参赛】CA 降维  多指标聚类数评判  KMeans  层次  DBSCAN 聚类的 Osmosis 点数分配工具经验分享_37023499938327.md) 和 [顾问 JR23144 (Rank 6)](/hc/en-us/profiles/28844048981143-顾问 JR23144 (Rank 6))  [【贺六浑】-【工具配置】OC2025 一键清空分数脚本 – WorldQuant BRAIN]([L2] 【贺六浑】-【工具配置】OC2025 一键清空分数脚本经验分享_37090321198359.md) 的文章。发现一些细节不足：

1. 清除分数会将所有区域清除，且不包含super alpha
2. 分配分数时四舍五入的偏差并没有通过API更新
3. 分类结果可能小于10类，不满足打分标准

所以在此做了略微改进，主要在于：

1. 给指定区域打分前先清空该区域所有分数（包括super alpha）
2. 通过API更新四舍五入的偏差
3. 不足十类的，给其他alpha赋值1，强行满足要求
4. 支持通过颜色/tag筛选要打分的alpha（这样可以把AI提交的烂alpha排除出去）

```
# # 清空# In[1]:# -*- coding: utf-8 -*-import urllib.parseimport loggingimport numpy as npimport pandas as pdfrom sklearn.preprocessing import StandardScaler, RobustScalerfrom sklearn.cluster import KMeans, DBSCAN, AgglomerativeClusteringfrom sklearn.metrics import silhouette_score, calinski_harabasz_scorefrom sklearn.decomposition import PCA# 假设该库返回requests.Session对象#from machine_lib import login  from ace_lib import (    start_session )import timefrom datetime import datetime, timedelta#from machine_lib import *  # 假设 login() 在这里from concurrent.futures import ThreadPoolExecutorimport json# In[2]:# ===================================================================# PART 1: 配置与函数定义# ===================================================================#  并发清除操作的线程数MAX_WORKERS = 10def up_alpha_properties_to_clear(s, alpha_id: str, old_osmosisPoints: str):    """    一个专门用于清除 Alpha 分数的函数。    它通过将 'osmosisPoints' 字段设置为 null 来实现。    """    params = {"osmosisPoints": None}  # 在 requests 中, None 会被序列化为 JSON null    response = s.patch(        f"[链接已屏蔽] json=params    )    if response.status_code == 200:        print(f"成功清除 Alpha {alpha_id} 的分数 (原分数: {old_osmosisPoints})。")        return "SUCCESS"    else:        print(f"清除 Alpha {alpha_id} 分数失败，状态码: {response.status_code}, 信息: {response.text}")        return "FAILED"def get_colored_alphas_in_date_range(s, start_date, end_date, region, alpha_num_limit=1000):    """    获取在指定日期范围内，所有设置了分数的Alpha。    """    colored_alphas = []    print(f"开始查找从 {start_date} 到 {end_date} 所有已设置分数的常规 Alpha...")    for i in range(0, alpha_num_limit, 100):        print(f"正在扫描第 {i} 到 {i + 100} 个 alpha...")        # 【重要】在 URL 中加入了 dateSubmitted 过滤器        url_e = (            f"[链接已屏蔽]            f"&status!=UNSUBMITTED&status!=IS_FAIL&hidden=false"            f"&dateSubmitted>={start_date}T00:00:00-04:00"            f"&dateSubmitted<{end_date}T00:00:00-04:00"            f"&settings.region={region}"          )        try:            response = s.get(url_e)            response.raise_for_status()            alpha_list = response.json().get("results", [])            if not alpha_list:                print("已扫描完所有符合条件的 Alpha。")                break            # 在客户端筛选出有分数的 Alpha            for alpha in alpha_list:                if alpha.get("osmosisPoints") is not None:                    record = {                        "id": alpha["id"],                        "osmosisPoints": alpha["osmosisPoints"]                    }                    colored_alphas.append(record)        except Exception as e:            print(f"获取alpha时发生异常: {e}")            resp = s.get('[链接已屏蔽])            if resp.status_code != 200:                print(f"用户会话可能已过期，状态码: {resp.status_code}")            break    print(f"\n查找完毕！共找到 {len(colored_alphas)} 个在指定日期内需要清除分数的 Alpha。")    return colored_alphas# In[3]:def get_history_alpha_ids(s, region, start_date, limit=50, offset=0, exclude_tags=None, exclude_color=None):    """    从接口分页获取指定地区、指定日期后的alpha数据    :param s: requests.Session对象，已完成登录的会话    :param region: 地区大写：USA, EUR ... ...    :param start_date: 过滤日期，获取该日期之后的因子    :param limit: 每页获取的数量    :param offset: 分页偏移量    :return: 包含alpha的id和各类is指标的列表    """    alphas_data = []    # 对日期字符串进行URL编码，避免特殊字符影响请求    start_date_str = urllib.parse.quote(start_date.astimezone().isoformat(timespec='seconds'))    # 分页获取数据    #去掉color为红的    while True:        url = (            f"[链接已屏蔽]            f"limit={limit}&offset={offset}"            f"&dateCreated%3E={start_date_str}"            f"&settings.region={region}"            f"&status!=UNSUBMITTED%1FIS-FAIL"            f"&hidden=false"            f"&order=-dateSubmitted"            f"&color!={exclude_color}"            f"&tag!={exclude_tags}"        )        try:            resp = s.get(url)            if resp.status_code != 200:                print(f"请求出错，状态码：{resp.status_code}")                break            data = resp.json()            results = data.get("results", [])            alphas_data.extend(results)            # 判断是否获取完所有数据，是则退出循环            if offset + len(results) >= data.get("count", 0) or len(results) < limit:                break            offset += limit        except Exception as e:            print(f"数据获取异常，异常信息：{e}")            break    # 提取需要的指标数据    alpha_metrics = []    for item in alphas_data:        # 检查is中的关键指标是否存在，避免键缺失报错        is_data = item.get('is', {})        metrics = {            'id': item['id'],            'fitness': is_data.get('fitness', 0.0),            'longCount': is_data.get('longCount', 0.0),            'shortCount': is_data.get('shortCount', 0.0),            'turnover': is_data.get('turnover', 0.0),            'returns': is_data.get('returns', 0.0),            'drawdown': is_data.get('drawdown', 0.0),            'margin': is_data.get('margin', 0.0),            'sharpe': is_data.get('sharpe', 0.0)        }        alpha_metrics.append(metrics)    if not alpha_metrics:        print("错误：没有获取到有效的alpha数据")        return []    return alpha_metricsdef determine_clusters_multi_criteria(X, min_clusters=5, max_clusters=50):    """    多指标确定聚类数（结合轮廓系数、CH指数，同时限制聚类数范围）    :param X: 标准化后的特征数据    :param min_clusters: 最小聚类数（避免过少）    :param max_clusters: 最大聚类数（避免过多）    :return: 最终聚类数量    """    if len(X) <= min_clusters:        return len(X)  # 样本数少于最小聚类数时，取样本数    # 限制聚类数范围：2 ~ 样本数（但不超过max_clusters，不低于min_clusters）    cluster_range = range(max(2, min_clusters), min(max_clusters + 1, len(X)))    scores = []    for k in cluster_range:        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')        labels = kmeans.fit_predict(X)        # 轮廓系数：衡量聚类紧密度和分离度，越接近1越好        sil_score = silhouette_score(X, labels)        # CH指数：数值越大表示聚类效果越好（类内紧密，类间分离）        ch_score = calinski_harabasz_score(X, labels)        # 综合得分（归一化后加权，可调整权重）        scores.append({            'k': k,            'sil': sil_score,            'ch': ch_score,            # 权重可调整，平衡轮廓系数和CH指数的影响            'composite': 0.4 * sil_score + 0.6 * (ch_score / 100000)        })    # 转换为DataFrame方便排序    score_df = pd.DataFrame(scores)    # 按综合得分降序排序，取第一个作为最佳聚类数    best_k = score_df.sort_values('composite', ascending=False)['k'].iloc[0]    # 兜底：确保聚类数在合理范围    best_k = max(min_clusters, min(best_k, max_clusters))    return best_kdef cluster_alphas_improved(alpha_metrics, use_pca=True, cluster_algorithm='kmeans'):    """    改进的聚类逻辑：支持PCA降维、多种聚类算法、多指标确定聚类数    :param alpha_metrics: alpha的指标数据    :param use_pca: 是否使用PCA降维（处理特征冗余）    :param cluster_algorithm: 聚类算法（kmeans/agglomerative/dbscan）    :return: 选中的alpha列表（每个聚类fitness最大）    """    # 转换为DataFrame方便处理    df = pd.DataFrame(alpha_metrics)    # 定义用于聚类的特征列    feature_cols = ['longCount', 'shortCount', 'turnover', 'returns', 'drawdown', 'margin', 'sharpe']    # 提取特征数据，处理缺失值（填充0）    X = df[feature_cols].fillna(0).values    # 改进1：使用RobustScaler标准化（抗异常值，比StandardScaler更适合金融数据）    scaler = RobustScaler()  # 替代StandardScaler，对异常值不敏感    X_scaled = scaler.fit_transform(X)    # 改进2：PCA降维（处理特征冗余，减少噪声）    if use_pca and len(feature_cols) > 2:        # 保留95%的方差，自动确定降维后的维度        pca = PCA(n_components=0.95, random_state=42)        X_processed = pca.fit_transform(X_scaled)        print(f"PCA降维后，特征维度从{len(feature_cols)}变为{X_processed.shape[1]}")    else:        X_processed = X_scaled    # 改进3：多指标确定聚类数（避免聚类数过少）    best_k = determine_clusters_multi_criteria(X_processed, min_clusters=5, max_clusters=50)    print(f"改进后确定的最佳聚类数量：{best_k}")    # 改进4：支持多种聚类算法（KMeans/层次聚类/DBSCAN）    if cluster_algorithm == 'kmeans':        # KMeans：适合球形分布，速度快        cluster_model = KMeans(n_clusters=best_k, random_state=42, n_init='auto')        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'agglomerative':        # 层次聚类：不假设球形分布，更灵活        cluster_model = AgglomerativeClustering(n_clusters=best_k)        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'dbscan':        # DBSCAN：无需指定聚类数，自动识别密度聚类（适合非球形分布）        # eps和min_samples可调整：eps越大，聚类数越少；min_samples越大，聚类数越多        cluster_model = DBSCAN(eps=0.5, min_samples=5)        df['cluster'] = cluster_model.fit_predict(X_processed)        # DBSCAN的-1表示噪声点，单独处理为一个聚类        noise_cluster = df['cluster'].max() + 1        df.loc[df['cluster'] == -1, 'cluster'] = noise_cluster        best_k = len(df['cluster'].unique())        print(f"DBSCAN聚类后实际聚类数量：{best_k}")    # 每个聚类中选择fitness最大的alpha    selected_alphas = []    for cluster in df['cluster'].unique():        cluster_df = df[df['cluster'] == cluster]        # 取fitness最大的行        best_alpha = cluster_df.loc[cluster_df['fitness'].idxmax()]        selected_alphas.append(best_alpha.to_dict())    return selected_alphas# In[4]:# ===================================================================# PART 3: 主逻辑 (先清除该地区，再赋值)# ===================================================================if __name__ == '__main__':    # 1. 基础配置    target_region = "USA"     advisor_date_obj = datetime(2025, 12, 10)    advisor_date_str = advisor_date_obj.strftime("%Y-%m-%d")    page_limit = 100  # 每页获取的alpha数量    page_offset = 0   # 分页起始偏移量    session = start_session()    # --- A. 清除该地区既有分数 ---    # 计算日期范围 (参考你清除脚本的逻辑)    begin_date = advisor_date_str    end_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")    print(f"正在清除地区 {target_region} 在 {begin_date} 之后的既有分数...")    alphas_to_clear = get_colored_alphas_in_date_range(session, begin_date, end_date, target_region)    if alphas_to_clear:        with ThreadPoolExecutor(max_workers=10) as executor:            for alpha_data in alphas_to_clear:                executor.submit(up_alpha_properties_to_clear, session, alpha_data["id"], alpha_data["osmosisPoints"])    else:        print("未找到需要清除分数的 Alpha。")    # 获取alpha的指标数据    alpha_metrics_list = get_history_alpha_ids(        s=session,        region=target_region,        start_date=advisor_date_obj,        limit=page_limit,        offset=page_offset,        #exclude_tags=["TEST"],         exclude_color='RED'    )    # 校验数据是否有效    if not alpha_metrics_list:        print("程序终止：未获取到有效alpha数据")        exit(1)    # 执行聚类并选择每个类别中fitness最大的alpha    selected_alpha_list = cluster_alphas_improved(        alpha_metrics=alpha_metrics_list,        use_pca=True,        cluster_algorithm='kmeans'    )    # 校验聚类结果    if not selected_alpha_list:        print("程序终止：聚类后未选中任何alpha")        exit(1)# In[5]:# --- 1. 获取聚类领头羊 ---# selected_alpha_list 已经是每个聚类里 fitness 最大的一个selected_ids = {a['id'] for a in selected_alpha_list}# --- 2. 补齐逻辑：如果不足 10 类，从备选池里抓取 ---target_count = 10current_count = len(selected_alpha_list)if current_count < target_count:    # 找出那些没被选中的因子    remaining_alphas = [a for a in alpha_metrics_list if a['id'] not in selected_ids]    # 按 Fitness 排序，选出表现较好的作为凑数因子    remaining_alphas.sort(key=lambda x: x['fitness'], reverse=True)    # 计算需要补多少个    needed = target_count - current_count    # 注意：补齐数量不能超过备选池总数    fillers = remaining_alphas[:needed]    for f in fillers:        f['cluster'] = 'filler'  # 标记为凑数        selected_alpha_list.append(f)# 更新当前最终选中的数量final_selected_count = len(selected_alpha_list)print(f"最终入选因子数：{final_selected_count} (其中聚类领头羊：{current_count}，凑数因子：{final_selected_count - current_count})")# --- 3. 分数分配逻辑 ---# 分成两拨处理：核心因子 vs 凑数因子leaders = [a for a in selected_alpha_list if a['cluster'] != 'filler']fillers = [a for a in selected_alpha_list if a['cluster'] == 'filler']# 凑数因子总分 = 数量 * 1分filler_total_points = len(fillers)# 核心因子总分 = 100,000 - 凑数分leader_pool_points = 100000 - filler_total_points# 核心因子基础分（平分池子）leader_base_score = leader_pool_points // len(leaders)leader_remainder = leader_pool_points % len(leaders)# --- 4. 执行 API 更新 ---total_check = 0for i, alpha_info in enumerate(selected_alpha_list):    alpha_id = alpha_info['id']    # 判断分数    if alpha_info['cluster'] == 'filler':        final_score = 1    else:        # 如果是核心因子中的第一个，拿走余数        if alpha_id == leaders[0]['id']:            final_score = leader_base_score + leader_remainder        else:            final_score = leader_base_score    print(f"Alpha {alpha_id} | Fitness值：{alpha_info['fitness']} | 类型: {alpha_info['cluster']} | 分配分数: {final_score}")    # 执行更新    update_url = f"[链接已屏蔽]    session.patch(update_url, json={"osmosisPoints": final_score}) # 确认无误后再取消注释    total_check += final_scoreprint(f"\n分配总计：{total_check} 分 (目标 100,000)")
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享

这套方案非常靠谱了  这就用起来

=============================================================================


---

### 技术对话片段 49 (原帖: 【own sa】一种根据使用频率进行select的方法)
- **原帖链接**: [Commented] 【own sa】一种根据使用频率进行select的方法.md
- **时间**: 8个月前

**提问/主帖背景 (DQ66419)**:
以下近2个月自用的一套own sa的select方法，目的是在保证sharpe和fitness>5的基础上，方便做出更多的own sa，甚至pc0.5以下的因子。

大家如果有瓶颈，不妨尝试下。如有雷同，纯属巧合。

先看下2个月的基本情况，我基本上是隔天做一个own sa。根据柱子的长短，可以看出部分own sa是满足35要求的。
 [图片 (图片已丢失)] 
下面是select的方法：
1、准备工作：把自己交过的RA\PPA筛选一遍，保留自己认为质量较好的且self corr在0.5以下的因子（这里并不关心prod_corr），进行favorite打标。这一步是保证sa的质量及低相似度的基础。
2、选择本次需要select的RA进行GREEN标记，具体代码在最下面。大致逻辑是，本次需要select的ra(比如30个)，被使用过的次数要尽可能的低，并且至少要有一部分因子(比如10个)是跟之前own sa不一样的。
3、固定使用这个selection expression来跑。limit数量根据第2个步自己想选择的数量设置。

```
own&&favorite&&color=="GREEN"
```

4、risk neut比较容易低corr，所以我一般只遍历这几个risk neut。
5、combo我没有什么特别的，都是之前游戏王等大佬们分享的技巧。
6、回测并check prod corr。如果本身自己的ra质量不高，可以考虑多select几个。

以下是select并打GREEN标识的代码，本人代码基础不好，仅供参考：

```
import asynciofrom collections import Counterfrom wqb import printimport src.common.common as commonregion = 'EUR'select_count = 35    #sa需要的ra个数diff_count = 10  #与已提交过的sa不重复的ra个数'''查询已提交过的own sa所select的ra'''wqbs = common.login(f'{common.get_file_name(__file__)}')submitted_alphas = wqbs.filter_alphas(    others=['status!=UNSUBMITTED%1FIS-FAIL'],    order='-dateSubmitted',    type='SUPER',    region=region,)saList = []for resp in submitted_alphas:    saList.extend(resp.json()['results'])selectedRaList = []for sa in saList:    if 'not(own)' in sa['selection']['code']:        continue    raList = asyncio.run(common.list_ra_of_sa(wqbs, sa['id']))    selectedRaList.append([ra['id'] for ra in raList])'''取出所有favorite的ra'''regular_alphas = wqbs.filter_alphas(    others=['status!=UNSUBMITTED%1FIS-FAIL'],    order='-dateSubmitted',    type='REGULAR',    favorite='true',    region=region,)favoriteRaList = []for resp in regular_alphas:    favoriteRaList.extend(ra['id'] for ra in resp.json()['results'])'''选择ra'''# 统计 selectedRaList 中每个id的出现频率all_id_in_selectedRaList = [id for row in selectedRaList for id in row]frequency = Counter(all_id_in_selectedRaList)# 对favoriteRaList 按频率升序排序（出现次数少的优先）sorted_favoriteRaList = sorted(favoriteRaList, key=lambda x: frequency.get(x, 0))selected = []  # 最终选中的for id in sorted_favoriteRaList:    if len(selected) >= select_count:        break    trial_selected = selected + [id]    valid = True    for row in selectedRaList:        row_set = set(row)        trial_set = set(trial_selected)        intersection_size = len(row_set & trial_set)        max_allowed_intersection = len(row) - diff_count        if max_allowed_intersection < 0:            continue        if intersection_size > max_allowed_intersection:            valid = False            break    if valid:        selected.append(id)    if len(selected) == select_count:        breakif len(selected) < select_count:    print(f"警告：只选出了 {len(selected)} 个，未能达到 {select_count} 个。")else:    print(selected)    '''颜色标记'''    for ra in favoriteRaList:        wqbs.patch_properties(alpha_id=ra, color='BLUE')    for ra in selected:        wqbs.patch_properties(alpha_id=ra, color='GREEN')
```

```
async def list_ra_of_sa(self, alpha_id):    resp = await self.retry(        'GET', wqb_urls.URL_ALPHAS + f'/{alpha_id}/alphas?limit=100&offset=0&status=ACTIVE%1DECOMMISSIONED', max_tries=600    )    return resp.json()['results']
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=======================================

感谢大佬分享，虽然我目前交的alpha数量不多还不太能产出SA，但技巧先码住了哈哈，希望到时候也能拿到大佬这种base

=================================================================================


---

### 技术对话片段 50 (原帖: 【own sa】一种根据使用频率进行select的方法)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【own sa】一种根据使用频率进行select的方法_35157464669847.md
- **时间**: 8个月前

**提问/主帖背景 (DQ66419)**:
以下近2个月自用的一套own sa的select方法，目的是在保证sharpe和fitness>5的基础上，方便做出更多的own sa，甚至pc0.5以下的因子。

大家如果有瓶颈，不妨尝试下。如有雷同，纯属巧合。

先看下2个月的基本情况，我基本上是隔天做一个own sa。根据柱子的长短，可以看出部分own sa是满足35要求的。
 [图片 (图片已丢失)] 
下面是select的方法：
1、准备工作：把自己交过的RA\PPA筛选一遍，保留自己认为质量较好的且self corr在0.5以下的因子（这里并不关心prod_corr），进行favorite打标。这一步是保证sa的质量及低相似度的基础。
2、选择本次需要select的RA进行GREEN标记，具体代码在最下面。大致逻辑是，本次需要select的ra(比如30个)，被使用过的次数要尽可能的低，并且至少要有一部分因子(比如10个)是跟之前own sa不一样的。
3、固定使用这个selection expression来跑。limit数量根据第2个步自己想选择的数量设置。

```
own&&favorite&&color=="GREEN"
```

4、risk neut比较容易低corr，所以我一般只遍历这几个risk neut。
5、combo我没有什么特别的，都是之前游戏王等大佬们分享的技巧。
6、回测并check prod corr。如果本身自己的ra质量不高，可以考虑多select几个。

以下是select并打GREEN标识的代码，本人代码基础不好，仅供参考：

```
import asynciofrom collections import Counterfrom wqb import printimport src.common.common as commonregion = 'EUR'select_count = 35    #sa需要的ra个数diff_count = 10  #与已提交过的sa不重复的ra个数'''查询已提交过的own sa所select的ra'''wqbs = common.login(f'{common.get_file_name(__file__)}')submitted_alphas = wqbs.filter_alphas(    others=['status!=UNSUBMITTED%1FIS-FAIL'],    order='-dateSubmitted',    type='SUPER',    region=region,)saList = []for resp in submitted_alphas:    saList.extend(resp.json()['results'])selectedRaList = []for sa in saList:    if 'not(own)' in sa['selection']['code']:        continue    raList = asyncio.run(common.list_ra_of_sa(wqbs, sa['id']))    selectedRaList.append([ra['id'] for ra in raList])'''取出所有favorite的ra'''regular_alphas = wqbs.filter_alphas(    others=['status!=UNSUBMITTED%1FIS-FAIL'],    order='-dateSubmitted',    type='REGULAR',    favorite='true',    region=region,)favoriteRaList = []for resp in regular_alphas:    favoriteRaList.extend(ra['id'] for ra in resp.json()['results'])'''选择ra'''# 统计 selectedRaList 中每个id的出现频率all_id_in_selectedRaList = [id for row in selectedRaList for id in row]frequency = Counter(all_id_in_selectedRaList)# 对favoriteRaList 按频率升序排序（出现次数少的优先）sorted_favoriteRaList = sorted(favoriteRaList, key=lambda x: frequency.get(x, 0))selected = []  # 最终选中的for id in sorted_favoriteRaList:    if len(selected) >= select_count:        break    trial_selected = selected + [id]    valid = True    for row in selectedRaList:        row_set = set(row)        trial_set = set(trial_selected)        intersection_size = len(row_set & trial_set)        max_allowed_intersection = len(row) - diff_count        if max_allowed_intersection < 0:            continue        if intersection_size > max_allowed_intersection:            valid = False            break    if valid:        selected.append(id)    if len(selected) == select_count:        breakif len(selected) < select_count:    print(f"警告：只选出了 {len(selected)} 个，未能达到 {select_count} 个。")else:    print(selected)    '''颜色标记'''    for ra in favoriteRaList:        wqbs.patch_properties(alpha_id=ra, color='BLUE')    for ra in selected:        wqbs.patch_properties(alpha_id=ra, color='GREEN')
```

```
async def list_ra_of_sa(self, alpha_id):    resp = await self.retry(        'GET', wqb_urls.URL_ALPHAS + f'/{alpha_id}/alphas?limit=100&offset=0&status=ACTIVE%1DECOMMISSIONED', max_tries=600    )    return resp.json()['results']
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=======================================

感谢大佬分享，虽然我目前交的alpha数量不多还不太能产出SA，但技巧先码住了哈哈，希望到时候也能拿到大佬这种base

=================================================================================


---

### 技术对话片段 51 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【Quant101】AIAC20 TOP25 经验分享经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (ZH87224)**:
AIAC2.0 Final Round 应该是出来了，预计下次全球大会时会公布结果，有幸拿到TOP25，跟大家分享一些我的经验。

我的主要方案在比赛中打造出来，后续一直持续使用，是我目前点塔的主要流程。我的方案是结合了几次AI培训课程的内容，包括GEM和来点灵感，在此基础之上我本人也做了一点微小的工作：数据集压缩。

整套方案在分析数据集时，需要读入整个数据集，看过代码的小伙伴都知道，如果数据集很大的情况下，实际上只会读取TOP-N条数据，这显然会丢失很多信息。

众所周知，Brain平台的数据集字段的命名实际上是有明显业务含义和规律的，一般来说符合以下格式：

[数据集id]_[经济学指标]_[时间周期]_[无含义后缀]

所以我们可以在最开始，执行一步数据集压缩，将整个数据集所有的字段都归纳为特定的模式（类似正则表达式），这样可以极大压缩信息量，也使得大模型更聚焦，更能精准结合数据集字段的经济学含义。

下面是我用的Prompt，供大家参考：

```
你是一位专业的投资经理和数据架构师，你的任务是以某数据集为核心构造搭建投资因子库。你需要分析数据集中的字段命名规律，将其归纳为通用的正则表达式模式。例如：pv87 数据集字段模式示例：```pv87_2_[indicator]_[freq]_matrix_[scope]_[metric]_[stat]```其中：- indicator: affops, bps, capex, cfps, csh, dps 等财务指标- freq: af (Annual), qf (Quarterly) 等频率标识- scope: all, p1, p1_b 等数据范围- metric: null (原始值), chngratio (变化率) 等数据类型- stat: high, low, mean, median, dts, number, std 等统计量请基于字段的**经济学含义**和**命名构成模式**，分析归纳其中的规律。**重要规则**:1. 每组正则表达式必须**互斥**(一个字段只能匹配一个regex)2. 如果新规律能与已有规律合并，请合并后输出（优化通用性）3. 特殊字段(Special)是那些不符合任何通用模式的字段4. 正则表达式必须足够精确，避免过度匹配5. 不可以使用通配符代表有经济含义指标，例如不可以使用[a-z0-9]+来表示财务指标、频率等内容，必须使用或"|"来枚举所有经济对象
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

这个数据集压缩的小技巧学到了

感谢大佬的无私分享！

=============================================================================


---

### 技术对话片段 52 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Quant101】AIAC20 TOP25 经验分享经验分享_39234849586967.md
- **时间**: 2个月前

**提问/主帖背景 (ZH87224)**:
AIAC2.0 Final Round 应该是出来了，预计下次全球大会时会公布结果，有幸拿到TOP25，跟大家分享一些我的经验。

我的主要方案在比赛中打造出来，后续一直持续使用，是我目前点塔的主要流程。我的方案是结合了几次AI培训课程的内容，包括GEM和来点灵感，在此基础之上我本人也做了一点微小的工作：数据集压缩。

整套方案在分析数据集时，需要读入整个数据集，看过代码的小伙伴都知道，如果数据集很大的情况下，实际上只会读取TOP-N条数据，这显然会丢失很多信息。

众所周知，Brain平台的数据集字段的命名实际上是有明显业务含义和规律的，一般来说符合以下格式：

[数据集id]_[经济学指标]_[时间周期]_[无含义后缀]

所以我们可以在最开始，执行一步数据集压缩，将整个数据集所有的字段都归纳为特定的模式（类似正则表达式），这样可以极大压缩信息量，也使得大模型更聚焦，更能精准结合数据集字段的经济学含义。

下面是我用的Prompt，供大家参考：

```
你是一位专业的投资经理和数据架构师，你的任务是以某数据集为核心构造搭建投资因子库。你需要分析数据集中的字段命名规律，将其归纳为通用的正则表达式模式。例如：pv87 数据集字段模式示例：```pv87_2_[indicator]_[freq]_matrix_[scope]_[metric]_[stat]```其中：- indicator: affops, bps, capex, cfps, csh, dps 等财务指标- freq: af (Annual), qf (Quarterly) 等频率标识- scope: all, p1, p1_b 等数据范围- metric: null (原始值), chngratio (变化率) 等数据类型- stat: high, low, mean, median, dts, number, std 等统计量请基于字段的**经济学含义**和**命名构成模式**，分析归纳其中的规律。**重要规则**:1. 每组正则表达式必须**互斥**(一个字段只能匹配一个regex)2. 如果新规律能与已有规律合并，请合并后输出（优化通用性）3. 特殊字段(Special)是那些不符合任何通用模式的字段4. 正则表达式必须足够精确，避免过度匹配5. 不可以使用通配符代表有经济含义指标，例如不可以使用[a-z0-9]+来表示财务指标、频率等内容，必须使用或"|"来枚举所有经济对象
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

这个数据集压缩的小技巧学到了

感谢大佬的无私分享！

=============================================================================


---

### 技术对话片段 53 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【TOKEN王】全球 2026Q2 geniusLevel 分组六维数据统计分析经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (SC77987)**:
2026Q1季度已经完成了定级，在4月1日，由华子哥的插件可以看到，三个等级的满足要求人数都超出了上限，master和expert的竞争极为激烈（后续4月9日combine更新后人数发生了变化，但是变化不大），因此六纬对于genius定级愈发重要，本文旨在分析2026Q1的gm、m、e的六维数据以帮助顾问们在这个季度有更明确的努力方向。 
> [!NOTE] [图片 OCR 识别内容]
> 各个Level 满足的人数 /最终的人数:
> For Expert: 1357
> 675
> For Master: 535
> 250
> For Grandmaster: 90/73


一、三大硬指标&六维分析

```
1、Alpha数量和金字塔数量
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> Alpha数量
> 275.96
> 269
> 227.104
> 222.0
> 176.523
> 169
> 金字塔数量
> 60.96
> 60
> 41.22
> 33.0
> 26.7481
> 29


```
2、Combine表现
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> PowerPool表现
> 1.718
> 1.98
> 1.0326
> 1.17
> 0.4352
> 0.55
  
> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 综合Alpha表现
> 2.0585
> 2.16
> 1.4016
> 1.41
> 0.816
> 0.8



> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> Selected Alpha表现
> 1.0705
> 1.06
> 0.3331
> 0.18
> 0.0944
> 0.0



> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> Osmosis表现
> -0.2433
> -0.23
> -0.4722
> 0.0
> -0.2703
> 0.0


```
3、操作符数量和字段数量
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 操作符数量
> 125.48
> 132
> 102.352
> 105.5
> 56.8548
> 48
> 字段数量
> 248.0533
> 230
> 211.924
> 190.0
> 143.683
> 122


```
4、平均操作符数量和平均字段数量
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 每个Alpha操作符均值
> 4.5815
> 4.44
> 4.3614
> 4.215
> 4.723
> 4.68
> 每个Alpha字段均值
> 1.7105
> 1.46
> 1.8684
> 1.66
> 1.842
> 1.66


```
5、社区活跃度和最大回测天数
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 社区活跃度
> 49.5627
> 49.4
> 43.4924
> 43.8
> 24.4668
> 24.2
> 最大连续回测天数
> 405.8267
> 403
> 361.96
> 346.5
> 255.4044
> 239


二、2025Q4 与 2026Q1对比

```
1、下面的矩阵表示用户从 2025Q4 到 2026Q1 的层级迁移情况
```


> [!NOTE] [图片 OCR 识别内容]
> 上一季度1下一季度
> GRANDMASTER
> MASTER
> EXPERT
> GOLD
> NIA
> GRANDMASTER
> 49
> 18
> 5
> 3
> MASTER
> 19
> 147
> 71
> 10
> EXPERT
> 5
> 71
> 346
> 241
> GOLD
> 2
> 14
> 253
> 9732
> 3
> NIA
> 0
> 0
> 18


```
2、三大硬指标&六维对比
```

感谢JX哥，2025Q4数据来源于

[../顾问 JX79797 (Rank 9)/[四季度六维数据] 聚焦目标数据超越自我.md](../顾问 JX79797 (Rank 9)/[四季度六维数据] 聚焦目标数据超越自我.md)


> [!NOTE] [图片 OCR 识别内容]
> 指标
> 层级
> 帖子均值
> 本次均值
> 均值差
> 帖子中位数
> 本次中位数
> 中位数差
> Alpha数量
> GRANDMASTER
> 318.36
> 275.96
> -42.4
> 302
> 269
> -33
> Alpha数量
> MASTER
> 256.52
> 227.104
> -29.416
> 246
> 222.0
> -24.0
> Alpha数量
> EXPERT
> 206.69
> 176.523
> -30.167
> 196
> 169
> -27
> 金字塔数量
> GRANDMASTER
> 61.4
> 60.96
> -0.44
> 60
> 60
> 金字塔数量
> MASTER
> 46.0
> 41.22
> -4.78
> 41
> 33.0
> -8.0
> 金字塔数量
> EXPERT
> 30.97
> 26.7481
> -4.2219
> 31
> 29
> 综合Alpha表现
> GRANDMASTER
> 2.12
> 2.0585
> -0.0615
> 2.14
> 2.16
> 0.02
> 综合Alpha表现
> MASTER
> 1.45
> 1.4016
> -0.0484
> 1.43
> 1.41
> -0.02
> 综合Alpha表现
> EXPERT
> 0.93
> 0.816
> -0.114
> 0.9
> 0.8
> -0.1



> [!NOTE] [图片 OCR 识别内容]
> 指标
> 层级
> 帖子均值
> 本次均值
> 均值差
> 帖子中位数
> 本次中位数
> 中位数差
> PowerPool表现
> GRANDMASTER
> 1.63
> 1.718
> 0.088
> 1.82
> 1.98
> 0.16
> PowerPool表现
> MASTER
> 0.95
> 1.0326
> 0.0826
> 1.1
> 1.17
> 0.07
> PowerPool表现
> EXPERT
> 0.51
> 0.4352
> -0.0748
> 0.61
> 0.55
> -0.06
> 操作符数量
> GRANDMASTER
> 132.64
> 125.48
> -7.16
> 134
> 132
> -2
> 操作符数量
> MASTER
> 100.74
> 102.352
> 1.612
> 101.5
> 105.5
> 4.0
> 操作符数量
> EXPERT
> 56.87
> 56.8548
> -0.0152
> 53
> 48
> -5
> 字段数量
> GRANDMASTER
> 275.09
> 248.0533
> -27.0367
> 249
> 230
> -19
> 字段数量
> MASTER
> 243.38
> 211.924
> -31.456
> 233
> 190.0
> 43.0
> 字段数量
> EXPERT
> 173.42
> 143.683
> -29.737
> 161
> 122
> -39
> 每个 Alpha操作符均值
> GRANDMASTER
> 4.19
> 4.5815
> 0.3915
> 4.14
> 4.44
> 0.3
> 每个 Alpha操作符均值
> MASTER
> 3.92
> 4.3614
> 0.4414
> 3.81
> 4.215
> 0.405
> 每个 Alpha操作符均值
> EXPERT
> 4.63
> 4.723
> 0.093
> 4.55
> 4.68
> 0.13
> 每个 Alpha字段均值
> GRANDMASTER
> 1.57
> 1.7105
> 0.1405
> 1.33
> 1.46
> 0.13
> 每个 Alpha字段均值
> MASTER
> 1.73
> 1.8684
> 0.1384
> 1.5
> 1.66
> 0.16
> 每个 Alpha字段均值
> EXPERT
> 1.86
> 1.842
> -0.018
> 1.69
> 1.66
> -0.03


祝大家在新赛季base高高，VF1，genius高高，继续壮大国区～

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！GM的平均实力好强！

这赛季继续努力！

=============================================================================


---

### 技术对话片段 54 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【TOKEN王】全球 2026Q2 geniusLevel 分组六维数据统计分析经验分享_39756841978519.md
- **时间**: 2个月前

**提问/主帖背景 (SC77987)**:
2026Q1季度已经完成了定级，在4月1日，由华子哥的插件可以看到，三个等级的满足要求人数都超出了上限，master和expert的竞争极为激烈（后续4月9日combine更新后人数发生了变化，但是变化不大），因此六纬对于genius定级愈发重要，本文旨在分析2026Q1的gm、m、e的六维数据以帮助顾问们在这个季度有更明确的努力方向。 
> [!NOTE] [图片 OCR 识别内容]
> 各个Level 满足的人数 /最终的人数:
> For Expert: 1357
> 675
> For Master: 535
> 250
> For Grandmaster: 90/73


一、三大硬指标&六维分析

```
1、Alpha数量和金字塔数量
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> Alpha数量
> 275.96
> 269
> 227.104
> 222.0
> 176.523
> 169
> 金字塔数量
> 60.96
> 60
> 41.22
> 33.0
> 26.7481
> 29


```
2、Combine表现
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> PowerPool表现
> 1.718
> 1.98
> 1.0326
> 1.17
> 0.4352
> 0.55
  
> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 综合Alpha表现
> 2.0585
> 2.16
> 1.4016
> 1.41
> 0.816
> 0.8



> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> Selected Alpha表现
> 1.0705
> 1.06
> 0.3331
> 0.18
> 0.0944
> 0.0



> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> Osmosis表现
> -0.2433
> -0.23
> -0.4722
> 0.0
> -0.2703
> 0.0


```
3、操作符数量和字段数量
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 操作符数量
> 125.48
> 132
> 102.352
> 105.5
> 56.8548
> 48
> 字段数量
> 248.0533
> 230
> 211.924
> 190.0
> 143.683
> 122


```
4、平均操作符数量和平均字段数量
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 每个Alpha操作符均值
> 4.5815
> 4.44
> 4.3614
> 4.215
> 4.723
> 4.68
> 每个Alpha字段均值
> 1.7105
> 1.46
> 1.8684
> 1.66
> 1.842
> 1.66


```
5、社区活跃度和最大回测天数
```


> [!NOTE] [图片 OCR 识别内容]
> 指标
> Grandmaster
> 均值 )
> Grandmaster
> 中位数 )
> Master
> 均值 )
> Master
> 中位数 )
> Expert
> 均值 )
> Expert
> 中位数 )
> 社区活跃度
> 49.5627
> 49.4
> 43.4924
> 43.8
> 24.4668
> 24.2
> 最大连续回测天数
> 405.8267
> 403
> 361.96
> 346.5
> 255.4044
> 239


二、2025Q4 与 2026Q1对比

```
1、下面的矩阵表示用户从 2025Q4 到 2026Q1 的层级迁移情况
```


> [!NOTE] [图片 OCR 识别内容]
> 上一季度1下一季度
> GRANDMASTER
> MASTER
> EXPERT
> GOLD
> NIA
> GRANDMASTER
> 49
> 18
> 5
> 3
> MASTER
> 19
> 147
> 71
> 10
> EXPERT
> 5
> 71
> 346
> 241
> GOLD
> 2
> 14
> 253
> 9732
> 3
> NIA
> 0
> 0
> 18


```
2、三大硬指标&六维对比
```

感谢JX哥，2025Q4数据来源于

[[L2] [四季度六维数据] 聚焦目标数据超越自我_37660909564311.md]([L2] [四季度六维数据] 聚焦目标数据超越自我_37660909564311.md)


> [!NOTE] [图片 OCR 识别内容]
> 指标
> 层级
> 帖子均值
> 本次均值
> 均值差
> 帖子中位数
> 本次中位数
> 中位数差
> Alpha数量
> GRANDMASTER
> 318.36
> 275.96
> -42.4
> 302
> 269
> -33
> Alpha数量
> MASTER
> 256.52
> 227.104
> -29.416
> 246
> 222.0
> -24.0
> Alpha数量
> EXPERT
> 206.69
> 176.523
> -30.167
> 196
> 169
> -27
> 金字塔数量
> GRANDMASTER
> 61.4
> 60.96
> -0.44
> 60
> 60
> 金字塔数量
> MASTER
> 46.0
> 41.22
> -4.78
> 41
> 33.0
> -8.0
> 金字塔数量
> EXPERT
> 30.97
> 26.7481
> -4.2219
> 31
> 29
> 综合Alpha表现
> GRANDMASTER
> 2.12
> 2.0585
> -0.0615
> 2.14
> 2.16
> 0.02
> 综合Alpha表现
> MASTER
> 1.45
> 1.4016
> -0.0484
> 1.43
> 1.41
> -0.02
> 综合Alpha表现
> EXPERT
> 0.93
> 0.816
> -0.114
> 0.9
> 0.8
> -0.1



> [!NOTE] [图片 OCR 识别内容]
> 指标
> 层级
> 帖子均值
> 本次均值
> 均值差
> 帖子中位数
> 本次中位数
> 中位数差
> PowerPool表现
> GRANDMASTER
> 1.63
> 1.718
> 0.088
> 1.82
> 1.98
> 0.16
> PowerPool表现
> MASTER
> 0.95
> 1.0326
> 0.0826
> 1.1
> 1.17
> 0.07
> PowerPool表现
> EXPERT
> 0.51
> 0.4352
> -0.0748
> 0.61
> 0.55
> -0.06
> 操作符数量
> GRANDMASTER
> 132.64
> 125.48
> -7.16
> 134
> 132
> -2
> 操作符数量
> MASTER
> 100.74
> 102.352
> 1.612
> 101.5
> 105.5
> 4.0
> 操作符数量
> EXPERT
> 56.87
> 56.8548
> -0.0152
> 53
> 48
> -5
> 字段数量
> GRANDMASTER
> 275.09
> 248.0533
> -27.0367
> 249
> 230
> -19
> 字段数量
> MASTER
> 243.38
> 211.924
> -31.456
> 233
> 190.0
> 43.0
> 字段数量
> EXPERT
> 173.42
> 143.683
> -29.737
> 161
> 122
> -39
> 每个 Alpha操作符均值
> GRANDMASTER
> 4.19
> 4.5815
> 0.3915
> 4.14
> 4.44
> 0.3
> 每个 Alpha操作符均值
> MASTER
> 3.92
> 4.3614
> 0.4414
> 3.81
> 4.215
> 0.405
> 每个 Alpha操作符均值
> EXPERT
> 4.63
> 4.723
> 0.093
> 4.55
> 4.68
> 0.13
> 每个 Alpha字段均值
> GRANDMASTER
> 1.57
> 1.7105
> 0.1405
> 1.33
> 1.46
> 0.13
> 每个 Alpha字段均值
> MASTER
> 1.73
> 1.8684
> 0.1384
> 1.5
> 1.66
> 0.16
> 每个 Alpha字段均值
> EXPERT
> 1.86
> 1.842
> -0.018
> 1.69
> 1.66
> -0.03


祝大家在新赛季base高高，VF1，genius高高，继续壮大国区～

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！GM的平均实力好强！

这赛季继续努力！

=============================================================================


---

### 技术对话片段 55 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【ValueFactor】关于近几次Value Factor更新后暂时仍保持097以上的一些思考与分享经验分享.md
- **时间**: 5个月前

**提问/主帖背景 (XW85841)**:
老规矩，无图无真相，先上图：


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025/5/24
> 2025/6/28
> 2025/7/20
> 2025/8/19
> 2025/9/20
> 2025/10/25
> 2025/11/21
> 2025/12/16
> Value Factor
> 0.74
> 0.59
> 0.94
> 0.95
> 0.97
> 0.99
> 0.97
> 0.97
> 2025.1.1
> 2025.2.1
> 2025.3.1
> 2025.1.1 
> 2025.5.1
> 2025.6.1 
> 2025.7.1
> 2025.8.1 
> Time period
> 2025.3.31
> 2025.4.30
> 2025.5.31
> 2025.6.30
> 2025.7.31
> 2025.8.31
> 2025.9.30
> 2025.10.31
> 说明
> 更新
> 更新
> 更新
> 更新
> 更新
> 更新
> 更新


可以看出，进入7月份以后，我的ValueFator数值基本上维持在0.9以上，并且从0.94一度上涨至0.99，最近两次更新之后也维持在0.97，还算是比较稳定、也算是中高位区间的分位段。对于我个人来说，从趋势上来看算是较为稳定的，并且一度在10月份的时候达到了0.99，虽然没有突破1.0的极限，但是对于没有任何量化、金融/股票、代码功底的我来说，个人还算是很满意的！

对于目前较为稳定的高VF的情况，我通过简要的回顾和分析（由于代码功底限制，无法通过代码进行定量和精准的分析，还请见谅），大概有以下几点原因，供大家批评指正，其中可取之处也希望能帮助到有需要的同志。
 **【1、坚持做SA】**

这是最为关键的核心点之一。之前已经有不少同志们提到了这一点，通过我的亲身经历的反馈，这个对于维持VF是至关重要的一个影响因素！在这里继续建议，无论当期的VF是高还是低，都建议坚持每天提交一个质量还可以的SA，可以不要求是35，但是起码fitness\sharpe\margin还是需要维持在较高的指标再去提交；不建议为了交SA而交SA，目标还是要优化该地区的总体指标。

**【2、坚持做四大地区+D1】**

我之前写过一篇帖子，主要是分享踩过的坑，里面就讨论过这一条。因为我之前因为没有人指导和提醒，提交了若干个小地区的因子，导致VF在5月份之前一直处于低水位的水平，直接影响了每天的BASE；后面就只做四大区域：USA\EUR\GLB\ASI，从VF变化反馈来看，这个选择和坚持是极为正确的！同时由于本人水平所限，一直不敢碰D0、也不敢碰CHN，但是四大区域对于维持Master的等级所需要的塔已经基本上够了！

帖子链接如下：
 [../顾问 FD69320 (Rank 34)/[Commented] 【避坑】一个龟速上升但仍坚持前行的老新手顾问踩过的一些坑经验分享.md](../顾问 FD69320 (Rank 34)/[Commented] 【避坑】一个龟速上升但仍坚持前行的老新手顾问踩过的一些坑经验分享.md)

**【3、提交regluar alpha数量保持稳定】**

从10月份VF从0.99降到11月的0.97、然后12月份仍然维持在0.97，通过我的简单分析，发现了应该是提交数量的震荡产生了影响：由于Q3点塔相对顺利，所以在9月份放松了一下，提交的数量只有7、8月份平均的70%左右的水平，这个直接就在11月份VF更新的时候反应了，同时这个因素也直接影响了12月份的VF，虽然数字上维持了0.97没有变化，但是主要还是8月份的正向影响保住了这个水平。同时反观7、8、9这三个月VF的正向趋势变化，也与6、7、8这三个月为了能够在Q3维持Master的段位而持续努力，提交的因子数量基本上自稳定略增加，也间接印证了我的判断。

同时，如果1月份再更新VF的时候，如果VF继续下降，那么就基本上可以再次印证了我的猜测——因为8月份的影响周期已结束了，9月少、10月更少；但是11月份数量赶了上来，希望能有所抵消9、10月份提交数量下降较多而导致的负面影响。

**【4、保证质量提交底线】**

通过与其他VF变动较大的同志们的聊天，不少VF急剧下跌的基本上都是为了点塔而提交了不少指标一般的因子！也就是我前面那个帖子里我自己踩过的坑——绿了就提交！这是坚持不建议的提交方式！如果想让自己的VF不骤降，仍然是强烈建议质量优先！在保证质量的前提下，再保证数量！
当然，这里也存在一个可以商讨的点：就是如果在点塔的时候，刚好差了一两个塔的时候，而又确实没有指标较好的因子可以提交的时候，可以为了点塔而牺牲一下质量，但是建议同时要在同地区下的其他数据集下面提交若干个高质量的因子！同时在SA的选择下，适度倾向这个地区，通过SA来拉回一些质量。

**【5、虚心请教，坚持学习与进步】**

这是我下半年最深切的体会，独学而无友，注定思路会受到严重的局限性影响，尤其是12月中下旬以来WQ平台规则越来越严格的情况下，必须要学习新鲜的思路和方法，并且积极尝试新的工具，比如AI、MCP、cnhkmcp等等，而这些好的工具都是需要和同志们一起探讨、共同提高，闭门造车注意是走不远的！

写在最后，感谢WQ平台、感谢国区的几位老师、感谢在下半年中直接或间接帮助我的同志们（排名不分先后）：华子哥、游戏王、橘子姐、孙哥、羊羊、琪姐、老虎哥、小虎哥、课代表、MG哥等等大佬……，感谢搞出来了cnhkmcp的造福大家的幕后匿名大佬！感谢无私赠送我鼠标垫的楠姐！！！

祝愿大家在即将结束的2025年收获满满！年初所想全部得尝所愿！

祝愿大家在即将到来的2026年大展鸿图！VF常驻1.0~~~~

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

感谢大佬分享，太强了，能连着这么久保持超高vf

我第二次更新vf就跌到0.8了，看完帖子学到了很多，希望能追上大佬vf的步伐

===================================================================================


---

### 技术对话片段 56 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【ValueFactor】关于近几次Value Factor更新后暂时仍保持097以上的一些思考与分享经验分享_37218633411223.md
- **时间**: 5个月前

**提问/主帖背景 (XW85841)**:
老规矩，无图无真相，先上图：


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025/5/24
> 2025/6/28
> 2025/7/20
> 2025/8/19
> 2025/9/20
> 2025/10/25
> 2025/11/21
> 2025/12/16
> Value Factor
> 0.74
> 0.59
> 0.94
> 0.95
> 0.97
> 0.99
> 0.97
> 0.97
> 2025.1.1
> 2025.2.1
> 2025.3.1
> 2025.1.1 
> 2025.5.1
> 2025.6.1 
> 2025.7.1
> 2025.8.1 
> Time period
> 2025.3.31
> 2025.4.30
> 2025.5.31
> 2025.6.30
> 2025.7.31
> 2025.8.31
> 2025.9.30
> 2025.10.31
> 说明
> 更新
> 更新
> 更新
> 更新
> 更新
> 更新
> 更新


可以看出，进入7月份以后，我的ValueFator数值基本上维持在0.9以上，并且从0.94一度上涨至0.99，最近两次更新之后也维持在0.97，还算是比较稳定、也算是中高位区间的分位段。对于我个人来说，从趋势上来看算是较为稳定的，并且一度在10月份的时候达到了0.99，虽然没有突破1.0的极限，但是对于没有任何量化、金融/股票、代码功底的我来说，个人还算是很满意的！

对于目前较为稳定的高VF的情况，我通过简要的回顾和分析（由于代码功底限制，无法通过代码进行定量和精准的分析，还请见谅），大概有以下几点原因，供大家批评指正，其中可取之处也希望能帮助到有需要的同志。
 **【1、坚持做SA】**

这是最为关键的核心点之一。之前已经有不少同志们提到了这一点，通过我的亲身经历的反馈，这个对于维持VF是至关重要的一个影响因素！在这里继续建议，无论当期的VF是高还是低，都建议坚持每天提交一个质量还可以的SA，可以不要求是35，但是起码fitness\sharpe\margin还是需要维持在较高的指标再去提交；不建议为了交SA而交SA，目标还是要优化该地区的总体指标。

**【2、坚持做四大地区+D1】**

我之前写过一篇帖子，主要是分享踩过的坑，里面就讨论过这一条。因为我之前因为没有人指导和提醒，提交了若干个小地区的因子，导致VF在5月份之前一直处于低水位的水平，直接影响了每天的BASE；后面就只做四大区域：USA\EUR\GLB\ASI，从VF变化反馈来看，这个选择和坚持是极为正确的！同时由于本人水平所限，一直不敢碰D0、也不敢碰CHN，但是四大区域对于维持Master的等级所需要的塔已经基本上够了！

帖子链接如下：
 [[L2] 【避坑】一个龟速上升但仍坚持前行的老新手顾问踩过的一些坑经验分享_32989653853975.md]([L2] 【避坑】一个龟速上升但仍坚持前行的老新手顾问踩过的一些坑经验分享_32989653853975.md)

**【3、提交regluar alpha数量保持稳定】**

从10月份VF从0.99降到11月的0.97、然后12月份仍然维持在0.97，通过我的简单分析，发现了应该是提交数量的震荡产生了影响：由于Q3点塔相对顺利，所以在9月份放松了一下，提交的数量只有7、8月份平均的70%左右的水平，这个直接就在11月份VF更新的时候反应了，同时这个因素也直接影响了12月份的VF，虽然数字上维持了0.97没有变化，但是主要还是8月份的正向影响保住了这个水平。同时反观7、8、9这三个月VF的正向趋势变化，也与6、7、8这三个月为了能够在Q3维持Master的段位而持续努力，提交的因子数量基本上自稳定略增加，也间接印证了我的判断。

同时，如果1月份再更新VF的时候，如果VF继续下降，那么就基本上可以再次印证了我的猜测——因为8月份的影响周期已结束了，9月少、10月更少；但是11月份数量赶了上来，希望能有所抵消9、10月份提交数量下降较多而导致的负面影响。

**【4、保证质量提交底线】**

通过与其他VF变动较大的同志们的聊天，不少VF急剧下跌的基本上都是为了点塔而提交了不少指标一般的因子！也就是我前面那个帖子里我自己踩过的坑——绿了就提交！这是坚持不建议的提交方式！如果想让自己的VF不骤降，仍然是强烈建议质量优先！在保证质量的前提下，再保证数量！
当然，这里也存在一个可以商讨的点：就是如果在点塔的时候，刚好差了一两个塔的时候，而又确实没有指标较好的因子可以提交的时候，可以为了点塔而牺牲一下质量，但是建议同时要在同地区下的其他数据集下面提交若干个高质量的因子！同时在SA的选择下，适度倾向这个地区，通过SA来拉回一些质量。

**【5、虚心请教，坚持学习与进步】**

这是我下半年最深切的体会，独学而无友，注定思路会受到严重的局限性影响，尤其是12月中下旬以来WQ平台规则越来越严格的情况下，必须要学习新鲜的思路和方法，并且积极尝试新的工具，比如AI、MCP、cnhkmcp等等，而这些好的工具都是需要和同志们一起探讨、共同提高，闭门造车注意是走不远的！

写在最后，感谢WQ平台、感谢国区的几位老师、感谢在下半年中直接或间接帮助我的同志们（排名不分先后）：华子哥、游戏王、橘子姐、孙哥、羊羊、琪姐、老虎哥、小虎哥、课代表、MG哥等等大佬……，感谢搞出来了cnhkmcp的造福大家的幕后匿名大佬！感谢无私赠送我鼠标垫的楠姐！！！

祝愿大家在即将结束的2025年收获满满！年初所想全部得尝所愿！

祝愿大家在即将到来的2026年大展鸿图！VF常驻1.0~~~~

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

感谢大佬分享，太强了，能连着这么久保持超高vf

我第二次更新vf就跌到0.8了，看完帖子学到了很多，希望能追上大佬vf的步伐

===================================================================================


---

### 技术对话片段 57 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【VF 095收入经验分享】高VF如何拿到更高的base经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (WL58980)**:
以VF更新为一个周期，Base到底有多少呢？

此次VF更新周期是2026年2月10日至3月23日，周期长达40天左右，也是非常幸运，此次VF提升到了0.95，在此期间我的base收入一共是US$1,917.72，日均将近US$50。


> [!NOTE] [图片 OCR 识别内容]
> Period
> Regular
> Super
> Total
> Displayed Period
> 02/10/2026
> 03/23/2026
> US$1,012.86
> US$904.86
> US$1,917.72


那么在高VF的情况下，应该如何拿到更高的base呢？

首先，来看看现阶段影响base的主要因素：

1.VF：决定base的上限，VF越高，base的上限越高；

2.Daily  Osmosis Rank（简称OS）:OS是二月刚上线与base关联的新指标，一周为一个周期，一周更新5次（重点）；

3.Alphas的质量，相关性与数量：Alphas的质量越好以及相关性越低，base相对会更高；而且应该尽量提交 rea ,4个ppa可能比不过一个rea；Super Alphas则尽量追求三“5”；

4. Datasets Theme：主题加成一般两周更新一次，提交主题Alphas可以获得更高的base。

那么如何根据这些相关因素来获取更高的base呢？

我的方法是，在保证Alphas质量的前提下“舍小取大”：

这里的大小只的是OS的大小，根据我几周的体验来看，0.65可能是OS的分水岭，所以大于0.65则为大，小于则为小。在OS大于0.65时，则提交 Datasets Theme相关的Alphas，小于0.65时则提交其他区域的Alphas,至于为何要这样取舍呢？

原因如下：

1，在OS较低时， Datasets Theme对base的影响并不是很大，然而在OS较高时， Datasets Theme可能带来双倍的收益，大家可以看我的base比例，Regular占比较高，说明我的这种方法是有效的（还有一部分原因是因为还是gold,Super Alphas还没有not(own)权限 ；


> [!NOTE] [图片 OCR 识别内容]
> 03/17/2026
> Regular: 59.52
> Super:
> 39.08
> Total:
> 98.C


2，很多人会说，既然 Datasets Theme能提高base，为何不一直提交 Datasets Theme相关的Alphas呢？由于 Datasets Theme长达两周，每天提交同一个区域的Alphas难度比较高，而且长期提交会导致Alphas过于集中，既影响combine又影响VF,得不偿失。

所以，从长远角度来看，应该有所取舍。

嘿嘿，大家有没有注意到上面我有标记“重点”，OS一周更新五次，那么剩余两天则与第五天的OS一样，那么如果在最后一天是高OS，那么就会有三天的高OS了，妙哉，妙哉！！！

最后，我想请教一下各位，你们的Community activity是如何提升的呀，我们每天都会在论坛学习，评论，偶尔也会发帖子，参加每月会议，可Community activity却每天都下降零点几，非常困惑。

最最后，祝大家每天base都拉满！！！！！！加油！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

大佬一个月的base pay都已经抵得上M的季度奖了

实在太强了！

=============================================================================


---

### 技术对话片段 58 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【VF 095收入经验分享】高VF如何拿到更高的base经验分享_39251610735639.md
- **时间**: 2个月前

**提问/主帖背景 (WL58980)**:
以VF更新为一个周期，Base到底有多少呢？

此次VF更新周期是2026年2月10日至3月23日，周期长达40天左右，也是非常幸运，此次VF提升到了0.95，在此期间我的base收入一共是US$1,917.72，日均将近US$50。


> [!NOTE] [图片 OCR 识别内容]
> Period
> Regular
> Super
> Total
> Displayed Period
> 02/10/2026
> 03/23/2026
> US$1,012.86
> US$904.86
> US$1,917.72


那么在高VF的情况下，应该如何拿到更高的base呢？

首先，来看看现阶段影响base的主要因素：

1.VF：决定base的上限，VF越高，base的上限越高；

2.Daily  Osmosis Rank（简称OS）:OS是二月刚上线与base关联的新指标，一周为一个周期，一周更新5次（重点）；

3.Alphas的质量，相关性与数量：Alphas的质量越好以及相关性越低，base相对会更高；而且应该尽量提交 rea ,4个ppa可能比不过一个rea；Super Alphas则尽量追求三“5”；

4. Datasets Theme：主题加成一般两周更新一次，提交主题Alphas可以获得更高的base。

那么如何根据这些相关因素来获取更高的base呢？

我的方法是，在保证Alphas质量的前提下“舍小取大”：

这里的大小只的是OS的大小，根据我几周的体验来看，0.65可能是OS的分水岭，所以大于0.65则为大，小于则为小。在OS大于0.65时，则提交 Datasets Theme相关的Alphas，小于0.65时则提交其他区域的Alphas,至于为何要这样取舍呢？

原因如下：

1，在OS较低时， Datasets Theme对base的影响并不是很大，然而在OS较高时， Datasets Theme可能带来双倍的收益，大家可以看我的base比例，Regular占比较高，说明我的这种方法是有效的（还有一部分原因是因为还是gold,Super Alphas还没有not(own)权限 ；


> [!NOTE] [图片 OCR 识别内容]
> 03/17/2026
> Regular: 59.52
> Super:
> 39.08
> Total:
> 98.C


2，很多人会说，既然 Datasets Theme能提高base，为何不一直提交 Datasets Theme相关的Alphas呢？由于 Datasets Theme长达两周，每天提交同一个区域的Alphas难度比较高，而且长期提交会导致Alphas过于集中，既影响combine又影响VF,得不偿失。

所以，从长远角度来看，应该有所取舍。

嘿嘿，大家有没有注意到上面我有标记“重点”，OS一周更新五次，那么剩余两天则与第五天的OS一样，那么如果在最后一天是高OS，那么就会有三天的高OS了，妙哉，妙哉！！！

最后，我想请教一下各位，你们的Community activity是如何提升的呀，我们每天都会在论坛学习，评论，偶尔也会发帖子，参加每月会议，可Community activity却每天都下降零点几，非常困惑。

最最后，祝大家每天base都拉满！！！！！！加油！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

大佬一个月的base pay都已经抵得上M的季度奖了

实在太强了！

=============================================================================


---

### 技术对话片段 59 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用_39466731879063.md
- **时间**: 2个月前

**提问/主帖背景 (JG15244)**:
### 【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？

昨天突发奇想，想加一个每日base排行榜，但不知道会有多少同学支持使用，毕竟人数太少的话，就没有实际意义了，所以如果你支持并且会使用的话，希望留下你的评论。

### 初步构想

- 每日金额由自己手动输入上传。【为增加可信度，允许上传截图（不强制）（提供ID水印，防止被二次盗取使用）】

- 可选匿名（wq_id）。
- 除base外，同时关联vf、osm信息（可选展示）、提交的alpha指标【同样允许上传截图】
- 开放范围：1. 仅对当日上传了base信息的用户展示。2. 仅对指定参与用户开放。

#### 

### 存在的作用

1. 可以清晰看到其他同学的收益。

2. 关联vf、osm、alpha指标后，可以对后续在什么vf + osm下提交何种alpha更易拿到高base有一个大概的认知。

3. 收集数据量够多后或许可以拟合出一个base函数来计算预期收益。

### 最后

欢迎评论区讨论，base榜存在的合理性，你是否会上传数据并使用它，不同意见的设计方案等等。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

蛮好的 这样大家也就知道各个os rank + vf的时候交什么Alpha能做到base收益最大化了

感谢大佬！

=============================================================================


---

### 技术对话片段 60 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【WQ Manager】大更新新增Base Payment排行榜_39907023480599.md
- **时间**: 2个月前

**提问/主帖背景 (JG15244)**:
继  [【WQ Manager 新需求调研】想加一个每日base排行榜，会有多少同学使用？]([Commented] 【WQ Manager 新需求调研】想加一个每日base排行榜会有多少同学使用_39466731879063.md)  需求调研后，Base Payment 排行榜也是正式上线了！

访问地址： [[链接已屏蔽]) OR 华子哥插件直达

### 使用方式

1. 点击右下角加号 ➕，再点击BASEPAY，进入 Base Payment Dashboard 页面
 
> [!NOTE] [图片 OCR 识别内容]
> Base Payment Dashboard
> 更新上传
> Refresh
> 快来看看大佬们今天都赚了多少刀乐吧!
> PROFILE
> RECORD DAT巳
> PERMISS10N GATE
> 2026-04-21
> 已上传2026-04-21,
> 可查看该日数据
> TRENDS
> GENIUS
> Daily Insight Dashboard
> 2026-04-21
> 展开
> NOTICE
> VALUE
> Base Payment Leaderboard
> Total 7
> COMBINED
> No
> Date
> User
> Total Payment
> Regular Payment
> Super Payment
> Regular Count
> Count
> Value Factor
> Daily Osmosis Rank
> CONSULTANT
> 2026-04-21
> D27384
> 11.34
> 2.90
> 8.44
> 0.96
> 0.3.
> OSMOSIS
> 2026-04-21
> DA98440
> 10.03
> 2.36
> 7.67
> 0.93
> 0.1.
> 2026-04-21
> PP26750
> 9.83
> 3.06
> 6.77
> 1.00
> 0.0:
> BASEPAY
> 2026-04-21
> 0X52484
> 9.23
> 4.03
> 5.20
> 0.94
> HOME
> 2026-04-21
> 匿名用户
> 8.81
> 4.24
> 4.57
> 0.8
> 0.31
> 2026-04-21
> LX57490
> 4.33
> 1.81
> 2.52
> 0.75
> 0.1'
> FEEDBACK
> 2026-04-21
> 顾问 JG15244 (Rank 67)
> 3.58
> 1.71
> 1.87
> 0.74
> 0.1
> Total 7
> Super
> SOIpage
 
2. 初次进入需要设置设置自己的验证口令，每8小时需要重新验证一次（暂时没有提供修改入口，忘记了话请联系作者）

> 目前依旧没有设置账号的概念，仅对base-payment页面及其接口设置权限验证


> [!NOTE] [图片 OCR 识别内容]
> Base Payment 访问验证
> 诸输入 Base Payment 页面访问口令
> 请输入访问口令
> 取消
> 验证井进入


3. 上传自己的数据

> 1. 当且仅当你上传了自己的数据后，才可以查看其他人的数据，不想让别人知道ID的话可以选择匿名。
> 2. 左上角选择不同的时间，可以上传不同时间的数据。
> 3. 上传图片可以增加可信性。
> 温馨提示：为保护其他人的权益，恳请您不要胡乱上传数据，证伪假数据后，将被禁止访问wqmanager！


> [!NOTE] [图片 OCR 识别内容]
> Base Payment Dal
> 2026-04-21
> 更新上传
> Refresh
> 更新 Base Payment
> 快来看看大佬们今天都赚了多少刀乐吧!
> 为保障信息准确有效。请您奶实填写;
> 此举既惠及他人;
> 也便利自身。
> 温馨提示:  不要乱填哦;乱填会被禁止访问网站喔!
> R巳CORD
> DAT巳
> 隐私设置
> 2026-04-21
> 展示方式
> 不匿名 (展示 WQ_ID)
> 匿名 (仅显示"匿名用户 )
> 收益与数量
> Daily Insight Dashboard
> 2026-04-21
> 展开
> Regular Payment
> Super Payment
> 1.71
> 1.87
> Regular Count
> Super Count
> Base Payment Leaderboard
> Total 7
> Value Factor
> Daily Osmosis Rank
> 0.74
> 0.17
> No
> Date
> UIe
> Factor
> Daily Osmosis Rank
> 图片上传(可选) [抓有截图可信度更高! ]
> 2026-04-21
> D27384
> 0.96
> 0.3.
> 支持最多9张图片。单张不超过 IOMB。
> 2026-04-21
> DA98440
> 0.93
> 0.1.
> 2026-04-21
> PP26750
> 1.00
> 0.0{
> 2026-04-21
> 0X5248
> 0.94
> 0.1
> 取消
> 更新
> 2026-04-21
> 匿名用户
> 0.81
> 0.31
> 2026-04-21
> LX57490
> 4.33
> 1.81
> 2.52
> 0.75
> 0.1
> 2026-04-21
> 顾问 JG15244 (Rank 67)
> 3.58
> 1.71
> 1.87
> 0.74
> 0.1
> Total 7
> User
> SOIpage


### 后续

1. 未避免账号密码泄露，网站不会提供一键上传操作，后续会有插件佬和好心人开发对应的插件，敬请期待。

2. 后续计划同时展示当日提交alpha的具体指标，如sharpe、fitness等等。

3. base功能尚处于初步阶段，可能存在bug和功能缺陷，恳请您使用后积极提出疑问和建议。

**欢迎大家使用共建！祝大家base节节高！**

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！

不过我最近base pay有点寒酸哈哈哈，填了一次发现快垫底了

=============================================================================


---

### 技术对话片段 61 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【WQ数据监控 v020】wqmanagerqzzio 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比代码优化.md
- **时间**: 3个月前

**提问/主帖背景 (JG15244)**:
在线地址： [[链接已屏蔽])

## 更新内容

1. 个人信息页面增加 Osmosis Rank 变化趋势图、周维度对比图。
2. 新增 consulant 页面，整合 consulant 全部信息。

## 更新截图


> [!NOTE] [图片 OCR 识别内容]
> Consultant Detail Dashboard
> REFRESH
> Merged view of ` Ieaderboard_consultant_user
> and
> leaderboard_genius_user
> RECORD
> DAT巳
> COUNTRY/REGION
> GENIUS LEVEL
> USER SEARCH
> 2026-02-23
> Select countrylregion
> Select level
> Enter WQ_ID keyword
> APPLY
> Reset
> FILTERED USERS
> CONSULTANT COVCRAGE
> GENIUS COVERAG卫
> MATCHED USERS
> COUNTRIPS
> GENIUS LEVELS
> 10,762
> 8,419
> 10,759
> 8,416
> 16
> 4
> Date 2026-02-23
> Fromn
> Fromn Ieaderboard
> UISET
> Users found i both tables On
> Distinct Countries in Curtent
> Distinct levels in current result
> leaderboard_consultant_
> UISeT
> selected date
> Tesult
> AllMetrics
> Total 10762
> No_
> User
> Country
> University
> Level
> Best Level
> Weight
> Value
> Osmosis
> Data Fields
> RA
> RA Prod
> RA SI
> Rank
> Subm
> Corr
> 6247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63372
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec.。
> GOLD
> GOLD
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> R19116
> IN
> Dr.APJ.Abdul Kalar。。
> GOLD
> GOLD
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> XL82940
> CN
> GOLD
> EXPERI
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> KE
> Jomo Kenyatta Univer。
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE
> GOLD
> GOLD
> 2.31
> 0.47
> 0.90
> 269
> 326
> 0.6803
> P24362
> CN
> TNuhan
> University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 0242372
> CN
> Harbin Engineering U。
> GOLD
> GOLD
> 0.00
> 0.93
> 0.89
> 145
> 167
> 0.6402
> 10
> 巫24675
> IN
> Deen Dayal Upadhyay.-
> GOLD
> EXPERI
> 26.63
> 0.30
> 0.88
> 1,990
> 1,755
> 0.6537
> 11
> T42173
> CN
> Arizona State Universi。
> EXPERI
> EXPERI
> 26.11
> 0.44
> 0.88
> 460
> 648
> 0.6685
> 12
> CL93587
> CN
> HangZhou Dianziuni。
> EXPERI
> EXPERI
> 14.88
> 0.28
> 0.87
> 390
> 295
> 0.6609
> 13
> J75700
> Harbin Institute Of Te。
> EXPERI
> EXPERI
> 0.00
> 0.90
> 0.87
> 124
> 106
> 0.6568
> 14
> PY32594
> CN
> Huazhong University
> EXPERI
> EXPERI
> 0.00
> 0.42
> 0.87
> 441
> 480
> 0.6867
> 15
> 2262721
> CN
> MASTER
> MASTER
> 7.37
> 0.95
> 0.87
> 405
> 316
> 0.7365
> 16
> SL10033
> University Of Internati。
> EXPERI
> MASTER
> 39.26
> 0.68
> 0.87
> 625
> 447
> 0.5676
> 17
> T12226
> CN
> GOLD
> GOLD
> 0.00
> 0.55
> 0.87
> 182
> 207
> 0.6052
> 18
> 4T26308
> IN
> Indian Institute Of Tec..
> GOLD
> MASTER
> 13.57
> 0.03
> 0.86
> 408
> 471
> 0.7073
> 19
> J025713
> KE
> CHUKA university
> EXPERI
> MASTER
> 4.72
> 0.32
> 0.86
> 1,404
> 1,498
> 0.6529
> 20
> 1053462
> CN
> NanJing Audit Univer。。。
> GOLD
> EXPERT
> 1.14
> 0.38
> 0.86
> 166
> 126
> 0.6513
> Total 10762
> 20/page
> 539
> genius



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Weekly
> R巳CORD DAT巳
> Rank
> 1.00
> 2026-02-23
> Reset
> 0.80
> 0.60
> FILTERED USERS
> GPNIUS LDVPLS
> 10,762
> 0.40
> Date 2026-02-23
> 0.33
> Distinct levels in current result
> 0.20
> 0.00
> All Metrics
> Total 10762
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 2026-02-16'
> 2026-02-17
> 2026-02-18'
> 2026-02-19'
> 2026-02-20'
> 2026-02-21'
> 2026-02-22'
> 2026-02-23'



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Daily
> R巳CORD DAT巳
> 2026-02-16
> 2026-02-22
> 3 2026-02-23
> 2026-03-01
> 2026-02-23
> Rank
> Reset
> 1.00
> 0.96
> 0.80
> FILTERED USERS
> GPNIUS LDVPLS
> 0.60
> 10,762
> Date 2026-02-23
> Distinct levels in current result
> 0.40
> 0.24
> 0.20
> All Metrics
> 0.00
> Total 10762
> 苘凶
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521



> [!NOTE] [图片 OCR 识别内容]
> 个人中心
> 退出登录
> 顾问 JG15244 (Rank 67)
> 单日最大娈化
> 当前 Weight
> 历史最高
> 今日娈化
> 0.79
> 17.60
> 17.60
> +0.00
> 日期2025-12-24
> Weight 变化趋势
> 共71犬
> 权重因子
> 19.56
> 15.00
> 11.23
> 10.00
> 5.00
> 00
> ^?
> ^9
> 8
> 8
> 2
> ^2
> 02
> 02
> 02
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> 16
> 19
> 20
> 23
> 02
> 02
> 02
> 02
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> Power
> Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 0.90
> 1.50
> 0.87
> 1.00
> 0.84
> 0.50
> 0.81
> 0.79
> 0.04
> 202508
> 202509
> 202510
> 202508
> 202509
> 202510
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 历史记录
> 共71条
> VALUE
> DA11
> 05M0515
> REGULAR
> REGULAR ALPHA
> REGULAR
> SUPER ALPH4
> SUPER ALPHA
> SUPER ALPH
> 日期
> WEIGHT
> FA CT0R
> RANk
> ALPHA 提交数
> 生产相关
> 41PH4
> 自相关
> 提交数
> 产相关
> 自相
> 2026-02-23
> 17.60
> 0.89
> 0.64
> 503
> 0.6133
> 0.3392
> 244
> 0.5860
> 0.50
> 2026-02-22
> 17.60
> 0.89
> 0.73
> 502
> 0.6131
> 0.3392
> 243
> 0.5865
> 0.50
> 2026-02-21
> 17.60
> 89
> 38
> 501
> 0.6128
> 3393
> 242
> 0.5861
> 0.50
> 2026-02-20
> 17.35
> 500
> 0.6135
> 3397
> 241
> 0.5869
> 0.50
> 2026-02-19
> 17.08
> 38
> 0.6149
> 3404
> 240
> 0.5865
> 0.50
> 2026-02-18
> 16.82
> 0.31
> 492
> 0.6174
> 3419
> 239
> 0.5875
> 0.50
> 2026-02-17
> 16.82
> 89
> 0.31
> 487
> 6204
> 3436
> 238
> 0.5873
> 0.50
> 2026-02-16
> 16.82
> 89
> 0.31
> 486
> ).6205
> 3438
> 237
> 0.5880
> 0.50
> 2026-02-15
> 16.82
> 89
> 486
> 0.6205
> 3438
> 236
> 0.5876
> 50
> 2026-02-14
> 16.64
> 89
> 485
> 1.6202
> 3439
> 234
> 0.5878
> 50
> Total 71
> Goto
> 01-06
> 01-16
> 01-18
> 01-20
> 12-17
> ~
> 12-23
> 12-25
> 12-27
> 12-29
> 12-31
> 01-02
> 01-04
> 01-08
> 01-10
> 01-12
> 01-14
> 01-22
> 01-24
> 01-26
> 01-28
> 01-30
> 02-01
> 02-03
> 02-07
> 02-11
> 02-13
> 02-21
> 合
> ~02-17
> ~02-18
> ~02-21
> ~02-22
> 2026
> 2026
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> Pool



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到曰维度
> 2026-02-16
> 2026-02-22
> 0
> 2026-02-23
> 2026-03-01
> Rank
> 1.00
> 80
> 0.64
> 60
> 0.40
> 0.20
> 0.00
> 周二
> 周三
> 周五
> 周六
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21
> ~02-16'
> ~02-17
> ~02-18
> ~02-19
> ~02-20
> ~02-22
> 2026-02-23'
> ~02-21
> 2026-
> 2026-
> 2026-
> 2026-C
> 2026-C
> 2026-C
> 2026-0


> 欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！
> 欢迎 start 和 issue ！
> 后端项目地址： [[链接已屏蔽])
> 前端项目地址： [[链接已屏蔽])

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

给大佬点赞   非常好用且实用

感谢大佬的无私分享！

===================================================================================


---

### 技术对话片段 62 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【WQ数据监控 v020】wqmanagerqzzio 版本更新 ---- 新增 Osmosis Rank 变化情况及周维度对比代码优化_38582852015895.md
- **时间**: 3个月前

**提问/主帖背景 (JG15244)**:
在线地址： [[链接已屏蔽])

## 更新内容

1. 个人信息页面增加 Osmosis Rank 变化趋势图、周维度对比图。
2. 新增 consulant 页面，整合 consulant 全部信息。

## 更新截图


> [!NOTE] [图片 OCR 识别内容]
> Consultant Detail Dashboard
> REFRESH
> Merged view of ` Ieaderboard_consultant_user
> and
> leaderboard_genius_user
> RECORD
> DAT巳
> COUNTRY/REGION
> GENIUS LEVEL
> USER SEARCH
> 2026-02-23
> Select countrylregion
> Select level
> Enter WQ_ID keyword
> APPLY
> Reset
> FILTERED USERS
> CONSULTANT COVCRAGE
> GENIUS COVERAG卫
> MATCHED USERS
> COUNTRIPS
> GENIUS LEVELS
> 10,762
> 8,419
> 10,759
> 8,416
> 16
> 4
> Date 2026-02-23
> Fromn
> Fromn Ieaderboard
> UISET
> Users found i both tables On
> Distinct Countries in Curtent
> Distinct levels in current result
> leaderboard_consultant_
> UISeT
> selected date
> Tesult
> AllMetrics
> Total 10762
> No_
> User
> Country
> University
> Level
> Best Level
> Weight
> Value
> Osmosis
> Data Fields
> RA
> RA Prod
> RA SI
> Rank
> Subm
> Corr
> 6247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63372
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec.。
> GOLD
> GOLD
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> R19116
> IN
> Dr.APJ.Abdul Kalar。。
> GOLD
> GOLD
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> XL82940
> CN
> GOLD
> EXPERI
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> KE
> Jomo Kenyatta Univer。
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE
> GOLD
> GOLD
> 2.31
> 0.47
> 0.90
> 269
> 326
> 0.6803
> P24362
> CN
> TNuhan
> University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 0242372
> CN
> Harbin Engineering U。
> GOLD
> GOLD
> 0.00
> 0.93
> 0.89
> 145
> 167
> 0.6402
> 10
> 巫24675
> IN
> Deen Dayal Upadhyay.-
> GOLD
> EXPERI
> 26.63
> 0.30
> 0.88
> 1,990
> 1,755
> 0.6537
> 11
> T42173
> CN
> Arizona State Universi。
> EXPERI
> EXPERI
> 26.11
> 0.44
> 0.88
> 460
> 648
> 0.6685
> 12
> CL93587
> CN
> HangZhou Dianziuni。
> EXPERI
> EXPERI
> 14.88
> 0.28
> 0.87
> 390
> 295
> 0.6609
> 13
> J75700
> Harbin Institute Of Te。
> EXPERI
> EXPERI
> 0.00
> 0.90
> 0.87
> 124
> 106
> 0.6568
> 14
> PY32594
> CN
> Huazhong University
> EXPERI
> EXPERI
> 0.00
> 0.42
> 0.87
> 441
> 480
> 0.6867
> 15
> 2262721
> CN
> MASTER
> MASTER
> 7.37
> 0.95
> 0.87
> 405
> 316
> 0.7365
> 16
> SL10033
> University Of Internati。
> EXPERI
> MASTER
> 39.26
> 0.68
> 0.87
> 625
> 447
> 0.5676
> 17
> T12226
> CN
> GOLD
> GOLD
> 0.00
> 0.55
> 0.87
> 182
> 207
> 0.6052
> 18
> 4T26308
> IN
> Indian Institute Of Tec..
> GOLD
> MASTER
> 13.57
> 0.03
> 0.86
> 408
> 471
> 0.7073
> 19
> J025713
> KE
> CHUKA university
> EXPERI
> MASTER
> 4.72
> 0.32
> 0.86
> 1,404
> 1,498
> 0.6529
> 20
> 1053462
> CN
> NanJing Audit Univer。。。
> GOLD
> EXPERT
> 1.14
> 0.38
> 0.86
> 166
> 126
> 0.6513
> Total 10762
> 20/page
> 539
> genius



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Weekly
> R巳CORD DAT巳
> Rank
> 1.00
> 2026-02-23
> Reset
> 0.80
> 0.60
> FILTERED USERS
> GPNIUS LDVPLS
> 10,762
> 0.40
> Date 2026-02-23
> 0.33
> Distinct levels in current result
> 0.20
> 0.00
> All Metrics
> Total 10762
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521
> 2026-02-16'
> 2026-02-17
> 2026-02-18'
> 2026-02-19'
> 2026-02-20'
> 2026-02-21'
> 2026-02-22'
> 2026-02-23'



> [!NOTE] [图片 OCR 识别内容]
> Consultant De
> 6247187
> Daily Osmosis Ralk Trend
> REFRESH
> Merged view of
> leaderboard_CO
> 2026-02-16
> 2026-02-23
> Switch to Daily
> R巳CORD DAT巳
> 2026-02-16
> 2026-02-22
> 3 2026-02-23
> 2026-03-01
> 2026-02-23
> Rank
> Reset
> 1.00
> 0.96
> 0.80
> FILTERED USERS
> GPNIUS LDVPLS
> 0.60
> 10,762
> Date 2026-02-23
> Distinct levels in current result
> 0.40
> 0.24
> 0.20
> All Metrics
> 0.00
> Total 10762
> 苘凶
> RA Prod
> No
> User
> RA5
> Rank
> SubIl
> COrI
> @247187
> CN
> GOLD
> GOLD
> 0.00
> 0.50
> 0.96
> 105
> 98
> 0.6465
> L63327
> CN
> GOLD
> GOLD
> 0.00
> 0.92
> 0.92
> 164
> 129
> 0.6381
> NP83488
> IN
> Indian Institute OfTec。。。 
> GOLD 
> GOLD 
> 0.02
> 0.50
> 0.92
> 91
> 148
> 0.8289
> 卫19116
> IN
> Dr.APJ.Abdul Kalam..
> GOLD 
> GOLD 
> 0.00
> 0.32
> 0.92
> 865
> 1,718
> 0.6898
> X82940
> CN
> GOLD
> EXPERT
> 0.00
> 0.05
> 0.92
> 436
> 432
> 0.6851
> 0014236
> K
> Jomo Kenyatta Univer_
> GOLD
> GOLD
> 15.15
> 0.73
> 0.91
> 457
> 615
> 0.6628
> 亚55093
> KE 
> GOLD 
> GOLD 
> 2.31
> 0.47
> 269
> 326
> 0.6803
> P24362
> CN
> Wuhan University
> EXPERT
> EXPERT
> 20.10
> 0.78
> 0.90
> 381
> 452
> 0.6521



> [!NOTE] [图片 OCR 识别内容]
> 个人中心
> 退出登录
> 顾问 JG15244 (Rank 67)
> 单日最大娈化
> 当前 Weight
> 历史最高
> 今日娈化
> 0.79
> 17.60
> 17.60
> +0.00
> 日期2025-12-24
> Weight 变化趋势
> 共71犬
> 权重因子
> 19.56
> 15.00
> 11.23
> 10.00
> 5.00
> 00
> ^?
> ^9
> 8
> 8
> 2
> ^2
> 02
> 02
> 02
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> 16
> 19
> 20
> 23
> 02
> 02
> 02
> 02
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> Power
> Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 0.90
> 1.50
> 0.87
> 1.00
> 0.84
> 0.50
> 0.81
> 0.79
> 0.04
> 202508
> 202509
> 202510
> 202508
> 202509
> 202510
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 历史记录
> 共71条
> VALUE
> DA11
> 05M0515
> REGULAR
> REGULAR ALPHA
> REGULAR
> SUPER ALPH4
> SUPER ALPHA
> SUPER ALPH
> 日期
> WEIGHT
> FA CT0R
> RANk
> ALPHA 提交数
> 生产相关
> 41PH4
> 自相关
> 提交数
> 产相关
> 自相
> 2026-02-23
> 17.60
> 0.89
> 0.64
> 503
> 0.6133
> 0.3392
> 244
> 0.5860
> 0.50
> 2026-02-22
> 17.60
> 0.89
> 0.73
> 502
> 0.6131
> 0.3392
> 243
> 0.5865
> 0.50
> 2026-02-21
> 17.60
> 89
> 38
> 501
> 0.6128
> 3393
> 242
> 0.5861
> 0.50
> 2026-02-20
> 17.35
> 500
> 0.6135
> 3397
> 241
> 0.5869
> 0.50
> 2026-02-19
> 17.08
> 38
> 0.6149
> 3404
> 240
> 0.5865
> 0.50
> 2026-02-18
> 16.82
> 0.31
> 492
> 0.6174
> 3419
> 239
> 0.5875
> 0.50
> 2026-02-17
> 16.82
> 89
> 0.31
> 487
> 6204
> 3436
> 238
> 0.5873
> 0.50
> 2026-02-16
> 16.82
> 89
> 0.31
> 486
> ).6205
> 3438
> 237
> 0.5880
> 0.50
> 2026-02-15
> 16.82
> 89
> 486
> 0.6205
> 3438
> 236
> 0.5876
> 50
> 2026-02-14
> 16.64
> 89
> 485
> 1.6202
> 3439
> 234
> 0.5878
> 50
> Total 71
> Goto
> 01-06
> 01-16
> 01-18
> 01-20
> 12-17
> ~
> 12-23
> 12-25
> 12-27
> 12-29
> 12-31
> 01-02
> 01-04
> 01-08
> 01-10
> 01-12
> 01-14
> 01-22
> 01-24
> 01-26
> 01-28
> 01-30
> 02-01
> 02-03
> 02-07
> 02-11
> 02-13
> 02-21
> 合
> ~02-17
> ~02-18
> ~02-21
> ~02-22
> 2026
> 2026
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> 2026-
> Pool



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到曰维度
> 2026-02-16
> 2026-02-22
> 0
> 2026-02-23
> 2026-03-01
> Rank
> 1.00
> 80
> 0.64
> 60
> 0.40
> 0.20
> 0.00
> 周二
> 周三
> 周五
> 周六
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21



> [!NOTE] [图片 OCR 识别内容]
> 5.00
> 0.00
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-23
> 切换到周维度
> Rank
> 1.00
> 0.80
> 0.60
> 0.43
> 0.40
> 0.20
> 0.00
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combined Alpha
> 0
> Power Pool
> ~ Selected Alpha
> 0.97
> Combined
> 0.96
> 2.32
> 0.93
> 2.00
> 12-15
> 12-19
> 12-25
> 12-29
> 01-06
> 01-08
> 01-10
> 01-12
> 01-14
> 01-16
> 01-18
> 01-26
> 01-30
> 02-05
> 02-09
> 02-13
> 02-15
> 02-19
> 12-17
> 12-21
> 12-23
> 12-27
> 12-31
> 01-02
> 01-04
> 01-20
> 01-22
> 01-24
> 01-28
> 02-01
> 02-03
> 02-07
> 02-11
> 02-17
> 02-23
> 02-21
> ~02-16'
> ~02-17
> ~02-18
> ~02-19
> ~02-20
> ~02-22
> 2026-02-23'
> ~02-21
> 2026-
> 2026-
> 2026-
> 2026-C
> 2026-C
> 2026-C
> 2026-0


> 欢迎提出各位大佬使用，欢迎提出需求、优化建议、bug！
> 欢迎 start 和 issue ！
> 后端项目地址： [[链接已屏蔽])
> 前端项目地址： [[链接已屏蔽])

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

给大佬点赞   非常好用且实用

感谢大佬的无私分享！

===================================================================================


---

### 技术对话片段 63 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据.md
- **时间**: 4个月前

**提问/主帖背景 (JG15244)**:
### 项目介绍

定时拉取平台的数据并存储，进行可视化展示。

目前主要进行weight变化、alpha提交情况进行展示，后续会逐步增加更多指标、维度的数据展示（欢迎提出你的需求）。

目前项目仅需通过WQ_ID即可进行登录，目前个性化展示的内容较少，暂未增加账号系统。

> 先已将所有国区ID加入登录名单

### 项目地址

在线地址： [[链接已屏蔽])

后端项目地址： [[链接已屏蔽])

前端项目地址： [[链接已屏蔽])

> 欢迎 start 和 issue

### 部分内容截图


> [!NOTE] [图片 OCR 识别内容]
> 你好。J615244
> 7天
> 15天
> 30天
> 登出
> 数据概览
> 总用户数
> 总ALPHA 数
> 总 INEIG HT
> 数据总量
> 8,169
> 3,264,520
> 128,002.04
> 933,274
> +86变化量
> +37870娈化量
> -1595.64变化量
> 最新数据 2026-02-02 (平台间)
> 选择国家/地区点击标签切换  (至少选择一
> ALL 全部总和
> VN 越南
> IN
> 印度
> CN 中国大陆
> TW
> 中国台湾
> KE 肯尼亚
> GB  英国
> KR 韩国
> ID 印度尼西亚
> SG 新加坡
> HK 中国香港
> MY 马来西亚
> US 美国
> TH 泰国
> AM 亚美尼亚
> HU
> 匈牙利
> NG 尼日利亚
> 国家/地区 Weight 娈化趋势
> 凶 乜03
> 十国大陆
> Weight Factor
> 7538.34
> 7000
> 6000
> 5000
> 4000
> 国家/地区Weight
> 用户Weight
> Genius等级Weight变化
> 越南
> 82688.07
> 眈
> {33369
> 1214.89
> 4007.60
> GRANDMASTER
> VN
> 3062.85(3.6%)
> CN
> 1214.89(100.096)
> 222.67(5.996)
> s
> 人数75
> 7天内娈化
> 印度
> 28303.63
> HN
> HN46545
> 193.97
> IN
> 854.63(2.996)
> TN
> 26.43(15.89)
> 13676.43
> MASTER
> 186.83(-1.496)
> MASTER
> 人数249
> 7天内变化
> 中国大陆
> 7117.74
> DD
> DD65284
> 340.15
> CN
> 1719.36 (31.896)
> TN
> 26.38 (8.496)
> EXPERT
> 18913.41
> 501.96 (-2.696)
> EPERT
> 人数675
> 中国台湾
> 4205.63
> CC
> 顾问 CC40930 (Rank 95)
> 177.58
> 7天内变化
> TTN
> 211.79(5.3961
> TTN
> 19.52(12.三
> GOLD
> 91404.62
> 肯尼亚
> 3081.81
> MC
> MC44186
> 149.35
> 1096.39(1.296)
> K卫
> 341.03(12.496)
> TTV
> 17.03(12.99)
> GSLC
> 人数7167
> 7天内变化
> 英国
> 1085.36
> CT
> 顾问 CT68712 (Rank 27)
> 93.72
> GB
> 6.12 (-0.696)
> TTN
> 16.62(21.6%)
> 01-06
> 01-07
> 01-10
> 01-14
> 01-16'
> 01-17
> 01-04
> 01-05 
> 01-08
> 01-09
> 01-11
> 01-12〉
> 01-13
> 01-15>
> 01-18
> 01-19
> 01-20〉
> 01-21
> 01-22'
> 01-23〉
> 01-24
> 01-25〉
> 01-26'
> 01-27〉
> 01-28
> 01-29〉
> 01-30
> 01-31
> 02-01>
> 02-02
> 3961
  
> [!NOTE] [图片 OCR 识别内容]
> Genius 分析仪表盘
> 刷新数据
> 按 Genius 等级与国家追踪 weight 变化与位置
> 时间范围
> GENIUS 等级
> 国家/地区
> 2026-01-01
> 至
> 2026-03-31
> GRANDMASTER
> CN
> 应用筛选
> 覆盖用户数
> 平均变化
> 中位数变化
> 极值变化区间
> 47
> +7.57
> +5.82
> 0.00
> N
> 31.74
> 总量趋势
> 娈化量分布
> Genius Weight 总和变化
> 凶 乜03
> 娈化量分布
> GRANDMASTER-CN
> Weight 总和
> 20
> 1357.97
> 1300.00
> 15
> 1200.00
> 10
> 1100.00
> 1000.00
> 916.65
> ~2
> @
> 0
> 41
> 个人娈化明细
> 共47人
> 娈化量降序
> 排名
> 用户
> 等级
> 国家
> 起始 WEIGHT
> 当前
> WEIGHT
> 变化量
> 位蹩
> HZ69256
> GRANDMASTER
> CN
> 70.64
> 102.38
> +31.74
> 100.009
> Q068782
> GRANDMASTER
> CN
> 52.72
> 78.47
> +25.75
> 97.839
> ZL35633
> GRANDMASTER
> CN
> 31.81
> 50.55
> +18.74
> 95.659
> WX16829
> GRANDMASTER
> CN
> 106.25
> 124.35
> +18.10
> 93.489
> 顾问 JY88060 (Rank 85)
> GRANDMASTER
> CN
> 33.77
> 51.37
> +17.60
> 1.309
> 0231817
> GRANDMASTER
> CN
> 39.25
> 56.06
> +16.81
> 89.139
> J16510
> GRANDMASTER
> CN
> 39.93
> 56.71
> +16.78
> 696
> 8A51127
> GRANDMASTER
> Cl
> 42.51
> 59.12
> +16.61
> 84.789
> 10
> Aoopzro
> GRNOMAsTER
> CN
> 3215
> 4085
> 41330
> '
> 8259
> 11
> XM75236
> GRANDMASTER
> CN
> 36.44
> 49.36
> +12.92
> 78.269
> 12
> XX42289
> GRANDMASTER
> CN
> 28.65
> 41.37
> +12.72
> 76.099
> 13
> 1479055
> GRANDMASTER
> CN
> 27.01
> 39.35
> +12.34
> 73.919
> 14
> 5283096
> GRANDMASTER
> CN
> 23.16
> 33.61
> +10.45
> 71.749
> 15
> K279256
> GRANDMASTER
> CN
> 120.75
> 130.97
> 10.22
> 69.579
> 16
> 顾问 YH25030 (Rank 31)
> GRANDMASTER
> CN
> 15.81
> 24.52
> 8.71
> 67.399
> 17
> 4871859
> GRANDMASTER
> CN
> 12.21
> 20.67
> 8.46
> 65.229
> 18
> M688592
> GRANDMASTER
> CN
> 26.14
> 33.86
> +7.72
> 63.049
> 19
> INX84677
> GRANDMASTER
> CN
> 17.75
> 25.39
> +7.64
> 60.879
> 20
> NV19619
> GRANDMASTER
> CN
> 20.94
> 28.14
> +7.20
> 58.709
> Total 47
> 0.00~3.97
> 3.97~7.93
> 7.93~11.90
> .90~15.87
> 15.87~19.84
> 19.84~23.80
> 23.80~27.77
> 27.77~31.74
> 01-14〉
> 01-09
> 01-10〉
> 言
> 01-13
> 01-15
> 01-16〉
> 01-17
> 01-18
  
> [!NOTE] [图片 OCR 识别内容]
> 趋势分析
> 查看各国家/地区的 Alpha 提交数量变化趋势 (每天疑似会有alpha消失。暂不确定是因为账号封禁还是alpha退役导致)
> 选择季度:
> 2026-01
> 显示项:
> RA提交
> SA提交
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> IN 印度
> KE 肯尼亚
> CN 中国大陆
> TW 中国台湾
> KR 韩国
> GB 英国
> SG 新加坡
> MY 马来西亚
> NG
> 尼日利亚
> US 美国
> HK 中国香港
> ID  印度尼西亚
> TH
> 泰国
> HU 匈牙利
> AM 亚美尼亚
> Consultant-Alpha 提交数量变化趋势 (2026-01)
> 凶乜93
> CN 中国大陆 R4变化
> CN $国大陆 $4变化
> 娈化二
> 1950
> 1800
> 1500
> 1200
> 900
> 600
> 300
> 选择季度:
> 2026-01
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> CN 中国大陆
> KE 肯尼亚
> IN
> 印度
> TW 中国台湾
> NG 尼日利亚
> KR 韩国
> GB 英国
> MY 马来西亚
> SG 新加坡
> US 美国
> TH
> HK 中国香港
> HU 匈牙利
>  ID 印度尼西亚
> AM 亚美尼亚
> Genius-Alpha提交数量变化趋势 (2026-01)
> 凶乜03
> CN 十国大陆 Alpha数量变化
> Alpha变化量
> 2500
> 2000
> 1500
> 1000
> 500
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-07
> 01-08
> 01-09
> 01-10
> 01-12'
> 01-13 '
> 01-14>
> 01-15
> 01-16
> 01-17
> 01-18
> 01-19
> 01-20
> 01-24>
> 01-25 
> 01-26 
> 01-28
> 01-29〉
> 01-30
> 01-06
> 01-17
> 01-21 
> 01-22
> 01-23
> 01-27
> 01-31
> 02-01
> 02-02
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-06
> 01-07>
> 01-08
> 01-09'
> 01-10
> 01-11
> 01-12〉
> 01-13〉
> 01-14
> 01-15
> 01-16 '
> 01-17
> 01-18
> 01-19'
> 01-20
> 01-21>
> 01-22〉
> 01-23
> 01-24〉
> 01-25〉
> 01-26
> 01-27〉
> 01-28
> 01-29'
> 01-30
> 01-37
> 02-01
> 02-02〉


> 欢迎大家体验，提出需求、bug、优化。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬NB  这得花不少功夫吧

看着非常赏心悦目   也祝自己早日拿到weight哈哈

===================================================================================


---

### 技术对话片段 64 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据.md
- **时间**: 4个月前

**提问/主帖背景 (JG15244)**:
### 项目介绍

定时拉取平台的数据并存储，进行可视化展示。

目前主要进行weight变化、alpha提交情况进行展示，后续会逐步增加更多指标、维度的数据展示（欢迎提出你的需求）。

目前项目仅需通过WQ_ID即可进行登录，目前个性化展示的内容较少，暂未增加账号系统。

> 先已将所有国区ID加入登录名单

### 项目地址

在线地址： [[链接已屏蔽])

后端项目地址： [[链接已屏蔽])

前端项目地址： [[链接已屏蔽])

> 欢迎 start 和 issue

### 部分内容截图


> [!NOTE] [图片 OCR 识别内容]
> 你好。J615244
> 7天
> 15天
> 30天
> 登出
> 数据概览
> 总用户数
> 总ALPHA 数
> 总 INEIG HT
> 数据总量
> 8,169
> 3,264,520
> 128,002.04
> 933,274
> +86变化量
> +37870娈化量
> -1595.64变化量
> 最新数据 2026-02-02 (平台间)
> 选择国家/地区点击标签切换  (至少选择一
> ALL 全部总和
> VN 越南
> IN
> 印度
> CN 中国大陆
> TW
> 中国台湾
> KE 肯尼亚
> GB  英国
> KR 韩国
> ID 印度尼西亚
> SG 新加坡
> HK 中国香港
> MY 马来西亚
> US 美国
> TH 泰国
> AM 亚美尼亚
> HU
> 匈牙利
> NG 尼日利亚
> 国家/地区 Weight 娈化趋势
> 凶 乜03
> 十国大陆
> Weight Factor
> 7538.34
> 7000
> 6000
> 5000
> 4000
> 国家/地区Weight
> 用户Weight
> Genius等级Weight变化
> 越南
> 82688.07
> 眈
> {33369
> 1214.89
> 4007.60
> GRANDMASTER
> VN
> 3062.85(3.6%)
> CN
> 1214.89(100.096)
> 222.67(5.996)
> s
> 人数75
> 7天内娈化
> 印度
> 28303.63
> HN
> HN46545
> 193.97
> IN
> 854.63(2.996)
> TN
> 26.43(15.89)
> 13676.43
> MASTER
> 186.83(-1.496)
> MASTER
> 人数249
> 7天内变化
> 中国大陆
> 7117.74
> DD
> DD65284
> 340.15
> CN
> 1719.36 (31.896)
> TN
> 26.38 (8.496)
> EXPERT
> 18913.41
> 501.96 (-2.696)
> EPERT
> 人数675
> 中国台湾
> 4205.63
> CC
> 顾问 CC40930 (Rank 95)
> 177.58
> 7天内变化
> TTN
> 211.79(5.3961
> TTN
> 19.52(12.三
> GOLD
> 91404.62
> 肯尼亚
> 3081.81
> MC
> MC44186
> 149.35
> 1096.39(1.296)
> K卫
> 341.03(12.496)
> TTV
> 17.03(12.99)
> GSLC
> 人数7167
> 7天内变化
> 英国
> 1085.36
> CT
> 顾问 CT68712 (Rank 27)
> 93.72
> GB
> 6.12 (-0.696)
> TTN
> 16.62(21.6%)
> 01-06
> 01-07
> 01-10
> 01-14
> 01-16'
> 01-17
> 01-04
> 01-05 
> 01-08
> 01-09
> 01-11
> 01-12〉
> 01-13
> 01-15>
> 01-18
> 01-19
> 01-20〉
> 01-21
> 01-22'
> 01-23〉
> 01-24
> 01-25〉
> 01-26'
> 01-27〉
> 01-28
> 01-29〉
> 01-30
> 01-31
> 02-01>
> 02-02
> 3961
  
> [!NOTE] [图片 OCR 识别内容]
> Genius 分析仪表盘
> 刷新数据
> 按 Genius 等级与国家追踪 weight 变化与位置
> 时间范围
> GENIUS 等级
> 国家/地区
> 2026-01-01
> 至
> 2026-03-31
> GRANDMASTER
> CN
> 应用筛选
> 覆盖用户数
> 平均变化
> 中位数变化
> 极值变化区间
> 47
> +7.57
> +5.82
> 0.00
> N
> 31.74
> 总量趋势
> 娈化量分布
> Genius Weight 总和变化
> 凶 乜03
> 娈化量分布
> GRANDMASTER-CN
> Weight 总和
> 20
> 1357.97
> 1300.00
> 15
> 1200.00
> 10
> 1100.00
> 1000.00
> 916.65
> ~2
> @
> 0
> 41
> 个人娈化明细
> 共47人
> 娈化量降序
> 排名
> 用户
> 等级
> 国家
> 起始 WEIGHT
> 当前
> WEIGHT
> 变化量
> 位蹩
> HZ69256
> GRANDMASTER
> CN
> 70.64
> 102.38
> +31.74
> 100.009
> Q068782
> GRANDMASTER
> CN
> 52.72
> 78.47
> +25.75
> 97.839
> ZL35633
> GRANDMASTER
> CN
> 31.81
> 50.55
> +18.74
> 95.659
> WX16829
> GRANDMASTER
> CN
> 106.25
> 124.35
> +18.10
> 93.489
> 顾问 JY88060 (Rank 85)
> GRANDMASTER
> CN
> 33.77
> 51.37
> +17.60
> 1.309
> 0231817
> GRANDMASTER
> CN
> 39.25
> 56.06
> +16.81
> 89.139
> J16510
> GRANDMASTER
> CN
> 39.93
> 56.71
> +16.78
> 696
> 8A51127
> GRANDMASTER
> Cl
> 42.51
> 59.12
> +16.61
> 84.789
> 10
> Aoopzro
> GRNOMAsTER
> CN
> 3215
> 4085
> 41330
> '
> 8259
> 11
> XM75236
> GRANDMASTER
> CN
> 36.44
> 49.36
> +12.92
> 78.269
> 12
> XX42289
> GRANDMASTER
> CN
> 28.65
> 41.37
> +12.72
> 76.099
> 13
> 1479055
> GRANDMASTER
> CN
> 27.01
> 39.35
> +12.34
> 73.919
> 14
> 5283096
> GRANDMASTER
> CN
> 23.16
> 33.61
> +10.45
> 71.749
> 15
> K279256
> GRANDMASTER
> CN
> 120.75
> 130.97
> 10.22
> 69.579
> 16
> 顾问 YH25030 (Rank 31)
> GRANDMASTER
> CN
> 15.81
> 24.52
> 8.71
> 67.399
> 17
> 4871859
> GRANDMASTER
> CN
> 12.21
> 20.67
> 8.46
> 65.229
> 18
> M688592
> GRANDMASTER
> CN
> 26.14
> 33.86
> +7.72
> 63.049
> 19
> INX84677
> GRANDMASTER
> CN
> 17.75
> 25.39
> +7.64
> 60.879
> 20
> NV19619
> GRANDMASTER
> CN
> 20.94
> 28.14
> +7.20
> 58.709
> Total 47
> 0.00~3.97
> 3.97~7.93
> 7.93~11.90
> .90~15.87
> 15.87~19.84
> 19.84~23.80
> 23.80~27.77
> 27.77~31.74
> 01-14〉
> 01-09
> 01-10〉
> 言
> 01-13
> 01-15
> 01-16〉
> 01-17
> 01-18
  
> [!NOTE] [图片 OCR 识别内容]
> 趋势分析
> 查看各国家/地区的 Alpha 提交数量变化趋势 (每天疑似会有alpha消失。暂不确定是因为账号封禁还是alpha退役导致)
> 选择季度:
> 2026-01
> 显示项:
> RA提交
> SA提交
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> IN 印度
> KE 肯尼亚
> CN 中国大陆
> TW 中国台湾
> KR 韩国
> GB 英国
> SG 新加坡
> MY 马来西亚
> NG
> 尼日利亚
> US 美国
> HK 中国香港
> ID  印度尼西亚
> TH
> 泰国
> HU 匈牙利
> AM 亚美尼亚
> Consultant-Alpha 提交数量变化趋势 (2026-01)
> 凶乜93
> CN 中国大陆 R4变化
> CN $国大陆 $4变化
> 娈化二
> 1950
> 1800
> 1500
> 1200
> 900
> 600
> 300
> 选择季度:
> 2026-01
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> CN 中国大陆
> KE 肯尼亚
> IN
> 印度
> TW 中国台湾
> NG 尼日利亚
> KR 韩国
> GB 英国
> MY 马来西亚
> SG 新加坡
> US 美国
> TH
> HK 中国香港
> HU 匈牙利
>  ID 印度尼西亚
> AM 亚美尼亚
> Genius-Alpha提交数量变化趋势 (2026-01)
> 凶乜03
> CN 十国大陆 Alpha数量变化
> Alpha变化量
> 2500
> 2000
> 1500
> 1000
> 500
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-07
> 01-08
> 01-09
> 01-10
> 01-12'
> 01-13 '
> 01-14>
> 01-15
> 01-16
> 01-17
> 01-18
> 01-19
> 01-20
> 01-24>
> 01-25 
> 01-26 
> 01-28
> 01-29〉
> 01-30
> 01-06
> 01-17
> 01-21 
> 01-22
> 01-23
> 01-27
> 01-31
> 02-01
> 02-02
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-06
> 01-07>
> 01-08
> 01-09'
> 01-10
> 01-11
> 01-12〉
> 01-13〉
> 01-14
> 01-15
> 01-16 '
> 01-17
> 01-18
> 01-19'
> 01-20
> 01-21>
> 01-22〉
> 01-23
> 01-24〉
> 01-25〉
> 01-26
> 01-27〉
> 01-28
> 01-29'
> 01-30
> 01-37
> 02-01
> 02-02〉


> 欢迎大家体验，提出需求、bug、优化。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬最近会把Osmosis分数也加入榜单吗

===================================================================================


---

### 技术对话片段 65 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据_38121748548759.md
- **时间**: 4个月前

**提问/主帖背景 (JG15244)**:
### 项目介绍

定时拉取平台的数据并存储，进行可视化展示。

目前主要进行weight变化、alpha提交情况进行展示，后续会逐步增加更多指标、维度的数据展示（欢迎提出你的需求）。

目前项目仅需通过WQ_ID即可进行登录，目前个性化展示的内容较少，暂未增加账号系统。

> 先已将所有国区ID加入登录名单

### 项目地址

在线地址： [[链接已屏蔽])

后端项目地址： [[链接已屏蔽])

前端项目地址： [[链接已屏蔽])

> 欢迎 start 和 issue

### 部分内容截图


> [!NOTE] [图片 OCR 识别内容]
> 你好。J615244
> 7天
> 15天
> 30天
> 登出
> 数据概览
> 总用户数
> 总ALPHA 数
> 总 INEIG HT
> 数据总量
> 8,169
> 3,264,520
> 128,002.04
> 933,274
> +86变化量
> +37870娈化量
> -1595.64变化量
> 最新数据 2026-02-02 (平台间)
> 选择国家/地区点击标签切换  (至少选择一
> ALL 全部总和
> VN 越南
> IN
> 印度
> CN 中国大陆
> TW
> 中国台湾
> KE 肯尼亚
> GB  英国
> KR 韩国
> ID 印度尼西亚
> SG 新加坡
> HK 中国香港
> MY 马来西亚
> US 美国
> TH 泰国
> AM 亚美尼亚
> HU
> 匈牙利
> NG 尼日利亚
> 国家/地区 Weight 娈化趋势
> 凶 乜03
> 十国大陆
> Weight Factor
> 7538.34
> 7000
> 6000
> 5000
> 4000
> 国家/地区Weight
> 用户Weight
> Genius等级Weight变化
> 越南
> 82688.07
> 眈
> {33369
> 1214.89
> 4007.60
> GRANDMASTER
> VN
> 3062.85(3.6%)
> CN
> 1214.89(100.096)
> 222.67(5.996)
> s
> 人数75
> 7天内娈化
> 印度
> 28303.63
> HN
> HN46545
> 193.97
> IN
> 854.63(2.996)
> TN
> 26.43(15.89)
> 13676.43
> MASTER
> 186.83(-1.496)
> MASTER
> 人数249
> 7天内变化
> 中国大陆
> 7117.74
> DD
> DD65284
> 340.15
> CN
> 1719.36 (31.896)
> TN
> 26.38 (8.496)
> EXPERT
> 18913.41
> 501.96 (-2.696)
> EPERT
> 人数675
> 中国台湾
> 4205.63
> CC
> 顾问 CC40930 (Rank 95)
> 177.58
> 7天内变化
> TTN
> 211.79(5.3961
> TTN
> 19.52(12.三
> GOLD
> 91404.62
> 肯尼亚
> 3081.81
> MC
> MC44186
> 149.35
> 1096.39(1.296)
> K卫
> 341.03(12.496)
> TTV
> 17.03(12.99)
> GSLC
> 人数7167
> 7天内变化
> 英国
> 1085.36
> CT
> 顾问 CT68712 (Rank 27)
> 93.72
> GB
> 6.12 (-0.696)
> TTN
> 16.62(21.6%)
> 01-06
> 01-07
> 01-10
> 01-14
> 01-16'
> 01-17
> 01-04
> 01-05 
> 01-08
> 01-09
> 01-11
> 01-12〉
> 01-13
> 01-15>
> 01-18
> 01-19
> 01-20〉
> 01-21
> 01-22'
> 01-23〉
> 01-24
> 01-25〉
> 01-26'
> 01-27〉
> 01-28
> 01-29〉
> 01-30
> 01-31
> 02-01>
> 02-02
> 3961
  
> [!NOTE] [图片 OCR 识别内容]
> Genius 分析仪表盘
> 刷新数据
> 按 Genius 等级与国家追踪 weight 变化与位置
> 时间范围
> GENIUS 等级
> 国家/地区
> 2026-01-01
> 至
> 2026-03-31
> GRANDMASTER
> CN
> 应用筛选
> 覆盖用户数
> 平均变化
> 中位数变化
> 极值变化区间
> 47
> +7.57
> +5.82
> 0.00
> N
> 31.74
> 总量趋势
> 娈化量分布
> Genius Weight 总和变化
> 凶 乜03
> 娈化量分布
> GRANDMASTER-CN
> Weight 总和
> 20
> 1357.97
> 1300.00
> 15
> 1200.00
> 10
> 1100.00
> 1000.00
> 916.65
> ~2
> @
> 0
> 41
> 个人娈化明细
> 共47人
> 娈化量降序
> 排名
> 用户
> 等级
> 国家
> 起始 WEIGHT
> 当前
> WEIGHT
> 变化量
> 位蹩
> HZ69256
> GRANDMASTER
> CN
> 70.64
> 102.38
> +31.74
> 100.009
> Q068782
> GRANDMASTER
> CN
> 52.72
> 78.47
> +25.75
> 97.839
> ZL35633
> GRANDMASTER
> CN
> 31.81
> 50.55
> +18.74
> 95.659
> WX16829
> GRANDMASTER
> CN
> 106.25
> 124.35
> +18.10
> 93.489
> 顾问 JY88060 (Rank 85)
> GRANDMASTER
> CN
> 33.77
> 51.37
> +17.60
> 1.309
> 0231817
> GRANDMASTER
> CN
> 39.25
> 56.06
> +16.81
> 89.139
> J16510
> GRANDMASTER
> CN
> 39.93
> 56.71
> +16.78
> 696
> 8A51127
> GRANDMASTER
> Cl
> 42.51
> 59.12
> +16.61
> 84.789
> 10
> Aoopzro
> GRNOMAsTER
> CN
> 3215
> 4085
> 41330
> '
> 8259
> 11
> XM75236
> GRANDMASTER
> CN
> 36.44
> 49.36
> +12.92
> 78.269
> 12
> XX42289
> GRANDMASTER
> CN
> 28.65
> 41.37
> +12.72
> 76.099
> 13
> 1479055
> GRANDMASTER
> CN
> 27.01
> 39.35
> +12.34
> 73.919
> 14
> 5283096
> GRANDMASTER
> CN
> 23.16
> 33.61
> +10.45
> 71.749
> 15
> K279256
> GRANDMASTER
> CN
> 120.75
> 130.97
> 10.22
> 69.579
> 16
> 顾问 YH25030 (Rank 31)
> GRANDMASTER
> CN
> 15.81
> 24.52
> 8.71
> 67.399
> 17
> 4871859
> GRANDMASTER
> CN
> 12.21
> 20.67
> 8.46
> 65.229
> 18
> M688592
> GRANDMASTER
> CN
> 26.14
> 33.86
> +7.72
> 63.049
> 19
> INX84677
> GRANDMASTER
> CN
> 17.75
> 25.39
> +7.64
> 60.879
> 20
> NV19619
> GRANDMASTER
> CN
> 20.94
> 28.14
> +7.20
> 58.709
> Total 47
> 0.00~3.97
> 3.97~7.93
> 7.93~11.90
> .90~15.87
> 15.87~19.84
> 19.84~23.80
> 23.80~27.77
> 27.77~31.74
> 01-14〉
> 01-09
> 01-10〉
> 言
> 01-13
> 01-15
> 01-16〉
> 01-17
> 01-18
  
> [!NOTE] [图片 OCR 识别内容]
> 趋势分析
> 查看各国家/地区的 Alpha 提交数量变化趋势 (每天疑似会有alpha消失。暂不确定是因为账号封禁还是alpha退役导致)
> 选择季度:
> 2026-01
> 显示项:
> RA提交
> SA提交
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> IN 印度
> KE 肯尼亚
> CN 中国大陆
> TW 中国台湾
> KR 韩国
> GB 英国
> SG 新加坡
> MY 马来西亚
> NG
> 尼日利亚
> US 美国
> HK 中国香港
> ID  印度尼西亚
> TH
> 泰国
> HU 匈牙利
> AM 亚美尼亚
> Consultant-Alpha 提交数量变化趋势 (2026-01)
> 凶乜93
> CN 中国大陆 R4变化
> CN $国大陆 $4变化
> 娈化二
> 1950
> 1800
> 1500
> 1200
> 900
> 600
> 300
> 选择季度:
> 2026-01
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> CN 中国大陆
> KE 肯尼亚
> IN
> 印度
> TW 中国台湾
> NG 尼日利亚
> KR 韩国
> GB 英国
> MY 马来西亚
> SG 新加坡
> US 美国
> TH
> HK 中国香港
> HU 匈牙利
>  ID 印度尼西亚
> AM 亚美尼亚
> Genius-Alpha提交数量变化趋势 (2026-01)
> 凶乜03
> CN 十国大陆 Alpha数量变化
> Alpha变化量
> 2500
> 2000
> 1500
> 1000
> 500
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-07
> 01-08
> 01-09
> 01-10
> 01-12'
> 01-13 '
> 01-14>
> 01-15
> 01-16
> 01-17
> 01-18
> 01-19
> 01-20
> 01-24>
> 01-25 
> 01-26 
> 01-28
> 01-29〉
> 01-30
> 01-06
> 01-17
> 01-21 
> 01-22
> 01-23
> 01-27
> 01-31
> 02-01
> 02-02
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-06
> 01-07>
> 01-08
> 01-09'
> 01-10
> 01-11
> 01-12〉
> 01-13〉
> 01-14
> 01-15
> 01-16 '
> 01-17
> 01-18
> 01-19'
> 01-20
> 01-21>
> 01-22〉
> 01-23
> 01-24〉
> 01-25〉
> 01-26
> 01-27〉
> 01-28
> 01-29'
> 01-30
> 01-37
> 02-01
> 02-02〉


> 欢迎大家体验，提出需求、bug、优化。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬NB  这得花不少功夫吧

看着非常赏心悦目   也祝自己早日拿到weight哈哈

===================================================================================


---

### 技术对话片段 66 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【WQ数据监控】wqmanagerqzzio 一览wq-leaderboard数据_38121748548759.md
- **时间**: 4个月前

**提问/主帖背景 (JG15244)**:
### 项目介绍

定时拉取平台的数据并存储，进行可视化展示。

目前主要进行weight变化、alpha提交情况进行展示，后续会逐步增加更多指标、维度的数据展示（欢迎提出你的需求）。

目前项目仅需通过WQ_ID即可进行登录，目前个性化展示的内容较少，暂未增加账号系统。

> 先已将所有国区ID加入登录名单

### 项目地址

在线地址： [[链接已屏蔽])

后端项目地址： [[链接已屏蔽])

前端项目地址： [[链接已屏蔽])

> 欢迎 start 和 issue

### 部分内容截图


> [!NOTE] [图片 OCR 识别内容]
> 你好。J615244
> 7天
> 15天
> 30天
> 登出
> 数据概览
> 总用户数
> 总ALPHA 数
> 总 INEIG HT
> 数据总量
> 8,169
> 3,264,520
> 128,002.04
> 933,274
> +86变化量
> +37870娈化量
> -1595.64变化量
> 最新数据 2026-02-02 (平台间)
> 选择国家/地区点击标签切换  (至少选择一
> ALL 全部总和
> VN 越南
> IN
> 印度
> CN 中国大陆
> TW
> 中国台湾
> KE 肯尼亚
> GB  英国
> KR 韩国
> ID 印度尼西亚
> SG 新加坡
> HK 中国香港
> MY 马来西亚
> US 美国
> TH 泰国
> AM 亚美尼亚
> HU
> 匈牙利
> NG 尼日利亚
> 国家/地区 Weight 娈化趋势
> 凶 乜03
> 十国大陆
> Weight Factor
> 7538.34
> 7000
> 6000
> 5000
> 4000
> 国家/地区Weight
> 用户Weight
> Genius等级Weight变化
> 越南
> 82688.07
> 眈
> {33369
> 1214.89
> 4007.60
> GRANDMASTER
> VN
> 3062.85(3.6%)
> CN
> 1214.89(100.096)
> 222.67(5.996)
> s
> 人数75
> 7天内娈化
> 印度
> 28303.63
> HN
> HN46545
> 193.97
> IN
> 854.63(2.996)
> TN
> 26.43(15.89)
> 13676.43
> MASTER
> 186.83(-1.496)
> MASTER
> 人数249
> 7天内变化
> 中国大陆
> 7117.74
> DD
> DD65284
> 340.15
> CN
> 1719.36 (31.896)
> TN
> 26.38 (8.496)
> EXPERT
> 18913.41
> 501.96 (-2.696)
> EPERT
> 人数675
> 中国台湾
> 4205.63
> CC
> 顾问 CC40930 (Rank 95)
> 177.58
> 7天内变化
> TTN
> 211.79(5.3961
> TTN
> 19.52(12.三
> GOLD
> 91404.62
> 肯尼亚
> 3081.81
> MC
> MC44186
> 149.35
> 1096.39(1.296)
> K卫
> 341.03(12.496)
> TTV
> 17.03(12.99)
> GSLC
> 人数7167
> 7天内变化
> 英国
> 1085.36
> CT
> 顾问 CT68712 (Rank 27)
> 93.72
> GB
> 6.12 (-0.696)
> TTN
> 16.62(21.6%)
> 01-06
> 01-07
> 01-10
> 01-14
> 01-16'
> 01-17
> 01-04
> 01-05 
> 01-08
> 01-09
> 01-11
> 01-12〉
> 01-13
> 01-15>
> 01-18
> 01-19
> 01-20〉
> 01-21
> 01-22'
> 01-23〉
> 01-24
> 01-25〉
> 01-26'
> 01-27〉
> 01-28
> 01-29〉
> 01-30
> 01-31
> 02-01>
> 02-02
> 3961
  
> [!NOTE] [图片 OCR 识别内容]
> Genius 分析仪表盘
> 刷新数据
> 按 Genius 等级与国家追踪 weight 变化与位置
> 时间范围
> GENIUS 等级
> 国家/地区
> 2026-01-01
> 至
> 2026-03-31
> GRANDMASTER
> CN
> 应用筛选
> 覆盖用户数
> 平均变化
> 中位数变化
> 极值变化区间
> 47
> +7.57
> +5.82
> 0.00
> N
> 31.74
> 总量趋势
> 娈化量分布
> Genius Weight 总和变化
> 凶 乜03
> 娈化量分布
> GRANDMASTER-CN
> Weight 总和
> 20
> 1357.97
> 1300.00
> 15
> 1200.00
> 10
> 1100.00
> 1000.00
> 916.65
> ~2
> @
> 0
> 41
> 个人娈化明细
> 共47人
> 娈化量降序
> 排名
> 用户
> 等级
> 国家
> 起始 WEIGHT
> 当前
> WEIGHT
> 变化量
> 位蹩
> HZ69256
> GRANDMASTER
> CN
> 70.64
> 102.38
> +31.74
> 100.009
> Q068782
> GRANDMASTER
> CN
> 52.72
> 78.47
> +25.75
> 97.839
> ZL35633
> GRANDMASTER
> CN
> 31.81
> 50.55
> +18.74
> 95.659
> WX16829
> GRANDMASTER
> CN
> 106.25
> 124.35
> +18.10
> 93.489
> 顾问 JY88060 (Rank 85)
> GRANDMASTER
> CN
> 33.77
> 51.37
> +17.60
> 1.309
> 0231817
> GRANDMASTER
> CN
> 39.25
> 56.06
> +16.81
> 89.139
> J16510
> GRANDMASTER
> CN
> 39.93
> 56.71
> +16.78
> 696
> 8A51127
> GRANDMASTER
> Cl
> 42.51
> 59.12
> +16.61
> 84.789
> 10
> Aoopzro
> GRNOMAsTER
> CN
> 3215
> 4085
> 41330
> '
> 8259
> 11
> XM75236
> GRANDMASTER
> CN
> 36.44
> 49.36
> +12.92
> 78.269
> 12
> XX42289
> GRANDMASTER
> CN
> 28.65
> 41.37
> +12.72
> 76.099
> 13
> 1479055
> GRANDMASTER
> CN
> 27.01
> 39.35
> +12.34
> 73.919
> 14
> 5283096
> GRANDMASTER
> CN
> 23.16
> 33.61
> +10.45
> 71.749
> 15
> K279256
> GRANDMASTER
> CN
> 120.75
> 130.97
> 10.22
> 69.579
> 16
> 顾问 YH25030 (Rank 31)
> GRANDMASTER
> CN
> 15.81
> 24.52
> 8.71
> 67.399
> 17
> 4871859
> GRANDMASTER
> CN
> 12.21
> 20.67
> 8.46
> 65.229
> 18
> M688592
> GRANDMASTER
> CN
> 26.14
> 33.86
> +7.72
> 63.049
> 19
> INX84677
> GRANDMASTER
> CN
> 17.75
> 25.39
> +7.64
> 60.879
> 20
> NV19619
> GRANDMASTER
> CN
> 20.94
> 28.14
> +7.20
> 58.709
> Total 47
> 0.00~3.97
> 3.97~7.93
> 7.93~11.90
> .90~15.87
> 15.87~19.84
> 19.84~23.80
> 23.80~27.77
> 27.77~31.74
> 01-14〉
> 01-09
> 01-10〉
> 言
> 01-13
> 01-15
> 01-16〉
> 01-17
> 01-18
  
> [!NOTE] [图片 OCR 识别内容]
> 趋势分析
> 查看各国家/地区的 Alpha 提交数量变化趋势 (每天疑似会有alpha消失。暂不确定是因为账号封禁还是alpha退役导致)
> 选择季度:
> 2026-01
> 显示项:
> RA提交
> SA提交
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> IN 印度
> KE 肯尼亚
> CN 中国大陆
> TW 中国台湾
> KR 韩国
> GB 英国
> SG 新加坡
> MY 马来西亚
> NG
> 尼日利亚
> US 美国
> HK 中国香港
> ID  印度尼西亚
> TH
> 泰国
> HU 匈牙利
> AM 亚美尼亚
> Consultant-Alpha 提交数量变化趋势 (2026-01)
> 凶乜93
> CN 中国大陆 R4变化
> CN $国大陆 $4变化
> 娈化二
> 1950
> 1800
> 1500
> 1200
> 900
> 600
> 300
> 选择季度:
> 2026-01
> 选择国家/地区点击标签切换 (至少选择一项)
> VN 越南
> CN 中国大陆
> KE 肯尼亚
> IN
> 印度
> TW 中国台湾
> NG 尼日利亚
> KR 韩国
> GB 英国
> MY 马来西亚
> SG 新加坡
> US 美国
> TH
> HK 中国香港
> HU 匈牙利
>  ID 印度尼西亚
> AM 亚美尼亚
> Genius-Alpha提交数量变化趋势 (2026-01)
> 凶乜03
> CN 十国大陆 Alpha数量变化
> Alpha变化量
> 2500
> 2000
> 1500
> 1000
> 500
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-07
> 01-08
> 01-09
> 01-10
> 01-12'
> 01-13 '
> 01-14>
> 01-15
> 01-16
> 01-17
> 01-18
> 01-19
> 01-20
> 01-24>
> 01-25 
> 01-26 
> 01-28
> 01-29〉
> 01-30
> 01-06
> 01-17
> 01-21 
> 01-22
> 01-23
> 01-27
> 01-31
> 02-01
> 02-02
> 01-01
> 01-02
> 01-03
> 01-04
> 01-05
> 01-06
> 01-07>
> 01-08
> 01-09'
> 01-10
> 01-11
> 01-12〉
> 01-13〉
> 01-14
> 01-15
> 01-16 '
> 01-17
> 01-18
> 01-19'
> 01-20
> 01-21>
> 01-22〉
> 01-23
> 01-24〉
> 01-25〉
> 01-26
> 01-27〉
> 01-28
> 01-29'
> 01-30
> 01-37
> 02-01
> 02-02〉


> 欢迎大家体验，提出需求、bug、优化。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬最近会把Osmosis分数也加入榜单吗

===================================================================================


---

### 技术对话片段 67 (原帖: 【大角羊】一分钟掌握参加Orthogonal HTVR Theme要点（三倍加成）！)
- **原帖链接**: [Commented] 【大角羊】一分钟掌握参加Orthogonal HTVR Theme要点三倍加成.md
- **时间**: 2个月前

**提问/主帖背景 (AL13375)**:

> [!NOTE] [图片 OCR 识别内容]
> NEW THEME
> 4月138
> 4月26曰 (2周)
> Orthogonal HTVR Theme
> 正交高换手率主题
> 正交高换手 Alpha 的本质
> 是研究 短周期内仍然经济有效 的信息
> Turnover 应该是  机制的自然结果
> 而不是把 "换手" 当作目标去硬优化
> 加成系数
> 适用地区
> 3
> USA
> Alpha 准入要求
> REGION
> USA
> NEUTRALIZATION
> RAM(REVERSION_AND_MOMENTUM)
> TURNOVER
> 20%
> PERFORMANCE
> High Turnover returns ratio
> >
> 0.75
> 0R
> Pnl Realization
> 20



> [!NOTE] [图片 OCR 识别内容]
> SECTION 01
> 高换手率 Alpha 的重要性
> 多样化收益 (Diversification)
> 信号新鲜度 (Signal Freshness)
> 具有不同的收益特征。与传统低换手率信号的相关性
> 较短的预测周期意味着信号衰减更快。能更迅速地捕
> 较低。
> 捉新信息。
> 互补性方案 (Complementary)
> 为现有投资组合构建提供正交的收益来源。



> [!NOTE] [图片 OCR 识别内容]
> SECTION 02
> 高换手率 Alpha 的特征
> 快速更新
> 表现分布'匀
> 信号更新速度足够快
> 足以支撑频繁的重新排名或调
> 收益不集中在极少数日期或特定标的上。
> 仓
> 符合现实约束
> 经济逻辑清晰
> 在应用现实约束或更具投资性的设置后, Alpha 依然
> 能够解释为什么信息会迅速产生并快速衰减。
> 合理。



> [!NOTE] [图片 OCR 识别内容]
> SECTION 03 
> 开发流程 (Workflow)
> Step 1: 构建简洁基准
> 从简单结构开始。避免在首个版本中堆叠过多的转换或交互。
> 2
> 2: 验证信号机制
> 检查信号娈动频率是否足够,
> 覆盖范围是否合理。
> 3
> Step 3: 观察换手率产出
> 换手率应是自然结果
> 而非通过添加噪声或不稳定转换强行提高。
> 4
> Step 4: 现实变体稳健性测试
> 测试扣除成本后的表现。在流动性子集中的表现及正交化后的表现。
> 5
> Step 5: 核心逻辑存活后再扩展
> 在基准版本可信后,
> 再探索不同的归一化。行业中性等娈体。
> Step



> [!NOTE] [图片 OCR 识别内容]
> SECTION 04
> 开发建议 (Actionable Tips)
> 偏好"娈化"而非"水平
> 谨慎使用条件逻辑
> Deltas: Surprises。 加速项等构造通常比静态水平值
> 利用流动性。关注度或事件状态进行门控 
> 帮助信号
> 更适合短周期。
> 在最合理的机制下生效。
> 横截面思考
> 尊重现实市场条件
> 许多高换手思路在相对价值排名中表现最强。而非绝
> 仅在流动性最差的股票尾部生效的信号实用性较低。
> 对阈值。
> 追求简单可重复的构造
> 如果你无法解释某个转换为何有效。那它很可能是过
> 拟合。



> [!NOTE] [图片 OCR 识别内容]
> SECTION 05
> 分类标准 (Classifications)
> 基础准入
> 扣费后 Alpha (After Cost)
> USA 地区;换手率 >20%,收益留存率 >0.75
> 扣除执行成本后的
> 1.0
> 可投资性 Alpha (Investable)
> 流动性 Alpha (Liquid)
> 在严格限制(maxtrade/maxpos)下
> 2.0且
> 在 TOP2O0 标的中
> 1.0
> 换手率
> 209
> 正交 Alpha (Orthogonal)
> 应用 RAM 中性化后仍可提交
> Sharpe
> Sharpe
> Sharpe
  
> [!NOTE] [图片 OCR 识别内容]
> SECTION 06
> 常见风险 (Risks)
> 人为换手率 (Artificial TVR)
> 单次测试依赖
> 因信号噪声大。不稳定或过度反应导致
> 而非信息驱
> 仅在特定宇宙。特定成本假设或特定约束设置下表现
> 动。
> 良好。
> 经济故事薄弱
> 覆盖脆弱性
> Alpha 只是算子的堆砌。缺乏短周期预测能力的逻辑
> 仅对极窄范围的股票或日期有效。
> 支撑。
> 参数挖掘 (Mining)
> 对窗口期或排名的微小调整会导致结果剧烈波动。
  
> [!NOTE] [图片 OCR 识别内容]
> SECTION 07
> 自查点 (Self-check)
> 自然达标
> 短周期逻辑
> Alpha 是否自然运行在 20% 换手率阈值以上?
> 是否有明确的短周期原因支撑该信号生效?
> 现实意识
> 参数稳健
> 是否在至少个"现实意识"方向 (如扣费)  检查过该
> 表现是否不完全依赖于某个脆弱的参数选择?
> 想法?
> 数据匹配
> 一句话解释
> 所选数据集对于快速衰减的信号是否合理?
> 能否用一两句话解释该 Alpha 捕捉到了什么?


最后，大角羊预祝诸位顾问大佬们在新主题期间做出高质量的主题RA，每天的OSM都能节节高，拿到心满意足的高BASE！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

大佬有推荐的数据集吗

试了几个感觉效果都不是很好

=============================================================================


---

### 技术对话片段 68 (原帖: 【大角羊】一分钟掌握参加Orthogonal HTVR Theme要点（三倍加成）！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【大角羊】一分钟掌握参加Orthogonal HTVR Theme要点三倍加成_39690289189015.md
- **时间**: 2个月前

**提问/主帖背景 (AL13375)**:

> [!NOTE] [图片 OCR 识别内容]
> NEW THEME
> 4月138
> 4月26曰 (2周)
> Orthogonal HTVR Theme
> 正交高换手率主题
> 正交高换手 Alpha 的本质
> 是研究 短周期内仍然经济有效 的信息
> Turnover 应该是  机制的自然结果
> 而不是把 "换手" 当作目标去硬优化
> 加成系数
> 适用地区
> 3
> USA
> Alpha 准入要求
> REGION
> USA
> NEUTRALIZATION
> RAM(REVERSION_AND_MOMENTUM)
> TURNOVER
> 20%
> PERFORMANCE
> High Turnover returns ratio
> >
> 0.75
> 0R
> Pnl Realization
> 20



> [!NOTE] [图片 OCR 识别内容]
> SECTION 01
> 高换手率 Alpha 的重要性
> 多样化收益 (Diversification)
> 信号新鲜度 (Signal Freshness)
> 具有不同的收益特征。与传统低换手率信号的相关性
> 较短的预测周期意味着信号衰减更快。能更迅速地捕
> 较低。
> 捉新信息。
> 互补性方案 (Complementary)
> 为现有投资组合构建提供正交的收益来源。



> [!NOTE] [图片 OCR 识别内容]
> SECTION 02
> 高换手率 Alpha 的特征
> 快速更新
> 表现分布'匀
> 信号更新速度足够快
> 足以支撑频繁的重新排名或调
> 收益不集中在极少数日期或特定标的上。
> 仓
> 符合现实约束
> 经济逻辑清晰
> 在应用现实约束或更具投资性的设置后, Alpha 依然
> 能够解释为什么信息会迅速产生并快速衰减。
> 合理。



> [!NOTE] [图片 OCR 识别内容]
> SECTION 03 
> 开发流程 (Workflow)
> Step 1: 构建简洁基准
> 从简单结构开始。避免在首个版本中堆叠过多的转换或交互。
> 2
> 2: 验证信号机制
> 检查信号娈动频率是否足够,
> 覆盖范围是否合理。
> 3
> Step 3: 观察换手率产出
> 换手率应是自然结果
> 而非通过添加噪声或不稳定转换强行提高。
> 4
> Step 4: 现实变体稳健性测试
> 测试扣除成本后的表现。在流动性子集中的表现及正交化后的表现。
> 5
> Step 5: 核心逻辑存活后再扩展
> 在基准版本可信后,
> 再探索不同的归一化。行业中性等娈体。
> Step



> [!NOTE] [图片 OCR 识别内容]
> SECTION 04
> 开发建议 (Actionable Tips)
> 偏好"娈化"而非"水平
> 谨慎使用条件逻辑
> Deltas: Surprises。 加速项等构造通常比静态水平值
> 利用流动性。关注度或事件状态进行门控 
> 帮助信号
> 更适合短周期。
> 在最合理的机制下生效。
> 横截面思考
> 尊重现实市场条件
> 许多高换手思路在相对价值排名中表现最强。而非绝
> 仅在流动性最差的股票尾部生效的信号实用性较低。
> 对阈值。
> 追求简单可重复的构造
> 如果你无法解释某个转换为何有效。那它很可能是过
> 拟合。



> [!NOTE] [图片 OCR 识别内容]
> SECTION 05
> 分类标准 (Classifications)
> 基础准入
> 扣费后 Alpha (After Cost)
> USA 地区;换手率 >20%,收益留存率 >0.75
> 扣除执行成本后的
> 1.0
> 可投资性 Alpha (Investable)
> 流动性 Alpha (Liquid)
> 在严格限制(maxtrade/maxpos)下
> 2.0且
> 在 TOP2O0 标的中
> 1.0
> 换手率
> 209
> 正交 Alpha (Orthogonal)
> 应用 RAM 中性化后仍可提交
> Sharpe
> Sharpe
> Sharpe
  
> [!NOTE] [图片 OCR 识别内容]
> SECTION 06
> 常见风险 (Risks)
> 人为换手率 (Artificial TVR)
> 单次测试依赖
> 因信号噪声大。不稳定或过度反应导致
> 而非信息驱
> 仅在特定宇宙。特定成本假设或特定约束设置下表现
> 动。
> 良好。
> 经济故事薄弱
> 覆盖脆弱性
> Alpha 只是算子的堆砌。缺乏短周期预测能力的逻辑
> 仅对极窄范围的股票或日期有效。
> 支撑。
> 参数挖掘 (Mining)
> 对窗口期或排名的微小调整会导致结果剧烈波动。
  
> [!NOTE] [图片 OCR 识别内容]
> SECTION 07
> 自查点 (Self-check)
> 自然达标
> 短周期逻辑
> Alpha 是否自然运行在 20% 换手率阈值以上?
> 是否有明确的短周期原因支撑该信号生效?
> 现实意识
> 参数稳健
> 是否在至少个"现实意识"方向 (如扣费)  检查过该
> 表现是否不完全依赖于某个脆弱的参数选择?
> 想法?
> 数据匹配
> 一句话解释
> 所选数据集对于快速衰减的信号是否合理?
> 能否用一两句话解释该 Alpha 捕捉到了什么?


最后，大角羊预祝诸位顾问大佬们在新主题期间做出高质量的主题RA，每天的OSM都能节节高，拿到心满意足的高BASE！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

大佬有推荐的数据集吗

试了几个感觉效果都不是很好

=============================================================================


---

### 技术对话片段 69 (原帖: 【工具分享】Pkgdiff：在线免费给cnhkmcp做版本差异分析)
- **原帖链接**: [Commented] 【工具分享】Pkgdiff在线免费给cnhkmcp做版本差异分析.md
- **时间**: 1个月前

**提问/主帖背景 (ZH74761)**:
上次做了一个小工具 [追踪每一次cnhkmcp的更新]( [[L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md]([L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md)  )，但还是有一些不人性化的地方，比如需要手动操作可能会破坏本地的代码，以及就算有版本diff也并看不懂的问题。于是诞生了这次新做的在线版本： [[链接已屏蔽])

**起因**

升级一个 Python 依赖之前，正常的流程是去 GitHub 翻 changelog或 release notes。但实际上经常会遇到几种情况：

- 包根本没有公开源码仓库
- 仓库存在但跟 PyPI 上发布的 wheel 已经不一致（构建脚本生成、私有 patch、被 fork 后改名上传等）
- 仓库的 release notes 写得极其敷衍，只有 "bugfixes and improvements"

这些场景下，唯一可信的事实来源就是 PyPI 上那个 wheel/sdist 本身。pkgdiff 就是奔着这个前提做的：不假设有 git 历史、不假设有 changelog，只看两个版本的发布产物。

**它做什么**

给定 (package, from_version, to_version)，输出一份结构化的 diff 报告：

1. **文件级 diff**  — 每个文件 added / removed / modified，文本文件给出 unified diff，二进制（.so / .pyd）只标记内容变化
2. **公共 API surface diff** — 加载两个版本的源码，对比模块、类、函数、属性的增删改，识别函数签名变化，标注哪些是 breaking
3. **元数据 diff** — Requires-Dist、Requires-Python、license、classifiers、entry points 的逐项变化
4. **LLM 摘要** — 把上面三段结构化 diff 喂给 LLM，生成一份人类可读的 Markdown 变更说明 + breaking-change brief

**第 4 点**  是关键的"最后一公里",也正是和前一篇内容的差别。前三个 analyzer 已经把"发生了什么"用机器可读的格式还原出来了，但人类升级依赖时真正想知道的是"这个变化会不会影响我"。LLM 在这里不负责发现事实，只负责把已经被严格挖出来的事实翻译成自然语言。

同时它还支持 Stepwise 模式。普通模式做 2.30.0 → 2.31.0 的 diff。但有时你跨了 5 个版本，把所有变化压成一个 diff 会丢失节奏感——你不知道 breaking change 是在哪个中间版本引入的。

Stepwise 模式给定一个版本序列，对每对相邻版本各跑一次完整 pipeline，最后再用一个汇总 LLM 调用把 N 份分步摘要合成一份统一的 changelog。

这个服务可以免费使用，且不需要注册！不仅针对cnhkmcp，也可以是任何python package. 大家有什么想法和建议欢迎评论~


> [!NOTE] [图片 OCR 识别内容]
> See What actually changed
> between two package versions。
> Don't trust hand-written changelogs. Pkgdiff reads the published artifacts directly and tells you
> exactly What's different
> public API, dependencies, files
> with an Al-written summary on
> ECOSYSTEM
> Python
> PACKAGE
> cnhkmcp
> FROM
> TO
> 2.3.18
> 3.1.11
> Add AI summary
> Step through every version
> 14 steps
> Analyze
> Currently supports Python
> tOP.



> [!NOTE] [图片 OCR 识别内容]
> CNHKMCP
> 2.3.18
> 3.1.11
> cnhkmcp
> 2.3.18
> 3.1.11
> breaking
> Overview
> 14steps
> 14 version steps
> 14 with breaking changes
> 2.3.18
> 2.3.19
> PUBLIC SYMBOLS
> API CHURN (SUM)
> BREAKING-API COUNT
> FILE OPS (SUM)
> 2.3.19
> 2.3.20
> 5
> 5
> +0
> -0
> ~0
> +10719
> -10183
> ~250
> 2.3.28
> 3.0.0
> 3.8.0
> 3.1.8
> 3.1.0
> 3.1.1
> Changelog
> 2.3.18
> 3.1.11
> 3.1.1
> 3.1.2
> Summary
> 3.1.2
> 3.1.3
> This upgrade is mostly about the app's embedded workflow tools rather than the importable Python APl. Across the range;
> cnhkmcp   grows from
> a small
> packaging refresh into
> a much broader BRAIN/orchestrator platform with pipeline lifecycle
> 3.1.3
> 3.1.4
> controls; prompt customization, simulation/status improvements;, credential/session persistence; and richer operator catalogs。
> 3.1.4
> 3.1.5
> The web UI also changes substantially: new dashboards and modal controls appear; some flows are reworked for better
> persistence and visibility, and the landing page is reorganized around the main BRAIN workflows. Operators using the pipeline
> 3.1.5
> 3.1.6
> Ul, simulator tooling, alpha submission paths, or generated formulas should review this upgrade carefully:
> 3.1.6
> 3.1.7
> New features
> 3.1.7
> 3.1.9
> Added and expanded the
> brain-orchestrator
> control plane under
> cnhkmcp /untracked /APP /brain-orchestrator /
> including
> 3.1.9
> 3.1.18
> pipeline runner/state management; stage modules
> stage_decide.py
> stage_enhance. Py
> stage_implement .py
> stage_inspect . Py
> stage
> simulate. py
> ) and dashboard docs/templates。
> 3.1.18
> 3.1.11
> Added pipeline lifecycle endpoints and UI actions for: delete, archive; restore, and list archived pipelines force-restart ofa
> pipeline via
> POST /api/pipeline/pipeline_id>
> force-restart
> updating stop conditions at runtime via
> POST
> /api/pipeline /<pipeline_id> /update-stop-conditions
> Added prompt-preview and prompt-editing support in the pipeline dashboard, including a phase-prompt preview endpoint
> and an advanced prompt/settings modal。
> Added structured stop-condition support for pipeline runs; including:  sharpe_target
> count
> pool_ideas
> max_alpha_
> submitted
> max_sim_completed
> max_iterations
> diminishing_returns
> optional
> use_abs
> for Sharpe
> thresholding
> Expanded
> trailSomeAlphas
> generation and enhancement workflows:
> implement
> idea.py
> DOW
> supports
> idea
> run_pipeline. Py
> HOW
> supports prompt overrides; adaptive retry on token-limit failures; and full-field prompting when
> max-fields
> is omitted
> enhance_template. py
> supports single-mode and cross-mode enhancement; with style instructions Via
> CROSS
> PROMPT_STYLES
> the cross-enhance UI now supports multiple uploaded idea files and selectable cross styles manual
> "Cross 手动输入
> Workflow documentation Was added
> Added environment propagation for universe-aware enhancement; including
> UNIVERSE
> being passed into subprocesses so
> manual and automated enhancement target the same stock pool。
> Added pipeline-level LLM request accounting:
> record_Ilm_request(
> summarize_IIm_requests
> Ilm_requests .jsonl
> artifacts per pipeline per-stage tagging for
> generate
> inspect
> enhance
> and
> decide
> max_



> [!NOTE] [图片 OCR 识别内容]
> cnhkmcp
> 3.1.10
> 3.1.11
> breaking changes
> pypi . generated 5/5/2026,4:37:53 PM
> API SYMBOLS
> API CHANGES
> DEPENDENCY ENTRIES CHANGED
> FILES (OLD
> NEW)
> 5
> 5
> +0
> -0
> ~0
> 949
> 949
> Export Markdown
> Export PDF
> Summary
> API
> Metadata
> Files
> 20
> Summary
> Summary
> cnhkmcp 3.1.11 is a UI- and operator-catalog-focused release. The package keeps the same public Python API surface; but several front-end workflows were refactored and
> the supported operator list changed. Engineers using the web UIor generating formulas from
> Vvalidop.json
> should review this upgrade carefully:
> New features
> Added a new simulator
> pointin
> cnhkmcp /untracked/APP _
> static /script.js
> runHKFacesimulator( )
> wired to a new
> 命令行页面 (人脸识别版)" option in the
> 'Run
> Simulator'
> modal
> Expanded the operator catalog in
> cnhkmcp
> untracked /APP /validop .json
> with new operators:
> pasteurize(x)
> ts
> returns (X,
> 4,
> mode
> 1 )
> group_count(x,
> group )
> group_std_dev(x,
> group )
> group_sum(x,
> group )
> Refactored the landing page in
> cnhkmcp /untracked/APP / templates
> index.html
> into staged sections for the main workflows, making the Alpha judge; Alpha submitter, and
> pipeline entry points more prominent:
> cnhkmcp_
> untracked
> APP
> static /inspiration.js
> now binds the inspiration modal to any
> inspiration-trigger
> element; allowing multiple UI entry points instead ofa
> single hard-coded button.
> fixes
> In
> cnhkmcp
> untracked/APP / 运行打开我 . Py
> credential caching now fails gracefully: writing ACE credentials to local disk is wrapped in
> try/except
> and Iogs a
> warning
> instead of raising.
> The pipeline credential sync
> in
> cnhkmcp /untracked/APP / 运行打开我 . Py
> is also guarded so local pipeline updates do not crash the process if an internal error occurs:
> Task lookup endpoints in
> cnhkmcp
> untracked/APP / 运行打开我. Py
> now return clearer JSON errors When a task is missing or when
> day_key
> is absent; replacing the previous
> garbled messages。
> The Alpha Inspector import pathlcomment in
> cnhkmcp /untracked/APP / 运行打开我 . Py
> Was corrected to Use
> 缘分
> 道桥
> Which should make the route setup easier to
> understand and maintain。
> Behavior & deprecations
> cnhkmcp /untracked/APP
> static /inspiration.js
> now enables/disables all
> inspiration-trigger
> buttons based on login state; rather than targeting a single
> entry
> Bug
> path



> [!NOTE] [图片 OCR 识别内容]
> Summary
> API
> Metadata
> Files
> 20
> 949
> 949 files
> +6 -6 ~8
> all
> added
> removed
> modified
> cnhkmcp/ _
> init_.Py
> cnhkmcp /untracked/APP
> ace
> cnhkmcp /untracked/APP _
> static /inspiration.js
> cnhkmcp /untracked/APP _
> static /script.js
> cnhkmcp /untracked/APP_
> static /styles _
> CSS
> cnhkmcp /untracked/APP / templates _
> index.html
> cnhkmcp /untracked/APP /validop .json
> cnhkmcp /untracked/APP _
> /运行打开我. py
> 285,7
> +285,18
> 285
> 285
> password
> str(password
> Or
> ).strip()
> 286
> 286
> i
> not
> Username
> Or
> not password:
> 287
> 287
> return
> 288
> WT
> ~ite_json_file(_ace_credentials_path(),
> {'email'
> username,
> password
> password} )
> 288
> try:
> 289
> Write_json_file(_ace_
> credentials_path(),
> {'email'
> username,
> password 
> password})
> 290
> except Exception
> as
> e:
> 291
> print (f"
> Warning:
> Could
> not
> cache
> credentials to
> local
> disk:
> {e}")
> 289
> 292
> 290
> 293
> 291
> 294
> def
> sync_pipeline_credentials (username
> password:
> str):
> 297,19 +380,22
> 297
> 300
> return
> 298
> 301
> 299
> 302
> updated
> 300
> for
> item
> in
> list pipelines()
> 1o8
> str,


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！ 作为代码小白总是不知道CNHKMCP每次更新了啥

这下一眼就能看出来了

=============================================================================


---

### 技术对话片段 70 (原帖: 【工具分享】Pkgdiff：在线免费给cnhkmcp做版本差异分析)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【工具分享】Pkgdiff在线免费给cnhkmcp做版本差异分析_40292420301591.md
- **时间**: 1个月前

**提问/主帖背景 (ZH74761)**:
上次做了一个小工具 [追踪每一次cnhkmcp的更新]( [[L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md]([L2] [工具分享] 追踪每一次cnhkmcp的更新_37760428555287.md)  )，但还是有一些不人性化的地方，比如需要手动操作可能会破坏本地的代码，以及就算有版本diff也并看不懂的问题。于是诞生了这次新做的在线版本： [[链接已屏蔽])

**起因**

升级一个 Python 依赖之前，正常的流程是去 GitHub 翻 changelog或 release notes。但实际上经常会遇到几种情况：

- 包根本没有公开源码仓库
- 仓库存在但跟 PyPI 上发布的 wheel 已经不一致（构建脚本生成、私有 patch、被 fork 后改名上传等）
- 仓库的 release notes 写得极其敷衍，只有 "bugfixes and improvements"

这些场景下，唯一可信的事实来源就是 PyPI 上那个 wheel/sdist 本身。pkgdiff 就是奔着这个前提做的：不假设有 git 历史、不假设有 changelog，只看两个版本的发布产物。

**它做什么**

给定 (package, from_version, to_version)，输出一份结构化的 diff 报告：

1. **文件级 diff**  — 每个文件 added / removed / modified，文本文件给出 unified diff，二进制（.so / .pyd）只标记内容变化
2. **公共 API surface diff** — 加载两个版本的源码，对比模块、类、函数、属性的增删改，识别函数签名变化，标注哪些是 breaking
3. **元数据 diff** — Requires-Dist、Requires-Python、license、classifiers、entry points 的逐项变化
4. **LLM 摘要** — 把上面三段结构化 diff 喂给 LLM，生成一份人类可读的 Markdown 变更说明 + breaking-change brief

**第 4 点**  是关键的"最后一公里",也正是和前一篇内容的差别。前三个 analyzer 已经把"发生了什么"用机器可读的格式还原出来了，但人类升级依赖时真正想知道的是"这个变化会不会影响我"。LLM 在这里不负责发现事实，只负责把已经被严格挖出来的事实翻译成自然语言。

同时它还支持 Stepwise 模式。普通模式做 2.30.0 → 2.31.0 的 diff。但有时你跨了 5 个版本，把所有变化压成一个 diff 会丢失节奏感——你不知道 breaking change 是在哪个中间版本引入的。

Stepwise 模式给定一个版本序列，对每对相邻版本各跑一次完整 pipeline，最后再用一个汇总 LLM 调用把 N 份分步摘要合成一份统一的 changelog。

这个服务可以免费使用，且不需要注册！不仅针对cnhkmcp，也可以是任何python package. 大家有什么想法和建议欢迎评论~


> [!NOTE] [图片 OCR 识别内容]
> See What actually changed
> between two package versions。
> Don't trust hand-written changelogs. Pkgdiff reads the published artifacts directly and tells you
> exactly What's different
> public API, dependencies, files
> with an Al-written summary on
> ECOSYSTEM
> Python
> PACKAGE
> cnhkmcp
> FROM
> TO
> 2.3.18
> 3.1.11
> Add AI summary
> Step through every version
> 14 steps
> Analyze
> Currently supports Python
> tOP.



> [!NOTE] [图片 OCR 识别内容]
> CNHKMCP
> 2.3.18
> 3.1.11
> cnhkmcp
> 2.3.18
> 3.1.11
> breaking
> Overview
> 14steps
> 14 version steps
> 14 with breaking changes
> 2.3.18
> 2.3.19
> PUBLIC SYMBOLS
> API CHURN (SUM)
> BREAKING-API COUNT
> FILE OPS (SUM)
> 2.3.19
> 2.3.20
> 5
> 5
> +0
> -0
> ~0
> +10719
> -10183
> ~250
> 2.3.28
> 3.0.0
> 3.8.0
> 3.1.8
> 3.1.0
> 3.1.1
> Changelog
> 2.3.18
> 3.1.11
> 3.1.1
> 3.1.2
> Summary
> 3.1.2
> 3.1.3
> This upgrade is mostly about the app's embedded workflow tools rather than the importable Python APl. Across the range;
> cnhkmcp   grows from
> a small
> packaging refresh into
> a much broader BRAIN/orchestrator platform with pipeline lifecycle
> 3.1.3
> 3.1.4
> controls; prompt customization, simulation/status improvements;, credential/session persistence; and richer operator catalogs。
> 3.1.4
> 3.1.5
> The web UI also changes substantially: new dashboards and modal controls appear; some flows are reworked for better
> persistence and visibility, and the landing page is reorganized around the main BRAIN workflows. Operators using the pipeline
> 3.1.5
> 3.1.6
> Ul, simulator tooling, alpha submission paths, or generated formulas should review this upgrade carefully:
> 3.1.6
> 3.1.7
> New features
> 3.1.7
> 3.1.9
> Added and expanded the
> brain-orchestrator
> control plane under
> cnhkmcp /untracked /APP /brain-orchestrator /
> including
> 3.1.9
> 3.1.18
> pipeline runner/state management; stage modules
> stage_decide.py
> stage_enhance. Py
> stage_implement .py
> stage_inspect . Py
> stage
> simulate. py
> ) and dashboard docs/templates。
> 3.1.18
> 3.1.11
> Added pipeline lifecycle endpoints and UI actions for: delete, archive; restore, and list archived pipelines force-restart ofa
> pipeline via
> POST /api/pipeline/pipeline_id>
> force-restart
> updating stop conditions at runtime via
> POST
> /api/pipeline /<pipeline_id> /update-stop-conditions
> Added prompt-preview and prompt-editing support in the pipeline dashboard, including a phase-prompt preview endpoint
> and an advanced prompt/settings modal。
> Added structured stop-condition support for pipeline runs; including:  sharpe_target
> count
> pool_ideas
> max_alpha_
> submitted
> max_sim_completed
> max_iterations
> diminishing_returns
> optional
> use_abs
> for Sharpe
> thresholding
> Expanded
> trailSomeAlphas
> generation and enhancement workflows:
> implement
> idea.py
> DOW
> supports
> idea
> run_pipeline. Py
> HOW
> supports prompt overrides; adaptive retry on token-limit failures; and full-field prompting when
> max-fields
> is omitted
> enhance_template. py
> supports single-mode and cross-mode enhancement; with style instructions Via
> CROSS
> PROMPT_STYLES
> the cross-enhance UI now supports multiple uploaded idea files and selectable cross styles manual
> "Cross 手动输入
> Workflow documentation Was added
> Added environment propagation for universe-aware enhancement; including
> UNIVERSE
> being passed into subprocesses so
> manual and automated enhancement target the same stock pool。
> Added pipeline-level LLM request accounting:
> record_Ilm_request(
> summarize_IIm_requests
> Ilm_requests .jsonl
> artifacts per pipeline per-stage tagging for
> generate
> inspect
> enhance
> and
> decide
> max_



> [!NOTE] [图片 OCR 识别内容]
> cnhkmcp
> 3.1.10
> 3.1.11
> breaking changes
> pypi . generated 5/5/2026,4:37:53 PM
> API SYMBOLS
> API CHANGES
> DEPENDENCY ENTRIES CHANGED
> FILES (OLD
> NEW)
> 5
> 5
> +0
> -0
> ~0
> 949
> 949
> Export Markdown
> Export PDF
> Summary
> API
> Metadata
> Files
> 20
> Summary
> Summary
> cnhkmcp 3.1.11 is a UI- and operator-catalog-focused release. The package keeps the same public Python API surface; but several front-end workflows were refactored and
> the supported operator list changed. Engineers using the web UIor generating formulas from
> Vvalidop.json
> should review this upgrade carefully:
> New features
> Added a new simulator
> pointin
> cnhkmcp /untracked/APP _
> static /script.js
> runHKFacesimulator( )
> wired to a new
> 命令行页面 (人脸识别版)" option in the
> 'Run
> Simulator'
> modal
> Expanded the operator catalog in
> cnhkmcp
> untracked /APP /validop .json
> with new operators:
> pasteurize(x)
> ts
> returns (X,
> 4,
> mode
> 1 )
> group_count(x,
> group )
> group_std_dev(x,
> group )
> group_sum(x,
> group )
> Refactored the landing page in
> cnhkmcp /untracked/APP / templates
> index.html
> into staged sections for the main workflows, making the Alpha judge; Alpha submitter, and
> pipeline entry points more prominent:
> cnhkmcp_
> untracked
> APP
> static /inspiration.js
> now binds the inspiration modal to any
> inspiration-trigger
> element; allowing multiple UI entry points instead ofa
> single hard-coded button.
> fixes
> In
> cnhkmcp
> untracked/APP / 运行打开我 . Py
> credential caching now fails gracefully: writing ACE credentials to local disk is wrapped in
> try/except
> and Iogs a
> warning
> instead of raising.
> The pipeline credential sync
> in
> cnhkmcp /untracked/APP / 运行打开我 . Py
> is also guarded so local pipeline updates do not crash the process if an internal error occurs:
> Task lookup endpoints in
> cnhkmcp
> untracked/APP / 运行打开我. Py
> now return clearer JSON errors When a task is missing or when
> day_key
> is absent; replacing the previous
> garbled messages。
> The Alpha Inspector import pathlcomment in
> cnhkmcp /untracked/APP / 运行打开我 . Py
> Was corrected to Use
> 缘分
> 道桥
> Which should make the route setup easier to
> understand and maintain。
> Behavior & deprecations
> cnhkmcp /untracked/APP
> static /inspiration.js
> now enables/disables all
> inspiration-trigger
> buttons based on login state; rather than targeting a single
> entry
> Bug
> path



> [!NOTE] [图片 OCR 识别内容]
> Summary
> API
> Metadata
> Files
> 20
> 949
> 949 files
> +6 -6 ~8
> all
> added
> removed
> modified
> cnhkmcp/ _
> init_.Py
> cnhkmcp /untracked/APP
> ace
> cnhkmcp /untracked/APP _
> static /inspiration.js
> cnhkmcp /untracked/APP _
> static /script.js
> cnhkmcp /untracked/APP_
> static /styles _
> CSS
> cnhkmcp /untracked/APP / templates _
> index.html
> cnhkmcp /untracked/APP /validop .json
> cnhkmcp /untracked/APP _
> /运行打开我. py
> 285,7
> +285,18
> 285
> 285
> password
> str(password
> Or
> ).strip()
> 286
> 286
> i
> not
> Username
> Or
> not password:
> 287
> 287
> return
> 288
> WT
> ~ite_json_file(_ace_credentials_path(),
> {'email'
> username,
> password
> password} )
> 288
> try:
> 289
> Write_json_file(_ace_
> credentials_path(),
> {'email'
> username,
> password 
> password})
> 290
> except Exception
> as
> e:
> 291
> print (f"
> Warning:
> Could
> not
> cache
> credentials to
> local
> disk:
> {e}")
> 289
> 292
> 290
> 293
> 291
> 294
> def
> sync_pipeline_credentials (username
> password:
> str):
> 297,19 +380,22
> 297
> 300
> return
> 298
> 301
> 299
> 302
> updated
> 300
> for
> item
> in
> list pipelines()
> 1o8
> str,


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！ 作为代码小白总是不知道CNHKMCP每次更新了啥

这下一眼就能看出来了

=============================================================================


---

### 技术对话片段 71 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【差生文具多】WQ助手102版安卓版本windows版本.md
- **时间**: 2个月前

**提问/主帖背景 (ZZ43261)**:
先发链接：

安卓： [[链接已屏蔽])

windows： [[链接已屏蔽])

ps:window版本是个压缩包 之前没加密码被干掉了 重新上传了一个加了解压密码wqhelper

然后是更新列表：

1 修复长时间后台挂起后唤醒没有自动重登录的bug

2 移除一些非常用数据和模块，常用模块重新排版UI优化

3 数据自刷新，不用点按钮手动刷新了

4 增加windows桌面版，方便非安卓手机用户（可以放云上和脚本一起用）

5 上一版本夏令时计算错误修复

新首页：


> [!NOTE] [图片 OCR 识别内容]
> WaHelper
> 今日提交
> 回测与收人
> 亍日回剜
> 昨日回蹰 
> 昨ORA收益
> 285
> 4696
> 昨日54收益
> 总BASE收益
> 总其他收莶
> 573.52
> 100.17
> 当前表现
> 日裟透分
> 0.75
> 0.21
> 综合表现
> PPA表现
> 选中RA表现
> 0.8
> 0.84
> 使用表达式
> 平均表达式
> 使用字段
> 23
> 5.19
> 14
> 平均字段
> 社区分
> 最大回剩
> 1.05
> 39.2
> 157
> 统计
> 塔
> Alpha
> 数据


ps：桌面版如果不能运行先装一下压缩包里的VC_redist.x64

这个版本没有功能上的大调整，主要是加入了os日排名的展示，和应答之前兄弟们提的一些建议的更新。这个赛季被组合拳重击了，首先是os总rank干了个-4分，然后是cb和vf双双跳水痛失master且vf0.2坐牢。接下来工作重心可能转向弄渗透分脚本和调整提交策略上了。然后希望兄弟们继续提使用意见和debug，wq助手还是会继续更新。同时恭喜晋级的兄弟们。祝大家新赛季都能进步。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！看的出来这背后的工作量确实不小哈哈

祝越做越好！

=============================================================================


---

### 技术对话片段 72 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【差生文具多】WQ助手102版安卓版本windows版本_39729140385559.md
- **时间**: 2个月前

**提问/主帖背景 (ZZ43261)**:
先发链接：

安卓： [[链接已屏蔽])

windows： [[链接已屏蔽])

ps:window版本是个压缩包 之前没加密码被干掉了 重新上传了一个加了解压密码wqhelper

然后是更新列表：

1 修复长时间后台挂起后唤醒没有自动重登录的bug

2 移除一些非常用数据和模块，常用模块重新排版UI优化

3 数据自刷新，不用点按钮手动刷新了

4 增加windows桌面版，方便非安卓手机用户（可以放云上和脚本一起用）

5 上一版本夏令时计算错误修复

新首页：


> [!NOTE] [图片 OCR 识别内容]
> WaHelper
> 今日提交
> 回测与收人
> 亍日回剜
> 昨日回蹰 
> 昨ORA收益
> 285
> 4696
> 昨日54收益
> 总BASE收益
> 总其他收莶
> 573.52
> 100.17
> 当前表现
> 日裟透分
> 0.75
> 0.21
> 综合表现
> PPA表现
> 选中RA表现
> 0.8
> 0.84
> 使用表达式
> 平均表达式
> 使用字段
> 23
> 5.19
> 14
> 平均字段
> 社区分
> 最大回剩
> 1.05
> 39.2
> 157
> 统计
> 塔
> Alpha
> 数据


ps：桌面版如果不能运行先装一下压缩包里的VC_redist.x64

这个版本没有功能上的大调整，主要是加入了os日排名的展示，和应答之前兄弟们提的一些建议的更新。这个赛季被组合拳重击了，首先是os总rank干了个-4分，然后是cb和vf双双跳水痛失master且vf0.2坐牢。接下来工作重心可能转向弄渗透分脚本和调整提交策略上了。然后希望兄弟们继续提使用意见和debug，wq助手还是会继续更新。同时恭喜晋级的兄弟们。祝大家新赛季都能进步。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！看的出来这背后的工作量确实不小哈哈

祝越做越好！

=============================================================================


---

### 技术对话片段 73 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: [Commented] 【效率王】APP-30完全自动化时代.md
- **时间**: 3个月前

**提问/主帖背景 (CQ89422)**:
吹哨人来了。万众瞩目的AI工具继续升级， **快更新到3.0以上的版本吧！** 。点击“🔄 Alpha自动流水线”按钮，快速感受以下功能吧！ **按需点塔，多个研究管线同时自动开工。**

> - **核心效果：自适应方式找种子，后根据群表现，AI自决策提升目标**


> [!NOTE] [图片 OCR 识别内容]
> fundamental6_EUR_d1_TOPCS16O0_1772864595
> 运行中
> 停止
> 捉示词
> Worker;
> Alpha/ 批:
> 生成
> 栓杏
> 6)回刊
> 4决策
> {5 坞弭
> 6) 实玑
> 池中 Ideas
> 已栓查
> 己回别
> 已坞犟
> 来自生咸
> 来自增强
> 迭代:01最后检查点: 2026-03-07106.23:157
> 生咸一详细8去
> 0003U!
> CMCIUWUZUUU
> UIIU1It
> LCUILUICVJ
> VUa LUI C
> [2026-03-0714:25:35]
> cptnewq
> Liabilities
> Total
> Mumeric
> (Currency)
> Quarteryy
> 974
> [2826-03-07 14.25:35]
> cptnowq_Coqq
> Common /Ordinary Equity
> Total
> Numoric (Curroncy)
> Quartorty
> 94
> [2026-03
> 07 14:25:36]
> newal_dltt'
> Debt
> Total
> Nuweric
> (Currency)
> Annual
> 858
> [2826-03-07 14;25:37]
> Nowal_dC'
> Dobt i
> Curront Liabilitios
> Total
> Numoric CCurroncy)
> Annual
> 829
> [2826-03-07 14:25:37]
> newaz_ppent`
> Property
> plant and Equipment
> Total Clet)
> Numeric
> (Currency)
> Mnual
> 98
> [2826-03-07 14;25:381
> Dew?
> ppegt'
> Property
> plant
> and Equipment
> Total (GToss)
> Numeric (Currenqy)
> Mnnual
> 883
> [2826-03
> 07 14:25.39]
> newq_dpactq '
> Depreciation
> Depletion
> Amortization
> (Accumulated)
> Numeric
> (Currency)
> Quarterly
> 753
> [2826-03-07 14;25:48]
> Dewal_Capx
> Capital Expenditures
> Numeric (Curreney)
> Annual
> 868
> [2826-03-07 14:25.41]
> DCway
> COgs
> Cost Of
> 050I005
> Sold
> Numeric (Currency]
> Annual
> 931
> [2026
> 03-07
> 
> :41]
> newa2_t59a
> Selling,
> General
> and
> Administrative Expense
> Mumeric
> (Curreney)
> Annual
> 915
> [2826-03
> 07 14:25.42]
> newal_invt'
> LNVeICOTICI5
> Total
> Nuoeric (Currency)
> Annual
> 783
> [2026-03-07 14:25:43]
> newaz_rect
> Receivables
> Total
> Nuaeric
> (Currency)
> Annual
> 89$
> [2826-03-07 14:25.43]
> 0Rwa
> che'
> Cash and Short-Torn
> UTVOISCDOTt5
> Numeric (Curroncy)
> Annual
> 96.
> [2026-03-07  14:25:44]
> eq-gpq
> Gross Profit
> (Loss)
> Numeric
> (Currency)
> Quarterly
> 901
> [2826-03
> 07 14.25:II]
> 0Owa2_MC叩
> Working Capital
> CBalance Shoot]
> Mumoric (Curroncy)
> Annual
> 846
> [2026-03
> 07 14:25.45]
> newaz_seq
> Stockholders' Equity
> Parent
> Numeric (Currency)
> Annual
> 93
> [2826-03-07 14;25:45]
> Lta
> Long
> Terw


> - **下一个功能：你来提！多试用，多提意见！**

个人试用了一晚上用不到10元，PPA已找到3个。

对了，请勿侵占相关人员的知识产权，必究！未经允许不可转发。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬更新的好快  都快更不上节奏了

这就立刻更新体验一下！

===================================================================================


---

### 技术对话片段 74 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】APP-30完全自动化时代_38872307253655.md
- **时间**: 3个月前

**提问/主帖背景 (CQ89422)**:
吹哨人来了。万众瞩目的AI工具继续升级， **快更新到3.0以上的版本吧！** 。点击“🔄 Alpha自动流水线”按钮，快速感受以下功能吧！ **按需点塔，多个研究管线同时自动开工。**

> - **核心效果：自适应方式找种子，后根据群表现，AI自决策提升目标**


> [!NOTE] [图片 OCR 识别内容]
> fundamental6_EUR_d1_TOPCS16O0_1772864595
> 运行中
> 停止
> 捉示词
> Worker;
> Alpha/ 批:
> 生成
> 栓杏
> 6)回刊
> 4决策
> {5 坞弭
> 6) 实玑
> 池中 Ideas
> 已栓查
> 己回别
> 已坞犟
> 来自生咸
> 来自增强
> 迭代:01最后检查点: 2026-03-07106.23:157
> 生咸一详细8去
> 0003U!
> CMCIUWUZUUU
> UIIU1It
> LCUILUICVJ
> VUa LUI C
> [2026-03-0714:25:35]
> cptnewq
> Liabilities
> Total
> Mumeric
> (Currency)
> Quarteryy
> 974
> [2826-03-07 14.25:35]
> cptnowq_Coqq
> Common /Ordinary Equity
> Total
> Numoric (Curroncy)
> Quartorty
> 94
> [2026-03
> 07 14:25:36]
> newal_dltt'
> Debt
> Total
> Nuweric
> (Currency)
> Annual
> 858
> [2826-03-07 14;25:37]
> Nowal_dC'
> Dobt i
> Curront Liabilitios
> Total
> Numoric CCurroncy)
> Annual
> 829
> [2826-03-07 14:25:37]
> newaz_ppent`
> Property
> plant and Equipment
> Total Clet)
> Numeric
> (Currency)
> Mnual
> 98
> [2826-03-07 14;25:381
> Dew?
> ppegt'
> Property
> plant
> and Equipment
> Total (GToss)
> Numeric (Currenqy)
> Mnnual
> 883
> [2826-03
> 07 14:25.39]
> newq_dpactq '
> Depreciation
> Depletion
> Amortization
> (Accumulated)
> Numeric
> (Currency)
> Quarterly
> 753
> [2826-03-07 14;25:48]
> Dewal_Capx
> Capital Expenditures
> Numeric (Curreney)
> Annual
> 868
> [2826-03-07 14:25.41]
> DCway
> COgs
> Cost Of
> 050I005
> Sold
> Numeric (Currency]
> Annual
> 931
> [2026
> 03-07
> 
> :41]
> newa2_t59a
> Selling,
> General
> and
> Administrative Expense
> Mumeric
> (Curreney)
> Annual
> 915
> [2826-03
> 07 14:25.42]
> newal_invt'
> LNVeICOTICI5
> Total
> Nuoeric (Currency)
> Annual
> 783
> [2026-03-07 14:25:43]
> newaz_rect
> Receivables
> Total
> Nuaeric
> (Currency)
> Annual
> 89$
> [2826-03-07 14:25.43]
> 0Rwa
> che'
> Cash and Short-Torn
> UTVOISCDOTt5
> Numeric (Curroncy)
> Annual
> 96.
> [2026-03-07  14:25:44]
> eq-gpq
> Gross Profit
> (Loss)
> Numeric
> (Currency)
> Quarterly
> 901
> [2826-03
> 07 14.25:II]
> 0Owa2_MC叩
> Working Capital
> CBalance Shoot]
> Mumoric (Curroncy)
> Annual
> 846
> [2026-03
> 07 14:25.45]
> newaz_seq
> Stockholders' Equity
> Parent
> Numeric (Currency)
> Annual
> 93
> [2826-03-07 14;25:45]
> Lta
> Long
> Terw


> - **下一个功能：你来提！多试用，多提意见！**

个人试用了一晚上用不到10元，PPA已找到3个。

对了，请勿侵占相关人员的知识产权，必究！未经允许不可转发。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬更新的好快  都快更不上节奏了

这就立刻更新体验一下！

===================================================================================


---

### 技术对话片段 75 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】APP重磅升级功能来点Alpha--重新定义AI时代123阶.md
- **时间**: 4个月前

**提问/主帖背景 (CQ89422)**:
吹哨人来了。万众瞩目的AI工具继续升级， **快更新到2.3.0以上的版本吧！** 。点击“找灵感”按钮，快速感受以下功能吧！ **一站式获得Alpha表达式，历史上从未有过如此简单做Alpha的时刻。**

> - **功能1：《来点Alpha》------对应AI时代1阶-----寻找初始信号**


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)
> 步骤3:  启动
> LLM Settings
> 2. Select Dataset
> 3. Resuits
> 生成 Alpha 模板
> 直接来点 Alpha
> 下载 Alpha 结果 ZIP
> Base URL
> Search dataset.
> 搜索
> hps.Ilapi deepseekcom
> 开始处理
> alalyst1
> #SI
> ilen_
> 3693101934?352400. jeor  (111)
> [arlalystl
> #SI
> iea
> ?693101934?3524600. json]  IJsins
> iea
> J80u1:
> Model Name
> 已选数据集: analystl1
> IT3er3 lireiyPData 红0241  Telp elllalce_
> batcli_tceieobu 01
> alalyst1
> SSI_l_ien_
> 步骤2:  选数据集
> [alalyatl
> #SI
> iea
> ?693101934?3524600. json]  IJsins
> aataeet
> CST:
> deepseek-chat
> D: IBRgIJroject cnhkjcp cnhkmcp  utracked yPtrailSomeglphas I8ki113  brain
> Name
> Category
> feature
> IP-
> elentatior lata   alalyst1
> #SI
> d1ap1 1aalyet1
> ISI_llapl
> C
> APIKey
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> Dataeet
> CST
> Leader
> 1|11T1R `
> 21;
> Performance-Weighted
> Baple
> 工 LITZ .
> 测试连接
> analyst10
> 4nalyst
> Analyst Estimates
> [alalyat
> #SI
> ?6931019343352400. jou]
> J801
> [alalyatl
> #SI
> iea
> ?6931019343352400. jou]
> 增强历史生成模板
> analystl
> ESG sCores
> 4nalyst
> [alaly3t1
> #SI
> iea_
> ?69?101934?352400
> jou]
> EIllallcel_
> telplatee
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> 下载增强结果 ZIP
> Estimations Of Key
> [alaly3t1
> #SI
> iea_
> ?693101934?35240
> jor」
> EIllallcel_
> telplate
> analyst14
> Fundamentals
> Analyst
> SrOUP_
> 工?1I]C
> {te_
> aelta (wireorize
> {eector_Perceltile}
> {corr_
> Ielehted
> Sectnr
> Perceltile} =
> 8tt4,
> 631
> industry) 
> analyst15
> Earnings forecasts
> 4nalyst
> [alaly3t1
> #SI
> iea_
> ?693101934?35240. jou]
> iea
> 行业内的时
> Simulation Settings
> 序改善信号
> 计算56对齐差距 {清洗后
> 在过去63天的娈化
> {te_
> aelta }
> 捕捉'差距正茌
> Region
> 步骤1: 必须输入Reg onanalystt6
> Real Time Estimates
> Analyst
> 扩大或缩小'的动态
> 然后在行业内部进行标淮化
> TLIIITI
> 卫RCUL E
> 聚焦于行业内相对改
> 化的怂司,剥离行业整体趋势的影响
> ASI
> Universel
> [alalyatl
> #SI
> iea
> ?6931019343352400. jou]
> Analyst Estimate Data for
> analyst4
> 4nalyst
> [alaly3t1
> #SI
> iea_
> ?69?101934?352400
> jor」
> Universe
> Delay
> Equity
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> erlalcel_telplate
> trade_whel {Sreater {te
> {2ector_
> Celtile}
> MINVOLII
> analyst4s
> Analyst Trade Ideas
> 4nalyst
> {corr_
> Ielehted
> ?e1十I]
> Erceritile}
> 252}
> eiguel_Power {sroWp_
> Decnre
> lectnr
> percertile}
> Delay
> analyst48
> Dividend estimation data
> 4nalyst
> {corr_
> Veielted_
> Bector_
> Perceltile} =
> industry} 
> 1.51
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> iea
> 事件驱动与
> Crrdzmnnt?
> Nn-lt
> 1a21
> 或恶
> 工ah


> - **功能2：《增强历史生成模板》------对应AI时代2阶-----对初始信号的模板进行增强**

把你下载好的模板进行增强，点击后输入第一步做好的模板即可（可多选）。


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)
> LLM Settings
> Base URL
> hps Ilapi deepseek Com
> Model
> Nane
> deepseek-Chat
> APIKey
> 测试连接
> 增强历史生成模板
> 下载增强结果 ZIP
> 这步需要AP| keye阿可


> - 最后一步：把下载好的Alpha列表附上Setting进行回测


> [!NOTE] [图片 OCR 识别内容]
> Alpha_Submitter提交器
> Connectedto BRAIN
> 打开回测器
> BRAIN Expression Template Decoder
> Open Simulator_hk
> AI创意工坊
> 论文分析
> Specialized template decoder with grammar checking for expression-like language
> 七十二娈
> 数据字段指南
> 缘分^道桥
> 模板空间
> 只屦示用户自建模板
> 导出用户自逮葆板
> 导入用户自廷模板
> 加戟72娈生成的椟板
> 载入表达式列表Json
> Vector数据处理模板
> 单字段深度处理
> 双重中性化
> 组内均值超额倍号 _ Matrix Data
> 组内均值超额僖号
> Vector Data
> 换手率娈动Delta模板
> 换手宰Hump模板
> 示例
> 双重中性化:以Analyst15为例
> 组间比较_GLB_topdiv
> 组间比较_glb_topdiv_anl15
> 顾问分析示例


> - **思考与讨论：AI时代的3阶是什么？**

是AI进一步对快要可以提交的信号的自动提升？CLI里面的自我迭代？还是人类作为最后一步手搓的灵感缪斯。快参与讨论吧！

对了，代码里附赠了一个AIAC2.0比赛的半成品，位置如下！如有侵权，请联系本人删帖或调整内容。


> [!NOTE] [图片 OCR 识别内容]
> APP
> Lpycache
> blueprints
> CUstom_templates
> give_me_idea
> hkSimulator
> ResultBuilder
> simulator
> static
> templates
> trailSomeAlphas
> skills
> braln-data-feature-engineerng
> braln-feature-implementation
> template_fnal_enhance
> acelog
> enhance_templatepy
> READMEmd
> requirements txt
> run_pipeline_step_by_stepipynb
> run_pipelinepy


对了，使用前别忘了运行这个👇来解决各类错误


> [!NOTE] [图片 OCR 识别内容]
> 配置前运行我_安装必要依赖包:py


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！ 好快的更新
这下又可以一键无痛参赛了！

===================================================================================


---

### 技术对话片段 76 (原帖: 【效率王】APP重磅升级功能：来点Alpha--重新定义AI时代123阶)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】APP重磅升级功能来点Alpha--重新定义AI时代123阶_38025695370775.md
- **时间**: 4个月前

**提问/主帖背景 (CQ89422)**:
吹哨人来了。万众瞩目的AI工具继续升级， **快更新到2.3.0以上的版本吧！** 。点击“找灵感”按钮，快速感受以下功能吧！ **一站式获得Alpha表达式，历史上从未有过如此简单做Alpha的时刻。**

> - **功能1：《来点Alpha》------对应AI时代1阶-----寻找初始信号**


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)
> 步骤3:  启动
> LLM Settings
> 2. Select Dataset
> 3. Resuits
> 生成 Alpha 模板
> 直接来点 Alpha
> 下载 Alpha 结果 ZIP
> Base URL
> Search dataset.
> 搜索
> hps.Ilapi deepseekcom
> 开始处理
> alalyst1
> #SI
> ilen_
> 3693101934?352400. jeor  (111)
> [arlalystl
> #SI
> iea
> ?693101934?3524600. json]  IJsins
> iea
> J80u1:
> Model Name
> 已选数据集: analystl1
> IT3er3 lireiyPData 红0241  Telp elllalce_
> batcli_tceieobu 01
> alalyst1
> SSI_l_ien_
> 步骤2:  选数据集
> [alalyatl
> #SI
> iea
> ?693101934?3524600. json]  IJsins
> aataeet
> CST:
> deepseek-chat
> D: IBRgIJroject cnhkjcp cnhkmcp  utracked yPtrailSomeglphas I8ki113  brain
> Name
> Category
> feature
> IP-
> elentatior lata   alalyst1
> #SI
> d1ap1 1aalyet1
> ISI_llapl
> C
> APIKey
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> Dataeet
> CST
> Leader
> 1|11T1R `
> 21;
> Performance-Weighted
> Baple
> 工 LITZ .
> 测试连接
> analyst10
> 4nalyst
> Analyst Estimates
> [alalyat
> #SI
> ?6931019343352400. jou]
> J801
> [alalyatl
> #SI
> iea
> ?6931019343352400. jou]
> 增强历史生成模板
> analystl
> ESG sCores
> 4nalyst
> [alaly3t1
> #SI
> iea_
> ?69?101934?352400
> jou]
> EIllallcel_
> telplatee
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> 下载增强结果 ZIP
> Estimations Of Key
> [alaly3t1
> #SI
> iea_
> ?693101934?35240
> jor」
> EIllallcel_
> telplate
> analyst14
> Fundamentals
> Analyst
> SrOUP_
> 工?1I]C
> {te_
> aelta (wireorize
> {eector_Perceltile}
> {corr_
> Ielehted
> Sectnr
> Perceltile} =
> 8tt4,
> 631
> industry) 
> analyst15
> Earnings forecasts
> 4nalyst
> [alaly3t1
> #SI
> iea_
> ?693101934?35240. jou]
> iea
> 行业内的时
> Simulation Settings
> 序改善信号
> 计算56对齐差距 {清洗后
> 在过去63天的娈化
> {te_
> aelta }
> 捕捉'差距正茌
> Region
> 步骤1: 必须输入Reg onanalystt6
> Real Time Estimates
> Analyst
> 扩大或缩小'的动态
> 然后在行业内部进行标淮化
> TLIIITI
> 卫RCUL E
> 聚焦于行业内相对改
> 化的怂司,剥离行业整体趋势的影响
> ASI
> Universel
> [alalyatl
> #SI
> iea
> ?6931019343352400. jou]
> Analyst Estimate Data for
> analyst4
> 4nalyst
> [alaly3t1
> #SI
> iea_
> ?69?101934?352400
> jor」
> Universe
> Delay
> Equity
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> erlalcel_telplate
> trade_whel {Sreater {te
> {2ector_
> Celtile}
> MINVOLII
> analyst4s
> Analyst Trade Ideas
> 4nalyst
> {corr_
> Ielehted
> ?e1十I]
> Erceritile}
> 252}
> eiguel_Power {sroWp_
> Decnre
> lectnr
> percertile}
> Delay
> analyst48
> Dividend estimation data
> 4nalyst
> {corr_
> Veielted_
> Bector_
> Perceltile} =
> industry} 
> 1.51
> [arlalystl
> #SI
> iea
> ?6931019343352400. jou]
> iea
> 事件驱动与
> Crrdzmnnt?
> Nn-lt
> 1a21
> 或恶
> 工ah


> - **功能2：《增强历史生成模板》------对应AI时代2阶-----对初始信号的模板进行增强**

把你下载好的模板进行增强，点击后输入第一步做好的模板即可（可多选）。


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)
> LLM Settings
> Base URL
> hps Ilapi deepseek Com
> Model
> Nane
> deepseek-Chat
> APIKey
> 测试连接
> 增强历史生成模板
> 下载增强结果 ZIP
> 这步需要AP| keye阿可


> - 最后一步：把下载好的Alpha列表附上Setting进行回测


> [!NOTE] [图片 OCR 识别内容]
> Alpha_Submitter提交器
> Connectedto BRAIN
> 打开回测器
> BRAIN Expression Template Decoder
> Open Simulator_hk
> AI创意工坊
> 论文分析
> Specialized template decoder with grammar checking for expression-like language
> 七十二娈
> 数据字段指南
> 缘分^道桥
> 模板空间
> 只屦示用户自建模板
> 导出用户自逮葆板
> 导入用户自廷模板
> 加戟72娈生成的椟板
> 载入表达式列表Json
> Vector数据处理模板
> 单字段深度处理
> 双重中性化
> 组内均值超额倍号 _ Matrix Data
> 组内均值超额僖号
> Vector Data
> 换手率娈动Delta模板
> 换手宰Hump模板
> 示例
> 双重中性化:以Analyst15为例
> 组间比较_GLB_topdiv
> 组间比较_glb_topdiv_anl15
> 顾问分析示例


> - **思考与讨论：AI时代的3阶是什么？**

是AI进一步对快要可以提交的信号的自动提升？CLI里面的自我迭代？还是人类作为最后一步手搓的灵感缪斯。快参与讨论吧！

对了，代码里附赠了一个AIAC2.0比赛的半成品，位置如下！如有侵权，请联系本人删帖或调整内容。


> [!NOTE] [图片 OCR 识别内容]
> APP
> Lpycache
> blueprints
> CUstom_templates
> give_me_idea
> hkSimulator
> ResultBuilder
> simulator
> static
> templates
> trailSomeAlphas
> skills
> braln-data-feature-engineerng
> braln-feature-implementation
> template_fnal_enhance
> acelog
> enhance_templatepy
> READMEmd
> requirements txt
> run_pipeline_step_by_stepipynb
> run_pipelinepy


对了，使用前别忘了运行这个👇来解决各类错误


> [!NOTE] [图片 OCR 识别内容]
> 配置前运行我_安装必要依赖包:py


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！ 好快的更新
这下又可以一键无痛参赛了！

===================================================================================


---

### 技术对话片段 77 (原帖: 打印最终限流状态)
- **原帖链接**: [Commented] 【新人向-SA的Prod检测  24h可检测600个】即插即用结合上一篇SA自相关文章.md
- **时间**: 5个月前

**提问/主帖背景 (LX57490)**:
### **本帖子展示了如何将前辈 [SY86571](/hc/zh-cn/profiles/30781531875223-SY86571) 的优雅避免prod检测受到限流处理及上一篇自相关检测的输出结果进行合二为一的SA-Prod检测代码！**

**一、登录及其配置参数**

1.  40，41行输入账号密码；

2.  38行更改时间，依据于上一篇自相关代码跑出来的文件时间；

3.  42行 **“**  **SELF_CORR_THRESHOLD = 0.58”** ，

三五可以改为0.5，0.5更容易出货；

二五可以改为0.58，以及查看各个alpha的其他指标来决定交不交！

阈值灵感来源游戏王大佬 [worldquant brain赛博游戏王](/hc/en-us/profiles/26858512793111-worldquant brain赛博游戏王) ！

**
> [!NOTE] [图片 OCR 识别内容]
> 37
> 
> 配置参数
> 只需修改这里
> ===
> 38
> START DATE
> "12-15"
> 起始日期 (MM-DD格式)
> 39
> REGION
> EUR"
> # 区域
> 40
> USERNAME
> PASSWORD
> #
> SELF_CORR_THRESHOLD
> 0.58
> 自相关阈值。 只处理小于此值的Alpha
**

**二、断点重连机制**

1.输入y，跳过之前检测成功的并继续监测！


> [!NOTE] [图片 OCR 识别内容]
> 开始处理:  12-15
> EUR
> 自相关阈值:
> 0.58
> 输入文件:
> IUsers IAdministratorIDesktop ISLEFISAISuperalpha_results_12-15_EUR.XIsx
> 输出文件:
> Wusers IAdministratorlDesktoplSLEFISAISuperalpha_prod_correlation_results_12-15_EUR.XIsx
> 尝试登录
> 2026-01-09  17:33:24,039
> INFO
> 登录成功:  用户ID LX57490
> 2026-01-09  17:33:27,379
> INFO
> 从 c: lUsers |AdministratorlDesktop ISLEFISAISuperalpha_results_12-15_EUR.xlsx 中读取到  1653 条记录
> 2026-01-09  17:33:27,379
> INFO
> 应用自相关过滤 (阈值:  0.58),
> 保留 3  条记录
> 开始处理  3 个alpha_id.
> 提示:  按ctrl+c可 中断程序并自动保存当前结果
> 2026
> OI-Og 17:33:27,389
> INFO
> 检测到部分结果文件: partial_results_ 20251212_003646
> CSV
> 是否从部分结果文件继续处理? (yln): Y
> 2026
> OI-Og 17:33:43,476
> INFO
> 跳过  17 个己处理的alpha_id
> 2026-01
> Og 17:33:43,479
> INFO
> 所有alpha_id己处理完成,无需额外处理
> 2026
> OI-Og 17:33:43,793
> INFO
> 结果己保存到Excel文件:
> lUsers |AdministratorIDesktoplSLEFISAISuperalpha_prod_correlation_results_12-15_EUR.xlsx


2. 输入n，开始新监测，并生成新的中间文件供你在prod没检测完提前选择！

中间文件命名方式：partial_results_20260109_174340.csv


> [!NOTE] [图片 OCR 识别内容]
> 削凹_什 ;
> JUSCI3 IUILLIL3 CTaLUI   UESKCOP ILF ISA IUVeraLpNa
> J OU
> CO | CLa CLOI1
> C3UL C3
> 工-13
> CUR; L3入
> 尝试登录
> 2026-01-09  17:33:58,682
> INFO
> 登录成功:  用户ID LX57490
> 2026
> 01-09
> 17:34:01,710
> INFO
> 从 c: lusers IAdministratorIDesktop ISLEFISAISuperalpha_results_12-15_EUR.xlsx 中读取到  1653 条记录
> 2026-01-09  17:34:01,713
> INFO
> 应用自相关过滤 (阈值:0.58),  保留 3 条记录
> 开始处理 3 个alpha_id.
> 冕示:  按ctrl+c可 中断程序并自动保存当前结果
> 2026-01-09  17:34:01,717
> INFO
> 检测到部分结果文件: partial_results_ 20251212_003646 _
> CSV
> 是否从部分结果文件继续处理? (yIn):
> 2026-01-09  17:43:19,186
> INFO
> 开始处理  3 个alpha_id。
> (每25个为一组)
> 堤示:  按Ctrl+c可中断程序并自动保存当前结果
> 2026
> OI-Og 17:43:19,194
> INFO
> 处理  1/3: QPdpel3g (自相关: 0.5715)
> 2026
> OI-Og 17:43:20,162
> WARNING
> 空响应
> 等待
> 20.0秒 (空响应重试:  1/10)
> 2026
> OI-Og 17:43:40,425
> INFO
> 成功获取 OPdpel3g 的max值:  0.5715
> 2026
> 01-09
> 17:43:40,485
> INFO
> 己保存部分结果到
> partial
> results_20260109_174340
> CSV
> 2026
> 01-09
> 17:43:40,506
> INFO
> 进度:  1/3 | 批处理:  1/25 (己用: ZIs)
> 成巧:  1 |失败:
> API剩余:  59
> 重置:  19.7后
> 2026-01
> 17:43:40,510
> INFO
> 处理  2/3: QPePIXWQ (自相关: 0.5769)
> 2026
> 01-09
> 17:43:40,836
> WARNING
> 空响应。等待  20.0秒 (空响应重试:  1/10)
> 2026
> 01
> 17:44:01,102
> INFO
> 成功获取 QPePIxWQ 的max值:  0.5769
> 2026
> 01-09
> 17:44:01,110
> INFO
> 己保存部分结果到: partial_results_20260109_174340.CSV
> 2026
> 01-09
> 17:44:01,110
> INFO
> 进度:  2/3 | 批处理:  2/25 (己用:
> 成巧:  2 |失败: 0
> API剩余:  59
> 重置:  59.7后
> 2026
> 01-09
> 17:44:01,112
> INFO
> 处理  3/3: eTJXOmgp (自相关: 0.5773)
> 2026
> 01-09
> 17:44:01,387
> WARNING
> 空响应。等待  20.0秒 (空响应重试:  1/10)
> 425)
  
> [!NOTE] [图片 OCR 识别内容]
> 围 partial_results_20260109_174340.csV
> alpha_id,prod_correlation
> Iax
>  OPdpel3g,0.5715
> QPePIXWQ,O.5769
> e7JXOmgp,


限流处理，每小时测试25个SA的prod后就休息半小时！

25*24=600 SA！！！！

以上都是一个基本框架，大家可以根据自己的流程进行改代码！！！！

#### 三、完整代码：

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**

import requests

import time

import threading

import logging

import pandas as pd

import os

import random

import json

import signal

import datetime

import traceback

from urllib3.util.retry import Retry

from requests.adapters import HTTPAdapter

import base64

import urllib3

from typing import List, Dict, Optional

# 禁用SSL警告

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 配置日志

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 全局变量用于存储Prod Correlation请求的限流状态

prod_corr_remaining = 60

prod_corr_reset_time = time.time() + 60

prod_corr_lock = threading.Lock()

# 全局变量

SESSION_REFRESH_INTERVAL = 3600  # 3.5小时

last_auth_time = time.time()

# 全局变量用于存储部分结果

partial_results = []

partial_file_path = ""

# ===== 配置参数 - 只需修改这里 =====

START_DATE = "01-01"  # 起始日期（MM-DD格式）

REGION = "EUR"  # 区域

USERNAME = ""

PASSWORD = ""

SELF_CORR_THRESHOLD = 0.58  # 自相关阈值，只处理小于此值的Alpha

# ================================

# 获取当前脚本所在目录

script_dir = os.path.dirname(os.path.abspath(__file__))

# 输入文件路径

INPUT_FILE = os.path.join(script_dir, f"Superalpha_results_{START_DATE}_{REGION}.xlsx")

# 输出文件路径（与代码同目录）

OUTPUT_FILE = os.path.join(script_dir, f"Superalpha_prod_correlation_results_{START_DATE}_{REGION}.xlsx")

def create_session():

"""创建带有重试机制的会话"""

session = requests.Session()

retry_strategy = Retry(

total=5,

backoff_factor=1,

status_forcelist=[429, 500, 502, 503, 504],

allowed_methods=["GET", "POST"]

)

adapter = HTTPAdapter(max_retries=retry_strategy)

session.mount("[链接已屏蔽] adapter)

session.mount("[链接已屏蔽] adapter)

return session

def save_partial_results():

"""保存当前获取的部分结果"""

if not partial_results:

return

global partial_file_path

if not partial_file_path:

# 生成带时间戳的文件名

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

partial_file_path = f"partial_results_{timestamp}.csv"

try:

# 使用CSV格式保存

df = pd.DataFrame(partial_results)

df.to_csv(partial_file_path, index=False)

logging.info(f"已保存部分结果到: {partial_file_path}")

except Exception as e:

logging.error(f"保存部分结果失败: {e}")

def handle_interrupt(signum, frame):

"""处理中断信号"""

logging.warning("检测到程序中断，正在保存当前结果...")

save_partial_results()

logging.info("部分结果已保存，程序退出")

os._exit(1)  # 立即退出程序

def load_partial_results(file_path: str) -> List[Dict]:

"""加载部分结果文件"""

try:

df = pd.read_csv(file_path)

logging.info(f"从部分结果文件加载了 {len(df)} 条记录")

return df.to_dict('records')

except Exception as e:

logging.error(f"加载部分结果失败: {e}")

return []

def ensure_session_valid(session, last_auth_time):

"""确保会话有效，如果超过刷新间隔则重新登录"""

current_time = time.time()

if current_time - last_auth_time > SESSION_REFRESH_INTERVAL:

logging.info("会话已超过3.5小时，正在刷新...")

try:

# 尝试删除现有认证

session.delete(' [[链接已屏蔽]) ')

except:

pass  # 忽略删除错误

# 重新登录

new_session = sign_in()

logging.info("会话刷新成功")

return new_session, current_time

return session, last_auth_time

def sign_in() -> Optional[requests.Session]:

"""登录WorldQuant Brain平台"""

session = create_session()

try:

# 构造认证字符串

auth_str = f"{USERNAME}:{PASSWORD}"

# 转换为字节并Base64编码

auth_bytes = auth_str.encode('utf-8')

base64_bytes = base64.b64encode(auth_bytes)

base64_str = base64_bytes.decode('utf-8')

headers = {

"Authorization": f"Basic {base64_str}",

"Content-Type": "application/json"

}

# 发送认证请求

response = session.post(

' [[链接已屏蔽]) ',

headers=headers,

verify=False  # 禁用SSL验证

)

# 检查响应状态

if response.status_code in [200, 201]:

user_id = response.json().get('user', {}).get('id', '未知用户')

logging.info(f"登录成功: 用户ID {user_id}")

return session

else:

logging.error(f"登录失败: 状态码 {response.status_code}, 响应: {response.text[:200]}")

return None

except Exception as e:

logging.error(f"登录过程中发生错误: {e}")

return None

def safe_get_error_detail(response):

"""安全获取错误详情，处理各种响应格式"""

try:

content = response.json()

if "detail" in content:

return content["detail"]

if "error" in content:

return content["error"]

if "message" in content:

return content["message"]

return json.dumps(content, indent=2)

except json.JSONDecodeError:

if "text/html" in response.headers.get("Content-Type", ""):

return "HTML响应: " + response.text[:500] + "..."

return response.text if response.text else '无错误详情'

def calculate_retry_delay(attempt, max_retries, error_type=None):

"""智能计算重试延迟时间，使用指数退避+抖动策略"""

base_delay = 1.0

if error_type == 'rate_limit':

base_delay = 5.0

elif error_type == 'client_error':

base_delay = 2.0

elif error_type == 'server_error':

base_delay = 3.0

delay = base_delay * (2 ** min(attempt, 8))

jitter = random.uniform(0.5, 1.5)

delay *= jitter

return min(delay, 60.0)

def get_prod_correlation_max(session: requests.Session, alpha_id: str, max_retries: int = 5) -> Optional[float]:

global prod_corr_remaining, prod_corr_reset_time, last_auth_time

# 确保会话有效

session, last_auth_time = ensure_session_valid(session, last_auth_time)

url = f" [[链接已屏蔽]) "

retries = 0

empty_retries = 0

max_empty_retries = 10

base_wait = 20.0  # 基础等待时间设为20秒

while retries < max_retries:

# 检查限流状态

with prod_corr_lock:

current_time = time.time()

if prod_corr_remaining <= 3 and prod_corr_reset_time > current_time:

wait_time = max(3, prod_corr_reset_time - current_time)

logging.info(f"等待限流重置: {wait_time:.1f}秒 (剩余次数: {prod_corr_remaining})")

time.sleep(wait_time)

try:

# 发送请求

resp = session.get(url, timeout=(15, 60))  # 增加超时时间

# 处理200响应

if resp.status_code == 200:

# 更新限流状态

with prod_corr_lock:

try:

remaining_str = resp.headers.get("Ratelimit-Remaining", "60")

reset_str = resp.headers.get("Ratelimit-Reset", "60")

prod_corr_remaining = int(remaining_str.split('.')[0])

reset_seconds = float(resp.headers.get("Ratelimit-Reset", "60"))

prod_corr_reset_time = current_time + reset_seconds

except Exception as e:

logging.warning(f"解析限流头部失败: {e}")

# 处理空响应

if not resp.content:

# 使用固定步长的增长策略，避免等待时间失控

if base_wait >= 120.0:  # 达到上限后不再增加

current_wait = 120.0

else:

current_wait = min(base_wait * (1 + empty_retries * 0.3), 120.0)

# 根据限流情况智能调整等待时间

with prod_corr_lock:

if prod_corr_remaining < 5 and prod_corr_reset_time > time.time():

time_gap = prod_corr_reset_time - time.time()

if 0 < time_gap < 120:

current_wait = max(current_wait, time_gap + 5)  # 确保覆盖重置时间

else:

current_wait = min(current_wait, 5)  # 如果重置时间较远，适度缩短等待

logging.warning(f"空响应，等待 {current_wait:.1f}秒 (空响应重试: {empty_retries + 1}/{max_empty_retries})")

time.sleep(current_wait)

base_wait = current_wait  # 更新基础等待时间

empty_retries += 1

if empty_retries >= max_empty_retries:

logging.error(f"达到最大空响应重试次数 {max_empty_retries}")

return None

continue

# 解析JSON响应

try:

data = resp.json()

return float(data.get("max", 0))

except ValueError:

logging.error(f"JSON解析失败: {resp.text[:100]}...")

return None

# 处理401未授权错误

elif resp.status_code == 401:

logging.warning("会话过期，尝试重新登录...")

session = sign_in()

last_auth_time = time.time()

continue  # 不消耗重试次数

# 处理429限流错误

elif resp.status_code == 429:

retry_after = float(resp.headers.get("Retry-After", "70"))

logging.warning(f"429限流，等待 {retry_after}秒")

time.sleep(retry_after)

continue  # 不消耗重试次数

# 处理400客户端错误

elif resp.status_code == 400:

error_detail = safe_get_error_detail(resp)

logging.error(f"400客户端错误: {error_detail}")

return None  # 不重试

# 处理5xx服务器错误

elif 500 <= resp.status_code < 600:

wait_time = calculate_retry_delay(retries, max_retries, 'server_error')

logging.error(f"服务器错误({resp.status_code})，等待 {wait_time:.2f}秒")

time.sleep(wait_time)

retries += 1

continue

# 其他错误

else:

error_detail = safe_get_error_detail(resp)

logging.error(f"错误状态: {resp.status_code}, 详情: {error_detail}")

return None

# 处理网络错误

except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:

wait_time = calculate_retry_delay(retries, max_retries)

logging.error(f"网络错误({type(e).__name__})，等待 {wait_time:.2f}秒")

time.sleep(wait_time)

retries += 1

except requests.exceptions.RequestException as e:

wait_time = calculate_retry_delay(retries, max_retries)

logging.error(f"请求异常: {e}，等待 {wait_time:.2f}秒")

time.sleep(wait_time)

retries += 1

except Exception as e:

logging.error(f"未知错误: {e}")

traceback.print_exc()

retries += 1

logging.error(f"超过最大重试次数 {max_retries}")

return None

def read_and_filter_data(file_path: str) -> pd.DataFrame:

"""从Excel文件中读取数据并应用自相关过滤"""

try:

if not os.path.exists(file_path):

logging.error(f"文件不存在: {file_path}")

return pd.DataFrame()

# 读取Excel文件

df = pd.read_excel(file_path)

# 检查必要列是否存在

if 'alpha_id' not in df.columns:

logging.error("文件缺少alpha_id列")

return pd.DataFrame()

# 检查自相关列是否存在

if 'self_correlation' not in df.columns:

logging.error("文件缺少self_correlation列，无法过滤")

return pd.DataFrame()

# 应用自相关过滤

original_count = len(df)

df = df[df['self_correlation'] < SELF_CORR_THRESHOLD]

filtered_count = len(df)

logging.info(f"从 {file_path} 中读取到 {original_count} 条记录")

logging.info(f"应用自相关过滤 (阈值: {SELF_CORR_THRESHOLD})，保留 {filtered_count} 条记录")

return df

except Exception as e:

logging.error(f"读取文件失败: {e}")

return pd.DataFrame()

def process_alpha_ids(session: requests.Session, df: pd.DataFrame):

"""处理DataFrame中的alpha_id，获取每个的max值并保存到文件"""

global partial_results, partial_file_path

# 注册中断信号处理

signal.signal(signal.SIGINT, handle_interrupt)

# 检查是否存在部分结果文件

partial_files = [f for f in os.listdir() if f.startswith("partial_results_") and f.endswith(".csv")]

if partial_files:

logging.info(f"检测到部分结果文件: {partial_files[0]}")

response = input("是否从部分结果文件继续处理? (y/n): ").strip().lower()

if response == 'y':

partial_file_path = partial_files[0]

partial_df = pd.read_csv(partial_file_path)

# 合并部分结果

df = df.merge(partial_df[['alpha_id', 'prod_correlation_max']],

on='alpha_id', how='left', suffixes=('', '_partial'))

# 获取已处理的alpha_id

processed_ids = set(partial_df['alpha_id'])

logging.info(f"跳过 {len(processed_ids)} 个已处理的alpha_id")

else:

# 添加空列用于存储结果

df['prod_correlation_max'] = None

# 如果没有部分结果，添加空列

if 'prod_correlation_max' not in df.columns:

df['prod_correlation_max'] = None

# 获取需要处理的alpha_id

to_process = df[df['prod_correlation_max'].isna()]

total = len(to_process)

if total == 0:

logging.info("所有alpha_id已处理完成，无需额外处理")

save_results(df)

return

# 批次处理配置

PER_BATCH_COUNT = 25  # 每批处理的Alpha数量

BREAK_DURATION = 1800  # 30分钟休息时间（秒）

batch_start_time = time.time()  # 记录批次开始时间

processed_in_batch = 0  # 当前批次计数

logging.info(f"开始处理 {total} 个alpha_id... (每{PER_BATCH_COUNT}个为一组)")

print("提示: 按Ctrl+C可中断程序并自动保存当前结果")

success_count = 0

failure_count = 0

batch_number = 1  # 当前批次编号

for i, row in to_process.iterrows():

alpha_id = row['alpha_id']

self_corr = row.get('self_correlation', 'N/A')

logging.info(f"处理 {i + 1}/{total}: {alpha_id} (自相关: {self_corr:.4f})")

max_value = get_prod_correlation_max(session, alpha_id)

if max_value is not None:

df.at[i, 'prod_correlation_max'] = max_value

logging.info(f"成功获取 {alpha_id} 的max值: {max_value:.4f}")

success_count += 1

else:

df.at[i, 'prod_correlation_max'] = -1  # 标记失败

logging.warning(f"获取 {alpha_id} 的max值失败")

failure_count += 1

# 每处理1个alpha_id保存一次部分结果

partial_results = df[['alpha_id', 'prod_correlation_max']].to_dict('records')

save_partial_results()

# 每处理1个打印批次状态（新增批次信息）

with prod_corr_lock:

remaining_time = max(0, prod_corr_reset_time - time.time())

batch_elapsed = time.time() - batch_start_time

logging.info(

f"进度: {i + 1}/{total} | 批处理: {processed_in_batch + 1}/{PER_BATCH_COUNT} (已用: {batch_elapsed:.0f}s)" +

f" | 成功: {success_count} | 失败: {failure_count} | API剩余: {prod_corr_remaining} | 重置: {remaining_time:.1f}秒后")

# 更新批次计数器

processed_in_batch += 1

# 检查是否完成一个批次

if processed_in_batch >= PER_BATCH_COUNT:

batch_end_time = time.time()

batch_duration = batch_end_time - batch_start_time

# 计算批次实际处理时间，确保整批处理不超过1小时

if batch_duration < 3600:  # 3600秒=1小时

remaining_time = 3600 - batch_duration

logging.info(f"已完成批次 #{batch_number} ({PER_BATCH_COUNT}个Alpha)")

logging.info(f"批次耗时: {batch_duration:.2f}秒, 剩余时间: {remaining_time:.2f}秒")

logging.info(f"休息 {BREAK_DURATION//60} 分钟后继续...")

time.sleep(max(remaining_time, BREAK_DURATION))  # 确保休息不少于30分钟

else:

logging.info(f"已完成批次 #{batch_number} ({PER_BATCH_COUNT}个Alpha), 耗时: {batch_duration:.2f}秒")

logging.info(f"休息 {BREAK_DURATION//60} 分钟后继续...")

time.sleep(BREAK_DURATION)

# 重置批次计数器

batch_number += 1

processed_in_batch = 0

batch_start_time = time.time()

# 处理完成后删除部分结果文件

if partial_file_path and os.path.exists(partial_file_path):

try:

os.remove(partial_file_path)

logging.info(f"已删除部分结果文件: {partial_file_path}")

except Exception as e:

logging.error(f"删除部分结果文件失败: {e}")

# 保存最终结果

save_results(df)

def save_results(df: pd.DataFrame):

"""保存结果到文件"""

try:

# 保存为Excel

df.to_excel(OUTPUT_FILE, index=False)

logging.info(f"结果已保存到Excel文件: {OUTPUT_FILE}")

# 打印统计信息

if 'prod_correlation_max' in df.columns:

valid_results = df[df['prod_correlation_max'] >= 0]

if not valid_results.empty:

print("\nProd相关性统计:")

print(f"平均Prod相关性: {valid_results['prod_correlation_max'].mean():.4f}")

print(f"最低Prod相关性: {valid_results['prod_correlation_max'].min():.4f}")

print(f"最高Prod相关性: {valid_results['prod_correlation_max'].max():.4f}")

# 找出Prod相关性最低的5个Alpha

low_prod = valid_results.nsmallest(5, 'prod_correlation_max')

print("\nProd相关性最低的5个Alpha:")

print(low_prod[['alpha_id', 'self_correlation', 'prod_correlation_max']].to_string(index=False))

except Exception as e:

logging.error(f"保存结果失败: {e}")

# 主程序

if __name__ == "__main__":

# 打印配置信息

print(f"开始处理: {START_DATE} - {REGION}")

print(f"自相关阈值: {SELF_CORR_THRESHOLD}")

print(f"输入文件: {INPUT_FILE}")

print(f"输出文件: {OUTPUT_FILE}")

# 登录

print("尝试登录...")

session = sign_in()

if session is None:

print("登录失败，请检查用户名和密码")

exit(1)

# 从文件读取数据并应用自相关过滤

df = read_and_filter_data(INPUT_FILE)

if df.empty:

print(f"未从 {INPUT_FILE} 中找到有效数据")

exit(1)

# 处理alpha_id列表

print(f"\n开始处理 {len(df)} 个alpha_id...")

print("提示: 按Ctrl+C可中断程序并自动保存当前结果")

process_alpha_ids(session, df)

# 打印最终限流状态

with prod_corr_lock:

remaining_time = max(0, prod_corr_reset_time - time.time())

print(f"\n处理完成! 结果已保存到 {OUTPUT_FILE}")

print(f"最终状态: 剩余查询次数 {prod_corr_remaining}, 重置时间 {remaining_time:.2f} 秒后")

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢尼克大佬分享 ！  新人向内容都很有用

再多发几个可以搞成合集了

===================================================================================


---

### 技术对话片段 78 (原帖: 打印最终限流状态)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【新人向-SA的Prod检测  24h可检测600个】即插即用结合上一篇SA自相关文章_37554208805911.md
- **时间**: 5个月前

**提问/主帖背景 (LX57490)**:
### **本帖子展示了如何将前辈 [SY86571](/hc/zh-cn/profiles/30781531875223-SY86571) 的优雅避免prod检测受到限流处理及上一篇自相关检测的输出结果进行合二为一的SA-Prod检测代码！**

**一、登录及其配置参数**

1.  40，41行输入账号密码；

2.  38行更改时间，依据于上一篇自相关代码跑出来的文件时间；

3.  42行 **“**  **SELF_CORR_THRESHOLD = 0.58”** ，

三五可以改为0.5，0.5更容易出货；

二五可以改为0.58，以及查看各个alpha的其他指标来决定交不交！

阈值灵感来源游戏王大佬 [worldquant brain赛博游戏王](/hc/en-us/profiles/26858512793111-worldquant brain赛博游戏王) ！

**
> [!NOTE] [图片 OCR 识别内容]
> 37
> 
> 配置参数
> 只需修改这里
> ===
> 38
> START DATE
> "12-15"
> 起始日期 (MM-DD格式)
> 39
> REGION
> EUR"
> # 区域
> 40
> USERNAME
> PASSWORD
> #
> SELF_CORR_THRESHOLD
> 0.58
> 自相关阈值。 只处理小于此值的Alpha
**

**二、断点重连机制**

1.输入y，跳过之前检测成功的并继续监测！


> [!NOTE] [图片 OCR 识别内容]
> 开始处理:  12-15
> EUR
> 自相关阈值:
> 0.58
> 输入文件:
> IUsers IAdministratorIDesktop ISLEFISAISuperalpha_results_12-15_EUR.XIsx
> 输出文件:
> Wusers IAdministratorlDesktoplSLEFISAISuperalpha_prod_correlation_results_12-15_EUR.XIsx
> 尝试登录
> 2026-01-09  17:33:24,039
> INFO
> 登录成功:  用户ID LX57490
> 2026-01-09  17:33:27,379
> INFO
> 从 c: lUsers |AdministratorlDesktop ISLEFISAISuperalpha_results_12-15_EUR.xlsx 中读取到  1653 条记录
> 2026-01-09  17:33:27,379
> INFO
> 应用自相关过滤 (阈值:  0.58),
> 保留 3  条记录
> 开始处理  3 个alpha_id.
> 提示:  按ctrl+c可 中断程序并自动保存当前结果
> 2026
> OI-Og 17:33:27,389
> INFO
> 检测到部分结果文件: partial_results_ 20251212_003646
> CSV
> 是否从部分结果文件继续处理? (yln): Y
> 2026
> OI-Og 17:33:43,476
> INFO
> 跳过  17 个己处理的alpha_id
> 2026-01
> Og 17:33:43,479
> INFO
> 所有alpha_id己处理完成,无需额外处理
> 2026
> OI-Og 17:33:43,793
> INFO
> 结果己保存到Excel文件:
> lUsers |AdministratorIDesktoplSLEFISAISuperalpha_prod_correlation_results_12-15_EUR.xlsx


2. 输入n，开始新监测，并生成新的中间文件供你在prod没检测完提前选择！

中间文件命名方式：partial_results_20260109_174340.csv


> [!NOTE] [图片 OCR 识别内容]
> 削凹_什 ;
> JUSCI3 IUILLIL3 CTaLUI   UESKCOP ILF ISA IUVeraLpNa
> J OU
> CO | CLa CLOI1
> C3UL C3
> 工-13
> CUR; L3入
> 尝试登录
> 2026-01-09  17:33:58,682
> INFO
> 登录成功:  用户ID LX57490
> 2026
> 01-09
> 17:34:01,710
> INFO
> 从 c: lusers IAdministratorIDesktop ISLEFISAISuperalpha_results_12-15_EUR.xlsx 中读取到  1653 条记录
> 2026-01-09  17:34:01,713
> INFO
> 应用自相关过滤 (阈值:0.58),  保留 3 条记录
> 开始处理 3 个alpha_id.
> 冕示:  按ctrl+c可 中断程序并自动保存当前结果
> 2026-01-09  17:34:01,717
> INFO
> 检测到部分结果文件: partial_results_ 20251212_003646 _
> CSV
> 是否从部分结果文件继续处理? (yIn):
> 2026-01-09  17:43:19,186
> INFO
> 开始处理  3 个alpha_id。
> (每25个为一组)
> 堤示:  按Ctrl+c可中断程序并自动保存当前结果
> 2026
> OI-Og 17:43:19,194
> INFO
> 处理  1/3: QPdpel3g (自相关: 0.5715)
> 2026
> OI-Og 17:43:20,162
> WARNING
> 空响应
> 等待
> 20.0秒 (空响应重试:  1/10)
> 2026
> OI-Og 17:43:40,425
> INFO
> 成功获取 OPdpel3g 的max值:  0.5715
> 2026
> 01-09
> 17:43:40,485
> INFO
> 己保存部分结果到
> partial
> results_20260109_174340
> CSV
> 2026
> 01-09
> 17:43:40,506
> INFO
> 进度:  1/3 | 批处理:  1/25 (己用: ZIs)
> 成巧:  1 |失败:
> API剩余:  59
> 重置:  19.7后
> 2026-01
> 17:43:40,510
> INFO
> 处理  2/3: QPePIXWQ (自相关: 0.5769)
> 2026
> 01-09
> 17:43:40,836
> WARNING
> 空响应。等待  20.0秒 (空响应重试:  1/10)
> 2026
> 01
> 17:44:01,102
> INFO
> 成功获取 QPePIxWQ 的max值:  0.5769
> 2026
> 01-09
> 17:44:01,110
> INFO
> 己保存部分结果到: partial_results_20260109_174340.CSV
> 2026
> 01-09
> 17:44:01,110
> INFO
> 进度:  2/3 | 批处理:  2/25 (己用:
> 成巧:  2 |失败: 0
> API剩余:  59
> 重置:  59.7后
> 2026
> 01-09
> 17:44:01,112
> INFO
> 处理  3/3: eTJXOmgp (自相关: 0.5773)
> 2026
> 01-09
> 17:44:01,387
> WARNING
> 空响应。等待  20.0秒 (空响应重试:  1/10)
> 425)
  
> [!NOTE] [图片 OCR 识别内容]
> 围 partial_results_20260109_174340.csV
> alpha_id,prod_correlation
> Iax
>  OPdpel3g,0.5715
> QPePIXWQ,O.5769
> e7JXOmgp,


限流处理，每小时测试25个SA的prod后就休息半小时！

25*24=600 SA！！！！

以上都是一个基本框架，大家可以根据自己的流程进行改代码！！！！

#### 三、完整代码：

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**

import requests

import time

import threading

import logging

import pandas as pd

import os

import random

import json

import signal

import datetime

import traceback

from urllib3.util.retry import Retry

from requests.adapters import HTTPAdapter

import base64

import urllib3

from typing import List, Dict, Optional

# 禁用SSL警告

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 配置日志

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 全局变量用于存储Prod Correlation请求的限流状态

prod_corr_remaining = 60

prod_corr_reset_time = time.time() + 60

prod_corr_lock = threading.Lock()

# 全局变量

SESSION_REFRESH_INTERVAL = 3600  # 3.5小时

last_auth_time = time.time()

# 全局变量用于存储部分结果

partial_results = []

partial_file_path = ""

# ===== 配置参数 - 只需修改这里 =====

START_DATE = "01-01"  # 起始日期（MM-DD格式）

REGION = "EUR"  # 区域

USERNAME = ""

PASSWORD = ""

SELF_CORR_THRESHOLD = 0.58  # 自相关阈值，只处理小于此值的Alpha

# ================================

# 获取当前脚本所在目录

script_dir = os.path.dirname(os.path.abspath(__file__))

# 输入文件路径

INPUT_FILE = os.path.join(script_dir, f"Superalpha_results_{START_DATE}_{REGION}.xlsx")

# 输出文件路径（与代码同目录）

OUTPUT_FILE = os.path.join(script_dir, f"Superalpha_prod_correlation_results_{START_DATE}_{REGION}.xlsx")

def create_session():

"""创建带有重试机制的会话"""

session = requests.Session()

retry_strategy = Retry(

total=5,

backoff_factor=1,

status_forcelist=[429, 500, 502, 503, 504],

allowed_methods=["GET", "POST"]

)

adapter = HTTPAdapter(max_retries=retry_strategy)

session.mount("[链接已屏蔽] adapter)

session.mount("[链接已屏蔽] adapter)

return session

def save_partial_results():

"""保存当前获取的部分结果"""

if not partial_results:

return

global partial_file_path

if not partial_file_path:

# 生成带时间戳的文件名

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

partial_file_path = f"partial_results_{timestamp}.csv"

try:

# 使用CSV格式保存

df = pd.DataFrame(partial_results)

df.to_csv(partial_file_path, index=False)

logging.info(f"已保存部分结果到: {partial_file_path}")

except Exception as e:

logging.error(f"保存部分结果失败: {e}")

def handle_interrupt(signum, frame):

"""处理中断信号"""

logging.warning("检测到程序中断，正在保存当前结果...")

save_partial_results()

logging.info("部分结果已保存，程序退出")

os._exit(1)  # 立即退出程序

def load_partial_results(file_path: str) -> List[Dict]:

"""加载部分结果文件"""

try:

df = pd.read_csv(file_path)

logging.info(f"从部分结果文件加载了 {len(df)} 条记录")

return df.to_dict('records')

except Exception as e:

logging.error(f"加载部分结果失败: {e}")

return []

def ensure_session_valid(session, last_auth_time):

"""确保会话有效，如果超过刷新间隔则重新登录"""

current_time = time.time()

if current_time - last_auth_time > SESSION_REFRESH_INTERVAL:

logging.info("会话已超过3.5小时，正在刷新...")

try:

# 尝试删除现有认证

session.delete(' [[链接已屏蔽]) ')

except:

pass  # 忽略删除错误

# 重新登录

new_session = sign_in()

logging.info("会话刷新成功")

return new_session, current_time

return session, last_auth_time

def sign_in() -> Optional[requests.Session]:

"""登录WorldQuant Brain平台"""

session = create_session()

try:

# 构造认证字符串

auth_str = f"{USERNAME}:{PASSWORD}"

# 转换为字节并Base64编码

auth_bytes = auth_str.encode('utf-8')

base64_bytes = base64.b64encode(auth_bytes)

base64_str = base64_bytes.decode('utf-8')

headers = {

"Authorization": f"Basic {base64_str}",

"Content-Type": "application/json"

}

# 发送认证请求

response = session.post(

' [[链接已屏蔽]) ',

headers=headers,

verify=False  # 禁用SSL验证

)

# 检查响应状态

if response.status_code in [200, 201]:

user_id = response.json().get('user', {}).get('id', '未知用户')

logging.info(f"登录成功: 用户ID {user_id}")

return session

else:

logging.error(f"登录失败: 状态码 {response.status_code}, 响应: {response.text[:200]}")

return None

except Exception as e:

logging.error(f"登录过程中发生错误: {e}")

return None

def safe_get_error_detail(response):

"""安全获取错误详情，处理各种响应格式"""

try:

content = response.json()

if "detail" in content:

return content["detail"]

if "error" in content:

return content["error"]

if "message" in content:

return content["message"]

return json.dumps(content, indent=2)

except json.JSONDecodeError:

if "text/html" in response.headers.get("Content-Type", ""):

return "HTML响应: " + response.text[:500] + "..."

return response.text if response.text else '无错误详情'

def calculate_retry_delay(attempt, max_retries, error_type=None):

"""智能计算重试延迟时间，使用指数退避+抖动策略"""

base_delay = 1.0

if error_type == 'rate_limit':

base_delay = 5.0

elif error_type == 'client_error':

base_delay = 2.0

elif error_type == 'server_error':

base_delay = 3.0

delay = base_delay * (2 ** min(attempt, 8))

jitter = random.uniform(0.5, 1.5)

delay *= jitter

return min(delay, 60.0)

def get_prod_correlation_max(session: requests.Session, alpha_id: str, max_retries: int = 5) -> Optional[float]:

global prod_corr_remaining, prod_corr_reset_time, last_auth_time

# 确保会话有效

session, last_auth_time = ensure_session_valid(session, last_auth_time)

url = f" [[链接已屏蔽]) "

retries = 0

empty_retries = 0

max_empty_retries = 10

base_wait = 20.0  # 基础等待时间设为20秒

while retries < max_retries:

# 检查限流状态

with prod_corr_lock:

current_time = time.time()

if prod_corr_remaining <= 3 and prod_corr_reset_time > current_time:

wait_time = max(3, prod_corr_reset_time - current_time)

logging.info(f"等待限流重置: {wait_time:.1f}秒 (剩余次数: {prod_corr_remaining})")

time.sleep(wait_time)

try:

# 发送请求

resp = session.get(url, timeout=(15, 60))  # 增加超时时间

# 处理200响应

if resp.status_code == 200:

# 更新限流状态

with prod_corr_lock:

try:

remaining_str = resp.headers.get("Ratelimit-Remaining", "60")

reset_str = resp.headers.get("Ratelimit-Reset", "60")

prod_corr_remaining = int(remaining_str.split('.')[0])

reset_seconds = float(resp.headers.get("Ratelimit-Reset", "60"))

prod_corr_reset_time = current_time + reset_seconds

except Exception as e:

logging.warning(f"解析限流头部失败: {e}")

# 处理空响应

if not resp.content:

# 使用固定步长的增长策略，避免等待时间失控

if base_wait >= 120.0:  # 达到上限后不再增加

current_wait = 120.0

else:

current_wait = min(base_wait * (1 + empty_retries * 0.3), 120.0)

# 根据限流情况智能调整等待时间

with prod_corr_lock:

if prod_corr_remaining < 5 and prod_corr_reset_time > time.time():

time_gap = prod_corr_reset_time - time.time()

if 0 < time_gap < 120:

current_wait = max(current_wait, time_gap + 5)  # 确保覆盖重置时间

else:

current_wait = min(current_wait, 5)  # 如果重置时间较远，适度缩短等待

logging.warning(f"空响应，等待 {current_wait:.1f}秒 (空响应重试: {empty_retries + 1}/{max_empty_retries})")

time.sleep(current_wait)

base_wait = current_wait  # 更新基础等待时间

empty_retries += 1

if empty_retries >= max_empty_retries:

logging.error(f"达到最大空响应重试次数 {max_empty_retries}")

return None

continue

# 解析JSON响应

try:

data = resp.json()

return float(data.get("max", 0))

except ValueError:

logging.error(f"JSON解析失败: {resp.text[:100]}...")

return None

# 处理401未授权错误

elif resp.status_code == 401:

logging.warning("会话过期，尝试重新登录...")

session = sign_in()

last_auth_time = time.time()

continue  # 不消耗重试次数

# 处理429限流错误

elif resp.status_code == 429:

retry_after = float(resp.headers.get("Retry-After", "70"))

logging.warning(f"429限流，等待 {retry_after}秒")

time.sleep(retry_after)

continue  # 不消耗重试次数

# 处理400客户端错误

elif resp.status_code == 400:

error_detail = safe_get_error_detail(resp)

logging.error(f"400客户端错误: {error_detail}")

return None  # 不重试

# 处理5xx服务器错误

elif 500 <= resp.status_code < 600:

wait_time = calculate_retry_delay(retries, max_retries, 'server_error')

logging.error(f"服务器错误({resp.status_code})，等待 {wait_time:.2f}秒")

time.sleep(wait_time)

retries += 1

continue

# 其他错误

else:

error_detail = safe_get_error_detail(resp)

logging.error(f"错误状态: {resp.status_code}, 详情: {error_detail}")

return None

# 处理网络错误

except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:

wait_time = calculate_retry_delay(retries, max_retries)

logging.error(f"网络错误({type(e).__name__})，等待 {wait_time:.2f}秒")

time.sleep(wait_time)

retries += 1

except requests.exceptions.RequestException as e:

wait_time = calculate_retry_delay(retries, max_retries)

logging.error(f"请求异常: {e}，等待 {wait_time:.2f}秒")

time.sleep(wait_time)

retries += 1

except Exception as e:

logging.error(f"未知错误: {e}")

traceback.print_exc()

retries += 1

logging.error(f"超过最大重试次数 {max_retries}")

return None

def read_and_filter_data(file_path: str) -> pd.DataFrame:

"""从Excel文件中读取数据并应用自相关过滤"""

try:

if not os.path.exists(file_path):

logging.error(f"文件不存在: {file_path}")

return pd.DataFrame()

# 读取Excel文件

df = pd.read_excel(file_path)

# 检查必要列是否存在

if 'alpha_id' not in df.columns:

logging.error("文件缺少alpha_id列")

return pd.DataFrame()

# 检查自相关列是否存在

if 'self_correlation' not in df.columns:

logging.error("文件缺少self_correlation列，无法过滤")

return pd.DataFrame()

# 应用自相关过滤

original_count = len(df)

df = df[df['self_correlation'] < SELF_CORR_THRESHOLD]

filtered_count = len(df)

logging.info(f"从 {file_path} 中读取到 {original_count} 条记录")

logging.info(f"应用自相关过滤 (阈值: {SELF_CORR_THRESHOLD})，保留 {filtered_count} 条记录")

return df

except Exception as e:

logging.error(f"读取文件失败: {e}")

return pd.DataFrame()

def process_alpha_ids(session: requests.Session, df: pd.DataFrame):

"""处理DataFrame中的alpha_id，获取每个的max值并保存到文件"""

global partial_results, partial_file_path

# 注册中断信号处理

signal.signal(signal.SIGINT, handle_interrupt)

# 检查是否存在部分结果文件

partial_files = [f for f in os.listdir() if f.startswith("partial_results_") and f.endswith(".csv")]

if partial_files:

logging.info(f"检测到部分结果文件: {partial_files[0]}")

response = input("是否从部分结果文件继续处理? (y/n): ").strip().lower()

if response == 'y':

partial_file_path = partial_files[0]

partial_df = pd.read_csv(partial_file_path)

# 合并部分结果

df = df.merge(partial_df[['alpha_id', 'prod_correlation_max']],

on='alpha_id', how='left', suffixes=('', '_partial'))

# 获取已处理的alpha_id

processed_ids = set(partial_df['alpha_id'])

logging.info(f"跳过 {len(processed_ids)} 个已处理的alpha_id")

else:

# 添加空列用于存储结果

df['prod_correlation_max'] = None

# 如果没有部分结果，添加空列

if 'prod_correlation_max' not in df.columns:

df['prod_correlation_max'] = None

# 获取需要处理的alpha_id

to_process = df[df['prod_correlation_max'].isna()]

total = len(to_process)

if total == 0:

logging.info("所有alpha_id已处理完成，无需额外处理")

save_results(df)

return

# 批次处理配置

PER_BATCH_COUNT = 25  # 每批处理的Alpha数量

BREAK_DURATION = 1800  # 30分钟休息时间（秒）

batch_start_time = time.time()  # 记录批次开始时间

processed_in_batch = 0  # 当前批次计数

logging.info(f"开始处理 {total} 个alpha_id... (每{PER_BATCH_COUNT}个为一组)")

print("提示: 按Ctrl+C可中断程序并自动保存当前结果")

success_count = 0

failure_count = 0

batch_number = 1  # 当前批次编号

for i, row in to_process.iterrows():

alpha_id = row['alpha_id']

self_corr = row.get('self_correlation', 'N/A')

logging.info(f"处理 {i + 1}/{total}: {alpha_id} (自相关: {self_corr:.4f})")

max_value = get_prod_correlation_max(session, alpha_id)

if max_value is not None:

df.at[i, 'prod_correlation_max'] = max_value

logging.info(f"成功获取 {alpha_id} 的max值: {max_value:.4f}")

success_count += 1

else:

df.at[i, 'prod_correlation_max'] = -1  # 标记失败

logging.warning(f"获取 {alpha_id} 的max值失败")

failure_count += 1

# 每处理1个alpha_id保存一次部分结果

partial_results = df[['alpha_id', 'prod_correlation_max']].to_dict('records')

save_partial_results()

# 每处理1个打印批次状态（新增批次信息）

with prod_corr_lock:

remaining_time = max(0, prod_corr_reset_time - time.time())

batch_elapsed = time.time() - batch_start_time

logging.info(

f"进度: {i + 1}/{total} | 批处理: {processed_in_batch + 1}/{PER_BATCH_COUNT} (已用: {batch_elapsed:.0f}s)" +

f" | 成功: {success_count} | 失败: {failure_count} | API剩余: {prod_corr_remaining} | 重置: {remaining_time:.1f}秒后")

# 更新批次计数器

processed_in_batch += 1

# 检查是否完成一个批次

if processed_in_batch >= PER_BATCH_COUNT:

batch_end_time = time.time()

batch_duration = batch_end_time - batch_start_time

# 计算批次实际处理时间，确保整批处理不超过1小时

if batch_duration < 3600:  # 3600秒=1小时

remaining_time = 3600 - batch_duration

logging.info(f"已完成批次 #{batch_number} ({PER_BATCH_COUNT}个Alpha)")

logging.info(f"批次耗时: {batch_duration:.2f}秒, 剩余时间: {remaining_time:.2f}秒")

logging.info(f"休息 {BREAK_DURATION//60} 分钟后继续...")

time.sleep(max(remaining_time, BREAK_DURATION))  # 确保休息不少于30分钟

else:

logging.info(f"已完成批次 #{batch_number} ({PER_BATCH_COUNT}个Alpha), 耗时: {batch_duration:.2f}秒")

logging.info(f"休息 {BREAK_DURATION//60} 分钟后继续...")

time.sleep(BREAK_DURATION)

# 重置批次计数器

batch_number += 1

processed_in_batch = 0

batch_start_time = time.time()

# 处理完成后删除部分结果文件

if partial_file_path and os.path.exists(partial_file_path):

try:

os.remove(partial_file_path)

logging.info(f"已删除部分结果文件: {partial_file_path}")

except Exception as e:

logging.error(f"删除部分结果文件失败: {e}")

# 保存最终结果

save_results(df)

def save_results(df: pd.DataFrame):

"""保存结果到文件"""

try:

# 保存为Excel

df.to_excel(OUTPUT_FILE, index=False)

logging.info(f"结果已保存到Excel文件: {OUTPUT_FILE}")

# 打印统计信息

if 'prod_correlation_max' in df.columns:

valid_results = df[df['prod_correlation_max'] >= 0]

if not valid_results.empty:

print("\nProd相关性统计:")

print(f"平均Prod相关性: {valid_results['prod_correlation_max'].mean():.4f}")

print(f"最低Prod相关性: {valid_results['prod_correlation_max'].min():.4f}")

print(f"最高Prod相关性: {valid_results['prod_correlation_max'].max():.4f}")

# 找出Prod相关性最低的5个Alpha

low_prod = valid_results.nsmallest(5, 'prod_correlation_max')

print("\nProd相关性最低的5个Alpha:")

print(low_prod[['alpha_id', 'self_correlation', 'prod_correlation_max']].to_string(index=False))

except Exception as e:

logging.error(f"保存结果失败: {e}")

# 主程序

if __name__ == "__main__":

# 打印配置信息

print(f"开始处理: {START_DATE} - {REGION}")

print(f"自相关阈值: {SELF_CORR_THRESHOLD}")

print(f"输入文件: {INPUT_FILE}")

print(f"输出文件: {OUTPUT_FILE}")

# 登录

print("尝试登录...")

session = sign_in()

if session is None:

print("登录失败，请检查用户名和密码")

exit(1)

# 从文件读取数据并应用自相关过滤

df = read_and_filter_data(INPUT_FILE)

if df.empty:

print(f"未从 {INPUT_FILE} 中找到有效数据")

exit(1)

# 处理alpha_id列表

print(f"\n开始处理 {len(df)} 个alpha_id...")

print("提示: 按Ctrl+C可中断程序并自动保存当前结果")

process_alpha_ids(session, df)

# 打印最终限流状态

with prod_corr_lock:

remaining_time = max(0, prod_corr_reset_time - time.time())

print(f"\n处理完成! 结果已保存到 {OUTPUT_FILE}")

print(f"最终状态: 剩余查询次数 {prod_corr_remaining}, 重置时间 {remaining_time:.2f} 秒后")

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢尼克大佬分享 ！  新人向内容都很有用

再多发几个可以搞成合集了

===================================================================================


---

### 技术对话片段 79 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【新人向】是否还在对华子哥数据WebDataRAW不会解压而感到苦恼即插即用代码来了仅需Excel就可以进行数据分析代码优化.md
- **时间**: 2个月前

**提问/主帖背景 (LX57490)**:
### **本帖子展示了如何将华子哥前辈（ [顾问 KZ79256 (Rank 21)](/hc/en-us/profiles/13609593802263-顾问 KZ79256 (Rank 21)) ）制作的WebDataRAW解压成Excel进行数据分析！**

**注：内存要求极高，请清空电脑目前全部其他打开的应用再进行运行代码！！！！**

**运行内存10G+可尝试！！！！**

**一、配置**

**1.  解压完WebDataRAW_20250219_V0.10.9在图示位置随便创建一个.py文件 ！   
> [!NOTE] [图片 OCR 识别内容]
> mainipynb
> info databin
> all_data pickle
**

**2.  复制代码到这个.py文件里面**

```
import pandas as pdimport msgpackimport zlibimport pickleimport osfrom collections.abc import Iterable# 数据加载函数 (保持原样)def load_obj(name: str) -> object:    with open(name + '.pickle', 'rb') as f:        return pickle.load(f)# 数据解码函数 (稍作优化)def decode_from_bin(file_path):    try:        with open(file_path, 'rb') as f:            compressed_data = f.read()        decompressed_data = zlib.decompress(compressed_data)        # 解决msgpack未导入的问题        import msgpack        data = msgpack.unpackb(decompressed_data, raw=False)        print(f"数据已从 {file_path} 成功解码")        return data    except Exception as e:        print(f"解码过程出错: {str(e)}")        return Nonedef merge_datasets(res_df, settings_df, is_df, os_df):    """合并四个具有相同ID的数据集"""    # 逐步合并数据（类似SQL JOIN）    merged = res_df.merge(settings_df, on='id', how='left', suffixes=('', '_settings'))    merged = merged.merge(is_df, on='id', how='left', suffixes=('', '_is'))    merged = merged.merge(os_df, on='id', how='left', suffixes=('', '_os'))    # 清理可能的重复列（保留原始列）    return merged.loc[:, ~merged.columns.duplicated()]def flatten_dict(d, parent_key='', sep='_'):    items = []    for k, v in d.items():        new_key = f"{parent_key}{sep}{k}" if parent_key else k        if isinstance(v, dict):            items.extend(flatten_dict(v, new_key, sep=sep).items())        elif isinstance(v, Iterable) and not isinstance(v, str):            items.append((new_key, ', '.join(map(str, v))))        else:            items.append((new_key, v))    return dict(items)def save_to_csv(data, filename, max_depth=3):    """    智能保存数据到CSV    """    # 创建输出目录    output_dir = 'data_csv'    os.makedirs(output_dir, exist_ok=True)    filepath = os.path.join(output_dir, filename)    if isinstance(data, dict):        # 展平嵌套字典        flat_data = flatten_dict(data)        pd.DataFrame([flat_data]).to_csv(filepath, index=False)        print(f"字典数据已保存到 {filepath}")    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):        # 处理字典列表        flat_data = []        for item in data:            try:                # 只展平前max_depth层嵌套                flat_data.append(flatten_dict(item, sep='_'))            except:                flat_data.append(item)  # 回退到原始数据        df = pd.DataFrame(flat_data)        df.to_csv(filepath, index=False)        print(f"列表数据({len(data)}条)已保存到 {filepath}")    else:        # 其他类型直接创建DF        try:            pd.DataFrame(data).to_csv(filepath, index=False)            print(f"数据已保存到 {filepath}")        except Exception as e:            print(f"无法保存 {filename}: {str(e)}")            with open(filepath.replace('.csv', '.txt'), 'w') as f:                f.write(str(data))def convert_to_dataframe(data):    """智能转换为DataFrame"""    if isinstance(data, dict):        return pd.DataFrame([flatten_dict(data)])    elif isinstance(data, list) and data and isinstance(data[0], dict):        return pd.DataFrame([flatten_dict(x) for x in data])    return pd.DataFrame(data)# 主处理函数def export_all_to_csv():    # 1. 加载全局数据    all_data = load_obj('all_data')  # 加载pickle数据    info_data = decode_from_bin('info_data.bin')  # 加载bin数据    # 2. 单独保存info_data（保持原功能）    save_to_csv(info_data, 'info_data.csv')    # 3. 配置所有需处理的地区和延迟    regions = ['USA', 'EUR', 'IND', 'ASI', 'GLB', 'JPN', 'KOR', 'HKG', 'TWN', 'CHN']    delays = [0, 1]    # 4. 为每个地区/延迟生成合并文件    for region in regions:        for delay in delays:            key = f"{region}_{delay}"            if key not in all_data:                continue            print(f"\n处理地区: {region}, 延迟: {delay}")            res, settings, is_data, os_data = all_data[key]            # 将各数据集转换为DataFrame            df_res = convert_to_dataframe(res)            df_settings = convert_to_dataframe(settings)            df_is = convert_to_dataframe(is_data)            df_os = convert_to_dataframe(os_data)            # 添加ID列（如果不存在）            for df, name in zip([df_res, df_settings, df_is, df_os],                                ['res', 'settings', 'is_data', 'os_data']):                if 'id' not in df.columns:                    df.insert(0, 'id', range(1, len(df) + 1))            # 合并数据集并保存            merged = merge_datasets(df_res, df_settings, df_is, df_os)            filename = f"merged_{region}_{delay}.csv"            save_to_csv(merged, filename)if __name__ == "__main__":    export_all_to_csv()
```

二、结果

1.   **解压比较慢，请耐心等待！！！！**

在data_csv里面会得到如下内容！
 
> [!NOTE] [图片 OCR 识别内容]
> merged_ASI_
> 1.CSV
> merged_CHN_O.csv
> merged_CHN
> 1.CsV
> merged_EUR_O.csv
> merged_EUR
> 1.CsV
> merged_GLB
> 1.CSV
> merged_HKG
> 1.CSV
> merged_IND
> 1.CSV
> merged_JPN_O.csv
> merged_JPN
> 1.CSV
> merged_KOR
> 1.CSV
> merged_TWN
> 1.CSV
> merged_USA_O.csv
> merged_USA_1.csv


2. 效果图

在这里你可以找到alpha的ID，数据标签，数据集类型，具体数据字段，具体数据集类型，操作符数量，IS数据，Risk数据，max trade数据，23 OS数据，2023年~2026.2月提交时间，制作alpha时间等等！

当然这只是一个小小的解压代码，你可以改进成更好的可视化等等！进行顶级的数据分析！

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**


> [!NOTE] [图片 OCR 识别内容]
> id
> lassif fdatafield
> dataset
> dateCrec
> dateSubr
> categor
> operatorTinstrlime
> ZQGKPxL8
> [' REGCLAR
> [' volume
> Close'
> a1194_find' ]
> ['DvI'
> analystg4'
> 2025-11-142025-11-1 [' analyst
> 8 EQUIII
> XAqbZdMm
> [' REGCLAR
> [' volume
> mdl1l0_score
> md1110_analyst_sentimelt'
> mdl110_valuc ['
> modelll0'
> 2025-11-0.2025-11-0. ['model
> 8 EQUIII
> Wlelwqd
> REGCLAR
> [' volume
> Close
> rsk70_nfn2_asetrd_sriskl'
> DVI'
> risk70'
> 2025-08-052025-08-05
> risk'
> EQUIII
> omgQebIb
> ['POIER_P(['cap'
> WWS54_eventcallbasicinfo_fiscalqlarter'
> IewS54
> 2025-10-2.2025-10-2. ['news
> EQUIII
> OLTvIIP
> POIER_P(['cap'
> fnd28_value_ 083064'
> DVI'
> fundameltal2 2025-08-0+2025-08-08
> fudamer
> EQUIII
> KgxQSbk8
> REGCLAR
> CaD
> 皿d1110
> SCOre
> nd126 high_price  52'
> a1194find'
> modelll0'
> 2026-01-142026-01-1
> model'
> EQUIII
> OdIITI
> REGCLAR
> ['cap
> udlllO_score
> DVI'
> modelll0'
> 2025-08-252025-08-25
> model
> EQUIII
> Wkb35Zx
> ['PONER
> P( ['returis
> close
> al194_find'
> analystg4'
> 2025-08-2(2025-08-2(
> analyst
> 8 EQUIII
> GJvnfMbE
> REGUL AR
> ['returIls'
> Split
> rsk70_mfn2_asetrd_divyild' ]
> DVI'
> risk70'
> 2025-11-222025-11-2: ['risk'
> EQUIII
> 58OrPqr6
> REGCLAR
> ['returIs
> mdlll0_score'
> modelll0' ]
> 2025-11-2(2025-11-2(['model'
> EQUIII
> 7e26081
> REGCLAR
> L Letlrlls
> udlllO_score
> star_val_Db'
> DVI'
> modelll0'
> 2026-01-182026-01-1:
> model'
> 8 EQUIII
> OmojblP2
> REGCLAR
> ['cIose'
> Opel'
> mdlll0_score
> al194_find'
> modelll0'
> 2026-01-0:2026-01-0; ['model
> 5 EQUIII
> blgbjnr
> DAIA_USI ['close
> opel
> 2025-08-182025-08-18
> DV
> 3 EQUIII
> 3 SqojgKlx
> DAIA_USL [' vwap'
> ]
> 2026-01-052026-01-05
> Dr'
> 3 EQUIII
> 24281o8E
> POIER_P(
> VaP
> anl4_afv4_div_high'
> all4_ebitda_flag'
> DVI'
> analyst4'
> 2025-11-0.2025-11-0二
> ~' analyst
> EQUIII
> amQKAKI
> ['POIER_P(
> mdl110_score
> Idl1I0_quality'
> alnfv_mfm2_vami
> modelll0'
> 0v37'
> 2025-08-3.2025-08-3
> model
> 8 EQUIII
> JALAOVj
> REGCLAR
> ['mdlll0_score
> md1110_price_momentlim_reversal'
> star_val_pe
> modelll0'
> mode1382025-09-052025-09-05
> model'
> EQUIII
> RxIEAjj
> REGCLAR
> ['ndlllO_score
> mdl1I0_price_momentlim_reversal'
> star_val_divider
> modelll0'
> mode1382025-08-252025-08-2:
> model'
> EQUIII
> 7RZGel2
> REGCLAR
> mdl110_score
> nd1138_3idpc
> S1t27_top7Spctrankingavg_36'
> modelll0'
> model132025-08-1:2025-08-1
> model'
> EQUIII
> I3ZAjOJ
> [' REGCLAR
> mdl1l0_score
> mdl110_price_momentlm_reversal
> a1115_gr_cal_fy] ['modelll0'
> analyst 2025-08-3.2025-08-3
> ['model'
> 8 EQUIII
> LLL7ETdM
> PONER_P(
> mdl110_score
> rsk70_Mfm2_asetrd_divyild'
> nd125_0Iv' ]
> modelll0'
> risk70' 2025-10-1:2025-10-1:
> model'
> EQUIII
> Dvl'
> Dvl'
> DvI'
> Dvl'
> DvI'
> Dvl'
> Dvl'
> Dvl'
> pv37


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

尼克太强了吧

这个新人向系列实在太实用了 学到了很多

给尼克大佬点赞

=============================================================================


---

### 技术对话片段 80 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【新人向】是否还在对华子哥数据WebDataRAW不会解压而感到苦恼即插即用代码来了仅需Excel就可以进行数据分析代码优化_39531360358295.md
- **时间**: 2个月前

**提问/主帖背景 (LX57490)**:
### **本帖子展示了如何将华子哥前辈（ [顾问 KZ79256 (Rank 21)](/hc/en-us/profiles/13609593802263-顾问 KZ79256 (Rank 21)) ）制作的WebDataRAW解压成Excel进行数据分析！**

**注：内存要求极高，请清空电脑目前全部其他打开的应用再进行运行代码！！！！**

**运行内存10G+可尝试！！！！**

**一、配置**

**1.  解压完WebDataRAW_20250219_V0.10.9在图示位置随便创建一个.py文件 ！   
> [!NOTE] [图片 OCR 识别内容]
> mainipynb
> info databin
> all_data pickle
**

**2.  复制代码到这个.py文件里面**

```
import pandas as pdimport msgpackimport zlibimport pickleimport osfrom collections.abc import Iterable# 数据加载函数 (保持原样)def load_obj(name: str) -> object:    with open(name + '.pickle', 'rb') as f:        return pickle.load(f)# 数据解码函数 (稍作优化)def decode_from_bin(file_path):    try:        with open(file_path, 'rb') as f:            compressed_data = f.read()        decompressed_data = zlib.decompress(compressed_data)        # 解决msgpack未导入的问题        import msgpack        data = msgpack.unpackb(decompressed_data, raw=False)        print(f"数据已从 {file_path} 成功解码")        return data    except Exception as e:        print(f"解码过程出错: {str(e)}")        return Nonedef merge_datasets(res_df, settings_df, is_df, os_df):    """合并四个具有相同ID的数据集"""    # 逐步合并数据（类似SQL JOIN）    merged = res_df.merge(settings_df, on='id', how='left', suffixes=('', '_settings'))    merged = merged.merge(is_df, on='id', how='left', suffixes=('', '_is'))    merged = merged.merge(os_df, on='id', how='left', suffixes=('', '_os'))    # 清理可能的重复列（保留原始列）    return merged.loc[:, ~merged.columns.duplicated()]def flatten_dict(d, parent_key='', sep='_'):    items = []    for k, v in d.items():        new_key = f"{parent_key}{sep}{k}" if parent_key else k        if isinstance(v, dict):            items.extend(flatten_dict(v, new_key, sep=sep).items())        elif isinstance(v, Iterable) and not isinstance(v, str):            items.append((new_key, ', '.join(map(str, v))))        else:            items.append((new_key, v))    return dict(items)def save_to_csv(data, filename, max_depth=3):    """    智能保存数据到CSV    """    # 创建输出目录    output_dir = 'data_csv'    os.makedirs(output_dir, exist_ok=True)    filepath = os.path.join(output_dir, filename)    if isinstance(data, dict):        # 展平嵌套字典        flat_data = flatten_dict(data)        pd.DataFrame([flat_data]).to_csv(filepath, index=False)        print(f"字典数据已保存到 {filepath}")    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):        # 处理字典列表        flat_data = []        for item in data:            try:                # 只展平前max_depth层嵌套                flat_data.append(flatten_dict(item, sep='_'))            except:                flat_data.append(item)  # 回退到原始数据        df = pd.DataFrame(flat_data)        df.to_csv(filepath, index=False)        print(f"列表数据({len(data)}条)已保存到 {filepath}")    else:        # 其他类型直接创建DF        try:            pd.DataFrame(data).to_csv(filepath, index=False)            print(f"数据已保存到 {filepath}")        except Exception as e:            print(f"无法保存 {filename}: {str(e)}")            with open(filepath.replace('.csv', '.txt'), 'w') as f:                f.write(str(data))def convert_to_dataframe(data):    """智能转换为DataFrame"""    if isinstance(data, dict):        return pd.DataFrame([flatten_dict(data)])    elif isinstance(data, list) and data and isinstance(data[0], dict):        return pd.DataFrame([flatten_dict(x) for x in data])    return pd.DataFrame(data)# 主处理函数def export_all_to_csv():    # 1. 加载全局数据    all_data = load_obj('all_data')  # 加载pickle数据    info_data = decode_from_bin('info_data.bin')  # 加载bin数据    # 2. 单独保存info_data（保持原功能）    save_to_csv(info_data, 'info_data.csv')    # 3. 配置所有需处理的地区和延迟    regions = ['USA', 'EUR', 'IND', 'ASI', 'GLB', 'JPN', 'KOR', 'HKG', 'TWN', 'CHN']    delays = [0, 1]    # 4. 为每个地区/延迟生成合并文件    for region in regions:        for delay in delays:            key = f"{region}_{delay}"            if key not in all_data:                continue            print(f"\n处理地区: {region}, 延迟: {delay}")            res, settings, is_data, os_data = all_data[key]            # 将各数据集转换为DataFrame            df_res = convert_to_dataframe(res)            df_settings = convert_to_dataframe(settings)            df_is = convert_to_dataframe(is_data)            df_os = convert_to_dataframe(os_data)            # 添加ID列（如果不存在）            for df, name in zip([df_res, df_settings, df_is, df_os],                                ['res', 'settings', 'is_data', 'os_data']):                if 'id' not in df.columns:                    df.insert(0, 'id', range(1, len(df) + 1))            # 合并数据集并保存            merged = merge_datasets(df_res, df_settings, df_is, df_os)            filename = f"merged_{region}_{delay}.csv"            save_to_csv(merged, filename)if __name__ == "__main__":    export_all_to_csv()
```

二、结果

1.   **解压比较慢，请耐心等待！！！！**

在data_csv里面会得到如下内容！
 
> [!NOTE] [图片 OCR 识别内容]
> merged_ASI_
> 1.CSV
> merged_CHN_O.csv
> merged_CHN
> 1.CsV
> merged_EUR_O.csv
> merged_EUR
> 1.CsV
> merged_GLB
> 1.CSV
> merged_HKG
> 1.CSV
> merged_IND
> 1.CSV
> merged_JPN_O.csv
> merged_JPN
> 1.CSV
> merged_KOR
> 1.CSV
> merged_TWN
> 1.CSV
> merged_USA_O.csv
> merged_USA_1.csv


2. 效果图

在这里你可以找到alpha的ID，数据标签，数据集类型，具体数据字段，具体数据集类型，操作符数量，IS数据，Risk数据，max trade数据，23 OS数据，2023年~2026.2月提交时间，制作alpha时间等等！

当然这只是一个小小的解压代码，你可以改进成更好的可视化等等！进行顶级的数据分析！

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**


> [!NOTE] [图片 OCR 识别内容]
> id
> lassif fdatafield
> dataset
> dateCrec
> dateSubr
> categor
> operatorTinstrlime
> ZQGKPxL8
> [' REGCLAR
> [' volume
> Close'
> a1194_find' ]
> ['DvI'
> analystg4'
> 2025-11-142025-11-1 [' analyst
> 8 EQUIII
> XAqbZdMm
> [' REGCLAR
> [' volume
> mdl1l0_score
> md1110_analyst_sentimelt'
> mdl110_valuc ['
> modelll0'
> 2025-11-0.2025-11-0. ['model
> 8 EQUIII
> Wlelwqd
> REGCLAR
> [' volume
> Close
> rsk70_nfn2_asetrd_sriskl'
> DVI'
> risk70'
> 2025-08-052025-08-05
> risk'
> EQUIII
> omgQebIb
> ['POIER_P(['cap'
> WWS54_eventcallbasicinfo_fiscalqlarter'
> IewS54
> 2025-10-2.2025-10-2. ['news
> EQUIII
> OLTvIIP
> POIER_P(['cap'
> fnd28_value_ 083064'
> DVI'
> fundameltal2 2025-08-0+2025-08-08
> fudamer
> EQUIII
> KgxQSbk8
> REGCLAR
> CaD
> 皿d1110
> SCOre
> nd126 high_price  52'
> a1194find'
> modelll0'
> 2026-01-142026-01-1
> model'
> EQUIII
> OdIITI
> REGCLAR
> ['cap
> udlllO_score
> DVI'
> modelll0'
> 2025-08-252025-08-25
> model
> EQUIII
> Wkb35Zx
> ['PONER
> P( ['returis
> close
> al194_find'
> analystg4'
> 2025-08-2(2025-08-2(
> analyst
> 8 EQUIII
> GJvnfMbE
> REGUL AR
> ['returIls'
> Split
> rsk70_mfn2_asetrd_divyild' ]
> DVI'
> risk70'
> 2025-11-222025-11-2: ['risk'
> EQUIII
> 58OrPqr6
> REGCLAR
> ['returIs
> mdlll0_score'
> modelll0' ]
> 2025-11-2(2025-11-2(['model'
> EQUIII
> 7e26081
> REGCLAR
> L Letlrlls
> udlllO_score
> star_val_Db'
> DVI'
> modelll0'
> 2026-01-182026-01-1:
> model'
> 8 EQUIII
> OmojblP2
> REGCLAR
> ['cIose'
> Opel'
> mdlll0_score
> al194_find'
> modelll0'
> 2026-01-0:2026-01-0; ['model
> 5 EQUIII
> blgbjnr
> DAIA_USI ['close
> opel
> 2025-08-182025-08-18
> DV
> 3 EQUIII
> 3 SqojgKlx
> DAIA_USL [' vwap'
> ]
> 2026-01-052026-01-05
> Dr'
> 3 EQUIII
> 24281o8E
> POIER_P(
> VaP
> anl4_afv4_div_high'
> all4_ebitda_flag'
> DVI'
> analyst4'
> 2025-11-0.2025-11-0二
> ~' analyst
> EQUIII
> amQKAKI
> ['POIER_P(
> mdl110_score
> Idl1I0_quality'
> alnfv_mfm2_vami
> modelll0'
> 0v37'
> 2025-08-3.2025-08-3
> model
> 8 EQUIII
> JALAOVj
> REGCLAR
> ['mdlll0_score
> md1110_price_momentlim_reversal'
> star_val_pe
> modelll0'
> mode1382025-09-052025-09-05
> model'
> EQUIII
> RxIEAjj
> REGCLAR
> ['ndlllO_score
> mdl1I0_price_momentlim_reversal'
> star_val_divider
> modelll0'
> mode1382025-08-252025-08-2:
> model'
> EQUIII
> 7RZGel2
> REGCLAR
> mdl110_score
> nd1138_3idpc
> S1t27_top7Spctrankingavg_36'
> modelll0'
> model132025-08-1:2025-08-1
> model'
> EQUIII
> I3ZAjOJ
> [' REGCLAR
> mdl1l0_score
> mdl110_price_momentlm_reversal
> a1115_gr_cal_fy] ['modelll0'
> analyst 2025-08-3.2025-08-3
> ['model'
> 8 EQUIII
> LLL7ETdM
> PONER_P(
> mdl110_score
> rsk70_Mfm2_asetrd_divyild'
> nd125_0Iv' ]
> modelll0'
> risk70' 2025-10-1:2025-10-1:
> model'
> EQUIII
> Dvl'
> Dvl'
> DvI'
> Dvl'
> DvI'
> Dvl'
> Dvl'
> Dvl'
> pv37


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

尼克太强了吧

这个新人向系列实在太实用了 学到了很多

给尼克大佬点赞

=============================================================================


---

### 技术对话片段 81 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.01.20

昨天第一次见到了更新OS的威力，很多alpha的OS走势都让人感到意想不到

吸取教训，希望以后能做出更好的alpha

===================================================================================


---

### 技术对话片段 82 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.01.19

AIAC 2.0比赛猝不及防的就这么开始了，甚至没有一丝丝的准备

这几天赶快把新的AIAC工作流搞定，争取尽快开始！！！

===================================================================================


---

### 技术对话片段 83 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.01.21

昨天在USA option居然交出了prod corr<0.5的alpha

这在USA还是蛮难得的哈哈

===================================================================================


---

### 技术对话片段 84 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.21

今天提交了AIAC2.0的第一个因子，看了看排行榜大佬们已经开始屠榜了

这几天再完善完善工作流，准备搞起来！

==================================================================================


---

### 技术对话片段 85 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.22

昨天提交了一个GLB 的model，这是看了更新之后的OS表现之后选的Parent跑的子alpha

希望它能和它的Parent一样给力

==================================================================================


---

### 技术对话片段 86 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.23

不得不说限定数据集+地区的PPA之后，有的塔确实非常难点

这几天再想一想怎么能高效点塔！

==================================================================================


---

### 技术对话片段 87 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.24

这几天开始交AIAC 2.0比赛的因子了

这排行榜的竞争属实格外激烈

==================================================================================


---

### 技术对话片段 88 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.25

这几天开始交AIAC 2.0比赛的因子了

到了2w分之后真的很难找到能加高分的因子

==================================================================================


---

### 技术对话片段 89 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.26

GLB这个主题属实有点难搞

想优化出RA有点难度，加油吧！

==================================================================================


---

### 技术对话片段 90 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.01.27

AIAC大家都好强，这几天的排名就像过山车，起起伏伏飘忽不定

希望OS得分也能稳住！

===================================================================================


---

### 技术对话片段 91 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.01.28

感觉AIAC IS评分的标准主要就是看Fit要增加，Turnover/Drawdown要低一点

越到后期感觉越难了

===================================================================================


---

### 技术对话片段 92 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

2026.01.30

AIAC的排行榜竞争格外激烈
这几天就像过山车一样忽上忽下   许个愿希望自己OS表现能好一点哈哈哈

==================================================================================


---

### 技术对话片段 93 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 4个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区======================================== 2026.01.31

今天通过AI第一次做出来了Insider数据集的ATOM RA，解锁了新的数据集的感觉还是挺爽的

希望后面点塔也能顺利完成！

==================================================================================


---

### 技术对话片段 94 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2025.10.12

第五季都来了，时间过的好快

这几天在改自己的回测架构，希望后面回测的能更快一点，有朝一日达到Grandmaster !

===================================================================================


---

### 技术对话片段 95 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

不知不觉都第八季了

888，发发发

祝大家本季度combine一起发 ===================================================================================


---

### 技术对话片段 96 (原帖: 【日常生活贴】我的量化日记第六季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

量化日记更新的好快

今天听完全球会之后感觉到了自己当前工作流的不足，有很多地方需要改进，今年还有两个月，加油

===================================================================================


---

### 技术对话片段 97 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.03.20 日记贴都第十一季了

不知不觉这个季度也要结束了

加油！冲刺Genius

===================================================================================


---

### 技术对话片段 98 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-01
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.54   fitness 1.12
三月的第一天，开个好头，继续专注挖信号。

==================================================================================


---

### 技术对话片段 99 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-02
昨日提交RA数量：2
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.88   fitness 1.45
今天运气不错，跑出了一个满意的SA，希望能顺利过测。

==================================================================================


---

### 技术对话片段 100 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-03
昨日提交RA数量：4
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.21   fitness 1.05
虽然数量凑够了，但整体质量感觉一般般，相关性太高了。

==================================================================================


---

### 技术对话片段 101 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-04
昨日提交RA数量：1
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.10   fitness 1.85
今天只提交了一个，但各项指标都很顶，因子还是贵在精不在多。

==================================================================================


---

### 技术对话片段 102 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-05
昨日提交RA数量：3
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.65   fitness 1.30
思路有点枯竭了，下午翻了翻几篇旧的论坛帖子找找灵感。

==================================================================================


---

### 技术对话片段 103 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-06
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.42   fitness 1.22
最近发现旧因子的衰减好厉害，周末得换个新的方向试试了。

==================================================================================


---

### 技术对话片段 104 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-07
昨日提交RA数量：4
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.75   fitness 1.60
周末也不敢懈怠，多跑几个高换手的因子试试看。

==================================================================================


---

### 技术对话片段 105 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-08
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.95   fitness 1.72
调参调得头晕眼花，不过看到sharpe稳步上去还是挺欣慰的。

==================================================================================


---

### 技术对话片段 106 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-09
昨日提交RA数量：1
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.33   fitness 1.15
SA的combo/select感觉还是很难，慢慢打磨吧。

==================================================================================


---

### 技术对话片段 107 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-10
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.05   fitness 1.88
突然来了灵感！今天这批因子质量奇高，希望实盘能有好的表现！

==================================================================================


---

### 技术对话片段 108 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-11
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.45   fitness 1.18
发现之前几个因子的回撤有点大，这部分还是要注意一下。

==================================================================================


---

### 技术对话片段 109 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-12
昨日提交RA数量：4
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.82   fitness 1.65
状态拉满！量产了一波，SA的逻辑也终于理顺了，希望保持下去。

==================================================================================


---

### 技术对话片段 110 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-13
昨日提交RA数量：1
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.15   fitness 1.05
卡壳了，想用点新的操作符，但是过拟合严重，只能勉强挑出一个凑合的。

==================================================================================


---

### 技术对话片段 111 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-14
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.66   fitness 1.42
趁着周末跑测速度快，多测试了几组不同中性化的参数，还算有收获。

==================================================================================


---

### 技术对话片段 112 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-15
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.15   fitness 1.95
无意中微调了一个delay参数，指标直接起飞，有点慌又有点爽。

==================================================================================


---

### 技术对话片段 113 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-16
昨日提交RA数量：1
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.55   fitness 1.33
今天重点打磨SA，加入了新的select方法，希望能抗得住OS的检验。

==================================================================================


---

### 技术对话片段 114 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-17
昨日提交RA数量：4
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.28   fitness 1.15
尝试了批量组合一下旧思路，算是量大管饱，但夏普确实不太亮眼。

==================================================================================


---

### 技术对话片段 115 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-18
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.78   fitness 1.50
看了篇研报有了新思路，赶紧写代码复现了一下，在平台上的效果居然还不错。

==================================================================================


---

### 技术对话片段 116 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-19
昨日提交RA数量：2
昨日提交SA数量：1
昨日提交RA 平均 sharpe：2.02   fitness 1.85
连续两天出好货，这个量价因子结合得相当精妙，今天可以心安理得地早点休息了。

==================================================================================


---

### 技术对话片段 117 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-21
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.71   fitness 1.25
近期提交alpha的难度感觉越来越大了，要加油了。

==================================================================================


---

### 技术对话片段 118 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-22
昨日提交RA数量：4
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.12   fitness 1.08
周末跑测跑得飞起，自己用Python写了个小脚本辅助筛选，效率确实高了不少。

==================================================================================


---

### 技术对话片段 119 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-03-23
昨日提交RA数量：1
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.21   fitness 1.98
因子不在多而在精，今天这个信号的表现在不同中性化下出奇地稳健。

==================================================================================


---

### 技术对话片段 120 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

日期:2026-02-10
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.42   fitness 1.15
把最近整理的因子逻辑用Python跑了下分布，剔除了几个极值，今天这批看起来稳健多了。

==================================================================================


---

### 技术对话片段 121 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-11
昨日提交RA数量：4
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.95   fitness 1.72
状态爆棚！前几天在Memos里随手记下的几个灵感今天挨个测试，居然跑出了一个极其漂亮、各项指标都达标的SA。

==============================================================================


---

### 技术对话片段 122 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-12
昨日提交RA数量：1
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.15   fitness 1.88
因子确实是贵在精不在多。今天尝试叠加了一个成交量过滤条件，夏普直接破2了。

=============================================================================


---

### 技术对话片段 123 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-13
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.25   fitness 1.10
猫主子今天跑酷差点把桌上的网线碰掉，还好提交没断，不过今天这几个因子的相关性有点偏高。

=============================================================================


---

### 技术对话片段 124 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-14
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.68   fitness 1.45
情人节也在老老实实挖矿，毕竟Alpha才是最忠诚的伴侣，今天表现中规中矩。

=============================================================================


---

### 技术对话片段 125 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-15
昨日提交RA数量：3
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.82   fitness 1.55
最近AI Alpha比赛竞争太激烈了，必须得提高点产出质量，今天这个基本面SA感觉有戏。

=============================================================================


---

### 技术对话片段 126 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-17
昨日提交RA数量：4
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.55   fitness 1.38
把几篇研报的PDF扔给Claude帮忙提炼了一下核心的量价逻辑，省了不少写基础表达式的脑细胞。

=============================================================================


---

### 技术对话片段 127 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-18
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.98   fitness 1.81
趁着晚上给NAS上的Docker容器升了个级，看着后台跑着的MongoDB备份，顺手交了两个低频因子。

=============================================================================


---

### 技术对话片段 128 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-19
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.35   fitness 1.18
新数据集的坑有点多，缺失值处理得不够干净，导致今天回测的几个都不太行。

=============================================================================


---

### 技术对话片段 129 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-20
昨日提交RA数量：2
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.75   fitness 1.62
磨了三天的SA终于成型了！风险中性化虽然难搞，但抗衰减能力确实强很多。

=============================================================================


---

### 技术对话片段 130 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-21
昨日提交RA数量：4
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.48   fitness 1.25
周末用N100那台小机器跑了点轻量级的小回测，挑出几个还算凑合的RA交了，量大管饱。

=============================================================================


---

### 技术对话片段 131 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-22
昨日提交RA数量：1
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.20   fitness 1.95
无心插柳柳成荫，随手改了一个delay参数，各项指标直接起飞，希望能经得起实盘检验。

=============================================================================


---

### 技术对话片段 132 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-23
昨日提交RA数量：3
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.62   fitness 1.40
尝试了一下将情绪数据和传统的动量因子结合，效果还可以，算是打开了新的思考角度。

=============================================================================


---

### 技术对话片段 133 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-24
昨日提交RA数量：2
昨日提交SA数量：1
昨日提交RA 平均 sharpe：1.88   fitness 1.70
今天主要梳理了下旧代码库，把之前废弃的几个SA逻辑缝合了一下，居然奇迹般地过测了。

=============================================================================


---

### 技术对话片段 134 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-25
昨日提交RA数量：4
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.18   fitness 1.08
批量替换了几个算子，生成的因子虽然多，但感觉大同小异，纯属为了维持平台活跃度了。

=============================================================================


---

### 技术对话片段 135 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-26
昨日提交RA数量：2
昨日提交SA数量：0
昨日提交RA 平均 sharpe：1.51   fitness 1.32
发现最近挖出的信号在小盘股上暴露太大，今天花了点时间在表达式里加了市值惩罚项。

=============================================================================


---

### 技术对话片段 136 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

日期:2026-02-27
昨日提交RA数量：1
昨日提交SA数量：0
昨日提交RA 平均 sharpe：2.08   fitness 1.85
月底了，不想太折腾，用最经典的均值回复逻辑做了一点小变种，没想到指标非常顶。

=============================================================================


---

### 技术对话片段 137 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.03.03

不容易 量化日记贴都开了这么多季了

现在一般几天不到就会提示帖子满了  赶紧先写几条

===================================================================================


---

### 技术对话片段 138 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

2026.03.04

DCC这个比赛目前还是有点摸不到头脑

这几天再让AI分析分析如何能好好设计一下流程

===================================================================================


---

### 技术对话片段 139 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

补 2026.03.02

今天已经到了新的Theme  本来说好的全地区 FAST主题似乎不见了

那就只好继续交GLB了

==================================================================================


---

### 技术对话片段 140 (原帖: 【日常生活贴】我的量化日记第十季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区========================================

补 2026.03.01

有的塔感觉是真的很难点亮  这几天费尽力气在死磕某一个塔

希望能点亮！

==================================================================================


---

### 技术对话片段 141 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================日记区=========================================

日期:2025-09-17

昨天提交了最近Merged alpha比赛的第二个因子，收益来看中规中矩只加了1.55刀，但IS score还行加了3000分，第一次参加比赛，希望能有好成绩吧！

===================================================================================


---

### 技术对话片段 142 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================日记区=========================================

日期:2025-09-17

昨天提交了最近Merged alpha比赛的第二个因子，收益来看中规中矩只加了1.55刀，但IS score还行加了3000分，第一次参加比赛，希望能有好成绩吧！

===================================================================================


---

### 技术对话片段 143 (原帖: 【经验分享】关于我Combine名列前茅却只定级Expert这件事😩经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】关于我Combine名列前茅却只定级Expert这件事经验分享_40962586503191.md
- **时间**: 19天前

**提问/主帖背景 (LZ63377)**:
大家好，我是Ricardo，26年Q1结算已经有一段时间了，之前我发分享了自己维持高Combine的一点心得体会。有兴趣的朋友可以看看我之前的帖子，可以了解我是怎样在 **一个月之内Combine提升超4** 并且冲上总池Combine全球第一的。

[[L2] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md]([L2] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md)

[[Commented] [经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享_39224484288663.md]([Commented] [经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享_39224484288663.md)

虽然Combine数据亮眼，但我的定级成绩却难尽人意，只堪堪定上了Expert，实在有些可惜，不过这也为我这个赛季的打法带来了一些启发，在此分享出来，如果对各位有所帮助，还请给我点个赞！


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Re?ched Imandmaster
> Combined Selected Alpha Performance
> No Tatchln?IThas TelresheJ Tonthl 
> Combined Power Pool Alpha Performance
> 1.53
> 0.47 more
> Gmandmaster
> Combined Osmosis Pertormance
> 0.8
> 02more
> Haster


先来看一下上个赛季定级时的数据，上赛季我的目标其实是master,所以点塔压力并不算大。


> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2026 O1,Junuury Ist 2026
> UIaT 77
> Opemtors perda
> WralT IeT
> HeldsTeranha
> 5.63
> 82
> 1.64
> Flo Usrd
> LTTIIUNILICTII
> Nx SIIUIlIon sIIIk
> 153
> 39.9
> 136


第一个问题，可以明显看出，我的 **平均操作符爆炸** 了，因为赛季初自己对操作符数量并不重视，只盯着表现看，甚至有时明明可以顺手消除掉的操作符比如-(A-B)这类表达式，也没有改写一遍，导致赛季末想补救也来不及了，所以一定要 **在赛季初就引起重视** 。还有像signed_power这种操作符，虽然能让因子的数值更好看，但也暗中增加了过拟合风险，一定谨慎使用。顺带一提，最近平台豁免了ts_backfill和group_backfill操作符，在因子中使用这两个操作符不会计入平均操作符数量，这无疑是个好消息，构建因子时可以多多考虑这一点。

第二个问题，平均字段偏高，但 **总字段数却没跟上** ，这说明我的因子有一些同质化问题。虽然有些优质字段确实更容易出信号，但过度集中在少量字段上，就相当于把鸡蛋放在一个篮子里，这在金融市场上显然不是个好事。如果在Osmosis点数的分配上也出现同质化问题，可能会导致每日Rank不稳定、上窜下跳，这也是老师们一直在强调diversity重要性的原因之一，所以一定要尽量 **避免过度集中** 。

还有就是回测天数和社区分这两个场外因素，回测天数没办法提升，只能保证尽量不要因为自身原因断回测。而社区分，上赛季我因为没有及时查看邮箱，错过了 **加入研究小组** 的机会，不仅失去了额外获取社区分的途径还失去了和大佬们交流学习的机会。所以这赛季再次收到邀请后，我立刻就申请加入了，真香！各位朋友一定多多查看邮箱，如果收到邀请，绝对不要错过。值得注意的是，想要加入研究小组需要满足 **任意Combine>1同时平均PC<0.7** ,否则是无法收到邀请的。

然后是关于各等级打法的一点看法，GM的点塔和Combine压力较大，六维反而不是那么的卷，建议冲GM的朋友起码维护两个Combine>2作为保险。Master的点塔和Combine较容易满足，因此是六维最卷的等级，想要冲Master六维不能有一项瘸腿，否则都会很艰难。Expert几乎不存在点塔压力，只要不乱开区域，Combine条件也是很容满足的，这个等级的门道就多了，你可以通过超低的平均操作符或者高字段数来提升排名，十分灵活。 **最近平台上线了Python alpha功能，当你有好的因子但操作符数量偏多时，可以尝试让AI将它转为Python alpha，这样既不会伤害六维，又能点塔，但要注意Vector类型字段现阶段还无法处理，先用Matrix试验一下吧！**

最后祝大家Combine与VF齐飞，Q2再上一层楼，看到这了，点个赞吧！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享这么优质的经验贴  这么高的combine居然没有评上GM真是可惜了

祝大佬这季度定级顺利

=============================================================================


---

### 技术对话片段 144 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: [Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 冲刺genius !
> 细节决定成败,你的六维还能提升 ! &模板
> 
> 
> 首先感谢游戏王 (2559763) ,
> 橘子姐
> (6383096) ,
> base payment 拉满的
> 大佬 (AH18340) 以及 上海 (MF59400)等等的帮助.也许你们自己都不知道 ,
> 但是潜移默化
> 的影响了我,
> 下面阐述的其中有-些内容是我在游戏王那里学习到的.


## **一、Genius定级与何相干？**

总体来说，一共与两方面有关，一是  **硬性指标** ，二是  **软指标** 。


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-03,July 1st, 2025
> September 3Oth; 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 266
> Reached Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 72
> Reached Grandmaster
> 10
> 30
> Combined Alpha Performance
> 2.39
> Reached Grandmaster
> 0.5


其中  **硬性指标** 包括由

1. 本季度 Signals (阿尔法)；

2. 本季度 Pyramids (金字塔)；

3. Combined Alpha Performance (提交的所有alpha表现)；

4. Combined Selected Alpha Performance (被选中的alpha费后表现)

5. Combined Power Pool Alpha Performance (power pool alpha表现)

五部分组成；

```
点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。
```

我们以Expert (专家)为例，硬性指标必须同时满足

1. 本季度alpha数量 Signals ≥ 20；

2. 本季度金字塔数量 Pyramids ≥ 10，

3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5

       这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).

[图片 (图片已丢失)]

**软指标** 又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。

**
> [!NOTE] [图片 OCR 识别内容]
> What happens 迂 more consultants qualify for a level than there are available
> If more consultants meet the base criteria for
> level than there are available Spots
> a tiebreaker criterion is used _
> This is based on a sum Of ranks across the following metrics
> 1.
> distinct Operators
> Alpha (Lower is better )
> 2.
> distinct Fields
> Alpha (Lower is better)
> 3. Total distinct Operators (Higher is better)
> 4
> Total distinct Fields (Higher is better)
> 5. Maximum Simulation Streak
> Best streak of
> consultant that ends i that quarter
> OI
> continues into the next quarter
> Streak does not reset to 0 every quarter。
> 6. Community leader
> Forum
> Number Of Likes on Posts Or comments that are
> published as Of the end Of quarter
> Ninimm length of post Or comment must be 100 characters。
> Referral
> Total number Of successful referrals i the quarter
> A referral is considered
> Slccessfil
> Khen the
> referring consultant h as become eligible to accrte the referral fee for someone
> have referred to BRAIN
> 讧 accordance with the guidelines Of the referral fee program
> Spots?
> Avg
> AVg
> they
**

**
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st, 2025
> September 3Oth, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.41
> 68
> 1.54
> Fields used
> Community activity
> Max simulation streak
> 260
> 33.2
> 88
**

其中  **软指标** (六维数据)包括由本季度

1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；

2. Operators used (操作符的去重使用个数)；

3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；

4. Fields used (字段使用(去重)数量)

5. Community activity (rank[社区活跃程度])

6. Max simulation streak (最大连续回测天数)

六部分组成；

```
·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。
```

[图片 (图片已丢失)]

## **二、冲刺 Genius !**

通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。

1. 关于六维数据  **细节**

这部分我们娓娓道来，关于六维数据我们能做的是什么?

i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；

ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；

iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；

iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；

v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .

首先，讲讲我的一些  **蠢行为! ,** 等等上面还有一点重要的忘记说了， **要保持区域、Delay以及数据集多样性！**

**
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st, 2025
> September 3Oth, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Fundamental
> Insiders
> Macro
> Mogel
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Social Media
> Earnin3s
**

使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多  **8~10**  个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Delayo
> NAN
> Delayl
> NAN
> Fundamental data
> Fundamental data
> Analyst data
> Analyst data
> Broker
> Broker
> News data
> News data
> Social media data
> Social media data
> Sentiment data
> Sentiment data
> Price VOluMe data
> Price Volume data
> Option data
> Option data
> Eamings
> Earnings
> Insiders
> Insiders
> Instiutional Ownership Data
> Instiutional Ownership Data
> Short interest data
> Short interest data
> Macro data
> Macro data
> Other
> Other
> Risk data
> Risk data
> Model data
> Model data
> USA
> ASI
> CHN
> EUR
> GL
> HKG
> KOR
> TVN
> AMR
> JPN
> USA
> ASI
> CHN
> EUR
> GLB
> HKG
> KOR
> TVN
> AMR
> JPN
> Click to drill down
> EUR
> ASI
> GLB
> USA
> CHN


保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.

[图片 (图片已丢失)]

接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/26/2025 EDT
> 顾问 ML47973 (Rank 100)
> Add Alphato
> LiSt
> Code
> IS Summary
> Period
> IS
> 05
> power(2,
> md177_astcomp
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> Simulation Settings
> 1.65
> 6.11%
> 2.64
> 31.939
> 16.609
> 104.449600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Subindustry
> On
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 1.69
> 5.46%
> 1.56
> 10.65%
> 4.76%
> 39.05920
> 1999
> 357
> 2019
> 4.949
> 1.71
> 18.5896
> 8.66%
> 75.279620
> 1988
> 375
> 2020
> -0.,04
> 029
> 0.01
> 0.5596
> 15.18%
> 82920
> 2010
> 375
> Clone Alpha 
> 2021
> 2.46
> 699
> 4.84
> 48.489
> 15.30%
> 122.899620
> 2142
> 380
> 2022
> 2.44
> 7.42%
> 6.08
> 77.70%
> 13.23%
> 209.41920
> 2136
> 390
> Chart
> Pnl
> 2023
> 3.61
> 6.13%
> 7.40
> 52.519
> 1.71%
> 171.19920
> 2114
> 397
> 匣
> Correlation
> 1ON
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,4;51
> PM
> 0.6840
> -0.0542
> OOOK
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,4;51
> Du
> 0.4204
> -0.1633
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 4;51
> 0
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul "22
> Jan '23
> Du
> 0.6874
> -0.6201
> Vear



> [!NOTE] [图片 OCR 识别内容]
> 这个 Q 当时让我 base payment 日 赚54.816 ,当时 iqc 结束 ,第一次0f更新0.86


直到我使用华子哥的插件才发现


> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 美东时间:2025/9/1200:38:06 北京时间: 2025/9/1212:38:06
> 在你可用的运算符中。共有67种运算符被使用。12种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统一为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x, Y, filter
> false); X + y
> 52
> COMBO,REGULARSELECTION
> base
> Arithmetic
> multiply(x ,y
> filterzfalse); X * y
> 76
> COMBO,REGULARSELECTION
> base
> Arithmetic
> sign(x)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> subtract(x, Y, filter-false) X -Y
> 157
> COMBO,REGULARSELECTION
> base
> Arithmetic
> pasteurize(x)
> COMBO,REGULAR
> genius
> Arithmetic
> log(x)
> COMBOREGULARSELECTION
> base
> Arithmetic
> maXfx;y
> COMBO,REGULARSELECTION
> base
> Arithmetic
> absfx)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> divide(x; y), XIy
> 158
> COMBO,REGULARSELECTION
> base


我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！

下面的操作有几率  **降低** 你的  ***Operators per Alpha*** ，和想要查看自己的alpha数据也可以认真看一下

在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)


> [!NOTE] [图片 OCR 识别内容]
> #  登录 (login)url
> CUrl
> --location
> --request
> POST
> https : / /api. worldquantbrain . com
> authentication
> header
> Authorization:
> Basic MZAZODUBMTAZOEBXcSSjbzeGQUYrQUYrQUYgMBFG
> ~-header
> Cookie:
> t=eyJeeXAiOiJKVIQiLCJhbGciOiJIUZIINiJg .eyJqdGkioi -



> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> login
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> POST
> https:Hapi.orldquantbrain comlauthentication
> Send
> Environments
> POST Simulation
> Params
> Authorization
> Headers (10)
> Body
> Scripts
> Settings
> Cookies
> PATCH alpha-adjust
> FIOws
> Auth Type
> GET data-fields
> Username
> 30-510
> COm
> Basic Auth
> GET alpha
> History
> GET Check
> Password
> The authorization header will be
> POST submit
> 0+
> automatically qenerated when yoU send the
> GET Self-COrr
> Body
> Cookies
> Headers (20)
> Test Results
> 201 Created
> 1.975
> 1.14 KB
> Save Response
> GET data-sets
> JSON
> Preview
> Visualize
> 三
> Q  @
> GET
> pyramid
> USET"
> id
> 顾问 ML47973 (Rank 100)
> Loken"
> EXDiTy
> 14400
> DeTmissions
> BEFORE
> ANID_
> AFTER
> PERFORMANCE_
> 10
> BRAIN_LA3S"
> 11
> BRAIN_LABS_JUPYTER
> L43
> 12
> CONSULTANTI
> 13
> "MULTI_SIMULATION "
> 14
> PROD_ALPHAS
> 15
> REFERRAL
> 16
> SUPER_ALPHA "
> 17
> IVISUALIZATION"
> 18
> WORKDAY"
> 19
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> 9@.


下面的是查询alpha信息的url


> [!NOTE] [图片 OCR 识别内容]
> #
> check_alpha_info 其中{alpha_id} 使用alpha_id替代即可
> Curl
> -location
> https : / /api .worldquantbrain . com/alphas / {alpha_id}
> -header
> Cookie:
> tseyJeexAioiJKVIQiLCJhbGciOiJIUZIINiJ9 .eyJqdGkioi


接下来我们就来看看几个alpha，查看它们的数据情况

1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/09/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> ib5
> SCOFe
> Single Data Set Alpha
> 俳
> Power Pool Alpha
> Pyramid theme: EURIDIIIMBALANCE X2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> Simulation Settings
> 3.37
> 22.089
> 2.26
> 9.9396
> 2.4596
> 9.009o0
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.02
> Statistical
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.19
> 23.9499
> 200
> 14.1990
> 1.08%
> 11.8590
> 1324
> 781
> 2014
> 4.55
> 23.2595
> 3.25
> 11.85%
> 0.78%
> 10.20950
> 1612
> 1005
> 2015
> 4.20
> 23.68%
> 3.26
> 13.02%
> 1.31%
> 11.00930
> 1101
> Clone Alpha
> 2016
> 4.52
> 22.9795
> 3.52
> 13.78%
> 1.65%
> 11.99930
> 627
> 1092
> 2017
> 4.22
> 22.0095
> 2.79
> 9.519
> 0.9190
> 8.72930
> 1749
> 1203
> Chart
> Pnl
> 2018
> 3.4
> 21.699
> 2.37
> 10.29%
> 20%
> 499
> 1714
> 1212
> 2019
> 3.26
> 21.4495
> 2.26
> 10.32%
> 1.23%
> 52930
> 1665
> 1162
> 2020
> 1.99
> 21.1495
> 1.12
> 6.6296
> 2.4596
> 2890
> 1616
> 1125
> 2021
> 2.52
> 20.1895
> 47
> 6.729
> 1.02%
> 58930
> 1703
> 1259
> 7,50OK
> 2022
> 1.37
> 20.139
> 0.67
> 4.839
> 2.29%
> 4.80930
> 652
> 1240
> 5,0OOK
> 2023
> -11.03
> 29.179
> 10.18
> -24.859
> 1.539
> -17.0293o
> 1505
> 1077
> 2,50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.99
> 8.649
> 1.44
> 6.5296
> 8.4096
> 15.089600
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 5;43
> PM
> 0.1456
> -0.0393
> 00
> IS Testing Status
> Period
> 05
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 5;43
> PM
> 0.6239
> -0.0916
> 6 PASS
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 5;43
> Sharpe Of 3.37 is above CUtOff of 1.58。
> PM
> Fitness Of 2.26 is above cutoff of 1
> 0.7043
> -0.3995
> Turnover of 22.089 is above cutoff of 1%
> Turnover of 22.08% is below cutoff of 70%


仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain.comlalphas BOPXEEZ
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 3.06
> 2.19 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> IaXTTaCE
> OFF
> operatorcount
> _
> 1Of1
> 个 b = X
> 17
> "language
> FASTEXPR'
> 18
> IVis0a1i2ation"
> false,
> 19
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE
> imb5_
> SCOIC!
> 24
> description
> Iaea:
> Take
> The
> negative
> Inverse
> O1 The
> inbalance
> SCOIE
> -0
> CIeaTe
> ConTLaLian Signal
> That
> elphasizes
> anC
> fLips
> The
> OIIgInal Ielatzonsh-p. InRatzonale
> for
> 0a-a
> USeC
> The
> inbalance
> SCOIE
> (imb5_
> SCOIE )
> Iikely
> IIea5ULe5
> OIOEI
> fIOW
> OI
> Iiquidity
> aSyIIeTTy;
> Its Inverse highlishts periods
> O1 balance,
> and
> The
> negative sign
> fuITher
> inverts
> The signal. InRationale
> fJI
> OperatoIs  used:
> The
> inVerBe
> (1/x)
> TTansfoIms high
> imbalance
> Into
> Ioy
> Values
> anC
> CHe
> negative sign
> (-〉 Iips
> The
> OUTpU
> PTLOIICIZe
> Conci-inns Where
> The OLiginal
> SCOIe
> Is negative (e.8
> sellIng pressuTe)
> bUT
> OWI
> appears
> positive signals
> 25
> ODeratozCount
> 25
> 27
> UateCzeated "
> 2025
> 09-09T01:43:59
> 04:00
> 28
> "dateSubmitted "
> 2025-09-09102:20:35-04:00
> "datelodified
> 2025-09-13109:42:37
> 04:00
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> alpha C


只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符

2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 08/14/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(2
> rsk72_atopzooO_dsrt
> rank
> mdl26
> FLtV
> rsSII
> 2000_30_
> Power Pool Alpha
> Pyramid theme: CHNIDIIRISK X1.4
> Simulation Settings
> Pyramid theme: CHNIDIIMODEL X1.6
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaNHar
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.59
> 48.989
> 0.96
> 17.739
> 14.389
> 7.249600
> Equity
> CHN
> TOPZOOOU
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,00
> 50.9796
> 2.14
> 25.8395
> 3.459
> 10.14930
> 376
> 311
> Clone Alpha
> 2014
> 3.19
> 50.37%6
> 2.39
> 28.3395
> 4.5996
> 11.259530
> 449
> 375
> 2015
> .99
> 43.99%
> 1.76
> 32.2995
> 14.38%
> 15.5935o
> 726
> 502
> 2016
> 2.15
> 46.26%
> 22.0595
> 5.0596
> 9.5390
> 675
> 556
> Chart
> Pnl
> 2017
> 0.46
> 46.93%
> 0.14
> 43895
> 8.6795
> 879530
> 595
> 501
> 2018
> 1.31
> 48.3796
> 0.64
> 11.6395
> 4.6796
> 83900
> 554
> 455
> 2019
> 2.07
> 50.56%
> 1.22
> 17.6995
> 4.11%
> 9850
> 524
> 420
> 2020
> 0.17
> 50.68%
> 0.03
> -1.9695
> 10.9096
> 0.77930
> 542
> 427
> 1ON
> 2021
> 51.20%
> 0.38
> 11.1295
> 9.73%
> 4.34900
> 543
> 425
> 2022
> 50.5696
> 1.12
> 20.1999
> 5.7390
> 7.979530
> 552
> 447
> 5,00OK
> 2023
> 10.25
> 50.3896
> 10.51
> 52.9395
> 2496
> 21.019500
> 562
> 484
> Risk neutralized
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> 1.17
> 48.989
> 0.39
> 5.4296
> 18.579
> 2.219600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.52
> 42.179
> 0.97
> 17.049
> 14.409
> 8.089600
> IS Testing Status
> Period
> IS
> 05
> [
> Correlation
> 8 PASS
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 6;01
> Turnover of 48.989 is above cutoff of 1%
> PM
> Turnover of 48.98% is below cutoff of 70%
> Weight is well distributed over instruments。
> Returns Of 17.73% is above cutoff of 8%.
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 6;01
> Sub-universe Sharpe of 1.55 is above Cutoff of 1.13.
> PM
> Robust universe Sharpe of 1.30 is above CUtoff of 0.64 (40% of Alphal
> 0.8918
> -0.2468
> Robust universe returns of 9.139 is above cutoff of 7.09% (40% of Alphal.
> These pyramid themes match with the following multipliers: CHN/DI/RISK-
> 1.4; CHNIDIIMODEL
> 1.6.The final
> pyramid theme multiplier is 1.4. Effective pyramid count for Genius is 2。
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 6;01
> PM
> 5WARNING
> 0.8234
> -0.6297
> Sharpe of 1.59is below CUtOff of 2.07.
> chng


我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi. worldquantbrain comlalphas/SdnGl4z
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 17.925
> 2.3 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三 Q6 &
> 15
> IaXTTaCE
> OFF
> operatorcount
> 酏*
> 1Of1
> 个 b = X
> 17
> "language
> IFASTEXPR"
> 18
> IVis0a1i2ation"
> false
> 19
> startDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> TegUIaT"
> 23
> COCE
> raIk (2
> ISk72_a20p2000_
> OSIT)
> raIk (3
> 10125_
> Chng_IICV_T_
> 工5511
> 2000_
> 30)
> 24
> "description"
> Iaea:
> Dual-Iank PIOCUCT
> Signal
> Combining
> SHOIT
> MnTerest
> anC
> RSS
> Iquidity
> Changes
> 1nRaTi3na12
> for 0a-a
> USeC:
> 1 -
> ISK72
> aTOp2OOO_OSIT:
> RUSSeII
> 2000
> SHOIT
> MnTerest
> percentile
> {几-
> Ic126_chng_
> IITV_T_ISSII
> 2000_
> 30:
> 30 -
> IelatIve Izquzdity
> Change
> SCOIC
> InlnRaionale
> fJI
> OpeIaTOIS
> USee
> 1-
> EXpOnenTiaI
> TransforIs
> CIeaTe
> COIVCX
> Ianking:
> 3a5e-2:
> SHOIT
> Interest
> aMplification
> 3a5e-3
> Htouidity
> change sensitivity
> 1 -
> MulTiplicaive
> Combinazion:
> High when
> boTh
> signals
> agTeE
> Near- ZeIn
> when
> eiTher
> neUTIaI
> {- Negative
> SIgn
> CargeTs:
> High
> SHOIT
> MnTerest
> CeTeriorating
> liquidity
> 1"5hoI
> 50UeeZe
> TIap
> ioentification
> OpezatozCount
> 25
> 27
> "datecreated "
> 2025
> 08-14T05:27:35-04:00
> 75
> rateSwhmitterl"
> 2025-08-15T01:04:25-04:Q0
> alpha C
> day


重复算 operatorCount 操作符了 .

没有  **字段使用数量信息** ，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .

[图片 (图片已丢失)]

**重点** ：巧妙的节省重复操作符 ！！！

从以上几个alpha操作符测试，让我们知道了

i ) +、-、*、/ 和 ^ 都是算入操作符计数的；

ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；

iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha

3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/12/2025 EDT
> anonymoUs
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> brk
> VeC
> Sum(brkl_start_stock_price);
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIBROKER X1.5
> alpha
> ts covariance
> bpk,
> 股票起始价格汇总
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> bpk
> 11同一序列的自相关讦算
> 1.05
> 13.439
> 0.86
> 9.059
> 10.689
> 13.479600
> 24
> 24周期(约1个月)滚动窗0
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0,80
> 14.3096
> 5.2995
> 5.0195
> 40930
> 1157
> 1571
> Instrument Tpe
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> 2014
> .85
> 12.39%
> .90
> 13.2495
> 3.239
> 21.369600
> 1424
> 1722
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> On
> OfT
> 2015
> +28
> 12.59%6
> 1.28
> 12.6295
> 7.6596
> 20.05930
> 1537
> 1751
> 2016
> 1.36
> 13.59%
> 1.57
> 18.2595
> 9.249
> 26.67930
> 1477
> 1690
> 2017
> 0.63
> 11.4796
> 0.32
> -3.20%
> 6.959
> -5.5893o
> 1746
> 1497
> Clone Alpha
> 2018
> 0.72
> 12.4696
> 0.52
> 5.469
> 8.5096
> 10.379530
> 1980
> 1765
> 2019
> 13.25%
> 1.71
> 13.5695
> 5.18%
> 20.47930
> 1757
> 1611
> 2020
> 0.47
> 15.54%
> 0.25
> 2.4495
> 7.5096
> 68930
> 1818
> 1731
> Chart
> Pnl
> 2021
> 14.52%
> 1.17
> 10.8195
> 4.0096
> 14.79930
> 2194
> 2300
> 2022
> 1.17
> 13.7096
> 0.94
> 8.759
> 6.35%
> 12.779530
> 1980
> 2197
> 2023
> 0.48
> 20.3796
> 0.17
> 26Ob
> 8296
> 2.5593o
> 1640
> 1992
> 7,50OK
> SOOOK
> Correlation
> 2,50OK
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,8;43
> Du
> 0.2112
> -0.0733
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
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 8;43
> PM
> 0.4247
> -0.0733
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 8;44
> PM
> 0.3960
> -0.3483


我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain comlalphaslobd5qOE
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 2.545
> 2.41 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> nanHandling"
> OFF
> operatorcount
> 劭
> ? Of1
> 个 b = X
> 16
> IaXTTaCE
> ON
> 17
> "language
> FASTEXPR
> 18
> IVis0ali2ation
> false,
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE"
> Ibrk
> VeC
> SUII ( bIkz_
> STAIT_
> sTOCk_priCe ) ; Irlnalpha
> C5_
> Covariance (IIin
> DIK,
> L 股票起始价格汇总 Irln
> bIk ,
> LL 同-序列的
> 自相关计算 {210
> 24
> J24周期〈约1个月)滚动窗OIrln) ; '
> 24
> "JesCZIptiOn"
> Iaea:
> COIpUTE
> the negatlve IoIIIng
> COVariance
> Of aggTegated
> starting stock prices with itself
> Iea5UIE
> 5e11-similarity
> anO
> invert
> The
> Ielationship
> InRationale
> fJI
> USeO:
> The aggIe
> starting
> STOCK priCe
> (VeC_
> SUII
> (brki_
> STaIT
> sTOCk_price)
> IeTIeCTS
> baseline
> Valuation
> levels
> 35
> boTh
> IpUTS
> COVariance
> CapTUIeS
> i5
> OIII
> Volatility
> and pattern
> consistency
> InRaTionale
> for OperatoIs
> USeC:
> The
> 24-period
> COVariance
> (TS
> COVariance)
> SeIies Iizh
> iself simplifies
> VaTZance
> measUring
> HOWI Uispersed
> The
> Values
> aIe
> aIOUnC
> Their
> IIean
> DVEI
> ShOIt
> term Window.
> The
> negative
> sign (-)
> TIVeITS
> 375,
> 50
> higher
> Variance (inszability)
> IeSUITs
> 11
> IOIeI
> 518na1 ,
> penalizing
> VoIatility
> 25
> OpezatozCount
> 25
> alpha C
> Jaza
> gazed
> Using


事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/01/2025 EDT
> jiao?
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> Vector
> neut
> VeC
> SUN(rSKGG
> offer),
> VeC
> SUm(rsk6o
> Offer)))
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> Simulation Settings
> 1.33
> 10.339
> 1.05
> 7.819
> 16.029
> 15.139600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Equity
> USA
> ILLIQUID_MINVOLIM
> Fast Expression
> 0.08
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.009
> 0.00
> 0.0096
> 00%
> 0093o
> 2014
> 1.30
> 7.1995
> 0.77
> 4.4296
> 1.6296
> 12.36950
> 936
> 1552
> 2015
> -0.29
> 7.5095
> -0.21
> 2.28%
> 8390
> 079330
> 716
> 1825
> Clone Alpha
> 2016
> 1.03
> 7.3295
> 5.4796
> 0996
> 14.93930
> 539
> 1878
> 2017
> 0.77
> 8.3595
> 3.36%
> 4.839
> 0593o
> 555
> 832
> Chart
> Pnl
> 2018
> 1.07
> 13.9099
> 5.29%
> 2.5795
> 7.62930
> 577
> 888
> 2019
> 0.95
> 13.0395
> 5.5596
> 4.98%
> 8.5390
> 512
> 1905
> 2020
> 1.25
> 11.1495
> 1.16
> 10.6596
> 5.11%
> 19.139500
> 464
> 1922
> 2021
> 0.91
> 10.1895
> 0.b
> 79%
> 12.53%
> 13.34930
> 2248
> 2022
> 5.02
> 14.389
> 7.52
> 32.31%
> 2.2796
> 44.9493o
> 1070
> 1821
> 40OOK
> 2023
> -1.55
> 10.6890
> -1.48
> -11.40%
> 2.35%
> -21.32930
> 752
> 1893
> 20OOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;55
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
> Du
> 0.3766
> -0.1774
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;55
> PM
> 0.3713
> -0.1928
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;55
> 00
> IS Testing Status
> Period
> OS
> PM
> 0.6809
> -0.5425


这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =

1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .

[图片 (图片已丢失)]

2. 点塔！

```
点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题
```

当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节： [交一个怎样的alpha能提升你的六维数据之定性定量分析 .](../顾问 WX64154 (Rank 32)/[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析.md)

我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！

关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：

i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)

[图片 (图片已丢失)]

比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 . 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(anl3g
> rOXLCXSpeq
> anl3g_xIcxspemtp)
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> RetUrns
> DrawOOwn
> Margin
> Simulation Settings
> 0.37
> 3.549
> 0.14
> 1.869
> 13.18%
> 10.539600
> Instrument Tpe
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.71
> 3.769
> 1.30
> -7.22%
> 11.439
> -38.389530
> 775
> 1332
> 2014
> 1.18
> 3.1795
> 0.75
> 5.0096
> 3.51%
> 31.53950
> 1058
> 1558
> 2015
> 0.37
> 3.4295
> 0.15
> 2.1796
> 7.36%
> -12.67900
> 1156
> 1557
> Clone Alpha
> 2016
> 1.83
> 3.8795
> 1.84
> 12.6796
> 3.21%
> 65.529530
> 1093
> 1627
> 2017
> 0.58
> 3.3295
> 0.32
> 2.6996
> 5.33%
> 16.2390
> 1172
> 1779
> Chart
> Pnl
> 2018
> 1.81
> 3.43995
> 1.42
> 7.42%
> 3.40%
> 43.25930
> 1135
> 1792
> 2019
> -U.61
> 3.3995
> 0.33
> 3.029
> 4.92%
> -17.9390
> 004
> 1825
> 2020
> 3.5395
> 0.10
> 5696
> 5.6796
> 8.84930
> 998
> 1752
> 2021
> 1.38
> 3.8595
> 5.5896
> 4.20%
> 28.97930
> 1855
> OOOK
> Mlwto
> 2022
> 0.32
> 3,6695
> 0.13
> 9996
> 859
> 10.8593o
> 1072
> 830
> 2023
> -3.70
> 3,0095
> 2.01
> -14.5890
> 0090
> 97.97930
> 970
> 1792
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Margin
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
> 0.27
> 2.2296
> 0.09
> 1.4096
> 14.639
> 12.579600
> Pnl
> Investability Constrained Pnl
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;36
> PM
> 0.2624
> -0.0448
> IS Testing Status
> Period
> OS
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;37
> PM
> 0.8554
> -0.6340
> 5PASS


通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 07/30/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank
> star
> Val
> industry_rank
> anl39
> rOXLCXSpeq
> anl39_xlcxspemtp
> Power Pool Alpha
> Pyramid theme: EURIDIIMODEL X1.4
> Simulation Settings
> Pyramid theme: EURIDIIANALYST X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.45
> 7.5596
> 1.91
> 7.629
> 4.2396
> 20.189600
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> On
> On
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.70
> 6.7096
> 1.04
> 46895
> 1.289
> 13.98900
> 778
> 1329
> Clone Alpha
> 2014
> 3.25
> 7.59%6
> 2.69
> 8.5495
> 1.149
> 22.5035o
> 1070
> 1525
> 2015
> 1.27
> 7.84%
> 0.72
> 2.0595
> 2.839
> 10.359500
> 1113
> 1611
> 2016
> 4,09
> 8.03%
> 2.34
> 12.0895
> .20%
> 35.07930
> 1025
> 695
> Chart
> Pnl
> 2017
> 2.61
> 7.3396
> 1.75
> 5.6295
> #1090
> 15.3390
> 1120
> 831
> 2018
> 3,05
> 7.7096
> 2.30
> 7.10%
> 2.0590
> 18.43900
> 1166
> 1750
> 2019
> 1.27
> 7.56%
> 62
> 3.0195
> 1.70%
> 7.95930
> 1183
> 1625
> 2020
> 2.34
> 8.01%
> 1.94
> 8.6095
> 1.72%
> 21.469530
> 1121
> 1621
> 5OOOK
> 2021
> 2.71
> 86%
> 2.35
> 9.4095
> 3.52%
> 27.40950
> 1122
> 1820
> 2022
> 2.45
> 7.81%6
> 2.27
> 10.75%
> 4.2390
> 27.51930
> 1163
> 1739
> 2,50OK
> 2023
> 3,80
> 7.5596
> 3.63
> 11.8095
> 0.489
> 31.269500
> 1093
> 1672
> Investability constrained
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.88
> 3.599
> 1.30
> 5.9796
> 3.9796
> 33.269600
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025,7.05
> PM
> 00
> IS Testing Status
> Period
> 05
> 0.5189
> -0.0937
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> 8 PASS
> PM
> 0.5189
> -0.1529
> Sharpe of 2.45 is above CUtOff of 1.58.
> Fitness Of 1.91 is above cutoffof1.
> Turnover of 7.5596 is above CUtoff of
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> PM
> Turnover of 7.55% is below cutoff of 70%.
> Weight is well distributed over instruments。
> 0.8288
> -0.4965
> Sub-universe Sharpe of 1.27 is above cutoff of 1.27.
> IS Iadder Sharpe Of 2.49 is above cutoff of 2.02 for Iadderyear 2: 1/20/2023.1/21/2021


ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> OS
> ts_target_
> tvr_decay (imbs_
> SCOre
> Iambda_min-o,
> Iambda
> maX=l, target
> tVr=0.1
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> Simulation Settings
> 2.86
> 7.7796
> 1.98
> 5.979
> 2.319
> 15.379600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.32
> 7.96%
> 2.54
> 7.3295
> 009
> 18.40950
> 1363
> 1355
> 2014
> 5.73
> 7.0796
> 5.12
> 9.999
> 0.739
> 28.259530
> 1569
> 1577
> 2015
> 4.83
> 7.5196
> 264
> 11.5495
> 1.289
> 30.7390
> 1645
> 653
> Clone Alpha 
> 2016
> 2.76
> 7.3796
> .82
> 5.42%
> .6890
> 14.71930
> 1574
> 593
> 2017
> 2.23
> 7.51%
> 3.00
> 5.2995
> 639
> 16.52930
> 1610
> 533
> Chart
> Pnl
> 2018
> 3.49
> 7.81%
> 2.54
> 6495
> .239
> 6.93930
> 1875
> 1871
> 2019
> 2.96
> 7.5596
> 2.04
> 5.9195
> 1.129
> 15.45930
> 645
> 1723
> 2020
> 8.30%6
> 22795
> 1.729
> 5.48930
> 1736
> 1813
> 2021
> .05
> 299
> 2.43%
> 2.31%
> 5.86930
> 2203
> 2291
> 40OOK
> 2022
> 7.97%6
> 0.22
> 1.5195
> .839
> 3.79950
> 2057
> 2121
> 2023
> 11.09%
> 5.57
> 8.2395
> 08%
> 14.85930
> 1783
> 1829
> ZOOOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;33
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
> PM
> 0.3352
> -0.0929
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> Du
> 0.5597
> -0.1764
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> IS Testing Status
> Period
> 0S
> Du
> 0.9227
> -0.5410
> Year


比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .


> [!NOTE] [图片 OCR 识别内容]
> 说到这里,
> 我想说一下关于提交 alpha 关于 Prod Correlation ,
> Power Pool
> Correlation 和 Self Correlation,
> 也许在绿灯亮起提交 alpha 显示出的错误或许不
> 那么明确. (个人看法,如有问题还望大佬们不忘吝啬,
> 可评论区说明我好做出调
> 整)但大致是这样的 .
> 举个例子:有一个国王喜欢吃各种各样式的苹果
> 大家都会送苹果给国王
> 吃,
> 当然会获得相应的报酬,吃之前需要将苹果放进池子进行清洗,
> 有两个大小
> 的池子。如果你送来的苹果好,自然是放在大池子里。和大池子里的苹果比较 ,
> 如果大池子没有类似的苹果,
> 或者如果有类似的苹果,
> 但是你的苹果比这个类似
> 的苹果有更少的瑕疵,那你的苹果将会被收取从而获得报酬;  如果你的苹果不满^
> 足大池子,
> 那就继续按照以上这种方式放小池子,
> 当然这种小池子只是大家人手
> 一个,
> 大池子也是谁想用可以随时搬自己家测试,
> 小池子的作用是什么,如果大
> 池子的苹果被国王吃完了,那就会考虑小池子了,当然人家毕竟是国王,没有那
> 么容易吃完大池子的稀奇苹果.



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 09/11/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> ts_target_
> tvr_decay (imbs_
> SCOre
> mCr63_membership,  Iambda
> min=0
> Iambda
> Iax=l
> targe
> Power Pool Alpha
> Pyramid theme: ASIIDIIIMBALANCE X1.1
> Simulation Settings
> Pyramid theme: ASIIDIIMACRO X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 7.739
> 1.19
> 5.249
> 5.899
> 13.56900
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> 0n
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.03
> 8.02%
> 1.34
> 5.4795
> 2.0596
> 13.63330
> 1377
> 1351
> Clone Alpha 
> 2014
> 2.21
> 7.0596
> 407
> 11.659
> .76%
> 33.089500
> 1573
> 1573
> 2015
> 3.41
> 7.4796
> 293
> 9.20%
> 1.129
> 24.61930
> 670
> 628
> 2016
> +94
> 7.45%6
> 0.47
> 3.16%
> 5.8990
> 48930
> 590
> 1577
> Chart
> Pnl
> 2017
> 2.28
> 7.50%
> 2.8895
> 1.6596
> 12.84930
> 620
> 1623
> 2018
> 2.55
> 7.74%
> .84
> 5.5395
> 1.2996
> 16.879500
> 899
> 1827
> 2019
> .83
> 7.5496
> 1.14
> 4.8795
> .9890
> 12.91930
> 1705
> 653
> 2020
> 0.02
> 8.3296
> 0.00
> 0.059
> 2.259
> 0.1593o
> 800
> 1729
> 2021
> 8.18%6
> 1.21
> 5.159
> .6390
> 12.5893o
> 2305
> 2190
> 2022
> 7.82%
> 0.07
> 0.8795
> 2.5696
> 2.239500
> 2113
> 2055
> ZOOOK
> 2023
> 3.80
> 10.50%
> 3.02
> 7.9295
> 0.1996
> 15.08930
> 864
> 1757
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;43
> PM
> 0.3474
> -0.0437
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.3645
> -0.0892
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.6217
> -0.4420
> PASS
> Vear


事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .

[图片 (图片已丢失)]

3. 好而优的 alpha

何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .

一点：好，我理解在:

1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；

2) fitness ≥ 1  全方面稳定还是非常不错；

3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；

4) returns ≥ 10%  收益还是要好点能赚钱吧；

5) drawdown 回撤越小越好吧，大了心理抗压不行；

6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；

7) 十年数据中做多做空不能太少吧，权重太高危险危险！

8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .

满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/08/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> 1
> OS Summary
> Period
> I5
> 05
> peVerse(r
> ib5
> SCOre
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDOIIMBALANCE
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> Simulation Settings
> 0172112023 CT
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Close
> Close Ratio
> Self-Correlation
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone Alpha
> 2013
> 3.9
> 23.8899
> 4.13
> 26.189
> 2.5995
> 21.929600
> 986
> 405
> 2014
> 3.52
> 22.6895
> 3.36
> 20.65%
> 2.9096
> 18.22930
> 1070
> 431
> 2015
> 3.32
> 22.8295
> 3.46
> 24.43%
> 3.03%
> 21.41950
> 1130
> 459
> Chart
> Pnl
> 2016
> 2.53
> 21.1195
> 2.65
> 21.4796
> 3.4796
> 20.349530
> 1138
> 455
> 2017
> 2.77
> 20.7795
> 2.47
> 16.5496
> 3.40%
> 15.92930
> 1125
> 470
> 2018
> 1.88
> 19.5696
> 1.67
> 15.3796
> 7.27%6
> 15.71930
> 1010
> 418
> 2019
> 2.77
> 19.1395
> 3.03
> 22.829
> 3.18%
> 23.8890
> 998
> 423
> 1ON
> 2020
> 0.71
> 19.4395
> 0.39
> 5.9596
> 5.659
> 2930
> 908
> 392
> 2021
> 1.73
> 19.20%
> 10.789
> 5.089
> 11.22930
> 972
> 416
> 5OOOK
> 2022
> 18.4390
> 1.42
> 14.789
> 4.5795
> 16.0493o
> 050
> 439
> 2023
> 10.22
> 31.6599
> -14.39
> 62.7790
> 3.5796
> 39.67930
> 945
> 393
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
> Pre
> Sharpe
> Pre


二点：优，我理解在:

1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；

2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；

3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；

使用


> [!NOTE] [图片 OCR 识别内容]
> 1
> 1.
> 事件距离基础信号:  距离越大。事件影响越小
> eVent
> signal
> VeC
> SUI
> nWs7g_event_detection_distance_358-
> 1
> 距离平方增骚:  放大极端距离信号的非线性影响
> brk
> VeC
> sum(brkl_start_stock_price);
> distance_squared
> event_signal
> 2;
> alpha
> ts covariance(
> brk,
> 股票起始价格汇总
> 1
> 词频倒数因子:  词数越少。信息浓度越高(1/词数)
> brk,
> 11  同一序列的自相关计算
> Word
> density
> 二 1
> VeC
> SUII
> nWS7g_word_count_391 )
> 24
> 24周期(约1个月)滚动窗口
> 10
> 1
> 复合事件驱动因子:  距离信号
> 非线性增骚
> 信息浓度
> 11
> alpha
> (event_signal
> distance_squared
> Word_density)



> [!NOTE] [图片 OCR 识别内容]
> 11 Core Logic:
> Reverse standardized composite factor
> reverse
> operation when large trader behavior diverges
> 1
> Synthetic
> Base
> Factor: Market
> pattern
> trader Value differential
> base factor
> mdl175 OGam
> power(Vec
> sum(pvz7_value_diff_large_trader), 2);
> /12. standardization: Convert to
> Z-score to eliminate scale effects
> Zscore_factor
> Zscore(base_factor) =
> 1
> Signal Reversal: Negative sign indicates
> Contrarian
> selection, seeking
> undervalued
> opportunities
> alpha
> ZSCOre
> factor;
> large



> [!NOTE] [图片 OCR 识别内容]
> Description
> 507
> 100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template_
> Idea: Identify the time index ofthe maximum imbalance score over a 2O-day Window, then invert the result:
> Rationale for data used: The imbalance score (imb5_score) likely measures order flow or liquidity asymmetry; its maximum pinpoints the
> most extreme positive imbalance event。
> Rationale for operators Used: The 20-dayarg max (ts_arg_max)returns the lookback period (0-19) where the series peaked_and the


不建议使用


> [!NOTE] [图片 OCR 识别内容]
> 1 |
> ts_covariance(vec
> SUm(brkl_start_stock_price) ,
> VeC
> sum(brkI_start_stock_price), 24)



> [!NOTE] [图片 OCR 识别内容]
> brk
> VeC
> sum(brkl_start_stock_price)
> alpha
> ts covariance
> brk,
> 股票起始价格汇总
> bk,
> 11同一序列的自相关计算
> 24
> 1124周期(约1个月)滚动窗口
> );
> alpha


[图片 (图片已丢失)]

**三、alpha模板 ！**

看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .


> [!NOTE] [图片 OCR 识别内容]
> N-1
> Ha
> 1,3N,8.七
> lim
> fa()-Cfa(a)
> 二
> Iim
> fa(a)
> n-〉+O
> n〉+O
> 2二1
> 2二1
> C=N
> 10-P


换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！

field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .

其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> 2,000
> UUJ
> OIlU
> 〈ee
> 3" A0。
> 02
> Displayed Period
> 02/14/2025
> 09/12/2025
> 149346
>  Mar
>  Mar
> Mar
> Mar
> Mar
> 30。
> 31。
> 24。


从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .

[图片 (图片已丢失)]

使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .

造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .

[图片 (图片已丢失)]

下节预告:  [Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析](../顾问 WX64154 (Rank 32)/[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析.md)

2025年9月14日

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，通过add点塔这个小技巧倒是真的学到了

不过发现自己两个per的数据都是大佬的一倍，作为gold感觉冲expert是有点艰难了

===================================================================================


---

### 技术对话片段 145 (原帖: 【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 冲刺genius !
> 细节决定成败,你的六维还能提升 ! &模板
> 
> 
> 首先感谢游戏王 (2559763) ,
> 橘子姐
> (6383096) ,
> base payment 拉满的
> 大佬 (AH18340) 以及 上海 (MF59400)等等的帮助.也许你们自己都不知道 ,
> 但是潜移默化
> 的影响了我,
> 下面阐述的其中有-些内容是我在游戏王那里学习到的.


## **一、Genius定级与何相干？**

总体来说，一共与两方面有关，一是  **硬性指标** ，二是  **软指标** 。


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-03,July 1st, 2025
> September 3Oth; 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 266
> Reached Grandmaster
> 20
> 120
> 220
> Pyramids Completed
> 72
> Reached Grandmaster
> 10
> 30
> Combined Alpha Performance
> 2.39
> Reached Grandmaster
> 0.5


其中  **硬性指标** 包括由

1. 本季度 Signals (阿尔法)；

2. 本季度 Pyramids (金字塔)；

3. Combined Alpha Performance (提交的所有alpha表现)；

4. Combined Selected Alpha Performance (被选中的alpha费后表现)

5. Combined Power Pool Alpha Performance (power pool alpha表现)

五部分组成；

```
点亮金字塔(俗称:点塔)表现为 同大区同Delay同数据集 提交至少3个alpha，不计倍数塔。
```

我们以Expert (专家)为例，硬性指标必须同时满足

1. 本季度alpha数量 Signals ≥ 20；

2. 本季度金字塔数量 Pyramids ≥ 10，

3. max(Combined Alpha Performance, Combined Selected Alpha Performance, Combined Power Pool Alpha Performance) ≥ 0.5

       这三个条件，才算达到Expert级别，但这并不代表最终定级，因为达到Expert的人数会超过 WorldQuant 的预期，所以就必然会出在淘汰制，优胜就指定在软指标(六维数据).

[图片 (图片已丢失)]

**软指标** 又称为“六维数据”，六维六维 很明显就是说有六个维度(指标)。

**
> [!NOTE] [图片 OCR 识别内容]
> What happens 迂 more consultants qualify for a level than there are available
> If more consultants meet the base criteria for
> level than there are available Spots
> a tiebreaker criterion is used _
> This is based on a sum Of ranks across the following metrics
> 1.
> distinct Operators
> Alpha (Lower is better )
> 2.
> distinct Fields
> Alpha (Lower is better)
> 3. Total distinct Operators (Higher is better)
> 4
> Total distinct Fields (Higher is better)
> 5. Maximum Simulation Streak
> Best streak of
> consultant that ends i that quarter
> OI
> continues into the next quarter
> Streak does not reset to 0 every quarter。
> 6. Community leader
> Forum
> Number Of Likes on Posts Or comments that are
> published as Of the end Of quarter
> Ninimm length of post Or comment must be 100 characters。
> Referral
> Total number Of successful referrals i the quarter
> A referral is considered
> Slccessfil
> Khen the
> referring consultant h as become eligible to accrte the referral fee for someone
> have referred to BRAIN
> 讧 accordance with the guidelines Of the referral fee program
> Spots?
> Avg
> AVg
> they
**

**
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st, 2025
> September 3Oth, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.41
> 68
> 1.54
> Fields used
> Community activity
> Max simulation streak
> 260
> 33.2
> 88
**

其中  **软指标** (六维数据)包括由本季度

1. Operators per Alpha (每个alpha的平均(不去重)操作符数量)；

2. Operators used (操作符的去重使用个数)；

3. Fields per Alpha (每个alpha的平均(不去重)字段数量)；

4. Fields used (字段使用(去重)数量)

5. Community activity (rank[社区活跃程度])

6. Max simulation streak (最大连续回测天数)

六部分组成；

```
·其中软指标第1，3条越小越好；2，4，5，6条越大越好，也就是含有per的越小越好，其他反之；·rank(社区活跃程度)可以通过参加会议、写帖子和帖子下评论(数量计分)以及拉新人[游戏王]；·Max simulation streak 是难以撼动的，只能保持。“你断下回测试试会有啥后果没”佬调侃到。
```

[图片 (图片已丢失)]

## **二、冲刺 Genius !**

通过第一部分我们知道了Genius是怎么定级，同时优胜制是与六维数据相关。

1. 关于六维数据  **细节**

这部分我们娓娓道来，关于六维数据我们能做的是什么?

i ) 保持 Max simulation streak 最大回测天数 不要断 !!! ；

ii ) 论坛咱们尽量多的去逛，不单单只是为了一点赚取社区分，论坛一定是包含某种强大的思想，无论是技术上还是学习上，有时小小的一个点就会让你悄无声息上一个层次；

iii ) 尽量拉满自己的Operators used，当然这个小gold会有一些吃亏(大佬们的Operators used会更加的多更加饱满一些)，多去尝试自己有而没有使用过的Operators used，都是会跑出alpha来的；

iv ) 关于 Fields used ，当我们在使用某alpha模板时，通常会跑出来某同数据集完全可以提交的alpha, 且alpha的phl是相似的，alpha各方面都比较均衡，这时我们就要选取那个我们没有使用的字段的alpha；

v ) Operators per Alpha 和 Fields per Alpha 两个 per，也是重要的指标，权衡谁强谁软，大家都会比较这唯一的两个per，下面我们仔细讲讲这两个指标细节 .

首先，讲讲我的一些  **蠢行为! ,** 等等上面还有一点重要的忘记说了， **要保持区域、Delay以及数据集多样性！**

**
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st, 2025
> September 3Oth, 2025
>  Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Fundamental
> Insiders
> Macro
> Mogel
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Social Media
> Earnin3s
**

使用关于金字塔的api控制自己的点塔行为，能找到alpha的情况下最好少在一个数据集点，一般来说某区域某Delay某数据集一般来说最多  **8~10**  个alpha最好 (个人见解)，同时还要自己的alpha分布比较均匀，比如：某区域delay数据集占比不能超过30%最好，某数据集占比太高甚至会被禁止使用此数据集字段 . 游戏王等大佬说D0的少做，特别是CHN区域的.


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Delayo
> NAN
> Delayl
> NAN
> Fundamental data
> Fundamental data
> Analyst data
> Analyst data
> Broker
> Broker
> News data
> News data
> Social media data
> Social media data
> Sentiment data
> Sentiment data
> Price VOluMe data
> Price Volume data
> Option data
> Option data
> Eamings
> Earnings
> Insiders
> Insiders
> Instiutional Ownership Data
> Instiutional Ownership Data
> Short interest data
> Short interest data
> Macro data
> Macro data
> Other
> Other
> Risk data
> Risk data
> Model data
> Model data
> USA
> ASI
> CHN
> EUR
> GL
> HKG
> KOR
> TVN
> AMR
> JPN
> USA
> ASI
> CHN
> EUR
> GLB
> HKG
> KOR
> TVN
> AMR
> JPN
> Click to drill down
> EUR
> ASI
> GLB
> USA
> CHN


保持区域多样性这个比较重要，会与Combine直接相关. 另外把某个地方多的alpha存起来，放在下一个季度去交，能直接增加两项硬性指标(alpha和金字塔数量)，岂不美哉.

[图片 (图片已丢失)]

接下来继续讲我的蠢行为，我曾以为 +、-、*、/ 和 ^ 等等和操作符 add(x, y)、multiply(x ,y, ... , filter=false)、divide(x, y)以及power(x, y)效果相同，但是不算操作符...，


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/26/2025 EDT
> 顾问 ML47973 (Rank 100)
> Add Alphato
> LiSt
> Code
> IS Summary
> Period
> IS
> 05
> power(2,
> md177_astcomp
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> Simulation Settings
> 1.65
> 6.11%
> 2.64
> 31.939
> 16.609
> 104.449600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Subindustry
> On
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 1.69
> 5.46%
> 1.56
> 10.65%
> 4.76%
> 39.05920
> 1999
> 357
> 2019
> 4.949
> 1.71
> 18.5896
> 8.66%
> 75.279620
> 1988
> 375
> 2020
> -0.,04
> 029
> 0.01
> 0.5596
> 15.18%
> 82920
> 2010
> 375
> Clone Alpha 
> 2021
> 2.46
> 699
> 4.84
> 48.489
> 15.30%
> 122.899620
> 2142
> 380
> 2022
> 2.44
> 7.42%
> 6.08
> 77.70%
> 13.23%
> 209.41920
> 2136
> 390
> Chart
> Pnl
> 2023
> 3.61
> 6.13%
> 7.40
> 52.519
> 1.71%
> 171.19920
> 2114
> 397
> 匣
> Correlation
> 1ON
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,4;51
> PM
> 0.6840
> -0.0542
> OOOK
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,4;51
> Du
> 0.4204
> -0.1633
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 4;51
> 0
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul "22
> Jan '23
> Du
> 0.6874
> -0.6201
> Vear



> [!NOTE] [图片 OCR 识别内容]
> 这个 Q 当时让我 base payment 日 赚54.816 ,当时 iqc 结束 ,第一次0f更新0.86


直到我使用华子哥的插件才发现


> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 美东时间:2025/9/1200:38:06 北京时间: 2025/9/1212:38:06
> 在你可用的运算符中。共有67种运算符被使用。12种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统一为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x, Y, filter
> false); X + y
> 52
> COMBO,REGULARSELECTION
> base
> Arithmetic
> multiply(x ,y
> filterzfalse); X * y
> 76
> COMBO,REGULARSELECTION
> base
> Arithmetic
> sign(x)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> subtract(x, Y, filter-false) X -Y
> 157
> COMBO,REGULARSELECTION
> base
> Arithmetic
> pasteurize(x)
> COMBO,REGULAR
> genius
> Arithmetic
> log(x)
> COMBOREGULARSELECTION
> base
> Arithmetic
> maXfx;y
> COMBO,REGULARSELECTION
> base
> Arithmetic
> absfx)
> COMBO,REGULARSELECTION
> base
> Arithmetic
> divide(x; y), XIy
> 158
> COMBO,REGULARSELECTION
> base


我的 + - * / 和 ^ 操作符数量十分高，于是我便知道了，他们效果一样，算操作符也是一样的算 法，于是我开始研究操作符和操作符重复使用的情况，此时我还在怀疑使用 vec_op 会不会提高 op_per，结果就是会算操作符会提高 op_per，那很糟糕了！

下面的操作有几率  **降低** 你的  ***Operators per Alpha*** ，和想要查看自己的alpha数据也可以认真看一下

在 postman (或者apifox) 上登录你的worldquant账号, (其中Cookie由你的账号和密码编码而来)


> [!NOTE] [图片 OCR 识别内容]
> #  登录 (login)url
> CUrl
> --location
> --request
> POST
> https : / /api. worldquantbrain . com
> authentication
> header
> Authorization:
> Basic MZAZODUBMTAZOEBXcSSjbzeGQUYrQUYrQUYgMBFG
> ~-header
> Cookie:
> t=eyJeeXAiOiJKVIQiLCJhbGciOiJIUZIINiJg .eyJqdGkioi -



> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> login
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> POST
> https:Hapi.orldquantbrain comlauthentication
> Send
> Environments
> POST Simulation
> Params
> Authorization
> Headers (10)
> Body
> Scripts
> Settings
> Cookies
> PATCH alpha-adjust
> FIOws
> Auth Type
> GET data-fields
> Username
> 30-510
> COm
> Basic Auth
> GET alpha
> History
> GET Check
> Password
> The authorization header will be
> POST submit
> 0+
> automatically qenerated when yoU send the
> GET Self-COrr
> Body
> Cookies
> Headers (20)
> Test Results
> 201 Created
> 1.975
> 1.14 KB
> Save Response
> GET data-sets
> JSON
> Preview
> Visualize
> 三
> Q  @
> GET
> pyramid
> USET"
> id
> 顾问 ML47973 (Rank 100)
> Loken"
> EXDiTy
> 14400
> DeTmissions
> BEFORE
> ANID_
> AFTER
> PERFORMANCE_
> 10
> BRAIN_LA3S"
> 11
> BRAIN_LABS_JUPYTER
> L43
> 12
> CONSULTANTI
> 13
> "MULTI_SIMULATION "
> 14
> PROD_ALPHAS
> 15
> REFERRAL
> 16
> SUPER_ALPHA "
> 17
> IVISUALIZATION"
> 18
> WORKDAY"
> 19
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> 9@.


下面的是查询alpha信息的url


> [!NOTE] [图片 OCR 识别内容]
> #
> check_alpha_info 其中{alpha_id} 使用alpha_id替代即可
> Curl
> -location
> https : / /api .worldquantbrain . com/alphas / {alpha_id}
> -header
> Cookie:
> tseyJeexAioiJKVIQiLCJhbGciOiJIUZIINiJ9 .eyJqdGkioi


接下来我们就来看看几个alpha，查看它们的数据情况

1 ）alpha表达式：“ - (1 / imb5_score) ”     —>    EUR-TOP2500-D1-OFF  id= '80PXEEz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/09/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> ib5
> SCOFe
> Single Data Set Alpha
> 俳
> Power Pool Alpha
> Pyramid theme: EURIDIIIMBALANCE X2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawJown
> Margin
> Simulation Settings
> 3.37
> 22.089
> 2.26
> 9.9396
> 2.4596
> 9.009o0
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.02
> Statistical
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 5.19
> 23.9499
> 200
> 14.1990
> 1.08%
> 11.8590
> 1324
> 781
> 2014
> 4.55
> 23.2595
> 3.25
> 11.85%
> 0.78%
> 10.20950
> 1612
> 1005
> 2015
> 4.20
> 23.68%
> 3.26
> 13.02%
> 1.31%
> 11.00930
> 1101
> Clone Alpha
> 2016
> 4.52
> 22.9795
> 3.52
> 13.78%
> 1.65%
> 11.99930
> 627
> 1092
> 2017
> 4.22
> 22.0095
> 2.79
> 9.519
> 0.9190
> 8.72930
> 1749
> 1203
> Chart
> Pnl
> 2018
> 3.4
> 21.699
> 2.37
> 10.29%
> 20%
> 499
> 1714
> 1212
> 2019
> 3.26
> 21.4495
> 2.26
> 10.32%
> 1.23%
> 52930
> 1665
> 1162
> 2020
> 1.99
> 21.1495
> 1.12
> 6.6296
> 2.4596
> 2890
> 1616
> 1125
> 2021
> 2.52
> 20.1895
> 47
> 6.729
> 1.02%
> 58930
> 1703
> 1259
> 7,50OK
> 2022
> 1.37
> 20.139
> 0.67
> 4.839
> 2.29%
> 4.80930
> 652
> 1240
> 5,0OOK
> 2023
> -11.03
> 29.179
> 10.18
> -24.859
> 1.539
> -17.0293o
> 1505
> 1077
> 2,50OK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.99
> 8.649
> 1.44
> 6.5296
> 8.4096
> 15.089600
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 5;43
> PM
> 0.1456
> -0.0393
> 00
> IS Testing Status
> Period
> 05
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 5;43
> PM
> 0.6239
> -0.0916
> 6 PASS
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 5;43
> Sharpe Of 3.37 is above CUtOff of 1.58。
> PM
> Fitness Of 2.26 is above cutoff of 1
> 0.7043
> -0.3995
> Turnover of 22.089 is above cutoff of 1%
> Turnover of 22.08% is below cutoff of 70%


仅仅使用了- 和 / 操作符，我们来查看此alpha的操作符使用情况


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain.comlalphas BOPXEEZ
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 3.06
> 2.19 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> IaXTTaCE
> OFF
> operatorcount
> _
> 1Of1
> 个 b = X
> 17
> "language
> FASTEXPR'
> 18
> IVis0a1i2ation"
> false,
> 19
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE
> imb5_
> SCOIC!
> 24
> description
> Iaea:
> Take
> The
> negative
> Inverse
> O1 The
> inbalance
> SCOIE
> -0
> CIeaTe
> ConTLaLian Signal
> That
> elphasizes
> anC
> fLips
> The
> OIIgInal Ielatzonsh-p. InRatzonale
> for
> 0a-a
> USeC
> The
> inbalance
> SCOIE
> (imb5_
> SCOIE )
> Iikely
> IIea5ULe5
> OIOEI
> fIOW
> OI
> Iiquidity
> aSyIIeTTy;
> Its Inverse highlishts periods
> O1 balance,
> and
> The
> negative sign
> fuITher
> inverts
> The signal. InRationale
> fJI
> OperatoIs  used:
> The
> inVerBe
> (1/x)
> TTansfoIms high
> imbalance
> Into
> Ioy
> Values
> anC
> CHe
> negative sign
> (-〉 Iips
> The
> OUTpU
> PTLOIICIZe
> Conci-inns Where
> The OLiginal
> SCOIe
> Is negative (e.8
> sellIng pressuTe)
> bUT
> OWI
> appears
> positive signals
> 25
> ODeratozCount
> 25
> 27
> UateCzeated "
> 2025
> 09-09T01:43:59
> 04:00
> 28
> "dateSubmitted "
> 2025-09-09102:20:35-04:00
> "datelodified
> 2025-09-13109:42:37
> 04:00
> Online
> Find and replace
> Console
> Postbot
> Runner
> C Start Proxy
> Cookies
> Vault
> Trash
> alpha C


只能查看到操作符的使用情况，而看不到字段的使用情况。使用了两个操作符，也就是 - 和 / 操作符

2 ）alpha表达式：“ - rank(2 ^ rsk72_atop2000_dsrt) * rank(3 ^ mdl26_chng_rltv_t_rssll_2000_30) ”      —>     CHN-TOP2000U-D1-OFF  id= '5dnGLAz'


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 08/14/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(2
> rsk72_atopzooO_dsrt
> rank
> mdl26
> FLtV
> rsSII
> 2000_30_
> Power Pool Alpha
> Pyramid theme: CHNIDIIRISK X1.4
> Simulation Settings
> Pyramid theme: CHNIDIIMODEL X1.6
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaNHar
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> RetUrns
> Drawdown
> Margin
> 1.59
> 48.989
> 0.96
> 17.739
> 14.389
> 7.249600
> Equity
> CHN
> TOPZOOOU
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3,00
> 50.9796
> 2.14
> 25.8395
> 3.459
> 10.14930
> 376
> 311
> Clone Alpha
> 2014
> 3.19
> 50.37%6
> 2.39
> 28.3395
> 4.5996
> 11.259530
> 449
> 375
> 2015
> .99
> 43.99%
> 1.76
> 32.2995
> 14.38%
> 15.5935o
> 726
> 502
> 2016
> 2.15
> 46.26%
> 22.0595
> 5.0596
> 9.5390
> 675
> 556
> Chart
> Pnl
> 2017
> 0.46
> 46.93%
> 0.14
> 43895
> 8.6795
> 879530
> 595
> 501
> 2018
> 1.31
> 48.3796
> 0.64
> 11.6395
> 4.6796
> 83900
> 554
> 455
> 2019
> 2.07
> 50.56%
> 1.22
> 17.6995
> 4.11%
> 9850
> 524
> 420
> 2020
> 0.17
> 50.68%
> 0.03
> -1.9695
> 10.9096
> 0.77930
> 542
> 427
> 1ON
> 2021
> 51.20%
> 0.38
> 11.1295
> 9.73%
> 4.34900
> 543
> 425
> 2022
> 50.5696
> 1.12
> 20.1999
> 5.7390
> 7.979530
> 552
> 447
> 5,00OK
> 2023
> 10.25
> 50.3896
> 10.51
> 52.9395
> 2496
> 21.019500
> 562
> 484
> Risk neutralized
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgown
> Margin
> 1.17
> 48.989
> 0.39
> 5.4296
> 18.579
> 2.219600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.52
> 42.179
> 0.97
> 17.049
> 14.409
> 8.089600
> IS Testing Status
> Period
> IS
> 05
> [
> Correlation
> 8 PASS
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 6;01
> Turnover of 48.989 is above cutoff of 1%
> PM
> Turnover of 48.98% is below cutoff of 70%
> Weight is well distributed over instruments。
> Returns Of 17.73% is above cutoff of 8%.
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 6;01
> Sub-universe Sharpe of 1.55 is above Cutoff of 1.13.
> PM
> Robust universe Sharpe of 1.30 is above CUtoff of 0.64 (40% of Alphal
> 0.8918
> -0.2468
> Robust universe returns of 9.139 is above cutoff of 7.09% (40% of Alphal.
> These pyramid themes match with the following multipliers: CHN/DI/RISK-
> 1.4; CHNIDIIMODEL
> 1.6.The final
> pyramid theme multiplier is 1.4. Effective pyramid count for Genius is 2。
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025
> 6;01
> PM
> 5WARNING
> 0.8234
> -0.6297
> Sharpe of 1.59is below CUtOff of 2.07.
> chng


我们来看一下操作符的使用，如果操作符信息返回6个，说明操作符重复计算；返回5个说明操作符没有重复计算! 来看结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> SaVe
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi. worldquantbrain comlalphas/SdnGl4z
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 17.925
> 2.3 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三 Q6 &
> 15
> IaXTTaCE
> OFF
> operatorcount
> 酏*
> 1Of1
> 个 b = X
> 17
> "language
> IFASTEXPR"
> 18
> IVis0a1i2ation"
> false
> 19
> startDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> TegUIaT"
> 23
> COCE
> raIk (2
> ISk72_a20p2000_
> OSIT)
> raIk (3
> 10125_
> Chng_IICV_T_
> 工5511
> 2000_
> 30)
> 24
> "description"
> Iaea:
> Dual-Iank PIOCUCT
> Signal
> Combining
> SHOIT
> MnTerest
> anC
> RSS
> Iquidity
> Changes
> 1nRaTi3na12
> for 0a-a
> USeC:
> 1 -
> ISK72
> aTOp2OOO_OSIT:
> RUSSeII
> 2000
> SHOIT
> MnTerest
> percentile
> {几-
> Ic126_chng_
> IITV_T_ISSII
> 2000_
> 30:
> 30 -
> IelatIve Izquzdity
> Change
> SCOIC
> InlnRaionale
> fJI
> OpeIaTOIS
> USee
> 1-
> EXpOnenTiaI
> TransforIs
> CIeaTe
> COIVCX
> Ianking:
> 3a5e-2:
> SHOIT
> Interest
> aMplification
> 3a5e-3
> Htouidity
> change sensitivity
> 1 -
> MulTiplicaive
> Combinazion:
> High when
> boTh
> signals
> agTeE
> Near- ZeIn
> when
> eiTher
> neUTIaI
> {- Negative
> SIgn
> CargeTs:
> High
> SHOIT
> MnTerest
> CeTeriorating
> liquidity
> 1"5hoI
> 50UeeZe
> TIap
> ioentification
> OpezatozCount
> 25
> 27
> "datecreated "
> 2025
> 08-14T05:27:35-04:00
> 75
> rateSwhmitterl"
> 2025-08-15T01:04:25-04:Q0
> alpha C
> day


重复算 operatorCount 操作符了 .

没有  **字段使用数量信息** ，我们怎么知道重复字段有没有计数，对于Fields per Alpha 位于1-2之间或者是整数的最好办，我的Fields per Alpha = 1.54，我尝试了 op(f1, f1)，结果Fields per Alpha降低，说明字段不重复计算；如果Fields per Alpha上升，说明重复计算 .

[图片 (图片已丢失)]

**重点** ：巧妙的节省重复操作符 ！！！

从以上几个alpha操作符测试，让我们知道了

i ) +、-、*、/ 和 ^ 都是算入操作符计数的；

ii ) vec_op（vec_sum 和 vec_avg）也是操作符计数的；

iii ) 重复的操作符也是计数的， 会影响 六维之一的 Operators per Alpha

3 ）alpha表达式： “见下图方框内”     —>    ASI-MINVOL1M-D1-OFF


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/12/2025 EDT
> anonymoUs
> udd Nphato
> List
> Code
> IS Summary
> Period
> IS
> 05
> brk
> VeC
> Sum(brkl_start_stock_price);
>  Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: ASIIDIIBROKER X1.5
> alpha
> ts covariance
> bpk,
> 股票起始价格汇总
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> bpk
> 11同一序列的自相关讦算
> 1.05
> 13.439
> 0.86
> 9.059
> 10.689
> 13.479600
> 24
> 24周期(约1个月)滚动窗0
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0,80
> 14.3096
> 5.2995
> 5.0195
> 40930
> 1157
> 1571
> Instrument Tpe
> Region
> Unierse
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> 2014
> .85
> 12.39%
> .90
> 13.2495
> 3.239
> 21.369600
> 1424
> 1722
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> On
> OfT
> 2015
> +28
> 12.59%6
> 1.28
> 12.6295
> 7.6596
> 20.05930
> 1537
> 1751
> 2016
> 1.36
> 13.59%
> 1.57
> 18.2595
> 9.249
> 26.67930
> 1477
> 1690
> 2017
> 0.63
> 11.4796
> 0.32
> -3.20%
> 6.959
> -5.5893o
> 1746
> 1497
> Clone Alpha
> 2018
> 0.72
> 12.4696
> 0.52
> 5.469
> 8.5096
> 10.379530
> 1980
> 1765
> 2019
> 13.25%
> 1.71
> 13.5695
> 5.18%
> 20.47930
> 1757
> 1611
> 2020
> 0.47
> 15.54%
> 0.25
> 2.4495
> 7.5096
> 68930
> 1818
> 1731
> Chart
> Pnl
> 2021
> 14.52%
> 1.17
> 10.8195
> 4.0096
> 14.79930
> 2194
> 2300
> 2022
> 1.17
> 13.7096
> 0.94
> 8.759
> 6.35%
> 12.779530
> 1980
> 2197
> 2023
> 0.48
> 20.3796
> 0.17
> 26Ob
> 8296
> 2.5593o
> 1640
> 1992
> 7,50OK
> SOOOK
> Correlation
> 2,50OK
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,8;43
> Du
> 0.2112
> -0.0733
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
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 8;43
> PM
> 0.4247
> -0.0733
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 8;44
> PM
> 0.3960
> -0.3483


我们将重复的 vec_op 使用变量代替，操作符会被计算几次呢？当然，不用变量代替肯定会计算两次，下面看查询结果


> [!NOTE] [图片 OCR 识别内容]
> Home
> Workspaces
> API Network
> Search Postnan
> Ctrl
> Invite
> Upgrade
> Q's Workspace
> New
> Import
> POST Iogin
> GET alpha
> No environment
> Search COllections
> Worldquant
> alpha
> Save
> Share
> Colleczions
> Worldquant
> POST
> login
> GET
> https:Ilapi.worldquantbrain comlalphaslobd5qOE
> Send
> Environments
> POST Simulation
> P3r3ms
> Authorization
> Headers (8
> Body
> Scripts
> Settings
> Cookies
> PATCH
> adjust
> FIOws
> Query Params
> GET data-fields
> Key
> Value
> Description
> Bulk Edit
> GET alpha
> History
> GET Check
> Key
> Value
> Description
> 00
> POST submit
> 0+
> GET Self-COrr
> GET data-sets
> Body
> Cookies (1)
> Headers (20)
> Test Results
> 200 OK
> 2.545
> 2.41 KB
> Save Response
> GET
> pyramid
> JSON
> Preview
> Visualize
> 三Q G
> 15
> nanHandling"
> OFF
> operatorcount
> 劭
> ? Of1
> 个 b = X
> 16
> IaXTTaCE
> ON
> 17
> "language
> FASTEXPR
> 18
> IVis0ali2ation
> false,
> staztDate
> 2013-01-20
> 20
> EncDate
> 2023
> 01-20
> 21
> 22
> Tegular"=
> 23
> COCE"
> Ibrk
> VeC
> SUII ( bIkz_
> STAIT_
> sTOCk_priCe ) ; Irlnalpha
> C5_
> Covariance (IIin
> DIK,
> L 股票起始价格汇总 Irln
> bIk ,
> LL 同-序列的
> 自相关计算 {210
> 24
> J24周期〈约1个月)滚动窗OIrln) ; '
> 24
> "JesCZIptiOn"
> Iaea:
> COIpUTE
> the negatlve IoIIIng
> COVariance
> Of aggTegated
> starting stock prices with itself
> Iea5UIE
> 5e11-similarity
> anO
> invert
> The
> Ielationship
> InRationale
> fJI
> USeO:
> The aggIe
> starting
> STOCK priCe
> (VeC_
> SUII
> (brki_
> STaIT
> sTOCk_price)
> IeTIeCTS
> baseline
> Valuation
> levels
> 35
> boTh
> IpUTS
> COVariance
> CapTUIeS
> i5
> OIII
> Volatility
> and pattern
> consistency
> InRaTionale
> for OperatoIs
> USeC:
> The
> 24-period
> COVariance
> (TS
> COVariance)
> SeIies Iizh
> iself simplifies
> VaTZance
> measUring
> HOWI Uispersed
> The
> Values
> aIe
> aIOUnC
> Their
> IIean
> DVEI
> ShOIt
> term Window.
> The
> negative
> sign (-)
> TIVeITS
> 375,
> 50
> higher
> Variance (inszability)
> IeSUITs
> 11
> IOIeI
> 518na1 ,
> penalizing
> VoIatility
> 25
> OpezatozCount
> 25
> alpha C
> Jaza
> gazed
> Using


事实证明，本来会被算四次操作符的使用变量代替，变成三个了，会节省重复的操作符数量，从而提升此alpha六维之一的  Operators per Alpha . 当我们使用复杂的 alpha 模板时，可能会节省 3 ~ 4 操作符的情况也是会有的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/01/2025 EDT
> jiao?
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> Vector
> neut
> VeC
> SUN(rSKGG
> offer),
> VeC
> SUm(rsk6o
> Offer)))
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawgwn
> Margin
> Simulation Settings
> 1.33
> 10.339
> 1.05
> 7.819
> 16.029
> 15.139600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> Equity
> USA
> ILLIQUID_MINVOLIM
> Fast Expression
> 0.08
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.00
> 0.009
> 0.00
> 0.0096
> 00%
> 0093o
> 2014
> 1.30
> 7.1995
> 0.77
> 4.4296
> 1.6296
> 12.36950
> 936
> 1552
> 2015
> -0.29
> 7.5095
> -0.21
> 2.28%
> 8390
> 079330
> 716
> 1825
> Clone Alpha
> 2016
> 1.03
> 7.3295
> 5.4796
> 0996
> 14.93930
> 539
> 1878
> 2017
> 0.77
> 8.3595
> 3.36%
> 4.839
> 0593o
> 555
> 832
> Chart
> Pnl
> 2018
> 1.07
> 13.9099
> 5.29%
> 2.5795
> 7.62930
> 577
> 888
> 2019
> 0.95
> 13.0395
> 5.5596
> 4.98%
> 8.5390
> 512
> 1905
> 2020
> 1.25
> 11.1495
> 1.16
> 10.6596
> 5.11%
> 19.139500
> 464
> 1922
> 2021
> 0.91
> 10.1895
> 0.b
> 79%
> 12.53%
> 13.34930
> 2248
> 2022
> 5.02
> 14.389
> 7.52
> 32.31%
> 2.2796
> 44.9493o
> 1070
> 1821
> 40OOK
> 2023
> -1.55
> 10.6890
> -1.48
> -11.40%
> 2.35%
> -21.32930
> 752
> 1893
> 20OOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;55
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
> Du
> 0.3766
> -0.1774
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;55
> PM
> 0.3713
> -0.1928
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;55
> 00
> IS Testing Status
> Period
> OS
> PM
> 0.6809
> -0.5425


这个 alpha 处在备选库中我还没有交，因为它13年做多做空数据为0，倘若使用变量 a =

1 / vec_sum(rsk60_offer)，那将使得此 alpha 节省两个操作符数量 .

[图片 (图片已丢失)]

2. 点塔！

```
点塔 从来都不是靠if_else算子来混塔！！！倒是可以用来点塔以及混合解决 Operators used问题
```

当我们在使用 == 和 != 等等 Operators used 时，常常是需要跟判断逻辑if_else、and 和 or 联系的 . 用来提高自己的Operators used，但在提高自己的Operators used时，同时也增加操作符，增大了此 alpha 的 Operators per Alpha，我们应该怎么来权衡这种利弊呢，请期待下一节： [交一个怎样的alpha能提升你的六维数据之定性定量分析 .]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

我理解一二三阶是一个循环嵌套的过程，我这里就是一种平行平替的点塔方式！

关于点塔，我想大家都比较关心，因为这项硬性指标直接挂钩Genius等级 . 我点塔一般来说一共有两点想法：

i ）在相关性低的情况下，有些alpha的表现还行，比如：sharpe = 0.94, fintess = 0.81，returns = 9.24%, margin = 12.3 / 万这样的数据，或者phl看起来比较规律，可以先自己调节参数，如果调节不上去，可以通过调节alpha来达到挽救的效果，op(f(f1)) —> op(f(f1 op f2))，其中 f2 属于要点的塔 (建议自己程序去匹配一下塔的api， 从而实现点塔)

[图片 (图片已丢失)]

比如：1. 看着一个较差的alpha，sharpe = 0.37, fitness = 0.14，但是Margin > 万10，还有看着phl曲线有上升趋势且较规律，此时我就会使用add来匹配还未点的塔. 使用+、-、* 和 / 都可以，需要自己看phl而定 . 
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> anonymoUs
> Add Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank(anl3g
> rOXLCXSpeq
> anl3g_xIcxspemtp)
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> RetUrns
> DrawOOwn
> Margin
> Simulation Settings
> 0.37
> 3.549
> 0.14
> 1.869
> 13.18%
> 10.539600
> Instrument Tpe
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> -1.71
> 3.769
> 1.30
> -7.22%
> 11.439
> -38.389530
> 775
> 1332
> 2014
> 1.18
> 3.1795
> 0.75
> 5.0096
> 3.51%
> 31.53950
> 1058
> 1558
> 2015
> 0.37
> 3.4295
> 0.15
> 2.1796
> 7.36%
> -12.67900
> 1156
> 1557
> Clone Alpha
> 2016
> 1.83
> 3.8795
> 1.84
> 12.6796
> 3.21%
> 65.529530
> 1093
> 1627
> 2017
> 0.58
> 3.3295
> 0.32
> 2.6996
> 5.33%
> 16.2390
> 1172
> 1779
> Chart
> Pnl
> 2018
> 1.81
> 3.43995
> 1.42
> 7.42%
> 3.40%
> 43.25930
> 1135
> 1792
> 2019
> -U.61
> 3.3995
> 0.33
> 3.029
> 4.92%
> -17.9390
> 004
> 1825
> 2020
> 3.5395
> 0.10
> 5696
> 5.6796
> 8.84930
> 998
> 1752
> 2021
> 1.38
> 3.8595
> 5.5896
> 4.20%
> 28.97930
> 1855
> OOOK
> Mlwto
> 2022
> 0.32
> 3,6695
> 0.13
> 9996
> 859
> 10.8593o
> 1072
> 830
> 2023
> -3.70
> 3,0095
> 2.01
> -14.5890
> 0090
> 97.97930
> 970
> 1792
> OOOK
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> Margin
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
> 0.27
> 2.2296
> 0.09
> 1.4096
> 14.639
> 12.579600
> Pnl
> Investability Constrained Pnl
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;36
> PM
> 0.2624
> -0.0448
> IS Testing Status
> Period
> OS
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;37
> PM
> 0.8554
> -0.6340
> 5PASS


通过增加一个需要点塔的数据集字段，并稍加调节，便得到了一个 add(sharpe, fitness) > 4，Margin > 万20，returns 提高4倍，self_corr 上升2倍 的alpha，总体看来还是不错的，可以达到可提交的效果 .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 07/30/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> IS Summary
> Period
> IS
> 05
> rank
> star
> Val
> industry_rank
> anl39
> rOXLCXSpeq
> anl39_xlcxspemtp
> Power Pool Alpha
> Pyramid theme: EURIDIIMODEL X1.4
> Simulation Settings
> Pyramid theme: EURIDIIANALYST X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.45
> 7.5596
> 1.91
> 7.629
> 4.2396
> 20.189600
> Equity
> EUR
> T0P2500
> Fast Expression
> RAM
> On
> On
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.70
> 6.7096
> 1.04
> 46895
> 1.289
> 13.98900
> 778
> 1329
> Clone Alpha
> 2014
> 3.25
> 7.59%6
> 2.69
> 8.5495
> 1.149
> 22.5035o
> 1070
> 1525
> 2015
> 1.27
> 7.84%
> 0.72
> 2.0595
> 2.839
> 10.359500
> 1113
> 1611
> 2016
> 4,09
> 8.03%
> 2.34
> 12.0895
> .20%
> 35.07930
> 1025
> 695
> Chart
> Pnl
> 2017
> 2.61
> 7.3396
> 1.75
> 5.6295
> #1090
> 15.3390
> 1120
> 831
> 2018
> 3,05
> 7.7096
> 2.30
> 7.10%
> 2.0590
> 18.43900
> 1166
> 1750
> 2019
> 1.27
> 7.56%
> 62
> 3.0195
> 1.70%
> 7.95930
> 1183
> 1625
> 2020
> 2.34
> 8.01%
> 1.94
> 8.6095
> 1.72%
> 21.469530
> 1121
> 1621
> 5OOOK
> 2021
> 2.71
> 86%
> 2.35
> 9.4095
> 3.52%
> 27.40950
> 1122
> 1820
> 2022
> 2.45
> 7.81%6
> 2.27
> 10.75%
> 4.2390
> 27.51930
> 1163
> 1739
> 2,50OK
> 2023
> 3,80
> 7.5596
> 3.63
> 11.8095
> 0.489
> 31.269500
> 1093
> 1672
> Investability constrained
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
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> DrawgOwn
> Margin
> 1.88
> 3.599
> 1.30
> 5.9796
> 3.9796
> 33.269600
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> Last Run: Sat 09/13/2025,7.05
> PM
> 00
> IS Testing Status
> Period
> 05
> 0.5189
> -0.0937
> Power Pool Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> 8 PASS
> PM
> 0.5189
> -0.1529
> Sharpe of 2.45 is above CUtOff of 1.58.
> Fitness Of 1.91 is above cutoffof1.
> Turnover of 7.5596 is above CUtoff of
> Prod Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,7;05
> PM
> Turnover of 7.55% is below cutoff of 70%.
> Weight is well distributed over instruments。
> 0.8288
> -0.4965
> Sub-universe Sharpe of 1.27 is above cutoff of 1.27.
> IS Iadder Sharpe Of 2.49 is above cutoff of 2.02 for Iadderyear 2: 1/20/2023.1/21/2021


ii ）在相关性很高的的情况下，但是alpha表现还是比较行的那种，我们可以通过点塔的方式，同样使用 +、-、* 和 /，或者 ts_op 、group_op 都是可以的，目的是达到降低 alpha 的相关性并实现点塔的目的 .


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09/13/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> OS
> ts_target_
> tvr_decay (imbs_
> SCOre
> Iambda_min-o,
> Iambda
> maX=l, target
> tVr=0.1
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawcown
> Margin
> Simulation Settings
> 2.86
> 7.7796
> 1.98
> 5.979
> 2.319
> 15.379600
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 3.32
> 7.96%
> 2.54
> 7.3295
> 009
> 18.40950
> 1363
> 1355
> 2014
> 5.73
> 7.0796
> 5.12
> 9.999
> 0.739
> 28.259530
> 1569
> 1577
> 2015
> 4.83
> 7.5196
> 264
> 11.5495
> 1.289
> 30.7390
> 1645
> 653
> Clone Alpha 
> 2016
> 2.76
> 7.3796
> .82
> 5.42%
> .6890
> 14.71930
> 1574
> 593
> 2017
> 2.23
> 7.51%
> 3.00
> 5.2995
> 639
> 16.52930
> 1610
> 533
> Chart
> Pnl
> 2018
> 3.49
> 7.81%
> 2.54
> 6495
> .239
> 6.93930
> 1875
> 1871
> 2019
> 2.96
> 7.5596
> 2.04
> 5.9195
> 1.129
> 15.45930
> 645
> 1723
> 2020
> 8.30%6
> 22795
> 1.729
> 5.48930
> 1736
> 1813
> 2021
> .05
> 299
> 2.43%
> 2.31%
> 5.86930
> 2203
> 2291
> 40OOK
> 2022
> 7.97%6
> 0.22
> 1.5195
> .839
> 3.79950
> 2057
> 2121
> 2023
> 11.09%
> 5.57
> 8.2395
> 08%
> 14.85930
> 1783
> 1829
> ZOOOK
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025,
> 9;33
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
> PM
> 0.3352
> -0.0929
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> Du
> 0.5597
> -0.1764
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,9;33
> IS Testing Status
> Period
> 0S
> Du
> 0.9227
> -0.5410
> Year


比如：此 alpha 与大池子相关性0.92， 与小池子相关性0.56都较高，且Robust universe Sharpe 也没通过少得也不多不少，于是想着通过 点塔字段来小幅度扰动，同时实现点塔 和 降低pc，岂不是两全其美 .


> [!NOTE] [图片 OCR 识别内容]
> 说到这里,
> 我想说一下关于提交 alpha 关于 Prod Correlation ,
> Power Pool
> Correlation 和 Self Correlation,
> 也许在绿灯亮起提交 alpha 显示出的错误或许不
> 那么明确. (个人看法,如有问题还望大佬们不忘吝啬,
> 可评论区说明我好做出调
> 整)但大致是这样的 .
> 举个例子:有一个国王喜欢吃各种各样式的苹果
> 大家都会送苹果给国王
> 吃,
> 当然会获得相应的报酬,吃之前需要将苹果放进池子进行清洗,
> 有两个大小
> 的池子。如果你送来的苹果好,自然是放在大池子里。和大池子里的苹果比较 ,
> 如果大池子没有类似的苹果,
> 或者如果有类似的苹果,
> 但是你的苹果比这个类似
> 的苹果有更少的瑕疵,那你的苹果将会被收取从而获得报酬;  如果你的苹果不满^
> 足大池子,
> 那就继续按照以上这种方式放小池子,
> 当然这种小池子只是大家人手
> 一个,
> 大池子也是谁想用可以随时搬自己家测试,
> 小池子的作用是什么,如果大
> 池子的苹果被国王吃完了,那就会考虑小池子了,当然人家毕竟是国王,没有那
> 么容易吃完大池子的稀奇苹果.



> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 09/11/2025 EDT
> 顾问 ML47973 (Rank 100)
> udd Alphato a List
> Code
> IS Summary
> Period
> IS
> 05
> ts_target_
> tvr_decay (imbs_
> SCOre
> mCr63_membership,  Iambda
> min=0
> Iambda
> Iax=l
> targe
> Power Pool Alpha
> Pyramid theme: ASIIDIIIMBALANCE X1.1
> Simulation Settings
> Pyramid theme: ASIIDIIMACRO X1.5
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Ha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.84
> 7.739
> 1.19
> 5.249
> 5.899
> 13.56900
> Equity
> 4SI
> MINVOLIM
> Fast Expression
> 0.08
> Fast Factors
> 0n
> Off
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.03
> 8.02%
> 1.34
> 5.4795
> 2.0596
> 13.63330
> 1377
> 1351
> Clone Alpha 
> 2014
> 2.21
> 7.0596
> 407
> 11.659
> .76%
> 33.089500
> 1573
> 1573
> 2015
> 3.41
> 7.4796
> 293
> 9.20%
> 1.129
> 24.61930
> 670
> 628
> 2016
> +94
> 7.45%6
> 0.47
> 3.16%
> 5.8990
> 48930
> 590
> 1577
> Chart
> Pnl
> 2017
> 2.28
> 7.50%
> 2.8895
> 1.6596
> 12.84930
> 620
> 1623
> 2018
> 2.55
> 7.74%
> .84
> 5.5395
> 1.2996
> 16.879500
> 899
> 1827
> 2019
> .83
> 7.5496
> 1.14
> 4.8795
> .9890
> 12.91930
> 1705
> 653
> 2020
> 0.02
> 8.3296
> 0.00
> 0.059
> 2.259
> 0.1593o
> 800
> 1729
> 2021
> 8.18%6
> 1.21
> 5.159
> .6390
> 12.5893o
> 2305
> 2190
> 2022
> 7.82%
> 0.07
> 0.8795
> 2.5696
> 2.239500
> 2113
> 2055
> ZOOOK
> 2023
> 3.80
> 10.50%
> 3.02
> 7.9295
> 0.1996
> 15.08930
> 864
> 1757
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
> [
> Correlation
> Self Correlation
> Maximum
> Minimun
> LastRun: Sat, 09/13/2025
> 9;43
> PM
> 0.3474
> -0.0437
> Power Pool Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.3645
> -0.0892
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimun
> Last Run: Sat  09/13/2025,
> 9;43
> Du
> 0.6217
> -0.4420
> PASS
> Vear


事实证明，使用 macro 数据集的 mcr63_membership 字段，能够使得pc 降低三分之一降至 0.62，，ppc 降低接近二分之一降至 0.36，从而实现点塔 .

[图片 (图片已丢失)]

3. 好而优的 alpha

何为好而优的 alpha？我理解有两点来说明，一点是 好 ，二点是 优 .

一点：好，我理解在:

1) sharpe ≥ 1.2  相同利益下承担的风险越小越好，降低个人的抗压；

2) fitness ≥ 1  全方面稳定还是非常不错；

3) turnover ≥ 2% & turnover ≤ 30% 既为对冲换手率不能低，换手率高了手续费遭不住；

4) returns ≥ 10%  收益还是要好点能赚钱吧；

5) drawdown 回撤越小越好吧，大了心理抗压不行；

6) margin ≥ 15% 单位收益要高点吧，赚钱了谁都开心；

7) 十年数据中做多做空不能太少吧，权重太高危险危险！

8) 十年数据做多做空少两年数据的扔了吧，还要每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15% .

满足这八条，第8) 条数据有些苛刻，想要 alpha 质量过得去，要求每(除最后)一年的returns ≥ 10% 同时 margin ≥ 15%，这个第8) 条我是从 游戏王 那里学到的 . 下面展示了一个还过得去得 alpha .


> [!NOTE] [图片 OCR 识别内容]
> CT
> Created 09/08/2025 EDT
> anonymoUs
> udd Nphato a List
> Code
> 1
> OS Summary
> Period
> I5
> 05
> peVerse(r
> ib5
> SCOre
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: EURIDOIIMBALANCE
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> Simulation Settings
> 0172112023 CT
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Hand
> Equity
> EUR
> T0P2500
> Fast Expression
> 0.08
> Subindustry
> On
> Off
> Sharpe 60
> Sharpe 125
> Sharpe 250
> Sharpe 500
> OSIIS Ratio
> Close
> Close Ratio
> Self-Correlation
> Vear
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Clone Alpha
> 2013
> 3.9
> 23.8899
> 4.13
> 26.189
> 2.5995
> 21.929600
> 986
> 405
> 2014
> 3.52
> 22.6895
> 3.36
> 20.65%
> 2.9096
> 18.22930
> 1070
> 431
> 2015
> 3.32
> 22.8295
> 3.46
> 24.43%
> 3.03%
> 21.41950
> 1130
> 459
> Chart
> Pnl
> 2016
> 2.53
> 21.1195
> 2.65
> 21.4796
> 3.4796
> 20.349530
> 1138
> 455
> 2017
> 2.77
> 20.7795
> 2.47
> 16.5496
> 3.40%
> 15.92930
> 1125
> 470
> 2018
> 1.88
> 19.5696
> 1.67
> 15.3796
> 7.27%6
> 15.71930
> 1010
> 418
> 2019
> 2.77
> 19.1395
> 3.03
> 22.829
> 3.18%
> 23.8890
> 998
> 423
> 1ON
> 2020
> 0.71
> 19.4395
> 0.39
> 5.9596
> 5.659
> 2930
> 908
> 392
> 2021
> 1.73
> 19.20%
> 10.789
> 5.089
> 11.22930
> 972
> 416
> 5OOOK
> 2022
> 18.4390
> 1.42
> 14.789
> 4.5795
> 16.0493o
> 050
> 439
> 2023
> 10.22
> 31.6599
> -14.39
> 62.7790
> 3.5796
> 39.67930
> 945
> 393
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
> Pre
> Sharpe
> Pre


二点：优，我理解在:

1) 看起来直观的，比如： 使用 - x 而不用 reverse(x)；

2) 能加注释的加注释，最好是英文注释，有经济学意义就填上；

3) 有时比如写个“alpha = *&%； alpha”，其实没必要这么写， 写“alpha = *&%；” 就好了；

使用


> [!NOTE] [图片 OCR 识别内容]
> 1
> 1.
> 事件距离基础信号:  距离越大。事件影响越小
> eVent
> signal
> VeC
> SUI
> nWs7g_event_detection_distance_358-
> 1
> 距离平方增骚:  放大极端距离信号的非线性影响
> brk
> VeC
> sum(brkl_start_stock_price);
> distance_squared
> event_signal
> 2;
> alpha
> ts covariance(
> brk,
> 股票起始价格汇总
> 1
> 词频倒数因子:  词数越少。信息浓度越高(1/词数)
> brk,
> 11  同一序列的自相关计算
> Word
> density
> 二 1
> VeC
> SUII
> nWS7g_word_count_391 )
> 24
> 24周期(约1个月)滚动窗口
> 10
> 1
> 复合事件驱动因子:  距离信号
> 非线性增骚
> 信息浓度
> 11
> alpha
> (event_signal
> distance_squared
> Word_density)



> [!NOTE] [图片 OCR 识别内容]
> 11 Core Logic:
> Reverse standardized composite factor
> reverse
> operation when large trader behavior diverges
> 1
> Synthetic
> Base
> Factor: Market
> pattern
> trader Value differential
> base factor
> mdl175 OGam
> power(Vec
> sum(pvz7_value_diff_large_trader), 2);
> /12. standardization: Convert to
> Z-score to eliminate scale effects
> Zscore_factor
> Zscore(base_factor) =
> 1
> Signal Reversal: Negative sign indicates
> Contrarian
> selection, seeking
> undervalued
> opportunities
> alpha
> ZSCOre
> factor;
> large



> [!NOTE] [图片 OCR 识别内容]
> Description
> 507
> 100 character minimum
> Power Pool Alpha
> Use the template
> In orderto submit this alpha, you have to add an alpha description following the given template_
> Idea: Identify the time index ofthe maximum imbalance score over a 2O-day Window, then invert the result:
> Rationale for data used: The imbalance score (imb5_score) likely measures order flow or liquidity asymmetry; its maximum pinpoints the
> most extreme positive imbalance event。
> Rationale for operators Used: The 20-dayarg max (ts_arg_max)returns the lookback period (0-19) where the series peaked_and the


不建议使用


> [!NOTE] [图片 OCR 识别内容]
> 1 |
> ts_covariance(vec
> SUm(brkl_start_stock_price) ,
> VeC
> sum(brkI_start_stock_price), 24)



> [!NOTE] [图片 OCR 识别内容]
> brk
> VeC
> sum(brkl_start_stock_price)
> alpha
> ts covariance
> brk,
> 股票起始价格汇总
> bk,
> 11同一序列的自相关计算
> 24
> 1124周期(约1个月)滚动窗口
> );
> alpha


[图片 (图片已丢失)]

**三、alpha模板 ！**

看到这里，你还在想向我找寻alpha模板吗？其实我没有模板 ... 时间多的话可以再瞧一瞧上面的内容，看看能不能给到你一点点启发呢 .


> [!NOTE] [图片 OCR 识别内容]
> N-1
> Ha
> 1,3N,8.七
> lim
> fa()-Cfa(a)
> 二
> Iim
> fa(a)
> n-〉+O
> n〉+O
> 2二1
> 2二1
> C=N
> 10-P


换个思路，我们做的是alpha， 是有经济学意义的的alpha，使用通过alpha模板去套字段，得到 alpha 数学模型. || 现在你不妨大胆一些，WoridQuantBrain 上现在不是有非常多的字段吗，不妨设想一下，你现在就是在 WQ 上创造数据字段的Consultant ！

field 本身算是一个字段，那 1 / field 也算一个字段，现在字段就已经实现翻倍了，abs(field)、log(field)、power(field, 2) 和 power(field, 3) 也可以算字段， 相反数会去匹配 sharpe .

其实一个字段就会有复杂度O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))，相对而言虽然 truncation 和 nan handling 对大多数字段影响没有那么大，但有时对于个别的字段影响比较大的，这两个在复杂度上倒是可以不用那么关心 .


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 3,000
> 2,000
> UUJ
> OIlU
> 〈ee
> 3" A0。
> 02
> Displayed Period
> 02/14/2025
> 09/12/2025
> 149346
>  Mar
>  Mar
> Mar
> Mar
> Mar
> 30。
> 31。
> 24。


从2月14日正式注册来，4月成为有条件顾问，一直到7月14日刚好5个月从有条件顾到正式顾问，到今天刚好7个月整. 我的总回测量跟前几天Bug时期大佬两天跑的回测量差不多. 其实有空跑一跑，摸一两个 alpha模板出来，O(Σ(region, universe, neutralization, delay, delay, truncation，maxtrade, nan handling))复杂度那么高，无论是为了点塔凑Operators used还是交alpha数量，alpha (至少ppa) 是会有的 .

[图片 (图片已丢失)]

使用操作符 ts_op(f, days) ，这是一个字段，继续套， 1 /  ts_op(f, days) 、power(ts_op(f, days), 2) 和 power(3, ts_op(f, days)) ，甚至如果你想要使用exp{x}、sinx、arctan(x)等等数学函数，但 worlduqant 没有对应的操作符，怎么办，可以自己造 .

造不出alpha，可以先‘少’管经济学意义，可以翻阅下自己的《数学分析》，或者说《高等数学》更好，你应该会有所收获.  同时结合自己的思考可以继续深入想象一下 . 充分发挥想象，那将是你的创造字段的无穷源泉 .

[图片 (图片已丢失)]

下节预告:  [Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析]([L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md)

2025年9月14日

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，通过add点塔这个小技巧倒是真的学到了

不过发现自己两个per的数据都是大佬的一倍，作为gold感觉冲expert是有点艰难了

===================================================================================


---

### 技术对话片段 146 (原帖: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN]([L2] 【插件】Genius Rank分析代码优化_29496672188951.md) 
             Github插件地址： [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 安装插件
> .访问插件 GitHub 地址: https
> //github. com /zhangkaihua88 / WebDataScope
> 能访问Gitlub的请跳过这红色部分
> 0)如果访问不了 github.
> COm
> 换一个浏览器试试,
> 有几率解决 ,
> 如果不行 ,
> 请按照以下步骤操作。
> 〈 〉 C 命 ^ 众
> 0
> [链接已屏蔽] MebDataScope
> 器
> 无法访问此网站
> 连接已重置。
> 请试试以下办法:
> 检查网络连接
> 检查代理服务器和防火墙
> 运行 Windows 网络诊断
> ERR_CONNECTION_RESET
> 重新加载
> 详情
> 1)同时按住 [Window
> Or
> Start ]
> + R, 输入 cmd 打开命令提示符,
> 然后输入 pin
> 吕
> github.com
> 如果 ping 不通,表现为
> ping
> 不是内部或外部命令,
> 也不是可运行的程序
  
> [!NOTE] [图片 OCR 识别内容]
> 或批处理文件=
> 建议将此错误扔给
> AI
> 解决,多半是环境娈量 问题)
> 得到并复制 gith
> ub 的 ip 地址.
> C:IWINDOWSIsystem3zlcmd.
> X
> Microsoft Windows
> [版本
> 10.0.26100.6584]
> Cc)
> Microsoft
> Corporation。
> 保留所有权利
> 0
> C: |Users
> Dping github
> C0I
> 正在
> Pinq
> qithub
> C0I
> 23
> 205.243.166]  具有
> 32  字节的数据:
> 20.205
> 243.166
> 复:  字节=32
> 时间=75ms
> TTL=I03
> 20.205
> 243
> 166
> 的
> 复:  字节=32  时间=75ms
> TTL=I03
> 黧
> 20.205.243.166  的
> 复:  字节=32  时间 =75ms
> TTL=I03
> 20.205.243.166  的
> 复:  字节=32  时间=75ms
> TTL=I03
> 20.205.243.166  的 Ping 统计信息 :
> 数据包:  已发送
> 二  4,
> 已接收 =4,
> 丢失
> 二
> 0
> (0%  丢失 ),
> 往返行程的估计时间 (以毫秒为单位 ):
> 最短
> 二
> T5mS,
> 最长
> 二
> T5mS,
> 平均
> 二
> T5ms
> 2)  复制 ip 地址。在服务器  搜索栏  输入 C: WWindows |System3z Idrivers letc Ihost
> 5 ,
> 打开方式选择  记事本 ,然后马上关闭记事本。接着在  搜索栏  搜索  记事本 并 右击
> 选择以管理员身份运行 ,随即将 github.com 的 ip 地址粘贴在最后.
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1 `
> :三 `
> 8 工 O  a
> # Copyright (c) 1993-2009 Microsoft
> #
> # This is asample HOSTS file used by Microsoft TCPIIP for Windows。
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept onan individual line. The IP address should
> # be placed in the first column followed by the corresponding host name:
> # The IP address and the host name should be separated by at least one
> # space。
> #
> # Additionally, comments (such as these) may be inserted on individual
> # lines O[
> following the machine name denoted by a '#' symbol。
> #
> # Forexample:
> #
> 102.54.94.97
> rhino.acme.com
> # SOUrCe Serer
> 38.25.63.10
> Xacme.com
> # X client host
> # localhost name resolution is handled within DNS itself
> #
> 127.0.0.1
> localhost
> #
> 门
> localhost
> 20.205.243.166
> 行10,列2
> 818个亨符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-8
> 3)
> 点击记事本左上角的 文件 然后选择  保存  即可。切记记得看记事本上面是
> 而不是 O 才算保存成功。
> Corp:
  
> [!NOTE] [图片 OCR 识别内容]
> hosts
> 文件
> 编辑
> 查看
> H1
> :三 `
> 8 工 O g
> # Copyright (c) 1993-2009 Microsoft Corp.
> #
> # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
> #
> # This file contains the mappings of IP addresses to host names. Each
> # entry should be kept on an individual line. The IP address should
> # be placed in the first column followed by the corresponding host name。
> # The IP address and the host name should be separated by at least one
> # space:
> #
> # Additionally comments (such as these) may be inserted on individual
> # lines Or following the machine name denoted by a '#' symbol。
> #
> # For example:
> #
> 102.54.94.97
> rhino.acme.com
> SOUrCe Serer
> 38.25.63.10
> X.acme.com
> client host
> # localhost name resolution is handled within DNS itself。
> #
> 127.0.0.1
> localhost
> Iocalhost
> 20.205.243.166
> 行22,列15
> 818个字符
> 纯文本
> 1009
> Windows (CRLF)
> UTF-S
> 4)  在 搜索栏  搜索
> cmd 并 右击选择以管理员身份运行 ,在  命令提示符  面板上键入 ip
> config/flushdns
> 返回
> 己成功刷新DN5解析缓存  便表示成功了.
> C
> 管理员: 命令提示符
> 义
> Uicrosoft Nindows [版不 10.0.26100.6584]
> (C)
> Iicrosoft Corporation。 保留所有权利。
> C: |Iindows |System32>ipconfig / flushdns
> Iindows
> IP 配置
> 己成功刷新 DVS 解析缓存。
> C: {Tindows |System32>
> # X
  
> [!NOTE] [图片 OCR 识别内容]
> 5)
> 访问华子哥的 Bithub 地址 https: //github_
> COm
> zhangkaihua88 /WebDatascope
> 成功.
> 囟 M。『图』 &
> WorldQuant BRAIN
> GitHub
> ZhangkalhuaBBNe
> C
> https /Igithubcom/zhangkaihuagg NebDatascope
> C 囤  &
> 8 &
> 器 ^4  泊
> 器
> Platform
> Solutions
> Resources
> Open Source
> Enterprise
> Search Orjump to.。
> Signin
> Sign up
> Zhangkaihua88 / WebDataScope
> Public
> Notifications
> Fork
> Stal
> Code
> SSUeS
> Pullrequests
> Actions
> Projects
> Security
> Insights
> main
> Branches
> GOto fle
> Code
> About
> No description website
> Ortopics provided。
> Zhangkaihuagg fix
> 0183285
> 2Weeks a90
> 118 Commits
> Readme
> Delete img/screenshotpng
> last year
> Apache 2.0license
> Activity
> SIC
> Weeks ago
> 69 stars
>  gitignore
> V0.4.3
> last year
> watching
> LICENSE
> VO.1.0
> last year
> 14 forks
> Report repository
> READMEmd
> 2 months ago
> manifestjson
> Weeks ago
> Releases
> responsejson
> Weeks ago
> WebDataScope 0.9.3 Release
> Lalest
> onIunT4
> 16 releases
> README
> Apache- 2 0 license
> Packages
> 以上为不能访问Gitlub解决方法
> 2
> 点击绿色
> Code 弹出
> Download
> ZIP
> 下载插件压缩包. Zip文件,
> 或者使用 &
> i
> 克隆 git
> clone https: //github.com/zhangkaihua88 / WebDataScope . git
> 将压缩包保
> 存在某目录下,比如我保存在
> 0:
> worldquant_plugin 目录下
> 确认下载
> About
> 链接:
> hub.comlzhangkaihuaggMebDataScopelziplrefs/heads/main
> No description, website; or topics provided。
> 文件名:
> WebDatascope-mainzip
> 394KB
> 0
> Readme
> 保存到:
> 0: {worldquant_plugin
> Apache- 2.0 license
> A
> Activity
> 打开
> 保存
> 取消
> 69 stars
> watching
> V0.1.0
> Open with GitHub Desktop
> 9
> 14 forks
> Download ZIP
> Report repository
> UP
> 3
> 使用解压软件将压缩包解压到(默认)当前目录下.
> Pricing
> Tags
> img
  
> [!NOTE] [图片 OCR 识别内容]
> Worldquant_plugin
> 此电脑
> 新加眷 (D:)
> worldquant_plugin
> 在 worldquant_plugin 中搜索
> 新逮
> 排序
> 三  苎看
> 全部解压宿
> 详洇信息
> 名祢
> 修改曰期
> 大小
> 主文仵夹
> WebDataScope-main
> 2025/9/1218:13
> 压宿(pped)文件。
> 394 KB
> 图库
> 捉敢压缩(Zipped]文件夹
> 选择
> 个目标并提取文件
> 文裆
> 文件将被捉致到这个文件夹(F:
> 囱片
> Dilworldquant_plugin WebDataScope main
> 浏览(R)
> 音乐
> 完戎时显示捉敢的文件(H)
> 视频
> 此电脑
> 本地硭岛 (C:)
> 新加卷(0:)
> 捉取(
> 职消
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 个项目
> 逆中
> 个目
> 393 KB
> 在浏览器中打开扩展管理页面,
> 网页键入 chrome:
> /extensions
> (如
> chrome: //extensions
> 八.
> WorldQuant BRAIN
> 扩展程序
> Cent BroWseT
> chrome /extensions
> 器 |#
> 省
> 器
> quant
> 节点
> MP3袼式
> 显化群每曰总若
> 常用网
> 扩展程序
> 搜索扩展程序
> 开发者摸式
> 我。}展穆序
> 键盘快捷键
> 在 CentBrowser 应田酋店中查找扩展程序和主题背景
> 在 Cent Browser 应jd店中
> 发现更多扩展程序和主题
> 5
> 开启
> 开发者模式》
> 点击 <加载己解压的扩展程序》
> 选择插件文件
> 夹。成功会显示  扩展加载完毕
> edge:
  
> [!NOTE] [图片 OCR 识别内容]
> 选择扩展程序目录
> worldquant_Pl
> WebDatascope main
> WebDatascope-main
> 器
> #
> 阎
> c识
> 新逮文件夹
> 名称
> 佟改曰期
> 开发者摸式
> 此电脑
> WebDataScope-main
> 2025/9/1218.27
> 文件夹
> 本地磁盘 (C:)
> 新加巷 (0;)
> 新加卷 (E:)
> 新加卷 (F:)
> 网咨
> 围l店中查找扩展程序和主题背景
> 文件夹:
> WebDatascope-main
> 迸文4夫
> 驭消
> 2
> 使用插件功能
> 打开 Genius 页面
> 安装完成后 ,打开 WorldQuantBrain 网页 Genius 页面 https : /Iplatform.worl
> dquantbrain.com/genius /
> (安装完成后第一次打开需要刷新页面等待若干(少许)时
> 间才能加载出插件)
> @
> 匕
> https:/Iplatform worldquantbrain com/genius/
> C 囤  众
> 8Q
> 器 ^4  省
> 器 ^8 quant
> U  节点
> MP3袼式
> 昱化群l日总结
> 常用网址
> WORLDOUANT
> BRANI
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> 恩 Competitions (5)
> Community
> Status
> Leaderboard
> FAQ
> Gsnlus
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析 
> 显示排名列表
> Genius level: Gold
> Best level: Gold
> Current quarter end: September 3oth; 2025
> SOLD
> 页面加载后,你会看到  配置插件
> 运算符分析
> 显示运算符分析  和「排名分析」
> 和「显示排名分析」以及「显示排名列表」六个按钮
> 依次点击  配置插件
> 运算符分析
> 显示运算符分析
> 配置插件  点击的作用是啥我不是很清楚,
> 这个得问华子哥才知道。点击  运算符
> 分析  按钮后插件会开始抓取你本季度交付的 alpha 全部操作符数量和使用数据 (按
> 钮上会显示抓取进度) ,抓取完成后,
> 点击显示运算符分析 ,会在页面最下方会生
> 成关于操作符的分析表格。右上角显示过去和美区分析 (何时分析)时间.会展示你
  
> [!NOTE] [图片 OCR 识别内容]
> 本赛季所有的操作符和数量以及使用情况.
> 命
> https: / /platform worldquantbrain comlgenius/
> C 困 &
> 8 ^Q  器 ^4
> 器 ^8 quant
> U  节 
> MP3格式
> 量化群每曰总结
> `用网址
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符未被使用。
> '有两种含义分别是substract和revers, 此处统
> 为substrac
> Operator Analysis
> 美东时间: 2025/9/1207:15:17北京时间:2025/9/1219:15:17
> 在你可用的运算符中。共有68种运算符被使用。11种运算符末被使用。
> '有两种含义分别是substract和revers, 此处统一
> 为substrac
> Category
> Definition
> Count
> Scope
> Level
> Arithmetic
> add(x; Y, filter
> false), X -y
> 52
> COMBOREGULARSELECTION
> base
> Arithmetic
> multiply(xyy
> filter-false); *
> 76
> COMBO,REGULAR SELECTION
> base
> 依次点击「排名分析」和「显示排名分析」以及「显示排名列表」
> 点击「排名分析」需要等待0.5 ~ 1min 左右 ,
> 需要计算排名情况, 计算完成
> 后点击「显示排名分析」 ,就可以看见比较多的信息,
> 包括但不限于顾问的总人
> 数,以及目前 genius 不同级别达标分别有多少人和自己目前的等级 ,
> 以及自己的
> 最终定级大概会在什么等级 ,
> 以及自己的六维数据。
> q
> 匕
> https:/Iplatform worldquantbraincom /genius/
> C 囤 。 令
> 凸 /Q 器 』4  省 :
> 器 ^8 quant
> 节忘
> MP3袼式
> 导化拜#曰总结
> 常用网址
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207:22:18北京时间: 2025/9/1219:22;18
> 我的排名信息
> 美东时间:2025/9/1207:22:18 北京时间:2025/9/1219:22.18
> 总人敛{9104
> 可能的基璀人数:2926 人
> (交够40个)
> 各个Level 满足的人数 /最终的人:
> For Expert;(512/ 585
> For Master: 4131234
> ForGranamaster
> 该用户目前满足的级别
> grandmaster
> 绢辑六维指标
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:87
> 585
> 总排名:91
> 234
> 总排名:34
> Operator Count: 307 名
> Operator Count: 200 名
> Operator Count: 39 名
> Operator
> 141名
> Operator
> 44名
> Operator AVg: 7名
> Field Count; 263 名
> Field Count; 152 名
> Field Count; 36 名
> Field
> 112名
> Field
> 30名
> Field
> 7名
> Community Activity: 252名
> Community Actiity: 142 名
> Community Activity: 27 名
> Completed Referrals: 1 名
> Completed Referrals:
> Completed Referrals: 1 名
> Max Simulation Streak: 903 名
> Max Simulation Streak: 338名
> Max Simulation Streak: 45 名
> Total Rank: 1979名
> Total Rank: 907 名
> TotalRank: 162 名
> 同时还有贴心的可以 编辑六维数据  按钮,这个功能非常还好,
> 可以让你知道自
> 己目前所处的级别到达是差在哪里,怎么去弥补自己的差分点.非常 nice!
> 点击「显示排名列表」可以多维度查看和分析所有顾问的某些数据,
> 想比对
> 想查看哪位大佬的数据都可以查看,同时支持多维度过滤筛选.
> AVB;
> AVg:
> Avg:
> Ave:
> Avg:
  
> [!NOTE] [图片 OCR 识别内容]
> https:/ /platform worldquantbrain com/genius /leaderboard
> C 囤
> 8Q
> 器 ^^4
> ^
> 器 ^9 quant
> 节点
> 1P3恪式
> 呈化群每曰总结
> 穷用网址
> Genius Rank List
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> 排名信息
> 美东时间:2025/9/1207:22:18北京时间:2025/9/1219:22:18
> Minimum 排名:
> Maximum 排名
> entries per page
> Search:
> 下荭原始J5JN
> 显示隐蒉列
> 排名
> 用FID
> 达成等级
> 最终等级
> 国家1区
> K279256
> grandmaster
> grandmaster
> CN
> J71699
> grandmaster
> grandmaster
> FL39657
> grandmaster
> grandmaster
> CN
> 064461
> grandmaster
> grandmaster
> VN
> YN82626
> grandmaster
> grandmaster
> TW
> PP87148
> grandmaster
> grandmaster
> IN
> AT56452
> grandmaster
> grandmaster
> RP76828
> grandmaster
> grandmaster
> CN
> F069320
> grandmaster
> grandmaster
> CN
> 2H78994
> grandmaster
> grandmaster
> T
> Showing
> TO 10of 5,116 entries
> 512
> 查看他人排名数据
> 华子哥的插件还有非常贴心的功能,就是可以查看别人的排名,
> 比如:  华子
> 哥
> K279256
> 课代表 XX
> 游戏王
> ZS(CL ) [ZSC]59763  和常州MG
> 顾问 MG88592 (Rank 38)
> 大佬等等.
> WORLDOUANT
> B人I
> Simulate
> 6Alphas
> Learn
> Data
> Labs
> Genius
> @ Competitions (5)
> Community
> 号
> Refer
> friend
> StatUs
> Leaderboard
> FAQ
> Genius
> Displaying quarter:
> 2025-03 (Current)
> 配置插件
> 运箅符分析完成267
> 显示运箅符分析
> 排名分析完成
> 显示排名分析
> 显示排名列表
> Genius Rank Analysis
> 美东时间:2025/9/1207;22:18 北京时间:2025/9/1219:22:18
> 我的排名信息
> 美东时问:  2025/9/1207.22:18北京时问:2025/9/1219:22:18
> 总人数:9104人
> 可能的基准人数:2926  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 1512
> 585
> FOr Master: 413
> 234
> For Grandmaster: 47/59
> 点击
> Leaderboard
> 将鼠标放置在某大佬的 ID 上,
> 便可查看六维排名和
> Geniu
> s等级。
  
> [!NOTE] [图片 OCR 识别内容]
> https:/platform worldquantbrain com /genius/leaderboard
> 出  ^
> {|仑
> JIIVIIOIIOC
> IIUIIOICC
> 386
> 顾问 ML47973 (Rank 100) (Mej
> Gold
> Gold
> 266
> 2.39
> 1.79
> 0.00
> 3.41
> [792
> 167
> 2.70
> RP76828 排名信息
> AK40g
> 总人数:9067人
> 6.17
> 可能的基准人数:2921人 (交够40个)
> HI3900
> 5,38
> 各个Level 满足的人数
> 最终的人数:
> RP768;
> 2.81
> For Expert: 1508
> 584
> YH250;
> For Master: 410
> 234
> 105
> 5.83
> ForGrandmaster: 45
> 58
> P11976
> 5,82
> 该用户目前满足的级别: Srandmaster
> LV571
> 编辑六维指标
> CM456
> 6.91
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> TV5921
> 8.26
> 总排名:4
> 584
> 总排名:4/234
> 总排名:7/58
> LV598
> 4.70
> Operator Count: 35 名
> Operator Count: 34 名
> Operator Count: 15 名
> DVGAAI
> Operator AVg: 64名
> Operator AVg: 17名
> Operator AVg: 4 名
> 3,73
> Field Count: 283名
> Field Count: 160 名
> Field Count: 35 名
> 儿7169
> Field AVg: 33名
> Field AVg: 7 名
> Field
> 名
> 100
> 3.58
> Community Activity: 96 名
> Community Activity: 71 名
> Community Activity: 20名
> EYg42
> Completed Referrals:
> Completed Referrals:
> 名
> Completed Referrals:
> 名
> 6.15
> Max Simulation Streak:
> Max Simulation Streak:
> Max Simulation Streak: 33
> 501 名
> 222名
> ID51
> 5,91
> Total Rank; 1013 名
> Total Rank: 512名
> Total Rank; 109 名
> 56764
> 116
> 7.35
> AN154671
> Expert
> Expert
> 366
> 0.48
> 0.12
> 0.21
> 6.47
> https;lIplatform worldquantbrain comprofle/public/RP76823
> Master
> Master
> 365
> 0,79
> 0.89
> 0,91
> 8,61
> 致谢
> 再次感谢华子哥和贡献者们的无私分享 !这个工具极大方便了排名分析,同
> 时在前端的颜色。样式和大小展示方面也贴合美观设,
> 无论是自我提升还是学习
> 他人策略都非常有用。建议大家试用并反馈 ,
> 共同完善插件 !
> AVE:


**顾问 RM49262 (Rank 30) 的解答与建议**:
想请问一下，插件中以Expert/Master/Grandmaster为universe的最下面那个total rank是什么意思呢？是指1.signal 2.pyramid 3.performance三选一  这三个条件均满足某个universe标准的人中我六维的综合排名吗？还是其他什么意思呢。谢谢！
-----------------------------------------------------------------------------------------------


---

### 技术对话片段 147 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【经验分享】涅槃重生vf从018到097combine从-125到202经验分享.md
- **时间**: 24天前

**提问/主帖背景 (WZ47295)**:
大家好，我是WZ47295，正修读集成电路专业，第一次接触到worldquant brain是25年的7月，申请顾问的过程坎坷，自己也三心二意，在25年12月成为有条件顾问开始提交alpha，第一次更新combine和vf就给我来了一个晴天霹雳，vf只有0.18，combine是-1.25.

当时都想放弃wqb了，每天只有1刀，expert也遥遥无望，但是在阅读了论坛众多大佬是如何力挽狂澜，gold直升grandmaster以及各种经验帖之后茅塞顿开，并且之前交的alpha数量并不多，想着再坚持一下，改进自己的工作流、深入了解因子构造、提高提交条件，最终在最近一次更新得到了重生！vf从0.18涨到了0.97，combine涨到了2.02，


> [!NOTE] [图片 OCR 识别内容]
> Value Factor
> 1.06
> 1.00
> 0.80
> 区间:202601.
> 202602
> 202603
> 0.60
> 更新时间:2026-05-09
> Value Factor: 0.97
> 0.40
> 0.20
> 09
> 202509
> 202510
> 202511
> 202512
> 202601
> 202510
> 202511
> 202512
> 202601
> 202602
> 202511
> 202512
> 202601
> 202602
> 202603



> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化趋势
> Combined Alpha
> Power Pool
> ()
> Selected Alpha
> 30
> Combined Osmosis
> Combined
> 2.68
> 2.00
> 1.00
> 0.00
> -1.00
> -2.00
> -2.36
> 202511
> 202512
> 202601
> 202602
> 202603


并且收入大大改善：


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 05/11/2026
> Super:
> 55.24
> Regular: 43.92
> Total:
> 99.16
> 50
> 25
> n
> S
> <9
> <@ <@
> N pO pO' pS' p
>  ?
> 8
> NO"
> 3'
> ^O" 2'
> 9
> ~3"
> '2
> Dec
> Dec
> 19.Jan
> 26.Jan
> Feb
>  Mar
> Mar
>  Mar
> Mar
> May
>  May
> 12.Jan


从以前的1.5刀到现在差点突破100刀，实现了小康生活，现在我将把我的心得体会分享给大家：

25.12月和26.01月：这两个月我还是用的传统一二三阶代码未做改动，无脑跑一二阶，不注重prod_corr和margin，属于是绿了就交的地步

26.02和03月：这两个月逐渐醒悟，第一步就是对一二三阶代码进行自己的改进，首先我把所有的字段爬下来，根据描述做聚类分析，把描述相近的字段分成一个组，在进行一阶回测的时候把同组内coverage最高的拿来回测，并且一阶回测我利用论坛里面的模板和AI的提示重新构造了一下，覆盖长期、短期、波动、趋势、等等不同风格的策略来捕捉不同的信号，二阶回测我将group修改为了不计入fields的常见group，如market、subindustry等等，三阶暂时放弃了；在抓取回测结果时，如果找到一个信号，就将这个信号所属的分组内所有的字段进行替换并回测，再利用最大团算法进行分团，提交每个团内表现最优的alpha。

关于描述的聚类，weijie老师之前针对这个写了很多篇帖子了，大多数时候同一个聚类里面回测的信号是差不多的，但是有时候会有奇迹，这样是一个很好的节约回测次数的操作。

至于何为表现好的alpha，论坛里面有很多大佬已经写了很多相关帖子了，这里简述一下我的提交准则：

sharpe最低不能小于1.3,fitness最低不能小于0.9，margin不能低于每个地区的提交阈值，turnover控制在20以内，two_year_sharpe不能低于1.4；

平均sharpe大于1.58，平均fitness大于1.2，平均margin大于20bps,平均prood_corr小于0.7.

在这后面我一直遵循这样的提交习惯进行提交，vf和combine的上升也证明了这样的习惯是可行的

最后感谢国区的老师们和论坛、社区的各位大佬！感谢大家的无私奉献！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享，经验里干货满满，不懈的坚持终于换来了combine的提升

也祝我自己的combine能越来越高哈哈

=============================================================================


---

### 技术对话片段 148 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】涅槃重生vf从018到097combine从-125到202经验分享_40433337996183.md
- **时间**: 25天前

**提问/主帖背景 (WZ47295)**:
大家好，我是WZ47295，正修读集成电路专业，第一次接触到worldquant brain是25年的7月，申请顾问的过程坎坷，自己也三心二意，在25年12月成为有条件顾问开始提交alpha，第一次更新combine和vf就给我来了一个晴天霹雳，vf只有0.18，combine是-1.25.

当时都想放弃wqb了，每天只有1刀，expert也遥遥无望，但是在阅读了论坛众多大佬是如何力挽狂澜，gold直升grandmaster以及各种经验帖之后茅塞顿开，并且之前交的alpha数量并不多，想着再坚持一下，改进自己的工作流、深入了解因子构造、提高提交条件，最终在最近一次更新得到了重生！vf从0.18涨到了0.97，combine涨到了2.02，


> [!NOTE] [图片 OCR 识别内容]
> Value Factor
> 1.06
> 1.00
> 0.80
> 区间:202601.
> 202602
> 202603
> 0.60
> 更新时间:2026-05-09
> Value Factor: 0.97
> 0.40
> 0.20
> 09
> 202509
> 202510
> 202511
> 202512
> 202601
> 202510
> 202511
> 202512
> 202601
> 202602
> 202511
> 202512
> 202601
> 202602
> 202603



> [!NOTE] [图片 OCR 识别内容]
> Combined 娈化趋势
> Combined Alpha
> Power Pool
> ()
> Selected Alpha
> 30
> Combined Osmosis
> Combined
> 2.68
> 2.00
> 1.00
> 0.00
> -1.00
> -2.00
> -2.36
> 202511
> 202512
> 202601
> 202602
> 202603


并且收入大大改善：


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 05/11/2026
> Super:
> 55.24
> Regular: 43.92
> Total:
> 99.16
> 50
> 25
> n
> S
> <9
> <@ <@
> N pO pO' pS' p
>  ?
> 8
> NO"
> 3'
> ^O" 2'
> 9
> ~3"
> '2
> Dec
> Dec
> 19.Jan
> 26.Jan
> Feb
>  Mar
> Mar
>  Mar
> Mar
> May
>  May
> 12.Jan


从以前的1.5刀到现在差点突破100刀，实现了小康生活，现在我将把我的心得体会分享给大家：

25.12月和26.01月：这两个月我还是用的传统一二三阶代码未做改动，无脑跑一二阶，不注重prod_corr和margin，属于是绿了就交的地步

26.02和03月：这两个月逐渐醒悟，第一步就是对一二三阶代码进行自己的改进，首先我把所有的字段爬下来，根据描述做聚类分析，把描述相近的字段分成一个组，在进行一阶回测的时候把同组内coverage最高的拿来回测，并且一阶回测我利用论坛里面的模板和AI的提示重新构造了一下，覆盖长期、短期、波动、趋势、等等不同风格的策略来捕捉不同的信号，二阶回测我将group修改为了不计入fields的常见group，如market、subindustry等等，三阶暂时放弃了；在抓取回测结果时，如果找到一个信号，就将这个信号所属的分组内所有的字段进行替换并回测，再利用最大团算法进行分团，提交每个团内表现最优的alpha。

关于描述的聚类，weijie老师之前针对这个写了很多篇帖子了，大多数时候同一个聚类里面回测的信号是差不多的，但是有时候会有奇迹，这样是一个很好的节约回测次数的操作。

至于何为表现好的alpha，论坛里面有很多大佬已经写了很多相关帖子了，这里简述一下我的提交准则：

sharpe最低不能小于1.3,fitness最低不能小于0.9，margin不能低于每个地区的提交阈值，turnover控制在20以内，two_year_sharpe不能低于1.4；

平均sharpe大于1.58，平均fitness大于1.2，平均margin大于20bps,平均prood_corr小于0.7.

在这后面我一直遵循这样的提交习惯进行提交，vf和combine的上升也证明了这样的习惯是可行的

最后感谢国区的老师们和论坛、社区的各位大佬！感谢大家的无私奉献！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享，经验里干货满满，不懈的坚持终于换来了combine的提升

也祝我自己的combine能越来越高哈哈

=============================================================================


---

### 技术对话片段 149 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【经验分享】菜鸟日记代码小白如何稳住6个月VF09经验分享.md
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

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

GM大佬不光优秀 还如此谦虚  简直是满分顾问

===================================================================================


---

### 技术对话片段 150 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

GM大佬不光优秀 还如此谦虚  简直是满分顾问

===================================================================================


---

### 技术对话片段 151 (原帖: 【”羊毛“合集】可供使用的AI免费资源)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【羊毛合集】可供使用的AI免费资源_37800870021015.md
- **时间**: 5 months ago

**提问/主帖背景 (WL13229)**:
1. [【邪修】当龙虾没有饲料了怎么办？白嫖啊！]([L2] 【邪修】当龙虾没有饲料了怎么办白嫖啊_39252022275223.md)
2. [【工具推荐】claude-code-proxy + AI打工人：使用免费的大模型白嫖打工人！ – WorldQuant BRAIN]([L2] 【工具推荐】claude-code-proxy  AI打工人使用免费的大模型白嫖打工人经验分享_37776070276119.md)
3. [谷歌Antigravity 如何使用Skills – WorldQuant BRAIN]([Commented] 谷歌Antigravity 如何使用Skills_37701654477847.md)
4. [盘点最近薅到的免费大模型 – WorldQuant BRAIN]([L2] 盘点最近薅到的免费大模型经验分享_37662026299543.md)
5. [免费大模型羊毛薅不完 – WorldQuant BRAIN]([L2] 免费大模型羊毛薅不完_37337374764695.md)
6. [【体验Sub Agent】将Antigravity的额度反向代理给Claude Code – WorldQuant BRAIN]([L2] 【体验Sub Agent】将Antigravity的额度反向代理给Claude Code经验分享_37267205177751.md)
7. [[MCP-守护] 让你的mcp无视token限制，实现免费的MAX模式 – WorldQuant BRAIN]([L2] [MCP-守护] 让你的mcp无视token限制实现免费的MAX模式经验分享_37220062772375.md)
8. [有趣的项目分享：网页版Gemini转API调用（Gemini-API） – WorldQuant BRAIN]([L2] 有趣的项目分享网页版Gemini转API调用Gemini-API代码优化_37163474989079.md)
9. [【Community Leader -因子构造 💎】TRAE+MCP 自动挖掘因子 – WorldQuant BRAIN]([L2] 【Community Leader -因子构造 】TRAEMCP 自动挖掘因子经验分享_37116093087895.md)
10. [【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用 – WorldQuant BRAIN]([L2] 【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用_37088940070295.md)
11. [【亲测可用】gemini3 pro学生优惠0成本纯白嫖保姆级教程！！！！ – WorldQuant BRAIN]([L2] 【亲测可用】gemini3 pro学生优惠0成本纯白嫖保姆级教程经验分享_37082297693719.md)
12. [【白嫖2年AI！】如何完成学生认证并使用长达2年的免费Copilot_pro+配置wq_mcp – WorldQuant BRAIN]([L2] 【白嫖2年AI】如何完成学生认证并使用长达2年的免费Copilot_pro配置wq_mcp经验分享_37024075283223.md)
13. [【Community Leader - 工具配置】免费大模型实现七十二变 经验分享 – WorldQuant BRAIN]([L2] 【Community Leader - 工具配置】免费大模型实现七十二变 经验分享经验分享_37013032632215.md)
14. [【MCP WorkFlow】MCP本地LLM配置 – WorldQuant BRAIN]([L2] 【MCP WorkFlow】MCP本地LLM配置经验分享_36975707112727.md)
15. [Gemini cli运行MCP工作流 从入门到入土问题解决 – WorldQuant BRAIN]([L2] Gemini cli运行MCP工作流  从入门到入土问题解决经验分享_36946833823895.md)
16. [【Community Leader -因子构造 💎】零预算网页端LLM + notebook + markdown指令交互流程: 附流程图 – WorldQuant BRAIN]([L2] 【Community Leader -因子构造 】零预算网页端LLM  notebook  markdown指令交互流程 附流程图经验分享_36944089777047.md)
17. [用 Gmail 账号匹配学生后登录 Gemini CLI，提示错误？部分踩坑与解决记录： – WorldQuant BRAIN]([L2] 用 Gmail 账号匹配学生后登录 Gemini CLI提示错误部分踩坑与解决记录经验分享_36907467592727.md)
18. [【Community Leader -因子构造 💎】零预算持续生成Alpha模板：通用大模型的辅助应用（附表达式生成指令） – WorldQuant BRAIN]([L2] 【Community Leader -因子构造 】零预算持续生成Alpha模板通用大模型的辅助应用附表达式生成指令论坛精选_36881490529815.md)
19. [【AI使用问题解决方案】如何正常登陆antigravity IDE （windows和mac通用），学生认证可以免费一年gemin3pro – WorldQuant BRAIN]([L2] 【AI使用问题解决方案】如何正常登陆antigravity IDE windows和mac通用学生认证可以免费一年gemin3pro经验分享_36879336144023.md)
20. [[MCP]免费使用阿里云100万token – WorldQuant BRAIN]([L2] [MCP]免费使用阿里云100万token经验分享_36852577295127.md)
21. [iflow心流 - 个人用户免费使用的API，如何在Linux服务器部署并配置mcp，让AI连续工作 – WorldQuant BRAIN]([L2] iflow心流 - 个人用户免费使用的API如何在Linux服务器部署并配置mcp让AI连续工作_36765806842007.md)
22. [【Community Leader - 因子构造】【睡一觉就改好】IND地区Robust universe Sharpe优化及MCP全自动因子回测，从0.7+到>1.0（附工作流及Prompt） – WorldQuant BRAIN]([L2] 【Community Leader - 因子构造】【睡一觉就改好】IND地区Robust universe Sharpe优化及MCP全自动因子回测从07到10附工作流及Prompt经验分享_36672024628119.md)
23. [【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索（附学生优惠方法/提示词/在服务器中使用） – WorldQuant BRAIN]([L2] 【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索附学生优惠方法提示词在服务器中使用经验分享_36634788057367.md)
24. [使用VSCODE中的通义灵码自建免费MCP – WorldQuant BRAIN]([L2] 使用VSCODE中的通义灵码自建免费MCP_36617019073943.md)
25. [[MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境 – WorldQuant BRAIN]([L2] [MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境经验分享_36512374893207.md)
26. [【免费API】使用大模型自动生成Power Pool Alpha描述 – WorldQuant BRAIN]([L2] 【免费API】使用大模型自动生成Power Pool Alpha描述_35026037757463.md)
27. [cline配置mcp与免费模型x及使用分享 – WorldQuant BRAIN]([L2] cline配置mcp与免费模型x及使用分享_34659891387031.md)
28. [[分享]白嫖才是王道，从搭建到实战免费最强版MCP – WorldQuant BRAIN]([L2] [分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)
29. [【傻瓜式安装教程】傻瓜式安装claude-code-router使用ai打工人的免费api – WorldQuant BRAIN]([L2] 【傻瓜式安装教程】傻瓜式安装claude-code-router使用ai打工人的免费api_37797346107671.md)
30. [【PPAC/Super Alpha Submitter】基于coze 生成描述，提交因子 – WorldQuant BRAIN]([L2] 【PPACSuper Alpha Submitter】基于coze 生成描述提交因子_36489114520471.md)
31. [英伟达免费模型接入Claude Code使用AI打工人]([L2] 英伟达免费模型接入Claude Code使用AI打工人经验分享_38011740910743.md)
32. [白嫖指南：长期稳定免费大模型 API]([L2] 白嫖指南长期稳定免费大模型 API_37982251006487.md)
33. [羊毛薅不完 Google for developers 每月10刀优惠 可用于调用Gemini api 助力你的AIAC 2.0](羊毛薅不完 Google for developers 每月10刀优惠 可用于调用Gemini api  助力你的AIAC 20_37983679645463.md)
34. [使用mcp+ai挖掘alpha过程中节约token的小技巧]([L2] 使用mcpai挖掘alpha过程中节约token的小技巧经验分享_38013569192983.md)
35. [【BRAIN 专属福利】KIMI 限时API额度羊毛活动来啦！](/hc/en-us/community/posts/37981514510359--BRAIN-%E4%B8%93%E5%B1%9E%E7%A6%8F%E5%88%A9-KIMI-%E9%99%90%E6%97%B6API%E9%A2%9D%E5%BA%A6%E7%BE%8A%E6%AF%9B%E6%B4%BB%E5%8A%A8%E6%9D%A5%E5%95%A6)

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢各位大佬无私分享，这波羊毛薅不完了！

感谢各位大佬无私分享，这波羊毛薅不完了！

===================================================================================


---

### 技术对话片段 152 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【课代表】【轻松点击即可完成参赛】CA 降维  多指标聚类数评判  KMeans  层次  DBSCAN 聚类的 Osmosis 点数分配工具经验分享_37023499938327.md
- **时间**: 6个月前

**提问/主帖背景 (XX42289)**:
# 特此感谢 [BJ65592](/hc/en-us/profiles/34337104554903-BJ65592) 的付出。

```
import urllib.parseimport loggingimport numpy as npimport pandas as pdfrom datetime import datetimefrom sklearn.preprocessing import StandardScaler, RobustScalerfrom sklearn.cluster import KMeans, DBSCAN, AgglomerativeClusteringfrom sklearn.metrics import silhouette_score, calinski_harabasz_scorefrom sklearn.decomposition import PCA# 假设该库返回requests.Session对象from machine_lib import login  def get_history_alpha_ids(s, region, start_date, limit=50, offset=0):    """    从接口分页获取指定地区、指定日期后的alpha数据    :param s: requests.Session对象，已完成登录的会话    :param region: 地区大写：USA, EUR ... ...    :param start_date: 过滤日期，获取该日期之后的因子    :param limit: 每页获取的数量    :param offset: 分页偏移量    :return: 包含alpha的id和各类is指标的列表    """    alphas_data = []    # 对日期字符串进行URL编码，避免特殊字符影响请求    start_date_str = urllib.parse.quote(start_date.astimezone().isoformat(timespec='seconds'))    # 分页获取数据    while True:        url = (            f"[链接已屏蔽]            f"limit={limit}&offset={offset}"            f"&dateCreated%3E={start_date_str}"            f"&settings.region={region}"            f"&status!=UNSUBMITTED%1FIS-FAIL"            f"&hidden=false"            f"&order=-dateSubmitted"        )        try:            resp = s.get(url)            if resp.status_code != 200:                print(f"请求出错，状态码：{resp.status_code}")                break            data = resp.json()            results = data.get("results", [])            alphas_data.extend(results)            # 判断是否获取完所有数据，是则退出循环            if offset + len(results) >= data.get("count", 0) or len(results) < limit:                break            offset += limit        except Exception as e:            print(f"数据获取异常，异常信息：{e}")            break    # 提取需要的指标数据    alpha_metrics = []    for item in alphas_data:        # 检查is中的关键指标是否存在，避免键缺失报错        is_data = item.get('is', {})        metrics = {            'id': item['id'],            'fitness': is_data.get('fitness', 0.0),            'longCount': is_data.get('longCount', 0.0),            'shortCount': is_data.get('shortCount', 0.0),            'turnover': is_data.get('turnover', 0.0),            'returns': is_data.get('returns', 0.0),            'drawdown': is_data.get('drawdown', 0.0),            'margin': is_data.get('margin', 0.0),            'sharpe': is_data.get('sharpe', 0.0)        }        alpha_metrics.append(metrics)    if not alpha_metrics:        print("错误：没有获取到有效的alpha数据")        return []    return alpha_metricsdef determine_clusters_multi_criteria(X, min_clusters=5, max_clusters=50):    """    多指标确定聚类数（结合轮廓系数、CH指数，同时限制聚类数范围）    :param X: 标准化后的特征数据    :param min_clusters: 最小聚类数（避免过少）    :param max_clusters: 最大聚类数（避免过多）    :return: 最终聚类数量    """    if len(X) <= min_clusters:        return len(X)  # 样本数少于最小聚类数时，取样本数    # 限制聚类数范围：2 ~ 样本数（但不超过max_clusters，不低于min_clusters）    cluster_range = range(max(2, min_clusters), min(max_clusters + 1, len(X)))    scores = []    for k in cluster_range:        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')        labels = kmeans.fit_predict(X)        # 轮廓系数：衡量聚类紧密度和分离度，越接近1越好        sil_score = silhouette_score(X, labels)        # CH指数：数值越大表示聚类效果越好（类内紧密，类间分离）        ch_score = calinski_harabasz_score(X, labels)        # 综合得分（归一化后加权，可调整权重）        scores.append({            'k': k,            'sil': sil_score,            'ch': ch_score,            # 权重可调整，平衡轮廓系数和CH指数的影响            'composite': 0.4 * sil_score + 0.6 * (ch_score / 100000)        })    # 转换为DataFrame方便排序    score_df = pd.DataFrame(scores)    # 按综合得分降序排序，取第一个作为最佳聚类数    best_k = score_df.sort_values('composite', ascending=False)['k'].iloc[0]    # 兜底：确保聚类数在合理范围    best_k = max(min_clusters, min(best_k, max_clusters))    return best_kdef cluster_alphas_improved(alpha_metrics, use_pca=True, cluster_algorithm='kmeans'):    """    改进的聚类逻辑：支持PCA降维、多种聚类算法、多指标确定聚类数    :param alpha_metrics: alpha的指标数据    :param use_pca: 是否使用PCA降维（处理特征冗余）    :param cluster_algorithm: 聚类算法（kmeans/agglomerative/dbscan）    :return: 选中的alpha列表（每个聚类fitness最大）    """    # 转换为DataFrame方便处理    df = pd.DataFrame(alpha_metrics)    # 定义用于聚类的特征列    feature_cols = ['longCount', 'shortCount', 'turnover', 'returns', 'drawdown', 'margin', 'sharpe']    # 提取特征数据，处理缺失值（填充0）    X = df[feature_cols].fillna(0).values    # 改进1：使用RobustScaler标准化（抗异常值，比StandardScaler更适合金融数据）    scaler = RobustScaler()  # 替代StandardScaler，对异常值不敏感    X_scaled = scaler.fit_transform(X)    # 改进2：PCA降维（处理特征冗余，减少噪声）    if use_pca and len(feature_cols) > 2:        # 保留95%的方差，自动确定降维后的维度        pca = PCA(n_components=0.95, random_state=42)        X_processed = pca.fit_transform(X_scaled)        print(f"PCA降维后，特征维度从{len(feature_cols)}变为{X_processed.shape[1]}")    else:        X_processed = X_scaled    # 改进3：多指标确定聚类数（避免聚类数过少）    best_k = determine_clusters_multi_criteria(X_processed, min_clusters=5, max_clusters=50)    print(f"改进后确定的最佳聚类数量：{best_k}")    # 改进4：支持多种聚类算法（KMeans/层次聚类/DBSCAN）    if cluster_algorithm == 'kmeans':        # KMeans：适合球形分布，速度快        cluster_model = KMeans(n_clusters=best_k, random_state=42, n_init='auto')        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'agglomerative':        # 层次聚类：不假设球形分布，更灵活        cluster_model = AgglomerativeClustering(n_clusters=best_k)        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'dbscan':        # DBSCAN：无需指定聚类数，自动识别密度聚类（适合非球形分布）        # eps和min_samples可调整：eps越大，聚类数越少；min_samples越大，聚类数越多        cluster_model = DBSCAN(eps=0.5, min_samples=5)        df['cluster'] = cluster_model.fit_predict(X_processed)        # DBSCAN的-1表示噪声点，单独处理为一个聚类        noise_cluster = df['cluster'].max() + 1        df.loc[df['cluster'] == -1, 'cluster'] = noise_cluster        best_k = len(df['cluster'].unique())        print(f"DBSCAN聚类后实际聚类数量：{best_k}")    # 每个聚类中选择fitness最大的alpha    selected_alphas = []    for cluster in df['cluster'].unique():        cluster_df = df[df['cluster'] == cluster]        # 取fitness最大的行        best_alpha = cluster_df.loc[cluster_df['fitness'].idxmax()]        selected_alphas.append(best_alpha.to_dict())    return selected_alphasif __name__ == '__main__':    # 配置参数：顾问相关日期、分页参数    advisor_date = datetime(2020, 1, 1)  # 成为顾问的日期，用于过滤该日期之后的因子    page_limit = 100  # 每页获取的alpha数量    page_offset = 0   # 分页起始偏移量    target_region = "EUR"  # 目标地区    # 初始化登录会话    session = login()    logging.info("登录成功，开始获取alpha数据")    # 获取alpha的指标数据    alpha_metrics_list = get_history_alpha_ids(        s=session,        region=target_region,        start_date=advisor_date,        limit=page_limit,        offset=page_offset    )    # 校验数据是否有效    if not alpha_metrics_list:        print("程序终止：未获取到有效alpha数据")        exit(1)    # 执行聚类并选择每个类别中fitness最大的alpha    selected_alpha_list = cluster_alphas_improved(        alpha_metrics=alpha_metrics_list,        use_pca=True,        cluster_algorithm='kmeans'    )    # 校验聚类结果    if not selected_alpha_list:        print("程序终止：聚类后未选中任何alpha")        exit(1)    # 计算平均权重并分配分数（总分为100000）    total_selected = len(selected_alpha_list)    per_alpha_weight = 1.0 / total_selected if total_selected > 0 else 0.0    total_allocated_score = 0    # 遍历选中的alpha，输出信息并计算分数    for alpha_info in selected_alpha_list:        alpha_score = int(per_alpha_weight * 100000)        print(            f"Alpha ID：{alpha_info['id']} | "            f"Fitness值：{alpha_info['fitness']} | "            f"所属聚类：{alpha_info['cluster']} | "            f"分配分数：{alpha_score}"        )        # 如需调用接口更新分数，取消以下注释        update_url = f"[链接已屏蔽]        session.patch(update_url, json={"osmosisPoints": alpha_score})        total_allocated_score += alpha_score    # 处理四舍五入导致的分数偏差    score_deviation = 100000 - total_allocated_score    if score_deviation != 0:        print(f"\n因四舍五入产生分数偏差：{score_deviation}分，已将偏差分加到第一个Alpha上")        # 修正第一个Alpha的分数        first_alpha_score = int(per_alpha_weight * 100000) + score_deviation        print(f"第一个Alpha {selected_alpha_list[0]['id']} 的最终分数：{first_alpha_score}")        total_allocated_score = 100000    # 输出最终分配结果    print(f"\n分数分配完成：总分配分数 {total_allocated_score} 分，无分数损耗")
```

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢课代表，这下真做到一键参赛了哈哈

===================================================================================


---

### 技术对话片段 153 (原帖: 【重复回测&哈希】大家是如何做好避免重复回测的？哈希是否是一个好的方案)
- **原帖链接**: [Commented] 【重复回测哈希】大家是如何做好避免重复回测的哈希是否是一个好的方案.md
- **时间**: 5个月前

**提问/主帖背景 (ZT38415)**:
## 问题

在回测过程中，有时候会出现重复回测的情况，这个在之前传统的一二三阶回测方案中，采用了记录断点后，进行断点续跑的方案。但是随着我当前构建的回测系统逐渐复杂，尤其是开始利用冷神的模板群方案后，对于避免重复回测成了一个难题。我当前是构建了一个较为复杂的json

```
{    "塔名": {        "pyramid_info": {            "pyramid_status": "light" | "completed_high_quality" | "completed_all_processed" | "in_progress",            "total_high_quality_signals": 0,            "created_time": "2025-10-03T...",            "last_updated": "2025-10-03T..."        },        "datasets": {            "数据集ID": {                "dataset_info": {                    "dataset_status": "completed" | "no_signal" | "interrupted",                    "current_expression_idx": 0,                    "total_expressions": 0,                    "high_quality_count": 0,                    "yellow_count": 0,                    "created_time": "2025-10-03T...",                    "last_updated": "2025-10-03T..."                },                "templates": {                    "T类型_索引": {                        "template_status": "completed" | "in_progress",                        "current_alpha_idx": 0,                        "high_quality_count": 0,                        "yellow_count": 0,                        "total_alpha_number": 0                    }                }            }        }    }}
```

但是后续我应该会逐渐修改我的回测系统，每次都要做好对之前系统回测记录的兼容，导致代码预发复杂，并且很可能导致记录出错，漏掉一些回测或者重复一些回测。

## 思路

我当前还没有用数据库，现在新的思路是每次的回测数据都提前记录为hash值

```
def generate_task_hash(sim_data):    """    计算 sim_data 的 SHA256 哈希值作为唯一任务 ID (task_id)。    对字典进行规范化排序(sort_keys=True)以确保相同内容的字典得到相同的哈希。    """    # 规范化 JSON 字符串    normalized_json = json.dumps(sim_data, sort_keys=True)    # 计算哈希    return hashlib.sha256(normalized_json.encode('utf-8')).hexdigest()
```

为了节约空间，只在文件中保持哈希数据，并且按照字典序排序。后面回测前，都先计算回测数据的哈希值，并且利用二分（复杂度logN，速度应该还是很快的）进行检索，如果不存在才进行回测，不知这样是否可行。对于可能在利用数据库的大家，是直接把所有回测数据都存在数据库中进行检索避免重复回测吗？我在想这样是不是会占用太大内存？以及大家是否有更好的方案呢

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

+1  我目前也是靠哈希来查重 避免重复回测的

之前问AI AI推荐的这个方案，不知道还有没有更好的方案哈哈

===================================================================================


---

### 技术对话片段 154 (原帖: 【重复回测&哈希】大家是如何做好避免重复回测的？哈希是否是一个好的方案)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【重复回测哈希】大家是如何做好避免重复回测的哈希是否是一个好的方案_36530366174615.md
- **时间**: 5个月前

**提问/主帖背景 (ZT38415)**:
## 问题

在回测过程中，有时候会出现重复回测的情况，这个在之前传统的一二三阶回测方案中，采用了记录断点后，进行断点续跑的方案。但是随着我当前构建的回测系统逐渐复杂，尤其是开始利用冷神的模板群方案后，对于避免重复回测成了一个难题。我当前是构建了一个较为复杂的json

```
{    "塔名": {        "pyramid_info": {            "pyramid_status": "light" | "completed_high_quality" | "completed_all_processed" | "in_progress",            "total_high_quality_signals": 0,            "created_time": "2025-10-03T...",            "last_updated": "2025-10-03T..."        },        "datasets": {            "数据集ID": {                "dataset_info": {                    "dataset_status": "completed" | "no_signal" | "interrupted",                    "current_expression_idx": 0,                    "total_expressions": 0,                    "high_quality_count": 0,                    "yellow_count": 0,                    "created_time": "2025-10-03T...",                    "last_updated": "2025-10-03T..."                },                "templates": {                    "T类型_索引": {                        "template_status": "completed" | "in_progress",                        "current_alpha_idx": 0,                        "high_quality_count": 0,                        "yellow_count": 0,                        "total_alpha_number": 0                    }                }            }        }    }}
```

但是后续我应该会逐渐修改我的回测系统，每次都要做好对之前系统回测记录的兼容，导致代码预发复杂，并且很可能导致记录出错，漏掉一些回测或者重复一些回测。

## 思路

我当前还没有用数据库，现在新的思路是每次的回测数据都提前记录为hash值

```
def generate_task_hash(sim_data):    """    计算 sim_data 的 SHA256 哈希值作为唯一任务 ID (task_id)。    对字典进行规范化排序(sort_keys=True)以确保相同内容的字典得到相同的哈希。    """    # 规范化 JSON 字符串    normalized_json = json.dumps(sim_data, sort_keys=True)    # 计算哈希    return hashlib.sha256(normalized_json.encode('utf-8')).hexdigest()
```

为了节约空间，只在文件中保持哈希数据，并且按照字典序排序。后面回测前，都先计算回测数据的哈希值，并且利用二分（复杂度logN，速度应该还是很快的）进行检索，如果不存在才进行回测，不知这样是否可行。对于可能在利用数据库的大家，是直接把所有回测数据都存在数据库中进行检索避免重复回测吗？我在想这样是不是会占用太大内存？以及大家是否有更好的方案呢

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

+1  我目前也是靠哈希来查重 避免重复回测的

之前问AI AI推荐的这个方案，不知道还有没有更好的方案哈哈

===================================================================================


---

### 技术对话片段 155 (原帖: 【顾问进阶】一文读懂风险中心化，掌握使用方法)
- **原帖链接**: [Commented] 【顾问进阶】一文读懂风险中心化掌握使用方法.md
- **时间**: 7个月前

**提问/主帖背景 (MH33574)**:
今天早上收到公告通知11月起， **PowerPool将仅接受风险中性化的因子，顾问仍然可以使用其他的非风险中性化（MARKET, SECTOR, INDUSTRY, SUBINDUSTRY, COUNTRY) 回测，但只有符合RA标准的才可以提交** 。很多新顾问可能还不太熟悉风险中性化这个概念，希望这篇文章对你有帮助

### **1. 什么是风险中性化？**

- **定义** ：“风口来了猪都可以飞上天”，风险中性化就是在去除已知的“风”。 风险中性化是一种通过消除特定风险因子对Alpha影响的技术，使Alpha的表现更加纯粹，专注于捕捉市场异常。通过风险中性化，可以剔除市场、行业或风格因子等已知风险对Alpha收益的干扰，从而更准确地评估Alpha的独立性和有效性。

- **理论背景** ：风险因子是影响资产收益的主要驱动因素，例如市场风险、行业风险、动量因子等。经典理论：Fama-French三因子模型（市场、规模、价值）和套利定价理论（APT）为风险因子模型奠定了基础。

### **2. 为什么要做风险中性化？**

- **消除已知风险因子的干扰** ：如果Alpha的收益完全由已知风险因子解释，则其价值有限，因为这些因子可以通过简单的模型复制。风险中性化可以帮助研究者专注于Alpha捕捉的独特市场异常。

- **降低风险** ：减少因风险因子回撤或波动性导致的潜在损失。提高Alpha在不同市场条件下的稳健性。

- **提升Alpha性能** ：通过剔除不必要的风险因子，提高Alpha的Sharpe比率，减少回撤，并优化换手率与交易成本之间的平衡。

### **3. 风险中性化的好处**

- **更高的Alpha独立性** ：通过剔除风险因子，Alpha表现更独立，能够更好地反映其捕捉市场异常的能力。

- **降低拥挤交易风险** ：减少因市场中大量投资者持有相似头寸而导致的价格剧烈波动。

- **增强多样性** ：通过不同的风险中性化方法，生成多样化的信号，丰富Alpha池。

- **优化长期表现** ：在保留Alpha收益的同时显著降低风险，提供更稳定、可靠的长期表现。

### **4. 如何使用风险中性化？**

- **界面操作** ：在BRAIN平台的回测界面中，进入模拟设置（Simulation Settings），在 `Neutralization` 选项中选择对应的风险中性化方法，BRAIN平台内置了六种风险中性：FAST, SLOW, SLOW_AND_FAST, CROWDING, STATISTICAL, REVERSION_AND_MOMENTUM (RAM)

- **API操作** ：在API中，通过调整代码中的 `neutralization` 参数实现。例如

```
{    "instrumentType": "EQUITY",    "region": "USA",    "universe": "TOP3000",    "delay": 1,    "decay": 0,    "neutralization": "FAST",  // 替换为上述对应的风险中性化方法    "truncation": 0.1,    "pasteurization": "ON",    "unitHandling": "VERIFY",    "nanHandling": "ON",    "language": "FASTEXPR",    "visualization": false}
```

### **5. 不同的风险中性化方法及其使用场景**

以下是平台支持的六种风险中性化方法的详细介绍：

#### **5.1 FAST**

- **定义** ：快速因子（Fast Factors）包括市场和行业风格因子，和高换手率的风格因子，例如反转因子。
- **适用场景** ：
  - 高换手率信号。
  - 需要捕捉短期市场趋势的Alpha。
- **注意事项** ：
  - 使用FAST中性化可能会增加Alpha的换手率。

#### **5.2 SLOW**

- **定义** ：慢速因子（Slow Factors）包括低换手率的风格因子，例如价值因子。
- **适用场景** ：
  - 低换手率信号。
  - 更关注长期趋势的Alpha。
- **注意事项** ：
  - SLOW因子适合稳健型投资策略。

#### **5.3 SLOW_AND_FAST**

- **定义** ：结合了慢速因子和快速因子的综合模型。
- **适用场景** ：
  - 需要同时考虑短期和长期趋势的Alpha。
  - 适合多样化的投资策略。
- **注意事项** ：
  - 可能会增加换手率，但能更全面地中性化风险。

#### **5.4 RAM（Reversion and Momentum）**

- **反转因子（REVERSION）** ：捕捉短期均值回归现象（如5天内的价格回调）。
- **定义** ：市场通常会对短期事件过度反应，导致暂时性错误定价。随着这些市场效率的修正，超卖的股票价格恢复，超买的股票价格回落。短期反转因子捕捉股票价格的均值回归现象，即近期表现不佳的股票往往在未来获得更高的回报，而近期表现较好的股票可能会出现回调。

- **动量因子（MOMENTUM）** ：捕捉长期价格趋势（如12个月内的价格趋势）。动量因子识别股票价格的持续趋势，即近期表现较好的股票往往继续上涨，而表现较差的股票则可能继续下跌。基于趋势跟随原则，已建立的价格趋势更可能延续而非逆转
- **适用场景** ：
  - 需要对冲短期均值回归和长期动量趋势的Alpha。
- **注意事项** ：
  - RAM中性化适用于多空平衡的Alpha。
  - 建议结合Alpha的特性，评估其是否容易受到反转或动量因子的影响。

#### **5.5 CROWDING**

- **定义** ：拥挤风险中性化，控制因市场中大量投资者持有相似头寸而导致的风险。随着更多投资者进入相同的头寸，交易的盈利能力可能下降。虽然价格在初期可能上涨，但随后可能变得脆弱，容易出现大幅下跌。
- **适用场景** ：需要减少拥挤交易风险的Alpha。当过多投资者同时试图卖出相同的头寸时，价格可能迅速下跌，导致更大的损失。适合在动量趋势强烈的市场中使用。

- **注意事项** ：拥挤风险中性化适用于多空平衡的Alpha。需要结合Alpha的特性，评估其是否容易受到拥挤交易的影响。

#### **5.6 STATISTICAL**

- **定义** ：因子模型的两大类别：基本面因子模型（Fundamental Factor Models）和基于统计因子模型（Statistical Factor Models），其中第二种使用统计技术（如主成分分析PCA或聚类分析）分析证券收益，识别市场数据中的模式和关系。依赖历史收益数据，通过统计方法预测未来表现或优化投资组合风险。经典案例比如：Roll和Ross的《套利定价理论的实证研究》（APT），强调使用统计方法提取影响资产收益的多个因子。
- **适用场景** ：捕捉复杂非线性关系的Alpha，生成在特定收益空间中表现良好的信号。

- **注意事项** ：
  - 统计风险中性化依赖于历史数据，可能对数据质量较为敏感。
  - 建议结合Alpha的特性，评估其是否适合统计模型的应用。

### **6. 总结**

- **风险中性化的核心价值** ：
  - 通过剔除已知风险因子，优化Alpha表现，降低风险。
- **选择合适的方法** ：
  - 根据Alpha的特点（如换手率、风险敞口）选择合适的风险中性化方法。
- **个人建议** ：
  - 在Simulation中先抽样一部分，尝试不同的风险中性化设置，评估其对Alpha表现的影响，选择最合适的再进行全量的回测

**英文原版文档阅读：**

[Getting Started: Risk Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Risk Neutralized Metrics | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Crowding Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Statistical Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with RAM Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！
各类Risk-neutralization的适用因子写的很清楚，这样就可以有的放矢地针对性的选择适合的中性化类型了！

===================================================================================


---

### 技术对话片段 156 (原帖: 【顾问进阶】一文读懂风险中心化，掌握使用方法)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【顾问进阶】一文读懂风险中心化掌握使用方法_35954596858903.md
- **时间**: 8 months ago

**提问/主帖背景 (MH33574)**:
今天早上收到公告通知11月起， **PowerPool将仅接受风险中性化的因子，顾问仍然可以使用其他的非风险中性化（MARKET, SECTOR, INDUSTRY, SUBINDUSTRY, COUNTRY) 回测，但只有符合RA标准的才可以提交** 。很多新顾问可能还不太熟悉风险中性化这个概念，希望这篇文章对你有帮助

### **1. 什么是风险中性化？**

- **定义** ：“风口来了猪都可以飞上天”，风险中性化就是在去除已知的“风”。 风险中性化是一种通过消除特定风险因子对Alpha影响的技术，使Alpha的表现更加纯粹，专注于捕捉市场异常。通过风险中性化，可以剔除市场、行业或风格因子等已知风险对Alpha收益的干扰，从而更准确地评估Alpha的独立性和有效性。

- **理论背景** ：风险因子是影响资产收益的主要驱动因素，例如市场风险、行业风险、动量因子等。经典理论：Fama-French三因子模型（市场、规模、价值）和套利定价理论（APT）为风险因子模型奠定了基础。

### **2. 为什么要做风险中性化？**

- **消除已知风险因子的干扰** ：如果Alpha的收益完全由已知风险因子解释，则其价值有限，因为这些因子可以通过简单的模型复制。风险中性化可以帮助研究者专注于Alpha捕捉的独特市场异常。

- **降低风险** ：减少因风险因子回撤或波动性导致的潜在损失。提高Alpha在不同市场条件下的稳健性。

- **提升Alpha性能** ：通过剔除不必要的风险因子，提高Alpha的Sharpe比率，减少回撤，并优化换手率与交易成本之间的平衡。

### **3. 风险中性化的好处**

- **更高的Alpha独立性** ：通过剔除风险因子，Alpha表现更独立，能够更好地反映其捕捉市场异常的能力。

- **降低拥挤交易风险** ：减少因市场中大量投资者持有相似头寸而导致的价格剧烈波动。

- **增强多样性** ：通过不同的风险中性化方法，生成多样化的信号，丰富Alpha池。

- **优化长期表现** ：在保留Alpha收益的同时显著降低风险，提供更稳定、可靠的长期表现。

### **4. 如何使用风险中性化？**

- **界面操作** ：在BRAIN平台的回测界面中，进入模拟设置（Simulation Settings），在 `Neutralization` 选项中选择对应的风险中性化方法，BRAIN平台内置了六种风险中性：FAST, SLOW, SLOW_AND_FAST, CROWDING, STATISTICAL, REVERSION_AND_MOMENTUM (RAM)

- **API操作** ：在API中，通过调整代码中的 `neutralization` 参数实现。例如

```
{    "instrumentType": "EQUITY",    "region": "USA",    "universe": "TOP3000",    "delay": 1,    "decay": 0,    "neutralization": "FAST",  // 替换为上述对应的风险中性化方法    "truncation": 0.1,    "pasteurization": "ON",    "unitHandling": "VERIFY",    "nanHandling": "ON",    "language": "FASTEXPR",    "visualization": false}
```

### **5. 不同的风险中性化方法及其使用场景**

以下是平台支持的六种风险中性化方法的详细介绍：

#### **5.1 FAST**

- **定义** ：快速因子（Fast Factors）包括市场和行业风格因子，和高换手率的风格因子，例如反转因子。
- **适用场景** ：
  - 高换手率信号。
  - 需要捕捉短期市场趋势的Alpha。
- **注意事项** ：
  - 使用FAST中性化可能会增加Alpha的换手率。

#### **5.2 SLOW**

- **定义** ：慢速因子（Slow Factors）包括低换手率的风格因子，例如价值因子。
- **适用场景** ：
  - 低换手率信号。
  - 更关注长期趋势的Alpha。
- **注意事项** ：
  - SLOW因子适合稳健型投资策略。

#### **5.3 SLOW_AND_FAST**

- **定义** ：结合了慢速因子和快速因子的综合模型。
- **适用场景** ：
  - 需要同时考虑短期和长期趋势的Alpha。
  - 适合多样化的投资策略。
- **注意事项** ：
  - 可能会增加换手率，但能更全面地中性化风险。

#### **5.4 RAM（Reversion and Momentum）**

- **反转因子（REVERSION）** ：捕捉短期均值回归现象（如5天内的价格回调）。
- **定义** ：市场通常会对短期事件过度反应，导致暂时性错误定价。随着这些市场效率的修正，超卖的股票价格恢复，超买的股票价格回落。短期反转因子捕捉股票价格的均值回归现象，即近期表现不佳的股票往往在未来获得更高的回报，而近期表现较好的股票可能会出现回调。

- **动量因子（MOMENTUM）** ：捕捉长期价格趋势（如12个月内的价格趋势）。动量因子识别股票价格的持续趋势，即近期表现较好的股票往往继续上涨，而表现较差的股票则可能继续下跌。基于趋势跟随原则，已建立的价格趋势更可能延续而非逆转
- **适用场景** ：
  - 需要对冲短期均值回归和长期动量趋势的Alpha。
- **注意事项** ：
  - RAM中性化适用于多空平衡的Alpha。
  - 建议结合Alpha的特性，评估其是否容易受到反转或动量因子的影响。

#### **5.5 CROWDING**

- **定义** ：拥挤风险中性化，控制因市场中大量投资者持有相似头寸而导致的风险。随着更多投资者进入相同的头寸，交易的盈利能力可能下降。虽然价格在初期可能上涨，但随后可能变得脆弱，容易出现大幅下跌。
- **适用场景** ：需要减少拥挤交易风险的Alpha。当过多投资者同时试图卖出相同的头寸时，价格可能迅速下跌，导致更大的损失。适合在动量趋势强烈的市场中使用。

- **注意事项** ：拥挤风险中性化适用于多空平衡的Alpha。需要结合Alpha的特性，评估其是否容易受到拥挤交易的影响。

#### **5.6 STATISTICAL**

- **定义** ：因子模型的两大类别：基本面因子模型（Fundamental Factor Models）和基于统计因子模型（Statistical Factor Models），其中第二种使用统计技术（如主成分分析PCA或聚类分析）分析证券收益，识别市场数据中的模式和关系。依赖历史收益数据，通过统计方法预测未来表现或优化投资组合风险。经典案例比如：Roll和Ross的《套利定价理论的实证研究》（APT），强调使用统计方法提取影响资产收益的多个因子。
- **适用场景** ：捕捉复杂非线性关系的Alpha，生成在特定收益空间中表现良好的信号。

- **注意事项** ：
  - 统计风险中性化依赖于历史数据，可能对数据质量较为敏感。
  - 建议结合Alpha的特性，评估其是否适合统计模型的应用。

### **6. 总结**

- **风险中性化的核心价值** ：
  - 通过剔除已知风险因子，优化Alpha表现，降低风险。
- **选择合适的方法** ：
  - 根据Alpha的特点（如换手率、风险敞口）选择合适的风险中性化方法。
- **个人建议** ：
  - 在Simulation中先抽样一部分，尝试不同的风险中性化设置，评估其对Alpha表现的影响，选择最合适的再进行全量的回测

**英文原版文档阅读：**

[Getting Started: Risk Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Risk Neutralized Metrics | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Crowding Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Statistical Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with RAM Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！
各类Risk-neutralization的适用因子写的很清楚，这样就可以有的放矢地针对性的选择适合的中性化类型了！

===================================================================================


---

### 技术对话片段 157 (原帖: 【龙虎榜·卷二】Combine惊雷再起，VF季决尘埃落定，神秘GM满值归来，万刀之上几何？)
- **原帖链接**: [Commented] 【龙虎榜卷二】Combine惊雷再起VF季决尘埃落定神秘GM满值归来万刀之上几何.md
- **时间**: 24天前

**提问/主帖背景 (AL13375)**:
### 山河震荡，榜动九州。

昨日 **Combine** 异动方歇，今朝惊雷又至；VF季决终章落笔，有人封侯拜相，有人黯然离场。

今日鹿死谁手，且看谁夺虎符，谁占龙庭！

### 顾问龙虎榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant顾问龙虎榜
> 2026-05-09
> Max VF
> Max WF
> Max Combine
> Max
> Combine
> Max Pyramid
> Rank
> VF
> Rank
> l0
> VF
> Rank
> CM
> Rank
> AVG
> Rank
> PYR
> AL
> 丛48527
> L00
> 019316
> 177143
> 460270
> 117
> 174218
> 383
> 159893
> 191
> 0123443
> 100
> 丛82709
> 136323
> 1074218
> 594
> 山60270
> 346
> 丛76363
> 57
> 172
> 卫B89987
> L00
> 丛78692
> 132765
> R41479
> 669
> U772
> 299
> J79797
> 55
> 163
> )65210
> 100
> 038384
> 117086
> 0C68819
> 603
> 4569440
> 288
> 山52291
> 52
> 1566
> 6581389
> L00
> VP76790
> 107337
> W74107
> 601
> 087152
> 286
> 139934
> 51
> 181
> 187757
> 100
> 0053160
> 106350
> 087152
> 586
> 1640486
> 284
> 5283096
> 157
> 1480116
> L00
> R570387
> 104971
> L71036
> 573
> Y11344
> 282
> R588503
> 5
> 182
> MC61836
> 100
> 8233369
> 978.25
> 5V78590
> 566
> X221889
> 278
> 」022447
> 45
> 189
> WC63274
> L00
> 5824011
> 95169
> 2F97721
> 541
> LN566Z5
> 278
> 1022811
> 45
> 171
> 10
> W062208
> 100
> 10
> 065624
> 94664
> 10
> Y816410
> 507
> 10
> 0C68819
> 264
> 10
> 644463
> 44
> 187
> 5017531
> 100
> P55616
> 92697
> 1640486
> 505
> EN91858
> 260
> 456452
> 169
> SM18051
> 100
> NP19911
> 90286
> 0C29779
> 491
> 」10865
> 256
> 490970
> 4
> 151
> 5N68553
> 100
> IN41467
> 80712
> 0692378
> 489
> 5224058
> 249
> 0419310
> 183
> 14
> J91272
> 100
> 0N69057
> 78655
> 14
> U15616
> 488
> 5864976
> 2.48
> X54051
> 179
> XX88140
> 100
> V87972
> 59249
> y11344
> 488
> 15
> 4047730
> 242
> 492336
> 42
> 170
> 16
> XY56645
> 100
> 16
> N823017
> 57531
> 16
> GK78216
> 486
> N067211
> 238
> 16
> 844462
> 158
> X25924
> 100
> 4652134
> 56630
> 」16243
> 486
> E28881
> 236
> 17
> 417279
> 134
> 18
> Y81852
> 100
> 18
> 0N14408
> 66292
> 18
> VP87972
> 481
> 2V96737
> 231
> 18
> 422845
> 41
> 189
> y72634
> 100
> 工051363
> 56206
> E15829
> 473
> W74107
> 231
> 4595259
> 41
> 185
> 20
> VL28382
> 100
> 20
> SK72105
> 655.67
> 20
> P514747
> 472
> 20
> YC29686
> 229
> 20
> 442868
> 41
> 170
> YL9GOGB
> 100
> 卫36426
> 54475
> 5R35346
> 454
> 」38399
> 229
> 2434713
> 41
> 162
> 22
> 4597533
> 099
> N72745
> 62238
> 5073114
> 451
> M12075
> 227
> 5C23342
> 129
> 0H65852
> 099
> 023095
> 57937
> CZ67480
> 444
> 23
> 山61722
> 225
> W25030
> 153
> C186067
> 099
> 24
> 445359
> 57910
> 24
> 4466051
> 441
> 24
> WX81181
> 225
> 24
> 8L78449
> 151
> CIGO525
> 099
> D64455
> 57617
> 425519
> 440
> 25
> LX77gOI
> 224
> 4643324
> 40
> 145
> ;
> CX60157
> 099
> 26
> 8U17144
> 57124
> 26
> 0P93973
> 439
> 26
> J37401
> 221
> 26
> YX50005
> 131
> 0024306
> 099
> 卫97630
> 56442
> 卫32665
> 436
> 27
> 163377
> 221
> K77697
> 115
> 0577651
> 099
> 28
> U25385
> 56280
> 28
> 止55914
> 436
> 28
> YC76553
> 221
> 28
> 232536
> 181
> 013559
> 099
> 29
> 0065284
> 55801
> U48957
> 433
> 1L90629
> 219
> 卫054914
> 175
> 30
> H61566
> 099
> MB13430
> 55546
> 30
> ML42552
> 419
> 622438
> 215
> 30
> E60707
> 156
> 412949
> 099
> 1084732
> 55118
> NT98018
> 419
> Y78429
> 211
> L89289
> 156
> 445023
> 099
> 0N13413
> 53131
> 4047730
> 416
> XY54051
> 209
> T094100
> 152
> 32
> J62872
> 099
> IN75488
> 51806
> D64455
> 415
> ZE97721
> 206
> 8693974
> 150
> 34
> 184394
> 099
> 34
> NB63040
> 50977
> 34
> E17513
> 413
> !70892
> 203
> 34
> 79256
> 147
> 1015326
> 099
> 454882
> 50289
> IN84689
> 411
> 35
> 卫32665
> 203
> 5535873
> 132
> 36
> 1471010
> 099
> 36
> N896944
> 47395
> 36
> NN39972
> 410
> 36
> 5784537
> 202
> 36
> 丛61864
> 117
> 丛33773
> 099
> 4025992
> 47075
> 37
> 丛N89184
> 409
> 37
> 顾问 ZH78994 (Rank 11)
> 202
> 卫078486
> 117
> 1584247
> 099
> 38
> 0N98774
> 46047
> 38
> 067350
> 408
> 4066932
> 201
> 38
> 2C54526
> 174
> Ly85808
> 099
> IN52580
> 45893
> 」38399
> 403
> XS34596
> 201
> ZR94671
> 165
> 0Y56787
> 099
> 40
> T079250
> 45808
> 40
> VS91693
> 395
> Z018587
> 199
> 40
> 1015326
> 163
> N63388
> 099
> N63388
> 45263
> 41
> 029942
> 390
> Z135633
> 199
> 1033850
> 160
> "
> 0K32246
> 415591
> 44464
> 0428368
> 386
> P514747
> 198
> 0014840
> 159
> 丛48711
> 099
> N023388
> 44215
> 卫054914
> 382
> YC99371
> 197
> L74024
> 142
> RS73796
> 099
> 44
> 4815407
> 43841
> 44
> 必57672
> 370
> 4C60527
> 197
> 44
> 顾问 MG88592 (Rank 38)
> 141
> SKI4418
> 099
> 5N36193
> 43735
> CK70116
> 368
> 45
> 465370
> 197
> 2559763
> 139
> 46
> 5073114
> 099
> 46
> 4433535
> 43563
> 46
> NN67211
> 367
> 46
> V415439
> 192
> 46
> N19619
> 137
> IL73802
> 099
> 丛453550
> 42601
> U54006
> 366
> 47
> Y296589
> 192
> J96079
> 135
> 48
> 工530457
> 099
> 48
> 0P93973
> 41694
> 48
> ZC26080
> 366
> E76003
> 192
> 48
> 0X52484
> 133
> T72336
> 099
> ID21847
> 41547
> Sk84434
> 355
> 059336
> 190
> D29715
> 102
> 50
> J61722
> 099
> 50
> 工057923
> 41058
> 50
> 4075156
> 354
> 50
> Y82626
> 190
> 50
> 1262807
> 37
> 171
> 1591693
> 0.99
> IL11G8O
> 408.20
> 4121336
> 353
> 061316
> 190
> EX67304
> 37
> 164
> WP88606
> 099
> IN14420
> 40402
> 52
> E39657
> 352
> 52
> 4R44095
> 1.89
> 52
> 顾问 JR23144 (Rank 6)
> 37
> 145
> 53
> WX18521
> 099
> 53
> 1438752
> 401.64
> 53
> ZV96737
> 348
> YIIO136
> 188
> 53
> MB13430
> 37
> 137
> 54
> XD81759
> 099
> 54
> L69850
> 393.66
> 54
> Y780024
> 347
> CM97448
> 1.88
> 54
> 顾问 LW67640 (Rank 24)
> 37
> 135
> 55
> YL42885
> 099
> 55
> 5N71847
> 392.15
> 55
> C216695
> 341
> 55
> 010343
> 187
> 55
> 4269256
> 37
> 134
> 56
> W22772
> 099
> 56
> V56392
> 39208
> 56
> LL90629
> 340
> 56
> 5530834
> 187
> 56
> XM75236
> 37
> 133
> Y82997
> 099
> AL71656
> 38991
> 57
> YJ89646
> 339
> 57
> YZ99035
> 186
> 171699
> 36
> 171
> 58
> 2H71971
> 099
> 58
> 028126
> 381.57
> 58
> 163377
> 337
> YC82708
> 1.85
> 58
> XG98059
> 36
> 163
> 59
> 顾问 ZH78994 (Rank 11)
> 099
> LV57140
> 380.78
> 59
> E95623
> 333
> 丛L80893
> 185
> 59
> J61289
> 154
> 60
> ZX59531
> 099
> 60
> 0N30025
> 37803
> 60
> YH78429
> 331
> 60
> U63604
> 1.84
> 60
> 0123443
> 152
> 7Y77039
> 099
> 卫79519
> 37657
> P017729
> 330
> D19979
> 184
> 0N16452
> 36
> 150
> ZZ40911
> 099
> 4026227
> 369.68
> F47631
> 3.28
> YP74336
> 183
> 顾问 FD69320 (Rank 34)
> 147
> AC58355
> 098
> D57101
> 366.80
> 4096966
> 321
> W548176
> 182
> D28368
> 144
> C094009
> 098
> 473186
> 364.86
> KP22438
> 321
> 4457211
> 181
> 582574
> 141
> 0N91908
> 098
> 工032856
> 361.49
> L65774
> 320
> 」74499
> 180
> Y81055
> 131
> 卧17351
> 098
> T90403
> 360.89
> 1053797
> 318
> 66
> ZX24677
> 1.79
> 66
> 顾问 YX23928 (Rank 8)
> 130
> EK80645
> 098
> 5T37368
> 35392
> X83124
> 316
> STG1360
> 179
> 4092395
> 121
> 68
> [639655
> 098
> 497420
> 351.84
> 」93257
> 313
> 68
> 455707
> 1.78
> 68
> MK410G0
> 36
> 101
> EI96533
> 098
> 1I58194
> 34314
> U63604
> 311
> MB86518
> 178
> H39000
> 190
> 70
> 」47083
> 098
> 70
> 471281
> 341.81
> 70
> YL81651
> 311
> 70
> 190400
> 1.78
> 70
> 0L45135
> 160
> 71
> J53335
> 098
> 71
> 4854738
> 33999
> 71
> MD65015
> 310
> IK47019
> 178
> XZ69776
> 35
> 158
> 」81222
> 098
> 72
> 4079370
> 33395
> 72
> XZ21889
> 310
> 72
> 1L61351
> 177
> 72
> 1U53797
> 149
> 7
> 1433235
> 098
> 73
> CC72318
> 32780
> 73
> KP26017
> 309
> XM19402
> 177
> 73
> 2V96737
> 35
> 148
> 74
> 140932
> 098
> 74
> N068030
> 32565
> 74
> 5224058
> 309
> 1015326
> 177
> 74
> 4C78364
> 35
> 147
> NE92729
> 098
> 75
> M065015
> 32300
> 75
> AM12075
> 307
> 75
> 4578592
> 176
> 75
> CI68712
> 144
> 76
> MG68462
> 098
> 76
> YC82708
> 322.54
> 76
> ZH74761
> 306
> 76
> KS88333
> 176
> 76
> 4565681
> 35
> 139
> NN39972
> 098
> NN89351
> 32082
> 77
> 455707
> 305
> 77
> YC99622
> 176
> 77
> E578924
> 35
> 136
> 78
> 卫078486
> 098
> 78
> 0P82177
> 319.40
> 78
> V82626
> 305
> 」C84638
> 1.75
> 78
> 8W28426
> 129
> P669645
> 098
> 79
> D82796
> 31751
> 79
> 0y13559
> 304
> 79
> CL56494
> 175
> 79
> ZZ55695
> 35
> 124
> 80
> 0H40023
> 098
> H28002
> 316.18
> TN20848
> 302
> 80
> 顾问 YX23928 (Rank 8)
> 175
> 80
> Y288594
> 114
> 0482915
> 098
> 420384
> 31537
> U37372299
> EL15829
> 175
> PW58059
> 34
> 162
> P26750
> 098
> NT61860
> 31203
> Z210277
> 299
> 82
> 1053797
> 175
> 82
> J16084
> 34
> 149
> 023235
> 098
> A193287
> 311.42
> DL80869
> 298
> 止60830
> 174
> 顾问 WX84677 (Rank 69)
> 144
> PT85351
> 098
> NQ12289
> 308.65
> H65370
> 298
> 84
> 顾问 YH25030 (Rank 31)
> 1.74
> 84
> 顾问 CT48231 (Rank 2)
> 34
> 141
> 0068782
> 098
> 顾问 CC40930 (Rank 95)
> 30730
> ZH41150
> 298
> 85
> PC73872
> 173
> XH77948
> 34
> 137
> R636120
> 098
> 175132
> 30717
> 420306
> 295
> C521130
> 1733
> NG78013
> 34
> 133
> RW93893
> 098
> ND59617
> 305.52
> JC84638
> 294
> 5Z83096
> 173
> M551256
> 34
> 127
> 5C67341
> 0T75470
> 305.06
> 」79797
> 294
> 0L86385
> 1.72
> Z147333
> 121
> T16179
> 098
> 0482915
> 30315
> EN44285
> 293
> CX98570
> 171
> 164154
> 34
> 107
> D71562
> 098
> 442510
> 302.81
> 顾问 KZ79256 (Rank 21)
> 293
> 4220306
> 1.71
> R890992
> 34
> 102
> 顾问 VC95113 (Rank 58)
> 098
> NN52920
> 301.75
> 0026285
> 292
> K79256
> 171
> 2053542
> 191
> Uk29840
> 098
> TP73016
> 30135
> 5Z84537
> 292
> PY32594
> 170
> U474101
> 177
> U89028
> 98
> N480227
> 301.19
> TD22984
> 292
> MN89184
> 170
> U78189
> 33
> 157
> U99277
> 098
> IN14425
> 300.70
> 顾问 ZH78994 (Rank 11)
> 291
> 5W39888
> 170
> 5P89971
> 155
> 0591221
> 098
> 1413207
> 29945
> 95
> KC78191
> 290
> 95
> RP76828
> 170
> 125854
> 33
> 154
> U63604
> 098
> R890992
> 298.22
> 4569440
> 288
> YL21428
> 1.70
> D71562
> 154
> XI80376
> 098
> 5M36732
> 29791
> B148361
> 287
> C197429
> 170
> 5I65808
> 145
> Y819132
> 098
> NL28110
> 294.94
> M060428
> 287
> 98
> 4096966
> 1.69
> XS83288
> 142
> Y231130
> 098
> U38282
> 29452
> T019081
> 287
> 顾问 JC25241 (Rank 12)
> 169
> D94923
> 141
> 100
> YZ62157
> 098
> 100
> C852451
> 29382
> 100
> J10865
> 2.86
> 100
> 0/73553
> 1.69
> 100
> M518311
> 135
> Ng


### 六维龙虎榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant六维龙虎榜
> 2026-05-09
> Rank
> operatorCount
> operatorAvg
> feldCount
> fieldAvg
> communityActivity
> maxSimulationstreak
> 082626
> 322
> 116
> L00
> 6040
> 530
> 184677
> 278
> 4770
> 527
> 5P89971
> 119
> 5860
> 406
> R693974
> 327
> 180
> 5560
> 539
> 2559753
> 133
> 5850
> 540
> R890992
> 器
> 131
> 5320
> 585
> 」615244
> 135
> 5600
> 459
> D94923
> 70
> 145
> 158
> 45.90
> 363
> 5C73595
> 116
> 117
> 4950
> 555
> 10
> 丛L47973
> 60
> 241
> 88
> 119
> 52.20
> 327
> 11
> M19619
> 104
> 25
> 4230
> 547
> 425474
> 72
> 86
> 3190
> 412
> 490970
> 36
> 137
> 5320
> 381
> "
> 79256
> 82
> 91
> 4410
> 453
> 0P72475
> 29
> 5010
> 453
> 16
> RP76828
> 112
> 47
> 105
> 05
> 5010
> 410
> L39100
> 4590
> 360
> 5783096
> '23
> 157
> 6100
> 489
> 19
> N52721
> 器
> 23
> 4820
> 93
> K30147
> 36
> 4830
> 286
> K61864
> 76
> 163
> 5500
> 540
> `
> u44462
> 64
> 168
> 5500
> 741
> 丛L58442
> 167
> 4410
> 541
> 24
> 顾问 MZ45384 (Rank 51)
> 102
> 90
> 112
> 57.40
> 335
> YL66992
> 5860
> 386
> 26
> 工094100
> 96
> 58
> 159
> 4770
> 358
> J23144
> 08
> 26
> 5830
> 386
> 28
> 1X89624
> 41
> 4950
> 263
> LO40GG0
> 123
> 4410
> 556
> 0L53864
> 57
> 104
> 170
> 4410
> 570
> 171699
> 146
> 24
> 3720
> 641
> ;
> 1494963
> 118
> 3240
> 370
> L16829
> 卫
> 36
> 5320
> 566
> 1N62753
> 88
> 102
> 45.90
> 590
> 1027384
> 5500
> 255
> 36
> 413375
> 113
> 5630
> 369
> L88OGO
> 58
> 4040
> 533
> 」38399
> 108
> 151
> 5740
> 400
> P511956
> 58
> 119
> 4680
> 373
> 40
> 1053797
> 62
> 154
> 6040
> 310
> AMUGO5Og
> 351
> 5320
> 335
> NS77148
> 241
> 82
> 111
> 5320
> 579
> 嚣
> 8636120
> 髫
> 4230
> 365
> u21812
> 105
> 75
> 51.40
> 813
> B451127
> 116
> 5920
> 634
> 46
> CX60157
> 108
> 2220
> 372
> J15679
> 114
> 5500
> 468
> 029269
> 111
> 79
> 4410
> 613
> N32626
> 105
> 4770
> 576
> 50
> XZ69776
> 108
> 4670
> 453
> 4551256
> 94
> 130
> 42.30
> 453
> IL75459
> 4.25
> 101
> 102
> 4230
> 279
> L89289
> 103
> 136
> 56.20
> 454
> 54
> ZV96737
> 55
> 112
> 1.17
> 38.60
> 438
> 55
> 丛97497
> 104
> 191
> 5320
> 742
> 56
> ZY36280
> 4.25
> 135
> 55.80
> 387
> 1/18421
> 59
> 153
> 6040
> 353
> 58
> XCG6172
> 59
> 151
> 4830
> 436
> 433503
> 56
> 372
> 121
> 4830
> 465
> 60
> XZ81923
> 36
> 100
> 1.18
> 43.90
> 421
> 顾问 ZH78994 (Rank 11)
> 36
> 5770
> 148
> 1637773
> 06
> 1
> 102
> 5500
> 481
> SW42429
> 104
> 1.00
> 3860
> K255390
> 381
> 103
> 4770
> 盥
> 顾问 WX64154 (Rank 32)
> 124
> 5370
> J16510
> 150
> 4770
> 593
> 顾问 CT48231 (Rank 2)
> 留
> 鹨
> 嚣
> 40
> 4690
> 242
> GM54012
> 1.78
> 4230
> 335
> 顾问 NL80893 (Rank 16)
> 115
> 5770
> 360
> 70
> 5081732
> 1.74
> 50.40
> 419
> 4C78364
> 器
> 58
> 99
> 110
> 4130
> 293
> 1y85808
> 13
> 77
> 1.24
> 40.40
> 427
> 7
> 0N16452
> 105
> 195
> 204
> 5040
> 587
> 74
> 5C77987
> 4.25
> 181
> 157
> 61.00
> 252
> 1433235
> 138
> 4590
> 595
> 75
> P23235
> 58
> 112
> 43.60
> 170
> J96079
> 86
> 06
> 114
> 138
> 3680
> 344
> 78
> 8W28426
> 26
> 90
> 131
> 73.70
> 413
> 顾问 LW67640 (Rank 24)
> 52
> 447
> 106
> 52.10
> 531
> 80
> YX37105
> 133
> 153
> 4770
> 207
> 4041126
> 120
> 200
> 4780
> 507
> 顾问 YX23928 (Rank 8)
> 38
> 00
> 94
> 1.26
> 58.60
> 522
> 835905
> 22
> 4370
> 327
> H62464
> 86
> 1.75
> 4410
> 4555260
> 105
> 5140
> 484
> 顾问 YL20193 (Rank 37)
> 翳
> 123
> 58.60
> 480
> V58435
> 100
> 4040
> 427
> MO62208
> 
> 65
> 1.56
> 4770
> 538
> 659154
> 416
> 142
> 5860
> 334
> 8N67375
> 104
> 84
> 181
> 56.50
> 369
> HE56620
> 107
> 197
> 51.00
> 433
> T21691
> 107
> 126
> 3680
> 362
> 5W82574
> 129
> 197
> 42.80
> 362
> 」79797
> 475
> 175
> 1.75
> 55.60
> 400
> 492336
> 194
> 4770
> 349
> D64461
> 105
> 438
> 121
> 183
> 3860
> 674
> 1L49894
> 363
> 146
> 147
> 2650
> 307
> SIGS8O8
> 457
> 136
> 153
> 3500
> 542
> 465370
> 374
> 117
> 140
> 5660
> 310
> 100
> 4095618
> 295
> 1.24
> 38.60
> 371


### 国区双榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant顾问龙虎榜 (围区)
> 2026-05-09
> Max VF
> Max WF
> Max Combine
> Max
> Combine
> Max Pyramid
> Rank
> VF
> Rank
> VF
> Rank
> CM
> Rank
> AVG
> Rank
> PYR
> AL
> E65210
> L00
> 卫33369
> 97825
> 174218
> 694
> 174218
> 383
> 79797
> 55
> 163
> 」87757
> 100
> 4269256
> 23367
> 0C68819
> 603
> 山37372
> 299
> 山52291
> 52
> 1566
> U062208
> L00
> 116829
> 18069
> L71036
> 573
> 4569440
> 288
> J39934
> 51
> 181
> 5017531
> 100
> K79256
> 13717
> ZE97721
> 541
> 1640486
> 284
> 5783096
> 51
> 157
> KX88140
> L00
> 0429412
> 13348
> JR15410
> 507
> Y11344
> 282
> 122447
> 45
> 189
> X56645
> 100
> L71699
> 12929
> 1640486
> 505
> X221889
> 278
> 1022811
> 171
> X25924
> L00
> L79055
> 12788
> L15616
> 488
> 0C68819
> 264
> 0H19310
> 45
> 183
> V81852
> 100
> 0068782
> 12500
> 411344
> 488
> E91858
> 260
> X54051
> 179
> y72634
> L00
> WY56787
> 12416
> 」16243
> 486
> 5224058
> 249
> 417279
> 134
> UL28382
> 100
> 10
> F69320
> 12157
> 10
> E15829
> 473
> 丘28881
> 236
> 422845
> 189
> YL9GOGB
> 100
> 卫53723
> 12109
> CZ67480
> 444
> ZV96737
> 231
> 」42868
> :
> 170
> C186067
> 099
> ZM43612
> 11916
> 0L32665
> 436
> 138399
> 229
> 2H34713
> 162
> 
> CX60157
> 099
> 13
> 5C13445
> 11907
> 止55914
> 436
> M12075
> 227
> 13
> 5C23342
> 129
> 0Y13559
> 099
> 188060
> 11733
> 14
> ML42552
> 419
> 1X81181
> 225
> 14
> Y25030
> 153
> 445023
> 099
> Y93864
> 11210
> 」38399
> 403
> J37401
> 221
> }78449
> 151
> J062872
> 099
> 16
> 2135633
> 11108
> 16
> 0129942
> 390
> 163377
> 221
> 16
> 4643324
> 145
> 17
> 184394
> 099
> 116510
> 10211
> ZC2G0BO
> 366
> YC76553
> 221
> JSOOO5
> 40
> 131
> 18
> 1015326
> 099
> 18
> 4433574
> 10134
> 18
> E39657
> 352
> LL90629
> 219
> 18
> 032536
> 181
> Ly85808
> 099
> 0231817
> 9189
> ZV96737
> 348
> &22438
> 215
> E60707
> 156
> 056787
> 099
> 20
> XM75236
> 83.21
> 20
> 1280024
> 347
> 20
> Y78429
> 211
> 20
> 」89289
> 156
> 0K32246
> 099
> SW48878
> 7114
> C215695
> 341
> X54051
> 209
> K79256
> 147
> "
> WP88606
> 099
> P64174
> 69.88
> 1L90629
> 340
> ZF97721
> 206
> 孟
> 2C54526
> 174
> 118521
> 099
> Y262157
> 6911
> Y89646
> 339
> 170892
> 203
> ZR94671
> 165
> XD81759
> 099
> 24
> 8451127
> 6866
> 24
> 163377
> 337
> 24
> 0L32665
> 203
> 24
> 1015326
> 163
> YL42885
> 099
> SIGI3GO
> 5836
> YH78429
> 331
> 5284537
> 202
> 25
> 1033850
> 160
> 26
> W22772
> 099
> 26
> 417279
> 66,27
> 26
> 622438
> 321
> 26
> 4066932
> 201
> 26
> 0014840
> 159
> Y82997
> 099
> 0y83769
> 5479
> 165774
> 320
> 27
> XS34596
> 201
> 4G88592
> 141
> ]
> 2H71971
> 099
> 28
> XZ23611
> 63.79
> 28
> 1U53797
> 318
> 7135633
> 28
> 7559763
> 139
> ZX59531
> 099
> 5C84371
> 5307
> X83124
> 316
> YC99371
> 197
> N19619
> 137
> 2Y77039
> 099
> 30
> 420306
> 6277
> 30
> U63604
> 311
> AC60527
> 197
> 30
> 0X52484
> 133
> 30
> ZZ40911
> 099
> J71859
> 5192
> YL81551
> 311
> 4P65370
> 197
> Y262807
> 37
> 171
> E639655
> 098
> 181819
> 59.24
> X221889
> 310
> 32
> Y296589
> 192
> {67304
> 37
> 164
> 3
> 147083
> 098
> 5L10033
> 5787
> 33
> 5224058
> 309
> HE76003
> 192
> 33
> J23144
> 37
> 145
> 34
> 」81222
> 098
> 34
> XD81759
> 5717
> 34
> 412075
> 307
> CY59336
> 190
> 34
> L67640
> 37
> 135
> 140932
> 098
> 169468
> 5712
> ZH74761
> 306
> 35
> YIO136
> 188
> 469256
> 37
> 134
> 36
> 卫26750
> 098
> 36
> 卫25631
> 5703
> 36
> 0y13559
> 304
> 36
> CM97448
> 36
> XU75236
> 37
> 133
> 0068782
> 098
> 1444620
> 56O6
> 丛7372_299
> 卫10343
> 187
> L71699
> 171
> 38
> 业63604
> 098
> 38
> 149592
> 5573
> 38
> 7710277
> 299
> 1299035
> 86
> 38
> XG98059
> 163
> XI80376
> 098
> 39
> 4G88592
> 5451
> 465370
> 298
> 丛80893
> 185
> J61289
> 154
> 1231130
> 098
> 40
> 0462432
> 5407
> 40
> ZH41150
> 298
> 业63604
> 184
> [D69320
> 147
> 40
> Y262157
> 098
> W84677
> 5362
> 420306
> 295
> 40
> YP74336
> 83
> w
> U81055
> 131
> 42
> 2590407
> 098
> 23928
> 5355
> 」79797
> 294
> W548176
> 182
> Y23928
> 130
> ZZ44620
> 098
> 4017963
> 5317
> K79256
> 293
> 457211
> 181
> 4092395
> 121
> 44
> 8592559
> 097
> 44
> 5017531
> 5297
> 44
> 5784537
> 292
> 44
> 174499
> 44
> 4L45135
> 35
> 160
> 140454
> 097
> 45
> X42289
> 5250
> 4569440
> 288
> ZX24677
> 179
> XZ69776
> 35
> 158
> 46
> 114975
> 097
> 46
> 444931
> 4806
> 46
> 848361
> 287
> 5I61360
> 179
> 46
> 1053797
> 149
> J80916
> 097
> 47
> C089422
> 4743
> W66806
> 283
> 190400
> 178
> 47
> ZV96737
> 35
> 148
> 48
> 1013454
> 097
> 48
> ZL29184
> 4646
> 48
> I88765
> 283
> 凹47019
> 178
> 48
> 4565681
> 35
> 139
> WE80243
> 097
> Z210277
> 4622
> Y084572
> 282
> 161351
> 177
> B28426
> 35
> 129
> 50
> 0429412
> 097
> 50
> 8L20996
> 4537
> 50
> Y288594
> 282
> 50
> XM19402
> 177
> 50
> ZZ55695
> 124
> W055029
> 097
> KD86036
> 4465
> 顾问 NL80893 (Rank 16)
> 281
> 1015326
> 177
> YZ88594
> 114
> WP52250
> 097
> 52
> CZ10093
> 44.20
> 52
> WX18521
> 281
> 52
> 4F78592
> 176
> 52
> PW58059
> 162
> 53
> WZ47295
> 097
> 53
> RP76828
> 4411
> 53
> Y93864
> 281
> YC99622
> 176
> 53
> J16084
> 149
> 54
> XL48428
> 097
> 54
> 顾问 LW67640 (Rank 24)
> 43.70
> 54
> MH33969
> 280
> CL56494
> 1.75
> 54
> 顾问 WX84677 (Rank 69)
> 144
> 55
> YD42421
> 097
> 55
> ML42552
> 4352
> 55
> 顾问 FD69320 (Rank 34)
> 278
> 55
> 顾问 YX23928 (Rank 8)
> 175
> 55
> XH77948
> 137
> 56
> YH87796
> 097
> 56
> J44290
> 43.07
> 56
> 1022811
> 272
> 56
> EL15829
> 175
> 56
> 顾问 MS51256 (Rank 28)
> 127
> C86846
> 096
> FP65798
> 4298
> 57
> ZH71971
> 272
> 57
> L053797
> 175
> 2147333
> 
> 121
> 58
> 0498440
> 096
> 58
> N19619
> 41.71
> 58
> 2H87224
> 271
> u60830
> 1.74
> 58
> 顾问 WX64154 (Rank 32)
> 107
> 59
> 032665
> 096
> 59
> 111546
> 4127
> 010343
> 270
> 顾问 YH25030 (Rank 31)
> 174
> 59
> 2053542
> 191
> 60
> GL98521
> 096
> 60
> YB49779
> 41.01
> JL80gOO
> 269
> 60
> PC73872
> 173
> 60
> U474101
> 177
> 5R857579
> 096
> CC21336
> 4082
> IL53163
> 268
> C521130
> 173
> U78189
> 157
> 420306
> 096
> 184152
> 40.28
> B59154
> 267
> 5283096
> 1733
> 1225854
> 154
> J023670
> 096
> 0P72475
> 4006
> 顾问 顾问 RM49262 (Rank 30) (Rank 30)
> 267
> D86385
> 172
> 5I65808
> 145
> J15679
> 096
> PW58059
> 39.89
> CC67505
> 264
> CX98570
> 1.71
> XS83288
> 142
> 」31069
> 096
> ILIOgOS
> 3955
> 125854
> 264
> 65
> 4220306
> 171
> 4248623
> 134
> LY52969
> 096
> 5081732
> 39.44
> Z135633
> 264
> K79256
> 171
> 丛80893
> 132
> 0W94165
> 096
> YL21428
> 3932
> 顾问 JR23144 (Rank 6)
> 263
> P32594
> 170
> 0P72475
> 33
> 126
> 0267721
> 096
> 68
> EL94401
> 38.96
> 116510
> 262
> 5W39888
> 170
> 68
> EL39657
> 33
> 124
> 5C23342
> 096
> ZX58901
> 3872
> CL56494
> 261
> RP76828
> 170
> 0068782
> 121
> 70
> 5014148
> 096
> 70
> 458883
> 38.49
> 70
> FN91858
> 260
> YL21428
> 170
> 70
> 484915
> 116
> 71
> W529639
> 096
> CL49716
> 3806
> 4248623
> 260
> C197429
> 170
> 1687838
> 115
> 7
> XL71350
> 096
> 72
> 1L87164
> 3795
> 72
> 顾问 LW67640 (Rank 24)
> 260
> 73
> 0173553
> 1.69
> #
> 0210943
> 33
> 114
> YH78429
> 096
> 73
> FL11741
> 3774
> 73
> X37939
> 260
> YZ88594
> 169
> 工21691
> 113
> 74
> Y051506
> 096
> 74
> IL42173
> 37.45
> 74
> 1033850
> 259
> 118421
> 1.68
> 74
> 1L49894
> 147
> 75
> YZ59361
> 096
> 75
> YC99622
> 3730
> 75
> 0L47372
> 258
> 0068782
> 167
> 75
> J51810
> 32
> 144
> 76
> 2559763
> 096
> 76
> 0T40395
> 36.88
> 76
> W18906_258
> 76
> C767480
> 167
> 163377
> 32
> 136
> 77
> DIG6970
> 095
> XP21100
> 3590
> 77
> YD77867
> 258
> CM59456
> 166
> 充
> 035234
> 32
> 132
> 78
> E39657
> 095
> 78
> YXI5005
> 35.61
> 78
> 顾问 YH25030 (Rank 31)
> 256
> J23144
> 1.66
> 78
> 4113375
> 128
> J78363
> 095
> 79
> 0y12692
> 3547
> 79
> B110003
> 255
> KC82433
> 166
> 79
> 5W34207
> 32
> 128
> 80
> 1087845
> 095
> 0Y27687
> 35.36
> 5017531
> 255
> 80
> 1022811
> 1.64
> 80
> XL98962
> 31
> 184
> LL81909
> 095
> BU28426
> 3423
> 161351
> 254
> H40076
> 163
> 2487224
> 31
> 138
> 1R93609
> 095
> XY56645
> 3347
> 578592
> 253
> 2242824
> 163
> 82
> XZ81923
> 135
> LW93678
> 095
> 5610230
> 3300
> 4583704
> 253
> 83
> E69320
> 163
> GW98315
> 31
> 134
> MY51598
> 095
> 5J65808
> 3292
> W26072
> 252
> 4699972
> 1.62
> 1W93678
> 134
> P16638
> 095
> 顾问 YH25030 (Rank 31)
> 3209
> 4457211
> 248
> 85
> 116510
> 160
> 乙Z74958
> 130
> XC47437
> 095
> 1494963
> 3207
> J96397
> 248
> XS80591
> 159
> CC21336
> 122
> XX42289
> 095
> 山L27618
> 3177
> WX81181
> 247
> 2H87224
> 159
> ZZ51745
> :
> 121
> Y282897
> 095
> 4533387
> 31.77
> 0J97429
> 2.46
> X37939
> 158
> ML42357
> 110
> YZ88594
> 095
> 4632717
> 3154
> 5I65808
> 246
> X17517
> 157
> NU28753
> ZC26080
> 095
> 082427
> 3097
> UL58980
> 246
> XX42289
> 157
> 」29779
> 158
> ZX24677
> 095
> YS95353
> 3068
> 0X52484
> 245
> Y084572
> 156
> U63604
> 145
> 4M12075
> 094
> 140454
> 30.40
> 139823
> 244
> 0H68852
> 156
> CN26548
> 144
> EC34030
> 5Z83096
> 3027
> 顾问 MS51256 (Rank 28)
> 241
> QL50450
> 156
> C695788
> 136
> H65370
> 094
> Y286931
> 30.09
> 5783096
> 241
> 0688592
> 1.55
> YL28729
> 132
> 120282
> 094
> WP77813
> 3006
> EX25214
> 240
> 95
> 651368
> 1.54
> 1479055
> 123
> 」61289
> 094
> F60707
> 2979
> 4Y17279
> 239
> 656831
> 1.54
> ?656831
> 117
> 」74499
> 094
> 024362
> 2977
> C521130
> 239
> 乙I81809
> 1.54
> AM12075
> 115
> MS70058
> 094
> CL88457
> 2948
> 433503
> 239
> HC66282
> 1.53
> U29742
> W424469
> 094
> W424469
> 2928
> 5C84371
> 239
> 4248623
> 153
> YT52851
> 149
> 100
> XCgGOOO
> 0.94
> 100
> YX50OO5
> 29.01
> 100
> 1y85808
> 238
> 100
> 1031804
> 1.52
> 100
> [78468
> 29
> 134
> Nvg


### 
> [!NOTE] [图片 OCR 识别内容]
> WorldQuantx维龙虎榜
> 国区)
> 2026-05-09
> Rank
> operatorCount
> operatorAvg
> feldCount
> fieldAvg
> communityActivity
> maxsimulationstreak
> 184677
> 278
> L00
> 4770
> 527
> 189624
> 311
> 4950
> 263
> 425474
> 3190
> 1027384
> 詈
> 5500
> 25
> L9100
> 4590
> 1615244
> 321
> 335
> 5600
> 山L47973
> 241
> 119
> 5220
> 2559763
> 393
> 133
> 5850
> 10
> N596s
> 95
> 85
> 104
> 38
> 129
> 4230
> 
> 11
> 0P72475
> 5010
> RP76828
> 112
> 447
> 05
> 6010
> K79256
> 4410
> %
> 188060
> 3
> 40.40
> 533
> 4L13375
> 113
> 38
> 6630
> 369
> 16
> 4745384
> 102
> 07
> 112
> 57.40
> 335
> J15679
> 114
> 5500
> 468
> 18
> 1637773
> 36
> 55.00
> 19
> YL66992
> 38
> 5860
> 386
> 171599
> 95
> 146
> 24
> 3720
> 641
> CX60157
> 108
> 08
> 2220
> 372
> "
> 2196737
> 81
> 112
> 117
> 3860
> 438
> 1494963
> 347
> 118
> 29
> 32.40
> 370
> J823144
> 421
> 108
> 26
> 5830
> 386
> 1517092
> 63
> 56
> 00
> 5680
> 243
> 丛80893
> 50
> 94
> 5770
> 360
> 鲨
> 5W42429
> 104
> 00
> 3860
> 254
> 山33503
> 72
> 121
> 4830
> 465
> 116829
> 374
> 盈
> 36
> 5320
> 566
> X281923
> 36
> 93
> 118
> 4390
> 
> 顾问 LY85808 (Rank 86)
> 124
> 4040
> 龆
> 」38399
> 108
> 151
> 5740
> 4551256
> 92
> 30
> 4230
> 453
> 34
> 5783096
> 59
> 423
> 器
> 157
> 6100
> 489
> L16510
> 44
> S0
> 4770
> 593
> 36
> P511956
> 52
> 58
> 4680
> 373
> XCGG172
> 58
> 59
> 99
> 151
> 4830
> 436
> XZ69776
> 410
> 108
> 137
> 4670
> 453
> 5081732
> 35
> 174
> 6040
> Y23928
> 4
> 26
> 5860
> 盥
> 4555260
> 05
> 5140
> 0695788
> 66
> 90
> 00
> 40.40
> 336
> "
> Zy36280
> 425
> 35
> 5580
> 387
> U18421
> 59
> 153
> 6040
> 353
> 189289
> 29
> 103
> 36
> 56.20
> 454
> 1U53797
> 62
> 60.40
> 310
> 45
> B28426
> 26
> 90
> 131
> 7370
> 413
> X85841
> 
> 43
> 56
> 113
> 4770
> 463
> B451127
> 418
> 116
> 5920
> 534
> 50
> M062208
> 65
> 56
> 4770
> 538
> K22438
> 430
> 75
> 00
> 3780
> 170
> 52
> K255390
> 371
> 103
> 47.70
> 353
> 465370
> 374
> 117
> 40
> 56G0
> 310
> 54
> 顾问 WX64154 (Rank 32)
> 87
> 60
> 53.70
> 311
> 55
> 659154
> 184
> 42
> 5860
> 56
> C163008
> 27
> 312
> 63
> 00
> 3680
> 鹬
> RJ74200
> 59
> 5860
> 58
> 064268
> 319
> 1.12
> 24.10
> p490725
> 93
> 123
> 5320
> 339
> 60
> 4518471
> 00
> 36.80
> 316
> LC34491
> 4.20
> 00
> 1680
> 210
> ZY88181
> 4.24
> 嚣
> 121
> 4650
> 367
> 885606
> 150
> 101
> 4770
> IL10905
> 334
> 93
> 58.60
> 2
> YX37105
> 153
> 4770
> CR35762
> 3.79
> "
> 07
> 51.40
> 369
> NL80034
> 443
> 00
> 2670
> 170
> ZC54526
> 116
> 55.00
> LL49894
> 146
> 147
> 2650
> 300
> 5C77987
> 4.25
> 181
> 157
> 61.00
> 70
> 顾问 LW67640 (Rank 24)
> 62
> 447
> 106
> 62.10
> [21691
> 107
> 416
> 126
> 36.80
> 蛋
> 5220589
> 125
> 152
> 28.70
> "
> FZ607OZ
> 120
> 392
> 115
> 68.20
> HE56620
> 107
> 97
> 51.00
> 433
> 0L47372
> 3.21
> 85
> 30
> 49.50
> 167
> E581271
> 377
> 162
> 31.40
> 350
> 78
> WL33473
> 50
> 87
> 111
> 40.40
> 359
> 5017531
> 嚣
> 152
> 5680
> 516
> 80
> ML74437
> 85
> 1.19
> 56.80
> 268
> C462432
> 87
> 123
> 39.20
> 412
> 0C90573
> 10
> 1.16
> 4410
> 285
> M78189
> 391
> 59
> 3500
> 277
> 0y49971
> 452
> 116
> 147
> 31.40
> 536
> 5I65808
> 82
> 457
> 136
> 153
> 3500
> 542
> E39657
> 82
> 3.78
> 134
> 51.40
> 137
> CX43424
> 315
> 09
> 1860
> 469256
> 459
> 147
> 50.40
> 652
> 」39934
> 415
> 154
> 5740
> 310
> GM92689
> 440
> 104
> 31.40
> 255
> 顾问 YH25030 (Rank 31)
> 442
> 
> 1.14
> 5010
> 430
> 0548533
> 333
> 97
> 2950
> 448
> YE22412
> 435
> 00
> 2040
> 158
> 0068782
> 56.80
> 382
> 0y13559
> 45
> 106
> 4770
> 231
> V22772
> 1.16
> 35.00
> 6H93979
> 427
> 58
> 100
> 2230
> 348
> 5C23342
> 93
> 3.85
> 223
> 4410
> 344
> DC11087
> 29
> 10
> 102
> 2410
> 193
> 100
> J454866
> 4.28
> 1.38
> 56.80
> 258
> 93
> 59


### Genius龙虎榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant genius
> 龙虎榜
> 2026-05-09
> Vedl
> patorCount
> fieldCount
> fieldAvg
> 5P89971
> 5850
> RR90992
> DKq4923
> NII19619
> 4y90970
> _0P72475
> 6100
> 顾问 TD94100 (Rank 7)
> 4770
> 1171699
> R636120
> XZ69776
> 4670
> 11189289
> 71/96737
> 1X64154
> 丛L80893
> 5040
> 81128426
> 1167640
> 62.10
> 492336
> 4770
> 5165303
> M813430
> 4040
> E6070
> 68.20
> 5500
> 4Y17279
> 4230
> 山41060
> 51.40
> 005373?
> 139934
> 刀/71562
> 4748623
> W478189
> OTSG4S?
> 7437221
> 3800
> 4040
> 137333
> 174024
> YL28729
> 2770
> 5860
> 5500
> 5920
> P054914
> N4G88592
> 8M1207
> N430407
> 4025387
> 46.50
> 2360
> 3380
> 顾问 FD69320 (Rank 34)
> 1015326
> 0045758
> 4290
> 5860
> 14/090077
> 4590
> 33.20
> 419328
> V4182621
> 49.50
> 顾问 ML47973 (Rank 100)
> 425474
> 31.90
> 60.10
> 115
> 11739100
> 顾问 KU30147 (Rank 55)
> 48.30
> 1
> NIICOA4?
> YL66992
> UX89624
> 15
> 53.2C
> Expert
> 55.00
> 40.40
> 205
> AMGOSOC
> 1
> 8451127
> 5500
> NT29269
> 顾问 NT32626 (Rank 80)
> Expert
> TL75459
> WY18421
> 60.40
> 4830
> 4830
> 剀33903
> 1637773
> 51I42429
> 47.70
> J16510
> Expert
> 26
> 60.40
> 40.40
> 5077937
> Expert
> 1433235
> Expert
> PT23235
> 16roilos
> 437C
> 4410
> 159
> 58G0
> 4040
> M06220E
> 163
> Expert
> FE56620
> 61.00
> HPE5370
> RI74200
> 5220589
> 28.70
> RH95743
> KP22438
> 顾问 VC95113 (Rank 58)
> 159
> Expert
> 1569925
> WC45s9
> 29
> 53.20
> Expert
> 4770
> 4H36812
> 184
> 0I90254
> 563C
> 164268
> C011207
> 4410
> 顾问 BM29781 (Rank 92)
> 4090
> 1135107
> R643820
> ZY88181
> HL26425
> 193
> YC48839
> TTI0055
> SM14025
> 5680
> 5017531
> 1
> 285
> Expert
> 48.00
> 4518471
> 203
> 61139014
> 0H62432
> KK76363
> 20
> 1061241
> 1070351
> 2770
> 401713559
> Expert
> 1C3449
> Expert
> 215
> 4026378
> 5680
> 36.8C
> 0Y62952
> 4230
> F4763
> 2470
> 219
> 5G 80
> 220
> XN13612
> 8N74418
> 222
> Expert
> 1480116
> 4770
> I7F306
> Expert
> 1X14975
> Expert
> TT91159
> 60.40
> 20 _岢56219
> BU14163
> 59.20
> 丛33473
> 40.40
> '
> DLI034
> Expert
> MF8384?
> 2
> UL58980
> 顾问 顾问 RM49262 (Rank 30) (Rank 30)
> 4230
> 04162372
> 5190
> FL11088
> 24
> 18.60
> 5860
> 248
> XNI23590
> Expert
> J871859
> 2
> 60.40
> VP879
> 40.40
> 0127687
> 56 30
> T72336
> 4290
> 29
> 0Y77844
> 1654887
> [25214
> 35.00
> 263
> N22772
> 0L50548
> 1087845
> 5490
> 266Is9so
> 158
> 38.60
> _0N41247
> 4230
> WP88GOE
> 40.40
> H179344
> YI8165
> 2H39644
> 45.90
> z
> TN10210
> 33.20
> 5P61833
> Expert
> 4410
> 40.40
> 7
> FI39510
> 306
> (750647
> 28.30
> ?
> VC26243
> 36.80
> 53.20
> MC4TOOF
> 4N30280
> Expert
> 1548176
> 289
> 8J10003
> 2040
> P64174
> 2230
> 2950
> 4720
> 296
> Expert
> RP40432
> Expert
> (523323
> Expert
> 5M58724
> _248
> 盗
> YL50102
> 556
> 3860
> 貂
> NH16784
> 3910
> MY21251
> 35.00
> MFS9400
> 55.00
> 035234
> 61128303
> Expert
> 4930
> KI 75220
> PN88168
> W494369
> Expert
> 31
> OI 7127C
> [639655
> 8H48458
> 3860
> 翌
> SM18051
> 3490
> MC44186
> Expert
> KP26017
> HI1584
> 」615244
> Expert
> Expert
> _ML74437
> Expert
> Expert
> Expert
> Expert
> Expert


潮起潮落，此卷暂且封存。

然庙堂之下，江湖之远，暗涌从未止息——昔有隐世GM，于VF九八之境摘金万八有余；今携满值而归，锋芒更盛。

此番季赏，是扶摇直上，再破云霄？

还是天道有衡，另藏玄机？

龙战于野，其血玄黄，待到时日， **卷三** 再会！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享，看这段开头的文字感觉不像是在看WQ论坛，而是在看武侠小说哈哈

=============================================================================


---

### 技术对话片段 158 (原帖: 【龙虎榜·卷二】Combine惊雷再起，VF季决尘埃落定，神秘GM满值归来，万刀之上几何？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【龙虎榜卷二】Combine惊雷再起VF季决尘埃落定神秘GM满值归来万刀之上几何_40347330265879.md
- **时间**: 24天前

**提问/主帖背景 (AL13375)**:
### 山河震荡，榜动九州。

昨日 **Combine** 异动方歇，今朝惊雷又至；VF季决终章落笔，有人封侯拜相，有人黯然离场。

今日鹿死谁手，且看谁夺虎符，谁占龙庭！

### 顾问龙虎榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant顾问龙虎榜
> 2026-05-09
> Max VF
> Max WF
> Max Combine
> Max
> Combine
> Max Pyramid
> Rank
> VF
> Rank
> l0
> VF
> Rank
> CM
> Rank
> AVG
> Rank
> PYR
> AL
> 丛48527
> L00
> 019316
> 177143
> 460270
> 117
> 174218
> 383
> 159893
> 191
> 0123443
> 100
> 丛82709
> 136323
> 1074218
> 594
> 山60270
> 346
> 丛76363
> 57
> 172
> 卫B89987
> L00
> 丛78692
> 132765
> R41479
> 669
> U772
> 299
> J79797
> 55
> 163
> )65210
> 100
> 038384
> 117086
> 0C68819
> 603
> 4569440
> 288
> 山52291
> 52
> 1566
> 6581389
> L00
> VP76790
> 107337
> W74107
> 601
> 087152
> 286
> 139934
> 51
> 181
> 187757
> 100
> 0053160
> 106350
> 087152
> 586
> 1640486
> 284
> 5283096
> 157
> 1480116
> L00
> R570387
> 104971
> L71036
> 573
> Y11344
> 282
> R588503
> 5
> 182
> MC61836
> 100
> 8233369
> 978.25
> 5V78590
> 566
> X221889
> 278
> 」022447
> 45
> 189
> WC63274
> L00
> 5824011
> 95169
> 2F97721
> 541
> LN566Z5
> 278
> 1022811
> 45
> 171
> 10
> W062208
> 100
> 10
> 065624
> 94664
> 10
> Y816410
> 507
> 10
> 0C68819
> 264
> 10
> 644463
> 44
> 187
> 5017531
> 100
> P55616
> 92697
> 1640486
> 505
> EN91858
> 260
> 456452
> 169
> SM18051
> 100
> NP19911
> 90286
> 0C29779
> 491
> 」10865
> 256
> 490970
> 4
> 151
> 5N68553
> 100
> IN41467
> 80712
> 0692378
> 489
> 5224058
> 249
> 0419310
> 183
> 14
> J91272
> 100
> 0N69057
> 78655
> 14
> U15616
> 488
> 5864976
> 2.48
> X54051
> 179
> XX88140
> 100
> V87972
> 59249
> y11344
> 488
> 15
> 4047730
> 242
> 492336
> 42
> 170
> 16
> XY56645
> 100
> 16
> N823017
> 57531
> 16
> GK78216
> 486
> N067211
> 238
> 16
> 844462
> 158
> X25924
> 100
> 4652134
> 56630
> 」16243
> 486
> E28881
> 236
> 17
> 417279
> 134
> 18
> Y81852
> 100
> 18
> 0N14408
> 66292
> 18
> VP87972
> 481
> 2V96737
> 231
> 18
> 422845
> 41
> 189
> y72634
> 100
> 工051363
> 56206
> E15829
> 473
> W74107
> 231
> 4595259
> 41
> 185
> 20
> VL28382
> 100
> 20
> SK72105
> 655.67
> 20
> P514747
> 472
> 20
> YC29686
> 229
> 20
> 442868
> 41
> 170
> YL9GOGB
> 100
> 卫36426
> 54475
> 5R35346
> 454
> 」38399
> 229
> 2434713
> 41
> 162
> 22
> 4597533
> 099
> N72745
> 62238
> 5073114
> 451
> M12075
> 227
> 5C23342
> 129
> 0H65852
> 099
> 023095
> 57937
> CZ67480
> 444
> 23
> 山61722
> 225
> W25030
> 153
> C186067
> 099
> 24
> 445359
> 57910
> 24
> 4466051
> 441
> 24
> WX81181
> 225
> 24
> 8L78449
> 151
> CIGO525
> 099
> D64455
> 57617
> 425519
> 440
> 25
> LX77gOI
> 224
> 4643324
> 40
> 145
> ;
> CX60157
> 099
> 26
> 8U17144
> 57124
> 26
> 0P93973
> 439
> 26
> J37401
> 221
> 26
> YX50005
> 131
> 0024306
> 099
> 卫97630
> 56442
> 卫32665
> 436
> 27
> 163377
> 221
> K77697
> 115
> 0577651
> 099
> 28
> U25385
> 56280
> 28
> 止55914
> 436
> 28
> YC76553
> 221
> 28
> 232536
> 181
> 013559
> 099
> 29
> 0065284
> 55801
> U48957
> 433
> 1L90629
> 219
> 卫054914
> 175
> 30
> H61566
> 099
> MB13430
> 55546
> 30
> ML42552
> 419
> 622438
> 215
> 30
> E60707
> 156
> 412949
> 099
> 1084732
> 55118
> NT98018
> 419
> Y78429
> 211
> L89289
> 156
> 445023
> 099
> 0N13413
> 53131
> 4047730
> 416
> XY54051
> 209
> T094100
> 152
> 32
> J62872
> 099
> IN75488
> 51806
> D64455
> 415
> ZE97721
> 206
> 8693974
> 150
> 34
> 184394
> 099
> 34
> NB63040
> 50977
> 34
> E17513
> 413
> !70892
> 203
> 34
> 79256
> 147
> 1015326
> 099
> 454882
> 50289
> IN84689
> 411
> 35
> 卫32665
> 203
> 5535873
> 132
> 36
> 1471010
> 099
> 36
> N896944
> 47395
> 36
> NN39972
> 410
> 36
> 5784537
> 202
> 36
> 丛61864
> 117
> 丛33773
> 099
> 4025992
> 47075
> 37
> 丛N89184
> 409
> 37
> 顾问 ZH78994 (Rank 11)
> 202
> 卫078486
> 117
> 1584247
> 099
> 38
> 0N98774
> 46047
> 38
> 067350
> 408
> 4066932
> 201
> 38
> 2C54526
> 174
> Ly85808
> 099
> IN52580
> 45893
> 」38399
> 403
> XS34596
> 201
> ZR94671
> 165
> 0Y56787
> 099
> 40
> T079250
> 45808
> 40
> VS91693
> 395
> Z018587
> 199
> 40
> 1015326
> 163
> N63388
> 099
> N63388
> 45263
> 41
> 029942
> 390
> Z135633
> 199
> 1033850
> 160
> "
> 0K32246
> 415591
> 44464
> 0428368
> 386
> P514747
> 198
> 0014840
> 159
> 丛48711
> 099
> N023388
> 44215
> 卫054914
> 382
> YC99371
> 197
> L74024
> 142
> RS73796
> 099
> 44
> 4815407
> 43841
> 44
> 必57672
> 370
> 4C60527
> 197
> 44
> 顾问 MG88592 (Rank 38)
> 141
> SKI4418
> 099
> 5N36193
> 43735
> CK70116
> 368
> 45
> 465370
> 197
> 2559763
> 139
> 46
> 5073114
> 099
> 46
> 4433535
> 43563
> 46
> NN67211
> 367
> 46
> V415439
> 192
> 46
> N19619
> 137
> IL73802
> 099
> 丛453550
> 42601
> U54006
> 366
> 47
> Y296589
> 192
> J96079
> 135
> 48
> 工530457
> 099
> 48
> 0P93973
> 41694
> 48
> ZC26080
> 366
> E76003
> 192
> 48
> 0X52484
> 133
> T72336
> 099
> ID21847
> 41547
> Sk84434
> 355
> 059336
> 190
> D29715
> 102
> 50
> J61722
> 099
> 50
> 工057923
> 41058
> 50
> 4075156
> 354
> 50
> Y82626
> 190
> 50
> 1262807
> 37
> 171
> 1591693
> 0.99
> IL11G8O
> 408.20
> 4121336
> 353
> 061316
> 190
> EX67304
> 37
> 164
> WP88606
> 099
> IN14420
> 40402
> 52
> E39657
> 352
> 52
> 4R44095
> 1.89
> 52
> 顾问 JR23144 (Rank 6)
> 37
> 145
> 53
> WX18521
> 099
> 53
> 1438752
> 401.64
> 53
> ZV96737
> 348
> YIIO136
> 188
> 53
> MB13430
> 37
> 137
> 54
> XD81759
> 099
> 54
> L69850
> 393.66
> 54
> Y780024
> 347
> CM97448
> 1.88
> 54
> 顾问 LW67640 (Rank 24)
> 37
> 135
> 55
> YL42885
> 099
> 55
> 5N71847
> 392.15
> 55
> C216695
> 341
> 55
> 010343
> 187
> 55
> 4269256
> 37
> 134
> 56
> W22772
> 099
> 56
> V56392
> 39208
> 56
> LL90629
> 340
> 56
> 5530834
> 187
> 56
> XM75236
> 37
> 133
> Y82997
> 099
> AL71656
> 38991
> 57
> YJ89646
> 339
> 57
> YZ99035
> 186
> 171699
> 36
> 171
> 58
> 2H71971
> 099
> 58
> 028126
> 381.57
> 58
> 163377
> 337
> YC82708
> 1.85
> 58
> XG98059
> 36
> 163
> 59
> 顾问 ZH78994 (Rank 11)
> 099
> LV57140
> 380.78
> 59
> E95623
> 333
> 丛L80893
> 185
> 59
> J61289
> 154
> 60
> ZX59531
> 099
> 60
> 0N30025
> 37803
> 60
> YH78429
> 331
> 60
> U63604
> 1.84
> 60
> 0123443
> 152
> 7Y77039
> 099
> 卫79519
> 37657
> P017729
> 330
> D19979
> 184
> 0N16452
> 36
> 150
> ZZ40911
> 099
> 4026227
> 369.68
> F47631
> 3.28
> YP74336
> 183
> 顾问 FD69320 (Rank 34)
> 147
> AC58355
> 098
> D57101
> 366.80
> 4096966
> 321
> W548176
> 182
> D28368
> 144
> C094009
> 098
> 473186
> 364.86
> KP22438
> 321
> 4457211
> 181
> 582574
> 141
> 0N91908
> 098
> 工032856
> 361.49
> L65774
> 320
> 」74499
> 180
> Y81055
> 131
> 卧17351
> 098
> T90403
> 360.89
> 1053797
> 318
> 66
> ZX24677
> 1.79
> 66
> 顾问 YX23928 (Rank 8)
> 130
> EK80645
> 098
> 5T37368
> 35392
> X83124
> 316
> STG1360
> 179
> 4092395
> 121
> 68
> [639655
> 098
> 497420
> 351.84
> 」93257
> 313
> 68
> 455707
> 1.78
> 68
> MK410G0
> 36
> 101
> EI96533
> 098
> 1I58194
> 34314
> U63604
> 311
> MB86518
> 178
> H39000
> 190
> 70
> 」47083
> 098
> 70
> 471281
> 341.81
> 70
> YL81651
> 311
> 70
> 190400
> 1.78
> 70
> 0L45135
> 160
> 71
> J53335
> 098
> 71
> 4854738
> 33999
> 71
> MD65015
> 310
> IK47019
> 178
> XZ69776
> 35
> 158
> 」81222
> 098
> 72
> 4079370
> 33395
> 72
> XZ21889
> 310
> 72
> 1L61351
> 177
> 72
> 1U53797
> 149
> 7
> 1433235
> 098
> 73
> CC72318
> 32780
> 73
> KP26017
> 309
> XM19402
> 177
> 73
> 2V96737
> 35
> 148
> 74
> 140932
> 098
> 74
> N068030
> 32565
> 74
> 5224058
> 309
> 1015326
> 177
> 74
> 4C78364
> 35
> 147
> NE92729
> 098
> 75
> M065015
> 32300
> 75
> AM12075
> 307
> 75
> 4578592
> 176
> 75
> CI68712
> 144
> 76
> MG68462
> 098
> 76
> YC82708
> 322.54
> 76
> ZH74761
> 306
> 76
> KS88333
> 176
> 76
> 4565681
> 35
> 139
> NN39972
> 098
> NN89351
> 32082
> 77
> 455707
> 305
> 77
> YC99622
> 176
> 77
> E578924
> 35
> 136
> 78
> 卫078486
> 098
> 78
> 0P82177
> 319.40
> 78
> V82626
> 305
> 」C84638
> 1.75
> 78
> 8W28426
> 129
> P669645
> 098
> 79
> D82796
> 31751
> 79
> 0y13559
> 304
> 79
> CL56494
> 175
> 79
> ZZ55695
> 35
> 124
> 80
> 0H40023
> 098
> H28002
> 316.18
> TN20848
> 302
> 80
> 顾问 YX23928 (Rank 8)
> 175
> 80
> Y288594
> 114
> 0482915
> 098
> 420384
> 31537
> U37372299
> EL15829
> 175
> PW58059
> 34
> 162
> P26750
> 098
> NT61860
> 31203
> Z210277
> 299
> 82
> 1053797
> 175
> 82
> J16084
> 34
> 149
> 023235
> 098
> A193287
> 311.42
> DL80869
> 298
> 止60830
> 174
> 顾问 WX84677 (Rank 69)
> 144
> PT85351
> 098
> NQ12289
> 308.65
> H65370
> 298
> 84
> 顾问 YH25030 (Rank 31)
> 1.74
> 84
> 顾问 CT48231 (Rank 2)
> 34
> 141
> 0068782
> 098
> 顾问 CC40930 (Rank 95)
> 30730
> ZH41150
> 298
> 85
> PC73872
> 173
> XH77948
> 34
> 137
> R636120
> 098
> 175132
> 30717
> 420306
> 295
> C521130
> 1733
> NG78013
> 34
> 133
> RW93893
> 098
> ND59617
> 305.52
> JC84638
> 294
> 5Z83096
> 173
> M551256
> 34
> 127
> 5C67341
> 0T75470
> 305.06
> 」79797
> 294
> 0L86385
> 1.72
> Z147333
> 121
> T16179
> 098
> 0482915
> 30315
> EN44285
> 293
> CX98570
> 171
> 164154
> 34
> 107
> D71562
> 098
> 442510
> 302.81
> 顾问 KZ79256 (Rank 21)
> 293
> 4220306
> 1.71
> R890992
> 34
> 102
> 顾问 VC95113 (Rank 58)
> 098
> NN52920
> 301.75
> 0026285
> 292
> K79256
> 171
> 2053542
> 191
> Uk29840
> 098
> TP73016
> 30135
> 5Z84537
> 292
> PY32594
> 170
> U474101
> 177
> U89028
> 98
> N480227
> 301.19
> TD22984
> 292
> MN89184
> 170
> U78189
> 33
> 157
> U99277
> 098
> IN14425
> 300.70
> 顾问 ZH78994 (Rank 11)
> 291
> 5W39888
> 170
> 5P89971
> 155
> 0591221
> 098
> 1413207
> 29945
> 95
> KC78191
> 290
> 95
> RP76828
> 170
> 125854
> 33
> 154
> U63604
> 098
> R890992
> 298.22
> 4569440
> 288
> YL21428
> 1.70
> D71562
> 154
> XI80376
> 098
> 5M36732
> 29791
> B148361
> 287
> C197429
> 170
> 5I65808
> 145
> Y819132
> 098
> NL28110
> 294.94
> M060428
> 287
> 98
> 4096966
> 1.69
> XS83288
> 142
> Y231130
> 098
> U38282
> 29452
> T019081
> 287
> 顾问 JC25241 (Rank 12)
> 169
> D94923
> 141
> 100
> YZ62157
> 098
> 100
> C852451
> 29382
> 100
> J10865
> 2.86
> 100
> 0/73553
> 1.69
> 100
> M518311
> 135
> Ng


### 六维龙虎榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant六维龙虎榜
> 2026-05-09
> Rank
> operatorCount
> operatorAvg
> feldCount
> fieldAvg
> communityActivity
> maxSimulationstreak
> 082626
> 322
> 116
> L00
> 6040
> 530
> 184677
> 278
> 4770
> 527
> 5P89971
> 119
> 5860
> 406
> R693974
> 327
> 180
> 5560
> 539
> 2559753
> 133
> 5850
> 540
> R890992
> 器
> 131
> 5320
> 585
> 」615244
> 135
> 5600
> 459
> D94923
> 70
> 145
> 158
> 45.90
> 363
> 5C73595
> 116
> 117
> 4950
> 555
> 10
> 丛L47973
> 60
> 241
> 88
> 119
> 52.20
> 327
> 11
> M19619
> 104
> 25
> 4230
> 547
> 425474
> 72
> 86
> 3190
> 412
> 490970
> 36
> 137
> 5320
> 381
> "
> 79256
> 82
> 91
> 4410
> 453
> 0P72475
> 29
> 5010
> 453
> 16
> RP76828
> 112
> 47
> 105
> 05
> 5010
> 410
> L39100
> 4590
> 360
> 5783096
> '23
> 157
> 6100
> 489
> 19
> N52721
> 器
> 23
> 4820
> 93
> K30147
> 36
> 4830
> 286
> K61864
> 76
> 163
> 5500
> 540
> `
> u44462
> 64
> 168
> 5500
> 741
> 丛L58442
> 167
> 4410
> 541
> 24
> 顾问 MZ45384 (Rank 51)
> 102
> 90
> 112
> 57.40
> 335
> YL66992
> 5860
> 386
> 26
> 工094100
> 96
> 58
> 159
> 4770
> 358
> J23144
> 08
> 26
> 5830
> 386
> 28
> 1X89624
> 41
> 4950
> 263
> LO40GG0
> 123
> 4410
> 556
> 0L53864
> 57
> 104
> 170
> 4410
> 570
> 171699
> 146
> 24
> 3720
> 641
> ;
> 1494963
> 118
> 3240
> 370
> L16829
> 卫
> 36
> 5320
> 566
> 1N62753
> 88
> 102
> 45.90
> 590
> 1027384
> 5500
> 255
> 36
> 413375
> 113
> 5630
> 369
> L88OGO
> 58
> 4040
> 533
> 」38399
> 108
> 151
> 5740
> 400
> P511956
> 58
> 119
> 4680
> 373
> 40
> 1053797
> 62
> 154
> 6040
> 310
> AMUGO5Og
> 351
> 5320
> 335
> NS77148
> 241
> 82
> 111
> 5320
> 579
> 嚣
> 8636120
> 髫
> 4230
> 365
> u21812
> 105
> 75
> 51.40
> 813
> B451127
> 116
> 5920
> 634
> 46
> CX60157
> 108
> 2220
> 372
> J15679
> 114
> 5500
> 468
> 029269
> 111
> 79
> 4410
> 613
> N32626
> 105
> 4770
> 576
> 50
> XZ69776
> 108
> 4670
> 453
> 4551256
> 94
> 130
> 42.30
> 453
> IL75459
> 4.25
> 101
> 102
> 4230
> 279
> L89289
> 103
> 136
> 56.20
> 454
> 54
> ZV96737
> 55
> 112
> 1.17
> 38.60
> 438
> 55
> 丛97497
> 104
> 191
> 5320
> 742
> 56
> ZY36280
> 4.25
> 135
> 55.80
> 387
> 1/18421
> 59
> 153
> 6040
> 353
> 58
> XCG6172
> 59
> 151
> 4830
> 436
> 433503
> 56
> 372
> 121
> 4830
> 465
> 60
> XZ81923
> 36
> 100
> 1.18
> 43.90
> 421
> 顾问 ZH78994 (Rank 11)
> 36
> 5770
> 148
> 1637773
> 06
> 1
> 102
> 5500
> 481
> SW42429
> 104
> 1.00
> 3860
> K255390
> 381
> 103
> 4770
> 盥
> 顾问 WX64154 (Rank 32)
> 124
> 5370
> J16510
> 150
> 4770
> 593
> 顾问 CT48231 (Rank 2)
> 留
> 鹨
> 嚣
> 40
> 4690
> 242
> GM54012
> 1.78
> 4230
> 335
> 顾问 NL80893 (Rank 16)
> 115
> 5770
> 360
> 70
> 5081732
> 1.74
> 50.40
> 419
> 4C78364
> 器
> 58
> 99
> 110
> 4130
> 293
> 1y85808
> 13
> 77
> 1.24
> 40.40
> 427
> 7
> 0N16452
> 105
> 195
> 204
> 5040
> 587
> 74
> 5C77987
> 4.25
> 181
> 157
> 61.00
> 252
> 1433235
> 138
> 4590
> 595
> 75
> P23235
> 58
> 112
> 43.60
> 170
> J96079
> 86
> 06
> 114
> 138
> 3680
> 344
> 78
> 8W28426
> 26
> 90
> 131
> 73.70
> 413
> 顾问 LW67640 (Rank 24)
> 52
> 447
> 106
> 52.10
> 531
> 80
> YX37105
> 133
> 153
> 4770
> 207
> 4041126
> 120
> 200
> 4780
> 507
> 顾问 YX23928 (Rank 8)
> 38
> 00
> 94
> 1.26
> 58.60
> 522
> 835905
> 22
> 4370
> 327
> H62464
> 86
> 1.75
> 4410
> 4555260
> 105
> 5140
> 484
> 顾问 YL20193 (Rank 37)
> 翳
> 123
> 58.60
> 480
> V58435
> 100
> 4040
> 427
> MO62208
> 
> 65
> 1.56
> 4770
> 538
> 659154
> 416
> 142
> 5860
> 334
> 8N67375
> 104
> 84
> 181
> 56.50
> 369
> HE56620
> 107
> 197
> 51.00
> 433
> T21691
> 107
> 126
> 3680
> 362
> 5W82574
> 129
> 197
> 42.80
> 362
> 」79797
> 475
> 175
> 1.75
> 55.60
> 400
> 492336
> 194
> 4770
> 349
> D64461
> 105
> 438
> 121
> 183
> 3860
> 674
> 1L49894
> 363
> 146
> 147
> 2650
> 307
> SIGS8O8
> 457
> 136
> 153
> 3500
> 542
> 465370
> 374
> 117
> 140
> 5660
> 310
> 100
> 4095618
> 295
> 1.24
> 38.60
> 371


### 国区双榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant顾问龙虎榜 (围区)
> 2026-05-09
> Max VF
> Max WF
> Max Combine
> Max
> Combine
> Max Pyramid
> Rank
> VF
> Rank
> VF
> Rank
> CM
> Rank
> AVG
> Rank
> PYR
> AL
> E65210
> L00
> 卫33369
> 97825
> 174218
> 694
> 174218
> 383
> 79797
> 55
> 163
> 」87757
> 100
> 4269256
> 23367
> 0C68819
> 603
> 山37372
> 299
> 山52291
> 52
> 1566
> U062208
> L00
> 116829
> 18069
> L71036
> 573
> 4569440
> 288
> J39934
> 51
> 181
> 5017531
> 100
> K79256
> 13717
> ZE97721
> 541
> 1640486
> 284
> 5783096
> 51
> 157
> KX88140
> L00
> 0429412
> 13348
> JR15410
> 507
> Y11344
> 282
> 122447
> 45
> 189
> X56645
> 100
> L71699
> 12929
> 1640486
> 505
> X221889
> 278
> 1022811
> 171
> X25924
> L00
> L79055
> 12788
> L15616
> 488
> 0C68819
> 264
> 0H19310
> 45
> 183
> V81852
> 100
> 0068782
> 12500
> 411344
> 488
> E91858
> 260
> X54051
> 179
> y72634
> L00
> WY56787
> 12416
> 」16243
> 486
> 5224058
> 249
> 417279
> 134
> UL28382
> 100
> 10
> F69320
> 12157
> 10
> E15829
> 473
> 丘28881
> 236
> 422845
> 189
> YL9GOGB
> 100
> 卫53723
> 12109
> CZ67480
> 444
> ZV96737
> 231
> 」42868
> :
> 170
> C186067
> 099
> ZM43612
> 11916
> 0L32665
> 436
> 138399
> 229
> 2H34713
> 162
> 
> CX60157
> 099
> 13
> 5C13445
> 11907
> 止55914
> 436
> M12075
> 227
> 13
> 5C23342
> 129
> 0Y13559
> 099
> 188060
> 11733
> 14
> ML42552
> 419
> 1X81181
> 225
> 14
> Y25030
> 153
> 445023
> 099
> Y93864
> 11210
> 」38399
> 403
> J37401
> 221
> }78449
> 151
> J062872
> 099
> 16
> 2135633
> 11108
> 16
> 0129942
> 390
> 163377
> 221
> 16
> 4643324
> 145
> 17
> 184394
> 099
> 116510
> 10211
> ZC2G0BO
> 366
> YC76553
> 221
> JSOOO5
> 40
> 131
> 18
> 1015326
> 099
> 18
> 4433574
> 10134
> 18
> E39657
> 352
> LL90629
> 219
> 18
> 032536
> 181
> Ly85808
> 099
> 0231817
> 9189
> ZV96737
> 348
> &22438
> 215
> E60707
> 156
> 056787
> 099
> 20
> XM75236
> 83.21
> 20
> 1280024
> 347
> 20
> Y78429
> 211
> 20
> 」89289
> 156
> 0K32246
> 099
> SW48878
> 7114
> C215695
> 341
> X54051
> 209
> K79256
> 147
> "
> WP88606
> 099
> P64174
> 69.88
> 1L90629
> 340
> ZF97721
> 206
> 孟
> 2C54526
> 174
> 118521
> 099
> Y262157
> 6911
> Y89646
> 339
> 170892
> 203
> ZR94671
> 165
> XD81759
> 099
> 24
> 8451127
> 6866
> 24
> 163377
> 337
> 24
> 0L32665
> 203
> 24
> 1015326
> 163
> YL42885
> 099
> SIGI3GO
> 5836
> YH78429
> 331
> 5284537
> 202
> 25
> 1033850
> 160
> 26
> W22772
> 099
> 26
> 417279
> 66,27
> 26
> 622438
> 321
> 26
> 4066932
> 201
> 26
> 0014840
> 159
> Y82997
> 099
> 0y83769
> 5479
> 165774
> 320
> 27
> XS34596
> 201
> 4G88592
> 141
> ]
> 2H71971
> 099
> 28
> XZ23611
> 63.79
> 28
> 1U53797
> 318
> 7135633
> 28
> 7559763
> 139
> ZX59531
> 099
> 5C84371
> 5307
> X83124
> 316
> YC99371
> 197
> N19619
> 137
> 2Y77039
> 099
> 30
> 420306
> 6277
> 30
> U63604
> 311
> AC60527
> 197
> 30
> 0X52484
> 133
> 30
> ZZ40911
> 099
> J71859
> 5192
> YL81551
> 311
> 4P65370
> 197
> Y262807
> 37
> 171
> E639655
> 098
> 181819
> 59.24
> X221889
> 310
> 32
> Y296589
> 192
> {67304
> 37
> 164
> 3
> 147083
> 098
> 5L10033
> 5787
> 33
> 5224058
> 309
> HE76003
> 192
> 33
> J23144
> 37
> 145
> 34
> 」81222
> 098
> 34
> XD81759
> 5717
> 34
> 412075
> 307
> CY59336
> 190
> 34
> L67640
> 37
> 135
> 140932
> 098
> 169468
> 5712
> ZH74761
> 306
> 35
> YIO136
> 188
> 469256
> 37
> 134
> 36
> 卫26750
> 098
> 36
> 卫25631
> 5703
> 36
> 0y13559
> 304
> 36
> CM97448
> 36
> XU75236
> 37
> 133
> 0068782
> 098
> 1444620
> 56O6
> 丛7372_299
> 卫10343
> 187
> L71699
> 171
> 38
> 业63604
> 098
> 38
> 149592
> 5573
> 38
> 7710277
> 299
> 1299035
> 86
> 38
> XG98059
> 163
> XI80376
> 098
> 39
> 4G88592
> 5451
> 465370
> 298
> 丛80893
> 185
> J61289
> 154
> 1231130
> 098
> 40
> 0462432
> 5407
> 40
> ZH41150
> 298
> 业63604
> 184
> [D69320
> 147
> 40
> Y262157
> 098
> W84677
> 5362
> 420306
> 295
> 40
> YP74336
> 83
> w
> U81055
> 131
> 42
> 2590407
> 098
> 23928
> 5355
> 」79797
> 294
> W548176
> 182
> Y23928
> 130
> ZZ44620
> 098
> 4017963
> 5317
> K79256
> 293
> 457211
> 181
> 4092395
> 121
> 44
> 8592559
> 097
> 44
> 5017531
> 5297
> 44
> 5784537
> 292
> 44
> 174499
> 44
> 4L45135
> 35
> 160
> 140454
> 097
> 45
> X42289
> 5250
> 4569440
> 288
> ZX24677
> 179
> XZ69776
> 35
> 158
> 46
> 114975
> 097
> 46
> 444931
> 4806
> 46
> 848361
> 287
> 5I61360
> 179
> 46
> 1053797
> 149
> J80916
> 097
> 47
> C089422
> 4743
> W66806
> 283
> 190400
> 178
> 47
> ZV96737
> 35
> 148
> 48
> 1013454
> 097
> 48
> ZL29184
> 4646
> 48
> I88765
> 283
> 凹47019
> 178
> 48
> 4565681
> 35
> 139
> WE80243
> 097
> Z210277
> 4622
> Y084572
> 282
> 161351
> 177
> B28426
> 35
> 129
> 50
> 0429412
> 097
> 50
> 8L20996
> 4537
> 50
> Y288594
> 282
> 50
> XM19402
> 177
> 50
> ZZ55695
> 124
> W055029
> 097
> KD86036
> 4465
> 顾问 NL80893 (Rank 16)
> 281
> 1015326
> 177
> YZ88594
> 114
> WP52250
> 097
> 52
> CZ10093
> 44.20
> 52
> WX18521
> 281
> 52
> 4F78592
> 176
> 52
> PW58059
> 162
> 53
> WZ47295
> 097
> 53
> RP76828
> 4411
> 53
> Y93864
> 281
> YC99622
> 176
> 53
> J16084
> 149
> 54
> XL48428
> 097
> 54
> 顾问 LW67640 (Rank 24)
> 43.70
> 54
> MH33969
> 280
> CL56494
> 1.75
> 54
> 顾问 WX84677 (Rank 69)
> 144
> 55
> YD42421
> 097
> 55
> ML42552
> 4352
> 55
> 顾问 FD69320 (Rank 34)
> 278
> 55
> 顾问 YX23928 (Rank 8)
> 175
> 55
> XH77948
> 137
> 56
> YH87796
> 097
> 56
> J44290
> 43.07
> 56
> 1022811
> 272
> 56
> EL15829
> 175
> 56
> 顾问 MS51256 (Rank 28)
> 127
> C86846
> 096
> FP65798
> 4298
> 57
> ZH71971
> 272
> 57
> L053797
> 175
> 2147333
> 
> 121
> 58
> 0498440
> 096
> 58
> N19619
> 41.71
> 58
> 2H87224
> 271
> u60830
> 1.74
> 58
> 顾问 WX64154 (Rank 32)
> 107
> 59
> 032665
> 096
> 59
> 111546
> 4127
> 010343
> 270
> 顾问 YH25030 (Rank 31)
> 174
> 59
> 2053542
> 191
> 60
> GL98521
> 096
> 60
> YB49779
> 41.01
> JL80gOO
> 269
> 60
> PC73872
> 173
> 60
> U474101
> 177
> 5R857579
> 096
> CC21336
> 4082
> IL53163
> 268
> C521130
> 173
> U78189
> 157
> 420306
> 096
> 184152
> 40.28
> B59154
> 267
> 5283096
> 1733
> 1225854
> 154
> J023670
> 096
> 0P72475
> 4006
> 顾问 顾问 RM49262 (Rank 30) (Rank 30)
> 267
> D86385
> 172
> 5I65808
> 145
> J15679
> 096
> PW58059
> 39.89
> CC67505
> 264
> CX98570
> 1.71
> XS83288
> 142
> 」31069
> 096
> ILIOgOS
> 3955
> 125854
> 264
> 65
> 4220306
> 171
> 4248623
> 134
> LY52969
> 096
> 5081732
> 39.44
> Z135633
> 264
> K79256
> 171
> 丛80893
> 132
> 0W94165
> 096
> YL21428
> 3932
> 顾问 JR23144 (Rank 6)
> 263
> P32594
> 170
> 0P72475
> 33
> 126
> 0267721
> 096
> 68
> EL94401
> 38.96
> 116510
> 262
> 5W39888
> 170
> 68
> EL39657
> 33
> 124
> 5C23342
> 096
> ZX58901
> 3872
> CL56494
> 261
> RP76828
> 170
> 0068782
> 121
> 70
> 5014148
> 096
> 70
> 458883
> 38.49
> 70
> FN91858
> 260
> YL21428
> 170
> 70
> 484915
> 116
> 71
> W529639
> 096
> CL49716
> 3806
> 4248623
> 260
> C197429
> 170
> 1687838
> 115
> 7
> XL71350
> 096
> 72
> 1L87164
> 3795
> 72
> 顾问 LW67640 (Rank 24)
> 260
> 73
> 0173553
> 1.69
> #
> 0210943
> 33
> 114
> YH78429
> 096
> 73
> FL11741
> 3774
> 73
> X37939
> 260
> YZ88594
> 169
> 工21691
> 113
> 74
> Y051506
> 096
> 74
> IL42173
> 37.45
> 74
> 1033850
> 259
> 118421
> 1.68
> 74
> 1L49894
> 147
> 75
> YZ59361
> 096
> 75
> YC99622
> 3730
> 75
> 0L47372
> 258
> 0068782
> 167
> 75
> J51810
> 32
> 144
> 76
> 2559763
> 096
> 76
> 0T40395
> 36.88
> 76
> W18906_258
> 76
> C767480
> 167
> 163377
> 32
> 136
> 77
> DIG6970
> 095
> XP21100
> 3590
> 77
> YD77867
> 258
> CM59456
> 166
> 充
> 035234
> 32
> 132
> 78
> E39657
> 095
> 78
> YXI5005
> 35.61
> 78
> 顾问 YH25030 (Rank 31)
> 256
> J23144
> 1.66
> 78
> 4113375
> 128
> J78363
> 095
> 79
> 0y12692
> 3547
> 79
> B110003
> 255
> KC82433
> 166
> 79
> 5W34207
> 32
> 128
> 80
> 1087845
> 095
> 0Y27687
> 35.36
> 5017531
> 255
> 80
> 1022811
> 1.64
> 80
> XL98962
> 31
> 184
> LL81909
> 095
> BU28426
> 3423
> 161351
> 254
> H40076
> 163
> 2487224
> 31
> 138
> 1R93609
> 095
> XY56645
> 3347
> 578592
> 253
> 2242824
> 163
> 82
> XZ81923
> 135
> LW93678
> 095
> 5610230
> 3300
> 4583704
> 253
> 83
> E69320
> 163
> GW98315
> 31
> 134
> MY51598
> 095
> 5J65808
> 3292
> W26072
> 252
> 4699972
> 1.62
> 1W93678
> 134
> P16638
> 095
> 顾问 YH25030 (Rank 31)
> 3209
> 4457211
> 248
> 85
> 116510
> 160
> 乙Z74958
> 130
> XC47437
> 095
> 1494963
> 3207
> J96397
> 248
> XS80591
> 159
> CC21336
> 122
> XX42289
> 095
> 山L27618
> 3177
> WX81181
> 247
> 2H87224
> 159
> ZZ51745
> :
> 121
> Y282897
> 095
> 4533387
> 31.77
> 0J97429
> 2.46
> X37939
> 158
> ML42357
> 110
> YZ88594
> 095
> 4632717
> 3154
> 5I65808
> 246
> X17517
> 157
> NU28753
> ZC26080
> 095
> 082427
> 3097
> UL58980
> 246
> XX42289
> 157
> 」29779
> 158
> ZX24677
> 095
> YS95353
> 3068
> 0X52484
> 245
> Y084572
> 156
> U63604
> 145
> 4M12075
> 094
> 140454
> 30.40
> 139823
> 244
> 0H68852
> 156
> CN26548
> 144
> EC34030
> 5Z83096
> 3027
> 顾问 MS51256 (Rank 28)
> 241
> QL50450
> 156
> C695788
> 136
> H65370
> 094
> Y286931
> 30.09
> 5783096
> 241
> 0688592
> 1.55
> YL28729
> 132
> 120282
> 094
> WP77813
> 3006
> EX25214
> 240
> 95
> 651368
> 1.54
> 1479055
> 123
> 」61289
> 094
> F60707
> 2979
> 4Y17279
> 239
> 656831
> 1.54
> ?656831
> 117
> 」74499
> 094
> 024362
> 2977
> C521130
> 239
> 乙I81809
> 1.54
> AM12075
> 115
> MS70058
> 094
> CL88457
> 2948
> 433503
> 239
> HC66282
> 1.53
> U29742
> W424469
> 094
> W424469
> 2928
> 5C84371
> 239
> 4248623
> 153
> YT52851
> 149
> 100
> XCgGOOO
> 0.94
> 100
> YX50OO5
> 29.01
> 100
> 1y85808
> 238
> 100
> 1031804
> 1.52
> 100
> [78468
> 29
> 134
> Nvg


### 
> [!NOTE] [图片 OCR 识别内容]
> WorldQuantx维龙虎榜
> 国区)
> 2026-05-09
> Rank
> operatorCount
> operatorAvg
> feldCount
> fieldAvg
> communityActivity
> maxsimulationstreak
> 184677
> 278
> L00
> 4770
> 527
> 189624
> 311
> 4950
> 263
> 425474
> 3190
> 1027384
> 詈
> 5500
> 25
> L9100
> 4590
> 1615244
> 321
> 335
> 5600
> 山L47973
> 241
> 119
> 5220
> 2559763
> 393
> 133
> 5850
> 10
> N596s
> 95
> 85
> 104
> 38
> 129
> 4230
> 
> 11
> 0P72475
> 5010
> RP76828
> 112
> 447
> 05
> 6010
> K79256
> 4410
> %
> 188060
> 3
> 40.40
> 533
> 4L13375
> 113
> 38
> 6630
> 369
> 16
> 4745384
> 102
> 07
> 112
> 57.40
> 335
> J15679
> 114
> 5500
> 468
> 18
> 1637773
> 36
> 55.00
> 19
> YL66992
> 38
> 5860
> 386
> 171599
> 95
> 146
> 24
> 3720
> 641
> CX60157
> 108
> 08
> 2220
> 372
> "
> 2196737
> 81
> 112
> 117
> 3860
> 438
> 1494963
> 347
> 118
> 29
> 32.40
> 370
> J823144
> 421
> 108
> 26
> 5830
> 386
> 1517092
> 63
> 56
> 00
> 5680
> 243
> 丛80893
> 50
> 94
> 5770
> 360
> 鲨
> 5W42429
> 104
> 00
> 3860
> 254
> 山33503
> 72
> 121
> 4830
> 465
> 116829
> 374
> 盈
> 36
> 5320
> 566
> X281923
> 36
> 93
> 118
> 4390
> 
> 顾问 LY85808 (Rank 86)
> 124
> 4040
> 龆
> 」38399
> 108
> 151
> 5740
> 4551256
> 92
> 30
> 4230
> 453
> 34
> 5783096
> 59
> 423
> 器
> 157
> 6100
> 489
> L16510
> 44
> S0
> 4770
> 593
> 36
> P511956
> 52
> 58
> 4680
> 373
> XCGG172
> 58
> 59
> 99
> 151
> 4830
> 436
> XZ69776
> 410
> 108
> 137
> 4670
> 453
> 5081732
> 35
> 174
> 6040
> Y23928
> 4
> 26
> 5860
> 盥
> 4555260
> 05
> 5140
> 0695788
> 66
> 90
> 00
> 40.40
> 336
> "
> Zy36280
> 425
> 35
> 5580
> 387
> U18421
> 59
> 153
> 6040
> 353
> 189289
> 29
> 103
> 36
> 56.20
> 454
> 1U53797
> 62
> 60.40
> 310
> 45
> B28426
> 26
> 90
> 131
> 7370
> 413
> X85841
> 
> 43
> 56
> 113
> 4770
> 463
> B451127
> 418
> 116
> 5920
> 534
> 50
> M062208
> 65
> 56
> 4770
> 538
> K22438
> 430
> 75
> 00
> 3780
> 170
> 52
> K255390
> 371
> 103
> 47.70
> 353
> 465370
> 374
> 117
> 40
> 56G0
> 310
> 54
> 顾问 WX64154 (Rank 32)
> 87
> 60
> 53.70
> 311
> 55
> 659154
> 184
> 42
> 5860
> 56
> C163008
> 27
> 312
> 63
> 00
> 3680
> 鹬
> RJ74200
> 59
> 5860
> 58
> 064268
> 319
> 1.12
> 24.10
> p490725
> 93
> 123
> 5320
> 339
> 60
> 4518471
> 00
> 36.80
> 316
> LC34491
> 4.20
> 00
> 1680
> 210
> ZY88181
> 4.24
> 嚣
> 121
> 4650
> 367
> 885606
> 150
> 101
> 4770
> IL10905
> 334
> 93
> 58.60
> 2
> YX37105
> 153
> 4770
> CR35762
> 3.79
> "
> 07
> 51.40
> 369
> NL80034
> 443
> 00
> 2670
> 170
> ZC54526
> 116
> 55.00
> LL49894
> 146
> 147
> 2650
> 300
> 5C77987
> 4.25
> 181
> 157
> 61.00
> 70
> 顾问 LW67640 (Rank 24)
> 62
> 447
> 106
> 62.10
> [21691
> 107
> 416
> 126
> 36.80
> 蛋
> 5220589
> 125
> 152
> 28.70
> "
> FZ607OZ
> 120
> 392
> 115
> 68.20
> HE56620
> 107
> 97
> 51.00
> 433
> 0L47372
> 3.21
> 85
> 30
> 49.50
> 167
> E581271
> 377
> 162
> 31.40
> 350
> 78
> WL33473
> 50
> 87
> 111
> 40.40
> 359
> 5017531
> 嚣
> 152
> 5680
> 516
> 80
> ML74437
> 85
> 1.19
> 56.80
> 268
> C462432
> 87
> 123
> 39.20
> 412
> 0C90573
> 10
> 1.16
> 4410
> 285
> M78189
> 391
> 59
> 3500
> 277
> 0y49971
> 452
> 116
> 147
> 31.40
> 536
> 5I65808
> 82
> 457
> 136
> 153
> 3500
> 542
> E39657
> 82
> 3.78
> 134
> 51.40
> 137
> CX43424
> 315
> 09
> 1860
> 469256
> 459
> 147
> 50.40
> 652
> 」39934
> 415
> 154
> 5740
> 310
> GM92689
> 440
> 104
> 31.40
> 255
> 顾问 YH25030 (Rank 31)
> 442
> 
> 1.14
> 5010
> 430
> 0548533
> 333
> 97
> 2950
> 448
> YE22412
> 435
> 00
> 2040
> 158
> 0068782
> 56.80
> 382
> 0y13559
> 45
> 106
> 4770
> 231
> V22772
> 1.16
> 35.00
> 6H93979
> 427
> 58
> 100
> 2230
> 348
> 5C23342
> 93
> 3.85
> 223
> 4410
> 344
> DC11087
> 29
> 10
> 102
> 2410
> 193
> 100
> J454866
> 4.28
> 1.38
> 56.80
> 258
> 93
> 59


### Genius龙虎榜


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant genius
> 龙虎榜
> 2026-05-09
> Vedl
> patorCount
> fieldCount
> fieldAvg
> 5P89971
> 5850
> RR90992
> DKq4923
> NII19619
> 4y90970
> _0P72475
> 6100
> 顾问 TD94100 (Rank 7)
> 4770
> 1171699
> R636120
> XZ69776
> 4670
> 11189289
> 71/96737
> 1X64154
> 丛L80893
> 5040
> 81128426
> 1167640
> 62.10
> 492336
> 4770
> 5165303
> M813430
> 4040
> E6070
> 68.20
> 5500
> 4Y17279
> 4230
> 山41060
> 51.40
> 005373?
> 139934
> 刀/71562
> 4748623
> W478189
> OTSG4S?
> 7437221
> 3800
> 4040
> 137333
> 174024
> YL28729
> 2770
> 5860
> 5500
> 5920
> P054914
> N4G88592
> 8M1207
> N430407
> 4025387
> 46.50
> 2360
> 3380
> 顾问 FD69320 (Rank 34)
> 1015326
> 0045758
> 4290
> 5860
> 14/090077
> 4590
> 33.20
> 419328
> V4182621
> 49.50
> 顾问 ML47973 (Rank 100)
> 425474
> 31.90
> 60.10
> 115
> 11739100
> 顾问 KU30147 (Rank 55)
> 48.30
> 1
> NIICOA4?
> YL66992
> UX89624
> 15
> 53.2C
> Expert
> 55.00
> 40.40
> 205
> AMGOSOC
> 1
> 8451127
> 5500
> NT29269
> 顾问 NT32626 (Rank 80)
> Expert
> TL75459
> WY18421
> 60.40
> 4830
> 4830
> 剀33903
> 1637773
> 51I42429
> 47.70
> J16510
> Expert
> 26
> 60.40
> 40.40
> 5077937
> Expert
> 1433235
> Expert
> PT23235
> 16roilos
> 437C
> 4410
> 159
> 58G0
> 4040
> M06220E
> 163
> Expert
> FE56620
> 61.00
> HPE5370
> RI74200
> 5220589
> 28.70
> RH95743
> KP22438
> 顾问 VC95113 (Rank 58)
> 159
> Expert
> 1569925
> WC45s9
> 29
> 53.20
> Expert
> 4770
> 4H36812
> 184
> 0I90254
> 563C
> 164268
> C011207
> 4410
> 顾问 BM29781 (Rank 92)
> 4090
> 1135107
> R643820
> ZY88181
> HL26425
> 193
> YC48839
> TTI0055
> SM14025
> 5680
> 5017531
> 1
> 285
> Expert
> 48.00
> 4518471
> 203
> 61139014
> 0H62432
> KK76363
> 20
> 1061241
> 1070351
> 2770
> 401713559
> Expert
> 1C3449
> Expert
> 215
> 4026378
> 5680
> 36.8C
> 0Y62952
> 4230
> F4763
> 2470
> 219
> 5G 80
> 220
> XN13612
> 8N74418
> 222
> Expert
> 1480116
> 4770
> I7F306
> Expert
> 1X14975
> Expert
> TT91159
> 60.40
> 20 _岢56219
> BU14163
> 59.20
> 丛33473
> 40.40
> '
> DLI034
> Expert
> MF8384?
> 2
> UL58980
> 顾问 顾问 RM49262 (Rank 30) (Rank 30)
> 4230
> 04162372
> 5190
> FL11088
> 24
> 18.60
> 5860
> 248
> XNI23590
> Expert
> J871859
> 2
> 60.40
> VP879
> 40.40
> 0127687
> 56 30
> T72336
> 4290
> 29
> 0Y77844
> 1654887
> [25214
> 35.00
> 263
> N22772
> 0L50548
> 1087845
> 5490
> 266Is9so
> 158
> 38.60
> _0N41247
> 4230
> WP88GOE
> 40.40
> H179344
> YI8165
> 2H39644
> 45.90
> z
> TN10210
> 33.20
> 5P61833
> Expert
> 4410
> 40.40
> 7
> FI39510
> 306
> (750647
> 28.30
> ?
> VC26243
> 36.80
> 53.20
> MC4TOOF
> 4N30280
> Expert
> 1548176
> 289
> 8J10003
> 2040
> P64174
> 2230
> 2950
> 4720
> 296
> Expert
> RP40432
> Expert
> (523323
> Expert
> 5M58724
> _248
> 盗
> YL50102
> 556
> 3860
> 貂
> NH16784
> 3910
> MY21251
> 35.00
> MFS9400
> 55.00
> 035234
> 61128303
> Expert
> 4930
> KI 75220
> PN88168
> W494369
> Expert
> 31
> OI 7127C
> [639655
> 8H48458
> 3860
> 翌
> SM18051
> 3490
> MC44186
> Expert
> KP26017
> HI1584
> 」615244
> Expert
> Expert
> _ML74437
> Expert
> Expert
> Expert
> Expert
> Expert


潮起潮落，此卷暂且封存。

然庙堂之下，江湖之远，暗涌从未止息——昔有隐世GM，于VF九八之境摘金万八有余；今携满值而归，锋芒更盛。

此番季赏，是扶摇直上，再破云霄？

还是天道有衡，另藏玄机？

龙战于野，其血玄黄，待到时日， **卷三** 再会！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享，看这段开头的文字感觉不像是在看WQ论坛，而是在看武侠小说哈哈

=============================================================================


---

### 技术对话片段 159 (原帖: 一个基于经典的动量/反转策略的模板，出信号率非常高！！！Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX6J%2B7iCA6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAh0BaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzM1NzcxNjM1NDYwMjQ3LSVFNCVCOCU4MCVFNCVCOCVBQSVFNSU5RiVCQSVFNCVCQSU4RSVFNyVCQiU4RiVFNSU4NSVCOCVFNyU5QSU4NCVFNSU4QSVBOCVFOSU4NyU4Ri0lRTUlOEYlOEQlRTglQkQlQUMlRTclQUQlOTYlRTclOTUlQTUlRTclOUElODQlRTYlQTglQTElRTYlOUQlQkYtJUU1JTg3JUJBJUU0JUJGJUExJUU1JThGJUI3JUU3JThFJTg3JUU5JTlEJTlFJUU1JUI4JUI4JUU5JUFCJTk4BjsIVDoOc2VhcmNoX2lkSSIpNTkzNzk1NDYtNjI0NS00ZGQzLTlmZmMtY2NiODJlMWQ3YzkyBjsIRjoJcmFua2kIOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMUk00OTI2MgY7CFQ6EnJlc3VsdHNfY291bnRpFA%3D%3D--744574eb836be0eae0172033705861d0d413f5d4
- **时间**: 8个月前

**提问/主帖背景 (HX40615)**:
动量策略：如果股票的势头非常好（差），那么未来会延续向好（差）。反转策略：如果股票的势头过于好（差），则未来会发生逆转。模板中使用与过去时间段的最大值/均值作比较，来判断势头好坏。在analyst、fundamental、model数据集上均适用，尤其是基本面、收益、量价指标相关的因子都有明显的信号。(+/-)ts_max_diff/ts_av_diff(<norm/>({field}),{day})其中，+表示遵循动量策略，-表示反转策略，norm为对字段的数据处理，operator选择非常广泛，可以是算术变换(log/signed_power)、时间平滑(ts_zscore, ts_mean)、或者横截面标准化(rank/quantile)。进一步扩展，当前是对字段值来比较，可以尝试比较字段的std_dev、ir、delta等。有待改进，跑出来的因子常常是高turnover，低margin，即包含大量无效操作，如何把低效转为高效操作？

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================感谢大佬分享！话说我没有ts_max_diff这个操作符，想问下和ts_max(x,d)-ts_min(x,d)等价吗？===================================================================================


---

### 技术对话片段 160 (原帖: 一个基于经典的动量/反转策略的模板，出信号率非常高！！！Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一个基于经典的动量反转策略的模板出信号率非常高Alpha Template_35771635460247.md
- **时间**: 8个月前

**提问/主帖背景 (HX40615)**:
动量策略：如果股票的势头非常好（差），那么未来会延续向好（差）。

反转策略：如果股票的势头过于好（差），则未来会发生逆转。

模板中使用与过去时间段的最大值/均值作比较，来判断势头好坏。在analyst、fundamental、model数据集上均适用，尤其是基本面、收益、量价指标相关的因子都有明显的信号。

```
(+/-)ts_max_diff/ts_av_diff(<norm/>({field}),{day})
```

其中，+表示遵循动量策略，-表示反转策略，

norm为对字段的数据处理，operator选择非常广泛，可以是算术变换(log/signed_power)、时间平滑(ts_zscore, ts_mean)、或者横截面标准化(rank/quantile)。

进一步扩展，当前是对字段值来比较，可以尝试比较字段的std_dev、ir、delta等。

有待改进，跑出来的因子常常是高turnover，低margin，即包含大量无效操作，

如何把低效转为高效操作？

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！

话说我没有ts_max_diff这个操作符，想问下和ts_max(x,d)-ts_min(x,d)等价吗？

===================================================================================


---

### 技术对话片段 161 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 临时解决alpha页面不能翻页的问题.md
- **时间**: 2个月前

**提问/主帖背景 (WW15616)**:
打开开发者工具(快捷键f12),切换到控制台(Console).输入以下命令即可翻页:

```
document.querySelector('.footer__button.footer__button--next').click()
```


> [!NOTE] [图片 OCR 识别内容]
> Page
> 10,000+
> Fter
> Name
> Competition
> Type
> Status
> Date Created (EST
> Region
> Universe
> Retums
> Tumover
> Margin
> Tag
> Date Submitted
> (ESTI
> Search
> See
> See
> See
> Search
> See
> See
> 6
> 6
> 6
> C8
> See
> Search
> aONIMOUS
> REBUlar
> UNSUBNITTED
> 03/05/2026 EST
> US4
> TP30D0
> 0.55
> 2.6635
> 13.2135
> 4029533
> aONIMOUS
> REBUlar
> UNSUBNITTED
> 03'05/2026 EST
> US。
> TP30DD
> 5935
> 16.5755
> 5.529333
> aONIMOUS
> REgUlaT
> UASUBTITTEL
> 03105/2026 EST
> USA
> TP300
> [
> 3.9435
> 6630
> 35
> EONIMOUS
> ReEUlaT
> UNSUBNITTED
> 03(05/2026 EST
> USA
> T0P3030
> 805
> 15.299
> 10.20
> SORMOUs
> Reaular
> ONTEO
> 0305202
> JS
>  --
> 303o
> 7.719
> Prev
> Next
> 次迎
> 〈少元素
> -拦制台
> 毖源代码
> 网绛
> 〈公性能
> 内存
> 应用程序
> IOP
> n迸器
> 默认级别
> 99-
> 1个己隐藏
> document
> querySelector('
> Footer
> butzon.Tooter
> bult-on-
> Iext').CLick()
> undefined
> 控制台
> 问题
> Sharpe


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！当时翻不了页只能干瞪眼

这次学到了，码住以防下次再出现这种bug

=============================================================================


---

### 技术对话片段 162 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 临时解决alpha页面不能翻页的问题_38845039675287.md
- **时间**: 2个月前

**提问/主帖背景 (WW15616)**:
打开开发者工具(快捷键f12),切换到控制台(Console).输入以下命令即可翻页:

```
document.querySelector('.footer__button.footer__button--next').click()
```


> [!NOTE] [图片 OCR 识别内容]
> Page
> 10,000+
> Fter
> Name
> Competition
> Type
> Status
> Date Created (EST
> Region
> Universe
> Retums
> Tumover
> Margin
> Tag
> Date Submitted
> (ESTI
> Search
> See
> See
> See
> Search
> See
> See
> 6
> 6
> 6
> C8
> See
> Search
> aONIMOUS
> REBUlar
> UNSUBNITTED
> 03/05/2026 EST
> US4
> TP30D0
> 0.55
> 2.6635
> 13.2135
> 4029533
> aONIMOUS
> REBUlar
> UNSUBNITTED
> 03'05/2026 EST
> US。
> TP30DD
> 5935
> 16.5755
> 5.529333
> aONIMOUS
> REgUlaT
> UASUBTITTEL
> 03105/2026 EST
> USA
> TP300
> [
> 3.9435
> 6630
> 35
> EONIMOUS
> ReEUlaT
> UNSUBNITTED
> 03(05/2026 EST
> USA
> T0P3030
> 805
> 15.299
> 10.20
> SORMOUs
> Reaular
> ONTEO
> 0305202
> JS
>  --
> 303o
> 7.719
> Prev
> Next
> 次迎
> 〈少元素
> -拦制台
> 毖源代码
> 网绛
> 〈公性能
> 内存
> 应用程序
> IOP
> n迸器
> 默认级别
> 99-
> 1个己隐藏
> document
> querySelector('
> Footer
> butzon.Tooter
> bult-on-
> Iext').CLick()
> undefined
> 控制台
> 问题
> Sharpe


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！当时翻不了页只能干瞪眼

这次学到了，码住以防下次再出现这种bug

=============================================================================


---

### 技术对话片段 163 (原帖: 二季度了2个月，和大家分享一些alpha挖掘的思路经验分享)
- **原帖链接**: [Commented] 二季度了2个月和大家分享一些alpha挖掘的思路经验分享.md
- **时间**: 21天前

**提问/主帖背景 (LD22811)**:
2026 年第二赛季已进入收官倒计时，相信大家都在为最后的点塔和赛季排名做最后冲刺。这赛季我在多个地区实战验证，踩过坑也总结出了一套可复制的 alpha 挖掘和点塔方法。今天严格按照自己的工作流，经验分享出来，希望能帮到大家，也欢迎在评论区交流指正。

## 1. 根据华子哥插件和网页的提交数据初步判断优质的数据集和字段

**先筛数据再干活，是所有工作的前提** 。每天早上我会花 30 分钟做数据勘探，绝不盲目写代码。

华子哥插件优先找绿色数据集这是华子哥通过GM权限通过SA筛选ra收集到的数据判断出的优质ALPHA比例高的数据集，其次看适合的中性化

配合网页端提交数据看全局：1.寻找提交较多的数据集/字段，你大概率也可以在这个数据集里找出可提交的alpha；2.寻找新的宇宙/数据集，这里的alpha相关性较低，竞争少。

## 2. AI 帮助生成初始信号

AI 是最高效的初始信号生成器，能帮我们快速扩大信号池。我的使用流程非常明确：

确定优质数据集后，给 AI 输入标准化 prompt：

- 明确要求生成 **0 阶信号** ，仅使用基础变换（rank、ts_rank、delta、log 等）
- 指定地区、数据集和核心字段范围
- 要求 AI 为每个信号附上 **一句话经济逻辑解释**
- 要求输出平台支持的标准语法，可直接复制运行

**关键原则** ：AI 生成的信号 90% 都是垃圾，我们只需要从中筛选出 3-5 个有逻辑、回测基础表现不错的信号，作为后续优化的起点。不要迷信 AI 给出的高夏普，大概率是过拟合。

## 3. 纯粹的 0 阶模板寻找优质字段信号

很多人看不起 0 阶模板，但 **真正能长期稳定的 alpha，80% 都源于 0 阶信号** 。

我常用的0阶段模板：最原始的字段回填\去极值；字段ts_rank；字段AB除法运算；字段AB减法运算。

我的标准操作：

- 对每个新数据集，先跑一遍所有字段的纯 0 阶信号
- 筛选出夏普 > 0.8、fit>0.5的字段，建立自己的 "种子字段库"
- 所有后续的高阶变换和组合，都基于这些种子字段展开

不要追求复杂的数学公式，最简单的信号往往最有效。这赛季我多个表现最好的 alpha，都是纯 0 阶的原始字段 rank。

## 4. 123 阶模板其实非常好，是放大信号最好的工具

这是被绝大多数人严重低估的神器。 **123 阶模板是比绝大多数人自己写的高阶模板效果都好** 。

## 5. 123 阶模板生成的 alpha 用 AI 帮助优化

当你用 123 阶模板得到基础 alpha 后，用 AI 进行优化能大幅提高效率。

我常用的 AI 优化方向：

- **参数调优** ：让 AI 在合理范围内遍历窗口大小、权重系数等参数，目标是提高夏普、降低换手率
- **噪声过滤** ：加入流动性过滤、涨跌停过滤、异常值剔除等条件，减少信号噪声
- **特征组合** ：将几个相关性低的基础信号进行加权组合，生成更稳定的复合信号
- **持仓周期优化** ：测试不同调仓频率，找到该信号的最优持仓周期

## 6. 提高自己手搓修正 alpha 性能的能力，自己动手比 AI 快

AI 是工具，但不能代替人的思考。 **手搓 alpha 的能力才是量化顾问的核心竞争力** ，而且在很多关键场景下，自己动手比 AI 快得多。

AI 的局限性在于它不懂信号背后的经济逻辑。当一个信号表现不佳时，AI 只能盲目尝试各种变换，而你可以通过分析市场结构和数据特性，快速定位问题并修正。

我的建议：

- 每天至少花 1 小时手搓 alpha，保持对数据和市场的敏感度
- 深入理解每个信号的经济逻辑，知道它为什么赚钱，什么时候会失效
- 针对不同地区的市场特点，手动调整信号的适用条件

## 7. 1 个月最好只做 2~3 个地区，以 atom 为主，部分数据集需要混量价信号大胆去混

## 8. 提交标准很重要，宁愿少交不要交一堆垃圾

这是最后一条，也是最重要的一条。 **提交垃圾 alpha 不仅浪费你的时间，还会降低你的审核通过率和优先级** 。

我目前提交标准：满足RA基本要求，也就是华子哥插件看过去0fail，近2年指标越高越好，参与ppa主题时pc值是次要标准，更关注alpha本身性能。

以上就是我成为顾问这大半年来总结的 经验。量化没有捷径，AI 能提高效率，但不能代替思考。希望大家都能在赛季末挖到更多优质 alpha，点塔成功！附上6月2号的点塔图，不过我踩了个大坑，6月1号上午发晕交了个asi，给季度结算埋了个大雷，不知道comb分还能不能保住，只能静观其变了。


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GU
> EUR
> CAN
> NOR
> TWNN
> JPN
> AR
> D
> MEA
> anahst
> ol=r
> Earninss
> Fundamsnzs
> Imtslance
> ITIaEr
> Insilin
> Mscro
> N3el
> NEs
> 0otion
> O-her
> Price Vclume
> Fisk
> SEniTET
> ShorIn-eres
> Social Ie3a
  
> [!NOTE] [图片 OCR 识别内容]
> Signals
> 235
> Reached Grandmaster
> 220
> Pyramids Completed
> 60
> Reached Grandmaster
> Combined Alpha Performance
> 2.35
> Reached Grandmaster
> Combined Selected Alpha Performance
> 2.72
> Reached Grandmaster
> Combined Power Pool Alpha Performance
> 1.69
> 0.31 more to Grandmaster
> Combined Osmosis Performance
> -0.21
> 0.71 more to Expert


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

给大佬点赞 这么早就点完了60个塔 combine还这么优秀

这么好的帖子值得一个赞

=============================================================================


---

### 技术对话片段 164 (原帖: 二季度了2个月，和大家分享一些alpha挖掘的思路经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 二季度了2个月和大家分享一些alpha挖掘的思路经验分享_40929650605207.md
- **时间**: 21天前

**提问/主帖背景 (LD22811)**:
2026 年第二赛季已进入收官倒计时，相信大家都在为最后的点塔和赛季排名做最后冲刺。这赛季我在多个地区实战验证，踩过坑也总结出了一套可复制的 alpha 挖掘和点塔方法。今天严格按照自己的工作流，经验分享出来，希望能帮到大家，也欢迎在评论区交流指正。

## 1. 根据华子哥插件和网页的提交数据初步判断优质的数据集和字段

**先筛数据再干活，是所有工作的前提** 。每天早上我会花 30 分钟做数据勘探，绝不盲目写代码。

华子哥插件优先找绿色数据集这是华子哥通过GM权限通过SA筛选ra收集到的数据判断出的优质ALPHA比例高的数据集，其次看适合的中性化

配合网页端提交数据看全局：1.寻找提交较多的数据集/字段，你大概率也可以在这个数据集里找出可提交的alpha；2.寻找新的宇宙/数据集，这里的alpha相关性较低，竞争少。

## 2. AI 帮助生成初始信号

AI 是最高效的初始信号生成器，能帮我们快速扩大信号池。我的使用流程非常明确：

确定优质数据集后，给 AI 输入标准化 prompt：

- 明确要求生成 **0 阶信号** ，仅使用基础变换（rank、ts_rank、delta、log 等）
- 指定地区、数据集和核心字段范围
- 要求 AI 为每个信号附上 **一句话经济逻辑解释**
- 要求输出平台支持的标准语法，可直接复制运行

**关键原则** ：AI 生成的信号 90% 都是垃圾，我们只需要从中筛选出 3-5 个有逻辑、回测基础表现不错的信号，作为后续优化的起点。不要迷信 AI 给出的高夏普，大概率是过拟合。

## 3. 纯粹的 0 阶模板寻找优质字段信号

很多人看不起 0 阶模板，但 **真正能长期稳定的 alpha，80% 都源于 0 阶信号** 。

我常用的0阶段模板：最原始的字段回填\去极值；字段ts_rank；字段AB除法运算；字段AB减法运算。

我的标准操作：

- 对每个新数据集，先跑一遍所有字段的纯 0 阶信号
- 筛选出夏普 > 0.8、fit>0.5的字段，建立自己的 "种子字段库"
- 所有后续的高阶变换和组合，都基于这些种子字段展开

不要追求复杂的数学公式，最简单的信号往往最有效。这赛季我多个表现最好的 alpha，都是纯 0 阶的原始字段 rank。

## 4. 123 阶模板其实非常好，是放大信号最好的工具

这是被绝大多数人严重低估的神器。 **123 阶模板是比绝大多数人自己写的高阶模板效果都好** 。

## 5. 123 阶模板生成的 alpha 用 AI 帮助优化

当你用 123 阶模板得到基础 alpha 后，用 AI 进行优化能大幅提高效率。

我常用的 AI 优化方向：

- **参数调优** ：让 AI 在合理范围内遍历窗口大小、权重系数等参数，目标是提高夏普、降低换手率
- **噪声过滤** ：加入流动性过滤、涨跌停过滤、异常值剔除等条件，减少信号噪声
- **特征组合** ：将几个相关性低的基础信号进行加权组合，生成更稳定的复合信号
- **持仓周期优化** ：测试不同调仓频率，找到该信号的最优持仓周期

## 6. 提高自己手搓修正 alpha 性能的能力，自己动手比 AI 快

AI 是工具，但不能代替人的思考。 **手搓 alpha 的能力才是量化顾问的核心竞争力** ，而且在很多关键场景下，自己动手比 AI 快得多。

AI 的局限性在于它不懂信号背后的经济逻辑。当一个信号表现不佳时，AI 只能盲目尝试各种变换，而你可以通过分析市场结构和数据特性，快速定位问题并修正。

我的建议：

- 每天至少花 1 小时手搓 alpha，保持对数据和市场的敏感度
- 深入理解每个信号的经济逻辑，知道它为什么赚钱，什么时候会失效
- 针对不同地区的市场特点，手动调整信号的适用条件

## 7. 1 个月最好只做 2~3 个地区，以 atom 为主，部分数据集需要混量价信号大胆去混

## 8. 提交标准很重要，宁愿少交不要交一堆垃圾

这是最后一条，也是最重要的一条。 **提交垃圾 alpha 不仅浪费你的时间，还会降低你的审核通过率和优先级** 。

我目前提交标准：满足RA基本要求，也就是华子哥插件看过去0fail，近2年指标越高越好，参与ppa主题时pc值是次要标准，更关注alpha本身性能。

以上就是我成为顾问这大半年来总结的 经验。量化没有捷径，AI 能提高效率，但不能代替思考。希望大家都能在赛季末挖到更多优质 alpha，点塔成功！附上6月2号的点塔图，不过我踩了个大坑，6月1号上午发晕交了个asi，给季度结算埋了个大雷，不知道comb分还能不能保住，只能静观其变了。


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GU
> EUR
> CAN
> NOR
> TWNN
> JPN
> AR
> D
> MEA
> anahst
> ol=r
> Earninss
> Fundamsnzs
> Imtslance
> ITIaEr
> Insilin
> Mscro
> N3el
> NEs
> 0otion
> O-her
> Price Vclume
> Fisk
> SEniTET
> ShorIn-eres
> Social Ie3a
  
> [!NOTE] [图片 OCR 识别内容]
> Signals
> 235
> Reached Grandmaster
> 220
> Pyramids Completed
> 60
> Reached Grandmaster
> Combined Alpha Performance
> 2.35
> Reached Grandmaster
> Combined Selected Alpha Performance
> 2.72
> Reached Grandmaster
> Combined Power Pool Alpha Performance
> 1.69
> 0.31 more to Grandmaster
> Combined Osmosis Performance
> -0.21
> 0.71 more to Expert


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

给大佬点赞 这么早就点完了60个塔 combine还这么优秀

这么好的帖子值得一个赞

=============================================================================


---

### 技术对话片段 165 (原帖: 从垃圾堆中翻出了一个MAPC的Alpha？请重视你生产的每一个Alpha！)
- **原帖链接**: [Commented] 从垃圾堆中翻出了一个MAPC的Alpha请重视你生产的每一个Alpha.md
- **时间**: 8个月前

**提问/主帖背景 (AK76468)**:
今天差点断粮，所以翻了翻垃圾桶，偶然间找到了一个有趣的alpha，表现如下：
 
> [!NOTE] [图片 OCR 识别内容]
> CVIaI (
> Pnl
> 8,0OOK
> 州
> 7,00OK
> OOOK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> -1,00OK
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
> Pnl
> Risk Neutralized Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> IS Summary
> Period
> IS 
> 06
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.67
> 2.029
> 0.54
> 8.179
> 47.229
> 81.09%oo
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.35
> 4.599
> 0.17
> 2.849
> 8.889
> 12.38%00
> 3722
> 2223
> 2014
> 1.78
> 1.669
> 2.12
> 17.66%
> 8.779
> 213.08%o。
> 5119
> 2955
> 2015
> 57
> 1.74%
> 1.91
> 18.43%
> 7.229
> 211.71%o。
> 5256
> 3113
> 2016
> -0.26
> 489
> 0.14
> -3.41%
> 18.73%
> 46_
> 5%oo
> 4999
> 3081
> 2017
> 0.41
> 1.75%
> 0.20
> 2.959
> 7.07%
> 33.80%0。
> 5189
> 3201
> 2018
> 68
> 1.70%
> .94
> 16.59%
> 6.129
> 195.20%o0
> 5616
> 3446
> 2019
> 0.26
> 1.569
> 0.11
> 2.22%
> 9.249
> 28.539o。
> 5034
> 3378
> 2020
> 2.16
> 1.88%
> -3.30
> 29.099
> 36.34%
> 310.28%00
> 5300
> 3436
> 2021
> 1.37
> 2.059
> 1.75
> 20.359
> 12.47%
> 198.23%00
> 6425
> 4197
> 2022
> 94
> 1.54%
> 3.29
> 36.029
> 11.09%
> 466.52%00
> 6097
> 4165
> 2023
> -11.09
> .52%
> 34.74
> -122.659
> 7.80%
> 1,614.93%。
> 5580
> 3703
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.44
> 0.75%
> 0.25
> 4.069
> 35.01%
> 107.99%o。
> APAC
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.70
> 0.839
> 0.36
> 3.249
> 12.11%
> 78.639。
> EMEA
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.42
> 0.449
> 0.11
> 0.879
> 7.279
> 39.73%0。
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.89
> 2.029
> 0.83
> 2.409
> 1.409
> 23.86%。
> I州
 可以看到，无论是总体还是各地区的pnl表现都很差，但是risk pnl很直出奇的好，所以切换中性化为Statistic后表现大幅提升：
 
> [!NOTE] [图片 OCR 识别内容]
> 7,00OK
> 6,0OOK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,0OOK
> 1,00OK
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
> Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> 000
> IS Summary
> Period
> IS 
> 05
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 2.04
> 8.159
> 1.63
> 8.01%
> 12.03%
> 19.66%o。
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.95
> 9.01%
> 0.43
> 2.549
> 2.48%
> 5.6496oo
> 3400
> 2558
> 2014
> 2.93
> 7.789
> 2.51
> 9.16%
> 2.189
> 23.54%o。
> 4624
> 3454
> 2015
> 2.11
> 7.66%
> 1.72
> 8.30%
> 2.21%
> 21.66%o0
> 4803
> 3569
> 2016
> 2.02
> 7.339
> 1.45
> 6.45%
> 2.899
> 17.5890。
> 4641
> 3440
> 2017
> 1.12
> 7.890
> 0.58
> 3.399
> 1.66%
> 8.60%o。
> 4819
> 3576
> 2018
> 3.10
> 8.179
> 2.86
> 10.61%
> 2.099
> 25.96%o。
> 5194
> 3875
> 2019
> 2.81
> 7.499
> 2.36
> 8.839
> 1.67%
> 23.579600
> 4835
> 3579
> 2020
> -1.23
> 8.379
> 0.87
> -6.329
> 9.549
> -15.10%oo
> 4990
> 3749
> 2021
> 2.24
> 8.7796
> 2.10
> 10.949
> 4.299
> 24.96%o0
> 6002
> 4627
> 2022
> 5.12
> 7.66%
> 7.16
> 24.429
> 1.959
> 63.76900
> 5937
> 4331
> 2023
> 0.98
> 7.66%
> 0.86
> 9.679
> 2.189
> 25.23%00
> 5350
> 3934
> AMER
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.33
> 3.34%
> 0.74
> 3.870
> 10.80%
> 23.1790。
> APAC
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.97
> 3.069
> 1.04
> 3.509
> 1.61%
> 22.90%oo
> EMEA
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.66
> 1.75%
> 0.15
> 0.649
> 3.509
> 7.3590。
> UMMZ
> Year
 但EUR sharpe仍有不足，后面从alpha idea的角度对数据进行了进一步处理：

- 原字段代表某ETF相对于其基准指数的每日残差return，可以体现有没有跑赢基准指数。
- 原Alpha的信号：用标准差衡量了该字段时序上的稳定程度，是否有稳定的跑赢基准指数？然后再按country分组求zscore。

我尝试的改进方式是：对过去一个季度的标准差进行滚动求和（ts_sum），以降低短期波动带来的噪声，从而衡量“是否能在较长时间内持续稳定跑赢基准”。尽管这个调整有一定尝试成分，但结果确实带来了提升。之后，我再基于（country + cap）进行双重中性化，最终得到了更优的表现，并成功提交为 MAPC alpha。
 
> [!NOTE] [图片 OCR 识别内容]
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
> OOOK
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
> IS Summary
> Period
> IS
> OS
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: GLBIDI/PV X1
> Pyramid theme: GLB/DI/MACRO X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.60
> 9.069
> 1.84
> 6.259
> 5.429
> 13.80%o。
> Year
>  Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.24
> 8.109
> 1.26
> 3.94%
> 1.37%
> 9.7290
> 3350
> 2608
> 2014
> 3.26
> 8.999
> 2.37
> 6.589
> 0.979
> 14.64%o。
> 4497
> 3580
> 2015
> 1.92
> 8.749
> 1.18
> 4.73%
> 1.429
> 10.82900
> 4650
> 3722
> 2016
> 3.85
> 8.719
> 3.05
> 7.82%
> 1.0596
> 17.9496o0
> 4505
> 3576
> 2017
> 1.13
> 8.3896
> 0.45
> 1.9796
> 0.9796
> 4.70900
> 4705
> 3690
> 2018
> 3.25
> 8.859
> 2.42
> 6.92%
> 0.989
> 15.65%0。
> 5112
> 3957
> 2019
> 4.16
> 8.199
> 3.36
> 8.15%
> 1.0096
> 19.90%o。
> 4656
> 3758
> 2020
> 0.26
> 9.769
> 0.07
> 0.80%
> 5.01%
> 1.6490。
> 4899
> 3839
> 2021
> 2.69
> 9.839
> 1.97
> 6.70%
> 1.489
> 13.64%0。
> 5871
> 4758
> 2022
> 4.88
> 9.389
> 5.29
> 14.71%
> 1.389
> 31.379o。
> 5629
> 4639
> 2023
> 0.72
> 9.349
> 0.48
> 5.53%
> 1.66%
> 11.84%o。
> 5105
> 4179
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.68
> 3.759
> 0.82
> 2.959
> 4.389
> 15.76%0。
> APAC
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.21
> 3.24%
> 1.02
> 2.679
> 1.339
> 16.53%0。
> EMEA
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.02
> 2.079
> 0.23
> 0.629
> 1.56%
> 5.989o。


从这次经验可以看出，如果仅依赖单一指标（如 Sharpe）作为筛选条件，很容易遗漏一些风险属性优秀、经调整后表现突出的 alpha。建议在进行 alpha 筛选和剪枝时，要充分结合风险表现来综合判断。

另外，结合之前会议上提到的“将GLB中在子区域表现优异的 alpha 单独在该区域回测”的思路，我们也可以将Risk pnl表现较好的 alpha，重新在 Risk 中性化设定下进行回测，以发掘更多潜在的有效因子。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=======================================

感谢大佬分享，又学到了一个小技巧

不过我目前能交到MAPC比赛的GLB alpha operator/datafield都很多，生怕交完影响本季度Genius排名，只能等十一之后再交了

=================================================================================


---

### 技术对话片段 166 (原帖: 从垃圾堆中翻出了一个MAPC的Alpha？请重视你生产的每一个Alpha！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 从垃圾堆中翻出了一个MAPC的Alpha请重视你生产的每一个Alpha_35244554775319.md
- **时间**: 8个月前

**提问/主帖背景 (AK76468)**:
今天差点断粮，所以翻了翻垃圾桶，偶然间找到了一个有趣的alpha，表现如下：
 
> [!NOTE] [图片 OCR 识别内容]
> CVIaI (
> Pnl
> 8,0OOK
> 州
> 7,00OK
> OOOK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> -1,00OK
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
> Pnl
> Risk Neutralized Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> IS Summary
> Period
> IS 
> 06
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.67
> 2.029
> 0.54
> 8.179
> 47.229
> 81.09%oo
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.35
> 4.599
> 0.17
> 2.849
> 8.889
> 12.38%00
> 3722
> 2223
> 2014
> 1.78
> 1.669
> 2.12
> 17.66%
> 8.779
> 213.08%o。
> 5119
> 2955
> 2015
> 57
> 1.74%
> 1.91
> 18.43%
> 7.229
> 211.71%o。
> 5256
> 3113
> 2016
> -0.26
> 489
> 0.14
> -3.41%
> 18.73%
> 46_
> 5%oo
> 4999
> 3081
> 2017
> 0.41
> 1.75%
> 0.20
> 2.959
> 7.07%
> 33.80%0。
> 5189
> 3201
> 2018
> 68
> 1.70%
> .94
> 16.59%
> 6.129
> 195.20%o0
> 5616
> 3446
> 2019
> 0.26
> 1.569
> 0.11
> 2.22%
> 9.249
> 28.539o。
> 5034
> 3378
> 2020
> 2.16
> 1.88%
> -3.30
> 29.099
> 36.34%
> 310.28%00
> 5300
> 3436
> 2021
> 1.37
> 2.059
> 1.75
> 20.359
> 12.47%
> 198.23%00
> 6425
> 4197
> 2022
> 94
> 1.54%
> 3.29
> 36.029
> 11.09%
> 466.52%00
> 6097
> 4165
> 2023
> -11.09
> .52%
> 34.74
> -122.659
> 7.80%
> 1,614.93%。
> 5580
> 3703
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.44
> 0.75%
> 0.25
> 4.069
> 35.01%
> 107.99%o。
> APAC
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.70
> 0.839
> 0.36
> 3.249
> 12.11%
> 78.639。
> EMEA
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.42
> 0.449
> 0.11
> 0.879
> 7.279
> 39.73%0。
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.89
> 2.029
> 0.83
> 2.409
> 1.409
> 23.86%。
> I州
 可以看到，无论是总体还是各地区的pnl表现都很差，但是risk pnl很直出奇的好，所以切换中性化为Statistic后表现大幅提升：
 
> [!NOTE] [图片 OCR 识别内容]
> 7,00OK
> 6,0OOK
> 5,00OK
> 4,00OK
> 3,00OK
> 2,0OOK
> 1,00OK
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
> Pnl
> AMER Pnl
> APAC Pnl
> EMEA Pnl
> 000
> IS Summary
> Period
> IS 
> 05
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 2.04
> 8.159
> 1.63
> 8.01%
> 12.03%
> 19.66%o。
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.95
> 9.01%
> 0.43
> 2.549
> 2.48%
> 5.6496oo
> 3400
> 2558
> 2014
> 2.93
> 7.789
> 2.51
> 9.16%
> 2.189
> 23.54%o。
> 4624
> 3454
> 2015
> 2.11
> 7.66%
> 1.72
> 8.30%
> 2.21%
> 21.66%o0
> 4803
> 3569
> 2016
> 2.02
> 7.339
> 1.45
> 6.45%
> 2.899
> 17.5890。
> 4641
> 3440
> 2017
> 1.12
> 7.890
> 0.58
> 3.399
> 1.66%
> 8.60%o。
> 4819
> 3576
> 2018
> 3.10
> 8.179
> 2.86
> 10.61%
> 2.099
> 25.96%o。
> 5194
> 3875
> 2019
> 2.81
> 7.499
> 2.36
> 8.839
> 1.67%
> 23.579600
> 4835
> 3579
> 2020
> -1.23
> 8.379
> 0.87
> -6.329
> 9.549
> -15.10%oo
> 4990
> 3749
> 2021
> 2.24
> 8.7796
> 2.10
> 10.949
> 4.299
> 24.96%o0
> 6002
> 4627
> 2022
> 5.12
> 7.66%
> 7.16
> 24.429
> 1.959
> 63.76900
> 5937
> 4331
> 2023
> 0.98
> 7.66%
> 0.86
> 9.679
> 2.189
> 25.23%00
> 5350
> 3934
> AMER
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.33
> 3.34%
> 0.74
> 3.870
> 10.80%
> 23.1790。
> APAC
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 1.97
> 3.069
> 1.04
> 3.509
> 1.61%
> 22.90%oo
> EMEA
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> 0.66
> 1.75%
> 0.15
> 0.649
> 3.509
> 7.3590。
> UMMZ
> Year
 但EUR sharpe仍有不足，后面从alpha idea的角度对数据进行了进一步处理：

- 原字段代表某ETF相对于其基准指数的每日残差return，可以体现有没有跑赢基准指数。
- 原Alpha的信号：用标准差衡量了该字段时序上的稳定程度，是否有稳定的跑赢基准指数？然后再按country分组求zscore。

我尝试的改进方式是：对过去一个季度的标准差进行滚动求和（ts_sum），以降低短期波动带来的噪声，从而衡量“是否能在较长时间内持续稳定跑赢基准”。尽管这个调整有一定尝试成分，但结果确实带来了提升。之后，我再基于（country + cap）进行双重中性化，最终得到了更优的表现，并成功提交为 MAPC alpha。
 
> [!NOTE] [图片 OCR 识别内容]
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
> OOOK
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
> IS Summary
> Period
> IS
> OS
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: GLBIDI/PV X1
> Pyramid theme: GLB/DI/MACRO X1.3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.60
> 9.069
> 1.84
> 6.259
> 5.429
> 13.80%o。
> Year
>  Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 2.24
> 8.109
> 1.26
> 3.94%
> 1.37%
> 9.7290
> 3350
> 2608
> 2014
> 3.26
> 8.999
> 2.37
> 6.589
> 0.979
> 14.64%o。
> 4497
> 3580
> 2015
> 1.92
> 8.749
> 1.18
> 4.73%
> 1.429
> 10.82900
> 4650
> 3722
> 2016
> 3.85
> 8.719
> 3.05
> 7.82%
> 1.0596
> 17.9496o0
> 4505
> 3576
> 2017
> 1.13
> 8.3896
> 0.45
> 1.9796
> 0.9796
> 4.70900
> 4705
> 3690
> 2018
> 3.25
> 8.859
> 2.42
> 6.92%
> 0.989
> 15.65%0。
> 5112
> 3957
> 2019
> 4.16
> 8.199
> 3.36
> 8.15%
> 1.0096
> 19.90%o。
> 4656
> 3758
> 2020
> 0.26
> 9.769
> 0.07
> 0.80%
> 5.01%
> 1.6490。
> 4899
> 3839
> 2021
> 2.69
> 9.839
> 1.97
> 6.70%
> 1.489
> 13.64%0。
> 5871
> 4758
> 2022
> 4.88
> 9.389
> 5.29
> 14.71%
> 1.389
> 31.379o。
> 5629
> 4639
> 2023
> 0.72
> 9.349
> 0.48
> 5.53%
> 1.66%
> 11.84%o。
> 5105
> 4179
> AMER
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.68
> 3.759
> 0.82
> 2.959
> 4.389
> 15.76%0。
> APAC
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.21
> 3.24%
> 1.02
> 2.679
> 1.339
> 16.53%0。
> EMEA
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.02
> 2.079
> 0.23
> 0.629
> 1.56%
> 5.989o。


从这次经验可以看出，如果仅依赖单一指标（如 Sharpe）作为筛选条件，很容易遗漏一些风险属性优秀、经调整后表现突出的 alpha。建议在进行 alpha 筛选和剪枝时，要充分结合风险表现来综合判断。

另外，结合之前会议上提到的“将GLB中在子区域表现优异的 alpha 单独在该区域回测”的思路，我们也可以将Risk pnl表现较好的 alpha，重新在 Risk 中性化设定下进行回测，以发掘更多潜在的有效因子。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=======================================

感谢大佬分享，又学到了一个小技巧

不过我目前能交到MAPC比赛的GLB alpha operator/datafield都很多，生怕交完影响本季度Genius排名，只能等十一之后再交了

=================================================================================


---

### 技术对话片段 167 (原帖: 低成本使用ai，助力回测！经验分享)
- **原帖链接**: [Commented] 低成本使用ai助力回测经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (JZ85816)**:
写这篇帖子的初衷在于笔者用好模型尝到了甜头。

从以前的opus到gpt-5.3-codex，到现在的低成本或者零成本畅用gpt5-4，个人体感opus4-6>gpt5.4>5.3-codex，由于现在opus的渠道不好找而且价格比较贵，所以下文只说明gpt5-4的低成本获取方法。

1. 可以去网上或者某鱼搜索公益站或者gpt这类关键词。不建议多买，建议少次尝鲜，因为现阶段有注册机的存在所以多数gpt是零成本的。

2. 如果你有多个公益gpt的站点的话来回切换不方便的话，可以使用octopus这个项目进行统一的对api进行中转。GitHub地址： [[链接已屏蔽])

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

但用公益站之类的总怕被恶意注入代码然后获取凭证之类的

这一点还是要小心的

=============================================================================


---

### 技术对话片段 168 (原帖: 低成本使用ai，助力回测！经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 低成本使用ai助力回测经验分享_39565397650839.md
- **时间**: 2个月前

**提问/主帖背景 (JZ85816)**:
写这篇帖子的初衷在于笔者用好模型尝到了甜头。

从以前的opus到gpt-5.3-codex，到现在的低成本或者零成本畅用gpt5-4，个人体感opus4-6>gpt5.4>5.3-codex，由于现在opus的渠道不好找而且价格比较贵，所以下文只说明gpt5-4的低成本获取方法。

1. 可以去网上或者某鱼搜索公益站或者gpt这类关键词。不建议多买，建议少次尝鲜，因为现阶段有注册机的存在所以多数gpt是零成本的。

2. 如果你有多个公益gpt的站点的话来回切换不方便的话，可以使用octopus这个项目进行统一的对api进行中转。GitHub地址： [[链接已屏蔽])

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

但用公益站之类的总怕被恶意注入代码然后获取凭证之类的

这一点还是要小心的

=============================================================================


---

### 技术对话片段 169 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: [Commented] 作为一个gold级别的新人我是怎么点满60个塔经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (LD22811)**:
我是11月18日成为顾问的新人，2025Q4有42天时间，交数量倒是满足MS级别了，但是12月的comb分0分，VF由于11月不够20天没有出分。提交的alpha质量应该是好坏都有，当时很多知识都不了解，胡乱提交的。

2026年1月我之前发了一个 [PPA活动主题限制下，提交ra点塔的一点心得。 – WorldQuant BRAIN]([Commented] PPA活动主题限制下提交ra点塔的一点心得.md) 帖子，alpha提交策略成熟了一些，1月comb也刷新到了1.49，VF第一次出分0.80。 
> [!NOTE] [图片 OCR 识别内容]
> Gsnius level: Gold
> I TTJC' Gol
> CUTtCUTCTCni: NIrh3151 2026
> Eligibility Criteria
> 7026 41.Iru 15t 2036
> Irc31s 2036
> S
> nr
> TTFTTm
> Sgnals
> 249
> Rached Crrdmrl
> Pramids ComPersJ
> Rached Crrdmrl
> TONh NS
> Alha Performance
> 1.49
> 151 TJr
> ITTam
> Combined Selected Alpha Performance
> TRNCT「CICCTR
> CombnsJ Fower PoolAlpha Ferforman-s
> 0.45
  
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2026-01,January 155 2026
> March 315t, 2026
> Cateyon
> U5
> GU
> EUR
> CHN
> NOOR
> TN
> Anayys
> 3O =
> Earr nEs
> FundaTsTts
> ImTaIT=
> IO
> Inaions
> a
> Idsl
> Nsws
> Cation
> Dher
> Price Volune
> Ris
> TTmn
> SorIntsrsst
> Sciallls-la


3月5日我的点塔数也60个了，达到了GM标准，看了华子哥插件是国区第4达标的，全球前十也只有我是个小GOLD，许愿马上刷新的comb分能上2.0。

主要经验是多做RA，跟活动的话交优质ppa，ppa就别太关注pc了。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬太强了  真点塔速度可以说超级惊人了

祝福大佬早日GM！

===================================================================================


---

### 技术对话片段 170 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 作为一个gold级别的新人我是怎么点满60个塔经验分享_38844379720727.md
- **时间**: 3个月前

**提问/主帖背景 (LD22811)**:
我是11月18日成为顾问的新人，2025Q4有42天时间，交数量倒是满足MS级别了，但是12月的comb分0分，VF由于11月不够20天没有出分。提交的alpha质量应该是好坏都有，当时很多知识都不了解，胡乱提交的。

2026年1月我之前发了一个 [PPA活动主题限制下，提交ra点塔的一点心得。 – WorldQuant BRAIN]([Commented] PPA活动主题限制下提交ra点塔的一点心得_38121310515223.md) 帖子，alpha提交策略成熟了一些，1月comb也刷新到了1.49，VF第一次出分0.80。 
> [!NOTE] [图片 OCR 识别内容]
> Gsnius level: Gold
> I TTJC' Gol
> CUTtCUTCTCni: NIrh3151 2026
> Eligibility Criteria
> 7026 41.Iru 15t 2036
> Irc31s 2036
> S
> nr
> TTFTTm
> Sgnals
> 249
> Rached Crrdmrl
> Pramids ComPersJ
> Rached Crrdmrl
> TONh NS
> Alha Performance
> 1.49
> 151 TJr
> ITTam
> Combined Selected Alpha Performance
> TRNCT「CICCTR
> CombnsJ Fower PoolAlpha Ferforman-s
> 0.45
  
> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2026-01,January 155 2026
> March 315t, 2026
> Cateyon
> U5
> GU
> EUR
> CHN
> NOOR
> TN
> Anayys
> 3O =
> Earr nEs
> FundaTsTts
> ImTaIT=
> IO
> Inaions
> a
> Idsl
> Nsws
> Cation
> Dher
> Price Volune
> Ris
> TTmn
> SorIntsrsst
> Sciallls-la


3月5日我的点塔数也60个了，达到了GM标准，看了华子哥插件是国区第4达标的，全球前十也只有我是个小GOLD，许愿马上刷新的comb分能上2.0。

主要经验是多做RA，跟活动的话交优质ppa，ppa就别太关注pc了。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬太强了  真点塔速度可以说超级惊人了

祝福大佬早日GM！

===================================================================================


---

### 技术对话片段 171 (原帖: 使用Mac系统跑App_wqb || App_0715 (BRAIN Expression Template Decoder)经验分享)
- **原帖链接**: [Commented] 使用Mac系统跑App_wqb  App_0715 BRAIN Expression Template Decoder经验分享.md
- **时间**: 10个月前

**提问/主帖背景 (CM48632)**:
## 在Mac系统上面跑 **App_wqb** 的两种方式（1）

### 1 将 App_wqb 部署到云电脑

#### 1.1 安装python环境

[VSCODE（必须，不解决因为使用其它环境而遇到的error） + Python 3.12 以上版本（vscode+python+jupyter环境搭建_哔哩哔哩_bilibili ）]([链接已屏蔽])

如果单一跑App_wqb，安装python环境就可以；跑代码，就按视频安装运行环境即可。

#### 1.2 运行App_wqb


> [!NOTE] [图片 OCR 识别内容]
> 0715
> X
> 文件
> `
> ~^查看
> 这台脑
> 文栏
> APP_0715
> @
> 掼紊"APP_0715"
> 0
> 名称
> 咨改曰期
> 奖型
> 大小
> 收蘅夹
> 下载
> blueprints
> 2025/7/2910;:39
> 文件夹
> 卓
> custom_templates
> 2025/7/517;52
> 文件夹
> 冕丘访闩钓位置
> ResultBuilder
> 2025/7/623:55
> 文件夹
> simulator
> 2025/7/1518:22
> 文件夹
> static
> 2025/7/103:19
> 文件夹
> 这台宅肫
> templates
> 2025/7/10 3:18
> 文件奕
> CharlesdeMacBoo
> 'gitignore
> 2025/7/517:52
> GITIGNORE 文件
> 1KB
> 视频
> mirror_config
> 2025/7/221;50
> 文太文档
> 1<8
> 图斤
> MODULAR_STRUCTURE.md
> 2025/7/311:30
> MD 文件
> 5KB
> 文栏
> READMEmd
> 2025/7/221:51
> MD 文件
> 12<3
> 下裁
> requirements
> 2025/7/92:11
> 文太文档
> 1KB
> 音乐
> run_app
> 2025/7/221:44
> Windows 批处理
> 1<8
> 桌
> run
> _app.sh
> 2025/7/221:44
> SH 文件
> 1<8
> 本圯磁盏 (C:)
> setup_tsinghua
> 2025/7/221:49
> Windows 批处理
> 2 (8
> 直接
> setup_tsinghua.sh
> 2025/7/221:49
> SH 文件
> 2<8
> 用鼠标双击
> 运行打开2
> 2025/7/104;11
> Python File
> 54KB
> 网咨
> 运行程序
> 16个项目
> 选中1个项目  53.3 KB
> APP_


运行结果，如下图所示：


> [!NOTE] [图片 OCR 识别内容]
> 又
> C:IWindowslpy.exe
> Collecting
> referencing > =0.28
> 4 <from
> jsonschema >=4.18
> 囚->jupyterlah-seryer<3>=2
> 22.1>notehook>=7.0.0->
> C: Wsers Ydministrator Vocuments Mpp_O715 Wequirement
> tXt
> Iine
> 15〉〉
> Downloading https: //nypi.tuna .tsinghua
> edu.cn /pac kages /c1/h173haf8O4c642h2hc2?1
> 89546225240208e410351e3feh4eh284e5f2745448a/referencing-囚.36
> 2-093-none-any.Whl
> 26
> K〉
> Collecting rpds-Py>=0.?.1
> Cfrom jsonschema〉=4.18 .囚->jupyterIah-seruer<3,>=2
> 27.1
> >notehook>=7 .0.囚>r
> C: Wsers Vdministrator <ocuments Mpp_O715 Wequirements .txtl
> 〈line
> 15〉〉
> Downloading https: //pypi.tuna .tsinghua .edu.cn /packages /94/c1/3c8c94c7aa3905ak
> He
> 268381c698228500a8041992423148?adcdh11?e9 /rpds _Py-0.26 .O-cp3l1-Cp311-win_amd64
> Whl
> <231
> J〉
> 231.27231 ?
> RB2 &
> 0s
> eta
> 囚:}:}
> Collecting
> python-json-Iogger >=2 .0.4
> Cfrom jupyter-euents> =囚.11 .囚->jupyter-serue
> 〈3〉2.4.0->notehook>=? .0.囚>r
> C: Wsers Ydministrator Wocuments Vpp_O715 Wequi
> Iements .txt
> 〈Iine
> 15〉〉
> Down loading
> https : / /pypi.tuna .ts inghua .edu.cn/pac kages /08/20/0f252319e50a8052h
> c6a812324fc8568ahhdc42010aef03a24750hdah3h2 /python_json_logger-3.3 .O-Py3-none-an
> 4.wl
> 〈15
> K〉
> Collect
> Dyyaml>=5.3
> 〈from
> jupyter-events > =0.11 .囚->jupyter-seryer<3,>=2.4.0-
> otehook>=7 .囚.囚>
> C: Wsers Vdministrator Documents
> _8715 Wequirements .txt
> (1
> ine
> 15〉
> Downloading https: / /pypi. tuna .tsinghua
> edu.cn/pac kages /e/23/8aaOhhe2ah9dcaall
> f4f455?ccaf 95c10h9811h13ecced089443ce59c3c8/PyyAlL-6 .0.2-cp311-cp311-win_ama6 4 .w
> h1
> (161
> KB〉
> ing
> Ypp
  
> [!NOTE] [图片 OCR 识别内容]
> 又
> C:lWindowslpy.exe
> Start
> BRAIN Expression
> Template
> Decoaer
> Neh
> Application
> Application
> 4il1
> Iun
> On
> http: //localhost :5000
> BRAIN API
> integration
> incIudea
> 00
> separate
> Doxy
> needea!
> 天
> Seruing
> Flask
> app
> '运行打开找'
> 升
> Dehug
> mode:
> 0n
> INRO :werkzeug : < [31mc [ImNARNING:
> This
> is
> deueIopment
> Seryer .
> Do
> n0t
> USe
> i
> i
> production
> aeployment
> Use
> production
> NSGI
> SeHUer
> instead.[Gm
> Runnin
> On
> a11
> addresgeg
> 〈_囚_囚
> Runn
> 00
> http: /7127 .囚.囚.1:5000
> 表示程序
> Runn
> 0n
> http: /710.1 .囚.2:5000
> 成功运行
> INFOEwerkzewg:F [33mPress
> CTRITC
> To
> quitt [Bm
> INRO :werkzeug:
> 夫 Restart
> win
> stat
> Initializing
> BRAIN Expression
> Template
> Decoaer
> Checking
> ana
> installing required
> aependencies
> Uerifying
> packages
> needea
> for
> BRAIN Expression
> Template
> Decoder .
> All required dependencies
> are
> already
> installea!
> Core
> packages
> importea
> SUCCeSSfulIy!
> Flask application
> iiiali2ea
> With CORS support!
> BRAIN API
> integration
> configurea!
> Blueprints
> iportea
> SUCCeSSfully!
> All hlueprints registered successfully!
> Idea
> House:
> /iaea-house
> Paper Analysis:
> /aper-analysis
> Peature
> Engineering:
> /feature-engineering
> Templates
> airectory
> reaay:
> C: Wsers Vdministrator WDocuments
> 0715 Custom
> 七
> ing
> ing
> ing
> ing
> YDD


#### 1.3 配置 防火墙


> [!NOTE] [图片 OCR 识别内容]
> 开始
> 服务器管理器
> 这台电脑
> 桌
> a
> 任务笞器
> 控制面板
> 开始里面找到
> 控制面板
> 3
> Intemet
> Explorer
> 笞理工具
> 文件资源笞理器
  
> [!NOTE] [图片 OCR 识别内容]
> 控制面板
> 又
> 控~面板
> @
> 掼烹控司面旅
> O
> 调整计算机的设置
> 查看方式:
> 类别
> 点击
> 系统和安全
> 系统和安全
> 用户帐户
> 竺窄你闪讦舁利状态
> 更改帐户类型
> 查看事件曰志
> 外观
> 网络和 Internet
> 更改s面背|
> 查看网络状态和任务
> 湄整异莓分辨率
> 硬件
> 时钟。语言和区域
> 查看设a和打印机
> 添加语言
> 添加设a
> 更换菊入法
> 设置时闫和日期
> 程序
> 更改8期。时闫或效字格式
> '款程
> 启用或关闭 Windows 功能
> 轻松使用
> 使乐 Windows 建议钓设置
> 优化视觉显示
  
> [!NOTE] [图片 OCR 识别内容]
> 系统和安全
> 又
> 控剖面板
> 系统和安全
> 掼烹控司面旅
> 0
> 控制面板F页
> 操作中心
> 系统和安全
> 检查计算机竹状态并解夫问题
> 更改用户帐户控制设置
> 常见计算机问题疑难解笞
> 网咨和 Internet
> Windows 防火墙
> 点击 Windows 防火墙
> 硬件
> 芒状悉
> 元识用通过 Windows 防火培
> 程序
> 系统
> 用户帐户
> 查看 RAM 的太小和处理器速度
> 允许远裎访问
> 启动远程办卧
> 查看该计算机的名称
> 外观
> Windows 更新
> 时钟 
> 浯言和区域
> 启用或关闭刍动更新
> 检查更新
> 安荒可选更新
> 查看更新历史记录
> 羟松使用
> 电源选项
> 唤d计算机时需要宓码
> 更改孑源按钮的功能
> 更改计算机愆眠时闫
> 管理工具
> 对你的驱动器迸行碎片整理和优化
> 刽建并袼式化硬盏分区
> 查看事件巳志
> 计划任务
> 生成系统徒恚报告
  
> [!NOTE] [图片 OCR 识别内容]
> Windows 防火墙
> 又
> 控~面板
> 系统和安全
> Windows 防火垲
> @
> 掼烹控司面旅
> 0
> 使用 Windows 防火墙来帮助保护你的电脑
> 控制面板F页
> Windows 防火垲有劢于防止黑客或恶套软件通过 Internet 或网络访问你的。脑。
> 允许应用或功能通过 Windows
> 防火培
> 更新防火垲设置
> 更改通知设置
> Windows 防火培末使用荏荐竹设置宋屎扩计等
> 使用准荐设置
> 启用或关闭 Windows 防火垲
> 还原默认值
> 推荐竹设置有绑些?
> 言级设置
> ~网咨逆行疑难解笞
> 专用网络(R)
> 末连接
> 来宾或公用网络(P)
> 已连接
> 点击
> 公共场所(囹如机场或吮啡卣中的网络
> 高级设置
> Windows 防火垲状态:
> 关闭
> 传入洼接:
> 阻止所有与末在允许应用列表中的应用的连接
> 活动的公用网络:
> 网咨
> 通知状态:
> Windows 防火培阻止新应用时不要通知我
> 另清参阅
> 蒺作心
> 网绐和共享中心
> 机。
  
> [!NOTE] [图片 OCR 识别内容]
> 高级安全 Windows 防火墙
> 又
> 文件(9
> -作(4)
> 查0
> 帮卧(H)
> 本圯计算机  上的啬级安全 Win
> 本地计算机 _上的高级安全 Windows 防火墙
> 操作
> 人'厕
> 本地计算机_上的高级安全 Wind。
> 出规则
> 高级安全 indows 防火墙为 'Hindows 计算机提供网络安全。
> 导入策晗。
> 竺规则
> 导策略。
> 槲述
> 还原默认策骆
> 域配罡文卅
> 诊断1佟复
> Hindows 防火墙己关闭。
> 查看
> 点击
> 专用配罡文卅
> 添加
> Windows 防火墙己关闭。
> 刷新
> 入
> 出站规则
> 唇 
> 公用配罡文件是活动的
> 帮卧
> #indows 防火墙己关闭。
> Nindows 防火墙属性
> 开始
> 计算机之间的身份验证通信
> 巢?性狈则#定傅用
> Internet
> 协议安全性 (IFSec)对计算机之间的连接进行身份验证和保护的
> 连接安全规则
> 查看和创建防火墙规则
> (篝[(默鼹:
> 匹配阻止它们的规则)
> 谮:[熨鳖毽;群?颛影
> 入站规则
> 出规则
> 查看当前防火墙以及
> IPseC
> 策略和活动
> 查看有关当前应用的防火墙与连接安全性规则和活~网络连接的安全关联的信息
> 导入策(.
  
> [!NOTE] [图片 OCR 识别内容]
> 高级安全 Windows 防火墙
> x
> 文件(
> -作(A)
> 查0
> 帮卧(H)
> 杰地让簋机上的啬级安全 Win
> 入站规则
> 操作
> 入站则
> 名称
> 配置文件
> 己启用
> 入站规则
> 弋末/贝
> wqbSooOin
> 是
> 新建规则.
> 连接安全=则
> BranchCache 对等机出玑0NSOulol
> BrancbCacbe
> 0竽t 皿
> E左
> 歪
> 监视
> BranchCache 内容枇
> 新建入站规则向导
> 义
> BranchCache 托管?
> 规则类型
> 第一步
> COMt 网络访问(04
> 选择要创建的防火墙规则类型
> COMt 远程管理(D4
> 第二步
> iSCSI 珉务(TCP-In)
> 步骤:
> Netlogon 服务(NP
> 规则类型
> 要创建的规则类型
> Netlogon 服务菝枫
> 协议和端0
> SMBDirect (iWARPI
> 程席()
> 操作
> 控制程席连掊的@则。
> SNMP
> Senricl
> SNMP
> Senicl
> 配罡文件
> 端口()
> 第三步
> TPM 奁拟智能卡笞
> 名称
> 控制 TCP 或 IF 端口连接的规则
> TPM 奁拟智能卡笞
> 璇叉():
> TPM 奁拟鹤卡c
> Bracllache
> 对等机发现 (使用 S0)
> TPM 奁拟智能卡笞
> 控制 indos 体验功能连接的规则=
> Windows Manage
> 自定义()
> Windows Manage
> 自定义规则
> Windows Manage
> SCW 远程访问防炒
> SCW 远程访问防刈
> SCW 远程访问防炒
> Windows 防火垲远
> 第四步
> Windows 防火垲远
> Windows 远程管璁
> 14T
> 〈上步(6)
> 下-步(玎) >
> 取消
> 所
> Trap
> Trap
  
> [!NOTE] [图片 OCR 识别内容]
> 新建入站规则向导
> 义
> 协议和端口
> 指定应用此规则的协议和端0
> 步骤:
> 此趄则应围于 ICP 还是 I?
> 规则类型
> 协议和端0
> TCP
> UDP
> 操作
> 配罡文件
> 此规则应用于所有本地端口还是特定的本地端口?
> 名称
> 所有本坳端0(A)
> 特定本血端0(S):
> SOOO
> 1 .
> 443,
> 5000-5010
> <
> 上一步{)
> 下步{)
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 又
> 新建入站规则向导
> 操痄
> 指定茌连接与规则中指定的条件相匹配时要执行的操作。
> 步骤:
> 规则类型
> 连接符合指定条件时应该进行什么操作?
> 协议和端口
> 允许连接(A)
> 操作
> 包括使用 IFsec 保护的连接。以及未使用 IFsec 保护的连接。
> 配罡文件
> 只允许安全连接(C)
> 名称
> 墨踅婺望粼燮s4 -
> IPseo
> 连攘的安全性将依照 IFsec 属性中的设
> [到保障。
> 自定义
> 阻止连接(
> 上一步{)
> 下-步()
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 新建入站规则向导
> 义
> 配罡文#
> 指定此规则应用的配罡文件
> 步骤:
> 规则类型
> 何时应用该规则?
> 协议和端0
> 域(0)
> 操作
> 计簋机连接到甚企业域时应围。
> 配罡文件
> 专用
> 名称
> 计算机连接到专用网络位蛊(例如;  家或工作单位)时应用
> 公用(U)
> 计算机连接到公用网络位蛊时应用:
> 上步(6})
> 下步{)
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 新建入站规则向导
> 义
> 名称
> 指定此规则的名称和描述。
> 步骤:
> 规则类型
> 协议和端口
> 操作
> 名称(+) =
> 配罡文件
> HQb50OOir
> 名称
> 描述(可选)(D):
> 上步{)
> 完成()
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 高级安全 Windows 防火墙
> 又
> 文件(9
> -作(4)
> 查0
> 帮卧(H)
> 本地计算机 _上的啬级安全 Win
> 入站规则
> 操作
> 入站则
> 沮
> 配置文件
> 己启用
> 入站规则
> 己站规则
> WqbSOOOin
> 所有
> 是
> 新建规则.
> 连接安全规则
> Branchcache 对等机发现(SD-In)
> BranchCache
> 对等机发现。.
> 所
> 监视
> 7
> 按=置文件筛选
> BranchCache 囚容检紊(HTTP-In)
> BranchCache
> 内容检亵(
> 所有
> 吾
> 了
> 按状态筛选
> BranchCache 托笞缓存服务器(HTTP-In)
> BranchCache
> 托管缓存屐
> 所有
> 按组筛选
> COMt 网络访问(DCOM-In)
> COMt 网络访问
> 所有
> 否
> COMt 远程管理(DCOM-In)
> COMt 远程管理
> 所有
> 否
> 查看
> iSCSI 服务(TCP-In)
> iSCSI 屐务
> 否
> 刷新
> Netlogon 服务(NP-In)
> Netlogon 服务
> r
> 否
> 导列表。
> Netlogon 服务菝权(RPC)
> Netlogon 股务
> 否
> 帮卧
> SMBDirect (WARP-In)上的文件和打印。
> SMBDirect 上钓文件和打印。
> 所有
> 否
> SNMP
> Serice (UDP In)
> SNMP
> 咸
> 否
> wqbsoooin
> SNMP
> Serice (UDP In)
> SNMP
> 专用;公用
> 否
> 禁#斯则
> TPM 虚拟智能卡管理(DCOM-In)
> TPM 奁拟智能卡笞理
> 域
> 否
> 剪切
> TPM 奁拟智能卡答理(DCOM-In)
> TPM 虑拟昝能卡邕理
> 专用;公用
> 否
> 妄制
> TPM 奁拟智能卡笞理(TCP-In)
> TPM 奁拟智能卡笞理
> 专用;公用
> 否
> &
> 删除
> TPM 奁拟智能卡答理(TCP-In)
> TPM 奁拟:能卡管逻
> 域
> 否
> 屋性
> Windows Management Instrumentati.
> Windows Management In
> 所有
> 否
> Windows Management Instrumentati.
> Windows Management In.
> 所有
> 否
> 帮卧
> Windows Management Instrumentati.
> Windows Management In
> 所有
> 否
> 完成
> SCW 远裎访问防火垲则
> Scshost
> Windows 安全琵置问导
> 所有
> 否
> SCW 远程访问防火垲则
> Scshost
> Windows 安全琵置向导
> 所有
> 否
> SCW 远裎访问防火垲规则
> Svchost
> T
> Windows 安全配置向导
> 所有
> 否
> 出站规则
> Windows 防火垲远程笞理(RPC)
> Windows 防火垲远程管理
> 所有
> 否
> 和入站设置一样
> Windows 防火垲远程笞理(RPC-EPMAP)
> Windows 防火培远程管理
> 所有
> 否
> Windows 远程管理(HTTP-In)
> Windows 远程笞理
> 域;专用
> 是
> 5
> V
> 
> TcTr
> >
> Trap
> Trap
> Trap
> Trap


#### 1.4 腾讯云电脑 网页端 配置

上面的图片，就是配置服务器的出入站规则，但是 还是无法访问（[链接已屏蔽]还需要进入网页端，进行配置，我的是 腾讯云，别的云电脑，应该也有这方面的问题，希望大家探索，下面配置 网页端


> [!NOTE] [图片 OCR 识别内容]
> 三
> 8腾讯云
> 控制台
> 支持通过实例I。 I。
> 名称等搜索资源
> 快捷键 /
> 集团账号
> 备案
> 工具
> 客
> 轻量云
> 免费试用
> 邀您试用数据安全审计。实时发现数据泄露等安全风险
> 查看详情 >
> 概要
> 域名解析
> 云硬盘
> 备份点
> 防火墙
> 快照
> 监控
> 对象存储
> 主机安全
> 执行命令
> 阅
> 游戏服专区
> 凸
> 2
> 轻量应用服务器
> 防火墙所提供的安全防护作用等同于云服务器中的安全组。不支持为轻量应用服务器配置安全组。
> 服务器
> 添加规则
> 导入规则
> 键放通
> 删除
> 排序
> 设罩多实例的防火墙? _
> OrcaTerm
> 区
> 已经添加的规则
> 自动化助手
> 应用类型
> 来源 0
> 协议0
> 端0 0
> 策略 0)
> 3
> 镜像
> 自定义
> 全部1Pv4地址
> TCP
> 5000
> 允许
> 云硬盘
> 自定义
> 全部IPv6地址
> TCP
> 5000
> 允许
  
> [!NOTE] [图片 OCR 识别内容]
> 添加规则
> 对轻量应用服务器实例的入流量进行控制。
> 试试用 Al 帮助你放通防火墙端口
> 协议选 TCP
> 应用类型
> 来源 0
> 协议
> 端0 0
> 策略
> 备注
> 自定义
> 全部1Pv4地址
> TCP
> 5000
> 允许
> 可输入60个字符
> 新增一条  您还可增加91条
> 端日5000
> IPv4和6可以都加上
> 确定
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 127.0.0.
> 5000
> 邮
> 1.1计算机语言发展。。
> 必应
> 精品MAC应用分享
> 马可菠萝
> 分享你。。
> Mac软件下载-mac。
> App news and revi。
> 腾讯课堂
> 黑马Admin-1011
> [NOMOSI2OI N。
> 口 所
> 将127.0.0.1:5000替换成
> Connect to BRAIN
> 你的云电脑[地址
> BRAIN Expression Template Decoder
> IP:5000
> Run Simulator
> Paper Analysis
> 访问成功
> Specialized template decoder with grammar checking for expression-like language
> DataField Guide
> Expression Templates
> Show Users Only
> Export User Templates
> Import User Templates
> Vector Data Processing
> Nested Feature Digger
> Double Neutralization
> Group Mean Residual_Matrix Data
> Group Mean Residual_Vector Data
> TVR Delta Limit
> TVR Hump
> samplel
> Double Neutral in Analyst15
> Group_compare_glb_topdiv
> Group_compare_glb_topdiv_anl15
> Group_compare_glb_topdivmodel26
> Expression Editor
> Decode Templates


**顾问 RM49262 (Rank 30) 的解答与建议**:
您好，能麻烦分享下app_wqb的代码吗？我的邮箱是 [rexmafelix@gmail.com](mailto:rexmafelix@gmail.com) ，谢谢！


---

### 技术对话片段 172 (原帖: 使用Mac系统跑App_wqb || App_0715 (BRAIN Expression Template Decoder)经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 使用Mac系统跑App_wqb  App_0715 BRAIN Expression Template Decoder经验分享_33784622229271.md
- **时间**: 10个月前

**提问/主帖背景 (CM48632)**:
## 在Mac系统上面跑 **App_wqb** 的两种方式（1）

### 1 将 App_wqb 部署到云电脑

#### 1.1 安装python环境

[VSCODE（必须，不解决因为使用其它环境而遇到的error） + Python 3.12 以上版本（vscode+python+jupyter环境搭建_哔哩哔哩_bilibili ）]([链接已屏蔽])

如果单一跑App_wqb，安装python环境就可以；跑代码，就按视频安装运行环境即可。

#### 1.2 运行App_wqb


> [!NOTE] [图片 OCR 识别内容]
> 0715
> X
> 文件
> `
> ~^查看
> 这台脑
> 文栏
> APP_0715
> @
> 掼紊"APP_0715"
> 0
> 名称
> 咨改曰期
> 奖型
> 大小
> 收蘅夹
> 下载
> blueprints
> 2025/7/2910;:39
> 文件夹
> 卓
> custom_templates
> 2025/7/517;52
> 文件夹
> 冕丘访闩钓位置
> ResultBuilder
> 2025/7/623:55
> 文件夹
> simulator
> 2025/7/1518:22
> 文件夹
> static
> 2025/7/103:19
> 文件夹
> 这台宅肫
> templates
> 2025/7/10 3:18
> 文件奕
> CharlesdeMacBoo
> 'gitignore
> 2025/7/517:52
> GITIGNORE 文件
> 1KB
> 视频
> mirror_config
> 2025/7/221;50
> 文太文档
> 1<8
> 图斤
> MODULAR_STRUCTURE.md
> 2025/7/311:30
> MD 文件
> 5KB
> 文栏
> READMEmd
> 2025/7/221:51
> MD 文件
> 12<3
> 下裁
> requirements
> 2025/7/92:11
> 文太文档
> 1KB
> 音乐
> run_app
> 2025/7/221:44
> Windows 批处理
> 1<8
> 桌
> run
> _app.sh
> 2025/7/221:44
> SH 文件
> 1<8
> 本圯磁盏 (C:)
> setup_tsinghua
> 2025/7/221:49
> Windows 批处理
> 2 (8
> 直接
> setup_tsinghua.sh
> 2025/7/221:49
> SH 文件
> 2<8
> 用鼠标双击
> 运行打开2
> 2025/7/104;11
> Python File
> 54KB
> 网咨
> 运行程序
> 16个项目
> 选中1个项目  53.3 KB
> APP_


运行结果，如下图所示：


> [!NOTE] [图片 OCR 识别内容]
> 又
> C:IWindowslpy.exe
> Collecting
> referencing > =0.28
> 4 <from
> jsonschema >=4.18
> 囚->jupyterlah-seryer<3>=2
> 22.1>notehook>=7.0.0->
> C: Wsers Ydministrator Vocuments Mpp_O715 Wequirement
> tXt
> Iine
> 15〉〉
> Downloading https: //nypi.tuna .tsinghua
> edu.cn /pac kages /c1/h173haf8O4c642h2hc2?1
> 89546225240208e410351e3feh4eh284e5f2745448a/referencing-囚.36
> 2-093-none-any.Whl
> 26
> K〉
> Collecting rpds-Py>=0.?.1
> Cfrom jsonschema〉=4.18 .囚->jupyterIah-seruer<3,>=2
> 27.1
> >notehook>=7 .0.囚>r
> C: Wsers Vdministrator <ocuments Mpp_O715 Wequirements .txtl
> 〈line
> 15〉〉
> Downloading https: //pypi.tuna .tsinghua .edu.cn /packages /94/c1/3c8c94c7aa3905ak
> He
> 268381c698228500a8041992423148?adcdh11?e9 /rpds _Py-0.26 .O-cp3l1-Cp311-win_amd64
> Whl
> <231
> J〉
> 231.27231 ?
> RB2 &
> 0s
> eta
> 囚:}:}
> Collecting
> python-json-Iogger >=2 .0.4
> Cfrom jupyter-euents> =囚.11 .囚->jupyter-serue
> 〈3〉2.4.0->notehook>=? .0.囚>r
> C: Wsers Ydministrator Wocuments Vpp_O715 Wequi
> Iements .txt
> 〈Iine
> 15〉〉
> Down loading
> https : / /pypi.tuna .ts inghua .edu.cn/pac kages /08/20/0f252319e50a8052h
> c6a812324fc8568ahhdc42010aef03a24750hdah3h2 /python_json_logger-3.3 .O-Py3-none-an
> 4.wl
> 〈15
> K〉
> Collect
> Dyyaml>=5.3
> 〈from
> jupyter-events > =0.11 .囚->jupyter-seryer<3,>=2.4.0-
> otehook>=7 .囚.囚>
> C: Wsers Vdministrator Documents
> _8715 Wequirements .txt
> (1
> ine
> 15〉
> Downloading https: / /pypi. tuna .tsinghua
> edu.cn/pac kages /e/23/8aaOhhe2ah9dcaall
> f4f455?ccaf 95c10h9811h13ecced089443ce59c3c8/PyyAlL-6 .0.2-cp311-cp311-win_ama6 4 .w
> h1
> (161
> KB〉
> ing
> Ypp
  
> [!NOTE] [图片 OCR 识别内容]
> 又
> C:lWindowslpy.exe
> Start
> BRAIN Expression
> Template
> Decoaer
> Neh
> Application
> Application
> 4il1
> Iun
> On
> http: //localhost :5000
> BRAIN API
> integration
> incIudea
> 00
> separate
> Doxy
> needea!
> 天
> Seruing
> Flask
> app
> '运行打开找'
> 升
> Dehug
> mode:
> 0n
> INRO :werkzeug : < [31mc [ImNARNING:
> This
> is
> deueIopment
> Seryer .
> Do
> n0t
> USe
> i
> i
> production
> aeployment
> Use
> production
> NSGI
> SeHUer
> instead.[Gm
> Runnin
> On
> a11
> addresgeg
> 〈_囚_囚
> Runn
> 00
> http: /7127 .囚.囚.1:5000
> 表示程序
> Runn
> 0n
> http: /710.1 .囚.2:5000
> 成功运行
> INFOEwerkzewg:F [33mPress
> CTRITC
> To
> quitt [Bm
> INRO :werkzeug:
> 夫 Restart
> win
> stat
> Initializing
> BRAIN Expression
> Template
> Decoaer
> Checking
> ana
> installing required
> aependencies
> Uerifying
> packages
> needea
> for
> BRAIN Expression
> Template
> Decoder .
> All required dependencies
> are
> already
> installea!
> Core
> packages
> importea
> SUCCeSSfulIy!
> Flask application
> iiiali2ea
> With CORS support!
> BRAIN API
> integration
> configurea!
> Blueprints
> iportea
> SUCCeSSfully!
> All hlueprints registered successfully!
> Idea
> House:
> /iaea-house
> Paper Analysis:
> /aper-analysis
> Peature
> Engineering:
> /feature-engineering
> Templates
> airectory
> reaay:
> C: Wsers Vdministrator WDocuments
> 0715 Custom
> 七
> ing
> ing
> ing
> ing
> YDD


#### 1.3 配置 防火墙


> [!NOTE] [图片 OCR 识别内容]
> 开始
> 服务器管理器
> 这台电脑
> 桌
> a
> 任务笞器
> 控制面板
> 开始里面找到
> 控制面板
> 3
> Intemet
> Explorer
> 笞理工具
> 文件资源笞理器
  
> [!NOTE] [图片 OCR 识别内容]
> 控制面板
> 又
> 控~面板
> @
> 掼烹控司面旅
> O
> 调整计算机的设置
> 查看方式:
> 类别
> 点击
> 系统和安全
> 系统和安全
> 用户帐户
> 竺窄你闪讦舁利状态
> 更改帐户类型
> 查看事件曰志
> 外观
> 网络和 Internet
> 更改s面背|
> 查看网络状态和任务
> 湄整异莓分辨率
> 硬件
> 时钟。语言和区域
> 查看设a和打印机
> 添加语言
> 添加设a
> 更换菊入法
> 设置时闫和日期
> 程序
> 更改8期。时闫或效字格式
> '款程
> 启用或关闭 Windows 功能
> 轻松使用
> 使乐 Windows 建议钓设置
> 优化视觉显示
  
> [!NOTE] [图片 OCR 识别内容]
> 系统和安全
> 又
> 控剖面板
> 系统和安全
> 掼烹控司面旅
> 0
> 控制面板F页
> 操作中心
> 系统和安全
> 检查计算机竹状态并解夫问题
> 更改用户帐户控制设置
> 常见计算机问题疑难解笞
> 网咨和 Internet
> Windows 防火墙
> 点击 Windows 防火墙
> 硬件
> 芒状悉
> 元识用通过 Windows 防火培
> 程序
> 系统
> 用户帐户
> 查看 RAM 的太小和处理器速度
> 允许远裎访问
> 启动远程办卧
> 查看该计算机的名称
> 外观
> Windows 更新
> 时钟 
> 浯言和区域
> 启用或关闭刍动更新
> 检查更新
> 安荒可选更新
> 查看更新历史记录
> 羟松使用
> 电源选项
> 唤d计算机时需要宓码
> 更改孑源按钮的功能
> 更改计算机愆眠时闫
> 管理工具
> 对你的驱动器迸行碎片整理和优化
> 刽建并袼式化硬盏分区
> 查看事件巳志
> 计划任务
> 生成系统徒恚报告
  
> [!NOTE] [图片 OCR 识别内容]
> Windows 防火墙
> 又
> 控~面板
> 系统和安全
> Windows 防火垲
> @
> 掼烹控司面旅
> 0
> 使用 Windows 防火墙来帮助保护你的电脑
> 控制面板F页
> Windows 防火垲有劢于防止黑客或恶套软件通过 Internet 或网络访问你的。脑。
> 允许应用或功能通过 Windows
> 防火培
> 更新防火垲设置
> 更改通知设置
> Windows 防火培末使用荏荐竹设置宋屎扩计等
> 使用准荐设置
> 启用或关闭 Windows 防火垲
> 还原默认值
> 推荐竹设置有绑些?
> 言级设置
> ~网咨逆行疑难解笞
> 专用网络(R)
> 末连接
> 来宾或公用网络(P)
> 已连接
> 点击
> 公共场所(囹如机场或吮啡卣中的网络
> 高级设置
> Windows 防火垲状态:
> 关闭
> 传入洼接:
> 阻止所有与末在允许应用列表中的应用的连接
> 活动的公用网络:
> 网咨
> 通知状态:
> Windows 防火培阻止新应用时不要通知我
> 另清参阅
> 蒺作心
> 网绐和共享中心
> 机。
  
> [!NOTE] [图片 OCR 识别内容]
> 高级安全 Windows 防火墙
> 又
> 文件(9
> -作(4)
> 查0
> 帮卧(H)
> 本圯计算机  上的啬级安全 Win
> 本地计算机 _上的高级安全 Windows 防火墙
> 操作
> 人'厕
> 本地计算机_上的高级安全 Wind。
> 出规则
> 高级安全 indows 防火墙为 'Hindows 计算机提供网络安全。
> 导入策晗。
> 竺规则
> 导策略。
> 槲述
> 还原默认策骆
> 域配罡文卅
> 诊断1佟复
> Hindows 防火墙己关闭。
> 查看
> 点击
> 专用配罡文卅
> 添加
> Windows 防火墙己关闭。
> 刷新
> 入
> 出站规则
> 唇 
> 公用配罡文件是活动的
> 帮卧
> #indows 防火墙己关闭。
> Nindows 防火墙属性
> 开始
> 计算机之间的身份验证通信
> 巢?性狈则#定傅用
> Internet
> 协议安全性 (IFSec)对计算机之间的连接进行身份验证和保护的
> 连接安全规则
> 查看和创建防火墙规则
> (篝[(默鼹:
> 匹配阻止它们的规则)
> 谮:[熨鳖毽;群?颛影
> 入站规则
> 出规则
> 查看当前防火墙以及
> IPseC
> 策略和活动
> 查看有关当前应用的防火墙与连接安全性规则和活~网络连接的安全关联的信息
> 导入策(.
  
> [!NOTE] [图片 OCR 识别内容]
> 高级安全 Windows 防火墙
> x
> 文件(
> -作(A)
> 查0
> 帮卧(H)
> 杰地让簋机上的啬级安全 Win
> 入站规则
> 操作
> 入站则
> 名称
> 配置文件
> 己启用
> 入站规则
> 弋末/贝
> wqbSooOin
> 是
> 新建规则.
> 连接安全=则
> BranchCache 对等机出玑0NSOulol
> BrancbCacbe
> 0竽t 皿
> E左
> 歪
> 监视
> BranchCache 内容枇
> 新建入站规则向导
> 义
> BranchCache 托管?
> 规则类型
> 第一步
> COMt 网络访问(04
> 选择要创建的防火墙规则类型
> COMt 远程管理(D4
> 第二步
> iSCSI 珉务(TCP-In)
> 步骤:
> Netlogon 服务(NP
> 规则类型
> 要创建的规则类型
> Netlogon 服务菝枫
> 协议和端0
> SMBDirect (iWARPI
> 程席()
> 操作
> 控制程席连掊的@则。
> SNMP
> Senricl
> SNMP
> Senicl
> 配罡文件
> 端口()
> 第三步
> TPM 奁拟智能卡笞
> 名称
> 控制 TCP 或 IF 端口连接的规则
> TPM 奁拟智能卡笞
> 璇叉():
> TPM 奁拟鹤卡c
> Bracllache
> 对等机发现 (使用 S0)
> TPM 奁拟智能卡笞
> 控制 indos 体验功能连接的规则=
> Windows Manage
> 自定义()
> Windows Manage
> 自定义规则
> Windows Manage
> SCW 远程访问防炒
> SCW 远程访问防刈
> SCW 远程访问防炒
> Windows 防火垲远
> 第四步
> Windows 防火垲远
> Windows 远程管璁
> 14T
> 〈上步(6)
> 下-步(玎) >
> 取消
> 所
> Trap
> Trap
  
> [!NOTE] [图片 OCR 识别内容]
> 新建入站规则向导
> 义
> 协议和端口
> 指定应用此规则的协议和端0
> 步骤:
> 此趄则应围于 ICP 还是 I?
> 规则类型
> 协议和端0
> TCP
> UDP
> 操作
> 配罡文件
> 此规则应用于所有本地端口还是特定的本地端口?
> 名称
> 所有本坳端0(A)
> 特定本血端0(S):
> SOOO
> 1 .
> 443,
> 5000-5010
> <
> 上一步{)
> 下步{)
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 又
> 新建入站规则向导
> 操痄
> 指定茌连接与规则中指定的条件相匹配时要执行的操作。
> 步骤:
> 规则类型
> 连接符合指定条件时应该进行什么操作?
> 协议和端口
> 允许连接(A)
> 操作
> 包括使用 IFsec 保护的连接。以及未使用 IFsec 保护的连接。
> 配罡文件
> 只允许安全连接(C)
> 名称
> 墨踅婺望粼燮s4 -
> IPseo
> 连攘的安全性将依照 IFsec 属性中的设
> [到保障。
> 自定义
> 阻止连接(
> 上一步{)
> 下-步()
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 新建入站规则向导
> 义
> 配罡文#
> 指定此规则应用的配罡文件
> 步骤:
> 规则类型
> 何时应用该规则?
> 协议和端0
> 域(0)
> 操作
> 计簋机连接到甚企业域时应围。
> 配罡文件
> 专用
> 名称
> 计算机连接到专用网络位蛊(例如;  家或工作单位)时应用
> 公用(U)
> 计算机连接到公用网络位蛊时应用:
> 上步(6})
> 下步{)
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 新建入站规则向导
> 义
> 名称
> 指定此规则的名称和描述。
> 步骤:
> 规则类型
> 协议和端口
> 操作
> 名称(+) =
> 配罡文件
> HQb50OOir
> 名称
> 描述(可选)(D):
> 上步{)
> 完成()
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 高级安全 Windows 防火墙
> 又
> 文件(9
> -作(4)
> 查0
> 帮卧(H)
> 本地计算机 _上的啬级安全 Win
> 入站规则
> 操作
> 入站则
> 沮
> 配置文件
> 己启用
> 入站规则
> 己站规则
> WqbSOOOin
> 所有
> 是
> 新建规则.
> 连接安全规则
> Branchcache 对等机发现(SD-In)
> BranchCache
> 对等机发现。.
> 所
> 监视
> 7
> 按=置文件筛选
> BranchCache 囚容检紊(HTTP-In)
> BranchCache
> 内容检亵(
> 所有
> 吾
> 了
> 按状态筛选
> BranchCache 托笞缓存服务器(HTTP-In)
> BranchCache
> 托管缓存屐
> 所有
> 按组筛选
> COMt 网络访问(DCOM-In)
> COMt 网络访问
> 所有
> 否
> COMt 远程管理(DCOM-In)
> COMt 远程管理
> 所有
> 否
> 查看
> iSCSI 服务(TCP-In)
> iSCSI 屐务
> 否
> 刷新
> Netlogon 服务(NP-In)
> Netlogon 服务
> r
> 否
> 导列表。
> Netlogon 服务菝权(RPC)
> Netlogon 股务
> 否
> 帮卧
> SMBDirect (WARP-In)上的文件和打印。
> SMBDirect 上钓文件和打印。
> 所有
> 否
> SNMP
> Serice (UDP In)
> SNMP
> 咸
> 否
> wqbsoooin
> SNMP
> Serice (UDP In)
> SNMP
> 专用;公用
> 否
> 禁#斯则
> TPM 虚拟智能卡管理(DCOM-In)
> TPM 奁拟智能卡笞理
> 域
> 否
> 剪切
> TPM 奁拟智能卡答理(DCOM-In)
> TPM 虑拟昝能卡邕理
> 专用;公用
> 否
> 妄制
> TPM 奁拟智能卡笞理(TCP-In)
> TPM 奁拟智能卡笞理
> 专用;公用
> 否
> &
> 删除
> TPM 奁拟智能卡答理(TCP-In)
> TPM 奁拟:能卡管逻
> 域
> 否
> 屋性
> Windows Management Instrumentati.
> Windows Management In
> 所有
> 否
> Windows Management Instrumentati.
> Windows Management In.
> 所有
> 否
> 帮卧
> Windows Management Instrumentati.
> Windows Management In
> 所有
> 否
> 完成
> SCW 远裎访问防火垲则
> Scshost
> Windows 安全琵置问导
> 所有
> 否
> SCW 远程访问防火垲则
> Scshost
> Windows 安全琵置向导
> 所有
> 否
> SCW 远裎访问防火垲规则
> Svchost
> T
> Windows 安全配置向导
> 所有
> 否
> 出站规则
> Windows 防火垲远程笞理(RPC)
> Windows 防火垲远程管理
> 所有
> 否
> 和入站设置一样
> Windows 防火垲远程笞理(RPC-EPMAP)
> Windows 防火培远程管理
> 所有
> 否
> Windows 远程管理(HTTP-In)
> Windows 远程笞理
> 域;专用
> 是
> 5
> V
> 
> TcTr
> >
> Trap
> Trap
> Trap
> Trap


#### 1.4 腾讯云电脑 网页端 配置

上面的图片，就是配置服务器的出入站规则，但是 还是无法访问（[链接已屏蔽]还需要进入网页端，进行配置，我的是 腾讯云，别的云电脑，应该也有这方面的问题，希望大家探索，下面配置 网页端


> [!NOTE] [图片 OCR 识别内容]
> 三
> 8腾讯云
> 控制台
> 支持通过实例I。 I。
> 名称等搜索资源
> 快捷键 /
> 集团账号
> 备案
> 工具
> 客
> 轻量云
> 免费试用
> 邀您试用数据安全审计。实时发现数据泄露等安全风险
> 查看详情 >
> 概要
> 域名解析
> 云硬盘
> 备份点
> 防火墙
> 快照
> 监控
> 对象存储
> 主机安全
> 执行命令
> 阅
> 游戏服专区
> 凸
> 2
> 轻量应用服务器
> 防火墙所提供的安全防护作用等同于云服务器中的安全组。不支持为轻量应用服务器配置安全组。
> 服务器
> 添加规则
> 导入规则
> 键放通
> 删除
> 排序
> 设罩多实例的防火墙? _
> OrcaTerm
> 区
> 已经添加的规则
> 自动化助手
> 应用类型
> 来源 0
> 协议0
> 端0 0
> 策略 0)
> 3
> 镜像
> 自定义
> 全部1Pv4地址
> TCP
> 5000
> 允许
> 云硬盘
> 自定义
> 全部IPv6地址
> TCP
> 5000
> 允许
  
> [!NOTE] [图片 OCR 识别内容]
> 添加规则
> 对轻量应用服务器实例的入流量进行控制。
> 试试用 Al 帮助你放通防火墙端口
> 协议选 TCP
> 应用类型
> 来源 0
> 协议
> 端0 0
> 策略
> 备注
> 自定义
> 全部1Pv4地址
> TCP
> 5000
> 允许
> 可输入60个字符
> 新增一条  您还可增加91条
> 端日5000
> IPv4和6可以都加上
> 确定
> 取消
  
> [!NOTE] [图片 OCR 识别内容]
> 127.0.0.
> 5000
> 邮
> 1.1计算机语言发展。。
> 必应
> 精品MAC应用分享
> 马可菠萝
> 分享你。。
> Mac软件下载-mac。
> App news and revi。
> 腾讯课堂
> 黑马Admin-1011
> [NOMOSI2OI N。
> 口 所
> 将127.0.0.1:5000替换成
> Connect to BRAIN
> 你的云电脑[地址
> BRAIN Expression Template Decoder
> IP:5000
> Run Simulator
> Paper Analysis
> 访问成功
> Specialized template decoder with grammar checking for expression-like language
> DataField Guide
> Expression Templates
> Show Users Only
> Export User Templates
> Import User Templates
> Vector Data Processing
> Nested Feature Digger
> Double Neutralization
> Group Mean Residual_Matrix Data
> Group Mean Residual_Vector Data
> TVR Delta Limit
> TVR Hump
> samplel
> Double Neutral in Analyst15
> Group_compare_glb_topdiv
> Group_compare_glb_topdiv_anl15
> Group_compare_glb_topdivmodel26
> Expression Editor
> Decode Templates


**顾问 RM49262 (Rank 30) 的解答与建议**:
您好，能麻烦分享下app_wqb的代码吗？我的邮箱是 [rexmafelix@gmail.com](mailto:rexmafelix@gmail.com) ，谢谢！


---

### 技术对话片段 173 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: [Commented] 分享一个自用的AI点塔工作流.md
- **时间**: 3个月前

**提问/主帖背景 (MC42701)**:
用前准备：wqb-MCP + 任何一款AI编辑器 + APP（找灵感）

# AI 点塔工作流：

这部分主要向AI介绍固定的点塔工作流。

1. 确定要点的塔

1. 明确当前工作的股票池：region/delay/universe

2. 选择要点的塔，依据：简单性优先和未点优先

- 简单性：使用`get_datasets` MCP-tool，参数选择alpha数量倒序，通常alpha数量越多，对应dataset越简单。

- 未点：使用`get_pyramid_alphas` MCP-tool，获取当前塔的alpha数量，如果一个塔的alpha数量小于3个，那么这个塔未点。

3. 确定要点的塔：典型的方法是，首先筛选简单的dataset，然后在其中找到未点的塔。

2. 确定回测数据集并搜集该数据集的alpha模板

1. 确定回测数据集：4参数`region/delay/universe/dataset`。注意：最后的dataset用小写字母

2. 获取alpha模板：这步很随意，通常使用`Alpha-Idear` MCP 生成多个alpha模板，或是查找本地模板库，找到数据类型相匹配的模板。

- 使用`alpha_idear` MCP ：输入4参数，等待返回模板

- 查找本地模板：使用能读取Excel文件的工具，本地模板库

3. 依据回测结果筛选有信号的模板

1. 对每一个模板，选择合适的参数，形成一个alpha表达式，使用`create_multi_simulate` MCP-tool 进行回测。注意：每一次`multi-simulate`最多只能回测5个alpha表达式，超过将触发限流

2. 对所有的表达式的回测结果对比分析，优先筛选夏普绝对值大于0.7的模板（如果夏普为负且绝对值大于0.7，说明信号需要反向）

3. 确定所选择的有信号的模板

4. 拓展模板，输出可回测挖掘的模板

1. 回测模板中alpha表达式数量限制：一个模板中所有参数乘积为alpha总数，不得超过6000个。

2. 合理替换模板中的参数：

- 字段参数：如果只用到一个字段，那么该字段可用直接使用对应数据集中的全部同类型字段

- 时间参数：如果使用到`ts_op`，那么其中输入的时间窗口也可替换

- 类别参数：如果使用到`group_op`，那么其中输入的组类别也可替换，这通常替换为`pv1`数据集中的`group`字段。

- 操作符参数：还可以将`vec_avg`替换为`vec_sum`。

3. 生成该模板的表达式，并注明参数

5. 生成Alpha表达式模板

我是把APP里面的“找灵感”功能给扣下来弄成了一个AI可调用的MCP的，然后AI就可以自动去找灵感了，这里要说一个可能的bug：

让AI调用`get_datasets`工具的时候，我一开始是返回：


> [!NOTE] [图片 OCR 识别内容]
> "delay":
> "instrument
> type":  "EQUITY"
> "pegion"
> IUSA"
> Iuniverse"
> "T0P3000"
> 响应
> errop":
> IAn
> unexpected error
> occurred: 400 Client
> Error: Bad
> Request
> for
> Url:
> https: //api
> Worldquantbrain.com /data-sets?
> instrumentTypesEQUITY&regionsUSA&delay=I&universe=TOP3OO
> O8themeALL


然后开始debug，最终发现是url多了个”theme=ALL"，去掉后就正常了：
 
> [!NOTE] [图片 OCR 识别内容]
> wqb-platformlget_datasets
> 'delay":
> "pegion"
> IEUR"
> Iuniverse"
> ITOPCS16OO"
> 响应
> "count"
> 129
> "results":
> "id": "analystlO"
> "name"
> "Performance-Weighted Analyst
> Estimates"
> "description"
> "This dataset
> provides
> smart
> estimates,|"
> Which
> are intelligently weighted averages
> 0f financial
> forecasts
> from institutional
> analysts.
> Individual
> analyst
> forecasts
> are weighted based
> On
> tWO
> key factors:
> the
> analyst's historical
> performance
> SCOTe
> the
> pecency
> 0f
> their
> estimate.
> This approach
> aims
> to
> create
> more
> accurate
> consensUs
> forecast by giving
> greater
> importance to estimates
> from
> historically
> proven
> timely analysts
> Ipatonnnv"
> and
> and
 然后是我让AI跑出来的一个power pool alpha：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> ZOOOK
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Risk Neutralized Pnl
> IS Testing Status
> Period
> 15
> 05
> 6 PASS
> 5WARNING
> 6 PENDING


最后说一下我的感想吧，AI发展的非常迅速，半年前这种活AI还不能胜任，而现在却完全不一样了。工作中一定不能拒绝/抵制AI，而是要正确看待，合理使用！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬的工作流看起来非常不错

只是单就最后这个alpha的PnL走势来看，厂的形态很明显了，这种大佬也会考虑交吗

===================================================================================


---

### 技术对话片段 174 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 分享一个自用的AI点塔工作流_38870096703639.md
- **时间**: 3个月前

**提问/主帖背景 (MC42701)**:
用前准备：wqb-MCP + 任何一款AI编辑器 + APP（找灵感）

# AI 点塔工作流：

这部分主要向AI介绍固定的点塔工作流。

1. 确定要点的塔

1. 明确当前工作的股票池：region/delay/universe

2. 选择要点的塔，依据：简单性优先和未点优先

- 简单性：使用`get_datasets` MCP-tool，参数选择alpha数量倒序，通常alpha数量越多，对应dataset越简单。

- 未点：使用`get_pyramid_alphas` MCP-tool，获取当前塔的alpha数量，如果一个塔的alpha数量小于3个，那么这个塔未点。

3. 确定要点的塔：典型的方法是，首先筛选简单的dataset，然后在其中找到未点的塔。

2. 确定回测数据集并搜集该数据集的alpha模板

1. 确定回测数据集：4参数`region/delay/universe/dataset`。注意：最后的dataset用小写字母

2. 获取alpha模板：这步很随意，通常使用`Alpha-Idear` MCP 生成多个alpha模板，或是查找本地模板库，找到数据类型相匹配的模板。

- 使用`alpha_idear` MCP ：输入4参数，等待返回模板

- 查找本地模板：使用能读取Excel文件的工具，本地模板库

3. 依据回测结果筛选有信号的模板

1. 对每一个模板，选择合适的参数，形成一个alpha表达式，使用`create_multi_simulate` MCP-tool 进行回测。注意：每一次`multi-simulate`最多只能回测5个alpha表达式，超过将触发限流

2. 对所有的表达式的回测结果对比分析，优先筛选夏普绝对值大于0.7的模板（如果夏普为负且绝对值大于0.7，说明信号需要反向）

3. 确定所选择的有信号的模板

4. 拓展模板，输出可回测挖掘的模板

1. 回测模板中alpha表达式数量限制：一个模板中所有参数乘积为alpha总数，不得超过6000个。

2. 合理替换模板中的参数：

- 字段参数：如果只用到一个字段，那么该字段可用直接使用对应数据集中的全部同类型字段

- 时间参数：如果使用到`ts_op`，那么其中输入的时间窗口也可替换

- 类别参数：如果使用到`group_op`，那么其中输入的组类别也可替换，这通常替换为`pv1`数据集中的`group`字段。

- 操作符参数：还可以将`vec_avg`替换为`vec_sum`。

3. 生成该模板的表达式，并注明参数

5. 生成Alpha表达式模板

我是把APP里面的“找灵感”功能给扣下来弄成了一个AI可调用的MCP的，然后AI就可以自动去找灵感了，这里要说一个可能的bug：

让AI调用`get_datasets`工具的时候，我一开始是返回：


> [!NOTE] [图片 OCR 识别内容]
> "delay":
> "instrument
> type":  "EQUITY"
> "pegion"
> IUSA"
> Iuniverse"
> "T0P3000"
> 响应
> errop":
> IAn
> unexpected error
> occurred: 400 Client
> Error: Bad
> Request
> for
> Url:
> https: //api
> Worldquantbrain.com /data-sets?
> instrumentTypesEQUITY&regionsUSA&delay=I&universe=TOP3OO
> O8themeALL


然后开始debug，最终发现是url多了个”theme=ALL"，去掉后就正常了：
 
> [!NOTE] [图片 OCR 识别内容]
> wqb-platformlget_datasets
> 'delay":
> "pegion"
> IEUR"
> Iuniverse"
> ITOPCS16OO"
> 响应
> "count"
> 129
> "results":
> "id": "analystlO"
> "name"
> "Performance-Weighted Analyst
> Estimates"
> "description"
> "This dataset
> provides
> smart
> estimates,|"
> Which
> are intelligently weighted averages
> 0f financial
> forecasts
> from institutional
> analysts.
> Individual
> analyst
> forecasts
> are weighted based
> On
> tWO
> key factors:
> the
> analyst's historical
> performance
> SCOTe
> the
> pecency
> 0f
> their
> estimate.
> This approach
> aims
> to
> create
> more
> accurate
> consensUs
> forecast by giving
> greater
> importance to estimates
> from
> historically
> proven
> timely analysts
> Ipatonnnv"
> and
> and
 然后是我让AI跑出来的一个power pool alpha：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> ZOOOK
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Risk Neutralized Pnl
> IS Testing Status
> Period
> 15
> 05
> 6 PASS
> 5WARNING
> 6 PENDING


最后说一下我的感想吧，AI发展的非常迅速，半年前这种活AI还不能胜任，而现在却完全不一样了。工作中一定不能拒绝/抵制AI，而是要正确看待，合理使用！

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬的工作流看起来非常不错

只是单就最后这个alpha的PnL走势来看，厂的形态很明显了，这种大佬也会考虑交吗

===================================================================================


---

### 技术对话片段 175 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 在wq半年从15刀到100刀我是怎么做到连续三个月vf10comb294的经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (PP26750)**:
时光飞逝，现在已经在wq干了半年了，刚入坑wq时，每天睁眼就怕连1.5刀都保不住，感觉自己随时要开始坐牢。现在偶尔能冲上百刀，却又开始焦虑明天的osmosis会不会翻车。每个阶段都有每个阶段的烦恼，但回头看，正是这些烦恼推着我往前走。

作为被论坛大佬们奶大的新人，我决定把自己连续三个月vf1.0、comb达到2.94的实操经验全盘托出。希望下一个写分享帖的，就是成功后的你。

我觉得最重要的有三点原因：

1. 多样性，绝对的多样性，很多人可能会使用遍历模板来交alpha，这样你的库里会有大量结构一样的alpha我觉得这是不够多样性的，我的做法是每个结构只用一次，这个结构交过之后交再也不碰了，这是最主要的一点多样性，下面还有几点
   - 中性化：不要一直交一种中性化，要雨露均沾，每种中性化都来点，然后推荐多用风险中性化，这个的os要比普通中性化好一些。
   - 换手率：这也是多样性的一部分，很多人会说不要交死鱼也不要交高换手，我觉得不是这样的，这些东西应该是不要交太多，你的池里面大部分换手率应该在5-20这样，再用低换手和高换手增加多样性。
   - sc和ppc：有时候会出现一个alpha的sc很高，但是ppc很低的情况，有些经常断粮的这时候交把持不住了，我一般是会取sc和ppc的最大值来看，两者最大值小于5才会提交
2. 一定要注意年度数据，特别是最近几年的，很多时候会有整体指标不错，但是最近几年不太好的情况，这种就是趋势不好了，我认为趋势是要大于哪些指标的，一个夏普0几fit0.4 0.3的alpha趋势好我还是会交的。
3. 最后一点是提交策略，这半年我发现很多朋友都喜欢无意义的刷六维和为了点塔交不好的alpha，明明comb连0.5都没有甚至是负的，说难听的连genius硬性标准都达不到你刷六维和点塔这有啥意义呢，多点些好数据集（这个可以用华子哥插件看），多用kunqi老师的gem来做alpha，平均op和字段数升上去没事只要你的alpha数据好且有意义就可以，op与是否过你和不是等号的关系。

还有就是些老生常谈的atom+ra+高质量+点塔+看Performance Comparison。这些在论坛都有很多介绍，我就不多说了。

最后祝大家都能在wq取得自己想要的成绩。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

太强了PP大师 combine都要3+了

这就把PP的经验学起来！

=============================================================================


---

### 技术对话片段 176 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 在wq半年从15刀到100刀我是怎么做到连续三个月vf10comb294的经验分享_39759673422487.md
- **时间**: 2个月前

**提问/主帖背景 (PP26750)**:
时光飞逝，现在已经在wq干了半年了，刚入坑wq时，每天睁眼就怕连1.5刀都保不住，感觉自己随时要开始坐牢。现在偶尔能冲上百刀，却又开始焦虑明天的osmosis会不会翻车。每个阶段都有每个阶段的烦恼，但回头看，正是这些烦恼推着我往前走。

作为被论坛大佬们奶大的新人，我决定把自己连续三个月vf1.0、comb达到2.94的实操经验全盘托出。希望下一个写分享帖的，就是成功后的你。

我觉得最重要的有三点原因：

1. 多样性，绝对的多样性，很多人可能会使用遍历模板来交alpha，这样你的库里会有大量结构一样的alpha我觉得这是不够多样性的，我的做法是每个结构只用一次，这个结构交过之后交再也不碰了，这是最主要的一点多样性，下面还有几点
   - 中性化：不要一直交一种中性化，要雨露均沾，每种中性化都来点，然后推荐多用风险中性化，这个的os要比普通中性化好一些。
   - 换手率：这也是多样性的一部分，很多人会说不要交死鱼也不要交高换手，我觉得不是这样的，这些东西应该是不要交太多，你的池里面大部分换手率应该在5-20这样，再用低换手和高换手增加多样性。
   - sc和ppc：有时候会出现一个alpha的sc很高，但是ppc很低的情况，有些经常断粮的这时候交把持不住了，我一般是会取sc和ppc的最大值来看，两者最大值小于5才会提交
2. 一定要注意年度数据，特别是最近几年的，很多时候会有整体指标不错，但是最近几年不太好的情况，这种就是趋势不好了，我认为趋势是要大于哪些指标的，一个夏普0几fit0.4 0.3的alpha趋势好我还是会交的。
3. 最后一点是提交策略，这半年我发现很多朋友都喜欢无意义的刷六维和为了点塔交不好的alpha，明明comb连0.5都没有甚至是负的，说难听的连genius硬性标准都达不到你刷六维和点塔这有啥意义呢，多点些好数据集（这个可以用华子哥插件看），多用kunqi老师的gem来做alpha，平均op和字段数升上去没事只要你的alpha数据好且有意义就可以，op与是否过你和不是等号的关系。

还有就是些老生常谈的atom+ra+高质量+点塔+看Performance Comparison。这些在论坛都有很多介绍，我就不多说了。

最后祝大家都能在wq取得自己想要的成绩。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

太强了PP大师 combine都要3+了

这就把PP的经验学起来！

=============================================================================


---

### 技术对话片段 177 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 成为expertvf连续三个月上09经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (ZY36280)**:

> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Factor
> Factor
> 2Y36280 (Me)
> 8,51
> 0,90


近三次更新的vf变化是：0.98->0.91->0.90，这次更新来到了12月，刚好包括了整个expert这三个月，因此打算依次查看下这三个月提交的alpha，总结expert这三个月高vf的原因。

首先8、9、10月的vf猛涨来到了0.98， [vf猛增0.48->0.98，第一次SA拿满60刀 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] vf猛增048-098第一次SA拿满60刀.md) 在这个帖子里已经总结了一部分了。

接下来是9、10、11月。
由于os已经更新了，可以很明显的看到11月提交的USA地区OS/IS Ratio这个指标很差，一共提交了11个，但是有5个alpha的OS/IS Ratio都小于0，剩下6个虽然是正的，但是也都小于0.4。可以说这对vf的影响是巨大的。我发现首先，三五的not(own)alpha确实很一般，基本os都崩了；然后基本上pnl到最后平了，os不会多好，比如：
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> ?nl
> ZSM
> ZOM
> 1SM
> 1OM
> 11/0812017
> Equal Weight Pnl:
> 12.3311
> Train Combo Pn:
> 508.08k
> 5OOOK
> 骷
> 2014
> 2015
> 2016
> 2017
> 2018
> 2020
> 2021
> 2022
> 2023
> Combo Pnl
> Equal Weieht Pnl
> 2019
 
同时，我还交了15个EUR地区的alpha，看OS/IS Ratio，大都是正的，但是也基本是不到1的。还好GLB地区和ASI地区的os还不错，尤其GLB地区，怪不得老师一直推荐我们做GLB的glb的alpha，不仅是11月，我翻看了我所有更新os的glb的alpha（由于glb跑得慢所以交的也不多），发现os都挺不错的，没有多少很崩的os。 
> [!NOTE] [图片 OCR 识别内容]
> OSIIS Ratio
> e.6> 1
> 1.77
> 1.72
> 1.01
> 0.99
> 0.82
> 0.82
> 0.80


ASI地区经过多次的增加难度，os也还可以，比11月的USA和EUR地区都好。主要这两个地区发力，才能vf才能只掉到0.91。

最后是10、11、12月。
12月我主交的是usa，一共提交了43个，其次是eur，交了21个。都是ATOM居多。感觉我做的USA地区的alpha，os会差一些，可能是有时候想要尽量减少operator的数量，导致不太稳定可能。同时12月也发现很多not own的sa，os都不好，own的sa反倒os会跟is一致。

最后，虽然vf还在0.9，很开心，但是os更新的结果也是要警醒自己。要管住手，提交要有一定的标准底线。一些pnl已经有些低头了的，一定要慎重；如果在犹豫要不要交，那感觉大概率还是别交；要交得多且多样，不仅是数据多样，思路最好也多样，多用ai尝试修改，生成模板，通过os可以看到很多alpha都只是在is期间表现好而已，如果交的少的话，除非对自己的alpha很有信心，不然还是越多越稳定。

最后祝大家新年快乐，月月vf1.0，季季都是GM。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬的vf真是令人羡慕  从大佬的经验分享中学到了很多

希望以后也能拥有和大佬一样高的vf

===================================================================================


---

### 技术对话片段 178 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 成为expertvf连续三个月上09经验分享_38720223996439.md
- **时间**: 3个月前

**提问/主帖背景 (ZY36280)**:

> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Factor
> Factor
> 2Y36280 (Me)
> 8,51
> 0,90


近三次更新的vf变化是：0.98->0.91->0.90，这次更新来到了12月，刚好包括了整个expert这三个月，因此打算依次查看下这三个月提交的alpha，总结expert这三个月高vf的原因。

首先8、9、10月的vf猛涨来到了0.98， [vf猛增0.48->0.98，第一次SA拿满60刀 – WorldQuant BRAIN]([L2] vf猛增048-098第一次SA拿满60刀_37055219307799.md) 在这个帖子里已经总结了一部分了。

接下来是9、10、11月。
由于os已经更新了，可以很明显的看到11月提交的USA地区OS/IS Ratio这个指标很差，一共提交了11个，但是有5个alpha的OS/IS Ratio都小于0，剩下6个虽然是正的，但是也都小于0.4。可以说这对vf的影响是巨大的。我发现首先，三五的not(own)alpha确实很一般，基本os都崩了；然后基本上pnl到最后平了，os不会多好，比如：
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> ?nl
> ZSM
> ZOM
> 1SM
> 1OM
> 11/0812017
> Equal Weight Pnl:
> 12.3311
> Train Combo Pn:
> 508.08k
> 5OOOK
> 骷
> 2014
> 2015
> 2016
> 2017
> 2018
> 2020
> 2021
> 2022
> 2023
> Combo Pnl
> Equal Weieht Pnl
> 2019
 
同时，我还交了15个EUR地区的alpha，看OS/IS Ratio，大都是正的，但是也基本是不到1的。还好GLB地区和ASI地区的os还不错，尤其GLB地区，怪不得老师一直推荐我们做GLB的glb的alpha，不仅是11月，我翻看了我所有更新os的glb的alpha（由于glb跑得慢所以交的也不多），发现os都挺不错的，没有多少很崩的os。 
> [!NOTE] [图片 OCR 识别内容]
> OSIIS Ratio
> e.6> 1
> 1.77
> 1.72
> 1.01
> 0.99
> 0.82
> 0.82
> 0.80


ASI地区经过多次的增加难度，os也还可以，比11月的USA和EUR地区都好。主要这两个地区发力，才能vf才能只掉到0.91。

最后是10、11、12月。
12月我主交的是usa，一共提交了43个，其次是eur，交了21个。都是ATOM居多。感觉我做的USA地区的alpha，os会差一些，可能是有时候想要尽量减少operator的数量，导致不太稳定可能。同时12月也发现很多not own的sa，os都不好，own的sa反倒os会跟is一致。

最后，虽然vf还在0.9，很开心，但是os更新的结果也是要警醒自己。要管住手，提交要有一定的标准底线。一些pnl已经有些低头了的，一定要慎重；如果在犹豫要不要交，那感觉大概率还是别交；要交得多且多样，不仅是数据多样，思路最好也多样，多用ai尝试修改，生成模板，通过os可以看到很多alpha都只是在is期间表现好而已，如果交的少的话，除非对自己的alpha很有信心，不然还是越多越稳定。

最后祝大家新年快乐，月月vf1.0，季季都是GM。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬的vf真是令人羡慕  从大佬的经验分享中学到了很多

希望以后也能拥有和大佬一样高的vf

===================================================================================


---

### 技术对话片段 179 (原帖: 成为顾问五个月，分享vf保持0.9+的经验经验分享)
- **原帖链接**: [Commented] 成为顾问五个月分享vf保持09的经验经验分享.md
- **时间**: 9个月前

**提问/主帖背景 (SC84371)**:
我在四月份成为了conditional consultant，vf经历了0.5-0.97-0.98-0.93的变化，除去最开始的vf空窗期外均保持0.9以上。我将从我的个人经历分享我的vf经验


> [!NOTE] [图片 OCR 识别内容]
> Base Payment


1.atom是非常重要的vf因素，强烈建议大家多交atom，事实上我绝大多数alpha都是atom，我并没有选择死板的使用一二三街模板，对于每一个不同的fields因为其中数据是具有共性的，我们可以根据其description进行具有经济及意义的模板攥写，而后发现该模板有较好的指标效果后进行代码批量回测，这得与在顾问课上weijie老师说经济意义是非常重要的一个因素。

2.不要死板的困在某一个地区，我对每一个fields都只提交3-4个在成功点亮pyramids后结束，一定要保持多样性，甚至于单个fields利用模板提交效果最好的那一个，然后更换其他fields用三个不同的fields点亮一个pyramids。

3.其实很多时候不必纠结于 base payment ，实际上base payment和pc有着很大的关系，但很多pc很低调alpha很容易存在某种缺陷。因此我建议可以观察近三年样本表现，以及可以利用sign 符号验证表现的稳定性。

4.保持高margin和合理的turnover,尽量将turnover保持在5-15的区间并且基本至少保证margin有大于10的效果，这是一个alpha能否拥有较好收益的一大因素。

5.一定要保证有一定的数量！我的六月份vf从0.98-0.93的因素在于六月份因准备考试只交了40几个alpha，造成的不稳定效果，因此保证一定数量的alpha提交时必须的。

最后在季度末请大家注意六维，我也在本季度正在冲击master

最后感谢weijie老师，感谢研究小组的各位

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！所以其实只要尽可能多交Atom，作为新人，即使交的alpha不满足1.5刀大法，vf提高的概率也是很大的是吗？

另外大佬能顺便也分享下mcp 那个value factor trend score的变化吗？谢谢！

===================================================================================


---

### 技术对话片段 180 (原帖: 成为顾问五个月，分享vf保持0.9+的经验经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 成为顾问五个月分享vf保持09的经验经验分享_34938580496023.md
- **时间**: 9个月前

**提问/主帖背景 (SC84371)**:
我在四月份成为了conditional consultant，vf经历了0.5-0.97-0.98-0.93的变化，除去最开始的vf空窗期外均保持0.9以上。我将从我的个人经历分享我的vf经验


> [!NOTE] [图片 OCR 识别内容]
> Base Payment


1.atom是非常重要的vf因素，强烈建议大家多交atom，事实上我绝大多数alpha都是atom，我并没有选择死板的使用一二三街模板，对于每一个不同的fields因为其中数据是具有共性的，我们可以根据其description进行具有经济及意义的模板攥写，而后发现该模板有较好的指标效果后进行代码批量回测，这得与在顾问课上weijie老师说经济意义是非常重要的一个因素。

2.不要死板的困在某一个地区，我对每一个fields都只提交3-4个在成功点亮pyramids后结束，一定要保持多样性，甚至于单个fields利用模板提交效果最好的那一个，然后更换其他fields用三个不同的fields点亮一个pyramids。

3.其实很多时候不必纠结于 base payment ，实际上base payment和pc有着很大的关系，但很多pc很低调alpha很容易存在某种缺陷。因此我建议可以观察近三年样本表现，以及可以利用sign 符号验证表现的稳定性。

4.保持高margin和合理的turnover,尽量将turnover保持在5-15的区间并且基本至少保证margin有大于10的效果，这是一个alpha能否拥有较好收益的一大因素。

5.一定要保证有一定的数量！我的六月份vf从0.98-0.93的因素在于六月份因准备考试只交了40几个alpha，造成的不稳定效果，因此保证一定数量的alpha提交时必须的。

最后在季度末请大家注意六维，我也在本季度正在冲击master

最后感谢weijie老师，感谢研究小组的各位

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享！所以其实只要尽可能多交Atom，作为新人，即使交的alpha不满足1.5刀大法，vf提高的概率也是很大的是吗？

另外大佬能顺便也分享下mcp 那个value factor trend score的变化吗？谢谢！

===================================================================================


---

### 技术对话片段 181 (原帖: 手机远程连接claudecode，24小时随时指挥AI干活！经验分享)
- **原帖链接**: [Commented] 手机远程连接claudecode24小时随时指挥AI干活经验分享.md
- **时间**: 4个月前

**提问/主帖背景 (ZL81441)**:
最近Clawdbot太火了，我已经被Clawdbot刷屏两天了

他实现了WhatsApp, Telegram, Discord,直接和ai对话，并且可以远程指挥你的电脑干活
 
> [!NOTE] [图片 OCR 识别内容]
> 核心能力
> 具体表现
> 支持 WhatsApp` Telegram
> Discord。
> Slack。
> Signal
> 全平台融入
> iMessage:
> Microsoft Teams 等10+ 主流平台
> 收发邮件。管理日历。预定航班。控制智能家居。运行代砑
> 超越闲聊的执行力
> 操作文件系统
> 记住你的偏好。工作习惯和历史对话。 Al 会随着时间推移变得
> 持久记忆与个性化
> 越来越懂你
> 浏览器控制。命令行执行。文件读写
> 网络搜索。技能扩展系
> 强大的系统集成
> 统
> 本地优先与数据隐私
> 运行在你自己的设备上。数据完全在你的掌控之中
 

我也是第一时间部署到了自己的Mac mini上，老实说这个玩意权限确实有点大，想尝试的小伙伴还是整一台新的电脑或者是部署到vps上。我折腾了半天只跑通了千问的模型，使用下来觉得很兴奋，又有点小失望。兴奋是功能和潜力十分强大，交互方式十分的新颖。失望是配置起来简单，后续各种权限的设置等等，比想象的要复杂，感觉笨笨的（也不知道是不是千问的问题）

最让人失望的是他居然不能自动调用claudecode！也就是说我不能用它来帮助我做alpha工作。

于是我转念一想，用AI控制电脑，执行等 **这些功能，Claude Code 不是都有吗？**

区别在于Claude code只能在终端里交互，而 Clawdbot 让你能在聊天软件里用。 Clawdbot启发了我， **搭一座桥，把聊天软件连到 Claude Code。**

这两者原理如下：

```

```

Telegram │ ───▶ │ Bot 程序 │ ───▶ │ Claude Code

(你手机) │ ◀─── │ (你电脑) │ ◀─── │ (AI) │

```

```

1. 你在 Telegram 发消息
2. Bot 程序收到消息，转发给 Claude Code
3. Claude Code 执行任务（搜索、写文件、跑代码...）
4. Bot 程序把结果发回 Telegram

Bot 程序只是个"传话筒"，真正干活的是 Claude Code。

想法有了，于是我开始说干就干。啊不，我也不是程序员，于是我开始找开源社区有没有现成解决方案，在尝试了很多方案后失败，终于跑通了两个方案。

## **一 ：Telegram机器人**

仓库的地址如下 [[链接已屏蔽]) 
 
> [!NOTE] [图片 OCR 识别内容]
> Error: CUDA out of memory. Tried to allocate 19.36 GiB. GPU 0 has a total capacity of 47.40 GiB of which 16.13 GiB is free. Including non-PyTorch memory, this process has 1.53 GiB memory in use. Process 58487 has 9.97 GiB memory in use. Process 58485 has 14.73 GiB memory in use. Process 58483 has 5.02 GiB memory in use. Of the allocated memory 1.02 GiB is allocated by PyTorch, and 204.03 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  ([链接已屏蔽])
 

至于部署的方式，仓库readme文件写的比较详细，我这儿就不贴了。
如何创建telegram的机器人：

1. 打开Telegram，搜索
   [@Botfather]([链接已屏蔽])
2. 发送 /newbot
3. 按提示输入名称
4. 获得一个 Token （Use this token to access the HTTP API后面这一串英文和数字）

如果不会的话，可以直接把仓库地址和Token丢给Claudecode，让他来帮你安装。
最终成效
 
> [!NOTE] [图片 OCR 识别内容]
> 0.07
> 4G
> 5G
> 2.05
> 4G
> 5G
> 7:42
> KBIs
> VPN
> SIlsoll 100
> 7:42
> KBIs
> VPN
> Sl s511 100
> M
> Myclaude77_bot
> M
> Myclaude77_bot
> 机器人
> 机器人
> 可以了 ,
> 连接通了
> 07:05
> 使用改进alpha 技能
> 优化
> 07:10
> 好的
> 连接通了!有什么需要我帮忙的
> 吗?
> 输出每个变体的表现  07:28
> 07:05
> ##  所有变体表现对比
> 查看你有哪些技能
> 07:07
> 根据我的配置,
> 我有以下可用技能:
> ### Alpha IC。
> Tr7vJ (原始)
> ##规划与管理
> **表达式**:
> planning-with-files
> 复杂任务的文件式
> 规划 ,
> 创建 taskplenmd
> fingingsmg
> 2
> 和 progressmg
> H liz
> ## WorldQuant BRAIN 相关技能
> expression_verifier
> 验证 alpha 表达
> 式的语法
> **性能指标**:
> brain-improve-alpha-performance - 改
> 指标 |值 |
> 进 BRAIN alphas 的5步工作流
>  |
> brain-datafield-exploration-general
> Sharpe
> 2.28
> 评估 BRAIN 数据集的6种方法
> Fitness
> 1.93
> brain-feature-implementation
> 从
> Returns
> 13.81%
> markdown 文件实现 BRAIN features
> Drawdown
> 5.09%
> brain-explain-alphas
> 分析和解释
> Turnover
> 0.1925
> BRAIN alpha 表达式
> 2Y Sharpe
> 1.96
> brain-dataset-exploration-general
> 深
> Robust Sharpe
> **0.51**
> 入探索 BRAIN 数据集
> Sub Sharpe
> 0.67
> brain-calculate-alpha-selfcorrQuick
> 计算 alpha 自相关性
> *相关性**:
> brain-how-to-pass-AlphaTest
> Alpha
> 类型
> 值 |状态 |
> 提交测试的要求和改进建议
> 一-----
> 井'40丫 |7791
> 十 /71 |
> 二菜单
> 输入消息
> 二菜单
> 腧入消息


## **二：Happy coder app**

## （写稿的时候才发现，新手更加推荐！）
官方网站： [[链接已屏蔽])

电脑终端输入代码
npm i -g happy-coder && happy

 
> [!NOTE] [图片 OCR 识别内容]
> Happy Coder
> Bulka, LLC
> 』
> 应用内购商品
> 4.9太
> 1万+
> 838条评价
> 次下载
> 3岁以上 @
> 安装
> 分享
> 添加到心愿单
> 6
> 在您的设备上可以使用此应用
> Code everything, everywhere,allat once
> Realtime Voice with multiple sessions
> Review changes or
> 应用支持
> ~
> PA?
> 8:123
> ODEITUIICLUebeIUely Uuray: MacerI NoJe.ls Refiesh
> ODEITUIICLUebeIUely Uuray: MacerI NoJe.ls Refiesh
> 臼 {erglstoiciDrvelop;opentunnelisrc
>  Urcp
> 1
> OITrsm
> Migration; Comp eta
> TEWTR ICn
> IL=Col
> ASTCIRPTCF DTET
> Cmson{
> IaT4
> Lontend
> 7 M +
> 7 1373
> C TTTaTT
> CIidr1
> U111(1LO?n SN SU4aICHII
> IIITTT
> LITII
> U^
> CmrInder
> Tronzend ;Frontendsessionts
> AICTTt
> sttrllon
> TTon
> eoncttrTent
> 类似应用
> CTTU'
> R11
> ITCie;T
> Etrof Hindllire
> TmTanmN+o7 7 Lm
> IIDOIt
> startrzomen
>  zonzeno'startFTOIC2NO
> Dinn
> Updated Iosger contiguration
> IhTanSOCTf Snta
> SIC !utils WodeTTaCter
> IIDoIt
> + Tngm
> _e++1LS
> N Ftah  RLLel fttyitl
> TH i f h API
> I
> Would you prefer re to:
>  
> CorrSrlt:Li51L'lu
> TT
> Vsti:
> KeED the CUrrenL Complete Upqrade Tcomierge]
> SETLII
> IorIn|
> TFHIITT
> 'TUe551111
> TypeScrpt compilation: Allerrols resolyed
> Rewert
> original state and do on; NATS upsrade Trst
> 记账城市 -用每笔收支。
> 建造你的城市
> UTC Cet
> Norin orresl;
> Show you the specific NATS changes
> detail
> TmstTnsT
> T !TTnf
> CLI functionalty: Al ccmmands cperational with properhelp text
> lot hardled
> +1153
> T1ntu
> the Currentapprouch
> thalall dependencies Iork togetherard are tested 25 3 corr plele
> FOR UNE
> SPARKFUL
> Orn OISINiti
> Cxisting functicnality wile moderizins
> TTII
> atcwl'CU preter
> CIRTaT
> ICMm
> TUIIII?
> thc lalest,Irost
> NII
> T[TIsrr
> allldeperdencies, takirg
> CTpli'fTn-on'
> fulladyantage
> modlern Nadels features and improed TypeScript supnor!
> SI
> TtT
> 21T
> iTmin?
> C+
> 4.1大
> mntzn
> OTT
>  Listeninn http port]
> Type
> 35530
> Ttoni
> SOTOTC
> LISTs
> 53TOT Frdmmints
> TImSe
> KOIC
> frsl te NATS Uperade?
> aCLionI Iuntlon
> CNOOb
> maste
> 1 Fnr
> L79.12
>  +-
> CLIUIIs '
> LI
> TILO '
> MTCETtan
> Lant m5
> ACCIC
> UUShe NSTC
> Jprade hrst, but Iie aread; ccrpleted the fJll
> UIT个
> RnT
> goTnRI
> 922n.
> Jeperdeney upgrade inludin the NRIS risration frorm Is rals to nals j5
> TTO
> CMUNI
> +」cOTtTUNL
> 3095
> st+Fomo |
> httppor, CaObJ.51
> PRO
> Lel ie shoi you Vha Nas dore
> specifial' [or .he IATs Jpsrade:
> Let UULt
> OMtLuI'
> UdseTTLubtJuIs
> 9239
> Lel IttP'
> optyons-pl
> y」SLTItLuutiur
> SLarLF OTeIIoI 
> HLLPO', OITonss1
> PR
> FI|
> CNITN
> VII stI (o I h(CHG WT
> '' 
> Overload Apps
> MLIII'
> T
> NATS,
> Durl
 
appstore或者play商店搜索happy coder下载

APP扫码终端二维码即可绑定，流程更加简单快捷，UI交互也更全面友好！
 
> [!NOTE] [图片 OCR 识别内容]
> 0.75
> 46
> 56
> 0.00
> 46
> 56
> 8:27
> KB/s
> VPN
> S5
> 99
> 8:25
> KBIs
> VPN
> SIsl
> 99
> 终端
> BRAIN risk数据集研究
> 已连接
> ~/Downloads/Claudebot
> ~|Downloads/Claudebot
> 启动ind auto angent,
> 研究-Frisk数据集
> Claudebot
> Title changed to
> BRAIN risk 数据集研
> 在线
> 研究risk数据集
> 730.0s
> BRAIN risk数据集研究
> ideating: 
> MCP: Brain-mcp Authenticate
> 724.0s
> )
> 是
> 是
> 不再询问此工具
> 否;并告诉 Claude 该如何不同地操作
> MCP: Brain-mcp Get Platfor
> 712.0s
> 是
> 是
> 不再询问此工具
> 否;并告诉 Claude 该如何不同地操作
> MCP: Brain-mcp Get Datasets
> 706
> 0s
> 在线
> 绕过所有权限
> 输入消息
> 岛
> 收件箱
> 终端
> 设置


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，这两天也被Clawdbot刷屏了

但我其实不明白的是，除了多了个聊天窗口控制的途径之外，这和我直接在Claude code中调用Skills有啥区别吗

===================================================================================


---

### 技术对话片段 182 (原帖: 手机远程连接claudecode，24小时随时指挥AI干活！经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 手机远程连接claudecode24小时随时指挥AI干活经验分享_37953156945687.md
- **时间**: 4个月前

**提问/主帖背景 (ZL81441)**:
最近Clawdbot太火了，我已经被Clawdbot刷屏两天了

他实现了WhatsApp, Telegram, Discord,直接和ai对话，并且可以远程指挥你的电脑干活
 
> [!NOTE] [图片 OCR 识别内容]
> 核心能力
> 具体表现
> 支持 WhatsApp` Telegram
> Discord。
> Slack。
> Signal
> 全平台融入
> iMessage:
> Microsoft Teams 等10+ 主流平台
> 收发邮件。管理日历。预定航班。控制智能家居。运行代砑
> 超越闲聊的执行力
> 操作文件系统
> 记住你的偏好。工作习惯和历史对话。 Al 会随着时间推移变得
> 持久记忆与个性化
> 越来越懂你
> 浏览器控制。命令行执行。文件读写
> 网络搜索。技能扩展系
> 强大的系统集成
> 统
> 本地优先与数据隐私
> 运行在你自己的设备上。数据完全在你的掌控之中
 

我也是第一时间部署到了自己的Mac mini上，老实说这个玩意权限确实有点大，想尝试的小伙伴还是整一台新的电脑或者是部署到vps上。我折腾了半天只跑通了千问的模型，使用下来觉得很兴奋，又有点小失望。兴奋是功能和潜力十分强大，交互方式十分的新颖。失望是配置起来简单，后续各种权限的设置等等，比想象的要复杂，感觉笨笨的（也不知道是不是千问的问题）

最让人失望的是他居然不能自动调用claudecode！也就是说我不能用它来帮助我做alpha工作。

于是我转念一想，用AI控制电脑，执行等 **这些功能，Claude Code 不是都有吗？**

区别在于Claude code只能在终端里交互，而 Clawdbot 让你能在聊天软件里用。 Clawdbot启发了我， **搭一座桥，把聊天软件连到 Claude Code。**

这两者原理如下：

```

```

Telegram │ ───▶ │ Bot 程序 │ ───▶ │ Claude Code

(你手机) │ ◀─── │ (你电脑) │ ◀─── │ (AI) │

```

```

1. 你在 Telegram 发消息
2. Bot 程序收到消息，转发给 Claude Code
3. Claude Code 执行任务（搜索、写文件、跑代码...）
4. Bot 程序把结果发回 Telegram

Bot 程序只是个"传话筒"，真正干活的是 Claude Code。

想法有了，于是我开始说干就干。啊不，我也不是程序员，于是我开始找开源社区有没有现成解决方案，在尝试了很多方案后失败，终于跑通了两个方案。

## **一 ：Telegram机器人**

仓库的地址如下 [[链接已屏蔽]) 
 
> [!NOTE] [图片 OCR 识别内容]
> Error: CUDA out of memory. Tried to allocate 19.36 GiB. GPU 0 has a total capacity of 47.40 GiB of which 11.47 GiB is free. Including non-PyTorch memory, this process has 1.49 GiB memory in use. Process 58488 has 11.00 GiB memory in use. Process 58482 has 12.66 GiB memory in use. Process 58486 has 10.76 GiB memory in use. Of the allocated memory 1.02 GiB is allocated by PyTorch, and 164.03 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  ([链接已屏蔽])
 

至于部署的方式，仓库readme文件写的比较详细，我这儿就不贴了。
如何创建telegram的机器人：

1. 打开Telegram，搜索
   [@Botfather]([链接已屏蔽])
2. 发送 /newbot
3. 按提示输入名称
4. 获得一个 Token （Use this token to access the HTTP API后面这一串英文和数字）

如果不会的话，可以直接把仓库地址和Token丢给Claudecode，让他来帮你安装。
最终成效
 
> [!NOTE] [图片 OCR 识别内容]
> 0.07
> 4G
> 5G
> 2.05
> 4G
> 5G
> 7:42
> KBIs
> VPN
> SIlsoll 100
> 7:42
> KBIs
> VPN
> Sl s511 100
> M
> Myclaude77_bot
> M
> Myclaude77_bot
> 机器人
> 机器人
> 可以了 ,
> 连接通了
> 07:05
> 使用改进alpha 技能
> 优化
> 07:10
> 好的
> 连接通了!有什么需要我帮忙的
> 吗?
> 输出每个变体的表现  07:28
> 07:05
> ##  所有变体表现对比
> 查看你有哪些技能
> 07:07
> 根据我的配置,
> 我有以下可用技能:
> ### Alpha IC。
> Tr7vJ (原始)
> ##规划与管理
> **表达式**:
> planning-with-files
> 复杂任务的文件式
> 规划 ,
> 创建 taskplenmd
> fingingsmg
> 2
> 和 progressmg
> H liz
> ## WorldQuant BRAIN 相关技能
> expression_verifier
> 验证 alpha 表达
> 式的语法
> **性能指标**:
> brain-improve-alpha-performance - 改
> 指标 |值 |
> 进 BRAIN alphas 的5步工作流
>  |
> brain-datafield-exploration-general
> Sharpe
> 2.28
> 评估 BRAIN 数据集的6种方法
> Fitness
> 1.93
> brain-feature-implementation
> 从
> Returns
> 13.81%
> markdown 文件实现 BRAIN features
> Drawdown
> 5.09%
> brain-explain-alphas
> 分析和解释
> Turnover
> 0.1925
> BRAIN alpha 表达式
> 2Y Sharpe
> 1.96
> brain-dataset-exploration-general
> 深
> Robust Sharpe
> **0.51**
> 入探索 BRAIN 数据集
> Sub Sharpe
> 0.67
> brain-calculate-alpha-selfcorrQuick
> 计算 alpha 自相关性
> *相关性**:
> brain-how-to-pass-AlphaTest
> Alpha
> 类型
> 值 |状态 |
> 提交测试的要求和改进建议
> 一-----
> 井'40丫 |7791
> 十 /71 |
> 二菜单
> 输入消息
> 二菜单
> 腧入消息


## **二：Happy coder app**

## （写稿的时候才发现，新手更加推荐！）
官方网站： [[链接已屏蔽])

电脑终端输入代码
npm i -g happy-coder && happy

 
> [!NOTE] [图片 OCR 识别内容]
> Happy Coder
> Bulka, LLC
> 』
> 应用内购商品
> 4.9太
> 1万+
> 838条评价
> 次下载
> 3岁以上 @
> 安装
> 分享
> 添加到心愿单
> 6
> 在您的设备上可以使用此应用
> Code everything, everywhere,allat once
> Realtime Voice with multiple sessions
> Review changes or
> 应用支持
> ~
> PA?
> 8:123
> ODEITUIICLUebeIUely Uuray: MacerI NoJe.ls Refiesh
> ODEITUIICLUebeIUely Uuray: MacerI NoJe.ls Refiesh
> 臼 {erglstoiciDrvelop;opentunnelisrc
>  Urcp
> 1
> OITrsm
> Migration; Comp eta
> TEWTR ICn
> IL=Col
> ASTCIRPTCF DTET
> Cmson{
> IaT4
> Lontend
> 7 M +
> 7 1373
> C TTTaTT
> CIidr1
> U111(1LO?n SN SU4aICHII
> IIITTT
> LITII
> U^
> CmrInder
> Tronzend ;Frontendsessionts
> AICTTt
> sttrllon
> TTon
> eoncttrTent
> 类似应用
> CTTU'
> R11
> ITCie;T
> Etrof Hindllire
> TmTanmN+o7 7 Lm
> IIDOIt
> startrzomen
>  zonzeno'startFTOIC2NO
> Dinn
> Updated Iosger contiguration
> IhTanSOCTf Snta
> SIC !utils WodeTTaCter
> IIDoIt
> + Tngm
> _e++1LS
> N Ftah  RLLel fttyitl
> TH i f h API
> I
> Would you prefer re to:
>  
> CorrSrlt:Li51L'lu
> TT
> Vsti:
> KeED the CUrrenL Complete Upqrade Tcomierge]
> SETLII
> IorIn|
> TFHIITT
> 'TUe551111
> TypeScrpt compilation: Allerrols resolyed
> Rewert
> original state and do on; NATS upsrade Trst
> 记账城市 -用每笔收支。
> 建造你的城市
> UTC Cet
> Norin orresl;
> Show you the specific NATS changes
> detail
> TmstTnsT
> T !TTnf
> CLI functionalty: Al ccmmands cperational with properhelp text
> lot hardled
> +1153
> T1ntu
> the Currentapprouch
> thalall dependencies Iork togetherard are tested 25 3 corr plele
> FOR UNE
> SPARKFUL
> Orn OISINiti
> Cxisting functicnality wile moderizins
> TTII
> atcwl'CU preter
> CIRTaT
> ICMm
> TUIIII?
> thc lalest,Irost
> NII
> T[TIsrr
> allldeperdencies, takirg
> CTpli'fTn-on'
> fulladyantage
> modlern Nadels features and improed TypeScript supnor!
> SI
> TtT
> 21T
> iTmin?
> C+
> 4.1大
> mntzn
> OTT
>  Listeninn http port]
> Type
> 35530
> Ttoni
> SOTOTC
> LISTs
> 53TOT Frdmmints
> TImSe
> KOIC
> frsl te NATS Uperade?
> aCLionI Iuntlon
> CNOOb
> maste
> 1 Fnr
> L79.12
>  +-
> CLIUIIs '
> LI
> TILO '
> MTCETtan
> Lant m5
> ACCIC
> UUShe NSTC
> Jprade hrst, but Iie aread; ccrpleted the fJll
> UIT个
> RnT
> goTnRI
> 922n.
> Jeperdeney upgrade inludin the NRIS risration frorm Is rals to nals j5
> TTO
> CMUNI
> +」cOTtTUNL
> 3095
> st+Fomo |
> httppor, CaObJ.51
> PRO
> Lel ie shoi you Vha Nas dore
> specifial' [or .he IATs Jpsrade:
> Let UULt
> OMtLuI'
> UdseTTLubtJuIs
> 9239
> Lel IttP'
> optyons-pl
> y」SLTItLuutiur
> SLarLF OTeIIoI 
> HLLPO', OITonss1
> PR
> FI|
> CNITN
> VII stI (o I h(CHG WT
> '' 
> Overload Apps
> MLIII'
> T
> NATS,
> Durl
 
appstore或者play商店搜索happy coder下载

APP扫码终端二维码即可绑定，流程更加简单快捷，UI交互也更全面友好！
 
> [!NOTE] [图片 OCR 识别内容]
> 0.75
> 46
> 56
> 0.00
> 46
> 56
> 8:27
> KB/s
> VPN
> S5
> 99
> 8:25
> KBIs
> VPN
> SIsl
> 99
> 终端
> BRAIN risk数据集研究
> 已连接
> ~/Downloads/Claudebot
> ~|Downloads/Claudebot
> 启动ind auto angent,
> 研究-Frisk数据集
> Claudebot
> Title changed to
> BRAIN risk 数据集研
> 在线
> 研究risk数据集
> 730.0s
> BRAIN risk数据集研究
> ideating: 
> MCP: Brain-mcp Authenticate
> 724.0s
> )
> 是
> 是
> 不再询问此工具
> 否;并告诉 Claude 该如何不同地操作
> MCP: Brain-mcp Get Platfor
> 712.0s
> 是
> 是
> 不再询问此工具
> 否;并告诉 Claude 该如何不同地操作
> MCP: Brain-mcp Get Datasets
> 706
> 0s
> 在线
> 绕过所有权限
> 输入消息
> 岛
> 收件箱
> 终端
> 设置


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享，这两天也被Clawdbot刷屏了

但我其实不明白的是，除了多了个聊天窗口控制的途径之外，这和我直接在Claude code中调用Skills有啥区别吗

===================================================================================


---

### 技术对话片段 183 (原帖: 新的AI比赛来了，我该采取什么策略？)
- **原帖链接**: [Commented] 新的AI比赛来了我该采取什么策略.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
大家应该已经看到，我们激动人心的AI比赛已经开启。下周将有相关的官方介绍课（Global Event, in English)，欢迎大家线上报名并了解规则。目前，您可以采取的策略是，尽量多提交各种数据集的多样化Alpha。不急于一时的排行榜。

现在需要做的准备工作有两个：1. 尽量多提交各种数据集的多样化Alpha 2.学会使用各大厂商的GPT，尤其是其API的方式，最好再学习Langraph package.

下周的讲课嘉宾是谁呢？好难猜啊。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

真的猜不出来，讲课嘉宾该不会是帅气的Weijie老师吧，期待住了
期待下周的官方介绍课！

===================================================================================


---

### 技术对话片段 184 (原帖: 新的AI比赛来了，我该采取什么策略？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新的AI比赛来了我该采取什么策略_35590359150103.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
大家应该已经看到，我们激动人心的AI比赛已经开启。下周将有相关的官方介绍课（Global Event, in English)，欢迎大家线上报名并了解规则。目前，您可以采取的策略是，尽量多提交各种数据集的多样化Alpha。不急于一时的排行榜。

现在需要做的准备工作有两个：1. 尽量多提交各种数据集的多样化Alpha 2.学会使用各大厂商的GPT，尤其是其API的方式，最好再学习Langraph package.

下周的讲课嘉宾是谁呢？好难猜啊。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

真的猜不出来，讲课嘉宾该不会是帅气的Weijie老师吧，期待住了
期待下周的官方介绍课！

===================================================================================


---

### 技术对话片段 185 (原帖: 稳稳拿下gm，combine到六维的耕耘经验经验分享)
- **原帖链接**: [Commented] 稳稳拿下gmcombine到六维的耕耘经验经验分享.md
- **时间**: 24天前

**提问/主帖背景 (YQ84572)**:

> [!NOTE] [图片 OCR 识别内容]
> Genius level: Grandmaster
> Best level: Grandmaster
> Current quarter end: June 3oth, 2026
> 1
> Eligibility Criteria
> 2026-02,April Tst 2026
> June 3oth, 2026
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 106
> 14 more to Master
> 120
> 220
> Pyramids Completed
> 22
> 8 more to Master
> Combined Alpha Performance
> 2.66
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 1.49
> 0.51 more to Grar
> API 清求监视器
> apiworldquantbraincom
> 展开
> 黹空
 
 
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2026-01.January 1st 2026
> March 31st. 2026
> Operators per Alpha
> Operators Used
> Fields per Alpha
> 3.48
> 133
> 1.29
> Fields Used
> ~ommunity actiity
> Max
> simulation streak
> 246
> 40.5
> 262
 当上一季度combine远远超2.0之后我就开始了六维的耕耘，在保持combine步降反升的前提下维持六维并稳稳拿下了gm。来给新人一些建议，想冲gm的话自身的combine一定要达标，然后要规划好点塔和因子质量在三个月份里，时刻关注全球大会拿清下一步平台的主题动向。跟着平台的主题去进行点塔。不要偷懒想着季度中再进行冲刺，制定好这个季度的计划才能有足够的时间控制六维与稳住combine

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 这combine真是让人羡慕啊

接大佬的好运 祝自己也能拿到GM

=============================================================================


---

### 技术对话片段 186 (原帖: 稳稳拿下gm，combine到六维的耕耘经验经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 稳稳拿下gmcombine到六维的耕耘经验经验分享_40294373064855.md
- **时间**: 24天前

**提问/主帖背景 (YQ84572)**:

> [!NOTE] [图片 OCR 识别内容]
> Genius level: Grandmaster
> Best level: Grandmaster
> Current quarter end: June 3oth, 2026
> 1
> Eligibility Criteria
> 2026-02,April Tst 2026
> June 3oth, 2026
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 106
> 14 more to Master
> 120
> 220
> Pyramids Completed
> 22
> 8 more to Master
> Combined Alpha Performance
> 2.66
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 1.49
> 0.51 more to Grar
> API 清求监视器
> apiworldquantbraincom
> 展开
> 黹空
 
 
> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2026-01.January 1st 2026
> March 31st. 2026
> Operators per Alpha
> Operators Used
> Fields per Alpha
> 3.48
> 133
> 1.29
> Fields Used
> ~ommunity actiity
> Max
> simulation streak
> 246
> 40.5
> 262
 当上一季度combine远远超2.0之后我就开始了六维的耕耘，在保持combine步降反升的前提下维持六维并稳稳拿下了gm。来给新人一些建议，想冲gm的话自身的combine一定要达标，然后要规划好点塔和因子质量在三个月份里，时刻关注全球大会拿清下一步平台的主题动向。跟着平台的主题去进行点塔。不要偷懒想着季度中再进行冲刺，制定好这个季度的计划才能有足够的时间控制六维与稳住combine

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 这combine真是让人羡慕啊

接大佬的好运 祝自己也能拿到GM

=============================================================================


---

### 技术对话片段 187 (原帖: 穿透参数迷雾：量化策略的敏感度分析与鲁棒性构建)
- **原帖链接**: [Commented] 穿透参数迷雾量化策略的敏感度分析与鲁棒性构建.md
- **时间**: 2个月前

**提问/主帖背景 (WW74101)**:
在量化交易的“炼金术”中，策略开发者常常面临一个核心困境：我们精心调优出的“最优参数”，究竟是捕捉到了市场的普适规律，还是仅仅“记住”了历史数据中的特定噪声？当市场环境悄然转变，一个依赖于某个精确“神奇数字”的策略，其盈利能力可能会如沙堡般迅速瓦解。

参数敏感度分析，正是破解这一困境、检验策略鲁棒性的关键工具。它并非追求参数的“最优”，而是探寻策略表现的“稳定”。本文将系统性地阐述如何进行参数敏感度分析，帮助你将脆弱的策略“尖峰”锻造成稳健的“高原”。

**为何要进行敏感度分析？**

量化策略的本质是一系列逻辑规则，而这些规则往往由参数驱动。无论是移动平均线的周期、RSI指标的阈值，还是止损的比例，参数的微小变动都可能对最终的收益曲线产生“蝴蝶效应”。

进行敏感度分析的核心目的有三：

1. 诊断过拟合：识别策略是否过度依赖于历史数据中的特定片段。
2. 评估鲁棒性：衡量策略在未来未知市场环境下的适应能力。
3. 理解策略逻辑：洞察不同参数对策略风险和收益的贡献程度。

一个优秀的策略，其表现不应是悬崖峭壁上的孤峰，而应是广袤平原上的高地——即使参数在一定范围内有所偏离，其核心盈利能力依然稳固。

**系统性分析的三步法**

进行参数敏感度分析，可以遵循一套清晰的“定义-测试-解读”流程。

第一步：确立基准与划定边界

一切分析的起点，是你通过初步回测或逻辑推导演绎出的一组“基准参数”。这组参数代表了你对策略在当前市场环境下的最优理解。

围绕这组基准，你需要为每个待分析的核心参数划定一个合理的测试边界。这个范围不宜过宽，以免引入不切实际的场景；也不宜过窄，否则无法检验其稳定性。一个常见的经验法则是，在基准值的基础上进行 ±20% 的浮动。同时，确定一个合适的测试步长，例如在该范围内均匀选取5到10个测试点。

**第二步：执行扰动与测试**

这是分析的核心环节，主要有两种经典的测试方法：

- 单参数分析法：这种方法遵循“控制变量”的科学原则。每次仅对一个参数进行扰动，使其在预设范围内变化，同时保持其他所有参数不变。通过观察策略表现（如夏普比率、最大回撤）随单一参数的变化曲线，可以清晰地识别出该参数的独立影响力。它的优点是逻辑直观，易于解读。
- 多参数网格搜索法：这种方法更为全面，它系统地测试多个参数的所有可能组合。例如，同时改变快线和慢线均线的周期，形成一个参数矩阵。虽然计算成本更高，但它能揭示参数之间复杂的相互作用关系，帮助你找到那些在单参数分析中无法发现的稳定区域。

**第三步：可视化与深度解读**

将测试结果转化为图形，是解读敏感度分析结果最有效的方式。

- 寻找“参数高原”：理想的结果是在图表上看到一个宽阔、平坦的“高原”区域。在这个区域内，策略的绩效指标（如夏普比率）始终维持在较高水平，对参数的具体取值不敏感。这表明策略的盈利逻辑是坚实且普适的。
- 警惕“参数尖峰”：最需要警惕的信号是，策略的优异表现仅集中在某个非常狭窄的参数点上，形成一个孤立的“尖峰”，而周围的参数组合表现都急剧下滑。这是过拟合的典型特征，意味着该策略在实盘中极不可靠，应果断舍弃。
- 巧用热力图：对于双参数分析，热力图是绝佳的可视化工具。横纵坐标代表两个参数，颜色的深浅则代表绩效指标的高低。一张优秀的热力图，会呈现出大片颜色相近的“高原”，而非零星的亮点。

**️ 进阶：从分析到风控**

参数敏感度分析不应仅仅是一次性的诊断工具，更应成为策略上线前的一道标准化风控流程。

你可以为策略设定明确的“鲁棒性阈值”。例如，规定当核心参数在 ±10% 的范围内变动时，策略的夏普比率衰减不得超过 15%。任何无法通过此测试的策略，都将被标记为“脆弱”，需要重新审视其底层逻辑或直接被淘汰。

通过这套系统性的方法，你不仅能筛选出更具生命力的策略，更能深刻理解策略盈利的来源与边界，从而在充满不确定性的市场中，建立起真正的竞争优势。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！这下终于明白如何解读这些鲁棒性检验的结果了！

希望Combine也能继续上涨~

=============================================================================


---

### 技术对话片段 188 (原帖: 穿透参数迷雾：量化策略的敏感度分析与鲁棒性构建)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 穿透参数迷雾量化策略的敏感度分析与鲁棒性构建_39854893045655.md
- **时间**: 2个月前

**提问/主帖背景 (WW74101)**:
在量化交易的“炼金术”中，策略开发者常常面临一个核心困境：我们精心调优出的“最优参数”，究竟是捕捉到了市场的普适规律，还是仅仅“记住”了历史数据中的特定噪声？当市场环境悄然转变，一个依赖于某个精确“神奇数字”的策略，其盈利能力可能会如沙堡般迅速瓦解。

参数敏感度分析，正是破解这一困境、检验策略鲁棒性的关键工具。它并非追求参数的“最优”，而是探寻策略表现的“稳定”。本文将系统性地阐述如何进行参数敏感度分析，帮助你将脆弱的策略“尖峰”锻造成稳健的“高原”。

**为何要进行敏感度分析？**

量化策略的本质是一系列逻辑规则，而这些规则往往由参数驱动。无论是移动平均线的周期、RSI指标的阈值，还是止损的比例，参数的微小变动都可能对最终的收益曲线产生“蝴蝶效应”。

进行敏感度分析的核心目的有三：

1. 诊断过拟合：识别策略是否过度依赖于历史数据中的特定片段。
2. 评估鲁棒性：衡量策略在未来未知市场环境下的适应能力。
3. 理解策略逻辑：洞察不同参数对策略风险和收益的贡献程度。

一个优秀的策略，其表现不应是悬崖峭壁上的孤峰，而应是广袤平原上的高地——即使参数在一定范围内有所偏离，其核心盈利能力依然稳固。

**系统性分析的三步法**

进行参数敏感度分析，可以遵循一套清晰的“定义-测试-解读”流程。

第一步：确立基准与划定边界

一切分析的起点，是你通过初步回测或逻辑推导演绎出的一组“基准参数”。这组参数代表了你对策略在当前市场环境下的最优理解。

围绕这组基准，你需要为每个待分析的核心参数划定一个合理的测试边界。这个范围不宜过宽，以免引入不切实际的场景；也不宜过窄，否则无法检验其稳定性。一个常见的经验法则是，在基准值的基础上进行 ±20% 的浮动。同时，确定一个合适的测试步长，例如在该范围内均匀选取5到10个测试点。

**第二步：执行扰动与测试**

这是分析的核心环节，主要有两种经典的测试方法：

- 单参数分析法：这种方法遵循“控制变量”的科学原则。每次仅对一个参数进行扰动，使其在预设范围内变化，同时保持其他所有参数不变。通过观察策略表现（如夏普比率、最大回撤）随单一参数的变化曲线，可以清晰地识别出该参数的独立影响力。它的优点是逻辑直观，易于解读。
- 多参数网格搜索法：这种方法更为全面，它系统地测试多个参数的所有可能组合。例如，同时改变快线和慢线均线的周期，形成一个参数矩阵。虽然计算成本更高，但它能揭示参数之间复杂的相互作用关系，帮助你找到那些在单参数分析中无法发现的稳定区域。

**第三步：可视化与深度解读**

将测试结果转化为图形，是解读敏感度分析结果最有效的方式。

- 寻找“参数高原”：理想的结果是在图表上看到一个宽阔、平坦的“高原”区域。在这个区域内，策略的绩效指标（如夏普比率）始终维持在较高水平，对参数的具体取值不敏感。这表明策略的盈利逻辑是坚实且普适的。
- 警惕“参数尖峰”：最需要警惕的信号是，策略的优异表现仅集中在某个非常狭窄的参数点上，形成一个孤立的“尖峰”，而周围的参数组合表现都急剧下滑。这是过拟合的典型特征，意味着该策略在实盘中极不可靠，应果断舍弃。
- 巧用热力图：对于双参数分析，热力图是绝佳的可视化工具。横纵坐标代表两个参数，颜色的深浅则代表绩效指标的高低。一张优秀的热力图，会呈现出大片颜色相近的“高原”，而非零星的亮点。

**️ 进阶：从分析到风控**

参数敏感度分析不应仅仅是一次性的诊断工具，更应成为策略上线前的一道标准化风控流程。

你可以为策略设定明确的“鲁棒性阈值”。例如，规定当核心参数在 ±10% 的范围内变动时，策略的夏普比率衰减不得超过 15%。任何无法通过此测试的策略，都将被标记为“脆弱”，需要重新审视其底层逻辑或直接被淘汰。

通过这套系统性的方法，你不仅能筛选出更具生命力的策略，更能深刻理解策略盈利的来源与边界，从而在充满不确定性的市场中，建立起真正的竞争优势。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享！这下终于明白如何解读这些鲁棒性检验的结果了！

希望Combine也能继续上涨~

=============================================================================


---

### 技术对话片段 189 (原帖: 行业中性加时序标准化：一个干净的 Alpha 模板Alpha Template)
- **原帖链接**: [Commented] 行业中性加时序标准化一个干净的 Alpha 模板Alpha Template.md
- **时间**: 21天前

**提问/主帖背景 (WX18521)**:
一个常见但实用的 Alpha 因子模板，拆开看就是三层：

```
ts_scale(
    group_rank(
        mdl250_maltahc_eq_score,
        industry
    ),
    30
)
```

1. 内层：`mdl250_maltahc_eq_score`
- 每只证券的主复合机器学习 Alpha 分数，概括了整体 ML 模型在目标预测周期内的选股信号；分值越高，预期相对收益越强。
- 本质上是一个 ML 生成的原始分数。本身已有预测能力，但需要中性化和归一化处理。

2. 中间层：`group_rank(..., industry)`
- 在每个行业内独立做百分位排名
- 输出范围：0~1（行业内）
- 作用：消除行业偏差，避免某些行业因系统性波动主导信号

3. 外层：`ts_scale(..., 30)`
- 对上述行业内排名，按过去30个时间截面做标准化
- ts_scale(x, d, constant) = (x - ts_min(x, d)) / (ts_max(x, d) - ts_min(x, d)) + constant
- 作用：让因子值在不同截面之间可比，去除时序上的趋势和波动差异

最终输出
一个行业内相对排序 + 时序上分布稳定的因子值，范围通常在 0~1 或 z-score 形式。

变体思路

- 30 是超参，可尝试 22 /66 /120 /240
- `ts_rank(group_rank(...), 30)` — 保留排序信息但不做标准化
- `ts_zscore(group_rank(...), 30)` — 明确用 z-score 版本
- 叠加市值中性：`group_rank(...,bucket(rank(cap), range='0.1, 1, 0.1'))`

已提交因子，包含ind、eur、mea地区，其他地区暂未尝试


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> 15
> 05
> 目
> Single Data Set Alpha
> 自
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: EUR/DIIMODEL X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.71
> 8.309
> 1.02
> 4.449
> 4.259
> 10.699oo



> [!NOTE] [图片 OCR 识别内容]
> 1IS Summary
> Period
> 15
> 05
> 自
> Single Data Set Alpha
> 自
> Power Pool Alpha
> 自
> Regular Alpha
> Pyramid theme: MEA/DIIMODEL X1.3
> ggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.68
> 4.51%
> 1.50
> 9.989
> 14.579
> 44.309oo
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0S
> 自
> Single Data Set Alpha
> u Regular Alpha
> Pyramid theme: IND/DIIOTHER X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.03
> 12.51 %
> 1.68
> 8.569
> 6.369
> 13.689o。
  
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> 15
> 05
> 目
> Single Data Set Alpha
> 自
> Power Pool Alpha
> 目
> Regular Alpha
> Pyramid theme: EUR/DIIMODEL X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.71
> 12.279
> 2.07
> 7.299
> 2.239
> 11.8796o0
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> 15
> 05
> 自
> Single Data Set Alpha
> 自
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: EUR/DIIFUNDAMENTAL X1.1
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.89
> 6.979
> 1.05
> 3.839
> 2.789
> 11.00%oo


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 模板很简洁  解释的也很清楚 看起来alpha效果也不错

这就准备去试试

=============================================================================


---

### 技术对话片段 190 (原帖: 行业中性加时序标准化：一个干净的 Alpha 模板Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 行业中性加时序标准化一个干净的 Alpha 模板Alpha Template_40902892248983.md
- **时间**: 21天前

**提问/主帖背景 (WX18521)**:
一个常见但实用的 Alpha 因子模板，拆开看就是三层：

```
ts_scale(
    group_rank(
        mdl250_maltahc_eq_score,
        industry
    ),
    30
)
```

1. 内层：`mdl250_maltahc_eq_score`
- 每只证券的主复合机器学习 Alpha 分数，概括了整体 ML 模型在目标预测周期内的选股信号；分值越高，预期相对收益越强。
- 本质上是一个 ML 生成的原始分数。本身已有预测能力，但需要中性化和归一化处理。

2. 中间层：`group_rank(..., industry)`
- 在每个行业内独立做百分位排名
- 输出范围：0~1（行业内）
- 作用：消除行业偏差，避免某些行业因系统性波动主导信号

3. 外层：`ts_scale(..., 30)`
- 对上述行业内排名，按过去30个时间截面做标准化
- ts_scale(x, d, constant) = (x - ts_min(x, d)) / (ts_max(x, d) - ts_min(x, d)) + constant
- 作用：让因子值在不同截面之间可比，去除时序上的趋势和波动差异

最终输出
一个行业内相对排序 + 时序上分布稳定的因子值，范围通常在 0~1 或 z-score 形式。

变体思路

- 30 是超参，可尝试 22 /66 /120 /240
- `ts_rank(group_rank(...), 30)` — 保留排序信息但不做标准化
- `ts_zscore(group_rank(...), 30)` — 明确用 z-score 版本
- 叠加市值中性：`group_rank(...,bucket(rank(cap), range='0.1, 1, 0.1'))`

已提交因子，包含ind、eur、mea地区，其他地区暂未尝试


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> 15
> 05
> 目
> Single Data Set Alpha
> 自
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: EUR/DIIMODEL X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.71
> 8.309
> 1.02
> 4.449
> 4.259
> 10.699oo



> [!NOTE] [图片 OCR 识别内容]
> 1IS Summary
> Period
> 15
> 05
> 自
> Single Data Set Alpha
> 自
> Power Pool Alpha
> 自
> Regular Alpha
> Pyramid theme: MEA/DIIMODEL X1.3
> ggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.68
> 4.51%
> 1.50
> 9.989
> 14.579
> 44.309oo
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0S
> 自
> Single Data Set Alpha
> u Regular Alpha
> Pyramid theme: IND/DIIOTHER X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.03
> 12.51 %
> 1.68
> 8.569
> 6.369
> 13.689o。
  
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> 15
> 05
> 目
> Single Data Set Alpha
> 自
> Power Pool Alpha
> 目
> Regular Alpha
> Pyramid theme: EUR/DIIMODEL X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.71
> 12.279
> 2.07
> 7.299
> 2.239
> 11.8796o0
  
> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> 15
> 05
> 自
> Single Data Set Alpha
> 自
> Power Pool Alpha
> Regular Alpha
> Pyramid theme: EUR/DIIFUNDAMENTAL X1.1
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.89
> 6.979
> 1.05
> 3.839
> 2.789
> 11.00%oo


**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢大佬分享 模板很简洁  解释的也很清楚 看起来alpha效果也不错

这就准备去试试

=============================================================================


---

### 技术对话片段 191 (原帖: 谷歌Antigravity 如何使用Skills)
- **原帖链接**: [Commented] 谷歌Antigravity 如何使用Skills.md
- **时间**: 5个月前

**提问/主帖背景 (CW62372)**:
谷歌Antigravity 也快速跟进Skills了。相关文档：  [[链接已屏蔽])

为什么使用 Antigravity？因为它现在甚至不需要学生认证就可以免费使用gemini3 pro，安装也比claude code和gemini-cli简单，只需梯子开tun模式就可以登录成功，gemini-cli还需要踩几步坑，claude code 需要花不少token钱。

它有两种配置模式，当前项目和全局：

Location
      Scope

  <workspace-root>/.agent/skills/<skill-folder>/

      当前项目

  ~/.gemini/antigravity/skills/<skill-folder>/

      所有项目

Skills 是 **可复用的知识包** ，用于扩展 Agent 的能力。每个 Skill 包含

.agent/skills/my-skill/

├── SKILL.md # 主指令文件（必需）

├── scripts/ # 辅助脚本（可选）

├── examples/ # 参考实现（可选）

└── resources/ # 模板和资源（可选）

Antigravity 如何 使用这次cnhkmcp中的skills：

- 首先你得有一个google账号；

- 下载  [[链接已屏蔽]) 或将antigravity更新到最新；

- 在你的项目下新建一个.agent目录；

- 把cnhkmcp中skills目录复制到.agent目录下；

- 把skills目录下，相关例子中，路径中的claude用全局替换，全部换成agent（路径原因）

超级简单，配置好后，你可以问一下ai，你有什么skills，就可以知道有没有成功。

再说下为什么使用Skills

Skills 功能的核心优势在于将 **“专家级**  **经验”** 与 **“标准化**  **流程”** 封装在一起，让复杂任务的执行变得极其高效且可靠。

具体来说，它的优势主要体现在以下几点：

1. **极高的执**  **行标准**

- **问题** : 面对复杂任务（如“优化Alpha”），普通的 AI 可能会漏掉步骤，或者每次执行的逻辑不一致。

- **优势** : Skill 强制严格遵循 SKILL.md 中定义的最佳实践流程。这就像是把一位资深专家的 SOP（标准作业程序）直接植入到了agent的大脑中，确保每一步都精确无误。

1. **附带工具**  **与自动化**

- **问题** : 纯对话只能提供建议，无法直接跑复杂的本地计算。

- **优势** : Skill 文件夹里不仅有说明书，还可以包含 Python 脚本、参考数据文件等。

1. **沟通效率**

- **问题** : 以前做复杂任务，您可能需要写几百字的 Prompt 来规定我要怎么做。

- **优势** : 现在只需要说“用那个优化 Alpha 的技能”，agent 就会自动读取几千字的详细指令。这大大节省了沟通成本。

期待大家的skills了

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享!  谷歌大善人给的Antigravity确实很好用，只是不知道还能这样爽用多久哈哈

===================================================================================


---

### 技术对话片段 192 (原帖: 谷歌Antigravity 如何使用Skills)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 谷歌Antigravity 如何使用Skills_37701654477847.md
- **时间**: 5个月前

**提问/主帖背景 (CW62372)**:
谷歌Antigravity 也快速跟进Skills了。相关文档：  [[链接已屏蔽])

为什么使用 Antigravity？因为它现在甚至不需要学生认证就可以免费使用gemini3 pro，安装也比claude code和gemini-cli简单，只需梯子开tun模式就可以登录成功，gemini-cli还需要踩几步坑，claude code 需要花不少token钱。

它有两种配置模式，当前项目和全局：

Location
      Scope

  <workspace-root>/.agent/skills/<skill-folder>/

      当前项目

  ~/.gemini/antigravity/skills/<skill-folder>/

      所有项目

Skills 是 **可复用的知识包** ，用于扩展 Agent 的能力。每个 Skill 包含

.agent/skills/my-skill/

├── SKILL.md # 主指令文件（必需）

├── scripts/ # 辅助脚本（可选）

├── examples/ # 参考实现（可选）

└── resources/ # 模板和资源（可选）

Antigravity 如何 使用这次cnhkmcp中的skills：

- 首先你得有一个google账号；

- 下载  [[链接已屏蔽]) 或将antigravity更新到最新；

- 在你的项目下新建一个.agent目录；

- 把cnhkmcp中skills目录复制到.agent目录下；

- 把skills目录下，相关例子中，路径中的claude用全局替换，全部换成agent（路径原因）

超级简单，配置好后，你可以问一下ai，你有什么skills，就可以知道有没有成功。

再说下为什么使用Skills

Skills 功能的核心优势在于将 **“专家级**  **经验”** 与 **“标准化**  **流程”** 封装在一起，让复杂任务的执行变得极其高效且可靠。

具体来说，它的优势主要体现在以下几点：

1. **极高的执**  **行标准**

- **问题** : 面对复杂任务（如“优化Alpha”），普通的 AI 可能会漏掉步骤，或者每次执行的逻辑不一致。

- **优势** : Skill 强制严格遵循 SKILL.md 中定义的最佳实践流程。这就像是把一位资深专家的 SOP（标准作业程序）直接植入到了agent的大脑中，确保每一步都精确无误。

1. **附带工具**  **与自动化**

- **问题** : 纯对话只能提供建议，无法直接跑复杂的本地计算。

- **优势** : Skill 文件夹里不仅有说明书，还可以包含 Python 脚本、参考数据文件等。

1. **沟通效率**

- **问题** : 以前做复杂任务，您可能需要写几百字的 Prompt 来规定我要怎么做。

- **优势** : 现在只需要说“用那个优化 Alpha 的技能”，agent 就会自动读取几千字的详细指令。这大大节省了沟通成本。

期待大家的skills了

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

感谢大佬分享!  谷歌大善人给的Antigravity确实很好用，只是不知道还能这样爽用多久哈哈

===================================================================================


---

### 技术对话片段 193 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 近8000刀Master赚到了GM的Quarterly Payment论坛精选_41000341056791.md
- **时间**: 17天前

**提问/主帖背景 (MY56787)**:
标题党了，抱歉！实际上离真正的Grandmaster还有不小的距离。不过2026 Q1的Quarterly Payment确实创了我个人新高——7000多美元（如下图），接近Master档位的上限。鉴于论坛上Master级别顾问分享收入的帖子较少，特将个人情况整理成文，希望能给正在爬坡的顾问们一点正能量和参考。


> [!NOTE] [图片 OCR 识别内容]
> 202601 Payment
> 05/27/2026
> 0S$7,266.03


根据Genius的薪酬体系，Master级别的Quarterly Payment区间是在2000至8000美元。过去我一直认为能在下限基础上有所增加便已满足，完全不敢奢望触及上限。而这次的突破，不仅证明了Brain设定的Quarterly Payment区间并非形同虚设，也验证了拿到接近上限是可能的。

Quarterly Payment的决定性参数主要依赖于 Value Factor 和 Weight Factor。本次能取得突破，主要得益于这两项指标阶段性冲高的共同作用：最近一次Value Factor达到了0.99（此前两次更新分别是0.96，0.97），且Weight Factor创下了我成为顾问以来的单季最大增幅。

关于 **Value Factor**

此前借鉴大佬们的经验，建议在单月周期集中火力“竖向点塔”或深耕两三个Region。但在今年3月，为了点塔我在部分区域仅提交了少量Alpha，导致布局被动分散。然而，这种 **非刻意的分散改变了自身以往的行为模式** 反而可能被系统算法判定为一种“进步”?当然，这也可能与近期Alpha在OS阶段碰巧表现优异有关，而非纯粹归功于这种Diversity。

论坛关于高Value Factor的经验分享已经非常多，我的做法是在保障Alpha提交频率和数量的基础上，优先筛选符合以下条件的Alpha，也许能加持Value Factor的提升：

1. **PNL**  **曲线形态择优** ：只保留走势平滑、持续向上的收益曲线，坚决舍弃厂型、抛物线型等波动畸形的Alpha。
2. **长期收益指标稳步向上** ：年度IS各项考核指标保持均衡，核心关注近2-3年夏普比率等核心收益指标，优先选择持续稳步提升的Alpha，规避指标逐年衰减的标的。
3. **多空仓位结构均衡** ：严格把控Long-count与Short-count比例，避免多空失衡。
4. **严控相关性阈值** ：在自我相关性、组合相关性＜0.7的基础上，优先筛选相关性更低的Alpha，最大程度降低组合内冗余度。
5. **具备组合增益价值** ：不苛求单条Alpha全维度指标最优，但必须保证其入池后，能为组合至少一项核心指标带来正向增益，且最好是近2-3年增益效果具备持续性。
6. **多维建模实现多样性** ：尽量覆盖不同数据类型、不同数据集，地区维度可长期分散布局，无需追求单月区域完全均衡，通过多维差异化构建提升组合多样性。
7. **依托测试期校验稳定性** ：熟练运用Test-period功能，以近2年数据为核心测试区间，筛选训练期与测试期表现一致、无明显收益衰减的高一致性Alpha。
8. **强化Alpha稳健性测试** ：对比新老Alpha的历史表现，优先选择收益和风险指标波动小、表现稳定的稳健型Alpha，剔除容错率低的脆弱Alpha。
9. **坚守经济学可解释性** ：所有提交的Alpha必须具备清晰的表达式逻辑与合理的底层经济学逻辑，杜绝无逻辑Alpha提交。
10. **稀缺性适度放宽标准** ：对于独特idea、小众稀缺数据集产出的Alpha，可在非核心指标上适度放宽筛选标准。

关于 **Weight Factor**

本次季度收益的另一助力，来自一季度Weight Factor的阶段性大幅增长，也是我成为研究顾问以来，单季增幅最突出的阶段。不过从二季度开始，我的Weight Factor已呈现持续回落趋势，对应的selected combine同步下降，目前暂未摸索出新一轮的突破方法。

此前我发布过复盘帖 *[《6个月Weight Factor从0.03到35+的自我复盘分享》]([Commented] 【Community Leader -因子筛选与组合】6个月Weight Factor从003到35的自我复盘分享经验分享_37180534933911.md)* ，有需要的顾问可以自行翻阅参考，核心经验总结如下：

1. **跳出单一相关性判断维度** ：Alpha多样性不能只看相关性数据，更要从Alpha设置、构建逻辑、收益表现、功能定位多维度打磨，丰富个人Alpha池的“品类多样性”，搭建专属“Alpha超市”，提升被PM、平台筛选入选的概率。

2. **高适配Alpha优先布局** ：大地区、高流动性、D1、risk-neut、使用主流数据类型、prod-correlation<0.7、PNL走势正常的ATOM Alpha，可能具备更高的入选优先级。

关于Osmosis机制的不确定性

值得一提的是，Osmosis机制在本次Quarterly Payment中似乎尚未体现出明显影响。由于我的Osmosis 日间表现波动较大，经过几次调整后Combine仍未见明显改善。目前尚不确定该机制在未来会对整体收益带来多大权重的影响，后续我将持续跟踪并适时调整策略。

最后，省流版总结：

**Value Factor**  **靠持续高质量交付+自我行为模式进化；**

**Weight Factor**  **靠丰富自我的“Alpha超市”增加被选概率；**

**以上两项如果不能持续保持高值，就策略性阶段性冲高。**

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

恭喜大佬 感谢大佬分享这么详细的经验贴

想问下大佬有专门多做小地区吗？毕竟听说小地区更容易上weight

=============================================================================


---

### 技术对话片段 194 (原帖: 这个因子到底有没有混信号？【传奇耐打王系列一】经验分享)
- **原帖链接**: [Commented] 这个因子到底有没有混信号【传奇耐打王系列一】经验分享.md
- **时间**: 24天前

**提问/主帖背景 (FX25214)**:
今天我想和大家很严肃的讨论一个问题
混信号
其实这个话题一直都是大家避不开的问题，而且大家也非常热衷于讨论这个问题。
本人也在这里给出一点自己的拙见。

一、关于混信号本身的讨论
首先，世坤给出 atom 的标识，是非常鼓励大家在同一个数据集对因子进行构造的。这里我完全不反对。但有的顾问会说，非 atom 就是混信号，跨数据集就是混信号。这确实让我非常哑然失笑。接下来我们分两个点来讨论：

1、atom 就没有混信号吗？

这肯定是不成立的。我来举个例子：
ts_product(a, 122) + ts_delta(a, 22)
这个毫无疑问，放在哪里都是 atom 了。但一个幂次加一个差分，这究竟是一个什么玩意？可能我作为一个刚刚数学本科毕业的学生给不出一个直观的解释。在我的视角来看，这就是妥妥的混信号了。

相信大家也看出来了，刚刚我是通过量纲进行观察，我认为两个没有直接联系，或者说从数学的角度完全不在一个维度的东西直接相加是非常不具备解释性的。

Ok，那同量纲，atom，就一定不混信号吗？
我们来看这个争议最大的例子：

rank(a) + rank(b)，a和b来自同一个数据集

就以某些fnd数据集来举例，这类数据集中往往同时存在表示实值（如公司负债）的单字段和表示比率（如公司利率）的单字段。a 和 b 分别来自这两种不同类的数据。这个实值当然可以是一个非常大的量级，百亿都有可能，但比率大概率不过1。都进行 rank，都变成0-1之间，量纲确实统一了。但我想你应该感觉到了这个因子不值得信任的方方面面。因为我们实在不知道两个不能有直接关系的字段为什么可以依靠 rank 之后调整到一起。更严肃一点来说，第一个 rank，是具备某些风格偏好的，就比如大市值公司天然的大。而第二个，是市场偏好的，赚得多的公司天然的大。我们用这样的 rank 相加，做的很可能是一个 β，并不是我们想要找到的 α。

2、非 atom 就一定是混信号吗？

这肯定也不成立。请看这个简单的例子：

分析师预期公司资产/公司实际资产
这实在是一个太常见的比率字段了。前一个大概率来自 anl，后一个来自 fnd。
我们的因子构建思路，就是在这个分析师预期与实际值的差异上做文章。

这样的因子，千千万，信号一跑一个准，当然很多人做过了避免不了 pc 高。

可我从来没听人正儿八经的说这个是混信号。

这样的比率构造，百分之一百符合世坤小而美的期待。这是一个十分具有目的性和经济学含义的因子构造。和混信号完全不搭边。

但我们总不能期待在数据集分类时，anl 数据和 fnd 数据分到一起吧。

- 关于混信号好不好的讨论

在我的视角中，我不倡导混信号。但不证明，混信号就一定是不好的。

大家经常说，我们用ts操作符，要用有意义的时间窗口：5, 22, 66, 252这样的。但真正有意义的是什么呢？

这里我来问一个问题，或许大家能有启发。国庆节为什么放七天假？

试问7是一个在上述列表的数字吗？

每一个事件，从来就不会固定的按照日周月季度年来开始和结束。这个事件只会在他该发生的时候发生，该结束的时候结束。

所以我认为很生硬的去固定一个时间窗口来进行因子的挖掘时很不明智的行为。

当时我做 ai alpha 的时候，很奇怪的看到ai给了我类似82、112这样的数字，说实话我也一脸懵。结果我自己调节时间窗口发现，有时候ai一步到位，选了一个最好的时间窗口，就跟见鬼了一样。

只能说，市场的洞见，不会按照一板一眼的来，因子的挖掘，也永远不会一板一眼。

选取合适的时间窗口，你说是混信号当然没问题，但或许这是对样本内一个较好的解释。

Ok，那换个角度，rank + rank，真的不可取吗？

我只能说，os 会告诉你可不可取。上一次os的更新，让我意识到了混信号≠os爆炸
下面这个因子我明确告诉大家就是 rank + rank这样的形式的，而且我明确的告诉大家其中一个字段是 imb5_score


> [!NOTE] [图片 OCR 识别内容]
> Chr


但我们能看到这个23年的 os 更新，这个因子相当的爆炸。而且我通过这样的方式解决了 imb圆顶的问题。

其实我们直接看除去23年的样本内数据，还是一个圆顶的趋势，但23年，他抬头了。

混信号，也不见得就没有作为。

我这么说不是倡导大家也去 rank + rank，而是想跟大家传递一种观念，市场不会因为你有解释性就承认你这个因子，也不会因为你解释不了就不认可你，市场无所谓你怎么挖，他只管他自己的脾气。所以，混信号并没有实质性的好或者不好。唯一的缺陷，就是在你的因子失败的时候，你没办法跟自己说：好吧这是一个失败的策略。因为你连为什么失败都不知道。我们做有经济学含义的因子，是为了给自己的失败一个解释，这真的很无奈。

可是朋友们，经济学含义是怎么来的？

经济学含义就是我提出了一个东西，这个东西被市场认证了，然后我们才把他归结到经济学含义中。

换句话说，要是你的 rank + rank每次 os 都很炸，那就是你说的算，你的含义就是经济学含义，这本就是一个结果导向的东西啊。因此纠结于是不是混信号真的毫无意义。

因此，做你想做的因子，好好的思考到底怎么做一个好的因子，这比你花时间想到底有没有混信号有意义的多。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢牛牛分享   确实，不能简单的把跨数据集和混信号划等号

还是得从经济学含义出发进一步评估

=============================================================================


---

### 技术对话片段 195 (原帖: 这个因子到底有没有混信号？【传奇耐打王系列一】经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 这个因子到底有没有混信号【传奇耐打王系列一】经验分享_40734437350679.md
- **时间**: 25天前

**提问/主帖背景 (FX25214)**:
今天我想和大家很严肃的讨论一个问题
混信号
其实这个话题一直都是大家避不开的问题，而且大家也非常热衷于讨论这个问题。
本人也在这里给出一点自己的拙见。

一、关于混信号本身的讨论
首先，世坤给出 atom 的标识，是非常鼓励大家在同一个数据集对因子进行构造的。这里我完全不反对。但有的顾问会说，非 atom 就是混信号，跨数据集就是混信号。这确实让我非常哑然失笑。接下来我们分两个点来讨论：

1、atom 就没有混信号吗？

这肯定是不成立的。我来举个例子：
ts_product(a, 122) + ts_delta(a, 22)
这个毫无疑问，放在哪里都是 atom 了。但一个幂次加一个差分，这究竟是一个什么玩意？可能我作为一个刚刚数学本科毕业的学生给不出一个直观的解释。在我的视角来看，这就是妥妥的混信号了。

相信大家也看出来了，刚刚我是通过量纲进行观察，我认为两个没有直接联系，或者说从数学的角度完全不在一个维度的东西直接相加是非常不具备解释性的。

Ok，那同量纲，atom，就一定不混信号吗？
我们来看这个争议最大的例子：

rank(a) + rank(b)，a和b来自同一个数据集

就以某些fnd数据集来举例，这类数据集中往往同时存在表示实值（如公司负债）的单字段和表示比率（如公司利率）的单字段。a 和 b 分别来自这两种不同类的数据。这个实值当然可以是一个非常大的量级，百亿都有可能，但比率大概率不过1。都进行 rank，都变成0-1之间，量纲确实统一了。但我想你应该感觉到了这个因子不值得信任的方方面面。因为我们实在不知道两个不能有直接关系的字段为什么可以依靠 rank 之后调整到一起。更严肃一点来说，第一个 rank，是具备某些风格偏好的，就比如大市值公司天然的大。而第二个，是市场偏好的，赚得多的公司天然的大。我们用这样的 rank 相加，做的很可能是一个 β，并不是我们想要找到的 α。

2、非 atom 就一定是混信号吗？

这肯定也不成立。请看这个简单的例子：

分析师预期公司资产/公司实际资产
这实在是一个太常见的比率字段了。前一个大概率来自 anl，后一个来自 fnd。
我们的因子构建思路，就是在这个分析师预期与实际值的差异上做文章。

这样的因子，千千万，信号一跑一个准，当然很多人做过了避免不了 pc 高。

可我从来没听人正儿八经的说这个是混信号。

这样的比率构造，百分之一百符合世坤小而美的期待。这是一个十分具有目的性和经济学含义的因子构造。和混信号完全不搭边。

但我们总不能期待在数据集分类时，anl 数据和 fnd 数据分到一起吧。

- 关于混信号好不好的讨论

在我的视角中，我不倡导混信号。但不证明，混信号就一定是不好的。

大家经常说，我们用ts操作符，要用有意义的时间窗口：5, 22, 66, 252这样的。但真正有意义的是什么呢？

这里我来问一个问题，或许大家能有启发。国庆节为什么放七天假？

试问7是一个在上述列表的数字吗？

每一个事件，从来就不会固定的按照日周月季度年来开始和结束。这个事件只会在他该发生的时候发生，该结束的时候结束。

所以我认为很生硬的去固定一个时间窗口来进行因子的挖掘时很不明智的行为。

当时我做 ai alpha 的时候，很奇怪的看到ai给了我类似82、112这样的数字，说实话我也一脸懵。结果我自己调节时间窗口发现，有时候ai一步到位，选了一个最好的时间窗口，就跟见鬼了一样。

只能说，市场的洞见，不会按照一板一眼的来，因子的挖掘，也永远不会一板一眼。

选取合适的时间窗口，你说是混信号当然没问题，但或许这是对样本内一个较好的解释。

Ok，那换个角度，rank + rank，真的不可取吗？

我只能说，os 会告诉你可不可取。上一次os的更新，让我意识到了混信号≠os爆炸
下面这个因子我明确告诉大家就是 rank + rank这样的形式的，而且我明确的告诉大家其中一个字段是 imb5_score


> [!NOTE] [图片 OCR 识别内容]
> Chr


但我们能看到这个23年的 os 更新，这个因子相当的爆炸。而且我通过这样的方式解决了 imb圆顶的问题。

其实我们直接看除去23年的样本内数据，还是一个圆顶的趋势，但23年，他抬头了。

混信号，也不见得就没有作为。

我这么说不是倡导大家也去 rank + rank，而是想跟大家传递一种观念，市场不会因为你有解释性就承认你这个因子，也不会因为你解释不了就不认可你，市场无所谓你怎么挖，他只管他自己的脾气。所以，混信号并没有实质性的好或者不好。唯一的缺陷，就是在你的因子失败的时候，你没办法跟自己说：好吧这是一个失败的策略。因为你连为什么失败都不知道。我们做有经济学含义的因子，是为了给自己的失败一个解释，这真的很无奈。

可是朋友们，经济学含义是怎么来的？

经济学含义就是我提出了一个东西，这个东西被市场认证了，然后我们才把他归结到经济学含义中。

换句话说，要是你的 rank + rank每次 os 都很炸，那就是你说的算，你的含义就是经济学含义，这本就是一个结果导向的东西啊。因此纠结于是不是混信号真的毫无意义。

因此，做你想做的因子，好好的思考到底怎么做一个好的因子，这比你花时间想到底有没有混信号有意义的多。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢牛牛分享   确实，不能简单的把跨数据集和混信号划等号

还是得从经济学含义出发进一步评估

=============================================================================


---

### 技术对话片段 196 (原帖: 这个模版到底怎么做？【传奇耐打王系列三】论坛精选)
- **原帖链接**: [Commented] 这个模版到底怎么做【传奇耐打王系列三】论坛精选.md
- **时间**: 24天前

**提问/主帖背景 (FX25214)**:
传奇耐打王好像从未分享过有实际用途或者含金量的东西。今天，他来了。

我们对于因子的构建思路来一个认真且专注的讨论。

我们都知道因子由操作符+字段组成。

那这个上，我们就先来他讨论一下操作符。

假设输出都是x。

就以捕捉x的波动性来举例：说到波动性我们的第一反应肯定是

- ts_std_dev 标准差可以反应一个对象的波动性
- 那标准差刻画的是什么？是不是x与ts_mean(x, d1)的偏离程度？

那我们不要算标准差这么复杂嘛，我们弄得简单一点：

x - ts_mean(x, d1)

x / ts_mean(x, d1)

- 那除了ts_mean(x, d1)能反映这个x这段时间的中心，还有什么可以反映？

ts_median(x, d1)，那刚刚的是不是可以再来一遍？

- 那既然中心考虑过了，那极值是不是也可以考虑一下？
  ts_max(x, d1), ts_min(x, d1)

5、这时候很多伙伴要跟我说了，但这些都已经有对应的操作符了呀，ts_av_diff, ts_min_diff

好的。那我来问一个问题？波动的波动有没有想过？

有没有可能在一段时间内，x持续的偏离ts_max(x, d1)且偏离的程度大差不差从而体现了平稳呢？

这当然是可能的！我们只需要做

ts_std_dev(ts_max_diff(x, d1), d2)，且d1 > d2。

如果这个值很小，表示短期的x持续的偏离长期的最大值，就体现了一个稳态。

这是多么有意思的事情！

6、可是朋友们，我们的思路绝对不能只局限于此啊。我是怎么思考波动性这个特征的呢？

简单思考一下，变化的快慢是不是可以体现波动性？

什么东西能反应变化的快慢？

我是数学专业，我的第一反应就是导数。

但我们没有求导这个操作符啊，那我怎么构造与求导类似的操作符组合呢？

我想到了差分。二阶差分就是最靠近导数的东西。

所以很简单的，我们构造出一个新的模版：

ts_delta(ts_delta(x, d1), d2)

- 那还能怎么思考呢？这里我再提供一个数学角度的思路。我们pnl曲线看多了总是喜欢平滑连续的东西。但我们实际拿到的字段可以是跳跃的、间断的。

那我们能通过这个跳跃和间断设计什么呢？我觉得可以做一个开关。

假设x的均线在a，x的最值在a+1000，那我是不是可以去捕捉x超出a + 500的时段或者说个数相对于总体的占比呢？

这个占比达到一个什么程度难道不也是一种波动的体现吗？
8、既然可以捕捉占比，那是不是也可以捕捉相邻两次突破设定的阈值间隔的时间呢？

关于波动性，我已经提供了8个思路，这还只是针对波动性捕捉的小小的一部分。只要你敢想，没什么做不出来的。当时我在研究小组调侃，我中午睡午觉想了一些模版。这8点中的一部分就是那个午觉带来的，经过测试，效果嘎嘎良好。

希望大家和我一起集思广益，这个因子的构造真的是无穷无尽的东西。

敬请期待下集，我分享关于字段构建中的巧思。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢牛牛分享！ 看见了红色的论坛精选tag就知道  牛牛出品 必属精品

这波对于操作符的组合打开了我的思路

=============================================================================


---

### 技术对话片段 197 (原帖: 这个模版到底怎么做？【传奇耐打王系列三】论坛精选)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 这个模版到底怎么做【传奇耐打王系列三】论坛精选_40735661471383.md
- **时间**: 25天前

**提问/主帖背景 (FX25214)**:
传奇耐打王好像从未分享过有实际用途或者含金量的东西。今天，他来了。

我们对于因子的构建思路来一个认真且专注的讨论。

我们都知道因子由操作符+字段组成。

那这个上，我们就先来他讨论一下操作符。

假设输出都是x。

就以捕捉x的波动性来举例：说到波动性我们的第一反应肯定是

- ts_std_dev 标准差可以反应一个对象的波动性
- 那标准差刻画的是什么？是不是x与ts_mean(x, d1)的偏离程度？

那我们不要算标准差这么复杂嘛，我们弄得简单一点：

x - ts_mean(x, d1)

x / ts_mean(x, d1)

- 那除了ts_mean(x, d1)能反映这个x这段时间的中心，还有什么可以反映？

ts_median(x, d1)，那刚刚的是不是可以再来一遍？

- 那既然中心考虑过了，那极值是不是也可以考虑一下？
  ts_max(x, d1), ts_min(x, d1)

5、这时候很多伙伴要跟我说了，但这些都已经有对应的操作符了呀，ts_av_diff, ts_min_diff

好的。那我来问一个问题？波动的波动有没有想过？

有没有可能在一段时间内，x持续的偏离ts_max(x, d1)且偏离的程度大差不差从而体现了平稳呢？

这当然是可能的！我们只需要做

ts_std_dev(ts_max_diff(x, d1), d2)，且d1 > d2。

如果这个值很小，表示短期的x持续的偏离长期的最大值，就体现了一个稳态。

这是多么有意思的事情！

6、可是朋友们，我们的思路绝对不能只局限于此啊。我是怎么思考波动性这个特征的呢？

简单思考一下，变化的快慢是不是可以体现波动性？

什么东西能反应变化的快慢？

我是数学专业，我的第一反应就是导数。

但我们没有求导这个操作符啊，那我怎么构造与求导类似的操作符组合呢？

我想到了差分。二阶差分就是最靠近导数的东西。

所以很简单的，我们构造出一个新的模版：

ts_delta(ts_delta(x, d1), d2)

- 那还能怎么思考呢？这里我再提供一个数学角度的思路。我们pnl曲线看多了总是喜欢平滑连续的东西。但我们实际拿到的字段可以是跳跃的、间断的。

那我们能通过这个跳跃和间断设计什么呢？我觉得可以做一个开关。

假设x的均线在a，x的最值在a+1000，那我是不是可以去捕捉x超出a + 500的时段或者说个数相对于总体的占比呢？

这个占比达到一个什么程度难道不也是一种波动的体现吗？
8、既然可以捕捉占比，那是不是也可以捕捉相邻两次突破设定的阈值间隔的时间呢？

关于波动性，我已经提供了8个思路，这还只是针对波动性捕捉的小小的一部分。只要你敢想，没什么做不出来的。当时我在研究小组调侃，我中午睡午觉想了一些模版。这8点中的一部分就是那个午觉带来的，经过测试，效果嘎嘎良好。

希望大家和我一起集思广益，这个因子的构造真的是无穷无尽的东西。

敬请期待下集，我分享关于字段构建中的巧思。

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区====================================

感谢牛牛分享！ 看见了红色的论坛精选tag就知道  牛牛出品 必属精品

这波对于操作符的组合打开了我的思路

=============================================================================


---

### 技术对话片段 198 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 适合邮箱自动推送的平台信息经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (WL27618)**:
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

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬的weight真的是令人羡慕哈哈

做了半年 weight还一直是0   有点难受

===================================================================================


---

### 技术对话片段 199 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 适合邮箱自动推送的平台信息经验分享_38472629440407.md
- **时间**: 3个月前

**提问/主帖背景 (WL27618)**:
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

**顾问 RM49262 (Rank 30) 的解答与建议**:
=====================================评论区=========================================

大佬的weight真的是令人羡慕哈哈

做了半年 weight还一直是0   有点难受

===================================================================================


---
