# [skills小工具]将数据库中数据封装成skills，用于AI工作流

- **链接**: https://support.worldquantbrain.com[Commented] [skills小工具]将数据库中数据封装成skills用于AI工作流_39215982466071.md
- **作者**: CZ39633
- **发布时间/热度**: 3个月前, 得票: 60

## 帖子正文

这几天随着Gemini pro的额度大砍，导致不得不想着怎么节省tokens和上下文。随后在与小虎哥的提点下得知采用将数据封装成skills来节省上下文和tokens，而刚好前几天我发了怎么将从网页拉取的数据存储到数据库的帖子（ [[L2] 将从网页拉取的数据存储到数据库_39183798681239.md]([L2] 将从网页拉取的数据存储到数据库_39183798681239.md)  ）

因此，在此基础上写了一个brain_alpha_dataset_onefile.py。这个文件是一个“一键把数据库字段数据转成本地技能包并提供本地查询入口”的单文件工具。会自动生成SKILL.md（技能使用说明文件，告诉AI 什么时候调用、怎么调用、返回什么），manifest.json（技能包元信息文件，告诉系统这个技能包叫什么、入口在哪。），index.json（轻量索引文件，存 region+dataset 的映射和字段总数，用于超快计数查询。）和各个地区的数据集中数据字段ID与描述文件。


> [!NOTE] [图片 OCR 识别内容]
> Mgent powering dow. Goodbyel
> Interaction Swmy
> Sesslon DD:
> 656136b9 UR4b N8bC 8630-585391836160
> Tool Calls:
> 2(12*00
> SUCeeSs Rate:
> 100,睢
> User Ngreanent:
> 100.0 (2 revlewed)
> Prforwama
> 4121
> Te:
> 23
> yent Activ:
> 叫B
> NPI Tine:
> 15.q (32 8
> Tool Tiwe
> 31.35 (6.2
> Nodel
> 肥
> Iout Tokens
> Cache Reads
> Output Tokens
> gemini-3 Flash previem
> 9,91
> 78,149
> 278
> Savings Mighlight; T8,N9 (57.骝)
> 吁 iput tokens #ere Served from the cache
> reducin costs


这个是采用skills后的tokens量


> [!NOTE] [图片 OCR 识别内容]
> Iteractiom Say
> Sessinn
> 皿:
> 19f37a19-2826-4957-8706-4463e0a6269
> Tool Call:
> 吾(]5e0)
> SICCeas Rat:
> 10.咄
> User R1?:
> 100.覆 (5 revieed)
> Drforla
> 眨11 T1:
> GT
> Aent Actio;
>  2
> #r ~:
> 32.45 (-。]
> Tool Tiu:
> 9.8 (19.骝)
> I》
> Rers
> IIput Tokens
> Cache Rads
> Output Tokens
> gemini-3 flash previem
> 125,695
> 118,575
> 4


这个是采用mcp的tokens消耗量。

由此可见，采用skills的tokens消耗量比用mcp的tokens消耗量少。

随后在上述操作结束后，我分别用了Gemini ，iflow,qwen的模型分别进行上述操作，我发现这个节省tokens量与模型的能力，SKILL.md中的描述息息相关。模型越好，节省的tokens量越多。这是因为性能较差模型在 skills 路径里走了错误调用链 （读大文件、grep、shell、反复试错），把 token 放大了。所以用mcp获取数字段和skills获取数据字段各有千秋，skills更适合用于性能较好的模型，mcp能用于各种模型，而skills还有待提高，后续我也会不断进行优化。同时也可以自行对SKILL.md进行修改，可能表现会更好。

最后，在此十分感谢小虎哥（顾问 SD17531 (Rank 15)）这位大帅哥和希望各位可以点点赞.

代码如下：

import argparse

import json

import os

import re

import shutil

import statistics

import sys

import time

import unittest

from dataclasses import dataclass

from datetime import datetime

from pathlib import Path

from typing import Any, Dict, Iterable, List, Optional, Tuple

import pymysql

RECORD_FIELDS = [

"id",

"description",

"dataset_id",

"dataset_name",

"category_id",

"category_name",

"subcategory_id",

"subcategory_name",

"region",

"delay",

"universe",

"type",

"dateCoverage",

"coverage",

"userCount",

"alphaCount",

"pyramidMultiplier",

"themes",

]

DEFAULT_REGIONS = ["USA", "EUR", "ASI", "IND", "GLB"]

_INDEX_CACHE: Dict[str, Dict[str, Any]] = {}

_INDEX_MTIME: Dict[str, float] = {}

# 使用说明：

# 1) 只想“一键运行”时，修改下面 USER_RUN_CONFIG 即可

# 2) 保存后直接运行：python brain_alpha_dataset_onefile.py

# 3) 高级用法仍可继续使用命令行子命令（pipeline/lookup/benchmark/run-tests）

USER_RUN_CONFIG = {

# 数据库连接信息

"db_host": "127.0.0.1",

"db_port": 3306,

"db_user": "root",

"db_password": "xxx",

"db_name": "xxx",

# 源表名

"table": "data_fields",

# 需要导出的地区

"regions": ["USA", "EUR", "ASI", "IND", "GLB"],

# full=全量，incremental=增量

"mode": "full",

# 增量模式起点（mode=incremental 时生效）

"since": "1970-01-01 00:00:00",

# DB 拉取批大小

"fetch_size": 5000,

# 构建输出根目录（会自动生成 brain-alpha-dataset 技能包）

# Windows 路径请用 raw 字符串 r"..." 或把 \ 改成 /

# 例如：r"C:\Users\.gemini\skills" 或 "C:/Users/.gemini/skills"

"build_root": str(Path(r"C:\Users\.gemini\skills")),

# 增量模式状态文件

"state_file": str(Path.cwd() / ".brain_alpha_dataset_state.json"),

# 可选：如果不走数据库，填本地 JSONL 文件路径；留空则从数据库导出

"source_jsonl": "",

# 是否每次都重写技能说明文件和 manifest（False=仅首次生成）

"overwrite_skill_files": False,

# 是否把每个字段的 markdown 文件也复制到 skills 目录（False 更省空间和 token）

"include_markdown_files_in_skill": False,

# 单次返回字段上限，避免一次返回上千字段导致 token 暴涨

"max_fields_per_call": 200,

}

class DatasetError(Exception):

pass

class ConfigError(DatasetError):

pass

class DataNotFoundError(DatasetError):

pass

@dataclass

class PipelineArtifacts:

exported_jsonl: Path

markdown_root: Path

skill_root: Path

manifest_path: Path

skill_file: Path

index_path: Path

def now_ts() -> str:

return datetime.now().strftime("%Y%m%d_%H%M%S")

def safe_name(text: str) -> str:

text = text.strip()

text = re.sub(r"[\/:*?\"<>|]+", "_", text)

return text or "unknown"

def parse_themes(value: Any) -> List[Any]:

if value is None:

return []

if isinstance(value, list):

return value

if isinstance(value, str):

s = value.strip()

if not s:

return []

try:

parsed = json.loads(s)

return parsed if isinstance(parsed, list) else []

except json.JSONDecodeError:

return []

return []

def connect_db(args: argparse.Namespace):

# 连接 MySQL，供导出阶段使用

return pymysql.connect(

host=args.db_host,

port=args.db_port,

user=args.db_user,

password=args.db_password,

database=args.db_name,

charset="utf8mb4",

cursorclass=pymysql.cursors.DictCursor,

autocommit=False,

)

def build_sql(mode: str, table: str, regions: List[str], since: str) -> Tuple[str, Tuple[Any, ...]]:

# 生成全量/增量 SQL

cols = ", ".join(RECORD_FIELDS + ["created_at"])

base = f"SELECT {cols} FROM {table}"

where_parts: List[str] = []

params: List[Any] = []

if regions:

placeholders = ",".join(["%s"] * len(regions))

where_parts.append(f"region IN ({placeholders})")

params.extend(regions)

if mode == "incremental":

where_parts.append("created_at >= %s")

params.append(since)

where_clause = ""

if where_parts:

where_clause = " WHERE " + " AND ".join(where_parts)

sql = f"{base}{where_clause} ORDER BY region, dataset_id, id"

return sql, tuple(params)

def export_from_db(args: argparse.Namespace, output_jsonl: Path) -> Tuple[int, Optional[str]]:

# 把数据库记录导出成 JSONL（每行一条），并返回总行数和最新时间

conn = connect_db(args)

total = 0

max_created_at: Optional[str] = None

sql, params = build_sql(args.mode, args.table, args.regions, args.since)

print(f"[pipeline] 开始导出: mode={args.mode}, table={args.table}, regions={args.regions}")

output_jsonl.parent.mkdir(parents=True, exist_ok=True)

with conn:

with conn.cursor() as cur:

cur.execute(sql, params)

with output_jsonl.open("w", encoding="utf-8") as f:

while True:

rows = cur.fetchmany(args.fetch_size)

if not rows:

break

for row in rows:

normalized = normalize_row(row)

f.write(json.dumps(normalized, ensure_ascii=False) + "\n")

total += 1

if total % 20000 == 0:

print(f"[pipeline] 已导出 {total} 条...")

c = row.get("created_at")

if c is not None:

c_text = str(c)

if max_created_at is None or c_text > max_created_at:

max_created_at = c_text

print(f"[pipeline] 导出完成，总计 {total} 条")

return total, max_created_at

def normalize_row(row: Dict[str, Any]) -> Dict[str, Any]:

# 标准化一条记录，兼容扁平结构和嵌套结构

normalized = {k: row.get(k) for k in RECORD_FIELDS}

dataset_obj = row.get("dataset") if isinstance(row.get("dataset"), dict) else {}

category_obj = row.get("category") if isinstance(row.get("category"), dict) else {}

subcategory_obj = row.get("subcategory") if isinstance(row.get("subcategory"), dict) else {}

if not normalized.get("dataset_id"):

normalized["dataset_id"] = dataset_obj.get("id")

if not normalized.get("dataset_name"):

normalized["dataset_name"] = dataset_obj.get("name")

if not normalized.get("category_id"):

normalized["category_id"] = category_obj.get("id")

if not normalized.get("category_name"):

normalized["category_name"] = category_obj.get("name")

if not normalized.get("subcategory_id"):

normalized["subcategory_id"] = subcategory_obj.get("id")

if not normalized.get("subcategory_name"):

normalized["subcategory_name"] = subcategory_obj.get("name")

normalized["description"] = (normalized.get("description") or "").strip()

normalized["dataset_name"] = (normalized.get("dataset_name") or "Unknown").strip() or "Unknown"

normalized["category_name"] = (normalized.get("category_name") or "Unknown").strip() or "Unknown"

normalized["subcategory_name"] = (normalized.get("subcategory_name") or "").strip()

normalized["dataset_id"] = (normalized.get("dataset_id") or "").strip()

normalized["category_id"] = (normalized.get("category_id") or "").strip()

normalized["subcategory_id"] = (normalized.get("subcategory_id") or "").strip()

normalized["region"] = (normalized.get("region") or "").strip()

normalized["themes"] = parse_themes(normalized.get("themes"))

return normalized

def load_jsonl(path: Path) -> List[Dict[str, Any]]:

if not path.exists():

raise DataNotFoundError(f"JSONL 文件不存在: {path}")

records: List[Dict[str, Any]] = []

with path.open("r", encoding="utf-8", errors="replace") as f:

for i, line in enumerate(f, start=1):

s = line.strip()

if not s:

continue

try:

obj = json.loads(s)

except json.JSONDecodeError as e:

raise DatasetError(f"JSONL 解析失败 line={i}: {e}") from e

records.append(normalize_row(obj))

return records

def render_markdown(record: Dict[str, Any]) -> str:

# 把单条字段元数据渲染成 Markdown 文本

themes_text = json.dumps(record.get("themes", []), ensure_ascii=False)

lines = [

f"# {record.get('id', '')}",

"",

f"- region: {record.get('region', '')}",

f"- dataset_id: {record.get('dataset_id', '')}",

f"- dataset_name: {record.get('dataset_name', '')}",

f"- category_id: {record.get('category_id', '')}",

f"- category_name: {record.get('category_name', '')}",

f"- subcategory_id: {record.get('subcategory_id', '')}",

f"- subcategory_name: {record.get('subcategory_name', '')}",

f"- delay: {record.get('delay', None)}",

f"- universe: {record.get('universe', '')}",

f"- type: {record.get('type', '')}",

f"- dateCoverage: {record.get('dateCoverage', None)}",

f"- coverage: {record.get('coverage', None)}",

f"- userCount: {record.get('userCount', None)}",

f"- alphaCount: {record.get('alphaCount', None)}",

f"- pyramidMultiplier: {record.get('pyramidMultiplier', None)}",

f"- themes: {themes_text}",

"",

"## Description",

"",

str(record.get("description", "")),

"",

]

return "\n".join(lines)

def write_markdown_tree(records: List[Dict[str, Any]], markdown_root: Path) -> Path:

# 按 region/dataset_id 两级目录写入 markdown，并生成索引文件 index.json

dataset_buckets: Dict[Tuple[str, str], List[Dict[str, str]]] = {}

desc_root = markdown_root / "desc"

for rec in records:

region = safe_name(str(rec.get("region", "") or "UNKNOWN"))

dataset_id = safe_name(str(rec.get("dataset_id", "") or "UNKNOWN"))

rec_id = safe_name(str(rec.get("id", "") or "unknown"))

target_dir = markdown_root / region / dataset_id

target_dir.mkdir(parents=True, exist_ok=True)

md_path = target_dir / f"{rec_id}.md"

md_path.write_text(render_markdown(rec), encoding="utf-8")

desc_dir = desc_root / region / dataset_id

desc_dir.mkdir(parents=True, exist_ok=True)

(desc_dir / f"{rec_id}.txt").write_text(str(rec.get("description", "")), encoding="utf-8")

dataset_buckets.setdefault((region, dataset_id), []).append(

{"id": rec.get("id", ""), "description": str(rec.get("description", ""))}

)

compact_root = markdown_root / "compact"

index: Dict[str, Dict[str, Dict[str, Any]]] = {}

counts: Dict[str, Dict[str, int]] = {}

for (region, dataset_id), fields in dataset_buckets.items():

compact_dir = compact_root / region

compact_dir.mkdir(parents=True, exist_ok=True)

compact_file = compact_dir / f"{dataset_id}.jsonl"

with compact_file.open("w", encoding="utf-8") as f:

for item in fields:

f.write(json.dumps(item, ensure_ascii=False) + "\n")

rel = str(compact_file.relative_to(markdown_root)).replace("\", "/")

index.setdefault(region, {})[dataset_id] = {

"count": len(fields),

"compact_file": rel,

"desc_dir": f"desc/{region}/{dataset_id}",

}

counts.setdefault(region, {})[dataset_id] = len(fields)

index_path = markdown_root / "index.json"

index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

counts_path = markdown_root / "counts.json"

counts_path.write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")

return index_path

def write_manifest(skill_root: Path) -> Path:

# 生成技能包 manifest，声明包名和入口函数

manifest = {

"name": "brain-alpha-dataset",

"version": "1.0.0",

"entrypoint": "brain_alpha_dataset_onefile.py:skill_entry",

"description": "Local Brain alpha dataset package with zero-token local lookup.",

"regions": DEFAULT_REGIONS,

}

path = skill_root / "manifest.json"

path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

return path

def write_skill_md(skill_root: Path) -> Path:

# 生成技能包内部说明文件（给模型判断何时调用）

text = """---

name: "brain-alpha-dataset"

description: "Reads local markdown field metadata for target region/dataset. Invoke when user asks to build or optimize alpha on a specified region+dataset."

---

# Brain Alpha Dataset

Use local skill data first when the user asks to build/optimize alpha on a specific region + dataset.

Do not call remote MCP when local data exists.

## Workflow Rule

Always resolve target region first, then fetch only the target dataset_id under that region.

Do not load unrelated regions or datasets.

## Input

- region

- dataset_id

- optional keyword

## Retrieval Rule

1. Read `data/index.json` and locate `region -> dataset_id`.

2. For "how many/count/数量" queries, return count directly from `index.json` (no folder scan, no shell).

3. For field list queries, read `data/compact/<region>/<dataset_id>.jsonl`.

4. For single-field description queries, read `data/desc/<region>/<dataset_id>/<field_id>.txt` directly.

5. If needed, call `field-desc` (exact id lookup) instead of scanning all lines.

6. If local data is missing, run pipeline to bootstrap local data from DB.

7. Never call MCP if local skill data exists.

8. Return paged fields (`limit/offset`) to minimize tokens.

## Output

- fields: `[{id, description}, ...]`

- count: `<int>` for count-only queries

- id + description for single-field queries

- total: `<int>` total fields in this dataset

- offset/limit/has_more: pagination metadata

- token_cost=0

"""

p = skill_root / "SKILL.md"

p.write_text(text, encoding="utf-8")

return p

def copy_markdown_to_skill(markdown_root: Path, skill_root: Path, include_markdown_files: bool) -> Path:

# 把 markdown 目录复制到技能包 data 目录

data_root = skill_root / "data"

if data_root.exists():

shutil.rmtree(data_root)

data_root.mkdir(parents=True, exist_ok=True)

for path in markdown_root.rglob("*"):

if path.is_file():

rel = path.relative_to(markdown_root)

keep_small_index = rel.name in {"index.json", "counts.json"}

keep_compact = rel.parts and rel.parts[0] == "compact"

keep_desc = rel.parts and rel.parts[0] == "desc"

if not include_markdown_files and not (keep_small_index or keep_compact or keep_desc):

continue

target = data_root / rel

target.parent.mkdir(parents=True, exist_ok=True)

target.write_bytes(path.read_bytes())

return data_root / "index.json"

def parse_instruction(text: str) -> Tuple[Optional[str], Optional[str]]:

# Extract region and dataset_id from natural language

region_match = re.search(r"\b(USA|EUR|ASI|IND|GLB)\b", text.upper())

dataset_match = re.search(r"dataset[\s:=_-]*([a-zA-Z0-9_-]+)", text, flags=re.IGNORECASE)

region = region_match.group(1) if region_match else None

dataset = dataset_match.group(1) if dataset_match else None

if dataset is None:

candidates = re.findall(r"\b([a-zA-Z]+[0-9]+[a-zA-Z0-9_-]*)\b", text)

upper_regions = set(DEFAULT_REGIONS)

for token in candidates:

if token.upper() not in upper_regions:

dataset = token

break

return region, dataset

def parse_field_id(text: str) -> Optional[str]:

tokens = re.findall(r"\b([a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)+)\b", text)

if not tokens:

return None

for t in tokens:

low = t.lower()

if "dataset" in low:

continue

if low in {"region", "description", "field"}:

continue

return t

return tokens[0]

def _ensure_skill_data(skill_root: Path) -> None:

data_index = skill_root / "data" / "index.json"

if data_index.exists():

return

bootstrap_args = argparse.Namespace(

cmd="pipeline",

db_host=USER_RUN_CONFIG["db_host"],

db_port=USER_RUN_CONFIG["db_port"],

db_user=USER_RUN_CONFIG["db_user"],

db_password=USER_RUN_CONFIG["db_password"],

db_name=USER_RUN_CONFIG["db_name"],

table=USER_RUN_CONFIG["table"],

regions=USER_RUN_CONFIG["regions"],

mode=USER_RUN_CONFIG["mode"],

since=USER_RUN_CONFIG["since"],

fetch_size=USER_RUN_CONFIG["fetch_size"],

build_root=str(skill_root.parent),

state_file=USER_RUN_CONFIG["state_file"],

source_jsonl=USER_RUN_CONFIG["source_jsonl"],

overwrite_skill_files=USER_RUN_CONFIG["overwrite_skill_files"],

include_markdown_files_in_skill=USER_RUN_CONFIG["include_markdown_files_in_skill"],

)

run_pipeline(bootstrap_args)

def _load_skill_index(data_root: Path) -> Dict[str, Any]:

index_path = data_root / "index.json"

if not index_path.exists():

raise DataNotFoundError(f"Missing index file: {index_path}")

key = str(index_path.resolve())

mtime = index_path.stat().st_mtime

if key not in _INDEX_CACHE or _INDEX_MTIME.get(key) != mtime:

_INDEX_CACHE[key] = json.loads(index_path.read_text(encoding="utf-8"))

_INDEX_MTIME[key] = mtime

return _INDEX_CACHE[key]

def quick_count(region: str, dataset_id: str, skill_root: str = "brain-alpha-dataset") -> int:

skill_root_path = Path(skill_root)

_ensure_skill_data(skill_root_path)

data_root = skill_root_path / "data"

index = _load_skill_index(data_root)

region = region.upper().strip()

dataset_id = dataset_id.strip()

if region not in index or dataset_id not in index[region]:

raise DataNotFoundError(f"No local data found for region={region}, dataset_id={dataset_id}.")

return int(index[region][dataset_id]["count"])

def get_field_description(region: str, dataset_id: str, field_id: str, skill_root: str = "brain-alpha-dataset") -> str:

skill_root_path = Path(skill_root)

_ensure_skill_data(skill_root_path)

data_root = skill_root_path / "data"

index = _load_skill_index(data_root)

region = region.upper().strip()

dataset_id = dataset_id.strip()

field_id = field_id.strip()

if region not in index or dataset_id not in index[region]:

raise DataNotFoundError(f"No local data found for region={region}, dataset_id={dataset_id}.")

desc_file = data_root / "desc" / region / dataset_id / f"{field_id}.txt"

if desc_file.exists():

return desc_file.read_text(encoding="utf-8", errors="replace").strip()

compact_file = data_root / index[region][dataset_id]["compact_file"]

with compact_file.open("r", encoding="utf-8", errors="replace") as f:

for line in f:

s = line.strip()

if not s:

continue

item = json.loads(s)

if item.get("id", "") == field_id:

return str(item.get("description", ""))

raise DataNotFoundError(f"No field found: {field_id} in region={region}, dataset_id={dataset_id}.")

def _is_count_query(text: str) -> bool:

t = text.lower()

signals = ["how many", "count", "number of", "多少", "几个", "总数", "数量"]

return any(s in t for s in signals)

def skill_entry(

instruction: str,

region: Optional[str] = None,

dataset_id: Optional[str] = None,

skill_root: str = "brain-alpha-dataset",

keyword: str = "",

field_id: Optional[str] = None,

limit: Optional[int] = None,

offset: int = 0,

) -> Dict[str, Any]:

# Unique skill entry: local lookup first, bootstrap local data when missing, return compact fields

region_from_text, dataset_from_text = parse_instruction(instruction or "")

field_from_text = parse_field_id(instruction or "")

region = (region or region_from_text or "").upper()

dataset_id = (dataset_id or dataset_from_text or "").strip()

field_id = (field_id or field_from_text or "").strip()

if not region or not dataset_id:

raise ConfigError("region and dataset_id are required, either by args or in instruction.")

skill_root_path = Path(skill_root)

_ensure_skill_data(skill_root_path)

data_root = skill_root_path / "data"

index = _load_skill_index(data_root)

if region not in index or dataset_id not in index[region]:

raise DataNotFoundError(f"No local data found for region={region}, dataset_id={dataset_id}.")

dataset_meta = index[region][dataset_id]

total_count = int(dataset_meta["count"])

if _is_count_query(instruction) and not keyword:

return {"count": total_count, "token_cost": 0}

if field_id:

desc = get_field_description(region=region, dataset_id=dataset_id, field_id=field_id, skill_root=skill_root)

return {"id": field_id, "description": desc, "token_cost": 0}

if limit is None:

limit = int(USER_RUN_CONFIG["max_fields_per_call"])

limit = max(1, int(limit))

offset = max(0, int(offset))

compact_file = data_root / dataset_meta["compact_file"]

field_items: List[Dict[str, str]] = []

start = offset

end = offset + limit

matched_idx = 0

matched_total = 0

with compact_file.open("r", encoding="utf-8", errors="replace") as f:

for line in f:

s = line.strip()

if not s:

continue

item = json.loads(s)

if keyword and keyword.lower() not in (item.get("description", "") + " " + item.get("id", "")).lower():

continue

if matched_idx < start:

matched_idx += 1

matched_total += 1

continue

if matched_idx < end:

field_items.append({"id": item.get("id", ""), "description": item.get("description", "")})

matched_idx += 1

matched_total += 1

visible_total = matched_total if keyword else total_count

has_more = (offset + len(field_items)) < visible_total

return {

"fields": field_items,

"total": visible_total,

"offset": offset,

"limit": limit,

"has_more": has_more,

"token_cost": 0,

}

def validate_lookup(skill_root: Path, region: str, dataset_id: str) -> Dict[str, Any]:

return skill_entry(

instruction=f"在 {region} 的 dataset {dataset_id} 上构建 alpha",

skill_root=str(skill_root),

)

def benchmark_lookup(skill_root: Path, region: str, dataset_id: str, loops: int) -> Dict[str, Any]:

# 压测本地读取延迟，输出 p50/p95

samples_ms: List[float] = []

for _ in range(loops):

t0 = time.perf_counter()

_ = validate_lookup(skill_root, region, dataset_id)

t1 = time.perf_counter()

samples_ms.append((t1 - t0) * 1000)

p50 = statistics.median(samples_ms) if samples_ms else 0.0

p95 = sorted(samples_ms)[int(max(0, loops * 0.95 - 1))] if samples_ms else 0.0

return {"p50_ms": p50, "p95_ms": p95, "token_cost": 0}

def persist_state(state_file: Path, max_created_at: Optional[str]) -> None:

payload = {"last_created_at": max_created_at or ""}

state_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

def load_state_since(state_file: Path) -> str:

if not state_file.exists():

return "1970-01-01 00:00:00"

try:

data = json.loads(state_file.read_text(encoding="utf-8"))

except json.JSONDecodeError:

return "1970-01-01 00:00:00"

value = str(data.get("last_created_at") or "").strip()

return value or "1970-01-01 00:00:00"

def run_pipeline(args: argparse.Namespace) -> PipelineArtifacts:

# 端到端流水线：SQL导出 -> Markdown渲染 -> 技能包组装 -> 本地入口验证

print("[pipeline] 启动端到端流程")

build_root = Path(args.build_root).resolve()

export_root = build_root / "export"

markdown_root = build_root / "markdown"

skill_root = build_root / "brain-alpha-dataset"

export_root.mkdir(parents=True, exist_ok=True)

markdown_root.mkdir(parents=True, exist_ok=True)

skill_root.mkdir(parents=True, exist_ok=True)

exported_jsonl = export_root / f"data_fields_{args.mode}_{now_ts()}.jsonl"

max_created_at = None

if args.source_jsonl:

source = Path(args.source_jsonl).resolve()

exported_jsonl.write_bytes(source.read_bytes())

records = load_jsonl(exported_jsonl)

else:

if args.mode == "incremental" and not args.since:

args.since = load_state_since(Path(args.state_file))

total, max_created_at = export_from_db(args, exported_jsonl)

if total == 0:

records = []

else:

records = load_jsonl(exported_jsonl)

index_path = write_markdown_tree(records, markdown_root)

manifest_path = skill_root / "manifest.json"

skill_file = skill_root / "SKILL.md"

if args.overwrite_skill_files or not manifest_path.exists():

manifest_path = write_manifest(skill_root)

else:

print("[pipeline] 保留已有 manifest.json，不重写")

if args.overwrite_skill_files or not skill_file.exists():

skill_file = write_skill_md(skill_root)

else:

print("[pipeline] 保留已有 SKILL.md，不重写")

skill_index = copy_markdown_to_skill(markdown_root, skill_root, args.include_markdown_files_in_skill)

if args.mode == "incremental":

persist_state(Path(args.state_file), max_created_at)

if records:

first = records[0]

_ = validate_lookup(skill_root, first["region"], first["dataset_id"])

return PipelineArtifacts(

exported_jsonl=exported_jsonl,

markdown_root=markdown_root,

skill_root=skill_root,

manifest_path=manifest_path,

skill_file=skill_file,

index_path=skill_index if skill_index.exists() else index_path,

)

class _UnitTests(unittest.TestCase):

def test_render_markdown(self):

rec = {

"id": "field_1",

"description": "hello",

"dataset_id": "ds1",

"dataset_name": "Dataset 1",

"category_id": "cat",

"category_name": "Cat",

"subcategory_id": "sub",

"subcategory_name": "Sub",

"region": "EUR",

"delay": 1,

"universe": "TOP3000",

"type": "MATRIX",

"dateCoverage": 1,

"coverage": 0.9,

"userCount": 1,

"alphaCount": 2,

"pyramidMultiplier": 1.2,

"themes": [],

}

md = render_markdown(rec)

self.assertIn("# field_1", md)

self.assertIn("dataset_id: ds1", md)

def test_skill_entry(self):

from tempfile import TemporaryDirectory

with TemporaryDirectory() as tmp:

root = Path(tmp)

markdown_root = root / "markdown"

rec = {

"id": "f1",

"description": "abc",

"dataset_id": "ds",

"dataset_name": "DS",

"category_id": "c",

"category_name": "C",

"subcategory_id": "s",

"subcategory_name": "S",

"region": "EUR",

"delay": 1,

"universe": "TOP3000",

"type": "MATRIX",

"dateCoverage": 1,

"coverage": 1,

"userCount": 1,

"alphaCount": 1,

"pyramidMultiplier": 1.1,

"themes": [],

}

write_markdown_tree([rec], markdown_root)

skill_root = root / "brain-alpha-dataset"

skill_root.mkdir(parents=True, exist_ok=True)

copy_markdown_to_skill(markdown_root, skill_root, include_markdown_files=False)

result = skill_entry("在 EUR 的 dataset ds 上构建 alpha", skill_root=str(skill_root))

self.assertEqual(result["fields"][0]["id"], "f1")

self.assertEqual(result["fields"][0]["description"], "abc")

self.assertEqual(result["token_cost"], 0)

self.assertEqual(result["total"], 1)

count_result = skill_entry("how many fields in EUR dataset ds", skill_root=str(skill_root))

self.assertEqual(count_result["count"], 1)

desc_result = skill_entry(

"get description of field f1 in EUR dataset ds",

skill_root=str(skill_root),

field_id="f1",

)

self.assertEqual(desc_result["id"], "f1")

self.assertEqual(desc_result["description"], "abc")

def test_pipeline_from_jsonl(self):

from tempfile import TemporaryDirectory

with TemporaryDirectory() as tmp:

root = Path(tmp)

src = root / "src.jsonl"

src.write_text(

json.dumps(

{

"id": "f2",

"description": "desc",

"dataset_id": "ds2",

"dataset_name": "DS2",

"category_id": "c2",

"category_name": "C2",

"subcategory_id": "s2",

"subcategory_name": "S2",

"region": "USA",

"delay": 1,

"universe": "TOP3000",

"type": "VECTOR",

"dateCoverage": 1,

"coverage": 0.5,

"userCount": 2,

"alphaCount": 3,

"pyramidMultiplier": 1.3,

"themes": [],

},

ensure_ascii=False,

)

+ "\n",

encoding="utf-8",

)

args = build_parser().parse_args(

[

"pipeline",

"--source-jsonl",

str(src),

"--build-root",

str(root / "out"),

]

)

art = run_pipeline(args)

self.assertTrue(art.manifest_path.exists())

self.assertTrue(art.skill_file.exists())

self.assertTrue((art.skill_root / "data" / "index.json").exists())

def run_tests() -> None:

# 运行内置单元测试 + 集成测试

suite = unittest.defaultTestLoader.loadTestsFromTestCase(_UnitTests)

result = unittest.TextTestRunner(verbosity=2).run(suite)

if not result.wasSuccessful():

raise SystemExit(1)

def print_solution(args: argparse.Namespace) -> None:

text = {

"sql_full": f"SELECT {', '.join(RECORD_FIELDS + ['created_at'])} FROM {args.table} WHERE region IN ({', '.join(args.regions)}) ORDER BY region, dataset_id, id;",

"sql_incremental": f"SELECT {', '.join(RECORD_FIELDS + ['created_at'])} FROM {args.table} WHERE region IN ({', '.join(args.regions)}) AND created_at >= '{args.since}' ORDER BY region, dataset_id, id;",

"performance_target": {"lookup_latency_ms": "<50", "token_cost_per_dataset_load": 0},

"entry_function": "skill_entry(instruction, region, dataset_id, skill_root, keyword)",

}

print(json.dumps(text, ensure_ascii=False, indent=2))

def build_parser() -> argparse.ArgumentParser:

parser = argparse.ArgumentParser()

sub = parser.add_subparsers(dest="cmd", required=True)

common = argparse.ArgumentParser(add_help=False)

common.add_argument("--db-host", default="127.0.0.1")

common.add_argument("--db-port", type=int, default=3306)

common.add_argument("--db-user", default="root")

common.add_argument("--db-password", default="")

common.add_argument("--db-name", default="wqb")

common.add_argument("--table", default="data_fields")

common.add_argument("--regions", nargs="+", default=DEFAULT_REGIONS)

common.add_argument("--mode", choices=["full", "incremental"], default="full")

common.add_argument("--since", default="1970-01-01 00:00:00")

common.add_argument("--fetch-size", type=int, default=5000)

common.add_argument("--build-root", default=str(Path.cwd() / "build_brain_alpha_dataset"))

common.add_argument("--state-file", default=str(Path.cwd() / ".brain_alpha_dataset_state.json"))

common.add_argument("--source-jsonl", default="")

common.add_argument("--overwrite-skill-files", action="store_true")

common.add_argument("--include-markdown-files-in-skill", action="store_true")

sub.add_parser("pipeline", parents=[common])

lookup = sub.add_parser("lookup")

lookup.add_argument("--skill-root", default="brain-alpha-dataset")

lookup.add_argument("--instruction", default="")

lookup.add_argument("--region", default="")

lookup.add_argument("--dataset-id", default="")

lookup.add_argument("--keyword", default="")

lookup.add_argument("--field-id", default="")

lookup.add_argument("--limit", type=int, default=200)

lookup.add_argument("--offset", type=int, default=0)

field_desc = sub.add_parser("field-desc")

field_desc.add_argument("--skill-root", default="brain-alpha-dataset")

field_desc.add_argument("--region", required=True)

field_desc.add_argument("--dataset-id", required=True)

field_desc.add_argument("--field-id", required=True)

bench = sub.add_parser("benchmark")

bench.add_argument("--skill-root", default="brain-alpha-dataset")

bench.add_argument("--region", required=True)

bench.add_argument("--dataset-id", required=True)

bench.add_argument("--loops", type=int, default=100)

sub.add_parser("run-tests")

sub.add_parser("solution", parents=[common])

return parser

def main() -> None:

# 无参数时走“一键模式”，读取 USER_RUN_CONFIG 自动执行 pipeline

if len(sys.argv) == 1:

print("[one-click] 检测到无参数运行，使用 USER_RUN_CONFIG 执行 pipeline")

args = argparse.Namespace(

cmd="pipeline",

db_host=USER_RUN_CONFIG["db_host"],

db_port=USER_RUN_CONFIG["db_port"],

db_user=USER_RUN_CONFIG["db_user"],

db_password=USER_RUN_CONFIG["db_password"],

db_name=USER_RUN_CONFIG["db_name"],

table=USER_RUN_CONFIG["table"],

regions=USER_RUN_CONFIG["regions"],

mode=USER_RUN_CONFIG["mode"],

since=USER_RUN_CONFIG["since"],

fetch_size=USER_RUN_CONFIG["fetch_size"],

build_root=USER_RUN_CONFIG["build_root"],

state_file=USER_RUN_CONFIG["state_file"],

source_jsonl=USER_RUN_CONFIG["source_jsonl"],

overwrite_skill_files=USER_RUN_CONFIG["overwrite_skill_files"],

include_markdown_files_in_skill=USER_RUN_CONFIG["include_markdown_files_in_skill"],

)

artifacts = run_pipeline(args)

print(

json.dumps(

{

"mode": "one-click",

"exported_jsonl": str(artifacts.exported_jsonl),

"markdown_root": str(artifacts.markdown_root),

"skill_root": str(artifacts.skill_root),

"manifest": str(artifacts.manifest_path),

"skill_md": str(artifacts.skill_file),

"index": str(artifacts.index_path),

},

ensure_ascii=False,

indent=2,

)

)

return

# 有参数时走高级命令模式（pipeline/lookup/benchmark/run-tests/solution）

parser = build_parser()

args = parser.parse_args()

if args.cmd == "pipeline":

artifacts = run_pipeline(args)

print(

json.dumps(

{

"exported_jsonl": str(artifacts.exported_jsonl),

"markdown_root": str(artifacts.markdown_root),

"skill_root": str(artifacts.skill_root),

"manifest": str(artifacts.manifest_path),

"skill_md": str(artifacts.skill_file),

"index": str(artifacts.index_path),

},

ensure_ascii=False,

indent=2,

)

)

return

if args.cmd == "lookup":

result = skill_entry(

instruction=args.instruction,

region=args.region or None,

dataset_id=args.dataset_id or None,

skill_root=args.skill_root,

keyword=args.keyword,

field_id=args.field_id or None,

limit=args.limit,

offset=args.offset,

)

print(json.dumps(result, ensure_ascii=False, indent=2))

return

if args.cmd == "field-desc":

result = {

"id": args.field_id,

"description": get_field_description(

region=args.region,

dataset_id=args.dataset_id,

field_id=args.field_id,

skill_root=args.skill_root,

),

"token_cost": 0,

}

print(json.dumps(result, ensure_ascii=False, indent=2))

return

if args.cmd == "benchmark":

result = benchmark_lookup(

skill_root=Path(args.skill_root),

region=args.region,

dataset_id=args.dataset_id,

loops=args.loops,

)

print(json.dumps(result, ensure_ascii=False, indent=2))

return

if args.cmd == "run-tests":

run_tests()

print("OK")

return

if args.cmd == "solution":

print_solution(args)

return

raise SystemExit(1)

if __name__ == "__main__":

main()

---

## 讨论与评论 (5)

### 评论 #1 (作者: 顾问 SJ65808 (Rank 20), 时间: 3个月前)

可以节省token，很棒的功能，感谢分享

==================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #2 (作者: LG87838, 时间: 3个月前)

好思路，听大家说过很多次，拖延症犯懒，一直没有行动起来，这次没有借口了。

--------------------------------------------------------------------------------------------------------------

慢慢来，相信时间的力量。

--------------------------------------------------------------------------------------------------------------

---

### 评论 #3 (作者: YQ51506, 时间: 3个月前)

====================================================================================看了一下代码，简单总结就是 **将本地数据库中的海量数据集字段转化为 AI 可高效调用的“轻量化本地知识库”，通过将数据从 MCP 远程调用转为 Skills 本地检索，实现 Token 消耗量大幅降低及查询速度的提升。** =====================================输入理解输出=====================================

---

### 评论 #4 (作者: 顾问 LW67640 (小虎) (Rank 24), 时间: 2个月前)

通过本地数据库的好处不止是省TOKEN，而是效率的提升，也是一种积极的约束，避免AI在不重要的环节消耗上下文。

============================================================

长风破浪会有时，直挂云帆济沧海。

============================================================

---

### 评论 #5 (作者: MP35172, 时间: 2个月前)

感谢大佬分享思路。

=======

生活就像一面镜子，你对它笑，它就对你笑；你对它哭，它也对你哭。你的心态，就是你真正的主人。你若积极，世界便处处是机遇与阳光；你若消极，人生便时时是阴霾与困境。因此，请用一颗热忱而坚定的心，去拥抱每一个清晨，去迎接每一次挑战，你会发现，生命的美好，往往就藏在你转念之间的积极里。

---

