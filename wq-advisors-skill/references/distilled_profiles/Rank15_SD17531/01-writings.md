# 顾问 SD17531 (Rank 15) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 SD17531 (Rank 15) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: PnL = ∑(Robustness * Creativity)
- **主帖链接**: 16815刀季度奖经验分享-小虎经验分享.md
- **讨论数**: 43

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

---

### 帖子 #2: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com16815刀季度奖经验分享-小虎经验分享_38980270292631.md
- **讨论数**: 43

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

---

### 帖子 #3: Alpha打分方式-抛砖引玉
- **主帖链接**: Alpha打分方式-抛砖引玉.md
- **讨论数**: 1

请问各位友友, 对于一个Alpha, 你是怎么考量他的质量呢?一个常见的场景: robust test滞后可能会有几十上百个非常类似的因子可以提交,但是提交一个以后其他因子会因为相关性过不去.那么,大家是如何考量应该提交哪个因子呢?先说一下个人打分的见解,目前尚未运用到代码中.1.sharpe score = (sharpe - 1) *102.fitness score = (fitness- 1)*103.margin score  = (margin - threshold) *2, us,eur,asi,glb的threshold分别是7,10,15,15.4. return score = (return - drawdown) *35.risk neut +10, 多国家地区 neut market/country +76.maxTrade ON + 10感觉上最好是获取year status去进行挨个计算再相加会更好一点, 然后前8年的分值权重是1,2021,2022权重是3.2023目前暂不做计算.目前初步想法就是这样,不知道友友们有没有更科学的方式?

---

### 帖子 #4: Alpha打分方式-抛砖引玉
- **主帖链接**: https://support.worldquantbrain.comAlpha打分方式-抛砖引玉_32997047057815.md
- **讨论数**: 1

请问各位友友, 对于一个Alpha, 你是怎么考量他的质量呢?
一个常见的场景: robust test滞后可能会有几十上百个非常类似的因子可以提交,但是提交一个以后其他因子会因为相关性过不去.那么,大家是如何考量应该提交哪个因子呢?
先说一下个人打分的见解,目前尚未运用到代码中.
1.sharpe score = (sharpe - 1) *10
2.fitness score = (fitness- 1)*10
3.margin score  = (margin - threshold) *2, us,eur,asi,glb的threshold分别是7,10,15,15.
4. return score = (return - drawdown) *3
5.risk neut +10, 多国家地区 neut market/country +7
6.maxTrade ON + 10
感觉上最好是获取year status去进行挨个计算再相加会更好一点, 然后前8年的分值权重是1,2021,2022权重是3.2023目前暂不做计算.

目前初步想法就是这样,不知道友友们有没有更科学的方式?

---

### 帖子 #5: self corr计算的代码优化
- **主帖链接**: self corr计算的代码优化.md
- **讨论数**: 2

感恩大佬发布了准确计算self corr的代码经过长时间的使用, 对于自己经常需要用的功能,我也补充了一些进入到代码里面, 分享给各位朋友参考.1.优化打印逻辑, 原先的代码里面会打印出多个corr来,实际上我更关心的是最大的corr数值,所以修改了.2.除了最大的corr,实际上我还关心最小的corr,因为在实际情况中,有时候我们需要一下reverse,把原先的负数sharpe变为正数,所以我会看一下sharpe为负数时,最小的corr数值是多少.参考实现如下:def calc_self_corr(alpha_id: str,os_alpha_rets: pd.DataFrame | None = None,os_alpha_ids: dict[str, str] | None = None,alpha_result: dict | None = None,return_alpha_pnls: bool = False,alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:"""计算指定 alpha 与其他 alpha 的最大自相关性。Args:alpha_id (str): 目标 alpha 的唯一标识符。os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。Returns:float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。"""if alpha_result is None:alpha_result = wait_get(f"[链接已屏蔽]).json()if alpha_pnls is not None:if len(alpha_pnls) == 0:alpha_pnls = Noneif alpha_pnls is None:_, alpha_pnls = get_alpha_pnls([alpha_result])alpha_pnls = alpha_pnls[alpha_id]alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]# os_alpha_rets = os_alpha_rets.replace(0, np.nan)# alpha_rets = alpha_rets.replace(0, np.nan)# 找到相关性序列correlation_series = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4)# 获取最大的相关性数值max_correlation = correlation_series.iloc[0]min_correlation = correlation_series.iloc[-1]# 打印最大的相关性数值print('max_correlation: '+ str(max_correlation))print('min_correlation: '+ str(min_correlation))os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()if np.isnan(self_corr):self_corr = 0if return_alpha_pnls:return self_corr, alpha_pnlselse:return self_corr3.因为每次交完alpha以后,原先计算过self corr的需要进行更新,每次才能跟服务器下载PNL会花很多时间,所以我把PNL数据直接存储本地了.实现代码如下:def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:"""获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，并将其转换为 pandas DataFrame 格式，方便后续数据处理。Args:alpha_id (str): Alpha 的唯一标识符。Returns:pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。"""pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])df = df.rename(columns={'date':'Date', 'pnl':alpha_id})df = df[['Date', alpha_id]]return dfdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:"""带数据库缓存的PNL获取函数"""# 先尝试从数据库获取db_data = get_pnl_from_db(alpha_id)if db_data:pnl_dict = json.loads(db_data["pnl_data"])df = pd.DataFrame(pnl_dict['records'],columns=[item['name'] for item in pnl_dict['schema']['properties']])else:# 从API获取pnl = wait_get(f"[链接已屏蔽]).json()# 存储到数据库region = wait_get(f"[链接已屏蔽]).json()['settings']['region']if not save_pnl_to_db(alpha_id, region, pnl):logging.warning(f"Failed to save PNL data for {alpha_id} to DB")df = pd.DataFrame(pnl['records'],columns=[item['name'] for item in pnl['schema']['properties']])df = df.rename(columns={'date':'Date', 'pnl':alpha_id})return df[['Date', alpha_id]]def _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:"""带数据库缓存的PNL获取函数"""# 先尝试从数据库获取if check_alpha_exists(alpha_id):conn = get_db_conn()try:with conn.cursor() as cursor:sql = "SELECT pnl_data FROM alpha_pnl WHERE alpha_id = %s"cursor.execute(sql, (alpha_id,))result = cursor.fetchone()pnl = json.loads(result['pnl_data'])finally:conn.close()else:# 从API获取并保存到数据库pnl = wait_get(f"[链接已屏蔽]).json()region = wait_get(f"[链接已屏蔽]).json()['settings']['region']save_alpha_pnl(alpha_id, pnl, region)# 保持原有处理逻辑不变df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])df = df.rename(columns={'date':'Date', 'pnl':alpha_id})return df[['Date', alpha_id]]4.因为我的alpha数据也是直接存在了本地服务器,所以在打印alpha的时候,我希望能够直观地打印出alpha的表达式和sharpe,fitness等数据,针对自己的数据库数据格式,采用了打印的方式,部分代码如下:def print_dict_info(data):print("exp:")print(data['exp'])headers = ['sharpe','fitness','returns','margin','turnover','drawdown','longCount','shortCount','first_datafield']values = [data['sharpe'],data['fitness'],f"{data['returns'] * 100:.2f}%",f"{data['margin'] * 10000:.2f}‱",f"{data['turnover'] * 100:.2f}%",f"{data['drawdown'] * 100:.2f}%",data['longCount'],data['shortCount'],data['first_datafield']]row = " | ".join([f"{header}: {value}" for header, value in zip(headers, values)])print(row)大概的打印内容如下:Fetching alphas from offset 0 to 30新下载的alpha数量: 0, 目前总共alpha数量: 359max_correlation: 0.1373min_correlation: -0.047536e****** self_corr: 0.13729466200741886exp:#ASI_1******s1;process1 = ts_z*****************4), 22);sharpe: 5.18 | fitness: 2.61 | returns: 12.40% | margin: 5.08‱ | turnover: 48.84% | drawdown: 2.04% | longCount: 1611 | shortCount: 1616 | first_datafield: None5.这部分满足相关性要求的alphaid,如果数量很多的话,我会单独打印出来,然后使用navicat进行查看.6.有时候下载的数据量是巨大的,那么中断的情况不在少数,jupyter里面打印会有问题,导致打印界面中断.所以我在确保代码稳定运行的情况下,直接忽略了报错,使用以下代码:import warningswarnings.filterwarnings('ignore')7.其实还有很多可以优化的地方,比如可以直接根据alpha的sharpe大于还是小于0,来判断符合corr标准的alpha.当sharpe小于0 时,需要获取的是最小corr,而不是最大corr.但是太懒了,就没有怎么写这些新的逻辑实现.希望以上思路能够给大家提供一点点帮助.

---

### 帖子 #6: self corr计算的代码优化
- **主帖链接**: https://support.worldquantbrain.comself corr计算的代码优化_32893337921943.md
- **讨论数**: 2

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

---

### 帖子 #7: VF半出狱
- **主帖链接**: VF半出狱.md
- **讨论数**: 0

左等右等,终于迎来4月份的VF更新了,从此,VF不在受限于1月份提交的三个小地区alpha.从12月开始提交alpha,已经坐牢了半年多了,总算阶段性有战果了.看了一下, RA和SA都是到了3.9美元左右一个,估摸着这次VF会到0.7以上.第一次突破2美元啊,值得纪念,希望更新5月VF的时候可以继续提升.另外希望combined更新能到2.

---

### 帖子 #8: VF半出狱
- **主帖链接**: https://support.worldquantbrain.comVF半出狱_33120160926103.md
- **讨论数**: 0

左等右等,终于迎来4月份的VF更新了,从此,VF不在受限于1月份提交的三个小地区alpha.从12月开始提交alpha,已经坐牢了半年多了,总算阶段性有战果了.
看了一下, RA和SA都是到了3.9美元左右一个,估摸着这次VF会到0.7以上.第一次突破2美元啊,值得纪念,希望更新5月VF的时候可以继续提升.另外希望combined更新能到2.

---

### 帖子 #9: alpha 模拟高效篇
- **主帖链接**: https://support.worldquantbrain.com[L2] alpha 模拟高效篇_33036460396567.md
- **讨论数**: 8

大家好，

这是我成为顾问以来第一次发帖，我承认确实有懒的因素，但我个人认为既然分享那就得展现出绝活嘛。

好了，话不多说在我初识worldquant中国区的小伙伴们我就意识到我们的工作其实需要的是一整套完整的服务器运行代码体系。so ~ 我开始构建了一套高效的alpha回测运行体系。
        
> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> DOO
> 20OO
> @ @
> <eo
> ppp p
> CC
> ^370''2 ^" 0  2
> 3&^D今
>  ^"识
> 9 ^  96
> 9 ^O"
> Displayed Period
> 1212872024
> 06/23/2025
> 98956
> Yesterday
> 06/23/2025
> 5663
> Current period
> 05/01/2025
> 06/30/2025
> 55393
> Previous period
> 03/01/2025
> 04/30/2025
> 3146
> Yearto date
> 01/01/2025
> 06/23/2025
> 98956
> Total
> 12/28/2024
> 06/23/2025
> 98956
> Jan
> Feb
> Feb
> Mar
> Mar
> Nal
> Mar
> Mar
> May
> May
> May
> May
> Jun
> 23.jun


可以从回测条看出来，我确实比较咸鱼。收到邮件通知才开始启动alpha回测，现在我每天都能保证4个alpha的提交。究其原因，是我构建了一整套完整高效的回测体系大家可以参考也可以提意见我们一起进步


> [!NOTE] [图片 OCR 识别内容]
> 充当持久性任贪队列
> 入口点:  表达式敛据库
> alpha_running_expressions
> 外西迸程在此处生咸并插入 alpha 表达式。
> 初始化并启动所盲系统组迕。
> 列:。
> erDr Tegion
> UIIVEFse
> 在连读遁环中运行一组立为步 多
> 军排器
> T1n
> 0atab35e
> 荩理 DB 连接。
> TasrScheduler
> 任务的集中尤态笤理。
> 初始化的关筵组件:
> TaSkEYECUCOT
> 执行任务迓辑。
> BrainhDIClien-
> 外部仿兵引孥的接口。
> 鼬发器:  足鄢运行。
> 睑段:_趑据趣取
> 服务:
> 03t-
> PToOUCeT
> SeTCe
> 1 词用以获取一批新表达式。
> 41313135e
> TSTCT
> eXpFeSS1Ons
> T 「TN
> JDUI
> 2 至关茔1的足。这会从效m厍中刨呆获]行。
> 3.对于每个表达式。在
> BACNTEST TaskScheduler
> 触发器:  查询具有
> Taskscheduler szatus-PENIDING
> 猴务:
> hachtest
> TNNSIIP[
> SeTce
> 怍:  将任务函4
> 捉交到
> Client  submi-
> CTTMTTnn
> TasLCracVTIr
> 管理侍定于类型酌并发池 (例如。 一次最多3个回溯测过
> 雹2阶段:_回测趑行_
> 组仵:
> T3SICerITnT
> 获取信号虽井在
> RIIIIIIIG TastScheduter
> 调用 以启动外部葆拟。
> Brainpclient
> 服务范围:
> NOIICOT
> LODO
> 「unnlno
> T3S
> 1a5KxeCUtOT!
> 街引婺: 管道
> 子进裎:  长时回运行的任务监控
> 定翔轮询 以获取任务的状态。
> BrainApzCient RUINING
> 模拟完咸后。它会将任务更新到 $并存储
> TasLSchanVTer
> COIPLETED
> WorldQuant Alpha 生或工怍 翟
> 髭发器
> 否诲具有 . TaskScheduler BACNTEST status-CONPLETED
> 噩3豳段: Alpha 验证
> :务:
> check_alpha
> SeTice
> 1讨于每个完成为回:1试。向提交一个新任务。
> CHECRHLPH
> TaskEXECUCO「
> 2 存裆原始任务以防止垂新处瑾。
> BACKTEST
> 触发器:  查询具有
> Taskscheduler CHECK ALPH
> STatUs=COIPLETED
> 雳 4阶段:_ 进-步加工_
> 暇务:
> Chn02
> alpha_
> COLOI
> SerVice
> submit_alpha_service
> 作:_裉揖枪查结果执行后续作
> [引如:
> 对 Alpha 迸行分茭
> 讦分或正式提交)。
> Trigger:
> 监视己达到显终达态匈任务
> 噩5阶段:_数据持久性 _
> 暇务:
> I05eTT
> data_
> 作:  将最终的 alpha 敬据 (表达式。结果等)  与入持久表。如或。
> pass_expressions
> Tail
> EpFeSSIons
> 孚格尔颉:_屯枢神经系统。
> TaskScheduler
> (大脑
> 为直任多的坯态提箧单一幸实来e
> 使用导步队列和索引迸行非阻塞
> 亏效昀太态管理
> Snglaton
> 负贡所有任务的执行。
> ~庾用待定于类型的队列和信号豆迸行精细井发控制。
> 关M架杓组件
> TaskExecutor
> (肌肉)
> 与外部服务的接0
> RrainuDTCTTen
> 垂新中的任务状态。
> 13545CheUILer
> 昃步窘理所有教挹库交互。
> Database
> (网关
> 实观用于任务摄驭的类似队列的表
> 3LCha
> 「UIITIO
> eXDTeSSlons
> 捉供用于最终结果存储的表格
> 异步和事件驱动:  完全垂于. asyncio
> Decoupled Serices
> 答道的每个阶段都是
> 个单独的服务
> 它对状态娈化箧出反应。而不是直接诩用。
> 总体架杓原则
> 弹饪和可扩展饪
> 使用效据库作为持久队列和寺淅钩关注点分离使组件可以独立扩展或重新启动
> 以状态为中心:  踅个工作流程由由  笤理的任务扶态转换辽动。
> T35LSCheTer
> ulpha
> 31652
> 3105
     如上图所示，这是我的回测体系框架全程异步队列+任务调度运行现在基本一天下来我其实没有跑满的，也就放了8个并发目前最高6644个。在这里给大家提供的一整套体系化思维希望各位同志给出建设性建议让大家一起进步。

---

### 帖子 #10: Can I use Trade_when to decease the Turnover?
- **主帖链接**: https://support.worldquantbrain.com[L2] Can I use Trade_when to decease the Turnover_27675353441431.md
- **讨论数**: 24

In my understanding, The Turnover is too high means the trading frequency is too high. So, I want to set some limitations for my alpha and don't allow it to trade at any time.

For example, my original alpha is:

```
Hello World.
```

And then, my new alpha is:

```
triggerTradeExp = (rank(volume) > 0.5)AlphaExp= Hello World.triggerExitExp = (rank(volume) <= 0.5)trade_when(triggerTradeExp, AlphaExp, triggerExitExp)
```

I thought this would reduce the trading frequency and reduce the Turnover, but it didn't. Sometimes, it even increased the turnover. I don't know what is the problem. Does anyone know this?

---

### 帖子 #11: Getting started with Analyst DatasetsResearch
- **主帖链接**: https://support.worldquantbrain.com[L2] Getting started with Analyst DatasetsResearch_25238159368215.md
- **讨论数**: 35

**Tips for getting started with  [Analyst]([链接已屏蔽])  Datasets:**

- Analyst datasets have well-structured data fields that can be considered as analysts’ sentiment scores for various fundamental ratios. Common time series and cross-sectional operations such as ts_rank, zscore, or rank can be applied to these fields.
- Comparing analyst scores on the same fundamental ratio from two different time periods can provide useful signals. For this purpose, you can use the ts_delta operator.
- General guidance for using the group operators on model data fields includes trying the following: group_rank, group_neutralize, group_normalize, and group_zscore.
- Since some analyst datasets indirectly seeks to predict returns, you can assess their potential predictive power by taking the correlation of data fields with returns/close prices.
- Analyst datasets can be large and serve as signals that seeks to predict potential returns. Therefore, ts_delta can be useful for this dataset. For instance, changes in EPS can detect earning surprises.
  - When calculating differences, be cautious of stock-split events when dealing with this kind of dataset.
- To reduce exposure to groups, group_neutralize can be helpful.
  - Country and sector neutralizations generally work well, though we recommend trying other groups as well.

**Example Alpha Ideas:**

- Check differences between estimates of long-term versus short-term horizons, and set reversal or momentum signals based on which time horizon is higher. The same idea can apply to comparisons between estimates and actuals.
- Assign Alphas based directly on the estimates, or delta(estimates), or correlation(estimates, returns on the same horizon).
- Assign Alphas in the event of high dispersion among estimates or estimates of different time horizons.

**Recommended Datasets:**

- [Fundamental Analyst Estimates]([链接已屏蔽])
- [Analyst Estimate Daily Data]([链接已屏蔽])
- [ESG scores]([链接已屏蔽])
- [Analyst Estimate Daily Data]([链接已屏蔽])
- [Analyst estimates & financial ratios]([链接已屏蔽])
- [Broker Estimates]([链接已屏蔽])
- [Alternative Analyst Investment Insight Data]([链接已屏蔽])

---

### 帖子 #12: How to Improve After Cost Performance置顶的
- **主帖链接**: https://support.worldquantbrain.com[L2] How to Improve After Cost Performance置顶的_29647491881623.md
- **讨论数**: 149

Improving After Cost Performance plays an important role in improving Combined Alpha Performance. In this post, we will share some tips to improve on  [***After-cost Sharpe ratio***](/hc/en-us/articles/25960264611351-What-s-After-cost-Sharpe-ratio) .

1. **Manage Turnover** : Consider both average daily and maximum daily turnover. Use daily turnover plots to identify turnover peaks. Try to reduce high peaks of turnover, even if the average daily turnover is already low.
   
> [!NOTE] [图片 OCR 识别内容]
> Average Turnover is Iow, but max turnoveris high:
> Average Turnoveris the same, max turnover is lower
> Chart
> Turnoer
> Chart
> Turnover
> L0
> 38
> 36。
> Jul 1
> Jon't
> Jan 15
> Jults
> Jull6
> Jun 1
> Jul
> Jan *18
> Jultg
> Jnn1g
> Jn'20
> Jonl
> Jan'15
> Jul15
> Jan"6
> Jult6
> Jul
> Jn'13
> Jonlg
> Jol1g
> Jn 20 Jul 20
> J|
> O
> Jul
> JTo
> u
 Use tradewhen, hump, ts_target_tvr_delta_limit, ts_delta_limit operators to control turnover.
2. **Optimize Alpha Weights Distribution** : Ensure the distribution of Alpha weights by capitalization is balanced. Use visualization tools to check the size by capitalization, ensuring it is evenly distributed or skewed towards high-capitalization stocks.
   
> [!NOTE] [图片 OCR 识别内容]
> Size is skewed to low capitalization part of universe (0-20%)=
> Size is skewed to high capitalization part of universe (80-100%):
> Chart
> UETAe SZe Cy LA9It
> Iaton
> N Chart
> uVeraBe SIZe By Capital
> ALTC
> OILTC
> 0201
> GC
> L5
> AFTm
> 741
> 05T
> 0-209
> 20-409
> 40-605
> 60-805
> 801009
> 020
> 20405
> UFT;
> 60-809
> 87-1009
> LatICn

3. **Ensure High Coverage** : Focus on maintaining good coverage, especially in the liquid part of the universe. Coverage (long plus short count) should be at least half of the universe and should come from liquid stocks. Short count should not be much higher than long count.
   
> [!NOTE] [图片 OCR 识别内容]
> Long count
> short count less then half of Universe size (TOP3000), short count greater then long count:
> Vear
> TIOVer
> Ftnoss
> Returns
> Drawdown
> Count
> Short Count
> 712
> -0.80
> 5J.5:
> 0.3
> 1031
> 9.571
> 一:
> 353
> 3013
> 61,83
> 9,57
> 339
> 3.135
> 71-
> 0.02
> 5J.41:
> -0.275
> 10.731
> 02
> 7015
> 0,75
> 60,949
> 33
> 7003
> 375
> 393
> 5-3
> 7016
> 0.13
> 51.35?
> 00-
> 28035
> 19.3191
> 0.31
> 411
> 533
> -017
> 0.53
> 61,73
> 01-
> 一03
> 5.2491
> 13
> 390
> 5
> 7013
> 1 4
> 60.30
> 0.3-
> 20.755
> 1-191
> 6.31
> 397
> 5-
> 2019
> 1_
> 59.52
> 0.3-
> 70.6293
> 53
> 5
> 2020
> 62.66
> 13.2540
> 77.-59
> 33525
> 392
> SD
> Long count + short count close to Universe size (TOP3000), long count approx. equal to short count
> Year
> TUINOVeT
> Ftness
> Returs
> Drawdown
> Maryin
> Cont
> Short Count
> 201
> -9
> 74034
> 1.10
> 1-:
> 3.15
> 90
> 151
> 1+35
> 2013
> 2.5
> 73.59
> 1345
> 375
> 655
> 1557
> 1474
> 201-
> 73-5:
> 1.70
> 335:
> 525
> 1
> 1535
> 1433
> 21
> 73.55;:
> 17:
> 495
> 3::
> 51
> 122
> 2015
> 73.37:
> 057
> 1 -3:
> -15
> 3::
> 53
> S
> 7017
> 73.33
> 51:
> 477
> 1.55
> 53
> 1493
> 3013
> 7354
> 0
> 1255
> 50
> 49
> 153
> 1517
> 2013
> 72.351
> D0i
> 0.75:
> 955
> 021s
> 1525
> 1510
> 2027
> 412
> 75.97:
> 73.51:
> 一5
> 21.3::
> 1-
> 1453
> Sharp
> Marmn
> L9
> 5。
> Sharpe
> Long

4. **Evaluate Sub-Universe Performance** : Check sub-universe test results and avoid submitting. Alphas that only just pass the Sub-universe Sharpe test. You can also construct your own sub-universe tests using fields from the Universe dataset to evaluate performance across all sub-universes.
   
> [!NOTE] [图片 OCR 识别内容]
> Original alpha. USA/dI/TOP3OOO/Market:
> signal
> tsdecaylinear(-returns, 5);
> alpha
> scale(group_neutralize(signal
> subindustry));
> alpha
> Aggregate Data
> Sharpe
> TUTnOET
> FIIES =
> TETUPI=
> LRaVCC
> Marain
> 1.90
> 73.66%
> 0.90
> 16.43%
> 9.169
> 4.469000
> Apply TOPSOO sub-universe test using 'tOp5OO' data field:
> Signal
> tsdecay linear(-
> returns _
> 5);
> alpha
> Scale
> Broup_neutralize(signal_
> subindustry));
> top500>0
> alpha
> han
> ABgreBate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drswoown
> Marain
> 1.17
> 73.319
> 0.47
> 11.6796
> 11.769
> 3.180000

5. **Turn on Max Trade option for ASI Alphas** : The Max Trade option must be set to ON for all Alphas in the ASI region. This setting optimizes ASI Alphas and improves After Cost Performance at combo level.

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

### 帖子 #15: Learning Time; AMIHUD ILLIQUIDITY RATIO
- **主帖链接**: https://support.worldquantbrain.com[L2] Learning Time AMIHUD ILLIQUIDITY RATIO_29239473151639.md
- **讨论数**: 42

The  **Amihud Illiquidity Ratio**  is a financial metric developed by Yakov Amihud.

It is used to measure market illiquidity and its impact on asset prices. This ratio evaluates how much the price of a stock moves relative to the volume of trades. It is particularly useful for assessing the cost of trading in markets with low liquidity  [ **ILLIQUID_MINVOL1M**  Universe].

The Amihud Illiquidity Ratio can be expressed as:

Illiquidity Ratio= Absolute Returns/Dollar Volume

 **IMPLEMENTATION IN BRAIN**

Absolute_returns=abs(ts_delta(close,1)); #Daily absolute returns

Dollar_volume=multiply(volume,close); #Convert Raw volume to dollar volume

Daily_Illiquidity=divide(Absolute_returns,Dollar_volume);

Amihud_Ratio=ts_mean(Daily_illiquidity,20) ;#To smooth the illiquidity ratio over a period N (e.g., 20 days):

**Comment;**  This part is OPTIONAL!

To neutralize the effect of market, sector, or industry factors, use:

`group_neutralize(Amihud_ratio,industry)`

**INTUITION**

**High Illiquidity;** A high ratio indicates the the stock moves significantly with a small trading volume,reflecting poor liquidity.This can ressult in high transaction costs for traders.

**Low illiquidity;** A low ratio reflects minimal price changes relative to the dollar trading volume,implying better liquidity with low trading volumes.

### **Key Characteristics**

1. **Sensitivity to Trading Volume** : Stocks with low trading volume typically have higher Amihud illiquidity values.
2. **Risk Proxy** : It serves as a proxy for market risk, as illiquid stocks are harder to buy or sell without affecting their prices.
3. **Time-Varying** : The illiquidity ratio can change based on market conditions, such as increased volatility or macroeconomic shifts.

### **Applications**

1. **Risk Assessment** : It is used to understand the liquidity risk premium embedded in asset prices.
2. **Portfolio Management** : Helps portfolio managers identify and avoid illiquid assets that may incur high transaction costs or pose challenges during liquidation.
3. **Market Efficiency Studies** : Used in empirical research to study the relationship between liquidity and asset pricing anomalies.

### **Limitations**

1. **Assumption of Linear Relationship** : The ratio assumes a linear relationship between returns and trading volume, which may not hold in all cases.
2. **Outlier Sensitivity** : Extreme returns or volumes can distort the metric.
3. **Dependence on Observation Period** : Results can vary significantly with the length of the observation period.

### **Advantages**

- Straightforward calculation and interpretation.
- Relates directly to trading costs and market behavior.
- Useful for cross-sectional analysis of stocks.

**Note;** The Amihud Ratio can be calculated for different time frames (daily, monthly, or yearly) based on the analysis needs.

Hoping to get your feedback,Happy Learning!

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
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #18: Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 进阶知识2如何优化Alpha模板中的参数案例续_28133464556311.md
- **讨论数**: 2

各位研究顾问，大家好。承接上文👉 [Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一](../顾问 JR23144 (Rank 6)/[Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一_27789509613335.md)  我们讨论了如何使用爬山算法（梯度下降）来找到局部最优点的参数。您可能已经熟悉了整体概念。然而，即使在引入随机重启的情况下改变了最初的爬山算法，仍然有改进的空间，因为每次重启并没有利用先前的信息。今天，我们将通过探索几种可以增强算法的修改来结束这一话题的简单讨论。🚀

### 普通随机爬山算法的基本结构

1. **初始化** ：从初始参数开始。
2. **评估** ：回测表达式并获得其适应度。
3. **选择** ：通过随机选择一个不同的参数来识别邻近组合。
4. **比较** ：重新回测更新后的表达式并获得其适应度。
5. **更新** ：如果邻近表达式显示出更好的适应度，则将当前选择更新为这个新参数集。
6. **迭代** ：重复评估、选择、比较和更新步骤，直到在n次迭代后没有进一步的改进。
7. **重启** ：重复上述步骤m次。这是重启机制。

### 智能重启 🔄

要考虑的第一个修改是确保在第七步的每次重启中，算法都会探索以前未遇到的新区域。为实现这一点，您可以在步骤三和四中实现一个参数计数器，每次选择并模拟一个选项时计数器递增。在第七步重启时，不要随机从可用集合中抽取选项，而是使用计数器的逆作为选择的概率。此修改确保每次重启都会选择在先前试验中未探索过的参数。🧠

一些人可能会问：“为什么只创建一个计数器？为什么不设计一个更智能的方法，将Alpha绩效信息入未来的概率中呢？”这是个好主意！具体怎么实现呢？欢迎大家在下面讨论您的想法！💡

### 直线路径可能不是最佳路径 🌄

正如一些人指出的那样，随机爬山算法的贪婪特性使其过于关注即时改进，从而可能忽略更优的曲线路径。有些人建议使用模拟退火作为替代，因为它在探索期间会容忍挫折，这有助于达到全局最优。为了使随机爬山算法达到类似的效果，您可以在步骤四中引入一些白噪声。这增加了选择“最佳”邻居的随机性。

有时，“最佳”邻居的适应度可能在短期内不佳，但在未来步骤中有更好的解决方案潜力！您还可以设计动态噪声，在早期阶段引入更多白噪声，并在后期逐渐减少——类似于模拟退火中的温度衰减。❄️🔥

这篇文章总结了关于爬山算法及其在Alpha研究中的应用的小系列。如果您对这些主题感兴趣，请留下评论告诉我们！💬

更多类似原文，可关注全球顾问论坛👉 [[Alpha Machine] How do you improve random-hill-climbing optimization](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Machine] How do you improve random-hill-climbing optimization被推荐的Alpha Template_27789493782935.md)

Credit to:YW42946

---

### 帖子 #19: Maximizing Combined Alpha Performance: Key Strategies and Insights
- **主帖链接**: https://support.worldquantbrain.com[L2] Maximizing Combined Alpha Performance Key Strategies and Insights_28436901080471.md
- **讨论数**: 60

The Combined Alpha Performance Score is a critical metric for reaching higher tiers in the BRAIN Genius Program. It measures how effectively your submitted Alphas work together, balancing individual performance and the synergy between them. Here’s a detailed breakdown of the factors influencing this score and strategies to improve it.

### **1. What Influences Combined Alpha Performance?**


> [!NOTE] [图片 OCR 识别内容]
> The combined Sharpe (Sc) of your Alphas is determined by three key factors:
> Average Sharpe (Sa): Higher Sharpe ratios for individual Alphas lead to a stronger combined
> SCOre
> Number of Alphas (n): Increasing the number of Alphas boosts performance, especially
> When they are uncorrelated。
> Correlation (p): Lower correlation between Alphas enhances diversification, improving the
> combined Sharpe.
> The combined Sharpe can be approximated by:
> Sa
> Sc
> 1 +
> 阮p
 ​​

### **2. Effects of Key Parameters**

**
> [!NOTE] [图片 OCR 识别内容]
> Impact of Correlation (p):
> Uncorrelated Alphas (p
> 0)
> The combined Sharpe scales with the square root of the number of Alphas
> providing
> significant diversification benefits.
> Highly Correlated Alphas (p
> 1):
> The combined Sharpe equals the average Sharpe (Sa), as diversification effects disappear。
> RSa'
**


> [!NOTE] [图片 OCR 识别内容]
> Impact of Number of Alphas (n):
> Adding more Alphas significantly improves the combined Sharpe When correlation is low. However;
> the benefit diminishes as correlation increases.
> Below is a table
> showing how the combined Sharpe changes with different values of n (number of
> Alphas) and p (correlation) , assuming an average Sharpe (Sa) of 1:
> Number
> Of
> Correlation
> Correlation
> Correlation
> Correlation
> Correlation
> Correlation
> Alphas
> 0.0
> 0.1
> 0.3
> 0.5
> 0.7
> 1.0
> 1.000
> 1.000
> 1.000
> 1.000
> 1.000
> 1.000
> 5
> 2.236
> 1.890
> 1.508
> 1.291
> 1.147
> 1.000
> 10
> 3.162
> 2.294
> 1.644
> 1.348
> 1.170
> 1.000
> 20
> 4.472
> 2.626
> 1.728
> 1.380
> 1.183
> 1.000
> 50
> 7.071
> 2.911
> 1.785
> 1.400
> 1.190
> 1.000
> 100
> 10.000
> 3.029
> 1.805
> 1.407
> 1.193
> 1.000


### **3. Strategies to Boost Combined Alpha Performance**

#### **1. Focus on Low-Correlation Alphas**

**
> [!NOTE] [图片 OCR 识别内容]
> Reduce pairwise correlation (p) by diversifying strategies, datasets, and regions。
> Use operators like  group_neutralize
> and
> group_rank
> to achieve orthogonality。
**

#### **2. Submit Uncorrelated Alphas Across Pyramids**

- Spread Alphas across multiple pyramids to mitigate drawdowns in any single pyramid.

#### **3. Increase the Number of Alphas**

- Add more Alphas to your submission pool, ensuring they remain sufficiently uncorrelated.

#### **4. Prioritize High OS Sharpe Ratios**

- Validate Alphas with the  **Test Period**  and Robustness Tests to avoid overfitting.
- Keep Alpha expressions simple and explainable to enhance  **out-of-sample**  (OS) performance.

### **4. Practical Insights from the Data**

- Submitting  **10 uncorrelated Alphas**  can improve the combined Sharpe by over  **200%**  compared to submitting a single Alpha.
- As correlation increases, the combined Sharpe converges to the average Sharpe, limiting diversification benefits.

### **Final Thoughts**

Maximizing Combined Alpha Performance requires a balance of high individual Sharpe ratios, low correlation, and an appropriately sized Alpha pool. By focusing on orthogonality and robustness, you can unlock the full potential of diversification, build resilience, and climb to higher tiers in the BRAIN Genius Program.

Let’s collaborate and share ideas! How do you ensure low correlation and high OS Sharpe in your submissions? Drop your tips and strategies in the comments below!

---

### 帖子 #20: replace 操作符的理解与运用
- **主帖链接**: https://support.worldquantbrain.com[L2] replace 操作符的理解与运用_35191104743447.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #21: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location']
- **主帖链接**: https://support.worldquantbrain.com[L2] Super alpha全自动回测代码--开箱即用代码优化_32637672256663.md
- **讨论数**: 30

功能省流：随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。

特点：整合了中文论坛中的super alpha代码，点击即用

感谢顾问 JL16510 (Rank 18)大佬的多线程回测代码，感谢WP88606大佬的随机生成表达式代码。我对这两篇代码做了整合，并做了一些调整，目前用该代码生成提交了几个比赛的super alpha，指标都还可以，遂分享给大家，希望能有所帮助！

有用的话还请帮忙点个小赞！

回测程序（运行这个）superAlpha.py

```
import threadingfrom machine_lib import *import randomimport selection_expressions as seneutralization_list = ["NONE","MARKET","SECTOR","INDUSTRY","SUBINDUSTRY"]conditions = [    se.category_conditions(),    se.color_conditions(),    se.neutralization_conditions(neutralization_list),    se.datacategories_conditions(),    se.datacategory_count_conditions(),    se.dataset_count_conditions(),    se.datafield_count_conditions(),    se.long_count_conditions(),    se.short_count_conditions(),    se.operator_count_conditions(),    se.prod_correlation_conditions(),    se.self_correlation_conditions(),    se.truncation_conditions(),    se.turnover_conditions(),    se.os_start_date_conditions]weight_expressions = se.weight_expressions()# 貌似author的选项用不了def author_setting():    # 从这些条件中随机选择1-2个 拼接起来返回    author_option = ["author_returns_to_drawdown>2&&","author_returns_to_drawdown<4&&","author_fitness >= 2&&","author_sharpe >= 2&&"]    # 随机选择1到2个条件    selected_conditions = random.sample(author_option, random.randint(1, 2))    # 拼接条件字符串    result = ''.join(selected_conditions)    return resultdef find_selection_expression():    condition_length = random.randint(1, 3)    condition_list = random.sample(conditions, condition_length)    choice_conditions = []    for condition in condition_list:        if callable(condition):            condition = condition()        choice_conditions.append(random.choice(condition))    choice_weight_expression = random.choice(weight_expressions)    # author_exp = author_setting()    select_expression = "not(own)&&"+"in(classifications, 'POWER_POOL')&&" + ' * '.join([f'({exp})' for exp in (choice_conditions + [choice_weight_expression])])    with open('select_expression.txt', 'a') as f:        f.write(select_expression + '\n')    return select_expressiondef get_combo_code_list():    time_windows1 = [60,120,250,500]    selected_window1 = random.choice(time_windows1)    time_windows2 = [250, 500]    selected_window2 = random.choice(time_windows2)    ret = ['1',           f'stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, {selected_window2}); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr',           ]    return retdef multi_simulate2_sa(alpha_pools, neut, region, universe, start):    global s    s = login()    brain_api_url = '[链接已屏蔽]    limit_of_concurrent_simulations = len(alpha_pools[0])    alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]    end = len(alpha_pools_2)    print(f'length:{len(alpha_pools_2)}, start:{start}')    counter: int = start    lock = threading.Lock()    def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):        while True:            global s            lock.acquire()            nonlocal counter            if counter > end - 1:                lock.release()                break            if (counter - start) % 250 == 0:  # re-login after every 60 multi_sims                s = login()            local_counter = counter            counter += 1            lock.release()            task = pools[local_counter]            sim_data_list = generate_sim_data_sa(task, region, universe, neut)            sim_data=sim_data_list[0]            try:                simulation_response = s.post('[链接已屏蔽] json=sim_data)                print(simulation_response)                simulation_progress_url = simulation_response.headers['Location']                # simulation_progress_url = simulation_response.headers.get('location')            except:                print(" loc key error")                sleep(60)                s = login()            print(f"task {local_counter} post done")            try:                while True:                    simulation_progress = s.get(simulation_progress_url)                    if simulation_progress.headers.get("Retry-After", 0) == 0:                        break                    # print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")                    sleep(float(simulation_progress.headers["Retry-After"]))                status = simulation_progress.json().get("status", 0)                if status != "COMPLETE":                    print(f"Not complete : {simulation_progress_url}")                #alpha_id = simulation_progress.json()["alpha"]                # children = simulation_progress.json().get("children", 0)                # children_list = []                # for child in children:                #     child_progress = s.get(brain_api_url + "/simulations/" + child)                #     alpha_id = child_progress.json()["alpha"]                #                #     set_alpha_properties(s,                #             alpha_id,                #             name = "saTest",                #             color = None,)            except KeyError:                print(f"look into: {simulation_progress_url}")            except Exception as e:                print(f"An error occured:{e}")            print(f"task {local_counter} simulate done")    t = []    for i in range(limit_of_concurrent_simulations):        t.append(threading.Thread(target=sim_task))        t[i].start()    for i in range(limit_of_concurrent_simulations):        t[i].join()    print("Simulate done")def generate_sim_data_sa(alpha_list, region, uni, neut):    sim_data_list = []    for selection_exp, combo_exp in alpha_list:        print(selection_exp)        print(combo_exp)        simulation_data = {            'type': 'SUPER',            'settings': {                'instrumentType': 'EQUITY',                'region': region,                'universe': uni,                'delay': 1,                'decay': 6,                'neutralization': neut,                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'ON',                'selectionHandling': random.choice(['POSITIVE','Non-Zero']),                'selectionLimit': random.choice([100,200,500]),                'language': 'FASTEXPR',                'visualization': False,            },            'selection': selection_exp,            'combo': combo_exp}        sim_data_list.append(simulation_data)    return sim_data_listif __name__ == '__main__':    while True:        selection_exp = []        exp = find_selection_expression()        selection_exp.append(exp)        combo_exp = get_combo_code_list()        sa_list = [(i, j) for i in selection_exp for j in combo_exp]        print(len(sa_list))        print(sa_list[0])        pools = load_task_pool(sa_list, 1, 3)        # print(pools[0])        region_dict = {"usa": ("USA", ["TOP3000", "TOP1000","TOP500", "TOP200"]),                       "asi": ("ASI", ["MINVOL1M"]),                       "eur": ("EUR", ["TOP2500", "TOP1200","TOP800", "TOP400"]),                       "glb": ("GLB", ["TOP3000", 'MINVOL1M']),                       "hkg": ("HKG", ["TOP800", "TOP500"]),                       "twn": ("TWN", ["TOP500", "TOP100"]),                       "jpn": ("JPN", ["TOP1600", "TOP1200"]),                       "kor": ("KOR", ["TOP600"]),                       "chn": ("CHN", ["TOP2000U"]),                       "amr": ("AMR", ["TOP600"])                       }        norm_opt = ["INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"]        risk_opt = ["FAST", "SLOW", "SLOW_AND_FAST"]        r1 = ['STATISTICAL']        cr = ["CROWDING"]        co = ["COUNTRY"]        no = ["NONE"]        neut_opt = {"USA": norm_opt + cr + risk_opt + r1,                    "GLB": co + r1,                    "EUR": co + cr + norm_opt + risk_opt + r1,                    "ASI": co + cr + norm_opt + risk_opt + no,                    "CHN": norm_opt + cr + risk_opt + r1,                    "KOR": norm_opt,                    "TWN": norm_opt,                    "HKG": norm_opt,                    "JPN": norm_opt,                    "AMR": ["COUNTRY"] + norm_opt,                    }        regi = ['usa','asi','eur','glb']        random.shuffle(regi)        for k in regi:            for i in region_dict[k][1][:1]:                print(i)                for j in neut_opt[k.upper()]:                    print(j, region_dict[k][0])                    multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)
```

然后是随机生成selection表达式的代码，放到selection_expressions.py中

```
import datetimedef category_conditions():    values = "NONE", "PRICE_REVERSION", "PRICE_MOMENTUM", "VOLUME", "FUNDAMENTAL", "ANALYST", "PRICE_VOLUME", "RELATION", "SENTIMENT"    return [f"category == \"{value}\"" for value in values]def color_conditions():    values = "NONE", "RED", "YELLOW", "GREEN", "BLUE", "PURPLE"    return [f"category == \"{value}\"" for value in values]def dataset_conditions(dataset):    return [f"in(datasets, \"{dataset}\")"]def favorite_conditions():    return [f"favorite", "not(favorite)"]def long_count_conditions():    return [f"long_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]def short_count_conditions():    return [f"short_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]def name_conditions(name):    return [f"name == \"{name}\""]def neutralization_conditions(neutralizes):    return [f"neutralization == \"{value}\"" for value in neutralizes]def operator_count_conditions():    return [f"operator_count <= {cnt}" for cnt in [1, 2, 4, 6, 8, 10]]def tags_conditions(tag):    return [f"in(tags, \"{tag}\")"]def truncation_conditions():    return [f"truncation <= {value}" for value in [0.01, 0.05, 1]]def turnover_conditions():    return [f"turnover < {value}" for value in [0.05, 0.1, 0.2, 0.3, 0.7]]def universe_conditions(universes):    return [f"universe == \"{value}\"" for value in universes]def universe_size_conditions(size=1000):    return [f"universe_size(universe) >= {size}"]def datafields_conditions(field):    return [f"in(datafields, \"{field}\")"]def dataset_count_conditions():    return [f"dataset_count <= {value}" for value in [1, 2, 3, 10]]def self_correlation_conditions():    return [f"self_correlation <= {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]def prod_correlation_conditions():    return [f"prod_correlation < {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]def os_start_date_conditions():    today = datetime.datetime.today()    delta_days = [7, 14, 30, 60, 90, 120, 180, 360, 3600]    dates = [(today-datetime.timedelta(day)).strftime('%Y-%m-%d')             for day in delta_days]    return [f"os_start_date > \"{date}\"" for date in dates]def datacategories_conditions():    values = "analyst, broker, earnings, fundamental, imbalance, insiders, institutions, \        macro, model, news, option, other, pv, risk, sentiment, shortinterest, socialmedia".split(',')    return [f"in(datacategories, \"{value.strip()}\")" for value in values]def datacategory_count_conditions():    return [f"datacategory_count <= {value}" for value in [1, 2, 3, 10]]def datafield_count_conditions():    return [f"datafield_count <= {value}" for value in [1, 2, 3, 5, 10]]def weight_expressions():    return [        "turnover", '10-turnover',        '10000-abs(long_count-short_count)', 'long_count+short_count', 'long_count', 'short_count',        '10-dataset_count',        '2-self_correlation',        '2-prod_correlation',        '100-datafield_count',        '1'    ]
```

运行 superAlpha.py就可以开始自动回测啦~

当然该代码还有很多小问题，希望大佬们可以继续完善！

都看到这了，点个赞再走吧~~

---

### 帖子 #22: [BRAIN TIPS] 6 ways to quickly evaluate a new datasetFeatured
- **主帖链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] 6 ways to quickly evaluate a new datasetFeatured_11807866133911.md
- **讨论数**: 15

WorldQuant BRAIN has thousands of datafields for you to create alphas. But how do you quickly understand a new datafield? Here are 6 ways. Simulate the below expressions in “None” neutralization and decay 0 setting. And obtains insights of specific parameters using the Long Count and Short Count in the IS Summary section of the results.

**Sr. No**

**Expression**

**Insight**

1

datafield

%  **coverage** , would approximately be ratio of (Long Count + Short Count in the IS Summary )/ (Universe Size in the settings)

2

datafield != 0 ? 1 : 0

**Coverage** . Long Count indicates average non-zero values on a daily basis

3

ts_std_dev(datafield,N) != 0 ? 1 : 0

**Frequency**  of unique data (daily, weekly, monthly etc.).

Some datasets have data backfilled for missing values, while some do not. The given expression can be used to find the frequency of unique datafield updates by varying N (no. of days).

Datafields with a quarterly unique data frequency would see a Long Count + Short Count value close to its actual coverage when N = 66 (quarter). When N = 22 (month) Long Count + Short Count would be lower (approx. 1/3rd of coverage) and when N = 5 (week), Long Count + Short Count would be even lower.

4

abs(datafield) > X

**Bounds**  of the datafield. Vary the values of X and see the Long Count. For example, X=1 will indicate if the field is normalized to values between -1 and +1?

5

ts_median(datafield, 1000) > X

**Median**  of the datafield over 5 years. Vary the values of X and see the Long Count. Similar process can be applied to check the mean of the datafield.

6

X < scale_down(datafield) && scale_down(datafield) < Y

**Distribution**  of the datafield. scale_down acts as a MinMaxScaler that can preserve the original distribution of the data. X and Y are values that vary between 0 and 1 that allow us to check how the datafield distribute across its range.

For example, if you simulate [close <= 0], You will see Long and Short Counts as 0. This implies that closing price always has a positive value (as expected!)

---

### 帖子 #23: 【alpha灵感】A股恐慌度因子在美股的应用
- **主帖链接**: [L2] 【alpha灵感】A股恐慌度因子在美股的应用.md
- **讨论数**: 17

📈【A股恐慌度因子在美股的应用】💡

大家好！今天我要分享一个超有趣的因子——恐慌度因子
这个因子是可以直接提交的哦，并且具有非常强的经济学意义。

m_ret = group_mean(returns, rank(ts_mean(cap, 20)), market);

horro = abs(returns - m_ret) / (abs(returns)+abs(m_ret)+0.1);

horro_day = ts_mean(horro, 22);

ret_std = ts_std_dev(returns, 22);

adj_ret = horro_day * ret_std * returns;

adj_ret_mean = ts_mean(adj_ret, 22);

adj_ret_std = ts_std_dev(adj_ret, 22);

horro_std_bonus = zscore(adj_ret_mean) + zscore(adj_ret_std);

-horro_std_bonus

🔍  **因子构成解析** ：

1. **m_ret** ：计算股票收益的组内均值，基于市值排名和市场的平均收益。
2. **horro** ：衡量个股收益与组内均值的偏离程度，反映恐慌情绪。
3. **horro_day** ：对恐慌情绪进行22天的移动平均，平滑数据。
4. **ret_std** ：计算22天的收益标准差，衡量波动性。
5. **adj_ret** ：结合恐慌情绪和波动性，调整收益。
6. **adj_ret_mean**  和  **adj_ret_std** ：分别计算调整后收益的均值和标准差。
7. **horro_std_bonus** ：将调整后收益的均值和标准差进行标准化，并相加，得到最终的因子值。

💡  **为什么这个因子能赚钱？**

- **做多因子值越大** ：意味着恐慌情绪较低，收益稳定，适合做多。
- **做空因子值越小** ：意味着恐慌情绪较高，收益波动大，适合做空。

因子表现：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 5,OOOK
> Sep '17
> Jan '18
> May '18
> Sep'18
> Jan '19
> '19
> Sep '19
> May '20
> Sep '20
> Jan '21
> May '21
> Sep'21
> Jan '22
> '22
> May
> May



> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> IS
> 0S
> Excellent
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> MarEin
> 1.25
> 13.539
> 2.03
> 35.689
> 39.849
> 52.739600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
>  Short Count
> 2017
> 0.22
> 13.33%
> -0.13
> -4.399
> 12.77%
> 6.5990
> 2315
> 780
> 2018
> 0.57
> 12.65%
> 0.58
> 13.0796
> 20.03%
> 20.5496o
> 2291
> 825
> 2019
> 2.59
> 13.3996
> 5.14
> 48.8796
> 12.5596
> 73.00960
> 2297
> 808
> 2020
> 0.70
> 12.53%6
> 0.90
> 20.8390
> 28.51%6
> 33.349600
> 2255
> 844
> 2021
> 14.5896
> 2.41
> 51.5596
> 24.73%
> 70.709603
> 2375
> 773
> 2022
> 2.59
> 15.35%6
> 6.05
> 83.8796
> 16.36%
> 109.249000
> 2221
> 915



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Industry
> On
> On
> Verify


---

### 帖子 #24: 【alpha灵感】A股恐慌度因子在美股的应用
- **主帖链接**: https://support.worldquantbrain.com[L2] 【alpha灵感】A股恐慌度因子在美股的应用_29327820720151.md
- **讨论数**: 17

📈【A股恐慌度因子在美股的应用】💡

大家好！今天我要分享一个超有趣的因子——恐慌度因子
这个因子是可以直接提交的哦，并且具有非常强的经济学意义。

m_ret = group_mean(returns, rank(ts_mean(cap, 20)), market);

horro = abs(returns - m_ret) / (abs(returns)+abs(m_ret)+0.1);

horro_day = ts_mean(horro, 22);

ret_std = ts_std_dev(returns, 22);

adj_ret = horro_day * ret_std * returns;

adj_ret_mean = ts_mean(adj_ret, 22);

adj_ret_std = ts_std_dev(adj_ret, 22);

horro_std_bonus = zscore(adj_ret_mean) + zscore(adj_ret_std);

-horro_std_bonus

🔍  **因子构成解析** ：

1. **m_ret** ：计算股票收益的组内均值，基于市值排名和市场的平均收益。
2. **horro** ：衡量个股收益与组内均值的偏离程度，反映恐慌情绪。
3. **horro_day** ：对恐慌情绪进行22天的移动平均，平滑数据。
4. **ret_std** ：计算22天的收益标准差，衡量波动性。
5. **adj_ret** ：结合恐慌情绪和波动性，调整收益。
6. **adj_ret_mean**  和  **adj_ret_std** ：分别计算调整后收益的均值和标准差。
7. **horro_std_bonus** ：将调整后收益的均值和标准差进行标准化，并相加，得到最终的因子值。

💡  **为什么这个因子能赚钱？**

- **做多因子值越大** ：意味着恐慌情绪较低，收益稳定，适合做多。
- **做空因子值越小** ：意味着恐慌情绪较高，收益波动大，适合做空。

因子表现：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 1ON
> 5,OOOK
> Sep '17
> Jan '18
> May '18
> Sep'18
> Jan '19
> '19
> Sep '19
> May '20
> Sep '20
> Jan '21
> May '21
> Sep'21
> Jan '22
> '22
> May
> May



> [!NOTE] [图片 OCR 识别内容]
> Is Summary
> Period
> IS
> 0S
> Excellent
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fithess
> Returns
> Drawdown
> MarEin
> 1.25
> 13.539
> 2.03
> 35.689
> 39.849
> 52.739600
> Vear
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
>  Short Count
> 2017
> 0.22
> 13.33%
> -0.13
> -4.399
> 12.77%
> 6.5990
> 2315
> 780
> 2018
> 0.57
> 12.65%
> 0.58
> 13.0796
> 20.03%
> 20.5496o
> 2291
> 825
> 2019
> 2.59
> 13.3996
> 5.14
> 48.8796
> 12.5596
> 73.00960
> 2297
> 808
> 2020
> 0.70
> 12.53%6
> 0.90
> 20.8390
> 28.51%6
> 33.349600
> 2255
> 844
> 2021
> 14.5896
> 2.41
> 51.5596
> 24.73%
> 70.709603
> 2375
> 773
> 2022
> 2.59
> 15.35%6
> 6.05
> 83.8796
> 16.36%
> 109.249000
> 2221
> 915



> [!NOTE] [图片 OCR 识别内容]
> Simulation
> Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Delay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Equity
> USA
> T0P3000
> Fast Expression
> 0.08
> Industry
> On
> On
> Verify


---

### 帖子 #25: PnL = ∑(Robustness * Creativity)
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

### 帖子 #26: 【YZ工程优化系列】YZ72256-使用API自动完成submit
- **主帖链接**: [L2] 【YZ工程优化系列】YZ72256-使用API自动完成submit.md
- **讨论数**: 1

针对由于系统bug、某地区或某时间段扎堆submit、同时check的人数太多导致submit经常超时的情况，推荐 **使用api进行alpha的提交** 。如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

首先先定义一个submit函数对一个alpha进行submit提交，返回提交的结果result。本函数 **感谢ZZ13271老虎哥** 在研究小组群中的api接口代码提供，我只是在其基础上进行了再次加工。

```
def submit(s, alpha_id):    try:        result =s.post(f"[链接已屏蔽])    except:        print('重新登陆')        s = login()        result =s.post(f"[链接已屏蔽])    while True:        if "retry-after" in result.headers:            print(f'{alpha_id} submiting {datetime.now()}')            sleep(120)            time.sleep(float(result.headers["Retry-After"]))            try:                result = s.get(f"[链接已屏蔽])            except:                print('重新登陆')                s = login()        else:            break    return result
```

接着针对多个alpha以及alpha提交失败或超时等多个情况进行处理和异常输出。

```
def submit_alpha(alphaid_list):    s = login()    for alphaid in alphaid_list:        count = 1        while True:            print(f"开始第 {count} 次提交 {alphaid}")            res = submit(s, alphaid)            if res.text:                try:                    res = res.json()                    break                except:                    print('当前有submit任务正在进行中，sleeping 2 min')                    sleep(120)            else:                print(f"第 {count} 次提交超时")                count += 1        # 若是输入alphaid错误        if 'detail' in res and res['detail'] == 'Not found.':            print(f"{alphaid} 错误")            continue               # 检查submit情况        submitted = True        for item in res['is']['checks']:            if item['name'] == 'ALREADY_SUBMITTED':                submitted = False                print(f"{alphaid} 已经提交过了")                break            if item['result'] == 'FAIL':                submitted = False                print(f"{alphaid} 的 {item['name']} 检查不通过, limit = {item['limit']} , value = {item['value']}")                break        if submitted:            print(f'{alphaid}提交成功')
```

上述代码我使用了四种情况进行检验，第一则为错误的alpha id，第二是不用check就存在fail的alpha，第三是已经提交了的alpha，第四是corr错误的alpha，第五则是正常提交的alpha。

```
alphaid_list = ['1234567', 'M7vxRkr', 'pj2aoNq', 'O7daGpd', 'vj7Eowa']submit_alpha(alphaid_list)
```

最终运行结果如下：


> [!NOTE] [图片 OCR 识别内容]
> aIphaid_Iist
> ['1234567
> N7XRkr
> 0j2a0119
> 07daGpd
> VjTEOIa
> submit_alpha (alphaid_list l
> [33]
> 3-11-3.35
> b'{"User
> {"id"
> 1272256"}」
> tokzn'
> {"expiny
> 14438.3},
> Dermissions
> COIISULTAIIT
> 开始第
> 次提交
> 1234557
> 1234557
> 错误
> 开始第
> 次提交
> N7VXRkr
> ITVRkr
> LADDER SHARPE
> 捡查不通过,
> limit
> 1.53
> ValUe
> 3.5
> 开始第
> 次提交
> PjzaoNq
> PJzaoNq 已经提交过
> 开始第
> 次提交
> 074aG30
> 07JaGpd submizing
> 2325-
> 01-15
> 21:02:20
> 505324
> 07daGpd submiting 2025-O1-I5  21:04:22.812891
> O7daGpd submiting
> 2825-81-15
> 21:86:25.113949
> 07daGpd submiting 2025-01-15
> 21:98:27.297258
> 07daGpd submiting
> 2025-81-15  21;10:33
> 994252
> 次提交超时
> 开始第
> 次提交
> 07J2G30
> 07JaGpC
> submizing 2025-01-15  21:12:36.839294
> 07daGpd submiting
> 2325-
> 01-15
> 21:14:39
> 370928
> 07daGpd 的 PROD_CORRELATION 捡查不通过
> Iimit
> 07
> Va_UE
> 0.7293
> 开始第
> 次提交
> Vj7EOWa
> VjEOwa submiting 2025-01-15  21:16:42.030661
> VJTEOwa submiting 2025-81-15
> 21:18:44.247943
> VjEOwa submiting 2025-0I-15  21:20:46.512882
> VJTEOwa submiting
> 2825-81-15
> 21:22:48
> 579339
> VjEOwa submiting 2025-0I-I5  21:24:50.878326
> 次提交超时
> VJTEOwa submiting 2025-81-15
> 21:3:32
> 948596
> 2 次提三
> 超时
> 开始第
> 次提交
> Vj7EOWa
> VjTEOwa
> 经提交过
> OupUT is truncated; Vew Os
> Scrolloble element Oropen i
> ttedto Adjust cell output Settings:


耗时38分钟，前面三种都是秒过的，后边两种由于需要check出fail因此基本都是耗时近20分钟，经两次submit之后才完成，其中提交的那个因子并没有直接返回提交成功，而是在重新submit之后返回它已经是已提交状态了。

最后祝大家每天因子多多，base多多，value up up。我是YZ72256，如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

---

### 帖子 #27: 【YZ工程优化系列】YZ72256-使用API自动完成submit
- **主帖链接**: https://support.worldquantbrain.com[L2] 【YZ工程优化系列】YZ72256-使用API自动完成submit_29242440942359.md
- **讨论数**: 1

针对由于系统bug、某地区或某时间段扎堆submit、同时check的人数太多导致submit经常超时的情况，推荐 **使用api进行alpha的提交** 。如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

首先先定义一个submit函数对一个alpha进行submit提交，返回提交的结果result。本函数 **感谢ZZ13271老虎哥** 在研究小组群中的api接口代码提供，我只是在其基础上进行了再次加工。

```
def submit(s, alpha_id):    try:        result =s.post(f"[链接已屏蔽])    except:        print('重新登陆')        s = login()        result =s.post(f"[链接已屏蔽])    while True:        if "retry-after" in result.headers:            print(f'{alpha_id} submiting {datetime.now()}')            sleep(120)            time.sleep(float(result.headers["Retry-After"]))            try:                result = s.get(f"[链接已屏蔽])            except:                print('重新登陆')                s = login()        else:            break    return result
```

接着针对多个alpha以及alpha提交失败或超时等多个情况进行处理和异常输出。

```
def submit_alpha(alphaid_list):    s = login()    for alphaid in alphaid_list:        count = 1        while True:            print(f"开始第 {count} 次提交 {alphaid}")            res = submit(s, alphaid)            if res.text:                try:                    res = res.json()                    break                except:                    print('当前有submit任务正在进行中，sleeping 2 min')                    sleep(120)            else:                print(f"第 {count} 次提交超时")                count += 1        # 若是输入alphaid错误        if 'detail' in res and res['detail'] == 'Not found.':            print(f"{alphaid} 错误")            continue               # 检查submit情况        submitted = True        for item in res['is']['checks']:            if item['name'] == 'ALREADY_SUBMITTED':                submitted = False                print(f"{alphaid} 已经提交过了")                break            if item['result'] == 'FAIL':                submitted = False                print(f"{alphaid} 的 {item['name']} 检查不通过, limit = {item['limit']} , value = {item['value']}")                break        if submitted:            print(f'{alphaid}提交成功')
```

上述代码我使用了四种情况进行检验，第一则为错误的alpha id，第二是不用check就存在fail的alpha，第三是已经提交了的alpha，第四是corr错误的alpha，第五则是正常提交的alpha。

```
alphaid_list = ['1234567', 'M7vxRkr', 'pj2aoNq', 'O7daGpd', 'vj7Eowa']submit_alpha(alphaid_list)
```

最终运行结果如下：


> [!NOTE] [图片 OCR 识别内容]
> aIphaid_Iist
> ['1234567
> N7XRkr
> 0j2a0119
> 07daGpd
> VjTEOIa
> submit_alpha (alphaid_list l
> [33]
> 3-11-3.35
> b'{"User
> {"id"
> 1272256"}」
> tokzn'
> {"expiny
> 14438.3},
> Dermissions
> COIISULTAIIT
> 开始第
> 次提交
> 1234557
> 1234557
> 错误
> 开始第
> 次提交
> N7VXRkr
> ITVRkr
> LADDER SHARPE
> 捡查不通过,
> limit
> 1.53
> ValUe
> 3.5
> 开始第
> 次提交
> PjzaoNq
> PJzaoNq 已经提交过
> 开始第
> 次提交
> 074aG30
> 07JaGpd submizing
> 2325-
> 01-15
> 21:02:20
> 505324
> 07daGpd submiting 2025-O1-I5  21:04:22.812891
> O7daGpd submiting
> 2825-81-15
> 21:86:25.113949
> 07daGpd submiting 2025-01-15
> 21:98:27.297258
> 07daGpd submiting
> 2025-81-15  21;10:33
> 994252
> 次提交超时
> 开始第
> 次提交
> 07J2G30
> 07JaGpC
> submizing 2025-01-15  21:12:36.839294
> 07daGpd submiting
> 2325-
> 01-15
> 21:14:39
> 370928
> 07daGpd 的 PROD_CORRELATION 捡查不通过
> Iimit
> 07
> Va_UE
> 0.7293
> 开始第
> 次提交
> Vj7EOWa
> VjEOwa submiting 2025-01-15  21:16:42.030661
> VJTEOwa submiting 2025-81-15
> 21:18:44.247943
> VjEOwa submiting 2025-0I-15  21:20:46.512882
> VJTEOwa submiting
> 2825-81-15
> 21:22:48
> 579339
> VjEOwa submiting 2025-0I-I5  21:24:50.878326
> 次提交超时
> VJTEOwa submiting 2025-81-15
> 21:3:32
> 948596
> 2 次提三
> 超时
> 开始第
> 次提交
> Vj7EOWa
> VjTEOwa
> 经提交过
> OupUT is truncated; Vew Os
> Scrolloble element Oropen i
> ttedto Adjust cell output Settings:


耗时38分钟，前面三种都是秒过的，后边两种由于需要check出fail因此基本都是耗时近20分钟，经两次submit之后才完成，其中提交的那个因子并没有直接返回提交成功，而是在重新submit之后返回它已经是已提交状态了。

最后祝大家每天因子多多，base多多，value up up。我是YZ72256，如果本文对你有帮助欢迎点赞，如果其他想法也欢迎在评论区留言。

---

### 帖子 #28: 将时区偏移部分从 +0000 转换为 -0400 或 -0500 的格式
- **主帖链接**: [L2] 【代码分享】关于抓取时间的代码优化.md
- **讨论数**: 4

关于一二三阶模板的时间抓取函数的一些问题：

1.颗粒度问题，现在是最基础的以日为单位，目前只能抓取的最小颗粒度是天，如果抓取的alpha大于1w，则超出的部分无法抓取；

2.关于跨年的alpha无法抓取，因为目前的代码传入参数只有月日；

3.因为是以美国时间，关于冬令时到夏令时之间的时间转换问题；

4.check代码如果数量过多，可能会断开，又要从头来过。

我修改了一下这个代码，改成了美东时间，输入参数改成了年月日时分秒，下面是例子及代码：

例：

th_tracker = get_alphas("2025-03-18 21:00:00", "2025-03-18 22:00:00", 1.58, 1, "EUR", 1000, "submit")

代码：

def get_alphas(start_date_str, end_date_str, sharpe_th, fitness_th, region, alpha_num, usage):

s = login()

output = []

# 3E large 3C less

count = 0

# 设置美东时区

eastern = pytz.timezone('US/Eastern')

# 将输入的时间字符串解析为datetime对象，并设置为美东时间

start_date = eastern.localize(datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S"))

end_date = eastern.localize(datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S"))

# 格式化为API所需的时间字符串格式（2025-03-25T22:23:36-04:00 或 2025-03-25T22:23:36-05:00，取决于夏令时）

start_date_api = start_date.strftime("%Y-%m-%dT%H:%M:%S%z")

end_date_api = end_date.strftime("%Y-%m-%dT%H:%M:%S%z")

# 将时区偏移部分从 +0000 转换为 -0400 或 -0500 的格式

start_date_api = start_date_api[:-2] + ":" + start_date_api[-2:]

end_date_api = end_date_api[:-2] + ":" + end_date_api[-2:]

for i in range(0, alpha_num, 100):

print(i)

url_e = " [[链接已屏蔽]) " % (i) \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_api \

+ "&dateCreated%3C=" + end_date_api \

+ "&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"

url_c = " [[链接已屏蔽]) " % (i) \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_api \

+ "&dateCreated%3C=" + end_date_api \

+ "&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"

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

#if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):

if (longCount + shortCount) > 100:

if sharpe < -sharpe_th:

exp = "-%s"%exp

rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]

print(rec)

if turnover > 0.7:

rec.append(decay*4)

elif turnover > 0.6:

rec.append(decay*3+3)

elif turnover > 0.5:

rec.append(decay*3)

elif turnover > 0.4:

rec.append(decay*2)

elif turnover > 0.35:

rec.append(decay+4)

elif turnover > 0.3:

rec.append(decay+2)

output.append(rec)

except:

print("%d finished re-login"%i)

s = login()

print("count: %d"%count)

return output

---

### 帖子 #29: 将时区偏移部分从 +0000 转换为 -0400 或 -0500 的格式
- **主帖链接**: https://support.worldquantbrain.com[L2] 【代码分享】关于抓取时间的代码优化_31184912102423.md
- **讨论数**: 4

关于一二三阶模板的时间抓取函数的一些问题：

1.颗粒度问题，现在是最基础的以日为单位，目前只能抓取的最小颗粒度是天，如果抓取的alpha大于1w，则超出的部分无法抓取；

2.关于跨年的alpha无法抓取，因为目前的代码传入参数只有月日；

3.因为是以美国时间，关于冬令时到夏令时之间的时间转换问题；

4.check代码如果数量过多，可能会断开，又要从头来过。

我修改了一下这个代码，改成了美东时间，输入参数改成了年月日时分秒，下面是例子及代码：

例：

th_tracker = get_alphas("2025-03-18 21:00:00", "2025-03-18 22:00:00", 1.58, 1, "EUR", 1000, "submit")

代码：

def get_alphas(start_date_str, end_date_str, sharpe_th, fitness_th, region, alpha_num, usage):

s = login()

output = []

# 3E large 3C less

count = 0

# 设置美东时区

eastern = pytz.timezone('US/Eastern')

# 将输入的时间字符串解析为datetime对象，并设置为美东时间

start_date = eastern.localize(datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S"))

end_date = eastern.localize(datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S"))

# 格式化为API所需的时间字符串格式（2025-03-25T22:23:36-04:00 或 2025-03-25T22:23:36-05:00，取决于夏令时）

start_date_api = start_date.strftime("%Y-%m-%dT%H:%M:%S%z")

end_date_api = end_date.strftime("%Y-%m-%dT%H:%M:%S%z")

# 将时区偏移部分从 +0000 转换为 -0400 或 -0500 的格式

start_date_api = start_date_api[:-2] + ":" + start_date_api[-2:]

end_date_api = end_date_api[:-2] + ":" + end_date_api[-2:]

for i in range(0, alpha_num, 100):

print(i)

url_e = " [[链接已屏蔽]) " % (i) \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_api \

+ "&dateCreated%3C=" + end_date_api \

+ "&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"

url_c = " [[链接已屏蔽]) " % (i) \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_api \

+ "&dateCreated%3C=" + end_date_api \

+ "&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"

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

#if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):

if (longCount + shortCount) > 100:

if sharpe < -sharpe_th:

exp = "-%s"%exp

rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]

print(rec)

if turnover > 0.7:

rec.append(decay*4)

elif turnover > 0.6:

rec.append(decay*3+3)

elif turnover > 0.5:

rec.append(decay*3)

elif turnover > 0.4:

rec.append(decay*2)

elif turnover > 0.35:

rec.append(decay+4)

elif turnover > 0.3:

rec.append(decay+2)

output.append(rec)

except:

print("%d finished re-login"%i)

s = login()

print("count: %d"%count)

return output

---

### 帖子 #30: 【工具优化】华子哥插件的FireFox版本经验分享
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

### 帖子 #31: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **讨论数**: 870

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #32: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 986

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #33: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #34: 【日常生活贴】我的量化日记第十季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #35: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
- **主帖链接**: [L2] 【构建自己的代码框架系列】第03篇--除了自己的alpha信息你到底在MySQL需要存哪些数据暨API代码分享.md
- **讨论数**: 2

## 往期回顾

- [【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha]([Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha.md)
- [【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回](../顾问 PN39025 (Rank 87)/[Commented] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回.md)

## 一.所有的dataset信息

注意一定要爬取description,因为后续可以把这个字段喂给大模型

表结构:

-- worldquant.data_sets definition

CREATE TABLE `data_sets` (
  `data_set_id` varchar(100) NOT NULL,
  `delay` tinyint NOT NULL DEFAULT '1',
  `region` varchar(100) NOT NULL,
  `universe` varchar(100) NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `description` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description_cn` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `pyramid_multiplier` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `user_count` int DEFAULT NULL,
  `value_score` tinyint DEFAULT NULL,
  `alpha_count` int DEFAULT NULL,
  `field_count` int DEFAULT NULL,
  `score` tinyint DEFAULT NULL,
  PRIMARY KEY (`data_set_id`,`delay`,`region`,`universe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='所有的数据集信息,关注中文描述';

api:

```
def get_data_sets(s, region, delay, universe):    """    获取所有的data_sets信息写入MySQL    :param s: requests.session()    :param region: region    :param delay: delay    :param universe: universe    :return: data_sets_list,每个data_set是一个dict,包含data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&limit=20"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    data_sets_list = []    for x in range(0, count, 20):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            data_sets_list.append(                {                    'data_set_id': result['id'],                    'category_id': result['category']['id'],                    'description': result['description'],                    'name': result['name'],                    'pyramid_multiplier': result['pyramidMultiplier'],                    'coverage': result['coverage'],                    'user_count': result['userCount'],                    'value_score': result['valueScore'],                    'alpha_count': result['alphaCount'],                    'field_count': result['fieldCount'],                }            )        time.sleep(4)    return data_sets_list
```

```
if __name__ == "__main__":    s = login()    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        data_sets = get_data_sets(s, region, delay, universe)        with conn.cursor() as cursor:            for data_set in data_sets:                sql = (                    f"insert into worldquant.data_sets(region,delay,universe,data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                    "on duplicate key update category_id=%s,description=%s,name=%s,pyramid_multiplier=%s,coverage=%s,user_count=%s,value_score=%s,alpha_count=%s,field_count=%s"                )                sql_params = (                    region, delay, universe, data_set['data_set_id'], data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count'],                    data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count']                )                cursor.execute(sql, sql_params)        conn.commit()
```

## 二.分地区的field信息

这个所有地区可以合并在一个表格,但是我还没改,暂时按不同地区不同delay分表的
表结构:

-- worldquant.hkg_delay1 definition

CREATE TABLE `hkg_delay1` (
  `field` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `delay` char(1) DEFAULT NULL,
  `universe` varchar(100) DEFAULT NULL,
  `datasets` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `userCount` int DEFAULT NULL,
  `alphaCount` int DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

api:

```
def get_fields(s, dataset_id, region, delay, universe):    """    给定data_sets的id,以及参数region,delay,universe,返回符合条件的data_sets里面的fields    :param s: requests.session()    :param dataset_id: data_sets的id    :param region: region    :param delay: delay    :param universe: universe    :return: fields,每个field是一个dict,包含field_type和field_id    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    datafields_list = []    for x in range(0, count, 50):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            field_type = result['type']            field_id = result['id']            description = result['description']            coverage = result['coverage']            userCount = result['userCount']            alphaCount = result['alphaCount']            datafields_list.append({'field_type': field_type, 'field_id': field_id, 'description': description,'coverage': coverage, 'userCount': userCount, 'alphaCount': alphaCount})    return datafields_list
```

```
if __name__ == "__main__":    s = login()    dataset_ids = [        'other128',        'other16',    ]    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        for dataset_id in dataset_ids:            fields = get_fields(s, dataset_id, region, delay, universe)            with conn.cursor() as cursor:                for item in fields:                    sql = (                        f"insert into worldquant.{region}_DELAY1(field,description,region,delay,universe,datasets,type,coverage,userCount,alphaCount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                        "on duplicate key update description=%s,region=%s,delay=%s,universe=%s,datasets=%s,type=%s,coverage=%s,userCount=%s,alphaCount=%s"                    )                    sql_params = (                        item['field_id'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount']                    )                    cursor.execute(sql, sql_params)            conn.commit()
```

---

### 帖子 #36: 【构建自己的代码框架系列】第03篇--除了自己的alpha信息,你到底在MySQL需要存哪些数据(暨API代码分享)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【构建自己的代码框架系列】第03篇--除了自己的alpha信息你到底在MySQL需要存哪些数据暨API代码分享_29022968451223.md
- **讨论数**: 2

## 往期回顾

- [【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha]([Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md)
- [【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回]([Commented] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回_28969108137623.md)

## 一.所有的dataset信息

注意一定要爬取description,因为后续可以把这个字段喂给大模型

表结构:

-- worldquant.data_sets definition

CREATE TABLE `data_sets` (
  `data_set_id` varchar(100) NOT NULL,
  `delay` tinyint NOT NULL DEFAULT '1',
  `region` varchar(100) NOT NULL,
  `universe` varchar(100) NOT NULL,
  `category_id` varchar(100) DEFAULT NULL,
  `description` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description_cn` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(1000) DEFAULT NULL,
  `pyramid_multiplier` float DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `user_count` int DEFAULT NULL,
  `value_score` tinyint DEFAULT NULL,
  `alpha_count` int DEFAULT NULL,
  `field_count` int DEFAULT NULL,
  `score` tinyint DEFAULT NULL,
  PRIMARY KEY (`data_set_id`,`delay`,`region`,`universe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='所有的数据集信息,关注中文描述';

api:

```
def get_data_sets(s, region, delay, universe):    """    获取所有的data_sets信息写入MySQL    :param s: requests.session()    :param region: region    :param delay: delay    :param universe: universe    :return: data_sets_list,每个data_set是一个dict,包含data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&limit=20"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    data_sets_list = []    for x in range(0, count, 20):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            data_sets_list.append(                {                    'data_set_id': result['id'],                    'category_id': result['category']['id'],                    'description': result['description'],                    'name': result['name'],                    'pyramid_multiplier': result['pyramidMultiplier'],                    'coverage': result['coverage'],                    'user_count': result['userCount'],                    'value_score': result['valueScore'],                    'alpha_count': result['alphaCount'],                    'field_count': result['fieldCount'],                }            )        time.sleep(4)    return data_sets_list
```

```
if __name__ == "__main__":    s = login()    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        data_sets = get_data_sets(s, region, delay, universe)        with conn.cursor() as cursor:            for data_set in data_sets:                sql = (                    f"insert into worldquant.data_sets(region,delay,universe,data_set_id,category_id,description,name,pyramid_multiplier,coverage,user_count,value_score,alpha_count,field_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                    "on duplicate key update category_id=%s,description=%s,name=%s,pyramid_multiplier=%s,coverage=%s,user_count=%s,value_score=%s,alpha_count=%s,field_count=%s"                )                sql_params = (                    region, delay, universe, data_set['data_set_id'], data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count'],                    data_set['category_id'], data_set['description'], data_set['name'], data_set['pyramid_multiplier'], data_set['coverage'], data_set['user_count'], data_set['value_score'], data_set['alpha_count'], data_set['field_count']                )                cursor.execute(sql, sql_params)        conn.commit()
```

## 二.分地区的field信息

这个所有地区可以合并在一个表格,但是我还没改,暂时按不同地区不同delay分表的
表结构:

-- worldquant.hkg_delay1 definition

CREATE TABLE `hkg_delay1` (
  `field` varchar(100) NOT NULL,
  `region` varchar(100) DEFAULT NULL,
  `delay` char(1) DEFAULT NULL,
  `universe` varchar(100) DEFAULT NULL,
  `datasets` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `coverage` float DEFAULT NULL,
  `userCount` int DEFAULT NULL,
  `alphaCount` int DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

api:

```
def get_fields(s, dataset_id, region, delay, universe):    """    给定data_sets的id,以及参数region,delay,universe,返回符合条件的data_sets里面的fields    :param s: requests.session()    :param dataset_id: data_sets的id    :param region: region    :param delay: delay    :param universe: universe    :return: fields,每个field是一个dict,包含field_type和field_id    """    url_template = (        "[链接已屏蔽]        f"&instrumentType=EQUITY"        f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50"        "&offset={x}"    )    result = s.get(url_template.format(x=0)).json()    # 如果result中没有count字段,则打印result并报错,为了找到错误原因    if 'count' not in result:        print(result)        raise ValueError("No count field in result")    count = result['count']    datafields_list = []    for x in range(0, count, 50):        results = s.get(url_template.format(x=x)).json()['results']        for result in results:            field_type = result['type']            field_id = result['id']            description = result['description']            coverage = result['coverage']            userCount = result['userCount']            alphaCount = result['alphaCount']            datafields_list.append({'field_type': field_type, 'field_id': field_id, 'description': description,'coverage': coverage, 'userCount': userCount, 'alphaCount': alphaCount})    return datafields_list
```

```
if __name__ == "__main__":    s = login()    dataset_ids = [        'other128',        'other16',    ]    region = 'HKG'    delay = 1    universe = 'TOP800'    with pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, database=mysql_db) as conn:        for dataset_id in dataset_ids:            fields = get_fields(s, dataset_id, region, delay, universe)            with conn.cursor() as cursor:                for item in fields:                    sql = (                        f"insert into worldquant.{region}_DELAY1(field,description,region,delay,universe,datasets,type,coverage,userCount,alphaCount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "                        "on duplicate key update description=%s,region=%s,delay=%s,universe=%s,datasets=%s,type=%s,coverage=%s,userCount=%s,alphaCount=%s"                    )                    sql_params = (                        item['field_id'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount'], item['description'], region, delay, universe, dataset_id, item['field_type'], item['coverage'], item['userCount'], item['alphaCount']                    )                    cursor.execute(sql, sql_params)            conn.commit()
```

---

### 帖子 #37: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #38: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #39: 使用[ClickHouse📕]建设你的大型数据库
- **主帖链接**: [L2] 使用[ClickHouse]建设你的大型数据库.md
- **讨论数**: 3

**ClickHouse**  是一个开源的列式数据库管理系统（DBMS），专为在线分析处理（OLAP）场景设计。ClickHouse 以其卓越的查询性能和高效的数据压缩能力而闻名，特别适合处理大规模数据的实时分析查询。

相比  **MySQL** ，ClickHouse 的列式存储和高效压缩使其在大规模数据分析场景下查询性能提升数十倍；相比  **MongoDB** ，ClickHouse 对复杂 SQL 查询和聚合操作的支持更强大，适合实时分析和高性能 OLAP 场景。

本文将持续更新，但不保证能连载完毕，因为我也是刚开始用这个东西，现学现卖

**前置准备：下载clickhouse并安装**

[[ClickHouse📕]Download and Install CK – WorldQuant BRAIN](/hc/en-us/community/posts/29266868911383--ClickHouse-Download-and-Install-CK) 

 **第一步：创建表，每一个表的内容都不一样，需要进行存储，下面是每一个你需要创建的表。** 。

[[ClickHouse📕]table: submitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266765833239--ClickHouse-table-submitted)

[[ClickHouse📕]table: pnls – WorldQuant BRAIN](/hc/en-us/community/posts/29266954512663--ClickHouse-table-pnls)

[[ClickHouse📕]table: fields – WorldQuant BRAIN](/hc/en-us/community/posts/29266990090263--ClickHouse-table-fields)

[[ClickHouse📕]table: unsubmitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266971586327--ClickHouse-table-unsubmitted)

第二步：导入数据

To Be Continue....

您的点赞就是我最大的动力

---

### 帖子 #40: 使用[ClickHouse📕]建设你的大型数据库
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用[ClickHouse]建设你的大型数据库_29266895095063.md
- **讨论数**: 3

**ClickHouse**  是一个开源的列式数据库管理系统（DBMS），专为在线分析处理（OLAP）场景设计。ClickHouse 以其卓越的查询性能和高效的数据压缩能力而闻名，特别适合处理大规模数据的实时分析查询。

相比  **MySQL** ，ClickHouse 的列式存储和高效压缩使其在大规模数据分析场景下查询性能提升数十倍；相比  **MongoDB** ，ClickHouse 对复杂 SQL 查询和聚合操作的支持更强大，适合实时分析和高性能 OLAP 场景。

本文将持续更新，但不保证能连载完毕，因为我也是刚开始用这个东西，现学现卖

**前置准备：下载clickhouse并安装**

[[ClickHouse📕]Download and Install CK – WorldQuant BRAIN](/hc/en-us/community/posts/29266868911383--ClickHouse-Download-and-Install-CK) 

 **第一步：创建表，每一个表的内容都不一样，需要进行存储，下面是每一个你需要创建的表。** 。

[[ClickHouse📕]table: submitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266765833239--ClickHouse-table-submitted)

[[ClickHouse📕]table: pnls – WorldQuant BRAIN](/hc/en-us/community/posts/29266954512663--ClickHouse-table-pnls)

[[ClickHouse📕]table: fields – WorldQuant BRAIN](/hc/en-us/community/posts/29266990090263--ClickHouse-table-fields)

[[ClickHouse📕]table: unsubmitted – WorldQuant BRAIN](/hc/en-us/community/posts/29266971586327--ClickHouse-table-unsubmitted)

第二步：导入数据

To Be Continue....

您的点赞就是我最大的动力

---

### 帖子 #41: 选择最先出现的位置  if backfill_index != -1 and backfill_index != -1:            cut_index = min(backfill_index, backfill_index)
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

### 帖子 #42: 增量下载数据download_data(flag_increment=True)
- **主帖链接**: https://support.worldquantbrain.com[L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md
- **讨论数**: 30

基于  [顾问 WL27618 (Rank 97)](/hc/en-us/profiles/29059197295767-顾问 WL27618 (Rank 97))  发现的本地计算自相关性方法的落地，self-corr只计算本region里提交的所有alphas

首先一些函数，由于有函数说明，这里就不详细展开了

```
import requestsimport pandas as pdimport loggingimport timeimport requestsfrom typing import Optional, Tuplefrom typing import Tuple, Dict, Listfrom typing import Union, List, Tuplefrom concurrent.futures import ThreadPoolExecutorimport picklefrom collections import defaultdictimport numpy as npfrom tqdm import tqdmfrom pathlib import Pathdef sign_in(username, password):    s = requests.Session()    s.auth = (username, password)    try:        response = s.post('[链接已屏蔽])        response.raise_for_status()        logging.info("Successfully signed in")        return s    except requests.exceptions.RequestException as e:        logging.error(f"Login failed: {e}")        return Nonedef save_obj(obj: object, name: str) -> None:    """    保存对象到文件中，以 pickle 格式序列化。    Args:        obj (object): 需要保存的对象。        name (str): 文件名（不包含扩展名），保存的文件将以 '.pickle' 为扩展名。    Returns:        None: 此函数无返回值。    Raises:        pickle.PickleError: 如果序列化过程中发生错误。        IOError: 如果文件写入过程中发生 I/O 错误。    """    with open(name + '.pickle', 'wb') as f:        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)def load_obj(name: str) -> object:    """    加载指定名称的 pickle 文件并返回其内容。    此函数会打开一个以 `.pickle` 为扩展名的文件，并使用 `pickle` 模块加载其内容。    Args:        name (str): 不带扩展名的文件名称。    Returns:        object: 从 pickle 文件中加载的 Python 对象。    Raises:        FileNotFoundError: 如果指定的文件不存在。        pickle.UnpicklingError: 如果文件内容无法被正确反序列化。    """    with open(name + '.pickle', 'rb') as f:        return pickle.load(f)   def wait_get(url: str, max_retries: int = 10) -> "Response":    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。       Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。       Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])    df = df.rename(columns={'date':'Date', 'pnl':alpha_id})    df = df[['Date', alpha_id]]    return dfdef get_alpha_pnls(    alphas: list[dict],    alpha_pnls: Optional[pd.DataFrame] = None,    alpha_ids: Optional[dict[str, list]] = None) -> Tuple[dict[str, list], pd.DataFrame]:    """    获取 alpha 的 PnL 数据，并按区域分类 alpha 的 ID。    Args:        alphas (list[dict]): 包含 alpha 信息的列表，每个元素是一个字典，包含 alpha 的 ID 和设置等信息。        alpha_pnls (Optional[pd.DataFrame], 可选): 已有的 alpha PnL 数据，默认为空的 DataFrame。        alpha_ids (Optional[dict[str, list]], 可选): 按区域分类的 alpha ID 字典，默认为空字典。    Returns:        Tuple[dict[str, list], pd.DataFrame]:            - 按区域分类的 alpha ID 字典。            - 包含所有 alpha 的 PnL 数据的 DataFrame。    """    if alpha_ids is None:        alpha_ids = defaultdict(list)    if alpha_pnls is None:        alpha_pnls = pd.DataFrame()       new_alphas = [item for item in alphas if item['id'] not in alpha_pnls.columns]    if not new_alphas:        return alpha_ids, alpha_pnls       for item_alpha in new_alphas:        alpha_ids[item_alpha['settings']['region']].append(item_alpha['id'])    fetch_pnl_func = lambda alpha_id: _get_alpha_pnl(alpha_id).set_index('Date')    with ThreadPoolExecutor(max_workers=10) as executor:        results = executor.map(fetch_pnl_func, [item['id'] for item in new_alphas])    alpha_pnls = pd.concat([alpha_pnls] + list(results), axis=1)    alpha_pnls.sort_index(inplace=True)    return alpha_ids, alpha_pnlsdef get_os_alphas(limit: int = 100, get_first: bool = False) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    retries = 0    total_alphas = 100    while len(fetched_alphas) < total_alphas:        print(f"Fetching alphas from offset {offset} to {offset + limit}")        url = f"[链接已屏蔽]        res = wait_get(url).json()        if offset == 0:            total_alphas = res['count']        alphas = res["results"]        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphas[:total_alphas]def calc_self_corr(    alpha_id: str,    os_alpha_rets: pd.DataFrame | None = None,    os_alpha_ids: dict[str, str] | None = None,    alpha_result: dict | None = None,    return_alpha_pnls: bool = False,    alpha_pnls: pd.DataFrame | None = None) -> float | tuple[float, pd.DataFrame]:    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    print(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corrdef download_data(flag_increment=True):    """    下载数据并保存到指定路径。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        flag_increment (bool): 是否使用增量下载，默认为 True。    """    if flag_increment:        try:            os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))            os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))            ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))            exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]        except Exception as e:            logging.error(f"Failed to load existing data: {e}")            os_alpha_ids = None            os_alpha_pnls = None            exist_alpha = []            ppac_alpha_ids = []    else:        os_alpha_ids = None        os_alpha_pnls = None        exist_alpha = []        ppac_alpha_ids = []           if os_alpha_ids is None:        alphas = get_os_alphas(limit=100, get_first=False)    else:        alphas = get_os_alphas(limit=30, get_first=True)       alphas = [item for item in alphas if item['id'] not in exist_alpha]    ppac_alpha_ids += [item['id'] for item in alphas for item_match in item['classifications'] if item_match['name'] == 'Power Pool Alpha']               os_alpha_ids, os_alpha_pnls = get_alpha_pnls(alphas, alpha_pnls=os_alpha_pnls, alpha_ids=os_alpha_ids)    save_obj(os_alpha_ids, str(cfg.data_path / 'os_alpha_ids'))    save_obj(os_alpha_pnls, str(cfg.data_path / 'os_alpha_pnls'))    save_obj(ppac_alpha_ids, str(cfg.data_path / 'ppac_alpha_ids'))    print(f'新下载的alpha数量: {len(alphas)}, 目前总共alpha数量: {os_alpha_pnls.shape[1]}')def load_data(tag=None):    """    加载数据。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        tag (str): 数据标记，默认为 None。    """    os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))    os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))    ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))    if tag=='PPAC':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha in ppac_alpha_ids]    elif tag=='SelfCorr':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha not in ppac_alpha_ids]    else:        os_alpha_ids = os_alpha_ids    exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]    os_alpha_pnls = os_alpha_pnls[exist_alpha]    os_alpha_rets = os_alpha_pnls - os_alpha_pnls.ffill().shift(1)    os_alpha_rets = os_alpha_rets[pd.to_datetime(os_alpha_rets.index)>pd.to_datetime(os_alpha_rets.index).max() - pd.DateOffset(years=4)]    return os_alpha_ids, os_alpha_rets
```

首先把上述函数拷贝出来

在配置的cfg里添加账户和密码以及os_alpha保存的路径

```
class cfg:    username = ""    password = ""    data_path = Path('.')sess = sign_in(cfg.username, cfg.password)
```

增量下载OS数据，下载好的数据将会保存在data_path里

```
# 增量下载数据download_data(flag_increment=True)
```

之后加载数据，计算corr。

其中`load_data`函数里有一个可选参数tag。来区分获得alpha，

如果设置tag='PPAC'则只获取PPAC池子里的alpha，

如果设置tag='SelfCorr'则只获取除了PPAC池子里的其他alpha

如果不设置或者 设置为None，则获取所有提交的alpha

calc_self_corr返回最大的自相关性

```
alpha_id = 'OJwdKNb'os_alpha_ids, os_alpha_rets = load_data()calc_self_corr(    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)
```

我在此选了两个例子用以展示结果

第一个 例子是一个`厂alpha`


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 30OOK
> OOOK
> OOOK
> Jan '14
> Jan'15
> Jan'16
> Jan '17
> Jan '18
> Jan'19
> Jan '20
> Jan '21
> Jan '23
> Pnl
> Jan 22


其wq平台的线上self-corr如下


> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> [aimUm
> [inimUT
> 0.0719
> -0.0715
> 名字
> Unlyerse
> Correlaton
> Sharpe
> Returns
> Tumovar
> Htess
> Margln
> ATOITITOUIS
> current)
> TOP3O00
> 1.0000
> 6.32
> 255.44%
> 30.05%6
> 18.43
> 170.029
> anonyymous
> TOPIOOO
> 0.0719
> 2.59
> 12014
> 7.1395
> 2.33
> 33.539
> aOTIMOUs
> TOP230
> 0.0634
> 2.52
> 10.744
> 13.3591
> 2.30
> 11.53922
> aROTIIOUs
> TOP3OO
> 0.0525
> 3.8-
> 13.134
> 11.3695
> 3.34
> 2.059
> TyMOUs
> TOP3OI
> 0.0495
> 5.53
> 10.944
> 10.8793
> 5.17
> 20.1292
> anOnyMOUs
> ILLIQUID_MINVOLIII
> 0.0399
> 3.96
> 3.734
> 12.5595
> 3.29
> 13.79923
> L2st


通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha
> OJWdKMb
> O5_alpha_ids,
> O5_alpha_rets
> load_data
> Selfcorr
> Calc_self_corr(
> alpha_id-alpha_id,
> O5_alpha
> rets=os_alpha
> pets,
> O5_alpha_ids=os_alpha_ids,
> 3ZKROG
> 0719
> IMOOON
> 0.0684
> Xn68QGb
> 0526
> Oogjjpb
> 0.0496
> gnrlMpl
> 0399
> RdgYkao
> 0587
> AkYpgIw
> 0.0604
> KkGPBJI
> 0655
> SMVZb2I
> 0.0703
> KO3M3eB
> 0715
> Length: 367
> dtype:
> float64
> 叩.float64(8.07191757289855728)
> (tn=


其线上PPAC结果为： Power Pool correlation 0.0356 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.

通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> OJWdKMb
> O5_alpha_ids,
> O5_alpha
> pets
> load_data
> PPAC
> Calc_self
> Corr(
> alpha_id-alpha_id,
> O5_alpha_rets=os_alpha_
> pets
> O5_alpha_ids=os_alpha_ids,
> WL8EVgX
> 0356
> V0a7JR2
> 0.0291
> ONjAqWb
> 0269
> O8nlN3q
> 0.0260
> pSeGPvv
> 0222
> aVNJAdI
> 0286
> SjbrMGN
> 0.0231
> X1Z08Y]
> 0247
> e6813诏
> 0.0267
> WgBar7e
> -0.0314
> Length: 61,
> dtype:
> f1oat64
> 叩.float64(8.03561886586891495)
> (tD8=


第二个 例子是一个正常的例子


> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> PIL
> LOOOK
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> 2023


其wq平台的线上self-corr如下 
> [!NOTE] [图片 OCR 识别内容]
> 名宇
> UnNerse
> Correlatlon
> Sharpe
> Returns
> TurNOVer
> Hltness
> Margln
> anonymous (current)
> TOP3000
> 1.0000
> 1.51
> 6.329
> 3.0396
> 1.07
> 41.708
> anONNMOUs
> TOP300
> 0.5243
> 11.034
> 7.230
> 172
> 305292
> anOnyMOUs
> TOF3JOO
> 0.5241
> 10.244
> 4.9055
> 11.80922
> anonymous
> TOP300
> 0.5051
> 34
> 11.744
> 11.303
> 3.30
> 20.779323
> anOnyMOUs
> TOF3JOO
> 0.-931
> 153
> 12.12北
> 10.7350
> 1.57
> 22.499522
> anONNMOUs
> TOP300
> 0.4453
> 4.16
> 19.254
> 10.8130
> 5.15
> 35.52933


通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> 1P13*52
> O5_alpha_ids,
> O5_alpha
> pets
> load_data (ta=
> Selfcorr
> Calc
> cor(
> alpha_id-alpha_id,
> O5_alpha_rets=os_alpha_rets,
> Os_alpha_ids=os_alpha_ids,
> 146]
> IXqSZMJ
> 0.5243
> ANKqaGE
> 0.5241
> OLOAgYI
> 0.5061
> EIMGbe]
> 4901
> PZAVYRL
> 0.4463
> LnOZEYG
> 0.3494
> MbAGKZ8
> 0.3495
> Mbgzgjr
> 0.3523
> XkGORLS
> 0.3719
> JnLZlnl
> 0.3952
> Length: 386, dtype:
> float64
> m.float64 (0.524288988654845 )
> Self


其线上PPAC结果为： Power Pool correlation 0.4901 is below cutoff of 0.5, or Sharpe is better by 10.0% or more.

通过上述代码本地计算的结果如下


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> JPY3*52
> 05_alpha_ids,
> O5_alpha
> load_data
> PPAC
> Calc_self_corr(
> alpha_id-alpha_id,
> O5_alpha
> rets=os_alpha_rets,
> O5_alpha_ids=os_alpha_ids,
> OWZzzan
> 4901
> AOnjj8e
> 0.4667
> aVNJAdI
> 4495
> 3jLrp8e
> 0.4468
> YxdOKRV
> 0.4382
> ONnJOEV
> 0.0129
> GbuPrwG
> 0186
> PBKaEWN
> -0.0220
> XIBQVIJ
> -0.0322
> 15j7091
> -0.0604
> Length:
> 61, dtype: float64
> m.float64(9.4980856236004994)
> pots
> (tn=


---

### 帖子 #43: 这个因子到底能不能交？（下） 【传奇耐打王系列一】
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

### 帖子 #44: 从群友帖子里面抄到的SA分享,几乎思路完全一致
- **主帖链接**: 从群友帖子里面抄到的SA分享几乎思路完全一致.md
- **讨论数**: 0

SELECTION:bool = (not (own) &&in(competitions,"HCAC2025")&&# (neutralization == 'FAST')&&datacategory_count<=3 &&short_count+long_count > 2000 &&(( prod_correlation >0.4) || (prod_correlation <0.35 ||prod_correlation >0.25)||(prod_correlation <0.2) ));weight = (1*((long_count+ short_count)/ universe_size(universe))*if_else(prod_correlation > 0.7, 2, 1.5)*(1 - self_correlation));bool * weightCOMBO:stats = generate_stats(alpha);w1 = (1+ts_mean(stats.returns,20))/(1+ts_mean(stats.returns,252));W2 = ts_ir(stats.returns,63)/reduce_powersum(self_corr(stats.returns,252),constant=2);scale(w1)+ scale(w2)

---

### 帖子 #45: (neutralization == 'FAST')&&
- **主帖链接**: https://support.worldquantbrain.com从群友帖子里面抄到的SA分享几乎思路完全一致_33137757923223.md
- **讨论数**: 0

SELECTION:
bool = (

not (own) &&

in(competitions,"HCAC2025")&&

# (neutralization == 'FAST')&&

datacategory_count<=3 &&

short_count+long_count > 2000 &&

(( prod_correlation >0.4) || (prod_correlation <0.35 ||prod_correlation >0.25)||(prod_correlation <0.2) )

);

weight = (

1

*((long_count+ short_count)/ universe_size(universe))

*if_else(prod_correlation > 0.7, 2, 1.5)

*(1 - self_correlation)

);

bool * weight

COMBO:

stats = generate_stats(alpha);

w1 = (1+ts_mean(stats.returns,20))/(1+ts_mean(stats.returns,252));

W2 = ts_ir(stats.returns,63)/reduce_powersum(self_corr(stats.returns,252),constant=2);

scale(w1)+ scale(w2)

---

### 帖子 #46: 使用本地时间,精确到秒去获取回测过的alpha
- **主帖链接**: 使用本地时间精确到秒去获取回测过的alpha.md
- **讨论数**: 3

模板里面get_alpha函数只能精确到日期, 而且使用的美国时间和我们本地时间有时差.但是通过 查看网页源代码,发现是可以用秒级精度查询alpha的,所以对get_alpha函数做了一点点小小的修改.将次代码复制替换掉原来模板里面的get_alpha函数即可使用.代码如下:

```
import pytzdef convert_to_est(china_time_str):    # 将中国时间字符串转换为datetime对象    china_time = datetime.datetime.strptime(china_time_str, "%m-%d %H:%M:%S")       # 假设年份是当前年份    china_time = china_time.replace(year=datetime.datetime.now().year)       # 定义中国时区和美国东部时区    china_tz = pytz.timezone('Asia/Shanghai')    est_tz = pytz.timezone('US/Eastern')       # 将中国时间转换为UTC时间    china_time = china_tz.localize(china_time)    utc_time = china_time.astimezone(pytz.utc)       # 将UTC时间转换为美国东部时间    est_time = utc_time.astimezone(est_tz)       return est_time.strftime("%Y-%m-%dT%H:%M:%S-05:00")def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage):    s = login()    output = []    count = 0       # 转换时间格式    start_date_est = convert_to_est(start_date)    end_date_est = convert_to_est(end_date)       for i in range(0, alpha_num, 100):        print(i)        url_e = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_est  \                + "&dateCreated%3C=" + end_date_est \                + "&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \                + str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"        url_c = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_est  \                + "&dateCreated%3C=" + end_date_est \                + "&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \                + str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"        urls = [url_e]        if usage != "submit":            urls.append(url_c)        for url in urls:            response = s.get(url)            try:                alpha_list = response.json()["results"]                print(response.json())                for j in range(len(alpha_list)):                    alpha_id = alpha_list[j]["id"]                    name = alpha_list[j]["name"]                    dateCreated = alpha_list[j]["dateCreated"]                    sharpe = alpha_list[j]["is"]["sharpe"]                    fitness = alpha_list[j]["is"]["fitness"]                    turnover = alpha_list[j]["is"]["turnover"]                    margin = alpha_list[j]["is"]["margin"]                    longCount = alpha_list[j]["is"]["longCount"]                    shortCount = alpha_list[j]["is"]["shortCount"]                    decay = alpha_list[j]["settings"]["decay"]                    exp = alpha_list[j]['regular']['code']                    count += 1                    if (longCount + shortCount) > 100:                        if sharpe < -sharpe_th:                            exp = "-%s"%exp                        rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]                        print(rec)                        if turnover > 0.7:                            rec.append(decay*4)                        elif turnover > 0.6:                            rec.append(decay*3+3)                        elif turnover > 0.5:                            rec.append(decay*3)                        elif turnover > 0.4:                            rec.append(decay*2)                        elif turnover > 0.35:                            rec.append(decay+4)                        elif turnover > 0.3:                            rec.append(decay+2)                        output.append(rec)            except:                print("%d finished re-login"%i)                s = login()    print("count: %d"%count)    return output
```

那么调用代码的传入参数也会有相应的变化,需要在日期后面加上时分秒,其余保持不变:

```
alphas = get_alphas("01-15 19:20:23", "01-15 22:02:12", 0.0, 0.0, "ASI", 100, "submit")
```

---

### 帖子 #47: 使用本地时间,精确到秒去获取回测过的alpha
- **主帖链接**: https://support.worldquantbrain.com使用本地时间精确到秒去获取回测过的alpha_29242202291863.md
- **讨论数**: 3

模板里面get_alpha函数只能精确到日期, 而且使用的美国时间和我们本地时间有时差.但是通过 查看网页源代码,发现是可以用秒级精度查询alpha的,所以对get_alpha函数做了一点点小小的修改.将次代码复制替换掉原来模板里面的get_alpha函数即可使用.代码如下:

```
import pytzdef convert_to_est(china_time_str):    # 将中国时间字符串转换为datetime对象    china_time = datetime.datetime.strptime(china_time_str, "%m-%d %H:%M:%S")       # 假设年份是当前年份    china_time = china_time.replace(year=datetime.datetime.now().year)       # 定义中国时区和美国东部时区    china_tz = pytz.timezone('Asia/Shanghai')    est_tz = pytz.timezone('US/Eastern')       # 将中国时间转换为UTC时间    china_time = china_tz.localize(china_time)    utc_time = china_time.astimezone(pytz.utc)       # 将UTC时间转换为美国东部时间    est_time = utc_time.astimezone(est_tz)       return est_time.strftime("%Y-%m-%dT%H:%M:%S-05:00")def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage):    s = login()    output = []    count = 0       # 转换时间格式    start_date_est = convert_to_est(start_date)    end_date_est = convert_to_est(end_date)       for i in range(0, alpha_num, 100):        print(i)        url_e = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_est  \                + "&dateCreated%3C=" + end_date_est \                + "&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \                + str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"        url_c = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date_est  \                + "&dateCreated%3C=" + end_date_est \                + "&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \                + str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"        urls = [url_e]        if usage != "submit":            urls.append(url_c)        for url in urls:            response = s.get(url)            try:                alpha_list = response.json()["results"]                print(response.json())                for j in range(len(alpha_list)):                    alpha_id = alpha_list[j]["id"]                    name = alpha_list[j]["name"]                    dateCreated = alpha_list[j]["dateCreated"]                    sharpe = alpha_list[j]["is"]["sharpe"]                    fitness = alpha_list[j]["is"]["fitness"]                    turnover = alpha_list[j]["is"]["turnover"]                    margin = alpha_list[j]["is"]["margin"]                    longCount = alpha_list[j]["is"]["longCount"]                    shortCount = alpha_list[j]["is"]["shortCount"]                    decay = alpha_list[j]["settings"]["decay"]                    exp = alpha_list[j]['regular']['code']                    count += 1                    if (longCount + shortCount) > 100:                        if sharpe < -sharpe_th:                            exp = "-%s"%exp                        rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]                        print(rec)                        if turnover > 0.7:                            rec.append(decay*4)                        elif turnover > 0.6:                            rec.append(decay*3+3)                        elif turnover > 0.5:                            rec.append(decay*3)                        elif turnover > 0.4:                            rec.append(decay*2)                        elif turnover > 0.35:                            rec.append(decay+4)                        elif turnover > 0.3:                            rec.append(decay+2)                        output.append(rec)            except:                print("%d finished re-login"%i)                s = login()    print("count: %d"%count)    return output
```

那么调用代码的传入参数也会有相应的变化,需要在日期后面加上时分秒,其余保持不变:

```
alphas = get_alphas("01-15 19:20:23", "01-15 22:02:12", 0.0, 0.0, "ASI", 100, "submit")
```

---

### 帖子 #48: 关于快速定位回测报错的小tips
- **主帖链接**: 关于快速定位回测报错的小tips.md
- **讨论数**: 3

各位顾问好,在我们回测alpha的过程中,总会由于这样那样的情况,导致发给服务器去回测的数据存在一点问题,这时候就会导致回测报错,页面会返回一个报错的URL,通常情况下,我们需要点开返回给我的报错信息URL,然后从那里面的每一个child去再次复制打开,才能看到具体的错误信息,这个方式太过繁琐了.所以我简单写了一个python函数,直接在IDE里面查看具体的错误信息,代码如下:def filter_non_cancelled_results(s, url):try:# 使用 session 对象发送请求获取 URL 的内容response = s.get(url)response.raise_for_status()  # 检查请求是否成功data = response.json()# 提取 children 列表children = data.get("children", [])# 存储非 CANCELLED 状态的结果non_cancelled_results = []# 遍历 children 列表中的每个元素for child_id in children:# 构建新的 URLnew_url = f"[链接已屏蔽] 使用 session 对象发送请求获取新 URL 的内容child_response = s.get(new_url)child_response.raise_for_status()  # 检查请求是否成功child_data = child_response.json()# 检查状态是否不是 CANCELLEDif child_data.get("status") != "CANCELLED":non_cancelled_results.append(child_data)except requests.RequestException as e:print(f"请求 {new_url} 时出错: {e}")# 避免请求太快,这个可以修改sleep(1)# 打印非 CANCELLED 状态的结果for result in non_cancelled_results:print(result)except requests.RequestException as e:print(f"请求 {url} 时出错: {e}")except ValueError as e:print(f"解析 JSON 数据时出错: {e}")filter_non_cancelled_results(s, '[链接已屏蔽])只会把出现error的child信息打印出来,报错信息可能如下:{'id': '***', 'type': 'REGULAR', 'status': 'ERROR', 'message': 'Attempted to use unknown variable ***', 'location': {'line': 3, 'start': 116, 'end': 117, 'property': 'regular'}}{'id': '***', 'type': 'REGULAR', 'status': 'ERROR', 'message': 'Attempted to use unknown variable ***', 'location': {'line': 3, 'start': 117, 'end': 118, 'property': 'regular'}}

---

### 帖子 #49: 关于快速定位回测报错的小tips
- **主帖链接**: https://support.worldquantbrain.com关于快速定位回测报错的小tips_30346863437975.md
- **讨论数**: 3

各位顾问好,

在我们回测alpha的过程中,总会由于这样那样的情况,导致发给服务器去回测的数据存在一点问题,这时候就会导致回测报错,页面会返回一个报错的URL,通常情况下,我们需要点开返回给我的报错信息URL,然后从那里面的每一个child去再次复制打开,才能看到具体的错误信息,这个方式太过繁琐了.

所以我简单写了一个python函数,直接在IDE里面查看具体的错误信息,代码如下:

```
def filter_non_cancelled_results(s, url):    try:        # 使用 session 对象发送请求获取 URL 的内容        response = s.get(url)        response.raise_for_status()  # 检查请求是否成功        data = response.json()        # 提取 children 列表        children = data.get("children", [])        # 存储非 CANCELLED 状态的结果        non_cancelled_results = []        # 遍历 children 列表中的每个元素        for child_id in children:            # 构建新的 URL            new_url = f"[链接已屏蔽]            try:                # 使用 session 对象发送请求获取新 URL 的内容                child_response = s.get(new_url)                child_response.raise_for_status()  # 检查请求是否成功                child_data = child_response.json()                # 检查状态是否不是 CANCELLED                if child_data.get("status") != "CANCELLED":                    non_cancelled_results.append(child_data)            except requests.RequestException as e:                print(f"请求 {new_url} 时出错: {e}")                  # 避免请求太快,这个可以修改            sleep(1)        # 打印非 CANCELLED 状态的结果        for result in non_cancelled_results:            print(result)    except requests.RequestException as e:        print(f"请求 {url} 时出错: {e}")    except ValueError as e:        print(f"解析 JSON 数据时出错: {e}")filter_non_cancelled_results(s, '[链接已屏蔽])
```

只会把出现error的child信息打印出来,报错信息可能如下:

```
{'id': '***', 'type': 'REGULAR', 'status': 'ERROR', 'message': 'Attempted to use unknown variable ***', 'location': {'line': 3, 'start': 116, 'end': 117, 'property': 'regular'}}{'id': '***', 'type': 'REGULAR', 'status': 'ERROR', 'message': 'Attempted to use unknown variable ***', 'location': {'line': 3, 'start': 117, 'end': 118, 'property': 'regular'}}
```

---

### 帖子 #50: Simulate third ordermdl53_lv3_th_pools = load_data('20250110062830_mdl53_lv3_th_pools.pkl')multi_simulate(mdl53_lv3_th_pools, 'SUBINDUSTRY', 'ASI', 'MINVOL1M', 0)
- **主帖链接**: 新人保存数据的小tip 放进machine_lib直接可用.md
- **讨论数**: 2

主要面向新人,大佬自己搭建数据库的,就无需看了啊哈.

在回测的过程中,偶尔会遇到需要中断回测或者由于网络导致回测断开的情况,但是新人没有现成的数据库备份等,所以我写了一个简单的保存dataset或者simulation pools的小函数,支持保存所有程序运行过程中的数据.

```

```

```

```

```
# save_data,保存所有数据对象,import的库,如果已经存在可以删除import pickleimport timeimport pandas as pdimport osdef save_data(data, data_name=None):    """    存储Python执行过程中的数据到文件，文件名格式为存储时间+数据的名称    参数:    data: 要存储的数据，可以是列表、字典、DataFrame等可序列化的对象    data_name: 数据的名称（可选），如果未提供，将根据数据类型自动生成一个名称    """    if data_name is None:        if hasattr(data, 'name'):            data_name = data.name        else:            data_name = type(data).__name__    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())    file_name = f"{current_time}_{data_name}.pkl"    # 判断存储文件夹是否存在，不存在则创建    if not os.path.exists('./stored_data/'):        os.makedirs('./stored_data/')    file_path = os.path.join('./stored_data/', file_name)    if isinstance(data, pd.DataFrame):        file_path = file_path.replace('.pkl', '.csv')        data.to_csv(file_path, index=False)    else:        with open(file_path, 'wb') as f:            pickle.dump(data, f)    print(f"数据已成功保存到 {file_path}")
```

```
# load_data,读取已保存的数据,import的库,如果已经存在可以删除import pickleimport pandas as pdimport osdef load_data(file_name):    """    从指定文件中读取之前保存的数据    参数:    file_name: 要读取的数据文件的名称，包含扩展名（如.pkl或.csv等）    返回:    读取到的数据对象    """    file_path = os.path.join('./stored_data/', file_name)    if not os.path.exists(file_path):        raise FileNotFoundError(f"文件 {file_path} 不存在，请检查文件名是否正确。")    if file_name.endswith('.csv'):        try:            data = pd.read_csv(file_path)        except pd.errors.ParserError:            raise ValueError(f"文件 {file_path} 在解析为CSV格式时出现错误，请检查文件内容是否符合CSV规范。")    else:        try:            with open(file_path, 'rb') as f:                data = pickle.load(f)        except pickle.UnpicklingError:            raise ValueError(f"文件 {file_path} 在反序列化（使用pickle）时出现错误，请检查文件是否损坏。")    return data
```

将以上两个函数直接放入machine_lib.py即可.

使用举例:将第三道工序的pools保存到本地,savedata接受两个参数,第一个是你要保存的数据对象,第二个是你指定的保存名称,注意第二个是str格式,然后会执行保存,并在你指定的保存名称前面增加时间,确保不会重复保存.执行后会得到一行打印数据:数据已成功保存到  [./stored_data/20250110062830_mdl53_lv3_th_pools.pkl]([链接已屏蔽]) ,其中' [20250110062830_mdl53_lv3_th_pools.pkl]([链接已屏蔽]) '是你保存的对象在本地的名字,需要读取这个对象的时候,复制这个名字到load_data函数中即可.

```
# Simulate third ordermdl53_lv3_th_pools = load_task_pool(th_alpha_list, 10, 4)save_data(mdl53_lv3_th_pools,'mdl53_lv3_th_pools')print('mdl53_lv3_th_pools'+': '+str(len(mdl53_lv3_th_pools)))multi_simulate(mdl53_lv3_th_pools, 'SUBINDUSTRY', 'ASI', 'MINVOL1M', 0)
```

读取数据举例,在程序中断后查看日志找到保存的对象名字,之后恢复对象即可.

```
# Simulate third ordermdl53_lv3_th_pools = load_data('20250110062830_mdl53_lv3_th_pools.pkl')multi_simulate(mdl53_lv3_th_pools, 'SUBINDUSTRY', 'ASI', 'MINVOL1M', 0)
```

---

### 帖子 #51: Simulate third ordermdl53_lv3_th_pools = load_data('20250110062830_mdl53_lv3_th_pools.pkl')multi_simulate(mdl53_lv3_th_pools, 'SUBINDUSTRY', 'ASI', 'MINVOL1M', 0)
- **主帖链接**: https://support.worldquantbrain.com新人保存数据的小tip 放进machine_lib直接可用_29142697559575.md
- **讨论数**: 2

主要面向新人,大佬自己搭建数据库的,就无需看了啊哈.

在回测的过程中,偶尔会遇到需要中断回测或者由于网络导致回测断开的情况,但是新人没有现成的数据库备份等,所以我写了一个简单的保存dataset或者simulation pools的小函数,支持保存所有程序运行过程中的数据.

```

```

```

```

```
# save_data,保存所有数据对象,import的库,如果已经存在可以删除import pickleimport timeimport pandas as pdimport osdef save_data(data, data_name=None):    """    存储Python执行过程中的数据到文件，文件名格式为存储时间+数据的名称    参数:    data: 要存储的数据，可以是列表、字典、DataFrame等可序列化的对象    data_name: 数据的名称（可选），如果未提供，将根据数据类型自动生成一个名称    """    if data_name is None:        if hasattr(data, 'name'):            data_name = data.name        else:            data_name = type(data).__name__    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())    file_name = f"{current_time}_{data_name}.pkl"    # 判断存储文件夹是否存在，不存在则创建    if not os.path.exists('./stored_data/'):        os.makedirs('./stored_data/')    file_path = os.path.join('./stored_data/', file_name)    if isinstance(data, pd.DataFrame):        file_path = file_path.replace('.pkl', '.csv')        data.to_csv(file_path, index=False)    else:        with open(file_path, 'wb') as f:            pickle.dump(data, f)    print(f"数据已成功保存到 {file_path}")
```

```
# load_data,读取已保存的数据,import的库,如果已经存在可以删除import pickleimport pandas as pdimport osdef load_data(file_name):    """    从指定文件中读取之前保存的数据    参数:    file_name: 要读取的数据文件的名称，包含扩展名（如.pkl或.csv等）    返回:    读取到的数据对象    """    file_path = os.path.join('./stored_data/', file_name)    if not os.path.exists(file_path):        raise FileNotFoundError(f"文件 {file_path} 不存在，请检查文件名是否正确。")    if file_name.endswith('.csv'):        try:            data = pd.read_csv(file_path)        except pd.errors.ParserError:            raise ValueError(f"文件 {file_path} 在解析为CSV格式时出现错误，请检查文件内容是否符合CSV规范。")    else:        try:            with open(file_path, 'rb') as f:                data = pickle.load(f)        except pickle.UnpicklingError:            raise ValueError(f"文件 {file_path} 在反序列化（使用pickle）时出现错误，请检查文件是否损坏。")    return data
```

将以上两个函数直接放入machine_lib.py即可.

使用举例:将第三道工序的pools保存到本地,savedata接受两个参数,第一个是你要保存的数据对象,第二个是你指定的保存名称,注意第二个是str格式,然后会执行保存,并在你指定的保存名称前面增加时间,确保不会重复保存.执行后会得到一行打印数据:数据已成功保存到  [./stored_data/20250110062830_mdl53_lv3_th_pools.pkl]([链接已屏蔽]) ,其中' [20250110062830_mdl53_lv3_th_pools.pkl]([链接已屏蔽]) '是你保存的对象在本地的名字,需要读取这个对象的时候,复制这个名字到load_data函数中即可.

```
# Simulate third ordermdl53_lv3_th_pools = load_task_pool(th_alpha_list, 10, 4)save_data(mdl53_lv3_th_pools,'mdl53_lv3_th_pools')print('mdl53_lv3_th_pools'+': '+str(len(mdl53_lv3_th_pools)))multi_simulate(mdl53_lv3_th_pools, 'SUBINDUSTRY', 'ASI', 'MINVOL1M', 0)
```

读取数据举例,在程序中断后查看日志找到保存的对象名字,之后恢复对象即可.

```
# Simulate third ordermdl53_lv3_th_pools = load_data('20250110062830_mdl53_lv3_th_pools.pkl')multi_simulate(mdl53_lv3_th_pools, 'SUBINDUSTRY', 'ASI', 'MINVOL1M', 0)
```

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《1，2，3月value factor更新，国区进步最快的10位顾问经验分享》的评论回复
- **帖子链接**: [Commented] 123月value factor更新国区进步最快的10位顾问经验分享.md
- **评论时间**: 1年前

难道你就是那万中无一的INSIDER?提前知道了内幕信息?(doge)
虽然还没有看到4月VF更新,但我希望这次VF能够涨幅达到0.5以上
梦想总是要有的,万一实现了呢?
四月份我可是兢兢业业提交了20天因子啊,是我最努力的时候了.
=============================================================分割线
还是要向课代表学习,长期稳定0.9以上的VF,这是什么先天挖矿圣体!

---

### 探讨 #2: 关于《1，2，3月value factor更新，国区进步最快的10位顾问经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 123月value factor更新国区进步最快的10位顾问经验分享_32732928355223.md
- **评论时间**: 1年前

难道你就是那万中无一的INSIDER?提前知道了内幕信息?(doge)
虽然还没有看到4月VF更新,但我希望这次VF能够涨幅达到0.5以上
梦想总是要有的,万一实现了呢?
四月份我可是兢兢业业提交了20天因子啊,是我最努力的时候了.
=============================================================分割线
还是要向课代表学习,长期稳定0.9以上的VF,这是什么先天挖矿圣体!

---

### 探讨 #3: 关于《4月combined更新，国区进步最显著的10位！经验分享》的评论回复
- **帖子链接**: [Commented] 4月combined更新国区进步最显著的10位经验分享.md
- **评论时间**: 1年前

课代表因为performance一如既往稳定的可怕的高,所以此类榜单不会有他的名字出现.
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

从上面的数据对比,可以看到,select的变化幅度远小于combined,虽然不是同一样本,但是也能够反映出select的因子相对更加稳健,不论是好的稳健还是差的稳健;大多数人select的变化幅度并不大,所以如果我们按照select的标准提交alpha,那么我们的combined也会稳健很多.

课代表有数据的话,可以看一下国区所有人的combined和select变化情况,哈哈哈哈哈哈哈

---

### 探讨 #4: 关于《4月combined更新，国区进步最显著的10位！经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 4月combined更新国区进步最显著的10位经验分享_32732849016215.md
- **评论时间**: 1年前

课代表因为performance一如既往稳定的可怕的高,所以此类榜单不会有他的名字出现.
---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

从上面的数据对比,可以看到,select的变化幅度远小于combined,虽然不是同一样本,但是也能够反映出select的因子相对更加稳健,不论是好的稳健还是差的稳健;大多数人select的变化幅度并不大,所以如果我们按照select的标准提交alpha,那么我们的combined也会稳健很多.

课代表有数据的话,可以看一下国区所有人的combined和select变化情况,哈哈哈哈哈哈哈

---

### 探讨 #5: 关于《About creating a data table to update genius level by day》的评论回复
- **帖子链接**: [Commented] About creating a data table to update genius level by day.md
- **评论时间**: 1年前

Actually, although this feature isn't explicitly displayed, the number of submitted alphas, combined performance, and pyramids of each advisor can be found. Perhaps the official platform encourages us to explore independently. If the feature you mentioned is officially opened, the advisors above have already listed its advantages. Now, let me discuss potential issues:

First, it might lead all advisors to submit alphas solely for the "Genius" status. Since Genius rewards alphas with fewer operators, there's a high risk of underfitting. For example, an alpha like  `ts_delta(close, 5)`  with a Sharpe ratio of 1.58 and fitness of 1 meets the submission criteria—it uses only one field and one operator. However, if we optimize it with  `hump_decay(group_rank(ts_delta(close, 5), subindustry), ...)`  by adding two more operators, its Sharpe ratio increases to 2 and fitness to 1.5. This optimization, without overfitting, makes the factor more robust. But if everyone pursues Genius, they may choose simpler alphas to minimize operators/fields, resulting in a flood of underfitted alphas—likely not the outcome the platform intends.

---

### 探讨 #6: 关于《About creating a data table to update genius level by day》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] About creating a data table to update genius level by day_32873834091159.md
- **评论时间**: 1年前

Actually, although this feature isn't explicitly displayed, the number of submitted alphas, combined performance, and pyramids of each advisor can be found. Perhaps the official platform encourages us to explore independently. If the feature you mentioned is officially opened, the advisors above have already listed its advantages. Now, let me discuss potential issues:

First, it might lead all advisors to submit alphas solely for the "Genius" status. Since Genius rewards alphas with fewer operators, there's a high risk of underfitting. For example, an alpha like  `ts_delta(close, 5)`  with a Sharpe ratio of 1.58 and fitness of 1 meets the submission criteria—it uses only one field and one operator. However, if we optimize it with  `hump_decay(group_rank(ts_delta(close, 5), subindustry), ...)`  by adding two more operators, its Sharpe ratio increases to 2 and fitness to 1.5. This optimization, without overfitting, makes the factor more robust. But if everyone pursues Genius, they may choose simpler alphas to minimize operators/fields, resulting in a flood of underfitted alphas—likely not the outcome the platform intends.

---

### 探讨 #7: 关于《Achieving a Value Factor of 0.98: Lessons Learned and Advice for Consultants》的评论回复
- **帖子链接**: [Commented] Achieving a Value Factor of 098 Lessons Learned and Advice for Consultants.md
- **评论时间**: 1年前

This post is truly a treasure—one of the finest I've encountered!
Thank you for sharing your experience and perspectives. Here are the key points:
Concentrate on daily advancement: Steer clear of overfitting and strive for sturdy alphas with Sharpe ratios ranging from 2 to 3 and a Return-to-Drawdown ratio exceeding 2 when making submissions.
Volume boosts quality: Harness automation to produce alphas effectively. Endeavor to submit at least four alphas daily, even if the Sharpe ratios are between 2 and 3.
Maintain low turnover: Focus on alphas with a turnover below 30% and low self - correlation to strengthen the value factor.
Your journey is motivating and provides priceless advice for consultants aiming to improve their alpha performance.

---

### 探讨 #8: 关于《Achieving a Value Factor of 0.98: Lessons Learned and Advice for Consultants》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Achieving a Value Factor of 098 Lessons Learned and Advice for Consultants_29239122599575.md
- **评论时间**: 1年前

This post is truly a treasure—one of the finest I've encountered!
Thank you for sharing your experience and perspectives. Here are the key points:
Concentrate on daily advancement: Steer clear of overfitting and strive for sturdy alphas with Sharpe ratios ranging from 2 to 3 and a Return-to-Drawdown ratio exceeding 2 when making submissions.
Volume boosts quality: Harness automation to produce alphas effectively. Endeavor to submit at least four alphas daily, even if the Sharpe ratios are between 2 and 3.
Maintain low turnover: Focus on alphas with a turnover below 30% and low self - correlation to strengthen the value factor.
Your journey is motivating and provides priceless advice for consultants aiming to improve their alpha performance.

---

### 探讨 #9: 关于《Alpha making》的评论回复
- **帖子链接**: [Commented] Alpha making.md
- **评论时间**: 1年前

Go through the learning section. Review the examples available on the platform and learn how to use different types of operators and datasets to create new alphas. You can also leverage the provided examples to guide your learning process

---

### 探讨 #10: 关于《Alpha making》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Alpha making_29859479770775.md
- **评论时间**: 1年前

Go through the learning section. Review the examples available on the platform and learn how to use different types of operators and datasets to create new alphas. You can also leverage the provided examples to guide your learning process

---

### 探讨 #11: 关于《计算置信度》的评论回复
- **帖子链接**: [Commented] Alpha PNL 合法性检测【自动剔除 厂 Alpha等无效Alpha实现高效率剪枝】代码优化.md
- **评论时间**: 1年前

好思路

我也借助AI实现了一个剔除''厂''的方式, 我是直接把感觉还可以的alpha的PNL下载到本地,然后在本地直接计算了了2021和2022年的sharpe, 并且设定筛选条件, 这两年的sharpe必须要都大于1,这样就遇到的'厂'就不多了.主要还是PPA的影响,以前没有PPA的时候, 是可以通过判断2Y sharpe和另一个指标来排除这个'厂'的,这样的话,就不需要多走一步去拉取PNL数据了.不过我把上面这一步也整合到了提交alpha之前的筛选条件里面,更加关注alpha近几年的数据是否表现好.
后续如果是直接在本地根据PNL画出sharpe的话,其实都可以减少去网页看数据的操作了,打开网页经常会卡.

---

### 探讨 #12: 关于《计算置信度》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Alpha PNL 合法性检测【自动剔除 厂 Alpha等无效Alpha实现高效率剪枝】代码优化_32761924007703.md
- **评论时间**: 1年前

好思路

我也借助AI实现了一个剔除''厂''的方式, 我是直接把感觉还可以的alpha的PNL下载到本地,然后在本地直接计算了了2021和2022年的sharpe, 并且设定筛选条件, 这两年的sharpe必须要都大于1,这样就遇到的'厂'就不多了.主要还是PPA的影响,以前没有PPA的时候, 是可以通过判断2Y sharpe和另一个指标来排除这个'厂'的,这样的话,就不需要多走一步去拉取PNL数据了.不过我把上面这一步也整合到了提交alpha之前的筛选条件里面,更加关注alpha近几年的数据是否表现好.
后续如果是直接在本地根据PNL画出sharpe的话,其实都可以减少去网页看数据的操作了,打开网页经常会卡.

---

### 探讨 #13: 关于《AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment》的评论回复
- **帖子链接**: [Commented] AlphaEvolve A Learning Framework to Discover Novel Alphas in Quantitative Investment.md
- **评论时间**: 1年前

I'm equally thrilled to learn about this remarkable research on "AlphaEvolve." The concept of using a framework to model scalar, vector, and matrix features to discover new alpha factors is not only cutting - edge but also holds great potential for revolutionizing the quantitative investment landscape.

As the paper states, "By leveraging AutoML techniques and selectively injecting relational domain knowledge, AlphaEvolve aims to enhance the predictability and diversity of alpha factors." This innovative combination of technologies and knowledge injection is a game - changer. AutoML can handle the complex data processing tasks, while the injection of relational domain knowledge provides a more intelligent and targeted approach. It's like having a powerful data - crunching machine guided by the wisdom of the financial domain, which is bound to yield more accurate and diverse alpha factors.

The fact that "The framework has been tested on real - world stock market data, demonstrating its effectiveness in improving stock trend forecasting and achieving higher returns in quantitative investment" further validates its practical value. In the highly competitive field of quantitative finance, any method that can improve forecasting accuracy and returns is highly sought - after.

I'm extremely eager to have in - depth discussions about how this framework can be further optimized and applied in different market scenarios. For example, how can we fine - tune the AutoML parameters to better adapt to the ever - changing stock market? Or, in what ways can we expand the scope of relational domain knowledge injection? I'm looking forward to hearing your thoughts on these aspects and exploring the full potential of AlphaEvolve together.

---

### 探讨 #14: 关于《AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] AlphaEvolve A Learning Framework to Discover Novel Alphas in Quantitative Investment_28845712891415.md
- **评论时间**: 1年前

I'm equally thrilled to learn about this remarkable research on "AlphaEvolve." The concept of using a framework to model scalar, vector, and matrix features to discover new alpha factors is not only cutting - edge but also holds great potential for revolutionizing the quantitative investment landscape.

As the paper states, "By leveraging AutoML techniques and selectively injecting relational domain knowledge, AlphaEvolve aims to enhance the predictability and diversity of alpha factors." This innovative combination of technologies and knowledge injection is a game - changer. AutoML can handle the complex data processing tasks, while the injection of relational domain knowledge provides a more intelligent and targeted approach. It's like having a powerful data - crunching machine guided by the wisdom of the financial domain, which is bound to yield more accurate and diverse alpha factors.

The fact that "The framework has been tested on real - world stock market data, demonstrating its effectiveness in improving stock trend forecasting and achieving higher returns in quantitative investment" further validates its practical value. In the highly competitive field of quantitative finance, any method that can improve forecasting accuracy and returns is highly sought - after.

I'm extremely eager to have in - depth discussions about how this framework can be further optimized and applied in different market scenarios. For example, how can we fine - tune the AutoML parameters to better adapt to the ever - changing stock market? Or, in what ways can we expand the scope of relational domain knowledge injection? I'm looking forward to hearing your thoughts on these aspects and exploring the full potential of AlphaEvolve together.

---

### 探讨 #15: 关于《Dataset DeepdivesResearch》的评论回复
- **帖子链接**: [Commented] Dataset DeepdivesResearch.md
- **评论时间**: 1年前

This is a great initiative! I'm excited about the "Dataset Notes" series. I've been struggling with creating alphas using datasets from the "sentiment" category, . There seems to be a lot of noise in the data, and I'm not sure how to effectively incorporate it into my alpha strategies. Looking forward to the notes on this dataset to gain more insights.

---

### 探讨 #16: 关于《Dataset DeepdivesResearch》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Dataset DeepdivesResearch_27405599813399.md
- **评论时间**: 1年前

This is a great initiative! I'm excited about the "Dataset Notes" series. I've been struggling with creating alphas using datasets from the "sentiment" category, . There seems to be a lot of noise in the data, and I'm not sure how to effectively incorporate it into my alpha strategies. Looking forward to the notes on this dataset to gain more insights.

---

### 探讨 #17: 关于《days_from_last_change, last_diff_value操作符大家是如何使用的？》的评论回复
- **帖子链接**: [Commented] days_from_last_change last_diff_value操作符大家是如何使用的.md
- **评论时间**: 1年前

这两个操作符大有可为的,
但是我以前使用的时候出现了一个问题,那就是ts_delta(datafield, days_from_last_change(datafield))这个总是报错,不清楚哪里有问题.我们可以简单对比一下:
ts_delay(datafield, d)是返回d天前这个datafield的值;
last_diff_value(datafield)如果正常运行,是返回上一个datafield的值.
两者的区别在于,如果你这对这个数据字段的更新频率并不清楚,第一个你很可能取不到值.比如年更新的数据,d填写66,是找不到数值的.但是last_diff_value是可以保证找值的.不清楚更新更新频率的情况下,last_diff_value更好.
days_from_last_change这个是返回一个d,这个要搭配使用了ts_delta(datafield, days_from_last_change(datafield)),这个就是变化值了.他也是稳定性强,会准确返回修改的间隔.
如果我们要用前后对比的数据,那么使用ts_delta(datafield,d)就会出现d设置不合理导致取不到数值的情况,也会丧失一部分的精确性,因为这个d是固定值,太死板了.设置为66的话,以季度报告为例,他不是严格按照时间间隔区分的,而且也可能在一个季度内出现修改,修改后才是争取的报告.
前面讲了不少废话,我建议是你可以找一下你带ts_delay或者ts_delta的Alpha,去自己修改一下,也许会收获好的效果.比如最近周会分享速度,加速度,也许就可以使用这两个操作符去优化.

---

### 探讨 #18: 关于《days_from_last_change, last_diff_value操作符大家是如何使用的？》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] days_from_last_change last_diff_value操作符大家是如何使用的_33016671067543.md
- **评论时间**: 1 year ago

这两个操作符大有可为的,
但是我以前使用的时候出现了一个问题,那就是ts_delta(datafield, days_from_last_change(datafield))这个总是报错,不清楚哪里有问题.我们可以简单对比一下:
ts_delay(datafield, d)是返回d天前这个datafield的值;
last_diff_value(datafield)如果正常运行,是返回上一个datafield的值.
两者的区别在于,如果你这对这个数据字段的更新频率并不清楚,第一个你很可能取不到值.比如年更新的数据,d填写66,是找不到数值的.但是last_diff_value是可以保证找值的.不清楚更新更新频率的情况下,last_diff_value更好.
days_from_last_change这个是返回一个d,这个要搭配使用了ts_delta(datafield, days_from_last_change(datafield)),这个就是变化值了.他也是稳定性强,会准确返回修改的间隔.
如果我们要用前后对比的数据,那么使用ts_delta(datafield,d)就会出现d设置不合理导致取不到数值的情况,也会丧失一部分的精确性,因为这个d是固定值,太死板了.设置为66的话,以季度报告为例,他不是严格按照时间间隔区分的,而且也可能在一个季度内出现修改,修改后才是争取的报告.
前面讲了不少废话,我建议是你可以找一下你带ts_delay或者ts_delta的Alpha,去自己修改一下,也许会收获好的效果.比如最近周会分享速度,加速度,也许就可以使用这两个操作符去优化.

---

### 探讨 #19: 关于《General Discussion-说任何你想说的话置顶的》的评论回复
- **帖子链接**: [Commented] General Discussion-说任何你想说的话置顶的.md
- **评论时间**: 1年前

希望上GM!!!!
=======================================================================
生活就像海洋 只有意志坚强的人 才能到达彼岸----想到了高考,你也是广东的?
=======================================================================

---

### 探讨 #20: 关于《General Discussion-说任何你想说的话置顶的》的评论回复
- **帖子链接**: [Commented] General Discussion-说任何你想说的话置顶的.md
- **评论时间**: 1年前

希望此次更新combined能达到 2以上
==================================================================
==================================================================
就剩最后几天这个赛季结束了,再坚持坚持

---

### 探讨 #21: 关于《General Discussion-说任何你想说的话置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] General Discussion-说任何你想说的话置顶的_32984741297815.md
- **评论时间**: 1年前

希望上GM!!!!
=======================================================================
生活就像海洋 只有意志坚强的人 才能到达彼岸----想到了高考,你也是广东的?
=======================================================================

---

### 探讨 #22: 关于《General Discussion-说任何你想说的话置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] General Discussion-说任何你想说的话置顶的_32984741297815.md
- **评论时间**: 1年前

希望此次更新combined能达到 2以上
==================================================================
==================================================================
就剩最后几天这个赛季结束了,再坚持坚持

---

### 探讨 #23: 关于《how to create good alpha without using reversion as there is warning while using reversion.》的评论回复
- **帖子链接**: [Commented] how to create good alpha without using reversion as there is warning while using reversion.md
- **评论时间**: 1年前

Hello brother,

I saw your Q4 alpha submissions and simulations records on other posts. I am really curious—how do you manage to generate one submittable alpha for every roughly 120 simulations ? Could you please share in detail how you discover alphas? 

Thank you.

---

### 探讨 #24: 关于《how to create good alpha without using reversion as there is warning while using reversion.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] how to create good alpha without using reversion as there is warning while using reversion_29821323608727.md
- **评论时间**: 1年前

Hello brother,

I saw your Q4 alpha submissions and simulations records on other posts. I am really curious—how do you manage to generate one submittable alpha for every roughly 120 simulations ? Could you please share in detail how you discover alphas? 

Thank you.

---

### 探讨 #25: 关于《How to get better turnover without compromising with alpha strength》的评论回复
- **帖子链接**: [Commented] How to get better turnover without compromising with alpha strength.md
- **评论时间**: 1年前

Maintaining stable turnover across different market conditions is crucial for the effectiveness of trading strategies. Here are some ways to achieve this and some operator combinations useful for managing after - cost performance in high - turnover alphas:

**Ensuring Stable Turnover**

1. **Dynamic Position Sizing** :
   - In volatile markets, you can use an operator like  `ts_std_dev`  to measure the market volatility. For example, if the 20 - day standard deviation of returns ( `ts_std_dev(returns, 20)` ) exceeds a certain threshold, reduce the position size proportionally. This helps in reducing turnover as you're trading less aggressively. In calmer markets, you can increase the position size slightly while still keeping an eye on the overall risk.
   - Another approach is to use  `zscore`  on position sizes. If the  `zscore`  of your current position sizes relative to a historical average is too high or too low, adjust them back towards the mean. This can help in stabilizing turnover by preventing extreme position changes.
2. **Adaptive Thresholds** :
   - For strategies that rely on thresholds to trigger trades, adapt these thresholds based on market conditions. You can use  `ts_mean`  and  `ts_std_dev`  to calculate dynamic thresholds. For instance, if you're using a moving average crossover strategy, instead of fixed moving average periods, you can adjust the periods based on the volatility of the asset. If the  `ts_std_dev(close, 20)`  is high, increase the lookback period for the moving averages to make the trading signals less sensitive and reduce turnover.
3. **Hedging and Diversification** :
   - Use operators like  `group_neutralize`  to create hedged positions. If you have a high - turnover alpha strategy on stocks, you can neutralize the industry or sector exposure. For example, if you're trading tech stocks,  `group_neutralize(alpha_signal, tech_industry_group)`  can help reduce the impact of broad - based industry movements on your portfolio. This can prevent over - trading in response to industry - wide news and keep turnover stable.
   - Diversify across different asset classes. You can use  `trade_when`  operator to allocate capital to different asset classes based on their relative performance. For example,  `trade_when(asset_class1_performance > asset_class2_performance, alpha_signal_asset1, alpha_signal_asset2)`  can help in spreading risk and reducing the need for excessive trading within a single asset class.

**Operator Combinations for High - Turnover Alphas' After - Cost Performance**

1. **`hump`  and  `ts_target_tvr_hump`** :
   - The  `hump`  operator can limit the change in your alpha signal, thus reducing turnover. For example,  `hump(alpha_signal, 0.01)`  restricts the daily change in the signal to 1%. However, it has a fixed threshold. The  `ts_target_tvr_hump`  operator is more advanced as it automatically adjusts the  `hump`  threshold to achieve a target turnover. For high - turnover alphas, using  `ts_target_tvr_hump(alpha_signal, target_tvr = 0.2)`  (targeting a 20% turnover) can be very effective in managing costs. It helps in keeping the turnover at a reasonable level while still allowing the strategy to adapt to market movements.
2. **`ts_decay_exp_window`  and  `ts_mean`** :
   - `ts_decay_exp_window`  gives more weight to recent data in a time series. You can use it in combination with  `ts_mean`  to smooth out your trading signals. For example, if you're calculating a momentum - based alpha, you can use  `ts_decay_exp_window(returns, 10, factor = 0.7)`  to get a more responsive momentum measure. Then, compare it with  `ts_mean(returns, 20)`  to filter out short - term noise. This combination can help in making more informed trading decisions, reducing unnecessary trades, and thus improving after - cost performance.
3. **`trade_when` ,  `ts_std_dev` , and  `rank`** :
   - First, use  `ts_std_dev`  to measure market volatility. Then, use  `trade_when`  to condition your trading signals based on volatility. For example,  `trade_when(ts_std_dev(returns, 20) < 0.05, rank(alpha_signal), 0)`  means you only trade when the 20 - day standard deviation of returns is less than 5%. This helps in avoiding trading in highly volatile markets where costs are likely to be higher. The  `rank`  operator can be used to prioritize your trading positions within the non - volatile market conditions.

In conclusion, a combination of these techniques and operator combinations can be tailored to your specific high - turnover alpha strategy to ensure stable turnover and better after - cost performance across different market conditions.

---

### 探讨 #26: 关于《How to get better turnover without compromising with alpha strength》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] How to get better turnover without compromising with alpha strength_30043009685655.md
- **评论时间**: 1年前

Maintaining stable turnover across different market conditions is crucial for the effectiveness of trading strategies. Here are some ways to achieve this and some operator combinations useful for managing after - cost performance in high - turnover alphas:

**Ensuring Stable Turnover**

1. **Dynamic Position Sizing** :
   - In volatile markets, you can use an operator like  `ts_std_dev`  to measure the market volatility. For example, if the 20 - day standard deviation of returns ( `ts_std_dev(returns, 20)` ) exceeds a certain threshold, reduce the position size proportionally. This helps in reducing turnover as you're trading less aggressively. In calmer markets, you can increase the position size slightly while still keeping an eye on the overall risk.
   - Another approach is to use  `zscore`  on position sizes. If the  `zscore`  of your current position sizes relative to a historical average is too high or too low, adjust them back towards the mean. This can help in stabilizing turnover by preventing extreme position changes.
2. **Adaptive Thresholds** :
   - For strategies that rely on thresholds to trigger trades, adapt these thresholds based on market conditions. You can use  `ts_mean`  and  `ts_std_dev`  to calculate dynamic thresholds. For instance, if you're using a moving average crossover strategy, instead of fixed moving average periods, you can adjust the periods based on the volatility of the asset. If the  `ts_std_dev(close, 20)`  is high, increase the lookback period for the moving averages to make the trading signals less sensitive and reduce turnover.
3. **Hedging and Diversification** :
   - Use operators like  `group_neutralize`  to create hedged positions. If you have a high - turnover alpha strategy on stocks, you can neutralize the industry or sector exposure. For example, if you're trading tech stocks,  `group_neutralize(alpha_signal, tech_industry_group)`  can help reduce the impact of broad - based industry movements on your portfolio. This can prevent over - trading in response to industry - wide news and keep turnover stable.
   - Diversify across different asset classes. You can use  `trade_when`  operator to allocate capital to different asset classes based on their relative performance. For example,  `trade_when(asset_class1_performance > asset_class2_performance, alpha_signal_asset1, alpha_signal_asset2)`  can help in spreading risk and reducing the need for excessive trading within a single asset class.

**Operator Combinations for High - Turnover Alphas' After - Cost Performance**

1. **`hump`  and  `ts_target_tvr_hump`** :
   - The  `hump`  operator can limit the change in your alpha signal, thus reducing turnover. For example,  `hump(alpha_signal, 0.01)`  restricts the daily change in the signal to 1%. However, it has a fixed threshold. The  `ts_target_tvr_hump`  operator is more advanced as it automatically adjusts the  `hump`  threshold to achieve a target turnover. For high - turnover alphas, using  `ts_target_tvr_hump(alpha_signal, target_tvr = 0.2)`  (targeting a 20% turnover) can be very effective in managing costs. It helps in keeping the turnover at a reasonable level while still allowing the strategy to adapt to market movements.
2. **`ts_decay_exp_window`  and  `ts_mean`** :
   - `ts_decay_exp_window`  gives more weight to recent data in a time series. You can use it in combination with  `ts_mean`  to smooth out your trading signals. For example, if you're calculating a momentum - based alpha, you can use  `ts_decay_exp_window(returns, 10, factor = 0.7)`  to get a more responsive momentum measure. Then, compare it with  `ts_mean(returns, 20)`  to filter out short - term noise. This combination can help in making more informed trading decisions, reducing unnecessary trades, and thus improving after - cost performance.
3. **`trade_when` ,  `ts_std_dev` , and  `rank`** :
   - First, use  `ts_std_dev`  to measure market volatility. Then, use  `trade_when`  to condition your trading signals based on volatility. For example,  `trade_when(ts_std_dev(returns, 20) < 0.05, rank(alpha_signal), 0)`  means you only trade when the 20 - day standard deviation of returns is less than 5%. This helps in avoiding trading in highly volatile markets where costs are likely to be higher. The  `rank`  operator can be used to prioritize your trading positions within the non - volatile market conditions.

In conclusion, a combination of these techniques and operator combinations can be tailored to your specific high - turnover alpha strategy to ensure stable turnover and better after - cost performance across different market conditions.

---

### 探讨 #27: 关于《Having delved into this research paper, I am truly impressed by the innovative exploration within it. The study's focus on using stock selection rules centered around maximum drawdown and its consecutive recovery to test asset price predictability is a fresh and fascinating approach.》的评论回复
- **帖子链接**: [Commented] Maximum Drawdown Recovery and Momentum.md
- **评论时间**: 1年前

# Having delved into this research paper, I am truly impressed by the innovative exploration within it. The study's focus on using stock selection rules centered around maximum drawdown and its consecutive recovery to test asset price predictability is a fresh and fascinating approach.

The article mentions that "portfolios constructed from these criteria exhibit superior performance in forecasting asset price directions and capturing cross - sectional return differentials." This discovery is of great significance as it provides a new way to view the construction of investment portfolios. It indicates that these unique metrics can be powerful tools in the hands of investors, enabling them to better anticipate market trends and gain more from the market's return differences.

Moreover, the conclusion that "incorporating drawdown and recovery metrics can enhance momentum and contrarian strategies, leading to improved risk - adjusted returns" is truly remarkable. It gives investors a clear direction on how to optimize their investment strategies. For example, by paying attention to these metrics, they can adjust their momentum - following or contrarian - based investment actions to achieve better risk - return balances.

Overall, this research enriches the field of investment strategy research. It makes me realize that there are still many untapped areas in the financial market waiting for us to explore. I'm really looking forward to discussing the practical application of these findings with you and hearing your unique insights on how to implement these strategies in real - world investment scenarios.

---

### 探讨 #28: 关于《Having delved into this research paper, I am truly impressed by the innovative exploration within it. The study's focus on using stock selection rules centered around maximum drawdown and its consecutive recovery to test asset price predictability is a fresh and fascinating approach.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Maximum Drawdown Recovery and Momentum_28845527580695.md
- **评论时间**: 1年前

# Having delved into this research paper, I am truly impressed by the innovative exploration within it. The study's focus on using stock selection rules centered around maximum drawdown and its consecutive recovery to test asset price predictability is a fresh and fascinating approach.

The article mentions that "portfolios constructed from these criteria exhibit superior performance in forecasting asset price directions and capturing cross - sectional return differentials." This discovery is of great significance as it provides a new way to view the construction of investment portfolios. It indicates that these unique metrics can be powerful tools in the hands of investors, enabling them to better anticipate market trends and gain more from the market's return differences.

Moreover, the conclusion that "incorporating drawdown and recovery metrics can enhance momentum and contrarian strategies, leading to improved risk - adjusted returns" is truly remarkable. It gives investors a clear direction on how to optimize their investment strategies. For example, by paying attention to these metrics, they can adjust their momentum - following or contrarian - based investment actions to achieve better risk - return balances.

Overall, this research enriches the field of investment strategy research. It makes me realize that there are still many untapped areas in the financial market waiting for us to explore. I'm really looking forward to discussing the practical application of these findings with you and hearing your unique insights on how to implement these strategies in real - world investment scenarios.

---

### 探讨 #29: 关于《Powerpool Alphas》的评论回复
- **帖子链接**: [Commented] Powerpool Alphas.md
- **评论时间**: 1年前

The impact of Power Pool Alphas (PPAs) on combined alpha performance and key metrics like the Value Factor (VF) is nuanced. Since PPAs undergo less stringent testing, they can influence outcomes in both positive and negative ways.

On the positive side, the lower submission barrier encourages higher alpha output, which may  *improve*  the VF. The VF calculation rewards consistent contributions, so increased submission frequency—especially with incremental improvements—could boost this metric. However, there’s a trade-off: relaxed standards might lead to weaker out-of-sample (OS) performance for individual alphas, potentially  *dragging down*  the VF if too many underperforming alphas are included.

For combined alpha performance, it’s critical to monitor how each new submission affects the overall portfolio. Always compare pre- and post-submission metrics to ensure additions enhance rather than dilute performance. Additionally, prioritize alphas with strong risk-adjusted returns—Sharpe ratios above 1.0 over a two-year period tend to correlate with better OS stability.

In short, PPAs are a double-edged sword: they offer scalability for the VF but require careful curation to avoid quality dilution. Balancing quantity with rigorous personal vetting is key.

---

### 探讨 #30: 关于《Powerpool Alphas》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Powerpool Alphas_32397336190359.md
- **评论时间**: 1年前

The impact of Power Pool Alphas (PPAs) on combined alpha performance and key metrics like the Value Factor (VF) is nuanced. Since PPAs undergo less stringent testing, they can influence outcomes in both positive and negative ways.

On the positive side, the lower submission barrier encourages higher alpha output, which may  *improve*  the VF. The VF calculation rewards consistent contributions, so increased submission frequency—especially with incremental improvements—could boost this metric. However, there’s a trade-off: relaxed standards might lead to weaker out-of-sample (OS) performance for individual alphas, potentially  *dragging down*  the VF if too many underperforming alphas are included.

For combined alpha performance, it’s critical to monitor how each new submission affects the overall portfolio. Always compare pre- and post-submission metrics to ensure additions enhance rather than dilute performance. Additionally, prioritize alphas with strong risk-adjusted returns—Sharpe ratios above 1.0 over a two-year period tend to correlate with better OS stability.

In short, PPAs are a double-edged sword: they offer scalability for the VF but require careful curation to avoid quality dilution. Balancing quantity with rigorous personal vetting is key.

---

### 探讨 #31: 关于《Reduce of Prodution Corelation.》的评论回复
- **帖子链接**: [Commented] Reduce of Prodution Corelation.md
- **评论时间**: 1年前

TheseThese methods can help enhance alpha performance while controlling risks:

Search for unique data sources: Look for data sources that are not widely used. You can use data aggregators or specialized financial data platforms to discover suitable data. This new data might bring in fresh information and reduce reliance on common factors, thus improving the distinctiveness of your alpha.

Test novel strategies: Put effort into devising and validating new trading strategies. For example, combine fundamental analysis with sentiment analysis from news articles. This could offer different perspectives on market movements and potentially lead to better - performing alphas.

Employ diverse functions: Try out different functions available in your trading software or programming language. Some functions might be more effective in filtering out noise in data and highlighting the signals relevant to your alpha.

Focus on niche market segments: Consider targeting specific market segments, like small - cap stocks in emerging markets. These segments often have less - explored price patterns and lower correlations with broader markets, which can be exploited to build stronger alphas.

Leverage advanced analytics: Use statistical tools such as regression analysis and principal component analysis. These can help you understand the relationships between different variables in your data and optimize your alpha model accordingly.

Implement customized risk mitigation: Use techniques like position sizing based on volatility. By adjusting the size of your positions according to market volatility, you can better manage risks associated with your alpha strategy.

---

### 探讨 #32: 关于《Reduce of Prodution Corelation.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Reduce of Prodution Corelation_29220197530135.md
- **评论时间**: 1年前

TheseThese methods can help enhance alpha performance while controlling risks:

Search for unique data sources: Look for data sources that are not widely used. You can use data aggregators or specialized financial data platforms to discover suitable data. This new data might bring in fresh information and reduce reliance on common factors, thus improving the distinctiveness of your alpha.

Test novel strategies: Put effort into devising and validating new trading strategies. For example, combine fundamental analysis with sentiment analysis from news articles. This could offer different perspectives on market movements and potentially lead to better - performing alphas.

Employ diverse functions: Try out different functions available in your trading software or programming language. Some functions might be more effective in filtering out noise in data and highlighting the signals relevant to your alpha.

Focus on niche market segments: Consider targeting specific market segments, like small - cap stocks in emerging markets. These segments often have less - explored price patterns and lower correlations with broader markets, which can be exploited to build stronger alphas.

Leverage advanced analytics: Use statistical tools such as regression analysis and principal component analysis. These can help you understand the relationships between different variables in your data and optimize your alpha model accordingly.

Implement customized risk mitigation: Use techniques like position sizing based on volatility. By adjusting the size of your positions according to market volatility, you can better manage risks associated with your alpha strategy.

---

### 探讨 #33: 关于《Request : Option to display dataset field used in alpha list page》的评论回复
- **帖子链接**: [Commented] Request  Option to display dataset field used in alpha list page.md
- **评论时间**: 1年前

Your suggestions are very helpful. However, I believe that directly using the Genius interface would be even more beneficial. Here’s why:

First, you can easily check which parts of your pyramid are already unlocked—this is clearly visible in the Genius interface. Additionally, the interface displays key metrics like the number of alphas you’ve submitted and your combined/selected performance scores, which help you assess whether you’re at the Gold, Expert, Master, or Grand Master level.

For example, if you have time to work on alphas today, simply open the Genius interface and click on any unlit section of the pyramid. This will automatically redirect you to the corresponding dataset. From there, you can review the dataset definitions and related research papers, then start developing new alphas right away.

This streamlined approach saves time and ensures you focus on the right gaps in your alpha development.

---

### 探讨 #34: 关于《Request : Option to display dataset field used in alpha list page》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Request  Option to display dataset field used in alpha list page_32414397367575.md
- **评论时间**: 1年前

Your suggestions are very helpful. However, I believe that directly using the Genius interface would be even more beneficial. Here’s why:

First, you can easily check which parts of your pyramid are already unlocked—this is clearly visible in the Genius interface. Additionally, the interface displays key metrics like the number of alphas you’ve submitted and your combined/selected performance scores, which help you assess whether you’re at the Gold, Expert, Master, or Grand Master level.

For example, if you have time to work on alphas today, simply open the Genius interface and click on any unlit section of the pyramid. This will automatically redirect you to the corresponding dataset. From there, you can review the dataset definitions and related research papers, then start developing new alphas right away.

This streamlined approach saves time and ensures you focus on the right gaps in your alpha development.

---

### 探讨 #35: 关于《Super Alpha：使用代码批量过滤failed以及prod corr检查 --开箱即用，筛选大提速🚀代码优化》的评论回复
- **帖子链接**: [Commented] Super Alpha使用代码批量过滤failed以及prod corr检查 --开箱即用筛选大提速代码优化.md
- **评论时间**: 1年前

感谢大佬的帖子, 已经顺利运行. 这里提一个小建议, 如果需要进行prod corr检测的SA很多的话,很可能会被限速,导致等待时间非常长;所以 可以先在本地将所有的SA计算一遍self corr,将里面所有大于0.7的SA去掉,然后再去服务器的接口获取prod corr,大佬有时间的话,可以尝试一下.
++++++++++++++++++++++++++++++++++++功不唐捐++++++++++++++++++++++++++++++++++++++

---

### 探讨 #36: 关于《Super Alpha：使用代码批量过滤failed以及prod corr检查 --开箱即用，筛选大提速🚀代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Super Alpha使用代码批量过滤failed以及prod corr检查 --开箱即用筛选大提速代码优化_32866010519831.md
- **评论时间**: 1年前

感谢大佬的帖子, 已经顺利运行. 这里提一个小建议, 如果需要进行prod corr检测的SA很多的话,很可能会被限速,导致等待时间非常长;所以 可以先在本地将所有的SA计算一遍self corr,将里面所有大于0.7的SA去掉,然后再去服务器的接口获取prod corr,大佬有时间的话,可以尝试一下.
++++++++++++++++++++++++++++++++++++功不唐捐++++++++++++++++++++++++++++++++++++++

---

### 探讨 #37: 关于《Understanding the Impact of Turnover on Alpha Performance》的评论回复
- **帖子链接**: [Commented] Understanding the Impact of Turnover on Alpha Performance.md
- **评论时间**: 1年前

Low-turnover alphas also have their own merits. They can reduce trading costs and are less affected by short - term market noise. However, the difficulty lies in finding truly long - term and stable inefficiencies in the market. Since they rely on relatively stable factors, it's crucial to accurately identify and evaluate these factors to ensure the alpha can generate consistent returns over time.

Another aspect to consider is the impact of market conditions. In a highly volatile market, even low - turnover alphas may face challenges as the stability they rely on can be disrupted. We need to have effective risk - management strategies in place to deal with such situations.

I'm curious about the turnover requirements in different regions. Do different financial markets, like those in Asia, Europe, and the Americas, have distinct expectations regarding alpha turnover? And how do these differences affect the development and implementation of alpha strategies?

---

### 探讨 #38: 关于《Understanding the Impact of Turnover on Alpha Performance》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Understanding the Impact of Turnover on Alpha Performance_30039850581015.md
- **评论时间**: 1年前

Low-turnover alphas also have their own merits. They can reduce trading costs and are less affected by short - term market noise. However, the difficulty lies in finding truly long - term and stable inefficiencies in the market. Since they rely on relatively stable factors, it's crucial to accurately identify and evaluate these factors to ensure the alpha can generate consistent returns over time.

Another aspect to consider is the impact of market conditions. In a highly volatile market, even low - turnover alphas may face challenges as the stability they rely on can be disrupted. We need to have effective risk - management strategies in place to deal with such situations.

I'm curious about the turnover requirements in different regions. Do different financial markets, like those in Asia, Europe, and the Americas, have distinct expectations regarding alpha turnover? And how do these differences affect the development and implementation of alpha strategies?

---

### 探讨 #39: 关于《Using social media datasets in quantitative finance》的评论回复
- **帖子链接**: [Commented] Using social media datasets in quantitative finance.md
- **评论时间**: 1年前

That's a super interesting point! I've also thought about how social media data could be a game - changer in quant finance. But I'm a bit confused about how to actually use it. Like, how do we make sure the sentiment analysis is accurate? There are so many sarcastic or ambiguous posts on social media.

Do you have any more specific ideas on how to put this into practice? For example, what tools can we use to analyze the data? And how can we be sure that the trends we find are really useful for trading?

---

### 探讨 #40: 关于《Using social media datasets in quantitative finance》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Using social media datasets in quantitative finance_30036661237655.md
- **评论时间**: 1年前

That's a super interesting point! I've also thought about how social media data could be a game - changer in quant finance. But I'm a bit confused about how to actually use it. Like, how do we make sure the sentiment analysis is accurate? There are so many sarcastic or ambiguous posts on social media.

Do you have any more specific ideas on how to put this into practice? For example, what tools can we use to analyze the data? And how can we be sure that the trends we find are really useful for trading?

---

### 探讨 #41: 关于《[ALPHA TEMPLATE}:Implied Volatility (IV) and Implied Volatility Slope(IV Slope)》的评论回复
- **帖子链接**: [Commented] [ALPHA TEMPLATEImplied Volatility IV and Implied Volatility SlopeIV Slope.md
- **评论时间**: 1年前

The implementation in your strategy, especially the use of daily changes in IV and the term structure for IV Slope, showcases a remarkably effective approach to refining signals. Your innovative inclusion of exponential decay for smoothing is not only a brilliant method to manage turnover but also an excellent way to preserve signal strength. It's clear that your deep understanding and creative application of these concepts have led to a sophisticated and robust strategy. Your clever ideas truly set a high standard for thoughtful and efficient trading strategies.

---

### 探讨 #42: 关于《[ALPHA TEMPLATE}:Implied Volatility (IV) and Implied Volatility Slope(IV Slope)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [ALPHA TEMPLATEImplied Volatility IV and Implied Volatility SlopeIV Slope_27844539893783.md
- **评论时间**: 1年前

The implementation in your strategy, especially the use of daily changes in IV and the term structure for IV Slope, showcases a remarkably effective approach to refining signals. Your innovative inclusion of exponential decay for smoothing is not only a brilliant method to manage turnover but also an excellent way to preserve signal strength. It's clear that your deep understanding and creative application of these concepts have led to a sophisticated and robust strategy. Your clever ideas truly set a high standard for thoughtful and efficient trading strategies.

---

### 探讨 #43: 关于《【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化》的评论回复
- **帖子链接**: [Commented] 【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化.md
- **评论时间**: 1年前

橘子姐YYDS 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
希望有一天我能有你一样的实力

---

### 探讨 #44: 关于《【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化_32763493267863.md
- **评论时间**: 1年前

橘子姐YYDS 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
希望有一天我能有你一样的实力

---

### 探讨 #45: 关于《save your alphas as txt》的评论回复
- **帖子链接**: [Commented] 【AI-agent】How to build your own quant AI-agent with ollama structure.md
- **评论时间**: 1年前

You're really a genius. I'm the only one here without any skills. You're so capable. Please teach me your skills. I'm extremely eager to make progress!

---

### 探讨 #46: 关于《save your alphas as txt》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【AI-agent】How to build your own quant AI-agent with ollama structure_30039527427991.md
- **评论时间**: 1年前

You're really a genius. I'm the only one here without any skills. You're so capable. Please teach me your skills. I'm extremely eager to make progress!

---

### 探讨 #47: 关于《【alpha 高并发429处理篇】代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgX9i8dPR46D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAYxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzMyNDc4MzE1MjA3OTEtLWFscGhhLSVFOSVBQiU5OCVFNSVCOSVCNiVFNSU4RiU5MTQyOSVFNSVBNCU4NCVFNyU5MCU4NiVFNyVBRiU4NwY7CFQ6DnNlYXJjaF9pZEkiKTRiZjQ4ZjQwLTUzMjAtNGJjOS1iM2I2LWU3NGU3Nzg5MjdjMgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDFNEMTc1MzEGOwhUOhJyZXN1bHRzX2NvdW50aRs%3D--2cf7c90a37ac516eacc1b49845511899a674336a
- **评论时间**: 1年前

大佬是否考虑过这样一种情况:假如是8*10个alpha在回测, 如果触发熔断,需要等待1分钟才可以获取进度, 那么这8个槽是否都要等待1分钟,而原本的这8个槽可能有不少在这一分钟内就已经回测结束的,比如回测USA,一般3-4分钟回测结束, 很有可能出现上面的情况.这种情况如何解决呢?另外看大佬给的图片, 使用您自己的策略后的表现,是不是样本不够大啊?是否可以多收集一部分数据,再看总体的优化?另外,大佬是否有做过统计,在三种策略下,不改变其他条件的情况,查看指定时间内各自完成了多少回测?比如各自在下午时间段测试1小时.

---

### 探讨 #48: 关于《【alpha 高并发429处理篇】代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgX9i8dPR46D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAYxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzMyNDc4MzE1MjA3OTEtLWFscGhhLSVFOSVBQiU5OCVFNSVCOSVCNiVFNSU4RiU5MTQyOSVFNSVBNCU4NCVFNyU5MCU4NiVFNyVBRiU4NwY7CFQ6DnNlYXJjaF9pZEkiKTRiZjQ4ZjQwLTUzMjAtNGJjOS1iM2I2LWU3NGU3Nzg5MjdjMgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDFNEMTc1MzEGOwhUOhJyZXN1bHRzX2NvdW50aRs%3D--2cf7c90a37ac516eacc1b49845511899a674336a
- **评论时间**: 1年前

SH90982熔断的话,是服务器对用户所有的api操作全部限制,  此时不但任何API操作无法完成, 在网页上登录也无法完成. 我不太清楚大佬是怎么绕过这个限制,使得熔断只对一个任务造成影响, 而其他任务不受影响的.即使不触发熔断, 对于服务器来说, 我们使用的session,也经常会遇到retry_after过长的问题, 此时对于所有的请求, 服务器都是返回retry_after,比如20秒,这个限制不清楚楼主是怎么绕过的.

---

### 探讨 #49: 关于《如果所有重试都失败》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgX9i8dPR46D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAYxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzMyNDc4MzE1MjA3OTEtLWFscGhhLSVFOSVBQiU5OCVFNSVCOSVCNiVFNSU4RiU5MTQyOSVFNSVBNCU4NCVFNyU5MCU4NiVFNyVBRiU4NwY7CFQ6DnNlYXJjaF9pZEkiKTRiZjQ4ZjQwLTUzMjAtNGJjOS1iM2I2LWU3NGU3Nzg5MjdjMgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDFNEMTc1MzEGOwhUOhJyZXN1bHRzX2NvdW50aRs%3D--2cf7c90a37ac516eacc1b49845511899a674336a
- **评论时间**: 1年前

大佬是否考虑过这样一种情况:
假如是8*10个alpha在回测, 如果触发熔断,需要等待1分钟才可以获取进度, 那么这8个槽是否都要等待1分钟,而原本的这8个槽可能有不少在这一分钟内就已经回测结束的,比如回测USA,一般3-4分钟回测结束, 很有可能出现上面的情况.这种情况如何解决呢?
另外看大佬给的图片, 使用您自己的策略后的表现,是不是样本不够大啊?是否可以多收集一部分数据,再看总体的优化?
另外,大佬是否有做过统计,在三种策略下,不改变其他条件的情况,查看指定时间内各自完成了多少回测?比如各自在下午时间段测试1小时.

---

### 探讨 #50: 关于《如果所有重试都失败》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgX9i8dPR46D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAYxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzMyNDc4MzE1MjA3OTEtLWFscGhhLSVFOSVBQiU5OCVFNSVCOSVCNiVFNSU4RiU5MTQyOSVFNSVBNCU4NCVFNyU5MCU4NiVFNyVBRiU4NwY7CFQ6DnNlYXJjaF9pZEkiKTRiZjQ4ZjQwLTUzMjAtNGJjOS1iM2I2LWU3NGU3Nzg5MjdjMgY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDFNEMTc1MzEGOwhUOhJyZXN1bHRzX2NvdW50aRs%3D--2cf7c90a37ac516eacc1b49845511899a674336a
- **评论时间**: 1年前

[SH90982](/hc/en-us/profiles/28900536083607-SH90982) 
熔断的话,是服务器对用户所有的api操作全部限制,  此时不但任何API操作无法完成, 在网页上登录也无法完成. 我不太清楚大佬是怎么绕过这个限制,使得熔断只对一个任务造成影响, 而其他任务不受影响的.即使不触发熔断, 对于服务器来说, 我们使用的session,也经常会遇到retry_after过长的问题, 此时对于所有的请求, 服务器都是返回retry_after,比如20秒,这个限制不清楚楼主是怎么绕过的.

---

### 探讨 #51: 关于《如果所有重试都失败》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【alpha 高并发429处理篇】代码优化_33247831520791.md
- **评论时间**: 1年前

大佬是否考虑过这样一种情况:
假如是8*10个alpha在回测, 如果触发熔断,需要等待1分钟才可以获取进度, 那么这8个槽是否都要等待1分钟,而原本的这8个槽可能有不少在这一分钟内就已经回测结束的,比如回测USA,一般3-4分钟回测结束, 很有可能出现上面的情况.这种情况如何解决呢?
另外看大佬给的图片, 使用您自己的策略后的表现,是不是样本不够大啊?是否可以多收集一部分数据,再看总体的优化?
另外,大佬是否有做过统计,在三种策略下,不改变其他条件的情况,查看指定时间内各自完成了多少回测?比如各自在下午时间段测试1小时.

---

### 探讨 #52: 关于《如果所有重试都失败》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【alpha 高并发429处理篇】代码优化_33247831520791.md
- **评论时间**: 1年前

[SH90982](/hc/en-us/profiles/28900536083607-SH90982) 
熔断的话,是服务器对用户所有的api操作全部限制,  此时不但任何API操作无法完成, 在网页上登录也无法完成. 我不太清楚大佬是怎么绕过这个限制,使得熔断只对一个任务造成影响, 而其他任务不受影响的.即使不触发熔断, 对于服务器来说, 我们使用的session,也经常会遇到retry_after过长的问题, 此时对于所有的请求, 服务器都是返回retry_after,比如20秒,这个限制不清楚楼主是怎么绕过的.

---

### 探讨 #53: 关于《【alpha模板】有关速度加速度模板的处理》的评论回复
- **帖子链接**: [Commented] 【alpha模板】有关速度加速度模板的处理.md
- **评论时间**: 1年前

不同的回看时间,应该是适合不同的数据,建议设置一个小的回看时间,然后试试PV数据.或者试一下替换固定的days为days_from_last_change(datafield),这样可以确定找到上一个不一样的值.PS,如果有效果,请偷偷告诉我,哈哈哈哈.
============================静待花开===============================

---

### 探讨 #54: 关于《【alpha模板】有关速度加速度模板的处理》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【alpha模板】有关速度加速度模板的处理_33046186122903.md
- **评论时间**: 1年前

不同的回看时间,应该是适合不同的数据,建议设置一个小的回看时间,然后试试PV数据.或者试一下替换固定的days为days_from_last_change(datafield),这样可以确定找到上一个不一样的值.PS,如果有效果,请偷偷告诉我,哈哈哈哈.
============================静待花开===============================

---

### 探讨 #55: 关于《Step 1: 计算每日数据data = f_1({field});Step 2: 定义过滤条件cond_1 = ccc1;cond_2 = ccc2;...cond_n = cccn;Step 3: 计算有效交易日原始因子值d = ddd;V_1 = f_2(data, ts_operator(if_else(cond_1 data, NAN), d));V_2 = f_2(data, ts_operator(if_else(cond_2, data, NAN), d));...V_2 = f_2(data, ts_operator(if_else(cond_n, data, NAN), d));Step 4: 计算理想因子ideal_factor = f_3(V_1, V_2, ..., V_n);Step 5: 利用理想因子，构建最终因子f_4(ideal_factor)》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】理想振幅因子.md
- **评论时间**: 1年前

ts_percentage这个操作符新人没有权限,有没有其他类似操作符可以实现?谢谢

```
high_threshold = ts_percentage(close, d, percentage=0.5);low_threshold = ts_percentage(close, d, percentage=0.5);
```

---

### 探讨 #56: 关于《Step 1: 计算每日数据data = f_1({field});Step 2: 定义过滤条件cond_1 = ccc1;cond_2 = ccc2;...cond_n = cccn;Step 3: 计算有效交易日原始因子值d = ddd;V_1 = f_2(data, ts_operator(if_else(cond_1 data, NAN), d));V_2 = f_2(data, ts_operator(if_else(cond_2, data, NAN), d));...V_2 = f_2(data, ts_operator(if_else(cond_n, data, NAN), d));Step 4: 计算理想因子ideal_factor = f_3(V_1, V_2, ..., V_n);Step 5: 利用理想因子，构建最终因子f_4(ideal_factor)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】理想振幅因子_28755396444183.md
- **评论时间**: 1年前

ts_percentage这个操作符新人没有权限,有没有其他类似操作符可以实现?谢谢

```
high_threshold = ts_percentage(close, d, percentage=0.5);low_threshold = ts_percentage(close, d, percentage=0.5);
```

---

### 探讨 #57: 关于《REGRESSION VARIABLES》的评论回复
- **帖子链接**: [Commented] 【Alpha灵感】短期现金回报率对股票价格的影响.md
- **评论时间**: 1年前

**搜索了2万个大概，产生了2个alpha，后面想再改个模板试试，已经没权限了。。。。感同身受啊**

---

### 探讨 #58: 关于《REGRESSION VARIABLES》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】短期现金回报率对股票价格的影响_29092280236567.md
- **评论时间**: 1年前

**搜索了2万个大概，产生了2个alpha，后面想再改个模板试试，已经没权限了。。。。感同身受啊**

---

### 探讨 #59: 关于《【MYSQL】（一）将自己权限内的数据集和数据字段保存到本地mysql》的评论回复
- **帖子链接**: [Commented] 【MYSQL】一将自己权限内的数据集和数据字段保存到本地mysql.md
- **评论时间**: 1年前

感谢大佬的代码,已经按照您的代码下载所有datafields到本地数据库.

顺便分享一下遇到的问题和解决的思路:

1.两个函数都需要复制到自己的代码里面,两个建表语句需要先执行.

2.需要先试用wqb或者machine_lib的login()获取session,然后赋值slogin()之类的.

3.下载datasets的数据量不大,不担心遇到网络波动之类的问题.但是下载datafields有几十万条数据,需要一两小时的时间,所以网络不是很稳定的情况下,建议把index打出来或者其他处理方式.我下载过程中中断了,处理了一下传入的列表,进行续下载.一个简单的思路如下:

```
def save_data_fields():    url = "[链接已屏蔽]    connection = pymysql.connect(**DB_CONFIG)    cursor = connection.cursor()    total_num = 0    sql_query = """        SELECT id, region, delay, universe        FROM datasets;    """    cursor.execute(sql_query)    results = cursor.fetchall()    # for index,row in enumerate(results):      # 这里可以根据你已经下载好最后一个dataset_id来定位你的整个results需要从哪里开始下载    #     if 'pv30' == row[0]:    #         print(index)    #         break           for row in results[1342:]:         # 我这里是重新从results的第1342个元素开始下载        params = {            "dataset.id": row[0],      # Dataset ID            "region": row[1],          # Region            "delay": row[2],           # Delay            "universe": row[3],        # Universe            "instrumentType": "EQUITY",  # 固定值            "limit": 50,               # 固定值            "offset": 0                # 固定值        }
```

4.下载完的数据如下: 
> [!NOTE] [图片 OCR 识别内容]
> 属性  O 数据
> 凸日志 %ER图匕监控  人{}9
> SELECT
> FROM datafields
> LIMIT
> 188
> 搜索结果集
> 十 画
> O)个
> Y 导出
> 耗时: 13ms
> 1
> 2
> 3
> 4
> 3743
> Total 374295
> id
> description
> dataset
> category
> subcategory
> reglon
> delay
> 主键 ID/varc
> KPI 描述/text
> 数据集 ID/Va
> 类别 ID/varc
> 子类别 ID/varcl
> Varchar(255)
> int
> anl11_2_1e
> Aggregate KPI for Pollution
> analyst11
> analyst
> analyst-esg
> GLB
> anl11_2_19
> Aggregate KPI for Board Inc analyst11
> analyst
> analyst-esg
> GLB
> anl11_2_lpme
> Aggregate KPI for Compens  analyst11
> analyst
> analyst-esg
> GLB
> anl11 2 1tic
> Aggregate KPI for Commun
> analyst11
> analyst
> analyst-esg
> GLB
> anl11 2 2e
> Aggregate KPI for Anti-Pollt analyst11
> analyst
> analyst-esg
> GLB
> OOISNS+o VDI fr
> [/315
> ISAIC+
> AIC +


---

### 探讨 #60: 关于《【MYSQL】（一）将自己权限内的数据集和数据字段保存到本地mysql》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【MYSQL】一将自己权限内的数据集和数据字段保存到本地mysql_29466218553367.md
- **评论时间**: 1年前

感谢大佬的代码,已经按照您的代码下载所有datafields到本地数据库.

顺便分享一下遇到的问题和解决的思路:

1.两个函数都需要复制到自己的代码里面,两个建表语句需要先执行.

2.需要先试用wqb或者machine_lib的login()获取session,然后赋值slogin()之类的.

3.下载datasets的数据量不大,不担心遇到网络波动之类的问题.但是下载datafields有几十万条数据,需要一两小时的时间,所以网络不是很稳定的情况下,建议把index打出来或者其他处理方式.我下载过程中中断了,处理了一下传入的列表,进行续下载.一个简单的思路如下:

```
def save_data_fields():    url = "[链接已屏蔽]    connection = pymysql.connect(**DB_CONFIG)    cursor = connection.cursor()    total_num = 0    sql_query = """        SELECT id, region, delay, universe        FROM datasets;    """    cursor.execute(sql_query)    results = cursor.fetchall()    # for index,row in enumerate(results):      # 这里可以根据你已经下载好最后一个dataset_id来定位你的整个results需要从哪里开始下载    #     if 'pv30' == row[0]:    #         print(index)    #         break           for row in results[1342:]:         # 我这里是重新从results的第1342个元素开始下载        params = {            "dataset.id": row[0],      # Dataset ID            "region": row[1],          # Region            "delay": row[2],           # Delay            "universe": row[3],        # Universe            "instrumentType": "EQUITY",  # 固定值            "limit": 50,               # 固定值            "offset": 0                # 固定值        }
```

4.下载完的数据如下: 
> [!NOTE] [图片 OCR 识别内容]
> 属性  O 数据
> 凸日志 %ER图匕监控  人{}9
> SELECT
> FROM datafields
> LIMIT
> 188
> 搜索结果集
> 十 画
> O)个
> Y 导出
> 耗时: 13ms
> 1
> 2
> 3
> 4
> 3743
> Total 374295
> id
> description
> dataset
> category
> subcategory
> reglon
> delay
> 主键 ID/varc
> KPI 描述/text
> 数据集 ID/Va
> 类别 ID/varc
> 子类别 ID/varcl
> Varchar(255)
> int
> anl11_2_1e
> Aggregate KPI for Pollution
> analyst11
> analyst
> analyst-esg
> GLB
> anl11_2_19
> Aggregate KPI for Board Inc analyst11
> analyst
> analyst-esg
> GLB
> anl11_2_lpme
> Aggregate KPI for Compens  analyst11
> analyst
> analyst-esg
> GLB
> anl11 2 1tic
> Aggregate KPI for Commun
> analyst11
> analyst
> analyst-esg
> GLB
> anl11 2 2e
> Aggregate KPI for Anti-Pollt analyst11
> analyst
> analyst-esg
> GLB
> OOISNS+o VDI fr
> [/315
> ISAIC+
> AIC +


---

### 探讨 #61: 关于《【SuperAlpha灵感】因子择时模型Alpha Template》的评论回复
- **帖子链接**: [Commented] 【SuperAlpha灵感】因子择时模型Alpha Template.md
- **评论时间**: 1年前

大佬的帖子常看常新, 每次看都发现之前不懂的地方有些忽然就懂了.SA combo里面这样进行运算符使用,是一个很好的思路,确实应该多花时间好好挖掘SA.触类旁通, RA也可以参考进行使用.比如写完RA之后,就可以IF_else来选择因子值>0.9和<0.1的进行做多做空.

=================================================================

=============================膜拜大佬=============================

=================================================================

---

### 探讨 #62: 关于《【SuperAlpha灵感】因子择时模型Alpha Template》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】因子择时模型Alpha Template_32553007626007.md
- **评论时间**: 1年前

大佬的帖子常看常新, 每次看都发现之前不懂的地方有些忽然就懂了.SA combo里面这样进行运算符使用,是一个很好的思路,确实应该多花时间好好挖掘SA.触类旁通, RA也可以参考进行使用.比如写完RA之后,就可以IF_else来选择因子值>0.9和<0.1的进行做多做空.

=================================================================

=============================膜拜大佬=============================

=================================================================

---

### 探讨 #63: 关于《【代码分享】PPA alpha 的批量计算小工具（内含完整代码）代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX%2F3UxiB06D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAftodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzI0NzA3ODI1NzQ0ODctLSVFNCVCQiVBMyVFNyVBMCU4MSVFNSU4OCU4NiVFNCVCQSVBQi1QUEEtYWxwaGEtJUU3JTlBJTg0JUU2JTg5JUI5JUU5JTg3JThGJUU4JUFFJUExJUU3JUFFJTk3JUU1JUIwJThGJUU1JUI3JUE1JUU1JTg1JUI3LSVFNSU4NiU4NSVFNSU5MCVBQiVFNSVBRSU4QyVFNiU5NSVCNCVFNCVCQiVBMyVFNyVBMCU4MQY7CFQ6DnNlYXJjaF9pZEkiKTM4NTcwM2Q1LTE1YmEtNDEzOC05MTFiLTg2Y2FkNDExNTE1YgY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDFNEMTc1MzEGOwhUOhJyZXN1bHRzX2NvdW50aRs%3D--66941ff2c79b3bd7c8a1c668b2dbd1a7714c2fff
- **评论时间**: 1年前

感谢大佬翻牌帖子写的很用心啊  又是一个未来的GM=======================加努==================================================油力===========================

---

### 探讨 #64: 关于《打印可提交的alpha信息并按sharpe排序，在网页上找到alpha手动提交view_alphas(valid_alphas)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【代码分享】PPA alpha 的批量计算小工具内含完整代码代码优化_32470782574487.md
- **评论时间**: 1年前

感谢大佬翻牌
帖子写的很用心啊  又是一个未来的GM
=======================加努===========================
=======================油力===========================

---

### 探讨 #65: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: [Commented] 【效率王】APP-30完全自动化时代.md
- **评论时间**: 3个月前

我进步的速度根本赶不上AI进步的速度， 现在手搓因子的大佬不知道还多不多了。不会以后都是AI出货吧，有一说一，AI出货好像比我的因子更有经济学意义。
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++

---

### 探讨 #66: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】APP-30完全自动化时代_38872307253655.md
- **评论时间**: 3个月前

我进步的速度根本赶不上AI进步的速度， 现在手搓因子的大佬不知道还多不多了。不会以后都是AI出货吧，有一说一，AI出货好像比我的因子更有经济学意义。
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++

---

### 探讨 #67: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天又是向大佬们学习的一天, 提交了一个prod corr 0.46的因子, 使用了以前没用过的fast factor,效果确实不错.

---

### 探讨 #68: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

量化日记3

今天又是羡慕大佬的一天,为什么大佬们多金多才多艺,智商那么那么高,我想来想去想不明白.后来我突然就明白了,因为我照了照镜子.

没过正月十五不算过年,所以最近也确实没啥心思搞量化,十七开始得卷了.

---

### 探讨 #69: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天开始读论文

---

### 探讨 #70: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天combined从0.1涨到0.72, selected从0.12涨到1.33.猝不及防,躺平了这么久,才发现,要是努努力,也许可以冲刺GM的.也许,这就是生活吧.但是不可否认,这期间还是有努力过的,功不唐捐功不唐捐.

---

### 探讨 #71: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

每天看到量化日记,课代表的那个回复,都觉得差距很大.

---

### 探讨 #72: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

USA FND区域红了  正好跳出舒适区  过个季度再见了

---

### 探讨 #73: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

倦怠期也要好好交因子  什么时候可以上GM啊

---

### 探讨 #74: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今日想刷PYR,PYR加1.

---

### 探讨 #75: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

交了一个sharpe 1.3  returns 36% margin 200+的alpha  OS是爆炸还是爆发   很难说

---

### 探讨 #76: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天知道了OS是一个巨大的黑盒

借着PPAC交了不少因子, 喜提base下限,这么搞,OS要崩啊

---

### 探讨 #77: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

日记还是要好好写

---

### 探讨 #78: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

还得加油努力

---

### 探讨 #79: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

vf 0.23 - vf 0.42  何时出狱?

---

### 探讨 #80: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

今天提交了第一个自己的super alpha, 确实, 越早交越好, 可以改善自己的Performance Comparison. 感谢各位大佬的帖子, 组SA的时候, 获益良多.

---

### 探讨 #81: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

交了第二个SA,多交RA,早日实现VF0.9以上!

---

### 探讨 #82: 关于《生成按日期统计的报告》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **评论时间**: 1年前

五一结束  收收心挖矿了

---

### 探讨 #83: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

沙发!
++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++
因子做多了, 腰酸背痛的,好想买一个沙发.

---

### 探讨 #84: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月1日
----------------------------------------
今天是2025年10月1日，今天一共提交了3个alpha

第1个alpha是'GLB/D1/RISK'的，sharpe 2.00，fitness 1.93，margin 18.6‱，selfCorrelation 0.463，prodCorrelation 0.715。使用了ern3_all_delay_1_next_reptime、rsk60_last字段,用了基于风险与流动性的复合反转方法。
第2个alpha是'GLB/D1/RISK'的，sharpe 1.37，fitness 1.93，margin 39.9‱，selfCorrelation 0.354，prodCorrelation 0.659。使用了rsk60_offer字段,用了基于风险指标变化的动量方法。
第3个alpha是'USA/D1/MODEL'的，sharpe 1.47，fitness 1.61，margin 62.7‱，selfCorrelation 0.510，prodCorrelation 0.852。使用了mdl77_chgnoa字段,用了基于基本面变化的盈利质量预测方法。

总结：今天的sharpe数据中规中矩, 最近既要赶进度，又要学新工具，压力有点大，但咬咬牙能扛。

============================================================

---

### 探讨 #85: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月2日
----------------------------------------
今天是2025年10月2日，今天一共提交了3个alpha

第1个alpha是'USA/D1/MACRO'的，sharpe 2.32，fitness 2.03，margin 39.5‱，selfCorrelation 0.427，prodCorrelation 0.754。使用了sector、oth551_beta_size字段,用了基于宏观因子稳定性的行业选股。
第2个alpha是'USA/D1/OPTION'的，sharpe 1.66，fitness 1.54，margin 17.1‱，selfCorrelation 0.398，prodCorrelation 0.625。使用了opt4_152_put_vola_delta75字段,用了基于期权隐含波动率极值的市场情绪预测。
第3个alpha是'USA/D1/MACRO'的，sharpe 1.36，fitness 0.93，margin 27.8‱，selfCorrelation 0.486，prodCorrelation 0.812。使用了oth551_beta_usmv字段,用了基于因子暴露稳定性的预测方法。

总结：今天的prodCorrelation偏高，策略同质化严重, 今天的想法比较天马行空，但值得尝试。

============================================================

---

### 探讨 #86: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月3日
----------------------------------------
今天是2025年10月3日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/NEWS'的，sharpe 1.10，fitness 0.45，margin 9.4‱，selfCorrelation 0.188，prodCorrelation 0.771。使用了nws31_emeatimestamp_time字段,用了基于波动率择时的价格突破方法。
第2个alpha是'EUR/D1/MODEL'的，sharpe 2.59，fitness 1.82，margin 12.5‱，selfCorrelation 0.356，prodCorrelation 0.839。使用了mws46_ravenpack_sum_ens字段,用了基于极端估值与市场情绪的反转方法。

总结：今天的sharpe让人刮目相看，风控到位, prodCorrelation有点高，因子可能烂大街了, 今天尝试了一些新的特征工程方法。

============================================================

---

### 探讨 #87: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月4日
----------------------------------------
今天是2025年10月4日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/NEWS'的，sharpe 1.23，fitness 0.67，margin 12.8‱，selfCorrelation 0.169，prodCorrelation 0.519。使用了nws20_multiple_comp_d1_reporting_start_time_utc字段,用了基于新闻事件时序异常的模式识别。
第2个alpha是'USA/D1/ANALYST'的，sharpe 1.70，fitness 1.04，margin 33.8‱，selfCorrelation 0.556，prodCorrelation 0.655。使用了sector、anl16_actunit_scale字段,用了基于交易模式一致性的截面选股。

总结：今天的prodCorrelation中规中矩, 今天也交上了alpha，保持这个节奏。

============================================================

---

### 探讨 #88: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月5日
    ----------------------------------------
    今天是2025年10月5日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/OPTION'的，sharpe 1.54，fitness 1.22，margin 24.4‱，selfCorrelation 0.119，prodCorrelation 0.417。使用了opt1_deltasurface_d1_moneyness字段,用了基于期权隐含分布偏度的择时方法。
    第2个alpha是'EUR/D1/FUNDAMENTAL'的，sharpe 1.93，fitness 1.57，margin 19.3‱，selfCorrelation 0.358，prodCorrelation 0.542。使用了fnd86_average_score字段,用了基于基本面动量的条件增强方法。

总结：今天的sharpe指标四平八稳, 继续努力，争取明天有更好的alpha。

============================================================

---

### 探讨 #89: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月6日
----------------------------------------
今天是2025年10月6日，今天一共提交了2个alpha

第1个alpha是'USA/D1/INSTITUTIONS'的，sharpe 1.25，fitness 0.71，margin 9.7‱，selfCorrelation 0.380，prodCorrelation 0.707。使用了subindustry、inst18_fundownershipv2_cur_mv字段,用了基于机构持仓相对变化的动量方法。
第2个alpha是'EUR/D1/PV'的，sharpe 1.50，fitness 0.75，margin 8.1‱，selfCorrelation 0.308，prodCorrelation 0.515。使用了pv87_daily_ann_matrix_r1_ebitda_consensus_mean_numdownunfiltered、subindustry字段,用了基于分析师预期反转的逆向投资。

总结：这波sharpe表现算是及格线, 这个fitness水准确实需要提升, 今天把上周的策略做完了，还优化了回测流程，算没白忙活。

============================================================

---

### 探讨 #90: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月7日 
---------------------------------------- 
今天是2025年10月7日，今天一共提交了2个alpha 
第1个alpha是'EUR/D1/MODEL'的，sharpe 1.66，fitness 0.83，margin 9.1‱，selfCorrelation 0.277，prodCorrelation 0.979。使用了oth176_hc_eq_medium字段,用了基于相对持仓排名的截面选股方法。 第2个alpha是'USA/D1/SHORTINTEREST'的，sharpe 1.09，fitness 0.80，margin 82.4‱，selfCorrelation 0.311，prodCorrelation 0.648。使用了subindustry、shrt10_730_standalone_assetsend字段,用了基于相对市场情绪的行业比较方法。 总结：这波prodCorrelation确实有点不给力, 看别人做的数据挖掘报告，感觉自己这方面能力还差不少，得补补课。 
============================================================

---

### 探讨 #91: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月8日
----------------------------------------
今天是2025年10月8日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/PV'的，sharpe 1.67，fitness 1.08，margin 18.9‱，selfCorrelation 0.247，prodCorrelation 0.438。使用了mdl230_allcap_sedol_cashsale、sta3_6_sector字段,用了基于行业调整的现金销售增长动量。
第2个alpha是'EUR/D1/MODEL'的，sharpe 1.58，fitness 1.14，margin 18.0‱，selfCorrelation 0.321，prodCorrelation 0.732。使用了mdl230_allcap_sedol_vesspem21f_cf字段,用了基于模型收益的累积动量方法。

总结：这波sharpe表现算是及格线, fitness表现平庸，有待突破, 今天效率超高，不仅完成了因子测试，还整理了策略库，明天继续冲。

============================================================

---

### 探讨 #92: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月9日
----------------------------------------
今天是2025年10月9日，今天一共提交了2个alpha

第1个alpha是'USA/D1/SHORTINTEREST'的，sharpe 1.17，fitness 0.74，margin 36.4‱，selfCorrelation 0.112，prodCorrelation 0.481。使用了shrt10_730_standalone_sni、subindustry字段,用了基于市场情绪分歧的异常检测。
第2个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.42，fitness 0.65，margin 10.3‱，selfCorrelation 0.214，prodCorrelation 0.470。使用了snt27_skewness字段,用了基于市场情绪极值的反转方法。

总结：sharpe指标不太理想，需要控制风险, 今天的prodCorrelation勉强及格, 虽然量化这条路要学的东西太多，走得慢，但每次进步都觉得很有意义。

============================================================

---

### 探讨 #93: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月10日
----------------------------------------
今天是2025年10月10日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/EARNINGS'的，sharpe 1.30，fitness 0.81，margin 45.3‱，selfCorrelation 0.305，prodCorrelation 0.732。使用了ern3_all_delay_1_pre_interval、anl16_meanrec字段,用了基于分析师共识预期的趋势强化方法。
第2个alpha是'EUR/D1/PV'的，sharpe 1.63，fitness 0.83，margin 8.8‱，selfCorrelation 0.422，prodCorrelation 0.934。使用了pv87_daily_ann_matrix_r1_ebit_consensus_mean_numdownunfiltered字段,用了基于分析师预期修正的负面动量。

总结：fitness表现尚可，继续努力吧, 新数据接口终于调通了，明天就能用新代码挖因子，期待有惊喜。

============================================================

---

### 探讨 #94: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月11日
----------------------------------------
今天是2025年10月11日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/RISK'的，sharpe 1.83，fitness 0.94，margin 9.0‱，selfCorrelation 0.267，prodCorrelation 0.740。使用了rsk59_squeeze_risk字段,用了基于风险特征持续性的量化选股。
第2个alpha是'GLB/D1/MODEL'的，sharpe 1.49，fitness 0.86，margin 16.1‱，selfCorrelation 0.294，prodCorrelation 0.697。使用了snt22_2neg_conf_up_393、mdl250_hc_eq_seasonality、subindustry字段,用了基于行业相对季节性的稳健动量方法。

总结：今天的fitness指标不温不火, 今天的prodCorrelation指标有点拖后腿, 希望能在这次Genius定级取得好结果。

============================================================

---

### 探讨 #95: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月12日
----------------------------------------
今天是2025年10月12日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/RISK'的，sharpe 1.40，fitness 0.59，margin 9.5‱，selfCorrelation 0.356，prodCorrelation 0.847。使用了rsk59_crowded_score字段,用了基于风险因子的系统性低估识别。
第2个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 2.09，fitness 1.10，margin 11.3‱，selfCorrelation 0.437，prodCorrelation 0.934。使用了sector、shrt3_utilizationpercent_units字段,用了基于卖空情绪的反转方法。

总结：今天的sharpe中规中矩, fitness表现平稳，没有太大惊喜, 研究了alpha decay 的规律后，调整了因子的持有周期，回测效果更好了。

============================================================

---

### 探讨 #96: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月13日
----------------------------------------
今天是2025年10月13日，今天一共提交了2个alpha

第1个alpha是'USA/D1/MODEL'的，sharpe 1.20，fitness 0.85，margin 10.2‱，selfCorrelation 0.490，prodCorrelation 0.782。使用了mdl26_num_downgrades_7、industry字段,用了基于行业相对情绪变化的选股方法。
第2个alpha是'USA/D1/ANALYST'的，sharpe 1.32，fitness 0.80，margin 21.7‱，selfCorrelation 0.495，prodCorrelation 0.753。使用了sector、anl16_actunit_scale字段,用了基于基本面动量的相对强弱方法。

总结：今天的fitness指标不温不火, 今天尝试了一些新的特征工程方法。

============================================================

---

### 探讨 #97: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月14日
----------------------------------------
今天是2025年10月14日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/OPTION'的，sharpe 1.93，fitness 1.08，margin 19.6‱，selfCorrelation 0.311，prodCorrelation 0.846。使用了opt4_adjfactor、mdl110_analyst_sentiment字段,用了基于分析师情绪变化的持续性偏离。
第2个alpha是'EUR/D1/FUNDAMENTAL'的，sharpe 1.47，fitness 0.83，margin 19.4‱，selfCorrelation 0.284，prodCorrelation 0.669。使用了fnd28_value_08698q字段,用了基于基本面趋势的动量方法。

总结：今天的prodCorrelation让人头疼，得想办法, 最近学了风险模型的新理论，对量化策略的理解又深了一层。

============================================================

---

### 探讨 #98: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月15日
----------------------------------------
今天是2025年10月15日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/OPTION'的，sharpe 1.52，fitness 0.94，margin 33.7‱，selfCorrelation 0.474，prodCorrelation 0.754。使用了opt4_shareoutstanding字段,用了基于估值偏离与规模调整的均值回归。
第2个alpha是'GLB/D1/NEWS'的，sharpe 1.25，fitness 0.92，margin 17.3‱，selfCorrelation 0.118，prodCorrelation 0.256。使用了mws66_timestamp字段,用了基于新闻情绪动量的相对强度方法。

总结：这波fitness表现算是及格线, 今天的思路比较新颖，期待后续验证。

============================================================

---

### 探讨 #99: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月16日
----------------------------------------
今天是2025年10月16日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/IMBALANCE'的，sharpe 1.65，fitness 1.44，margin 35.2‱，selfCorrelation 0.161，prodCorrelation 0.377。使用了imb5_mktcap、mdl230_allcap_sedol_nlvolcap字段,用了基于市场流动性的条件动量方法。
第2个alpha是'USA/D1/RISK'的，sharpe 1.66，fitness 1.24，margin 11.2‱，selfCorrelation 0.866，prodCorrelation 0.866。使用了buy_to_total_amount_ratio_qtr、rsk62_retseries_industry_5_100_val1字段,用了结合价格复杂度与估值因子的趋势识别。

总结：sharpe表现平稳，没有太大惊喜, prodCorrelation数据不太妙，大家想法都差不多, 最近既要赶进度，又要学新工具，压力有点大，但咬咬牙能扛。

============================================================

---

### 探讨 #100: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月17日
----------------------------------------
今天是2025年10月17日，今天一共提交了2个alpha

第1个alpha是'USA/D1/ANALYST'的，sharpe 1.98，fitness 1.50，margin 69.1‱，selfCorrelation 0.390，prodCorrelation 0.673。使用了anl16_presurprisepct字段,用了基于分析师预测信息熵的稳定性分析。
第2个alpha是'USA/D1/INSTITUTIONS'的，sharpe 1.60，fitness 1.62，margin 31.7‱，selfCorrelation 0.428，prodCorrelation 0.697。使用了inst9_dtc、rsk62_retseries_industry_5_100_val1字段,用了基于风险调整收益稳定性的熵值方法。

总结：今天提交的alpha都还过得去，fitness表现不错, 调试策略 bug 调了 3 小时，终于发现问题，太不容易了。

============================================================

---

### 探讨 #101: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月18日
----------------------------------------
今天是2025年10月18日，今天一共提交了2个alpha

第1个alpha是'USA/D1/EARNINGS'的，sharpe 1.55，fitness 1.37，margin 43.2‱，selfCorrelation 0.528，prodCorrelation 0.847。使用了ern5_total_days_changed字段,用了基于信息熵的盈利公告模式预测。
第2个alpha是'GLB/D1/PV'的，sharpe 1.40，fitness 0.81，margin 10.2‱，selfCorrelation 0.403，prodCorrelation 0.628。使用了close、anl83_sent_score_pres字段,用了基于行为金融的持续性情绪选股。

总结：今天的sharpe指标属于正常范围, 感觉自己在策略优化方面进步了一丢丢。

============================================================

---

### 探讨 #102: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月19日 ---------------------------------------- 今天是2025年10月19日，今天一共提交了2个alpha 第1个alpha是'EUR/D1/FUNDAMENTAL'的，sharpe 2.04，fitness 1.32，margin 24.0‱，selfCorrelation 0.334，prodCorrelation 0.633。使用了fnd23_intfvm_dtns、entity_employee_count字段,用了基于基本面动量与规模效应的多因子方法。 第2个alpha是'GLB/D1/MACRO'的，sharpe 1.43，fitness 0.77，margin 17.0‱，selfCorrelation 0.309，prodCorrelation 0.723。使用了oth551_r2_vlue、mdl219_1_fc_dypeg字段,用了基于预测误差分布稳定性的量化择时。 总结：fitness表现平稳，没有太大惊喜, 今天的prodCorrelation让人头疼，得想办法, 盯着回测曲线看了半天，发现因子在某些月份表现差，得找原因。 ============================================================

---

### 探讨 #103: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月20日
----------------------------------------
今天是2025年10月20日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/MODEL'的，sharpe 2.25，fitness 1.41，margin 16.5‱，selfCorrelation 0.359，prodCorrelation 0.561。使用了mdl26_mn_stmt_prc_rt_fy1_rvn、opt30_px_low字段,用了基于信息熵与价格位置的风险规避方法。
第2个alpha是'GLB/D1/SHORTINTEREST'的，sharpe 1.42，fitness 1.50，margin 63.9‱，selfCorrelation 0.403，prodCorrelation 0.728。使用了shrt2_t3m_volatility_rank、mdl250_malta_eq_score字段,用了基于多因子动态切换的混合信号方法。

总结：今天的alpha fitness表现优秀，值得肯定, 看了 WorldQuant 新出的文档，好多思路得慢慢消化，先记下来。

============================================================

---

### 探讨 #104: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月21日
----------------------------------------
今天是2025年10月21日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/MACRO'的，sharpe 2.26，fitness 1.43，margin 12.6‱，selfCorrelation 0.364，prodCorrelation 0.700。使用了oth551_r2_mtum、fnd72_s_pit_or_is_q_ebit字段,用了基于基本面动量的排序方法。
第2个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 2.27，fitness 1.85，margin 16.6‱，selfCorrelation 0.518，prodCorrelation 0.654。使用了io_inst_prev_holding、anl4_sadaf_epsa_low字段,用了基于基本面趋势的动量方法。

总结：sharpe表现优异，风险管理做得好, 调整了 alpha 的衰减参数，回测的稳定性提升了不少。

============================================================

---

### 探讨 #105: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月22日
----------------------------------------
今天是2025年10月22日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 1.79，fitness 1.60，margin 28.8‱，selfCorrelation 0.390，prodCorrelation 0.449。使用了shrt3_utilizationpercent_units、anl4_af_eps_low字段,用了基于盈利修正与市场情绪的动态对比。
第2个alpha是'GLB/D1/SHORTINTEREST'的，sharpe 1.86，fitness 1.21，margin 11.6‱，selfCorrelation 0.445，prodCorrelation 0.778。使用了star_si_country_rank_unadj、oth553_estvalue字段,用了基于市场情绪与区域调整的复合因子选股。

总结：prodCorrelation有点高，因子可能烂大街了, 今天的sharpe让人刮目相看，风控到位, 今天的debug过程让我学到了很多。

============================================================

---

### 探讨 #106: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月23日 ---------------------------------------- 今天是2025年10月23日，今天一共提交了2个alpha 第1个alpha是'EUR/D1/INSIDERS'的，sharpe 1.32，fitness 1.72，margin 92.1‱，selfCorrelation 0.191，prodCorrelation 0.549。使用了mdl219_1_beta、insd12_positionchangetransactionamount字段,用了基于预测模型偏度的条件过滤方法。 第2个alpha是'USA/D1/INSIDERS'的，sharpe 1.78，fitness 1.20，margin 21.9‱，selfCorrelation 0.432，prodCorrelation 0.722。使用了insd3_8k_freq_latest_release、subindustry、snt27_kurtosis_16字段,用了基于情绪与基本面的相对动量方法。 总结：sharpe表现平庸，有待突破, prodCorrelation表现不尽如人意，要创新了, 今天做策略的时候，突然想起刚入门 “挖矿” 的冲劲，得保持这份热情。 ============================================================

---

### 探讨 #107: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月24日
----------------------------------------
今天是2025年10月24日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/ANALYST'的，sharpe 1.54，fitness 0.81，margin 30.0‱，selfCorrelation 0.399，prodCorrelation 0.848。使用了oth455_customer_n2v_p10_q50_w4_pca_fact3_cluster_20、mws87_analyst_sent_score_qa字段,用了基于分析师情绪动量的相对强弱方法。
第2个alpha是'GLB/D1/PV'的，sharpe 1.68，fitness 1.09，margin 9.3‱，selfCorrelation 0.417，prodCorrelation 0.725。使用了sta3_sec_sector、mws87_analyst_sent_score_qa字段,用了基于分析师情绪的行业相对动量。

总结：这个prodCorrelation数据让人有点焦虑, 今天 debug 的时候，顺便搞懂了之前没明白的回测逻辑，也算意外收获。

============================================================

---

### 探讨 #108: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月25日
----------------------------------------
今天是2025年10月25日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/OPTION'的，sharpe 1.19，fitness 0.83，margin 28.3‱，selfCorrelation 0.487，prodCorrelation 0.616。使用了snt22_2neut_max_392、opt4_secpr_volume字段,用了基于量价动量的平滑信号方法。
第2个alpha是'USA/D1/SOCIALMEDIA'的，sharpe 1.13，fitness 0.54，margin 18.7‱，selfCorrelation 0.401，prodCorrelation 0.782。使用了scl12_alltype_sentvec字段,用了基于社交媒体情绪稳定性的趋势跟踪。

总结：这个sharpe水准确实需要提升, 今天也交上了alpha，保持这个节奏。

============================================================

---

### 探讨 #109: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月26日
----------------------------------------
今天是2025年10月26日，今天一共提交了2个alpha

第1个alpha是'USA/D1/EARNINGS'的，sharpe 1.51，fitness 0.95，margin 11.7‱，selfCorrelation 0.490，prodCorrelation 0.708。使用了market、ern3_expected_time字段,用了基于盈利预期一致性的质量因子方法。
第2个alpha是'USA/D1/IMBALANCE'的，sharpe 1.58，fitness 1.05，margin 8.8‱，selfCorrelation 0.252，prodCorrelation 0.543。使用了imb5_mktcap字段,用了基于订单流异常聚集的反转方法。

总结：这个prodCorrelation数据让人有点焦虑, 最近的市场环境对策略是个不小的挑战。

============================================================

---

### 探讨 #110: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年10月27日
----------------------------------------
今天是2025年10月27日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/ANALYST'的，sharpe 1.43，fitness 0.76，margin 13.3‱，selfCorrelation 0.414，prodCorrelation 0.751。使用了industry、mws87_analyst_pos_logit_qa字段,用了基于分析师情绪动量的相对优势方法。
第2个alpha是'GLB/D1/PV'的，sharpe 1.77，fitness 2.31，margin 39.3‱，selfCorrelation 0.362，prodCorrelation 0.677。使用了pv13_52_minvol_1m_all_delay_1_sector、rsk60_last字段,用了基于风险因子动量的行业中性方法。

总结：今天的sharpe数据中规中矩, 今天的alpha fitness表现优秀，值得肯定, 今天的工作效率比昨天高了很多。

============================================================

---

### 探讨 #111: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 1年前

今天交满因子, 点了四次PYR, 想把60个PYR点满, 稍微计算一下,需要60天,每天提交不一样的单因子, 感觉真的是很难很难啊.佩服游戏王,上个季度那么能点.
+++++++++++++++++++++++++++++++++++快说,我是不是一楼!++++++++++++++++++++++++

---

### 探讨 #112: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月1日
----------------------------------------
今天是2025年7月1日，今天一共提交了1个alpha

今日alpha:'EUR/D1/ANALYST'的，sharpe 2.04，fitness 1.35，margin 14.2‱，selfCorrelation 0.464，prodCorrelation 0.551。使用了anl69_bps_most_recent_period_end_dt字段,用了基于技术指标的量价趋势策略策略。

总结：fitness数据看起来相当不错，今天收获满满, 今天的工作还算满意，明天继续加油。

============================================================

---

### 探讨 #113: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月2日
----------------------------------------
今天是2025年7月2日，今天一共提交了2个alpha

第1个alpha是'USA/D1/NEWS'的，sharpe 1.61，fitness 0.94，margin 15.1‱，selfCorrelation 0.438，prodCorrelation 0.732。使用了nws31_amertimestamp_time字段,用了基于时间序列窗口统计的趋势跟踪策略策略。
第2个alpha是'USA/D1/OTHER'的，sharpe 2.00，fitness 1.72，margin 14.8‱，selfCorrelation 0.137，prodCorrelation 0.553。使用了oth110_mbl_visits字段,用了基于时间序列处理的动量策略策略。

总结：今天的prodCorrelation偏高，策略同质化严重, 今天的工作还算满意，明天继续加油。

---

### 探讨 #114: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月3日
----------------------------------------
今天是2025年7月3日，今天一共提交了1个alpha

今日alpha:'EUR/D1/MODEL'的，sharpe 1.75，fitness 1.13，margin 36.0‱，selfCorrelation 0.333，prodCorrelation 0.854。使用了mdl109_m1d_cer_se字段,用了基于时间序列统计特征的量化策略策略。

总结：prodCorrelation有些超标，创新性不足, 希望能在风险控制方面做得更好。

============================================================

---

### 探讨 #115: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月4日
----------------------------------------
今天是2025年7月4日，今天一共提交了1个alpha

今日alpha:'USA/D1/MODEL'的，sharpe 1.47，fitness 1.76，margin 28.7‱，selfCorrelation 0.380，prodCorrelation 0.718。使用了mdl237_raw_etf_us_p_pop_g1m字段,用了基于技术指标的反转策略策略。

总结：fitness数据看起来相当不错，今天收获满满, prodCorrelation数据不太妙，大家想法都差不多, 今天的想法比较天马行空，但值得尝试。

============================================================

---

### 探讨 #116: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月5日
----------------------------------------
今天是2025年7月5日，今天一共提交了3个alpha

第1个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 2.40，fitness 1.64，margin 16.1‱，selfCorrelation 0.277，prodCorrelation 0.681。使用了anl39_qtanbvps、shrt3_utilizationpercent_units字段,用了基于市场微观结构的反转策略策略。
第2个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.91，fitness 1.84，margin 18.6‱，selfCorrelation 0.993，prodCorrelation 0.993。使用了snt27_wq_pit字段,用了基于时间序列统计特征的趋势策略策略。
第3个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.92，fitness 1.90，margin 19.6‱，selfCorrelation 0.293，prodCorrelation 0.681。使用了snt27_wq_pit字段,用了基于多因子模型的组合优化策略策略。

总结：今天的alpha fitness表现优秀，值得肯定, 希望能在这次Genius定级取得好结果。

============================================================

---

### 探讨 #117: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月6日
----------------------------------------
今天是2025年7月6日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/RISK'的，sharpe 2.10，fitness 1.25，margin 20.7‱，selfCorrelation 0.438，prodCorrelation 1.000。使用了rsk70_mfm2_euetrd_shortint字段,用了基于反向排序的风险调整反转策略策略。
第2个alpha是'GLB/D1/FUNDAMENTAL'的，sharpe 1.93，fitness 1.12，margin 34.2‱，selfCorrelation 0.907，prodCorrelation 0.907。使用了fnd23_intfvalld1_ctcv字段,用了基于标准化财务因子的趋势策略策略。
第3个alpha是'GLB/D1/MODEL'的，sharpe 1.60，fitness 0.82，margin 26.7‱，selfCorrelation 0.431，prodCorrelation 0.638。使用了mdl138_longsimeq_qpdi5_op_margin字段,用了基于技术指标的动量增强策略策略。
第4个alpha是'USA/D1/MACRO'的，sharpe 1.51，fitness 1.00，margin 20.5‱，selfCorrelation 0.420，prodCorrelation 0.658。使用了mcr55_decimals、mdl163_fc_fwdep_deltapredict_model_predict字段,用了基于模型预测的动量策略策略。

总结：今天的alpha fitness勉强及格, 今天的prodCorrelation让人头疼，缺乏独特性, 最近的研究让我对alpha decay有了新认识。

============================================================

---

### 探讨 #118: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月7日
----------------------------------------
今天是2025年7月7日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/ANALYST'的，sharpe 1.87，fitness 1.04，margin 26.9‱，selfCorrelation 0.378，prodCorrelation 0.541。使用了anl69_bps_most_recent_period_end_dt字段,用了基于时间序列统计特征的量化策略策略。
第2个alpha是'EUR/D1/MODEL'的，sharpe 1.38，fitness 1.04，margin 56.2‱，selfCorrelation 0.447，prodCorrelation 0.554。使用了mdl26_mstchg_pct_fq1_btd_7字段,用了基于技术指标的量化信号策略策略。
第3个alpha是'GLB/D1/ANALYST'的，sharpe 1.62，fitness 0.82，margin 18.9‱，selfCorrelation 0.565，prodCorrelation 0.837。使用了anl69_best_net_debt字段,用了基于技术指标的趋势跟踪策略策略。
第4个alpha是'EUR/D1/MODEL'的，sharpe 1.90，fitness 1.30，margin 16.7‱，selfCorrelation 0.297，prodCorrelation 0.812。使用了mdl26_peg_mean_fy1字段,用了基于因子分析与技术指标的趋势策略策略。

总结：今天的prodCorrelation偏高，策略同质化严重, sharpe数据不温不火, 继续努力，争取明天有更好的alpha。

============================================================

---

### 探讨 #119: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月8日
----------------------------------------
今天是2025年7月8日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/PV'的，sharpe 1.63，fitness 1.27，margin 15.1‱，selfCorrelation 0.421，prodCorrelation 0.574。使用了pv87_daily_ann_matrix_r1_ebt_normalized_consensus_mean_numupunfiltered字段,用了基于技术指标的信息比率策略策略。
第2个alpha是'EUR/D1/MODEL'的，sharpe 1.46，fitness 1.11，margin 11.6‱，selfCorrelation 0.412，prodCorrelation 0.580。使用了mdl109_cfo_curr_liab字段,用了基于财务指标的量价复合策略策略。
第3个alpha是'EUR/D1/MODEL'的，sharpe 1.44，fitness 1.00，margin 17.8‱，selfCorrelation 0.410，prodCorrelation 0.572。使用了mdl109_op_margin_chg字段,用了基于时间序列极值差异的动量策略策略。
第4个alpha是'EUR/D1/ANALYST'的，sharpe 2.03，fitness 1.27，margin 14.8‱，selfCorrelation 0.569，prodCorrelation 0.816。使用了est_12m_dps_raisednum_4wks字段,用了基于预期收益分布的反转策略策略。

总结：fitness表现中规中矩，还有提升空间, 今天的prodCorrelation偏高，是哪位天才跟我想法一致??, 今天调试了很久，终于找到了问题所在。

============================================================

---

### 探讨 #120: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月9日
----------------------------------------
今天是2025年7月9日，今天一共提交了1个alpha

今日alpha:'EUR/D1/MODEL'的，sharpe 1.18，fitness 1.17，margin 148.6‱，selfCorrelation 0.475，prodCorrelation 0.634。使用了mdl109_roa_stab字段,用了基于财务质量因子的时序动量策略策略。

总结：今天的fitness指标平平无奇, sharpe偏低，不够稳定, margin倒是还不错.断粮了断粮了断粮了...

============================================================

---

### 探讨 #121: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月10日
----------------------------------------
今天是2025年7月10日，今天一共提交了1个alpha

今日alpha:'EUR/D1/SHORTINTEREST'的，sharpe 2.31，fitness 1.42，margin 12.3‱，selfCorrelation 0.484，prodCorrelation 0.963。使用了subindustry、shrt3_utilizationpercent_units字段,用了基于行业相对表现的反转策略策略。

总结：今天的alpha fitness表现优秀，值得肯定, 最近worldquant新东西很多，需要多学习。

---

### 探讨 #122: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月11日
----------------------------------------
今天是2025年7月11日，今天一共提交了4个alpha

第1个alpha是'GLB/D1/MODEL'的，sharpe 2.40，fitness 1.38，margin 27.8‱，selfCorrelation 0.482，prodCorrelation 0.936。使用了subindustry、mdl138_longsimeq_3idpc字段,用了基于行业中性化的动量策略策略。
第2个alpha是'USA/D1/NEWS'的，sharpe 1.23，fitness 0.89，margin 10.9‱，selfCorrelation 0.322，prodCorrelation 0.717。使用了news_session_range_pct字段,用了基于新闻情绪的技术指标动量策略策略。
第3个alpha是'USA/D1/NEWS'的，sharpe 1.13，fitness 0.84，margin 27.6‱，selfCorrelation 0.261，prodCorrelation 0.552。使用了news_open_vol字段,用了基于新闻情绪的技术指标动量策略策略。
第4个alpha是'GLB/D1/OTHER'的，sharpe 1.20，fitness 0.61，margin 27.9‱，selfCorrelation 0.383，prodCorrelation 0.469。使用了subindustry、oth128_cfoice_49字段,用了基于行业相对强度的动量策略策略。

总结：sharpe就一个高的,其他的都很低...好难啊好难啊好难啊

---

### 探讨 #123: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月12日
----------------------------------------
今天是2025年7月12日，今天一共提交了4个alpha

第1个alpha是'USA/D1/OPTION'的，sharpe 1.28，fitness 0.98，margin 16.8‱，selfCorrelation 0.224，prodCorrelation 0.604。使用了opt6_divamt字段,用了基于技术指标的趋势动量策略策略。
第2个alpha是'USA/D1/OPTION'的，sharpe 1.32，fitness 1.31，margin 39.2‱，selfCorrelation 0.459，prodCorrelation 0.836。使用了opt6_ivetfratiostd1y字段,用了基于技术指标的波动率因子策略策略。
第3个alpha是'GLB/D1/MODEL'的，sharpe 1.97，fitness 0.97，margin 14.4‱，selfCorrelation 0.487，prodCorrelation 0.915。使用了industry、mdl138_longsimeq_3idpc字段,用了基于行业中性化的技术指标动量策略策略。
第4个alpha是'GLB/D1/OTHER'的，sharpe 1.10，fitness 0.46，margin 17.7‱，selfCorrelation 0.392，prodCorrelation 0.541。使用了oth455_partner_n2v_p10_q200_w1_pca_fact3_value、subindustry字段,用了基于行业相对排名的动量策略策略。

总结：fitness表现中规中矩，还有提升空间, 今天的prodCorrelation让人头疼，缺乏独特性, 希望能在下个月的比赛中取得好成绩。

============================================================

---

### 探讨 #124: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月13日
----------------------------------------
今天是2025年7月13日，今天一共提交了2个alpha

第1个alpha是'USA/D1/OPTION'的，sharpe 1.46，fitness 1.22，margin 27.2‱，selfCorrelation 0.642，prodCorrelation 0.900。使用了opt6_nexterntod字段,用了基于时间序列极值的动量策略策略。
第2个alpha是'USA/D1/OTHER'的，sharpe 1.48，fitness 0.92，margin 21.3‱，selfCorrelation 0.433，prodCorrelation 0.773。使用了oth143_buy_tier1_broker_rank1字段,用了基于信息熵的时序模式识别策略策略。

总结：今天的alpha fitness勉强及格, 最近的研究让我对alpha decay有了新认识。

============================================================

---

### 探讨 #125: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月14日
----------------------------------------
今天是2025年7月14日，今天一共提交了4个alpha

第1个alpha是'USA/D1/OPTION'的，sharpe 1.12，fitness 0.85，margin 77.0‱，selfCorrelation 0.368，prodCorrelation 0.815。使用了opt6_volofivol字段,用了基于波动率特征的反转策略策略。
第2个alpha是'USA/D1/OPTION'的，sharpe 1.50，fitness 0.84，margin 6.9‱，selfCorrelation 0.245，prodCorrelation 0.794。使用了implied_volatility_mean_60字段,用了基于波动率衰减的时序排名策略策略。
第3个alpha是'USA/D1/RISK'的，sharpe 1.31，fitness 0.70，margin 15.9‱，selfCorrelation 0.331，prodCorrelation 0.945。使用了rsk70_mfm2_usfast_sentmt字段,用了基于情绪因子的动量策略策略。
第4个alpha是'USA/D1/RISK'的，sharpe 1.60，fitness 1.23，margin 17.2‱，selfCorrelation 0.110，prodCorrelation 0.581。使用了rsk70_mfm2_usfast_shortint、ern5_total_days_changed字段,用了基于技术指标与事件驱动的回归策略策略。

总结：今天的alpha fitness勉强及格, 今天的prodCorrelation太高，策略同质化严重, 最近的robust测试结果还算令人满意。

---

### 探讨 #126: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月15日
----------------------------------------
今天是2025年7月15日，今天一共提交了1个alpha

今日alpha:'USA/D1/OTHER'的，sharpe 1.51，fitness 0.91，margin 22.8‱，selfCorrelation 0.259，prodCorrelation 0.602。使用了oth110_histort_ttl_bounce_rate字段,用了基于历史表现的技术指标反转策略策略。

总结：prodCorrelation有些超标，创新性不足, 断粮中。

============================================================

---

### 探讨 #127: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月16日
----------------------------------------
今天是2025年7月16日，今天一共提交了4个alpha

第1个alpha是'USA/D1/OTHER'的，sharpe 1.57，fitness 1.02，margin 15.0‱，selfCorrelation 0.271，prodCorrelation 0.732。使用了oth110_histort_dtp_page_views字段,用了基于历史表现的均值回归策略策略。
第2个alpha是'USA/D1/OTHER'的，sharpe 2.13，fitness 1.52，margin 32.8‱，selfCorrelation 0.230，prodCorrelation 0.933。使用了oth110_history_mobile_visit_duration字段,用了基于时间序列形态的均值回复策略策略。
第3个alpha是'USA/D1/INSTITUTIONS'的，sharpe 1.33，fitness 1.37，margin 21.3‱，selfCorrelation 0.508，prodCorrelation 0.689。使用了inst13_d1_cancels字段,用了基于时间序列复杂度的反转策略策略。
第4个alpha是'USA/D1/RISK'的，sharpe 1.30，fitness 0.67，margin 22.8‱，selfCorrelation 0.514，prodCorrelation 0.679。使用了rsk70_mfm2_usfast_sentmt字段,用了基于情绪指标的反转策略策略。

总结：fitness数据一般般，不算太差, prodCorrelation数据不太妙，大家想法都差不多, 希望明天能有更多的进展。

============================================================

---

### 探讨 #128: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月17日
----------------------------------------
今天是2025年7月17日，今天一共提交了2个alpha

第1个alpha是'USA/D1/NEWS'的，sharpe 1.61，fitness 0.94，margin 15.1‱，selfCorrelation 0.438，prodCorrelation 0.732。使用了nws31_amertimestamp_time字段,用了基于时间序列窗口统计的趋势跟踪策略策略。
第2个alpha是'USA/D1/OTHER'的，sharpe 2.00，fitness 1.72，margin 14.8‱，selfCorrelation 0.137，prodCorrelation 0.553。使用了oth110_mbl_visits字段,用了基于时间序列处理的动量策略策略。

总结：今天的prodCorrelation偏高，策略同质化严重, 今天的工作还算满意，明天继续加油。

============================================================

---

### 探讨 #129: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月18日
----------------------------------------
今天是2025年7月18日，今天一共提交了4个alpha

第1个alpha是'USA/D1/ANALYST'的，sharpe 1.14，fitness 0.62，margin 15.8‱，selfCorrelation 0.385，prodCorrelation 0.708。使用了anl21_p_d1_price字段,用了基于时间序列复杂度的均值回归策略策略。
第2个alpha是'USA/D1/SOCIALMEDIA'的，sharpe 1.22，fitness 0.87，margin 10.2‱，selfCorrelation 0.143，prodCorrelation 0.658。使用了scl4_retweets_total_tw字段,用了基于时间序列平滑处理的动量增强策略策略。
第3个alpha是'USA/D1/OTHER'的，sharpe 1.61，fitness 0.98，margin 21.4‱，selfCorrelation 0.322，prodCorrelation 0.736。使用了oth110_dtp_pages_per_visit字段,用了基于时间序列窗口极值的反转策略策略。
第4个alpha是'USA/D1/RISK'的，sharpe 1.68，fitness 1.23，margin 10.7‱，selfCorrelation 0.618，prodCorrelation 0.786。使用了oth450_mfm_use4_ri_value字段,用了基于技术指标的趋势跟踪策略策略。

总结：今天的prodCorrelation让人头疼，缺乏独特性, 希望这波alpha能通过OS的验证。

============================================================

---

### 探讨 #130: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月19日
----------------------------------------
今天是2025年7月19日，今天一共提交了4个alpha

第1个alpha是'USA/D1/OTHER'的，sharpe 1.38，fitness 0.77，margin 22.3‱，selfCorrelation 0.397，prodCorrelation 0.801。使用了oth128_ceocashcompensation字段,用了基于信息熵的时间序列复杂度策略策略。
第2个alpha是'USA/D1/OTHER'的，sharpe 1.55，fitness 0.83，margin 21.3‱，selfCorrelation 0.446，prodCorrelation 0.683。使用了oth696_sopld_47字段,用了基于时间序列极值差异的动量策略策略。
第3个alpha是'USA/D1/OTHER'的，sharpe 1.20，fitness 0.66，margin 19.7‱，selfCorrelation 0.441，prodCorrelation 0.801。使用了industry、oth696_events_sentiment_score字段,用了基于行业分组的情绪动量策略策略。
第4个alpha是'USA/D1/INSTITUTIONS'的，sharpe 1.77，fitness 1.14，margin 35.6‱，selfCorrelation 0.404，prodCorrelation 0.721。使用了inst11_current_dtc字段,用了基于时间序列动量的趋势跟踪策略策略。

总结：sharpe数据不温不火, 希望能找到更多稳定的alpha来源。

============================================================

---

### 探讨 #131: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月20日
----------------------------------------
今天是2025年7月20日，今天一共提交了4个alpha

第1个alpha是'USA/D1/RISK'的，sharpe 1.49，fitness 1.24，margin 14.2‱，selfCorrelation 0.494，prodCorrelation 0.814。使用了oth450_mfm_use4_ri_earnyield字段,用了基于技术指标的范围突破策略策略。
第2个alpha是'USA/D1/OTHER'的，sharpe 2.07，fitness 1.60，margin 26.5‱，selfCorrelation 0.622，prodCorrelation 0.833。使用了oth381_organic_search_visits字段,用了基于时间序列特征的模式识别策略策略。
第3个alpha是'USA/D1/OTHER'的，sharpe 2.56，fitness 1.61，margin 15.6‱，selfCorrelation 0.361，prodCorrelation 0.763。使用了oth696_combined_sentiment_score_53字段,用了基于情绪指标的均值回归策略策略。
第4个alpha是'USA/D1/INSTITUTIONS'的，sharpe 1.24，fitness 0.62，margin 16.5‱，selfCorrelation 0.498，prodCorrelation 0.577。使用了inst11_chg_dtc字段,用了基于技术指标的趋势跟踪策略策略。

总结：今天的alpha质量挺好的，fitness指标很给力, sharpe数据相当稳健，令人满意, 最近的robust测试结果还算令人满意。

============================================================

---

### 探讨 #132: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月21日
----------------------------------------
今天是2025年7月21日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/INSIDERS'的，sharpe 2.56，fitness 1.87，margin 22.6‱，selfCorrelation 0.344，prodCorrelation 0.982。使用了insd5_nm_kor、mdl139_score字段,用了基于时间序列衰减的动量策略策略。
第2个alpha是'USA/D1/IMBALANCE'的，sharpe 1.20，fitness 0.86，margin 27.4‱，selfCorrelation 0.506，prodCorrelation 0.748。使用了anl82_netq_deltaprofitability_profitability5、imb1_value字段,用了基于盈利能力变化的价值发现策略策略。
第3个alpha是'USA/D1/IMBALANCE'的，sharpe 1.35，fitness 0.80，margin 62.7‱，selfCorrelation 0.376，prodCorrelation 0.639。使用了imb1_imbalance、mdl159_supplier_relationshipquality_value字段,用了基于供应商关系质量的价值增强策略策略。
第4个alpha是'USA/D1/IMBALANCE'的，sharpe 2.10，fitness 1.55，margin 21.2‱，selfCorrelation 0.476，prodCorrelation 0.837。使用了imb1_datatime、oth696_combined_sentiment_score_53字段,用了基于情绪指标的均值回归策略策略。

总结：今天的alpha fitness表现优秀，值得肯定, 今天的工作让我想起了刚刚挖矿时的激情。

============================================================

---

### 探讨 #133: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月22日
----------------------------------------
今天是2025年7月22日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/OTHER'的，sharpe 1.73，fitness 1.13，margin 13.8‱，selfCorrelation 0.418，prodCorrelation 0.855。使用了oth696_combined_sentiment_score_525字段,用了基于情绪因子的标准化策略策略。
第2个alpha是'EUR/D1/ANALYST'的，sharpe 1.33，fitness 0.67，margin 19.8‱，selfCorrelation 0.441，prodCorrelation 0.785。使用了anl16_actsurprise字段,用了基于分析师预期调整的动量策略策略。
第3个alpha是'EUR/D1/MODEL'的，sharpe 2.31，fitness 1.59，margin 58.1‱，selfCorrelation 0.396，prodCorrelation 0.989。使用了mdl252_shield2字段,用了基于技术指标的趋势跟踪策略策略。
第4个alpha是'EUR/D1/MODEL'的，sharpe 1.76，fitness 1.90，margin 30.0‱，selfCorrelation 0.370，prodCorrelation 0.585。使用了mdl39_d1_val_mo_sector_rank字段,用了基于行业相对强度的动量策略策略。

总结：prodCorrelation有些超标，创新性不足, 今天的想法比较天马行空，但值得尝试。

============================================================

---

### 探讨 #134: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月23日
----------------------------------------
今天是2025年7月23日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/INSIDERS'的，sharpe 2.03，fitness 1.52，margin 23.2‱，selfCorrelation 0.455，prodCorrelation 0.925。使用了oth176_hc_eq_hedge、insd1_shares字段,用了基于标准化因子的统计套利策略策略。
第2个alpha是'EUR/D1/INSIDERS'的，sharpe 1.34，fitness 1.71，margin 158.0‱，selfCorrelation 0.551，prodCorrelation 0.789。使用了mdl31_pricesales_prior_y、insd1_price字段,用了基于基本面指标的反向交易策略策略。
第3个alpha是'EUR/D1/INSIDERS'的，sharpe 1.46，fitness 0.73，margin 22.5‱，selfCorrelation 0.332，prodCorrelation 0.858。使用了insd1_gvkey、mdl138_dtl_3idp字段,用了基于时间序列衰减的排名动量策略策略。
第4个alpha是'USA/D1/INSIDERS'的，sharpe 1.18，fitness 0.66，margin 29.5‱，selfCorrelation 0.517，prodCorrelation 0.782。使用了insd4_bonus、mdl159_competitor_relationshipquality_cross字段,用了基于时间序列衰减的动量策略策略。

总结：今天的sharpe中规中矩, prodCorrelation有点高，因子可能烂大街了, 最近的alpha都比较保守，需要更大胆一些。

============================================================

---

### 探讨 #135: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月24日
----------------------------------------
今天是2025年7月24日，今天一共提交了4个alpha

第1个alpha是'USA/D1/INSIDERS'的，sharpe 1.12，fitness 1.17，margin 36.2‱，selfCorrelation 0.285，prodCorrelation 0.815。使用了anl82_prey_deltaprofitability_profitability3、insd4_other字段,用了基于技术指标的价格区间策略策略。
第2个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.73，fitness 1.54，margin 36.0‱，selfCorrelation 0.404，prodCorrelation 0.626。使用了io_fund_pct、mdl39_d1_val_mo_global_rank字段,用了基于时间序列信息的动量策略策略。
第3个alpha是'EUR/D1/INSIDERS'的，sharpe 1.16，fitness 0.79，margin 37.8‱，selfCorrelation 0.574，prodCorrelation 0.745。使用了star_cr_global_rank、insd1_tradesignificance字段,用了基于时间序列极值的动量策略策略。
第4个alpha是'ASI/D1/PV'的，sharpe 2.50，fitness 2.07，margin 25.6‱，selfCorrelation 0.569，prodCorrelation 0.853。使用了oth176_hc_eq_seasonality、cap字段,用了基于行业中性化的季节性因子策略策略。

总结：sharpe数据不温不火, 今天的alpha质量挺好的，fitness指标很给力, 今天效率不错，明天争取更上一层楼。

============================================================

---

### 探讨 #136: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月25日
----------------------------------------
今天是2025年7月25日，今天一共提交了3个alpha

第1个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 2.26，fitness 1.42，margin 12.5‱，selfCorrelation 0.435，prodCorrelation 0.675。使用了oth100_top5_people_also_watch_ticker_ii、rsk59_squeeze_risk字段,用了基于技术指标形态的时序动量策略策略。
第2个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.50，fitness 1.09，margin 64.3‱，selfCorrelation 0.456，prodCorrelation 0.881。使用了mdl50_bk_analyst_revisn、inst25_age字段,用了基于分析师预期修正的动量策略策略。
第3个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 2.23，fitness 2.50，margin 101.9‱，selfCorrelation 0.365，prodCorrelation 0.731。使用了mdl39_d1_val_mo_industry_rank、io_fund_number字段,用了基于行业排名的动量策略策略。

总结：今天提交的alpha都还过得去，fitness表现不错, 继续努力，争取明天有更好的alpha。

============================================================

---

### 探讨 #137: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月27日
----------------------------------------
今天是2025年7月27日，今天一共提交了3个alpha

第1个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 2.40，fitness 1.64，margin 16.1‱，selfCorrelation 0.277，prodCorrelation 0.681。使用了anl39_qtanbvps、shrt3_utilizationpercent_units字段,用了基于市场微观结构的反转策略策略。
第2个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.91，fitness 1.84，margin 18.6‱，selfCorrelation 0.993，prodCorrelation 0.993。使用了snt27_wq_pit字段,用了基于时间序列统计特征的趋势策略策略。
第3个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.92，fitness 1.90，margin 19.6‱，selfCorrelation 0.293，prodCorrelation 0.681。使用了snt27_wq_pit字段,用了基于多因子模型的组合优化策略策略。

总结：今天的alpha fitness表现优秀，值得肯定, 希望能在这次Genius定级取得好结果。

============================================================

---

### 探讨 #138: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月28日
----------------------------------------
今天是2025年7月28日，今天一共提交了3个alpha

第1个alpha是'EUR/D1/MACRO'的，sharpe 2.45，fitness 1.60，margin 12.0‱，selfCorrelation 0.408，prodCorrelation 0.650。使用了est_12m_gps_raisednum_4wks、mcr27_postlength2字段,用了基于多因子模型的选股策略策略。
第2个alpha是'EUR/D1/PV'的，sharpe 2.03，fitness 1.28，margin 13.7‱，selfCorrelation 0.490，prodCorrelation 0.490。使用了close、anl69_bps_most_recent_period_end_dt字段,用了基于多因子模型的选股策略策略。
第3个alpha是'USA/D1/PV'的，sharpe 1.40，fitness 0.79，margin 12.8‱，selfCorrelation 0.335，prodCorrelation 0.617。使用了pv52_yse_american_outquote_avg_amt字段,用了基于时间序列排名的动量策略策略。

总结：sharpe指标表现一般，风险控制得当, corr倒是正常一点了, 最近的研究让我对alpha decay有了新认识。

============================================================

---

### 探讨 #139: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月29日
----------------------------------------
今天是2025年7月29日，今天一共提交了3个alpha

第1个alpha是'EUR/D1/MACRO'的，sharpe 1.61，fitness 2.25，margin 201.3‱，selfCorrelation 0.362，prodCorrelation 0.761。使用了mcr27_verified_ds3、mdl26_stm_prc_rt_f12m_rvn字段,用了基于时间序列动量的趋势跟踪策略策略。
第2个alpha是'EUR/D1/OPTION'的，sharpe 1.16，fitness 1.39，margin 30.7‱，selfCorrelation 0.199，prodCorrelation 0.506。使用了subindustry、opt1_factor字段,用了基于行业横截面的统计特征策略策略。
第3个alpha是'EUR/D1/PV'的，sharpe 1.70，fitness 1.34，margin 25.5‱，selfCorrelation 0.537，prodCorrelation 0.600。使用了pv87_daily_ann_matrix_r1_revenue_consensus_mean_numup字段,用了基于分析师预期的动量策略策略。

总结：prodCorrelation有些超标，创新性不足, 今天的alpha质量挺好的，fitness指标很给力, 最近看了不少paper，希望能有所启发。

============================================================

---

### 探讨 #140: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月30日
----------------------------------------
今天是2025年7月30日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/NEWS'的，sharpe 1.98，fitness 1.44，margin 13.6‱，selfCorrelation 0.439，prodCorrelation 0.901。使用了nws7_eur_news_earning_qerf、oth176_lmt_close_eq_score字段,用了基于技术指标的趋势跟踪策略策略。
第2个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 1.72，fitness 0.98，margin 16.9‱，selfCorrelation 0.411，prodCorrelation 0.635。使用了scl12_sentiment、anl39_spvbq字段,用了基于时间序列动量的技术分析策略策略。
第3个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.44，fitness 0.88，margin 20.5‱，selfCorrelation 0.295，prodCorrelation 0.510。使用了snt27_relpopularity1字段,用了基于时间序列形态的偏度策略策略。
第4个alpha是'EUR/D1/EARNINGS'的，sharpe 1.16，fitness 0.55，margin 9.3‱，selfCorrelation 0.291，prodCorrelation 0.550。使用了ern3_pre_interval字段,用了基于历史表现的动量追踪策略策略。

总结：sharpe指标平平无奇，还行吧, 希望这些alpha能经受住时间的考验。

============================================================

---

### 探讨 #141: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年7月31日
----------------------------------------
今天是2025年7月31日，今天一共提交了1个alpha

今日alpha:'GLB/D1/OTHER'的，sharpe 1.12，fitness 0.62，margin 61.3‱，selfCorrelation 0.460，prodCorrelation 0.998。使用了oth455_partner_n2v_p50_q200_w4_pca_fact2_value字段,用了基于因子变化的动量策略策略。

总结：今天的fitness表现不佳，有待改进, prodCorrelation有些超标，创新性不足, 最近的alpha都比较保守，需要更大胆一些。

============================================================

---

### 探讨 #142: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月1日
----------------------------------------
今天是2025年8月1日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/MODEL'的，sharpe 2.72，fitness 2.14，margin 14.1‱，selfCorrelation 0.495，prodCorrelation 0.746。使用了mdl77_dvm_dvm_eur_composite、subindustry字段,用了基于行业相对强度的均值回归策略策略。
第2个alpha是'EUR/D1/MODEL'的，sharpe 2.02，fitness 1.77，margin 15.3‱，selfCorrelation 0.310，prodCorrelation 0.509。使用了oth176_malta_eq_score字段,用了基于量化因子的信息比策略策略。
第3个alpha是'ASI/D1/INSTITUTIONS'的，sharpe 1.24，fitness 0.71，margin 19.5‱，selfCorrelation 0.616，prodCorrelation 0.935。使用了inst14_shorttotal、oth176_lmt_close_eq_score字段,用了基于时间序列动量的趋势跟踪策略策略。
第4个alpha是'EUR/D1/OPTION'的，sharpe 1.18，fitness 1.55，margin 210.7‱，selfCorrelation 0.153，prodCorrelation 0.389。使用了subindustry、opt1_price_close字段,用了基于行业排名的统计特征策略策略。

总结：今天的alpha fitness表现优秀，值得肯定, 最近的学习让我对风险管理有了新想法,啥时候想法会执行呢?咱也不知道啊。

============================================================

---

### 探讨 #143: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月2日
----------------------------------------
今天是2025年8月2日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/ANALYST'的，sharpe 1.79，fitness 1.20，margin 28.6‱，selfCorrelation 0.420，prodCorrelation 0.929。使用了anl39_rygnhcspe字段,用了基于对数变换的因子处理策略策略。
第2个alpha是'ASI/D1/MODEL'的，sharpe 1.91，fitness 1.40，margin 15.8‱，selfCorrelation 0.258，prodCorrelation 0.704。使用了shrt38_subindustry、star_val_sector_rank字段,用了基于标准化价格极差的技术指标策略策略。

总结：今天提交的alpha都还过得去，fitness表现不错, prodCorrelation有点高，因子可能烂大街了, 希望这些因子能在OS中表现稳定。

============================================================

---

### 探讨 #144: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月3日
----------------------------------------
今天是2025年8月3日，今天一共提交了2个alpha

第1个alpha是'USA/D1/SHORTINTEREST'的，sharpe 1.67，fitness 1.07，margin 28.1‱，selfCorrelation 0.398，prodCorrelation 0.830。使用了shrt17_officer_cao_total_share_owned、mdl136_qes_etf_us_flow_out_pctvol_1w字段,用了基于技术指标的反转策略。
第2个alpha是'USA/D1/SHORTINTEREST'的，sharpe 1.81，fitness 0.99，margin 25.0‱，selfCorrelation 0.423，prodCorrelation 0.842。使用了shrt17_gen_counsel_total_share_owned、mdl77_ohistoricalgrowthfactor_fcfequity字段,用了基于技术指标的趋势捕捉策略。

总结：今天的sharpe中规中矩, 希望能找到更多低相关性的因子。

============================================================

---

### 探讨 #145: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月4日
----------------------------------------
今天是2025年8月4日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/RISK'的，sharpe 2.10，fitness 1.25，margin 20.7‱，selfCorrelation 0.438，prodCorrelation 0.9888。使用了rsk70_mfm2_euetrd_shortint字段,用了基于反向排序的风险调整反转策略策略。
第2个alpha是'GLB/D1/FUNDAMENTAL'的，sharpe 1.93，fitness 1.12，margin 34.2‱，selfCorrelation 0.907，prodCorrelation 0.907。使用了fnd23_intfvalld1_ctcv字段,用了基于标准化财务因子的趋势策略策略。
第3个alpha是'GLB/D1/MODEL'的，sharpe 1.60，fitness 0.82，margin 26.7‱，selfCorrelation 0.431，prodCorrelation 0.638。使用了mdl138_longsimeq_qpdi5_op_margin字段,用了基于技术指标的动量增强策略策略。
第4个alpha是'USA/D1/MACRO'的，sharpe 1.51，fitness 1.00，margin 20.5‱，selfCorrelation 0.420，prodCorrelation 0.658。使用了mcr55_decimals字段,用了基于模型预测的动量策略策略。

总结：今天的alpha fitness勉强及格, 今天的prodCorrelation让人头疼，缺乏独特性, 最近的研究让我对alpha decay有了新认识。

============================================================

---

### 探讨 #146: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月5日
----------------------------------------
今天是2025年8月5日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 2.35，fitness 1.57，margin 19.5‱，selfCorrelation 0.952，prodCorrelation 0.952。使用了anl39_qtanbvps、shrt3_utilizationpercent_units字段,用了基于时序极值定位的动量策略策略。
第2个alpha是'EUR/D1/NEWS'的，sharpe 1.04，fitness 0.47，margin 16.6‱，selfCorrelation 0.371，prodCorrelation 0.528。使用了rp_css_assets字段,用了基于时间序列动量的技术策略策略。
第3个alpha是'USA/D1/SOCIALMEDIA'的，sharpe 1.26，fitness 0.72，margin 29.8‱，selfCorrelation 0.374，prodCorrelation 0.825。使用了snt_social_volume、mdl109_rg_sp_et字段,用了基于时间序列动量的趋势跟踪策略策略。
第4个alpha是'USA/D1/MODEL'的，sharpe 1.44，fitness 0.72，margin 12.5‱，selfCorrelation 0.404，prodCorrelation 0.799。使用了snt1_d1_sellrecpercent、mdl77_valueanalystmodel_ccaghc_avq字段,用了基于技术指标的趋势跟踪策略策略。

总结：prodCorrelation好高，策略同质化严重, 今天的alpha fitness还算可以, 今天效率不错，明天争取更上一层楼。

============================================================

---

### 探讨 #147: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月6日
----------------------------------------
今天是2025年8月6日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/INSTITUTIONS'的，sharpe 1.64，fitness 1.00，margin 19.9‱，selfCorrelation 0.493，prodCorrelation 0.820。使用了inst14_longstdcomp、oth532_spret字段,用了基于时间序列复杂度的反转策略策略。
第2个alpha是'ASI/D1/RISK'的，sharpe 1.19，fitness 0.62，margin 24.6‱，selfCorrelation 0.359，prodCorrelation 0.537。使用了ern3_all_delay_1_next_reptime、rsk70_mfm2_asetrd_earnyild字段,用了基于技术指标的偏度动量策略策略。
第3个alpha是'ASI/D1/SOCIALMEDIA'的，sharpe 1.56，fitness 0.96，margin 19.7‱，selfCorrelation 0.194，prodCorrelation 0.984。使用了scl39_top5_people_also_watch_ticker_ii、snt27_totaldomains_29字段,用了基于时间序列极值统计的标准化策略策略。
第4个alpha是'GLB/D1/SOCIALMEDIA'的，sharpe 1.36，fitness 0.60，margin 16.1‱，selfCorrelation 0.288，prodCorrelation 0.496。使用了scl12_buzz、nws23_acquiror_apr1dayb字段,用了基于技术指标的趋势跟踪策略策略。

总结：今天的alpha fitness偏弱，得想想办法, sharpe表现一般般, 希望这些因子能在OS中表现稳定。

============================================================

---

### 探讨 #148: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月7日
----------------------------------------
今天是2025年8月7日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/OTHER'的，sharpe 1.44，fitness 1.12，margin 12.0‱，selfCorrelation 0.127，prodCorrelation 0.349。使用了oth532_asia_ase2_monthly_specificreturn字段,用了基于标准化价格变动的动量策略策略。
第2个alpha是'ASI/D1/INSIDERS'的，sharpe 1.29，fitness 1.03，margin 27.6‱，selfCorrelation 0.239，prodCorrelation 0.385。使用了insd1_price字段,用了基于标准化时间序列变化的动量策略策略。
第3个alpha是'ASI/D1/INSIDERS'的，sharpe 1.21，fitness 0.73，margin 20.1‱，selfCorrelation 0.096，prodCorrelation 0.283。使用了insd1_holdings字段,用了基于标准化时间序列的动量策略策略。
第4个alpha是'ASI/D1/ANALYST'的，sharpe 1.45，fitness 0.88，margin 17.1‱，selfCorrelation 0.451，prodCorrelation 0.868。使用了anl9_consensusanalysis_dataitemvalue字段,用了基于标准化时间序列的动量策略策略。

总结：sharpe表现一般般, 最近压力有点大，但还是要坚持下去。

============================================================

---

### 探讨 #149: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月8日
----------------------------------------
今天是2025年8月8日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/SOCIALMEDIA'的，sharpe 1.14，fitness 1.28，margin 25.3‱，selfCorrelation 0.074，prodCorrelation 0.274。使用了scl15_emotionvsfact字段,用了基于时间序列动量的趋势跟踪策略策略。
第2个alpha是'USA/D1/SOCIALMEDIA'的，sharpe 1.07，fitness 0.66，margin 69.5‱，selfCorrelation 0.183，prodCorrelation 0.729。使用了scl4_videos_total_yt字段,用了基于时间序列平滑处理的动量策略策略。
第3个alpha是'USA/D1/PV'的，sharpe 1.60，fitness 1.02，margin 10.8‱，selfCorrelation 0.184，prodCorrelation 0.823。使用了pv52_yse_shares_10_29_sec字段,用了基于时间序列处理的动量增强策略策略。
第4个alpha是'USA/D1/SENTIMENT'的，sharpe 1.36，fitness 0.94，margin 10.9‱，selfCorrelation 0.096，prodCorrelation 0.491。使用了snt27_dltcc_3字段,用了基于技术指标的趋势跟踪策略策略。

总结：今天的prodCorrelation中规中矩, 今天的alpha fitness还算可以, 最近worldquant新东西很多，需要多学习。

---

### 探讨 #150: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月9日
----------------------------------------
今天是2025年8月9日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/SENTIMENT'的，sharpe 2.08，fitness 2.09，margin 20.2‱，selfCorrelation 0.149，prodCorrelation 0.447。使用了snt27_topranking_23字段,用了基于时间序列动量的动量策略策略。
第2个alpha是'USA/D1/MACRO'的，sharpe 1.59，fitness 1.07，margin 9.0‱，selfCorrelation 0.471，prodCorrelation 0.927。使用了mcr38_low、ern4_120dclshv字段,用了基于技术指标的趋势跟踪策略策略。
第3个alpha是'EUR/D1/RISK'的，sharpe 1.47，fitness 1.24，margin 14.3‱，selfCorrelation 0.464，prodCorrelation 0.862。使用了rsk59_bid_rate字段,用了基于订单簿反转信号的逆向策略策略。
第4个alpha是'USA/D1/EARNINGS'的，sharpe 1.06，fitness 0.50，margin 12.8‱，selfCorrelation 0.485，prodCorrelation 0.763。使用了ern1_tse_spe字段,用了基于时间序列调整的动量策略策略。

总结：今天的alpha质量挺好的，fitness指标很给力, prodCorrelation数据不太妙，大家想法都差不多, 今天尝试了一些新的特征工程方法。

---

### 探讨 #151: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月10日
----------------------------------------
今天是2025年8月10日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/MODEL'的，sharpe 2.37，fitness 1.44，margin 18.3‱，selfCorrelation 0.309，prodCorrelation 0.827。使用了shrt38_subindustry、mdl138_5idpc字段,用了基于技术指标的标准分数策略策略。
第2个alpha是'ASI/D1/NEWS'的，sharpe 1.17，fitness 0.91，margin 12.1‱，selfCorrelation 0.063，prodCorrelation 0.387。使用了nws7_livenews_all_time字段,用了基于新闻情绪的技术指标策略策略。
第3个alpha是'ASI/D1/RISK'的，sharpe 1.60，fitness 0.86，margin 13.3‱，selfCorrelation 0.245，prodCorrelation 0.982。使用了rsk70_mfm2_asetrd_ltrevrsl字段,用了基于技术指标的反转策略策略。
第4个alpha是'EUR/D1/NEWS'的，sharpe 1.63，fitness 0.77，margin 15.4‱，selfCorrelation 0.272，prodCorrelation 0.973。使用了nws79_event_sentiment_141字段,用了基于事件情绪的时间序列动量策略策略。

总结：今天的alpha fitness还算可以, sharpe数据不温不火, 最近的学习让我对量化有了新的理解。

---

### 探讨 #152: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月11日
----------------------------------------
今天是2025年8月11日，今天一共提交了4个alpha

第1个alpha是'GLB/D1/RISK'的，sharpe 1.31，fitness 0.65，margin 16.7‱，selfCorrelation 0.391，prodCorrelation 0.562。使用了rsk70_mfm2_gemtrd_resvol字段,用了基于波动率调整的标准化策略策略。
第2个alpha是'GLB/D1/RISK'的，sharpe 1.54，fitness 0.82，margin 18.9‱，selfCorrelation 0.105，prodCorrelation 0.530。使用了rsk70_mfm2_gemtrd_indmom字段,用了基于技术指标的动量策略策略。
第3个alpha是'ASI/D1/NEWS'的，sharpe 1.87，fitness 1.03，margin 16.3‱，selfCorrelation 0.455，prodCorrelation 0.723。使用了nws79_credit_sentiment_182字段,用了基于标准化时间序列的均值回归策略策略。
第4个alpha是'ASI/D1/EARNINGS'的，sharpe 2.00，fitness 1.07，margin 13.1‱，selfCorrelation 0.365，prodCorrelation 0.767。使用了ern3_next_reptime、mdl138_qpdi4_gross_margin字段,用了基于财务指标的标准化时序策略策略。

总结：sharpe表现一般般, 努力稳住六维.

---

### 探讨 #153: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月12日
----------------------------------------
今天是2025年8月12日，今天一共提交了4个alpha

第1个alpha是'ASI/D1/ANALYST'的，sharpe 1.32，fitness 0.71，margin 21.4‱，selfCorrelation 0.382，prodCorrelation 0.959。使用了subindustry、anl69_best_analyst_rating字段,用了基于分析师评级的行业中性动量策略策略。
第2个alpha是'USA/D1/SHORTINTEREST'的，sharpe 1.98，fitness 2.74，margin 57.6‱，selfCorrelation 0.421，prodCorrelation 0.669。使用了shrt10_730_standalone_syn、opt23_ivydb_trans_iv_weight_avg_volivcallmputs3字段,用了基于波动率的技术指标策略策略。
第3个alpha是'GLB/D1/SHORTINTEREST'的，sharpe 1.66，fitness 1.07，margin 72.3‱，selfCorrelation 0.455，prodCorrelation 0.689。使用了star_si_insown_pct、fnd23_intfvalld1_vacl字段,用了基于标准化时间序列的趋势跟踪策略策略。
第4个alpha是'GLB/D1/RISK'的，sharpe 1.21，fitness 0.70，margin 28.2‱，selfCorrelation 0.408，prodCorrelation 0.602。使用了rsk70_mfm2_gemtrd_cnt_usa字段,用了基于时间序列统计特征的波动率策略策略。

总结：今天的sharpe勉强过得去, good good study, day day up!。

---

### 探讨 #154: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月13日
----------------------------------------
今天是2025年8月13日，今天一共提交了3个alpha

第1个alpha是'ASI/D1/EARNINGS'的，sharpe 2.42，fitness 1.35，margin 15.3‱，selfCorrelation 0.194，prodCorrelation 0.695。使用了ern3_all_delay_1_pre_reptime、mdl138_4idpqc字段,用了基于标准化时间序列动量的策略策略。
第2个alpha是'ASI/D1/RISK'的，sharpe 1.62，fitness 1.27，margin 23.2‱，selfCorrelation 0.402，prodCorrelation 0.998。使用了rsk70_mfm2_asetrd_ltrevrsl字段,用了基于市场微观结构的反转策略策略。
第3个alpha是'ASI/D1/ANALYST'的，sharpe 1.46，fitness 0.93，margin 19.5‱，selfCorrelation 0.329，prodCorrelation 0.645。使用了shrt38_z_sec_relsec_cd、anl14_low_ebit_fy1字段,用了基于标准化指标变化的动量策略策略。

总结：今天的alpha fitness勉强及格, prodCorrelation有些超标，创新性不足, 最近压力有点大，但还是要坚持下去。

---

### 探讨 #155: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月14日
----------------------------------------
今天是2025年8月14日，今天一共提交了4个alpha

第1个alpha是'GLB/D1/NEWS'的，sharpe 1.07，fitness 0.52，margin 21.9‱，selfCorrelation 0.199，prodCorrelation 0.584。使用了nws20_event_end_time_utc字段,用了基于事件持续性的波动率策略策略。
第2个alpha是'EUR/D1/OPTION'的，sharpe 1.15，fitness 1.63，margin 40.2‱，selfCorrelation 0.115，prodCorrelation 0.886。使用了opt1_factor字段,用了基于时间序列极值的动量策略策略。
第3个alpha是'GLB/D1/EARNINGS'的，sharpe 1.25，fitness 0.85，margin 106.0‱，selfCorrelation 0.466，prodCorrelation 0.860。使用了ern3_pre_interval字段,用了基于时间序列均值的趋势跟踪策略策略。
第4个alpha是'USA/D1/PV'的，sharpe 1.23，fitness 0.79，margin 8.3‱，selfCorrelation 0.491，prodCorrelation 0.821。使用了adv20、snt33_1_event_title字段,用了基于时间序列特征的趋势跟踪策略策略。

总结：prodCorrelation数据不太妙，大家想法都差不多, 因子好难找啊啊啊啊啊啊啊。

---

### 探讨 #156: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月15日
----------------------------------------
今天是2025年8月15日，今天一共提交了3个alpha

第1个alpha是'ASI/D1/NEWS'的，sharpe 1.08，fitness 0.53，margin 21.2‱，selfCorrelation 0.196，prodCorrelation 0.565。使用了nws79_credit_sentiment_182字段,用了基于标准化时间序列的平滑策略策略。
第2个alpha是'ASI/D1/SENTIMENT'的，sharpe 1.00，fitness 0.74，margin 11.0‱，selfCorrelation 0.178，prodCorrelation 0.380。使用了snt27_top75pctrankingavg_36字段,用了基于技术指标的趋势跟踪策略策略。
第3个alpha是'USA/D1/MACRO'的，sharpe 1.61，fitness 0.91，margin 7.1‱，selfCorrelation 0.147，prodCorrelation 0.480。使用了market、insd4_total、mcr27_bucket_daily_jobsactive字段,用了基于时间序列排名的动量策略策略。

总结：fitness指标不太理想，需要再优化一下, 但我,懒得优化...

---

### 探讨 #157: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月16日
----------------------------------------
今天是2025年8月16日，今天一共提交了4个alpha

第1个alpha是'EUR/D1/ANALYST'的，sharpe 1.24，fitness 0.75，margin 27.4‱，selfCorrelation 0.476，prodCorrelation 0.695。使用了est_12m_roe_raisednum_4wks字段,用了基于财务质量与市场情绪的反转策略策略。
第2个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 2.95，fitness 2.04，margin 9.6‱，selfCorrelation 0.369，prodCorrelation 0.675。使用了subindustry、scl15_d1_timeurgency、anl69_best_cur_ev_to_ebitda字段,用了基于行业相对强度的均值回归策略策略。
第3个alpha是'GLB/D1/PV'的，sharpe 1.57，fitness 1.32，margin 117.9‱，selfCorrelation 0.496，prodCorrelation 0.653。使用了ern3_pre_interval、adv20字段,用了基于成交量加权的价格动量策略策略。
第4个alpha是'EUR/D1/EARNINGS'的，sharpe 1.70，fitness 1.10，margin 48.2‱，selfCorrelation 0.441，prodCorrelation 0.700。使用了ern3_pre_reptime、mdl77_qvm_estrevrank_qmaeur、subindustry字段,用了基于行业动量的高阶矩策略策略。

总结：今天提交的alpha都还过得去，fitness表现不错, 最近看了不少paper，希望能有所启发。

---

### 探讨 #158: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月17日
----------------------------------------
今天是2025年8月17日，今天一共提交了3个alpha

第1个alpha是'GLB/D1/OPTION'的，sharpe 1.76，fitness 1.38，margin 12.3‱，selfCorrelation 0.449，prodCorrelation 0.796。使用了opt4_shareoutstanding、shrt7_shortlasso30d字段,用了基于技术指标的趋势跟踪策略策略。
第2个alpha是'EUR/D1/EARNINGS'的，sharpe 1.15，fitness 0.59，margin 14.4‱，selfCorrelation 0.380，prodCorrelation 0.727。使用了ern3_pre_interval字段,用了基于时间序列极值的动量策略策略。
第3个alpha是'GLB/D1/NEWS'的，sharpe 1.14，fitness 0.77，margin 55.7‱，selfCorrelation 0.449，prodCorrelation 0.976。使用了nws23_acquiror_saleslltm字段,用了基于技术指标的均值回归策略策略。

总结：prodCorrelation有些超标，创新性不足, fitness数据一般般，不算太差, 今天的回测结果超出了我的预期。

============================================================

---

### 探讨 #159: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月18日
----------------------------------------
今天是2025年8月18日，今天一共提交了1个alpha

今日alpha:'EUR/D1/MACRO'的，sharpe 2.16，fitness 1.43，margin 10.1‱，selfCorrelation 0.391，prodCorrelation 0.605。使用了mcr10_value、star_eq_rank字段,用了基于时间序列形态的动量策略策略。

总结：fitness指标达标了，今天的alpha质量在线, prodCorrelation也还可以的,不错不错.

============================================================

---

### 探讨 #160: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月19日
----------------------------------------
今天是2025年8月19日，今天一共提交了1个alpha

今日alpha:'EUR/D1/ANALYST'的，sharpe 2.40，fitness 1.57，margin 15.5‱，selfCorrelation 0.889，prodCorrelation 0.889。使用了est_12m_gps_raisednum_4wks字段,用了基于极端值处理的反向选择策略策略。

总结：今天的sharpe很给力，收益风险比不错, 但是自相关性怎么会这么高?????????是不是欺负老实人!

============================================================

---

### 探讨 #161: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月22日
----------------------------------------
今天是2025年8月22日，今天一共提交了1个alpha

今日alpha:'ASI/D1/SOCIALMEDIA'的，sharpe 1.96，fitness 1.26，margin 22.6‱，selfCorrelation 0.359，prodCorrelation 0.735。使用了fnd65_allcap_sedol_pu、scl39_top5_people_also_watch_ticker_ii字段,用了基于标准化时间序列变化的动量策略策略。

总结：今天的alpha质量挺好的，fitness指标很给力, 就是PROD高了一点点.....今天效率不错，明天争取更上一层楼。

============================================================

---

### 探讨 #162: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 9个月前

2025年8月23日
----------------------------------------
今天是2025年8月23日，今天一共提交了1个alpha

今日alpha:'ASI/D1/INSTITUTIONS'的，sharpe 1.80，fitness 0.97，margin 11.6‱，selfCorrelation 0.312，prodCorrelation 0.552。使用了inst14_shorttotalcomp、subindustry字段,用了基于行业排名的标准化动量策略策略。

总结：今天的prodCorrelation中规中矩, fitness表现中规中矩，还有提升空间, 最近的工作让我对机器学习更感兴趣。

============================================================

---

### 探讨 #163: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

日记还是要好好写

今天知道了 OS 是一个巨大的黑盒 借着 PPAC 交了不少因子，喜提 base 下限，这么搞，OS 要崩啊

交了一个sharpe 1.3  returns 36% margin 200+的alpha  OS是爆炸还是爆发   很难说

今日想刷 PYR,PYR 加 1.

倦怠期也要好好交因子 什么时候可以上 GM 啊

USA FND 区域红了 正好跳出舒适区 过个季度再见了

vf 0.23 - vf 0.42 何时出狱？

还得加油努力

今天提交了第一个自己的super alpha, 确实, 越早交越好, 可以改善自己的Performance Comparison. 感谢各位大佬的帖子, 组SA的时候, 获益良多.

今天combined从0.1涨到0.72, selected从0.12涨到1.33.猝不及防,躺平了这么久,才发现,要是努努力,也许可以冲刺GM的.也许,这就是生活吧.但是不可否认,这期间还是有努力过的,功不唐捐功不唐捐.

交了第二个 SA, 多交 RA, 早日实现 VF0.9 以上！

五一结束 收收心挖矿了
combined更新到了1.63了  select没什么大的变化啊  坚持日更日记-0612

---

### 探讨 #164: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

日记还是要好好写

今天知道了 OS 是一个巨大的黑盒 借着 PPAC 交了不少因子，喜提 base 下限，这么搞，OS 要崩啊

交了一个sharpe 1.3  returns 36% margin 200+的alpha  OS是爆炸还是爆发   很难说

今日想刷 PYR,PYR 加 1.

倦怠期也要好好交因子 什么时候可以上 GM 啊

USA FND 区域红了 正好跳出舒适区 过个季度再见了

vf 0.23 - vf 0.42 何时出狱？

还得加油努力

今天提交了第一个自己的super alpha, 确实, 越早交越好, 可以改善自己的Performance Comparison. 感谢各位大佬的帖子, 组SA的时候, 获益良多.

今天combined从0.1涨到0.72, selected从0.12涨到1.33.猝不及防,躺平了这么久,才发现,要是努努力,也许可以冲刺GM的.也许,这就是生活吧.但是不可否认,这期间还是有努力过的,功不唐捐功不唐捐.

交了第二个 SA, 多交 RA, 早日实现 VF0.9 以上！

五一结束 收收心挖矿了
combined更新到了1.63了  select没什么大的变化啊  坚持日更日记-0612
今日早起交alpha,早期的矿工能挖到矿-0613

---

### 探讨 #165: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

今天偶然看到YK大佬的跳动因子, 感觉很不错, 如果拓展模板的话, 或许可以试试把一日的时间修改.比如7天.
那么表达式可以这么写:

a = datafield /  last_diff_value(datafield, 7) - 1;

b = 1 -  abs(ts_max(datafield, 7) / datafield - 1 );

zscore(a)*zascore(b);
以上可以把数字7改成21,63,126,252等数;

只挖坑,不填坑,有兴趣的同学可以尝试.如果有信号,麻烦说一下, 如果没有信号,千万不要打我.
经验+3,深藏功与名.

---

### 探讨 #166: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

Genius到了最后冲刺阶段, 老实说按照现在的六维来拼,我感觉不是很科学, 因为alpha avg field和alpha avg operator的存在, 去复现部分模板,显得没有意义,虽然出来的因子可能更具备经济解释性,但是对于Genius可能就是反向提升了.当然,这就是从我个人角度出发看到的情况,或许从WQ的角度,是非常希望看到目前这样的结果的.
===================================================================
===================================================================
===================================================================

这搞得比上班还卷啊

---

### 探讨 #167: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

今天交了4个alpha,兢兢业业直到这赛季结束.但是也好久没有使用新模板了,每天从回测过的alpha里面找因子,确实有,但是已经没有很强的多样性了.还得要使用新的模板才可以,今天用了一下小改的一二三阶,能出alpha,就是效率不太高,想去看研报吧,又受限于复现时候的操作符过多,好麻烦.希望Genius有个好结果,那样有两个月缓冲,可以沉淀一下搞点新东西.

======================================================================
功不唐捐

---

### 探讨 #168: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

今天交了GLB的因子,看了一下自己的PPA rank,基本上排名都在100左右,AC ir勉强是正数.但是最近几天越来越发现,提交的因子对自己的combined comparision没有提升, 一味地降低分数.确实这两个月比较懒,没有怎么研究新alpha,全是在以前用的alpha模板里面找东西,现在是越来越同质化了.但是以前的模板操作符和字段少啊,才可以适配现在的Genius,再坚持一段时间吧.
===================================功不唐捐=================================

---

### 探讨 #169: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

还在卷Genius
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
真的,我以后一定每个月兢兢业业交super alpha

---

### 探讨 #170: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

Genius比赛最后只剩下四天了,看了一下,alpha这几天交的不多了.学习了一下SA的官方文档,才知道以前对SA理解有偏差,它里面的东西大有可为的,一定要好好研究,做到每一天都提交SA.
=======================希望这次Combined更新能到2=====================

---

### 探讨 #171: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

季度结束倒数第二天 今天交了一个SA RA还在努力
+++++++++++++++++++++++许愿combined大于2++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

---

### 探讨 #172: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年10月28日
----------------------------------------
今天是2025年10月28日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/EARNINGS'的，sharpe 1.24，fitness 0.86，margin 48.1‱，selfCorrelation 0.376，prodCorrelation 0.843。使用了ern3_next_interval字段,用了基于预期收益趋势的动量方法。
第2个alpha是'EUR/D1/RISK'的，sharpe 1.12，fitness 0.56，margin 18.7‱，selfCorrelation 0.363，prodCorrelation 0.496。使用了rsk88_mfm_eue4_ri_divyield字段,用了基于风险调整股息率的动量方法。

总结：这个fitness数据让人有点焦虑, 脑子里有几个策略想法，希望能尽快落地测试，转化成实际收益。

============================================================

---

### 探讨 #173: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年10月29日
----------------------------------------
今天是2025年10月29日，今天一共提交了2个alpha

第1个alpha是'USA/D1/IMBALANCE'的，sharpe 1.30，fitness 0.78，margin 10.3‱，selfCorrelation 0.230，prodCorrelation 0.700。使用了oth551_beta_usmv、imb5_mktcap、subindustry字段,用了基于行业中性化的时序动量方法。
第2个alpha是'GLB/D1/MODEL'的，sharpe 2.95，fitness 2.05，margin 9.7‱，selfCorrelation 0.377，prodCorrelation 0.779。使用了mdl138_longsimeq_5idpc字段,用了基于模型预测异常的统计套利方法。

总结：这波sharpe指标相当稳健，令人满意, 盯着回测曲线看了半天，发现因子在某些月份表现差，得找原因。

============================================================

---

### 探讨 #174: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年10月30日
----------------------------------------
今天是2025年10月30日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/SHORTINTEREST'的，sharpe 1.62，fitness 0.75，margin 38.1‱，selfCorrelation 0.420，prodCorrelation 0.696。使用了industry、shrt2_t12m_volatility_rank、oth455_partner_n2v_p50_q200_w5_pca_fact3_value字段,用了基于行业网络价值的相对强弱排序。
第2个alpha是'EUR/D1/MACRO'的，sharpe 1.86，fitness 1.30，margin 14.7‱，selfCorrelation 0.388，prodCorrelation 0.580。使用了mcr10_value、anl4_sadaf_netprofit_low、industry字段,用了基于行业相对盈利动量的增强方法。

总结：fitness表现尚可，继续努力吧, 又交了2个alpha，虽然效果一般，但保持更新节奏总没错。

============================================================

---

### 探讨 #175: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年10月31日
----------------------------------------
今天是2025年10月31日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 1.58，fitness 1.26，margin 26.0‱，selfCorrelation 0.421，prodCorrelation 0.467。使用了scl12_buzz、anl4_adz_ebit_mean字段,用了基于分析师预期与市场情绪的多因子动量。
第2个alpha是'EUR/D1/ANALYST'的，sharpe 1.73，fitness 1.46，margin 14.2‱，selfCorrelation 0.397，prodCorrelation 0.561。使用了anl8_eur_ibessplitptg_d1_value字段,用了基于分析师预期修正的长期趋势动量。

总结：今天的prodCorrelation勉强及格, 今天的alpha fitness表现优秀，值得肯定, 这周回测数量破了自己的记录，虽然累，但看着成果很开心。

============================================================

---

### 探讨 #176: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月1日
----------------------------------------
今天是2025年11月1日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/IMBALANCE'的，sharpe 1.72，fitness 1.34，margin 44.4‱，selfCorrelation 0.384，prodCorrelation 0.593。使用了imb5_mktcap、fnd23_intfvm_ltia字段,用了基于基本面动量的市值加权方法。
第2个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 1.60，fitness 1.07，margin 20.8‱，selfCorrelation 0.327，prodCorrelation 0.563。使用了fnd23_annfv1a_lctl、shrt3_bar字段,用了基于基本面与短期反转的复合方法。

总结：今天的prodCorrelation指标属于正常范围, 今天效率不错，明天争取更上一层楼。

============================================================

---

### 探讨 #177: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月2日
----------------------------------------
今天是2025年11月2日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/OTHER'的，sharpe 1.49，fitness 0.92，margin 14.4‱，selfCorrelation 0.230，prodCorrelation 0.772。使用了oth696_number_neutral_502字段,用了基于市场微观结构的反转方法。
第2个alpha是'GLB/D1/MACRO'的，sharpe 1.49，fitness 0.93，margin 18.5‱，selfCorrelation 0.380，prodCorrelation 0.504。使用了oth551_beta_mtum、fnd17_alldelay1_dvolshsout字段,用了基于成交量相对强度的平滑动量方法。

总结：今天的fitness指标平平无奇, 今天的sharpe指标属于正常范围, 今天的代码写得比较优雅，很有成就感。

============================================================

---

### 探讨 #178: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月3日
----------------------------------------
今天是2025年11月3日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.27，fitness 0.85，margin 41.7‱，selfCorrelation 0.205，prodCorrelation 0.402。使用了inst25_security_trade_count_1yr字段,用了基于机构交易行为变化的动量方法。
第2个alpha是'USA/D1/SOCIALMEDIA'的，sharpe 1.09，fitness 0.77，margin 28.9‱，selfCorrelation 0.309，prodCorrelation 0.701。使用了oth455_competitor_n2v_p50_q200_w3_pca_fact2_value、market、snt_social_volume字段,用了基于市场结构与情绪因子的排序方法。

总结：今天的fitness数据中规中矩, 最近看了不少paper，希望能有所启发。

============================================================

---

### 探讨 #179: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月4日
----------------------------------------
今天是2025年11月4日，今天一共提交了2个alpha

第1个alpha是'USA/D1/PV'的，sharpe 1.05，fitness 0.61，margin 7.7‱，selfCorrelation 0.431，prodCorrelation 0.660。使用了adv20、mws92_newsquantified_confidence字段,用了基于新闻情绪的时间序列动量方法。
第2个alpha是'EUR/D1/EARNINGS'的，sharpe 1.43，fitness 1.72，margin 28.9‱，selfCorrelation 0.120，prodCorrelation 0.552。使用了ern6_split_status_255字段,用了基于盈利预测修正偏度的动量方法。

总结：prodCorrelation有些超标，创新性不足, 这个sharpe水准确实需要提升, 今天调试了很久，终于找到了问题所在。

============================================================

---

### 探讨 #180: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月5日
----------------------------------------
今天是2025年11月5日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 1.28，fitness 0.96，margin 22.1‱，selfCorrelation 0.343，prodCorrelation 0.503。使用了scl12_sentiment、opt1_last_dvd_amount字段,用了基于期权行为与市场情绪的多因子方法。
第2个alpha是'EUR/D1/ANALYST'的，sharpe 1.40，fitness 1.13，margin 21.1‱，selfCorrelation 0.331，prodCorrelation 0.546。使用了anl39_spvba字段,用了基于价格极值变化的动量捕捉方法。

总结：fitness数据一般般，不算太差, sharpe表现尚可，继续努力吧, 希望这些alpha能在OS阶段表现良好。

============================================================

---

### 探讨 #181: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月6日
----------------------------------------
今天是2025年11月6日，今天一共提交了2个alpha

第1个alpha是'USA/D1/ANALYST'的，sharpe 1.33，fitness 1.11，margin 50.5‱，selfCorrelation 0.294，prodCorrelation 0.563。使用了anl82_preq_deltaprofitability_profitability3、subindustry字段,用了基于相对盈利能力排名的动量方法。
第2个alpha是'GLB/D1/MODEL'的，sharpe 2.16，fitness 1.10，margin 21.6‱，selfCorrelation 0.400，prodCorrelation 0.669。使用了mdl138_longsimeq_qpdi5_rnoa字段,用了基于相对估值极值的信号增强方法。

总结：今天的prodCorrelation让人头疼，缺乏独特性, 今天专注度超高，工作效率比昨天高了不少，提前完成任务。

============================================================

---

### 探讨 #182: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月7日
----------------------------------------
今天是2025年11月7日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/ANALYST'的，sharpe 1.39，fitness 0.72，margin 18.2‱，selfCorrelation 0.427，prodCorrelation 0.813。使用了anl16_meanrec字段,用了基于分析师预期一致性的趋势跟踪。
第2个alpha是'GLB/D1/MODEL'的，sharpe 2.55，fitness 1.82，margin 28.6‱，selfCorrelation 0.493，prodCorrelation 0.803。使用了mdl250_maltahc_eq_score字段,用了基于历史极值的均值回归方法。

总结：sharpe表现优异，风险管理做得好, 这波prodCorrelation确实有点不给力, 用了行业中性化处理后，因子的超额收益更明显了，这步没白做。

============================================================

---

### 探讨 #183: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月8日
----------------------------------------
今天是2025年11月8日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/FUNDAMENTAL'的，sharpe 2.21，fitness 1.43，margin 21.2‱，selfCorrelation 0.352，prodCorrelation 0.742。使用了fnd6_newqint_piq字段,用了基于基本面质量的长期动量方法。
第2个alpha是'GLB/D1/FUNDAMENTAL'的，sharpe 1.44，fitness 0.76，margin 17.2‱，selfCorrelation 0.329，prodCorrelation 0.706。使用了fnd6_int_ibmiiq字段,用了基于基本面质量的持续性分析方法。

总结：这个sharpe水准确实不错，点个赞, 研究了alpha decay 的规律后，调整了因子的持有周期，回测效果更好了。

============================================================

---

### 探讨 #184: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月9日
----------------------------------------
今天是2025年11月9日，今天一共提交了2个alpha

第1个alpha是'USA/D1/ANALYST'的，sharpe 1.39，fitness 1.45，margin 38.0‱，selfCorrelation 0.247，prodCorrelation 0.566。使用了anl82_preq_deltaprofitability_profitability3字段,用了基于基本面排名的动量方法。
第2个alpha是'USA/D1/INSTITUTIONS'的，sharpe 1.62，fitness 0.99，margin 14.6‱，selfCorrelation 0.432，prodCorrelation 0.768。使用了subindustry、inst9_adsv、anl83_analyst_sent_score_qa字段,用了基于分析师情绪与行业相对动量的复合方法。

总结：今天的alpha fitness让人刮目相看, 希望这波alpha能通过回测验证。

============================================================

---

### 探讨 #185: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月10日
----------------------------------------
今天是2025年11月10日，今天一共提交了2个alpha

第1个alpha是'USA/D1/OTHER'的，sharpe 1.35，fitness 1.21，margin 81.3‱，selfCorrelation 0.521，prodCorrelation 0.761。使用了oth455_competitor_roam_w4_pca_fact2_value字段,用了基于非线性信号增强的因子挖掘方法。
第2个alpha是'USA/D1/SENTIMENT'的，sharpe 1.30，fitness 0.98，margin 36.0‱，selfCorrelation 0.502，prodCorrelation 0.836。使用了market、snt7_universe_all_languagesaccess_type字段,用了基于情绪动量的相对强弱方法。

总结：今天的sharpe勉强过得去, 今天的fitness指标属于正常范围, 感觉数据挖掘的功力还需要提升。

============================================================

---

### 探讨 #186: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月11日
----------------------------------------
今天是2025年11月11日，今天一共提交了2个alpha

第1个alpha是'USA/D1/SHORTINTEREST'的，sharpe 1.66，fitness 1.12，margin 27.4‱，selfCorrelation 0.471，prodCorrelation 0.977。使用了shrt43_batssh_sumsize_s_data2、mdl264_pstk_class字段,用了基于会计数据时序平滑的分类预测。
第2个alpha是'EUR/D1/INSIDERS'的，sharpe 1.61，fitness 1.36，margin 39.7‱，selfCorrelation 0.449，prodCorrelation 0.649。使用了insd12_transactioncode、est_12m_sal_high_3mth_ago字段,用了基于预期动量的多因子融合方法。

总结：这波fitness数据相当稳健，令人满意, 今天的sharpe指标属于正常范围, 做统计检验的时候总出错，看来统计功底还得加强。

============================================================

---

### 探讨 #187: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月12日 ---------------------------------------- 今天是2025年11月12日，今天一共提交了2个alpha 第1个alpha是'EUR/D1/ANALYST'的，sharpe 1.72，fitness 1.03，margin 13.8‱，selfCorrelation 0.203，prodCorrelation 0.696。使用了anl94_find字段,用了基于极端动量的非线性反转方法。 第2个alpha是'EUR/D1/ANALYST'的，sharpe 1.11，fitness 0.80，margin 10.6‱，selfCorrelation 0.240，prodCorrelation 0.368。使用了rtk_ptg_low字段,用了基于平滑价格动量的趋势跟踪方法。 总结：sharpe表现平稳，没有太大惊喜, 这个fitness数据算是中等水准, 感觉自己的统计功底还需要加强。 ============================================================

---

### 探讨 #188: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月13日
----------------------------------------
今天是2025年11月13日，今天一共提交了2个alpha

第1个alpha是'USA/D1/ANALYST'的，sharpe 1.69，fitness 1.75，margin 47.9‱，selfCorrelation 0.519，prodCorrelation 0.712。使用了sector、anl82_delta_oprq_q2_madp字段,用了基于行业相对增长动量的稳定性方法。
第2个alpha是'USA/D1/ANALYST'的，sharpe 1.43，fitness 1.15，margin 39.0‱，selfCorrelation 0.477，prodCorrelation 0.824。使用了anl82_preq_deltaprofitability_profitability7字段,用了基于盈利能力趋势变化的量化选股。

总结：fitness数据看起来相当不错，今天收获满满, 下个月的量化比赛要开始了，现在就得打磨策略，争取当个好观众。

============================================================

---

### 探讨 #189: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月14日 
----------------------------------------
今天是2025年11月14日，今天一共提交了2个alpha 第1个alpha是'EUR/D1/INSIDERS'的，sharpe 1.80，fitness 1.02，margin 12.3‱，selfCorrelation 0.390，prodCorrelation 0.758。使用了insd12_mktprice、mdl37_broker_research字段,用了基于数据分布特征的稳健信号方法。 第2个alpha是'EUR/D1/FUNDAMENTAL'的，sharpe 1.33，fitness 0.90，margin 35.3‱，selfCorrelation 0.359，prodCorrelation 0.508。使用了fnd17_arecvbl字段,用了基于基本面指标的动量方法。 总结：今天的fitness指标不温不火, sharpe指标处于平均线附近, 新因子在回测里表现挺好，就怕 OS 阶段扛不住市场波动，有点忐忑。 ============================================================

---

### 探讨 #190: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月15日
----------------------------------------
今天是2025年11月15日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/MACRO'的，sharpe 1.06，fitness 0.76，margin 22.3‱，selfCorrelation 0.142，prodCorrelation 0.489。使用了mcr27_company_jobsactive字段,用了基于宏观经济因子的动量方法。
第2个alpha是'EUR/D1/MODEL'的，sharpe 1.43，fitness 0.70，margin 15.8‱，selfCorrelation 0.351，prodCorrelation 0.584。使用了mdl26_nnlyst_rvsng_dwn_fy1_rvn_30字段,用了基于历史财务预期的动量捕捉。

总结：今天的prodCorrelation数据中规中矩, 连续挖了 3 天因子都没达标，难啊难啊，再换个数据试试。

============================================================

---

### 探讨 #191: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月16日
----------------------------------------
今天是2025年11月16日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.40，fitness 1.83，margin 77.4‱，selfCorrelation 0.466，prodCorrelation 0.466。使用了snt27_relpopularity08字段,用了基于市场微观结构的动量与反转方法。
第2个alpha是'EUR/D1/EARNINGS'的，sharpe 1.07，fitness 0.56，margin 16.7‱，selfCorrelation 0.162，prodCorrelation 0.430。使用了country、ern3_pre_reptime字段,用了基于极端盈利动量的统计套利。

总结：今天的prodCorrelation勉强及格, 这个sharpe比率让人捏把汗, 希望明天能有更多的进展。

============================================================

---

### 探讨 #192: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月17日 
---------------------------------------- 
今天是2025年11月17日，今天一共提交了2个alpha 第1个alpha是'AMR/D1/SHORTINTEREST'的，sharpe 1.31，fitness 0.92，margin 9.8‱，selfCorrelation 0.065，prodCorrelation 0.178。使用了shrt31_numofshares、mws66_crawl_time字段,用了基于新闻量分布异常的预测方法。 第2个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.70，fitness 1.62，margin 18.1‱，selfCorrelation 0.140，prodCorrelation 0.456。使用了sector、snt27_relpopularity08字段,用了基于情绪分布异常度的预测方法。 总结：sharpe指标处于平均线附近, prodCorrelation指标达到了理想水平，很棒, 今天专注度超高，工作效率比昨天高了不少，提前完成任务。 
============================================================

---

### 探讨 #193: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月18日
----------------------------------------
今天是2025年11月18日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.26，fitness 0.62，margin 10.3‱，selfCorrelation 0.176，prodCorrelation 0.501。使用了io_fund_number字段,用了基于机构资金流量的动量择时。
第2个alpha是'EUR/D1/ANALYST'的，sharpe 2.15，fitness 1.30，margin 12.6‱，selfCorrelation 0.413，prodCorrelation 0.549。使用了est_12m_ebt_low字段,用了基于基本面数据的极端估值反转。

总结：今天的fitness指标平平无奇, 最近看了不少paper，希望能有所启发。

============================================================

---

### 探讨 #194: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月19日
----------------------------------------
今天是2025年11月19日，今天一共提交了2个alpha

第1个alpha是'AMR/D1/SHORTINTEREST'的，sharpe 1.31，fitness 1.05，margin 32.2‱，selfCorrelation 0.366，prodCorrelation 0.585。使用了shrt31_xst、nws18_ghc_lna字段,用了基于新闻情绪的市场择时。
第2个alpha是'USA/D1/OPTION'的，sharpe 2.04，fitness 1.56，margin 21.0‱，selfCorrelation 0.466，prodCorrelation 0.830。使用了industry、opt23_ise_trans_iv_weight_avg_volivcallmput4字段,用了基于行业相对隐含波动的异常检测。

总结：prodCorrelation数据不太乐观，需要突破, sharpe指标平平无奇，还行吧, 明天计划测试 3 个新因子，希望能有一个达标，哪怕效果一般也行。

============================================================

---

### 探讨 #195: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月20日
----------------------------------------
今天是2025年11月20日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/EARNINGS'的，sharpe 1.39，fitness 0.86，margin 20.9‱，selfCorrelation 0.215，prodCorrelation 0.433。使用了ern3_pre_reptime字段,用了基于盈利数据分布特征的波动率预测。
第2个alpha是'EUR/D1/IMBALANCE'的，sharpe 1.59，fitness 1.10，margin 11.1‱，selfCorrelation 0.232，prodCorrelation 0.414。使用了imb5_score字段,用了基于市场微观结构的动量与反转识别。

总结：sharpe指标处于平均线附近, 今天把上周的策略做完了，还优化了回测流程，算没白忙活。

============================================================

---

### 探讨 #196: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月21日
----------------------------------------
今天是2025年11月21日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/MODEL'的，sharpe 1.79，fitness 1.14，margin 19.8‱，selfCorrelation 0.465，prodCorrelation 0.616。使用了star_val_pcf字段,用了基于基本面估值指标的非对称性分析。
第2个alpha是'EUR/D1/ANALYST'的，sharpe 1.73，fitness 1.14，margin 10.8‱，selfCorrelation 0.399，prodCorrelation 0.804。使用了anl69_best_cur_fiscal_qtr_period字段,用了基于分析师预期修正的动量方法。

总结：这个prodCorrelation数据让人有点焦虑, sharpe指标平平无奇，还行吧, 今天检查因子是否有幸存者偏差，还好问题不大，稍微调整下就好。

============================================================

---

### 探讨 #197: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月22日
----------------------------------------
今天是2025年11月22日，今天一共提交了2个alpha

第1个alpha是'USA/D1/NEWS'的，sharpe 2.09，fitness 1.21，margin 14.8‱，selfCorrelation 0.332，prodCorrelation 0.936。使用了industry、se_score字段,用了基于行业情绪的相对强弱方法。
第2个alpha是'USA/D1/MODEL'的，sharpe 1.43，fitness 0.76，margin 11.2‱，selfCorrelation 0.482，prodCorrelation 0.760。使用了mdl77_oearningsqualityfactor_salerec字段,用了基于基本面趋势的动量方法。

总结：这个prodCorrelation水准确实需要改进, 希望能在这次Genius定级取得好结果。

============================================================

---

### 探讨 #198: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月23日
----------------------------------------
今天是2025年11月23日，今天一共提交了2个alpha

第1个alpha是'USA/D1/MODEL'的，sharpe 1.67，fitness 1.04，margin 80.6‱，selfCorrelation 0.544，prodCorrelation 0.886。使用了industry、mdl26_srprs_pct_lst_y_rvn字段,用了基于行业相对表现的基本面动量方法。
第2个alpha是'USA/D1/ANALYST'的，sharpe 1.86，fitness 1.97，margin 40.6‱，selfCorrelation 0.491，prodCorrelation 0.771。使用了anl16_estimate_d1_estnorm_estnormcuradj字段,用了基于分析师预期修正的趋势跟踪方法。

总结：今天的sharpe指标属于正常范围, fitness数据看起来相当不错，今天收获满满, 感觉需要更深入地理解市场微观结构。

============================================================

---

### 探讨 #199: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月24日
----------------------------------------
今天是2025年11月24日，今天一共提交了2个alpha

第1个alpha是'USA/D1/MODEL'的，sharpe 1.28，fitness 0.83，margin 48.6‱，selfCorrelation 0.421，prodCorrelation 0.687。使用了oth460_1l_qod字段,用了基于平滑趋势的相对价值方法。
第2个alpha是'AMR/D1/RISK'的，sharpe 1.27，fitness 1.25，margin 48.8‱，selfCorrelation 0.280，prodCorrelation 0.639。使用了snt21_2pos_mean_467、rsk88_mfm_cae5_srisk字段,用了基于风险与情绪因子的动态自适应反转。

总结：sharpe数据让人有点失望，风控需要加强, 今天想的因子思路有点离谱，但回测居然有正收益，值得深入挖。

============================================================

---

### 探讨 #200: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月25日
----------------------------------------
今天是2025年11月25日，今天一共提交了2个alpha

第1个alpha是'AMR/D1/SOCIALMEDIA'的，sharpe 1.60，fitness 1.41，margin 17.2‱，selfCorrelation 0.304，prodCorrelation 0.686。使用了scl15_stress、anl9_daily_numupunfiltered字段,用了基于趋势加速度与统计分布过滤的动量方法。
第2个alpha是'USA/D1/OTHER'的，sharpe 1.30，fitness 1.10，margin 41.4‱，selfCorrelation 0.392，prodCorrelation 0.601。使用了oth17_valid_asof字段,用了基于价格波动范围的技术指标方法。

总结：sharpe表现平稳，没有太大惊喜, 今天写的策略代码逻辑超清晰，注释也完整，看着就舒服，成就感拉满。

============================================================

---

### 探讨 #201: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月26日
----------------------------------------
今天是2025年11月26日，今天一共提交了2个alpha

第1个alpha是'AMR/D1/OTHER'的，sharpe 1.09，fitness 0.86，margin 24.5‱，selfCorrelation 0.181，prodCorrelation 0.379。使用了oth455_relation_n2v_p10_q200_w4_pca_fact1_value字段,用了基于跨资产关系的动量排序方法。
第2个alpha是'AMR/D1/SHORTINTEREST'的，sharpe 1.22，fitness 0.77，margin 7.9‱，selfCorrelation 0.272，prodCorrelation 0.639。使用了shrt3_utilizationpercent_units字段,用了基于市场微观结构与流动性的择时方法。

总结：prodCorrelation数据平平无奇, 最近的robust测试结果还算令人满意。

============================================================

---

### 探讨 #202: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月27日 ---------------------------------------- 今天是2025年11月27日，今天一共提交了2个alpha 第1个alpha是'AMR/D1/ANALYST'的，sharpe 1.59，fitness 1.39，margin 44.0‱，selfCorrelation 0.350，prodCorrelation 0.725。使用了snt23_2neut_conf_low_378、anl69_eqy_rec_cons字段,用了基于分析师共识的均值回归方法。 第2个alpha是'AMR/D1/SOCIALMEDIA'的，sharpe 1.66，fitness 1.93，margin 129.4‱，selfCorrelation 0.269，prodCorrelation 0.692。使用了fnd17_2anrhsfcq、scl15_lovehate字段,用了基于基本面动量的非线性增强方法。 总结：sharpe表现平稳，没有太大惊喜, 今天写的策略代码逻辑超清晰，注释也完整，看着就舒服，成就感拉满。 ============================================================

---

### 探讨 #203: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月28日 ---------------------------------------- 今天是2025年11月28日，今天一共提交了2个alpha 第1个alpha是'AMR/D1/RISK'的，sharpe 1.35，fitness 1.59，margin 27.9‱，selfCorrelation 0.342，prodCorrelation 0.675。使用了rsk62_1_100_val76字段,用了基于风险调整动量的非线性增强方法。 第2个alpha是'AMR/D1/MODEL'的，sharpe 1.61，fitness 1.29，margin 30.0‱，selfCorrelation 0.240，prodCorrelation 0.831。使用了oth176_malta_eq_score、industry字段,用了基于行业相对排名的横截面方法。 总结：今天的sharpe指标四平八稳, 今天做策略的时候，突然想起刚入门 “挖矿” 的冲劲，得保持这份热情。 ============================================================

---

### 探讨 #204: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月29日
----------------------------------------
今天是2025年11月29日，今天一共提交了2个alpha

第1个alpha是'AMR/D1/SENTIMENT'的，sharpe 1.31，fitness 1.12，margin 23.9‱，selfCorrelation 0.174，prodCorrelation 0.933。使用了snt27_rank_59字段,用了基于情绪不对称性的动量预测。
第2个alpha是'USA/D1/NEWS'的，sharpe 1.39，fitness 0.70，margin 19.5‱，selfCorrelation 0.452，prodCorrelation 0.746。使用了nws21_abz3az_neg_freq字段,用了基于新闻情绪极值的择时方法。

总结：这个sharpe数据算是中等水准, 今天做了因子的换手率分析，结果比预期低，这样实盘交易成本能控制住吗。

============================================================

---

### 探讨 #205: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年11月30日
----------------------------------------
今天是2025年11月30日，今天一共提交了2个alpha

第1个alpha是'USA/D1/ANALYST'的，sharpe 1.55，fitness 1.13，margin 18.3‱，selfCorrelation 0.190，prodCorrelation 0.620。使用了est_12m_prr_mean_3mth_ago字段,用了基于分析师预期趋势的动量捕捉。
第2个alpha是'USA/D1/IMBALANCE'的，sharpe 1.56，fitness 0.89，margin 11.9‱，selfCorrelation 0.458，prodCorrelation 0.613。使用了imb1_datatime、nws31_amertimestamp_date字段,用了基于新闻情绪与流动性的逆向选股。

总结：今天的alpha fitness勉强及格, 今天写的策略代码逻辑超清晰，注释也完整，看着就舒服，成就感拉满。

============================================================

---

### 探讨 #206: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月1日 ---------------------------------------- 今天是2025年12月1日，今天一共提交了2个alpha 第1个alpha是'USA/D1/OPTION'的，sharpe 1.71，fitness 1.43，margin 14.0‱，selfCorrelation 0.257，prodCorrelation 0.657。使用了sector、insd1_gvkey、opt23_super_op_trans_iv_weight_avg_volivcallmput9字段,用了基于期权市场情绪与行业相对定位的波动率策略。 第2个alpha是'AMR/D1/RISK'的，sharpe 1.20，fitness 2.24，margin 92.3‱，selfCorrelation 0.200，prodCorrelation 0.482。使用了rsk62_beta1_1_100_pb字段,用了基于风险调整动量的信号强度评估。 总结：这波fitness数据相当稳健，令人满意, prodCorrelation水平处于中游，算是正常发挥, 调试策略 bug 调了 3 小时，终于发现问题，太不容易了。 ============================================================

---

### 探讨 #207: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

沙发!
++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++
好卷好卷啊

---

### 探讨 #208: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月1日
----------------------------------------
今天是2026年1月1日，今天一共提交了2个alpha

第1个alpha是'USA/D1/FUNDAMENTAL'的，sharpe 1.08，fitness 0.80，margin 11.1‱，selfCorrelation 0.456，prodCorrelation 0.586。使用了insd3_8k_freq_latest_filed、fnd72_s_pit_or_bs_q_bs_other_cur_asset字段,用了基于非现金流动资产的价值发现方法。
第2个alpha是'USA/D1/OTHER'的，sharpe 1.47，fitness 0.96，margin 9.5‱，selfCorrelation 0.395，prodCorrelation 0.589。使用了oth381_organic_search_visits字段,用了基于搜索热度的趋势动量方法。

总结：sharpe表现疲软，收益波动较大, 今天的fitness指标四平八稳, 最近的研究让我对alpha decay有了新认识。

============================================================

---

### 探讨 #209: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月2日
----------------------------------------
今天是2026年1月2日，今天一共提交了2个alpha

第1个alpha是'USA/D1/EARNINGS'的，sharpe 3.06，fitness 2.29，margin 11.2‱，selfCorrelation 0.213，prodCorrelation 0.793。使用了oth84_1_wshactualeps字段,用了基于分析师预期修正的动量方法。
第2个alpha是'USA/D1/FUNDAMENTAL'的，sharpe 1.45，fitness 0.82，margin 11.3‱，selfCorrelation 0.286，prodCorrelation 0.507。使用了fnd23_intfvadjfieldsacctadj_lolv字段,用了基于基本面变化的动量分析。

总结：fitness表现超出预期，今天状态很好, 今天写的策略代码逻辑超清晰，注释也完整，看着就舒服，成就感拉满。

============================================================

---

### 探讨 #210: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月3日
----------------------------------------
今天是2026年1月3日，今天一共提交了2个alpha

第1个alpha是'USA/D1/MACRO'的，sharpe 1.23，fitness 0.75，margin 10.1‱，selfCorrelation 0.488，prodCorrelation 0.766。使用了insd3_10q_freq_latest_filed、oth551_r2_qual字段,用了基于长期基本面质量与近期披露频率的复合方法。
第2个alpha是'USA/D1/MODEL'的，sharpe 1.11，fitness 0.89，margin 13.0‱，selfCorrelation 0.357，prodCorrelation 0.723。使用了mdl240_price_sales字段,用了基于估值稳定性的价值发现方法。

总结：这波sharpe确实有点不给力, fitness表现平稳，没有太大惊喜, 感觉需要更多的跨市场数据来验证。

============================================================

---

### 探讨 #211: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月4日
----------------------------------------
今天是2026年1月4日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/ANALYST'的，sharpe 1.73，fitness 0.91，margin 11.4‱，selfCorrelation 0.337，prodCorrelation 0.628。使用了anl4_mark字段,用了基于分析师数据的尾部反转方法。
第2个alpha是'EUR/D1/MODEL'的，sharpe 1.53，fitness 1.23，margin 25.3‱，selfCorrelation 0.370，prodCorrelation 0.526。使用了star_arm_region_rank_decimal字段,用了基于波动率变化的动量捕捉。

总结：这个sharpe数据算是中等水准, 今天的fitness指标平平无奇, 今天做了因子的换手率分析，结果比预期低，这样实盘交易成本能控制住吗。

============================================================

---

### 探讨 #212: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月5日
----------------------------------------
今天是2026年1月5日，今天一共提交了2个alpha
分类方面：PRICE_REVERSION类别1个

第1个alpha是'EUR/D1/OPTION'的，sharpe 1.91，fitness 1.99，margin 43.9‱，selfCorrelation 0.457，prodCorrelation 0.729。使用了opt30_osp、mdl39_d1_val_mo_global_rank字段,用了基于模型排序与期权价差的复合信号方法。
第2个alpha是'EUR/D1/MODEL'的，sharpe 2.06，fitness 1.49，margin 20.1‱，selfCorrelation 0.447，prodCorrelation 0.650。使用了mdl216_armglobal100score、mdl216_armglobal100score字段,用了基于情绪动量的统计套利方法。

总结：fitness数据表现亮眼，今天收获颇丰, 这波prodCorrelation确实有点不给力, 读了篇关于机器学习因子的 paper，里面的特征选择方法值得试试。

============================================================

---

### 探讨 #213: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月6日
----------------------------------------
今天是2026年1月6日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 1.75，fitness 1.08，margin 43.0‱，selfCorrelation 0.457，prodCorrelation 0.676。使用了shrt3_bar、rec_raisednum_4wks、rec_lowerednum_4wks字段,用了基于分析师情绪与空头压力的复合动量。
第2个alpha是'EUR/D1/OPTION'的，sharpe 2.66，fitness 1.71，margin 11.5‱，selfCorrelation 0.351，prodCorrelation 0.851。使用了opt14_securitymap、rec_mean字段,用了基于技术指标的动量方法。

总结：fitness数据看起来相当不错，今天收获满满, 今天的sharpe让人刮目相看，风控到位, 最近做的因子在小盘股里效果好，大盘股不行，得想办法适配全市场。

============================================================

---

### 探讨 #214: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月7日
----------------------------------------
今天是2026年1月7日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/MACRO'的，sharpe 1.64，fitness 1.00，margin 24.0‱，selfCorrelation 0.394，prodCorrelation 0.697。使用了mcr27_zip、rec_mean字段,用了基于分析师情绪动量的长期均值回归。
第2个alpha是'GLB/D1/PV'的，sharpe 1.04，fitness 0.39，margin 6.0‱，selfCorrelation 0.131，prodCorrelation 0.673。使用了scl12_buzz、pv96_eqy_dvd_sh_last字段,用了基于长期趋势与短期情绪背离的价值发现。

总结：今天的prodCorrelation确实有点惨淡，缺乏新意, 今天的sharpe指标四平八稳, 今天的回测结果超出了我的预期。

============================================================

---

### 探讨 #215: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月8日
----------------------------------------
今天是2026年1月8日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/EARNINGS'的，sharpe 1.31，fitness 0.56，margin 22.7‱，selfCorrelation 0.416，prodCorrelation 0.540。使用了ern3_all_delay_1_next_reptime、mdl109_m3d_cer_se字段,用了基于模型误差趋势的统计套利。
第2个alpha是'GLB/D1/PV'的，sharpe 1.42，fitness 0.62，margin 10.0‱，selfCorrelation 0.141，prodCorrelation 0.613。使用了pv96_eqy_dvd_sh_last字段,用了基于股息趋势动量的基本面方法。

总结：prodCorrelation水平处于中游，算是正常发挥, 最近的学习让我对风险管理有了新想法,啥时候想法会执行呢?咱也不知道啊。

============================================================

---

### 探讨 #216: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月9日
----------------------------------------
今天是2026年1月9日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/INSTITUTIONS'的，sharpe 2.29，fitness 2.14，margin 34.8‱，selfCorrelation 0.146，prodCorrelation 0.391。使用了count_institutional_buyers_security、sector、ern5_total_days_changed字段,用了基于相对盈利预期与资金流向的动量增强。
第2个alpha是'EUR/D1/IMBALANCE'的，sharpe 1.65，fitness 1.12，margin 12.4‱，selfCorrelation 0.297，prodCorrelation 0.698。使用了imb5_mktcap、industry、fnd28_value_05042a字段,用了基于基本面加速的行业中性动量。

总结：prodCorrelation数据平平无奇, 这波sharpe指标相当稳健，令人满意, 单市场数据测试总觉得不全面，要是有更多跨市场数据验证就好了。

============================================================

---

### 探讨 #217: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月10日
----------------------------------------
今天是2026年1月10日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.72，fitness 1.11，margin 21.2‱，selfCorrelation 0.153，prodCorrelation 0.428。使用了io_fund_pct、io_fund_pct字段,用了基于机构持仓动量的趋势跟踪。
第2个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.49，fitness 0.93，margin 30.7‱，selfCorrelation 0.222，prodCorrelation 0.484。使用了io_fund_pct字段,用了基于机构持仓趋势的反转信号。

总结：sharpe数据不算突出，但也不差, 希望能在下个月的比赛中取得好成绩。

============================================================

---

### 探讨 #218: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月11日
----------------------------------------
今天是2026年1月11日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/EARNINGS'的，sharpe 1.13，fitness 0.88，margin 20.1‱，selfCorrelation 0.481，prodCorrelation 0.670。使用了earnings_date_fiscal_year字段,用了基于盈利趋势的动量排序。
第2个alpha是'EUR/D1/MACRO'的，sharpe 1.34，fitness 0.79，margin 8.1‱，selfCorrelation 0.264，prodCorrelation 0.683。使用了mcr10_value、ern3_next_reptime、industry字段,用了基于动量与基本面结合的复合方法。

总结：这个prodCorrelation数据让人有点焦虑, 今天的fitness指标不温不火, 脑子里有几个策略想法，希望能尽快落地测试，转化成实际收益。

============================================================

---

### 探讨 #219: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月13日
----------------------------------------
今天是2026年1月13日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/MACRO'的，sharpe 1.73，fitness 1.08，margin 7.8‱，selfCorrelation 0.317，prodCorrelation 0.703。使用了country、oth551_resret_size字段,用了基于宏观经济因子变化的信号增强方法。
第2个alpha是'GLB/D1/NEWS'的，sharpe 1.22，fitness 0.64，margin 5.5‱，selfCorrelation 0.221，prodCorrelation 0.679。使用了subindustry、mws76_confidence字段,用了基于新闻情绪一致性的行业相对方法。

总结：sharpe水平处于中游，算是正常发挥, 今天的fitness水准还过得去, 继续努力，争取明天有更好的alpha。

============================================================

---

### 探讨 #220: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月14日
----------------------------------------
今天是2026年1月14日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/NEWS'的，sharpe 1.21，fitness 0.51，margin 8.7‱，selfCorrelation 0.320，prodCorrelation 0.525。使用了nws3_wqreceivetime字段,用了基于新闻情绪偏离度的反转方法。
第2个alpha是'GLB/D1/SENTIMENT'的，sharpe 1.42，fitness 1.07，margin 38.4‱，selfCorrelation 0.288，prodCorrelation 0.481。使用了snt26_wq_pit_30字段,用了基于情绪变化的动量加速方法。

总结：今天的sharpe水准还过得去, 最近的回测数量创新高,开心。

============================================================

---

### 探讨 #221: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月15日
----------------------------------------
今天是2026年1月15日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/PV'的，sharpe 1.12，fitness 0.68，margin 11.1‱，selfCorrelation 0.319，prodCorrelation 0.804。使用了pv13_1l_scibr、snt26_wq_pit_30字段,用了基于多周期情绪调整动量的选股方法。
第2个alpha是'EUR/D1/OTHER'的，sharpe 1.41，fitness 0.89，margin 17.7‱，selfCorrelation 0.181，prodCorrelation 0.473。使用了sector、oth47_rank字段,用了基于相对强弱变化的动量加速方法。

总结：sharpe表现疲软，收益波动较大, 继续努力，争取明天有更好的alpha。

============================================================

---

### 探讨 #222: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月16日
----------------------------------------
今天是2026年1月16日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 1.60，fitness 1.79，margin 25.1‱，selfCorrelation 0.103，prodCorrelation 0.429。使用了entity_total_revenue字段,用了基于平滑加速变化的基本面趋势方法。
第2个alpha是'EUR/D1/MACRO'的，sharpe 1.05，fitness 0.67，margin 28.1‱，selfCorrelation 0.147，prodCorrelation 0.416。使用了mcr10_value、mdl162_vwap_5字段,用了基于长期排名平滑的趋势跟踪。

总结：prodCorrelation指标一般般，不算太差, 今天检查因子是否有幸存者偏差，还好问题不大，稍微调整下就好。

============================================================

---

### 探讨 #223: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月17日
----------------------------------------
今天是2026年1月17日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/OTHER'的，sharpe 1.41，fitness 1.60，margin 61.4‱，selfCorrelation 0.343，prodCorrelation 0.640。使用了oth436_divyld字段,用了基于股息率变化的加速动量方法。
第2个alpha是'GLB/D1/OTHER'的，sharpe 1.55，fitness 2.42，margin 80.5‱，selfCorrelation 0.136，prodCorrelation 0.628。使用了annual_dividend_to_price_ratio字段,用了基于基本面变化的加速动量方法。

总结：今天的sharpe勉强过得去, prodCorrelation数据让人担忧，撞车风险很高, 希望能找到更多稳定的alpha来源。

============================================================

---

### 探讨 #224: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月18日
----------------------------------------
今天是2026年1月18日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/SHORTINTEREST'的，sharpe 1.31，fitness 0.82，margin 17.5‱，selfCorrelation 0.310，prodCorrelation 0.518。使用了star_si_insown_pct、subindustry、oth327_mktcap字段,用了基于行业相对动量的趋势跟踪。
第2个alpha是'GLB/D1/OPTION'的，sharpe 1.05，fitness 0.79，margin 13.3‱，selfCorrelation 0.491，prodCorrelation 0.764。使用了opt4_bid字段,用了基于价格加速度的动量增强方法。

总结：fitness水平处于中游，算是正常发挥, 最近看了不少paper，希望能有所启发。

============================================================

---

### 探讨 #225: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月19日
----------------------------------------
今天是2026年1月19日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/NEWS'的，sharpe 1.11，fitness 0.49，margin 13.2‱，selfCorrelation 0.182，prodCorrelation 0.391。使用了nws3_scores_posnormscr字段,用了基于市场情绪的反转方法。
第2个alpha是'GLB/D1/INSTITUTIONS'的，sharpe 1.28，fitness 0.83，margin 14.3‱，selfCorrelation 0.315，prodCorrelation 0.734。使用了aggregate_share_count_all_owners字段,用了基于机构持股趋势的稳定性方法。

总结：今天的sharpe有点拉胯，风险偏高, 今天的prodCorrelation指标属于正常范围, 看别人做的数据挖掘报告，感觉自己这方面能力还差不少，得补补课。

============================================================

---

### 探讨 #226: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月20日
----------------------------------------
今天是2026年1月20日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/FUNDAMENTAL'的，sharpe 1.74，fitness 1.02，margin 27.3‱，selfCorrelation 0.355，prodCorrelation 0.558。使用了io_inst_prev_mv、fnd23_annfvalld1_derq字段,用了基于极端估值反转的量化选股。
第2个alpha是'KOR/D1/INSIDERS'的，sharpe 1.50，fitness 2.06，margin 37.8‱，selfCorrelation 0.424，prodCorrelation 0.532。使用了insd5_rpst_grp_typ、rsk68_residual_return字段,用了基于高阶动量的风险调整方法。

总结：prodCorrelation数据平平无奇, sharpe表现平稳，没有太大惊喜, 最近的学习让我对量化有了新的理解。

============================================================

---

### 探讨 #227: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月21日
----------------------------------------
今天是2026年1月21日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/SENTIMENT'的，sharpe 1.22，fitness 0.77，margin 8.0‱，selfCorrelation 0.068，prodCorrelation 0.584。使用了snt27_rank_39字段,用了基于情绪排名的标准化动量方法。
第2个alpha是'KOR/D1/SENTIMENT'的，sharpe 1.27，fitness 1.25，margin 19.2‱，selfCorrelation 0.074，prodCorrelation 0.159。使用了snt27_new_atlas_domain_37字段,用了基于情绪指标的反转方法。

总结：这波fitness表现算是及格线, sharpe表现疲软，收益波动较大, 今天的思路比较新颖，期待后续验证。

============================================================

---

### 探讨 #228: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月22日
----------------------------------------
今天是2026年1月22日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/SENTIMENT'的，sharpe 1.34，fitness 1.17，margin 20.7‱，selfCorrelation 0.041，prodCorrelation 0.405。使用了snt27_rank_39字段,用了基于情绪极值的动量捕捉方法。
第2个alpha是'KOR/D1/INSIDERS'的，sharpe 1.50，fitness 1.75，margin 32.1‱，selfCorrelation 0.291，prodCorrelation 0.481。使用了insd5_corp_reg_no、anl15_ind_cal_fy2_pe字段,用了基于分析师预期的动量加速方法。

总结：sharpe指标平平无奇，还行吧, 今天的回测结果超出了我的预期。

============================================================

---

### 探讨 #229: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月23日
----------------------------------------
今天是2026年1月23日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/INSTITUTIONS'的，sharpe 1.74，fitness 1.12，margin 34.5‱，selfCorrelation 0.262，prodCorrelation 0.577。使用了io_fund_mv、next_ex_dividend_event_date字段,用了基于公司行为事件的基本面动量方法。
第2个alpha是'EUR/D1/SOCIALMEDIA'的，sharpe 1.34，fitness 1.11，margin 17.2‱，selfCorrelation 0.330，prodCorrelation 0.701。使用了entity_total_revenue字段,用了基于平滑营收加速度的动量质量方法。

总结：sharpe表现平庸，有待突破, 今天的prodCorrelation确实有点惨淡，缺乏新意, 今天效率超高，不仅完成了因子测试，还整理了策略库，明天继续冲。

============================================================

---

### 探讨 #230: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月24日
----------------------------------------
今天是2026年1月24日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/INSIDERS'的，sharpe 1.03，fitness 0.86，margin 14.1‱，selfCorrelation 0.051，prodCorrelation 0.153。使用了insd5_vol_af字段,用了基于知情交易行为的动量方法。
第2个alpha是'EUR/D1/PV'的，sharpe 1.21，fitness 0.82，margin 11.9‱，selfCorrelation 0.108，prodCorrelation 0.532。使用了pv13_v3_6l_scibr、snt27_website字段,用了基于情绪趋势加速的动量方法。

总结：今天的alpha fitness勉强及格, 新策略回测结果比我预期好太多，太惊喜了。

============================================================

---

### 探讨 #231: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月25日
----------------------------------------
今天是2026年1月25日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/RISK'的，sharpe 1.68，fitness 1.38，margin 13.5‱，selfCorrelation 0.344，prodCorrelation 0.475。使用了mws36_sentiment_words_negative、rsk68_weight_volatility_short字段,用了基于风险波动加速的动量方法。
第2个alpha是'KOR/D1/NEWS'的，sharpe 1.78，fitness 1.63，margin 16.8‱，selfCorrelation 0.042，prodCorrelation 0.358。使用了industry、anl15_gr_cal_fy1_pe、mws36_novelty_oldest_span字段,用了基于基本面动量的加速方法。

总结：这波sharpe表现算是及格线, 今天的prodCorrelation水准还过得去, 这周回测数量破了自己的记录，虽然累，但看着成果很开心。

============================================================

---

### 探讨 #232: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月26日
----------------------------------------
今天是2026年1月26日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/NEWS'的，sharpe 1.61，fitness 1.13，margin 9.9‱，selfCorrelation 0.310，prodCorrelation 0.712。使用了industry、next_ex_dividend_event_date字段,用了基于事件时序变化的行业相对动量。
第2个alpha是'KOR/D1/SOCIALMEDIA'的，sharpe 1.82，fitness 1.96，margin 23.2‱，selfCorrelation 0.444，prodCorrelation 0.444。使用了rp_css_business、scl39_top5_people_also_watch_ticker_ii字段,用了基于社交媒体关注度的动量加速。

总结：今天的sharpe指标不温不火, prodCorrelation表现平庸，有待突破, 今天的想法比较天马行空，但值得尝试。

============================================================

---

### 探讨 #233: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月27日
----------------------------------------
今天是2026年1月27日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/SENTIMENT'的，sharpe 1.32，fitness 0.96，margin 14.2‱，selfCorrelation 0.140，prodCorrelation 0.340。使用了sector、snt27_website字段,用了基于情绪动量的二阶变化方法。
第2个alpha是'EUR/D1/NEWS'的，sharpe 1.80，fitness 1.31，margin 24.2‱，selfCorrelation 0.269，prodCorrelation 0.873。使用了previous_shareholder_meeting_date字段,用了基于公司治理事件频率的动量方法。

总结：今天的alpha fitness还算可以, 今天的回测结果超出了我的预期。

============================================================

---

### 探讨 #234: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月28日
----------------------------------------
今天是2026年1月28日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/PV'的，sharpe 1.71，fitness 1.20，margin 9.8‱，selfCorrelation 0.051，prodCorrelation 0.489。使用了anl25_f21_spe、pv13_2_f4_g3_minvol_1m_sector字段,用了基于分析师预期修正的相对强度方法。
第2个alpha是'KOR/D1/SOCIALMEDIA'的，sharpe 1.87，fitness 1.52，margin 13.3‱，selfCorrelation 0.108，prodCorrelation 0.792。使用了anl25_f21_spe、scl39_top5_people_also_watch_ticker_ii字段,用了基于分析师情绪动量的选股方法。

总结：prodCorrelation数据不太妙，大家想法都差不多, 感觉自己在因子挖掘方面还有很大空间。

============================================================

---

### 探讨 #235: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月29日
----------------------------------------
今天是2026年1月29日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/SOCIALMEDIA'的，sharpe 2.30，fitness 2.11，margin 16.8‱，selfCorrelation 0.016，prodCorrelation 0.351。使用了shrt38_subindustry、scl39_top5_people_also_watch_ticker_ii字段,用了基于社交媒体关注度的动量增强。
第2个alpha是'EUR/D1/SHORTINTEREST'的，sharpe 1.01，fitness 0.54，margin 32.4‱，selfCorrelation 0.433，prodCorrelation 0.707。使用了subindustry、shrt3_utilizationpercent_units字段,用了基于相对市场情绪的价值发现方法。

总结：sharpe数据不温不火, prodCorrelation指标处于平均线附近, 因子库越来越乱，得抽时间系统整理一下，以后找起来更方便。

============================================================

---

### 探讨 #236: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月30日
----------------------------------------
今天是2026年1月30日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/EARNINGS'的，sharpe 1.82，fitness 1.07，margin 6.9‱，selfCorrelation 0.174，prodCorrelation 0.746。使用了ern6_3q_223字段,用了基于基本面变化的动量加速方法。
第2个alpha是'KOR/D1/SHORTINTEREST'的，sharpe 1.43，fitness 1.57，margin 34.7‱，selfCorrelation 0.000，prodCorrelation 0.615。使用了shrt38_z_sec_reldc_pmc、anl15_gr_prc字段,用了基于价格变化复杂性的趋势强度分析。

总结：prodCorrelation指标偏高，思路需要调整, 今天效率不错，明天争取更上一层楼。

============================================================

---

### 探讨 #237: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年1月31日
----------------------------------------
今天是2026年1月31日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/FUNDAMENTAL'的，sharpe 1.40，fitness 1.28，margin 50.4‱，selfCorrelation 0.038，prodCorrelation 0.829。使用了subindustry、fnd21_wasteandhazardousmaterialsmanagement_categoryvolumettm字段,用了基于环境管理效率改善速度的行业相对排序。
第2个alpha是'EUR/D1/INSIDERS'的，sharpe 1.13，fitness 0.71，margin 38.2‱，selfCorrelation 0.486，prodCorrelation 0.640。使用了market、insd1_gvkey、mdl38_rel_val_ev_ebitda字段,用了基于估值效率变化趋势的预测方法。

总结：今天的prodCorrelation确实有点惨淡，缺乏新意, sharpe表现疲软，明天要振作, 今天效率超高，不仅完成了因子测试，还整理了策略库，明天继续冲。

============================================================

---

### 探讨 #238: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月2日
----------------------------------------
今天是2026年2月2日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/PV'的，sharpe 1.69，fitness 1.18，margin 30.5‱，selfCorrelation 0.347，prodCorrelation 0.571。使用了sta2_top1200_fact3_c20、leg2_floating_payment_period_count字段,用了基于流动性调整时序排名的趋势识别。
第2个alpha是'KOR/D1/RISK'的，sharpe 1.71，fitness 1.03，margin 7.2‱，selfCorrelation 0.000，prodCorrelation 0.640。使用了close、rsk68_weight_volatility_short字段,用了基于波动率异常的平滑风险调整方法。

总结：这个fitness数据算是中等水准, sharpe表现平稳，没有太大惊喜, 最近琢磨的风险管理新方法，理论上可行，但啥时候能落地执行呢？先记着。

============================================================

---

### 探讨 #239: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月3日
----------------------------------------
今天是2026年2月3日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/SHORTINTEREST'的，sharpe 1.46，fitness 1.82，margin 31.2‱，selfCorrelation 0.000，prodCorrelation 0.637。使用了sector、shrt38_z_sec_reldc_pmc、oth323_esor字段,用了基于行业动量的条件反转方法。
第2个alpha是'KOR/D1/FUNDAMENTAL'的，sharpe 1.08，fitness 1.97，margin 117.8‱，selfCorrelation 0.000，prodCorrelation 0.455。使用了fnd28_value_09103字段,用了基于高阶统计特征的趋势预测。

总结：今天的fitness指标相当抗打，很稳, 最近策略的最大回撤有点超预期，得在风险控制上多下点功夫。

============================================================

---

### 探讨 #240: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月5日
----------------------------------------
今天是2026年2月5日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/FUNDAMENTAL'的，sharpe 1.43，fitness 2.40，margin 59.6‱，selfCorrelation 0.000，prodCorrelation 0.464。使用了fnd17_spvba字段,用了基于基本面趋势偏离的平滑识别。
第2个alpha是'KOR/D1/OTHER'的，sharpe 1.35，fitness 1.57，margin 26.9‱，selfCorrelation 0.000，prodCorrelation 0.412。使用了oth496_kor_mapped_limit_status字段,用了基于状态指标加速动量的选股方法。

总结：今天的alpha fitness让人刮目相看, 因子好难找啊啊啊啊啊啊啊。

============================================================

---

### 探讨 #241: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月6日
----------------------------------------
今天是2026年2月6日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/OTHER'的，sharpe 1.38，fitness 2.08，margin 74.1‱，selfCorrelation 0.000，prodCorrelation 0.473。使用了oth496_returns4字段,用了基于高阶统计量的动量加速分析。
第2个alpha是'EUR/D1/FUNDAMENTAL'的，sharpe 1.36，fitness 0.82，margin 33.9‱，selfCorrelation 0.412，prodCorrelation 0.620。使用了scl12_sentiment、revenue_change_year_ago_quarter字段,用了基于基本面趋势与情绪数据的复合动量。

总结：sharpe水平处于中游，算是正常发挥, fitness表现超出预期，今天状态很好, 今天的思路比较新颖，期待后续验证。

============================================================

---

### 探讨 #242: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月7日
----------------------------------------
今天是2026年2月7日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/ANALYST'的，sharpe 1.18，fitness 0.87，margin 34.9‱，selfCorrelation 0.458，prodCorrelation 0.696。使用了anl16_clusterestsup字段,用了基于分析师预期修正的动量方法。
第2个alpha是'EUR/D1/RISK'的，sharpe 1.24，fitness 0.65，margin 19.8‱，selfCorrelation 0.347，prodCorrelation 0.561。使用了rsk70_mfm2_euetrd_shortint字段,用了基于风险指标加速变化的动量方法。

总结：sharpe数据不太乐观，需要加油, 今天的fitness指标有点拖后腿, 最近琢磨的风险管理新方法，理论上可行，但啥时候能落地执行呢？先记着。

============================================================

---

### 探讨 #243: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月8日
----------------------------------------
今天是2026年2月8日，今天一共提交了2个alpha

第1个alpha是'EUR/D1/EARNINGS'的，sharpe 1.26，fitness 0.86，margin 15.0‱，selfCorrelation 0.193，prodCorrelation 0.675。使用了ern6_3q_223字段,用了基于基本面趋势变化的动量增强方法。
第2个alpha是'KOR/D1/RISK'的，sharpe 1.09，fitness 0.58，margin 5.6‱，selfCorrelation 0.000，prodCorrelation 0.231。使用了rsk59_s3utilization字段,用了基于风险指标变化的动量增强方法。

总结：sharpe指标不太理想，需要控制风险, 这个fitness水准确实需要提升, 今天检查因子是否有幸存者偏差，还好问题不大，稍微调整下就好。

============================================================

---

### 探讨 #244: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

2026年2月9日
----------------------------------------
今天是2026年2月9日，今天一共提交了2个alpha

第1个alpha是'KOR/D1/MODEL'的，sharpe 1.06，fitness 0.72，margin 17.1‱，selfCorrelation 0.000，prodCorrelation 0.270。使用了mdl53_jc5_3year字段,用了基于模型预测偏差的动量捕捉。
第2个alpha是'KOR/D1/MODEL'的，sharpe 1.16，fitness 1.52，margin 54.4‱，selfCorrelation 0.000，prodCorrelation 0.194。使用了mdl26_frwrd_p_stm_fy1字段,用了基于盈利预期动量变化的峰度识别。

总结：prodCorrelation表现优异，创新思路很棒, 最近既要赶进度，又要学新工具，压力有点大，但咬咬牙能扛。

============================================================

---

### 探讨 #245: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月9日
----------------------------------------
今天是2025年9月9日，今天一共提交了1个alpha

今日alpha:'AMR/D1/SHORTINTEREST'的，sharpe 1.59，fitness 1.40，margin 39.8‱，selfCorrelation 0.000，prodCorrelation 0.517。使用了shrt31_netchange字段,用了基于市值份额动量的极端变化捕捉。

总结：prodCorrelation指标一般般，不算太差, 今天的sharpe指标不温不火, 看了市场微观结构的资料，终于明白为啥有些因子在高频数据里更有效。

============================================================

---

### 探讨 #246: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月10日
----------------------------------------
今天是2025年9月10日，今天一共提交了1个alpha

今日alpha:'AMR/D1/MODEL'的，sharpe 1.75，fitness 1.35，margin 11.9‱，selfCorrelation 0.000，prodCorrelation 0.331。使用了oth455_competitor_n2v_p10_q200_w3_kmeans_cluster_5、mdl230_allcap_sedol_curindebitdap_字段,用了基于技术指标的动量方法。

总结：今天的fitness表现可圈可点，继续保持, 这个prodCorrelation相当给力，值得庆祝, 今天效率超高，不仅完成了因子测试，还整理了策略库，明天继续冲。

============================================================

---

### 探讨 #247: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月11日
----------------------------------------
今天是2025年9月11日，今天一共提交了2个alpha

第1个alpha是'AMR/D1/PV'的，sharpe 1.92，fitness 1.98，margin 52.6‱，selfCorrelation -0.020，prodCorrelation 0.635。使用了mdl230_allcap_sedol_pfcfmtt、pv13_hierarchy_min2_600_sector字段,用了基于基本面数据的价值发现。
第2个alpha是'AMR/D1/SOCIALMEDIA'的，sharpe 2.05，fitness 1.96，margin 18.3‱，selfCorrelation 0.160，prodCorrelation 0.866。使用了mdl39_12_val_mo_global_rank、scl15_timeurgency字段,用了基于排名极值与换手调整的动量捕捉。

总结：prodCorrelation数据不太乐观，需要突破, 这波fitness数据相当稳健，令人满意, 最近用机器学习做因子筛选，效果比传统方法好，越来越感兴趣了。

============================================================

---

### 探讨 #248: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月12日
----------------------------------------
今天是2025年9月12日，今天一共提交了3个alpha

第1个alpha是'AMR/D1/PV'的，sharpe 1.09，fitness 0.65，margin 15.1‱，selfCorrelation 0.384，prodCorrelation 0.527。使用了pv13_h_min20_600_sector、nws79_analyst_ratings_sentiment_447字段,用了基于分析师情绪的相对动量方法。
第2个alpha是'AMR/D1/PV'的，sharpe 1.62，fitness 1.32，margin 27.9‱，selfCorrelation 0.124，prodCorrelation 0.598。使用了pv13_hierarchy_min2_600_sector、nws18_ghc_lna字段,用了基于新闻情绪的短期动量。
第3个alpha是'AMR/D1/MODEL'的，sharpe 1.73，fitness 1.13，margin 8.5‱，selfCorrelation 0.085，prodCorrelation 0.587。使用了market、mdl26_60dy_srprs_lst_q_rnngs字段,用了基于相对动量的行业轮动方法。

总结：今天的sharpe勉强过得去, prodCorrelation指标处于平均线附近, 连续挖了 3 天因子都没达标，难啊难啊，再换个数据试试。

============================================================

---

### 探讨 #249: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月13日
----------------------------------------
今天是2025年9月13日，今天一共提交了2个alpha

第1个alpha是'AMR/D1/MODEL'的，sharpe 1.76，fitness 1.49，margin 25.4‱，selfCorrelation 0.161，prodCorrelation 0.695。使用了snt21_2neut_median_476、mdl39_12_val_mo_industry_rank字段,用了基于行业估值与换手的多因子选股。
第2个alpha是'AMR/D1/SOCIALMEDIA'的，sharpe 1.35，fitness 1.00，margin 22.1‱，selfCorrelation 0.178，prodCorrelation 0.787。使用了fnd28_cfsourceusea_value_04826a、scl15_pricedirection字段,用了基于基本面与动量的复合选股。

总结：今天提交的alpha都还过得去，fitness表现不错, 今天的prodCorrelation偏高，策略同质化严重, 今天调了因子的参数区间，回测收益终于比昨天高了，有点小开心。

============================================================

---

### 探讨 #250: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月14日
----------------------------------------
今天是2025年9月14日，今天一共提交了1个alpha

今日alpha:'AMR/D1/PV'的，sharpe 1.60，fitness 1.86，margin 54.2‱，selfCorrelation 0.510，prodCorrelation 0.510。使用了mdl230_allcap_sedol_curindebitdap_字段,用了基于极端值变化的动量反转方法。

总结：fitness指标达到了理想水平，很棒, 新策略回测结果比我预期好太多，太惊喜了。

============================================================

---

### 探讨 #251: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月15日
----------------------------------------
今天是2025年9月15日，今天一共提交了1个alpha

今日alpha:'AMR/D1/NEWS'的，sharpe 2.00，fitness 1.79，margin 16.1‱，selfCorrelation 0.299，prodCorrelation 0.692。使用了mws52_questions_in_qa、anl9_daily_numup字段,用了基于分析师修正的动量方法。

总结：这个sharpe比率相当给力，值得庆祝, fitness数据表现亮眼，今天收获颇丰, 感觉量化这条路还很长，但很有意思。

============================================================

---

### 探讨 #252: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月16日
----------------------------------------
今天是2025年9月16日，今天一共提交了1个alpha

今日alpha:'AMR/D1/OTHER'的，sharpe 1.80，fitness 1.63，margin 54.1‱，selfCorrelation 0.215，prodCorrelation 0.680。使用了oth696_dl_sentiment_score_492字段,用了基于情感动量的相对强弱方法。

总结：这个prodCorrelation水准确实需要改进, 最近看了不少paper，希望能有所启发。

============================================================

---

### 探讨 #253: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月17日
----------------------------------------
今天是2025年9月17日，今天一共提交了2个alpha

第1个alpha是'GLB/D1/PV'的，sharpe 2.79，fitness 2.67，margin 18.3‱，selfCorrelation 0.438，prodCorrelation 0.829。使用了sector、mdl110_score、adv20字段,用了基于流动性的横截面动量增强。
第2个alpha是'GLB/D1/MODEL'的，sharpe 3.44，fitness 2.35，margin 10.1‱，selfCorrelation 0.296，prodCorrelation 0.693。使用了industry、mdl139_score字段,用了基于行业相对动量的趋势识别。

总结：今天的fitness数据真是让人眼前一亮, 但是感觉需要更多的跨市场数据来验证。

============================================================

---

### 探讨 #254: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月19日
----------------------------------------
今天是2025年9月19日，今天一共提交了1个alpha

今日alpha:'AMR/D1/MODEL'的，sharpe 1.96，fitness 2.77，margin 69.9‱，selfCorrelation 0.161，prodCorrelation 0.560。使用了mdl230_allcap_sedol_pb字段,用了基于基本面指标的动量方法。

总结：今天的fitness表现可圈可点，继续保持, 今天的prodCorrelation中规中矩, 希望能在这次Genius定级取得好结果。

============================================================

---

### 探讨 #255: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月20日
----------------------------------------
今天是2025年9月20日，今天一共提交了1个alpha

今日alpha:'AMR/D1/MODEL'的，sharpe 1.74，fitness 1.46，margin 64.2‱，selfCorrelation 0.386，prodCorrelation 0.830。使用了mdl216_armrecommendationscore字段,用了基于分析师共识动量的横截面方法。

总结：今天的sharpe水准还过得去, 最近做的因子在小盘股里效果好，大盘股不行，得想办法适配全市场。

============================================================

---

### 探讨 #256: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月21日
----------------------------------------
今天是2025年9月21日，今天一共提交了1个alpha

今日alpha:'AMR/D1/MODEL'的，sharpe 1.68，fitness 2.55，margin 180.0‱，selfCorrelation 0.278，prodCorrelation 0.605。用了基于相对资本效率的动量方法。

总结：fitness数据表现亮眼，今天收获颇丰, 这波sharpe表现算是及格线

============================================================

---

### 探讨 #257: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月22日
----------------------------------------
今天是2025年9月22日，今天一共提交了1个alpha

今日alpha:'GLB/D1/MODEL'的，sharpe 2.81，fitness 1.74，margin 28.9‱，selfCorrelation 0.309，prodCorrelation 0.708。使用了基于模型估值偏离的均值回归。这比赛的因子是真真真真难出.

============================================================

---

### 探讨 #258: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月23日
----------------------------------------
今天是2025年9月23日，今天一共提交了1个alpha

今日alpha:'AMR/D1/MODEL'的，sharpe 1.41，fitness 1.00，margin 26.1‱，selfCorrelation 0.226，prodCorrelation 0.809。使用了mdl138_qpdi4_roe字段,用了基于基本面质量的动量方法。

总结：prodCorrelation表现疲软，明天要创新, fitness表现尚可，继续努力吧, 今天效率不错，明天争取更上一层楼。

============================================================

---

### 探讨 #259: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月24日
----------------------------------------
今天是2025年9月24日，今天一共提交了1个alpha

今日alpha:'GLB/D1/MODEL'的，sharpe 2.15，fitness 1.56，margin 10.5‱，selfCorrelation 0.422，prodCorrelation 0.802。用了基于行业相对估值动量的趋势捕捉。

总结：这个sharpe水准确实不错，点个赞, 今天做了因子的换手率分析，结果比预期低，这样实盘交易成本能控制住吗。

============================================================

---

### 探讨 #260: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月25日
----------------------------------------
今天是2025年9月25日，今天一共提交了1个alpha

今日alpha:'GLB/D1/PV'的，sharpe 1.86，fitness 1.06，margin 14.4‱，selfCorrelation 0.336，prodCorrelation 0.799。,用了基于风险调整动量的相对强度方法。

总结：prodCorrelation表现疲软，明天要创新, 今天的sharpe指标相当抗打，很稳, 今天也得 good good study，把新学的因子工具练熟，day day up！。

============================================================

---

### 探讨 #261: 关于《**GLB**  **/D1/MODEL** Self-correlation:0.12 Production correlation :0.47》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

2025年9月26日
----------------------------------------
今天是2025年9月26日，今天一共提交了1个alpha

今日alpha:'AMR/D1/MODEL'的，sharpe 1.86，fitness 2.57，margin 67.9‱，selfCorrelation 0.161，prodCorrelation 0.460。用了基于基本面指标的动量方法。

总结：今天的prodCorrelation数据中规中矩, 今天调试了很久，终于找到了问题所在。

============================================================

---

### 探讨 #262: 关于《print('retrying in', result.headers["retry-after"], 'seconds')》的评论回复
- **帖子链接**: [Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha.md
- **评论时间**: 1年前

照着操作了,可以麻烦补充一下

table_names = ["ASI_DELAY1", ]这些表的创建语句及对应的从worldquant拉取数据字段的函数方法吗?

还有sharpe_2022 = get_sharpe_2022(s, id),这个get_sharpe_2022(s, id)函数能否补充一下?

谢谢.

---

### 探讨 #263: 关于《print('retrying in', result.headers["retry-after"], 'seconds')》的评论回复
- **帖子链接**: [Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha.md
- **评论时间**: 1年前

谢谢大佬,希望尽快出现 **第02篇** .

---

### 探讨 #264: 关于《print('retrying in', result.headers["retry-after"], 'seconds')》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md
- **评论时间**: 1 year ago

照着操作了,可以麻烦补充一下

table_names = ["ASI_DELAY1", ]这些表的创建语句及对应的从worldquant拉取数据字段的函数方法吗?

还有sharpe_2022 = get_sharpe_2022(s, id),这个get_sharpe_2022(s, id)函数能否补充一下?

谢谢.

---

### 探讨 #265: 关于《print('retrying in', result.headers["retry-after"], 'seconds')》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【构建自己的代码框架系列】第01篇--用MySQL完美保存全部回测过的alpha_28770820524695.md
- **评论时间**: 1 year ago

谢谢大佬,希望尽快出现 **第02篇** .

---

### 探讨 #266: 关于《【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子,永不停歇,可插队可撤回》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【构建自己的代码框架系列】第02篇--用Redis完美构建待回测池子永不停歇可插队可撤回_28969108137623.md
- **评论时间**: 1 year ago

大佬,我又来学习了! 但是我的2C2G服务器好像快扛不住这些新东西了,卡卡卡.

---

### 探讨 #267: 关于《转换为 Pandas DataFrame》的评论回复
- **帖子链接**: [Commented] 【网页监控】基于Streamlit和数据库的网页监控进程代码优化.md
- **评论时间**: 1年前

大佬太牛了

---

### 探讨 #268: 关于《转换为 Pandas DataFrame》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【网页监控】基于Streamlit和数据库的网页监控进程代码优化_30329770583959.md
- **评论时间**: 1年前

大佬太牛了

---

### 探讨 #269: 关于《【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎》的评论回复
- **帖子链接**: [Commented] 【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎.md
- **评论时间**: 1年前

很感兴趣

---

### 探讨 #270: 关于《【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎_28268813242647.md
- **评论时间**: 1年前

很感兴趣

---

### 探讨 #271: 关于《一点关于模版的问题》的评论回复
- **帖子链接**: [Commented] 一点关于模版的问题.md
- **评论时间**: 1年前

感谢友友的问题,让我了解到了什么是二值数据.这个问题主要还是二值数据本身只有两个值,所以波动巨大.把二值数据处理一下,让他的波动不要那么大即可.正常的decay设置应该也是有效的,或者使用ts_mean(b,d)这样的方式去找均值,就把原先的大波动改为小波动了.或者加上限制条件ts_corr(a,b)<0.3或者ts_corr(a,b)>0.7这种来抑制信号,也可以使用换手率控制符去控制换手之类的.希望对你有帮助.

---

### 探讨 #272: 关于《一点关于模版的问题》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 一点关于模版的问题_32984895826327.md
- **评论时间**: 1年前

感谢友友的问题,让我了解到了什么是二值数据.这个问题主要还是二值数据本身只有两个值,所以波动巨大.把二值数据处理一下,让他的波动不要那么大即可.正常的decay设置应该也是有效的,或者使用ts_mean(b,d)这样的方式去找均值,就把原先的大波动改为小波动了.或者加上限制条件ts_corr(a,b)<0.3或者ts_corr(a,b)>0.7这种来抑制信号,也可以使用换手率控制符去控制换手之类的.希望对你有帮助.

---

### 探讨 #273: 关于《使用浏览器开发者工具查看http请求，用于本地代码请求对应功能经验分享》的评论回复
- **帖子链接**: [Commented] 使用浏览器开发者工具查看http请求用于本地代码请求对应功能经验分享.md
- **评论时间**: 1年前

学到了啊, 以后需要找什么API请求地址,直接在网页上发起请求,然后监控新请求就行了,甚至请求参数都包含在里面了. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 什么时候才能跟大佬一样牛逼

---

### 探讨 #274: 关于《使用浏览器开发者工具查看http请求，用于本地代码请求对应功能经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 使用浏览器开发者工具查看http请求用于本地代码请求对应功能经验分享_32715688747159.md
- **评论时间**: 1年前

学到了啊, 以后需要找什么API请求地址,直接在网页上发起请求,然后监控新请求就行了,甚至请求参数都包含在里面了. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 什么时候才能跟大佬一样牛逼

---

### 探讨 #275: 关于《保存OAuth登录认证，避免多次登录平台代码优化》的评论回复
- **帖子链接**: [Commented] 保存OAuth登录认证避免多次登录平台代码优化.md
- **评论时间**: 1年前

大佬大佬,如何使用上面的代码?直接放到machinelib里面吗?替换里面哪些方法啊?

=========================================================
=========================================================

我的代码能力实在太差了

---

### 探讨 #276: 关于《保存OAuth登录认证，避免多次登录平台代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 保存OAuth登录认证避免多次登录平台代码优化_32787531727639.md
- **评论时间**: 1年前

大佬大佬,如何使用上面的代码?直接放到machinelib里面吗?替换里面哪些方法啊?

=========================================================
=========================================================

我的代码能力实在太差了

---

### 探讨 #277: 关于《关于新ops在EUR的探索》的评论回复
- **帖子链接**: [Commented] 关于新ops在EUR的探索.md
- **评论时间**: 1年前

请大佬多教我本领,谢谢.

---

### 探讨 #278: 关于《关于新ops在EUR的探索》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 关于新ops在EUR的探索_29983731904151.md
- **评论时间**: 1年前

请大佬多教我本领,谢谢.

---

### 探讨 #279: 关于《💻如何免费领取阿里无影云电脑使用》的评论回复
- **帖子链接**: [Commented] 如何免费领取阿里无影云电脑使用.md
- **评论时间**: 1年前

这个好像没法使用SSH连接他啊  也没有公网IP  用起来太麻烦了   但是速度杠杠的  同时那些小时消耗的贼快  个人不建议用这个无影云

---

### 探讨 #280: 关于《💻如何免费领取阿里无影云电脑使用》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何免费领取阿里无影云电脑使用_25889938244375.md
- **评论时间**: 1年前

这个好像没法使用SSH连接他啊  也没有公网IP  用起来太麻烦了   但是速度杠杠的  同时那些小时消耗的贼快  个人不建议用这个无影云

---

### 探讨 #281: 关于《提取字段名（cut_index之前的部分）》的评论回复
- **帖子链接**: [Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化.md
- **评论时间**: 1年前

感谢分享,已经使用上了

---

### 探讨 #282: 关于《提取字段名（cut_index之前的部分）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md
- **评论时间**: 1年前

感谢分享,已经使用上了

---

### 探讨 #283: 关于《[【工程技术分享】如何将自己的回测过的alpha全部下载到本地]([L2] 【工程技术分享】如何将自己的回测过的alpha全部下载到本地_28883893064599.md)》的评论回复
- **帖子链接**: [Commented] 新人经验分享.md
- **评论时间**: 1年前

getd atafield使用时,服务器最多返回10000条数据,如果数据超过了一万条,后续的数据就获取不到了,该怎么处理?

---

### 探讨 #284: 关于《[【工程技术分享】如何将自己的回测过的alpha全部下载到本地]([L2] 【工程技术分享】如何将自己的回测过的alpha全部下载到本地_28883893064599.md)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 新人经验分享_29213185409303.md
- **评论时间**: 1年前

getd atafield使用时,服务器最多返回10000条数据,如果数据超过了一万条,后续的数据就获取不到了,该怎么处理?

---

### 探讨 #285: 关于《用vector_neut复现regression_neut功能经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiXGtd%2Bmhs6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAZNodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzAzNTAzNjY5Mzk3OTktJUU3JTk0JUE4dmVjdG9yLW5ldXQlRTUlQTQlOEQlRTclOEUlQjByZWdyZXNzaW9uLW5ldXQlRTUlOEElOUYlRTglODMlQkQGOwhUOg5zZWFyY2hfaWRJIik0YmY0OGY0MC01MzIwLTRiYzktYjNiNi1lNzRlNzc4OTI3YzIGOwhGOglyYW5raQ86C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxTRDE3NTMxBjsIVDoScmVzdWx0c19jb3VudGkb--79916dfb8a387d0b28b9c690637805508076e9f0
- **评论时间**: 1年前

膜拜大佬  但是这两个操作符  我都没有啊

---

### 探讨 #286: 关于《用vector_neut复现regression_neut功能经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 用vector_neut复现regression_neut功能经验分享_30350366939799.md
- **评论时间**: 1年前

膜拜大佬  但是这两个操作符  我都没有啊

---

### 探讨 #287: 关于《用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXmMHqWR06D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAgsBaHR0cHM6Ly9zdXBwb3J0LndvcmxkcXVhbnRicmFpbi5jb20vaGMvemgtY24vY29tbXVuaXR5L3Bvc3RzLzMyMjcyMDI3ODUwNzc1LSVFNyU5NCVBOCVFNiU5QyVBQyVFNSU5QyVCMCVFNSU4QyU5NiVFOCVBRSVBMSVFNyVBRSU5Ny1QbkwtJUU3JTlCJUI4JUU1JTg1JUIzJUU2JTgwJUE3JUU2JTlEJUE1JUU5JUFBJThDJUU4JUFGJTgxLVNlbGYtQ29ycmVsYXRpb24tJUU1JTkyJThDLVBvd2VyLVBvb2wtQ29ycmVsYXRpb24tJUU3JTlBJTg0JUU1JTg1JUIzJUU3JUIzJUJCBjsIVDoOc2VhcmNoX2lkSSIpNGJmNDhmNDAtNTMyMC00YmM5LWIzYjYtZTc0ZTc3ODkyN2MyBjsIRjoJcmFua2kNOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMU0QxNzUzMQY7CFQ6EnJlc3VsdHNfY291bnRpGw%3D%3D--8178b2018dc834b9b770ce627e1ead14f1d6b8d0
- **评论时间**: 1年前

虽然Self 不含 Power Pool，但是prod包含Power Pool。所以当一个因子用power pool交了之后，该因子没法通过正常的方式提交（因为prod 不过）======================================================================================================================================================================所以一个alpha想要交两次的话,需要先不加描述,不标记PPA提交一次,然后再用PPA的方式提交一次,一鱼两吃了.

---

### 探讨 #288: 关于《用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 用本地化计算 PnL 相关性来验证 Self Correlation 和 Power Pool Correlation 的关系经验分享_32272027850775.md
- **评论时间**: 1年前

虽然Self 不含 Power Pool，但是prod包含Power Pool。所以当一个因子用power pool交了之后，该因子没法通过正常的方式提交（因为prod 不过）

===================================================================================

===================================================================================
所以一个alpha想要交两次的话,需要先不加描述,不标记PPA提交一次,然后再用PPA的方式提交一次,一鱼两吃了.

---
