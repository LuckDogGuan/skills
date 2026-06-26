# 顾问 JX79797 (Rank 9) 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 JX79797 (Rank 9) 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location'])
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

**顾问 JX79797 (Rank 9) 的解答与建议**:
目前还用不上，看起来很有用的样子，mark一下

```
#========= WORLDQUANT BRAIN CONSULTANT ========== ## Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%# sys.setrecursionlimit(α∞) # PnL = ∑(Robustness * Creativity)#无限探索、鲁棒性优先，创新性增值#=================奋进的小徐=======================#
```


---

### 技术对话片段 2 (原帖: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location'])
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

**顾问 JX79797 (Rank 9) 的解答与建议**:
目前还用不上，看起来很有用的样子，mark一下

```
#========= WORLDQUANT BRAIN CONSULTANT ========== ## Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%# sys.setrecursionlimit(α∞) # PnL = ∑(Robustness * Creativity)#无限探索、鲁棒性优先，创新性增值#=================奋进的小徐=======================#
```


---

### 技术对话片段 3 (原帖: --- 阶段二：创建和重命名SUPER Alphas ---)
- **原帖链接**: [Commented] ValueFactor 预测器自动化滚动3个月 Alpha 表现评估代码优化.md
- **时间**: 11个月前

**提问/主帖背景 (JR23144)**:
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


**顾问 JX79797 (Rank 9) 的解答与建议**:
已下载使用，非常完美，还没来得及干的事情可以省下了

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 4 (原帖: --- 阶段二：创建和重命名SUPER Alphas ---)
- **原帖链接**: https://support.worldquantbrain.com[Commented] ValueFactor 预测器自动化滚动3个月 Alpha 表现评估代码优化_33729239058839.md
- **时间**: 11个月前

**提问/主帖背景 (JR23144)**:
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


**顾问 JX79797 (Rank 9) 的解答与建议**:
已下载使用，非常完美，还没来得及干的事情可以省下了

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 5 (原帖: [Alpha Idea]Is predictability of industry returns after M&A announcement effictive ?)
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

**顾问 JX79797 (Rank 9) 的解答与建议**:
权重微调的最后一版，明显不如前一版啊

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 6 (原帖: [Alpha Idea]Is predictability of industry returns after M&A announcement effictive ?)
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

**顾问 JX79797 (Rank 9) 的解答与建议**:
权重微调的最后一版，明显不如前一版啊

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 7 (原帖: [SuperAlpha]SELECTION框架-v2经验分享)
- **原帖链接**: [Commented] [SuperAlpha]SELECTION框架-v2经验分享.md
- **时间**: 11个月前

**提问/主帖背景 (ZS59763)**:
本文是 [组sa时如何选取高质量因子？ – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 组sa时如何选取高质量因子经验分享.md) 的优化版本，增加了一些额外的筛选项与选择思路，剔除了筛选权重排列，并使用额外的筛选条件进行替代。

以下正文：

## **select流程**

第一步：own or not own，对于expert及以上顾问适用

第二步：选择因子种类，sac2025中提供了很多可以按照因子种类进行筛选的语句，可以直接复制来用。主要包含两类，一类是因子的类别，例如atom，ppac。例：

```
in(classifications, "ATOM")
```

```
in(classifications, "POWER_POOL")
```

第三步：因子的设置。sac中有一周主题叫做风险中性化，需要用使用风险中性化的因子，这个思路感觉很好（因为在ra层面已经中性掉一些风险），也可以根据自己需求进行选择：

```
((neutralization == 'SLOW') || (neutralization == 'FAST') || (neutralization == 'SLOW_AND_FAST') || (neutralization == 'CROWDING') || (neutralization == 'STATISTICAL') || (neutralization == 'REVERSION_AND_MOMENTUM'))
```

使用常规的4个中性化亦可。

第四步：因子的类别。大家在日常跑因子的时候会感觉一些“小众”数据集跑出来的效果一般，这一步可以选取特定的数据类型。思路来源于橘子姐，在此表示感谢。例：

```
&&(in(datacategories, "fundamental")||in(datacategories, "analyst")||in(datacategories, "model")||in(datacategories, "news")||in(datacategories, "other")||in(datacategories, "risk")||in(datacategories, "pv"))
```

至于选择哪些类别，可以按需进行。例如：我想选一些差异较大的类别，那么可以选择fnd和socialmeida，如果我想针对基本面进行选择，则可以囊括fnd，anl，ern。

第五步：分层方式：之前的版本中提出用turnover进行分层，理由是一个因子的turnover不能反映因子的表现，但turnover可以把因子池划分成若干个区间，每次取不同的区间可以避免重复选取。除去turnover之外，也可以按照long count，short count进行分层。count数也不能反映因子表现，但可以分层。例：

```
turnover<0.1&&turnover>0.05
```

```
long_count>1000&&long_count<1200
```

```
a=sqrt(long_count*short_count);a>1000&&a<1200
```

第六步：相关性限制

经与weijie老师讨论，一味地选取低相关性可能不是很好的选择。因为有些好的因子被反复选到后相关性提高，初步的解决方式是利用prodcor和selfcor进行类似powerpool的双重选择。例：

```
((prod_correlation<0.6&&prod_correlation>0.1)&&(self_correlation<0.3&&self_correlation>0.05))  
```

第七步：运算符与字段个数选择。我们早就知道，过多的op和过多的字段不可避免地会带来过拟合，之前的版本中只是选择了op数目进行限制，这是有偏颇的。一阶因子的稳定度不如二阶，有些字段信号强到甚至可以“裸交”，但质量一般。为了剔除掉这些因子，可以采用op数目上下界+字段个数上界的方式进行选择。例：

```
&&(operator_count<=8)&&(operator_count>=2)&&(datafield_count<=3)
```

第八步：decay和truncation选择。这一步的目的是剔除掉一些没有经济学含义，靠着一味调整decay从而实现提交的因子。decay可以选择0,1,3,5,20等有经济学含义的参数。而不是17,29这种没有实质含义的参数。至于truncation，这是为了满足weight分布所做，truncation太高的ppa可能会有weight的warning，从而使得sa的weight不被均匀分布。例：

```
&&(decay<=5)&&(truncation<=0.1)  
```

第九步：universe选择。usa，asi等地区都有illliquid的universe，这些地区的因子大多是靠着低流动性挣钱，会造成maxtrade线和pnl的分歧，在费后表现也没有保障，可以通过universe参数剔除。

```
&&(universe=='TOP2500')
```

第十步：检查选择出的因子。注意：

## **选择过细等于不选择**

## **设置selectlimit不如设置更多的条件**

下边给出一些实例：

(

not(own)&&

((turnover<0.08&&turnover>0.06)

||(turnover<0.13&&turnover>0.11)

)

&&(in(datacategories, "fundamental")

||in(datacategories, "analyst")

||in(datacategories, "model")

||in(datacategories, "news")

||in(datacategories, "other")

||in(datacategories, "risk")

||in(datacategories, "pv"))

&&(operator_count<=8)

&&(operator_count>=2)

&&(datafield_count<=4)

&&((prod_correlation<0.5&&prod_correlation>0.1)

&&(self_correlation<0.4&&self_correlation>0.05))

&&(decay<=5)

&&(universe=='TOP2500')

&&(truncation<=0.1)

)

(in(classifications, "ATOM")&&((neutralization == 'SLOW') || (neutralization == 'FAST') || (neutralization == 'SLOW_AND_FAST') || (neutralization == 'CROWDING') || (neutralization == 'STATISTICAL') || (neutralization == 'REVERSION_AND_MOMENTUM'))

&&(prod_correlation<0.47&&prod_correlation>0.1)

&&((turnover<0.09&&turnover>0.07)

||(turnover<0.15&&turnover>0.13)

||(turnover<0.20&&turnover>0.18))

&&(operator_count<=10)

&&(operator_count>=3)

&&(dataset_count<=4)

&&(universe!='ILLIQUID_MINVOL1M')

&&(decay==0||decay==1||decay==3||decay==5)

&&(truncation<=0.1)

)

仅供参考，祝各位select愉快：）

**顾问 JX79797 (Rank 9) 的解答与建议**:
写的太好了，昨天用之前的版本做出了三五，值得收藏书签学习

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 8 (原帖: [SuperAlpha]SELECTION框架-v2经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [SuperAlpha]SELECTION框架-v2经验分享_33745533142679.md
- **时间**: 11个月前

**提问/主帖背景 (ZS59763)**:
本文是 [组sa时如何选取高质量因子？ – WorldQuant BRAIN]([L2] 组sa时如何选取高质量因子经验分享_32034293019671.md) 的优化版本，增加了一些额外的筛选项与选择思路，剔除了筛选权重排列，并使用额外的筛选条件进行替代。

以下正文：

## **select流程**

第一步：own or not own，对于expert及以上顾问适用

第二步：选择因子种类，sac2025中提供了很多可以按照因子种类进行筛选的语句，可以直接复制来用。主要包含两类，一类是因子的类别，例如atom，ppac。例：

```
in(classifications, "ATOM")
```

```
in(classifications, "POWER_POOL")
```

第三步：因子的设置。sac中有一周主题叫做风险中性化，需要用使用风险中性化的因子，这个思路感觉很好（因为在ra层面已经中性掉一些风险），也可以根据自己需求进行选择：

```
((neutralization == 'SLOW') || (neutralization == 'FAST') || (neutralization == 'SLOW_AND_FAST') || (neutralization == 'CROWDING') || (neutralization == 'STATISTICAL') || (neutralization == 'REVERSION_AND_MOMENTUM'))
```

使用常规的4个中性化亦可。

第四步：因子的类别。大家在日常跑因子的时候会感觉一些“小众”数据集跑出来的效果一般，这一步可以选取特定的数据类型。思路来源于橘子姐，在此表示感谢。例：

```
&&(in(datacategories, "fundamental")||in(datacategories, "analyst")||in(datacategories, "model")||in(datacategories, "news")||in(datacategories, "other")||in(datacategories, "risk")||in(datacategories, "pv"))
```

至于选择哪些类别，可以按需进行。例如：我想选一些差异较大的类别，那么可以选择fnd和socialmeida，如果我想针对基本面进行选择，则可以囊括fnd，anl，ern。

第五步：分层方式：之前的版本中提出用turnover进行分层，理由是一个因子的turnover不能反映因子的表现，但turnover可以把因子池划分成若干个区间，每次取不同的区间可以避免重复选取。除去turnover之外，也可以按照long count，short count进行分层。count数也不能反映因子表现，但可以分层。例：

```
turnover<0.1&&turnover>0.05
```

```
long_count>1000&&long_count<1200
```

```
a=sqrt(long_count*short_count);a>1000&&a<1200
```

第六步：相关性限制

经与weijie老师讨论，一味地选取低相关性可能不是很好的选择。因为有些好的因子被反复选到后相关性提高，初步的解决方式是利用prodcor和selfcor进行类似powerpool的双重选择。例：

```
((prod_correlation<0.6&&prod_correlation>0.1)&&(self_correlation<0.3&&self_correlation>0.05))  
```

第七步：运算符与字段个数选择。我们早就知道，过多的op和过多的字段不可避免地会带来过拟合，之前的版本中只是选择了op数目进行限制，这是有偏颇的。一阶因子的稳定度不如二阶，有些字段信号强到甚至可以“裸交”，但质量一般。为了剔除掉这些因子，可以采用op数目上下界+字段个数上界的方式进行选择。例：

```
&&(operator_count<=8)&&(operator_count>=2)&&(datafield_count<=3)
```

第八步：decay和truncation选择。这一步的目的是剔除掉一些没有经济学含义，靠着一味调整decay从而实现提交的因子。decay可以选择0,1,3,5,20等有经济学含义的参数。而不是17,29这种没有实质含义的参数。至于truncation，这是为了满足weight分布所做，truncation太高的ppa可能会有weight的warning，从而使得sa的weight不被均匀分布。例：

```
&&(decay<=5)&&(truncation<=0.1)  
```

第九步：universe选择。usa，asi等地区都有illliquid的universe，这些地区的因子大多是靠着低流动性挣钱，会造成maxtrade线和pnl的分歧，在费后表现也没有保障，可以通过universe参数剔除。

```
&&(universe=='TOP2500')
```

第十步：检查选择出的因子。注意：

## **选择过细等于不选择**

## **设置selectlimit不如设置更多的条件**

下边给出一些实例：

(

not(own)&&

((turnover<0.08&&turnover>0.06)

||(turnover<0.13&&turnover>0.11)

)

&&(in(datacategories, "fundamental")

||in(datacategories, "analyst")

||in(datacategories, "model")

||in(datacategories, "news")

||in(datacategories, "other")

||in(datacategories, "risk")

||in(datacategories, "pv"))

&&(operator_count<=8)

&&(operator_count>=2)

&&(datafield_count<=4)

&&((prod_correlation<0.5&&prod_correlation>0.1)

&&(self_correlation<0.4&&self_correlation>0.05))

&&(decay<=5)

&&(universe=='TOP2500')

&&(truncation<=0.1)

)

(in(classifications, "ATOM")&&((neutralization == 'SLOW') || (neutralization == 'FAST') || (neutralization == 'SLOW_AND_FAST') || (neutralization == 'CROWDING') || (neutralization == 'STATISTICAL') || (neutralization == 'REVERSION_AND_MOMENTUM'))

&&(prod_correlation<0.47&&prod_correlation>0.1)

&&((turnover<0.09&&turnover>0.07)

||(turnover<0.15&&turnover>0.13)

||(turnover<0.20&&turnover>0.18))

&&(operator_count<=10)

&&(operator_count>=3)

&&(dataset_count<=4)

&&(universe!='ILLIQUID_MINVOL1M')

&&(decay==0||decay==1||decay==3||decay==5)

&&(truncation<=0.1)

)

仅供参考，祝各位select愉快：）

**顾问 JX79797 (Rank 9) 的解答与建议**:
写的太好了，昨天用之前的版本做出了三五，值得收藏书签学习

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 9 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] [六维小助手]赛季已提交因子字段查询浏览器插件.md
- **时间**: 5个月前

**提问/主帖背景 (JX39934)**:
大家好，我是Midas

我是9月新顾问，2025年Q4也是我顾问生涯中正儿八经的第一个赛季，在这个赛季冲Level的过程中遇到许许多多的问题，其中一个就是这个字段数，我一开始以为不同地区的同字段是算多个fileds的，没想到会去重，也算同个字段，然后呢，自己又得想办法把已提交因子表达式捞出来，然后每次提交因子前还要去查一下这个字段有没有用过，感觉太麻烦了，所以就有了这个插件的诞生，以下是功能展示：

1、可以自己选择哪年的哪个季度，浏览器只要登录了wq平台，点击下载数据，插件就会通过浏览器的cookies去下载此季度已提交因子，并将id，提交date和expression存放在本地


> [!NOTE] [图片 OCR 识别内容]
> 1.下载赛季数据
> 2023
> 下载
> 更新数据



> [!NOTE] [图片 OCR 识别内容]
> 1。下载赛季数据
> 2025
> 下载_
> 更新数据
> 成功下载 167  个因子到 2025-04


2、如果你想提交某个因子，可以先把字段拿来搜索一下，确认没有提交过，再拿去交，减少重复字段数的因子提交


> [!NOTE] [图片 OCR 识别内容]
> 2.匹配本地字段
> Country
> 搜索匹配
> 找到 26  个匹配:
> 2025-12-21720.3746-05-nn IIn
> T戛1
> 2025-12-21
> T7777-
> 77T .
> 1_ !U


甚至你可以用来搜索OP运算符，看看有没有用过（虽然有点多余，华子哥的插件自带运算符分析）


> [!NOTE] [图片 OCR 识别内容]
> 2.匹配本地字段
> ts backfill
> 搜索匹配
> 找到 73 个匹配:


说到这里我留下github地址： [[链接已屏蔽])

使用方法也很简单，谷歌浏览器或者edge浏览器加载插件选中这个dist文件夹就行

希望能帮助到大家，也希望有帮助的话给我点点赞，写写评论

**顾问 JX79797 (Rank 9) 的解答与建议**:
差不多实现


> [!NOTE] [图片 OCR 识别内容]
> Pyramid Distribution (按月份范围)
> 起始:
> 2025
> 10
> 结束:
> 2025
> 12
> 获取数据



> [!NOTE] [图片 OCR 识别内容]
> 1
> subtract
> ern3
> pre_in
> ern3
> alldelav
> Dre
> iterval)
> Simulation Settings
> ern3_pre_interval 字段在本赛季提交状态:
> Instrument Type
> Region
> Universe
> Alpha ID: OOaVEbQI
> Equity
> GLB
> MINVOLIM
> 设置: EQUITY
> EUR
> TOP2500
> D1
> 代码:
> group_neutralize (ts_
> min
> max
> Cps (ts_scale



---

### 技术对话片段 10 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] [六维小助手]赛季已提交因子字段查询浏览器插件_37219186339991.md
- **时间**: 5个月前

**提问/主帖背景 (JX39934)**:
大家好，我是Midas

我是9月新顾问，2025年Q4也是我顾问生涯中正儿八经的第一个赛季，在这个赛季冲Level的过程中遇到许许多多的问题，其中一个就是这个字段数，我一开始以为不同地区的同字段是算多个fileds的，没想到会去重，也算同个字段，然后呢，自己又得想办法把已提交因子表达式捞出来，然后每次提交因子前还要去查一下这个字段有没有用过，感觉太麻烦了，所以就有了这个插件的诞生，以下是功能展示：

1、可以自己选择哪年的哪个季度，浏览器只要登录了wq平台，点击下载数据，插件就会通过浏览器的cookies去下载此季度已提交因子，并将id，提交date和expression存放在本地


> [!NOTE] [图片 OCR 识别内容]
> 1.下载赛季数据
> 2023
> 下载
> 更新数据



> [!NOTE] [图片 OCR 识别内容]
> 1。下载赛季数据
> 2025
> 下载_
> 更新数据
> 成功下载 167  个因子到 2025-04


2、如果你想提交某个因子，可以先把字段拿来搜索一下，确认没有提交过，再拿去交，减少重复字段数的因子提交


> [!NOTE] [图片 OCR 识别内容]
> 2.匹配本地字段
> Country
> 搜索匹配
> 找到 26  个匹配:
> 2025-12-21720.3746-05-nn IIn
> T戛1
> 2025-12-21
> T7777-
> 77T .
> 1_ !U


甚至你可以用来搜索OP运算符，看看有没有用过（虽然有点多余，华子哥的插件自带运算符分析）


> [!NOTE] [图片 OCR 识别内容]
> 2.匹配本地字段
> ts backfill
> 搜索匹配
> 找到 73 个匹配:


说到这里我留下github地址： [[链接已屏蔽])

使用方法也很简单，谷歌浏览器或者edge浏览器加载插件选中这个dist文件夹就行

希望能帮助到大家，也希望有帮助的话给我点点赞，写写评论

**顾问 JX79797 (Rank 9) 的解答与建议**:
差不多实现


> [!NOTE] [图片 OCR 识别内容]
> Pyramid Distribution (按月份范围)
> 起始:
> 2025
> 10
> 结束:
> 2025
> 12
> 获取数据



> [!NOTE] [图片 OCR 识别内容]
> 1
> subtract
> ern3
> pre_in
> ern3
> alldelav
> Dre
> iterval)
> Simulation Settings
> ern3_pre_interval 字段在本赛季提交状态:
> Instrument Type
> Region
> Universe
> Alpha ID: OOaVEbQI
> Equity
> GLB
> MINVOLIM
> 设置: EQUITY
> EUR
> TOP2500
> D1
> 代码:
> group_neutralize (ts_
> min
> max
> Cps (ts_scale



---

### 技术对话片段 11 (原帖: 【Alpha灵感】借助BRAIN Labs 实证Fama-MacBeth回归检验)
- **原帖链接**: [Commented] 【Alpha灵感】借助BRAIN Labs 实证Fama-MacBeth回归检验.md
- **时间**: 9个月前

**提问/主帖背景 (LR93609)**:
**一、概述**

1.  **什么是Fama-MacBeth 两步回归？** 部分借助Kimi大模型（节省查文献的时间）

****一句话理解：**** 先每天与returns进行横截面回归，再对系数做 t 检验——看因子对未来收益的预测能力是否显著。

**类比一句话：** 就像你每天做一次  **“考试”** （与returns进行横截面回归），然后看  **平均分** （mean_beta）和  **标准差** （std_error），最后算  **p 值** （t_value）——判断这个因子是不是  **“真学霸”**  还是  **“蒙的”** 。

**总结一句话：** 回归检验框架 = 用“统计铁锤”砸因子，看它是真金还是泡沫。

**2. 输出指标怎么看？借助Kimi大模型**


> [!NOTE] [图片 OCR 识别内容]
> 捐标
> 含义
> 判断标准
> mean_beta
> 因子每涨1  单位。未来收益平均变化多少
> 绝对值越大越好
> t_Value
> 显著性检验
> 川
> 2.0才算显著
> 95% CI
> beta 的置信区间
> 不包含0才算有效
> mean_rz
> 横截面解释力
> >0.01  就有信息量
> Valid_days
> 有效回归天数
> >250才稳健


**3. 检验可用数据有哪些？个人理解**

- 可以是单因子；

- 也可以是多因子合成的时间序列因子值；

- 理论上只要是固定格式时间序列值，都可以。

简单起见，此处使用USA D1中PV数据集中的pv13_custretsig_retsig（Sign of customer return）举例

**二、实证过程**

**1. 是否能够生成有效因子，使用者多少？来自Data中的数据描述**

**
> [!NOTE] [图片 OCR 识别内容]
> Resion
> Dzay
> Uniwerse
> Data
> Datas2zs > Relationship Data forEqUiTI>
> custretsIgretsig
> U-
> TOF0
> Simulate Field
> Visualize Field
> Field description
> Category: Price VoluME
> Rela-onshp
> Type: Matrix
> SIan
> CUstomerreturn
> Reglon
> Delay
> Unlerse
> Pramld Theme
> LOerage
> Na5
> MUUUOUe
> TIPTI
> 4
> pvTy
> TREI
> Uen
**

**2. 数据分布情况如何？分布是否均匀？借助Brain Labs分析value分布，接近正态分布**


> [!NOTE] [图片 OCR 识别内容]
> TCJn
> TnC
> 071T
> TN/CFIn o
> Flal
> CUTCTCC519
> 「519
> UITCTSR
> 773000'
> O个5
> 7
> 0.0111
> NIT-+FT
> Nisri ;OIITadel
> Tilnt
> Distnuon of pv13 custretslq
> 「a/SI alles
> SNIIIIT
> UIIIO
> 
> 300000
> TOI
> JOUOUU
> 191



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> CO Cl
> custrets 诅B_rets JB;
> 昵 SeIe Data Ses Moh3
> eate Data
> ShE P=
> TMPTC
> TT S
> [SHo
> 0.,87
> 15.9290
> -0.,52
> 5,6700
> 5S,5
> 859
> 39300
> 5411UUJLUOI
> SeltII =
> Itnw-lu TI 
> Reglom
>  UNer
> URU
> Day
> Uo
> Trneatn
> Nubollolon
>  Pasteurtaton
> NoN Hancng
> Unt Hanong
> Ue Trede
> SN
> Tumo
> Reurs
> Io
> Uong Cun
> Shot Cont
> U5
> TO?C
> SFres:
> 0.23
> Subindustr;
> 2013
> .+
> 151
> 1
> .1*
> 243
> 0+53
> 15
> 71_
> J.s
> 15::
> .45
> ?:
> 51
> 115
> 2=
> _
> :
> J?
> 43::
> 12
> Clone Alpha
> ZE
> 1.34
> 1 _
> 04
> 1''
> 13_7 
> 17
> 172
> 3017
> E
> ECs
> 55
> TT
> 11
> Chart
> Pnl
> 71
> 0.10
> 1C;
> D
> CI
> 35.
> 7.512.
> 仨?
> 1
> -715
> 1.55
> 87
> El
> 5-
> 113
> 1-
> 17
> 220
> 53
> 4
> 322:
> 一
> 1
> OOJK
> .2
> 177::
> 72:
> :
> #:
> 1SJe
> 222
> 52
> 3
> 0.23
> 5
> 5-
>  :
> 1
> 0721202D
> OOJK
> RIL NeIrra
> 8778
> 72
> 3*
> u;
> -3871SE:
> ~OOJ
> Risk neutralized
> ln
> 1 C
> Jn9
> Jr'-
> J '21
> In 22
> 1n-
> Assregale Data
> 5131
> [12!
> 011@
> UTIN
> 0.31
> 15.92%
> 0.28
> 1.959
> 21.02%
> 2.479630
> P1
>  N
> Ma
> SU5


**3. 分组是否清晰、均匀？分组中性化结果是否有畸变？**

**- 分组：清晰、均匀**


> [!NOTE] [图片 OCR 识别内容]
> UIETOe
> Dvl} custretsIg
> retslg
> SUILITOISLR;
> CUCLUL
> CJeL+
> CVCLL
> CeLLN
> CVCC-L_
> CNeCU
> CCCU 
> CVCC-LU
> CVCYU1
> UJllt
> 71031(
> V=tenals AT
> CTTMMTI=TITTC
> ~911431e
> 71031/
> 23[NCCS
> NIaCITanGznere
> TTAJC
> LTCOIUIC
> 13-1
> Retal-KEJn
> UEpt Store
> UVeTtSITO AOENCIEs
> Computsr Nded Uesiqn
> nanoal GIaantee I
> MaCITRMaLenE
> LanJl
> CTTbII CSINITCI|
> TtallLESTaUTTt
> auyertising
> Cl
> CmII=
> SCITIt
> [33Tc
> mmInitTr
> NIacISNIILTd
> LTT
> CUTTPITTUIT
> Retal-sportng
> 69
> UVeTtSITIC
> SEMCZS
> CUIUULZ
> STIZE
> 7sh2112
> NchlnaRHUIDs
> LTate
> TIUIt'
> HetallIJ
> StOTE
> 三TI-031
> UETans =
> CTmII=
> 5nfta
> NlacInThemI PTC -ess
> PTfelTna
> STIITT
> RfalTSh Sr(rtr
> UTOSDAC
> UETZns =
> ZCUIDIent
> CDILULTS
> OUJCaNIEC
> Nann
> SEMICS
> LCDTt
> CasValt Ins
> HetallMtIIns
> VUT SUp
> ayricultural BIotecn
> CTmIMtrcnanrtedShams
> cd-catering
> NCr =
> ITTSUITMS52/7
> CIHECTIn Sfah
> U-hTrTCT
> aget Cars
> LCTICUITUTa
> CTeMICAIs
> CUILULTSMeMOIY UeICZ
> OUJ CONecIOnET;
> NEOICa
> at107 S/5
> Fblic Thorcughtares
> HUbUE
> HaSHIC TOUUCs
> LTTICUITUITaI
> Ope
> 73NT/5
> CTIIMtrs MthE
> 1 LnITTICC
> NCr =
> ITIN2
> MIAIITITT-10
> ThHFCIT
> UIF MIUIDn CorTS
> EOUITIIZT
> CTTTULZTs HnnTZra
> COUIONER
> UalT
> NECICa
> Labs
> ZSHIT ?
> LUOIITITO-Mewspaqars
> IrIts Centr
> LTIIT Sc
> CTTTMtc
> TE-nTnrtI
> TNI-EA Lr TTIT
> Neris
> Lstars
> MIhIITITT-CImprals
> TTIS Tatem U
> Mrmort Uevelcn
> Ialtnance
> CTTSUITIT Serilcas
> LOOO-TIsC
> UTerItlen
> NECICa
> HTOTUCT
> SaTyIh
> ITTIs SOUHEITU
> Uem
> CTSTI
> CTNCIm
> PCTIs-LIC 
> NJ-sl
> NCr =
> TTST =
> GGene
> AFILAnTmert
> TTISMm (
> UEMaIIVE
> Wasie IECT
> CTntaInErs VEa
> G1a55
> LOOO-VHUeSaI
> Uistnt
> NCCalUNUI
> REITS Drersihed
> Satallne
> ZCCII
> appare
> MaTIFTIIT
> CtanFr Man-r
> Plastic
> TN'ea
> Jelatet 'rparel
> NerliralGarFTIC Mmn
> AIT-Haalh CaT
> Thools
> RIInce
> TTSMT-NCc
> TIFTTIa=
> SVT =
> HLC[个s
> Sa ng
> LTTOTI


**- 模拟：均匀、无畸变**


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Cregted 09.082025 EDT
> JnonymOs
> * pha
> 3Lst
> Code
> IS Summary
> Prodl
> custretsig_rets 琚;
> 眺 See Dats Ser Mloh3
> Broup_Fank(u, subindustry);
> Hat
> Dar
> TITTI
> TITE
> CT
> Warar
> 12.2690
> 1,25
> ,95%6
> 4489
> 12.969000
> SIIIIITIOI
> Setrlnzs
> Srpo
> Tunou
> T
> Reume
> OIoo
> Mrgln
> Uong Cnt
> Sht Cwnt
> UtwtclTD
> Rdl
> Uoherse
> Lenguay
> 0cay
> Oay
> Twncaton
> Nuualhabon
> Pasturtad
> NaNHalo
> UtHnUlno
> Ua Trede
> 2013
> 3.53
> .31.
> 1.9.
> 3 .
> 53:
> 15-
> U 
> TC?3O]
> 王 =C
> 0.03
> SJU
> 201-
> 7
>  
> 0.73
> 一?:
> 3.2:
> C:
> 1_-
> 2=
> 29
> :
> 2-5
> 12 :
> 污:
> 1 :
> 14
> Clone Alpha
> ZE
> 3
> 11.318
> 274
> 5
> 3:
> 1汜
> 143
> 3017
> 15#
> 05
> 1
> 51
> 116
> 71
> 15
> 002
> C4
> 41
> TST
> 1713
> 1-7
> Chart
> -715
> 1.75
> 2.35*
> 2.
> 15C
> 1T2
> 1-33
> 220
> 4:
> 11 :
> 3-7
> 1
> 11 _
> 537
> 二 :
> :
> 37.5:
> 17=
> 15
> 25'0712021
> TJDK
> Pn
> 37.-5k
> 222
> _:
> 8
> 汀
> 2:
> 1_73
> Rlk NeuralkedPnL-.
> 72
> U
> 03*
> :
> 1
> 20
> Risk neutralized
> Assresale Data
> |
> UTI@
> 0
> Ia11
> Jn 4
> Jon15
> 4Jn'16
> J `18
> Jung
> J3
> Jn 73
> 1.10
> 12.26%
> 0.58
> 3.51%
> 3.78%
> 390
> Rsk NEUTaIZEDPnl
> Pv
> _


4.  **Fama-MacBeth 回归检验结果如何？**

**- 代码：来自Brain Labs案例**


> [!NOTE] [图片 OCR 识别内容]
> 127T1
> TTnnr
> Tnyrl
> IINOTT
> 1 :n6rReorrssion
> TnTt
> SCTT';
> 517+-
> 5TT
> T Tegressionuf
> GaS:1 :
> Lhaci
> SIgnals With Fana
> I UetnNegresSrUI
> retyrns
> TUtrat170 UT
> df.sU(Jf.neanlaxis=
> 3115二 |
> Jetaye0
> 0+Tl
> 21116221
> NIMTCaITa
> 3h(
> SIL15=11
> ShTt'
> Olu5
> IqUJreo
> 「turns
> 6rnin
> 16rin
> Filgl"return '
> ITarr
> T-7-F
> inle
> RarrT
> STatisTIC2 simni-icae
> [131
> 01-+3
> LlVas
> 「-hnc1
> TCUFNS
> Ltves
> VEnenUent
> Whl
> VJLLU Isk
> LSMIN I
> 1LutLC' !
> 1SJMLY1
> T]
> YL]'6
> 711
> VLI11457k
> C-055-SC-tionl
> TTTC5TOI
> 1ET1
> 11+1
> [02l
> LIn=aTRTTEsSIOTI|
> [Tel
> 717
> U1
> NlU |
> Ltus_tLst
> OLL JIOLl
> SVare
> T
> predic: (x_validl
> CTTCIC
> C
> SCCCon
> TRnRT
> TnT3 |
> SIIy
> Tpeanly
> 6111902 1
> o111
> SITI
> 471+
> SOUaTE0
> 「1043
> TotalI
> total
> else np.nan
> SNI
> JTEN IT
> SIUaTECI
> elye
> [499
> JHL OOLT .Ih
> SNUHTCI
> UTTCTTTC
> NSa个
> TSTIEFT
> [+
> 1is1
> S141T
> i
> Std_rror
> M.Nasdlberas_lIst)
> {
> l
> TT{
> 1)
> U
> T+T
> 'tve
> ?Fro「
> 5tT
> CONTIOENC? Irtenal
> Cy
> TOTP
> UUII0T
> 953021
> 3TTUT
> SOFTIA/I
> JL[
> UULIIO
> ULJI CCl
> .90
> ISCU Crror
> SOTINI
> VU-Ia
> 1
> Ah
> TNITTTO
> Lrd listi
> prinz |
> H HEITeSSITI
> SUIT3T
> 5 |
> |CUS107
> 31
> LaT'
> SCCNI
> 9371
> 5LUCTror:
> LSLTTOUnUlsed CrTr
> mm
> IT+
> 1s?TTTOUNJIUCNC [
> JOI
> |
> [str(roud (upper_bound。 2)11 ]
> Th
> TUTTd
> 5TTTTomdlnn
> SAUTCI
> 711
> U1 
> 015 ;
> 4541559
> 0;|
> 71+
> OFOI ^


**- 计算结果**


> [!NOTE] [图片 OCR 识别内容]
> U
> Bralnlregions UsA 
> PLJ-
> UVerse=' TopJe30]
> daulleld_dl
> UToLIsy UJ
> 1JnICTJ-I
> Uulu
> 1UUJIU
> CUStieLg_Tets-y
> TCgTc55?oplo7tt1ocd 01
> KCICUl
> UII
> ]+ *
> 'TI
> PTFII '
> 95 ConTicens
> Tneryal :
> 177
> SOULCeC
> Vuld_duy: 251
> 「S


**- 结论分析（借助Kimi大模型）**

**
> [!NOTE] [图片 OCR 识别内容]
> 指标
> 数值
> 含义
> mean_beta
> -1.85
> 每增加1个标准差
> 未来收益平均下跌1.85%
> t_Value
> -9.99
> 极度显著 (p ~ 0)
> 95% CI
> [-2.21,-1.48]
> 不包含 0,方向稳定
> Valid_days
> 2517
> 10 年+的样本,极度稳健
> mean
> squared
> 0.0
> 横截面 解释力极低
> 但这不是问题
> (FM 回归 Rz 通常都很低)
**

**- 结论：这是一个极度显著、方向稳定、样本充足的反向因子**

**三、 验证二步回归结果**

**1. 用rank≥0.7和sign≥0.4实证二步回归检验**

**- rank验证：sharpe标准0.87×0.7=0.61＜0.67，合格**


> [!NOTE] [图片 OCR 识别内容]
> U
> Created 09/082025 EDT
> anonymOUs
> Add Nphato
> Ust
> Code
> IS Summary
> Perod
> 0VI3_custretsig retslg;
> 吣 Snele Data Setsloha
> rank (a)
> ASBregate Data
> SharDs
> TUrno=
> Flnes:
> C
> Orawgowr
> Wrain
> 0.67
> 15.5096
> 0.34
> 3.9996
> 12.59%
> 5.1596o0
> Simulation Settines
> IstrUMI Typa
> Reolon
> Uherse
> LnOage
> Co
> Oy
> Truneton
> Neutllnwon
> Pastewrtato
> NaNHang
> Unlt HanO
> Nax Tmd
> Shalp
> Tutwer
> Fgs
> Returns
> Dewdown
> Uagln
> Log Cont
> Shot Count
> Sauny
> C-
> TO-J
> Fast S Cressn
> T
> 0.03
> SubnJ-sr
> =r
> 7013
> 0,7
> 1537:
> 03
> 77
> C3-
> 33:
> 15
> 1
> -1
> 7
> 1_7-:
> CEJ
> 459沁
>  .
> 5--
> 1533
> 15-
> 301=
> 0.3
> 15
> 0?
> 303
> 251汨
> '130
> 157
> 153
> Clone Alpha
> -015
> 0.34
> 1-37-
> 037
> 二75:
> ~55.
> 33-
> 三
> 127
> 2017
> 111
> 12
> 5855
> 2376
> 3319
> 521
> 1527
> Chart
> nl
> 2013
>  E
> 1_5:
> 0=
> Cs:
> 225
> 77:
> =
> 1525
> 2019
> .34
> 151
> 0.10
> 1.21沿
> 85汩
> 52
> 115
> 152
> 01
> 153:
> 140
> 3
> 1E
> 5;
> T=
> 1513
> 一-
> 5
> 17.3
> 0-J
> 1.07
> 9.33
> 3
> 154
> 1SE_
> 0JJ
> 11/232018
> 3022
> 0.1E
> 1535
> 005
> 4沿
> C12
> 157:
> 11
> 1573
> Du
> 333.17
> Risk Neutralized Pnl
> 582.36<
> -
> 15_
> 131
> 11.75.
> T1
> -:
> 1-3
> 1537
> Risk neutralized
> Jn '14
> JaT 15
> 0715
> Ja
> 13713
> 119
> J2
> 157.71
> J7 -
> J2
> Aeereeate Data
> Sharce
> IUTTO
> Finess
> FetUCN
> 903OU
> Warein
> 0.71
> 15.509
> 0.23
> 1.5996
> 6.5490
> 2.0596oo
> Pn
> Risk Neutralzeo Pnl


**- sign验证：sharpe标准0.87×0.4=0.35＜0.54，合格**

**
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09;08/2025 EDT
> anonymous
> uodphato
> Ust
> Code
> IS Summary
> Perod
> Custretsig retsig;
> 0 Snele Data Set slpha
> sign (a)
> Aeeregate Data
> Sharp=
> UTMC Ir
> Fisness
> T=upns
> OTaUT
> Nsrain
> 0.52
> 12.1296
> 0.24
> 2.4596
> 12.78%
> 4.049600
> Simulation Settines
> IstrumltType
> Reolo
> Uhers
> Lnoage
> Cy
> Oely
> TNNCton
> Newtllawon
> Rastertzatm
> NaN Handlg
> Unlt Handwng
> Ia Tmd
> Sherpe
> 
> Fes
> Rts
> Dowdowm
> Noym
> Lo Co
> Shot Count
> Sury
> U-
> TO-J
> Fast SpressIen
> TZE
> 0.03
> Subindusoy
> Ur
> T0
> Cs
> 14
> Ds
> 3
> 222:
> 302:
> 151
> 131
> 2011
> 11.459
> 0.82
> 4419
> 4.15
> 7.7C.
> 53
> 15_
> 2015
> 025
> 113
> DDE
> 7.
> 3
> 2
> 5
> 1565
> Alpha
> ZOIE
> 031
> |_
> 0.03
> 0.35:
> 1
> SL:
> 110
> 1SES
> 2017
> TCE
> 11635
> 0.3
> 41
> 3
> J5
> 435
> 1545
> N Chart
> Pnl
> TO
> 0E3
> 41 =
> 0
> 1.359:
> 3:
> 37:
> =13
> 1=3
> 201
> +0.20
> 121
> 4
> 5
> 243
> 0.9
> 4
> 1545
> 3030
> 731
> =
> 73
> 17-
> 11
> 72:
> 13
> 19
> -1
> DS
> 1.759
> 031
> 4+9
> 1559
> 551.
> 45
> 15-3
> 7OD
> 702
> 011
> 1705
> D0
> 32.
> E S2.
> 5.711:
> 1513
> 1E01
> DJO
> 一
> .-5
> 125
> |
> 7.519
> 0.5:
> S:
> 110
> 1-
> Risk neutralized
> Jny
> Ja 15
> 17 16
> Ja
> Jan8
> Jan9
> Jan '20
> 1371
> J7 -
> Jn
> AEEregate Data
> SNarce
> Turnove
> Fihe_=
> Reury_
> DrawJowi
> Warsin
> 0.51
> 12.12%
> 0.15
> 1.06%
> 4.84%
> 1.759600
> Pn_
> Risk NeJralzzo Pn_
> 0v13
> Clone
**

**2. 分组、验证、增强并提交：** 用ts_rank进行增强并提交

**- 分组：sharpe=1.57**


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Cregted 09.082025 EDT
> JnonymOs
> * pha
> 3Lst
> Code
> IS Summary
> Prodl
> custretsig_rets 琚;
> 眺 See Dats Ser Mloh3
> Broup_Fank(u, subindustry);
> Hat
> Dar
> TITTI
> TITE
> CT
> Warar
> 12.2690
> 1,25
> ,95%6
> 4489
> 12.969000
> SIIIIITIOI
> Setrlnzs
> Srpo
> Tunou
> T
> Reume
> OIoo
> Mrgln
> Uong Cnt
> Sht Cwnt
> UtwtclTD
> Rdl
> Uoherse
> Lenguay
> 0cay
> Oay
> Twncaton
> Nuualhabon
> Pasturtad
> NaNHalo
> UtHnUlno
> Ua Trede
> 2013
> 3.53
> .31.
> 1.9.
> 3 .
> 53:
> 15-
> U 
> TC?3O]
> 王 =C
> 0.03
> SJU
> 201-
> 7
>  
> 0.73
> 一?:
> 3.2:
> C:
> 1_-
> 2=
> 29
> :
> 2-5
> 12 :
> 污:
> 1 :
> 14
> Clone Alpha
> ZE
> 3
> 11.318
> 274
> 5
> 3:
> 1汜
> 143
> 3017
> 15#
> 05
> 1
> 51
> 116
> 71
> 15
> 002
> C4
> 41
> TST
> 1713
> 1-7
> Chart
> -715
> 1.75
> 2.35*
> 2.
> 15C
> 1T2
> 1-33
> 220
> 4:
> 11 :
> 3-7
> 1
> 11 _
> 537
> 二 :
> :
> 37.5:
> 17=
> 15
> 25'0712021
> TJDK
> Pn
> 37.-5k
> 222
> _:
> 8
> 汀
> 2:
> 1_73
> Rlk NeuralkedPnL-.
> 72
> U
> 03*
> :
> 1
> 20
> Risk neutralized
> Assresale Data
> |
> UTI@
> 0
> Ia11
> Jn 4
> Jon15
> 4Jn'16
> J `18
> Jung
> J3
> Jn 73
> 1.10
> 12.26%
> 0.58
> 3.51%
> 3.78%
> 390
> Rsk NEUTaIZEDPnl
> Pv
> _


**- rank验证：sharpe标准=1.57×0.7=1.1＜1.57，合格**


> [!NOTE] [图片 OCR 识别内容]
> UNS
> Creglsd 09082025 EDT
> anonymOus
> NJDataJS
> Code
> IS Summary
> PuTrod
> pVI3_custretsJB_Fets g;
> [ See Dats Ser Moha
> PTUIV
> Tank(a, subindustry);
> eank {)
> AEBreeate
> 0C3
> TUTTO
> TICN
> TTJTI
> LTyC
> 1.57
> 12.2690
> 1,25
> 7.9790
> 4.509
> 3,019000
> SIIUIaton Settllzs
> WotwelTYD
> Reglon
>  UoNerse
> UB
> Way
> Tmncaton
> Nuballallon
> [-T
> NaNHandlg
> UntHanolng
> Ua Trede
> Ver
> Cro
> Tmg
> Ft
> Reum
> [r
> Wrgln
> Long Cont
> Shot Cont
> TS?
> Fast XPres:?
> 7.13
> Subindustr
> Vn
> 21
> 3.D
> .5.
> C
> 1.5
> 3.5.
> 275:
> 15
> 201-
> 1
> 一_ :
> 一?
> 3
> =:
> 1__
> 3
> ;
> 10.2 :
> 污:
> 5:
> Clone Alpha
> ZE
> 38
> 277*
> 3
> 1u
> 3017
> 0.31
> 0
> AE
> 45
> 二!
> 113
> 2018
> 52.
> C
> [J
> 4.17
> TSE
> 1715
> 147
> N Chart
> 2115
> |
> 20
> 1-SC
> 20120
> 2
> 1015
> 3.
> 1 -
> 1-11
> 2.55
> C_:
> Js :
> :
> _:
> 1
> -3
> 222
> 222
> 210:
> 3污-
> =:
> 17
> 1212'2213
> 51
> 2
> 3
> SDK
> 2315r
> RLsk Neutrallzed PnL 1ASE 6S
> Risk neutralized
> DUu
> Orauro
> Jr'20
> In 
> Jn 77
> 1.09
> 12.269
> 0.58
> 3.529
> 3.84%
> 5.74960
> ZSKNEE
> ZEU Pnl
> 0a
> 三」
> ?5
> Fesi
> SLut


**- sign验证：sharpe标准1.57×0.4=0.63＜1.42，合格**


> [!NOTE] [图片 OCR 识别内容]
> UNS
> Creglsd 09082025 EDT
> anonymOus
> NJDataJS
> Code
> IS Summary
> PuTrod
> DVIL
> custretsiB_rets 氓;
> 昵 Sele Dats Ser Nlph3
> PTUIV
> Tank(a, subindustry);
> SLBn ()
> AEBreeate Data
> 3C=
> LUIFnC
> TTS
> TZUTT
> a
> 42
> 5,7
> 1,14
> 8,009
> 5,5791
> 28,029000
> SIIUIaUOn SetUnas
> WotwelTYD
> Reglom
>  UoNerse
> UB
> Tmncaton
> Nuballallon
> [-T
> NaNHandlg
> UntHanolng
> 2
> Ver
> Chc
> Tuler
> 「t
> Rhr
> 0r
> Marglm
> Cnt
> Shot Cont
> TS?
> Fast XPres:?
> 7.13
> Sidustr
> 711
> 3
> 3
> 537.
> 4.529
> |.
> 一_
> S.E
> E:
> 3.1:
> 3+:
> 1E
> 3
> -5:
> 12-3:
> :
> Clone Alpha
> ZIE
> 143:
> 4.21.
> 3017
> 055
> Cr
> 5
> 31
>  T.
> 2018
> 055
> 1.57 .
> 4,139.
> 5ZS
> 153
> 113
> N Chart
> 2115
> 7-
> 5.03
> 3 .
> .239
> 3.
> 15
> 220
> ~5
> 5715
> 03
> 一-
> :
> 53
> 2:
> 一:
> :
> 2017
> 137
> DDK
> C1272
> 222
> -5
> 312:
> 污:
> 1218
> 355.52k
> Risk Nautralzed PnL:
> 3153
> 22
> :
> 0.738
> 15;
> 1
> 2S3cK
> Risk neutralized
> Aesregate
> DUu
> TurnO
> Rlurr
> SISJ
> Warel
> Jun 14
> en '1
> In 
> Jn 77
> 0.91
> 5.70%
> 0.46
> 3.23%
> 4.8795
> 11.3496
> Pnl
> Risk NEUTaIZED Pnl
> Uen
> 0a
> Ct
> 20
> 5:
> DT
> 2;
> gL


**- ts_rank增强并提交**

**
> [!NOTE] [图片 OCR 识别内容]
> ACV
> Cralsd OSOS 2025 EDT
> anonymoUs
> AU Aphgt 3 UIst
> Code
> IS Summary
> Period
> a 「CVerse(ts
> Fank (EFCUP
> TMI
> CustretsJB_retsJ'
> subindustry)
> 752));
> ICme
> VarasetUtilaton Iheme
> 昵 Sirale Daza Ser Alpha
> Power Pol Alpha
> Pramio there: USNDIIPV &1
> NEBreEate
> 0ara
> TITTI
> CIT
> Crano
> 13.8590
> 1.25
> 7,789
> 6.349
> 11.,249000
> SIIUIatIor
> Settinss
> ImuTR 
> Reglon
>  Uner
> URU
> De
> Tmncgtn
> N-uuallaton
> Pasturbouo
> NoN Helclg
> Unt Hanoung
> Ue Trede
> S[ 
> Tum
> T
> UI
> Io
> OM
> on Cun
> Sht Cont
> TC-
> Fsst SFrsss ?
> 1.23
> Sbindustr
> 2513
> 17
> 12-3
> 1_ .
> 53:
> 1s+E
>  _
> _
> E.S
> 207:
> 3:
> 1ss
> 2015
> 1_-
> 一1::;
> 17-
> 洪:
> 125
> Clone Alpha
> ZTE
> 14
> 1
> 70_
> 377-
> -
> 1_汇
> 3017
> 1-
> 5
> 15
> E
> 1
> N Chart
> 211
> 1
> 5.25玷
> 1
> 3.25
> 715
> 1235
> E.23沿
> -3.
> 10.51:
> 1
> 一
> 5:
> 一5
> E
> 5:
> 1-3
> :
> 23.75沿
> 43:
> 3:
> U
> 13
> SDDK
> 2122
> _
> 473-
> C:
> 1
> 1_5
> OIJE -13
> 
> E
> J
> ~抵;
> 118
> 15Pnl  3353.E2
>  =JO
> Risk neutralized
> HSICSJL
> 1
> T
> U
> Marein
> 24
> 13.859
> 0.59
> 3.0995
> 4.31%
> 4.46950
> 1
> 1n
> 3__
> In _
> Pv13
> Ce
> 』
> TL
> ShaTF
**

**3. 总结：** 金融与资产定价研究中，Fama-MacBeth 回归（1973）至今仍是国际学术界最主流、最通用、最被认可的因子显著性检验框架之一 ——  **解释来自借助Kimi大模型**

- 能够通过二步回归检验，说明因子的预测性是显著的，能够在很大程度上确保OS的稳定。

- 建议在后续因子分析中，有条件的情况下，应首先进行二步回归，避免走弯路，提高分析效率。

- 在一定程度上说明，rank≥0.7和sign≥0.4的验证是有效的（相对宽松），在simulator中可以使用。

**顾问 JX79797 (Rank 9) 的解答与建议**:
[LR93609](/hc/en-us/profiles/30244554462231-LR93609)     冷兄的一系列 灵感贴 看了很有启发， 目前集中在框架、mcp，下季度一定好好研究研究！！！

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 12 (原帖: 【Alpha灵感】借助BRAIN Labs 实证Fama-MacBeth回归检验)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】借助BRAIN Labs 实证Fama-MacBeth回归检验_34778720525335.md
- **时间**: 9个月前

**提问/主帖背景 (LR93609)**:
**一、概述**

1.  **什么是Fama-MacBeth 两步回归？** 部分借助Kimi大模型（节省查文献的时间）

****一句话理解：**** 先每天与returns进行横截面回归，再对系数做 t 检验——看因子对未来收益的预测能力是否显著。

**类比一句话：** 就像你每天做一次  **“考试”** （与returns进行横截面回归），然后看  **平均分** （mean_beta）和  **标准差** （std_error），最后算  **p 值** （t_value）——判断这个因子是不是  **“真学霸”**  还是  **“蒙的”** 。

**总结一句话：** 回归检验框架 = 用“统计铁锤”砸因子，看它是真金还是泡沫。

**2. 输出指标怎么看？借助Kimi大模型**


> [!NOTE] [图片 OCR 识别内容]
> 捐标
> 含义
> 判断标准
> mean_beta
> 因子每涨1  单位。未来收益平均变化多少
> 绝对值越大越好
> t_Value
> 显著性检验
> 川
> 2.0才算显著
> 95% CI
> beta 的置信区间
> 不包含0才算有效
> mean_rz
> 横截面解释力
> >0.01  就有信息量
> Valid_days
> 有效回归天数
> >250才稳健


**3. 检验可用数据有哪些？个人理解**

- 可以是单因子；

- 也可以是多因子合成的时间序列因子值；

- 理论上只要是固定格式时间序列值，都可以。

简单起见，此处使用USA D1中PV数据集中的pv13_custretsig_retsig（Sign of customer return）举例

**二、实证过程**

**1. 是否能够生成有效因子，使用者多少？来自Data中的数据描述**

**
> [!NOTE] [图片 OCR 识别内容]
> Resion
> Dzay
> Uniwerse
> Data
> Datas2zs > Relationship Data forEqUiTI>
> custretsIgretsig
> U-
> TOF0
> Simulate Field
> Visualize Field
> Field description
> Category: Price VoluME
> Rela-onshp
> Type: Matrix
> SIan
> CUstomerreturn
> Reglon
> Delay
> Unlerse
> Pramld Theme
> LOerage
> Na5
> MUUUOUe
> TIPTI
> 4
> pvTy
> TREI
> Uen
**

**2. 数据分布情况如何？分布是否均匀？借助Brain Labs分析value分布，接近正态分布**


> [!NOTE] [图片 OCR 识别内容]
> TCJn
> TnC
> 071T
> TN/CFIn o
> Flal
> CUTCTCC519
> 「519
> UITCTSR
> 773000'
> O个5
> 7
> 0.0111
> NIT-+FT
> Nisri ;OIITadel
> Tilnt
> Distnuon of pv13 custretslq
> 「a/SI alles
> SNIIIIT
> UIIIO
> 
> 300000
> TOI
> JOUOUU
> 191



> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> CO Cl
> custrets 诅B_rets JB;
> 昵 SeIe Data Ses Moh3
> eate Data
> ShE P=
> TMPTC
> TT S
> [SHo
> 0.,87
> 15.9290
> -0.,52
> 5,6700
> 5S,5
> 859
> 39300
> 5411UUJLUOI
> SeltII =
> Itnw-lu TI 
> Reglom
>  UNer
> URU
> Day
> Uo
> Trneatn
> Nubollolon
>  Pasteurtaton
> NoN Hancng
> Unt Hanong
> Ue Trede
> SN
> Tumo
> Reurs
> Io
> Uong Cun
> Shot Cont
> U5
> TO?C
> SFres:
> 0.23
> Subindustr;
> 2013
> .+
> 151
> 1
> .1*
> 243
> 0+53
> 15
> 71_
> J.s
> 15::
> .45
> ?:
> 51
> 115
> 2=
> _
> :
> J?
> 43::
> 12
> Clone Alpha
> ZE
> 1.34
> 1 _
> 04
> 1''
> 13_7 
> 17
> 172
> 3017
> E
> ECs
> 55
> TT
> 11
> Chart
> Pnl
> 71
> 0.10
> 1C;
> D
> CI
> 35.
> 7.512.
> 仨?
> 1
> -715
> 1.55
> 87
> El
> 5-
> 113
> 1-
> 17
> 220
> 53
> 4
> 322:
> 一
> 1
> OOJK
> .2
> 177::
> 72:
> :
> #:
> 1SJe
> 222
> 52
> 3
> 0.23
> 5
> 5-
>  :
> 1
> 0721202D
> OOJK
> RIL NeIrra
> 8778
> 72
> 3*
> u;
> -3871SE:
> ~OOJ
> Risk neutralized
> ln
> 1 C
> Jn9
> Jr'-
> J '21
> In 22
> 1n-
> Assregale Data
> 5131
> [12!
> 011@
> UTIN
> 0.31
> 15.92%
> 0.28
> 1.959
> 21.02%
> 2.479630
> P1
>  N
> Ma
> SU5


**3. 分组是否清晰、均匀？分组中性化结果是否有畸变？**

**- 分组：清晰、均匀**


> [!NOTE] [图片 OCR 识别内容]
> UIETOe
> Dvl} custretsIg
> retslg
> SUILITOISLR;
> CUCLUL
> CJeL+
> CVCLL
> CeLLN
> CVCC-L_
> CNeCU
> CCCU 
> CVCC-LU
> CVCYU1
> UJllt
> 71031(
> V=tenals AT
> CTTMMTI=TITTC
> ~911431e
> 71031/
> 23[NCCS
> NIaCITanGznere
> TTAJC
> LTCOIUIC
> 13-1
> Retal-KEJn
> UEpt Store
> UVeTtSITO AOENCIEs
> Computsr Nded Uesiqn
> nanoal GIaantee I
> MaCITRMaLenE
> LanJl
> CTTbII CSINITCI|
> TtallLESTaUTTt
> auyertising
> Cl
> CmII=
> SCITIt
> [33Tc
> mmInitTr
> NIacISNIILTd
> LTT
> CUTTPITTUIT
> Retal-sportng
> 69
> UVeTtSITIC
> SEMCZS
> CUIUULZ
> STIZE
> 7sh2112
> NchlnaRHUIDs
> LTate
> TIUIt'
> HetallIJ
> StOTE
> 三TI-031
> UETans =
> CTmII=
> 5nfta
> NlacInThemI PTC -ess
> PTfelTna
> STIITT
> RfalTSh Sr(rtr
> UTOSDAC
> UETZns =
> ZCUIDIent
> CDILULTS
> OUJCaNIEC
> Nann
> SEMICS
> LCDTt
> CasValt Ins
> HetallMtIIns
> VUT SUp
> ayricultural BIotecn
> CTmIMtrcnanrtedShams
> cd-catering
> NCr =
> ITTSUITMS52/7
> CIHECTIn Sfah
> U-hTrTCT
> aget Cars
> LCTICUITUTa
> CTeMICAIs
> CUILULTSMeMOIY UeICZ
> OUJ CONecIOnET;
> NEOICa
> at107 S/5
> Fblic Thorcughtares
> HUbUE
> HaSHIC TOUUCs
> LTTICUITUITaI
> Ope
> 73NT/5
> CTIIMtrs MthE
> 1 LnITTICC
> NCr =
> ITIN2
> MIAIITITT-10
> ThHFCIT
> UIF MIUIDn CorTS
> EOUITIIZT
> CTTTULZTs HnnTZra
> COUIONER
> UalT
> NECICa
> Labs
> ZSHIT ?
> LUOIITITO-Mewspaqars
> IrIts Centr
> LTIIT Sc
> CTTTMtc
> TE-nTnrtI
> TNI-EA Lr TTIT
> Neris
> Lstars
> MIhIITITT-CImprals
> TTIS Tatem U
> Mrmort Uevelcn
> Ialtnance
> CTTSUITIT Serilcas
> LOOO-TIsC
> UTerItlen
> NECICa
> HTOTUCT
> SaTyIh
> ITTIs SOUHEITU
> Uem
> CTSTI
> CTNCIm
> PCTIs-LIC 
> NJ-sl
> NCr =
> TTST =
> GGene
> AFILAnTmert
> TTISMm (
> UEMaIIVE
> Wasie IECT
> CTntaInErs VEa
> G1a55
> LOOO-VHUeSaI
> Uistnt
> NCCalUNUI
> REITS Drersihed
> Satallne
> ZCCII
> appare
> MaTIFTIIT
> CtanFr Man-r
> Plastic
> TN'ea
> Jelatet 'rparel
> NerliralGarFTIC Mmn
> AIT-Haalh CaT
> Thools
> RIInce
> TTSMT-NCc
> TIFTTIa=
> SVT =
> HLC[个s
> Sa ng
> LTTOTI


**- 模拟：均匀、无畸变**


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Cregted 09.082025 EDT
> JnonymOs
> * pha
> 3Lst
> Code
> IS Summary
> Prodl
> custretsig_rets 琚;
> 眺 See Dats Ser Mloh3
> Broup_Fank(u, subindustry);
> Hat
> Dar
> TITTI
> TITE
> CT
> Warar
> 12.2690
> 1,25
> ,95%6
> 4489
> 12.969000
> SIIIIITIOI
> Setrlnzs
> Srpo
> Tunou
> T
> Reume
> OIoo
> Mrgln
> Uong Cnt
> Sht Cwnt
> UtwtclTD
> Rdl
> Uoherse
> Lenguay
> 0cay
> Oay
> Twncaton
> Nuualhabon
> Pasturtad
> NaNHalo
> UtHnUlno
> Ua Trede
> 2013
> 3.53
> .31.
> 1.9.
> 3 .
> 53:
> 15-
> U 
> TC?3O]
> 王 =C
> 0.03
> SJU
> 201-
> 7
>  
> 0.73
> 一?:
> 3.2:
> C:
> 1_-
> 2=
> 29
> :
> 2-5
> 12 :
> 污:
> 1 :
> 14
> Clone Alpha
> ZE
> 3
> 11.318
> 274
> 5
> 3:
> 1汜
> 143
> 3017
> 15#
> 05
> 1
> 51
> 116
> 71
> 15
> 002
> C4
> 41
> TST
> 1713
> 1-7
> Chart
> -715
> 1.75
> 2.35*
> 2.
> 15C
> 1T2
> 1-33
> 220
> 4:
> 11 :
> 3-7
> 1
> 11 _
> 537
> 二 :
> :
> 37.5:
> 17=
> 15
> 25'0712021
> TJDK
> Pn
> 37.-5k
> 222
> _:
> 8
> 汀
> 2:
> 1_73
> Rlk NeuralkedPnL-.
> 72
> U
> 03*
> :
> 1
> 20
> Risk neutralized
> Assresale Data
> |
> UTI@
> 0
> Ia11
> Jn 4
> Jon15
> 4Jn'16
> J `18
> Jung
> J3
> Jn 73
> 1.10
> 12.26%
> 0.58
> 3.51%
> 3.78%
> 390
> Rsk NEUTaIZEDPnl
> Pv
> _


4.  **Fama-MacBeth 回归检验结果如何？**

**- 代码：来自Brain Labs案例**


> [!NOTE] [图片 OCR 识别内容]
> 127T1
> TTnnr
> Tnyrl
> IINOTT
> 1 :n6rReorrssion
> TnTt
> SCTT';
> 517+-
> 5TT
> T Tegressionuf
> GaS:1 :
> Lhaci
> SIgnals With Fana
> I UetnNegresSrUI
> retyrns
> TUtrat170 UT
> df.sU(Jf.neanlaxis=
> 3115二 |
> Jetaye0
> 0+Tl
> 21116221
> NIMTCaITa
> 3h(
> SIL15=11
> ShTt'
> Olu5
> IqUJreo
> 「turns
> 6rnin
> 16rin
> Filgl"return '
> ITarr
> T-7-F
> inle
> RarrT
> STatisTIC2 simni-icae
> [131
> 01-+3
> LlVas
> 「-hnc1
> TCUFNS
> Ltves
> VEnenUent
> Whl
> VJLLU Isk
> LSMIN I
> 1LutLC' !
> 1SJMLY1
> T]
> YL]'6
> 711
> VLI11457k
> C-055-SC-tionl
> TTTC5TOI
> 1ET1
> 11+1
> [02l
> LIn=aTRTTEsSIOTI|
> [Tel
> 717
> U1
> NlU |
> Ltus_tLst
> OLL JIOLl
> SVare
> T
> predic: (x_validl
> CTTCIC
> C
> SCCCon
> TRnRT
> TnT3 |
> SIIy
> Tpeanly
> 6111902 1
> o111
> SITI
> 471+
> SOUaTE0
> 「1043
> TotalI
> total
> else np.nan
> SNI
> JTEN IT
> SIUaTECI
> elye
> [499
> JHL OOLT .Ih
> SNUHTCI
> UTTCTTTC
> NSa个
> TSTIEFT
> [+
> 1is1
> S141T
> i
> Std_rror
> M.Nasdlberas_lIst)
> {
> l
> TT{
> 1)
> U
> T+T
> 'tve
> ?Fro「
> 5tT
> CONTIOENC? Irtenal
> Cy
> TOTP
> UUII0T
> 953021
> 3TTUT
> SOFTIA/I
> JL[
> UULIIO
> ULJI CCl
> .90
> ISCU Crror
> SOTINI
> VU-Ia
> 1
> Ah
> TNITTTO
> Lrd listi
> prinz |
> H HEITeSSITI
> SUIT3T
> 5 |
> |CUS107
> 31
> LaT'
> SCCNI
> 9371
> 5LUCTror:
> LSLTTOUnUlsed CrTr
> mm
> IT+
> 1s?TTTOUNJIUCNC [
> JOI
> |
> [str(roud (upper_bound。 2)11 ]
> Th
> TUTTd
> 5TTTTomdlnn
> SAUTCI
> 711
> U1 
> 015 ;
> 4541559
> 0;|
> 71+
> OFOI ^


**- 计算结果**


> [!NOTE] [图片 OCR 识别内容]
> U
> Bralnlregions UsA 
> PLJ-
> UVerse=' TopJe30]
> daulleld_dl
> UToLIsy UJ
> 1JnICTJ-I
> Uulu
> 1UUJIU
> CUStieLg_Tets-y
> TCgTc55?oplo7tt1ocd 01
> KCICUl
> UII
> ]+ *
> 'TI
> PTFII '
> 95 ConTicens
> Tneryal :
> 177
> SOULCeC
> Vuld_duy: 251
> 「S


**- 结论分析（借助Kimi大模型）**

**
> [!NOTE] [图片 OCR 识别内容]
> 指标
> 数值
> 含义
> mean_beta
> -1.85
> 每增加1个标准差
> 未来收益平均下跌1.85%
> t_Value
> -9.99
> 极度显著 (p ~ 0)
> 95% CI
> [-2.21,-1.48]
> 不包含 0,方向稳定
> Valid_days
> 2517
> 10 年+的样本,极度稳健
> mean
> squared
> 0.0
> 横截面 解释力极低
> 但这不是问题
> (FM 回归 Rz 通常都很低)
**

**- 结论：这是一个极度显著、方向稳定、样本充足的反向因子**

**三、 验证二步回归结果**

**1. 用rank≥0.7和sign≥0.4实证二步回归检验**

**- rank验证：sharpe标准0.87×0.7=0.61＜0.67，合格**


> [!NOTE] [图片 OCR 识别内容]
> U
> Created 09/082025 EDT
> anonymOUs
> Add Nphato
> Ust
> Code
> IS Summary
> Perod
> 0VI3_custretsig retslg;
> 吣 Snele Data Setsloha
> rank (a)
> ASBregate Data
> SharDs
> TUrno=
> Flnes:
> C
> Orawgowr
> Wrain
> 0.67
> 15.5096
> 0.34
> 3.9996
> 12.59%
> 5.1596o0
> Simulation Settines
> IstrUMI Typa
> Reolon
> Uherse
> LnOage
> Co
> Oy
> Truneton
> Neutllnwon
> Pastewrtato
> NaNHang
> Unlt HanO
> Nax Tmd
> Shalp
> Tutwer
> Fgs
> Returns
> Dewdown
> Uagln
> Log Cont
> Shot Count
> Sauny
> C-
> TO-J
> Fast S Cressn
> T
> 0.03
> SubnJ-sr
> =r
> 7013
> 0,7
> 1537:
> 03
> 77
> C3-
> 33:
> 15
> 1
> -1
> 7
> 1_7-:
> CEJ
> 459沁
>  .
> 5--
> 1533
> 15-
> 301=
> 0.3
> 15
> 0?
> 303
> 251汨
> '130
> 157
> 153
> Clone Alpha
> -015
> 0.34
> 1-37-
> 037
> 二75:
> ~55.
> 33-
> 三
> 127
> 2017
> 111
> 12
> 5855
> 2376
> 3319
> 521
> 1527
> Chart
> nl
> 2013
>  E
> 1_5:
> 0=
> Cs:
> 225
> 77:
> =
> 1525
> 2019
> .34
> 151
> 0.10
> 1.21沿
> 85汩
> 52
> 115
> 152
> 01
> 153:
> 140
> 3
> 1E
> 5;
> T=
> 1513
> 一-
> 5
> 17.3
> 0-J
> 1.07
> 9.33
> 3
> 154
> 1SE_
> 0JJ
> 11/232018
> 3022
> 0.1E
> 1535
> 005
> 4沿
> C12
> 157:
> 11
> 1573
> Du
> 333.17
> Risk Neutralized Pnl
> 582.36<
> -
> 15_
> 131
> 11.75.
> T1
> -:
> 1-3
> 1537
> Risk neutralized
> Jn '14
> JaT 15
> 0715
> Ja
> 13713
> 119
> J2
> 157.71
> J7 -
> J2
> Aeereeate Data
> Sharce
> IUTTO
> Finess
> FetUCN
> 903OU
> Warein
> 0.71
> 15.509
> 0.23
> 1.5996
> 6.5490
> 2.0596oo
> Pn
> Risk Neutralzeo Pnl


**- sign验证：sharpe标准0.87×0.4=0.35＜0.54，合格**

**
> [!NOTE] [图片 OCR 识别内容]
> UNSUB
> Created 09;08/2025 EDT
> anonymous
> uodphato
> Ust
> Code
> IS Summary
> Perod
> Custretsig retsig;
> 0 Snele Data Set slpha
> sign (a)
> Aeeregate Data
> Sharp=
> UTMC Ir
> Fisness
> T=upns
> OTaUT
> Nsrain
> 0.52
> 12.1296
> 0.24
> 2.4596
> 12.78%
> 4.049600
> Simulation Settines
> IstrumltType
> Reolo
> Uhers
> Lnoage
> Cy
> Oely
> TNNCton
> Newtllawon
> Rastertzatm
> NaN Handlg
> Unlt Handwng
> Ia Tmd
> Sherpe
> 
> Fes
> Rts
> Dowdowm
> Noym
> Lo Co
> Shot Count
> Sury
> U-
> TO-J
> Fast SpressIen
> TZE
> 0.03
> Subindusoy
> Ur
> T0
> Cs
> 14
> Ds
> 3
> 222:
> 302:
> 151
> 131
> 2011
> 11.459
> 0.82
> 4419
> 4.15
> 7.7C.
> 53
> 15_
> 2015
> 025
> 113
> DDE
> 7.
> 3
> 2
> 5
> 1565
> Alpha
> ZOIE
> 031
> |_
> 0.03
> 0.35:
> 1
> SL:
> 110
> 1SES
> 2017
> TCE
> 11635
> 0.3
> 41
> 3
> J5
> 435
> 1545
> N Chart
> Pnl
> TO
> 0E3
> 41 =
> 0
> 1.359:
> 3:
> 37:
> =13
> 1=3
> 201
> +0.20
> 121
> 4
> 5
> 243
> 0.9
> 4
> 1545
> 3030
> 731
> =
> 73
> 17-
> 11
> 72:
> 13
> 19
> -1
> DS
> 1.759
> 031
> 4+9
> 1559
> 551.
> 45
> 15-3
> 7OD
> 702
> 011
> 1705
> D0
> 32.
> E S2.
> 5.711:
> 1513
> 1E01
> DJO
> 一
> .-5
> 125
> |
> 7.519
> 0.5:
> S:
> 110
> 1-
> Risk neutralized
> Jny
> Ja 15
> 17 16
> Ja
> Jan8
> Jan9
> Jan '20
> 1371
> J7 -
> Jn
> AEEregate Data
> SNarce
> Turnove
> Fihe_=
> Reury_
> DrawJowi
> Warsin
> 0.51
> 12.12%
> 0.15
> 1.06%
> 4.84%
> 1.759600
> Pn_
> Risk NeJralzzo Pn_
> 0v13
> Clone
**

**2. 分组、验证、增强并提交：** 用ts_rank进行增强并提交

**- 分组：sharpe=1.57**


> [!NOTE] [图片 OCR 识别内容]
> UNISUB
> Cregted 09.082025 EDT
> JnonymOs
> * pha
> 3Lst
> Code
> IS Summary
> Prodl
> custretsig_rets 琚;
> 眺 See Dats Ser Mloh3
> Broup_Fank(u, subindustry);
> Hat
> Dar
> TITTI
> TITE
> CT
> Warar
> 12.2690
> 1,25
> ,95%6
> 4489
> 12.969000
> SIIIIITIOI
> Setrlnzs
> Srpo
> Tunou
> T
> Reume
> OIoo
> Mrgln
> Uong Cnt
> Sht Cwnt
> UtwtclTD
> Rdl
> Uoherse
> Lenguay
> 0cay
> Oay
> Twncaton
> Nuualhabon
> Pasturtad
> NaNHalo
> UtHnUlno
> Ua Trede
> 2013
> 3.53
> .31.
> 1.9.
> 3 .
> 53:
> 15-
> U 
> TC?3O]
> 王 =C
> 0.03
> SJU
> 201-
> 7
>  
> 0.73
> 一?:
> 3.2:
> C:
> 1_-
> 2=
> 29
> :
> 2-5
> 12 :
> 污:
> 1 :
> 14
> Clone Alpha
> ZE
> 3
> 11.318
> 274
> 5
> 3:
> 1汜
> 143
> 3017
> 15#
> 05
> 1
> 51
> 116
> 71
> 15
> 002
> C4
> 41
> TST
> 1713
> 1-7
> Chart
> -715
> 1.75
> 2.35*
> 2.
> 15C
> 1T2
> 1-33
> 220
> 4:
> 11 :
> 3-7
> 1
> 11 _
> 537
> 二 :
> :
> 37.5:
> 17=
> 15
> 25'0712021
> TJDK
> Pn
> 37.-5k
> 222
> _:
> 8
> 汀
> 2:
> 1_73
> Rlk NeuralkedPnL-.
> 72
> U
> 03*
> :
> 1
> 20
> Risk neutralized
> Assresale Data
> |
> UTI@
> 0
> Ia11
> Jn 4
> Jon15
> 4Jn'16
> J `18
> Jung
> J3
> Jn 73
> 1.10
> 12.26%
> 0.58
> 3.51%
> 3.78%
> 390
> Rsk NEUTaIZEDPnl
> Pv
> _


**- rank验证：sharpe标准=1.57×0.7=1.1＜1.57，合格**


> [!NOTE] [图片 OCR 识别内容]
> UNS
> Creglsd 09082025 EDT
> anonymOus
> NJDataJS
> Code
> IS Summary
> PuTrod
> pVI3_custretsJB_Fets g;
> [ See Dats Ser Moha
> PTUIV
> Tank(a, subindustry);
> eank {)
> AEBreeate
> 0C3
> TUTTO
> TICN
> TTJTI
> LTyC
> 1.57
> 12.2690
> 1,25
> 7.9790
> 4.509
> 3,019000
> SIIUIaton Settllzs
> WotwelTYD
> Reglon
>  UoNerse
> UB
> Way
> Tmncaton
> Nuballallon
> [-T
> NaNHandlg
> UntHanolng
> Ua Trede
> Ver
> Cro
> Tmg
> Ft
> Reum
> [r
> Wrgln
> Long Cont
> Shot Cont
> TS?
> Fast XPres:?
> 7.13
> Subindustr
> Vn
> 21
> 3.D
> .5.
> C
> 1.5
> 3.5.
> 275:
> 15
> 201-
> 1
> 一_ :
> 一?
> 3
> =:
> 1__
> 3
> ;
> 10.2 :
> 污:
> 5:
> Clone Alpha
> ZE
> 38
> 277*
> 3
> 1u
> 3017
> 0.31
> 0
> AE
> 45
> 二!
> 113
> 2018
> 52.
> C
> [J
> 4.17
> TSE
> 1715
> 147
> N Chart
> 2115
> |
> 20
> 1-SC
> 20120
> 2
> 1015
> 3.
> 1 -
> 1-11
> 2.55
> C_:
> Js :
> :
> _:
> 1
> -3
> 222
> 222
> 210:
> 3污-
> =:
> 17
> 1212'2213
> 51
> 2
> 3
> SDK
> 2315r
> RLsk Neutrallzed PnL 1ASE 6S
> Risk neutralized
> DUu
> Orauro
> Jr'20
> In 
> Jn 77
> 1.09
> 12.269
> 0.58
> 3.529
> 3.84%
> 5.74960
> ZSKNEE
> ZEU Pnl
> 0a
> 三」
> ?5
> Fesi
> SLut


**- sign验证：sharpe标准1.57×0.4=0.63＜1.42，合格**


> [!NOTE] [图片 OCR 识别内容]
> UNS
> Creglsd 09082025 EDT
> anonymOus
> NJDataJS
> Code
> IS Summary
> PuTrod
> DVIL
> custretsiB_rets 氓;
> 昵 Sele Dats Ser Nlph3
> PTUIV
> Tank(a, subindustry);
> SLBn ()
> AEBreeate Data
> 3C=
> LUIFnC
> TTS
> TZUTT
> a
> 42
> 5,7
> 1,14
> 8,009
> 5,5791
> 28,029000
> SIIUIaUOn SetUnas
> WotwelTYD
> Reglom
>  UoNerse
> UB
> Tmncaton
> Nuballallon
> [-T
> NaNHandlg
> UntHanolng
> 2
> Ver
> Chc
> Tuler
> 「t
> Rhr
> 0r
> Marglm
> Cnt
> Shot Cont
> TS?
> Fast XPres:?
> 7.13
> Sidustr
> 711
> 3
> 3
> 537.
> 4.529
> |.
> 一_
> S.E
> E:
> 3.1:
> 3+:
> 1E
> 3
> -5:
> 12-3:
> :
> Clone Alpha
> ZIE
> 143:
> 4.21.
> 3017
> 055
> Cr
> 5
> 31
>  T.
> 2018
> 055
> 1.57 .
> 4,139.
> 5ZS
> 153
> 113
> N Chart
> 2115
> 7-
> 5.03
> 3 .
> .239
> 3.
> 15
> 220
> ~5
> 5715
> 03
> 一-
> :
> 53
> 2:
> 一:
> :
> 2017
> 137
> DDK
> C1272
> 222
> -5
> 312:
> 污:
> 1218
> 355.52k
> Risk Nautralzed PnL:
> 3153
> 22
> :
> 0.738
> 15;
> 1
> 2S3cK
> Risk neutralized
> Aesregate
> DUu
> TurnO
> Rlurr
> SISJ
> Warel
> Jun 14
> en '1
> In 
> Jn 77
> 0.91
> 5.70%
> 0.46
> 3.23%
> 4.8795
> 11.3496
> Pnl
> Risk NEUTaIZED Pnl
> Uen
> 0a
> Ct
> 20
> 5:
> DT
> 2;
> gL


**- ts_rank增强并提交**

**
> [!NOTE] [图片 OCR 识别内容]
> ACV
> Cralsd OSOS 2025 EDT
> anonymoUs
> AU Aphgt 3 UIst
> Code
> IS Summary
> Period
> a 「CVerse(ts
> Fank (EFCUP
> TMI
> CustretsJB_retsJ'
> subindustry)
> 752));
> ICme
> VarasetUtilaton Iheme
> 昵 Sirale Daza Ser Alpha
> Power Pol Alpha
> Pramio there: USNDIIPV &1
> NEBreEate
> 0ara
> TITTI
> CIT
> Crano
> 13.8590
> 1.25
> 7,789
> 6.349
> 11.,249000
> SIIUIatIor
> Settinss
> ImuTR 
> Reglon
>  Uner
> URU
> De
> Tmncgtn
> N-uuallaton
> Pasturbouo
> NoN Helclg
> Unt Hanoung
> Ue Trede
> S[ 
> Tum
> T
> UI
> Io
> OM
> on Cun
> Sht Cont
> TC-
> Fsst SFrsss ?
> 1.23
> Sbindustr
> 2513
> 17
> 12-3
> 1_ .
> 53:
> 1s+E
>  _
> _
> E.S
> 207:
> 3:
> 1ss
> 2015
> 1_-
> 一1::;
> 17-
> 洪:
> 125
> Clone Alpha
> ZTE
> 14
> 1
> 70_
> 377-
> -
> 1_汇
> 3017
> 1-
> 5
> 15
> E
> 1
> N Chart
> 211
> 1
> 5.25玷
> 1
> 3.25
> 715
> 1235
> E.23沿
> -3.
> 10.51:
> 1
> 一
> 5:
> 一5
> E
> 5:
> 1-3
> :
> 23.75沿
> 43:
> 3:
> U
> 13
> SDDK
> 2122
> _
> 473-
> C:
> 1
> 1_5
> OIJE -13
> 
> E
> J
> ~抵;
> 118
> 15Pnl  3353.E2
>  =JO
> Risk neutralized
> HSICSJL
> 1
> T
> U
> Marein
> 24
> 13.859
> 0.59
> 3.0995
> 4.31%
> 4.46950
> 1
> 1n
> 3__
> In _
> Pv13
> Ce
> 』
> TL
> ShaTF
**

**3. 总结：** 金融与资产定价研究中，Fama-MacBeth 回归（1973）至今仍是国际学术界最主流、最通用、最被认可的因子显著性检验框架之一 ——  **解释来自借助Kimi大模型**

- 能够通过二步回归检验，说明因子的预测性是显著的，能够在很大程度上确保OS的稳定。

- 建议在后续因子分析中，有条件的情况下，应首先进行二步回归，避免走弯路，提高分析效率。

- 在一定程度上说明，rank≥0.7和sign≥0.4的验证是有效的（相对宽松），在simulator中可以使用。

**顾问 JX79797 (Rank 9) 的解答与建议**:
[LR93609](/hc/en-us/profiles/30244554462231-LR93609)     冷兄的一系列 灵感贴 看了很有启发， 目前集中在框架、mcp，下季度一定好好研究研究！！！

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 13 (原帖: 中文版：Alpha 解析工作流程)
- **原帖链接**: [Commented] 【MCP WorkFlow】一个使用MCP来给Alpha写描述并获取更多启发的工作流.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
我们都知道，要发挥MCP的功能，就需要把它当作我们的秘书。以下是一个参考工作流，你可以让它照着做，并把Alpha表达式和Region给它，就能给你Alpha进行解释，并给你进一步点塔的启发，和撰写description的台词。

# Alpha Explanation Workflow

This manual provides a step-by-step workflow for analyzing and explaining a WorldQuant BRAIN alpha expression. By following this guide, you can efficiently gather the necessary information to understand the logic and potential strategy behind any alpha.

## Step 1: Deconstruct the Alpha Expression

The first step is to break down the alpha expression into its fundamental components:  **data fields**  and  **operators** .

For example, given the expression  `quantile(ts_regression(oth423_find,group_mean(oth423_find,vec_max(shrt3_bar),country),90))` :

- **Data Fields:**   `oth423_find` ,  `shrt3_bar`
- **Operators:**   `quantile` ,  `ts_regression` ,  `group_mean` ,  `vec_max`

## Step 2: Analyze Data Fields

Use the  `brain-platform-mcp`  tool  `get_datafields`  to get detailed information about each data field.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_datafields</tool_name> <arguments> { "instrument_type": "EQUITY", "region": "ASI", "delay": 1, "universe": "MINVOL1M", "data_type": "VECTOR", "search": "shrt3_bar" } </arguments> </use_mcp_tool>`

**Tips for effective searching:**

- **Specify Parameters:**  Always provide as much information as you know, including  `instrument_type` ,  `region` ,  `delay` ,  `universe` , and  `data_type`  ( `MATRIX`  or  `VECTOR` ).
- **Iterate:**  If you don't find the data field on your first try, try different combinations of parameters. The  `ASI`  region, for example, has two universes:  `MINVOL1M`  and  `ILLIQUID_MINVOL1M` .
- **Check Data Type:**  Be sure to check if the data is a  `MATRIX`  (one value per stock per day) or a  `VECTOR`  (multiple values per stock per day). This is crucial for understanding how the data is used.

**Example Data Field Information:**

- **`oth423_find`** : A  **matrix**  data field from the "Fundamental Income and Dividend Model" dataset in the ASI region. It represents a "Find score," likely indicating fundamental attractiveness.
- **`shrt3_bar`** : A  **vector**  data field from the "Securities Lending Files Data" dataset in the ASI region. It provides a vector of ratings (1-10) indicating the demand to borrow a stock, which is a proxy for short-selling interest.

## Step 3: Understand the Operators

Use the  `brain-platform-mcp`  tool  `get_operators`  to get a list of all available operators and their descriptions.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_operators</tool_name> <arguments> {} </arguments> </use_mcp_tool>`  The output of this command contains a wealth of information. For your convenience, a table of the most common operators is included in the Appendix of this manual.

## Step 4: Consult Official Documentation

For more complex topics, the official BRAIN documentation is an invaluable resource. Use the  `get_documentations`  tool to see a list of available documents, and  `get_documentation_page`  to read a specific page.

**Example:**  To understand vector data fields better, I consulted the "Vector Data Fields ðŸ¥‰" document ( `vector-datafields` ). This revealed that vector data contains multiple values per instrument per day and must be aggregated by a vector operator before being used with other operators.

## Step 5: Broaden Understanding with External Research (Optional)

For cutting-edge ideas and inspiration, you can search for academic papers on arXiv using the provided  `arxiv_api.py`  script.

**Workflow:**

1. **Identify Keywords:**  Based on your analysis of the alpha, identify relevant keywords. For our example, these were:  `"short interest"` ,  `"fundamental analysis"` ,  `"relative value"` , and  `"news sentiment"` .
2. **Run the Script:**  Use the  `with-wrappers`  script to avoid SSL errors.
   ```
   python arxiv_api.py "your keywords here" -n 10
   ```

## Step 6: Synthesize and Explain

Once you have gathered all the necessary information, structure your explanation in a clear and concise format. The following template is recommended:

- **Idea:**  A high-level summary of the alpha's strategy.
- **Rationale for data used:**  An explanation of why each data field was chosen and what it represents.
- **Rationale for operators used:**  A step-by-step explanation of how the operators transform the data to generate the final signal.
- **Further Inspiration:**  Ideas for new alphas based on your research.

## Troubleshooting

- **SSL Errors:**  If you encounter a  `CERTIFICATE_VERIFY_FAILED`  error when running python scripts that access the internet, use the  `AI to help you change or make`  script to execute your command.

## Appendix A: Understanding Vector Data

Vector Data is a distinct type of data field where the number of events recorded per day, per instrument, can vary. This is in contrast to standard matrix data, which has a single value for each instrument per day.

For example, news sentiment data is often a vector because a stock can have multiple news articles on a single day. To use this data in most BRAIN operators, it must first be aggregated into a single value using a  **vector operator** .

**顾问 JX79797 (Rank 9) 的解答与建议**:
[SK10818](/hc/en-us/profiles/29090704445463-SK10818)

是的，输入框直接输入，使用xxxx.md工作流，为xxxxx(表达式)输出描述

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 14 (原帖: 中文版：Alpha 解析工作流程)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【MCP WorkFlow】一个使用MCP来给Alpha写描述并获取更多启发的工作流_34213553037335.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
我们都知道，要发挥MCP的功能，就需要把它当作我们的秘书。以下是一个参考工作流，你可以让它照着做，并把Alpha表达式和Region给它，就能给你Alpha进行解释，并给你进一步点塔的启发，和撰写description的台词。

# Alpha Explanation Workflow

This manual provides a step-by-step workflow for analyzing and explaining a WorldQuant BRAIN alpha expression. By following this guide, you can efficiently gather the necessary information to understand the logic and potential strategy behind any alpha.

## Step 1: Deconstruct the Alpha Expression

The first step is to break down the alpha expression into its fundamental components:  **data fields**  and  **operators** .

For example, given the expression  `quantile(ts_regression(oth423_find,group_mean(oth423_find,vec_max(shrt3_bar),country),90))` :

- **Data Fields:**   `oth423_find` ,  `shrt3_bar`
- **Operators:**   `quantile` ,  `ts_regression` ,  `group_mean` ,  `vec_max`

## Step 2: Analyze Data Fields

Use the  `brain-platform-mcp`  tool  `get_datafields`  to get detailed information about each data field.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_datafields</tool_name> <arguments> { "instrument_type": "EQUITY", "region": "ASI", "delay": 1, "universe": "MINVOL1M", "data_type": "VECTOR", "search": "shrt3_bar" } </arguments> </use_mcp_tool>`

**Tips for effective searching:**

- **Specify Parameters:**  Always provide as much information as you know, including  `instrument_type` ,  `region` ,  `delay` ,  `universe` , and  `data_type`  ( `MATRIX`  or  `VECTOR` ).
- **Iterate:**  If you don't find the data field on your first try, try different combinations of parameters. The  `ASI`  region, for example, has two universes:  `MINVOL1M`  and  `ILLIQUID_MINVOL1M` .
- **Check Data Type:**  Be sure to check if the data is a  `MATRIX`  (one value per stock per day) or a  `VECTOR`  (multiple values per stock per day). This is crucial for understanding how the data is used.

**Example Data Field Information:**

- **`oth423_find`** : A  **matrix**  data field from the "Fundamental Income and Dividend Model" dataset in the ASI region. It represents a "Find score," likely indicating fundamental attractiveness.
- **`shrt3_bar`** : A  **vector**  data field from the "Securities Lending Files Data" dataset in the ASI region. It provides a vector of ratings (1-10) indicating the demand to borrow a stock, which is a proxy for short-selling interest.

## Step 3: Understand the Operators

Use the  `brain-platform-mcp`  tool  `get_operators`  to get a list of all available operators and their descriptions.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_operators</tool_name> <arguments> {} </arguments> </use_mcp_tool>`  The output of this command contains a wealth of information. For your convenience, a table of the most common operators is included in the Appendix of this manual.

## Step 4: Consult Official Documentation

For more complex topics, the official BRAIN documentation is an invaluable resource. Use the  `get_documentations`  tool to see a list of available documents, and  `get_documentation_page`  to read a specific page.

**Example:**  To understand vector data fields better, I consulted the "Vector Data Fields ðŸ¥‰" document ( `vector-datafields` ). This revealed that vector data contains multiple values per instrument per day and must be aggregated by a vector operator before being used with other operators.

## Step 5: Broaden Understanding with External Research (Optional)

For cutting-edge ideas and inspiration, you can search for academic papers on arXiv using the provided  `arxiv_api.py`  script.

**Workflow:**

1. **Identify Keywords:**  Based on your analysis of the alpha, identify relevant keywords. For our example, these were:  `"short interest"` ,  `"fundamental analysis"` ,  `"relative value"` , and  `"news sentiment"` .
2. **Run the Script:**  Use the  `with-wrappers`  script to avoid SSL errors.
   ```
   python arxiv_api.py "your keywords here" -n 10
   ```

## Step 6: Synthesize and Explain

Once you have gathered all the necessary information, structure your explanation in a clear and concise format. The following template is recommended:

- **Idea:**  A high-level summary of the alpha's strategy.
- **Rationale for data used:**  An explanation of why each data field was chosen and what it represents.
- **Rationale for operators used:**  A step-by-step explanation of how the operators transform the data to generate the final signal.
- **Further Inspiration:**  Ideas for new alphas based on your research.

## Troubleshooting

- **SSL Errors:**  If you encounter a  `CERTIFICATE_VERIFY_FAILED`  error when running python scripts that access the internet, use the  `AI to help you change or make`  script to execute your command.

## Appendix A: Understanding Vector Data

Vector Data is a distinct type of data field where the number of events recorded per day, per instrument, can vary. This is in contrast to standard matrix data, which has a single value for each instrument per day.

For example, news sentiment data is often a vector because a stock can have multiple news articles on a single day. To use this data in most BRAIN operators, it must first be aggregated into a single value using a  **vector operator** .

**顾问 JX79797 (Rank 9) 的解答与建议**:
[SK10818](/hc/en-us/profiles/29090704445463-SK10818)

是的，输入框直接输入，使用xxxx.md工作流，为xxxxx(表达式)输出描述

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 15 (原帖: 【MCP workflow】根据GLB的alpha，自动挖掘其他地区alpha的工作流)
- **原帖链接**: [Commented] 【MCP workflow】根据GLB的alpha自动挖掘其他地区alpha的工作流.md
- **时间**: 9个月前

**提问/主帖背景 (FF56620)**:
基于weijie老师的分享，我选择了「根据GLB的alpha，来挖掘其他地区的alpha」这个部分的内容，进行了MCP的workflow探索，简单尝试了几个alpha，发现效果还不错，跟大家分享一下工作流，希望有所帮助。

先贴一下效果，我选取的alpha在亚洲表现不错，所以工作流探索了ASI地区


> [!NOTE] [图片 OCR 识别内容]
> 原始
> Alpha 3NV3QKe
> 区域表现:
> GLB_APAC: Sharpe
> 2.37
> 收益率
> 3.40%,
> Pnl
> 3.52M
> 最佳 )
> 
> 
> GLB_EMEA:
> Sharpe 1.16,
> 收益率
> 1.45%
> Pnl
> 1.SOMe
> GLB_AMER:
> Sharpe 0.93,
> 收益率
> 0.62%,
> Pnl
> 0.G4M
> 低 Sharpe 告警
> 
> 
> 
> 
> ASI
> 区域替换字段回测
> (均启用
> max_trade-ON)
> 
> 
> Alpha Zeojbyb: Sharpe
> 1.62,
> 收益率
> 4.43%,
> Pnl
> 4.58M
> 鲁棒指标偏弱 _
> 需强化 )
> 
> 2
> Alpha KWm7dgN: Sharpe 0.87,
> 收益率
> 2.43%,
> Pnl
> 2.52M (信号较弱 )
> 
> 
> 3
> Alpha dNKjVgg: Sharpe 1.46,
> 收益率
> 3.91%,
> Pnl
> 4.Q4M (介于两者之间 )
> 
> 
> 
> 
> 
> 结论要点:
> 
> 
> 亚太季度频率字段继承原信号
> 收益率提升但
> Fitness
> 鲁棒性仍待优化
> 
> 
> 年度 /半年度数据更新慢_
> 信号衰减明显
> 
> 
> 
> 可在既有模板上叠加
> winsorize
> 截断或共享其他盈利字段 ,
> 以提高提交合格率 ,
> 再迂移回
> GLB 做终测


可以看到，在ASI区域，该字段映射效果还不错，但由于max_trade的开启与鲁棒性检测，存在部分不通过的情况，需要进行微调。

工作流内容如下：

> # 跨区域相似因子挖掘工作流
> ## 阶段一：基线诊断
> - 输入 `alpha_id`，调用 `wqb_mcp__get_alpha_details` 获取原因子的区域、参数配置以及各地区表现。
> - 整理 Sharpe、收益率、警报等指标，为后续的区域选择和策略调整提供依据。
> ## 阶段二：信号拆解
> - 解析 Alpha 代码，定位核心数据字段及其操作符结构。
> - 使用 `wqb_mcp__get_datafields`（参数沿用原始区域、universe、delay 等设置）获取field的描述信息，并进行理解。
> ## 阶段三：目标区域映射与字段检索
> - 根据已知区域映射确定迁移区域：`APAC → ASI`、`EMEA → EUR`、`AMER → USA`。
> - 对于每个目标区域，优先使用与原因子相同的 `dataset_id` 调用 `wqb_mcp__get_datafields`；若该数据集在目标区域不可用，则改用相同 `category` 并通过字段关键字搜索。
> - 在确保 `instrument_type`、`delay`、`universe` 等参数匹配的同时，筛选出描述、覆盖率和使用度最接近的字段，建立候选字段池，候选字段池建议为3-8个，一次回测可完成。
> ## 阶段四：候选因子构建
> - 以原公式为模板，将核心字段替换为候选字段，并视需要添加 winsorize、截断、混合周期等调节操作。
> - 保持中性化方式、衰减、延迟等关键参数一致，以保证结果可比性。
> ## 阶段五：批量回测与评估
> - 使用 `wqb_mcp__create_multiSim`（或多次 `wqb_mcp__create_simulation`）在目标区域批量回测候选因子，在 ASI 区域必须开启 `max_trade` 为 `ON`，其他区域使用和选择数据相同的universe即可，其他参数不用调整。
> - 记录 Sharpe、Fitness、鲁棒性检查、风险中性结果等核心指标，并保存 Simulation ID 以便复现与归档。
> ## 阶段六：验证与推广
> - 对表现较好的候选，进行两轮有经济学含义的operator增加和删减，找出表现最好的alpha。
> - 将优胜策略迁移到其他映射区域或回到全域回测，并形成标准化报告，包含字段来源、回测指标及后续优化建议。

大家可以尝试更多的alpha，同时这个策略是从GLB映射到其他地区，其实也可以从其他地区映射到GLB，对工作流进行少量修改即可，如有帮助，请点赞。

更多MCP workflow，可参考我往期帖子，自动挖掘，降turnover，手机使用mcp等

**顾问 JX79797 (Rank 9) 的解答与建议**:
非常好的使用场景，基于分享，自己也想到了两个idea，等国庆期间发帖分享给大家，共同进步，早日gm.

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 16 (原帖: 【MCP workflow】根据GLB的alpha，自动挖掘其他地区alpha的工作流)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【MCP workflow】根据GLB的alpha自动挖掘其他地区alpha的工作流_35239747718679.md
- **时间**: 9个月前

**提问/主帖背景 (FF56620)**:
基于weijie老师的分享，我选择了「根据GLB的alpha，来挖掘其他地区的alpha」这个部分的内容，进行了MCP的workflow探索，简单尝试了几个alpha，发现效果还不错，跟大家分享一下工作流，希望有所帮助。

先贴一下效果，我选取的alpha在亚洲表现不错，所以工作流探索了ASI地区


> [!NOTE] [图片 OCR 识别内容]
> 原始
> Alpha 3NV3QKe
> 区域表现:
> GLB_APAC: Sharpe
> 2.37
> 收益率
> 3.40%,
> Pnl
> 3.52M
> 最佳 )
> 
> 
> GLB_EMEA:
> Sharpe 1.16,
> 收益率
> 1.45%
> Pnl
> 1.SOMe
> GLB_AMER:
> Sharpe 0.93,
> 收益率
> 0.62%,
> Pnl
> 0.G4M
> 低 Sharpe 告警
> 
> 
> 
> 
> ASI
> 区域替换字段回测
> (均启用
> max_trade-ON)
> 
> 
> Alpha Zeojbyb: Sharpe
> 1.62,
> 收益率
> 4.43%,
> Pnl
> 4.58M
> 鲁棒指标偏弱 _
> 需强化 )
> 
> 2
> Alpha KWm7dgN: Sharpe 0.87,
> 收益率
> 2.43%,
> Pnl
> 2.52M (信号较弱 )
> 
> 
> 3
> Alpha dNKjVgg: Sharpe 1.46,
> 收益率
> 3.91%,
> Pnl
> 4.Q4M (介于两者之间 )
> 
> 
> 
> 
> 
> 结论要点:
> 
> 
> 亚太季度频率字段继承原信号
> 收益率提升但
> Fitness
> 鲁棒性仍待优化
> 
> 
> 年度 /半年度数据更新慢_
> 信号衰减明显
> 
> 
> 
> 可在既有模板上叠加
> winsorize
> 截断或共享其他盈利字段 ,
> 以提高提交合格率 ,
> 再迂移回
> GLB 做终测


可以看到，在ASI区域，该字段映射效果还不错，但由于max_trade的开启与鲁棒性检测，存在部分不通过的情况，需要进行微调。

工作流内容如下：

> # 跨区域相似因子挖掘工作流
> ## 阶段一：基线诊断
> - 输入 `alpha_id`，调用 `wqb_mcp__get_alpha_details` 获取原因子的区域、参数配置以及各地区表现。
> - 整理 Sharpe、收益率、警报等指标，为后续的区域选择和策略调整提供依据。
> ## 阶段二：信号拆解
> - 解析 Alpha 代码，定位核心数据字段及其操作符结构。
> - 使用 `wqb_mcp__get_datafields`（参数沿用原始区域、universe、delay 等设置）获取field的描述信息，并进行理解。
> ## 阶段三：目标区域映射与字段检索
> - 根据已知区域映射确定迁移区域：`APAC → ASI`、`EMEA → EUR`、`AMER → USA`。
> - 对于每个目标区域，优先使用与原因子相同的 `dataset_id` 调用 `wqb_mcp__get_datafields`；若该数据集在目标区域不可用，则改用相同 `category` 并通过字段关键字搜索。
> - 在确保 `instrument_type`、`delay`、`universe` 等参数匹配的同时，筛选出描述、覆盖率和使用度最接近的字段，建立候选字段池，候选字段池建议为3-8个，一次回测可完成。
> ## 阶段四：候选因子构建
> - 以原公式为模板，将核心字段替换为候选字段，并视需要添加 winsorize、截断、混合周期等调节操作。
> - 保持中性化方式、衰减、延迟等关键参数一致，以保证结果可比性。
> ## 阶段五：批量回测与评估
> - 使用 `wqb_mcp__create_multiSim`（或多次 `wqb_mcp__create_simulation`）在目标区域批量回测候选因子，在 ASI 区域必须开启 `max_trade` 为 `ON`，其他区域使用和选择数据相同的universe即可，其他参数不用调整。
> - 记录 Sharpe、Fitness、鲁棒性检查、风险中性结果等核心指标，并保存 Simulation ID 以便复现与归档。
> ## 阶段六：验证与推广
> - 对表现较好的候选，进行两轮有经济学含义的operator增加和删减，找出表现最好的alpha。
> - 将优胜策略迁移到其他映射区域或回到全域回测，并形成标准化报告，包含字段来源、回测指标及后续优化建议。

大家可以尝试更多的alpha，同时这个策略是从GLB映射到其他地区，其实也可以从其他地区映射到GLB，对工作流进行少量修改即可，如有帮助，请点赞。

更多MCP workflow，可参考我往期帖子，自动挖掘，降turnover，手机使用mcp等

**顾问 JX79797 (Rank 9) 的解答与建议**:
非常好的使用场景，基于分享，自己也想到了两个idea，等国庆期间发帖分享给大家，共同进步，早日gm.

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 17 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-12-05

连续回测的第245天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 63

#### 本赛季表现指标

- RA Count: 244
- RA Prod Corr: 0.6044
- RA Self Corr: 0.2421
- SA Count: 54
- SA Prod Corr: 0.5124
- SA Self Corr: 0.4263

#### 最近两周表现指标

- RA Count: 49
- RA Prod Corr: 0.6399
- RA Self Corr: 0.2445
- SA Count: 15
- SA Prod Corr: 0.4189
- SA Self Corr: 0.3289

#### 最近一周表现指标

- RA Count: 28
- RA Prod Corr: 0.6888
- RA Self Corr: 0.2653
- SA Count: 8
- SA Prod Corr: 0.4144
- SA Self Corr: 0.3964

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 18 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-12-06

连续回测的第246天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 63

#### 本赛季表现指标

- RA Count: 248
- RA Prod Corr: 0.6044
- RA Self Corr: 0.2421
- SA Count: 55
- SA Prod Corr: 0.5124
- SA Self Corr: 0.4263

#### 最近两周表现指标

- RA Count: 49
- RA Prod Corr: 0.6399
- RA Self Corr: 0.2445
- SA Count: 15
- SA Prod Corr: 0.4189
- SA Self Corr: 0.3289

#### 最近一周表现指标

- RA Count: 28
- RA Prod Corr: 0.6888
- RA Self Corr: 0.2653
- SA Count: 8
- SA Prod Corr: 0.4144
- SA Self Corr: 0.3964

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 19 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-12-07

连续回测的第247天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 63

#### 本赛季表现指标

- RA Count: 248
- RA Prod Corr: 0.6055
- RA Self Corr: 0.2434
- SA Count: 56
- SA Prod Corr: 0.5072
- SA Self Corr: 0.4227

#### 最近两周表现指标

- RA Count: 51
- RA Prod Corr: 0.6548
- RA Self Corr: 0.2549
- SA Count: 15
- SA Prod Corr: 0.4027
- SA Self Corr: 0.3302

#### 最近一周表现指标

- RA Count: 26
- RA Prod Corr: 0.6712
- RA Self Corr: 0.2583
- SA Count: 8
- SA Prod Corr: 0.3834
- SA Self Corr: 0.3620

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 20 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-12-08

连续回测的第248天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 63

#### 本赛季表现指标

- RA Count: 252
- RA Prod Corr: 0.6040
- RA Self Corr: 0.2419
- SA Count: 57
- SA Prod Corr: 0.5063
- SA Self Corr: 0.4232

#### 最近两周表现指标

- RA Count: 52
- RA Prod Corr: 0.6420
- RA Self Corr: 0.2513
- SA Count: 15
- SA Prod Corr: 0.3970
- SA Self Corr: 0.3366

#### 最近一周表现指标

- RA Count: 28
- RA Prod Corr: 0.6480
- RA Self Corr: 0.2378
- SA Count: 8
- SA Prod Corr: 0.3663
- SA Self Corr: 0.3442

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 21 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
- 2025-12-09
  连续回测的第249天
  今日提交：4个Regular Alpha，1个Super Alpha。
  本赛季Alpha覆盖金字塔类别总数: 63

#### 本赛季表现指标

- RA Count: 260
- RA Prod Corr: 0.6068
- RA Self Corr: 0.2422
- SA Count: 58
- SA Prod Corr: 0.5027
- SA Self Corr: 0.4196

#### 最近两周表现指标

- RA Count: 52
- RA Prod Corr: 0.6466
- RA Self Corr: 0.2575
- SA Count: 13
- SA Prod Corr: 0.3904
- SA Self Corr: 0.3548

#### 最近一周表现指标

- RA Count: 24
- RA Prod Corr: 0.6727
- RA Self Corr: 0.2598
- SA Count: 7
- SA Prod Corr: 0.3495
- SA Self Corr: 0.3126

- #========= WORLDQUANT BRAIN CONSULTANT ========== #
  # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
  # sys.setrecursionlimit(α∞)
  # PnL = ∑(Robustness * Creativity)
  #无限探索、鲁棒性优先，创新性增值
  #=================奋进的小徐=======================#


---

### 技术对话片段 22 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) ）因评论到达上限，已无法评论，特此展开第七季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
- 2025-12-10
  连续回测的第250天
  今日提交：4个Regular Alpha，1个Super Alpha。
  本赛季Alpha覆盖金字塔类别总数: 63
  #### 本赛季表现指标
  - RA Count: 264
  - RA Prod Corr: 0.6075
  - RA Self Corr: 0.2449
  - SA Count: 60
  - SA Prod Corr: 0.4991
  - SA Self Corr: 0.4165
  #### 最近两周表现指标
  - RA Count: 53
  - RA Prod Corr: 0.6452
  - RA Self Corr: 0.2672
  - SA Count: 14
  - SA Prod Corr: 0.3996
  - SA Self Corr: 0.3672
  #### 最近一周表现指标
  - RA Count: 27
  - RA Prod Corr: 0.6708
  - RA Self Corr: 0.2808
  - SA Count: 7
  - SA Prod Corr: 0.3663
  - SA Self Corr: 0.3118

- #========= WORLDQUANT BRAIN CONSULTANT ========== #
  # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
  # sys.setrecursionlimit(α∞)
  # PnL = ∑(Robustness * Creativity)
  #无限探索、鲁棒性优先，创新性增值
  #=================奋进的小徐=======================#


---

### 技术对话片段 23 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-10

连续回测的第189天

今日提交：2个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 11

#### 本赛季表现指标

- RA Count: 33
- RA Prod Corr: 0.6098
- RA Self Corr: 0.2945
- SA Count: 6
- SA Prod Corr: 0.6542
- SA Self Corr: 0.6512

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 24 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-11

连续回测的第190天

今日提交：3个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 13

#### 本赛季表现指标

- RA Count: 36
- RA Prod Corr: 0.6024
- RA Self Corr: 0.2862
- SA Count: 6
- SA Prod Corr: 0.6542
- SA Self Corr: 0.6512

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 25 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-12

连续回测的第191天

今日提交：3个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 14

#### 本赛季表现指标

- RA Count: 39
- RA Prod Corr: 0.6076
- RA Self Corr: 0.2837
- SA Count: 6
- SA Prod Corr: 0.6542
- SA Self Corr: 0.6512

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 26 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-12

连续回测的第192天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 15

#### 本赛季表现指标

#### 本赛季表现指标

- RA Count: 42
- RA Prod Corr: 0.6017
- RA Self Corr: 0.2729
- SA Count: 7
- SA Prod Corr: 0.6279
- SA Self Corr: 0.6254

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 27 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-14

连续回测的第194天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 16

#### 本赛季表现指标

- RA Count: 49
- RA Prod Corr: 0.6035
- RA Self Corr: 0.2627
- SA Count: 8
- SA Prod Corr: 0.6090
- SA Self Corr: 0.6061

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 28 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-16

连续回测的第196天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 16

#### 本赛季表现指标

- RA Count: 53
- RA Prod Corr: 0.6084
- RA Self Corr: 0.2575
- SA Count: 10
- SA Prod Corr: 0.6017
- SA Self Corr: 0.5974

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 29 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-19

连续回测的第198天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 21

#### 本赛季表现指标

- RA Count: 64
- RA Prod Corr: 0.5965
- RA Self Corr: 0.2449
- SA Count: 10
- SA Prod Corr: 0.6017
- SA Self Corr: 0.5974

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 30 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-20

连续回测的第199天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 22

#### 本赛季表现指标

- RA Count: 69
- RA Prod Corr: 0.6018
- RA Self Corr: 0.2502
- SA Count: 10
- SA Prod Corr: 0.6017
- SA Self Corr: 0.5974

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 31 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-21

连续回测的第200天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 23

#### 本赛季表现指标

- RA Count: 72
- RA Prod Corr: 0.6063
- RA Self Corr: 0.2467
- SA Count: 10
- SA Prod Corr: 0.6017
- SA Self Corr: 0.5974

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 32 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-22

连续回测的第201天

今日提交：3个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 26, 被系统吞了2个变成了24

#### 本赛季表现指标

- RA Count: 75
- RA Prod Corr: 0.6063
- RA Self Corr: 0.2478
- SA Count: 11
- SA Prod Corr: 0.5913
- SA Self Corr: 0.5825

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 33 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-23

连续回测的第202天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 26

#### 本赛季表现指标

- RA Count: 79
- RA Prod Corr: 0.6080
- RA Self Corr: 0.2433
- SA Count: 12
- SA Prod Corr: 0.5825
- SA Self Corr: 0.5744

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 34 (原帖: 【日常生活贴】我的量化日记第五季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **时间**: 8个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-10-26

连续回测的第205天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 28

#### 本赛季表现指标

- RA Count: 91
- RA Prod Corr: 0.6004
- RA Self Corr: 0.2171
- SA Count: 15
- SA Prod Corr: 0.5761
- SA Self Corr: 0.5690

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 35 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
- 2025-12-19
  连续回测的第259天
  今日提交：2个Regular Alpha，1个Super Alpha。
  本赛季Alpha覆盖金字塔类别总数: 63
- #### 本赛季表现指标
  - RA Count: 288
  - RA Prod Corr: 0.6067
  - RA Self Corr: 0.2449
  - SA Count: 62
  - SA Prod Corr: 0.4949
  - SA Self Corr: 0.4125
  #### 最近两周表现指标
  - RA Count: 57
  - RA Prod Corr: 0.6475
  - RA Self Corr: 0.2645
  - SA Count: 14
  - SA Prod Corr: 0.3819
  - SA Self Corr: 0.3429
  #### 最近一周表现指标
  - RA Count: 24
  - RA Prod Corr: 0.6196
  - RA Self Corr: 0.2605
  - SA Count: 6
  - SA Prod Corr: 0.3800
  - SA Self Corr: 0.3175

- #========= WORLDQUANT BRAIN CONSULTANT ========== #
  # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
  # sys.setrecursionlimit(α∞)
  # PnL = ∑(Robustness * Creativity)
  #无限探索、鲁棒性优先，创新性增值
  #=================奋进的小徐=======================#


---

### 技术对话片段 36 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
- 2025-12-20
  连续回测的第260天
  今日提交：2个Regular Alpha，1个Super Alpha。
  本赛季Alpha覆盖金字塔类别总数: 63
- #### 本赛季表现指标
  - RA Count: 290
  - RA Prod Corr: 0.6104
  - RA Self Corr: 0.2442
  - SA Count: 70
  - SA Prod Corr: 0.4817
  - SA Self Corr: 0.4040
  #### 最近两周表现指标
  - RA Count: 43
  - RA Prod Corr: 0.6467
  - RA Self Corr: 0.2519
  - SA Count: 14
  - SA Prod Corr: 0.3798
  - SA Self Corr: 0.3293
  #### 最近一周表现指标
  - RA Count: 19
  - RA Prod Corr: 0.6574
  - RA Self Corr: 0.2176
  - SA Count: 7
  - SA Prod Corr: 0.3696
  - SA Self Corr: 0.3223

- #========= WORLDQUANT BRAIN CONSULTANT ========== #
  # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
  # sys.setrecursionlimit(α∞)
  # PnL = ∑(Robustness * Creativity)
  #无限探索、鲁棒性优先，创新性增值
  #=================奋进的小徐=======================#


---

### 技术对话片段 37 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **时间**: 6 months ago

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
- 2025-12-21
  连续回测的第261天
  今日提交：4个Regular Alpha，1个Super Alpha。
  本赛季Alpha覆盖金字塔类别总数: 63
- #### 本赛季表现指标
  - RA Count: 294
  - RA Prod Corr: 0.6104
  - RA Self Corr: 0.2442
  - SA Count: 70
  - SA Prod Corr: 0.4817
  - SA Self Corr: 0.4040
  #### 最近两周表现指标
  - RA Count: 43
  - RA Prod Corr: 0.6467
  - RA Self Corr: 0.2519
  - SA Count: 14
  - SA Prod Corr: 0.3798
  - SA Self Corr: 0.3293
  #### 最近一周表现指标
  - RA Count: 19
  - RA Prod Corr: 0.6574
  - RA Self Corr: 0.2176
  - SA Count: 7
  - SA Prod Corr: 0.3696
  - SA Self Corr: 0.3223

- #========= WORLDQUANT BRAIN CONSULTANT ========== #
  # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
  # sys.setrecursionlimit(α∞)
  # PnL = ∑(Robustness * Creativity)
  #无限探索、鲁棒性优先，创新性增值
  #=================奋进的小徐=======================#


---

### 技术对话片段 38 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-11

连续回测的第221天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 43

#### 本赛季表现指标

- RA Count: 155
- RA Prod Corr: 0.5604
- RA Self Corr: 0.2137
- SA Count: 29
- SA Prod Corr: 0.5547
- SA Self Corr: 0.4845

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 39 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-12

连续回测的第222天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 44

#### 本赛季表现指标

- RA Count: 159
- RA Prod Corr: 0.5759
- RA Self Corr: 0.2257
- SA Count: 31
- SA Prod Corr: 0.5528
- SA Self Corr: 0.4877

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 40 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-13

连续回测的第223天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 45

#### 本赛季表现指标

- RA Count: 163
- RA Prod Corr: 0.5767
- RA Self Corr: 0.2270
- SA Count: 32
- SA Prod Corr: 0.5556
- SA Self Corr: 0.4898

#### 最近两周表现指标

- RA Count: 56
- RA Prod Corr: 0.5975
- RA Self Corr: 0.2728
- SA Count: 13
- SA Prod Corr: 0.5435
- SA Self Corr: 0.4488

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 41 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-14

连续回测的第224天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 47

#### 本赛季表现指标

- RA Count: 167
- RA Prod Corr: 0.5786
- RA Self Corr: 0.2322
- SA Count: 33
- SA Prod Corr: 0.5533
- SA Self Corr: 0.4878

#### 最近两周表现指标

- RA Count: 56
- RA Prod Corr: 0.6322
- RA Self Corr: 0.3002
- SA Count: 13
- SA Prod Corr: 0.5537
- SA Self Corr: 0.4664

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 42 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-15

连续回测的第225天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 48

#### 本赛季表现指标

- RA Count: 171
- RA Prod Corr: 0.5840
- RA Self Corr: 0.2330
- SA Count: 34
- SA Prod Corr: 0.5554
- SA Self Corr: 0.4829

#### 最近两周表现指标

- RA Count: 53
- RA Prod Corr: 0.6536
- RA Self Corr: 0.3072
- SA Count: 12
- SA Prod Corr: 0.5638
- SA Self Corr: 0.4804

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 43 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-16

连续回测的第226天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 49

#### 本赛季表现指标

- RA Count: 175
- RA Prod Corr: 0.5859
- RA Self Corr: 0.2371
- SA Count: 35
- SA Prod Corr: 0.5533
- SA Self Corr: 0.4768

#### 最近两周表现指标

- RA Count: 56
- RA Prod Corr: 0.6558
- RA Self Corr: 0.3161
- SA Count: 13
- SA Prod Corr: 0.5576
- SA Self Corr: 0.4641

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 44 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-17

连续回测的第227天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 49

#### 本赛季表现指标

- RA Count: 179
- RA Prod Corr: 0.5876
- RA Self Corr: 0.2398
- SA Count: 36
- SA Prod Corr: 0.5536
- SA Self Corr: 0.4698

#### 最近两周表现指标

- RA Count: 56
- RA Prod Corr: 0.6721
- RA Self Corr: 0.3291
- SA Count: 13
- SA Prod Corr: 0.5499
- SA Self Corr: 0.4435

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 45 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-18

连续回测的第228天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 50

#### 本赛季表现指标

- RA Count: 183
- RA Prod Corr: 0.5876
- RA Self Corr: 0.2398
- SA Count: 36
- SA Prod Corr: 0.5536
- SA Self Corr: 0.4698

#### 最近两周表现指标

- RA Count: 57
- RA Prod Corr: 0.6721
- RA Self Corr: 0.3291
- SA Count: 13
- SA Prod Corr: 0.5499
- SA Self Corr: 0.4435

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 46 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-20

连续回测的第230天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 51

#### 本赛季表现指标

- RA Count: 191
- RA Prod Corr: 0.5876
- RA Self Corr: 0.2398
- SA Count: 36
- SA Prod Corr: 0.5536
- SA Self Corr: 0.4698

#### 最近两周表现指标

- RA Count: 57
- RA Prod Corr: 0.6721
- RA Self Corr: 0.3291
- SA Count: 13
- SA Prod Corr: 0.5499
- SA Self Corr: 0.4435

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 47 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-21

连续回测的第231天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 52

#### 本赛季表现指标

- RA Count: 195
- RA Prod Corr: 0.5955
- RA Self Corr: 0.2415
- SA Count: 39
- SA Prod Corr: 0.5483
- SA Self Corr: 0.4638

#### 最近两周表现指标

- RA Count: 56
- RA Prod Corr: 0.6996
- RA Self Corr: 0.3291
- SA Count: 13
- SA Prod Corr: 0.5455
- SA Self Corr: 0.4360

#### 最近一周表现指标

- RA Count: 28
- RA Prod Corr: 0.6962
- RA Self Corr: 0.2973
- SA Count: 7
- SA Prod Corr: 0.5152
- SA Self Corr: 0.3451

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 48 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-22

连续回测的第232天

今日提交：1个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 52

#### 本赛季表现指标

- RA Count: 196
- RA Prod Corr: 0.5955
- RA Self Corr: 0.2415
- SA Count: 39
- SA Prod Corr: 0.5483
- SA Self Corr: 0.4638

#### 最近两周表现指标

- RA Count: 56
- RA Prod Corr: 0.6996
- RA Self Corr: 0.3291
- SA Count: 13
- SA Prod Corr: 0.5455
- SA Self Corr: 0.4360

#### 最近一周表现指标

- RA Count: 28
- RA Prod Corr: 0.6962
- RA Self Corr: 0.2973
- SA Count: 7
- SA Prod Corr: 0.5152
- SA Self Corr: 0.3451

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 49 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **时间**: 7个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-11-23

连续回测的第233天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 54

#### 本赛季表现指标

- RA Count: 201
- RA Prod Corr: 0.5942
- RA Self Corr: 0.2394
- SA Count: 42
- SA Prod Corr: 0.5453
- SA Self Corr: 0.4541

#### 最近两周表现指标

- RA Count: 54
- RA Prod Corr: 0.6863
- RA Self Corr: 0.3095
- SA Count: 14
- SA Prod Corr: 0.5337
- SA Self Corr: 0.4037

#### 最近一周表现指标

- RA Count: 26
- RA Prod Corr: 0.6502
- RA Self Corr: 0.2547
- SA Count: 7
- SA Prod Corr: 0.5052
- SA Self Corr: 0.3409

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 50 (原帖: 拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **时间**: 3个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第五季_35580578002327.md) + [【日常生活贴】我的量化日记第六季]([Commented] 【日常生活贴】我的量化日记第六季_36251528053527.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md) + [【日常生活贴】我的量化日记第九季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第九季_37796479641111.md) ）因评论到达上限，已无法评论，特此展开第十季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
- 2026-03-05, GM已达标
  连续回测的第335天
  今日提交：4个Regular Alpha，1个Super Alpha。
  本赛季Alpha覆盖金字塔类别总数: 60
- #### 本赛季表现指标
  - RA Count: 208
  - RA Prod Corr: 0.5840
  - RA Self Corr: 0.3079
  - SA Count: 60
  - SA Prod Corr: 0.5239
  - SA Self Corr: 0.4918
  #### 最近两周表现指标
  - RA Count: 49
  - RA Prod Corr: 0.6044
  - RA Self Corr: 0.3257
  - SA Count: 13
  - SA Prod Corr: 0.5626
  - SA Self Corr: 0.5075
  #### 最近一周表现指标
  - RA Count: 23
  - RA Prod Corr: 0.6357
  - RA Self Corr: 0.3872
  - SA Count: 6
  - SA Prod Corr: 0.5542
  - SA Self Corr: 0.5309

- #========= WORLDQUANT BRAIN CONSULTANT ========== #
  # Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
  # sys.setrecursionlimit(α∞)
  # PnL = ∑(Robustness * Creativity)
  #无限探索、鲁棒性优先，创新性增值
  #=================奋进的小徐=======================#


---

### 技术对话片段 51 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025年9月16日

连续回测的第166天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季 (7-9月) Alpha覆盖金字塔类别总数: 46

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 52 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-17

连续回测的第167天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 49

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 53 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-18

连续回测的第168天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季 (2025-07-01 - 2025-09-18) Alpha覆盖金字塔类别总数: 50

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 54 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-19

连续回测的第169天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季 (2025-07-01 - 2025-09-19) Alpha覆盖金字塔类别总数: 52

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 55 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025年9月20日

连续回测的第170天

今日提交：3个Regular Alpha，0个Super Alpha。

本赛季 (7-9月) Alpha覆盖金字塔类别总数: 53

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 56 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-24

连续回测的第174天

今日提交：3个Regular Alpha，1个Super Alpha。

本赛季 (07-09月) Alpha覆盖金字塔类别总数: 58


---

### 技术对话片段 57 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-25

连续回测的第175天

今日提交：2个Regular Alpha，1个Super Alpha。

本赛季 (07-09月) Alpha覆盖金字塔类别总数: 59


---

### 技术对话片段 58 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: [Commented] 【日常生活贴】我的量化日记第四季.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-26

连续回测的第176天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季 (07-09月) Alpha覆盖金字塔类别总数: 60


---

### 技术对话片段 59 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025年9月16日

连续回测的第166天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季 (7-9月) Alpha覆盖金字塔类别总数: 46

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 60 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-17

连续回测的第167天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季Alpha覆盖金字塔类别总数: 49

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 61 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-18

连续回测的第168天

今日提交：4个Regular Alpha，0个Super Alpha。

本赛季 (2025-07-01 - 2025-09-18) Alpha覆盖金字塔类别总数: 50

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 62 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-19

连续回测的第169天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季 (2025-07-01 - 2025-09-19) Alpha覆盖金字塔类别总数: 52

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 63 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025年9月20日

连续回测的第170天

今日提交：3个Regular Alpha，0个Super Alpha。

本赛季 (7-9月) Alpha覆盖金字塔类别总数: 53

#========= WORLDQUANT BRAIN CONSULTANT ========== #

# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%

# sys.setrecursionlimit(α∞)

# PnL = ∑(Robustness * Creativity)

#无限探索、鲁棒性优先，创新性增值

#=================奋进的小徐=======================#


---

### 技术对话片段 64 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-24

连续回测的第174天

今日提交：3个Regular Alpha，1个Super Alpha。

本赛季 (07-09月) Alpha覆盖金字塔类别总数: 58


---

### 技术对话片段 65 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-25

连续回测的第175天

今日提交：2个Regular Alpha，1个Super Alpha。

本赛季 (07-09月) Alpha覆盖金字塔类别总数: 59


---

### 技术对话片段 66 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **时间**: 9个月前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 JX79797 (Rank 9) 的解答与建议**:
2025-09-26

连续回测的第176天

今日提交：4个Regular Alpha，1个Super Alpha。

本赛季 (07-09月) Alpha覆盖金字塔类别总数: 60


---

### 技术对话片段 67 (原帖: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享)
- **原帖链接**: [Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享.md
- **时间**: 9个月前

**提问/主帖背景 (ML47973)**:

> [!NOTE] [图片 OCR 识别内容]
> 华子哥 Genius Jank 插件安装和使用教程^
> 首先感谢华子哥开发并开源 Genius Rank 分析插件如此强大的工具!也
> 感谢课代表 XX42289提供的分析代码以及量化小组群友们的贡献。下面是一个详
> 细的安装和使用说明教程,帮助新顾问和社区用户不会安装插件和使用的快速上
> 手:
              Genius Rank 帖子： [【插件】Genius Rank分析 – WorldQuant BRAIN](../顾问 JL71699 (Rank 64)/[Commented] 【插件】Genius Rank分析代码优化.md) 
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


**顾问 JX79797 (Rank 9) 的解答与建议**:
@ [YH47265](/hc/zh-cn/profiles/31706852029335-YH47265)     不可能发生这种情况的，很多人习惯性赛季末发力。 假如这不够就是m增多  m+gm 10%

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 68 (原帖: 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享)
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


**顾问 JX79797 (Rank 9) 的解答与建议**:
@ [YH47265](/hc/zh-cn/profiles/31706852029335-YH47265)     不可能发生这种情况的，很多人习惯性赛季末发力。 假如这不够就是m增多  m+gm 10%

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 69 (原帖: 做了一个开源工作流控制面板)
- **原帖链接**: [Commented] 做了一个开源工作流控制面板.md
- **时间**: 9个月前

**提问/主帖背景 (XC96000)**:
大家好，这里e.e.，

初来社区，请各位大佬多多关照。

最近在社区也是看到很多优秀的check方案，但看大家用的都比较保守，于是吸取大家的优秀方案，写了一个交互式的工具，此工具包含：

1. 可视化的操作界面
2. 独立的会话管理，用最少的认证请求保持会话畅通
3. 独立的check方案，无人值守自动完成RA，PPAC因子相关性检测
4. 自动检测新提交因子，并重新检查剩余可提交因子相关性

相关性检查参考文章： [本地0误差计算自相关性-即插即用版](../顾问 KZ79256 (Rank 21)/本地0误差计算自相关性【即插即用版】代码优化.md)

会话管理参考文章： [【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎](../顾问 SD17531 (Rank 15)/[Commented] 【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎.md)

更多内容可以直接查看GitHub上的开源项目： [WQOS]([链接已屏蔽])

以下是工具的一些预览：


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant Alpha 挖掘控制面板
> 欢迎;
> ee
> 控制面板
> 配置管理
> 世 Alpha 状态查看
> 进程管理
> 查看可提交Alpha的状态和相关性检测结果
> 山
> Alpha状态
> 总计
> 普通因子
> PPAC因子
> 待检测因子
> 世370
> 076
> 8294
> 00
> 待检测因子
> 普通因子
> 70
> PPAC因孑
> 294
> 筛选条件:
> 显示激进因子:
> (己隐藏102  个激进因子)
> 标签筛选:
> 选择标签进行筛选
> 重置筛选
> Alpha ID
> 标签
> Fitness
> Sharpe
> Power Pool Correlation
> JaGejgp
> USA_I_EQUITY_TOP3OOO_analystl
> stepl
> 1.660
> 1.090
> 0.0673
> RORbOXO
> USA_I_EQUITY_TOP3OOO_sentimentl_stepl
> 1.580
> 1.260
> 0.1385
> jdj
> USA_I_EQUITY_TOP3OOO_analystl
> stepl
> 1.490
> 1.300
> 0.0707
> W2l让
> fundamentalG_usa_2step
> 1.030
> 1.070
> 0.3108
> 88089e7
> fundamentalG
> UI53
> 2step
> 0.960
> 1.030
> 0.3177
> AXangye
> analystl4_eur_Istep
> 0.920
> 1.650
> 0.1455
> OLKLdVI
> 0.910
> 1.580
> 0.2619
  
> [!NOTE] [图片 OCR 识别内容]
> I
> WorldQuant Alpha 挖掘控制面板
> 欢迎;
> Ce
> 控制面板
> 相关性检查器
> 脚本运行中
> 刷新已停止
> 26,224行
> 实时模式
> 实时模式
> 8自动
> C 刷新
> 日志
> 配置管理
> 进程管理 
> 2025-09-06 21:5:08
> Sharpe:
> 1.040
> (需要
> 1.58)
> FitIless:
> 0.440
> (需要
> 1.0)
> PPAC:
> 0.0197
> 0.5
> 进程管理
> 统
> -管理所有脚本的启动。停止和监控
> 2025-09-06  21:55:08
> 检耷Alpha T7AVnJx
> 2025-09-06 21:5:08
> AIpla指标:
> Sharpe=l. 000,
> Fitness=0.410,
> Operators=3
> 2025-09-06
> 21:5;08
> 检测策略:  需要PP4C检查=True, 需要普通检耷-False
> 山
> Alpha状态
> 2025-09-06 21:5:08
> Alpha T7AVaJx: 不满足普通检测条件。仅通过PPAC
> BLLE
> 脚本管理
> 2025-09-06
> 21:55:08
> Sharpe:
> 1.000
> (需要>1.58)
> FitIess:
> 0.410 X
> (需要
> 1.0)
> PPAC:
> 0.0227
> 0.5
> 2025-09-06 21:5:08
> 检查4lpha Gjd9o
> 2025-09-06
> 21:55:08
> Alpha指标:
> Sharpe=l. 000,
> Fitness=0. 430,
> Operators=s
> 2025-09-06 21:5:08
> 检测策略:  需要PP4C检查-Irue;
> 需要普通检查-Fals2
> 脚本名称
> 状态
> 迸程ID
> 启动时间
> 停止
> 2025-09-06
> 21:55;08
> Alpha GjVAKgo: 不满足普通检测条件,
> 仅通过PPAC
> BLUE
> 2025-09-06 21:5:08
> Sharpe:
> 1.000
> (需要
> 1.58)
> FitIless:
> 0.430
> (需要
> 1.0)
> PPAC:
> 0.2265
> 0.5
> 因子挖掘
> stepl
> 运行中
> 6568
> 2025/9/620:28:41 
> 2025-09-06
> 21:55:08
> 批次结果处理_
> 2025-09-06 21:5:08
> GREEN: 0 |
> BLIE: 18
> RED: 0 |
> PURPLE:
> 2025-09-06
> 21:55:08
> 更新  18 个4lpha的祖关性数值。
> 因子挖掘
> stepz
> 运行中
> 4888
> 2025/9/618:09:43
> 2025-09-06 21:5:08
> 成功更新  18  个4lpha的祖关性数值
> 2025-09-06
> 21:5;08
> 标记 18  个Alpha为BLCE.
> 2025-09-06 21:5:08
> 开始批量设置 18  个4lpha为BL[E。
> 相关性检查器
> 运行中
> 103
> 2025/9/611.52.33
> 2025-09-06  21:55:10
> BL[E 标记完成:  成功18,
> 失败 0
> 2025-09-06 21:5:10
> 批次 1:  成功设置 18 个Alpha
> 2025-09-06
> 21:5;10
> 凹
> 数据库更新完成:  18  个4lpla设为BLCE
> Alpha检查器 
> 运行中
> 95
> 2025/9/611.52.27
> 2025-09-06 21:5:10
> 祖关性检查统计:
> 会话保持器
> 运行中
> 27
> 2025/9/611.51.36 
> 2025-09-06 21:5:10
> 总检耷: 419 个4lpla
> 2025-09-06
> 21:5;10
> GREEN: 76 个
> (18。19)
> 通过普通裣查
> 2025-09-06 21:5:10
> BLUE: 294个 (70.29)
> 仅通过P4C检查
> 2025-09-06  21:55:10
> RD:
> 49
> (11.79)
> 未通过裣查
> 2025-09-06 21:5:10
> PURPLE:
> 个 (0.09)
> 厂字型Alpla
> 2025-09-06  21:55:10
> AGGRESSITE: 178 个
> 激进馍式AIpha (早期为0,近期强势上涨)
> 2025-09-06 21:5:10
> 保留率:  88.39
> 2025-09-06 21:55:10
> 移除率:  11.79
> 2025-09-06 21:5:10
> 清理P 缓存:  移除  50 个末通过检测的41p1a,
> 保留  370  个
> 2025-09-06
> 21:55:11
> 本轮检查完成:  419个4101a处理完毕
> 2025-09-06
> 21:55:11
> 笫 120  轮检查完成,
> 有41pha被处理
> 2025-09-06 21:5:11
> 检耷周期完成。耗时:  136.8Gs, 163.14秒后开始下轮检耷
> 2025-09-06  21:55:11
> 提示:  按 CtzltC 可停止监控
> TIO


**顾问 JX79797 (Rank 9) 的解答与建议**:
正在构思，写了一些方案，感觉部分还是可以高复用的，下载下来玩一玩，看看能不能直接在这个基础上去完善。 多谢🙏

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 70 (原帖: 做了一个开源工作流控制面板)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 做了一个开源工作流控制面板_34750579992087.md
- **时间**: 9个月前

**提问/主帖背景 (XC96000)**:
大家好，这里e.e.，

初来社区，请各位大佬多多关照。

最近在社区也是看到很多优秀的check方案，但看大家用的都比较保守，于是吸取大家的优秀方案，写了一个交互式的工具，此工具包含：

1. 可视化的操作界面
2. 独立的会话管理，用最少的认证请求保持会话畅通
3. 独立的check方案，无人值守自动完成RA，PPAC因子相关性检测
4. 自动检测新提交因子，并重新检查剩余可提交因子相关性

相关性检查参考文章： [本地0误差计算自相关性-即插即用版]([L2] 本地0误差计算自相关性【即插即用版】代码优化_31343962309143.md)

会话管理参考文章： [【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎]([L2] 【设计思路分享】在Linux云服务器打造不停机的alpha运行引擎_28268813242647.md)

更多内容可以直接查看GitHub上的开源项目： [WQOS]([链接已屏蔽])

以下是工具的一些预览：


> [!NOTE] [图片 OCR 识别内容]
> WorldQuant Alpha 挖掘控制面板
> 欢迎;
> ee
> 控制面板
> 配置管理
> 世 Alpha 状态查看
> 进程管理
> 查看可提交Alpha的状态和相关性检测结果
> 山
> Alpha状态
> 总计
> 普通因子
> PPAC因子
> 待检测因子
> 世370
> 076
> 8294
> 00
> 待检测因子
> 普通因子
> 70
> PPAC因孑
> 294
> 筛选条件:
> 显示激进因子:
> (己隐藏102  个激进因子)
> 标签筛选:
> 选择标签进行筛选
> 重置筛选
> Alpha ID
> 标签
> Fitness
> Sharpe
> Power Pool Correlation
> JaGejgp
> USA_I_EQUITY_TOP3OOO_analystl
> stepl
> 1.660
> 1.090
> 0.0673
> RORbOXO
> USA_I_EQUITY_TOP3OOO_sentimentl_stepl
> 1.580
> 1.260
> 0.1385
> jdj
> USA_I_EQUITY_TOP3OOO_analystl
> stepl
> 1.490
> 1.300
> 0.0707
> W2l让
> fundamentalG_usa_2step
> 1.030
> 1.070
> 0.3108
> 88089e7
> fundamentalG
> UI53
> 2step
> 0.960
> 1.030
> 0.3177
> AXangye
> analystl4_eur_Istep
> 0.920
> 1.650
> 0.1455
> OLKLdVI
> 0.910
> 1.580
> 0.2619
  
> [!NOTE] [图片 OCR 识别内容]
> I
> WorldQuant Alpha 挖掘控制面板
> 欢迎;
> Ce
> 控制面板
> 相关性检查器
> 脚本运行中
> 刷新已停止
> 26,224行
> 实时模式
> 实时模式
> 8自动
> C 刷新
> 日志
> 配置管理
> 进程管理 
> 2025-09-06 21:5:08
> Sharpe:
> 1.040
> (需要
> 1.58)
> FitIless:
> 0.440
> (需要
> 1.0)
> PPAC:
> 0.0197
> 0.5
> 进程管理
> 统
> -管理所有脚本的启动。停止和监控
> 2025-09-06  21:55:08
> 检耷Alpha T7AVnJx
> 2025-09-06 21:5:08
> AIpla指标:
> Sharpe=l. 000,
> Fitness=0.410,
> Operators=3
> 2025-09-06
> 21:5;08
> 检测策略:  需要PP4C检查=True, 需要普通检耷-False
> 山
> Alpha状态
> 2025-09-06 21:5:08
> Alpha T7AVaJx: 不满足普通检测条件。仅通过PPAC
> BLLE
> 脚本管理
> 2025-09-06
> 21:55:08
> Sharpe:
> 1.000
> (需要>1.58)
> FitIess:
> 0.410 X
> (需要
> 1.0)
> PPAC:
> 0.0227
> 0.5
> 2025-09-06 21:5:08
> 检查4lpha Gjd9o
> 2025-09-06
> 21:55:08
> Alpha指标:
> Sharpe=l. 000,
> Fitness=0. 430,
> Operators=s
> 2025-09-06 21:5:08
> 检测策略:  需要PP4C检查-Irue;
> 需要普通检查-Fals2
> 脚本名称
> 状态
> 迸程ID
> 启动时间
> 停止
> 2025-09-06
> 21:55;08
> Alpha GjVAKgo: 不满足普通检测条件,
> 仅通过PPAC
> BLUE
> 2025-09-06 21:5:08
> Sharpe:
> 1.000
> (需要
> 1.58)
> FitIless:
> 0.430
> (需要
> 1.0)
> PPAC:
> 0.2265
> 0.5
> 因子挖掘
> stepl
> 运行中
> 6568
> 2025/9/620:28:41 
> 2025-09-06
> 21:55:08
> 批次结果处理_
> 2025-09-06 21:5:08
> GREEN: 0 |
> BLIE: 18
> RED: 0 |
> PURPLE:
> 2025-09-06
> 21:55:08
> 更新  18 个4lpha的祖关性数值。
> 因子挖掘
> stepz
> 运行中
> 4888
> 2025/9/618:09:43
> 2025-09-06 21:5:08
> 成功更新  18  个4lpha的祖关性数值
> 2025-09-06
> 21:5;08
> 标记 18  个Alpha为BLCE.
> 2025-09-06 21:5:08
> 开始批量设置 18  个4lpha为BL[E。
> 相关性检查器
> 运行中
> 103
> 2025/9/611.52.33
> 2025-09-06  21:55:10
> BL[E 标记完成:  成功18,
> 失败 0
> 2025-09-06 21:5:10
> 批次 1:  成功设置 18 个Alpha
> 2025-09-06
> 21:5;10
> 凹
> 数据库更新完成:  18  个4lpla设为BLCE
> Alpha检查器 
> 运行中
> 95
> 2025/9/611.52.27
> 2025-09-06 21:5:10
> 祖关性检查统计:
> 会话保持器
> 运行中
> 27
> 2025/9/611.51.36 
> 2025-09-06 21:5:10
> 总检耷: 419 个4lpla
> 2025-09-06
> 21:5;10
> GREEN: 76 个
> (18。19)
> 通过普通裣查
> 2025-09-06 21:5:10
> BLUE: 294个 (70.29)
> 仅通过P4C检查
> 2025-09-06  21:55:10
> RD:
> 49
> (11.79)
> 未通过裣查
> 2025-09-06 21:5:10
> PURPLE:
> 个 (0.09)
> 厂字型Alpla
> 2025-09-06  21:55:10
> AGGRESSITE: 178 个
> 激进馍式AIpha (早期为0,近期强势上涨)
> 2025-09-06 21:5:10
> 保留率:  88.39
> 2025-09-06 21:55:10
> 移除率:  11.79
> 2025-09-06 21:5:10
> 清理P 缓存:  移除  50 个末通过检测的41p1a,
> 保留  370  个
> 2025-09-06
> 21:55:11
> 本轮检查完成:  419个4101a处理完毕
> 2025-09-06
> 21:55:11
> 笫 120  轮检查完成,
> 有41pha被处理
> 2025-09-06 21:5:11
> 检耷周期完成。耗时:  136.8Gs, 163.14秒后开始下轮检耷
> 2025-09-06  21:55:11
> 提示:  按 CtzltC 可停止监控
> TIO


**顾问 JX79797 (Rank 9) 的解答与建议**:
正在构思，写了一些方案，感觉部分还是可以高复用的，下载下来玩一玩，看看能不能直接在这个基础上去完善。 多谢🙏

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 71 (原帖: 全局变量保存调度器实例_scheduler = Nonedef start_scheduler():    global _scheduler    避免在 reloader 进程中启动调度器，避免启动两次    if os.environ.get('RUN_MAIN') == 'true':        print("This is the reloader process. Scheduler not started.")        return    if _scheduler is not None:        print("Scheduler already running.")        return    _scheduler = BackgroundScheduler()    from app01.utils.util_funcs import count_perHour    每小时整点运行一次任务    _scheduler.add_job(        count_perHour,        'cron',        minute=0  整点执行    )    _scheduler.start()    print("Scheduler started and will run every hour at :00"))
- **原帖链接**: [Commented] 打造自己的BrainAdmin用手机也能管理回测代码运行经验分享.md
- **时间**: 0年前

**提问/主帖背景 (HW93328)**:
# 1.前言

想要制作这个BrainAdmin的原因：1.登录云服务器非常卡（可能是配置低的原因），每次想查看代码运行情况都要被硬控好久。2.在手边没有电脑或者懒得打开电脑的场景下，通过ipad/手机就可以对模板的回测运行进行管理，非常灵活方便。3.将其他一些功能代码集成到系统中，方便使用和管理。

接下来会对系统功能进行逐一介绍，我最看重的还是在ipad和手机上也能进行操作，在没有电脑的场景下还是非常方便的。

ipad端


> [!NOTE] [图片 OCR 识别内容]
> 18:55
> 7月14日周
> 0100%
> L7BrainAdmin
> KAnderson
> 运行日志查看
> 在下方输入要查看的L08文件名称 (ex:tmpz)
> 日志信息已成功获取
> 日志名称
> 请输入日志名称
> 提交
> 日志内容
> tmpz.log
> 总行数:  3476行
> 当前展示:
> 1000 行 (仅展示最新1000行)
> Simulating for alpha:
> LL2 region: USA,
> universe: TOP3OO0, decay: 3,
> 1
> Simulating for alpha:
> region: USA, universe: TOP3000, decay: 3, delay:
> Alpha 7IkLX3L properties updated successfully!
> Alpha GgqW3XQ properties updated successfully!
> _
> simulation_progress_url: https:/lapi.worldquantbrain.com/simulationsl
> Alpha L3PMXra properties updated successfully!
> Alpha gLYeoGQ properties updated successfully!
> simulation_progress_url completed! https:Ilapi.worldquantbrain.comlsimulations;
> Alpha 7IkLXrO properties updated successfully!
> Ih3 LOVNIL OI nrnnortioc IInrltor
> CIICCOCCfIIIIII
>  3C'
> delay:
> Tag:
> Tag:
> 1-_
> Tag:
> Tag:
> Tag:


手机端


> [!NOTE] [图片 OCR 识别内容]
> 18:54
> 0
> 三
> template2
> Region
> Universe
> dataset
> njobs
> template_name
> Password
> 开启
> 停止
> 正在运行


整个系统看起来还是比较粗糙的，毕竟是自用嘛，很多细节上都是本着能用就行的程度哈哈哈，也希望有开发经验的大佬能够提出指点（手动抱拳~）

# 2.模板回测管理功能介绍

首先来介绍构建这个系统的初衷，用来管理回测代码运行的部分，接下来的展示为了方便都以PC网页为例。

整个模板管理页面可以分为三个部分：


> [!NOTE] [图片 OCR 识别内容]
> LTBrainAdmin
> Search
> K Anderson
> 品  主页
> 模板管理
> Home
> 模板管理
> 冒  实用工具
> templatez
> step2
> alpha提交
> Region
> Universe
> dataset
> stepl_name
> alpha Check
> USA
> TOP3000
> maCro4
> PAGES
> 模板运行管理
> njobs
> njobs
> 模板曰志查询
> template_name
> template_name
> 已提交列表
> tmp2
> Password
> 开启
> 停止
> 未运行
> 开启
> 停止
> 正在运行
> 回测数量(每小时统计)
> template8
> 1200
> Region
> Universe
> 1,000
> 800
> Catasetl
> datasetz
> 600
> 400
> njobs
> 200
> 27,00
> 22.00
> 11.02
> 15.00
> 16.00
> 20.59
> 2100
> template_name
> Password
> 模板信息
> 开启
> 停止
> 未运行
> 讨
> template_
> hame
> status
> description
> tmp2
> tmp8
> templateg
> step2
> [TT
> !
>  | + +


①.左侧一列是模板启动/关闭 管理面板

启动模板进行回测：在表单中填入Region、Universe、dataset等参数，点击开启，该回测程序就会在后端启动起来，当然这里需要填入的参数也因程序和模板的不同而需因人而异。

后端启动回测程序的代码如下：

```
# 每次运行前清空日志with open('tmp2.log', 'w') as f:    pass  # 启动一个子进程运行回测程序，并且传入所需参数process = subprocess.Popen(['python', 'templates2.py', region, universe, dataset, njobs],stdout=open('tmp2.log','a'), stderr=subprocess.STDOUT)print(f"PID of tmp2: {process.pid}")# 保存该程序对应的进程template_processes['tmp2'] = process# 更新Template表中的状态Template.objects.filter(template_name=template_name).update(status=1)
```

点击停止，后端会根据找到对应的子进程关闭，并发送关闭成功的通知


> [!NOTE] [图片 OCR 识别内容]
> WxPusher消息推送平台
> 来源: Wqb提醒
> 时间:
> 2025-07-1416.38.38
> 链接:
> 怠击查看
> tmp2 已暂停


推送信息相关的代码在论坛中也有大佬分享过，有兴趣可以搜索一下~

②.模板状态信息

这个数据表中保存了所有模板的信息，方便确认当前模板的运行状态

③.统计每小时的回测数量

在这个系统中设置了一个定时任务，每到整点时就触发函数获取上一个小时的回测数量，若是连续三个小时的回测数量都是0，则会发送通知警告回测数量的异常（时间宝贵！）

获取数量的代码之后放在评论区中。

模板日志查看功能：

该功能可以方便通过网页随时查看回测程序的运行情况


> [!NOTE] [图片 OCR 识别内容]
> 18:55
> 7月14日周
> 0100%
> L7BrainAdmin
> KAnderson
> 运行日志查看
> 在下方输入要查看的L08文件名称 (ex:tmpz)
> 日志信息已成功获取
> 日志名称
> 请输入日志名称
> 提交
> 日志内容
> tmpz.log
> 总行数:  3476行
> 当前展示:
> 1000 行 (仅展示最新1000行)
> Simulating for alpha:
> LL2 region: USA,
> universe: TOP3OO0, decay: 3,
> 1
> Simulating for alpha:
> region: USA, universe: TOP3000, decay: 3, delay:
> Alpha 7IkLX3L properties updated successfully!
> Alpha GgqW3XQ properties updated successfully!
> _
> simulation_progress_url: https:/lapi.worldquantbrain.com/simulationsl
> Alpha L3PMXra properties updated successfully!
> Alpha gLYeoGQ properties updated successfully!
> simulation_progress_url completed! https:Ilapi.worldquantbrain.comlsimulations;
> Alpha 7IkLXrO properties updated successfully!
> Ih3 LOVNIL OI nrnnortioc IInrltor
> CIICCOCCfIIIIII
>  3C'
> delay:
> Tag:
> Tag:
> 1-_
> Tag:
> Tag:
> Tag:


# 3.其他功能介绍

一、输入alpha_id 就可以进行提交alpha，省去在网页上等待的时间~


> [!NOTE] [图片 OCR 识别内容]
> BrainAdmin
> Search
> 器  主页
> alpha提交
> Home
> alpha提交
> 实用工具
> alpha 提交
> alpha提交
> 在下方输入alpha_id进行alpha的提交~
> alpha Check
> Alpha ID
> PAGES
> 请输入 alpha_id
> 模板运行管理
> 模板日志查询
> 提交
> 已提交列表


二、在这个系统中我获取了已提交因子，将其信息放在表中方便进行数据分析。当然也可以再做一个表格，获取一些满足条件的unsubmitted 因子，方便进行筛选。


> [!NOTE] [图片 OCR 识别内容]
> LTBrainAdmin
> Search
> K.Anderson
> 器  主页
> Data Tables
> Home
> Tables
> Submitted alphas Data
> 实用工具
> 已提交alpha数据列表
> PAGES
> 模板运行管理
> 刷新数据
> 模板日志查询
> 10
> entries per page
> Search。
> 已提交列表
> alpha_id
> date_submitted
> Code
> region
> universe
> neutralization
> sharpe
> fitness
> returns
> turnover
> margin
> Ops_counts
> self_cor
> prod_cor
> pyramid
> AzXk
> June 29,2025,
> GLB
> MINVOLIM
> SUBINDUSTRY
> 1.27
> 1.28
> 0.1263
> 0.0143
> 0.017721
> 3
> 0.4226
> 0.5598
> GLB/DI/FUNDAMENTAL
> 1:12pm。
> VzaC
> June 28,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.58
> 0.97
> 0.0467
> 085
> 0.001098
> 0.2347
> 0.
> .4222
> GLB/DI/FUNDAMENTAL
> 11:07a.m。
> LZNN -
> July 1,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.65
> 1.29
> 0.1177
> 0.1926
> 0.001222
> 3
> .9965
> 0.9965
> GLB/DI/FUNDAMENTAL
> 11:05am.
> SGb匕
> June 28,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.65
> 1.31
> 0.1175
> 0.
> 1853
> 0.
> 001267
> 0.2216
> 0.5679
> GLB/DI/FUNDAMENTAL
> 10:30a.m.
> 3PXg:
> June 30,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.44
> 1.32
> 0.2133
> 0.2535
> 0.001683
> 0.5823
> 0.5823
> GLB/DI/FUNDAMENTAL
> 9:27a.m。
> 10
> 3PRA
> June 27,2025,
> EUR
> TOP2500
> REVERSION_AND_MOMENTUM
> 2.26
> 1.63
> 0.0714
> 0.1367
> 0.001045
> 3
> 0.4927
> 0.8199
> EURIDIIMODEL
> 8:22a.m.
> 11
> OZF
> June 26,2025,
> USA
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.49
> 0.95
> 0.0511
> 0.0585
> 0.001747
> 3
> 0.4687
> 0.9995
> USAIDIIMODEL
> 10:09a.m.
> 12
> XZL
> June 24,2025,
> EUR
> TOP1200
> REVERSION_AND_MOMENTUM
> 1.9
> 1.24
> 0.1169
> 0.2748
> 0.000851
> 0.1475
> 0.5464
> EUR/DI/FUNDAMENTAL
> 11:21 a.m_
> 13
> VZK
> June 23,2025,
> EUR
> TOP2500
> REVERSION_AND_MOMENTUM
> 2.84
> 1.93
> 0.0891
> 0.1934
> 0.
> 000921
> 3
> 0.2897
> 0.6931
> EURIDIIMODEL
> 1:20 p.m。
> 14
> PzjC
> June 23,2025,
> EUR
> TOP2500
> REVERSION_AND_MOMENTUM
> 2.61
> 2.04
> 0814
> 0.1327
> 0.001227
> 0.9929
> 0.9929
> EUR/DIIMODEL
> 1:26 p.m。
> Showing
> to 10 of 169 entries
> 17


待完善：主页上也可以放一些数据类的内容，目前是简单设计了一下，图中数据均为随机填写，后面可以通过brain api获取。


> [!NOTE] [图片 OCR 识别内容]
> 主页
> Hore
> 主页
> Submit
> Totol
> ReVenUe
> This Month
> GeniUs
> This qucrter
> 六维数据
> Today
> 114
> 5541
> Gold
> Operators per Alpha
> 5.58
> 12% increase
> 8% IICreJse
> 12go  decrease
> Operators used
> Field per Alpha
> 2.22
> Fields used
> 110
> Base payment ITodoy
> Community activity
> 66.6
> Max simulation streak
> Budget Report
> ThIs Montn
> IIIC
> Budget
> Atual Spenclmg
> SUILS
> Administration
> Warkeung
> Sep
> Sep
> 2Sep
> 24 Sep
> Rybase
> S4base
> Recent Payment
> TodGy
> Inlormdtion Techlology
> Ooeloprrint
> chtrics per page
> SCalch
> LLSIIITICI
> Suppor
> date
> RA payment
> SA payment
> Total
> 2025.07-14
> 1.14
> 5.14
> 56.23
> 2025-07-13
> 1.11
> 5,14
> 56.38
> Website Traffic
> ToOq
> 2025-07-12
> 114
> 5,14
> 56.23
> 2025-07-11
> 1.14
> 5.14
> 56.23
> SPJIoh
> Engine
> Iirerl
> Lrmall
> Uion As
> Wideo Ads
> 2025.07.10
> 1.1
> 5.14
> 56.23
> Showirg
> OU5enrles
> Sep


以上就是本文的全部内容啦，觉得有用的话还麻烦点个小赞啦~也希望大佬们提供些思路，这个系统中还能填充进哪些实用内容！

**顾问 JX79797 (Rank 9) 的解答与建议**:
先点赞 再评论 太强了

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---

### 技术对话片段 72 (原帖: 全局变量保存调度器实例_scheduler = Nonedef start_scheduler():    global _scheduler    避免在 reloader 进程中启动调度器，避免启动两次    if os.environ.get('RUN_MAIN') == 'true':        print("This is the reloader process. Scheduler not started.")        return    if _scheduler is not None:        print("Scheduler already running.")        return    _scheduler = BackgroundScheduler()    from app01.utils.util_funcs import count_perHour    每小时整点运行一次任务    _scheduler.add_job(        count_perHour,        'cron',        minute=0  整点执行    )    _scheduler.start()    print("Scheduler started and will run every hour at :00"))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 打造自己的BrainAdmin用手机也能管理回测代码运行经验分享_33454849256599.md
- **时间**: 1年前

**提问/主帖背景 (HW93328)**:
# 1.前言

想要制作这个BrainAdmin的原因：1.登录云服务器非常卡（可能是配置低的原因），每次想查看代码运行情况都要被硬控好久。2.在手边没有电脑或者懒得打开电脑的场景下，通过ipad/手机就可以对模板的回测运行进行管理，非常灵活方便。3.将其他一些功能代码集成到系统中，方便使用和管理。

接下来会对系统功能进行逐一介绍，我最看重的还是在ipad和手机上也能进行操作，在没有电脑的场景下还是非常方便的。

ipad端


> [!NOTE] [图片 OCR 识别内容]
> 18:55
> 7月14日周
> 0100%
> L7BrainAdmin
> KAnderson
> 运行日志查看
> 在下方输入要查看的L08文件名称 (ex:tmpz)
> 日志信息已成功获取
> 日志名称
> 请输入日志名称
> 提交
> 日志内容
> tmpz.log
> 总行数:  3476行
> 当前展示:
> 1000 行 (仅展示最新1000行)
> Simulating for alpha:
> LL2 region: USA,
> universe: TOP3OO0, decay: 3,
> 1
> Simulating for alpha:
> region: USA, universe: TOP3000, decay: 3, delay:
> Alpha 7IkLX3L properties updated successfully!
> Alpha GgqW3XQ properties updated successfully!
> _
> simulation_progress_url: https:/lapi.worldquantbrain.com/simulationsl
> Alpha L3PMXra properties updated successfully!
> Alpha gLYeoGQ properties updated successfully!
> simulation_progress_url completed! https:Ilapi.worldquantbrain.comlsimulations;
> Alpha 7IkLXrO properties updated successfully!
> Ih3 LOVNIL OI nrnnortioc IInrltor
> CIICCOCCfIIIIII
>  3C'
> delay:
> Tag:
> Tag:
> 1-_
> Tag:
> Tag:
> Tag:


手机端


> [!NOTE] [图片 OCR 识别内容]
> 18:54
> 0
> 三
> template2
> Region
> Universe
> dataset
> njobs
> template_name
> Password
> 开启
> 停止
> 正在运行


整个系统看起来还是比较粗糙的，毕竟是自用嘛，很多细节上都是本着能用就行的程度哈哈哈，也希望有开发经验的大佬能够提出指点（手动抱拳~）

# 2.模板回测管理功能介绍

首先来介绍构建这个系统的初衷，用来管理回测代码运行的部分，接下来的展示为了方便都以PC网页为例。

整个模板管理页面可以分为三个部分：


> [!NOTE] [图片 OCR 识别内容]
> LTBrainAdmin
> Search
> K Anderson
> 品  主页
> 模板管理
> Home
> 模板管理
> 冒  实用工具
> templatez
> step2
> alpha提交
> Region
> Universe
> dataset
> stepl_name
> alpha Check
> USA
> TOP3000
> maCro4
> PAGES
> 模板运行管理
> njobs
> njobs
> 模板曰志查询
> template_name
> template_name
> 已提交列表
> tmp2
> Password
> 开启
> 停止
> 未运行
> 开启
> 停止
> 正在运行
> 回测数量(每小时统计)
> template8
> 1200
> Region
> Universe
> 1,000
> 800
> Catasetl
> datasetz
> 600
> 400
> njobs
> 200
> 27,00
> 22.00
> 11.02
> 15.00
> 16.00
> 20.59
> 2100
> template_name
> Password
> 模板信息
> 开启
> 停止
> 未运行
> 讨
> template_
> hame
> status
> description
> tmp2
> tmp8
> templateg
> step2
> [TT
> !
>  | + +


①.左侧一列是模板启动/关闭 管理面板

启动模板进行回测：在表单中填入Region、Universe、dataset等参数，点击开启，该回测程序就会在后端启动起来，当然这里需要填入的参数也因程序和模板的不同而需因人而异。

后端启动回测程序的代码如下：

```
# 每次运行前清空日志with open('tmp2.log', 'w') as f:    pass  # 启动一个子进程运行回测程序，并且传入所需参数process = subprocess.Popen(['python', 'templates2.py', region, universe, dataset, njobs],stdout=open('tmp2.log','a'), stderr=subprocess.STDOUT)print(f"PID of tmp2: {process.pid}")# 保存该程序对应的进程template_processes['tmp2'] = process# 更新Template表中的状态Template.objects.filter(template_name=template_name).update(status=1)
```

点击停止，后端会根据找到对应的子进程关闭，并发送关闭成功的通知


> [!NOTE] [图片 OCR 识别内容]
> WxPusher消息推送平台
> 来源: Wqb提醒
> 时间:
> 2025-07-1416.38.38
> 链接:
> 怠击查看
> tmp2 已暂停


推送信息相关的代码在论坛中也有大佬分享过，有兴趣可以搜索一下~

②.模板状态信息

这个数据表中保存了所有模板的信息，方便确认当前模板的运行状态

③.统计每小时的回测数量

在这个系统中设置了一个定时任务，每到整点时就触发函数获取上一个小时的回测数量，若是连续三个小时的回测数量都是0，则会发送通知警告回测数量的异常（时间宝贵！）

获取数量的代码之后放在评论区中。

模板日志查看功能：

该功能可以方便通过网页随时查看回测程序的运行情况


> [!NOTE] [图片 OCR 识别内容]
> 18:55
> 7月14日周
> 0100%
> L7BrainAdmin
> KAnderson
> 运行日志查看
> 在下方输入要查看的L08文件名称 (ex:tmpz)
> 日志信息已成功获取
> 日志名称
> 请输入日志名称
> 提交
> 日志内容
> tmpz.log
> 总行数:  3476行
> 当前展示:
> 1000 行 (仅展示最新1000行)
> Simulating for alpha:
> LL2 region: USA,
> universe: TOP3OO0, decay: 3,
> 1
> Simulating for alpha:
> region: USA, universe: TOP3000, decay: 3, delay:
> Alpha 7IkLX3L properties updated successfully!
> Alpha GgqW3XQ properties updated successfully!
> _
> simulation_progress_url: https:/lapi.worldquantbrain.com/simulationsl
> Alpha L3PMXra properties updated successfully!
> Alpha gLYeoGQ properties updated successfully!
> simulation_progress_url completed! https:Ilapi.worldquantbrain.comlsimulations;
> Alpha 7IkLXrO properties updated successfully!
> Ih3 LOVNIL OI nrnnortioc IInrltor
> CIICCOCCfIIIIII
>  3C'
> delay:
> Tag:
> Tag:
> 1-_
> Tag:
> Tag:
> Tag:


# 3.其他功能介绍

一、输入alpha_id 就可以进行提交alpha，省去在网页上等待的时间~


> [!NOTE] [图片 OCR 识别内容]
> BrainAdmin
> Search
> 器  主页
> alpha提交
> Home
> alpha提交
> 实用工具
> alpha 提交
> alpha提交
> 在下方输入alpha_id进行alpha的提交~
> alpha Check
> Alpha ID
> PAGES
> 请输入 alpha_id
> 模板运行管理
> 模板日志查询
> 提交
> 已提交列表


二、在这个系统中我获取了已提交因子，将其信息放在表中方便进行数据分析。当然也可以再做一个表格，获取一些满足条件的unsubmitted 因子，方便进行筛选。


> [!NOTE] [图片 OCR 识别内容]
> LTBrainAdmin
> Search
> K.Anderson
> 器  主页
> Data Tables
> Home
> Tables
> Submitted alphas Data
> 实用工具
> 已提交alpha数据列表
> PAGES
> 模板运行管理
> 刷新数据
> 模板日志查询
> 10
> entries per page
> Search。
> 已提交列表
> alpha_id
> date_submitted
> Code
> region
> universe
> neutralization
> sharpe
> fitness
> returns
> turnover
> margin
> Ops_counts
> self_cor
> prod_cor
> pyramid
> AzXk
> June 29,2025,
> GLB
> MINVOLIM
> SUBINDUSTRY
> 1.27
> 1.28
> 0.1263
> 0.0143
> 0.017721
> 3
> 0.4226
> 0.5598
> GLB/DI/FUNDAMENTAL
> 1:12pm。
> VzaC
> June 28,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.58
> 0.97
> 0.0467
> 085
> 0.001098
> 0.2347
> 0.
> .4222
> GLB/DI/FUNDAMENTAL
> 11:07a.m。
> LZNN -
> July 1,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.65
> 1.29
> 0.1177
> 0.1926
> 0.001222
> 3
> .9965
> 0.9965
> GLB/DI/FUNDAMENTAL
> 11:05am.
> SGb匕
> June 28,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.65
> 1.31
> 0.1175
> 0.
> 1853
> 0.
> 001267
> 0.2216
> 0.5679
> GLB/DI/FUNDAMENTAL
> 10:30a.m.
> 3PXg:
> June 30,2025,
> GLB
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.44
> 1.32
> 0.2133
> 0.2535
> 0.001683
> 0.5823
> 0.5823
> GLB/DI/FUNDAMENTAL
> 9:27a.m。
> 10
> 3PRA
> June 27,2025,
> EUR
> TOP2500
> REVERSION_AND_MOMENTUM
> 2.26
> 1.63
> 0.0714
> 0.1367
> 0.001045
> 3
> 0.4927
> 0.8199
> EURIDIIMODEL
> 8:22a.m.
> 11
> OZF
> June 26,2025,
> USA
> TOP3000
> REVERSION_AND_MOMENTUM
> 1.49
> 0.95
> 0.0511
> 0.0585
> 0.001747
> 3
> 0.4687
> 0.9995
> USAIDIIMODEL
> 10:09a.m.
> 12
> XZL
> June 24,2025,
> EUR
> TOP1200
> REVERSION_AND_MOMENTUM
> 1.9
> 1.24
> 0.1169
> 0.2748
> 0.000851
> 0.1475
> 0.5464
> EUR/DI/FUNDAMENTAL
> 11:21 a.m_
> 13
> VZK
> June 23,2025,
> EUR
> TOP2500
> REVERSION_AND_MOMENTUM
> 2.84
> 1.93
> 0.0891
> 0.1934
> 0.
> 000921
> 3
> 0.2897
> 0.6931
> EURIDIIMODEL
> 1:20 p.m。
> 14
> PzjC
> June 23,2025,
> EUR
> TOP2500
> REVERSION_AND_MOMENTUM
> 2.61
> 2.04
> 0814
> 0.1327
> 0.001227
> 0.9929
> 0.9929
> EUR/DIIMODEL
> 1:26 p.m。
> Showing
> to 10 of 169 entries
> 17


待完善：主页上也可以放一些数据类的内容，目前是简单设计了一下，图中数据均为随机填写，后面可以通过brain api获取。


> [!NOTE] [图片 OCR 识别内容]
> 主页
> Hore
> 主页
> Submit
> Totol
> ReVenUe
> This Month
> GeniUs
> This qucrter
> 六维数据
> Today
> 114
> 5541
> Gold
> Operators per Alpha
> 5.58
> 12% increase
> 8% IICreJse
> 12go  decrease
> Operators used
> Field per Alpha
> 2.22
> Fields used
> 110
> Base payment ITodoy
> Community activity
> 66.6
> Max simulation streak
> Budget Report
> ThIs Montn
> IIIC
> Budget
> Atual Spenclmg
> SUILS
> Administration
> Warkeung
> Sep
> Sep
> 2Sep
> 24 Sep
> Rybase
> S4base
> Recent Payment
> TodGy
> Inlormdtion Techlology
> Ooeloprrint
> chtrics per page
> SCalch
> LLSIIITICI
> Suppor
> date
> RA payment
> SA payment
> Total
> 2025.07-14
> 1.14
> 5.14
> 56.23
> 2025-07-13
> 1.11
> 5,14
> 56.38
> Website Traffic
> ToOq
> 2025-07-12
> 114
> 5,14
> 56.23
> 2025-07-11
> 1.14
> 5.14
> 56.23
> SPJIoh
> Engine
> Iirerl
> Lrmall
> Uion As
> Wideo Ads
> 2025.07.10
> 1.1
> 5.14
> 56.23
> Showirg
> OU5enrles
> Sep


以上就是本文的全部内容啦，觉得有用的话还麻烦点个小赞啦~也希望大佬们提供些思路，这个系统中还能填充进哪些实用内容！

**顾问 JX79797 (Rank 9) 的解答与建议**:
先点赞 再评论 太强了

**#========= WORLDQUANT BRAIN CONSULTANT ========== #**

**# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%**

**# sys.setrecursionlimit(α∞)**

**# PnL = ∑(Robustness * Creativity)**

**#无限探索、鲁棒性优先，创新性增值**

**#=================奋进的小徐=======================#**


---
