# 顾问 JR23144 (Rank 6) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 JR23144 (Rank 6) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: 计算置信度
- **主帖链接**: Alpha PNL 合法性检测【自动剔除 厂 Alpha等无效Alpha实现高效率剪枝】代码优化.md
- **讨论数**: 25

在进行培训代码回测时，我发现一个规律：如果一个 Alpha 在一阶回测时表现为 “厂” Alpha（指 PNL 呈现特定不良模式），那么基于这个 Alpha 进行后续的二阶、三阶优化或组合，其结果大概率仍然是“厂”Alpha。因此，我认为有必要在初步筛选阶段就将这类 Alpha 剔除。

[图片 (图片已丢失)]

两个步骤，就能开箱即用

**1.** 新建一个名为 **pnl_test.py**  的Python 文件  **，粘贴下列代码（并修改登录信息为你的实际登录信息）**

```
import osfrom dotenv import load_dotenvimport loggingimport timeimport requestsfrom machine_lib import *class cfg:    env_path = "user.env"    load_dotenv(dotenv_path=env_path)    username = os.environ["USER_NAME"]    password = os.environ["PASSWORD"]def sign_in(username, password):    s = requests.Session()    s.auth = (username, password)    try:        response = s.post('[链接已屏蔽])        response.raise_for_status()        logging.info("Successfully signed in")        return s    except requests.exceptions.RequestException as e:        logging.error(f"Login failed: {e}")        return Nonedef wait_get(url: str, max_retries: int = 10) -> "Response":    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef check_consecutive_non_zero_values(alpha_id, data, required_streak=200):    if not data or len(data) < required_streak:        return True    def check_column(column_data):        if len(column_data) < required_streak:            return True        current_streak_count = 0        current_streak_value = None        for value in column_data:            if value != 0:                if value == current_streak_value:                    current_streak_count += 1                else:                    current_streak_value = value                    current_streak_count = 1            else:                current_streak_value = None                current_streak_count = 0            if current_streak_count >= required_streak:                return False        return True    column1_values = []    column2_values = []    for row in data:        if len(row) >= 3:            column1_values.append(row[1])            column2_values.append(row[2])        else:            pass    if column1_values and column2_values:        is_col1_all_zeros = all(v == 0 for v in column1_values)        is_col2_all_zeros = all(v == 0 for v in column2_values)        if is_col1_all_zeros or is_col2_all_zeros:            print(alpha_id, "不合法")            return False    if not check_column(column1_values):        print(alpha_id, "不合法")        return False    if not check_column(column2_values):        print(alpha_id, "不合法")        return False    print(alpha_id, "通过")    return Truedef get_alpha_pnl_legal(alpha_id: str) -> bool:    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    records = pnl["records"]    return check_consecutive_non_zero_values(alpha_id, records)def get_alpha_pnl_legal_list(fo_tracker: list) -> list:    global sess    sess = sign_in(cfg.username, cfg.password)    fo_tracker =[fo for fo in fo_tracker if get_alpha_pnl_legal(fo[0])]    return fo_trackersess = sign_in(cfg.username, cfg.password)
```

**2.  在notebook中** 修改其中筛选第一次回测完的Alpha

```
fo_tracker = get_alphas("06-12", "06-13", 1, 0.7, "ASI", 200, "track")# 添加以下几行import pnl_testf_num = len(fo_tracker)print(f_num,"个alpha 进行pnl合法检测，请耐心等待")fo_tracker = pnl_test.get_alpha_pnl_legal_list(fo_tracker)print(f_num -len(fo_tracker),"个不合法的pnl,已被剔除" )
```

**希望这个小脚本能帮你提升回测效率。** 
 **觉得还行？一个小赞就能让我动力满满，一起day day Alpha！**

---

### 帖子 #2: 计算置信度
- **主帖链接**: https://support.worldquantbrain.comAlpha PNL 合法性检测【自动剔除 厂 Alpha等无效Alpha实现高效率剪枝】代码优化_32761924007703.md
- **讨论数**: 25

在进行培训代码回测时，我发现一个规律：如果一个 Alpha 在一阶回测时表现为 “厂” Alpha（指 PNL 呈现特定不良模式），那么基于这个 Alpha 进行后续的二阶、三阶优化或组合，其结果大概率仍然是“厂”Alpha。因此，我认为有必要在初步筛选阶段就将这类 Alpha 剔除。


> [!NOTE] [图片 OCR 识别内容]
> ts_delay ( fnd6_nitq/ fnd6_cptnewq_ceqq,
> 240
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> TUTIOVeI
> Fitness
> RetUrhs
> DrawdOwh
> Margin
> Simulation Settings
> 2.62
> 5.729
> 5.85
> 62.409
> 13.239
> 218.339600
> Instrument Type:
> Equity
> Truncation:
> 0.08
> 这个
> alpha 的各个指标都很高
> Region:
> ASI
> Neutralization:
> Subindustry
> Universe:
> MINVOLIM
> Pasteurization:
> On
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
> Fast Expression
> NaN
> Handling:
> 0n
> Decay:
> Unit Handling:
> Verify
> 2013
> 2.03
> 3.4595
> 3.52
> 37.5495
> 13.2395
> 218.33900
> Max Trade:
> On
> 2014
> 0.00
> 0.0095
> 0.00
> 00%
> 00%
> 0.00Soo
> 2015
> 0.00
> 0.0095
> U.UU
> 0.009
> 0.0095
> 00Dooo
> 2016
> 0.00
> 0.0095
> 0,0095
> 0.009
> 0.00Soo
> Clone Alpha 
> 2017
> 0.00
> 0.009
> 0,0095
> 0Oo
> 0.00Soo
> 但
> PNL 是不合法的
> 2018
> 0.00
> 0.0095
> U.UU
> 0.0095
> 0.0095
> 00Dooa
> N
> Chart
> Pnl
> 2019
> 0.00
> 000
> 00O
> 0Oo
> 0OSoo
> 2020
> 0.00
> 0.0095
> U.UU
> 0.0095
> 009
> 00Dooa
> 2021
> 0.00
> 0.0095
> 0.00
> 0.009
> 0.0095
> 00Dooo
> 2022
> 0.009
> 0OSoo
> 下面的提交按钮
> 2023
> 有瞧候熊是趟的
> 0.00
> 0.0095
> 0.0095
> 但是实际点击后是通过不了的
> Risk neutralized
> Aggregate Data
> Sharpe
> TurhoVer
> Fitness
> Returns
> Drawdown
> Margin
> 2.16
> 5.72%
> 4.39
> 51.66%
> 13.43%
> 180.749600
> Delay:
> 0OYooo


两个步骤，就能开箱即用

**1.** 新建一个名为 **pnl_test.py**  的Python 文件  **，粘贴下列代码（并修改登录信息为你的实际登录信息）**

```
import osfrom dotenv import load_dotenvimport loggingimport timeimport requestsfrom machine_lib import *class cfg:    env_path = "user.env"    load_dotenv(dotenv_path=env_path)    username = os.environ["USER_NAME"]    password = os.environ["PASSWORD"]def sign_in(username, password):    s = requests.Session()    s.auth = (username, password)    try:        response = s.post('[链接已屏蔽])        response.raise_for_status()        logging.info("Successfully signed in")        return s    except requests.exceptions.RequestException as e:        logging.error(f"Login failed: {e}")        return Nonedef wait_get(url: str, max_retries: int = 10) -> "Response":    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef check_consecutive_non_zero_values(alpha_id, data, required_streak=200):    if not data or len(data) < required_streak:        return True    def check_column(column_data):        if len(column_data) < required_streak:            return True        current_streak_count = 0        current_streak_value = None        for value in column_data:            if value != 0:                if value == current_streak_value:                    current_streak_count += 1                else:                    current_streak_value = value                    current_streak_count = 1            else:                current_streak_value = None                current_streak_count = 0            if current_streak_count >= required_streak:                return False        return True    column1_values = []    column2_values = []    for row in data:        if len(row) >= 3:            column1_values.append(row[1])            column2_values.append(row[2])        else:            pass    if column1_values and column2_values:        is_col1_all_zeros = all(v == 0 for v in column1_values)        is_col2_all_zeros = all(v == 0 for v in column2_values)        if is_col1_all_zeros or is_col2_all_zeros:            print(alpha_id, "不合法")            return False    if not check_column(column1_values):        print(alpha_id, "不合法")        return False    if not check_column(column2_values):        print(alpha_id, "不合法")        return False    print(alpha_id, "通过")    return Truedef get_alpha_pnl_legal(alpha_id: str) -> bool:    pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()    records = pnl["records"]    return check_consecutive_non_zero_values(alpha_id, records)def get_alpha_pnl_legal_list(fo_tracker: list) -> list:    global sess    sess = sign_in(cfg.username, cfg.password)    fo_tracker =[fo for fo in fo_tracker if get_alpha_pnl_legal(fo[0])]    return fo_trackersess = sign_in(cfg.username, cfg.password)
```

**2.  在notebook中** 修改其中筛选第一次回测完的Alpha

```
fo_tracker = get_alphas("06-12", "06-13", 1, 0.7, "ASI", 200, "track")# 添加以下几行import pnl_testf_num = len(fo_tracker)print(f_num,"个alpha 进行pnl合法检测，请耐心等待")fo_tracker = pnl_test.get_alpha_pnl_legal_list(fo_tracker)print(f_num -len(fo_tracker),"个不合法的pnl,已被剔除" )
```

**希望这个小脚本能帮你提升回测效率。** 
 **觉得还行？一个小赞就能让我动力满满，一起day day Alpha！**

---

### 帖子 #3: --- 阶段二：创建和重命名SUPER Alphas ---
- **主帖链接**: ValueFactor 预测器自动化滚动3个月 Alpha 表现评估代码优化.md
- **讨论数**: 6

**开箱即用，助您洞悉近期alpha提交的质量**

### 引言：为何需要这个工具？

作为一名 因子挖掘者，如何客观、持续地评估自己提交alpha的表现？我们提交的 Alpha 数量众多，手动去筛选、组合、回测最近几个月的成果，不仅耗时耗力，而且难以形成统一的评估标准。

这个工具旨在解决这一痛点。它能自动化地完成以下任务：

1. **动态筛选** ：自动识别并标记出您最近三个月内提交的 Regular Alphas。
2. **智能组合** ：将标记出的 Alphas 按区域（Region）分组，并为每个符合条件的区域生成一个 SUPER Alpha。
3. **客观评估** ：这个生成的 SUPER Alpha 本身就是一个“价值因子”（Value Factor），它的表现直观地反映了您近期研发工作的综合成效。
4. **自动化流程** ：整个过程通过一个脚本全自动执行，您只需设置一次自己的“顾问生效日期”，即可每日运行，持续追踪。

### 核心理念与设计思路

在深入代码之前，理解其背后的设计思想至关重要。

1. **为何不直接用 Selection Expression？**
   BRAIN 平台的 SUPER Alpha 在选择子 Alpha 时，默认会优先选择 **最早提交** 的 Alpha。这与我们希望评估 **近期表现** 的目标背道而驰。因此，我们不能简单地依赖 selectionLimit，而必须采用一种方式主动筛选出我们想要的 Alpha。
   
> [!NOTE] [图片 OCR 识别内容]
> 瞿SeBCC
> 仕
> CeRBEsgn 填
> OWh
> Combo Expression 填1
> setting 中
> Selection Limit = 26 的条件下 Ealpha 按时间顺序选择选择之前莳不选择最
> 近提交的 所以这样不去修改alpha属性筛选实现不了这个功能。
> Selected Alphas
> 26 Alphas have been selecte
> View
> Nam
> UniVerse
> TUINOeT
> Ftness
> Returs
> Drawdown
> Marqin
> CF
> TCP250
> 2.75
> 23.524
> 1.27
> 5054
> 1.754
> 4.2586oo
> CF
> TCP2500
> 2.23
> 17.054
> 1.19
> G5
> G5
> 456oo
> CF
> TCP250
> 1.554
> 3.534
> 12.-04
> 104.975500
> CF
> TCP2500
> 1.784
> 7.101
> 384
> 79.63530
> CVF
> TCP2500
> 3.06
> 36.634
> .651:
> 354
> ~275530
> Sharpe

2. **为什么选择用“名字(Name)”进行标记？
   对于RA 的名字的修改只修改已提交阶段的，不影响如果你在未提交阶段对于RA 名字的操作，已提交阶段的alpha 名字用的人应该少吧。**
   为了让 SUPER Alpha 能精准地选中我们想要的子 Alpha，我们需要一个“标记”。通过 API，我们可以修改 Alpha 的名字（Name）或颜色（Color）或打一个Tags 。本脚本选择使用名字，将目标 Alpha 命名为  **"CVF"** （可理解为 Calculate Value Factor）。这样，在 SUPER Alpha 的 Selection Expression 中，我们就可以使用 own && name == "CVF" 来精确抓取这些被选中的 Alpha。
   
> [!NOTE] [图片 OCR 识别内容]
> CaEEON
> User-SEleted CECEEONY
> Strine 'NONE"
> PZICEZEIERSION,
> CaTEEONJ
> NONE"
>  RICENOMENTN"IOLUME
> FUNDALIENT-L"'
> IANALYST
> PRICEVOLUME ,
> RELATION
> SENTINEIIT
> COIOT
> Us=rselzczd Colar
> Sirine:"NONE"
> REDIVELON GREEN
> BLVE
> Color="GREEN"
>  PURPLE
> 筛选ra的函数可以通过名字或颜色或打tags 来筛选。这里我选择用名字名字在筛选函数中  只能全匹配不能 like %name%
> 这样 所以查询先删除之前全部等于CVF 的代码。这里也可以打一个 tags 或者用颜色 
> 因为我想着 已提交阶段的alpha名字
> 在论坛里没看到有人使用它的文章
> 所以我这里就用了名字。
> Rame
> Custom UseT-Crealed Alpha name Must bean exaCT
> StrinB
> RIE
> goodalpha"
> Match
> TUtralzaton
> NEUTralization settinE
> Srrins  NONE , M-RKET
> SECTOR, INDUSTRYr
> neutralization =二"M-RKET
> SSUEINDUSTR

3. **“滚动三月”的动态标记逻辑**
   这是整个工具的核心。脚本会执行以下逻辑：
   - **计算评估窗口** ：脚本会自动获取当前日期，并计算出 **三个月前** 的日期作为评估窗口的开始（begin_date）。同时，它会与您设定的 tobe_consultant_day（顾问生效日）进行比较，取 **更晚的那个日期** 作为最终的窗口起点，确保只评估顾问期内的 Alpha。
   - **标记新 Alpha** ：遍历所有顾问期内提交的 Alpha，如果其提交日期落在评估窗口内，且名字 **不是**  "CVF"，脚本会自动将其命名为 "CVF"。
   - **取消旧标记** ：如果一个 Alpha 的提交日期在评估窗口 **之外** ，但其名字却 **是**  "CVF"（说明它是上个周期被标记的），脚本会自动将其名字删除（设置为 None）。
4. **区域性评估与触发条件**
   为了更细致地评估，脚本会按区域（如 EUR, USA 等）对 Alpha 进行分组统计。只有当某个区域内被标记为 "CVF" 的 Alpha 数量 **达到或超过10个** 时，脚本才会为该区域生成 SUPER Alpha。 RA去组SA 要求最少RA为10个。

### 工作原理解析

整个脚本的执行流程分为两个主要阶段：

#### 阶段一：动态标记 Regular Alphas

1. **初始化与日期计算** ：脚本启动，登录 BRAIN，并根据当前日期和您设置的 tobe_consultant_day 计算出最终的评估窗口 [begin_date, end_date)。
2. **获取数据** ：调用 get_submit_alphas 函数，获取您顾问生效日之后提交的所有 Regular Alphas 的信息（ID, Region, Name, DateSubmitted）。
3. **遍历与判断** ：
   - 循环遍历每一个获取到的 Alpha。
   - 判断其提交日期 submitted_date 是否在 [begin_date, end_date) 范围内。
   - **若在范围内** ：检查其名字。如果不是 "CVF"，则调用 up_alpha_properties 函数将其命名为 "CVF"。
   - **若在范围外** ：检查其名字。如果是 "CVF"，则调用 up_alpha_properties 函数将其名字删除。
4. **统计数量** ：在标记过程中，脚本会按区域统计符合条件的 "CVF" Alpha 数量，为下一阶段做准备。

#### 阶段二：生成并命名 SUPER Alphas

1. **构建回测任务** ：遍历上一阶段统计出的各区域 "CVF" 数量。如果某个区域的数量 >= 10，则构建一个 SUPER Alpha 的回测请求 item_data。其中关键配置为：
   - selection: 'own && name == "CVF"' (只选择我们标记的Alpha)
   - combo: '1' (简单求和)
   - settings.selectionLimit: 设为该区域的 "CVF" Alpha 数量。
2. **并行提交** ：使用 ThreadPoolExecutor (线程池)，将所有构建好的回测任务并行提交到 BRAIN 服务器。这大大提升了处理效率，尤其当您在多个区域都有足够数量的 Alpha 时。
3. **等待与获取结果** ：simulate_super_alpha 函数负责处理单个回测任务。它会提交请求，然后通过 wait_get 函数轮询检查回测状态，直到任务完成或失败。
4. **自动重命名** ：一旦一个 SUPER Alpha 成功生成，simulate_and_rename_super_alpha 函数会立即获取其 ID，并将其重命名为一个标准格式：YYYYMMDDVFT_{REGION}（例如：20250819VFT_EUR）。这便于您在平台上查找和管理这些每日生成的价值因子。

### 如何使用

本脚本被设计为“开箱即用”，您只需进行极少的配置。

#### 1. 前置准备

- 确保您的环境中已安装必要的库。
- 确保您的项目路径下有 machine_lib.py 文件，并且其中的 login() 函数可以正常工作（无需手动输入账号密码）。

#### 2. 唯一需要修改的参数

打开脚本，找到下面这行代码，将其中的日期修改为您 **正式成为顾问的日期** 。

```
# 全部代码中只需要修改一处  成为顾问的日期，也就是你alpha开始算钱的日子 ====================
tobe_consultant_day = "2025-04-14"
```

#### 3. 可选修改的参数

- **查询数量** ：如果您在顾问期间提交的 Regular Alphas 总数 **远大于1000** ，请修改下面这行代码中的 1000 为一个更大的数字。
  ```
  all_consultant_alphas = get_submit_alphas(s, tobe_consultant_day, end_date, 1000)
  ```
- **并发线程数** ：如果您希望调整同时进行回测的任务数量，可以修改 MAX_WORKERS 的值。
  Generated python
  ```
  MAX_WORKERS = 3
  ```

#### 4. 运行脚本

完成上述配置后，直接运行此 Python 脚本即可。它会自动完成所有的工作。

### 完整代码

```
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from machine_lib import *  # 假设 login() 在这里
from concurrent.futures import ThreadPoolExecutor, wait
import json

# ===================================================================
# PART 1: 函数定义
# ===================================================================

def up_alpha_properties(s, alpha_id, name: str = None):
    """
    一个简化的函数，专门用于修改alpha的名字。
    """
    if name is None:
        # 删除名字
        params = {"name": None}
    else:
        # 设置新名字
        params = {"name": name}

    response = s.patch(
        f"[链接已屏蔽] json=params
    )
    if response.status_code == 200:
        print(f"成功将 Alpha {alpha_id} 的名字修改为 '{name}'。")
    else:
        print(f"修改 Alpha {alpha_id} 名字失败，状态码: {response.status_code}, 信息: {response.text}")

REGIONS = {
            "USA": "TOP3000",
            "GLB": "TOP3000",
            "EUR": "TOP2500",
            "ASI": "MINVOL1M",
            "CHN": "TOP2000U",
            'KOR': 'TOP600',
            'TWN': 'TOP500',
            'HKG': 'TOP800',
            'JPN': 'TOP1600',
            'AMR': 'TOP600',
            # ... 只取其中一个就行了 因为无论选哪一个universe ，都会默认用该区域下的任何alpha
        }

def get_submit_alphas(s, start_date, end_date, alpha_num):
    # 此函数保持您提供的版本
    output = []
    count = 0
    for i in range(0, alpha_num, 100):
        print(f"正在获取第 {i} 到 {i + 100} 个 alpha...")
        url_e = f"[链接已屏蔽] \
                f"&status!=UNSUBMITTED%1FIS_FAIL&dateSubmitted>={start_date}T00:00:00-04:00" \
                f"&dateSubmitted<{end_date}T00:00:00-04:00&order=-is.sharpe&hidden=false&type!=SUPER&settings.delay=1"
        try:
            response = s.get(url_e)
            response.raise_for_status()
            alpha_list = response.json()["results"]
            if not alpha_list:
                print("已获取所有符合条件的 alpha。")
                break
            for j in range(len(alpha_list)):
                alpha_id = alpha_list[j]["id"]
                region = alpha_list[j]["settings"]["region"]
                name = alpha_list[j]["name"]
                dateSubmitted = alpha_list[j]['dateSubmitted']
                rec = [alpha_id, region, name, dateSubmitted]
                output.append(rec)
            count += len(alpha_list)
        except Exception as e:
            print(f"获取alpha时发生异常: {e}")
            resp = s.get('[链接已屏蔽])
            if resp.status_code != 200:
                print(f"用户会话可能已过期，状态码: {resp.status_code}")
            break
    print(f"总共获取了 {len(output)} 个 alphas。")
    return output

def wait_get(s, url: str, max_retries: int = 10) -> "Response":
    """发送带有重试机制的 GET 请求。"""
    retries = 0
    while retries < max_retries:
        while True:
            simulation_progress = s.get(url)
            if simulation_progress.headers.get("Retry-After", 0) == 0:
                break
            time.sleep(float(simulation_progress.headers["Retry-After"]))
        if simulation_progress.status_code < 400:
            if "ERROR" in simulation_progress.text:
                try:
                    data = simulation_progress.json()
                    message = data.get("message")
                    print(f"回测检查失败 {url}：{message}")
                except json.JSONDecodeError:
                    print(f"回测检查失败 {url}：{simulation_progress.text}")
            return simulation_progress
        else:
            time.sleep(2 ** retries)
            retries += 1
    print(f"达到最大重试次数后，获取 {url} 仍然失败。")
    return simulation_progress

def simulate_super_alpha(s, data, alpha_fail_attempt_tolerance=5):
    """提交SUPER alpha回测，等待完成，并返回alpha ID。"""
    failure_count = 0
    while failure_count < alpha_fail_attempt_tolerance:
        try:
            print(f"正在为区域 {data['settings']['region']} 提交SUPER alpha回测...")
            simulation_response = s.post('[链接已屏蔽] json=data)
            simulation_response.raise_for_status()  # 检查提交是否成功

            simulation_progress_url = simulation_response.headers['Location']
            child_id = simulation_progress_url.split('/')[-1]

            print(f"回测任务 {child_id} 已提交，正在等待结果...")
            child_progress_response = wait_get(s, f'[链接已屏蔽])

            if child_progress_response.status_code == 200:
                child_progress = child_progress_response.json()
                if child_progress['status'] in ['COMPLETE', 'WARNING']:
                    print(f"回测 {child_id} 成功！新的 SUPER alpha ID: {child_progress['alpha']}")
                    return child_progress['alpha']  # 成功，返回 alpha ID
                else:
                    print(
                        f"回测 {child_id} 失败或被取消，状态: {child_progress['status']}, 原因: {child_progress.get('message')}")
                    return None  # 回测失败
            else:
                print(f"获取回测结果 {child_id} 失败，状态码: {child_progress_response.status_code}")
                failure_count += 1
                time.sleep(15)

        except Exception as e:
            print(f"提交回测或等待过程中发生异常: {e}。正在重试...")
            time.sleep(15)
            failure_count += 1
            if failure_count % 3 == 0:  # 每3次失败重新登录一下
                print("尝试重新登录...")
                s = login()

    print(f"为区域 {data['settings']['region']} 的回测任务失败次数过多，放弃。")
    return None  # 多次失败后，返回 None

def simulate_and_rename_super_alpha(s, item_data):
    """完整流程：提交、等待、成功后重命名"""
    new_alpha_id = simulate_super_alpha(s, item_data)

    if new_alpha_id:
        # 生成新名字，例如：20250819VFT_EUR
        today_str = datetime.now().strftime("%Y%m%d")
        region = item_data["settings"]["region"]
        new_name = f"{today_str}VFT_{region}"

        print(f"准备将新的 SUPER alpha {new_alpha_id} 重命名为 '{new_name}'...")
        up_alpha_properties(s, new_alpha_id, name=new_name)
    else:
        print(f"由于区域 {item_data['settings']['region']} 的SUPER alpha创建失败，跳过重命名。")

# ===================================================================
# PART 2: 主逻辑
# ===================================================================

s = login()

# --- 阶段一：标记Regular Alphas ---
tobe_consultant_day = "2025-04-14"  # 全部代码中只需要修改一处  成为顾问的日期，也就是你alpha开始算钱的日子 ====================
calculate_month = datetime.now().strftime("%Y-%m")
calc_month_obj = datetime.strptime(calculate_month, "%Y-%m")
begin_date_obj = calc_month_obj - relativedelta(months=3)
begin_date = begin_date_obj.strftime("%Y-%m-%d")
end_date_obj = datetime.now() + timedelta(days=1)
end_date = end_date_obj.strftime("%Y-%m-%d")

print("配置信息:")
print(f"自动获取的计算月份: {calculate_month}")
print(f"顾问开始日: {tobe_consultant_day}")
if tobe_consultant_day > begin_date:
    print(f"顾问开始日晚于计算日期，将使用顾问开始日作为有效起始点。")
    begin_date = tobe_consultant_day
print(f"最终生效的VF窗口开始日期: {begin_date}")
print("-" * 30)

all_consultant_alphas = get_submit_alphas(s, tobe_consultant_day, end_date, 1000)

print("\n开始处理 Regular Alphas...")
begin_date_compare = datetime.strptime(begin_date, "%Y-%m-%d").date()
end_date_compare = datetime.strptime(end_date, "%Y-%m-%d").date()
regions_num = {}

for alpha_data in all_consultant_alphas:
    alpha_id, region, alpha_name, date_submitted_str = alpha_data
    if region not in regions_num:
        regions_num[region] = 0

    submitted_date = datetime.fromisoformat(date_submitted_str).date()

    if begin_date_compare <= submitted_date < end_date_compare:
        regions_num[region] += 1
        if alpha_name != "CVF":
            up_alpha_properties(s, alpha_id, name="CVF")
    else:
        if alpha_name == "CVF":
            up_alpha_properties(s, alpha_id, name=None)

# --- 阶段二：创建和重命名SUPER Alphas ---
print("\n开始创建 SUPER Alphas...")
sim_data_list = []
for query_region, num in regions_num.items():
    if num >= 10:  # 只有当一个区域有足够数量的CVF alpha时才创建
        print(f"区域 {query_region} 有 {num} 个CVF alpha，符合创建SUPER alpha的条件。")
        item_data = {
            "type": "SUPER",
            "settings": {
                "nanHandling": "OFF", "instrumentType": "EQUITY", "delay": 1,
                "universe": REGIONS.get(query_region, "TOP3000"),  # 使用.get()更安全
                "truncation": 0.01, "unitHandling": "VERIFY", "selectionLimit": num,
                "selectionHandling": "POSITIVE", "pasteurization": "ON", "region": query_region,
                "language": "FASTEXPR", "decay": 5, "neutralization": "INDUSTRY",
                "visualization": False, "testPeriod": "P2Y",
            },
            "combo": '1', "selection": 'own&&name == \"CVF\"',
        }
        if query_region in ["ASI"]:
            item_data["settings"]["maxTrade"] = "ON"
        sim_data_list.append(item_data)

if not sim_data_list:
    print("\n没有需要创建的 SUPER alpha。程序结束。")
else:
    # 使用线程池并行处理
    MAX_WORKERS = 2
    print(f"\n准备使用 {MAX_WORKERS} 个线程并行创建和重命名 {len(sim_data_list)} 个 SUPER alpha...")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 提交所有任务
        futures = [executor.submit(simulate_and_rename_super_alpha, s, batch) for batch in sim_data_list]
        # 等待所有任务完成
        wait(futures)

    print("\n所有滚动检测并生成SA处理任务已完成。")
```

运行截图：
 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page size
> 100
> OUt Of 306
> Filter
> 选中时间内的alpha 都被修改了名字
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Delay
> Neutralization
> Sharpe
> Returns
> Turnover
> Submission Date
> (EST)
> Searcn
> Selec
> Selec
> Selec
> Searcn
> Selec
> Selec
> Selec
> Selec
> e.6> 1
> e.6> 1
> e.6> 1
> Selec
> Searcn
> CF
> Regular
> ACTIVE
> 07/24/2025 EDT
> EUR
> TOP2500
> Fas- Factors
> PowerPoolSelec.
> 07/24/2025 EDT
> CF
> Regular
> ACTIVE
> 07/24/2025 EDT
> GLB
> TOPDN3OOO
> RAll
> PowerPoolSelec.
> 07/24/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/23/2025 EDT
> US4
> TOP3OOD
> SIOw
> Fast Fact:
> 07/24/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/22/2025 EDT
> US4
> T0P3000
> SIOw
> Fast Fact:
> 07/23/2025 EDT
> CF
> Regular
> ACTIVE
> 07/23/2025 EDT
> GLB
> TOPDN3OOO
> Subindusry
> PowerPoolSelec.
> 07/2312025 EDT
> CF
> Regular
> ACTIVE
> 07/22/2025 EDT
> EUR
> T0P2500
> Sector
> PowerPoolSelec.
> 07/2312025 EDT
> Regular
> ACTIVE
> 07/23/2025 EDT
> EUR
> TOPZSOD
> Subindusy
> PowerPoolSelec.
> 07/2312025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/22/2025 EDT
> US4
> ILLIQUID_MINV。
> Marke
> 07/22/2025 EDT
> CVF
> Regular
> ACTIVE
> 07/21/2025 EDT
> GLB
> TOPDN3OOO
> RAN
> PowerPoolSalsc:
> 07/22/2025 EDT
> CVF
> Regular
> ACTIVE
> 07/21/2025 EDT
> GLB
> TOPDN3OOO
> RAN
> PowerPoolSalsc:
> 07/22/2025 EDT
> CF
> Regular
> ACTIVE
> 07/21/2025 EDT
> GLB
> TOPDI3OO0
> Crowdins Factors
> PowerPoolSelec.
> 07/21/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/20/2025 EDT
> GLB
> MINVOLIN
> Szaziszical
> 07/21/2025 EDT
> CF
> Regular
> ACTIVE
> 07/20/2025 EDT
> EUR
> TOP2500
> Subindusry
> PowerPoolSelec.
> 07/21/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/19/2025 EDT
> US4
> T0P3000
> Marke
> 07/20/2025 EDT
> RaUlar
> ACTIVE
> 071012025 COT
> TOPI000
> Fl!
> Pos Dclcsl=r
> 071022025 FOT
> Tag



> [!NOTE] [图片 OCR 识别内容]
> 配置信息:
> 自动获取的计算月份:  2025-07
> VF 计算比如今天是7月26
> 那么实际上计算是 456月提交的alpha
> 顾问开始日:
> 2025-04-14
> 但是我这里要实现滚动监测,那么就精确到本月+1天。也就是 7月27
> 顾问开始日晚于计算日期将使用顾问开始日作为有效起始点。
> 最终生效的V窗口开始日期:
> 2025-04-14
> 正在获取第  0  到  100
> alpha
> 正在获取第  100  到
> 200
> alpha
> 已提交阶段
> 正在获取笫  200  到
> 300
> alpha
> 己获取所有符合条件的 alpha。
> 总共获取了
> 157
> 个
> alphas。
> 注意:  代码会去修改alpha 的名字。如果名字对你有其他用
> 途
> 请改成用颜色
> 开始处理 Regular Alphas 
> 成功将 Alpha
> eN2gonM 的名字修改为
> 'CVF'
> 成功将 Alpha 0Rb5827 的名字修改为 'CVF'
> 成功将 Alpha 6OPJNKp 的名字修改为 'CVF'
> 成功将 Alpha
> nmoxgQq 的名字修改为
> 'CVF'
> 成功将 Alpha Sp7delo 的名字修改为
> 'CVF'
> 成功将 Alpha
> 8V22202  的名字修改为
> 'CVF'
> 成功将 Alpha 3GQOSMN 的名字修改为
> 'CVF'
> 成功将 Alpha
> LE7Qmxe  的名字修改为 'CVF'
> 成功将 AZpha gdGLSxe 的名字修改为 'CVF
> 成功将 Alpha
> XVnMOn 的名字修改为
> 'CVF'
> 成功将
> Aloha
> mlOW8M9
> 的名宰修改为
> 'CVF



> [!NOTE] [图片 OCR 识别内容]
> 自动获取的计算月份:
> 2025-08
> 顾问开始日:
> 2025-04-14
> 我修改了本机电脑时间为8月19号
> 那么检测VF 的SA 选择时间为  5月1号
> 8月20号,
> 当然如
> 最终生效的V窗口开始日期:
> 2025-05-01
> 果开始时间早于顾问生效时间。那么开始时间则是 顾问生效时间。
> 正在获取第
> 0到  100
> alpha
> 正在获取第
> 100  到
> 200
> alpha
> 正在获取第
> 200  到  300
> 个 alpha_
> 己获取所有符合条件的 alpha。
> 总共获取了
> 180
> alphas
> 开始处理 Regular Alphas _
> 开始创建
> SUPER
> Alphas
> 区域 EUR 有
> 51
> 个CVF alpha, 符合创建SUPER alpha的条件。
> 区域 USA 有
> 68
> 个CVF alpha, 符合创建SUPER alpha的条件:
> 区域 BLB 有 33
> 个CVF alpha, 符合创建SUPER alpha的条件:
> 区域 ASI
> 有
> 20
> 个CVF alpha, 符合创建SUPER alpha的条件。
> 程序会生成super alpha, 请减少或暂停你正在生成 $A的程序
> 准备使用
> 2  个线程并行创建和重命名
> 个
> SUPER alpha
> 正在为区域 EUR 提交SUPER alpha回测
> 正在为区域 USA 提交SUPER alpha回测.
> 回测任务 BbUMKLeCZGNZCGEVOOCjNWNW
> 己提交,正在等待结果
> 回测任务
> SOOWe2UBGWTblhl2Ta2sZb
> 己提交。正在等待结果



> [!NOTE] [图片 OCR 识别内容]
> 岂^
> Simulate
> Alphas
> Learn
> Data
> 罟
> Labs
> Genius
> 思 Competitions (3)
> Community
> g
> Refer
> friend
> Worldquant BRNINis experiencing Some
> UNSUB
> Created 07/25/2025 EDT
> 20250726VFT_USA
> Add Alpha t0
> Lst
> Openalpha details in newtab
> Alphas
> Unsubmitted
> Submitted 
> Code
> 生成好了 alpha 的名字
> Selection Expression
> Page size 
> 100
> 0Ut0f
> 000+
> Ownggname
> "CVF"
> Combo Expression
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Searcn
> Select
> SupEr
> Select
> Searcn
> Select
> 20250726VFT。
> SuPEr
> UNSUBNITTED
> 07125/2025 EDT
> UIS4
> Simulation Settings
> Instrument Type
> Region
> Universe
> LangUage
> Decay
> Delay
> Truncatijon
> Neutralization
> Pasteuriatijon
> NaN Handling
> Unit Handling
> MaxTrade
> CoIpO
> 20250726VFT_E
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> ElR
> Equity
> 054
> TCP3000
> Fast Erpression
> 0.01
> Industy
> Verify
> anonymoUs
> SuPEr
> UNSUBNITTED
> 07125/2025 EDT
> ElR
> 20250726VFT_ASI
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> anonymaUs
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> Clone Alpha
> 20250726VFT_G.
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> GLB
> 20250819VFT_U.
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> UIS4
> Show test period
> Test period and overall stats are hidden by default when test period is specified.
> 20250819VFT_E
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> ElR
> anonymaUs
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> ElR


---

### 帖子 #4: --- 阶段二：创建和重命名SUPER Alphas ---
- **主帖链接**: https://support.worldquantbrain.comValueFactor 预测器自动化滚动3个月 Alpha 表现评估代码优化_33729239058839.md
- **讨论数**: 6

**开箱即用，助您洞悉近期alpha提交的质量**

### 引言：为何需要这个工具？

作为一名 因子挖掘者，如何客观、持续地评估自己提交alpha的表现？我们提交的 Alpha 数量众多，手动去筛选、组合、回测最近几个月的成果，不仅耗时耗力，而且难以形成统一的评估标准。

这个工具旨在解决这一痛点。它能自动化地完成以下任务：

1. **动态筛选** ：自动识别并标记出您最近三个月内提交的 Regular Alphas。
2. **智能组合** ：将标记出的 Alphas 按区域（Region）分组，并为每个符合条件的区域生成一个 SUPER Alpha。
3. **客观评估** ：这个生成的 SUPER Alpha 本身就是一个“价值因子”（Value Factor），它的表现直观地反映了您近期研发工作的综合成效。
4. **自动化流程** ：整个过程通过一个脚本全自动执行，您只需设置一次自己的“顾问生效日期”，即可每日运行，持续追踪。

### 核心理念与设计思路

在深入代码之前，理解其背后的设计思想至关重要。

1. **为何不直接用 Selection Expression？**
   BRAIN 平台的 SUPER Alpha 在选择子 Alpha 时，默认会优先选择 **最早提交** 的 Alpha。这与我们希望评估 **近期表现** 的目标背道而驰。因此，我们不能简单地依赖 selectionLimit，而必须采用一种方式主动筛选出我们想要的 Alpha。
   
> [!NOTE] [图片 OCR 识别内容]
> 瞿SeBCC
> 仕
> CeRBEsgn 填
> OWh
> Combo Expression 填1
> setting 中
> Selection Limit = 26 的条件下 Ealpha 按时间顺序选择选择之前莳不选择最
> 近提交的 所以这样不去修改alpha属性筛选实现不了这个功能。
> Selected Alphas
> 26 Alphas have been selecte
> View
> Nam
> UniVerse
> TUINOeT
> Ftness
> Returs
> Drawdown
> Marqin
> CF
> TCP250
> 2.75
> 23.524
> 1.27
> 5054
> 1.754
> 4.2586oo
> CF
> TCP2500
> 2.23
> 17.054
> 1.19
> G5
> G5
> 456oo
> CF
> TCP250
> 1.554
> 3.534
> 12.-04
> 104.975500
> CF
> TCP2500
> 1.784
> 7.101
> 384
> 79.63530
> CVF
> TCP2500
> 3.06
> 36.634
> .651:
> 354
> ~275530
> Sharpe

2. **为什么选择用“名字(Name)”进行标记？
   对于RA 的名字的修改只修改已提交阶段的，不影响如果你在未提交阶段对于RA 名字的操作，已提交阶段的alpha 名字用的人应该少吧。**
   为了让 SUPER Alpha 能精准地选中我们想要的子 Alpha，我们需要一个“标记”。通过 API，我们可以修改 Alpha 的名字（Name）或颜色（Color）或打一个Tags 。本脚本选择使用名字，将目标 Alpha 命名为  **"CVF"** （可理解为 Calculate Value Factor）。这样，在 SUPER Alpha 的 Selection Expression 中，我们就可以使用 own && name == "CVF" 来精确抓取这些被选中的 Alpha。
   
> [!NOTE] [图片 OCR 识别内容]
> CaEEON
> User-SEleted CECEEONY
> Strine 'NONE"
> PZICEZEIERSION,
> CaTEEONJ
> NONE"
>  RICENOMENTN"IOLUME
> FUNDALIENT-L"'
> IANALYST
> PRICEVOLUME ,
> RELATION
> SENTINEIIT
> COIOT
> Us=rselzczd Colar
> Sirine:"NONE"
> REDIVELON GREEN
> BLVE
> Color="GREEN"
>  PURPLE
> 筛选ra的函数可以通过名字或颜色或打tags 来筛选。这里我选择用名字名字在筛选函数中  只能全匹配不能 like %name%
> 这样 所以查询先删除之前全部等于CVF 的代码。这里也可以打一个 tags 或者用颜色 
> 因为我想着 已提交阶段的alpha名字
> 在论坛里没看到有人使用它的文章
> 所以我这里就用了名字。
> Rame
> Custom UseT-Crealed Alpha name Must bean exaCT
> StrinB
> RIE
> goodalpha"
> Match
> TUtralzaton
> NEUTralization settinE
> Srrins  NONE , M-RKET
> SECTOR, INDUSTRYr
> neutralization =二"M-RKET
> SSUEINDUSTR

3. **“滚动三月”的动态标记逻辑**
   这是整个工具的核心。脚本会执行以下逻辑：
   - **计算评估窗口** ：脚本会自动获取当前日期，并计算出 **三个月前** 的日期作为评估窗口的开始（begin_date）。同时，它会与您设定的 tobe_consultant_day（顾问生效日）进行比较，取 **更晚的那个日期** 作为最终的窗口起点，确保只评估顾问期内的 Alpha。
   - **标记新 Alpha** ：遍历所有顾问期内提交的 Alpha，如果其提交日期落在评估窗口内，且名字 **不是**  "CVF"，脚本会自动将其命名为 "CVF"。
   - **取消旧标记** ：如果一个 Alpha 的提交日期在评估窗口 **之外** ，但其名字却 **是**  "CVF"（说明它是上个周期被标记的），脚本会自动将其名字删除（设置为 None）。
4. **区域性评估与触发条件**
   为了更细致地评估，脚本会按区域（如 EUR, USA 等）对 Alpha 进行分组统计。只有当某个区域内被标记为 "CVF" 的 Alpha 数量 **达到或超过10个** 时，脚本才会为该区域生成 SUPER Alpha。 RA去组SA 要求最少RA为10个。

### 工作原理解析

整个脚本的执行流程分为两个主要阶段：

#### 阶段一：动态标记 Regular Alphas

1. **初始化与日期计算** ：脚本启动，登录 BRAIN，并根据当前日期和您设置的 tobe_consultant_day 计算出最终的评估窗口 [begin_date, end_date)。
2. **获取数据** ：调用 get_submit_alphas 函数，获取您顾问生效日之后提交的所有 Regular Alphas 的信息（ID, Region, Name, DateSubmitted）。
3. **遍历与判断** ：
   - 循环遍历每一个获取到的 Alpha。
   - 判断其提交日期 submitted_date 是否在 [begin_date, end_date) 范围内。
   - **若在范围内** ：检查其名字。如果不是 "CVF"，则调用 up_alpha_properties 函数将其命名为 "CVF"。
   - **若在范围外** ：检查其名字。如果是 "CVF"，则调用 up_alpha_properties 函数将其名字删除。
4. **统计数量** ：在标记过程中，脚本会按区域统计符合条件的 "CVF" Alpha 数量，为下一阶段做准备。

#### 阶段二：生成并命名 SUPER Alphas

1. **构建回测任务** ：遍历上一阶段统计出的各区域 "CVF" 数量。如果某个区域的数量 >= 10，则构建一个 SUPER Alpha 的回测请求 item_data。其中关键配置为：
   - selection: 'own && name == "CVF"' (只选择我们标记的Alpha)
   - combo: '1' (简单求和)
   - settings.selectionLimit: 设为该区域的 "CVF" Alpha 数量。
2. **并行提交** ：使用 ThreadPoolExecutor (线程池)，将所有构建好的回测任务并行提交到 BRAIN 服务器。这大大提升了处理效率，尤其当您在多个区域都有足够数量的 Alpha 时。
3. **等待与获取结果** ：simulate_super_alpha 函数负责处理单个回测任务。它会提交请求，然后通过 wait_get 函数轮询检查回测状态，直到任务完成或失败。
4. **自动重命名** ：一旦一个 SUPER Alpha 成功生成，simulate_and_rename_super_alpha 函数会立即获取其 ID，并将其重命名为一个标准格式：YYYYMMDDVFT_{REGION}（例如：20250819VFT_EUR）。这便于您在平台上查找和管理这些每日生成的价值因子。

### 如何使用

本脚本被设计为“开箱即用”，您只需进行极少的配置。

#### 1. 前置准备

- 确保您的环境中已安装必要的库。
- 确保您的项目路径下有 machine_lib.py 文件，并且其中的 login() 函数可以正常工作（无需手动输入账号密码）。

#### 2. 唯一需要修改的参数

打开脚本，找到下面这行代码，将其中的日期修改为您 **正式成为顾问的日期** 。

```
# 全部代码中只需要修改一处  成为顾问的日期，也就是你alpha开始算钱的日子 ====================
tobe_consultant_day = "2025-04-14"
```

#### 3. 可选修改的参数

- **查询数量** ：如果您在顾问期间提交的 Regular Alphas 总数 **远大于1000** ，请修改下面这行代码中的 1000 为一个更大的数字。
  ```
  all_consultant_alphas = get_submit_alphas(s, tobe_consultant_day, end_date, 1000)
  ```
- **并发线程数** ：如果您希望调整同时进行回测的任务数量，可以修改 MAX_WORKERS 的值。
  Generated python
  ```
  MAX_WORKERS = 3
  ```

#### 4. 运行脚本

完成上述配置后，直接运行此 Python 脚本即可。它会自动完成所有的工作。

### 完整代码

```
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from machine_lib import *  # 假设 login() 在这里
from concurrent.futures import ThreadPoolExecutor, wait
import json

# ===================================================================
# PART 1: 函数定义
# ===================================================================

def up_alpha_properties(s, alpha_id, name: str = None):
    """
    一个简化的函数，专门用于修改alpha的名字。
    """
    if name is None:
        # 删除名字
        params = {"name": None}
    else:
        # 设置新名字
        params = {"name": name}

    response = s.patch(
        f"[链接已屏蔽] json=params
    )
    if response.status_code == 200:
        print(f"成功将 Alpha {alpha_id} 的名字修改为 '{name}'。")
    else:
        print(f"修改 Alpha {alpha_id} 名字失败，状态码: {response.status_code}, 信息: {response.text}")

REGIONS = {
            "USA": "TOP3000",
            "GLB": "TOP3000",
            "EUR": "TOP2500",
            "ASI": "MINVOL1M",
            "CHN": "TOP2000U",
            'KOR': 'TOP600',
            'TWN': 'TOP500',
            'HKG': 'TOP800',
            'JPN': 'TOP1600',
            'AMR': 'TOP600',
            # ... 只取其中一个就行了 因为无论选哪一个universe ，都会默认用该区域下的任何alpha
        }

def get_submit_alphas(s, start_date, end_date, alpha_num):
    # 此函数保持您提供的版本
    output = []
    count = 0
    for i in range(0, alpha_num, 100):
        print(f"正在获取第 {i} 到 {i + 100} 个 alpha...")
        url_e = f"[链接已屏蔽] \
                f"&status!=UNSUBMITTED%1FIS_FAIL&dateSubmitted>={start_date}T00:00:00-04:00" \
                f"&dateSubmitted<{end_date}T00:00:00-04:00&order=-is.sharpe&hidden=false&type!=SUPER&settings.delay=1"
        try:
            response = s.get(url_e)
            response.raise_for_status()
            alpha_list = response.json()["results"]
            if not alpha_list:
                print("已获取所有符合条件的 alpha。")
                break
            for j in range(len(alpha_list)):
                alpha_id = alpha_list[j]["id"]
                region = alpha_list[j]["settings"]["region"]
                name = alpha_list[j]["name"]
                dateSubmitted = alpha_list[j]['dateSubmitted']
                rec = [alpha_id, region, name, dateSubmitted]
                output.append(rec)
            count += len(alpha_list)
        except Exception as e:
            print(f"获取alpha时发生异常: {e}")
            resp = s.get('[链接已屏蔽])
            if resp.status_code != 200:
                print(f"用户会话可能已过期，状态码: {resp.status_code}")
            break
    print(f"总共获取了 {len(output)} 个 alphas。")
    return output

def wait_get(s, url: str, max_retries: int = 10) -> "Response":
    """发送带有重试机制的 GET 请求。"""
    retries = 0
    while retries < max_retries:
        while True:
            simulation_progress = s.get(url)
            if simulation_progress.headers.get("Retry-After", 0) == 0:
                break
            time.sleep(float(simulation_progress.headers["Retry-After"]))
        if simulation_progress.status_code < 400:
            if "ERROR" in simulation_progress.text:
                try:
                    data = simulation_progress.json()
                    message = data.get("message")
                    print(f"回测检查失败 {url}：{message}")
                except json.JSONDecodeError:
                    print(f"回测检查失败 {url}：{simulation_progress.text}")
            return simulation_progress
        else:
            time.sleep(2 ** retries)
            retries += 1
    print(f"达到最大重试次数后，获取 {url} 仍然失败。")
    return simulation_progress

def simulate_super_alpha(s, data, alpha_fail_attempt_tolerance=5):
    """提交SUPER alpha回测，等待完成，并返回alpha ID。"""
    failure_count = 0
    while failure_count < alpha_fail_attempt_tolerance:
        try:
            print(f"正在为区域 {data['settings']['region']} 提交SUPER alpha回测...")
            simulation_response = s.post('[链接已屏蔽] json=data)
            simulation_response.raise_for_status()  # 检查提交是否成功

            simulation_progress_url = simulation_response.headers['Location']
            child_id = simulation_progress_url.split('/')[-1]

            print(f"回测任务 {child_id} 已提交，正在等待结果...")
            child_progress_response = wait_get(s, f'[链接已屏蔽])

            if child_progress_response.status_code == 200:
                child_progress = child_progress_response.json()
                if child_progress['status'] in ['COMPLETE', 'WARNING']:
                    print(f"回测 {child_id} 成功！新的 SUPER alpha ID: {child_progress['alpha']}")
                    return child_progress['alpha']  # 成功，返回 alpha ID
                else:
                    print(
                        f"回测 {child_id} 失败或被取消，状态: {child_progress['status']}, 原因: {child_progress.get('message')}")
                    return None  # 回测失败
            else:
                print(f"获取回测结果 {child_id} 失败，状态码: {child_progress_response.status_code}")
                failure_count += 1
                time.sleep(15)

        except Exception as e:
            print(f"提交回测或等待过程中发生异常: {e}。正在重试...")
            time.sleep(15)
            failure_count += 1
            if failure_count % 3 == 0:  # 每3次失败重新登录一下
                print("尝试重新登录...")
                s = login()

    print(f"为区域 {data['settings']['region']} 的回测任务失败次数过多，放弃。")
    return None  # 多次失败后，返回 None

def simulate_and_rename_super_alpha(s, item_data):
    """完整流程：提交、等待、成功后重命名"""
    new_alpha_id = simulate_super_alpha(s, item_data)

    if new_alpha_id:
        # 生成新名字，例如：20250819VFT_EUR
        today_str = datetime.now().strftime("%Y%m%d")
        region = item_data["settings"]["region"]
        new_name = f"{today_str}VFT_{region}"

        print(f"准备将新的 SUPER alpha {new_alpha_id} 重命名为 '{new_name}'...")
        up_alpha_properties(s, new_alpha_id, name=new_name)
    else:
        print(f"由于区域 {item_data['settings']['region']} 的SUPER alpha创建失败，跳过重命名。")

# ===================================================================
# PART 2: 主逻辑
# ===================================================================

s = login()

# --- 阶段一：标记Regular Alphas ---
tobe_consultant_day = "2025-04-14"  # 全部代码中只需要修改一处  成为顾问的日期，也就是你alpha开始算钱的日子 ====================
calculate_month = datetime.now().strftime("%Y-%m")
calc_month_obj = datetime.strptime(calculate_month, "%Y-%m")
begin_date_obj = calc_month_obj - relativedelta(months=3)
begin_date = begin_date_obj.strftime("%Y-%m-%d")
end_date_obj = datetime.now() + timedelta(days=1)
end_date = end_date_obj.strftime("%Y-%m-%d")

print("配置信息:")
print(f"自动获取的计算月份: {calculate_month}")
print(f"顾问开始日: {tobe_consultant_day}")
if tobe_consultant_day > begin_date:
    print(f"顾问开始日晚于计算日期，将使用顾问开始日作为有效起始点。")
    begin_date = tobe_consultant_day
print(f"最终生效的VF窗口开始日期: {begin_date}")
print("-" * 30)

all_consultant_alphas = get_submit_alphas(s, tobe_consultant_day, end_date, 1000)

print("\n开始处理 Regular Alphas...")
begin_date_compare = datetime.strptime(begin_date, "%Y-%m-%d").date()
end_date_compare = datetime.strptime(end_date, "%Y-%m-%d").date()
regions_num = {}

for alpha_data in all_consultant_alphas:
    alpha_id, region, alpha_name, date_submitted_str = alpha_data
    if region not in regions_num:
        regions_num[region] = 0

    submitted_date = datetime.fromisoformat(date_submitted_str).date()

    if begin_date_compare <= submitted_date < end_date_compare:
        regions_num[region] += 1
        if alpha_name != "CVF":
            up_alpha_properties(s, alpha_id, name="CVF")
    else:
        if alpha_name == "CVF":
            up_alpha_properties(s, alpha_id, name=None)

# --- 阶段二：创建和重命名SUPER Alphas ---
print("\n开始创建 SUPER Alphas...")
sim_data_list = []
for query_region, num in regions_num.items():
    if num >= 10:  # 只有当一个区域有足够数量的CVF alpha时才创建
        print(f"区域 {query_region} 有 {num} 个CVF alpha，符合创建SUPER alpha的条件。")
        item_data = {
            "type": "SUPER",
            "settings": {
                "nanHandling": "OFF", "instrumentType": "EQUITY", "delay": 1,
                "universe": REGIONS.get(query_region, "TOP3000"),  # 使用.get()更安全
                "truncation": 0.01, "unitHandling": "VERIFY", "selectionLimit": num,
                "selectionHandling": "POSITIVE", "pasteurization": "ON", "region": query_region,
                "language": "FASTEXPR", "decay": 5, "neutralization": "INDUSTRY",
                "visualization": False, "testPeriod": "P2Y",
            },
            "combo": '1', "selection": 'own&&name == \"CVF\"',
        }
        if query_region in ["ASI"]:
            item_data["settings"]["maxTrade"] = "ON"
        sim_data_list.append(item_data)

if not sim_data_list:
    print("\n没有需要创建的 SUPER alpha。程序结束。")
else:
    # 使用线程池并行处理
    MAX_WORKERS = 2
    print(f"\n准备使用 {MAX_WORKERS} 个线程并行创建和重命名 {len(sim_data_list)} 个 SUPER alpha...")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 提交所有任务
        futures = [executor.submit(simulate_and_rename_super_alpha, s, batch) for batch in sim_data_list]
        # 等待所有任务完成
        wait(futures)

    print("\n所有滚动检测并生成SA处理任务已完成。")
```

运行截图：
 
> [!NOTE] [图片 OCR 识别内容]
> Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Page size
> 100
> OUt Of 306
> Filter
> 选中时间内的alpha 都被修改了名字
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Delay
> Neutralization
> Sharpe
> Returns
> Turnover
> Submission Date
> (EST)
> Searcn
> Selec
> Selec
> Selec
> Searcn
> Selec
> Selec
> Selec
> Selec
> e.6> 1
> e.6> 1
> e.6> 1
> Selec
> Searcn
> CF
> Regular
> ACTIVE
> 07/24/2025 EDT
> EUR
> TOP2500
> Fas- Factors
> PowerPoolSelec.
> 07/24/2025 EDT
> CF
> Regular
> ACTIVE
> 07/24/2025 EDT
> GLB
> TOPDN3OOO
> RAll
> PowerPoolSelec.
> 07/24/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/23/2025 EDT
> US4
> TOP3OOD
> SIOw
> Fast Fact:
> 07/24/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/22/2025 EDT
> US4
> T0P3000
> SIOw
> Fast Fact:
> 07/23/2025 EDT
> CF
> Regular
> ACTIVE
> 07/23/2025 EDT
> GLB
> TOPDN3OOO
> Subindusry
> PowerPoolSelec.
> 07/2312025 EDT
> CF
> Regular
> ACTIVE
> 07/22/2025 EDT
> EUR
> T0P2500
> Sector
> PowerPoolSelec.
> 07/2312025 EDT
> Regular
> ACTIVE
> 07/23/2025 EDT
> EUR
> TOPZSOD
> Subindusy
> PowerPoolSelec.
> 07/2312025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/22/2025 EDT
> US4
> ILLIQUID_MINV。
> Marke
> 07/22/2025 EDT
> CVF
> Regular
> ACTIVE
> 07/21/2025 EDT
> GLB
> TOPDN3OOO
> RAN
> PowerPoolSalsc:
> 07/22/2025 EDT
> CVF
> Regular
> ACTIVE
> 07/21/2025 EDT
> GLB
> TOPDN3OOO
> RAN
> PowerPoolSalsc:
> 07/22/2025 EDT
> CF
> Regular
> ACTIVE
> 07/21/2025 EDT
> GLB
> TOPDI3OO0
> Crowdins Factors
> PowerPoolSelec.
> 07/21/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/20/2025 EDT
> GLB
> MINVOLIN
> Szaziszical
> 07/21/2025 EDT
> CF
> Regular
> ACTIVE
> 07/20/2025 EDT
> EUR
> TOP2500
> Subindusry
> PowerPoolSelec.
> 07/21/2025 EDT
> anonymoUs
> Super
> ACTIVE
> 07/19/2025 EDT
> US4
> T0P3000
> Marke
> 07/20/2025 EDT
> RaUlar
> ACTIVE
> 071012025 COT
> TOPI000
> Fl!
> Pos Dclcsl=r
> 071022025 FOT
> Tag



> [!NOTE] [图片 OCR 识别内容]
> 配置信息:
> 自动获取的计算月份:  2025-07
> VF 计算比如今天是7月26
> 那么实际上计算是 456月提交的alpha
> 顾问开始日:
> 2025-04-14
> 但是我这里要实现滚动监测,那么就精确到本月+1天。也就是 7月27
> 顾问开始日晚于计算日期将使用顾问开始日作为有效起始点。
> 最终生效的V窗口开始日期:
> 2025-04-14
> 正在获取第  0  到  100
> alpha
> 正在获取第  100  到
> 200
> alpha
> 已提交阶段
> 正在获取笫  200  到
> 300
> alpha
> 己获取所有符合条件的 alpha。
> 总共获取了
> 157
> 个
> alphas。
> 注意:  代码会去修改alpha 的名字。如果名字对你有其他用
> 途
> 请改成用颜色
> 开始处理 Regular Alphas 
> 成功将 Alpha
> eN2gonM 的名字修改为
> 'CVF'
> 成功将 Alpha 0Rb5827 的名字修改为 'CVF'
> 成功将 Alpha 6OPJNKp 的名字修改为 'CVF'
> 成功将 Alpha
> nmoxgQq 的名字修改为
> 'CVF'
> 成功将 Alpha Sp7delo 的名字修改为
> 'CVF'
> 成功将 Alpha
> 8V22202  的名字修改为
> 'CVF'
> 成功将 Alpha 3GQOSMN 的名字修改为
> 'CVF'
> 成功将 Alpha
> LE7Qmxe  的名字修改为 'CVF'
> 成功将 AZpha gdGLSxe 的名字修改为 'CVF
> 成功将 Alpha
> XVnMOn 的名字修改为
> 'CVF'
> 成功将
> Aloha
> mlOW8M9
> 的名宰修改为
> 'CVF



> [!NOTE] [图片 OCR 识别内容]
> 自动获取的计算月份:
> 2025-08
> 顾问开始日:
> 2025-04-14
> 我修改了本机电脑时间为8月19号
> 那么检测VF 的SA 选择时间为  5月1号
> 8月20号,
> 当然如
> 最终生效的V窗口开始日期:
> 2025-05-01
> 果开始时间早于顾问生效时间。那么开始时间则是 顾问生效时间。
> 正在获取第
> 0到  100
> alpha
> 正在获取第
> 100  到
> 200
> alpha
> 正在获取第
> 200  到  300
> 个 alpha_
> 己获取所有符合条件的 alpha。
> 总共获取了
> 180
> alphas
> 开始处理 Regular Alphas _
> 开始创建
> SUPER
> Alphas
> 区域 EUR 有
> 51
> 个CVF alpha, 符合创建SUPER alpha的条件。
> 区域 USA 有
> 68
> 个CVF alpha, 符合创建SUPER alpha的条件:
> 区域 BLB 有 33
> 个CVF alpha, 符合创建SUPER alpha的条件:
> 区域 ASI
> 有
> 20
> 个CVF alpha, 符合创建SUPER alpha的条件。
> 程序会生成super alpha, 请减少或暂停你正在生成 $A的程序
> 准备使用
> 2  个线程并行创建和重命名
> 个
> SUPER alpha
> 正在为区域 EUR 提交SUPER alpha回测
> 正在为区域 USA 提交SUPER alpha回测.
> 回测任务 BbUMKLeCZGNZCGEVOOCjNWNW
> 己提交,正在等待结果
> 回测任务
> SOOWe2UBGWTblhl2Ta2sZb
> 己提交。正在等待结果



> [!NOTE] [图片 OCR 识别内容]
> 岂^
> Simulate
> Alphas
> Learn
> Data
> 罟
> Labs
> Genius
> 思 Competitions (3)
> Community
> g
> Refer
> friend
> Worldquant BRNINis experiencing Some
> UNSUB
> Created 07/25/2025 EDT
> 20250726VFT_USA
> Add Alpha t0
> Lst
> Openalpha details in newtab
> Alphas
> Unsubmitted
> Submitted 
> Code
> 生成好了 alpha 的名字
> Selection Expression
> Page size 
> 100
> 0Ut0f
> 000+
> Ownggname
> "CVF"
> Combo Expression
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Searcn
> Select
> SupEr
> Select
> Searcn
> Select
> 20250726VFT。
> SuPEr
> UNSUBNITTED
> 07125/2025 EDT
> UIS4
> Simulation Settings
> Instrument Type
> Region
> Universe
> LangUage
> Decay
> Delay
> Truncatijon
> Neutralization
> Pasteuriatijon
> NaN Handling
> Unit Handling
> MaxTrade
> CoIpO
> 20250726VFT_E
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> ElR
> Equity
> 054
> TCP3000
> Fast Erpression
> 0.01
> Industy
> Verify
> anonymoUs
> SuPEr
> UNSUBNITTED
> 07125/2025 EDT
> ElR
> 20250726VFT_ASI
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> anonymaUs
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> Clone Alpha
> 20250726VFT_G.
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> GLB
> 20250819VFT_U.
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> UIS4
> Show test period
> Test period and overall stats are hidden by default when test period is specified.
> 20250819VFT_E
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> ElR
> anonymaUs
> SuPEr
> UNSUBNITTED
> 07/25/2025 EDT
> ElR


---

### 帖子 #5: alpha 模拟高效篇
- **主帖链接**: [L2] alpha 模拟高效篇.md
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

### 帖子 #6: Can I use Trade_when to decease the Turnover?
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

### 帖子 #7: Getting started with Risk DatasetsResearch
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

### 帖子 #8: Lab中处理Vector数据的一种方法代码优化
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

### 帖子 #9: replace 操作符的理解与运用
- **主帖链接**: [L2] replace 操作符的理解与运用.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #10: replace 操作符的理解与运用
- **主帖链接**: https://support.worldquantbrain.com[L2] replace 操作符的理解与运用_35191104743447.md
- **讨论数**: 0

在算术操作符中有一个"replace" 操作符，其作用是将变量中的一个值替换为另外一个值。具体如下：

replace(x, target="v1 v2 ..vn", dest="d1,d2,..dn")

其中target和dest的值的个数保持对应，中间用空格链接，当d1,d2...dn的值相同时可以简写为一个。具体用法可能有以下几种：

1.空值处理，如将nan替换为0或者将0替换为nan

2.合并分组，在industry分组中将一些行业代码合并，构建自己觉得有意义的分组

3.用特定值回填缺失值，如行业均值或者时间序列均值回填

---

### 帖子 #11: Research Paper: Firm Life Cycle, Expectation Errors and Future Stock ReturnsPinned
- **主帖链接**: https://support.worldquantbrain.com[L2] Research Paper Firm Life Cycle Expectation Errors and Future Stock ReturnsPinned_14111788609047.md
- **讨论数**: 0

**Abstract:**

I study the return predictability of firm life cycle, originally documented by Dickinson (2011). I show that a hedge portfolio strategy going long on mature firms and short on introduction firms generates a significant hedge portfolio return of 1.29% per month in return-weighted portfolios and 0.72% in value-weighted portfolios. The returns to firm life cycle are related to investors’ and analysts’ expectation errors, are driven by market-wide investor sentiment, and are more pronounced among stocks with low institutional ownership and high idiosyncratic volatility. Quantile regressions show that introduction firms have considerably greater uncertainty and skewness in future earnings growth outcomes than mature firms, such that analysts are better able to justify optimistically biased forecasts for introduction firms compared to mature firms.

Key ideas:

- Page 6 paragraph 2
- Page 18 paragraph 2

Useful datafields on BRAIN:

**Term**

**Datafield**

**Dataset**

sentiment

mdl17_score

[**Model17**]([链接已屏蔽])

institutional ownership

mdl10_inst_ownership

[**Model10**]([链接已屏蔽])

error

fnd90_game_eps_sur_vol

[**Fundamental90**]([链接已屏蔽])

Author: Theodosia Konstantinidi

Year : 2022

Link:  [[链接已屏蔽])

---

### 帖子 #12: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location']
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

### 帖子 #13: velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享
- **主帖链接**: [L2] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享.md
- **讨论数**: 25

在我第一次更新VF（velue factor）时，数值显示为0.04。当时，我心中充满了疑问：系统难道出错了吗？怎么会有这么低的VF值？于是，我急忙写邮件询问，是否是系统问题，但得到的回复却是：“没有问题。”这让我瞬间陷入了深深的失落，几乎觉得天塌了——怎么可能，连0.1都不到，之后还能做什么？

然而，这只是我VF学习之路的起点。为了寻找答案，我开始请教一些经验丰富的大佬，他们中有些VF值高达0.98甚至1.0。他们耐心地与我分享了他们的经验和见解，这些交流让我逐渐找到了自己的问题所在。原来，我不自觉地陷入了过拟合的泥潭，交出的结果都是“垃圾”。我明白了：问题出在自己的方法上。

**重新审视与总结**

经过这段时间的反思，我发现了自己在方法上的几个关键错误。在不知不觉中，我深陷于一阶、二阶、三阶死代码的漩涡，完全忽视了核心的“alpha”操作。我每天就是无脑地运行代码，反复跑着一堆没有意义的模型，完全没有思考“为什么”去做这些。VF值的低迷，也正是这些无用操作累积的结果。

意识到问题后，我开始调整思路。为了避免重复犯错，我决定通过更为系统的方式进行自我提升。我开始更加积极地参加论坛讨论、查阅书籍，并向研究小组里的资深成员请教，深入了解模型的核心思想与技术细节。每天都坚持积累，不再盲目操作，而是逐步理清了我自己的逻辑框架。

**突破与升华**

随着不断的实践与学习，我逐渐整理出了属于自己的交alpha逻辑和代码。我的模型开始逐步改进，VF值也在不断提高。最终，我成功突破了0.5以下的瓶颈，达到了0.93还成为了Expert。这段艰辛的成长历程，虽然充满挑战，但也让我收获了宝贵的经验和深刻的理解。

通过这次经历，我深刻认识到，技术和方法固然重要，但更重要的是要保持不断学习、持续反思的态度。没有什么是“一蹴而就”的，每一次的低谷，都是我们成长的铺垫。正是这份坚持与耐心，才让我从0.04走到了0.93，终于找到了属于自己的成功之路。

---

### 帖子 #14: velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享_32340009231127.md
- **讨论数**: 25

在我第一次更新VF（velue factor）时，数值显示为0.04。当时，我心中充满了疑问：系统难道出错了吗？怎么会有这么低的VF值？于是，我急忙写邮件询问，是否是系统问题，但得到的回复却是：“没有问题。”这让我瞬间陷入了深深的失落，几乎觉得天塌了——怎么可能，连0.1都不到，之后还能做什么？

然而，这只是我VF学习之路的起点。为了寻找答案，我开始请教一些经验丰富的大佬，他们中有些VF值高达0.98甚至1.0。他们耐心地与我分享了他们的经验和见解，这些交流让我逐渐找到了自己的问题所在。原来，我不自觉地陷入了过拟合的泥潭，交出的结果都是“垃圾”。我明白了：问题出在自己的方法上。

**重新审视与总结**

经过这段时间的反思，我发现了自己在方法上的几个关键错误。在不知不觉中，我深陷于一阶、二阶、三阶死代码的漩涡，完全忽视了核心的“alpha”操作。我每天就是无脑地运行代码，反复跑着一堆没有意义的模型，完全没有思考“为什么”去做这些。VF值的低迷，也正是这些无用操作累积的结果。

意识到问题后，我开始调整思路。为了避免重复犯错，我决定通过更为系统的方式进行自我提升。我开始更加积极地参加论坛讨论、查阅书籍，并向研究小组里的资深成员请教，深入了解模型的核心思想与技术细节。每天都坚持积累，不再盲目操作，而是逐步理清了我自己的逻辑框架。

**突破与升华**

随着不断的实践与学习，我逐渐整理出了属于自己的交alpha逻辑和代码。我的模型开始逐步改进，VF值也在不断提高。最终，我成功突破了0.5以下的瓶颈，达到了0.93还成为了Expert。这段艰辛的成长历程，虽然充满挑战，但也让我收获了宝贵的经验和深刻的理解。

通过这次经历，我深刻认识到，技术和方法固然重要，但更重要的是要保持不断学习、持续反思的态度。没有什么是“一蹴而就”的，每一次的低谷，都是我们成长的铺垫。正是这份坚持与耐心，才让我从0.04走到了0.93，终于找到了属于自己的成功之路。

---

### 帖子 #15: VF0.5->1.0->1.0->1.0->?,1.0体验卡结束后的总结与思考【指标分析篇】经验分享
- **主帖链接**: [L2] VF05-10-10-10-10体验卡结束后的总结与思考【指标分析篇】经验分享.md
- **讨论数**: 9

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

---

### 帖子 #16: VF0.5->1.0->1.0->1.0->?,1.0体验卡结束后的总结与思考【指标分析篇】经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] VF05-10-10-10-10体验卡结束后的总结与思考【指标分析篇】经验分享_35880708570391.md
- **讨论数**: 9

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

---

### 帖子 #17: [Alpha Machine] How do you optimize parameters within Alpha template?Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] [Alpha Machine] How do you optimize parameters within Alpha templateAlpha Template_27266129583255.md
- **讨论数**: 20

Hello everyone, 👋
In the earlier discussions, we shared the idea of the  [Alpha template](../顾问 AM60509 (Rank 61)/[Commented] 【Alpha Template Collections】- Continuously UpdatePinnedAlpha Template_24472586368279.md) . The Alpha template aims to encapsulate a specific economic intuition. For example, consider the template from an  [earlier post](../顾问 CC40930 (Rank 95)/[Commented] [Alpha Template] How can you use estimate and actual earnings data to create AlphasAlpha Template_25775603889431.md) :

> group_zscore(subtract(group_zscore(<act_data>, industry), group_zscore(<est_data>, industry)), industry)

This template calculates the difference in group-normalized actual data versus estimated data. You can explore pairs of actual and estimated data in datasets such as analyst7. This template can be further extended to:

> <group_compare_op_1>(<diff_op>(<group_compare_op_2>(<act_data>, <group_2>), <group_compare_op_3>(<est_data>, <group_3>)), <group_1>)

In this extended template, all the operators and group data turns into abstract choices. Each of these choices embodies the economic intuition behind the original selection. For instance, <group_compare_op_1> initially uses group_zscore, but other valid choices could include group_rank, which also compares the instrument to its relative peers in <group_1>.

Now, the question arises: how do you optimally choose for each available slot?  Below is an outline of a hill-climbing algorithm to identify favorable pairs:

1. Initialization: Start with an initial choice of parameters.
2. Evaluation: Simulate the expression and get the fitness.
3. Selection: Identify neighboring combinations by randomly choosing a different parameter from a randomly picked option.
4. Comparison: Re-simulate the updated expression and get the fitness.
5. Update: If a neighboring expression shows improved fitness, update the current choice to this new parameter set.
6. Iteration: Repeat the evaluation, selection, comparison, and update steps until no further improvements for 10 iterations.

By employing this algorithm, we can systematically improve the performance of the Alpha template.
However, there may be several obvious inductive biases in this framework. Have you noticed them? How can one further improve this framework? 🤔

Give this post a like 👍 and share your thoughts below! 💬

We will announce the correct answer after this post reaches 25 likes! 🚀

---

### 帖子 #18: [Alpha Template] Time-Series Sentiment Comparison TemplateAlpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] [Alpha Template] Time-Series Sentiment Comparison TemplateAlpha Template_24756474790551.md
- **讨论数**: 7

Hi Community,

Below is a template for sentiment related data:

> < [time_series_operator>]([链接已屏蔽]) (<positive_sentiment> - <negative_sentiment>, days)

Hypothesis: If a net sentiment of a company compared to earlier is positive, the stock price may increase.

Implementation:

- Simply choose time series operators on net sentiment value.
- Use reasonable day parameter, such as week(5 days), month(20 days), quarter(60 days) or year(250 days).
- [Sentiment Model]([链接已屏蔽])  and  [Neutralization]([链接已屏蔽]) to improve Alpha.

Besides this simple implementation, you may want to expand this into a more complicated format, for example:

> positive_sentiment = rank(<backfill_op>(<positive_sentiment, days));
> negative_sentiment = rank(<backfill_op>(<negative_sentiment, days));
> sentiment_difference = <compare_op>(positive_sentiment, negative_sentiment):
> <time_series_operator>(sentiment_difference, days)

Implementation:

- <backfill_op>: Since sentiment data usually has low coverage, it's better to backfill the data with ts_backfill or to_nan to achieve higher coverage.
- Rank: this template uses the rank operator on the backfill sentiment, this ensures the distribution of the data is under a familiar range. This step also remove some noise from the raw data.
- <compare_op>: Besides the original subtract operator, there may be other comparison operators that you can pick from.
- By altering data fields, operators and parameters within the template, you can efficiently generate a diverse range of submittable Alphas, especially via  [BRAIN API](/hc/en-us/articles/20786107171351) .

Go ahead and try out this template.
Please comment your findings on this template below!

---

### 帖子 #19: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
- **主帖链接**: [L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation.md
- **讨论数**: 73

一句话总结该活动：直接在评论区评论，分享你的模板。

> ```
> 被审核通过者将获得BRAIN纪念品一份（下图背包）优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至8.31日23：59（以服务器时间为准） [图片 (图片已丢失)]

活动要求：参赛同学可发布多个模板参赛， **必须展示下列所有元素** 。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。

- 模板
  - **模板中的变量必须使用< />进行声明，不符合语法规则的评论无法参评**
  - 需阐述具体变量赋值，如operator类别、数据集id、地区等
  - 阐述搜索空间的大小
  - 阐述模板的idea，implement细节（即哪步是数据处理，哪步是主信号）
  - 产出效果（回测：Alpha数量，可以仅展示比率）
  - 建议其他顾问未来尝试的探索方向

> **再次强调，必须至少展示上述所有信息👆先到先得！有些模板过于类似的将不再被批复，建议大家快快抓住机会！**

---

### 帖子 #20: 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha模板】基于labs分析macro做出可泛化的模板经验分享_34584423754263.md
- **讨论数**: 28

还记得weijie老师上课说过的一句话，一些sharp很高，turnover也很高的alpha是非常具有价值的，然后当时我就找到了下面这个alpha，并在labs上对其数据进行了分析。

本文讲的相对比较详细，建议新手务必认真读完，模板在本文的最下面，经过验证可以，在USA，GLB，EUR 三个大区都有不错的效果，至于你问我为什么没有ASI，因为我也没有这个数据集的权限。其他的数据集我相信也会有一定的效果，但是我还是十分建议你先在labs上对数据进行分析研究，而不是无脑的跑模板。

1.首先我们需要找到这样的alpha


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Created 05/01/2025 EDT
> anonymous
> Udd Mpha tO
> Lst
> Alphas
> Unsubmitted
> Openalpha details in newtab
> Aggregate Data
> 5harDE
> TUrnover
> Fitness
> Re-Urns
> Drawidowin
> Warsin
> Size
> OUL OT
> 1.92
> 34.089
> 0.70
> 4.539
> 2.429
> 2.669600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Select Columns
> Name
> Competition
> Type
> Date Created
> 2013
> 36,75{
> 0,50
> 3.9435
> 1.1795
> 2.143oc
> 500
> 496
> Search
> Selec
> Regular
> 05/01/2025
> 2014
> 2.43
> 35,153
> 0,95
> 5.1395
> 0335
> 923occ
> 553
> 553
> anonymous
> Regular
> 05/01/2025
> 2015
> 34,951
> 0.56
> 983
> 263
> 2.233oc
> 525
> 530
> 2016
> 0.23
> 35,38{
> 0,03
> 0.5335
> 9235
> 303occ
> 570
> 53'
> 2017
> 3.19
> 33.953
> 5.9095
> 0.9535
> 433o0c
> 708
> 725
> 2018
> 0.42
> 33,381
> 0,07
> .88驮
> 2.-23
> 0.533o
> 794
> 780
> 2019
> 3.11
> 33.035
> 1,40
> 5.733
> 1.193
> 1.073occ
> 829
> 78'
> 2020
> 2.99
> 31,153
> 1,51
> 8.2635
> 5095
> 5.303oc
> 331
> 301
> 2021
> 101
> 35,303
> 2.15
> 10.319
> 0.1795
> 5.7G3occ
> 876
> 875
> 2021
> 1.21
> 33.595
> 0,38
> 3.38%
> 1.173
> 2.013occ
> 1125
> 1070
> 2022
> 2.52
> 33.335
> 1.23
> 7.363
> 0.923
> 1.413oc
> 1230
> 1176
> 2023
> 31,323
> -2.45
> 10.6195
> 6245
> 733occ
> 1223
> 1220
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RezUrns
> Drawdown
> Marsin
> 2.24
> 34.089
> 0.82
> 4.609
> 2.029
> 2.709600
> Page


2. 然后将其用到的字段名复制下来，在Data上搜索


> [!NOTE] [图片 OCR 识别内容]
> 40QL
> 鬯
> Simulate
> C Alphas
> Learn
> Data
> 器
> Labs
> Genius
> 智
> Competitions (4)
> Community
> y Refer a friend
> Region
> Delay
> Universe
> USA
> T0P3000
> What data do you want to find?
> mcr27_
> company_jobsactivel
> Search
> Fields
> The number of active job postings by the company。
> mcrz7_company_jobsactive in Job records from job posting
> Show all matching fields
> Datasets
> mid theme multipliers
> No datasets found by quick search
> Analyst
> Showallmatching datasets
> TCe
> Value score: 4
> Value score: 6
> Value score: 5
> Value score:
> Datasets: 38
> Datasets: 9
> Datasets: 36
> Datasets:
> Fields: 11618
> Fields: 251
> Fields: 20081
> Fields: 3
> Regions: AMR, ASI, CHN,EUR, GLB,
> Regions: AMR, ASI,CHN EUR, GLB
> Regions: AMR, ASL, CHN, EUR, GLB,
> Regions: USA
> JPN,USA
> JPN,USA
> JPN,USA


3. 点击搜索后得到下面的结果


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Search result
> USA
> TOP3000
> Fields
> Datasets
> Search
> Theme
> Coverage
> Type
> Alphas
> Users
> mcrz7_company_jol
> 100
> Clear
> Dataset
> Field
> Description
> Vpe
> Pyramid
> Coverage
> Users
> Alphas
> Theme
> Multiplier
> Iobrecords trom job posting
> mcrz7_bucket_monthly_jobsa
> The number of active jobs postings bythe
> Vector
> 51 %
> ctive
> Company。
> mcrz7_bucket_daily_jobsactiv
> The number of active job postings by the
> Vector
> 50%
> 192
> 540
> Company
> mcrz7_daily_sdioc
> The number of company IDs with active jobs
> Vector
> 50%
> in the Same macro bUCket。
> mCrz7_monthly_sdioc
> The number of company IDs with active jobs
> Vector
> i the Same IaCro DUICKet
> mCr27_bUcket_daily_jobsactiv
> The number of active jobs postings bythe
> Vector
> 4996
> company,after neutralizationinthe
> respective macro bucket
> mCr27_bUcket_monthly_jobsa
> The number of active jobs postings bythe
> Vector
> 4996
> ctive_n
> company,after neutralizationinthe
> respective macro bucket
> mCrz7_daily_jr_sdioc
> The number of company IDs inthe same
> Vector
> 45%6
> macro bucket that have removed jobs since
> the last scraping:
> mCrz7_daily_jc_sdioc
> The number of company IDs inthe same
> Vector
> 4596
> macro bucket that have created jobs since the
> last scraping:
> mcrz7_bucket_daily_jobsremo
> The number ofjob postings removed by the
> Vector
> 459
> Ved
> company
> ICrz7 DUCez monthl ObSI
> The number ofiob postines remoyed by the
> Vector


一般第一个就是你要的那个字段，之后点进去再找到下面的Visualiaze Field


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> Universe
> Data
> Datasets
> Job records from job posting
> mcrz7_bucket_monthly_jobsactive
> USA
> TOP3000
> Simulate Field
> Visualize Field
> Field description
> Category: Macro
> Macroeconomic Activities
> Type: Vector
> The number of active jobs postings by the company.
> Region
> Delay
> Universe
> Pyramid Theme
> Theme
> Coverage
> Users
> Alphas
> Multiplier
> USA
> T0P3000
> 519
> Show all settings
> Data field visualizationincludes:
> Whatis the range ofvalues and theirfrequency?
> How Uothe Values Vany Dy SECtor?
> How does the distribution Vary overtime?
> How often do Values update?
> What % Ofvalues are NaNOrZero?
> And more。
> 黟^
> Visualize Field


4.开始分析数据

这里我们发现这个数据字段是大量的0值的，这种情况我们的ts_backfill是没有办法进行填充的，所以我们在这之前需要先 to_nan 一下  ，例 : ts_backfill(to_nan({data_filed}),60)


> [!NOTE] [图片 OCR 识别内容]
> What is the range of mcr27_
> bucket_monthly_jobsactive Values
> their frequency?
> L2N
> IM
> Linear Axes
> 08N
> Log X-Axis
> 
> 0.GN
> Y-Axis
> 0AM
> Log-Log Axes
> 0.2N
> SOK
> I0OK
> 15Ok
> 20Or
> 25OK
> TIP
> and
> Log


简单的处理之后turnover会有明显的下降，两个alpha之间唯一的区别就是有没有加to_nan，下面的图因为我改了一下decay，所以和刚找的alpha有一点点不太一样（是的，难以想象只是改了一下decay，turnover居然高了这么多）


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Date Created (EST)
> Region
> Delay
> Neutralization
> Sharpe
> Returns
> Turnover
> Margin
> Fitness
> Color
> Search
> Seec
> Regular
> 08/30/2025
> 08/31/
> USA
> Selec
> e.g>
> e.g>
> Pg
> e.g>
> e.g>
> Purple
> anOIYMOUS
> RegUlaT
> 08/31/2025 EDT 
> USA
> Subindustry
> +94
> 4.5596
> 34.09%6
> 2.67960c
> 0.71
> Purple
> anOIYMOUS
> RegUlaT
> 08/31/2025 EDT 
> USA
> Subindustry
> 1.61
> 4.73%6
> 75.78%
> 1.25960c
> 0.40
> Purple


一个简简单单的0值处理成nan，就把turnover降了一半，同时sharp和return都有一定的提升

5.发现异常值，对异常值进行处理


> [!NOTE] [图片 OCR 识别内容]
> (3.685.465,1.307732N)
> L2N
> IN
> Linear Axes
> 08N
> X-AxIs
> 
> 0.GN
> YAxis
> 04l
> Log-Log Axes
> 02N1
> In
> TV
> 0.001
> 1000
> IN
> Value
> Log
> Log



> [!NOTE] [图片 OCR 识别内容]
> What are the key statistical characteristics (min, max; mean, median, and quantiles) of the mcr27
> BOK
> M
> Mean
> Da
> median
> GOK
> 25th_quantile
> 75th_quantile
> `
> 4OK
> ZOK
> 9
> 2014
> 2015
> 2018
> 2020
> 2022
> Date


在这里我尝试了ts_quantile和winsorize，发现ts_quantile的效果要更好

至此，数据处理的环节就完成了

例：ts_quantile(ts_backfill(to_nan({datafield}),60), 5, driver=gaussian)

6.将处理好的数据放入一二三阶框架中直接运行，就能得到不错的效果，我尝试了一二（先时序处理再横截面处理）和二一（先横截面处理再时序处理），目前来看一二的效果比较好（时序处理：ts；横截面处理：group）

7.最后展示一下结果（USA)


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 12/30/2022
> Test Pnl: 4,952.33k
> DOOK
> 3.0OOk
> Z.0OOK
> DOOK



> [!NOTE] [图片 OCR 识别内容]
> Single Data Set Alpha
> Power Pool Alpha
> Pyramidtheme: USADIIMACRO X1.1
> Aggre
> Data
> SharDE
> Turnover
> Fitness
> Rezurns
> Drawdowin
> Marsin
> 2.00
> 12.209
> 1.27
> 5.01%
> 2.229
> 8.229600
> Sharpe
> Turnover
> Fitness
> Returs
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 1.30
> 12.493
> 0.53
> 2.479
> 539
> 3,959230
> 1493
> 1598
> 2014
> 2.17
> 11.925
> 1.27
> 4,309
> 269
> 7.229230
> 1472
> 1526
> 2015
> 212
> 12.153
> 1.31
> 4.7936
> 163
> 885230
> 1453
> 1576
> 2016
> 0,33
> 11.525
> 0.08
> 0.719
> 1,213
> 229330
> 444
> 1586
> 2017
> 2.23
> 11.991
> 1.37
> 4.719
> 629
> 869330
> 505
> 1597
> 2018
> 1,61
> 12.50
> 0.85
> 3,48%
> 28%
> 585330
> 553
> 1553
> 2019
> 3.35
> 12.13{
> 2.-3
> ,503
> 974
> 10,3753
> 430
> 1529
> 2020
> 3,67
> 12.435
> 3.69
> 12.519
> 1.799
> 20.299330
> 1573
> 1525
> 2021
> -1,50
> 13.531
> 0.96
> -5.549
> 0.56%
> 68po
> 534
> 1468
> 2021
> 1.51
> 12.73{
> 0.97
> 5.243
> 2.20%
> 8.2-So30
> 1705
> 2022
> 2.00
> 11.9535
> 1.33
> 5.923
> 1.103
> 895330
> 1431
> 1675
> 2023
> 3,88
> 13.251
> 3.34
> ,849
> 14,839330
> 404
> 1772
> egate
> Year
> 147


不算特别好，但只是简单处理了一下数据，就能得到一个还不是“死鱼”的Alpha，还算不错  （注：死鱼是weijie老师的一个梗，暗指turnover小于5的Alpha）

最后的最后，大家还能结合一下MCP找到一些有意思的处理方式，下面抛砖引玉

### 1. 时间序列特征明显

- 数据有明显的趋势变化（2018年末转折点）

- 存在周期性波动和异常尖峰

- 推荐operators：

- ts_delta - 捕捉趋势变化

- ts_rank - 处理时间序列排序

- ts_zscore - 标准化处理异常值

- ts_returns - 计算收益率变化

### 2. 异常值处理需求

- 数据中存在显著的异常尖峰

- 分布从集中变为高度偏斜

- 推荐operators：

- ts_quantile - 分位数处理，减少异常值影响

- ts_skewness - 检测偏度变化

- ts_std_dev - 标准差，识别异常波动

- ts_entropy - 信息熵，检测分布变化

### 3. 分布特征变化

- 从稳定分布变为高度偏斜

- 不同时期数据特征差异巨大

- 推荐operators：

- rank - 排序，处理分布偏斜

- zscore - 标准化

- quantile - 分位数变换

- normalize - 归一化处理

### 4. 多实体比较

- 不同实体表现差异显著

- 推荐operators：

- group_rank - 分组排序

- group_mean - 分组均值

- group_std_dev - 分组标准差

### 组合1：异常值稳健处理

ts_quantile(ts_zscore(mcr27, 22), 22, driver='gaussian')

### 组合2：趋势捕捉

ts_delta(ts_rank(mcr27, 66), 5)

### 组合3：分布标准化

rank(ts_std_dev(mcr27, 120))

### 组合4：分组比较

group_rank(ts_mean(mcr27, 22), densify(sector))

如果你觉得写得还不错，麻烦给个宝贵的赞，这将是对我最大的鼓励！！

---

### 帖子 #21: 【SuperAlpha灵感】因子择时模型Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【SuperAlpha灵感】因子择时模型Alpha Template_32553007626007.md
- **讨论数**: 30

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

---

### 帖子 #22: 【ValueFactor预测器】滚动3个月SA，掌握你最近3个月提交alpha情况_python版代码优化
- **主帖链接**: [L2] 【ValueFactor预测器】滚动3个月SA掌握你最近3个月提交alpha情况_python版代码优化.md
- **讨论数**: 9

首先感谢weijie老师提出的idea:

选择你最近3个月提交的alpha 组SA，根据SA的表现衡量你过去3个月提交的alpha的质量，sa的表现可以视作value factor的预告。之后，你提交的alpah，需要和过去3个月组合的sa的相关性低。

那么如何滚动3个月的alpha组合sa呢？

根据alpha提交的时间，添加年份-月份的tags，然后在组sa的时候，选择tags是指定月份的alpha，进行回测，根据sa的表现，衡量你最近3个月提交的sa质量，代码如下：

```
import jsonimport sysimport timefrom datetime import datetimefrom time import sleepimport requestsfrom requests.adapters import HTTPAdapterfrom requests.packages.urllib3.util.retry import Retrydef load_config(file_path):    """从指定路径f加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user=config["user"]passwd=config["password"]def login():    username = user    password =  passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    max_try = 3    retry=0    while True:        try:            response = s.post('[链接已屏蔽])            if response.status_code  in [200,201]:                print(f"login success")                return s        except Exception as e:            print(f"login err :{e}")            print(f"login failed ,sleep 5 ,try again")            sleep(5)        retry +=1        if retry > max_try:            break    return Nonedef get_submited_alphas_three_month(s,start_date,end_date,region,only_ppa=True):    # only_ppa 设置是否只获取ppa的alpha设置tags，后续组sa时根据tags值的年份月份筛选    print(f"正在获取{start_date}到{end_date}内，{region}地区的ppa alpha")    url=f"[链接已屏蔽]    count=0    print(url)    count=s.get(url).json()['count']    print(count)    alpha_list=[]    for i in range(0,count,100):        url=f"[链接已屏蔽]        response=s.get(url).json()        for alpha in response['results']:            if only_ppa:                flag=0                for item in alpha["classifications"]:                    if item['name']=='Power Pool Alpha':                        flag=1                        break                if flag==1:                    alpha_list.append(alpha)            else:                alpha_list.append(alpha)    print(f"在时间范围{start_date}到{end_date}内，{region}地区，获取了 {len(alpha_list)}个ppa alpha")    return alpha_list# 对所有alpha 在原有tags列表上增加年份+月份的tags，如2025-05def set_alpha_property_list(s,alpha_list):    count = 0    for alpha in alpha_list:        alpha_id=alpha['id']        print(f"正在设置第{count}个alpha 的属性,{alpha_id}; 总alpha数量{len(alpha_list)}")        tags=alpha['tags']        name=alpha['name']        date_created=alpha['dateCreated']        color=alpha['color']        description=alpha['regular']['description']        dt = datetime.fromisoformat(date_created.replace('Z', '+00:00'))        year_month = dt.strftime('%Y-%m')  # "2025-07"        print(year_month)        if year_month in tags:            continue        else:            tags.append(year_month)        category=alpha['category']        if category is None:            category=None        if color is None:            color=None        if name is None:            name=None        print(tags)        params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": description},        "combo": {"description": description},        "selection": {"description": description}}        response = s.patch( "[链接已屏蔽] + alpha_id, json=params)        # print(response.json())        sleep(1)        count+=1    return Truedef make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade):    simulation_data={    "type": "SUPER",    "settings": {        "maxTrade": maxtrade,        "nanHandling": "ON",        "instrumentType": "EQUITY",        "delay": delay,        "universe": universe,        "truncation": 0.08,        "unitHandling": "VERIFY",        "selectionLimit": select_num,        "selectionHandling": select_handle,        "testPeriod": "P0D",        "componentActivation": "IS",        "pasteurization": "ON",        "region": region,        "language": "FASTEXPR",        "decay": decay,        "neutralization": neut_,        "visualization": False    },    "combo": str(combo),    "selection": select}    return simulation_datadef simulate_sa(s,simulation_data):    brain_api_url = '[链接已屏蔽]    try:        simulation_response=s.post(f'{brain_api_url}/simulations',json=simulation_data)        # print(simulation_response.json())    except Exception as e:        print(f"模拟sa失败:{e}")        return None    simulation_progress_url = simulation_response.headers['Location']    print(simulation_progress_url)    while True:        simulation_progress_response=s.get(simulation_progress_url)        retry_after = simulation_progress_response.headers.get("Retry-After", 0)        if str(retry_after) == '0':            status = simulation_progress_response.json().get("status", "not_found")            if status == "COMPLETE":                res_=simulation_progress_response.json()                alpha_id=res_["alpha"]                print(f"最近3个月的ppa组成的sa模拟完成,alpha_id:{alpha_id}")                break        else:            print(f"processing,begin sleep {float(retry_after)}")            time.sleep(float(retry_after))    return alpha_id# 对指定日期范围内的ppa 设置年月标签来确认是否是指定时间范围的ppas = login()#设置你想滚动组合sa的月份start_date='2025-04-01'end_date='2025-06-30'data_range=['2025-04','2025-05','2025-06']# 地区，universeregion='USA'universe='TOP3000'delay=1decay=0select_handle='POSITIVE'select_num=300maxtrade='ON'alpha_list=get_submited_alphas_three_month(s,start_date,end_date,region)print(f"在时间范围{start_date}到{end_date}内，提交了 {len(alpha_list)}个ppa alpha")print(alpha_list[0]['id'],)set_alpha_property_list(s,alpha_list)select=f'(own) && ((in(tags,"{data_range[0]}")) || (in(tags,"{data_range[1]}"))|| (in(tags,"{data_range[2]}")))'print(select)combo=1alpha_ids=[]for decay in  [0]:    ##可根据需要对多种neut回测查看sa表现    for neut_ in  ["CROWDING","REVERSION_AND_MOMENTUM"]:        simulation_data=make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade)        alpha_id=simulate_sa(s,simulation_data)        alpha_ids.append(alpha_id)print(f"完成回测,alpha_id如下")print(alpha_ids)print(f"最近3个月， {region} 提交的ppa 组合的sa表现如下")for alpha_id in alpha_ids:    res=s.get(f"[链接已屏蔽])    res_json=res.json()    sharpe=res_json['is']['sharpe']    fitness=res_json['is']['fitness']    return_=res_json['is']['returns']    drawdown=res_json['is']['drawdown']    margin=res_json['is']['margin']    turnover=res_json['is']['turnover']    neut=res_json['settings']['neutralization']    decay=res_json['settings']['decay']    print(f"{alpha_id}: sharpe: {sharpe}, fitness: {fitness}, return: {return_}, drawdown: {drawdown}, margin: {margin}, turnover: {turnover}, neut: {neut},decay: {decay}")
```

输出结果如下：

```
完成回测,alpha_id如下['12Q7xez', 'E2XGKG0']最近3个月提交的ppa USA 组合的sa表现如下12Q7xez: sharpe: 3.71, fitness: 5.36, return: 0.2609, drawdown: 0.0647, margin: 0.00873, turnover: 0.0598, neut: CROWDING,decay: 0E2XGKG0: sharpe: 4.11, fitness: 5.85, return: 0.2533, drawdown: 0.0429, margin: 0.006105, turnover: 0.083, neut: REVERSION_AND_MOMENTUM,decay: 0
```

---

### 帖子 #23: 【ValueFactor预测器】滚动3个月SA，掌握你最近3个月提交alpha情况_python版代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 【ValueFactor预测器】滚动3个月SA掌握你最近3个月提交alpha情况_python版代码优化_33715194478615.md
- **讨论数**: 9

首先感谢weijie老师提出的idea:

选择你最近3个月提交的alpha 组SA，根据SA的表现衡量你过去3个月提交的alpha的质量，sa的表现可以视作value factor的预告。之后，你提交的alpah，需要和过去3个月组合的sa的相关性低。

那么如何滚动3个月的alpha组合sa呢？

根据alpha提交的时间，添加年份-月份的tags，然后在组sa的时候，选择tags是指定月份的alpha，进行回测，根据sa的表现，衡量你最近3个月提交的sa质量，代码如下：

```
import jsonimport sysimport timefrom datetime import datetimefrom time import sleepimport requestsfrom requests.adapters import HTTPAdapterfrom requests.packages.urllib3.util.retry import Retrydef load_config(file_path):    """从指定路径f加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user=config["user"]passwd=config["password"]def login():    username = user    password =  passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    max_try = 3    retry=0    while True:        try:            response = s.post('[链接已屏蔽])            if response.status_code  in [200,201]:                print(f"login success")                return s        except Exception as e:            print(f"login err :{e}")            print(f"login failed ,sleep 5 ,try again")            sleep(5)        retry +=1        if retry > max_try:            break    return Nonedef get_submited_alphas_three_month(s,start_date,end_date,region,only_ppa=True):    # only_ppa 设置是否只获取ppa的alpha设置tags，后续组sa时根据tags值的年份月份筛选    print(f"正在获取{start_date}到{end_date}内，{region}地区的ppa alpha")    url=f"[链接已屏蔽]    count=0    print(url)    count=s.get(url).json()['count']    print(count)    alpha_list=[]    for i in range(0,count,100):        url=f"[链接已屏蔽]        response=s.get(url).json()        for alpha in response['results']:            if only_ppa:                flag=0                for item in alpha["classifications"]:                    if item['name']=='Power Pool Alpha':                        flag=1                        break                if flag==1:                    alpha_list.append(alpha)            else:                alpha_list.append(alpha)    print(f"在时间范围{start_date}到{end_date}内，{region}地区，获取了 {len(alpha_list)}个ppa alpha")    return alpha_list# 对所有alpha 在原有tags列表上增加年份+月份的tags，如2025-05def set_alpha_property_list(s,alpha_list):    count = 0    for alpha in alpha_list:        alpha_id=alpha['id']        print(f"正在设置第{count}个alpha 的属性,{alpha_id}; 总alpha数量{len(alpha_list)}")        tags=alpha['tags']        name=alpha['name']        date_created=alpha['dateCreated']        color=alpha['color']        description=alpha['regular']['description']        dt = datetime.fromisoformat(date_created.replace('Z', '+00:00'))        year_month = dt.strftime('%Y-%m')  # "2025-07"        print(year_month)        if year_month in tags:            continue        else:            tags.append(year_month)        category=alpha['category']        if category is None:            category=None        if color is None:            color=None        if name is None:            name=None        print(tags)        params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": description},        "combo": {"description": description},        "selection": {"description": description}}        response = s.patch( "[链接已屏蔽] + alpha_id, json=params)        # print(response.json())        sleep(1)        count+=1    return Truedef make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade):    simulation_data={    "type": "SUPER",    "settings": {        "maxTrade": maxtrade,        "nanHandling": "ON",        "instrumentType": "EQUITY",        "delay": delay,        "universe": universe,        "truncation": 0.08,        "unitHandling": "VERIFY",        "selectionLimit": select_num,        "selectionHandling": select_handle,        "testPeriod": "P0D",        "componentActivation": "IS",        "pasteurization": "ON",        "region": region,        "language": "FASTEXPR",        "decay": decay,        "neutralization": neut_,        "visualization": False    },    "combo": str(combo),    "selection": select}    return simulation_datadef simulate_sa(s,simulation_data):    brain_api_url = '[链接已屏蔽]    try:        simulation_response=s.post(f'{brain_api_url}/simulations',json=simulation_data)        # print(simulation_response.json())    except Exception as e:        print(f"模拟sa失败:{e}")        return None    simulation_progress_url = simulation_response.headers['Location']    print(simulation_progress_url)    while True:        simulation_progress_response=s.get(simulation_progress_url)        retry_after = simulation_progress_response.headers.get("Retry-After", 0)        if str(retry_after) == '0':            status = simulation_progress_response.json().get("status", "not_found")            if status == "COMPLETE":                res_=simulation_progress_response.json()                alpha_id=res_["alpha"]                print(f"最近3个月的ppa组成的sa模拟完成,alpha_id:{alpha_id}")                break        else:            print(f"processing,begin sleep {float(retry_after)}")            time.sleep(float(retry_after))    return alpha_id# 对指定日期范围内的ppa 设置年月标签来确认是否是指定时间范围的ppas = login()#设置你想滚动组合sa的月份start_date='2025-04-01'end_date='2025-06-30'data_range=['2025-04','2025-05','2025-06']# 地区，universeregion='USA'universe='TOP3000'delay=1decay=0select_handle='POSITIVE'select_num=300maxtrade='ON'alpha_list=get_submited_alphas_three_month(s,start_date,end_date,region)print(f"在时间范围{start_date}到{end_date}内，提交了 {len(alpha_list)}个ppa alpha")print(alpha_list[0]['id'],)set_alpha_property_list(s,alpha_list)select=f'(own) && ((in(tags,"{data_range[0]}")) || (in(tags,"{data_range[1]}"))|| (in(tags,"{data_range[2]}")))'print(select)combo=1alpha_ids=[]for decay in  [0]:    ##可根据需要对多种neut回测查看sa表现    for neut_ in  ["CROWDING","REVERSION_AND_MOMENTUM"]:        simulation_data=make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade)        alpha_id=simulate_sa(s,simulation_data)        alpha_ids.append(alpha_id)print(f"完成回测,alpha_id如下")print(alpha_ids)print(f"最近3个月， {region} 提交的ppa 组合的sa表现如下")for alpha_id in alpha_ids:    res=s.get(f"[链接已屏蔽])    res_json=res.json()    sharpe=res_json['is']['sharpe']    fitness=res_json['is']['fitness']    return_=res_json['is']['returns']    drawdown=res_json['is']['drawdown']    margin=res_json['is']['margin']    turnover=res_json['is']['turnover']    neut=res_json['settings']['neutralization']    decay=res_json['settings']['decay']    print(f"{alpha_id}: sharpe: {sharpe}, fitness: {fitness}, return: {return_}, drawdown: {drawdown}, margin: {margin}, turnover: {turnover}, neut: {neut},decay: {decay}")
```

输出结果如下：

```
完成回测,alpha_id如下['12Q7xez', 'E2XGKG0']最近3个月提交的ppa USA 组合的sa表现如下12Q7xez: sharpe: 3.71, fitness: 5.36, return: 0.2609, drawdown: 0.0647, margin: 0.00873, turnover: 0.0598, neut: CROWDING,decay: 0E2XGKG0: sharpe: 4.11, fitness: 5.85, return: 0.2533, drawdown: 0.0429, margin: 0.006105, turnover: 0.083, neut: REVERSION_AND_MOMENTUM,decay: 0
```

---

### 帖子 #24: 【VF 0.9+顾问分享】新人常见误区之Under Fitting （欠拟合）经验分享
- **主帖链接**: [L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享.md
- **讨论数**: 17

春节期间有些懈怠了，回来收收心继续搬砖，并且给新人分享一些常见容易忽视的地方

一、【Fitting】

在很多培训中老师都有讲过 不要过拟合，Over fitting。在本文中就不在赘述了，总之一句话 when you feels not right, it is not right! 但往往新手顾问找到可以提交的alpha 以后就直接提交了，这也错失了很多提高alpha 表现从而提高value factor的机会

**总结我常见的fitting方式包括：**

**1. 改变天数 Days、Std 等Operator里面的天数**

这部分没有太多的技术含量，通过有意义的天数进行替代，最简单的办法是都试一遍 5、22、60、120、240等。当然有经验的同学可以根据数据特性来进行有针对性的调优，比如季度更新频率的数据在ts backfill 5显然是没有意义的。

**2. 更改Universe, 中性化，decay等setting里的参数**

这里也可以暴力替换，自己维护一个不同region的universe、中性化的表即可。在实操中注意第一步里替换了天数等可以选择2-5个作为表达式进行回测，一方面multi simulation要大于1个alpha才可以。

**3.针对特定情况（比如高换手率）的fitting**

一个很好用但容易被忽视的工具 PnL Visualization, 默认大家可以看到的是PnL的曲线，点击右上角的下拉菜单还可以看到不同时间的换手率，sharpe等数值。

[图片 (图片已丢失)]

尤其有用的是turnover，但你看到在某一个时间这个alpha出现了剧烈的turnover的升高，很有可能是那段时间的数据有误，可以通过以下方式进行规避。（但group count是genius operator 部分人可能没有）

trade_when(group_count(alpha,market)>个数，alpha，0)

另外在手工回测的时候也可以勾选visulization选项（simulate按钮旁）这样也可以在pnl图上获取更多的信息（行业分布、市值分布、国家分布等）

此外降低turnover的常见方法包括  ts_decay_linear 等函数，尤其是平台最新推出的含有关键词tvr的operator，虽然可能会降低Sharpe，但降低tvr后可以提高fitness和margin  找到一个合理的平衡点即可。

需要注意的是这些operator需要配合scale使用，即 Operator（Scale(Alpha), Scale(Volume 如adv20）， 其他参数）

**二、【Fitting与Robust Testing】**

Value Factor本质是看OS的表现，那如果你的alpha可以在不同的universe 不同的中性化条件下都有不错的表现，也侧面证明了这个alpha本身是有很好的意义的，那也可以放心提交。

通过以上的步骤二，可以观察这个alpha在不同setting下的表现，从而进行判断是否提交该alpha

**以下是一些代码供参考**

**#获取alpha的表达式, 用来参考基线，并获取表达式**

```
target_id = 'alpha id'alpha_result = get_simulation_result_json(s,target_id)print('EXPRESSION:',alpha_result['regular']['code'])decay = alpha_result['settings']['decay']neut = alpha_result['settings']['neutralization']uni = alpha_result['settings']['universe']print('SHARPE:',alpha_result['is']['sharpe'])print('FITNESS:',alpha_result['is']['fitness'])print('MARGIN',alpha_result['is']['margin'])
```

#自行维护的对应关系表

```
region = 'ASI'neutralization = ['MARKET','SECTOR','INDUSTRY','SUBINDUSTRY']if region == 'ASI':neutralization.extend(['COUNTRY','CROWDING','FAST','SLOW','SLOW_AND_FAST'])universe= ['MINVOL1M','ILLIQUID_MINVOL1M']elif region == 'JPN':universe= ['TOP1600','TOP1200']print(neutralization)print(universe)
```

**第一步：更换天数等input**

```
days = ['5','22','60','120','240']winsorizes = ['1','2','3','4']
```

```
template = '''Alpha Expression'''expressions = []for day1 in days:forwinsorizeinwinsorizes:forday2indays:expression=template.replace('A', day1).replace('B', winsorize).replace('C',day2)expressions.append(expression)
```

**发送回测（请根据自己的代码做适配调整）**

```
#first round find daysfine_alpha_list=[]for expression in expressions:fine_alpha_list.append((expression, decay))fine_pools = load_task_pool(fine_alpha_list,10,10)print(datetime.now())multi_simulate2(fine_pools, neut, region, uni, 0, 1)print(datetime.now())
```

---

### 帖子 #25: 【VF 0.9+顾问分享】新人常见误区之Under Fitting （欠拟合）经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md
- **讨论数**: 17

春节期间有些懈怠了，回来收收心继续搬砖，并且给新人分享一些常见容易忽视的地方

一、【Fitting】

在很多培训中老师都有讲过 不要过拟合，Over fitting。在本文中就不在赘述了，总之一句话 when you feels not right, it is not right! 但往往新手顾问找到可以提交的alpha 以后就直接提交了，这也错失了很多提高alpha 表现从而提高value factor的机会

**总结我常见的fitting方式包括：**

**1. 改变天数 Days、Std 等Operator里面的天数**

这部分没有太多的技术含量，通过有意义的天数进行替代，最简单的办法是都试一遍 5、22、60、120、240等。当然有经验的同学可以根据数据特性来进行有针对性的调优，比如季度更新频率的数据在ts backfill 5显然是没有意义的。

**2. 更改Universe, 中性化，decay等setting里的参数**

这里也可以暴力替换，自己维护一个不同region的universe、中性化的表即可。在实操中注意第一步里替换了天数等可以选择2-5个作为表达式进行回测，一方面multi simulation要大于1个alpha才可以。

**3.针对特定情况（比如高换手率）的fitting**

一个很好用但容易被忽视的工具 PnL Visualization, 默认大家可以看到的是PnL的曲线，点击右上角的下拉菜单还可以看到不同时间的换手率，sharpe等数值。


> [!NOTE] [图片 OCR 识别内容]
> 区 Open alpha details in new tab
> Chart
> Pnl
> Performance
> Pnl
> 6,00OK
> Turnover
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> OW
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
> Check Submission
> Submit Alpha
> Sharpe
> NNN


尤其有用的是turnover，但你看到在某一个时间这个alpha出现了剧烈的turnover的升高，很有可能是那段时间的数据有误，可以通过以下方式进行规避。（但group count是genius operator 部分人可能没有）

trade_when(group_count(alpha,market)>个数，alpha，0)

另外在手工回测的时候也可以勾选visulization选项（simulate按钮旁）这样也可以在pnl图上获取更多的信息（行业分布、市值分布、国家分布等）

此外降低turnover的常见方法包括  ts_decay_linear 等函数，尤其是平台最新推出的含有关键词tvr的operator，虽然可能会降低Sharpe，但降低tvr后可以提高fitness和margin  找到一个合理的平衡点即可。

需要注意的是这些operator需要配合scale使用，即 Operator（Scale(Alpha), Scale(Volume 如adv20）， 其他参数）

**二、【Fitting与Robust Testing】**

Value Factor本质是看OS的表现，那如果你的alpha可以在不同的universe 不同的中性化条件下都有不错的表现，也侧面证明了这个alpha本身是有很好的意义的，那也可以放心提交。

通过以上的步骤二，可以观察这个alpha在不同setting下的表现，从而进行判断是否提交该alpha

**以下是一些代码供参考**

**#获取alpha的表达式, 用来参考基线，并获取表达式**

```
target_id = 'alpha id'alpha_result = get_simulation_result_json(s,target_id)print('EXPRESSION:',alpha_result['regular']['code'])decay = alpha_result['settings']['decay']neut = alpha_result['settings']['neutralization']uni = alpha_result['settings']['universe']print('SHARPE:',alpha_result['is']['sharpe'])print('FITNESS:',alpha_result['is']['fitness'])print('MARGIN',alpha_result['is']['margin'])
```

#自行维护的对应关系表

```
region = 'ASI'neutralization = ['MARKET','SECTOR','INDUSTRY','SUBINDUSTRY']if region == 'ASI':neutralization.extend(['COUNTRY','CROWDING','FAST','SLOW','SLOW_AND_FAST'])universe= ['MINVOL1M','ILLIQUID_MINVOL1M']elif region == 'JPN':universe= ['TOP1600','TOP1200']print(neutralization)print(universe)
```

**第一步：更换天数等input**

```
days = ['5','22','60','120','240']winsorizes = ['1','2','3','4']
```

```
template = '''Alpha Expression'''expressions = []for day1 in days:forwinsorizeinwinsorizes:forday2indays:expression=template.replace('A', day1).replace('B', winsorize).replace('C',day2)expressions.append(expression)
```

**发送回测（请根据自己的代码做适配调整）**

```
#first round find daysfine_alpha_list=[]for expression in expressions:fine_alpha_list.append((expression, decay))fine_pools = load_task_pool(fine_alpha_list,10,10)print(datetime.now())multi_simulate2(fine_pools, neut, region, uni, 0, 1)print(datetime.now())
```

---

### 帖子 #26: 【代碼分享】一鍵測試alpha穩健性，即插即用Python代碼代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 【代碼分享】一鍵測試alpha穩健性即插即用Python代碼代码优化_34092588057111.md
- **讨论数**: 8

在七月成爲正式顧問前，我曾經參加IQC。在Stage 1 IS結算前提交了大約50個alpha，IS分數達到了23,000，雖然不算高但已足以成爲港區第一。可惜這一切都是假象，過幾天OS分數出爐後，我的OS分數只有5,600，明顯地我提交的alpha中出現了嚴重的overfitting，這亦令我的排名從第一跌至第六。

過了幾天我約了Weijie老師談話，並請教了他如何避免overfitting的問題。他給了很多實用的建議，但其中一句特別深刻：

> 在中學的時候你有學過很多數學方法可以測試alpha的表現是否consistent（一致），但你沒有用他們罷了。

現在我就把他這段話轉爲行動。這個program只需你的alpha_id，就可運用量化方法為你的alpha穩健性評分，分數介乎0 ~ 1之間。

這個program一共會進行5個test：

- 一：Long/Short ratio test，ratio越接近1，分數越高。
- 二：Sharpe standard deviation test，Sharpe的標準差越接近0，分數越高。
- 三：Return standard deviation test，Return的標準差越接近0，分數越高。
- 四：滿足Sharpe > 1的比例
- 五：Returns/Drawdown ratio test，ratio越高，分數越高。

最後將五個分數取平均值，就能得到該alpha的最終分數。Program内comment有注明計算每個test分數的函數。

```
import requestsimport numpy as npimport mathfrom datetime import datetimebase_url = "[链接已屏蔽] = base_url + "/authentication"alpha_url = base_url + "/alphas"email = "<YOUR_EMAIL>"password = "<YOUR_PASSWORD>"def get_alpha_robust_score(alpha_id: str, session=None) -> float:    yearly_url = f"{alpha_url}/{alpha_id}/recordsets/yearly-stats"    this_alpha_url = f"{alpha_url}/{alpha_id}"    # Login first.    if session is None:        session = requests.Session()        resp = session.post(login_url, auth=(email, password))        if resp.status_code == requests.status_codes.codes.unauthorized:            if resp.headers["WWW-Authenticate"] == "persona":                biometric_loc = resp.headers["Location"]                input(                    f"Complete the biometric authentication at the following url: {base_url + biometric_loc}\nAfter finished, press Enter to continue ...")                session.post(f"{base_url + biometric_loc}")                resp2 = session.get(login_url)                if resp2.status_code == 204:                    print(f"[{datetime.now().strftime("%Y %b %d %H:%M:%S")}] Not authorized. Try again.")                elif resp2.status_code == 200:                    print(f"[{datetime.now().strftime("%Y %b %d %H:%M:%S")}] Successfully authenticated.")        elif resp.status_code == 200:            print(f"[{datetime.now().strftime("%Y %b %d %H:%M:%S")}] Successfully authenticated.")    # Get the data, except for the last year    stats = session.get(yearly_url).json()["records"][: -1]    is_result = session.get(this_alpha_url).json()["is"]    long, short, sharpe, returns, drawdown = (np.array([]) for _ in range(5))    total_returns, total_drawdown = is_result["returns"], is_result["drawdown"]    for stat in stats:        long = np.append(long, stat[3])        short = np.append(short, stat[4])        sharpe = np.append(sharpe, stat[6])        returns = np.append(returns, stat[7])        drawdown = np.append(drawdown, stat[8])    # Test 1    # Take the function 2x/(1+x^2). Maps from [0, +inf) to [0, 1], and output the same value for reciprocals. Average this score over the whole IS period.    x1 = np.where((short != 0) & (long != 0), long / short, 0)    score1 = np.mean(2 * x1 / (1 + x1 ** 2))    # Test 2    # Take the function e^-0.25x. Maps from [0, +inf) to [0, 1].    x2 = np.std(sharpe)    score2 = math.exp(-0.25 * x2)    # Test 3    # Take the function e^-0.25x. Maps from [0, +inf) to [0, 1].    x3 = np.std(returns)    score3 = math.exp(-0.25 * x3)    # Test 4    # The ratio of years with sharpe > 1    score4 = np.mean(sharpe > 1)    # Test 5    # Take the function tanh(x). Maps from (0, +inf) to (0, 1).    score5 = math.tanh(total_returns / total_drawdown) if total_drawdown > 0 else 0    return round(0.2 * (score1 + score2 + score3 + score4 + score5), 4)
```

以下是一些運行效果的範例：
（一，score=0.9436）
 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> max(Broup_rank(est_12m_ndt_median,
> stal
> tOp4gBCS),
> ts_rank(est_IZm_ndt_median, 252) )
> 们 Power Pool Alpha
> Pyramid thene: EURIDTIPVX1
> FyramiytheTe: EURIDIIANALYST1.5
> ABgregate Data
> Shsro=
> TITTTI=
> Firnssc
> R-UCns
> Da'do
> Marein
> Simulation Settings
> 2.99
> 69%
> 2.00
> 5.62%
> 2.94%6
> 16.8
> 900
> Instrumemt Type
> Region
> Universe
> Language
> Dcay
> Dlay
> Truncaton
> Newtralization
> Pastewrialion
> NaN Hanlng
> Unit Handling
> EqUID
> EUIR
> TCF2SC
> SSECTESSIT
> 3.05
> Fas: Factors
> TIT
> Vear
> Sharpe
> Turover
> Ftness
> Returs
> Dawdown
> Nargin
> Long Count
> Short Count
> 2013
> 7.374
> 3.7
> -S
> 0.30汩
> 213:
> 1013
> 134
> 2014
> 2.55
> 7.12
> 5.723
> 0.32汩
> 1_30
> C
> 1330
> 201
> E.抡汩
> 4.30
> 133
> SE:
> 70
> 170
> 1353
> Clone Alpha
> ZOIE
> 2.53
> LJE;
> 353
> 1.11汩
> 14049
> 13-5
> 2017
>  
> 5313
> 0.-15
> 13.339:
> 1435
> 1455
> 201
> 2.74
> 14:
> 1415
> T:
> 11355:
> 1477
> 1s
> N Chart
> PIL
> 2019
> 2.73
> E.S
> 一133
> 1.115
> 13459
> 136
> 1455
> 2020
> 25
> S汩
> 73395
> 325
> 22239:
> 1335
> 1425
> 2021
> 2.57
> Es
> 5.723
> T:
> 13459
> 143
> 1137
> DOJK
> 2022
> E.32
> 0.70
> 3.173
> 2.34汩
> 10.055
> 1435
> 1138
> 2023
> ~1.13
> _
> 1.57
> 375
> 0.545
> 3155t
> 14
> 1450
> OJK
> Investability constrained
> Aggregate Data
> SArCe
> TUTNOIE
> FIIeS
> TCJTT
> UrauOUITT
> 41aFIT
> 2.48
> 4.03%
> 1.54
> 4.839
> 2.6
> 23.9
> 0000
> 2014
> 2015
> 2015
> 2017
> 2015
> 2019
> 2020
> 2021
> 20
> 2023
  
> [!NOTE] [图片 OCR 识别内容]
> Project
> aplpy
> playground py
> 三 alpha_2025_08_11_173717.CsV
> maln py
> alpha_2025_07_31_201113.CsV
> def get_alpha_robust
> SCOre (alpha_id:
> StT
> Session=None )
> float:
> 04 01 3
> alpha_2025_07_31_224131.CsV
> The ratio
> 0f years With
> sharpe
> 三 alpha_2025_08_01_174315.CsV
> SCOPE4
> 叩.Mean(sharpe
> 三 alpha_2025_08_02_134530.CsV
> |
> 三 alpha_2025_08_02_174922.CsV
> # Test
> 三 alpha_2025_08_03_223811.CsV
> # Take
> the function
> tanhCx )
> SCOTe5
> nath
> tanh (total_returns
> total_drawdown) 讦f
> total_draldoyn
> elSe
> 三 alpha_2025_08_09_014818.CsV
> 三 alpha_2025_08_10_232930.CsV
> peturn
> Found
> (0.2
> (SCOreI
> SCQReZ
> SCOPE3
> SCQReG
> SCOre5), 4
> 三 alpha_2025_08_10_235640.CsV
> 三 alpha_2025_08_11_002448.CsV
> 三 alpha_2025_08_11_003126.CsV
> --name__
> _main_
> 三 alpha_2025_08_11_124526.CsV
> SCOPE
> get_alpha
> Fobust_SCOFe(
> dPIIVJr2
> alpha_2025_08_11_173717.CsV
> print(score)
> configjson
> abC py
> aplpy
> bot py
> Client py
> 1311
> Run
> playground
> 1 :
> C: |Useps 114725 IPycharmprojects IWorldquant |. Venv IScripts Ipython
> exe C: Users |14725|Pycharmprojects IIorldquant Iplayground .py
> Complete
> the
> biometric
> authentication at
> the
> following
> url: hts:Llaiwpldqwantbma n comlaythentieationlpersonaiquipying_LZXIYKKUNQE9Z8IVSTZGCBRGDW
> After finished,
> press
> Enter
> continue
> [2025
> 11 20:18:28] SUccessfully
> authenticated
> 0.9436
> Process finished With
> exit
> Code
> ?9
> Worldouant
> playground py
> AVG: Not enough Values
> 36.45
> CRLF
> UTF 8
> Spaces
> Python 3.12 (WorldQuant)
> USagE
> AUg
 
（二，score=0.75）


> [!NOTE] [图片 OCR 识别内容]
> Project
> aplpy
> playground py
> 三 alpha_2025_08_11_173717.CsV
> maln py
> alpha_2025_07_31_201113.CsV
> def get_alpha_robust
> SCOre (alpha_id:
> StT
> Session=None )
> float:
> 44』1
> alpha_2025_07_31_224131.CsV
> The ratio
> 0f years With
> sharpe
> 三 alpha_2025_08_01_174315.CsV
> SCOPE4
> 叩.Mean(sharpe
> 三 alpha_2025_08_02_134530.CsV
> |
> 三 alpha_2025_08_02_174922.CsV
> # Test
> 三 alpha_2025_08_03_223811.CsV
> # Take
> the function
> tanhCx )
> SCOTe5
> nath
> tanh (total_returns
> total_drawdown) 讦f
> total_draldoyn
> elSe
> 三 alpha_2025_08_09_014818.CsV
> 三 alpha_2025_08_10_232930.CsV
> peturn
> Found
> (0.2
> (SCOreI
> SCQRe2
> SCOPE3
> SCQReG
> SCOre5), 4
> 三 alpha_2025_08_10_235640.CsV
> 三 alpha_2025_08_11_002448.CsV
> 三 alpha_2025_08_11_003126.CsV
> --name__
> _main_
> 三 alpha_2025_08_11_124526.CsV
> SCOPE
> get_alpha
> Fobust_SCOFe(
> "Z9WRQQ3
> alpha_2025_08_11_173717.CsV
> print(score)
> configjson
> abC py
> aplpy
> bot py
> Client py
> 1311
> Run
> playground
> After finished
> press
> Enter
> continue
> [2025
> 20:22:52] SUccessfully
> authenticated
> C:seslg225
> pychammppoiectslopldqyantlplayqpoyw N:52:
> Runtimellarning:
> invalid
> Value
> encountered i
> Uivide
> 0.75
> Process finished With
> exit
> Code
> 89
> Worldouant
> playground py
> AVG: Not enough Values
> 84.1
> CRLF
> UTF 8
> Spaces
> Python 3.12 (WorldQuant)
> USagE
> AUg
  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> dfI
> VeC_sUm(anl6g_ndebt_most
> ecent_period_end_dt); max(group_neutralize (dfl,
> oth455_competitor
> Shsro=
> TITTTI
> Firnsss
> R-UCns
> Cra'do
> Aggr
> Data
> Warzin
> 1.06
> 1.54%
> 0.78
> 6.78%
> 6.35%
> 88.23900
> Simulation Settings
> Instrument Type
> Region
> Unierse
> Langwaye
> Decay
> Delay
> Truncation
> Neutraliation
> Pasteuriation
> NaN Handling
> Unit Handli
> Vear
> Shrpe
> Tumover
> NT-
> Retums
> Uawdown
> Maryin
> Long Count
> Short Count
> Equity
> NIO_I
> Excression
> 0.35
> TrwJins
> CC
> VEr
> 201
> 0.03
> TTL
> 3.039
> TTL
> 0.3C20
> 2014
> 0.07
> 0.1
> 3.039
> TTI
> U.Oo
> Z05
> 0.23
> 1.55
> 12.55:
> ZOIE
> O.EG
> 52汩
> 5.34沉
> 5.1420
> 1257
> 1317
> Clone Alpha
> 20
> 3汩
> SES:
> 3汩
> 3.1020
> _
> 2325
> 201
> 1.03
> 5
> .7
> EETO:
> 3汩
> 3.SE20
> 2352
> Chart
> 2019
> 022
> 一13
> 一
> 1227
> 2330
> PIL
> 2020
> 1,315
> 13.339
> 3汩
> ;
> 1-1
> 213
> 2021
> 0.53
> 1.31汩
> 7.67
> 5219
> 3.3
> 3.-320
> 1771
> 2720
> 2022
> 1.32
> 11.339
> 14
> 171.540
> 2512
> 202
> 3.53
> 1.31汩
> 12.259
> _汩
> 137.5420
> 2.
> OJK
> Correlation
> Self Correlation
> IHMUMT
> TNIMUNI
> L35t Rur -
> 2014
> 2015
> 2016
> 2017
> 2015
> 2019
> 2020
> 2021
> 2022
> 2023
> POWeF Pool Correlation
> TsmI
> WTimu
> EBate
> 73


我個人的建議是，最終分數大於0.9才好提交。
希望這個program對大家有幫助，亦歡迎任何意見或debug建議。最後祝大家vf爆1，base payment滿滿，直通GM👑！
（大家別忘了點贊這個post😁😁

---

### 帖子 #27: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo](../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo)
> 结合我最近参加的新顾问培课程中关于如何利用MCP来开发、优化alpha等内容，发表我的经验，顺便谈点感想。

作为新顾问的一份子，尤其代表零编程基础和零金融学基础的双小白，刚入门的我，只能靠模仿论坛中各位大佬，用他们现有的代码，跑论坛中现有的模板，虽然是“抄作业”，但我觉得完全不丢人，因为我相信没有谁与生俱来就拥有这能力，都是从模仿开始。于是我便靠着现有资源（三阶模板）每天碰碰运气，这样做的结果是一天有一天没，两天打渔三天晒网，不是跑不出来，而是跑出来的相关性太高。特别是11月开始深挖IND地区的时候，断粮了...


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Regular
> Regular
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> 儿52079 (Me)
> 0,00
> 0.50
> 0,37
> 0.19
> 0,00
> 0,00
> Tot
> policable
> Mainlar
> Super
> Super
> Super



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 转为正式顾问


直到11月8日，参加了新顾问的线上培训，课程上老师分享了很多能提高效率的工具和方法，其中包括了如何用MCP开发alpha模板，如何用app来实现全流程自动化。又恰逢IND地区开放，于是我决定，为了提升我的研究能力，接下来一段时间专注于IND地区的alpha开发（尽管不建议新手跑IND），当然我的方法也从开始的三阶代码换成了MCP和APP工具。

经过小半个月在IND地区的实践，发现挖出来的alpha老是出现几种问题，总结如下：

- 现有模板跑出来的相关性过高，shi都吃不上一口热的；
- 相关性低的，非常容易出现“Robust universe Sharpe of  **XX**  is below cutoff of  **X** .”
- 其他常见问题。

在拜读了大量论坛经验帖子后，决定将相关性太高的alpha直接放弃，于是乎突破点就集中在了如何解决Robust universe Sharpe过低上面，这里要特别感谢ZX12447大佬的分享，让我有了灵感，再结合MCP的智慧，创建了一个专门用于优化Robust universe Sharpe的工作流。基于该工作流，我成功优化几个alpha，解决了Robust universe Sharpe不达标的问题。

优化前问题：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained Pnl
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 05
> 9PASS
> Sharoe oT 3.25
> abOVe CUOffcf 1.58
> Finess of 3.11 isabove Cutoffof 1.
> Turnover of 15,60%
> abore CUtof of 196,
> Turpoverof 15.60%
> below CUOffof 4096.
> INeisht is WelI distribu-ed oerinstruments
> Sub-universe Sharpe CT 1.4isaboire Cutoff ot 0.96.
> 2year Sharpe Of 2.58 is
> bore Cutoff of 1.58,
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier oT -
> Effective Pyramid coun-for Genius is
> These -hemes mazch with the followinE multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The finalthEME Multiplizris 2
> 1FAIL
> Robust universe Sharpe Of 0.98
> below CUTOfOf1.
> 4PENDING
 优化后效果：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> TOM
> 5OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained
> Pn
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10PASS
> Sharpe OT 3.21
> aboVe cUOff of
> Fizness of 3,01isaboire Cutoff of -
> Turnoverof 18.2896
> aboie CUtoTf 196
> Turnover of 18.28%
> below CUOff of 40%
> Weisht is WEIl distrbuzed overinstruments。
> Sub-universe Sharpe
> 1.43
> bove Cutof of 0.95,
> Robust uniers=
> Of 1.01
> abore Cutoff ot
> 2year Sharpe Of 2.15 is above CutOff of 一
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier or
> Effectiye Pyramid Counzfor Genius
> These themes mazch with the followine multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The final theme multiplieris 2
> PENDING
> Shrpe


虽然这个alpha最终因相关性过高而未被提交，但是这是我用工作流成功优化的第一个alpha，所以将它作为代表案例展示出来。任务完成后，我让MCP将本次优化过程总结成了工作流，并且每次基于该工作流成功优化后将案例添加进工作流中。


> [!NOTE] [图片 OCR 识别内容]
> 9
> 你说
> 很好请将本次对话总结为优化robust的工作流
> API请求
> 50.0054
> Roo 说
> 我来为您创建
> 完整的IN0地区Robust universe Sharpe优化工作流文档。
> 检查点
> [
> 需要新建文件
> IND_Robust_Sharpe_优化工作流 .md
> +212
> -0巴
> 二
> API请求
> 50.0033
> 任务完咸


从这以后（11月23日），我竟然恢复了口粮，并且开始提交纯ra（之前都是ppa），今天（27日）提交了3个ra，所以借用论坛一位大佬的话“ *要重视你生产的每一个alpha* ”，因为它可能就是你下一个成功提交的对象。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod
> IESTI
> Correlation
> Correlation
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.6> 1
> e.6> 1
> e6>1
> SeeC
> e.6 >
> e.6 >
> anonymOUs
> Reaular
> ACTTVE
> 11/2712025 EST
> IND
> TOPSOO
> 0.58
> 0.61
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> 0.30
> 0.68
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> ReadyToSubmit
> 0.14
> 0.66
> anonymoUs
> Regular
> ACTIVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.41
> 0.49
> anonymOUs
> Reaular
> ACTTVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.13
> 0.70
> anonymoUs
> Reaular
> ACTTVE
> 11/25/2025 EST
> IND
> TOPSOO
> O.00
> 0.65
> anonymOUs
> Reaular
> ACTTVE
> 11/23/2025 EST
> IND
> TOPSOO
> 0.02
> 0.68
> anonymoUs
> ACTTVE
> 11/02/2025 EST
> IND
> TOPSOO
> O.00
> 0.17
> Reaular


最后送给诸君一句话并附上工作流：
 **The journey of a thousand miles begins with one step. JUST DO IT.**

```
# IND地区Robust Universe Sharpe优化工作流## 问题背景在IND地区alpha开发中，经常遇到**Robust universe Sharpe略低于1.0**的问题，导致无法提交。本工作流基于社区经验和实际案例，提供系统化的解决方案。## 工作流概览```mermaidgraph TD    A[诊断问题] --> B{分析差距}    B -->|差距<0.1| C[轻度优化]    B -->|差距>0.1| D[重度优化]    C --> E[时间参数调整]    C --> F[运算符优化]    D --> G[结构重构]    E --> H[测试验证]    F --> H    G --> H    H --> I{是否达标}    I -->|是| J[提交准备]    I -->|否| C```## 诊断阶段### 1. 问题识别```python# 检查Robust universe Sharpe指标LOW_ROBUST_UNIVERSE_SHARPE:  - result: FAIL  - limit: 1.0  - value: 0.98  # 差距0.02```### 2. 差距分析- **轻度问题**: 差距 < 0.1 (推荐本工作流)- **重度问题**: 差距 > 0.1 (建议重构alpha逻辑)## 优化工具箱### 核心优化方法#### 1. 时间参数调整 (最有效)```python# 原始ts_backfill(x, 60) → ts_backfill(x, 75)group_backfill(x, sector, 120) → group_backfill(x, sector, 275)# 推荐参数范围- ts_backfill: 60 → 75, 90, 120- group_backfill: 120 → 180, 252, 275```#### 2. 运算符增强```python# 添加稳定性运算符group_zscore(x, sector)        # 标准化信号ts_scale(x, 0.5)               # 时间序列缩放signed_power(x, 0.6)           # 符号幂变换```#### 3. 中性化优化```python# 尝试不同中性化组合group_neutralize(x, industry)group_neutralize(x, sector)group_neutralize(x, subindustry)group_neutralize(x, market)  # 对模型数据类Alpha特别有效```**中性化策略选择指南**：- **模型数据类Alpha**：优先尝试MARKET中性化- **基本面数据类Alpha**：优先尝试SECTOR/INDUSTRY中性化- **技术指标类Alpha**：根据数据特性选择合适的中性化层级#### 4. 截尾处理优化```python# 调整winsorize参数winsorize(x, std=4) → winsorize(x, std=3)winsorize(x, std=4) → winsorize(x, std=5)```## 实战案例### 案例1：IND地区imb5_score优化**原始alpha (FAIL)**```pythonfilled_score = ts_backfill(imb5_score, 60);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);signed_alpha = signed_power(neutralized, 0.5);final_alpha = group_backfill(signed_alpha,sector,120,std=4);final_alpha```- Robust Sharpe: 0.98 (FAIL)**优化版本1 (PASS)**```python3```- Robust Sharpe: 1.02 (PASS)**优化版本2 (简化版)**```pythonfilled_score = ts_backfill(imb5_score, 75);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);final_alpha = group_backfill(neutralized,sector,275,std=4);final_alpha```- Robust Sharpe: 1.01 (PASS)### 案例2：IND地区score_analyst_estimate_revisions优化（中性化策略优化）**原始alpha (FAIL)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 138), std=0.92), 108), 0.8), densify(sector))```- Robust Sharpe: 0.99 (FAIL)- 数据字段：score_analyst_estimate_revisions (覆盖率86.45%，金字塔乘数1.6)**优化版本 (PASS)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 150), std=0.85), 120), 0.8), densify(market))```- **关键优化**：中性化从SECTOR改为MARKET- **参数调整**：ts_backfill(138→150), ts_zscore(108→120), winsorize(std=0.92→0.85)- **性能提升**：  - Robust Sharpe: 0.99 → 1.11 (+12.1%)  - PnL: 11,095,177 → 12,997,115 (+17.1%)  - Sharpe: 2.56 → 2.62 (+2.3%)  - Fitness: 2.06 → 2.51 (+21.8%)  - 周转率: 16.63% → 13.66% (-17.9%)**核心洞察**：对于IND地区的模型数据类Alpha，MARKET中性化配合适当的时间窗口调整能有效提升Robust Sharpe表现，同时改善整体性能指标。## 系统化优化流程### 步骤1：基础诊断1. 运行原始alpha获取基准数据2. 记录所有检查项结果3. 重点关注Robust universe Sharpe差距### 步骤2：轻度优化 (差距<0.1)```python# 第一轮：时间参数调整尝试组合：- ts_backfill(60→75), group_backfill(120→275)- ts_backfill(60→90), group_backfill(120→252)- ts_backfill(60→120), group_backfill(120→180)```### 步骤3：运算符增强```python# 第二轮：添加稳定性运算符在group_neutralize后添加：- group_zscore(x, sector)- ts_scale(x, 0.5)- signed_power(x, 0.6)```### 步骤4：参数微调```python# 第三轮：参数优化调整：- winsorize std参数 (3,4,5)- signed_power指数 (0.5,0.6,0.7)- decay值 (0,5,20)```### 步骤5：验证与选择1. 比较所有优化版本的性能2. 选择运算符最少的版本3. 确保其他指标不受影响## 避免过拟合原则### 运算符数量控制- **理想**: 3-5个运算符- **可接受**: 6-8个运算符  - **风险**: >8个运算符### 经济意义保持- 每次优化应有合理的金融解释- 避免单纯为了提升指标而堆砌运算符- 保持alpha逻辑的简洁性和可解释性## IND地区特殊注意事项### 数据特性- Universe: 仅支持TOP500- 中性化选项有限- 数据字段相对较少### 优化策略1. **优先时间参数调整** - 对IND地区最有效2. **谨慎使用复杂运算符** - 避免过拟合3. **关注数据质量** - IND地区数据相对稀疏## 成功指标### 主要目标- ✅ Robust universe Sharpe ≥ 1.0- ✅ 其他检查项全部PASS- ✅ 运算符数量控制在合理范围### 次要目标  - 📈 IS Sharpe保持或提升- 💰 PnL表现稳定- 🔄 Turnover在合理范围内## 工具与资源### BRAIN平台工具- `get_platform_setting_options()` - 获取有效设置- `create_simulation()` - 测试优化版本- `get_alpha_details()` - 分析详细结果### 社区经验- **group_backfill/ts_backfill** - 时间参数调整最有效- **group_zscore** - 增强信号稳定性- **winsorize** - 处理异常值- **避免过度复杂化** - 保持alpha简洁## 总结本工作流通过**系统化的诊断→优化→验证**流程，有效解决IND地区Robust universe Sharpe问题。基于成功案例经验，关键优化策略包括：1. **精准诊断** - 明确问题差距和数据类型2. **中性化策略优化** - 根据数据类型选择合适的中性化层级3. **时间参数调整** - 适当延长时间窗口增强稳定性4. **避免过拟合** - 保持alpha逻辑简洁性和经济意义### 成功案例验证**score_analyst_estimate_revisions优化案例**证明了：- **MARKET中性化**对模型数据类Alpha效果显著- **参数微调**能同时提升多个性能指标- **整体性能提升**：Robust Sharpe +12.1%，PnL +17.1%，Fitness +21.8%通过这个方法，可以将接近达标的alpha（如0.98-0.99）成功优化到合格水平（≥1.0），同时显著提升整体性能表现。
```

---

### 帖子 #28: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享_36617664667159.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo](../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo)
> 结合我最近参加的新顾问培课程中关于如何利用MCP来开发、优化alpha等内容，发表我的经验，顺便谈点感想。

作为新顾问的一份子，尤其代表零编程基础和零金融学基础的双小白，刚入门的我，只能靠模仿论坛中各位大佬，用他们现有的代码，跑论坛中现有的模板，虽然是“抄作业”，但我觉得完全不丢人，因为我相信没有谁与生俱来就拥有这能力，都是从模仿开始。于是我便靠着现有资源（三阶模板）每天碰碰运气，这样做的结果是一天有一天没，两天打渔三天晒网，不是跑不出来，而是跑出来的相关性太高。特别是11月开始深挖IND地区的时候，断粮了...


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Regular
> Regular
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> 儿52079 (Me)
> 0,00
> 0.50
> 0,37
> 0.19
> 0,00
> 0,00
> Tot
> policable
> Mainlar
> Super
> Super
> Super



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 转为正式顾问


直到11月8日，参加了新顾问的线上培训，课程上老师分享了很多能提高效率的工具和方法，其中包括了如何用MCP开发alpha模板，如何用app来实现全流程自动化。又恰逢IND地区开放，于是我决定，为了提升我的研究能力，接下来一段时间专注于IND地区的alpha开发（尽管不建议新手跑IND），当然我的方法也从开始的三阶代码换成了MCP和APP工具。

经过小半个月在IND地区的实践，发现挖出来的alpha老是出现几种问题，总结如下：

- 现有模板跑出来的相关性过高，shi都吃不上一口热的；
- 相关性低的，非常容易出现“Robust universe Sharpe of  **XX**  is below cutoff of  **X** .”
- 其他常见问题。

在拜读了大量论坛经验帖子后，决定将相关性太高的alpha直接放弃，于是乎突破点就集中在了如何解决Robust universe Sharpe过低上面，这里要特别感谢ZX12447大佬的分享，让我有了灵感，再结合MCP的智慧，创建了一个专门用于优化Robust universe Sharpe的工作流。基于该工作流，我成功优化几个alpha，解决了Robust universe Sharpe不达标的问题。

优化前问题：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained Pnl
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 05
> 9PASS
> Sharoe oT 3.25
> abOVe CUOffcf 1.58
> Finess of 3.11 isabove Cutoffof 1.
> Turnover of 15,60%
> abore CUtof of 196,
> Turpoverof 15.60%
> below CUOffof 4096.
> INeisht is WelI distribu-ed oerinstruments
> Sub-universe Sharpe CT 1.4isaboire Cutoff ot 0.96.
> 2year Sharpe Of 2.58 is
> bore Cutoff of 1.58,
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier oT -
> Effective Pyramid coun-for Genius is
> These -hemes mazch with the followinE multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The finalthEME Multiplizris 2
> 1FAIL
> Robust universe Sharpe Of 0.98
> below CUTOfOf1.
> 4PENDING
 优化后效果：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> TOM
> 5OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained
> Pn
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10PASS
> Sharpe OT 3.21
> aboVe cUOff of
> Fizness of 3,01isaboire Cutoff of -
> Turnoverof 18.2896
> aboie CUtoTf 196
> Turnover of 18.28%
> below CUOff of 40%
> Weisht is WEIl distrbuzed overinstruments。
> Sub-universe Sharpe
> 1.43
> bove Cutof of 0.95,
> Robust uniers=
> Of 1.01
> abore Cutoff ot
> 2year Sharpe Of 2.15 is above CutOff of 一
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier or
> Effectiye Pyramid Counzfor Genius
> These themes mazch with the followine multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The final theme multiplieris 2
> PENDING
> Shrpe


虽然这个alpha最终因相关性过高而未被提交，但是这是我用工作流成功优化的第一个alpha，所以将它作为代表案例展示出来。任务完成后，我让MCP将本次优化过程总结成了工作流，并且每次基于该工作流成功优化后将案例添加进工作流中。


> [!NOTE] [图片 OCR 识别内容]
> 9
> 你说
> 很好请将本次对话总结为优化robust的工作流
> API请求
> 50.0054
> Roo 说
> 我来为您创建
> 完整的IN0地区Robust universe Sharpe优化工作流文档。
> 检查点
> [
> 需要新建文件
> IND_Robust_Sharpe_优化工作流 .md
> +212
> -0巴
> 二
> API请求
> 50.0033
> 任务完咸


从这以后（11月23日），我竟然恢复了口粮，并且开始提交纯ra（之前都是ppa），今天（27日）提交了3个ra，所以借用论坛一位大佬的话“ *要重视你生产的每一个alpha* ”，因为它可能就是你下一个成功提交的对象。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod
> IESTI
> Correlation
> Correlation
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.6> 1
> e.6> 1
> e6>1
> SeeC
> e.6 >
> e.6 >
> anonymOUs
> Reaular
> ACTTVE
> 11/2712025 EST
> IND
> TOPSOO
> 0.58
> 0.61
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> 0.30
> 0.68
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> ReadyToSubmit
> 0.14
> 0.66
> anonymoUs
> Regular
> ACTIVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.41
> 0.49
> anonymOUs
> Reaular
> ACTTVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.13
> 0.70
> anonymoUs
> Reaular
> ACTTVE
> 11/25/2025 EST
> IND
> TOPSOO
> O.00
> 0.65
> anonymOUs
> Reaular
> ACTTVE
> 11/23/2025 EST
> IND
> TOPSOO
> 0.02
> 0.68
> anonymoUs
> ACTTVE
> 11/02/2025 EST
> IND
> TOPSOO
> O.00
> 0.17
> Reaular


最后送给诸君一句话并附上工作流：
 **The journey of a thousand miles begins with one step. JUST DO IT.**

```
# IND地区Robust Universe Sharpe优化工作流## 问题背景在IND地区alpha开发中，经常遇到**Robust universe Sharpe略低于1.0**的问题，导致无法提交。本工作流基于社区经验和实际案例，提供系统化的解决方案。## 工作流概览```mermaidgraph TD    A[诊断问题] --> B{分析差距}    B -->|差距<0.1| C[轻度优化]    B -->|差距>0.1| D[重度优化]    C --> E[时间参数调整]    C --> F[运算符优化]    D --> G[结构重构]    E --> H[测试验证]    F --> H    G --> H    H --> I{是否达标}    I -->|是| J[提交准备]    I -->|否| C```## 诊断阶段### 1. 问题识别```python# 检查Robust universe Sharpe指标LOW_ROBUST_UNIVERSE_SHARPE:  - result: FAIL  - limit: 1.0  - value: 0.98  # 差距0.02```### 2. 差距分析- **轻度问题**: 差距 < 0.1 (推荐本工作流)- **重度问题**: 差距 > 0.1 (建议重构alpha逻辑)## 优化工具箱### 核心优化方法#### 1. 时间参数调整 (最有效)```python# 原始ts_backfill(x, 60) → ts_backfill(x, 75)group_backfill(x, sector, 120) → group_backfill(x, sector, 275)# 推荐参数范围- ts_backfill: 60 → 75, 90, 120- group_backfill: 120 → 180, 252, 275```#### 2. 运算符增强```python# 添加稳定性运算符group_zscore(x, sector)        # 标准化信号ts_scale(x, 0.5)               # 时间序列缩放signed_power(x, 0.6)           # 符号幂变换```#### 3. 中性化优化```python# 尝试不同中性化组合group_neutralize(x, industry)group_neutralize(x, sector)group_neutralize(x, subindustry)group_neutralize(x, market)  # 对模型数据类Alpha特别有效```**中性化策略选择指南**：- **模型数据类Alpha**：优先尝试MARKET中性化- **基本面数据类Alpha**：优先尝试SECTOR/INDUSTRY中性化- **技术指标类Alpha**：根据数据特性选择合适的中性化层级#### 4. 截尾处理优化```python# 调整winsorize参数winsorize(x, std=4) → winsorize(x, std=3)winsorize(x, std=4) → winsorize(x, std=5)```## 实战案例### 案例1：IND地区imb5_score优化**原始alpha (FAIL)**```pythonfilled_score = ts_backfill(imb5_score, 60);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);signed_alpha = signed_power(neutralized, 0.5);final_alpha = group_backfill(signed_alpha,sector,120,std=4);final_alpha```- Robust Sharpe: 0.98 (FAIL)**优化版本1 (PASS)**```python3```- Robust Sharpe: 1.02 (PASS)**优化版本2 (简化版)**```pythonfilled_score = ts_backfill(imb5_score, 75);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);final_alpha = group_backfill(neutralized,sector,275,std=4);final_alpha```- Robust Sharpe: 1.01 (PASS)### 案例2：IND地区score_analyst_estimate_revisions优化（中性化策略优化）**原始alpha (FAIL)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 138), std=0.92), 108), 0.8), densify(sector))```- Robust Sharpe: 0.99 (FAIL)- 数据字段：score_analyst_estimate_revisions (覆盖率86.45%，金字塔乘数1.6)**优化版本 (PASS)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 150), std=0.85), 120), 0.8), densify(market))```- **关键优化**：中性化从SECTOR改为MARKET- **参数调整**：ts_backfill(138→150), ts_zscore(108→120), winsorize(std=0.92→0.85)- **性能提升**：  - Robust Sharpe: 0.99 → 1.11 (+12.1%)  - PnL: 11,095,177 → 12,997,115 (+17.1%)  - Sharpe: 2.56 → 2.62 (+2.3%)  - Fitness: 2.06 → 2.51 (+21.8%)  - 周转率: 16.63% → 13.66% (-17.9%)**核心洞察**：对于IND地区的模型数据类Alpha，MARKET中性化配合适当的时间窗口调整能有效提升Robust Sharpe表现，同时改善整体性能指标。## 系统化优化流程### 步骤1：基础诊断1. 运行原始alpha获取基准数据2. 记录所有检查项结果3. 重点关注Robust universe Sharpe差距### 步骤2：轻度优化 (差距<0.1)```python# 第一轮：时间参数调整尝试组合：- ts_backfill(60→75), group_backfill(120→275)- ts_backfill(60→90), group_backfill(120→252)- ts_backfill(60→120), group_backfill(120→180)```### 步骤3：运算符增强```python# 第二轮：添加稳定性运算符在group_neutralize后添加：- group_zscore(x, sector)- ts_scale(x, 0.5)- signed_power(x, 0.6)```### 步骤4：参数微调```python# 第三轮：参数优化调整：- winsorize std参数 (3,4,5)- signed_power指数 (0.5,0.6,0.7)- decay值 (0,5,20)```### 步骤5：验证与选择1. 比较所有优化版本的性能2. 选择运算符最少的版本3. 确保其他指标不受影响## 避免过拟合原则### 运算符数量控制- **理想**: 3-5个运算符- **可接受**: 6-8个运算符  - **风险**: >8个运算符### 经济意义保持- 每次优化应有合理的金融解释- 避免单纯为了提升指标而堆砌运算符- 保持alpha逻辑的简洁性和可解释性## IND地区特殊注意事项### 数据特性- Universe: 仅支持TOP500- 中性化选项有限- 数据字段相对较少### 优化策略1. **优先时间参数调整** - 对IND地区最有效2. **谨慎使用复杂运算符** - 避免过拟合3. **关注数据质量** - IND地区数据相对稀疏## 成功指标### 主要目标- ✅ Robust universe Sharpe ≥ 1.0- ✅ 其他检查项全部PASS- ✅ 运算符数量控制在合理范围### 次要目标  - 📈 IS Sharpe保持或提升- 💰 PnL表现稳定- 🔄 Turnover在合理范围内## 工具与资源### BRAIN平台工具- `get_platform_setting_options()` - 获取有效设置- `create_simulation()` - 测试优化版本- `get_alpha_details()` - 分析详细结果### 社区经验- **group_backfill/ts_backfill** - 时间参数调整最有效- **group_zscore** - 增强信号稳定性- **winsorize** - 处理异常值- **避免过度复杂化** - 保持alpha简洁## 总结本工作流通过**系统化的诊断→优化→验证**流程，有效解决IND地区Robust universe Sharpe问题。基于成功案例经验，关键优化策略包括：1. **精准诊断** - 明确问题差距和数据类型2. **中性化策略优化** - 根据数据类型选择合适的中性化层级3. **时间参数调整** - 适当延长时间窗口增强稳定性4. **避免过拟合** - 保持alpha逻辑简洁性和经济意义### 成功案例验证**score_analyst_estimate_revisions优化案例**证明了：- **MARKET中性化**对模型数据类Alpha效果显著- **参数微调**能同时提升多个性能指标- **整体性能提升**：Robust Sharpe +12.1%，PnL +17.1%，Fitness +21.8%通过这个方法，可以将接近达标的alpha（如0.98-0.99）成功优化到合格水平（≥1.0），同时显著提升整体性能表现。
```

---

### 帖子 #29: 【分析】Genius冲刺! 交一个怎样的alpha能有效提升你的六维数据之定性定量分析
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分析】Genius冲刺 交一个怎样的alpha能有效提升你的六维数据之定性定量分析_34918096433559.md
- **讨论数**: 4


> [!NOTE] [图片 OCR 识别内容]
> Wotloquant 启动 !
> 分析1
> 交一个怎样的 & 能提升六维数据之定性定量分析
> IL47973
> 罗超林


[图片 (图片已丢失)]

在定性定量分析六维数据之前，如果你还不知道啥是genius等级和六维数据，建议去看以一下
 [【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板 – WorldQuant BRAIN]([Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md)  这一篇帖子，有解释了genius定级优胜制和六维数据字面意思，为此帖子做铺垫，和有几率增强六维某些数据的小tips；
        当然还有一些所见即所得的alpha 和 邪修alpha模板(没有)，以及包括一些点塔方法，不可否认的是，帖子内容的点塔方法有混塔嫌疑，没事。同上帖子还有一种明显的混塔方式(会多出一至两个op) 以及 一种隐形的 (不完全，存在小幅度扰动) 混塔方式 (至少多出两个op)，当然还有两种 非显非隐 纯点塔 (与混塔毫无干系) 方法，会大程度降低pc，且不会浪费操作符. 能不能看出来并想到就看自己了 .

[图片 (图片已丢失)]

写这个帖子的初衷是来源于 在冲刺genius等级时，我至少是想要保住我的 Operators per Alpha 和 Fields per Alpha 的. 
        有一天 (前两周)，我在操作自己产出的alpha时，发现有些 alpha 的操作符是大于我的 Operators per Alpha 的，此时我就在想，使用自己未使用的操作符作用在此 alpha 上会让此 alpha 信号变得更好时，我应该把 未使用过的操作符 加之在哪里 (操作符少于Operators per Alpha的alpha上还是大于亦或者是等于) 更加合适或者说怎么来降低 Operators per Alpha 的增大程度. [图片 (图片已丢失)]

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 《喜羊羊与灰太狼》
> 中惬意音乐响起令人放松的蟹螺湾椰树


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> )
> 欲将操作符分配与放置于后验&对前验0的平均操作符的变化程度是否有关?


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 第 genius 季度 ,我巳经在 worldquant 上提交了 N 个a, 将这 N 个a
> 按照某种顺序排列 ,便可得到 Q 序列.记为:
> )
> CN.
> 每个Q平均操作符数量 (不重复计数) Nop_per_alpha 计算公式为:
> N
> N
> Operators_count
> OP_per_alpha
> N
> k=1
> Operators_count 表示第k个 a 的操作符数量.
> C1'
> 02
> 03〉
> 其中 Ok



> [!NOTE] [图片 OCR 识别内容]
> 每个Q平均字段数量 (不重复计数) Nfield_per_alpha 计算公式为:
> Nfield_per_alpha
> Fields_count
> N
> k=l
> Fields_count
> 表示第尼个a 的字段数量.
> 其中 0k



> [!NOTE] [图片 OCR 识别内容]
> 记
> alpha 表示衡量 Q 的 OP_per_alpha 的变化程度 ,公式为:
> OP_per_alpha
> abs (OP_per_alphal
> OP_per_alpha)
> 其中 OP_per_alpha' 表示新增 &后的平均操作符数量。
> 现要提交两个&,一个0的操作符数小于X记为 QOperators_count
> 另外一
> N+I
> 个&的操作符数大于孓记为 QOperators_count
> 为了方便起见 ,我们不妨令已经
> 提交的 N 个c的平均操作符数量记为孓 ,现要增加 M 个操作符.
> Dop_per
> N+2



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> X
> 将这 MI 个操作符作用于 QwtI , 记L =孓+
> 此公
> N + 1
> 式一是为了方便观察先后作用,二是简化表达式 ,便会得到
> Ck



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> MI
> 十
> M
> N +1
> (N+I+ _
> N+2)
> OP_per_alpha'
> 二
> Ixtl +
> N + 1
> N + 2
> LNtI
> M+2



> [!NOTE] [图片 OCR 识别内容]
> 将这 M 个操作符作用于 Qwt2 , 会得到



> [!NOTE] [图片 OCR 识别内容]
> Operators_count
> MI
> 十
> M
> N +1
> (N+1, N+2T)
> OP_per_alpha'
> Ixt2 + N+I
> N + 2
> Lx+2
> M+I



> [!NOTE] [图片 OCR 识别内容]
> 通过化简 ,可以得到
> (N+It, Nt2) OP_Per_
> alpha
> (N+I,N+t2t) OP_Per_
> alpha'
> 也即
> (N+I+, N+2)
> Aop_per_alpha
> (NtI, N+2+ )
> Aop_per_alpha
> 说明操作符作用于某种类型的 & 并不会改变前验 a 的变化程度 .
> 以上证明也只是能说明操作符全部作用于小于或大于X的 Q, 不会改变
> 前验 Q 变化程度 ,还无法说明作用在等于X身上或每种类型作用若干操作符
> 会不会该改变前验 Q 的变化程度.
  
> [!NOTE] [图片 OCR 识别内容]
> 下面我们直接采用后验来证明操作符无论怎么作用于 Q, 对前验 Q 的变
> 化程度没有任何影响 .
> 若此 genils 季度 ,接下来总共还会交0个a,其中小于 等于和大于孓的
> Q分别有4,e,f个 ,有 def = 0等式成立 ,其等式中省略加法运算符号 ,采
> 用抽代并置表示加法.
  
> [!NOTE] [图片 OCR 识别内容]
> N+a
> N+d+e
> N+dtetf
> Operators_count
> Operators_count
> Operators_count
> 不妨记
> Qk
> :
> Qk
> k=N+I
> k=N+d+I
> k=Ntdtetl



> [!NOTE] [图片 OCR 识别内容]
> 分别表示为小于。等于和大于X的操作符数量之和 .同样地 ,现要增加 I 个操作符.
  
> [!NOTE] [图片 OCR 识别内容]
> N+a+etf
> Aop_per_alpha
> abs
> aOperators_count
> M - 孓.0
> /(N + 0) -孓
> K=N+I



> [!NOTE] [图片 OCR 识别内容]
> 从 Aop_per_alpha 公式可以看出干扰 Q 的 Operators per AIpha 的变化程度
> 跟0的操作符总数量。增加的 M 个操作符数量,
> 此 genius 赛季巳交a和操作符
> 数量有关 ,与这 MI 个操作符如何分配和放置无关 .


[图片 (图片已丢失)]

通过计算知道，将操作符分配与放置于后验alpha对前验alpha的平均操作符变化程度无关 . 
        虽无关，但在操作符对后验alpha影响小时，建议将其放置在性能相对而言不那么好的alpha身上，理应当让好鱼卖一个好的价钱 .

[图片 (图片已丢失)]

[图片 (图片已丢失)]  
> [!NOTE] [图片 OCR 识别内容]
> 《天堂度假村》前前右旁的小草地树林


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 二。六维数据定性分析


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 若两个函数&与h有相同的趋势 ,
> 则认为它们在趋势上对等,记为 8~-h.
> 在不考虑 genils 等级时 ,记 fscore 为个人总得分 , rank 为最终评级得分
> fscore
> rank , 也就是说 fscore 趋势与rank 相同 =
> fscore 便与最终得分有相同的效
> 果可作为最终评分 .
  
> [!NOTE] [图片 OCR 识别内容]
> 定性分析 ,记 Operators per Alpha  Operators used -
> Fields per Alpha`
> Rieldsused ,
> Community activity 和 Max simulation streak 分别表示六维的  每
> 个c的平均(去重)操作符数量。操作符的去重使用个数。每个Q 的平均(去重)字
> 段数量,
> 字段使用(去重)数量 rank [社区活跃程度]和最大连续回测天数 ,下面
> 使用简写 ,比如:最大连续回测天数记为 MIsS . 对于六维排名下面给出两种排名方
> 法,一种不需要量纲 .
  
> [!NOTE] [图片 OCR 识别内容]
> 第一种便是 rank , rank 是一个减函数,排名也是一个减函数 .由于 OpA
> 与FPA 越小越好 (有些会为0 ,需排除0) ,所以使用 rank 时尽量保持属于],
> 所以排名为
  
> [!NOTE] [图片 OCR 识别内容]
> rank
> rank
> rank(Ou)
> rank
> rank(Fu) + rank(Ca)
> rank(MIss)
> 十
> OpA2
> 1十
> FPA2
  
> [!NOTE] [图片 OCR 识别内容]
> 这样子是比较合理的 ,
> 按照权重来。每一个维度都是等权的 ,逻辑也是非常清晰的 .
  
> [!NOTE] [图片 OCR 识别内容]
> 但是需要注意的是当 OPA 和FA的数值为 0时,在内层 rank 时应设置为最
> 后一名 .
> 第二种是常用的标准化后加权求和 ,核心思想是:先消除不同指标的量纲
> 和尺度差异 ,再根据指标的重要性赋予权重 ,最后合并成一个综合得分 fscore
  
> [!NOTE] [图片 OCR 识别内容]
> 1.最小-最大归一化 ( Min
> Mac Normalization) , 又称为 [0 ,1]标准化 .
> 公式为
> X
> 3
> 3
> 其中,3表示原始数据 ,
> 是数据中的最小值 ,
> 是数据中的最大值 ,3'
> 是归一化之后的数据 .
> ?min
> ?max
> ?min
> RCmax
  
> [!NOTE] [图片 OCR 识别内容]
> 2.乏
> Score (标准差 )标准化
> 3 一 L
> 乙 =
> 几
> 其中 M: 该指标平均值,
> M = 1
> di
> 
> i=1
> 几
> 1
> O:
> 该指标标准差 ,
> O =
> Di -p)2
> 几
> i=1
  
> [!NOTE] [图片 OCR 识别内容]
> 3.赋予权重分配+综合得分
> fscore , 使用 [0 ,1]标准化公式 ,每个维度都分
> 配在 [0 ,1] ,六个维度使用等权 ,这里同样需要考虑当3' =0时的特殊情况 .
  
> [!NOTE] [图片 OCR 识别内容]
> SCOre
> dimension
> (1 - OpA)
> Ou' + (1 -FA)+ F' + Ca' + Mss'
> i=1
  
> [!NOTE] [图片 OCR 识别内容]
> 最后 rank(fscore ) 即可得出排名 .
  
> [!NOTE] [图片 OCR 识别内容]
> 第三种是我自己想的 ,感觉有一丢丢意义 ,于是在这里说一下,首先去掉
> 些异常值 (在逻辑自洽这块其实应该不要丢弃最好 ,因为每一个顾问的数
> 据都是真实的 ,不存在说是异常的 ),综合得分 fscore -
> 1.找出六维每个维度所有顾问的平均值丛或中位数;
> 几
> 山=1
> Ri
> 几
> i=1
> 2.使用最小公倍数 LCM 方法计算每个维度的权重 weight;
> weight
> LCM(opA; Nou
> NEu; Mca) MMsg)/
> Ri
> 几
> 2二1
> UFpA '
  
> [!NOTE] [图片 OCR 识别内容]
> 3.对于 OpA 和 FPA 数据使用关于均值对称反转 ,取 OpA ' 和 FPA' ,其
> 他维度都有 D' = 2 ;
> OPA
> 二
> 0 , OPA'
> 二 0
> FPA
> 二
> 0 ,RPA' =0
> OPAT
> OpA
> FPA'
> 一
> FPA
> 4.
> 计权重综合得分 fscore =
> fscore
> weight;
> dimension
> 2=1
> 最后 rank(fscore) 即可得出排名 .
> WopA
> WopA
> MppA
> NFpA



> [!NOTE] [图片 OCR 识别内容]
> C
> 欧拉乘积
> 1
> $(8) =
> 工
> 8
> 1-0
> p prime
  
> [!NOTE] [图片 OCR 识别内容]
> 《欧拉乘积公式》以此可证明素数无穷


[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 三 六维数据定量分析


[图片 (图片已丢失)]

[图片 (图片已丢失)]

先说结论:  分而治之！分为三部分，1. Max simulation streak (最大连续回测天数) 保持回测不要断；2. 在社区有效学习；3. 其他四维为一块，如果操作符还未使用完，可以刷，看看上面的结论，操作符放在哪儿效果都是一样的，尽量交能够降低自己的平均操作符和平均字段，从rank来说，优先保证 Operators per Alpha  和 Fields per Alpha 的增量降低，然后再是 Fields used，因为 Operators per Alpha  和 Fields per Alpha 的密度更高，做好一次性rank可以上升好几名 .

[图片 (图片已丢失)]


> [!NOTE] [图片 OCR 识别内容]
> 定量分析 .在数学中, rank 犹如是一个 bug 的存在 ,
> 因为 rank 算是一个
> 指标器 ,
> 可以帮助进行排名 ,但是又没有办法去(计)量化细化它 ,只能类比
> 趋势.
> 由于不好量化 rank , 定性分析第一种方法有内置 ralk , 当有一个维度的
> rank 较低时 ,十分干扰整个排名 ,所以舍弃;第二种方法比较常规且好 ,我们
> 使用笫三种方法来定量分析 .
  
> [!NOTE] [图片 OCR 识别内容]
> 1.
> 计算每个维度的均值丛;
> [bopd] = 5, [bou] = 100, [LEpA]
> 二
> 4, [MRu] = 300, [bca]
> 二
> 25,
> 二150
> 2.计算每个维度的权重 weight;
> LCI
> Nou '
> NRui Hca' |Mss _
> 二 300
> weightopa
> 60, veight
> Ou
> 二
> 3, weightpo4
> 75, veight
> Fu
> 1, weightca
> 12, weight
> U85
> 2
> [Muss
> WopA '
> IFpA '
  
> [!NOTE] [图片 OCR 识别内容]
> 3.计算每个维度应该被权重值?';
> OpA' = 6.6 , Ou'
> 二
> 68 , FPA' = 6.5 , Fu'
> 二
> 260
> Ca'
> 二
> 3
> MIss
> -
> 88
> 4.计算综合得分 fscore;
> fscore
> 
> 60 .6.6 十3 .68+75 .6.5+1
> 260+12
> 33+2.88
> 二
> 1919.5


---

### 帖子 #30: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 839

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #31: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #32: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #33: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季_37179224417303.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #34: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #35: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([L2] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #36: 【环境配置】在Nvim中配置MCP的方法经验分享
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

### 帖子 #37: 【课代表📕】关于2阶段的改进，字段方向Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【课代表】关于2阶段的改进字段方向Alpha Template_31503981064087.md
- **讨论数**: 8

在这里推荐大家可以加入更多新颖的bucket，这里以split为例

bucket(rank(split), range='0.1, 1, 0.1')


> [!NOTE] [图片 OCR 识别内容]
> Simulate Field
> Field description
> Category: Price Volume
> Price Volume
> Type: Matrix
> Stock split ratio
> Region
> Delay
> Universe
> Pyramid Theme
> Theme
>  Coverage
> Users
> Alphas
> Multiplier
> USA
> TOP3000
> 1.1
> 100%
> 803
> 8309
> Show all settings


“Stock split ratio” 就是 “股票分割比率”

我猜测不同分割比率的股票可能会有相似性，就需要去做组内的中性化。

这是我用这个group做出来的某个因子，三条线都非常稳健，大家可以尝试加入自己的二阶段！


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> TRAIN
> TEST
> IS
> 0S
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.61
> 3.659
> 9.76
> 91.349
> 27.059
> 500.019600
> Year
>  Sharpe
> Trnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> .0096
> 00%
> 0.009
> 0.003ooa
> 2014
> 0.0096
> 00%
> 00%
> 0.003oo
> 2015
> 2.39
> 3.3196
> 4.19
> 38.4696
> 8.009
> 232.74360
> 622
> 250
> 2016
> .90
> 2.4396
> 3.05
> 32.1796
> 15.6096
> 264.869600
> 1619
> 282
> 2017
> 0.42
> 2.8696
> 0.28
> ~5.7096
> 14.6096
> 39.82900
> 1758
> 264
> 2018
> 3.20
> 2.7996
> ,35
> 49.2496
> 10.70%6
> 353.
> 33600
> 899
> 318
> 2019
> 2.89
> 3.28%6
> 5.53
> 47.4996
> 10.039
> 289.479600
> 2012
> 241
> 2020
> 0.46
> 3.98%6
> 0.50
> 14.9796
> 31.139
> 75.29300
> 2103
> 194
> 2021
> -7.44
> 3.5496
> 30.34
> 207.92%6
> 8.87%6
> -1,175.77960
> 2179
> 256
> 2021
> 3.22
> 3.9096
> 8.13
> 79.7696
> 16.899
> 409.179600
> 2466
> 328
> 2022
> 5.12
> 3.4096
> 16.03
> 122.51%
> 8.809
> 719.969600
> 2555
> 352
> 2023
> 6.61
> 3.95%
> 32.15
> 295.7196
> 15.3596
> 1,497.829600
> 2344
> 300
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 3.11
> 3.659
> 5.80
> 43.51%
> 11.92%
> 238.169600
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.73
> 2.31%
> 5.98
> 60.02%
> 23.71%
> 520.499600



> [!NOTE] [图片 OCR 识别内容]
> ZON
> 10N
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
> IS Summary
> Period
> TRAIN
> TEST
> 1S
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawaown
> Margin
> 2.07
> 3.24%
> 3.88
> 43.93%
> 33.66%
> 271.019600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2013
> 0.00
> 0.00%
> 0.00
> 0,00q
> 0.009
> 0.003oo
> 2014
> 0096
> 0,00q
> 0.009
> 0.003ooa
> 2015
> 2.39
> 3.31%6
> 4.19
> 38.4696
> 8.009
> 232.749o00
> 622
> 250
> 2016
> 1.90
> 2.43%
> 3.05
> 32.1796
> 15.60%
> 264.86900
> 1619
> 282
> 2017
> -0.42
> 2.86%
> -0.28
> -5.7096
> 14.6090
> 39.823600
> 1758
> 264
> 2018
> 3.20
> 2.7996
> 49.2496
> 10.7096
> 353.
> 39o00
> 899
> 318
> 2019
> 2.89
> 3.2896
> 5.63
> 47.49N6
> 10.0396
> 289.479o00
> 2012
> 241
> 2020
> 0.46
> 3.9896
> 0.50
> 14.9796
> 31.1396
> 75.299600
> 2103
> 194
> 2021
> -7.44
> 3.5496
> 30.34
> -207.92%6
> 8.8796
> 1,175.779600
> 2179
> 256
> 2021
> 3.22
> 3.90%
> 8.13
> 79.
> 6%6
> 16.8996
> 409.
> 79oo0
> 2466
> 328
> 2022
> 5.12
> 3.4096
> 16.03
> 122.5196
> 8.809
> 719.96960o
> 2555
> 352
> 2023
> 6.61
> 3.9596
> 32.15
> 295.7196
> 15.3596
> 1,497.829300
> 2344
> 300
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.93
> 3.24%
> 2.69
> 24.20%
> 13.16%
> 149.28900
> Investability constrained
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> DrawCOwn
> Margin
> 1.73
> 2.16%
> 2.60
> 28.13%
> 34.09%
> 260.289600


---

### 帖子 #38: 一种随机生成 SuperAlpha，进行机器回测的方式代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 一种随机生成 SuperAlpha进行机器回测的方式代码优化_32009801307671.md
- **讨论数**: 21

听了之前 GrandMaster，Master 大佬们的分享，启发颇多，一个比较重要的一点是要交 SuperAlpha。自己确实只手动交过两个，再尝试就都是相关性无法通过测试，而且手动回测速度实在太慢了。

进过反复阅读 SuperAlpha 的文档，尝试，暂时想到了一种随机生成 SuperAlpha 的方式，最近连续几天都有交 SuperAlpha，可能也得益于 PowerPool 比赛的原因交了不少低相关性因子。

分享出来，算是抛砖引玉，有什么建议还请大佬们不吝赐教。

主要思路还是来自文档里的例子，发现这些 Selection 表达式，似乎都有一个共同点，就是多是一些判断条件，相乘，还有一个用来排序的权重字段（比如 turnover）。这个可以理解，判断条件返回布尔值，结果为假返回 0，为真返回 1，只有为真时表达式才有值。

所以想到，可不可以随机选择多个判断条件相乘，最后再乘上一个权重字段，构成表达式。

接下来就是创建条件列表，有哪些条件呢？

文档里提到可以给 alpha 打 tag，category，但是自己都是机器跑出来的，自己都无法判断是什么策略，还好可以交给大语言模型判断，对因子经济学含义的理解，我想大语言模型比我强多了。

还有老师培训时提供的灵感，使用以往比赛的限制条件，比如低 turnover，atom，低 correlation，当然应该也可以反过来，高 turnover，高 correlation，多尝试总没有错，反正是用机器跑。

还有一点需要指出，Selection Handling 的选择，看文档有点绕，为了简化，只使用 Positive，因为一些负数的权重，可以通过减法转换成正数。

然后构建了下面这些条件和权重表达式：
selection_expressions.py
```python
import datetime

def category_conditions():
    values = "NONE", "PRICE_REVERSION", "PRICE_MOMENTUM", "VOLUME", "FUNDAMENTAL", "ANALYST", "PRICE_VOLUME", "RELATION", "SENTIMENT"
    return [f"category == \"{value}\"" for value in values]

def color_conditions():
    values = "NONE", "RED", "YELLOW", "GREEN", "BLUE", "PURPLE"
    return [f"category == \"{value}\"" for value in values]

def dataset_conditions(dataset):
    return [f"in(datasets, \"{dataset}\")"]

def favorite_conditions():
    return [f"favorite", "not(favorite)"]

def long_count_conditions():
    return [f"long_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]

def short_count_conditions():
    return [f"short_count > universe_size(universe) * {percent}" for percent in [0.2, 0.3, 0.4, 0.5]]

def name_conditions(name):
    return [f"name == \"{name}\""]

def neutralization_conditions(neutralizes):
    return [f"neutralization == \"{value}\"" for value in neutralizes]

def operator_count_conditions():
    return [f"operator_count <= {cnt}" for cnt in [1, 2, 4, 6, 8, 10]]

def tags_conditions(tag):
    return [f"in(tags, \"{tag}\")"]

def truncation_conditions():
    return [f"truncation <= {value}" for value in [0.01, 0.05, 1]]

def turnover_conditions():
    return [f"turnover < {value}" for value in [0.05, 0.1, 0.2, 0.3, 0.7]]

def universe_conditions(universes):
    return [f"universe == \"{value}\"" for value in universes]

def universe_size_conditions(size=1000):
    return [f"universe_size(universe) >= {size}"]

def datafields_conditions(field):
    return [f"in(datafields, \"{field}\")"]

def dataset_count_conditions():
    return [f"dataset_count <= {value}" for value in [1, 2, 3, 10]]

def self_correlation_conditions():
    return [f"self_correlation <= {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]

def prod_correlation_conditions():
    return [f"prod_correlation < {value}" for value in [0.7, 0.6, 0.5, 0.4, 0.3, 0.2]]

def os_start_date_conditions():
    today = datetime.datetime.today()
    delta_days = [7, 14, 30, 60, 90, 120, 180, 360, 3600]
    dates = [(today-datetime.timedelta(day)).strftime('%Y-%m-%d')
             for day in delta_days]
    return [f"os_start_date > \"{date}\"" for date in dates]

def datacategories_conditions():
    values = "analyst, broker, earnings, fundamental, imbalance, insiders, institutions, \
        macro, model, news, option, other, pv, risk, sentiment, shortinterest, socialmedia".split(',')
    return [f"in(datacategories, \"{value.strip()}\")" for value in values]

def datacategory_count_conditions():
    return [f"datacategory_count <= {value}" for value in [1, 2, 3, 10]]

def datafield_count_conditions():
    return [f"datafield_count <= {value}" for value in [1, 2, 3, 5, 10]]

def weight_expressions():
    return [
        "turnover", '10-turnover',
        '10000-abs(long_count-short_count)', 'long_count+short_count', 'long_count', 'short_count',
        '10-dataset_count',
        '2-self_correlation',
        '2-prod_correlation',
        '100-datafield_count',
        '1'
    ]
```

接下来是随机选择条件，组装 selection 表达式的代码：

```python
import random
import selection_expressions as se
from settings import get_universe_list, get_neutralization_list

region = 'USA'
delay = 1
universe_list = get_universe_list(region)
neutralization_list = get_neutralization_list(region)
conditions = [
    se.category_conditions(),
    se.color_conditions(),
    se.neutralization_conditions(neutralization_list),
    se.universe_conditions(universe_list),
    se.datacategories_conditions(),

se.datacategory_count_conditions(),
    se.dataset_count_conditions(),
    se.datafield_count_conditions(),
    se.long_count_conditions(),
    se.short_count_conditions(),
    se.operator_count_conditions(),

se.prod_correlation_conditions(),
    se.self_correlation_conditions(),
    se.truncation_conditions(),
    se.turnover_conditions(),

se.os_start_date_conditions
]
weight_expressions = se.weight_expressions()

def find_selection_expression():
    while True:
        condition_length = random.randint(1, 4)
        condition_list = random.sample(conditions, condition_length)
        choice_conditions = []
        for condition in condition_list:
            if callable(condition):
                condition = condition()
            choice_conditions.append(random.choice(condition))
        choice_weight_expression = random.choice(weight_expressions)
        select_expression = ' * '.join([f'({exp})' for exp in (choice_conditions + [choice_weight_expression])])
        logger.info(f'random select expression: {select_expression}'    )
        selection_limit = random.choice([20, 30, 50, 70, 100])
        # 检查选择的alpha是否够十个，不然无法进行回测，页面上有这个API：/simulations/super-selection，wqb库好像没有
        response = wqb.get_super_selection(region=region, delay=delay, selection=select_expression, selection_limit=selection_limit)
        if not response or response['count'] < 10:
            continue
        return select_expression, selection_limit

```

结合 combo 表达式，生成最终的 alpha，combo 有点复杂，还不知道如何大量生成，主要使用了文档中的例子，还有 combo_a 操作符。

```python
def get_combo_code_list():
    ret = ['1',
           'stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr); maxCorr = reduce_max(ic); 1 - maxCorr'
           ]
    for day in [500]:
        for algo in ['algo1', 'algo2', 'algo3']:
            code = f"combo_a(alpha, nlength = {day}, mode = '{algo}')"
            ret.append(code)
    return ret

def generate_super_alpha():
    select_expression, selection_limit = find_selection_expression()
    combo_expression = random.choice(get_combo_code_list())
    neutralization = random.choice(neutralization_list)
    return {
        'type': 'SUPER',
        'settings': {
            'instrumentType': 'EQUITY', 'region': 'USA', 'universe': 'TOP3000', 'delay': 1, 'decay': 5, neutralization: 'INDUSTRY', 'truncation': 0.08, 'pasteurization': 'ON', 'unitHandling': 'VERIFY', 'nanHandling': 'OFF', 'language': 'FASTEXPR', 'visualization': False, 'testPeriod': 'P2Y', 'maxTrade': 'ON', 'selectionHandling': 'POSITIVE', 'selectionLimit': selection_limit
        },
        'combo': combo_expression,
        'selection': select_expression
    }
    return {
        "type": "SUPER",
        "settings": {

},
        "combo": combo_expression,
        "selection": select_expression
    }
```
总之，这样生成的SuperAlpha应该还是非常有限的，可能过一段时间就会枯竭了，还需要不断的添加新的低相关性的RegularAlpha才可能延续。combo表达式对PNL影响比较大，还有待学习。

---

### 帖子 #39: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
- **主帖链接**: [L2] 代码分享拉取某个category下的全部dataset并实现批量生产数据预处理备战Pyramid.md
- **讨论数**: 5

```
分享代码给所有冲刺Pyramid的同学，分享不易，感谢点赞评论
```

这套代码结合了三阶框架和ACE Library，之前我们在跑单数据集的时候经常会放弃一些小数据集，从而可能错失一些有效的字段。本代码可以批量拉取某个category下的字段，并进行一定的筛选。

- **核心代码：获取全部datasets**

```
def get_datasets(    s,    instrument_type: str = 'EQUITY',    region: str = 'USA',    delay: int = 1,    universe: str = 'TOP3000'):    brain_api_url = "[链接已屏蔽]    url = brain_api_url + "/data-sets?" +\        f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"    result = s.get(url)    datasets_df = pd.DataFrame(result.json()['results'])    return datasets_df
```

- 筛选需要的category和coverage等信息

```
region = "JPN"region_code = "jpn"universe = "TOP1600"delay = 1datasets_df = get_datasets(s,region='JPN',delay=1,universe='TOP1600')pd.set_option('display.max_columns', None)  # 显示所有列pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值# select needed datasetsselected_datasets_df = datasets_df[    (datasets_df["delay"] == delay) &    (datasets_df["coverage"] > 0.5) & (datasets_df["coverage"] <= 1) &    (datasets_df["fieldCount"] > 0) & (datasets_df["fieldCount"] < 2000) &    (datasets_df["region"] == region) &    (datasets_df["universe"] == universe) &    (datasets_df["userCount"] > 0) & (datasets_df["userCount"] < 100) &    (datasets_df["valueScore"] > 1) & (datasets_df["valueScore"] < 10) &    (datasets_df["category"].apply(lambda x: x.get("id") if isinstance(x, dict) else None) == "analyst")    #(datasets_df["category"]  'analyst')    #datasets_df["name"].str.contains('news', case=False) &    #((datasets_df["category"] == 'analyst') | (datasets_df["category"] == 'analyst'))].sort_values(by=['valueScore'], ascending=False)print(selected_datasets_df)
```

- 批量预处理数据，生成数据大表，这里的作用等价于老师在论坛写的推荐数据

```
reset_fleg = 0for dataset_id in selected_datasets_df['id']:    df1 = get_datafields(s, dataset_id = dataset_id, region= region, universe=universe, delay=delay)    pd.set_option('display.max_columns', None)  # 显示所有列    pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值    df2 = df1[df1['type'] == 'MATRIX']    df3 = df1[df1['type'] == 'VECTOR']    #df4 = df1[df1['type'] == 'GROUP']    try:        print(len(data))        if reset_fleg == 1:            data = []      except NameError:        data = []    if len(df2)>0:        matrix_fields_1 = process_datafields(df1, "matrix")        data.extend(matrix_fields_1)    if len(df3)>0:        vector_fields_1 = process_datafields(df1, "vector")           data.extend(vector_fields_1)    print(dataset_id,'执行完毕')print(len(data))
```

剩下的工作就是套在不同的模版中了，祝大家早日达到MASTER!

---

### 帖子 #40: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
- **主帖链接**: https://support.worldquantbrain.com[L2] 代码分享拉取某个category下的全部dataset并实现批量生产数据预处理备战Pyramid_28040550959511.md
- **讨论数**: 5

```
分享代码给所有冲刺Pyramid的同学，分享不易，感谢点赞评论
```

这套代码结合了三阶框架和ACE Library，之前我们在跑单数据集的时候经常会放弃一些小数据集，从而可能错失一些有效的字段。本代码可以批量拉取某个category下的字段，并进行一定的筛选。

- **核心代码：获取全部datasets**

```
def get_datasets(    s,    instrument_type: str = 'EQUITY',    region: str = 'USA',    delay: int = 1,    universe: str = 'TOP3000'):    brain_api_url = "[链接已屏蔽]    url = brain_api_url + "/data-sets?" +\        f"instrumentType={instrument_type}&region={region}&delay={str(delay)}&universe={universe}"    result = s.get(url)    datasets_df = pd.DataFrame(result.json()['results'])    return datasets_df
```

- 筛选需要的category和coverage等信息

```
region = "JPN"region_code = "jpn"universe = "TOP1600"delay = 1datasets_df = get_datasets(s,region='JPN',delay=1,universe='TOP1600')pd.set_option('display.max_columns', None)  # 显示所有列pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值# select needed datasetsselected_datasets_df = datasets_df[    (datasets_df["delay"] == delay) &    (datasets_df["coverage"] > 0.5) & (datasets_df["coverage"] <= 1) &    (datasets_df["fieldCount"] > 0) & (datasets_df["fieldCount"] < 2000) &    (datasets_df["region"] == region) &    (datasets_df["universe"] == universe) &    (datasets_df["userCount"] > 0) & (datasets_df["userCount"] < 100) &    (datasets_df["valueScore"] > 1) & (datasets_df["valueScore"] < 10) &    (datasets_df["category"].apply(lambda x: x.get("id") if isinstance(x, dict) else None) == "analyst")    #(datasets_df["category"]  'analyst')    #datasets_df["name"].str.contains('news', case=False) &    #((datasets_df["category"] == 'analyst') | (datasets_df["category"] == 'analyst'))].sort_values(by=['valueScore'], ascending=False)print(selected_datasets_df)
```

- 批量预处理数据，生成数据大表，这里的作用等价于老师在论坛写的推荐数据

```
reset_fleg = 0for dataset_id in selected_datasets_df['id']:    df1 = get_datafields(s, dataset_id = dataset_id, region= region, universe=universe, delay=delay)    pd.set_option('display.max_columns', None)  # 显示所有列    pd.set_option('display.width', 1000)  # 设置输出宽度，根据你的屏幕调整这个值    df2 = df1[df1['type'] == 'MATRIX']    df3 = df1[df1['type'] == 'VECTOR']    #df4 = df1[df1['type'] == 'GROUP']    try:        print(len(data))        if reset_fleg == 1:            data = []      except NameError:        data = []    if len(df2)>0:        matrix_fields_1 = process_datafields(df1, "matrix")        data.extend(matrix_fields_1)    if len(df3)>0:        vector_fields_1 = process_datafields(df1, "vector")           data.extend(vector_fields_1)    print(dataset_id,'执行完毕')print(len(data))
```

剩下的工作就是套在不同的模版中了，祝大家早日达到MASTER!

---

### 帖子 #41: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **讨论数**: 37

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

---

### 帖子 #42: print(pools[0])
- **主帖链接**: https://support.worldquantbrain.com[L2] 多线程遍历回测super alpha代码优化_31527668843671.md
- **讨论数**: 21

def multi_simulate2_sa(alpha_pools, neut, region, universe, start):
    global s

s = login()

brain_api_url = ' [[链接已屏蔽]) '

limit_of_concurrent_simulations = len(alpha_pools[0])

alpha_pools_2 = [multi_alphas for pool in alpha_pools for multi_alphas in pool]
    # print(alpha_pools_2)

end = len(alpha_pools_2)

print(f'length:{len(alpha_pools_2)}, start:{start}')
    counter: int = start
    lock = threading.Lock()

def sim_task(pools=alpha_pools_2, region=region, universe=universe, neut=neut):
        while True:
            global s
            lock.acquire()
            nonlocal counter
            if counter > end - 1:
                lock.release()
                break
            if (counter - start) % 250 == 0:  # re-login after every 60 multi_sims
                s = login()
            local_counter = counter
            counter += 1
            lock.release()
            task = pools[local_counter]
            sim_data_list = generate_sim_data_sa(task, region, universe, neut)
            sim_data=sim_data_list[0]
            try:
                simulation_response = s.post(' [[链接已屏蔽]) ', json=sim_data)
                simulation_progress_url = simulation_response.headers['Location']
                # simulation_progress_url = simulation_response.headers.get('location')
            except:
                print(" loc key error")
                sleep(600)
                s = login()

print(f"task {local_counter} post done")

try:
                while True:
                    simulation_progress = s.get(simulation_progress_url)
                    if simulation_progress.headers.get("Retry-After", 0) == 0:
                        break
                    # print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
                    sleep(float(simulation_progress.headers["Retry-After"]))

status = simulation_progress.json().get("status", 0)
                if status != "COMPLETE":
                    print(f"Not complete : {simulation_progress_url}")

"""
                #alpha_id = simulation_progress.json()["alpha"]
                children = simulation_progress.json().get("children", 0)
                children_list = []
                for child in children:
                    child_progress = s.get(brain_api_url + "/simulations/" + child)
                    alpha_id = child_progress.json()["alpha"]

set_alpha_properties(s,
                            alpha_id,
                            name = "%s"%name,
                            color = None,)
                """
            except KeyError:
                print(f"look into: {simulation_progress_url}")
            except:
                print("other")

print(f"task {local_counter} simulate done")

t = []
    for i in range(limit_of_concurrent_simulations):
        t.append(threading.Thread(target=sim_task))
        t[i].start()

for i in range(limit_of_concurrent_simulations):
        t[i].join()

print("Simulate done")

def generate_sim_data_sa(alpha_list, region, uni, neut):
    sim_data_list = []
    for selection_exp, combo_exp in alpha_list:
        # print(selection_exp)
        # print(combo_exp)
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
            'combo': combo_exp}

sim_data_list.append(simulation_data)
    return sim_data_list

```
import threading
```

```
from machine_lib import *
```

selection_exp=['turnover<0.15']
combo_exp=['stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr);maxCorr = reduce_max(ic); 1 - maxCorr']
sa_list=[(i,j) for i in selection_exp for j in combo_exp]
print(len(sa_list))
print(sa_list[0])

pools = load_task_pool(sa_list, 1, 3)
# print(pools[0])
region_dict = {"usa": ("USA", ["TOP3000", "TOP1000", "TOP500", "TOP200"]),
               "asi": ("ASI", ["MINVOL1M"]),
               "eur": ("EUR", ["TOP2500","TOP1200", "TOP800", "TOP400"]),
               "glb": ("GLB", ["TOP3000", 'MINVOL1M']),
               "hkg": ("HKG", ["TOP800", "TOP500"]),
               "twn": ("TWN", ["TOP500", "TOP100"]),
               "jpn": ("JPN", ["TOP1600", "TOP1200"]),
               "kor": ("KOR", ["TOP600"]),
               "chn": ("CHN", ["TOP2000U"]),
               "amr": ("AMR", ["TOP600"])}

norm_opt=["INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"]
risk_opt=["FAST","SLOW","SLOW_AND_FAST"]
r1=['STATISTICAL']
cr=["CROWDING"]
co=["COUNTRY"]
no=["NONE"]
neut_opt={"USA":norm_opt+cr+risk_opt+r1,
          "GLB":co+r1,
          "EUR":co+cr+norm_opt+risk_opt+r1,
"ASI":co+cr+norm_opt+risk_opt+no,
"CHN":norm_opt+cr+risk_opt+r1,
          "KOR":norm_opt,
          "TWN":norm_opt,
          "HKG":norm_opt,
          "JPN":norm_opt,
          "AMR": ["COUNTRY"]+norm_opt,
          }

regi = ['usa']
for k in regi:
    for i in region_dict[k][1][:1]:
        print(i)
        for j in neut_opt[k.upper()]:
            print(j, region_dict[k][0])
            multi_simulate2_sa(pools, j, region_dict[k][0], i, 0)

最后说明，该代码的多线程部分是由一位大佬编写，用于回测regler alpha，曾经分享在学习群，我在此基础改编成用于回测super alpha。如果本人看到此贴请留下相关链接，后续加上相关信息。

---

### 帖子 #43: 选择最先出现的位置  if backfill_index != -1 and backfill_index != -1:            cut_index = min(backfill_index, backfill_index)
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

### 帖子 #44: 成为顾问五个月，分享vf保持0.9+的经验经验分享
- **主帖链接**: [L2] 成为顾问五个月分享vf保持09的经验经验分享.md
- **讨论数**: 32

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

---

### 帖子 #45: 成为顾问五个月，分享vf保持0.9+的经验经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 成为顾问五个月分享vf保持09的经验经验分享_34938580496023.md
- **讨论数**: 32

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

---

### 帖子 #46: 曲折的Value Factor之路：0.2-0.4-0.8-0.5-0.94-0.99, 得出的一点点心得经验分享
- **主帖链接**: [L2] 曲折的Value Factor之路02-04-08-05-094-099 得出的一点点心得经验分享.md
- **讨论数**: 7

去年10月成为的顾问，应该也算是一名老顾问了。vf波动很大，前期基本都是0.2左右，ppac比赛后开始回升，但比赛结束后，又被打入谷底，最近两次更新浮出水面：0.94，0.99.写一点自己的心得，供大家参考。

声明：论坛里关于Value Factor的讨论很多，不要把这些讨论直接照搬，这些都是大家站在自己的角度总结的经验。如果一个顾问的VF常年保持在0.9以上，我觉得是值得参考模仿的。但大多数帖子只是停留在0.9一次而得出的经验，可能不够全面。包括这篇帖子，也是一点心得分享，请勿直接照搬。这个帖子我会尽力在每次VF更新的时候都总结一下，希望能给大家一点参考。

最近几个月我做了那些改变：

1. 持续的提交Super Alpha；

2. 对Margin的要求提高到10以上；

3. 多点塔提高多样性；

4. 基本都是ATOM。

5. 经常交不上ra，那就不交。

中文顾问论坛是一个宝库，推荐新顾问们一定要多看看里面的帖子，常看常新。回测提交并没有一个万能钥匙，但一定有一个固定不变的方法论，结合自己的情况，不断成长。

长期、短期永远有一个取舍，收入是短期的，学习到知识和经验，才是自己未来的财富。不要小看量化交易这四个字的含金量。

---

### 帖子 #47: 曲折的Value Factor之路：0.2-0.4-0.8-0.5-0.94-0.99, 得出的一点点心得经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 曲折的Value Factor之路02-04-08-05-094-099 得出的一点点心得经验分享_35888667819159.md
- **讨论数**: 7

去年10月成为的顾问，应该也算是一名老顾问了。vf波动很大，前期基本都是0.2左右，ppac比赛后开始回升，但比赛结束后，又被打入谷底，最近两次更新浮出水面：0.94，0.99.写一点自己的心得，供大家参考。

声明：论坛里关于Value Factor的讨论很多，不要把这些讨论直接照搬，这些都是大家站在自己的角度总结的经验。如果一个顾问的VF常年保持在0.9以上，我觉得是值得参考模仿的。但大多数帖子只是停留在0.9一次而得出的经验，可能不够全面。包括这篇帖子，也是一点心得分享，请勿直接照搬。这个帖子我会尽力在每次VF更新的时候都总结一下，希望能给大家一点参考。

最近几个月我做了那些改变：

1. 持续的提交Super Alpha；

2. 对Margin的要求提高到10以上；

3. 多点塔提高多样性；

4. 基本都是ATOM。

5. 经常交不上ra，那就不交。

中文顾问论坛是一个宝库，推荐新顾问们一定要多看看里面的帖子，常看常新。回测提交并没有一个万能钥匙，但一定有一个固定不变的方法论，结合自己的情况，不断成长。

长期、短期永远有一个取舍，收入是短期的，学习到知识和经验，才是自己未来的财富。不要小看量化交易这四个字的含金量。

---

### 帖子 #48: 1. 下载/增量更新download_data(session, flag_increment=True)Self-correlation 0.7691 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.这是代码计算结果：alpha_id:  XgQqkZda self_corr:  0.7691116930719178alpha_id = "XgQqkZda"Self-correlation is 0.4589, which is above cutoff of 0.7, or Sharpe is better by 10.0% or more.这是代码计算结果：alpha_id:  zq6wpknV self_corr:  0.48371278563080605alpha_id = "zq6wpknV"加载数据os_alpha_ids, os_alpha_rets = load_data(tag='SelfCorr')self_corr = calc_self_corr(    session,    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)print("alpha_id: ", alpha_id, "self_corr: ", self_corr)
- **主帖链接**: https://support.worldquantbrain.com[L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md
- **讨论数**: 64

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

### 帖子 #49: 获取数据，修改日期范围和alpha数量
- **主帖链接**: [L2] 来时路运气与努力交织的结果 vf 从 033 到 098 的成长附代码经验分享.md
- **讨论数**: 12

这次 vf 更新至 0.98，着实出乎我的意料。原本预期在 0.7-0.85 之间，能有这样的突破，运气成分确实占了不小比重 —— 毕竟至今我仍未完全摸清直接影响 vf 的核心指标。这里必须感谢论坛的前辈们，在 "坐牢期" 按他们分享的方法提交后，竟收获了这样的意外之喜。

虽不敢说能给大家太多成熟建议，但还是想把这几个月的实践总结出来，希望能提供一些参考：

1. **紧跟官方节奏提交。** 在 "坐牢" 阶段，官方强调多交 atom，我便集中精力提交这类内容，非 atom 的一律不碰，确保方向与平台引导一致。
2. **保证提交数量，稳定输出。** 记得很早前有老师说过："宁可每天交 4 个合格的 RA，也不要每天只交 1 个优质的 RA。" 我践行这一点，每天尽量保证 "3+1"，最好能做到 "4+1"，保持稳定的活跃度。
3. **重视 SA 质量，助力提高vf 。** 能快速提升，SA 的贡献功不可没。我始终保证至少有一个数据在 5 以上（Sharp/Fitness/PC），也曾有过几次提交 3 个 5 的 SA 的经历，优质内容的积累或许是关键。 这里补充一点，SA需要你提交更多的RA来组合，多交RA很重要。
4. **多区域覆盖，借势活动。** 由于同时在冲塔，我几乎覆盖了所有可提交的区域。结合官方的双倍活动，既避免了提交区域的单一性，也提高了投入产出比。

前辈们总结的提升 vf 的方法，大致可归为两类：

**垂直深耕，聚焦质量：** 追求 Sharp 大于 2、Fitness1.5 以上，同时保证 pnl 曲线美观，兼顾低 turnover、低 Drawdown、高 Return 与高 margin。

**广度拓展，多维布局：** 多冲塔 + 低sc和pc + 坚持 ATOM，在保证数量的基础上，确保其他数据不过于拉垮（比如 margin 最好维持在 10% 以上）。

最后附上这几个月的部分数据，供大家参考。也恳请看到的前辈们不吝指导 —— 从数据趋势看，我预判下个月的 vf 可能会有所回落。股市里常说："凭运气赚的钱，终会凭实力亏回去。" 所以搞懂底层逻辑才是根本。

（图片传不上.jpeg ）

但有一句话始终没错：一分耕耘，一分收获。即便当下有运气加持，但若没有前期的努力铺垫，也难有这份回报。

文末附上我 **基于官方代码** 修改的工具，能查询当前各项数据的平均值。建议大家每周跑一次，及时关注指标波动，针对性调整。共勉！

> from datetime import datetime
> from machine_lib import *
> s = login()
> def get_submit_alphas(s, start_date, end_date, alpha_num):
> output = {
> "prodCorrelation": [],
> "sharpe": [],
> "turnover": [],
> "fitness": [],
> "returns": [],
> "drawdown": [],
> "margin": [],
> "pnl": []
> }
> for i in range(0, alpha_num, 100):
> # 构造查询url
> url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \
> + "&status!=UNSUBMITTED%1FIS_FAIL&dateSubmitted%3E=" + start_date  \
> + "T00:00:00-04:00&dateSubmitted%3C" + end_date \
> + "T00:00:00-04:00&order=-is.sharpe&hidden=false&type!=SUPER"
> urls = [url_e]
> for url in urls:
> response = s.get(url)
> try:
> alpha_list = response.json()["results"]
> for alpha in alpha_list:
> output["prodCorrelation"].append(alpha["is"]["prodCorrelation"])
> output["sharpe"].append(alpha["is"]["sharpe"])
> output["turnover"].append(alpha["is"]["turnover"])
> output["fitness"].append(alpha["is"]["fitness"])
> output["returns"].append(alpha["is"]["returns"])
> output["drawdown"].append(alpha["is"]["drawdown"])
> output["margin"].append(alpha["is"]["margin"])
> output["pnl"].append(alpha["is"]["pnl"])
> return output
> except Exception as e:
> print(f"当前异常为{e}")
> resp = s.get(' [[链接已屏蔽]) ')
> if resp.status_code != 200:
> print(f"resp 返回值{resp.status_code}")
> return output
> # 获取数据，修改日期范围和alpha数量
> alpha_metrics = get_submit_alphas(s, "2025-10-01", "2025-11-01", 200)
> # 计算平均值的函数
> def calculate_average(metric_list):
> if len(metric_list) > 0:
> return sum(metric_list) / len(metric_list)
> return 0
> # 分别计算各项指标的平均值
> average_prod_corr = calculate_average(alpha_metrics["prodCorrelation"])
> average_sharpe = calculate_average(alpha_metrics["sharpe"])
> average_turnover = calculate_average(alpha_metrics["turnover"])
> average_fitness = calculate_average(alpha_metrics["fitness"])
> average_returns = calculate_average(alpha_metrics["returns"])
> average_drawdown = calculate_average(alpha_metrics["drawdown"])
> average_margin = calculate_average(alpha_metrics["margin"])
> average_pnl = calculate_average(alpha_metrics["pnl"])  # 计算 Pnl 的平均值
> # 打印结果
> print(f"10月份共提交了{len(alpha_metrics['prodCorrelation'])}个普通alpha")
> print(f"Prod Corr 平均值: {average_prod_corr:.4f}")
> print(f"Sharpe 平均值: {average_sharpe:.4f}")
> print(f"Turnover 平均值: {average_turnover:.4f}")
> print(f"Fitness 平均值: {average_fitness:.4f}")
> print(f"Returns 平均值: {average_returns:.4f}")
> print(f"Drawdown 平均值: {average_drawdown:.4f}")
> print(f"Margin 平均值: {average_margin:.4f}")
> print(f"Pnl 平均值: {average_pnl:.4f}")

---

### 帖子 #50: 获取数据，修改日期范围和alpha数量
- **主帖链接**: https://support.worldquantbrain.com[L2] 来时路运气与努力交织的结果 vf 从 033 到 098 的成长附代码经验分享_35877688682391.md
- **讨论数**: 12

这次 vf 更新至 0.98，着实出乎我的意料。原本预期在 0.7-0.85 之间，能有这样的突破，运气成分确实占了不小比重 —— 毕竟至今我仍未完全摸清直接影响 vf 的核心指标。这里必须感谢论坛的前辈们，在 "坐牢期" 按他们分享的方法提交后，竟收获了这样的意外之喜。

虽不敢说能给大家太多成熟建议，但还是想把这几个月的实践总结出来，希望能提供一些参考：

1. **紧跟官方节奏提交。** 在 "坐牢" 阶段，官方强调多交 atom，我便集中精力提交这类内容，非 atom 的一律不碰，确保方向与平台引导一致。
2. **保证提交数量，稳定输出。** 记得很早前有老师说过："宁可每天交 4 个合格的 RA，也不要每天只交 1 个优质的 RA。" 我践行这一点，每天尽量保证 "3+1"，最好能做到 "4+1"，保持稳定的活跃度。
3. **重视 SA 质量，助力提高vf 。** 能快速提升，SA 的贡献功不可没。我始终保证至少有一个数据在 5 以上（Sharp/Fitness/PC），也曾有过几次提交 3 个 5 的 SA 的经历，优质内容的积累或许是关键。 这里补充一点，SA需要你提交更多的RA来组合，多交RA很重要。
4. **多区域覆盖，借势活动。** 由于同时在冲塔，我几乎覆盖了所有可提交的区域。结合官方的双倍活动，既避免了提交区域的单一性，也提高了投入产出比。

前辈们总结的提升 vf 的方法，大致可归为两类：

**垂直深耕，聚焦质量：** 追求 Sharp 大于 2、Fitness1.5 以上，同时保证 pnl 曲线美观，兼顾低 turnover、低 Drawdown、高 Return 与高 margin。

**广度拓展，多维布局：** 多冲塔 + 低sc和pc + 坚持 ATOM，在保证数量的基础上，确保其他数据不过于拉垮（比如 margin 最好维持在 10% 以上）。

最后附上这几个月的部分数据，供大家参考。也恳请看到的前辈们不吝指导 —— 从数据趋势看，我预判下个月的 vf 可能会有所回落。股市里常说："凭运气赚的钱，终会凭实力亏回去。" 所以搞懂底层逻辑才是根本。

（图片传不上.jpeg ）

但有一句话始终没错：一分耕耘，一分收获。即便当下有运气加持，但若没有前期的努力铺垫，也难有这份回报。

文末附上我 **基于官方代码** 修改的工具，能查询当前各项数据的平均值。建议大家每周跑一次，及时关注指标波动，针对性调整。共勉！

> from datetime import datetime
> from machine_lib import *
> s = login()
> def get_submit_alphas(s, start_date, end_date, alpha_num):
> output = {
> "prodCorrelation": [],
> "sharpe": [],
> "turnover": [],
> "fitness": [],
> "returns": [],
> "drawdown": [],
> "margin": [],
> "pnl": []
> }
> for i in range(0, alpha_num, 100):
> # 构造查询url
> url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \
> + "&status!=UNSUBMITTED%1FIS_FAIL&dateSubmitted%3E=" + start_date  \
> + "T00:00:00-04:00&dateSubmitted%3C" + end_date \
> + "T00:00:00-04:00&order=-is.sharpe&hidden=false&type!=SUPER"
> urls = [url_e]
> for url in urls:
> response = s.get(url)
> try:
> alpha_list = response.json()["results"]
> for alpha in alpha_list:
> output["prodCorrelation"].append(alpha["is"]["prodCorrelation"])
> output["sharpe"].append(alpha["is"]["sharpe"])
> output["turnover"].append(alpha["is"]["turnover"])
> output["fitness"].append(alpha["is"]["fitness"])
> output["returns"].append(alpha["is"]["returns"])
> output["drawdown"].append(alpha["is"]["drawdown"])
> output["margin"].append(alpha["is"]["margin"])
> output["pnl"].append(alpha["is"]["pnl"])
> return output
> except Exception as e:
> print(f"当前异常为{e}")
> resp = s.get(' [[链接已屏蔽]) ')
> if resp.status_code != 200:
> print(f"resp 返回值{resp.status_code}")
> return output
> # 获取数据，修改日期范围和alpha数量
> alpha_metrics = get_submit_alphas(s, "2025-10-01", "2025-11-01", 200)
> # 计算平均值的函数
> def calculate_average(metric_list):
> if len(metric_list) > 0:
> return sum(metric_list) / len(metric_list)
> return 0
> # 分别计算各项指标的平均值
> average_prod_corr = calculate_average(alpha_metrics["prodCorrelation"])
> average_sharpe = calculate_average(alpha_metrics["sharpe"])
> average_turnover = calculate_average(alpha_metrics["turnover"])
> average_fitness = calculate_average(alpha_metrics["fitness"])
> average_returns = calculate_average(alpha_metrics["returns"])
> average_drawdown = calculate_average(alpha_metrics["drawdown"])
> average_margin = calculate_average(alpha_metrics["margin"])
> average_pnl = calculate_average(alpha_metrics["pnl"])  # 计算 Pnl 的平均值
> # 打印结果
> print(f"10月份共提交了{len(alpha_metrics['prodCorrelation'])}个普通alpha")
> print(f"Prod Corr 平均值: {average_prod_corr:.4f}")
> print(f"Sharpe 平均值: {average_sharpe:.4f}")
> print(f"Turnover 平均值: {average_turnover:.4f}")
> print(f"Fitness 平均值: {average_fitness:.4f}")
> print(f"Returns 平均值: {average_returns:.4f}")
> print(f"Drawdown 平均值: {average_drawdown:.4f}")
> print(f"Margin 平均值: {average_margin:.4f}")
> print(f"Pnl 平均值: {average_pnl:.4f}")

---

### 帖子 #51: 理解顾问最重要的指标Value Factor! 分享不同数值对应的预计每日收入
- **主帖链接**: [L2] 理解顾问最重要的指标Value Factor 分享不同数值对应的预计每日收入.md
- **讨论数**: 40

```
冲击Grand Master! 帮助大家树立信息维护好自己的value factor！感谢大家点击右侧VOTE点赞或留言互动！
```

**终于每日Base Payment从1.X USD 到了现在的20USD，经验分享出来更更多的同学**

**
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 15
> 10
**

**1. 什么是Value Factor？**

Value Factor 衡量的是最近提交的Alpha对组合Alpha表现的影响，同时考虑三个特定因素：(a) Alpha的个体表现，(b) 最近Alpha提交的多样性，以及 (c) 提交的独特性，即与您过去的提交以及其他顾问提交的比较。

换句话说，Value Factor 是在适用的日历季度中最近提交的Alpha组合的OS（样本外）表现。

Value Factor 是基础支付和季度支付的组成部分。 **范围是0到1。初始值是0.5，可以在consultant 排行榜上面查到**

**2. 什么时候开始更新Value Factor?**

目前来看每个月会更新一次，11月1日更新的是8月开始交alpha的，12月1日今天应该是更新了9月开始交alpha的，以此类推。（个人观察，如果理解错误请官方指正），每次更新会在右上角Announcement处看到。通查你的base payment的变更会比通知来的更早

**3. 提升Value Factor 都需要注意什么？**

**首先，要有足够多的数量，** 上课老师有讲过统计学中的中心极限定理会保证体现出你的真实水平，但这要建立在足够多的alpha上，个人经验最好保持近乎每个月在50个左右，不少于每天都提交。

**其次，最直观的就是看那条PnL的曲线，** 当你进入到一个阶段后已经不再担心找到可以提交的alpha，就要开始选取好的alpha 来交，以下是典型的几个我认为要三思而后行的

a. 先来个好看的，基本上是比较平稳，覆盖的时间足够长。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,50OK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,000K
> 2,50OK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> ANVI


b. 大家经常可能会遇到PnL的覆盖时间从2018年开始的，但线还算平稳，尤其是最近一两年还不错，原理上自己也能说的通，这种不是说完全不能交，但是需要自己权衡一下。 **之后我也会找时间分享一下如何批量识别这样alpha的代码，求点赞！**


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,5OOK
> 1,00OK
> SOOK
> 03/14/2018
> Pnl: 120.30K
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> {MMM
> NAM


c. 数据时间短，图形很乱，最近一两年走平，甚至是负数的。这种如果不缺alpha的话个人就不建议提交了。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,5OOK
> I
> 6,00OK
> 5,5OOK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,5OOK
> 07/31/2018
> Pnl: 3,319.60K
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Mp}


**第三，多样性。** 追求多pyramid，这个和genius program的要求也是相辅相成的，也可以理解为BRAIN官方想要奖励和推荐的行为。这里就不建议大家在一个地方交太久，即使有多余的可以留一下等下个月再交（当然也有可能被别人交了，自己权衡下）。尤其如果遇到了oversued的warning以后。

**第四，低相关性。** 这个在很多前辈大佬上分享中也多次提交过了，我基本主要提交的都控制在PROD correlation在0.6以内的，越低越好。你会发现多去探索新的pyramid，会有更高的theme加成，也会更容易有低相关性。

第五，使用performance comparison 功能，关注sharp，fitness 和 margin 提交前后的变化

**3. 如果Value Factor 已经低了怎么办？**

不要摆烂不交了！保持提交，但不要交太多！

这里的建议是每天提交1个alpha，因为交多了也不到1.5USD。但要保证有提交，这样下个月的时候才有可能被拉回来

**4. 不同的value factor对应的base payment可能在什么范围？**

**免责声明：以下仅仅是个人经验，非官方标准**

以提交2个alpha，中等质量为例

Value factor 0.3    daily  1.3 USD

Value factor 0.5    daily 1.5-3 USD

Value factor 0.7    daily 6-10 USD

Value factor 0.8+  daily 15+ USD

Quarterly Payment 还没有太多的经验，后续有更新了再来补充

祝大家都能实现第二收入自由！ 如果觉得有用，记得vote点赞哈

---

### 帖子 #52: 理解顾问最重要的指标Value Factor! 分享不同数值对应的预计每日收入
- **主帖链接**: https://support.worldquantbrain.com[L2] 理解顾问最重要的指标Value Factor 分享不同数值对应的预计每日收入_28199144447255.md
- **讨论数**: 40

```
冲击Grand Master! 帮助大家树立信息维护好自己的value factor！感谢大家点击右侧VOTE点赞或留言互动！
```

**终于每日Base Payment从1.X USD 到了现在的20USD，经验分享出来更更多的同学**

**
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 15
> 10
**

**1. 什么是Value Factor？**

Value Factor 衡量的是最近提交的Alpha对组合Alpha表现的影响，同时考虑三个特定因素：(a) Alpha的个体表现，(b) 最近Alpha提交的多样性，以及 (c) 提交的独特性，即与您过去的提交以及其他顾问提交的比较。

换句话说，Value Factor 是在适用的日历季度中最近提交的Alpha组合的OS（样本外）表现。

Value Factor 是基础支付和季度支付的组成部分。 **范围是0到1。初始值是0.5，可以在consultant 排行榜上面查到**

**2. 什么时候开始更新Value Factor?**

目前来看每个月会更新一次，11月1日更新的是8月开始交alpha的，12月1日今天应该是更新了9月开始交alpha的，以此类推。（个人观察，如果理解错误请官方指正），每次更新会在右上角Announcement处看到。通查你的base payment的变更会比通知来的更早

**3. 提升Value Factor 都需要注意什么？**

**首先，要有足够多的数量，** 上课老师有讲过统计学中的中心极限定理会保证体现出你的真实水平，但这要建立在足够多的alpha上，个人经验最好保持近乎每个月在50个左右，不少于每天都提交。

**其次，最直观的就是看那条PnL的曲线，** 当你进入到一个阶段后已经不再担心找到可以提交的alpha，就要开始选取好的alpha 来交，以下是典型的几个我认为要三思而后行的

a. 先来个好看的，基本上是比较平稳，覆盖的时间足够长。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,50OK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,000K
> 2,50OK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> ANVI


b. 大家经常可能会遇到PnL的覆盖时间从2018年开始的，但线还算平稳，尤其是最近一两年还不错，原理上自己也能说的通，这种不是说完全不能交，但是需要自己权衡一下。 **之后我也会找时间分享一下如何批量识别这样alpha的代码，求点赞！**


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,5OOK
> 1,00OK
> SOOK
> 03/14/2018
> Pnl: 120.30K
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> {MMM
> NAM


c. 数据时间短，图形很乱，最近一两年走平，甚至是负数的。这种如果不缺alpha的话个人就不建议提交了。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,5OOK
> I
> 6,00OK
> 5,5OOK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,5OOK
> 07/31/2018
> Pnl: 3,319.60K
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Mp}


**第三，多样性。** 追求多pyramid，这个和genius program的要求也是相辅相成的，也可以理解为BRAIN官方想要奖励和推荐的行为。这里就不建议大家在一个地方交太久，即使有多余的可以留一下等下个月再交（当然也有可能被别人交了，自己权衡下）。尤其如果遇到了oversued的warning以后。

**第四，低相关性。** 这个在很多前辈大佬上分享中也多次提交过了，我基本主要提交的都控制在PROD correlation在0.6以内的，越低越好。你会发现多去探索新的pyramid，会有更高的theme加成，也会更容易有低相关性。

第五，使用performance comparison 功能，关注sharp，fitness 和 margin 提交前后的变化

**3. 如果Value Factor 已经低了怎么办？**

不要摆烂不交了！保持提交，但不要交太多！

这里的建议是每天提交1个alpha，因为交多了也不到1.5USD。但要保证有提交，这样下个月的时候才有可能被拉回来

**4. 不同的value factor对应的base payment可能在什么范围？**

**免责声明：以下仅仅是个人经验，非官方标准**

以提交2个alpha，中等质量为例

Value factor 0.3    daily  1.3 USD

Value factor 0.5    daily 1.5-3 USD

Value factor 0.7    daily 6-10 USD

Value factor 0.8+  daily 15+ USD

Quarterly Payment 还没有太多的经验，后续有更新了再来补充

祝大家都能实现第二收入自由！ 如果觉得有用，记得vote点赞哈

---

### 帖子 #53: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 组sa时如何选取高质量因子经验分享_32034293019671.md
- **讨论数**: 24

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

---

### 帖子 #54: 经验分享｜PPAC全球第三名，回馈社区经验分享
- **主帖链接**: [L2] 经验分享PPAC全球第三名回馈社区经验分享.md
- **讨论数**: 36

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

---

### 帖子 #55: 给新手跑region和dataset的小建议
- **主帖链接**: https://support.worldquantbrain.com[L2] 给新手跑region和dataset的小建议_28467103126679.md
- **讨论数**: 8

我是一个 ***10月25日*** 才加入顾问计划的新人，经过非常非常多的尝试，每天花费了大量时间后， ***现在因子交了167个，金字塔完成了48个。*** 

前期新人跑数据挖掘遇到的大问题就是， **region** 的选择和 **dataset** 的选择，因为每个类型的数据集和每个地区的难度都是不一样的，所以前期新人更适合选一些简单的region或者dataset。

接下来我将分享一下我个人的一些心得体会，希望对新人有所帮助。

## 首先是region的选择。

region一共有10个，分别是：USA, GLB, EUR, ASI, CHN, KOR, TWN, JPN, HKG, AMR。

```
REGION_LIST = ['USA', 'GLB', 'EUR', 'ASI', 'CHN', 'KOR', 'TWN', 'JPN', 'HKG', 'AMR']
```

他们的简单程度我认为是

ASI > USA > TWN > EUR > GLB > JPN = CHN = HKG > KOR > AMR （都是delay 1的）

## 然后是category的选择

category一共有16个，分别是：pv, fundamental, analyst, socialmedia, news, option, model, shortinterest, institutions, other, sentiment, insiders, earnings, macro, imbalance, risk。

```
DATASET_CATEGORY_LIST = ['pv', 'fundamental', 'analyst', 'socialmedia', 'news', 'option', 'model', 'shortinterest', 'institutions', 'other', 'sentiment', 'insiders', 'earnings', 'macro', 'imbalance', 'risk']
```

他们的简单程度我认为是

model > pv > analyst = fundamental > other > option > institutions = news = insiders = sentiment > macro = risk = shortinterest = socialmedia > earnings > imbalance （都是delay 1的）

另外不建议新手去做delay 0的，我跑了近50万个都没有一个可以交的。

---

### 帖子 #56: 零基础考研失败应届生的一点经验经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 零基础考研失败应届生的一点经验经验分享_30694634496663.md
- **讨论数**: 4

由于长期备考研究生，导致脑袋里除了课本知识基本什么都没有了，仅剩的一点代码基础也都忘记的差不多了，于是，只能从头开始学习，由于没有工作，因此可以把时间都投入到学习中。

首先，我先用ai搜索了量化交易的相关信息，知道了要学习哪些相关知识，然后在小破站学习了python数据分析，再结合社区论坛和用户课程大概了解了brain平台的运行流程以及如何构建alpha，也是很轻松的成为了顾问，学习了顾问培训的 课程之后，成功的提交了第一个顾问alpha，给了我很大信心，后来的学习过程中，连续看了三次不同的part1培训课程，每一次都有很大的收获，目前看完part2的顾问培训，还没有把知识完全消化。

我的建议是一定要把用户四节课和顾问的两节课琢磨透，不会的问ai，然后代码和金融基础薄弱的话，可以到小破站学习相关课程，除此之外，我还每天坚持刷力扣，提高自己对代码的理解，论坛每天没事的时候都可以逛逛，会有很多意想不到的收获。

我是成为顾问之后才开始认真投入学习的，从2月26号开始，截至目前总共提交了38个alpha,很荣幸获得了进入研究小组的资格，虽然在学习过程中会遇到各种困难，但是坚持下去总是能克服的，在这里感谢一下顾问小组里各位大佬和同学的帮助。

目前提交的alpha质量并不高，其中有8个质量不过关，其余的base payment过关了，但是不知道是不是受之前eur活动的影响，因此最近三天都没有提交alpha，同时建议各位新人一定要以质量为主。 
> [!NOTE] [图片 OCR 识别内容]
> Total Payment (AII Time): 0S$28.23
> Base Payment
> Submitted Alphas
> 03/02/2025
> Base Payment: 1.82
> Total:
> 1.82
> <@ <@
> s
> sN
> 23
> <@
> s
> 1
> ?"
> 2
> 3'
> D
> A'
> ^^'
> A
> "
> ^A
> :
> 0'
> 2:
> 1
> ^ &
> ^8.
> ^^'
> A
> '
> ^公
> ^'
> ^@"
> Displayed Period
> 02/24/2025
> 03/16/2025
> 05528.23
> Displayed Period
> 02/23/2025
> 03/16/2025
> 38
> Yesterday
> 03/16/2025
> USS0.00
> Yesterday
> 03/16/2025
> Current period
> 03/01/2025
> 04/30/2025
> 05$23.33
> Current period
> 03/01/2025
> 04/30/2025
> 30
> Previous period
> 01/01/2025
> 02/28/2025
> US$4.90
> Previous period
> 01/01/2025
> 02/28/2025
> 15
> Year to date
> 02/17/2025
> 03/16/2025
> 05$28.23
> Yearto date
> 01/01/2025
> 03/16/2025
> 45
> Total
> 02/17/2025
> 03/16/2025
> 05$28.23
> Total
> 12/30/2024
> 03/16/2025
> 45
>  Mar
>  Mar
>  Mar
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> Mar
>  Mar
>  Mar
>  Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> Mar
>  Mar
>  Feb
>  Feb
>  Mar
> Mar
> Mar
> Feb
>  Feb
> Feb
> Feb
>  Mar
> Mar
> Mar
> Mar
> Mar
> 10。



> [!NOTE] [图片 OCR 识别内容]
> Current level: Gold
> Best level: Gold
> Current quarter end: March 31st, 2025
> GOLD
> Eligibility Criteria
> 2025-01,January 1st, 2025
> March 31st, 2025
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 38
> 82 more to Master
> 20
> 120
> 220
> Pyramids Completed
> 1
> 3 more to Expert
> 10
> 30
> Combined Alpha Performance


---

### 帖子 #57: 6. 总结
- **主帖链接**: [python Alpha 挑战赛] 从使用操作符到设计框架一次因子结构压缩与状态化研究实践经验分享.md
- **讨论数**: 7

# 1. Idea

自从 BRAIN 平台开放 Python Alpha 之后，论坛里出现了很多关于 Fast Expression 转 Python Alpha 的讨论。

但经过最近一段时间的研究，我发现：

Python Alpha 最有价值的地方，其实并不是把已有因子翻译成代码。

因为如果只是实现完全等价转换，那么最终得到的仍然是同一个 Alpha，只不过换了一种表达方式而已。

总部培训时也提到过类似观点：

> 单纯将平台表达式翻译成 Python Alpha，本身并没有太大的研究价值。

真正让我感兴趣的是几个问题：

- Python Alpha 能否帮助我们发现因子中的冗余结构？
- Python Alpha 能否重新审视已有 Alpha 的信息来源？
- Python Alpha 能否实现 Fast Expression 无法表达的新计算结构？

带着这些问题，我对一个已经通过测试的 Alpha 进行了拆解实验。

原始表达式如下：

signed_power(group_zscore(round_down(ts_decay_exp_window(floor(ts_mean(winsorize(plant_data,std=4),xxx)),xxx,factor=0.x),f=1),sector),2)

整个结构包含：

- winsorize
- ts_mean
- floor
- ts_decay_exp_window
- round_down
- group_zscore
- signed_power

共计 7 层操作符嵌套。

从 Fast Expression 的角度来看，这是一个非常典型的 Alpha 结构。

但问题是：

这 7 个操作符是否都在贡献有效信息？

还是其中部分操作符只是历史迭代过程中不断叠加出来的“装饰层”？

于是我决定利用 Python Alpha 对其进行逐层拆解。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
>  |t
> slened_pONET(Broup_TsCore(round_down ts_dacay_ep_ndow(floor(ts_Iean MInsorize(f
> RsrsDt S0:477
> TBIPEATP 436
> SIUAToN 52TTIN
> 1.6|
> 5.179
> +05
> 5.1190
> 4.5891
> 15.81930o
> Ohooot 
> s
> U
> 
> a
> om
> f
> Ieeh
> Ma To
> N Fe
> 4J!
> TU
> CUesr
> SU
> S
> [e
> Tl
> [e4
> [oeto
> t
>  Le Cen
> Tl Cene
> 
> 
> Clom Mlpha
> J5
> 2
> N Chart
> 2
> 318
> 1。
> ~JIOP
> Ivesability COnSTJICO
> ATCcateDJta
> Ju1+
> J5
> JJl
> Jn 1
> Jus
> Jeu
> JJ-
> Jonl
> J1
> Jn
> 』J
> J7
> J3
> Jn -
> J?1
> J1 2
> J2
> Jn
> JJl
> 1.52
> 099
> 4.5590
> 5.2196
> 14.943co
> [vesabilis
> Consle|Pl
> 匡 Correlation
> SCIrCoTITIOI
> Wum r
> LelsT +
> I5 Testing Status
> Pend
> LOWCT LOOICoTTCIton
> 
> L I
> 8 PASS
> LTCf mTaITCI
> 1C
> NN TTCPI
> WARNIING
> 0.5218
> 0.5042
> Inoncsalc UiLfr inzJ nacrs;Itr] Crccl Uil
> TJC
> VrTTF  TTSLrT
> KehTITOer TIOE
> 4
> Delay CONCL20
> TOON
> 一 =O
> TTUTTIeTTeLMsaTT0 290
> TCCOTC0
> CTFCTT
> CCTI
> m
> Theme CL HehTurnover Darasets Theme CJer
> TShwTTUTClercf2
> PCNOIIG


# 2. 实现

在 Python Alpha 中，我并没有直接复刻全部表达式。

而是把每一层逻辑拆开，观察其对最终结果的贡献。

研究过程中我发现一个有趣现象：

因子的主要信息实际上集中在以下链路中：

winsorize → ts_mean → floor → ts_decay_exp_window → round_down

而最外层的：

- group_zscore
- signed_power

对于最终 Sharpe 和 Fitness 的提升远低于预期。

换句话说：

原始表达式虽然包含 7 个操作符，但真正承担主要信息提取任务的只有前面几个核心模块。

因此最终 Python Alpha 保留了核心部分：

winsorize → ts_mean → floor → decay → round_down

并移除了部分贡献有限的后处理结构。

这里有一个有趣的现象。

如果只是简单把表达式封装进 Python Alpha，那么本质上仍然是在复刻已有逻辑。

研究价值其实并不高。

真正值得关注的是：

当我们开始拆解 Alpha 时，会发现哪些部分是真正提供信息的，哪些部分只是不断叠加出来的复杂度。

结果令人意外。

回测表现与原始表达式保持高度一致。

但整体复杂度显著下降。

从研究角度来看，这相当于完成了一次因子结构压缩（Factor Compression）。

过去我们习惯不断向 Alpha 外层叠加新的操作符。

而 Python Alpha 给了我们反向思考的机会：

- 哪些操作符是真正有价值的？
- 哪些操作符只是让表达式变得更长？
- 哪些部分是核心信号？
- 哪些部分只是后处理包装？


> [!NOTE] [图片 OCR 识别内容]
> 区 Openalpha datailsin newtab
> Code
> from brain.alphas mort apha
> iort nwpy as 叩
> iport numpy.typing
> npt
> SITUIatIOI
> Settings
> InsnueType
> Reglon
> Uoere
> Laneo
> Decy
> Uelay
> Truncaton
> Newuraliaon
> Pateurtaon
> Cookback
> Nax Trad
> Na Posiuon
> Cuil'
> TUFZUUJ
> D
> SlulisliLl
> Clone Alpha 
> IS Summary
> Pariod
> ASinz = Czta Set ~ pFs
> A Resular -ohs
> Fyrmidtems USAIDIIANALYST 12
> AEBTegate Data
> SMulre
> TuTlUVL
> FIomo
> Reluriy
> Cd
> Ua
> 1.54
> 5.6995
> 1.00
> 4.529
> 7.0496
> 16.24900
> Yea
> Chok
> TUIO
> Te
> Relr
> Dr
> Maroin
> Lmo Co
> Sor CUNt



> [!NOTE] [图片 OCR 识别内容]
> Steak 416 day
> f_vals[k]
> 叩. floor(mean_val)
> tsbufo 恶妥保(聂近 dO 步的 winsorize 纺采。月于计H下-个 ts_rean
> tsbufo
> Min_W[-d: ]
> tsbufI I妥保K聂近 dI 步的 floor(ts_wean) 纺呆。用于计M ts_decay_exp_hindon
> tsbufl
> Vals
> TeTIn
> tsbufo
> tsbutr
> ealpha(
> Jata=
> plant_data' ],
> ST0Te
> TaIE
> itsbufo"
> aJims
> "yi'
> extend"
> 叩.float32(I.nan)}
> name
> ntsbufl"
> "dims
> "ti'
> extend"
> m.float3z(Ipnan)}
> Jef alpha_func (data
> store)
> ntIurray[ m .float3z]:
> Ist
> Jata plant_data.shape[l]
> 1。暖启动初妗化 store.tsbufo 和 store.tsbufl
> i store.tsbufo is None
> store.tsbufI is None:
> tsbufo
> tsbufr
> Rrmup_buffers (data
> 180,228,
> inst)
> store.tsbufo
> tsbufo
> store.tsbufl
> tsbufl
> 2。为辰计M:  聂薪一天竹茯面效O Winsorize
> winsorize_Id(data.plant_data[-1]
> ^劲更新 tsbufo (FIFO) 井且计.y薪一天前
> floor(ts_wean)
> store.tsbufo[:-1]
> store.tsbufo[I:
> Capy()
> store.tsbufo[-1] =
> Mth np.errstate(invalid-'inore
> divide'inore' ):
> mea_ral
> np.nanmeanlstore.tsbufe, axis g
> T.floor(wean_val)
> 滚劲更新 tsbufl (FIFO) 井且计卑聂葑一天前 ts_decay_eXP_windo
> store.tsbufr[:-1]
> store.tsbufz [1:
> Capy()
> store.tsbufI[-1] =
> 十间辰计.:  荇颁赉>咨劲平均
> Mith np.errstate(invalid 'inore
> Jivide- 'inore
> ts_decay_exp_Mindou(store.tsbufl;
> 220
> I88
> 戛外层计奘:
> TOUIU
> dow(.
> f-1)
> 「oud_don(a, 1.8)
> 103
> Feturn
> rasbpe(mp.float32)


# 3. 一个更有趣的发现：Python Alpha 的价值并不在于“翻译”

随着研究继续深入，我逐渐意识到：

Python Alpha 最大的价值可能根本不在于表达式转换。

而在于：

## 计算自由（Computational Freedom）

Fast Expression 时代，我们所有研究都建立在已有操作符体系之上。

研究过程通常是：

```
研究 = 组合操作符
```

发现数据 → 选择操作符 → 拼接表达式 → 回测

整个研究流程都围绕已有工具展开。

而 Python Alpha 的出现带来了一个变化：

研究者开始能够自己设计计算过程。

过去：

如果平台没有某个操作符。

研究思路可能就无法实现。

现在：

我们可以直接实现自己的逻辑。

甚至可以设计属于自己的中间状态。

从某种意义上说：

Python Alpha 正在把研究者从“操作符使用者”变成“计算框架设计者”。

这是一种完全不同的研究范式。

# 4. 一个被忽略的能力：双缓存状态流水线（Dual Buffer Stateful Pipeline）

在整个实验过程中，我认为最容易被忽略的能力并不是操作符数量。

而是：

## 状态（State）

Fast Expression 本质上属于无状态计算框架。

每次计算都依赖于历史窗口重新扫描。

例如：

- ts_mean
- ts_std_dev
- ts_decay_exp_window

本质上都是：

读取历史窗口 → 计算 → 输出结果

然后进入下一天重新执行。

研究者更多是在调用已有操作符。

而不是管理计算过程本身。

但 Python Alpha 出现之后，情况开始发生变化。

通过 Store，我们第一次拥有了保存状态的能力。

在本文实现中，我设计了一个简单但有趣的双缓存状态流水线（Dual Buffer Stateful Pipeline）。

整体结构如下：

```
plant_data      ↓ winsorize      ↓ ┌─────────┐ │ tsbuf0  │ └─────────┘      ↓  ts_mean      ↓   floor      ↓ ┌─────────┐ │ tsbuf1  │ └─────────┘      ↓ ts_decay      ↓ round_down      ↓  Alpha
```

### 第一层缓存：tsbuf0

tsbuf0 保存最近 180 天的 winsorize 结果。

每个交易日到来时：

- 删除最旧数据
- 插入最新数据
- 保持窗口长度不变

这样后续计算 ts_mean 时，不需要重新构造完整历史序列。

tsbuf0 更像是一个：

**基础信号仓库（Raw Signal Buffer）**

### 第二层缓存：tsbuf1

tsbuf1 保存最近 220 天的 floor(ts_mean) 结果。

这一层已经不再是原始数据。

而是经过第一层处理后的中间状态。

因此：

tsbuf1 本质上是一个：

**特征状态仓库（Feature Buffer）**

### 为什么这很重要？

如果只看最终结果：

这个 Alpha 看起来只是：

winsorize → ts_mean → floor → decay → round_down

但从计算框架来看：

实际上已经变成：

```
数据层    ↓状态层    ↓特征层    ↓输出层
```

这是一种完全不同的研究思路。

过去：

研究 = 组合操作符

现在：

研究 = 设计数据流

### Python Alpha 带来的不仅是代码能力

更重要的是：

它允许研究者自行设计状态结构。

例如：

- 单缓存结构
- 双缓存结构
- 多级状态流水线
- 自适应状态更新机制

这些能力在 Fast Expression 中很难直接表达。

而在 Python Alpha 中却变得十分自然。

# 5. 为什么我认为这对 Genius 评级有意义

对于很多顾问来说，Genius 不仅是一套评级体系，也是长期研究能力的体现。

从目前公开规则来看：

- Operator Count
- Field Count
- Alpha 提交数量
- Tower Coverage
- Combine
- 六维指标

都会对最终评级产生影响。

因此很多顾问在研究过程中都会面临一个问题：

如何在保证 Alpha 质量的同时，优化整体结构。

本次实验给我的启发是：

Python Alpha 的价值并不仅仅在于减少操作符。

如果只是简单把 Fast Expression 翻译成 Python Alpha，那么意义并不大。

真正有价值的是：

利用 Python Alpha 实现 Fast Expression 难以表达的新结构。

例如本文使用的：

- 双缓存状态流水线
- Store 状态管理
- 多层特征缓存

这些能力本身并不存在于传统操作符体系之中。

从这个角度来看：

Python Alpha 不只是新的表达方式。

它提供了一种新的研究工具。

一方面可以帮助研究者重新审视 Alpha 结构；

另一方面也能够探索传统 Fast Expression 难以实现的新思路。

对于希望提升 Genius 综合竞争力的顾问来说，这种能力或许值得进一步研究。

# 6. 总结

这次实验最大的收获，并不是成功把 Fast Expression 转换成 Python Alpha。

而是让我意识到：

很多时候：

复杂并不等于有效。

长表达式也不一定意味着更多信息。

通过逐层拆解，我发现部分操作符对于最终结果的贡献远低于预期，而核心信号却能够在更简单的结构中被保留下来。

与此同时，Python Alpha 还提供了 Fast Expression 所不具备的能力：

- 自定义计算逻辑
- 状态管理
- 多层缓存结构
- 流水线式特征构建

在本文案例中，双缓存状态流水线（Dual Buffer Stateful Pipeline）只是一个简单尝试。

但它让我看到了另一种研究方向：

过去我们是在使用操作符。

未来我们或许可以开始设计计算框架。

过去我们是在组合 Alpha。

未来我们或许可以开始构建 Alpha Framework。

而这，也许才是 Python Alpha 真正有趣的地方。

---

### 帖子 #58: 6. 总结
- **主帖链接**: https://support.worldquantbrain.com[python Alpha 挑战赛] 从使用操作符到设计框架一次因子结构压缩与状态化研究实践经验分享_41047901195799.md
- **讨论数**: 7

# 1. Idea

自从 BRAIN 平台开放 Python Alpha 之后，论坛里出现了很多关于 Fast Expression 转 Python Alpha 的讨论。

但经过最近一段时间的研究，我发现：

Python Alpha 最有价值的地方，其实并不是把已有因子翻译成代码。

因为如果只是实现完全等价转换，那么最终得到的仍然是同一个 Alpha，只不过换了一种表达方式而已。

总部培训时也提到过类似观点：

> 单纯将平台表达式翻译成 Python Alpha，本身并没有太大的研究价值。

真正让我感兴趣的是几个问题：

- Python Alpha 能否帮助我们发现因子中的冗余结构？
- Python Alpha 能否重新审视已有 Alpha 的信息来源？
- Python Alpha 能否实现 Fast Expression 无法表达的新计算结构？

带着这些问题，我对一个已经通过测试的 Alpha 进行了拆解实验。

原始表达式如下：

signed_power(group_zscore(round_down(ts_decay_exp_window(floor(ts_mean(winsorize(plant_data,std=4),xxx)),xxx,factor=0.x),f=1),sector),2)

整个结构包含：

- winsorize
- ts_mean
- floor
- ts_decay_exp_window
- round_down
- group_zscore
- signed_power

共计 7 层操作符嵌套。

从 Fast Expression 的角度来看，这是一个非常典型的 Alpha 结构。

但问题是：

这 7 个操作符是否都在贡献有效信息？

还是其中部分操作符只是历史迭代过程中不断叠加出来的“装饰层”？

于是我决定利用 Python Alpha 对其进行逐层拆解。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
>  |t
> slened_pONET(Broup_TsCore(round_down ts_dacay_ep_ndow(floor(ts_Iean MInsorize(f
> RsrsDt S0:477
> TBIPEATP 436
> SIUAToN 52TTIN
> 1.6|
> 5.179
> +05
> 5.1190
> 4.5891
> 15.81930o
> Ohooot 
> s
> U
> 
> a
> om
> f
> Ieeh
> Ma To
> N Fe
> 4J!
> TU
> CUesr
> SU
> S
> [e
> Tl
> [e4
> [oeto
> t
>  Le Cen
> Tl Cene
> 
> 
> Clom Mlpha
> J5
> 2
> N Chart
> 2
> 318
> 1。
> ~JIOP
> Ivesability COnSTJICO
> ATCcateDJta
> Ju1+
> J5
> JJl
> Jn 1
> Jus
> Jeu
> JJ-
> Jonl
> J1
> Jn
> 』J
> J7
> J3
> Jn -
> J?1
> J1 2
> J2
> Jn
> JJl
> 1.52
> 099
> 4.5590
> 5.2196
> 14.943co
> [vesabilis
> Consle|Pl
> 匡 Correlation
> SCIrCoTITIOI
> Wum r
> LelsT +
> I5 Testing Status
> Pend
> LOWCT LOOICoTTCIton
> 
> L I
> 8 PASS
> LTCf mTaITCI
> 1C
> NN TTCPI
> WARNIING
> 0.5218
> 0.5042
> Inoncsalc UiLfr inzJ nacrs;Itr] Crccl Uil
> TJC
> VrTTF  TTSLrT
> KehTITOer TIOE
> 4
> Delay CONCL20
> TOON
> 一 =O
> TTUTTIeTTeLMsaTT0 290
> TCCOTC0
> CTFCTT
> CCTI
> m
> Theme CL HehTurnover Darasets Theme CJer
> TShwTTUTClercf2
> PCNOIIG


# 2. 实现

在 Python Alpha 中，我并没有直接复刻全部表达式。

而是把每一层逻辑拆开，观察其对最终结果的贡献。

研究过程中我发现一个有趣现象：

因子的主要信息实际上集中在以下链路中：

winsorize → ts_mean → floor → ts_decay_exp_window → round_down

而最外层的：

- group_zscore
- signed_power

对于最终 Sharpe 和 Fitness 的提升远低于预期。

换句话说：

原始表达式虽然包含 7 个操作符，但真正承担主要信息提取任务的只有前面几个核心模块。

因此最终 Python Alpha 保留了核心部分：

winsorize → ts_mean → floor → decay → round_down

并移除了部分贡献有限的后处理结构。

这里有一个有趣的现象。

如果只是简单把表达式封装进 Python Alpha，那么本质上仍然是在复刻已有逻辑。

研究价值其实并不高。

真正值得关注的是：

当我们开始拆解 Alpha 时，会发现哪些部分是真正提供信息的，哪些部分只是不断叠加出来的复杂度。

结果令人意外。

回测表现与原始表达式保持高度一致。

但整体复杂度显著下降。

从研究角度来看，这相当于完成了一次因子结构压缩（Factor Compression）。

过去我们习惯不断向 Alpha 外层叠加新的操作符。

而 Python Alpha 给了我们反向思考的机会：

- 哪些操作符是真正有价值的？
- 哪些操作符只是让表达式变得更长？
- 哪些部分是核心信号？
- 哪些部分只是后处理包装？


> [!NOTE] [图片 OCR 识别内容]
> 区 Openalpha datailsin newtab
> Code
> from brain.alphas mort apha
> iort nwpy as 叩
> iport numpy.typing
> npt
> SITUIatIOI
> Settings
> InsnueType
> Reglon
> Uoere
> Laneo
> Decy
> Uelay
> Truncaton
> Newuraliaon
> Pateurtaon
> Cookback
> Nax Trad
> Na Posiuon
> Cuil'
> TUFZUUJ
> D
> SlulisliLl
> Clone Alpha 
> IS Summary
> Pariod
> ASinz = Czta Set ~ pFs
> A Resular -ohs
> Fyrmidtems USAIDIIANALYST 12
> AEBTegate Data
> SMulre
> TuTlUVL
> FIomo
> Reluriy
> Cd
> Ua
> 1.54
> 5.6995
> 1.00
> 4.529
> 7.0496
> 16.24900
> Yea
> Chok
> TUIO
> Te
> Relr
> Dr
> Maroin
> Lmo Co
> Sor CUNt



> [!NOTE] [图片 OCR 识别内容]
> Steak 416 day
> f_vals[k]
> 叩. floor(mean_val)
> tsbufo 恶妥保(聂近 dO 步的 winsorize 纺采。月于计H下-个 ts_rean
> tsbufo
> Min_W[-d: ]
> tsbufI I妥保K聂近 dI 步的 floor(ts_wean) 纺呆。用于计M ts_decay_exp_hindon
> tsbufl
> Vals
> TeTIn
> tsbufo
> tsbutr
> ealpha(
> Jata=
> plant_data' ],
> ST0Te
> TaIE
> itsbufo"
> aJims
> "yi'
> extend"
> 叩.float32(I.nan)}
> name
> ntsbufl"
> "dims
> "ti'
> extend"
> m.float3z(Ipnan)}
> Jef alpha_func (data
> store)
> ntIurray[ m .float3z]:
> Ist
> Jata plant_data.shape[l]
> 1。暖启动初妗化 store.tsbufo 和 store.tsbufl
> i store.tsbufo is None
> store.tsbufI is None:
> tsbufo
> tsbufr
> Rrmup_buffers (data
> 180,228,
> inst)
> store.tsbufo
> tsbufo
> store.tsbufl
> tsbufl
> 2。为辰计M:  聂薪一天竹茯面效O Winsorize
> winsorize_Id(data.plant_data[-1]
> ^劲更新 tsbufo (FIFO) 井且计.y薪一天前
> floor(ts_wean)
> store.tsbufo[:-1]
> store.tsbufo[I:
> Capy()
> store.tsbufo[-1] =
> Mth np.errstate(invalid-'inore
> divide'inore' ):
> mea_ral
> np.nanmeanlstore.tsbufe, axis g
> T.floor(wean_val)
> 滚劲更新 tsbufl (FIFO) 井且计卑聂葑一天前 ts_decay_eXP_windo
> store.tsbufr[:-1]
> store.tsbufz [1:
> Capy()
> store.tsbufI[-1] =
> 十间辰计.:  荇颁赉>咨劲平均
> Mith np.errstate(invalid 'inore
> Jivide- 'inore
> ts_decay_exp_Mindou(store.tsbufl;
> 220
> I88
> 戛外层计奘:
> TOUIU
> dow(.
> f-1)
> 「oud_don(a, 1.8)
> 103
> Feturn
> rasbpe(mp.float32)


# 3. 一个更有趣的发现：Python Alpha 的价值并不在于“翻译”

随着研究继续深入，我逐渐意识到：

Python Alpha 最大的价值可能根本不在于表达式转换。

而在于：

## 计算自由（Computational Freedom）

Fast Expression 时代，我们所有研究都建立在已有操作符体系之上。

研究过程通常是：

```
研究 = 组合操作符
```

发现数据 → 选择操作符 → 拼接表达式 → 回测

整个研究流程都围绕已有工具展开。

而 Python Alpha 的出现带来了一个变化：

研究者开始能够自己设计计算过程。

过去：

如果平台没有某个操作符。

研究思路可能就无法实现。

现在：

我们可以直接实现自己的逻辑。

甚至可以设计属于自己的中间状态。

从某种意义上说：

Python Alpha 正在把研究者从“操作符使用者”变成“计算框架设计者”。

这是一种完全不同的研究范式。

# 4. 一个被忽略的能力：双缓存状态流水线（Dual Buffer Stateful Pipeline）

在整个实验过程中，我认为最容易被忽略的能力并不是操作符数量。

而是：

## 状态（State）

Fast Expression 本质上属于无状态计算框架。

每次计算都依赖于历史窗口重新扫描。

例如：

- ts_mean
- ts_std_dev
- ts_decay_exp_window

本质上都是：

读取历史窗口 → 计算 → 输出结果

然后进入下一天重新执行。

研究者更多是在调用已有操作符。

而不是管理计算过程本身。

但 Python Alpha 出现之后，情况开始发生变化。

通过 Store，我们第一次拥有了保存状态的能力。

在本文实现中，我设计了一个简单但有趣的双缓存状态流水线（Dual Buffer Stateful Pipeline）。

整体结构如下：

```
plant_data      ↓ winsorize      ↓ ┌─────────┐ │ tsbuf0  │ └─────────┘      ↓  ts_mean      ↓   floor      ↓ ┌─────────┐ │ tsbuf1  │ └─────────┘      ↓ ts_decay      ↓ round_down      ↓  Alpha
```

### 第一层缓存：tsbuf0

tsbuf0 保存最近 180 天的 winsorize 结果。

每个交易日到来时：

- 删除最旧数据
- 插入最新数据
- 保持窗口长度不变

这样后续计算 ts_mean 时，不需要重新构造完整历史序列。

tsbuf0 更像是一个：

**基础信号仓库（Raw Signal Buffer）**

### 第二层缓存：tsbuf1

tsbuf1 保存最近 220 天的 floor(ts_mean) 结果。

这一层已经不再是原始数据。

而是经过第一层处理后的中间状态。

因此：

tsbuf1 本质上是一个：

**特征状态仓库（Feature Buffer）**

### 为什么这很重要？

如果只看最终结果：

这个 Alpha 看起来只是：

winsorize → ts_mean → floor → decay → round_down

但从计算框架来看：

实际上已经变成：

```
数据层    ↓状态层    ↓特征层    ↓输出层
```

这是一种完全不同的研究思路。

过去：

研究 = 组合操作符

现在：

研究 = 设计数据流

### Python Alpha 带来的不仅是代码能力

更重要的是：

它允许研究者自行设计状态结构。

例如：

- 单缓存结构
- 双缓存结构
- 多级状态流水线
- 自适应状态更新机制

这些能力在 Fast Expression 中很难直接表达。

而在 Python Alpha 中却变得十分自然。

# 5. 为什么我认为这对 Genius 评级有意义

对于很多顾问来说，Genius 不仅是一套评级体系，也是长期研究能力的体现。

从目前公开规则来看：

- Operator Count
- Field Count
- Alpha 提交数量
- Tower Coverage
- Combine
- 六维指标

都会对最终评级产生影响。

因此很多顾问在研究过程中都会面临一个问题：

如何在保证 Alpha 质量的同时，优化整体结构。

本次实验给我的启发是：

Python Alpha 的价值并不仅仅在于减少操作符。

如果只是简单把 Fast Expression 翻译成 Python Alpha，那么意义并不大。

真正有价值的是：

利用 Python Alpha 实现 Fast Expression 难以表达的新结构。

例如本文使用的：

- 双缓存状态流水线
- Store 状态管理
- 多层特征缓存

这些能力本身并不存在于传统操作符体系之中。

从这个角度来看：

Python Alpha 不只是新的表达方式。

它提供了一种新的研究工具。

一方面可以帮助研究者重新审视 Alpha 结构；

另一方面也能够探索传统 Fast Expression 难以实现的新思路。

对于希望提升 Genius 综合竞争力的顾问来说，这种能力或许值得进一步研究。

# 6. 总结

这次实验最大的收获，并不是成功把 Fast Expression 转换成 Python Alpha。

而是让我意识到：

很多时候：

复杂并不等于有效。

长表达式也不一定意味着更多信息。

通过逐层拆解，我发现部分操作符对于最终结果的贡献远低于预期，而核心信号却能够在更简单的结构中被保留下来。

与此同时，Python Alpha 还提供了 Fast Expression 所不具备的能力：

- 自定义计算逻辑
- 状态管理
- 多层缓存结构
- 流水线式特征构建

在本文案例中，双缓存状态流水线（Dual Buffer Stateful Pipeline）只是一个简单尝试。

但它让我看到了另一种研究方向：

过去我们是在使用操作符。

未来我们或许可以开始设计计算框架。

过去我们是在组合 Alpha。

未来我们或许可以开始构建 Alpha Framework。

而这，也许才是 Python Alpha 真正有趣的地方。

---

### 帖子 #59: 【PPAC 提交经验分享】注意！Prod Correlation 报错，实际卡点可能是 Power Pool 相关性
- **主帖链接**: 【PPAC 提交经验分享】注意Prod Correlation 报错实际卡点可能是 Power Pool 相关性.md
- **讨论数**: 3

各位还在肝 PPAC 的朋友们，大家好！

最近在提交 Power Pool Alpha 的时候，遇到了一个有点迷惑的报错情况，研究了一下，想把经验分享给大家，希望能帮到可能遇到同样问题的人。

**情况是这样的：**

大家知道，PPAC 的规则里明确写着 Power Pool Alpha  **豁免检查 Prod Correlation** 。同时，对于 “Self-Correlation” 中的  **“与已标记为Power Pool的Alphas的相关系数 ≤0.5”**  这一条，如果超过了，系统也是不会允许检查通过的。

**但诡异的地方来了：**

当我这个 Power Pool 相关系数（比如 0.6104）确实超过 0.5 时，我收到的 **并不是** 预期的明确 Power Pool 相关性超标的因此无法提交的 FAIL，而是直接收到另一个  **FAIL** ，提示信息是  **“Prod correlation 0.9311 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.”**

**我的分析和结论是：**

尽管 PPAC 规则中 Prod Correlation 是豁免项，但当你的  **“Power Pool的Alphas的相关系数” 实际上已经大于 0.5 时，系统似乎会转而通过 Prod Correlation (>0.7) 这个条件来卡住你的提交，并给出 FAIL。**

也就是说，虽然错误信息显示的是 Prod Correlation 问题，但 **根本原因很可能是你的 Alpha 与现有 Power Pool Alpha 的相关性超过了 0.5 的阈值** 。它没有直接报 Power Pool 相关性超标导致 FAIL，而是“借用”了 Prod Correlation 的名义。

**给大家的提醒：**

所以，如果你在提交 Power Pool Alpha 时，明明知道 Prod Correlation 是豁免的，但最后却收到了因为 Prod Correlation 过高（比如 >0.7）而导致的 FAIL，那么请 **务必回头检查你的 Alpha 与现有 Power Pool Alphas 的相关系数是否已经超过了 0.5** 。这很可能才是真正的症结所在！


> [!NOTE] [图片 OCR 识别内容]
> 邑 Correlation
> IS Testing Status
> Period
> Self Correlation
> IHMUMT
> Nnimum
> 11PASS
> 1FAIL
> Prod Correlation
> NsmUM
> TMNC
> Prod correlaton 0.9311
> above CUtoff of 0.7and Sharpe not better by 10.0% Or more
> 2WARNNG
> PoiEI Pool CorrElaton 06104
> above CUOff of 0.5 and Sharpe not better by 10.095 Ormore
> IeIe FOWETPOOLNPHaS Theme JOES RJC TatCH NITMUtTDIeTOTZS
> Performance Comparison
> 虽然池子大于了0.5才是不通过原因
> 但是它是WARNING
> FAIL 用的是 Prod Correlation
> Properties
> Name
> Why not sUb
> Selectaddtags
> Description
> Idea: https:lIsupportworldquantbrain.comlhclen-UsIComMU
> Aphas
> Rationale for data used: is a Eood sien 可以带来比较不锘的收芒
> [2+
> PLieLlLese
> Cannot submit Alpha:
> test failed
> Tags


虽然规则说放低了条件，不查 Prod-Correlation，但还是需要我们注意，避免提交IS表现很差的Alpha，从而影响我们的 Value Factor。

希望这个小发现能帮到大家，祝各位提交顺利！

---

### 帖子 #60: 【PPAC 提交经验分享】注意！Prod Correlation 报错，实际卡点可能是 Power Pool 相关性
- **主帖链接**: https://support.worldquantbrain.com【PPAC 提交经验分享】注意Prod Correlation 报错实际卡点可能是 Power Pool 相关性_32223192365207.md
- **讨论数**: 3

各位还在肝 PPAC 的朋友们，大家好！

最近在提交 Power Pool Alpha 的时候，遇到了一个有点迷惑的报错情况，研究了一下，想把经验分享给大家，希望能帮到可能遇到同样问题的人。

**情况是这样的：**

大家知道，PPAC 的规则里明确写着 Power Pool Alpha  **豁免检查 Prod Correlation** 。同时，对于 “Self-Correlation” 中的  **“与已标记为Power Pool的Alphas的相关系数 ≤0.5”**  这一条，如果超过了，系统也是不会允许检查通过的。

**但诡异的地方来了：**

当我这个 Power Pool 相关系数（比如 0.6104）确实超过 0.5 时，我收到的 **并不是** 预期的明确 Power Pool 相关性超标的因此无法提交的 FAIL，而是直接收到另一个  **FAIL** ，提示信息是  **“Prod correlation 0.9311 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.”**

**我的分析和结论是：**

尽管 PPAC 规则中 Prod Correlation 是豁免项，但当你的  **“Power Pool的Alphas的相关系数” 实际上已经大于 0.5 时，系统似乎会转而通过 Prod Correlation (>0.7) 这个条件来卡住你的提交，并给出 FAIL。**

也就是说，虽然错误信息显示的是 Prod Correlation 问题，但 **根本原因很可能是你的 Alpha 与现有 Power Pool Alpha 的相关性超过了 0.5 的阈值** 。它没有直接报 Power Pool 相关性超标导致 FAIL，而是“借用”了 Prod Correlation 的名义。

**给大家的提醒：**

所以，如果你在提交 Power Pool Alpha 时，明明知道 Prod Correlation 是豁免的，但最后却收到了因为 Prod Correlation 过高（比如 >0.7）而导致的 FAIL，那么请 **务必回头检查你的 Alpha 与现有 Power Pool Alphas 的相关系数是否已经超过了 0.5** 。这很可能才是真正的症结所在！


> [!NOTE] [图片 OCR 识别内容]
> 邑 Correlation
> IS Testing Status
> Period
> Self Correlation
> IHMUMT
> Nnimum
> 11PASS
> 1FAIL
> Prod Correlation
> NsmUM
> TMNC
> Prod correlaton 0.9311
> above CUtoff of 0.7and Sharpe not better by 10.0% Or more
> 2WARNNG
> PoiEI Pool CorrElaton 06104
> above CUOff of 0.5 and Sharpe not better by 10.095 Ormore
> IeIe FOWETPOOLNPHaS Theme JOES RJC TatCH NITMUtTDIeTOTZS
> Performance Comparison
> 虽然池子大于了0.5才是不通过原因
> 但是它是WARNING
> FAIL 用的是 Prod Correlation
> Properties
> Name
> Why not sUb
> Selectaddtags
> Description
> Idea: https:lIsupportworldquantbrain.comlhclen-UsIComMU
> Aphas
> Rationale for data used: is a Eood sien 可以带来比较不锘的收芒
> [2+
> PLieLlLese
> Cannot submit Alpha:
> test failed
> Tags


虽然规则说放低了条件，不查 Prod-Correlation，但还是需要我们注意，避免提交IS表现很差的Alpha，从而影响我们的 Value Factor。

希望这个小发现能帮到大家，祝各位提交顺利！

---

### 帖子 #61: 【贺六浑】 回测次数到达4700，自动强制终止回测 开箱即用脚本代码优化
- **主帖链接**: 【贺六浑】 回测次数到达4700自动强制终止回测 开箱即用脚本代码优化.md
- **讨论数**: 5

各位肝RA SA PPA  的大佬们，新年好！

大家是不是经常遇到这种情况：晚上写好了思路，挂着脚本跑因子，心想“明天早上起来收菜”。结果早上睡醒一看，好家伙，脚本确实很勤奋，把那 5000 次每日回测额度跑得干干净净（甚至还透支了）。

这时候如果你突然来了灵感，想手搓两个 Alpha，或者是想让 AI 针对昨晚的结果再做一轮精细优化，结果发现—— **没额度了！**  只能干瞪眼等美东时间重置，那种感觉太难受了。

为了解决这个问题，我写了一个 “防爆仓“ 的看门狗脚本。

### 核心原理

我们在跑回测的主程序之外，开一个 **后台监控线程** 。 这个线程每隔几秒钟就去问一下服务器：“我现在用了多少次了？” 一旦发现回测次数超过设定的阈值（比如 4700 次），它就会 **直接拔电源** （强制杀掉进程），强行留下 300 次给咱们早上起来“手动操作”或“AI 优化”的空间。

### 准备工作

你需要安装  `pytz`  库来精确处理美东时间（不用自己算时差了，超准）：

Bash

```
pip install pytz
```

### 开箱即用代码

代码分为两部分：

1. **高精度查询函数  和 监控函数** （自动处理夏令时，不需要手动改UTC偏移量）。
2. **主程序** （直接替换你原本的运行入口）。

#### 第一步：把这个查询函数加到你的代码里

这个版本上个硬减 13 小时的代码更稳，直接定位纽约时区。

```
from datetime import datetime, timedeltaimport pytzimport threadingimport timeimport osimport asyncio# 假设你已经导入了 wqb 相关库def get_today_simulations_count(session):    """    获取当前纽约时间当天的回测提交数量    自动处理夏令时(DST)，无需手动计算时差    """    try:        # 直接定位纽约时间        ny_tz = pytz.timezone('America/New_York')        today_start = datetime.now(ny_tz).replace(hour=0, minute=0, second=0, microsecond=0)        tomorrow_start = today_start + timedelta(days=1)        payload = {            'limit': 1,            'offset': 0,            'status': 'UNSUBMITTED\x1fIS_FAIL',             'dateCreated>': today_start.isoformat(),            'dateCreated<': tomorrow_start.isoformat(),            'hidden': 'false'        }        response = session.get(            '[链接已屏蔽]             params=payload,            timeout=10        )        response.raise_for_status()        return response.json().get('count', 0)    except Exception as e:        print(f"[查询API波动] 暂时无法获取数量: {e}")        return 0 # 返回0防止误杀，或者根据需求处理# ---------------- 配置区域 ----------------SAFE_LIMIT = 4700  # 你想保留的阈值CHECK_INTERVAL = 30  # 检查间隔(秒)，建议30秒，太快费API，太慢容易超def monitor_quota_and_kill():    # 在线程里单独登录一次，避免和主线程session冲突    s_monitor = login()    while True:        try:            # 查询当前用量            current_num = get_today_simulations_count(s_monitor)            print(f"[监控中] 当前回测次数: {current_num}")            if current_num > SAFE_LIMIT:                print(f"\n" + "!" * 40)                print(f"!!! 警告：回测次数达到 {current_num}，超过阈值 {SAFE_LIMIT} !!!")                print("!!! 正在强制终止进程以保护资源 !!!")                print("!" * 40 + "\n")                # os._exit(0) 是核弹级退出，不给主线程任何反应机会，直接杀                # 这样才能确保不会多跑任何一个测试                time.sleep(1)                os._exit(0)        except Exception as e:            # 监控线程报错不要停，继续下次检查            pass        time.sleep(CHECK_INTERVAL)
```

2.主程序中添加 两行逻辑

```
t = threading.Thread(target=monitor_quota_and_kill, daemon=True)t.start()# 这里是你原来的回测逻辑 (以 wqb 库为例)# 佬们自行替换成自己的 回测方式multi_fo_alphas = wqb.to_multi_alphas(fo_alphas, 8)concurrency = 8  # 1 <= concurrency <= 10resps = asyncio.run(    wqbs.concurrent_simulate(        multi_fo_alphas,  # `alphas` or `multi_alphas`        concurrency,        return_exceptions=True,        on_nolocation=lambda vars: print(vars['target'], vars['resp'], sep='\n'),        on_start=lambda vars: print(vars['url']),        on_finish=lambda vars: print(vars['resp']),        on_success=lambda vars: print(vars['resp']),        on_failure=lambda vars: print(vars['resp']),    ))for idx, resp in enumerate(resps, start=1):    print(idx)
```

运行结果展示：


> [!NOTE] [图片 OCR 识别内容]
> Ckespon5e
> LLUU」 >
> <Response [200]>
> ht5:LLapiWopldqwantbr ncomLsiwylation
> <Response [200]〉
> <Response [200]〉
> ht5_
> Liwopldqyantbr ncomLsiwylation
> 监控中]  当前回测次数:  4701
> 警告
> 回测次数达到 4701,超过阈值  4700
> 正在强制终止进程以保护资源


祝大家 VF 暴涨，早日 GM！

---

### 帖子 #62: 【贺六浑】 回测次数到达4700，自动强制终止回测 开箱即用脚本代码优化
- **主帖链接**: https://support.worldquantbrain.com【贺六浑】 回测次数到达4700自动强制终止回测 开箱即用脚本代码优化_37553419414807.md
- **讨论数**: 5

各位肝RA SA PPA  的大佬们，新年好！

大家是不是经常遇到这种情况：晚上写好了思路，挂着脚本跑因子，心想“明天早上起来收菜”。结果早上睡醒一看，好家伙，脚本确实很勤奋，把那 5000 次每日回测额度跑得干干净净（甚至还透支了）。

这时候如果你突然来了灵感，想手搓两个 Alpha，或者是想让 AI 针对昨晚的结果再做一轮精细优化，结果发现—— **没额度了！**  只能干瞪眼等美东时间重置，那种感觉太难受了。

为了解决这个问题，我写了一个 “防爆仓“ 的看门狗脚本。

### 核心原理

我们在跑回测的主程序之外，开一个 **后台监控线程** 。 这个线程每隔几秒钟就去问一下服务器：“我现在用了多少次了？” 一旦发现回测次数超过设定的阈值（比如 4700 次），它就会 **直接拔电源** （强制杀掉进程），强行留下 300 次给咱们早上起来“手动操作”或“AI 优化”的空间。

### 准备工作

你需要安装  `pytz`  库来精确处理美东时间（不用自己算时差了，超准）：

Bash

```
pip install pytz
```

### 开箱即用代码

代码分为两部分：

1. **高精度查询函数  和 监控函数** （自动处理夏令时，不需要手动改UTC偏移量）。
2. **主程序** （直接替换你原本的运行入口）。

#### 第一步：把这个查询函数加到你的代码里

这个版本上个硬减 13 小时的代码更稳，直接定位纽约时区。

```
from datetime import datetime, timedeltaimport pytzimport threadingimport timeimport osimport asyncio# 假设你已经导入了 wqb 相关库def get_today_simulations_count(session):    """    获取当前纽约时间当天的回测提交数量    自动处理夏令时(DST)，无需手动计算时差    """    try:        # 直接定位纽约时间        ny_tz = pytz.timezone('America/New_York')        today_start = datetime.now(ny_tz).replace(hour=0, minute=0, second=0, microsecond=0)        tomorrow_start = today_start + timedelta(days=1)        payload = {            'limit': 1,            'offset': 0,            'status': 'UNSUBMITTED\x1fIS_FAIL',             'dateCreated>': today_start.isoformat(),            'dateCreated<': tomorrow_start.isoformat(),            'hidden': 'false'        }        response = session.get(            '[链接已屏蔽]             params=payload,            timeout=10        )        response.raise_for_status()        return response.json().get('count', 0)    except Exception as e:        print(f"[查询API波动] 暂时无法获取数量: {e}")        return 0 # 返回0防止误杀，或者根据需求处理# ---------------- 配置区域 ----------------SAFE_LIMIT = 4700  # 你想保留的阈值CHECK_INTERVAL = 30  # 检查间隔(秒)，建议30秒，太快费API，太慢容易超def monitor_quota_and_kill():    # 在线程里单独登录一次，避免和主线程session冲突    s_monitor = login()    while True:        try:            # 查询当前用量            current_num = get_today_simulations_count(s_monitor)            print(f"[监控中] 当前回测次数: {current_num}")            if current_num > SAFE_LIMIT:                print(f"\n" + "!" * 40)                print(f"!!! 警告：回测次数达到 {current_num}，超过阈值 {SAFE_LIMIT} !!!")                print("!!! 正在强制终止进程以保护资源 !!!")                print("!" * 40 + "\n")                # os._exit(0) 是核弹级退出，不给主线程任何反应机会，直接杀                # 这样才能确保不会多跑任何一个测试                time.sleep(1)                os._exit(0)        except Exception as e:            # 监控线程报错不要停，继续下次检查            pass        time.sleep(CHECK_INTERVAL)
```

2.主程序中添加 两行逻辑

```
t = threading.Thread(target=monitor_quota_and_kill, daemon=True)t.start()# 这里是你原来的回测逻辑 (以 wqb 库为例)# 佬们自行替换成自己的 回测方式multi_fo_alphas = wqb.to_multi_alphas(fo_alphas, 8)concurrency = 8  # 1 <= concurrency <= 10resps = asyncio.run(    wqbs.concurrent_simulate(        multi_fo_alphas,  # `alphas` or `multi_alphas`        concurrency,        return_exceptions=True,        on_nolocation=lambda vars: print(vars['target'], vars['resp'], sep='\n'),        on_start=lambda vars: print(vars['url']),        on_finish=lambda vars: print(vars['resp']),        on_success=lambda vars: print(vars['resp']),        on_failure=lambda vars: print(vars['resp']),    ))for idx, resp in enumerate(resps, start=1):    print(idx)
```

运行结果展示：


> [!NOTE] [图片 OCR 识别内容]
> Ckespon5e
> LLUU」 >
> <Response [200]>
> ht5:LLapiWopldqwantbr ncomLsiwylation
> <Response [200]〉
> <Response [200]〉
> ht5_
> Liwopldqyantbr ncomLsiwylation
> 监控中]  当前回测次数:  4701
> 警告
> 回测次数达到 4701,超过阈值  4700
> 正在强制终止进程以保护资源


祝大家 VF 暴涨，早日 GM！

---

### 帖子 #63: --- 阶段四：打印总结报告 ---
- **主帖链接**: 【贺六浑】-【工具配置】OC2025 一键清空分数脚本经验分享.md
- **讨论数**: 19

前两天看到 课代表  **@XX42289**  分享的《CA 降维 + 多指标聚类数评判 Osmosis 点数分配工具》，确实是大神级的干货，直接实现了科学分配分数，在此先感谢课代表的付出！

不过在使用过程中我发现一个小痛点： 课代表的代码主要负责“分配”，但如果我们调整了参数想 **重新分配** ，或者想把之前的旧分数 **全部推倒重来** ，手动一个个去清空（或者等新代码覆盖）就显得有点麻烦了，尤其是当 Alpha 数量很多的时候。

为了配合那个分配工具，实现真正的“一键流”闭环，我写了一个【一键清空分数脚本】。

**它的主要功能：**

1. **多线程并发** ：使用了线程池，清空速度比单线程快得多。
2. **安全范围** ：可以指定日期范围（比如成为 Consultant 的日期），只清空该日期之后的 Alpha 分数，不误伤老资产。
3. **智能筛选** ：只处理有分数的常规 Alpha，不浪费请求次数。

**使用场景：**  想重新跑聚类分配算法前，先运行此脚本，还你一个干干净净的列表。

```
# -*- coding: utf-8 -*-import timefrom datetime import datetime, timedeltafrom machine_lib import *  # 假设 login() 在这里from concurrent.futures import ThreadPoolExecutorimport json# ===================================================================# PART 1: 配置与函数定义# ===================================================================# --- 用户配置 ---# 1. 成为顾问的日期，也是 Alpha 开始计算收益的日期TOBE_CONSULTANT_DAY = "2025-04-14"# 2. 并发清除操作的线程数MAX_WORKERS = 10def up_alpha_properties_to_clear(s, alpha_id: str, old_osmosisPoints: str):    """    一个专门用于清除 Alpha 分数的函数。    它通过将 'osmosisPoints' 字段设置为 null 来实现。    """    params = {"osmosisPoints": None}  # 在 requests 中, None 会被序列化为 JSON null    response = s.patch(        f"[链接已屏蔽] json=params    )    if response.status_code == 200:        print(f"成功清除 Alpha {alpha_id} 的分数 (原分数: {old_osmosisPoints})。")        return "SUCCESS"    else:        print(f"清除 Alpha {alpha_id} 分数失败，状态码: {response.status_code}, 信息: {response.text}")        return "FAILED"def get_colored_alphas_in_date_range(s, start_date, end_date, alpha_num_limit=1000):    """    获取在指定日期范围内，所有设置了分数的常规 (non-SUPER) Alpha。    """    colored_alphas = []    print(f"开始查找从 {start_date} 到 {end_date} 所有已设置分数的常规 Alpha...")    for i in range(0, alpha_num_limit, 100):        print(f"正在扫描第 {i} 到 {i + 100} 个 alpha...")        # 【重要】在 URL 中加入了 dateSubmitted 过滤器        url_e = (            f"[链接已屏蔽]            f"&status!=UNSUBMITTED&status!=IS_FAIL&type!=SUPER&hidden=false"            f"&dateSubmitted>={start_date}T00:00:00-04:00"            f"&dateSubmitted<{end_date}T00:00:00-04:00"        )        try:            response = s.get(url_e)            response.raise_for_status()            alpha_list = response.json().get("results", [])            if not alpha_list:                print("已扫描完所有符合条件的 Alpha。")                break            # 在客户端筛选出有分数的 Alpha            for alpha in alpha_list:                if alpha.get("osmosisPoints") is not None:                    record = {                        "id": alpha["id"],                        "osmosisPoints": alpha["osmosisPoints"]                    }                    colored_alphas.append(record)        except Exception as e:            print(f"获取alpha时发生异常: {e}")            resp = s.get('[链接已屏蔽])            if resp.status_code != 200:                print(f"用户会话可能已过期，状态码: {resp.status_code}")            break    print(f"\n查找完毕！共找到 {len(colored_alphas)} 个在指定日期内需要清除分数的 Alpha。")    return colored_alphas# ===================================================================# PART 2: 主逻辑# ===================================================================if __name__ == "__main__":    s = login()    # --- 阶段一：计算日期范围 ---    begin_date = TOBE_CONSULTANT_DAY    end_date_obj = datetime.now() + timedelta(days=1)    end_date = end_date_obj.strftime("%Y-%m-%d")    print("-" * 50)    print("本脚本将查找并清除指定日期范围内的常规 Alpha 分数。")    print(f"顾问开始日 (脚本起始日期): {begin_date}")    print(f"脚本截止日期: {end_date}")    print("-" * 50)    # --- 阶段二：获取指定日期范围内带分数的 Alphas ---    alphas_to_clear = get_colored_alphas_in_date_range(s, begin_date, end_date)    if not alphas_to_clear:        print("在指定日期范围内未找到任何设置了分数的 Alpha，程序结束。")    else:        # --- 阶段三：并发清除分数 ---        print("\n准备开始清除分数...")        tasks = []        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:            for alpha_data in alphas_to_clear:                alpha_id = alpha_data["id"]                old_osmosisPoints = alpha_data["osmosisPoints"]                tasks.append(executor.submit(up_alpha_properties_to_clear, s, alpha_id, old_osmosisPoints))        # 等待所有任务完成并收集结果        results = [task.result() for task in tasks]        # --- 阶段四：打印总结报告 ---        print("\n" + "=" * 50)        print("所有分数清除任务已完成。")        success_count = results.count("SUCCESS")        failed_count = results.count("FAILED")        print(f"\n总结报告:")        print(f"- 成功清除分数的 Alpha 数量: {success_count}")        print(f"- 失败的任务数量: {failed_count}")        print("\n脚本执行完毕。")        print("=" * 50)
```


> [!NOTE] [图片 OCR 识别内容]
> C: |Users Iruanyanghui |AppData |Local |Programs | Python |Python312 Ipython.exe
> I:
> b'{"user": {"id":"顾问 顾问 JR23144 (Rank 6) (Rank 6)"} , "token" : {"expiry" : 86400.0}
> permissions
> [ "BEFORE
> 亏
> 过
> 本脚本将耷找并清除指定日期范围内的常规 Alpha 分数。
> 顾问开始日
> (脚本起始日期):
> 2025-04-14
> 脚本截止日期:
> 2025-12-18
> 开始耷找从
> 2025-04-14  到
> 2025-12-18
> 所有己设置分数的常规 Alpha
> 正在扫描第
> 0到  100
> alpha
> 正在扫描第
> 100  到
> 200
> alpha
> 正在扫描第
> 200  到
> 300
> alpha
> 正在扫描第
> 300  到
> 400
> alpha
> 正在扫描第  400  到
> 500
> alpha
> 正在扫描第
> 500  到
> 600
> alpha
> 正在扫描第
> 600  到
> 700
> alpha
> 己扫描完所有符合条件的
> Alpha:
> 耷找完毕!共找到
> 20  个在指定日期内需要清除分数的 Alpha。
> 淮备开始清除分数.
> 成功清除
> Alpha
> 的分数 (原分数:
> 3448).
> 成功清除 Alpha
> 哟分数
> (原分数:
> 10000).
> 成功清除 Alpha
> 的分数
> (原分数:
> 10000)
> HTTr喾压
> 17 nh3
> O5 
> C屑幺~
> 101000


---

### 帖子 #64: --- 阶段四：打印总结报告 ---
- **主帖链接**: https://support.worldquantbrain.com【贺六浑】-【工具配置】OC2025 一键清空分数脚本经验分享_37090321198359.md
- **讨论数**: 19

前两天看到 课代表  **@XX42289**  分享的《CA 降维 + 多指标聚类数评判 Osmosis 点数分配工具》，确实是大神级的干货，直接实现了科学分配分数，在此先感谢课代表的付出！

不过在使用过程中我发现一个小痛点： 课代表的代码主要负责“分配”，但如果我们调整了参数想 **重新分配** ，或者想把之前的旧分数 **全部推倒重来** ，手动一个个去清空（或者等新代码覆盖）就显得有点麻烦了，尤其是当 Alpha 数量很多的时候。

为了配合那个分配工具，实现真正的“一键流”闭环，我写了一个【一键清空分数脚本】。

**它的主要功能：**

1. **多线程并发** ：使用了线程池，清空速度比单线程快得多。
2. **安全范围** ：可以指定日期范围（比如成为 Consultant 的日期），只清空该日期之后的 Alpha 分数，不误伤老资产。
3. **智能筛选** ：只处理有分数的常规 Alpha，不浪费请求次数。

**使用场景：**  想重新跑聚类分配算法前，先运行此脚本，还你一个干干净净的列表。

```
# -*- coding: utf-8 -*-import timefrom datetime import datetime, timedeltafrom machine_lib import *  # 假设 login() 在这里from concurrent.futures import ThreadPoolExecutorimport json# ===================================================================# PART 1: 配置与函数定义# ===================================================================# --- 用户配置 ---# 1. 成为顾问的日期，也是 Alpha 开始计算收益的日期TOBE_CONSULTANT_DAY = "2025-04-14"# 2. 并发清除操作的线程数MAX_WORKERS = 10def up_alpha_properties_to_clear(s, alpha_id: str, old_osmosisPoints: str):    """    一个专门用于清除 Alpha 分数的函数。    它通过将 'osmosisPoints' 字段设置为 null 来实现。    """    params = {"osmosisPoints": None}  # 在 requests 中, None 会被序列化为 JSON null    response = s.patch(        f"[链接已屏蔽] json=params    )    if response.status_code == 200:        print(f"成功清除 Alpha {alpha_id} 的分数 (原分数: {old_osmosisPoints})。")        return "SUCCESS"    else:        print(f"清除 Alpha {alpha_id} 分数失败，状态码: {response.status_code}, 信息: {response.text}")        return "FAILED"def get_colored_alphas_in_date_range(s, start_date, end_date, alpha_num_limit=1000):    """    获取在指定日期范围内，所有设置了分数的常规 (non-SUPER) Alpha。    """    colored_alphas = []    print(f"开始查找从 {start_date} 到 {end_date} 所有已设置分数的常规 Alpha...")    for i in range(0, alpha_num_limit, 100):        print(f"正在扫描第 {i} 到 {i + 100} 个 alpha...")        # 【重要】在 URL 中加入了 dateSubmitted 过滤器        url_e = (            f"[链接已屏蔽]            f"&status!=UNSUBMITTED&status!=IS_FAIL&type!=SUPER&hidden=false"            f"&dateSubmitted>={start_date}T00:00:00-04:00"            f"&dateSubmitted<{end_date}T00:00:00-04:00"        )        try:            response = s.get(url_e)            response.raise_for_status()            alpha_list = response.json().get("results", [])            if not alpha_list:                print("已扫描完所有符合条件的 Alpha。")                break            # 在客户端筛选出有分数的 Alpha            for alpha in alpha_list:                if alpha.get("osmosisPoints") is not None:                    record = {                        "id": alpha["id"],                        "osmosisPoints": alpha["osmosisPoints"]                    }                    colored_alphas.append(record)        except Exception as e:            print(f"获取alpha时发生异常: {e}")            resp = s.get('[链接已屏蔽])            if resp.status_code != 200:                print(f"用户会话可能已过期，状态码: {resp.status_code}")            break    print(f"\n查找完毕！共找到 {len(colored_alphas)} 个在指定日期内需要清除分数的 Alpha。")    return colored_alphas# ===================================================================# PART 2: 主逻辑# ===================================================================if __name__ == "__main__":    s = login()    # --- 阶段一：计算日期范围 ---    begin_date = TOBE_CONSULTANT_DAY    end_date_obj = datetime.now() + timedelta(days=1)    end_date = end_date_obj.strftime("%Y-%m-%d")    print("-" * 50)    print("本脚本将查找并清除指定日期范围内的常规 Alpha 分数。")    print(f"顾问开始日 (脚本起始日期): {begin_date}")    print(f"脚本截止日期: {end_date}")    print("-" * 50)    # --- 阶段二：获取指定日期范围内带分数的 Alphas ---    alphas_to_clear = get_colored_alphas_in_date_range(s, begin_date, end_date)    if not alphas_to_clear:        print("在指定日期范围内未找到任何设置了分数的 Alpha，程序结束。")    else:        # --- 阶段三：并发清除分数 ---        print("\n准备开始清除分数...")        tasks = []        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:            for alpha_data in alphas_to_clear:                alpha_id = alpha_data["id"]                old_osmosisPoints = alpha_data["osmosisPoints"]                tasks.append(executor.submit(up_alpha_properties_to_clear, s, alpha_id, old_osmosisPoints))        # 等待所有任务完成并收集结果        results = [task.result() for task in tasks]        # --- 阶段四：打印总结报告 ---        print("\n" + "=" * 50)        print("所有分数清除任务已完成。")        success_count = results.count("SUCCESS")        failed_count = results.count("FAILED")        print(f"\n总结报告:")        print(f"- 成功清除分数的 Alpha 数量: {success_count}")        print(f"- 失败的任务数量: {failed_count}")        print("\n脚本执行完毕。")        print("=" * 50)
```


> [!NOTE] [图片 OCR 识别内容]
> C: |Users Iruanyanghui |AppData |Local |Programs | Python |Python312 Ipython.exe
> I:
> b'{"user": {"id":"顾问 顾问 JR23144 (Rank 6) (Rank 6)"} , "token" : {"expiry" : 86400.0}
> permissions
> [ "BEFORE
> 亏
> 过
> 本脚本将耷找并清除指定日期范围内的常规 Alpha 分数。
> 顾问开始日
> (脚本起始日期):
> 2025-04-14
> 脚本截止日期:
> 2025-12-18
> 开始耷找从
> 2025-04-14  到
> 2025-12-18
> 所有己设置分数的常规 Alpha
> 正在扫描第
> 0到  100
> alpha
> 正在扫描第
> 100  到
> 200
> alpha
> 正在扫描第
> 200  到
> 300
> alpha
> 正在扫描第
> 300  到
> 400
> alpha
> 正在扫描第  400  到
> 500
> alpha
> 正在扫描第
> 500  到
> 600
> alpha
> 正在扫描第
> 600  到
> 700
> alpha
> 己扫描完所有符合条件的
> Alpha:
> 耷找完毕!共找到
> 20  个在指定日期内需要清除分数的 Alpha。
> 淮备开始清除分数.
> 成功清除
> Alpha
> 的分数 (原分数:
> 3448).
> 成功清除 Alpha
> 哟分数
> (原分数:
> 10000).
> 成功清除 Alpha
> 的分数
> (原分数:
> 10000)
> HTTr喾压
> 17 nh3
> O5 
> C屑幺~
> 101000


---

### 帖子 #65: PnL = ∑(Robustness * Creativity)
- **主帖链接**: 【贺六浑】OpenClaw 快速安装与避坑指南代码优化.md
- **讨论数**: 17

### 💻 环境与系统要求

- **基础依赖** ：Node.js 22 及以上版本（如果使用下方的一键脚本，系统会自动检测并帮你安装）。
- **支持系统** ：macOS、Linux 或 Windows。
- **特别提醒** ：Windows 用户强烈建议在  **WSL2**  环境下进行安装和运行。

### 🛠️ 核心安装步骤

**👉 方式一：一键安装脚本（官方推荐，最省心）**  只需运行下面这行命令，脚本会自动搞定 Node 环境、下载安装包并引导你完成初始化配置。

- **macOS / Linux / WSL2 环境** ：
  Bash
  ```
  curl -fsSL [链接已屏蔽] | bash
  ```
- **Windows (PowerShell) 环境** ：
  PowerShell
  ```
  iwr -useb [链接已屏蔽] | iex
  ```

**👉 方式二：通过 npm 手动安装**  如果你电脑里已经装好了 Node 22+，并且喜欢自己掌控安装流程，可以直接全局安装：

Bash

```
npm install -g openclaw-cn@latest
openclaw-cn onboard --install-daemon

```

### ✅ 安装后验证

跑完安装流程后，在终端输入以下命令验证是否成功：

- `openclaw-cn doctor`  —— 自动检查环境和配置是否有隐患。
- `openclaw-cn status`  —— 查看当前网关的运行状态。
- `openclaw-cn dashboard`  —— 直接在浏览器中打开管理控制台。

### ⚠️ 常见排错与避坑

**1. 报错提示：找不到  `openclaw-cn`  命令**  这通常是因为 npm 的全局目录没在系统的  `$PATH`  环境变量里。

- **修复方法（macOS/Linux）** ：将  `export PATH="$(npm prefix -g)/bin:$PATH"`  添加到你的  `~/.zshrc`  或  `~/.bashrc`  文件中，然后重启终端。

**2. 使用 npm 安装时  `sharp`  构建失败？**  如果你之前用 Homebrew 装过全局的  `libvips`  可能会冲突，可以带上环境变量强制使用预构建包来安装：

Bash

```
SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw-cn@latest
```

---

### 帖子 #66: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【贺六浑】OpenClaw 快速安装与避坑指南代码优化_38909536551575.md
- **讨论数**: 17

### 💻 环境与系统要求

- **基础依赖** ：Node.js 22 及以上版本（如果使用下方的一键脚本，系统会自动检测并帮你安装）。
- **支持系统** ：macOS、Linux 或 Windows。
- **特别提醒** ：Windows 用户强烈建议在  **WSL2**  环境下进行安装和运行。

### 🛠️ 核心安装步骤

**👉 方式一：一键安装脚本（官方推荐，最省心）**  只需运行下面这行命令，脚本会自动搞定 Node 环境、下载安装包并引导你完成初始化配置。

- **macOS / Linux / WSL2 环境** ：
  Bash
  ```
  curl -fsSL [链接已屏蔽] | bash
  ```
- **Windows (PowerShell) 环境** ：
  PowerShell
  ```
  iwr -useb [链接已屏蔽] | iex
  ```

**👉 方式二：通过 npm 手动安装**  如果你电脑里已经装好了 Node 22+，并且喜欢自己掌控安装流程，可以直接全局安装：

Bash

```
npm install -g openclaw-cn@latest
openclaw-cn onboard --install-daemon

```

### ✅ 安装后验证

跑完安装流程后，在终端输入以下命令验证是否成功：

- `openclaw-cn doctor`  —— 自动检查环境和配置是否有隐患。
- `openclaw-cn status`  —— 查看当前网关的运行状态。
- `openclaw-cn dashboard`  —— 直接在浏览器中打开管理控制台。

### ⚠️ 常见排错与避坑

**1. 报错提示：找不到  `openclaw-cn`  命令**  这通常是因为 npm 的全局目录没在系统的  `$PATH`  环境变量里。

- **修复方法（macOS/Linux）** ：将  `export PATH="$(npm prefix -g)/bin:$PATH"`  添加到你的  `~/.zshrc`  或  `~/.bashrc`  文件中，然后重启终端。

**2. 使用 npm 安装时  `sharp`  构建失败？**  如果你之前用 Homebrew 装过全局的  `libvips`  可能会冲突，可以带上环境变量强制使用预构建包来安装：

Bash

```
SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw-cn@latest
```

---

### 帖子 #67: PnL = ∑(Robustness * Creativity)
- **主帖链接**: 【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享.md
- **讨论数**: 32

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

---

### 帖子 #68: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享_38927243023383.md
- **讨论数**: 32

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

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《04.【永久置顶】高Value Factor顾问分享合集，赚钱必读！(更新1029）置顶的经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 04【永久置顶】高Value Factor顾问分享合集赚钱必读更新1029置顶的经验分享_32032776365079.md
- **评论时间**: 1年前

现在是追求高的fitness的，还是要追求原子性 交的都是atom这些单数据字段的alpha，交原子性的alpha 感觉fitness 都不会高，上次听到说，数据字段和操作符多的，虽然fitness 高，但是os 爆炸性降低的比比皆是，反而atom 的alpha，表现都不会差，是这样吗

---

### 探讨 #2: 关于《25Q3顾问提交情况播报（每日更新）》的评论回复
- **帖子链接**: [Commented] 25Q3顾问提交情况播报每日更新.md
- **评论时间**: 1年前

25年Q3赛季一开始，就竞争这么激烈的吗 作为萌新瑟瑟发抖 每天能有 2050 个人来提交alpha ,这也太恐怖了，加油啊！
================================VF 1.0========================================

---

### 探讨 #3: 关于《25Q3顾问提交情况播报（每日更新）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 25Q3顾问提交情况播报每日更新_33266491538199.md
- **评论时间**: 1年前

25年Q3赛季一开始，就竞争这么激烈的吗 作为萌新瑟瑟发抖 每天能有 2050 个人来提交alpha ,这也太恐怖了，加油啊！
================================VF 1.0========================================

---

### 探讨 #4: 关于《4个月内升到master以及获得三个比赛奖项的经验分享经验分享》的评论回复
- **帖子链接**: [Commented] 4个月内升到master以及获得三个比赛奖项的经验分享经验分享.md
- **评论时间**: 1年前

非常有价值的干货分享，感谢鼠鼠大佬！特别是你关于IS/OS的思考、PPAC的经验，以及HCAC的SA策略，都非常具体且有启发性。看到你如何从早期PC相关性的困境中走出来，并找到适合自己的方法，真的给了我很多信心。恭喜荣升Master！你的成功证明了坚持和正确的方法论是多么重要。向你学习！

---

### 探讨 #5: 关于《4个月内升到master以及获得三个比赛奖项的经验分享经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 4个月内升到master以及获得三个比赛奖项的经验分享经验分享_33438282558999.md
- **评论时间**: 1年前

非常有价值的干货分享，感谢鼠鼠大佬！特别是你关于IS/OS的思考、PPAC的经验，以及HCAC的SA策略，都非常具体且有启发性。看到你如何从早期PC相关性的困境中走出来，并找到适合自己的方法，真的给了我很多信心。恭喜荣升Master！你的成功证明了坚持和正确的方法论是多么重要。向你学习！

---

### 探讨 #6: 关于《About slots of Genius competitions》的评论回复
- **帖子链接**: [Commented] About slots of Genius competitions.md
- **评论时间**: 1年前

（黄金级 70%，专家级 20%，大师级 8%，宗师级 2%） 不过，需要注意的是，只有符合季度付款条件的顾问才会被考虑，也就是 交了 20天alpha 的人才算在里面 那这个感觉本赛季 genius 挤进600名才能到 expert 呀

---

### 探讨 #7: 关于《About slots of Genius competitions》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] About slots of Genius competitions_28646715513495.md
- **评论时间**: 1年前

（黄金级 70%，专家级 20%，大师级 8%，宗师级 2%） 不过，需要注意的是，只有符合季度付款条件的顾问才会被考虑，也就是 交了 20天alpha 的人才算在里面 那这个感觉本赛季 genius 挤进600名才能到 expert 呀

---

### 探讨 #8: 关于《alpha 模拟高效篇》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] alpha 模拟高效篇_33036460396567.md
- **评论时间**: 1年前

大佬真是咸鱼翻身的典范啊！靠邮件才启动回测，现在靠自己搞出一套超高效的异步队列+任务调度体系，效率直接飞起，8个并发一天轻松跑6644个，还能保证每天提交4个alpha，简直不要太猛， 萌新目前一天只能提交1个，有时候还会断粮，羡慕大佬呀

---

### 探讨 #9: 关于《Combined Power Pool Alpha Performance Now Counts to Genius Level》的评论回复
- **帖子链接**: [Commented] Combined Power Pool Alpha Performance Now Counts to Genius Level.md
- **评论时间**: 11个月前

Thanks for kicking off this important discussion,  [AK40989](/hc/en-us/profiles/26422151767703-AK40989)    . For me, the new Combined Power Pool Alpha Performance was a pleasant surprise and actually ended up being the highest of my three scores. It seems my more experimental alphas, which I had tagged for the Power Pool, collectively performed better than expected. This definitely makes me reconsider my tagging strategy for the next quarter, perhaps allocating more diverse ideas to the pool.

---

### 探讨 #10: 关于《Combined Power Pool Alpha Performance Now Counts to Genius Level》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Combined Power Pool Alpha Performance Now Counts to Genius Level_33317801710615.md
- **评论时间**: 0年前

Thanks for kicking off this important discussion,  [AK40989](/hc/en-us/profiles/26422151767703-AK40989)    . For me, the new Combined Power Pool Alpha Performance was a pleasant surprise and actually ended up being the highest of my three scores. It seems my more experimental alphas, which I had tagged for the Power Pool, collectively performed better than expected. This definitely makes me reconsider my tagging strategy for the next quarter, perhaps allocating more diverse ideas to the pool.

---

### 探讨 #11: 关于《Genius Tier Refresh - Congrats to All!》的评论回复
- **帖子链接**: [Commented] Genius Tier Refresh - Congrats to All.md
- **评论时间**: 1年前

Great to see the updated distribution! Seeing nearly 8,000 consultants across these top tiers is incredibly motivating. Congratulations to all, especially the 59 Grandmasters who set a high bar for us to aspire to. Welcome to the IQC newcomers. Let's make this a quarter of significant growth and alpha!

---

### 探讨 #12: 关于《Genius Tier Refresh - Congrats to All!》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Genius Tier Refresh - Congrats to All_33373547911191.md
- **评论时间**: 1年前

Great to see the updated distribution! Seeing nearly 8,000 consultants across these top tiers is incredibly motivating. Congratulations to all, especially the 59 Grandmasters who set a high bar for us to aspire to. Welcome to the IQC newcomers. Let's make this a quarter of significant growth and alpha!

---

### 探讨 #13: 关于《Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一》的评论回复
- **帖子链接**: [Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一.md
- **评论时间**: 1年前

写的好棒呀，小菜鸡的我，终于看懂了

---

### 探讨 #14: 关于《Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一_27789509613335.md
- **评论时间**: 1年前

写的好棒呀，小菜鸡的我，终于看懂了

---

### 探讨 #15: 关于《PPA活动主题限制下，提交ra点塔的一点心得。》的评论回复
- **帖子链接**: [Commented] PPA活动主题限制下提交ra点塔的一点心得.md
- **评论时间**: 3个月前

新人也太强了吧，学习到了，想请教下新人大佬 
比如说

- [Weight concentration](/hc/en-us/articles/19248385997719)   **37.74%**  is above cutoff of  **10%**  on  **1/7/2015** .
  这种警告怎么解决呢，有这些对于因子是否能实盘是很有影响的，不知道大佬有什么好的解决方案”
  ==========================VF 1.0=====================================
  ==========================贺六浑=====================================

---

### 探讨 #16: 关于《PPA活动主题限制下，提交ra点塔的一点心得。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] PPA活动主题限制下提交ra点塔的一点心得_38121310515223.md
- **评论时间**: 3个月前

新人也太强了吧，学习到了，想请教下新人大佬 
比如说

- [Weight concentration](/hc/en-us/articles/19248385997719)   **37.74%**  is above cutoff of  **10%**  on  **1/7/2015** .
  这种警告怎么解决呢，有这些对于因子是否能实盘是很有影响的，不知道大佬有什么好的解决方案”
  ==========================VF 1.0=====================================
  ==========================贺六浑=====================================

---

### 探讨 #17: 关于《In RAM neutralization, these factors are statistically identified and stripped from signals or portfolios using regression or optimization. This helps avoid unintended exposure to behavioral biases and market regimes, making strategies more robust and focused on non-RAM sources of return.》的评论回复
- **帖子链接**: [Commented] RAM Neutralization.md
- **评论时间**: 1年前

Oh man, I just found out about the 2X multiplier for the RAM Neutralization Theme today, June 19th! With it ending on the 22nd, I've basically missed most of it. Such a shame I didn't see this sooner, haha!

---

### 探讨 #18: 关于《In RAM neutralization, these factors are statistically identified and stripped from signals or portfolios using regression or optimization. This helps avoid unintended exposure to behavioral biases and market regimes, making strategies more robust and focused on non-RAM sources of return.》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] RAM Neutralization_32734733402903.md
- **评论时间**: 1年前

Oh man, I just found out about the 2X multiplier for the RAM Neutralization Theme today, June 19th! With it ending on the 22nd, I've basically missed most of it. Such a shame I didn't see this sooner, haha!

---

### 探讨 #19: 关于《SA日入50刀，如何把握好SuperAlphaCompetition经验分享》的评论回复
- **帖子链接**: [Commented] SA日入50刀如何把握好SuperAlphaCompetition经验分享.md
- **评论时间**: 1年前

​​感谢楼主分享，所以我们要利用6月赛事资源解锁权限，通过PC优化（<0.5）快速提升Base收益，同时借提升计划夯实策略稳定性​​。优先参与PPAC排名（复用历史Alpha）和Super Alpha周赛（限时GM权限），结合一些大佬分享的想法来优化PC

---

### 探讨 #20: 关于《SA日入50刀，如何把握好SuperAlphaCompetition经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] SA日入50刀如何把握好SuperAlphaCompetition经验分享_32630124449559.md
- **评论时间**: 1年前

​​感谢楼主分享，所以我们要利用6月赛事资源解锁权限，通过PC优化（<0.5）快速提升Base收益，同时借提升计划夯实策略稳定性​​。优先参与PPAC排名（复用历史Alpha）和Super Alpha周赛（限时GM权限），结合一些大佬分享的想法来优化PC

---

### 探讨 #21: 关于《Super Alpha：使用代码批量过滤failed以及prod corr检查 --开箱即用，筛选大提速🚀代码优化》的评论回复
- **帖子链接**: [Commented] Super Alpha使用代码批量过滤failed以及prod corr检查 --开箱即用筛选大提速代码优化.md
- **评论时间**: 1年前

为使用Super alpha全自动回测代码的顾问提供了有价值的补充。通过结合代码和WQ API，实现了对Super alpha的批量获取和筛选，尤其是能过滤掉含有fail项的alpha，专注于IS pass的alpha，并进一步获取其prod corr，这对于提高提交效率和质量非常有帮助。分享的成果数据展示了这一方法的有效性，特别是对于追求高VF和顶格base的顾问来说，具有很大的吸引力。感谢大佬的分享，祝所有顾问都能取得更好的成果

---

### 探讨 #22: 关于《Super Alpha：使用代码批量过滤failed以及prod corr检查 --开箱即用，筛选大提速🚀代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Super Alpha使用代码批量过滤failed以及prod corr检查 --开箱即用筛选大提速代码优化_32866010519831.md
- **评论时间**: 1年前

为使用Super alpha全自动回测代码的顾问提供了有价值的补充。通过结合代码和WQ API，实现了对Super alpha的批量获取和筛选，尤其是能过滤掉含有fail项的alpha，专注于IS pass的alpha，并进一步获取其prod corr，这对于提高提交效率和质量非常有帮助。分享的成果数据展示了这一方法的有效性，特别是对于追求高VF和顶格base的顾问来说，具有很大的吸引力。感谢大佬的分享，祝所有顾问都能取得更好的成果

---

### 探讨 #23: 关于《Vscode自动提示operator代码优化》的评论回复
- **帖子链接**: [Commented] Vscode自动提示operator代码优化.md
- **评论时间**: 1年前

大佬厉害呀，这个vs code 插件很好用，以后写代码，就不用去翻网页，直接在vs code 中就可以写了

===================================== VF1.0 ========================================

---

### 探讨 #24: 关于《Vscode自动提示operator代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Vscode自动提示operator代码优化_33274404140439.md
- **评论时间**: 1年前

大佬厉害呀，这个vs code 插件很好用，以后写代码，就不用去翻网页，直接在vs code 中就可以写了

===================================== VF1.0 ========================================

---

### 探讨 #25: 关于《【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化》的评论回复
- **帖子链接**: [Commented] 【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化.md
- **评论时间**: 1年前

感谢 橙子姐 的无私分享，我的SA 还在直接去服务器请求 生产相关性，有了大佬的代码后，提供了非常好的思路，先去检查本地相关性，再去服务器校验生产相关性 厉害呀

===============VF 1.0 ================================================

---

### 探讨 #26: 关于《【 SA赚钱大法 】怎么快速找到有可能降低prod到0.5以下的sa进行调整代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【 SA赚钱大法 】怎么快速找到有可能降低prod到05以下的sa进行调整代码优化_32763493267863.md
- **评论时间**: 1年前

感谢 橙子姐 的无私分享，我的SA 还在直接去服务器请求 生产相关性，有了大佬的代码后，提供了非常好的思路，先去检查本地相关性，再去服务器校验生产相关性 厉害呀

===============VF 1.0 ================================================

---

### 探讨 #27: 关于《【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **评论时间**: 11个月前

### 基于oth455 网络因子差值动量模板

**模板**

<ts_operator_op/> ( <oth455_xxxx_fact1_value/> <math_op/> <oth455_xxxx_fact2_value/>,<days_op/>)

**1. 模板中的变量使用< />进行了声明，总共五个变量。**

**具体变量1：<ts_operator_op/> 可以是** ts_rank, ts_zscore, ts_delta, ts_sum, ts_delay, ts_std_dev, ts_mean, ts_arg_min, ts_arg_max, ts_scale, ts_quantile  等

**具体变量2：<oth455_xxxx_fact1_value/> 可以是** oth455_relation_roam_w3_pca_fact1_value, oth455_relation_roam_w4_pca_fact1_value, oth455_relation_roam_w5_pca_fact1_value, oth455_partner_roam_w5_pca_fact1_value 等

**具体变量3：<math_op/> 可以是** + ，-，* , / 等

**具体变量4：<oth455_xxxx_fact2_value/> 可以是** oth455_relation_roam_w3_pca_fact2_value, oth455_relation_roam_w4_pca_fact2_value, oth455_relation_roam_w5_pca_fact2_value, oth455_partner_roam_w5_pca_fact2_value 等

**具体变量5：<days_op/> 可以是** 20,60,120,240 等

**2. 搜索空间的大小**

以oth455数据集为例，因子配对（如fact1-fact2, fact1- fact3, fact2-fact3,fact1* fact2）有3种核心组合。数据集本身有约11 **(时间序列算子）**  * 4 **(数学运算)**  * 300 ****(基础设定)****  = 13,200 种不同的“关系-算法-窗口”基础设定 。 数据量非常大，有巨大的挖掘潜力 。

**3. 模板的idea，implement细节（即哪步是数据处理，哪步是主信号）**

- **Idea** : oth455的PCA因子（fact1, fact2, fact3）捕捉了公司在关系网络中不同层面的特征。fact1通常代表“主流/规模”特征，而fact2、fact3代表更“小众/特色”的特征。本模板的核心思想是，通过计算不同因子间的 **差值或比率** ，来寻找网络地位**“失衡” **的公司，例如那些“主流地位”不强但“特色地位”突出的“隐形冠军”。然后，通过时间序列算子捕捉这种“失衡”特征的** 持续性或变化动量**。
- **Implement细节** :
  - **<oth455_xxxx_fact1_value/> <math_op/> <oth455_xxxx_fact2_value/>;**   这是 **数据处理** 步骤。它将两个独立的网络因子合成为一个具有更清晰经济学意义的“差值”信号。
  - **<ts_operator_op/>(factor_difference, <days_op/>)**  这是 **主信号生成** 步骤。它作用于处理后的“差值”信号，将其转化为一个捕捉长期累积效应（如ts_sum）或短期变化趋势（如ts_delta）的最终Alpha。

**4. 产出效果**

EUR 市场中 Other模块 **乘数** 是 **最高** 的，不过也是能找到很多alpha的。给大家展示一个提交了的alpha，使用 ts_sum(oth455_xxxx_fact2_value - oth455_xxxx_fact1_value, 240) 这个具体表达式，从附图的回测结果看，虽然Fitness为0.6，还有提升空间，但其有0.07 的margin 并且operator 少，还有Risk neutralized 也是紧贴着的所以我交了。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> ts_SUm(oth455
> factz_Value
> oth455
> factI
> Value
> 240)
> 眈 Single Data Ser Mlpha
> M Power Pool Alpha
> Pyramid theme: EURIDIIOTHER Y.7
> Aggregate Data
> SArCe
> LUTCIe
> TIIe
> ReUTI
> LTaIOO
> NIreIr
> Simulation Settings
> 1.01
> 1.15%
> 0.60
> 4.42%
> 4.49%
> 76.7
> 900
> Instrument Type
> Region
> Unlerse
> Langwage
> Decay
> Delay
> Trncation
> Neutraliation
> Pastewriation
> NaN Handling
> Unt Handling
> TaTrade
> Equity
> EUR
> TCF2507
> ExprEssion
> D.JE
> Subindustry
> Werf
> Vear
> Sharpe
> Tumower
> Ftness
> Rehrs
> Dowdown
> Long Count
> Shrt Count
> 2013
> .353
> 357
> 201沾
> 5E.39
> 30
> 13JE
> 2014
> D.Js
> 1.173
> 0.02
> .41
> 2.84沾
> 7.549
> T1
> Clone Alpha
> 2015
> 0.35
> 633
> 0.4
> 153
> 4.00
> 131.3
> ZOIE
> 0.21
> 0.7096
> OOE
> D.S5
> 4.4s汩
> 2.1293
> 1732
> 2017
> 1.72
> 0.7595
> 1.13
> 508
> 1.734
> So
> 1316
> 1135
> N Chart
> PIL
> 2018
> .973
> 0.07
> 3.57
> 4.05沾
> 12.704
> 1306
> 112E
> 2015
> 187
> DZE
> {3:
> 2.08沾
> -.-32
> 1715
> 1115
> 2020
> 0.3
> 059
> O.EE
> SED
> 3.34沾
> T
> 15_
> 1033
> 2021
> 333
> DE
> 53:
> 2.5汩
> 0193
> 13E
> 1571
> 03JK
> 2022
> 35
> 2.7
> 10.39
> e汩
> 151.37
> 112
> 1777
> 2,00OK
> 2023
> .773
> 15.52
> 0.60治
> 413.59
> 1172
> 1535
> 03JK
> Risk neutralized
> Aggregate Data
> SrDe
> LUTOET
> CTS
> RUUTS
> CaOC
> Ir3IT
> 1.05
> 1.159
> 0.50
> 2.88%
> 3.209
> 49.909600
> J37"14
> Jan'15
> Jan'16
> Jan '17
> Jan'18
> Jan '19
> Jan '20
> Jan '21
> J30'22
> J3n'23
> Wrgin


**5. 建议其他顾问未来尝试的探索方向**

1. **系统性挖掘** : 全面遍历我上面提到的 <ts_operator_op/> ， <oth455_xxxx_fact1_value/> ，<math_op/> ，<oth455_xxxx_fact2_value/>，<days_op/>的组合，大概率能发现比我这个ts_sum版本表现更优的Alpha。
2. **构建二阶Alpha 三阶Alpha** : 这个模板产出的信号还是有的，非常适合作为**“基石”或“风控”因子**。可以该模板去套培训用的二阶三阶模版，相信也是会有更好表现的。
3. **跨关系比较** : 我模板中比较的是同一关系内的fact1和fact2。一个更有趣的方向是进行 **跨关系比较** ，例如 customer_fact1 - competitor_fact1，这可以构建一个衡量公司“网络护城河”的强大信号。

---

### 探讨 #28: 关于《如果所有重试都失败》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【alpha 高并发429处理篇】代码优化_33247831520791.md
- **评论时间**: 1年前

看到分层延迟和JitterType.FULL我就跪了——这才是真正抗并发洪水的设计啊！之前自己瞎写sleep(random())简直弟弟。断路器整合进HTTP客户端这个操作也帅，比裸调API优雅多了。不过好奇自适应因子_apply_adaptive_factor的实际数据反馈，成功率波动大时延迟跳变会明显吗？另：retry_after合理性校验那行细节拉满，防止恶意服务器这思路学到了

---

### 探讨 #29: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template.md
- **评论时间**: 8个月前

可以呀，竟然还可以这么做，我在Expert 的时候，好像都没有注意到这个操作符，现在用些数据集，来复现这个模板，跑出来，再来感谢楼主

=====================================VF1.0====================================================================================================================

---

### 探讨 #30: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template_35294898626711.md
- **评论时间**: 8个月前

可以呀，竟然还可以这么做，我在Expert 的时候，好像都没有注意到这个操作符，现在用些数据集，来复现这个模板，跑出来，再来感谢楼主

=====================================VF1.0====================================================================================================================

---

### 探讨 #31: 关于《【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享》的评论回复
- **帖子链接**: [Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享.md
- **评论时间**: 1年前

感谢大佬分享，连续几天都是 60$  ，顶格收益让人羡慕不已，原来认为 主要是要 提高 fitness 和 shape ，降低Prod Correlation , 现在可以试试游戏王大佬分享的 turnover 分层思想

====================================VF 1.0===========================================

---

### 探讨 #32: 关于《【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享_33316845356439.md
- **评论时间**: 1年前

感谢大佬分享，连续几天都是 60$  ，顶格收益让人羡慕不已，原来认为 主要是要 提高 fitness 和 shape ，降低Prod Correlation , 现在可以试试游戏王大佬分享的 turnover 分层思想

====================================VF 1.0===========================================

---

### 探讨 #33: 关于《【代码优化】解决429报错的方法》的评论回复
- **帖子链接**: [Commented] 【代码优化】解决429报错的方法.md
- **评论时间**: 1年前

wqb 在10* 10 回测的时候，为啥没有打印出 回测进度

---

### 探讨 #34: 关于《【代码优化】解决429报错的方法》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【代码优化】解决429报错的方法_32183460328087.md
- **评论时间**: 1年前

wqb 在10* 10 回测的时候，为啥没有打印出 回测进度

---

### 探讨 #35: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【新人心魔】打破心魔之旅这样的因子到底要不要交经验分享.md
- **评论时间**: 2个月前

详细的拜读了大佬的帖子，发现大佬一再强调  margin 的重要 性，可是最近在跑的

SLOW_AND_FAST  中性化中 ，能做到 margin > 10/10000 的寥寥无几 等同于没有，还有就是在 换手率 高的情况下 ，margin 大于万分之十 也是很少的，当然 一些大佬可能都做到了，最近几个月我放开了 margin 的提交标准，这也许是我最近 VF  下降的 原因吧。祈祷下一次VF 更新 回升 。

=================================VF 1.0====================================

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【新人心魔】打破心魔之旅这样的因子到底要不要交经验分享_39759058734359.md
- **评论时间**: 2个月前

详细的拜读了大佬的帖子，发现大佬一再强调  margin 的重要 性，可是最近在跑的

SLOW_AND_FAST  中性化中 ，能做到 margin > 10/10000 的寥寥无几 等同于没有，还有就是在 换手率 高的情况下 ，margin 大于万分之十 也是很少的，当然 一些大佬可能都做到了，最近几个月我放开了 margin 的提交标准，这也许是我最近 VF  下降的 原因吧。祈祷下一次VF 更新 回升 。

=================================VF 1.0====================================

---

### 探讨 #37: 关于《【新人指南】SA 从入门到进阶，使用 ACE 工具构建与回测 SuperAlpha：代码实战指南论坛精选》的评论回复
- **帖子链接**: [Commented] 【新人指南】SA 从入门到进阶使用 ACE 工具构建与回测 SuperAlpha代码实战指南论坛精选.md
- **评论时间**: 1年前

厉害呢 学到了

---

### 探讨 #38: 关于《【新人指南】SA 从入门到进阶，使用 ACE 工具构建与回测 SuperAlpha：代码实战指南论坛精选》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【新人指南】SA 从入门到进阶使用 ACE 工具构建与回测 SuperAlpha代码实战指南论坛精选_32628718991639.md
- **评论时间**: 1年前

厉害呢 学到了

---

### 探讨 #39: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025年7月12日，天晴气清 本赛季我第三次写量化日记，

现在每天一睁眼 就是world quant 启动，梦里也是找寻因子。

内心中有野兽咆哮一般汹涌的声音==============================

三天点两塔，怒冲GM ！！！

三天点两塔，怒冲GM ！！！

三天点两塔，怒冲GM ！！！

---

### 探讨 #40: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 11个月前

2025年7月29日，天晴气清，昨天提交了一个花了1天半，熬夜到2点第二天继续修得到的三 5 alpha  40$,,今天花了一小时调试了not own alpha,又是踩线过。继续加油！！！ 
> [!NOTE] [图片 OCR 识别内容]
> Self Correlation
> NatmUm
> UIIMUII
> 0.4099
> -0.0411
> Prod Correlation
> TsTIm
> LTTII
> 0.4981
> -0.6157
> TOOI
> 4
> 1OK
 =======================VF 1======================================

---

### 探讨 #41: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年7月31日，深夜改bug ,调试 SA ，
今日看到了 一些大佬发的文章，vf 要提升多做atom ，少做d0，我翻了翻我6月交了3个EUR d0 ，等8月更新vf 怕是要炸了
=====================================VF 1.0=====================================

---

### 探讨 #42: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月1日，天气炎热，今天看了下 把EUR 和GLB 点的差不多了，先在开始弄 USA 的 了，要冲击GM 真的还有好多塔要点，加油
=====================================================================================================================VF 1.0===========================================

---

### 探讨 #43: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月4日，天气炎热
这两天从 EUR 和GLB 切区切到了 USA 和ASI 由于 之前 USA 和ASI 跑过大量的alpha ,导致现在跑出来的alpha 全部都有自相关问题，交不上去，即使是ppa 的也交不上去，导致这两天已经断粮了，要继续用新的模版来跑了
======================================VF 1.0 ===================================

---

### 探讨 #44: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月5日，天气炎热
每天都要写日记，昨天在12点前第一次 交满了 4+1 个alpha ，不过看genius 排名又掉了4名，看来竞争是异常激烈呀，这个星期 跑USA D1 的 anylst ,跑出来全是自相关比较高的数据，很头疼，还是要继续努力，大家都要加油哦

================================VF 1.0===========================================

---

### 探讨 #45: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月7日 ,每天都要写日记，和上班一样写日报

跑了 三天 ASI 的 erning  根本跑不出货呀，但是看到字段上的alpha 数量还都是很多的，不着调大家是怎么点掉这座塔的，继续加油，combine 更新出来 千万不要蹦呀，为了点塔交了不少的差的alpha。也不是说质量差吧，就是说表现一般般的那种
==================================VF 1.0==========================================

---

### 探讨 #46: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月8日 每天都要写日记

昨天只交了一个RA 和一个SA ，SA  own 的三五真的太难组出来了，调试了一上午，根本就出不来，SA 的own 还是 叫 双五吧， not  own 来组三五，昨天 combine 更新，提升了一些， VF 应该也会马上更，祈祷不要降低呀

===================================================================================================VF 1.0=====================================================

---

### 探讨 #47: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月9日 天气 炎热  
从前天开始我的EUR再也组不出 三五 的SA 了， 看来是要换区了，我再试试今晚还是组不出来，我就换别的区去试一试 。

==========================================================================================================VF 1.0================================================

---

### 探讨 #48: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月10日 终于点完了master 要点的塔了，还有30座要点 ，SA 现在断粮了太难受了，根本跑不出好的，USA 跑出来 ，sharpe 巨低， 根本不敢看，GLB  的 SA 跑出来直接报错了，EUR 跑出来的 全是高相关性。乖乖 这可怎么玩。 继续加油  早日GM！！！
=================================================================================================VF1.0========================================================

---

### 探讨 #49: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月11日，今日来跑usa 的model 数据集，发现跑出来的好差劲呀，不是那啥相关性太高，就是pnl 的曲线不好看，要么就是 fitness sharpe margin 拉胯 ，这个数据集跑了有三四天了 =====================================================================================================VF1.0=================================================================

---

### 探讨 #50: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年08月12日/星期三，窗外大雨连绵，我找因子中，发现glb 比赛满足这个要求的因子太难找了，要么跑出来后那个margin 太低了，这可怎么办，并且上个月已经点了glb 很多塔了，真的是把glb 做的很难受，算了还是先点塔吧===============================================================================================================VF 1.0=========================================

---

### 探讨 #51: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月13日，今天早上睡到个8点起来，结果发现自己的程序卡段了，浪费了一晚上没跑，太可惜了，于是乎，今天真的断粮了，昨天弄了USA 的 Macro ，硬是没找到一个可以提交的，太难受了，一直没跑出，就一直弄，不过还是继续加油吧 ===========================================================================================================VF 1.0=============================================

---

### 探讨 #52: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月14日，天气炎热   Q3季度已经过去45天，过半了发现后面30座塔会比前面30座塔难点太多了，实在是不知道是否可以点完，不过还是继续加油，看大家都在很努力的交因子，glb 的塔很难点，还是暂时不参加了，安心做genius   ==================================================VF1.0===============================================

---

### 探讨 #53: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月15日，天气炎热，发现后面30座塔，比前面30座难的不是一星半点，点起来太痛苦了，哈哈哈，最近own 的SA 又断粮了，不过换新的模板去跑，也期待出些货 总之继续加油，再接再厉 ============================================================================================VF 1.0=======================================================================

---

### 探讨 #54: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月17日，JR 的量化日记，天气炎热 昨天到今天早上一个都没跑出来， USA D1  news   ,这个数据集好烦呀，还有一个多小时，赶紧再调一调，看看可不可以弄一个出来，大佬们的塔 都点47  48 座了，都是冲 GM 的高手，我还是和大佬们有很大的差距的 =========================================================================================================VF 1.0==============================================

---

### 探讨 #55: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月18日，我的量化日记，昨天只交了一个RA 和一个SA ，然后发现今天的base 变少了一点， 感觉 从0.95 -> 0,9 左右，应该是6月为了点塔交了点垃圾的因子导致的，不过今天还发现 ASI 的要有乘数 必须那啥 alpha 还要同时满足RA 标准才有 ，这就有点那啥了

===============================VF 1.0===============================================

---

### 探讨 #56: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月19日，我的量化日记，天气炎热，VF 更新了 0.95 -> 0.93 ,不知道是交了d0 的缘故还是什么原因，让我的VF 变低了，不过也还行，要继续努力了。==================================================================================================================VF 1.0===========================

---

### 探讨 #57: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月20日，我的量化日记，天气炎热，今天和昨天跑了 USA d1 的 risk 和 ASI 的short interest 发现这两个好难出货呀，都快搞断粮了咯，根本点不动这个塔呀，不知道其他大佬是怎么点的这个塔 =================================VF 1.0 =======================================================================================

---

### 探讨 #58: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月22日，我的量化日记，天气炎热，一些大佬真的很厉害，塔已经点完60座了，我发现后面的塔是真的难点，根本点不动，跑了几天总是出不了货，自信心都被打击没了，不过还是要继续加油 ========================================================================================VF1.0========================================================================================================

---

### 探讨 #59: 关于《【日常生活贴】我的量化日记第三季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **评论时间**: 10个月前

2025年8月30日，我的量化日记，已经好久没写日记了，昨天3 五alpha 刷新了历史新低，竟然只有9$,平时应该都有 30+ ,感觉大家都在玩乘数，自己不玩好吃亏呀。打不过就加入

==================================VF 1.0========================= =================================================================

---

### 探讨 #60: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第二季.md
- **评论时间**: 1 year ago

News 数据集 回测 怎么很容易抛出   Your simulation probably took too much resource.  有没有大神遇见过，解答一下

---

### 探讨 #61: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第二季.md
- **评论时间**: 1 year ago

去年12 月注册了 WorldQuant 账号，今年 4 月成为了 consultant。目前顾问阶段的 alpha已交了100 个，赛季临近尾声，我希望本赛季拿到 expert 段位。尽管在优化 alpha 质量、提升 VF 值方面遇到了一些瓶颈，但我相信只要保持积极的心态、不断学习改进，就一定会有进步。接下来，我会更加深入地研究数据、创新模板、学习社区经验，努力突破瓶颈，向着更高的目标冲刺

---

### 探讨 #62: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

News 数据集 回测 怎么很容易抛出   Your simulation probably took too much resource.  有没有大神遇见过，解答一下

---

### 探讨 #63: 关于《【日常生活贴】我的量化日记第二季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **评论时间**: 1年前

去年12 月注册了 WorldQuant 账号，今年 4 月成为了 consultant。目前顾问阶段的 alpha已交了100 个，赛季临近尾声，我希望本赛季拿到 expert 段位。尽管在优化 alpha 质量、提升 VF 值方面遇到了一些瓶颈，但我相信只要保持积极的心态、不断学习改进，就一定会有进步。接下来，我会更加深入地研究数据、创新模板、学习社区经验，努力突破瓶颈，向着更高的目标冲刺

---

### 探讨 #64: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025年10月12日， 今日天气凉爽， 昨天交了3+1 ，收入 91$ ,glb 还是比较难做的，到今天晚上12点仍然没跑出一个 ，太难了，等到USA 有乘数 应该会好点了

==============================VF1.0============================================================================================

---

### 探讨 #65: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

10.14 ,天气已经凉爽了起来了，base 结算 只有平时一半，昨天出去玩了，没得时间搞，只弄了1个ra（pc0.69） 和一个sa ,导致base 平时低一些 ，还是要继续努力，

今天有个发现  ts_operate(xxx,1)  和 xxx 并不等效，

`ts_operate(xxx,1)`  与  `xxx`  在纸面上等价，但 WorldQuant 的 **NaN 处理、算子标签、warm-up 规则** 会让它们走 **不同的执行路径** ，最终回测效果出现偏差。

================================================VF 1.0================================== =========================================

---

### 探讨 #66: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

由于没跑 小地区，在跑 高pc 的USA 地区 ，pc 拉不下来的，0.55 的10月平均pc 就不要再想了，保住 0.65 以下就可以了，现在感觉每天base 都在下降，可能是由于没交到好的alpha 吧， 继续加油！！！

=============================VF1.0===============================================================================================================

---

### 探讨 #67: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

25年10月19日，天气慢慢寒冷了下来，昨天交了3个 0.6pc 和一个0.8+ pc 的RA ，结果发现base 不如只交2个pc <0.7 的多，看来还是不能交超过0.7pc 的，不然就没啥base了 ，继续加油！！！

====================================VF 1.0=========================================

==================================================================================

---

### 探讨 #68: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

25年10月20日，空气中有着浓浓的冬天味道，昨日提交 了4个RA 和1个SA ，base 可能还是没有之前的多，可能是usa 的alpha 好做吧，base 稍低一些，今天中午开始，回测不了一点更加难受了，继续加油！！！

=============================VF 1.0=============================================

================================================================================

---

### 探讨 #69: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025年10月23日，今天罕见的交完了4+1 个alpha 等待12点过后看下base 多少，感觉最近的无论是RA  还是SA base 都少了一些，不知道是怎么回事，还有VF 还没有更， 9 月份为了点塔 交的质量一般，不知道VF 更完会是什么情况 ， 继续加油！！！！

=============================VF 1.0================================================

===============================================================================

---

### 探讨 #70: 关于《【日常生活贴】我的量化日记第五季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **评论时间**: 8个月前

2025.10.28
VF 更新后来到了0.97 ，发现更完 base 少了13- 14 $ ,原来交3五就能50刀左右的好日子一去不复返了，现在要虚心向大家学习，如何做出553alpha ，继续加油！！！

===============================VF 1.0=======================================

===========================================================================

---

### 探讨 #71: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

2025 11月12日

昨天交了一个fitness 3.01 pc 0.4 的IND 区域的因子，只交了这么一个RA ，第二天更base 发现 37$ ,比平时多了不少，看来还是要交高fitness 低pc 的 ,继续加油！！！

=================================VF 1.0===================================

===============================================================

---

### 探讨 #72: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

25.11.21 天晴气清

VF 更新后来到了 0.85 比之前0.97 base 少了很多，一时有些不知道咋说，可能是交的不够分散吧，9月份的时候，也许是成长因子给用完了，总之还是要继续看下怎么改进自己的模式，让VF 加回来。！！！

==============================VF 1.0=============================================

========================================================================

---

### 探讨 #73: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **评论时间**: 7个月前

25.11.24 温暖的冬日 昨日交了印度的一个因子后再难点了，还是换个区继续做吧，昨日base 远远不如 之前高啊，还是要继续努力 ！！！

==============================VF 1.0============================================= ===============================================================================

---

### 探讨 #74: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

2026 03 02  昨天交2RA 1SA base 13，啊这os 系数真的很头疼啊，分数上不去难受，得找机会重新分配os 分数了 ，加油！！！！
  ==========================VF 1.0================================== ================================================================...

---

### 探讨 #75: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

2026 03 03

天清气晴 今日收获昨日base RA 有20$ ,小地区乘数 还是挺厉害的，继续努力，看到量化交流群中，有大佬分享一个RA 50$ ,还是非常的羡慕，最近的base 特别的低迷

，加油！！！！
  ==========================VF 1.0==================================

============================================================

---

### 探讨 #76: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

2026 03 04

今日休息一天，晚上回来，交个SA ，看下昨天的base 60$,满意 不错，继续加油，要是os 一直高就好了，还有21个 not own sa 额度，接下来无论啥情况都交  not own 吧 ，fitting ！！！！

，加油！！！！
  ==========================VF 1.0==================================

=============================贺六浑的量化日记=========================

---

### 探讨 #77: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

2026 03 05 在跑小地区JPN,发现margin 都好低，有些都不敢交，但是要点塔，就难受了，还是尽量交margin 高的吧，希望combine稳住，这赛季还相当GM

==========================VF 1.0================================

============================贺六浑的量化日记===================================

---

### 探讨 #78: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

2026 03 06  os 分数来到了0.4，感觉比0.5多的话，base 就会高一些，不知道呀，这个分数我不太稳定，想要稳定在0.5以上就好了

==========================VF 1.0================================

============================贺六浑的量化日记===================================

---

### 探讨 #79: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **评论时间**: 9个月前

已经点完了60座塔了，但是最近几天发现排名一直在掉，感觉还是有些危险，再交一些新的字段 和少的操作符拉一下avg 水平，大家都是挺强的，这个赛季还有gold 直冲 gm 的，太强了 =======================VF 1.0=================================== =========================================================

---

### 探讨 #80: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: [Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法.md
- **评论时间**: 1 year ago

**在社区投稿了一篇用代码的帖子，功能包括随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。使用 了 MySQL 数据库实现的自动生成super alpha ,并多线程回测super alpha的方案，并且这个方案具备“断点续传”的能力，无惧程序中途宕机** 。

[Super-Alpha-自动生成-多线程自动回测-mysql-版本-无惧程序宕机-断点续传](Super Alpha 自动生成多线程自动回测 mysql 版本 无惧程序宕机断点续传代码优化.md)

---

### 探讨 #81: 关于《步骤2: 计算残差与X平方的协方差》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md
- **评论时间**: 1年前

**在社区投稿了一篇用代码的帖子，功能包括随机生成selection表达式，与自定义combo表达式组合进行不间断的super alpha回测，可自定义limit、地区、中心化等选项。使用 了 MySQL 数据库实现的自动生成super alpha ,并多线程回测super alpha的方案，并且这个方案具备“断点续传”的能力，无惧程序中途宕机** 。

[Super-Alpha-自动生成-多线程自动回测-mysql-版本-无惧程序宕机-断点续传](Super Alpha 自动生成多线程自动回测 mysql 版本 无惧程序宕机断点续传代码优化_32683522027159.md)

---

### 探讨 #82: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: [Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享.md
- **评论时间**: 9个月前

太强了， gold 直升 GM ，点塔的范围也让我深有启发，chn 也可以点这么多的哇，下个赛季我再来碰chn 吧，感谢大佬分享

=========================================================================================VF1.0===================================================================================

---

### 探讨 #83: 关于《【经验分享】冲刺 genius！+ 细节决定成-败，你的六维还能提升！+ 点塔！+ alpha模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】冲刺 genius 细节决定成-败你的六维还能提升 点塔 alpha模板经验分享_34913747788695.md
- **评论时间**: 9个月前

太强了， gold 直升 GM ，点塔的范围也让我深有启发，chn 也可以点这么多的哇，下个赛季我再来碰chn 吧，感谢大佬分享

=========================================================================================VF1.0===================================================================================

---

### 探讨 #84: 关于《模拟的相关性检查函数》的评论回复
- **帖子链接**: [Commented] 【老毛课堂】同时测10000个alpha的Prod Correlation和Self Correlation.md
- **评论时间**: 1年前

THROTTLED  被限流之后，多久能恢复呀

---

### 探讨 #85: 关于《模拟的相关性检查函数》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【老毛课堂】同时测10000个alpha的Prod Correlation和Self Correlation_29173696213143.md
- **评论时间**: 1年前

THROTTLED  被限流之后，多久能恢复呀

---

### 探讨 #86: 关于《点击name以获取alpha id》的评论回复
- **帖子链接**: [Commented] 【自动化脚本】在unsubmitted列表中快速检索可提交alpha.md
- **评论时间**: 1年前

不用这么写 爬网页，不如直接调用api

```
[链接已屏蔽]
```

---

### 探讨 #87: 关于《点击name以获取alpha id》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【自动化脚本】在unsubmitted列表中快速检索可提交alpha_29393852864407.md
- **评论时间**: 1年前

不用这么写 爬网页，不如直接调用api

```
[链接已屏蔽]
```

---

### 探讨 #88: 关于《一文搞懂并推测alpha表达式在证券市场中的含义》的评论回复
- **帖子链接**: [Commented] 一文搞懂并推测alpha表达式在证券市场中的含义.md
- **评论时间**: 1年前

感谢大佬分享 深入浅出地讲解了alpha表达式在证券市场中的含义，以具体的表达式为例，从内到外逐层剖析了每个函数的作用和意义。对于新手来说非常友好，能够帮助他们快速理解复杂表达式的构造逻辑。结合市场情绪、投资者行为和技术分析的示例，生动展示了这些处理步骤如何揭示市场规律，实用性很强。文章最后点明了反转数据顺序分析的独特价值，拓宽了读者的分析思路。美中不足的是没有提供实际代码示例，不过整体来说是一篇不可多得的好文，强烈建议收藏反复研读！

---

### 探讨 #89: 关于《一文搞懂并推测alpha表达式在证券市场中的含义》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 一文搞懂并推测alpha表达式在证券市场中的含义_32862695953047.md
- **评论时间**: 1年前

感谢大佬分享 深入浅出地讲解了alpha表达式在证券市场中的含义，以具体的表达式为例，从内到外逐层剖析了每个函数的作用和意义。对于新手来说非常友好，能够帮助他们快速理解复杂表达式的构造逻辑。结合市场情绪、投资者行为和技术分析的示例，生动展示了这些处理步骤如何揭示市场规律，实用性很强。文章最后点明了反转数据顺序分析的独特价值，拓宽了读者的分析思路。美中不足的是没有提供实际代码示例，不过整体来说是一篇不可多得的好文，强烈建议收藏反复研读！

---

### 探讨 #90: 关于《使用Gemini CLI创建可能有效的模板经验分享》的评论回复
- **帖子链接**: [Commented] 使用Gemini CLI创建可能有效的模板经验分享.md
- **评论时间**: 1年前

感谢大佬分享  不过 本地用 Gemini 是不是要用魔法呀，有时候感觉GEmini 的幻觉很重，它思考过程 是 英文的，不像deepseek 思考过程是 中文的， 还是更喜欢用deepseek 一点， 不过能创建出有用的模板还是挺好的，喂它资料生成自己的知识库。
================================VF 1.0 ========================================

---

### 探讨 #91: 关于《使用Gemini CLI创建可能有效的模板经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 使用Gemini CLI创建可能有效的模板经验分享_33223735552407.md
- **评论时间**: 1年前

感谢大佬分享  不过 本地用 Gemini 是不是要用魔法呀，有时候感觉GEmini 的幻觉很重，它思考过程 是 英文的，不像deepseek 思考过程是 中文的， 还是更喜欢用deepseek 一点， 不过能创建出有用的模板还是挺好的，喂它资料生成自己的知识库。
================================VF 1.0 ========================================

---

### 探讨 #92: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 在wq半年从15刀到100刀我是怎么做到连续三个月vf10comb294的经验分享.md
- **评论时间**: 2个月前

连续三个月 VF 1.0 ，太羡慕了，我最高才0.99，这几个月还疯狂掉，

- sc和ppc：有时候会出现一个alpha的sc很高，但是ppc很低的情况，有些经常断粮的这时候交把持不住了，我一般是会取sc和ppc的最大值来看，两者最大值小于5才会提交

大佬这里说的， 两者最大值小于5啥意思  ，他们的范围不是 0-1 吗，肯定是小于5的呀，还望 大佬解释一下

=====================================VF1.0=========================================

---

### 探讨 #93: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 在wq半年从15刀到100刀我是怎么做到连续三个月vf10comb294的经验分享_39759673422487.md
- **评论时间**: 2个月前

连续三个月 VF 1.0 ，太羡慕了，我最高才0.99，这几个月还疯狂掉，

- sc和ppc：有时候会出现一个alpha的sc很高，但是ppc很低的情况，有些经常断粮的这时候交把持不住了，我一般是会取sc和ppc的最大值来看，两者最大值小于5才会提交

大佬这里说的， 两者最大值小于5啥意思  ，他们的范围不是 0-1 吗，肯定是小于5的呀，还望 大佬解释一下

=====================================VF1.0=========================================

---

### 探讨 #94: 关于《提取字段名（cut_index之前的部分）》的评论回复
- **帖子链接**: [Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化.md
- **评论时间**: 1年前

感谢游戏王大佬的分享，用了这个代码，果真把我的换手率降低了，把margin 和 return 都提高了，谢谢大佬的代码，手动点赞

================================VF 1.0===========================================

---

### 探讨 #95: 关于《提取字段名（cut_index之前的部分）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md
- **评论时间**: 1年前

感谢游戏王大佬的分享，用了这个代码，果真把我的换手率降低了，把margin 和 return 都提高了，谢谢大佬的代码，手动点赞

================================VF 1.0===========================================

---

### 探讨 #96: 关于《我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化》的评论回复
- **帖子链接**: [Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化.md
- **评论时间**: 1年前

非常不错的分享，不过之前我也搞了类似的知识库，喂养了世坤的表达式，和数据字段等数据给他，不过由于自身电脑显卡是 4060 ，跑起来，大半天才出一些字，有时候AI 幻觉还很重，通过它跑出来的一些表达式 有些还可以，主要是慢，最后放弃了，大佬还是挺不错的

---

### 探讨 #97: 关于《我把论坛模板的知识喂给腾讯IMA，看看他如何帮我生成上千个ALPHA表达式代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 我把论坛模板的知识喂给腾讯IMA看看他如何帮我生成上千个ALPHA表达式代码优化_33016862088599.md
- **评论时间**: 1年前

非常不错的分享，不过之前我也搞了类似的知识库，喂养了世坤的表达式，和数据字段等数据给他，不过由于自身电脑显卡是 4060 ，跑起来，大半天才出一些字，有时候AI 幻觉还很重，通过它跑出来的一些表达式 有些还可以，主要是慢，最后放弃了，大佬还是挺不错的

---

### 探讨 #98: 关于《src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    ...    获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...])》的评论回复
- **帖子链接**: [Commented] 构建 724 小时不间断 Alpha 回测系统基于 Celery 和动态任务队列的架构分享代码优化.md
- **评论时间**: 1年前

感谢大佬分享
小白从量化新手一路到能设计出这么棒的回测系统，这成长够惊艳的。文章把晦涩的技术原理讲得简单易懂，从背景介绍到架构设计、关键代码实现，再到实际效果，逻辑清晰得很。这Celery的引入，把回测任务管理得井井有条，7×24小时自动跑，还解耦、资源占用低，让回测变得轻松又高效，对量化研究帮助肯定大。
分享特别实在，给咱这些想搞自动化回测的人指了条明路，赞！

---

### 探讨 #99: 关于《src/tasks/scheduler_tasks.py@app.taskdef check_queue_status():    ...    获取可分配的任务 (按优先级排序)    pending_queues = await AlphaBacktestQueue.filter(status=0)\                                           .order_by("-priority")\                                           .limit(available_slots)        分配任务给 Celery Worker    for queue in pending_queues:        queue.status = 1  标记为进行中        await queue.save()        run_backtest_task.apply_async(args=[queue.id, ...])》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 构建 724 小时不间断 Alpha 回测系统基于 Celery 和动态任务队列的架构分享代码优化_33040125516311.md
- **评论时间**: 1年前

感谢大佬分享
小白从量化新手一路到能设计出这么棒的回测系统，这成长够惊艳的。文章把晦涩的技术原理讲得简单易懂，从背景介绍到架构设计、关键代码实现，再到实际效果，逻辑清晰得很。这Celery的引入，把回测任务管理得井井有条，7×24小时自动跑，还解耦、资源占用低，让回测变得轻松又高效，对量化研究帮助肯定大。
分享特别实在，给咱这些想搞自动化回测的人指了条明路，赞！

---

### 探讨 #100: 关于《欧洲市场weight大于10%能提交吗》的评论回复
- **帖子链接**: [Commented] 欧洲市场weight大于10能提交吗.md
- **评论时间**: 10个月前

in this  Community ,please speak English ， But I want to tell you that you can click on perform. If there is more, I will submit it.

==================================VF 1.0============================================

==================================VF 1.0============================================

---

### 探讨 #101: 关于《欧洲市场weight大于10%能提交吗》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 欧洲市场weight大于10能提交吗_33843134935319.md
- **评论时间**: 10个月前

in this  Community ,please speak English ， But I want to tell you that you can click on perform. If there is more, I will submit it.

==================================VF 1.0============================================

==================================VF 1.0============================================

---

### 探讨 #102: 关于《监控进程和日志，避免回测长时间中断，避免连续回测天数指标清零代码优化》的评论回复
- **帖子链接**: [Commented] 监控进程和日志避免回测长时间中断避免连续回测天数指标清零代码优化.md
- **评论时间**: 1年前

感谢博主的分享，您的经验很有启发。关于程序监控，我也建立了一套自己的“强提醒”机制。我写了一个监控脚本，当主程序意外中断或崩溃时，它会自动触发一个告警流程。首先，它会在一小时的窗口期内，持续尝试向我的手机邮箱发送警报邮件。考虑到网络可能不稳定导致邮件发送失败，我还设计了一个备用方案（Fallback）：如果邮件在设定时间内无法成功发出，脚本会自动调用电脑的播放器，无限循环播放音乐。这样，即使在断网的情况下，我也能通过这个“物理”声音警报，及时发现程序已崩溃，从而进行手动重启。

===================VF 1.0===========================

---

### 探讨 #103: 关于《监控进程和日志，避免回测长时间中断，避免连续回测天数指标清零代码优化》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 监控进程和日志避免回测长时间中断避免连续回测天数指标清零代码优化_32934983147031.md
- **评论时间**: 1年前

感谢博主的分享，您的经验很有启发。关于程序监控，我也建立了一套自己的“强提醒”机制。我写了一个监控脚本，当主程序意外中断或崩溃时，它会自动触发一个告警流程。首先，它会在一小时的窗口期内，持续尝试向我的手机邮箱发送警报邮件。考虑到网络可能不稳定导致邮件发送失败，我还设计了一个备用方案（Fallback）：如果邮件在设定时间内无法成功发出，脚本会自动调用电脑的播放器，无限循环播放音乐。这样，即使在断网的情况下，我也能通过这个“物理”声音警报，及时发现程序已崩溃，从而进行手动重启。

===================VF 1.0===========================

---

### 探讨 #104: 关于《第一赛季Value Factor Improvement 心得与分享》的评论回复
- **帖子链接**: [Commented] 第一赛季Value Factor Improvement 心得与分享.md
- **评论时间**: 1年前

大佬厉害，学习了

---

### 探讨 #105: 关于《第一赛季Value Factor Improvement 心得与分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 第一赛季Value Factor Improvement 心得与分享_32578030064407.md
- **评论时间**: 1年前

大佬厉害，学习了

---

### 探讨 #106: 关于《之前代码不变alpha_list = response.json()["results"]print(response.json())for j in range(len(alpha_list)):    c_r = True      for k in alpha_list[j]["is"]["checks"]:        if k["name"] == 'MATCHES_THEMES' and k['result']=='PENDING':            c_r = False      if c_r: 如果不是 满足 ppac的 alpha 则跳过        continue    alpha_id = alpha_list[j]["id"]    name = alpha_list[j]["name"]    dateCreated = alpha_list[j]["dateCreated"]    sharpe = alpha_list[j]["is"]["sharpe"]#接后续代码》的评论回复
- **帖子链接**: [Commented] 筛选历史回测中满足PPAC的alpha含代码代码优化.md
- **评论时间**: 1年前

博主写的不错， 不过在程序中 ，competition_result 本身就是bool 值， 不需要些 if  competition_result==True   直接写   if competition_result  就行了 并且现在 MATCHES_COMPETITION  已经改成了MATCHES_THEMES

```
# 之前代码不变alpha_list = response.json()["results"]# print(response.json())for j in range(len(alpha_list)):    c_r = True      for k in alpha_list[j]["is"]["checks"]:        if k["name"] == 'MATCHES_THEMES' and k['result']=='PENDING':            c_r = False      if c_r: # 如果不是 满足 ppac的 alpha 则跳过        continue    alpha_id = alpha_list[j]["id"]    name = alpha_list[j]["name"]    dateCreated = alpha_list[j]["dateCreated"]    sharpe = alpha_list[j]["is"]["sharpe"]#接后续代码
```

---

### 探讨 #107: 关于《之前代码不变alpha_list = response.json()["results"]print(response.json())for j in range(len(alpha_list)):    c_r = True      for k in alpha_list[j]["is"]["checks"]:        if k["name"] == 'MATCHES_THEMES' and k['result']=='PENDING':            c_r = False      if c_r: 如果不是 满足 ppac的 alpha 则跳过        continue    alpha_id = alpha_list[j]["id"]    name = alpha_list[j]["name"]    dateCreated = alpha_list[j]["dateCreated"]    sharpe = alpha_list[j]["is"]["sharpe"]#接后续代码》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 筛选历史回测中满足PPAC的alpha含代码代码优化_31028934380055.md
- **评论时间**: 1年前

博主写的不错， 不过在程序中 ，competition_result 本身就是bool 值， 不需要些 if  competition_result==True   直接写   if competition_result  就行了 并且现在 MATCHES_COMPETITION  已经改成了MATCHES_THEMES

```
# 之前代码不变alpha_list = response.json()["results"]# print(response.json())for j in range(len(alpha_list)):    c_r = True      for k in alpha_list[j]["is"]["checks"]:        if k["name"] == 'MATCHES_THEMES' and k['result']=='PENDING':            c_r = False      if c_r: # 如果不是 满足 ppac的 alpha 则跳过        continue    alpha_id = alpha_list[j]["id"]    name = alpha_list[j]["name"]    dateCreated = alpha_list[j]["dateCreated"]    sharpe = alpha_list[j]["is"]["sharpe"]#接后续代码
```

---

### 探讨 #108: 关于《经验分享｜PPAC全球第三名，回馈社区经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **评论时间**: 1年前


> [!NOTE] [图片 OCR 识别内容]
> 15 |eSUIg StatU5
> Fepioq
> Self Correlation
> NsmUM
> TMNC
> Last Run:
> 05/19/2025。4.13 Prl
> 11 PASS
> 1FAIL
> Prod Correlation
> NaximJm
> WIAITUM
> L35t Rur -
> Prod COrrelaton 09311
> aDOVE CUtOff Of 0.7and ShaTPE not Deter by 10095 OTMore。
> 2WARNINC
> There are no prod-orrelated
> PhEs
> Performance Comparison
> TI
> Properties
> Lsst savsd Nor; 05/19/2025。7.53 Pl
> Name
> Category
> Why not sUb
> NOne
> Tags
> Color
> PowerpoolSelected <
> None
> Description
> Tlea: https:TsUpporworldquantoraincomnoen-Usicommunityposts} 29985532824343Npha-Template-HoW-CaryOU-UtilZe-The-PEG-tO-create
> Aphas
> Rationa
> TOr data Used: is
> eood sien 可以带来比较不锘的收益
> Rationa
> Toroperators Used: Tnis illgive
> lnearsiena
> Cannotsubmiit Alpha:
> test falled
> Nop
 ppac 不是不检查 prod correlation 吗，为啥这个检查了

---

### 探讨 #109: 关于《说说成为顾问之后的一些体会。经验分享》的评论回复
- **帖子链接**: [Commented] 说说成为顾问之后的一些体会经验分享.md
- **评论时间**: 1年前

太有共鸣了！尤其关于代码优化那块，真的深有体会。一开始拿着标准模板硬跑，遇到点特殊情况就傻眼。后来也是靠GPT和论坛大佬的帖子救命，自己一点点改，那种捣鼓明白后的成就感贼爽。还有你对数据集和value factor的提醒也是金玉良言，新顾问最容易踩的坑都点到了，谢大佬分享！

---

### 探讨 #110: 关于《说说成为顾问之后的一些体会。经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 说说成为顾问之后的一些体会经验分享_33143682171415.md
- **评论时间**: 1年前

太有共鸣了！尤其关于代码优化那块，真的深有体会。一开始拿着标准模板硬跑，遇到点特殊情况就傻眼。后来也是靠GPT和论坛大佬的帖子救命，自己一点点改，那种捣鼓明白后的成就感贼爽。还有你对数据集和value factor的提醒也是金玉良言，新顾问最容易踩的坑都点到了，谢大佬分享！

---
