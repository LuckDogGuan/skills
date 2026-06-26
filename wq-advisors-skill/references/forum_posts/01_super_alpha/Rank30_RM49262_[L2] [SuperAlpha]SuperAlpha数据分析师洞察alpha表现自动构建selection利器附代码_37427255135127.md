# [SuperAlpha]SuperAlpha数据分析师，洞察alpha表现自动构建selection利器(附代码)

- **链接**: https://support.worldquantbrain.com[L2] [SuperAlpha]SuperAlpha数据分析师洞察alpha表现自动构建selection利器附代码_37427255135127.md
- **作者**: 顾问 JX79797 (Rank 9)
- **发布时间/热度**: 5个月前, 得票: 75

## 帖子正文

在上一篇帖子中，

[[Commented] [SuperAlpha] 基于SuperAlpha数据分析师--Own极简回测次数源源不断三五附代码_37427295710359.md]([Commented] [SuperAlpha] 基于SuperAlpha数据分析师--Own极简回测次数源源不断三五附代码_37427295710359.md)  [SuperAlpha] 基于SuperAlpha数据分析师--Own极简回测次数源源不断三五

背后的“大脑”——`sa_selection_analyzer.py`，它提供了一个强大的 `SuperAlphaSelectionAnalyzer` 类，帮助我们深入理解 `selection` 表达式的效果，并优化Super Alpha的构建策略。

`SuperAlphaSelectionAnalyzer` 不仅仅是一个数据获取器，更是一个**多维度的Alpha表现分析平台**。它能够将BRAIN平台API返回的原始数据转化为结构化的、可分析的信息，并提供一系列工具来帮助您识别趋势、发现问题并做出更明智的决策。

**核心功能**

**1. 灵活的Alpha数据获取**

精准拉取：根据您提供的 `selection` 表达式、区域 (Region) 和延迟 (Delay) 等参数，`fetch_alphas` 方法能够精确地从BRAIN平台API拉取所有匹配的Alpha数据。

统一的 `os.sharpe` 提取：考虑到API返回数据中 `os.sharpe` 可能存在于不同的结构中（例如直接作为字段或嵌套在 `os.checks` 列表中），它提供了一个辅助函数 `_extract_os_sharpe` 来统一提取，确保数据的一致性。

**2. 强大的数据分析与报告功能**

* DataFrame集成：所有拉取到的Alpha数据都会被转换为易于操作和分析的 `pandas.DataFrame` 格式，让您可以充分利用Pandas的强大功能。

* 最差表现Alpha报告 (`get_worst_performers_report`, `qu`)：

通过指定排序指标（例如 `os.sharpe_unified`, `is.turnover` 等），您可以轻松找出表现最差的N个Alpha。这对于识别低质量或有问题的Alpha信号至关重要。这些函数不仅返回最差Alpha的ID，还会展示其关键特征，帮助您快速定位问题所在。

* Margin 比较计数 (`get_margin_comparison_counts`)：此功能允许您根据 `is.margin` 的不同阈值，统计满足条件的Alpha数量。这对于评估Alpha的杠杆使用情况和风险暴露非常有用。

* 核心指标统计摘要 (`get_metrics_summary`)提供 `is.sharpe`, `os.sharpe_unified`, `is.turnover`, `is.fitness`, `is.prodCorrelation`, `is.longCount`, `is.shortCount`, `regular.operatorCount` 等核心指标的描述性统计（均值、标准差、分位数等），帮助您快速了解Alpha集合的整体表现特征。

* 分组计数 (`get_group_counts`)：可以按任何列对Alpha进行分组并计数，例如按 `settings.universe` 或 `settings.neutralization`，以了解不同配置组合下Alpha的分布情况。

* 失败检查摘要 (`get_failed_checks_summary`)：统计 `is.checks` 中各项失败的次数，帮助您快速识别Alpha在In-Sample阶段常遇到的问题（如 `LOW_SHARPE`, `HIGH_TURNOVER` 等）。

* 金字塔匹配摘要 (`get_pyramid_summary`)：汇总Alpha在金字塔中的匹配情况，包括匹配到金字塔的Alpha总数以及每个金字塔（如 `USA/EQUITY/FUNDAMENTAL/D1`）下的Alpha数量。这对于评估Super Alpha的多元化贡献和奖励潜力非常有帮助。

`sa_selection_analyzer.py` 与 `own_superalpha.py` 的协同

`SuperAlphaSelectionAnalyzer` 在 `own_superalpha.py` 中扮演着至关重要的角色，尤其是在 `generate_and_refine_selection_expression_own` 函数中：

**1. 实时效果评估** ：当 `own_superalpha.py` 生成一个候选 `selection` 表达式时，它会立即调用 `SuperAlphaSelectionAnalyzer` 的 `fetch_alphas` 方法来获取该表达式所匹配的Alpha。

2 **. 数量与质量控制** ：`SuperAlphaSelectionAnalyzer` 帮助 `own_superalpha.py` 检查匹配到的Alpha数量是否在目标范围内（例如 40-70 个），并提供Alpha的性能指标，以便 `own_superalpha.py` 能够根据这些信息对 `selection` 表达式进行调整和优化（例如，通过排除表现最差的Alpha来精炼表达式）。

3.  **多样性保障** ：通过 `SuperAlphaSelectionAnalyzer` 获取的Alpha ID集合，`own_superalpha.py` 能够判断新生成的 `selection` 表达式是否与之前生成的表达式具有足够的多样性，避免重复劳动。

**总结**

验证 `selection` 表达式的有效性

识别并排除低质量的Alpha

优化Super Alpha的组件选择

确保Super Alpha组合的多样性和稳健性

**代码分享**

```
# sa_selection_analyzer.pyimport urllib.parsefrom collections import Counterimport pandas as pdfrom typing import Optionalclass SuperAlphaSelectionAnalyzer:    """    一个用于获取和分析 Super Alpha selection 表达式匹配结果的工具类。    """    def __init__(self, session, verbose: bool = True):        """        初始化分析器。        :param session: 已登录的 WorldQuant BRAIN session 对象。        :param verbose: 是否打印详细信息 (默认为 True)。        """        if not session:            raise ValueError("Session 对象不能为空。")        self.session = session        self.raw_results = []        self.df = None        self.verbose = verbose    def fetch_alphas(self, selection_expr: str, region: str = 'USA', delay: int = 1, selection_limit: int = 1000) -> 'SuperAlphaSelectionAnalyzer':        """        获取所有匹配表达式的 alpha 数据，并存储在实例内部。        返回 self，以支持链式调用。        """        print(f"正在为区域 '{region}' (Delay: {delay}) 拉取表达式的全部结果:")        print(f"  -> {selection_expr}")        total_count_from_api = self.get_total_count_from_api(selection_expr, region, delay, selection_limit)        if total_count_from_api is not None:            print(f"API 报告总数: {total_count_from_api} 条记录。")        else:            print("警告: 未能获取到 API 报告的总数。")        self.raw_results = []                base_url = "https://api.worldquantbrain.com/simulations/super-selection"        params = {            "settings.instrumentType": "EQUITY",            "settings.region": region,            "settings.delay": delay,            "selection": selection_expr,            "limit": 100,            "selectionLimit": selection_limit,            "selectionHandling": "POSITIVE"        }        next_url = f"{base_url}?{urllib.parse.urlencode(params)}"        page_num = 1        while next_url:            print(f"正在拉取第 {page_num} 页数据...")            try:                response = self.session.get(next_url)                response.raise_for_status()                data = response.json()                results_on_page = data.get("results", [])                if results_on_page:                    self.raw_results.extend(results_on_page)                                next_url = data.get("next")                if next_url and "http://" in next_url and ":443" in next_url:                    next_url = next_url.replace("http://", "https://").replace(":443", "")                page_num += 1            except Exception as e:                print(f"请求 API 时发生错误: {e}")                try:                    print("API 错误响应:", response.text)                except:                    pass                # 清空已拉取的数据，表示失败                self.raw_results = []                break                print(f"数据拉取完毕，共 {len(self.raw_results)} 条记录。")        if total_count_from_api is not None:            if len(self.raw_results) == total_count_from_api:                print(f"验证成功: 拉取到的记录数 ({len(self.raw_results)}) 与 API 报告的总数 ({total_count_from_api}) 一致。")            else:                print(f"!!! 验证失败: 拉取到的记录数 ({len(self.raw_results)}) 与 API 报告的总数 ({total_count_from_api}) 不一致。 !!!")        if self.raw_results:            self.df = pd.json_normalize(self.raw_results)            # 创建一个统一的 os.sharpe 列来处理不同的数据结构或缺失数据            self.df['os.sharpe_unified'] = self.df.apply(self._extract_os_sharpe, axis=1)        else:            self.df = pd.DataFrame() # 如果没有结果，则创建一个空的DataFrame        return self    def get_total_count_from_api(self, selection_expr: str, region: str = 'USA', delay: int = 1, selection_limit: int = 1000) -> Optional[int]:        """        仅获取匹配表达式的 alpha 总数，不拉取具体数据。        """        print(f"正在为区域 '{region}' (Delay: {delay}) 获取表达式的总记录数:")        print(f"  -> {selection_expr}")        base_url = "https://api.worldquantbrain.com/simulations/super-selection"        params = {            "settings.instrumentType": "EQUITY",            "settings.region": region,            "settings.delay": delay,            "selection": selection_expr,            "limit": 1,  # 只请求一条数据以获取总数            "selectionLimit": selection_limit,            "selectionHandling": "POSITIVE"        }        url = f"{base_url}?{urllib.parse.urlencode(params)}"        try:            response = self.session.get(url)            response.raise_for_status()            data = response.json()            return data.get("count")        except Exception as e:            print(f"获取总数时请求 API 发生错误: {e}")            try:                print("API 错误响应:", response.text)            except:                pass            return None    def _extract_os_sharpe(self, row):        """        一个辅助函数，用于从不同可能的位置提取 os.sharpe。        """        # 优先尝试从 os.checks 列表中获取        if 'os.checks' in row and isinstance(row['os.checks'], list):            for check in row['os.checks']:                if isinstance(check, dict) and check.get('name') == 'SHARPE' and 'value' in check:                    return check['value']                # 如果上面找不到，再尝试直接从 os.sharpe 获取        if 'os.sharpe' in row:            return row['os.sharpe']                    return None # 都找不到则返回None    def _extract_is_margin(self, row):        """        一个辅助函数，用于从不同可能的位置提取 is.margin。        """        # 优先尝试从 is.checks 列表中获取        if 'is.checks' in row and isinstance(row['is.checks'], list):            for check in row['is.checks']:                if isinstance(check, dict) and check.get('name') == 'MARGIN' and 'value' in check:                    return check['value']                # 如果上面找不到，再尝试直接从 is.margin 获取        if 'is.margin' in row:            return row['is.margin']                    return None # 都找不到则返回None    def get_worst_performers_report(self, sort_by_column: str, n: int = 10, columns_to_show: list = None):        """        找出按指定指标排序表现最差的 n 个 alpha，并展示它们的指定特征。        :param sort_by_column: 用于排序的列 (e.g., 'os.sharpe_unified').        :param n: 返回的最差 alpha 的数量.        :param columns_to_show: 要展示的列.        :return: 包含最差 n 个 alpha 特征的 DataFrame.        """        if self.df is None or self.df.empty:            print("没有数据可供分析。请先调用 fetch_alphas()。")            return None                if sort_by_column not in self.df.columns:            print(f"错误: 排序参照列 '{sort_by_column}' 不存在。")            return None        # 确保排序列是数值类型        self.df[sort_by_column] = pd.to_numeric(self.df[sort_by_column], errors='coerce')                # 排序并选出最差的 n 个 (处理 NaN 值，将它们视为最差)        worst_df = self.df.sort_values(by=sort_by_column, ascending=True, na_position='first').head(n)        if columns_to_show is None:            columns_to_show = ['id', sort_by_column, 'is.turnover', 'regular.operatorCount', 'is.sharpe']        existing_cols = [col for col in worst_df.columns]                return worst_df[existing_cols]    def get_margin_comparison_counts(self, margin_thresholds: list) -> str:        """        根据提供的 is.margin 阈值列表，计算 is.margin * 10000 大于每个阈值的 alpha 数量。        :param margin_thresholds: 一个整数列表，代表 is.margin 的阈值。        :return: 一个字符串，包含每个阈值对应的 alpha 数量，用下划线 '_' 连接。                 例如，如果阈值为 [15, 10]，结果可能为 "43_100"。        """        if self.df is None or self.df.empty:            print("没有数据可供分析。请先调用 fetch_alphas()。")            return ""        # 确保 'is.margin' 列存在或可以被提取        if 'is.margin' not in self.df.columns:            self.df['is.margin'] = self.df.apply(self._extract_is_margin, axis=1)            if 'is.margin' not in self.df.columns:                print("错误: 'is.margin' 列不存在，也无法从 'is.checks' 中提取。")                return ""        # 将 is.margin 转换为数值类型，并乘以 10000        margin_values = pd.to_numeric(self.df['is.margin'], errors='coerce').fillna(0) * 10000        counts = []        for threshold in margin_thresholds:            count = (margin_values > threshold).sum()            counts.append(str(count))        return "_".join(counts)    def get_count(self) -> int:        """返回拉取到的 alpha 总数。"""        return len(self.raw_results)    def get_dataframe(self) -> pd.DataFrame:        """返回包含所有数据的 pandas DataFrame。"""        return self.df    def get_metrics_summary(self, columns: list = None) -> pd.DataFrame:        """返回核心数值指标的统计摘要。"""        if self.df is None or self.df.empty:            print("没有数据可供分析。请先调用 fetch_alphas()。")            return None                if columns is None:            columns = [                'is.sharpe', 'os.sharpe_unified', 'is.turnover', 'is.fitness',                 'is.prodCorrelation', 'is.longCount', 'is.shortCount', 'regular.operatorCount'            ]                existing_cols = [col for col in columns if col in self.df.columns]        if not existing_cols:            print("指定的列在数据中都不存在。")            return None                    pd.set_option('display.float_format', lambda x: '%.3f' % x)        return self.df[existing_cols].describe(percentiles=[.25, .5, .75])    def get_group_counts(self, group_by_column: str) -> pd.Series:        """按指定列进行分组并计数。"""        if self.df is None or self.df.empty:            print("没有数据可供分析。请先调用 fetch_alphas()。")            return None                if group_by_column not in self.df.columns:            print(f"错误: 列 '{group_by_column}' 不存在。")            return None                    return self.df.groupby(group_by_column).size().sort_index()    def get_failed_checks_summary(self) -> pd.Series:        """统计 IS Checks 中各项失败的次数。"""        if self.df is None or self.df.empty or 'is.checks' not in self.df.columns:            print("没有 'is.checks' 数据可供分析。")            return None                    failed_checks = self.df['is.checks'].explode().apply(            lambda x: x['name'] if isinstance(x, dict) and x.get('result') == 'FAIL' else None        )        failed_counts = failed_checks.value_counts()        return failed_counts if not failed_counts.empty else pd.Series(dtype=int)    def get_pyramid_summary(self) -> pd.DataFrame:        """统计金字塔的匹配情况。"""        if self.df is None or self.df.empty or 'is.checks' not in self.df.columns:            print("没有 'is.checks' (pyramids) 数据可供分析。")            return None        pyramid_check = self.df['is.checks'].explode().dropna().apply(            lambda x: x if isinstance(x, dict) and x.get('name') == 'MATCHES_PYRAMID' and x.get('result') == 'PASS' else None        )                alphas_with_pyramids = pyramid_check.dropna().index.unique().size        print(f"匹配到金字塔的 Alpha 总数: {alphas_with_pyramids}")        all_pyramids = pyramid_check.dropna().apply(lambda x: [p['name'] for p in x.get('pyramids', [])])        pyramid_counts = Counter(p for sublist in all_pyramids for p in sublist)                if not pyramid_counts:            return pd.DataFrame(columns=['Pyramid', 'Count'])                    pyramid_df = pd.DataFrame(pyramid_counts.items(), columns=['Pyramid', 'Count']).sort_values(by='Count', ascending=False).reset_index(drop=True)        return pyramid_df    def qu(self, sort_by_column: str, n: int = 50, columns_to_show: list = None):        """        找出按指定指标排序表现最差的 n 个 alpha，并展示它们的指定特征。        :param sort_by_column: 用于排序的列 (e.g., 'os.sharpe_unified').        :param n: 返回的最差 alpha 的数量.        :param columns_to_show: 要展示的列.        :return: 包含最差 n 个 alpha 特征的 DataFrame.        """        if self.df is None or self.df.empty:            print("没有数据可供分析。请先调用 fetch_alphas()。")            return None                if sort_by_column not in self.df.columns:            print(f"错误: 排序参照列 '{sort_by_column}' 不存在。")            return None        # 确保排序列是数值类型        self.df[sort_by_column] = pd.to_numeric(self.df[sort_by_column], errors='coerce')                # 过滤掉 NaN 值后再排序并选出最差的 n 个        # 应该是有值的才参与，NAN的不去排序        filtered_df = self.df.dropna(subset=[sort_by_column])        worst_df = filtered_df.sort_values(by=sort_by_column, ascending=True).head(n)        if columns_to_show is None:            columns_to_show = ['id', sort_by_column, 'is.turnover', 'regular.operatorCount', 'is.sharpe']        existing_cols = [col for col in columns_to_show if col in worst_df.columns]                return worst_df[existing_cols]    def get_conditional_subset(self, condition_column: str, operator: str, value: float) -> pd.DataFrame:        """        根据指定条件筛选 alpha，并返回筛选后的 DataFrame 子集。        :param condition_column: 用于筛选的列 (e.g., 'os.sharpe_unified').        :param operator: 运算符 ('>', '<', '==', '>=', '<=').        :param value: 用于比较的值.        :return: 筛选后的 pandas DataFrame 子集.        """        if self.df is None or self.df.empty:            print("没有数据可供分析。请先调用 fetch_alphas()。")            return pd.DataFrame()                # 检查列是否存在，并处理缺失值        if condition_column not in self.df.columns:            print(f"错误: 条件列 '{condition_column}' 不存在。")            return pd.DataFrame()                # 在比较前，确保列是数值类型，并将无法转换的设置为NaN        numeric_column = pd.to_numeric(self.df[condition_column], errors='coerce')        # 根据操作符构建筛选条件        if operator == '>':            condition = numeric_column > value        elif operator == '<':            condition = numeric_column < value        elif operator == '==':            condition = numeric_column == value        elif operator == '>=':            condition = numeric_column >= value        elif operator == '<=':            condition = numeric_column <= value        else:            print(f"错误: 不支持的运算符 '{operator}'。")            return pd.DataFrame()        # 应用筛选条件 (fillna(False)确保NaN值不被选中)        subset_df = self.df[condition.fillna(False)]        print(f"\n筛选条件: `{condition_column} {operator} {value}` | 匹配到的 Alpha 数量: {len(subset_df)}")        if subset_df.empty:            print("没有 Alpha 满足此条件。")                return subset_df    def get_sharpe_distribution(self, column: str = 'os.sharpe') -> pd.Series:        """        计算 Sharpe 比率的分布情况。        将 Sharpe 值分到预定义的桶中并计数。        """        if self.df is None or self.df.empty or column not in self.df.columns:            print(f"没有 '{column}' 数据可供分析。")            return None        # 定义分桶的边界        bins = [-float('inf'), -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, float('inf')]        # 定义每个桶的标签        labels = [            "x < -1.5",            "-1.5 <= x < -1.0",            "-1.0 <= x < -0.5",            "-0.5 <= x < 0.0",            "0.0 <= x < 0.5",            "0.5 <= x < 1.0",            "1.0 <= x < 1.5",            "1.5 <= x < 2.0",            "2.0 <= x < 2.5",            "x >= 2.5"        ]        # 使用 pd.cut 进行分桶        sharpe_bins = pd.cut(self.df[column], bins=bins, labels=labels, right=False)        # 统计每个桶的数量        distribution = sharpe_bins.value_counts().sort_index()        return distribution
```

---

## 讨论与评论 (3)

### 评论 #1 (作者: XB37939, 时间: 5个月前)

大佬能不能把sa的运行过程描述下，菜鸡拿到了你这两个文件，执行了，只输出了下面的内容，也不会用：

& D:/Python/Python313/python.exe e:/code/gitee/brain/brain-consultant/own_superalpha.PY
usage: own_superalpha.PY [-h] {run_sims,gen_configs} ...

WorldQuant BRAIN Alpha 管理工具

positional arguments:
  {run_sims,gen_configs}
                        可用的命令
    run_sims            运行 Alpha 模拟
    gen_configs         生成 Alpha 模拟配置

options:
  -h, --help            show this help message and exit

#========= WORLDQUANT BRAIN CONSULTANT ========== #
#每天进步一点点，加油
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================加油每一天=======================#

---

### 评论 #2 (作者: HY20507, 时间: 4个月前)

### `sa_selection_analyzer.py——API 数据获取与分析工具类`

1. 从 WorldQuant BRAIN API 获取 Super Alpha 表达式匹配结果
2. 提供多种数据分析方法（最差表现者分析、统计摘要、分布分析等）
3. 支持链式调用，便于数据分析流水线

作为大佬另一篇帖子代码的工具箱

---

### 评论 #3 (作者: PZ64174, 时间: 4个月前)

大佬666，解了我的燃眉之急！太需要这个了。有让ai研究但是好像ai研究不太到位，总是打不到我要的效果，加上又限制回测，导致之前随机跑不是很适用，这个代码能够让我更快的做出own 的好superalpha！

====================================================================

一年一个台阶，一步一个脚印

====================================================================

---

