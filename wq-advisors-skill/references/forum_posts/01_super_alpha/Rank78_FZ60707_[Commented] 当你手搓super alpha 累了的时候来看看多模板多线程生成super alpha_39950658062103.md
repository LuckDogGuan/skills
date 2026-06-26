# 当你手搓super alpha 累了的时候,来看看多模板多线程生成super alpha

- **链接**: https://support.worldquantbrain.com[Commented] 当你手搓super alpha 累了的时候来看看多模板多线程生成super alpha_39950658062103.md
- **作者**: TT92977
- **发布时间/热度**: 2个月前, 得票: 39

## 帖子正文

本文是我自己基于论坛中的各位大佬论坛模板进行整合并现写的一个Python代码:基于 WorldQuant BRAIN 平台的多线程 Super Alpha 回测框架，帮助量化研究者高效测试和优化 Super Alpha 策略。

**核心功能** ：

- 多线程并行回测，提高测试效率
- 基于成功案例的 Selection 和 Combo 表达式模板
- 智能组合生成和优先级排序
- 支持多种市场和中性化方法

具体包含的模板为

### 表达式模板库

#### Selection 表达式模板

代码包含11种 Selection 表达式模板，基于实际成功案例：

1. **质量综合评分** ：基于简单性、decay和sharpe的综合评分
2. **简单turnover过滤** ：QPdgn6Vw成功案例（OS Sharpe 2.81）
3. **更宽松turnover范围**
4. **质量评分+更严格turnover**
5. **基于fitness的评分**
6. **Sharpe优先筛选**
7. **相关性+质量双控**
8. **prod_correlation平方根权重**
9. **激进差异化1** ：高turnover区间（0.35-0.50）
10. **激进差异化2** ：低turnover+fitness主导（0.05-0.12）
11. **激进差异化3** ：显式反QPdgn6Vw惩罚

#### Combo 表达式模板

代码包含11种 Combo 表达式模板：

1. **300天窗口反相关** ：最成功案例（GrVGoROP, QPdgn6Vw）
2. **60天窗口+惩罚机制** ：YPXPE0N6实际使用
3. **252天窗口反相关** ：标准年化周期
4. **120天窗口反相关** ：中周期
5. **等权重基准**
6. **combo_a算法** ：论坛推荐
7. **300天窗口+质量权重**
8. **60天窗口+严格惩罚**
9. **180天窗口** ：中等差异化
10. **90天窗口+fitness权重** ：短周期+质量
11. **200天窗口+自相关惩罚** ：降低self_correlation

话不多说,开始上教程

## 使用指南

安装必要的依赖：

```
pip install requests
```

配置  `user_secret.txt`  文件，包含 WorldQuant BRAIN 平台的登录信息

```
直接运行脚本python 你的脚本.py
```

------

以下是代码内容:

#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

多线程遍历回测super alpha

基于WorldQuant BRAIN论坛文章改编

"""

import threading

import time

import requests

import logging as logger

from requests.adapters import HTTPAdapter

from urllib3.util.retry import Retry

# 设置日志级别为 INFO

logger.basicConfig(

level=logger.INFO,

format='%(asctime)s - %(levelname)s - %(message)s'

)

def login(max_retries=3, timeout=30):

# 从txt文件解密并读取数据

# txt格式:

# password: 'password'

# username: 'username'

def load_decrypted_data(txt_file='user_secret.txt'):

with open(txt_file, 'r') as f:

data = f.read()

data = data.strip().split('\n')

data = {line.split(': ')[0]: line.split(': ')[1] for line in data}

return data['username'][1:-1], data['password'][1:-1]

username, password = load_decrypted_data("user_secret.txt")

# Create a session with connection pooling and timeout

s = requests.Session()

# 配置连接池和重试机制

# 兼容不同 urllib3 版本

retry_kwargs = {

'total': max_retries,

'backoff_factor': 1,

'status_forcelist': [429, 500, 502, 503, 504],

}

# 尝试使用新版本的参数名，如果失败则使用旧的

try:

retry_strategy = Retry(**retry_kwargs, allowed_methods=["HEAD", "GET", "OPTIONS", "POST"])

except TypeError:

retry_strategy = Retry(**retry_kwargs, method_whitelist=["HEAD", "GET", "OPTIONS", "POST"])

adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=10, pool_maxsize=10)

s.mount("https://", adapter)

s.mount("http://", adapter)

# Save credentials into session

s.auth = (username, password)

# Send a POST request to the /authentication API with retry

for attempt in range(max_retries):

try:

response = s.post(' [https://api.worldquantbrain.com/authentication](https://api.worldquantbrain.com/authentication) ', timeout=timeout)

response.raise_for_status()

info_ = response.content.decode('utf-8')

logger.info(info_)

if "INVALID_CREDENTIALS" in info_:

raise Exception("你的账号密码有误，请在【user_info.txt】输入正确的邮箱和密码！\n"

"Your username or password is incorrect. Please enter the correct email and password!")

return s

except requests.exceptions.SSLError as e:

logger.warning(f"SSL Error on attempt {attempt + 1}/{max_retries}: {e}")

if attempt < max_retries - 1:

time.sleep(2 ** attempt)  # Exponential backoff

else:

raise Exception(f"Failed to login after {max_retries} attempts due to SSL error")

except requests.exceptions.ConnectionError as e:

logger.warning(f"Connection Error on attempt {attempt + 1}/{max_retries}: {e}")

if attempt < max_retries - 1:

time.sleep(2 ** attempt)

else:

raise Exception(f"Failed to login after {max_retries} attempts due to connection error")

except requests.exceptions.RequestException as e:

logger.error(f"Request Error: {e}")

raise

def load_task_pool(alpha_list, limit_of_multi_simulations, limit_of_concurrent_simulations):

'''

Input:

alpha_list : list of (alpha, decay) tuples

limit_of_multi_simulations : number of simulation in a multi-simulation

limit_of_multi_simulations : number of simultaneous multi-simulations

Output:

task : [10 * (alpha, decay)] for a multi-simulation

pool : [10 * [10 * (alpha, decay)]] for simultaneous multi-simulations

pools : [[10 * [10 * (alpha, decay)]]]

'''

tasks = [alpha_list[i:i + limit_of_multi_simulations] for i in

range(0, len(alpha_list), limit_of_multi_simulations)]

pools = [tasks[i:i + limit_of_concurrent_simulations] for i in

range(0, len(tasks), limit_of_concurrent_simulations)]

return pools

def multi_simulate2_sa(alpha_pools, neut, region, universe, start):

"""

多线程回测super alpha

参数:

alpha_pools: alpha池，包含多个alpha任务

neut: 中性化方法

region: 地区

universe: 股票池

start: 开始索引

"""

brain_api_url = ' [https://api.worldquantbrain.com](https://api.worldquantbrain.com) '

limit_of_concurrent_simulations = min(len(alpha_pools[0]), 3)  # 限制并发数不超过3

alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]

end = len(alpha_pools_2)

print(f'length:{len(alpha_pools_2)}, start:{start}, concurrent_threads:{limit_of_concurrent_simulations}')

counter: int = start

lock = threading.Lock()

def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):

"""单个回测任务"""

local_session = None

while True:

lock.acquire()

nonlocal counter

if counter > end - 1:

lock.release()

break

if (counter - start) % 100 == 0 and local_session is not None:  # 每100个任务重新登录

try:

local_session.close()

except:

pass

local_session = login()

if local_session is None:

local_session = login()

local_counter = counter

counter += 1

lock.release()

task = pools[local_counter]

sim_data_list = generate_sim_data_sa(task, region, universe, neut)

sim_data = sim_data_list[0]

max_retries = 3

simulation_progress_url = None

for retry in range(max_retries):

try:

simulation_response = local_session.post(

' [https://api.worldquantbrain.com/simulations](https://api.worldquantbrain.com/simulations) ',

json=sim_data,

timeout=60

)

simulation_response.raise_for_status()

simulation_progress_url = simulation_response.headers['Location']

break

except KeyError:

print(f"task {local_counter} attempt {retry+1}/{max_retries}: Location header missing")

if retry < max_retries - 1:

time.sleep(5 * (retry + 1))

try:

local_session.close()

except:

pass

local_session = login()

except requests.exceptions.RequestException as e:

print(f"task {local_counter} attempt {retry+1}/{max_retries}: {type(e).__name__}")

if retry < max_retries - 1:

time.sleep(5 * (retry + 1))

try:

local_session.close()

except:

pass

local_session = login()

if simulation_progress_url is None:

print(f"task {local_counter} failed after retries, skipping")

continue

print(f"task {local_counter} post done")

try:

while True:

simulation_progress = local_session.get(simulation_progress_url, timeout=60)

if simulation_progress.headers.get("Retry-After", 0) == 0:

break

time.sleep(float(simulation_progress.headers["Retry-After"]))

status = simulation_progress.json().get("status", 0)

if status != "COMPLETE":

print(f"task {local_counter}: simulation not complete")

except KeyError:

print(f"task {local_counter}: key error in progress check")

except Exception as e:

print(f"task {local_counter}: {type(e).__name__}")

print(f"task {local_counter} simulate done")

if local_session is not None:

try:

local_session.close()

except:

pass

# 创建并启动线程

threads = []

for i in range(limit_of_concurrent_simulations):

t = threading.Thread(target=sim_task)

threads.append(t)

t.start()

# 等待所有线程完成

for t in threads:

t.join()

print("Simulate done")

def generate_sim_data_sa(alpha_list, region, uni, neut):

"""

生成super alpha回测数据

参数:

alpha_list: alpha表达式列表，包含(selection_exp, combo_exp)元组

region: 地区

uni: 股票池

neut: 中性化方法

返回:

回测数据列表

"""

sim_data_list = []

for selection_exp, combo_exp in alpha_list:

simulation_data = {

'type': 'SUPER',

'settings': {

'instrumentType': 'EQUITY',

'region': region,

'universe': uni,

'delay': 1,

'decay': 6,

'neutralization': neut,

'truncation': 0.08,

'pasteurization': 'ON',

'unitHandling': 'VERIFY',

'nanHandling': 'ON',

'selectionHandling': 'POSITIVE',

'selectionLimit': 1000,

'language': 'FASTEXPR',

'visualization': False,

},

'selection': selection_exp,

'combo': combo_exp

}

sim_data_list.append(simulation_data)

return sim_data_list

def main():

"""

主函数，提供示例用法

"""

# 示例：设置selection和combo表达式

# -------------- Selection表达式模板 (基于实际成功案例 v4.0) --------------

# 核心策略：基于你已提交的成功Super Alpha实际模板

# 成功案例：GrVGoROP (OS Sharpe 2.48), QPdgn6Vw (OS Sharpe 2.81)

# 1. 质量综合评分 - 简单性+decay+sharpe奖励 (你的成功案例⭐)

selection_exp1 = ['simplicity = 1 / (operator_count + 1); decay_bonus = if_else(decay < 1.5, 1.3, 1); bonus = if_else(author_sharpe >= 2.5 && author_sharpe <= 3.5, 1.2, 1); score = simplicity * decay_bonus * bonus; if_else(turnover >= 0.30, nan, score)']

# 2. 简单turnover过滤 (QPdgn6Vw成功案例 - OS Sharpe 2.81⭐⭐)

selection_exp2 = ['sqrt(prod_correlation)*((turnover>0.12 && turnover<0.35))']

# 3. 变体1：更宽松turnover范围

selection_exp3 = ['sqrt(prod_correlation)*((turnover>0.08 && turnover<0.40))']

# 4. 变体2：质量评分+更严格turnover

selection_exp4 = ['simplicity = 1 / (operator_count + 1); decay_bonus = if_else(decay < 2, 1.2, 1); bonus = if_else(author_sharpe >= 2.0 && author_sharpe <= 4.0, 1.3, 1); score = simplicity * decay_bonus * bonus; if_else(turnover >= 0.25, nan, score)']

# 5. 变体3：基于fitness的评分

selection_exp5 = ['simplicity = 1 / (operator_count + 1); fitness_bonus = if_else(fitness >= 0.5, 1.2, 1); score = simplicity * fitness_bonus; if_else(turnover >= 0.30, nan, score)']

# 6. 变体4：Sharpe优先筛选

selection_exp6 = ['if_else(sharpe >= 1.8 && turnover >= 0.10 && turnover <= 0.35, sharpe, nan)']

# 7. 变体5：相关性+质量双控

selection_exp7 = ['if_else(self_correlation <= 0.4 && prod_correlation < 0.7 && turnover >= 0.10 && turnover <= 0.30, 1, nan)']

# 8. 变体6：prod_correlation平方根权重

selection_exp8 = ['sqrt(prod_correlation)*((turnover>0.15 && turnover<0.30 && sharpe >= 1.5))']

# 9. 激进差异化1：高turnover区间（完全不重叠QPdgn6Vw）

selection_exp9 = ['sqrt(prod_correlation)*((turnover>0.35 && turnover<0.50))']

# 10. 激进差异化2：低turnover+fitness主导

selection_exp10 = ['fitness_score = fitness * (1 - self_correlation); if_else(fitness_score >= 0.8 && turnover >= 0.05 && turnover < 0.12, fitness_score, nan)']

# 11. 激进差异化3：显式反QPdgn6Vw惩罚

selection_exp11 = ['anti_overlap = if_else(turnover >= 0.12 && turnover <= 0.35, 0.3, 1.0); score = sqrt(prod_correlation) * anti_overlap * if_else(sharpe >= 2.0, 1, nan); if_else(score > 0, score, nan)']

# -------------- Combo表达式模板 (基于实际成功案例 v4.0) --------------

# 核心策略：内部相关性(innerCorr)反向权重 - 你的成功案例核心

# 参考：GrVGoROP (OS Sharpe 2.48), QPdgn6Vw (OS Sharpe 2.81)

# 1. 300天窗口反相关 (最成功⭐⭐ - GrVGoROP, QPdgn6Vw实际使用)

combo_exp1 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 300); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr']

# 2. 60天窗口+惩罚机制 (YPXPE0N6实际使用)

combo_exp2 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 60); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); (1 - maxCorr) * if_else(maxCorr > 0.6, 0.5, 1)']

# 3. 252天窗口反相关 (标准年化周期)

combo_exp3 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 252); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr']

# 4. 120天窗口反相关 (中周期)

combo_exp4 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 120); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr']

# 5. 等权重基准 (论坛推荐作为对照)

combo_exp5 = ['1']

# 6. combo_a算法1-252天 (论坛常用)

combo_exp6 = ['combo_a(alpha, nlength=252, mode="algo1")']

# 7. 300天窗口+质量权重

combo_exp7 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 300); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); (1 - maxCorr) * sharpe']

# 8. 60天窗口+严格惩罚

combo_exp8 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 60); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); (1 - maxCorr) * if_else(maxCorr > 0.5, 0.3, 1)']

# 9. 180天窗口（中等差异化）

combo_exp9 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 180); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr']

# 10. 90天窗口+fitness权重（短周期+质量）

combo_exp10 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 90); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); (1 - maxCorr) * fitness']

# 11. 200天窗口+自相关惩罚（显式降低self_correlation）

combo_exp11 = ['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 200); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); (1 - maxCorr) * (1 - self_correlation)']

# -------------- 组合测试配置 (基于实际成功案例 v4.0) --------------

# 核心策略：使用你已提交的成功Super Alpha实际模板组合

# 最佳案例：selection_exp2 + combo_exp1 (QPdgn6Vw模式, OS Sharpe 2.81)

#          selection_exp1 + combo_exp1 (GrVGoROP模式, OS Sharpe 2.48)

# 选择要测试的selection表达式 - 优先你的成功模板

test_selection_exps = [

selection_exp1[0],  # 质量综合评分 (你的成功案例⭐)

selection_exp2[0],  # 简单turnover过滤 (QPdgn6Vw - OS 2.81⭐⭐)

selection_exp3[0],  # 更宽松turnover范围

selection_exp4[0],  # 质量评分+严格turnover

selection_exp5[0],  # Fitness评分

selection_exp6[0],  # Sharpe优先筛选

selection_exp7[0],  # 相关性+质量双控

selection_exp8[0],  # prod_correlation平方根权重

selection_exp9[0],  # 激进差异化1：高turnover（0.35-0.50）⭐降低与QPdgn6Vw相关性

selection_exp10[0], # 激进差异化2：低turnover+fitness（0.05-0.12）⭐

selection_exp11[0], # 激进差异化3：显式反QPdgn6Vw惩罚⭐

]

# 选择要测试的combo表达式 - 优先你的成功模板

test_combo_exps = [

combo_exp1[0],   # 300天反相关 (最成功⭐⭐ - GrVGoROP, QPdgn6Vw)

combo_exp2[0],   # 60天+惩罚 (YPXPE0N6)

combo_exp3[0],   # 252天反相关

combo_exp4[0],   # 120天反相关

combo_exp5[0],   # 等权重基准

combo_exp6[0],   # combo_a算法

combo_exp7[0],   # 300天+质量权重

combo_exp8[0],   # 60天+严格惩罚

combo_exp9[0],   # 180天窗口（中等差异化）⭐

combo_exp10[0],  # 90天+fitness权重⭐

combo_exp11[0],  # 200天+自相关惩罚⭐降低self_correlation

]

# 生成所有可能的组合

sa_list = [(sel, combo) for sel in test_selection_exps for combo in test_combo_exps]

print(f"生成的组合数量: {len(sa_list)}")

print("\n基于你的成功案例优化后的模板组合:")

print(f"Selection模板: {len(test_selection_exps)}种 (你的实际成功案例⭐)")

print(f"Combo模板: {len(test_combo_exps)}种 (内部相关性反向权重策略)")

print("\n最成功的案例参考:")

print("  - QPdgn6Vw: OS Sharpe 2.81 (selection_exp2 + combo_exp1)")

print("  - GrVGoROP: OS Sharpe 2.48 (selection_exp1 + combo_exp1)")

print("  - GrVGo5kJ: OS Sharpe 1.45 (selection_exp1 + combo_exp1)")

# 为了避免API限制，限制测试数量

# 建议：Selection选2-3个，Combo选2-3个，总共4-9个组合

max_tests = 16  # 最多测试16个组合

if len(sa_list) > max_tests:

import random

# 按优先级选择：优先使用你的实际成功组合

recommended_indices = [

# 最成功的原始组合

(1, 0),  # selection_exp2 + combo_exp1 (QPdgn6Vw模式 - OS 2.81⭐⭐最佳)

(0, 0),  # selection_exp1 + combo_exp1 (GrVGoROP模式 - OS 2.48⭐)

# 激进差异化组合（针对降低自相关性）⭐⭐专门解决wpXdlx9Y问题

(8, 8),  # selection_exp9(高turnover 0.35-0.50) + combo_exp9(180天) ⭐⭐最推荐

(9, 9),  # selection_exp10(低turnover+fitness) + combo_exp10(90天+fitness) ⭐⭐

(10, 10), # selection_exp11(反QPdgn6Vw惩罚) + combo_exp11(200天+自相关惩罚) ⭐⭐

(8, 10), # selection_exp9(高turnover) + combo_exp11(自相关惩罚)

(9, 8),  # selection_exp10(低turnover+fitness) + combo_exp9(180天)

# 其他有效组合

(1, 2),  # selection_exp2 + combo_exp3 (简单+252天)

(0, 2),  # selection_exp1 + combo_exp3 (质量+252天)

(2, 0),  # selection_exp3 + combo_exp1 (宽松+300天)

(3, 0),  # selection_exp4 + combo_exp1 (严格+300天)

(1, 1),  # selection_exp2 + combo_exp2 (简单+60天惩罚)

(0, 1),  # selection_exp1 + combo_exp2 (质量+60天惩罚)

]

# 构建推荐组合列表

recommended_list = []

for sel_idx, combo_idx in recommended_indices:

if sel_idx < len(test_selection_exps) and combo_idx < len(test_combo_exps):

recommended_list.append((test_selection_exps[sel_idx], test_combo_exps[combo_idx]))

# 如果推荐组合不足max_tests，补充其他随机组合

if len(recommended_list) < max_tests:

remaining = [item for item in sa_list if item not in recommended_list]

additional = random.sample(remaining, min(max_tests - len(recommended_list), len(remaining)))

sa_list = recommended_list + additional

else:

sa_list = recommended_list[:max_tests]

print(f"\n优先级选择 {len(sa_list)} 个组合进行测试:")

for i, (sel, combo) in enumerate(sa_list):

print(f"  {i+1}. Selection: {sel[:60]}...")

print(f"     Combo: {combo[:60]}...")

else:

print("\n将测试所有组合:")

for i, (sel, combo) in enumerate(sa_list):

print(f"  {i+1}. Selection: {sel[:60]}...")

print(f"     Combo: {combo[:60]}...")

# 加载任务池

pools = load_task_pool(sa_list, 1, 3)

# 地区配置

region_dict = {

"usa": ("USA", ["TOP3000", "TOP1000", "TOP500", "TOP200","ILLIQUID_MINVOL1M"]),

"asi": ("ASI", ["MINVOL1M"]),

"eur": ("EUR", ["TOP2500", "TOP1200", "TOP800", "TOP400"]),

"glb": ("GLB", ["TOP3000", "MINVOL1M"]),

"hkg": ("HKG", ["TOP800", "TOP500"]),

"twn": ("TWN", ["TOP500", "TOP100"]),

"jpn": ("JPN", ["TOP1600", "TOP1200"]),

"kor": ("KOR", ["TOP600"]),

"chn": ("CHN", ["TOP2000U"]),

"amr": ("AMR", ["TOP600"]),

"ind": ("IND", ["TOP500"])

}

# 中性化选项配置

norm_opt = ["INDUSTRY", "STATISTIC", "MARKET", "SECTOR"]

risk_opt = ["FAST", "SLOW", "SLOW_AND_FAST"]

r1 = ['STATISTICAL']

cr = ["CROWDING"]

co = ["COUNTRY"]

no = ["NONE"]

neut_opt = {

"USA": norm_opt + cr + risk_opt + r1,

"GLB": co + r1,

"EUR": co + cr + norm_opt + risk_opt + r1,

"ASI": co + cr + norm_opt + risk_opt + no,

"CHN": norm_opt + cr + risk_opt + r1,

"KOR": norm_opt,

"TWN": norm_opt,

"HKG": norm_opt,

"JPN": norm_opt,

"AMR": ["COUNTRY"] + norm_opt,

"IND": ["COUNTRY"] + norm_opt,

}

# 选择要测试的地区（示例：只测试美国市场）

regi = ['usa']

# 遍历测试

for k in regi:

# 只选择第一个股票池进行测试，实际使用时可以调整

for i in region_dict[k][1][:1]:

print(f"测试股票池: {i}")

# 遍历所有中性化方法

for j in neut_opt[k.upper()]:

print(f"使用中性化方法: {j}, 地区: {region_dict[k][0]}")

# 执行多线程回测

multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)

if __name__ == "__main__":

print("开始多线程回测super alpha...")

main()

print("回测完成！")
----

---

## 讨论与评论 (7)

### 评论 #1 (作者: JL33484, 时间: 2个月前)

挺好用的

---

### 评论 #2 (作者: XS60818, 时间: 2个月前)

学长，想请教下图片中的"直接运行脚本"这几个字也是直接输入到cmd中的嘛，我不太会代码，想用学长的super alpha增加收益 
> [!NOTE] [图片 OCR 识别内容]
> 直接运行脚本
> psthon 你的脚本.D


---

### 评论 #3 (作者: JX96306, 时间: 2个月前)

感谢 大佬分享 虽然还没到那一步 收藏了 慢慢研究一下

---

### 评论 #4 (作者: TT92977, 时间: 1个月前)

运行脚本: 比如你复制我的代码  创建了 文件名叫: run_super_alpha.py 的程序 那么 你再运行的时候 需要在cmd中 执行  python run_super_alpha.py 这样就可以运行了 ,如果运行失败 会有报错信息 大概率是 你缺失user_secret.txt文件 或者 python环境缺少依赖 可以根据报错信息 问ai 帮你解决

---

### 评论 #5 (作者: LK75170, 时间: 1个月前)

感谢大佬分享！

---

### 评论 #6 (作者: 顾问 FZ60707 (Rank 78), 时间: 1个月前)

很实用的框架，尤其是针对降低自相关和组合多样化的设计思路，对已有一定积累的研究员很有参考价值。不过新手可能需要先理解模板里的表达式含义再跑代码，否则容易迷失在参数里。感谢分享！

====================================================================================================================================================================

---

### 评论 #7 (作者: ZL29846, 时间: 1个月前)

学习了，慢慢测试下

---

