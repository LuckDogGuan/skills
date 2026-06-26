# 顾问 MS51256 (Rank 28) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 MS51256 (Rank 28) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: PnL = ∑(Robustness * Creativity))
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
顾问 SJ65808 (Rank 20)两位大佬都有分享。帖子分别如下： [[Commented] 一个非科班选手的量化打怪升级路季度奖突破万刀必读_38628691756695.md]([Commented] 一个非科班选手的量化打怪升级路季度奖突破万刀必读_38628691756695.md)  

 [[Commented] 2025年度收入回顾经验分享_38623022786839.md]([Commented] 2025年度收入回顾经验分享_38623022786839.md)  

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

**顾问 MS51256 (Rank 28) 的解答与建议**:
666向优秀的大佬学习，努力成为1W刀+的GM

#========= WORLDQUANT BRAIN CONSULTANT ========== #
#每天进步一点点，加油
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================加油每一天=======================#


---

### 技术对话片段 2 (原帖: 25Q3顾问提交情况播报（每日更新）)
- **原帖链接**: [Commented] 25Q3顾问提交情况播报每日更新.md
- **时间**: 9个月前

**提问/主帖背景 (HQ17963)**:
本贴使用Genius排行榜及Consultant排行榜数据，对以下指标进行统计：

- 本季度有提交、今日有提交、提交满20天（定级基准）的顾问人数
- SA、RA提交情况（数量和平均相关性）
- RA平均操作符数量、平均字段数量

并且每种指标分别对以下群体统计：

- 今日有提交的顾问
- 今日有提交且Combined Alpha Performance>=2的顾问
- 今日有提交且Combined Selected Alpha Performance>=2的顾问
- 今日有提交且Value Factor>=0.95的顾问

本贴每日更新。如有疑问、指标建议、排版建议等，欢迎留言讨论，欢迎写下你对数据的敏锐洞察！

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢HQ大佬每日的信息分享，期待你的更新，让我们可以准确掌握排名情况。祝好
=-===============================================================
-================================================================
=-==================================================================


---

### 技术对话片段 3 (原帖: 25Q3顾问提交情况播报（每日更新）)
- **原帖链接**: [Commented] 25Q3顾问提交情况播报每日更新.md
- **时间**: 9个月前

**提问/主帖背景 (HQ17963)**:
本贴使用Genius排行榜及Consultant排行榜数据，对以下指标进行统计：

- 本季度有提交、今日有提交、提交满20天（定级基准）的顾问人数
- SA、RA提交情况（数量和平均相关性）
- RA平均操作符数量、平均字段数量

并且每种指标分别对以下群体统计：

- 今日有提交的顾问
- 今日有提交且Combined Alpha Performance>=2的顾问
- 今日有提交且Combined Selected Alpha Performance>=2的顾问
- 今日有提交且Value Factor>=0.95的顾问

本贴每日更新。如有疑问、指标建议、排版建议等，欢迎留言讨论，欢迎写下你对数据的敏锐洞察！

**顾问 MS51256 (Rank 28) 的解答与建议**:
super idol的数据统计真全面，可以为赛季末的预测提供精确的指导，太感谢了
=========================================================
==========================================================
==========================================================


---

### 技术对话片段 4 (原帖: 25Q3顾问提交情况播报（每日更新）)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 25Q3顾问提交情况播报每日更新_33266491538199.md
- **时间**: 9个月前

**提问/主帖背景 (HQ17963)**:
本贴使用Genius排行榜及Consultant排行榜数据，对以下指标进行统计：

- 本季度有提交、今日有提交、提交满20天（定级基准）的顾问人数
- SA、RA提交情况（数量和平均相关性）
- RA平均操作符数量、平均字段数量

并且每种指标分别对以下群体统计：

- 今日有提交的顾问
- 今日有提交且Combined Alpha Performance>=2的顾问
- 今日有提交且Combined Selected Alpha Performance>=2的顾问
- 今日有提交且Value Factor>=0.95的顾问

本贴每日更新。如有疑问、指标建议、排版建议等，欢迎留言讨论，欢迎写下你对数据的敏锐洞察！

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢HQ大佬每日的信息分享，期待你的更新，让我们可以准确掌握排名情况。祝好
=-===============================================================
-================================================================
=-==================================================================


---

### 技术对话片段 5 (原帖: 25Q3顾问提交情况播报（每日更新）)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 25Q3顾问提交情况播报每日更新_33266491538199.md
- **时间**: 9个月前

**提问/主帖背景 (HQ17963)**:
本贴使用Genius排行榜及Consultant排行榜数据，对以下指标进行统计：

- 本季度有提交、今日有提交、提交满20天（定级基准）的顾问人数
- SA、RA提交情况（数量和平均相关性）
- RA平均操作符数量、平均字段数量

并且每种指标分别对以下群体统计：

- 今日有提交的顾问
- 今日有提交且Combined Alpha Performance>=2的顾问
- 今日有提交且Combined Selected Alpha Performance>=2的顾问
- 今日有提交且Value Factor>=0.95的顾问

本贴每日更新。如有疑问、指标建议、排版建议等，欢迎留言讨论，欢迎写下你对数据的敏锐洞察！

**顾问 MS51256 (Rank 28) 的解答与建议**:
super idol的数据统计真全面，可以为赛季末的预测提供精确的指导，太感谢了
=========================================================
==========================================================
==========================================================


---

### 技术对话片段 6 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] AIAC 比赛用模板Alpha Template.md
- **时间**: 3个月前

**提问/主帖背景 (SJ65808)**:
给大家分享一个我在AIAC比赛期间用AI发现的一个模板，模板如下：

```
ts_rank(ts_max({data},d1),d2),d1,d2可以取(60,250)或者(20,120)
```

经济学解释:当d1,d2 = (60,250)时该模板衡量当前季度的峰值在过去一年中处于什么位置。

- **高分值信号（接近 1.0）** ：表示当前的季度最高值是过去一年中所有季度最高价里最高的。这通常对应着 **年度级别的向上突破** ，代表了极强的动能和市场共识。
- **低分值信号（接近 0.0）** ：表示当前的季度最高点甚至比过去一年中任何时候的季度最高点都要低。这通常反映了 **长期的阴跌趋势** ，即每一次反弹的高点都在不断下移。

效果展示(EUR地区出货较多):

analyst:


> [!NOTE] [图片 OCR 识别内容]
> Broup_neutralize (ts_rank (ts_Oax (VeC_aVB(anllo
> Broup_cartesian_product (coun
> Sin1111atnI
> Settinas
> Intrment Ty
> Reylon
> Uolerse
> Language
> Dcay
> Dlay
> Tmncation
> Mltalat
> Pasturtallon
> NaN Handllng
> Uot Hanlng
> Va Tad 
> MaxRos
> Equty
> TOP SOD
> Fas Exorsssior
> 0.2
> Fast Tactors
> Vrin
> Clone Alpha
> IS Summary
> Tarint
> . Sirele Data Set Aphs
> A Reaular Alpha
> Pramia theme: EURDIIANALYSTA -
> ABaregate
> Uata
> UUAC
> OLUPTO'
> 017
> 1.87
> 5.12%
> 1.UU
> 3.59%
> 2.0896
> 14.039600
> Vear
> Tuwmver
> Fh
> Returs
>  Orawdow
> Margln
> Long Count
> Short Comt
> 201-
> 5.235
> 5
> 205
> 3
> 1311
> 12
> 2015
> 23
> 5.135
> 35
> 7.305
> 1415
> 1413
> 11
> 2015
> 2.0
> 5.29
> 1.13
> 35
> D0S
> 14E
> 12
> 2017
> 2.5
> 5.125
> 404沾
> 7.75
> 1 ?
> 137
> 2013
> 一 V
> 063
> 24586
> 335
> 1-
> 2019
> 0.91
> 1.915
> .33
> 5
> 50S
> _
> 1T
> 2020
> 1.5
> 5.175
> 089
> 11
> 2015
> 三
> 2.4
> 1.705
> 1-3
> ~
> TTFC
> 1-
> 1
> 2022
> 5.025
> 7.73
> 33
> 9-5
> 1_1
> 1393
> 1515
> 2023
> 7
> C 
> 5
> 1.935
> 21.745
> 1313
> 1L3
> Sla


model:


> [!NOTE] [图片 OCR 识别内容]
> Broup_neutralize (ts_rank (ts_wax(ts_backfill(
> Broup_cartesian_product
> Simulation Settinas
> Instrument TyI
> Reglon
> Unerse
> Language
> Dlay
> TN71
> Neutralzato
> Pasteurtatlon
> NaN Handtng
> Unt Handllng
> Vax Trade
> VaxRos
> Equity
> TOP_SOO
> Has EMTEEIUT
> 0.3
> R- {
> VTI;
> Clone Alpha
> IS Summary
> Period
> 眺 Sirzle Data Set Nphs
> Powver Pool Hphs
> 酣 Resular Alpha
> Pramid theme: EURIDIIMODEL *I _
> 4831e2ate
> Data
> TurIO
> FIIeS
> Reuuli
> DrJwUo
> 1.94
> 3.94%
> 1.11
> 4.10%
> 3.4696
> 20.8
> 9oo
> Vear
> Salp
> TONeT
> Ftness
> Reur
> ILa
> Nalgln
> Long Count
> Short Cot
> 201-
> -3
> 1.355
> 7-
> 7.745
> 3-
> 15
> 2015
> -1
> 1.105
> 3-5
> 878
> 1.155
> 425
> 15
> 2016
> 0.32
> 一 U
> 0.75
> C
> 
> 13
> 2017
> 595
> 一-
> -h
> Z
> 1493
> 1451
> 2013
> 3T
> 5
> 1.125
> 5
> 143
> 2019
> 3.315
> 2355
> 2735
> ?
> 15-3
> 2020
> 1.135
> 728
> 775
> 3-5
> 58o
> 1
> 23
> 3.77
> 453
> L02
> ZSC。
> 145
> 202
> 105
> 5
> 275
> 1.715
> 11
> 2023
> 3.11
> 3.555
> 213
> 5.76沾
> 7.305
> a
> 1-59
> 131
> Oco


pv:


> [!NOTE] [图片 OCR 识别内容]
> BrOUP_ZSCOre(
> Broup_neutralize (ts_rank ts
> 
> idustry),exchange
> 3101U1at101
> Settinas
> Instrument TyI
> Reglon
> Unerse
> Language
> Dlay
> TN71
> Neutralzato
>  Pasteurtatlon
> NaN Handtng
> Unt Handllng
> Vax Trade
> VaxRos
> ETU
> TOP_SOO
> Fast Ersssion
> VTI;
> Clone Alpha
> IS Summary
> Period
> 眺 Sirzle Data Set Nphs
> 眙 Power Pool Npha
> 眺 Rezular Mlpha
> Pramio theme: EURDTIPV31.1
> 82ate
> Data
> TurIO'
> FIIeS
> Reuurn
> DrJwUo
> MJi
> 89
> 3.70%
> 1.04
> 3.80%
> 2.6696
> 20.499600
> Salp
> JITO
> Ftness
> JT
> Ia
> Nalgln
> Long Count
> Short Cot
> 201-
> 1.17
> 95
> 17
> 05
> 2
> 1255
> 1
> 2015
> 3.53
> 1.3-5
> 728
> 7.315
> 3E
> 1132
> 2016
> 0.-1
> .5
> 03
> 35
> SZs
> 1332
> 132
> 2017
> .39
> 1
> 195
> 115
> 1363
> 2013
> 1.525
> 4653
> 7.705
> 2_1
> 1533
> 123
> 2019
> 3.63
> 3.575
> 617
> 7.795
> 34SESo
> 12
> 2020
> 90
> 273
> 423
> 110e
> 17
> 13-9
> 1417
> 2021
> .475
> 7.01
> -014
> 2669;
> ~7518
> 1476
> 143
> 202
> 1.53
> 3.525
> 12
> 995
> 卫1
> 1619
> 123
> 2023
> 3.0
> 1.415
> 5353
> 3.5-5
> 313
> 143-
> 17
> Oco


fundamental:


> [!NOTE] [图片 OCR 识别内容]
> Broup_scale( -Eroup_neutralize (ts_rank(ts_max(ts_backfill
> industry ),warket)
> Sin1111atnI
> Settings
> Intrment Ty
> Reglon
> Uolerse
> Language
> Dcay
> Dlay
> Tncato
> Mltalat
> Pasturtallon
> NaN Handlm
> Uot Hanlng
> Va Tad 
> Tao
> Equty
> TOP SOD
> Fas Exorsssior
> 0.2
> R- {
> Vris
> Clone Alpha
> IS Summary
> Tarint
> . Single Data Set Nphs
> A Resular Jlpha
> Pramia themE
> EURDTIFUNDANENTAL  1.1
> ABaregate
> Uata
> UUA
> OLUTC
> FPUITT
> 1.85
> 3.20%
> 1.01
> 3.76%
> 4.01%6
> 23.489600
> Tover
> Fh
> Returs
> Drawdow
> Margln
> Long Count
> Short Comt
> 2011
> .71
> 1.27
> 2
> 7.995
> 1575
> 1239
> 2015
> 3.32
> .063
> 745
> 7.305
> 4 3
> 1333
> 1
> 2015
> 1.125
> JOD
> 072
> 3-5
> J11
> 1253
> J
> 2017
> 2
> 3.0-5
> 350
> 3.555
> 3E
> 1403
> 2013
> 11
> 3.115
> 5
> 7.755
> 25
> 14
> 2019
> 2.915
> 077
> 2778
> 035
> T
> 2020
> 3.235
> 545
> 1.815
> 375
> 1ss
> 2021
> 0.93
> 3.155
> 0-3
> 2
> 2-7
> 147
> 1-77
> 1123
> 2022
> 0.25
> 3.075
> 7.08
> 03
> 101
> SEo
> 1
> 2023
> 3.93
> 3.065
> 309
> 752治
> 3.745
> U
> e
> Sw


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 7 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] AIAC 比赛用模板Alpha Template_38654934214423.md
- **时间**: 3个月前

**提问/主帖背景 (SJ65808)**:
给大家分享一个我在AIAC比赛期间用AI发现的一个模板，模板如下：

```
ts_rank(ts_max({data},d1),d2),d1,d2可以取(60,250)或者(20,120)
```

经济学解释:当d1,d2 = (60,250)时该模板衡量当前季度的峰值在过去一年中处于什么位置。

- **高分值信号（接近 1.0）** ：表示当前的季度最高值是过去一年中所有季度最高价里最高的。这通常对应着 **年度级别的向上突破** ，代表了极强的动能和市场共识。
- **低分值信号（接近 0.0）** ：表示当前的季度最高点甚至比过去一年中任何时候的季度最高点都要低。这通常反映了 **长期的阴跌趋势** ，即每一次反弹的高点都在不断下移。

效果展示(EUR地区出货较多):

analyst:


> [!NOTE] [图片 OCR 识别内容]
> Broup_neutralize (ts_rank (ts_Oax (VeC_aVB(anllo
> Broup_cartesian_product (coun
> Sin1111atnI
> Settinas
> Intrment Ty
> Reylon
> Uolerse
> Language
> Dcay
> Dlay
> Tmncation
> Mltalat
> Pasturtallon
> NaN Handllng
> Uot Hanlng
> Va Tad 
> MaxRos
> Equty
> TOP SOD
> Fas Exorsssior
> 0.2
> Fast Tactors
> Vrin
> Clone Alpha
> IS Summary
> Tarint
> . Sirele Data Set Aphs
> A Reaular Alpha
> Pramia theme: EURDIIANALYSTA -
> ABaregate
> Uata
> UUAC
> OLUPTO'
> 017
> 1.87
> 5.12%
> 1.UU
> 3.59%
> 2.0896
> 14.039600
> Vear
> Tuwmver
> Fh
> Returs
>  Orawdow
> Margln
> Long Count
> Short Comt
> 201-
> 5.235
> 5
> 205
> 3
> 1311
> 12
> 2015
> 23
> 5.135
> 35
> 7.305
> 1415
> 1413
> 11
> 2015
> 2.0
> 5.29
> 1.13
> 35
> D0S
> 14E
> 12
> 2017
> 2.5
> 5.125
> 404沾
> 7.75
> 1 ?
> 137
> 2013
> 一 V
> 063
> 24586
> 335
> 1-
> 2019
> 0.91
> 1.915
> .33
> 5
> 50S
> _
> 1T
> 2020
> 1.5
> 5.175
> 089
> 11
> 2015
> 三
> 2.4
> 1.705
> 1-3
> ~
> TTFC
> 1-
> 1
> 2022
> 5.025
> 7.73
> 33
> 9-5
> 1_1
> 1393
> 1515
> 2023
> 7
> C 
> 5
> 1.935
> 21.745
> 1313
> 1L3
> Sla


model:


> [!NOTE] [图片 OCR 识别内容]
> Broup_neutralize (ts_rank (ts_wax(ts_backfill(
> Broup_cartesian_product
> Simulation Settinas
> Instrument TyI
> Reglon
> Unerse
> Language
> Dlay
> TN71
> Neutralzato
> Pasteurtatlon
> NaN Handtng
> Unt Handllng
> Vax Trade
> VaxRos
> Equity
> TOP_SOO
> Has EMTEEIUT
> 0.3
> R- {
> VTI;
> Clone Alpha
> IS Summary
> Period
> 眺 Sirzle Data Set Nphs
> Powver Pool Hphs
> 酣 Resular Alpha
> Pramid theme: EURIDIIMODEL *I _
> 4831e2ate
> Data
> TurIO
> FIIeS
> Reuuli
> DrJwUo
> 1.94
> 3.94%
> 1.11
> 4.10%
> 3.4696
> 20.8
> 9oo
> Vear
> Salp
> TONeT
> Ftness
> Reur
> ILa
> Nalgln
> Long Count
> Short Cot
> 201-
> -3
> 1.355
> 7-
> 7.745
> 3-
> 15
> 2015
> -1
> 1.105
> 3-5
> 878
> 1.155
> 425
> 15
> 2016
> 0.32
> 一 U
> 0.75
> C
> 
> 13
> 2017
> 595
> 一-
> -h
> Z
> 1493
> 1451
> 2013
> 3T
> 5
> 1.125
> 5
> 143
> 2019
> 3.315
> 2355
> 2735
> ?
> 15-3
> 2020
> 1.135
> 728
> 775
> 3-5
> 58o
> 1
> 23
> 3.77
> 453
> L02
> ZSC。
> 145
> 202
> 105
> 5
> 275
> 1.715
> 11
> 2023
> 3.11
> 3.555
> 213
> 5.76沾
> 7.305
> a
> 1-59
> 131
> Oco


pv:


> [!NOTE] [图片 OCR 识别内容]
> BrOUP_ZSCOre(
> Broup_neutralize (ts_rank ts
> 
> idustry),exchange
> 3101U1at101
> Settinas
> Instrument TyI
> Reglon
> Unerse
> Language
> Dlay
> TN71
> Neutralzato
>  Pasteurtatlon
> NaN Handtng
> Unt Handllng
> Vax Trade
> VaxRos
> ETU
> TOP_SOO
> Fast Ersssion
> VTI;
> Clone Alpha
> IS Summary
> Period
> 眺 Sirzle Data Set Nphs
> 眙 Power Pool Npha
> 眺 Rezular Mlpha
> Pramio theme: EURDTIPV31.1
> 82ate
> Data
> TurIO'
> FIIeS
> Reuurn
> DrJwUo
> MJi
> 89
> 3.70%
> 1.04
> 3.80%
> 2.6696
> 20.499600
> Salp
> JITO
> Ftness
> JT
> Ia
> Nalgln
> Long Count
> Short Cot
> 201-
> 1.17
> 95
> 17
> 05
> 2
> 1255
> 1
> 2015
> 3.53
> 1.3-5
> 728
> 7.315
> 3E
> 1132
> 2016
> 0.-1
> .5
> 03
> 35
> SZs
> 1332
> 132
> 2017
> .39
> 1
> 195
> 115
> 1363
> 2013
> 1.525
> 4653
> 7.705
> 2_1
> 1533
> 123
> 2019
> 3.63
> 3.575
> 617
> 7.795
> 34SESo
> 12
> 2020
> 90
> 273
> 423
> 110e
> 17
> 13-9
> 1417
> 2021
> .475
> 7.01
> -014
> 2669;
> ~7518
> 1476
> 143
> 202
> 1.53
> 3.525
> 12
> 995
> 卫1
> 1619
> 123
> 2023
> 3.0
> 1.415
> 5353
> 3.5-5
> 313
> 143-
> 17
> Oco


fundamental:


> [!NOTE] [图片 OCR 识别内容]
> Broup_scale( -Eroup_neutralize (ts_rank(ts_max(ts_backfill
> industry ),warket)
> Sin1111atnI
> Settings
> Intrment Ty
> Reglon
> Uolerse
> Language
> Dcay
> Dlay
> Tncato
> Mltalat
> Pasturtallon
> NaN Handlm
> Uot Hanlng
> Va Tad 
> Tao
> Equty
> TOP SOD
> Fas Exorsssior
> 0.2
> R- {
> Vris
> Clone Alpha
> IS Summary
> Tarint
> . Single Data Set Nphs
> A Resular Jlpha
> Pramia themE
> EURDTIFUNDANENTAL  1.1
> ABaregate
> Uata
> UUA
> OLUTC
> FPUITT
> 1.85
> 3.20%
> 1.01
> 3.76%
> 4.01%6
> 23.489600
> Tover
> Fh
> Returs
> Drawdow
> Margln
> Long Count
> Short Comt
> 2011
> .71
> 1.27
> 2
> 7.995
> 1575
> 1239
> 2015
> 3.32
> .063
> 745
> 7.305
> 4 3
> 1333
> 1
> 2015
> 1.125
> JOD
> 072
> 3-5
> J11
> 1253
> J
> 2017
> 2
> 3.0-5
> 350
> 3.555
> 3E
> 1403
> 2013
> 11
> 3.115
> 5
> 7.755
> 25
> 14
> 2019
> 2.915
> 077
> 2778
> 035
> T
> 2020
> 3.235
> 545
> 1.815
> 375
> 1ss
> 2021
> 0.93
> 3.155
> 0-3
> 2
> 2-7
> 147
> 1-77
> 1123
> 2022
> 0.25
> 3.075
> 7.08
> 03
> 101
> SEo
> 1
> 2023
> 3.93
> 3.065
> 309
> 752治
> 3.745
> U
> e
> Sw


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 8 (原帖: 对dataframe进行回测)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Alpha稳健性检验代码经验分享_38234815701911.md
- **时间**: 3个月前

**提问/主帖背景 (JL11546)**:
# 导入官方库

import json

import os

import requests

from requests.auth import HTTPBasicAuth

import time

# 导入第三方库

from dotenv import load_dotenv  # 导入环境变量，非必需 pip install python-dotenv

import matplotlib.pyplot as plt

import pandas as pd

# 读取环境变量文件

load_dotenv()

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 9 (原帖: ASI robust FAIL优化小技巧)
- **原帖链接**: [Commented] ASI robust FAIL优化小技巧.md
- **时间**: 6个月前

**提问/主帖背景 (SZ83096)**:
robust 测试是什么：（结合AI和官方文档的理解）

**稳健宇宙测试** 是一种严格健壮性评估方法，旨在确保Alpha因子在不同市场范围
和规模条件下都能保持稳定优异的表现。

brain 平台要求robust 合格的条件是：

```
收益保持率 ≥ 90% : 在调整后的可扩展的universe上的收益至少达到原始提交版本的90%sharpe >=90: 在调整后的可扩展的universe上的sharpe至少达到原始提交版本
```

理解了robust 的概念后，开始尝试优化alpha的robust 过提交标准：

如图： 这是优化前的初始alpha，is指标都不错，但是robust Sharpe和robust returns都差一些，没法提交。


> [!NOTE] [图片 OCR 识别内容]
> #second_order
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.79
> 4.869
> 1.01
> 3.999
> 2.839
> 16.399o。
> imulal [
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Instrur
> 鼍
> 3u
> 0ou
> 禺
> 03m
> Jasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2013
> 0.55
> 5.96%6
> 0.18
> 1.309
> 2.3990
> 4.37260。
> 1432
> 1294
> Equity
> u 』
> 罾0鼍罾
> Jn
> On
> Verify
> On
> 2014
> 1.81
> 4.4796
> .01
> 3.92%
> 1.37%6
> 17.56960
> 1673
> 1473
> 2015
> 1.04
> 4.87%
> 0.45
> 2.34%
> 1.48%
> 9.62900
> 1758
> 1538
> 2016
> 47
> 4.48%
> 0.74
> 3.159
> 1.2090
> 14.069oo
> 690
> 1477
> Clone Alpha 
> 2017
> 2.78
> 4.92%
> 87
> 5.68%
> 1.03%
> 23.07960
> 1723
> 1520
> 2018
> 3.09
> 4.74%
> 2.32
> 7.02%
> 1.01%
> 29.63%600
> 1984
> 1762
> 2019
> 1.14
> 4.71%
> 0.50
> 2.4596
> 1.759
> 10.419oo
> 1758
> 1610
> Chart
> Pnl
> 2020
> 46
> 5.08%
> 0.76
> 3.41%
> 2.83%
> 13.4290
> 1910
> 639
> 2021
> 2.66
> 5.12%
> 1.75
> 5.42%
> 1.14%
> 21.16%0。
> 2400
> 2091
> 2022
> 2.17
> 4.36%
> 44
> 5.49%
> 1.56%
> 25.18%o0
> 2232
> 1945
> 2023
> 1.94
> 4.97%
> -1.18
> -4.63%
> 0.99%
> -18.61%00
> 1964
> 1668
> 300OK
> 2,00OK
> Correlation
> OOOK
> Self Correlation
> Naximum
> Minimum
> Last Run:
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
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 1
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8
> PASS
> 2 FAIL
> Robust universe Sharpe of 1.45 is below cutoff of 1.61 (90% of Alpha):
> Robust universe returns of 3.51% is below cutoff of 3.599 (909 of Alpha):
> Properties
> Last saved Mon; 11/17/2025,7.15 PM
> 2MNARNING


优化1: 尝试了用power ，参数设置3 （参考论坛优化robust 的），没有明显改善


> [!NOTE] [图片 OCR 识别内容]
> #Second
> 0rder
> 眼 Single Data Set Alpha
> 3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.09
> 5.339
> 1.37
> 5.389
> 3.649
> 20.199oo
> power(b,3)
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> mulation
> Settings
> 2013
> 0.52
> 6.55%
> 0.18
> 1.47%
> 3.64%
> 4.48900
> 1458
> 1267
> Instrument Type
> Region
> IInivorse
> aqwane
> Dpraw
> Dolaw
> Triratinn
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 2.13
> 95%
> 1.40
> 5.43%
> 1.75%
> 21.93900
> 1763
> 1383
> Equity
> ASI
> On
> On
> Verify
> On
> 2015
> 28
> 5.26%
> 0.66
> 3.33%
> 80%
> 12.679600
> 1868
> 1428
> 2016
> 28
> 6996
> 0.63
> 3.01%
> 48%
> 12.829600
> 1789
> 1379
> 2017
> 3.08
> 5.28%
> 2.39
> 7.53%
> 66%
> 28.5490
> 1805
> 1438
>  Clone Alpha
> 2018
> 3.23
> 5.11%
> 2.59
> 8.06%
> 1.1796
> 31.5190o
> 2078
> 668
> 2019
> 2.43
> 5.22%
> 1.73
> 34%
> 29%
> 24.319600
> 1858
> 1510
> 2020
> 2.54
> 5.80%
> 87
> 80%
> 2.81%
> 23.45900
> 2028
> 1521
> Chart
> Pnl
> 2021
> 3.44
> 5.6996
> 2.72
> 84%
> 1.319
> 27.5790
> 2567
> 1924
> 2022
> 60
> 4.82%6
> 0.96
> 4.50%
> 2.34%
> 18.64900
> 2404
> 1773
> 2023
> 1.73
> 5.4496
> -1.13
> 38%
> 1.069
> -19.78900
> 2116
> 1516
> Correlation
> Z,OOOK
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8 PASS
> 2 FAIL
> Robust universe Sharpe Of 1.63 is below cutoff of 1.88 (90% of Alpha).
> Properties
> Last Saved Mon; 11/17/2025,7:15 PM
> Robust universe returns of 4.40% is below cutoff of 4.849 (90% of Alpha).
> 2WARNING
> Name
> Category
> 5 PENDING
> Currently 'anonymous'
> None


原alpha最后一步是neut 操作，想了下，更换下power和 group_op的处理顺序后，结果如下，robust returns 过了，但是robust sharpe 还是没改善


> [!NOTE] [图片 OCR 识别内容]
> 卧
> Single Data Set Alpha
> d=power(a,3) ;
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> bgroup_mean
> d,1,industry )-d;b
> 2.19
> 4.91%
> 1.41
> 5.189
> 3.089
> 21.129o。
> Sharpe
> Turnover
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.25
> 5.949
> 0.06
> 0.64%
> 2.96%
> 2.17900
> 1504
> 1222
> Instrument Type
> Region
> Universe
> Language
> hSr
> Q圜g
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 89
> 4.5596
> 1.11
> 4.35%
> 1.169
> 19.139600
> 1764
> 1382
> Equity
> ASI
> MINVOLIM
> Fast Expression
> On
> On
> Verify
> On
> 2015
> 1.57
> 4.819
> 0.86
> 3.72%
> 29%6
> 15.49900
> 1845
> 1451
> 2016
> 54
> 4.37%
> 0.81
> 3.44%
> 1.12%
> 15.76900
> 1765
> 1402
> 2017
> 3.72
> 99%
> 2.97
> 7.97%
> 02%
> 31.92900
> 1787
> 1456
> Clone Alpha 
> 2018
> 3.84
> 4.78%
> 3.27
> 9.05%
> 0.99%6
> 37.88900
> 2068
> 1678
> 2019
> 60
> 4.79%
> 0.89
> 3.84%
> 1.16%
> 16.05900
> 1856
> 1512
> 2020
> 2.24
> 5.32%
> 51
> 5.67%
> 3.08%
> 21.30900
> 2016
> 1533
> N Chart
> Pnl
> 2021
> 3.18
> 5.15%
> 2.34
> 6.79%
> 1.12%
> 26.35900
> 2541
> 1949
> 2022
> 2.67
> 4.44%
> 96
> 77%
> 80%
> 30.549600
> 2374
> 1803
> 2023
> 2.04
> 5.139
> -1.36
> -5.52%
> 1.049
> -21.5190o
> 2064
> 1568
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0s
> Performance Comparison
> Last Run:
> 9 PASS
> 1 FAIL
> Robust universe Sharpe of 1.83 is below cutoff of 1.97 (90% of Alpha)。
> Properties
> Last saved Mon 11/17/2025,7.15 PM
> 2 WARNING
> Name
> Category
> 5 PENDING
> Year
> Fitness


根据字段的定义和labs中查看了字段的分布，值范围，了解到 字段的值范围在0-10；

想了下，是否可以过滤掉一些影响robust sharpe信号的数据（可能过拟合？）

尝试了用tail处理，robust sharpe有比较明显的改善，如图：


> [!NOTE] [图片 OCR 识别内容]
> #SeCond
> Order
> A Single Data Set Alpha
> d-power(tail(a, lower
> 0,
> Upper
> 9, newval
> 01,31;
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Roturns
> Drawdown
> Margin
> bgroup_mean(d,
> industry )-d;b
> 2.31
> 5.049
> 1.56
> 5.71%
> 3.1296
> 22.649o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Cour
> 2013
> 0.55
> 6,25%
> 0.20
> 59%
> 3.12%
> 5.119oo
> 1553
> 117
> Uzation
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 1.91
> 4.799
> 1.15
> 4.5790
> 0.939
> 19.089o
> 1862
> 128
> On
> On
> VeriTy
> On
> 2015
> 4,77%
> 1.17
> 65%
> +40%
> 19.489oo
> 1899
> 139
> 2016
> 0.92
> 4.269
> 0.38
> 089
> 2.119
> 9.7793
> 1810
> 135
> 2017
> 08
> 99%
> 3.46
> 8.98%
> 0.91%
> 36.049oo
> 1831
> 141
> Clone Alpha
> 2018
> 3.92
> 4.78%
> 3.39
> 9.349
> 1.219
> 39.053o
> 2152
> 159
> 2019
> 2.19
> 4,88%
> 1.48
> 5.70%
> 1.,019
> 23.39o
> 1921
> 144
> 2020
> 2.97
> 5.68%
> 2.36
> 7.909
> 2.270
> 27.829o
> 2104
> 144
> Chart
> Pnl
> 2021
> 2.93
> 5,36%
> 2.11
> 6.479
> 1.13%
> 24.17966
> 2782
> 170
> 2022
> 2.44
> 4.809
> 1.74
> 6.359
> 2.009
> 26.479o
> 2540
> 163
> 2023
> 5,279
> ~0.81
> 299
> 1.199
> 16.29%e。
> 2152
> 148
> 40OOK
> Correlation
> ZOOOK
> Self Correlation
> Matmum
> Minimum
> Last Run;
> Power Pool Correlation
> MaMmUm
> MnImUm
> Last Run;
> Jan '14
> Jan '15
> Jan '16
> jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Malmum
> MinImUT
> Last Run:
> IS Testing Status
> Period
> I5
> 0S
> Performance Comparison
> Last Run;
> 9PASS
> Sharpe of 2.31is above cutoff ot
> .58。
> Fitness of 1.56 is above cUtoff ot 1
> Turnover ol
> 04%
> above Cutoff Of 1%。
> Properties
> Last saved Mon 11/17/2025,7.15P1
> Turnoverof
> 049
> below
> Of 709
> Weightis well distributed over instruments.
> Name
> Category
> Sub universe Sharpe of 0.98 is above cutoff of 0.68。
> Robust universe returns of 5.44% Is above cutoff of
> 14% (90% ofAlpha)。
> Currently anonymous'
> None
> Sharpe of 2.41is above cutoff of
> 58
> Pyramid theme ASIIDIISHORTINTEREST matches with multiplier of 1.3. Effective pyramid count for Genius is
> Tags
> Color
> FAIL
> Selectladd tags
> None
> Robust universe Sharpe of 2.05 is below cutoff of 2.08 (909 of Alpha)
> Long
> CUtoff
> year


最后，凭直觉用quantile 变换下分布，robust pass


> [!NOTE] [图片 OCR 识别内容]
> power(tail
> a, lOwer
> Upper
> 9,
> newval
> 01,3);
> ] Single Data Set Alpha
> bgroup
> mean (d,1
> industry)-d;
> ts_mean (X,60)
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> quantile (b,
> driver
> gaussian,
> Sigma
> 1.0 )
> 2.38
> 4.579
> 1.50
> 4.959
> 2.739
> 21.69%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> imulation Settings
> 2013
> 0.05
> 5.72%
> 0.00
> 0.11%
> 2.73%
> 0.38900
> 1385
> 1341
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
> Max Trade
> 2014
> 2.39
> 4.30%
> 1.51
> 4.98%
> 0.829
> 23.20900
> 1598
> 1548
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.66
> 4.4796
> .81
> 5.78%
> 0.929
> 25.889600
> 1648
> 1648
> 2016
> .20
> 4.01%
> 0.53
> 2.44%
> 8496
> 12.14%00
> 1602
> 1565
> 2017
> 4.39
> 4.63%
> 3.61
> 8.47%
> 0.91%
> 36.57900
> 1642
> 1601
> Clone Alpha 
> 2018
> 3.24
> 4.36%
> 2.38
> 6.73%
> 099
> 30.87900
> 869
> 1877
> 2019
> 2.57
> 4.28%
> 1.71
> 5.51%
> 0.879
> 25.73900
> 1683
> 1684
> 2020
> 3.21
> 4.899
> 2.37
> 6.84%
> 79%
> 27.96900
> 853
> 1696
> N
> Chart
> Pnl
> 2021
> 2.85
> 88%
> 89
> 5.51%
> 00%6
> 22.59900
> 2314
> 2177
> 2022
> 86
> 4.24%
> 02
> 3.79%
> 66%
> 17.88900
> 2127
> 2051
> 2023
> 2.89
> 4.419
> 2.24
> -7.48%
> .16%
> -33.90900
> 1883
> 1748
> Correlation
> Z,OOOK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 10 PASS
> 2WARNING
> Competition Al Alphas Competition 2025 does not match.
> Properties
> Last saved Mon, 11/17/2025,12:59 PM
> Theme IND Region Theme does not match with multiplier of 2。
> 5 PENDING
> Name
> Cateeorv


这个alpha op数6个，有亿点点多，尝试去掉power  ，robust也是能过的，优化完成✅


> [!NOTE] [图片 OCR 识别内容]
> d=(tail(a
> LOWer
> Upper
> newval
> 01 )
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> b=group_mean
> d,1, industry )-d;
> 2.37
> 4.569
> 1.48
> 4.909
> 2.819
> 21.47900
> quantile(b,
> driver
> gaussian,
> Sigma
> 1.01
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Urawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.11
> 5.72%
> 0.02
> 0.25%
> 2.81%
> 0.89900
> 1385
> 1341
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
> Max Trade
> 2014
> 2.41
> 4.29%
> 52
> 4.98%
> 0.80%
> 23.20900
> 1606
> 1540
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 63
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.79
> 4.46%
> 94
> 6.04%
> 0.92%
> 27.07900
> 1656
> 1640
> 2016
> 1.19
> 4.029
> 0.52
> 2.39%
> 909
> 11.9090o
> 1611
> 1556
> 2017
> 4.29
> 4.62%
> 3.47
> 8.20%
> 0.96%
> 35.52900
> 651
> 1591
> Clone Alpha 
> 2018
> 3.20
> 4.36%
> 33
> 6.61%
> 03%
> 30.33900
> 867
> 1879
> 2019
> 2.52
> 4.28%
> 65
> 5.39%6
> 0.88%
> 25.21900
> 686
> 682
> 2020
> 3.16
> 87%6
> 2.31
> 69%
> 7996
> 27.509oo
> 853
> 696
> Chart
> Pnl
> 2021
> 2.70
> 4.88%
> 1.75
> 5.24%6
> 9996
> 21.46900
> 2319
> 2172
> 2022
> 89
> 4.2596
> 05
> 3.84%
> 709
> 18.08300
> 2139
> 2039
> 2023
> 3.03
> 4.43%
> 2.39
> 7.78%
> 1.15%
> 35.07900
> 1887
> 1745
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Performance Comparison
> Last Run:
> 10 PASS
> 2 WARNING
> 5 PENDING
> Properties
> Last saved Mon; 11/17/2025,8:17 PM
> Name
> Category
> Currently 'anonymous'
> NOne


结束语：

```
这个alpha，是需要反转的，考虑到我group_mean op这个季度还没用到，所以，我把 -group_neutralize 换成了group_mean(d,1,group)-d (来着研究小组同学的讨论分享，感谢) 
```

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢橘子姐姐的分享，橘子姐姐对op的应用真的让我叹为观止！
好好研究op和字段含义才是做好研究的不二法门。

================================Do your best ================================**


---

### 技术对话片段 10 (原帖: ASI robust FAIL优化小技巧)
- **原帖链接**: https://support.worldquantbrain.com[Commented] ASI robust FAIL优化小技巧_36383377642391.md
- **时间**: 6个月前

**提问/主帖背景 (SZ83096)**:
robust 测试是什么：（结合AI和官方文档的理解）

**稳健宇宙测试** 是一种严格健壮性评估方法，旨在确保Alpha因子在不同市场范围
和规模条件下都能保持稳定优异的表现。

brain 平台要求robust 合格的条件是：

```
收益保持率 ≥ 90% : 在调整后的可扩展的universe上的收益至少达到原始提交版本的90%sharpe >=90: 在调整后的可扩展的universe上的sharpe至少达到原始提交版本
```

理解了robust 的概念后，开始尝试优化alpha的robust 过提交标准：

如图： 这是优化前的初始alpha，is指标都不错，但是robust Sharpe和robust returns都差一些，没法提交。


> [!NOTE] [图片 OCR 识别内容]
> #second_order
>  Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.79
> 4.869
> 1.01
> 3.999
> 2.839
> 16.399o。
> imulal [
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Instrur
> 鼍
> 3u
> 0ou
> 禺
> 03m
> Jasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2013
> 0.55
> 5.96%6
> 0.18
> 1.309
> 2.3990
> 4.37260。
> 1432
> 1294
> Equity
> u 』
> 罾0鼍罾
> Jn
> On
> Verify
> On
> 2014
> 1.81
> 4.4796
> .01
> 3.92%
> 1.37%6
> 17.56960
> 1673
> 1473
> 2015
> 1.04
> 4.87%
> 0.45
> 2.34%
> 1.48%
> 9.62900
> 1758
> 1538
> 2016
> 47
> 4.48%
> 0.74
> 3.159
> 1.2090
> 14.069oo
> 690
> 1477
> Clone Alpha 
> 2017
> 2.78
> 4.92%
> 87
> 5.68%
> 1.03%
> 23.07960
> 1723
> 1520
> 2018
> 3.09
> 4.74%
> 2.32
> 7.02%
> 1.01%
> 29.63%600
> 1984
> 1762
> 2019
> 1.14
> 4.71%
> 0.50
> 2.4596
> 1.759
> 10.419oo
> 1758
> 1610
> Chart
> Pnl
> 2020
> 46
> 5.08%
> 0.76
> 3.41%
> 2.83%
> 13.4290
> 1910
> 639
> 2021
> 2.66
> 5.12%
> 1.75
> 5.42%
> 1.14%
> 21.16%0。
> 2400
> 2091
> 2022
> 2.17
> 4.36%
> 44
> 5.49%
> 1.56%
> 25.18%o0
> 2232
> 1945
> 2023
> 1.94
> 4.97%
> -1.18
> -4.63%
> 0.99%
> -18.61%00
> 1964
> 1668
> 300OK
> 2,00OK
> Correlation
> OOOK
> Self Correlation
> Naximum
> Minimum
> Last Run:
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
> Minimum
> Last Run:
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 1
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8
> PASS
> 2 FAIL
> Robust universe Sharpe of 1.45 is below cutoff of 1.61 (90% of Alpha):
> Robust universe returns of 3.51% is below cutoff of 3.599 (909 of Alpha):
> Properties
> Last saved Mon; 11/17/2025,7.15 PM
> 2MNARNING


优化1: 尝试了用power ，参数设置3 （参考论坛优化robust 的），没有明显改善


> [!NOTE] [图片 OCR 识别内容]
> #Second
> 0rder
> 眼 Single Data Set Alpha
> 3
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.09
> 5.339
> 1.37
> 5.389
> 3.649
> 20.199oo
> power(b,3)
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> mulation
> Settings
> 2013
> 0.52
> 6.55%
> 0.18
> 1.47%
> 3.64%
> 4.48900
> 1458
> 1267
> Instrument Type
> Region
> IInivorse
> aqwane
> Dpraw
> Dolaw
> Triratinn
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 2.13
> 95%
> 1.40
> 5.43%
> 1.75%
> 21.93900
> 1763
> 1383
> Equity
> ASI
> On
> On
> Verify
> On
> 2015
> 28
> 5.26%
> 0.66
> 3.33%
> 80%
> 12.679600
> 1868
> 1428
> 2016
> 28
> 6996
> 0.63
> 3.01%
> 48%
> 12.829600
> 1789
> 1379
> 2017
> 3.08
> 5.28%
> 2.39
> 7.53%
> 66%
> 28.5490
> 1805
> 1438
>  Clone Alpha
> 2018
> 3.23
> 5.11%
> 2.59
> 8.06%
> 1.1796
> 31.5190o
> 2078
> 668
> 2019
> 2.43
> 5.22%
> 1.73
> 34%
> 29%
> 24.319600
> 1858
> 1510
> 2020
> 2.54
> 5.80%
> 87
> 80%
> 2.81%
> 23.45900
> 2028
> 1521
> Chart
> Pnl
> 2021
> 3.44
> 5.6996
> 2.72
> 84%
> 1.319
> 27.5790
> 2567
> 1924
> 2022
> 60
> 4.82%6
> 0.96
> 4.50%
> 2.34%
> 18.64900
> 2404
> 1773
> 2023
> 1.73
> 5.4496
> -1.13
> 38%
> 1.069
> -19.78900
> 2116
> 1516
> Correlation
> Z,OOOK
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 8 PASS
> 2 FAIL
> Robust universe Sharpe Of 1.63 is below cutoff of 1.88 (90% of Alpha).
> Properties
> Last Saved Mon; 11/17/2025,7:15 PM
> Robust universe returns of 4.40% is below cutoff of 4.849 (90% of Alpha).
> 2WARNING
> Name
> Category
> 5 PENDING
> Currently 'anonymous'
> None


原alpha最后一步是neut 操作，想了下，更换下power和 group_op的处理顺序后，结果如下，robust returns 过了，但是robust sharpe 还是没改善


> [!NOTE] [图片 OCR 识别内容]
> 卧
> Single Data Set Alpha
> d=power(a,3) ;
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawgown
> Margin
> bgroup_mean
> d,1,industry )-d;b
> 2.19
> 4.91%
> 1.41
> 5.189
> 3.089
> 21.129o。
> Sharpe
> Turnover
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.25
> 5.949
> 0.06
> 0.64%
> 2.96%
> 2.17900
> 1504
> 1222
> Instrument Type
> Region
> Universe
> Language
> hSr
> Q圜g
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 89
> 4.5596
> 1.11
> 4.35%
> 1.169
> 19.139600
> 1764
> 1382
> Equity
> ASI
> MINVOLIM
> Fast Expression
> On
> On
> Verify
> On
> 2015
> 1.57
> 4.819
> 0.86
> 3.72%
> 29%6
> 15.49900
> 1845
> 1451
> 2016
> 54
> 4.37%
> 0.81
> 3.44%
> 1.12%
> 15.76900
> 1765
> 1402
> 2017
> 3.72
> 99%
> 2.97
> 7.97%
> 02%
> 31.92900
> 1787
> 1456
> Clone Alpha 
> 2018
> 3.84
> 4.78%
> 3.27
> 9.05%
> 0.99%6
> 37.88900
> 2068
> 1678
> 2019
> 60
> 4.79%
> 0.89
> 3.84%
> 1.16%
> 16.05900
> 1856
> 1512
> 2020
> 2.24
> 5.32%
> 51
> 5.67%
> 3.08%
> 21.30900
> 2016
> 1533
> N Chart
> Pnl
> 2021
> 3.18
> 5.15%
> 2.34
> 6.79%
> 1.12%
> 26.35900
> 2541
> 1949
> 2022
> 2.67
> 4.44%
> 96
> 77%
> 80%
> 30.549600
> 2374
> 1803
> 2023
> 2.04
> 5.139
> -1.36
> -5.52%
> 1.049
> -21.5190o
> 2064
> 1568
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0s
> Performance Comparison
> Last Run:
> 9 PASS
> 1 FAIL
> Robust universe Sharpe of 1.83 is below cutoff of 1.97 (90% of Alpha)。
> Properties
> Last saved Mon 11/17/2025,7.15 PM
> 2 WARNING
> Name
> Category
> 5 PENDING
> Year
> Fitness


根据字段的定义和labs中查看了字段的分布，值范围，了解到 字段的值范围在0-10；

想了下，是否可以过滤掉一些影响robust sharpe信号的数据（可能过拟合？）

尝试了用tail处理，robust sharpe有比较明显的改善，如图：


> [!NOTE] [图片 OCR 识别内容]
> #SeCond
> Order
> A Single Data Set Alpha
> d-power(tail(a, lower
> 0,
> Upper
> 9, newval
> 01,31;
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Roturns
> Drawdown
> Margin
> bgroup_mean(d,
> industry )-d;b
> 2.31
> 5.049
> 1.56
> 5.71%
> 3.1296
> 22.649o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Cour
> 2013
> 0.55
> 6,25%
> 0.20
> 59%
> 3.12%
> 5.119oo
> 1553
> 117
> Uzation
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> 2014
> 1.91
> 4.799
> 1.15
> 4.5790
> 0.939
> 19.089o
> 1862
> 128
> On
> On
> VeriTy
> On
> 2015
> 4,77%
> 1.17
> 65%
> +40%
> 19.489oo
> 1899
> 139
> 2016
> 0.92
> 4.269
> 0.38
> 089
> 2.119
> 9.7793
> 1810
> 135
> 2017
> 08
> 99%
> 3.46
> 8.98%
> 0.91%
> 36.049oo
> 1831
> 141
> Clone Alpha
> 2018
> 3.92
> 4.78%
> 3.39
> 9.349
> 1.219
> 39.053o
> 2152
> 159
> 2019
> 2.19
> 4,88%
> 1.48
> 5.70%
> 1.,019
> 23.39o
> 1921
> 144
> 2020
> 2.97
> 5.68%
> 2.36
> 7.909
> 2.270
> 27.829o
> 2104
> 144
> Chart
> Pnl
> 2021
> 2.93
> 5,36%
> 2.11
> 6.479
> 1.13%
> 24.17966
> 2782
> 170
> 2022
> 2.44
> 4.809
> 1.74
> 6.359
> 2.009
> 26.479o
> 2540
> 163
> 2023
> 5,279
> ~0.81
> 299
> 1.199
> 16.29%e。
> 2152
> 148
> 40OOK
> Correlation
> ZOOOK
> Self Correlation
> Matmum
> Minimum
> Last Run;
> Power Pool Correlation
> MaMmUm
> MnImUm
> Last Run;
> Jan '14
> Jan '15
> Jan '16
> jan'17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Malmum
> MinImUT
> Last Run:
> IS Testing Status
> Period
> I5
> 0S
> Performance Comparison
> Last Run;
> 9PASS
> Sharpe of 2.31is above cutoff ot
> .58。
> Fitness of 1.56 is above cUtoff ot 1
> Turnover ol
> 04%
> above Cutoff Of 1%。
> Properties
> Last saved Mon 11/17/2025,7.15P1
> Turnoverof
> 049
> below
> Of 709
> Weightis well distributed over instruments.
> Name
> Category
> Sub universe Sharpe of 0.98 is above cutoff of 0.68。
> Robust universe returns of 5.44% Is above cutoff of
> 14% (90% ofAlpha)。
> Currently anonymous'
> None
> Sharpe of 2.41is above cutoff of
> 58
> Pyramid theme ASIIDIISHORTINTEREST matches with multiplier of 1.3. Effective pyramid count for Genius is
> Tags
> Color
> FAIL
> Selectladd tags
> None
> Robust universe Sharpe of 2.05 is below cutoff of 2.08 (909 of Alpha)
> Long
> CUtoff
> year


最后，凭直觉用quantile 变换下分布，robust pass


> [!NOTE] [图片 OCR 识别内容]
> power(tail
> a, lOwer
> Upper
> 9,
> newval
> 01,3);
> ] Single Data Set Alpha
> bgroup
> mean (d,1
> industry)-d;
> ts_mean (X,60)
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> quantile (b,
> driver
> gaussian,
> Sigma
> 1.0 )
> 2.38
> 4.579
> 1.50
> 4.959
> 2.739
> 21.69%o。
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> imulation Settings
> 2013
> 0.05
> 5.72%
> 0.00
> 0.11%
> 2.73%
> 0.38900
> 1385
> 1341
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
> Max Trade
> 2014
> 2.39
> 4.30%
> 1.51
> 4.98%
> 0.829
> 23.20900
> 1598
> 1548
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.66
> 4.4796
> .81
> 5.78%
> 0.929
> 25.889600
> 1648
> 1648
> 2016
> .20
> 4.01%
> 0.53
> 2.44%
> 8496
> 12.14%00
> 1602
> 1565
> 2017
> 4.39
> 4.63%
> 3.61
> 8.47%
> 0.91%
> 36.57900
> 1642
> 1601
> Clone Alpha 
> 2018
> 3.24
> 4.36%
> 2.38
> 6.73%
> 099
> 30.87900
> 869
> 1877
> 2019
> 2.57
> 4.28%
> 1.71
> 5.51%
> 0.879
> 25.73900
> 1683
> 1684
> 2020
> 3.21
> 4.899
> 2.37
> 6.84%
> 79%
> 27.96900
> 853
> 1696
> N
> Chart
> Pnl
> 2021
> 2.85
> 88%
> 89
> 5.51%
> 00%6
> 22.59900
> 2314
> 2177
> 2022
> 86
> 4.24%
> 02
> 3.79%
> 66%
> 17.88900
> 2127
> 2051
> 2023
> 2.89
> 4.419
> 2.24
> -7.48%
> .16%
> -33.90900
> 1883
> 1748
> Correlation
> Z,OOOK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Performance Comparison
> Last Run:
> 10 PASS
> 2WARNING
> Competition Al Alphas Competition 2025 does not match.
> Properties
> Last saved Mon, 11/17/2025,12:59 PM
> Theme IND Region Theme does not match with multiplier of 2。
> 5 PENDING
> Name
> Cateeorv


这个alpha op数6个，有亿点点多，尝试去掉power  ，robust也是能过的，优化完成✅


> [!NOTE] [图片 OCR 识别内容]
> d=(tail(a
> LOWer
> Upper
> newval
> 01 )
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> b=group_mean
> d,1, industry )-d;
> 2.37
> 4.569
> 1.48
> 4.909
> 2.819
> 21.47900
> quantile(b,
> driver
> gaussian,
> Sigma
> 1.01
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Urawdown
> Margin
> Long Count
> Short Count
> Simulation Settings
> 2013
> 0.11
> 5.72%
> 0.02
> 0.25%
> 2.81%
> 0.89900
> 1385
> 1341
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
> Max Trade
> 2014
> 2.41
> 4.29%
> 52
> 4.98%
> 0.80%
> 23.20900
> 1606
> 1540
> Equity
> ASI
> MINVOLIM
> Fast Expression
> 63
> 0.04
> Statistical
> On
> On
> Verify
> On
> 2015
> 2.79
> 4.46%
> 94
> 6.04%
> 0.92%
> 27.07900
> 1656
> 1640
> 2016
> 1.19
> 4.029
> 0.52
> 2.39%
> 909
> 11.9090o
> 1611
> 1556
> 2017
> 4.29
> 4.62%
> 3.47
> 8.20%
> 0.96%
> 35.52900
> 651
> 1591
> Clone Alpha 
> 2018
> 3.20
> 4.36%
> 33
> 6.61%
> 03%
> 30.33900
> 867
> 1879
> 2019
> 2.52
> 4.28%
> 65
> 5.39%6
> 0.88%
> 25.21900
> 686
> 682
> 2020
> 3.16
> 87%6
> 2.31
> 69%
> 7996
> 27.509oo
> 853
> 696
> Chart
> Pnl
> 2021
> 2.70
> 4.88%
> 1.75
> 5.24%6
> 9996
> 21.46900
> 2319
> 2172
> 2022
> 89
> 4.2596
> 05
> 3.84%
> 709
> 18.08300
> 2139
> 2039
> 2023
> 3.03
> 4.43%
> 2.39
> 7.78%
> 1.15%
> 35.07900
> 1887
> 1745
> Correlation
> 2,00OK
> Self Correlation
> Waximum
> Minimum
> Last Run:
> Power Pool Correlation
> Waximum
> Minimum
> Last Run:
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21
> Jan '22
> Jan '23
> Prod Correlation
> Waximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Performance Comparison
> Last Run:
> 10 PASS
> 2 WARNING
> 5 PENDING
> Properties
> Last saved Mon; 11/17/2025,8:17 PM
> Name
> Category
> Currently 'anonymous'
> NOne


结束语：

```
这个alpha，是需要反转的，考虑到我group_mean op这个季度还没用到，所以，我把 -group_neutralize 换成了group_mean(d,1,group)-d (来着研究小组同学的讨论分享，感谢) 
```

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢橘子姐姐的分享，橘子姐姐对op的应用真的让我叹为观止！
好好研究op和字段含义才是做好研究的不二法门。

================================Do your best ================================**


---

### 技术对话片段 11 (原帖: 附录：所有函数速查表)
- **原帖链接**: [Commented] DCC比赛Tutorial和代码详解代码优化.md
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，祝您发财
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 12 (原帖: 附录：所有函数速查表)
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，祝您发财
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 13 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] EUR TOPCS1600的经验解决Robust universe Sharpe  Sub-universe Sharpe  Weight concentration 问题经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (XW90844)**:
EUR TOPCS1600是最近新开放的炙手可热的universe。然而回测中经常遇到几个典型的问题：

- Robust universe Sharpe of 0.xx is below cutoff of 0.70.
- Sub-universe Sharpe of xx is below cutoff of 1.xx.
- Weight concentration xx% is above cutoff of 10% on mm/dd/yyyy.

尤其对新顾问，如果只看官方文档的解释和建议，更是一头雾水。但很多做过IND region的老顾问都明白，这是由于新区的数据覆盖率不足导致的，这次的TOPCS1600也是同理。这类问题很多靠ts_backfill和group_backfill就能解决。关键是 **分清到底是数据在哪个维度上覆盖率不足** 。

## **1. Date Coverage不足：用ts_backfill解决**

举例，imb5_score这个字段，Coverage 55%，Date coverage 100%，回测有warning “Weight is too strongly concentrated or too few instruments are assigned weight.”，表面看似乎是股票数量覆盖率不足。

但打开Visualization Chart中的Coverage Of Universe，可以看到实际覆盖率并不低（每天都在1300只股票以上），而是有特定的几天覆盖率为0。 
> [!NOTE] [图片 OCR 识别内容]
> Code
> imb5
> SCOre
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast
> Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> Chart
> Coverage Of Universe
> 1,000
> 500
>  Jul '14
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
>  Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
>  Jul '23
> Jan '24
> IS Testing Status
> Period
> 15
> Os
> 8 PASS
> 5WARNING
> Weight is too strongly concentrated ortoo few instruments are assigned weight。
> Delay


这种情况，简单的ts_backfill就能解决这个问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> ts_backfill
> imb5_score,
> 63)
> Simulation Settings
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> N Chart
> Coverage Of Universe
> 1,500
> 1,400
> 1,300
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> JUl'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul'20
> Jan '21
> Jul '21
> Jan '22
> JUl '22
> Jan '23
> Jul '23
> Jan '24


## **2. 股票数量Coverage不足：用group_backfill解决**

这是另一个基本面字段组合，回测报Robust universe Sharpe和特定日期Weight concentration问题。用同样的方法检查，发现时间序列上覆盖率没明显问题，但整体股票数量覆盖率较低（每天在800~1200只之间）。 
> [!NOTE] [图片 OCR 识别内容]
> reverse(ts
> std
> de
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUPIOIP|
> Ftness
> Returns
> OraMIdoINn
> Margin
> Simulation Settings
> 1.14
> 1.499
> 1.63
> 25.41 %
> 26.159
> 340.31%00
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.80
> 2.4396
> 5.58
> 49.6796
> 9.959
> 408.0096o
> 796
> 2015
> 1.79
> 1.19%
> 3.19
> 39.81%
> 12.20%6
> 667.149600
> 774
> 107
> Clone Alpha
> 2016
> 0.72
> 9896
> 0.82
> 16.1096
> 19.4490
> 162.339600
> 757
> 141
> 2017
> 68
> 1.0296
> 2.31
> 23.5596
> 9.159
> 459.639600
> 865
> 143
> 2018
> -0.97
> 8796
> '23
> -20.0796
> 25.73%
> 214.999600
> 872
> 165
> Chart
> Coverage Of Universe
> 2019
> 1.71
> 1.3796
> 80
> 33.5096
> 12.5096
> 487.519600
> 829
> 148
> 2020
> -016
> 0.849
> 10
> -5.0990
> 20.0796
> -121.119600
> 927
> 2021
> 49
> 0.6096
> 2.47
> 34.2496
> 13.5096
> 1,137
> 69600
> 954
> 24
> 2022
> 2.19
> 2.16%
> 09
> 67.56%
> 13.83%
> 626.759600
> 870
> 159
> 000
> 2023
> 0.92
> 1.4196
> 0.92
> 12.3996
> 14.989
> 176.239600
> 786
> 239
> 950
> Risk neutralized
> 900
> Aggregate Data
> Sharpe
> TITnOIe
> Fitnesc
> Retlrns
> OrlNdOWI
> Margin
> 0.60
> 1.499
> 0.58
> 11.849
> 28.239
> 158.549600
> 850
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> 22
> Jan '23
> Jul '23  Jan '24
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> 1 FAIL
> Robust universe Sharpe of 0.49 is below cUtoff of 0.70
> 5 WARNING
> Performance Comparison
> Sharpe of 1.14is below cutoff of 1.58.
> Weight concentration 36.81%
> above cUtoff of 10% on 4/12/2016.
> Rrln
> UVuAM
> Jul"


尝试应用ts_backfill后，也发现并不能增加覆盖率，Robust universe Sharpe也未改善。这就需要group_backfill了。

group_backfill(alpha, country, 126)，这种方式对覆盖率提升最多，但这种回填方式较糙，未解决Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts
> std
> deV
> group_backfill
> ts_backfill
> 126), country,
> 126 )
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TITnOVe
> Fitness
> Returns
> OraMdOINI
> Margin
> Simulation
> Settings
> 1.14
> 1.349
> 1.46
> 20.639
> 29.699
> 308.739600
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.70
> 2.4896
> 80
> 39.489
> 8.0996
> 318.249600
> 1097
> 256
> 2015
> 1.97
> 1.1396
> 3.14
> 31.699
> 9.1196
> 559.409600
> 1023
> 337
> Clone Alpha
> 2016
> 0.52
> 1.4190
> 0.35
> 5.5396
> 10.30%
> 78.759600
> 1062
> 315
> 2017
> 55
> 0.919
> 83
> 17.3896
> 8.439
> 381.309600
> 1214
> 290
> 2018
> 0.04
> 1.42%
> 0.01
> 0.70%
> 14.79%
> 889600
> 1318
> 228
> N Chart
> Coverage Of Universe
> 2019
> 66
> 1.1696
> 2.44
> 27.0696
> 8.6596
> 467.549600
> 1236
> 293
> 2020
> 42
> 1.15%
> 42
> 12.259
> 21.15%
> -213.929600
> 1315
> 248
> 2021
> 1.32
> 0.5596
> 2.06
> 30.3096
> 12.3896
> 1,096.429600
> 1505
> 88
> 2022
> 2.55
> 1.8196
> 58
> 59.769
> 7.8196
> 66
> 069600
> 1312
> 269
> 500
> 2023
> 0.33
> 3390
> 0.19
> 4.0290
> 18.3196
> 60.329600
> 1262
> 310
> 400
> Risk neutralized
> Aggregate Data
> Sharpe
> Trnowe
> Fitness
> RotIrn
> DraiNdoir
> Margin
> 0.55
> 1.349
> 0.46
> 8.58%
> 26.229
> 128.379600
> 300
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23
> Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run: -
> Power Pool Correlation
> Maximum
> Minimum
> Last Run: -
> IS Testing Status
> Period
> IS
> Os
> Prod Correlation
> Maximum
> Minimum
> Last Run: -
> 7 PASS
> 1FAIL
> Robust universe Sharpe of 0.56 is below cutoff of 0.70
> Long


group_backfill(alpha, subindustry, 126)，覆盖率中等提升，但这种基本面数据按照行业均值回填明显比按country回填更合理，成功解决了Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts_std_dev
> Eroup_
> backfill (ts
> backfill
> 126), subindustry,
> 126) ,
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnove
> Returns
> Drawdowr
> Margin
> Simulation Settings
> 1.45
> 1.2496
> 1.89
> 21.209
> 20.699
> 341.619600
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCS1G00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.50
> 2.5096
> 4.36
> 37.94%
> 9.2296
> 303.719600
> 981
> 148
> 2015
> 00
> 1.1696
> 2.96
> 27.30%
> 8.2696
> 469.739600
> 1014
> 147
> Clone Alpha
> 2016
> 0.78
> 1.449
> 0.69
> 9.73%
> 11.5596
> 135.269600
> 972
> 195
> 2017
> 80
> 0596
> 2.49
> 23.95%
> 6.7396
> 455.589600
> 1130
> 168
> 2018
> 0.17
> 1.1096
> -0.08
> -2.61%
> 18.3596
> -47.599600
> 1281
> N Chart
> Coverage Of Universe
> 2019
> 2.87
> 02%6
> 98
> 37.66%
> 6.81%
> 738.029600
> 1281
> 90
> 2020
> 0.45
> 0.8596
> 0.35
> 7.55%
> 5596
> 177.659600
> 1269
> 94
> 2021
> 62
> 0.6796
> 2.42
> 27.99%
> 80%6
> 830.179600
> 1349
> 55
> 2022
> 99
> 5896
> 3.15
> 31.31%
> 11.1496
> 395.639600
> 1261
> 121
> 300
> 2023
> 0.81
> .0196
> 0.73
> 10.16%
> 16.939
> 20
> 0096oo
> 1244
> 128
> 200
> Risk neutralized
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> Returns
> DrawdOWn
> Margin
> 0.74
> 1.249
> 0.62
> 8.679
> 19.639
> 139.739600
> 1,100
> JUl'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul'23 Jan '24
> Correlation
> Self Correlation
> MaYimIm
> NIinimrm
> 13c+
> Prn
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> Fitness of
> 89 is above cUtoff of
> Turnoverof
> .24%
> above cUtoff of 1 %
> Turnoverof
> .249
> below cUtOff of 709.
> Sub-universe Sharpe of 1.19 is above CUtOff of 0.77.
> Robust universe Sharpe of 0.79 is above Cutoff of 0.70.
> Fitnes


最后应用group_backfill(alpha, group_cartesian_product(country, subindustry), 126)，取得最佳效果： 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> Os
> reVerse(ts
> std_deV
> Broup_backfill(ts_backfill
> 126)
> group
> cartesian_product (country,
> subindus
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTnOVer
> Fitness
> Returns
> DrawdOWI
> Margin
> Simulation Settings
> 1.45
> 1.339
> 2.15
> 27.499
> 41.009
> 412.659600
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.25
> 64%6
> 4.10
> 41.43%
> 9.44%6
> 314.439600
> 898
> 137
> 2015
> 2.28
> 0.8796
> 67
> 32.309
> 10.769
> 738.519600
> 939
> 84
> Clone Alpha
> 2016
> 38
> 51%
> 1.74
> 19.9196
> 8.79%6
> 262.919600
> 844
> 195
> 2017
> 1.46
> 0.6996
> 2.13
> 26.6496
> 8.0396
> 774.909600
> 1046
> 119
> 2018
> 06
> 16%
> .37
> 20.86%
> 9.75%
> 358.649600
> 1143
> N Chart
> Coverage Of Universe
> 2019
> 2.67
> 0696
> 4.97
> 43.2996
> 9.3596
> 818.869600
> 1085
> 94
> 2020
> 1.12
> 0996
> 62
> 26.2996
> 33.209
> -48
> 879600
> 1149
> 2021
> 93
> 5396
> .38
> 38.2996
> 11.2796
> 1,444.509600
> 1211
> 26
> 2022
> 2.43
> 2.4796
> 5.22
> 57.7296
> 9.4696
> 466.629600
> 990
> 252
> 2023
> 0.89
> .2896
> 02
> 16.4996
> 23.889
> 257.429600
> 1065
> 176
> 100
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Returns
> DrawgOWn
> Margin
> 0.80
> 1.339
> 0.80
> 12.639
> 29.099
> 189.549600
> 000
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan "17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23 Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> o
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run: Fri, 02/27/2026,2:32 AW
> 8 PASS
> Fitness of 2.15 is aboVe cUtoff of
> 0.7002
> -0.3901
> Turnover of
> .339is above cUtoff Of 1%.
> Turnoverof-
> .33%
> below cUtoff of 70%
> Sub-universe Sharpe of 1.35
> aboVe cutoff of 0.77 _
> Robust universe Sharpe of 0.82 is above cutoff of 0.70.
> Long


有兴趣的还可以看Coverage by Industry图，限于篇幅就不细说了。总的来说，建议大家对某个idea大规模回测之前，先把各种group fields都用group_backfill试一下，找到最合适的回填方式，再大规模回测。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 14 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] EUR TOPCS1600的经验解决Robust universe Sharpe  Sub-universe Sharpe  Weight concentration 问题经验分享_38669179039255.md
- **时间**: 3个月前

**提问/主帖背景 (XW90844)**:
EUR TOPCS1600是最近新开放的炙手可热的universe。然而回测中经常遇到几个典型的问题：

- Robust universe Sharpe of 0.xx is below cutoff of 0.70.
- Sub-universe Sharpe of xx is below cutoff of 1.xx.
- Weight concentration xx% is above cutoff of 10% on mm/dd/yyyy.

尤其对新顾问，如果只看官方文档的解释和建议，更是一头雾水。但很多做过IND region的老顾问都明白，这是由于新区的数据覆盖率不足导致的，这次的TOPCS1600也是同理。这类问题很多靠ts_backfill和group_backfill就能解决。关键是 **分清到底是数据在哪个维度上覆盖率不足** 。

## **1. Date Coverage不足：用ts_backfill解决**

举例，imb5_score这个字段，Coverage 55%，Date coverage 100%，回测有warning “Weight is too strongly concentrated or too few instruments are assigned weight.”，表面看似乎是股票数量覆盖率不足。

但打开Visualization Chart中的Coverage Of Universe，可以看到实际覆盖率并不低（每天都在1300只股票以上），而是有特定的几天覆盖率为0。 
> [!NOTE] [图片 OCR 识别内容]
> Code
> imb5
> SCOre
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast
> Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> Chart
> Coverage Of Universe
> 1,000
> 500
>  Jul '14
> Jan '15
> Jul'15
> Jan '16
> Jul'16
> Jan '17
>  Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
>  Jul '23
> Jan '24
> IS Testing Status
> Period
> 15
> Os
> 8 PASS
> 5WARNING
> Weight is too strongly concentrated ortoo few instruments are assigned weight。
> Delay


这种情况，简单的ts_backfill就能解决这个问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> ts_backfill
> imb5_score,
> 63)
> Simulation Settings
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.02
> Fast Factors
> On
> Off
> Verify
> Off
> OFF
> Clone Alpha 
> N Chart
> Coverage Of Universe
> 1,500
> 1,400
> 1,300
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> JUl'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul'20
> Jan '21
> Jul '21
> Jan '22
> JUl '22
> Jan '23
> Jul '23
> Jan '24


## **2. 股票数量Coverage不足：用group_backfill解决**

这是另一个基本面字段组合，回测报Robust universe Sharpe和特定日期Weight concentration问题。用同样的方法检查，发现时间序列上覆盖率没明显问题，但整体股票数量覆盖率较低（每天在800~1200只之间）。 
> [!NOTE] [图片 OCR 识别内容]
> reverse(ts
> std
> de
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUPIOIP|
> Ftness
> Returns
> OraMIdoINn
> Margin
> Simulation Settings
> 1.14
> 1.499
> 1.63
> 25.41 %
> 26.159
> 340.31%00
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.80
> 2.4396
> 5.58
> 49.6796
> 9.959
> 408.0096o
> 796
> 2015
> 1.79
> 1.19%
> 3.19
> 39.81%
> 12.20%6
> 667.149600
> 774
> 107
> Clone Alpha
> 2016
> 0.72
> 9896
> 0.82
> 16.1096
> 19.4490
> 162.339600
> 757
> 141
> 2017
> 68
> 1.0296
> 2.31
> 23.5596
> 9.159
> 459.639600
> 865
> 143
> 2018
> -0.97
> 8796
> '23
> -20.0796
> 25.73%
> 214.999600
> 872
> 165
> Chart
> Coverage Of Universe
> 2019
> 1.71
> 1.3796
> 80
> 33.5096
> 12.5096
> 487.519600
> 829
> 148
> 2020
> -016
> 0.849
> 10
> -5.0990
> 20.0796
> -121.119600
> 927
> 2021
> 49
> 0.6096
> 2.47
> 34.2496
> 13.5096
> 1,137
> 69600
> 954
> 24
> 2022
> 2.19
> 2.16%
> 09
> 67.56%
> 13.83%
> 626.759600
> 870
> 159
> 000
> 2023
> 0.92
> 1.4196
> 0.92
> 12.3996
> 14.989
> 176.239600
> 786
> 239
> 950
> Risk neutralized
> 900
> Aggregate Data
> Sharpe
> TITnOIe
> Fitnesc
> Retlrns
> OrlNdOWI
> Margin
> 0.60
> 1.499
> 0.58
> 11.849
> 28.239
> 158.549600
> 850
> Jul'14
> Jan '15
> Jul '15
> Jan '16
> '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> 22
> Jan '23
> Jul '23  Jan '24
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 05
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> 1 FAIL
> Robust universe Sharpe of 0.49 is below cUtoff of 0.70
> 5 WARNING
> Performance Comparison
> Sharpe of 1.14is below cutoff of 1.58.
> Weight concentration 36.81%
> above cUtoff of 10% on 4/12/2016.
> Rrln
> UVuAM
> Jul"


尝试应用ts_backfill后，也发现并不能增加覆盖率，Robust universe Sharpe也未改善。这就需要group_backfill了。

group_backfill(alpha, country, 126)，这种方式对覆盖率提升最多，但这种回填方式较糙，未解决Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts
> std
> deV
> group_backfill
> ts_backfill
> 126), country,
> 126 )
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TITnOVe
> Fitness
> Returns
> OraMdOINI
> Margin
> Simulation
> Settings
> 1.14
> 1.349
> 1.46
> 20.639
> 29.699
> 308.739600
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.70
> 2.4896
> 80
> 39.489
> 8.0996
> 318.249600
> 1097
> 256
> 2015
> 1.97
> 1.1396
> 3.14
> 31.699
> 9.1196
> 559.409600
> 1023
> 337
> Clone Alpha
> 2016
> 0.52
> 1.4190
> 0.35
> 5.5396
> 10.30%
> 78.759600
> 1062
> 315
> 2017
> 55
> 0.919
> 83
> 17.3896
> 8.439
> 381.309600
> 1214
> 290
> 2018
> 0.04
> 1.42%
> 0.01
> 0.70%
> 14.79%
> 889600
> 1318
> 228
> N Chart
> Coverage Of Universe
> 2019
> 66
> 1.1696
> 2.44
> 27.0696
> 8.6596
> 467.549600
> 1236
> 293
> 2020
> 42
> 1.15%
> 42
> 12.259
> 21.15%
> -213.929600
> 1315
> 248
> 2021
> 1.32
> 0.5596
> 2.06
> 30.3096
> 12.3896
> 1,096.429600
> 1505
> 88
> 2022
> 2.55
> 1.8196
> 58
> 59.769
> 7.8196
> 66
> 069600
> 1312
> 269
> 500
> 2023
> 0.33
> 3390
> 0.19
> 4.0290
> 18.3196
> 60.329600
> 1262
> 310
> 400
> Risk neutralized
> Aggregate Data
> Sharpe
> Trnowe
> Fitness
> RotIrn
> DraiNdoir
> Margin
> 0.55
> 1.349
> 0.46
> 8.58%
> 26.229
> 128.379600
> 300
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23
> Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run: -
> Power Pool Correlation
> Maximum
> Minimum
> Last Run: -
> IS Testing Status
> Period
> IS
> Os
> Prod Correlation
> Maximum
> Minimum
> Last Run: -
> 7 PASS
> 1FAIL
> Robust universe Sharpe of 0.56 is below cutoff of 0.70
> Long


group_backfill(alpha, subindustry, 126)，覆盖率中等提升，但这种基本面数据按照行业均值回填明显比按country回填更合理，成功解决了Robust问题：


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> 0S
> reverse(ts_std_dev
> Eroup_
> backfill (ts
> backfill
> 126), subindustry,
> 126) ,
> 252)
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnove
> Returns
> Drawdowr
> Margin
> Simulation Settings
> 1.45
> 1.2496
> 1.89
> 21.209
> 20.699
> 341.619600
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCS1G00
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2014
> 2.50
> 2.5096
> 4.36
> 37.94%
> 9.2296
> 303.719600
> 981
> 148
> 2015
> 00
> 1.1696
> 2.96
> 27.30%
> 8.2696
> 469.739600
> 1014
> 147
> Clone Alpha
> 2016
> 0.78
> 1.449
> 0.69
> 9.73%
> 11.5596
> 135.269600
> 972
> 195
> 2017
> 80
> 0596
> 2.49
> 23.95%
> 6.7396
> 455.589600
> 1130
> 168
> 2018
> 0.17
> 1.1096
> -0.08
> -2.61%
> 18.3596
> -47.599600
> 1281
> N Chart
> Coverage Of Universe
> 2019
> 2.87
> 02%6
> 98
> 37.66%
> 6.81%
> 738.029600
> 1281
> 90
> 2020
> 0.45
> 0.8596
> 0.35
> 7.55%
> 5596
> 177.659600
> 1269
> 94
> 2021
> 62
> 0.6796
> 2.42
> 27.99%
> 80%6
> 830.179600
> 1349
> 55
> 2022
> 99
> 5896
> 3.15
> 31.31%
> 11.1496
> 395.639600
> 1261
> 121
> 300
> 2023
> 0.81
> .0196
> 0.73
> 10.16%
> 16.939
> 20
> 0096oo
> 1244
> 128
> 200
> Risk neutralized
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> Returns
> DrawdOWn
> Margin
> 0.74
> 1.249
> 0.62
> 8.679
> 19.639
> 139.739600
> 1,100
> JUl'14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul'23 Jan '24
> Correlation
> Self Correlation
> MaYimIm
> NIinimrm
> 13c+
> Prn
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run:
> 7 PASS
> Fitness of
> 89 is above cUtoff of
> Turnoverof
> .24%
> above cUtoff of 1 %
> Turnoverof
> .249
> below cUtOff of 709.
> Sub-universe Sharpe of 1.19 is above CUtOff of 0.77.
> Robust universe Sharpe of 0.79 is above Cutoff of 0.70.
> Fitnes


最后应用group_backfill(alpha, group_cartesian_product(country, subindustry), 126)，取得最佳效果： 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> IS
> Os
> reVerse(ts
> std_deV
> Broup_backfill(ts_backfill
> 126)
> group
> cartesian_product (country,
> subindus
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTnOVer
> Fitness
> Returns
> DrawdOWI
> Margin
> Simulation Settings
> 1.45
> 1.339
> 2.15
> 27.499
> 41.009
> 412.659600
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
> Max Trade
> Max Position
> Equity
> EUR
> TOPCSIG0O
> Fast Expression
> 0.05
> Market
> On
> Off
> Verify
> On
> OFF
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2014
> 2.25
> 64%6
> 4.10
> 41.43%
> 9.44%6
> 314.439600
> 898
> 137
> 2015
> 2.28
> 0.8796
> 67
> 32.309
> 10.769
> 738.519600
> 939
> 84
> Clone Alpha
> 2016
> 38
> 51%
> 1.74
> 19.9196
> 8.79%6
> 262.919600
> 844
> 195
> 2017
> 1.46
> 0.6996
> 2.13
> 26.6496
> 8.0396
> 774.909600
> 1046
> 119
> 2018
> 06
> 16%
> .37
> 20.86%
> 9.75%
> 358.649600
> 1143
> N Chart
> Coverage Of Universe
> 2019
> 2.67
> 0696
> 4.97
> 43.2996
> 9.3596
> 818.869600
> 1085
> 94
> 2020
> 1.12
> 0996
> 62
> 26.2996
> 33.209
> -48
> 879600
> 1149
> 2021
> 93
> 5396
> .38
> 38.2996
> 11.2796
> 1,444.509600
> 1211
> 26
> 2022
> 2.43
> 2.4796
> 5.22
> 57.7296
> 9.4696
> 466.629600
> 990
> 252
> 2023
> 0.89
> .2896
> 02
> 16.4996
> 23.889
> 257.429600
> 1065
> 176
> 100
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnove
> Fitness
> Returns
> DrawgOWn
> Margin
> 0.80
> 1.339
> 0.80
> 12.639
> 29.099
> 189.549600
> 000
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan "17
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> Jan '23
> Jul '23 Jan '24
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> Power Pool Correlation
> Maximum
> Minimum
> Last Run:
> o
> IS Testing Status
> Period
> IS
> 0S
> Prod Correlation
> Maximum
> Minimum
> Last Run: Fri, 02/27/2026,2:32 AW
> 8 PASS
> Fitness of 2.15 is aboVe cUtoff of
> 0.7002
> -0.3901
> Turnover of
> .339is above cUtoff Of 1%.
> Turnoverof-
> .33%
> below cUtoff of 70%
> Sub-universe Sharpe of 1.35
> aboVe cutoff of 0.77 _
> Robust universe Sharpe of 0.82 is above cutoff of 0.70.
> Long


有兴趣的还可以看Coverage by Industry图，限于篇幅就不细说了。总的来说，建议大家对某个idea大规模回测之前，先把各种group fields都用group_backfill试一下，找到最合适的回填方式，再大规模回测。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 15 (原帖: I observed that alpha neutralizing with MARKET sometimes gives a result quite close to alpha neutralizing with CROWDING.)
- **原帖链接**: https://support.worldquantbrain.com[Commented] I observed that alpha neutralizing with MARKET sometimes gives a result quite close to alpha neutralizing with CROWDING_39045701282583.md
- **时间**: 3个月前

**提问/主帖背景 (MZ45384)**:


**顾问 MS51256 (Rank 28) 的解答与建议**:
That's a really interesting observation! It makes sense that market-neutralization and crowding-neutralization could sometimes align, as both are implicitly trying to remove systematic market-driven exposure. Have you found this correlation to be stronger with certain types of alphas, perhaps those that are more sensitive to broad market movements or have a more pronounced style factor exposure? I'm curious about the underlying drivers you've seen for this overlap.


---

### 技术对话片段 16 (原帖: PPAC比赛技巧：使用Alpha List功能判断相关性 + 是否保留在Pool中经验分享)
- **原帖链接**: [Commented] PPAC比赛技巧使用Alpha List功能判断相关性  是否保留在Pool中经验分享.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
## **一、新人科普，组合（Power Pool) 背后的经济学原理？**

**降低非系统性风险** ：投资组合可以分散特定资产或特定行业的风险。例如，如果你只投资一家公司的股票，这家公司如果出现问题，你的投资可能会遭受重大损失。但如果投资多个不同行业的公司，即使其中一家公司出现问题，其他资产的表现可能会抵消部分损失。

**减少波动性** ：不同资产的价格波动可能不一致，甚至可能相互抵消。通过选择相关性较低的资产，可以降低组合的整体波动性，使投资组合更加稳定。

**提高夏普比率：** 夏普比率是衡量投资组合每单位风险所获得的超额回报的指标。通过构建低相关性的投资组合，可以在相同的预期回报下降低风险，从而提高夏普比率。

## **二、为什么低相关性更能提高Sharpe？**

高相关性的资产在价格波动上表现出相似性，这意味着它们在面对市场变化时会同时上涨或下跌。如果投资组合中包含大量高相关性的资产，那么组合的风险将集中在少数几个因素上，无法实现有效的风险分散。

如果两个资产的回报完全正相关（相关系数为1），那么它们的价格波动将完全一致，无法通过组合来降低风险。相反，如果两个资产的回报完全负相关（相关系数为-1），那么一个资产的上涨可以完全抵消另一个资产的下跌，从而最大程度地降低组合的风险。

夏普比率是衡量投资组合每单位风险所获得的超额回报的指标。通过降低组合的风险（即降低波动性），可以在相同的预期回报下提高夏普比率。当组合内的资产相关性较低时，组合的整体波动性降低，即使预期回报保持不变，夏普比率也会提高。

## 三、Alpha List 功能介绍

这个功能在平台的培训和资料中很少被讲到，我也是偶然发现的这个非常有用的功能，尤其是对这个比赛非常有帮助的功能。他可以选定一些特定的alpha，加入到自己构建的list中，


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 08/10/2024 EDT
> _fO_USa
> Add Alpha to a List
> 凸 Openalpha details innew 址
> Code
> pV1_


从而实现：

1. **对这些alpha的IS参数进行直观比较。**
2. **对这些alpha的pnl进行图形化对比。**
3. **对这些alpha的内在相关性直接计算。**

（注：这个inner correlation和self correlation不是完全一致，但可以近似）

**2.1 对参数直观比较的作用-优选高margin，低turnover**

我们知道比赛的平分标准分为BC （before cost) score和AC (after cost) score, 观察你的排行榜分数，如果AC的score较低则需要考虑对低margin的alpha进行移除，四个小时后进行观测AC score是否上涨


> [!NOTE] [图片 OCR 识别内容]
> List USA PPAC
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Search
> Select
> Select
> Select
> Search
> Select
> Select
> e.8>1
> @.8>1
> @.8>1
> Select
> 533.0
> Regular
> ACTIVE
> 04/14/2025 EDT
> USA
> TOP3000
> 1.38
> 5.84%
> 10.439
> Improve Perfor
> LMePzj2
> Regular
> UNSUBMITTED
> 04/14/2025 EDT
> USA
> TOP3000
> 1.63
> 4.289
> 8.429
> Self Correlation,
> anonymoUs
> Regular
> ACTIVE
> 04/14/2025 EDT
> USA
> TOP3000
> 1.25
> 3.229
> 6.909
> PowerPoolselec..
> 491.0
> Regular
> ACTIVE
> 04/13/2025 EDT
> USA
> TOP3000
> 1.17
> 2.789
> 7.739
> Improve Perfor
> anonymoUs
> Regular
> ACTIVE
> 04/13/2025 EDT
> USA
> TOP3000
> 1.42
> 7.71%
> 18.199
> PowerPoolSelec...
> anonymoUs
> Regular
> ACTIVE
> 04/13/2025 EDT
> USA
> TOP3000
> 1.52
> 3.509
> 16.25%
> PowerPoolSelec。
> Tag


**2.2 观测PNL，对比merge performance的pnl，进一步分析哪些不稳定的alpha可能需要剔除**

**
> [!NOTE] [图片 OCR 识别内容]
> Comparison Chart
> 7,00OK
> 6,00OK
> 5,OOOK
> 4,00OK
> 3,000K
> 05/06/2018
> 533.0.
> 1,992.78k
> anonymous: 1,710.00K
> 2,00OK
> 491.0:
> 1,009.02K
> anonymous: 2,630.98K
> anonymous: 2,173.79K
> COI
> 1,0OOK
> LMepzj2:
> 1,411.271
> Jul '13
> Jan '14
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> 533.0
> anonymous
> 491.0
> anonymous
> anonymous
> LMePzj2
> None
> All
**

**2.3 直观看到相关性，方便的看到是否新的alpha可以提交，并考虑移除已提交高相关alpha**

**
> [!NOTE] [图片 OCR 识别内容]
> Inner Correlation
> 533.0
> anonymous
> 491.0
> anonymous
> anonymous
> LMepzjz
> 533.0
> -0.0473
> 0.057
> -0.0278
> 0.0819
> 0.732
> anonymous
> -0.0473
> -0.0181
> -0.0003
> -0.0326
> -0.0659
> 491.0
> 0.057
> -0.0181
> 0.0323
> -0.0007
> 0.0713
> anonymous
> -0.0278
> -0.0003
> 0.0323
> -0.0158
> -0.0152
> anonymous
> 0.0819
> -0.0326
> -0.0007
> -0.0158
> 0.0685
> LMepzjz
> 0.732
> -0.0659
> 0.0713
> -0.0152
> 0.0685
**

**2.4 功能局限**

**每个List都最多有10个alpah，所以需要自己多做几个list，去进行一些切分管理（可以考虑按不同universe，不同pyramid，不同模版，不同turnover区间等）**

**最后预祝大家都取得好成绩，为国区争光！也记得Like呀！**

**顾问 MS51256 (Rank 28) 的解答与建议**:
非常实用的分享，目前比赛排名位于100名守门员，希望通过调整维持住！


---

### 技术对话片段 17 (原帖: PPAC比赛技巧：使用Alpha List功能判断相关性 + 是否保留在Pool中经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] PPAC比赛技巧使用Alpha List功能判断相关性  是否保留在Pool中经验分享_31447591579031.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
## **一、新人科普，组合（Power Pool) 背后的经济学原理？**

**降低非系统性风险** ：投资组合可以分散特定资产或特定行业的风险。例如，如果你只投资一家公司的股票，这家公司如果出现问题，你的投资可能会遭受重大损失。但如果投资多个不同行业的公司，即使其中一家公司出现问题，其他资产的表现可能会抵消部分损失。

**减少波动性** ：不同资产的价格波动可能不一致，甚至可能相互抵消。通过选择相关性较低的资产，可以降低组合的整体波动性，使投资组合更加稳定。

**提高夏普比率：** 夏普比率是衡量投资组合每单位风险所获得的超额回报的指标。通过构建低相关性的投资组合，可以在相同的预期回报下降低风险，从而提高夏普比率。

## **二、为什么低相关性更能提高Sharpe？**

高相关性的资产在价格波动上表现出相似性，这意味着它们在面对市场变化时会同时上涨或下跌。如果投资组合中包含大量高相关性的资产，那么组合的风险将集中在少数几个因素上，无法实现有效的风险分散。

如果两个资产的回报完全正相关（相关系数为1），那么它们的价格波动将完全一致，无法通过组合来降低风险。相反，如果两个资产的回报完全负相关（相关系数为-1），那么一个资产的上涨可以完全抵消另一个资产的下跌，从而最大程度地降低组合的风险。

夏普比率是衡量投资组合每单位风险所获得的超额回报的指标。通过降低组合的风险（即降低波动性），可以在相同的预期回报下提高夏普比率。当组合内的资产相关性较低时，组合的整体波动性降低，即使预期回报保持不变，夏普比率也会提高。

## 三、Alpha List 功能介绍

这个功能在平台的培训和资料中很少被讲到，我也是偶然发现的这个非常有用的功能，尤其是对这个比赛非常有帮助的功能。他可以选定一些特定的alpha，加入到自己构建的list中，


> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 08/10/2024 EDT
> _fO_USa
> Add Alpha to a List
> 凸 Openalpha details innew 址
> Code
> pV1_


从而实现：

1. **对这些alpha的IS参数进行直观比较。**
2. **对这些alpha的pnl进行图形化对比。**
3. **对这些alpha的内在相关性直接计算。**

（注：这个inner correlation和self correlation不是完全一致，但可以近似）

**2.1 对参数直观比较的作用-优选高margin，低turnover**

我们知道比赛的平分标准分为BC （before cost) score和AC (after cost) score, 观察你的排行榜分数，如果AC的score较低则需要考虑对低margin的alpha进行移除，四个小时后进行观测AC score是否上涨


> [!NOTE] [图片 OCR 识别内容]
> List USA PPAC
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Search
> Select
> Select
> Select
> Search
> Select
> Select
> e.8>1
> @.8>1
> @.8>1
> Select
> 533.0
> Regular
> ACTIVE
> 04/14/2025 EDT
> USA
> TOP3000
> 1.38
> 5.84%
> 10.439
> Improve Perfor
> LMePzj2
> Regular
> UNSUBMITTED
> 04/14/2025 EDT
> USA
> TOP3000
> 1.63
> 4.289
> 8.429
> Self Correlation,
> anonymoUs
> Regular
> ACTIVE
> 04/14/2025 EDT
> USA
> TOP3000
> 1.25
> 3.229
> 6.909
> PowerPoolselec..
> 491.0
> Regular
> ACTIVE
> 04/13/2025 EDT
> USA
> TOP3000
> 1.17
> 2.789
> 7.739
> Improve Perfor
> anonymoUs
> Regular
> ACTIVE
> 04/13/2025 EDT
> USA
> TOP3000
> 1.42
> 7.71%
> 18.199
> PowerPoolSelec...
> anonymoUs
> Regular
> ACTIVE
> 04/13/2025 EDT
> USA
> TOP3000
> 1.52
> 3.509
> 16.25%
> PowerPoolSelec。
> Tag


**2.2 观测PNL，对比merge performance的pnl，进一步分析哪些不稳定的alpha可能需要剔除**

**
> [!NOTE] [图片 OCR 识别内容]
> Comparison Chart
> 7,00OK
> 6,00OK
> 5,OOOK
> 4,00OK
> 3,000K
> 05/06/2018
> 533.0.
> 1,992.78k
> anonymous: 1,710.00K
> 2,00OK
> 491.0:
> 1,009.02K
> anonymous: 2,630.98K
> anonymous: 2,173.79K
> COI
> 1,0OOK
> LMepzj2:
> 1,411.271
> Jul '13
> Jan '14
> Jul '14
> Jan '15
> Jul '15
> Jan '16
> Jul '16
> Jan '17
> Jul'17
> Jan '18
> Jul'18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul '21
> Jan '22
> Jul '22
> 533.0
> anonymous
> 491.0
> anonymous
> anonymous
> LMePzj2
> None
> All
**

**2.3 直观看到相关性，方便的看到是否新的alpha可以提交，并考虑移除已提交高相关alpha**

**
> [!NOTE] [图片 OCR 识别内容]
> Inner Correlation
> 533.0
> anonymous
> 491.0
> anonymous
> anonymous
> LMepzjz
> 533.0
> -0.0473
> 0.057
> -0.0278
> 0.0819
> 0.732
> anonymous
> -0.0473
> -0.0181
> -0.0003
> -0.0326
> -0.0659
> 491.0
> 0.057
> -0.0181
> 0.0323
> -0.0007
> 0.0713
> anonymous
> -0.0278
> -0.0003
> 0.0323
> -0.0158
> -0.0152
> anonymous
> 0.0819
> -0.0326
> -0.0007
> -0.0158
> 0.0685
> LMepzjz
> 0.732
> -0.0659
> 0.0713
> -0.0152
> 0.0685
**

**2.4 功能局限**

**每个List都最多有10个alpah，所以需要自己多做几个list，去进行一些切分管理（可以考虑按不同universe，不同pyramid，不同模版，不同turnover区间等）**

**最后预祝大家都取得好成绩，为国区争光！也记得Like呀！**

**顾问 MS51256 (Rank 28) 的解答与建议**:
非常实用的分享，目前比赛排名位于100名守门员，希望通过调整维持住！


---

### 技术对话片段 18 (原帖: Request : Option to display dataset field used in alpha list page)
- **原帖链接**: [Commented] Request  Option to display dataset field used in alpha list page.md
- **时间**: 1年前

**提问/主帖背景 (MM98541)**:
The Submitted & Unsubmitted alpha list page has a lot of options to display likel Neutralization Universe, Sharpe, Turnover etc.

It would really help if there is an option to display the dataset used in the alpha. This would really help in focusing on & completing the uncompleted pyramids, with the Genius scoring in effect now.

**顾问 MS51256 (Rank 28) 的解答与建议**:
Adding a column to display the datasets used in each alpha would definitely enhance workflow efficiency, especially when trying to complete dataset pyramids or analyze alpha diversity. This feature could also help in identifying data overlap and improving overall strategy design. Hope the team considers implementing it soon!


---

### 技术对话片段 19 (原帖: Request : Option to display dataset field used in alpha list page)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Request  Option to display dataset field used in alpha list page_32414397367575.md
- **时间**: 1年前

**提问/主帖背景 (MM98541)**:
The Submitted & Unsubmitted alpha list page has a lot of options to display likel Neutralization Universe, Sharpe, Turnover etc.

It would really help if there is an option to display the dataset used in the alpha. This would really help in focusing on & completing the uncompleted pyramids, with the Genius scoring in effect now.

**顾问 MS51256 (Rank 28) 的解答与建议**:
Adding a column to display the datasets used in each alpha would definitely enhance workflow efficiency, especially when trying to complete dataset pyramids or analyze alpha diversity. This feature could also help in identifying data overlap and improving overall strategy design. Hope the team considers implementing it soon!


---

### 技术对话片段 20 (原帖: Super Alpha Competition 2025 Selection Expression)
- **原帖链接**: [Commented] Super Alpha Competition 2025 Selection Expression.md
- **时间**: 1年前

**提问/主帖背景 (VS18359)**:
What is the selection expression to select alphas with the classification 'SIMPLE'?

**顾问 MS51256 (Rank 28) 的解答与建议**:
in the ace2023  we can use the selection : ont(own)&&in (competitions,"ACE2023"）&&turnover<0.3&&prod_corrlation<0.5&&dataset_count<3
to choose those good alpha to combo a super alpha


---

### 技术对话片段 21 (原帖: Super Alpha Competition 2025 Selection Expression)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Super Alpha Competition 2025 Selection Expression_32838638764439.md
- **时间**: 1年前

**提问/主帖背景 (VS18359)**:
What is the selection expression to select alphas with the classification 'SIMPLE'?

**顾问 MS51256 (Rank 28) 的解答与建议**:
in the ace2023  we can use the selection : ont(own)&&in (competitions,"ACE2023"）&&turnover<0.3&&prod_corrlation<0.5&&dataset_count<3
to choose those good alpha to combo a super alpha


---

### 技术对话片段 22 (原帖: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location'])
- **原帖链接**: [Commented] Super alpha全自动回测代码--开箱即用代码优化.md
- **时间**: 1年前

**提问/主帖背景 (HW93328)**:
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
=======================================================================================
太强了，完美适配目前的比赛，
=-==========================================================================================================================================================================


---

### 技术对话片段 23 (原帖: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location'])
- **原帖链接**: https://support.worldquantbrain.com[Commented] Super alpha全自动回测代码--开箱即用代码优化_32637672256663.md
- **时间**: 1年前

**提问/主帖背景 (HW93328)**:
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
=======================================================================================
太强了，完美适配目前的比赛，
=-==========================================================================================================================================================================


---

### 技术对话片段 24 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] USA analyst一些具有经济学意义的重组数据字段_38927191768343.md
- **时间**: 3个月前

**提问/主帖背景 (YL20168)**:
之前利用workflow对现有的数据字段进行了重组，生成了一些具有经济学意义的新的数据，有的数据直接调用老的三阶模板就可以实现效果比较好的alpha，之前用这种方式把value factor从0.27提高到了>0.8，现在把之前生成的一些新的数据分享出来：

USA analyst：

act_12m_ebi_value / act_12m_sal_value

act_12m_net_value / act_12m_bps_value

act_12m_net_value / act_12m_roa_value

act_q_eps_value / act_q_bps_value

act_12m_sal_value - act_12m_cpx_value

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_consensus_2351

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v0_2389

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v1_2381

anl10_cpsfq1_pred_surps_v0_2389 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq1_pred_surps_v1_2381 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq1_pred_surps_v2_2364 - anl10_cpsfq1_pred_surps_v2_2364

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_consensus_2366

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v0_2365

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v1_2352

anl10_cpsfq2_pred_surps_v0_2365 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfq2_pred_surps_v1_2352 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfq2_pred_surps_v2_2379 - anl10_cpsfq2_pred_surps_v2_2379

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_consensus_2368

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v0_2378

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v1_2385

anl10_cpsfy1_pred_surps_v0_2378 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy1_pred_surps_v1_2385 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy1_pred_surps_v2_2383 - anl10_cpsfy1_pred_surps_v2_2383

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_consensus_2362

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v0_2356

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v1_2390

anl10_cpsfy2_pred_surps_v0_2356 - anl10_cpsfy2_pred_surps_v2_2360

anl10_cpsfy2_pred_surps_v1_2390 - anl10_cpsfy2_pred_surps_v2_2360

anl10_cpsfy2_pred_surps_v2_2360 - anl10_cpsfy2_pred_surps_v2_2360

anl14_actvalue_eps_fp0 / anl14_actvalue_revenue_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_eps_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_ndebt_fp0 / anl14_actvalue_roe_fp0

anl14_actvalue_ndebt_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_cfps_fp0 / anl14_actvalue_eps_fp0

anl14_actvalue_cfps_fp0 / anl14_actvalue_revenue_fp0

anl14_actvalue_revenue_fp0 / anl14_actvalue_cfps_fp0

anl14_actvalue_cfps_fp0 - anl14_actvalue_ndebt_fp0

anl44_2_ebitdaps_prevalue / anl44_2_bps_prevalue

anl44_2_ebitdaps_prevalue / anl44_2_nav_prevalue

anl44_2_netdebt_prevalue / anl44_2_bps_prevalue

anl44_2_netdebt_prevalue / anl44_2_nav_prevalue

anl44_2_capex_prevalue / anl44_2_ebitdaps_prevalue

anl44_2_nav_prevalue - anl44_2_netdebt_prevalue

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，向优秀的大佬学习

#========= WORLDQUANT BRAIN CONSULTANT ========== #
#每天进步一点点，加油
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================加油每一天=======================#


---

### 技术对话片段 25 (原帖: VF0.5->1.0->1.0->1.0->?,1.0体验卡结束后的总结与思考【指标分析篇】经验分享)
- **原帖链接**: [Commented] VF05-10-10-10-10体验卡结束后的总结与思考【指标分析篇】经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (HW93328)**:
6、7、8月的VF终于是更新了，在幸运的拿到三个月的1.0体验卡后也终于产生了变化，最新的VF下降到了0.85。之前一直没有完整的总结分析过过往几个月提交的alpha的情况，所以也借着次更新变动的契机来做一个基于alpha指标的分析总结。在分析过程中会得出一些可能的结论，纯个人总结猜测，不一定为真。

看到有顾问朋友问拿到了高VF怎么交能拿高base，欢迎看看我的上一篇帖子

1.指标数据概览


> [!NOTE] [图片 OCR 识别内容]
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> sharpe
> 1.684
> 1.82
> 1.815
> 1.794
> 1.619
> fitness
> 1.812
> 1.587
> 1.461
> 1.513
> 1.415
> returns
> 0.193
> 0.119
> 0.106
> 0.118
> 0.118
> turnoVer
> 0.108
> 0.098
> 0.101
> 0.113
> 0.101
> margin
> 0.005
> 0.004
> 0.003
> 0.003
> 0.004
> Self cor
> 0.184
> 0.036
> 0.346
> 0.441
> 0.263
> prod_cor
> 0.255
> 0.475
> 0.752
> 0.755
> 0.671
> Count
> 15.0
> 71.0
> 68.0
> 74.0
> 91.0


我是今年4月底成为的consultant，因子在2025-04只提交了少量的alpha，所以在后面的分析中，不把4月的指标做重要考虑。我首次刷新VF是在3、4、5这个时间窗口内，对于我来说也就是4、5两个月的alpha数据。

4、5月-->1.0 4、5、6月-->1.0 5、6、7-->1.0 6、7、8月-->0.85

从这四次VF的刷新中不难看出，5月的alpha数据在三次1.0中应该是起到了比较大的作用，毕竟5月的窗口过去之后VF就产生了较大变化。如果只从各个指标的avg数据上来看，2025-08的平均指标确实要比2025-05差上一些，但整体上我觉得是一个可接受波动范围。（8月开始为了genius可能交了一些指标没有那么好的alpha）

**结论1: 在WQ，从不缺少优秀的consultant，不进则是退。**

关于super alpha我这次没有做详细指标统计，我从6月的比赛开始陆续做sa，7月、8月提交的基本都是指标较好的super alpha（base图中sa收入也是占大头），暂时不能判断sa对于VF的影响，也许要等到下次VF刷新时再观察。但如果是sa之前交的很少，那多交一些sa应该是有助于VF的。


> [!NOTE] [图片 OCR 识别内容]
> 2025-04 to 2025-06
> 2025-05 to 2025-07
> 2025-06 to 2025-08
> sharpe
> 1.805
> 1.809
> 1.732
> fitness
> 1.554
> 1.521
> 1.459
> returns
> 0.12
> 0.114
> 0.115
> turnover
> 0.101
> 0.104
> 0.105
> margin
> 0.004
> 0.003
> 0.003
> Self Cor
> 0.187
> 0.276
> 0.344
> prod
> COI
> 0.576
> 0.661
> 0.721
> Count
> 154
> 213
> 233


从3个月的平均指标上来看，确实是比之前低一些的。在5月时貌似有个bug，有些ra提交后其prod会显示为0，所以在统计上5月的pc指标上就明显低了一些。

2.指标分布情况


> [!NOTE] [图片 OCR 识别内容]
> sharpe comparison
> fitness comparison
> returns comparison
> 1.0
> 1.0
> 0.8
> 0.8
> 0.6
> 0.6
> 
> 
> 喜
> 3
> 0.4
> 0.4
> 2
> 0.2
> 0.2
> 0.0
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> Sharpe
> fitness
> returns
> turnover comparison
> margin comparison
> prod_cor comparison
> 2.5
> 200
> 175
> 2.0
> 150
> 125
> 1.5
> 
> 3
> 喜
> 100
> 
> 1.0
> 75
> 2
> 50
> 0.5
> 25
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 0.00
> 0.01
> 0.02
> 0.03
> 0.04
> -0.2
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> turnover
> margin
> prod_cor


图片中蓝色为567月时间窗口中的指标分布，黄色为678月。上图中有较明显变化的是sharpe、turnover和prod，sharpe上明显低的个数变多了，turnover上30%-40%这块有所增加（温和的turnover是ok的，但这个区间明显偏高了）。prod上还算正常，有高有低。

5、6、7月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆
> 豆20
> 豆40
> 1.5
> 20
> 2.5
> 30
> 35
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 2.5
> 30
> 35
> 4.0
> 4.5
> 0.4
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 100
> 豆
> 8
> 豆 15
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 0005
> 0010
> 0.015
> 0.020
> 0.025
> 0030
> 0035
> 0.040
> 0.4
> 06
> 1.0
> bUrOVeT
> margIn
> Prod
> COI


6、7、8月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆20
> 豆20
> 豆
> 1.0
> 1.5
> 2.0
> 2.5
> 30
> 3.5
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 25
> 30
> 3.5
> 40
> 45
> U0
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 20.0
> 17.5
> 15.0
> 12.5
> 8
> 8
> 10.0
> 7.5
> 50
> 25
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 005
> 0010
> 0015
> 020
> 0.2
> 0.3
> 0.4
> 05
> 0.6
> 07
> 0.8
> 0.9
> 1.0
> WUrnoVeT
> margIn
> Prod
> COI
> 豆


其实我个人从以上指标分布的对比中没有感觉出特别明显的差异，我提交因子时也会把握一个标准，从日常提交上来说也没有太大差异。

结论2: 做好自己的研究，剩下的交给系统

影响VF的因素实在太多了，数量、diversity、OS、成长表现、rank等等等等，不可能做到面面具到，只有尽量做出好alpha，提交符合自己审美的alpha，尽力就好。

3.地区/数据集分布


> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/DI
> 100
> 37.88%
> EUR/DI
> 88
> 33.33%
> ASIID1
> 46
> 17.42%
> GLB/DI
> 30
> 11.36%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> MODEL
> 54
> 20.45%
> RISK
> 39
> 14.77%
> FUNDAMENTAL
> 31
> 11.74%
> PV
> 31
> 11.74%
> ANALYST
> 30
> 11.36%
> OTHER
> 19
> 7.20%
> NEWS
> 15
> 5.68%
> OPTION
> 3.79%
> MACRO
> 9
> 2.65%
> SENTIMENT
> 7
> 2.65%
> INSTITUTIONS
> 7
> 2.65%
> EARNINGS
> 2.65%
> INSIDERS
> 3
> 1.14%
> SOCIALMEDIA
> 2
> 0.76%
> SHORTINTEREST
> 2
> 0.76%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/D1
> 38.68%
> EUR/D1
> 5
> 19.86%
> ASIID1
> 42
> 14.63%
> AMR/D1
> 31
> 10.80%
> GLB/D1
> 25
> 8.71%
> JPNIDI
> 21
> 7.32%
> Total
> 287
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> ANALYST
> 39
> 13.59%
> MODEL
> 37
> 12.89%
> RISK
> 35
> 12.20%
> FUNDAMENTAL
> 33
> 11.50%
> PV
> 33
> 11.50%
> OTHER
> 26
> 9.06%
> OPTION
> 5.92%
> NEWS
> 1
> 5.57%
> SENTIMENT
> 3.83%
> INSTITUTIONS
> "
> 2.79%
> EARNINGS
> 7
> 2.44%
> INSIDERS
> 7
> 2.44%
> SHORTINTEREST
> 6
> 2.09%
> SOCIALMEDIA
> 6
> 2.09%
> MACRO
> 4
> 1.39%
> BROKER
> 2
> 0.70%
> Total
> 287
> 100.00%


8月下旬开始陆陆续续开始交了一些jpn和amr的alpha，数量不多，可能是组合中不稳定的来源。D0听说也比较难，我还没有尝试过。

最后，现在无论是genius还是vf，竞争都很激烈，还是要努力提升自己，多交高质量的alpha！祝各位vf常高，base长红～

（结论3:新顾问要抓住机会，刚开始时的成长贡献可能会带给你一个高VF）

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢大佬的分享，三次1.0是非常难的，跌下来也是必不可免的，毕竟冲刺了gm就要有所取舍。

能再分析一下吗，这次作者的更新vf是0.45  9月份究竟交了什么抽象因子导致降低这么多。

================================Do your best ================================**


---

### 技术对话片段 26 (原帖: VF0.5->1.0->1.0->1.0->?,1.0体验卡结束后的总结与思考【指标分析篇】经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] VF05-10-10-10-10体验卡结束后的总结与思考【指标分析篇】经验分享_35880708570391.md
- **时间**: 6个月前

**提问/主帖背景 (HW93328)**:
6、7、8月的VF终于是更新了，在幸运的拿到三个月的1.0体验卡后也终于产生了变化，最新的VF下降到了0.85。之前一直没有完整的总结分析过过往几个月提交的alpha的情况，所以也借着次更新变动的契机来做一个基于alpha指标的分析总结。在分析过程中会得出一些可能的结论，纯个人总结猜测，不一定为真。

看到有顾问朋友问拿到了高VF怎么交能拿高base，欢迎看看我的上一篇帖子

1.指标数据概览


> [!NOTE] [图片 OCR 识别内容]
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> sharpe
> 1.684
> 1.82
> 1.815
> 1.794
> 1.619
> fitness
> 1.812
> 1.587
> 1.461
> 1.513
> 1.415
> returns
> 0.193
> 0.119
> 0.106
> 0.118
> 0.118
> turnoVer
> 0.108
> 0.098
> 0.101
> 0.113
> 0.101
> margin
> 0.005
> 0.004
> 0.003
> 0.003
> 0.004
> Self cor
> 0.184
> 0.036
> 0.346
> 0.441
> 0.263
> prod_cor
> 0.255
> 0.475
> 0.752
> 0.755
> 0.671
> Count
> 15.0
> 71.0
> 68.0
> 74.0
> 91.0


我是今年4月底成为的consultant，因子在2025-04只提交了少量的alpha，所以在后面的分析中，不把4月的指标做重要考虑。我首次刷新VF是在3、4、5这个时间窗口内，对于我来说也就是4、5两个月的alpha数据。

4、5月-->1.0 4、5、6月-->1.0 5、6、7-->1.0 6、7、8月-->0.85

从这四次VF的刷新中不难看出，5月的alpha数据在三次1.0中应该是起到了比较大的作用，毕竟5月的窗口过去之后VF就产生了较大变化。如果只从各个指标的avg数据上来看，2025-08的平均指标确实要比2025-05差上一些，但整体上我觉得是一个可接受波动范围。（8月开始为了genius可能交了一些指标没有那么好的alpha）

**结论1: 在WQ，从不缺少优秀的consultant，不进则是退。**

关于super alpha我这次没有做详细指标统计，我从6月的比赛开始陆续做sa，7月、8月提交的基本都是指标较好的super alpha（base图中sa收入也是占大头），暂时不能判断sa对于VF的影响，也许要等到下次VF刷新时再观察。但如果是sa之前交的很少，那多交一些sa应该是有助于VF的。


> [!NOTE] [图片 OCR 识别内容]
> 2025-04 to 2025-06
> 2025-05 to 2025-07
> 2025-06 to 2025-08
> sharpe
> 1.805
> 1.809
> 1.732
> fitness
> 1.554
> 1.521
> 1.459
> returns
> 0.12
> 0.114
> 0.115
> turnover
> 0.101
> 0.104
> 0.105
> margin
> 0.004
> 0.003
> 0.003
> Self Cor
> 0.187
> 0.276
> 0.344
> prod
> COI
> 0.576
> 0.661
> 0.721
> Count
> 154
> 213
> 233


从3个月的平均指标上来看，确实是比之前低一些的。在5月时貌似有个bug，有些ra提交后其prod会显示为0，所以在统计上5月的pc指标上就明显低了一些。

2.指标分布情况


> [!NOTE] [图片 OCR 识别内容]
> sharpe comparison
> fitness comparison
> returns comparison
> 1.0
> 1.0
> 0.8
> 0.8
> 0.6
> 0.6
> 
> 
> 喜
> 3
> 0.4
> 0.4
> 2
> 0.2
> 0.2
> 0.0
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> Sharpe
> fitness
> returns
> turnover comparison
> margin comparison
> prod_cor comparison
> 2.5
> 200
> 175
> 2.0
> 150
> 125
> 1.5
> 
> 3
> 喜
> 100
> 
> 1.0
> 75
> 2
> 50
> 0.5
> 25
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 0.00
> 0.01
> 0.02
> 0.03
> 0.04
> -0.2
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> turnover
> margin
> prod_cor


图片中蓝色为567月时间窗口中的指标分布，黄色为678月。上图中有较明显变化的是sharpe、turnover和prod，sharpe上明显低的个数变多了，turnover上30%-40%这块有所增加（温和的turnover是ok的，但这个区间明显偏高了）。prod上还算正常，有高有低。

5、6、7月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆
> 豆20
> 豆40
> 1.5
> 20
> 2.5
> 30
> 35
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 2.5
> 30
> 35
> 4.0
> 4.5
> 0.4
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 100
> 豆
> 8
> 豆 15
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 0005
> 0010
> 0.015
> 0.020
> 0.025
> 0030
> 0035
> 0.040
> 0.4
> 06
> 1.0
> bUrOVeT
> margIn
> Prod
> COI


6、7、8月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆20
> 豆20
> 豆
> 1.0
> 1.5
> 2.0
> 2.5
> 30
> 3.5
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 25
> 30
> 3.5
> 40
> 45
> U0
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 20.0
> 17.5
> 15.0
> 12.5
> 8
> 8
> 10.0
> 7.5
> 50
> 25
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 005
> 0010
> 0015
> 020
> 0.2
> 0.3
> 0.4
> 05
> 0.6
> 07
> 0.8
> 0.9
> 1.0
> WUrnoVeT
> margIn
> Prod
> COI
> 豆


其实我个人从以上指标分布的对比中没有感觉出特别明显的差异，我提交因子时也会把握一个标准，从日常提交上来说也没有太大差异。

结论2: 做好自己的研究，剩下的交给系统

影响VF的因素实在太多了，数量、diversity、OS、成长表现、rank等等等等，不可能做到面面具到，只有尽量做出好alpha，提交符合自己审美的alpha，尽力就好。

3.地区/数据集分布


> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/DI
> 100
> 37.88%
> EUR/DI
> 88
> 33.33%
> ASIID1
> 46
> 17.42%
> GLB/DI
> 30
> 11.36%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> MODEL
> 54
> 20.45%
> RISK
> 39
> 14.77%
> FUNDAMENTAL
> 31
> 11.74%
> PV
> 31
> 11.74%
> ANALYST
> 30
> 11.36%
> OTHER
> 19
> 7.20%
> NEWS
> 15
> 5.68%
> OPTION
> 3.79%
> MACRO
> 9
> 2.65%
> SENTIMENT
> 7
> 2.65%
> INSTITUTIONS
> 7
> 2.65%
> EARNINGS
> 2.65%
> INSIDERS
> 3
> 1.14%
> SOCIALMEDIA
> 2
> 0.76%
> SHORTINTEREST
> 2
> 0.76%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/D1
> 38.68%
> EUR/D1
> 5
> 19.86%
> ASIID1
> 42
> 14.63%
> AMR/D1
> 31
> 10.80%
> GLB/D1
> 25
> 8.71%
> JPNIDI
> 21
> 7.32%
> Total
> 287
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> ANALYST
> 39
> 13.59%
> MODEL
> 37
> 12.89%
> RISK
> 35
> 12.20%
> FUNDAMENTAL
> 33
> 11.50%
> PV
> 33
> 11.50%
> OTHER
> 26
> 9.06%
> OPTION
> 5.92%
> NEWS
> 1
> 5.57%
> SENTIMENT
> 3.83%
> INSTITUTIONS
> "
> 2.79%
> EARNINGS
> 7
> 2.44%
> INSIDERS
> 7
> 2.44%
> SHORTINTEREST
> 6
> 2.09%
> SOCIALMEDIA
> 6
> 2.09%
> MACRO
> 4
> 1.39%
> BROKER
> 2
> 0.70%
> Total
> 287
> 100.00%


8月下旬开始陆陆续续开始交了一些jpn和amr的alpha，数量不多，可能是组合中不稳定的来源。D0听说也比较难，我还没有尝试过。

最后，现在无论是genius还是vf，竞争都很激烈，还是要努力提升自己，多交高质量的alpha！祝各位vf常高，base长红～

（结论3:新顾问要抓住机会，刚开始时的成长贡献可能会带给你一个高VF）

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢大佬的分享，三次1.0是非常难的，跌下来也是必不可免的，毕竟冲刺了gm就要有所取舍。

能再分析一下吗，这次作者的更新vf是0.45  9月份究竟交了什么抽象因子导致降低这么多。

================================Do your best ================================**


---

### 技术对话片段 27 (原帖: VF第一次更新从0.5-0.88的感想)
- **原帖链接**: https://support.worldquantbrain.com[Commented] VF第一次更新从05-088的感想_38209592294167.md
- **时间**: 3个月前

**提问/主帖背景 (ZL75781)**:
大家好！我是ZL75781。做为从2025年10月进来的新顾问来和大家分享一下我从0.5到0.88的感想。

这次VF更新是9 10 11 这三个月，刚好OS也更新了，我给大家看看我这三个月交了些什么。

我一共是交了34个，其中IND地区8个。 
> [!NOTE] [图片 OCR 识别内容]
> (EST
> Correlation
> Sea
> Select
> Select
> Select
> 09/01/2025
> 11/30e1
> IND
> Select
> Select
> Ce
> eE>1
> Ce
> Ce
> Select
> Ce
> Ce
> Ce
> SOOO
> ReSUIaT
> ACTIVE
> 11/2512025 EST
> INC
> TOPSDD
> 5.04
> 14549
> 3057-
> 5.33
> 4.55
> 0.53
> 1800
> Resular
> ACTIE
> 11/2112025 EST
> IND
> TOPSDO
> 3.533
> 21.239
> 15.915
> 3.15
> 2.71
> 0.53
> ZOOO
> Resular
> ACTIE
> 11/2612025 EST
> IND
> TOPSDO
> 3.55
> 4.5795
> 37265
> 452
> 3.75
> 405
> 300
> Resular
> ACTIVE
> 11/24/2025 EST
> IND
> TOPSDO
> 3.54
> 13.0695
> 2432
> 401
> 0.35
> 3.97
> 0.53
> 5O0
> Regular 
> ACTIVE
> 11/2112025 EST
> IND
> TOPSDO
> 2.82
> 18.5895
> 1320*
> 2.29
> IND;
> 4.22
> 3.78
> 0.72
> 700
> Resular 
> ACTIVE
> 11/2112025 EST
> IND
> TOPSDO
> 0.13
> 9.3395
> 58N
> 0.05
> IND
> 490 
> 2.13
> 0.57
> F 
> O5GPC
> Regular 
> ACTIVE
> 11120/2025 EST
> IND
> TOPSDO
> 2.32
> 5.7595
> 4023
> 2.23
> IND;
> -0.43
> 2.03
> 0.55
> 牺
> 5O0
> Regular 
> ACTIVE
> 11/20/2025 EST
> IND
> TOPSDO
> 0.50 
> 4.2195
> 8.958
> 0.19
> 0.83
> 0.59


可以看到我IND地区的sharpe125都非常不错，但是有两个不好的因子存在。

而我的EUR/1地区相比之下逊色不少


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Unierse
> Delay
> Sharpe
> Tumover
> Margin
> Fitness
> Tag
> Sharpe 60
> Sharpe 125
> Prod
> (EST
> Correlation
> Search
> See
> See
> See
> 03/01/2025
> 11/30
> EUR
> See
> 巳吕>
> e吕>
> e吕>
> e吕>
> See
> e吕>
> e吕>
> e吕>
> anonymous
> Regular
> ACTIVE
> 10/2112025 EDT
> EUR 
> TOP250O
> 2.31
> 15.0595 
> 8.79*
> 1.53
> 5.55
> 3.73
> 0.51 
> aORJMOUs
> ReSular
> ACTIVE
> 10/2612025 EDT
> EUR
> TOPZSOO
> 0.35
> 5.5435
> .79*
> 2.55
> 1.33
> 0.70
> anonymOUs
> SUPer
> ACTIVE
> 10/2612025 EDT
> EUR
> TOPZSOO
> 2.20
> 11.0531
> 11.04-
> 1.34
> 1.33
> 0.54
> P0.52
> Resular
> ACTIVE
> 10/1612025 EDT
> EUR
> TOPZSOO
> 0.54
> 15.7893
> 2.105
> 0.21
> T2-
> 0.54
> 0.53
> RESUlar
> ACTIVE
> 10/142025 EDT
> EUR
> TOPZSOO
> 0.03
> 11.4293
> 0205
> -0.07
> 7.34
> 1.13
> 0.55
> RESUlar
> ACTIVE
> 10/1212025 EDT
> EUR
> TOPZSOO
> 0.92
> 24.1595
> 2.12*
> 0.30
> 1.02
> 0.53
> EUR_I_EQUIT..
> Regular 
> ACTIVE
> 10/2312025 EDT
> EUR
> TOPZSOO
> 3.2195
> 35.46*
> 1.23
> EUR_I_EQUITY_-
> 0.22
> 0.95
> 0.59
> TIIAO
> RESUlar
> ACTIVE
> 10/1712025 EDT
> EUR
> TOPZSOO
> 0.33
> 5.2593
> 12.775
> 0.+5
> test C
> 1.31
> 7.92
> 0.70
> RESUlaT
> ACTIVE
> 10/2-2025 EDT
> EUR
> TOPZSOO
> 1.02
> 4349
> 55
> 0.47
> 7.33
> 0.42
> 0.53
> :
> EUR_I_EQUITY.. 
> Regular 
> ACTIVE
> 10/09/2025 EDT
> EUR
> TOPZSOO
> 1.13
> 3.1535
> 85*
> 0.52
> EUR_I_EQUITY_-
> 1.10
> 1
> 0.59
> Regular
> ACTIVE
> 10/1112025 EDT
> EUR
> TOPZSOO
> 0.21
> 24.4893
> 040t
> 0.03
> 0.33
> 0.15
> 0.53
> IIFING
> ReSUlar
> ACTIVE
> 10/1412025 EDT
> EUR
> TOPZSOO
> 0.97
> 12.91353
> 36*
> 0.50
> -0.53
> 0.45


最最不好的是EUR/0地区出现了，这个是我新手时期不懂事交上去的高turnover低margin。可以看出来是非常的不好，但是我认为，这些“不好的因子”其实也是为我别样的多样性进行一个提升。让我能够有机会获得到0.88的这个vf值。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Unrerse
> Delay
> Sharpe
> Turnover
> Margin
> Fitness
> Tag
> Sharpe 60
> Sharpe 125
> Prod
> IEST
> Correlation
> 423TCh
> Select
> Select
> Select
> 09/01/2025
> 11/30
> USA
> Select
> Select
> aORJIOUS
> Regular 
> ACTIVE
> 11/1612025 EST
> US4
> TOP3DOO
> 0.32
> 65.9395
> 0.61*
> 0.14
> 3.25
> 1.03
> 0.75
> 0.7734
> Regular
> ACTIVE
> 11/19/2025 EST
> US4
> TOP3DOO
> 0.73
> 8.5595
> -8436
> 0.33
> 1111.
> -1.33
> 0.05
> 0.7127
> ReSUlar
> ACTIVE
> 11/1312025 EST
> US4
> TOP3OOO
> -0.31
> 4.369
> -3325
> -0.03
> 1111,
> 1.75
> 0.41
> 0.70
> anonymous
> ReSUlar
> ACTIVE
> 11/1112025 EST
> US4
> TOP3OOO
> 14.1393
> 45
> 0.33
> 0.43
> 0.33
> 0.53
> 056 CON
> Resular
> ACTIVE
> 11/0412025 EST
> US4
> TOP3OOO
> 0.45
> 4.343
> 5.05-
> 0.14
> 0.37
> 0.34
 同样不好的还有USA地区，可以说是暴雷地区了，对于我来说，也是非常不好的一个地区。

最后还有一个GLB地区，我只交了一个，这个是当时有个活动安排你去跑各种地区，我分配到了GLB和USA，然后我去尝试结果没注意数量，这也为我下一篇文章做了一个铺垫。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> UnNerse
> Delay
> Sharpe
> Tumover
> Margin
> Fitness
> Tag
> Sharpe 60
> Sharpe 125
> Prod
> (EST
> Correlation
> Search
> SeEO
> SeEO
> SeEO
> 03/01/2025
> 11/30
> GLE
> SeEO
> C8
> C8
> C8
> 2吕>1
> SeEO
> C8
> e吕>
> C8
> aOHYITOUs
> ReSUlar
> ACTIE
> 11/0312025 EST
> GLs
> NINVOLIN
> 0.24
> 35.3695
> -0215
> 0.02
> 0.52
> -2.17


可以从上面的这些看出来，至少你得有一个地区得做的好能够去吧不好的地区带起来。

但是现在的我认为，不要为了冲塔冲活动而去乱交一些因子，让自己懊悔。交因子之前要有一定的预判能力例如，


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 003k
> OODK
> 03JK
> OJJK
> 00JK
> 403OK
> 3,00OK
> OJJK
> 03JK
> 03'27/201-
> Pnl  361+5K
> 2014
> 2015
> 2016
> 2017
> 2013
> 2019
> 2020
> 2021
> 2022
> 2023



> [!NOTE] [图片 OCR 识别内容]
> OS Summary
> Period
> 酏
> Dazs Set Apha
> 酣 Power Pool Alpha
> Pyramid theme- USAIDIIMODEL <1.3
> Start Date
> Snarpe
> TUTTTU
> Fitness
> ReUTns
> JralOIAT
> Warsin
> 01/21/2023 Es
> 0.73
> 8.65%
> 0.39
> 3.65%
> 5.72%
> 8.439600
> Sharpe 60
> Sharpe 125
> Sharp  250
> Sharpe 5O0
> 05/15 Ratio
> Pre Clos  Sharpe
> Pre Close Ratio
> Self Corelation
> 0.35
> 3.33
> Year
> Shrpe
> Tumower
> Ftness
> Returts
> Orawdown
> Nargin
> Long Count
> Short Count
> 2713
> 1.10
> SJ9:
> 0.52
> 2.7沿
> 141
> 3.7
> 13
> 149
> 201-
> 1.S0
> 5.759:
> 5.33汩
> 731
> 17.293
> 1536
> T
> 2015
> 1.SO
> 7.279
> 5.22沾
> 82沾
> 14.39
> 1526
> 1511
> 2716
> 829
> 1.21
> 7.35汩
> 2.23
> SCT
> 1518
> 1575
> 2017
> 0E2
> S29:
> 1.25
> 212汩
> 2.55
> .314
> 1553
> 112
> 2018
> 224
> 359
> 1.73
> 7.4沾
> 731
> 20.25
> 1553
> 1450
> 2013
> 1.92
> 5.305
> 85:
> TRo
> 143E
> 2027
> ZTE
> 3.63
> 22.37汩
> 47
> 52.324
> 1553
> 1537
> 2721
> 243
> Sq:
> 2.32
> 15.34汩
> 87
> 一1
> 1773
> 10
> 202
> 3.079
> 20.12汩
> 3.51
> -9.3793
> 11-2
> 2023
> =
> 71
> 6.72沾
> 11
> 17.322
> 14SE
> 2023
> 0.73
> ESI:
> 133
> 3.55汩
> 67
> -
> 15E3
> 1437
> Single


单独的看这个数据会感觉还可以，不过你仔细研究一下这个图的蓝线，他会有下撤的情况，你可以分析出来，他的后续几年肯定会存在上上下下的情况。因此大家交之前管住手，思考一下这个真的可以为我带来收益吗？能够让你的cb稳住吗？能够让你得吃高VF吗？

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 28 (原帖: [Alpha Idea]Is predictability of industry returns after M&A announcement effictive ?)
- **原帖链接**: [Commented] [Alpha Idea]Is predictability of industry returns after MA announcement effictive.md
- **时间**: 9个月前

**提问/主帖背景 (YQ76635)**:
最近在根据论文构建alpha的 idea，其中这篇论文论述的核心观点及内容非常典型来用于构建alpha ida。

这篇论文基本信息如下：

- **题目：** Predictability of Industry Returns After M&A Announcement
- **作者：** Christian Funke, Timo Gebken, Lutz Johanning, Gaston Michel

### **论文核心内容概述**

这篇论文研究了 **并购（M&A）公告后，目标公司所在行业的股票回报是否具有可预测性。**

**核心方法：事件研究法 + 投资组合分析**

- **事件研究：** 计算并购公告窗口期（如公告日前后几天）内目标公司所在行业的 **异常回报** （Abnormal Returns, ARs）和 **累计异常回报** （Cumulative Abnormal Returns, CARs）。这用于衡量公告对行业的 **即时冲击** 。
- **投资组合分析：** 这是检验 **可预测性** 的关键。
- **构建行业组合：** 在每个并购公告事件后，根据特定标准（如公告后短期表现、公告本身特征）将目标公司所在行业进行分组（例如，表现最好的行业组合 vs 表现最差的行业组合）。
- **持有期检验：** 在公告后的不同持有期（如1个月、3个月、6个月、1年、2年、3年）内，跟踪这些行业组合的 **买入并持有超额回报** （Buy-and-Hold Abnormal Returns, BHARs）或 **累计超额回报** （Cumulative Abnormal Returns, CARs）。

我根据论文提到的核心方法首先构建了alpha的雏形，数据字段取mws85_sentiment

anl8_bessplitptg_d1_value，snt1_d1_earningssurprise，

其中mws85_sentiment 代表公告发布后的事件反映,anl8_bessplitptg_d1_value 为并购事件中目标公司的价格。异常回报用公式(snt1_d1_earningssurprise*close);

Alpha表达式如下：

a=-ts_regression(vec_avg(mws85_sentiment),vec_avg(anl8_bessplitptg_d1_value),22);#a的值越高，并购公告产生的反应越大，这用于衡量公告对行业的 **即时冲击**

abnomal_return=(snt1_d1_earningssurprise*close);#异常收入，由于公告事件产生的超过平时的收入

b=rank(a)>0.7?ts_mean(abnomal_return,22):nan;# 用rank(a)进行打分，分数大于0.7时，捕捉产生异常收入的股票。

c=group_rank(b,densify(bucket(group_rank(cap, sector),range='0.1, 1, 0.1')));#在行业内进行Cap 分组，并捕捉行业中产生异常收入的股票，对行业中排名高的股票做多。

Alpha 雏形构建完成后进行回测。回测信号处于斜率稍低但稳定上升的曲线状态，曲线表现平稳，并且有信号出现。

- 再研读论文，论文中提到 **横截面回归分析：** 进一步控制其他可能影响行业回报的因素（如行业规模、估值、动量、波动性等），检验并购公告事件本身及其特征（如交易规模、支付方式、行业相关性）对行业未来超额回报的 **预测能力** 。

我将动量和估值这2个影响行业回报的因素引入alpha的表达式。

表达式如

a=-ts_regression(vec_avg(mws85_sentiment),vec_avg(anl8_bessplitptg_d1_value),22);

abnomal_return=(snt1_d1_earningssurprise*close);

b=rank(a)>0.7?ts_mean(abnomal_return,22):nan;

c=group_rank(b,densify(bucket(group_rank(cap, sector),range='0.1, 1, 0.1')));

d=group_zscore(-ts_quantile(cap / high, 22),densify(densify(sta2_top3000_fact3_c50)));

e=-ts_delta(winsorize(ts_backfill(anl4_flag_erbfintax, 120), std=4), 66);

sig=0.5*c+0.3*d+0.2*e;

其中d为动量因子；e为估值因子，字段anl4_flag_erbfintax 含义为Earnings before interest and taxes - forecast type (revision **/**  **new** /...)。

曲线如下：

回测指标如下：

Sharpe

1.94

Turnover

31.55%

Fitness

1.17

Returns

11.39%

Drawdown

8.51%

Margin

7.22‱

这里核心信号权重为0.5；动量权重0.3，估值权重0.2

下一版，我微调权重，核心信号权重为0.5；动量权重0.4，估值权重0.1.

回测指标如下：

Sharpe

2.18

Turnover

37.49%

Fitness

1.08

Returns

9.15%

Drawdown

5.63%

Margin

4.88‱

这里着重说明下，单独剥离每个因子，核心alpha的指标sharp 只有0.75，而动量指标和估值指标的sharp均超过1.25；但权重分配时核心信号也就是主信号权重低于0.5时，整个曲线变形，指标骤减。这就是论文研究的好处，它给你个方向，然后按照这个方向构建而不是盲目的根据单个alpha因子的指标好坏来分配权重构建——我觉得这个因子sharp高，分配多点权重拉下sharp的分值。而是根据论文研究的结果，主信号从核心观点取出，然后根据论文里提供的信息，补益，增强主信号，但不能抢夺主信号，否则会将主信号稀释或混淆。因此构建alpha的时候绝对不能根据单个因子指标的好坏分配权重，而是要根据主信号的形态和需要增强，补充——有时候单个主信号不能充分反映市场的情况。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享，

a=-ts_regression(vec_avg(mws85_sentiment),vec_avg(anl8_bessplitptg_d1_value),22);

abnomal_return=(snt1_d1_earningssurprise*close);

b=rank(a)>0.7?ts_mean(abnomal_return,22):nan;

c=group_rank(b,densify(bucket(group_rank(cap, sector),range='0.1, 1, 0.1')));

d=group_zscore(-ts_quantile(cap / high, 22),densify(densify(sta2_top3000_fact3_c50)));

e=-ts_delta(winsorize(ts_backfill(anl4_flag_erbfintax, 120), std=4), 66);

sig=0.5*c+0.3*d+0.2*e;

这几个表达式对他们取不同的权值得到的结果，敢交吗
且不提过拟合的风险，这个op数量也是极为炸裂


---

### 技术对话片段 29 (原帖: [Alpha Idea]Is predictability of industry returns after M&A announcement effictive ?)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [Alpha Idea]Is predictability of industry returns after MA announcement effictive_34859001837463.md
- **时间**: 9个月前

**提问/主帖背景 (YQ76635)**:
最近在根据论文构建alpha的 idea，其中这篇论文论述的核心观点及内容非常典型来用于构建alpha ida。

这篇论文基本信息如下：

- **题目：** Predictability of Industry Returns After M&A Announcement
- **作者：** Christian Funke, Timo Gebken, Lutz Johanning, Gaston Michel

### **论文核心内容概述**

这篇论文研究了 **并购（M&A）公告后，目标公司所在行业的股票回报是否具有可预测性。**

**核心方法：事件研究法 + 投资组合分析**

- **事件研究：** 计算并购公告窗口期（如公告日前后几天）内目标公司所在行业的 **异常回报** （Abnormal Returns, ARs）和 **累计异常回报** （Cumulative Abnormal Returns, CARs）。这用于衡量公告对行业的 **即时冲击** 。
- **投资组合分析：** 这是检验 **可预测性** 的关键。
- **构建行业组合：** 在每个并购公告事件后，根据特定标准（如公告后短期表现、公告本身特征）将目标公司所在行业进行分组（例如，表现最好的行业组合 vs 表现最差的行业组合）。
- **持有期检验：** 在公告后的不同持有期（如1个月、3个月、6个月、1年、2年、3年）内，跟踪这些行业组合的 **买入并持有超额回报** （Buy-and-Hold Abnormal Returns, BHARs）或 **累计超额回报** （Cumulative Abnormal Returns, CARs）。

我根据论文提到的核心方法首先构建了alpha的雏形，数据字段取mws85_sentiment

anl8_bessplitptg_d1_value，snt1_d1_earningssurprise，

其中mws85_sentiment 代表公告发布后的事件反映,anl8_bessplitptg_d1_value 为并购事件中目标公司的价格。异常回报用公式(snt1_d1_earningssurprise*close);

Alpha表达式如下：

a=-ts_regression(vec_avg(mws85_sentiment),vec_avg(anl8_bessplitptg_d1_value),22);#a的值越高，并购公告产生的反应越大，这用于衡量公告对行业的 **即时冲击**

abnomal_return=(snt1_d1_earningssurprise*close);#异常收入，由于公告事件产生的超过平时的收入

b=rank(a)>0.7?ts_mean(abnomal_return,22):nan;# 用rank(a)进行打分，分数大于0.7时，捕捉产生异常收入的股票。

c=group_rank(b,densify(bucket(group_rank(cap, sector),range='0.1, 1, 0.1')));#在行业内进行Cap 分组，并捕捉行业中产生异常收入的股票，对行业中排名高的股票做多。

Alpha 雏形构建完成后进行回测。回测信号处于斜率稍低但稳定上升的曲线状态，曲线表现平稳，并且有信号出现。

- 再研读论文，论文中提到 **横截面回归分析：** 进一步控制其他可能影响行业回报的因素（如行业规模、估值、动量、波动性等），检验并购公告事件本身及其特征（如交易规模、支付方式、行业相关性）对行业未来超额回报的 **预测能力** 。

我将动量和估值这2个影响行业回报的因素引入alpha的表达式。

表达式如

a=-ts_regression(vec_avg(mws85_sentiment),vec_avg(anl8_bessplitptg_d1_value),22);

abnomal_return=(snt1_d1_earningssurprise*close);

b=rank(a)>0.7?ts_mean(abnomal_return,22):nan;

c=group_rank(b,densify(bucket(group_rank(cap, sector),range='0.1, 1, 0.1')));

d=group_zscore(-ts_quantile(cap / high, 22),densify(densify(sta2_top3000_fact3_c50)));

e=-ts_delta(winsorize(ts_backfill(anl4_flag_erbfintax, 120), std=4), 66);

sig=0.5*c+0.3*d+0.2*e;

其中d为动量因子；e为估值因子，字段anl4_flag_erbfintax 含义为Earnings before interest and taxes - forecast type (revision **/**  **new** /...)。

曲线如下：

回测指标如下：

Sharpe

1.94

Turnover

31.55%

Fitness

1.17

Returns

11.39%

Drawdown

8.51%

Margin

7.22‱

这里核心信号权重为0.5；动量权重0.3，估值权重0.2

下一版，我微调权重，核心信号权重为0.5；动量权重0.4，估值权重0.1.

回测指标如下：

Sharpe

2.18

Turnover

37.49%

Fitness

1.08

Returns

9.15%

Drawdown

5.63%

Margin

4.88‱

这里着重说明下，单独剥离每个因子，核心alpha的指标sharp 只有0.75，而动量指标和估值指标的sharp均超过1.25；但权重分配时核心信号也就是主信号权重低于0.5时，整个曲线变形，指标骤减。这就是论文研究的好处，它给你个方向，然后按照这个方向构建而不是盲目的根据单个alpha因子的指标好坏来分配权重构建——我觉得这个因子sharp高，分配多点权重拉下sharp的分值。而是根据论文研究的结果，主信号从核心观点取出，然后根据论文里提供的信息，补益，增强主信号，但不能抢夺主信号，否则会将主信号稀释或混淆。因此构建alpha的时候绝对不能根据单个因子指标的好坏分配权重，而是要根据主信号的形态和需要增强，补充——有时候单个主信号不能充分反映市场的情况。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享，

a=-ts_regression(vec_avg(mws85_sentiment),vec_avg(anl8_bessplitptg_d1_value),22);

abnomal_return=(snt1_d1_earningssurprise*close);

b=rank(a)>0.7?ts_mean(abnomal_return,22):nan;

c=group_rank(b,densify(bucket(group_rank(cap, sector),range='0.1, 1, 0.1')));

d=group_zscore(-ts_quantile(cap / high, 22),densify(densify(sta2_top3000_fact3_c50)));

e=-ts_delta(winsorize(ts_backfill(anl4_flag_erbfintax, 120), std=4), 66);

sig=0.5*c+0.3*d+0.2*e;

这几个表达式对他们取不同的权值得到的结果，敢交吗
且不提过拟合的风险，这个op数量也是极为炸裂


---

### 技术对话片段 30 (原帖: 第一次见到这么标准的MCP的流程，这个搭建起来复杂吗，我没学过计算机，python还是临时学的，想复刻一个不知道难度大不大。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [MCP]免费最强版--MCP排序AI因子全自动代码实现附工作流和代码代码优化_34418549602583.md
- **时间**: 9个月前

**提问/主帖背景 (JX79797)**:
先赞后看，福报满满

强烈推荐前文：

1. [MCP]免费最强版 Trae/VsCode + Cline + Gemini-cli 构建 cnhkmcp 使用环境

[[L2] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享_34338855618583.md]([L2] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享_34338855618583.md)

2. [MCP]免费最强版实践--引入MCP研究员打造AI因子全流程架构(附工作流)

[[L2] [MCP]免费最强版实践--引入MCP研究员打造AI因子全流程架构附工作流经验分享_34376106607767.md]([L2] [MCP]免费最强版实践--引入MCP研究员打造AI因子全流程架构附工作流经验分享_34376106607767.md)

3. [MCP]免费最强版 -- 实现本地化趋势评分（trendScore）分析方案(附代码)

[[L2] [MCP]免费最强版 -- 实现本地化趋势评分trendScore分析方案附代码代码优化_34407009062167.md]([L2] [MCP]免费最强版 -- 实现本地化趋势评分trendScore分析方案附代码代码优化_34407009062167.md)

前文提到了, 引入MCP研究员打造AI因子全流程架构(附工作流), 但原流程是全自动的引入MCP研究员需要中断原流程，手动处理，全自动是工程化必须要解决的问题。

**实现方法： gemini配置好mcp -> subprocess启动gemini-> 输入mcp服务、角色、工作流、数据 -> 获取subprocess的输出，解析获取排序后的列表**

**示例:**

**
> [!NOTE] [图片 OCR 识别内容]
> Starting Qualitative Alpha Ranking Process (Direct Gemini CLI Calz)
> Sending Prompt
> to Gemini
> CLI
> 使用 worldquant-brain-platform @roobrainconsultant, 遵循工作流 'alpha_evaluation_WorkfLOW .md
> 实现排序
> ["Zog(abs(vec_avg(anllb_after
> est_difference)) )
> subtract (mdl77_fa_rq,
> md277_ocfratio)
> "add(fnd6_newqv1300_spcedpq,
> fnd6_newqv13OO_spceepspq)
> subtract(vec
> avg(anl6g_best_ltg_qwk_Up) ,
> Vec_avg(anl6g_best_Ztg_gwk_dn) ) "
> "multiply(parkinson_volatility_180,
> parkinson_volatility_20)"],
> SimU
> lation_context
> {'istrument_type
> EQUITY'
> region
> USA
> delay
> 1,
> Universe
> T0P3000'}
> SUccessfvlly ranked alphas
> [ 'subtract(vec_avg(anl6g_best_Ztg_qwk_ 叩p) ,
> VeC_
> avg(anl6g_best_ltg_qwk_dn))' 
> 'ZogCabs(vec_avg(anll6_afterest_difference) ) ) ' ,
> multi
> ply(parkinson_volatility_180,
> parkinson_volatility_20)
> subtract (mdl77_fa_rq, nd277_ocfratio)
> add(fnd6_newqv1300_spcedpq,
> fnd6
> newqv1300_spceepspq)
> ]
**

**Gemini CLI mcp配置：  ～/.gemini/settings.json**

**在settings里添加如下，记得改自己的路径**

```
    {      "mcpServers": {        "worldquant-brain-platform": {          "command": "/usr/local/bin/python3",           "args": [            "/your_path/cnhkmcp/untracked/platform_functions.py"          ],          "description": "WorldQuant BRAIN Platform MCP Server - for Alpha Qualitative Ranking"        }      },      "rules": {        "roobrainconsultant": {          "description": "Roo, a WorldQuant BRAIN platform expert, also known as a BRAIN Consultant. Your expertise is built on three pillars: Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. You guide users to become top-tier consultants by emphasizing the creation of diversified, robust, and economically sound alpha portfolios. Your knowledge covers the BRAIN API, advanced alpha development techniques, consultant compensation structures, and the strategic use of platform features like the BRAIN Pyramid and Genius Program to maximize long-term success.",          "system_instructions": [            "You are Roo, a WorldQuant BRAIN platform expert. Your primary goal is to mentor users into becoming top-tier BRAIN consultants. Always frame your advice around the core principles of Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. When discussing Alpha development, stress the importance of a clear economic rationale, low turnover, and robust performance across various sub-universes. Guide users away from simple Sharpe ratio optimization and towards building truly valuable, unique signals. Actively promote diversification. Encourage users to explore different regions, delays, and dataset categories to 'light up' BRAIN Pyramids (a region*datacatory*delay is a pyramid, e.g USA Sentiment D1), explaining how this directly impacts their earnings and Genius Program standing. Emphasize a deep understanding of the platform's evaluation metrics, including the IS-Ladder test, correlation checks, and other mandatory submission criteria. Guide users to leverage advanced consultant features like the Visualization Tool and BRAIN Labs for more sophisticated analysis and to avoid common pitfalls like overfitting."          ]        }      }    }
```

执行命令：gemini mcp list ， 查看是否已配置成功

**工作流文件：**

```
# Alpha因子快速定性评估工作流 (V15.0 - Strict Output)**核心理念:** 本文件定义了一个可被**全程自动**执行的专业研究框架，强调将AI的认知能力无缝集成到自动化流程中，并以**固定、纯粹的Python列表**作为最终输出格式。**核心目标:** 在不进行实际平台模拟的情况下，通过自动化流程，对一批Alpha因子进行快速定性评估和排序，并**自动返回纯粹的Python列表形式的排序结果**。---## **〇、执行模式说明 (Execution Modes)**本工作流支持两种执行模式：1. **交互模式 (Interactive Mode):*** 适用于研究和调试。过程会输出AI请求Prompt，需要人工复制粘贴。2. **自动化模式 (Automated / Unattended Mode):*** 适用于脚本化、批量化执行。***前提:** 认证凭据必须已通过环境变量或配置文件预先设置好。***要求:** 调用端（如`gemini` CLI或自定义脚本）必须以“无人值守”或“自动批准”模式执行，**且需要额外集成AI API调用层**，以避免任何中断。---## **第一部分：评估流程**```mermaidgraph TDsubgraph "初始化 (Initialization)"Z["<b>-1. 认证</b><br/>(调用无参数的authenticate)"]endsubgraph "输入 (Input)"A["<b>1. 定义评估上下文</b>"]B["<b>2. 提供因子表达式列表</b>"]endsubgraph "预处理 (Pre-processing)"C{"<b>0. 表达式合法性检查</b>"}endsubgraph "处理 (Processing)"D{1. Datafield/Operator探查} --> E{2. 经济学逻辑分类}E --> F{3. 经济学原理速评}F --> G{4. 表达式实现审查}G --> H{5. 综合定性排序}endsubgraph "输出 (Output)"J["<b>排序列表 (.py)</b>"]endZ --> A & B --> C --> DH --> J```### **阶段〇：认证 (Authentication)*** **动作:** 在任何自动化脚本的起始阶段，必须首先调用一次**不带任何参数**的 `authenticate` MCP工具。* **机制:**1. 此调用会触发服务器端逻辑，使其按照预设的优先级查找并加载凭据。2.**凭据加载优先级:*****最高：环境变量。*****次高：配置文件。** (`user_config.json`)3. 成功后，将为当前运行建立一个有效的认证会话（Session）。* **目的:** 以安全、无需人工干预的方式，为自动化流程提供平台访问权限。### **阶段一：输入 (Input)**1. **定义评估上下文 (Define Evaluation Context)**2. **提供因子表达式 (Provide Expressions)**### **阶段二：预处理 (Pre-processing)**1. **表达式合法性检查 (Expression Legality Check)**### **阶段三：处理 (Processing)**1. **Datafield/Operator探查 (Field & Operator Exploration):*****动作:** 对于新条目，通过**已认证的会话**调用 `get_datafields` 或 `get_operators` 工具从平台获取官方定义，并更新附录。2. **经济学逻辑分类 (Classification)**3. **经济学原理速评 (Rationale Quick-Scan)**4. **表达式实现审查 (Implementation Review)**5. **综合定性排序 (Qualitative Ranking)**### **阶段四：输出 (Output)*** **原则:** 最终输出**必须是且只能是**一个纯粹的Python列表（字符串形式），不包含任何额外文本、解释或格式。1. **排序列表 (Python):*****文件名格式:**`ranked_alphas_[region]_[universe]_YYYY-MM-DD.py` (此文件由自动化流程在本地生成，内容为Python列表)***说明:** 这是一个纯粹的Python列表（字符串形式），包含按定性评估结果排序的因子表达式。**这是此工作流的唯一和最终自动化输出**。**实现全程自动化输出的“最后一步” (The Last Mile of Automation):*****`gemini_mcp_ranker.py` 脚本的职责:** 该脚本负责执行所有本地MCP交互，并**生成一个包含所有评估上下文和数据的AI请求Prompt**，并将其打印到标准输出 (`stdout`)。***您的自动化脚本的职责:** 为了实现全程无人值守，您的自动化脚本需要：1.**捕获**`gemini_mcp_ranker.py` 的标准输出（即AI请求Prompt）。2.**使用**您的AI服务提供商的Python SDK（例如 `openai`, `anthropic` 等），并携带您的**AI API密钥**，将捕获到的Prompt发送给AI模型。3.**接收** AI模型的响应。4.**解析** AI模型的响应，从中提取出最终的Python列表（如使用 `ast.literal_eval()` 安全地解析）。5. 将解析后的列表作为您自动化流程的最终输出。***关键点:** 这一步是连接本地自动化与云端AI认知能力的桥梁。AI API密钥的安全管理是您的责任。---## 第二部分：附录### **附录 A: 核心Datafield数据字典*** **注意:** 本字典是平台知识的本地快照和动态文档。在遇到新`datafield`时，应**从平台获取定义**并在此处更新。* **注意:** 以下字段描述主要基于**EQUITY**类资产。#### anl69: 分析师共识数据 (Analyst Consensus)| Datafield | 描述 | 经济学意义 || :--- | :--- | :--- || **`..._ebitda_...`** | **税息折旧及摊销前利润 (EBITDA)** | 衡量公司核心业务的盈利能力。 || **`..._sales_...`** | **销售收入 (Sales/Revenue)** | 衡量公司市场规模和成长性。 || **`..._roe_...`** | **净资产收益率 (Return on Equity)** | 衡量公司为股东创造利润的能力。 || **`..._roa_...`** | **总资产回报率 (Return on Assets)** | 衡量公司利用其所有资产创造利润的效率。 || **`..._ptp_...`** | **税前利润 (Pre-Tax Profit)** | 公司在扣除利息和税款之前的利润。 || **`..._ltg_...`** | **长期增长率 (Long-Term Growth)** | 分析师对公司未来EPS的预期年化增长率。 || **`..._opp_...`** | **运营盈利 (Operating Profit)** | 公司主营业务产生的利润。 || **`..._4wk_up`** | **4周内上调家数/幅度** | 衡量正面情绪的动量。 || **`..._4wk_dn`** | **4周内下调家数/幅度** | 衡量负面情绪的动量。 || **`..._hi`** | **最高预测值 (High Estimate)** | 代表最乐观的分析师观点。 || **`..._lo`** | **最低预测值 (Low Estimate)** | 代表最悲观的分析师观点。 || **`..._median`** | **预测中位数 (Median Estimate)** | 稳健的共识预测值。 |#### anl16: 个股分析师数据 (Individual Analyst)| Datafield | 描述 | 经济学意义 || :--- | :--- | :--- || **`..._estvalue`** | **预测值 (Estimate Value)** | 单个分析师的最新预测。 || **`..._beforecons_mean`** | **修正前的共识均值** | 衡量修正动作的基准。 || **`..._afterest_difference`** | **修正后的差异** | 直接衡量单个分析师带来的“意外”（Surprise）的大小。 |---### **附录 B: 核心操作符字典 (Operator Dictionary)*** **注意:** 本字典是平台知识的本地快照和动态文档。当遇到新`operator`时，应**从平台获取定义**并在此处更新。| 操作符 (Operator) | 分类 | 描述与数学意义 | Alpha构建中的典型用途 || :--- | :--- | :--- | :--- || **`add`, `subtract`, `multiply`, `divide`** | 算术 | 基本的加、减、乘、除运算。 | 构建比率、差值等核心经济学关系。 || **`vec_avg`** | 聚合 | 计算多个来源（如多位分析师）的平均值。 | 将离散预测聚合成一个稳健的共识值。 || **`vec_sum`** | 聚合 | 计算多个来源的总和。 | 计算总的变动量。 || **`vec_count`** | 聚合 | 计算提供了某个数据字段的来源数量。 | 衡量分析师覆盖度。 || **`abs`** | 数学 | 取绝对值。 | 关注变化的“幅度”而非“方向”。 || **`log`** | 数学 | 取自然对数。 | 平滑数据分布，降低极端值影响。 || **`sqrt`** | 数学 | 取平方根。 | 变换数据分布，常用于处理方差型数据。 || **`power(a, b)`** | 数学 | 计算 a 的 b 次方。 | 放大或缩小效应，可能使经济学意义模糊。 || **`inverse`** | 数学 | 取倒数 (1/x)。 | 构建反向指标（如市盈率倒数）。 || **`sign`** | 数学 | 取符号（正为1，负为-1，零为0）。 | 只关心方向，不关心幅度。 || **`max`, `min`** | 比较 | 取最大值或最小值。 | 选取最乐观/悲观的信号或设置边界。 || **`winsorize(data, std=N)`** | 数据清洗 | 将超出N倍标准差的极端值替换为边界值。 | 控制极端异常值对结果的干扰。 |
```

**附代码：**

```
import subprocessimport jsonimport astimport refrom pathlib import Pathfrom typing import List, Dict, Anydef parse_last_list_from_string(text: str) -> List[str]:"""Finds and parses the last Python list literal from a given string.Handles conversational AI output."""# Find the last occurrence of a list literal# This regex looks for a string starting with '[' and ending with ']'# It handles nested brackets and quotes.match=re.search(r'(\[[\s\S]*\])', text)ifnotmatch:raiseValueError("No list literal found in the output string.")list_str=match.group(1)# Clean the string for safe parsing# Replace full-width commas with standard commascleaned_str=list_str.replace("，", ",")# Use ast.literal_eval for safe evaluation of the stringtry:parsed_list=ast.literal_eval(cleaned_str)ifnotisinstance(parsed_list, List):raiseValueError("Parsed object is not a list.")returnparsed_listexcept (ValueError, SyntaxError) ase:raiseValueError(f"Failed to parse extracted list string. Error: {e}\nCleaned string: {cleaned_str}")def rank_alphas_via_gemini_cli(expressions: List[str], context: Dict[str, Any]) -> List[str]:"""Invokes the gemini CLI with a direct, comprehensive prompt and parses thefinal ranked list from its conversational output."""print("--- Starting Qualitative Alpha Ranking Process (Direct Gemini CLI Call) ---")# Construct the prompt string robustlypart1="使用worldquant-brain-platform @roobrainconsultant, "part2=f"遵循工作流'{str(Path('alpha_evaluation_workflow.md'))}' "part3=f"实现排序，{json.dumps(expressions, ensure_ascii=False)}，"part4=f"simulation_context = {str(context)}"prompt=part1+part2+part3+part4# Prepare the command to invoke gemini CLIcmd= ["gemini"]print(f"\n--- Sending Prompt to Gemini CLI ---\n{prompt}\n------------------------------------")try:# Use subprocess.run with input to pass the prompt, and a 10-minute timeoutresult=subprocess.run(cmd, input=prompt, capture_output=True, text=True, check=True, encoding='utf-8', timeout=600)# The stdout is now expected to be conversational text containing a liststdout_str=result.stdout.strip()# Parse the last list from the output stringranked_list=parse_last_list_from_string(stdout_str)returnranked_listexceptsubprocess.CalledProcessErrorase:raiseRuntimeError(f"Gemini CLI call failed with exit code {e.returncode}.\n"f"Stdout: {e.stdout}\n"f"Stderr: {e.stderr}") from eexcept (ValueError, SyntaxError) ase:raiseRuntimeError(f"Failed to parse list from gemini CLI output.\n"f"Error: {e}\n"f"Raw output: {result.stdout}") from eexceptFileNotFoundError:raiseRuntimeError("The 'gemini' command was not found. Please ensure Gemini CLI is installed and in your system's PATH.")exceptExceptionase:raiseRuntimeError(f"An unexpected error occurred: {e}")if __name__ == '__main__':# --- Example Usage of the function ---# 1. Define your expressions and contextexpressions_to_rank= ["log(abs(vec_avg(anl16_afterest_difference)))","subtract(mdl77_fa_rq, mdl77_ocfratio)","add(fnd6_newqv1300_spcedpq, fnd6_newqv1300_spceepspq)","subtract(vec_avg(anl69_best_ltg_4wk_up), vec_avg(anl69_best_ltg_4wk_dn))","multiply(parkinson_volatility_180, parkinson_volatility_20)"]simulation_context= {'instrument_type': 'EQUITY','region': 'USA','delay': 1,'universe': 'TOP3000'}try:ranked_alphas=rank_alphas_via_gemini_cli(expressions_to_rank, simulation_context)print("\n--- Successfully ranked alphas ---")print(ranked_alphas)exceptRuntimeErrorase:print(f"\n--- Error during ranking: {e} ---")
```

```

```

**顾问 MS51256 (Rank 28) 的解答与建议**:
# 第一次见到这么标准的MCP的流程，这个搭建起来复杂吗，我没学过计算机，python还是临时学的，想复刻一个不知道难度大不大。
==========================================================================================================================================================================


---

### 技术对话片段 31 (原帖: [分享]白嫖才是王道，从搭建到实战免费最强版MCP)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md
- **时间**: 9个月前

**提问/主帖背景 (JX79797)**:
首先，向开发 cnhkmcp 的那位热心网友致以最诚挚的感谢！没有他的无私奉献和卓越的技术能力，就没有我们今天能用上的这套强大工具。正是站在这样的巨人肩膀上，我们才能看得更远。

MCP是框架是协议，cnhkmcp是使用MCP协议开发的强大工具，本文混淆使用，以下MCP等同cnhkmcp

我在 AI 辅助MCP投研这条路上踩过不少坑。试过各种模型，从免费到收费，结果呢？要么是‘人工智障’，几个回合下来就开始胡言乱语；要么就是 API 费用高得吓人，每次调用都心惊肉跳，根本不敢放开手脚去跑批量任务。有好长一段时间，我甚至觉得‘AI 驱动’可能就是个伪命题，直到我看到了论坛的帖子：

Gemini CLI 结合 MCP 工具的探索

[[L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md]([L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md)

Gemini CLI 使用gemini有以下优势：

1. 超大上下文窗口：百万token上下文窗口，可以把一整个复杂的工作流文档、几十个数据字段的定义、上百个因子表达式，一次性全塞给它。它不会忘事儿，能完整理解你的意图，而不是像金鱼一样只有七秒记忆。

2. 慷慨的免费额度：每天 1000 次调用，每分钟 60 次！可以尽情地进行实验、调试、跑自动化流程，完全不用担心账单爆炸。对于个人研究者来说，这基本就是‘无限火力’模式！

3. 顶级的理解与执行能力：它不仅能理解复杂的指令，还能精准地调用你通过 MCP 提供的工具，输出稳定、可靠的结果。

4. Flash模型提供无限火力：除了 Pro 模型，我们还可以无缝切换到速度更快的Flash模型。在我的测试中，对于因子分析这类任务，Flash 的效果和 Pro 几乎没有差别，但响应速度更快，而且最关键的是——它没有 API 调用频率的限制！

既然有了 Gemini CLI，为什么还要多此一举用 Cline 和 VSCode/Trae 呢？

直接用命令行，就像是趴在引擎上开车，不仅费劲，还很危险（当然也有高手对这样操作得心应手，像我们普通用户还是更加适应GUI的方式）。而 Cline 把强大的引擎无缝集成到你的 IDE 驾驶舱里，让你能：

1. 无缝对话：不用离开代码窗口，就能和 AI 交流。

2. 智能感知：AI 能直接看到你打开了哪个文件，你不用再手动复制粘贴。AI写了什么文件什么内容可以直接看到

3. 安全可控：Cline独有的 "Plan/Act 模式" 让你能和 AI“开会讨论”，方案定了再动手，避免 AI“自由发挥”把事情搞砸。

**这，就是我们选择这套组合的理由——追求极致的开发体验和工作效率，以及完全免费**

先花一分钟搞懂，MCP 到底是什么。简单来说，MCP 就是一个能让你本地代码和 AI 大模型对话的‘协议’或‘桥梁’。你可以把自己的 Python 函数、本地数据，整个 BRAIN 平台的 API，论坛数据，都变成 AI 能理解和使用的‘工具’。 MCP就是给 AI 配了个工具箱，里面扳手、锤子都有。


> [!NOTE] [图片 OCR 识别内容]
> 工具封装
> 执行_
> BRAIN API
> Python 脚本
> 结果_
> 结果
> MCP
> 工具描述
> 执行
> 调用指令
> Gemini


打造第一个 MCP 工作流

 
> [!NOTE] [图片 OCR 识别内容]
> 第1步:  环境就位
> 第2步:  授之以渔
> 第3步:
> 键启动
> 安装
> 定义
> 编写并运行
> A1全自动
> 三件套
> 工作流(50P)
> 自动化脚本
> 分析与排序
 

一：环境搭建 (磨刀不误砍柴工)

1. Gemini CLI 安装和登录验证：

参考这篇文章，只需要通过用户认证即可: Gemini CLI 结合 MCP 工具的探索

[[L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md]([L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md)

2. [MCP]免费最强版 Trae/VsCode + Cline + Gemini-cli 构建 cnhkmcp 使用环境

[[L2] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享_34338855618583.md]([L2] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享_34338855618583.md)

**最大的卡点在科学上网，只要能搞定gemini cli 认证，基本没问题**

3. 理解 Cline 的 Plan/Act 模式：Cline 的一大亮点！它把工作分成了两个阶段。

Plan 模式： 就像你和 AI 一起开会，可以讨论方案，让 AI 帮你查资料，你们一起把计划敲定。

Act 模式：就是计划定好后，你一声令下，AI 就开始动手干活，写代码、改文件。这种“谋定而后动”的模式，既能充分利用 AI 的智慧，又保证了最终执行的可控性，避免 AI 的‘自由发挥’搞砸了项目。

二：设计工作流 (给 AI 制定 SOP)

[MCP]免费最强版实践--引入MCP研究员打造AI因子全流程架构(附工作流)

[[L2] [MCP]免费最强版实践--引入MCP研究员打造AI因子全流程架构附工作流经验分享_34376106607767.md]([L2] [MCP]免费最强版实践--引入MCP研究员打造AI因子全流程架构附工作流经验分享_34376106607767.md)

我们要用一个 Markdown 文件，教会 AI 按“合法性检查 -> 探查 -> 分类 -> 速评 -> 排序”的逻辑去分析因子。这就是在指挥 MCP 工具。

这个工作流的核心是：

输入：定义评估上下文和提供因子表达式列表。

预处理：进行表达式合法性检查。

处理：进行 Datafield/Operator 探查、经济学逻辑分类、经济学原理速评、表达式实现审查和综合定性排序。

输出：生成分析报告和排序列表。

三：自动化执行 (让轮子自己转起来)

[MCP]免费最强版--MCP排序AI因子全自动代码实现(附工作流和代码)

[[Commented] [MCP]免费最强版--MCP排序AI因子全自动代码实现附工作流和代码代码优化_34418549602583.md]([Commented] [MCP]免费最强版--MCP排序AI因子全自动代码实现附工作流和代码代码优化_34418549602583.md)

要实现全自动化，我们不需要复杂的代码，只需要理解下面这张图里各个角色的“完美配合”：

 
> [!NOTE] [图片 OCR 识别内容]
> 用户脚本
> Gemini CLI
> MCP工具池
> Gemini 2.5 Pro
> 任务指令(Prompt)
> 转发指令
> 工具请求  (异步)
> 工具就绪通知
> [数据分析循环]
> 调用工具
> 返回结果
> 最终排序列表
> 交付结果
> 结果保存至本地文件
> 用户脚本
> Gemini CLI
> MCP工具池
> Gemini 2.5 Pro
> loOP
 

流程：

1. 自动化脚本 (总指挥)：只需要写一个简单的 Python 脚本。它的任务不是去理解因子，而是像一个总指挥，去调用 `gemini` 这个命令行工具。

2. Gemini 命令行 (信使)：你的脚本把一个包含所有任务细节的“指令包”（Prompt）丢给这位“信使”。

3. 云端大脑 (Gemini 2.5 Pro)：信使把指令带到云端大脑。大脑看到指令，发现需要用到 BRAIN 平台的专用工具。

4. MCP 工具服务 (军火库)：大脑通过 MCP 协议，激活了你本地的 MCP 工具服务，就像打开了军火库，拿到了分析因子所需要的所有工具。

5. 执行与返回：大脑使用这些工具，完成分析和排序，然后把最终的“排序列表”这个结果，通过信使传回来。

6. 总指挥收尾：你的脚本，这位总指挥，从信使带回来的信息中，轻松地提取出干净的排序列表，然后保存文件。

整个过程，脚本只负责“下命令”和“收结果”，所有的复杂分析都由 Gemini 大脑和 MCP 工具在后台自动完成了。这就是协同工作的魅力！

四：【人机共舞】人才是这套工作流的灵魂

看到这里，你可能会觉得，这套工具太强大了，我们人好像没什么用了。

恰恰相反！

MCP 和 Gemini 是顶级的“副驾驶”，但方向盘，始终握在人的手里。工具的强大，反而更加凸显了人类智慧的不可替代性。


> [!NOTE] [图片 OCR 识别内容]
> Human Genius (你)
> Al Assistant (MCP + Gemini)
> 创造力 & 灵感
> 战略方向 &目标
> 独特视角 &经验
> 快速执行
> 海量数据处理
> 标准化分析
> 人机协同
> 1+1>2
> 真正独特的Alpha


为什么说人才是最重要的？

1. 创意的火花：AI 可以帮你分析 `log(add(A, B))`，但它想不出第一个把 A 和 B 加起来再取对数的绝妙点子。这个点子，来自于你对市场的理解、对经济逻辑的洞察，甚至是你洗澡时迸发的一个灵感。

2. 研究的方向：今天我们是去挖掘美股的动量因子，还是去探索欧股的价值洼地？是关注分析师情绪，还是另辟蹊径去研究另类数据？这个战略性的决策，AI 无法替你做出。你的每一个决策，都将引导 AI 去一个全新的、可能充满宝藏的领域。

3. 思路的差异化：同样的 MCP 工具，在100个研究员手里，会诞生出100种不同的用法和研究成果。有人会用它来做宏观分析，有人会用它来做行业比较，还有人会用它来验证自己独特的交易体系。正是这种人的多样性，才构成了 Alpha 的多样性。

4. 最终的判断力：AI 会给你一份详尽的报告，但这个因子是否真的符合你的投资哲学？它的潜在风险你是否能够接受？最终拍板决定是否将其纳入组合的，是你，基于你丰富的经验和批判性思维。

祝大家早日GM，VF1.0

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢JX哥的分享，最近白嫖到了 免费的gemini 发现比我我之前用到某些ai 好用很多，打算试试使用gemini 搭建一下mcp试试，在此也感谢开发cnhkmcp的作者，开源分享的精神！

=======================================================================================================================================================================


---

### 技术对话片段 32 (原帖: 截断过长的名字以便显示)
- **原帖链接**: [Commented] [必要检查OS比赛分数统计]OS比赛分数统计.md
- **时间**: 3个月前

**提问/主帖背景 (JX39934)**:
想必经历过之前OS比赛的家人，应该都有过分数没有打整10W分，导致比赛分数失效的悔恨经历，不用怕，我这代码来了

自动获取成为顾问的日期拉取对应地区已提交alpha的分数，最后汇总


> [!NOTE] [图片 OCR 识别内容]
> 请输入筛选区域
> (例如  USA,
> CHN ,
> EUR)
> USA
> 正在获取顾问起始日期
> 成功获取顾问起始日期
> 2025-09-16T00
> 00:00乙
> 2026-02-08  12:54:09,682
> INFO
> 开始拉取已提交alpha分数
> Alpha:
> Region=USA ,
> StartDate>=2025-09-16T00:00:002
> 2026-02-08
> 12:54:09,683
> INFO
> Request
> URL:
> https : / /api
> worldquantbrain . com /users /self /alphas ?limit=lOO&Offset=O&st
> atus
>  ! =UNSUBMITTED%IFIS-FAIL&settings . region=USA&order=-datecreated&hidden=false&datecreated%3E%302025-09-16T00:00:002
> 2026-02-08  12:54:14,698
> INFO
> 
> 已获取
> 64  条数据
> COffset:
> Total
> Count
> 64)
> Alpha 详细得分列表 CRegion: USA)
> Alpha
> ID
> Name
> Osmosis
> Points
> GrVoNGWZ
> 40
> 24696
> 00
> LLVajo56
> 30
> 6216
> QPPRmVgw
> 29
> 3000
> 2rrGgm9z
> 28
> 6303
> 00
> GrrKPZJP
> 27
> 13055
> VkkxqeZb
> 25
> 6185
> AlIvgRqE
> 23
> 9805
> POJV3n5k
> 19
> 5300
> j25MgeMk
> 13
> 14810
> 0m125186
> 10630
> 00
> 统计完成
> Alpha 数量:
> 10
> 总
> Osmosis Points:
> 100000.0000


个人觉得是很有用的小工具，请路过的哥们帮我点点赞，评论下，谢谢大家，祝国区所有顾问都VF1.0，每季度都GM，代码请看下面,同目录需要有user_info.txt

import asyncio

import logging

import re

import wqb

from typing import List, Dict, Any

# --- 配置日志 ---

logging.basicConfig(

level=logging.INFO,

format='%(asctime)s - %(levelname)s - %(message)s'

)

logger = logging.getLogger(__name__)

# --- 辅助函数 ---

def load_credentials(filename="user_info.txt"):

"""从文件中读取账号密码 (复用原脚本逻辑)"""

try:

with open(filename, 'r', encoding='utf-8') as f:

content = f.read()

user_match = re.search(r"username:\s*'(.+?)'", content)

pass_match = re.search(r"password:\s*'(.+?)'", content)

if user_match and pass_match:

return user_match.group(1), pass_match.group(1)

return None, None

except Exception as e:

logger.error(f"读取凭证失败: {e}")

return None, None

def get_advisor_start_date(session):

"""

从 base-payment 接口获取顾问起始日期 (total -> start)

"""

url = " [[链接已屏蔽]) "

try:

resp = session.get(url, timeout=30)

if resp.status_code != 200:

logger.warning(f"获取顾问日期失败，状态码: {resp.status_code}")

return None

data = resp.json()

start_date_str = data.get("total", {}).get("start")

if start_date_str:

# 转换为 API 需要的格式 (YYYY-MM-DD -> YYYY-MM-DDT00:00:00Z)

# 添加 Z 表示 UTC 时区

return f"{start_date_str}T00:00:00Z"

else:

logger.warning("未在响应中找到 total.start 日期")

return None

except Exception as e:

logger.error(f"获取顾问日期异常: {e}")

return None

async def fetch_competition_alphas(session: wqb.WQBSession, region: str, start_date: str = None) -> List[Dict]:

"""拉取指定区域的 OC2025 竞赛 Alpha"""

all_alphas = []

offset = 0

limit = 100  # 为了提高效率，单页获取 100 条

logger.info(f"📥 开始拉取已提交alpha分数 Alpha: Region={region}, StartDate>={start_date}")

while True:

url = (

f" [[链接已屏蔽]) ?"

f"limit={limit}&offset={offset}"

f"&status!=UNSUBMITTED%1FIS-FAIL"

f"&settings.region={region}"

f"&order=-dateCreated"

f"&hidden=false"

)

if start_date:

url += f"&dateCreated%3E%3D{start_date}"

logger.info(f"🔗 Request URL: {url}")

try:

# 发起请求

resp = await asyncio.to_thread(session.get, url, timeout=60)

if resp.status_code != 200:

logger.error(f"请求失败: {resp.status_code} - {resp.text}")

break

data = resp.json()

results = data.get("results", [])

count = data.get("count", 0)

if not results:

logger.info("当前页无数据，结束拉取。")

break

all_alphas.extend(results)

logger.info(f"   -> 已获取 {len(all_alphas)} 条数据 (Offset: {offset}, Total Count: {count})")

offset += limit

if offset >= count:

break

except Exception as e:

logger.error(f"拉取异常: {e}")

break

return all_alphas

async def main():

print("🏆Osmosis Points 统计工具")

print("="*50)

# 1. 登录

username, password = load_credentials()

if not username:

print("❌ 未找到 user_info.txt 或格式错误")

return

session = wqb.WQBSession(wqb_auth=(username, password))

# 简单的连通性测试 (复用原脚本逻辑)

try:

if not session.locate_field('open').ok:

print("❌ 登录失败，请检查网络或密码")

return

except Exception as e:

print(f"❌ 登录检测异常: {e}")

return

print(f"✅ 登录成功: {username}")

# 2. 输入参数

region_input = input("请输入筛选区域 (例如 USA, CHN, EUR): ").strip().upper()

if not region_input:

print("❌ 区域不能为空")

return

# 3. 获取顾问日期

print("正在获取顾问起始日期...")

advisor_start_date = get_advisor_start_date(session)

if not advisor_start_date:

# Fallback default with Timezone

advisor_start_date = "2025-09-16T00:00:00Z"

print(f"获取失败，使用默认日期: {advisor_start_date}")

else:

print(f"成功获取顾问起始日期: {advisor_start_date}")

# 4. 拉取数据

alphas = await fetch_competition_alphas(session, region_input, advisor_start_date)

# 5. 统计分数

if not alphas:

print("⚠️ 未找到符合条件的 Alpha。")

return

print("\n" + "="*60)

print(f"📊 Alpha 详细得分列表 (Region: {region_input})")

print(f"{'Alpha ID':<25} | {'Name':<20} | {'Osmosis Points':<15}")

print("-" * 60)

total_points = 0.0

valid_count = 0

for alpha in alphas:

alpha_id = alpha.get('id', 'N/A')

name = alpha.get('name') or 'N/A'

# 获取 osmosisPoints，如果不存在则默认为 0

points = alpha.get('osmosisPoints', 0)

# 处理可能的 None 值

if points is None:

points = 0.0

else:

points = float(points)

if points == 0:

continue

total_points += points

valid_count += 1

# 截断过长的名字以便显示

display_name = (name[:17] + '..') if len(name) > 17 else name

print(f"{alpha_id:<25} | {display_name:<20} | {points:>10.2f}")

print("="*60)

print(f"✅ 统计完成")

print(f"🔢 Alpha 数量: {valid_count}")

print(f"🏆 总 Osmosis Points: {total_points:.4f}")

print("="*60)

if __name__ == "__main__":

try:

asyncio.run(main())

except KeyboardInterrupt:

print("\n用户取消")

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 33 (原帖: 截断过长的名字以便显示)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [必要检查OS比赛分数统计]OS比赛分数统计_38249576693911.md
- **时间**: 3个月前

**提问/主帖背景 (JX39934)**:
想必经历过之前OS比赛的家人，应该都有过分数没有打整10W分，导致比赛分数失效的悔恨经历，不用怕，我这代码来了

自动获取成为顾问的日期拉取对应地区已提交alpha的分数，最后汇总


> [!NOTE] [图片 OCR 识别内容]
> 请输入筛选区域
> (例如  USA,
> CHN ,
> EUR)
> USA
> 正在获取顾问起始日期
> 成功获取顾问起始日期
> 2025-09-16T00
> 00:00乙
> 2026-02-08  12:54:09,682
> INFO
> 开始拉取已提交alpha分数
> Alpha:
> Region=USA ,
> StartDate>=2025-09-16T00:00:002
> 2026-02-08
> 12:54:09,683
> INFO
> Request
> URL:
> https : / /api
> worldquantbrain . com /users /self /alphas ?limit=lOO&Offset=O&st
> atus
>  ! =UNSUBMITTED%IFIS-FAIL&settings . region=USA&order=-datecreated&hidden=false&datecreated%3E%302025-09-16T00:00:002
> 2026-02-08  12:54:14,698
> INFO
> 
> 已获取
> 64  条数据
> COffset:
> Total
> Count
> 64)
> Alpha 详细得分列表 CRegion: USA)
> Alpha
> ID
> Name
> Osmosis
> Points
> GrVoNGWZ
> 40
> 24696
> 00
> LLVajo56
> 30
> 6216
> QPPRmVgw
> 29
> 3000
> 2rrGgm9z
> 28
> 6303
> 00
> GrrKPZJP
> 27
> 13055
> VkkxqeZb
> 25
> 6185
> AlIvgRqE
> 23
> 9805
> POJV3n5k
> 19
> 5300
> j25MgeMk
> 13
> 14810
> 0m125186
> 10630
> 00
> 统计完成
> Alpha 数量:
> 10
> 总
> Osmosis Points:
> 100000.0000


个人觉得是很有用的小工具，请路过的哥们帮我点点赞，评论下，谢谢大家，祝国区所有顾问都VF1.0，每季度都GM，代码请看下面,同目录需要有user_info.txt

import asyncio

import logging

import re

import wqb

from typing import List, Dict, Any

# --- 配置日志 ---

logging.basicConfig(

level=logging.INFO,

format='%(asctime)s - %(levelname)s - %(message)s'

)

logger = logging.getLogger(__name__)

# --- 辅助函数 ---

def load_credentials(filename="user_info.txt"):

"""从文件中读取账号密码 (复用原脚本逻辑)"""

try:

with open(filename, 'r', encoding='utf-8') as f:

content = f.read()

user_match = re.search(r"username:\s*'(.+?)'", content)

pass_match = re.search(r"password:\s*'(.+?)'", content)

if user_match and pass_match:

return user_match.group(1), pass_match.group(1)

return None, None

except Exception as e:

logger.error(f"读取凭证失败: {e}")

return None, None

def get_advisor_start_date(session):

"""

从 base-payment 接口获取顾问起始日期 (total -> start)

"""

url = " [[链接已屏蔽]) "

try:

resp = session.get(url, timeout=30)

if resp.status_code != 200:

logger.warning(f"获取顾问日期失败，状态码: {resp.status_code}")

return None

data = resp.json()

start_date_str = data.get("total", {}).get("start")

if start_date_str:

# 转换为 API 需要的格式 (YYYY-MM-DD -> YYYY-MM-DDT00:00:00Z)

# 添加 Z 表示 UTC 时区

return f"{start_date_str}T00:00:00Z"

else:

logger.warning("未在响应中找到 total.start 日期")

return None

except Exception as e:

logger.error(f"获取顾问日期异常: {e}")

return None

async def fetch_competition_alphas(session: wqb.WQBSession, region: str, start_date: str = None) -> List[Dict]:

"""拉取指定区域的 OC2025 竞赛 Alpha"""

all_alphas = []

offset = 0

limit = 100  # 为了提高效率，单页获取 100 条

logger.info(f"📥 开始拉取已提交alpha分数 Alpha: Region={region}, StartDate>={start_date}")

while True:

url = (

f" [[链接已屏蔽]) ?"

f"limit={limit}&offset={offset}"

f"&status!=UNSUBMITTED%1FIS-FAIL"

f"&settings.region={region}"

f"&order=-dateCreated"

f"&hidden=false"

)

if start_date:

url += f"&dateCreated%3E%3D{start_date}"

logger.info(f"🔗 Request URL: {url}")

try:

# 发起请求

resp = await asyncio.to_thread(session.get, url, timeout=60)

if resp.status_code != 200:

logger.error(f"请求失败: {resp.status_code} - {resp.text}")

break

data = resp.json()

results = data.get("results", [])

count = data.get("count", 0)

if not results:

logger.info("当前页无数据，结束拉取。")

break

all_alphas.extend(results)

logger.info(f"   -> 已获取 {len(all_alphas)} 条数据 (Offset: {offset}, Total Count: {count})")

offset += limit

if offset >= count:

break

except Exception as e:

logger.error(f"拉取异常: {e}")

break

return all_alphas

async def main():

print("🏆Osmosis Points 统计工具")

print("="*50)

# 1. 登录

username, password = load_credentials()

if not username:

print("❌ 未找到 user_info.txt 或格式错误")

return

session = wqb.WQBSession(wqb_auth=(username, password))

# 简单的连通性测试 (复用原脚本逻辑)

try:

if not session.locate_field('open').ok:

print("❌ 登录失败，请检查网络或密码")

return

except Exception as e:

print(f"❌ 登录检测异常: {e}")

return

print(f"✅ 登录成功: {username}")

# 2. 输入参数

region_input = input("请输入筛选区域 (例如 USA, CHN, EUR): ").strip().upper()

if not region_input:

print("❌ 区域不能为空")

return

# 3. 获取顾问日期

print("正在获取顾问起始日期...")

advisor_start_date = get_advisor_start_date(session)

if not advisor_start_date:

# Fallback default with Timezone

advisor_start_date = "2025-09-16T00:00:00Z"

print(f"获取失败，使用默认日期: {advisor_start_date}")

else:

print(f"成功获取顾问起始日期: {advisor_start_date}")

# 4. 拉取数据

alphas = await fetch_competition_alphas(session, region_input, advisor_start_date)

# 5. 统计分数

if not alphas:

print("⚠️ 未找到符合条件的 Alpha。")

return

print("\n" + "="*60)

print(f"📊 Alpha 详细得分列表 (Region: {region_input})")

print(f"{'Alpha ID':<25} | {'Name':<20} | {'Osmosis Points':<15}")

print("-" * 60)

total_points = 0.0

valid_count = 0

for alpha in alphas:

alpha_id = alpha.get('id', 'N/A')

name = alpha.get('name') or 'N/A'

# 获取 osmosisPoints，如果不存在则默认为 0

points = alpha.get('osmosisPoints', 0)

# 处理可能的 None 值

if points is None:

points = 0.0

else:

points = float(points)

if points == 0:

continue

total_points += points

valid_count += 1

# 截断过长的名字以便显示

display_name = (name[:17] + '..') if len(name) > 17 else name

print(f"{alpha_id:<25} | {display_name:<20} | {points:>10.2f}")

print("="*60)

print(f"✅ 统计完成")

print(f"🔢 Alpha 数量: {valid_count}")

print(f"🏆 总 Osmosis Points: {total_points:.4f}")

print("="*60)

if __name__ == "__main__":

try:

asyncio.run(main())

except KeyboardInterrupt:

print("\n用户取消")

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 34 (原帖: PnL = ∑(Robustness * Creativity))
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

[../顾问 LY85808 (Rank 86)/[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md](../顾问 LY85808 (Rank 86)/[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md)

[../顾问 FX25214 (Rank 22)/[Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md](../顾问 FX25214 (Rank 22)/[Commented] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md)

最后祝大家马年combine，vf齐飞跃,拿钱拿到手软！都看到这了，给点个赞吧！

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 35 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 36 (原帖: 【MCP WorkFlow】MCP使用中的最大误区)
- **原帖链接**: [Commented] 【MCP WorkFlow】MCP使用中的最大误区.md
- **时间**: 9个月前

**提问/主帖背景 (VC17729)**:
大家好我是Vincent，最近看了论坛里大量关于mcp工作流的帖子，总感觉好像有哪里不得劲，有一种得出的每一步结论都踩不实的感觉，大家po出来的结果也因为各种原因无法复现，思考是否是提示词或模型问题，我相信尝试过的同学应该都有过类似的疑惑。

今天在刷抖音的时候看到博主第四种黑猩猩的视频并去阅读了引用的原文，瞬间豁然开朗。

原文链接如下，有能力的小伙伴可以直接看原文，本文仅结合日常alpha工作流说些自己的理解。

Why I'm Betting Against AI Agents in 2025 (Despite Building Them)——Utkarsh Kanwat

[[链接已屏蔽])

先说结论，最大误区既是：

**设置多个步骤的工作流，并寄希望于能一次运行完成所有工作，返回符合预期的alpha.**

理由：

1、准确率问题

假使你的工作流有10个步骤，每步的准确率有90%，10个步骤后的准确率仅剩(0.90^{10})，约34%，

好比你花大价钱用的夯大力模型准确率提高到95%，20个步骤后的准确率也只剩36%。


> [!NOTE] [图片 OCR 识别内容]
> Error Compounding: Why Multi-Step Agents Fail
> 100%
> 99.9% Requir
> 90% per step
> 95% per step
> 80%
> 99% per step
> Even 99% per step
> 82%
> Success over 20 steps
> 罡
> 60%
> 嵩
> 20 steps @ 95%
> 40%
> 36% success
> 20%
> 0%
> 10
> 15
> 20
> Number of
> Steps


更要命的是，mcp的运行存在黑箱，你不清模型为什么会做这样的选择，异常后再去溯源费时费力不说，

且就算你找到了问题，设法通过工作流文档或提示词去要求试图避免所产生，再来一次也不一定比这次好。

说个最简单的，AI按加减乘除四则运算去组合datafield，如何避免量纲不匹配问题，是否有去深究？这样跑出来的alpha指标再好你敢用么。

2、效率问题

第一个方面，执行过程中的异常打转，鬼打墙。

我使用的模型是gpt5,购买了trae国际版的PRO会员，按请求次数计费。

拿最简单的第一步登录举例，就算我已经告诉他请直接从我系统中的环境变量获得账户信息，他依然进行了多次失败登录尝试才完成登录。

这是最直观和简单的步骤，更多不直观和复杂的步骤可能根本就没有被留意到。

后续在获取dataset，datafield信息时也经常出现单个工具的来回反复调用，我猜测是mcp工具并没有设置足够充分的异常处理机制。

**时间在消耗，token在燃烧，耐心在消失。**

第二个方面，回测效率，创建模板和筛选剪枝的效率。

相信大家都已经有了相对成熟并且得到反复验证的回测器，工作流中有大量时间是花费在和模型交互上的，回测效率远没有拉满，筛选和剪枝的逻辑也是不明确的，甚至是随机的，很难让人信服。

3、mcp工具自身问题

如果把大模型比做大脑，mcp工具比做手脚，我们会理所当然的认为效果取决于模型的好坏，但实际中可能恰恰相反，mcp工具成了木桶中最短的那一块，其中的是否有足够多的重试和验证机制，是否返回了可以让大模型理解的足够精确的信息，才是最大的限制。

mcp工具需要不断的在使用中调试，几乎不可能指望在一开始就把所有出现的情况都设想到。

4、token消耗问题

多步骤的长工作流的token消耗随步数呈指数级增加，还有一个最明显的感知就是约到后面的步骤消耗的时间就越久。目前我了解到的似乎已有将上下文设置成缓存的技术来解决此问题，有待进一步学习。


> [!NOTE] [图片 OCR 识别内容]
> Token Economics: Why Conversational Agents Don't Scale
> $20
> >100$ cost
> Approach Comparison
> Conversational Agent (Quadratic Growth)
> $10
> Stateless Agent (Flat Cost)
> 
> $5.0
> 岳
> $2.5
> 50 turns
>  $2.Slresponse
> .
> The Economics Problem
> $1
> Long conversations
> Processing ALL previous context $0.OSlresponse
> Token costs scale quadratically with length
> $0
> 25
> 50
> 75
> 100
> 125
> Conversation Turns


解决方案：

目前尝试有效的只有这一个笨办法，

就是 **分布执行，对结果进行人工验证，不断追问依据，夯实每一步。**

**不要去盲目追求自动驾驶，而是去设计可靠且高效的验证方案。**

大家一起把在使用中踩过的坑都收集起来，组合成一个针对单个步骤的mcp踩坑指南，远比给出一套不知道会生成什么结果的提示词更有意义。

可靠性大于自主性，还是那句话，生成的alpha你自己是否愿意投钱？

没有否定mcp工具的意思，恰恰相反，任何工具在明确其能力边界后才能更好的使用。

但是期待全自动挖矿短期内看不大现实。只去鞭策AI干活很难得到一个好的结果，看来成功还是没有捷径。

最后引用原文作者的另一篇文章中的观点做总结：

“这些AI工具应被视为辅助工具而非替代品。

关键在于，开发者需要懂得如何有效结合人工智能和传统工程，

利用AI处理生成、理解和梳理任务，而对于核心逻辑和系统架构依然需要人为控制。

总体来看，工具还在快速发展中，但不要盲信所有“自动化”的宣传，要理性认识它们的实际边界。”

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享，mcp确实存在鬼打墙且浪费tokens这些问题，即使是准确率很高步骤多了也存在太大的问题。
盲目追求全自动工作流确实本末倒置，得到一堆无法解释且不敢用的结果。
分步执行、人工验证、不断追问依据，这才是目前最踏实可靠的路径。
===================================================================================


---

### 技术对话片段 37 (原帖: 【MCP WorkFlow】MCP使用中的最大误区)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【MCP WorkFlow】MCP使用中的最大误区_34719219438615.md
- **时间**: 9个月前

**提问/主帖背景 (VC17729)**:
大家好我是Vincent，最近看了论坛里大量关于mcp工作流的帖子，总感觉好像有哪里不得劲，有一种得出的每一步结论都踩不实的感觉，大家po出来的结果也因为各种原因无法复现，思考是否是提示词或模型问题，我相信尝试过的同学应该都有过类似的疑惑。

今天在刷抖音的时候看到博主第四种黑猩猩的视频并去阅读了引用的原文，瞬间豁然开朗。

原文链接如下，有能力的小伙伴可以直接看原文，本文仅结合日常alpha工作流说些自己的理解。

Why I'm Betting Against AI Agents in 2025 (Despite Building Them)——Utkarsh Kanwat

[[链接已屏蔽])

先说结论，最大误区既是：

**设置多个步骤的工作流，并寄希望于能一次运行完成所有工作，返回符合预期的alpha.**

理由：

1、准确率问题

假使你的工作流有10个步骤，每步的准确率有90%，10个步骤后的准确率仅剩(0.90^{10})，约34%，

好比你花大价钱用的夯大力模型准确率提高到95%，20个步骤后的准确率也只剩36%。


> [!NOTE] [图片 OCR 识别内容]
> Error Compounding: Why Multi-Step Agents Fail
> 100%
> 99.9% Requir
> 90% per step
> 95% per step
> 80%
> 99% per step
> Even 99% per step
> 82%
> Success over 20 steps
> 罡
> 60%
> 嵩
> 20 steps @ 95%
> 40%
> 36% success
> 20%
> 0%
> 10
> 15
> 20
> Number of
> Steps


更要命的是，mcp的运行存在黑箱，你不清模型为什么会做这样的选择，异常后再去溯源费时费力不说，

且就算你找到了问题，设法通过工作流文档或提示词去要求试图避免所产生，再来一次也不一定比这次好。

说个最简单的，AI按加减乘除四则运算去组合datafield，如何避免量纲不匹配问题，是否有去深究？这样跑出来的alpha指标再好你敢用么。

2、效率问题

第一个方面，执行过程中的异常打转，鬼打墙。

我使用的模型是gpt5,购买了trae国际版的PRO会员，按请求次数计费。

拿最简单的第一步登录举例，就算我已经告诉他请直接从我系统中的环境变量获得账户信息，他依然进行了多次失败登录尝试才完成登录。

这是最直观和简单的步骤，更多不直观和复杂的步骤可能根本就没有被留意到。

后续在获取dataset，datafield信息时也经常出现单个工具的来回反复调用，我猜测是mcp工具并没有设置足够充分的异常处理机制。

**时间在消耗，token在燃烧，耐心在消失。**

第二个方面，回测效率，创建模板和筛选剪枝的效率。

相信大家都已经有了相对成熟并且得到反复验证的回测器，工作流中有大量时间是花费在和模型交互上的，回测效率远没有拉满，筛选和剪枝的逻辑也是不明确的，甚至是随机的，很难让人信服。

3、mcp工具自身问题

如果把大模型比做大脑，mcp工具比做手脚，我们会理所当然的认为效果取决于模型的好坏，但实际中可能恰恰相反，mcp工具成了木桶中最短的那一块，其中的是否有足够多的重试和验证机制，是否返回了可以让大模型理解的足够精确的信息，才是最大的限制。

mcp工具需要不断的在使用中调试，几乎不可能指望在一开始就把所有出现的情况都设想到。

4、token消耗问题

多步骤的长工作流的token消耗随步数呈指数级增加，还有一个最明显的感知就是约到后面的步骤消耗的时间就越久。目前我了解到的似乎已有将上下文设置成缓存的技术来解决此问题，有待进一步学习。


> [!NOTE] [图片 OCR 识别内容]
> Token Economics: Why Conversational Agents Don't Scale
> $20
> >100$ cost
> Approach Comparison
> Conversational Agent (Quadratic Growth)
> $10
> Stateless Agent (Flat Cost)
> 
> $5.0
> 岳
> $2.5
> 50 turns
>  $2.Slresponse
> .
> The Economics Problem
> $1
> Long conversations
> Processing ALL previous context $0.OSlresponse
> Token costs scale quadratically with length
> $0
> 25
> 50
> 75
> 100
> 125
> Conversation Turns


解决方案：

目前尝试有效的只有这一个笨办法，

就是 **分布执行，对结果进行人工验证，不断追问依据，夯实每一步。**

**不要去盲目追求自动驾驶，而是去设计可靠且高效的验证方案。**

大家一起把在使用中踩过的坑都收集起来，组合成一个针对单个步骤的mcp踩坑指南，远比给出一套不知道会生成什么结果的提示词更有意义。

可靠性大于自主性，还是那句话，生成的alpha你自己是否愿意投钱？

没有否定mcp工具的意思，恰恰相反，任何工具在明确其能力边界后才能更好的使用。

但是期待全自动挖矿短期内看不大现实。只去鞭策AI干活很难得到一个好的结果，看来成功还是没有捷径。

最后引用原文作者的另一篇文章中的观点做总结：

“这些AI工具应被视为辅助工具而非替代品。

关键在于，开发者需要懂得如何有效结合人工智能和传统工程，

利用AI处理生成、理解和梳理任务，而对于核心逻辑和系统架构依然需要人为控制。

总体来看，工具还在快速发展中，但不要盲信所有“自动化”的宣传，要理性认识它们的实际边界。”

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享，mcp确实存在鬼打墙且浪费tokens这些问题，即使是准确率很高步骤多了也存在太大的问题。
盲目追求全自动工作流确实本末倒置，得到一堆无法解释且不敢用的结果。
分步执行、人工验证、不断追问依据，这才是目前最踏实可靠的路径。
===================================================================================


---

### 技术对话片段 38 (原帖: 【own sa】一种根据使用频率进行select的方法)
- **原帖链接**: [Commented] 【own sa】一种根据使用频率进行select的方法.md
- **时间**: 9个月前

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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享，手动挑选一部分打标签颜色或者喜好都是较为好的一个做sa的方法，但是就是存在耗时较长的情况，如果可以开发一个自动化选取一部分没选取过的因子来自动打标签应该是个非常好的想法。

========================================================================================================================================================================


---

### 技术对话片段 39 (原帖: 【own sa】一种根据使用频率进行select的方法)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【own sa】一种根据使用频率进行select的方法_35157464669847.md
- **时间**: 9个月前

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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享，手动挑选一部分打标签颜色或者喜好都是较为好的一个做sa的方法，但是就是存在耗时较长的情况，如果可以开发一个自动化选取一部分没选取过的因子来自动打标签应该是个非常好的想法。

========================================================================================================================================================================


---

### 技术对话片段 40 (原帖: 【PPAC】比赛中的相关性如何影响Base payment？)
- **原帖链接**: [Commented] 【PPAC】比赛中的相关性如何影响Base payment.md
- **时间**: 1年前

**提问/主帖背景 (AK76468)**:
## 0.发现

相信很多顾问都发现了： **Self&Proc Correlation为零的alpha，它们的base payment很高** 在maxTrade theme开始的时候，我抱着测试的心态提交了 ***Alpha1*** ：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 4,00OK
> I
> 3,50OK
> 3,00OK
> 2,50OK
> 2,00OK
> 000000
> 1,50OK
> 1,0OOK
> SOOK
> 11/13/2014
> Train Pnl: 0.00
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
  
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.35
> 1.589
> 3.32
> 25.01%
> 7.509
> 316.109oo


这个base payment给到了6.07$（新人顾问，vf=0.5）

对于这一个 ***Alpha2*** ：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 12M
> 1OM
> Slow factor
> 8,00OK
> 600OK
> 4,00OK
> 2,00OK
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
> 00
> IS Summary
> Period
> IS 
> 0S
> Theme: Investability Constraints Theme X2
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: USAIDIIOPTION X1.2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.88
> 11.489
> 1.98
> 13.939
> 9.949
> 24.289o0


在slow中性化设置下的表现应该还算不错，但是在theme加成下的base是1.56$

再看这个 ***Alpha3：***

***
> [!NOTE] [图片 OCR 识别内容]
> 8,0OOK
> 7,00OK
> 6,00OK
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
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
> MrubwNWNNN
  
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.67
> 42.08%
> 0.77
> 9.009
> 4.789
> 4.289。。
*** 这个表现比 ***Alpha2*** 差很多，但是在theme加成下给了3.88$

不考虑每个alpha对组合提升的情况下：

- 对于Alpha1，尽管它的书面指标很亮眼，但是毕竟数据的窗口期太短了，是一个还需观察的“新朋友”；
- 对于Alpha2，在Slow设置下，各项指标也还算不错，是一个可以相信的“老朋友”；
- 对于Alpha3，它的表现就差很多了。我尝试降低换手率，然而性能更差，我猜想该Alpha是依靠频繁换手盈利的，可是margin只有万分之4.28，可以预见的after cost表现差；

## 1.疑问

我预期的Base排名是：Alpha2>Alpha1>Alpha3

但结果却是：Alpha1>Alpha3>Alpha2

究竟是什么原因导致Base payment不符合预期呢？

继续看其他因素， **PPAC的比赛是不检查产品相关性的，而且Sharpe>1&self corr<0.5就达到了提交标准，这意味着什么？**

## **2.再发现！**

PPAC比赛意味着你可以提交Alpha1，这种本来不能被提交的Alpha，所以 **它的Product correlation和Self Correlation都是0！**

而影响Base payment中Quality factor的一个重要的指标就是correlation，当corr=0，这意味着这一项几乎被拉满了，会使你的Quality factor出乎意料的高！


> [!NOTE] [图片 OCR 识别内容]
> Quality Factor
> Regularly check anouncements
> and Theme calendar
> Are you regularly submitting
> No
> Create Alphas in the
> theme Alphas?
> multiplier theme
> Ensure most of your submissions
> match the Theme; check Forum
> Threads
> Do you use the same datafields
> Yes
> often? Check out datasets with
> high Dataset Value Score
> Do you use the same operators
> often? Check out other operators;
> etailed description) and settings
> All (AlphalSuperalpha
> prodlself corr) in your consultant
> Yes
> Lower your Alphas'
> Explore Vector Datafields, for
> leaderboard stats are close to 0.7?
> correlations
> example Social Medie
> Try different neutralizations
> Check out Research Forum
> No
> Read "Getting started on Illiquid
> Universes:
> Diversify your pool,
> Do you submit Alphas in
> No
> try Alphas on
> Try simulating your submitted
> IlliquidlLarge Universes?
>  IliquidlLarge
> Alphas on larger (less liquid)
> Universes
> Universes
> Look for completely new signals in
> illiquid universe


再看Alpha2，我一在强调这个因子还不错，所以可以预料到已经有人交过了。毫不意外，它的self corr=0.29，prod corr=0.76，它的相关性相比Alpha1“太高了”，这就是导致它base只有1.5的主要原因吧。

然后也就不难理解Alpha3会有3.88$了，首先它的fitness<1，场外（比赛外）不能被提交，并且Turnover很高Margin又很低，after cost后表现会很差，所以没有人愿意交。那么它的Corr也都是0，这是它高base的重要原因。

## 3.认知

我再一次深刻地认识到了Correlation的重要性，它是如何影响着顾问们的每日收入的，为什么平台会强调尽可能的降低Correlation，以及为什么提交了表现看似不好的alpha，却对组合有增益。

> *菜市场里不可能全是卖苹果的，也不可能是全是卖猪肉的，不然迟早要倒闭*

当你是市场里唯一一个卖苹果的人，假设人们对苹果的需求是固定的，那么所有的需求都被你消化掉，利润固然很可观；当市场里卖苹果的人变多了，你的利润就要被瓜分了。 **换句话说，你的商品/销售模式/策略等等，原本的独特性就被稀释调了。**

这是WorldQuant不愿看到的，所以会通过Base来激励顾问们走向健康的方向。针对上面问题，一个比较好的解决方案是：增加商品/销售模式/策略的多样性，什么都售卖，建造一个超级商超，不会因为单一商品受到较大的影响。

这可能是PPAC比赛的目的之一吧： **纯粹与多样**

> 以上内容仅针对个人，是新人顾问在学习中的探索与发现，绝不是鼓励大家交什么样Alpha。比如Alpha1，尽管它的报酬很高，但是也要承担因为样本量少而可能引发的高风险；比如Alpha2，尽管它的报酬低，但是它的OS可信度更高，更容易提高比赛分数，相信阅读此文大家会有自己的判断。

最后，欢迎大家在评论区留下你们的Base payment与相关性的情况，如果有不一样的见解，希望大家多讨论！！！

LOVE&PEACE :D

**顾问 MS51256 (Rank 28) 的解答与建议**:
-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

华子哥我见解确实独到，sc pc低base高 但是可能并不是很好的因子

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------


---

### 技术对话片段 41 (原帖: 【PPAC】比赛中的相关性如何影响Base payment？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【PPAC】比赛中的相关性如何影响Base payment_31248622176791.md
- **时间**: 1年前

**提问/主帖背景 (AK76468)**:
## 0.发现

相信很多顾问都发现了： **Self&Proc Correlation为零的alpha，它们的base payment很高** 在maxTrade theme开始的时候，我抱着测试的心态提交了 ***Alpha1*** ：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 4,00OK
> I
> 3,50OK
> 3,00OK
> 2,50OK
> 2,00OK
> 000000
> 1,50OK
> 1,0OOK
> SOOK
> 11/13/2014
> Train Pnl: 0.00
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
  
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.35
> 1.589
> 3.32
> 25.01%
> 7.509
> 316.109oo


这个base payment给到了6.07$（新人顾问，vf=0.5）

对于这一个 ***Alpha2*** ：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 12M
> 1OM
> Slow factor
> 8,00OK
> 600OK
> 4,00OK
> 2,00OK
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
> 00
> IS Summary
> Period
> IS 
> 0S
> Theme: Investability Constraints Theme X2
> Single Data Set Alpha
> Power Pool Alpha
> Pyramid theme: USAIDIIOPTION X1.2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.88
> 11.489
> 1.98
> 13.939
> 9.949
> 24.289o0


在slow中性化设置下的表现应该还算不错，但是在theme加成下的base是1.56$

再看这个 ***Alpha3：***

***
> [!NOTE] [图片 OCR 识别内容]
> 8,0OOK
> 7,00OK
> 6,00OK
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
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
> MrubwNWNNN
  
> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.67
> 42.08%
> 0.77
> 9.009
> 4.789
> 4.289。。
*** 这个表现比 ***Alpha2*** 差很多，但是在theme加成下给了3.88$

不考虑每个alpha对组合提升的情况下：

- 对于Alpha1，尽管它的书面指标很亮眼，但是毕竟数据的窗口期太短了，是一个还需观察的“新朋友”；
- 对于Alpha2，在Slow设置下，各项指标也还算不错，是一个可以相信的“老朋友”；
- 对于Alpha3，它的表现就差很多了。我尝试降低换手率，然而性能更差，我猜想该Alpha是依靠频繁换手盈利的，可是margin只有万分之4.28，可以预见的after cost表现差；

## 1.疑问

我预期的Base排名是：Alpha2>Alpha1>Alpha3

但结果却是：Alpha1>Alpha3>Alpha2

究竟是什么原因导致Base payment不符合预期呢？

继续看其他因素， **PPAC的比赛是不检查产品相关性的，而且Sharpe>1&self corr<0.5就达到了提交标准，这意味着什么？**

## **2.再发现！**

PPAC比赛意味着你可以提交Alpha1，这种本来不能被提交的Alpha，所以 **它的Product correlation和Self Correlation都是0！**

而影响Base payment中Quality factor的一个重要的指标就是correlation，当corr=0，这意味着这一项几乎被拉满了，会使你的Quality factor出乎意料的高！


> [!NOTE] [图片 OCR 识别内容]
> Quality Factor
> Regularly check anouncements
> and Theme calendar
> Are you regularly submitting
> No
> Create Alphas in the
> theme Alphas?
> multiplier theme
> Ensure most of your submissions
> match the Theme; check Forum
> Threads
> Do you use the same datafields
> Yes
> often? Check out datasets with
> high Dataset Value Score
> Do you use the same operators
> often? Check out other operators;
> etailed description) and settings
> All (AlphalSuperalpha
> prodlself corr) in your consultant
> Yes
> Lower your Alphas'
> Explore Vector Datafields, for
> leaderboard stats are close to 0.7?
> correlations
> example Social Medie
> Try different neutralizations
> Check out Research Forum
> No
> Read "Getting started on Illiquid
> Universes:
> Diversify your pool,
> Do you submit Alphas in
> No
> try Alphas on
> Try simulating your submitted
> IlliquidlLarge Universes?
>  IliquidlLarge
> Alphas on larger (less liquid)
> Universes
> Universes
> Look for completely new signals in
> illiquid universe


再看Alpha2，我一在强调这个因子还不错，所以可以预料到已经有人交过了。毫不意外，它的self corr=0.29，prod corr=0.76，它的相关性相比Alpha1“太高了”，这就是导致它base只有1.5的主要原因吧。

然后也就不难理解Alpha3会有3.88$了，首先它的fitness<1，场外（比赛外）不能被提交，并且Turnover很高Margin又很低，after cost后表现会很差，所以没有人愿意交。那么它的Corr也都是0，这是它高base的重要原因。

## 3.认知

我再一次深刻地认识到了Correlation的重要性，它是如何影响着顾问们的每日收入的，为什么平台会强调尽可能的降低Correlation，以及为什么提交了表现看似不好的alpha，却对组合有增益。

> *菜市场里不可能全是卖苹果的，也不可能是全是卖猪肉的，不然迟早要倒闭*

当你是市场里唯一一个卖苹果的人，假设人们对苹果的需求是固定的，那么所有的需求都被你消化掉，利润固然很可观；当市场里卖苹果的人变多了，你的利润就要被瓜分了。 **换句话说，你的商品/销售模式/策略等等，原本的独特性就被稀释调了。**

这是WorldQuant不愿看到的，所以会通过Base来激励顾问们走向健康的方向。针对上面问题，一个比较好的解决方案是：增加商品/销售模式/策略的多样性，什么都售卖，建造一个超级商超，不会因为单一商品受到较大的影响。

这可能是PPAC比赛的目的之一吧： **纯粹与多样**

> 以上内容仅针对个人，是新人顾问在学习中的探索与发现，绝不是鼓励大家交什么样Alpha。比如Alpha1，尽管它的报酬很高，但是也要承担因为样本量少而可能引发的高风险；比如Alpha2，尽管它的报酬低，但是它的OS可信度更高，更容易提高比赛分数，相信阅读此文大家会有自己的判断。

最后，欢迎大家在评论区留下你们的Base payment与相关性的情况，如果有不一样的见解，希望大家多讨论！！！

LOVE&PEACE :D

**顾问 MS51256 (Rank 28) 的解答与建议**:
-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

华子哥我见解确实独到，sc pc低base高 但是可能并不是很好的因子

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------


---

### 技术对话片段 42 (原帖: 【大角羊】VF0.5-0.62-0.89-0.96-0.96，辛苦耕耘-终得硕果！)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiX%2FqP7LyE6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzY0ODk5NjkwMDgyNzktLSVFNSVBNCVBNyVFOCVBNyU5MiVFNyVCRSU4QS1WRjAtNS0wLTYyLTAtODktMC05Ni0wLTk2LSVFOCVCRSU5QiVFOCU4QiVBNiVFOCU4MCU5NSVFOCU4MCU5OC0lRTclQkIlODglRTUlQkUlOTclRTclQTElOTUlRTYlOUUlOUMGOwhUOg5zZWFyY2hfaWRJIik2ZTg5NzNkOC0wODhhLTQ1NWEtYWE3Mi0zODM1ZmM1NzFhOWIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxNUzUxMjU2BjsIVDoScmVzdWx0c19jb3VudGkt--fd5419c2726996a2255c85d3ee200cdf0bbceadc
- **时间**: 6个月前

**提问/主帖背景 (AL13375)**:
我是2024年11月份加入的WQ，2025年1月份暂时离开，于2025年5月份中旬重新回归。算下来，应该是个“老”新人吧。刚回来的时候，基本上把WQ的知识全部忘完了，幸好有认识的顾问帮助才重新拾起来这份工作，同时也感谢老师们和其他顾问大佬们的热心答疑！刚回来的时候，VF已经回归到了0.5，按照VF的更新规则，我要等到八月份才能看到VF的变化，也就是说，我还需要在得不到任何反馈的情况下坚持三个月的努力，这一度让我怀疑过这份付出是否值得。但好在我有许多顾问朋友的陪伴和支持，这里特别感谢孙哥、Mike哥、琪姐、小虎哥、橘子姐、强哥、虎哥等等，你们是我量化研究道路上同行伙伴，也是我的榜样！回归到量化研究上来，首先附上我从五月份至今的alpha提交情况和combine、VF变化情况表：为方便新人理解，简单介绍一下各个VF对应alpha的情况，这里大佬们可以直接跳过：VF0.62对应的是5、6月份提交的alpha；VF0.89对应的是5、6、7月份提交的alpha；VF0.96对应的是6、7、8月份提交的alpha；VF0.96对应的是7、8、9月份提交的alpha。可以看出，我提交的alpha数量并不稳定，这主要是因为我并没有很强的做alpha的能力，所以只能勉强保持一天一两个的alpha的提交（ra+sa）。但是可以从combine和VF的变化上可以看出来，这样也是可以拿到高的combine和VF的。抛去提交数量这个影响VF变化的因素，我总结了几个可能会对VF有提升的经验：交SA!多做ATOM多做D1没有把握的情况下不要碰小地区和D0多点塔，不要在单一数据集上交太多alpha提交alpha之前关注近两年表现关注invest的PNL表现观察Performance Comparison低SC、PC感谢看到这里的顾问朋友们，无论你的VF身处低谷还是VF历经一波三折，都不要放弃未来的希望，永远向上吧朋友们！* 感谢WQ平台，感谢凯哥、weijie老师、kunqi老师的指导，感谢华子哥、游戏王、冷神等大佬的分享，祝愿大家越来越好！

**顾问 MS51256 (Rank 28) 的解答与建议**:
===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================感谢大角羊的分享，vf与genius等级的提升对大佬来说是水到渠成的事情，有所努力就会有所收获，成功是努力后应有的果实。可以看出super alpha还是极为重要的，vf combine的提升降低都与sa记为相关，分散性也是极为重要的。================================Do your best ================================


---

### 技术对话片段 43 (原帖: 【大角羊】VF0.5-0.62-0.89-0.96-0.96，辛苦耕耘-终得硕果！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【大角羊】VF05-062-089-096-096辛苦耕耘-终得硕果_36489969008279.md
- **时间**: 6个月前

**提问/主帖背景 (AL13375)**:
我是2024年11月份加入的WQ，2025年1月份暂时离开，于2025年5月份中旬重新回归。算下来，应该是个“老”新人吧。刚回来的时候，基本上把WQ的知识全部忘完了，幸好有认识的顾问帮助才重新拾起来这份工作，同时也感谢老师们和其他顾问大佬们的热心答疑！

刚回来的时候，VF已经回归到了0.5，按照VF的更新规则，我要等到八月份才能看到VF的变化，也就是说，我还需要在得不到任何反馈的情况下坚持三个月的努力，这一度让我怀疑过这份付出是否值得。但好在我有许多顾问朋友的陪伴和支持，这里特别感谢孙哥、Mike哥、琪姐、小虎哥、橘子姐、强哥、虎哥等等，你们是我量化研究道路上同行伙伴，也是我的榜样！

回归到量化研究上来，首先附上我从五月份至今的alpha提交情况和combine、VF变化情况表：


> [!NOTE] [图片 OCR 识别内容]
> 数值
> 月份
> 娄型
> R COIJNTT
> 鼬 COIJNT
> 28
> 13
> 11
> S[JJ
> 70
> conbile
> 2.61
> &52
> SEIected conbine
> HPa
> conbile
> 1.5
> 2.15
> 1.91
> 0.62
> 0.89^
> 0.96
> 0.96


为方便新人理解，简单介绍一下各个VF对应alpha的情况，这里大佬们可以直接跳过：

VF0.62对应的是5、6月份提交的alpha；

VF0.89对应的是5、6、7月份提交的alpha；

VF0.96对应的是6、7、8月份提交的alpha；

VF0.96对应的是7、8、9月份提交的alpha。

可以看出，我提交的alpha数量并不稳定，这主要是因为我并没有很强的做alpha的能力，所以只能勉强保持一天一两个的alpha的提交（ra+sa）。但是可以从combine和VF的变化上可以看出来，这样也是可以拿到高的combine和VF的。

抛去提交数量这个影响VF变化的因素，我总结了几个可能会对VF有提升的经验：

- 交SA!
- 多做ATOM
- 多做D1
- 没有把握的情况下不要碰小地区和D0
- 多点塔，不要在单一数据集上交太多alpha
- 提交alpha之前关注近两年表现
- 关注invest的PNL表现
- 观察Performance Comparison
- 低SC、PC

感谢看到这里的顾问朋友们，无论你的VF身处低谷还是VF历经一波三折，都不要放弃未来的希望，永远向上吧朋友们！

* 感谢WQ平台，感谢凯哥、weijie老师、kunqi老师的指导，感谢华子哥、游戏王、冷神等大佬的分享，祝愿大家越来越好！

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢大角羊的分享，vf与genius等级的提升对大佬来说是水到渠成的事情，有所努力就会有所收获，成功是努力后应有的果实。
可以看出super alpha还是极为重要的，vf combine的提升降低都与sa记为相关，分散性也是极为重要的。

================================Do your best ================================**


---

### 技术对话片段 44 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【工具分享】用Claude Code  MCP搭建全自动因子挖掘流水线的实践论坛精选_38979342434455.md
- **时间**: 3个月前

**提问/主帖背景 (LH94963)**:
最近看到论坛上越来越多大佬分享AI挖因子的经验，什么TRAE + MCP、Gemini CLI + Agent、Claude Skills模块化……说实话看得我又兴奋又焦虑。兴奋是因为这条路确实可行，焦虑是因为感觉不跟上就要被卷飞了。

所以我花了大概两周时间，搭了一套自己的自动化流水线，目前已经稳定跑了一个多月。今天来做一个比较详细的分享，尽量把我踩过的坑和想明白的东西都说清楚。

### 一、我的背景和动机

看到论坛上大佬的帖子，才意识到MCP这个东西的存在——原来可以让AI直接调BRAIN的API，不用自己写一行请求代码！

所以我想搭一个 **尽量简单、但真正能跑起来** 的方案。

### 二、整体架构

核心就三层，画个简单的图：

```
┌─────────────────────────────────────────────┐
│              Claude Code (主控大脑)            │
│  - 分析数据集字段特征                           │
│  - 基于金融逻辑生成alpha候选表达式               │
│  - 分析回测结果，决定下一步策略                   │
│  - 对过线alpha做变体生成和微调                   │
└──────────────────┬──────────────────────────┘
                   │ 调用MCP工具
┌──────────────────▼──────────────────────────┐
│           WQ Brain MCP (执行层)               │
│  - 查询数据集和字段信息                         │
│  - 批量提交simulation（8个一批！）               │
│  - 拉取回测结果和alpha详情                      │
│  - 检查相关性（Self Corr / Prod Corr）          │
└──────────────────┬──────────────────────────┘
                   │ 读写缓存
┌──────────────────▼──────────────────────────┐
│           本地SQLite (缓存和记录)               │
│  - 已回测表达式去重（避免重复浪费）               │
│  - alpha详情缓存（减少API调用）                  │
│  - 挖掘日志和统计                               │
└─────────────────────────────────────────────┘
```

为什么选Claude Code而不是Cursor/TRAE？主要是因为Claude Code是命令行工具， **天然适合长时间无人值守运行** 。Cursor之类的IDE工具虽然交互体验好，但跑久了容易卡、上下文容易断。Claude Code挂在终端里，该干嘛干嘛，非常稳。

### 三、工作流程详解

整个流程分5个阶段，每个阶段都有一些关键细节：

**阶段1：数据集和字段分析**

不是上来就瞎跑。我会先让AI分析目标数据集的字段分布：

- 哪些字段覆盖率高（coverage > 70%的优先）
- 哪些字段是连续型的（适合ts操作）vs 离散型的
- 哪些字段更新频率高（每天 vs 季度）

这一步很重要，能过滤掉60%以上的无效尝试。比如一个coverage只有30%的字段，你怎么折腾Sharpe都上不去。

**阶段2：候选表达式生成**

这是AI发挥价值最大的地方。我在system prompt里给了几条核心规则：

1. **每批必须恰好8个表达式** ——这是BRAIN API的硬性要求，多了少了都不行
2. **同一批内的8个表达式要有差异性** ——不同字段、不同操作符、不同窗口长度，避免浪费
3. **优先用简单的操作符组合** ——2-3层嵌套为主，不要一上来就搞5-6层
4. **每个表达式必须有明确的金融逻辑** ——"为什么这个因子会有预测力？"说不清楚的不要

一个比较好的prompt技巧是：先让AI分析一批已经通过的alpha的共性特征，然后基于这些特征去生成新的候选。这比让AI从零开始想要高效得多。

**阶段3：批量回测和结果分析**

表达式生成后，通过MCP批量提交回测。这里有几个关键的坑：

**坑1：回测不是即时返回的。**  提交后需要轮询等待结果，有时候一批8个要等2-3分钟。我一开始没处理好这个等待逻辑，AI一直在那转圈浪费token。后来在prompt里加了明确的等待指令，好多了。

**坑2：错误处理很重要。**  有些表达式语法没问题但回测会报错（字段不支持某个操作符、覆盖率不足等），需要AI能理解错误信息并跳过，而不是卡住。

**坑3：一定要做结果缓存。**  同样的表达式+同样的参数，回测结果是确定的。我用SQLite把所有回测过的表达式都记录下来，下次遇到相同或相似的直接跳过。这一个优化大概节省了30%的API调用。

**阶段4：过线alpha的深度分析**

对于初筛通过（Sharpe > 1.5, Fitness > 0.8）的alpha，不是直接提交，而是做进一步分析：

1. **查看yearly stats** ：确认不是靠某一年暴涨撑起来的
2. **看PnL曲线** ：近两年必须是稳定上升的
3. **检查Prod Corr** ：和已有alpha的相关性不能太高
4. **尝试微调** ：换decay、换neutralization，看能不能进一步优化

这个阶段我会让AI给出详细的分析报告，然后 **我自己做最终决策** 。提交这一步我不让AI自动执行，必须人工确认。

**阶段5：变体生成（可选）**

对于表现好的alpha，让AI生成变体：

- 换一个相近的字段
- 调整lookback窗口
- 增加一层ts_mean平滑
- 换一个group操作符

变体和原始alpha的相关性要控制在0.6以内，否则不值得交。

### 四、一些关键的Prompt工程技巧

说实话这套系统的核心不在代码，在于 **怎么给AI下指令** 。分享几条我反复调试后沉淀下来的规则：

**1. "8个一批"必须反复强调**

这条规则我在prompt里写了三遍，分别在开头、中间、和回测前的提醒里。不这么做的话，AI经常会"贴心地"一次生成10个或者12个，然后API就报错了。

**2. 给AI看成功案例**

与其告诉AI"生成好的alpha"，不如直接给它看几个已经通过的alpha的表达式和指标，让它自己总结规律。AI学习模式 >> 遵循指令。

**3. 明确禁止事项**

比如：

- 禁止跨数据集引用字段（ATOM规则）
- 禁止使用超过8个操作符
- 禁止生成和已缓存的表达式重复或高度相似的

这些"不要做什么"往往比"要做什么"更重要。

**4. 让AI自我反思**

每跑完一批，我会让AI总结："这批8个里面哪些过了？哪些没过？没过的原因可能是什么？下一批应该怎么调整？"

这个反思环节对提升出货率帮助很大。

### 五、真实数据和效果

跑了一个半月，数据如下（以USA_D1_TOP3000为主）：

指标

数据

总共回测的表达式数

~3200个

初筛通过（Sharpe > 1.5）

~120个（3.75%）

IS全部通过

~45个（1.4%）

PC < 0.7可提交

18个（0.56%）

最终实际提交

14个

平均每天回测量

~70个表达式

平均每天token消耗

约10万token

对比我之前纯手动的效率（一天20-30个，出货率<0.3%），提升大概是 **3-5倍的速度 + 2倍的出货率** 。

说实话没有论坛上某些大佬说的那么夸张（"一天出10个可提交alpha"），但对我这个水平来说已经很满意了。

### 六、踩过的坑（血泪总结）

**坑1：上下文爆炸**

Claude Code的上下文是有限的。如果你一口气让它跑50批回测，到后面它会"忘记"前面的结果和约束条件，开始重复生成一样的表达式。

**解决方案** ：每跑10批左右就让AI做一次总结，把关键信息压缩记录下来，然后可以清理上下文重新开始。

**坑2：AI会"偷懒"**

跑久了AI会倾向于生成和之前通过的alpha很相似的表达式——因为这样"安全"。但这些相似的alpha之间相关性很高，交了也没用。

**解决方案** ：在prompt里加入"多样性要求"，强制每批至少覆盖2个不同的数据集字段或操作符组合。

**坑3：晚上跑经常断**

Claude Code长时间运行有时会因为网络波动或者API限流中断。

**解决方案** ：做好断点恢复——每批结果都实时写入SQLite，中断后可以从上次的进度继续。

**坑4：API限流**

BRAIN的API有调用频率限制，跑太快会被throttle。

**解决方案** ：控制并发数，我现在设的是同时最多2个worker，每批之间间隔30秒。慢是慢了点，但稳定。

### 七、成本分析

大家肯定关心成本问题，我算了一下：

成本项

月均费用

Claude API token

~$15-20

我的时间（每天review 30分钟）

无价（笑）

**总计**

**~$15-20/月**

产出是平均每月10-15个可提交alpha，如果VF表现OK的话，月收入能到$150-200。ROI还是很可观的。

当然如果你用的是Claude Code的订阅版（$20/月），那成本就是固定的，跑多少都一样，更划算。

### 八、写在最后

这套系统不完美，还有很多可以优化的空间：

- 可以加入更智能的策略演化（比如遗传算法的思路）
- 可以做多区域并行挖掘
- 可以把变体生成和自相关检查也自动化

但对于个人用户来说，我觉得 **够用就好** 。过度工程化反而会分散精力，不如把时间花在理解金融逻辑和分析alpha质量上。

**顾问 MS51256 (Rank 28) 的解答与建议**:
666向优秀的大佬学习，感谢分享

#========= WORLDQUANT BRAIN CONSULTANT ========== #
#每天进步一点点，加油
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================加油每一天=======================#


---

### 技术对话片段 45 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【差生文具多】WQ助手101版本安卓版本_38182819864471.md
- **时间**: 3个月前

**提问/主帖背景 (ZZ43261)**:
之前发布了1.0版本之后，在一些兄弟们的反馈和我自己使用发现了一些bug，这个版本主要是解决以下bug问题。

修复列表：

1 收入统计之前未计算sa部分- 已修复

2 alpha今日提交的sa卡槽未能正确显示sa-已修复

3 data查询页面双单词字段的传参错误不能正确查询-已修复

4 偶发登陆后还是报错401无权限问题-已修复

另外有一些之前设计的功能可能UI提示做的不好,提醒一下大家我还有这些功能：

1 六维卡片可以点击查看过去趋势图表


> [!NOTE] [图片 OCR 识别内容]
> 欢迎:ZZ43261
> 登出
> 数据更新时间
> 2026-02-0517.27.34
> 加载
> 平均表达式变化趋势
> 5.5
> 加载
>  
> 12/19
> 12/19
> 12/22
> 12/22
> 1/4
> 1/4
> 1/6
> 1/6
> 1/8
> 1/8
> 1/9
> 1/9
> 1/14
> 1/14
> 1/30
> 1/30
> 2/3
> 2/3
> 2/5
> 总数据
> 加载
> 苜页
> Alpha
> 记录


2 在金字塔表格中点击格子可以自动跳转对应data查询


> [!NOTE] [图片 OCR 识别内容]
> 点塔数
> 提交数
> 加载上季赓
> 加载本季度
> Category
> ASI
> CHN
> CHN
> EUR
> EUR
> GLB
> IND
> JPN
> JPN
> USA
> USA
>  delay
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> News
> Option
> 首
> Alpha
> 记录
> 数据
> 罾


接下来是对一些兄弟们想要github源码的回复：首先说结论，暂时不准备公布源码。原因主要是因为app中使用的一些接口不是官方公开发布的，我担心会违反某些协议。另外我相信如果有使用源码能力的兄弟们想要获取这些接口也不是难事，除了这些接口的整合我的app暂时还没弄什么其他功能。拿不到这些接口的拿源码也没啥用。

最后是接下来app开发的几个方向

1 加入回测功能 或者部署一个回测脚本的服务端用app远程调用，真正实现手机玩wq

2 加入alpha pnl的展示，之前因为我对alpha的学习不深入没觉得pnl很有用就没加

3 探索和mcp app的整合交互

最后最重要的下载地址： [[链接已屏蔽])

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 46 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **时间**: 3个月前

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

**[[MCP]找灵感功能上手详解](../顾问 QL47372 (Rank 36)/[L2] [MCP]找灵感功能上手详解经验分享_37113649831831.md)**

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 47 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
===============================================================

===============================================================

感谢大佬的分享，十分感谢。点塔王

===============================================================

===============================================================


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞.md
- **时间**: 3个月前

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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，祝您发财
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 49 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
===============================================================

===============================================================

感谢大佬的分享，十分感谢。点塔王

===============================================================

===============================================================


---

### 技术对话片段 50 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md
- **时间**: 3个月前

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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，祝您发财
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 51 (原帖: 【新人指南】到底要交什么样的Alpha？置顶的)
- **原帖链接**: [Commented] 【新人指南】到底要交什么样的Alpha置顶的.md
- **时间**: 1年前

**提问/主帖背景 (XZ23611)**:
## **到底要交什么样的Alpha？——新人指南**

在Alpha开发与提交的过程中，许多新人常常会问：“到底什么样的Alpha才值得提交？”这是一个复杂的问题，因为Alpha的质量并没有一个单一的“金标准”可以作为绝对的判断依据。新人常见的错误是过度依赖某一两个单一指标，比如  **Sharpe** 、 **Fitness**  或  **Margin** ，认为只要这些指标表现良好，Alpha就一定值得提交。

然而，判断一个Alpha是否值得提交更像是诊断病情——不能仅仅依靠一个指标或单一的维度来做出决定。单一指标可能会提供片面的信息，而忽略了Alpha整体表现的复杂性和多样性。这种过度依赖单一指标的思维方式，往往会导致新人在Alpha提交过程中出现偏差。

### **数量与质量的平衡：螺旋上升的原则**

在Alpha的开发与提交过程中， **数量** 和 **质量** 是两个不可分割的重要维度。许多新人在实践中常常犯两个极端的错误：要么过度关注质量而忽视数量，要么完全不管质量，只追求数量。这两种错误都会对Alpha的整体表现产生负面影响。

#### **数量不足的问题**

如果过度追求质量而导致提交的Alpha数量不足，可能会出现以下问题：

1. **Portfolio不稳定** ：
   Alpha的数量不足会导致整体Portfolio的表现缺乏多样性，从而增加OS（Out-of-Sample）结果的不稳定性。
2. **缺乏真实水平的验证** ：
   单个Alpha的表现可能具有偶然性，只有通过足够的数量才能更接近整体的真实水平，避免因个别Alpha的异常表现而影响整体判断。

#### **质量不足的问题**

另一方面，如果完全忽视质量，只追求数量，也会带来风险：

1. **Portfolio表现受损** ：
   大量低质量的Alpha会拉低整体Portfolio的表现，导致Margin、Sharpe等关键指标下降。
2. **资源浪费** ：
   提交大量低质量Alpha不仅浪费了开发时间，也可能对平台的审核资源造成压力。

#### **螺旋上升的原则**

数量和质量并非对立，而是一个螺旋上升的过程。新人在初期阶段可以优先解决数量的问题，通过提交足够数量的Alpha来建立基础，然后逐步提高质量要求，最终实现数量与质量的平衡。

- **新人建议** ：
  每个月提交的Alpha数量不要少于  **40个** 。这一数量可以帮助新人更接近整体的真实水平，同时避免因单月表现异常而影响长期结果。
  - **数量的意义** ：足够的数量可以为Portfolio提供多样性，降低单个Alpha表现异常对整体的影响。
  - **质量的提升** ：在数量达到一定基础后，可以逐步提高Alpha的质量要求，例如优化Turnover、Margin等关键指标。

### **平台的“最低标准”与其意义**

在Alpha提交过程中，平台设定了一些“最低标准”，这是每位新人必须满足的基本要求。这些标准的存在并非是为了限制，而是为了确保Alpha在实际应用中具有一定的可行性和质量。然而，许多新人在实践中往往只关注如何通过这些指标，而忽略了这些要求背后的逻辑和意义。

#### **Turnover的要求**

**Turnover**  是一个重要的指标，它衡量了Alpha的换手率。平台要求Turnover不能高于  **70%** ，这是为了避免交易频率过高导致交易成本过高，从而影响  **Margin**  的表现。换手率过高会显著增加手续费，最终削弱Alpha的盈利能力。

- **进阶建议** ：
  - 当你的水平到达一定程度，建议将Turnover控制在  **30%**  以下。
  - 当你已经不再断粮，建议将这一指标进一步降低至  **15%**  以下。
- **特殊情况** ：
  - 如果Turnover较高，但  **Margin**  同时表现非常优秀（例如Margin超过  **10** ），这种情况下高换手率是可以接受的。

#### **Turnover的下限**

平台同时要求Turnover不能低于  **1%** ，这一点常常让新人感到困惑。事实上，这一要求的意义在于避免Alpha的持仓过于稳定。换手率过低会导致Position长期不变，而这与对冲基金的核心理念相悖。对冲基金的本质是通过动态调整持仓来捕捉市场机会，而过低的换手率可能意味着Alpha缺乏足够的市场反应能力。

### **Sub Universe与Robust Test的重要性**

在Alpha的评估过程中， **Sub Universe**  是一个关键的测试维度。平台要求Alpha在较小的股票范围（Sub Universe）中仍然保持一定的表现，这一要求的最低标准是  **50%**  的Sharpe。这意味着，如果Alpha在当前的Universe（例如Top3000股票）中表现良好，那么在更小的Universe（例如Top1000股票）中，它的Sharpe也必须达到至少50%的水平。

#### **Sub Universe的原理**

这一要求的核心逻辑是为了避免Alpha的信号仅来源于流动性较低的小市值股票。如果一个Alpha在Top3000股票中表现良好，但在Top1000股票中完全失效，这通常表明其收益主要依赖于流动性较低的那2000只股票。这种情况可能会导致Alpha在实际应用中面临较大的风险，例如流动性不足或交易成本过高。

#### **Robust Test的概念**

**Robust Test**  是一个更广泛的概念，旨在通过调整各种参数来测试Alpha的稳定性和敏感性。具体来说，Robust Test可以包括以下两种方式：

1. **调整Settings中的指标** ：
   - 例如修改交易成本、滑点、或其他市场环境参数，观察Alpha的表现是否稳定。
2. **调整Expression中的参数** ：
   - 修改Alpha表达式中的关键参数，测试结果的敏感性。
   - 如果结果收敛性较好，说明Alpha具有较强的鲁棒性；如果结果发散性较强，则表明Alpha可能过于依赖某些特定条件。

#### **实践建议**

- **前期阶段** ：
  在Alpha开发的初期，可以暂时不需要过多关注Robust Test，重点放在满足平台的最低要求（如Sub Universe的表现）。
- **后期阶段** ：
  随着经验的积累，可以逐步加强Robust Test的强度，通过调整参数和环境来验证Alpha的稳定性。

### **IS测试与长期稳定性：Alpha的“望诊”**

在Alpha的评估过程中， **IS Ladder Testing** （针对Regular Alpha）和 **2-Year Testing** （针对Atom Alpha）是平台用于检测Alpha稳定性的重要工具。这些测试的核心目标是通过观察Alpha的PNL表现，评估其长期稳定性。这一过程类似于“望诊”，通过观察PNL的形状来判断Alpha的健康状况。

#### **PNL的理想形状**

最理想的PNL表现是一条从左下角到右上角的稳定直线。这种形状表明Alpha在长期内具有持续的盈利能力和较低的波动性，是稳定性和可靠性的最佳体现。

- **新人阶段的目标** ：
  对于新人来说，能够通过平台的IS Ladder Testing或2-Year Testing已经是一个不错的开始。这表明Alpha在基本稳定性方面达到了平台的最低要求。

#### **进阶要求**

在进阶阶段，可以通过以下标准来进一步评估Alpha的长期稳定性：

1. **过去10年的表现** ：
   - 在过去10年中，Alpha的Sharpe超过  **1**  的年份不少于  **X年** （具体标准可根据个人目标设定）。
2. **最近两年的表现** ：
   - 特别关注最近两年的PNL表现，尤其是  **2022年**  的表现。

### **为什么要有PPAC？低相关性与Portfolio的多样性**

在Alpha开发与提交的过程中，平台引入了  **PPAC**  的机制，这不仅是为了给新人提供一个更宽松的探索环境，更重要的是为了强调  **低相关性**  和  **Portfolio的多样性**  对整体表现的重要性。

#### **Portfolio的概念：你的军队**

为了更直观地理解Portfolio的意义，可以将它比喻为一支军队。以往的Alpha评估标准过度追求  **Sharpe**  和  **Fitness**  等单一指标，这就像你的军队里清一色都是身高体壮的步兵。虽然这些步兵看起来很强壮，但缺乏多样性会让你的军队在面对复杂战场时显得单薄。

要让你的军队更有战斗力，就需要补充更多的兵种，例如：

- **斥候** ：负责侦查，提供灵活性。
- **炮兵** ：提供远程打击能力。
- **后勤兵** ：确保资源供应，维持军队的稳定性。

同样的道理，Alpha的Portfolio也需要多样性。一个多样化的Portfolio可以更好地应对不同的市场环境（OS），从而提升整体的稳定性和表现。

Self Correlation是一个很直观指标，新人的时候0.7是平台的要求。PPAC的要求是Pool内0.5的要求。值得一提的是这里的SC会随着提交数量的变多而更难有低的表现

- 0.5-0.7 之间的sc是可以通过的标准
- 0.3-0.5 之间的sc已经是很不错的了，通常对portfolio有一些提升
- 0.3以下的sc通常是很低的了

### **经济学意义与OS表现：从Alpha描述开始**

在Alpha开发与提交过程中， **经济学意义**  是决定OS（Out-of-Sample）表现的关键因素之一。许多老师常常强调这一点，因为具有经济学意义的Alpha往往能够更好地适应不同的市场环境，展现出更强的稳定性和可靠性。

#### **写Description的重要性**

对于新人来说，写好Alpha的  **Description** （描述）是一个非常重要的环节。这不仅是对Alpha逻辑的总结，也是开发者学习和思考的过程。可以将Description视为自己的学习日记，通过记录Alpha的核心逻辑和设计思路，帮助自己更好地理解经济学意义。

### **总结**

Alpha的开发与提交是一项复杂的任务，既需要满足平台的最低要求，也需要从长期稳定性、Portfolio优化和经济学意义的角度进行深入思考。新人在实践中应避免过度依赖单一指标，重视数量与质量的平衡，关注整体Portfolio的表现，并通过写Description来梳理自己的思路和逻辑。希望这篇指南能够帮助新人更好地理解Alpha开发的核心原则，并逐步提升自己的能力。

**顾问 MS51256 (Rank 28) 的解答与建议**:
========================================================================================================================================================================
学到了，我提交的因子质量太差了，难怪我vf0.62
========================================================================================================================================================================


---

### 技术对话片段 52 (原帖: 【新人指南】到底要交什么样的Alpha？置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【新人指南】到底要交什么样的Alpha置顶的_32226888249239.md
- **时间**: 1年前

**提问/主帖背景 (XZ23611)**:
## **到底要交什么样的Alpha？——新人指南**

在Alpha开发与提交的过程中，许多新人常常会问：“到底什么样的Alpha才值得提交？”这是一个复杂的问题，因为Alpha的质量并没有一个单一的“金标准”可以作为绝对的判断依据。新人常见的错误是过度依赖某一两个单一指标，比如  **Sharpe** 、 **Fitness**  或  **Margin** ，认为只要这些指标表现良好，Alpha就一定值得提交。

然而，判断一个Alpha是否值得提交更像是诊断病情——不能仅仅依靠一个指标或单一的维度来做出决定。单一指标可能会提供片面的信息，而忽略了Alpha整体表现的复杂性和多样性。这种过度依赖单一指标的思维方式，往往会导致新人在Alpha提交过程中出现偏差。

### **数量与质量的平衡：螺旋上升的原则**

在Alpha的开发与提交过程中， **数量** 和 **质量** 是两个不可分割的重要维度。许多新人在实践中常常犯两个极端的错误：要么过度关注质量而忽视数量，要么完全不管质量，只追求数量。这两种错误都会对Alpha的整体表现产生负面影响。

#### **数量不足的问题**

如果过度追求质量而导致提交的Alpha数量不足，可能会出现以下问题：

1. **Portfolio不稳定** ：
   Alpha的数量不足会导致整体Portfolio的表现缺乏多样性，从而增加OS（Out-of-Sample）结果的不稳定性。
2. **缺乏真实水平的验证** ：
   单个Alpha的表现可能具有偶然性，只有通过足够的数量才能更接近整体的真实水平，避免因个别Alpha的异常表现而影响整体判断。

#### **质量不足的问题**

另一方面，如果完全忽视质量，只追求数量，也会带来风险：

1. **Portfolio表现受损** ：
   大量低质量的Alpha会拉低整体Portfolio的表现，导致Margin、Sharpe等关键指标下降。
2. **资源浪费** ：
   提交大量低质量Alpha不仅浪费了开发时间，也可能对平台的审核资源造成压力。

#### **螺旋上升的原则**

数量和质量并非对立，而是一个螺旋上升的过程。新人在初期阶段可以优先解决数量的问题，通过提交足够数量的Alpha来建立基础，然后逐步提高质量要求，最终实现数量与质量的平衡。

- **新人建议** ：
  每个月提交的Alpha数量不要少于  **40个** 。这一数量可以帮助新人更接近整体的真实水平，同时避免因单月表现异常而影响长期结果。
  - **数量的意义** ：足够的数量可以为Portfolio提供多样性，降低单个Alpha表现异常对整体的影响。
  - **质量的提升** ：在数量达到一定基础后，可以逐步提高Alpha的质量要求，例如优化Turnover、Margin等关键指标。

### **平台的“最低标准”与其意义**

在Alpha提交过程中，平台设定了一些“最低标准”，这是每位新人必须满足的基本要求。这些标准的存在并非是为了限制，而是为了确保Alpha在实际应用中具有一定的可行性和质量。然而，许多新人在实践中往往只关注如何通过这些指标，而忽略了这些要求背后的逻辑和意义。

#### **Turnover的要求**

**Turnover**  是一个重要的指标，它衡量了Alpha的换手率。平台要求Turnover不能高于  **70%** ，这是为了避免交易频率过高导致交易成本过高，从而影响  **Margin**  的表现。换手率过高会显著增加手续费，最终削弱Alpha的盈利能力。

- **进阶建议** ：
  - 当你的水平到达一定程度，建议将Turnover控制在  **30%**  以下。
  - 当你已经不再断粮，建议将这一指标进一步降低至  **15%**  以下。
- **特殊情况** ：
  - 如果Turnover较高，但  **Margin**  同时表现非常优秀（例如Margin超过  **10** ），这种情况下高换手率是可以接受的。

#### **Turnover的下限**

平台同时要求Turnover不能低于  **1%** ，这一点常常让新人感到困惑。事实上，这一要求的意义在于避免Alpha的持仓过于稳定。换手率过低会导致Position长期不变，而这与对冲基金的核心理念相悖。对冲基金的本质是通过动态调整持仓来捕捉市场机会，而过低的换手率可能意味着Alpha缺乏足够的市场反应能力。

### **Sub Universe与Robust Test的重要性**

在Alpha的评估过程中， **Sub Universe**  是一个关键的测试维度。平台要求Alpha在较小的股票范围（Sub Universe）中仍然保持一定的表现，这一要求的最低标准是  **50%**  的Sharpe。这意味着，如果Alpha在当前的Universe（例如Top3000股票）中表现良好，那么在更小的Universe（例如Top1000股票）中，它的Sharpe也必须达到至少50%的水平。

#### **Sub Universe的原理**

这一要求的核心逻辑是为了避免Alpha的信号仅来源于流动性较低的小市值股票。如果一个Alpha在Top3000股票中表现良好，但在Top1000股票中完全失效，这通常表明其收益主要依赖于流动性较低的那2000只股票。这种情况可能会导致Alpha在实际应用中面临较大的风险，例如流动性不足或交易成本过高。

#### **Robust Test的概念**

**Robust Test**  是一个更广泛的概念，旨在通过调整各种参数来测试Alpha的稳定性和敏感性。具体来说，Robust Test可以包括以下两种方式：

1. **调整Settings中的指标** ：
   - 例如修改交易成本、滑点、或其他市场环境参数，观察Alpha的表现是否稳定。
2. **调整Expression中的参数** ：
   - 修改Alpha表达式中的关键参数，测试结果的敏感性。
   - 如果结果收敛性较好，说明Alpha具有较强的鲁棒性；如果结果发散性较强，则表明Alpha可能过于依赖某些特定条件。

#### **实践建议**

- **前期阶段** ：
  在Alpha开发的初期，可以暂时不需要过多关注Robust Test，重点放在满足平台的最低要求（如Sub Universe的表现）。
- **后期阶段** ：
  随着经验的积累，可以逐步加强Robust Test的强度，通过调整参数和环境来验证Alpha的稳定性。

### **IS测试与长期稳定性：Alpha的“望诊”**

在Alpha的评估过程中， **IS Ladder Testing** （针对Regular Alpha）和 **2-Year Testing** （针对Atom Alpha）是平台用于检测Alpha稳定性的重要工具。这些测试的核心目标是通过观察Alpha的PNL表现，评估其长期稳定性。这一过程类似于“望诊”，通过观察PNL的形状来判断Alpha的健康状况。

#### **PNL的理想形状**

最理想的PNL表现是一条从左下角到右上角的稳定直线。这种形状表明Alpha在长期内具有持续的盈利能力和较低的波动性，是稳定性和可靠性的最佳体现。

- **新人阶段的目标** ：
  对于新人来说，能够通过平台的IS Ladder Testing或2-Year Testing已经是一个不错的开始。这表明Alpha在基本稳定性方面达到了平台的最低要求。

#### **进阶要求**

在进阶阶段，可以通过以下标准来进一步评估Alpha的长期稳定性：

1. **过去10年的表现** ：
   - 在过去10年中，Alpha的Sharpe超过  **1**  的年份不少于  **X年** （具体标准可根据个人目标设定）。
2. **最近两年的表现** ：
   - 特别关注最近两年的PNL表现，尤其是  **2022年**  的表现。

### **为什么要有PPAC？低相关性与Portfolio的多样性**

在Alpha开发与提交的过程中，平台引入了  **PPAC**  的机制，这不仅是为了给新人提供一个更宽松的探索环境，更重要的是为了强调  **低相关性**  和  **Portfolio的多样性**  对整体表现的重要性。

#### **Portfolio的概念：你的军队**

为了更直观地理解Portfolio的意义，可以将它比喻为一支军队。以往的Alpha评估标准过度追求  **Sharpe**  和  **Fitness**  等单一指标，这就像你的军队里清一色都是身高体壮的步兵。虽然这些步兵看起来很强壮，但缺乏多样性会让你的军队在面对复杂战场时显得单薄。

要让你的军队更有战斗力，就需要补充更多的兵种，例如：

- **斥候** ：负责侦查，提供灵活性。
- **炮兵** ：提供远程打击能力。
- **后勤兵** ：确保资源供应，维持军队的稳定性。

同样的道理，Alpha的Portfolio也需要多样性。一个多样化的Portfolio可以更好地应对不同的市场环境（OS），从而提升整体的稳定性和表现。

Self Correlation是一个很直观指标，新人的时候0.7是平台的要求。PPAC的要求是Pool内0.5的要求。值得一提的是这里的SC会随着提交数量的变多而更难有低的表现

- 0.5-0.7 之间的sc是可以通过的标准
- 0.3-0.5 之间的sc已经是很不错的了，通常对portfolio有一些提升
- 0.3以下的sc通常是很低的了

### **经济学意义与OS表现：从Alpha描述开始**

在Alpha开发与提交过程中， **经济学意义**  是决定OS（Out-of-Sample）表现的关键因素之一。许多老师常常强调这一点，因为具有经济学意义的Alpha往往能够更好地适应不同的市场环境，展现出更强的稳定性和可靠性。

#### **写Description的重要性**

对于新人来说，写好Alpha的  **Description** （描述）是一个非常重要的环节。这不仅是对Alpha逻辑的总结，也是开发者学习和思考的过程。可以将Description视为自己的学习日记，通过记录Alpha的核心逻辑和设计思路，帮助自己更好地理解经济学意义。

### **总结**

Alpha的开发与提交是一项复杂的任务，既需要满足平台的最低要求，也需要从长期稳定性、Portfolio优化和经济学意义的角度进行深入思考。新人在实践中应避免过度依赖单一指标，重视数量与质量的平衡，关注整体Portfolio的表现，并通过写Description来梳理自己的思路和逻辑。希望这篇指南能够帮助新人更好地理解Alpha开发的核心原则，并逐步提升自己的能力。

**顾问 MS51256 (Rank 28) 的解答与建议**:
========================================================================================================================================================================
学到了，我提交的因子质量太差了，难怪我vf0.62
========================================================================================================================================================================


---

### 技术对话片段 53 (原帖: 【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的)
- **原帖链接**: [Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的.md
- **时间**: 6个月前

**提问/主帖背景 (XZ23611)**:
今天我们来聊聊顾问的名片指标也是GENIUS最重要的指标： **Combined Alpha Performance** 。无论你是刚入门的新人，还是已经提交了几百个 alpha 的“老手”，这个话题都值得你花点时间认真琢磨。因为理解它，不仅能帮你提升 alpha 的表现，还能让你少走很多弯路。

## **什么是 Combined Alpha Performance？**

先说说这个“Combined Alpha Performance”到底是什么。简单来说，它是一个用来衡量所有提交过的 alpha 和 super alpha 的整体表现的指标。它的计算方式很直接：把所有地区已经提交的 alpha 和 super alpha  **等权组合** ，然后看它们在 2023-2025 年（semi-OS）的表现，具体是 **费后表现。**

这就像是一个大锅饭——你提交的每一个 alpha 都是这锅饭里的一粒米，表现好的米会让这锅饭更香，而表现差的米则可能毁掉整锅饭的味道。所以， **Combined Alpha Performance**  不仅仅是一个数字，它实际上反映了你提交的 alpha 是否在整体上“靠谱”。

## **计算原理：从公式看本质**

Combined Alpha Performance 的计算公式其实很简单：
 **等权组合 + 手续费调整 + 2023-2025 年的费后表现** 。

换句话说，平台会把你提交的所有 alpha 和 super alpha 按等权组合起来，然后在 2023-2025 年的市场环境下模拟它们的表现，最后扣除手续费，得出一个费后的 Sharpe 值。

从这个公式里，我们可以提炼出三个提升表现的关键词：

```
分散、质量、手续费。
```

接下来，我们就从这三个关键词出发，聊聊如何一步步提升你的 Combined Alpha Performance。

## **关键词一：分散（Diversity)**

### **为什么分散很重要？**

分散的核心在于降低风险。就像投资一样，如果你把所有的钱都投在一个篮子里（比如一个地区、一个模板），一旦这个篮子表现不好，你的整体表现就会被拖累。而分散可以让你的 alpha 表现更加稳定，减少单一因素的影响。

### **如何做到分散？**

1. **地区分散** ：
   最容易做到的分散就是  **region 的分散** 。不同地区的市场环境、手续费、波动性都不一样，把 alpha 分散到多个地区，可以有效降低单一区域表现不佳的风险。
2. **降低同一地区的 SC（Self Correlation）** ：
   在同一个 region 下，尽量降低 alpha 之间的相关性（SC）。最直接的方法就是多用不同类型的模板和数据类别（category）。也就是多点塔（Pyramid）这里要注意一点：我们说的“点塔”是指  **主信号**  的多样性，而不是通过科技（技术优化）或者附带信号来实现的点塔。换句话说，真正的分散是从信号本身出发，而不是靠“修修补补”来实现。

### **总结**

分散是提升 Combined Alpha Performance 的第一步，也是最容易做到的一步。记住： **多地区、多模板、多数据类别** ，多中性化，尤其是风险中性化，让你的 alpha 表现更加稳健。

## **关键词二：质量**

### **质量比数量更重要**

不管是 Combined Alpha Performance 还是 VF(Value Factor），在不能兼顾的情况下， **质量永远比数量重要得多** 。一个质量差的 alpha 不仅不会给你的组合加分，反而会拖累整体表现。而且，质量差的 alpha 需要很多个高质量的 alpha 来弥补。

### **举个例子：一个负的 OS Sharpe 如何拖累组合表现？**

#### **假设场景**

我们有一个组合，资金规模为  **100 万美元** ，包含以下几个 alpha：

- **Alpha A** ：OS Sharpe = -1
- **Alpha B** ：OS Sharpe = +1
- **Alpha C** ：OS Sharpe = +1

这些 alpha 是等权分配资金的，也就是说每个 alpha 分配的资金为：
 **100 万 ÷ 3 = 33.33 万美元** 。

#### **计算组合表现**

1. **Alpha A 的影响** ：
   - Alpha A 的 OS Sharpe = -1，相当于这 33.33 万美元的资金在拖累组合表现。
2. **Alpha B 和 Alpha C 的贡献** ：
   - Alpha B 和 Alpha C 的 OS Sharpe = +1，它们的表现为组合提供了正收益。
3. **组合表现** ：
   - 由于等权组合的 Sharpe 是所有 alpha 的加权平均值，Alpha A 的负表现会显著拉低整体表现。
   - 结果是：即使有两个 OS Sharpe = +1 的 alpha，组合的 Sharpe 也只有  **0.33** ，远低于 +1。一个负的alpha 让原本+1的组合表现降低了-66%

#### **需要多少好的 alpha 来弥补？**

如果我们想让组合的 Sharpe ≥ +1，那么至少需要  **2 个 OS Sharpe = +1 的 alpha 来弥补 1 个 OS Sharpe = -1 的 alpha** 。
如果有 2 个 OS Sharpe = -1 的 alpha，则需要至少  **4 个 OS Sharpe = +1 的 alpha**  来弥补。

### **如何提升质量？**

1. **关注 alpha 的核心逻辑** ：
   一个 alpha 的质量，核心在于它的逻辑是否有意义。不要为了提交而提交，确保你的 alpha 有清晰的经济学或统计学依据。论坛内有很多其它顾问的内容，就不在此赘述
2. 巧用AI和MCP来帮助我们验证一个alpha是否有意义。在MCP样例中就有如何写出alpha description （验证是否合理）和 alpha performance improvement会让你受益匪浅

[使用MCP成功地将alpha优化成可提交状态的案例 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 使用MCP成功地将alpha优化成可提交状态的案例经验分享.md)

### **总结**

质量是 Combined Alpha Performance 的基石。在不能兼顾的情况下，不要盲目追求数量，专注于打磨高质量的 alpha。

## **关键词三：手续费**

### **手续费的影响**

我们在提交 alpha 时看到的 Sharpe，都是  **不计手续费**  的。但在 Combined Alpha Performance 和真实的市场交易中，手续费是必须考虑的。

如果一个 alpha 的 margin（利润空间）过低，那么在扣除手续费后，原本的正 Sharpe 可能会变成负的，或者大幅降低。

### **如何控制手续费？**

1. **关注 ASI** ：
   不同市场的手续费标准不同。通常来说：
   - **亚洲市场（ASI）** ：尽量保持在 15 以上，20以上为佳。
   - **其他地区** ：建议保持在 10 以上。
2. **优化交易频率** ：
   如果一个 alpha 的交易频率过高，手续费会显著增加。通过调整 decay 或者优化信号，可以有效降低交易频率，从而减少手续费。论坛内有其它帖子自行搜索
3. **避免低 margin 的 alpha** ：
   提交前，检查 alpha 的 margin。如果 margin 太低，即使 Sharpe 看起来不错，也可能在扣除手续费后变得毫无价值。

## **关于 Super Alpha（SA）：双刃剑的误区与正确使用**

### **误区：IS Sharpe 高的 SA 一定能提升表现**

很多人会觉得， **SA 的 IS Sharpe 高** ，所以它一定能在 OS 中表现得很好。但事实是， **IS 的表现和 OS 的表现没有直接关系** 。一个 IS Sharpe 高达 10 的 SA，在 OS 中可能会是负的表现。

### **风险：质量差的 RA 会让 SA 成为“双倍伤害”**

SA 是通过组合多个原始 alpha（RA）生成的。如果这些 RA 的质量本身就很差，那么 SA 的表现也不会好。正所谓  **“Garbage In, Garbage Out”** ，如果你用的是“垃圾”原材料，SA 只会把这些问题放大。

### **如何正确使用 SA？**

- **过滤掉 IQC 表现差的 RA** ：如果IQC的OS表现不好，组SA时候学会剔除 product_correlation > 0 的 RA，确保组合的分散性。
- **确保 RA 的质量** ：优先选择 OS 表现稳定且为正的 RA。
- **优化组合逻辑** ：降低相关性，分散风险，提升 SA 的稳定性。

## **结语：提升 Combined Alpha Performance 的核心思路**

总结一下，提升 Combined Alpha Performance 的核心在于三个关键词： **分散、质量、手续费** 。

- **分散** ：多地区、多模板、多数据类别，多风险中性化，降低风险。
- **质量** ：专注于高质量的 alpha，避免被低质量的 alpha 拖累。
- **手续费** ：优化交易频率，确保 ASI 达标，避免低 margin 的 alpha。

最后送给大家一句话： **“少即是多，精益求精。”**  希望这篇文章能对你有所启发，祝大家的 Combined Alpha Performance 节节高升！

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢科普

==================================================================

祝大家base多多，大家都是GM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

COMBINE2+

==================================================================


---

### 技术对话片段 54 (原帖: 【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的_35928620962839.md
- **时间**: 6个月前

**提问/主帖背景 (XZ23611)**:
今天我们来聊聊顾问的名片指标也是GENIUS最重要的指标： **Combined Alpha Performance** 。无论你是刚入门的新人，还是已经提交了几百个 alpha 的“老手”，这个话题都值得你花点时间认真琢磨。因为理解它，不仅能帮你提升 alpha 的表现，还能让你少走很多弯路。

## **什么是 Combined Alpha Performance？**

先说说这个“Combined Alpha Performance”到底是什么。简单来说，它是一个用来衡量所有提交过的 alpha 和 super alpha 的整体表现的指标。它的计算方式很直接：把所有地区已经提交的 alpha 和 super alpha  **等权组合** ，然后看它们在 2023-2025 年（semi-OS）的表现，具体是 **费后表现。**

这就像是一个大锅饭——你提交的每一个 alpha 都是这锅饭里的一粒米，表现好的米会让这锅饭更香，而表现差的米则可能毁掉整锅饭的味道。所以， **Combined Alpha Performance**  不仅仅是一个数字，它实际上反映了你提交的 alpha 是否在整体上“靠谱”。

## **计算原理：从公式看本质**

Combined Alpha Performance 的计算公式其实很简单：
 **等权组合 + 手续费调整 + 2023-2025 年的费后表现** 。

换句话说，平台会把你提交的所有 alpha 和 super alpha 按等权组合起来，然后在 2023-2025 年的市场环境下模拟它们的表现，最后扣除手续费，得出一个费后的 Sharpe 值。

从这个公式里，我们可以提炼出三个提升表现的关键词：

```
分散、质量、手续费。
```

接下来，我们就从这三个关键词出发，聊聊如何一步步提升你的 Combined Alpha Performance。

## **关键词一：分散（Diversity)**

### **为什么分散很重要？**

分散的核心在于降低风险。就像投资一样，如果你把所有的钱都投在一个篮子里（比如一个地区、一个模板），一旦这个篮子表现不好，你的整体表现就会被拖累。而分散可以让你的 alpha 表现更加稳定，减少单一因素的影响。

### **如何做到分散？**

1. **地区分散** ：
   最容易做到的分散就是  **region 的分散** 。不同地区的市场环境、手续费、波动性都不一样，把 alpha 分散到多个地区，可以有效降低单一区域表现不佳的风险。
2. **降低同一地区的 SC（Self Correlation）** ：
   在同一个 region 下，尽量降低 alpha 之间的相关性（SC）。最直接的方法就是多用不同类型的模板和数据类别（category）。也就是多点塔（Pyramid）这里要注意一点：我们说的“点塔”是指  **主信号**  的多样性，而不是通过科技（技术优化）或者附带信号来实现的点塔。换句话说，真正的分散是从信号本身出发，而不是靠“修修补补”来实现。

### **总结**

分散是提升 Combined Alpha Performance 的第一步，也是最容易做到的一步。记住： **多地区、多模板、多数据类别** ，多中性化，尤其是风险中性化，让你的 alpha 表现更加稳健。

## **关键词二：质量**

### **质量比数量更重要**

不管是 Combined Alpha Performance 还是 VF(Value Factor），在不能兼顾的情况下， **质量永远比数量重要得多** 。一个质量差的 alpha 不仅不会给你的组合加分，反而会拖累整体表现。而且，质量差的 alpha 需要很多个高质量的 alpha 来弥补。

### **举个例子：一个负的 OS Sharpe 如何拖累组合表现？**

#### **假设场景**

我们有一个组合，资金规模为  **100 万美元** ，包含以下几个 alpha：

- **Alpha A** ：OS Sharpe = -1
- **Alpha B** ：OS Sharpe = +1
- **Alpha C** ：OS Sharpe = +1

这些 alpha 是等权分配资金的，也就是说每个 alpha 分配的资金为：
 **100 万 ÷ 3 = 33.33 万美元** 。

#### **计算组合表现**

1. **Alpha A 的影响** ：
   - Alpha A 的 OS Sharpe = -1，相当于这 33.33 万美元的资金在拖累组合表现。
2. **Alpha B 和 Alpha C 的贡献** ：
   - Alpha B 和 Alpha C 的 OS Sharpe = +1，它们的表现为组合提供了正收益。
3. **组合表现** ：
   - 由于等权组合的 Sharpe 是所有 alpha 的加权平均值，Alpha A 的负表现会显著拉低整体表现。
   - 结果是：即使有两个 OS Sharpe = +1 的 alpha，组合的 Sharpe 也只有  **0.33** ，远低于 +1。一个负的alpha 让原本+1的组合表现降低了-66%

#### **需要多少好的 alpha 来弥补？**

如果我们想让组合的 Sharpe ≥ +1，那么至少需要  **2 个 OS Sharpe = +1 的 alpha 来弥补 1 个 OS Sharpe = -1 的 alpha** 。
如果有 2 个 OS Sharpe = -1 的 alpha，则需要至少  **4 个 OS Sharpe = +1 的 alpha**  来弥补。

### **如何提升质量？**

1. **关注 alpha 的核心逻辑** ：
   一个 alpha 的质量，核心在于它的逻辑是否有意义。不要为了提交而提交，确保你的 alpha 有清晰的经济学或统计学依据。论坛内有很多其它顾问的内容，就不在此赘述
2. 巧用AI和MCP来帮助我们验证一个alpha是否有意义。在MCP样例中就有如何写出alpha description （验证是否合理）和 alpha performance improvement会让你受益匪浅

[使用MCP成功地将alpha优化成可提交状态的案例 – WorldQuant BRAIN]([L2] 使用MCP成功地将alpha优化成可提交状态的案例经验分享_35587548741015.md)

### **总结**

质量是 Combined Alpha Performance 的基石。在不能兼顾的情况下，不要盲目追求数量，专注于打磨高质量的 alpha。

## **关键词三：手续费**

### **手续费的影响**

我们在提交 alpha 时看到的 Sharpe，都是  **不计手续费**  的。但在 Combined Alpha Performance 和真实的市场交易中，手续费是必须考虑的。

如果一个 alpha 的 margin（利润空间）过低，那么在扣除手续费后，原本的正 Sharpe 可能会变成负的，或者大幅降低。

### **如何控制手续费？**

1. **关注 ASI** ：
   不同市场的手续费标准不同。通常来说：
   - **亚洲市场（ASI）** ：尽量保持在 15 以上，20以上为佳。
   - **其他地区** ：建议保持在 10 以上。
2. **优化交易频率** ：
   如果一个 alpha 的交易频率过高，手续费会显著增加。通过调整 decay 或者优化信号，可以有效降低交易频率，从而减少手续费。论坛内有其它帖子自行搜索
3. **避免低 margin 的 alpha** ：
   提交前，检查 alpha 的 margin。如果 margin 太低，即使 Sharpe 看起来不错，也可能在扣除手续费后变得毫无价值。

## **关于 Super Alpha（SA）：双刃剑的误区与正确使用**

### **误区：IS Sharpe 高的 SA 一定能提升表现**

很多人会觉得， **SA 的 IS Sharpe 高** ，所以它一定能在 OS 中表现得很好。但事实是， **IS 的表现和 OS 的表现没有直接关系** 。一个 IS Sharpe 高达 10 的 SA，在 OS 中可能会是负的表现。

### **风险：质量差的 RA 会让 SA 成为“双倍伤害”**

SA 是通过组合多个原始 alpha（RA）生成的。如果这些 RA 的质量本身就很差，那么 SA 的表现也不会好。正所谓  **“Garbage In, Garbage Out”** ，如果你用的是“垃圾”原材料，SA 只会把这些问题放大。

### **如何正确使用 SA？**

- **过滤掉 IQC 表现差的 RA** ：如果IQC的OS表现不好，组SA时候学会剔除 product_correlation > 0 的 RA，确保组合的分散性。
- **确保 RA 的质量** ：优先选择 OS 表现稳定且为正的 RA。
- **优化组合逻辑** ：降低相关性，分散风险，提升 SA 的稳定性。

## **结语：提升 Combined Alpha Performance 的核心思路**

总结一下，提升 Combined Alpha Performance 的核心在于三个关键词： **分散、质量、手续费** 。

- **分散** ：多地区、多模板、多数据类别，多风险中性化，降低风险。
- **质量** ：专注于高质量的 alpha，避免被低质量的 alpha 拖累。
- **手续费** ：优化交易频率，确保 ASI 达标，避免低 margin 的 alpha。

最后送给大家一句话： **“少即是多，精益求精。”**  希望这篇文章能对你有所启发，祝大家的 Combined Alpha Performance 节节高升！

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢科普

==================================================================

祝大家base多多，大家都是GM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

COMBINE2+

==================================================================


---

### 技术对话片段 55 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了两个因子，收益在1.75刀  质量不是很高。其中两个都是USA的  今天交了两个比赛的因子看看收益情况。


---

### 技术对话片段 56 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
今天的basepayment是1.66  交了一个质量很一般


---

### 技术对话片段 57 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了一个GLB model 2.1倍  给了1.73刀。 感觉不是很高。


---

### 技术对话片段 58 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了 4个收入 3.1刀  感谢ppac


---

### 技术对话片段 59 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了四个 3.8刀  希望尽快更新vf   想体验一下30刀的感觉


---

### 技术对话片段 60 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了三个因子，base1.86  不算合格的优秀因子，希望以后可以更新一个高的vf 突破个位数的收入


---

### 技术对话片段 61 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢新的比赛 让我断粮得以结束，今天交了四个ASI 因子  明天看看收益
********************************************************************************
********************************************************************************
********************************************************************************


---

### 技术对话片段 62 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了4个因子 给了5刀  今天继续加油
=================================================================================================================================================================================================================================================================================================================================================================================================================================


---

### 技术对话片段 63 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
2025/04/15
昨天交了四个因子，今天收入为1.8刀
====================================================================================================================================================================================================================================================================================================================================================================================================================================


---

### 技术对话片段 64 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
2025/4.13   昨天交了四个ppac 收入2.6刀 继续努力！！！
===============================================================================================================================================================================================================================================================


---

### 技术对话片段 65 (原帖: 生成按日期统计的报告)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨天交了四个因子收入只有2.5刀，究其原因就是pc过高。
前天收入有5.7刀，原因就是前天交的self corr 和prod corr 都是0，而昨天提交的prod corr 有三个高于0.7.众所周知，prod corr 高了会对base有很大的影响，感觉会影响一半的base payment................
今天交了四个因子，仍然有3个 prod corr >0.7  
由于这个比赛 prod corr 的check  与提交后的check 不相同 这就导致 提交后的prod corr 是一个开盲盒的事情。
明天估计收入还是2刀左右
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 66 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
=======================================================================
昨日收益8.5刀

regular 5刀 super 3.5刀

vf0.6

最近好消息是combine os>1

有希望成为master

努力 加油！！！！
=================================================================================


---

### 技术对话片段 67 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
==========================================================================================================================================================================
昨日base收入足足有九刀，距离10刀 一步之遥=======================================================================================================================================================================================


---

### 技术对话片段 68 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
昨日只提交了一个sa  3.3刀的收益，最近ra没有产出，很难受
眼看着就要结束了 希望能够稳住排名  combine千万别崩
========================================================
=========================================================
===========================================================


---

### 技术对话片段 69 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
最近更新的vf，从0.93跌倒了 0.75

base腰斩，还是需要提升质量，最近回测数量下降，产出显著降低

=========================================================


---

### 技术对话片段 70 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([L2] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
============================================================

平平wu qi的一天，交了一个superalpha。拿到了5刀，两杯咖啡钱。

最近还是在tag ppa alpha。希望可以升高ppa combine

============================================================


---

### 技术对话片段 71 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
好久没写量化日记了

这个季度事情比较多

vf 提升到0.96了

朴实无华的没有啥进步

combine距离2还有一些差距

如何成为grandmaster  

还是太难了，
尽力而为吧

----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 72 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
----------------------------------------------------------------------------------------------------------------------------
9.22提交一个amr 1.8pyr的因子  给了60刀
简直不可思议！！！！！

此外sa目前给的钱太不稳定了 究竟是什么愿意

----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 73 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
----------------------------------------------------------------------------------------------------------------------------
9.23提交一个fitness大于5的因子  给了10刀
sa 收益腰斩
ra 大于0.5收益也会变少很多

----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 74 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 MS51256 (Rank 28) 的解答与建议**:
----------------------------------------------------------------------------------------------------------------------------
9.24

今天提交格外的慢

提交了一天只交上了一个sa

三5 收益40刀左右

----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 75 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【经验分享】如何从expert直升GM经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (JD62872)**:
我是25年7月拿到顾问资格的，一开始其实就很懵懂，对genius规则也不熟悉，9月初的时候才在论坛看到华子哥的插件，看了下排名，发现自己有希望冲击master，于是在9月开始重视六维，但是由于前期没重视社区分，导致去年三季度最终定级在expert。进入四季度后，我制定了四季度点塔以及六维的整体计划，并在执行的过程中根据进程实时进行微调，最终在四季度进入了gm的序列。

大家都知道，要在genius定级系统里拿到好的成绩，我们需要关注四个方面，分别是因子提交数量、点塔数、三个combine（现在是四个了）以及六维，我也就从这四个方面再加上我订立计划的方法等五个方面分享下我的一些经验。

（一）点塔


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> Analyst
> 10
> 26
> Broker
> Earnings
> Fundamental
> 11
> 15
> 13
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 23
> 19
> News
> Option
> Other
> 13
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


上图是我三季度的点塔图，我觉得也是我能够拿到gm评级的关键。我总结我的点塔策略就是两个字：“少”和“满”。“少”指的是我开的区域少，而“满”则是指我需要极限点塔。从图中可以看出，我只开了达成gm所需要的最小数量的地区，这就迫使我需要做到两点：（1）我需要在每个已开地区提交大量因子，因此这些因子会使我整体组合的稳定性变强；（2）我每个区域都需要极限点塔，因此会让我的多样性足够好。我觉得这两点可能是我最后能够稳住combine拿到gm的关键。

（二）因子提交数量


> [!NOTE] [图片 OCR 识别内容]
> Signals
> 394
> Reached Grandmaster
> 20
> 120
> 220


我在去年四季度总共提交了394个因子，在10月和11月几乎每天都是交满4个的，12月之后开始每天交2-3个因子。另外，我从11月开始交sa，基本也是每天提交。10月和11月我为了降低平均操作符数，交的绝大部分因子都是一阶因子，也基本都是ppa为主。

此外，分区域来看，我在每个区域提交的因子数量都比较多。我EUR区域提交的因子数超过200个，USA区域提交的因子数超过150个，GLB区域的提交量也超过120个，最少的是ASI，提交数量超过80个。我认为可能这个提交数量让我在这些地区的构筑的组合足够稳定，从而从整体上提高了我组合的鲁棒性。当然，因为提交的多，所以肯定会提交一些不好的因子，这直接导致我的vf一直不是很高，因此后续还需要在提交数量和提交质量之间找好平衡。

（三）Combine


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.03
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.09


上图是我1月定级的combine。说来也是幸运，我第一次combine上2就拿到了gm。但我在去年四季度的combine其实经历了一个非常大的起伏的，我10月的combine是1.56，但11月一下跌到0.9附近了，当时心凉了半截，也尝试找各种原因，但直到现在都没找到。好在随后公布的12月的combine回升到了1.89，这也让我松了一口气，开始重拾信心，最终在定级的时候达到了2。我回顾我成为顾问以后直到现在的combine，除了11月外，其他月份一直都是一个稳定上升的状态，我觉得这可能表明我一直以来的提交策略都是对的，保持对核心区域的深耕应该对我构建组合的combine提供了不小的帮助。

此外，除了我在每个地区交的数量相对多以外，我跑的数据集也足够多。我基本每两天就会更换一个数据集，这个习惯直到现在都在保持，我认为这会提高我因子的多样性，从结果来看这个策略可能也帮到我不少。

（四）六维


> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st, 2025
> December 31st, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 4.74
> 109
> 1.16
> Fields used
> Community activity
> Max simulation streak
> 300
> 27.3
> 256


上图是我上季度末的六维。我平常也会去学习下大佬们的六维，我觉得我的六维在一众大佬们当中是显得非常平庸的，但这个六维组合可能胜在平衡，就是没有哪个方面会非常差。从总结经验的角度来看，我觉得六维就好像高考，最好的当然是那种门门功课都非常优秀的同学（大佬们），但如果我们没法做到门门功课都优秀，那么我觉得要么就门门功课都能良好，要么就有几门功课特别优秀。当然我选择了门门功课都良好，所以拿到了还不错的结果。

（五）计划的订立及微调

我从中学时代开始就有定计划的习惯，我觉得定计划的好处是能够清晰的知道自己在做什么，哪怕在进行过程中遇到一些问题，也能比较从容的应对。且订立计划会让我对进度心里有数，不会太过于焦虑。具体到我每个季度的genius的计划，我会根据上个季度genius的排名情况，结合自己在上个季度的六维给自己制定一个能够做得到的到的计划。比如我在去年四季度初通过排名就计划在四季度将平均操作符控制在5以内，平均字段数控制在1.2以内，然后最大化利用可利用的操作符，总字段数达到350。从实行结果来看，除了总字段数，其他计划都基本顺利完成。当然，在执行的过程中我也会根据情况进行一些微调，比如进入12月之后，因为要开始限制回测量了，且我11月的combine掉到了0.9附近，这让我意识到我的质量可能不够，我就开始有意识的减少提交数量，增强因子的质量。进入2026年之后，总部对规则进行了大量的修改，因此我们也需要跟随总部的步伐来适应新的规则，但维持整体的计划，并坚定的执行，我认为还是对我们冲击更高级别的Genius会有很大的帮助的。

最后做个总结，我觉得我之所以四季度能拿到满意的结果，可能在这几个方面做的比较好，（1）只做自己熟悉和经过验证的区域，别贪多；（2）在数量和质量间找好平衡，要想拿到好的genius评级，还是需要提交足够数量的因子的；（3）一定做好多样性，逼自己交一些小数据集，点一些难点的小塔，可能会有意想不到的收获；（4）六维需要有策略的卷，要根据自己的情况制定对自己有利的计划。

希望我的这些微末经验能够给大家带来些帮助，同时也祝大家都能在新的赛季里获得好的结果！

**顾问 MS51256 (Rank 28) 的解答与建议**:
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 76 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【经验分享】如何从expert直升GM经验分享_38320422749463.md
- **时间**: 3个月前

**提问/主帖背景 (JD62872)**:
我是25年7月拿到顾问资格的，一开始其实就很懵懂，对genius规则也不熟悉，9月初的时候才在论坛看到华子哥的插件，看了下排名，发现自己有希望冲击master，于是在9月开始重视六维，但是由于前期没重视社区分，导致去年三季度最终定级在expert。进入四季度后，我制定了四季度点塔以及六维的整体计划，并在执行的过程中根据进程实时进行微调，最终在四季度进入了gm的序列。

大家都知道，要在genius定级系统里拿到好的成绩，我们需要关注四个方面，分别是因子提交数量、点塔数、三个combine（现在是四个了）以及六维，我也就从这四个方面再加上我订立计划的方法等五个方面分享下我的一些经验。

（一）点塔


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GLB
> EUR
> ASI
> Analyst
> 10
> 26
> Broker
> Earnings
> Fundamental
> 11
> 15
> 13
> Imbalance
> Insiders
> Institutions
> Macro
> Model
> 23
> 19
> News
> Option
> Other
> 13
> Price Volume
> Risk
> Sentiment
> Short Interest
> Social Media


上图是我三季度的点塔图，我觉得也是我能够拿到gm评级的关键。我总结我的点塔策略就是两个字：“少”和“满”。“少”指的是我开的区域少，而“满”则是指我需要极限点塔。从图中可以看出，我只开了达成gm所需要的最小数量的地区，这就迫使我需要做到两点：（1）我需要在每个已开地区提交大量因子，因此这些因子会使我整体组合的稳定性变强；（2）我每个区域都需要极限点塔，因此会让我的多样性足够好。我觉得这两点可能是我最后能够稳住combine拿到gm的关键。

（二）因子提交数量


> [!NOTE] [图片 OCR 识别内容]
> Signals
> 394
> Reached Grandmaster
> 20
> 120
> 220


我在去年四季度总共提交了394个因子，在10月和11月几乎每天都是交满4个的，12月之后开始每天交2-3个因子。另外，我从11月开始交sa，基本也是每天提交。10月和11月我为了降低平均操作符数，交的绝大部分因子都是一阶因子，也基本都是ppa为主。

此外，分区域来看，我在每个区域提交的因子数量都比较多。我EUR区域提交的因子数超过200个，USA区域提交的因子数超过150个，GLB区域的提交量也超过120个，最少的是ASI，提交数量超过80个。我认为可能这个提交数量让我在这些地区的构筑的组合足够稳定，从而从整体上提高了我组合的鲁棒性。当然，因为提交的多，所以肯定会提交一些不好的因子，这直接导致我的vf一直不是很高，因此后续还需要在提交数量和提交质量之间找好平衡。

（三）Combine


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.03
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> No matching Alphas, refreshed monthly
> Combined Power Pool Alpha Performance
> 2.09


上图是我1月定级的combine。说来也是幸运，我第一次combine上2就拿到了gm。但我在去年四季度的combine其实经历了一个非常大的起伏的，我10月的combine是1.56，但11月一下跌到0.9附近了，当时心凉了半截，也尝试找各种原因，但直到现在都没找到。好在随后公布的12月的combine回升到了1.89，这也让我松了一口气，开始重拾信心，最终在定级的时候达到了2。我回顾我成为顾问以后直到现在的combine，除了11月外，其他月份一直都是一个稳定上升的状态，我觉得这可能表明我一直以来的提交策略都是对的，保持对核心区域的深耕应该对我构建组合的combine提供了不小的帮助。

此外，除了我在每个地区交的数量相对多以外，我跑的数据集也足够多。我基本每两天就会更换一个数据集，这个习惯直到现在都在保持，我认为这会提高我因子的多样性，从结果来看这个策略可能也帮到我不少。

（四）六维


> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-04, October 1st, 2025
> December 31st, 2025
> Operators per Alpha
> Operators used
> Fields per Alpha
> 4.74
> 109
> 1.16
> Fields used
> Community activity
> Max simulation streak
> 300
> 27.3
> 256


上图是我上季度末的六维。我平常也会去学习下大佬们的六维，我觉得我的六维在一众大佬们当中是显得非常平庸的，但这个六维组合可能胜在平衡，就是没有哪个方面会非常差。从总结经验的角度来看，我觉得六维就好像高考，最好的当然是那种门门功课都非常优秀的同学（大佬们），但如果我们没法做到门门功课都优秀，那么我觉得要么就门门功课都能良好，要么就有几门功课特别优秀。当然我选择了门门功课都良好，所以拿到了还不错的结果。

（五）计划的订立及微调

我从中学时代开始就有定计划的习惯，我觉得定计划的好处是能够清晰的知道自己在做什么，哪怕在进行过程中遇到一些问题，也能比较从容的应对。且订立计划会让我对进度心里有数，不会太过于焦虑。具体到我每个季度的genius的计划，我会根据上个季度genius的排名情况，结合自己在上个季度的六维给自己制定一个能够做得到的到的计划。比如我在去年四季度初通过排名就计划在四季度将平均操作符控制在5以内，平均字段数控制在1.2以内，然后最大化利用可利用的操作符，总字段数达到350。从实行结果来看，除了总字段数，其他计划都基本顺利完成。当然，在执行的过程中我也会根据情况进行一些微调，比如进入12月之后，因为要开始限制回测量了，且我11月的combine掉到了0.9附近，这让我意识到我的质量可能不够，我就开始有意识的减少提交数量，增强因子的质量。进入2026年之后，总部对规则进行了大量的修改，因此我们也需要跟随总部的步伐来适应新的规则，但维持整体的计划，并坚定的执行，我认为还是对我们冲击更高级别的Genius会有很大的帮助的。

最后做个总结，我觉得我之所以四季度能拿到满意的结果，可能在这几个方面做的比较好，（1）只做自己熟悉和经过验证的区域，别贪多；（2）在数量和质量间找好平衡，要想拿到好的genius评级，还是需要提交足够数量的因子的；（3）一定做好多样性，逼自己交一些小数据集，点一些难点的小塔，可能会有意想不到的收获；（4）六维需要有策略的卷，要根据自己的情况制定对自己有利的计划。

希望我的这些微末经验能够给大家带来些帮助，同时也祝大家都能在新的赛季里获得好的结果！

**顾问 MS51256 (Rank 28) 的解答与建议**:
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 77 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，向优秀的大佬学习，我的combine只有2.1

#========= WORLDQUANT BRAIN CONSULTANT ========== #
#每天进步一点点，加油
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================加油每一天=======================#


---

### 技术对话片段 78 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享_38927243023383.md
- **时间**: 3个月前

**提问/主帖背景 (JR23144)**:
大家好

年前 kunqi 老师邀请我做个分享，说实话，过年期间走亲访友多喝了几杯，一直没腾出空来。今天终于坐在屏幕前，想着老生常谈的套路大家在论坛也看腻了，那我就分享一点我不一样的“打怪升级”经历和最近的 Alpha 巧思。

按照国际惯例，先上战绩镇楼：


> [!NOTE] [图片 OCR 识别内容]
> BRNR
> Ganius
> Awarded to
> on
> achieving
> EXPERT
> EXPERT Level
> 2025 Quarter 3
> LEVEL
> CERTIFICATE
> Authorized and presented by
> Nitish Maini
> Cnet stratsgy Othcer ot Wcrldcuant
> ESNSESLNWVS CXPERTGENUS EXPERTGENIUS EXPERT GENIUS



> [!NOTE] [图片 OCR 识别内容]
> BRAII
> Ganius
> Awarded to
> onachieving
> GRAND
> GRAND MASTER Level
> MASTER
> 2025 Quarter 4
> LEVEL
> CERTIFICATE
> Nuthorizedand presenteq by
> Nitish Maini
> Cet stratsgy Othcer ot Wcrldouant



> [!NOTE] [图片 OCR 识别内容]
> B人
> Ganius
> Awarded to
> On
> achieving
> GRAND
> GRAND MASTER Level
> MASTER
> 2026 Quarter
> LEVEL
> CERTIFICATE
> Authorizedand presented by
> Nitish Maini
> Cniaf Strategy Otticerot Worldouar


- **段位记录：**  一次Expert 两次定级 Grand Master
- **VF 更新记录：** 4-6月 0.5 ， 7月0.95， 8月0.92， 9月0.99， 10月0.97， 11月 0.85 12月 0.88 ,1月0.98 , 2月0.77
- **阶段性收益：**  在 Expert 阶段拿过 347 刀的季度奖，一次gm季度奖公布下来是8090刀。
- **日收益** ： 高的时候 一天100$,低的时候一天十几刀。
  
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 09/2912025
> Super:
> 55.25
> Regular;
> 5.76
> Total:
> 110.00999999999999
> May
> May
  
> [!NOTE] [图片 OCR 识别内容]
> Ill
> 02/15/2025
> Super:
> 7.27
> Regular:
> 3.80
> Total:
> 11.27

- **时间投入** ：每天投入大概3-4小时。

#### 1. 背景：一个退居18线小城的前大厂程序员

和很多金融、金工科班出身的大佬不同，我以前其实是个在互联网大厂里“拧螺丝”的程序员。后来为了更好的生活节奏，退居到了一个18线小城市。

小城市好是好，但想拿到一线城市的薪资水平并不容易。直到我接触了 WorldQuant BRAIN。它给我提供了一个绝佳的杠杆： **用纯粹的代码和逻辑，去对冲地理位置带来的劣势。**  从写业务代码到写因子，这中间虽然有壁垒，但大厂经历留给我的数据敏感度和抗压能力，是我能一路冲到 GM 的基本盘。

#### 2. 新形势下的心态：接受 VF 的“玄学”，拿稳能拿的钱

在论坛里，大家总喜欢看那些一路高歌猛进的完美剧本。但我今天想分享点真实的痛点。

不知道大家有没有同感： **每次要更新季度奖的时候，那个月的 VF 就不高。**  就像我现在的 0.77，说不心痛是假的。在新规和当下多变的市场形态下，一味地去死磕、焦虑这个波动，其实非常内耗。

我的策略是： **底线思维，稳吃保底。**  既然高 VF 有时候看天吃饭，那就在日常把基础的 Alpha 数量和质量打扎实。不要等到季度末才去突击，而是把力气匀在平时，保证即使在 VF 表现拉胯的月份，依然有 10几刀 这样的保底饭钱收益托底。心态稳了，回测的手才不会抖。

#### 3. 拒绝同质化：分享一个突破瓶颈的 Alpha 巧思

官方老师特意嘱咐我分享一点“不一样”的方法。那我就把我压箱底的一个小技巧拿出来： **特定场景下的冷门算子降维打击。**

大家在写因子或者用 AI 优化时，遇到 Vector（向量）数据，是不是下意识就敲  `vec_sum()`  或者  `vec_avg()` ？不可否认它们很好用，但在寻找极值信号时，它们会让你的 Alpha 变得平庸。

**我的巧思是：**  当你外层使用的是求极小的相关算子（如  `ts_min()` ,  `ts_arg_min()` ,  `group_min()` ）时，内层的向量处理一定要配合使用  **`vec_min()`** ；同理，外层是寻找极大值的逻辑时，内层配合  **`vec_max()`** 。

不要小看这一步替换。在我的单变量回测中，把原本的  `vec_sum()`  换成同向匹配的  `vec_min()` ， **Sharpe 直接从 1.73 跃升到了 1.81，Fitness 突破 1.05** 。这种底层逻辑的纯粹性，往往能帮你避开拥挤的赛道，拿到那些别人忽略的高质量信号。

#### 4. 写在最后

量化这条路，有时候很像我们古代历史里的王朝更迭（对，我平时挺喜欢研究三国，南北朝，唐宋明清历史的哈哈），有盛世也有低谷。重要的不是你一时冲得有多高，而是你能在这个牌桌上坐多久。

祝大家在新的一年里，都能找到属于自己的 Alpha 节奏，咱们一起在马年多赚钱，VF 早日重回巅峰！

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，就是靠着大佬的sa分享才能产出写质量不错的因子。

#========= WORLDQUANT BRAIN CONSULTANT ========== #
#每天进步一点点，加油
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================加油每一天=======================#


---

### 技术对话片段 79 (原帖: 【顾问进阶】一文读懂风险中心化，掌握使用方法)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXTPlUsyA6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAfpodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzU5NTQ1OTY4NTg5MDMtLSVFOSVBMSVCRSVFOSU5NyVBRSVFOCVCRiU5QiVFOSU5OCVCNi0lRTQlQjglODAlRTYlOTYlODclRTglQUYlQkIlRTYlODclODIlRTklQTMlOEUlRTklOTklQTklRTQlQjglQUQlRTUlQkYlODMlRTUlOEMlOTYtJUU2JThFJThDJUU2JThGJUExJUU0JUJEJUJGJUU3JTk0JUE4JUU2JTk2JUI5JUU2JUIzJTk1BjsIVDoOc2VhcmNoX2lkSSIpNmU4OTczZDgtMDg4YS00NTVhLWFhNzItMzgzNWZjNTcxYTliBjsIRjoJcmFua2kLOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMTVM1MTI1NgY7CFQ6EnJlc3VsdHNfY291bnRpLQ%3D%3D--f82996e5fa1f163cc69b0758eb8c67e0fd607518
- **时间**: 6个月前

**提问/主帖背景 (MH33574)**:
今天早上收到公告通知11月起，PowerPool将仅接受风险中性化的因子，顾问仍然可以使用其他的非风险中性化（MARKET, SECTOR, INDUSTRY, SUBINDUSTRY, COUNTRY) 回测，但只有符合RA标准的才可以提交。很多新顾问可能还不太熟悉风险中性化这个概念，希望这篇文章对你有帮助1. 什么是风险中性化？定义：“风口来了猪都可以飞上天”，风险中性化就是在去除已知的“风”。 风险中性化是一种通过消除特定风险因子对Alpha影响的技术，使Alpha的表现更加纯粹，专注于捕捉市场异常。通过风险中性化，可以剔除市场、行业或风格因子等已知风险对Alpha收益的干扰，从而更准确地评估Alpha的独立性和有效性。理论背景：风险因子是影响资产收益的主要驱动因素，例如市场风险、行业风险、动量因子等。经典理论：Fama-French三因子模型（市场、规模、价值）和套利定价理论（APT）为风险因子模型奠定了基础。2. 为什么要做风险中性化？消除已知风险因子的干扰：如果Alpha的收益完全由已知风险因子解释，则其价值有限，因为这些因子可以通过简单的模型复制。风险中性化可以帮助研究者专注于Alpha捕捉的独特市场异常。降低风险：减少因风险因子回撤或波动性导致的潜在损失。提高Alpha在不同市场条件下的稳健性。提升Alpha性能：通过剔除不必要的风险因子，提高Alpha的Sharpe比率，减少回撤，并优化换手率与交易成本之间的平衡。3. 风险中性化的好处更高的Alpha独立性：通过剔除风险因子，Alpha表现更独立，能够更好地反映其捕捉市场异常的能力。降低拥挤交易风险：减少因市场中大量投资者持有相似头寸而导致的价格剧烈波动。增强多样性：通过不同的风险中性化方法，生成多样化的信号，丰富Alpha池。优化长期表现：在保留Alpha收益的同时显著降低风险，提供更稳定、可靠的长期表现。4. 如何使用风险中性化？界面操作：在BRAIN平台的回测界面中，进入模拟设置（Simulation Settings），在Neutralization选项中选择对应的风险中性化方法，BRAIN平台内置了六种风险中性：FAST, SLOW, SLOW_AND_FAST, CROWDING, STATISTICAL, REVERSION_AND_MOMENTUM (RAM)API操作：在API中，通过调整代码中的neutralization参数实现。例如{"instrumentType": "EQUITY","region": "USA","universe": "TOP3000","delay": 1,"decay": 0,"neutralization": "FAST",  // 替换为上述对应的风险中性化方法"truncation": 0.1,"pasteurization": "ON","unitHandling": "VERIFY","nanHandling": "ON","language": "FASTEXPR","visualization": false}5. 不同的风险中性化方法及其使用场景以下是平台支持的六种风险中性化方法的详细介绍：5.1 FAST定义：快速因子（Fast Factors）包括市场和行业风格因子，和高换手率的风格因子，例如反转因子。适用场景：高换手率信号。需要捕捉短期市场趋势的Alpha。注意事项：使用FAST中性化可能会增加Alpha的换手率。5.2 SLOW定义：慢速因子（Slow Factors）包括低换手率的风格因子，例如价值因子。适用场景：低换手率信号。更关注长期趋势的Alpha。注意事项：SLOW因子适合稳健型投资策略。5.3 SLOW_AND_FAST定义：结合了慢速因子和快速因子的综合模型。适用场景：需要同时考虑短期和长期趋势的Alpha。适合多样化的投资策略。注意事项：可能会增加换手率，但能更全面地中性化风险。5.4 RAM（Reversion and Momentum）反转因子（REVERSION）：捕捉短期均值回归现象（如5天内的价格回调）。定义：市场通常会对短期事件过度反应，导致暂时性错误定价。随着这些市场效率的修正，超卖的股票价格恢复，超买的股票价格回落。短期反转因子捕捉股票价格的均值回归现象，即近期表现不佳的股票往往在未来获得更高的回报，而近期表现较好的股票可能会出现回调。动量因子（MOMENTUM）：捕捉长期价格趋势（如12个月内的价格趋势）。动量因子识别股票价格的持续趋势，即近期表现较好的股票往往继续上涨，而表现较差的股票则可能继续下跌。基于趋势跟随原则，已建立的价格趋势更可能延续而非逆转适用场景：需要对冲短期均值回归和长期动量趋势的Alpha。注意事项：RAM中性化适用于多空平衡的Alpha。建议结合Alpha的特性，评估其是否容易受到反转或动量因子的影响。5.5 CROWDING定义：拥挤风险中性化，控制因市场中大量投资者持有相似头寸而导致的风险。随着更多投资者进入相同的头寸，交易的盈利能力可能下降。虽然价格在初期可能上涨，但随后可能变得脆弱，容易出现大幅下跌。适用场景：需要减少拥挤交易风险的Alpha。当过多投资者同时试图卖出相同的头寸时，价格可能迅速下跌，导致更大的损失。适合在动量趋势强烈的市场中使用。注意事项：拥挤风险中性化适用于多空平衡的Alpha。需要结合Alpha的特性，评估其是否容易受到拥挤交易的影响。5.6 STATISTICAL定义：因子模型的两大类别：基本面因子模型（Fundamental Factor Models）和基于统计因子模型（Statistical Factor Models），其中第二种使用统计技术（如主成分分析PCA或聚类分析）分析证券收益，识别市场数据中的模式和关系。依赖历史收益数据，通过统计方法预测未来表现或优化投资组合风险。经典案例比如：Roll和Ross的《套利定价理论的实证研究》（APT），强调使用统计方法提取影响资产收益的多个因子。适用场景：捕捉复杂非线性关系的Alpha，生成在特定收益空间中表现良好的信号。注意事项：统计风险中性化依赖于历史数据，可能对数据质量较为敏感。建议结合Alpha的特性，评估其是否适合统计模型的应用。6. 总结风险中性化的核心价值：通过剔除已知风险因子，优化Alpha表现，降低风险。选择合适的方法：根据Alpha的特点（如换手率、风险敞口）选择合适的风险中性化方法。个人建议：在Simulation中先抽样一部分，尝试不同的风险中性化设置，评估其对Alpha表现的影响，选择最合适的再进行全量的回测英文原版文档阅读：Getting Started: Risk Neutralized Alphas | WorldQuant BRAINGetting Started with Risk Neutralized Metrics | WorldQuant BRAINGetting Started with Crowding Risk-Neutralized Alphas | WorldQuant BRAINGetting Started with Statistical Risk-Neutralized Alphas | WorldQuant BRAINGetting Started with RAM Risk-Neutralized Alphas | WorldQuant BRAIN

**顾问 MS51256 (Rank 28) 的解答与建议**:
===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================感谢大佬的科普，写的非常详细，选好neut 不仅可以有效的提升alpha 的表现还可以降低pc以获取更丰厚的base，此外中性化不应该集中于某几个，要多用多种不同的中性化，不能只会三板斧。================================Do your best ================================


---

### 技术对话片段 80 (原帖: 【顾问进阶】一文读懂风险中心化，掌握使用方法)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【顾问进阶】一文读懂风险中心化掌握使用方法_35954596858903.md
- **时间**: 6 months ago

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

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢大佬的科普，写的非常详细，选好neut 不仅可以有效的提升alpha 的表现还可以降低pc以获取更丰厚的base，此外中性化不应该集中于某几个，要多用多种不同的中性化，不能只会三板斧。

================================Do your best ================================**


---

### 技术对话片段 81 (原帖: 一件获取你各个地区的因子数量和因子平均表现（为combined计划做准备）经验分享)
- **原帖链接**: [Commented] 一件获取你各个地区的因子数量和因子平均表现为combined计划做准备经验分享.md
- **时间**: 6个月前

**提问/主帖背景 (XX42289)**:
注意：
记得自己写一个login函数，传回自己的session即可。

start_date="2024-01-01"可以改成自己成为有条件顾问的日期

在获取alpha的url中有type!=SUPER，这个是剔除了SUPER的

```
import pandas as pdimport requestsimport timeimport loggingfrom typing import List, Dict# 配置日志logging.basicConfig(    level=logging.INFO,    format="%(asctime)s - %(levelname)s - %(message)s")logger = logging.getLogger(__name__)def fetch_submitted_alphas(        session: requests.Session,        start_date: str,        end_date: str,        max_offset: int = 9900  # 最大偏移量限制) -> List[Dict]:    """    拉取指定日期范围内提交的Alpha信息（基于count自动分页）    参数:        session: 已登录的requests会话对象        start_date/end_date: 日期范围（格式：YYYY-MM-DD）        max_offset: 最大偏移量（防止无限循环）    返回:        符合条件的Alpha信息列表    """    alpha_list = []    offset = 0  # 起始偏移量    while True:        # 构建请求URL（恢复原始筛选条件，移除sharpe等额外筛选）        url = (            f"[链接已屏蔽]            "&status!=UNSUBMITTED%1FIS_FAIL"            f"&dateSubmitted%3E={start_date}T00:00:00-04:00"            f"&dateSubmitted%3C={end_date}T00:00:00-04:00"            "&order=-is.sharpe&hidden=false&type!=SUPER"        )        # 发送请求        response = session.get(url)        try:            logger.info(f"当前偏移量: {offset}")            # 解析响应数据            response_data = response.json()            total_count = response_data.get("count", 0)            logger.info(f"符合条件的总数量: {total_count}")            # 提取当前页结果            if "results" in response_data:                alpha_list.extend(response_data["results"])                logger.info(f"累计获取: {len(alpha_list)} 条Alpha")            # 判断终止条件：偏移量超过总数或达到最大限制            offset += 100            if offset >= total_count or offset > max_offset:                logger.info("分页拉取完成")                break            # 避免请求过于频繁            time.sleep(1)        except Exception as e:            logger.error(f"拉取失败: {str(e)}")            # 回退偏移量并重试            offset -= 100            logger.info("等待10秒后重试...")            time.sleep(10)            # 重新登录获取会话            session = login()            # 确保偏移量不为负            if offset < 0:                offset = 0    return alpha_listdef calculate_region_statistics(alpha_records: List[Dict]) -> pd.DataFrame:    """按地区统计Alpha的关键指标"""    analysis_data = []    for alpha in alpha_records:        # 提取地区信息        region = alpha.get("settings", {}).get("region", "UNKNOWN")        # 提取IS指标        is_metrics = alpha.get("is", {})        analysis_data.append({            "region": region,            "is_sharpe": is_metrics.get("sharpe"),            "is_fitness": is_metrics.get("fitness"),            "is_margin": is_metrics.get("margin")        })    # 分组统计    alpha_df = pd.DataFrame(analysis_data)    return alpha_df.groupby("region").agg(        alpha_count=("region", "count"),        avg_is_sharpe=("is_sharpe", "mean"),        avg_is_fitness=("is_fitness", "mean"),        avg_is_margin=("is_margin", "mean")    ).reset_index()def main():    # 登录获取会话    logger.info("开始登录...")    session = login()    if not session:        logger.error("登录失败，无法继续")        return    # 拉取Alpha数据（使用原始日期范围）    logger.info("开始拉取Alpha信息...")    alphas = fetch_submitted_alphas(        session=session,        start_date="2024-01-01",        end_date="2099-11-01"    )    logger.info(f"拉取完成，共获取 {len(alphas)} 条Alpha信息")    # 统计并展示结果    if alphas:        stats = calculate_region_statistics(alphas)        logger.info("\n===== 各地区Alpha统计结果 =====")        print(stats.to_string(index=False))    else:        logger.info("未获取到任何Alpha信息，无法统计")if __name__ == "__main__":    main()
```

**顾问 MS51256 (Rank 28) 的解答与建议**:
[YC62305](/hc/en-us/profiles/28856294144279-YC62305)  官方给的machine lib中有封装，参考一下就可以了。

**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢课代表的分享，课代表的每一次分享都是极为重要的工具，感谢，已安利

================================Do your best ================================**


---

### 技术对话片段 82 (原帖: 一件获取你各个地区的因子数量和因子平均表现（为combined计划做准备）经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一件获取你各个地区的因子数量和因子平均表现为combined计划做准备经验分享_35930680060695.md
- **时间**: 6个月前

**提问/主帖背景 (XX42289)**:
注意：
记得自己写一个login函数，传回自己的session即可。

start_date="2024-01-01"可以改成自己成为有条件顾问的日期

在获取alpha的url中有type!=SUPER，这个是剔除了SUPER的

```
import pandas as pdimport requestsimport timeimport loggingfrom typing import List, Dict# 配置日志logging.basicConfig(    level=logging.INFO,    format="%(asctime)s - %(levelname)s - %(message)s")logger = logging.getLogger(__name__)def fetch_submitted_alphas(        session: requests.Session,        start_date: str,        end_date: str,        max_offset: int = 9900  # 最大偏移量限制) -> List[Dict]:    """    拉取指定日期范围内提交的Alpha信息（基于count自动分页）    参数:        session: 已登录的requests会话对象        start_date/end_date: 日期范围（格式：YYYY-MM-DD）        max_offset: 最大偏移量（防止无限循环）    返回:        符合条件的Alpha信息列表    """    alpha_list = []    offset = 0  # 起始偏移量    while True:        # 构建请求URL（恢复原始筛选条件，移除sharpe等额外筛选）        url = (            f"[链接已屏蔽]            "&status!=UNSUBMITTED%1FIS_FAIL"            f"&dateSubmitted%3E={start_date}T00:00:00-04:00"            f"&dateSubmitted%3C={end_date}T00:00:00-04:00"            "&order=-is.sharpe&hidden=false&type!=SUPER"        )        # 发送请求        response = session.get(url)        try:            logger.info(f"当前偏移量: {offset}")            # 解析响应数据            response_data = response.json()            total_count = response_data.get("count", 0)            logger.info(f"符合条件的总数量: {total_count}")            # 提取当前页结果            if "results" in response_data:                alpha_list.extend(response_data["results"])                logger.info(f"累计获取: {len(alpha_list)} 条Alpha")            # 判断终止条件：偏移量超过总数或达到最大限制            offset += 100            if offset >= total_count or offset > max_offset:                logger.info("分页拉取完成")                break            # 避免请求过于频繁            time.sleep(1)        except Exception as e:            logger.error(f"拉取失败: {str(e)}")            # 回退偏移量并重试            offset -= 100            logger.info("等待10秒后重试...")            time.sleep(10)            # 重新登录获取会话            session = login()            # 确保偏移量不为负            if offset < 0:                offset = 0    return alpha_listdef calculate_region_statistics(alpha_records: List[Dict]) -> pd.DataFrame:    """按地区统计Alpha的关键指标"""    analysis_data = []    for alpha in alpha_records:        # 提取地区信息        region = alpha.get("settings", {}).get("region", "UNKNOWN")        # 提取IS指标        is_metrics = alpha.get("is", {})        analysis_data.append({            "region": region,            "is_sharpe": is_metrics.get("sharpe"),            "is_fitness": is_metrics.get("fitness"),            "is_margin": is_metrics.get("margin")        })    # 分组统计    alpha_df = pd.DataFrame(analysis_data)    return alpha_df.groupby("region").agg(        alpha_count=("region", "count"),        avg_is_sharpe=("is_sharpe", "mean"),        avg_is_fitness=("is_fitness", "mean"),        avg_is_margin=("is_margin", "mean")    ).reset_index()def main():    # 登录获取会话    logger.info("开始登录...")    session = login()    if not session:        logger.error("登录失败，无法继续")        return    # 拉取Alpha数据（使用原始日期范围）    logger.info("开始拉取Alpha信息...")    alphas = fetch_submitted_alphas(        session=session,        start_date="2024-01-01",        end_date="2099-11-01"    )    logger.info(f"拉取完成，共获取 {len(alphas)} 条Alpha信息")    # 统计并展示结果    if alphas:        stats = calculate_region_statistics(alphas)        logger.info("\n===== 各地区Alpha统计结果 =====")        print(stats.to_string(index=False))    else:        logger.info("未获取到任何Alpha信息，无法统计")if __name__ == "__main__":    main()
```

**顾问 MS51256 (Rank 28) 的解答与建议**:
[YC62305](/hc/en-us/profiles/28856294144279-YC62305)  官方给的machine lib中有封装，参考一下就可以了。

**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢课代表的分享，课代表的每一次分享都是极为重要的工具，感谢，已安利

================================Do your best ================================**


---

### 技术对话片段 83 (原帖: sharpe：用于筛选进入下一阶段的最低要求)
- **原帖链接**: [Commented] 一文解锁手机自动化回测 从此随时随地想跑就跑---基于QPython安卓--附代码.md
- **时间**: 9个月前

**提问/主帖背景 (RJ74200)**:
大部分人都会选择云服务器来进行批量回测,如果觉得云服务器贵or前期懒得配置云服务器，更或者假期出去游玩没办法登录云服务器来操作，或许手机端批量自动化回测是一个不错的选择.

服务器可看作是一个高配置的电脑主机,而手机则可以是低配的电脑主机,对于回测使用的内存/硬盘/网络带宽完全足够.我选择的时QPYTHON，应用无广告，可开多个py文件进程。


> [!NOTE] [图片 OCR 识别内容]
> 20:56
> ()
> #
> 0N & ail HD
> 50
> 口
> u
> 终端
> Notebook
> 编辑器
> u
> 文件
> 扩展
> 设置
> 社区
> 课程


启动流程: 手机应用商店下载Qpython ,点击进入APP -> 中间选择扩展 -> 选择AIPY ->往下滑动点击Pandas包安装.也可以在扩展界面选择PIP客户端进入手动下载一些pip库,但是支持的没那么多.（基础配置就弄好啦。）->.py文件，选择以QPYTHON打开，点击下面的运行符号。等待即可

如何查看手机文件的主目录: 点击文件夹最上面的默认分区.我的是/storage/emulated/0/,当文件存储在其他路径时,可能有权限问题,需要让QPython拥有更多权限,一般在手机设置中.由于json写入其他目录不对问题，所以我把状态文件Qpython的文件夹中

最后附上自动化回测代码，支持自动跑一二三N阶，支持断点续测，可扩展性强，但是函数比较少，可以自己多多添加。应该是支持顾问阶段和用户阶段的，可能需要自己稍微调一下确保代码没问题（有个缺点就是无法拉取超过10000的回测量，之前的手机摔坏了，所以没用这套代码了，下个版本还没调好，有机会再分享）。

单槽回测/用户阶段记得更改：if len(arr) == 10为if len(arr) == 1。max_post为最大槽位数量，用户阶段需要改为3。

字段分词以两个空格来分词，所以传入的表达式不要使用两个空格连在一起。

主函数如下：第一个为文件名称, 以.csv结尾。列名为code

flow("news18-EUR-1-TOP2500-m2-df", region="EUR", universe="TOP2500",delay=1, neu="FAST")

其他组合函数命名：ff：代表不做组合，ts_first->对应一阶，group_second->对应二阶，when_third->对应三阶。 完全支持各种顺序组合，更改funcs = [ff, ts_first, group_second, when_third,][:]的顺序或者删减即可。

代码如下：

import requests, logging, os, sys, re

from logging.handlers import RotatingFileHandler

import json

from requests.auth import HTTPBasicAuth

import pandas as pd

from time import sleep

import datetime

import pytz

import logging

class quant:

def __init__(self, data_name: str) -> None:

self.arr = []

self.count = 0

self.path = "/storage/emulated/0/qua/" if sys.platform == "linux"\

else "C:\Project\qua\"

self.path += data_name.split("-")[0]+"/"

os.makedirs(self.path, exist_ok=True)

self.data_name =self.path+data_name

self.log_name = self.path+data_name+'-log.txt'

self.case_name = self.data_name+"-case.json"

self.case_df = self.data_name+"-df.json"

self.result_df = self.data_name+"-result.csv"

self.sess = requests.Session()

self.save_file: StopIteration = None

def login(self,):

# 用户名和密码文件brain.txt格式: ["username", "password"]

with open(self.path + '../brain.txt') as f:

self.username, self.password = json.load(f)

self.sess.auth = HTTPBasicAuth(self.username, self.password)

response = self.sess.post(' [[链接已屏蔽]) ')

print(response)

def save_result(self, alpha_num, s_time) -> pd.DataFrame:

# 2025-07-04T22:52:30

arr = []

print(alpha_num, s_time)

for i in range(0, alpha_num+100, 100):

print(i)

url = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + s_time  \

+ "-04:00"

print(url)

response = self.sess.get(url)

print(response)

alpha_list = response.json()["results"]

print

if len(alpha_list)==0:

return pd.DataFrame(arr)

for alphas_p in alpha_list:

result = dict()

result["id"] = alphas_p["id"]

result["code"] = alphas_p["regular"]["code"]

result["result"] = "FAIL" if  [i.get("name") for i in alphas_p["is"]["checks"] if i.get("result") == "FAIL"] else "PASS"

LOW_SUB_UNIVERSE_SHARPE = [i for i in alphas_p["is"]["checks"] if i["name"] == "LOW_SUB_UNIVERSE_SHARPE"][0]

result["sub"]=LOW_SUB_UNIVERSE_SHARPE.get("value", -2)-LOW_SUB_UNIVERSE_SHARPE.get("limit", 2)

CONCENTRATED_WEIGHT: dict = [i for i in alphas_p["is"]["checks"] if i["name"] == "CONCENTRATED_WEIGHT"][0]

result["weight"] = CONCENTRATED_WEIGHT.get("limit", 0) - CONCENTRATED_WEIGHT.get("value", 0)

aplha_is:dict = alphas_p["is"]

delete =  ["startDate", "checks", "bookSize"]

for ite in delete:

del aplha_is[ite]

# del

result.update(aplha_is)

result["settings"] = alphas_p["settings"]

arr.append(result)

return pd.DataFrame(arr)

def submit_simulations(self, index,  alpha_list, max_post=3):

if self.count % 80 == 0:

self.sess.close()

self.login()

self.count +=1

if  alpha_list:

print(alpha_list[0])

if len(alpha_list)==0:

alpha_list =alpha_list[0]

for _ in range(20):

try:

sim1 = None

sim1 = self.sess.post(' [[链接已屏蔽]) ', json=alpha_list,)

location = sim1.headers['Location'].split("/")[-1]

break

except  Exception as e:

print(e, index, sim1)

sleep(10)

if _ == 19:

cfg.log(f"post ERROR: {index}")

return

self.arr.append((index, location))

self.save_status(index)

try:

print(self.arr)

while len(self.arr) >= max_post:

for index, ip in self.arr:

url = " [[链接已屏蔽]) " + ip

sim_progress_resp = self.sess.get(url)

retry_after_sec = sim_progress_resp.headers.get("Retry-After", 0)

if retry_after_sec == 0:  # simulation done!模拟完成!

if (index, ip) in self.arr:

self.arr.remove((index, ip)) #删除对应的值

children = sim_progress_resp.json().get("children")  # 获取alpha id

status1 = sim_progress_resp.json().get("status")

if status1 == "ERROR":

cfg.log(f"status ERROR: {index} {ip}" )

print(index, status1, children)

sleep(0.1)

else:

sleep(0.25)

except Exception as e:

cfg.log(e)

print(e)

cfg.log(f"no location [{index}], sleep for 10 seconds and try next alpha.没有位置，睡10秒然后尝试下一个字母。”")

sleep(10)

def save_status(self, index):

cfg.status["case"] = index

cfg.log(str(cfg.status))

with open(self.case_name, "w") as f:

f.write(json.dumps(cfg.status))

def sims(self, df: pd.DataFrame, start: int=0, max_post: int=8):

print(len(df.index))

arr= []

start = cfg.status.get("case",-1)

i = 0

start+=1

for i, index in enumerate(df.index[start:], start=start):

alpha_s =  {

"type": "REGULAR",

"settings": df.loc[index]["settings"],

"regular": df.loc[index]["code"] }

arr.append(alpha_s)

# 每个槽位的数量,用户阶段需要设置为1

if len(arr) == 10:

print(arr[0])

cfg.log(f"index is: {index}")

cfg.qua.submit_simulations(index, arr, max_post=max_post)

arr = []

cfg.qua.submit_simulations(index, arr, max_post=max_post)

cfg.qua.submit_simulations(i, [], max_post=1)

def deal_data(self, df: pd.DataFrame,sharpe: float=0.9,n: int=1, save_file:str=""):

# 变更sharpe和fitness，按照原始表达式分组。按照fitness+sharpe排序取前n。

for a in df.index:

if df.loc[a]["sharpe"] <0:

df.iat[a]["code"] = "-"+df.loc[a]["code"]

df = df[df["longCount"]+df["shortCount"]>4]

df["total"] = abs(df["fitness"] + df["sharpe"])

df["exp"] = df["code"].apply(lambda x: x.split("  ")[1] if "  " in x else x)

df["op"] = df["code"].apply(lambda x: x.split("(")[1] if "(" in x else x)

df.sort_values(by="total", inplace=True,ascending=False)

df.to_csv(self.save_file +".csv")

df = df[(abs(df["sharpe"])>=sharpe) | (abs(df["fitness"]) >= 1)]

df = df.groupby(["exp", "op"]).head(n)

df = df[["code", "settings"]]

df.to_json(self.case_df)

cfg.status = {}

return df

#原始序列

def ff(df :pd.DataFrame):

return df

# ts序列

def ts_first(df: pd.DataFrame, days:list = [5, 22, 66, 252]) ->pd.DataFrame:

ts_ops = ["ts_rank", "ts_zscore", "ts_delta",  "ts_sum", "ts_delay",

"ts_std_dev", "ts_mean",  "ts_arg_min", "ts_arg_max","ts_scale", "ts_quantile"]

arr = []

for i in df.index:

for op in ts_ops:

for day in days:

arr.append({"code": f'{op}({df.loc[i]["code"]}, {day})',

"settings": df.loc[i]["settings"]})

return pd.DataFrame(arr)

def group_second(df: pd.DataFrame,):

groups=["group_rank", "group_zscore", "group_scale", "group_neutralize"]

gps = ["industry", "subindustry"]

if df.loc[df.index[0], "settings"]["region"] in ["GLB", "EUR","ASI"]:

gps += ["group_cartesian_product(country, industry)",

"group_cartesian_product(country, subindustry)"]

arr = []

for i in df.index:

for op in groups:

for gp in gps:

arr.append({"code": f'{op}({df.loc[i]["code"]}, {gp})',

"settings": df.loc[i]["settings"]})

return pd.DataFrame(arr)

def when_third(df:pd.DataFrame,) ->pd.DataFrame:

open_events = ['group_rank(ts_std_dev(returns,60),sector)>0.7',

'ts_mean(volume,5)>ts_mean(volume,60)',

'ts_zscore(returns,60)>2',

'ts_std_dev(returns, 5)>ts_std_dev(returns, 20)',

'returns<0.09',

'ts_corr(close,volume,5)>0',

'ts_corr(close,volume,5)<0',

'returns>-0.09',

"abs(returns)<0.10"]

# open_events=["rank(rp_css_business)>0.8","ts_rank(rp_css_business,22)>0.8",

# "rank(vec_avg(nws3_scores_posnormscr))>0.8",

# "ts_rank(vec_avg(nws3_scores_posnormscr),22)>0.8",]

arr=  []

for i in df.index:

for op in open_events:

arr.append({"code":f'{op}? {df.loc[i]["code"]}:-1',

"settings": df.loc[i]["settings"]})

return pd.DataFrame(arr)

def cases(func, df, sharpe=1.4, max_post=7, s_time=""):

cfg.qua.save_file = cfg.qua.data_name + f"-{func.__name__}.csv"

arrs = func(df)

if not cfg.status.get("time"):

now = datetime.datetime.now(pytz.timezone('America/New_York'))

s_time =  now.isoformat().split(".")[0]

cfg.status["time"] = s_time

cfg.status["func"] = func.__name__

print(cfg.status)

cfg.qua.sims(arrs, start=0,max_post=max_post)

df: pd.DataFrame = cfg.qua.save_result(len(arrs), cfg.status.get("time"))

df = cfg.qua.deal_data(df, sharpe=sharpe,)

return df

def log(name,):

logger = logging.getLogger(name)

formater = logging.Formatter( "[%(asctime)s] %(message)s", '%Y-%m-%d %H:%M:%S' )

logger.setLevel(logging.DEBUG)

# if not show:

file_log = logging.FileHandler(name, )

file_log.setFormatter(formater)

logger.addHandler(file_log)

ch = logging.StreamHandler()

ch.setFormatter(formater)

logger.addHandler(ch)

return logger

class cfg:

qua: quant = None

status = {}

log = None

def flow(data_name, settings: dict= {}, region= "USA",universe="TOP3000", delay=1,neu="SUBINDUSTRY" ):

cfg.qua = quant(data_name)

cfg.log = log(cfg.qua.log_name).info

# 加载原始文件

df = pd.read_csv(cfg.qua.data_name+".csv")

# 状态

if os.path.exists(cfg.qua.case_name):

with open(cfg.qua.case_name, "r") as f:

cfg.status = json.load(f)

# 存在中间过程文件

if os.path.exists(cfg.qua.case_df):

df = pd.read_json(cfg.qua.case_df)

if "settings" not in df.columns:

df["code"] = "  " + df["code"] + "  "

settings = {

"instrumentType": "EQUITY",

"region": region,

"universe": universe,

"delay": delay,

"decay": 0,

"neutralization": neu,

"truncation": 0.08,

"pasteurization": "ON",

"unitHandling": "VERIFY",

"nanHandling": "ON",

"language": "FASTEXPR",

"visualization": False }

df = df.to_dict()

df["settings"] ={i:settings for i in list(df["code"].keys())}

df = pd.DataFrame(df)

print("status: ", cfg.status)

cfg.qua.login()

funcs = [ff, ts_first, group_second, when_third,][:] #

for i, func  in enumerate(funcs):

if cfg.status.get("func") and cfg.status.get("func")!= func.__name__:

continue

# sharpe：用于筛选进入下一阶段的最低要求

df = cases(func, df, sharpe=0.7+i*0.2, max_post=8)

df: pd.DataFrame = None

for i in os.listdir(cfg.qua.path):

if data_name +"-df"  in i:

continue

if data_name +".csv" in i:

dft = pd.read_csv(cfg.qua.path+i)

df = pd.concat([df, dft])

df.to_csv(cfg.qua.data_name+"-all.csv")

flow("news18-EUR-1-TOP2500-m2-df", region="EUR", universe="TOP2500",delay=1, neu="SUBINDUSTRY")

**顾问 MS51256 (Rank 28) 的解答与建议**:
----------------------------------------------------------------------------------------------------------------------------

牛逼，想问一下ios可以吗  
还是只能安卓？
----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 84 (原帖: sharpe：用于筛选进入下一阶段的最低要求)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一文解锁手机自动化回测 从此随时随地想跑就跑---基于QPython安卓--附代码_35081418033047.md
- **时间**: 9个月前

**提问/主帖背景 (RJ74200)**:
大部分人都会选择云服务器来进行批量回测,如果觉得云服务器贵or前期懒得配置云服务器，更或者假期出去游玩没办法登录云服务器来操作，或许手机端批量自动化回测是一个不错的选择.

服务器可看作是一个高配置的电脑主机,而手机则可以是低配的电脑主机,对于回测使用的内存/硬盘/网络带宽完全足够.我选择的时QPYTHON，应用无广告，可开多个py文件进程。


> [!NOTE] [图片 OCR 识别内容]
> 20:56
> ()
> #
> 0N & ail HD
> 50
> 口
> u
> 终端
> Notebook
> 编辑器
> u
> 文件
> 扩展
> 设置
> 社区
> 课程


启动流程: 手机应用商店下载Qpython ,点击进入APP -> 中间选择扩展 -> 选择AIPY ->往下滑动点击Pandas包安装.也可以在扩展界面选择PIP客户端进入手动下载一些pip库,但是支持的没那么多.（基础配置就弄好啦。）->.py文件，选择以QPYTHON打开，点击下面的运行符号。等待即可

如何查看手机文件的主目录: 点击文件夹最上面的默认分区.我的是/storage/emulated/0/,当文件存储在其他路径时,可能有权限问题,需要让QPython拥有更多权限,一般在手机设置中.由于json写入其他目录不对问题，所以我把状态文件Qpython的文件夹中

最后附上自动化回测代码，支持自动跑一二三N阶，支持断点续测，可扩展性强，但是函数比较少，可以自己多多添加。应该是支持顾问阶段和用户阶段的，可能需要自己稍微调一下确保代码没问题（有个缺点就是无法拉取超过10000的回测量，之前的手机摔坏了，所以没用这套代码了，下个版本还没调好，有机会再分享）。

单槽回测/用户阶段记得更改：if len(arr) == 10为if len(arr) == 1。max_post为最大槽位数量，用户阶段需要改为3。

字段分词以两个空格来分词，所以传入的表达式不要使用两个空格连在一起。

主函数如下：第一个为文件名称, 以.csv结尾。列名为code

flow("news18-EUR-1-TOP2500-m2-df", region="EUR", universe="TOP2500",delay=1, neu="FAST")

其他组合函数命名：ff：代表不做组合，ts_first->对应一阶，group_second->对应二阶，when_third->对应三阶。 完全支持各种顺序组合，更改funcs = [ff, ts_first, group_second, when_third,][:]的顺序或者删减即可。

代码如下：

import requests, logging, os, sys, re

from logging.handlers import RotatingFileHandler

import json

from requests.auth import HTTPBasicAuth

import pandas as pd

from time import sleep

import datetime

import pytz

import logging

class quant:

def __init__(self, data_name: str) -> None:

self.arr = []

self.count = 0

self.path = "/storage/emulated/0/qua/" if sys.platform == "linux"\

else "C:\Project\qua\"

self.path += data_name.split("-")[0]+"/"

os.makedirs(self.path, exist_ok=True)

self.data_name =self.path+data_name

self.log_name = self.path+data_name+'-log.txt'

self.case_name = self.data_name+"-case.json"

self.case_df = self.data_name+"-df.json"

self.result_df = self.data_name+"-result.csv"

self.sess = requests.Session()

self.save_file: StopIteration = None

def login(self,):

# 用户名和密码文件brain.txt格式: ["username", "password"]

with open(self.path + '../brain.txt') as f:

self.username, self.password = json.load(f)

self.sess.auth = HTTPBasicAuth(self.username, self.password)

response = self.sess.post(' [[链接已屏蔽]) ')

print(response)

def save_result(self, alpha_num, s_time) -> pd.DataFrame:

# 2025-07-04T22:52:30

arr = []

print(alpha_num, s_time)

for i in range(0, alpha_num+100, 100):

print(i)

url = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + s_time  \

+ "-04:00"

print(url)

response = self.sess.get(url)

print(response)

alpha_list = response.json()["results"]

print

if len(alpha_list)==0:

return pd.DataFrame(arr)

for alphas_p in alpha_list:

result = dict()

result["id"] = alphas_p["id"]

result["code"] = alphas_p["regular"]["code"]

result["result"] = "FAIL" if  [i.get("name") for i in alphas_p["is"]["checks"] if i.get("result") == "FAIL"] else "PASS"

LOW_SUB_UNIVERSE_SHARPE = [i for i in alphas_p["is"]["checks"] if i["name"] == "LOW_SUB_UNIVERSE_SHARPE"][0]

result["sub"]=LOW_SUB_UNIVERSE_SHARPE.get("value", -2)-LOW_SUB_UNIVERSE_SHARPE.get("limit", 2)

CONCENTRATED_WEIGHT: dict = [i for i in alphas_p["is"]["checks"] if i["name"] == "CONCENTRATED_WEIGHT"][0]

result["weight"] = CONCENTRATED_WEIGHT.get("limit", 0) - CONCENTRATED_WEIGHT.get("value", 0)

aplha_is:dict = alphas_p["is"]

delete =  ["startDate", "checks", "bookSize"]

for ite in delete:

del aplha_is[ite]

# del

result.update(aplha_is)

result["settings"] = alphas_p["settings"]

arr.append(result)

return pd.DataFrame(arr)

def submit_simulations(self, index,  alpha_list, max_post=3):

if self.count % 80 == 0:

self.sess.close()

self.login()

self.count +=1

if  alpha_list:

print(alpha_list[0])

if len(alpha_list)==0:

alpha_list =alpha_list[0]

for _ in range(20):

try:

sim1 = None

sim1 = self.sess.post(' [[链接已屏蔽]) ', json=alpha_list,)

location = sim1.headers['Location'].split("/")[-1]

break

except  Exception as e:

print(e, index, sim1)

sleep(10)

if _ == 19:

cfg.log(f"post ERROR: {index}")

return

self.arr.append((index, location))

self.save_status(index)

try:

print(self.arr)

while len(self.arr) >= max_post:

for index, ip in self.arr:

url = " [[链接已屏蔽]) " + ip

sim_progress_resp = self.sess.get(url)

retry_after_sec = sim_progress_resp.headers.get("Retry-After", 0)

if retry_after_sec == 0:  # simulation done!模拟完成!

if (index, ip) in self.arr:

self.arr.remove((index, ip)) #删除对应的值

children = sim_progress_resp.json().get("children")  # 获取alpha id

status1 = sim_progress_resp.json().get("status")

if status1 == "ERROR":

cfg.log(f"status ERROR: {index} {ip}" )

print(index, status1, children)

sleep(0.1)

else:

sleep(0.25)

except Exception as e:

cfg.log(e)

print(e)

cfg.log(f"no location [{index}], sleep for 10 seconds and try next alpha.没有位置，睡10秒然后尝试下一个字母。”")

sleep(10)

def save_status(self, index):

cfg.status["case"] = index

cfg.log(str(cfg.status))

with open(self.case_name, "w") as f:

f.write(json.dumps(cfg.status))

def sims(self, df: pd.DataFrame, start: int=0, max_post: int=8):

print(len(df.index))

arr= []

start = cfg.status.get("case",-1)

i = 0

start+=1

for i, index in enumerate(df.index[start:], start=start):

alpha_s =  {

"type": "REGULAR",

"settings": df.loc[index]["settings"],

"regular": df.loc[index]["code"] }

arr.append(alpha_s)

# 每个槽位的数量,用户阶段需要设置为1

if len(arr) == 10:

print(arr[0])

cfg.log(f"index is: {index}")

cfg.qua.submit_simulations(index, arr, max_post=max_post)

arr = []

cfg.qua.submit_simulations(index, arr, max_post=max_post)

cfg.qua.submit_simulations(i, [], max_post=1)

def deal_data(self, df: pd.DataFrame,sharpe: float=0.9,n: int=1, save_file:str=""):

# 变更sharpe和fitness，按照原始表达式分组。按照fitness+sharpe排序取前n。

for a in df.index:

if df.loc[a]["sharpe"] <0:

df.iat[a]["code"] = "-"+df.loc[a]["code"]

df = df[df["longCount"]+df["shortCount"]>4]

df["total"] = abs(df["fitness"] + df["sharpe"])

df["exp"] = df["code"].apply(lambda x: x.split("  ")[1] if "  " in x else x)

df["op"] = df["code"].apply(lambda x: x.split("(")[1] if "(" in x else x)

df.sort_values(by="total", inplace=True,ascending=False)

df.to_csv(self.save_file +".csv")

df = df[(abs(df["sharpe"])>=sharpe) | (abs(df["fitness"]) >= 1)]

df = df.groupby(["exp", "op"]).head(n)

df = df[["code", "settings"]]

df.to_json(self.case_df)

cfg.status = {}

return df

#原始序列

def ff(df :pd.DataFrame):

return df

# ts序列

def ts_first(df: pd.DataFrame, days:list = [5, 22, 66, 252]) ->pd.DataFrame:

ts_ops = ["ts_rank", "ts_zscore", "ts_delta",  "ts_sum", "ts_delay",

"ts_std_dev", "ts_mean",  "ts_arg_min", "ts_arg_max","ts_scale", "ts_quantile"]

arr = []

for i in df.index:

for op in ts_ops:

for day in days:

arr.append({"code": f'{op}({df.loc[i]["code"]}, {day})',

"settings": df.loc[i]["settings"]})

return pd.DataFrame(arr)

def group_second(df: pd.DataFrame,):

groups=["group_rank", "group_zscore", "group_scale", "group_neutralize"]

gps = ["industry", "subindustry"]

if df.loc[df.index[0], "settings"]["region"] in ["GLB", "EUR","ASI"]:

gps += ["group_cartesian_product(country, industry)",

"group_cartesian_product(country, subindustry)"]

arr = []

for i in df.index:

for op in groups:

for gp in gps:

arr.append({"code": f'{op}({df.loc[i]["code"]}, {gp})',

"settings": df.loc[i]["settings"]})

return pd.DataFrame(arr)

def when_third(df:pd.DataFrame,) ->pd.DataFrame:

open_events = ['group_rank(ts_std_dev(returns,60),sector)>0.7',

'ts_mean(volume,5)>ts_mean(volume,60)',

'ts_zscore(returns,60)>2',

'ts_std_dev(returns, 5)>ts_std_dev(returns, 20)',

'returns<0.09',

'ts_corr(close,volume,5)>0',

'ts_corr(close,volume,5)<0',

'returns>-0.09',

"abs(returns)<0.10"]

# open_events=["rank(rp_css_business)>0.8","ts_rank(rp_css_business,22)>0.8",

# "rank(vec_avg(nws3_scores_posnormscr))>0.8",

# "ts_rank(vec_avg(nws3_scores_posnormscr),22)>0.8",]

arr=  []

for i in df.index:

for op in open_events:

arr.append({"code":f'{op}? {df.loc[i]["code"]}:-1',

"settings": df.loc[i]["settings"]})

return pd.DataFrame(arr)

def cases(func, df, sharpe=1.4, max_post=7, s_time=""):

cfg.qua.save_file = cfg.qua.data_name + f"-{func.__name__}.csv"

arrs = func(df)

if not cfg.status.get("time"):

now = datetime.datetime.now(pytz.timezone('America/New_York'))

s_time =  now.isoformat().split(".")[0]

cfg.status["time"] = s_time

cfg.status["func"] = func.__name__

print(cfg.status)

cfg.qua.sims(arrs, start=0,max_post=max_post)

df: pd.DataFrame = cfg.qua.save_result(len(arrs), cfg.status.get("time"))

df = cfg.qua.deal_data(df, sharpe=sharpe,)

return df

def log(name,):

logger = logging.getLogger(name)

formater = logging.Formatter( "[%(asctime)s] %(message)s", '%Y-%m-%d %H:%M:%S' )

logger.setLevel(logging.DEBUG)

# if not show:

file_log = logging.FileHandler(name, )

file_log.setFormatter(formater)

logger.addHandler(file_log)

ch = logging.StreamHandler()

ch.setFormatter(formater)

logger.addHandler(ch)

return logger

class cfg:

qua: quant = None

status = {}

log = None

def flow(data_name, settings: dict= {}, region= "USA",universe="TOP3000", delay=1,neu="SUBINDUSTRY" ):

cfg.qua = quant(data_name)

cfg.log = log(cfg.qua.log_name).info

# 加载原始文件

df = pd.read_csv(cfg.qua.data_name+".csv")

# 状态

if os.path.exists(cfg.qua.case_name):

with open(cfg.qua.case_name, "r") as f:

cfg.status = json.load(f)

# 存在中间过程文件

if os.path.exists(cfg.qua.case_df):

df = pd.read_json(cfg.qua.case_df)

if "settings" not in df.columns:

df["code"] = "  " + df["code"] + "  "

settings = {

"instrumentType": "EQUITY",

"region": region,

"universe": universe,

"delay": delay,

"decay": 0,

"neutralization": neu,

"truncation": 0.08,

"pasteurization": "ON",

"unitHandling": "VERIFY",

"nanHandling": "ON",

"language": "FASTEXPR",

"visualization": False }

df = df.to_dict()

df["settings"] ={i:settings for i in list(df["code"].keys())}

df = pd.DataFrame(df)

print("status: ", cfg.status)

cfg.qua.login()

funcs = [ff, ts_first, group_second, when_third,][:] #

for i, func  in enumerate(funcs):

if cfg.status.get("func") and cfg.status.get("func")!= func.__name__:

continue

# sharpe：用于筛选进入下一阶段的最低要求

df = cases(func, df, sharpe=0.7+i*0.2, max_post=8)

df: pd.DataFrame = None

for i in os.listdir(cfg.qua.path):

if data_name +"-df"  in i:

continue

if data_name +".csv" in i:

dft = pd.read_csv(cfg.qua.path+i)

df = pd.concat([df, dft])

df.to_csv(cfg.qua.data_name+"-all.csv")

flow("news18-EUR-1-TOP2500-m2-df", region="EUR", universe="TOP2500",delay=1, neu="SUBINDUSTRY")

**顾问 MS51256 (Rank 28) 的解答与建议**:
----------------------------------------------------------------------------------------------------------------------------

牛逼，想问一下ios可以吗  
还是只能安卓？
----------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 85 (原帖: 一键检验alpha稳定性代码优化)
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


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢顾问 JL71699 (Rank 64)大佬的分享，这个功能对我来说非常使用，一键检验Alpha 的稳定性，大大简化了手工微调的测试流程。本来我需要再网页上微调好几次，不同的中性化。这个自动抢占线程真的很实用！！！！手工和代码去抢线程不仅累还等待时间久。通过输入alphaid，自动获取信息、修改设置并发送模拟请求，还能爬取数据绘制PnL图表，功能强大且高效。
楼主开源代码方便大家学习和优化，对我们这些业余量化研究者来说是个难得的好工具，期待更多功能更新！
此外祝愿大佬，Base不断新高，Grandmaster一直保持。


---

### 技术对话片段 86 (原帖: 一键检验alpha稳定性代码优化)
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


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢顾问 JL71699 (Rank 64)大佬的分享，这个功能对我来说非常使用，一键检验Alpha 的稳定性，大大简化了手工微调的测试流程。本来我需要再网页上微调好几次，不同的中性化。这个自动抢占线程真的很实用！！！！手工和代码去抢线程不仅累还等待时间久。通过输入alphaid，自动获取信息、修改设置并发送模拟请求，还能爬取数据绘制PnL图表，功能强大且高效。
楼主开源代码方便大家学习和优化，对我们这些业余量化研究者来说是个难得的好工具，期待更多功能更新！
此外祝愿大佬，Base不断新高，Grandmaster一直保持。


---

### 技术对话片段 87 (原帖: 从新手到研究顾问的历程分享)
- **原帖链接**: [Commented] 从新手到研究顾问的历程分享.md
- **时间**: 1年前

**提问/主帖背景 (YH25030)**:
去年12月底，一个很偶然的机会，看到微信朋友圈发WQ的兼职顾问的广告。因为自学过一些python的基础知识，所以就抱着好奇心和自我挑战的心态，注册了Brain平台的账号。1月初开始参加培训，尝试提交因子。1月底拿到Gold后，收到顾问邀请，并很快就填写了申请。最终在经历了漫长的等待后，在3月中旬成为了有条件顾问。

以下是给新手的一点点个人建议。

1. 仔细听基础课。因为对Brain平台，操作符，数据特征等等知识点的理解和掌握有很大帮助。
2. 多看中文论坛的帖子。前人的经验十分宝贵，可以避免自己走很多弯路。比如填写申请表信息，一定要看仔细，否则很容易填错。还有，论坛里面的alpha灵感等帖子，对自己写模板有非常大的启发，建议阅读收藏。
3. 在学习小组里多多交流。有些问题自己无法在平台上找到答案，可以尝试问问同学，大家一起解决。比如一些代码的设置等等。
4. 最后关于云处理器的设置。华为的弹性云服务器可以免费用一个月，新手可以不妨一试。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢宝贵的经验分享，祝您base多多


---

### 技术对话片段 88 (原帖: 从新手到研究顾问的历程分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 从新手到研究顾问的历程分享_31531182229911.md
- **时间**: 1年前

**提问/主帖背景 (YH25030)**:
去年12月底，一个很偶然的机会，看到微信朋友圈发WQ的兼职顾问的广告。因为自学过一些python的基础知识，所以就抱着好奇心和自我挑战的心态，注册了Brain平台的账号。1月初开始参加培训，尝试提交因子。1月底拿到Gold后，收到顾问邀请，并很快就填写了申请。最终在经历了漫长的等待后，在3月中旬成为了有条件顾问。

以下是给新手的一点点个人建议。

1. 仔细听基础课。因为对Brain平台，操作符，数据特征等等知识点的理解和掌握有很大帮助。
2. 多看中文论坛的帖子。前人的经验十分宝贵，可以避免自己走很多弯路。比如填写申请表信息，一定要看仔细，否则很容易填错。还有，论坛里面的alpha灵感等帖子，对自己写模板有非常大的启发，建议阅读收藏。
3. 在学习小组里多多交流。有些问题自己无法在平台上找到答案，可以尝试问问同学，大家一起解决。比如一些代码的设置等等。
4. 最后关于云处理器的设置。华为的弹性云服务器可以免费用一个月，新手可以不妨一试。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢宝贵的经验分享，祝您base多多


---

### 技术对话片段 89 (原帖: 优化Sub-universe Sharpe的一个方法经验分享)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXM9c3zCA6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAZ5odHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzYwNjE0ODIyNjc0MTUtJUU0JUJDJTk4JUU1JThDJTk2U3ViLXVuaXZlcnNlLVNoYXJwZSVFNyU5QSU4NCVFNCVCOCU4MCVFNCVCOCVBQSVFNiU5NiVCOSVFNiVCMyU5NQY7CFQ6DnNlYXJjaF9pZEkiKTZlODk3M2Q4LTA4OGEtNDU1YS1hYTcyLTM4MzVmYzU3MWE5YgY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKemgtY24GOwhUOgpxdWVyeUkiDE1TNTEyNTYGOwhUOhJyZXN1bHRzX2NvdW50aS0%3D--f216692bb286111b46d34b58860b0a915d9c892f
- **时间**: 6个月前

**提问/主帖背景 (WX96180)**:
我们在回测完去筛选Alpha的过程中经常会遇到明明Sharpe、fitness等指标都很不错，但偏偏Sub-universe Sharpe筑起了一道不可逾越的鸿沟，关上了提交的大门。那么如何对其进行优化，使得其成为可以提交的Alpha，今天和大家分享一个方法。论坛上已经有很多小伙伴对于Sub-universe Sharpe是什么给出了详尽的解释，这里不多做赘述，仅分享我自己的经历。首先，是在流动性不那么高的市场上simulate同样的alpha，很多时候alpha会直接没有信号，这种现象说明什么呢？推测可能并不是TOP3000中流动性不高的股票起到主要作用，可能是这个alpha做了较多的TOP1000 ~ TOP3000的股票，所以对应的方法是将低市值的股票排除出去，可以用if_else函数和rank(cap)来实现这个结果。例如，if_else(rank(cap) > 0.3, alpha, 0)然而，实践中发现，虽然不在有Sub-universe Sharpe of xx is below cutoff of xx的报错，但Sharpe和fitness会大大降低，可见这些小市值股票也起到一定的作用，那么如何改进这一情况呢？考虑到Sub-universe Sharpe是衡量流动性小的次级股票池的盈利能力，那么我们可以通过找一些衡量流动性的指标并结合市值联合筛选，比如现金比率就可以用于衡量企业流动性，那么公式可以变成：if_else(and(rank(mdl219_1_cashratio) < 0.9, rank(cap) > 0.15), alpha, 0)。小伙伴们也可以考虑其他的衡量流动性的指标。通过这两个约束条件，我成功实践，将一个原来不能提交的alpha变成达到标准的alpha，但同时我也有疑惑，这样是否会过拟合呢？评论区欢迎大佬进行评价。

**顾问 MS51256 (Rank 28) 的解答与建议**:
===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================感谢分享，LV21122说的非常有道理，如果参数的设置缺乏合理性，那os的爆炸是极为可能的，不过调好一个因子用来点塔是非常可以的。================================Do your best ================================


---

### 技术对话片段 90 (原帖: 优化Sub-universe Sharpe的一个方法经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 优化Sub-universe Sharpe的一个方法经验分享_36061482267415.md
- **时间**: 6个月前

**提问/主帖背景 (WX96180)**:
我们在回测完去筛选Alpha的过程中经常会遇到明明Sharpe、fitness等指标都很不错，但偏偏Sub-universe Sharpe筑起了一道不可逾越的鸿沟，关上了提交的大门。那么如何对其进行优化，使得其成为可以提交的Alpha，今天和大家分享一个方法。

论坛上已经有很多小伙伴对于Sub-universe Sharpe是什么给出了详尽的解释，这里不多做赘述，仅分享我自己的经历。

首先，是在流动性不那么高的市场上simulate同样的alpha，很多时候alpha会直接没有信号，这种现象说明什么呢？推测可能并不是TOP3000中流动性不高的股票起到主要作用，可能是这个alpha做了较多的TOP1000 ~ TOP3000的股票，所以对应的方法是将低市值的股票排除出去，可以用if_else函数和rank(cap)来实现这个结果。

例如，if_else(rank(cap) > 0.3, alpha, 0)

然而，实践中发现，虽然不在有Sub-universe Sharpe of xx is below cutoff of xx的报错，但Sharpe和fitness会大大降低，可见这些小市值股票也起到一定的作用，那么如何改进这一情况呢？考虑到Sub-universe Sharpe是衡量流动性小的次级股票池的盈利能力，那么我们可以通过找一些衡量流动性的指标并结合市值联合筛选，比如现金比率就可以用于衡量企业流动性，那么公式可以变成：

if_else(and(rank(mdl219_1_cashratio) < 0.9, rank(cap) > 0.15), alpha, 0)。

小伙伴们也可以考虑其他的衡量流动性的指标。

通过这两个约束条件，我成功实践，将一个原来不能提交的alpha变成达到标准的alpha，但同时我也有疑惑，这样是否会过拟合呢？评论区欢迎大佬进行评价。

**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢分享， [LV21122](/hc/en-us/profiles/34339142150551-LV21122) 说的非常有道理，如果参数的设置缺乏合理性，那os的爆炸是极为可能的，不过调好一个因子用来点塔是非常可以的。

================================Do your best ================================**


---

### 技术对话片段 91 (原帖: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享)
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
倍受启发，目前vf0.5，genius gold。向毛老师学习。


---

### 技术对话片段 92 (原帖: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享)
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
倍受启发，目前vf0.5，genius gold。向毛老师学习。


---

### 技术对话片段 93 (原帖: 使用VSCODE中的通义灵码自建免费MCP)
- **原帖链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwiXJWqQTSE6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcFodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzY2MTcwMTkwNzM5NDMtJUU0JUJEJUJGJUU3JTk0JUE4VlNDT0RFJUU0JUI4JUFEJUU3JTlBJTg0JUU5JTgwJTlBJUU0JUI5JTg5JUU3JTgxJUI1JUU3JUEwJTgxJUU4JTg3JUFBJUU1JUJCJUJBJUU1JTg1JThEJUU4JUI0JUI5TUNQBjsIVDoOc2VhcmNoX2lkSSIpMjA3MmRmMWQtOTg0Ny00NzE5LWFkMWQtYWE0NDcyZGVlNTQ4BjsIRjoJcmFua2kOOgtsb2NhbGVJIgp6aC1jbgY7CFQ6CnF1ZXJ5SSIMTVM1MTI1NgY7CFQ6EnJlc3VsdHNfY291bnRpLQ%3D%3D--93ededbed1ff4425a77411620faf815463a19264
- **时间**: 6个月前

**提问/主帖背景 (WY85693)**:
论坛里面大家讨论的都很多，但是还是会踩各种各样的坑。这次我来手把手教大家怎么在VSCODE中利用阿里的通义灵码建一个免费的MCP。首先下载安装VSCODE；在插件市场安装通义灵码；安装大佬们编写好的mcp库。pip install cnhkmcp 。此时需要你明确清楚的知道你的cnhkmcp安装的位置，后面需要导入脚本。如果不知道，可以直接在通义灵码当中询问，【我安装的cnhkmcp的位置在哪？】打开通义灵码的个人设置（要登陆）。在右上角点击新增MCP-配置文件添加 。这里coomand是写你当前执行python的运行位置。(版本要在3.11以上)。args是你刚刚安装cnhkmcp包位置中的platform_functions.py。description是这个mcp的一个简单描述，用于分辨，怎么写都行。"WorldQuant BRAIN Platform Mcp Server - Comprehensive trading platform integration with simulation managementalpha operations, and authentication. Credentials are stored inuser config.json in the same directory. Provides tools for creatingsimulations, checking status, managing alphas, and accessing platform features."配置好了之后，在相同位置的user_config.json中，写入你的brain平台的账号密码。所有内容配置好了之后，有个测试，点击测试，在所有步骤正确的情况下，就可以查看大佬们写的mcp工具了。最后希望大家都能装好自己的MCP。:D

**顾问 MS51256 (Rank 28) 的解答与建议**:
===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================感谢大佬的分享，mcp不断在不同的平台不同的ai中应用，在可预见的未来国区的因子质量将会被ai显著提升，期待每一位顾问的分享，期待国区再创佳绩。================================Do your best ================================


---

### 技术对话片段 94 (原帖: 使用VSCODE中的通义灵码自建免费MCP)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 使用VSCODE中的通义灵码自建免费MCP_36617019073943.md
- **时间**: 6个月前

**提问/主帖背景 (WY85693)**:
论坛里面大家讨论的都很多，但是还是会踩各种各样的坑。这次我来手把手教大家怎么在VSCODE中利用阿里的通义灵码建一个免费的MCP。

1. 首先下载安装VSCODE；
2. 在插件市场安装通义灵码； 
> [!NOTE] [图片 OCR 识别内容]
> Lingma
> Alibaba Cloud AI Coding Assistant
> V2.5.17
> Alibaba-Cloud
> 1,953.396
> 太大大太太(132]
> Type Less; Code More
> :用
> 即载
> 功能
> 更改8志

3. 安装大佬们编写好的mcp库。pip install cnhkmcp 。此时需要你明确清楚的知道你的cnhkmcp安装的位置，后面需要导入脚本。如果不知道，可以直接在通义灵码当中询问，【我安装的cnhkmcp的位置在哪？】
4. 打开通义灵码的个人设置（要登陆）。 
> [!NOTE] [图片 OCR 识别内容]
> @ R
> 智能会话
> 个人设置
> 个人设置
> 『邀出
> 基础信息
> 9人
> 账号
> 版本
> 个人版
> 改进计划
> 改进计划
> 记忆管理
> 1
> 记忆是自动从使用通!灵码的过程中不断积累的
> 可以帮助通义灵码更好坳和'互
> 它贯穿于你和通义灵码的对话中
> 并且随着时间旒逝。也能够让通义灵码越来越
> 懂你。
> 条记忆
> MCP 眼务
> MCP 是通V灵码扩展新工具的
> 种方式。可以查看帮助文档
> 解更多。
> 服务己连接
> 规则
> 规则可以帮助通义灵码更了解当前工程中的规则。
> 查看帮助文档获取更多使用示例
> 条规则

5. 在右上角点击新增MCP-配置文件添加 。这里coomand是写你当前执行python的运行位置。(版本要在3.11以上)。args是你刚刚安装cnhkmcp包位置中的platform_functions.py。description是这个mcp的一个简单描述，用于分辨，怎么写都行。
   "WorldQuant BRAIN Platform Mcp Server - Comprehensive trading platform integration with simulation managementalpha operations, and authentication. Credentials are stored inuser config.json in the same directory. Provides tools for creatingsimulations, checking status, managing alphas, and accessing platform features."
   
> [!NOTE] [图片 OCR 识别内容]
> Lib
> site-packages
> cnhkmcp
> untracked
> 在 untracked 中搜索
> @
> N #序 
> 三  查
> 详绍岸
> 二称
> 修改日期
> 奖型
> 天小
> Pycache
> 2025/11/2617:23
> 文件奕
> APP
> 2025/11/2616:58
> 文件奕
> mcp文件论坛版2_如果原版启动不了浏览器就试这个
> 2025/11/2616:58
> 文件奕
> aryiv_apipy
> 2025/11/2616:53
> Pthon 源文件
> arXiv_API_Toon
> Manualmd
> 2025/11/2616:58
> Markdown 源文件
> 14K3
> forum_functions:py
> 2025/11/2616:53
> Pthon 源文件
> 42<3
> platform_functions;py
> 2025/11/2617:28
> Pthon 源文件
> 119K3
> sample_mCP_configjson
> 2025/11/2616:58
> JSON 源文件
> 2C3
> User_configjson
> 这今so则是仵需要输2些骚鹎的位訾三
> 源文件
> 配置前运行我_安$必要农赖包 py
> 2025/11/2616:58
> Pthon 源文件
> 示例参考文栏 BRAINAlpha_Test_Requirements_
> Tipsimd
> 2025/11/2616:58
> Markdown 源文件
> 17 KB
> 示例工怍流 Alpha_explaination_workflow.md
> 2025/11/2616:53
> Markdown 源文件
> 5 K3
> 示例工怍流 BRAIN_
> Tips_Datafield_Exploration_Guidemd
> 2025/11/2616:58
> Markdown 源文件
> 示例工怍流 BRAIN_Alpha_Improvement_Workflow.md
> 2025/11/2616:53
> Markdown 源文件
> 5 K3
> 示例工怅流 daily_report_workflow.md
> 2025/11/2616:58
> Markdown 源文件
> 10K3
> 示例工作流_Dataset_Exploration_Expert_Manualmd
> 2025/11/2616:58
> Markdown 源文件
> 24<3
> snd
  
> [!NOTE] [图片 OCR 识别内容]
> Users
> lingma
> lingma_mcpjson
> mcpServers
> worldquant-brain-platform"
> Command"
> "C: /Users/
> AppData/ Local /Programs /Python/Python3l2/python.exe
> args
> C: /Users /
> {AppData / Local /Programs /Python /Python312/Lib/site-packages / cnhkmcp /untracked /platform_functions
> description"
> "WorldQuant BRAIN Platform Mcp Server
> Comprehensive trading platform integration with simulation
> managementalpha operations,
> and authentication
> Credentials
> are
> stored
> inuser ConfiB.json
> in the
> Same
> directory .
> Provides
> tools
> for creatingsimulations,
> checking status,
> managing alphas,
> accessing platform features
> Py"
> and

6. 配置好了之后，在相同位置的user_config.json中，写入你的brain平台的账号密码。 
> [!NOTE] [图片 OCR 识别内容]
> credentials"
> email"
> password"
> apisettings
> base_Url"
> htts:Lapiwopldquantbrain
> COI
> timeout"
> 30,
> retry_attempts
> forum_settings":
> 'base
> Url 
> https : //support .worldquantbrain
> COI
> 'headless
> true
> timeout"
> 5imulation_defaults"
> type
> REGULAR"
> instrument_type'
> EQUITY"
> region"
> "USA"
> universe'
> T0P3080"
> delay"
> decay"
> neutralization"
> "NONE
> truncation"
> test_period"
> POYBM"
> unit
> handling"
> NONE
> nan
> handling
> NONE
> "language'
> FASTEXPR"
> Visualization"
> true

7. 所有内容配置好了之后，有个测试，点击测试，在所有步骤正确的情况下，就可以查看大佬们写的mcp工具了。
8. 最后希望大家都能装好自己的MCP。:D 
> [!NOTE] [图片 OCR 识别内容]
> C:(Users/l
> 'AppDatalLocallPrograms/Python(Python31z/python
> exe
> 工具(40]
> authenticate
> Authenticate with WorldQua。。
> Value_factor_trendscore
> Compute and retum the dwversit
> manage_config
> Manage configuration settin。。
> Create_slmulation
> Create
> DeW simulation on
> get_alpha_details
> Get detailed infommation ab.
> get_datasets
> Get available datasets Tor re。
> get_datafields
> Get available data felds for
> get_alpha_pnl
> Get PnL (Proft and LOss] dat
> getuser_alphas
> Get Users alphas with adyan。
> submit_alpha
> Submit an alpha for product。
> getevents
> Get available events and CO。。
> get_leaderboard
> Get leaderboard data。Args;
> SaVe_slmulation_data
> SaVe slmulatlon data to
> getoperators
> Get available operators for
> run_selection
> Run
> selection queryto flt。。
> get_user_profile
> Get user profile information。。。
> get_documentations
> Get available documentatiO.
> get_messages
> Get messages Torthe current Us
> getglossan_terms
> Get glossanyterms from WO..
> search_forum_posts
> Search forum posts on Worl。
> read_forum_post
> Get
> specifc forum post by。。
> get_alpha_yearty_stats
> Get yearly statistics for an alpha。
> check_correlation
> Check alpha correlation against
> get_submission_check
> Comprehensive pre-submission
> set_alpha_properties
> Update alpha propertles (name。
> get_record_sets
> List available record sets Toran
> get_record_set_data
> Get data from
> specific record
> get_user_activities
> Get User activity diversit data。
> get_Pyramid_multipliers
> Get Curent
> multipliers
> Pyramid


**顾问 MS51256 (Rank 28) 的解答与建议**:
**===============================顾问 顾问 MS51256 (Rank 28) (Rank 28)的评论===============================**

**感谢大佬的分享，mcp不断在不同的平台不同的ai中应用，在可预见的未来国区的因子质量将会被ai显著提升，期待每一位顾问的分享，期待国区再创佳绩。

================================Do your best ================================**


---

### 技术对话片段 95 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 借助ai手搓出一个IND region的other355字段alpha记录一下步骤经过.md
- **时间**: 3个月前

**提问/主帖背景 (YT18046)**:
首先，将other355数据集的字段丢给AI,我是直接截图给到ai：


> [!NOTE] [图片 OCR 识别内容]
> TsT
> 0+1
> e
> '』+R
> I
> UoGIAn』+CT
> MnI
> ToIro0+0 +1
> NNo-
> 将以上图片中的文字总结形成列表。分别输出字段和描述


Ai会总结输出文字列表：

### **完整字段与描述列表**

1. **字段** ：oth335_combined_all_region_hedge **描述** ：来自对冲模型的得分（Score from the hedge model）
2. **字段** ：oth335_combined_all_region_linear **描述** ：线性模型中的得分（Score from the linear model）
3. **字段** ：oth335_combined_all_region_mind **描述** ：最终综合 MIND 得分（Final composite MIND score）
4. **字段** ：oth335_combined_all_region_mktcap **描述** ：市值（Market Cap）
5. **字段** ：oth335_combined_all_region_shield **描述** ：神盾局模型评分（Score from the SHIELD model）
6. **字段** ：oth335_hc_combined_all_region_hedge **描述** ：来自对冲模型的得分（Score from the hedge model）
7. **字段** ：oth335_hc_combined_all_region_linear **描述** ：线性模型中的得分（Score from the linear model）
8. **字段** ：oth335_hc_combined_all_region_mind **描述** ：最终综合 MIND 得分（Final composite MIND score）
9. **字段** ：oth335_hc_combined_all_region_mktcap **描述** ：市值（Market Cap）
10. **字段** ：oth335_hc_combined_all_region_shield **描述** ：神盾局模型评分（Score from the SHIELD model）

Ai并且直接问我：需要我帮你把这些字段整理成一个 **可直接复制到 WQB 平台的字段选择清单** 吗？这样你在开发多字段 Alpha 时可以快速调用。

我说需要，于是有了以下整理清单，将字段分了两类：

# oth335 全区域基础字段

oth335_combined_all_region_hedge

oth335_combined_all_region_linear

oth335_combined_all_region_mind

oth335_combined_all_region_mktcap

oth335_combined_all_region_shield

# oth335 港股通（hc）全区域字段

oth335_hc_combined_all_region_hedge oth335_hc_combined_all_region_linear oth335_hc_combined_all_region_mind oth335_hc_combined_all_region_mktcap oth335_hc_combined_all_region_shield

第二步，我继续让ai执行以下操作：请将以上字段，通过不同运算符，生成有经济学意义的两字段组合表达式（因为培训时记得老师说单字段不好出，所以直接让ai生成两字段组合的）

Ai生成了三类8个表达式，前面七个我都删减了具体内容，经过回测，只有第8个有信号，指标较好：

### **一、 模型得分关联类（核心逻辑：不同模型得分的互补 / 验证）**

#### **1. 对冲模型波动率 × 线性模型均值**

- **运算符** ：乘法（*）

#### **2. MIND 综合得分 - 神盾局模型评分**

- **运算符** ：减法（-）

#### **3. 对冲模型得分 / 线性模型得分**

- **运算符** ：除法（/）

#### **4. MIND 综合得分的分位数 & 神盾局评分的排名**

- **运算符** ：按位与（&，结合 trade_when 择时）

### **二、 市值修正类（核心逻辑：消除市值规模对模型得分的干扰）**

#### **1. MIND 综合得分 × 市值 Z-score**

- **运算符** ：乘法（*）

#### **2. 对冲模型得分 - 市值对数**

- **运算符** ：减法（-）

### **三、 跨市场联动类（核心逻辑：利用港股通字段捕捉跨境定价一致性）**

#### **1. 全区域对冲模型得分 - 港股通对冲模型得分**

- **运算符** ：减法（-）

#### **2. 全区域 MIND 得分 × 港股通线性模型得分相关性**

- **运算符** ：乘法（*）
- **经济学意义** ：将全区域 MIND 综合得分与港股通线性模型得分的相关性结合，相关性高时代表跨境定价一致，MIND 得分的有效性更强，收益稳定性更高。
- **表达式** ：

python

运行

winsorize(ts_backfill(oth335_combined_all_region_mind, 120), std=3) * ts_corr(winsorize(ts_backfill(oth335_combined_all_region_linear, 120), std=3), winsorize(ts_backfill(oth335_hc_combined_all_region_linear, 120), std=3), 20)

经过回测，只有最后一个指标较好，但提示 robust universe sharpe 为0.8，低于1


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawcOwn
> Margin
> 2.56
> 20.489
> 1.93
> 11.649
> 3.909
> 11.379600
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 8 PASS
> 1FAIL
> Robust universe Sharpe of 0.80is below cutoff of 1
> 1WARNING
> PENDING


第三步，优化提升这个alpha的robust universe sharpe ，这个正好参考论坛最近一篇文章：

[关于印度区因子挖掘遇到一些常见问题的一些小技巧 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[L2] 关于印度区因子挖掘遇到一些常见问题的一些小技巧.md)

直接让ai使用group_rank或signed_power进行针对优化提升。

最终group_rank优化之后，已经达到提交标准，虽然margin不是很好，没有达到15以上，但按我的目前水平，也差不多了哈哈。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
>  Single Data Set Alpha
> Regular Alpha
> Pyramid theme: INDIDIIOTHER X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.62
> 20.159
> 1.90
> 10.629
> 3.139
> 10.549600
  
> [!NOTE] [图片 OCR 识别内容]
> Self
> Prod
> Correlation
> Correlation
> e.B>1
> erg
> 0.43


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 96 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 借助ai手搓出一个IND region的other355字段alpha记录一下步骤经过_38628480955671.md
- **时间**: 3个月前

**提问/主帖背景 (YT18046)**:
首先，将other355数据集的字段丢给AI,我是直接截图给到ai：


> [!NOTE] [图片 OCR 识别内容]
> TsT
> 0+1
> e
> '』+R
> I
> UoGIAn』+CT
> MnI
> ToIro0+0 +1
> NNo-
> 将以上图片中的文字总结形成列表。分别输出字段和描述


Ai会总结输出文字列表：

### **完整字段与描述列表**

1. **字段** ：oth335_combined_all_region_hedge **描述** ：来自对冲模型的得分（Score from the hedge model）
2. **字段** ：oth335_combined_all_region_linear **描述** ：线性模型中的得分（Score from the linear model）
3. **字段** ：oth335_combined_all_region_mind **描述** ：最终综合 MIND 得分（Final composite MIND score）
4. **字段** ：oth335_combined_all_region_mktcap **描述** ：市值（Market Cap）
5. **字段** ：oth335_combined_all_region_shield **描述** ：神盾局模型评分（Score from the SHIELD model）
6. **字段** ：oth335_hc_combined_all_region_hedge **描述** ：来自对冲模型的得分（Score from the hedge model）
7. **字段** ：oth335_hc_combined_all_region_linear **描述** ：线性模型中的得分（Score from the linear model）
8. **字段** ：oth335_hc_combined_all_region_mind **描述** ：最终综合 MIND 得分（Final composite MIND score）
9. **字段** ：oth335_hc_combined_all_region_mktcap **描述** ：市值（Market Cap）
10. **字段** ：oth335_hc_combined_all_region_shield **描述** ：神盾局模型评分（Score from the SHIELD model）

Ai并且直接问我：需要我帮你把这些字段整理成一个 **可直接复制到 WQB 平台的字段选择清单** 吗？这样你在开发多字段 Alpha 时可以快速调用。

我说需要，于是有了以下整理清单，将字段分了两类：

# oth335 全区域基础字段

oth335_combined_all_region_hedge

oth335_combined_all_region_linear

oth335_combined_all_region_mind

oth335_combined_all_region_mktcap

oth335_combined_all_region_shield

# oth335 港股通（hc）全区域字段

oth335_hc_combined_all_region_hedge oth335_hc_combined_all_region_linear oth335_hc_combined_all_region_mind oth335_hc_combined_all_region_mktcap oth335_hc_combined_all_region_shield

第二步，我继续让ai执行以下操作：请将以上字段，通过不同运算符，生成有经济学意义的两字段组合表达式（因为培训时记得老师说单字段不好出，所以直接让ai生成两字段组合的）

Ai生成了三类8个表达式，前面七个我都删减了具体内容，经过回测，只有第8个有信号，指标较好：

### **一、 模型得分关联类（核心逻辑：不同模型得分的互补 / 验证）**

#### **1. 对冲模型波动率 × 线性模型均值**

- **运算符** ：乘法（*）

#### **2. MIND 综合得分 - 神盾局模型评分**

- **运算符** ：减法（-）

#### **3. 对冲模型得分 / 线性模型得分**

- **运算符** ：除法（/）

#### **4. MIND 综合得分的分位数 & 神盾局评分的排名**

- **运算符** ：按位与（&，结合 trade_when 择时）

### **二、 市值修正类（核心逻辑：消除市值规模对模型得分的干扰）**

#### **1. MIND 综合得分 × 市值 Z-score**

- **运算符** ：乘法（*）

#### **2. 对冲模型得分 - 市值对数**

- **运算符** ：减法（-）

### **三、 跨市场联动类（核心逻辑：利用港股通字段捕捉跨境定价一致性）**

#### **1. 全区域对冲模型得分 - 港股通对冲模型得分**

- **运算符** ：减法（-）

#### **2. 全区域 MIND 得分 × 港股通线性模型得分相关性**

- **运算符** ：乘法（*）
- **经济学意义** ：将全区域 MIND 综合得分与港股通线性模型得分的相关性结合，相关性高时代表跨境定价一致，MIND 得分的有效性更强，收益稳定性更高。
- **表达式** ：

python

运行

winsorize(ts_backfill(oth335_combined_all_region_mind, 120), std=3) * ts_corr(winsorize(ts_backfill(oth335_combined_all_region_linear, 120), std=3), winsorize(ts_backfill(oth335_hc_combined_all_region_linear, 120), std=3), 20)

经过回测，只有最后一个指标较好，但提示 robust universe sharpe 为0.8，低于1


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawcOwn
> Margin
> 2.56
> 20.489
> 1.93
> 11.649
> 3.909
> 11.379600
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> 8 PASS
> 1FAIL
> Robust universe Sharpe of 0.80is below cutoff of 1
> 1WARNING
> PENDING


第三步，优化提升这个alpha的robust universe sharpe ，这个正好参考论坛最近一篇文章：

[关于印度区因子挖掘遇到一些常见问题的一些小技巧 – WorldQuant BRAIN]([L2] 关于印度区因子挖掘遇到一些常见问题的一些小技巧_37641142548119.md)

直接让ai使用group_rank或signed_power进行针对优化提升。

最终group_rank优化之后，已经达到提交标准，虽然margin不是很好，没有达到15以上，但按我的目前水平，也差不多了哈哈。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
>  Single Data Set Alpha
> Regular Alpha
> Pyramid theme: INDIDIIOTHER X1.4
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.62
> 20.159
> 1.90
> 10.629
> 3.139
> 10.549600
  
> [!NOTE] [图片 OCR 识别内容]
> Self
> Prod
> Correlation
> Correlation
> e.B>1
> erg
> 0.43


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 97 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化.md
- **时间**: 6个月前

**提问/主帖背景 (YZ14671)**:
从比赛开始到现在已经过半了，这个过程里面也感受到了熬夜两周搭建智能体的过程，这是这段时间的一个成果，主要难点在提示词优化的边界控制上，以及具体的工作流程上进行反复的打磨，其中大家可以参考wj老师发布的具体的工作流程，在实现的基础上继续进行优化。废话不多说，以下是我的详细的AIAC比赛的notebook笔记，配置好后，即插即用，提醒！！！在使用ai时请注意好的你的钱包。

！！！第一call

import sys

import pandas as pd

import ace_lib as ace

import nest_asyncio

import asyncio

import re

from openai import AsyncOpenAI

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

import httpx

nest_asyncio.apply()

_llm_instance = None

def extract_relevant_operators(alpha_expression, all_operators):

"""提取 Alpha 表达式中实际使用的操作符"""

operator_names = all_operators['name'].tolist()

used_operators = []

for op_name in operator_names:

# 使用正则表达式匹配操作符（后面跟着括号）

if re.search(rf'\b{re.escape(op_name)}\s*\(', alpha_expression):

used_operators.append(op_name)

return all_operators[all_operators['name'].isin(used_operators)]

def extract_relevant_datafields(alpha_expression, all_datafields):

"""提取 Alpha 表达式中实际使用的数据字段"""

field_ids = all_datafields['id'].tolist()

used_fields = []

for field_id in field_ids:

if field_id in alpha_expression:

used_fields.append(field_id)

return all_datafields[all_datafields['id'].isin(used_fields)]

def format_operators_for_prompt(operators_df):

"""将操作符数据格式化为简洁的字符串"""

if operators_df.empty:

return "无使用的操作符"

result = []

for _, row in operators_df.iterrows():

result.append(f"- {row['name']}: {row.get('description', 'N/A')}")

return "\n".join(result)

def format_datafields_for_prompt(datafields_df):

"""将数据字段格式化为简洁的字符串"""

if datafields_df.empty:

return "无使用的数据字段"

result = []

for _, row in datafields_df.iterrows():

result.append(f"- {row['id']}: {row.get('name', 'N/A')} (类型: {row.get('type', 'N/A')})")

return "\n".join(result)

def parse_alpha_expressions(llm_response):

"""

从 LLM 响应中解析出 Alpha 表达式

返回格式: [(expression, description), ...]

"""

lines = llm_response.strip().split('\n')

alphas = []

for line in lines:

line = line.strip()

if not line:

continue

# 尝试分离表达式和注释

if '#' in line:

parts = line.split('#', 1)

expression = parts[0].strip()

description = parts[1].strip() if len(parts) > 1 else ""

else:

expression = line

description = ""

# 简单验证：表达式应该包含括号

if '(' in expression and ')' in expression:

alphas.append((expression, description))

return alphas

# 添加重试装饰器，针对连接错误进行重试

@retry(

stop=stop_after_attempt(5),  # 最多重试5次

wait=wait_exponential(multiplier=1, min=4, max=60),  # 指数退避：4秒、8秒、16秒、32秒、60秒

retry=retry_if_exception_type((httpx.RemoteProtocolError, httpx.ConnectError, httpx.ReadTimeout, ConnectionError)),

reraise=True

)

async def call_llm(prompt, timeout=180):

"""

Interface with the LLM API to process the given prompt.

添加了重试机制和超时设置

"""

try:

# 使用更长的超时时间和自定义 httpx 客户端

http_client = httpx.AsyncClient(

timeout=httpx.Timeout(timeout, connect=30.0),

limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),

transport=httpx.AsyncHTTPTransport(retries=3)

)

client = AsyncOpenAI(

base_url=" [[链接已屏蔽]) ",

api_key="sk-xxxxxxx",

http_client=http_client,

timeout=timeout,

max_retries=3

)

print(f"正在调用 LLM (超时设置: {timeout}秒)...")

response = await client.chat.completions.create(

model="deepseek-reasoner",

messages=[

{"role": "user", "content": prompt}

]

)

print("✓ LLM 调用成功")

return response.choices[0].message.content.strip()

except httpx.ReadTimeout as e:

print(f"✗ LLM 调用超时 ({timeout}秒): {e}")

raise

except (httpx.RemoteProtocolError, httpx.ConnectError) as e:

print(f"✗ 连接错误，准备重试: {e}")

raise

except Exception as e:

print(f"✗ 调用 LLM 时出错: {type(e).__name__}: {e}")

return None

finally:

try:

await http_client.aclose()

except:

pass

async def generate_alpha_description(alpha_id, brain_session, max_retries=3):

"""生成 Alpha 的中文描述，从量化研究员的角度分析其经济学意义"""

for attempt in range(1, max_retries + 1):

try:

print(f"\n尝试生成描述 (第 {attempt}/{max_retries} 次)...")

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

alpha_expression = alpha_details['regular']['code']

print(f"Alpha 表达式: {alpha_expression}")

# 获取所有操作符和数据字段

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

dataset_ids = ['pv87', 'fundamental17']

all_datafields = pd.concat(

[ace.get_datafields(brain_session, region='USA', universe='TOP3000', dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids],

ignore_index=True

)

# 提取相关的操作符和数据字段

relevant_operators = extract_relevant_operators(alpha_expression, regular_operators)

relevant_datafields = extract_relevant_datafields(alpha_expression, all_datafields)

print(f"找到 {len(relevant_operators)} 个相关操作符和 {len(relevant_datafields)} 个相关数据字段")

# 格式化为简洁的字符串

operators_str = format_operators_for_prompt(relevant_operators)

datafields_str = format_datafields_for_prompt(relevant_datafields)

# 从资深量化研究员角度生成 prompt

prompt = f"""你是一位资深量化研究员，请从经济学和金融学的角度分析以下 Alpha 表达式：

Alpha 表达式: {alpha_expression}

使用的操作符:

{operators_str}

使用的数据字段:

{datafields_str}

请用中文提供详细分析，包括：

1. **经济学直觉**：这个 Alpha 试图捕捉什么经济现象或市场行为？

2. **信号逻辑**：为什么这种组合可能产生预测能力？

3. **潜在的市场假设**：这个 Alpha 隐含了哪些关于市场效率或投资者行为的假设？

4. **适用场景**：在什么市场环境下这个信号可能表现更好？

请保持分析简洁但深入，重点关注经济合理性。"""

# 使用更长的超时时间（3分钟）

description = await call_llm(prompt, timeout=180)

if description is None:

if attempt < max_retries:

wait_time = 2 ** attempt  # 指数退避

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

continue

return f"无法生成 Alpha 描述 (已重试 {max_retries} 次): {alpha_expression}"

print("✓ 描述生成成功")

return description.strip()

except Exception as e:

print(f"✗ 生成 Alpha 描述时出错 (第 {attempt} 次): {type(e).__name__}: {e}")

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

else:

return f"生成描述时出错 (已重试 {max_retries} 次): {str(e)}"

return f"生成描述失败: 已达到最大重试次数 ({max_retries})"

async def generate_new_alphas(alpha_description, original_expression, brain_session, max_retries=3):

"""

基于经济学原理生成高质量的 Alpha 变体

允许改变操作符结构以提升因子质量

"""

for attempt in range(1, max_retries + 1):

try:

print(f"\n尝试生成新 Alpha (第 {attempt}/{max_retries} 次)...")

num_alphas = 5

# 获取所有可用的操作符

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

operators_list = regular_operators['name'].tolist()

dataset_ids = ['pv87', 'fundamental17']

data_fields = pd.concat(

[ace.get_datafields(brain_session, region='USA', universe='TOP3000', dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids],

ignore_index=True

)

# 提取数据字段信息

datafields_summary = []

for _, row in data_fields.iterrows():

datafields_summary.append(f"{row['id']} (类型: {row.get('type', 'N/A')}, 名称: {row.get('name', 'N/A')})")

datafields_str = "\n".join(datafields_summary[:150])  # 提供更多字段选择

# 从资深量化研究员角度设计 prompt

prompt = f"""你是一位资深量化研究员，专注于开发具有明确经济学意义的 Alpha 因子。

【原始 Alpha 分析】

表达式: {original_expression}

经济学解读:

{alpha_description}

【可用资源】

操作符（部分）: {', '.join(operators_list[:50])}

可用数据字段:

{datafields_str}

【任务要求】

基于原始 Alpha 的经济学直觉，生成 {num_alphas} 个高质量的变体表达式。

【核心原则 - 作为顶级 BRAIN 顾问】

1. **经济合理性优先**：每个 Alpha 必须有清晰的经济学逻辑，避免纯数据挖掘

2. **低换手率**：优先使用较长的时间窗口（如 ts_decay_linear, ts_mean），避免高频交易信号

3. **稳健性**：使用 winsorize、rank、neutralize 等操作符提升因子稳健性

4. **多样性**：探索不同的数据类别（基本面、情绪、技术指标）以提升金字塔覆盖度

【操作符结构调整指南】

- 可以改变操作符组合以提升因子质量

- 推荐的稳健操作符：ts_decay_linear, ts_mean, ts_rank, winsorize, rank, neutralize

- 避免过度复杂的嵌套（不超过 4-5 层）

- 时间窗口建议：5-60 天（避免过短导致高换手）

【数据字段选择】

- 优先选择基本面数据（earnings, revenue, cash_flow 等）

- 考虑分析师预期数据（consensus, estimate）

- 可以组合不同类型的数据以捕捉多维信号

【语法规范】

- type=MATRIX 字段可直接使用

- type=VECTOR 字段必须用 Vector() 包装

- type=GROUP 字段只能作为 Group 操作符参数

- 确保所有括号匹配，参数格式正确

【输出格式】

请生成 {num_alphas} 个表达式，每行一个，格式如下：

表达式1  # 经济学逻辑说明

表达式2  # 经济学逻辑说明

...

示例格式：

ts_decay_linear(rank(fundamental17_sales_growth), 20)  # 捕捉销售增长的持续性趋势

"""

# 使用更长的超时时间（3分钟）

response = await call_llm(prompt, timeout=180)

if response is None:

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

continue

return f"生成新 Alpha 失败 (已重试 {max_retries} 次)，请检查 LLM 连接。"

print("✓ 新 Alpha 生成成功")

return response.strip()

except Exception as e:

print(f"✗ 生成新 Alpha 时出错 (第 {attempt} 次): {type(e).__name__}: {e}")

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

else:

return f"生成新 Alpha 时出错 (已重试 {max_retries} 次): {str(e)}"

return f"生成新 Alpha 失败: 已达到最大重试次数 ({max_retries})"

async def main():

# 启动 Brain 会话

brain_session = ace.start_session()

# Alpha ID 列表

alpha_ids = ["kqEnlEA8"]

for alpha_id in alpha_ids:

print(f"\n{'='*60}")

print(f"处理 Alpha ID: {alpha_id}")

print(f"{'='*60}")

# 获取原始表达式

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

original_expression = alpha_details['regular']['code']

# 步骤 1: 生成 Alpha 的经济学描述（带重试）

alpha_description = await generate_alpha_description(alpha_id, brain_session, max_retries=3)

if alpha_description and not alpha_description.startswith("无法") and not alpha_description.startswith("生成描述时出错") and not alpha_description.startswith("生成描述失败"):

print(f"\n【Alpha 经济学分析】\n{alpha_description}")

# 步骤 2: 基于经济学原理生成新的高质量 Alpha（带重试）

new_alphas_response = await generate_new_alphas(alpha_description, original_expression, brain_session, max_retries=3)

print(f"\n【生成的高质量 Alpha 变体】\n{new_alphas_response}")

# 步骤 3: 解析生成的 Alpha 表达式

parsed_alphas = parse_alpha_expressions(new_alphas_response)

if not parsed_alphas:

print("\n警告: 未能从 LLM 响应中解析出有效的 Alpha 表达式")

continue

print(f"\n成功解析 {len(parsed_alphas)} 个 Alpha 表达式，开始模拟...")

# 步骤 4: 逐个模拟生成的 Alpha

successful_simulations = []

failed_simulations = []

for idx, (expression, description) in enumerate(parsed_alphas, 1):

print(f"\n--- 模拟 Alpha {idx}/{len(parsed_alphas)} ---")

print(f"表达式: {expression}")

print(f"说明: {description}")

try:

# 生成 Alpha 配置

simulate_data = ace.generate_alpha(

regular=expression,

alpha_type="REGULAR",

region="USA",

universe="TOP3000",

delay=1,

decay=0,

neutralization="INDUSTRY",

truncation=0.08,

pasteurization="ON",

nan_handling="OFF",

unit_handling="VERIFY",

visualization=True

)

# 执行模拟

print("正在提交模拟...")

simulation_result = ace.simulate_single_alpha(brain_session, simulate_data)

child_alpha_id = simulation_result.get('alpha_id')

if child_alpha_id:

print(f"✓ 模拟成功! Alpha ID: {child_alpha_id}")

# 设置 Alpha 属性和标签

full_description = f"【父 Alpha】{alpha_id}\n【经济学逻辑】{description}\n【原始分析】{alpha_description[:200]}..."

ace.set_alpha_properties(

brain_session,

child_alpha_id,

tags=[alpha_id],

regular_desc=full_description

)

print(f"✓ 已设置标签和描述")

successful_simulations.append({

'alpha_id': child_alpha_id,

'expression': expression,

'description': description

})

else:

print(f"✗ 模拟失败: 未返回 Alpha ID")

failed_simulations.append({

'expression': expression,

'reason': '未返回 Alpha ID'

})

except Exception as e:

print(f"✗ 模拟出错: {str(e)}")

failed_simulations.append({

'expression': expression,

'reason': str(e)

})

# 步骤 5: 输出总结

print(f"\n{'='*60}")

print(f"模拟总结 - 父 Alpha: {alpha_id}")

print(f"{'='*60}")

print(f"成功: {len(successful_simulations)} 个")

print(f"失败: {len(failed_simulations)} 个")

if successful_simulations:

print("\n成功的 Alpha:")

for item in successful_simulations:

print(f"  - {item['alpha_id']}: {item['expression'][:60]}...")

if failed_simulations:

print("\n失败的 Alpha:")

for item in failed_simulations:

print(f"  - {item['expression'][:60]}... (原因: {item['reason']})")

else:

print(f"\n{alpha_description}")

print("由于描述生成错误，跳过 Alpha 生成。")

！！！第二call

asyncio.run(main())

！！！第三call

# 检索性能指标、可视化和分析

# 选出冠军alpha

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

from datetime import datetime

# 设置中文字体支持

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']

plt.rcParams['axes.unicode_minus'] = False

async def get_alpha_performance(brain_session, alpha_id):

"""获取 Alpha 的性能指标"""

try:

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

# 提取关键性能指标

is_stats = alpha_details.get('is', {})

performance = {

'alpha_id': alpha_id,

'sharpe': is_stats.get('sharpe'),

'fitness': is_stats.get('fitness'),

'turnover': is_stats.get('turnover'),

'returns': is_stats.get('returns'),

'drawdown': is_stats.get('drawdown'),

'margin': is_stats.get('margin'),

'expression': alpha_details.get('regular', {}).get('code', ''),

'created_at': alpha_details.get('created')

}

return performance

except Exception as e:

print(f"获取 Alpha {alpha_id} 性能时出错: {e}")

return None

async def get_alphas_by_tag(brain_session, tag):

"""通过标签获取 Alpha 家族"""

try:

# 获取用户的所有 IS 阶段 Alphas

response = brain_session.get(

" [[链接已屏蔽]) ",

params={'stage': 'IS', 'limit': 100}

).json()

alphas = response.get('results', [])

# 筛选包含指定标签的 Alphas

tagged_alphas = []

for alpha in alphas:

if tag in alpha.get('tags', []):

tagged_alphas.append(alpha['id'])

print(f"找到 {len(tagged_alphas)} 个带有标签 '{tag}' 的 Alphas")

return tagged_alphas

except Exception as e:

print(f"获取标签 Alphas 时出错: {e}")

return []

def visualize_performance(performance_data, parent_alpha_id):

"""可视化性能对比"""

if not performance_data:

print("没有可用的性能数据")

return

# 过滤掉 None 值

valid_data = [p for p in performance_data if p and all(

p.get(k) is not None for k in ['sharpe', 'fitness', 'turnover']

)]

if not valid_data:

print("没有完整的性能数据可供可视化")

return

df = pd.DataFrame(valid_data)

# 创建 2x2 子图

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

fig.suptitle(f'Alpha 家族性能对比 (父 Alpha: {parent_alpha_id})', fontsize=16, fontweight='bold')

# 1. Sharpe vs Fitness 散点图

ax1 = axes[0, 0]

scatter = ax1.scatter(df['sharpe'], df['fitness'],

c=df['turnover'],cmap='viridis',

s=200, alpha=0.6, edgecolors='black')

ax1.set_xlabel('Sharpe Ratio', fontsize=12)

ax1.set_ylabel('Fitness', fontsize=12)

ax1.set_title('Sharpe vs Fitness (颜色=Turnover)', fontsize=14)

ax1.grid(True, alpha=0.3)

# 添加颜色条

cbar = plt.colorbar(scatter, ax=ax1)

cbar.set_label('Turnover', fontsize=10)

# 标注 Alpha ID

for idx, row in df.iterrows():

ax1.annotate(row['alpha_id'][:6],

(row['sharpe'], row['fitness']),

fontsize=8, alpha=0.7)

# 2. 性能指标柱状图对比

ax2 = axes[0, 1]

x = np.arange(len(df))

width = 0.25

ax2.bar(x - width, df['sharpe'], width, label='Sharpe', alpha=0.8)

ax2.bar(x, df['fitness'], width, label='Fitness', alpha=0.8)

ax2.bar(x + width, df['turnover'], width, label='Turnover', alpha=0.8)

ax2.set_xlabel('Alpha Index', fontsize=12)

ax2.set_ylabel('指标值', fontsize=12)

ax2.set_title('关键指标对比', fontsize=14)

ax2.set_xticks(x)

ax2.set_xticklabels([f"#{i+1}" for i in range(len(df))], fontsize=9)

ax2.legend()

ax2.grid(True, alpha=0.3, axis='y')

# 3. Turnover 分布

ax3 = axes[1, 0]

ax3.barh(range(len(df)), df['turnover'], color='coral', alpha=0.7, edgecolor='black')

ax3.set_yticks(range(len(df)))

ax3.set_yticklabels([aid[:8] for aid in df['alpha_id']], fontsize=9)

ax3.set_xlabel('Turnover', fontsize=12)

ax3.set_title('换手率对比', fontsize=14)

ax3.grid(True, alpha=0.3, axis='x')

# 添加参考线（低换手率阈值）

ax3.axvline(x=0.1, color='green', linestyle='--', linewidth=2, label='低换手阈值 (0.1)')

ax3.legend()

# 4. 综合评分雷达图（选择前3个）

ax4 = axes[1, 1]

if len(df) > 0:

# 归一化数据到 0-1

metrics = ['sharpe', 'fitness', 'returns', 'margin']

available_metrics = [m for m in metrics if m in df.columns and df[m].notna().any()]

if len(available_metrics) >= 3:

# 选择前3个 Alpha

top_alphas = df.nlargest(min(3, len(df)), 'fitness')

angles = np.linspace(0, 2 * np.pi, len(available_metrics), endpoint=False).tolist()

angles += angles[:1]

ax4 = plt.subplot(2, 2, 4, projection='polar')

for idx, row in top_alphas.iterrows():

values = []

for metric in available_metrics:

val = row[metric]

# 简单归一化

max_val = df[metric].max()

min_val = df[metric].min()

if max_val != min_val:

normalized = (val - min_val) / (max_val - min_val)

else:

normalized = 0.5

values.append(normalized)

values += values[:1]

ax4.plot(angles, values, 'o-', linewidth=2, label=row['alpha_id'][:8])

ax4.fill(angles, values, alpha=0.15)

ax4.set_xticks(angles[:-1])

ax4.set_xticklabels(available_metrics, fontsize=10)

ax4.set_ylim(0, 1)

ax4.set_title('Top 3 Alphas 综合对比', fontsize=14, pad=20)

ax4.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

ax4.grid(True)

else:

ax4.text(0.5,0.5,'数据不足，无法生成雷达图',

ha='center', va='center', fontsize=12)

ax4.axis('off')

plt.tight_layout()

plt.show()

return df

async def llm_analyze_results(performance_df, parent_alpha_id, brain_session):

"""LLM 分析实验结果并提出建议"""

if performance_df is None or len(performance_df) == 0:

return "没有可用的性能数据进行分析"

# 准备数据摘要

summary_stats = {

'total_alphas': len(performance_df),

'avg_sharpe': performance_df['sharpe'].mean(),

'max_sharpe': performance_df['sharpe'].max(),

'avg_fitness': performance_df['fitness'].mean(),

'max_fitness': performance_df['fitness'].max(),

'avg_turnover': performance_df['turnover'].mean(),

'min_turnover': performance_df['turnover'].min()

}

# 找出最佳 Alpha

best_alpha = performance_df.loc[performance_df['fitness'].idxmax()]

# 构建分析 prompt

prompt = f"""你是一位资深量化研究员，请分析以下 Alpha 实验结果：

【实验概况】

- 父 Alpha ID: {parent_alpha_id}

- 生成的变体数量: {summary_stats['total_alphas']}

【性能统计】

- 平均 Sharpe: {summary_stats['avg_sharpe']:.4f} (最高: {summary_stats['max_sharpe']:.4f})

- 平均 Fitness: {summary_stats['avg_fitness']:.4f} (最高: {summary_stats['max_fitness']:.4f})

- 平均 Turnover: {summary_stats['avg_turnover']:.4f} (最低: {summary_stats['min_turnover']:.4f})

【最佳 Alpha】

- ID: {best_alpha['alpha_id']}

- Sharpe: {best_alpha['sharpe']:.4f}

- Fitness: {best_alpha['fitness']:.4f}

- Turnover: {best_alpha['turnover']:.4f}

- 表达式: {best_alpha['expression']}

【详细数据】

{performance_df[['alpha_id', 'sharpe', 'fitness', 'turnover', 'returns']].to_string()}

请提供以下分析：

1. **实验成果评估**

- 这批 Alpha 的整体质量如何？

- 是否有突出的表现者？

2. **关键发现**

- 哪些因子组合或数据字段表现最好？

- Sharpe、Fitness、Turnover 之间的权衡如何？

3. **改进方向**

- 基于当前结果，下一轮实验应该关注什么？

- 建议调整哪些参数或尝试哪些新的数据组合？

4. **金字塔策略**

- 从金字塔多样性角度，建议探索哪些新的数据类别或因子逻辑？

请用中文提供简洁但深入的分析。"""

print("\n正在生成 LLM 分析报告...")

analysis = await call_llm(prompt, timeout=180)

return analysis

async def analyze_alpha_family(parent_alpha_id):

"""完整的 Alpha 家族分析流程"""

brain_session = ace.start_session()

print(f"\n{'='*60}")

print(f"Alpha 家族分析 - 父 Alpha: {parent_alpha_id}")

print(f"{'='*60}\n")

# 步骤 1: 通过标签获取 Alpha 家族

print("步骤 1: 检索 Alpha 家族...")

alpha_ids = await get_alphas_by_tag(brain_session, parent_alpha_id)

if not alpha_ids:

print(f"未找到带有标签 '{parent_alpha_id}' 的 Alphas")

return

# 步骤 2: 获取所有 Alpha 的性能数据

print("\n步骤 2: 获取性能指标...")

performance_data = []

for alpha_id in alpha_ids:

print(f"  获取 {alpha_id} 的性能数据...")

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

performance_data.append(perf)

if not performance_data:

print("未能获取任何性能数据")

return

print(f"\n成功获取 {len(performance_data)} 个 Alpha 的性能数据")

# 步骤 3: 可视化性能对比

print("\n步骤 3: 生成可视化图表...")

performance_df = visualize_performance(performance_data, parent_alpha_id)

# 步骤 4: LLM 分析结果

print("\n步骤 4: LLM 分析实验结果...")

analysis = await llm_analyze_results(performance_df, parent_alpha_id, brain_session)

print(f"\n{'='*60}")

print("LLM 分析报告")

print(f"{'='*60}\n")

print(analysis)

# 返回结果供后续使用

return {

'performance_df': performance_df,

'analysis': analysis,

'alpha_ids': alpha_ids

}

# 执行分析

parent_alpha_id = "kqEnlEA8"  # 替换为你的父 Alpha ID

results = await analyze_alpha_family(parent_alpha_id)

！！！第四call

# ==================== Cell 4: 完整的自动迭代优化系统 ====================

# ===== 辅助函数声明 =====

async def get_alphas_by_tag(brain_session, tag):

"""根据标签获取 Alpha ID 列表"""

try:

# 直接使用 Brain API 获取用户的 Alpha 列表

url = f" [[链接已屏蔽]) "

alphas_response = brain_session.get(url).json()

# 过滤出带有指定标签的 Alpha

alpha_ids = []

for alpha in alphas_response.get('results', []):

if tag in alpha.get('tags', []):

alpha_ids.append(alpha['id'])

print(f"找到 {len(alpha_ids)} 个带有标签 '{tag}' 的 Alphas")

return alpha_ids

except Exception as e:

print(f"获取 Alpha 列表失败: {e}")

return []

async def get_alpha_performance(brain_session, alpha_id):

"""获取单个 Alpha 的性能指标"""

try:

alpha_details = ace.get_simulation_result_json(brain_session, alpha_id)

if not alpha_details or 'is' not in alpha_details:

return None

is_data = alpha_details['is']

return {

'alpha_id': alpha_id,

'sharpe': is_data.get('sharpe', 0),

'fitness': is_data.get('fitness', 0),

'returns': is_data.get('returns', 0),

'turnover': is_data.get('turnover', 0),

'margin': is_data.get('margin', 0),

'drawdown': is_data.get('drawdown', 0),

'expression': alpha_details.get('regular', {}).get('code', '')

}

except Exception as e:

print(f"获取 Alpha {alpha_id} 性能失败: {str(e)}")

return None

def visualize_performance(performance_data, parent_alpha_id):

"""可视化性能数据"""

if not performance_data:

print("没有数据可供可视化")

return

df = pd.DataFrame(performance_data)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

fig.suptitle(f'Alpha Family {parent_alpha_id} - Performance Overview', fontsize=16)

# Sharpe vs Fitness

axes[0, 0].scatter(df['sharpe'], df['fitness'], alpha=0.6, s=100)

axes[0, 0].set_xlabel('Sharpe Ratio')

axes[0, 0].set_ylabel('Fitness')

axes[0, 0].set_title('Sharpe vs Fitness')

axes[0, 0].grid(True, alpha=0.3)

# Turnover vs Returns

axes[0, 1].scatter(df['turnover'], df['returns'], alpha=0.6, s=100, c='green')

axes[0, 1].set_xlabel('Turnover')

axes[0, 1].set_ylabel('Returns')

axes[0, 1].set_title('Turnover vs Returns')

axes[0, 1].grid(True, alpha=0.3)

# Sharpe Distribution

axes[1, 0].hist(df['sharpe'], bins=20, alpha=0.7, color='blue', edgecolor='black')

axes[1, 0].set_xlabel('Sharpe Ratio')

axes[1, 0].set_ylabel('Frequency')

axes[1, 0].set_title('Sharpe Distribution')

axes[1, 0].grid(True, alpha=0.3)

# Top Alphas

top_df = df.nlargest(10, 'sharpe')

axes[1, 1].barh(range(len(top_df)), top_df['sharpe'])

axes[1, 1].set_yticks(range(len(top_df)))

axes[1, 1].set_yticklabels([aid[:8] for aid in top_df['alpha_id']])

axes[1, 1].set_xlabel('Sharpe Ratio')

axes[1, 1].set_title('Top 10 Alphas by Sharpe')

axes[1, 1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()

plt.show()

async def select_best_alphas(performance_df, criteria='balanced', top_n=3):

"""选择最佳 Alpha"""

if performance_df.empty:

return []

df = performance_df.copy()

if criteria == 'sharpe':

df = df.sort_values('sharpe', ascending=False)

elif criteria == 'fitness':

df = df.sort_values('fitness', ascending=False)

elif criteria == 'balanced':

# 综合评分: Sharpe * 0.4 + Fitness * 0.3 + (1/Turnover) * 0.3

df['score'] = (df['sharpe'] *0.4+

df['fitness'] *0.3+

(1 / (df['turnover'] + 0.01)) * 0.3)

df = df.sort_values('score', ascending=False)

best = df.head(top_n).to_dict('records')

print(f"\n选出 Top {len(best)} Alpha:")

for i, alpha in enumerate(best, 1):

print(f"{i}. {alpha['alpha_id']}")

print(f"   Sharpe: {alpha['sharpe']:.4f}, Fitness: {alpha['fitness']:.4f}, Turnover: {alpha['turnover']:.4f}")

return best

async def decide_next_iteration(performance_df, current_iteration, max_iterations):

"""决策是否继续迭代"""

if current_iteration >= max_iterations:

return False, "达到最大迭代次数", []

if performance_df.empty:

return False, "没有有效的性能数据", []

# 检查是否有改进

avg_sharpe = performance_df['sharpe'].mean()

avg_fitness = performance_df['fitness'].mean()

if avg_sharpe < 0.5 or avg_fitness < 0.3:

return False, "整体性能过低，建议重新设计策略", []

suggestions = [

"继续优化参数",

"尝试新的数据字段组合",

"调整时间窗口以降低换手率"

]

return True, "性能有提升空间，继续迭代", suggestions

async def llm_analyze_results(performance_df, parent_alpha_id, brain_session):

"""LLM 分析结果"""

if performance_df.empty:

return "没有数据可供分析"

stats = {

'count': len(performance_df),

'avg_sharpe': performance_df['sharpe'].mean(),

'max_sharpe': performance_df['sharpe'].max(),

'avg_fitness': performance_df['fitness'].mean(),

'avg_turnover': performance_df['turnover'].mean()

}

prompt = f"""分析以下 Alpha 家族的性能数据:

Alpha 数量: {stats['count']}

平均 Sharpe: {stats['avg_sharpe']:.4f}

最高 Sharpe: {stats['max_sharpe']:.4f}

平均 Fitness: {stats['avg_fitness']:.4f}

平均 Turnover: {stats['avg_turnover']:.4f}

请提供简洁的分析（3-5 句话）:

1. 整体表现评价

2. 主要优势

3. 需要改进的方面

"""

response = await call_llm(prompt, timeout=60)

return response if response else "分析失败"

async def llm_iteration_suggestions(performance_df, iteration, best_alphas):

"""LLM 生成迭代优化建议"""

if not best_alphas:

return "没有最佳 Alpha 可供分析"

top_alpha = best_alphas[0]

prompt = f"""当前是第 {iteration} 轮迭代。

最佳 Alpha 表现:

- 表达式: {top_alpha['expression']}

- Sharpe: {top_alpha['sharpe']:.4f}

- Fitness: {top_alpha['fitness']:.4f}

- Turnover: {top_alpha['turnover']:.4f}

请提供 3-5 条具体的优化建议，每条建议应该:

1. 针对具体问题

2. 给出可操作的改进方向

3. 简洁明了（每条 1-2 句话）

"""

response = await call_llm(prompt, timeout=60)

return response if response else "建议生成失败"

async def export_alpha_family(parent_alpha_id, performance_df, best_alphas, output_file):

"""导出 Alpha 家族报告"""

with open(output_file, 'w', encoding='utf-8') as f:

f.write(f"Alpha Family Report: {parent_alpha_id}\n")

f.write(f"Generated: {datetime.now()}\n")

f.write("="*80 + "\n\n")

f.write(f"Total Alphas: {len(performance_df)}\n")

f.write(f"Average Sharpe: {performance_df['sharpe'].mean():.4f}\n")

f.write(f"Average Fitness: {performance_df['fitness'].mean():.4f}\n")

f.write(f"Average Turnover: {performance_df['turnover'].mean():.4f}\n\n")

f.write("Top 5 Best Alphas:\n")

f.write("-"*80 + "\n")

for i, alpha in enumerate(best_alphas[:5], 1):

f.write(f"\n{i}. Alpha ID: {alpha['alpha_id']}\n")

f.write(f"   Expression: {alpha['expression']}\n")

f.write(f"   Sharpe: {alpha['sharpe']:.4f}\n")

f.write(f"   Fitness: {alpha['fitness']:.4f}\n")

f.write(f"   Turnover: {alpha['turnover']:.4f}\n")

print(f"✓ 报告已导出到: {output_file}")

return output_file

# ===== 主要函数 =====

async def generate_optimized_alphas_from_best(best_alphas, brain_session, optimization_suggestions, num_new_alphas=5):

"""基于最佳 Alpha 和优化建议生成新一轮 Alpha"""

print(f"\n{'='*60}")

print(f"基于最佳 Alpha 生成新一轮优化变体")

print(f"{'='*60}\n")

if not best_alphas or len(best_alphas) == 0:

print("没有可用的最佳 Alpha")

return []

# 选择表现最好的 Alpha 作为基础

base_alpha = best_alphas[0]

base_expression = base_alpha['expression']

base_alpha_id = base_alpha['alpha_id']

print(f"基础 Alpha ID: {base_alpha_id}")

print(f"基础表达式: {base_expression}")

print(f"性能指标: Sharpe={base_alpha['sharpe']:.4f}, Fitness={base_alpha['fitness']:.4f}, Turnover={base_alpha['turnover']:.4f}\n")

# 获取操作符和数据字段

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

operators_list = regular_operators['name'].tolist()

dataset_ids = ['pv87', 'fundamental17']

data_fields = pd.concat([

ace.get_datafields(brain_session,region='USA',universe='TOP3000',

dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids

], ignore_index=True)

datafields_summary = [

f"{row['id']} (类型: {row.get('type','N/A')}, 名称: {row.get('name','N/A')})"

for _, row in data_fields.iterrows()

]

datafields_str = "\n".join(datafields_summary[:150])

# 构建优化 prompt

prompt = f"""你是一位资深量化研究员，正在进行 Alpha 因子的迭代优化。

【上一轮最佳 Alpha】

表达式: {base_expression}

性能: Sharpe={base_alpha['sharpe']:.4f}, Fitness={base_alpha['fitness']:.4f}, Turnover={base_alpha['turnover']:.4f}

【优化建议】

{optimization_suggestions}

【可用资源】

操作符（部分）: {', '.join(operators_list[:50])}

可用数据字段:

{datafields_str}

【优化任务】

基于上述最佳 Alpha 和优化建议，生成 {num_new_alphas} 个改进版本的 Alpha 表达式。

【优化策略】

1. **保留优势**: 保持最佳 Alpha 中表现好的核心逻辑

2. **针对性改进**: 根据优化建议调整参数或操作符

3. **渐进式变化**: 每次只改变 1-2 个关键要素，避免过度变异

4. **多样化探索**: 在保持核心逻辑的同时，尝试不同的实现方式

【具体改进方向】

- 如果 Turnover 过高: 增加时间窗口参数（如 20→40），使用 ts_decay_linear

- 如果 Sharpe 不足: 尝试组合更多数据字段，增强信号强度

- 如果 Fitness 偏低: 添加 winsorize、rank、neutralize 提升稳健性

- 探索新的数据类别: 基本面、分析师预期、情绪指标等

【语法规范】

- type=MATRIX 字段可直接使用

- type=VECTOR 字段必须用 Vector() 包装

- type=GROUP 字段只能作为 Group 操作符参数

- 确保所有括号匹配，参数格式正确

【输出格式】

请生成 {num_new_alphas} 个表达式，每行一个，格式如下：

表达式1  # 改进说明

表达式2  # 改进说明

...

示例：

ts_decay_linear(rank(fundamental17_sales_growth), 40)  # 增加时间窗口从20到40，降低换手率

"""

print("正在调用 LLM 生成优化后的 Alpha...")

response = await call_llm(prompt, timeout=180)

if response is None:

print("✗ LLM 调用失败")

return []

print("✓ LLM 生成成功\n")

# 解析生成的 Alpha 表达式

parsed_alphas = parse_alpha_expressions(response)

if not parsed_alphas:

print("警告: 未能解析出有效的 Alpha 表达式")

return []

print(f"成功解析 {len(parsed_alphas)} 个 Alpha 表达式，开始模拟...\n")

# 模拟新生成的 Alpha

new_alpha_ids = []

successful_simulations = []

failed_simulations = []

for idx, (expression, description) in enumerate(parsed_alphas, 1):

print(f"--- 模拟优化 Alpha {idx}/{len(parsed_alphas)} ---")

print(f"表达式: {expression}")

print(f"说明: {description}")

try:

simulate_data = ace.generate_alpha(

regular=expression,

alpha_type="REGULAR",

region="USA",

universe="TOP3000",

delay=1,

decay=0,

neutralization="INDUSTRY",

truncation=0.08,

pasteurization="ON",

nan_handling="OFF",

unit_handling="VERIFY",

visualization=True

)

print("正在提交模拟...")

simulation_result = ace.simulate_single_alpha(brain_session, simulate_data)

child_alpha_id = simulation_result.get('alpha_id')

if child_alpha_id:

print(f"✓ 模拟成功! Alpha ID: {child_alpha_id}")

# 设置标签（使用原始父 Alpha ID）

parent_tag = base_alpha.get('parent_alpha_id', base_alpha_id)

full_description = f"【父 Alpha】{parent_tag}\n【优化自】{base_alpha_id}\n【改进说明】{description}"

ace.set_alpha_properties(

brain_session,

child_alpha_id,

tags=[parent_tag],

regular_desc=full_description

)

print(f"✓ 已设置标签: {parent_tag}\n")

new_alpha_ids.append(child_alpha_id)

successful_simulations.append({

'alpha_id': child_alpha_id,

'expression': expression,

'description': description

})

else:

print(f"✗ 模拟失败: 未返回 Alpha ID\n")

failed_simulations.append({

'expression': expression,

'reason': '未返回 Alpha ID'

})

except Exception as e:

print(f"✗ 模拟出错: {str(e)}\n")

failed_simulations.append({

'expression': expression,

'reason': str(e)

})

# 输出总结

print(f"{'='*60}")

print(f"本轮优化模拟总结")

print(f"{'='*60}")

print(f"成功: {len(successful_simulations)} 个")

print(f"失败: {len(failed_simulations)} 个")

if successful_simulations:

print("\n成功的 Alpha:")

for item in successful_simulations:

print(f"  - {item['alpha_id']}: {item['expression'][:60]}...")

if failed_simulations:

print("\n失败的 Alpha:")

for item in failed_simulations:

print(f"  - {item['expression'][:60]}... (原因: {item['reason']})")

return new_alpha_ids

asyncdeffull_auto_iteration_workflow(parent_alpha_id,max_iterations=5,alphas_per_iteration=5,

selection_criteria='balanced', min_quality_threshold=None):

"""完全自动化的迭代优化工作流"""

brain_session = ace.start_session()

print(f"\n{'#'*80}")

print(f"# 完全自动化 Alpha 迭代优化工作流")

print(f"# 初始父 Alpha: {parent_alpha_id}")

print(f"# 最大迭代次数: {max_iterations}")

print(f"# 每轮生成数量: {alphas_per_iteration}")

print(f"# 选择标准: {selection_criteria}")

print(f"{'#'*80}\n")

# 设置默认质量阈值

if min_quality_threshold is None:

min_quality_threshold = {

'sharpe': 1.5,

'fitness': 1,

'turnover': 0.15

}

all_iterations_history = []

current_parent_id = parent_alpha_id

for iteration in range(1, max_iterations + 1):

print(f"\n{'='*80}")

print(f"第 {iteration}/{max_iterations} 轮迭代")

print(f"{'='*80}\n")

iteration_start_time = datetime.now()

# ===== 步骤 1: 获取当前 Alpha 家族 =====

print("步骤 1: 检索 Alpha 家族...")

alpha_ids = await get_alphas_by_tag(brain_session, current_parent_id)

if not alpha_ids:

if iteration == 1:

print(f"第一轮未找到 Alpha，请先运行初始 Alpha 生成")

return None

else:

print("未找到新的 Alpha，使用上一轮数据")

break

print(f"找到 {len(alpha_ids)} 个 Alpha\n")

# ===== 步骤 2: 获取性能数据 =====

print("步骤 2: 获取性能指标...")

performance_data = []

for alpha_id in alpha_ids:

print(f"  获取 {alpha_id}...")

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

perf['parent_alpha_id'] = current_parent_id

performance_data.append(perf)

if not performance_data:

print("未能获取任何性能数据")

break

performance_df = pd.DataFrame(performance_data)

print(f"成功获取 {len(performance_df)} 个 Alpha 的性能数据\n")

# ===== 步骤 3: 可视化 =====

print("步骤 3: 生成可视化图表...")

visualize_performance(performance_data, current_parent_id)

# ===== 步骤 4: 选择最佳 Alpha =====

print("\n步骤 4: 选择最佳 Alpha...")

best_alphas = await select_best_alphas(performance_df, selection_criteria, top_n=3)

if not best_alphas:

print("未能选择出最佳 Alpha")

break

# ===== 步骤 5: 检查是否达到质量阈值 =====

print("\n步骤 5: 检查质量阈值...")

top_alpha = best_alphas[0]

quality_check = (

top_alpha['sharpe'] >= min_quality_threshold['sharpe'] and

top_alpha['fitness'] >= min_quality_threshold['fitness'] and

top_alpha['turnover'] <= min_quality_threshold['turnover']

)

if quality_check:

print(f"✓ 达到质量阈值!")

print(f"  Sharpe: {top_alpha['sharpe']:.4f} >= {min_quality_threshold['sharpe']}")

print(f"  Fitness: {top_alpha['fitness']:.4f} >= {min_quality_threshold['fitness']}")

print(f"  Turnover: {top_alpha['turnover']:.4f} <= {min_quality_threshold['turnover']}")

should_continue = False

reason = "达到质量阈值，优化成功"

suggestions = []

else:

# ===== 步骤 6: 决策是否继续迭代 =====

print("\n步骤 6: 迭代决策...")

should_continue, reason, suggestions = await decide_next_iteration(

performance_df, iteration, max_iterations

)

# ===== 步骤 7: LLM 分析 =====

print("\n步骤 7: LLM 分析结果...")

llm_analysis = await llm_analyze_results(performance_df, current_parent_id, brain_session)

print(f"\n【LLM 分析】\n{llm_analysis}\n")

# ===== 步骤 8: 生成优化建议 =====

print("\n步骤 8: 生成优化建议...")

llm_suggestions = await llm_iteration_suggestions(performance_df, iteration, best_alphas)

print(f"\n【LLM 优化建议】\n{llm_suggestions}\n")

# 保存本轮数据

iteration_data = {

'iteration': iteration,

'parent_alpha_id': current_parent_id,

'alpha_count': len(alpha_ids),

'performance_df': performance_df,

'best_alphas': best_alphas,

'should_continue': should_continue,

'reason': reason,

'suggestions': suggestions,

'llm_analysis': llm_analysis,

'llm_suggestions': llm_suggestions,

'duration': (datetime.now() - iteration_start_time).total_seconds()

}

all_iterations_history.append(iteration_data)

# ===== 决策点: 是否继续迭代 =====

if not should_continue:

print(f"\n{'='*80}")

print(f"✓ 迭代结束: {reason}")

print(f"{'='*80}\n")

break

# ===== 步骤 9: 生成下一轮 Alpha =====

if iteration < max_iterations:

print(f"\n步骤 9: 生成下一轮优化 Alpha...")

print(f"{'='*80}\n")

new_alpha_ids = await generate_optimized_alphas_from_best(

best_alphas, brain_session, llm_suggestions,

num_new_alphas=alphas_per_iteration

)

if not new_alpha_ids:

print("未能生成新的 Alpha，迭代终止")

break

print(f"\n✓ 成功生成 {len(new_alpha_ids)} 个新 Alpha")

print(f"等待模拟完成后进入下一轮...\n")

# 等待一段时间让模拟完成

wait_time = 30

print(f"等待 {wait_time} 秒让模拟完成...")

await asyncio.sleep(wait_time)

# ===== 最终总结 =====

print(f"\n{'#'*80}")

print(f"# 迭代优化完成")

print(f"# 总迭代轮数: {len(all_iterations_history)}")

print(f"{'#'*80}\n")

# 汇总所有 Alpha

print("汇总所有迭代的 Alpha...")

all_alpha_ids = await get_alphas_by_tag(brain_session, parent_alpha_id)

all_performance_data = []

for alpha_id in all_alpha_ids:

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

all_performance_data.append(perf)

final_performance_df = pd.DataFrame(all_performance_data)

# 选择最终的最佳 Alpha

print("\n选择最终最佳 Alpha...")

final_best_alphas = await select_best_alphas(final_performance_df, selection_criteria, top_n=5)

# 生成最终可视化

print("\n生成最终性能对比图...")

visualize_performance(all_performance_data, parent_alpha_id)

# 导出最终报告

print("\n导出最终报告...")

final_report = await export_alpha_family(

parent_alpha_id,

final_performance_df,

final_best_alphas,

output_file=f'alpha_family_{parent_alpha_id}_final_report.txt'

)

# 返回完整结果

return {

'iterations_history': all_iterations_history,

'final_performance_df': final_performance_df,

'final_best_alphas': final_best_alphas,

'final_report': final_report,

'total_alphas_generated': len(all_alpha_ids),

'total_iterations': len(all_iterations_history)

}

# ==================== 执行完全自动化工作流 ====================

# 运行完全自动化的迭代优化

parent_alpha_id = "kqEnlEA8"  # 替换为你的初始父 Alpha ID

results = await full_auto_iteration_workflow(

parent_alpha_id=parent_alpha_id,

max_iterations=8,              # 最多迭代 8 轮

alphas_per_iteration=5,        # 每轮生成 5 个 Alpha

selection_criteria='balanced',  # 综合平衡选择

min_quality_threshold={        # 质量阈值（达到即停止）

'sharpe': 1.5,

'fitness': 1,

'turnover': 0.15

}

)

# 查看结果

if results:

print(f"\n{'='*80}")

print("最终结果摘要")

print(f"{'='*80}")

print(f"总迭代轮数: {results['total_iterations']}")

print(f"总生成 Alpha 数: {results['total_alphas_generated']}")

print(f"\nTop 5 最佳 Alpha:")

for i, alpha in enumerate(results['final_best_alphas'][:5], 1):

print(f"{i}. {alpha['alpha_id']} - Sharpe: {alpha['sharpe']:.4f}, Fitness: {alpha['fitness']:.4f}")

！！！！最后欢迎在评论区讨论和留言，看到点赞和留言我会开心。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享！！！！

国区大佬越来越多，无私的开源分享精神会让国区越来越强

下个季度回测数量被压缩，一定要用好ai去筛掉无效回测。太感谢了


---

### 技术对话片段 98 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化_36196107273879.md
- **时间**: 6个月前

**提问/主帖背景 (YZ14671)**:
从比赛开始到现在已经过半了，这个过程里面也感受到了熬夜两周搭建智能体的过程，这是这段时间的一个成果，主要难点在提示词优化的边界控制上，以及具体的工作流程上进行反复的打磨，其中大家可以参考wj老师发布的具体的工作流程，在实现的基础上继续进行优化。废话不多说，以下是我的详细的AIAC比赛的notebook笔记，配置好后，即插即用，提醒！！！在使用ai时请注意好的你的钱包。

！！！第一call

import sys

import pandas as pd

import ace_lib as ace

import nest_asyncio

import asyncio

import re

from openai import AsyncOpenAI

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

import httpx

nest_asyncio.apply()

_llm_instance = None

def extract_relevant_operators(alpha_expression, all_operators):

"""提取 Alpha 表达式中实际使用的操作符"""

operator_names = all_operators['name'].tolist()

used_operators = []

for op_name in operator_names:

# 使用正则表达式匹配操作符（后面跟着括号）

if re.search(rf'\b{re.escape(op_name)}\s*\(', alpha_expression):

used_operators.append(op_name)

return all_operators[all_operators['name'].isin(used_operators)]

def extract_relevant_datafields(alpha_expression, all_datafields):

"""提取 Alpha 表达式中实际使用的数据字段"""

field_ids = all_datafields['id'].tolist()

used_fields = []

for field_id in field_ids:

if field_id in alpha_expression:

used_fields.append(field_id)

return all_datafields[all_datafields['id'].isin(used_fields)]

def format_operators_for_prompt(operators_df):

"""将操作符数据格式化为简洁的字符串"""

if operators_df.empty:

return "无使用的操作符"

result = []

for _, row in operators_df.iterrows():

result.append(f"- {row['name']}: {row.get('description', 'N/A')}")

return "\n".join(result)

def format_datafields_for_prompt(datafields_df):

"""将数据字段格式化为简洁的字符串"""

if datafields_df.empty:

return "无使用的数据字段"

result = []

for _, row in datafields_df.iterrows():

result.append(f"- {row['id']}: {row.get('name', 'N/A')} (类型: {row.get('type', 'N/A')})")

return "\n".join(result)

def parse_alpha_expressions(llm_response):

"""

从 LLM 响应中解析出 Alpha 表达式

返回格式: [(expression, description), ...]

"""

lines = llm_response.strip().split('\n')

alphas = []

for line in lines:

line = line.strip()

if not line:

continue

# 尝试分离表达式和注释

if '#' in line:

parts = line.split('#', 1)

expression = parts[0].strip()

description = parts[1].strip() if len(parts) > 1 else ""

else:

expression = line

description = ""

# 简单验证：表达式应该包含括号

if '(' in expression and ')' in expression:

alphas.append((expression, description))

return alphas

# 添加重试装饰器，针对连接错误进行重试

@retry(

stop=stop_after_attempt(5),  # 最多重试5次

wait=wait_exponential(multiplier=1, min=4, max=60),  # 指数退避：4秒、8秒、16秒、32秒、60秒

retry=retry_if_exception_type((httpx.RemoteProtocolError, httpx.ConnectError, httpx.ReadTimeout, ConnectionError)),

reraise=True

)

async def call_llm(prompt, timeout=180):

"""

Interface with the LLM API to process the given prompt.

添加了重试机制和超时设置

"""

try:

# 使用更长的超时时间和自定义 httpx 客户端

http_client = httpx.AsyncClient(

timeout=httpx.Timeout(timeout, connect=30.0),

limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),

transport=httpx.AsyncHTTPTransport(retries=3)

)

client = AsyncOpenAI(

base_url=" [[链接已屏蔽]) ",

api_key="sk-xxxxxxx",

http_client=http_client,

timeout=timeout,

max_retries=3

)

print(f"正在调用 LLM (超时设置: {timeout}秒)...")

response = await client.chat.completions.create(

model="deepseek-reasoner",

messages=[

{"role": "user", "content": prompt}

]

)

print("✓ LLM 调用成功")

return response.choices[0].message.content.strip()

except httpx.ReadTimeout as e:

print(f"✗ LLM 调用超时 ({timeout}秒): {e}")

raise

except (httpx.RemoteProtocolError, httpx.ConnectError) as e:

print(f"✗ 连接错误，准备重试: {e}")

raise

except Exception as e:

print(f"✗ 调用 LLM 时出错: {type(e).__name__}: {e}")

return None

finally:

try:

await http_client.aclose()

except:

pass

async def generate_alpha_description(alpha_id, brain_session, max_retries=3):

"""生成 Alpha 的中文描述，从量化研究员的角度分析其经济学意义"""

for attempt in range(1, max_retries + 1):

try:

print(f"\n尝试生成描述 (第 {attempt}/{max_retries} 次)...")

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

alpha_expression = alpha_details['regular']['code']

print(f"Alpha 表达式: {alpha_expression}")

# 获取所有操作符和数据字段

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

dataset_ids = ['pv87', 'fundamental17']

all_datafields = pd.concat(

[ace.get_datafields(brain_session, region='USA', universe='TOP3000', dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids],

ignore_index=True

)

# 提取相关的操作符和数据字段

relevant_operators = extract_relevant_operators(alpha_expression, regular_operators)

relevant_datafields = extract_relevant_datafields(alpha_expression, all_datafields)

print(f"找到 {len(relevant_operators)} 个相关操作符和 {len(relevant_datafields)} 个相关数据字段")

# 格式化为简洁的字符串

operators_str = format_operators_for_prompt(relevant_operators)

datafields_str = format_datafields_for_prompt(relevant_datafields)

# 从资深量化研究员角度生成 prompt

prompt = f"""你是一位资深量化研究员，请从经济学和金融学的角度分析以下 Alpha 表达式：

Alpha 表达式: {alpha_expression}

使用的操作符:

{operators_str}

使用的数据字段:

{datafields_str}

请用中文提供详细分析，包括：

1. **经济学直觉**：这个 Alpha 试图捕捉什么经济现象或市场行为？

2. **信号逻辑**：为什么这种组合可能产生预测能力？

3. **潜在的市场假设**：这个 Alpha 隐含了哪些关于市场效率或投资者行为的假设？

4. **适用场景**：在什么市场环境下这个信号可能表现更好？

请保持分析简洁但深入，重点关注经济合理性。"""

# 使用更长的超时时间（3分钟）

description = await call_llm(prompt, timeout=180)

if description is None:

if attempt < max_retries:

wait_time = 2 ** attempt  # 指数退避

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

continue

return f"无法生成 Alpha 描述 (已重试 {max_retries} 次): {alpha_expression}"

print("✓ 描述生成成功")

return description.strip()

except Exception as e:

print(f"✗ 生成 Alpha 描述时出错 (第 {attempt} 次): {type(e).__name__}: {e}")

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

else:

return f"生成描述时出错 (已重试 {max_retries} 次): {str(e)}"

return f"生成描述失败: 已达到最大重试次数 ({max_retries})"

async def generate_new_alphas(alpha_description, original_expression, brain_session, max_retries=3):

"""

基于经济学原理生成高质量的 Alpha 变体

允许改变操作符结构以提升因子质量

"""

for attempt in range(1, max_retries + 1):

try:

print(f"\n尝试生成新 Alpha (第 {attempt}/{max_retries} 次)...")

num_alphas = 5

# 获取所有可用的操作符

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

operators_list = regular_operators['name'].tolist()

dataset_ids = ['pv87', 'fundamental17']

data_fields = pd.concat(

[ace.get_datafields(brain_session, region='USA', universe='TOP3000', dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids],

ignore_index=True

)

# 提取数据字段信息

datafields_summary = []

for _, row in data_fields.iterrows():

datafields_summary.append(f"{row['id']} (类型: {row.get('type', 'N/A')}, 名称: {row.get('name', 'N/A')})")

datafields_str = "\n".join(datafields_summary[:150])  # 提供更多字段选择

# 从资深量化研究员角度设计 prompt

prompt = f"""你是一位资深量化研究员，专注于开发具有明确经济学意义的 Alpha 因子。

【原始 Alpha 分析】

表达式: {original_expression}

经济学解读:

{alpha_description}

【可用资源】

操作符（部分）: {', '.join(operators_list[:50])}

可用数据字段:

{datafields_str}

【任务要求】

基于原始 Alpha 的经济学直觉，生成 {num_alphas} 个高质量的变体表达式。

【核心原则 - 作为顶级 BRAIN 顾问】

1. **经济合理性优先**：每个 Alpha 必须有清晰的经济学逻辑，避免纯数据挖掘

2. **低换手率**：优先使用较长的时间窗口（如 ts_decay_linear, ts_mean），避免高频交易信号

3. **稳健性**：使用 winsorize、rank、neutralize 等操作符提升因子稳健性

4. **多样性**：探索不同的数据类别（基本面、情绪、技术指标）以提升金字塔覆盖度

【操作符结构调整指南】

- 可以改变操作符组合以提升因子质量

- 推荐的稳健操作符：ts_decay_linear, ts_mean, ts_rank, winsorize, rank, neutralize

- 避免过度复杂的嵌套（不超过 4-5 层）

- 时间窗口建议：5-60 天（避免过短导致高换手）

【数据字段选择】

- 优先选择基本面数据（earnings, revenue, cash_flow 等）

- 考虑分析师预期数据（consensus, estimate）

- 可以组合不同类型的数据以捕捉多维信号

【语法规范】

- type=MATRIX 字段可直接使用

- type=VECTOR 字段必须用 Vector() 包装

- type=GROUP 字段只能作为 Group 操作符参数

- 确保所有括号匹配，参数格式正确

【输出格式】

请生成 {num_alphas} 个表达式，每行一个，格式如下：

表达式1  # 经济学逻辑说明

表达式2  # 经济学逻辑说明

...

示例格式：

ts_decay_linear(rank(fundamental17_sales_growth), 20)  # 捕捉销售增长的持续性趋势

"""

# 使用更长的超时时间（3分钟）

response = await call_llm(prompt, timeout=180)

if response is None:

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

continue

return f"生成新 Alpha 失败 (已重试 {max_retries} 次)，请检查 LLM 连接。"

print("✓ 新 Alpha 生成成功")

return response.strip()

except Exception as e:

print(f"✗ 生成新 Alpha 时出错 (第 {attempt} 次): {type(e).__name__}: {e}")

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

else:

return f"生成新 Alpha 时出错 (已重试 {max_retries} 次): {str(e)}"

return f"生成新 Alpha 失败: 已达到最大重试次数 ({max_retries})"

async def main():

# 启动 Brain 会话

brain_session = ace.start_session()

# Alpha ID 列表

alpha_ids = ["kqEnlEA8"]

for alpha_id in alpha_ids:

print(f"\n{'='*60}")

print(f"处理 Alpha ID: {alpha_id}")

print(f"{'='*60}")

# 获取原始表达式

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

original_expression = alpha_details['regular']['code']

# 步骤 1: 生成 Alpha 的经济学描述（带重试）

alpha_description = await generate_alpha_description(alpha_id, brain_session, max_retries=3)

if alpha_description and not alpha_description.startswith("无法") and not alpha_description.startswith("生成描述时出错") and not alpha_description.startswith("生成描述失败"):

print(f"\n【Alpha 经济学分析】\n{alpha_description}")

# 步骤 2: 基于经济学原理生成新的高质量 Alpha（带重试）

new_alphas_response = await generate_new_alphas(alpha_description, original_expression, brain_session, max_retries=3)

print(f"\n【生成的高质量 Alpha 变体】\n{new_alphas_response}")

# 步骤 3: 解析生成的 Alpha 表达式

parsed_alphas = parse_alpha_expressions(new_alphas_response)

if not parsed_alphas:

print("\n警告: 未能从 LLM 响应中解析出有效的 Alpha 表达式")

continue

print(f"\n成功解析 {len(parsed_alphas)} 个 Alpha 表达式，开始模拟...")

# 步骤 4: 逐个模拟生成的 Alpha

successful_simulations = []

failed_simulations = []

for idx, (expression, description) in enumerate(parsed_alphas, 1):

print(f"\n--- 模拟 Alpha {idx}/{len(parsed_alphas)} ---")

print(f"表达式: {expression}")

print(f"说明: {description}")

try:

# 生成 Alpha 配置

simulate_data = ace.generate_alpha(

regular=expression,

alpha_type="REGULAR",

region="USA",

universe="TOP3000",

delay=1,

decay=0,

neutralization="INDUSTRY",

truncation=0.08,

pasteurization="ON",

nan_handling="OFF",

unit_handling="VERIFY",

visualization=True

)

# 执行模拟

print("正在提交模拟...")

simulation_result = ace.simulate_single_alpha(brain_session, simulate_data)

child_alpha_id = simulation_result.get('alpha_id')

if child_alpha_id:

print(f"✓ 模拟成功! Alpha ID: {child_alpha_id}")

# 设置 Alpha 属性和标签

full_description = f"【父 Alpha】{alpha_id}\n【经济学逻辑】{description}\n【原始分析】{alpha_description[:200]}..."

ace.set_alpha_properties(

brain_session,

child_alpha_id,

tags=[alpha_id],

regular_desc=full_description

)

print(f"✓ 已设置标签和描述")

successful_simulations.append({

'alpha_id': child_alpha_id,

'expression': expression,

'description': description

})

else:

print(f"✗ 模拟失败: 未返回 Alpha ID")

failed_simulations.append({

'expression': expression,

'reason': '未返回 Alpha ID'

})

except Exception as e:

print(f"✗ 模拟出错: {str(e)}")

failed_simulations.append({

'expression': expression,

'reason': str(e)

})

# 步骤 5: 输出总结

print(f"\n{'='*60}")

print(f"模拟总结 - 父 Alpha: {alpha_id}")

print(f"{'='*60}")

print(f"成功: {len(successful_simulations)} 个")

print(f"失败: {len(failed_simulations)} 个")

if successful_simulations:

print("\n成功的 Alpha:")

for item in successful_simulations:

print(f"  - {item['alpha_id']}: {item['expression'][:60]}...")

if failed_simulations:

print("\n失败的 Alpha:")

for item in failed_simulations:

print(f"  - {item['expression'][:60]}... (原因: {item['reason']})")

else:

print(f"\n{alpha_description}")

print("由于描述生成错误，跳过 Alpha 生成。")

！！！第二call

asyncio.run(main())

！！！第三call

# 检索性能指标、可视化和分析

# 选出冠军alpha

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

from datetime import datetime

# 设置中文字体支持

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']

plt.rcParams['axes.unicode_minus'] = False

async def get_alpha_performance(brain_session, alpha_id):

"""获取 Alpha 的性能指标"""

try:

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

# 提取关键性能指标

is_stats = alpha_details.get('is', {})

performance = {

'alpha_id': alpha_id,

'sharpe': is_stats.get('sharpe'),

'fitness': is_stats.get('fitness'),

'turnover': is_stats.get('turnover'),

'returns': is_stats.get('returns'),

'drawdown': is_stats.get('drawdown'),

'margin': is_stats.get('margin'),

'expression': alpha_details.get('regular', {}).get('code', ''),

'created_at': alpha_details.get('created')

}

return performance

except Exception as e:

print(f"获取 Alpha {alpha_id} 性能时出错: {e}")

return None

async def get_alphas_by_tag(brain_session, tag):

"""通过标签获取 Alpha 家族"""

try:

# 获取用户的所有 IS 阶段 Alphas

response = brain_session.get(

" [[链接已屏蔽]) ",

params={'stage': 'IS', 'limit': 100}

).json()

alphas = response.get('results', [])

# 筛选包含指定标签的 Alphas

tagged_alphas = []

for alpha in alphas:

if tag in alpha.get('tags', []):

tagged_alphas.append(alpha['id'])

print(f"找到 {len(tagged_alphas)} 个带有标签 '{tag}' 的 Alphas")

return tagged_alphas

except Exception as e:

print(f"获取标签 Alphas 时出错: {e}")

return []

def visualize_performance(performance_data, parent_alpha_id):

"""可视化性能对比"""

if not performance_data:

print("没有可用的性能数据")

return

# 过滤掉 None 值

valid_data = [p for p in performance_data if p and all(

p.get(k) is not None for k in ['sharpe', 'fitness', 'turnover']

)]

if not valid_data:

print("没有完整的性能数据可供可视化")

return

df = pd.DataFrame(valid_data)

# 创建 2x2 子图

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

fig.suptitle(f'Alpha 家族性能对比 (父 Alpha: {parent_alpha_id})', fontsize=16, fontweight='bold')

# 1. Sharpe vs Fitness 散点图

ax1 = axes[0, 0]

scatter = ax1.scatter(df['sharpe'], df['fitness'],

c=df['turnover'],cmap='viridis',

s=200, alpha=0.6, edgecolors='black')

ax1.set_xlabel('Sharpe Ratio', fontsize=12)

ax1.set_ylabel('Fitness', fontsize=12)

ax1.set_title('Sharpe vs Fitness (颜色=Turnover)', fontsize=14)

ax1.grid(True, alpha=0.3)

# 添加颜色条

cbar = plt.colorbar(scatter, ax=ax1)

cbar.set_label('Turnover', fontsize=10)

# 标注 Alpha ID

for idx, row in df.iterrows():

ax1.annotate(row['alpha_id'][:6],

(row['sharpe'], row['fitness']),

fontsize=8, alpha=0.7)

# 2. 性能指标柱状图对比

ax2 = axes[0, 1]

x = np.arange(len(df))

width = 0.25

ax2.bar(x - width, df['sharpe'], width, label='Sharpe', alpha=0.8)

ax2.bar(x, df['fitness'], width, label='Fitness', alpha=0.8)

ax2.bar(x + width, df['turnover'], width, label='Turnover', alpha=0.8)

ax2.set_xlabel('Alpha Index', fontsize=12)

ax2.set_ylabel('指标值', fontsize=12)

ax2.set_title('关键指标对比', fontsize=14)

ax2.set_xticks(x)

ax2.set_xticklabels([f"#{i+1}" for i in range(len(df))], fontsize=9)

ax2.legend()

ax2.grid(True, alpha=0.3, axis='y')

# 3. Turnover 分布

ax3 = axes[1, 0]

ax3.barh(range(len(df)), df['turnover'], color='coral', alpha=0.7, edgecolor='black')

ax3.set_yticks(range(len(df)))

ax3.set_yticklabels([aid[:8] for aid in df['alpha_id']], fontsize=9)

ax3.set_xlabel('Turnover', fontsize=12)

ax3.set_title('换手率对比', fontsize=14)

ax3.grid(True, alpha=0.3, axis='x')

# 添加参考线（低换手率阈值）

ax3.axvline(x=0.1, color='green', linestyle='--', linewidth=2, label='低换手阈值 (0.1)')

ax3.legend()

# 4. 综合评分雷达图（选择前3个）

ax4 = axes[1, 1]

if len(df) > 0:

# 归一化数据到 0-1

metrics = ['sharpe', 'fitness', 'returns', 'margin']

available_metrics = [m for m in metrics if m in df.columns and df[m].notna().any()]

if len(available_metrics) >= 3:

# 选择前3个 Alpha

top_alphas = df.nlargest(min(3, len(df)), 'fitness')

angles = np.linspace(0, 2 * np.pi, len(available_metrics), endpoint=False).tolist()

angles += angles[:1]

ax4 = plt.subplot(2, 2, 4, projection='polar')

for idx, row in top_alphas.iterrows():

values = []

for metric in available_metrics:

val = row[metric]

# 简单归一化

max_val = df[metric].max()

min_val = df[metric].min()

if max_val != min_val:

normalized = (val - min_val) / (max_val - min_val)

else:

normalized = 0.5

values.append(normalized)

values += values[:1]

ax4.plot(angles, values, 'o-', linewidth=2, label=row['alpha_id'][:8])

ax4.fill(angles, values, alpha=0.15)

ax4.set_xticks(angles[:-1])

ax4.set_xticklabels(available_metrics, fontsize=10)

ax4.set_ylim(0, 1)

ax4.set_title('Top 3 Alphas 综合对比', fontsize=14, pad=20)

ax4.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

ax4.grid(True)

else:

ax4.text(0.5,0.5,'数据不足，无法生成雷达图',

ha='center', va='center', fontsize=12)

ax4.axis('off')

plt.tight_layout()

plt.show()

return df

async def llm_analyze_results(performance_df, parent_alpha_id, brain_session):

"""LLM 分析实验结果并提出建议"""

if performance_df is None or len(performance_df) == 0:

return "没有可用的性能数据进行分析"

# 准备数据摘要

summary_stats = {

'total_alphas': len(performance_df),

'avg_sharpe': performance_df['sharpe'].mean(),

'max_sharpe': performance_df['sharpe'].max(),

'avg_fitness': performance_df['fitness'].mean(),

'max_fitness': performance_df['fitness'].max(),

'avg_turnover': performance_df['turnover'].mean(),

'min_turnover': performance_df['turnover'].min()

}

# 找出最佳 Alpha

best_alpha = performance_df.loc[performance_df['fitness'].idxmax()]

# 构建分析 prompt

prompt = f"""你是一位资深量化研究员，请分析以下 Alpha 实验结果：

【实验概况】

- 父 Alpha ID: {parent_alpha_id}

- 生成的变体数量: {summary_stats['total_alphas']}

【性能统计】

- 平均 Sharpe: {summary_stats['avg_sharpe']:.4f} (最高: {summary_stats['max_sharpe']:.4f})

- 平均 Fitness: {summary_stats['avg_fitness']:.4f} (最高: {summary_stats['max_fitness']:.4f})

- 平均 Turnover: {summary_stats['avg_turnover']:.4f} (最低: {summary_stats['min_turnover']:.4f})

【最佳 Alpha】

- ID: {best_alpha['alpha_id']}

- Sharpe: {best_alpha['sharpe']:.4f}

- Fitness: {best_alpha['fitness']:.4f}

- Turnover: {best_alpha['turnover']:.4f}

- 表达式: {best_alpha['expression']}

【详细数据】

{performance_df[['alpha_id', 'sharpe', 'fitness', 'turnover', 'returns']].to_string()}

请提供以下分析：

1. **实验成果评估**

- 这批 Alpha 的整体质量如何？

- 是否有突出的表现者？

2. **关键发现**

- 哪些因子组合或数据字段表现最好？

- Sharpe、Fitness、Turnover 之间的权衡如何？

3. **改进方向**

- 基于当前结果，下一轮实验应该关注什么？

- 建议调整哪些参数或尝试哪些新的数据组合？

4. **金字塔策略**

- 从金字塔多样性角度，建议探索哪些新的数据类别或因子逻辑？

请用中文提供简洁但深入的分析。"""

print("\n正在生成 LLM 分析报告...")

analysis = await call_llm(prompt, timeout=180)

return analysis

async def analyze_alpha_family(parent_alpha_id):

"""完整的 Alpha 家族分析流程"""

brain_session = ace.start_session()

print(f"\n{'='*60}")

print(f"Alpha 家族分析 - 父 Alpha: {parent_alpha_id}")

print(f"{'='*60}\n")

# 步骤 1: 通过标签获取 Alpha 家族

print("步骤 1: 检索 Alpha 家族...")

alpha_ids = await get_alphas_by_tag(brain_session, parent_alpha_id)

if not alpha_ids:

print(f"未找到带有标签 '{parent_alpha_id}' 的 Alphas")

return

# 步骤 2: 获取所有 Alpha 的性能数据

print("\n步骤 2: 获取性能指标...")

performance_data = []

for alpha_id in alpha_ids:

print(f"  获取 {alpha_id} 的性能数据...")

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

performance_data.append(perf)

if not performance_data:

print("未能获取任何性能数据")

return

print(f"\n成功获取 {len(performance_data)} 个 Alpha 的性能数据")

# 步骤 3: 可视化性能对比

print("\n步骤 3: 生成可视化图表...")

performance_df = visualize_performance(performance_data, parent_alpha_id)

# 步骤 4: LLM 分析结果

print("\n步骤 4: LLM 分析实验结果...")

analysis = await llm_analyze_results(performance_df, parent_alpha_id, brain_session)

print(f"\n{'='*60}")

print("LLM 分析报告")

print(f"{'='*60}\n")

print(analysis)

# 返回结果供后续使用

return {

'performance_df': performance_df,

'analysis': analysis,

'alpha_ids': alpha_ids

}

# 执行分析

parent_alpha_id = "kqEnlEA8"  # 替换为你的父 Alpha ID

results = await analyze_alpha_family(parent_alpha_id)

！！！第四call

# ==================== Cell 4: 完整的自动迭代优化系统 ====================

# ===== 辅助函数声明 =====

async def get_alphas_by_tag(brain_session, tag):

"""根据标签获取 Alpha ID 列表"""

try:

# 直接使用 Brain API 获取用户的 Alpha 列表

url = f" [[链接已屏蔽]) "

alphas_response = brain_session.get(url).json()

# 过滤出带有指定标签的 Alpha

alpha_ids = []

for alpha in alphas_response.get('results', []):

if tag in alpha.get('tags', []):

alpha_ids.append(alpha['id'])

print(f"找到 {len(alpha_ids)} 个带有标签 '{tag}' 的 Alphas")

return alpha_ids

except Exception as e:

print(f"获取 Alpha 列表失败: {e}")

return []

async def get_alpha_performance(brain_session, alpha_id):

"""获取单个 Alpha 的性能指标"""

try:

alpha_details = ace.get_simulation_result_json(brain_session, alpha_id)

if not alpha_details or 'is' not in alpha_details:

return None

is_data = alpha_details['is']

return {

'alpha_id': alpha_id,

'sharpe': is_data.get('sharpe', 0),

'fitness': is_data.get('fitness', 0),

'returns': is_data.get('returns', 0),

'turnover': is_data.get('turnover', 0),

'margin': is_data.get('margin', 0),

'drawdown': is_data.get('drawdown', 0),

'expression': alpha_details.get('regular', {}).get('code', '')

}

except Exception as e:

print(f"获取 Alpha {alpha_id} 性能失败: {str(e)}")

return None

def visualize_performance(performance_data, parent_alpha_id):

"""可视化性能数据"""

if not performance_data:

print("没有数据可供可视化")

return

df = pd.DataFrame(performance_data)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

fig.suptitle(f'Alpha Family {parent_alpha_id} - Performance Overview', fontsize=16)

# Sharpe vs Fitness

axes[0, 0].scatter(df['sharpe'], df['fitness'], alpha=0.6, s=100)

axes[0, 0].set_xlabel('Sharpe Ratio')

axes[0, 0].set_ylabel('Fitness')

axes[0, 0].set_title('Sharpe vs Fitness')

axes[0, 0].grid(True, alpha=0.3)

# Turnover vs Returns

axes[0, 1].scatter(df['turnover'], df['returns'], alpha=0.6, s=100, c='green')

axes[0, 1].set_xlabel('Turnover')

axes[0, 1].set_ylabel('Returns')

axes[0, 1].set_title('Turnover vs Returns')

axes[0, 1].grid(True, alpha=0.3)

# Sharpe Distribution

axes[1, 0].hist(df['sharpe'], bins=20, alpha=0.7, color='blue', edgecolor='black')

axes[1, 0].set_xlabel('Sharpe Ratio')

axes[1, 0].set_ylabel('Frequency')

axes[1, 0].set_title('Sharpe Distribution')

axes[1, 0].grid(True, alpha=0.3)

# Top Alphas

top_df = df.nlargest(10, 'sharpe')

axes[1, 1].barh(range(len(top_df)), top_df['sharpe'])

axes[1, 1].set_yticks(range(len(top_df)))

axes[1, 1].set_yticklabels([aid[:8] for aid in top_df['alpha_id']])

axes[1, 1].set_xlabel('Sharpe Ratio')

axes[1, 1].set_title('Top 10 Alphas by Sharpe')

axes[1, 1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()

plt.show()

async def select_best_alphas(performance_df, criteria='balanced', top_n=3):

"""选择最佳 Alpha"""

if performance_df.empty:

return []

df = performance_df.copy()

if criteria == 'sharpe':

df = df.sort_values('sharpe', ascending=False)

elif criteria == 'fitness':

df = df.sort_values('fitness', ascending=False)

elif criteria == 'balanced':

# 综合评分: Sharpe * 0.4 + Fitness * 0.3 + (1/Turnover) * 0.3

df['score'] = (df['sharpe'] *0.4+

df['fitness'] *0.3+

(1 / (df['turnover'] + 0.01)) * 0.3)

df = df.sort_values('score', ascending=False)

best = df.head(top_n).to_dict('records')

print(f"\n选出 Top {len(best)} Alpha:")

for i, alpha in enumerate(best, 1):

print(f"{i}. {alpha['alpha_id']}")

print(f"   Sharpe: {alpha['sharpe']:.4f}, Fitness: {alpha['fitness']:.4f}, Turnover: {alpha['turnover']:.4f}")

return best

async def decide_next_iteration(performance_df, current_iteration, max_iterations):

"""决策是否继续迭代"""

if current_iteration >= max_iterations:

return False, "达到最大迭代次数", []

if performance_df.empty:

return False, "没有有效的性能数据", []

# 检查是否有改进

avg_sharpe = performance_df['sharpe'].mean()

avg_fitness = performance_df['fitness'].mean()

if avg_sharpe < 0.5 or avg_fitness < 0.3:

return False, "整体性能过低，建议重新设计策略", []

suggestions = [

"继续优化参数",

"尝试新的数据字段组合",

"调整时间窗口以降低换手率"

]

return True, "性能有提升空间，继续迭代", suggestions

async def llm_analyze_results(performance_df, parent_alpha_id, brain_session):

"""LLM 分析结果"""

if performance_df.empty:

return "没有数据可供分析"

stats = {

'count': len(performance_df),

'avg_sharpe': performance_df['sharpe'].mean(),

'max_sharpe': performance_df['sharpe'].max(),

'avg_fitness': performance_df['fitness'].mean(),

'avg_turnover': performance_df['turnover'].mean()

}

prompt = f"""分析以下 Alpha 家族的性能数据:

Alpha 数量: {stats['count']}

平均 Sharpe: {stats['avg_sharpe']:.4f}

最高 Sharpe: {stats['max_sharpe']:.4f}

平均 Fitness: {stats['avg_fitness']:.4f}

平均 Turnover: {stats['avg_turnover']:.4f}

请提供简洁的分析（3-5 句话）:

1. 整体表现评价

2. 主要优势

3. 需要改进的方面

"""

response = await call_llm(prompt, timeout=60)

return response if response else "分析失败"

async def llm_iteration_suggestions(performance_df, iteration, best_alphas):

"""LLM 生成迭代优化建议"""

if not best_alphas:

return "没有最佳 Alpha 可供分析"

top_alpha = best_alphas[0]

prompt = f"""当前是第 {iteration} 轮迭代。

最佳 Alpha 表现:

- 表达式: {top_alpha['expression']}

- Sharpe: {top_alpha['sharpe']:.4f}

- Fitness: {top_alpha['fitness']:.4f}

- Turnover: {top_alpha['turnover']:.4f}

请提供 3-5 条具体的优化建议，每条建议应该:

1. 针对具体问题

2. 给出可操作的改进方向

3. 简洁明了（每条 1-2 句话）

"""

response = await call_llm(prompt, timeout=60)

return response if response else "建议生成失败"

async def export_alpha_family(parent_alpha_id, performance_df, best_alphas, output_file):

"""导出 Alpha 家族报告"""

with open(output_file, 'w', encoding='utf-8') as f:

f.write(f"Alpha Family Report: {parent_alpha_id}\n")

f.write(f"Generated: {datetime.now()}\n")

f.write("="*80 + "\n\n")

f.write(f"Total Alphas: {len(performance_df)}\n")

f.write(f"Average Sharpe: {performance_df['sharpe'].mean():.4f}\n")

f.write(f"Average Fitness: {performance_df['fitness'].mean():.4f}\n")

f.write(f"Average Turnover: {performance_df['turnover'].mean():.4f}\n\n")

f.write("Top 5 Best Alphas:\n")

f.write("-"*80 + "\n")

for i, alpha in enumerate(best_alphas[:5], 1):

f.write(f"\n{i}. Alpha ID: {alpha['alpha_id']}\n")

f.write(f"   Expression: {alpha['expression']}\n")

f.write(f"   Sharpe: {alpha['sharpe']:.4f}\n")

f.write(f"   Fitness: {alpha['fitness']:.4f}\n")

f.write(f"   Turnover: {alpha['turnover']:.4f}\n")

print(f"✓ 报告已导出到: {output_file}")

return output_file

# ===== 主要函数 =====

async def generate_optimized_alphas_from_best(best_alphas, brain_session, optimization_suggestions, num_new_alphas=5):

"""基于最佳 Alpha 和优化建议生成新一轮 Alpha"""

print(f"\n{'='*60}")

print(f"基于最佳 Alpha 生成新一轮优化变体")

print(f"{'='*60}\n")

if not best_alphas or len(best_alphas) == 0:

print("没有可用的最佳 Alpha")

return []

# 选择表现最好的 Alpha 作为基础

base_alpha = best_alphas[0]

base_expression = base_alpha['expression']

base_alpha_id = base_alpha['alpha_id']

print(f"基础 Alpha ID: {base_alpha_id}")

print(f"基础表达式: {base_expression}")

print(f"性能指标: Sharpe={base_alpha['sharpe']:.4f}, Fitness={base_alpha['fitness']:.4f}, Turnover={base_alpha['turnover']:.4f}\n")

# 获取操作符和数据字段

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

operators_list = regular_operators['name'].tolist()

dataset_ids = ['pv87', 'fundamental17']

data_fields = pd.concat([

ace.get_datafields(brain_session,region='USA',universe='TOP3000',

dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids

], ignore_index=True)

datafields_summary = [

f"{row['id']} (类型: {row.get('type','N/A')}, 名称: {row.get('name','N/A')})"

for _, row in data_fields.iterrows()

]

datafields_str = "\n".join(datafields_summary[:150])

# 构建优化 prompt

prompt = f"""你是一位资深量化研究员，正在进行 Alpha 因子的迭代优化。

【上一轮最佳 Alpha】

表达式: {base_expression}

性能: Sharpe={base_alpha['sharpe']:.4f}, Fitness={base_alpha['fitness']:.4f}, Turnover={base_alpha['turnover']:.4f}

【优化建议】

{optimization_suggestions}

【可用资源】

操作符（部分）: {', '.join(operators_list[:50])}

可用数据字段:

{datafields_str}

【优化任务】

基于上述最佳 Alpha 和优化建议，生成 {num_new_alphas} 个改进版本的 Alpha 表达式。

【优化策略】

1. **保留优势**: 保持最佳 Alpha 中表现好的核心逻辑

2. **针对性改进**: 根据优化建议调整参数或操作符

3. **渐进式变化**: 每次只改变 1-2 个关键要素，避免过度变异

4. **多样化探索**: 在保持核心逻辑的同时，尝试不同的实现方式

【具体改进方向】

- 如果 Turnover 过高: 增加时间窗口参数（如 20→40），使用 ts_decay_linear

- 如果 Sharpe 不足: 尝试组合更多数据字段，增强信号强度

- 如果 Fitness 偏低: 添加 winsorize、rank、neutralize 提升稳健性

- 探索新的数据类别: 基本面、分析师预期、情绪指标等

【语法规范】

- type=MATRIX 字段可直接使用

- type=VECTOR 字段必须用 Vector() 包装

- type=GROUP 字段只能作为 Group 操作符参数

- 确保所有括号匹配，参数格式正确

【输出格式】

请生成 {num_new_alphas} 个表达式，每行一个，格式如下：

表达式1  # 改进说明

表达式2  # 改进说明

...

示例：

ts_decay_linear(rank(fundamental17_sales_growth), 40)  # 增加时间窗口从20到40，降低换手率

"""

print("正在调用 LLM 生成优化后的 Alpha...")

response = await call_llm(prompt, timeout=180)

if response is None:

print("✗ LLM 调用失败")

return []

print("✓ LLM 生成成功\n")

# 解析生成的 Alpha 表达式

parsed_alphas = parse_alpha_expressions(response)

if not parsed_alphas:

print("警告: 未能解析出有效的 Alpha 表达式")

return []

print(f"成功解析 {len(parsed_alphas)} 个 Alpha 表达式，开始模拟...\n")

# 模拟新生成的 Alpha

new_alpha_ids = []

successful_simulations = []

failed_simulations = []

for idx, (expression, description) in enumerate(parsed_alphas, 1):

print(f"--- 模拟优化 Alpha {idx}/{len(parsed_alphas)} ---")

print(f"表达式: {expression}")

print(f"说明: {description}")

try:

simulate_data = ace.generate_alpha(

regular=expression,

alpha_type="REGULAR",

region="USA",

universe="TOP3000",

delay=1,

decay=0,

neutralization="INDUSTRY",

truncation=0.08,

pasteurization="ON",

nan_handling="OFF",

unit_handling="VERIFY",

visualization=True

)

print("正在提交模拟...")

simulation_result = ace.simulate_single_alpha(brain_session, simulate_data)

child_alpha_id = simulation_result.get('alpha_id')

if child_alpha_id:

print(f"✓ 模拟成功! Alpha ID: {child_alpha_id}")

# 设置标签（使用原始父 Alpha ID）

parent_tag = base_alpha.get('parent_alpha_id', base_alpha_id)

full_description = f"【父 Alpha】{parent_tag}\n【优化自】{base_alpha_id}\n【改进说明】{description}"

ace.set_alpha_properties(

brain_session,

child_alpha_id,

tags=[parent_tag],

regular_desc=full_description

)

print(f"✓ 已设置标签: {parent_tag}\n")

new_alpha_ids.append(child_alpha_id)

successful_simulations.append({

'alpha_id': child_alpha_id,

'expression': expression,

'description': description

})

else:

print(f"✗ 模拟失败: 未返回 Alpha ID\n")

failed_simulations.append({

'expression': expression,

'reason': '未返回 Alpha ID'

})

except Exception as e:

print(f"✗ 模拟出错: {str(e)}\n")

failed_simulations.append({

'expression': expression,

'reason': str(e)

})

# 输出总结

print(f"{'='*60}")

print(f"本轮优化模拟总结")

print(f"{'='*60}")

print(f"成功: {len(successful_simulations)} 个")

print(f"失败: {len(failed_simulations)} 个")

if successful_simulations:

print("\n成功的 Alpha:")

for item in successful_simulations:

print(f"  - {item['alpha_id']}: {item['expression'][:60]}...")

if failed_simulations:

print("\n失败的 Alpha:")

for item in failed_simulations:

print(f"  - {item['expression'][:60]}... (原因: {item['reason']})")

return new_alpha_ids

asyncdeffull_auto_iteration_workflow(parent_alpha_id,max_iterations=5,alphas_per_iteration=5,

selection_criteria='balanced', min_quality_threshold=None):

"""完全自动化的迭代优化工作流"""

brain_session = ace.start_session()

print(f"\n{'#'*80}")

print(f"# 完全自动化 Alpha 迭代优化工作流")

print(f"# 初始父 Alpha: {parent_alpha_id}")

print(f"# 最大迭代次数: {max_iterations}")

print(f"# 每轮生成数量: {alphas_per_iteration}")

print(f"# 选择标准: {selection_criteria}")

print(f"{'#'*80}\n")

# 设置默认质量阈值

if min_quality_threshold is None:

min_quality_threshold = {

'sharpe': 1.5,

'fitness': 1,

'turnover': 0.15

}

all_iterations_history = []

current_parent_id = parent_alpha_id

for iteration in range(1, max_iterations + 1):

print(f"\n{'='*80}")

print(f"第 {iteration}/{max_iterations} 轮迭代")

print(f"{'='*80}\n")

iteration_start_time = datetime.now()

# ===== 步骤 1: 获取当前 Alpha 家族 =====

print("步骤 1: 检索 Alpha 家族...")

alpha_ids = await get_alphas_by_tag(brain_session, current_parent_id)

if not alpha_ids:

if iteration == 1:

print(f"第一轮未找到 Alpha，请先运行初始 Alpha 生成")

return None

else:

print("未找到新的 Alpha，使用上一轮数据")

break

print(f"找到 {len(alpha_ids)} 个 Alpha\n")

# ===== 步骤 2: 获取性能数据 =====

print("步骤 2: 获取性能指标...")

performance_data = []

for alpha_id in alpha_ids:

print(f"  获取 {alpha_id}...")

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

perf['parent_alpha_id'] = current_parent_id

performance_data.append(perf)

if not performance_data:

print("未能获取任何性能数据")

break

performance_df = pd.DataFrame(performance_data)

print(f"成功获取 {len(performance_df)} 个 Alpha 的性能数据\n")

# ===== 步骤 3: 可视化 =====

print("步骤 3: 生成可视化图表...")

visualize_performance(performance_data, current_parent_id)

# ===== 步骤 4: 选择最佳 Alpha =====

print("\n步骤 4: 选择最佳 Alpha...")

best_alphas = await select_best_alphas(performance_df, selection_criteria, top_n=3)

if not best_alphas:

print("未能选择出最佳 Alpha")

break

# ===== 步骤 5: 检查是否达到质量阈值 =====

print("\n步骤 5: 检查质量阈值...")

top_alpha = best_alphas[0]

quality_check = (

top_alpha['sharpe'] >= min_quality_threshold['sharpe'] and

top_alpha['fitness'] >= min_quality_threshold['fitness'] and

top_alpha['turnover'] <= min_quality_threshold['turnover']

)

if quality_check:

print(f"✓ 达到质量阈值!")

print(f"  Sharpe: {top_alpha['sharpe']:.4f} >= {min_quality_threshold['sharpe']}")

print(f"  Fitness: {top_alpha['fitness']:.4f} >= {min_quality_threshold['fitness']}")

print(f"  Turnover: {top_alpha['turnover']:.4f} <= {min_quality_threshold['turnover']}")

should_continue = False

reason = "达到质量阈值，优化成功"

suggestions = []

else:

# ===== 步骤 6: 决策是否继续迭代 =====

print("\n步骤 6: 迭代决策...")

should_continue, reason, suggestions = await decide_next_iteration(

performance_df, iteration, max_iterations

)

# ===== 步骤 7: LLM 分析 =====

print("\n步骤 7: LLM 分析结果...")

llm_analysis = await llm_analyze_results(performance_df, current_parent_id, brain_session)

print(f"\n【LLM 分析】\n{llm_analysis}\n")

# ===== 步骤 8: 生成优化建议 =====

print("\n步骤 8: 生成优化建议...")

llm_suggestions = await llm_iteration_suggestions(performance_df, iteration, best_alphas)

print(f"\n【LLM 优化建议】\n{llm_suggestions}\n")

# 保存本轮数据

iteration_data = {

'iteration': iteration,

'parent_alpha_id': current_parent_id,

'alpha_count': len(alpha_ids),

'performance_df': performance_df,

'best_alphas': best_alphas,

'should_continue': should_continue,

'reason': reason,

'suggestions': suggestions,

'llm_analysis': llm_analysis,

'llm_suggestions': llm_suggestions,

'duration': (datetime.now() - iteration_start_time).total_seconds()

}

all_iterations_history.append(iteration_data)

# ===== 决策点: 是否继续迭代 =====

if not should_continue:

print(f"\n{'='*80}")

print(f"✓ 迭代结束: {reason}")

print(f"{'='*80}\n")

break

# ===== 步骤 9: 生成下一轮 Alpha =====

if iteration < max_iterations:

print(f"\n步骤 9: 生成下一轮优化 Alpha...")

print(f"{'='*80}\n")

new_alpha_ids = await generate_optimized_alphas_from_best(

best_alphas, brain_session, llm_suggestions,

num_new_alphas=alphas_per_iteration

)

if not new_alpha_ids:

print("未能生成新的 Alpha，迭代终止")

break

print(f"\n✓ 成功生成 {len(new_alpha_ids)} 个新 Alpha")

print(f"等待模拟完成后进入下一轮...\n")

# 等待一段时间让模拟完成

wait_time = 30

print(f"等待 {wait_time} 秒让模拟完成...")

await asyncio.sleep(wait_time)

# ===== 最终总结 =====

print(f"\n{'#'*80}")

print(f"# 迭代优化完成")

print(f"# 总迭代轮数: {len(all_iterations_history)}")

print(f"{'#'*80}\n")

# 汇总所有 Alpha

print("汇总所有迭代的 Alpha...")

all_alpha_ids = await get_alphas_by_tag(brain_session, parent_alpha_id)

all_performance_data = []

for alpha_id in all_alpha_ids:

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

all_performance_data.append(perf)

final_performance_df = pd.DataFrame(all_performance_data)

# 选择最终的最佳 Alpha

print("\n选择最终最佳 Alpha...")

final_best_alphas = await select_best_alphas(final_performance_df, selection_criteria, top_n=5)

# 生成最终可视化

print("\n生成最终性能对比图...")

visualize_performance(all_performance_data, parent_alpha_id)

# 导出最终报告

print("\n导出最终报告...")

final_report = await export_alpha_family(

parent_alpha_id,

final_performance_df,

final_best_alphas,

output_file=f'alpha_family_{parent_alpha_id}_final_report.txt'

)

# 返回完整结果

return {

'iterations_history': all_iterations_history,

'final_performance_df': final_performance_df,

'final_best_alphas': final_best_alphas,

'final_report': final_report,

'total_alphas_generated': len(all_alpha_ids),

'total_iterations': len(all_iterations_history)

}

# ==================== 执行完全自动化工作流 ====================

# 运行完全自动化的迭代优化

parent_alpha_id = "kqEnlEA8"  # 替换为你的初始父 Alpha ID

results = await full_auto_iteration_workflow(

parent_alpha_id=parent_alpha_id,

max_iterations=8,              # 最多迭代 8 轮

alphas_per_iteration=5,        # 每轮生成 5 个 Alpha

selection_criteria='balanced',  # 综合平衡选择

min_quality_threshold={        # 质量阈值（达到即停止）

'sharpe': 1.5,

'fitness': 1,

'turnover': 0.15

}

)

# 查看结果

if results:

print(f"\n{'='*80}")

print("最终结果摘要")

print(f"{'='*80}")

print(f"总迭代轮数: {results['total_iterations']}")

print(f"总生成 Alpha 数: {results['total_alphas_generated']}")

print(f"\nTop 5 最佳 Alpha:")

for i, alpha in enumerate(results['final_best_alphas'][:5], 1):

print(f"{i}. {alpha['alpha_id']} - Sharpe: {alpha['sharpe']:.4f}, Fitness: {alpha['fitness']:.4f}")

！！！！最后欢迎在评论区讨论和留言，看到点赞和留言我会开心。

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的分享！！！！

国区大佬越来越多，无私的开源分享精神会让国区越来越强

下个季度回测数量被压缩，一定要用好ai去筛掉无效回测。太感谢了


---

### 技术对话片段 99 (原帖: 在wq平台, 我们应该通过mcp提供什么工具经验分享)
- **原帖链接**: [Commented] 在wq平台 我们应该通过mcp提供什么工具经验分享.md
- **时间**: 3个月前

**提问/主帖背景 (WL27618)**:
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 100 (原帖: 在wq平台, 我们应该通过mcp提供什么工具经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 在wq平台 我们应该通过mcp提供什么工具经验分享_38652207939735.md
- **时间**: 3个月前

**提问/主帖背景 (WL27618)**:
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 101 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 102 (原帖: PnL = ∑(Robustness * Creativity))
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢大佬的无私分享，太厉害了
=======================================
========================================
===========================================


---

### 技术对话片段 103 (原帖: 数据字段创建比赛首次培训)
- **原帖链接**: [Commented] 数据字段创建比赛首次培训.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
Introduction to Data Creation Challenge 2026

[[链接已屏蔽])

本周四中国时间晚九点

**顾问 MS51256 (Rank 28) 的解答与建议**:
参赛参赛，这下连数据字段都要自己创造了，又能探索新事物了

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 104 (原帖: 数据字段创建比赛首次培训)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 数据字段创建比赛首次培训_38609982663191.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
Introduction to Data Creation Challenge 2026

[[链接已屏蔽])

本周四中国时间晚九点

**顾问 MS51256 (Rank 28) 的解答与建议**:
参赛参赛，这下连数据字段都要自己创造了，又能探索新事物了

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 105 (原帖: 新人小小小心得)
- **原帖链接**: [Commented] 新人小小小心得.md
- **时间**: 1年前

**提问/主帖背景 (LZ84152)**:
作为新人一开始真的使用三阶段代码无脑交，没有太多思考，后来发现无脑提交的alpha质量高的不多，但又不太想为了交而交，索性开始逛起了论坛，就来说说论坛对于新人来说比较重要的一些小tip。
一、alpha 提交基础规则

对于vf0.5的新人，不知道如何评价alpha质量，可以查看这篇文章

[日赚90刀💵作为新人，我是怎么样从value factor 0.5升到0.99的？ – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 日赚90刀作为新人我是怎么样从value factor 05升到099的经验分享.md)

有时候有些alpha的其他内容表现都很好，但就是turnover比较高，margin较低，可以查看

[如何提高流水率？– WorldQuant 大脑](/hc/en-us/articles/20251419309719-How-to-improve-Turnover)

***删除 [对于check，要记住check只有三个槽，同时每天四个alpha提交完后，check无法运行。所以要一直check就不能一次交满4个alpha，可以选择每天更新前提前半小时交最后一个。]***

二、效率提升经验总结

即插即用的多线程提交，把它放在multi_simulate_dynamic中修改一下就好，不会直接两个代码放gpt，要他改为多线程一般也就好了。

```
import concurrent.futureswith concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:    # 当队列未空 或 存在正在运行的任务时，持续循环    while not task_queue.empty() or futures:        # 当活动任务数小于10且队列中还有任务时持续提交        while not task_queue.empty() and len(futures) < 8:            try:                task = task_queue.get(timeout=2)            except Empty:                break            # 提交任务并加入列表            times = datetime.datetime.now()            args.log_id.Info(f"processing task: {now_id}")            future = executor.submit(simulate_and_check, task, args, s, now_id)            futures.append(future)            task_queue.task_done()            now_id += 1        # 等待任意一个任务完成        if futures:            done, not_done = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)            futures = list(not_done)
```

二、模板的选择

对于如何找alpha，可以看下面两个链接，一个英文和一个中文的alpha模板合集：

[【Alpha Template Collections】- Continuously Update – WorldQuant BRAIN](../顾问 CH36668 (Rank 76)/[Commented] 【Alpha Template Collections】- Continuously UpdatePinnedAlpha Template.md)

[如何找到更多alpha的思考（新手进阶篇）系列 - 第三篇：论坛内的模版 – WorldQuant BRAIN](../顾问 KZ79256 (Rank 21)/[Commented] 如何找到更多alpha的思考新手进阶篇系列 - 第三篇论坛内的模版.md)

我自己先择差不多抛弃了三阶段方式，主要是现在更新点亮dines区域的数据集点亮规则变了，现在主要尝试论坛中的模板加套一个二阶段，二阶段可以是分组，也可以是trade_when。之后就是尝试更多的一些模板的可能性。

**顾问 MS51256 (Rank 28) 的解答与建议**:
对于check，要记住check只有三个槽，同时每天四个alpha提交完后，check无法运行。所以要一直check就不能一次交满4个alpha，可以选择每天更新前提前半小时交最后一个。
有这个说法吗
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 106 (原帖: 新人小小小心得)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新人小小小心得_31747867191191.md
- **时间**: 1年前

**提问/主帖背景 (LZ84152)**:
作为新人一开始真的使用三阶段代码无脑交，没有太多思考，后来发现无脑提交的alpha质量高的不多，但又不太想为了交而交，索性开始逛起了论坛，就来说说论坛对于新人来说比较重要的一些小tip。
一、alpha 提交基础规则

对于vf0.5的新人，不知道如何评价alpha质量，可以查看这篇文章

[日赚90刀💵作为新人，我是怎么样从value factor 0.5升到0.99的？ – WorldQuant BRAIN]([L2] 日赚90刀作为新人我是怎么样从value factor 05升到099的经验分享_28856000657303.md)

有时候有些alpha的其他内容表现都很好，但就是turnover比较高，margin较低，可以查看

[如何提高流水率？– WorldQuant 大脑](/hc/en-us/articles/20251419309719-How-to-improve-Turnover)

***删除 [对于check，要记住check只有三个槽，同时每天四个alpha提交完后，check无法运行。所以要一直check就不能一次交满4个alpha，可以选择每天更新前提前半小时交最后一个。]***

二、效率提升经验总结

即插即用的多线程提交，把它放在multi_simulate_dynamic中修改一下就好，不会直接两个代码放gpt，要他改为多线程一般也就好了。

```
import concurrent.futureswith concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:    # 当队列未空 或 存在正在运行的任务时，持续循环    while not task_queue.empty() or futures:        # 当活动任务数小于10且队列中还有任务时持续提交        while not task_queue.empty() and len(futures) < 8:            try:                task = task_queue.get(timeout=2)            except Empty:                break            # 提交任务并加入列表            times = datetime.datetime.now()            args.log_id.Info(f"processing task: {now_id}")            future = executor.submit(simulate_and_check, task, args, s, now_id)            futures.append(future)            task_queue.task_done()            now_id += 1        # 等待任意一个任务完成        if futures:            done, not_done = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)            futures = list(not_done)
```

二、模板的选择

对于如何找alpha，可以看下面两个链接，一个英文和一个中文的alpha模板合集：

[【Alpha Template Collections】- Continuously Update – WorldQuant BRAIN]([L2] 【Alpha Template Collections】- Continuously UpdatePinnedAlpha Template_24472586368279.md)

[如何找到更多alpha的思考（新手进阶篇）系列 - 第三篇：论坛内的模版 – WorldQuant BRAIN]([L2] 如何找到更多alpha的思考新手进阶篇系列 - 第三篇论坛内的模版_27758310278295.md)

我自己先择差不多抛弃了三阶段方式，主要是现在更新点亮dines区域的数据集点亮规则变了，现在主要尝试论坛中的模板加套一个二阶段，二阶段可以是分组，也可以是trade_when。之后就是尝试更多的一些模板的可能性。

**顾问 MS51256 (Rank 28) 的解答与建议**:
对于check，要记住check只有三个槽，同时每天四个alpha提交完后，check无法运行。所以要一直check就不能一次交满4个alpha，可以选择每天更新前提前半小时交最后一个。
有这个说法吗
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---

### 技术对话片段 107 (原帖: 新增的免费ai api 大模型提供商，【七牛云注册就送300万token】根本用不完)
- **原帖链接**: [Commented] 新增的免费ai api 大模型提供商【七牛云注册就送300万token】根本用不完.md
- **时间**: 3个月前

**提问/主帖背景 (MX83967)**:
最近发现了个新的新的免费ai api 大模型提供商，【七牛云注册就送300万token】根本用不完
七牛云新用户注册免费赠送大模型 api 300万token,各大常用的大模型平台都能免费使用，是第三方大模型 api 提供商，集成了很多国内外常见的大模型服务平台，一次注册就可以使用多个大模型，根本用不完，很适合金融量化因子挖掘任务

 
> [!NOTE] [图片 OCR 识别内容]
> 实时推理全系列模型 3OOW (新用户体验
> 包)


这是我获得的300万token 体验包，根本就用不完


> [!NOTE] [图片 OCR 识别内容]
> AI 大模型推理服务
> 提供多个顶级闭源和开源大模型
> 兼容 OpenAl API 和 Anthropic APIC


gpt claude,kimi,deepseek等常用大模型免费使用
 
> [!NOTE] [图片 OCR 识别内容]
> 立即体验 Al 推理大模型
> 竹
> Kimi
> 5gel
> q咖
> 豆包大幞型
> deepseek
> 文山大瘼{
> HINIHAX
> N


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 108 (原帖: 新增的免费ai api 大模型提供商，【七牛云注册就送300万token】根本用不完)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新增的免费ai api 大模型提供商【七牛云注册就送300万token】根本用不完_38251309633303.md
- **时间**: 3个月前

**提问/主帖背景 (MX83967)**:
最近发现了个新的新的免费ai api 大模型提供商，【七牛云注册就送300万token】根本用不完
七牛云新用户注册免费赠送大模型 api 300万token,各大常用的大模型平台都能免费使用，是第三方大模型 api 提供商，集成了很多国内外常见的大模型服务平台，一次注册就可以使用多个大模型，根本用不完，很适合金融量化因子挖掘任务

 
> [!NOTE] [图片 OCR 识别内容]
> 实时推理全系列模型 3OOW (新用户体验
> 包)


这是我获得的300万token 体验包，根本就用不完


> [!NOTE] [图片 OCR 识别内容]
> AI 大模型推理服务
> 提供多个顶级闭源和开源大模型
> 兼容 OpenAl API 和 Anthropic APIC


gpt claude,kimi,deepseek等常用大模型免费使用
 
> [!NOTE] [图片 OCR 识别内容]
> 立即体验 Al 推理大模型
> 竹
> Kimi
> 5gel
> q咖
> 豆包大幞型
> deepseek
> 文山大瘼{
> HINIHAX
> N


**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================


---

### 技术对话片段 109 (原帖: 增量下载数据download_data(flag_increment=True))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md
- **时间**: 1 year ago

**提问/主帖背景 (KZ79256)**:
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


**顾问 MS51256 (Rank 28) 的解答与建议**:
有一个问题想请教一下，最近Power Pool Alpha 期间 只检测自己的因子相关性是不是<0.5.如何修改代码实现批量的获取网页上的alpha id来本地批量检测ppa 相关性,最近都是网页上找一些合适的去手动复制 alpha id去检验，随着提交越来越多，相关性越来越难过，手动复制耗费的时间也越来越久了。代码能力不足只能耗费更多的时间来弥补了。
====================================================================
最后祝愿楼主早日value factor 1.0  genius 晋升为Grand Master!!!!
====================================================================


---

### 技术对话片段 110 (原帖: 本地存储alpha信息的数据库表设计，附源码代码优化)
- **原帖链接**: [Commented] 本地存储alpha信息的数据库表设计附源码代码优化.md
- **时间**: 1年前

**提问/主帖背景 (TQ88961)**:
为提高效率，我们需要将远端alpha信息拉到本地数据库。由于远端alpha信息是嵌套json文件，存放到本地数据库时，需要展开字段。以下是一种设计，采用sqlalchemy来定义。

```
Base = declarative_base()class AlphaFactor(Base):    __tablename__ = 'alpha_factors'      uid = Column(Integer, Sequence('uid_seq'), primary_key=True, autoincrement=True)    id = Column(String, unique=True)    type = Column(String)      author = Column(String)    settings_instrument_type = Column(String)    settings_region = Column(String)    settings_universe = Column(String)    settings_delay = Column(Integer)    settings_decay = Column(Integer)    settings_neutralization = Column(String)    settings_truncation = Column(Float)    settings_pasteurization = Column(String)    settings_unit_handling = Column(String)    settings_nan_handling = Column(String)    settings_max_trade = Column(String)    settings_language = Column(String)    settings_visualization = Column(Boolean)    regular_code = Column(String)    regular_description = Column(String, nullable=True)    regular_operator_count = Column(Integer)    date_created = Column(DateTime)    date_submitted = Column(DateTime, nullable=True)    date_modified = Column(DateTime)    name = Column(String)    favorite = Column(Boolean)    hidden = Column(Boolean)    color = Column(String, nullable=True)    category = Column(String, nullable=True)    tags = Column(String)    classifications = Column(String)    grade = Column(String, nullable=True)    stage = Column(String)    status = Column(String)    is_pnl = Column(Integer)    is_book_size = Column(Integer)    is_long_count = Column(Integer)    is_short_count = Column(Integer)    is_turnover = Column(Float)    is_returns = Column(Float)    is_drawdown = Column(Float)    is_margin = Column(Float)    is_sharpe = Column(Float)    is_fitness = Column(Float)    is_start_date = Column(String)    is_investability_pnl = Column(Integer)    is_investability_book_size = Column(Integer)    is_investability_long_count = Column(Integer)    is_investability_short_count = Column(Integer)    is_investability_turnover = Column(Float)    is_investability_returns = Column(Float)    is_investability_drawdown = Column(Float)    is_investability_margin = Column(Float)    is_investability_fitness = Column(Float)    is_investability_sharpe = Column(Float)    is_risk_neutralized_pnl = Column(Integer)    is_risk_neutralized_book_size = Column(Integer)    is_risk_neutralized_long_count = Column(Integer)    is_risk_neutralized_short_count = Column(Integer)    is_risk_neutralized_turnover = Column(Float)    is_risk_neutralized_returns = Column(Float)    is_risk_neutralized_drawdown = Column(Float)    is_risk_neutralized_margin = Column(Float)    is_risk_neutralized_fitness = Column(Float)    is_risk_neutralized_sharpe = Column(Float)    check_low_sharpe_result = Column(String)    check_low_sharpe_limit = Column(Float)    check_low_sharpe_value = Column(Float)    check_low_fitness_result = Column(String)    check_low_fitness_limit = Column(Float)    check_low_fitness_value = Column(Float)    check_low_turnover_result = Column(String)    check_low_turnover_limit = Column(Float)    check_low_turnover_value = Column(Float)    check_high_turnover_result = Column(String)    check_high_turnover_limit = Column(Float)    check_high_turnover_value = Column(Float)    check_concentrated_weight_result = Column(String)    check_concentrated_weight_date = Column(String)    check_concentrated_weight_limit = Column(Float)    check_concentrated_weight_value = Column(Float)    check_self_correlation_result = Column(String)    check_data_diversity_result = Column(String)    check_prod_correlation_result = Column(String)    check_regular_submission_result = Column(String)    check_matches_competition_result = Column(String)    check_matches_competition_competitions = Column(String)    check_low_2y_sharpe_result = Column(String)    check_low_2y_sharpe_value = Column(Float)    check_low_2y_sharpe_limit = Column(Float)    check_matches_pyramid_result = Column(String)    check_matches_pyramid_multiplier = Column(Float)    check_matches_pyramid_pyramids = Column(String)    check_matches_themes_result = Column(String)    check_matches_themes_themes = Column(String)    check_power_pool_correlation_result = Column(String)    origin = Column(Text)    def __repr__(self):       return f"<AlphaFactor(uid={self.uid}, id='{self.id}', name='{self.name}', stage='{self.stage}')>"def create_db_table(db_path="sqlite:///alpha_factors.db"):    """创建数据库表"""    if not db_path.startswith("sqlite:///"):        db_path = "sqlite:///" + db_path.replace("\\", "/")        # 创建数据库引擎    engine = create_engine(db_path, echo=False)        # 创建表    Base.metadata.create_all(engine)    print(f"数据库表已创建于 {db_path}")
```

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，一直想存进数据库中，一直没思路


---

### 技术对话片段 111 (原帖: 本地存储alpha信息的数据库表设计，附源码代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 本地存储alpha信息的数据库表设计附源码代码优化_31570875902103.md
- **时间**: 1年前

**提问/主帖背景 (TQ88961)**:
为提高效率，我们需要将远端alpha信息拉到本地数据库。由于远端alpha信息是嵌套json文件，存放到本地数据库时，需要展开字段。以下是一种设计，采用sqlalchemy来定义。

```
Base = declarative_base()class AlphaFactor(Base):    __tablename__ = 'alpha_factors'      uid = Column(Integer, Sequence('uid_seq'), primary_key=True, autoincrement=True)    id = Column(String, unique=True)    type = Column(String)      author = Column(String)    settings_instrument_type = Column(String)    settings_region = Column(String)    settings_universe = Column(String)    settings_delay = Column(Integer)    settings_decay = Column(Integer)    settings_neutralization = Column(String)    settings_truncation = Column(Float)    settings_pasteurization = Column(String)    settings_unit_handling = Column(String)    settings_nan_handling = Column(String)    settings_max_trade = Column(String)    settings_language = Column(String)    settings_visualization = Column(Boolean)    regular_code = Column(String)    regular_description = Column(String, nullable=True)    regular_operator_count = Column(Integer)    date_created = Column(DateTime)    date_submitted = Column(DateTime, nullable=True)    date_modified = Column(DateTime)    name = Column(String)    favorite = Column(Boolean)    hidden = Column(Boolean)    color = Column(String, nullable=True)    category = Column(String, nullable=True)    tags = Column(String)    classifications = Column(String)    grade = Column(String, nullable=True)    stage = Column(String)    status = Column(String)    is_pnl = Column(Integer)    is_book_size = Column(Integer)    is_long_count = Column(Integer)    is_short_count = Column(Integer)    is_turnover = Column(Float)    is_returns = Column(Float)    is_drawdown = Column(Float)    is_margin = Column(Float)    is_sharpe = Column(Float)    is_fitness = Column(Float)    is_start_date = Column(String)    is_investability_pnl = Column(Integer)    is_investability_book_size = Column(Integer)    is_investability_long_count = Column(Integer)    is_investability_short_count = Column(Integer)    is_investability_turnover = Column(Float)    is_investability_returns = Column(Float)    is_investability_drawdown = Column(Float)    is_investability_margin = Column(Float)    is_investability_fitness = Column(Float)    is_investability_sharpe = Column(Float)    is_risk_neutralized_pnl = Column(Integer)    is_risk_neutralized_book_size = Column(Integer)    is_risk_neutralized_long_count = Column(Integer)    is_risk_neutralized_short_count = Column(Integer)    is_risk_neutralized_turnover = Column(Float)    is_risk_neutralized_returns = Column(Float)    is_risk_neutralized_drawdown = Column(Float)    is_risk_neutralized_margin = Column(Float)    is_risk_neutralized_fitness = Column(Float)    is_risk_neutralized_sharpe = Column(Float)    check_low_sharpe_result = Column(String)    check_low_sharpe_limit = Column(Float)    check_low_sharpe_value = Column(Float)    check_low_fitness_result = Column(String)    check_low_fitness_limit = Column(Float)    check_low_fitness_value = Column(Float)    check_low_turnover_result = Column(String)    check_low_turnover_limit = Column(Float)    check_low_turnover_value = Column(Float)    check_high_turnover_result = Column(String)    check_high_turnover_limit = Column(Float)    check_high_turnover_value = Column(Float)    check_concentrated_weight_result = Column(String)    check_concentrated_weight_date = Column(String)    check_concentrated_weight_limit = Column(Float)    check_concentrated_weight_value = Column(Float)    check_self_correlation_result = Column(String)    check_data_diversity_result = Column(String)    check_prod_correlation_result = Column(String)    check_regular_submission_result = Column(String)    check_matches_competition_result = Column(String)    check_matches_competition_competitions = Column(String)    check_low_2y_sharpe_result = Column(String)    check_low_2y_sharpe_value = Column(Float)    check_low_2y_sharpe_limit = Column(Float)    check_matches_pyramid_result = Column(String)    check_matches_pyramid_multiplier = Column(Float)    check_matches_pyramid_pyramids = Column(String)    check_matches_themes_result = Column(String)    check_matches_themes_themes = Column(String)    check_power_pool_correlation_result = Column(String)    origin = Column(Text)    def __repr__(self):       return f"<AlphaFactor(uid={self.uid}, id='{self.id}', name='{self.name}', stage='{self.stage}')>"def create_db_table(db_path="sqlite:///alpha_factors.db"):    """创建数据库表"""    if not db_path.startswith("sqlite:///"):        db_path = "sqlite:///" + db_path.replace("\\", "/")        # 创建数据库引擎    engine = create_engine(db_path, echo=False)        # 创建表    Base.metadata.create_all(engine)    print(f"数据库表已创建于 {db_path}")
```

**顾问 MS51256 (Rank 28) 的解答与建议**:
感谢分享，一直想存进数据库中，一直没思路


---

### 技术对话片段 112 (原帖: 过滤掉 Python 内置函数和关键字)
- **原帖链接**: [Commented] 用python ast提取表达式中operator和datafield的方法代码优化.md
- **时间**: 1年前

**提问/主帖背景 (WL27618)**:
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
非常有用的功能，可以实现对op field的统计  从而知道哪些被使用的而去使用别的数据或者操作符
===========================================================================================================================================================================================================================================================


---

### 技术对话片段 113 (原帖: 过滤掉 Python 内置函数和关键字)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 用python ast提取表达式中operator和datafield的方法代码优化_30870358077463.md
- **时间**: 1年前

**提问/主帖背景 (WL27618)**:
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

**顾问 MS51256 (Rank 28) 的解答与建议**:
非常有用的功能，可以实现对op field的统计  从而知道哪些被使用的而去使用别的数据或者操作符
===========================================================================================================================================================================================================================================================


---

### 技术对话片段 114 (原帖: 缓解当前Check和提交速度慢的几点建议)
- **原帖链接**: [Commented] 缓解当前Check和提交速度慢的几点建议.md
- **时间**: 1年前

**提问/主帖背景 (KH94146)**:
由于当前IQC和Power Pool比赛同时在USA Region进行等其它原因，近期收到很多关于回测和提交较慢的问题。Tech正在积极的解决这个问题，在当前给大家一些建议如下

1.使用代码进行提交，并使用多次retry。可在顾问论坛中搜索submit关键字或者在ACE Lib中下载相关代码。

2. 避免过多的check，因为提交前还是需要进check，由于执行了大量的check任务会导致限流从而让submit超时。

3.通常早上9点前为non peak hour，提交会更快

**顾问 MS51256 (Rank 28) 的解答与建议**:
感觉 6 7 点人最少，这时候交大概半小时就交完。


---

### 技术对话片段 115 (原帖: 缓解当前Check和提交速度慢的几点建议)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 缓解当前Check和提交速度慢的几点建议_30909184976023.md
- **时间**: 1年前

**提问/主帖背景 (KH94146)**:
由于当前IQC和Power Pool比赛同时在USA Region进行等其它原因，近期收到很多关于回测和提交较慢的问题。Tech正在积极的解决这个问题，在当前给大家一些建议如下

1.使用代码进行提交，并使用多次retry。可在顾问论坛中搜索submit关键字或者在ACE Lib中下载相关代码。

2. 避免过多的check，因为提交前还是需要进check，由于执行了大量的check任务会导致限流从而让submit超时。

3.通常早上9点前为non peak hour，提交会更快

**顾问 MS51256 (Rank 28) 的解答与建议**:
感觉 6 7 点人最少，这时候交大概半小时就交完。


---
