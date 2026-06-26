# 顾问 BL59154 (Rank 74) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 BL59154 (Rank 74) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: [ BRAIN TIPS ] How does regression_neut work ?
- **主帖链接**: https://support.worldquantbrain.com[L2] [ BRAIN TIPS ] How does regression_neut work_9672576065943.md
- **讨论数**: 1

The regression_neut (Y,X) operator conducts a cross-sectional regression on all the stocks in a given universe for the variables Y and X, using the parameters ‘a’ and ‘b’ — creating the final neutralized output of Y-(a+b*X) for each of the stocks in the universe.

Say, you have a dataset with sales and assets for 3,000 USA-listed companies and you want to answer the question: On a particular day, if my company’s assets equal 10, what sales would it have? You look into all the other companies with assets equaling ‘any value’ and their sales happen to be ‘any other value.’ You want to find the dependency between sales and assets and come up with a line provided by regression.

This line is defined as: sales_estimation = a+b*assets, where a and b come from regression by 3,000 points (companies’ sales–assets pairs) on a particular day, and assets are the assets for your company on that day. The regression_neut is sales (actual sales for your company) - sales_estimation (cross-sectional).

Here are a couple of examples of how this idea can be used in your workflow:

- As cross-sectional mean reversion (or momentum) of some value (ratio, returns, etc.) by something related to this value (otherwise b would be 0).
- For orthogonalization to some factors defined by X (similar to vector_neut operator). One popular factor is long price momentum/reversion.

---

### 帖子 #2: 一种随机生成 SuperAlpha，进行机器回测的方式代码优化
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

### 帖子 #3: 增量下载数据download_data(flag_increment=True)
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

### 帖子 #4: 【ValueFactor提升经验】从0.26->0.53->0.56->0.9->0.95的经验之谈
- **主帖链接**: 【ValueFactor提升经验】从026-053-056-09-095的经验之谈.md
- **讨论数**: 10

我是4月就开始成为条件顾问的，由于参加IQC的缘故，7月才计算valuefactor，印象中7、8月的vf好像是0.8左右，出乎意料以至于我放松警惕，交了若干过拟合的因子，来到了噩梦般的9月，vf一下子骤降到了0.26，连坐了三个月牢，一直到12份vf才有了质的变化。对于为什么突然骤降这么低，以及之后怎么改进，也有了一些经验，希望大家也能从中获得一些收获。为什么骤降？9月份更新的vf是5、6、7月三个月的因子os表现，鉴于我8月的vf不错，推断出问题出现在7月份提交的因子。7月份我提交的大多数是usa的pv因子，因为那段时间在复现alpha101因子，alpha101因子中几乎都是pv因子，并且通过二三阶来减低相关性来达到提交条件，因此造成了巨大的过拟合，即使7月份我几乎每天都有提交superalpha，但是os表现依旧很差。因此，我得出了三个经验：1. 不能只重复在一个category中做因子，尤其是一些容易过拟合的category，例如pv，model等，因子尽量分散在不同category中。2. 尽量不要单纯只是为了能提交而增加表达式复杂性。7月份我交的因子大多是三阶的，运算符也比较多，所以过拟合的概率就比较大。最好在有经济学意义的情况下才增加运算符。3. superalpha不是万能的。之前看很多大佬的经验都有说superalpha能提升整体因子表现，但是惨痛的经验告诉我交了差的ra因子，真的是神都难救。之后怎么改进？经过惨痛的教训之后，在这几个月中我都分散不同的category回测提交因子，尽量做到每个category都刚好只有三个因子（满足点塔要求）之后就去回测别的category；并且，ppac也尽量做到达到ra的要求，以保证表现。做到这些之后，vf也是慢慢地好起来了。希望我分享的这些经验对大家有所帮助，vf步步高升！

---

### 帖子 #5: 【ValueFactor提升经验】从0.26->0.53->0.56->0.9->0.95的经验之谈
- **主帖链接**: https://support.worldquantbrain.com【ValueFactor提升经验】从026-053-056-09-095的经验之谈_38154547987607.md
- **讨论数**: 10

我是4月就开始成为条件顾问的，由于参加IQC的缘故，7月才计算valuefactor，印象中7、8月的vf好像是0.8左右，出乎意料以至于我放松警惕，交了若干过拟合的因子，来到了噩梦般的9月，vf一下子骤降到了0.26，连坐了三个月牢，一直到12份vf才有了质的变化。对于为什么突然骤降这么低，以及之后怎么改进，也有了一些经验，希望大家也能从中获得一些收获。

**为什么骤降？**

9月份更新的vf是5、6、7月三个月的因子os表现，鉴于我8月的vf不错，推断出问题出现在7月份提交的因子。7月份我提交的大多数是usa的pv因子，因为那段时间在复现alpha101因子，alpha101因子中几乎都是pv因子，并且通过二三阶来减低相关性来达到提交条件，因此造成了巨大的过拟合，即使7月份我几乎每天都有提交superalpha，但是os表现依旧很差。因此，我得出了三个经验：

1. 不能只重复在一个category中做因子，尤其是一些容易过拟合的category，例如pv，model等，因子尽量分散在不同category中。

2. 尽量不要单纯只是为了能提交而增加表达式复杂性。7月份我交的因子大多是三阶的，运算符也比较多，所以过拟合的概率就比较大。最好在有经济学意义的情况下才增加运算符。

3. superalpha不是万能的。之前看很多大佬的经验都有说superalpha能提升整体因子表现，但是惨痛的经验告诉我交了差的ra因子，真的是神都难救。

**之后怎么改进？**

经过惨痛的教训之后，在这几个月中我都分散不同的category回测提交因子，尽量做到每个category都刚好只有三个因子（满足点塔要求）之后就去回测别的category；并且，ppac也尽量做到达到ra的要求，以保证表现。做到这些之后，vf也是慢慢地好起来了。

希望我分享的这些经验对大家有所帮助，vf步步高升！

---

### 帖子 #6: 【代码分享】检测可提交的SuperAlpha
- **主帖链接**: 【代码分享】检测可提交的SuperAlpha.md
- **讨论数**: 0

本人最近刚开通了super alpha的权限，使用了论坛中的../顾问 FZ60707 (Rank 78)/[Commented] 一种随机生成 SuperAlpha进行机器回测的方式代码优化.md分享的方式生成了super alpha,感谢大佬的分享，但是在搜索检测可提交的alpha的时候遇到了问题：如何只拉取super alpha到本地？super alpha需要写描述之后才能提交，如果没写描述，api检测是不通过的，如何解决这个问题，找到除了缺少描述之外所有指标都可提交的super alpha？经过一段时间的努力，终于解决了上述问题。对于第一个问题，修改machine_lib的get_alphas函数，删除url中type!=SUPER部分，且按照请求返回的type字段来区分alpha的类型，就可以只获得super alpha。def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage, return_detail=False, tag='REGULAR'):s = login()output = []output_detail = []# 3E large 3C lesscount = 0if tag == 'PPAC':tag = 'REGULAR'sub_tag = 'PPAC'else: sub_tag = ''for i in range(0, alpha_num, 100):logging.info(i)# 大于url_e = "[链接已屏蔽]) \+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \+ "T00:00:00-04:00&dateCreated%3C2025-" + end_date \+ "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \+ str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false" #&type!=SUPER"# 小于url_c = "[链接已屏蔽]) \+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \+ "T00:00:00-04:00&dateCreated%3C2025-" + end_date \+ "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \+ str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false" #&type!=SUPER"urls = [url_e]if usage != "submit":urls.append(url_c)for url in urls:response = s.get(url)#logging.info(response.json())try:alpha_list = response.json()["results"]#logging.info(response.json())for j in range(len(alpha_list)):alpha_type = alpha_list[j]["type"]alpha_id = alpha_list[j]["id"]name = alpha_list[j]["name"]dateCreated = alpha_list[j]["dateCreated"]sharpe = alpha_list[j]["is"]["sharpe"]fitness = alpha_list[j]["is"]["fitness"]turnover = alpha_list[j]["is"]["turnover"]margin = alpha_list[j]["is"]["margin"]longCount = alpha_list[j]["is"]["longCount"]shortCount = alpha_list[j]["is"]["shortCount"]decay = alpha_list[j]["settings"]["decay"]if alpha_type == tag:if tag == 'SUPER':exp = alpha_list[j]['selection']['code']#[, alpha_list[j]['combo']['code']]elif sub_tag == 'PPAC':operatercount = alpha_list[j]['regular']['operatorCount']exp = alpha_list[j]['regular']['code']if operatercount > 8:continueelse:exp = alpha_list[j]['regular']['code']else:continuecount += 1#if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):if (longCount + shortCount) > 100:if sharpe < -sharpe_th:exp = "-%s"%exprec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]logging.info(rec)if turnover > 0.7:rec.append(decay*4)elif turnover > 0.6:rec.append(decay*3+3)elif turnover > 0.5:rec.append(decay*3)elif turnover > 0.4:rec.append(decay*2)elif turnover > 0.35:rec.append(decay+4)elif turnover > 0.3:rec.append(decay+2)output.append(rec)output_detail.append(alpha_list[j])except:logging.info("%d finished re-login"%i)s = login()logging.info("count: %d"%count)if return_detail:return output_detailreturn output对于第二个问题，则是通过先填充描述的方式来解决，找到可提交的super alpha之后，再自己手动写入有意义的描述。主要修改的是get_check_submission函数，def get_check_submission(s, alpha_id, tag=None):result = _get_check_submission(s, alpha_id)try:checks_df = _get_check_result(result)if type(checks_df) == str:logging.info(checks_df)return "sleep"if tag == 'PPAC':  # PPAC alphaif 'POWER_POOL_CORRELATION' in checks_df.name.tolist():set_alpha_properties(s,alpha_id,desc = '''Idea: xxxxxxxxxxxxxxxxxxRationale for data used: xxxxxxxxxxxxxxxxxxxxxxxxRationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',)result = _get_check_submission(s, alpha_id)checks_df = _get_check_result(result)logging.info(checks_df)if type(checks_df) == str: return "sleep"pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]return pcelse:return 'fail'elif tag == 'SUPER':set_alpha_properties(s,alpha_id,selection_desc = '''Idea: xxxxxxxxxxxxxxxxxxRationale for data used: xxxxxxxxxxxxxxxxxxxxxxxxRationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',combo_desc = '''Idea: xxxxxxxxxxxxxxxxxxRationale for data used: xxxxxxxxxxxxxxxxxxxxxxxxRationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''')result = _get_check_submission(s, alpha_id)checks_df = _get_check_result(result)if type(checks_df) == str:logging.info(checks_df)return "sleep"if not any(checks_df["result"] == "FAIL"):pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]return pcelse:return "fail"else: # otherpc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]if not any(checks_df["result"] == "FAIL"):return pcelse:return "fail"except Exception as e:logging.info("catch: %s"%(alpha_id))logging.info(e)return "error"def _get_check_submission(s, alpha_id):while True:result = s.get("[链接已屏蔽] + alpha_id + "/check")if "retry-after" in result.headers:time.sleep(float(result.headers["Retry-After"]))else:breakreturn resultdef _get_check_result(result):if result.json().get("is", 0) == 0:logging.info("logged out")return "sleep"checks_df = pd.DataFrame(result.json()["is"]["checks"])return checks_df除此之外，还加入了本地自相关性检测（排除self correlation较高的因子），来减少需要api检测的因子，这部分是在../顾问 KZ79256 (Rank 21)/本地0误差计算自相关性【即插即用版】代码优化.md基础上进行了修改，感谢大佬。最后还根据pc对可提交的sa进行了排序，并且以邮件的方式发送到邮箱里，方便获取进度并及时提交。以下是完整的代码，希望对大家有所帮助。1. main.pyfrom machine_lib import *import loggingstart_date = "07-28"end_date = "07-31"sharpe_thres = 5fitness_thres = 5logging.basicConfig(format='%(asctime)s: %(message)s',level=logging.INFO,filename='log\submitalpha_super_2025{}-{}.log'.format(start_date, end_date),filemode='a',encoding='utf-8',force=True)# 增量下载已提交的alpha数据，用于本地自相关性检测download_data(flag_increment=True)# 拉取线上start_date到end_date的大于sharpe_thres且大于fitness_thres的super alphath_tracker = get_alphas(start_date, end_date, sharpe_thres, fitness_thres, "USA", 3000, "submit", return_detail=True, tag='SUPER')gold_bag = []# 本地自相关性检测silver_bag2 = []os_alpha_ids, os_alpha_pnls, ppac_alpha_ids = load_os_alphas_data()for alpha in th_tracker:alpha_id = alpha['id']self_corr = get_self_corr(alpha_id, os_alpha_ids, os_alpha_pnls, ppac_alpha_ids, alpha_result=alpha)logging.info("{}, {}".format(alpha_id, self_corr))if self_corr < 0.7:silver_bag2.append((self_corr, alpha_id))silver_bag2.sort(key = lambda x : x[0])silver_bag3 = [alpha_id for _, alpha_id in silver_bag2]logging.info("len(silver_bag3): {}".format(len(silver_bag3)))# api检测check_submission(silver_bag3, gold_bag, 0, tag='SUPER')if len(gold_bag) == 0:send_email('no alpha')else:# 打印可提交的alpha信息并按pc排序sharp_list = view_alphas(gold_bag, tag="SUPER")# 写邮件并发送email_str = ''for gold_alpha_info in sharp_list[:50]:alpha_id, sharpe, turnover, fitness, margin, _, _, prod_corr = gold_alpha_infoself_corr = find_self_corr_using_listcomp(silver_bag2, alpha_id)email_str += 'alpha_id: {}, self_corr: {}, prod_corr: {}, sharpe: {}, turnover: {}, fitness: {}, margin: {}\n'.format(alpha_id, self_corr, prod_corr, sharpe, turnover, fitness, margin)logging.info(email_str)send_email(email_str)2、machine_lib.py相关代码部分import requestsfrom os import environfrom time import sleepimport timeimport jsonimport pandas as pdimport randomimport picklefrom urllib.parse import urljoinfrom itertools import productfrom itertools import combinationsfrom collections import defaultdictimport pickleimport loggingdef download_data(flag_increment=True):"""下载数据并保存到指定路径。此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。Args:flag_increment (bool): 是否使用增量下载，默认为 True。"""if flag_increment:try:os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]except Exception as e:# logging.error(f"Failed to load existing data: {e}")os_alpha_ids = Noneos_alpha_pnls = Noneexist_alpha = []ppac_alpha_ids = []else:os_alpha_ids = Noneos_alpha_pnls = Noneexist_alpha = []ppac_alpha_ids = []if os_alpha_ids is None:alphas = get_os_alphas(limit=100, get_first=False)else:alphas = get_os_alphas(limit=30, get_first=True)alphas = [item for item in alphas if item['id'] not in exist_alpha]ppac_alpha_ids += [item['id'] for item in alphas for item_match in item['classifications'] if item_match['name'] == 'Power Pool Alpha']os_alpha_ids, os_alpha_pnls = get_alpha_pnls(alphas, alpha_pnls=os_alpha_pnls, alpha_ids=os_alpha_ids)save_obj(os_alpha_ids, str(cfg.data_path / 'os_alpha_ids'))save_obj(os_alpha_pnls, str(cfg.data_path / 'os_alpha_pnls'))save_obj(ppac_alpha_ids, str(cfg.data_path / 'ppac_alpha_ids'))# logging.info(f'新下载的alpha数量: {len(alphas)}, 目前总共alpha数量: {os_alpha_pnls.shape[1]}')def load_obj(name: str) -> object:"""加载指定名称的 pickle 文件并返回其内容。此函数会打开一个以 `.pickle` 为扩展名的文件，并使用 `pickle` 模块加载其内容。Args:name (str): 不带扩展名的文件名称。Returns:object: 从 pickle 文件中加载的 Python 对象。Raises:FileNotFoundError: 如果指定的文件不存在。pickle.UnpicklingError: 如果文件内容无法被正确反序列化。"""with open(name + '.pickle', 'rb') as f:return pickle.load(f)def get_os_alphas(limit: int = 100, get_first: bool = False, exist_alpha_num: int = 0) -> List[Dict]:"""获取OS阶段的alpha列表。此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。Args:limit (int, optional): 每次请求获取的alpha数量限制。默认为100。get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。Returns:List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。"""fetched_alphas = []offset = 0retries = 0# total_alphas = 100while True:try:url = f"[链接已屏蔽] = wait_get(url).json()total_alphas = res['count']breakexcept Exception as e:logging.info(e)sleep(600)s = login()if get_first:limit = total_alphas - exist_alpha_numwhile len(fetched_alphas) < total_alphas:# logging.info(f"Fetching alphas from offset {offset} to {offset + limit}")while True:try:url = f"[链接已屏蔽] = wait_get(url).json()if offset == 0:total_alphas = res['count']alphas = res["results"]breakexcept Exception as e:logging.info(e)sleep(600)s = login()fetched_alphas.extend(alphas)if len(alphas) < limit:breakoffset += limitif get_first:breakreturn fetched_alphas[:total_alphas]def get_alpha_pnls(alphas: list[dict],alpha_pnls: Optional[pd.DataFrame] = None,alpha_ids: Optional[dict[str, list]] = None) -> Tuple[dict[str, list], pd.DataFrame]:"""获取 alpha 的 PnL 数据，并按区域分类 alpha 的 ID。Args:alphas (list[dict]): 包含 alpha 信息的列表，每个元素是一个字典，包含 alpha 的 ID 和设置等信息。alpha_pnls (Optional[pd.DataFrame], 可选): 已有的 alpha PnL 数据，默认为空的 DataFrame。alpha_ids (Optional[dict[str, list]], 可选): 按区域分类的 alpha ID 字典，默认为空字典。Returns:Tuple[dict[str, list], pd.DataFrame]:- 按区域分类的 alpha ID 字典。- 包含所有 alpha 的 PnL 数据的 DataFrame。"""while True:try:if alpha_ids is None:alpha_ids = defaultdict(list)if alpha_pnls is None:alpha_pnls = pd.DataFrame()new_alphas = [item for item in alphas if item['id'] not in alpha_pnls.columns]if not new_alphas:return alpha_ids, alpha_pnlsfor item_alpha in new_alphas:alpha_ids[item_alpha['settings']['region']].append(item_alpha['id'])fetch_pnl_func = lambda alpha_id: _get_alpha_pnl(alpha_id).set_index('Date')with ThreadPoolExecutor(max_workers=10) as executor:results = executor.map(fetch_pnl_func, [item['id'] for item in new_alphas])alpha_pnls = pd.concat([alpha_pnls] + list(results), axis=1)alpha_pnls.sort_index(inplace=True)breakexcept Exception as e:logging.info(e)sleep(600)s = login()return alpha_ids, alpha_pnlsdef wait_get(url: str, max_retries: int = 10) -> "Response":"""发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。Args:url (str): 目标 URL。max_retries (int, optional): 最大重试次数，默认为 10。Returns:Response: 请求的响应对象。"""retries = 0while retries < max_retries:while True:simulation_progress = sess.get(url)if simulation_progress.headers.get("Retry-After", 0) == 0:breaktime.sleep(float(simulation_progress.headers["Retry-After"]))if simulation_progress.status_code < 400:breakelse:time.sleep(2 ** retries)retries += 1return simulation_progressdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:"""获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，并将其转换为 pandas DataFrame 格式，方便后续数据处理。Args:alpha_id (str): Alpha 的唯一标识符。Returns:pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。"""while True:try:pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])df = df.rename(columns={'date':'Date', 'pnl':alpha_id})df = df[['Date', alpha_id]]breakexcept Exception as e:logging.info(e)sleep(600)s = login()return dfdef save_obj(obj: object, name: str) -> None:"""保存对象到文件中，以 pickle 格式序列化。Args:obj (object): 需要保存的对象。name (str): 文件名（不包含扩展名），保存的文件将以 '.pickle' 为扩展名。Returns:None: 此函数无返回值。Raises:pickle.PickleError: 如果序列化过程中发生错误。IOError: 如果文件写入过程中发生 I/O 错误。"""with open(name + '.pickle', 'wb') as f:pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage, return_detail=False, tag='REGULAR'):s = login()output = []output_detail = []# 3E large 3C lesscount = 0if tag == 'PPAC':tag = 'REGULAR'sub_tag = 'PPAC'else: sub_tag = ''for i in range(0, alpha_num, 100):logging.info(i)# 大于url_e = "[链接已屏蔽]) \+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \+ "T00:00:00-04:00&dateCreated%3C2025-" + end_date \+ "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \+ str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false" #&type!=SUPER"# 小于url_c = "[链接已屏蔽]) \+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \+ "T00:00:00-04:00&dateCreated%3C2025-" + end_date \+ "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \+ str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false" #&type!=SUPER"urls = [url_e]if usage != "submit":urls.append(url_c)for url in urls:response = s.get(url)#logging.info(response.json())try:alpha_list = response.json()["results"]#logging.info(response.json())for j in range(len(alpha_list)):alpha_type = alpha_list[j]["type"]alpha_id = alpha_list[j]["id"]name = alpha_list[j]["name"]dateCreated = alpha_list[j]["dateCreated"]sharpe = alpha_list[j]["is"]["sharpe"]fitness = alpha_list[j]["is"]["fitness"]turnover = alpha_list[j]["is"]["turnover"]margin = alpha_list[j]["is"]["margin"]longCount = alpha_list[j]["is"]["longCount"]shortCount = alpha_list[j]["is"]["shortCount"]decay = alpha_list[j]["settings"]["decay"]if alpha_type == tag:if tag == 'SUPER':exp = alpha_list[j]['selection']['code']#[, alpha_list[j]['combo']['code']]elif sub_tag == 'PPAC':operatercount = alpha_list[j]['regular']['operatorCount']exp = alpha_list[j]['regular']['code']if operatercount > 8:continueelse:exp = alpha_list[j]['regular']['code']else:continuecount += 1#if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):if (longCount + shortCount) > 100:if sharpe < -sharpe_th:exp = "-%s"%exprec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]logging.info(rec)if turnover > 0.7:rec.append(decay*4)elif turnover > 0.6:rec.append(decay*3+3)elif turnover > 0.5:rec.append(decay*3)elif turnover > 0.4:rec.append(decay*2)elif turnover > 0.35:rec.append(decay+4)elif turnover > 0.3:rec.append(decay+2)output.append(rec)output_detail.append(alpha_list[j])except:logging.info("%d finished re-login"%i)s = login()logging.info("count: %d"%count)if return_detail:return output_detailreturn outputdef load_os_alphas_data(alpha_ids_file='os_alpha_ids', alpha_pnls_file='os_alpha_pnls', ppac_alpha_ids_file='ppac_alpha_ids'):os_alpha_ids = load_obj(str(cfg.data_path / alpha_ids_file))os_alpha_pnls = load_obj(str(cfg.data_path / alpha_pnls_file))ppac_alpha_ids = load_obj(str(cfg.data_path / ppac_alpha_ids_file))return os_alpha_ids, os_alpha_pnls, ppac_alpha_idsimport copydef get_self_corr(alpha_id, os_alpha_ids_ori, os_alpha_pnls_ori, ppac_alpha_ids_ori, track=False, tag=None, alpha_result=None):# logging.info('os_alpha_ids:{}'.format(os_alpha_ids))os_alpha_ids, os_alpha_pnls, ppac_alpha_ids = copy.deepcopy(os_alpha_ids_ori), copy.deepcopy(os_alpha_pnls_ori), copy.deepcopy(ppac_alpha_ids_ori)os_alpha_ids, os_alpha_rets = load_data(os_alpha_ids, os_alpha_pnls, ppac_alpha_ids, tag=tag, tar_alpha_id=alpha_id)if not track:self_corr = calc_self_corr(alpha_id=alpha_id,os_alpha_rets=os_alpha_rets,os_alpha_ids=os_alpha_ids,alpha_result=alpha_result)return self_correlse:self_corr, high_corr_alpha_ids, high_corrs = calc_self_corr_track(alpha_id=alpha_id,os_alpha_rets=os_alpha_rets,os_alpha_ids=os_alpha_ids,alpha_result=alpha_result)return high_corr_alpha_ids, high_corrsdef load_data(os_alpha_ids, os_alpha_pnls, ppac_alpha_ids, tag=None, tar_alpha_id=''):"""加载数据。此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。Args:tag (str): 数据标记，默认为 None。"""if tag=='PPAC':for item in os_alpha_ids:os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha in ppac_alpha_ids]elif tag=='SelfCorr':for item in os_alpha_ids:os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha not in ppac_alpha_ids]else:os_alpha_ids = os_alpha_idsexist_alpha = []for k, ids in os_alpha_ids.items():pop_index = Nonefor i, alpha in enumerate(ids):if alpha != tar_alpha_id:exist_alpha.append(alpha)else:pop_index = iif pop_index is not None: ids.pop(pop_index)os_alpha_ids[k] = ids# logging.info('os_alpha_ids:{}'.format(os_alpha_ids))os_alpha_pnls = os_alpha_pnls[exist_alpha]os_alpha_rets = os_alpha_pnls - os_alpha_pnls.ffill().shift(1)os_alpha_rets = os_alpha_rets[pd.to_datetime(os_alpha_rets.index)>pd.to_datetime(os_alpha_rets.index).max() - pd.DateOffset(years=4)]return os_alpha_ids, os_alpha_retsdef calc_self_corr(alpha_id,os_alpha_rets = None,os_alpha_ids = None,alpha_result = None,return_alpha_pnls = False,alpha_pnls = None):"""计算指定 alpha 与其他 alpha 的最大自相关性。Args:alpha_id (str): 目标 alpha 的唯一标识符。os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。Returns:float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。"""if alpha_result is None:alpha_result = wait_get(f"[链接已屏蔽]).json()if alpha_pnls is not None:if len(alpha_pnls) == 0:alpha_pnls = Noneif alpha_pnls is None:_, alpha_pnls = get_alpha_pnls([alpha_result])alpha_pnls = alpha_pnls[alpha_id]alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]# os_alpha_rets = os_alpha_rets.replace(0, np.nan)# alpha_rets = alpha_rets.replace(0, np.nan)# logging.info(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()if np.isnan(self_corr):self_corr = 0if return_alpha_pnls:return self_corr, alpha_pnlselse:return self_corrdef calc_self_corr_track(alpha_id,os_alpha_rets = None,os_alpha_ids = None,alpha_result = None,return_alpha_pnls = False,alpha_pnls = None):"""计算指定 alpha 与其他 alpha 的最大自相关性。Args:alpha_id (str): 目标 alpha 的唯一标识符。os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。Returns:float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。"""if alpha_result is None:alpha_result = wait_get(f"[链接已屏蔽]).json()if alpha_pnls is not None:if len(alpha_pnls) == 0:alpha_pnls = Noneif alpha_pnls is None:_, alpha_pnls = get_alpha_pnls([alpha_result])alpha_pnls = alpha_pnls[alpha_id]alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]# os_alpha_rets = os_alpha_rets.replace(0, np.nan)# alpha_rets = alpha_rets.replace(0, np.nan)# logging.info(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))corr_series = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4)high_corr_alpha_ids = corr_series[corr_series > 0.7].index.tolist()high_corrs = corr_series[corr_series > 0.7].tolist()self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()if np.isnan(self_corr):self_corr = 0if return_alpha_pnls:return self_corr, alpha_pnls, high_corr_alpha_ids, high_corrselse:return self_corr, high_corr_alpha_ids, high_corrsfrom tqdm import tqdmdef check_submission(alpha_bag, gold_bag, start, tag=None):depot = []s = login()for idx, g in tqdm(enumerate(alpha_bag), desc='check submit'):if idx < start:continue# if idx % 5 == 0:#     logging.info(idx)if idx % 200 == 0:s = login()#logging.info(idx)pc = get_check_submission(s, g, tag=tag)logging.info(pc)if pc == "sleep":logging.info("sleep")sleep(100)s = login()alpha_bag.append(g)elif pc != pc:# pc is nanlogging.info("check self-corrlation error")sleep(100)alpha_bag.append(g)elif pc == "fail":logging.info(g)continueelif pc == "error":depot.append(g)else:logging.info(g)gold_bag.append((g, pc))logging.info(depot)return gold_bagdef get_check_submission(s, alpha_id, tag=None):result = _get_check_submission(s, alpha_id)# logging.info(result.json())try:checks_df = _get_check_result(result)if type(checks_df) == str:logging.info(checks_df)return "sleep"# logging.info(alpha_id)# logging.info(checks_df)# logging.info(checks_df.name.tolist())if tag == 'PPAC':  # PPAC alphaif 'POWER_POOL_CORRELATION' in checks_df.name.tolist():set_alpha_properties(s,alpha_id,desc = '''Idea: xxxxxxxxxxxxxxxxxxRationale for data used: xxxxxxxxxxxxxxxxxxxxxxxxRationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',)result = _get_check_submission(s, alpha_id)checks_df = _get_check_result(result)logging.info(checks_df)if type(checks_df) == str: return "sleep"pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]return pcelse:return 'fail'elif tag == 'SUPER':set_alpha_properties(s,alpha_id,selection_desc = '''Idea: xxxxxxxxxxxxxxxxxxRationale for data used: xxxxxxxxxxxxxxxxxxxxxxxxRationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',combo_desc = '''Idea: xxxxxxxxxxxxxxxxxxRationale for data used: xxxxxxxxxxxxxxxxxxxxxxxxRationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''')# if all(v != "FAIL" for k, v in checks_df.items() if "DESCRIPTION" not in k):result = _get_check_submission(s, alpha_id)checks_df = _get_check_result(result)if type(checks_df) == str:logging.info(checks_df)return "sleep"if not any(checks_df["result"] == "FAIL"): # all(v != "FAIL" for k, v in checks_df.items() if k != "LONG_DURATION"): #pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]return pcelse:return "fail"else: # otherpc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]if not any(checks_df["result"] == "FAIL"): # all(v != "FAIL" for k, v in checks_df.items() if k != "LONG_DURATION"): #return pcelse:return "fail"except Exception as e:logging.info("catch: %s"%(alpha_id))logging.info(e)return "error"def _get_check_submission(s, alpha_id):while True:result = s.get("[链接已屏蔽] + alpha_id + "/check")if "retry-after" in result.headers:# logging.info("sleep for {}".format(float(result.headers["Retry-After"])))time.sleep(float(result.headers["Retry-After"]))else:breakreturn resultdef _get_check_result(result):if result.json().get("is", 0) == 0:logging.info("logged out")return "sleep"checks_df = pd.DataFrame(result.json()["is"]["checks"])return checks_dfdef set_alpha_properties(s,alpha_id,name: str = None,color: str = None,desc: str = "None",selection_desc: str = "None",combo_desc: str = "None",tags: str = ["ace_tag"],):"""Function changes alpha's description parameters"""params = {"color": color,"name": name,"tags": tags,"category": None,"regular": {"description": desc},"combo": {"description": combo_desc},"selection": {"description": selection_desc},}response = s.patch("[链接已屏蔽] + alpha_id, json=params)import smtplibimport email.utilsfrom email.mime.text import MIMETextdef send_email(content):name = "xxx"  # 自定义名字email_address = "xxxxxxx@qq.com" # 想要发送的邮箱地址code = "xxxxxxxxxxx"  # 授权码，获取方式网上搜下# 创建MIMEText对象，设置邮件内容message = MIMEText(content)# 设置收件人和发件人信息message['To'] = email.utils.formataddr((name, email_address))message['From'] = email.utils.formataddr((name, email_address))# 设置邮件主题message['Subject'] = '程序运行完成通知'# 连接到QQ邮箱的SMTP服务器server = smtplib.SMTP_SSL('smtp.qq.com', 465)# 使用邮箱和授权码登录server.login(email_address, code)try:# 发送邮件server.sendmail(email_address, [email_address], message.as_string())server.quit()print("邮件发送成功")except Exception as e:# 异常处理print("邮件发送失败:", e)def view_alphas(gold_bag, tag=None):s = login()sharp_list = []for gold, pc in gold_bag:triple = locate_alpha(s, gold)info = [triple[0], triple[2], triple[3], triple[4], triple[5], triple[6], triple[1]]info.append(pc)sharp_list.append(info)if tag == 'SUPER':sharp_list.sort(reverse=True, key = lambda x : (-x[-1], x[1]))else:sharp_list.sort(reverse=True, key = lambda x : (x[1], -x[-1]))logging.info('可提交的alpha:')for i in sharp_list:logging.info(i)return sharp_listdef locate_alpha(s, alpha_id):while True:alpha = s.get("[链接已屏蔽] + alpha_id)if "retry-after" in alpha.headers:time.sleep(float(alpha.headers["Retry-After"]))else:breakstring = alpha.content.decode('utf-8')metrics = json.loads(string)#logging.info(metrics["regular"]["code"])dateCreated = metrics["dateCreated"]sharpe = metrics["is"]["sharpe"]fitness = metrics["is"]["fitness"]turnover = metrics["is"]["turnover"]margin = metrics["is"]["margin"]decay = metrics["settings"]["decay"]try:exp = metrics['regular']['code']except:exp = metrics['selection']['code']triple = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]return tripledef find_self_corr_using_listcomp(silver_bag2, target_alpha_id):results = [self_corr for self_corr, alpha_id in silver_bag2 if alpha_id == target_alpha_id]return results[0] if results else None

---

### 帖子 #7: 【代码分享】检测可提交的SuperAlpha
- **主帖链接**: https://support.worldquantbrain.com【代码分享】检测可提交的SuperAlpha_33841017342999.md
- **讨论数**: 0

本人最近刚开通了super alpha的权限，使用了论坛中的 [[L2] 一种随机生成 SuperAlpha进行机器回测的方式代码优化_32009801307671.md]([L2] 一种随机生成 SuperAlpha进行机器回测的方式代码优化_32009801307671.md)  分享的方式生成了super alpha,感谢大佬的分享，但是在搜索检测可提交的alpha的时候遇到了问题：

- 如何只拉取super alpha到本地？
- super alpha需要写描述之后才能提交，如果没写描述，api检测是不通过的，如何解决这个问题，找到除了缺少描述之外所有指标都可提交的super alpha？

经过一段时间的努力，终于解决了上述问题。对于第一个问题，修改machine_lib的get_alphas函数，删除url中type!=SUPER部分，且按照请求返回的type字段来区分alpha的类型，就可以只获得super alpha。

```
def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage, return_detail=False, tag='REGULAR'):    s = login()    output = []    output_detail = []    # 3E large 3C less    count = 0    if tag == 'PPAC':        tag = 'REGULAR'        sub_tag = 'PPAC'    else: sub_tag = ''    for i in range(0, alpha_num, 100):        logging.info(i)        # 大于        url_e = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \                + "T00:00:00-04:00&dateCreated%3C2025-" + end_date \                + "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \                + str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false" #&type!=SUPER"        # 小于        url_c = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \                + "T00:00:00-04:00&dateCreated%3C2025-" + end_date \                + "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \                + str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false" #&type!=SUPER"        urls = [url_e]        if usage != "submit":            urls.append(url_c)        for url in urls:            response = s.get(url)            #logging.info(response.json())            try:                alpha_list = response.json()["results"]                #logging.info(response.json())                for j in range(len(alpha_list)):                    alpha_type = alpha_list[j]["type"]                    alpha_id = alpha_list[j]["id"]                    name = alpha_list[j]["name"]                    dateCreated = alpha_list[j]["dateCreated"]                    sharpe = alpha_list[j]["is"]["sharpe"]                    fitness = alpha_list[j]["is"]["fitness"]                    turnover = alpha_list[j]["is"]["turnover"]                    margin = alpha_list[j]["is"]["margin"]                    longCount = alpha_list[j]["is"]["longCount"]                    shortCount = alpha_list[j]["is"]["shortCount"]                    decay = alpha_list[j]["settings"]["decay"]                    if alpha_type == tag:                        if tag == 'SUPER':                            exp = alpha_list[j]['selection']['code']#[, alpha_list[j]['combo']['code']]                                    elif sub_tag == 'PPAC':                            operatercount = alpha_list[j]['regular']['operatorCount']                            exp = alpha_list[j]['regular']['code']                            if operatercount > 8:                                continue                        else:                            exp = alpha_list[j]['regular']['code']                    else:                        continue                    count += 1                    #if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):                    if (longCount + shortCount) > 100:                        if sharpe < -sharpe_th:                            exp = "-%s"%exp                        rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]                        logging.info(rec)                        if turnover > 0.7:                            rec.append(decay*4)                        elif turnover > 0.6:                            rec.append(decay*3+3)                        elif turnover > 0.5:                            rec.append(decay*3)                        elif turnover > 0.4:                            rec.append(decay*2)                        elif turnover > 0.35:                            rec.append(decay+4)                        elif turnover > 0.3:                            rec.append(decay+2)                        output.append(rec)                        output_detail.append(alpha_list[j])            except:                logging.info("%d finished re-login"%i)                s = login()    logging.info("count: %d"%count)    if return_detail:        return output_detail    return output
```

对于第二个问题，则是通过先填充描述的方式来解决，找到可提交的super alpha之后，再自己手动写入有意义的描述。主要修改的是get_check_submission函数，

```
def get_check_submission(s, alpha_id, tag=None):    result = _get_check_submission(s, alpha_id)    try:        checks_df = _get_check_result(result)        if type(checks_df) == str:             logging.info(checks_df)            return "sleep"        if tag == 'PPAC':  # PPAC alpha            if 'POWER_POOL_CORRELATION' in checks_df.name.tolist():                set_alpha_properties(s,                    alpha_id,                    desc = '''Idea: xxxxxxxxxxxxxxxxxx    Rationale for data used: xxxxxxxxxxxxxxxxxxxxxxxx    Rationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',)                result = _get_check_submission(s, alpha_id)                checks_df = _get_check_result(result)                logging.info(checks_df)                if type(checks_df) == str: return "sleep"                pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]                return pc            else:                return 'fail'        elif tag == 'SUPER':            set_alpha_properties(s,                alpha_id,                selection_desc = '''Idea: xxxxxxxxxxxxxxxxxx    Rationale for data used: xxxxxxxxxxxxxxxxxxxxxxxx    Rationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',                combo_desc = '''Idea: xxxxxxxxxxxxxxxxxx    Rationale for data used: xxxxxxxxxxxxxxxxxxxxxxxx    Rationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''')            result = _get_check_submission(s, alpha_id)            checks_df = _get_check_result(result)            if type(checks_df) == str:                 logging.info(checks_df)                return "sleep"            if not any(checks_df["result"] == "FAIL"):                pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]                return pc            else:                return "fail"        else: # other            pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]            if not any(checks_df["result"] == "FAIL"):                 return pc            else:                return "fail"    except Exception as e:        logging.info("catch: %s"%(alpha_id))        logging.info(e)        return "error"def _get_check_submission(s, alpha_id):    while True:        result = s.get("[链接已屏蔽] + alpha_id + "/check")        if "retry-after" in result.headers:            time.sleep(float(result.headers["Retry-After"]))        else:            break    return resultdef _get_check_result(result):    if result.json().get("is", 0) == 0:        logging.info("logged out")        return "sleep"    checks_df = pd.DataFrame(            result.json()["is"]["checks"]    )  return checks_df
```

除此之外，还加入了本地自相关性检测（排除self correlation较高的因子），来减少需要api检测的因子，这部分是在 [[L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md]([L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md)  基础上进行了修改，感谢大佬。

最后还根据pc对可提交的sa进行了排序，并且以邮件的方式发送到邮箱里，方便获取进度并及时提交。

以下是完整的代码，希望对大家有所帮助。

1. main.py

```
from machine_lib import * import loggingstart_date = "07-28"end_date = "07-31"sharpe_thres = 5fitness_thres = 5logging.basicConfig(format='%(asctime)s: %(message)s',                    level=logging.INFO,                    filename='log\submitalpha_super_2025{}-{}.log'.format(start_date, end_date),                    filemode='a',encoding='utf-8',force=True)# 增量下载已提交的alpha数据，用于本地自相关性检测download_data(flag_increment=True)# 拉取线上start_date到end_date的大于sharpe_thres且大于fitness_thres的super alphath_tracker = get_alphas(start_date, end_date, sharpe_thres, fitness_thres, "USA", 3000, "submit", return_detail=True, tag='SUPER')gold_bag = []# 本地自相关性检测silver_bag2 = []os_alpha_ids, os_alpha_pnls, ppac_alpha_ids = load_os_alphas_data()for alpha in th_tracker:    alpha_id = alpha['id']    self_corr = get_self_corr(alpha_id, os_alpha_ids, os_alpha_pnls, ppac_alpha_ids, alpha_result=alpha)    logging.info("{}, {}".format(alpha_id, self_corr))    if self_corr < 0.7:        silver_bag2.append((self_corr, alpha_id))silver_bag2.sort(key = lambda x : x[0])silver_bag3 = [alpha_id for _, alpha_id in silver_bag2]logging.info("len(silver_bag3): {}".format(len(silver_bag3)))# api检测check_submission(silver_bag3, gold_bag, 0, tag='SUPER')if len(gold_bag) == 0:    send_email('no alpha')else:    # 打印可提交的alpha信息并按pc排序    sharp_list = view_alphas(gold_bag, tag="SUPER")    # 写邮件并发送    email_str = ''    for gold_alpha_info in sharp_list[:50]:        alpha_id, sharpe, turnover, fitness, margin, _, _, prod_corr = gold_alpha_info        self_corr = find_self_corr_using_listcomp(silver_bag2, alpha_id)        email_str += 'alpha_id: {}, self_corr: {}, prod_corr: {}, sharpe: {}, turnover: {}, fitness: {}, margin: {}\n'.format(alpha_id, self_corr, prod_corr, sharpe, turnover, fitness, margin)    logging.info(email_str)    send_email(email_str)
```

2、machine_lib.py相关代码部分

```
import requestsfrom os import environfrom time import sleepimport timeimport jsonimport pandas as pdimport randomimport picklefrom urllib.parse import urljoinfrom itertools import productfrom itertools import combinationsfrom collections import defaultdictimport pickleimport loggingdef download_data(flag_increment=True):    """    下载数据并保存到指定路径。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        flag_increment (bool): 是否使用增量下载，默认为 True。    """    if flag_increment:        try:            os_alpha_ids = load_obj(str(cfg.data_path / 'os_alpha_ids'))            os_alpha_pnls = load_obj(str(cfg.data_path / 'os_alpha_pnls'))            ppac_alpha_ids = load_obj(str(cfg.data_path / 'ppac_alpha_ids'))            exist_alpha = [alpha for ids in os_alpha_ids.values() for alpha in ids]        except Exception as e:            # logging.error(f"Failed to load existing data: {e}")            os_alpha_ids = None            os_alpha_pnls = None            exist_alpha = []            ppac_alpha_ids = []    else:        os_alpha_ids = None        os_alpha_pnls = None        exist_alpha = []        ppac_alpha_ids = []           if os_alpha_ids is None:        alphas = get_os_alphas(limit=100, get_first=False)    else:        alphas = get_os_alphas(limit=30, get_first=True)       alphas = [item for item in alphas if item['id'] not in exist_alpha]    ppac_alpha_ids += [item['id'] for item in alphas for item_match in item['classifications'] if item_match['name'] == 'Power Pool Alpha']               os_alpha_ids, os_alpha_pnls = get_alpha_pnls(alphas, alpha_pnls=os_alpha_pnls, alpha_ids=os_alpha_ids)    save_obj(os_alpha_ids, str(cfg.data_path / 'os_alpha_ids'))    save_obj(os_alpha_pnls, str(cfg.data_path / 'os_alpha_pnls'))    save_obj(ppac_alpha_ids, str(cfg.data_path / 'ppac_alpha_ids'))    # logging.info(f'新下载的alpha数量: {len(alphas)}, 目前总共alpha数量: {os_alpha_pnls.shape[1]}')def load_obj(name: str) -> object:    """    加载指定名称的 pickle 文件并返回其内容。    此函数会打开一个以 `.pickle` 为扩展名的文件，并使用 `pickle` 模块加载其内容。    Args:        name (str): 不带扩展名的文件名称。    Returns:        object: 从 pickle 文件中加载的 Python 对象。    Raises:        FileNotFoundError: 如果指定的文件不存在。        pickle.UnpicklingError: 如果文件内容无法被正确反序列化。    """    with open(name + '.pickle', 'rb') as f:        return pickle.load(f)def get_os_alphas(limit: int = 100, get_first: bool = False, exist_alpha_num: int = 0) -> List[Dict]:    """    获取OS阶段的alpha列表。    此函数通过调用WorldQuant Brain API获取用户的alpha列表，支持分页获取，并可以选择只获取第一个结果。    Args:        limit (int, optional): 每次请求获取的alpha数量限制。默认为100。        get_first (bool, optional): 是否只获取第一次请求的alpha结果。如果为True，则只请求一次。默认为False。    Returns:        List[Dict]: 包含alpha信息的字典列表，每个字典表示一个alpha。    """    fetched_alphas = []    offset = 0    retries = 0    # total_alphas = 100    while True:        try:            url = f"[链接已屏蔽]            res = wait_get(url).json()            total_alphas = res['count']            break        except Exception as e:            logging.info(e)            sleep(600)            s = login()       if get_first:        limit = total_alphas - exist_alpha_num    while len(fetched_alphas) < total_alphas:        # logging.info(f"Fetching alphas from offset {offset} to {offset + limit}")        while True:            try:                url = f"[链接已屏蔽]                res = wait_get(url).json()                if offset == 0:                    total_alphas = res['count']                alphas = res["results"]                break            except Exception as e:                logging.info(e)                sleep(600)                s = login()        fetched_alphas.extend(alphas)        if len(alphas) < limit:            break        offset += limit        if get_first:            break    return fetched_alphas[:total_alphas]def get_alpha_pnls(    alphas: list[dict],    alpha_pnls: Optional[pd.DataFrame] = None,    alpha_ids: Optional[dict[str, list]] = None) -> Tuple[dict[str, list], pd.DataFrame]:    """    获取 alpha 的 PnL 数据，并按区域分类 alpha 的 ID。    Args:        alphas (list[dict]): 包含 alpha 信息的列表，每个元素是一个字典，包含 alpha 的 ID 和设置等信息。        alpha_pnls (Optional[pd.DataFrame], 可选): 已有的 alpha PnL 数据，默认为空的 DataFrame。        alpha_ids (Optional[dict[str, list]], 可选): 按区域分类的 alpha ID 字典，默认为空字典。    Returns:        Tuple[dict[str, list], pd.DataFrame]:            - 按区域分类的 alpha ID 字典。            - 包含所有 alpha 的 PnL 数据的 DataFrame。    """    while True:        try:            if alpha_ids is None:                alpha_ids = defaultdict(list)            if alpha_pnls is None:                alpha_pnls = pd.DataFrame()                    new_alphas = [item for item in alphas if item['id'] not in alpha_pnls.columns]            if not new_alphas:                return alpha_ids, alpha_pnls                    for item_alpha in new_alphas:                alpha_ids[item_alpha['settings']['region']].append(item_alpha['id'])            fetch_pnl_func = lambda alpha_id: _get_alpha_pnl(alpha_id).set_index('Date')            with ThreadPoolExecutor(max_workers=10) as executor:                results = executor.map(fetch_pnl_func, [item['id'] for item in new_alphas])            alpha_pnls = pd.concat([alpha_pnls] + list(results), axis=1)            alpha_pnls.sort_index(inplace=True)            break        except Exception as e:            logging.info(e)            sleep(600)            s = login()    return alpha_ids, alpha_pnlsdef wait_get(url: str, max_retries: int = 10) -> "Response":    """    发送带有重试机制的 GET 请求，直到成功或达到最大重试次数。    此函数会根据服务器返回的 `Retry-After` 头信息进行等待，并在遇到 401 状态码时重新初始化配置。       Args:        url (str): 目标 URL。        max_retries (int, optional): 最大重试次数，默认为 10。       Returns:        Response: 请求的响应对象。    """    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef _get_alpha_pnl(alpha_id: str) -> pd.DataFrame:    """    获取指定 alpha 的 PnL数据，并返回一个包含日期和 PnL 的 DataFrame。    此函数通过调用 WorldQuant Brain API 获取指定 alpha 的 PnL 数据，    并将其转换为 pandas DataFrame 格式，方便后续数据处理。    Args:        alpha_id (str): Alpha 的唯一标识符。    Returns:        pd.DataFrame: 包含日期和对应 PnL 数据的 DataFrame，列名为 'Date' 和 alpha_id。    """    while True:        try:            pnl = wait_get("[链接已屏蔽] + alpha_id + "/recordsets/pnl").json()            df = pd.DataFrame(pnl['records'], columns=[item['name'] for item in pnl['schema']['properties']])            df = df.rename(columns={'date':'Date', 'pnl':alpha_id})            df = df[['Date', alpha_id]]            break        except Exception as e:            logging.info(e)            sleep(600)            s = login()    return dfdef save_obj(obj: object, name: str) -> None:    """    保存对象到文件中，以 pickle 格式序列化。    Args:        obj (object): 需要保存的对象。        name (str): 文件名（不包含扩展名），保存的文件将以 '.pickle' 为扩展名。    Returns:        None: 此函数无返回值。    Raises:        pickle.PickleError: 如果序列化过程中发生错误。        IOError: 如果文件写入过程中发生 I/O 错误。    """    with open(name + '.pickle', 'wb') as f:        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage, return_detail=False, tag='REGULAR'):    s = login()    output = []    output_detail = []    # 3E large 3C less    count = 0    if tag == 'PPAC':        tag = 'REGULAR'        sub_tag = 'PPAC'    else: sub_tag = ''    for i in range(0, alpha_num, 100):        logging.info(i)        # 大于        url_e = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \                + "T00:00:00-04:00&dateCreated%3C2025-" + end_date \                + "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \                + str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false" #&type!=SUPER"        # 小于        url_c = "[链接已屏蔽]) \                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \                + "T00:00:00-04:00&dateCreated%3C2025-" + end_date \                + "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \                + str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false" #&type!=SUPER"        urls = [url_e]        if usage != "submit":            urls.append(url_c)        for url in urls:            response = s.get(url)            #logging.info(response.json())            try:                alpha_list = response.json()["results"]                #logging.info(response.json())                for j in range(len(alpha_list)):                    alpha_type = alpha_list[j]["type"]                    alpha_id = alpha_list[j]["id"]                    name = alpha_list[j]["name"]                    dateCreated = alpha_list[j]["dateCreated"]                    sharpe = alpha_list[j]["is"]["sharpe"]                    fitness = alpha_list[j]["is"]["fitness"]                    turnover = alpha_list[j]["is"]["turnover"]                    margin = alpha_list[j]["is"]["margin"]                    longCount = alpha_list[j]["is"]["longCount"]                    shortCount = alpha_list[j]["is"]["shortCount"]                    decay = alpha_list[j]["settings"]["decay"]                    if alpha_type == tag:                        if tag == 'SUPER':                            exp = alpha_list[j]['selection']['code']#[, alpha_list[j]['combo']['code']]                                    elif sub_tag == 'PPAC':                            operatercount = alpha_list[j]['regular']['operatorCount']                            exp = alpha_list[j]['regular']['code']                            if operatercount > 8:                                continue                        else:                            exp = alpha_list[j]['regular']['code']                    else:                        continue                    count += 1                    #if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):                    if (longCount + shortCount) > 100:                        if sharpe < -sharpe_th:                            exp = "-%s"%exp                        rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]                        logging.info(rec)                        if turnover > 0.7:                            rec.append(decay*4)                        elif turnover > 0.6:                            rec.append(decay*3+3)                        elif turnover > 0.5:                            rec.append(decay*3)                        elif turnover > 0.4:                            rec.append(decay*2)                        elif turnover > 0.35:                            rec.append(decay+4)                        elif turnover > 0.3:                            rec.append(decay+2)                        output.append(rec)                        output_detail.append(alpha_list[j])            except:                logging.info("%d finished re-login"%i)                s = login()    logging.info("count: %d"%count)    if return_detail:        return output_detail    return outputdef load_os_alphas_data(alpha_ids_file='os_alpha_ids', alpha_pnls_file='os_alpha_pnls', ppac_alpha_ids_file='ppac_alpha_ids'):    os_alpha_ids = load_obj(str(cfg.data_path / alpha_ids_file))    os_alpha_pnls = load_obj(str(cfg.data_path / alpha_pnls_file))    ppac_alpha_ids = load_obj(str(cfg.data_path / ppac_alpha_ids_file))    return os_alpha_ids, os_alpha_pnls, ppac_alpha_idsimport copydef get_self_corr(alpha_id, os_alpha_ids_ori, os_alpha_pnls_ori, ppac_alpha_ids_ori, track=False, tag=None, alpha_result=None):    # logging.info('os_alpha_ids:{}'.format(os_alpha_ids))    os_alpha_ids, os_alpha_pnls, ppac_alpha_ids = copy.deepcopy(os_alpha_ids_ori), copy.deepcopy(os_alpha_pnls_ori), copy.deepcopy(ppac_alpha_ids_ori)    os_alpha_ids, os_alpha_rets = load_data(os_alpha_ids, os_alpha_pnls, ppac_alpha_ids, tag=tag, tar_alpha_id=alpha_id)    if not track:        self_corr = calc_self_corr(            alpha_id=alpha_id,            os_alpha_rets=os_alpha_rets,            os_alpha_ids=os_alpha_ids,            alpha_result=alpha_result        )        return self_corr    else:        self_corr, high_corr_alpha_ids, high_corrs = calc_self_corr_track(            alpha_id=alpha_id,            os_alpha_rets=os_alpha_rets,            os_alpha_ids=os_alpha_ids,            alpha_result=alpha_result        )        return high_corr_alpha_ids, high_corrsdef load_data(os_alpha_ids, os_alpha_pnls, ppac_alpha_ids, tag=None, tar_alpha_id=''):    """    加载数据。    此函数会检查数据是否已经存在，如果不存在，则从 API 下载数据并保存到指定路径。    Args:        tag (str): 数据标记，默认为 None。    """    if tag=='PPAC':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha in ppac_alpha_ids]    elif tag=='SelfCorr':        for item in os_alpha_ids:            os_alpha_ids[item] = [alpha for alpha in os_alpha_ids[item] if alpha not in ppac_alpha_ids]    else:        os_alpha_ids = os_alpha_ids    exist_alpha = []    for k, ids in os_alpha_ids.items():        pop_index = None        for i, alpha in enumerate(ids):            if alpha != tar_alpha_id:                exist_alpha.append(alpha)            else:                pop_index = i        if pop_index is not None: ids.pop(pop_index)        os_alpha_ids[k] = ids    # logging.info('os_alpha_ids:{}'.format(os_alpha_ids))               os_alpha_pnls = os_alpha_pnls[exist_alpha]    os_alpha_rets = os_alpha_pnls - os_alpha_pnls.ffill().shift(1)    os_alpha_rets = os_alpha_rets[pd.to_datetime(os_alpha_rets.index)>pd.to_datetime(os_alpha_rets.index).max() - pd.DateOffset(years=4)]    return os_alpha_ids, os_alpha_retsdef calc_self_corr(    alpha_id,    os_alpha_rets = None,    os_alpha_ids = None,    alpha_result = None,    return_alpha_pnls = False,    alpha_pnls = None):    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    # logging.info(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))    os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4).to_csv(str(cfg.data_path / 'os_alpha_corr.csv'))    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls    else:        return self_corrdef calc_self_corr_track(    alpha_id,    os_alpha_rets = None,    os_alpha_ids = None,    alpha_result = None,    return_alpha_pnls = False,    alpha_pnls = None):    """    计算指定 alpha 与其他 alpha 的最大自相关性。    Args:        alpha_id (str): 目标 alpha 的唯一标识符。        os_alpha_rets (pd.DataFrame | None, optional): 其他 alpha 的收益率数据，默认为 None。        os_alpha_ids (dict[str, str] | None, optional): 其他 alpha 的标识符映射，默认为 None。        alpha_result (dict | None, optional): 目标 alpha 的详细信息，默认为 None。        return_alpha_pnls (bool, optional): 是否返回 alpha 的 PnL 数据，默认为 False。        alpha_pnls (pd.DataFrame | None, optional): 目标 alpha 的 PnL 数据，默认为 None。    Returns:        float | tuple[float, pd.DataFrame]: 如果 `return_alpha_pnls` 为 False，返回最大自相关性值；            如果 `return_alpha_pnls` 为 True，返回包含最大自相关性值和 alpha PnL 数据的元组。    """    if alpha_result is None:        alpha_result = wait_get(f"[链接已屏蔽]).json()    if alpha_pnls is not None:        if len(alpha_pnls) == 0:            alpha_pnls = None    if alpha_pnls is None:        _, alpha_pnls = get_alpha_pnls([alpha_result])        alpha_pnls = alpha_pnls[alpha_id]    alpha_rets = alpha_pnls - alpha_pnls.ffill().shift(1)    alpha_rets = alpha_rets[pd.to_datetime(alpha_rets.index)>pd.to_datetime(alpha_rets.index).max() - pd.DateOffset(years=4)]    # os_alpha_rets = os_alpha_rets.replace(0, np.nan)    # alpha_rets = alpha_rets.replace(0, np.nan)    # logging.info(os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4))    corr_series = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).sort_values(ascending=False).round(4)    high_corr_alpha_ids = corr_series[corr_series > 0.7].index.tolist()    high_corrs = corr_series[corr_series > 0.7].tolist()    self_corr = os_alpha_rets[os_alpha_ids[alpha_result['settings']['region']]].corrwith(alpha_rets).max()    if np.isnan(self_corr):        self_corr = 0    if return_alpha_pnls:        return self_corr, alpha_pnls, high_corr_alpha_ids, high_corrs    else:        return self_corr, high_corr_alpha_ids, high_corrsfrom tqdm import tqdmdef check_submission(alpha_bag, gold_bag, start, tag=None):    depot = []    s = login()    for idx, g in tqdm(enumerate(alpha_bag), desc='check submit'):        if idx < start:            continue        # if idx % 5 == 0:        #     logging.info(idx)        if idx % 200 == 0:            s = login()        #logging.info(idx)        pc = get_check_submission(s, g, tag=tag)        logging.info(pc)        if pc == "sleep":            logging.info("sleep")            sleep(100)            s = login()            alpha_bag.append(g)        elif pc != pc:            # pc is nan            logging.info("check self-corrlation error")            sleep(100)            alpha_bag.append(g)        elif pc == "fail":            logging.info(g)            continue        elif pc == "error":            depot.append(g)        else:            logging.info(g)            gold_bag.append((g, pc))    logging.info(depot)    return gold_bagdef get_check_submission(s, alpha_id, tag=None):    result = _get_check_submission(s, alpha_id)    # logging.info(result.json())    try:        checks_df = _get_check_result(result)        if type(checks_df) == str:             logging.info(checks_df)            return "sleep"        # logging.info(alpha_id)        # logging.info(checks_df)        # logging.info(checks_df.name.tolist())        if tag == 'PPAC':  # PPAC alpha            if 'POWER_POOL_CORRELATION' in checks_df.name.tolist():                set_alpha_properties(s,                    alpha_id,                    desc = '''Idea: xxxxxxxxxxxxxxxxxx    Rationale for data used: xxxxxxxxxxxxxxxxxxxxxxxx    Rationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',)                result = _get_check_submission(s, alpha_id)                checks_df = _get_check_result(result)                logging.info(checks_df)                if type(checks_df) == str: return "sleep"                pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]                return pc            else:                return 'fail'        elif tag == 'SUPER':            set_alpha_properties(s,                alpha_id,                selection_desc = '''Idea: xxxxxxxxxxxxxxxxxx    Rationale for data used: xxxxxxxxxxxxxxxxxxxxxxxx    Rationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''',                combo_desc = '''Idea: xxxxxxxxxxxxxxxxxx    Rationale for data used: xxxxxxxxxxxxxxxxxxxxxxxx    Rationale for operators used: xxxxxxxxxxxxxxxxxxxxxx''')            # if all(v != "FAIL" for k, v in checks_df.items() if "DESCRIPTION" not in k):            result = _get_check_submission(s, alpha_id)            checks_df = _get_check_result(result)            if type(checks_df) == str:                 logging.info(checks_df)                return "sleep"            if not any(checks_df["result"] == "FAIL"): # all(v != "FAIL" for k, v in checks_df.items() if k != "LONG_DURATION"): #                pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]                return pc            else:                return "fail"        else: # other            pc = checks_df[checks_df.name == "PROD_CORRELATION"]["value"].values[0]            if not any(checks_df["result"] == "FAIL"): # all(v != "FAIL" for k, v in checks_df.items() if k != "LONG_DURATION"): #                return pc            else:                return "fail"    except Exception as e:        logging.info("catch: %s"%(alpha_id))        logging.info(e)        return "error"def _get_check_submission(s, alpha_id):    while True:        result = s.get("[链接已屏蔽] + alpha_id + "/check")        if "retry-after" in result.headers:            # logging.info("sleep for {}".format(float(result.headers["Retry-After"])))            time.sleep(float(result.headers["Retry-After"]))        else:            break    return resultdef _get_check_result(result):    if result.json().get("is", 0) == 0:        logging.info("logged out")        return "sleep"    checks_df = pd.DataFrame(            result.json()["is"]["checks"]    )    return checks_dfdef set_alpha_properties(    s,    alpha_id,    name: str = None,    color: str = None,    desc: str = "None",    selection_desc: str = "None",    combo_desc: str = "None",    tags: str = ["ace_tag"],):    """    Function changes alpha's description parameters    """     params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": desc},        "combo": {"description": combo_desc},        "selection": {"description": selection_desc},    }    response = s.patch(        "[链接已屏蔽] + alpha_id, json=params    )import smtplibimport email.utilsfrom email.mime.text import MIMETextdef send_email(content):    name = "xxx"  # 自定义名字    email_address = "xxxxxxx@qq.com" # 想要发送的邮箱地址    code = "xxxxxxxxxxx"  # 授权码，获取方式网上搜下    # 创建MIMEText对象，设置邮件内容    message = MIMEText(content)        # 设置收件人和发件人信息    message['To'] = email.utils.formataddr((name, email_address))    message['From'] = email.utils.formataddr((name, email_address))        # 设置邮件主题    message['Subject'] = '程序运行完成通知'    # 连接到QQ邮箱的SMTP服务器    server = smtplib.SMTP_SSL('smtp.qq.com', 465)        # 使用邮箱和授权码登录    server.login(email_address, code)        try:        # 发送邮件        server.sendmail(email_address, [email_address], message.as_string())        server.quit()        print("邮件发送成功")    except Exception as e:        # 异常处理        print("邮件发送失败:", e)def view_alphas(gold_bag, tag=None):    s = login()    sharp_list = []    for gold, pc in gold_bag:        triple = locate_alpha(s, gold)        info = [triple[0], triple[2], triple[3], triple[4], triple[5], triple[6], triple[1]]        info.append(pc)        sharp_list.append(info)    if tag == 'SUPER':        sharp_list.sort(reverse=True, key = lambda x : (-x[-1], x[1]))    else:        sharp_list.sort(reverse=True, key = lambda x : (x[1], -x[-1]))    logging.info('可提交的alpha:')    for i in sharp_list:        logging.info(i)    return sharp_listdef locate_alpha(s, alpha_id):    while True:        alpha = s.get("[链接已屏蔽] + alpha_id)        if "retry-after" in alpha.headers:            time.sleep(float(alpha.headers["Retry-After"]))        else:            break    string = alpha.content.decode('utf-8')    metrics = json.loads(string)    #logging.info(metrics["regular"]["code"])        dateCreated = metrics["dateCreated"]    sharpe = metrics["is"]["sharpe"]    fitness = metrics["is"]["fitness"]    turnover = metrics["is"]["turnover"]    margin = metrics["is"]["margin"]    decay = metrics["settings"]["decay"]    try:        exp = metrics['regular']['code']    except:        exp = metrics['selection']['code']        triple = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]    return tripledef find_self_corr_using_listcomp(silver_bag2, target_alpha_id):    results = [self_corr for self_corr, alpha_id in silver_bag2 if alpha_id == target_alpha_id]    return results[0] if results else None
```

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《Step 5: 计算中性化结果》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Operator大师-用基础的operator实现复杂功能_29085671898775.md
- **评论时间**: 10个月前

ts_min可以用以下表达式替代：（ts_max同理）

```
ts_min({datafield}, {days}) = ts_backfill(if_else(ts_arg_min({datafield}, {days})==0, {datafield}, nan), 120)
```

---
