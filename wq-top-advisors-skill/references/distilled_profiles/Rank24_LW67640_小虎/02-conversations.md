# 顾问 LW67640 (小虎) (Rank 24) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 LW67640 (小虎) (Rank 24) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
英雄不问出处。很多时候，学历/知识背景可能就是一种借口，阻碍自己向上的借口。

听了分享，收获良多，感谢分享。

这篇帖子值得经常回来看看，给自己鼓励加油。

----------------------------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海。

----------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 2 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
英雄不问出处。很多时候，学历/知识背景可能就是一种借口，阻碍自己向上的借口。

听了分享，收获良多，感谢分享。

这篇帖子值得经常回来看看，给自己鼓励加油。

----------------------------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海。

----------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 3 (原帖: 6.29 value factor更新！)
- **原帖链接**: [Commented] 629 value factor更新.md
- **时间**: 1年前

**提问/主帖背景 (XX42289)**:
下面是CN地区进步最大的10位顾问

排名
顾问ID
Old Value Factor
New Value Factor
进步值

🥇1
YL21428
0.0500
0.9800
+0.9300

🥈2
WY63791
0.2000
0.9200
+0.7200

🥉3
XZ38372
0.0900
0.7500
+0.6600

4
顾问 NW19619 (Rank 56)
0.2600
0.9100
+0.6500

5
PZ64174
0.1800
0.8200
+0.6400

6
PM90725
0.1100
0.7000
+0.5900

7
GR20154
0.2800
0.8400
+0.5600

8
CO95231
0.0800
0.5900
+0.5100

9
HZ76661
0.2300
0.7400
+0.5100

10
ZD27134
0.1900
0.6700
+0.4800


> [!NOTE] [图片 OCR 识别内容]
> 顾问价值因子进步表彰
> 中国区进步最大的10位顾问
> 数据对比周期: 2025-1
> 2025-3 To 2025-2~ 2025-4
> 排名
> 顾问I
> Old Value Factor
> New Value Factor
> 进步值
> YL21428
> 0.0500
> 0.9800
> +0.9300
> WY63791
> 0.2000
> 0.9200
> +0.7200
> XZ38372
> 0.0900
> 0.7500
> +0.6600
> 顾问 NW19619 (Rank 56)
> 0.2600
> 0.9100
> +0.6500
> 5
> PZ64174
> 0.1800
> 0.8200
> +0.6400
> PM90725
> 0.1100
> 0.7000
> +0.5900
> GR20154
> 0.2800
> 0.8400
> +0.5600
> C095231
> 0.0800
> 0.5900
> +0.5100
> HZ76661
> 0.2300
> 0.7400
> +0.5100
> 10
> Z027134
> 0.1900
> 0.6700
> +0.4800


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
给这些有进步的顾问们点赞，做得漂亮，再接再厉！期待你们的分享！

给课代表点赞！

---------------------------------------------------------------------

vf一路下滑，不能再依赖运气了！

---------------------------------------------------------------------


---

### 技术对话片段 4 (原帖: 6.29 value factor更新！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 629 value factor更新_33126777986199.md
- **时间**: 1年前

**提问/主帖背景 (XX42289)**:
下面是CN地区进步最大的10位顾问

排名
顾问ID
Old Value Factor
New Value Factor
进步值

🥇1
YL21428
0.0500
0.9800
+0.9300

🥈2
WY63791
0.2000
0.9200
+0.7200

🥉3
XZ38372
0.0900
0.7500
+0.6600

4
顾问 NW19619 (Rank 56)
0.2600
0.9100
+0.6500

5
PZ64174
0.1800
0.8200
+0.6400

6
PM90725
0.1100
0.7000
+0.5900

7
GR20154
0.2800
0.8400
+0.5600

8
CO95231
0.0800
0.5900
+0.5100

9
HZ76661
0.2300
0.7400
+0.5100

10
ZD27134
0.1900
0.6700
+0.4800


> [!NOTE] [图片 OCR 识别内容]
> 顾问价值因子进步表彰
> 中国区进步最大的10位顾问
> 数据对比周期: 2025-1
> 2025-3 To 2025-2~ 2025-4
> 排名
> 顾问I
> Old Value Factor
> New Value Factor
> 进步值
> YL21428
> 0.0500
> 0.9800
> +0.9300
> WY63791
> 0.2000
> 0.9200
> +0.7200
> XZ38372
> 0.0900
> 0.7500
> +0.6600
> 顾问 NW19619 (Rank 56)
> 0.2600
> 0.9100
> +0.6500
> 5
> PZ64174
> 0.1800
> 0.8200
> +0.6400
> PM90725
> 0.1100
> 0.7000
> +0.5900
> GR20154
> 0.2800
> 0.8400
> +0.5600
> C095231
> 0.0800
> 0.5900
> +0.5100
> HZ76661
> 0.2300
> 0.7400
> +0.5100
> 10
> Z027134
> 0.1900
> 0.6700
> +0.4800


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
给这些有进步的顾问们点赞，做得漂亮，再接再厉！期待你们的分享！

给课代表点赞！

---------------------------------------------------------------------

vf一路下滑，不能再依赖运气了！

---------------------------------------------------------------------


---

### 技术对话片段 5 (原帖: A freshman's reflections on PPAC Competition & Key Learnings)
- **原帖链接**: [Commented] A freshmans reflections on PPAC Competition  Key Learnings.md
- **时间**: 1年前

**提问/主帖背景 (LG87838)**:
Dear WorldQuant and Forum Community,

I’m thrilled to share that I recently secured  **17th place**  in the PPAC competition—an incredibly rewarding experience that deepened my understanding of quantitative research. Beyond the ranking, the true value came from the lessons learned, which I’d love to reflect on here.

First, the competition reinforced the power of  **diversity** —not just in data sources or features, but in methodological approaches. Experimenting with different perspectives often led to unexpected insights, proving that a rigid framework can limit potential.

Second, I gained a newfound appreciation for  **ensemble techniques**  and how strategic combinations of models (even simple ones) can outperform overly complex solutions. This ties into my third takeaway:  **“less is more.”**  Sometimes, pruning redundant features or simplifying assumptions improved robustness far more than adding complexity did.

Most of all, I’m grateful for this platform. WorldQuant’s initiatives like PPAC are invaluable for fostering growth in our field, and the forum’s collaborative spirit—where seasoned quants and newcomers openly share ideas—made the journey even more enriching.

To future participants: Embrace the iterative process. Progress often hides in small, persistent refinements rather than radical overhauls.

A sincere thank you to everyone involved! I’d be happy to discuss specifics or hear others’ experiences.

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
Congratulations on your outstanding achievement in the PPAC competition! Your insights are truly valuable. I completely agree with you that diversity in methodology and the power of ensemble techniques are key factors in quantitative research. It’s fascinating how simplicity can sometimes yield better results than complexity. The collaborative environment of the forum is indeed a great asset for learning and growth.

Your experience has inspired me a lot, and I will definitely keep your advice in mind. Looking forward to more discussions with you!


---

### 技术对话片段 6 (原帖: A freshman's reflections on PPAC Competition & Key Learnings)
- **原帖链接**: https://support.worldquantbrain.com[Commented] A freshmans reflections on PPAC Competition  Key Learnings_32186337696791.md
- **时间**: 1年前

**提问/主帖背景 (LG87838)**:
Dear WorldQuant and Forum Community,

I’m thrilled to share that I recently secured  **17th place**  in the PPAC competition—an incredibly rewarding experience that deepened my understanding of quantitative research. Beyond the ranking, the true value came from the lessons learned, which I’d love to reflect on here.

First, the competition reinforced the power of  **diversity** —not just in data sources or features, but in methodological approaches. Experimenting with different perspectives often led to unexpected insights, proving that a rigid framework can limit potential.

Second, I gained a newfound appreciation for  **ensemble techniques**  and how strategic combinations of models (even simple ones) can outperform overly complex solutions. This ties into my third takeaway:  **“less is more.”**  Sometimes, pruning redundant features or simplifying assumptions improved robustness far more than adding complexity did.

Most of all, I’m grateful for this platform. WorldQuant’s initiatives like PPAC are invaluable for fostering growth in our field, and the forum’s collaborative spirit—where seasoned quants and newcomers openly share ideas—made the journey even more enriching.

To future participants: Embrace the iterative process. Progress often hides in small, persistent refinements rather than radical overhauls.

A sincere thank you to everyone involved! I’d be happy to discuss specifics or hear others’ experiences.

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
Congratulations on your outstanding achievement in the PPAC competition! Your insights are truly valuable. I completely agree with you that diversity in methodology and the power of ensemble techniques are key factors in quantitative research. It’s fascinating how simplicity can sometimes yield better results than complexity. The collaborative environment of the forum is indeed a great asset for learning and growth.

Your experience has inspired me a lot, and I will definitely keep your advice in mind. Looking forward to more discussions with you!


---

### 技术对话片段 7 (原帖: Combined alpha performance and combined selected alpha performance)
- **原帖链接**: [Commented] Combined alpha performance and combined selected alpha performance.md
- **时间**: 1年前

**提问/主帖背景 (AS77213)**:
- How can i increase my combined alpha performance and  combined selected alpha performance?
- By using which operator we can increase both?
- By using which data set we can increase both?
- How to keep both above 1?

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
As mentioned in  [How-can-you-earn-more-Base-payment?](/hc/en-us/articles/4672184130455-How-can-you-earn-more-Base-payment)

these two combined critical depend on your regular submitted alphas, take more attention on daily submitted is a good way to increase your combined indicators. for me, I add some check process before summiting according on the link, like rank or sign alpha to check stability...

and 2nd way is try to submit SuperAlpha, super alpha combine more regular alphas, its' OS performance will has stronger risk - resistance ability than a single regular alpha.


---

### 技术对话片段 8 (原帖: Combined alpha performance and combined selected alpha performance)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Combined alpha performance and combined selected alpha performance_32658322195095.md
- **时间**: 1年前

**提问/主帖背景 (AS77213)**:
- How can i increase my combined alpha performance and  combined selected alpha performance?
- By using which operator we can increase both?
- By using which data set we can increase both?
- How to keep both above 1?

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
As mentioned in  [How-can-you-earn-more-Base-payment?](/hc/en-us/articles/4672184130455-How-can-you-earn-more-Base-payment)

these two combined critical depend on your regular submitted alphas, take more attention on daily submitted is a good way to increase your combined indicators. for me, I add some check process before summiting according on the link, like rank or sign alpha to check stability...

and 2nd way is try to submit SuperAlpha, super alpha combine more regular alphas, its' OS performance will has stronger risk - resistance ability than a single regular alpha.


---

### 技术对话片段 9 (原帖: CONCENTRATED WEIGHT 系统性排查与修复手册-1（基于实战经验的 CW 攻防全指南）)
- **原帖链接**: https://support.worldquantbrain.com[Commented] CONCENTRATED WEIGHT 系统性排查与修复手册-1基于实战经验的 CW 攻防全指南_40972941718807.md
- **时间**: 20天前

**提问/主帖背景 (LC97552)**:
## **开头需要吸引人，以下是我最近一周的提交情况，本次分享的经验也是基于成功提交的过程中提取：**

**
> [!NOTE] [图片 OCR 识别内容]
> Regular
> ACTIVE
> Fast Expression
> 06/01/2026 EDT 
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 06/01/2026 EDT 
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 06/01/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 06/01/2026 EDT
> KOR
> TOPGOO
> Regular
> ACTIVE
> Fast Expression 
> 05/31/2026 EDT 
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/31/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/31/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/31/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/30/2026 EDT 
> KOR
> TOPGOO
> Regular
> ACTIVE
> Fast Expression 
> 05/30/2026 EDT 
> KOR
> TOPGOO
> Regular
> ACTIVE
> Fast Expression 
> 05/30/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/30/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/29/2026 EDT 
> HKG
> TOP8OO
> Regular
> ACTIVE
> Fast Expression 
> 05/29/2026 EDT
> MEA
> TOP300
> Regular
> ACTIVE
> Fast Expression 
> 05/29/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/29/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/28/2026 EDT 
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/28/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/28/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/28/2026 EDT 
> EUR
> TOP2500
  
> [!NOTE] [图片 OCR 识别内容]
> Regular
> ACTIVE
> Fast Expression
> 05/28/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/28/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/27/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/27/2026 EDT
> HKG
> TOP8OO
> Regular
> ACTIVE
> Fast Expression 
> 05/27/2026 EDT
> HKG
> TOP8OO
> Regular
> ACTIVE
> Fast Expression 
> 05/27/2026 EDT
> HKG
> TOP8OO
> Regular
> ACTIVE
> Fast Expression 
> 05/26/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/26/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/26/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/26/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/25/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/25/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/25/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/25/2026 EDT
> CHN
> TOPZOOOU
> Regular
> ACTIVE
> Fast Expression 
> 05/24/2026 EDT
> EUR
> TOP2500
> Regular
> ACTIVE
> Fast Expression 
> 05/24/2026 EDT
> IND
> TOP5OO
> Regular
> ACTIVE
> Fast Expression 
> 05/24/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/24/2026 EDT
> CHN
> TOPZOOOU
> Regular
> ACTIVE
> Fast Expression 
> 05/23/2026 EDT
> MEA
> TOP400
> Regular
> ACTIVE
> Fast Expression 
> 05/23/2026 EDT
> EUR
> TOP2500
**

> ## **我是** LC97552，以下是我优化过程中的经验，仅代表特定情况，所有方案仅供参考

## 

## **一、CW的本质？**

CW FAIL（权重过度集中）是 BRAIN 平台最常见的 IS 检查失败，也是最容易被误诊的。

权重集中（Weight Concentration）指少数极端信号主导投资组合权重，BRAIN平台限制为总账面规模的10%。常见触发原因：

• 覆盖范围不足：多头/空头股票<10只，或总股票<20只；

• 数据缺失：NaN导致权重被迫集中在少数有数据的股票；

• 分布异常：信号偏态、存在极端异常值；

• 中性化错配：市场中性化强制产生大额对冲头寸，表现为集中。

大多数人遇到 CW 的第一反应是：调 truncation → 加 neutralization → 换算子 → 换窗口…一轮下来 30 个变体，CW 纹丝不动。

> *真相是：90% 的 CW 失败不是参数问题。CW 是平台最诚实的检查项——它直接暴露信号底层结构的数据品质问题。*

## 

## **二、诊断：CW 的四种根因**

### **类型一：覆盖率不足——"数据都没有，你怎么不集中？"**

案例：MEA / TOP400，使用 model242 数据集。


> [!NOTE] [图片 OCR 识别内容]
> 窗0
> Truncation
> Neutralization
> 变体数
> CW 结果
> 各种尝试
> 各种取值
> 各种方式
> ~90
> 全部 WARNING


直到第 90 个变体才发现：该数据集在 MEA/TOP400 的覆盖率只有 27%。400 只股票里只有 109 只有数据。不到三分之一的股票有信号，剩下 70% 只能在少数有数据的股票上集中持仓。

> 解决方案：换数据集。同样的公式换到 fundamental72（覆盖率 54.5%），15 个变体就实现 CW PASS，持仓从几十只分散到 311 只。


> [!NOTE] [图片 OCR 识别内容]
> 数据集
> 覆盖宰
> CW 结果
> 斫需变体
> model242
> 27% (109/400)
> 全部 WARNING
> ~90
> fundamental72
> 54.5% (218/400)
> PASS
> 15
> PV
> (Close
> 100%
> PASS
> (基线)


```
覆盖率 < 40% → 立即换数据集。这是 ROI 最高的 CW 决策。
```

### **类型二：窗口长度——"差 2 天，CW 天差地别"**

*案例：EUR / TOP2500，mdl144_model_score × rp_ess_business 乘积结构。*

*
> [!NOTE] [图片 OCR 识别内容]
> mdl144 窗0
> Sharpe
> CW 结果
> 15天
> 2.12
> WARNING
> 20天
> 1.94
> WARNING
> 22天
> 1.53
> WARNING
> 24天
> 1.56
> PASS
> 25天
> 1.55
> PASS
*

CW 的阈值恰好卡在 22~24 天之间。但拉长窗口有代价——Sharpe 从 2.12 降到 1.56。

在这个案例中，尝试过的失败修复包括：truncation 、neutralization 、ts_zscore 标准化。

> *truncation 修的是截面极端值，CW 反映的是时间序列平滑度——两个完全不相关的维度。Window 才是 CW 的主因。*

### **类型三：事件型字段——"数据是季度更新的，CW 永远过不了"**

案例：IND / TOP500，EARNINGS 数据集。覆盖率 > 80%，但 50+ 变体全部 CW FAIL。


> [!NOTE] [图片 OCR 识别内容]
> 尝试方向
> 娈体数
> CW 结果
> ts_delta
> aV_diff
> ts_mean
> 20+
> 全部 FAIL
> -core 各种窗口
> 15+
> 全部 FAIL
> (66/120/252)
> truncation
> neutralization 徵调
> 15+
> 全部 FAIL


根本原因：EARNINGS 是事件型数据——财报每季度才一条，大部分时间没有新数据。CW 瓶颈不在截面分布，在时间稀疏性。

> *事件型字段的 CW 瓶颈不在截面分布，而在时间稀疏。算子修复在同 Category 内无效。*

解决方案：停止同 Category 修复，跨到 PV 端做 rank 加法组合：

> *add(rank(event_field), rank(ts_rank(close, 90))) → CW 从 FAIL 变 PASS，同时恢复 IS_LADDER。*

反面案例也有：

- IND 同一市场，ANALYST 数据集的 eps_y1 字段 userCount=0（从没有人用过），提交后 CW 直接 PASS。

*蓝海字段（userCount=0）是 CW 的免费通行证。天然零竞争 = 权重自动分散。*

- 同样在 MEA/FUNDAMENTAL 中，fnd72 作为 VECTOR 类型数据，90+ 变体全部 CW FAIL。但使用 vec_avg 转标量 + ts_backfill(66) 填缺口后，CW 从 WARNING → PASS。

### **类型四：vwap/cap 的结构性 CW**

案例：EUR / TOP2500，vwap/cap × institutional 组合。


> [!NOTE] [图片 OCR 识别内容]
> PV 端价格字段
> CW 结果
> Sharpe
> WaR
> Cap
> WARNING
> 2.37
> VolUme
> Cap
> PASS
> 2.27
> Volumelcap 窗0
> CW
> SUB Sharpe
> I5S Ladder
> 40天
> PASS
> 1.23
> 1.50
> 66 天
> PASS
> 1.31
> 1.56
> 72天
> PASS
> 1.38
> 1.62
> 90天
> PASS
> 1.35
> 1.58


> *72 天窗口 = SUB + Ladder 双优的 sweet spot。INDUSTRY 中性化是此组合的 CW 平衡点。*

## **三、CW 修复工具评测**

### **1、ts_backfill —— 可用，但是双刃剑**

*案例：* EUR / OTHER 的 dividend + PV + MODEL om_pct 组合。


> [!NOTE] [图片 OCR 识别内容]
> MODEL 端处理
> CW
> IS Ladder
> 无 backfill
> X FAIL
> 2.06
> backfill(2)
> PASS
> 2.06
> backfill(l)
> X FAIL
> 2.04


> *backfill(2) 是此结构的 CW 最小可行修复——更小窗口 CW 仍 FAIL，更大窗口 ISL 开始下降。*

### *2、*  **跨 Category rank 加法 —— 事件型 CW 的终极解**

事件型数据在同 Category 内有明确的 CW 修复失败证明（50+ 变体）。唯一的出路是跨 Category 组合——用 PV/volume 等高频数据补充低频事件信号的时间维密度。

## **四、CW 排查决策流程**

- 遇到 CW FAIL → 【第一步】查数据集覆盖率 %
- 覆盖率 < 40%？→ 结构性 CW，直接换数据集
- 覆盖率 ≥ 40%？→ 【第二步】查数据类型
- VECTOR 类型？→ vec_avg 转标量 + ts_backfill
- 事件型（EARNINGS/consensus）？→ 跨 Category rank 加法
- 时序型（PV/ANALYST price target）？→ 【第三步】查窗口长度
- 拉长信号窗口 2-5 天 → CW 转为 PASS？
- 仍 FAIL？→ 尝试 ts_backfill 最小窗口（从 1-5 天开始试）

## **五、给AI的金句**

*① CW 是数据品质问题，不是参数问题。truncation / decay / neutralization 修不了 CW。*

*② 覆盖率 < 40% 立刻换数据集。别在算子上浪费变体——这是最高 ROI 的决策。*

*③ 事件型字段的 CW 只能靠跨 Category 组合。同 Category 内的算子修复有明确的失败证明。*

## 六、总结

祝大家天天4+1！有更好的解决方案可以一起讨论~

## 附件一、论坛中所有关于CW的解决方案的汇总（可喂AI）

### 1. 缺失数据与覆盖范围（根本原因）

当大量股票因NaN获得零权重时，剩余股票被迫承担全部权重。

• ts_backfill(x, d)：时间序列回填，推荐 d=2~40（基本面数据可用60）

• group_backfill：按组均值回填，处理组内缺失模式差异

• group_extra：组均值填充，配合微小噪声可解决初期数据不足

• group_count(is_nan(a), market) > N ? a : nan：检测并剔除因缺失数据导致覆盖范围骤降的时期（N可试40/100/150）

### 2. 信号分布控制

改变数据分布形态，将极端值压缩，使权重分配更均匀。

• rank() / ts_rank(alpha, 20) / group_rank()：最常用，将分布转为均匀分布，同时有助于通过排名测试

• zscore()：标准化，但对偏态敏感，建议配合 tighter truncation（0.01~0.05）

• scale()：范围规范化

• truncate(x, maxPercent=0.5)：直接限制可获极端值的股票比例

• left_tail(x, max) / right_tail(x, min)：截断尾部，消除异常值主导排名

• log()：处理右偏数据

### 3. 平滑与降噪

减少日间跳变和噪声导致的权重脉冲式集中。

• ts_decay_exp_window(x, d, factor)：指数加权平均，平滑噪声输入，生成慢速稳定信号

• exp_window：指数窗口，在group_neutralize后使用可提升稳定性

• ts_weighted_delay(x, k)：混合今日与昨日值（k→1为原值，k→0为延迟），防止日间极端跳变

• days_from_last_change(x)：统计距上次变化天数，延长持仓、减少频繁调仓

• last_diff_value(x, d)：返回最近非零差分，抑制微小噪声导致的权重尖刺

• keep(x, f, period)：强制信号在period天内保持不变，避免每日反应式摆动

### 4. 中性化与分组处理

结构性集中往往源于中性化方式与alpha信号不匹配。

• 切换中性化层级：若alpha有强行业倾斜，市场中性化会强制大额对冲；改为sector/industry中性化可减少结构性失衡

### 5. 交易与持仓控制

• trade_when(x, y, z)：仅在条件触发时更新alpha，否则保持前值；显著降低换手率和权重波动

• 简化表达式：避免不必要嵌套，保持表达式简洁

### 6. 新兴市场特殊处理

新兴市场常见问题：①个别交易日数据不全；②回测初期（如2012年）大量股票无数据。前者可用常规回填解决；后者若group_count检测无效，可采用「微小噪声填充法」：

a = group_rank(ts_scale(mdl39_12_val_mo_sector_rank, 240), industry);
b = group_extra(a, 1, industry);
t = ts_mean(returns, 20);
add(b, 0.0001 * group_rank(-t, industry), filter = true)

原理：利用高覆盖度的group_rank(-returns)作为噪声项，通过add(filter=true)填补初期NaN，同时group_extra与industry neutralization均为组均值，可抵消噪声影响。

### 7. 注意事项

• 平台截断（Truncation）功能仅为防御性设计，用于样本外异常突刺保护，不保证样本内通过权重测试；

• rank函数同时是稳健性测试（排名测试）的一部分，含rank的alpha更易通过该测试；

• 若尝试上述所有方法后仍无法通过权重测试，建议更换alpha思路——某些想法可能天然无法以合规方式表达；

• 低覆盖范围（如20只）的alpha在样本外通常无法维持，与高覆盖期（500只）表现不可比；

• 避免在回填函数中使用过大lookback，否则可能引入前瞻性偏差或严重损害性能。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，思路清晰！

有个问题想请教：对于"类型三：事件型字段"的CW问题，你提到可以用 add(rank(event_field), rank(ts_rank(close, 90))) 跨Category组合。这种跨Category组合是否会影响alpha的原始信号逻辑？如果原始alpha的逻辑是捕捉财报公告后的价格反应，加上高频数据rank后，会不会反而稀释了原始信号的alpha？

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================


---

### 技术对话片段 10 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享.md
- **时间**: 5个月前

**提问/主帖背景 (PP26750)**:
最近cnhkmcp更新了个好东西Skills，有了它我们就可以将自己摸索出来的或者大佬分享的 **"方法论"全部告诉ai，再配合Gemini 3 pro这个最强大脑真的是当之无愧的好东西**

**不过现在Gemini cli默认无法使用skills，需要进行一些配置**

**关于cnhkmcp的更新这里就不再讲解了，更新完成后会多一个skills文件夹，你需要在你的项目文件夹下新建.gemini文件夹然后将cnhkmcp中的skills文件夹复制到.gemini文件夹中。**

**第一步需要在终端运行更新，让你的Gemini cli到最新的预览版**

```
npm install -g @google/gemini-cli@preview
```

更新完成后再输入

```
gemini --version
```


> [!NOTE] [图片 OCR 识别内容]
> PS 0: |量化 IAIKnowledgeBase> gemini
> C-Version
> 0.24.0-preview . 2


如图所示如果显示0.24.0-preview.2就表示成功了，我们再用gemini进入

在对话框中输入/settings进入设置模式


> [!NOTE] [图片 OCR 识别内容]
> Settings
> Bearch
> to
> filter
> Preview Features Ce.9.
> models)
> truex
> Enable preview features
> preview models)
> Vim Mode
> false
> Enable
> Vim keybindings
> Disable Auto Update
> false
> Disable
> automatic updates
> Apply
> To
> User
> Settings
> Workspace Settings
> System Settings
> (Use
> Enter to select,
> Tab to change focus
> Esc
> to close)
> Ce.9.


第一个 Preview Features (e.g., models)推荐打开，也就是右边显示为true*

然后再在上方的搜索框中输入skills，按回车将Agent Skills设置为true*如图所示


> [!NOTE] [图片 OCR 识别内容]
> Settings
> skill
> Agent Skills
> tPuex
> Enable Agent
> Skills Cexperimental)
> Apply
> To
> User Settings
> Workspace Settings
> System Settings
> (Use
> Enter
> to
> select
> Tab
> to change focus
> Esc
> to
> Close)


这时候我们退出再重新进入，在对话框中输入/skills列出所有的技能，如图所示就表示成功了，有一点需要注意你启动Gemini的目录中需要有~/.gemini/skills/ 
> [!NOTE] [图片 OCR 识别内容]
> /skills
> Available Agent
> Skills
> brain-Calculate-alpha-selfcorrQuick
> Calculates
> self-correlation
> and
> PPAC (Power Pool Alpha
> correlations
> checks
> PPAC
> brain-datafield-exploration-general
> Provides
> 6 proVen
> methods
> to
> eValuate
> new datasets
> 00
> t
> Use
> When
> the
> USer Wants
> to
> understand
> specific datafie
> brain-dataset-exploration-general
> Provides
> comprehensive Workflow for deep-diving
> into
> research
> Use
> When
> the
> user Wants
> to
> audit
> dataset"
> brain-explain-alphas
> Provides
> step-by-step Workflow for analyzing
> and explz
> operators
> Work together
> Includes
> steps
> for data
> field
> brain-how-to-pass-AlphaTest
> Provides
> detailed requirements
> thresholds
> and improver
> When the
> User asks
> about alpha submission
> failures
> how


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，太赞啦！

在xhs上搜索了好几天，没有结果。

问iflow, gemini，没有结果。

但在咱们的顾问论坛里找到了解决方法，再次感谢！

============================================================================

长风破浪会有时，直挂云帆济沧海

============================================================================


---

### 技术对话片段 11 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] Gemini cli如何使用cnhkmcp中的Skills经验分享_37661413598231.md
- **时间**: 5个月前

**提问/主帖背景 (PP26750)**:
最近cnhkmcp更新了个好东西Skills，有了它我们就可以将自己摸索出来的或者大佬分享的 **"方法论"全部告诉ai，再配合Gemini 3 pro这个最强大脑真的是当之无愧的好东西**

**不过现在Gemini cli默认无法使用skills，需要进行一些配置**

**关于cnhkmcp的更新这里就不再讲解了，更新完成后会多一个skills文件夹，你需要在你的项目文件夹下新建.gemini文件夹然后将cnhkmcp中的skills文件夹复制到.gemini文件夹中。**

**第一步需要在终端运行更新，让你的Gemini cli到最新的预览版**

```
npm install -g @google/gemini-cli@preview
```

更新完成后再输入

```
gemini --version
```


> [!NOTE] [图片 OCR 识别内容]
> PS 0: |量化 IAIKnowledgeBase> gemini
> C-Version
> 0.24.0-preview . 2


如图所示如果显示0.24.0-preview.2就表示成功了，我们再用gemini进入

在对话框中输入/settings进入设置模式


> [!NOTE] [图片 OCR 识别内容]
> Settings
> Bearch
> to
> filter
> Preview Features Ce.9.
> models)
> truex
> Enable preview features
> preview models)
> Vim Mode
> false
> Enable
> Vim keybindings
> Disable Auto Update
> false
> Disable
> automatic updates
> Apply
> To
> User
> Settings
> Workspace Settings
> System Settings
> (Use
> Enter to select,
> Tab to change focus
> Esc
> to close)
> Ce.9.


第一个 Preview Features (e.g., models)推荐打开，也就是右边显示为true*

然后再在上方的搜索框中输入skills，按回车将Agent Skills设置为true*如图所示


> [!NOTE] [图片 OCR 识别内容]
> Settings
> skill
> Agent Skills
> tPuex
> Enable Agent
> Skills Cexperimental)
> Apply
> To
> User Settings
> Workspace Settings
> System Settings
> (Use
> Enter
> to
> select
> Tab
> to change focus
> Esc
> to
> Close)


这时候我们退出再重新进入，在对话框中输入/skills列出所有的技能，如图所示就表示成功了，有一点需要注意你启动Gemini的目录中需要有~/.gemini/skills/ 
> [!NOTE] [图片 OCR 识别内容]
> /skills
> Available Agent
> Skills
> brain-Calculate-alpha-selfcorrQuick
> Calculates
> self-correlation
> and
> PPAC (Power Pool Alpha
> correlations
> checks
> PPAC
> brain-datafield-exploration-general
> Provides
> 6 proVen
> methods
> to
> eValuate
> new datasets
> 00
> t
> Use
> When
> the
> USer Wants
> to
> understand
> specific datafie
> brain-dataset-exploration-general
> Provides
> comprehensive Workflow for deep-diving
> into
> research
> Use
> When
> the
> user Wants
> to
> audit
> dataset"
> brain-explain-alphas
> Provides
> step-by-step Workflow for analyzing
> and explz
> operators
> Work together
> Includes
> steps
> for data
> field
> brain-how-to-pass-AlphaTest
> Provides
> detailed requirements
> thresholds
> and improver
> When the
> User asks
> about alpha submission
> failures
> how


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，太赞啦！

在xhs上搜索了好几天，没有结果。

问iflow, gemini，没有结果。

但在咱们的顾问论坛里找到了解决方法，再次感谢！

============================================================================

长风破浪会有时，直挂云帆济沧海

============================================================================


---

### 技术对话片段 12 (原帖: General Discussion-说任何你想说的话置顶的)
- **原帖链接**: [Commented] General Discussion-说任何你想说的话置顶的.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
说 **任何** 你想说的话

 **Criteria** 
 **Action** 
 **Points** 
 **Weightage** 

论坛活动
当前季度内对您在本季度发布的评论（评论长度不少于100字符）的点赞数

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

对您的Gunies评级中的社区活跃项有20%的权重影响

当前季度内对您在本季度发布的帖子（帖子长度不少于100字符）的点赞数

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

👆中文翻译，👇以英文为主

Forum Activity
Likes in the current quarter on a comment published in current quarter (min. length 100 chars)

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

20%

Likes in the current quarter on a post published in current quarter (min. length 100 chars)

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
谢谢Weijie老师, 还没有预约过1v1呢。

有这样一个可以和大家聊一聊量化的地方太好了。

=======================================================================

路慢慢其修远兮。。。

=======================================================================


---

### 技术对话片段 13 (原帖: General Discussion-说任何你想说的话置顶的)
- **原帖链接**: [Commented] General Discussion-说任何你想说的话置顶的.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
说 **任何** 你想说的话

 **Criteria** 
 **Action** 
 **Points** 
 **Weightage** 

论坛活动
当前季度内对您在本季度发布的评论（评论长度不少于100字符）的点赞数

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

对您的Gunies评级中的社区活跃项有20%的权重影响

当前季度内对您在本季度发布的帖子（帖子长度不少于100字符）的点赞数

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

👆中文翻译，👇以英文为主

Forum Activity
Likes in the current quarter on a comment published in current quarter (min. length 100 chars)

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

20%

Likes in the current quarter on a post published in current quarter (min. length 100 chars)

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
====================================================================================

感谢Weijie老师和其他国区老师的努力，终于有了一个适合新手发帖的地方。

新手多提问，大佬多回答，大家一起攒社区活动分。也希望我可以回答更多的帖子，来证明自己的成长。

====================================================================================


---

### 技术对话片段 14 (原帖: General Discussion-说任何你想说的话置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] General Discussion-说任何你想说的话置顶的_32984741297815.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
说 **任何** 你想说的话

 **Criteria** 
 **Action** 
 **Points** 
 **Weightage** 

论坛活动
当前季度内对您在本季度发布的评论（评论长度不少于100字符）的点赞数

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

对您的Gunies评级中的社区活跃项有20%的权重影响

当前季度内对您在本季度发布的帖子（帖子长度不少于100字符）的点赞数

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

👆中文翻译，👇以英文为主

Forum Activity
Likes in the current quarter on a comment published in current quarter (min. length 100 chars)

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

20%

Likes in the current quarter on a post published in current quarter (min. length 100 chars)

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
谢谢Weijie老师, 还没有预约过1v1呢。

有这样一个可以和大家聊一聊量化的地方太好了。

=======================================================================

路慢慢其修远兮。。。

=======================================================================


---

### 技术对话片段 15 (原帖: General Discussion-说任何你想说的话置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] General Discussion-说任何你想说的话置顶的_32984741297815.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
说 **任何** 你想说的话

 **Criteria** 
 **Action** 
 **Points** 
 **Weightage** 

论坛活动
当前季度内对您在本季度发布的评论（评论长度不少于100字符）的点赞数

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

对您的Gunies评级中的社区活跃项有20%的权重影响

当前季度内对您在本季度发布的帖子（帖子长度不少于100字符）的点赞数

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

👆中文翻译，👇以英文为主

Forum Activity
Likes in the current quarter on a comment published in current quarter (min. length 100 chars)

10 to 19 likes: 0.1

20 to 49 likes: 0.2

>50 likes: 0.5

20%

Likes in the current quarter on a post published in current quarter (min. length 100 chars)

10 to 19 likes: 1

20 to 49 likes: 2

>50 likes: 5

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
====================================================================================

感谢Weijie老师和其他国区老师的努力，终于有了一个适合新手发帖的地方。

新手多提问，大佬多回答，大家一起攒社区活动分。也希望我可以回答更多的帖子，来证明自己的成长。

====================================================================================


---

### 技术对话片段 16 (原帖: Harness engineering下的AI Quant经验分享)
- **原帖链接**: [Commented] Harness engineering下的AI Quant经验分享.md
- **时间**: 2个月前

**提问/主帖背景 (DZ31817)**:
这篇文章介绍一套我长期使用的人机协同工作流，以及我对这套流程的一些理解。

这套方法并不追求把量化研究完全交给 AI。我的做法更接近一种分工明确的协作框架：让 AI 参与它最擅长的环节，让代码承担稳定、重复、可验证的部分，让人保留目标设定、异常判断和最终提交权。

从来源上看，这套流程仍然建立在最传统的 1/2/3 阶框架之上，但过去一年多里不断吸收研究小组和论坛中的许多经验，把原先“简单提取字段再做扩展”的思路，逐步改造成了“由 AI 驱动”的结构。因此，它在今天依然保持着很强的生命力。

整套流程可以概括为三步：

1. 由 AI 生成结构简单、具有经济学含义的裸信号。
2. 从中筛出已有一定信号量的候选，再通过 1/2/3 阶和 robust 做增强。
3. 对符合提交条件的 alpha 做各类检测，补充经济学解释，最终由人决定是否提交。

在这三步中，AI 主要参与第一步和第三步中的解释辅助。中间的大部分流程，由硬编码脚本和人工调整的阈值共同完成。

这样的分工有一个直接好处：既能利用 AI 的创造力和高吞吐能力，又能尽量避免全 AI 工作流里常见的幻觉、偏航问题。入口端保持创新发散，中后段保持收敛，整套系统就能稳定运行。


> [!NOTE] [图片 OCR 识别内容]
> Harness 架构的三段式蓝图
> 阶段一:  信号生成
> 阶段二:  信号增强
> 阶段三:  检验提交
> Tier-1大模型发散生
> 机械化预处理。多通道剪
> 本地与平台指标检
> 成纯粹的经济学裸信
> 枝。1/2/3阶算子增强。
> 验。A1重新介入提
> 号。
> AI在此被绝对隔离。
> 供解释。人类执行
> 最终决策。
> 注意A1角色:  被高度隔离。仅负责提供创造力基石与逻辑解释。
> NotebookLN


———

## **## 一、AI 生成裸信号**

具体做法是：根据当前要做的塔，先确定对应的数据集，再从中选取一批数据字段，把字段名和字段描述发给 AI，要求它生成 50 到 100 个具有经济学含义的裸信号。这里我通常会强调三点：

1. 思路要尽量创新、发散。
2. 表达式要尽量简单、纯粹。
3. 可用的 op 只允许从我事先给定的基础 op 集合中选择。
4. 一定要有经济学含义，在输出表达式的同时也要输出经济学含义。

之所以强调“简单”，是因为这一步的目标还不是直接得到成熟 alpha，而是尽量生成一些结构清晰、逻辑直白、带有经济直觉的信号种子。后续的 1/2/3 阶和 robust，会承担大部分加工和增强工作。

AI 生成完成之后，我会对这批因子做两类预处理，这两步都由代码完成，AI 不参与：

1. #### 语法检查

使用论坛开源的语法解析器，检查字段是否存在、op 用法是否正确，先把明显无效的表达式清理掉。

1. #### vec 数据检查

对属性为 vector 的数据字段，自动补上 vec op。由于裸信号数量本来就不算多，这里我通常会把所有 vec op 都补上，因子数量虽然会增加，但总体仍在可控范围内。

处理完这些步骤之后，再对这批裸信号进行统一回测。

### ### 一些经验观察

在实际使用中，我有几条比较稳定的经验：

1. 模型越强，裸信号质量通常越高。实际效果上，tier 1 的模型，例如 GPT 和 Claude，通常明显优于更便宜的模型。
2. 更适合直接用 instant 模式，不开 thinking。我的实际观察是，一旦进入长链条思考，生成结果反而更容易变复杂，纯粹性会下降。
3. 输入给 AI 的信息不宜过多。只提供字段名和字段描述，效果往往最好；如果再加上覆盖度、用户量等额外信息，结果有时会变差。

后两条还没有非常明确的理论解释。我的猜测是，输入越复杂，模型越容易把注意力放到一些次要信息上，输出也更容易偏向“复杂但不纯”的表达式。


> [!NOTE] [图片 OCR 识别内容]
> 阶段一:  纯粹的A1引擎 (信号生成)
> 极简输入
> Tier 1 大模型
> 极简输入:  仅提供基础
> 输出
> 字段名 +字段描述。严
> 开启 Instant Mode
> 50-100个极简裸信号
> 禁输入复杂元数据。
> Thinwiiy "ode
> 髭
> 上下文复杂度
> 反直觉发现 "Anti-Thinking"
> 给予A1的上下文越少。 思考路径越短。生成的金融信号反而越纯粹。
> NotebookLM


———

## ## 二、信号增强

回测结束后，流程进入信号增强阶段。

### ### 2.1 阈值初筛

第一步是按一定阈值筛选裸信号，例如 Sharpe > 0.6、Fitness > 0.4 等。阈值并不是固定不变的，会根据当前塔、当前样本质量和候选数量做适当调整。

### ### 2.2 剔除无效因子

初筛之后，我会进一步剔除一些没有继续增强价值的无效因子，主要包括厂、横线因子等。这类因子不只是没法用，还会污染下一步相关性剪枝的计算。

常见的剔除方式包括：

1. 剔除 longCount + shortCount 过少的因子。
2. 剔除 PnL 最后若干个数值全为 0 的因子，这种情况基本可以直接视为厂。

### ### 2.3 多通道相关性剪枝

这是整个中段最重要的一步。

做法是：把通过初筛的因子，分别按 Sharpe、Fitness、Margin 等多个维度排序。每个维度都可以看作一个“通道”。在每个通道里，先把排第一的因子放进该通道候选池，后续因子只有在与当前池子的 max corr 小于阈值时，才会被保留，否则丢弃。最后将多个通道得到的候选池取并集，得到剪枝结果。这样做的目的，是尽量保留多样性，避免单一指标主导。

相关性阈值本身也不一定要固定。为了多保留一些高质量候选，我通常会采用逐步衰减的方式，例如：

- 前 5 个因子，阈值设为 0.85

- 第 5 到第 10 个因子，阈值设为 0.80

- 之后的阈值设为 0.75


> [!NOTE] [图片 OCR 识别内容]
> 阶段二:  多通道相关性剪枝 (保持物种多样性)
> Pruning Matrix
> Top 5 候选池
> 第5-10候选池
> 第10+候选池
> (Max Corr < 0.85)
> (Max Corr < 0.80)
> (Max Corr < 0.75)
> Sharpe 通道
> Fitness 通道
> Margin 通道
> raW
> signals
> 拒绝单-维度的粗暴过滤。多维降维与衰减式相关性阈值。有效防止因孑沦为高度同质化的近亲繁殛产物。
> NotebookLN


### ### 2.4 进入 1/2/3 阶或 robust

完成剪枝之后，就进入传统的增强流程。

最常见的路径是：

裸信号进入 1 阶，1 阶继续筛选后进入 2 阶，2 阶再进入 3 阶。每一阶之间，都会重复上述的步骤。

如果跑完 1 阶或 2 阶之后，就已经获得了相当数量的可提交因子，那流程通常就到此为止，不再继续向下扩展。

如果跑完之后，可提交因子仍然偏少，我会考虑补跑 robust，通过参数遍历做进一步增强。但这一步需要非常克制。robust 的初衷是检验因子，而不是增强因子。使用过度，容易走向过拟合。

———

## ## 三、检验和提交

### ### 3.1 先过本地相关性

如果候选是 ppa，直接本地跑自己 ppa 池子的相关性即可。

如果候选是 ra，通常会先跑自己 ra 池子的自相关，再继续跑平台 check。

### ### 3.2 借助数据库做一轮人工筛选

对所有待提交因子，我会先在自己的数据库里做一轮浏览和筛选。除了 Sharpe、Fitness 这些基本指标之外，我的数据库里还会显示其他辅助判断信息，例如：

- maxTrade 线是否接近原 PnL

- op 数

- df 数

一般会先按 Sharpe、Fitness、Margin 从高到低排序，再剔除 turnover 过高、op 过多、df 过多的因子，然后进行挑选。

这一层仍然保留较强的人工判断成分。

### ### 3.3 执行测试（一）

这一轮主要是网页端的人工复核，重点看以下几项：

1. 看 compare，对自己的组合有没有提升。对组合明显拖后腿的因子，通常不会进入提交。
2. 看基本指标，确认 TVR 和 return 是否正常，最大回撤是否过高。
3. 看分年度表格。如果 2022 年和 2023 年表现过低，通常也会比较谨慎。
4. 看 PnL 线、Sharpe 线、Turnover 线的形态是否顺眼。

这一层虽然带有一定主观性，但对剔除一些“表面过线、整体感觉不对”的结果很有帮助。

### ### 3.4 执行测试（二）

这一轮主要做可自动化的一键测试。

#### 第一部分是 rank/sign test：

对候选因子跑 rank(alpha) 和 sign(alpha)。如果这些变形版本的 Sharpe 低于原 alpha 的 50%，我一般不会提交。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 067
> 1.00
> 0.40
> 0.75
> 04
> 0.50
> 0.2
> 0.25
> 鼍
> 0.0
> 000
> -0.2
> -0.25
> -0.4
> org sharpe
> 1.00
> -0.50
> 50% orig = 0.50
> -0.6
> 054
> 0.59
> orig
> rank
> slgn
> sign_gn
> sign_gn
> none
> orig
> raTk
> sign
> sign_gn
> sign_gn_none
> Margin
> Turnover
> 10.07
> 24.52
> 745
> 25
> 4|1
> 20
> -20
> 14.62
> 15
> S
> 8
> 11.73
> -40
> 10
> 8.75
> G0
> 3.93
> 78.13
> orig
> rank
> slgn
> sign_gn
> sign_gn_
> none
> org
> rank
> slgn
> slgn_gn
> sign_gn_none
> Returns
> Drawdown
> 301
> 211.27
> 200
> 3.00
> 175
> 150
> 125
> 8
> 100


#### 
> [!NOTE] [图片 OCR 识别内容]
> 181
> RS Test Pnl Compare: QPjgNLqp
> orig
> QPjBNLqP
> OrIg
> rank
> ZYIRLk2Q
> sign
> 58GZVNa1
> sign_gn
> pwzqganx
> 05
> sign_gn_none | mLzPkeqx
> 「
> SIgn_gn
> 日
> -0.5
> -1.0
> -1.5
> Slgn_gn
> none
> UuNw
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
> 2024
> Date


#### 第二部分是 robust test：

对原 alpha 跑 robust 测试。如果结果方差过大，也会比较谨慎。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> 最大值:  1.0900
> 均值: 0.3135
> 中位数:  0.2800
> 最小值:
> -0.3200
> 标准差:
> 0.2960
> 四分位距 (IQR):
> 0.4450
> 极差:  1.4100
> Fitness
> 最大值:  1.8400
> 均值: 0.2300
> 中位数:
> 0.1300
> 最小值: -0.2000
> 标准差:
> 0.3274
> 四分位距 (IQR):
> 0.2900
> 极差:  2.0400
> Margin
> 最大值:  134.2600
> 均值:  12.5754
> 中位数:
> 3.6900
> 最小值: -17.3000
> 标准差:  25.9616
> 四分位距
> (IQR) :
> 10.7450
> 极差:
> 151.5600
> Turnover
> 最大值:  40.9200
> 均值:  14.7835
> 中位数:  11.9300
> 最小值:  3.2800
> 标准差:  8.5542
> 四分位距 (IQR): 12.5750
> 极差:  37.6400
> Returns
> 最大值:  41.9000



> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 100
> 40
> 75
> 30
> 墨
> 20
> 詈
> 50
> 10
> 25
> 0
> 2
> 2
> 2
> 2
> Sharpe
> Fitness
> Margin
> TurnoVer
> 150
> 40
> 詈
> 100
> 詈
> 20
> 50
> -200
> -150
> -100
> -50
> 50
> 100
> 150
> 200
> 10
> 20
> 30
> 40
> 50
> 60
> 70
> Margin
> TurnoVer
> Returns
> Drawdown
> 100
> 75
> 40
> 詈
> 50
> 詈
> 20
> 25
> -40
> -20
> 20
> 40
> 20
> 40
> G0
> 80
> 100
> Returns
> Drawdown



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Decay
> Fitness by Decay
> 1.00
> 1.5
> 0.75
> 0.50
> 1.0
> 0.25
> 0.5
> 0.00
> 0.0
> -0.25
> 22
> GG
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Margin by Decay
> Turnover by Decay
> 40
> 125
> 100
> 30
> 75
> 50
> 20
> 25
> 圭
> 圭
> 10
> 22
> 66
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Returns by Decay
> Drawdown by Decay
> 40
> 125
> 30
> 100
> 20
> 75
> 10
> 50
> 25
> 22
> RG
> 120
> 240
> 512
> 22
> FG
> 120
> 240
> 512



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Universe
> Fitness by Universe
> 1.0
> 0.5
> 0.0
> 丰
> A
> A
> Universe
> Universe
> Margin by Universe
> Turnover by Universe
> 40
> 100
> 50
> 20
> Universe
> Universe
> Returns by Universe
> Drawdown by Universe
> 40
> 100
> 20
> 50
> 0
> 0
> TOPSOO
> TOP2O0
> TOP3000
> TOPSP5OO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1000
> MINVOLI
> MINVOL
> ILLIQUID
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOPSPSOO
> TOP1000
> MINVOLIM
> MINVOLTM
> '
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOP1OOO
> TOPSPSOO
> MINVOLIM
> TOPSPSOO
> MINVOLTN



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Neut
> Fitness by Neut
> 生
> 圭空臣孛l
> Neut
> Neut
> Margin by Neut
> Turnover by Neut
> 40
> 100
> 20
> 丢
> Neut
> Neut
> Returns by Neut
> Drawdown by Neut
> 25
> 100
> 垩 +
> 豆S星|臣
> 50
> 鹇 -工
> 丰茔茔
> 簋
> SLOW
> SECTOR
> 簋
> 磊
> 
> SECTOR
> 
> NONE
> FAST
> INDUSTRY
> 
> MONRKM
> CROWDING
> 鸶
> FAST
> 
> _MOMERKAM
> STATISTICAL
> STATISTICAL
> AND
> AND_
> SLOW_
> SLOW
> 昱
> AND_
> REVERSION
> REVERSION
> 簋
> SLOW
> NONE
> FAST
> INDUSTRY
> SUBINDUSTRY
> SECTOR
> 
> CROWDING
> 簋
> SLOW
> NONE
> n
> SUBINDUSTRY
> SECTOR
> _MOMERKBM
> CROWDING
> INDUSTRY
> STATISTICAL
> STATISTICAL
> 昱
> AND_
> SLOW
> SLOW
> AND_
> AND
> REVERSION
> REVERSION
> 簋
> SUBINDUSTRY
> FAST
> SUBINDUSTRY
> $
> NONE
> FAST
> INDUSTRY
> SECTOR
> MOMRKEM
> CROWDING
> SLOW
> NONE
> FAST
> INDUSTRY
> 暑
> _MOMERKAM
> CROWDING
> STATISTICAL
> STATISTICAL
> AND_
> AND_
> s
> SLOW_
> AND_
> AND_
> IERSION
> IRSION



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Group
> Fitness by Group
> 1.0
> 0.5
> 00
> 9
> "
> Group
> Group
> Margin by Group
> Turnover by Group
> 40
> 100
> 50
> 20
> y
> 聃貊
> 酾堕百
> 酝
> 苫 酶错
> Group
> Group
> Returns by Group
> Drawdown by Group
> 40
> 丐
> 100
> 20
> 亘
> 5
> q醒
> 50
> 5颐
> 牾-鸱



> [!NOTE] [图片 OCR 识别内容]
> 167
> PNL Curves by universe (colored by group max PNL)
> 1e7
> universe
> TOP200141898873.0000)
> C"」 '
> T0P3000(34151195.00OOJ
> TOPSP500 (33184197.0000)
> 1' |
> TOP500131186982.0000)
> ICY7 
> 4.00
> TOP1000 125998203.000OJ
> Lqiyc
> ILLOUID_NINVOLII (2136329400001
> 3.75
> 3.50
> 3.25
> _
> 300
> 2.75
> 250
> 2.25
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
> 2024



> [!NOTE] [图片 OCR 识别内容]
> 1e7
> PNL Curves by uni neut (colored by group max PNL )
> 1e7
> uni*neut
> TOP2OO NONE (41898873.0000)
> CeyAr
> 40
> T0P3000 NONE (34151196.00001
> T
> TOPSPSOO NONE 133184197.00OO)
> VSA
> TOP5OO NONE (311869820000)
> TOPIO0 NONE (259982030000)
> ILLIGUID_NINVOLIIINONE (21363294.00001
> 35
> TOPZOO SECTOR (13214659.0000)
> TOPZOOINDUSTRY (13052861.0000)
> TOP2OO MARKET (10940356.00001
> TOP3000 SUBINDUSTRY (1033918000001
> TOP3OOD*INDUSTRY (9251236.0000)
> 30
> TOP300 FAST (9050392.00001
> TOP200 REVERSION_AND_NONENTUI (8732002.0000j
> TOP3OOO SECTOR (8669384.0000)
> TOP30ODNARKET (7947224.0000)
> 25
> 
> TOP3OOOREVERSION_AND_MOMENTUM 17463611.0000)
> TOP200CROIDING (7316500.000O)
> TOP3OOOCROWDING (71144850000I
> 鱼
> TOPSPSOO FAST (6302806.00001
> _
> TOP3000 SLOI (6275460,000OI
> 20
> 盏
> TOPZOO*FAST (6193168.00001
> TOPSPSOO SECTOR (6187494,0000)
> TOP3000 SLOI
> AND_FAST (6159347.0000)
> 趸
> TOP3000STATISTICAL (5796010,0DOOI
> TOP5OD FAST (5775770.00001
> TOP5OD*SLOW (5654524,0000)
> 1.5
> 邕
> TOPSOOINDUSTRY (5461946.0000)
> TOPSPSOOINDUSTRY (5428550.0OOOI
> TOP5OOSLOW_AND_FAST (5389790.00OO)
> TOP200*SUBINDUSTRY (4519126.0000)
> TOPSP5OO M4RKET (4494552,000OI
> 1.0
> TOPSPSOO SLOI (44774460000)
> TOPSPSOOSLOI_AND_FAST (4446454,0000)
> TOPSOOCROWDING (4356666.0000)
> ILLOUID_NINVOLII FAST (4308647.000O)
> TOPSPSOO REVERSION_AND_NOMENTUN 14271460.0000]
> 05
> TOPSOO REVERSION_AND_NONENTUN14255880.0000)
> TOP5O0 SECTOR (421024-.0OOOI
> TOPSPSOO CROWDING (3929487.000O)
> TOP5O0 NIARKET (3624809.0OOO)
> ILLQUID_NINVOLIIINDUSTRY (31659490000)
> 00
> ILLIQUID_NINVOLIISLOW_AND_FAST (31279620000)
> O
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 2024
> TOPI0OOINDUSTRY (3089212000O
> ILLIQUID_NINVOLII SLOW (2823083 OOOOI
> Date
> TOP5OO*STATISTICAL (2540856,000O)


这一部分已经实现了自动化，只需要输入原 alpha 的 id，就可以一键完成。

### ### 3.5 执行测试（三）

这一步是 AI 第二次进入流程。

把该因子的表达式、数据字段含义发给 AI，让它输出以下内容：

1. 经济学解释
2. 因子值越大代表什么
3. 做多/做空因子值高/低的公司的合理性与潜在不合理处
4. 符合平台格式的因子描述，用于填写因子描述

对于经济学解释显著与常识不符的，我会慎重考虑。让AI提出正反两方面的观点，也可以防止从结果倒推原因。另外，认真填写描述似乎对weight有一定作用，可能可以增加自己因子被选中的机会。


> [!NOTE] [图片 OCR 识别内容]
> 二
> 经济学含义 (核心)
> 这个因子本质是在找:
> 在同一子行业内。同时具备高盈利能力 (ROA) 和高运营效率 (资产周转率)  的公司
> 因子值高的公司意味着什么?
> 当因子值高时,
> 公司通常具备:
> 1。资产赚钱能力强 (高ROA)
> 成本控制好 /定价能力强
> 或者资本结构合理
> 2。资产使用效率高 (高资产周转率)
> 存货周转快
> 业务模式轻资产 |高周转
> 3。经营质量高
> 不是"靠重资产堆利润'
> 而是"又赚得多;
> 又转得快"
> 典型特征:
> 消费品龙头 (高周转+稳定利润)
> 优质制造企业 (精益生产)
> 平台型轻资产公司



> [!NOTE] [图片 OCR 识别内容]
> 三
> 做多高因子股票的逻辑
> 合理性
> 1
> 质量因子 (Quality Factor)
> 高ROA = 好公司
> 高周转 =高效率
> 〉
> 双重筛选。避免"假盈利"
> 2。抗周期能力强
> 高效率公司更能应对需求波动
> 3。资本配置优
> 资产利用率高 >再投资回报更高
> 4
> 行业内比较更公平
> group_rank避免行业偏差 (例如银行 Vs 科技)
> 风险与不合理之处
> 1。可能错杀"重资产优质公司"
> 如公用事业
> 能源。半导体
> 天生周转率低 >被低估
> 2
> 周期顶部风险
> 在景气周期中:
> 收入暴涨 >周转率虚高
> 利润暴涨 > ROA虚高
> >因子容易在高点买入
> 3.
> ZSCore引l入极端值放大
> 异常高收入公司可能被过度放大权重
> 4。没有考虑增长性
> 高ROA + 高周转+高成长
> 可能是"成熟但不增长"的公司



> [!NOTE] [图片 OCR 识别内容]
> 四。做空低因子股票的逻辑
> 合理性
> 低ROA + 低周转:
> 〉
> 资产使用效率差 +盈利能力差
> 〉常见于:
> 僵尸企业
> 低效国企
> 管理层低效公司
> 风险
> 1
> 反转风险 (Turnaround)
> 低效公司一旦改革 >爆发性上涨
> 2
> 高投入早期公司
> 科技|创新企业:
> 当前ROA低。周转低
> 但末来潜力大
> 3.
> 行业周期底部
> 全行业ROA下降 >错误做空



> [!NOTE] [图片 OCR 识别内容]
> 五。整体评价
> 这个因子:
> 逻辑清晰 (杜邦框架)
> 行业内中性化 (很重要)
> 同时刻画"盈利 +效率"
> 但=
> 对周期敏感
> 偏好轻资产行业
> 缺乏增长维度
> 六。推荐评分
> 评分:  &110
> 适合作为:
> 核心质量因子之一
> 与成长因子 |估值因子结合使用
> 不建议单独使用的原因:
> 周期波动较大
> 行业风格偏向明显
> 七
> 英文总结
> Idea: Identify firms
> both high profitability and high asset efficiency within subindustries。
> Rationale for data used: Net income over total assets captures profitability (ROA), While revenue over
> total assets measures asset turnover; jointly reflecting operational and capital efficiency。
> Rationale for operators used: Ranking ROA emphasizes relative profitability; Z-scoring turnover highlights
> deviations in efficiency; and multiplication ensures only firms strong in both dimensions score highly; while
> group ranking neutralizes industry effects。
> with


### ### 3.6 提交

完成上述步骤之后，进入最终提交。

———

## ## 四、Harness engineering 下的 AI Quant

这套工作流我已经用了很久。回头看，它最核心的一点其实很简单：让 AI 做擅长的创新扩展的工作，让代码承担稳定、重复、明确的任务，让人保留高层决策和控制权。最近 harness engineering 这个概念开始流行起来，我觉得它非常适合概括这套方法。

如果打个比喻，这套流程更像一列火车。AI 驱动的裸信号生成，像是给火车换上了更强劲的引擎；而相关性约束、稳健性测试、RS 测试和分层筛选机制，则像轨道、道岔和信号系统。动力很强，方向也比较稳定。AI 先提出新的创意，后续流程再为这些创意补上轨道，因此轨道本身并不会提前封死创新。

相比之下，全 AI 工作流更像一辆高性能汽车。它有强劲动力，有自动驾驶，也有各种 skills 和提示词作为导航和路牌，但它仍然要在开放路网里持续做局部判断。一旦方向偏了，系统往往不会立刻停下，而是会沿着错误道路继续高速前进。动力越强，偏航之后冲出去的距离通常也越远，最后掉头的成本越高。


> [!NOTE] [图片 OCR 识别内容]
> 认知重构:  全A1工作流 VS. Harness Engineering
> 全A1工作流 /汽车模型
> Harness Engineering / 火车模型
> 特征:  极高的自主性;Al包揽生成。测试与纠错。
> 特征: A1提供前迸的动力 (引擎)
> 硬编码视则提供运行的轨道 (铁轨)
> 隐患:  在金酃嗓声中猴易[轨或陷入幻觉;方向不可控,容崭成本极高。
> 优势:  能量榄精准约束。铁轨本身不限制创造力,只设定致命哟边界。
> 真正的力量不在于A1的绝对自主。而在于对A1能量的精准约束。
> NotebookLM


———

## ## 五、与模板爆炸法的区别

AI打工人中现在用的一套方法，是先让 AI 提出一个因子表达式模板，再给出可以填入模板的数据集，然后围绕这个模板做大规模生成和回测。这种方法可以称为模板爆炸法。

研究者先假定某种表达式结构大体有效，再让模型或程序去填不同的数据字段。这样做的好处是效率高、可控性强，也适合围绕某一类已知有效结构做快速放大。但这个方法对于所使用的模板要求是比较高的。除了内置的几套验证过的有效模板，如果新手直接自己探索模板或者让AI未经验证给出一个模板，其实很难说效果会好。

而生成裸信号的方法更偏向发现式研究。通过这个方法发现和验证后的结果，也可以总结成模板，两者并不冲突。

———

## ## 六、AI 还能继续做的事

在当前版本里，AI 主要参与裸信号生成和最终的经济学解释。中间流程仍然以硬代码和人工软判断为主。但如果将现在中间段的操作日志、数据全量记录下来，然后交给AI去统计和发现其中的模式，AI 也会在这些位置上逐步加深参与。

———

## ## 结语

我对这套工作流的总体评价很简单：

它让 AI 做 AI 擅长的部分，让代码做代码擅长的部分，让人继续承担研究中最重要的判断工作。

在量化研究这种高噪声、高伪阳性、高竞争的场景里，有价值的通常不是盲目追求让 AI 覆盖更多步骤，而是能够约束并高效利用AI的能量。

这正是 Harness engineering 在 AI Quant 里的意义。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的分享，kitty哥是一个严谨思考的人，经常看到他的各种统计图。

使用AI的过程，感觉大起大落，缺少了约束，受益良多。

===========================================================

长风破浪会有时，直挂云帆济沧海。

===========================================================


---

### 技术对话片段 17 (原帖: Harness engineering下的AI Quant经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Harness engineering下的AI Quant经验分享_39304762113815.md
- **时间**: 2 months ago

**提问/主帖背景 (DZ31817)**:
这篇文章介绍一套我长期使用的人机协同工作流，以及我对这套流程的一些理解。

这套方法并不追求把量化研究完全交给 AI。我的做法更接近一种分工明确的协作框架：让 AI 参与它最擅长的环节，让代码承担稳定、重复、可验证的部分，让人保留目标设定、异常判断和最终提交权。

从来源上看，这套流程仍然建立在最传统的 1/2/3 阶框架之上，但过去一年多里不断吸收研究小组和论坛中的许多经验，把原先“简单提取字段再做扩展”的思路，逐步改造成了“由 AI 驱动”的结构。因此，它在今天依然保持着很强的生命力。

整套流程可以概括为三步：

1. 由 AI 生成结构简单、具有经济学含义的裸信号。
2. 从中筛出已有一定信号量的候选，再通过 1/2/3 阶和 robust 做增强。
3. 对符合提交条件的 alpha 做各类检测，补充经济学解释，最终由人决定是否提交。

在这三步中，AI 主要参与第一步和第三步中的解释辅助。中间的大部分流程，由硬编码脚本和人工调整的阈值共同完成。

这样的分工有一个直接好处：既能利用 AI 的创造力和高吞吐能力，又能尽量避免全 AI 工作流里常见的幻觉、偏航问题。入口端保持创新发散，中后段保持收敛，整套系统就能稳定运行。


> [!NOTE] [图片 OCR 识别内容]
> Harness 架构的三段式蓝图
> 阶段一:  信号生成
> 阶段二:  信号增强
> 阶段三:  检验提交
> Tier-1大模型发散生
> 机械化预处理。多通道剪
> 本地与平台指标检
> 成纯粹的经济学裸信
> 枝。1/2/3阶算子增强。
> 验。A1重新介入提
> 号。
> AI在此被绝对隔离。
> 供解释。人类执行
> 最终决策。
> 注意A1角色:  被高度隔离。仅负责提供创造力基石与逻辑解释。
> NotebookLN


———

## **## 一、AI 生成裸信号**

具体做法是：根据当前要做的塔，先确定对应的数据集，再从中选取一批数据字段，把字段名和字段描述发给 AI，要求它生成 50 到 100 个具有经济学含义的裸信号。这里我通常会强调三点：

1. 思路要尽量创新、发散。
2. 表达式要尽量简单、纯粹。
3. 可用的 op 只允许从我事先给定的基础 op 集合中选择。
4. 一定要有经济学含义，在输出表达式的同时也要输出经济学含义。

之所以强调“简单”，是因为这一步的目标还不是直接得到成熟 alpha，而是尽量生成一些结构清晰、逻辑直白、带有经济直觉的信号种子。后续的 1/2/3 阶和 robust，会承担大部分加工和增强工作。

AI 生成完成之后，我会对这批因子做两类预处理，这两步都由代码完成，AI 不参与：

1. #### 语法检查

使用论坛开源的语法解析器，检查字段是否存在、op 用法是否正确，先把明显无效的表达式清理掉。

1. #### vec 数据检查

对属性为 vector 的数据字段，自动补上 vec op。由于裸信号数量本来就不算多，这里我通常会把所有 vec op 都补上，因子数量虽然会增加，但总体仍在可控范围内。

处理完这些步骤之后，再对这批裸信号进行统一回测。

### ### 一些经验观察

在实际使用中，我有几条比较稳定的经验：

1. 模型越强，裸信号质量通常越高。实际效果上，tier 1 的模型，例如 GPT 和 Claude，通常明显优于更便宜的模型。
2. 更适合直接用 instant 模式，不开 thinking。我的实际观察是，一旦进入长链条思考，生成结果反而更容易变复杂，纯粹性会下降。
3. 输入给 AI 的信息不宜过多。只提供字段名和字段描述，效果往往最好；如果再加上覆盖度、用户量等额外信息，结果有时会变差。

后两条还没有非常明确的理论解释。我的猜测是，输入越复杂，模型越容易把注意力放到一些次要信息上，输出也更容易偏向“复杂但不纯”的表达式。


> [!NOTE] [图片 OCR 识别内容]
> 阶段一:  纯粹的A1引擎 (信号生成)
> 极简输入
> Tier 1 大模型
> 极简输入:  仅提供基础
> 输出
> 字段名 +字段描述。严
> 开启 Instant Mode
> 50-100个极简裸信号
> 禁输入复杂元数据。
> Thinwiiy "ode
> 髭
> 上下文复杂度
> 反直觉发现 "Anti-Thinking"
> 给予A1的上下文越少。 思考路径越短。生成的金融信号反而越纯粹。
> NotebookLM


———

## ## 二、信号增强

回测结束后，流程进入信号增强阶段。

### ### 2.1 阈值初筛

第一步是按一定阈值筛选裸信号，例如 Sharpe > 0.6、Fitness > 0.4 等。阈值并不是固定不变的，会根据当前塔、当前样本质量和候选数量做适当调整。

### ### 2.2 剔除无效因子

初筛之后，我会进一步剔除一些没有继续增强价值的无效因子，主要包括厂、横线因子等。这类因子不只是没法用，还会污染下一步相关性剪枝的计算。

常见的剔除方式包括：

1. 剔除 longCount + shortCount 过少的因子。
2. 剔除 PnL 最后若干个数值全为 0 的因子，这种情况基本可以直接视为厂。

### ### 2.3 多通道相关性剪枝

这是整个中段最重要的一步。

做法是：把通过初筛的因子，分别按 Sharpe、Fitness、Margin 等多个维度排序。每个维度都可以看作一个“通道”。在每个通道里，先把排第一的因子放进该通道候选池，后续因子只有在与当前池子的 max corr 小于阈值时，才会被保留，否则丢弃。最后将多个通道得到的候选池取并集，得到剪枝结果。这样做的目的，是尽量保留多样性，避免单一指标主导。

相关性阈值本身也不一定要固定。为了多保留一些高质量候选，我通常会采用逐步衰减的方式，例如：

- 前 5 个因子，阈值设为 0.85

- 第 5 到第 10 个因子，阈值设为 0.80

- 之后的阈值设为 0.75


> [!NOTE] [图片 OCR 识别内容]
> 阶段二:  多通道相关性剪枝 (保持物种多样性)
> Pruning Matrix
> Top 5 候选池
> 第5-10候选池
> 第10+候选池
> (Max Corr < 0.85)
> (Max Corr < 0.80)
> (Max Corr < 0.75)
> Sharpe 通道
> Fitness 通道
> Margin 通道
> raW
> signals
> 拒绝单-维度的粗暴过滤。多维降维与衰减式相关性阈值。有效防止因孑沦为高度同质化的近亲繁殛产物。
> NotebookLN


### ### 2.4 进入 1/2/3 阶或 robust

完成剪枝之后，就进入传统的增强流程。

最常见的路径是：

裸信号进入 1 阶，1 阶继续筛选后进入 2 阶，2 阶再进入 3 阶。每一阶之间，都会重复上述的步骤。

如果跑完 1 阶或 2 阶之后，就已经获得了相当数量的可提交因子，那流程通常就到此为止，不再继续向下扩展。

如果跑完之后，可提交因子仍然偏少，我会考虑补跑 robust，通过参数遍历做进一步增强。但这一步需要非常克制。robust 的初衷是检验因子，而不是增强因子。使用过度，容易走向过拟合。

———

## ## 三、检验和提交

### ### 3.1 先过本地相关性

如果候选是 ppa，直接本地跑自己 ppa 池子的相关性即可。

如果候选是 ra，通常会先跑自己 ra 池子的自相关，再继续跑平台 check。

### ### 3.2 借助数据库做一轮人工筛选

对所有待提交因子，我会先在自己的数据库里做一轮浏览和筛选。除了 Sharpe、Fitness 这些基本指标之外，我的数据库里还会显示其他辅助判断信息，例如：

- maxTrade 线是否接近原 PnL

- op 数

- df 数

一般会先按 Sharpe、Fitness、Margin 从高到低排序，再剔除 turnover 过高、op 过多、df 过多的因子，然后进行挑选。

这一层仍然保留较强的人工判断成分。

### ### 3.3 执行测试（一）

这一轮主要是网页端的人工复核，重点看以下几项：

1. 看 compare，对自己的组合有没有提升。对组合明显拖后腿的因子，通常不会进入提交。
2. 看基本指标，确认 TVR 和 return 是否正常，最大回撤是否过高。
3. 看分年度表格。如果 2022 年和 2023 年表现过低，通常也会比较谨慎。
4. 看 PnL 线、Sharpe 线、Turnover 线的形态是否顺眼。

这一层虽然带有一定主观性，但对剔除一些“表面过线、整体感觉不对”的结果很有帮助。

### ### 3.4 执行测试（二）

这一轮主要做可自动化的一键测试。

#### 第一部分是 rank/sign test：

对候选因子跑 rank(alpha) 和 sign(alpha)。如果这些变形版本的 Sharpe 低于原 alpha 的 50%，我一般不会提交。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 067
> 1.00
> 0.40
> 0.75
> 04
> 0.50
> 0.2
> 0.25
> 鼍
> 0.0
> 000
> -0.2
> -0.25
> -0.4
> org sharpe
> 1.00
> -0.50
> 50% orig = 0.50
> -0.6
> 054
> 0.59
> orig
> rank
> slgn
> sign_gn
> sign_gn
> none
> orig
> raTk
> sign
> sign_gn
> sign_gn_none
> Margin
> Turnover
> 10.07
> 24.52
> 745
> 25
> 4|1
> 20
> -20
> 14.62
> 15
> S
> 8
> 11.73
> -40
> 10
> 8.75
> G0
> 3.93
> 78.13
> orig
> rank
> slgn
> sign_gn
> sign_gn_
> none
> org
> rank
> slgn
> slgn_gn
> sign_gn_none
> Returns
> Drawdown
> 301
> 211.27
> 200
> 3.00
> 175
> 150
> 125
> 8
> 100


#### 
> [!NOTE] [图片 OCR 识别内容]
> 181
> RS Test Pnl Compare: QPjgNLqp
> orig
> QPjBNLqP
> OrIg
> rank
> ZYIRLk2Q
> sign
> 58GZVNa1
> sign_gn
> pwzqganx
> 05
> sign_gn_none | mLzPkeqx
> 「
> SIgn_gn
> 日
> -0.5
> -1.0
> -1.5
> Slgn_gn
> none
> UuNw
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
> 2024
> Date


#### 第二部分是 robust test：

对原 alpha 跑 robust 测试。如果结果方差过大，也会比较谨慎。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> 最大值:  1.0900
> 均值: 0.3135
> 中位数:  0.2800
> 最小值:
> -0.3200
> 标准差:
> 0.2960
> 四分位距 (IQR):
> 0.4450
> 极差:  1.4100
> Fitness
> 最大值:  1.8400
> 均值: 0.2300
> 中位数:
> 0.1300
> 最小值: -0.2000
> 标准差:
> 0.3274
> 四分位距 (IQR):
> 0.2900
> 极差:  2.0400
> Margin
> 最大值:  134.2600
> 均值:  12.5754
> 中位数:
> 3.6900
> 最小值: -17.3000
> 标准差:  25.9616
> 四分位距
> (IQR) :
> 10.7450
> 极差:
> 151.5600
> Turnover
> 最大值:  40.9200
> 均值:  14.7835
> 中位数:  11.9300
> 最小值:  3.2800
> 标准差:  8.5542
> 四分位距 (IQR): 12.5750
> 极差:  37.6400
> Returns
> 最大值:  41.9000



> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 100
> 40
> 75
> 30
> 墨
> 20
> 詈
> 50
> 10
> 25
> 0
> 2
> 2
> 2
> 2
> Sharpe
> Fitness
> Margin
> TurnoVer
> 150
> 40
> 詈
> 100
> 詈
> 20
> 50
> -200
> -150
> -100
> -50
> 50
> 100
> 150
> 200
> 10
> 20
> 30
> 40
> 50
> 60
> 70
> Margin
> TurnoVer
> Returns
> Drawdown
> 100
> 75
> 40
> 詈
> 50
> 詈
> 20
> 25
> -40
> -20
> 20
> 40
> 20
> 40
> G0
> 80
> 100
> Returns
> Drawdown



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Decay
> Fitness by Decay
> 1.00
> 1.5
> 0.75
> 0.50
> 1.0
> 0.25
> 0.5
> 0.00
> 0.0
> -0.25
> 22
> GG
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Margin by Decay
> Turnover by Decay
> 40
> 125
> 100
> 30
> 75
> 50
> 20
> 25
> 圭
> 圭
> 10
> 22
> 66
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Returns by Decay
> Drawdown by Decay
> 40
> 125
> 30
> 100
> 20
> 75
> 10
> 50
> 25
> 22
> RG
> 120
> 240
> 512
> 22
> FG
> 120
> 240
> 512



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Universe
> Fitness by Universe
> 1.0
> 0.5
> 0.0
> 丰
> A
> A
> Universe
> Universe
> Margin by Universe
> Turnover by Universe
> 40
> 100
> 50
> 20
> Universe
> Universe
> Returns by Universe
> Drawdown by Universe
> 40
> 100
> 20
> 50
> 0
> 0
> TOPSOO
> TOP2O0
> TOP3000
> TOPSP5OO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1000
> MINVOLI
> MINVOL
> ILLIQUID
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOPSPSOO
> TOP1000
> MINVOLIM
> MINVOLTM
> '
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOP1OOO
> TOPSPSOO
> MINVOLIM
> TOPSPSOO
> MINVOLTN



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Neut
> Fitness by Neut
> 生
> 圭空臣孛l
> Neut
> Neut
> Margin by Neut
> Turnover by Neut
> 40
> 100
> 20
> 丢
> Neut
> Neut
> Returns by Neut
> Drawdown by Neut
> 25
> 100
> 垩 +
> 豆S星|臣
> 50
> 鹇 -工
> 丰茔茔
> 簋
> SLOW
> SECTOR
> 簋
> 磊
> 
> SECTOR
> 
> NONE
> FAST
> INDUSTRY
> 
> MONRKM
> CROWDING
> 鸶
> FAST
> 
> _MOMERKAM
> STATISTICAL
> STATISTICAL
> AND
> AND_
> SLOW_
> SLOW
> 昱
> AND_
> REVERSION
> REVERSION
> 簋
> SLOW
> NONE
> FAST
> INDUSTRY
> SUBINDUSTRY
> SECTOR
> 
> CROWDING
> 簋
> SLOW
> NONE
> n
> SUBINDUSTRY
> SECTOR
> _MOMERKBM
> CROWDING
> INDUSTRY
> STATISTICAL
> STATISTICAL
> 昱
> AND_
> SLOW
> SLOW
> AND_
> AND
> REVERSION
> REVERSION
> 簋
> SUBINDUSTRY
> FAST
> SUBINDUSTRY
> $
> NONE
> FAST
> INDUSTRY
> SECTOR
> MOMRKEM
> CROWDING
> SLOW
> NONE
> FAST
> INDUSTRY
> 暑
> _MOMERKAM
> CROWDING
> STATISTICAL
> STATISTICAL
> AND_
> AND_
> s
> SLOW_
> AND_
> AND_
> IERSION
> IRSION



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Group
> Fitness by Group
> 1.0
> 0.5
> 00
> 9
> "
> Group
> Group
> Margin by Group
> Turnover by Group
> 40
> 100
> 50
> 20
> y
> 聃貊
> 酾堕百
> 酝
> 苫 酶错
> Group
> Group
> Returns by Group
> Drawdown by Group
> 40
> 丐
> 100
> 20
> 亘
> 5
> q醒
> 50
> 5颐
> 牾-鸱



> [!NOTE] [图片 OCR 识别内容]
> 167
> PNL Curves by universe (colored by group max PNL)
> 1e7
> universe
> TOP200141898873.0000)
> C"」 '
> T0P3000(34151195.00OOJ
> TOPSP500 (33184197.0000)
> 1' |
> TOP500131186982.0000)
> ICY7 
> 4.00
> TOP1000 125998203.000OJ
> Lqiyc
> ILLOUID_NINVOLII (2136329400001
> 3.75
> 3.50
> 3.25
> _
> 300
> 2.75
> 250
> 2.25
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
> 2024



> [!NOTE] [图片 OCR 识别内容]
> 1e7
> PNL Curves by uni neut (colored by group max PNL )
> 1e7
> uni*neut
> TOP2OO NONE (41898873.0000)
> CeyAr
> 40
> T0P3000 NONE (34151196.00001
> T
> TOPSPSOO NONE 133184197.00OO)
> VSA
> TOP5OO NONE (311869820000)
> TOPIO0 NONE (259982030000)
> ILLIGUID_NINVOLIIINONE (21363294.00001
> 35
> TOPZOO SECTOR (13214659.0000)
> TOPZOOINDUSTRY (13052861.0000)
> TOP2OO MARKET (10940356.00001
> TOP3000 SUBINDUSTRY (1033918000001
> TOP3OOD*INDUSTRY (9251236.0000)
> 30
> TOP300 FAST (9050392.00001
> TOP200 REVERSION_AND_NONENTUI (8732002.0000j
> TOP3OOO SECTOR (8669384.0000)
> TOP30ODNARKET (7947224.0000)
> 25
> 
> TOP3OOOREVERSION_AND_MOMENTUM 17463611.0000)
> TOP200CROIDING (7316500.000O)
> TOP3OOOCROWDING (71144850000I
> 鱼
> TOPSPSOO FAST (6302806.00001
> _
> TOP3000 SLOI (6275460,000OI
> 20
> 盏
> TOPZOO*FAST (6193168.00001
> TOPSPSOO SECTOR (6187494,0000)
> TOP3000 SLOI
> AND_FAST (6159347.0000)
> 趸
> TOP3000STATISTICAL (5796010,0DOOI
> TOP5OD FAST (5775770.00001
> TOP5OD*SLOW (5654524,0000)
> 1.5
> 邕
> TOPSOOINDUSTRY (5461946.0000)
> TOPSPSOOINDUSTRY (5428550.0OOOI
> TOP5OOSLOW_AND_FAST (5389790.00OO)
> TOP200*SUBINDUSTRY (4519126.0000)
> TOPSP5OO M4RKET (4494552,000OI
> 1.0
> TOPSPSOO SLOI (44774460000)
> TOPSPSOOSLOI_AND_FAST (4446454,0000)
> TOPSOOCROWDING (4356666.0000)
> ILLOUID_NINVOLII FAST (4308647.000O)
> TOPSPSOO REVERSION_AND_NOMENTUN 14271460.0000]
> 05
> TOPSOO REVERSION_AND_NONENTUN14255880.0000)
> TOP5O0 SECTOR (421024-.0OOOI
> TOPSPSOO CROWDING (3929487.000O)
> TOP5O0 NIARKET (3624809.0OOO)
> ILLQUID_NINVOLIIINDUSTRY (31659490000)
> 00
> ILLIQUID_NINVOLIISLOW_AND_FAST (31279620000)
> O
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 2024
> TOPI0OOINDUSTRY (3089212000O
> ILLIQUID_NINVOLII SLOW (2823083 OOOOI
> Date
> TOP5OO*STATISTICAL (2540856,000O)


这一部分已经实现了自动化，只需要输入原 alpha 的 id，就可以一键完成。

### ### 3.5 执行测试（三）

这一步是 AI 第二次进入流程。

把该因子的表达式、数据字段含义发给 AI，让它输出以下内容：

1. 经济学解释
2. 因子值越大代表什么
3. 做多/做空因子值高/低的公司的合理性与潜在不合理处
4. 符合平台格式的因子描述，用于填写因子描述

对于经济学解释显著与常识不符的，我会慎重考虑。让AI提出正反两方面的观点，也可以防止从结果倒推原因。另外，认真填写描述似乎对weight有一定作用，可能可以增加自己因子被选中的机会。


> [!NOTE] [图片 OCR 识别内容]
> 二
> 经济学含义 (核心)
> 这个因子本质是在找:
> 在同一子行业内。同时具备高盈利能力 (ROA) 和高运营效率 (资产周转率)  的公司
> 因子值高的公司意味着什么?
> 当因子值高时,
> 公司通常具备:
> 1。资产赚钱能力强 (高ROA)
> 成本控制好 /定价能力强
> 或者资本结构合理
> 2。资产使用效率高 (高资产周转率)
> 存货周转快
> 业务模式轻资产 |高周转
> 3。经营质量高
> 不是"靠重资产堆利润'
> 而是"又赚得多;
> 又转得快"
> 典型特征:
> 消费品龙头 (高周转+稳定利润)
> 优质制造企业 (精益生产)
> 平台型轻资产公司



> [!NOTE] [图片 OCR 识别内容]
> 三
> 做多高因子股票的逻辑
> 合理性
> 1
> 质量因子 (Quality Factor)
> 高ROA = 好公司
> 高周转 =高效率
> 〉
> 双重筛选。避免"假盈利"
> 2。抗周期能力强
> 高效率公司更能应对需求波动
> 3。资本配置优
> 资产利用率高 >再投资回报更高
> 4
> 行业内比较更公平
> group_rank避免行业偏差 (例如银行 Vs 科技)
> 风险与不合理之处
> 1。可能错杀"重资产优质公司"
> 如公用事业
> 能源。半导体
> 天生周转率低 >被低估
> 2
> 周期顶部风险
> 在景气周期中:
> 收入暴涨 >周转率虚高
> 利润暴涨 > ROA虚高
> >因子容易在高点买入
> 3.
> ZSCore引l入极端值放大
> 异常高收入公司可能被过度放大权重
> 4。没有考虑增长性
> 高ROA + 高周转+高成长
> 可能是"成熟但不增长"的公司



> [!NOTE] [图片 OCR 识别内容]
> 四。做空低因子股票的逻辑
> 合理性
> 低ROA + 低周转:
> 〉
> 资产使用效率差 +盈利能力差
> 〉常见于:
> 僵尸企业
> 低效国企
> 管理层低效公司
> 风险
> 1
> 反转风险 (Turnaround)
> 低效公司一旦改革 >爆发性上涨
> 2
> 高投入早期公司
> 科技|创新企业:
> 当前ROA低。周转低
> 但末来潜力大
> 3.
> 行业周期底部
> 全行业ROA下降 >错误做空



> [!NOTE] [图片 OCR 识别内容]
> 五。整体评价
> 这个因子:
> 逻辑清晰 (杜邦框架)
> 行业内中性化 (很重要)
> 同时刻画"盈利 +效率"
> 但=
> 对周期敏感
> 偏好轻资产行业
> 缺乏增长维度
> 六。推荐评分
> 评分:  &110
> 适合作为:
> 核心质量因子之一
> 与成长因子 |估值因子结合使用
> 不建议单独使用的原因:
> 周期波动较大
> 行业风格偏向明显
> 七
> 英文总结
> Idea: Identify firms
> both high profitability and high asset efficiency within subindustries。
> Rationale for data used: Net income over total assets captures profitability (ROA), While revenue over
> total assets measures asset turnover; jointly reflecting operational and capital efficiency。
> Rationale for operators used: Ranking ROA emphasizes relative profitability; Z-scoring turnover highlights
> deviations in efficiency; and multiplication ensures only firms strong in both dimensions score highly; while
> group ranking neutralizes industry effects。
> with


### ### 3.6 提交

完成上述步骤之后，进入最终提交。

———

## ## 四、Harness engineering 下的 AI Quant

这套工作流我已经用了很久。回头看，它最核心的一点其实很简单：让 AI 做擅长的创新扩展的工作，让代码承担稳定、重复、明确的任务，让人保留高层决策和控制权。最近 harness engineering 这个概念开始流行起来，我觉得它非常适合概括这套方法。

如果打个比喻，这套流程更像一列火车。AI 驱动的裸信号生成，像是给火车换上了更强劲的引擎；而相关性约束、稳健性测试、RS 测试和分层筛选机制，则像轨道、道岔和信号系统。动力很强，方向也比较稳定。AI 先提出新的创意，后续流程再为这些创意补上轨道，因此轨道本身并不会提前封死创新。

相比之下，全 AI 工作流更像一辆高性能汽车。它有强劲动力，有自动驾驶，也有各种 skills 和提示词作为导航和路牌，但它仍然要在开放路网里持续做局部判断。一旦方向偏了，系统往往不会立刻停下，而是会沿着错误道路继续高速前进。动力越强，偏航之后冲出去的距离通常也越远，最后掉头的成本越高。


> [!NOTE] [图片 OCR 识别内容]
> 认知重构:  全A1工作流 VS. Harness Engineering
> 全A1工作流 /汽车模型
> Harness Engineering / 火车模型
> 特征:  极高的自主性;Al包揽生成。测试与纠错。
> 特征: A1提供前迸的动力 (引擎)
> 硬编码视则提供运行的轨道 (铁轨)
> 隐患:  在金酃嗓声中猴易[轨或陷入幻觉;方向不可控,容崭成本极高。
> 优势:  能量榄精准约束。铁轨本身不限制创造力,只设定致命哟边界。
> 真正的力量不在于A1的绝对自主。而在于对A1能量的精准约束。
> NotebookLM


———

## ## 五、与模板爆炸法的区别

AI打工人中现在用的一套方法，是先让 AI 提出一个因子表达式模板，再给出可以填入模板的数据集，然后围绕这个模板做大规模生成和回测。这种方法可以称为模板爆炸法。

研究者先假定某种表达式结构大体有效，再让模型或程序去填不同的数据字段。这样做的好处是效率高、可控性强，也适合围绕某一类已知有效结构做快速放大。但这个方法对于所使用的模板要求是比较高的。除了内置的几套验证过的有效模板，如果新手直接自己探索模板或者让AI未经验证给出一个模板，其实很难说效果会好。

而生成裸信号的方法更偏向发现式研究。通过这个方法发现和验证后的结果，也可以总结成模板，两者并不冲突。

———

## ## 六、AI 还能继续做的事

在当前版本里，AI 主要参与裸信号生成和最终的经济学解释。中间流程仍然以硬代码和人工软判断为主。但如果将现在中间段的操作日志、数据全量记录下来，然后交给AI去统计和发现其中的模式，AI 也会在这些位置上逐步加深参与。

———

## ## 结语

我对这套工作流的总体评价很简单：

它让 AI 做 AI 擅长的部分，让代码做代码擅长的部分，让人继续承担研究中最重要的判断工作。

在量化研究这种高噪声、高伪阳性、高竞争的场景里，有价值的通常不是盲目追求让 AI 覆盖更多步骤，而是能够约束并高效利用AI的能量。

这正是 Harness engineering 在 AI Quant 里的意义。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的分享，kitty哥是一个严谨思考的人，经常看到他的各种统计图。

使用AI的过程，感觉大起大落，缺少了约束，受益良多。

===========================================================

长风破浪会有时，直挂云帆济沧海。

===========================================================


---

### 技术对话片段 18 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: [Commented] OpenClaw三省六部架构助力Alpha构建实践.md
- **时间**: 3个月前

**提问/主帖背景 (CZ39633)**:
## 三省六部 OpenClaw 架构概述


> [!NOTE] [图片 OCR 识别内容]
> README
> Ri Contributing
> 巫
> MIT license
> 
> 三省六部
> Edict
> 我用 1300年前的帝国制度。重新设计了 Al 多 Agent 协作架构。
> 结果发现。古人比现代 Al 框架更懂分权制衡。
> 12个 AlAgent (11 个业务角色 +1个n容角色) 组成三省六部:  太子分拣。中#省规刘。门下省审核封驳。尚书省派发。六部+吏部井行执行。
> 比 CrewAl 多-层割/性囤核。比 AutoGen 多一个实时雷板。
> Oemo
> 30秒体验
> 架构
> 看板功能
> 架构文档
> English
> 参与贡献
> OpenClaw  Required
> Python
> 3.9+
> Agents  12 Speclalied
> Dashboard
> mam
> Ucense
> MO
> Frontend
> React 18
> Backend  Stdllb only
> 公众号
> CFT0808
 
我最近发现了GitHub上活跃的开源项目“三省六部·Edict”，它基于OpenClaw框架，借鉴了唐代三省六部制，重新设计AI协作流程。该系统由 **12**  **个AI**  **角色** （含1个兼容官）组成：包括 **太子** （消息分拣）、 **中书省** （规划中心）、 **门下省** （审核把关）、 **尚书省** （调度大脑），以及六部（ **户、礼、兵、刑、工、吏** ）和 **早朝官** 。各角色分工明确，通过严格的权限矩阵和状态检查，保证任务沿中书→门下→尚书→六部的单向流程流转。这一架构的特点是：在 **中书规划** 和 **门下审查** 之间加入了强制质检关卡，并辅以实时看板监控，全程可停、可审、可追踪。下图概括了其关键流程：


> [!NOTE] [图片 OCR 识别内容]
> 行派岗
> 户部:  数据处理
> 行派岗
> 礼部:  文档编写
> +行派岗
> 兵部:  代码实现
> 接受任务 (太子)
> 中书省:  规划方案
> 门下省:  方案审核
> 尚书省:  批;并派发
> 尚书省:  汇总结果
> 回报归档 (奏折)
> 牛行派岗
> 刑部:  合规审计
> 行派岗
> 工部:  环境部署
> 并行派发
> 吏部: Agent管理


## Agent与Alpha构建环节映射

下面的表格展示了三省六部各Agent的职责如何映射到Alpha构建的关键步骤：

**Agent**

**职责摘要**

**对应Alpha**  **环节**

**示例任务**

太子

消息分拣，提炼需求

接收需求、确认目标

从聊天记录识别并提炼出“需构建RSI因子”

中书省

规划中枢，拆解子任务

设计因子方案

确定因子用到哪些数据字段、逻辑流程

门下省

审议把关，质量与风险评估

校验方案完整性

审查因子是否使用未来数据、是否符规则

尚书省

调度大脑，分配执行任务

任务派发与进度跟踪

将需求分配给数据、编码、测试任务并跟踪

户部

数据资源与核算

数据准备

提取股票行情/财报等数据并整理分析

礼部

文档规范与报告

文档和报告输出

撰写Alpha方案说明、生成提交报告

兵部

功能开发与代码实现

方案实现与调试

使用表达式语言/代码实现因子逻辑

刑部

安全合规与审计

合规与安全检查

扫描因子代码中的违规问题（如未来函数）

工部

CI/CD与基础设施

环境部署与自动化

搭建回测流水线、Docker配置或托管方案

吏部

人事与Agent管理

系统管理与权限配置

管理Agent技能库、配置API访问权限

早朝官

情报枢纽，资讯收集

情报与参考支持

收集财经新闻/研报，为因子设计提供背景信息

通过这种映射，我们可以看到每个Agent与Alpha开发各环节的对应关系，例如中书省负责分解构思任务、兵部负责编码实现等。借助平台提供的Python API，这些Agent的任务都可以通过Skill或脚本调用平台模拟接口，自动化执行相应工作。

## OpenClaw解决AI构建Alpha痛点

使用大模型构建Alpha时，我们常遇到质量不可控、结果难审计、成本高等问题。 **三省六部**  **OpenClaw**  **架构** 针对这些痛点提供了机制：
-  **质量把关+**  **自动化监控：**  引入门下省进行强制审核，任何不合格的方案都会被退回重做。通过实时看板和多角色协作，避免了单个模型“胡乱输出”而无人监管的情况。中所示，系统可实时监控各Agent进度并支持随时暂停/恢复，增强调度可控性。
-  **可审计性与可追踪：**  与传统直接对话式AI不同，三省六部框架强调流程记录。每一步任务状态和输出都会存档归档（奏折），形成完整日志。这使得因子构建过程可复现、可审计，符合量化研究对可解释性的要求。
-  **成本控制与效率：**  虽然引入多Agent看似增加查询次数，但也可细化任务、并行处理、热切换模型。比如让简单任务用小模型解决，让核心规划/审计环节调用大模型，有助于降低整体Token消耗。军机处提供Token排行榜和消耗监测，可帮助我们优化调用策略。
-  **自动化协作：**  各Agent角色可通过Skill集成现有工具，形成近似SOP的工作流。例如使用Agent间信息流和权限控制，我们可以构建半自动化流程，让AI协作产出Alpha而不是漫谈式讨论。如Edict所示，信息单向流向受控，确保复杂任务执行可预测。

**具体建议：**  为充分利用这些优势，我建议：
- 在设计因子时将任务拆分，将AI生成的构思视为 **规划输出** ，由“门下省”补充风险控管步骤；
- 利用看板实时监控多步骤任务执行，一旦出现偏差（如模型跑偏），可人工干预停止或修正；
- 设定成本预算，在 **吏部** 角色下监控Token和资源使用，优先用轻量模型处理非关键子任务；
- 将平台回测和分析步骤也纳入多Agent流程（如由兵部或工部自动调用BRAIN模拟接口），形成端到端协作。

## 实施路线图

可以分阶段导入OpenClaw三省六部架构，逐步验证并优化：


> [!NOTE] [图片 OCR 识别内容]
> 阶
> 目标
> 关键动作
> 验收标准
> 资原[拔本
> 环境搭
> 部署OpenClaw/Edic实例;  配置与
> 系统部署成功。所有
> 少眼务器
> 建与角
> 台4PI的接入;  定义各AgentsgsoUL
> Agent在线并己初步配
> 资源;  可复
> 霞
> 色义
> (职责说明)
> 置5OUL; 权限矩陟生
> 用公开镜像
> 验证任
> 选择简单因子需求进行测试:  例如制
> 能出因孑方案并1功
> 模型调用费
> 总
> 务 示
> 定"移动平均Alpha"任务;  让中书背规
> 完成一次模拟回测;  谎
> 用 测试数
> 演
> 划-门下肖审核-各部执行
> 程日志可查看
> 优1交
> 根据试点反馈优化50UL与撰示;  为
> 部署-套稳定的因子开
> 主要为a间
> 茌
> 互与技
> Agent添加平台数据和回测相关的
> 发工怍;  实际因子效
> 「本。r步
> Sklls;
> 调整模型切换策略
> 果达到  
> 完善
> 扩展至
> 在谎程中加入复杂因子构建场景 (如
> 多种因子成功提交;  效
> 培训成本
> 穆
> 更因
> 融合新阋:子)
> 培训团队使用新系
> 率或成功率相较原~程
> 可能坳更
> 子类
> 巯;  整合自动报告生成
> 有提升
> 多模型调用


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享。

大佬，这么搞一个alpha需要多少token，思路很严谨，多agent互相协作。

=================================================================

长风破浪会有时，直挂云帆济沧海。

=================================================================


---

### 技术对话片段 19 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] OpenClaw三省六部架构助力Alpha构建实践_39070236782231.md
- **时间**: 3个月前

**提问/主帖背景 (CZ39633)**:
## 三省六部 OpenClaw 架构概述


> [!NOTE] [图片 OCR 识别内容]
> README
> Ri Contributing
> 巫
> MIT license
> 
> 三省六部
> Edict
> 我用 1300年前的帝国制度。重新设计了 Al 多 Agent 协作架构。
> 结果发现。古人比现代 Al 框架更懂分权制衡。
> 12个 AlAgent (11 个业务角色 +1个n容角色) 组成三省六部:  太子分拣。中#省规刘。门下省审核封驳。尚书省派发。六部+吏部井行执行。
> 比 CrewAl 多-层割/性囤核。比 AutoGen 多一个实时雷板。
> Oemo
> 30秒体验
> 架构
> 看板功能
> 架构文档
> English
> 参与贡献
> OpenClaw  Required
> Python
> 3.9+
> Agents  12 Speclalied
> Dashboard
> mam
> Ucense
> MO
> Frontend
> React 18
> Backend  Stdllb only
> 公众号
> CFT0808
 
我最近发现了GitHub上活跃的开源项目“三省六部·Edict”，它基于OpenClaw框架，借鉴了唐代三省六部制，重新设计AI协作流程。该系统由 **12**  **个AI**  **角色** （含1个兼容官）组成：包括 **太子** （消息分拣）、 **中书省** （规划中心）、 **门下省** （审核把关）、 **尚书省** （调度大脑），以及六部（ **户、礼、兵、刑、工、吏** ）和 **早朝官** 。各角色分工明确，通过严格的权限矩阵和状态检查，保证任务沿中书→门下→尚书→六部的单向流程流转。这一架构的特点是：在 **中书规划** 和 **门下审查** 之间加入了强制质检关卡，并辅以实时看板监控，全程可停、可审、可追踪。下图概括了其关键流程：


> [!NOTE] [图片 OCR 识别内容]
> 行派岗
> 户部:  数据处理
> 行派岗
> 礼部:  文档编写
> +行派岗
> 兵部:  代码实现
> 接受任务 (太子)
> 中书省:  规划方案
> 门下省:  方案审核
> 尚书省:  批;并派发
> 尚书省:  汇总结果
> 回报归档 (奏折)
> 牛行派岗
> 刑部:  合规审计
> 行派岗
> 工部:  环境部署
> 并行派发
> 吏部: Agent管理


## Agent与Alpha构建环节映射

下面的表格展示了三省六部各Agent的职责如何映射到Alpha构建的关键步骤：

**Agent**

**职责摘要**

**对应Alpha**  **环节**

**示例任务**

太子

消息分拣，提炼需求

接收需求、确认目标

从聊天记录识别并提炼出“需构建RSI因子”

中书省

规划中枢，拆解子任务

设计因子方案

确定因子用到哪些数据字段、逻辑流程

门下省

审议把关，质量与风险评估

校验方案完整性

审查因子是否使用未来数据、是否符规则

尚书省

调度大脑，分配执行任务

任务派发与进度跟踪

将需求分配给数据、编码、测试任务并跟踪

户部

数据资源与核算

数据准备

提取股票行情/财报等数据并整理分析

礼部

文档规范与报告

文档和报告输出

撰写Alpha方案说明、生成提交报告

兵部

功能开发与代码实现

方案实现与调试

使用表达式语言/代码实现因子逻辑

刑部

安全合规与审计

合规与安全检查

扫描因子代码中的违规问题（如未来函数）

工部

CI/CD与基础设施

环境部署与自动化

搭建回测流水线、Docker配置或托管方案

吏部

人事与Agent管理

系统管理与权限配置

管理Agent技能库、配置API访问权限

早朝官

情报枢纽，资讯收集

情报与参考支持

收集财经新闻/研报，为因子设计提供背景信息

通过这种映射，我们可以看到每个Agent与Alpha开发各环节的对应关系，例如中书省负责分解构思任务、兵部负责编码实现等。借助平台提供的Python API，这些Agent的任务都可以通过Skill或脚本调用平台模拟接口，自动化执行相应工作。

## OpenClaw解决AI构建Alpha痛点

使用大模型构建Alpha时，我们常遇到质量不可控、结果难审计、成本高等问题。 **三省六部**  **OpenClaw**  **架构** 针对这些痛点提供了机制：
-  **质量把关+**  **自动化监控：**  引入门下省进行强制审核，任何不合格的方案都会被退回重做。通过实时看板和多角色协作，避免了单个模型“胡乱输出”而无人监管的情况。中所示，系统可实时监控各Agent进度并支持随时暂停/恢复，增强调度可控性。
-  **可审计性与可追踪：**  与传统直接对话式AI不同，三省六部框架强调流程记录。每一步任务状态和输出都会存档归档（奏折），形成完整日志。这使得因子构建过程可复现、可审计，符合量化研究对可解释性的要求。
-  **成本控制与效率：**  虽然引入多Agent看似增加查询次数，但也可细化任务、并行处理、热切换模型。比如让简单任务用小模型解决，让核心规划/审计环节调用大模型，有助于降低整体Token消耗。军机处提供Token排行榜和消耗监测，可帮助我们优化调用策略。
-  **自动化协作：**  各Agent角色可通过Skill集成现有工具，形成近似SOP的工作流。例如使用Agent间信息流和权限控制，我们可以构建半自动化流程，让AI协作产出Alpha而不是漫谈式讨论。如Edict所示，信息单向流向受控，确保复杂任务执行可预测。

**具体建议：**  为充分利用这些优势，我建议：
- 在设计因子时将任务拆分，将AI生成的构思视为 **规划输出** ，由“门下省”补充风险控管步骤；
- 利用看板实时监控多步骤任务执行，一旦出现偏差（如模型跑偏），可人工干预停止或修正；
- 设定成本预算，在 **吏部** 角色下监控Token和资源使用，优先用轻量模型处理非关键子任务；
- 将平台回测和分析步骤也纳入多Agent流程（如由兵部或工部自动调用BRAIN模拟接口），形成端到端协作。

## 实施路线图

可以分阶段导入OpenClaw三省六部架构，逐步验证并优化：


> [!NOTE] [图片 OCR 识别内容]
> 阶
> 目标
> 关键动作
> 验收标准
> 资原[拔本
> 环境搭
> 部署OpenClaw/Edic实例;  配置与
> 系统部署成功。所有
> 少眼务器
> 建与角
> 台4PI的接入;  定义各AgentsgsoUL
> Agent在线并己初步配
> 资源;  可复
> 霞
> 色义
> (职责说明)
> 置5OUL; 权限矩陟生
> 用公开镜像
> 验证任
> 选择简单因子需求进行测试:  例如制
> 能出因孑方案并1功
> 模型调用费
> 总
> 务 示
> 定"移动平均Alpha"任务;  让中书背规
> 完成一次模拟回测;  谎
> 用 测试数
> 演
> 划-门下肖审核-各部执行
> 程日志可查看
> 优1交
> 根据试点反馈优化50UL与撰示;  为
> 部署-套稳定的因子开
> 主要为a间
> 茌
> 互与技
> Agent添加平台数据和回测相关的
> 发工怍;  实际因子效
> 「本。r步
> Sklls;
> 调整模型切换策略
> 果达到  
> 完善
> 扩展至
> 在谎程中加入复杂因子构建场景 (如
> 多种因子成功提交;  效
> 培训成本
> 穆
> 更因
> 融合新阋:子)
> 培训团队使用新系
> 率或成功率相较原~程
> 可能坳更
> 子类
> 巯;  整合自动报告生成
> 有提升
> 多模型调用


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享。

大佬，这么搞一个alpha需要多少token，思路很严谨，多agent互相协作。

=================================================================

长风破浪会有时，直挂云帆济沧海。

=================================================================


---

### 技术对话片段 20 (原帖: OS Super Alpha Competition 2025 (SAC))
- **原帖链接**: [Commented] OS Super Alpha Competition 2025 SAC.md
- **时间**: 1年前

**提问/主帖背景 (HT97317)**:
```
How to improve OS score in the Super Alpha Competition 2025 (SAC)?
```

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
The challenge of improving the OS score in SAC—or anticipating Super Alpha’s out-of-sample performance—deserves deeper exploration, yet remains under-discussed in our community. Given that Super Alpha comprises numerous Regular Alphas, this gap is particularly noteworthy.

As a newcomer, I’ve studied the Powerpool Alpha rules closely, including insights from PPAC webinars. One observation stands out: many Regular Alphas with  *average*  Sharpe/Fitness metrics demonstrate  **robust performance**  when combined. This suggests a critical nuance:  **Super Alpha shouldn’t be evaluated through the lens of individual alphas alone** . Portfolio construction, as a specialized field within quant investing, plays a decisive role.

In the current SAC competition (Group G2), my initial review of the selected Regular Alphas revealed underwhelming standalone metrics. However, their  *combined output*  proved surprisingly effective.

I look forward to hearing others’ perspectives on alpha diversity or alternative approaches to enhancing Super Alpha’s out-of-sample resilience.


---

### 技术对话片段 21 (原帖: OS Super Alpha Competition 2025 (SAC))
- **原帖链接**: https://support.worldquantbrain.com[Commented] OS Super Alpha Competition 2025 SAC_32603381339927.md
- **时间**: 1年前

**提问/主帖背景 (HT97317)**:
```
How to improve OS score in the Super Alpha Competition 2025 (SAC)?
```

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
The challenge of improving the OS score in SAC—or anticipating Super Alpha’s out-of-sample performance—deserves deeper exploration, yet remains under-discussed in our community. Given that Super Alpha comprises numerous Regular Alphas, this gap is particularly noteworthy.

As a newcomer, I’ve studied the Powerpool Alpha rules closely, including insights from PPAC webinars. One observation stands out: many Regular Alphas with  *average*  Sharpe/Fitness metrics demonstrate  **robust performance**  when combined. This suggests a critical nuance:  **Super Alpha shouldn’t be evaluated through the lens of individual alphas alone** . Portfolio construction, as a specialized field within quant investing, plays a decisive role.

In the current SAC competition (Group G2), my initial review of the selected Regular Alphas revealed underwhelming standalone metrics. However, their  *combined output*  proved surprisingly effective.

I look forward to hearing others’ perspectives on alpha diversity or alternative approaches to enhancing Super Alpha’s out-of-sample resilience.


---

### 技术对话片段 22 (原帖: PPAC 82名一些小心得经验分享)
- **原帖链接**: [Commented] PPAC 82名一些小心得经验分享.md
- **时间**: 1年前

**提问/主帖背景 (XZ77557)**:
大家好，本人于今年1月份成为顾问开始提交alpha，参加了PPAC比赛，获得82名，分享一下一些心得体会。
（1）alpha挖掘
我在提交每个alpha前都会遍历一遍所有的中性化，选最好的提交，这个方式在很多时候都会找到更好的因子可以提交。
如果有group字段的话，我参考论坛里的帖子，提前暴力一遍所有group，对group进行分组，每次使用group时从组里面选一个来回测，提高回测效率
（2）提交标准
低相关性：我一般会选择相关性低的提交，确保组合的多样性，从而提高组合的表现。
margin：我一般只提交margin大于15%的因子，防止手续费过多
turnover：我提交的因子一般在15%以下的换手率，如果过高换手，会看retruns和margin，这两个高的话才会交，但是大于30%的换手一般也不交
fitness：尽量交1.5以上的
年份：只提交年份多的因子
目前的value还比较低，还需要有很多改进的方向，还得向论坛里的前辈们学习，继续努力！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
坚持做正确的事，value factor会提升的，感谢分享！

====================================================================================

==================================================================================================================================================================================


---

### 技术对话片段 23 (原帖: PPAC 82名一些小心得经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] PPAC 82名一些小心得经验分享_32602221310487.md
- **时间**: 1年前

**提问/主帖背景 (XZ77557)**:
大家好，本人于今年1月份成为顾问开始提交alpha，参加了PPAC比赛，获得82名，分享一下一些心得体会。
（1）alpha挖掘
我在提交每个alpha前都会遍历一遍所有的中性化，选最好的提交，这个方式在很多时候都会找到更好的因子可以提交。
如果有group字段的话，我参考论坛里的帖子，提前暴力一遍所有group，对group进行分组，每次使用group时从组里面选一个来回测，提高回测效率
（2）提交标准
低相关性：我一般会选择相关性低的提交，确保组合的多样性，从而提高组合的表现。
margin：我一般只提交margin大于15%的因子，防止手续费过多
turnover：我提交的因子一般在15%以下的换手率，如果过高换手，会看retruns和margin，这两个高的话才会交，但是大于30%的换手一般也不交
fitness：尽量交1.5以上的
年份：只提交年份多的因子
目前的value还比较低，还需要有很多改进的方向，还得向论坛里的前辈们学习，继续努力！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
坚持做正确的事，value factor会提升的，感谢分享！

====================================================================================

==================================================================================================================================================================================


---

### 技术对话片段 24 (原帖: PPAC量化经历分享经验分享)
- **原帖链接**: [Commented] PPAC量化经历分享经验分享.md
- **时间**: 1年前

**提问/主帖背景 (IM49242)**:
1.得益于ppac比赛，alpha的提交不再需要Production correlation的检测。三阶模板可以在usa delay1中回测获取大量alpha。在一个数据集中太多的回测结果在提交3个alpha左右后过多的alpha的自相关性不再满足比赛的条件。巧合下，我在平台上看到了顾问 KZ79256 (Rank 21)分享的本地0误差计算自相关性的帖子，阅读完帖子就可以轻松使用。再通过剪枝函数可以减少check的数量，更快找到可以提交的alpha。

2.除三阶模板之外的alpha模板的提交：在模板大师论坛中寻找一些自己运算符权限之内的模板。为了满足ppac比赛，通过chatgpt去掉了一些运算符，然后自己回测一下，确认有主信号之后就可以使用该模板了。

这里我找到一个alpha是关于期权数据的

trade_when(prc_ui_1080<1,implied_volatility_call_1080-implied_volatility_put_1080,-1)

implied_volatility_call_1080-implied_volatility_put_1080回测已经有明显信号了，但是自宇宙sharpe不满足条件。在prc_ui_1080<1之后就可以通过自宇宙测试了。

通过对期权数据的学习，prc_ui_1080<1应该反映了市场是乐观的。但是不清楚为什么

implied_volatility_call_1080-implied_volatility_put_1080信号明显。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢楼主分享，期权的call-put这个模版非常好。


---

### 技术对话片段 25 (原帖: PPAC量化经历分享经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] PPAC量化经历分享经验分享_31708782472727.md
- **时间**: 1年前

**提问/主帖背景 (IM49242)**:
1.得益于ppac比赛，alpha的提交不再需要Production correlation的检测。三阶模板可以在usa delay1中回测获取大量alpha。在一个数据集中太多的回测结果在提交3个alpha左右后过多的alpha的自相关性不再满足比赛的条件。巧合下，我在平台上看到了顾问 KZ79256 (Rank 21)分享的本地0误差计算自相关性的帖子，阅读完帖子就可以轻松使用。再通过剪枝函数可以减少check的数量，更快找到可以提交的alpha。

2.除三阶模板之外的alpha模板的提交：在模板大师论坛中寻找一些自己运算符权限之内的模板。为了满足ppac比赛，通过chatgpt去掉了一些运算符，然后自己回测一下，确认有主信号之后就可以使用该模板了。

这里我找到一个alpha是关于期权数据的

trade_when(prc_ui_1080<1,implied_volatility_call_1080-implied_volatility_put_1080,-1)

implied_volatility_call_1080-implied_volatility_put_1080回测已经有明显信号了，但是自宇宙sharpe不满足条件。在prc_ui_1080<1之后就可以通过自宇宙测试了。

通过对期权数据的学习，prc_ui_1080<1应该反映了市场是乐观的。但是不清楚为什么

implied_volatility_call_1080-implied_volatility_put_1080信号明显。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢楼主分享，期权的call-put这个模版非常好。


---

### 技术对话片段 26 (原帖: QuantGo Kit：基于Grafana的WorldQuant量化可视化篇代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] QuantGo Kit基于Grafana的WorldQuant量化可视化篇代码优化_37495033591447.md
- **时间**: 5 months ago

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> Value-at-Risk
> (Vaz)
> 
> Mean
> Probability
> 一8
> CVaRB
> LOss
> VaRp


## **一、2026 开端**

本篇是基于上篇  **[QuantGo Kit：基于Go开发的WorldQuant量化工具箱篇]([Commented] QuantGo Kit基于Go开发的WorldQuant量化工具箱篇代码优化_37163832225943.md)**  存入数据库数据做 Grafana可视化，多维度查看和分析自己做过的 Alpha，以及 操作符Op 和 Combine & vf & wf 等数据 .


> [!NOTE] [图片 OCR 识别内容]
> Quantco Kit: 基于Co开发的WorldQuant量化工具箱篇
> 代码优化
> 顾问 ML47973 (Rank 100)
> QuantGo Kit 为何诞生?
> 去年十月,说错了。今年十月, WorldQuant 围区的
> Drod
> COII
> 比赛启动后。我创建了第一个文件夹;
> 写了个计箅平均
> Drod_
> COII
> 的小工具
> 随着需求增多;一个个独立的小程序相继诞生
> 每个都待在各自的文
> 件夹里
> 很快问题浮现:  文件夹海洋让我迷失方向。相似的命名让查找娈得困难;  想要对比多个程序效果时,不得不
> 开启数个VSCode窗口。管理成本陡增
> 于是,
> 一个想法诞生:  为什么不让它们和谐共处?  将所有工具集成到统一框架下,
> 一键运行
> 即时对比 .当
> 这个工具箱逐渐成型时,我想
> 也许其他人也会需要这样的便利 
> 就这样, Quant * Go Kit 诞生了


Grafana 官方下载中心： `[链接已屏蔽]  ，我选择下载Grafana到本地，可以不使用Docker启动 . 默认访问地址  `[链接已屏蔽] ，首次登录账号/密码  `admin/admin`  .


> [!NOTE] [图片 OCR 识别内容]
> GrafanaLabs
> Products
> Open Source
> Solutions
> Leam
> Docs
> Downloads
> Contact Us
> Signin
> Grafana
> Overview
> Grafana project
> Grafana Alerting
> Download
> Download Grafana
> Nightly Builds
> Grafana Cloud
> You
> can USe
> Grafana Cloud to avoid installing; maintaining; and scaling Your own instance of Grafana. Create a free account to get started, which includes free forever access to
> 10k series Prometheus metrics; 5068 logs, 50GB traces; & more。
> Version:
> 12.3.
> Edition:
> Enterprise
> The Enterprise Edition is the default and recommended edition.
> It includes all the features of the OSS Edition; can be used for free and can be upgraded to the full
> Enterprise feature set, including support for Enterprise plugins.
> License:
> Grafana Labs License
> Release Date:
> December 17, 2025
> Release Info:
> Linux
> Windows
> Mac
> Docker
> Linux on ARNIG4
> Pricing


## 

## **二、Visual Layout**

从大布局来看，Grafana - WorldQuant 项目下包括

1. Alpha Quant (Alpha信息数据)

2. Combin & vf & wf (Alpha表现 / Value_Factor / Weight_Factor)

3. Op Informatization (季度性操作符Op信息)

4. Pyramid alpha distribution (季度 | 非季度性 金字塔数据)

四大板块信息 .


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dashboards
> Ai &
> 8|众
> 首页 〉仪表板
> 搜索
> CtrItk
> 十 ~
> 仪表板
> 新建
> 创建并管理仪表板,以将您的数据可视化
> 搜索仪表板
> 按标签筛选
> 已加星标
> 排序
> 名称
> 标签
> WorldQuant
> Alpha Quant
> 器 Combine & Vf & Wf
> 器 Op Informatization
> 品 Pyramid alpha distribution
> CloudVendor Classified Files
> Riemann's Ideas & Analysis


其中，Alpha Quant 共包括 6个 Row, 分别是 理论与可投资术语、已提交的全部alpha(包括隐藏和sa)、GroupBy 分组、Ts_Mean 时序均值、Value Factor 潜在可能影响情况 与 Osmosis Competition 2025 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dladrrggglalpha-quant?orgld=
> &from= 2025-02-13T16:00:00.000Z8to=nowatimezone=browsergvar-alphalD=&var-type=s
> all8var-geniusquarter=S_all8var-region= $_
> Ai
> 8 |众
> 首页
> 仪表板
> WorldQuant
> Alpha Quant
> 搜索。
> CtrI-k
> 十 ~
> 0
> 添加
> 设置
> 退出编辑
> 保存仪表板
> AlphalD
> 输入数值
> TYPE
> AIl
> GENIUS季度
> AlI
> REGION
> AlI X
> UNIVERSE
> AlI X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> All X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> (1panel)
> 已提交的全部alpha(包括隐藏和sa)
> Danels)
> GroupBy 分组
> (6 panels)
> Ts_Mean 时序均值
> (5 panels)
> Value Factor 潜在可能影响情况
> Danels)
> Osmosis Competition 2025
> (5 panels)


[图片 (图片已丢失)]

Combin & vf & wf 有3个数据表，数据来源于 weight_value_factor 和 combined_alpha_performance 表，可以分析Combine、wf何时开始有数据，以及变化情况 .


> [!NOTE] [图片 OCR 识别内容]
> 首页
> 仪表板
> WorldQuant
> Combine & Vf & Wf
> Q 搜索
> CtrItk
> 十 ~
> 19
> 编辑
> 导出
> 分享
> Combine & Vf & wf
> Vf & Combine update
> Combine
> Time
> 10
> 12
> 13
> Value_factor
> 0.86
> 0.71
> 0.75
> 0.48
> 0.72
> 0.44
> 0.57
> combined_alpha_performance
> 2.14
> 2.39
> 2.03
> 1.71
> 1.78
> 1.84
> combined_selected_alpha_performance
> 1.47
> 1.32
> combined_power_pool_alpha_performance
> 1.79
> 1.45
> 1.53
> 1.63
> 1.72
> genius_level
> Grand Master
> Calculation_date
> 2025-06-28
> 2025-07-20 2025-08-07
> 2025-08-19
> 2025-09-11
> 2025-09-20
> 2025-10-06
> 2025-10-25  2025-11-20
> 2025-11-21 2025-12-08  2025-12-162026-01-06
> Vf & Combine '折'线图
> 2.6
> 0,86
> 2,39
> 24
> 0,8
> 2.14
> 22
> 0.75
> 2.03
> 0.72
> 0.71
> 0
> 1,84
> 1.79
> 1.,78
> 1.71
> 1.721.8
> 1.63
> 06
> 53
> 0.57
> 1.6
> 1.45
> 1.321.4
> 0.5
> 48
> 0.44
> 1.18
> 1.2
> 04
> 06/28
> 07/05
> 07/12
> 07/19
> 07/26
> 08/02
> 08/09
> 08/16
> 08/23
> 08/30
> 09/06
> 09/13
> 09/20
> 09/27
> 10/04
> 10/11
> 10/18
> 10/25
> 11/01
> 11/08
> 11/15
> 11/22
> 11/29
> 12/06
> 12/13
> 12/20
> 12/27
> 01/03
> Value_factor
> combined_alpha_performance
> combined_selected_alpha_performance
> combined_power_pool_alpha_
> performance
> 1.18


[图片 (图片已丢失)]

Op Informatization 板块目前只包括 operators 表数据，只存了一个图表，支持操作符 / 操作符类别 / Scope 类别 / Genius等级 / Genius季度 等过滤，这个板块我想要做的是 等季度更新之后，再做一个比较的图表，比如: 2025-Q4 与 2026-Q1 操作符比较，掉级导致操作符少了哪些 信息 .


> [!NOTE] [图片 OCR 识别内容]
> localhost:3OOO/dladgzmgm/op-informatization?orgld = 18from=now-Gh8to=nowgtimezone=browsergvar-OpName=&var-Category=$
> all8var-Scope=$_
> all8var-Geniuslevel= $_
> alI8Var。。
> A》 &
> 8 |众
> 首页
> 仪表板
> WorldQuant
> Op Informatization
> 搜索。
> CtrI-k
> 十~
> 编辑
> 导出
> 分享
> 操作符名
> 输入数值
> 操作符类别
> AII
> Scope类别
> AlI
> Genius等级
> AlI X
> Genius季度 0
> AlI X
> Op操作符表
> name
> category
> SCODe
> definition
> en_description
> Cn
> add
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> addlxi
> Y, filter
> falsel X + Y
> Add all inputs (at least 2 inputs required). If filter
> true  filterall
> eXP
> Arithmetic
> ["COMBO
> "REGULAR" "SELECTION"]
> eXP(X)
> Natural exponential function: e^x
> multiply
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> multiply(x ,y
> filter-false), X
> Multiply all inputs. At least 2 inputs are required. Filter sets the
> sign
> Arithmetic
> ["COMBO
> "REGULAR" "SELECTION"]
> sign(x)
> 讦 input
> 0, return 1; if input
> 0, return -1; if input
> 0, return 0;
> sUbtract
> Arithmetic
> ["COMBO"
> REGULAR" "SELECTION"]
> subtractlx, Y, filter-false), X -Yy
> X-Y.If filter
> true, filter all input NaN to 0 before
> subtracting
> pasteurize
> Arithmetic
> ["COMBO" "REGULAR"]
> pasteurizelx)
> Set to NaN 讦f Xis INF or if the underlying instrument is notin the
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> Iog(x)
> Natural logarithm. For example: Log(high llow) uses natural logal
> purify
> Arithmetic
> ["COMBO
> "REGULAR", "SELECTION"]
> purify(x)
> Clear infinities (+inf, -inf) by replacing with NaN
> arc_tan
> Arithmetic
> ["COMBO
> REGULAR" "SELECTION"]
> arc_tan(x)
> This operator does inverse tangent of input
> log


## **三、详细说明 Alpha Quant 板块**

Alpha Quant 板块 数据来源于 active_alpha_list 数据大表，其中包括了几乎alpha接口的所有数据，不包括 alpha Pnl 数据，然后


> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> AlI
> REGION
> AIl
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> All X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值


**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> OYmgll2
> TYPE 0
> AII X
> GENIUS季度
> AII
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE @
> AII X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
**

**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> AII
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AII X
> STATUS
> AlI X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 样本内-单位收益;非使用例: !二 5%0
> 理论与可投资术语
> panel)
**

**
> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> OYmgll2
> TYPE 0
> AII
> GENIUS季度
> AlI
> REGION
> AII X
> UNIVERSE
> AIl
> DELAY
> AIl
> NEUTRALIZATION
> AII
> MAX TRADE 0
> AII X
> STATUS
> DECOMMISSIONED X
> xQ
> SHARPE 0
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> Selected (1)
> 理论与可投资术语
> panel)
> AII
> 已提交的全部alpha(包括隐藏和sa)
> ACTIVE
> Submitted Alphas (同网页端)
> DECOMMISSIONED
> 100
> UNSUBMITTED
**

过滤字段 包括 AlphaID 可以查询某一个alpha的信息，TYPE分类 ra 与 sa，alpha 属于哪个大区、股票池、延迟处理 和 中性化等等，以及 Alpha的状态，还有 alpha满足 sharpe、fitness、returns 和 margin 等等，所有过滤条件对 Alpha Quant 板块所有数据图表支持查询过滤 .


> [!NOTE] [图片 OCR 识别内容]
> 首页
> 仪表板
> WorldQuant
> Alpha Quant
> Q 搜索
> CtrItk
> 十 `
> |
> 编辑
> 导出
> 分享
> AlphalD
> 输入数值
> TYPE @
> AIl
> GENIUS季度 @
> AlI
> REGION
> AII X
> UNIVERSE
> AII X
> DELAY @
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AI
> STATUS @
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 25-02-15
> 2025-03-11
> 2025-04-04
> 2025-04-28
> 2025-05-22
> 2025-06-15
> 2025-07-09
> 2025-08-02
> 2025-08-26
> 2025-09-19
> 2025-10-13
> 2025-11-06
> 2025-11-30
> 2025-12-24
> Submitted Alphas (每日提交和累计总和)
> 800
> 700
> 600
> 500
> 400
> 300
> 200
> 100
> 02/14
> 03/01
> 03/16
> 03/31
> 04/15
> 04/30
> 05/15
> 05/30
> 06/14
> 06/29
> 07/14
> 07/29
> 08/13
> 08/28
> 09/12
> 09/27
> 10/12
> 10/27
> 11/11
> 11/26
> 12/11
> 12/26
> 每曰提交数
> 暴计总和
> 已提交全部alpha(包括sa)
> id 5
> type ?
> author
> instrument_type ?
> region ?
> universe 5
> delay ?
> decay
> neutralization
> truncat
> OmWI2gQk
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
> TOP5O0
> 18
> MARKET
> OmWlJNmG
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> ILLIQUID_MINVOLIM
> STATISTICAL
> ONK3wVq
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> INDUSTRY
> OVaRQV8
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> STATISTICAL
> OXNXEI2
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> SUBINDUSTRY
> OY32dmq
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> 100
> SUBINDUSTRY
> 0Ymgll2
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> TOP3000
> SUBINDUSTRY
> 13eKO8R
> REGULAR
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR
> T0P2500
> 10
> SUBINDUSTRY
> 1837Vr0
> PFFIII 40
> AAI ^7072
> FOIIITV
> FUNI
> TODnnnl
> FOOIININIC
> active regular alpha
> active superalpha
> id
> region
> universe
> delay
> decay ?
> neutralizatior
> type
> author
> instrument_type
> region
> O1ZJp7r
> ASI
> MINVOLIM
> INDUSTRY
> OmWI2gQk
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
>  OJO3AgP
> GLB
> TOP3O00 
> 10
> REVERSION_AND_MC
> 2rkLkpVW
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> IND
> OJYZYOV
> USA
> TOP3000
> SECTOR
> 3v1gVle
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR
> OL53m3p 
> EUR
> TOP2500
> SUBINDUSTR
> 58XG3NJo
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> JPN
> 0LgKQ7q
> GLB
> TOP3000
> SUBINDUSTA
> GQSZrRE
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> OUzrgk 
> USA
> TOP3O00 
> STATISTICA
> GXmeKNYp
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> USA
> Om352Irr
> USA
> ILLIQUID_MINVOLIM
> STATISTICA
> GXOKW3k5
> SUPER
> 顾问 ML47973 (Rank 100)
> EQUITY
> EUR


已提交的全部alpha(包括隐藏和sa)  包括（日期已经匹配了美国夏冬令时）5个图标，总体来说就是描述随着日期 Alpha 的提交量，以及已经提交的所有 Alpha 列表，还有就是分成 ra 与 sa 的两个小图表 .

其中 Submitted Alphas (同网页端) 图表就是模仿 WorldQuantBrain  [performance]([链接已屏蔽])  做的，不过比平台多了一些查询功能 (图表太多，下面就不展示过滤功能了)，平台只显示了整体每一天总的提交量，无法区分ra 与 sa分别交了多少， 交的是哪个Region的，Grafana支持 Type 与 Region 等过滤查询 .


> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE
> SUDer
> GENIUS季度
> All
> REGION 0
> AII
> UNIVERSE
> AII
> DELAY
> AlI X
> NEUTRALIZATION
> AII X
> MAX TRADE 0
> AII X
> STATUS
> AII
> SHARPE 0
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN 0
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 0.4
> 0.2
> '025-07-02
> 2025-07-15
> 2025-07-28
> 2025-08-10
> 2025-08-23
> 2025-09-05
> 2025-09-18
> 2025-10-01
> 2025-10-14
> 2025-10-27
> 2025-11-09
> 2025-11-22
> 2025-12-05
> 2025-12-18



> [!NOTE] [图片 OCR 识别内容]
> AlphalD
> 输入数值
> TYPE 0
> AII X
> GENIUS季度
> All
> REGION
> HKG
> UNIVERSE
> AlI X
> DELAY 0
> AII X
> NEUTRALIZATION
> AII X
> MAX TRADE
> AII X
> STATUS
> AII X
> SHARPE
> 输入数值
> FITNESS
> 输入数值
> RETURNS
> 输入数值
> MARGIN
> 输入数值
> 理论与可投资术语
> panel)
> 已提交的全部alpha(包括隐藏和sa)
> Submitted Alphas (同网页端)
> 2.5
> 0.5
> 2025-10-13
> 2025-10-17
> 2025-10-21
> 2025-10-25
> 2025-10-29
> 2025-11-02
> 2025-11-06
> 2025-11-10
> 2025-11-14
> 2025-11-18
> 2025-11-22
> 2025-11-26
> 2025-11-30
> 2025-12


[图片 (图片已丢失)]

GroupBy 分组 Row 就是将 Alpha 按照 Region / Neutralization / Universe / Delay / Decay 分组，可以查看 Alpha 大体主要是交在了哪些 Region / Neutralization 等 .


> [!NOTE] [图片 OCR 识别内容]
> GroupBy 分组
> Region
> Decay (count > 5)
> 350
> 250
> 300
> 200
> 250
> 200
> 150
> 150
> 100
> 100
> 50
> 50
> USA
> EUR
> ASI
> GLB
> KOR
> JPN
> CHN
> AMR
> HKG
> TNN
> IND
> 10
> 16
> 20
> 30
> 40
> 60
> 100
> 200
> 512
> Universe
> Neutralization
> 300
> 300
> 250
> 200
> 200
> 150
> 100
> 100
> 50
> Type
> Delay
> regularalpha
> ra
> atom
> Ppa
> 无延迟
> superalpha
> 有延迟
> 128
> 256
> 512
> 1.02
> 512
> MINVOLIM
> TOP1OOO
> TOP1200
> TOP16OO
> TOP2OOOU
> TOP2500
> TOP3000
> 400
> TOPSOO
> TOP8OO
> MINVOLIM
> TOPGOO
> RAM
> Statistical
> Factors
> Factors
> Factors
> Market
> Sector
> Industry
>  Subindustry
> Factors
> None
> TOPC
> Fast
> Fast 
> Crowding
> Slow
> ILLIQUID_
> SIOW


从上面图表中，我能够很清楚的知道，主要交的 Alpaha 在 USA / TOP3000 / Subindustry / decay = 4，这个也正是符合最开始做 WorldQuant 时，国区老师们交我们 setting 的参数 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Ts_Mean 时序均值
> 日度因子指标均值
> 140%
> 400 %oo
> 120%
> 100%
> 300 %00
> 80%
> 200 %oo
> 60%
> 40%
> 100 %oo
> 20%
> 0%
> 9o00
> 02/14
> 03/13
> 04/07
> 05/02
> 05/27
> 06/21
> 07117
> 08/12
> 9/06
> 10/01
> 10/26
> 11/20
> 12/15
> sharpe
> fitness
> turnoVer
> drawdown
> 「eturns
> margin
> 月度因子指标均值
> Name
> Max
> Mean
> 25%
> 50 %00
> sharpe
> 2.15
> 1.72
> fitness
> 1.82
> 1.50
> 20%
> 50 %oo
> turnoVer
> 0.223
> 0.157
> 1.5
> 40 %ooo
> drawdown
> 24.7%
> 12.5%
> 159
> returns
> 20.1%
> 13.8%
> 30 %oo
> margin
> (右侧Y轴)
> 61.9 %00
> 41.4 %00
> 109
> 20 %oo
> 0.5
> 5%
> 10 %oo
> 9o00
> 2025-02
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
> 2026-01
> 月度因子指标均值
> 2.2
> 25%
> GO %ooo
> 20%
> 50 %ooo
> 1.8
> 40 Vooo
> 16
> 15 %
> 30 %oo
> 10%
> 20 %oo
> 02/14
> 03/01
> 03/16
> 03/31
> 04/15
> 04/30
> 05/15
> 05/30
> 06/14
> 06/29
> 07/14
> 07/29
> 08/13
> 08/28
> 09/12
> 09/27
> 10/12
> 10/27
> 11/11
> 11/26
> 12111
> 12/26
> sharpe
> fitness
> turnoVer
> drawdown
> 「eturns
> margin
> 季度因子指标均值
> 50 %00
> Name
> Max
> Mean
> 20%
> 1.75
> sharpe
> 1.86
> 1.68
> 50 %oo
> 1.5
> ftness
> 1.70
> 1.48
> 159
> tUrnOVeT
> 20.6%
> 15.9%
> 1.25
> 40 %oo
> drawdown
> 16.4%
> 12.9%
> 30 %oo
> 「etUrns
> 16.1%
> 14.0%
> 109
> 0.75
> margin
> (右侧Y轴)
> 57.9 %oo
> 40.6 %00
> 20 %0o
> 0.5
> 59
> 10 %0o
> 0.25
> 9000
> 2025-01
> 2025-02
> 2025-03
> 2025-04
> 2026-01
> 年度因子指标均值
> 1.75
> Name
> Max
> Mean
> 15%
> 35 %oo
> Sharpe
> 1.71
> 1.55
> 1.5
> 30 %oo
> fitness
> 1.47
> 1.37
> 12.5%
> 1.25
> tUTIOVeT
> 15.7%
> 14.4%
> 25 %00
> 10%
> drawdown
> 16.4%
> 14.8%
> 20 %oo
> 「EtUrns
> 13.5%
> 13.4%
> 7.5%
> 0.75
> IIIUIIIL
> 15 %00
> margin
> (右侧Y轴)
> 38.0 %oo
> 33.5 %00
> 5%
> 0.5
> 10 %0
> 2.5%
> 0.25
> 5 %ooa
> 0%
> Vooo
> 2025年
> 2026年


Ts_Mean 时序均值 Row 记录了 Alpha 主要指标的均值，包括 sharpe、fitness、turnover 和 margin， 以此来分析 vf 可能和哪些数据有关，或者与哪些数据的组合有关 (这块是我想要做的)，你想要单独比较某列数据，你就
 
> [!NOTE] [图片 OCR 识别内容]
> 月度因子指标均值
> 51.9 93
> Name
> Max
> Mean
> 50 %0o
> sharpe
> 2.15
> 1.72
> 55.2 %
> 52.1
> fitness
> 1.82
> 1.50
> 48.2 %ooo
> 50 %000
> 45.7 %oco
> tUrnoVer
> 0.223
> 0.157
> 40 %ooo
> grawdown
> 24.7%
> 12.5%
> 35.9 %
> 35.8 %
> returns
> 20.1%
> 13.8%
> 29.1 %ooo
> 30 %oo
> 26.7 Socs
> margin
> (右侧Y轴)
> 61.9 %oo
> 41.4 %0
> 22.0 %co
> 22.2 %ooo
> 20 %0o
> 10 %ooo
> 9o00
> 2025-02
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
> 2026-01


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 潜在可能影响情况
> 季度型滑动窗口因子指标均值
> 5O %ooo
> Name
> Max
> Mean
> 17.5%
> 1.75
> sharpe
> 1.86
> 1.72
> 50 %oo
> 15%
> 1.5
> fitness
> 1.74
> 1.52
> turnoVer
> 18.1%
> 16.0%
> 12.5%
> 1.25
> 40 %ooo
> drawdown
> 16.5%
> 12.7%
> 10%
> 30 %oo
> returns
> 16.8%
> 14.4%
> 7.5%
> 0.75
> margln
> (右侧〈轴〉
> 57.3 %00
> 44.2 %0
> 20 %oo
> 5%
> 0.5
> 10 %oo
> 2.5%
> 0.25
> 0oo
> %oo
> 2025-020304
> 2025-030405
> 2025-040506
> 2025-050607
> 2025-060708
> 2025-070809
> 2025-080910
> 2025-091011
> 2025-101112
> 普通
> 有条件
> 正式顾问指标均值
> 209
> 000
> Name
> Max
> Mean
> G00
> 1.75
> 17.59
> alpha因子数量
> 588
> 263
> 50 %oo
> 500
> sharpe
> 1.82
> 1.76
> 1.5
> 15%
> fitness
> 1.67
> 1.58
> 40 %oo
> 1.25 400
> 12.590
> turnOVeT
> (右侧Y轴)
> 18.6%
> 16.5%
> 10%
> 30 %oo
> drawdown
> 13.8%
> 11.9%
> 300
> returns
> 15.9%
> 14.8%
> 0.75
> 7.5%
> 20
> 200
> margin
> (右侧Y轴)
> 57.1 %oo
> 47.7 %00
> 0.5
> 5%
> sharpe_std
> 0.944
> 0.585
> 100
> 10 %00
> 0.25
> 2.59
> returns_std
> 11.1%
> 9.61%
> 0%
> 9000
> 通顾问
> 有条件顾问
> 正式顾问
> 正式研究顾问前后指标均值
> Name
> Max
> Mean
> 1.75
> G00
> 15%
> 50 %0
> alpha因子数量
> 588
> 395
> 1.5
> 500
> sharpe
> 1.78
> 1.73
> 12.5%
> 7.25
> 40 %ooo
> ftness
> 1.66
> 1.53
> 400
> 109
> tUrnOVeT
> (右则Y轴)
> 16.5%
> 15.9%
> 30 %0
> drawdown
> 13.8%
> 12.5%
> 300
> 7.5%
> 0.75
> returns
> 15.8%
> 14.3%
> 20 %oo
> 200
> 59
> margin
> (右侧Y轴)
> 54.9 %0o
> 43.5 %00
> 05
> 0.25
> 100
> 2.5%
> 10 %0
> 00o
> Vooo
> 成为顾问前
> 成为顾问后


Value Factor 潜在可能影响情况 Row 记录了 vf 可能会被什么数据影响，以及 vf 是按照 季度型滑动，所以我记录了 2025-040506， 2025-070809 这样的均值数据 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> Osmosis Competition 2025 All Alpha
> id 9
> regular_code ?
> osmosis_points ?
> region ?
> universe ?
> neutralization
> OXNXEI2
> if_else(pvl3_reve
> al >=0,1,21
> if_e
> 2000
> USA
> TOP3000
> SUBINDUSTRY
> QNRTLqQ
> std_dev(mdl77
> tOr_as
> 2000
> USA
> TOP3000
> SUBINDUSTRY
> 1YQIAjvz
> jump_decay(pv87_ivy_opr
> Ivcallmputs3, 60, sensiti
> 0.1)
> 2000
> USA
> TOP3O00
> REVERSION_AND_MC
> 2AmOQYZ
> ts_sum(lanl4_
> gric_low)
> 31l4_[OLa
> 951
> group
> lensify(close 2000
> USA
> TOP3000
> SUBINDUSTRY
> REORbA1
> Win
> backfill(implied_volatility_call 180
> 10,2), std
> 9),C2000
> USA
> TOP3O00
> SUBINDUSTRY
> SEGaPpk
> grOUP
> rallze
> tincome_
> T,densify 2000
> USA
> TOP3000
> SUBINDUSTRY
> SGZrgIN
> sentiment
> delay
> 21,20); Vhat
> ression(volume sentimE 2000
> USA
> TOP3O00
> SUBINDUSTRY
> GGKISVE
> ts_sumlpowerlpower(zsco
> delay(powe
> DS「
> 0000
> USA
> TOP3000
> SECTOR
> 7LVLKKZ
> ts_sum((anl4_gric_hi
> 9014
> anl4_tot
> Iow  78)
> 000
> USA
> TOP3000
> SUBINDUSTRY
> group by Region
> group_by Universe
> alpha_count
> 175K
> alpha_count
> 100K
> total_points
> total_
> points
> 150K
> avg_points
> avg_points
> 80K
> 125K
> 60 K
> 1O0K
> 75 K
> 40K
> 50K
> 20K
> 25K
> USA
> GLB
> EUR
> ASI
> MINVOLIM
> TOP3000
> TOP2500
> ILLIQUID_MINVOLIN
> group_by Neutralization
> group_by Decay
> 150k
> alpha
> CoUnt
> 120K
> gecay
> total_points
> alpha_count
> 125K
> 100K
> avg_points
> total_points
> 100K
> avg_points
> 80K
> 75 K
> 60 k
> 50K
> 40k
> 25k
> 20k
> 2K 2K 2K 2K 2K 2K 2K 2K 2K
> 2K10K10K 2K 2K 2K 2K 2K 2K 2K 2K
> gric
> FAST
> INDUSTRY
> FAST
> SUBINDUSTRY
> MARKET
> SECTOR
> MOMENTUM
> CROWDING
> STATISTICAL
> SLOW_AND
> REVERSION_AND


Osmosis Competition 2025 Row 记录了  Osmosis 比赛 被选中的 Alpha，以及 Alpha 被分配了多少分，以及按照某些字段分组图标.
 
> [!NOTE] [图片 OCR 识别内容]
> https:/Iplatform worldquantbrain.com/competition/0C2025
> 出 AI 众
> { |众
> WORL
> 鬯"
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> { Competitions (5)
> Community
> @ $ & 三
> This competition starts on December 15th, 2025 at 1:00:00 PM CST and ends on January Sth, 2026 at 12:59:59 PM CST。 
> Osmosis Competition
> Score
> Leaderboard
> Guidelines
> FAQ
> OSMOSIs
> 2025
> 2025-26
> Aggregate by:
> University
> Country
> Region
> Filter
> Rank
> User
> Total
> Combo IR
> Alphas
> Points
> Daily
> Combo IR
> Alphas
> Points
> Daily
> Combo IR
> Alphas
> Scoreas
> Rank
> USA
> Allocated
> PNL USA
> Rank
> GLB
> Allocated
> PNL GLB
> Rank
> EUR
> on Dec
> USA
> USA
> GLB
> GLB
> EUR
> 29th
> 顾问 ML47973 (Rank 100) (Me)
> 63,183
> 98,529
> 50
> 100,000
> 68,392
> 99,529
> 10
> 100,000
> 61,655
> 51,805
> DA98440
> 78,562
> 82,353
> 100,000
> 19,767
> 37,562
> 100,000
> 34,785
> 85,740
> 儿71699
> 77,823
> 97,059
> 100,000
> -14,867
> 93,321
> 100,000
> -31,197
> 76,895
> X42289
> 76,265
> 64,706
> 100,000
> 29,421
> 97,959
> 100,000
> 10,707
> 78,339
> AM112075
> 75,547
> 93,934
> 26
> 100,000
> 48,545
> 89,425
> 100,000
> -38,506
> 74,368
> Y815978
> 74,474
> 99,265
> 25
> 100,000
> -15,368
> 53,432
> 100,000
> -4,331
> 99,278
> 0X52484
> 73,278
> 88,971
> 20
> 100,000
> 17,561
> 82,746
> 20
> 100,000
> 8,101
> 72,744
> User


USA 分配了50个 Alpha, GLB分配了10个 Alpha，都是均分 .  从结果上来看，USA 和 GLB 的 Combo IR Rank 都还不错 .

## **四、**  **智源勘探 (Intellisource Prospecting)**

Grafana - WorldQuant 项目我还想要补全，但是还未完成的 :

1. 为了方便同时查看所有 Alpha 的 PnL 数据，可以使用 Grafana 的 JSON API 插件，通过登录 WorldQuant Brain 账号直接接入数据 . 只要在插件中配置好 PnL 接口（例如： `[链接已屏蔽] ），并利用  `alpha_id`  变量，理论上就能在同一个面板中动态展示不同 Alpha 的 PnL . 但我对 API 返回的数据格式不太熟悉，不确定在 Grafana 中具体应该如何配置查询和字段映射 . 如果有类似的经验或成功配置过，欢迎在评论区分享，非常感谢！

2. Value_Factor (vf) 这个数据，大家都比较关心，在排除他人影响的情况下，想要通过自己的 sharpe、fitness、 returns 和 margin 等数据构建某种线性 | 非线性函数，拟合自己的 vf，得到一个大致接近有预测自己下一次的 函数 .

3. 补全 Alpha Quant 板块的 理论与可投资术语 Row，使用 轻量级标记语言 Markdown 丰富，可以写记录 一些公式 比如：sharpeRatio = (Rp - Rf) / σp ，Equal Weight PnL、Combo PnL、Investability Constrained PnL 和 Risk Neutralized PnL曲线图表，记录它们之间的关系，比如，当 Max Trade = OFF 时，Combo PnL 与 Investability Constrained PnL 走势背驰意味着什么 等等，方便大家记录和学习 .

## **五、**  **Grafana Visualization JSON 共享**

当下载好 Grafana 后， 接上篇下载数据进数据库并导入评论区 Grafana JSON 数据，便可以多维度查看和分析自己的 Alpha 啦 .

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
这个可视化厉害了，感谢分享。

早就听说了Grafana做可视化大屏厉害，一直没有动手，现在跟着大佬都教程可以做起来了。

------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------------------


---

### 技术对话片段 27 (原帖: self corr计算的代码优化)
- **原帖链接**: [Commented] self corr计算的代码优化.md
- **时间**: 1年前

**提问/主帖背景 (SD17531)**:
感恩大佬发布了准确计算self corr的代码

经过长时间的使用, 对于自己经常需要用的功能,我也补充了一些进入到代码里面, 分享给各位朋友参考.

1.优化打印逻辑, 原先的代码里面会打印出多个corr来,实际上我更关心的是最大的corr数值,所以修改了.

2.除了最大的corr,实际上我还关心最小的corr,因为在实际情况中,有时候我们需要一下reverse,把原先的负数sharpe变为正数,所以我会看一下sharpe为负数时,最小的corr数值是多少.

参考实现如下:

```
def calc_self_corr(    alpha_id: str,    os_alpha_rets: pd.DataFrame | None = None,    os_alpha_ids: dict[str, str] | None = None,    alpha_result: dict | None = None,    return_alpha_pnls: bool = False,    alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    # 找到相关性序列    correlation_series = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4)    # 获取最大的相关性数值    max_correlation = correlation_series.iloc[0]    min_correlation = correlation_series.iloc[-1]    # 打印最大的相关性数值    print('max_correlation: '+ str(max_correlation))    print('min_correlation: '+ str(min_correlation))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corr
```

3.因为每次交完alpha以后,原先计算过self corr的需要进行更新,每次才能跟服务器下载PNL会花很多时间,所以我把PNL数据直接存储本地了.实现代码如下:

```
def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    df = df[['Date', alpha_id]]    return dfdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """带数据库缓存的PNL获取函数"""    # 先尝试从数据库获取    db_data = get_pnl_from_db(alpha_id)    if db_data:        pnl_dict = json.loads(db_data["pnl_data"])        df = pd.DataFrame(pnl_dict['records'],                         columns=[item['name'] for item in pnl_dict['schema']['properties']])    else:        # 从API获取        pnl = wait_get(f"[链接已屏蔽]).json()        # 存储到数据库        region = wait_get(f"[链接已屏蔽]).json()['settings']['region']        if not save_pnl_to_db(alpha_id, region, pnl):            logging.warning(f"Failed to save PNL data for {alpha_id} to DB")               df = pd.DataFrame(pnl['records'],                         columns=[item['name'] for item in pnl['schema']['properties']])       df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    return df[['Date', alpha_id]]def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """带数据库缓存的PNL获取函数"""    # 先尝试从数据库获取    if check_alpha_exists(alpha_id):        conn = get_db_conn()        try:            with conn.cursor() as cursor:                sql = "SELECT pnl_data FROM alpha_pnl WHERE alpha_id = %s"                cursor.execute(sql, (alpha_id,))                result = cursor.fetchone()                pnl = json.loads(result['pnl_data'])        finally:            conn.close()    else:        # 从API获取并保存到数据库        pnl = wait_get(f"[链接已屏蔽]).json()        region = wait_get(f"[链接已屏蔽]).json()['settings']['region']        save_alpha_pnl(alpha_id, pnl, region)       # 保持原有处理逻辑不变    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    return df[['Date', alpha_id]]
```

4.因为我的alpha数据也是直接存在了本地服务器,所以在打印alpha的时候,我希望能够直观地打印出alpha的表达式和sharpe,fitness等数据,针对自己的数据库数据格式,采用了打印的方式,部分代码如下:

```
def print_dict_info(data):    print("exp:")    print(data['exp'])    headers = [        'sharpe',        'fitness',        'returns',        'margin',        'turnover',        'drawdown',        'longCount',        'shortCount',        'first_datafield'    ]    values = [        data['sharpe'],        data['fitness'],        f"{data['returns'] * 100:.2f}%",        f"{data['margin'] * 10000:.2f}‱",        f"{data['turnover'] * 100:.2f}%",        f"{data['drawdown'] * 100:.2f}%",        data['longCount'],        data['shortCount'],        data['first_datafield']    ]    row = " | ".join([f"{header}: {value}" for header, value in zip(headers, values)])    print(row)
```

大概的打印内容如下:

```
Fetching alphas from offset 0 to 30新下载的alpha数量: 0, 目前总共alpha数量: 359max_correlation: 0.1373min_correlation: -0.047536e****** self_corr: 0.13729466200741886exp:#ASI_1******s1;process1 = ts_z*****************4), 22);sharpe: 5.18 | fitness: 2.61 | returns: 12.40% | margin: 5.08‱ | turnover: 48.84% | drawdown: 2.04% | longCount: 1611 | shortCount: 1616 | first_datafield: None
```

5.这部分满足相关性要求的alphaid,如果数量很多的话,我会单独打印出来,然后使用navicat进行查看.

6.有时候下载的数据量是巨大的,那么中断的情况不在少数,jupyter里面打印会有问题,导致打印界面中断.所以我在确保代码稳定运行的情况下,直接忽略了报错,使用以下代码:

```
import warningswarnings.filterwarnings('ignore')
```

7.其实还有很多可以优化的地方,比如可以直接根据alpha的sharpe大于还是小于0,来判断符合corr标准的alpha.当sharpe小于0 时,需要获取的是最小corr,而不是最大corr.但是太懒了,就没有怎么写这些新的逻辑实现.

希望以上思路能够给大家提供一点点帮助.

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，也感谢华子哥打好的基础，顾问必备的好工具。

在Pnl查询和比对的时候，可以增加一个统计pnl为0，或者去重的检查，可以在一定程度上检查出厂字的alpha。

-------------------------------------------

不混信号是需要有自制力的。

--------------------------------------------


---

### 技术对话片段 28 (原帖: self corr计算的代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] self corr计算的代码优化_32893337921943.md
- **时间**: 1年前

**提问/主帖背景 (SD17531)**:
感恩大佬发布了准确计算self corr的代码

经过长时间的使用, 对于自己经常需要用的功能,我也补充了一些进入到代码里面, 分享给各位朋友参考.

1.优化打印逻辑, 原先的代码里面会打印出多个corr来,实际上我更关心的是最大的corr数值,所以修改了.

2.除了最大的corr,实际上我还关心最小的corr,因为在实际情况中,有时候我们需要一下reverse,把原先的负数sharpe变为正数,所以我会看一下sharpe为负数时,最小的corr数值是多少.

参考实现如下:

```
def calc_self_corr(    alpha_id: str,    os_alpha_rets: pd.DataFrame | None = None,    os_alpha_ids: dict[str, str] | None = None,    alpha_result: dict | None = None,    return_alpha_pnls: bool = False,    alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    # 找到相关性序列    correlation_series = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4)    # 获取最大的相关性数值    max_correlation = correlation_series.iloc[0]    min_correlation = correlation_series.iloc[-1]    # 打印最大的相关性数值    print('max_correlation: '+ str(max_correlation))    print('min_correlation: '+ str(min_correlation))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corr
```

3.因为每次交完alpha以后,原先计算过self corr的需要进行更新,每次才能跟服务器下载PNL会花很多时间,所以我把PNL数据直接存储本地了.实现代码如下:

```
def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    df = df[['Date', alpha_id]]    return dfdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """带数据库缓存的PNL获取函数"""    # 先尝试从数据库获取    db_data = get_pnl_from_db(alpha_id)    if db_data:        pnl_dict = json.loads(db_data["pnl_data"])        df = pd.DataFrame(pnl_dict['records'],                         columns=[item['name'] for item in pnl_dict['schema']['properties']])    else:        # 从API获取        pnl = wait_get(f"[链接已屏蔽]).json()        # 存储到数据库        region = wait_get(f"[链接已屏蔽]).json()['settings']['region']        if not save_pnl_to_db(alpha_id, region, pnl):            logging.warning(f"Failed to save PNL data for {alpha_id} to DB")               df = pd.DataFrame(pnl['records'],                         columns=[item['name'] for item in pnl['schema']['properties']])       df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    return df[['Date', alpha_id]]def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """带数据库缓存的PNL获取函数"""    # 先尝试从数据库获取    if check_alpha_exists(alpha_id):        conn = get_db_conn()        try:            with conn.cursor() as cursor:                sql = "SELECT pnl_data FROM alpha_pnl WHERE alpha_id = %s"                cursor.execute(sql, (alpha_id,))                result = cursor.fetchone()                pnl = json.loads(result['pnl_data'])        finally:            conn.close()    else:        # 从API获取并保存到数据库        pnl = wait_get(f"[链接已屏蔽]).json()        region = wait_get(f"[链接已屏蔽]).json()['settings']['region']        save_alpha_pnl(alpha_id, pnl, region)       # 保持原有处理逻辑不变    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    return df[['Date', alpha_id]]
```

4.因为我的alpha数据也是直接存在了本地服务器,所以在打印alpha的时候,我希望能够直观地打印出alpha的表达式和sharpe,fitness等数据,针对自己的数据库数据格式,采用了打印的方式,部分代码如下:

```
def print_dict_info(data):    print("exp:")    print(data['exp'])    headers = [        'sharpe',        'fitness',        'returns',        'margin',        'turnover',        'drawdown',        'longCount',        'shortCount',        'first_datafield'    ]    values = [        data['sharpe'],        data['fitness'],        f"{data['returns'] * 100:.2f}%",        f"{data['margin'] * 10000:.2f}‱",        f"{data['turnover'] * 100:.2f}%",        f"{data['drawdown'] * 100:.2f}%",        data['longCount'],        data['shortCount'],        data['first_datafield']    ]    row = " | ".join([f"{header}: {value}" for header, value in zip(headers, values)])    print(row)
```

大概的打印内容如下:

```
Fetching alphas from offset 0 to 30新下载的alpha数量: 0, 目前总共alpha数量: 359max_correlation: 0.1373min_correlation: -0.047536e****** self_corr: 0.13729466200741886exp:#ASI_1******s1;process1 = ts_z*****************4), 22);sharpe: 5.18 | fitness: 2.61 | returns: 12.40% | margin: 5.08‱ | turnover: 48.84% | drawdown: 2.04% | longCount: 1611 | shortCount: 1616 | first_datafield: None
```

5.这部分满足相关性要求的alphaid,如果数量很多的话,我会单独打印出来,然后使用navicat进行查看.

6.有时候下载的数据量是巨大的,那么中断的情况不在少数,jupyter里面打印会有问题,导致打印界面中断.所以我在确保代码稳定运行的情况下,直接忽略了报错,使用以下代码:

```
import warningswarnings.filterwarnings('ignore')
```

7.其实还有很多可以优化的地方,比如可以直接根据alpha的sharpe大于还是小于0,来判断符合corr标准的alpha.当sharpe小于0 时,需要获取的是最小corr,而不是最大corr.但是太懒了,就没有怎么写这些新的逻辑实现.

希望以上思路能够给大家提供一点点帮助.

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，也感谢华子哥打好的基础，顾问必备的好工具。

在Pnl查询和比对的时候，可以增加一个统计pnl为0，或者去重的检查，可以在一定程度上检查出厂字的alpha。

-------------------------------------------

不混信号是需要有自制力的。

--------------------------------------------


---

### 技术对话片段 29 (原帖: 基于模版的Alpha生成相似字段Alpha工作流这是一个通用工作流，旨在通过替换现有Alpha表达式中的特定组件（如数据字段）来系统地、批量地生成新的Alpha变体。这种方法适用于快速探索相似因子的表现，并扩大有效的Alpha策略池。#核心思想该工作流的核心是“模板化”和“替换”。我们从一个表现良好或结构有趣的“种子Alpha”开始，将其视为一个模板。然后，我们识别出该模板中的某个关键部分（通常是一个数据字段），并找到一系列与之相似或相关的替代项，最后通过批量替换生成大量新的候选Alpha。#工作流步骤##1. 选择种子Alpha (Seed Alpha)选择一个作为起点的Alpha表达式。这个表达式可以来源于：- 你自己过去研究中发现的高绩效Alpha。- 一个具有特定逻辑结构（例如，时间序列操作、截面操作组合）的Alpha。- 一个你希望探索其变体的基础因子。**示例种子Alpha**：```-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))```在这个例子中，我们选择了一个基于`anl44_2_grossmargin_lastactccy`（毛利率）字段最后变动天数的表达式。##2. 识别可变组件确定你想要替换的表达式部分。最常见的是数据字段，但也可以是算子或参数。**示例可变组件**：在 `-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))` 中，可变组件是数据字段 `anl44_2_grossmargin_lastactccy`。##3. 发现相似组件寻找与上一步中识别出的可变组件相似或相关的替代项。这是提升Alpha生成质量的关键步骤。- **对于数据字段**：1.**筛选同一数据集 (Primary Filter)**：首先，将范围缩小到与原字段相同的数​​据集。例如，如果原字段来自 `anl44`，则优先探索该数据集下的其他字段。这可以作为初步筛选，因为同一数据集的字段通常在逻辑上是相关的。2.**分析语义相似性 (Key Step)**：在第一步筛选出的字段中，进一步通过分析其**描述（description）**来判断语义相似性。这是最重要的一步。寻找衡量相似经济或金融概念的字段。-**示例**：如果你的种子Alpha使用了一个关于“毛利率”（Gross Margin）的字段，那么在寻找替代项时，应优先选择描述中同样涉及**盈利能力**的字段，例如：-`EBITDA` (税息折旧及摊销前利润)-`Net Profit` (净利润)-`EPS` (每股收益)-`ROE` (股本回报率)- 通过这种方式，你可以确保新生成的Alpha在逻辑上与种子Alpha保持一致，而不仅仅是字段名称或来源相似。3.**考虑名称相似性 (Optional)**：在某些情况下，名称相似的字段也可能相关，但这通常不如基于描述的语义分析可靠。**发现工具与数据来源**：- **本地文件**：数据字段存储在本地的 `data/fields` 目录下的 CSV 文件中。你需要读取相关文件并解析其内容，特别是包含字段名称和描述的列，以寻找相似组件。不应使用 API 来获取字段。**示例相似组件**：假设我们发现 `anl44` 数据集中，除了关于 `grossmargin` 的字段，还有以下同样衡量盈利能力的字段：- `anl44_2_ebitdaps_value` (描述: ebitdaps value)- `anl44_2_epsr_value` (描述: epsr value)- `anl44_2_netprofit_rep_value` (描述: netprofit rep value)- `anl44_2_roe_value` (描述: roe value)- ...等等##4. 生成新表达式以编程方式，将种子Alpha模板中的可变组件替换为你在上一步中找到的相似组件列表，从而生成一系列新的Alpha表达式。**示例生成结果**：生成的表达式应直接在对话中以 Python 列表的格式返回，方便用户直接复制使用。```pythonexpressions = ["ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_qty),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_qty),120), 5)"]```##5. 评估与迭代 (可选但推荐)对生成的新Alpha表达式进行性能评估。- **批量回测**：使用 `create_multiSim` 工具可以一次性回测多个表达式，高效地获取它们的性能指标。- **分析结果**：分析回测报告，筛选出表现优异的Alpha。- **迭代优化**：基于评估结果，可以重复此工作流，例如选择一个新的种子Alpha，或探索另一组相似组件。#总结这个工作流提供了一种半自动化的方法，能够基于已有的知识和发现，快速、大规模地生成新的、有潜力的Alpha。它将研究员的洞察力（选择种子和相似组件）与机器的执行力（批量生成和回测）有效结合起来。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [MCP] 基于相似字段产生alpha的工作流分享_35797714275223.md
- **时间**: 22天前

**提问/主帖背景 (JX79797)**:
使用的工具链参考：  [[L2] [分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md]([L2] [分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)

**本工作流基于相似字段寻找更多的alpha**

**1. 可以用于ai alpha比赛产生子alpha**

**2. 可以用于 ASI 通过Robust测试**

**工作流程：**

1. 选择一个“种子Alpha”: 从一个已知表现良好或结构有趣的Alpha表达式开始，把它当作一个模板。

2. 识别并替换关键部分:

确定该Alpha中的一个关键组成部分（通常是一个数据字段），例如一个关于“毛利率”的字段。

3. 发现相似字段: 寻找与该关键字段在语义上相似的替代字段。工作流强调，关键在于分析字段的描

述来寻找衡量相似经济概念的替代品（例如，用另一个盈利能力指标如“净利润”或“EBITDA”来替换“

毛利率”），而不仅仅是看字段名称。

4. 批量生成:

用找到的相似字段列表，批量替换模板中的原始字段，从而快速生成大量逻辑一致的新Alpha变体

**使用提示：**

```
Instrument Type: Equity, Region: ASI, Universe: MINVOL1M, Delay: 1 下的alpha "ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactsell_amt),120), 5)", 使用工作流similar_field_alpha_generation_workflow.md 生成 20 个新的表达式
```

上文示例中的alpha，Robust失败无法提交

- **Robust universe Sharpe of 1.13 is below cutoff of 1.46 (90% of Alpha).**

使用工作流得到新的20个表达式，执行回测，得到2个可提交alpha

**工作流内容**

```
# 基于模版的Alpha生成相似字段Alpha工作流这是一个通用工作流，旨在通过替换现有Alpha表达式中的特定组件（如数据字段）来系统地、批量地生成新的Alpha变体。这种方法适用于快速探索相似因子的表现，并扩大有效的Alpha策略池。## 核心思想该工作流的核心是“模板化”和“替换”。我们从一个表现良好或结构有趣的“种子Alpha”开始，将其视为一个模板。然后，我们识别出该模板中的某个关键部分（通常是一个数据字段），并找到一系列与之相似或相关的替代项，最后通过批量替换生成大量新的候选Alpha。## 工作流步骤### 1. 选择种子Alpha (Seed Alpha)选择一个作为起点的Alpha表达式。这个表达式可以来源于：- 你自己过去研究中发现的高绩效Alpha。- 一个具有特定逻辑结构（例如，时间序列操作、截面操作组合）的Alpha。- 一个你希望探索其变体的基础因子。**示例种子Alpha**：```-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))```在这个例子中，我们选择了一个基于`anl44_2_grossmargin_lastactccy`（毛利率）字段最后变动天数的表达式。### 2. 识别可变组件确定你想要替换的表达式部分。最常见的是数据字段，但也可以是算子或参数。**示例可变组件**：在 `-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))` 中，可变组件是数据字段 `anl44_2_grossmargin_lastactccy`。### 3. 发现相似组件寻找与上一步中识别出的可变组件相似或相关的替代项。这是提升Alpha生成质量的关键步骤。- **对于数据字段**：1.**筛选同一数据集 (Primary Filter)**：首先，将范围缩小到与原字段相同的数​​据集。例如，如果原字段来自 `anl44`，则优先探索该数据集下的其他字段。这可以作为初步筛选，因为同一数据集的字段通常在逻辑上是相关的。2.**分析语义相似性 (Key Step)**：在第一步筛选出的字段中，进一步通过分析其**描述（description）**来判断语义相似性。这是最重要的一步。寻找衡量相似经济或金融概念的字段。-**示例**：如果你的种子Alpha使用了一个关于“毛利率”（Gross Margin）的字段，那么在寻找替代项时，应优先选择描述中同样涉及**盈利能力**的字段，例如：-`EBITDA` (税息折旧及摊销前利润)-`Net Profit` (净利润)-`EPS` (每股收益)-`ROE` (股本回报率)- 通过这种方式，你可以确保新生成的Alpha在逻辑上与种子Alpha保持一致，而不仅仅是字段名称或来源相似。3.**考虑名称相似性 (Optional)**：在某些情况下，名称相似的字段也可能相关，但这通常不如基于描述的语义分析可靠。**发现工具与数据来源**：- **本地文件**：数据字段存储在本地的 `data/fields` 目录下的 CSV 文件中。你需要读取相关文件并解析其内容，特别是包含字段名称和描述的列，以寻找相似组件。不应使用 API 来获取字段。**示例相似组件**：假设我们发现 `anl44` 数据集中，除了关于 `grossmargin` 的字段，还有以下同样衡量盈利能力的字段：- `anl44_2_ebitdaps_value` (描述: ebitdaps value)- `anl44_2_epsr_value` (描述: epsr value)- `anl44_2_netprofit_rep_value` (描述: netprofit rep value)- `anl44_2_roe_value` (描述: roe value)- ...等等### 4. 生成新表达式以编程方式，将种子Alpha模板中的可变组件替换为你在上一步中找到的相似组件列表，从而生成一系列新的Alpha表达式。**示例生成结果**：生成的表达式应直接在对话中以 Python 列表的格式返回，方便用户直接复制使用。```pythonexpressions = ["ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_qty),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_qty),120), 5)"]```### 5. 评估与迭代 (可选但推荐)对生成的新Alpha表达式进行性能评估。- **批量回测**：使用 `create_multiSim` 工具可以一次性回测多个表达式，高效地获取它们的性能指标。- **分析结果**：分析回测报告，筛选出表现优异的Alpha。- **迭代优化**：基于评估结果，可以重复此工作流，例如选择一个新的种子Alpha，或探索另一组相似组件。## 总结这个工作流提供了一种半自动化的方法，能够基于已有的知识和发现，快速、大规模地生成新的、有潜力的Alpha。它将研究员的洞察力（选择种子和相似组件）与机器的执行力（批量生成和回测）有效结合起来。
```

```

```

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢徐佬的分享，这种有直接帮助的帖子值得更多人看到。直接喂给了AI以后，下午用这个方法优化出了一个News。。。。。。这种帖子可以多发点哈！

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================


---

### 技术对话片段 30 (原帖: 5. 主流程)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Agent Memory模块探索】用Supermemory在WorldQuant平台自动化挖掘Alpha因子经验分享_39354315278103.md
- **时间**: 2个月前

**提问/主帖背景 (HA11071)**:
你是否曾在WorldQuant平台上，为了挖掘一个有效的Alpha因子而绞尽脑汁？面对海量的价量数据、财务报表和学术论文，传统的“试错法”不仅耗时耗力，更考验着研究员的经验与直觉。

现在，一个全新的思路或许能为你打开一扇门：将WorldQuant平台强大的回测能力，与GitHub上炙手可热的AI记忆引擎——Supermemory相结合，构建一个能够“记住”历史、并从中学习的自动化因子挖掘系统。

这并非要取代你的金融洞见，而是为你配备一位不知疲倦的“副驾驶”，帮你处理繁琐的重复性工作，让你能更专注于策略逻辑的顶层设计。

#### Supermemory：为AI装上“海马体”

在深入实战之前，我们先来认识一下本次的主角——Supermemory。简单来说，它是一个为AI应用设计的持久化记忆系统。你可以把它想象成AI的“海马体”，它能让AI记住你的一切：你的偏好、项目背景、历史对话中的关键信息，甚至是上传的文档内容。

它的核心优势在于：

- **自动提取与更新** ：能从对话或文档中自动抓取关键信息并存档。当新信息出现时，它能智能地覆盖或修正旧记忆，确保记忆的准确性。
- **极速检索** ：通过简单的API调用，能在50毫秒内加载完整的上下文，让AI瞬间“回忆”起相关信息。
- **多模态支持** ：不仅能处理文本，还能解析PDF、图片、代码等多种格式的数据。

在量化投资的场景中，我们可以利用Supermemory来构建一个不断进化的“因子知识库”，让AI记住哪些因子结构是有效的，哪些是无效的，从而在后续的挖掘中提供更具启发性的建议。

#### 实战演练：搭建你的AI因子挖掘助手

接下来，我们将手把手教你搭建这个系统。

**第一步：环境准备**

一个稳定、可复现的开发环境是成功的第一步。我们强烈建议使用 `conda` 来管理项目依赖。

1. **创建并激活虚拟环境** ：

```
# 创建一个名为"quant_memory"的Python 3.13环境
conda create -n quant_memory python=3.13 -y
# 激活环境
conda activate quant_memory

```

1. **安装核心依赖库** ：
   我们将需要以下几个关键的Python库：

- `requests`  /  `httpx` : 用于与WorldQuant API通信。
- `supermemory` : Supermemory的Python客户端，用于记忆管理。
- `openai`  (或其他大模型SDK): 用于调用大语言模型，生成因子代码。
- `pandas`  &  `numpy` : 数据处理和分析的基础。

通过以下命令一次性安装：

```
pip install requests supermemory openai pandas numpy

```

1. **配置API密钥** ：
   Supermemory你需要提前获取它们的API密钥。

- **Supermemory API密钥** ：在Supermemory官网注册并获取你的API Key。
- **大模型API密钥** ：以OpenAI为例，在其平台创建API Key。你也可以替换为DeepSeek、智谱AI等其他服务。

为了安全，我们将这些密钥保存在环境变量中。在项目根目录创建一个 `.env` 文件：

```
# .env 文件
SUPERMEMORY_API_KEY="你的Supermemory_API_Key"
OPENAI_API_KEY="你的OpenAI_API_Key"

```

**第二步：构建记忆驱动的因子挖掘流程**

核心思路是：让大模型在生成因子代码时，先从Supermemory中检索历史上表现优异的因子模式，然后结合这些“经验”来创造新的因子。

以下是一个简化的Python代码示例，展示了这一流程：

```
import os
from dotenv import load_dotenv
import openai
from supermemory import Supermemory
import requests

# 1. 加载环境变量
load_dotenv()
SM_API_KEY = os.getenv('SUPERMEMORY_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# 2. 初始化客户端
client = openai.OpenAI(api_key=OPENAI_API_KEY)
sm_client = Supermemory(api_key=SM_API_KEY)

# 3. 定义从Supermemory检索历史因子的函数
def get_historical_alpha_patterns():
    """从记忆中检索表现优异的Alpha因子模式"""
    # 搜索与"高夏普比率"、"低换手率"相关的因子代码
    search_results = sm_client.search(q="高夏普比率 低换手率 alpha因子代码")
    # 这里简单提取搜索结果的内容，实际应用中可以做更复杂的处理
    patterns = "\n".join([result.content for result in search_results.results])
    return patterns

# 4. 定义让大模型生成因子的函数
def generate_alpha_with_memory():
    """结合历史记忆，让大模型生成新的Alpha因子"""
    # 首先，从记忆中获取历史优秀因子的模式
    historical_patterns = get_historical_alpha_patterns()

    # 构建提示词，将历史模式作为上下文提供给大模型
    prompt = f"""
    你是一个资深的量化研究员。请基于以下历史上表现优异的Alpha因子模式，构思并生成一个新的、逻辑不同的Alpha因子。

    历史因子模式:
    {historical_patterns}

    要求:
    1. 因子逻辑清晰，具有经济学或行为金融学解释。
    2. 使用WorldQuant平台支持的表达式语法。
    3. 输出因子的完整代码和简要逻辑说明。
    """

    # 调用大模型生成因子
    response = client.chat.completions.create(
        model="gpt-4o", # 或其他你选择的模型
        messages=[{"role": "user", "content": prompt}]
    )

    new_alpha_code = response.choices[0].message.content
    return new_alpha_code

# 5. 主流程
if __name__ == "__main__":
    # 生成新的Alpha因子
    alpha_code = generate_alpha_with_memory()
    print("新生成的Alpha因子:\n", alpha_code)

    # 将新生成的因子（无论回测结果如何）作为新的记忆存入Supermemory
    # 在实际应用中，你可以在WorldQuant平台回测后，将回测结果也一并存入
    sm_client.add(content=alpha_code, source="auto_generated_alpha")
    print("新因子已存入记忆库。")

```

#### 结语

通过以上步骤，你就搭建了一个最基础的、由AI记忆驱动的因子挖掘原型。这个系统的潜力是巨大的。你可以不断地将回测结果（无论是成功的还是失败的）反馈给Supermemory，让它“学习”和“进化”。久而久之，它会成为一个只属于你的、凝聚了你所有研究智慧的量化投资大脑。

未来，我们甚至可以探索更复杂的模式，比如让多个AI智能体协作，一个负责生成，一个负责批判，一个负责从海量研报中搜寻灵感，而Supermemory则是它们共享的“知识库”。

量化投资的AI时代，才刚刚拉开序幕。希望这篇文章能为你带来一些启发，开启你的探索之旅。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
大家的新武器好多，真是跟不上，感谢分享。

之前一直思考如何把回测数据库对接上，听起来这个好像更容易一点。

没有记忆，是问题，有了记忆，上下文过长，又是问题。看看这个效果如何。

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================


---

### 技术对话片段 31 (原帖: 例如，一个可能的策略是：当餐厅评分上升且顾客流量增加时，我们认为这是一个积极的信号；而当菜品价格急剧上涨时，我们可能认为这是一个消极的信号。)
- **原帖链接**: [Commented] 【Alpha灵感】餐厅指标对我们的一些参考作用.md
- **时间**: 1年前

**提问/主帖背景 (ML42552)**:
文章链接： [[2501.03862] Rendezfood: A Design Case Study of a Conversational Location-based Approach in Restaurants]([链接已屏蔽])

# Rendezfood: A Design Case Study of a Conversational Location-based Approach in Restaurants

# 假设我们有以下“餐厅指标”作为输入（这些在真实的WorldQuant环境中需要被替换为金融数据）：
# restaurant_rating: 餐厅评分（可以视为某种“价格”指标）
# customer_flow: 顾客流量（可以视为“交易量”指标）
# menu_price_change: 菜品价格变化率（可以视为某种“动量”指标）

# 注意：以下表达式是概念性的，并不是真正的WorldQuant代码。

# 步骤1: 定义基础变量
# 这些变量将代表我们的“餐厅指标”，并需要在每个时间点进行更新。

# 步骤2: 计算策略信号
# 我们可以构建一个策略信号，该信号基于餐厅评分的变化、顾客流量的增加或减少，以及菜品价格的变化率。
# 例如，一个可能的策略是：当餐厅评分上升且顾客流量增加时，我们认为这是一个积极的信号；而当菜品价格急剧上涨时，我们可能认为这是一个消极的信号。


> [!NOTE] [图片 OCR 识别内容]
> Settings
> ASIIDIIMINVOLIM
> Convert to Multi-Sir
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> ASI
> MINVOLIN
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save a5 Default
> Apply


模板：

A=ts_corr(close, volume, 20) > 0.5;

B=group_backfill(winsorize(ts_backfill({data},5),std=4),market,22, std=4.0);

trade_when(A, B, -1)


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Marain
> 1.32
> 2.689
> 1.48
> 15.809
> 11.329
> 118.089600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 0.00
> 0.0095
> .00
> 00N
> 0.0095
> OOSoo
> 2013
> 0.00
> 0.0035
> 0.00
> 0.0095
> 0.0095
> OOSoo
> 2014
> UUU
> 3.0035
> ,00
> 0.009
> 0.00q
> OO9uoo
> 2015
> 0.00
> 0.0035
> 0.009
> 0.00q
> OO9uoo
> 2015
> 0.00
> 0.0035
> 00N
> 0.00q
> OO9uoo
> 2017
> 0.00
> 0.0035
> 0.009
> 0.00q
> OO9uoo
> 2018
> 2.14
> 5.0795
> 2.50
> 17.0595
> 7.5995
> 67.25900
> 1792
> 360
> 2019
> 0.23
> 2.3095
> 0,09
> 2.0795
> 11.3695
> -18.059300
> 1673
> 1605
> 2020
> 0.51
> 3.3235
> 141
> 38
> 12.2495
> 38.43900
> 1334
> 1507
> 2021
> 0.37
> 3.9135
> 0.16
> 2.4095
> 4.8790
> 12.25900
> 2282
> 895
> 2021
> 3.45
> 3.0235
> 5.02
> 26.5035
> 3.149
> 175.499600
> 2545
> 2065
> 2022
> 0.44
> 2.3835
> 0.32
> 6.479
> 11.329
> 54.489600
> 2319
> 2009



> [!NOTE] [图片 OCR 识别内容]
> D
> Correlation
> Self Correlation
> Maximun
> Winimum
> Last Run:
> Prod Correlation
> Maximum
> Winimum
> Last Run:
> 01/1312025,
> 12.014M
> 0.5752
> -0.4815
> 1N
> 10OK
> 寰
> 1OK
> 昱
> 8
> 100
> MoT


GLB 的表现


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Rezurns
> DrawdOwn
> Marsin
> 1.37
> 4.029
> 0.98
> 6.349
> 3.249
> 31.509600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 0.77
> 12.519
> 0.54
> -5.3135
> 7.5535
> 10.009c
> 779
> 825
> 2013
> 0.75
> 5.483
> 0.36
> -2.9535
> 1735
> 10.829500
> 1172
> 497
> 2012
> -0.60
> 4.43q
> 0.23
> 2.6395
> 4.3035
> 879500
> 1367
> 1361
> 2015
> 1.10
> 4.2796
> 0.52
> 3.9935
> 3.5335
> 18.589500
> 1267
> 1458
> 2015
> 0.56
> 4.1096
> 0.24
> 2.3895
> 2.7895
> 5090
> 1130
> 1565
> 2017
> 1.27
> 5.3696
> 0.53
> 3.0795
> 3.3835
> 5590
> 1251
> 1538
> 2018
> 1.31
> 4.50q6
> 0.92
> 5.1335
> 2.3935
> 27.25950
> 1277
> 1474
> 2019
> -2.09
> 4.583
> +59
> -8.1335
> 9.2035
> -34.759600
> 185
> 1578
> 2020
> 0.55
> 5.2496
> 0.35
> -4.9235
> 14.5735
> 18.779503
> 1325
> 1422
> 2021
> 5.95q6
> 0.44
> 3.0195
> 2.9935
> 10.
> So
> 1254
> 500
> 2021
> 0.97
> 4.243
> 0.54
> 3.8235
> 1.3135
> 13.019503
> 1263
> 1445
> 2022
> 1.65
> 3.339
> 1.36
> 3.5335
> 3.2495
> 44.509b0
> 1219
> 1445



> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximun
> Winimum
> Last Run:
> Prod Correlation
> Maximum
> Winimum
> Last Run:
> 01/13/2025,
> 12.054N
> 0.3379
> -0.4194
> TN
> 1Ok
> 鬓
> 昱
> 8
> 100
> MOT
> ~0.7.


读论文系列目前对自己来说还是有点难度，最大的难点在找到有效的论文，其次是对自己operators 的熟悉程度，这几天刚把自己所有的operators借助大语言模型学习了一番，想要创造自己的模板还是任重而道远呀

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
为什么要使用group_backfill呢？


---

### 技术对话片段 32 (原帖: 例如，一个可能的策略是：当餐厅评分上升且顾客流量增加时，我们认为这是一个积极的信号；而当菜品价格急剧上涨时，我们可能认为这是一个消极的信号。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】餐厅指标对我们的一些参考作用_29162445139991.md
- **时间**: 1年前

**提问/主帖背景 (ML42552)**:
文章链接： [[2501.03862] Rendezfood: A Design Case Study of a Conversational Location-based Approach in Restaurants]([链接已屏蔽])

# Rendezfood: A Design Case Study of a Conversational Location-based Approach in Restaurants

# 假设我们有以下“餐厅指标”作为输入（这些在真实的WorldQuant环境中需要被替换为金融数据）：
# restaurant_rating: 餐厅评分（可以视为某种“价格”指标）
# customer_flow: 顾客流量（可以视为“交易量”指标）
# menu_price_change: 菜品价格变化率（可以视为某种“动量”指标）

# 注意：以下表达式是概念性的，并不是真正的WorldQuant代码。

# 步骤1: 定义基础变量
# 这些变量将代表我们的“餐厅指标”，并需要在每个时间点进行更新。

# 步骤2: 计算策略信号
# 我们可以构建一个策略信号，该信号基于餐厅评分的变化、顾客流量的增加或减少，以及菜品价格的变化率。
# 例如，一个可能的策略是：当餐厅评分上升且顾客流量增加时，我们认为这是一个积极的信号；而当菜品价格急剧上涨时，我们可能认为这是一个消极的信号。


> [!NOTE] [图片 OCR 识别内容]
> Settings
> ASIIDIIMINVOLIM
> Convert to Multi-Sir
> LNGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> ASI
> MINVOLIN
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Market
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save a5 Default
> Apply


模板：

A=ts_corr(close, volume, 20) > 0.5;

B=group_backfill(winsorize(ts_backfill({data},5),std=4),market,22, std=4.0);

trade_when(A, B, -1)


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Marain
> 1.32
> 2.689
> 1.48
> 15.809
> 11.329
> 118.089600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 0.00
> 0.0095
> .00
> 00N
> 0.0095
> OOSoo
> 2013
> 0.00
> 0.0035
> 0.00
> 0.0095
> 0.0095
> OOSoo
> 2014
> UUU
> 3.0035
> ,00
> 0.009
> 0.00q
> OO9uoo
> 2015
> 0.00
> 0.0035
> 0.009
> 0.00q
> OO9uoo
> 2015
> 0.00
> 0.0035
> 00N
> 0.00q
> OO9uoo
> 2017
> 0.00
> 0.0035
> 0.009
> 0.00q
> OO9uoo
> 2018
> 2.14
> 5.0795
> 2.50
> 17.0595
> 7.5995
> 67.25900
> 1792
> 360
> 2019
> 0.23
> 2.3095
> 0,09
> 2.0795
> 11.3695
> -18.059300
> 1673
> 1605
> 2020
> 0.51
> 3.3235
> 141
> 38
> 12.2495
> 38.43900
> 1334
> 1507
> 2021
> 0.37
> 3.9135
> 0.16
> 2.4095
> 4.8790
> 12.25900
> 2282
> 895
> 2021
> 3.45
> 3.0235
> 5.02
> 26.5035
> 3.149
> 175.499600
> 2545
> 2065
> 2022
> 0.44
> 2.3835
> 0.32
> 6.479
> 11.329
> 54.489600
> 2319
> 2009



> [!NOTE] [图片 OCR 识别内容]
> D
> Correlation
> Self Correlation
> Maximun
> Winimum
> Last Run:
> Prod Correlation
> Maximum
> Winimum
> Last Run:
> 01/1312025,
> 12.014M
> 0.5752
> -0.4815
> 1N
> 10OK
> 寰
> 1OK
> 昱
> 8
> 100
> MoT


GLB 的表现


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Rezurns
> DrawdOwn
> Marsin
> 1.37
> 4.029
> 0.98
> 6.349
> 3.249
> 31.509600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 0.77
> 12.519
> 0.54
> -5.3135
> 7.5535
> 10.009c
> 779
> 825
> 2013
> 0.75
> 5.483
> 0.36
> -2.9535
> 1735
> 10.829500
> 1172
> 497
> 2012
> -0.60
> 4.43q
> 0.23
> 2.6395
> 4.3035
> 879500
> 1367
> 1361
> 2015
> 1.10
> 4.2796
> 0.52
> 3.9935
> 3.5335
> 18.589500
> 1267
> 1458
> 2015
> 0.56
> 4.1096
> 0.24
> 2.3895
> 2.7895
> 5090
> 1130
> 1565
> 2017
> 1.27
> 5.3696
> 0.53
> 3.0795
> 3.3835
> 5590
> 1251
> 1538
> 2018
> 1.31
> 4.50q6
> 0.92
> 5.1335
> 2.3935
> 27.25950
> 1277
> 1474
> 2019
> -2.09
> 4.583
> +59
> -8.1335
> 9.2035
> -34.759600
> 185
> 1578
> 2020
> 0.55
> 5.2496
> 0.35
> -4.9235
> 14.5735
> 18.779503
> 1325
> 1422
> 2021
> 5.95q6
> 0.44
> 3.0195
> 2.9935
> 10.
> So
> 1254
> 500
> 2021
> 0.97
> 4.243
> 0.54
> 3.8235
> 1.3135
> 13.019503
> 1263
> 1445
> 2022
> 1.65
> 3.339
> 1.36
> 3.5335
> 3.2495
> 44.509b0
> 1219
> 1445



> [!NOTE] [图片 OCR 识别内容]
> Correlation
> Self Correlation
> Maximun
> Winimum
> Last Run:
> Prod Correlation
> Maximum
> Winimum
> Last Run:
> 01/13/2025,
> 12.054N
> 0.3379
> -0.4194
> TN
> 1Ok
> 鬓
> 昱
> 8
> 100
> MOT
> ~0.7.


读论文系列目前对自己来说还是有点难度，最大的难点在找到有效的论文，其次是对自己operators 的熟悉程度，这几天刚把自己所有的operators借助大语言模型学习了一番，想要创造自己的模板还是任重而道远呀

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
为什么要使用group_backfill呢？


---

### 技术对话片段 33 (原帖: 【check王】验证表达式是否正确的脚本——七十二变黄金搭档)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【check王】验证表达式是否正确的脚本七十二变黄金搭档_36740689434391.md
- **时间**: 6 months ago

**提问/主帖背景 (AH18340)**:
使用72变或者大模型生成的alpha表达式可能有语法错误，基于PLY(Python Lex-Yacc)写了第一版用于校验表达式是否正确

使用方法

1.安装库

pip install ply

2.执行脚本(脚本名我命名为expression_validator.py)

```
python expression_validator.py
```

会提示输入json文件路径，如果你把脚本放到cnhkmcp\untracked/APP目录下，72变生成的alpha刚好放在Tranformer/output/Alpha_generated_expressions.json文件中，回车执行即可

```
请输入要校验的表达式JSON文件路径（默认：Tranformer/output/Alpha_generated_expressions.json）: 
```

执行后会生成两个文件Alpha_generated_expressions_success.json 和Alpha_generated_expressions_error.json 对应符合规则和不符合的。

由于是第一版本，目前主要校验表达式中操作符的使用，字段主要校验是不是字母数字下划线组成。有许多不完善的地方，如果有不对的测试用例欢迎在评论区补充

代码：

```
#!/usr/bin/env python3# -*- coding: utf-8 -*-"""表达式验证器 - 使用抽象语法树验证字符串表达式格式是否正确本模块实现了一个能够检测字符串表达式格式是否正确的系统，基于PLY(Python Lex-Yacc)构建词法分析器和语法分析器，识别表达式中的操作符、函数和字段，并验证其格式正确性。"""import reimport sysimport jsonimport osfrom typing import List, Dict, Any, Optional, Tuple# 尝试导入PLY库，如果不存在则提供安装提示try:    import ply.lex as lex    import ply.yacc as yaccexcept ImportError:    print("错误: 需要安装PLY库。请运行 'pip install ply' 来安装。")    sys.exit(1)# 1. 定义支持的操作符和函数supported_functions = {    # Group 类别函数    'group_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_mean': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'group_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_rank': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_vector_proj': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_normalize': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'category', 'expression', 'expression', 'expression']},    'group_extra': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_backfill': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression'], 'param_names': ['x', 'cat', 'days', 'std']},    'group_scale': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_count': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_neutralize': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_multi_regression': {'min_args': 4, 'max_args': 9, 'arg_types': ['expression'] * 9},    'group_cartesian_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['category', 'category']},    'combo_a': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},        # Transformational 类别函数    'right_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'bucket': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 第二个参数可以是string类型的range参数    'tail': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression']},    'left_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'trade_when': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'generate_stats': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},        # Cross Sectional 类别函数    'winsorize': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression'], 'param_names': ['x', 'std']},    'rank': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_proj': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'vector_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'multi_regression': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # 支持多个自变量        # Time Series 类别函数    'ts_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_mean': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delay': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_corr': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_returns': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'mode']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_backfill': {'min_args': 2, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'string']},    'days_from_last_change': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'last_diff_value': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_scale': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_entropy': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'd', 'buckets']},    'ts_step': {'min_args': 1, 'max_args': 1, 'arg_types': ['number']},    'ts_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_co_kurtosis': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'inst_tvr': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_exp_window': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'factor']},    'ts_av_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_kurtosis': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_diff': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_arg_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_cps': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_rank': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_ir': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_theilsen': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'hump_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_weighted_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_quantile': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'string']},    'ts_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_count_nans': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_covariance': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_co_skewness': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_min_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_linear': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'boolean']},    'jump_decay': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'number', 'expression', 'number', 'number'], 'param_names': ['x', 'd', 'stddev', 'sensitivity', 'force']},    'ts_moment': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'k']},    'ts_arg_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_regression': {'min_args': 3, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number'], 'param_names': ['y', 'x', 'd', 'lag', 'rettype']},    'ts_skewness': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'kth_element': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'hump': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'hump']},    'ts_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delta': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_poly_regression': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'number', 'number']},    'ts_target_tvr_decay': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number'], 'param_names': ['x', 'lambda_min', 'lambda_max', 'target_tvr']},    'ts_target_tvr_delta_limit': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number']},    'ts_target_tvr_hump': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number']},    'ts_delta_limit': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},        # Special 类别函数    'inst_pnl': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'self_corr': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'in': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'universe_size': {'min_args': 0, 'max_args': 0, 'arg_types': []},        # Missing functions from operators.py    'quantile': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'driver', 'sigma']},  # quantile(x, driver = gaussian, sigma = 1.0)    'normalize': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'boolean', 'number']},  # normalize(x, useStd = false, limit = 0.0)    'zscore': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # zscore(x)        # Logical 类别函数    'or': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'and': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'not': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # 注意：这是关键字    'is_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'is_not_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'less': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'is_finite': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'if_else': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'not_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'less_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},        # Vector 类别函数    'vec_kurtosis': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_min': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_count': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_sum': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_skewness': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_max': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_avg': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_range': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_choose': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'nth']},    'vec_powersum': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},    'vec_stddev': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_percentage': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'percentage']},    'vec_ir': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_norm': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'ts_percentage': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'percentage']},    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},        # Additional functions from test cases    'rank_by_side': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'rate', 'scale']},    'log_diff': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_mask': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'ts_partial_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'ts_triple_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'clamp': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},    'keep': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'condition', 'period']},    'replace': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'target', 'dest']},    'filter': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'h', 't']},    'one_side': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'string'], 'param_names': ['x', 'side']},    'scale_down': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},        # Arithmetic 类别函数    'add': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # add(x, y, filter=false)    'multiply': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 99 + ['boolean'], 'param_names': ['x', 'y', 'filter']},  # multiply(x, y, ..., filter=false)    'sign': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'subtract': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # subtract(x, y, filter=false)    'pasteurize': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'log': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'purify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'arc_tan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'max': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # max(x, y, ...)    'to_nan': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # to_nan(x, value=0, reverse=false)    'abs': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sigmoid': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'divide': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # divide(x, y)    'min': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # min(x, y, ...)    'tanh': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_out': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},  # nan_out(x, lower=0, upper=0)    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # signed_power(x, y)    'inverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'round': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sqrt': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    's_log_1p': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'reverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # -x    'power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # power(x, y)    'densify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'floor': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},}# 2. 定义group类型字段group_fields = {    'sector', 'subindustry', 'industry', 'exchange', 'country', 'market'}# 3. 有效类别集合valid_categories = group_fields# 4. 字段命名模式 - 只校验字段是不是数字字母下划线组成field_patterns = [    re.compile(r'^[a-zA-Z0-9_]+$'),  # 只允许数字、字母和下划线组成的字段名]# 4. 抽象语法树节点类型class ASTNode:    """抽象语法树节点基类"""    def __init__(self, node_type: str, children: Optional[List['ASTNode']] = None,                  value: Optional[Any] = None, line: Optional[int] = None):        self.node_type = node_type  # 'function', 'operator', 'field', 'number', 'expression'        self.children = children or []        self.value = value        self.line = line        def __str__(self) -> str:        return f"ASTNode({self.node_type}, {self.value}, line={self.line})"        def __repr__(self) -> str:        return self.__str__()class ExpressionValidator:    """表达式验证器类"""        def __init__(self):        """初始化词法分析器和语法分析器"""        # 构建词法分析器        self.lexer = lex.lex(module=self, debug=False)        # 构建语法分析器        self.parser = yacc.yacc(module=self, debug=False)        # 错误信息存储        self.errors = []        # 词法分析器规则    tokens = ('FUNCTION', 'FIELD', 'NUMBER', 'LPAREN', 'RPAREN',               'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'COMMA', 'CATEGORY',              'EQUAL', 'ASSIGN', 'IDENTIFIER', 'STRING', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'NOTEQUAL', 'BOOLEAN')        # 忽略空白字符    t_ignore = ' \t\n'        # 操作符 - 注意顺序很重要，长的操作符要放在前面    t_PLUS = r'\+'    t_MINUS = r'-'    t_TIMES = r'\*'    t_DIVIDE = r'/'    t_LPAREN = r'\('    t_RPAREN = r'\)'    t_COMMA = r','        t_EQUAL = r'=='    t_NOTEQUAL = r'!='    t_GREATEREQUAL = r'>='    t_LESSEQUAL = r'<='    t_GREATER = r'>'    t_LESS = r'<'    t_ASSIGN = r'='        # 数字（整数和浮点数）    def t_NUMBER(self, t):        r'\d+\.?\d*'        if '.' in t.value:            t.value = float(t.value)        else:            t.value = int(t.value)        return t        # 字符串 - 需要放在所有其他标识符规则之前    def t_STRING(self, t):        r"'[^']*'|\"[^\"]*\""        # 去除引号        t.value = t.value[1:-1]        return t        # 函数和字段名    def t_IDENTIFIER(self, t):        r'[a-zA-Z_][a-zA-Z0-9_]*'        # 检查是否为布尔值        if t.value.lower() in {'true', 'false'}:            t.type = 'BOOLEAN'            t.value = t.value.lower()  # 转换为小写以保持一致性        else:            # 查看当前token后面的字符，判断是否为参数名（后面跟着'='）            lexpos = t.lexpos            next_chars = ''            if lexpos + len(t.value) < len(t.lexer.lexdata):                # 查看当前token后面的字符，跳过空格                next_pos = lexpos + len(t.value)                while next_pos < len(t.lexer.lexdata) and t.lexer.lexdata[next_pos].isspace():                    next_pos += 1                if next_pos < len(t.lexer.lexdata):                    next_chars = t.lexer.lexdata[next_pos:next_pos+1]                        # 如果后面跟着'='，则为参数名            if next_chars == '=':                t.type = 'IDENTIFIER'            # 如果后面跟着'('，则为函数名            elif next_chars == '(':                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为参数名（支持更多参数名）            elif t.value in {'std', 'k', 'lambda_min', 'lambda_max', 'target_tvr', 'range', 'buckets', 'lag', 'rettype', 'mode', 'nth', 'constant', 'percentage', 'driver', 'sigma', 'rate', 'scale', 'filter', 'lower', 'upper', 'target', 'dest', 'event', 'sensitivity', 'force', 'h', 't', 'period', 'stddev', 'factor', 'k', 'useStd', 'limit', 'gaussian', 'uniform', 'cauchy'}:                t.type = 'IDENTIFIER'            # 检查是否为函数名（不区分大小写）            elif t.value.lower() in supported_functions:                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为有效类别            elif t.value in valid_categories:                t.type = 'CATEGORY'            # 检查是否为字段名            elif self._is_valid_field(t.value):                t.type = 'FIELD'            else:                # 其他标识符，保留为IDENTIFIER类型                t.type = 'IDENTIFIER'        return t        # 行号跟踪    def t_newline(self, t):        r'\n+'        t.lexer.lineno += len(t.value)        # 错误处理    def t_error(self, t):        if t:            # 检查是否为非法字符            if not re.match(r'[a-zA-Z0-9_\+\-\*/\(\)\,\s=<>!]', t.value[0]):                # 这是一个非法字符                self.errors.append(f"非法字符 '{t.value[0]}' (行 {t.lexer.lineno})")            else:                # 这是一个非法标记                self.errors.append(f"非法标记 '{t.value}' (行 {t.lexer.lineno})")            # 跳过这个字符，继续处理            t.lexer.skip(1)        else:            self.errors.append("词法分析器到达文件末尾")        # 语法分析器规则    def p_expression(self, p):        """expression : comparison                      | expression EQUAL comparison                      | expression NOTEQUAL comparison                      | expression GREATER comparison                      | expression LESS comparison                      | expression GREATEREQUAL comparison                      | expression LESSEQUAL comparison"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_comparison(self, p):        """comparison : term                      | comparison PLUS term                      | comparison MINUS term"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_term(self, p):        """term : factor                | term TIMES factor                | term DIVIDE factor"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_factor(self, p):        """factor : NUMBER                  | STRING                  | FIELD                  | CATEGORY                  | IDENTIFIER                  | BOOLEAN                  | MINUS factor                  | LPAREN expression RPAREN                  | function_call"""        if len(p) == 2:            # 数字、字符串、字段、类别或标识符            if p.slice[1].type == 'NUMBER':                p[0] = ASTNode('number', value=p[1])            elif p.slice[1].type == 'STRING':                p[0] = ASTNode('string', value=p[1])            elif p.slice[1].type == 'FIELD':                p[0] = ASTNode('field', value=p[1])            elif p.slice[1].type == 'CATEGORY':                p[0] = ASTNode('category', value=p[1])            elif p.slice[1].type == 'BOOLEAN':                p[0] = ASTNode('boolean', value=p[1])            elif p.slice[1].type == 'IDENTIFIER':                p[0] = ASTNode('identifier', value=p[1])            else:                p[0] = p[1]        elif len(p) == 3:            # 一元负号            p[0] = ASTNode('unop', [p[2]], {'op': p[1]})        elif len(p) == 4:            # 括号表达式            p[0] = p[2]        else:            # 函数调用            p[0] = p[1]        def p_function_call(self, p):        '''function_call : FUNCTION LPAREN args RPAREN'''        p[0] = ASTNode('function', p[3], p[1])        def p_args(self, p):        '''args : arg_list                | empty'''        if len(p) == 2 and p[1] is not None:            p[0] = p[1]        else:            p[0] = []        def p_arg_list(self, p):        '''arg_list : arg                   | arg_list COMMA arg'''        if len(p) == 2:            p[0] = [p[1]]        else:            p[0] = p[1] + [p[3]]        def p_arg(self, p):        '''arg : expression              | IDENTIFIER ASSIGN expression'''        if len(p) == 2:            p[0] = {'type': 'positional', 'value': p[1]}        else:            p[0] = {'type': 'named', 'name': p[1], 'value': p[3]}        def p_empty(self, p):        '''empty :'''        p[0] = None        # 语法错误处理    def p_error(self, p):        if p:            self.errors.append(f"语法错误在位置 {p.lexpos}: 非法标记 '{p.value}'")        else:            self.errors.append("语法错误: 表达式不完整")        def _is_valid_field(self, field_name: str) -> bool:        """检查字段名是否符合模式"""        for pattern in field_patterns:            if pattern.match(field_name):                return True        return False        def validate_function(self, node: ASTNode, is_in_group_arg: bool = False) -> List[str]:        """验证函数调用的参数数量和类型"""        function_name = node.value        args = node.children        function_info = supported_functions.get(function_name)                if not function_info:            return [f"未知函数: {function_name}"]                errors = []                # 检查参数数量        if len(args) < function_info['min_args']:            errors.append(f"函数 {function_name} 需要至少 {function_info['min_args']} 个参数，但只提供了 {len(args)}")        elif len(args) > function_info['max_args']:            errors.append(f"函数 {function_name} 最多接受 {function_info['max_args']} 个参数，但提供了 {len(args)}")                # 处理参数验证        # 跟踪已使用的位置参数索引        positional_index = 0                # 对于所有函数，支持命名参数        for arg in args:            if isinstance(arg, dict):                if arg['type'] == 'named':                    # 命名参数                    if 'param_names' in function_info and arg['name'] in function_info['param_names']:                        # 查找参数在param_names中的索引                        param_index = function_info['param_names'].index(arg['name'])                        if param_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][param_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, param_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    # 对于winsorize函数，支持std和clip参数                    elif function_name == 'winsorize' and arg['name'] in ['std', 'clip']:                        arg_errors = self._validate_arg_type(arg['value'], 'number', 0, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    # 对于bucket函数，支持'range'和'buckets'参数                    elif function_name == 'bucket' and arg['name'] in ['range', 'buckets']:                        # range和buckets参数应该是string类型                        arg_errors = self._validate_arg_type(arg['value'], 'string', 1, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    else:                        errors.append(f"函数 {function_name} 不存在参数 '{arg['name']}'")                elif arg['type'] == 'positional':                    # 位置参数（字典形式）                    # 对于winsorize函数，第二个参数必须是命名参数                    if function_name == 'winsorize' and positional_index == 1:                        errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                    # 对于ts_moment函数，第三个参数必须是命名参数                    elif function_name == 'ts_moment' and positional_index == 2:                        errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                    else:                        # 验证位置参数的类型                        if positional_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][positional_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, positional_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    positional_index += 1                else:                    # 其他字典类型参数                    errors.append(f"参数 {positional_index+1} 格式错误")                    positional_index += 1            else:                # 位置参数（直接ASTNode形式）                # 对于winsorize函数，第二个参数必须是命名参数                if function_name == 'winsorize' and positional_index == 1:                    errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                # 对于ts_moment函数，第三个参数必须是命名参数                elif function_name == 'ts_moment' and positional_index == 2:                    errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                else:                    # 验证位置参数的类型                    if positional_index < len(function_info['arg_types']):                        expected_type = function_info['arg_types'][positional_index]                        arg_errors = self._validate_arg_type(arg, expected_type, positional_index, function_name, is_in_group_arg)                        errors.extend(arg_errors)                positional_index += 1                return errors        def _validate_arg_type(self, arg: ASTNode, expected_type: str, arg_index: int, function_name: str, is_in_group_arg: bool = False) -> List[str]:        """验证参数类型是否符合预期"""        errors = []                # 首先检查是否是group类型字段，如果是则只能用于Group类型函数        # 但是如果当前函数是group_xxx或在group函数的参数链中，则允许使用        if arg.node_type == 'category' and arg.value in group_fields:            if not (function_name.startswith('group_') or is_in_group_arg):                errors.append(f"Group类型字段 '{arg.value}' 只能用于Group类型函数的参数中")                # 然后验证参数类型是否符合预期        if expected_type == 'expression':            # 表达式可以是任何有效的AST节点            pass        elif expected_type == 'number':            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个数字，但得到 {arg.node_type}")        elif expected_type == 'boolean':            # 布尔值可以是数字（0/1）            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个布尔值（0/1），但得到 {arg.node_type}")        elif expected_type == 'field':            if arg.node_type != 'field' and arg.node_type != 'category':                # 允许field或category作为字段参数                errors.append(f"参数 {arg_index+1} 应该是一个字段，但得到 {arg.node_type}")            elif arg.node_type == 'field' and not self._is_valid_field(arg.value):                errors.append(f"无效的字段名: {arg.value}")        elif expected_type == 'category':            if not function_name.startswith('group_'):                # 非group函数的category参数必须是category类型且在valid_categories中                if arg.node_type != 'category':                    errors.append(f"参数 {arg_index+1} 应该是一个类别，但得到 {arg.node_type}")                elif arg.value not in valid_categories:                    errors.append(f"无效的类别: {arg.value}")            # group函数的category参数可以是任何类型（field、category等），不进行类型校验                return errors        def validate_ast(self, ast: Optional[ASTNode], is_in_group_arg: bool = False) -> List[str]:        """递归验证抽象语法树"""        if not ast:            return ["无法解析表达式"]                errors = []                # 根据节点类型进行验证        if ast.node_type == 'function':            # 检查当前函数是否是group函数            is_group_function = ast.value.startswith('group_')            # 确定当前是否在group函数的参数链中            current_in_group_arg = is_in_group_arg or is_group_function            # 验证函数            function_errors = self.validate_function(ast, current_in_group_arg)            errors.extend(function_errors)                        # 递归验证子节点时使用current_in_group_arg            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], current_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, current_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type in ['unop', 'binop']:            # 对操作符的子节点进行验证            for child in ast.children:                if hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type == 'field':            # 验证字段名            if not self._is_valid_field(ast.value):                errors.append(f"无效的字段名: {ast.value}")        else:            # 递归验证子节点            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], is_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)                return errors        def _process_semicolon_expression(self, expression: str) -> Tuple[bool, str]:        """处理带有分号的表达式，将其转换为不带分号的简化形式                Args:            expression: 要处理的表达式字符串                    Returns:            Tuple[bool, str]: (是否成功, 转换后的表达式或错误信息)        """        # 检查表达式是否以分号结尾        if expression.strip().endswith(';'):            return False, "表达式不能以分号结尾"                # 分割表达式为语句列表        statements = [stmt.strip() for stmt in expression.split(';') if stmt.strip()]        if not statements:            return False, "表达式不能为空"                # 存储变量赋值        variables = {}                # 处理每个赋值语句（除了最后一个）        for i, stmt in enumerate(statements[:-1]):            # 检查是否包含赋值符号            if '=' not in stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 检查是否是比较操作符（==, !=, <=, >=）            if any(op in stmt for op in ['==', '!=', '<=', '>=']):                # 如果包含比较操作符，需要确认是否有赋值符号                # 使用临时替换法：将比较操作符替换为临时标记，再检查是否还有=                temp_stmt = stmt                for op in ['==', '!=', '<=', '>=']:                    temp_stmt = temp_stmt.replace(op, '---')                                if '=' not in temp_stmt:                    return False, f"第{i+1}个语句必须是赋值语句，不能只是比较表达式"                        # 找到第一个=符号（不是比较操作符的一部分）            # 先将比较操作符替换为临时标记，再找=            temp_stmt = stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' not in temp_stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 找到实际的=位置            equals_pos = temp_stmt.index('=')                        # 在原始语句中找到对应位置            real_equals_pos = 0            temp_count = 0            for char in stmt:                if temp_count == equals_pos:                    break                if char in '!<>':                    # 检查是否是比较操作符的一部分                    if real_equals_pos + 1 < len(stmt) and stmt[real_equals_pos + 1] == '=':                        # 是比较操作符，跳过两个字符                        real_equals_pos += 2                        temp_count += 3  # 因为替换成了三个字符的---                    else:                        real_equals_pos += 1                        temp_count += 1                else:                    real_equals_pos += 1                    temp_count += 1                        # 分割变量名和值            var_name = stmt[:real_equals_pos].strip()            var_value = stmt[real_equals_pos + 1:].strip()                        # 检查变量名是否有效            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var_name):                return False, f"第{i+1}个语句的变量名'{var_name}'无效，只能包含字母、数字和下划线，且不能以数字开头"                        var_name_lower = var_name.lower()  # 变量名不区分大小写                        # 检查变量名是否在后续表达式中使用            # 这里不需要，因为后面的表达式会检查                        # 检查变量值中使用的变量是否已经定义            # 简单检查：提取所有可能的变量名            used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', var_value)            for used_var in used_vars:                used_var_lower = used_var.lower()                if used_var_lower not in variables:                    # 检查是否是函数名                    if used_var not in supported_functions:                        # 对于单个字母或简单单词，不自动视为字段名，要求先定义                        if len(used_var) <= 2:                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 对于较长的字段名，仍然允许作为字段名                        elif not self._is_valid_field(used_var):                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 将之前定义的变量替换到当前值中            for existing_var, existing_val in variables.items():                # 使用单词边界匹配，避免替换到其他单词的一部分                var_value = re.sub(rf'\b{existing_var}\b', existing_val, var_value)                        # 存储变量            variables[var_name_lower] = var_value                # 处理最后一个语句（实际的表达式）        final_stmt = statements[-1]                # 检查最后一个语句是否是赋值语句        if '=' in final_stmt:            # 替换比较操作符为临时标记，然后检查是否还有单独的=            temp_stmt = final_stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' in temp_stmt:                return False, "最后一个语句不能是赋值语句"                # 检查最后一个语句中使用的变量是否已经定义        used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', final_stmt)        for used_var in used_vars:            used_var_lower = used_var.lower()            if used_var_lower not in variables:                # 检查是否是函数名                if used_var not in supported_functions:                    # 在分号表达式中，所有非函数名的标识符都必须是变量，必须在之前定义                    return False, f"最后一个语句中使用的变量'{used_var}'未在之前定义"                # 将变量替换到最后一个表达式中        final_expr = final_stmt        for var_name, var_value in variables.items():            final_expr = re.sub(rf'\b{var_name}\b', var_value, final_expr)                return True, final_expr        def check_expression(self, expression: str) -> Dict[str, Any]:        """        检查表达式格式是否正确                Args:            expression: 要验证的表达式字符串                    Returns:            包含验证结果的字典        """        # 重置错误列表        self.errors = []                try:            expression = expression.strip()            if not expression:                return {                    'valid': False,                    'errors': ['表达式不能为空'],                    'tokens': [],                    'ast': None                }                        # 处理带有分号的表达式            if ';' in expression:                success, result = self._process_semicolon_expression(expression)                if not success:                    return {                        'valid': False,                        'errors': [result],                        'tokens': [],                        'ast': None                    }                expression = result                        # 重置词法分析器的行号            self.lexer.lineno = 1                        # 词法分析（用于调试）            self.lexer.input(expression)            tokens = []            # 调试：打印识别的标记            print(f"\n调试 - 表达式: {expression}")            print("识别的标记:")            for token in self.lexer:                print(f"  - 类型: {token.type}, 值: '{token.value}', 位置: {token.lexpos}")                tokens.append(token)                        # 重新设置词法分析器的输入，以便语法分析器使用            self.lexer.input(expression)            self.lexer.lineno = 1                        # 语法分析            ast = self.parser.parse(expression, lexer=self.lexer)                        # 验证AST            validation_errors = self.validate_ast(ast)                        # 合并所有错误            all_errors = self.errors + validation_errors                        # 检查括号是否匹配            bracket_count = 0            for char in expression:                if char == '(':                    bracket_count += 1                elif char == ')':                    bracket_count -= 1                if bracket_count < 0:                    all_errors.append("括号不匹配: 右括号过多")                    break            if bracket_count > 0:                all_errors.append("括号不匹配: 左括号过多")                        return {                'valid': len(all_errors) == 0,                'errors': all_errors,                'tokens': tokens,                'ast': ast            }        except Exception as e:            return {                'valid': False,                'errors': [f"解析错误: {str(e)}"],                'tokens': [],                'ast': None            }def main():    """主函数 - 用于验证表达式并输出结果到JSON文件"""    validator = ExpressionValidator()        # 获取用户输入的JSON文件路径，默认路径为当前路径下的Tranformer/output/Alpha_generated_expressions.json    default_path = os.path.join("Tranformer", "output", "Alpha_generated_expressions.json")    input_path = input(f"请输入要校验的表达式JSON文件路径（默认：{default_path}）: ").strip()        if not input_path:        input_path = default_path        # 检查文件是否存在    if not os.path.exists(input_path):        print(f"错误: 文件 {input_path} 不存在")        return        # 读取JSON文件    try:        with open(input_path, 'r', encoding='utf-8') as f:            expressions_data = json.load(f)    except json.JSONDecodeError as e:        print(f"错误: JSON文件解析失败 - {e}")        return        # 提取表达式列表    # 假设JSON文件结构为 {"expressions": ["expr1", "expr2", ...]} 或直接是 ["expr1", "expr2", ...]    if isinstance(expressions_data, dict) and "expressions" in expressions_data:        expressions = expressions_data["expressions"]    elif isinstance(expressions_data, list):        expressions = expressions_data    else:        print("错误: JSON文件格式不正确，需要包含表达式列表")        return        # 验证表达式    valid_expressions = []    invalid_expressions = []        print(f"开始验证 {len(expressions)} 个表达式...")    for i, expr in enumerate(expressions, 1):        if i % 10 == 0:            print(f"已验证 {i}/{len(expressions)} 个表达式")                    result = validator.check_expression(expr)        if result["valid"]:            valid_expressions.append(expr)        else:            invalid_expressions.append({"expression": expr, "errors": result["errors"]})        # 生成输出文件路径    base_name = os.path.basename(input_path)    name, ext = os.path.splitext(base_name)    output_dir = os.path.dirname(input_path)        valid_output_path = os.path.join(output_dir, f"{name}_success{ext}")    invalid_output_path = os.path.join(output_dir, f"{name}_error{ext}")        # 保存结果到JSON文件    print(f"\n验证完成！")    print(f"有效表达式: {len(valid_expressions)}")    print(f"无效表达式: {len(invalid_expressions)}")        # 保存有效表达式    try:        with open(valid_output_path, 'w', encoding='utf-8') as f:            json.dump(valid_expressions, f, ensure_ascii=False, indent=2)        print(f"有效表达式已保存到: {valid_output_path}")    except Exception as e:        print(f"错误: 保存有效表达式失败 - {e}")        # 保存无效表达式    try:        with open(invalid_output_path, 'w', encoding='utf-8') as f:            json.dump(invalid_expressions, f, ensure_ascii=False, indent=2)        print(f"无效表达式已保存到: {invalid_output_path}")    except Exception as e:        print(f"错误: 保存无效表达式失败 - {e}")if __name__ == "__main__":    main()
```

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
大佬的动作好快，昨晚我还想怎么弄，今天就看到了帖子。

运行一次通过，非常有启发。

-----------------------------------------------------------------------------------------------------------

大模型的时代不知不觉就来了。。。用中学。。。


---

### 技术对话片段 34 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【Community Leader -因子构造 】ai推荐比率按照实际含义推荐operator经验分享.md
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，最早课代表发过一个帖子，让豆包做比率，一年后又进化了，比率这个方向挺好的，使用范围广。而且有时候可以点两个塔，pnl曲线也不错。

----------------------------------------------------------------------------------

回归本质，做简单的事，比如：让AI做比率

----------------------------------------------------------------------------------


---

### 技术对话片段 35 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，最早课代表发过一个帖子，让豆包做比率，一年后又进化了，比率这个方向挺好的，使用范围广。而且有时候可以点两个塔，pnl曲线也不错。

----------------------------------------------------------------------------------

回归本质，做简单的事，比如：让AI做比率

----------------------------------------------------------------------------------


---

### 技术对话片段 36 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享，目前我最薄弱的环节就是提示词了。

gemini/iflow都配置好了，下一步就跟着大家的提示词练起来。现在顾问的差异可能就是提示词的优化程度了，希望也能分享一个有用的提示词给社区。

---------------------------------------------------------------------------------

时间要花在有效率的地方

---------------------------------------------------------------------------------


---

### 技术对话片段 37 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】本地数据库的使用筛选代码优化_36682316922135.md
- **时间**: 6个月前

**提问/主帖背景 (WL27618)**:
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
mongodb安装在本地，定期从服务器拉取，如果在服务器上运行，低配的服务器可能性能跟不上。

另外，可以分批查询，第一次全量查询24G内存的电脑直接崩了。让gemini改成了分批，效果就好了，最简单的指定一个日期范围。

------------------------------------------------------------------------------------------

路虽远，行则将至。

-------------------------------------------------------------------------------------------


---

### 技术对话片段 38 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Eligibility Criteria篇】一文告诉你如何GOLD直通Grandmaster上篇置顶的论坛精选_39922788056343.md
- **时间**: 26天前

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

感谢weijie老师，kunqi老师，huangkai老师，顾问 KZ79256 (Rank 21) (华子哥)，XX42289 (课代表) ，worldquant brain赛博游戏王 (游戏王)，顾问 QX52484 (Rank 35) (司源老师)，顾问 FX25214 (传奇耐打王/耐打王) (Rank 22)，DA98440，JX39934，ZH41150，顾问 RM49262 (Rank 30)，PP26750， LD27384，顾问 JG15244 (Rank 67)，LS17092，WT73952，XJ80376，QW94165，ZY20347，JZ45765，ll46807，JW52291等研究小组二群的各位朋友们！！！！

**最后祝各位顾问月月VF1.0！RA60刀！SA60！日日120刀！！！！**

**高筑墙！广积粮！缓称王！**

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
哇塞！绝对是值得反复看的帖子呀。越看越敬佩，帖子说的也很清楚，模版思路、提交标准都有了，希望能看到更多尼克总的分享贴。。。

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================


---

### 技术对话片段 39 (原帖: 【LLM agent】构建全流程的大模型交易agent——第二步：收集operators信息)
- **原帖链接**: [Commented] 【LLM agent】构建全流程的大模型交易agent第二步收集operators信息.md
- **时间**: 1年前

**提问/主帖背景 (YK53163)**:
since operators are as important as data fields, and it can be difficult to search for operators directly, we need to build an operators database to help us (or LLM) understand the operators.

考虑到操作符的重要性和数据字段一样，而且直接放入操作符会很困难，所以我们需要构建一个操作符DB来帮助我们（或LLM）理解操作符。

### Step1. 获取operators信息

最近刚好operator的功能有更新，我看了一下是对部分operator有了图解和例子，其实对于理解非常好，不过由于多模态llm和其他的一些东西还没时间弄，所以只能先做纯text llm，这个时候需要先爬取数据

#### 法一：使用selenium爬取

```
from selenium import webdriverfrom selenium.webdriver.chrome.service import Servicefrom selenium.webdriver.common.by import Byimport timechrome_driver_path = "path/to/chromedriver"  # 替换为你的 ChromeDriver 路径service = Service(chrome_driver_path)driver = webdriver.Chrome(service=service)login_url = "[链接已屏蔽])email_input = driver.find_element(By.ID, "email")  # 根据实际 HTML ID 修改password_input = driver.find_element(By.ID, "password")  # 根据实际 HTML ID 修改email_input.send_keys("your_email@example.com")  # 替换为你的邮箱password_input.send_keys("your_password")  # 替换为你的密码login_button = driver.find_element(By.ID, "login-button")  login_button.click()time.sleep(5)# 获取目标页面内容url = "[链接已屏蔽])# 保存 HTML 内容html_content = driver.page_sourcewith open("operators.html", "w", encoding="utf-8") as file:    file.write(html_content)print("HTML 内容已保存到 operators.html 文件中")# 关闭浏览器driver.quit()
```

#### 法二：直接复制粘贴

复制粘贴比上面那个方便很多（对于单页面来说），如果爬虫不是很熟悉的盆友用这个办法肯定不会出错

windows: ctrl + shift + I -> 开发者工具 -> 放到header上 -> 编辑为html -> ctrl + A -> ctrl + C -> 粘贴到文件中


> [!NOTE] [图片 OCR 识别内容]
> !DOCTYPE html〉
> 〈html
> 一++
> dn
> 〈hea
> 添加属性
> 〈bod
> CI(
> 编辑属性
> <di
> 〈nC
> 编辑为 HTML
> ;Cr


*（默认存储为operators.html）*

### Step2. 解析数据

首先这个数据是藏在一个比较深的地方，可以随便搜索一个


> [!NOTE] [图片 OCR 识别内容]
> F10CeL1
> STyLe=
> 十LC
> bU
> aUTO;
> WIOTh
> Searchoperators
> Scope:
> AIl
> GOpX;
> 〈1div〉
> 〈div class="rt-td rt-td--description
> role=
> 'gridcell" styles"flex:
> 200
> auto;
> Arithmetic
> Width:
> 2OOpx;
> 〈/div〉
> 〈1div〉
> 〈/div〉
> Operator
> Scope
> Description
> 〈div class="rt-tr-group
> role="rowgroup
> 〈/div〉
> FIex
> aDS(x)
> Combo; Regular; Selection
> Jbsolute Value OTx
> <div
> CLass="rt-tr-group
> role="rowgroup
> flex
> add(xy filter
> falsej; x +y
> Combo; Regular; Selection
> Jddallinputs (at
> east
> inputs requiredj.If filter
> trUe
> flter allinput NaNto
> beTore
> adding
> 〈div CIass="rt-tr
> -Odd" role="row
> TLex
> 〈div CIass="rt-td rt-td--definition
> role=
> 'gridcell" style-"flex:
> 60
> auto;
> If-1二X二 1: arCCOSIXJ; 2lse NaN
> Width:
> 6OpX;
> div#tarc_tan.alphas-list-table
> 〈div id
> arc tan
> class="alphas-Iist-ta
> cell-contentalphas-list-tabl
> 181.9*38.98
> ble
> Cell-content alphas-Iist-table_
> Ce
> cell-content -with-
> If-1 =X二 1: arcsinlxj; else NaN
> 11-content--Wi
> th-wrapping
> arC
> tan
> 〈Idiv〉
> $0
> arC_tanlx)
> Combo; Regular; Selection
> This Operator doesinverse
> tangent ofinput
> 〈1div〉
> ShOW MOrE
> 〈div class="rt-td rt-td--scope
> role="吕
> ridcell"
> style="flex:
> 60
> auto; Width:
> GOpX;
> 〈1div〉


解析代码如下：

```
from bs4 import BeautifulSoupimport pandas as pdwith open("operators.html", "r", encoding="utf-8") as file:    html_content = file.read()soup = BeautifulSoup(html_content, "lxml")tables = soup.find_all("div", class_="operator-table")all_tables = {}for table in tables:    # get the title --- (h2)    table_title = table.find_previous("h2").text.strip()    headers = [header.text.strip() for header in table.find_all("div", class_="rt-th")]    # extract table    data = []    rows = table.find_all("div", class_="rt-tr-group")    for row in rows:        # tract all data cells        cells = row.find_all("div", class_="rt-td")        row_data = [cell.text.strip().replace('"', '') for cell in cells]  # 移除双引号        if row_data:  # filter nan row            data.append(row_data)    # check consistency    if headers and data and len(headers) != len(data[0]):        print(f"表格 {table_title} 的列数不匹配。修正列数ing...")        # since there is a situation about mismatch between number of rows and number of columns, so here it will be fixed        # 不一致情况的解决        if len(headers) > len(data[0]):            headers = headers[:len(data[0])]  # truncate        elif len(headers) < len(data[0]):            headers += [f"Extra Column {i}" for i in range(len(headers), len(data[0]))]  # add extra columns    if headers and data:        df = pd.DataFrame(data, columns=headers)        all_tables[table_title] = df    else:        print(f"Table {table_title} extract fail-提取失败")# save tablesfor table_name, df in all_tables.items():    filename = f"{table_name.replace(' ', '_').lower()}_table.csv"    df.to_csv(filename, index=False, encoding="utf-8")    print(f"Table {table_name} saved {filename} - 成功保存")# merge tables into one tableif all_tables:    df["Ops_Category"] = table_name    combined_df = pd.concat(all_tables.values(), keys=all_tables.keys())    combined_df.to_csv("operators.csv", index=False, encoding="utf-8")    print("combined table is saved to  operators.csv")else:    print("no valid table")
```

### step3. 存入operators数据表

```
db_name = "..\worldquant.db"conn = sqlite3.connect(db_name)  combined_df.to_sql("operators", conn, if_exists="replace", index=False)print("saved successfully! - table operators")conn.close()
```

#### 验证（之前都忘了）

```
db_name = "..\worldquant.db"conn = sqlite3.connect(db_name) query = """SELECT *FROM operatorsdf = pd.read_sql(query, conn)print(df)conn.close()
```

**注意**

1. 之前的话其实我一直在思考就是如何存储会比较方便后面的检索，因此在检索的时候keywords会比较重要，我去问了一些大佬们综合了一下决定先把operators放一个表，但是datafields按照category分开，这样是为了在获取信息的时候一般都是优先考虑data，然后再看region等，拆开的话检索效率也会比较高，不过由于还没有批量实操，所以具体的话还并不清楚

2. 目前还是在做数据（Data is Electricity :> )。而且数据其实还有一些准备工作，不过我觉得这两个是最重要的两个数据，并且是非常难直接给大模型的，因此只放入这两个（暂时）。在具体处理fast experssion或者skill的时候我用的是别的一些方法（后续谈）

*PS: Pipeline还没有画好，有空的话大概这周能更新pipeline*

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
好像大模型对json的支持比较好，mongo可能更方便。期待更新


---

### 技术对话片段 40 (原帖: 【LLM agent】构建全流程的大模型交易agent——第二步：收集operators信息)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【LLM agent】构建全流程的大模型交易agent第二步收集operators信息_28883831871511.md
- **时间**: 1年前

**提问/主帖背景 (YK53163)**:
since operators are as important as data fields, and it can be difficult to search for operators directly, we need to build an operators database to help us (or LLM) understand the operators.

考虑到操作符的重要性和数据字段一样，而且直接放入操作符会很困难，所以我们需要构建一个操作符DB来帮助我们（或LLM）理解操作符。

### Step1. 获取operators信息

最近刚好operator的功能有更新，我看了一下是对部分operator有了图解和例子，其实对于理解非常好，不过由于多模态llm和其他的一些东西还没时间弄，所以只能先做纯text llm，这个时候需要先爬取数据

#### 法一：使用selenium爬取

```
from selenium import webdriverfrom selenium.webdriver.chrome.service import Servicefrom selenium.webdriver.common.by import Byimport timechrome_driver_path = "path/to/chromedriver"  # 替换为你的 ChromeDriver 路径service = Service(chrome_driver_path)driver = webdriver.Chrome(service=service)login_url = "[链接已屏蔽])email_input = driver.find_element(By.ID, "email")  # 根据实际 HTML ID 修改password_input = driver.find_element(By.ID, "password")  # 根据实际 HTML ID 修改email_input.send_keys("your_email@example.com")  # 替换为你的邮箱password_input.send_keys("your_password")  # 替换为你的密码login_button = driver.find_element(By.ID, "login-button")  login_button.click()time.sleep(5)# 获取目标页面内容url = "[链接已屏蔽])# 保存 HTML 内容html_content = driver.page_sourcewith open("operators.html", "w", encoding="utf-8") as file:    file.write(html_content)print("HTML 内容已保存到 operators.html 文件中")# 关闭浏览器driver.quit()
```

#### 法二：直接复制粘贴

复制粘贴比上面那个方便很多（对于单页面来说），如果爬虫不是很熟悉的盆友用这个办法肯定不会出错

windows: ctrl + shift + I -> 开发者工具 -> 放到header上 -> 编辑为html -> ctrl + A -> ctrl + C -> 粘贴到文件中


> [!NOTE] [图片 OCR 识别内容]
> !DOCTYPE html〉
> 〈html
> 一++
> dn
> 〈hea
> 添加属性
> 〈bod
> CI(
> 编辑属性
> <di
> 〈nC
> 编辑为 HTML
> ;Cr


*（默认存储为operators.html）*

### Step2. 解析数据

首先这个数据是藏在一个比较深的地方，可以随便搜索一个


> [!NOTE] [图片 OCR 识别内容]
> F10CeL1
> STyLe=
> 十LC
> bU
> aUTO;
> WIOTh
> Searchoperators
> Scope:
> AIl
> GOpX;
> 〈1div〉
> 〈div class="rt-td rt-td--description
> role=
> 'gridcell" styles"flex:
> 200
> auto;
> Arithmetic
> Width:
> 2OOpx;
> 〈/div〉
> 〈1div〉
> 〈/div〉
> Operator
> Scope
> Description
> 〈div class="rt-tr-group
> role="rowgroup
> 〈/div〉
> FIex
> aDS(x)
> Combo; Regular; Selection
> Jbsolute Value OTx
> <div
> CLass="rt-tr-group
> role="rowgroup
> flex
> add(xy filter
> falsej; x +y
> Combo; Regular; Selection
> Jddallinputs (at
> east
> inputs requiredj.If filter
> trUe
> flter allinput NaNto
> beTore
> adding
> 〈div CIass="rt-tr
> -Odd" role="row
> TLex
> 〈div CIass="rt-td rt-td--definition
> role=
> 'gridcell" style-"flex:
> 60
> auto;
> If-1二X二 1: arCCOSIXJ; 2lse NaN
> Width:
> 6OpX;
> div#tarc_tan.alphas-list-table
> 〈div id
> arc tan
> class="alphas-Iist-ta
> cell-contentalphas-list-tabl
> 181.9*38.98
> ble
> Cell-content alphas-Iist-table_
> Ce
> cell-content -with-
> If-1 =X二 1: arcsinlxj; else NaN
> 11-content--Wi
> th-wrapping
> arC
> tan
> 〈Idiv〉
> $0
> arC_tanlx)
> Combo; Regular; Selection
> This Operator doesinverse
> tangent ofinput
> 〈1div〉
> ShOW MOrE
> 〈div class="rt-td rt-td--scope
> role="吕
> ridcell"
> style="flex:
> 60
> auto; Width:
> GOpX;
> 〈1div〉


解析代码如下：

```
from bs4 import BeautifulSoupimport pandas as pdwith open("operators.html", "r", encoding="utf-8") as file:    html_content = file.read()soup = BeautifulSoup(html_content, "lxml")tables = soup.find_all("div", class_="operator-table")all_tables = {}for table in tables:    # get the title --- (h2)    table_title = table.find_previous("h2").text.strip()    headers = [header.text.strip() for header in table.find_all("div", class_="rt-th")]    # extract table    data = []    rows = table.find_all("div", class_="rt-tr-group")    for row in rows:        # tract all data cells        cells = row.find_all("div", class_="rt-td")        row_data = [cell.text.strip().replace('"', '') for cell in cells]  # 移除双引号        if row_data:  # filter nan row            data.append(row_data)    # check consistency    if headers and data and len(headers) != len(data[0]):        print(f"表格 {table_title} 的列数不匹配。修正列数ing...")        # since there is a situation about mismatch between number of rows and number of columns, so here it will be fixed        # 不一致情况的解决        if len(headers) > len(data[0]):            headers = headers[:len(data[0])]  # truncate        elif len(headers) < len(data[0]):            headers += [f"Extra Column {i}" for i in range(len(headers), len(data[0]))]  # add extra columns    if headers and data:        df = pd.DataFrame(data, columns=headers)        all_tables[table_title] = df    else:        print(f"Table {table_title} extract fail-提取失败")# save tablesfor table_name, df in all_tables.items():    filename = f"{table_name.replace(' ', '_').lower()}_table.csv"    df.to_csv(filename, index=False, encoding="utf-8")    print(f"Table {table_name} saved {filename} - 成功保存")# merge tables into one tableif all_tables:    df["Ops_Category"] = table_name    combined_df = pd.concat(all_tables.values(), keys=all_tables.keys())    combined_df.to_csv("operators.csv", index=False, encoding="utf-8")    print("combined table is saved to  operators.csv")else:    print("no valid table")
```

### step3. 存入operators数据表

```
db_name = "..\worldquant.db"conn = sqlite3.connect(db_name)  combined_df.to_sql("operators", conn, if_exists="replace", index=False)print("saved successfully! - table operators")conn.close()
```

#### 验证（之前都忘了）

```
db_name = "..\worldquant.db"conn = sqlite3.connect(db_name) query = """SELECT *FROM operatorsdf = pd.read_sql(query, conn)print(df)conn.close()
```

**注意**

1. 之前的话其实我一直在思考就是如何存储会比较方便后面的检索，因此在检索的时候keywords会比较重要，我去问了一些大佬们综合了一下决定先把operators放一个表，但是datafields按照category分开，这样是为了在获取信息的时候一般都是优先考虑data，然后再看region等，拆开的话检索效率也会比较高，不过由于还没有批量实操，所以具体的话还并不清楚

2. 目前还是在做数据（Data is Electricity :> )。而且数据其实还有一些准备工作，不过我觉得这两个是最重要的两个数据，并且是非常难直接给大模型的，因此只放入这两个（暂时）。在具体处理fast experssion或者skill的时候我用的是别的一些方法（后续谈）

*PS: Pipeline还没有画好，有空的话大概这周能更新pipeline*

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
好像大模型对json的支持比较好，mongo可能更方便。期待更新


---

### 技术对话片段 41 (原帖: resps 是concurrent_simulate 返回的值)
- **原帖链接**: [Commented] 【PyPI Package】基于异步实现的better machine lib一键安装pip install wqb论坛精选.md
- **时间**: 1年前

**提问/主帖背景 (HD44583)**:
分享网络好工具之 **wqb** ！

**仓库 / 下载 / 更新 / 用法：** 
 **PyPI:**   [pypi.org/project/wqb]([链接已屏蔽]) 
 **GitHub:**   [github.com/rocky-d/wqb]([链接已屏蔽])

- 使用前请认真阅读README.md
- 核心类wqb.WQBSession继承requests.Session，兼容machine_lib.py
- 自动认证机制，再也无需担心session过期
- 日志完善INFO & WARNING，log文本文件+控制台输出
- 方法涵盖Datasets, Fields, Alphas, Simulate, Check, Submit
- 核心methods基于异步实现，效率提升显著（相比旧machine_lib.py）
- 更多methods等你探索
- 如遇问题欢迎在GitHub仓库中提Issues

USA/1/TOP3000 实测约 50k/天（下图右侧部分，对比左侧部分旧machine_lib.py效率提升约50%）


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 01/11/2025
> Simulated Alphas: 50.64
> 2OK
> 3
> 3
> 9
> ^O.
> ^2;
> AA:
> 〈"
> ^8'
> 8
> 2
> N
> @
> ?8
> 35'
> 八 *
> 9*
> 9
> A'
> O
> ^^.
> ^3'
> ^'
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> "Jan
> 岳
> 岳
> 豆
> 岳
> 岳


祝大家新春快乐，Python蛇年快乐，新的一年Alpha多多！

[👉来自其他同学的补丁👉自己更改和完善后的wqb库 – WorldQuant BRAIN]([Commented] 自己更改和完善后的wqb库代码优化.md)

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的代码，Readme的示例里有一个小bug，倒数第二行少了字典的key

resp = wqbs.search_operators()

# print(resp.json())

operators = [item['name'] for item in resp.json()]

# print(operators)

operators_by_category = {}

for item in resp.json():

name = item['name']

category = item['category']

if category notin operators_by_category:

operators_by_category[category] = []

operators_by_category[category].append(name)

print(operators_by_category)


---

### 技术对话片段 42 (原帖: resps 是concurrent_simulate 返回的值)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【PyPI Package】基于异步实现的better machine lib一键安装pip install wqb论坛精选_29550580282775.md
- **时间**: 1年前

**提问/主帖背景 (HD44583)**:
分享网络好工具之 **wqb** ！

**仓库 / 下载 / 更新 / 用法：** 
 **PyPI:**   [pypi.org/project/wqb]([链接已屏蔽]) 
 **GitHub:**   [github.com/rocky-d/wqb]([链接已屏蔽])

- 使用前请认真阅读README.md
- 核心类wqb.WQBSession继承requests.Session，兼容machine_lib.py
- 自动认证机制，再也无需担心session过期
- 日志完善INFO & WARNING，log文本文件+控制台输出
- 方法涵盖Datasets, Fields, Alphas, Simulate, Check, Submit
- 核心methods基于异步实现，效率提升显著（相比旧machine_lib.py）
- 更多methods等你探索
- 如遇问题欢迎在GitHub仓库中提Issues

USA/1/TOP3000 实测约 50k/天（下图右侧部分，对比左侧部分旧machine_lib.py效率提升约50%）


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 01/11/2025
> Simulated Alphas: 50.64
> 2OK
> 3
> 3
> 9
> ^O.
> ^2;
> AA:
> 〈"
> ^8'
> 8
> 2
> N
> @
> ?8
> 35'
> 八 *
> 9*
> 9
> A'
> O
> ^^.
> ^3'
> ^'
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> Dec
> "Jan
> 岳
> 岳
> 豆
> 岳
> 岳


祝大家新春快乐，Python蛇年快乐，新的一年Alpha多多！

[👉来自其他同学的补丁👉自己更改和完善后的wqb库 – WorldQuant BRAIN]([Commented] 自己更改和完善后的wqb库代码优化_32415074214167.md)

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的代码，Readme的示例里有一个小bug，倒数第二行少了字典的key

resp = wqbs.search_operators()

# print(resp.json())

operators = [item['name'] for item in resp.json()]

# print(operators)

operators_by_category = {}

for item in resp.json():

name = item['name']

category = item['category']

if category notin operators_by_category:

operators_by_category[category] = []

operators_by_category[category].append(name)

print(operators_by_category)


---

### 技术对话片段 43 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Quant101】手把手教你搭建本地因子库 ①经验分享_39213565539095.md
- **时间**: 2个月前

**提问/主帖背景 (ZH87224)**:
新的一期 IQC 已经开跑，又会有一批新顾问进场。平台功能多、接口和字段杂，如果完全wqb、machine_lib或一些零散脚本，因子一多就很难检索、去重和做版本管理。

此外，对于顾问来说，有几个都会遇到的痛点：

- 平台使用美东时间，并且有夏令时切换，但我们都在CN，每次检索&设置还得考虑时区问题
- 现在回测很宝贵，每天就5000次，如何在回测时跳过已经回测过的表达式？
- 如果快速计算Self-Corr，并且区分PPA和RA？
- 如何快速知道哪些因子可以Check？
- ….

本地因子库就是来解决这一问题的，老顾问大多早就有了自己的一套流程和工具，我准备写一系列文章，面向刚入门、还没搭过完整系统的的新手，把本地因子库的搭建思路分享给大家，如果有帮到大家，欢迎点赞评论。

## 环境与工具

- **运行时依赖** ： `tortoise-orm>=1.1.6`
- **Notebook / 交互开发** ：建议安装  `ipykernel` ，在 VSCode 里使用 Jupyter Notebook 进行开发。
- **数据库浏览** ：SQLite 文件用 DataGrip 或 VS Code 的 SQLite 插件都能直接看表结构和数据。

## 为什么用 ORM 做本地因子库

写 SQL 太繁琐了，而且容易出错，ORM框架可以将数据库对象转换为Python对象，像代码一样操作数据库。

至于为什么选择 tortoise-orm，是因为本人有尝鲜情节，再加上 sqlalchemy 实在太笨重了。

## 废话不多说，直接上代码

```
from __future__ import annotations

import enum
import hashlib
from datetime import date, datetime
from pathlib import Path
from typing import Any, Self
from zoneinfo import ZoneInfo

from tortoise import Tortoise, fields, signals
from tortoise.models import Model

class AlphaType(enum.StrEnum):
    REGULAR = "REGULAR"
    SUPER = "SUPER"

class Status(enum.StrEnum):
    ACTIVE = "ACTIVE"
    UNSUBMITTED = "UNSUBMITTED"
    DECOMMISSIONED = "DECOMMISSIONED"

class Language(enum.StrEnum):
    FASTEXPR = "FASTEXPR"
    EXPR = "EXPR"
    PYTHON = "PYTHON"

class Instrument(enum.StrEnum):
    CRYPTO = "CRYPTO"
    EQUITY = "EQUITY"

class Region(enum.StrEnum):
    USA = "USA"
    GLB = "GLB"
    EUR = "EUR"
    ASI = "ASI"
    CHN = "CHN"
    IND = "IND"
    HKG = "HKG"

    def universes(self) -> list[Universe]:
        match self:
            case Region.USA:
                return [
                    Universe.TOP3000,
                    Universe.TOP1000,
                    Universe.TOP500,
                    Universe.TOP200,
                    Universe.ILLIQUID_MINVOL1M,
                    Universe.TOPSP500,
                ]
            case Region.GLB:
                return [Universe.TOP3000, Universe.TOPDIV3000, Universe.MINVOL1M]
            case Region.EUR:
                return [
                    Universe.TOP2500,
                    Universe.TOP1200,
                    Universe.ILLIQUID_MINVOL1M,
                    Universe.TOP800,
                    Universe.TOP400,
                    Universe.TOPCS1600,
                ]
            case Region.ASI:
                return [
                    Universe.ILLIQUID_MINVOL1M,
                    Universe.MINVOL1M,
                ]
            case Region.CHN:
                return [Universe.TOP2000U]
            case Region.IND:
                return [Universe.TOP500]
            case Region.HKG:
                return [Universe.TOP800, Universe.TOP500]
            case _:
                raise ValueError(f"Region {self} not supported")

    def neutralizations(self) -> list[Neutralization]:
        basic_neu = [
            Neutralization.NONE,
            Neutralization.MARKET,
            Neutralization.SECTOR,
            Neutralization.INDUSTRY,
            Neutralization.SUBINDUSTRY,
        ]
        stat_neu = [
            Neutralization.REVERSION_AND_MOMENTUM,
            Neutralization.CROWDING,
            Neutralization.FAST,
            Neutralization.SLOW,
            Neutralization.SLOW_AND_FAST,
        ]
        match self:
            case Region.USA:
                return [*basic_neu, *stat_neu, Neutralization.STATISTICAL]
            case Region.GLB | Region.EUR | Region.ASI:
                return [*basic_neu, *stat_neu, Neutralization.STATISTICAL, Neutralization.COUNTRY]
            case Region.CHN | Region.IND:
                return [*basic_neu, *stat_neu]
            case _:
                raise ValueError(f"Region {self} not supported")

class Universe(enum.StrEnum):
    TOP3000 = "TOP3000"
    TOPDIV3000 = "TOPDIV3000"
    TOP2500 = "TOP2500"
    TOP2000U = "TOP2000U"
    TOP1200 = "TOP1200"
    TOP1000 = "TOP1000"
    TOP800 = "TOP800"
    TOP500 = "TOP500"
    TOPSP500 = "TOPSP500"
    TOP400 = "TOP400"
    TOP200 = "TOP200"
    ILLIQUID_MINVOL1M = "ILLIQUID_MINVOL1M"
    MINVOL1M = "MINVOL1M"
    TOPCS1600 = "TOPCS1600"

class Category(enum.StrEnum):
    PRICE_REVERSION = "PRICE_REVERSION"
    PRICE_MOMENTUM = "PRICE_MOMENTUM"
    VOLUME = "VOLUME"
    FUNDAMENTAL = "FUNDAMENTAL"
    ANALYST = "ANALYST"
    PRICE_VOLUME = "PRICE_VOLUME"
    RELATION = "RELATION"
    SENTIMENT = "SENTIMENT"

class Neutralization(enum.StrEnum):
    NONE = "NONE"
    REVERSION_AND_MOMENTUM = "REVERSION_AND_MOMENTUM"
    STATISTICAL = "STATISTICAL"
    CROWDING = "CROWDING"
    FAST = "FAST"
    SLOW = "SLOW"
    MARKET = "MARKET"
    SECTOR = "SECTOR"
    INDUSTRY = "INDUSTRY"
    SUBINDUSTRY = "SUBINDUSTRY"
    SLOW_AND_FAST = "SLOW_AND_FAST"
    COUNTRY = "COUNTRY"

class Switch(enum.StrEnum):
    ON = "ON"
    OFF = "OFF"

class ComponentActivation(enum.StrEnum):
    IS = "IS"
    OS = "OS"

class UnitHandling(enum.StrEnum):
    VERIFY = "VERIFY"

class Color(enum.StrEnum):
    RED = "RED"
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    GREEN = "GREEN"
    PURPLE = "PURPLE"

class Grade(enum.StrEnum):
    AVERAGE = "AVERAGE"
    GOOD = "GOOD"
    EXCELLENT = "EXCELLENT"
    SPECTACULAR = "SPECTACULAR"
    NEEDIMPROVMENT = "NEEDIMPROVMENT"

class Stage(enum.StrEnum):
    IS = "IS"
    OS = "OS"

class SelectionHandling(enum.StrEnum):
    POSITIVE = "POSITIVE"
    NON_ZERO = "NON_ZERO"
    NON_NAN = "NON_NAN"

class ResponseStatus(enum.StrEnum):
    SUCCESS = "SUCCESS"
    LOGIN_FAILED = "LOGIN_FAILED"
    TRY_LATER = "TRY_LATER"
    BAD_REQUEST = "BAD_REQUEST"

class HTTPMethod(enum.StrEnum):
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    GET_LATER = "GET_LATER"

class FieldType(enum.StrEnum):
    GROUP = "GROUP"
    VECTOR = "VECTOR"
    MATRIX = "MATRIX"
    OTHER = "OTHER"

class OpScope(enum.StrEnum):
    REGULAR = "REGULAR"
    SELECTION = "SELECTION"
    COMBO = "COMBO"

class OpType(enum.StrEnum):
    ARITHMETIC = "ARITHMETIC"
    LOGICAL = "LOGICAL"
    TIMESERIES = "TIMESERIES"
    CROSS_SECTIONAL = "CROSS_SECTIONAL"
    VECTOR = "VECTOR"
    TRANSFORM = "TRANSFORM"
    GROUP = "GROUP"
    SELECTION = "SELECTION"
    COMBO = "COMBO"

class SimulationType(enum.StrEnum):
    REGULAR = "REGULAR"
    SUPER = "SUPER"

class TimeStampMixin:
    """本地时间戳 Mixin"""

    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_at = fields.DatetimeField(auto_now=True, description="更新时间")

class ExternalIDMixin:
    """外部主键 Mixin"""

    id = fields.CharField(max_length=16, primary_key=True)

class AlphaStatusMixin:
    """因子状态 Mixin"""

    status = fields.CharEnumField(Status, description="因子状态")
    stage = fields.CharEnumField(Stage, description="因子阶段")
    date_created = fields.DatetimeField(description="创建日期")
    date_modified = fields.DatetimeField(description="修改日期")
    date_submitted = fields.DatetimeField(description="提交日期", null=True)
    deprecated = fields.BooleanField(description="是否弃用", default=False)

    classifications = fields.JSONField(description="分类", default=list)
    competitions = fields.JSONField(description="比赛", null=True)
    themes = fields.JSONField(description="主题", null=True)
    pyramids = fields.JSONField(description="金字塔", null=True)
    pyramid_themes = fields.JSONField(description="金字塔主题", null=True)
    team = fields.JSONField(description="团队", null=True)

    start_date = fields.DateField(description="开始日期")
    end_date = fields.DateField(description="结束日期")

class AlphaSettingsMixin:
    """回测设置 Mixin"""

    instrument = fields.CharEnumField(Instrument, description="投资工具", default=Instrument.EQUITY)
    language = fields.CharEnumField(Language, description="因子语言", default=Language.FASTEXPR)
    region = fields.CharEnumField(Region, description="投资区域")
    universe = fields.CharEnumField(Universe, description="投资范围")
    delay = fields.IntField(description="Delay", ge=0, le=1)
    decay = fields.IntField(description="Decay", ge=0)
    neutralization = fields.CharEnumField(Neutralization, description="中性化策略")
    truncation = fields.FloatField(description="权重截断", gt=0, le=1)
    pasteurization = fields.CharEnumField(Switch, description="池化", default=Switch.ON)
    unit_handling = fields.CharEnumField(UnitHandling, description="单位验证", default=UnitHandling.VERIFY)
    max_trade = fields.CharEnumField(Switch, description="流动性控制", default=Switch.OFF)
    max_position = fields.CharEnumField(
        Switch, description="最大仓位控制", default=Switch.OFF, db_default=Switch.OFF
    )
    nan_handling = fields.CharEnumField(Switch, description="空值处理", default=Switch.ON)
    visualization = fields.BooleanField(description="高级可视化", default=False)
    test_period = fields.CharField(description="测试期结构", max_length=64, default="P2Y6M", null=True)

class AlphaMarkingMixin:
    """因子标记 Mixin"""

    name = fields.CharField(description="名称", max_length=255, null=True, default=None)
    favorite = fields.BooleanField(description="标星", default=False)
    hidden = fields.BooleanField(description="隐藏", default=False)
    color = fields.CharEnumField(Color, description="颜色", null=True)
    category = fields.CharEnumField(Category, description="类别", null=True)
    tags = fields.JSONField(description="标签", default=list)
    osmosis_points = fields.IntField(description="因子点数", default=None, null=True)

class AlphaPerformanceMixin:
    """因子表现 Mixin"""

    is_pnl = fields.IntField(description="盈亏曲线")
    is_booksize = fields.IntField(description="交易规模")
    is_longcnt = fields.IntField(description="多头数量")
    is_shortcnt = fields.IntField(description="空头数量")
    is_turnover = fields.FloatField(description="成交额")
    is_returns = fields.FloatField(description="收益")
    is_drawdown = fields.FloatField(description="回撤")
    is_margin = fields.FloatField(description="利润")
    is_sharpe = fields.FloatField(description="夏普率")
    is_fitness = fields.FloatField(description="因子评分")
    is_startdate = fields.DateField(description="开始日期")
    is_others = fields.JSONField(description="中性化表现", default=list)
    is_checks = fields.JSONField(description="提交检查器", default=list)

class AlphaRawMixin:
    """因子原始内容 Mixin"""

    record_raw = fields.JSONField(description="因子明细原始数据", null=False, default=None)
    pnl_raw = fields.JSONField(description="盈亏明细", null=True, default=None)
    self_corr_raw = fields.JSONField(description="自相关", null=True, default=None)
    prod_corr_raw = fields.JSONField(description="生产相关性", null=True, default=None)
    combine_perf_raw = fields.JSONField(description="提交前后表现", null=True, default=None)
    yearly_stats_raw = fields.JSONField(description="年度统计", null=True, default=None)

class AlphaComputedMixin:
    """因子计算属性"""

    self_corr = fields.FloatField(description="本地自相关性", null=True, default=None)
    prod_corr = fields.FloatField(description="生产相关性", null=True, default=None)

class HashcodeMixin:
    """自动哈希 Mixin"""

    __hashkey__: list[str] = []
    hashcode = fields.CharField(max_length=512, db_index=True)

    def hashing(self) -> str:
        keys = getattr(self.__class__, "__hashkey__", [])
        parts = [
            str(getattr(self, k, "|")).lower()
            if isinstance(getattr(self, k, "|"), bool)
            else str(getattr(self, k, "|"))
            for k in keys
        ]
        encode = "".join(parts)
        return hashlib.md5(encode.encode("utf-8")).hexdigest()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        async def _pre_save(
            sender: type[Model],
            instance: Model,
            using_db: Any,
            update_fields: list[str],
        ) -> None:
            if not isinstance(instance, cls):
                return
            instance.hashcode = instance.hashing()

        signals.pre_save(cls)(_pre_save)

class ExternalModel(Model, TimeStampMixin, ExternalIDMixin):
    class Meta:
        abstract = True

class LocalModel(Model, TimeStampMixin, HashcodeMixin):
    class Meta:
        abstract = True

    def __str__(self) -> str:
        hashcode = self.hashing()
        return f"{self.__class__.__name__}({getattr(self, 'hashcode') or hashcode})"

class AlphaCore(
    ExternalModel,
    AlphaRawMixin,
    AlphaSettingsMixin,
    AlphaPerformanceMixin,
    AlphaStatusMixin,
    AlphaMarkingMixin,
    AlphaComputedMixin,
):
    class Meta:
        abstract = True

    @classmethod
    def get_kv_from_record(cls, record: dict) -> dict:
        return {
            "id": record["id"],
            "status": Status(record["status"]),
            "stage": Stage(record["stage"]),
            "date_created": datetime.fromisoformat(record["dateCreated"]),
            "date_modified": datetime.fromisoformat(record["dateModified"]),
            "date_submitted": datetime.fromisoformat(record["dateSubmitted"])
            if record["dateSubmitted"]
            else None,
            "instrument": Instrument(record["settings"]["instrumentType"]),
            "language": Language(record["settings"]["language"]),
            "region": Region(record["settings"]["region"]),
            "universe": Universe(record["settings"]["universe"]),
            "delay": record["settings"]["delay"],
            "decay": record["settings"]["decay"],
            "neutralization": Neutralization(record["settings"]["neutralization"]),
            "truncation": record["settings"]["truncation"],
            "pasteurization": Switch(record["settings"]["pasteurization"]),
            "unit_handling": UnitHandling(record["settings"]["unitHandling"]),
            "nan_handling": Switch(record["settings"]["nanHandling"]),
            "max_trade": Switch(record["settings"]["maxTrade"]),
            "visualization": record["settings"]["visualization"],
            "start_date": date.fromisoformat(record["settings"]["startDate"]),
            "end_date": date.fromisoformat(record["settings"]["endDate"]),
            "test_period": record["settings"].get("testPeriod"),
            "name": record["name"],
            "favorite": record["favorite"],
            "hidden": record["hidden"],
            "color": Color(record["color"]) if record["color"] else None,
            "category": Category(record["category"]) if record["category"] else None,
            "tags": record["tags"],
            "classifications": record["classifications"],
            "competitions": record["competitions"],
            "themes": record["themes"],
            "pyramids": record["pyramids"],
            "pyramid_themes": record["pyramidThemes"],
            "team": record["team"],
            "osmosis_points": record["osmosisPoints"],
            "is_pnl": record["is"]["pnl"],
            "is_booksize": record["is"]["bookSize"],
            "is_longcnt": record["is"]["longCount"],
            "is_shortcnt": record["is"]["shortCount"],
            "is_turnover": record["is"]["turnover"],
            "is_returns": record["is"]["returns"],
            "is_drawdown": record["is"]["drawdown"],
            "is_margin": record["is"]["margin"],
            "is_sharpe": record["is"]["sharpe"],
            "is_fitness": record["is"]["fitness"] or 0,
            "is_startdate": date.fromisoformat(record["is"]["startDate"]),
            "is_others": {},
            "is_checks": {
                check_["name"]: {k: v for k, v in check_.items() if k != "name"}
                for check_ in record["is"]["checks"]
            },
            "record_raw": record,
        }

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({getattr(self, 'id')}|{self.is_sharpe})"

    @property
    def checkable(self) -> bool:
        return not bool(list(filter(lambda x: x["result"] == "FAIL", self.is_checks.values())))

class User(ExternalModel):
    username = fields.CharField(max_length=32, description="用户名")
    password = fields.CharField(max_length=32, description="密码")
    permissions = fields.JSONField(default=list, description="帐户权限")
    cookie = fields.CharField(max_length=320, null=True, description="登陆令牌")
    expiry = fields.FloatField(description="令牌时效")

class RegularAlpha(AlphaCore):
    user = fields.ForeignKeyField("niffler.User", related_name="regular_alphas")
    expr = fields.TextField(description="因子表达式")
    description = fields.TextField(description="因子描述", null=True)
    operator_count = fields.IntField(description="操作符数", null=True)

    @classmethod
    def from_record(cls, record: dict) -> Self:
        assert record["type"] == "REGULAR", "因子类型错误"
        kv = cls.get_kv_from_record(record)
        kv = {
            **kv,
            **{
                "user_id": record["author"],
                "expr": record["regular"]["code"],
                "description": record["regular"]["description"],
                "operator_count": record["regular"]["operatorCount"],
            },
        }
        return cls(**kv)

    @classmethod
    def get_keys_from_record(cls, record: dict) -> list[str]:
        return list(cls.get_kv_from_record(record).keys()) + [
            "expr",
            "description",
            "user_id",
            "operator_count",
        ]

    def to_description(self) -> dict:
        return {
            "category": self.category.value if self.category is not None else None,
            "regular": {"description": self.description},
            "color": self.color.value if self.color is not None else None,
            "name": self.name,
            "tags": self.tags,
            "hidden": self.hidden,
            "favorite": self.favorite,
            "osmosisPoints": self.osmosis_points,
        }

    def to_simulation(self) -> dict:
        return {
            "simulation_type": SimulationType.REGULAR,
            "region": self.region,
            "universe": self.universe,
            "delay": self.delay,
            "decay": self.decay,
            "truncation": self.truncation,
            "pasteurization": self.pasteurization,
            "max_trade": self.max_trade,
            "nan_handling": self.nan_handling,
            "visualization": self.visualization,
            "test_period": self.test_period,
            "neutralization": self.neutralization,
            "name": self.name,
            "tags": self.tags,
            "expr": self.expr,
            "description": self.description,
        }

    @property
    def checkable_ra(self) -> bool:
        return not bool(list(filter(lambda x: x["result"] == "FAIL", self.is_checks.values())))

class SuperAlpha(AlphaCore):
    user = fields.ForeignKeyField("niffler.User", related_name="super_alphas")
    combo = fields.TextField(description="因子表达式-组合")
    selection = fields.TextField(description="因子表达式-选择")

    selection_limit = fields.IntField(description="选择限制", ge=10)
    selection_handling = fields.CharEnumField(SelectionHandling, description="选择处理")
    component_activation = fields.CharEnumField(
        ComponentActivation, description="组件激活", default=ComponentActivation.IS
    )

    description_combo = fields.TextField(description="描述-组合", null=True)
    description_selection = fields.TextField(description="描述-选择", null=True)
    operator_count_combo = fields.IntField(description="操作符数-组合", null=True)
    operator_count_selection = fields.IntField(description="操作符数-选择", null=True)

    @classmethod
    def from_record(cls, record: dict) -> Self:
        assert record["type"] == "SUPER", "因子类型错误"
        kv = cls.get_kv_from_record(record)
        kv = {
            **kv,
            **{
                "user_id": record["author"],
                "combo": record["combo"]["code"],
                "selection": record["selection"]["code"],
                "selection_handling": SelectionHandling(record["settings"]["selectionHandling"]),
                "selection_limit": record["settings"]["selectionLimit"],
                "component_activation": ComponentActivation(record["settings"]["componentActivation"]),
                "description_combo": record["combo"]["description"],
                "description_selection": record["selection"]["description"],
                "operator_count_combo": record["combo"]["operatorCount"],
                "operator_count_selection": record["selection"]["operatorCount"],
            },
        }
        return cls(**kv)

    @classmethod
    def get_keys_from_record(cls, record: dict) -> list[str]:
        return list(cls.get_kv_from_record(record).keys()) + [
            "combo",
            "selection",
            "user_id",
            "selection_handling",
            "selection_limit",
            "component_activation",
            "description_combo",
            "description_selection",
            "operator_count_combo",
            "operator_count_selection",
        ]

    def to_description(self) -> dict:
        payload = {
            "name": self.name,
            "color": self.color.value if self.color is not None else None,
            "tags": self.tags,
            "category": self.category.value if self.category is not None else None,
            "regular": {"description": None},
            "favorite": self.favorite,
            "osmosisPoints": self.osmosis_points,
        }
        if self.description_combo is not None:
            payload["combo"] = {"description": self.description_combo}
        if self.description_selection is not None:
            payload["selection"] = {"description": self.description_selection}
        return payload

    def to_simulation(self) -> dict:
        return {
            "simulation_type": SimulationType.SUPER,
            "region": self.region,
            "universe": self.universe,
            "delay": self.delay,
            "decay": self.decay,
            "truncation": self.truncation,
            "pasteurization": self.pasteurization,
            "max_trade": self.max_trade,
            "nan_handling": self.nan_handling,
            "visualization": self.visualization,
            "test_period": self.test_period,
            "neutralization": self.neutralization,
            "name": self.name,
            "tags": self.tags,
            "combo": self.combo,
            "selection": self.selection,
            "description": self.description,
            "selection_limit": self.selection_limit,
            "selection_handling": self.selection_handling,
            "component_activation": self.component_activation,
            "description_combo": self.description_combo,
            "description_selection": self.description_selection,
        }

class AlphaSet(LocalModel):
    __hashkey__ = [
        "user_id",
        "alpha_type",
        "region",
        "universe",
        "delay",
        "date_from",
        "date_to",
        "sharpe_from",
        "sharpe_to",
        "fitness_from",
        "fitness_to",
        "status",
        "tag",
        "name",
        "category",
        "color",
        "hidden",
    ]

    user = fields.ForeignKeyField("niffler.User", related_name="alphasets")
    alpha_ids = fields.JSONField(description="因子集", default=list)
    n_regular = fields.IntField(description="因子集大小(Regular)", default=0)
    n_super = fields.IntField(description="因子集大小(Super)", default=0)

    alpha_type = fields.CharEnumField(AlphaType, description="因子类型", null=True, default=None)
    region = fields.CharEnumField(Region, description="地区", null=True, default=None)
    universe = fields.CharEnumField(Universe, description=" Universe", null=True, default=None)
    delay = fields.IntField(description="延迟", null=True, default=None, ge=0, le=1)
    date_from = fields.DatetimeField(description="开始时间", null=True, default=None)
    date_to = fields.DatetimeField(description="结束时间", null=True, default=None)
    sharpe_from = fields.FloatField(description="最低夏普率", null=True, default=None)
    sharpe_to = fields.FloatField(description="最高夏普率", null=True, default=None)
    fitness_from = fields.FloatField(description="最低稳健性", null=True, default=None)
    fitness_to = fields.FloatField(description="最高稳健性", null=True, default=None)

    status = fields.CharEnumField(Status, description="状态", null=True, default=None)
    tag = fields.CharField(description="检索标签", null=True, default=None, max_length=256)
    name = fields.CharField(description="检索名称", null=True, default=None, max_length=256)
    category = fields.CharEnumField(Category, description="因子类别", null=True, default=None)
    color = fields.CharEnumField(Color, description="因子颜色", null=True, default=None)
    hidden = fields.BooleanField(description="隐藏因子", null=True, default=None)

    def to_params(self) -> dict:
        params: dict[str, Any] = {"order": "-is.fitness"}
        if self.alpha_type is not None:
            params["type"] = self.alpha_type.value
        if self.date_from is not None:
            params["dateCreated>"] = self.date_from.astimezone(ZoneInfo("America/New_York")).isoformat()
        if self.date_to is not None:
            params["dateCreated<"] = self.date_to.astimezone(ZoneInfo("America/New_York")).isoformat()
        if self.status is not None:
            params["status"] = self.status.value
        if self.delay is not None:
            params["delay"] = self.delay

        for setting, setting_s in zip(
            [self.region, self.universe],
            ["region", "universe"],
        ):
            if setting is not None:
                params[f"settings.{setting_s}"] = setting.value

        for is_value, is_value_s in zip(
            [self.sharpe_from, self.sharpe_to, self.fitness_from, self.fitness_to],
            ["sharpe>", "sharpe<", "fitness>", "fitness<"],
        ):
            if is_value is not None:
                params[f"is.{is_value_s}"] = is_value

        for info, info_s in zip([self.tag, self.name], ["tag", "name"]):
            if info is not None:
                params[info_s] = info

        for info, info_s in zip([self.color, self.category], ["color", "category"]):
            if info is not None:
                params[info_s] = info.value

        return params

    @property
    def is_frozen(self) -> bool:
        info = [self.status, self.tag, self.name, self.category, self.color, self.hidden]
        if len([i for i in info if i is not None]) > 0:
            return False
        elif self.date_to is None or self.updated_at is None or self.updated_at < self.date_to:
            return False
        else:
            return True

    def update_from_record(self, record: list) -> Self:
        ra_ids = [rcd["id"] for rcd in record if rcd["type"] == "REGULAR"]
        sa_ids = [rcd["id"] for rcd in record if rcd["type"] == "SUPER"]
        self.alpha_ids = ra_ids + sa_ids
        self.n_regular = len(ra_ids)
        self.n_super = len(sa_ids)
        return self

class Simulation(LocalModel, AlphaSettingsMixin, AlphaMarkingMixin):
    __hashkey__ = [
        "simulation_type",
        "expr",
        "combo",
        "selection",
        "instrument",
        "region",
        "universe",
        "decay",
        "delay",
        "neutralization",
        "truncation",
        "pasteurization",
        "unit_handling",
        "max_trade",
        "max_position",
        "language",
        "nan_handling",
        "visualization",
    ]

    simulation_type = fields.CharEnumField(SimulationType, description="回测类型")
    alpha_id = fields.CharField(default=None, null=True, max_length=64)
    simid = fields.CharField(default=None, null=True, max_length=64)

    expr = fields.TextField(description="因子表达式", null=True, default=None)
    combo = fields.TextField(description="因子表达式-组合", null=True, default=None)
    selection = fields.TextField(description="因子表达式-选择", null=True, default=None)

    selection_limit = fields.IntField(description="选择限制", ge=10, default=10)
    selection_handling = fields.CharEnumField(
        SelectionHandling, description="选择处理", default=SelectionHandling.NON_NAN
    )
    component_activation = fields.CharEnumField(
        ComponentActivation, description="组件激活", default=ComponentActivation.IS
    )

    description = fields.TextField(description="描述", null=True, default=None)
    description_combo = fields.TextField(description="描述-组合", null=True, default=None)
    description_selection = fields.TextField(description="描述-选择", null=True, default=None)

    def to_payload(self) -> dict:
        if self.simulation_type == SimulationType.REGULAR:
            return {
                "type": "REGULAR",
                "settings": {
                    "instrumentType": self.instrument.value,
                    "language": self.language.value,
                    "region": self.region.value,
                    "universe": self.universe.value,
                    "delay": self.delay,
                    "decay": self.decay,
                    "visualization": self.visualization,
                    "neutralization": self.neutralization.value,
                    "truncation": self.truncation,
                    "pasteurization": self.pasteurization.value,
                    "unitHandling": self.unit_handling.value,
                    "nanHandling": self.nan_handling.value,
                    "maxTrade": self.max_trade.value,
                    "maxPosition": self.max_position.value,
                    "testPeriod": self.test_period,
                },
                "regular": self.expr,
            }
        else:
            return {
                "type": "SUPER",
                "settings": {
                    "instrumentType": self.instrument.value,
                    "language": self.language.value,
                    "region": self.region.value,
                    "universe": self.universe.value,
                    "delay": self.delay,
                    "decay": self.decay,
                    "visualization": self.visualization,
                    "neutralization": self.neutralization.value,
                    "truncation": self.truncation,
                    "pasteurization": self.pasteurization.value,
                    "unitHandling": self.unit_handling.value,
                    "nanHandling": self.nan_handling.value,
                    "maxTrade": self.max_trade.value,
                    "maxPosition": self.max_position.value,
                    "selectionLimit": self.selection_limit,
                    "selectionHandling": self.selection_handling.value,
                    "componentActivation": self.component_activation.value,
                    "testPeriod": self.test_period,
                },
                "combo": self.combo,
                "selection": self.selection,
            }

```

接下来是代码解释

## 枚举定义

我们首先定义一组枚举，作用有三点：

1. 平台API交互涉及大量字符串，为了和平台下拉框、API 字符串一一对应，避免魔法字符串散落在业务代码里，我们把这些字符串声明为枚举。
2. `CharEnumField`  直接吃枚举类型，入库仍是字符串，读出来又是枚举，IDE 能补全。
3. 可以给一些枚举绑定方法，例如给 Region 绑定方法，可以获取 Region 对应的所有 Universe 和 Neutralization，写筛选条件时不用翻文档，提交任务时也可以用来校验。

涉及因子与回测的主要枚举包括： `AlphaType` 、 `Status` 、 `Language` 、 `Instrument` 、 `Region` 、 `Universe` 、 `Category` 、 `Neutralization` 、 `Switch` 、 `ComponentActivation` 、 `UnitHandling` 、 `Color` 、 `Grade` 、 `Stage` 、 `SelectionHandling` 、 `SimulationType`  等。

## 模型共享组件

### 时间戳与外部主键

- **`TimeStampMixin`** ： `created_at` （ `auto_now_add` ）、 `updated_at` （ `auto_now` ）自动时间戳
- **`ExternalIDMixin`** ： `id`  为  `CharField(max_length=16, primary_key=True)` ，与平台侧的 alpha id 一致，本地表不再自增整数主键。

### 因子共用字段（Regular / Super 都会用到）

按职责拆成多个 Mixin，全部叠在后面的抽象核心上：

Mixin
职责概要

 `AlphaStatusMixin` 
状态、阶段、各日期、弃用标记、分类/比赛/主题/金字塔等 JSON

 `AlphaSettingsMixin` 
instrument、language、region、universe、delay、decay、neutralization、truncation、pasteurization、unit_handling、max_trade、max_position、nan_handling、visualization、test_period

 `AlphaMarkingMixin` 
name、favorite、hidden、color、category、tags、osmosis_points

 `AlphaPerformanceMixin` 
IS 维度的 pnl、booksize、换手、收益、夏普、fitness、checks 等

 `AlphaRawMixin` 

 `record_raw`  存整包平台 JSON，以及 pnl / 自相关等原始明细 JSON

 `AlphaComputedMixin` 
本地二次计算字段，如  `self_corr` 、 `prod_corr` 

这样 Super 与 Regular 只在自己类里追加差异不分，其余列结构一致，后续修改方便（例如最近新增的 MaxPosition 只需要给 AlphaSettingMixin 新增一个字段，所有的本地因子都自动获得该属性）。

### 基础抽象模型

- **`ExternalModel`** ： `Model`  +  `TimeStampMixin`  +  `ExternalIDMixin` ， `abstract = True` 。所有带平台ID的实体从这里派生，例如  `User` 、RegularAlpha、SuperAlpha。
- **`LocalModel`** ： `Model`  +  `TimeStampMixin`  +  `HashcodeMixin` ， `abstract = True` 。主键不是平台 id、本地保存的对象，例如后面的  `AlphaSet` 、 `Simulation` 。

### HashcodeMixin：本地去重与索引🌟

这个组件帮助大家解决一个核心痛点：回测时如何跳过已经回测过的因子？

这个组件里定义了类属性  `__hashkey__` ：这里面的键会作为模型的唯一参数来计算模型哈希值，而在我们的因子库里，哈希值可以设置成唯一的。

（但我实际上没有设计成唯一的，而是在使用的时候检查哈希值是否存在的方式手动控制重复性）

## 抽象核心：AlphaCore

**`AlphaCore`**  继承  `ExternalModel` ，并混入上述所有 Alpha 相关 Mixin， `Meta.abstract = True` 。它是 Regular / Super 的公共父类，本身不对应单独一张业务表。

值得单独说的几个点：

1. **`get_kv_from_record(record: dict)`**
   类方法，把平台返回的一条 alpha 记录（字典）转换成 Tortoise 构造函数可用的扁平  `kwargs` ：这里你可以直接把平台API接口返回的JSON对象胃进来，通过时间戳自动转换，帮助我们解决了国际时区的痛点
2. **`checkable`  属性**
   扫  `is_checks`  里是否出现  `result == "FAIL"` ，用于快速判断是否满足提交前检查，当is_checks 是 True 时，平台上的 Check 是绿的，帮助我们解决又一个痛点
3. **`__str__`**
   打印类名、平台  `id`  和  `is_sharpe` ，日志里好辨认。

## 具体模型（每张表一类）

### User

继承  `ExternalModel` 。存用户名、密码、权限列表、登录 cookie 与过期时间等账号维度的字段。

### RegularAlpha 与 SuperAlpha

二者都继承  `AlphaCore` ，区别在平台类型与代码字段

### AlphaSet

继承  `LocalModel` ，带完整的  `__hashkey__` （用户、因子类型、地区、universe、delay、时间范围、夏普与 fitness 区间、状态、标签、名称、类别、颜色、是否隐藏等）。

- `alpha_ids` 、 `n_regular` 、 `n_super`  保存结果集统计；
- `to_params()`  把条件转成平台列表接口的 query 参数（含美东时区下的  `dateCreated`  边界）；
- `is_frozen`  判断该快照是否还可视为已冻结；
- `update_from_record`  从原始 record 列表拆出 Regular / Super 的 id。

为什么要设计这么个对象？当我们从平台检索大量因子时（例如我要看近一年所有美区的已模拟因子）非常耗时，但对于某些检索条件，其结果是已冻结的（就是不会改变，例如我要看 3月20～3月21日的Sharpe>1.5的USA因子，由于今天已经过了 3月21，且因子的Sharpe是固定的，所以这个检索条件的结果永远都是固定的，就是已冻结）我们就可以通过本地缓存快速获取，节省大量时间（尤其是每天要挑选交什么因子的时候。

### Simulation

继承  `LocalModel` ，并混入  `AlphaSettingsMixin`  与  `AlphaMarkingMixin。`

该对象增加了 `to_payload()`  ，可以直接输出回测用的 JSON Payload。

## 使用案例

将上面的代码放到  [`brain.py`]([链接已屏蔽])  文件内，然后另开一个 Jupyter：

```
import brain

from tortoise import Tortoise

ctx = await Tortoise.init(
    config={
        "connections": {"default": "sqlite://./db.sqlite"},
        "apps": {
            "niffler": {
                "models": ["brain"],
                "default_connection": "default",
            }
        },
        "use_tz": True,
        "timezone": "Asia/Shanghai",
    },
    _enable_global_fallback=True,
)

_ = await Tortoise.generate_schemas(safe=True)

```

只需要执行以上代码，你就可以生成一个基于 SQLite 的本地因子库。

看到这里你可能会有疑问，现在我有了本地因子库了，如何使用呢？（创建因子、获取因子）接下来你需要

1. 可以去研究一下 Tortoise 语法，学习一下如何操作Models，然后再结合进自己的工作流中
2. 将 Tortoise 语法包装成高级接口

我正在马不停蹄的撰写下一篇文章：BuildYourOwnClient，手把手教大家包装一个高级 Client，这里可以给点预告：

```
class MyClient:
    # ...    

    # 获取 Alpha
    # 如果 Alpha 在本地因子库，则直接拉取，如果Alpha不在，则尝试获取远程
    async def get_alpha(self, alpha_id: str, force: bool = False) -> RegularAlpha | SuperAlpha:
        if not force:
            ra = await RegularAlpha.get_or_none(id=alpha_id)
            sa = await SuperAlpha.get_or_none(id=alpha_id)
            if ra is not None:
                # self._logger.debug(f"读取本地 RA: {ra}")
                return ra
            if sa is not None:
                # self._logger.debug(f"读取本地 SA: {sa}")
                return sa
        rcd = await self.get(url=self._config.platform.alpha_info.format(alpha_id=alpha_id))
        assert isinstance(rcd, dict), "获取因子失败"
        if rcd["type"] == "SUPER":
            alpha = SuperAlpha.from_record(rcd)
            keys = SuperAlpha.get_keys_from_record(rcd)
            alpha_batch = await self.batch_update_or_create(
                [alpha], SuperAlpha, [k for k in keys if k not in ["id"]]
            )
        elif rcd["type"] == "REGULAR":
            alpha = RegularAlpha.from_record(rcd)
            keys = RegularAlpha.get_keys_from_record(rcd)
            alpha_batch = await self.batch_update_or_create(
                [alpha], RegularAlpha, [k for k in keys if k not in ["id"]]
            )
        else:
            raise ValueError(f"alpha type {rcd['type']} not supported")
        alpha_get = alpha_batch[0]
        self._logger.debug(f"在线加载因子: {alpha_get}")
        return alpha_get

```

求赞求赞

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
已经让ai学习了这篇帖子，完成了代码的修改。

感谢分享，数据库是提高产出alpha效率的有效途径，各位新人早点用起来，用熟练，避免像我这样人工低效的耗费时间。

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================


---

### 技术对话片段 44 (原帖: 【SuperAlpha灵感】因子择时模型Alpha Template)
- **原帖链接**: [Commented] 【SuperAlpha灵感】因子择时模型Alpha Template.md
- **时间**: 1年前

**提问/主帖背景 (YW93864)**:
**文献参考：**

**1. 《** 基于趋势和拐点的市值因子择时模型》

**概述：** 本贴将该报告中的精华部分摘出来，结合Brain提供的字段，供大家在SAC比赛时使用。本文主要参考了十类拥挤度指标介绍，并将可以在Brain上使用的 **动量之差、成交额之比、波动率之比和配对相关性之差** 进行了一些简化及复现。

**提示：**

**1.** 本贴的逻辑和研报逻辑不同。主要是因为前提假设是Brain上的alpha均是具备正向预测能力，而报告中的市值因子是可以存在下跌的情况的。换而言之，Brain上的alpha尽量不要做空（因为可能出现的情况是短期大幅失效、长期小幅稳定有效，如果为了一些极端事件去调整，那很容易出现过拟合），而市值因子可以做空，以上是前提假设。

**2.** 在该假设的基础上，不建议不交易某个alpha或者配负向的权重，因此传统的择时因子框架可能不起效果。具体来说：在制作择时因子时，我们会使用门限测试（像报告中提到那样），首先对时序因子进标准化，时序标准化可以使用ts_zscore或者ts_rank，我们这里为了方便使用ts_rank，如果当前rank大于0.9，我们认为这个信号非常强烈，所以我们会进行开仓；做空时也一样，如果rank小于0.1，我们认为负向信号非常强烈，我们会进行做空。由于前提假设为Brain上的alpha都是具备正向预测能力的，所以不建议使用这类的表达式，假设我们通过因子动量筛选

```
stats = generate_stats(alpha);alpha_mom = ts_sum(stats.returns,60);mom_rank = ts_rank(alpha_mom,500);if_else(mom_rank>0.9,1,if_else(mom_rank<0.1,-1,0))
```

这样虽然符合一般择时因子的逻辑，但在一堆有正向预测能力的alpha中不推荐这样做。

**3.**   **1和2我经过了大量的测试，保证结果在一定程度上合理（以上结论会和select到的不同alpha池有关联，不同的alpha池具备不同的表现，可能会使上述结果不成立）；因此，后文提供了连续性的赋值方式**

**4.**  因子择时和择时因子不是一回事，前者是对“因子”这类对象进行择时（赋权），后者强调了“择时”这种方法，媒介是“因子”。将思路嫁接到Combo上，我们需要制作新的combo表达式（择时因子）对alpha（每个alpha可以视为一个投资标的）进行择时

**5** . 本文仅提供一些思路，笔者也在不断摸索。本文的表达式不一定能beat等权组合，SA最重要的是如何Select，其次才是在Combo表达式。选到的alpha质量决定着SA的下限，而Combo只能起到锦上添花的作用。

**6.** 本文后续介绍到的combo表达式部分逻辑和研报有差异，这是在预期内的。根据每个alpha池的性质不同，呈现的结果会有差异。正如动量因子在USA是正向的，在CHN是反向的。

**正文：**

**1. 因子动量**

预期假设：过去一段时间表现较好的alpha，在未来也会更好。(这里选用了)

```
stats = generate_stats(alpha);mom = ts_ir(stats.returns,60);ts_rank(mom,500)
```

**2. 因子成交额之比**

预期假设：过去一段时间交易额过多的alpha，说明alpha所对应的标的关注较多，关注较多时可以相当于“有效市场”，其中的利润很难赚取，那么alpha的预测能力的衰减就会加重。

```
tv = ts_mean(stats.trade_value,60);tv_crowd = tv/ts_delay(tv,60);ts_rank(-tv_crowd,500)
```

**3.因子波动率之比**

预期假设：过去一段时间波动率较大的alpha，不够稳健。

```
std = ts_std_dev(stats.returns,60);std_crowd = std /ts_delay(std,60);ts_rank(-std_crowd ,500)
```

**4. 相关性**

预期假设：选出过去一段时间相关性更小的alpha

```
ic = self_corr(stats.returns,60);inneric = if_else(ic==1,nan,ic);ts_rank(-reduce_min(inneric),500)
```

以上还能衍生出更多的变体，会有一定提升，大家可以多加尝试。

最主要的还是选出独特的、高质量的alpha池，并且尽可能使用多的alpha，以此基础上尝试一些combo

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
您的每一个帖子都认真拜读，很佩服您的研报复现能力，

最近一直在学习周期的概念，您提到的因子成交额的观点，受益良多。感谢分享！

---------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 45 (原帖: 【SuperAlpha灵感】因子择时模型Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】因子择时模型Alpha Template_32553007626007.md
- **时间**: 1年前

**提问/主帖背景 (YW93864)**:
**文献参考：**

**1. 《** 基于趋势和拐点的市值因子择时模型》

**概述：** 本贴将该报告中的精华部分摘出来，结合Brain提供的字段，供大家在SAC比赛时使用。本文主要参考了十类拥挤度指标介绍，并将可以在Brain上使用的 **动量之差、成交额之比、波动率之比和配对相关性之差** 进行了一些简化及复现。

**提示：**

**1.** 本贴的逻辑和研报逻辑不同。主要是因为前提假设是Brain上的alpha均是具备正向预测能力，而报告中的市值因子是可以存在下跌的情况的。换而言之，Brain上的alpha尽量不要做空（因为可能出现的情况是短期大幅失效、长期小幅稳定有效，如果为了一些极端事件去调整，那很容易出现过拟合），而市值因子可以做空，以上是前提假设。

**2.** 在该假设的基础上，不建议不交易某个alpha或者配负向的权重，因此传统的择时因子框架可能不起效果。具体来说：在制作择时因子时，我们会使用门限测试（像报告中提到那样），首先对时序因子进标准化，时序标准化可以使用ts_zscore或者ts_rank，我们这里为了方便使用ts_rank，如果当前rank大于0.9，我们认为这个信号非常强烈，所以我们会进行开仓；做空时也一样，如果rank小于0.1，我们认为负向信号非常强烈，我们会进行做空。由于前提假设为Brain上的alpha都是具备正向预测能力的，所以不建议使用这类的表达式，假设我们通过因子动量筛选

```
stats = generate_stats(alpha);alpha_mom = ts_sum(stats.returns,60);mom_rank = ts_rank(alpha_mom,500);if_else(mom_rank>0.9,1,if_else(mom_rank<0.1,-1,0))
```

这样虽然符合一般择时因子的逻辑，但在一堆有正向预测能力的alpha中不推荐这样做。

**3.**   **1和2我经过了大量的测试，保证结果在一定程度上合理（以上结论会和select到的不同alpha池有关联，不同的alpha池具备不同的表现，可能会使上述结果不成立）；因此，后文提供了连续性的赋值方式**

**4.**  因子择时和择时因子不是一回事，前者是对“因子”这类对象进行择时（赋权），后者强调了“择时”这种方法，媒介是“因子”。将思路嫁接到Combo上，我们需要制作新的combo表达式（择时因子）对alpha（每个alpha可以视为一个投资标的）进行择时

**5** . 本文仅提供一些思路，笔者也在不断摸索。本文的表达式不一定能beat等权组合，SA最重要的是如何Select，其次才是在Combo表达式。选到的alpha质量决定着SA的下限，而Combo只能起到锦上添花的作用。

**6.** 本文后续介绍到的combo表达式部分逻辑和研报有差异，这是在预期内的。根据每个alpha池的性质不同，呈现的结果会有差异。正如动量因子在USA是正向的，在CHN是反向的。

**正文：**

**1. 因子动量**

预期假设：过去一段时间表现较好的alpha，在未来也会更好。(这里选用了)

```
stats = generate_stats(alpha);mom = ts_ir(stats.returns,60);ts_rank(mom,500)
```

**2. 因子成交额之比**

预期假设：过去一段时间交易额过多的alpha，说明alpha所对应的标的关注较多，关注较多时可以相当于“有效市场”，其中的利润很难赚取，那么alpha的预测能力的衰减就会加重。

```
tv = ts_mean(stats.trade_value,60);tv_crowd = tv/ts_delay(tv,60);ts_rank(-tv_crowd,500)
```

**3.因子波动率之比**

预期假设：过去一段时间波动率较大的alpha，不够稳健。

```
std = ts_std_dev(stats.returns,60);std_crowd = std /ts_delay(std,60);ts_rank(-std_crowd ,500)
```

**4. 相关性**

预期假设：选出过去一段时间相关性更小的alpha

```
ic = self_corr(stats.returns,60);inneric = if_else(ic==1,nan,ic);ts_rank(-reduce_min(inneric),500)
```

以上还能衍生出更多的变体，会有一定提升，大家可以多加尝试。

最主要的还是选出独特的、高质量的alpha池，并且尽可能使用多的alpha，以此基础上尝试一些combo

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
您的每一个帖子都认真拜读，很佩服您的研报复现能力，

最近一直在学习周期的概念，您提到的因子成交额的观点，受益良多。感谢分享！

---------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 46 (原帖: 【工具推荐】zcf + Claude Code + GLM-4.6：低价也能实现优质效果！经验分享)
- **原帖链接**: [Commented] 【工具推荐】zcf  Claude Code  GLM-46低价也能实现优质效果经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (TD65874)**:
GLM-4.6是我目前使用过的所有AI中唯一提供‘真正’包月套餐的模型，和按token或者是‘假’包月的那些大模型相比，性价比可以说是相当高，但如果是直接使用GLM-4.6，据我使用感受而言，是比较一般的，所以，我们得搭配Claude Code来使用，这样才能达到很不错的效果。

然后在使用Claude Code的途中我又发现了一个好用的工具——zcf [GitHub - UfoMiao/zcf: Zero-Config Code Flow for Claude code & Codex]( [[链接已屏蔽])（零配置,一键搞定]([链接已屏蔽])%EF%BC%88%E9%9B%B6%E9%85%8D%E7%BD%AE,%E4%B8%80%E9%94%AE%E6%90%9E%E5%AE%9A)  Claude Code & Codex 环境设置 - 支持中英文双语配置、智能代理系统和个性化 AI 助手），非常适合搞不定Claude Code相关配置的朋友，具体操作非常简单：
### Step 1：安装 Node.js
zcf需要 Node 来跑，所以电脑没安装node的朋友请先安装一下node，官网：  [[链接已屏蔽])  ，官网下载自己系统的版本，安装之后在终端里输入：
```
node -v
npm -v
npx -v
```
能看到版本号，就说明成功了。
 
> [!NOTE] [图片 OCR 识别内容]
> PS C: |Users |10597> node
> CV
> V22.18.0
> Ps
> C: | Users |10597>
> npm
> CV
> 11
> 5.2
> PS C: |Users |10597>
> npX
> CV
> 11
> 5.2
> PS C: |Users |10597>


### Step 2：zcf 初始化
命令行中输入：`npx zcf` 打开交互式菜单，按需选择即可。
 
> [!NOTE] [图片 OCR 识别内容]
> C: | Users | 10597>npx
> ZCf
> Need
> to
> install
> the
> following packages
> ZCf@3
> 4.3
> Ok
> to proceed?
> Cy)
> E巳巨
> for
> Claude
> Code
> Zero-Config Code FLow
> Version:
> 3.4.3
> https : / /github . com /UfoMiao/zcf
> 请选择功能
> Claude Code
> 1
> 完整初始化
> 安装
> Claude Code
> 导入工作流
> 配置
> API 或
> CCR 代理
> 配置 MCP 服务
> 2
> 导入工作流
> 仅导入 /更新工作流相关文件
> 3
> 配置
> API 或
> CCR 代理
> 配置
> API
> URL
> 认证信息或
> CCR 代理
> 4.
> 配置
> MCP
> 配置
> MCP 服务 (含
> Windows 修复 )
> 5.
> 配置默认模型
> 设置默认模型 (opus/sonnet/sonnet Im/自定义)
> 6。
> 配置
> Claude 全局记忆
> 配置
> AI 输出语言和输出风格
> 7
> 导入推荐环境娈量和权限配置
> 导入隐私保护环境娈量和系统权限配置
> 其他工具
> R。
> CCR
> 配置
> Claude
> Code
> Router 以使用多个
> AI 模型
> U.
> CCusage
> Claude
> Code 用量分析
> 匕
> CCometixLine
> 基于
> Rust 的高性能
> Claude Code 状态栏工具, 集成 Git 信息和实时使用量跟踪
> ZCF
> 更改显示语言
> Select display language
> 更改
> ZCF 界面语言
> 5
> 切换代码工具
> 在支持的代码工具之间切换
> (Claude Code,
> Codex)
> 卸载和删除配置
> 从系统中删除
> Claude
> Code 配置和工具
> 检查更新
> 检查并更新
> Claude
> Code
> CCR 和
> CCometixLine 的版本
> @.
> 退出
> 请输入选项,回车确认 (不区分大小写)


### Step3：指定模型为GLM-4.6


> [!NOTE] [图片 OCR 识别内容]
> 「请输入选项 ,
> 回车确认 (不区分大小写)
> 3
> 请选择
> API 配置模式
> 2.
> 自定义
> API 配置
> Claude
> Code 配置管理
> 当前配置数量:
> 1
> 当前默认配置:  glm-test
> 请选择操作
> 1.
> 添加配置
> 2.
> 编辑配置
> 3.
> 复制配置
> 4.
> 删除配置
> 5.
> 跳过
> N navigate
> select
  
> [!NOTE] [图片 OCR 识别内容]
> [
> 请选择操作
> 1.
> 添加配置
> 添加新配置
> 「请选择
> API 供应商
> 4.
> GLN
> 己选择供应商:
> GLN
> 「配置名称 (仅限字母
> 数字
> 空格.
> '一)
> 9lm-4.6
> 请输入
> GLM 的
> API
> Key
 
选择供应商GLM，然后输入自己的GLM-4.6的api key即可。

这一步如果没有api key的朋友，可以通过我的**邀请链接**注册：
 [[链接已屏蔽]) 
或者直接进官网注册也可以：
 [[链接已屏蔽])

注册完之后，进入特惠专区：
 
> [!NOTE] [图片 OCR 识别内容]
> BigModel
> 特惠专区
> 大模型
> 应用空间
> 体验中心
> 价格
> 开发者 ~
> 企业
> 关于智谱
> 开发文档
> 控制台
> GLM Coding 跨年限时特惠
> 1/7价格.
> 3倍用量
> 适用Claude Code
> Cline
> 等主流编程工具
> GLM Coding
> 跨年特惠Coding套餐
> 邀好友赚赠金



> [!NOTE] [图片 OCR 识别内容]
> BigModel
> 我的编程套餐
> 接入编程工具 `
> 调AMCP
> 社区
> 常见问题
> API
> GLM Ioclimg pam:跨年特惠
> 12.08-01.15:
> 50% 首购立减 +额外节日限定优惠! 详细说明
> 全球顶尖编程模型 GLM-4.6 驱动
> GLM-4.6 发布时。在推理。代码和智能体能力等方面达到开
> 源模型 SOTA 水平
> Claude Sonnet 4.5
> 1387
> 无缝适配多种主流 Al 编程工具
> GLM 4.6
> 1372
> 超大容量
> 更低价格
> GPT 5.1
> 1364
> 免费享专属 MCP 
> 解锁高级能力
> 位列 Code Arena 榜单第一梯队
> 取自榜单更新时间 2025-11-22
> 首月享5折,
> 最高立省200元
> 琏续包月
> 连续包季
> -559
> 连续包年
> -609
 
订阅适合自己的套餐即可，订阅后点击右上角的API Key，然后创建api key并复制即可。

### Step4：开始使用
在按照zcf上面的步骤配置完成之后，我们先在控制台中cd到自己项目的地址，比如：`cd C:\Code\wqb` ，然后输入：`claude`，然后回车即可，如果出现如图所示的页面代表配置成功：
 
> [!NOTE] [图片 OCR 识别内容]
> Ps
> C: | Users |10597>
> cd
> C: | Code Iwqb
> Ps
> C: | Code'
> claude
> Claude
> Code
> V2.0.26
> Tips
> for getting started
> Welcome
> back !
> Run
> /init
> to
> Create
> CLAUDE .md
> file with
> instructions
> for Claude
> Recent
> activity
> No
> recent
> activity
> Sonnet
> 4.5
> API Usage Billing
> C: | Code|wqb
> Iy
> Iedit
> <filepath>
> to
> Sonnet
> 4.5
> main
> 0.6%
> 1.Ik tokens
> Thinking
> On
> Ctab
> to
> toggle)
> Wqb>
> Wqb
 
然后就可以正式使用了。

更多关于zcf的用法、参数与工作流说明可以查看文档： [ [[链接已屏蔽])]([链接已屏蔽]))

==然后补充一点，如果用不习惯Claude Code cli命令行工具的，可以去vscode中下载Claude Code插件：
 
> [!NOTE] [图片 OCR 识别内容]
> File
> Edit
> Selection
> View
> Go
> Run
> Terminal
> Help
> WQ-code [Administrator]
> 侣
> EXTENSIONS
> 田 Extension: Claude Code for VS Code X
> 米 凹
> Claude Code
> Search Extensions in Marketplace
> Past Conversations
> Claude Code for VS Code
> V2
> INSTALLED
> Cline
> Update
> Anthropic
> anthropiccom
> 2,335,422
> Claude Code
> CodellDB
> 13ms
> Claude Code for VS Code: Harness the power of Cla.
> Debugger for native code; powered by LLDB。
> Restart Extensions
> Disable
> Uninstall
> Auto Up
> Vadim Chugunov
> Update
> CICt +
> DETAILS
> FEATURES
> CICt +
> CICt + Intellisense; debugging, and code bro.
> Microsoft
> Restart Extensions
> Categories
> C# Dev Kit
> Claude Code for VS
> 0#
> Official C# extension
> Microsoft
> Chat
> Microsoft
> Restart Extensions
> Code
> Claude Code for VS Code
> ggms
> Resources
> Claude Code for VS Code: Harness the power
> Unleash Claude's raw power directly in your
> It's a beautiful
> to use the computer, don't
> Anthropic
> Restart Extensions
> terminal Search million-line codebases instantly。
> Marketplace
> you think?
> Turn hours-long workflows into a single
> Issues
> ESLint
> 31ms
> command. Your tools。 Your workflow. Your
> Anthropic
> ES
> Integrates ESLint JavaScript into VS Code。
> Uint
> codebase; evolving at thought speed。
> Microsoft
> Restart Extensions
> More Info
> Powerful intelligence: Use the latest
> Lua
> Lua Language Server coded by Lua
> Claude models using your Pro, Max; Team;
> Published 2025-06-19,
> Ua
> sumneko
> Restart Extensions
> OI
> Enterprise subscription; or pay-as
> 00:32:16
> go pricing
> Last
> 2025-12-18,
> Prefer the Terminal experience? Switch back in Settings。
> Lua Debug
> Works alongside you: Claude
> released
> 06:13:33
> Ua
> VSCode
> debugger extension for Lua
> autonomously explores
> codebase;
> Last
> 2025-12-18,
> ctrl esc to focus or unfocus Claude
> YOUT
> actboyl68
> Restart Extensions
> updated
> 15.01.48
> readsand writes code; and runs Term
> Identifier
> anthropic. claude
> Ask before edits
> alpha_searcher_use:ipynb
> Prettier
> Code formatter
> G1ms
> commands with your permission。
> Code
> Code formatter
> prettier
> Now ferhor mtorface that makes 汁
> from
> day
> JOU
> using


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我之前发给一个帖子关于iflow的，iflow有个人用户免费的api接口，也有glm-4.6模型，推荐给有需要的顾问。

---------------------------------------------------------------------------------

时间要花在有效率的地方

---------------------------------------------------------------------------------


---

### 技术对话片段 47 (原帖: 【工具推荐】zcf + Claude Code + GLM-4.6：低价也能实现优质效果！经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【工具推荐】zcf  Claude Code  GLM-46低价也能实现优质效果经验分享_37119934888599.md
- **时间**: 6个月前

**提问/主帖背景 (TD65874)**:
GLM-4.6是我目前使用过的所有AI中唯一提供‘真正’包月套餐的模型，和按token或者是‘假’包月的那些大模型相比，性价比可以说是相当高，但如果是直接使用GLM-4.6，据我使用感受而言，是比较一般的，所以，我们得搭配Claude Code来使用，这样才能达到很不错的效果。

然后在使用Claude Code的途中我又发现了一个好用的工具——zcf [GitHub - UfoMiao/zcf: Zero-Config Code Flow for Claude code & Codex]( [[链接已屏蔽])（零配置,一键搞定]([链接已屏蔽])%EF%BC%88%E9%9B%B6%E9%85%8D%E7%BD%AE,%E4%B8%80%E9%94%AE%E6%90%9E%E5%AE%9A)  Claude Code & Codex 环境设置 - 支持中英文双语配置、智能代理系统和个性化 AI 助手），非常适合搞不定Claude Code相关配置的朋友，具体操作非常简单：
### Step 1：安装 Node.js
zcf需要 Node 来跑，所以电脑没安装node的朋友请先安装一下node，官网：  [[链接已屏蔽])  ，官网下载自己系统的版本，安装之后在终端里输入：
```
node -v
npm -v
npx -v
```
能看到版本号，就说明成功了。
 
> [!NOTE] [图片 OCR 识别内容]
> PS C: |Users |10597> node
> CV
> V22.18.0
> Ps
> C: | Users |10597>
> npm
> CV
> 11
> 5.2
> PS C: |Users |10597>
> npX
> CV
> 11
> 5.2
> PS C: |Users |10597>


### Step 2：zcf 初始化
命令行中输入：`npx zcf` 打开交互式菜单，按需选择即可。
 
> [!NOTE] [图片 OCR 识别内容]
> C: | Users | 10597>npx
> ZCf
> Need
> to
> install
> the
> following packages
> ZCf@3
> 4.3
> Ok
> to proceed?
> Cy)
> E巳巨
> for
> Claude
> Code
> Zero-Config Code FLow
> Version:
> 3.4.3
> https : / /github . com /UfoMiao/zcf
> 请选择功能
> Claude Code
> 1
> 完整初始化
> 安装
> Claude Code
> 导入工作流
> 配置
> API 或
> CCR 代理
> 配置 MCP 服务
> 2
> 导入工作流
> 仅导入 /更新工作流相关文件
> 3
> 配置
> API 或
> CCR 代理
> 配置
> API
> URL
> 认证信息或
> CCR 代理
> 4.
> 配置
> MCP
> 配置
> MCP 服务 (含
> Windows 修复 )
> 5.
> 配置默认模型
> 设置默认模型 (opus/sonnet/sonnet Im/自定义)
> 6。
> 配置
> Claude 全局记忆
> 配置
> AI 输出语言和输出风格
> 7
> 导入推荐环境娈量和权限配置
> 导入隐私保护环境娈量和系统权限配置
> 其他工具
> R。
> CCR
> 配置
> Claude
> Code
> Router 以使用多个
> AI 模型
> U.
> CCusage
> Claude
> Code 用量分析
> 匕
> CCometixLine
> 基于
> Rust 的高性能
> Claude Code 状态栏工具, 集成 Git 信息和实时使用量跟踪
> ZCF
> 更改显示语言
> Select display language
> 更改
> ZCF 界面语言
> 5
> 切换代码工具
> 在支持的代码工具之间切换
> (Claude Code,
> Codex)
> 卸载和删除配置
> 从系统中删除
> Claude
> Code 配置和工具
> 检查更新
> 检查并更新
> Claude
> Code
> CCR 和
> CCometixLine 的版本
> @.
> 退出
> 请输入选项,回车确认 (不区分大小写)


### Step3：指定模型为GLM-4.6


> [!NOTE] [图片 OCR 识别内容]
> 「请输入选项 ,
> 回车确认 (不区分大小写)
> 3
> 请选择
> API 配置模式
> 2.
> 自定义
> API 配置
> Claude
> Code 配置管理
> 当前配置数量:
> 1
> 当前默认配置:  glm-test
> 请选择操作
> 1.
> 添加配置
> 2.
> 编辑配置
> 3.
> 复制配置
> 4.
> 删除配置
> 5.
> 跳过
> N navigate
> select
  
> [!NOTE] [图片 OCR 识别内容]
> [
> 请选择操作
> 1.
> 添加配置
> 添加新配置
> 「请选择
> API 供应商
> 4.
> GLN
> 己选择供应商:
> GLN
> 「配置名称 (仅限字母
> 数字
> 空格.
> '一)
> 9lm-4.6
> 请输入
> GLM 的
> API
> Key
 
选择供应商GLM，然后输入自己的GLM-4.6的api key即可。

这一步如果没有api key的朋友，可以通过我的**邀请链接**注册：
 [[链接已屏蔽]) 
或者直接进官网注册也可以：
 [[链接已屏蔽])

注册完之后，进入特惠专区：
 
> [!NOTE] [图片 OCR 识别内容]
> BigModel
> 特惠专区
> 大模型
> 应用空间
> 体验中心
> 价格
> 开发者 ~
> 企业
> 关于智谱
> 开发文档
> 控制台
> GLM Coding 跨年限时特惠
> 1/7价格.
> 3倍用量
> 适用Claude Code
> Cline
> 等主流编程工具
> GLM Coding
> 跨年特惠Coding套餐
> 邀好友赚赠金



> [!NOTE] [图片 OCR 识别内容]
> BigModel
> 我的编程套餐
> 接入编程工具 `
> 调AMCP
> 社区
> 常见问题
> API
> GLM Ioclimg pam:跨年特惠
> 12.08-01.15:
> 50% 首购立减 +额外节日限定优惠! 详细说明
> 全球顶尖编程模型 GLM-4.6 驱动
> GLM-4.6 发布时。在推理。代码和智能体能力等方面达到开
> 源模型 SOTA 水平
> Claude Sonnet 4.5
> 1387
> 无缝适配多种主流 Al 编程工具
> GLM 4.6
> 1372
> 超大容量
> 更低价格
> GPT 5.1
> 1364
> 免费享专属 MCP 
> 解锁高级能力
> 位列 Code Arena 榜单第一梯队
> 取自榜单更新时间 2025-11-22
> 首月享5折,
> 最高立省200元
> 琏续包月
> 连续包季
> -559
> 连续包年
> -609
 
订阅适合自己的套餐即可，订阅后点击右上角的API Key，然后创建api key并复制即可。

### Step4：开始使用
在按照zcf上面的步骤配置完成之后，我们先在控制台中cd到自己项目的地址，比如：`cd C:\Code\wqb` ，然后输入：`claude`，然后回车即可，如果出现如图所示的页面代表配置成功：
 
> [!NOTE] [图片 OCR 识别内容]
> Ps
> C: | Users |10597>
> cd
> C: | Code Iwqb
> Ps
> C: | Code'
> claude
> Claude
> Code
> V2.0.26
> Tips
> for getting started
> Welcome
> back !
> Run
> /init
> to
> Create
> CLAUDE .md
> file with
> instructions
> for Claude
> Recent
> activity
> No
> recent
> activity
> Sonnet
> 4.5
> API Usage Billing
> C: | Code|wqb
> Iy
> Iedit
> <filepath>
> to
> Sonnet
> 4.5
> main
> 0.6%
> 1.Ik tokens
> Thinking
> On
> Ctab
> to
> toggle)
> Wqb>
> Wqb
 
然后就可以正式使用了。

更多关于zcf的用法、参数与工作流说明可以查看文档： [ [[链接已屏蔽])]([链接已屏蔽]))

==然后补充一点，如果用不习惯Claude Code cli命令行工具的，可以去vscode中下载Claude Code插件：
 
> [!NOTE] [图片 OCR 识别内容]
> File
> Edit
> Selection
> View
> Go
> Run
> Terminal
> Help
> WQ-code [Administrator]
> 侣
> EXTENSIONS
> 田 Extension: Claude Code for VS Code X
> 米 凹
> Claude Code
> Search Extensions in Marketplace
> Past Conversations
> Claude Code for VS Code
> V2
> INSTALLED
> Cline
> Update
> Anthropic
> anthropiccom
> 2,335,422
> Claude Code
> CodellDB
> 13ms
> Claude Code for VS Code: Harness the power of Cla.
> Debugger for native code; powered by LLDB。
> Restart Extensions
> Disable
> Uninstall
> Auto Up
> Vadim Chugunov
> Update
> CICt +
> DETAILS
> FEATURES
> CICt +
> CICt + Intellisense; debugging, and code bro.
> Microsoft
> Restart Extensions
> Categories
> C# Dev Kit
> Claude Code for VS
> 0#
> Official C# extension
> Microsoft
> Chat
> Microsoft
> Restart Extensions
> Code
> Claude Code for VS Code
> ggms
> Resources
> Claude Code for VS Code: Harness the power
> Unleash Claude's raw power directly in your
> It's a beautiful
> to use the computer, don't
> Anthropic
> Restart Extensions
> terminal Search million-line codebases instantly。
> Marketplace
> you think?
> Turn hours-long workflows into a single
> Issues
> ESLint
> 31ms
> command. Your tools。 Your workflow. Your
> Anthropic
> ES
> Integrates ESLint JavaScript into VS Code。
> Uint
> codebase; evolving at thought speed。
> Microsoft
> Restart Extensions
> More Info
> Powerful intelligence: Use the latest
> Lua
> Lua Language Server coded by Lua
> Claude models using your Pro, Max; Team;
> Published 2025-06-19,
> Ua
> sumneko
> Restart Extensions
> OI
> Enterprise subscription; or pay-as
> 00:32:16
> go pricing
> Last
> 2025-12-18,
> Prefer the Terminal experience? Switch back in Settings。
> Lua Debug
> Works alongside you: Claude
> released
> 06:13:33
> Ua
> VSCode
> debugger extension for Lua
> autonomously explores
> codebase;
> Last
> 2025-12-18,
> ctrl esc to focus or unfocus Claude
> YOUT
> actboyl68
> Restart Extensions
> updated
> 15.01.48
> readsand writes code; and runs Term
> Identifier
> anthropic. claude
> Ask before edits
> alpha_searcher_use:ipynb
> Prettier
> Code formatter
> G1ms
> commands with your permission。
> Code
> Code formatter
> prettier
> Now ferhor mtorface that makes 汁
> from
> day
> JOU
> using


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我之前发给一个帖子关于iflow的，iflow有个人用户免费的api接口，也有glm-4.6模型，推荐给有需要的顾问。

---------------------------------------------------------------------------------

时间要花在有效率的地方

---------------------------------------------------------------------------------


---

### 技术对话片段 48 (原帖: 【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template)
- **原帖链接**: [Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
今天听说mcp里的APP发布了更新，有了新功能


> [!NOTE] [图片 OCR 识别内容]
> Open Submtter
> Open Simulator_M
> 七十娈


当然，为了更好使用新功能，你需要一个APIkey:  [[链接已屏蔽])

试用之后，我马上获得很多很好的模板！我直接开交！感觉我甚至不用做模板了，这是不是一种错觉？


> [!NOTE] [图片 OCR 识别内容]
> ts_rank(cIiability_gap_field/>,
> 252)"
> Broup_Zscore(ts_mean(ts_delay (cresidual_returns/>
> 21) ,
> 252),
> Sector)


唉，开始感觉自己以前交的Alpha类别有点太单一了，都是一个模板做出来的，现在好了，有了这种工具，反而我用了几次就发现，AI都被我太单一的idea限制住了，出新模板的能力都没那么好了。

还是赶紧多做不一样的吧！再次感谢作者，这个社区分我先”不要脸“地拿了，如果作者要claim这个著作权，请随时留言，我会撤回这个帖子。再次感谢！

**跟大家补充请教：生成的表达式太多咋办？以后限流遭不住。**

**补充点赞:  [【check王】验证表达式是否正确的脚本——七十二变黄金搭档]([Commented] 【check王】验证表达式是否正确的脚本七十二变黄金搭档_36740689434391.md)**

**虽然我自己用首页的import来检查就够，但这个朋友写得不错**

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的分享，试了一下真挺好的，建议大家都试一下，坚持学习努力和AI共生共存！

---------------------假如你每天都来论坛好好学习，你将会获得一个GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 49 (原帖: 【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template_36671111976983.md
- **时间**: 6 months ago

**提问/主帖背景 (CQ89422)**:
今天听说mcp里的APP发布了更新，有了新功能


> [!NOTE] [图片 OCR 识别内容]
> Open Submtter
> Open Simulator_M
> 七十娈


当然，为了更好使用新功能，你需要一个APIkey:  [[链接已屏蔽])

试用之后，我马上获得很多很好的模板！我直接开交！感觉我甚至不用做模板了，这是不是一种错觉？


> [!NOTE] [图片 OCR 识别内容]
> ts_rank(cIiability_gap_field/>,
> 252)"
> Broup_Zscore(ts_mean(ts_delay (cresidual_returns/>
> 21) ,
> 252),
> Sector)


唉，开始感觉自己以前交的Alpha类别有点太单一了，都是一个模板做出来的，现在好了，有了这种工具，反而我用了几次就发现，AI都被我太单一的idea限制住了，出新模板的能力都没那么好了。

还是赶紧多做不一样的吧！再次感谢作者，这个社区分我先”不要脸“地拿了，如果作者要claim这个著作权，请随时留言，我会撤回这个帖子。再次感谢！

**跟大家补充请教：生成的表达式太多咋办？以后限流遭不住。**

**补充点赞:  [【check王】验证表达式是否正确的脚本——七十二变黄金搭档]([Commented] 【check王】验证表达式是否正确的脚本七十二变黄金搭档_36740689434391.md)**

**虽然我自己用首页的import来检查就够，但这个朋友写得不错**

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的分享，试了一下真挺好的，建议大家都试一下，坚持学习努力和AI共生共存！

---------------------假如你每天都来论坛好好学习，你将会获得一个GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 50 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
吹哨人我又来了。看到了MCP里的新工具


> [!NOTE] [图片 OCR 识别内容]
> 缘分一道桥 (Alpha 跨区连锁)
> 返回主页
> C 使用说明
> 1.获取一段时间内的Alpha列表
> 2.分析每个 Alpha里的数据字段并迸行强替换。查看是否在其他Region/Universe/Delay有同样字段
> 3.生成新的Alpha
> 4.本页面的回测方式为排队回测; 一个完成后才会发送另一个;因此中途退出页面会中断回测
> 5.过长的回测队列有时会因为账号超时登出而出现连续失败。因此不建议选择过长时间跨度
> 6.如想批量回测;请下载所有待回测的Alphaf 选择首页回测器迸行回测
> 7.如果你想;你可以输入个很大的时间范围;下载所有表达式。慢慢迸行批量回测。


这个能直接一键回测并且横向点塔。更新到1.7.0版本以上就有噢。

我已经想到这样美好的图景：

- 1.横向点塔 （跨区、跨Universe)
- 2.点亮的塔，放入72变纵向点塔
- 3.被72变点量的纵向塔，再用桥，横向点塔。
- 4.横向点了塔，再72变
- 5. 如此反复，无穷尽也

以后我的研究，只需要专注于做好1-2个手搓或者AI合作的高级货，就能不断繁衍了！

效果不错，单击一下就能直接排队回测，我已经又完成了今天的提交。


> [!NOTE] [图片 OCR 识别内容]
> 2025-11-30104:40:58-05;00
> 10 个可用娈体
> 表达式: Srowp
> IIOIJLalize (1
> subindustry}
> 夏普: 0.65|收益:4.1%
> 戛普:0.69
> 收益:
> 4%
> 夏普:1.121收益:6.0%
> 夏普:0.95
> 收益:4.9%
> 夏普:
> 收益:
> .8%
> 夏普:086
> 收益:4.5%
> 戛普:0.76
> 收益:4.1%
> 戛普:1.16 |收益:7.7%
> 夏普:1.11 |收益:7.5%
> 夏普
> 1.05
> 收益-7.2%


再次叠甲：如有侵权，请联系本人。再次感谢作者。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
作者不仅厉害，还很勤奋，感谢作者的辛苦付出，及时雨！

升级到1.8.3后，如果指定了目标区域，产出的模版是0. 这个是什么问题？

------------------------------------------------------------------------------------------------

论坛里多看看，多学学，收获多多！

------------------------------------------------------------------------------------------------


---

### 技术对话片段 51 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md
- **时间**: 6个月前

**提问/主帖背景 (CQ89422)**:
吹哨人我又来了。看到了MCP里的新工具


> [!NOTE] [图片 OCR 识别内容]
> 缘分一道桥 (Alpha 跨区连锁)
> 返回主页
> C 使用说明
> 1.获取一段时间内的Alpha列表
> 2.分析每个 Alpha里的数据字段并迸行强替换。查看是否在其他Region/Universe/Delay有同样字段
> 3.生成新的Alpha
> 4.本页面的回测方式为排队回测; 一个完成后才会发送另一个;因此中途退出页面会中断回测
> 5.过长的回测队列有时会因为账号超时登出而出现连续失败。因此不建议选择过长时间跨度
> 6.如想批量回测;请下载所有待回测的Alphaf 选择首页回测器迸行回测
> 7.如果你想;你可以输入个很大的时间范围;下载所有表达式。慢慢迸行批量回测。


这个能直接一键回测并且横向点塔。更新到1.7.0版本以上就有噢。

我已经想到这样美好的图景：

- 1.横向点塔 （跨区、跨Universe)
- 2.点亮的塔，放入72变纵向点塔
- 3.被72变点量的纵向塔，再用桥，横向点塔。
- 4.横向点了塔，再72变
- 5. 如此反复，无穷尽也

以后我的研究，只需要专注于做好1-2个手搓或者AI合作的高级货，就能不断繁衍了！

效果不错，单击一下就能直接排队回测，我已经又完成了今天的提交。


> [!NOTE] [图片 OCR 识别内容]
> 2025-11-30104:40:58-05;00
> 10 个可用娈体
> 表达式: Srowp
> IIOIJLalize (1
> subindustry}
> 夏普: 0.65|收益:4.1%
> 戛普:0.69
> 收益:
> 4%
> 夏普:1.121收益:6.0%
> 夏普:0.95
> 收益:4.9%
> 夏普:
> 收益:
> .8%
> 夏普:086
> 收益:4.5%
> 戛普:0.76
> 收益:4.1%
> 戛普:1.16 |收益:7.7%
> 夏普:1.11 |收益:7.5%
> 夏普
> 1.05
> 收益-7.2%


再次叠甲：如有侵权，请联系本人。再次感谢作者。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
作者不仅厉害，还很勤奋，感谢作者的辛苦付出，及时雨！

升级到1.8.3后，如果指定了目标区域，产出的模版是0. 这个是什么问题？

------------------------------------------------------------------------------------------------

论坛里多看看，多学学，收获多多！

------------------------------------------------------------------------------------------------


---

### 技术对话片段 52 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
自己组合操作符，参数想怎么调就怎么调，不容易跟别人“撞衫”。但得想清楚：改动后逻辑还通吗？会不会搞出个“四不像”？

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 53 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
早上查了下Alpha池子，发现GLB那边几个因子最近有点掉效果。下午主要在搞RAM模型，试了把反转和动量因子叠一起跑。回测时内存爆了，只好分批喂数据。

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 54 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
这周和老师们一起搭了MCP，建了自己的工作流，做了个news数据模板。正在跑遍历，筛出了一些有效信号率约0.1%的因子。

平台限回测次数了，得抓紧提效，是挑战也是机会，要让自己也72变啦。

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 55 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025还剩不到一个月，60个塔的目标怕是达不成了，越来越感觉现在的工作流效率不够，还是得静下心好好学习建塔。加油吧！

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 56 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
今日提交一个ra一个sa，和之前的节奏一样，但base越来越少，看来提交的质量堪忧。

=======================================
长风破浪会有时，直挂云帆济沧海。

=======================================


---

### 技术对话片段 57 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
有几个质量一般的想优化再交，但和AI交流的结果不理想，那就等改好再提交，这次一定管住手。

GLB的combined有些担忧，回测慢也就代表了之后的各个地区的难度，MCP抓紧了。

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 58 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
要少跑回测了，工作方式也得赶紧改。的避开数据缺失、重复跑这些无效情况。稳健性测试太占资源了，后面打算手动测，凭经验判断不能无脑遍历了。

=======================================
长风破浪会有时，直挂云帆济沧海。

=======================================


---

### 技术对话片段 59 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
VF一降，每天Base看着真发愁。10月还能日达30+，11月破10都费劲。得好好刷论坛、跟大佬取经，盼着下次VF能回到0.98以上。也指望大佬们多分享干货，让我捡点灵感攒点经验。一起加油进步吧！

=======================================
长风破浪会有时，直挂云帆济沧海。

=======================================


---

### 技术对话片段 60 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025/12/6 我的量化日记

今天提交如下：

1 个regular alpha    收入  1.78dollar

1个super alpha       收入  3.18dollar

继续加油，努力学习，争取早日回到日平均收入50dollar以上，不给wq拖后腿！

=======================================
长风破浪会有时，直挂云帆济沧海。

=======================================


---

### 技术对话片段 61 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我的量化疑惑

为啥我的Combined Selected Alpha成绩一直卡在零点几呢？各位大佬们都是怎么提上去的，有啥法子能拉起来吗，真心求教🙏

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 62 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我的量化之——疑难杂症（Refer流失）

各位大佬，请教个难题：

你们都是怎么管理并提升Refer通过率的？我这儿注册的人不少，但大部分几天热度就流失了，能坚持到顾问阶段的很少。这中间该怎么帮（或者监督）他们坚持下去呢？求指教！

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 63 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我的量化日记——提交与收益

昨交1个Ra（1.73dao）+1个Sa（3.23dao）

最近提交数和收入都差不多，得加把劲了，争取早日跟上大佬们的节奏！

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 64 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
最近CNHKMCP更新的频率好快，希望有机会给大佬点赞！

============================================================================
=====================VF漂浮不定，alpha的质量和数量急需提升++++===================
============================================================================


---

### 技术对话片段 65 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
季度末感觉又要断粮了，今天只交了1个SA

============================================================================
=====================VF漂浮不定，alpha的质量和数量急需提升++++===================
============================================================================


---

### 技术对话片段 66 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
operators没有使用过的，让MCP试试，不要害怕失败，还是有收获的。

============================================================================
=====================VF漂浮不定，alpha的质量和数量急需提升++++===================
============================================================================


---

### 技术对话片段 67 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
MCP不是灵丹妙药，要允许他的失败和幻觉，慢慢地就会找到感觉。

============================================================================
=====================VF漂浮不定，alpha的质量和数量急需提升++++===================
============================================================================


---

### 技术对话片段 68 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
量化日记：昨交只交了1个Sa（4.88dao）。最近几天都没有合适的ra可以提交了，得加把劲了，争取早日跟上大佬们的节奏！

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 69 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
今天BASE又降了，一个SA才2.75dao。本以为10月交得还行，这次VF更新能涨点呢，现在只能盼着明天数值别掉下0.8了。

=======================================
长风破浪会有时，直挂云帆济沧海。


---

### 技术对话片段 70 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 11个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025/07/18

昨晚双周会听了大佬们的分享，收获很多。每次听其他顾问的分享，都有一种眼前一亮的感觉。新的赛季开始就是感觉很难，regular很难提交。

==================================================================================

长风破浪会有时，直挂云帆济沧海

==================================================================================


---

### 技术对话片段 71 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 11个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025/07/19

最近尝试跑GLB的新universe，感觉相关性并没有像EUR刚出TOP2500那样的低，与之前的MINVOL1M的相关性还是很接近。

==================================================================================

长风破浪会有时，直挂云帆济沧海

==================================================================================


---

### 技术对话片段 72 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2026-01-21提交结果

提交情况：RA 1个+ SA 1个 ;

收入情况：RA  1.93+SA  44.28 = 46.21；

提交心情：一心想做GLB的PPA,奈何天不遂人愿，搞了1天，PPA的指标就总是差那么一丢丢！

提交愿望：让我的iFllow幻觉减少一些，让我的PPA种子都可以达到标准！

————————————————————————————————-————————————

长风破浪会有时，直挂云帆济沧海！

————————————————————————————————————————————


---

### 技术对话片段 73 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2026-01-19

VF终于更新了，最近半个月提交都是谨小慎微的，生怕交错了会让我的VF继续下降。

终于更新了，终于从0.67回到了0.9以上，开心一小下！

————————————————————————————————-————————————

长风破浪会有时，直挂云帆济沧海！

—————————————————————————————————————————— ——


---

### 技术对话片段 74 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2026-01-20提交结果

提交情况：RA 2个+ SA 1个 ;

收入情况：RA  4.41+SA  39.42= 43.83；

提交心情：一心想做GLB的PPA,奈何出来的全是RA，明天继续PPA之旅！

提交愿望：让我的iFllow幻觉减少一些，让我的PPA种子都可以达到标准！

————————————————————————————————-————————————

长风破浪会有时，直挂云帆济沧海！

————————————————————————————————————————————


---

### 技术对话片段 75 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2026-01-17提交结果

提交情况：RA 2个；

收入情况：RA  3.32

VF太低了，保持提交，耐心等待中。。。。。。

————————————————————————————————-————————————

长风破浪会有时，直挂云帆济沧海！

—————————————————————————————————————————————


---

### 技术对话片段 76 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2026-01-18 提交结果

提交情况：RA 1个+SA 1个；

收入情况：RA 3.98+SA37.92=41.9

VF更了，可以提交SA了！

————————————————————————————————-————————————

长风破浪会有时，直挂云帆济沧海！

—————————————————————————————————————————————


---

### 技术对话片段 77 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
使用Gemini的一点小感受：

1、这玩意儿喜欢自动提交，连续2天，早上起床发现给我RA交了，吓得我呀。。。。。。

2、这玩意儿喜欢PUA，如下是他给我的回复：在“不增加数据字段、不超过7个运算符”的限制下，此结果已达极限。建议您提交此 Alpha（*******），因为： 1. 高夏普 (1.61) 有时能让系统在人工审核阶段宽容 Robust Sharpe 的不足。2. 它是目前唯一在 Sharpe 和 Fitness 双项指标上均达标的策略。

——————————————————————————————————————

长风破浪会有时，直挂云帆济沧海

——————————————————————————————————————


---

### 技术对话片段 78 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
今日AI讨论趣闻：

主角是GLMv4.7，这玩意儿很执拗，做测试，让他给我存个文件到目录中（目录中已经有了），结果他没存到对的文件夹内。我说他文件放错地方了，他说好的。。。。。。然后我发现他把我文件夹全给我删除了！！！

——————————————————————————————————————

长风破浪会有时，直挂云帆济沧海

——————————————————————————————————————


---

### 技术对话片段 79 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **时间**: 5个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2026-01-22提交结果

提交情况：Regular Alpha 1个；IND的Super alpha 1 个。

收入情况：RA  3.32

VF太低了，保持提交，耐心等待中。。。。。。

————————————————————————————————-————————————

长风破浪会有时，直挂云帆济沧海！

—————————————————————————————————————————————


---

### 技术对话片段 80 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
目前对数据集的理解还是停留在观察字段的差异上，比如opt的call/put，oth的sell/buy，通过字段差异找一些alpha，还是属于比较浅显的理解。

这个季度D1的字段已经跑得差不多了，其中的一些因为跑了一些没有明显的信号就放弃了。D0和CHN不知道跑下来的效果如何，但不跑肯定是不对的，走出舒适区。

ppac已经提交了很多，最近3天又开始断粮，看很多新人可以一天交好几个，很佩服。归0心态，学习和不断的积累吧。目前的期望就是希望每天可以交一个非ppac的ra。


---

### 技术对话片段 81 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
sac比赛分到了G2，开始感觉没有大家讨论的那么难，但今天是第3天，很多不错的sa因为相关性都无法提交，难度陡然上升。可以想象后续的竞争会越来越激烈。要做出差异化的sa，感觉难度很大。

之前Global论坛里有一个sac的板块为什么找不到了？按照目前的态势，想持续的提交SA可能是一个有挑战性的工作，最后的胜利者可能就是提交数量最多的。不知道预想的对不对，留帖为证吧。

sac比赛的激烈程度让原本用于开发ra的时间更捉襟见肘了，时间嘛，挤一挤总归是有的。希望大家都能取得理想的比赛名次。

=========================每天进步一点点，总会成长为一颗大树=========================


---

### 技术对话片段 82 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
今天是SAC比赛的第4天，提交了一个EUR，指标如下：
Sharpe 5.83
Turnover 11.66%
Fitness 5.33
Returns 10.45%
Drawdown 1.76%
Margin 17.92‱

增加了7000分，merge的分数是综合的成绩，因为还有fitness/sharpe接近8的，但分数还是负数。。。研究小组里讨论的sharpe曲线衰减问题，不容易遇到好的，大部分都是衰减的。晚上双周会，Weijie老师提到的哪里不够补哪里的思路很有启发，如果盯着分数，可能得不偿失。把margin/return提升，turnover降低，可能是参加这个比赛有意义的地方。关于SA的评判标准，还是比较模糊，希望大佬们可以多回帖说说。


---

### 技术对话片段 83 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年6月6日

复盘昨日工作，提交了1个EUR地区的SA和1个PPAC标准的RA。SA质量尚可，预计与昨日base相当，但两个RA仅勉强达标，需继续优化。目前重点关注降低per op和ops count指标，盘活闲置op提升整体利用率。

昨日全球SA会议收获颇丰，特别是关于combo应用的案例分享：
1. 分组zscore方法能有效控制行业暴露，通过sector分组标准化可降低alpha间相关性；
2. 市值加权策略展示中，alpha*rank(cap)的简单组合就能带来意外效果；
3. 风险中性化筛选条件清单非常实用，已保存为模板。

今日计划重点测试SLOW_AND_FAST中性化组合，尝试将operator_count控制在10以内，同时保持turnover<0.2的约束条件。另需注意避免在单一池子重复提交，保持策略多样性。


---

### 技术对话片段 84 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年6月7日

复盘昨日工作，提交了1个GLB地区的SA, RA又断粮了。

新的Theme又出来了，RAM后跑了几个，感觉和MAX TRADE一样，可能更接近实盘，导致各项指标都比较差。模拟盘和实盘的差距还是很大，想象一下如果自己搞量化，真的很难。现成的，大量的，各种各样的数据字段，快速高效的量化回测平台，结果还是搞成这样。网上经常看到很多人缺程序员，花钱找人写策略。。。都是想象中的美好，现实中的残酷。

今天有点想明白了，为什么sac很多人不交满，估计是减分的原因。但IS只占比25%，如果有检验SA稳定性的标准，数量多才有优势吧？每天做完了，又多了很多的新问题。

又是困惑的一天。


---

### 技术对话片段 85 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年6月11日

SAC比赛换区后，回测的neutralization设置里把"REVERSION_AND_MOMENTUM"写成了RAM，犯了一个低级错误，从昨晚到现在一个也没跑出来，全是报错的信息："message":"API rate limit exceeded" 和 text: {"settings":{"neutralization":["\"RAM\" is not a valid choice."]}}。

Selection条件没有对turnover做限制，换手率高于70%，也是一种错误。

希望看到帖子的顾问们，避免这样的错误。

这个季度就快结束了，还有5个塔没有点，努力！

最近大家都在讨论六纬，field count代表了回测了字段数量，其实也是多样性的一种体现，只有排名最高的一半，说明回测的设计还是缺乏多样性。


---

### 技术对话片段 86 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年06月12日周四早09:40

季度末的Genius评级冲刺太吓人了，我的排名以每天10名的速度快速下降。卷不过，还是卷不过。

==================================我是分割线========================================

今天收到邮件，课代表对最新的2，3，4月的ValueFactor做了分析，没有看到更新啊？课代表这是什么操作呢？

==================================我是分割线========================================

SAC比赛现在基本加不了分，不知道其他顾问如何，今天提交了一个减分1000多的，prod是0.6


---

### 技术对话片段 87 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
昨天提交了一个RAM主题的RA，相关性0.43，VF0.81的收入是32刀。。。低相关性确实是影响日收入的关键因素之一。之前交的RAM主题，相关性0.68的只有5刀。供大家参考。

研究小组看到了SAC周赛第一，第二的邮件，国区厉害了，期待大佬们的分享。之前大家拼分追求高Fitness和Sharpe，估计之后大家会换一个角度来看待比赛了。

我现在觉得能多追求低相关性可能是最难，但最值得的。

==================================================================================


---

### 技术对话片段 88 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025.06.13 最新战况美东时间2025-06-13 03:53：
Genius排行榜总人数: 6050 (-29)
满足Q2上交40个signals的人数：1961 (+9)
满足Expert条件的总人数：909 / 392 (+26)
满足Master条件的总人数：352 / 157 (+11)
满足Grandmaster条件的总人数：35 / 39 (+3)

----------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 89 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年6月15日10:10

交了一个SA，交了一个RA。

GLB的SA回测速度比较慢，考虑到个人的GLB performance比较低，还是硬着头皮继续交GLB吧，但margin和returns这两个指标通过SA想提升的想法执行起来也是不容易的，现在可以组合所有顾问的GLB regular alpha了，通过这些SA还是比较难提升，看来GLB在我有的四个区域USA EUR GLB ASI里难度确实比较大，所有顾问平均后的指标纬度并没有比个人的好太多。

然后把SA的帖子又复习了一遍，继续优化selection/combo的语句，看看是否可以组合出更好的GLB。

RA这次提交的是RAM主题的ppa，prod corr是0.47，没有通过regular ra的全部检测，下午看看收入如何。

----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 90 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年6月16日11:12

昨日提交了一个SA，regular alpha没有合适的，断交一天。

SAC比赛的相关性越来越高，本质就是同质化严重，反复阅读论坛里的相关内容，今天又是一个新主题周了，希望能找到一些低相关性的SA。

6月已经过半，Genius排名竞争异常激烈。

还有不到15天，最后的冲刺阶段，不能泄劲。

---------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 91 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025-06-17

今天终于提交了一个regular alpha，指标一般，考虑到自相关性0.12，还是交了。

SAC比赛还可以勉强提交，相关性普遍章0.65左右，不是很乐观。

--------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 92 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025-06-18

今天SAC比赛的SA提交很困难，普遍的相关性都比较高。

Regular alpha今天没有找到，存货也已经被反复挖掘，没有了。

还是月底的冲刺阶段，十分的捉急。

--------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 93 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025.06.25

很久没有写量化日记了，看到大佬们都收到了SAC比赛的邮件，感觉这次的比赛又是重在参与了，无论从相关性，还是IS表现都没有找到好的方法，停留在了原地。

晚上参加了SAC的全球顾问培训，收获很多。

继续努力吧。

==================================================================


---

### 技术对话片段 94 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年6月28日

Base收入明显下降，虽然Value Factor还没有变化，但大概率是又又下降了。果然是坐牢就不会轻易出狱。

不知道combined更新能不能稳住，有点忐忑不安的感觉。

----------------------------------------------------------------------------------------------

加油，有问题就修正，等待时间的回归。

-----------------------------------------------------------------------------------------------


---

### 技术对话片段 95 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
2025年06月29日

这个赛季马上就要结束了，量化日记的回帖数量也超过了900条。每个顾问都在评级而努力，希望各位顾问都可以达到自己期望的定级。

今天最不开心的事就是vf更新后，比预期又降低了，希望不要影响combined。

==================================================================================


---

### 技术对话片段 96 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
季度末，第八季，积极参与。

12.17

提交1个sa，0个ra。

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 97 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
12.18

提交1个sa，1个ppa

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 98 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
12.19

提交1个sa，1个ra。终于又有ra可以交了，开心。

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 99 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
12.20

提交1个sa，又断粮了。

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 100 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
12.21

继续断粮，回测数量限制后的工作流程还没有适应。

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 101 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
12.22

学习论坛的帖子，给比赛的alpha打分。和MCP聊了很久，他也没有给出好的思路，先参与。

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 102 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
与Deepseek聊天有感

上周听了文WD大佬的AI分享，周末赶紧想着复现一下，先让Deepseek学习了WD大佬的帖子，然后开始提问。。。

------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

------------------------------------------------------------------------------------


---

### 技术对话片段 103 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
跟着帖子，通过risk里的字段代替cap，实现点亮risk字段，这个方法好！

-----------------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海

-----------------------------------------------------------------------------------------------------------


---

### 技术对话片段 104 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
量化日记：2025-12-23

昨日收入主要来自Super Alpha，共1.89dao。最近空闲时间都在学习和AI交流，进展稍有好转，但离目标还远，继续加油！

=======================================
长风破浪会有时，直挂云帆济沧海。

=======================================


---

### 技术对话片段 105 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
论坛里的好帖子太多了，学不过来，根本学不过来！复现的过程中，还是无法做到原贴的效果，可能还是有很多的细节没有理解，导致了结果却不好。

提示词、本地资料的准备、数据集的选择。。。影响的因素可能很多，不能单靠一个提示词或者workflow。

========================================================
长风破浪会有时，直挂云帆济沧海。

========================================================


---

### 技术对话片段 106 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
周四晚上的分享会，又得到了一个新的方向：多agent。

学无止境。跟不上大家的节奏啊。

===============================================================

长风破浪会有时，直挂云帆济沧海

===============================================================


---

### 技术对话片段 107 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
今天是圣诞节，提交一个regular alpha，算过节了！

也祝大家节日快乐，天天开心

===============================================================

长风破浪会有时，直挂云帆济沧海

===============================================================


---

### 技术对话片段 108 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
季度末的日子开始倒数了，各项genius指标基本定型，沉下心来，多读论坛，多复现实践，为下一个季度准备一个好的开端。

===============================================================

长风破浪会有时，直挂云帆济沧海

===============================================================


---

### 技术对话片段 109 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
翻看量化日记，看到很多的顾问和我一样，和AI的沟通又累效率又低。。。不能放弃啊，AI的技术在进步，不用大概率会跟不上时代，Kunqi老师说得很好，用好AI，不仅仅是在worldquant，对自己的学习和工作同样有帮助。

===============================================================

长风破浪会有时，直挂云帆济沧海

===============================================================


---

### 技术对话片段 110 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
12.27 osmosis比赛的alpha要优选，而不是吃大锅饭。尝试以组合sa的方式，来挑选因子，以为找到了非常接近35的super alpha。

===============================================================

长风破浪会有时，直挂云帆济沧海

===============================================================


---

### 技术对话片段 111 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
如果从sa的IS表现来筛选比赛的regular alpha，那每个地区的就有了不同的策略，分数打上去了，看看之后的pnl daily表现吧。

===============================================================

长风破浪会有时，直挂云帆济沧海

===============================================================


---

### 技术对话片段 112 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
202603016 我的量化日记

第11季开始了，继续记录我的量化生活。

完成提交1+1，最近在持续的断粮，存货里也翻不出来了。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 113 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
202603017 我的量化日记

只提交了一个super alpha，持续的断粮，让我焦虑。。。。。。。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 114 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
202603018 我的量化日记

提交了一个super alpha，季度末力不从心。没有季度初点塔的热情。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 115 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
202603019 我的量化日记

提交了一个super alpha和一个PPA，1+1好开心。每天提交的数量大幅下降，焦虑我的VF。。。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 116 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
202603020 我的量化日记

提交了一个super alpha和一个PPA，我要做长跑选手，向橘子姐好好学习，太厉害了。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 117 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
Combined更新了，又小幅度下降。。。。

感觉遇到了瓶颈，提交不顺利，模版没有产出。。。。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 118 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
已经3月下旬，为什么这次的VF更新这么慢呢？

OSMOSIS打分出来问题，rank为0，天天的BASE好难受。。。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 119 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
继续研究龙虾，看来大佬关于龙虾的帖子，感觉现阶段还是属于折腾的阶段，有前途，但不容易搞起来。。。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 120 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
翻阅之前的量化日记看到了橘子姐姐的提交：

USA的regualr，还是analyst，self_correlation只有0.1804 ，优秀！

最近也在做USA，看来还是太依赖模版了。。。导致相关性过高，而无法提交。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 121 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期

- [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments)
- [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md)
- [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md)
- [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)
- [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md)
- [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md)
- [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md)
- [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md)
- [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md)
- [【日常生活贴】我的量化日记第十季]([L2] 【日常生活贴】我的量化日记第十季_38768672144151.md)

因评论到达上限，已无法评论，特此展开第十一季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
iflow就要停止维护，下个月下线，又一个免费的Token羊毛没有了。

腾讯的workbuddy还可以试试，最终还是需要买token plan，

大家购买Token plan了吗，推荐一个。

==========================================================================

长风破浪会有时，直挂云帆济沧海！

==========================================================================


---

### 技术对话片段 122 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (HP65370)**:
大家好，我是25年参加了IQC之后在7月1日左右拿到顾问权限的，刚开始什么都不懂，连ppa是什么都不知道，也不知道六维是什么，拿到权限的7天后才提交了自己的第一个顾问因子，最后也是从新手课和众多大佬的经验帖子里面逐渐熟悉规则，在789三个月里成功从gold冲到master，10 11 12三个月从master冲上了grandmaster。

**(一)Gold→Master**

在最终结算的时候我的六维:


> [!NOTE] [图片 OCR 识别内容]
> 编辑六维指标 
> 编辑六维指标数据
> Operator Count:
> Operator
> 69
> 4.2
> Field Count:
> Field
> 200
> 1.7
> Community Activity:
> Max Simulation Streak:
> 25
> 89
> 更新排名
> 以 Expert 为 Universe
> 以 Master 为 Universe
> Grandmaster 为 Universe
> 总排名:279/699
> 总排名:309
> 279
> 总排名:107
> 70
> Operator Count: 455 名
> Operator Count: 347 名
> Operator Count: 109名
> Operator
> 454名
> Operator
> 210名
> Operator AVg: 48名
> Field Count: 661 名
> Field Count: 395 名
> Field Count: 104 名
> Field AVg: 260名
> Field AVg: 103名
> Field AVg: 25 名
> Community Activity: 356名
> Community Activity: 291 名
> Community Activity: 92 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Max Simulation Streak: 1135 名
> Max Simulation Streak: 526 名
> Max Simulation Streak: 110名
> Total Rank: 3322名
> Total Rank: 1873名
> Total Rank: 489名
> AVg:
> AVg:
> AVg:
> AVg:


**我的提交与回测系统：**

我在7月，只做了eur和usa两个地区，一共提交了55个alpha，采用的是传统一二三阶代码，完全没有修改，但是最多只会做到二阶；在8月，做了glb、eur、asi，一共提交了73个alpha,由于传统二阶代码会严重拉跨平均操作符和平均字段，于是我逐渐舍弃二阶，并修改一阶中的模板；在9月，只做了usa这一个地区，由于时间不充裕，只交了23个alpha，延续了8月的风格，以压操作符和字段为主。

**我的combine:**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.16
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.38


当时也是很惊讶能有这么高，更新到6月也就是iqc期间，我的combine是0.34,第二次更新到7月，记得好像是1.2，第三次更新到8月，combine最高来到了2.38;提交的核心标准是margin要达标，turnover不能过高，其他的综合来看，觉得不是很难看就交了，除了二阶里面的group类型字段，几乎没有做过双字段的alpha。

(点塔图没有找到)

**（二）Master** → **Grandmaster**

最终结算的时候我的六维、combine、塔图:


> [!NOTE] [图片 OCR 识别内容]
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.69
> 125
> 1.34
> Fields used
> Community activity
> Max simulation streak
> 311
> 48.4
> 181



> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 3.02



> [!NOTE] [图片 OCR 识别内容]
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
> Analyst
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 10
> 14
> 14
> 10
> 13
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


相比于上个赛季，我的工作流变化挺大的，

**1、提前过滤字段**

在传统一阶回测的时候经常会遇到缺数据的字段，这样既浪费了回测数量，也严重影响了我的心情，于是我以一个塔为单位，例如把一个region内所有归属于model的全部字段直接回测，提前把那些缺数据的字段拉黑，提高了后续回测任务的效率，并利用数据库来记录，判断缺数据的字段也很简单，利用api获取回测出来的alpha的每年的sharpe有多少个0就行了。

**2、优化模板流**

在传统的一阶回测或者是论坛中的一些模板，其大多都有个共性，也就是探索度太大了，在有限的回测次数内，出货效率很低，并且类似的模板对同一个字段跑出来的alpha的相关性过高，有时会花费过多回测数量在一个难以出货的字段上面，于是我做出改进，把每个模板 的探索度降为1，具体做法为：固定时间参数，固定操作符，比如group_op(ts_op(x,day),group),day我会取一个固定的值，group我只在market,industry,sector,subindustry中选一个，group_op我一般在group_rank,group_zscore,group_neutralize中选一个，ts_op也一样。目的是在较少的回测数量内挖掘出一个字段的基础信号，哪怕是微小信号也好。

其次，把这些表达式批量写入数据库，每一组回测完后就回填数据，计算相关性，并做好标记以免重复回测。

**3、对alpha的初加工**

对上述回测完的alpha进行进一步的改进，设立了一个评分机制，同一个数据字段内的alpha为一组，对组内的alpha以sharpe、fitness、margin为指标进行打分，选取分值最高的并且相关性小于0.5的那个进入下一步的加工环节，传统的二阶是对所有sharpe、fitness满足条件的alpha进行提升，可是在同一个数据字段内的alpha本身相关性就很高，可能交了一个alpha后其他alpha可能都交不了了，为何不选择一个最好的来做二阶呢。

加工我采用的是：遍历中性化、遍历时间参数、非线性变换、是否保留ts_backfill和winsorize；其中遍历时间参数以等差数列进行遍历，大约需要多回测9次，非线性变换主要包括tanh,sqrt,log,signed_power,arc_cos,exp；再批量把这些操作于这个分值最高的alpha上并写进数据库自动回测。

**4、对alpha的细加工**

对于初加工的alpha，我会人工去把它们组合起来，比如在最佳中性化下运用最佳的时间参数并看是否需要结合非线性变换，并确认是否需要删除多余操作符，把这样的表达式拿去平台回测，并进行细微的优化，比如turnover过高，我会加decay，weight超了，想办法去降。

**5、回测数量的分配**

每天回测就5000次，我们应该规划好这些次数拿来做什么，我是多塔同时出发，8个槽或者glb的四个槽，每一个槽都会回测不一样的塔，避免在一个难出的塔上面一直耗下去，在点亮了塔之后便停掉跑其他的，直到全部点亮或者点不亮时才会回去做一些好出的塔比如model、pv等凑数量。

其他的基本和Q3一样，比如提交标准没变，combine更新到11月，其最高combine来到了3.02，点塔也是一个月最多三个地区，每个地区在一个月内我会尽可能交三十多个，平均一天3个加一个superalpha，唯一的变数是在12月，我只做了两个地区，usa的d0和d1，平均每天只交了2个加一个superalpha，同样的在Q3的最后一月，提交的数量相较于上个月少了很多，两次都导致我的vf骤降，combine微跌，但是影响这两个指标变化的因素有很多，我也不知道为什么会这样。

**踩过的坑：**

对于新人来说，冲刺master或者grandmaster的第一阻碍或许是最大连续回测天数，我最初没有看懂这个以至于到了顾问阶段回测天数断了，若是中途断了就需要在六维的其他方面花费更多的精力。

**思考&改进：**

有些模板彼此间就有很强的相关性，做出来的alpha彼此间大概率也是高相关性，可以计算单个数据字段内alpha间互相的相关性，利用多组数据，找到均值比较高的那组，删去指标较差的那个模板，以此来简化模板流。（还没有时间做）

**总结：**

想要在genius中获得高评级，点塔、六维、combine缺一不可，核心都是在有限的回测次数内做出大量优质alpha。

===============================================

最后祝愿大家所愿皆所得，vf wf combine base genius全都升！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬分享工作流，一直想优化，但千头万绪不知道从哪里开始。每天忙得不亦乐乎，却忘了思考如何提高效率，磨刀不误砍柴工。

现在有了参考，每天花一点时间找LLM讨论一下工作流，争取早日从重复劳动中解脱出来，认真的研究因子。

---------------------------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海。

---------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 123 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享_38932709256727.md
- **时间**: 3个月前

**提问/主帖背景 (HP65370)**:
大家好，我是25年参加了IQC之后在7月1日左右拿到顾问权限的，刚开始什么都不懂，连ppa是什么都不知道，也不知道六维是什么，拿到权限的7天后才提交了自己的第一个顾问因子，最后也是从新手课和众多大佬的经验帖子里面逐渐熟悉规则，在789三个月里成功从gold冲到master，10 11 12三个月从master冲上了grandmaster。

**(一)Gold→Master**

在最终结算的时候我的六维:


> [!NOTE] [图片 OCR 识别内容]
> 编辑六维指标 
> 编辑六维指标数据
> Operator Count:
> Operator
> 69
> 4.2
> Field Count:
> Field
> 200
> 1.7
> Community Activity:
> Max Simulation Streak:
> 25
> 89
> 更新排名
> 以 Expert 为 Universe
> 以 Master 为 Universe
> Grandmaster 为 Universe
> 总排名:279/699
> 总排名:309
> 279
> 总排名:107
> 70
> Operator Count: 455 名
> Operator Count: 347 名
> Operator Count: 109名
> Operator
> 454名
> Operator
> 210名
> Operator AVg: 48名
> Field Count: 661 名
> Field Count: 395 名
> Field Count: 104 名
> Field AVg: 260名
> Field AVg: 103名
> Field AVg: 25 名
> Community Activity: 356名
> Community Activity: 291 名
> Community Activity: 92 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Completed Referrals: 1 名
> Max Simulation Streak: 1135 名
> Max Simulation Streak: 526 名
> Max Simulation Streak: 110名
> Total Rank: 3322名
> Total Rank: 1873名
> Total Rank: 489名
> AVg:
> AVg:
> AVg:
> AVg:


**我的提交与回测系统：**

我在7月，只做了eur和usa两个地区，一共提交了55个alpha，采用的是传统一二三阶代码，完全没有修改，但是最多只会做到二阶；在8月，做了glb、eur、asi，一共提交了73个alpha,由于传统二阶代码会严重拉跨平均操作符和平均字段，于是我逐渐舍弃二阶，并修改一阶中的模板；在9月，只做了usa这一个地区，由于时间不充裕，只交了23个alpha，延续了8月的风格，以压操作符和字段为主。

**我的combine:**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.16
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No
> matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.38


当时也是很惊讶能有这么高，更新到6月也就是iqc期间，我的combine是0.34,第二次更新到7月，记得好像是1.2，第三次更新到8月，combine最高来到了2.38;提交的核心标准是margin要达标，turnover不能过高，其他的综合来看，觉得不是很难看就交了，除了二阶里面的group类型字段，几乎没有做过双字段的alpha。

(点塔图没有找到)

**（二）Master** → **Grandmaster**

最终结算的时候我的六维、combine、塔图:


> [!NOTE] [图片 OCR 识别内容]
> Operators per Alpha
> Operators used
> Fields per Alpha
> 3.69
> 125
> 1.34
> Fields used
> Community activity
> Max simulation streak
> 311
> 48.4
> 181



> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 3.02



> [!NOTE] [图片 OCR 识别内容]
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
> Analyst
> Broker
> Earnings
> Fundamental
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 10
> 14
> 14
> 10
> 13
> News
> Option
> Other
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


相比于上个赛季，我的工作流变化挺大的，

**1、提前过滤字段**

在传统一阶回测的时候经常会遇到缺数据的字段，这样既浪费了回测数量，也严重影响了我的心情，于是我以一个塔为单位，例如把一个region内所有归属于model的全部字段直接回测，提前把那些缺数据的字段拉黑，提高了后续回测任务的效率，并利用数据库来记录，判断缺数据的字段也很简单，利用api获取回测出来的alpha的每年的sharpe有多少个0就行了。

**2、优化模板流**

在传统的一阶回测或者是论坛中的一些模板，其大多都有个共性，也就是探索度太大了，在有限的回测次数内，出货效率很低，并且类似的模板对同一个字段跑出来的alpha的相关性过高，有时会花费过多回测数量在一个难以出货的字段上面，于是我做出改进，把每个模板 的探索度降为1，具体做法为：固定时间参数，固定操作符，比如group_op(ts_op(x,day),group),day我会取一个固定的值，group我只在market,industry,sector,subindustry中选一个，group_op我一般在group_rank,group_zscore,group_neutralize中选一个，ts_op也一样。目的是在较少的回测数量内挖掘出一个字段的基础信号，哪怕是微小信号也好。

其次，把这些表达式批量写入数据库，每一组回测完后就回填数据，计算相关性，并做好标记以免重复回测。

**3、对alpha的初加工**

对上述回测完的alpha进行进一步的改进，设立了一个评分机制，同一个数据字段内的alpha为一组，对组内的alpha以sharpe、fitness、margin为指标进行打分，选取分值最高的并且相关性小于0.5的那个进入下一步的加工环节，传统的二阶是对所有sharpe、fitness满足条件的alpha进行提升，可是在同一个数据字段内的alpha本身相关性就很高，可能交了一个alpha后其他alpha可能都交不了了，为何不选择一个最好的来做二阶呢。

加工我采用的是：遍历中性化、遍历时间参数、非线性变换、是否保留ts_backfill和winsorize；其中遍历时间参数以等差数列进行遍历，大约需要多回测9次，非线性变换主要包括tanh,sqrt,log,signed_power,arc_cos,exp；再批量把这些操作于这个分值最高的alpha上并写进数据库自动回测。

**4、对alpha的细加工**

对于初加工的alpha，我会人工去把它们组合起来，比如在最佳中性化下运用最佳的时间参数并看是否需要结合非线性变换，并确认是否需要删除多余操作符，把这样的表达式拿去平台回测，并进行细微的优化，比如turnover过高，我会加decay，weight超了，想办法去降。

**5、回测数量的分配**

每天回测就5000次，我们应该规划好这些次数拿来做什么，我是多塔同时出发，8个槽或者glb的四个槽，每一个槽都会回测不一样的塔，避免在一个难出的塔上面一直耗下去，在点亮了塔之后便停掉跑其他的，直到全部点亮或者点不亮时才会回去做一些好出的塔比如model、pv等凑数量。

其他的基本和Q3一样，比如提交标准没变，combine更新到11月，其最高combine来到了3.02，点塔也是一个月最多三个地区，每个地区在一个月内我会尽可能交三十多个，平均一天3个加一个superalpha，唯一的变数是在12月，我只做了两个地区，usa的d0和d1，平均每天只交了2个加一个superalpha，同样的在Q3的最后一月，提交的数量相较于上个月少了很多，两次都导致我的vf骤降，combine微跌，但是影响这两个指标变化的因素有很多，我也不知道为什么会这样。

**踩过的坑：**

对于新人来说，冲刺master或者grandmaster的第一阻碍或许是最大连续回测天数，我最初没有看懂这个以至于到了顾问阶段回测天数断了，若是中途断了就需要在六维的其他方面花费更多的精力。

**思考&改进：**

有些模板彼此间就有很强的相关性，做出来的alpha彼此间大概率也是高相关性，可以计算单个数据字段内alpha间互相的相关性，利用多组数据，找到均值比较高的那组，删去指标较差的那个模板，以此来简化模板流。（还没有时间做）

**总结：**

想要在genius中获得高评级，点塔、六维、combine缺一不可，核心都是在有限的回测次数内做出大量优质alpha。

===============================================

最后祝愿大家所愿皆所得，vf wf combine base genius全都升！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬分享工作流，一直想优化，但千头万绪不知道从哪里开始。每天忙得不亦乐乎，却忘了思考如何提高效率，磨刀不误砍柴工。

现在有了参考，每天花一点时间找LLM讨论一下工作流，争取早日从重复劳动中解脱出来，认真的研究因子。

---------------------------------------------------------------------------------------------------------------------

长风破浪会有时，直挂云帆济沧海。

---------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 124 (原帖: 一键检验alpha稳定性代码优化)
- **原帖链接**: [Commented] 一键检验alpha稳定性代码优化.md
- **时间**: 1 year ago

**提问/主帖背景 (JL71699)**:
很多顾问提交的alpha都是machine alpha，就会遇到一个问题，如何检验稳定性，通过常规方法就是改变neutralization和decay观察信号是否有明显的变化，于是我就有下面的思路，原理是我输一个id，get了alpha的信息，修改alpha setting，就自动发送命令，然后抢线发送，然后顺着发送的链接，get到alphaid再爬回来稳定性检验alpha的数据及pnl，之后本地绘制pnl并且绘制表格，给出对比

只需要输入想进行稳定性分析的alphaid，就能得到下面的图像，具体的稳定性测试方法可以在代码中进行修改。

具体代码我已经开源到研究小组，有需要可自取 [[链接已屏蔽])

下图为示例，并且会有跟随的alpha表格（具体未展示）


> [!NOTE] [图片 OCR 识别内容]
> 126
> 多时间序列邓比
> WO7qbpx
> PSLrOZWI
> 7YPqAd1
> VATnqMQ
> MGvlog6
> XTWMOII
> gaNqvlQ
> QORrm7r
> LKobeMe
> LKobq7m
> 日期
> rTa6QPI
> 2014
> 2015
> 2018
> 2019
> 2013
> 2016
> 2017
> 2020
> 2022
> 2023
> 2021


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
参考官方给出的alpha提交前的checklist，可以增加rank, sign的检查，作为稳健性检查的一个环节。感谢大佬的代码和思路。


---

### 技术对话片段 125 (原帖: 一键检验alpha稳定性代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一键检验alpha稳定性代码优化_32008506789655.md
- **时间**: 1年前

**提问/主帖背景 (JL71699)**:
很多顾问提交的alpha都是machine alpha，就会遇到一个问题，如何检验稳定性，通过常规方法就是改变neutralization和decay观察信号是否有明显的变化，于是我就有下面的思路，原理是我输一个id，get了alpha的信息，修改alpha setting，就自动发送命令，然后抢线发送，然后顺着发送的链接，get到alphaid再爬回来稳定性检验alpha的数据及pnl，之后本地绘制pnl并且绘制表格，给出对比

只需要输入想进行稳定性分析的alphaid，就能得到下面的图像，具体的稳定性测试方法可以在代码中进行修改。

具体代码我已经开源到研究小组，有需要可自取 [[链接已屏蔽])

下图为示例，并且会有跟随的alpha表格（具体未展示）


> [!NOTE] [图片 OCR 识别内容]
> 126
> 多时间序列邓比
> WO7qbpx
> PSLrOZWI
> 7YPqAd1
> VATnqMQ
> MGvlog6
> XTWMOII
> gaNqvlQ
> QORrm7r
> LKobeMe
> LKobq7m
> 日期
> rTa6QPI
> 2014
> 2015
> 2018
> 2019
> 2013
> 2016
> 2017
> 2020
> 2022
> 2023
> 2021


**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
参考官方给出的alpha提交前的checklist，可以增加rank, sign的检查，作为稳健性检查的一个环节。感谢大佬的代码和思路。


---

### 技术对话片段 126 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 借助MCP手搓IND地区short_interest点塔经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (CY96125)**:
IND地区作为最近炙手可热的研究地区，作为新手的我当然不想错过这个机会，于是寻找数据字段进行点塔，看到了short interest模块只有三个字段，想去借助MCP工具尝试一波。

先去了解数据字段的含义：


> [!NOTE] [图片 OCR 识别内容]
> Roo 说
> 很好!  我找到了shortinterests数据集。从结果中可以看到。它昀10是"shortinterests"
> 名称
> 是 Daily Price Limit Data
> 描逑是关于上海。深圳和香港交易所的股票交易停牌和价格限制
> 数据。现在我恶要获取该数据集中的具体datafeld列衷。


MCP给出了三个datafields的经济学含义分析，在此因为篇幅原因不展开讲了，我的prompt里要求的是给出字段的经济学含义，并且组成可能的alpha expression，因此在最后给了我在Alpha构建中的应用建议：

1. **限制突破策略** :
2. **流动性压力指标** :
3. **市场情绪代理** :

在这个基础上，我先分别回测了这三个字段套上rank，发现了这三个数据字段回测的结果完全一样。综合了以上回测结果和MCP给予的指示，我想到了 **量价动量** 模型，先从pv字段去寻找，发现ts_corr(volume, close, 5)与short interest的字段结合信号强烈，但是pc太高了，于是去找MCP来解决问题.


> [!NOTE] [图片 OCR 识别内容]
> 首先。我需要查看这个alpha的详细信息。包括其表达式。性能等。使用MCP工具
> get_alpha_details
> 获取alpha信息。
> 同时。我将创建一个todo列表来跟踪步骤。
> 5  已更新待办事项列表
> ::分析经济学含义
> 黛理解现有表达式 -rank(ts_corr(close; volume; 5))
> :寻找替代字段构造相同意义的表达式
> ::组合rank(price_limit_condition)
> :提供建议和解释
> 获取alpha QPXIMAXM的详细信息



> [!NOTE] [图片 OCR 识别内容]
> Roo 说
> 现在分析经济学含义。该alpha的核心表达式足:
> alpha
> ank(ts_corr(close, volume
> 5))
> rank (price_Iimit_condition);
> 然后经过填充。缩尾。行业中性化。板块回填等处理。
> 古先
> COTTC052
> VO LUNe
> 5)计箅过去5天的收盘价与成交显的时间序列相关性。这个
> 相关性反映了价量关系:  正相关可能蒽味着价量齐升 (趋势跟随) ,负相关可能意味着价量
> 背离 (反转信号)。
> rark(:::)
> 衷示对相关性进行排名井取负。即相关性越高的股票得分越低
> (做空) ,相关性越低的股票得分越高  (做多)。这本质上是在押注价量相关性低的股票 (即
> 价显背离)  未来表现更好。而价屉相关性高的股票末来表现更耋。
> price_lipit_condition
> 是价格限制条件,可能是
> 个布尔值或数值。表示股票是否处于涨跌
> 停状态或其他价格限制情况。
> rank(price_Iimit_condition)
> 对其排名。可能表示价格限制程
> 度高的股票得分高。
> 两者相乘; alpha结合了价量背离信号和价格限制信号。经济学含义可能是:  价量背离的股票
> (可能意味着市场惰绪与价格走势不一致)加上价格限制 (流动性受限)  可能产生特殊的市
> 场异常收益。这种组合可能捕捉到市场微观结构中的定价无效宰。



> [!NOTE] [图片 OCR 识别内容]
> Roo
> 现在寻找替代字段。我们有许多价格和成交量字段: open high
> IOu
> WWaP
> returns。
> adv20等。我们可以构造以下替代表达式:
> ~rank(ts_Corr(open
> Volue
> 5))
> 使用开盘价代替收盘价。
> -pank(ts
> corr(hieh,
> Volue,
> 5))
> 使用最高价。
> ~pank(ts_corr
> Volume, 5))
> 使用最低价。
> ~rank(ts_corr(Vwap
> Volume
> 5))
> 使用成交显加权平均价。
> ~rank(ts
> CORRCROUUTI s
> volume, 5))
> 使用收益宰代替价格。
> ~rank(ts_corr(close,
> a420
> 5)
> 使用平均成交量代替日成交量。
> rank(ts_Corr(close
> 101
> 10))
> 改娈时间窗口。
> 8-rank(ts_corr(close
> Volue; 3))
> 更短窗口。
> 我们还可以使用其他相关性度显。例如ts
> 或ts_regression。 但为了保持相同意义;。我
> 们应坚持使用相关性。
> 此外;
> 我们可以使用其他技术指标,如md1135_del_tpv  (量价趋势)  或md1135_d3_ivn (负成
> 交显指数)。这些指标已经捕捉了价显关系。可能捉供类似的信号。
> 但用户要求"用其他的字段datafeld构造和-rankfts_corr(close; volume; 5))相同意义的
> expresslon
> 这意味着我们需要使用不同的数据字段。但产生相似的经济学含义。我们可以
> 选择与价量相关的宇段。但避免使用close和volume, 以降低相关性。
> 例如。使用 open 和 adyz0
> rank(ts
> COTTLOUCI
> adv20
> 5)) 。或者使用 hieh 和 volune
> 我们还需要考虑price_limit_condition 字段。我们需要了解price_limit_condition 足什么。
> 它可能是
> 个表示价格限制的字段 (例如涨跌停)。我们可以搜索该字段。
> (lo;


完成后，我手动将MCP提供的选择进行了回测（最近ds的reasoner不稳定，chat模式流水太快了），找到了一个还不错的信号。


> [!NOTE] [图片 OCR 识别内容]
> alpha
> pank(ts
> Corr(Vwap,
> Volume
> rank (max_price_increase_ratio);



> [!NOTE] [图片 OCR 识别内容]
> Chart
> OJZROI]
> 70



> [!NOTE] [图片 OCR 识别内容]
> 5 Summary
> Piou
> Tr INO Rcson ThCIC'?
> Rrtln Nh`
> d
> NTTT
>  NOOTHOOTITLN
> A5ToAl Oal
> 3.81
> 29,2995
> 2,74
> 15.1596
> 3.949
> 10,349


随后，我又把目光放在了其他数据字段的相关量价动量字段，借助MCP进行寻找，给了我如下结果：

**任务完成**

价格动量与价格限制组合 Alpha 表达式

基于您在 IND 区域（TOP500, D1）找到的价格动量相关 datafields，我为您设计了以下三个表达式，每个都包含经济学含义解释。

表达式 1：短期动量 × 价格限制

alpha = rank(short_horizon_momentum_score_float) * rank(price_limit_condition) *;*

**经济学含义** ：

- short_horizon_momentum_score_float 反映股票近期（短期）的价格动量强度，得分越高表示上涨势头越强。
- price_limit_condition 表示价格限制（如涨跌停）的严格程度，排名越高代表流动性约束越大。
- 两者相乘构建的信号认为： **短期动量强且流动性受限的股票，其动量效应可能因交易摩擦而持续更久** （买方需求无法充分释放，导致后续继续上涨）。该组合捕捉了市场微观结构扭曲下的动量增强效应。

表达式 2：全球动量排名 × 价格限制

alpha = rank(global_momentum_rank_float) * rank(price_limit_condition) *;*

**经济学含义** ：

- global_momentum_rank_float 是股票在全球 universe 中的动量排名（越高表示动量越强，需确认方向，假设排名越高动量越强）。
- 该表达式结合了 **全球相对动量** 与 **本地流动性约束** 。在全球范围内动量领先的股票，若在本地市场受到价格限制，可能意味着其强势尚未被完全定价（因为限制抑制了价格调整）。组合信号押注这类股票在限制解除后继续上涨。

表达式 3：价格动量模型短期成分 × 价格限制

alpha = star_pm_shortterm_d1 * rank(price_limit_condition) *;*

**经济学含义** ：

- star_pm_shortterm_d1 来自 Price Momentum Model，是专门建模的短期价格动量成分（已为标准化得分）。
- 该表达式直接使用模型输出的动量得分，避免了二次排名，保留了更多信息。与价格限制相乘后，信号强调 **模型认定的短期动量与流动性约束的交互作用** 。这可以视为对传统动量因子的流动性修正，旨在筛选出在限制环境下仍保持动量的股票。

推荐顺序

1. 优先测试  **表达式1** ，因为 short_horizon_momentum_score_float 使用广泛、覆盖率高，且短期动量与价格限制的组合直觉较强。
2. 若表达式1相关性仍高，可尝试  **表达式3** ，因为模型得分可能与其他 Alpha 的重叠度较低。
3. 表达式2作为备选，适合希望引入全球视角的策略。

回测后选择了信号最强的进行提交：


> [!NOTE] [图片 OCR 识别内容]
> alpha
> short_horizon
> momentum_score_float
> rank(price_Iimit_condition )



> [!NOTE] [图片 OCR 识别内容]
> Chart
> 1
> 50
> 
> a
> 177th
> 22



> [!NOTE] [图片 OCR 识别内容]
> I5 Summary
> Pericd
> Thers INOAn Ther
> NGL' KCU
> TNOTTNUONMNTILI'1
> FTr
> NOONOOIL5
> CNIORATo Dal
> 2.97
> 36.2195
> 1.78
> 13.0896
> 4099
> 7.22"


**总结：**

结合了MCP工具后，实现了IND地区的short-interest的一日手搓速通（用于点塔还是比较舒服的）。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
这个点塔的模式太优雅了，感谢大佬的分享。

理论上一个区域有效果，还可以横向扩展，AI/MCP用起来，补充个人的能力短板。

-----------------------------------------------------------------------------------------------------------

大模型的时代不知不觉就来了。。。用中学。。。


---

### 技术对话片段 127 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 借助MCP手搓IND地区short_interest点塔经验分享_36772326144279.md
- **时间**: 6个月前

**提问/主帖背景 (CY96125)**:
IND地区作为最近炙手可热的研究地区，作为新手的我当然不想错过这个机会，于是寻找数据字段进行点塔，看到了short interest模块只有三个字段，想去借助MCP工具尝试一波。

先去了解数据字段的含义：


> [!NOTE] [图片 OCR 识别内容]
> Roo 说
> 很好!  我找到了shortinterests数据集。从结果中可以看到。它昀10是"shortinterests"
> 名称
> 是 Daily Price Limit Data
> 描逑是关于上海。深圳和香港交易所的股票交易停牌和价格限制
> 数据。现在我恶要获取该数据集中的具体datafeld列衷。


MCP给出了三个datafields的经济学含义分析，在此因为篇幅原因不展开讲了，我的prompt里要求的是给出字段的经济学含义，并且组成可能的alpha expression，因此在最后给了我在Alpha构建中的应用建议：

1. **限制突破策略** :
2. **流动性压力指标** :
3. **市场情绪代理** :

在这个基础上，我先分别回测了这三个字段套上rank，发现了这三个数据字段回测的结果完全一样。综合了以上回测结果和MCP给予的指示，我想到了 **量价动量** 模型，先从pv字段去寻找，发现ts_corr(volume, close, 5)与short interest的字段结合信号强烈，但是pc太高了，于是去找MCP来解决问题.


> [!NOTE] [图片 OCR 识别内容]
> 首先。我需要查看这个alpha的详细信息。包括其表达式。性能等。使用MCP工具
> get_alpha_details
> 获取alpha信息。
> 同时。我将创建一个todo列表来跟踪步骤。
> 5  已更新待办事项列表
> ::分析经济学含义
> 黛理解现有表达式 -rank(ts_corr(close; volume; 5))
> :寻找替代字段构造相同意义的表达式
> ::组合rank(price_limit_condition)
> :提供建议和解释
> 获取alpha QPXIMAXM的详细信息



> [!NOTE] [图片 OCR 识别内容]
> Roo 说
> 现在分析经济学含义。该alpha的核心表达式足:
> alpha
> ank(ts_corr(close, volume
> 5))
> rank (price_Iimit_condition);
> 然后经过填充。缩尾。行业中性化。板块回填等处理。
> 古先
> COTTC052
> VO LUNe
> 5)计箅过去5天的收盘价与成交显的时间序列相关性。这个
> 相关性反映了价量关系:  正相关可能蒽味着价量齐升 (趋势跟随) ,负相关可能意味着价量
> 背离 (反转信号)。
> rark(:::)
> 衷示对相关性进行排名井取负。即相关性越高的股票得分越低
> (做空) ,相关性越低的股票得分越高  (做多)。这本质上是在押注价量相关性低的股票 (即
> 价显背离)  未来表现更好。而价屉相关性高的股票末来表现更耋。
> price_lipit_condition
> 是价格限制条件,可能是
> 个布尔值或数值。表示股票是否处于涨跌
> 停状态或其他价格限制情况。
> rank(price_Iimit_condition)
> 对其排名。可能表示价格限制程
> 度高的股票得分高。
> 两者相乘; alpha结合了价量背离信号和价格限制信号。经济学含义可能是:  价量背离的股票
> (可能意味着市场惰绪与价格走势不一致)加上价格限制 (流动性受限)  可能产生特殊的市
> 场异常收益。这种组合可能捕捉到市场微观结构中的定价无效宰。



> [!NOTE] [图片 OCR 识别内容]
> Roo
> 现在寻找替代字段。我们有许多价格和成交量字段: open high
> IOu
> WWaP
> returns。
> adv20等。我们可以构造以下替代表达式:
> ~rank(ts_Corr(open
> Volue
> 5))
> 使用开盘价代替收盘价。
> -pank(ts
> corr(hieh,
> Volue,
> 5))
> 使用最高价。
> ~pank(ts_corr
> Volume, 5))
> 使用最低价。
> ~rank(ts_corr(Vwap
> Volume
> 5))
> 使用成交显加权平均价。
> ~rank(ts
> CORRCROUUTI s
> volume, 5))
> 使用收益宰代替价格。
> ~rank(ts_corr(close,
> a420
> 5)
> 使用平均成交量代替日成交量。
> rank(ts_Corr(close
> 101
> 10))
> 改娈时间窗口。
> 8-rank(ts_corr(close
> Volue; 3))
> 更短窗口。
> 我们还可以使用其他相关性度显。例如ts
> 或ts_regression。 但为了保持相同意义;。我
> 们应坚持使用相关性。
> 此外;
> 我们可以使用其他技术指标,如md1135_del_tpv  (量价趋势)  或md1135_d3_ivn (负成
> 交显指数)。这些指标已经捕捉了价显关系。可能捉供类似的信号。
> 但用户要求"用其他的字段datafeld构造和-rankfts_corr(close; volume; 5))相同意义的
> expresslon
> 这意味着我们需要使用不同的数据字段。但产生相似的经济学含义。我们可以
> 选择与价量相关的宇段。但避免使用close和volume, 以降低相关性。
> 例如。使用 open 和 adyz0
> rank(ts
> COTTLOUCI
> adv20
> 5)) 。或者使用 hieh 和 volune
> 我们还需要考虑price_limit_condition 字段。我们需要了解price_limit_condition 足什么。
> 它可能是
> 个表示价格限制的字段 (例如涨跌停)。我们可以搜索该字段。
> (lo;


完成后，我手动将MCP提供的选择进行了回测（最近ds的reasoner不稳定，chat模式流水太快了），找到了一个还不错的信号。


> [!NOTE] [图片 OCR 识别内容]
> alpha
> pank(ts
> Corr(Vwap,
> Volume
> rank (max_price_increase_ratio);



> [!NOTE] [图片 OCR 识别内容]
> Chart
> OJZROI]
> 70



> [!NOTE] [图片 OCR 识别内容]
> 5 Summary
> Piou
> Tr INO Rcson ThCIC'?
> Rrtln Nh`
> d
> NTTT
>  NOOTHOOTITLN
> A5ToAl Oal
> 3.81
> 29,2995
> 2,74
> 15.1596
> 3.949
> 10,349


随后，我又把目光放在了其他数据字段的相关量价动量字段，借助MCP进行寻找，给了我如下结果：

**任务完成**

价格动量与价格限制组合 Alpha 表达式

基于您在 IND 区域（TOP500, D1）找到的价格动量相关 datafields，我为您设计了以下三个表达式，每个都包含经济学含义解释。

表达式 1：短期动量 × 价格限制

alpha = rank(short_horizon_momentum_score_float) * rank(price_limit_condition) *;*

**经济学含义** ：

- short_horizon_momentum_score_float 反映股票近期（短期）的价格动量强度，得分越高表示上涨势头越强。
- price_limit_condition 表示价格限制（如涨跌停）的严格程度，排名越高代表流动性约束越大。
- 两者相乘构建的信号认为： **短期动量强且流动性受限的股票，其动量效应可能因交易摩擦而持续更久** （买方需求无法充分释放，导致后续继续上涨）。该组合捕捉了市场微观结构扭曲下的动量增强效应。

表达式 2：全球动量排名 × 价格限制

alpha = rank(global_momentum_rank_float) * rank(price_limit_condition) *;*

**经济学含义** ：

- global_momentum_rank_float 是股票在全球 universe 中的动量排名（越高表示动量越强，需确认方向，假设排名越高动量越强）。
- 该表达式结合了 **全球相对动量** 与 **本地流动性约束** 。在全球范围内动量领先的股票，若在本地市场受到价格限制，可能意味着其强势尚未被完全定价（因为限制抑制了价格调整）。组合信号押注这类股票在限制解除后继续上涨。

表达式 3：价格动量模型短期成分 × 价格限制

alpha = star_pm_shortterm_d1 * rank(price_limit_condition) *;*

**经济学含义** ：

- star_pm_shortterm_d1 来自 Price Momentum Model，是专门建模的短期价格动量成分（已为标准化得分）。
- 该表达式直接使用模型输出的动量得分，避免了二次排名，保留了更多信息。与价格限制相乘后，信号强调 **模型认定的短期动量与流动性约束的交互作用** 。这可以视为对传统动量因子的流动性修正，旨在筛选出在限制环境下仍保持动量的股票。

推荐顺序

1. 优先测试  **表达式1** ，因为 short_horizon_momentum_score_float 使用广泛、覆盖率高，且短期动量与价格限制的组合直觉较强。
2. 若表达式1相关性仍高，可尝试  **表达式3** ，因为模型得分可能与其他 Alpha 的重叠度较低。
3. 表达式2作为备选，适合希望引入全球视角的策略。

回测后选择了信号最强的进行提交：


> [!NOTE] [图片 OCR 识别内容]
> alpha
> short_horizon
> momentum_score_float
> rank(price_Iimit_condition )



> [!NOTE] [图片 OCR 识别内容]
> Chart
> 1
> 50
> 
> a
> 177th
> 22



> [!NOTE] [图片 OCR 识别内容]
> I5 Summary
> Pericd
> Thers INOAn Ther
> NGL' KCU
> TNOTTNUONMNTILI'1
> FTr
> NOONOOIL5
> CNIORATo Dal
> 2.97
> 36.2195
> 1.78
> 13.0896
> 4099
> 7.22"


**总结：**

结合了MCP工具后，实现了IND地区的short-interest的一日手搓速通（用于点塔还是比较舒服的）。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
这个点塔的模式太优雅了，感谢大佬的分享。

理论上一个区域有效果，还可以横向扩展，AI/MCP用起来，补充个人的能力短板。

-----------------------------------------------------------------------------------------------------------

大模型的时代不知不觉就来了。。。用中学。。。


---

### 技术对话片段 128 (原帖: 分享自己实现的alpha数据库，一行代码保存所有alpha，并进行灵活查询！)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXzVDxRBo6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAjkBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzI4ODgzNDA4NzAyNzQzLSVFNSU4OCU4NiVFNCVCQSVBQiVFOCU4NyVBQSVFNSVCNyVCMSVFNSVBRSU5RSVFNyU4RSVCMCVFNyU5QSU4NGFscGhhJUU2JTk1JUIwJUU2JThEJUFFJUU1JUJBJTkzLSVFNCVCOCU4MCVFOCVBMSU4QyVFNCVCQiVBMyVFNyVBMCU4MSVFNCVCRiU5RCVFNSVBRCU5OCVFNiU4OSU4MCVFNiU5QyU4OWFscGhhLSVFNSVCOSVCNiVFOCVCRiU5QiVFOCVBMSU4QyVFNyU4MSVCNSVFNiVCNCVCQiVFNiU5RiVBNSVFOCVBRiVBMgY7CFQ6DnNlYXJjaF9pZEkiKWJhMTlhNmYzLWNmM2ItNDc0Ni04MzViLTZkZjA1NDM5ZTFkZAY7CEY6CXJhbmtpDToLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDExXNjc2NDAGOwhUOhJyZXN1bHRzX2NvdW50aRU%3D--51e30599746e1f7be6811f3a88fbf78a72e34d73
- **时间**: 1年前

**提问/主帖背景 (HQ17963)**:
本文基于纯python实现了一个具有添加和查询功能的alpha数据库。在此基础上实现了一行代码从旧到新获取所有alpha的操作。这份代码（见文末）经过较长时期使用，已充分验证了功能。用例1：创建/打开alpha数据库，并打印各区域alpha的保存情况。from sim_alpha_database import SimAlphaDatabasedata_dir_path=r'sim_alpha_database' # 可自定义储存位置sim_alpha_database=SimAlphaDatabase(data_dir_path)print(sim_alpha_database.region_universe_info_dict)结果：说明：该字典为每个区域已保存的alpha信息。其中键是(region, universe)参数，值是一个长度为4的列表。第1个参数为“该地区已保存的最新alpha的创建时间”，第2个参数为“分块保存的文件数”，第3个参数为“该地区已保存的alpha数量”，第4个参数为“最新创建时间相同的alpha_id”（用于避免重复保存相同的alpha）。用例2：保存所有回测的alpha。get_alpha_up_to_date()结果：说明：数据库中已有部分旧alpha时，只会获取新的alpha。若alpha数量超过10000，会自动分阶段获取全部alpha。用例3：查询符合条件的alpha。例如，查询AMR区域，TOP600 Universe，表达式含有”// using Time-Series Sentiment Comparison Template”字符串，且可进行Check Submission（即IS Testing Status中不存在fail）的alpha。定义查询函数：def filter(sim_alpha_result_list):picked_alphas=[]for result in sim_alpha_result_list:code=result['regular']['code']# lines=code.split('\n')# first_line=lines[0] # 可按行查询if '// using Time-Series Sentiment Comparison Template' not in code:continuefitness=result['is']['fitness']sharpe=result['is']['sharpe']turnover=result['is']['turnover']longCount=result['is']['longCount']shortCount=result['is']['shortCount']drawdown=result['is']['drawdown']margin=result['is']['margin']if fitness is None: # 排除没有fitness值的异常alphacontinue# if abs(fitness)<1: # 排除fitness绝对值小于1的alpha#     continue# if abs(sharpe)<1.58: # 排除sharpe绝对值小于1.58的alpha#     continue# if  longCount<60 or shortCount<60: # 排除longcount或shortcount小于60的alpha#     continue# if sharpe>8: # 排除pnl曲线为直角的异常alpha#     assert abs(drawdown)<0.01, result['id']#     continue# 排除IS Testing Status中有fail的alphachecks=result['is']['checks']check_dict={}ok=Truefor check in checks:check_dict[check['name']]=checkif check['result'] not in ['PASS','PENDING','WARNING']:assert check['result']=='FAIL'ok=Falsebreakif not ok:continuepicked_alphas.append(result)return picked_alphas查询：region="AMR"universe="TOP600"picked_alphas=sim_alpha_database.do_filter(filter,region,universe)print(f'picked_alphas: {len(picked_alphas)}')结果：关于查询性能：数据库实现了查询缓存功能，对于相同的查询函数，初次查询耗时稍长，后续查询极快。例如，在笔者电脑上，对AMR区域，TOP600 Universe中的296876个alpha进行上述查询，初次查询时间为4.3s，后续查询时间<0.1s。关于存储空间：数据库实现了3倍左右的数据压缩，平均使用空间为6.2MB/万alpha。数据库默认以1万个alpha进行分块储存和查询，避免将所有alpha装入内存，导致内存占用过多的问题。这份代码还有许多可以改进的地方，若有任何问题、看法、建议，欢迎在评论区留言，欢迎点赞支持，谢谢！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
非常喜欢您这个设计思路，在使用了几天后，我修改了两个字段，把每次从服务器拉去的条数改成了100条。之后再怎么运行都报错，尝试了修复pickle文件，还原修改的字段，删除pending文件等方法后，还是无法恢复。请帮忙分析一下：{('CHN', 'TOP2000U'): ['2024-12-27T06:29:07-05:00', 0, 7681, ['djLpJgv']], ('USA', 'TOP3000'): ['2025-01-01T01:24:56-05:00', 9, 99320, ['wj5mn9Y', 'rjb3Je3', 'Q7nJ2bg']], ('USA', 'TOP1000'): ['2024-10-14T10:02:18-04:00', 0, 3, ['olElR5l']], ('USA', 'TOP500'): ['2024-10-16T11:05:52-04:00', 0, 1, ['71GJZ35']], ('USA', 'TOP200'): ['2024-10-16T11:14:15-04:00', 0, 1, ['e01LVdM']], ('GLB', 'TOP3000'): ['2024-12-12T21:43:55-05:00', 0, 8102, ['JGOwKbO']], ('ASI', 'MINVOL1M'): ['2025-01-05T05:33:17-05:00', 14, 142646, ['X7bEY9l']], ('JPN', 'TOP1600'): ['2024-12-21T01:23:04-05:00', 8, 84541, ['EG2M9q0']], ('USA', 'ILLIQUID_MINVOL1M'): ['2024-12-02T12:01:12-05:00', 2, 28490, ['r2pQGdJ']], ('GLB', 'MINVOL1M'): ['2024-12-13T21:22:56-05:00', 1, 15256, ['m559VKW', 'KGGaEV8']], ('EUR', 'TOP1200'): ['2025-01-01T01:58:09-05:00', 21, 210387, ['n7nMQgd']], ('KOR', 'TOP600'): ['2024-12-16T04:37:41-05:00', 0, 5856, ['wab0zbQ']], ('ASI', 'ILLIQUID_MINVOL1M'): ['2024-12-04T05:33:30-05:00', 0, 3206, ['VGj9wY5']], ('AMR', 'TOP600'): ['2025-01-02T06:43:24-05:00', 22, 220295, ['Al3ALYQ']], ('USA', 'TOPSP500'): ['2024-11-21T06:17:43-05:00', 0, 338, ['g9WgRbv', 'GegKMl3']], ('HKG', 'TOP800'): ['2025-01-02T06:08:25-05:00', 12, 121231, ['ElKP9vG']], ('EUR', 'ILLIQUID_MINVOL1M'): ['2024-12-03T05:06:37-05:00', 0, 4854, ['pNmJv2q']], ('TWN', 'TOP500'): ['2025-01-04T07:35:49-05:00', 1, 15469, ['kjjr2eK']], ('HKG', 'TOP500'): ['2024-12-23T02:23:49-05:00', 0, 75, ['nNE3LN8']], ('TWN', 'TOP100'): ['2024-12-13T08:45:06-05:00', 0, 150, ['m5VMAVW']]}Starting to fetch alphas with time string: 2025-01-02T00:00:00-00:00Fetching URL:[链接已屏蔽] 50 results.Traceback (most recent call last):File "/home/ubuntu/world_quant/sim_alphas2db.py", line 443, in <module>get_alpha_up_to_date()File "/home/ubuntu/world_quant/sim_alphas2db.py", line 415, in get_alpha_up_to_datesim_alpha_database.add_multi_alpha_data(data["results"])File "/home/ubuntu/world_quant/sim_alphas2db.py", line 186, in add_multi_alpha_dataself.add_alpha_data(alpha_result)File "/home/ubuntu/world_quant/sim_alphas2db.py", line 149, in add_alpha_datalast_storage=self.load_last_storage(region,universe) # 同时会加载region_universe_info_dict^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^File "/home/ubuntu/world_quant/sim_alphas2db.py", line 82, in load_last_storagelast_storage = pickle.loads(compressed_pickle)^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^EOFError: Ran out of input


---

### 技术对话片段 129 (原帖: 分享自己实现的alpha数据库，一行代码保存所有alpha，并进行灵活查询！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 分享自己实现的alpha数据库一行代码保存所有alpha并进行灵活查询_28883408702743.md
- **时间**: 1年前

**提问/主帖背景 (HQ17963)**:
本文基于纯python实现了一个具有添加和查询功能的alpha数据库。在此基础上实现了一行代码从旧到新获取所有alpha的操作。这份代码（见文末）经过较长时期使用，已充分验证了功能。

**用例1：创建/打开alpha数据库，并打印各区域alpha的保存情况。**

```
from sim_alpha_database import SimAlphaDatabasedata_dir_path=r'sim_alpha_database' # 可自定义储存位置sim_alpha_database=SimAlphaDatabase(data_dir_path)print(sim_alpha_database.region_universe_info_dict)
```

结果：


> [!NOTE] [图片 OCR 识别内容]
> {('CHN'
> TOPzBBU' ): ['2824-18-38110:81:84-84:88
> 0,1599, [ `nglooza' ]],
> ( 'USA
> TOP1880' ): ['2824-11-27189:34:03-85:80
> 238,
> ['7nralwz']],
> ( 'USA
> TOP3888'): [`2824-12-82710:47:28-85:80
> 12,
> 124892, [ 'IpkEVZM' ]],
> ( 'USA
> TOP5BB' ):
> ['2024-18-23103:54:52-84:80'
> 9, ['6921E0]' ]],
> ( "USA
> TOP2B8' ):
> ['2824-11-38T16:37:80-05:80'
> 15894,
> [ 'NRYSLZE' ,
> ZRleg8X' ]],
> ('EUR
> ILLIQUID_MINVOLIN ):
> ['2824-11-30T01:39:18-05:88
> 1933,
> ['WErGIdp' ]],
> ('ASI
> MINVOLIM ):
> ['2824-12-87123:11:39-85:88
> 9887,
> [ 'WAwnggk' ]],
> AR
> TOP6BB" ): ['2024-12-22701:33:21-05:80
> 29,296876, ['7ZPAL7Z' ]],
> JPN
> TOPI688' ):
> ['2824-12-86189:39:45-85:80
> 11995,
> [ 'KGRBZWE
> B8zalRM' ]],
> ( 'KOR
> TOPGBB" ): ['2024-12-28128:01:04-05:80` _
> 249612,
> [ 'Nkqlqw ]],
> ( 'EUR
> TOP12O8' ):
> ['2824-12-29122:26:36-85:80
> 10,
> 102155,
> [ 'X7PRGSX'
> OQAO7WG' ]]}
> 24,


说明：该字典为每个区域已保存的alpha信息。其中键是(region, universe)参数，值是一个长度为4的列表。第1个参数为“该地区已保存的最新alpha的创建时间”，第2个参数为“分块保存的文件数”，第3个参数为“该地区已保存的alpha数量”，第4个参数为“最新创建时间相同的alpha_id”（用于避免重复保存相同的alpha）。

**用例2：保存所有回测的alpha。**

```
get_alpha_up_to_date()
```

结果：


> [!NOTE] [图片 OCR 识别内容]
> Starting to fetch alphas with time string: 2024-12-31702:29:09-05:80
> Fetching URL: https: Llapi worldqyantbrain comLusersLselflalphas?limit=5gg
> Fetched
> 5O results.
> Incrementing offset to:
> 58
> 181
> Fetching URL: https:Llapi worldqyantbrain comlusersLselflalphas?limits5gg
> Fetched
> 5O results.
> Incrementing Offset
> to:
> 188
> 181
> Fetching URL: https; Llapi worldqyantbrain comlusersLselflalphas?limit=5@g
> Fetched 58 results.
> Incrementing Offset
> to:
> 158
> 181
> Fetching URL: https:Llepi worldqyantbrain comluserslselflalphas?limitsSeg
> Fetched
> 31 results.
> Incrementing offset
> to:
> 288
> 181
> Fetching URL: https:Llapi worldqyantbrain comlusersLselflalphas?limit=seg
> Fetched
> 8 results.
> No more results found, returning:


说明：数据库中已有部分旧alpha时，只会获取新的alpha。若alpha数量超过10000，会自动分阶段获取全部alpha。

**用例3：查询符合条件的alpha。**

例如，查询AMR区域，TOP600 Universe，表达式含有”// using Time-Series Sentiment Comparison Template”字符串，且可进行Check Submission（即 **IS Testing Status** 中不存在fail）的alpha。

定义查询函数：

```
def filter(sim_alpha_result_list):    picked_alphas=[]    for result in sim_alpha_result_list:        code=result['regular']['code']                # lines=code.split('\n')        # first_line=lines[0] # 可按行查询        if '// using Time-Series Sentiment Comparison Template' not in code:            continue                    fitness=result['is']['fitness']        sharpe=result['is']['sharpe']        turnover=result['is']['turnover']        longCount=result['is']['longCount']        shortCount=result['is']['shortCount']        drawdown=result['is']['drawdown']        margin=result['is']['margin']        if fitness is None: # 排除没有fitness值的异常alpha            continue        # if abs(fitness)<1: # 排除fitness绝对值小于1的alpha        #     continue        # if abs(sharpe)<1.58: # 排除sharpe绝对值小于1.58的alpha        #     continue        # if  longCount<60 or shortCount<60: # 排除longcount或shortcount小于60的alpha        #     continue        # if sharpe>8: # 排除pnl曲线为直角的异常alpha        #     assert abs(drawdown)<0.01, result['id']        #     continue        # 排除IS Testing Status中有fail的alpha        checks=result['is']['checks']        check_dict={}        ok=True        for check in checks:            check_dict[check['name']]=check            if check['result'] not in ['PASS','PENDING','WARNING']:                assert check['result']=='FAIL'                ok=False                break         if not ok:            continue            picked_alphas.append(result)    return picked_alphas
```

查询：

```
region="AMR"universe="TOP600"picked_alphas=sim_alpha_database.do_filter(filter,region,universe)print(f'picked_alphas: {len(picked_alphas)}')
```

结果：


> [!NOTE] [图片 OCR 识别内容]
> picked_alphas:
> 1918



> [!NOTE] [图片 OCR 识别内容]
> picked_alphas [8]
> 00s
> {'id
> GGNe2SP
> Vype
> REGULAR
> author
> H017963
> settinBs
> {'instrumentType
> EQUITY
> region
> AR
> universe
> TOP68O
> delay
> decay
> neutralization
> COUNTRY
> truncation
> 88,
> pasteurization
> QN'
> unitHandling
> VERIFY
> nanHandline
> ON'
> language
> FASTEXPR
> Visualization
> False};
> regular
> Code
> 11 using
> Time-Series
> Sentiment Comparison Templatelnpositive
> sentiment
> description
> None,
> operatorCount
> 8},
> dateCreated
> 2824-12-16123:56:59-85:88
> datesuboitted
> None,
> datelodified
> 2824-12-16T23:57:80-85:88
> name
> None,
> favorite
> False
> hidden
> False,


**关于查询性能：**

数据库实现了查询缓存功能，对于相同的查询函数，初次查询耗时稍长，后续查询极快。

例如，在笔者电脑上，对AMR区域，TOP600 Universe中的296876个alpha进行上述查询，初次查询时间为4.3s，后续查询时间<0.1s。

**关于存储空间：**

数据库实现了3倍左右的数据压缩，平均使用空间为6.2MB/万alpha。

数据库默认以1万个alpha进行分块储存和查询，避免将所有alpha装入内存，导致内存占用过多的问题。

这份代码还有许多可以改进的地方，若有任何问题、看法、建议，欢迎在评论区留言，欢迎点赞支持，谢谢！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
非常喜欢您这个设计思路，在使用了几天后，我修改了两个字段，把每次从服务器拉去的条数改成了100条。之后再怎么运行都报错，尝试了修复pickle文件，还原修改的字段，删除pending文件等方法后，还是无法恢复。请帮忙分析一下：{('CHN', 'TOP2000U'): ['2024-12-27T06:29:07-05:00', 0, 7681, ['djLpJgv']], ('USA', 'TOP3000'): ['2025-01-01T01:24:56-05:00', 9, 99320, ['wj5mn9Y', 'rjb3Je3', 'Q7nJ2bg']], ('USA', 'TOP1000'): ['2024-10-14T10:02:18-04:00', 0, 3, ['olElR5l']], ('USA', 'TOP500'): ['2024-10-16T11:05:52-04:00', 0, 1, ['71GJZ35']], ('USA', 'TOP200'): ['2024-10-16T11:14:15-04:00', 0, 1, ['e01LVdM']], ('GLB', 'TOP3000'): ['2024-12-12T21:43:55-05:00', 0, 8102, ['JGOwKbO']], ('ASI', 'MINVOL1M'): ['2025-01-05T05:33:17-05:00', 14, 142646, ['X7bEY9l']], ('JPN', 'TOP1600'): ['2024-12-21T01:23:04-05:00', 8, 84541, ['EG2M9q0']], ('USA', 'ILLIQUID_MINVOL1M'): ['2024-12-02T12:01:12-05:00', 2, 28490, ['r2pQGdJ']], ('GLB', 'MINVOL1M'): ['2024-12-13T21:22:56-05:00', 1, 15256, ['m559VKW', 'KGGaEV8']], ('EUR', 'TOP1200'): ['2025-01-01T01:58:09-05:00', 21, 210387, ['n7nMQgd']], ('KOR', 'TOP600'): ['2024-12-16T04:37:41-05:00', 0, 5856, ['wab0zbQ']], ('ASI', 'ILLIQUID_MINVOL1M'): ['2024-12-04T05:33:30-05:00', 0, 3206, ['VGj9wY5']], ('AMR', 'TOP600'): ['2025-01-02T06:43:24-05:00', 22, 220295, ['Al3ALYQ']], ('USA', 'TOPSP500'): ['2024-11-21T06:17:43-05:00', 0, 338, ['g9WgRbv', 'GegKMl3']], ('HKG', 'TOP800'): ['2025-01-02T06:08:25-05:00', 12, 121231, ['ElKP9vG']], ('EUR', 'ILLIQUID_MINVOL1M'): ['2024-12-03T05:06:37-05:00', 0, 4854, ['pNmJv2q']], ('TWN', 'TOP500'): ['2025-01-04T07:35:49-05:00', 1, 15469, ['kjjr2eK']], ('HKG', 'TOP500'): ['2024-12-23T02:23:49-05:00', 0, 75, ['nNE3LN8']], ('TWN', 'TOP100'): ['2024-12-13T08:45:06-05:00', 0, 150, ['m5VMAVW']]}
Starting to fetch alphas with time string: 2025-01-02T00:00:00-00:00
Fetching URL:  [[链接已屏蔽]) 
Fetched 50 results.
Traceback (most recent call last):
  File "/home/ubuntu/world_quant/sim_alphas2db.py", line 443, in <module>
    get_alpha_up_to_date()
  File "/home/ubuntu/world_quant/sim_alphas2db.py", line 415, in get_alpha_up_to_date
    sim_alpha_database.add_multi_alpha_data(data["results"])
  File "/home/ubuntu/world_quant/sim_alphas2db.py", line 186, in add_multi_alpha_data
    self.add_alpha_data(alpha_result)
  File "/home/ubuntu/world_quant/sim_alphas2db.py", line 149, in add_alpha_data
    last_storage=self.load_last_storage(region,universe) # 同时会加载region_universe_info_dict
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/world_quant/sim_alphas2db.py", line 82, in load_last_storage
    last_storage = pickle.loads(compressed_pickle)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EOFError: Ran out of input


---

### 技术对话片段 130 (原帖: 好用的因子模板分享)
- **原帖链接**: [Commented] 好用的因子模板分享.md
- **时间**: 1年前

**提问/主帖背景 (XL31477)**:
```
[    {        "因子模板": "rank(ts_weighted_decay(ts_delta({field1}, 5), k=0.7)) * ts_corr(ts_min_diff({field2}, 10), ts_max({field3}, 15), 20)",        "模板idea": "计算字段在过去5个交易日的变化率，并应用加权衰减函数对其进行排名；然后计算两个字段在过去10个交易日最小差异和另一个字段在过去15个交易日的最大值之间的相关性。此因子结合了短期因子动量和中期相对强弱。",        "适用数据集": {            "field1": {                "analyst": ["analyst11"],                "earnings": ["earnings3"],                "fundamental": ["fundamental13"],                "model": ["model21"],                "imbalance": ["imbalance1"],                "insiders": ["insiders1"],                "institutions": ["institutions6"],                "macro": ["macro17"],                "other": ["other110"],                "news": ["news12"],                "option": ["option1"],                "socialmedia": ["socialmedia4"],                "sentiment": ["sentiment1"],                "risk": ["risk59"],                "pv": ["pv1"],                "shortinterest": ["shortinterest2"]            },            "field2": {                "analyst": ["analyst12"],                "earnings": ["earnings4"],                "fundamental": ["fundamental28"],                "model": ["model20"],                "imbalance": ["imbalance1"],                "insiders": ["insiders4"],                "institutions": ["institutions4"],                "macro": ["macro10"],                "other": ["other128"],                "news": ["news20"],                "option": ["option6"],                "socialmedia": ["socialmedia3"],                "sentiment": ["sentiment1"],                "risk": ["risk71"],                "pv": ["pv103"],                "shortinterest": ["shortinterest14"]            },            "field3": {                "analyst": ["analyst14"],                "earnings": ["earnings9"],                "fundamental": ["fundamental31"],                "model": ["model31"],                "imbalance": ["imbalance1"],                "insiders": ["insiders1"],                "institutions": ["institutions13"],                "macro": ["macro4"],                "other": ["other159"],                "news": ["news22"],                "option": ["option13"],                "socialmedia": ["socialmedia5"],                "sentiment": ["sentiment27"],                "risk": ["risk62"],                "pv": ["pv3"],                "shortinterest": ["shortinterest17"]            }        }}]
```

**解释：** 
1. rank(ts_weighted_decay(ts_delta({field1}, 5), k=0.7)):
   - ts_delta({field1}, 5): 计算字段1（{field1}）在最近5个交易日的变化率（差值）。
   - ts_weighted_decay(..., k=0.7): 对上述变化率应用一个加权衰减函数，其中k=0.7是衰减系数，表示越近期的数据权重越高。
   - rank(...): 对加权衰减后的结果进行排名，生成一个排名值。

1. ts_corr(ts_min_diff({field2}, 10), ts_max({field3}, 15), 20):
   - ts_min_diff({field2}, 10): 计算字段2（{field2}）在最近10个交易日的最小差异（可能是最小波动或最小变化）。
   - ts_max({field3}, 15): 计算字段3（{field3}）在最近15个交易日的最大值。
   - ts_corr(..., 20): 计算上述两个时间序列在过去20个交易日的相关性。
2. 整体因子: 将排名值与相关性值相乘，生成最终的因子值。

**模板idea (Template Idea)** 
- 短期动量: 通过计算字段1在过去5个交易日的变化率，并应用加权衰减函数进行排名，捕捉短期动量效应。
- 中期相对强弱: 通过计算字段2和字段3之间的相关性，其中字段2是过去10个交易日的最小差异，字段3是过去15个交易日的最大值，来衡量中期的相对强弱。

**适用场景** 
这个因子模板适用于那些需要结合短期动量和中期相对强弱的数据字段。通过结合排名和相关性分析，可以识别出具有潜在投资价值的股票。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享。我随便尝试了3个字段，有明显的信号。


---

### 技术对话片段 131 (原帖: 好用的因子模板分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 好用的因子模板分享_28752139913111.md
- **时间**: 1年前

**提问/主帖背景 (XL31477)**:
```
[    {        "因子模板": "rank(ts_weighted_decay(ts_delta({field1}, 5), k=0.7)) * ts_corr(ts_min_diff({field2}, 10), ts_max({field3}, 15), 20)",        "模板idea": "计算字段在过去5个交易日的变化率，并应用加权衰减函数对其进行排名；然后计算两个字段在过去10个交易日最小差异和另一个字段在过去15个交易日的最大值之间的相关性。此因子结合了短期因子动量和中期相对强弱。",        "适用数据集": {            "field1": {                "analyst": ["analyst11"],                "earnings": ["earnings3"],                "fundamental": ["fundamental13"],                "model": ["model21"],                "imbalance": ["imbalance1"],                "insiders": ["insiders1"],                "institutions": ["institutions6"],                "macro": ["macro17"],                "other": ["other110"],                "news": ["news12"],                "option": ["option1"],                "socialmedia": ["socialmedia4"],                "sentiment": ["sentiment1"],                "risk": ["risk59"],                "pv": ["pv1"],                "shortinterest": ["shortinterest2"]            },            "field2": {                "analyst": ["analyst12"],                "earnings": ["earnings4"],                "fundamental": ["fundamental28"],                "model": ["model20"],                "imbalance": ["imbalance1"],                "insiders": ["insiders4"],                "institutions": ["institutions4"],                "macro": ["macro10"],                "other": ["other128"],                "news": ["news20"],                "option": ["option6"],                "socialmedia": ["socialmedia3"],                "sentiment": ["sentiment1"],                "risk": ["risk71"],                "pv": ["pv103"],                "shortinterest": ["shortinterest14"]            },            "field3": {                "analyst": ["analyst14"],                "earnings": ["earnings9"],                "fundamental": ["fundamental31"],                "model": ["model31"],                "imbalance": ["imbalance1"],                "insiders": ["insiders1"],                "institutions": ["institutions13"],                "macro": ["macro4"],                "other": ["other159"],                "news": ["news22"],                "option": ["option13"],                "socialmedia": ["socialmedia5"],                "sentiment": ["sentiment27"],                "risk": ["risk62"],                "pv": ["pv3"],                "shortinterest": ["shortinterest17"]            }        }}]
```

**解释：** 
1. rank(ts_weighted_decay(ts_delta({field1}, 5), k=0.7)):
   - ts_delta({field1}, 5): 计算字段1（{field1}）在最近5个交易日的变化率（差值）。
   - ts_weighted_decay(..., k=0.7): 对上述变化率应用一个加权衰减函数，其中k=0.7是衰减系数，表示越近期的数据权重越高。
   - rank(...): 对加权衰减后的结果进行排名，生成一个排名值。

1. ts_corr(ts_min_diff({field2}, 10), ts_max({field3}, 15), 20):
   - ts_min_diff({field2}, 10): 计算字段2（{field2}）在最近10个交易日的最小差异（可能是最小波动或最小变化）。
   - ts_max({field3}, 15): 计算字段3（{field3}）在最近15个交易日的最大值。
   - ts_corr(..., 20): 计算上述两个时间序列在过去20个交易日的相关性。
2. 整体因子: 将排名值与相关性值相乘，生成最终的因子值。

**模板idea (Template Idea)** 
- 短期动量: 通过计算字段1在过去5个交易日的变化率，并应用加权衰减函数进行排名，捕捉短期动量效应。
- 中期相对强弱: 通过计算字段2和字段3之间的相关性，其中字段2是过去10个交易日的最小差异，字段3是过去15个交易日的最大值，来衡量中期的相对强弱。

**适用场景** 
这个因子模板适用于那些需要结合短期动量和中期相对强弱的数据字段。通过结合排名和相关性分析，可以识别出具有潜在投资价值的股票。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢分享。我随便尝试了3个字段，有明显的信号。


---

### 技术对话片段 132 (原帖: 存货周转率疑义探讨)
- **原帖链接**: [Commented] 存货周转率疑义探讨.md
- **时间**: 1年前

**提问/主帖背景 (YH82809)**:

> [!NOTE] [图片 OCR 识别内容]
> 存货周转率
> 财务比率是基本面数据的比率。可以深入了解公司的健康状况和投资决策。
> -种常见的财务比率是存货周转
> 率。它是一种活动比率。用于衡量公司销售和替换存货的速度。计算公式为:
> InuentoryTurnouer
> Saleg | AuerageInuentory
> 销售额除以平均存货
> 通常。较高的存货水平与更高的存储成本。保险费用和损耗有关。假设是具有较高存货周转率的股票将具有
> 较差的股票表现。因此将被分配负权重。
> 其Alpha表达式如下:
> inventory
> turnover


在我们的学习课程周，有一个存货周转率的目标，课程中假设了具有较高存货周转率的股票将具有较差的股票表现，因此将被分配负权重，我认为恰恰相反，理由如下：

1. ‌存货周转率的定义与意义‌
存货周转率（销售额 ÷ 平均存货）衡量企业存货转化为销售收入的效率。‌高周转率‌通常表明企业能快速销售存货，减少库存积压，从而降低存储成本、保险费用和损耗风险‌；

2. ‌课程假设的矛盾点‌
 课程中假设“高存货周转率对应较差的股票表现”存在逻辑矛盾。根据企业运营常识和财务理论：2.1   高周转率的正向影响‌：

2.1.1成本控制‌：减少存货持有时间可降低仓储成本、陈旧风险（如易损坏或过时）‌
      2.1.2 流动性提升‌：快速回笼资金，增强企业现金流和偿债能力‌
 ‌     2.2    股票表现关联性‌：
              高效存货管理通常反映企业运营能力较强，可能提升盈利预期，进而推动股价正向

表现‌.

3. ‌假设可能存在的误解‌
   若假设“高周转率对应负权重”，需注意以下可能错误：
‌3.1 混淆指标方向‌：
      高周转率是效率指标，通常与正收益相关；若需反映“存货积压风险”，应关注‌低周转率‌ （如存货滞销导致的资产减值风险）‌
3‌.2 模型设计偏差‌：
    若模型将高周转率直接与负权重挂钩，可能未考虑周转率与盈利能力的非线性关系（如过

高周转率可能引发供应链压力）‌;

4. ‌改进建议‌
4‌.1 变量调整‌：
若需反映存货积压风险，建议使用‌低周转率‌或‌存货减值比例‌作为负权重指标‌
4‌.2 多维度验证‌：
结合其他财务指标（如毛利率、现金流）综合分析周转率的影响，避免单一指标误导结论‌

这是个人意见，供大家参考讨论。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我最近也在尝试手工做一些alpha，找了很多的研报，包括尝试论坛的里alpha灵感系列。我也遇到了类似的问题，一个看似合理的逻辑，往往回测的结果并不好。一些相对简单直接的交易想法所蕴含的信息，可能早已被市场参与者充分挖掘并消化。换句话说，这些想法所基于的逻辑在当前市场环境下已不再具备明显的优势，难以有效形成具有盈利能力的 alpha 因子。其次，回到回测本身，这里面的问题可能是忽略了一些细节，有时候可能换一个neutralization后，回测的结果就有改善。

这可能也是研究alpha的意义所在，有一个好的出发点，还需要不断的去完善，也许最后的结果与我们的出发点可能会差异很大，反复的验证、调整与优化，才能有望开发出具有实际应用价值的 alpha 策略，在复杂多变的金融市场中获取超额收益。

作为一名新手，以上内容仅供参考，不一定对啊。


---

### 技术对话片段 133 (原帖: 存货周转率疑义探讨)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 存货周转率疑义探讨_30668648522519.md
- **时间**: 1年前

**提问/主帖背景 (YH82809)**:

> [!NOTE] [图片 OCR 识别内容]
> 存货周转率
> 财务比率是基本面数据的比率。可以深入了解公司的健康状况和投资决策。
> -种常见的财务比率是存货周转
> 率。它是一种活动比率。用于衡量公司销售和替换存货的速度。计算公式为:
> InuentoryTurnouer
> Saleg | AuerageInuentory
> 销售额除以平均存货
> 通常。较高的存货水平与更高的存储成本。保险费用和损耗有关。假设是具有较高存货周转率的股票将具有
> 较差的股票表现。因此将被分配负权重。
> 其Alpha表达式如下:
> inventory
> turnover


在我们的学习课程周，有一个存货周转率的目标，课程中假设了具有较高存货周转率的股票将具有较差的股票表现，因此将被分配负权重，我认为恰恰相反，理由如下：

1. ‌存货周转率的定义与意义‌
存货周转率（销售额 ÷ 平均存货）衡量企业存货转化为销售收入的效率。‌高周转率‌通常表明企业能快速销售存货，减少库存积压，从而降低存储成本、保险费用和损耗风险‌；

2. ‌课程假设的矛盾点‌
 课程中假设“高存货周转率对应较差的股票表现”存在逻辑矛盾。根据企业运营常识和财务理论：2.1   高周转率的正向影响‌：

2.1.1成本控制‌：减少存货持有时间可降低仓储成本、陈旧风险（如易损坏或过时）‌
      2.1.2 流动性提升‌：快速回笼资金，增强企业现金流和偿债能力‌
 ‌     2.2    股票表现关联性‌：
              高效存货管理通常反映企业运营能力较强，可能提升盈利预期，进而推动股价正向

表现‌.

3. ‌假设可能存在的误解‌
   若假设“高周转率对应负权重”，需注意以下可能错误：
‌3.1 混淆指标方向‌：
      高周转率是效率指标，通常与正收益相关；若需反映“存货积压风险”，应关注‌低周转率‌ （如存货滞销导致的资产减值风险）‌
3‌.2 模型设计偏差‌：
    若模型将高周转率直接与负权重挂钩，可能未考虑周转率与盈利能力的非线性关系（如过

高周转率可能引发供应链压力）‌;

4. ‌改进建议‌
4‌.1 变量调整‌：
若需反映存货积压风险，建议使用‌低周转率‌或‌存货减值比例‌作为负权重指标‌
4‌.2 多维度验证‌：
结合其他财务指标（如毛利率、现金流）综合分析周转率的影响，避免单一指标误导结论‌

这是个人意见，供大家参考讨论。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
我最近也在尝试手工做一些alpha，找了很多的研报，包括尝试论坛的里alpha灵感系列。我也遇到了类似的问题，一个看似合理的逻辑，往往回测的结果并不好。一些相对简单直接的交易想法所蕴含的信息，可能早已被市场参与者充分挖掘并消化。换句话说，这些想法所基于的逻辑在当前市场环境下已不再具备明显的优势，难以有效形成具有盈利能力的 alpha 因子。其次，回到回测本身，这里面的问题可能是忽略了一些细节，有时候可能换一个neutralization后，回测的结果就有改善。

这可能也是研究alpha的意义所在，有一个好的出发点，还需要不断的去完善，也许最后的结果与我们的出发点可能会差异很大，反复的验证、调整与优化，才能有望开发出具有实际应用价值的 alpha 策略，在复杂多变的金融市场中获取超额收益。

作为一名新手，以上内容仅供参考，不一定对啊。


---

### 技术对话片段 134 (原帖: 实测不同中性化策略的性能及信号数量：以动量模版为例经验分享)
- **原帖链接**: [Commented] 实测不同中性化策略的性能及信号数量以动量模版为例经验分享.md
- **时间**: 7个月前

**提问/主帖背景 (HQ20665)**:
对于新人来说，我在跑模板的时候，常常不知道怎么选择中性化，跑一阶段任务的时候，不同的中性化策略会影响测试速度，挖掘的信号数量，因此找到一个合适的中性化策略尤其重要。

在近期的研究中，我尝试对比了不同中性化策略在相同模板下的执行性能与信号数量。测试目标是了解在相同的数据集、相同公式框架下，不同中性化方式对模拟耗时与 alpha 输出数量的影响。通过实际测试，加深对中性化策略的理解。

我选用的模版是经典的动量方程（考虑到它是简单的一阶表达式公式，且有经济学意义）。具体公式为：

```
ts_av_diff(<norm/>({field}),{day})
```

norm为对字段的数据处理，选择算术变换signed_power、时间平滑ts_zscore、截面标准化rank。

测试数据集随机选择EUR TOP25000基本面类数据集，模版产生的测试数量为1752个，设置不同的中性化策略进行模拟，然后记录每个alpha的平均耗时 和 信号数量。测试的中性化有：MARKET，CROWDING，RAM，SECTOR，INDUSTRY，COUNTRY，STATISTICAL，SUBINDUSTRY，FAST，SLOW_AND_FAST，SLOW。

- **平均耗时分析**


> [!NOTE] [图片 OCR 识别内容]
> 平均耗时(秒)
> 91.8
> 95.1
> 100
> 90
> 80
> 70
> 70
> 60
> 50
> 40
> 23.3
> 30
> 16.6
> 17.3
> 18.7
> 19.2
> 19.4
> 19.9
> 20
> 20
> 10
> 簋
> 簋
> MARKET
> CROWDING
> RAM
> SECTOR
> INDUSTRY
> COUNTRY
> SUBINDUSTRY
> STATISTICAL
> SLOW
> _AND
> SLOW_


可以看到 FAST，SLOW_AND_FAST，SLOW 策略跑得最慢，约为其他中性化耗时的3~5倍.

- **信号数量分析**


> [!NOTE] [图片 OCR 识别内容]
> 信号量(个)
> 15
> 12
> 12
> 11
> 
> RAM
> INDUSTRY
> COUNTRY
> SUBINDUSTRY
> FAST
> 簋
> CROWDING
> SECTOR
> SLOW
> STATISTICAL
> _AND_
> SLOW_


可以看到INDUSTRY, STATISTICAL, SUBINDUSTRY,  FAST产生的信号数量是最多的，均大于10.

因为现在PPA提交限定在风险类中性化因子，因此可以直接选择STATISTICAL作为中性化策略，兼顾回测速度与信号数量。

在进行大规模回测的时候，也可以在一阶使用速度更快的中性化，在二阶的时候切换到其他风险类中性化。

通过这次实验，为今后的研究提供了中性化选择思路。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢楼主的发帖，很有启发性。

learn文档里有一篇内容是说明如何设置中性化的，特别是不同的数据分类推荐了不同的中性化分组，但没有包括风险中性化的推荐， 其中的基本面数据推荐的中性化就是INDUSTRY。

论坛里还有一篇一键测试稳定性的帖子。

结合这些内容，我主观的认为好的表达式应该在不同的中性化下应该不会有大幅的差异，进而确实应该选择最快速的中性化用于回测，同时对不同的数据分类尽量考虑官方推荐的常规中性化分组，有信号后再选择风险中性化。


---

### 技术对话片段 135 (原帖: 实测不同中性化策略的性能及信号数量：以动量模版为例经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 实测不同中性化策略的性能及信号数量以动量模版为例经验分享_36302287798295.md
- **时间**: 7个月前

**提问/主帖背景 (HQ20665)**:
对于新人来说，我在跑模板的时候，常常不知道怎么选择中性化，跑一阶段任务的时候，不同的中性化策略会影响测试速度，挖掘的信号数量，因此找到一个合适的中性化策略尤其重要。

在近期的研究中，我尝试对比了不同中性化策略在相同模板下的执行性能与信号数量。测试目标是了解在相同的数据集、相同公式框架下，不同中性化方式对模拟耗时与 alpha 输出数量的影响。通过实际测试，加深对中性化策略的理解。

我选用的模版是经典的动量方程（考虑到它是简单的一阶表达式公式，且有经济学意义）。具体公式为：

```
ts_av_diff(<norm/>({field}),{day})
```

norm为对字段的数据处理，选择算术变换signed_power、时间平滑ts_zscore、截面标准化rank。

测试数据集随机选择EUR TOP25000基本面类数据集，模版产生的测试数量为1752个，设置不同的中性化策略进行模拟，然后记录每个alpha的平均耗时 和 信号数量。测试的中性化有：MARKET，CROWDING，RAM，SECTOR，INDUSTRY，COUNTRY，STATISTICAL，SUBINDUSTRY，FAST，SLOW_AND_FAST，SLOW。

- **平均耗时分析**


> [!NOTE] [图片 OCR 识别内容]
> 平均耗时(秒)
> 91.8
> 95.1
> 100
> 90
> 80
> 70
> 70
> 60
> 50
> 40
> 23.3
> 30
> 16.6
> 17.3
> 18.7
> 19.2
> 19.4
> 19.9
> 20
> 20
> 10
> 簋
> 簋
> MARKET
> CROWDING
> RAM
> SECTOR
> INDUSTRY
> COUNTRY
> SUBINDUSTRY
> STATISTICAL
> SLOW
> _AND
> SLOW_


可以看到 FAST，SLOW_AND_FAST，SLOW 策略跑得最慢，约为其他中性化耗时的3~5倍.

- **信号数量分析**


> [!NOTE] [图片 OCR 识别内容]
> 信号量(个)
> 15
> 12
> 12
> 11
> 
> RAM
> INDUSTRY
> COUNTRY
> SUBINDUSTRY
> FAST
> 簋
> CROWDING
> SECTOR
> SLOW
> STATISTICAL
> _AND_
> SLOW_


可以看到INDUSTRY, STATISTICAL, SUBINDUSTRY,  FAST产生的信号数量是最多的，均大于10.

因为现在PPA提交限定在风险类中性化因子，因此可以直接选择STATISTICAL作为中性化策略，兼顾回测速度与信号数量。

在进行大规模回测的时候，也可以在一阶使用速度更快的中性化，在二阶的时候切换到其他风险类中性化。

通过这次实验，为今后的研究提供了中性化选择思路。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢楼主的发帖，很有启发性。

learn文档里有一篇内容是说明如何设置中性化的，特别是不同的数据分类推荐了不同的中性化分组，但没有包括风险中性化的推荐， 其中的基本面数据推荐的中性化就是INDUSTRY。

论坛里还有一篇一键测试稳定性的帖子。

结合这些内容，我主观的认为好的表达式应该在不同的中性化下应该不会有大幅的差异，进而确实应该选择最快速的中性化用于回测，同时对不同的数据分类尽量考虑官方推荐的常规中性化分组，有信号后再选择风险中性化。


---

### 技术对话片段 136 (原帖: 微信Clawbot接通AI打工人经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 微信Clawbot接通AI打工人经验分享_39289349830295.md
- **时间**: 2个月前

**提问/主帖背景 (DZ31817)**:
最近微信开放了clawbot插件，可以链接openclaw。这里介绍一款插件，可以使微信clawbot桥接到claude code、codex、gemini等openclaw以外的CLI。

[[链接已屏蔽])

安装很简单，按README的步骤一步安装到位，之后即可在微信中连通你电脑上的claude code、codex、gemini，如图：


> [!NOTE] [图片 OCR 识别内容]
> 15:08
> 17
> 微信 ClawBot
> A
> JcX 你好你是谁
> 你好,
> 我是 Codex,
> 一个
> Al 编程助手。
> 0
> 我可以帮你:
> 看代码
> 改代码
> 查问题
> 写脚本。命令 
> 测试
> 解释技术方案,
> 做代码 review
> 如果你有项目或报错,
> 直接发给我。
> 14:31
> Jcc 你好  你是谁
> 你好!我是 Claude,
> Anthropic 开发的 Al 助手。
> 0
> 有什么我可以帮你做的吗?
> Igm 你好你是谁
> 你好!我是 Gemini CLI,
> 一个由 Google 训练的
> 大型语言模型。专门为您提供软件工程任务方面
> 的协助。我可以在命令行环境中帮助您编写代
> 码。分析项目。修复 Bug 以及执行各种开发相
> 关的操作。
> 有什么我可以帮您的吗?
> OoO
> 510


接下来，如果你已经在claude code、codex或gemini中配置了AI打工人agent，就可以直接在微信上跟它对话了：


> [!NOTE] [图片 OCR 识别内容]
> 14:40
> 16
> 微信 ClawBot
> Al
> 你好  你是谁
> 我是这个仓库里的 WorldQuant Codex 助手。
> 我可以直接帮你做几类事:
> 查和用 WorldQuant BRAIN 相关能力
> 做 alpha 研究
> 改进表达式
> 看回测结果
> 分析数据集
> datafield
> submission 质量
> 相关性
> 直接改这个项目里的代码
> 脚本和工作流
> 如果你有具体目标,
> 直接说一句就行,
> 比如:
> 帮我分析-个 alpha
> 帮我批量跑模拟
> 帮我看看怎么提高通过率 `
> 我  是
> 你好
> 你  这  嗯
> 自由
> 这个
> C
> V
> 
> p
> 9
> S
> 0
> 9
> h
> K
> 乙
> 0
> 门
> m
> 123
> 空格
> 换行



> [!NOTE] [图片 OCR 识别内容]
> 14:48
> 15
> 微信 ClawBot
> Al
> 帮我看下最近回测的10个因子的表现,形成简短的
> 分析报告
> 归
> 14:47
> 按 BRAIN 里最近创建的 10
> IS 因子看,
> 这一
> 批都来自同-一条
> USAITOP3OOOIDIIMACRO`
> 主线,
> 创建时间都是
> 2026-03-2302:42:48
> -04:00 `
> 整体结论是:  底层信号有一定有效
> 性,
> 但这一批还不适合直接提交。10 个里有8
> 个是正 Sharpe,
> 去掉两个明显失效的
> ts_kurtosis
> 版本后。剩余8 个的平均
> Sharpe
> 约
> 1.41'
> 平均
> Returns
> 约
> 7.549
> 平均
> Turnover
> 约
> 68.59
> 平均
> Drawdown
> 约
> 8.89/`; 但
> Fitness
> 全部低
> 于
> 1.0`,
> 而且我抽查的 4个头部候选
> production correlation-
> 都高于
> 0.7 ,
> 说明这
> 条 macro 主线已经比较拥挤。
> 表现最好的三个是
> 58916012
> ts_aV_diff(.., 5) `:
> Sharpe
> 1.83
> Returns 10.219
> 但
> Turnover
> 0.922
> 过高,
> Concentrated Weight
> 和
> IS ladder sharpe
> 也失败,
> prod corr
> 0.788
> VRSbYX7d
> Signed_powerl.. 0.5) `:
> Sharpe 1.49
> Returns 8.039
> Drawdown 7.549
> 是更均衡的版本,
> 但
> 21651


注：默认的对话方式是每次新的对话都重新拉起一次CLI通话，因此是没有记忆的。若要达到跟CLI中对话一样的效果，需要通过ACP长驻子进程，通过 stdio通信，该插件也是支持ACP的。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
厉害啦，感谢分享。这是随时当pm监控ai干活的节奏。

大佬，你这么多ai，每个月的花费可不低。希望有时间能反馈一下：效果/产出？

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================


---

### 技术对话片段 137 (原帖: src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    ...    获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...]))
- **原帖链接**: [Commented] 构建 724 小时不间断 Alpha 回测系统基于 Celery 和动态任务队列的架构分享代码优化.md
- **时间**: 1年前

**提问/主帖背景 (BL72197)**:
### 背景

大家好，我是量化新人小白，5 月底成为了有条件顾问，从老师的 alpha_machine 代码起步跑 123 阶任务，开启了 WQ 之旅。在量化研究中，我们常常遇到一个痛点：Alpha 表达式的生成过程与回测执行过程紧密耦合。这导致我们无法灵活地管理回测任务，比如有了新的想法想想跑个回测，要么得排队等，要么就得手动启停任务，一不小心就把跑了一半的进程给干掉了，而那些表达式回测了那些没有回测不知道，还要时不时要看看回测执行到哪里了，任务半夜执行完了或者完成了都不知道=。=，没法及时添加新的回测任务等情况大家应该深有体会。

### 系统架构设计

为了解决这个问题，我对现有的代码进行了魔改，引入了数据库（建议使用 ORM，不用手撕 SQL，如异步库 tortoise-orm）管理表达式、创建任务队列和利用 celery 实现回测任务调度，直接上架构图：
 
> [!NOTE] [图片 OCR 识别内容]
> Alpha 数据库
> Alpha 回测队列
> Celery 任务调度
> 定时任务
> 用户IAPI
> 用户IAPI
> 按队列优先级
> 查找未开始的队列
> templatelidea 生成表
> 任务调度给空闲的
> 达式
> handle_alpha_queue
> Worker
> 存储数据库
> Workerl
> Worker2
> 加入队列的进
> 行标记
> WorkerN
> 新增回测队列
> 查询回测队列
> DB
> 删除队列的取
> worker 执行回测
> 消标记
> 没有队列时发
> 删除回测队列
> 送消息提醒
> 开始
> 完成后
> 消息机器人
> 发送逍息提醒
 

系统逻辑很简单，就三块，各干各的，互不影响：

1. 随时基于模版或者新的 idea 创建表达式和 settings 存入表 alpha_expressions 中，标记表达式状态是否已被取样、是哪个模版、是几阶表达式、源表达式（之后用于剪枝）。
2. 管理待回测的任务队列，从数据库中选择自己想要跑的表达式加入到回测队列中，设置数量、优先级、出自哪个模版等，可以随时添加或删除不想执行回测的队列。
3. 利用 celery 定时任务，定时检查是否有空闲的 worker（对应一个回测槽位），如果有就将未开始的任务队列分配给它进行回测。另外还有定时任务将回测结果拉回本地存进服务器和其他自相关检查、分析等任务

这样实现之后，我不用去关注回测的执行情况，没有回测队列和任务完成会有机器人实现提醒，接下来重点就是挖掘新的 alpha idea 就可以了。
 
> [!NOTE] [图片 OCR 识别内容]
> (env)
> [rooteiv-ydwszexqtck3Gdlaadfy my_alpha_machine] # python3 handlealpha_queue .Py
> list
> -5
> 1
> 2025-06-25
> 16:16:
> 809
> Src . database. config
> INFO
> 芷在连接到数据库
> localhost: 5432/alpha_machine-
> 2025-06-25
> 16:16:22,822
> src. database. conf g
> INFO
> 数据库连接成功
> 2025-06-25
> 16:16:22,822
> Src . database. conf g
> INFO
> 正在生成数据库表结构
> 2025-06-25
> 16:16:22,845
> src . database . confg
> INFO
> 数据库表结构生成完成
> 2025-06-25
> 16:16:22,880
> Src. core.alpha_queue
> INFO
> 共找到3个回测队列:
> 2025-06-25
> 16:16:22,880
> SrC.Core.
> alpha_queue
> INFO
> ID:
> 28,名称 : template_2_500_3阶 _优先级7,状态
> 莲篌
> 优先级 :
> 7,数量
> 500
> 2025-06-25
> 16:16:22,880
> Src. core.alpha_queue
> INFO
> ID:
> 27,
> 名称 : template_2-500_3阶-优先级7, 状态
> 优先级 :
> 7,数量
> 500
> 2025-06-25
> 16:16:22,880
> Src.core.alpha_queue
> INFO
> ID:
> 26
> 名称: template_2_500_3阶 _优先级7,状态:  迸行中
> 优先级: 7。数量:
> 500
> 2025-06-25
> 16:16:22,880
> Src.database.
> conflg
> INFO
> 正在关闭数据库连接
> 2025-06-25
> 16:16:22,882
> tortoise
> INFO
> Tortoise-ORM
> Shutdown
> 2025-06-25
> 16:16:22,882
> Src . database.
> config
> INFO
> 数据库连接已关闭
> (env)
> [rooteiv-ydwszexgtck3Gdlaadfy my_alpha_machine] # python3 handle alpha_queue . Py
> list
> 5
> 2025-06-25
> 16:16:26,677
> Src . database.
> conf B
> INFO
> 芷在连接到数据库
> localhost: 5432/alpha_machine
> 2025-06-25
> 16:16:26,690
> Src . database. conf g
> INFO
> 数据库连接成功
> 2025-06-25
> 16:16:26,690
> src . database. confg
> INFO
> 正在生成数据库表结构
> 2025-06-25
> 16:16:26,713
> src . database. conf 语
> INFO
> 数据库表结构生成完成
> 2025-06-25
> 16:16:26,749
> SrC.Core.
> alpha_queue
> INFO
> 共找到12个回测队列
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 37,名称:
> template_2_500_3阶
> 优
> 500
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 36,
> 称
> template_2_500_3阶
> ~优先级
> 500
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 35,
> 称
> template_2_500_3阶 -优先级
> 蟹
> 先
> 趸
> 500
> 2025-06-25
> 16:16:26,749
> SrC.Core.
> alpha_queue
> INFO
> ID:
> 34,
> 称
> template_2_500_3阶 -优先级
> 500
> 2025-06-25
> 16:16:26,749
> STC.Core.
> alpha_queue
> INFO
> ID:
> 称
> template_2_500_3阶
> 先
> #
> 7
> 500
> 2025-06-3
> 1:16:7,749
> src. core。
> alha_queue
> HFO
> k:
> 翌;
> 1
> 黎
> template Z_500_3阶
> :
> 筅
> 蠡
> 7
> (`
> 5
> 2025-06-25
> 16:16:26,749
> SrC.core.
> alpha_queue
> INFO
> ID:
> 30,
> template_2_500_3阶
> 50
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 29,
> 称
> template_2_500_3阶
> ~优先级
> 7;
> 500
> 2025-06-25
> 16:16:26,749
> SrC.Core
> alpha_queue
> INFO
> ID:
> 22,
> 称
> template_2_500_3阶 -优先级6,
> 优先
> 6,
> 500
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 21,
> 名称
> template_2_500_3阶 -优先级6,
> 优先
> 6,
> 500
> 2025-06-25
> 16:16:26,749
> SrC.Core
> alpha_queue
> INFO
> ID:
> 20
> 名称: template_2_500_3阶 _优先级6,状态
> 未开始
> 优先级: 6,
> 500
> 2025-06-25
> 16:16:26,749
> Src . database . config
> INFO
> 正在关闭数据库连接 .
> 2025-06-25
> 16:16:26,751
> tortoise
> INFO
> Tortoise-ORM
> Shutdown
> 2025-06-25
> 16:
> 16:26,751
> Src .database . config
> INFO
> 数据库连接已关闭
> on
> 「rnntai-VAIC7oynt k36412adfr
> I
> 37nh2
> m2Chino7 #
> 22,
> 33,
 
 
> [!NOTE] [图片 OCR 识别内容]
> 4:40
> bj 的机器人
> BOT
> 回测队列已完成: template_2_500_13阶_优先级9
> 队列I0: 40
> 工作进程: worker2
> 成功数: 486
> 失败数: 14
> 耗时: 659分钟
> bj的机器人
> BOT
> 开始回测队列: template_2_500_3阶_优先级7
> 队列I0:28
> 工作进程: Worker2
> 优先级:7
> 表达式数量: 500
 

### 关键代码实现

1. 任务队列模型（Tortoise-ORM），好处是不需要手撕 SQL，查询的每一行结果是一个对象，可以直接用属性来访问每个字段。

```
# src/models/alpha_models.pyclass AlphaBacktestQueue(Model):"""Alpha回测队列模型"""    id=fields.IntField(pk=True)    alpha_expression_ids=fields.JSONField(description="Alpha表达式ID列表")    queue_name=fields.CharField(max_length=50,description="队列名称")    queue_count=fields.IntField(default=0,description="队列数量")    priority=fields.IntField(default=5,description="优先级")    created_at=fields.DatetimeField(auto_now_add=True,description="创建时间")    status=fields.IntField(default=0,description="状态")# 0: 未开始 1: 进行中 2: 已完成 -1: 失败    start_time=fields.DatetimeField(null=True,description="开始时间")    end_time=fields.DatetimeField(null=True,description="结束时间")    success_count=fields.IntField(default=0,description="成功数量")    error_count=fields.IntField(default=0,description="错误数量")    worker_name=fields.CharField(max_length=50,null=True,description="工作进程名称")    classMeta:        table="alpha_backtest_queue"    def__str__(self):        returnf"{self.queue_name} (优先级: {self.priority})"
```

2. 创建回测队列 
这个脚本允许我们随时从主数据库中抽样，创建一个带优先级的回测任务队列。队列信息被写入数据库，状态为“未开始”，等待调度器认领。

```
# src/core/alpha_queue.pyasync def create_alpha_queue(template_name: str, sample_size: int, priority: int = 5):    # 查询数据库根据条件选择未取样的    query = AlphaExpression.filter(is_sampled=False, expression_order=order, template_name=template_name)    ...    # 核心：在数据库中创建一条队列记录，状态为0 (未开始)    await AlphaBacktestQueue.create(        alpha_expression_ids=sampled_ids,        priority=priority,        status=0,    )    # 标记表达式为已取样    await AlphaExpression.filter(id__in=sampled_ids).update(is_sampled=True)
```

3. 自动化任务调度
Celery Beat 定期运行此任务，它会自动从数据库中寻找 status=0 的队列，并将其分配给空闲的 Worker。

```
# src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    # ...    # 获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        # 分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  # 标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...])
```

### 

### 背景小科普：Celery 是个啥？

可能有人对 Celery 不太熟，简单说两句。Celery 是 python 的一个异步任务调度库，你可以把它想象成一个任劳任怨的“项目外包公司”。

- 发任务：在你的主程序里，只需要把一个“任务”（比如一个函数调用 run_backtest(alpha_id=123)）打包好，然后喊一嗓子：“喂，Celery，这活儿给你了！” 然后你的主程序就解放了，可以去干别的事了。

- 任务清单 (Broker)：Celery 接到活儿之后，不会立马就干，而是先把任务扔到一个叫“消息代理（Broker）”的地方（我们这里用的是 Redis）。这个 Broker 就像个任务清单。

- 工人 (Worker)：另一边，我们有一堆提前启动好的“工人（Worker）”进程，它们一直盯着这个任务清单。谁闲下来了，就去清单里领个任务开干。

- 包工头 (Beat)：我们架构图里提到的那个“包工头”，就是 Celery Beat。它是个定时器，会到点就自动往任务清单里扔一个“检查任务”，让 Worker 去执行。

这样一套下来，重量级的计算任务就被外包出去了，实现了异步化和分布式，我们才能搞定后面的事情。

### 总结一下

这么搞下来，最大的好处就是：

- 彻底解耦：想加任务、删任务、改优先级，随时都能搞，再也不用停掉跑了一半的 Worker 了。

- 全自动化：机器 7x24 小时自己跑，我们躺着看结果就行。

- 资源占用低：2 核 4G 的云服务器可以轻松起 8 个 Worker 线程。

折腾了一段时间，效果还不错。欢迎交流。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的分享，一个完整的一体化框架。

请教楼主，应该不会遇到429的问题？我感觉这套代码的优势就是可以统一会话管理，期待您的回复。

我的实现没有使用celery，只是把生产者和消费者分为两个文件，中间通过json沟通，也实现了结偶，但总是遇到429，很苦恼。

-------------------------------------------------

每天进步一点点，加油！

------------------------------------------------


---

### 技术对话片段 138 (原帖: src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    ...    获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...]))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 构建 724 小时不间断 Alpha 回测系统基于 Celery 和动态任务队列的架构分享代码优化_33040125516311.md
- **时间**: 1年前

**提问/主帖背景 (BL72197)**:
### 背景

大家好，我是量化新人小白，5 月底成为了有条件顾问，从老师的 alpha_machine 代码起步跑 123 阶任务，开启了 WQ 之旅。在量化研究中，我们常常遇到一个痛点：Alpha 表达式的生成过程与回测执行过程紧密耦合。这导致我们无法灵活地管理回测任务，比如有了新的想法想想跑个回测，要么得排队等，要么就得手动启停任务，一不小心就把跑了一半的进程给干掉了，而那些表达式回测了那些没有回测不知道，还要时不时要看看回测执行到哪里了，任务半夜执行完了或者完成了都不知道=。=，没法及时添加新的回测任务等情况大家应该深有体会。

### 系统架构设计

为了解决这个问题，我对现有的代码进行了魔改，引入了数据库（建议使用 ORM，不用手撕 SQL，如异步库 tortoise-orm）管理表达式、创建任务队列和利用 celery 实现回测任务调度，直接上架构图：
 
> [!NOTE] [图片 OCR 识别内容]
> Alpha 数据库
> Alpha 回测队列
> Celery 任务调度
> 定时任务
> 用户IAPI
> 用户IAPI
> 按队列优先级
> 查找未开始的队列
> templatelidea 生成表
> 任务调度给空闲的
> 达式
> handle_alpha_queue
> Worker
> 存储数据库
> Workerl
> Worker2
> 加入队列的进
> 行标记
> WorkerN
> 新增回测队列
> 查询回测队列
> DB
> 删除队列的取
> worker 执行回测
> 消标记
> 没有队列时发
> 删除回测队列
> 送消息提醒
> 开始
> 完成后
> 消息机器人
> 发送逍息提醒
 

系统逻辑很简单，就三块，各干各的，互不影响：

1. 随时基于模版或者新的 idea 创建表达式和 settings 存入表 alpha_expressions 中，标记表达式状态是否已被取样、是哪个模版、是几阶表达式、源表达式（之后用于剪枝）。
2. 管理待回测的任务队列，从数据库中选择自己想要跑的表达式加入到回测队列中，设置数量、优先级、出自哪个模版等，可以随时添加或删除不想执行回测的队列。
3. 利用 celery 定时任务，定时检查是否有空闲的 worker（对应一个回测槽位），如果有就将未开始的任务队列分配给它进行回测。另外还有定时任务将回测结果拉回本地存进服务器和其他自相关检查、分析等任务

这样实现之后，我不用去关注回测的执行情况，没有回测队列和任务完成会有机器人实现提醒，接下来重点就是挖掘新的 alpha idea 就可以了。
 
> [!NOTE] [图片 OCR 识别内容]
> (env)
> [rooteiv-ydwszexqtck3Gdlaadfy my_alpha_machine] # python3 handlealpha_queue .Py
> list
> -5
> 1
> 2025-06-25
> 16:16:
> 809
> Src . database. config
> INFO
> 芷在连接到数据库
> localhost: 5432/alpha_machine-
> 2025-06-25
> 16:16:22,822
> src. database. conf g
> INFO
> 数据库连接成功
> 2025-06-25
> 16:16:22,822
> Src . database. conf g
> INFO
> 正在生成数据库表结构
> 2025-06-25
> 16:16:22,845
> src . database . confg
> INFO
> 数据库表结构生成完成
> 2025-06-25
> 16:16:22,880
> Src. core.alpha_queue
> INFO
> 共找到3个回测队列:
> 2025-06-25
> 16:16:22,880
> SrC.Core.
> alpha_queue
> INFO
> ID:
> 28,名称 : template_2_500_3阶 _优先级7,状态
> 莲篌
> 优先级 :
> 7,数量
> 500
> 2025-06-25
> 16:16:22,880
> Src. core.alpha_queue
> INFO
> ID:
> 27,
> 名称 : template_2-500_3阶-优先级7, 状态
> 优先级 :
> 7,数量
> 500
> 2025-06-25
> 16:16:22,880
> Src.core.alpha_queue
> INFO
> ID:
> 26
> 名称: template_2_500_3阶 _优先级7,状态:  迸行中
> 优先级: 7。数量:
> 500
> 2025-06-25
> 16:16:22,880
> Src.database.
> conflg
> INFO
> 正在关闭数据库连接
> 2025-06-25
> 16:16:22,882
> tortoise
> INFO
> Tortoise-ORM
> Shutdown
> 2025-06-25
> 16:16:22,882
> Src . database.
> config
> INFO
> 数据库连接已关闭
> (env)
> [rooteiv-ydwszexgtck3Gdlaadfy my_alpha_machine] # python3 handle alpha_queue . Py
> list
> 5
> 2025-06-25
> 16:16:26,677
> Src . database.
> conf B
> INFO
> 芷在连接到数据库
> localhost: 5432/alpha_machine
> 2025-06-25
> 16:16:26,690
> Src . database. conf g
> INFO
> 数据库连接成功
> 2025-06-25
> 16:16:26,690
> src . database. confg
> INFO
> 正在生成数据库表结构
> 2025-06-25
> 16:16:26,713
> src . database. conf 语
> INFO
> 数据库表结构生成完成
> 2025-06-25
> 16:16:26,749
> SrC.Core.
> alpha_queue
> INFO
> 共找到12个回测队列
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 37,名称:
> template_2_500_3阶
> 优
> 500
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 36,
> 称
> template_2_500_3阶
> ~优先级
> 500
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 35,
> 称
> template_2_500_3阶 -优先级
> 蟹
> 先
> 趸
> 500
> 2025-06-25
> 16:16:26,749
> SrC.Core.
> alpha_queue
> INFO
> ID:
> 34,
> 称
> template_2_500_3阶 -优先级
> 500
> 2025-06-25
> 16:16:26,749
> STC.Core.
> alpha_queue
> INFO
> ID:
> 称
> template_2_500_3阶
> 先
> #
> 7
> 500
> 2025-06-3
> 1:16:7,749
> src. core。
> alha_queue
> HFO
> k:
> 翌;
> 1
> 黎
> template Z_500_3阶
> :
> 筅
> 蠡
> 7
> (`
> 5
> 2025-06-25
> 16:16:26,749
> SrC.core.
> alpha_queue
> INFO
> ID:
> 30,
> template_2_500_3阶
> 50
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 29,
> 称
> template_2_500_3阶
> ~优先级
> 7;
> 500
> 2025-06-25
> 16:16:26,749
> SrC.Core
> alpha_queue
> INFO
> ID:
> 22,
> 称
> template_2_500_3阶 -优先级6,
> 优先
> 6,
> 500
> 2025-06-25
> 16:16:26,749
> Src. core.alpha_queue
> INFO
> ID:
> 21,
> 名称
> template_2_500_3阶 -优先级6,
> 优先
> 6,
> 500
> 2025-06-25
> 16:16:26,749
> SrC.Core
> alpha_queue
> INFO
> ID:
> 20
> 名称: template_2_500_3阶 _优先级6,状态
> 未开始
> 优先级: 6,
> 500
> 2025-06-25
> 16:16:26,749
> Src . database . config
> INFO
> 正在关闭数据库连接 .
> 2025-06-25
> 16:16:26,751
> tortoise
> INFO
> Tortoise-ORM
> Shutdown
> 2025-06-25
> 16:
> 16:26,751
> Src .database . config
> INFO
> 数据库连接已关闭
> on
> 「rnntai-VAIC7oynt k36412adfr
> I
> 37nh2
> m2Chino7 #
> 22,
> 33,
 
 
> [!NOTE] [图片 OCR 识别内容]
> 4:40
> bj 的机器人
> BOT
> 回测队列已完成: template_2_500_13阶_优先级9
> 队列I0: 40
> 工作进程: worker2
> 成功数: 486
> 失败数: 14
> 耗时: 659分钟
> bj的机器人
> BOT
> 开始回测队列: template_2_500_3阶_优先级7
> 队列I0:28
> 工作进程: Worker2
> 优先级:7
> 表达式数量: 500
 

### 关键代码实现

1. 任务队列模型（Tortoise-ORM），好处是不需要手撕 SQL，查询的每一行结果是一个对象，可以直接用属性来访问每个字段。

```
# src/models/alpha_models.pyclass AlphaBacktestQueue(Model):"""Alpha回测队列模型"""    id=fields.IntField(pk=True)    alpha_expression_ids=fields.JSONField(description="Alpha表达式ID列表")    queue_name=fields.CharField(max_length=50,description="队列名称")    queue_count=fields.IntField(default=0,description="队列数量")    priority=fields.IntField(default=5,description="优先级")    created_at=fields.DatetimeField(auto_now_add=True,description="创建时间")    status=fields.IntField(default=0,description="状态")# 0: 未开始 1: 进行中 2: 已完成 -1: 失败    start_time=fields.DatetimeField(null=True,description="开始时间")    end_time=fields.DatetimeField(null=True,description="结束时间")    success_count=fields.IntField(default=0,description="成功数量")    error_count=fields.IntField(default=0,description="错误数量")    worker_name=fields.CharField(max_length=50,null=True,description="工作进程名称")    classMeta:        table="alpha_backtest_queue"    def__str__(self):        returnf"{self.queue_name} (优先级: {self.priority})"
```

2. 创建回测队列 
这个脚本允许我们随时从主数据库中抽样，创建一个带优先级的回测任务队列。队列信息被写入数据库，状态为“未开始”，等待调度器认领。

```
# src/core/alpha_queue.pyasync def create_alpha_queue(template_name: str, sample_size: int, priority: int = 5):    # 查询数据库根据条件选择未取样的    query = AlphaExpression.filter(is_sampled=False, expression_order=order, template_name=template_name)    ...    # 核心：在数据库中创建一条队列记录，状态为0 (未开始)    await AlphaBacktestQueue.create(        alpha_expression_ids=sampled_ids,        priority=priority,        status=0,    )    # 标记表达式为已取样    await AlphaExpression.filter(id__in=sampled_ids).update(is_sampled=True)
```

3. 自动化任务调度
Celery Beat 定期运行此任务，它会自动从数据库中寻找 status=0 的队列，并将其分配给空闲的 Worker。

```
# src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    # ...    # 获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        # 分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  # 标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...])
```

### 

### 背景小科普：Celery 是个啥？

可能有人对 Celery 不太熟，简单说两句。Celery 是 python 的一个异步任务调度库，你可以把它想象成一个任劳任怨的“项目外包公司”。

- 发任务：在你的主程序里，只需要把一个“任务”（比如一个函数调用 run_backtest(alpha_id=123)）打包好，然后喊一嗓子：“喂，Celery，这活儿给你了！” 然后你的主程序就解放了，可以去干别的事了。

- 任务清单 (Broker)：Celery 接到活儿之后，不会立马就干，而是先把任务扔到一个叫“消息代理（Broker）”的地方（我们这里用的是 Redis）。这个 Broker 就像个任务清单。

- 工人 (Worker)：另一边，我们有一堆提前启动好的“工人（Worker）”进程，它们一直盯着这个任务清单。谁闲下来了，就去清单里领个任务开干。

- 包工头 (Beat)：我们架构图里提到的那个“包工头”，就是 Celery Beat。它是个定时器，会到点就自动往任务清单里扔一个“检查任务”，让 Worker 去执行。

这样一套下来，重量级的计算任务就被外包出去了，实现了异步化和分布式，我们才能搞定后面的事情。

### 总结一下

这么搞下来，最大的好处就是：

- 彻底解耦：想加任务、删任务、改优先级，随时都能搞，再也不用停掉跑了一半的 Worker 了。

- 全自动化：机器 7x24 小时自己跑，我们躺着看结果就行。

- 资源占用低：2 核 4G 的云服务器可以轻松起 8 个 Worker 线程。

折腾了一段时间，效果还不错。欢迎交流。

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢大佬的分享，一个完整的一体化框架。

请教楼主，应该不会遇到429的问题？我感觉这套代码的优势就是可以统一会话管理，期待您的回复。

我的实现没有使用celery，只是把生产者和消费者分为两个文件，中间通过json沟通，也实现了结偶，但总是遇到429，很苦恼。

-------------------------------------------------

每天进步一点点，加油！

------------------------------------------------


---

### 技术对话片段 139 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXMKdjSB06D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcdodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzIxOTY3NDY3NTIwMjMtJUU3JUJCJThGJUU5JUFBJThDJUU1JTg4JTg2JUU0JUJBJUFCLVBQQUMlRTUlODUlQTglRTclOTAlODMlRTclQUMlQUMlRTQlQjglODklRTUlOTAlOEQtJUU1JTlCJTlFJUU5JUE2JTg4JUU3JUE0JUJFJUU1JThDJUJBBjsIVDoOc2VhcmNoX2lkSSIpYmExOWE2ZjMtY2YzYi00NzQ2LTgzNWItNmRmMDU0MzllMWRkBjsIRjoJcmFua2kMOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMTFc2NzY0MAY7CFQ6EnJlc3VsdHNfY291bnRpFQ%3D%3D--9ff0fce2aac1ca092e6ac75a4873d104dbe64709
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
引言：参赛背景与成绩概述在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。第一阶段：Alpha 构建（前五周）比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。我主要从以下三类渠道构建 Alpha：1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。构建期间，我也特别注意以下三方面的多样性控制：- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性此外，在筛选 Alpha 入库时，我建立了以下五步流程：① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；③ 计算并筛除自相关过高的表达式，提高组合独立性；④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。第二阶段：Alpha 筛选（第六周）第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级GPT 在筛选阶段的最大作用体现在两个方面：1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。此外，GPT 还协助完成以下操作：- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；- 避免过多同类中性化、universe 和数据来源重复的表达式；- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。结语：经验与建议1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
恭喜，感谢精彩的分享。做事最怕认真二字，您的工作做得太细致了，相比之下我的34名感觉太水了。收获良多，期待您的更多分享。另外请教一下：有一些alpha是减分，依然选择了提交，是因为因子的独特性，还是其他的原因呢？


---

### 技术对话片段 140 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
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

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
恭喜，感谢精彩的分享。做事最怕认真二字，您的工作做得太细致了，相比之下我的34名感觉太水了。收获良多，期待您的更多分享。另外请教一下：有一些alpha是减分，依然选择了提交，是因为因子的独特性，还是其他的原因呢？


---

### 技术对话片段 141 (原帖: 显式关闭连接但不检查响应)
- **原帖链接**: [Commented] 自己更改和完善后的wqb库代码优化.md
- **时间**: 1年前

**提问/主帖背景 (YS95353)**:
开始成为顾问后，就使用wqb库的代码，功能很全，代码也更系统化。后来自己一点点做了优化，主要在以下方面：

1.concurrent_simulate每次的控制台输出更友好、更简洁

2.logger的输出也更简洁

3.增加多重重试机制，尽最大可能减少超时导致失败的情况，并及时发邮箱通知

4.融合进了之前有大佬完成的本地自相关性检测，凡是需要访问wqb服务器的方法都放进wqb库里

5.有些方法从同步改成异步

希望能帮到大家，也欢迎讨论交流和指点。如有问题，也希望批评指正。

我是把pip install wqb得到的wqb文件夹直接复制粘贴到项目文件夹里，然后直接import这个修改后的wqb库。原先下载的wqb库就弃用了。下面是wqb_session.py的完整代码，我主要就是改了这个文件，其他文件基本没动。

import json
import os
import asyncio
import datetime
import itertools
import logging
from collections.abc import Awaitable, Callable, Coroutine, Generator, Iterable, Sized
import time
from typing import Any, Dict, List, Type, Optional, Tuple
import concurrent
from requests import RequestException, Response
import requests
from requests.auth import HTTPBasicAuth

from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from theme.utils.email_sender import send_email

from . import (
    GET,
    POST,
    LOCATION,
    RETRY_AFTER,
    EQUITY,
    Null,
    Alpha,
    MultiAlpha,
    Region,
    Delay,
    Universe,
    InstrumentType,
    DataCategory,
    FieldType,
    DatasetsOrder,
    FieldsOrder,
    Status,
    AlphaType,
    AlphaCategory,
    Language,
    Color,
    Neutralization,
    UnitHandling,
    NanHandling,
    Pasteurization,
    AlphasOrder,
)
from .auto_auth_session import AutoAuthSession
from .filter_range import FilterRange
from .wqb_urls import (
    URL_ALPHAS,
    URL_ALPHAS_ALPHAID,
    URL_ALPHAS_ALPHAID_CHECK,
    URL_ALPHAS_ALPHAID_SUBMIT,
    URL_AUTHENTICATION,
    URL_DATAFIELDS,
    URL_DATAFIELDS_FIELDID,
    URL_DATASETS,
    URL_DATASETS_DATASETID,
    URL_OPERATORS,
    URL_SIMULATIONS,
    URL_USERS_SELF_ALPHAS,
    WQB_API_URL,
)

__all__ = ['print', 'wqb_logger', 'to_multi_alphas', 'concurrent_await', 'WQBSession']

_print = print

def print(
    *args,
    **kwargs,
) -> None:
    """
    Prints, and then flushes instantly.

The usage is the same as the built-in `print`.

Parameters

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢楼主的分享，对我这样的代码小白来说非常有帮助。

您在使用的过程中，会遇到这样的错误吗？

```
status_code: 429    reason: Too Many Requests    url: [链接已屏蔽]    elapsed: 0:00:00.243682    headers: {'Date': 'Sun, 15 Jun 2025 06:45:33 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '41', 'Connection': 'keep-alive', 'X-RateLimit-Remaining-Minute': '0', 'X-RateLimit-Limit-Minute': '5', 'RateLimit-Remaining': '0', 'RateLimit-Reset': '27', 'Retry-After': '27', 'RateLimit-Limit': '5', 'vary': 'Origin', 'Access-Control-Allow-Origin': '[链接已屏蔽] 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Expose-Headers': 'Location,Retry-After', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'}    text: {  "message":"API rate limit exceeded"
```


---

### 技术对话片段 142 (原帖: 显式关闭连接但不检查响应)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 自己更改和完善后的wqb库代码优化_32415074214167.md
- **时间**: 1 year ago

**提问/主帖背景 (YS95353)**:
开始成为顾问后，就使用wqb库的代码，功能很全，代码也更系统化。后来自己一点点做了优化，主要在以下方面：

1.concurrent_simulate每次的控制台输出更友好、更简洁

2.logger的输出也更简洁

3.增加多重重试机制，尽最大可能减少超时导致失败的情况，并及时发邮箱通知

4.融合进了之前有大佬完成的本地自相关性检测，凡是需要访问wqb服务器的方法都放进wqb库里

5.有些方法从同步改成异步

希望能帮到大家，也欢迎讨论交流和指点。如有问题，也希望批评指正。

我是把pip install wqb得到的wqb文件夹直接复制粘贴到项目文件夹里，然后直接import这个修改后的wqb库。原先下载的wqb库就弃用了。下面是wqb_session.py的完整代码，我主要就是改了这个文件，其他文件基本没动。

import json
import os
import asyncio
import datetime
import itertools
import logging
from collections.abc import Awaitable, Callable, Coroutine, Generator, Iterable, Sized
import time
from typing import Any, Dict, List, Type, Optional, Tuple
import concurrent
from requests import RequestException, Response
import requests
from requests.auth import HTTPBasicAuth

from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from theme.utils.email_sender import send_email

from . import (
    GET,
    POST,
    LOCATION,
    RETRY_AFTER,
    EQUITY,
    Null,
    Alpha,
    MultiAlpha,
    Region,
    Delay,
    Universe,
    InstrumentType,
    DataCategory,
    FieldType,
    DatasetsOrder,
    FieldsOrder,
    Status,
    AlphaType,
    AlphaCategory,
    Language,
    Color,
    Neutralization,
    UnitHandling,
    NanHandling,
    Pasteurization,
    AlphasOrder,
)
from .auto_auth_session import AutoAuthSession
from .filter_range import FilterRange
from .wqb_urls import (
    URL_ALPHAS,
    URL_ALPHAS_ALPHAID,
    URL_ALPHAS_ALPHAID_CHECK,
    URL_ALPHAS_ALPHAID_SUBMIT,
    URL_AUTHENTICATION,
    URL_DATAFIELDS,
    URL_DATAFIELDS_FIELDID,
    URL_DATASETS,
    URL_DATASETS_DATASETID,
    URL_OPERATORS,
    URL_SIMULATIONS,
    URL_USERS_SELF_ALPHAS,
    WQB_API_URL,
)

__all__ = ['print', 'wqb_logger', 'to_multi_alphas', 'concurrent_await', 'WQBSession']

_print = print

def print(
    *args,
    **kwargs,
) -> None:
    """
    Prints, and then flushes instantly.

The usage is the same as the built-in `print`.

Parameters

**顾问 LW67640 (小虎) (Rank 24) 的解答与建议**:
感谢楼主的分享，对我这样的代码小白来说非常有帮助。

您在使用的过程中，会遇到这样的错误吗？

```
status_code: 429    reason: Too Many Requests    url: [链接已屏蔽]    elapsed: 0:00:00.243682    headers: {'Date': 'Sun, 15 Jun 2025 06:45:33 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '41', 'Connection': 'keep-alive', 'X-RateLimit-Remaining-Minute': '0', 'X-RateLimit-Limit-Minute': '5', 'RateLimit-Remaining': '0', 'RateLimit-Reset': '27', 'Retry-After': '27', 'RateLimit-Limit': '5', 'vary': 'Origin', 'Access-Control-Allow-Origin': '[链接已屏蔽] 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Expose-Headers': 'Location,Retry-After', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'}    text: {  "message":"API rate limit exceeded"
```


---
