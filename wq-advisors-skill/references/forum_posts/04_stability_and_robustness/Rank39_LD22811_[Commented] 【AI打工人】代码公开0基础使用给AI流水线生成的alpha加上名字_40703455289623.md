# 【AI打工人】代码公开，0基础使用，给AI流水线生成的alpha加上名字

- **链接**: https://support.worldquantbrain.com[Commented] 【AI打工人】代码公开0基础使用给AI流水线生成的alpha加上名字_40703455289623.md
- **作者**: WW11235
- **发布时间/热度**: 1个月前, 得票: 11

## 帖子正文

说明：

我是0基础不懂经济学及python的新手顾问，在论坛获取了AI打工人后开始尝试。结果生成了一页的未命名的alpha，发现二次分析很困难，也搞不清楚哪个是哪个。

于是我利用AI在代码中进行了修改。新生成的alpha就有了自己的名字和tag。

修改前


> [!NOTE] [图片 OCR 识别内容]
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.00
> 0.009
> 0.009
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 1.82
> 7.6496
> 8.5896
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.66
> 29.139
> 16.65%
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.63
> 28.509
> 24.46%
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.60
> 27.349
> 40.389
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.66
> 28.899
> 18.769
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.62
> 28.239
> 40.269
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.66
> 29.269
> 18.349
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.67
> 29.439
> 15.229
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.63
> 28.389
> 24.259
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.64
> 28.349
> 19.529
> anonymous
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> 0.60
> 27.399
> 40.28%


修改后：


> [!NOTE] [图片 OCR 识别内容]
> model77_USA_ai
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> -0.22
> -1.159
> 3.51%
> ai_generat
> model77_USA_ai
> Regular
> UNSUBMITTED
> Fast Expression
> 05/24/2026 EDT
> USA
> TOP3000
> -0.96
> -5.169
> 3.329
> ai_genera


公开代码供大家参考。减少修改时间。

# Alpha 自动命名修改日志

# 方案：在 _save_result 中同步命名

# 修改目标: 回测成功的 alpha 自动设置 name={dataset_id}_{region}_ai, tags=["ai_generated", ...]

================================================================================

## 文件 1: brain-orchestrator/scripts/vendor/batch_simulator.py

================================================================================

### 修改 1.1: BatchSimulator.__init__ 增加 dataset_id / region 参数

# 位置: 第 301 行

# 原代码（打 # 注释掉）:

#     def __init__(self, session: ace_lib.SingleSession, output_csv="alpha_simulation_status.csv", cancel_check=None, on_batch_start=None, on_result_saved=None):

# 新代码:

def __init__(self, session: ace_lib.SingleSession, output_csv="alpha_simulation_status.csv",

cancel_check=None, on_batch_start=None, on_result_saved=None,

dataset_id=None, region=None):

--------------------------------------------------------------------------------

### 修改 1.2: BatchSimulator.__init__ 体内保存 dataset_id / region

# 位置: 第 307 行之后（self.completed_fingerprints = set() 之后）

# 原代码: 无（新增）

# 新代码（插入在 self.completed_fingerprints = set() 下一行）:

self.dataset_id = dataset_id or ""

self.region = region or ""

--------------------------------------------------------------------------------

### 修改 1.3: _save_result 方法增加命名逻辑

# 位置: 第 521-539 行

# 原代码（整段替换）:

#     def _save_result(self, result_dict: dict):

#         """Thread-safe write to CSV."""

#         write_ok = False

#         with self.csv_lock:

#             try:

#                 normalized = {key: result_dict.get(key, "") for key in self.csv_columns}

#                 df = pd.DataFrame([normalized], columns=self.csv_columns)

#

#                 # Append to CSV, create header if file doesn't exist

#                 write_header = not pd.io.common.file_exists(self.output_csv)

#                 df.to_csv(self.output_csv, mode='a', header=write_header, index=False)

#                 write_ok = True

#             except Exception as e:

#                 logger.error(f"Failed to write result to CSV: {e}")

#         if write_ok and self._on_result_saved:

#             try:

#                 self._on_result_saved()

#             except Exception:

#                 pass

# 新代码:

def _save_result(self, result_dict: dict):

"""Thread-safe write to CSV."""

write_ok = False

with self.csv_lock:

try:

normalized = {key: result_dict.get(key, "") for key in self.csv_columns}

df = pd.DataFrame([normalized], columns=self.csv_columns)

# Append to CSV, create header if file doesn't exist

write_header = not pd.io.common.file_exists(self.output_csv)

df.to_csv(self.output_csv, mode='a', header=write_header, index=False)

write_ok = True

except Exception as e:

logger.error(f"Failed to write result to CSV: {e}")

# ---- Alpha auto-naming on successful simulation ----

status = str(result_dict.get("status", "")).upper().strip()

alpha_id = result_dict.get("alpha_id")

if (status in {"COMPLETED", "COMPLETE"}

and alpha_id

and self.dataset_id

and self.region):

try:

name = f"{self.dataset_id}_{self.region}_ai"

ace_lib.set_alpha_properties(

self.session,

str(alpha_id),

name=name,

tags=["ai_generated", self.dataset_id, self.region]

)

logger.info(f"Named alpha {alpha_id} as '{name}'")

except Exception as e:

logger.warning(f"Failed to set alpha properties for {alpha_id}: {e}")

# ---- End alpha auto-naming ----

if write_ok and self._on_result_saved:

try:

self._on_result_saved()

except Exception:

pass

================================================================================

## 文件 2: brain-orchestrator/stage_simulate.py

================================================================================

### 修改 2.1: simulate_idea 函数签名增加 config 参数

# 位置: 第 122-130 行

# 原代码（打 # 注释掉）:

# def simulate_idea(

#     alpha_list_path: Path,

#     output_csv: Path,

#     session,

#     sim_multi_slots: int = 2,

#     cancel_check=None,

#     progress_callback=None,

#     location_callback=None,

# ) -> dict:

# 新代码:

def simulate_idea(

alpha_list_path: Path,

output_csv: Path,

session,

sim_multi_slots: int = 2,

cancel_check=None,

progress_callback=None,

location_callback=None,

config: dict = None,

) -> dict:

--------------------------------------------------------------------------------

### 修改 2.2: BatchSimulator 实例化时传入 dataset_id / region

# 位置: 第 163-169 行

# 原代码（打 # 注释掉）:

#     simulator = BatchSimulator(

#         session,

#         output_csv=str(output_csv),

#         cancel_check=cancel_check,

#         on_batch_start=location_callback,

#         on_result_saved=_on_batch_done,

#     )

# 新代码:

simulator = BatchSimulator(

session,

output_csv=str(output_csv),

cancel_check=cancel_check,

on_batch_start=location_callback,

on_result_saved=_on_batch_done,

dataset_id=(config or {}).get("dataset_id"),

region=(config or {}).get("region"),

)

================================================================================

## 文件 3: brain-orchestrator/pipeline_runner.py

================================================================================

### 修改 3.1: simulate_idea 调用处传入 config

# 位置: 第 548-556 行

# 原代码（打 # 注释掉）:

#                 summary = simulate_idea(

#                     alpha_list_path=alpha_list_path,

#                     output_csv=output_csv,

#                     session=session,

#                     sim_multi_slots=sim_multi_slots,

#                     cancel_check=cancel_fn,

#                     progress_callback=_progress,

#                     location_callback=_on_location,

#                 )

# 新代码:

summary = simulate_idea(

alpha_list_path=alpha_list_path,

output_csv=output_csv,

session=session,

sim_multi_slots=sim_multi_slots,

cancel_check=cancel_fn,

progress_callback=_progress,

location_callback=_on_location,

config=self.config,

)

---

## 讨论与评论 (6)

### 评论 #1 (作者: WL58980, 时间: 1个月前)

Tag一旦生成就无法删除，建议只生成name。

============================================================================

Study hard — quality over quantity, no room for mediocrity. Cherish every learning opportunity, stay focused, and learn from the experts. Keep pushing!

============================================================================

---

### 评论 #2 (作者: FF45555, 时间: 1个月前)

感谢大佬的分享，用这个能够很直观的看出alpha的父子关系，交了一个之后，其余的相关alpha都可以不用查sc和pc了，基本就是一窝端了，极大的节省了查pc的额度。

====================================================================================== # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% # sys.setrecursionlimit(α∞) # PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。

---

### 评论 #3 (作者: FF65210, 时间: 1个月前)

好思路，但是我并不用ai流水线，可以在app模板回测的alpha上面用吗，我还不太理解怎么用这段代码。

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

### 评论 #4 (作者: LL83568, 时间: 1个月前)

谢谢分享~

---

### 评论 #5 (作者: 顾问 LD22811 (Rank 39), 时间: 1个月前)

感谢分享

---

### 评论 #6 (作者: BW14163, 时间: 1个月前)

很有想法的一次尝试：在网页端筛选alpha，通过为alpha命名的方式做一个简单的筛选。

**********************************
紧跟大佬的脚步，每天坚持至少学一个知识点，尽量不混信号，不过拟合。
Prioritize diversity, strong margin, low correlation, stable diversification; strictly control costs and overfitting.
**********************************

---

